# Product Requirements Document (PRD)
## Project: AttendX – Smart Attendance Monitoring & Parent Notification System

**Version:** 1.0.0  
**Status:** Approved  
**Author:** AttendX Core Engineering & Product Team  
**Tagline:** *“Attendance. Awareness. Action.”*  
**Theme:** Futuristic Smart-Campus 3D Glassmorphism Control System  

---

### 1. Executive Summary
Traditional college attendance systems are fragmented, paper-reliant, or built on outdated administrative portals with poor user engagement and zero real-time transparency for parents. 

**AttendX** is a next-generation, futuristic smart campus attendance monitoring and parent notification platform. Built with a sleek dark-mode glassmorphic 3D aesthetic, AttendX empowers administrators, professors, students, and parents with live attendance logging, automated threshold alerts (<75%), immediate parental notifications, subject-wise analytics, and seamless role-based workflows.

---

### 2. Problem Statement
1. **Attendance Latency:** Teachers often record attendance on paper sheets or clunky legacy systems, delaying administrative awareness by days.
2. **Parental Blindspots:** Parents typically learn about chronic absenteeism weeks or months later during report card distributions or exam debarment notices.
3. **Student Disengagement:** Students lack real-time visibility into their subject-wise percentages, streaks, and risk zones before falling below mandatory 75% thresholds.
4. **Data Fragmentation:** Absence data is disconnected from notification channels, requiring manual emails or SMS broadcasts.

---

### 3. Core Objectives & Success Metrics
- **Instant Notification Latency:** Under 1 second from teacher submission to parent alert delivery.
- **Role-Centric Usability:** Under 30 seconds for a teacher to mark an entire class of 40 students.
- **Actionable Visibility:** Instant color-coded warning (<75%) on student and parent dashboards.
- **Engagement:** Daily active verification from students and parents through attendance streaks and interactive monthly calendars.

---

### 4. Target Users & Personas

| Role | Persona | Key Goal | Primary Actions |
|---|---|---|---|
| **Admin** | Dr. Alistair Vance (Dean of Academics) | Oversee campus-wide attendance health, identify anomalies, and manage institutional records. | View real-time KPI metrics, monitor class comparisons, manage student roster, audit logs. |
| **Teacher / Professor** | Prof. Elena Rostova (Dept of CS) | Fast, friction-free attendance taking, automated parent alerts, and subject historical tracking. | Select class/subject/date, toggle Present/Absent/Late, 1-click "Mark All Present", "Notify Parents". |
| **Parent** | Marcus Chen (Father of Leo Chen) | Stay proactively informed of child's safety and attendance without waiting for semester letters. | Check today's status, review color-coded monthly calendar, receive absence alerts, message teacher. |
| **Student** | Leo Chen (3rd Year Computer Science) | Maintain eligibility, track subject requirements, and build attendance streaks. | Inspect subject progress bars, maintain attendance streak 🔥, heed low-attendance warnings. |

---

### 5. Detailed Functional Requirements

#### 5.1 Landing Page & Smart Campus Showcase
- **Hero Section:** Featuring the headline *“Attendance. Awareness. Action.”*, high-tech subtitle, "Launch Portal" and "Explore Roles" call-to-actions.
- **3D Interactive Hero Canvas:** Holographic campus visualization with floating glassmorphic widget layers (Live Ring Gauge, Floating Profile Card, Live Attendance Pill).
- **Live Campus Statistics:** 98% Accuracy, 1,250+ Students, 45+ Classes, Real-Time Notification Engine.
- **Sections:** Architecture Showcase, Core Features Grid, Role-based Access Walkthrough, Interactive Live Simulator, Testimonials, FAQ accordion, Futuristic Footer.

#### 5.2 Role Selection & Authentication System
- Interactive role switcher cards: **Admin**, **Teacher**, **Parent**, **Student**.
- 1-click Quick Demo Credentials autofill for rapid testing and grading evaluation.
- Simulated credential validation with persistent session storage.
- Password reveal toggle and Remember Me support.

