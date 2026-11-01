import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs('diagrams', exist_ok=True)

# Common styling palette matching reference docx
CLR_NAVY = '#1A365D'
CLR_BLUE = '#2B6CB0'
CLR_LIGHTBLUE = '#EBF8FF'
CLR_BORDER = '#2B6CB0'
CLR_TEXT = '#1A202C'
CLR_MUTED = '#4A5568'
CLR_GREEN = '#2F855A'
CLR_LIGHTGREEN = '#F0FFF4'
CLR_RED = '#C53030'
CLR_LIGHTRED = '#FFF5F5'
CLR_AMBER = '#DD6B20'
CLR_LIGHTAMBER = '#FFFAF0'
CLR_GRAY = '#718096'
CLR_LIGHTGRAY = '#EDF2F7'
CLR_PURPLE = '#6B46C1'
CLR_LIGHTPURPLE = '#FAF5FF'

def save_fig(fig, name):
    path = os.path.join('diagrams', name)
    plt.tight_layout()
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f'Generated: {path}')

# -------------------------------------------------------------
# Figure 1.1: Logical Architecture and Service Integrations
# -------------------------------------------------------------
def gen_fig1_1():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 7.2, "AttendX Logical Architecture & Service Integrations", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # Subgraph: Presentation UI Layer
    rect_ui = patches.FancyBboxPatch((0.4, 4.4), 10.2, 2.4, boxstyle="round,pad=0.1", 
                                     facecolor='#F7FAFC', edgecolor=CLR_BLUE, linewidth=1.5, linestyle='--')
    ax.add_patch(rect_ui)
    ax.text(0.7, 6.5, "Client Presentation Layer (SPA Browser Runtime)", fontsize=10, fontweight='bold', color=CLR_BLUE)

    ui_boxes = [
        ("Landing Showcase & 3D Hero\n(Cyber Canvas 60fps)", 0.6, 4.6, 2.3, 1.6),
        ("Role Auth & Switcher\n(Admin, Teacher, Parent, Student)", 3.1, 4.6, 2.4, 1.6),
        ("Role Command Dashboards\n(Admin, Teacher, Parent, Student)", 5.7, 4.6, 2.5, 1.6),
        ("Global Notification Drawer\n& Toast Alert System", 8.4, 4.6, 2.0, 1.6)
    ]
    for text, x, y, w, h in ui_boxes:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BORDER, linewidth=1.2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8.5, color=CLR_TEXT, multialignment='center')

    # Subgraph: Core Engine / Controller Layer
    rect_core = patches.FancyBboxPatch((0.4, 2.2), 10.2, 1.9, boxstyle="round,pad=0.1", 
                                       facecolor='#F7FAFC', edgecolor=CLR_PURPLE, linewidth=1.5, linestyle='--')
    ax.add_patch(rect_core)
    ax.text(0.7, 3.8, "Application State & Reactive Services (js/)", fontsize=10, fontweight='bold', color=CLR_PURPLE)

    core_boxes = [
        ("View Router &\nEvent Delegator (app.js)", 0.6, 2.4, 2.3, 1.2),
        ("AttendX Reactive Store\n(store.js State Engine)", 3.1, 2.4, 2.4, 1.2),
        ("Parent Alert Dispatcher &\nNotification Bus", 5.7, 2.4, 2.5, 1.2),
        ("Chart.js Holographic\nVisualizer (charts.js)", 8.4, 2.4, 2.0, 1.2)
    ]
    for text, x, y, w, h in core_boxes:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", facecolor=CLR_LIGHTPURPLE, edgecolor=CLR_PURPLE, linewidth=1.2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8.5, color=CLR_TEXT, multialignment='center')

    # Subgraph: Data & Runtime Layer
    rect_data = patches.FancyBboxPatch((0.4, 0.4), 10.2, 1.5, boxstyle="round,pad=0.1", 
                                       facecolor='#F7FAFC', edgecolor=CLR_GREEN, linewidth=1.5, linestyle='--')
    ax.add_patch(rect_data)
    ax.text(0.7, 1.65, "Storage, Audio & Host Environment", fontsize=10, fontweight='bold', color=CLR_GREEN)

    data_boxes = [
        ("HTML5 LocalStorage Engine\n(attendx_v2_* JSON cache)", 0.6, 0.6, 3.0, 0.9),
        ("Centralized Seed Factory\n(js/data.js CS & IT Datasets)", 3.8, 0.6, 3.2, 0.9),
        ("Web Audio API Synthesizer &\nNode.js HTTP Server (server.js)", 7.2, 0.6, 3.2, 0.9)
    ]
    for text, x, y, w, h in data_boxes:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", facecolor=CLR_LIGHTGREEN, edgecolor=CLR_GREEN, linewidth=1.2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8.5, color=CLR_TEXT, multialignment='center')

    # Connecting arrows
    for xc in [1.75, 4.3, 6.95, 9.4]:
        ax.annotate('', xy=(xc, 3.7), xytext=(xc, 4.5), arrowprops=dict(arrowstyle="<->", color=CLR_NAVY, lw=1.2))
    for xc in [2.1, 5.4, 8.8]:
        ax.annotate('', xy=(xc, 1.6), xytext=(xc, 2.3), arrowprops=dict(arrowstyle="<->", color=CLR_NAVY, lw=1.2))

    save_fig(fig, 'fig1_1_architecture.png')

