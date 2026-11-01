import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_front_matter(doc, helpers):
    add_h2 = helpers['add_h2']
    add_h3 = helpers['add_h3']
    add_p = helpers['add_p']
    create_table = helpers['create_table']

    # =========================================================================
    # COVER / TITLE PAGE
    # =========================================================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(12)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\nSMART CAMPUS ENGINEERING & TECHNOLOGY INSTITUTE")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0x24, 0x3F, 0x60)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("ATTENDX: SMART ATTENDANCE MONITORING\n& PARENT NOTIFICATION SYSTEM")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(6)
    p_sub.paragraph_format.space_after = Pt(28)
    r_sub = p_sub.add_run("A MINOR PROJECT REPORT\nSubmitted in partial fulfillment of the requirements for the Degree of\nBachelor of Technology in Computer Science & Engineering")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    # Student & Guide Details Table
    meta_headers = ["Academic Parameter", "Project Documentation Details"]
    meta_data = [
        ["Project Title", "AttendX \u2013 Smart Attendance Monitoring & Parent Notification System"],
        ["Submitted By", "Vaishnavi Chavan"],
        ["Roll No. / Seat No.", "CS-01 (Exam Seat No: 2023-CS-001)"],
        ["Degree & Branch", "Bachelor of Technology (B.Tech) \u2013 Computer Science & Engineering"],
        ["Internal Project Guide", "Prof. Trupti Thakur (Assistant Professor, Dept. of CSE)"],
        ["Head of Department & Dean", "Dr. Vidya Mohod (Head of Department & Academic Dean)"],
        ["Institution", "Smart Campus Engineering & Technology Institute"],
        ["Academic Year", "2025 \u2013 2026"],
        ["Reference Format Standard", "SQMS Academic Engineering Documentation Reference Specification"]
    ]
    create_table(meta_headers, meta_data, [Inches(2.5), Inches(4.0)])

    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(30)
    r_foot = p_foot.add_run("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\nACADEMIC YEAR 2025 \u2013 2026")
    r_foot.font.name = 'Times New Roman'
    r_foot.font.size = Pt(10)
    r_foot.font.bold = True
    r_foot.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

    doc.add_page_break()

    # =========================================================================
    # CERTIFICATE OF APPROVAL
    # =========================================================================
    p_cert_head = doc.add_paragraph()
    p_cert_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_head.paragraph_format.space_before = Pt(18)
    p_cert_head.paragraph_format.space_after = Pt(14)
    r_cert = p_cert_head.add_run("CERTIFICATE OF APPROVAL")
    r_cert.font.name = 'Times New Roman'
    r_cert.font.size = Pt(16)
    r_cert.font.bold = True
    r_cert.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    add_p("This is to certify that the minor project report entitled \"ATTENDX: SMART ATTENDANCE MONITORING & PARENT NOTIFICATION SYSTEM\" submitted by Vaishnavi Chavan (Roll No: CS-01 / Exam Seat No: 2023-CS-001) is a bona fide record of work carried out under our supervision and guidance in partial fulfillment of the requirements for the degree of Bachelor of Technology in Computer Science & Engineering from Smart Campus Engineering & Technology Institute during the academic year 2025\u20132026.")
    
    add_p("The project report has been examined and approved as satisfying the academic requirements prescribed for the minor project curriculum. The empirical demonstrations, design models, algorithm verifications, and system implementations presented in this report have been thoroughly reviewed and found to adhere to institutional academic standards.")

    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(40)
    p_sig.paragraph_format.space_after = Pt(10)

    sig_headers = ["Project Guide", "Head of Department", "External Examiner"]
    sig_data = [
        ["________________________\nProf. Trupti Thakur\nAssistant Professor\nDept. of Computer Science",
         "________________________\nDr. Vidya Mohod\nHead of Department & Dean\nDept. of Computer Science",
         "________________________\nExternal Examiner\nSeal of Institution / Date"]
    ]
    create_table(sig_headers, sig_data, [Inches(2.1), Inches(2.2), Inches(2.2)])

    doc.add_page_break()

    # =========================================================================
    # DECLARATION
    # =========================================================================
    p_dec_head = doc.add_paragraph()
    p_dec_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec_head.paragraph_format.space_before = Pt(18)
    p_dec_head.paragraph_format.space_after = Pt(14)
    r_dec = p_dec_head.add_run("CANDIDATE DECLARATION")
    r_dec.font.name = 'Times New Roman'
    r_dec.font.size = Pt(16)
    r_dec.font.bold = True
    r_dec.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    add_p("I hereby declare that the project documentation entitled \"ATTENDX: SMART ATTENDANCE MONITORING & PARENT NOTIFICATION SYSTEM\" submitted by me to the Department of Computer Science & Engineering, Smart Campus Engineering & Technology Institute, is an authentic record of original engineering and research work carried out by me under the esteemed guidance of Prof. Trupti Thakur and Dr. Vidya Mohod.")

    add_p("I further declare that this documentation, or any significant part thereof, has not been submitted previously to this or any other university or institution for the award of any degree, diploma, fellowship, or other academic recognition. The external software libraries, technical documentation standards, and frameworks utilized in the realization of this system have been duly acknowledged and cited in the references section.")

    p_cand_sig = doc.add_paragraph()
    p_cand_sig.paragraph_format.space_before = Pt(40)
    r_cand = p_cand_sig.add_run("Date: 29th October 2026\nPlace: Campus Technological Center\n\n\n_____________________________________\nVaishnavi Chavan\n(Exam Seat No: 2023-CS-001 / Roll No: CS-01)\nB.Tech Final Year, Computer Science & Engineering")
    r_cand.font.name = 'Times New Roman'
    r_cand.font.size = Pt(10.5)

    doc.add_page_break()

    # =========================================================================
    # ACKNOWLEDGEMENTS
    # =========================================================================
    p_ack_head = doc.add_paragraph()
    p_ack_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_head.paragraph_format.space_before = Pt(18)
    p_ack_head.paragraph_format.space_after = Pt(14)
    r_ack = p_ack_head.add_run("ACKNOWLEDGEMENTS")
    r_ack.font.name = 'Times New Roman'
    r_ack.font.size = Pt(16)
    r_ack.font.bold = True
    r_ack.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    add_p("The completion of this project report on \"AttendX \u2013 Smart Attendance Monitoring & Parent Notification System\" represents a major academic milestone, made possible through the constant encouragement, guidance, and support extended by numerous mentors and institutional facilitators.")

    add_p("First and foremost, I express my profound gratitude and deepest respect to my project guide, Prof. Trupti Thakur, Assistant Professor in the Department of Computer Science & Engineering, for her invaluable technical insights, constant motivation, meticulous reviews, and constructive critiques throughout the stages of system requirement analysis, architectural modeling, and software verification.")

    add_p("I take this privilege to record my heartfelt gratefulness to Dr. Vidya Mohod, Head of Department (Computer Science & Engineering) and Academic Dean, for providing the necessary infrastructural resources, state-of-the-art laboratory facilities, and an encouraging research atmosphere that enabled the seamless conceptualization and execution of this project.")

    add_p("I also extend my sincere thanks to the respected faculty members of the Computer Science and Information Technology departments\u2014specifically Prof. Swapnali Jadhav, Prof. Anuja Kanawade, and Prof. Srushti Parab\u2014for offering practical feedback on faculty roster workflows and institutional attendance governance.")

    add_p("Finally, I express my warmest gratitude to my parents, family members, and friends for their continuous patience, moral support, and inspiration throughout my academic journey.")

    doc.add_page_break()

    # =========================================================================
    # ABSTRACT
    # =========================================================================
    p_abs_head = doc.add_paragraph()
    p_abs_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_head.paragraph_format.space_before = Pt(18)
    p_abs_head.paragraph_format.space_after = Pt(14)
    r_abs = p_abs_head.add_run("ABSTRACT")
    r_abs.font.name = 'Times New Roman'
    r_abs.font.size = Pt(16)
    r_abs.font.bold = True
    r_abs.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    add_p("Traditional college attendance management systems are predominantly manual, paper-reliant, or built on fragmented legacy administrative portals characterized by sluggish user experiences, delayed defaulter detection, and near-zero real-time transparency for parents and guardians. In most university setups, student attendance is recorded on physical registers, entered into spreadsheets at semester-end, and defaulters (students below the statutory 75% attendance threshold prescribed by UGC/AICTE) are identified only days before university examinations\u2014precluding timely academic counseling or corrective recovery.")

    add_p("To overcome these institutional bottlenecks, AttendX: Smart Attendance Monitoring & Parent Notification System is developed as a futuristic, responsive, cybernetic smart campus web platform. The system operates on a responsive dark-mode 3D glassmorphic control architecture engineered with HTML5, CSS3, JavaScript (ES6+), Chart.js data visualization, and an Express/Node.js backend with synchronized Web Storage persistence. AttendX provides centralized, role-segregated workspaces tailored for four institutional user tiers: Central Administrators (Dean), Faculty / Subject Teachers, Parents / Legal Guardians, and Students.")

    add_p("Key operational capabilities of AttendX include: (1) Rapid single-click digital roster marking for faculty across lecture sessions and laboratory batches; (2) An automated dynamic defaulter evaluation engine that monitors the mandatory 75% threshold in real-time; (3) Instant multi-channel parental notification dispatch via SMS, WhatsApp, and webhook simulators whenever student absences or late arrivals occur; (4) A dedicated Parent Guardian Portal featuring interactive color-coded monthly calendar drilldowns and direct messaging with academic counselors; (5) A Student Self-Service Workspace equipped with a proactive 75% recovery advisor projecting the exact number of consecutive lectures required to regain eligibility; and (6) An executive Campus Analytics Hub offering real-time departmental KPI aggregation, pie/bar visualizers, and one-click master CSV audit exports.")

    add_p("Rigorous unit, integration, usability, and verification testing demonstrate that AttendX executes roster marking and percentage updates in under 45 milliseconds, dispatches simulated parent alerts instantaneously, and provides 100% data fidelity across browser sessions. By bridging the communication gap between academic faculty and parents, AttendX eliminates administrative overhead, eradicates proxy marking, fosters early attendance awareness, and promotes student academic success.")

    doc.add_page_break()

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    p_toc_head = doc.add_paragraph()
    p_toc_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_head.paragraph_format.space_before = Pt(18)
    p_toc_head.paragraph_format.space_after = Pt(14)
    r_toc = p_toc_head.add_run("TABLE OF CONTENTS")
    r_toc.font.name = 'Times New Roman'
    r_toc.font.size = Pt(16)
    r_toc.font.bold = True
    r_toc.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    toc_headers = ["Chapter / Section", "Title / Topic", "Reference Topic Focus"]
    toc_data = [
        ["Preliminary Pages", "Certificate, Declaration, Acknowledgements, Abstract", "Academic Front Matter"],
        ["CHAPTER 1", "INTRODUCTION", "Background, Objectives, Scope, Applicability & Achievements"],
        ["1.1", "Background", "Manual Attendance Drawbacks & Smart Campus Vision"],
        ["1.2", "Objectives", "7 Core Architectural & Operational Goals"],
        ["1.3", "Purpose, Scope & Applicability", "Functional Boundaries & Target Educational Environments"],
        ["1.3.1", "Purpose", "5 Primary Institutional Motivations"],
        ["1.3.2", "Scope", "7 Core Operational Subsystems"],
        ["1.3.3", "Applicability", "Institutional Personas & Deployment Contexts"],
        ["1.4", "Achievements", "10 Concrete Engineering Milestones"],
        ["1.5", "Organization of The Report", "Structure & Chapter-by-Chapter Road-map"],
        ["CHAPTER 2", "SURVEY OF TECHNOLOGIES", "Analysis of Frontend, Visualizer & Backend Stack"],
        ["2.1 to 2.9", "Technology Profiles (HTML5, CSS3, JS, Chart.js, Node.js, Storage)", "Key Features, Rationale & Framework Architecture"],
        ["CHAPTER 3", "REQUIREMENTS AND ANALYSIS", "Problem Definition, SRS, Planning & Sizing"],
        ["3.1", "Problem Definition", "Analysis of Legacy Inefficiencies & Proxy Marking"],
        ["3.2", "Requirements Specification", "Functional (FR-1 to FR-8) & Non-Functional (NFR-1 to NFR-6)"],
        ["3.3", "Planning and Scheduling", "Indicative Gantt Chart, PERT Analysis & Work Breakdown"],
        ["3.4", "Software and Hardware Requirements", "Minimum & Recommended Runtime Specifications"],
        ["3.5", "Function Point (FP) Sizing & Estimation", "UFP, VAF, AFP, LOC & Effort Quantification"],
        ["3.6", "Preliminary Product Description", "Executive Summary of the AttendX System Platform"],
        ["CHAPTER 4", "SYSTEM DESIGN", "Modules, Schemas, Procedural Logic & UML Models"],
        ["4.1", "Basic Modules", "7 Core Subsystems & Operational Responsibilities"],
        ["4.2", "Data Design & Schemas", "System Architecture & 8-Table Relational Data Dictionary"],
        ["4.3", "Procedural Design & Algorithms", "DFD Level 0/1, Structured Chart, 5 Core Algorithms"],
        ["4.4 to 4.6", "UI Design, Security Issues & Test Cases Design", "Glassmorphic Guidelines, RBAC & Test Categorization"],
        ["UML Models", "10 Comprehensive UML Diagrams", "Use Case, Class, Object, Sequence, State, Activity, Deployment"],
        ["CHAPTER 5", "IMPLEMENTATION AND TESTING", "Detailed Code Snippets & Formal Verification"],
        ["5.1", "Coding Details", "index.html, store.js, app.js, charts.js, server.js"],
        ["5.2", "Testing Approach & Test Report", "Unit, Integrated, Beta, Regression & 15-Row Formal Report"],
        ["CHAPTER 6", "RESULTS AND DISCUSSION", "Empirical Outcomes & 9-Screen UI Walkthrough"],
        ["6.1 to 6.9", "High-Resolution Screenshot Walkthroughs", "Landing, Modal, Admin, Teacher, Notify, Parent, Student, Analytics, Export"],
        ["Discussion", "Performance Benchmarking & Validation", "Latency Metrics, Usability Feedback & Outcomes"],
        ["CHAPTER 7", "CONCLUSION", "Final Evaluation, Significance, Limitations & Future Scope"],
        ["7.1 to 7.4", "System Significance, Limitations & Future Road-map", "Academic Impact, IoT/Biometric & Mobile Vision"],
        ["REFERENCES", "Online Resources & Documentation", "Standards, Framework Manuals & Tool References"]
    ]
    create_table(toc_headers, toc_data, [Inches(1.5), Inches(3.2), Inches(2.3)])

    doc.add_page_break()

    # =========================================================================
    # LIST OF FIGURES
    # =========================================================================
    p_lof_head = doc.add_paragraph()
    p_lof_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_head.paragraph_format.space_before = Pt(18)
    p_lof_head.paragraph_format.space_after = Pt(14)
    r_lof = p_lof_head.add_run("LIST OF FIGURES")
    r_lof.font.name = 'Times New Roman'
    r_lof.font.size = Pt(16)
    r_lof.font.bold = True
    r_lof.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    lof_headers = ["Figure No.", "Figure Title & Description", "System Artifact Category"]
    lof_data = [
        ["Figure 3.1", "Gantt Chart & Indicative Project Schedule (fig9_1_gantt_chart.png)", "Project Planning Model"],
        ["Figure 4.1", "AttendX Overall System Architecture & Data Flow (fig1_1_architecture.png)", "System Architecture"],
        ["Figure 4.2", "Context Diagram \u2013 Level 0 Data Flow Diagram (fig2_1_context_dfd.png)", "Structural Analysis"],
        ["Figure 4.3", "Level 1 Data Flow Diagram (fig2_2_level1_dfd.png)", "Process Flow Model"],
        ["Figure 4.4", "AttendX Modular Structured Chart (fig2_3_structured_chart.png)", "Procedural Hierarchy"],
        ["Figure 4.5", "AttendX Comprehensive Use Case Diagram (fig3_1_use_case.png)", "Behavioral Requirements"],
        ["Figure 4.6", "Detailed Domain Class Diagram (fig4_1_class_diagram.png)", "Object-Oriented Design"],
        ["Figure 4.7", "Runtime Object Diagram Instance (fig4_2_object_diagram.png)", "Structural State Model"],
        ["Figure 4.8", "Attendance Session State Chart Diagram (fig5_1_state_chart.png)", "State Machine Specification"],
        ["Figure 4.9", "Attendance Logging Activity Diagram (fig5_2_activity_attendance.png)", "Workflow Activity Model"],
        ["Figure 4.10", "Multi-Role Authentication Activity Diagram (fig5_3_activity_auth.png)", "Security Workflow Model"],
        ["Figure 4.11", "Parent Alert Fulfilment Activity Diagram (fig5_4_activity_parent.png)", "Notification Pipeline Model"],
        ["Figure 4.12", "Attendance Marking Sequence Diagram (fig6_1_sequence_attendance.png)", "Interaction Model"],
        ["Figure 4.13", "Roster Notification Collaboration Diagram (fig6_2_collaboration_diagram.png)", "Interaction Relationship Model"],
        ["Figure 4.14", "AttendX Subsystem Component Diagram (fig7_1_component_diagram.png)", "Implementation Architecture"],
        ["Figure 4.15", "Distributed Deployment Diagram (fig7_2_deployment_diagram.png)", "Hardware & Runtime Topology"],
        ["Figure 6.1", "Cybernetic Landing Page Showcase (ss_01_landing_hero.png)", "User Interface Screenshot"],
        ["Figure 6.2", "Multi-Role Authentication Modal (ss_02_auth_modal.png)", "User Interface Screenshot"],
        ["Figure 6.3", "Central Administrator & Academic Dean Dashboard (ss_03_admin_dashboard.png)", "User Interface Screenshot"],
        ["Figure 6.4", "Faculty Attendance Suite & Roster Workspace (ss_04_teacher_roster.png)", "User Interface Screenshot"],
        ["Figure 6.5", "Parental Notification Dispatch Engine (ss_05_teacher_notify.png)", "User Interface Screenshot"],
        ["Figure 6.6", "Parent Guardian Portal & Calendar Drilldown (ss_06_parent_dashboard.png)", "User Interface Screenshot"],
        ["Figure 6.7", "Student Portal & Recovery Advisor (ss_07_student_dashboard.png)", "User Interface Screenshot"],
        ["Figure 6.8", "Campus Visual Analytics Hub (ss_08_campus_analytics.png)", "User Interface Screenshot"],
        ["Figure 6.9", "Master Audit Log & Institutional CSV Export (ss_09_reports_export.png)", "User Interface Screenshot"]
    ]
    create_table(lof_headers, lof_data, [Inches(1.2), Inches(4.3), Inches(1.5)])

    doc.add_page_break()

    # =========================================================================
    # LIST OF TABLES
    # =========================================================================
    p_lot_head = doc.add_paragraph()
    p_lot_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_head.paragraph_format.space_before = Pt(18)
    p_lot_head.paragraph_format.space_after = Pt(14)
    r_lot = p_lot_head.add_run("LIST OF TABLES")
    r_lot.font.name = 'Times New Roman'
    r_lot.font.size = Pt(16)
    r_lot.font.bold = True
    r_lot.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    lot_headers = ["Table No.", "Table Title & Contents", "Document Chapter"]
    lot_data = [
        ["Table 1.1", "AttendX Academic Project Record & Metadata", "Title Page / Chapter 1"],
        ["Table 3.1", "AttendX Development Phases & Indicative Schedule", "Chapter 3: Requirements & Analysis"],
        ["Table 3.2", "PERT Task Dependencies and Duration Estimation", "Chapter 3: Requirements & Analysis"],
        ["Table 3.3", "Software and Hardware Operating Requirements", "Chapter 3: Requirements & Analysis"],
        ["Table 3.4", "Function Point Complexity Element Breakdown", "Chapter 3: Requirements & Analysis"],
        ["Table 4.1", "AttendX Core Basic Modules and Operational Responsibilities", "Chapter 4: System Design"],
        ["Table 4.2", "Relational Schema: Users Table Specification", "Chapter 4: System Design"],
        ["Table 4.3", "Relational Schema: Students Table Specification", "Chapter 4: System Design"],
        ["Table 4.4", "Relational Schema: Teachers Table Specification", "Chapter 4: System Design"],
        ["Table 4.5", "Relational Schema: AttendanceSessions Table Specification", "Chapter 4: System Design"],
        ["Table 4.6", "Relational Schema: AttendanceLogs Table Specification", "Chapter 4: System Design"],
        ["Table 4.7", "Relational Schema: Notifications / ParentAlerts Table Specification", "Chapter 4: System Design"],
        ["Table 4.8", "Actor-to-Use-Case Access Matrix", "Chapter 4: System Design"],
        ["Table 5.1", "Formal System Verification Test Report (15 Scenarios)", "Chapter 5: Implementation & Testing"],
        ["Table 6.1", "Performance Metrics & System Latency Benchmark", "Chapter 6: Results & Discussion"]
    ]
    create_table(lot_headers, lot_data, [Inches(1.2), Inches(4.3), Inches(1.5)])

    doc.add_page_break()
    print("Front matter generated successfully.")