#### 5.3 Admin Command Dashboard
- 4 High-impact glowing KPI cards: Total Enrolled (1,250), Present Today (1,156), Absent Today (94), Average Campus Attendance (92.4%).
- **Interactive Visualizations:**
  - 7-Day Attendance Trend Line Chart.
  - Present vs Absent vs Late radial doughnut distribution.
  - Department/Class-wise comparative bar charts.
- **Real-time Live Activity Stream:** Displays attendance events as they are submitted by teachers.
- **At-Risk Student Watchlist:** Automatically flags any student with attendance < 75% with a 1-click "Send Warning" trigger.

#### 5.4 Teacher Roster & Attendance Control
- Dynamic Class (e.g., CS-3A, CS-2B, EE-4A), Subject (Data Structures, AI, Networks), and Date picker.
- Student list with individual status toggles:
  - 🟢 **Present** (Green glow)
  - 🔴 **Absent** (Red neon)
  - 🟡 **Late** (Amber neon)
- Bulk Actions: **"Mark All Present"**, **"Reset All"**.
- Live summary counters (Total, Present, Absent, Late) that update instantaneously upon button click.
- **"Save Attendance"** button: Commits record to LocalStorage and triggers success toast.
- **"Notify Parents"** button: Automatically scans current absentees/late students and creates targeted parental alerts.
- **Attendance History Log:** View and filter past marked sessions.

#### 5.5 Parent Insight Portal
- Child Profile Header: Avatar, Name, Department, Roll No, Overall Attendance Gauge.
- Radial Holographic Attendance Ring (92%).
- **Interactive Monthly Calendar:**
  - Day tiles color-coded: Green (Present), Red (Absent), Yellow (Late), Gray (Weekend/Holiday).
  - Clicking any date reveals detailed lecture-by-lecture breakdown.
- **Absence Alert Center:** Detailed alerts with Subject, Time, Teacher Name, and an interactive "Acknowledge" button.
- **Direct Teacher Communication:** In-app messaging simulation between parent and mentor.
- **Report Download:** 1-click print-ready monthly attendance transcript.

#### 5.6 Student Progress Dashboard
- Personalized greeting: *"Good Morning, Leo!"*
- Today's Lecture Schedule: Live status of each session today.
- Overall attendance metric & **Attendance Streak** (🔥 12 Days Present).
- Subject-wise progress cards with neon percentage bars:
  - Advanced Mathematics: 94%
  - Computer Networks: 91%
  - Artificial Intelligence: 96%
  - Cloud Computing: 86%
- **Dynamic Warning Banner:** If any subject drops below 75%, an alert banner appears with criteria for recovery.

#### 5.7 Student Management Module (Admin)
- Searchable, filterable directory of all registered students.
- Modals for **Add New Student**, **Edit Student Information**, and **Delete Student**.
- Student profile inspection modal showing attendance trajectory and contact details.

#### 5.8 Notification Dispatcher & Management
- Send campus-wide broadcasts or targeted alerts (Absence Warning, Low Attendance Debarment Warning, General Campus Event).
- Notification history table with filtering by severity level (Info, Success, Warning, Danger).
- Real-time notification slide-ins with synthesized futuristic audio chime.

#### 5.9 Visual Analytics Suite
- Deep-dive charts for Daily, Weekly, and Monthly trends.
- Class-to-Class and Subject-to-Subject comparative analysis.
- Risk Distribution and attendance percentile distribution.

#### 5.10 Audit Reports & Export Engine
- Multi-parameter filtering: Date range, Class, Student, Subject, Status.
- Real-time filtered preview table.
- Print-friendly layout (`@media print` optimized for clean physical printing / PDF creation).
- CSV export capability for spreadsheet analysis.

---

### 6. Non-Functional Requirements
- **Performance:** Sub-second page rendering; smooth 60fps canvas particle rendering.
- **Offline & Persistence:** 100% functional in modern browsers using HTML5 LocalStorage without requiring database configuration.
- **Responsiveness:** Fluid adaptation across mobile smartphones (360px+), tablets, laptops, and ultra-wide 4K monitors.
- **Design Quality:** State-of-the-art futuristic glassmorphic UI, high-contrast dark theme, micro-animations, and zero generic Bootstrap aesthetics.
