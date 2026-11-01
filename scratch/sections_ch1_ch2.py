import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_chapter1_and_chapter2(doc, helpers):
    add_chapter_header = helpers['add_chapter_header']
    add_h2 = helpers['add_h2']
    add_h3 = helpers['add_h3']
    add_h4 = helpers['add_h4']
    add_p = helpers['add_p']
    add_bullet = helpers['add_bullet']
    add_numbered_item = helpers['add_numbered_item']
    create_table = helpers['create_table']

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    add_chapter_header("1", "INTRODUCTION")

    add_p("The AttendX \u2013 Smart Attendance Monitoring & Parent Notification System is a futuristic, web-based software application engineered to simplify, automate, and modernize the process of student attendance tracking, institutional defaulter detection, and real-time parental communication in higher education and secondary educational institutions. It provides a centralized, role-segregated digital platform where college administrators, professors, parents, and students can interact transparently to foster academic discipline, eliminate proxy marking, and proactively address low attendance before university examination debarment.")

    add_p("In traditional college setups, attendance is manually marked on paper registers or entered periodically into fragmented spreadsheets. This legacy methodology is error-prone, highly labor-intensive, and fails to notify parents in real time when their child misses lectures. Consequently, parents remain completely unaware of chronic absenteeism until the end of the semester, when statutory university attendance requirements (such as the mandatory 75% threshold mandated by UGC and AICTE) have already been violated. AttendX eliminates this severe institutional disconnect by combining rapid, single-click roster marking for teachers with automated, instantaneous multi-channel notifications (SMS, WhatsApp, and email alerts) dispatched directly to parents.")

    add_p("The platform is engineered with a modern dark-mode glassmorphic 3D aesthetic that delivers high responsiveness, visual clarity, and intuitive navigation across desktop and mobile browsers. By leveraging HTML5, CSS3, JavaScript (ES6+), Chart.js data visualization, and synchronized client-side Web Storage backed by Node.js microservices, AttendX provides an enterprise-grade control system that guarantees immediate data consistency, zero paper dependency, and comprehensive auditability.")

    # 1.1 Background
    add_h2("1.1 Background")
    add_p("Regular student attendance is a direct predictor of academic performance, cognitive development, and classroom engagement. Across accredited engineering institutions and universities, governing bodies strictly mandate that every registered student maintain a minimum cumulative attendance of 75% in theory lectures and practical laboratories to remain eligible for term-end semester examinations.")

    add_p("Despite this critical academic requirement, conventional attendance management in colleges continues to suffer from four deep-rooted structural vulnerabilities:")
    add_numbered_item("1", "Vulnerability to Proxy Attendance and Manipulation:", "Physical attendance rosters passed around crowded lecture halls facilitate proxy roll calls and unverified initials, distorting institutional records.")
    add_numbered_item("2", "Cumbersome Administrative Overhead:", "Professors spend significant lecture time calling out roll numbers and hundreds of hours at semester-end manually consolidating monthly attendance ledgers.")
    add_numbered_item("3", "Delayed Identification of Defaulters:", "Because paper registers are compiled weeks after lectures occur, students slipping below the 75% threshold are flagged only when examination hall tickets are processed, leaving zero window for remedial recovery.")
    add_numbered_item("4", "Zero Real-Time Transparency for Parents:", "Working parents have virtually no daily insight into whether their child arrived safely at college or attended specific subject lectures, learning of severe attendance shortages only when formal suspension or detainment notices arrive.")

    add_p("AttendX was conceptualized and developed to address these specific operational challenges by providing an automated, real-time, transparent attendance monitoring ecosystem. It introduces a closed-loop governance cycle: faculty mark attendance digitally in seconds; the system recalculates attendance percentages on the fly; defaulters falling below 75% are immediately flagged; and automated alerts are instantaneously dispatched to guardians.")

    # 1.2 Objectives
    add_h2("1.2 Objectives")
    add_p("The core objectives of the AttendX Smart Attendance Monitoring & Parent Notification System are systematically formulated as follows:")
    add_numbered_item("1", "Efficient Digital Attendance Management:", "To allow professors and subject teachers to mark, update, and manage subject-wise lecture and laboratory attendance rapidly through an interactive, digital roster workspace.")
    add_numbered_item("2", "Automated Defaulter Detection (<75%):", "To provide an automated evaluation engine that continuously computes cumulative attendance percentages, dynamically flags defaulters below the statutory 75% threshold, and highlights critical risks.")
    add_numbered_item("3", "Instant Multi-Channel Parental Notifications:", "To automatically generate and dispatch real-time attendance alerts to parents/guardians via simulated SMS, WhatsApp, and email webhooks immediately after attendance is submitted.")
    add_numbered_item("4", "Role-Segregated Transparent Dashboards:", "To provide tailored, highly intuitive user interfaces for Central Administrators (Academic Dean), Teachers, Parents, and Students with strictly enforced role-based permissions.")
    add_numbered_item("5", "Interactive Calendar & Drilldown Analytics:", "To provide parents and students with a color-coded day-wise monthly attendance calendar, subject-by-subject percentage breakdowns, and consecutive absence tracking.")
    add_numbered_item("6", "Proactive Attendance Recovery Advice:", "To equip students with an intelligent self-service advisor that calculates exactly how many consecutive upcoming lectures must be attended to regain 75% eligibility.")
    add_numbered_item("7", "Campus-Wide Visual Analytics and Audit Export:", "To empower academic deans and heads of department with real-time graphical KPI charts, departmental comparisons, and one-click master CSV audit logs for administrative governance.")

    # 1.3 Purpose, Scope & Applicability
    add_h2("1.3 Purpose, Scope & Applicability")
    
    add_h3("1.3.1 Purpose")
    add_p("The primary purposes of the AttendX platform are defined as follows:")
    add_numbered_item("1", "Simplifying and Accelerating Attendance Workflows:", "To replace cumbersome paper registers with an ultra-fast digital roster allowing teachers to mark an entire class of students with bulk-toggle shortcuts in under 30 seconds.")
    add_numbered_item("2", "Bridging the Campus-Parent Communication Gap:", "To establish direct, automated, and immediate communication between the institution and parents, ensuring guardians are informed the exact instant a student is marked absent or late.")
    add_numbered_item("3", "Enabling Early Proactive Academic Intervention:", "To shift attendance management from punitive post-semester debarment to proactive real-time counseling, allowing students to recover before examination cutoffs.")
    add_numbered_item("4", "Eliminating Proxy Marking and Human Errors:", "To establish an accountable, time-stamped digital audit trail that records which faculty member submitted attendance for each specific session.")
    add_numbered_item("5", "Providing Data-Driven Institutional Governance:", "To furnish academic deans with immediate macro-level metrics on departmental attendance trends, faculty lecture progress, and campus-wide compliance.")

    add_h3("1.3.2 Scope")
    add_p("The operational scope of the AttendX system encompasses the following comprehensive functional domains:")
    add_numbered_item("1", "User Authentication & Role Governance:", "Secure access control for four distinct stakeholder personas (Administrator, Teacher, Parent, Student) featuring 1-click credentialed demo switchers for evaluation.")
    add_numbered_item("2", "Roster & Session Attendance Marking:", "Interactive roster grids supporting 'Present', 'Absent', and 'Late' status toggles, bulk 'Mark All Present', and real-time tally computation.")
    add_numbered_item("3", "Automated Defaulter & Consecutive Absence Logic:", "Instant mathematical evaluation of student attendance ratios against the statutory 75% benchmark, with special escalation for consecutive missed lectures.")
    add_numbered_item("4", "Multi-Channel Notification Dispatch Engine:", "Simulated multi-gateway dispatch subsystem generating tailored SMS, WhatsApp, and webhook alert payloads with personalized student and subject details.")
    add_numbered_item("5", "Parent Guardian Portal:", "A dedicated portal displaying overall attendance gauges, month-by-month interactive calendar grids, subject-wise statistics, and a two-way counseling message thread.")
    add_numbered_item("6", "Student Self-Service Portal & Recovery Engine:", "Student workspace displaying personalized attendance metrics, subject cards, teacher feedback, and an automated projection calculator predicting future recovery lectures.")
    add_numbered_item("7", "Campus Visual Analytics & Audit Logging:", "Executive visual dashboards featuring dynamic Chart.js canvas elements (pie and bar distributions), department comparison metrics, and institutional CSV export facilities.")

    add_h3("1.3.3 Applicability")
    add_p("The AttendX system is engineered with high architectural modularity, making it readily applicable across diverse academic and vocational learning environments:")
    add_numbered_item("1", "Colleges and Universities:", "Autonomous engineering institutes, polytechnics, and university departments requiring rigorous compliance with UGC/AICTE 75% attendance mandates and timely parent notifications.")
    add_numbered_item("2", "Higher Secondary Schools & Junior Colleges:", "High schools where daily student punctuality and immediate guardian intimation are essential for student safety and institutional discipline.")
    add_numbered_item("3", "Coaching Institutes & Competitive Examination Centers:", "Test-prep academies (JEE, NEET, GATE) where daily attendance tracking and parental transparency directly impact student performance.")
    add_numbered_item("4", "Faculty Members & Course Coordinators:", "Individual professors seeking to automate their classroom records and generate instant attendance ledgers without manual tallying.")
    add_numbered_item("5", "Academic Counseling and Mentorship Committees:", "Institutional mentor-mentee cells that require reliable attendance drilldown logs to conduct targeted academic counseling sessions.")
    add_numbered_item("6", "Corporate Training and Apprenticeship Programs:", "Enterprise internship programs monitoring apprentice participation, session completion rates, and contractual attendance compliance.")

    # 1.4 Achievements
    add_h2("1.4 Achievements")
    add_p("The conceptualization, implementation, and verification of the AttendX project resulted in the following key engineering achievements:")
    add_numbered_item("1", "Centralized Multi-Role Architecture:", "Successfully developed and unified four specialized user workspaces (Admin, Teacher, Parent, Student) under a single cohesive web application.")
    add_numbered_item("2", "Ultra-Rapid Single-Click Roster Marking:", "Implemented an interactive digital roster workspace enabling faculty to complete an entire lecture session marking in less than 30 seconds.")
    add_numbered_item("3", "Real-Time 75% Defaulter Detection Engine:", "Engineered an automatic calculation algorithm that dynamically flags students falling below the mandatory 75% threshold instantly upon session submission.")
    add_numbered_item("4", "Automated Parental Notification Pipeline:", "Constructed a multi-channel alert engine that formats and dispatches customized SMS, WhatsApp, and email alert payloads immediately upon student absence.")
    add_numbered_item("5", "Interactive Parent Guardian Calendar:", "Created a full-featured monthly attendance calendar with visual color codes (Green: Present, Red: Absent, Amber: Late, Blue: Holiday/Event) for parent drilldown.")
    add_numbered_item("6", "Intelligent Student Recovery Advisor:", "Developed a mathematical recovery algorithm that computes and guides students on the exact number of consecutive upcoming lectures needed to achieve 75% compliance.")
    add_numbered_item("7", "Executive Campus Visual Analytics Hub:", "Integrated Chart.js dynamic visualizers to render department-wise attendance comparisons, defaulter ratios, and real-time institutional KPIs.")
    add_numbered_item("8", "Resilient State Management & Web Storage Persistence:", "Implemented a centralized reactive Store class with synchronized LocalStorage persistence that guarantees zero data loss across page reloads.")
    add_numbered_item("9", "Institutional Audit Logging & Master CSV Export:", "Engineered an administrative reporting module that generates fully formatted, timestamped CSV files capturing historical attendance records for college records.")
    add_numbered_item("10", "Cybernetic Dark-Mode Glassmorphic User Interface:", "Designed an accessible, futuristic 3D glassmorphic UI using modern CSS backdrop filters, responsive flex/grid layouts, and cyberpunk audio-visual feedback.")

    # 1.5 Organization of The Report
    add_h2("1.5 Organization of The Report")
    add_p("This documentation is systematically organized into seven comprehensive chapters and a formal references section, following the academic engineering report standards exemplified in the reference SQMS specification:")
    
    add_bullet("Provides an executive overview of AttendX, its institutional background, core operational objectives, purpose, scope, applicability across educational bodies, and major project achievements.", bold_prefix="Chapter 1 \u2013 Introduction: ")
    add_bullet("Surveys the technology stack and development environment utilized to construct the platform, including HTML5, CSS3, JavaScript (ES6+), Chart.js, Node.js, Express, LocalStorage API, and Visual Studio Code.", bold_prefix="Chapter 2 \u2013 Survey of Technologies: ")
    add_bullet("Details the problem definition, software requirements specification (SRS with functional and non-functional requirements), project scheduling (Gantt chart and PERT analysis), hardware/software environments, Function Point (FP) analysis, and preliminary product description.", bold_prefix="Chapter 3 \u2013 Requirements and Analysis: ")
    add_bullet("Presents the end-to-end design of AttendX, including basic modules, database schema design, data integrity constraints, procedural design, logic workflows, data structures, algorithms, UI design, security issues, test case design, and 10 detailed UML diagrams (Use Case, Class, Object, State Chart, Activity, Sequence, Collaboration, Component, and Deployment).", bold_prefix="Chapter 4 \u2013 System Design: ")
    add_bullet("Examines the coding details and architecture across index.html, store.js, app.js, charts.js, and server.js, followed by the testing approach (unit, integration, beta, and regression) and a comprehensive 15-scenario formal verification test report.", bold_prefix="Chapter 5 \u2013 Implementation and Testing: ")
    add_bullet("Presents the implementation outcomes and visual evidence through high-resolution screenshots and detailed technical explanations for all 9 key system interfaces, supported by performance latency benchmarks.", bold_prefix="Chapter 6 \u2013 Results and Discussion: ")
    add_bullet("Summarizes the completed engineering project, evaluates the institutional significance of AttendX, outlines operational limitations, and articulates future enhancements (biometrics, WhatsApp Business API, mobile apps).", bold_prefix="Chapter 7 \u2013 Conclusion: ")
    add_bullet("Lists the official technical documentation, books, standards, and online learning resources consulted during the development of the system.", bold_prefix="References: ")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 2: SURVEY OF TECHNOLOGIES
    # =========================================================================
    add_chapter_header("2", "SURVEY OF TECHNOLOGIES")

    add_p("The AttendX Smart Attendance Monitoring & Parent Notification System is developed using modern web engineering technologies that combine to provide a fast, resilient, responsive, and visually compelling platform. These technologies support the development of the user interface, client-side reactive state management, asynchronous data visualization, simulated notification dispatch, and backend microservice hosting. The careful selection of lightweight web technologies ensures that the application runs seamlessly in modern desktop and mobile browsers without requiring complex local database installations.")

    # 2.1 HTML5
    add_h2("2.1 HTML5 & Semantic Web Technologies")
    add_p("HTML5 (HyperText Markup Language 5) provides the core structural skeleton and semantic hierarchy for the AttendX platform. Semantic elements such as <header>, <nav>, <main>, <section>, <article>, and <footer> are utilized to organize application modules into clean, accessible documents. Form input controls, modal containers, and canvas elements are integrated natively.")
    add_p("Key Features of HTML5:")
    add_bullet("Provides clean semantic elements that enhance accessibility and structured document navigation.")
    add_bullet("Supports native form validation, input controls, and modal dialog containers.")
    add_bullet("Enables hardware-accelerated 2D graphics rendering through the HTML5 <canvas> element.")
    add_bullet("Offers built-in web storage interfaces (LocalStorage and SessionStorage) for client-side persistence.")
    add_bullet("Ensures high compatibility across modern desktop, tablet, and smartphone web browsers.")

    # 2.2 CSS3
    add_h2("2.2 CSS3 & Glassmorphism Design System")
    add_p("CSS3 (Cascading Style Sheets 3) controls the visual styling, responsive grid layouts, animations, and cyberpunk aesthetic of AttendX. The application implements an advanced Glassmorphism design system using CSS custom properties (variables), backdrop filters (blur), multi-stop linear gradients, translucent RGBA color palettes, and box-shadow depth layers to create an engaging 3D control deck experience.")
    add_p("Key Features of CSS3:")
    add_bullet("Implements backdrop-filter: blur() to produce modern frosted glass translucent UI cards.")
    add_bullet("Uses CSS Flexbox and CSS Grid to construct responsive layouts adaptable to all screen sizes.")
    add_bullet("Leverages CSS custom properties (--color-bg, --color-cyan, --glass-border) for unified theming.")
    add_bullet("Provides smooth CSS transitions, hover transforms, and pulse animations for interactive UI elements.")
    add_bullet("Maintains a futuristic dark-mode color scheme optimized for visual comfort during prolonged use.")

    # 2.3 JavaScript
    add_h2("2.3 JavaScript (ES6+) & DOM Engine")
    add_p("JavaScript (ECMAScript 2020+) is the core scripting language driving the dynamic behavior, reactive state updates, and DOM interactions in AttendX. The system employs modern ES6+ features including classes, arrow functions, template literals, destructuring, the Spread operator, promises, and the Web Audio API to deliver instant UI updates without whole-page reloads.")
    add_p("Key Features of JavaScript (ES6+):")
    add_bullet("Drives dynamic DOM manipulation, modal popups, and view transitions asynchronously.")
    add_bullet("Implements object-oriented classes (Store, AttendXCharts) for clean modular separation.")
    add_bullet("Provides custom event pub/sub mechanisms for reactive state synchronization across views.")
    add_bullet("Calculates attendance percentages, defaulter classifications, and recovery metrics in real time.")
    add_bullet("Utilizes the Web Audio API to generate synthetic cyberpunk audio feedback tones upon user actions.")

    # 2.4 Chart.js
    add_h2("2.4 Chart.js & Interactive Data Visualization")
    add_p("Chart.js is a high-performance open-source JavaScript library utilized in AttendX to render dynamic, interactive graphical charts on HTML5 <canvas> elements. In AttendX, Chart.js powers the Campus Visual Analytics hub, generating department-wise attendance bar comparisons, defaulter-to-regular student doughnut distributions, and monthly attendance trend curves.")
    add_p("Key Features of Chart.js:")
    add_bullet("Renders crisp canvas-based responsive charts supporting retina displays and mobile screens.")
    add_bullet("Supports neon gradient fills, animated tooltips, and interactive legends matching dark themes.")
    add_bullet("Offers animated transitions when attendance data changes dynamically.")
    add_bullet("Provides robust configuration for custom scales, gridlines, fonts, and numeric formatting.")
    add_bullet("Lightweight footprint with zero external dependencies, ensuring instant page loading.")

    # 2.5 Node.js & Express
    add_h2("2.5 Node.js & Express HTTP Microservices")
    add_p("Node.js is an asynchronous, event-driven JavaScript runtime environment that executes JavaScript code outside a web browser. In AttendX, a lightweight Node.js HTTP server (configured via server.js) provides static file delivery, correct MIME-type streaming, and mock API endpoints on port 8080. This enables the application to run either locally as a self-contained server or in cloud-hosted Node environments.")
    add_p("Key Features of Node.js & Express:")
    add_bullet("Employs an asynchronous, non-blocking I/O model for fast request handling.")
    add_bullet("Serves static assets (HTML, CSS, JS, images, fonts) with proper MIME headers and caching.")
    add_bullet("Facilitates simulated backend REST API endpoints for attendance records and alert dispatch.")
    add_bullet("Requires minimal dependencies, utilizing native HTTP, File System, and Path modules.")
    add_bullet("Cross-platform runtime compatible with Windows, macOS, and Linux servers.")

    # 2.6 LocalStorage
    add_h2("2.6 LocalStorage & Web Storage Persistence API")
    add_p("The Web Storage API (specifically LocalStorage) is used as the primary client-side persistence mechanism in AttendX. The application stores structured JSON trees containing student rosters, teacher profiles, attendance session logs, parent notification dispatches, and user accounts. This allows users to test the full system offline, refresh pages, and switch roles without data loss.")
    add_p("Key Features of LocalStorage:")
    add_bullet("Stores up to 5 MB of structured JSON key-value data persistently within the browser sandbox.")
    add_bullet("Synchronous read/write operations provide instantaneous UI updates (<5 ms latency).")
    add_bullet("Survives page reloads, browser restarts, and offline disconnects without session resets.")
    add_bullet("Allows instant factory reset to default seed data via a single store method call.")
    add_bullet("Completely eliminates the requirement for local SQL database setup during demos and evaluations.")

    # 2.7 Notification APIs
    add_h2("2.7 Multi-Channel Notification Dispatch APIs")
    add_p("AttendX incorporates a simulated multi-channel notification dispatch architecture designed to mirror commercial SMS gateways (such as Twilio), WhatsApp Business API webhooks, and SMTP email services. When a student is marked absent or late, the system generates standardized, personalized alert payloads and updates an in-memory audit log and parent notification drawer.")
    add_p("Key Features of Notification Subsystem:")
    add_bullet("Generates personalized alert templates containing student name, subject, date, and status.")
    add_bullet("Supports multi-channel payload formatting (SMS, WhatsApp, and Webhook/Email).")
    add_bullet("Maintains an immutable historical dispatch log for parent verification and institutional audit.")
    add_bullet("Simulates real-world delivery latency and acknowledgment receipts for realistic demonstration.")
    add_bullet("Architecturally prepared for plug-and-play connection to production Twilio/Meta API keys.")

    # 2.8 Visual Studio Code
    add_h2("2.8 Visual Studio Code IDE")
    add_p("Visual Studio Code (VS Code) was the primary integrated development environment (IDE) utilized for authoring, debugging, and managing the AttendX codebase. Its extensive ecosystem of web development extensions, integrated terminal, Git version control, and live reloading tools significantly accelerated development.")
    add_p("Key Features of Visual Studio Code:")
    add_bullet("Provides intelligent code completion (IntelliSense) for JavaScript, HTML5, and CSS3.")
    add_bullet("Features an integrated terminal supporting PowerShell, Bash, and Node CLI execution.")
    add_bullet("Includes built-in Git source control integration for commit tracking and branch management.")
    add_bullet("Supports extensions such as Live Server, Prettier, and ESLint for code formatting and testing.")
    add_bullet("Offers fast project workspace navigation and file searching across large codebases.")

    # 2.9 Modern Web Browsers
    add_h2("2.9 Modern Web Browsers & Chrome DevTools")
    add_p("Modern web browsers (Google Chrome, Microsoft Edge, Mozilla Firefox) served as the runtime execution and testing environment for AttendX. Chrome DevTools was extensively utilized to inspect DOM structures, debug JavaScript breakpoints, monitor LocalStorage keys, analyze network waterfalls, and test responsive viewports across mobile, tablet, and 4K desktop displays.")
    add_p("Key Features of Modern Browsers & DevTools:")
    add_bullet("Executes V8-powered high-speed JavaScript compilation and rendering.")
    add_bullet("Provides interactive console logging, DOM tree inspection, and dynamic CSS live-editing.")
    add_bullet("Features dedicated Application tab for viewing, modifying, and clearing LocalStorage entries.")
    add_bullet("Includes device emulation mode to test mobile and tablet responsive layouts.")
    add_bullet("Supports Lighthouse audits for verifying performance, accessibility, and web best practices.")

    # 2.10 Google Firebase Cloud Platform & Firestore
    add_h2("2.10 Google Firebase Cloud Platform & Cloud Firestore")
    add_p("Google Firebase is a comprehensive cloud backend-as-a-service (BaaS) platform providing real-time NoSQL cloud databases, authentication, hosting, and cloud messaging. In AttendX, Cloud Firestore is integrated via a dual-mode reactive bridge to synchronize attendance sessions, student cumulative metrics, real-time parent notifications, and counselor chat messages across classroom and guardian devices.")
    add_p("Key Features of Google Cloud Firestore:")
    add_bullet("Offers real-time data synchronization using persistent WebSocket connections and onSnapshot streams.")
    add_bullet("Provides client-side offline persistence and automatic background resynchronization upon reconnection.")
    add_bullet("Scales horizontally with automatic indexing, sub-second query execution, and high security rules.")
    add_bullet("Enables seamless multi-device testing between teacher classroom laptops and parent mobile phones.")
    add_bullet("Supports modular configuration with customizable credentials via an integrated browser UI modal.")

    doc.add_page_break()
    print("Chapters 1 and 2 generated successfully.")