# -------------------------------------------------------------
# Figure 2.1: Context Diagram (Level 0 DFD)
# -------------------------------------------------------------
def gen_fig2_1():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.0, 6.7, "AttendX Context Diagram (Level 0 DFD)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # Central System Process (Circle)
    circle = patches.Circle((5.0, 3.5), 1.4, facecolor=CLR_LIGHTBLUE, edgecolor=CLR_NAVY, linewidth=2.0)
    ax.add_patch(circle)
    ax.text(5.0, 3.8, "0.0\nAttendX Smart Attendance\n& Parent Notification\nSystem", 
            ha='center', va='center', fontsize=9.5, fontweight='bold', color=CLR_NAVY, multialignment='center')

    # Entities
    # Teacher (Top Left)
    p_t = patches.FancyBboxPatch((0.5, 4.6), 2.0, 1.1, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGRAY, edgecolor=CLR_TEXT, linewidth=1.5)
    ax.add_patch(p_t)
    ax.text(1.5, 5.15, "Teacher\n(Faculty Roster)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=CLR_TEXT)

    # Administrator (Bottom Left)
    p_a = patches.FancyBboxPatch((0.5, 1.3), 2.0, 1.1, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGRAY, edgecolor=CLR_TEXT, linewidth=1.5)
    ax.add_patch(p_a)
    ax.text(1.5, 1.85, "Administrator\n(Dean / HOD)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=CLR_TEXT)

    # Parent (Top Right)
    p_p = patches.FancyBboxPatch((7.5, 4.6), 2.0, 1.1, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGRAY, edgecolor=CLR_TEXT, linewidth=1.5)
    ax.add_patch(p_p)
    ax.text(8.5, 5.15, "Parent / Guardian\n(Rajaram Chavan)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=CLR_TEXT)

    # Student (Bottom Right)
    p_s = patches.FancyBboxPatch((7.5, 1.3), 2.0, 1.1, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGRAY, edgecolor=CLR_TEXT, linewidth=1.5)
    ax.add_patch(p_s)
    ax.text(8.5, 1.85, "Student\n(Vaishnavi Chavan)", ha='center', va='center', fontsize=9.5, fontweight='bold', color=CLR_TEXT)

    # Flows with Teacher
    ax.annotate('', xy=(3.8, 4.1), xytext=(2.5, 5.0), arrowprops=dict(arrowstyle="->", color=CLR_BLUE, lw=1.2))
    ax.text(2.6, 4.7, "Attendance Marks &\nSession Details", fontsize=7.5, color=CLR_BLUE, rotation=35)
    ax.annotate('', xy=(2.5, 4.7), xytext=(3.7, 3.8), arrowprops=dict(arrowstyle="->", color=CLR_GREEN, lw=1.2))
    ax.text(3.1, 4.1, "Roster & Confirmations", fontsize=7.5, color=CLR_GREEN, rotation=35)

    # Flows with Admin
    ax.annotate('', xy=(3.8, 2.9), xytext=(2.5, 2.0), arrowprops=dict(arrowstyle="->", color=CLR_BLUE, lw=1.2))
    ax.text(2.6, 2.5, "Student/Faculty CRUD\n& Settings", fontsize=7.5, color=CLR_BLUE, rotation=-35)
    ax.annotate('', xy=(2.5, 1.7), xytext=(3.7, 2.6), arrowprops=dict(arrowstyle="->", color=CLR_GREEN, lw=1.2))
    ax.text(3.1, 1.9, "Campus KPIs & Audit Logs", fontsize=7.5, color=CLR_GREEN, rotation=-35)

    # Flows with Parent
    ax.annotate('', xy=(7.5, 5.0), xytext=(6.2, 4.1), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2))
    ax.text(6.4, 4.7, "Real-time Absence &\nLate Notifications", fontsize=7.5, color=CLR_RED, rotation=-35)
    ax.annotate('', xy=(6.3, 3.8), xytext=(7.5, 4.7), arrowprops=dict(arrowstyle="->", color=CLR_PURPLE, lw=1.2))
    ax.text(6.9, 4.1, "Acknowledgement &\nInquiry Messages", fontsize=7.5, color=CLR_PURPLE, rotation=-35)

    # Flows with Student
    ax.annotate('', xy=(7.5, 1.7), xytext=(6.2, 2.6), arrowprops=dict(arrowstyle="->", color=CLR_GREEN, lw=1.2))
    ax.text(6.4, 2.2, "Subject % & Attendance\nStreak Metrics", fontsize=7.5, color=CLR_GREEN, rotation=35)
    ax.annotate('', xy=(6.3, 2.9), xytext=(7.5, 2.0), arrowprops=dict(arrowstyle="->", color=CLR_BLUE, lw=1.2))
    ax.text(7.0, 2.6, "View Timetable &\nCalendar Records", fontsize=7.5, color=CLR_BLUE, rotation=35)

    save_fig(fig, 'fig2_1_context_dfd.png')

# -------------------------------------------------------------
# Figure 2.2: Level 1 DFD
# -------------------------------------------------------------
def gen_fig2_2():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(5.5, 7.6, "AttendX Level 1 Data Flow Diagram (Process & Storage)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # 5 Processes
    procs = [
        ("1.0\nAuthentication &\nSession Controller", 1.5, 5.8),
        ("2.0\nAttendance Roster &\nSession Logging", 5.5, 5.8),
        ("3.0\nAlert Dispatcher &\nAudio Synth", 9.0, 5.8),
        ("4.0\nParent & Student\nInsight Services", 7.5, 2.2),
        ("5.0\nAdmin Analytics &\nDirectory Manager", 2.5, 2.2),
    ]
    for text, cx, cy in procs:
        c = patches.Circle((cx, cy), 0.95, facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE, linewidth=1.5)
        ax.add_patch(c)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_NAVY, multialignment='center')

    # 4 Data Stores (Open-ended rectangles)
    stores = [
        ("D1: attendx_v2_accounts", 1.0, 3.8, 2.5, 0.6),
        ("D2: attendx_v2_students/teachers", 4.2, 3.8, 3.0, 0.6),
        ("D3: attendx_v2_attendance", 5.5, 0.6, 2.6, 0.6),
        ("D4: attendx_v2_notifications", 8.2, 3.8, 2.6, 0.6),
    ]
    for text, x, y, w, h in stores:
        # Draw open rectangle (top, bottom, right lines)
        ax.plot([x, x+w, x+w, x], [y+h, y+h, y, y], color=CLR_GREEN, lw=1.5)
        ax.fill([x, x+w, x+w, x], [y, y, y+h, y+h], color=CLR_LIGHTGREEN, alpha=0.5)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_GREEN)

    # Arrows between processes and data stores
    # 1.0 <-> D1
    ax.annotate('', xy=(1.5, 4.4), xytext=(1.5, 4.8), arrowprops=dict(arrowstyle="<->", color=CLR_MUTED, lw=1.2))
    # 2.0 -> D3
    ax.annotate('', xy=(6.0, 1.2), xytext=(5.6, 4.8), arrowprops=dict(arrowstyle="->", color=CLR_BLUE, lw=1.2))
    ax.text(6.0, 3.0, "Save Session Records", fontsize=7.5, color=CLR_BLUE, rotation=-70)
    # 2.0 -> 3.0 (Absent / Late students trigger)
    ax.annotate('', xy=(8.0, 5.8), xytext=(6.5, 5.8), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.5))
    ax.text(7.25, 6.1, "Absentees Event", ha='center', fontsize=8, fontweight='bold', color=CLR_RED)
    # 3.0 -> D4
    ax.annotate('', xy=(9.2, 4.4), xytext=(9.2, 4.8), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2))
    ax.text(9.3, 4.6, "Store Alert", fontsize=7.5, color=CLR_RED)
    # 4.0 <-> D4
    ax.annotate('', xy=(8.8, 3.8), xytext=(8.0, 3.1), arrowprops=dict(arrowstyle="<->", color=CLR_PURPLE, lw=1.2))
    ax.text(8.5, 3.3, "Fetch/Ack", fontsize=7.5, color=CLR_PURPLE)
    # 4.0 <-> D3
    ax.annotate('', xy=(7.2, 1.2), xytext=(7.4, 1.4), arrowprops=dict(arrowstyle="<-", color=CLR_GREEN, lw=1.2))
    # 5.0 <-> D2
    ax.annotate('', xy=(3.8, 3.8), xytext=(3.0, 3.1), arrowprops=dict(arrowstyle="<->", color=CLR_MUTED, lw=1.2))
    # 5.0 <-> D3
    ax.annotate('', xy=(5.5, 0.9), xytext=(3.5, 2.2), arrowprops=dict(arrowstyle="<-", color=CLR_MUTED, lw=1.2))
    ax.text(4.2, 1.3, "Aggregate Stats", fontsize=7.5, color=CLR_MUTED)

    save_fig(fig, 'fig2_2_level1_dfd.png')

