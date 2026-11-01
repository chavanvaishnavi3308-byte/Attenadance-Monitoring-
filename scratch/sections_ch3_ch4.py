import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_chapter3_and_chapter4(doc, helpers):
    add_chapter_header = helpers['add_chapter_header']
    add_h2 = helpers['add_h2']
    add_h3 = helpers['add_h3']
    add_h4 = helpers['add_h4']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_numbered_item = helpers['add_numbered_item']
    add_fig = helpers['add_fig']
    create_table = helpers['create_table']

    # =========================================================================
    # CHAPTER 3: REQUIREMENTS AND ANALYSIS
    # =========================================================================
    add_chapter_header("3", "REQUIREMENTS AND ANALYSIS")

    add_p("The engineering of the AttendX Smart Attendance Monitoring & Parent Notification System follows a rigorous, analytical software engineering lifecycle. This chapter outlines the formal problem definition, software requirements specification (SRS with functional and non-functional requirements), project planning and scheduling (including Gantt chart modeling and PERT network analysis), runtime hardware and software specifications, Function Point (FP) sizing, and the preliminary product description.")

    # 3.1 Problem Definition
    add_h2("3.1 Problem Definition")
    add_p("In tertiary academic institutions, maintaining accurate, verifiable student attendance is a statutory prerequisite for academic governance and accreditation compliance. However, the prevalent manual attendance procedures practiced across universities exhibit critical systemic defects:")
    add_numbered_item("1", "Vulnerability to Proxy Marking and Human Error:", "Paper attendance sheets passed through classrooms allow unauthorized students to sign or mark proxies for absent peers. Furthermore, professors frequently miscalculate attendance totals during manual data consolidation at the end of each academic month.")
    add_numbered_item("2", "Excessive Consumption of Instructional Time:", "Calling out roll numbers across large lecture classes (60 to 120 students) consumes between 8 to 12 minutes of each instructional hour\u2014wasting up to 20% of scheduled academic contact time.")
    add_numbered_item("3", "Delayed Detection of Attendance Defaulters:", "Because paper registers are compiled weeks after lectures occur, students slipping below the statutory 75% attendance threshold are identified only when examination hall tickets are processed, leaving zero window for remedial counseling.")
    add_numbered_item("4", "Total Disconnect with Parents and Guardians:", "Parents have no immediate insight into their ward's classroom attendance. When chronic absenteeism leads to examination debarment, parents are blindsided and lack the temporal opportunity to intervene.")
    add_numbered_item("5", "Absence of Centralized Institutional Visibility:", "Departmental heads and deans cannot monitor real-time institutional attendance trends, faculty lecture completion rates, or class-wide attendance deficits due to isolated, fragmented paper records.")

    add_p("To eliminate these vulnerabilities, AttendX provides a centralized, digital, automated attendance monitoring system that records attendance in seconds, dynamically computes percentages, flags defaulters immediately, and dispatches instant notifications directly to parents.")

    # 3.2 Requirements Specification
    add_h2("3.2 Requirements Specification")
    
    add_h3("3.2.1 Functional Requirements")
    add_p("The functional requirements of AttendX specify the precise operational actions that the software platform must perform for each user persona:")
    add_numbered_item("FR-1", "Multi-Role User Authentication & Demo Switching:", "The system shall provide secure authentication for four stakeholder roles (Administrator, Teacher, Parent, Student). It shall support 1-click credentialed demo switcher profiles to enable swift institutional evaluation.")
    add_numbered_item("FR-2", "Teacher Interactive Attendance Roster:", "The system shall allow authenticated teachers to select assigned classes and subjects, load an interactive digital student roster, toggle individual status ('Present', 'Absent', 'Late'), and execute bulk 'Mark All Present' shortcuts.")
    add_numbered_item("FR-3", "Automated Defaulter Flagging (<75%):", "The system shall automatically recompute student cumulative attendance percentages upon session submission, dynamically classifying students with <75% cumulative attendance as 'Defaulter' with visual amber/red indicators.")
    add_numbered_item("FR-4", "Multi-Channel Parental Notification Dispatch:", "Upon recording absences or late arrivals, the system shall automatically format and dispatch instant alert payloads to parent contact profiles via simulated SMS, WhatsApp, and webhook channels, logging timestamped dispatch records.")
    add_numbered_item("FR-5", "Parent Guardian Portal & Calendar Drilldown:", "The system shall provide parents with a dedicated portal displaying ward summary metrics, an interactive color-coded monthly attendance calendar, subject-by-subject statistics, and a direct counseling inquiry thread.")
    add_numbered_item("FR-6", "Student Self-Service Portal & Recovery Advisor:", "The system shall allow students to inspect personalized attendance figures and provide an automated projection calculator indicating the exact number of consecutive upcoming lectures required to achieve or restore 75% eligibility.")
    add_numbered_item("FR-7", "Campus-Wide Visual Analytics Hub:", "The system shall aggregate campus attendance metrics, rendering dynamic Chart.js visualizers for department attendance comparisons, defaulter-to-regular ratios, and key institutional KPI summary cards.")
    add_numbered_item("FR-8", "Master Attendance Audit Log & CSV Export:", "The system shall maintain an immutable, chronological session audit log and provide single-click export of attendance rosters and defaulter summaries into standard CSV format for archiving.")

    add_h3("3.2.2 Non-Functional Requirements")
    add_p("The non-functional requirements define the architectural quality attributes, performance constraints, and user experience standards of AttendX:")
    add_numbered_item("NFR-1", "Performance & Low Latency:", "The application shall render UI views in less than 100 milliseconds and process a 60-student roster submission with percentage re-evaluations in under 50 milliseconds.")
    add_numbered_item("NFR-2", "Security & Role-Based Access Control (RBAC):", "The system shall strictly segregate UI views and actions based on the authenticated user's assigned role, preventing unauthorized access to administrative or faculty controls.")
    add_numbered_item("NFR-3", "Usability & 3D Glassmorphism Interface:", "The user interface shall adhere to a responsive cybernetic dark-mode glassmorphic design system with high contrast text, intuitive iconography, visual color-coded badges, and audio feedback.")
    add_numbered_item("NFR-4", "Reliability & Data Consistency:", "The system shall ensure that all roster updates, session logs, and notification dispatches are synchronously committed to persistent storage, guaranteeing zero data loss across page refreshes.")
    add_numbered_item("NFR-5", "Maintainability & Modularity:", "The codebase shall be structured into clean, decoupled modules (Store state controller, Charts visualizer, UI application controller) to facilitate future extension to biometric hardware and external APIs.")
    add_numbered_item("NFR-6", "Cross-Browser & Multi-Device Compatibility:", "The application shall render flawlessly across modern desktop, tablet, and mobile browsers (Chrome, Edge, Firefox, Safari) without layout distortion.")

    # 3.3 Planning and Scheduling
    add_h2("3.3 Planning and Scheduling")
    add_p("The AttendX engineering project was organized across six systematic development phases following an iterative, agile-informed software development lifecycle. The duration and milestones of each phase are outlined below.")

    sched_headers = ["Phase", "Activity / Milestone", "Planned Wks", "Actual Wks", "Milestone Deliverable"]
    sched_data = [
        ["Phase 1", "Literature Survey, Problem Formulation & SRS", "2 Weeks", "2 Weeks", "Finalized SRS & PRD Specification"],
        ["Phase 2", "System Architecture & UML Modeling", "3 Weeks", "3 Weeks", "10 UML Diagrams & Schema Specs"],
        ["Phase 3", "Cybernetic UI Design & Glassmorphism Styling", "2 Weeks", "2 Weeks", "Responsive CSS & Component Layouts"],
        ["Phase 4", "Frontend & State Controller Implementation", "4 Weeks", "4 Weeks", "Store.js, App.js, Charts.js & DOM"],
        ["Phase 5", "Backend Microservice & API Integration", "2 Weeks", "2 Weeks", "Node.js Server.js & Mock Gateways"],
        ["Phase 6", "System Verification, Testing & Documentation", "3 Weeks", "3 Weeks", "Test Report & Academic Documentation"]
    ]
    create_table(sched_headers, sched_data, [Inches(0.9), Inches(2.6), Inches(1.0), Inches(1.0), Inches(1.8)])

    add_fig("fig9_1_gantt_chart.png", "Figure 3.1: AttendX Indicative Project Gantt Chart & Phase Schedule")

    add_h3("PERT Network Analysis")
    add_p("A Program Evaluation and Review Technique (PERT) analysis was performed to identify the project's critical path and optimize task concurrency. The project activities, predecessor constraints, and estimated durations are detailed in Table 3.2:")

    pert_headers = ["Task ID", "Project Activity Description", "Predecessors", "Optimistic (a)", "Most Likely (m)", "Pessimistic (b)", "Expected (te)"]
    pert_data = [
        ["A", "Requirement Analysis & Scope Definition", "None", "1.5 Wks", "2.0 Wks", "2.5 Wks", "2.00 Wks"],
        ["B", "System Modeling & UML Architectural Design", "A", "2.5 Wks", "3.0 Wks", "3.5 Wks", "3.00 Wks"],
        ["C", "UI Glassmorphic Design & Prototype", "B", "1.5 Wks", "2.0 Wks", "2.5 Wks", "2.00 Wks"],
        ["D", "Reactive State Controller (store.js)", "B", "2.0 Wks", "2.5 Wks", "3.0 Wks", "2.50 Wks"],
        ["E", "Teacher Roster & Attendance Engine", "C, D", "2.5 Wks", "3.0 Wks", "3.5 Wks", "3.00 Wks"],
        ["F", "Parent Notification & Alert Engine", "E", "1.5 Wks", "2.0 Wks", "2.5 Wks", "2.00 Wks"],
        ["G", "Parent & Student Self-Service Portals", "E", "2.0 Wks", "2.5 Wks", "3.0 Wks", "2.50 Wks"],
        ["H", "Campus Visual Analytics & CSV Export", "E", "1.5 Wks", "2.0 Wks", "2.5 Wks", "2.00 Wks"],
        ["I", "System Integration & Verification Testing", "F, G, H", "2.0 Wks", "2.5 Wks", "3.0 Wks", "2.50 Wks"],
        ["J", "Final Academic Documentation & Review", "I", "1.0 Wks", "1.5 Wks", "2.0 Wks", "1.50 Wks"]
    ]
    create_table(pert_headers, pert_data, [Inches(0.7), Inches(2.3), Inches(0.9), Inches(0.9), Inches(0.9), Inches(0.9), Inches(0.9)])

    add_p("The Critical Path of the project traverses activities A \u2192 B \u2192 D \u2192 E \u2192 G \u2192 I \u2192 J, establishing an expected total duration of 16.5 weeks with a variance of 0.83 weeks.")

    # 3.4 Software and Hardware Requirements
    add_h2("3.4 Software and Hardware Requirements")
    add_p("To run, develop, and evaluate AttendX effectively, the following software and hardware requirements are specified:")

    req_headers = ["Category", "Minimum Requirement", "Recommended Specification"]
    req_data = [
        ["Operating System", "Windows 10 / Ubuntu 20.04 / macOS 11+", "Windows 11 / Ubuntu 22.04 / macOS Sonoma"],
        ["Runtime Environment", "Node.js v16.x LTS", "Node.js v18.x or v20.x LTS"],
        ["Web Browser", "Google Chrome 90+ / Edge 90+ / Firefox 88+", "Latest Stable Google Chrome or Microsoft Edge"],
        ["Display Resolution", "1280 \u00d7 720 (HD)", "1920 \u00d7 1080 (Full HD) or higher"],
        ["Processor (CPU)", "Dual-Core 2.0 GHz x64 processor", "Intel Core i5 / AMD Ryzen 5 Quad-Core 2.8+ GHz"],
        ["System Memory (RAM)", "4 GB RAM", "8 GB or 16 GB DDR4/DDR5 RAM"],
        ["Disk Storage", "500 MB free disk space", "2 GB SSD available storage"],
        ["Input Devices", "Standard Keyboard and Pointing Device", "Full-sized Keyboard, High-Precision Mouse/Trackpad"],
        ["Internet Connectivity", "Offline capable (Optional for initial CDN fonts)", "Broadband 10 Mbps (for external assets/APIs)"]
    ]
    create_table(req_headers, req_data, [Inches(1.8), Inches(2.7), Inches(2.8)])

    # 3.5 Function Point Sizing
    add_h2("3.5 Function Point (FP) Sizing & Estimation")
    add_p("Function Point Analysis (FPA) was conducted using IFPUG guidelines to objectively measure the functional size of the AttendX software system independently of the implementation language.")

    fp_headers = ["Functional Component Type", "Count", "Low Weight", "Avg Weight", "High Weight", "Unadjusted FP (UFP)"]
    fp_data = [
        ["Internal Logical Files (ILF)", "5 (Users, Students, Teachers, Sessions, Alerts)", "1 \u00d7 7", "3 \u00d7 10", "1 \u00d7 15", "52 UFP"],
        ["External Interface Files (EIF)", "2 (Notification Gateway, Holiday Config)", "2 \u00d7 5", "0 \u00d7 7", "0 \u00d7 10", "10 UFP"],
        ["External Inputs (EI)", "6 (Login, Roster Mark, Add User, Msg, Reset, Config)", "2 \u00d7 3", "4 \u00d7 4", "0 \u00d7 6", "22 UFP"],
        ["External Outputs (EO)", "4 (CSV Export, Alert Dispatch, Recovery Report, Tally)", "1 \u00d7 4", "3 \u00d7 5", "0 \u00d7 7", "19 UFP"],
        ["External Inquiries (EQ)", "5 (Student Lookup, Subject Roster, Calendar, Stats, History)", "2 \u00d7 3", "3 \u00d7 4", "0 \u00d7 6", "18 UFP"]
    ]
    create_table(fp_headers, fp_data, [Inches(2.2), Inches(0.7), Inches(0.9), Inches(0.9), Inches(0.9), Inches(1.1)])

    add_p("Total Unadjusted Function Points (UFP) = 52 + 10 + 22 + 19 + 18 = 121 UFP.")
    add_p("Value Adjustment Factor (VAF): Evaluating the 14 General System Characteristics (data communications, distributed processing, performance, heavily used configuration, transaction rate, online data entry, end-user efficiency, online update, complex processing, reusability, installation ease, operational ease, multiple sites, facilitative change) yields a Total Degree of Influence (TDI) of 34.")
    add_p("VAF = 0.65 + (0.01 \u00d7 TDI) = 0.65 + (0.01 \u00d7 34) = 0.99.")
    add_p("Adjusted Function Points (AFP) = UFP \u00d7 VAF = 121 \u00d7 0.99 = 119.79 AFP.")
    add_p("Using the standard QSM conversion factor of 53 Source Lines of Code (SLOC) per Function Point for JavaScript (ES6+), the estimated codebase size is approximately 119.79 \u00d7 53 \u2248 6,348 SLOC, closely matching the actual AttendX implementation footprint (~5,800 lines across HTML, CSS, and JS).")

    # 3.6 Preliminary Product Description
    add_h2("3.6 Preliminary Product Description")
    add_p("AttendX is an automated smart campus attendance management and parent notification platform designed to eliminate the administrative delays and communication barriers inherent in traditional college attendance systems. Key characteristics of the system include:")
    add_bullet("Unified Four-Tier Architecture: Tailored role-governed workspaces for Administrators (Dean), Faculty, Parents, and Students.", bold_prefix="Role Governance: ")
    add_bullet("Interactive Roster Engine: High-speed, single-click digital roster workspace with bulk attendance toggles and instant present/absent tallies.", bold_prefix="Rapid Attendance: ")
    add_bullet("Automated 75% Thresholding: Continuous, dynamic evaluation of attendance ratios against UGC/AICTE mandates with instant defaulter classification.", bold_prefix="Defaulter Detection: ")
    add_bullet("Real-Time Multi-Channel Alerts: Instantaneous generation and dispatch of personalized absence alerts via SMS, WhatsApp, and webhook simulators.", bold_prefix="Parental Notification: ")
    add_bullet("Interactive Monthly Calendar: Color-coded daily attendance drilldowns and counselor inquiry messaging for parents.", bold_prefix="Parental Engagement: ")
    add_bullet("Automated Recovery Advisor: Projection calculator that empowers students to compute the exact future lectures needed to regain eligibility.", bold_prefix="Student Recovery: ")
    add_bullet("Executive Campus Visual Analytics: Real-time graphical KPI charts, departmental comparisons, and one-click master CSV audit logs.", bold_prefix="Administrative Visibility: ")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 4: SYSTEM DESIGN
    # =========================================================================
    add_chapter_header("4", "SYSTEM DESIGN")

    add_p("The system design phase translates functional requirements into a concrete technical blueprint. This chapter details the modular decomposition of AttendX, relational database schema specifications, procedural logic workflows, data structures, algorithm designs, user interface principles, security mechanisms, test case design, and 10 detailed UML diagrams representing system structure and runtime behavior.")

    # 4.1 Basic Modules
    add_h2("4.1 Basic Modules")
    add_p("AttendX is decomposed into seven cohesive, loosely coupled basic modules, each responsible for specific functional domains:")

    mod_headers = ["Module Identifier", "Module Name", "Primary Responsibilities", "Key Inputs & Outputs"]
    mod_data = [
        ["MOD-01", "User Authentication & RBAC Module", "Manages credentials, validates passwords, establishes active user session, and enforces role-based navigation permissions.", "Input: Role, ID, Password\nOutput: Session token, Profile object"],
        ["MOD-02", "Teacher Roster & Attendance Engine", "Renders subject student rosters, captures attendance marks (Present/Absent/Late), computes session tallies, and commits attendance logs.", "Input: Class, Subject, Date, Status Map\nOutput: Session record, Updated tallies"],
        ["MOD-03", "Defaulter & Metric Recalculation Engine", "Recalculates attended/total lectures, computes cumulative percentage, and flags defaulters (<75%) and consecutive absences.", "Input: Student attendance history\nOutput: Attendance %, Status flag"],
        ["MOD-04", "Parental Multi-Channel Notification Engine", "Filters absent/late students, interpolates alert message templates, and dispatches SMS/WhatsApp/Webhook notifications to parents.", "Input: Absentee list, Parent contacts\nOutput: Dispatch payload, Audit record"],
        ["MOD-05", "Parent Guardian Portal Module", "Renders ward summary metrics, color-coded monthly attendance calendar, subject-wise statistics, and two-way inquiry messaging.", "Input: Parent session, Ward ID\nOutput: Calendar DOM, Message logs"],
        ["MOD-06", "Student Self-Service & Recovery Module", "Displays student personal metrics, subject breakdown cards, and an interactive calculator projecting future recovery lectures.", "Input: Student session, Target %\nOutput: Recovery projection count"],
        ["MOD-07", "Campus Visual Analytics & Export Module", "Aggregates campus-wide attendance stats, renders Chart.js visualizers, and formats master attendance audit logs into downloadable CSV.", "Input: System state dataset\nOutput: Dynamic charts, Exported CSV file"]
    ]
    create_table(mod_headers, mod_data, [Inches(0.9), Inches(1.8), Inches(2.4), Inches(2.0)])

    # 4.2 Data Design
    add_h2("4.2 Data Design")
    add_p("Data design defines how information is structured, related, and persistently maintained across the AttendX platform. The overall system architecture and data flow are illustrated in Figure 4.1:")

    add_fig("fig1_1_architecture.png", "Figure 4.1: AttendX Overall System Architecture & Data Flow")

    add_h3("4.2.1 Schema Design")
    add_p("The AttendX data architecture models an educational institution's organizational hierarchy using eight core entities. The technical schema definitions are detailed in the tables below:")

    # Table Users
    add_p("1. Users Table (Core Authentication & Credentials):", bold_prefix="")
    user_headers = ["Field Name", "Data Type", "Null?", "Key / Constraint", "Description / Purpose"]
    user_data = [
        ["id", "VARCHAR(32)", "NO", "PRIMARY KEY", "Unique system identifier (e.g., ADM-001, TCH-001, PRN-CS01, STD-CS01)"],
        ["name", "VARCHAR(128)", "NO", "NOT NULL", "Full display name of user (e.g., Dr. Vidya Mohod, Vaishnavi Chavan)"],
        ["email", "VARCHAR(128)", "NO", "UNIQUE", "Institutional email address used for login and notifications"],
        ["role", "VARCHAR(20)", "NO", "CHECK (role IN ...)", "User role: 'admin', 'teacher', 'parent', 'student'"],
        ["department", "VARCHAR(64)", "YES", "DEFAULT NULL", "Assigned department (e.g., 'Computer Science', 'Information Tech')"],
        ["password", "VARCHAR(128)", "NO", "NOT NULL", "Account authentication password credential"],
        ["status", "VARCHAR(20)", "NO", "DEFAULT 'active'", "Account status: 'active', 'suspended', 'pending'"],
        ["createdAt", "DATETIME", "NO", "TIMESTAMP", "Record creation timestamp"]
    ]
    create_table(user_headers, user_data, [Inches(1.1), Inches(1.2), Inches(0.6), Inches(1.8), Inches(2.4)])

    # Table Students
    add_p("2. Students Table (Academic Enrollment & Cumulative Metrics):", bold_prefix="")
    std_headers = ["Field Name", "Data Type", "Null?", "Key / Constraint", "Description / Purpose"]
    std_data = [
        ["id", "VARCHAR(32)", "NO", "PRIMARY KEY", "Unique student enrollment ID (e.g., STD-CS01, STD-IT01)"],
        ["name", "VARCHAR(128)", "NO", "NOT NULL", "Student full legal name (e.g., Vaishnavi Chavan)"],
        ["rollNo", "VARCHAR(32)", "NO", "UNIQUE", "Institutional roll number / seat number (e.g., CS-01)"],
        ["classId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Enrolled class identifier referencing Classes.id ('CLASS-CS', 'CLASS-IT')"],
        ["department", "VARCHAR(64)", "NO", "NOT NULL", "Academic department: 'Computer Science', 'Information Technology'"],
        ["overallAttendance", "DECIMAL(5,2)", "NO", "DEFAULT 0.00", "Current cumulative attendance percentage (0.00% to 100.00%)"],
        ["attendedLectures", "INT", "NO", "DEFAULT 0", "Total number of lectures student was present or late"],
        ["totalLectures", "INT", "NO", "DEFAULT 0", "Total number of conducted lectures across all subjects"],
        ["consecutiveAbsences", "INT", "NO", "DEFAULT 0", "Current count of consecutive missed sessions"],
        ["isDefaulter", "BOOLEAN", "NO", "DEFAULT FALSE", "Automated flag set to TRUE if overallAttendance < 75.00%"],
        ["parentId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Parent guardian account referencing Users.id (e.g., PRN-CS01)"]
    ]
    create_table(std_headers, std_data, [Inches(1.4), Inches(1.1), Inches(0.5), Inches(1.6), Inches(2.5)])

    # Table Teachers
    add_p("3. Teachers Table (Faculty Profiles & Course Allocation):", bold_prefix="")
    tch_headers = ["Field Name", "Data Type", "Null?", "Key / Constraint", "Description / Purpose"]
    tch_data = [
        ["id", "VARCHAR(32)", "NO", "PRIMARY KEY", "Unique faculty employee ID (e.g., TCH-001, TCH-004)"],
        ["name", "VARCHAR(128)", "NO", "NOT NULL", "Faculty member name (e.g., Swapnali Jadhav, Prof. Trupti Thakur)"],
        ["email", "VARCHAR(128)", "NO", "UNIQUE", "Institutional faculty email address"],
        ["department", "VARCHAR(64)", "NO", "NOT NULL", "Department: 'Computer Science', 'Information Technology'"],
        ["designation", "VARCHAR(64)", "NO", "NOT NULL", "Academic designation: 'Assistant Professor', 'Associate Professor'"],
        ["assignedClass", "VARCHAR(32)", "NO", "FOREIGN KEY", "Primary assigned class ID referencing Classes.id"],
        ["subjectSpecialty", "VARCHAR(64)", "NO", "NOT NULL", "Primary subject taught (e.g., 'Data Structures', 'Operating Systems')"]
    ]
    create_table(tch_headers, tch_data, [Inches(1.2), Inches(1.1), Inches(0.5), Inches(1.6), Inches(2.7)])

    # Table AttendanceSessions
    add_p("4. AttendanceSessions Table (Lecture Attendance Records):", bold_prefix="")
    ses_headers = ["Field Name", "Data Type", "Null?", "Key / Constraint", "Description / Purpose"]
    ses_data = [
        ["id", "VARCHAR(64)", "NO", "PRIMARY KEY", "Unique session hash (e.g., SES-CS-DS-20261029-01)"],
        ["classId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Class ID for which attendance was taken ('CLASS-CS', 'CLASS-IT')"],
        ["subjectId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Subject ID (e.g., 'SUB-CS-01', 'SUB-CS-02')"],
        ["date", "DATE", "NO", "NOT NULL", "Calendar date on which lecture was conducted (YYYY-MM-DD)"],
        ["teacherId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Faculty member who conducted and submitted session"],
        ["totalStudents", "INT", "NO", "NOT NULL", "Total number of students enrolled on roster"],
        ["presentCount", "INT", "NO", "NOT NULL", "Number of students marked present"],
        ["absentCount", "INT", "NO", "NOT NULL", "Number of students marked absent"],
        ["lateCount", "INT", "NO", "NOT NULL", "Number of students marked late"],
        ["statusMap", "JSON / TEXT", "NO", "NOT NULL", "JSON object mapping student IDs to status ('present'|'absent'|'late')"],
        ["timestamp", "DATETIME", "NO", "TIMESTAMP", "Exact timestamp when session was recorded into system"]
    ]
    create_table(ses_headers, ses_data, [Inches(1.2), Inches(1.1), Inches(0.5), Inches(1.6), Inches(2.7)])

    # Table Notifications
    add_p("5. Notifications Table (Parent Alert Dispatches):", bold_prefix="")
    notif_headers = ["Field Name", "Data Type", "Null?", "Key / Constraint", "Description / Purpose"]
    notif_data = [
        ["id", "VARCHAR(64)", "NO", "PRIMARY KEY", "Unique dispatch ID (e.g., NOTIF-STD-CS01-1730000000)"],
        ["studentId", "VARCHAR(32)", "NO", "FOREIGN KEY", "Student ID associated with attendance event"],
        ["recipientRole", "VARCHAR(20)", "NO", "DEFAULT 'parent'", "Target recipient role ('parent', 'student', 'admin')"],
        ["type", "VARCHAR(20)", "NO", "NOT NULL", "Alert classification ('absent', 'late', 'defaulter_warning')"],
        ["title", "VARCHAR(128)", "NO", "NOT NULL", "Short headline (e.g., 'Absence Alert \u2013 Data Structures')"],
        ["message", "TEXT", "NO", "NOT NULL", "Full formatted notification body dispatched to parent"],
        ["channel", "VARCHAR(32)", "NO", "DEFAULT 'MULTI'", "Delivery channel ('SMS', 'WhatsApp', 'Webhook', 'MULTI')"],
        ["isRead", "BOOLEAN", "NO", "DEFAULT FALSE", "Read receipt status in parent guardian notification drawer"],
        ["timestamp", "DATETIME", "NO", "TIMESTAMP", "Exact dispatch timestamp"]
    ]
    create_table(notif_headers, notif_data, [Inches(1.2), Inches(1.1), Inches(0.5), Inches(1.6), Inches(2.7)])

    # 4.2.2 Data Integrity
    add_h3("4.2.2 Data Integrity and Constraints")
    add_p("To guarantee data accuracy, consistency, and relational validity, the following structural constraints are enforced across the AttendX data tier:")
    add_numbered_item("1", "Primary Key Uniqueness:", "Every entity table utilizes an immutable, unique primary key (e.g., STD-CS01, TCH-001) preventing duplicate record insertion.")
    add_numbered_item("2", "Referential Integrity via Foreign Keys:", "Student records reference valid Class and Parent identifiers; attendance session logs reference valid Teacher, Class, and Subject records.")
    add_numbered_item("3", "Domain Range & Format Validations:", "Attendance status is strictly constrained to the enumeration ('present', 'absent', 'late'); cumulative percentages are mathematically bounded between 0.00% and 100.00%.")
    add_numbered_item("4", "Unique Academic Identity Constraints:", "Roll numbers and institutional emails are indexed with unique constraints to prevent conflicting student registrations.")
    add_numbered_item("5", "Atomic State Transactions:", "When attendance is recorded, the session log creation, student percentage updates, defaulter re-evaluations, and parent alert generations execute as an atomic transaction, preventing partial data corruption.")

    # 4.3 Procedural Design
    add_h2("4.3 Procedural Design")
    add_p("Procedural design outlines the flow of control, data transformations, logic hierarchies, and algorithmic routines that execute within AttendX.")

    add_h3("4.3.1 Logic Diagrams & Process Workflows")
    add_p("The operational data flows within AttendX are illustrated across three complementary structural levels:")
    add_bullet("Context Diagram (Level 0 DFD): Illustrates the high-level boundary of AttendX, depicting external entities (Admin, Teacher, Parent, Student) and the bidirectional flow of credentials, roster marks, alerts, and analytics reports.", bold_prefix="1. Context DFD: ")
    add_fig("fig2_1_context_dfd.png", "Figure 4.2: Context Diagram \u2013 Level 0 Data Flow Diagram")

    add_bullet("Level 1 DFD: Decomposes the central AttendX process into four sub-processes: (1.0) User Authentication, (2.0) Attendance Roster Marking, (3.0) Defaulter Detection & Alert Dispatch, and (4.0) Analytics & Report Generation.", bold_prefix="2. Level 1 DFD: ")
    add_fig("fig2_2_level1_dfd.png", "Figure 4.3: Level 1 Data Flow Diagram (Functional Decomposition)")

    add_bullet("Structured Chart: Illustrates the hierarchical top-down modular calling structure of the AttendX software controller.", bold_prefix="3. Structured Chart: ")
    add_fig("fig2_3_structured_chart.png", "Figure 4.4: AttendX Modular Structured Chart")

    add_h3("4.3.2 Data Structures")
    add_p("AttendX leverages structured in-memory JavaScript data structures optimized for rapid lookup and reactivity:")
    add_numbered_item("1", "Nested Associative Objects (Hash Maps):", "Used for student and teacher catalogs (keyed by ID for O(1) retrieval) and the session statusMap (studentId \u2192 'present'|'absent'|'late').")
    add_numbered_item("2", "Ordered Arrays of Entities:", "Used to store chronological attendance session histories, calendar day objects, and notification dispatch streams.")
    add_numbered_item("3", "JSON Serialized Blobs:", "Used to serialize the entire relational state tree into LocalStorage keys under strict schema versioning ('attendx_v2_version').")
    add_numbered_item("4", "Publish/Subscribe Event Listener Arrays:", "Maintained within the Store instance to notify subscribed UI view controllers whenever attendance data is modified.")

    add_h3("4.3.3 Algorithms Design")
    add_p("The core operational logic of AttendX is driven by five deterministic algorithms:")

    add_p("Algorithm 1: Multi-Role User Authentication & Permission Gating", bold_prefix="")
    add_p("Input: User identifier, selected role, password.\nOutput: Authenticated session object or descriptive error.")
    add_bullet("1. Read identifier, role, and password from login interface.")
    add_bullet("2. Query Store.getAccounts() matching the entered identifier and role.")
    add_bullet("3. If matching account is not found: return Error('Account not registered for this role').")
    add_bullet("4. If account.status === 'suspended': return Error('Account is suspended. Contact Admin').")
    add_bullet("5. If account.password !== enteredPassword: return Error('Invalid password credential').")
    add_bullet("6. Store authenticated user profile in LocalStorage under 'attendx_v2_currentUser'.")
    add_bullet("7. Update sidebar navigation links and render the role-specific dashboard.")

    add_p("Algorithm 2: Dynamic Attendance Percentage & Defaulter Classification", bold_prefix="")
    add_p("Input: Student attended lectures count, total conducted lectures count.\nOutput: Cumulative attendance percentage, isDefaulter boolean flag.")
    add_bullet("1. For each student enrolled in the marked class:")
    add_bullet("2. If session status === 'present' or 'late': attendedLectures = attendedLectures + 1.")
    add_bullet("3. totalLectures = totalLectures + 1.")
    add_bullet("4. Compute: percentage = (attendedLectures / totalLectures) * 100.")
    add_bullet("5. If percentage < 75.00: set isDefaulter = true; else set isDefaulter = false.")
    add_bullet("6. Update student record and commit to LocalStorage.")

    add_p("Algorithm 3: Consecutive Absence Detection & Escalation", bold_prefix="")
    add_p("Input: Student session status history.\nOutput: Consecutive absence tally, Escalation alert trigger.")
    add_bullet("1. If current session status === 'absent': consecutiveAbsences = consecutiveAbsences + 1.")
    add_bullet("2. Else if status === 'present' or 'late': consecutiveAbsences = 0 (reset tally).")
    add_bullet("3. If consecutiveAbsences >= 3: Trigger priority Defaulter Escalation Alert to Academic Counselor.")

    add_p("Algorithm 4: Parental Multi-Channel Alert Formatting & Dispatch", bold_prefix="")
    add_p("Input: ClassId, SubjectId, Date, statusMap.\nOutput: Dispatched alert payloads across SMS, WhatsApp, Webhooks.")
    add_bullet("1. Iterate through statusMap entries (studentId, status).")
    add_bullet("2. If status === 'absent' or status === 'late':")
    add_bullet("3. Retrieve student object and corresponding parentId from Store.")
    add_bullet("4. Format alert body: 'Dear Parent, your ward [StudentName] was marked [STATUS] in [SubjectName] on [Date]. Current cumulative attendance: [Percentage]%.'")
    add_bullet("5. Generate dispatch object with unique ID, timestamp, channel='MULTI', and isRead=false.")
    add_bullet("6. Append to Store notifications list and trigger parent drawer audio chime.")

    add_p("Algorithm 5: Master Attendance Audit Log & CSV Export Serialization", bold_prefix="")
    add_p("Input: Class filter, date range, student attendance records.\nOutput: Formatted RFC-4180 compliant CSV file download.")
    add_bullet("1. Construct CSV header row: 'Roll No,Student Name,Department,Attended,Total,Percentage,Status,Parent Contact'.")
    add_bullet("2. For each student matching active filter:")
    add_bullet("3. Escape special characters and format row values: [rollNo, name, department, attended, total, percentage+'%', isDefaulter ? 'DEFAULTER' : 'REGULAR', parentPhone].")
    add_bullet("4. Combine header and rows with newline delimiters (\r\n).")
    add_bullet("5. Create Blob object with MIME type 'text/csv;charset=utf-8;'.")
    add_bullet("6. Trigger client-side anchor download: 'AttendX_Master_Audit_[Date].csv'.")

    # 4.4 UI Design
    add_h2("4.4 User Interface Design")
    add_p("The AttendX user interface is crafted to combine futuristic cybernetic styling with high academic utility:")
    add_bullet("Dark-Mode 3D Glassmorphism: Frosted glass panels with backdrop blur, translucent neon cyan/blue borders, and layered drop shadows create depth without visual fatigue.", bold_prefix="Aesthetic Architecture: ")
    add_bullet("Responsive 12-Column Grid: Seamlessly scales from 360px mobile viewports to ultra-wide 4K displays.", bold_prefix="Grid System: ")
    add_bullet("Role Switcher Modal: Instant 1-click credentialed login selector enabling evaluators to test all four personas effortlessly.", bold_prefix="Accessibility: ")
    add_bullet("Audio Feedback Synthesizer: Built-in Web Audio API tone generator playing distinctive cyberpunk chimes upon success, warning, or error.", bold_prefix="Multimodal Cues: ")

    # 4.5 Security Issues
    add_h2("4.5 Security Issues")
    add_p("Security and privacy are engineered into the core architecture of AttendX:")
    add_numbered_item("1", "Strict Role-Based Access Control (RBAC):", "Client views, administrative actions, and attendance marking controls are restricted strictly to authorized role tokens.")
    add_numbered_item("2", "Input Sanitization & XSS Prevention:", "All user-supplied text inputs are sanitized through DOM text escaping before being rendered, preventing cross-site scripting.")
    add_numbered_item("3", "Parent Contact Privacy & Masking:", "Phone numbers and parent emails are displayed with middle-digit masking (e.g., +91 98****1234) on public rosters to safeguard family privacy.")
    add_numbered_item("4", "Anti-Tamper State Key Isolation:", "LocalStorage keys are isolated under a dedicated namespace with automated schema integrity validation upon boot.")

    # 4.6 Test Cases Design
    add_h2("4.6 Test Cases Design")
    add_p("Test cases were systematically designed across five testing domains: Functional, Validation, Security, Data Integrity, and Performance. The specific execution scenarios and verification criteria are formalized in Chapter 5.")

    # =========================================================================
    # SYSTEM UML MODELS (10 DIAGRAMS)
    # =========================================================================
    add_h2("System UML Models & Behavioral Diagrams")
    add_p("To comprehensively document the object-oriented structure and behavioral dynamics of AttendX, ten formal UML models were developed:")

    add_h3("1. Use Case Diagram")
    add_p("The Use Case Diagram defines the interactions between the four primary actors (Admin, Teacher, Parent, Student) and the functional use cases provided by the AttendX system:")
    add_fig("fig3_1_use_case.png", "Figure 4.5: AttendX Comprehensive Use Case Diagram")

    add_h3("2. Class Diagram")
    add_p("The Class Diagram illustrates the object-oriented domain model of AttendX, specifying attributes, operations, access modifiers, and associations between User, Student, Teacher, AttendanceSession, Notification, and Store classes:")
    add_fig("fig4_1_class_diagram.png", "Figure 4.6: AttendX Detailed Domain Class Diagram")

    add_h3("3. Object Diagram")
    add_p("The Object Diagram captures an illustrative runtime instance snapshot of the system, showing actual instantiated objects (Admin 'Dr. Vidya Mohod', Teacher 'Swapnali Jadhav', Student 'Vaishnavi Chavan', and Parent 'Rajaram Chavan'):")
    add_fig("fig4_2_object_diagram.png", "Figure 4.7: Runtime Object Diagram Instance")

    add_h3("4. State Chart Diagram")
    add_p("The State Chart Diagram models the dynamic lifecycle states of an attendance session, from Creation \u2192 Roster Loaded \u2192 In-Progress Marking \u2192 Verification \u2192 Committed & Alerts Dispatched:")
    add_fig("fig5_1_state_chart.png", "Figure 4.8: Attendance Session State Chart Diagram")

    add_h3("5. Activity Diagrams")
    add_p("Activity diagrams capture the operational workflows of the system:")
    add_bullet("Attendance Logging Activity: Workflow of teacher selecting class, toggling roster, submitting session, recalculating stats, and dispatching alerts.", bold_prefix="Roster Marking Activity: ")
    add_fig("fig5_2_activity_attendance.png", "Figure 4.9: Attendance Logging Activity Diagram")

    add_bullet("Authentication Activity: User credential verification, role-based redirection, and session initiation.", bold_prefix="Authentication Activity: ")
    add_fig("fig5_3_activity_auth.png", "Figure 4.10: Multi-Role Authentication Activity Diagram")

    add_bullet("Parent Alert Fulfilment Activity: Filtering absentees, composing message bodies, dispatching multi-channel alerts, and updating parent calendar.", bold_prefix="Parent Notification Activity: ")
    add_fig("fig5_4_activity_parent.png", "Figure 4.11: Parent Alert Fulfilment Activity Diagram")

    add_h3("6. Sequence & Collaboration Diagrams")
    add_p("The Sequence Diagram depicts the chronological message exchange between Teacher, Roster UI, Store Controller, Metric Evaluator, and Notification Dispatcher:")
    add_fig("fig6_1_sequence_attendance.png", "Figure 4.12: Attendance Marking Sequence Diagram")

    add_p("The Collaboration Diagram illustrates the structural relationship and message ordering among runtime software components:")
    add_fig("fig6_2_collaboration_diagram.png", "Figure 4.13: Roster Notification Collaboration Diagram")

    add_h3("7. Component & Deployment Diagrams")
    add_p("The Component Diagram shows the software organization into Presentation UI, Reactive Controller, Visual Analytics, and Storage layers:")
    add_fig("fig7_1_component_diagram.png", "Figure 4.14: AttendX Subsystem Component Diagram")

    add_p("The Deployment Diagram illustrates the physical nodes (Client Desktop/Mobile Browser, Node.js HTTP Application Server, Persistent Storage sandbox):")
    add_fig("fig7_2_deployment_diagram.png", "Figure 4.15: AttendX Distributed Deployment Diagram")

    doc.add_page_break()
    print("Chapters 3 and 4 generated successfully.")

