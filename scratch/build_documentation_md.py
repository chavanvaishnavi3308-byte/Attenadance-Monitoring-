import os

def build_md():
    print("Generating AttendX_Software_Engineering_Documentation.md...")
    md_content = """# ATTENDX – SMART ATTENDANCE MONITORING & PARENT NOTIFICATION SYSTEM
## SOFTWARE ENGINEERING PROJECT DOCUMENTATION
### Requirements, System Models, Function Point Sizing, Project Scheduling, and Verification Design

---

### Academic Project Information
| Academic Project Attribute | Institutional Record Details |
|---|---|
| **Project Title** | AttendX – Smart Attendance Monitoring & Parent Notification System |
| **Submitted by** | Vaishnavi Chavan |
| **Roll Number** | CS-01 (Exam Seat No: 2023-CS-001) |
| **Programme / Department** | Department of Computer Science & Engineering |
| **Institution** | Smart Campus Engineering & Technology Institute |
| **Project Guides** | Prof. Trupti Thakur (Assistant Professor) & Dr. Vidya Mohod Ma’am (Dean & HOD) |
| **Academic Year** | 2025–2026 |
| **Document Classification** | Academic Capstone / Mini-Project Engineering Specification (v2.0) |

---

## CONTENTS
1. [Problem Statement & Software Requirements Specification (SRS)](#1-problem-statement--software-requirements-specification-srs)
2. [Data Flow Diagram (DFD) & Structured Chart](#2-data-flow-diagram-dfd--structured-chart)
3. [Use Case Diagram and Descriptions](#3-use-case-diagram-and-descriptions)
4. [Class Diagram & Object Diagram](#4-class-diagram--object-diagram)
5. [State Chart & Activity Diagrams](#5-state-chart--activity-diagrams)
6. [Sequence & Collaboration Diagrams](#6-sequence--collaboration-diagrams)
7. [Component & Deployment Diagrams](#7-component--deployment-diagrams)
8. [Function Point (FP) Analysis](#8-function-point-fp-analysis)
9. [Project Scheduling](#9-project-scheduling)
10. [Testing Strategy & Test Cases](#10-testing-strategy--test-cases)
11. [Conclusion](#11-conclusion)

---

## 1. PROBLEM STATEMENT & SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

### 1.1 Problem Statement
Academic operations across modern higher education institutions require prompt and accurate recording of classroom attendance, rigorous oversight of statutory attendance thresholds, timely parental notification, and granular tracking of institutional health. In conventional collegiate workflows, attendance is frequently recorded on physical paper sheets or logged into cumbersome legacy ERP systems days or weeks after the session concludes. This latency generates substantial administrative friction, prevents proactive academic intervention, and leaves parents completely oblivious to student absenteeism until final semester debarment notices are issued.

AttendX is an integrated, browser-based smart attendance monitoring and parent notification platform designed to eliminate these operational deficiencies. Operating with a high-performance cybernetic glassmorphic user interface, AttendX coordinates four dedicated stakeholder workspaces: central administrators (Deans/HODs), subject teachers, parents, and students.

| Operational challenge | Effect addressed by AttendX |
|---|---|
| **Paper-based attendance latency** | Eliminates multi-day reporting delays through instant in-browser roster toggles and 1-click bulk marking. |
| **Parental communication blindspots** | Automates instantaneous alert dispatch to guardians as soon as a student is flagged absent or late. |
| **Unmonitored attendance deficits (<75%)** | Dynamically warns students and parents with recovery targets before statutory exam debarment. |
| **Disjointed administrative governance** | Consolidates campus-wide attendance KPIs, at-risk watchlists, and faculty session logs into real-time dashboards. |
| **Absence dispute and lack of auditability** | Provides closed-loop parent acknowledgement, direct messaging to teachers, and tamper-resistant session logs. |

### 1.2 Project Overview
The AttendX platform is constructed as a modern, decoupled single-page application (SPA) supported by a lightweight Node.js static server (`server.js`) on port 8080 and deployable to edge environments like Vercel. Application state, role security, faculty and student directories, lecture logs, and notification records are managed by a centralized reactive storage authority (`AttendXStore` in `js/store.js`). An interactive cybernetic canvas background running a 60fps particle simulation, synthesized Web Audio chimes, and holographic Chart.js analytics ensure high usability.

| Objective | System contribution |
|---|---|
| **O-01 - Rapid Session Logging** | Enables teachers to select class/subject and mark an entire roster in under 30 seconds via bulk 'Mark All Present'. |
| **O-02 - Instant Parent Alerts** | Dispatches targeted alerts for absent or late students to linked guardians with audible synthesized notification chimes. |
| **O-03 - Closed-Loop Engagement** | Empowers parents to review lecture-by-lecture calendar breakdowns, acknowledge alerts, and message professors directly. |
| **O-04 - Student Self-Regulation** | Provides students with live subject-wise percentages, attendance streaks (e.g. 🔥 12 Days), and low-attendance warnings. |
| **O-05 - Executive Academic Oversight** | Furnishes administrators with real-time KPI cards, at-risk watchlists (<75%), student CRUD, and print-ready transcripts. |

```mermaid
graph TD
    subgraph UI Layer
        LP[Landing Showcase & 3D Hero]
        AUTH[Role Auth & Switcher]
        ADM[Admin Command Portal]
        TCH[Teacher Attendance Suite]
        PRN[Parent Monitoring Portal]
        STD[Student Tracker Portal]
        NOTIF[Toast & Notification Drawer]
    end

    subgraph Core Engine
        ROUTER[View Router & State Machine]
        STORE[AttendX Reactive Data Store]
        DISPATCH[Notification Dispatcher]
        CHARTENG[Chart.js Holographic Engine]
        AUDIO[Web Audio Holographic Chime]
    end

    subgraph Storage Layer
        DB[(LocalStorage attendx_v2_*)]
        SEEDS[Centralized Seed Factory]
    end

    LP --> ROUTER
    AUTH --> ROUTER
    ADM --> ROUTER
    TCH --> ROUTER
    PRN --> ROUTER
    STD --> ROUTER

    ROUTER <--> STORE
    STORE <--> DB
    SEEDS --> STORE
    TCH -- "Mark & Notify" --> DISPATCH
    DISPATCH --> STORE
    DISPATCH --> NOTIF
    DISPATCH --> AUDIO
    STORE --> CHARTENG
```

### 1.3 Software Requirements Specification (SRS)

#### 1.3.1 Functional Requirements
| ID | Requirement | Expected behavior | Status basis |
|---|---|---|---|
| **FR-01** | Public Smart Showcase | Present interactive landing page with 3D perspective hero, live statistics, and role walkthroughs. | Implemented |
| **FR-02** | Role Authentication | Provide 1-click demo credential autofill and role-scoped session management for Admin, Teacher, Parent, Student. | Implemented |
| **FR-03** | Roster Retrieval | Dynamically filter and render student rosters based on selected Department, Class (CS/IT), and Subject. | Implemented |
| **FR-04** | Bulk Status Operations | Support single-click 'Mark All Present' and 'Reset All' convenience actions with instant counter recalculations. | Implemented |
| **FR-05** | Granular Attendance Marking | Allow per-student toggles across three discrete states: Present (Green), Absent (Red), and Late (Amber). | Implemented |
| **FR-06** | Session Persistence | Commit attendance logs with timestamp, class ID, and subject ID atomically into the persistent storage engine. | Implemented |
| **FR-07** | Automated Parent Dispatch | Scan session records upon 'Notify Parents' trigger and dispatch targeted high-severity alerts to guardian accounts. | Implemented |
| **FR-08** | Web Audio Chime Synthesis | Synthesize distinctive futuristic cybernetic frequencies (880Hz / 440Hz) via HTML5 Web Audio API on alert dispatch. | Implemented |
| **FR-09** | Parent Calendar Drilldown | Render color-coded monthly calendar tiles (Green, Red, Yellow) with click-to-view lecture breakdown modals. | Implemented |
| **FR-10** | Parent Alert Acknowledgment | Allow parents to view absence warning cards and mark notices as acknowledged, updating read state in the store. | Implemented |
| **FR-11** | Teacher-Parent Messaging | Facilitate direct in-app messaging between parents and subject professors regarding authorized leave or inquiries. | Implemented |
| **FR-12** | Student Timetable & Streak | Track daily lecture progress, display active attendance streaks (🔥 days present), and compute subject percentages. | Implemented |
| **FR-13** | At-Risk Threshold Warning | Automatically display pulsating neon warning banners when any subject attendance falls below the mandatory 75% limit. | Implemented |
| **FR-14** | Admin Campus Command Center | Display 4 high-impact glowing KPI cards: Total Enrolled, Present Today, Absent Today, and Average Campus Attendance. | Implemented |
| **FR-15** | Student Directory CRUD | Enable administrators to add new students, edit profiles with parent contact linkages, and remove student records. | Implemented |
| **FR-16** | Audit & Report Generation | Filter attendance history across dates, classes, and subjects, with print-ready transcript view and CSV data download. | Implemented |

#### 1.3.2 Actors
| Actor | Primary interaction |
|---|---|
| **Administrator (Dean / HOD)** | Oversees campus attendance KPIs, investigates low-attendance watchlists, manages student/teacher directories, and exports audit logs. |
| **Teacher (Faculty / Professor)** | Selects class/subject, marks attendance rosters via bulk or individual toggles, commits records, and dispatches parent alerts. |
| **Parent / Guardian** | Monitors linked child's daily presence, inspects monthly attendance calendar, acknowledges absence notices, and sends inquiries to teachers. |
| **Student** | Tracks personal timetable, verifies subject-wise percentages, maintains attendance streaks, and monitors recovery targets if below 75%. |
| **System Dispatcher & Audio Synth** | Monitors attendance mutation events, writes notification records, tallies unread badges, and generates synthetic audio tones. |
| **Browser Client Host** | Renders cybernetic DOM elements, executes 60fps canvas starfield, handles LocalStorage I/O, and formats printable reports. |

#### 1.3.3 Non-Functional Requirements
| Quality attribute | Requirement | Verification approach |
|---|---|---|
| **Performance** | Roster rendering latency under 50ms; parent alert dispatch under 100ms from button click. | Browser Performance Timeline profiling. |
| **Reliability** | Zero data loss on page refresh; defensive try/catch blocks for LocalStorage quota exceptions. | Storage corruption and quota testing. |
| **Security & RBAC** | Strict view isolation; parents restricted exclusively to linked child records; XSS input sanitization. | Role tampering and script injection tests. |
| **Aesthetic Excellence** | Futuristic glassmorphism with backdrop-blur, subtle cyan glowing borders, and 3D elevation cards. | Visual inspection across device resolutions. |
| **Accessibility** | WCAG AA contrast compliant text (>4.5:1 ratio); semantic HTML5 landmarks and aria-labels on triggers. | Lighthouse accessibility audit. |
| **Maintainability** | Strict modular separation of concerns across data.js, store.js, charts.js, and app.js. | Code architecture review and ESLint check. |
| **Portability** | Compatible with Google Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari without plugins. | Cross-browser execution verification. |
| **Data Integrity** | Atomic immutable array transformations in store mutations to prevent dirty state reads. | Unit tests on store mutation methods. |
| **Audio Usability** | Zero external audio file dependencies; synthesizes clean 880Hz chimes using Web Audio API. | Browser audio context verification. |
| **Auditability** | Deterministic timestamping on every attendance mark, parent notification, and student registration. | Log trail inspection in store inspector. |

### 1.4 System Scope
| Status | Capabilities / boundary described in the supplied report |
|---|---|
| **Fully Implemented** | Public showcase, 4-role authentication, session management, roster marking, bulk operations, parent alert dispatch, Web Audio chime synthesis, monthly calendar heatmap, parent acknowledgement, student streak calculation, low-attendance warning banner (<75%), admin KPIs, student CRUD, and CSV/print reporting. |
| **Simulated / Prototype** | Credential validation utilizes sandboxed demo accounts with persistent LocalStorage tokens; external SMS/WhatsApp communication is simulated via reactive internal inboxes. |
| **Planned Future Enhancements** | Integration with physical biometric/RFID turnstiles, automated multi-channel SMS gateway (Twilio), facial recognition auto-logging, and PostgreSQL/Firebase cloud persistence. |

### 1.5 Hardware, Software & Operating Environment
| Interface | Information exchanged | Boundary / note |
|---|---|---|
| **Browser Execution Runtime** | HTML5 DOM, CSS3 styling, ECMAScript 2020+ execution context. | Standard desktop or mobile browser environment (Chrome 90+, Edge 90+, Safari 14+, Firefox 88+). |
| **Web Storage API** | Key-value JSON serialization under 'attendx_v2_*' namespace. | Client-side isolated sandbox; 5MB persistent storage allocation per origin. |
| **Web Audio API** | Synthetic audio frequency synthesis via AudioContext oscillators. | Non-blocking audio tone playback upon alert dispatch (880Hz -> 440Hz alert decay). |
| **Chart.js Holographic Engine** | Canvas 2D context rendering of line, doughnut, and bar charts. | Client-side visual rendering library loaded via secure CDN. |
| **Local Node HTTP Server** | Static asset serving, MIME type mapping, SPA fallback routing. | Lightweight zero-dependency Node.js HTTP server running on port 8080 (`server.js`). |
| **Hardware Requirements** | CPU 1.5 GHz or higher, RAM 2 GB minimum, Display 1280x720 or higher. | Client workstation, tablet, or smartphone device. |

### 1.6 Assumptions and Documentation Boundaries
| Topic | Documented basis | Boundary |
|---|---|---|
| **Client-Side Sandbox** | All operational data is persisted in the client's LocalStorage instance. | Clearing browser application cache resets state to the default seed dataset (v2.0). |
| **Institutional Structure** | Preconfigured for 2 Departments (CS & IT), 2 Core Classes, 6 Faculty, 15 Students. | Demonstrates realistic institutional workflows with full scalability for expansion. |
| **Demo Authentication** | Allows rapid 1-click persona switching without requiring SMS 2FA verification. | Designed for academic project defense and live evaluation scenarios. |
| **Notification Delivery** | Delivered instantaneously to the integrated parent drawer and toast alerts. | External telecommunication SMS delivery requires live SMS provider credentials. |
| **Browser Audio Policy** | AudioContext requires at least one user gesture (click) before emitting chimes. | Complies with standard browser Autoplay Security Policies. |
| **Attendance Benchmark** | Statutory threshold is calibrated at 75.0% across all courses. | Institutional policies requiring different limits can adjust the threshold constant in store.js. |
| **Reporting Standard** | Audit statements utilize standard browser print stylesheets and CSV tables. | Direct server-side PDF generation is identified as a future extension. |

---

## 2. DATA FLOW DIAGRAM (DFD) & STRUCTURED CHART

### 2.1 Context Diagram (Level 0 DFD)
```mermaid
graph TD
    TEACHER[Teacher / Faculty] -->|Attendance Marks & Session Data| SYSTEM((0.0 AttendX System))
    SYSTEM -->|Roster & Confirmations| TEACHER
    
    ADMIN[Administrator / Dean] -->|Student Directory CRUD & Config| SYSTEM
    SYSTEM -->|Campus KPIs & Audit Logs| ADMIN
    
    SYSTEM -->|Real-time Absence & Late Alerts| PARENT[Parent / Guardian]
    PARENT -->|Alert Acknowledgement & Inquiries| SYSTEM
    
    SYSTEM -->|Subject % & Attendance Streak| STUDENT[Student]
    STUDENT -->|Timetable & Calendar Queries| SYSTEM
```

| Flow | Source | Processing / destination |
|---|---|---|
| **User Credentials & Role Choice** | Teacher / Admin / Parent / Student | Validated by Authentication Controller; returns session token and active persona profile. |
| **Attendance Marks & Session Data** | Teacher | Processed by Attendance Roster Engine; updates lecture logs and recalculates student percentages. |
| **Parent Absence & Late Alerts** | System Alert Dispatcher | Routed to linked Parent portal; triggers toast card, badge increment, and audio chime. |
| **Alert Acknowledgement & Inquiries** | Parent / Guardian | Stored in message threads; updates notification status to 'acknowledged' and alerts teacher. |
| **Student Timetable & Streak Queries** | Student | Calculates active attendance streak, lecture schedule, and warns if subject attendance < 75%. |
| **Campus KPIs & Watchlist Queries** | Administrator | Aggregates institutional health, identifies at-risk students, and renders trend charts. |
| **Roster & Student Directory CRUD** | Administrator | Mutates central student and faculty datasets; updates storage records atomically. |

### 2.2 Level 1 DFD
```mermaid
graph TD
    AUTH((1.0 Auth & Session Controller)) <--> D1[(D1: attendx_v2_accounts)]
    ROSTER((2.0 Attendance Roster Engine)) -->|Save Session Records| D3[(D3: attendx_v2_attendance)]
    ROSTER -->|Absentees Event| ALERT((3.0 Alert Dispatcher & Audio Synth))
    ALERT -->|Store Alerts| D4[(D4: attendx_v2_notifications)]
    INSIGHT((4.0 Parent & Student Insight Services)) <--> D4
    INSIGHT <--> D3
    ADMINPROC((5.0 Admin Analytics & Directory Manager)) <--> D2[(D2: attendx_v2_students/teachers)]
    ADMINPROC <--> D3
```

### 2.3 Structured Chart
```mermaid
graph TD
    ROOT[0.0 AttendX System Controller]
    ROOT --> M1[1.0 Auth & Session Controller]
    ROOT --> M2[2.0 Attendance Roster Engine]
    ROOT --> M3[3.0 Alert Dispatcher & Audio Synth]
    ROOT --> M4[4.0 Visual Analytics & Chart Engine]
    ROOT --> M5[5.0 Directory & Report Subsystem]

    M1 --> S1[• Login Validate<br>• Demo Autofill<br>• Role Guard]
    M2 --> S2[• Class/Subject Load<br>• Mark All Present<br>• Record Persist]
    M3 --> S3[• Scan Absentees<br>• Emit Chime 880Hz<br>• Badge Counter]
    M4 --> S4[• 7-Day Trend Chart<br>• Status Doughnut<br>• At-Risk <75% Scan]
    M5 --> S5[• Student CRUD<br>• Monthly Calendar<br>• CSV & Print Export]
```

| Module | Representative functions |
|---|---|
| **0.0 AttendX Master Controller** | Orchestrates view transitions, state synchronization, audio context, and DOM lifecycle events. |
| **1.0 Auth & Session Controller** | Handles credential verification, 1-click demo autofill, session token creation, and RBAC view guards. |
| **2.0 Attendance Roster Engine** | Loads class/subject rosters, executes 'Mark All Present', updates status toggles, and commits session logs. |
| **3.0 Alert Dispatcher & Audio Synth** | Scans session records for absentees, appends parent notifications, increments badges, and plays 880Hz chimes. |
| **4.0 Visual Analytics & Chart Engine** | Renders 7-day trend line charts, status distribution doughnuts, and comparative departmental bar charts. |
| **5.0 Directory & Report Subsystem** | Provides student/faculty CRUD operations, monthly calendar drilldown, and print/CSV export facilities. |

---

## 3. USE CASE DIAGRAM AND DESCRIPTIONS

### 3.1 Use Case Diagram
```mermaid
graph LR
    subgraph AttendX System Boundary
        UC1((UC-01: Select Class & Subject))
        UC2((UC-02: Mark Attendance))
        UC3((UC-03: Mark All Present))
        UC4((UC-04: Dispatch Parent Alerts))
        UC5((UC-05: View Monthly Calendar))
        UC6((UC-06: Acknowledge Absence Notice))
        UC7((UC-07: Track Streak & Subjects))
        UC8((UC-08: Low-Attendance Warning))
        UC9((UC-09: Monitor Campus Health))
        UC10((UC-10: Manage Student Directory))
    end

    TEACHER[Teacher: Swapnali Jadhav] --> UC1
    TEACHER --> UC2
    TEACHER --> UC3
    TEACHER --> UC4

    PARENT[Parent: Rajaram Chavan] --> UC4
    PARENT --> UC5
    PARENT --> UC6

    STUDENT[Student: Vaishnavi Chavan] --> UC7
    STUDENT --> UC8

    ADMIN[Admin: Dr. Vidya Mohod] --> UC9
    ADMIN --> UC10

    UC2 -.->|<<include>>| UC3
    UC2 -.->|<<extend>>| UC4
```

### 3.2 Use Case Descriptions
| Use case | Actor | Description | Precondition | Postcondition |
|---|---|---|---|---|
| **UC-01: Mark Attendance** | Teacher | Select class/subject, toggle student statuses or mark all present, and commit session log. | Teacher authenticated; valid roster available. | Session records saved in store; metrics recalculated. |
| **UC-02: Dispatch Parent Alerts** | Teacher / Dispatcher | Scan session absentees/late arrivals and dispatch targeted notifications to parents. | Attendance session saved with >=1 absentee. | Notification records created; audio chime synthesized. |
| **UC-03: View Monthly Calendar** | Parent | Inspect child's color-coded monthly calendar and drill into lecture breakdown. | Parent authenticated and linked to child. | Displays date tiles and lecture-by-lecture presence. |
| **UC-04: Acknowledge Absence Notice** | Parent | Review high-priority absence alert card and click acknowledge receipt. | Unread absence alert exists in inbox. | Alert marked read = true; confirmation feedback shown. |
| **UC-05: Send Teacher Inquiry** | Parent | Compose and send direct message to subject teacher regarding child's attendance. | Parent authenticated; teacher contact exists. | Message thread appended in store; teacher notified. |
| **UC-06: Track Streak & Subjects** | Student | Review daily lecture schedule, subject percentages, and maintain attendance streak. | Student authenticated. | Displays subject progress bars and streak flame badge. |
| **UC-07: Low-Attendance Warning** | Student / Parent | Display pulsing alert banner when attendance drops below 75% with recovery advice. | Subject attendance < 75.0%. | Warning banner rendered with required lectures calculation. |
| **UC-08: Monitor Campus Health** | Admin | Review campus attendance KPIs, trend line charts, and low-attendance watchlist. | Admin authenticated. | Displays campus KPIs, charts, and student audit trail. |
| **UC-09: Manage Student Directory** | Admin | Add, edit, or delete student profiles and configure linked parent contact details. | Admin authenticated. | Student record committed to store; roster views updated. |

---

## 4. CLASS DIAGRAM & OBJECT DIAGRAM

### 4.1 Class Diagram
```mermaid
classDiagram
    class UserAccount {
        -String id
        -String email
        -RoleEnum role
        -String name
        +authenticate() Boolean
        +getSessionToken() String
    }

    class Student {
        -String rollNo
        -String classId
        -String parentId
        -Float overallAttendance
        +getStats() Object
        +checkStreak() Int
    }

    class Teacher {
        -String department
        -String assignedClass
        -String specialty
        +markRoster() Session
        +notifyParents() Void
    }

    class Parent {
        -String childId
        -String phone
        -String relationship
        +viewCalendar() Void
        +acknowledgeNotice() Void
    }

    class AttendanceSession {
        -String id
        -String classId
        -String subjectId
        -Date date
        -Long timestamp
        +addRecord(r) Void
        +getSummary() Counts
    }

    class AttendanceRecord {
        -String studentId
        -StatusEnum status
        -Boolean verified
        +setStatus(s) Void
    }

    class NotificationItem {
        -String id
        -NotifType type
        -String title
        -String message
        -SeverityEnum severity
        -Boolean read
        +markRead() Void
        +acknowledge() Void
    }

    class AttendXStore {
        -Map STORAGE_KEYS
        -Map listeners
        +saveAttendance() Void
        +notifyParentsForSession() Void
        +getCampusStats() Object
    }

    UserAccount <|-- Student
    UserAccount <|-- Teacher
    UserAccount <|-- Parent
    Teacher "1" --> "*" AttendanceSession : logs
    AttendanceSession "1" *-- "1..*" AttendanceRecord : contains
    AttendanceSession --> NotificationItem : triggers
    AttendXStore <--> UserAccount
    AttendXStore <--> AttendanceSession
```

| Conceptual class | Representative information and responsibility |
|---|---|
| **UserAccount** | Base entity managing id, email, role (admin/teacher/parent/student), name, and credential authentication methods. |
| **Student** | Extends UserAccount; maintains rollNo (CS-01), classId (CS), parentId (PAR-001), attendance metrics, streak counter, and status. |
| **Teacher** | Extends UserAccount; maintains department (CS/IT), assignedClass, subjectSpecialty, roster marking methods, and alert triggers. |
| **Parent** | Extends UserAccount; maintains childId (STD-CS01), contact phone, relationship, inbox review, and acknowledgement methods. |
| **AttendanceSession** | Represents a discrete classroom lecture; maintains classId, subjectId, teacherId, date, and contains 1..* AttendanceRecords. |
| **AttendanceRecord** | Maintains individual studentId, presence status ('present' \| 'absent' \| 'late'), verification timestamp, and remarks. |
| **NotificationItem** | Represents alerts dispatched to guardians/students; maintains id, targetId, title, message, severity, and read flag. |
| **AttendXStore (Singleton)** | Central state manager; exposes atomic query and mutation methods synchronized with HTML5 LocalStorage. |

### 4.2 Object Diagram (Illustrative Instance)
| Illustrative object | Symbolic state |
|---|---|
| **adminUser : Admin** | `id = "ADM-001", name = "Dr. Vidya Mohod Ma’am", role = "admin", dept = "Central Administration"` |
| **teacherInst : Teacher** | `id = "TCH-001", name = "Swapnali Jadhav", assignedClass = "CS", subject = "Data Structures & Algorithms"` |
| **studentInst : Student** | `id = "STD-CS01", rollNo = "CS-01", name = "Vaishnavi Chavan", class = "CS", overallAttendance = 94.2%` |
| **parentInst : Parent** | `id = "PAR-001", name = "Rajaram Chavan", childId = "STD-CS01", phone = "+91 98201 44521"` |
| **sessionRecord : AttendanceSession** | `id = "SES-20261016-CS301", classId = "CS", subjectId = "CS-301", date = "2026-10-16", records = 10` |
| **alertInst : NotificationItem** | `id = "NOTIF-9821", type = "ABSENCE_ALERT", targetId = "STD-CS01", severity = "DANGER", read = false` |

---

## 5. STATE CHART & ACTIVITY DIAGRAMS

### 5.1 Attendance Session State Chart
```mermaid
stateDiagram-v2
    [*] --> Draft : selectSession(class, subject)
    Draft --> SessionMarked : toggleStatus() / bulkPresent()
    SessionMarked --> Committed : clickSave() [valid roster]
    Committed --> AlertDispatched : clickNotify() [absentees > 0]
    AlertDispatched --> AlertReceived : parentLogin() & reviewInbox()
    AlertReceived --> Acknowledged : clickAcknowledge()
    Acknowledged --> [*]
```

| From state | Allowed event | To state | Guard / note |
|---|---|---|---|
| **[Uninitialized]** | selectSession(class, subject) | Draft / Loaded | Requires valid class and subject selection. |
| **Draft / Loaded** | toggleStatus() / bulkPresent() | Session Marked | Roster displayed; live counter tallies update in DOM. |
| **Session Marked** | clickSave() | Committed / Persisted | Validates that all students have an assigned status. |
| **Committed / Persisted** | clickNotify() | Alert Dispatched | Evaluates absentees > 0; triggers chime and notification records. |
| **Alert Dispatched** | parentLogin() & reviewInbox() | Alert Received | Delivered to linked guardian inbox and notification drawer. |
| **Alert Received** | clickAcknowledge() | Acknowledged / Closed | Updates read = true; parent can optionally message teacher. |

### 5.2 Attendance Logging Activity Diagram
| Control step | Expected handling |
|---|---|
| **1. Session Selection** | Teacher selects Class (CS) and Subject (CS-301); UI queries Store for matching student roster. |
| **2. Roster Rendering** | UI renders student list with individual status pill toggles and bulk action buttons. |
| **3. Status Modification** | Teacher clicks 'Mark All Present' or toggles individual students; live counters update instantly. |
| **4. Local Commitment** | Teacher clicks 'Save Attendance'; Store writes serialized JSON records and computes percentage deltas. |
| **5. Notification Trigger** | Teacher clicks 'Notify Parents'; Engine extracts absentees, synthesizes 880Hz chime, and alerts parent. |

---

## 6. SEQUENCE & COLLABORATION DIAGRAMS

### 6.1 Attendance Marking Sequence Diagram
```mermaid
sequenceDiagram
    autonumber
    actor Teacher as Teacher (Swapnali Jadhav)
    participant UI as AttendX UI View
    participant Store as AttendXStore
    participant Storage as LocalStorage
    participant Audio as Web Audio Synth
    actor Parent as Parent (Rajaram Chavan)

    Teacher->>UI: Selects Class: CS, Subject: CS-301
    UI->>Store: getStudents("CS")
    Store-->>UI: Returns 10 CS Students
    Teacher->>UI: Clicks 'Mark All Present' & Marks Roll CS-01 Absent
    Teacher->>UI: Clicks 'Save Attendance'
    UI->>Store: saveAttendance("CS", "CS-301", date, records)
    Store->>Storage: setItem("attendx_v2_attendance", JSON)
    UI-->>Teacher: Toast: "Attendance saved successfully"
    Teacher->>UI: Clicks 'Notify Parents'
    UI->>Store: notifyParentsForSession("CS", "CS-301", date)
    Store->>Audio: emitChime(880Hz, "alert")
    Store->>Storage: setItem("attendx_v2_notifications", JSON)
    Storage-->>Parent: Delivers Red Absence Alert to Parent Inbox
```

---

## 7. COMPONENT & DEPLOYMENT DIAGRAMS

### 7.1 System Component Diagram
| Component | Inputs | Responsibility / output |
|---|---|---|
| **Presentation View (index.html / CSS)** | DOM events, CSS variables, User clicks | Renders 3D glassmorphic cards, 60fps canvas starfield, modal dialogs, and responsive grid layouts. |
| **Application Controller (app.js)** | View triggers, form submissions | Manages client-side routing, event delegation, toast queuing, and modal lifecycle. |
| **Reactive State Store (store.js)** | Mutations, filters, session queries | Encapsulates business rules, recalculates percentages, and ensures atomic storage synchronization. |
| **Charts Visualizer (charts.js)** | Attendance aggregate series | Configures glowing neon Chart.js instances for trends, status distribution, and class comparisons. |
| **Web Audio Synthesizer** | Trigger frequency events | Synthesizes real-time audio chime waveforms (880Hz / 440Hz) via HTML5 AudioContext. |
| **Persistence Engine (LocalStorage)** | Serialized JSON strings | Persists application entities under isolated namespace ('attendx_v2_*') with 5MB quota. |
| **Static HTTP Host (server.js)** | HTTP GET requests on port 8080 | Lightweight Node.js web server handling MIME types and SPA fallback routing. |

---

## 8. FUNCTION POINT (FP) ANALYSIS

### 8.1 Unadjusted Function Point Calculation
| Function type | Illustrative functions / data groups | Count | Weight | Subtotal |
|---|---|---|---|---|
| **External Inputs (EI)** | Mark attendance, Save session, Notify parents, Add student, Acknowledge alert, Message teacher, Login auth. | 7 | 4 (Avg) | 28 |
| **External Outputs (EO)** | Parent alert card, Web Audio chime emit, Low-attendance warning banner, KPI recalculation, CSV export. | 5 | 5 (Avg) | 25 |
| **External Inquiries (EQ)** | Class roster query, Monthly calendar breakdown, Student streak query, At-risk watchlist search, Session history. | 5 | 4 (Avg) | 20 |
| **Internal Logical Files (ILF)** | Accounts file, Student directory, Attendance logs, Notification records, Message threads. | 5 | 10 (Avg) | 50 |
| **External Interface Files (EIF)** | Chart.js graphics engine, Google Fonts typography, Web Audio browser API interface. | 3 | 7 (Avg) | 21 |
| **Total Unadjusted FP (UFP)** | Sum of all weighted functional components across the platform | 25 | - | **144** |

### 8.2 Adjusted Function Points & Effort
- **Total Degree of Influence (TDI):** 54 (based on 14 GSCs rated 2 to 5)
- **Value Adjustment Factor (VAF):** $VAF = 0.65 + (0.01 \times 54) = 1.19$
- **Adjusted Function Points (AFP):** $144.0 \times 1.19 = \mathbf{171.36\text{ FP}}$
- **Equivalent Code Size (SLOC):** $171.36 \times 50 \approx \mathbf{8,568\text{ SLOC}}$
- **Development Effort:** $\mathbf{21.42\text{ Person-Months}}$ (under COCOMO II Organic Model)
- **Academic Schedule:** $\mathbf{16\text{ Academic Weeks}}$ (~4 calendar months for 2-person team)

---

## 9. PROJECT SCHEDULING

| Phase | Duration | Predecessor | Planned deliverable |
|---|---|---|---|
| **Phase 1: Problem Formulation & SRS** | Weeks 1–3 | None | Product Requirements Document (`prd.md`), User personas, Scope. |
| **Phase 2: Architecture & Modeling** | Weeks 3–5 | Phase 1 | Architecture specification (`Architecture.md`), DFDs, Class diagram. |
| **Phase 3: UI/UX Cyber-Glass Foundation** | Weeks 5–8 | Phase 2 | Vanilla CSS glassmorphic design system (`style.css`), 60fps Canvas. |
| **Phase 4: Auth & Reactive Store** | Weeks 7–10 | Phase 3 | AttendXStore state controller (`store.js`), LocalStorage v2.0 schema. |
| **Phase 5: Attendance & Parent Dispatch** | Weeks 9–12 | Phase 4 | Roster toggles, bulk actions, Web Audio chimes, parent alert inbox. |
| **Phase 6: Visual Analytics & Reports** | Weeks 11–14 | Phase 5 | Chart.js neon visualizations (`charts.js`), calendar heatmap, CSV export. |
| **Phase 7: Testing & Defect Remediation** | Weeks 13–15 | Phase 6 | Test suite execution, role tampering validation, browser audit. |
| **Phase 8: Project Report & Defense** | Weeks 15–16 | Phase 7 | Formal Software Engineering Documentation, Defense presentation. |

---

## 10. TESTING STRATEGY & TEST CASES

| Test ID | Scenario | Input / action | Expected result | Status |
|---|---|---|---|---|
| **TC-01** | Public Showcase Load | Navigate to `http://localhost:8080/` in browser. | Landing page renders with 60fps canvas, statistics, and role cards. | **PASS** |
| **TC-02** | 1-Click Demo Autofill | Open Role Modal, click 'Teacher' tab, click 'Auto-fill Demo'. | Fields populated with `swapnali.jadhav@attendx.edu` and password. | **PASS** |
| **TC-03** | Teacher Role Authentication | Click 'Login to Portal' with teacher credentials. | Redirects to Teacher Portal; navbar displays Teacher badge. | **PASS** |
| **TC-04** | Class & Subject Roster Load | Select Class = 'CS', Subject = 'CS-301 Data Structures'. | Roster dynamically renders 10 CS students with Roll CS-01 to CS-10. | **PASS** |
| **TC-05** | Bulk 'Mark All Present' | Click 'Mark All Present' button. | All 10 students toggle to Green; Present counter shows 10, Absent shows 0. | **PASS** |
| **TC-06** | Individual Status Toggle | Click 'Absent' (Red) on student Vaishnavi Chavan (Roll CS-01). | Status switches to Absent; Present counter becomes 9, Absent becomes 1. | **PASS** |
| **TC-07** | Session Record Commitment | Click 'Save Attendance' button. | Record written to LocalStorage; toast confirms 'Attendance saved successfully'. | **PASS** |
| **TC-08** | Parent Alert Dispatch | Click 'Notify Parents' button. | Dispatcher identifies absent student; plays synthesized 880Hz chime. | **PASS** |
| **TC-09** | Parent Dashboard Verification | Switch role to Parent (Rajaram Chavan). | Dashboard displays child Vaishnavi Chavan; unread alert badge shows '1'. | **PASS** |
| **TC-10** | Parent Calendar Drilldown | Click today's date tile on interactive monthly calendar. | Modal opens displaying CS-301 Data Structures with status 'ABSENT'. | **PASS** |
| **TC-11** | Parent Alert Acknowledgment | Click 'Acknowledge Notice' button on red warning card. | Card updates to verified state; read status saved as true in store. | **PASS** |
| **TC-12** | Student Streak & Warning | Login as Student Vaishnavi Chavan. | Dashboard shows timetable; warning banner displays low attendance advice. | **PASS** |
| **TC-13** | RBAC Route Guarding | Attempt to access Admin URL view while logged in as Student. | View transition blocked; user remains in Student portal. | **PASS** |
| **TC-14** | Parent Data Isolation | Parent inspects student list queries in store console. | Only records matching childId (STD-CS01) are returned. | **PASS** |
| **TC-15** | XSS Script Injection | Submit student name containing `<script>alert('xss')</script>`. | Input sanitized before DOM insertion; script does not execute. | **PASS** |
| **TC-16** | Storage Quota Fallback | Simulate LocalStorage quota exceeded during session save. | Try/catch catches error; displays friendly warning toast. | **PASS** |
| **TC-17** | Audio Autoplay Resilience | Trigger alert before any user gesture in fresh browser session. | Browser autoplay exception caught gracefully without crash. | **PASS** |
| **TC-18** | Responsive Viewport Scaling | Resize browser window from 1920px down to 375px mobile view. | Sidebar collapses into burger menu; glass cards stack cleanly. | **PASS** |
| **TC-19** | Print Stylesheet Rendering | Press Ctrl+P / Cmd+P on Monthly Report view. | Background canvas hidden; clean high-contrast black/white transcript. | **PASS** |
| **TC-20** | Offline Operation Continuity | Disconnect network after initial page load; mark attendance. | Application continues functioning seamlessly via LocalStorage cache. | **PASS** |
| **TC-21** | CSV Export Formatting | Click 'Export CSV' in Admin Reports view. | Browser downloads properly formatted comma-delimited `.csv` file. | **PASS** |
| **TC-22** | Dataset Version Upgrade | Corrupt or alter storage version key and reload. | Store detects version mismatch, purges stale keys, and re-seeds v2.0. | **PASS** |

---

## 11. CONCLUSION

AttendX – Smart Attendance Monitoring & Parent Notification System represents a comprehensive, production-grade engineering solution that bridges the critical communication chasm between collegiate academic institutions and student homes. By replacing paper sheets and delayed legacy ERP systems with a reactive, glassmorphic single-page architecture, AttendX achieves rapid attendance capture (<30 seconds per class), sub-second parental alert dispatch, closed-loop guardian acknowledgement, and proactive low-attendance mitigation before statutory 75% exam debarment thresholds are breached.

### Key Learnings and Achievements
1. **Architectural Decoupling:** Demonstrates the power of modular client-side state machines (`store.js`) coordinating view controllers, charting visualizers, and HTML5 Web Audio synthesizers without external framework bloat.
2. **Visual Design Rigor:** Implements cutting-edge dark-mode glassmorphic aesthetics that elevate user engagement while maintaining strict WCAG AA contrast ratios and responsive viewport scalability.
3. **Reliable Offline-First Persistence:** Leverages HTML5 LocalStorage with atomic mutation guards, defensive exception handling, and deterministic seed recovery to ensure bulletproof stability.
4. **Quantitative Engineering:** Rigorously sizes the system through IFPUG Function Point Analysis (171.36 AFP) and plans execution using PERT/CPM and Gantt scheduling across a 16-week semester lifecycle.

### Abbreviations & Glossary
| Term | Meaning in this report |
|---|---|
| **AFP** | Adjusted Function Points (quantified functional size after environmental adjustment) |
| **AMC** | Annual Maintenance Contract / Academic Monitoring Committee |
| **API** | Application Programming Interface |
| **CRUD** | Create, Read, Update, Delete (data entity management operations) |
| **DFD** | Data Flow Diagram (graphical representation of data movement through a system) |
| **DOM** | Document Object Model (browser HTML hierarchy) |
| **EIF** | External Interface File (logical data maintained external to the application) |
| **FP / FPA** | Function Point / Function Point Analysis (IFPUG sizing methodology) |
| **GSC** | General System Characteristics (14 environmental complexity factors in FPA) |
| **HOD** | Head of Department |
| **IFPUG** | International Function Point Users Group |
| **ILF** | Internal Logical File (user-identifiable logical data maintained inside the application) |
| **KPI** | Key Performance Indicator (metrics such as average attendance percentage) |
| **RBAC** | Role-Based Access Control (restricting system capabilities based on user role) |
| **SLOC** | Source Lines of Code (metric used in COCOMO cost estimation) |
| **SPA** | Single Page Application (web app loading a single HTML page and updating dynamically) |
| **SRS** | Software Requirements Specification |
| **UFP** | Unadjusted Function Points |
| **VAF** | Value Adjustment Factor (derived from the 14 GSC ratings) |
| **WBS** | Work Breakdown Structure (hierarchical decomposition of project phases) |
"""
    output_path = "AttendX_Software_Engineering_Documentation.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"AttendX Markdown documentation generated at: {output_path}")

if __name__ == "__main__":
    build_md()
