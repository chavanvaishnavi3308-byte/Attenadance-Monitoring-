/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Centralized Seed Dataset
 * 
 * Strict Configuration:
 * - Admin: Dr. Vidya Mohod Ma’am
 * - Teachers (6): Swapnali Jadhav, Anuja Kanawade, Srushti Parab, Trupti Thakur, Sneha Mokal / Mali, Chaitrali Naik
 * - Parent: Rajaram Chavan (Child: Vaishnavi Chavan)
 * - Departments (2): Computer Science (CS), Information Technology (IT)
 * - Classes (2): CS, IT
 * - CS Students (10): Vaishnavi Chavan, Sainath Chanvir, Shubham Sanap, Omkar Madav, Tushar Thakur, Tanvi Bhoir, Aayush Panchal, Sandeep Kami, Manali Kolhe, Aditya Pisale
 * - IT Students (5): Sanika Kamble, Komal Ingle, Aviraj Latpate, Om Gavali, Payal Ghagh
 */

const SEED_DATA = {
  // System Metadata & Admin
  admin: {
    id: "ADM-001",
    name: "Dr. Vidya Mohod Ma’am",
    email: "admin@attendx.edu",
    role: "admin",
    department: "Central Administration",
    title: "Head of Institution & Academic Dean",
    avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=200&q=80"
  },

  // Parent Profile (Rajaram Chavan linked to Vaishnavi Chavan)
  parent: {
    id: "PAR-001",
    name: "Rajaram Chavan",
    email: "rajaram.chavan@parent.attendx.edu",
    phone: "+91 98201 44521",
    relationship: "Father / Primary Guardian",
    role: "parent",
    childId: "STD-CS01",
    childName: "Vaishnavi Chavan",
    childClass: "CS",
    childDepartment: "Computer Science"
  },

  // Exactly Two Departments
  departments: [
    {
      id: "CS",
      name: "Computer Science",
      code: "CS",
      head: "Dr. Vidya Mohod Ma’am",
      description: "Department of Computer Science & Engineering",
      totalStudents: 10,
      totalTeachers: 3,
      classes: ["CS"]
    },
    {
      id: "IT",
      name: "Information Technology",
      code: "IT",
      head: "Dr. Vidya Mohod Ma’am",
      description: "Department of Information Technology",
      totalStudents: 5,
      totalTeachers: 3,
      classes: ["IT"]
    }
  ],

  // Exactly Two Campus Classes
  classes: [
    {
      id: "CS",
      name: "CS (Computer Science)",
      department: "Computer Science",
      departmentCode: "CS",
      semester: 6,
      totalStudents: 10,
      description: "Year 3 Computer Science Engineering Core Batch"
    },
    {
      id: "IT",
      name: "IT (Information Technology)",
      department: "Information Technology",
      departmentCode: "IT",
      semester: 6,
      totalStudents: 5,
      description: "Year 3 Information Technology Core Batch"
    }
  ],

  // Exactly Six Teachers
  teachers: [
    {
      id: "TCH-001",
      name: "Swapnali Jadhav",
      email: "swapnali.jadhav@attendx.edu",
      role: "teacher",
      department: "Computer Science",
      departmentCode: "CS",
      assignedClass: "CS",
      title: "Assistant Professor, Computer Science",
      subjectSpecialty: "Advanced Data Structures & Algorithms",
      avatar: "assets/avatar_teacher.jpg"
    },
    {
      id: "TCH-002",
      name: "Anuja Kanawade",
      email: "anuja.kanawade@attendx.edu",
      role: "teacher",
      department: "Computer Science",
      departmentCode: "CS",
      assignedClass: "CS",
      title: "Associate Professor, Computer Science",
      subjectSpecialty: "Database Management Systems",
      avatar: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=200&q=80"
    },
    {
      id: "TCH-003",
      name: "Srushti Parab",
      email: "srushti.parab@attendx.edu",
      role: "teacher",
      department: "Information Technology",
      departmentCode: "IT",
      assignedClass: "IT",
      title: "Assistant Professor, Information Technology",
      subjectSpecialty: "Web Technologies & Cloud Services",
      avatar: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=200&q=80"
    },
    {
      id: "TCH-004",
      name: "Trupti Thakur",
      email: "trupti.thakur@attendx.edu",
      role: "teacher",
      department: "Computer Science",
      departmentCode: "CS",
      assignedClass: "CS",
      title: "Assistant Professor, Computer Science",
      subjectSpecialty: "Software Engineering & Project Management",
      avatar: "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?auto=format&fit=crop&w=200&q=80"
    },
    {
      id: "TCH-005",
      name: "Sneha Mokal / Mali",
      email: "sneha.mokal@attendx.edu",
      role: "teacher",
      department: "Information Technology",
      departmentCode: "IT",
      assignedClass: "IT",
      title: "Associate Professor, Information Technology",
      subjectSpecialty: "Network Security & Cryptography",
      avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80"
    },
    {
      id: "TCH-006",
      name: "Chaitrali Naik",
      email: "chaitrali.naik@attendx.edu",
      role: "teacher",
      department: "Information Technology",
      departmentCode: "IT",
      assignedClass: "IT",
      title: "Assistant Professor, Information Technology",
      subjectSpecialty: "Data Analytics & Python Programming",
      avatar: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=200&q=80"
    }
  ],

  // Subjects for CS and IT
  subjects: [
    {
      id: "SUB-CS301",
      code: "CS-301",
      name: "Data Structures & Algorithms",
      classId: "CS",
      department: "Computer Science",
      teacher: "Swapnali Jadhav"
    },
    {
      id: "SUB-CS302",
      code: "CS-302",
      name: "Database Management Systems",
      classId: "CS",
      department: "Computer Science",
      teacher: "Anuja Kanawade"
    },
    {
      id: "SUB-CS303",
      code: "CS-303",
      name: "Software Engineering",
      classId: "CS",
      department: "Computer Science",
      teacher: "Trupti Thakur"
    },
    {
      id: "SUB-IT301",
      code: "IT-301",
      name: "Web Technologies & Cloud Services",
      classId: "IT",
      department: "Information Technology",
      teacher: "Srushti Parab"
    },
    {
      id: "SUB-IT302",
      code: "IT-302",
      name: "Network Security & Cryptography",
      classId: "IT",
      department: "Information Technology",
      teacher: "Sneha Mokal / Mali"
    },
    {
      id: "SUB-IT303",
      code: "IT-303",
      name: "Data Analytics & Python Programming",
      classId: "IT",
      department: "Information Technology",
      teacher: "Chaitrali Naik"
    }
  ],

  // Exactly 15 Students: 10 CS, 5 IT
  students: [
    // --- 10 Computer Science Students ---
    {
      id: "STD-CS01",
      name: "Vaishnavi Chavan",
      rollNo: "CS-01",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "vaishnavi.chavan@attendx.edu",
      avatar: "assets/avatar_student.jpg",
      overallAttendance: 94.5,
      streak: 16,
      parentName: "Rajaram Chavan",
      parentPhone: "+91 98201 44521",
      parentEmail: "rajaram.chavan@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 96, total: 32, attended: 31, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 94, total: 34, attended: 32, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 93, total: 28, attended: 26, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS02",
      name: "Sainath Chanvir",
      rollNo: "CS-02",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "sainath.chanvir@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 91.2,
      streak: 12,
      parentName: "Ramesh Chanvir",
      parentPhone: "+91 98201 44522",
      parentEmail: "ramesh.chanvir@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 91, total: 32, attended: 29, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 91, total: 34, attended: 31, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 92, total: 28, attended: 26, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS03",
      name: "Shubham Sanap",
      rollNo: "CS-03",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "shubham.sanap@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 88.7,
      streak: 8,
      parentName: "Dnyaneshwar Sanap",
      parentPhone: "+91 98201 44523",
      parentEmail: "dnyaneshwar.sanap@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 88, total: 32, attended: 28, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 89, total: 34, attended: 30, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 89, total: 28, attended: 25, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS04",
      name: "Omkar Madav",
      rollNo: "CS-04",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "omkar.madav@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 95.0,
      streak: 19,
      parentName: "Prakash Madav",
      parentPhone: "+91 98201 44524",
      parentEmail: "prakash.madav@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 95, total: 32, attended: 30, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 94, total: 34, attended: 32, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 96, total: 28, attended: 27, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS05",
      name: "Tushar Thakur",
      rollNo: "CS-05",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "tushar.thakur@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 68.4, // At-risk (< 75%)
      streak: 0,
      parentName: "Santosh Thakur",
      parentPhone: "+91 98201 44525",
      parentEmail: "santosh.thakur@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 66, total: 32, attended: 21, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 70, total: 34, attended: 24, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 69, total: 28, attended: 19, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS06",
      name: "Tanvi Bhoir",
      rollNo: "CS-06",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "tanvi.bhoir@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 92.8,
      streak: 14,
      parentName: "Suresh Bhoir",
      parentPhone: "+91 98201 44526",
      parentEmail: "suresh.bhoir@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 93, total: 32, attended: 30, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 92, total: 34, attended: 31, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 93, total: 28, attended: 26, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS07",
      name: "Aayush Panchal",
      rollNo: "CS-07",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "aayush.panchal@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 90.1,
      streak: 9,
      parentName: "Dilip Panchal",
      parentPhone: "+91 98201 44527",
      parentEmail: "dilip.panchal@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 90, total: 32, attended: 29, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 90, total: 34, attended: 31, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 90, total: 28, attended: 25, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS08",
      name: "Sandeep Kami",
      rollNo: "CS-08",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "sandeep.kami@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 86.5,
      streak: 6,
      parentName: "Bahadur Kami",
      parentPhone: "+91 98201 44528",
      parentEmail: "bahadur.kami@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 87, total: 32, attended: 28, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 86, total: 34, attended: 29, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 86, total: 28, attended: 24, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS09",
      name: "Manali Kolhe",
      rollNo: "CS-09",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "manali.kolhe@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 96.2,
      streak: 21,
      parentName: "Sunil Kolhe",
      parentPhone: "+91 98201 44529",
      parentEmail: "sunil.kolhe@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 97, total: 32, attended: 31, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 96, total: 34, attended: 33, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 96, total: 28, attended: 27, teacher: "Trupti Thakur" }
      ]
    },
    {
      id: "STD-CS10",
      name: "Aditya Pisale",
      rollNo: "CS-10",
      classId: "CS",
      department: "Computer Science",
      departmentCode: "CS",
      email: "aditya.pisale@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 89.0,
      streak: 7,
      parentName: "Sanjay Pisale",
      parentPhone: "+91 98201 44530",
      parentEmail: "sanjay.pisale@parent.attendx.edu",
      subjects: [
        { name: "Data Structures & Algorithms", code: "CS-301", attendance: 89, total: 32, attended: 28, teacher: "Swapnali Jadhav" },
        { name: "Database Management Systems", code: "CS-302", attendance: 88, total: 34, attended: 30, teacher: "Anuja Kanawade" },
        { name: "Software Engineering", code: "CS-303", attendance: 90, total: 28, attended: 25, teacher: "Trupti Thakur" }
      ]
    },

    // --- 5 Information Technology Students ---
    {
      id: "STD-IT01",
      name: "Sanika Kamble",
      rollNo: "IT-01",
      classId: "IT",
      department: "Information Technology",
      departmentCode: "IT",
      email: "sanika.kamble@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 93.4,
      streak: 15,
      parentName: "Ashok Kamble",
      parentPhone: "+91 98201 44531",
      parentEmail: "ashok.kamble@parent.attendx.edu",
      subjects: [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 94, total: 30, attended: 28, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 93, total: 30, attended: 28, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 93, total: 30, attended: 28, teacher: "Chaitrali Naik" }
      ]
    },
    {
      id: "STD-IT02",
      name: "Komal Ingle",
      rollNo: "IT-02",
      classId: "IT",
      department: "Information Technology",
      departmentCode: "IT",
      email: "komal.ingle@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 95.8,
      streak: 22,
      parentName: "Vijay Ingle",
      parentPhone: "+91 98201 44532",
      parentEmail: "vijay.ingle@parent.attendx.edu",
      subjects: [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 96, total: 30, attended: 29, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 95, total: 30, attended: 29, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 96, total: 30, attended: 29, teacher: "Chaitrali Naik" }
      ]
    },
    {
      id: "STD-IT03",
      name: "Aviraj Latpate",
      rollNo: "IT-03",
      classId: "IT",
      department: "Information Technology",
      departmentCode: "IT",
      email: "aviraj.latpate@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 87.2,
      streak: 5,
      parentName: "Bharat Latpate",
      parentPhone: "+91 98201 44533",
      parentEmail: "bharat.latpate@parent.attendx.edu",
      subjects: [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 87, total: 30, attended: 26, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 87, total: 30, attended: 26, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 88, total: 30, attended: 26, teacher: "Chaitrali Naik" }
      ]
    },
    {
      id: "STD-IT04",
      name: "Om Gavali",
      rollNo: "IT-04",
      classId: "IT",
      department: "Information Technology",
      departmentCode: "IT",
      email: "om.gavali@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 71.3, // At-risk (< 75%)
      streak: 1,
      parentName: "Anil Gavali",
      parentPhone: "+91 98201 44534",
      parentEmail: "anil.gavali@parent.attendx.edu",
      subjects: [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 71, total: 30, attended: 21, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 72, total: 30, attended: 22, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 71, total: 30, attended: 21, teacher: "Chaitrali Naik" }
      ]
    },
    {
      id: "STD-IT05",
      name: "Payal Ghagh",
      rollNo: "IT-05",
      classId: "IT",
      department: "Information Technology",
      departmentCode: "IT",
      email: "payal.ghagh@attendx.edu",
      avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80",
      overallAttendance: 92.0,
      streak: 11,
      parentName: "Ravindra Ghagh",
      parentPhone: "+91 98201 44535",
      parentEmail: "ravindra.ghagh@parent.attendx.edu",
      subjects: [
        { name: "Web Technologies & Cloud Services", code: "IT-301", attendance: 92, total: 30, attended: 28, teacher: "Srushti Parab" },
        { name: "Network Security & Cryptography", code: "IT-302", attendance: 92, total: 30, attended: 28, teacher: "Sneha Mokal / Mali" },
        { name: "Data Analytics & Python Programming", code: "IT-303", attendance: 92, total: 30, attended: 28, teacher: "Chaitrali Naik" }
      ]
    }
  ],

  // Sample Past Attendance Records
  attendanceRecords: [
    {
      id: "REC-20261002-CS-DSA",
      classId: "CS",
      subjectId: "SUB-CS301",
      subjectName: "Data Structures & Algorithms",
      date: "2026-10-02",
      time: "09:30 AM",
      markedBy: "Swapnali Jadhav",
      records: {
        "STD-CS01": "present",
        "STD-CS02": "present",
        "STD-CS03": "present",
        "STD-CS04": "present",
        "STD-CS05": "absent",
        "STD-CS06": "present",
        "STD-CS07": "present",
        "STD-CS08": "present",
        "STD-CS09": "present",
        "STD-CS10": "present"
      }
    },
    {
      id: "REC-20261002-IT-WEB",
      classId: "IT",
      subjectId: "SUB-IT301",
      subjectName: "Web Technologies & Cloud Services",
      date: "2026-10-02",
      time: "10:15 AM",
      markedBy: "Srushti Parab",
      records: {
        "STD-IT01": "present",
        "STD-IT02": "present",
        "STD-IT03": "present",
        "STD-IT04": "absent",
        "STD-IT05": "present"
      }
    },
    {
      id: "REC-20261001-CS-DBMS",
      classId: "CS",
      subjectId: "SUB-CS302",
      subjectName: "Database Management Systems",
      date: "2026-10-01",
      time: "11:15 AM",
      markedBy: "Anuja Kanawade",
      records: {
        "STD-CS01": "present",
        "STD-CS02": "present",
        "STD-CS03": "present",
        "STD-CS04": "present",
        "STD-CS05": "absent",
        "STD-CS06": "present",
        "STD-CS07": "late",
        "STD-CS08": "present",
        "STD-CS09": "present",
        "STD-CS10": "present"
      }
    },
    {
      id: "REC-20260930-CS-SE",
      classId: "CS",
      subjectId: "SUB-CS303",
      subjectName: "Software Engineering",
      date: "2026-09-30",
      time: "02:00 PM",
      markedBy: "Trupti Thakur",
      records: {
        "STD-CS01": "present",
        "STD-CS02": "present",
        "STD-CS03": "present",
        "STD-CS04": "present",
        "STD-CS05": "absent",
        "STD-CS06": "present",
        "STD-CS07": "present",
        "STD-CS08": "present",
        "STD-CS09": "present",
        "STD-CS10": "present"
      }
    }
  ],

  // Official Holidays & Events (Selected Month: October 2026)
  // Sundays are automatically identified by day-of-week
  holidays: [
    {
      date: "2026-10-02",
      day: 2,
      name: "Mahatma Gandhi Jayanti",
      type: "holiday",
      isOfficial: true,
      description: "National Holiday - Campus Closed in observance of Gandhi Jayanti"
    },
    {
      date: "2026-10-15",
      day: 15,
      name: "Campus Technical Project Showcase",
      type: "event",
      isOfficial: false,
      description: "Annual Engineering Innovation & Code Exhibition"
    },
    {
      date: "2026-10-20",
      day: 20,
      name: "Dussehra / Vijayadashami",
      type: "holiday",
      isOfficial: true,
      description: "Official Festival Holiday - Non-working Day"
    },
    {
      date: "2026-10-22",
      day: 22,
      name: "Mid-Semester Hackathon & Review",
      type: "event",
      isOfficial: false,
      description: "Full-day Software Evaluation & Industry Mentor Reviews"
    },
    {
      date: "2026-10-28",
      day: 28,
      name: "Maharishi Valmiki Jayanti",
      type: "holiday",
      isOfficial: true,
      description: "Campus Holiday - Institutional Leave"
    }
  ],

  // System Notifications
  notifications: [
    {
      id: "NOTIF-001",
      type: "warning",
      severity: "danger",
      title: "Attendance Warning (<75%)",
      message: "Student Tushar Thakur (Roll: CS-05) has fallen to 68.4% attendance. Debarment intervention advised by Dr. Vidya Mohod Ma’am.",
      date: "Oct 02 09:45 AM",
      studentId: "STD-CS05",
      classId: "CS",
      read: false
    },
    {
      id: "NOTIF-002",
      type: "present",
      severity: "success",
      title: "Attendance Logged Successfully",
      message: "Vaishnavi Chavan marked Present in Data Structures & Algorithms today.",
      date: "Oct 02 09:35 AM",
      studentId: "STD-CS01",
      classId: "CS",
      read: true
    },
    {
      id: "NOTIF-003",
      type: "absent",
      severity: "danger",
      title: "Student Absence Alert Dispatched",
      message: "Tushar Thakur was recorded absent in today's CS morning session.",
      date: "Oct 02 09:36 AM",
      studentId: "STD-CS05",
      classId: "CS",
      read: false
    },
    {
      id: "NOTIF-004",
      type: "report",
      severity: "info",
      title: "Campus Attendance Audit Ready",
      message: "Official Weekly Attendance Digest for CS & IT compiled by Dr. Vidya Mohod Ma’am.",
      date: "Oct 01 05:00 PM",
      studentId: null,
      classId: "CS",
      read: true
    }
  ],

  // Direct Teacher-Parent Messages
  messages: [
    {
      id: "MSG-001",
      from: "Swapnali Jadhav",
      fromRole: "teacher",
      to: "Rajaram Chavan",
      studentId: "STD-CS01",
      text: "Namaste Mr. Rajaram Chavan. Vaishnavi is performing exceptionally well in Computer Science, maintaining 94.5% overall attendance.",
      time: "Yesterday, 4:20 PM",
      isSelf: false
    },
    {
      id: "MSG-002",
      from: "Rajaram Chavan (Parent)",
      fromRole: "parent",
      to: "Swapnali Jadhav",
      studentId: "STD-CS01",
      text: "Thank you Prof. Swapnali Jadhav! We are very proud of Vaishnavi's consistency and appreciate your guidance.",
      time: "Yesterday, 5:10 PM",
      isSelf: true
    }
  ],

  // Registered Portal Login Accounts (Explicit account registration required for authentication)
  // Teacher directory records represent faculty profiles and do not automatically possess accounts.
  accounts: [
    {
      id: "ACC-ADM01",
      profileId: "ADM-001",
      role: "admin",
      name: "Dr. Vidya Mohod Ma’am",
      email: "admin@attendx.edu",
      username: "admin",
      password: "VidyaAdmin@2026",
      acceptedPasswords: ["VidyaAdmin@2026", "admin123", "attendx2026"],
      status: "active",
      createdAt: "2026-01-10T09:00:00Z"
    },
    {
      id: "ACC-TCH01",
      profileId: "TCH-001",
      role: "teacher",
      name: "Swapnali Jadhav",
      email: "swapnali.jadhav@attendx.edu",
      aliases: ["swapnalijadhav@gmail.com", "swapnali.jadhav"],
      username: "swapnali.jadhav",
      password: "swapnali@123",
      acceptedPasswords: ["swapnali@123", "Swapnali@123", "attendx2026"],
      status: "active",
      createdAt: "2026-01-10T09:00:00Z"
    },
    {
      id: "ACC-STD01",
      profileId: "STD-CS01",
      role: "student",
      name: "Vaishnavi Chavan",
      email: "vaishnavi.chavan@attendx.edu",
      aliases: ["cs-01", "cs01", "std-cs01"],
      username: "vaishnavi.chavan",
      password: "vaishnavi@123",
      acceptedPasswords: ["vaishnavi@123", "Vaishnavi@2026", "attendx2026"],
      status: "active",
      createdAt: "2026-01-10T09:00:00Z"
    },
    {
      id: "ACC-PAR01",
      profileId: "PAR-001",
      role: "parent",
      name: "Rajaram Chavan",
      email: "rajaram.chavan@parent.attendx.edu",
      aliases: ["cs01.parent@attendx.edu", "9820144521", "+91 98201 44521"],
      username: "rajaram.chavan",
      password: "rajaram@123",
      acceptedPasswords: ["rajaram@123", "Rajaram@2026", "attendx2026"],
      status: "active",
      createdAt: "2026-01-10T09:00:00Z"
    }
  ]
};

// Export globally
if (typeof window !== "undefined") {
  window.SEED_DATA = SEED_DATA;
}
