# AttendX Complete User & Operational Flows
## End-to-End User Journey & Interaction Workflows

**Version:** 1.0.0  
**Project:** AttendX – Smart Attendance Monitoring & Parent Notification System  

---

### 1. High-Level Universal User Journey

```mermaid
graph TD
    A[Visitor Lands on AttendX Landing Page] --> B{User Chooses Action}
    B -->|Explore Public Features| C[3D Interactive Hero & Live Simulator]
    B -->|Authenticate| D[Open Role Selector Modal]
    D --> E[Select Persona: Admin / Teacher / Parent / Student]
    E --> F[Enter Credentials or Click 1-Click Demo Fill]
    F --> G[Authenticate & Enter Respective Portal]
    G --> H[Session Managed in LocalStorage]
    H --> I[Role Switcher Available from Top Nav]
```

---

### 2. Admin Operational Flow

```mermaid
graph TD
    A1[Admin Enters Command Center] --> A2[Review Real-Time KPIs & Campus Health]
    A2 --> A3[Inspect Low Attendance Watchlist <75%]
    A3 --> A4[Click 'Send Notice' to Alert At-Risk Students]
    A2 --> A5[Open Student Management Directory]
    A5 --> A6[Add New Student / Edit Existing / Delete]
    A2 --> A7[Open Institutional Analytics]
    A7 --> A8[Analyze Class Trends & Subject Breakdowns]
    A2 --> A9[Generate Institutional Audit Reports]
    A9 --> A10[Filter Records & Print / Download CSV]
```

**Step-by-step Execution:**
1. Login with Admin credentials (`admin@attendx.edu` / `admin123`).
2. Verify total active students (1,250), present count (1,156), and campus average (92.4%).
3. Track real-time attendance trends on dynamic neon charts.
4. Drill down to students with low attendance (<75%) and trigger direct reminders.
5. Search or filter the student directory; add new students with parent contact links.

---

### 3. Teacher Operational Flow (Attendance Taking & Parent Dispatch)

```mermaid
graph TD
    T1[Teacher Enters Portal] --> T2[Select Class: e.g., CS-3A]
    T2 --> T3[Select Subject: Machine Learning]
    T3 --> T4[Select Session Date: Today]
    T4 --> T5[Student Roster Loads Automatically]
    T5 --> T6[Toggle Status: Present / Absent / Late]
    T5 --> T7[Optional: Click 'Mark All Present' for Quick Baseline]
    T7 --> T8[Adjust Individual Absentees & Late Arrivals]
    T8 --> T9[Click 'Save Attendance' Button]
    T9 --> T10[Toast Notification: 'Attendance Saved Successfully']
    T10 --> T11[Click 'Notify Parents' Action Button]
    T11 --> T12[System Automatically Dispatches Targeted Parent Alerts]
    T12 --> T13[Records Stored in LocalStorage & Parent Portals Updated]
```

**Step-by-step Execution:**
1. Login with Teacher credentials (`prof.elena@attendx.edu` / `teacher123`).
2. Select target class and subject.
3. Roster dynamically displays students with instant status buttons (🟢 Present, 🔴 Absent, 🟡 Late).
4. Teacher marks attendance with live status counters tallying totals.
5. Click **"Save Attendance"** -> triggers local persistence and success banner.
6. Click **"Notify Parents"** -> automated dispatch sends notifications specifically to parents whose children are marked absent or late.

---

### 4. Parent Operational Flow (Real-Time Child Monitoring)

```mermaid
graph TD
    P1[Parent Enters Portal] --> P2[View Linked Child Profile: Leo Chen]
    P2 --> P3[Check Today's Status: Present / Absent / Late]
    P2 --> P4[Inspect Circular Attendance Ring: 92%]
    P2 --> P5[Open Monthly Interactive Calendar]
    P5 --> P6[Review Green/Red/Yellow Date Tiles]
    P6 --> P7[Click Date to View Lecture-by-Lecture Breakdown]
    P2 --> P8[Review Absence Alert Feed]
    P8 --> P9[Click 'Acknowledge' on Teacher Absence Alert]
    P2 --> P10[Send Direct Inquiry Message to Subject Teacher]
    P2 --> P11[Download or Print Official Monthly Attendance Report]
```

**Step-by-step Execution:**
1. Login with Parent credentials (`parent.sharma@attendx.edu` / `parent123`).
2. Immediately observe child's real-time campus presence and attendance percentage.
3. Check notification feed: if child was marked absent today by the teacher, a high-priority red alert card is visible.
4. Parent clicks "Acknowledge" to log receipt of the alert.
5. Parent uses the internal message composer to communicate with the professor if leave was pre-authorized.
6. Downloads or prints the verified attendance statement.

---

### 5. Student Operational Flow (Self-Tracking & Engagement)

```mermaid
graph TD
    S1[Student Enters Portal] --> S2[Greeted by Personalized Dashboard]
    S2 --> S3[Check Active Attendance Streak: 🔥 12 Days]
    S2 --> S4[View Today's Completed and Upcoming Lectures]
    S2 --> S5[Inspect Subject-Wise Attendance Bars]
    S5 --> S6{Any Subject <75%?}
    S6 -->|Yes| S7[Display Glowing Red Warning Banner & Safe Cutoff Target]
    S6 -->|No| S8[Display Green Good Standing Status]
    S2 --> S9[Review Monthly Attendance Calendar & Records]
```

**Step-by-step Execution:**
1. Login with Student credentials (`student.leo@attendx.edu` / `student123`).
2. Personalized dashboard presents attendance streak and today's timetable.
3. Student inspects subject progress bars (e.g., Mathematics: 94%, CS: 91%, English: 96%, Physics: 87%).
4. If attendance dips under 75%, an interactive warning banner advises how many consecutive lectures are needed to restore good standing.

---

### 6. Notification Engine Flow

```mermaid
sequenceDiagram
    autonumber
    participant Source as Teacher / Admin Dispatcher
    participant Store as AttendX Storage Engine
    participant Audio as Web Audio Synthesizer
    participant UI as Toast & Drawer UI
    participant Recipient as Parent / Student

    Source->>Store: Send Notification (type, targetId, title, message, severity)
    Store->>Store: Append record to attendx_v1_notifications in LocalStorage
    Store->>Audio: Trigger cybernetic alert frequency (880Hz -> 440Hz)
    Store->>UI: Render slide-in glassmorphic Toast notification
    Store->>UI: Increment unread badge counter in navigation bar
    Recipient->>UI: Opens Notification Drawer
    UI->>Recipient: Displays chronological alert cards with quick actions
    Recipient->>UI: Clicks "Mark as Read" or "Acknowledge"
    UI->>Store: Updates read status in LocalStorage
```