# -------------------------------------------------------------
# Figure 2.3: Structured Chart
# -------------------------------------------------------------
def gen_fig2_3():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5.5, 6.2, "AttendX Structured Chart (Functional Decomposition)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # Root Level
    p_root = patches.FancyBboxPatch((4.0, 4.9), 3.0, 0.9, boxstyle="round,pad=0.08", facecolor=CLR_NAVY, edgecolor=CLR_NAVY, linewidth=1.5)
    ax.add_patch(p_root)
    ax.text(5.5, 5.35, "0.0 AttendX System Controller\n(Master Orchestration Engine)", ha='center', va='center', fontsize=9, fontweight='bold', color='white')

    # Level 1 Modules
    l1_mods = [
        ("1.0 Auth & Session\nController", 0.6, 3.2, 1.7, 0.8),
        ("2.0 Attendance Roster\n& Marking Engine", 2.6, 3.2, 1.8, 0.8),
        ("3.0 Alert Dispatcher\n& Web Audio Engine", 4.7, 3.2, 1.8, 0.8),
        ("4.0 Analytics &\nChart.js Visualizer", 6.8, 3.2, 1.7, 0.8),
        ("5.0 Directory &\nReport Subsystem", 8.8, 3.2, 1.7, 0.8)
    ]
    for text, x, y, w, h in l1_mods:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE, linewidth=1.2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.8, fontweight='bold', color=CLR_NAVY, multialignment='center')
        # Line from root to module
        ax.plot([5.5, x + w/2], [4.9, 4.0], color=CLR_NAVY, lw=1.2)

    # Level 2 Sub-functions
    l2_subs = [
        ("• Login Validate\n• Demo Autofill\n• Role Guard", 0.6, 1.4, 1.7, 1.2),
        ("• Class/Subject Load\n• Mark All Present\n• Record Persist", 2.6, 1.4, 1.8, 1.2),
        ("• Scan Absentees\n• Emit Chime 880Hz\n• Badge Counter", 4.7, 1.4, 1.8, 1.2),
        ("• 7-Day Trend Chart\n• Status Doughnut\n• At-Risk <75% Scan", 6.8, 1.4, 1.7, 1.2),
        ("• Student CRUD\n• Monthly Calendar\n• CSV & Print Export", 8.8, 1.4, 1.7, 1.2)
    ]
    for text, x, y, w, h in l2_subs:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGRAY, edgecolor=CLR_GRAY, linewidth=1.0)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.2, color=CLR_TEXT, multialignment='left')
        ax.plot([x + w/2, x + w/2], [3.2, 2.6], color=CLR_GRAY, lw=1.0)

    save_fig(fig, 'fig2_3_structured_chart.png')

# -------------------------------------------------------------
# Figure 3.1: Use Case Diagram
# -------------------------------------------------------------
def gen_fig3_1():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(5.5, 8.1, "AttendX Use Case Diagram (Roles & System Boundaries)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # System boundary box
    rect_bound = patches.FancyBboxPatch((2.2, 0.4), 6.6, 7.3, boxstyle="round,pad=0.1", 
                                        facecolor='#FAFAFA', edgecolor=CLR_NAVY, linewidth=2.0)
    ax.add_patch(rect_bound)
    ax.text(2.5, 7.4, "AttendX Smart Campus System Boundary", fontsize=10, fontweight='bold', color=CLR_NAVY)

    # Helper for Stick Figure
    def draw_actor(x, y, label):
        # Head
        ax.add_patch(patches.Circle((x, y + 0.45), 0.18, facecolor='white', edgecolor=CLR_NAVY, lw=1.5))
        # Body
        ax.plot([x, x], [y + 0.27, y - 0.15], color=CLR_NAVY, lw=1.5)
        # Arms
        ax.plot([x - 0.25, x + 0.25], [y + 0.12, y + 0.12], color=CLR_NAVY, lw=1.5)
        # Legs
        ax.plot([x, x - 0.2], [y - 0.15, y - 0.45], color=CLR_NAVY, lw=1.5)
        ax.plot([x, x + 0.2], [y - 0.15, y - 0.45], color=CLR_NAVY, lw=1.5)
        ax.text(x, y - 0.7, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color=CLR_NAVY)

    # Actors
    draw_actor(1.0, 6.2, "Teacher\n(Swapnali Jadhav)")
    draw_actor(1.0, 2.2, "Admin\n(Dr. Vidya Mohod)")
    draw_actor(10.0, 6.2, "Parent\n(Rajaram Chavan)")
    draw_actor(10.0, 2.2, "Student\n(Vaishnavi Chavan)")

    # Use cases (Ellipses)
    ucs = [
        ("UC-01: Select Class & Subject", 3.7, 6.8),
        ("UC-02: Mark Attendance (Present/Absent/Late)", 4.0, 5.8),
        ("UC-03: Quick Mark All Present", 4.0, 4.8),
        ("UC-04: Dispatch Real-time Parent Alerts", 6.8, 6.0),
        ("UC-05: View Child Monthly Attendance Calendar", 6.8, 5.0),
        ("UC-06: Acknowledge Absence Notice & Inquire", 6.8, 4.0),
        ("UC-07: Track Personal % & Attendance Streak", 6.5, 2.6),
        ("UC-08: View Low-Attendance Warning (<75%)", 6.5, 1.4),
        ("UC-09: Monitor Campus KPIs & Trend Analytics", 3.8, 2.6),
        ("UC-10: Manage Student Directory (CRUD)", 3.8, 1.4),
        ("UC-11: Authenticate / Switch Role Session", 5.5, 7.2)
    ]
    for text, cx, cy in ucs:
        ell = patches.Ellipse((cx, cy), 2.2, 0.65, facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE, linewidth=1.2)
        ax.add_patch(ell)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=7.2, color=CLR_TEXT, multialignment='center')

    # Association lines
    # Teacher to UC-01, UC-02, UC-03, UC-04
    ax.plot([1.2, 2.6], [6.2, 6.8], color=CLR_BLUE, lw=1.0)
    ax.plot([1.2, 2.9], [6.2, 5.8], color=CLR_BLUE, lw=1.0)
    ax.plot([1.2, 2.9], [6.2, 4.8], color=CLR_BLUE, lw=1.0)
    ax.plot([1.2, 5.7], [6.2, 6.0], color=CLR_BLUE, lw=1.0)

    # Admin to UC-09, UC-10
    ax.plot([1.2, 2.7], [2.2, 2.6], color=CLR_BLUE, lw=1.0)
    ax.plot([1.2, 2.7], [2.2, 1.4], color=CLR_BLUE, lw=1.0)

    # Parent to UC-04, UC-05, UC-06
    ax.plot([9.8, 7.9], [6.2, 6.0], color=CLR_BLUE, lw=1.0)
    ax.plot([9.8, 7.9], [6.2, 5.0], color=CLR_BLUE, lw=1.0)
    ax.plot([9.8, 7.9], [6.2, 4.0], color=CLR_BLUE, lw=1.0)

    # Student to UC-07, UC-08
    ax.plot([9.8, 7.6], [2.2, 2.6], color=CLR_BLUE, lw=1.0)
    ax.plot([9.8, 7.6], [2.2, 1.4], color=CLR_BLUE, lw=1.0)

    # Includes / Extends
    ax.annotate('<<include>>', xy=(4.0, 5.5), xytext=(4.0, 5.1), 
                arrowprops=dict(arrowstyle="->", linestyle="--", color=CLR_PURPLE, lw=1.0),
                ha='center', fontsize=7, color=CLR_PURPLE)
    ax.annotate('<<extend>>', xy=(5.7, 6.0), xytext=(5.1, 5.8), 
                arrowprops=dict(arrowstyle="->", linestyle="--", color=CLR_RED, lw=1.0),
                ha='center', fontsize=7, color=CLR_RED)

    save_fig(fig, 'fig3_1_use_case.png')

