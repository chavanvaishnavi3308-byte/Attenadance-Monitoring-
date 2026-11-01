/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Reactive State Management & Centralized Storage Controller
 * 
 * Central Data Authority:
 * - Admin: Dr. Vidya Mohod Ma’am
 * - Teachers (6): Swapnali Jadhav, Anuja Kanawade, Srushti Parab, Trupti Thakur, Sneha Mokal / Mali, Chaitrali Naik
 * - Parent: Rajaram Chavan (Student: Vaishnavi Chavan, Dept: Computer Science CS)
 * - Departments (2): CS, IT
 * - Classes (2): CS, IT
 * - Students (15): 10 CS, 5 IT
 */

class Store {
  constructor() {
    this.STORAGE_KEYS = {
      VERSION: "attendx_v2_version",
      CURRENT_USER: "attendx_v2_currentUser",
      ACCOUNTS: "attendx_v2_accounts",
      STUDENTS: "attendx_v2_students",
      TEACHERS: "attendx_v2_teachers",
      DEPARTMENTS: "attendx_v2_departments",
      CLASSES: "attendx_v2_classes",
      SUBJECTS: "attendx_v2_subjects",
      ATTENDANCE: "attendx_v2_attendance",
      NOTIFICATIONS: "attendx_v2_notifications",
      MESSAGES: "attendx_v2_messages",
      HOLIDAYS: "attendx_v2_holidays"
    };

    this.listeners = {};
    this.init();
  }

