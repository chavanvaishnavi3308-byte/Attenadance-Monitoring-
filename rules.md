# AttendX Engineering & Design Rules
## Coding Standards, UI Principles, and Architectural Guidelines

**Version:** 1.0.0  
**Scope:** AttendX Smart Campus Web Application  

---

### 1. Coding Rules
1. **Zero External CSS Framework Bloat:** Do not inject Twitter Bootstrap, Tailwind CDN, or Materialize. All aesthetics must be built with clean, modular Vanilla CSS using CSS Custom Properties (CSS variables).
2. **Modular JavaScript Separation:**
   - `data.js`: Holds raw static seed definitions only.
   - `store.js`: Manages state, mutations, LocalStorage synchronization, and getter queries.
   - `charts.js`: Encapsulates Chart.js configuration, themes, and lifecycle.
   - `app.js`: Coordinates DOM rendering, event delegation, audio synthesis, and view transitions.
3. **Immutability in State Operations:** When updating students, attendance, or notifications in `store.js`, avoid direct array mutations; always produce new array references before committing to LocalStorage.
4. **Resilient LocalStorage Fallbacks:** Always wrap `JSON.parse` and `localStorage.setItem` in `try...catch` blocks to gracefully handle potential quota exceeded errors or corrupted storage strings.
5. **No Inline Event Handlers:** Prefer `addEventListener` over inline `onclick=""` in JavaScript templates to maintain a clean Content Security Policy (CSP).

---

### 2. UI & Design Rules
1. **Futuristic Glassmorphic Theme:**
   - Deep cyber background: `#060919` to `#0B112C`.
   - Card surfaces: Translucent dark navy with `backdrop-filter: blur(16px)` and subtle glowing cyan/purple borders (`border: 1px solid rgba(0, 240, 255, 0.15)`).
   - Accents: Neon Cyan (`#00F0FF`), Electric Blue (`#3B82F6`), Neon Violet (`#8B5CF6`).
2. **Status Color Matrix:**
   - 🟢 **Present:** Neon Emerald (`#10B981`, `rgba(16, 185, 129, 0.2)` glow).
   - 🔴 **Absent:** Cyber Coral (`#EF4444`, `rgba(239, 68, 68, 0.25)` glow).
   - 🟡 **Late:** Solar Amber (`#F59E0B`, `rgba(245, 158, 11, 0.2)` glow).
   - 🔵 **Info / Report:** Electric Cyan (`#06B6D4`, `rgba(6, 182, 212, 0.2)` glow).
   - ⚠️ **Critical Low Warning (<75%):** Pulsing Amber/Red neon badge.
3. **Typography Hierarchy:**
   - Primary Headings & KPI Counters: `Outfit`, `Plus Jakarta Sans`, or `Inter` with font weights 600, 700, 800.
   - Body & Micro-copy: `Plus Jakarta Sans` or `Inter`, font weight 400-500, letter-spacing +0.01em.
   - Code & Roll Numbers: `JetBrains Mono` or system monospace for alignment.
4. **Depth and 3D Micro-interactions:**
   - Cards must elevate on hover with `transform: translateY(-4px) scale(1.01)` and an increased box-shadow glow.
   - Interactive buttons must feature smooth active states with `transform: scale(0.97)`.

---

### 3. Naming Conventions
- **HTML IDs:** Lowercase hyphenated descriptive names (`id="view-admin-dashboard"`, `id="btn-mark-all-present"`, `id="global-search-input"`).
- **CSS Classes:** BEM-influenced utility classes (`.glass-card`, `.stat-card__metric`, `.btn-cyber-primary`, `.badge--present`).
- **JavaScript Variables & Functions:** camelCase for variables and functions (`saveAttendanceRecord()`, `currentActiveRole`), PascalCase for Store classes (`AttendXStore`), UPPER_SNAKE_CASE for constants (`STORAGE_KEYS`).

---

### 4. Component Rules
1. **Self-Contained Views:** Every primary view (`#view-landing`, `#view-admin-dashboard`, `#view-teacher-dashboard`, `#view-parent-dashboard`, `#view-student-dashboard`, `#view-students`, `#view-notifications`, `#view-reports`, `#view-analytics`) lives inside a structured container. Switching views toggles `.active-view` with a CSS fade-in slide keyframe.
2. **Reusable Modal Architecture:** A universal modal wrapper (`#attendxModal`) manages dynamic headers, bodies, and footers, with escape key dismissal and backdrop click handling.
3. **Toast Notifications:** Toasts must automatically self-dismiss after 4 seconds and allow manual dismissal with an exit slide animation.

---

### 5. Accessibility (a11y) Rules
1. **Semantic Hierarchy:** Use proper `<h1>`, `<h2>`, `<header>`, `<nav>`, `<aside>`, `<main>`, and `<section>` tags.
2. **Aria Labels & Roles:** Provide `aria-label` on icon-only buttons (notification bell, sidebar collapse, modal close).
3. **High Contrast Ratios:** Ensure text on translucent dark backgrounds passes WCAG AA contrast standards (minimum 4.5:1 ratio).
4. **Keyboard Navigability:** All interactive buttons and form inputs must have visible `:focus-visible` glowing cyan outlines.

---

### 6. Data Validation Rules
1. **Student Registration:**
   - Full Name: Minimum 2 characters, alphabets and spaces only.
   - Roll Number: Required, alphanumeric (e.g., `CS-042`).
   - Class ID: Must match an active class identifier.
   - Parent Phone: 10 digits numeric format.
2. **Attendance Operations:**
   - Marking attendance requires a valid Class, Subject, and Date selection.
   - Preventing empty attendance submissions (all students must have an assigned state).
3. **Notification Dispatch:**
   - Notification messages must not be empty or whitespace-only.
   - Target must be explicitly selected (All, Class, or Student).
