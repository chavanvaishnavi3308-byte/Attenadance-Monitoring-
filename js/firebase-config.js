/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Firebase Cloud Configuration & Initialization Module
 *
 * Provides persistent configuration management with localStorage support,
 * allowing instant connection to Google Firebase Cloud Firestore.
 */

(function (window) {
  "use strict";

  const STORAGE_KEY_FIREBASE = "attendx_firebase_config";

  // Default / Demo Firebase Configuration template
  // Users can replace these values or paste their own credentials via the Cloud Settings modal in the UI.
  const DEFAULT_FIREBASE_CONFIG = {
    apiKey: "AIzaSyDemo-AttendXSmartCampusAttendanceKey",
    authDomain: "attendx-smart-campus.firebaseapp.com",
    projectId: "attendx-smart-campus",
    storageBucket: "attendx-smart-campus.appspot.com",
    messagingSenderId: "109827364521",
    appId: "1:109827364521:web:a9b8c7d6e5f40123"
  };

  /**
   * Retrieves the active Firebase configuration.
   * Priority: LocalStorage saved configuration -> Default template configuration.
   */
  function getFirebaseConfig() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY_FIREBASE);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed && parsed.projectId) {
          return parsed;
        }
      }
    } catch (e) {
      console.warn("AttendX Firebase: Could not parse saved config, using default template.", e);
    }
    return { ...DEFAULT_FIREBASE_CONFIG };
  }

  /**
   * Saves a custom Firebase configuration to localStorage.
   * @param {Object} config
   */
  function saveFirebaseConfig(config) {
    if (!config || !config.projectId) {
      throw new Error("Invalid Firebase configuration: projectId is required.");
    }
    localStorage.setItem(STORAGE_KEY_FIREBASE, JSON.stringify(config));
    console.log("AttendX Firebase: Configuration saved to localStorage.");
  }

  /**
   * Clears any saved custom Firebase configuration, restoring defaults.
   */
  function resetFirebaseConfig() {
    localStorage.removeItem(STORAGE_KEY_FIREBASE);
    console.log("AttendX Firebase: Configuration reset to default template.");
  }

  /**
   * Checks if Firebase SDK is loaded on window.
   */
  function isFirebaseSDKAvailable() {
    return typeof window.firebase !== "undefined" && typeof window.firebase.initializeApp === "function";
  }

  // Export to window
  window.AttendXFirebaseConfig = {
    get: getFirebaseConfig,
    save: saveFirebaseConfig,
    reset: resetFirebaseConfig,
    isSDKAvailable: isFirebaseSDKAvailable,
    defaultConfig: DEFAULT_FIREBASE_CONFIG
  };
})(window);

