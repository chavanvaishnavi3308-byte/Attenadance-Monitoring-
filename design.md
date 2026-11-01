# AttendX Design System & Visual Guidelines
## Futuristic 3D Glassmorphism Smart Campus Specification

**Version:** 1.0.0  
**Aesthetic:** Cybernetic Glassmorphism, Deep Navy Dark Mode, Glowing Laser Accents, 3D Elevation  

---

### 1. Color System

#### 1.1 Base & Background Palette
| Token Name | Hex Code | Purpose |
|---|---|---|
| `--bg-space-dark` | `#060919` | Deep space root background |
| `--bg-surface-navy` | `#0B112C` | Secondary background & deep container base |
| `--glass-panel-bg` | `rgba(13, 22, 53, 0.72)` | Primary glassmorphism card background |
| `--glass-border` | `rgba(0, 240, 255, 0.18)` | Subtle glowing border for glass cards |
| `--glass-border-hover` | `rgba(0, 240, 255, 0.45)` | Elevated border glow on interaction |

#### 1.2 Futuristic Accent Palette
| Accent | Hex Code | Glow / Shadow | Usage |
|---|---|---|---|
| **Cyan Laser** | `#00F0FF` | `0 0 16px rgba(0, 240, 255, 0.5)` | Primary CTAs, active indicators, focus outlines |
| **Electric Violet**| `#8B5CF6` | `0 0 16px rgba(139, 92, 246, 0.5)` | Secondary accents, hero gradients, badges |
| **Emerald Cyber** | `#10B981` | `0 0 12px rgba(16, 185, 129, 0.4)` | Present status, positive metrics, success toasts |
| **Coral Alert** | `#EF4444` | `0 0 12px rgba(239, 68, 68, 0.4)` | Absent status, low attendance warnings, danger |
| **Solar Amber** | `#F59E0B` | `0 0 12px rgba(245, 158, 11, 0.4)` | Late status, caution alerts, streak icons |
| **Sky Radiant** | `#38BDF8` | `0 0 12px rgba(56, 189, 248, 0.4)` | Informational notifications, link hovers |

#### 1.3 Text Hierarchy Palette
| Token Name | Hex / Value | Usage |
|---|---|---|
| `--text-primary` | `#F8FAFC` | Primary headings, prominent values, modal titles |
| `--text-secondary`| `#94A3B8` | Subtitles, labels, descriptions, table body |
| `--text-muted` | `#64748B` | Timestamps, inactive tabs, placeholder text |

---

### 2. Typography

- **Headings & Brand:** `'Plus Jakarta Sans', 'Outfit', sans-serif`
  - Hero Headline: `clamp(2.5rem, 5vw, 4.2rem)`, weight 800, line-height 1.1.
  - Section Headings: `clamp(1.75rem, 3vw, 2.4rem)`, weight 700.
  - Card Titles: `1.15rem`, weight 600, letter-spacing -0.01em.
- **Body & Data Displays:** `'Inter', sans-serif`
  - Body Text: `0.95rem`, weight 400, line-height 1.6.
  - Badges & Chips: `0.75rem`, weight 600, uppercase, letter-spacing 0.05em.
- **Numbers & Roll Identifiers:** `'JetBrains Mono', monospace`
  - Roll Numbers & IDs: `0.85rem`, weight 500.

---

### 3. Spacing & Radius System

- **Spacing Scale:**
  - `xs`: 4px | `sm`: 8px | `md`: 16px | `lg`: 24px | `xl`: 32px | `2xl`: 48px | `3xl`: 64px
- **Border Radii:**
  - Micro Badges: `6px`
  - Buttons & Inputs: `12px`
  - Glass Cards: `20px`
  - Hero Mockup & Modals: `24px`
  - Circular Gauges & Avatars: `9999px` (Pill/Circle)

---

### 4. Components

#### 4.1 Glassmorphic Cards (`.glass-card`)
```css
background: rgba(13, 22, 53, 0.72);
backdrop-filter: blur(16px);
-webkit-backdrop-filter: blur(16px);
border: 1px solid rgba(0, 240, 255, 0.16);
border-radius: 20px;
box-shadow: 0 12px 32px -4px rgba(0, 0, 0, 0.4), inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.3s ease, box-shadow 0.3s ease;
```

#### 4.2 Buttons
- **Primary Cyber Button (`.btn-cyber-primary`):** Cyan-to-blue gradient fill, glowing box shadow, bold white text, hover lift.
- **Secondary Glass Button (`.btn-cyber-ghost`):** Translucent background with glowing border and cyan hover text.
- **Status Toggle Buttons:**
  - `.btn-status-present`: Green background when active, emerald neon glow.
  - `.btn-status-absent`: Red background when active, coral neon glow.
  - `.btn-status-late`: Amber background when active, solar amber glow.

#### 4.3 Forms & Inputs
- Translucent input backgrounds (`rgba(7, 12, 33, 0.6)`), border radius 12px, glowing cyan outline on `:focus-visible`.

#### 4.4 Charts
- Chart.js initialized with dark background canvas grid lines (`rgba(255, 255, 255, 0.05)`), neon cyan/violet gradient fills, and customized glass tooltip overlays.

---

### 5. Responsive Design Rules
- **Desktop (>= 1024px):** Fixed glass sidebar, top navigation bar, 4-column metric grid, side-by-side charts and data tables.
- **Tablet (768px - 1023px):** Compact sidebar with icon labels, 2-column metric cards, full-width responsive charts.
- **Mobile (< 768px):** Slide-in off-canvas drawer controlled via hamburger icon, 1-column stacked metric cards, horizontally scrollable data tables with sticky action buttons, touch-friendly tap targets (minimum 44x44px).

---

### 6. Animation & Micro-interactions
- **Page / View Fade & Lift:** `@keyframes viewSlideIn { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }`
- **Floating 3D Elements:** `@keyframes floatSlow { 0%, 100% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-12px) rotate(1.5deg); } }`
- **Pulsing Neon Glow:** Soft breathing opacity between 0.4 and 0.85 on notification indicators.
- **Progress Bar Fill:** Linear transitions on width for subject attendance visualization.
