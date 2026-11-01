# AttendX — Smart Attendance Monitoring & Parent Notification System

> **Tagline:** *Attendance. Awareness. Action.*  
> **Aesthetic:** Futuristic Smart-Campus 3D Glassmorphism Control Deck  
> **Academic Capstone & Engineering Mini-Project**  
> **Author:** Vaishnavi Chavan (Dept. of Computer Science & Engineering)  
> **Project Guides:** Prof. Trupti Thakur & Dr. Vidya Mohod  

---

## 📌 Executive Summary

Traditional college attendance tracking is fragmented, paper-reliant, and suffers from delayed defaulter identification and zero real-time communication with parents.

**AttendX** is a next-generation smart campus web platform that combines rapid digital classroom roster marking with automated, real-time parent notifications. Engineered with a responsive dark-mode 3D glassmorphic aesthetic, AttendX unites Administrators, Teachers, Parents, and Students into a cohesive, transparent academic governance ecosystem.

---

## ✨ Key System Features

- ⚡ **Rapid Digital Roster Marking:** Teachers can complete classroom roll call with single-click toggles (`Present`, `Absent`, `Late`) or bulk "Mark All Present" in under 30 seconds.
- 🚨 **Automated 75% Defaulter Detection:** Continuously evaluates student cumulative attendance against statutory UGC/AICTE minimum mandates and immediately flags at-risk students.
- 📱 **Real-Time Multi-Channel Parental Notifications:** Instantly formats and dispatches alert payloads (SMS, WhatsApp, and webhook simulators) to guardians upon student absence or tardiness.
- 📅 **Interactive Parent Monthly Calendar Drilldown:** Color-coded daily attendance logs (Green = Present, Red = Absent, Amber = Late, Blue = College Event) with direct counselor inquiry messaging.
- 📈 **Student 75% Recovery Advisor:** A proactive mathematical recovery calculator predicting the exact number of consecutive upcoming lectures needed to regain examination eligibility.
- 🔥 **Google Firebase Cloud Firestore Integration:** Real-time multi-device cloud synchronization across classroom laptops and guardian smartphones, backed by seamless offline LocalStorage fallback.
- 📊 **Executive Campus Visual Analytics (Chart.js):** Hardware-accelerated canvas charts for departmental comparisons, defaulter ratios, and real-time institutional KPIs.
- 📑 **Master Audit Log & Institutional CSV Export:** Generates RFC-4180 compliant CSV audit spreadsheets with a single click.

---

## 🛠️ Technology Stack

| Layer | Technologies & Tools |
| :--- | :--- |
| **Frontend UI** | HTML5 Semantic Markup, CSS3 Custom Properties & 3D Glassmorphism, Lucide Icons, FontAwesome |
| **Logic & Reactivity** | JavaScript (ES6+), Web Audio API Synthesizer, Web Storage API (LocalStorage) |
| **Data Visualization** | Chart.js 4.x (Dynamic Bar, Line, Doughnut Charts with Neon Gradients) |
| **Cloud Database** | Google Firebase Cloud Platform & Cloud Firestore (Real-time `onSnapshot` streaming) |
| **Local Runtime** | Node.js HTTP Server (`server.js`) |
| **UML & Modeling** | 10 Comprehensive UML Diagrams (Use Case, Class, Object, State, Activity, Sequence, Component, Deployment) |
| **Documentation** | IEEE SRS compliant project documentation (`.docx`, `.md`) |

---

## 🚀 Quick Start Guide

### Option 1: Direct Browser Launch
Simply double-click or open [`index.html`](index.html) in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).

### Option 2: Run with Local Node.js Server
Ensure Node.js (v16+) is installed on your computer:
```bash
# Clone the repository
git clone https://github.com/chavanvaishnavi3308-byte/Attenadance-Monitoring-.git

# Navigate to project directory
cd Attenadance-Monitoring-

# Launch the lightweight Node HTTP server
node server.js
```
Now open your browser and navigate to:
```
http://localhost:8080
```

---

## 👥 Pre-Configured Demo Stakeholder Accounts

Click any 1-click demo profile in the **Authentication Modal** to test:

| Persona / Role | Name & Title | Credentials / ID | Primary Workspace |
| :--- | :--- | :--- | :--- |
| **Admin** | Dr. Vidya Mohod (Academic Dean) | `admin@attendx.edu` | Campus Analytics, Teacher & Class Directory, Audit Logs |
| **Teacher** | Prof. Swapnali Jadhav (CSE Faculty) | `swapnali@attendx.edu` | Subject Roster Workspace, Real-time Attendance Marking |
| **Teacher** | Prof. Trupti Thakur (CSE Faculty) | `trupti@attendx.edu` | Faculty Roster Workspace & Session Logs |
| **Parent** | Rajaram Chavan (Guardian) | `rajaram.chavan@mail.com` | Ward Attendance Calendar, Subject Breakdown, Counselor Chat |
| **Student** | Vaishnavi Chavan (Roll: CS-01) | `vaishnavi.cs@attendx.edu` | Self-Service Dashboard, 75% Recovery Advisor, Feedback |

---

## 📁 Repository Structure

```
├── assets/                    # Static branding, logo, and sample avatar images
├── css/
│   └── style.css              # Cybernetic 3D Glassmorphic design system & layout styles
├── js/
│   ├── firebase-config.js     # Firebase credentials & initialization config
│   ├── firebase-service.js    # Firestore async cloud sync & onSnapshot listeners
│   ├── data.js                # Seed datasets (departments, classes, students, teachers)
│   ├── store.js               # Reactive centralized state controller & LocalStorage bridge
│   ├── charts.js              # Chart.js holographic canvas visualizers
│   └── app.js                 # View router, UI event listeners & modal controllers
├── diagrams/                  # 16 High-resolution UML, DFD & Architecture diagrams
├── screenshots/               # 9 High-resolution full-screen UI interface showcases
├── scratch/                   # Automated diagnostic test scripts & doc builders
├── index.html                 # Main single-page application entry shell
├── server.js                  # Standalone native Node.js HTTP server
├── Architecture.md            # System architectural specification
├── prd.md                     # Product Requirements Document (PRD)
├── AttendX_Project_Documentation.docx # Comprehensive 50-page Academic Project Report
└── README.md                  # Project repository documentation
```

---

## 📜 Academic Project Information

- **Project Title:** AttendX – Smart Attendance Monitoring & Parent Notification System
- **Candidate Name:** Vaishnavi Chavan (Seat No: 2023-CS-001 / Roll No: CS-01)
- **Programme:** Bachelor of Technology (B.Tech) – Computer Science & Engineering
- **Department:** Department of Computer Science & Engineering
- **Project Guides:** Prof. Trupti Thakur (Assistant Professor) & Dr. Vidya Mohod (Dean & HOD)
- **Academic Year:** 2025 – 2026

---

## 📄 License
This project is developed for educational and academic capstone demonstration purposes.