# -------------------------------------------------------------
# Figure 4.1: Class Diagram
# -------------------------------------------------------------
def gen_fig4_1():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(5.5, 7.7, "AttendX Conceptual Class Diagram (Domain Model & Associations)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    def draw_class(name, attrs, methods, x, y, w=2.4, h=2.2):
        # Outer box
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", facecolor='#FFFFFF', edgecolor=CLR_NAVY, linewidth=1.5)
        ax.add_patch(p)
        # Header compartment
        h_h = 0.45
        p_head = patches.Rectangle((x, y + h - h_h), w, h_h, facecolor=CLR_NAVY)
        ax.add_patch(p_head)
        ax.text(x + w/2, y + h - h_h/2, name, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        # Attributes compartment
        a_h = (h - h_h) * 0.48
        ax.plot([x, x + w], [y + h - h_h - a_h, y + h - h_h - a_h], color=CLR_NAVY, lw=1.0)
        attr_text = "\n".join(attrs)
        ax.text(x + 0.1, y + h - h_h - 0.1, attr_text, ha='left', va='top', fontsize=6.8, color=CLR_TEXT)
        # Methods compartment
        meth_text = "\n".join(methods)
        ax.text(x + 0.1, y + h - h_h - a_h - 0.1, meth_text, ha='left', va='top', fontsize=6.8, color=CLR_TEXT)

    # Class UserAccount
    draw_class("UserAccount", 
               ["- id: String", "- email: String", "- role: RoleEnum", "- name: String"],
               ["+ authenticate(): Boolean", "+ getSessionToken(): String"],
               0.5, 4.8, 2.2, 1.8)

    # Class Student (inherits)
    draw_class("Student", 
               ["- rollNo: String", "- classId: String", "- parentId: String", "- attendanceRate: Float"],
               ["+ getStats(): Object", "+ checkStreak(): Int"],
               0.5, 1.8, 2.2, 2.2)

    # Class Teacher (inherits)
    draw_class("Teacher", 
               ["- department: String", "- assignedClass: String", "- specialty: String"],
               ["+ markRoster(): Session", "+ notifyParents(): Void"],
               3.2, 4.8, 2.3, 2.0)

    # Class AttendanceSession
    draw_class("AttendanceSession", 
               ["- id: String", "- classId: String", "- subjectId: String", "- date: Date", "- timestamp: Long"],
               ["+ addRecord(r): Void", "+ getSummary(): Counts"],
               6.0, 4.8, 2.4, 2.0)

    # Class AttendanceRecord
    draw_class("AttendanceRecord", 
               ["- studentId: String", "- status: Enum", "- verified: Boolean"],
               ["+ setStatus(status): Void"],
               8.8, 4.8, 1.8, 1.8)

    # Class NotificationItem
    draw_class("NotificationItem", 
               ["- id: String", "- type: NotifType", "- title: String", "- message: String", "- severity: Enum", "- read: Boolean"],
               ["+ markRead(): Void", "+ acknowledge(): Void"],
               6.0, 1.8, 2.4, 2.2)

    # Class AttendXStore
    draw_class("AttendXStore (Singleton)", 
               ["- STORAGE_KEYS: Map", "- listeners: Map"],
               ["+ saveAttendance(): Void", "+ notifyParentsForSession()", "+ getCampusStats(): Object"],
               3.2, 1.8, 2.4, 2.2)

    # Inheritance arrow UserAccount -> Student
    ax.annotate('', xy=(1.6, 4.8), xytext=(1.6, 4.0), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    # Association Teacher -> AttendanceSession (1 to *)
    ax.annotate('', xy=(6.0, 5.8), xytext=(5.5, 5.8), arrowprops=dict(arrowstyle="-", color=CLR_NAVY, lw=1.2))
    ax.text(5.6, 6.0, "1..* logs", fontsize=7, color=CLR_MUTED)
    # Composition AttendanceSession -> AttendanceRecord (1 to 1..*)
    ax.annotate('', xy=(8.8, 5.8), xytext=(8.4, 5.8), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.text(8.4, 6.0, "1..*", fontsize=7, color=CLR_MUTED)
    # Association AttendanceSession -> NotificationItem
    ax.annotate('', xy=(7.2, 4.0), xytext=(7.2, 4.8), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2))
    ax.text(7.3, 4.4, "triggers", fontsize=7, color=CLR_RED)
    # Store associations
    ax.annotate('', xy=(6.0, 2.9), xytext=(5.6, 2.9), arrowprops=dict(arrowstyle="<->", color=CLR_BLUE, lw=1.2))
    ax.annotate('', xy=(3.2, 2.9), xytext=(2.7, 2.9), arrowprops=dict(arrowstyle="<->", color=CLR_BLUE, lw=1.2))

    save_fig(fig, 'fig4_1_class_diagram.png')

# -------------------------------------------------------------
# Figure 4.2: Object Diagram (Illustrative Runtime Snapshot)
# -------------------------------------------------------------
def gen_fig4_2():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    ax.text(5.5, 6.2, "AttendX Object Diagram (Runtime Instance Snapshot: CS-3A Session)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    def draw_obj(name, fields, x, y, w=2.4, h=1.8):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03", facecolor='#F7FAFC', edgecolor=CLR_BLUE, linewidth=1.5)
        ax.add_patch(p)
        h_h = 0.4
        p_head = patches.Rectangle((x, y + h - h_h), w, h_h, facecolor=CLR_LIGHTBLUE)
        ax.add_patch(p_head)
        ax.text(x + w/2, y + h - h_h/2, name, ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_NAVY)
        field_text = "\n".join(fields)
        ax.text(x + 0.1, y + h - h_h - 0.1, field_text, ha='left', va='top', fontsize=7, color=CLR_TEXT)

    # Objects
    draw_obj("adminUser : Admin", 
             ["id = \"ADM-001\"", "name = \"Dr. Vidya Mohod\"", "role = \"admin\"", "dept = \"Central Admin\""],
             0.5, 4.0, 2.3, 1.8)

    draw_obj("teacherInst : Teacher", 
             ["id = \"TCH-001\"", "name = \"Swapnali Jadhav\"", "role = \"teacher\"", "assignedClass = \"CS\""],
             3.2, 4.0, 2.3, 1.8)

    draw_obj("sessionRecord : AttendanceSession", 
             ["id = \"SES-20261016-CS301\"", "classId = \"CS\"", "subjectId = \"CS-301\"", "date = \"2026-10-16\""],
             6.0, 4.0, 2.6, 1.8)

    draw_obj("studentInst : Student", 
             ["id = \"STD-CS01\"", "rollNo = \"CS-01\"", "name = \"Vaishnavi Chavan\"", "overallAttendance = 94.2%"],
             0.5, 1.2, 2.3, 2.0)

    draw_obj("parentInst : Parent", 
             ["id = \"PAR-001\"", "name = \"Rajaram Chavan\"", "childId = \"STD-CS01\"", "phone = \"+91 98201 44521\""],
             3.2, 1.2, 2.3, 2.0)

    draw_obj("alertInst : NotificationItem", 
             ["id = \"NOTIF-9821\"", "type = \"ABSENCE_ALERT\"", "severity = \"DANGER\"", "read = false"],
             6.0, 1.2, 2.6, 2.0)

    draw_obj("statusEntry : AttendanceRecord", 
             ["studentId = \"STD-CS01\"", "status = \"present\"", "timestamp = 1776314739"],
             9.0, 2.8, 1.8, 1.6)

    # Links
    ax.plot([2.8, 3.2], [4.9, 4.9], color=CLR_MUTED, lw=1.2)
    ax.plot([5.5, 6.0], [4.9, 4.9], color=CLR_MUTED, lw=1.2)
    ax.plot([1.6, 1.6], [4.0, 3.2], color=CLR_MUTED, lw=1.2)
    ax.plot([2.8, 3.2], [2.2, 2.2], color=CLR_MUTED, lw=1.2)
    ax.plot([7.3, 7.3], [4.0, 3.2], color=CLR_RED, lw=1.2)
    ax.plot([8.6, 9.0], [4.5, 3.6], color=CLR_MUTED, lw=1.2)

    save_fig(fig, 'fig4_2_object_diagram.png')

# -------------------------------------------------------------
# Figure 5.1: State Chart Diagram
# -------------------------------------------------------------
def gen_fig5_1():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.5)
    ax.axis('off')

    ax.text(5.5, 5.1, "AttendX Attendance Session & Notification Lifecycle State Chart", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    # Initial State
    ax.add_patch(patches.Circle((0.8, 3.0), 0.15, facecolor='black', edgecolor='black'))

    states = [
        ("Draft / Roster Loaded\n[Class & Subject Selected]", 1.6, 2.4, 2.1, 1.2),
        ("Session Marked\n[Toggles Updated / Counters Live]", 4.3, 2.4, 2.2, 1.2),
        ("Committed & Persisted\n[Saved to LocalStorage]", 7.1, 2.4, 2.2, 1.2),
        ("Alert Dispatched\n[Absentees Notified / Chime Played]", 7.1, 0.4, 2.2, 1.2),
        ("Parent Acknowledged\n[Notice Read & Verified]", 3.2, 0.4, 2.2, 1.2)
    ]
    for text, x, y, w, h in states:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_NAVY, linewidth=1.5)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.8, fontweight='bold', color=CLR_NAVY, multialignment='center')

    # Transitions
    ax.annotate('', xy=(1.6, 3.0), xytext=(0.95, 3.0), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.annotate('selectSession()', xy=(2.9, 3.0), xytext=(2.9, 3.7), ha='center', fontsize=7.5, color=CLR_BLUE)

    ax.annotate('', xy=(4.3, 3.0), xytext=(3.7, 3.0), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.text(4.0, 3.3, "toggleStatus()\n/ bulkPresent()", ha='center', fontsize=7, color=CLR_BLUE)

    ax.annotate('', xy=(7.1, 3.0), xytext=(6.5, 3.0), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.text(6.8, 3.3, "clickSave()\n[valid roster]", ha='center', fontsize=7, color=CLR_BLUE)

    ax.annotate('', xy=(8.2, 1.6), xytext=(8.2, 2.4), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.5))
    ax.text(8.3, 2.0, "clickNotify()\n[absentees > 0]", fontsize=7.5, fontweight='bold', color=CLR_RED)

    ax.annotate('', xy=(5.4, 1.0), xytext=(7.1, 1.0), arrowprops=dict(arrowstyle="->", color=CLR_PURPLE, lw=1.2))
    ax.text(6.25, 1.2, "parentLogin()\n& reviewInbox()", ha='center', fontsize=7, color=CLR_PURPLE)

    # Final state
    ax.add_patch(patches.Circle((1.5, 1.0), 0.18, facecolor='none', edgecolor='black', lw=1.5))
    ax.add_patch(patches.Circle((1.5, 1.0), 0.12, facecolor='black', edgecolor='black'))
    ax.annotate('', xy=(1.7, 1.0), xytext=(3.2, 1.0), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.text(2.4, 1.2, "clickAcknowledge()", ha='center', fontsize=7, color=CLR_NAVY)

    save_fig(fig, 'fig5_1_state_chart.png')

# -------------------------------------------------------------
# Figure 5.2: Activity Diagram - Attendance Logging
# -------------------------------------------------------------
def gen_fig5_2():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(5.5, 7.7, "Activity Diagram: Attendance Logging & Automated Parent Notification Flow", 
            ha='center', va='center', fontsize=13, fontweight='bold', color=CLR_NAVY)

    # Swimlanes
    lanes = ["Teacher (Faculty)", "AttendX UI View", "AttendXStore & LocalStorage", "Notification Engine", "Parent Portal"]
    for i, lane in enumerate(lanes):
        x = 0.4 + i * 2.1
        ax.plot([x, x], [0.5, 7.2], color=CLR_GRAY, lw=1.0, linestyle=':')
        p_head = patches.Rectangle((x, 6.8), 2.0, 0.4, facecolor=CLR_NAVY)
        ax.add_patch(p_head)
        ax.text(x + 1.0, 7.0, lane, ha='center', va='center', fontsize=7.5, fontweight='bold', color='white')

    # Start
    ax.add_patch(patches.Circle((1.4, 6.4), 0.12, facecolor='black'))

    # Action 1: Select Class & Subject (Teacher)
    p1 = patches.FancyBboxPatch((0.6, 5.5), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
    ax.add_patch(p1)
    ax.text(1.4, 5.8, "Select Class &\nSubject (e.g. CS-301)", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 2: Render Roster (UI)
    p2 = patches.FancyBboxPatch((2.7, 5.5), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
    ax.add_patch(p2)
    ax.text(3.5, 5.8, "Render 10 CS Students\nwith Status Toggles", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 3: Mark Status (Teacher)
    p3 = patches.FancyBboxPatch((0.6, 4.4), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
    ax.add_patch(p3)
    ax.text(1.4, 4.7, "Toggle Status or\n'Mark All Present'", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 4: Click Save (Teacher)
    p4 = patches.FancyBboxPatch((0.6, 3.3), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
    ax.add_patch(p4)
    ax.text(1.4, 3.6, "Click \"Save Attendance\"", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 5: Commit to LocalStorage (Store)
    p5 = patches.FancyBboxPatch((4.8, 3.3), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGREEN, edgecolor=CLR_GREEN)
    ax.add_patch(p5)
    ax.text(5.6, 3.6, "Write to LocalStorage\n& Recalculate %", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 6: Click Notify Parents (Teacher)
    p6 = patches.FancyBboxPatch((0.6, 2.2), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTRED, edgecolor=CLR_RED)
    ax.add_patch(p6)
    ax.text(1.4, 2.5, "Click \"Notify Parents\"", ha='center', va='center', fontsize=7, fontweight='bold', color=CLR_RED)

    # Action 7: Scan & Emit Chime (Engine)
    p7 = patches.FancyBboxPatch((6.9, 2.2), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTPURPLE, edgecolor=CLR_PURPLE)
    ax.add_patch(p7)
    ax.text(7.7, 2.5, "Filter Absentees &\nPlay Audio Chime", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # Action 8: Receive Alert & Review (Parent)
    p8 = patches.FancyBboxPatch((9.0, 1.1), 1.6, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTRED, edgecolor=CLR_RED)
    ax.add_patch(p8)
    ax.text(9.8, 1.4, "Receive Alert Card &\nAcknowledge Notice", ha='center', va='center', fontsize=7, color=CLR_TEXT)

    # End
    ax.add_patch(patches.Circle((9.8, 0.6), 0.15, facecolor='none', edgecolor='black', lw=1.5))
    ax.add_patch(patches.Circle((9.8, 0.6), 0.1, facecolor='black'))

    # Connecting arrows
    ax.annotate('', xy=(1.4, 6.1), xytext=(1.4, 6.28), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(2.7, 5.8), xytext=(2.2, 5.8), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(1.4, 5.0), xytext=(2.7, 5.5), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(1.4, 3.9), xytext=(1.4, 4.4), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(4.8, 3.6), xytext=(2.2, 3.6), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(1.4, 2.8), xytext=(1.4, 3.3), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(6.9, 2.5), xytext=(2.2, 2.5), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2))
    ax.annotate('', xy=(9.0, 1.4), xytext=(8.5, 2.2), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2))
    ax.annotate('', xy=(9.8, 0.75), xytext=(9.8, 1.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))

    save_fig(fig, 'fig5_2_activity_attendance.png')

# -------------------------------------------------------------
# Figure 5.3: Activity Diagram - Authentication & Access
# -------------------------------------------------------------
def gen_fig5_3():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.0, 6.7, "Activity Diagram: Authentication & Role-Based Access Routing", 
            ha='center', va='center', fontsize=13, fontweight='bold', color=CLR_NAVY)

    # Start
    ax.add_patch(patches.Circle((5.0, 6.2), 0.12, facecolor='black'))

    # Step 1: Open Login Modal & Select Role
    p1 = patches.FancyBboxPatch((3.5, 5.2), 3.0, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
    ax.add_patch(p1)
    ax.text(5.0, 5.5, "Select Role & Enter Credentials\n(or 1-Click Demo Fill)", ha='center', va='center', fontsize=8, color=CLR_TEXT)

    # Step 2: Validate Account Decision
    # Diamond
    ax.plot([5.0, 6.0, 5.0, 4.0, 5.0], [4.6, 4.0, 3.4, 4.0, 4.6], color=CLR_NAVY, lw=1.5)
    ax.text(5.0, 4.0, "Credentials\nValid?", ha='center', va='center', fontsize=7.5, fontweight='bold', color=CLR_NAVY)

    # Invalid -> Toast error
    p_err = patches.FancyBboxPatch((7.2, 3.7), 2.2, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTRED, edgecolor=CLR_RED)
    ax.add_patch(p_err)
    ax.text(8.3, 4.0, "Show Error Toast\n& Shake Modal", ha='center', va='center', fontsize=7.5, color=CLR_RED)
    ax.annotate('No', xy=(7.2, 4.0), xytext=(6.0, 4.0), arrowprops=dict(arrowstyle="->", color=CLR_RED, lw=1.2), fontsize=8, color=CLR_RED)

    # Valid -> Set Session & Role Switch
    ax.annotate('Yes', xy=(5.0, 2.7), xytext=(5.0, 3.4), arrowprops=dict(arrowstyle="->", color=CLR_GREEN, lw=1.2), fontsize=8, color=CLR_GREEN)

    p_sess = patches.FancyBboxPatch((3.5, 2.1), 3.0, 0.6, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTGREEN, edgecolor=CLR_GREEN)
    ax.add_patch(p_sess)
    ax.text(5.0, 2.4, "Set Session in LocalStorage\n& Route to Target Portal", ha='center', va='center', fontsize=8, color=CLR_TEXT)

    # Fork to 4 portals
    portals = [
        ("Admin Portal\n(Dean KPIs)", 0.6, 0.8, 1.8, 0.6),
        ("Teacher Portal\n(CS/IT Roster)", 2.8, 0.8, 1.8, 0.6),
        ("Parent Portal\n(Child Calendar)", 5.0, 0.8, 1.8, 0.6),
        ("Student Portal\n(Timetable & Streak)", 7.2, 0.8, 2.2, 0.6)
    ]
    for text, x, y, w, h in portals:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTPURPLE, edgecolor=CLR_PURPLE)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.2, color=CLR_TEXT, multialignment='center')
        ax.annotate('', xy=(x + w/2, 1.4), xytext=(5.0, 2.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.0))

    # Connect p1 to diamond
    ax.annotate('', xy=(5.0, 4.6), xytext=(5.0, 5.2), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(5.0, 5.2), xytext=(5.0, 6.08), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))

    save_fig(fig, 'fig5_3_activity_auth.png')

# -------------------------------------------------------------
# Figure 5.4: Activity Diagram - Parent Fulfilment & Inquiry
# -------------------------------------------------------------
def gen_fig5_4():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.0, 6.7, "Activity Diagram: Parent Alert Review, Acknowledgement & Teacher Inquiry", 
            ha='center', va='center', fontsize=13, fontweight='bold', color=CLR_NAVY)

    # Start
    ax.add_patch(patches.Circle((5.0, 6.1), 0.12, facecolor='black'))

    steps = [
        ("Parent Logs In & Opens Child Dashboard\n(Linked to Vaishnavi Chavan, Roll CS-01)", 2.5, 5.1, 5.0, 0.6),
        ("System Queries Unread Notifications\nFilter: targetId = \"STD-CS01\" or classId = \"CS\"", 2.5, 4.1, 5.0, 0.6),
        ("Display Red Absence Warning Card\nLecture: CS-301 DSA | Status: ABSENT", 2.5, 3.1, 5.0, 0.6),
        ("Parent Clicks \"Acknowledge Notice\"\nUpdates read = true in LocalStorage", 1.0, 1.8, 3.6, 0.7),
        ("Parent Clicks \"Message Teacher\"\nSends direct message to Prof. Swapnali", 5.4, 1.8, 3.8, 0.7)
    ]
    for text, x, y, w, h in steps:
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_BLUE)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.8, color=CLR_TEXT, multialignment='center')

    # End
    ax.add_patch(patches.Circle((5.0, 0.6), 0.15, facecolor='none', edgecolor='black', lw=1.5))
    ax.add_patch(patches.Circle((5.0, 0.6), 0.1, facecolor='black'))

    # Connectors
    ax.annotate('', xy=(5.0, 5.7), xytext=(5.0, 5.98), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(5.0, 4.7), xytext=(5.0, 5.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(5.0, 3.7), xytext=(5.0, 4.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(2.8, 2.5), xytext=(4.5, 3.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(7.2, 2.5), xytext=(5.5, 3.1), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(4.8, 0.75), xytext=(2.8, 1.8), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))
    ax.annotate('', xy=(5.2, 0.75), xytext=(7.2, 1.8), arrowprops=dict(arrowstyle="->", color=CLR_NAVY))

    save_fig(fig, 'fig5_4_activity_parent.png')

# -------------------------------------------------------------
# Figure 6.1: Sequence Diagram
# -------------------------------------------------------------
def gen_fig6_1():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(5.5, 7.7, "AttendX Sequence Diagram: Attendance Marking, Storage & Alert Dispatch", 
            ha='center', va='center', fontsize=13, fontweight='bold', color=CLR_NAVY)

    lifelines = [
        ("TeacherUI", 1.0),
        ("AppRouter", 2.8),
        ("AttendXStore", 4.8),
        ("LocalStorage", 6.8),
        ("AudioSynth", 8.6),
        ("ParentUI", 10.2)
    ]
    for name, x in lifelines:
        p = patches.Rectangle((x - 0.7, 7.0), 1.4, 0.45, facecolor=CLR_NAVY)
        ax.add_patch(p)
        ax.text(x, 7.22, name, ha='center', va='center', fontsize=8, fontweight='bold', color='white')
        ax.plot([x, x], [0.6, 7.0], color=CLR_GRAY, lw=1.0, linestyle='--')

    # Messages
    msgs = [
        ("1: selectClass(CS, CS-301)", 1.0, 2.8, 6.5, False),
        ("2: getStudents(\"CS\")", 2.8, 4.8, 6.0, False),
        ("3: return [10 Students]", 4.8, 2.8, 5.6, True),
        ("4: renderRoster()", 2.8, 1.0, 5.2, True),
        ("5: saveAttendance(classId, records)", 1.0, 4.8, 4.6, False),
        ("6: setItem(attendx_v2_attendance)", 4.8, 6.8, 4.2, False),
        ("7: notifyParentsForSession()", 1.0, 4.8, 3.6, False),
        ("8: emitChime(880Hz, alert)", 4.8, 8.6, 3.0, False),
        ("9: appendNotification(absentees)", 4.8, 6.8, 2.4, False),
        ("10: renderToastAlert()", 4.8, 1.0, 1.8, True),
        ("11: onAlertReceived()", 6.8, 10.2, 1.2, False)
    ]
    for label, x1, x2, y, is_ret in msgs:
        style = "<-" if is_ret else "->"
        ls = "--" if is_ret else "-"
        color = CLR_GREEN if is_ret else (CLR_RED if "notify" in label.lower() or "alert" in label.lower() else CLR_BLUE)
        ax.annotate('', xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle=style, linestyle=ls, color=color, lw=1.2))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 0.12, label, ha='center', va='bottom', fontsize=7, color=color, fontweight='bold' if "notify" in label else 'normal')

    save_fig(fig, 'fig6_1_sequence_attendance.png')

# -------------------------------------------------------------
# Figure 6.2: Collaboration Diagram
# -------------------------------------------------------------
def gen_fig6_2():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.0, 6.7, "AttendX Collaboration (Communication) Diagram", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    def draw_cbox(name, x, y, w=2.0, h=1.0):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=CLR_LIGHTBLUE, edgecolor=CLR_NAVY, linewidth=1.5)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, name, ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_NAVY, multialignment='center')

    draw_cbox("1 : TeacherPortal\n(:UI View)", 0.6, 4.6)
    draw_cbox("2 : StoreController\n(:AttendXStore)", 4.0, 4.6)
    draw_cbox("3 : AudioEngine\n(:WebAudioSynth)", 7.4, 4.6)
    draw_cbox("4 : LocalStorage\n(:BrowserEngine)", 4.0, 1.4)
    draw_cbox("5 : ParentPortal\n(:UI View)", 7.4, 1.4)

    # Links with numbered messages
    # 1 <-> 2
    ax.plot([2.6, 4.0], [5.1, 5.1], color=CLR_NAVY, lw=1.5)
    ax.text(3.3, 5.5, "1: markRoster()\n3: saveSession()", ha='center', fontsize=7, color=CLR_BLUE)
    ax.text(3.3, 4.7, "2: rosterData", ha='center', fontsize=7, color=CLR_GREEN)

    # 2 <-> 3
    ax.plot([6.0, 7.4], [5.1, 5.1], color=CLR_NAVY, lw=1.5)
    ax.text(6.7, 5.4, "5: playAlertChime()", ha='center', fontsize=7, color=CLR_PURPLE)

    # 2 <-> 4
    ax.plot([5.0, 5.0], [4.6, 2.4], color=CLR_NAVY, lw=1.5)
    ax.text(5.1, 3.5, "4: setItem(attendance)\n6: setItem(notifs)", ha='left', fontsize=7, color=CLR_BLUE)

    # 4 <-> 5
    ax.plot([6.0, 7.4], [1.9, 1.9], color=CLR_NAVY, lw=1.5)
    ax.text(6.7, 2.2, "7: queryNotifs()\n8: ackNotice()", ha='center', fontsize=7, color=CLR_RED)

    save_fig(fig, 'fig6_2_collaboration_diagram.png')

# -------------------------------------------------------------
# Figure 7.1: Component Diagram
# -------------------------------------------------------------
def gen_fig7_1():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.5, 6.7, "AttendX System Component Diagram & Internal Dependencies", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    def draw_comp(name, desc, x, y, w=2.6, h=1.4, color=CLR_LIGHTBLUE, border=CLR_BLUE):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0.0", facecolor=color, edgecolor=border, linewidth=1.5)
        ax.add_patch(p)
        # Component icon tabs on left
        t1 = patches.Rectangle((x - 0.2, y + h - 0.4), 0.4, 0.2, facecolor=color, edgecolor=border, lw=1.0)
        t2 = patches.Rectangle((x - 0.2, y + 0.2), 0.4, 0.2, facecolor=color, edgecolor=border, lw=1.0)
        ax.add_patch(t1)
        ax.add_patch(t2)
        ax.text(x + w/2, y + h - 0.35, f"<<component>>\n{name}", ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_NAVY)
        ax.text(x + w/2, y + 0.4, desc, ha='center', va='center', fontsize=7, color=CLR_MUTED, multialignment='center')

    # Components
    draw_comp("Presentation View", "index.html & css/style.css\nCyber Canvas & Glass UI", 0.6, 4.6)
    draw_comp("Application Controller", "js/app.js\nRouting & Modal Engine", 4.2, 4.6)
    draw_comp("Charts Visualizer", "js/charts.js\nChart.js Neon Engine", 7.8, 4.6)

    draw_comp("Reactive State Store", "js/store.js\nAttendXStore Singleton", 4.2, 2.2, color=CLR_LIGHTGREEN, border=CLR_GREEN)
    draw_comp("Web Audio Synthesizer", "HTML5 AudioContext\nSynthetic Frequency Chimes", 7.8, 2.2, color=CLR_LIGHTPURPLE, border=CLR_PURPLE)

    draw_comp("Persistence Layer", "HTML5 LocalStorage Engine\nNamespace: attendx_v2_*", 4.2, 0.4, color=CLR_LIGHTGRAY, border=CLR_GRAY)
    draw_comp("Static HTTP Server", "server.js (Node.js Port 8080)\nZero-Config Asset Host", 0.6, 0.4, color=CLR_LIGHTAMBER, border=CLR_AMBER)

    # Connections
    ax.annotate('', xy=(4.2, 5.3), xytext=(3.2, 5.3), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.annotate('', xy=(7.8, 5.3), xytext=(6.8, 5.3), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.annotate('', xy=(5.5, 3.6), xytext=(5.5, 4.6), arrowprops=dict(arrowstyle="->", color=CLR_NAVY, lw=1.2))
    ax.annotate('', xy=(7.8, 2.9), xytext=(6.8, 2.9), arrowprops=dict(arrowstyle="->", color=CLR_PURPLE, lw=1.2))
    ax.annotate('', xy=(5.5, 1.8), xytext=(5.5, 2.2), arrowprops=dict(arrowstyle="->", color=CLR_GREEN, lw=1.2))

    save_fig(fig, 'fig7_1_component_diagram.png')

# -------------------------------------------------------------
# Figure 7.2: Deployment Diagram
# -------------------------------------------------------------
def gen_fig7_2():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.5, 6.7, "AttendX System Deployment Topology (Browser Client & Static Host)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color=CLR_NAVY)

    def draw_node(name, artifacts, x, y, w=3.4, h=2.5, color='#F7FAFC'):
        # 3D box effect
        depth = 0.25
        # Front
        p_front = patches.Rectangle((x, y), w, h, facecolor=color, edgecolor=CLR_NAVY, lw=1.5)
        ax.add_patch(p_front)
        # Top
        ax.fill([x, x + depth, x + w + depth, x + w], [y + h, y + h + depth, y + h + depth, y + h], color='#E2E8F0', edgecolor=CLR_NAVY, lw=1.2)
        # Right
        ax.fill([x + w, x + w + depth, x + w + depth, x + w], [y, y + depth, y + h + depth, y + h], color='#CBD5E0', edgecolor=CLR_NAVY, lw=1.2)

        ax.text(x + w/2, y + h - 0.35, f"<<device / execution environment>>\n{name}", ha='center', va='center', fontsize=8, fontweight='bold', color=CLR_NAVY)
        art_y = y + h - 0.8
        for art in artifacts:
            p_art = patches.Rectangle((x + 0.2, art_y - 0.25), w - 0.4, 0.35, facecolor='white', edgecolor=CLR_BLUE, lw=1.0)
            ax.add_patch(p_art)
            ax.text(x + w/2, art_y - 0.08, art, ha='center', va='center', fontsize=6.8, color=CLR_TEXT)
            art_y -= 0.45

    draw_node("Client Workstation / Mobile Browser\n(Google Chrome / Safari / Edge)", 
              ["<<artifact>> index.html & style.css", "<<artifact>> js/{app,store,data,charts}.js", "<<artifact>> LocalStorage Key-Value DB", "<<subsystem>> Web Audio API Synth"],
              0.6, 2.0, 3.8, 3.8)

    draw_node("Application Web Host\n(Node.js Server / Vercel Edge)", 
              ["<<artifact>> server.js (Node HTTP Server)", "<<environment>> Port 8080 Listener", "<<service>> MIME Streamer & Fallbacks"],
              6.5, 2.8, 3.8, 3.0)

    # Communication protocol line
    ax.annotate('', xy=(6.5, 4.3), xytext=(4.4, 4.3), arrowprops=dict(arrowstyle="<->", color=CLR_NAVY, lw=1.5))
    ax.text(5.45, 4.6, "HTTP / HTTPS (GET/Static)\n(Zero external cloud DB dependencies)", ha='center', fontsize=7.5, color=CLR_NAVY, fontweight='bold')

    save_fig(fig, 'fig7_2_deployment_diagram.png')

# -------------------------------------------------------------
# Figure 9.1: Indicative Gantt Chart
# -------------------------------------------------------------
def gen_fig9_1():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_xlim(0, 17)
    ax.set_ylim(-0.5, 8.5)

    ax.set_title("AttendX 16-Week Academic Project Scheduling (Gantt Chart)", fontsize=13, fontweight='bold', color=CLR_NAVY, pad=15)
    ax.set_xlabel("Academic Project Timeline (Weeks 1 to 16)", fontsize=10, fontweight='bold', color=CLR_NAVY)
    ax.set_xticks(range(1, 17))
    ax.set_xticklabels([f"W{i}" for i in range(1, 17)])
    ax.grid(axis='x', linestyle='--', alpha=0.6)

    phases = [
        ("Phase 1: Problem Statement & SRS Formulation", 1, 3, CLR_BLUE),
        ("Phase 2: Architectural Design & System Modeling", 3, 5, CLR_BLUE),
        ("Phase 3: UI/UX Cyber-Glass Design System", 5, 8, CLR_PURPLE),
        ("Phase 4: Role-Based Auth & Session Engine", 7, 10, CLR_PURPLE),
        ("Phase 5: Attendance Marking & Parent Alert Dispatch", 9, 12, CLR_RED),
        ("Phase 6: Visual Analytics & Chart.js Integration", 11, 14, CLR_GREEN),
        ("Phase 7: Verification, Test Execution & Defect Fixing", 13, 15, CLR_AMBER),
        ("Phase 8: Project Documentation & Final Defense Review", 15, 16.8, CLR_NAVY)
    ]

    y_pos = list(reversed(range(len(phases))))
    phase_names = [p[0] for p in phases]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(phase_names, fontsize=8.5, fontweight='bold', color=CLR_TEXT)

    for i, (_, start, end, color) in enumerate(phases):
        w = end - start
        y = y_pos[i]
        rect = patches.FancyBboxPatch((start, y - 0.28), w, 0.56, boxstyle="round,pad=0.04", facecolor=color, edgecolor=color, alpha=0.85)
        ax.add_patch(rect)
        # Milestone diamond at end
        ax.plot(end, y, marker='D', color=CLR_NAVY, markersize=7)
        ax.text(start + w/2, y, f"{w:.1f} wks", ha='center', va='center', fontsize=7.5, fontweight='bold', color='white')

    ax.invert_yaxis()
    save_fig(fig, 'fig9_1_gantt_chart.png')

if __name__ == '__main__':
    print("Generating all 16 AttendX diagrams...")
    gen_fig1_1()
    gen_fig2_1()
    gen_fig2_2()
    gen_fig2_3()
    gen_fig3_1()
    gen_fig4_1()
    gen_fig4_2()
    gen_fig5_1()
    gen_fig5_2()
    gen_fig5_3()
    gen_fig5_4()
    gen_fig6_1()
    gen_fig6_2()
    gen_fig7_1()
    gen_fig7_2()
    gen_fig9_1()
    print("All 16 diagrams generated successfully!")
