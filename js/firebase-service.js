/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Firebase Cloud Firestore Service Module
 *
 * Implements real-time cloud data synchronization, live parental push
 * notifications, and real-time parent-counselor messaging via Google Cloud Firestore.
 */

(function (window) {
  "use strict";

  class FirebaseService {
    constructor() {
      this.app = null;
      this.db = null;
      this.isConnected = false;
      this.isOnline = navigator.onLine;
      this.lastSyncTime = null;
      this.error = null;
      this.listeners = [];

      // Monitor network online/offline transitions
      window.addEventListener("online", () => {
        this.isOnline = true;
        console.log("AttendX Firebase: Network status changed to ONLINE");
      });
      window.addEventListener("offline", () => {
        this.isOnline = false;
        console.log("AttendX Firebase: Network status changed to OFFLINE");
      });
    }

    /**
     * Initializes Firebase App and Firestore instance using AttendXFirebaseConfig.
     */
    async init() {
      if (!window.AttendXFirebaseConfig || !window.AttendXFirebaseConfig.isSDKAvailable()) {
        this.isConnected = false;
        this.error = "Firebase SDK not loaded on window.";
        console.warn("AttendX Firebase Service: Firebase SDK is not loaded. Operating in local fallback mode.");
        return false;
      }

      try {
        const config = window.AttendXFirebaseConfig.get();
        if (!config || !config.projectId) {
          throw new Error("Missing projectId in Firebase configuration.");
        }

        // Initialize or reuse existing app
        if (!window.firebase.apps.length) {
          this.app = window.firebase.initializeApp(config);
        } else {
          this.app = window.firebase.app();
        }

        this.db = window.firebase.firestore();

        // Enable offline persistence if supported in browser
        try {
          // Enable offline cache if not already enabled
          await this.db.enablePersistence({ synchronizeTabs: true });
          console.log("AttendX Firebase: Multi-tab offline persistence enabled.");
        } catch (persErr) {
          if (persErr.code === "failed-precondition") {
            // Multiple tabs open simultaneously, persistence can only be enabled in one tab at a time.
            console.log("AttendX Firebase: Offline persistence active in another tab.");
          } else if (persErr.code === "unimplemented") {
            // Browser doesn't support all required features
            console.log("AttendX Firebase: Offline persistence not supported by this browser.");
          }
        }

        this.isConnected = true;
        this.lastSyncTime = new Date().toISOString();
        this.error = null;
        console.log(`AttendX Firebase: Successfully connected to Project [${config.projectId}]`);
        return true;
      } catch (err) {
        this.isConnected = false;
        this.error = err.message || "Failed to initialize Firebase Firestore.";
        console.warn("AttendX Firebase Service Initialization Notice:", this.error);
        return false;
      }
    }

    /**
     * Retrieves current operational status of the cloud database connection.
     */
    getStatus() {
      const config = window.AttendXFirebaseConfig ? window.AttendXFirebaseConfig.get() : null;
      return {
        isConnected: this.isConnected,
        isOnline: this.isOnline,
        projectId: config ? config.projectId : "None",
        lastSyncTime: this.lastSyncTime,
        error: this.error
      };
    }

    /**
     * Asynchronously syncs an attendance session record to Firestore collection `attendance_sessions`.
     * @param {Object} session
     */
    async syncSessionToCloud(session) {
      if (!this.isConnected || !this.db) {
        return false;
      }
      try {
        const docId = session.id || `SES-${Date.now()}`;
        await this.db.collection("attendance_sessions").doc(docId).set({
          ...session,
          syncedAt: window.firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        this.lastSyncTime = new Date().toISOString();
        console.log(`AttendX Firebase: Session [${docId}] synced to cloud.`);
        return true;
      } catch (err) {
        console.warn("AttendX Firebase: Could not sync session to cloud:", err.message);
        return false;
      }
    }

    /**
     * Batch updates student records in Firestore collection `students`.
     * @param {Array} studentsList
     */
    async syncStudentsToCloud(studentsList) {
      if (!this.isConnected || !this.db || !Array.isArray(studentsList)) {
        return false;
      }
      try {
        const batch = this.db.batch();
        studentsList.forEach(student => {
          if (student && student.id) {
            const ref = this.db.collection("students").doc(student.id);
            batch.set(ref, {
              ...student,
              updatedAt: window.firebase.firestore.FieldValue.serverTimestamp()
            }, { merge: true });
          }
        });

        await batch.commit();
        this.lastSyncTime = new Date().toISOString();
        console.log(`AttendX Firebase: Successfully batch-synced ${studentsList.length} students to cloud.`);
        return true;
      } catch (err) {
        console.warn("AttendX Firebase: Could not batch-sync students to cloud:", err.message);
        return false;
      }
    }

    /**
     * Dispatches a real-time notification alert to Firestore collection `notifications`.
     * @param {Object} notifData
     */
    async dispatchCloudNotification(notifData) {
      if (!this.isConnected || !this.db) {
        return false;
      }
      try {
        const docId = notifData.id || `NOTIF-${Date.now()}`;
        await this.db.collection("notifications").doc(docId).set({
          ...notifData,
          createdAt: window.firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        console.log(`AttendX Firebase: Notification [${docId}] dispatched to cloud.`);
        return true;
      } catch (err) {
        console.warn("AttendX Firebase: Could not dispatch cloud notification:", err.message);
        return false;
      }
    }

    /**
     * Subscribes to real-time notification alerts via Firestore `onSnapshot`.
     * Enables parents to receive live absence alerts on another device instantly.
     * @param {String|null} studentId - Filter for specific student, or null for all.
     * @param {Function} callback - Triggered with incoming notifications array.
     * @returns {Function} Unsubscribe function.
     */
    listenToCloudNotifications(studentId, callback) {
      if (!this.isConnected || !this.db) {
        return () => {};
      }

      try {
        let query = this.db.collection("notifications");
        if (studentId) {
          query = query.where("studentId", "==", studentId);
        }

        const unsubscribe = query.onSnapshot(snapshot => {
          const notifs = [];
          snapshot.forEach(doc => {
            notifs.push({ id: doc.id, ...doc.data() });
          });
          callback(notifs);
        }, err => {
          console.warn("AttendX Firebase: Notification snapshot listener error:", err.message);
        });

        this.listeners.push(unsubscribe);
        return unsubscribe;
      } catch (err) {
        console.warn("AttendX Firebase: Error setting up notification listener:", err.message);
        return () => {};
      }
    }

    /**
     * Dispatches a counseling chat message to Firestore collection `messages`.
     * @param {Object} messageData
     */
    async sendCloudMessage(messageData) {
      if (!this.isConnected || !this.db) {
        return false;
      }
      try {
        const docId = messageData.id || `MSG-${Date.now()}`;
        await this.db.collection("messages").doc(docId).set({
          ...messageData,
          sentAt: window.firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });

        console.log(`AttendX Firebase: Chat message [${docId}] synced to cloud.`);
        return true;
      } catch (err) {
        console.warn("AttendX Firebase: Could not send cloud message:", err.message);
        return false;
      }
    }

    /**
     * Subscribes to real-time parent-counselor messages via Firestore `onSnapshot`.
     * @param {String} studentId
     * @param {Function} callback
     * @returns {Function} Unsubscribe function.
     */
    listenToCloudMessages(studentId, callback) {
      if (!this.isConnected || !this.db) {
        return () => {};
      }

      try {
        const query = this.db.collection("messages").where("studentId", "==", studentId);
        const unsubscribe = query.onSnapshot(snapshot => {
          const msgs = [];
          snapshot.forEach(doc => {
            msgs.push({ id: doc.id, ...doc.data() });
          });
          callback(msgs);
        }, err => {
          console.warn("AttendX Firebase: Messages snapshot listener error:", err.message);
        });

        this.listeners.push(unsubscribe);
        return unsubscribe;
      } catch (err) {
        console.warn("AttendX Firebase: Error setting up messages listener:", err.message);
        return () => {};
      }
    }

    /**
     * Uploads the full baseline SEED dataset to Firebase Cloud Firestore.
     * Useful for one-click initial setup of cloud database.
     * @param {Object} seed
     */
    async seedCloudDatabase(seed) {
      if (!this.isConnected || !this.db) {
        throw new Error("Cannot seed: Firebase Cloud Database is not connected.");
      }

      const SEED = seed || window.SEED_DATA;
      if (!SEED) {
        throw new Error("SEED_DATA not found.");
      }

      console.log("AttendX Firebase: Committing initial SEED dataset to Cloud Firestore...");

      // 1. Seed Accounts
      if (Array.isArray(SEED.accounts)) {
        const accBatch = this.db.batch();
        SEED.accounts.forEach(acc => {
          const ref = this.db.collection("accounts").doc(acc.id);
          accBatch.set(ref, acc, { merge: true });
        });
        await accBatch.commit();
      }

      // 2. Seed Students
      if (Array.isArray(SEED.students)) {
        const stdBatch = this.db.batch();
        SEED.students.forEach(std => {
          const ref = this.db.collection("students").doc(std.id);
          stdBatch.set(ref, std, { merge: true });
        });
        await stdBatch.commit();
      }

      // 3. Seed Teachers
      if (Array.isArray(SEED.teachers)) {
        const tchBatch = this.db.batch();
        SEED.teachers.forEach(tch => {
          const ref = this.db.collection("teachers").doc(tch.id);
          tchBatch.set(ref, tch, { merge: true });
        });
        await tchBatch.commit();
      }

      // 4. Seed Departments & Classes
      if (Array.isArray(SEED.departments)) {
        const deptBatch = this.db.batch();
        SEED.departments.forEach(dept => {
          const ref = this.db.collection("departments").doc(dept.id);
          deptBatch.set(ref, dept, { merge: true });
        });
        await deptBatch.commit();
      }

      this.lastSyncTime = new Date().toISOString();
      console.log("AttendX Firebase: Cloud Firestore successfully populated with seed data!");
      return true;
    }
  }

  // Export singleton service instance
  window.firebaseService = new FirebaseService();
})(window);

