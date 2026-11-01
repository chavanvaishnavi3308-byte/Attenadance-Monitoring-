/**
 * Automated Test Suite for AttendX Firebase Cloud Integration
 */

const fs = require('fs');
const path = require('path');

console.log("============================================================");
console.log("RUNNING ATTENDX FIREBASE CLOUD INTEGRATION TEST SUITE");
console.log("============================================================");

// 1. Setup Mock DOM Environment
const mockLocalStorage = {
  store: {},
  getItem(key) { return this.store[key] || null; },
  setItem(key, val) { this.store[key] = String(val); },
  removeItem(key) { delete this.store[key]; },
  clear() { this.store = {}; }
};

global.window = {
  addEventListener: () => {},
  navigator: { onLine: true },
  SEED_DATA: null
};
global.localStorage = mockLocalStorage;
global.sessionStorage = mockLocalStorage;
global.navigator = { onLine: true };

// Mock Firebase SDK compat
const mockFirestoreData = {
  attendance_sessions: {},
  students: {},
  notifications: {},
  messages: {}
};

global.window.firebase = {
  apps: [],
  initializeApp(config) {
    const app = { name: "[DEFAULT]", options: config };
    this.apps.push(app);
    return app;
  },
  app() { return this.apps[0]; },
  firestore: Object.assign(function() {
    return {
      enablePersistence: async () => true,
      batch: () => ({
        set: (ref, data) => { mockFirestoreData[ref.col][ref.id] = data; },
        commit: async () => true
      }),
      collection: (colName) => ({
        colName,
        doc: (docId) => ({
          col: colName,
          id: docId,
          set: async (data) => {
            if (!mockFirestoreData[colName]) mockFirestoreData[colName] = {};
            mockFirestoreData[colName][docId] = data;
            return true;
          }
        }),
        where: () => ({
          onSnapshot: (cb) => {
            cb([]);
            return () => {};
          }
        }),
        onSnapshot: (cb) => {
          cb([]);
          return () => {};
        }
      })
    };
  }, {
    FieldValue: {
      serverTimestamp: () => new Date().toISOString()
    }
  })
};

// 2. Load Seed Data
eval(fs.readFileSync('js/data.js', 'utf-8'));
console.log("[Test 1/5] Loaded SEED_DATA successfully. CS Students:", window.SEED_DATA.students.filter(s => s.classId === 'CS').length);

// 3. Load Firebase Config Module
eval(fs.readFileSync('js/firebase-config.js', 'utf-8'));
const fbConfig = window.AttendXFirebaseConfig.get();
if (fbConfig && fbConfig.projectId === "attendx-smart-campus") {
  console.log("[Test 2/5] AttendXFirebaseConfig loaded default template successfully:", fbConfig.projectId);
} else {
  throw new Error("Failed to load Firebase Config!");
}

// 4. Load Firebase Service Module & Init
eval(fs.readFileSync('js/firebase-service.js', 'utf-8'));
window.firebaseService.init().then(async (connected) => {
  if (!connected) throw new Error("FirebaseService.init failed!");
  console.log("[Test 3/5] FirebaseService connected to mock Cloud Firestore successfully!");

  // 5. Load Store Module
  eval(fs.readFileSync('js/store.js', 'utf-8'));
  const store = window.attendxStore;
  console.log("[Test 4/5] Store initialized. Total accounts:", store.getAccounts().length);

  // 6. Test Roster Session Commit with Cloud Sync
  const testDate = "2026-10-30";
  const testStatusMap = {
    "STD-CS01": "absent",
    "STD-CS02": "present"
  };

  const savedRecord = store.saveAttendance("CS", "SUB-CS01", testDate, testStatusMap, "Prof. Swapnali Jadhav");
  const alertsSent = store.notifyParentsForSession("CS", "SUB-CS01", testDate, testStatusMap);

  // Allow async promises to resolve
  await new Promise(r => setTimeout(r, 200));

  console.log("[Test 5/5] Attendance Session committed & alerts generated:");
  console.log("  - Local Attendance Records count:", store.getAttendanceRecords().length);
  console.log("  - Cloud attendance_sessions count:", Object.keys(mockFirestoreData.attendance_sessions).length);
  console.log("  - Cloud notifications count:", Object.keys(mockFirestoreData.notifications).length);
  console.log("  - Cloud students updated count:", Object.keys(mockFirestoreData.students).length);

  if (Object.keys(mockFirestoreData.attendance_sessions).length >= 1 &&
      Object.keys(mockFirestoreData.notifications).length >= 1) {
    console.log("============================================================");
    console.log("SUCCESS: ALL 5 FIREBASE INTEGRATION TESTS PASSED!");
    console.log("============================================================");
  } else {
    throw new Error("Cloud data sync assertion failed!");
  }
}).catch(err => {
  console.error("TEST FAILED:", err);
  process.exit(1);
});