  // Initialize store with fresh data seeds, clearing any stale v1 keys
  init() {
    try {
      const currentVersion = localStorage.getItem(this.STORAGE_KEYS.VERSION);
      const SEED = window.SEED_DATA;
      if (!SEED) {
        console.warn("AttendX: SEED_DATA not yet loaded on window.");
        return;
      }

      // Upgrade / Reset if version is not 2.0
      if (currentVersion !== "2.0") {
        console.log("AttendX: Upgrading dataset to v2.0 (Dr. Vidya Mohod Ma’am, CS & IT departments)");
        // Clear old keys
        Object.keys(localStorage).forEach(key => {
          if (key.startsWith("attendx_v1_")) {
            localStorage.removeItem(key);
          }
        });

        localStorage.setItem(this.STORAGE_KEYS.VERSION, "2.0");
        localStorage.setItem(this.STORAGE_KEYS.ACCOUNTS, JSON.stringify(SEED.accounts || []));
        localStorage.setItem(this.STORAGE_KEYS.STUDENTS, JSON.stringify(SEED.students));
        localStorage.setItem(this.STORAGE_KEYS.TEACHERS, JSON.stringify(SEED.teachers));
        localStorage.setItem(this.STORAGE_KEYS.DEPARTMENTS, JSON.stringify(SEED.departments));
        localStorage.setItem(this.STORAGE_KEYS.CLASSES, JSON.stringify(SEED.classes));
        localStorage.setItem(this.STORAGE_KEYS.SUBJECTS, JSON.stringify(SEED.subjects));
        localStorage.setItem(this.STORAGE_KEYS.ATTENDANCE, JSON.stringify(SEED.attendanceRecords));
        localStorage.setItem(this.STORAGE_KEYS.NOTIFICATIONS, JSON.stringify(SEED.notifications));
        localStorage.setItem(this.STORAGE_KEYS.MESSAGES, JSON.stringify(SEED.messages));
        localStorage.setItem(this.STORAGE_KEYS.HOLIDAYS, JSON.stringify(SEED.holidays));
      } else {
        // Ensure individual keys exist
        if (!localStorage.getItem(this.STORAGE_KEYS.ACCOUNTS)) {
          localStorage.setItem(this.STORAGE_KEYS.ACCOUNTS, JSON.stringify(SEED.accounts || []));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.STUDENTS)) {
          localStorage.setItem(this.STORAGE_KEYS.STUDENTS, JSON.stringify(SEED.students));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.TEACHERS)) {
          localStorage.setItem(this.STORAGE_KEYS.TEACHERS, JSON.stringify(SEED.teachers));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.DEPARTMENTS)) {
          localStorage.setItem(this.STORAGE_KEYS.DEPARTMENTS, JSON.stringify(SEED.departments));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.CLASSES)) {
          localStorage.setItem(this.STORAGE_KEYS.CLASSES, JSON.stringify(SEED.classes));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.SUBJECTS)) {
          localStorage.setItem(this.STORAGE_KEYS.SUBJECTS, JSON.stringify(SEED.subjects));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.ATTENDANCE)) {
          localStorage.setItem(this.STORAGE_KEYS.ATTENDANCE, JSON.stringify(SEED.attendanceRecords));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.NOTIFICATIONS)) {
          localStorage.setItem(this.STORAGE_KEYS.NOTIFICATIONS, JSON.stringify(SEED.notifications));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.MESSAGES)) {
          localStorage.setItem(this.STORAGE_KEYS.MESSAGES, JSON.stringify(SEED.messages));
        }
        if (!localStorage.getItem(this.STORAGE_KEYS.HOLIDAYS)) {
          localStorage.setItem(this.STORAGE_KEYS.HOLIDAYS, JSON.stringify(SEED.holidays));
        }
      }

      // Purge any accidental credential keys and ensure no plaintext passwords in storage
      this.cleanStoredCredentials();

      // Asynchronously bootstrap Firebase Cloud Integration
      setTimeout(() => this.initFirebaseIntegration(), 100);
    } catch (e) {
      console.warn("AttendX: LocalStorage access limited, running with memory fallback", e);
    }
  }

  // Remove any stray stored credentials or plaintext passwords from storage
  cleanStoredCredentials() {
    try {
      const sensitiveKeys = [
        "saved_email", "saved_password", "attendx_saved_email", "attendx_saved_password",
        "user_email", "user_password", "login_email", "login_password", "remember_email"
      ];
      sensitiveKeys.forEach(k => {
        try { localStorage.removeItem(k); } catch (e) {}
        try { sessionStorage.removeItem(k); } catch (e) {}
      });

      // Ensure no plaintext password remains in CURRENT_USER object
      const rawUser = localStorage.getItem(this.STORAGE_KEYS.CURRENT_USER);
      if (rawUser) {
        try {
          const user = JSON.parse(rawUser);
          if (user && user.password) {
            delete user.password;
            localStorage.setItem(this.STORAGE_KEYS.CURRENT_USER, JSON.stringify(user));
          }
        } catch (e) {}
      }
    } catch (e) {}
  }

  // Bootstrap Firebase Cloud Integration with real-time listeners
  async initFirebaseIntegration() {
    if (!window.firebaseService) return;
    try {
      const connected = await window.firebaseService.init();
      this.emit("firebaseStatusChanged", window.firebaseService.getStatus());

      if (connected) {
        console.log("AttendX Store: Firebase Cloud Synchronization active.");

        // Real-time listener for incoming remote notifications
        window.firebaseService.listenToCloudNotifications(null, (remoteNotifs) => {
          if (Array.isArray(remoteNotifs) && remoteNotifs.length > 0) {
            let localList = this.getItem(this.STORAGE_KEYS.NOTIFICATIONS, []);
            let hasNew = false;
            remoteNotifs.forEach(rn => {
              if (rn && rn.id && !localList.some(ln => ln.id === rn.id)) {
                localList.unshift(rn);
                hasNew = true;
              }
            });
            if (hasNew) {
              this.setItem(this.STORAGE_KEYS.NOTIFICATIONS, localList);
              this.emit("notificationsChanged", localList);
              if (typeof window.playCyberTone === "function") {
                window.playCyberTone("alert");
              }
            }
          }
        });

        // Real-time listener for remote chat messages
        window.firebaseService.listenToCloudMessages("STD-CS01", (remoteMsgs) => {
          if (Array.isArray(remoteMsgs) && remoteMsgs.length > 0) {
            let localMsgs = this.getItem(this.STORAGE_KEYS.MESSAGES, []);
            let hasNew = false;
            remoteMsgs.forEach(rm => {
              if (rm && rm.id && !localMsgs.some(lm => lm.id === rm.id)) {
                localMsgs.push(rm);
                hasNew = true;
              }
            });
            if (hasNew) {
              this.setItem(this.STORAGE_KEYS.MESSAGES, localMsgs);
              this.emit("messagesChanged", localMsgs);
            }
          }
        });
      }
    } catch (e) {
      console.warn("AttendX Store: Firebase integration notice:", e);
    }
  }

  // Event Pub/Sub
  subscribe(event, callback) {
    if (!this.listeners[event]) this.listeners[event] = [];
    this.listeners[event].push(callback);
    return () => {
      this.listeners[event] = this.listeners[event].filter(cb => cb !== callback);
    };
  }

  emit(event, data) {
    if (this.listeners[event]) {
      this.listeners[event].forEach(cb => {
        try { cb(data); } catch (err) { console.error("Event handler error:", err); }
      });
    }
  }

  // Generic Storage Helpers
  getItem(key, defaultVal = []) {
    try {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : defaultVal;
    } catch (e) {
      return defaultVal;
    }
  }

  setItem(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      console.error("LocalStorage write error:", e);
    }
  }

  // ------------------------------------
  // AUTHENTICATION & SESSION
  // ------------------------------------
  getCurrentUser() {
    try {
      const sessionUser = sessionStorage.getItem("attendx_v2_currentUser");
      if (sessionUser) return JSON.parse(sessionUser);
    } catch (e) {}
    return this.getItem(this.STORAGE_KEYS.CURRENT_USER, null);
  }

  setCurrentUser(user) {
    // Ensure no password property is ever persisted
    const safeUser = user ? { ...user } : null;
    if (safeUser && safeUser.password) delete safeUser.password;
    this.setItem(this.STORAGE_KEYS.CURRENT_USER, safeUser);
    this.emit("userChanged", safeUser);
  }

  logout() {
    try {
      sessionStorage.removeItem("attendx_v2_currentUser");
      localStorage.removeItem(this.STORAGE_KEYS.CURRENT_USER);
    } catch (e) {}
    this.emit("userChanged", null);
  }

  // ------------------------------------
  // REGISTERED ACCOUNTS (Authentication Authority)
  // ------------------------------------
  getAccounts() {
    return this.getItem(this.STORAGE_KEYS.ACCOUNTS, (window.SEED_DATA && window.SEED_DATA.accounts) ? window.SEED_DATA.accounts : []);
  }

  getAccountByProfileId(profileId) {
    if (!profileId) return null;
    const accounts = this.getAccounts();
    return accounts.find(a => a.profileId === profileId) || null;
  }

  getAccountByIdentifier(identifier, role = null) {
    if (!identifier) return null;
    const q = identifier.trim().toLowerCase();
    const accounts = this.getAccounts();
    return accounts.find(a => {
      if (role && a.role !== role) return false;
      const email = (a.email || "").toLowerCase();
      const username = (a.username || "").toLowerCase();
      const aliases = (a.aliases || []).map(x => (x || "").toLowerCase());
      return email === q || username === q || aliases.includes(q);
    }) || null;
  }

  saveAccount(accountData) {
    if (!accountData || !accountData.profileId) return null;
    let accounts = this.getAccounts();
    const index = accounts.findIndex(a => a.profileId === accountData.profileId);
    if (index >= 0) {
      accounts[index] = { ...accounts[index], ...accountData, updatedAt: new Date().toISOString() };
    } else {
      accounts.push({
        id: accountData.id || `ACC-${accountData.profileId}`,
        createdAt: new Date().toISOString(),
        status: "active",
        ...accountData
      });
    }
    this.setItem(this.STORAGE_KEYS.ACCOUNTS, accounts);
    this.emit("accountsChanged", accounts);
    return accounts.find(a => a.profileId === accountData.profileId);
  }

  deleteAccount(profileId) {
    let accounts = this.getAccounts();
    accounts = accounts.filter(a => a.profileId !== profileId);
    this.setItem(this.STORAGE_KEYS.ACCOUNTS, accounts);
    this.emit("accountsChanged", accounts);
  }

  provisionTeacherAccount(teacherId, password, status = "active") {
    const teacher = this.getTeacherById(teacherId);
    if (!teacher) throw new Error("Teacher record not found in directory.");
    if (!password || password.trim().length === 0) throw new Error("A valid password must be specified for account creation.");
    
    const accountData = {
      profileId: teacherId,
      role: "teacher",
      name: teacher.name,
      email: teacher.email,
      username: teacher.email ? teacher.email.split("@")[0] : teacherId.toLowerCase(),
      password: password.trim(),
      acceptedPasswords: [password.trim()],
      status: status
    };
    return this.saveAccount(accountData);
  }

  revokeTeacherAccount(teacherId) {
    this.deleteAccount(teacherId);
  }

  // Preset demo accounts
  getDemoAccounts() {
    return {
      admin: {
        id: "ADM-001",
        name: "Dr. Vidya Mohod Ma’am",
        role: "admin",
        email: "admin@attendx.edu",
        avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=200&q=80",
        title: "Dean of Academics & Campus Head",
        department: "Central Administration"
      },
      teacher: {
        id: "TCH-001",
        name: "Swapnali Jadhav",
        role: "teacher",
        email: "swapnali.jadhav@attendx.edu",
        avatar: "assets/avatar_teacher.jpg",
        title: "Assistant Professor, Computer Science",
        department: "Computer Science",
        assignedClass: "CS"
      },
      parent: {
        id: "PRN-001",
        name: "Rajaram Chavan",
        role: "parent",
        email: "rajaram.chavan@parent.attendx.edu",
        studentId: "STD-CS01",
        childName: "Vaishnavi Chavan",
        avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
        title: "Guardian of Vaishnavi Chavan",
        department: "Computer Science (CS)"
      },
      student: {
        id: "STD-CS01",
        name: "Vaishnavi Chavan",
        role: "student",
        email: "vaishnavi.chavan@attendx.edu",
        studentId: "STD-CS01",
        avatar: "assets/avatar_student.jpg",
        rollNo: "CS-01",
        classId: "CS",
        title: "Year 3 Undergraduate",
        department: "Computer Science"
      }
    };
  }

  // Lookup user by role, accountId, or email to support logging in as ANY student, teacher, parent, or admin
  findUser(email = "", role = "admin", accountId = "") {
    const teachers = this.getTeachers();
    const students = this.getStudents();
    const demo = this.getDemoAccounts();

    if (accountId) {
      if (role === "teacher") {
        const t = teachers.find(x => x.id === accountId);
        if (t) return { ...t, role: "teacher" };
      } else if (role === "student") {
        const s = students.find(x => x.id === accountId);
        if (s) return { ...s, role: "student", studentId: s.id };
      } else if (role === "parent") {
        const s = students.find(x => x.id === accountId);
        if (s) {
          return {
            id: "PRN-" + s.id,
            name: s.parentName || `Guardian of ${s.name}`,
            role: "parent",
            email: s.parentEmail || `${s.rollNo.toLowerCase()}.parent@attendx.edu`,
            studentId: s.id,
            childName: s.name,
            avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
            title: `Guardian of ${s.name}`,
            department: `${s.department} (${s.classId})`
          };
        }
      } else if (role === "admin") {
        return demo.admin;
      }
    }

    if (email) {
      const q = email.trim().toLowerCase();
      if (demo.admin.email.toLowerCase() === q) return demo.admin;

      const t = teachers.find(x => x.email && x.email.toLowerCase() === q);
      if (t) return { ...t, role: "teacher" };

      const s = students.find(x => (x.email && x.email.toLowerCase() === q) || (x.rollNo && x.rollNo.toLowerCase() === q));
      if (s) return { ...s, role: "student", studentId: s.id };

      const pStudent = students.find(x => (x.parentEmail && x.parentEmail.toLowerCase() === q) || (x.email && x.email.toLowerCase().includes(q)));
      if (pStudent) {
        return {
          id: "PRN-" + pStudent.id,
          name: pStudent.parentName || `Guardian of ${pStudent.name}`,
          role: "parent",
          email: q,
          studentId: pStudent.id,
          childName: pStudent.name,
          avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
          title: `Guardian of ${pStudent.name}`,
          department: `${pStudent.department} (${pStudent.classId})`
        };
      }
    }

    // Role-based fallback
    return demo[role] || demo.admin;
  }

  // ------------------------------------
  // DEPARTMENTS (Only CS & IT)
  // ------------------------------------
  getDepartments() {
    return this.getItem(this.STORAGE_KEYS.DEPARTMENTS, window.SEED_DATA.departments);
  }

  getDepartmentById(id) {
    const list = this.getDepartments();
    return list.find(d => d.id === id || d.code === id) || null;
  }

  // ------------------------------------
  // CLASSES (Only CS & IT)
  // ------------------------------------
  getClasses() {
    return this.getItem(this.STORAGE_KEYS.CLASSES, window.SEED_DATA.classes);
  }

  getClassById(id) {
    const list = this.getClasses();
    return list.find(c => c.id === id) || null;
  }

  // ------------------------------------
  // TEACHERS (Exactly 6 teachers)
  // ------------------------------------
  getTeachers() {
    return this.getItem(this.STORAGE_KEYS.TEACHERS, window.SEED_DATA.teachers);
  }

  getTeacherById(id) {
    const list = this.getTeachers();
    return list.find(t => t.id === id || t.name === id) || null;
  }

  updateTeacher(id, teacherData) {
    let list = this.getTeachers();
    list = list.map(t => (t.id === id ? { ...t, ...teacherData } : t));
    this.setItem(this.STORAGE_KEYS.TEACHERS, list);
    this.emit("teachersChanged", list);
    return list.find(t => t.id === id);
  }

  assignTeacherClass(teacherId, classId, subjectSpecialty = "") {
    let list = this.getTeachers();
    list = list.map(t => {
      if (t.id === teacherId) {
        return {
          ...t,
          assignedClass: classId,
          department: classId === "IT" ? "Information Technology" : "Computer Science",
          departmentCode: classId,
          subjectSpecialty: subjectSpecialty || t.subjectSpecialty
        };
      }
      return t;
    });
    this.setItem(this.STORAGE_KEYS.TEACHERS, list);
    this.emit("teachersChanged", list);
  }

  addTeacher(teacherData) {
    const list = this.getTeachers();
    const classId = teacherData.assignedClass === "IT" ? "IT" : "CS";
    const deptName = classId === "IT" ? "Information Technology" : "Computer Science";
    const newId = "TCH-" + (list.length + 1).toString().padStart(3, "0");

    const newTeacher = {
      id: newId,
      name: teacherData.name,
      email: teacherData.email || `${teacherData.name.toLowerCase().replace(/\s+/g, ".")}@attendx.edu`,
      role: "teacher",
      department: deptName,
      departmentCode: classId,
      assignedClass: classId,
      title: teacherData.title || (classId === "CS" ? "Assistant Professor, Computer Science" : "Assistant Professor, Information Technology"),
      subjectSpecialty: teacherData.subjectSpecialty || "Core Engineering",
      avatar: teacherData.avatar || "assets/avatar_teacher.jpg",
      ...teacherData
    };

    list.push(newTeacher);
    this.setItem(this.STORAGE_KEYS.TEACHERS, list);
    this.emit("teachersChanged", list);
    return newTeacher;
  }

  deleteTeacher(id) {
    let list = this.getTeachers();
    list = list.filter(t => t.id !== id);
    this.setItem(this.STORAGE_KEYS.TEACHERS, list);
    this.emit("teachersChanged", list);
  }

  // ------------------------------------
  // SUBJECTS
  // ------------------------------------
  getSubjects(classId = null) {
    const subjects = this.getItem(this.STORAGE_KEYS.SUBJECTS, window.SEED_DATA.subjects);
    if (!classId || classId === "ALL") return subjects;
    return subjects.filter(s => s.classId === classId);
  }

  // ------------------------------------
  // STUDENTS CRUD & SEARCH/FILTER
  // ------------------------------------
  getStudents(classFilter = "ALL", query = "", statusFilter = "ALL") {
    let list = this.getItem(this.STORAGE_KEYS.STUDENTS, window.SEED_DATA.students);

    // Filter by class (CS or IT)
    if (classFilter && classFilter !== "ALL") {
      list = list.filter(s => s.classId === classFilter || s.departmentCode === classFilter);
    }

    // Filter by attendance status
    if (statusFilter === "warning") {
      list = list.filter(s => s.overallAttendance < 75);
    } else if (statusFilter === "regular") {
      list = list.filter(s => s.overallAttendance >= 75);
    }

    // Search query matches: student name, roll number, email, class, parent name, or subject teacher
    if (query && query.trim() !== "") {
      const q = query.toLowerCase().trim();
      list = list.filter(s => {
        const nameMatch = s.name.toLowerCase().includes(q);
        const rollMatch = s.rollNo.toLowerCase().includes(q);
        const emailMatch = s.email.toLowerCase().includes(q);
        const classMatch = s.classId.toLowerCase().includes(q);
        const parentMatch = s.parentName && s.parentName.toLowerCase().includes(q);
        const subjectTeacherMatch = s.subjects && s.subjects.some(sub => sub.teacher && sub.teacher.toLowerCase().includes(q));
        return nameMatch || rollMatch || emailMatch || classMatch || parentMatch || subjectTeacherMatch;
      });
    }

    return list;
  }

  getStudentById(id) {
    const list = this.getStudents();
    return list.find(s => s.id === id || s.rollNo === id) || null;
  }

  addStudent(studentData) {
    const list = this.getStudents();
    const classId = studentData.classId === "IT" ? "IT" : "CS";
    const deptName = classId === "IT" ? "Information Technology" : "Computer Science";

    const newStudent = {
      id: "STD-" + classId + (list.filter(s => s.classId === classId).length + 1).toString().padStart(2, "0"),
      avatar: studentData.avatar || "assets/avatar_student.jpg",
      overallAttendance: 100,
      streak: 1,
      classId: classId,
      department: deptName,
      departmentCode: classId,
      subjects: classId === "CS" ? [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 100, total: 32, attended: 32, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 100, total: 34, attended: 34, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 100, total: 28, attended: 28, teacher: "Trupti Thakur" }
      ] : [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 100, total: 30, attended: 30, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 100, total: 30, attended: 30, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 100, total: 30, attended: 30, teacher: "Chaitrali Naik" }
      ],
      ...studentData
    };

    list.push(newStudent);
    this.setItem(this.STORAGE_KEYS.STUDENTS, list);
    this.emit("studentsChanged", list);
    return newStudent;
  }

  updateStudent(id, studentData) {
    let list = this.getStudents();
    list = list.map(s => {
      if (s.id === id) {
        const updated = { ...s, ...studentData };
        // If class changed, align department name
        if (studentData.classId) {
          updated.department = studentData.classId === "IT" ? "Information Technology" : "Computer Science";
          updated.departmentCode = studentData.classId;
        }
        return updated;
      }
      return s;
    });

    this.setItem(this.STORAGE_KEYS.STUDENTS, list);
    this.emit("studentsChanged", list);

    // If updated student is Vaishnavi Chavan, keep demo parent linked
    if (id === "STD-CS01" && studentData.name) {
      const demoAccounts = this.getDemoAccounts();
      if (demoAccounts.parent) {
        demoAccounts.parent.childName = studentData.name;
      }
    }
  }

  deleteStudent(id) {
    let list = this.getStudents();
    list = list.filter(s => s.id !== id);
    this.setItem(this.STORAGE_KEYS.STUDENTS, list);
    this.emit("studentsChanged", list);
  }

  // ------------------------------------
  // ATTENDANCE SESSIONS & ACTIONS
  // ------------------------------------
  getAttendanceRecords(filter = {}) {
    let records = this.getItem(this.STORAGE_KEYS.ATTENDANCE, window.SEED_DATA.attendanceRecords);
    if (filter.classId && filter.classId !== "ALL") {
      records = records.filter(r => r.classId === filter.classId);
    }
    if (filter.subjectId && filter.subjectId !== "ALL") {
      records = records.filter(r => r.subjectId === filter.subjectId);
    }
    if (filter.date) {
      records = records.filter(r => r.date === filter.date);
    }
    return records;
  }

  getAttendanceForSession(classId, subjectId, date) {
    const records = this.getAttendanceRecords();
    return records.find(r => r.classId === classId && r.subjectId === subjectId && r.date === date) || null;
  }

  saveAttendance(classId, subjectId, date, statusMap, teacherName = "Swapnali Jadhav") {
    let records = this.getItem(this.STORAGE_KEYS.ATTENDANCE, window.SEED_DATA.attendanceRecords);
    const subjects = this.getSubjects();
    const currentSubject = subjects.find(s => s.id === subjectId) || { name: "Class Session", code: classId + "-101" };

    const existingIndex = records.findIndex(r => r.classId === classId && r.subjectId === subjectId && r.date === date);

    const recordPayload = {
      id: "REC-" + date.replace(/-/g, "") + "-" + classId + "-" + subjectId,
      classId,
      subjectId,
      subjectName: currentSubject.name,
      date,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      markedBy: teacherName,
      records: statusMap
    };

    if (existingIndex >= 0) {
      records[existingIndex] = recordPayload;
    } else {
      records.unshift(recordPayload);
    }

    this.setItem(this.STORAGE_KEYS.ATTENDANCE, records);

    // Update students' metrics
    this.recalculateStudentMetrics(classId, statusMap);

    // Sync session to Firebase Cloud if connected
    if (window.firebaseService && window.firebaseService.isConnected) {
      window.firebaseService.syncSessionToCloud(recordPayload);
    }

    this.emit("attendanceSaved", recordPayload);
    return recordPayload;
  }

  recalculateStudentMetrics(classId, statusMap) {
    let students = this.getStudents();
    let changed = false;

    students = students.map(student => {
      if (student.classId === classId && statusMap[student.id]) {
        changed = true;
        const status = statusMap[student.id];
        let overall = student.overallAttendance;
        let streak = student.streak || 0;

        if (status === "present") {
          streak += 1;
          overall = Math.min(100, +(overall + 0.4).toFixed(1));
        } else if (status === "late") {
          streak = Math.max(1, streak);
          overall = +(overall - 0.2).toFixed(1);
        } else if (status === "absent") {
          streak = 0;
          overall = Math.max(40, +(overall - 1.5).toFixed(1));
        }

        return {
          ...student,
          overallAttendance: overall,
          streak
        };
      }
      return student;
    });

    if (changed) {
      this.setItem(this.STORAGE_KEYS.STUDENTS, students);
      if (window.firebaseService && window.firebaseService.isConnected) {
        window.firebaseService.syncStudentsToCloud(students);
      }
      this.emit("studentsChanged", students);
    }
  }

  // Teacher clicks "Notify Parents"
  notifyParentsForSession(classId, subjectId, date, statusMap) {
    const students = this.getStudents(classId);
    const subjects = this.getSubjects();
    const currentSubject = subjects.find(s => s.id === subjectId) || { name: "Class Session" };
    let alertsCreated = 0;

    students.forEach(student => {
      const status = statusMap[student.id];
      if (status === "absent") {
        this.sendNotification({
          type: "absent",
          severity: "danger",
          title: "🔴 Absence Notification",
          message: `Dear ${student.parentName || 'Parent'}, your child ${student.name} was marked ABSENT today (${date}) in ${currentSubject.name}.`,
          studentId: student.id,
          classId: classId
        });
        alertsCreated++;
      } else if (status === "late") {
        this.sendNotification({
          type: "late",
          severity: "warning",
          title: "🟡 Late Arrival Notification",
          message: `Dear ${student.parentName || 'Parent'}, your child ${student.name} arrived late for ${currentSubject.name} today (${date}).`,
          studentId: student.id,
          classId: classId
        });
        alertsCreated++;
      } else if (status === "present") {
        this.sendNotification({
          type: "present",
          severity: "success",
          title: "🟢 Attendance Confirmed",
          message: `${student.name} attended today's session in ${currentSubject.name}.`,
          studentId: student.id,
          classId: classId
        });
        alertsCreated++;
      }
    });

    return alertsCreated;
  }

  // ------------------------------------
  // NOTIFICATIONS
  // ------------------------------------
  getNotifications(role = "all", studentId = null) {
    const list = this.getItem(this.STORAGE_KEYS.NOTIFICATIONS, window.SEED_DATA.notifications);
    if (role === "parent" || role === "student") {
      const targetId = studentId || "STD-CS01";
      return list.filter(n => n.studentId === targetId || n.studentId === null);
    }
    return list;
  }

  sendNotification(data) {
    const list = this.getItem(this.STORAGE_KEYS.NOTIFICATIONS, window.SEED_DATA.notifications);
    const newNotif = {
      id: "NOTIF-" + Date.now(),
      type: data.type || "info",
      severity: data.severity || "info",
      title: data.title || "Campus Alert",
      message: data.message || "",
      date: new Date().toLocaleDateString("en-US", { month: "short", day: "numeric" }) + " " + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      studentId: data.studentId || null,
      classId: data.classId || null,
      read: false
    };
    list.unshift(newNotif);
    this.setItem(this.STORAGE_KEYS.NOTIFICATIONS, list);

    // Sync notification to Firebase Cloud for real-time multi-device alerts
    if (window.firebaseService && window.firebaseService.isConnected) {
      window.firebaseService.dispatchCloudNotification(newNotif);
    }

    this.emit("notificationAdded", newNotif);
    return newNotif;
  }

  markNotificationRead(id) {
    let list = this.getItem(this.STORAGE_KEYS.NOTIFICATIONS, window.SEED_DATA.notifications);
    list = list.map(n => n.id === id ? { ...n, read: true } : n);
    this.setItem(this.STORAGE_KEYS.NOTIFICATIONS, list);
    this.emit("notificationsChanged", list);
  }

  markAllNotificationsRead() {
    let list = this.getItem(this.STORAGE_KEYS.NOTIFICATIONS, window.SEED_DATA.notifications);
    list = list.map(n => ({ ...n, read: true }));
    this.setItem(this.STORAGE_KEYS.NOTIFICATIONS, list);
    this.emit("notificationsChanged", list);
  }

  // ------------------------------------
  // MESSAGES (TEACHER - PARENT)
  // ------------------------------------
  getMessages(studentId = "STD-CS01") {
    const messages = this.getItem(this.STORAGE_KEYS.MESSAGES, window.SEED_DATA.messages);
    return messages.filter(m => m.studentId === studentId);
  }

  sendMessage(messageData) {
    const messages = this.getItem(this.STORAGE_KEYS.MESSAGES, window.SEED_DATA.messages);
    const newMsg = {
      id: "MSG-" + Date.now(),
      from: messageData.from,
      fromRole: messageData.fromRole,
      to: messageData.to,
      studentId: messageData.studentId || "STD-CS01",
      text: messageData.text,
      time: "Just now",
      isSelf: messageData.isSelf !== undefined ? messageData.isSelf : true
    };
    messages.push(newMsg);
    this.setItem(this.STORAGE_KEYS.MESSAGES, messages);

    // Sync message to Firebase Cloud for real-time parent-counselor chat
    if (window.firebaseService && window.firebaseService.isConnected) {
      window.firebaseService.sendCloudMessage(newMsg);
    }

    this.emit("messageAdded", newMsg);
    return newMsg;
  }

  // ------------------------------------
  // STATS & DASHBOARD CALCULATIONS
  // ------------------------------------
  getCampusStats() {
    const students = this.getStudents();
    const teachers = this.getTeachers();
    const departments = this.getDepartments();
    const classes = this.getClasses();

    const csStudents = students.filter(s => s.classId === "CS");
    const itStudents = students.filter(s => s.classId === "IT");

    // Dynamic stats
    const totalStudents = students.length; // 15
    const totalTeachers = teachers.length; // 6
    const totalDepartments = departments.length; // 2
    const totalClasses = classes.length; // 2

    // Compute active presence
    const lowAttendanceStudents = students.filter(s => s.overallAttendance < 75);
    const absentToday = lowAttendanceStudents.length;
    const presentToday = totalStudents - absentToday;

    let sumPct = 0;
    students.forEach(s => { sumPct += s.overallAttendance; });
    const avgAttendance = students.length ? +(sumPct / students.length).toFixed(1) : 0;

    let csSum = 0;
    csStudents.forEach(s => { csSum += s.overallAttendance; });
    const csAvg = csStudents.length ? +(csSum / csStudents.length).toFixed(1) : 0;

    let itSum = 0;
    itStudents.forEach(s => { itSum += s.overallAttendance; });
    const itAvg = itStudents.length ? +(itSum / itStudents.length).toFixed(1) : 0;

    return {
      totalStudents,
      totalTeachers,
      totalDepartments,
      totalClasses,
      csCount: csStudents.length,
      itCount: itStudents.length,
      csAvg,
      itAvg,
      presentToday,
      absentToday,
      lateToday: 0,
      avgAttendance,
      lowAttendanceCount: lowAttendanceStudents.length,
      lowAttendanceStudents
    };
  }

  // ------------------------------------
  // PARENT PORTAL & COMPLETE MONTH CALENDAR
  // ------------------------------------
  getStudentStats(studentId = "STD-CS01", year = 2026, month = 9) { // month: 9 = October (0-indexed)
    const student = this.getStudentById(studentId) || this.getStudents()[0];
    const holidaysList = this.getItem(this.STORAGE_KEYS.HOLIDAYS, window.SEED_DATA.holidays);

    // Compute lectures
    let totalLectures = 0;
    let attendedLectures = 0;
    if (student.subjects && student.subjects.length > 0) {
      student.subjects.forEach(s => {
        totalLectures += s.total || 30;
        attendedLectures += s.attended || 28;
      });
    } else {
      totalLectures = 94;
      attendedLectures = 89;
    }
    const missedLectures = totalLectures - attendedLectures;

    // Monthly Calendar Generation
    // October 2026 has 31 days. Oct 1, 2026 is Thursday (dayOfWeek = 4 in 0=Sun format)
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayOfWeek = new Date(year, month, 1).getDay(); // 0 = Sun, 1 = Mon ... 4 = Thu

    const calendarDays = [];

    // Padding empty cells for proper alignment with SUN MON TUE WED THU FRI SAT header
    for (let pad = 0; pad < firstDayOfWeek; pad++) {
      calendarDays.push({
        day: "",
        isPad: true,
        status: "empty"
      });
    }

    // Days in current month
    for (let day = 1; day <= daysInMonth; day++) {
      const currentDateObj = new Date(year, month, day);
      const dayOfWeek = currentDateObj.getDay(); // 0 is Sunday
      const dateStr = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;

      // Check official holidays list
      const holidayEntry = holidaysList.find(h => {
        return h.date === dateStr || h.day === day;
      });

      let status = "present";
      let statusLabel = "Present";
      let statusBadge = "🟢 Present";
      let holidayName = "";
      let description = "Regular classroom lectures conducted.";
      let isHoliday = false;
      let isSunday = false;
      let isEvent = false;

      // 1. Every Sunday is strictly a Holiday with blue highlighting
      if (dayOfWeek === 0) {
        status = "holiday";
        isSunday = true;
        isHoliday = true;
        statusLabel = "Sunday Holiday";
        statusBadge = "🔵 Holiday";
        holidayName = "Sunday Holiday";
        description = "Weekly Institutional Holiday • Campus Closed";
      }
      // 2. Official holidays from list
      else if (holidayEntry && holidayEntry.type === "holiday") {
        status = "holiday";
        isHoliday = true;
        statusLabel = holidayEntry.name;
        statusBadge = "🔵 Holiday";
        holidayName = holidayEntry.name;
        description = holidayEntry.description || "Official Non-working Campus Holiday";
      }
      // 3. College Events
      else if (holidayEntry && holidayEntry.type === "event") {
        status = "event";
        isEvent = true;
        statusLabel = holidayEntry.name;
        statusBadge = "🟡 Event";
        holidayName = holidayEntry.name;
        description = holidayEntry.description || "Important Campus Event";
      }
      // 4. Working days attendance evaluation
      else {
        // If student is Tushar Thakur (low attendance) or Om Gavali
        if (student.overallAttendance < 75 && (day === 7 || day === 14 || day === 21 || day === 27)) {
          status = "absent";
          statusLabel = "Absent";
          statusBadge = "🔴 Absent";
          description = "Student marked absent by subject instructor.";
        } else if (day === 10 || day === 24) {
          // Saturday elective workshop / late
          status = "late";
          statusLabel = "Late Arrival";
          statusBadge = "🟡 Late";
          description = "Arrived 15 minutes late for lecture.";
        } else if (day > 28) {
          // Future / upcoming dates
          status = "nodata";
          statusLabel = "Scheduled";
          statusBadge = "⚪ Scheduled";
          description = "Upcoming lecture session.";
        } else {
          status = "present";
          statusLabel = "Present";
          statusBadge = "🟢 Present";
          description = "Full attendance recorded across all daily lectures.";
        }
      }

      // Check if Today
      const isToday = (day === 2 && month === 9 && year === 2026); // Default demo date Oct 2, 2026

      calendarDays.push({
        day,
        date: dateStr,
        dayOfWeek,
        dayName: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][dayOfWeek],
        status,
        statusLabel,
        statusBadge,
        isSunday,
        isHoliday,
        isEvent,
        holidayName,
        description,
        isToday,
        isPad: false,
        sessions: isHoliday ? [] : [
          {
            time: "09:30 AM",
            subject: student.classId === "IT" ? "Web Technologies" : "Data Structures & Algorithms",
            teacher: student.classId === "IT" ? "Srushti Parab" : "Swapnali Jadhav",
            status: status === "event" ? "Event Session" : status
          },
          {
            time: "11:15 AM",
            subject: student.classId === "IT" ? "Network Security" : "Database Management Systems",
            teacher: student.classId === "IT" ? "Sneha Mokal / Mali" : "Anuja Kanawade",
            status: status === "event" ? "Event Session" : (status === "absent" ? "absent" : "present")
          }
        ]
      });
    }

    return {
      student,
      parentName: student.parentName || "Rajaram Chavan",
      department: student.department || "Computer Science",
      departmentCode: student.classId || "CS",
      overallAttendance: student.overallAttendance,
      streak: student.streak || 16,
      attendedLectures,
      missedLectures,
      totalLectures,
      isWarning: student.overallAttendance < 75,
      subjects: student.subjects || [],
      calendarDays,
      monthName: "October",
      year: 2026
    };
  }
}

// Instantiate and expose globally
window.attendxStore = new Store();
