/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Core Application Controller, Interactive Visuals, and Routing
 * 
 * Configured Authorities:
 * - Admin: Dr. Vidya Mohod Ma’am
 * - Teachers (6): Swapnali Jadhav, Anuja Kanawade, Srushti Parab, Trupti Thakur, Sneha Mokal / Mali, Chaitrali Naik
 * - Parent: Rajaram Chavan (Student: Vaishnavi Chavan, Dept: Computer Science CS)
 * - Departments: Computer Science (CS), Information Technology (IT)
 * - Classes: CS, IT
 * - Students: 15 total (10 CS, 5 IT)
 */

document.addEventListener("DOMContentLoaded", () => {
  // =========================================================================
  // 1. CYBER CANVAS 60FPS STARFIELD & CONSTELLATION SIMULATION
  // =========================================================================
  const canvas = document.getElementById("cyberCanvas");
  if (canvas) {
    const ctx = canvas.getContext("2d");
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener("resize", () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(65, Math.floor(window.innerWidth / 20));

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.45,
        vy: (Math.random() - 0.5) * 0.45,
        radius: Math.random() * 2 + 1,
        color: Math.random() > 0.4 ? "rgba(0, 240, 255, " : "rgba(139, 92, 246, "
      });
    }

    let mouseX = -1000;
    let mouseY = -1000;
    window.addEventListener("mousemove", e => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    function renderCanvas() {
      ctx.clearRect(0, 0, width, height);

      // Draw subtle cyber grid
      ctx.strokeStyle = "rgba(0, 240, 255, 0.015)";
      ctx.lineWidth = 1;
      const gridSize = 60;
      for (let x = 0; x < width; x += gridSize) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }
      for (let y = 0; y < height; y += gridSize) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.stroke();
      }

      // Draw particles & connect constellation lines
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        // Subtle mouse push
        const dxM = p.x - mouseX;
        const dyM = p.y - mouseY;
        const distM = Math.sqrt(dxM * dxM + dyM * dyM);
        if (distM < 120) {
          p.x += (dxM / distM) * 1.5;
          p.y += (dyM / distM) * 1.5;
        }

        ctx.fillStyle = p.color + "0.8)";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dx = p.x - p2.x;
          const dy = p.y - p2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 130) {
            const alpha = (1 - dist / 130) * 0.18;
            ctx.strokeStyle = `rgba(0, 240, 255, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(renderCanvas);
    }
    renderCanvas();
  }

  // =========================================================================
  // 2. SYNTHESIZED WEB AUDIO FEEDBACK
  // =========================================================================
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) audioCtx = new AudioContext();
    }
    if (audioCtx && audioCtx.state === "suspended") {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playCyberTone(type = "success") {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      const now = ctx.currentTime;
      if (type === "success") {
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.15); // G5
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      } else if (type === "alert") {
        osc.type = "sawtooth";
        osc.frequency.setValueAtTime(880, now);
        osc.frequency.exponentialRampToValueAtTime(440, now + 0.25);
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        osc.start(now);
        osc.stop(now + 0.3);
      }
    } catch (e) {
      // Audio autoplay policy fallback
    }
  }

  // =========================================================================
  // 3. TOAST SYSTEM
  // =========================================================================
  function showToast(title, message, severity = "success") {
    playCyberTone(severity === "danger" ? "alert" : "success");
    const container = document.getElementById("toast-container");
    if (!container) return;

    const toast = document.createElement("div");
    toast.className = `toast toast-${severity}`;

    let iconName = "check-circle";
    if (severity === "danger") iconName = "alert-circle";
    if (severity === "warning") iconName = "alert-triangle";
    if (severity === "info") iconName = "info";

    toast.innerHTML = `
      <div style="color: ${severity === 'danger' ? 'var(--coral)' : severity === 'warning' ? 'var(--amber)' : 'var(--cyan)'}; font-size: 1.3rem;">
        <i data-lucide="${iconName}"></i>
      </div>
      <div style="flex-grow: 1;">
        <div style="font-weight: 700; font-size: 0.9rem; color: #FFFFFF;">${title}</div>
        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 2px;">${message}</div>
      </div>
      <button class="toast-close" style="background:none; border:none; color:var(--text-muted); cursor:pointer;">
        <i data-lucide="x" style="width:16px;height:16px;"></i>
      </button>
    `;

    container.appendChild(toast);
    if (window.lucide) window.lucide.createIcons();

    const closeBtn = toast.querySelector(".toast-close");
    closeBtn.addEventListener("click", () => toast.remove());

    setTimeout(() => {
      toast.style.transition = "opacity 0.4s ease, transform 0.4s ease";
      toast.style.opacity = "0";
      toast.style.transform = "translateX(50px)";
      setTimeout(() => toast.remove(), 400);
    }, 4500);
  }
  window.showToast = showToast;

  // =========================================================================
  // 4. LIVE HEADER CLOCK & SEARCH
  // =========================================================================
  function updateLiveClock() {
    const el = document.getElementById("liveCampusClock");
    if (el) {
      const now = new Date();
      const dateStr = now.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
      const timeStr = now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
      el.textContent = `${dateStr} • ${timeStr} • Campus Active`;
    }
  }
  setInterval(updateLiveClock, 1000);
  updateLiveClock();

  // Global Search Box
  const globalSearchInput = document.getElementById("globalSearchInput");
  if (globalSearchInput) {
    globalSearchInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const query = globalSearchInput.value.trim();
        if (query) {
          switchView("students");
          const searchField = document.getElementById("studentSearchInput");
          if (searchField) {
            searchField.value = query;
            renderStudentTable();
          }
        }
      }
    });
  }

  // =========================================================================
  // 5. VIEW ROUTER & NAVIGATION
  // =========================================================================
  let currentActiveView = "landing";

  // Update sidebar navigation links based on authenticated user role
  function updateSidebarNavigation(role) {
    const parentHiddenViews = [
      "teacher-dashboard",
      "students",
      "teachers-dir",
      "analytics",
      "reports",
      "admin-dashboard",
      "student-dashboard"
    ];
    const studentHiddenViews = [
      "admin-dashboard",
      "teacher-dashboard",
      "parent-dashboard",
      "students",
      "teachers-dir",
      "reports",
      "analytics"
    ];
    const teacherHiddenViews = [
      "admin-dashboard",
      "parent-dashboard",
      "student-dashboard"
    ];
    const adminHiddenViews = [
      "parent-dashboard",
      "student-dashboard"
    ];

    document.querySelectorAll(".nav-link-item[data-view]").forEach(link => {
      const view = link.getAttribute("data-view");
      let shouldHide = false;

      if (role === "parent") {
        shouldHide = parentHiddenViews.includes(view);
      } else if (role === "student") {
        shouldHide = studentHiddenViews.includes(view);
      } else if (role === "teacher") {
        shouldHide = teacherHiddenViews.includes(view);
      } else if (role === "admin") {
        shouldHide = adminHiddenViews.includes(view);
      }

      link.style.display = shouldHide ? "none" : "flex";
    });
  }
  window.updateSidebarNavigation = updateSidebarNavigation;

  function switchView(viewName) {
    // Role-based route authorization guard
    const currentUser = window.attendxStore.getCurrentUser();
    if (currentUser) {
      if (currentUser.role === "parent") {
        const parentBlockedViews = [
          "teacher-dashboard",
          "students",
          "teachers-dir",
          "analytics",
          "reports",
          "admin-dashboard",
          "student-dashboard",
          "campus-classes"
        ];
        if (parentBlockedViews.includes(viewName)) {
          viewName = "parent-dashboard";
        }
      } else if (currentUser.role === "student") {
        const studentBlockedViews = [
          "admin-dashboard",
          "teacher-dashboard",
          "parent-dashboard",
          "students",
          "teachers-dir",
          "reports",
          "campus-classes"
        ];
        if (studentBlockedViews.includes(viewName)) {
          viewName = "student-dashboard";
        }
      } else if (currentUser.role === "teacher") {
        const teacherBlockedViews = [
          "admin-dashboard",
          "parent-dashboard",
          "student-dashboard"
        ];
        if (teacherBlockedViews.includes(viewName)) {
          viewName = "teacher-dashboard";
        }
      }
    }

    currentActiveView = viewName;

    // Toggle Landing Page vs App Shell
    const landingView = document.getElementById("view-landing");
    const appShell = document.getElementById("app-shell");

    if (viewName === "landing") {
      if (landingView) landingView.style.display = "block";
      if (appShell) appShell.classList.remove("active");
      window.scrollTo({ top: 0, behavior: "smooth" });
      return;
    }

    if (landingView) landingView.style.display = "none";
    if (appShell) appShell.classList.add("active");

    // Hide all portal views
    const allViews = document.querySelectorAll(".app-view");
    allViews.forEach(v => v.classList.remove("active-view"));

    // Activate specific view
    const targetView = document.getElementById(`view-${viewName}`);
    if (targetView) {
      targetView.classList.add("active-view");
    }

    // Update sidebar active links
    document.querySelectorAll(".nav-link-item").forEach(link => {
      if (link.getAttribute("data-view") === viewName) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });

    // Close mobile drawer if open
    const sidebar = document.querySelector(".app-sidebar");
    if (sidebar) sidebar.classList.remove("mobile-open");

    // Trigger chart refreshes & data loads
    if (viewName === "admin-dashboard") {
      renderAdminDashboard();
    } else if (viewName === "campus-classes") {
      renderCampusClassesView();
    } else if (viewName === "teachers-dir") {
      renderTeachersDirectory();
    } else if (viewName === "teacher-dashboard") {
      initTeacherDashboard();
    } else if (viewName === "parent-dashboard") {
      renderParentDashboard();
    } else if (viewName === "student-dashboard") {
      renderStudentDashboard();
    } else if (viewName === "students") {
      renderStudentTable();
    } else if (viewName === "notifications") {
      renderNotificationCenter();
    } else if (viewName === "analytics") {
      renderAnalyticsView();
    } else if (viewName === "reports") {
      initReportsPage();
    }

    if (window.lucide) window.lucide.createIcons();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  window.switchView = switchView;

  // Sidebar link clicks
  document.querySelectorAll(".nav-link-item[data-view]").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const view = link.getAttribute("data-view");
      switchView(view);
    });
  });

  // Mobile menu button
  const mobileMenuBtn = document.getElementById("mobileMenuBtn");
  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener("click", () => {
      const sidebar = document.querySelector(".app-sidebar");
      if (sidebar) sidebar.classList.toggle("mobile-open");
    });
  }

  // =========================================================================
  // 6. ROLE SWITCHER & LOGIN MODAL (Dr. Vidya Mohod Ma’am, Rajaram Chavan)
  // =========================================================================
  const loginModal = document.getElementById("loginModal");
  let selectedLoginRole = "admin";

  function clearLoginFields(keepReadonly = true) {
    const emailInput = document.getElementById("loginEmail");
    const passInput = document.getElementById("loginPassword");
    const showPassCheckbox = document.getElementById("showPasswordCheckbox");
    const passIcon = document.getElementById("togglePasswordIcon");

    if (emailInput) {
      emailInput.value = "";
      delete emailInput.dataset.userTyped;
      if (keepReadonly) emailInput.setAttribute("readonly", "true");
    }
    if (passInput) {
      passInput.value = "";
      passInput.type = "password";
      delete passInput.dataset.userTyped;
      if (keepReadonly) passInput.setAttribute("readonly", "true");
    }
    if (showPassCheckbox) {
      showPassCheckbox.checked = false;
    }
    if (passIcon) {
      passIcon.setAttribute("data-lucide", "eye");
      if (window.lucide) window.lucide.createIcons();
    }
    hideLoginError();
  }

  function openLoginModal(defaultRole = "admin") {
    selectedLoginRole = defaultRole;
    clearLoginFields(true);
    updateRoleSelectionCards(defaultRole);
    if (loginModal) loginModal.classList.add("active");

    // Guard against aggressive asynchronous browser password manager injections
    [50, 150, 300].forEach(delay => {
      setTimeout(() => {
        const emailInput = document.getElementById("loginEmail");
        const passInput = document.getElementById("loginPassword");
        if (emailInput && !emailInput.dataset.userTyped && emailInput.value !== "") {
          emailInput.value = "";
        }
        if (passInput && !passInput.dataset.userTyped && passInput.value !== "") {
          passInput.value = "";
        }
      }, delay);
    });
  }
  window.openLoginModal = openLoginModal;

  function closeLoginModal() {
    clearLoginFields(true);
    if (loginModal) loginModal.classList.remove("active");
  }
  window.closeLoginModal = closeLoginModal;

  function showLoginError(message) {
    const errorBox = document.getElementById("loginErrorMessage");
    const errorText = document.getElementById("loginErrorText");
    if (errorBox && errorText) {
      errorText.textContent = message;
      errorBox.style.display = "flex";
      if (window.lucide) window.lucide.createIcons();
    }
    showToast("Authentication Failed", message, "danger");
  }

  function hideLoginError() {
    const errorBox = document.getElementById("loginErrorMessage");
    const errorText = document.getElementById("loginErrorText");
    if (errorBox) errorBox.style.display = "none";
    if (errorText) errorText.textContent = "";
  }

  function updateRoleSelectionCards(role) {
    selectedLoginRole = role;
    clearLoginFields(true);
    document.querySelectorAll(".role-card-item").forEach(card => {
      if (card.getAttribute("data-role") === role) {
        card.classList.add("selected");
      } else {
        card.classList.remove("selected");
      }
    });

    const accountSelect = document.getElementById("loginAccountSelect");
    const accountLabel = document.getElementById("loginAccountSelectLabel");
    const roleBadge = document.getElementById("loginRoleBadge");

    // Guard against asynchronous autofill after role selection
    [50, 150, 300].forEach(delay => {
      setTimeout(() => {
        const emailInput = document.getElementById("loginEmail");
        const passInput = document.getElementById("loginPassword");
        if (emailInput && !emailInput.dataset.userTyped && emailInput.value !== "") {
          emailInput.value = "";
        }
        if (passInput && !passInput.dataset.userTyped && passInput.value !== "") {
          passInput.value = "";
        }
      }, delay);
    });

    // Dynamic placeholders based on selected operational role
    const emailInput = document.getElementById("loginEmail");
    const passInput = document.getElementById("loginPassword");
    if (emailInput) {
      if (role === "admin") {
        emailInput.placeholder = "e.g. admin@attendx.edu or admin";
      } else if (role === "teacher") {
        emailInput.placeholder = "e.g. swapnali.jadhav@attendx.edu or username";
      } else if (role === "student") {
        emailInput.placeholder = "e.g. vaishnavi.chavan@attendx.edu or roll no";
      } else if (role === "parent") {
        emailInput.placeholder = "e.g. rajaram.chavan@parent.attendx.edu or phone";
      }
    }
    if (passInput) {
      if (role === "admin") {
        passInput.placeholder = "Enter administrator portal password";
      } else if (role === "teacher") {
        passInput.placeholder = "Enter faculty portal password";
      } else if (role === "student") {
        passInput.placeholder = "Enter student portal password";
      } else if (role === "parent") {
        passInput.placeholder = "Enter guardian portal password";
      }
    }

    if (accountSelect) {
      if (role === "admin") {
        if (accountLabel) accountLabel.textContent = "2. CHOOSE ADMINISTRATIVE PROFILE";
        const admin = window.attendxStore.getDemoAccounts().admin;
        accountSelect.innerHTML = `<option value="${admin.id}" data-email="${admin.email}">${admin.name} — ${admin.title}</option>`;
        if (roleBadge) roleBadge.textContent = "ADMIN: Dr. Vidya Mohod";
      } else if (role === "teacher") {
        if (accountLabel) accountLabel.textContent = "2. CHOOSE FACULTY / TEACHER PROFILE";
        const teachers = window.attendxStore.getTeachers();
        accountSelect.innerHTML = teachers.map(t => {
          const acc = window.attendxStore.getAccountByProfileId ? window.attendxStore.getAccountByProfileId(t.id) : null;
          const statusTag = acc ? "" : " — [No Portal Account]";
          return `<option value="${t.id}" data-email="${t.email}">Prof. ${t.name} — ${t.title || 'Faculty'} (${t.assignedClass} Class)${statusTag}</option>`;
        }).join("");
        if (teachers.length > 0 && roleBadge) {
          roleBadge.textContent = `TEACHER: ${teachers[0].name.split(" ")[0]}`;
        }
      } else if (role === "student") {
        if (accountLabel) accountLabel.textContent = "2. CHOOSE STUDENT PROFILE";
        const students = window.attendxStore.getStudents();
        accountSelect.innerHTML = students.map(s => `
          <option value="${s.id}" data-email="${s.email}">${s.name} (Roll: ${s.rollNo} • Class: ${s.classId})</option>
        `).join("");
        if (students.length > 0 && roleBadge) {
          roleBadge.textContent = `STUDENT: ${students[0].name.split(" ")[0]}`;
        }
      } else if (role === "parent") {
        if (accountLabel) accountLabel.textContent = "2. CHOOSE GUARDIAN / PARENT OF";
        const students = window.attendxStore.getStudents();
        accountSelect.innerHTML = students.map(s => {
          const parentName = s.parentName || "Parent of " + s.name;
          const parentEmail = s.parentEmail || `${s.rollNo.toLowerCase()}.parent@attendx.edu`;
          return `<option value="${s.id}" data-email="${parentEmail}">${parentName} — Guardian of ${s.name} (${s.classId})</option>`;
        }).join("");
        if (students.length > 0 && roleBadge) {
          roleBadge.textContent = `PARENT: ${students[0].name.split(" ")[0]}'s Parent`;
        }
      }
    }
  }

  // Account selector dropdown change handler: clear fields and update badge only
  const loginAccountSelect = document.getElementById("loginAccountSelect");
  if (loginAccountSelect) {
    loginAccountSelect.addEventListener("change", () => {
      clearLoginFields(true);
      const selectedOption = loginAccountSelect.options[loginAccountSelect.selectedIndex];
      if (selectedOption) {
        const roleBadge = document.getElementById("loginRoleBadge");
        if (roleBadge) {
          const labelText = selectedOption.textContent.split("—")[0].trim();
          roleBadge.textContent = `${selectedLoginRole.toUpperCase()}: ${labelText}`;
        }
      }
    });
  }

  // Input listeners: remove readonly on user interaction, track typing
  const loginEmailEl = document.getElementById("loginEmail");
  if (loginEmailEl) {
    loginEmailEl.addEventListener("focus", () => loginEmailEl.removeAttribute("readonly"));
    loginEmailEl.addEventListener("input", () => {
      loginEmailEl.dataset.userTyped = "true";
      hideLoginError();
    });
  }
  const loginPassEl = document.getElementById("loginPassword");
  if (loginPassEl) {
    loginPassEl.addEventListener("focus", () => loginPassEl.removeAttribute("readonly"));
    loginPassEl.addEventListener("input", () => {
      loginPassEl.dataset.userTyped = "true";
      hideLoginError();
    });
  }

  // Password visibility toggle handler (eye button and checkbox)
  function togglePasswordVisibility(forceShow = null) {
    const passInput = document.getElementById("loginPassword");
    const passIcon = document.getElementById("togglePasswordIcon");
    const passCheckbox = document.getElementById("showPasswordCheckbox");
    if (!passInput) return;

    const willShow = forceShow !== null ? forceShow : (passInput.type === "password");
    passInput.type = willShow ? "text" : "password";

    if (passCheckbox) passCheckbox.checked = willShow;

    if (passIcon) {
      passIcon.setAttribute("data-lucide", willShow ? "eye-off" : "eye");
      if (window.lucide) window.lucide.createIcons();
    }
  }

  const btnTogglePassword = document.getElementById("btnTogglePassword");
  if (btnTogglePassword) {
    btnTogglePassword.addEventListener("click", () => togglePasswordVisibility());
  }

  const showPasswordCheckbox = document.getElementById("showPasswordCheckbox");
  if (showPasswordCheckbox) {
    showPasswordCheckbox.addEventListener("change", (e) => togglePasswordVisibility(e.target.checked));
  }

  document.querySelectorAll(".role-card-item").forEach(card => {
    card.addEventListener("click", () => {
      const role = card.getAttribute("data-role");
      updateRoleSelectionCards(role);
    });
  });

  // Credential validation logic against Registered Accounts Authority
  function validateUserCredentials(role, accountId, identifier, password) {
    if (!identifier && !password) {
      return { error: "Please enter your registered email or username and password." };
    }
    if (!identifier) {
      return { error: "Please enter your registered email or username." };
    }
    if (!password) {
      return { error: "Please enter your password." };
    }

    const q = identifier.trim().toLowerCase();
    const accounts = window.attendxStore.getAccounts ? window.attendxStore.getAccounts() : [];
    const demoAccounts = window.attendxStore.getDemoAccounts();
    const teachers = window.attendxStore.getTeachers();
    const students = window.attendxStore.getStudents();

    // 1. Identify directory profile matching identifier / accountId
    let directoryProfile = null;

    if (role === "admin") {
      const admin = demoAccounts.admin;
      const isAdminMatch = (
        q === "admin" ||
        q === "admin@attendx.edu" ||
        q === admin.id.toLowerCase() ||
        (admin.email && admin.email.toLowerCase() === q) ||
        q.includes("vidya") ||
        (admin.name && admin.name.toLowerCase() === q)
      );
      if (isAdminMatch) directoryProfile = admin;
    } else if (role === "teacher") {
      const isTeacherMatch = (t) => {
        if (!t) return false;
        const email = (t.email || "").toLowerCase();
        const username = email.split("@")[0];
        const id = (t.id || "").toLowerCase();
        const name = (t.name || "").toLowerCase();
        return q === email || q === username || q === id || q === name || (q === "swapnalijadhav@gmail.com" && t.id === "TCH-001");
      };

      const selectedTeacher = teachers.find(t => t.id === accountId);
      if (selectedTeacher && isTeacherMatch(selectedTeacher)) {
        directoryProfile = selectedTeacher;
      } else {
        directoryProfile = teachers.find(isTeacherMatch) || null;
      }
    } else if (role === "student") {
      const isStudentMatch = (s) => {
        if (!s) return false;
        const email = (s.email || "").toLowerCase();
        const username = email.split("@")[0];
        const id = (s.id || "").toLowerCase();
        const roll = (s.rollNo || "").toLowerCase();
        const name = (s.name || "").toLowerCase();
        return q === email || q === username || q === id || q === roll || q === name;
      };

      const selectedStudent = students.find(s => s.id === accountId);
      if (selectedStudent && isStudentMatch(selectedStudent)) {
        directoryProfile = selectedStudent;
      } else {
        directoryProfile = students.find(isStudentMatch) || null;
      }
    } else if (role === "parent") {
      const isParentMatch = (s) => {
        if (!s) return false;
        const pEmail = (s.parentEmail || `${s.rollNo.toLowerCase()}.parent@attendx.edu`).toLowerCase();
        const pUsername = pEmail.split("@")[0];
        const pPhone = (s.parentPhone || "").replace(/\D/g, "");
        const pName = (s.parentName || "").toLowerCase();
        const childRoll = (s.rollNo || "").toLowerCase();
        const childId = (s.id || "").toLowerCase();
        const parentId = ("prn-" + s.id).toLowerCase();
        const cleanQ = q.replace(/\D/g, "");

        return (
          q === pEmail ||
          q === pUsername ||
          q === pName ||
          q === childRoll ||
          q === childId ||
          q === parentId ||
          (cleanQ.length >= 6 && pPhone && cleanQ === pPhone)
        );
      };

      const selectedStudent = students.find(s => s.id === accountId);
      if (selectedStudent && isParentMatch(selectedStudent)) {
        directoryProfile = selectedStudent;
      } else {
        directoryProfile = students.find(isParentMatch) || null;
      }
    }

    // 2. Identify registered account in the authentication store
    let registeredAccount = accounts.find(acc => {
      if (acc.role !== role) return false;
      if (directoryProfile && (acc.profileId === directoryProfile.id || (acc.email && acc.email.toLowerCase() === (directoryProfile.email || "").toLowerCase()))) {
        return true;
      }
      const accEmail = (acc.email || "").toLowerCase();
      const accUsername = (acc.username || "").toLowerCase();
      const aliases = (acc.aliases || []).map(a => (a || "").toLowerCase());
      return q === accEmail || q === accUsername || aliases.includes(q);
    });

    // If not found in selected role tab, auto-detect across all registered accounts by identifier
    // to authoritatively honor the verified account's actual role!
    if (!registeredAccount) {
      registeredAccount = accounts.find(acc => {
        const accEmail = (acc.email || "").toLowerCase();
        const accUsername = (acc.username || "").toLowerCase();
        const aliases = (acc.aliases || []).map(a => (a || "").toLowerCase());
        return q === accEmail || q === accUsername || aliases.includes(q);
      });
      if (registeredAccount) {
        role = registeredAccount.role;
      }
    }

    // 3. Handle directory profiles without an active registered account
    if (directoryProfile && !registeredAccount) {
      if (role === "teacher") {
        return {
          error: `No portal login account is registered for Prof. ${directoryProfile.name}. Please contact Administrator (Dr. Vidya Mohod) to provision portal access.`
        };
      } else {
        return {
          error: `No active portal login account is registered for this ${role} profile. Please contact Administrator (Dr. Vidya Mohod).`
        };
      }
    }

    // 4. Handle unrecognized credentials
    if (!registeredAccount) {
      return {
        error: `Invalid credentials. No registered ${role} profile or account found for "${identifier}".`
      };
    }

    // 5. Account status check
    if (registeredAccount.status && registeredAccount.status !== "active") {
      return {
        error: "This portal account has been deactivated or suspended. Please contact Administrator (Dr. Vidya Mohod)."
      };
    }

    // 6. Verify credentials against registered account's password
    const acceptedPasswords = [
      registeredAccount.password,
      ...(registeredAccount.acceptedPasswords || [])
    ].filter(Boolean);

    const isPasswordValid = acceptedPasswords.includes(password);
    if (!isPasswordValid) {
      return { error: "Incorrect password. Please verify your credentials and try again." };
    }

    // 7. Successful authentication: assemble session user with verified account role
    const effectiveRole = registeredAccount.role || role;
    let userSession = null;
    if (effectiveRole === "admin") {
      userSession = { ...demoAccounts.admin, role: "admin" };
    } else if (effectiveRole === "teacher") {
      const t = teachers.find(x => x.id === registeredAccount.profileId) || directoryProfile;
      userSession = { ...t, role: "teacher" };
    } else if (effectiveRole === "student") {
      const s = students.find(x => x.id === registeredAccount.profileId) || directoryProfile;
      userSession = { ...s, role: "student", studentId: s.id };
    } else if (effectiveRole === "parent") {
      const s = directoryProfile || students.find(x => x.id === registeredAccount.profileId) || students[0];
      userSession = {
        id: "PRN-" + s.id,
        name: s.parentName || `Guardian of ${s.name}`,
        role: "parent",
        email: registeredAccount.email || s.parentEmail || `${s.rollNo.toLowerCase()}.parent@attendx.edu`,
        studentId: s.id,
        childName: s.name,
        avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=200&q=80",
        title: `Guardian of ${s.name}`,
        department: `${s.department} (${s.classId})`
      };
    }

    return { user: userSession };
  }

  // Quick Demo Login: populate demo credentials ONLY when explicitly clicked, then login
  const btnQuickDemo = document.getElementById("btnQuickDemoLogin");
  if (btnQuickDemo) {
    btnQuickDemo.addEventListener("click", () => {
      hideLoginError();
      const accountSelect = document.getElementById("loginAccountSelect");
      const accountId = accountSelect?.value || "";
      const emailInput = document.getElementById("loginEmail");
      const passInput = document.getElementById("loginPassword");

      let demoEmail = "";
      let demoPass = "";

      if (selectedLoginRole === "admin") {
        demoEmail = "admin@attendx.edu";
        demoPass = "admin123";
      } else if (selectedLoginRole === "teacher") {
        demoEmail = "swapnali.jadhav@attendx.edu";
        demoPass = "swapnali@123";
      } else if (selectedLoginRole === "student") {
        demoEmail = "vaishnavi.chavan@attendx.edu";
        demoPass = "vaishnavi@123";
      } else if (selectedLoginRole === "parent") {
        demoEmail = "rajaram.chavan@parent.attendx.edu";
        demoPass = "rajaram@123";
      }

      // Explicitly populate credentials only upon clicking Quick Demo Login
      if (emailInput) {
        emailInput.removeAttribute("readonly");
        emailInput.value = demoEmail;
        delete emailInput.dataset.userTyped;
      }
      if (passInput) {
        passInput.removeAttribute("readonly");
        passInput.value = demoPass;
        delete passInput.dataset.userTyped;
      }

      const result = validateUserCredentials(selectedLoginRole, accountId, demoEmail, demoPass);
      if (result.user) {
        completeLogin(result.user);
      }
    });
  }

  // Manual Form Submission: validates credentials against the authentication system
  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      hideLoginError();

      const accountSelect = document.getElementById("loginAccountSelect");
      const accountId = accountSelect?.value || "";
      const emailInput = document.getElementById("loginEmail");
      const passInput = document.getElementById("loginPassword");
      const identifier = emailInput ? emailInput.value.trim() : "";
      const password = passInput ? passInput.value : "";

      const result = validateUserCredentials(selectedLoginRole, accountId, identifier, password);
      if (result.error) {
        showLoginError(result.error);
        if (!identifier && emailInput) {
          emailInput.removeAttribute("readonly");
          emailInput.focus();
        } else if (!password && passInput) {
          passInput.removeAttribute("readonly");
          passInput.focus();
        } else if (result.error.toLowerCase().includes("password") && passInput) {
          passInput.removeAttribute("readonly");
          passInput.focus();
        } else if (emailInput) {
          emailInput.removeAttribute("readonly");
          emailInput.focus();
        }
        return;
      }

      completeLogin(result.user);
    });
  }

  function completeLogin(user) {
    // Sanitize user: ensure no plaintext passwords in session
    const safeUser = { ...user };
    delete safeUser.password;

    const rememberCheckbox = document.getElementById("rememberSessionCheckbox");
    const rememberMe = rememberCheckbox ? rememberCheckbox.checked : true;

    if (rememberMe) {
      window.attendxStore.setCurrentUser(safeUser);
      try { sessionStorage.removeItem("attendx_v2_currentUser"); } catch (e) {}
    } else {
      try {
        sessionStorage.setItem("attendx_v2_currentUser", JSON.stringify(safeUser));
        localStorage.removeItem(window.attendxStore.STORAGE_KEYS.CURRENT_USER);
      } catch (e) {}
      window.attendxStore.emit("userChanged", safeUser);
    }

    closeLoginModal();

    showToast("Authenticated", `Welcome, ${safeUser.name} (${safeUser.role.toUpperCase()})`, "success");

    // Dynamic sidebar navigation filtered by authenticated user role
    updateSidebarNavigation(safeUser.role);

    // Direct routing to verified role's dashboard
    if (safeUser.role === "admin") {
      switchView("admin-dashboard");
    } else if (safeUser.role === "teacher") {
      currentTeacherState.teacherName = safeUser.name;
      if (safeUser.assignedClass) currentTeacherState.classId = safeUser.assignedClass;
      switchView("teacher-dashboard");
    } else if (safeUser.role === "parent") {
      switchView("parent-dashboard");
    } else if (safeUser.role === "student") {
      switchView("student-dashboard");
    }

    updateUserInterfaceSession(safeUser);
  }
  window.completeLogin = completeLogin;
  window.validateUserCredentials = validateUserCredentials;

  function updateUserInterfaceSession(user) {
    if (!user) return;
    const avatarEls = document.querySelectorAll(".user-session-avatar");
    const nameEls = document.querySelectorAll(".user-session-name");
    const titleEls = document.querySelectorAll(".user-session-title");
    const roleEls = document.querySelectorAll(".user-session-role");

    avatarEls.forEach(img => { img.src = user.avatar; });
    nameEls.forEach(el => { el.textContent = user.name; });
    titleEls.forEach(el => { el.textContent = user.title || user.department || "Campus Faculty"; });
    roleEls.forEach(el => { el.textContent = user.role.toUpperCase(); });

    updateSidebarNavigation(user.role);
  }

  window.handleLogout = function() {
    try {
      sessionStorage.removeItem("attendx_v2_currentUser");
    } catch (e) {}
    window.attendxStore.logout();
    clearLoginFields(true);
    showToast("Signed Out", "You have securely disconnected from the campus terminal.", "info");
    updateSidebarNavigation("admin");
    switchView("landing");
  };

  window.openRoleSwitchDropdown = function() {
    openLoginModal(window.attendxStore.getCurrentUser()?.role || "admin");
  };

  // =========================================================================
  // 7. ADMIN DASHBOARD INITIALIZATION (Requirements 1 & 11)
  // =========================================================================
  function renderAdminDashboard() {
    const stats = window.attendxStore.getCampusStats();

    // 4 Dynamic KPI Cards (Students: 15, Teachers: 6, Departments: 2, Classes: 2)
    const totalStudentsEl = document.getElementById("adminKpiTotalStudents");
    const totalTeachersEl = document.getElementById("adminKpiTotalTeachers");
    const totalDeptsEl = document.getElementById("adminKpiTotalDepartments");
    const totalClassesEl = document.getElementById("adminKpiTotalClasses");

    if (totalStudentsEl) totalStudentsEl.textContent = stats.totalStudents;
    if (totalTeachersEl) totalTeachersEl.textContent = stats.totalTeachers;
    if (totalDeptsEl) totalDeptsEl.textContent = stats.totalDepartments;
    if (totalClassesEl) totalClassesEl.textContent = stats.totalClasses;

    // Presence Ribbon
    const presentEl = document.getElementById("adminKpiPresent");
    const absentEl = document.getElementById("adminKpiAbsent");
    const avgEl = document.getElementById("adminKpiAvg");
    const lowEl = document.getElementById("adminKpiLow");

    if (presentEl) presentEl.textContent = stats.presentToday;
    if (absentEl) absentEl.textContent = stats.absentToday;
    if (avgEl) avgEl.textContent = stats.avgAttendance + "%";
    if (lowEl) lowEl.textContent = stats.lowAttendanceCount + " Students";

    // Charts
    setTimeout(() => {
      if (window.attendxCharts) {
        window.attendxCharts.renderAttendanceTrend("trendChart");
        window.attendxCharts.renderStatusDoughnut("statusDoughnutChart");
        window.attendxCharts.renderClassComparison("classBarChart");
      }
    }, 50);

    // At-Risk Low Attendance List (<75%)
    const lowListEl = document.getElementById("adminLowAttendanceList");
    if (lowListEl) {
      if (stats.lowAttendanceStudents.length === 0) {
        lowListEl.innerHTML = `<div style="text-align:center; padding:24px; color:var(--text-muted);">All students currently exceed the 75% benchmark.</div>`;
      } else {
        lowListEl.innerHTML = stats.lowAttendanceStudents.map(student => `
          <div style="display:flex; align-items:center; justify-content:space-between; padding:12px 14px; background:rgba(6, 11, 28, 0.6); border-radius:var(--radius-sm); border:1px solid rgba(239, 68, 68, 0.2);">
            <div style="display:flex; align-items:center; gap:12px;">
              <img src="${student.avatar}" style="width:34px;height:34px;border-radius:50%;object-fit:cover;border:1px solid var(--coral);" />
              <div>
                <div style="font-weight:600;font-size:0.9rem;">${student.name}</div>
                <div style="font-size:0.75rem;color:var(--text-muted);font-family:var(--font-mono);">${student.rollNo} • Class: ${student.classId} (${student.department})</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
              <span class="badge badge-warning">${student.overallAttendance}% ATTENDANCE</span>
              <button class="btn btn-sm btn-danger" onclick="sendWarningNotice('${student.id}', '${student.name}')">
                <i data-lucide="send" style="width:14px;height:14px;"></i> Alert Parent
              </button>
            </div>
          </div>
        `).join("");
      }
    }

    if (window.lucide) window.lucide.createIcons();
  }

  window.sendWarningNotice = function(studentId, studentName) {
    const student = window.attendxStore.getStudentById(studentId);
    window.attendxStore.sendNotification({
      type: "warning",
      severity: "danger",
      title: "⚠️ Low Attendance Caution Dispatched",
      message: `Formal academic caution issued to ${studentName} and guardian (${student?.parentName || 'Parent'}) by Dr. Vidya Mohod Ma’am regarding attendance below 75%.`,
      studentId: studentId
    });
    showToast("Warning Notice Dispatched", `Official warning sent to ${studentName}'s guardians.`, "warning");
    renderAdminDashboard();
  };

  // =========================================================================
  // 8. ALL CAMPUS CLASSES VIEW (Requirement 6: Display ONLY CS & IT)
  // =========================================================================
  let selectedCampusClass = "CS";

  window.selectCampusClass = function(classId) {
    selectedCampusClass = classId;

    // Toggle card styles
    const csCard = document.getElementById("classCard-CS");
    const itCard = document.getElementById("classCard-IT");
    if (csCard) csCard.classList.toggle("active-class", classId === "CS");
    if (itCard) itCard.classList.toggle("active-class", classId === "IT");

    renderCampusClassesView();
  };

  function renderCampusClassesView() {
    const titleEl = document.getElementById("campusClassRosterTitle");
    const subEl = document.getElementById("campusClassRosterSub");
    const tbody = document.getElementById("campusClassRosterBody");
    if (!tbody) return;

    const students = window.attendxStore.getStudents(selectedCampusClass);

    if (titleEl) {
      titleEl.textContent = selectedCampusClass === "CS" 
        ? "Computer Science (CS) Student Roster" 
        : "Information Technology (IT) Student Roster";
    }
    if (subEl) {
      subEl.textContent = `${students.length} Enrolled Students • Department of ${selectedCampusClass === "CS" ? "Computer Science" : "Information Technology"}`;
    }

    tbody.innerHTML = students.map((s, idx) => {
      const isLow = s.overallAttendance < 75;
      return `
        <tr>
          <td><span style="font-family:var(--font-mono); color:var(--text-muted);">${idx + 1}</span></td>
          <td>
            <div class="student-row-pill">
              <img src="${s.avatar}" class="student-table-avatar" />
              <div>
                <div style="font-weight:600; color:var(--text-primary);">${s.name}</div>
                <div style="font-size:0.75rem; color:var(--text-muted);">${s.email}</div>
              </div>
            </div>
          </td>
          <td><span style="font-family:var(--font-mono); color:var(--cyan); font-weight:700;">${s.rollNo}</span></td>
          <td><span class="badge badge-cyan">${s.departmentCode}</span></td>
          <td>
            <span style="font-family:var(--font-mono); font-weight:700; color:${isLow ? 'var(--coral)' : 'var(--emerald)'};">
              ${s.overallAttendance}%
            </span>
          </td>
          <td>
            <div style="font-size:0.85rem; color:var(--text-primary); font-weight:600;">${s.parentName || 'Parent'}</div>
            <div style="font-size:0.75rem; color:var(--text-muted);">${s.parentPhone || ''}</div>
          </td>
          <td>
            <span class="badge ${isLow ? 'badge-warning' : 'badge-present'}">
              ${isLow ? 'RISK (<75%)' : 'REGULAR'}
            </span>
          </td>
        </tr>
      `;
    }).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  // =========================================================================
  // 9. TEACHERS DIRECTORY (Faculty Directory & Account Provisioning)
  // =========================================================================
  function renderTeachersDirectory() {
    const tbody = document.getElementById("teachersTableBody");
    if (!tbody) return;

    const teachers = window.attendxStore.getTeachers();

    tbody.innerHTML = teachers.map(t => {
      const acc = window.attendxStore.getAccountByProfileId ? window.attendxStore.getAccountByProfileId(t.id) : null;
      const hasAccount = !!acc;
      const accountBadge = hasAccount ? `
        <span class="badge badge-success" style="font-size:0.7rem; padding:2px 8px; display:inline-flex; align-items:center; gap:4px;" title="Active Portal Login Account">
          <i data-lucide="shield-check" style="width:11px;height:11px;"></i> Active Account
        </span>
      ` : `
        <span class="badge" style="background:rgba(234,179,8,0.15); color:var(--amber); border:1px solid rgba(234,179,8,0.3); font-size:0.7rem; padding:2px 8px; display:inline-flex; align-items:center; gap:4px;" title="No Portal Account Provisioned">
          <i data-lucide="shield-alert" style="width:11px;height:11px;"></i> No Login Account
        </span>
      `;

      return `
        <tr>
          <td>
            <div class="student-row-pill">
              <img src="${t.avatar}" class="student-table-avatar" style="border-color:var(--violet);" />
              <div>
                <div style="font-weight:700; color:#FFFFFF;">${t.name}</div>
                <div style="font-size:0.75rem; color:var(--violet); font-weight:600;">${t.title}</div>
              </div>
            </div>
          </td>
          <td><span style="font-size:0.85rem; color:var(--text-muted);">${t.email}</span></td>
          <td><span class="badge badge-cyan">${t.department}</span></td>
          <td><span class="badge" style="background:rgba(139,92,246,0.2); color:var(--violet); border:1px solid var(--violet); font-weight:700;">${t.assignedClass} Class</span></td>
          <td><span style="font-size:0.85rem; color:var(--text-primary);">${t.subjectSpecialty || 'Core Engineering'}</span></td>
          <td>
            <div style="display:flex; flex-direction:column; gap:4px;">
              <span style="font-size:0.8rem; color:var(--text-muted);">Head: Dr. Vidya Mohod</span>
              ${accountBadge}
            </div>
          </td>
          <td>
            <div style="display:flex; gap:6px;">
              <button class="btn btn-sm btn-ghost" onclick="openProvisionAccountModal('${t.id}')" title="${hasAccount ? 'Manage / Reset Portal Password' : 'Create & Provision Portal Login Account'}">
                <i data-lucide="key" style="width:14px;height:14px; color:${hasAccount ? 'var(--cyan)' : 'var(--amber)'};"></i>
              </button>
              <button class="btn btn-sm btn-ghost" onclick="openEditTeacherModal('${t.id}')" title="Edit Faculty Profile">
                <i data-lucide="edit" style="width:14px;height:14px;"></i>
              </button>
              <button class="btn btn-sm btn-ghost" onclick="promptClassReassignment('${t.id}', '${t.name}', '${t.assignedClass}')" title="Reassign Class">
                <i data-lucide="refresh-cw" style="width:14px;height:14px;"></i>
              </button>
              <button class="btn btn-sm btn-cyan" onclick="switchTeacherView('${t.id}')" title="Launch Teacher Attendance">
                <i data-lucide="arrow-right" style="width:14px;height:14px;"></i> Open
              </button>
              <button class="btn btn-sm btn-danger" onclick="deleteTeacherRecord('${t.id}')" title="Delete Faculty">
                <i data-lucide="trash-2" style="width:14px;height:14px;"></i>
              </button>
            </div>
          </td>
        </tr>
      `;
    }).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  // Administrator Account Provisioning Modal Handlers
  window.openProvisionAccountModal = function(teacherId) {
    const t = window.attendxStore.getTeacherById(teacherId);
    if (!t) return;
    const modal = document.getElementById("provisionAccountModal");
    const acc = window.attendxStore.getAccountByProfileId ? window.attendxStore.getAccountByProfileId(teacherId) : null;

    document.getElementById("provisionTeacherId").value = t.id;
    document.getElementById("provisionTeacherName").textContent = `Prof. ${t.name}`;
    document.getElementById("provisionTeacherEmail").textContent = t.email;
    document.getElementById("provisionTeacherMeta").textContent = `${t.department} • ${t.title || 'Faculty'} (${t.assignedClass} Class)`;
    document.getElementById("provisionTeacherAvatar").src = t.avatar || "assets/avatar_teacher.jpg";
    document.getElementById("provisionTeacherEmailDisplay").value = t.email;

    const passInput = document.getElementById("provisionPassword");
    if (passInput) {
      passInput.value = "";
      passInput.type = "password";
    }

    const statusSelect = document.getElementById("provisionStatus");
    if (statusSelect) statusSelect.value = acc ? (acc.status || "active") : "active";

    const badgeContainer = document.getElementById("provisionCurrentStatusBadge");
    const btnRevoke = document.getElementById("btnRevokeAccount");

    if (acc) {
      if (badgeContainer) {
        badgeContainer.innerHTML = `<span class="badge badge-success" style="font-size:0.75rem;"><i data-lucide="shield-check" style="width:12px;height:12px;"></i> Active Portal Account</span>`;
      }
      if (btnRevoke) btnRevoke.style.display = "inline-flex";
    } else {
      if (badgeContainer) {
        badgeContainer.innerHTML = `<span class="badge" style="background:rgba(234,179,8,0.15); color:var(--amber); border:1px solid rgba(234,179,8,0.3); font-size:0.75rem;"><i data-lucide="shield-alert" style="width:12px;height:12px;"></i> No Account Registered</span>`;
      }
      if (btnRevoke) btnRevoke.style.display = "none";
    }

    if (modal) modal.classList.add("active");
    if (window.lucide) window.lucide.createIcons();
  };

  window.closeProvisionAccountModal = function() {
    const modal = document.getElementById("provisionAccountModal");
    if (modal) modal.classList.remove("active");
  };

  window.handleRevokeTeacherAccount = function() {
    const teacherId = document.getElementById("provisionTeacherId").value;
    const t = window.attendxStore.getTeacherById(teacherId);
    const teacherName = t ? t.name : "this faculty member";
    if (confirm(`Revoke portal login access for Prof. ${teacherName}? The faculty profile will remain in the directory, but they will not be able to log in.`)) {
      if (window.attendxStore.revokeTeacherAccount) {
        window.attendxStore.revokeTeacherAccount(teacherId);
      }
      showToast("Access Revoked", `Portal login access revoked for Prof. ${teacherName}.`, "danger");
      closeProvisionAccountModal();
      renderTeachersDirectory();
    }
  };

  const provisionAccountForm = document.getElementById("provisionAccountForm");
  if (provisionAccountForm) {
    provisionAccountForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const teacherId = document.getElementById("provisionTeacherId").value;
      const passInput = document.getElementById("provisionPassword");
      const password = passInput ? passInput.value : "";
      const statusSelect = document.getElementById("provisionStatus");
      const status = statusSelect ? statusSelect.value : "active";

      if (!password || password.trim().length === 0) {
        showToast("Validation Error", "Please provide a password for the faculty portal account.", "danger");
        return;
      }

      try {
        window.attendxStore.provisionTeacherAccount(teacherId, password.trim(), status);
        const t = window.attendxStore.getTeacherById(teacherId);
        showToast("Account Provisioned", `Portal access successfully provisioned for Prof. ${t ? t.name : ""}.`, "success");
        closeProvisionAccountModal();
        renderTeachersDirectory();
      } catch (err) {
        showToast("Error", err.message || "Failed to provision account.", "danger");
      }
    });
  }

  const btnToggleProvisionPass = document.getElementById("btnToggleProvisionPassword");
  if (btnToggleProvisionPass) {
    btnToggleProvisionPass.addEventListener("click", () => {
      const passInput = document.getElementById("provisionPassword");
      const passIcon = document.getElementById("toggleProvisionPassIcon");
      if (!passInput) return;
      const isPass = passInput.type === "password";
      passInput.type = isPass ? "text" : "password";
      if (passIcon) {
        passIcon.setAttribute("data-lucide", isPass ? "eye-off" : "eye");
        if (window.lucide) window.lucide.createIcons();
      }
    });
  }

  window.openAddTeacherModal = function() {
    const modal = document.getElementById("teacherFormModal");
    document.getElementById("teacherModalTitle").textContent = "Register New Faculty Member";
    document.getElementById("teacherFormId").value = "";
    document.getElementById("teacherFormName").value = "";
    document.getElementById("teacherFormEmail").value = "";
    document.getElementById("teacherFormTitle").value = "Assistant Professor";
    document.getElementById("teacherFormClass").value = "CS";
    document.getElementById("teacherFormSpecialty").value = "";
    const passField = document.getElementById("teacherFormPassword");
    if (passField) passField.value = "";
    const badge = document.getElementById("teacherFormAccountBadge");
    if (badge) {
      badge.className = "badge";
      badge.style.background = "rgba(234,179,8,0.15)";
      badge.style.color = "var(--amber)";
      badge.style.border = "1px solid rgba(234,179,8,0.3)";
      badge.textContent = "No Login Account";
    }
    if (modal) modal.classList.add("active");
  };

  window.openEditTeacherModal = function(id) {
    const t = window.attendxStore.getTeacherById(id);
    if (!t) return;
    const modal = document.getElementById("teacherFormModal");
    const acc = window.attendxStore.getAccountByProfileId ? window.attendxStore.getAccountByProfileId(id) : null;
    document.getElementById("teacherModalTitle").textContent = `Edit Faculty: ${t.name}`;
    document.getElementById("teacherFormId").value = t.id;
    document.getElementById("teacherFormName").value = t.name;
    document.getElementById("teacherFormEmail").value = t.email || "";
    document.getElementById("teacherFormTitle").value = t.title || "Assistant Professor";
    document.getElementById("teacherFormClass").value = t.assignedClass || "CS";
    document.getElementById("teacherFormSpecialty").value = t.subjectSpecialty || "";
    const passField = document.getElementById("teacherFormPassword");
    if (passField) passField.value = "";
    const badge = document.getElementById("teacherFormAccountBadge");
    if (badge) {
      if (acc) {
        badge.className = "badge badge-success";
        badge.style.background = "";
        badge.style.color = "";
        badge.style.border = "";
        badge.textContent = "Active Portal Account";
      } else {
        badge.className = "badge";
        badge.style.background = "rgba(234,179,8,0.15)";
        badge.style.color = "var(--amber)";
        badge.style.border = "1px solid rgba(234,179,8,0.3)";
        badge.textContent = "No Login Account";
      }
    }
    if (modal) modal.classList.add("active");
  };

  window.closeTeacherModal = function() {
    const modal = document.getElementById("teacherFormModal");
    if (modal) modal.classList.remove("active");
  };

  const teacherForm = document.getElementById("teacherForm");
  if (teacherForm) {
    teacherForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const id = document.getElementById("teacherFormId").value;
      const data = {
        name: document.getElementById("teacherFormName").value.trim(),
        email: document.getElementById("teacherFormEmail").value.trim(),
        assignedClass: document.getElementById("teacherFormClass").value,
        title: document.getElementById("teacherFormTitle").value.trim(),
        subjectSpecialty: document.getElementById("teacherFormSpecialty").value.trim()
      };
      const enteredPassword = document.getElementById("teacherFormPassword")?.value?.trim();

      if (id) {
        window.attendxStore.updateTeacher(id, data);
        if (enteredPassword && window.attendxStore.provisionTeacherAccount) {
          window.attendxStore.provisionTeacherAccount(id, enteredPassword);
          showToast("Faculty & Account Updated", `Record and login credentials for ${data.name} saved.`, "success");
        } else {
          showToast("Faculty Updated", `Record for ${data.name} saved.`, "success");
        }
      } else {
        const newTeacher = window.attendxStore.addTeacher(data);
        if (enteredPassword && newTeacher && window.attendxStore.provisionTeacherAccount) {
          window.attendxStore.provisionTeacherAccount(newTeacher.id, enteredPassword);
          showToast("Faculty & Account Registered", `${data.name} registered with active portal account.`, "success");
        } else {
          showToast("Faculty Registered", `${data.name} assigned to Class ${data.assignedClass} (directory record only).`, "success");
        }
      }

      closeTeacherModal();
      renderTeachersDirectory();
      renderAdminDashboard();
      initTeacherDashboard();
    });
  }

  window.deleteTeacherRecord = function(id) {
    if (confirm("Are you certain you wish to delete this faculty record?")) {
      window.attendxStore.deleteTeacher(id);
      showToast("Faculty Removed", "Teacher was removed from the faculty directory.", "danger");
      renderTeachersDirectory();
      renderAdminDashboard();
      initTeacherDashboard();
    }
  };

  window.promptClassReassignment = function(teacherId, teacherName, currentClass) {
    const targetClass = currentClass === "CS" ? "IT" : "CS";
    if (confirm(`Reassign Professor ${teacherName} from ${currentClass} to ${targetClass}?`)) {
      window.attendxStore.assignTeacherClass(teacherId, targetClass);
      showToast("Class Reassigned", `${teacherName} is now assigned to ${targetClass}.`, "success");
      renderTeachersDirectory();
    }
  };

  window.switchTeacherView = function(teacherId) {
    const teacher = window.attendxStore.getTeacherById(teacherId);
    if (teacher) {
      currentTeacherState.teacherName = teacher.name;
      currentTeacherState.classId = teacher.assignedClass;
      switchView("teacher-dashboard");
    }
  };

  // =========================================================================
  // 10. TEACHER ATTENDANCE SUITE (Requirement 10: CS & IT Attendance)
  // =========================================================================
  let currentTeacherState = {
    teacherName: "Swapnali Jadhav",
    classId: "CS",
    subjectId: "SUB-CS301",
    date: "2026-10-02",
    rosterRecords: {} // studentId -> 'present' | 'absent' | 'late'
  };

  function initTeacherDashboard() {
    const currentUser = window.attendxStore.getCurrentUser();
    if (currentUser && currentUser.role === "teacher") {
      currentTeacherState.teacherName = currentUser.name;
      if (currentUser.assignedClass) currentTeacherState.classId = currentUser.assignedClass;
    }

    const teacherActiveSelect = document.getElementById("teacherActiveSelect");
    const classSelect = document.getElementById("teacherClassSelect");
    const subjectSelect = document.getElementById("teacherSubjectSelect");
    const dateInput = document.getElementById("teacherDateInput");
    const instructorDisplay = document.getElementById("teacherInstructorName");

    // 1. Populate Teacher selector with all teachers
    if (teacherActiveSelect) {
      const teachers = window.attendxStore.getTeachers();
      teacherActiveSelect.innerHTML = teachers.map(t => `<option value="${t.name}">${t.name} (${t.assignedClass})</option>`).join("");
      teacherActiveSelect.value = currentTeacherState.teacherName;

      teacherActiveSelect.onchange = () => {
        const selectedT = teachers.find(t => t.name === teacherActiveSelect.value);
        if (selectedT) {
          currentTeacherState.teacherName = selectedT.name;
          currentTeacherState.classId = selectedT.assignedClass;
          if (classSelect) classSelect.value = selectedT.assignedClass;
          if (instructorDisplay) instructorDisplay.textContent = selectedT.name;
          populateSubjectDropdown();
          loadTeacherRoster();
        }
      };
    }

    if (instructorDisplay) {
      instructorDisplay.textContent = currentTeacherState.teacherName;
    }

    // 2. Populate Class selector (CS and IT only)
    if (classSelect) {
      const classes = window.attendxStore.getClasses();
      classSelect.innerHTML = classes.map(c => `<option value="${c.id}">${c.name}</option>`).join("");
      classSelect.value = currentTeacherState.classId;

      classSelect.onchange = () => {
        currentTeacherState.classId = classSelect.value;
        populateSubjectDropdown();
        loadTeacherRoster();
      };
    }

    // 3. Date
    if (dateInput) {
      dateInput.value = currentTeacherState.date;
      dateInput.onchange = () => {
        currentTeacherState.date = dateInput.value;
        loadTeacherRoster();
      };
    }

    populateSubjectDropdown();
    loadTeacherRoster();
    renderAttendanceHistory();
  }

  function populateSubjectDropdown() {
    const subjectSelect = document.getElementById("teacherSubjectSelect");
    if (!subjectSelect) return;
    const subjects = window.attendxStore.getSubjects(currentTeacherState.classId);
    subjectSelect.innerHTML = subjects.map(s => `<option value="${s.id}">${s.code} - ${s.name}</option>`).join("");
    if (subjects.length > 0) {
      currentTeacherState.subjectId = subjects[0].id;
      subjectSelect.value = subjects[0].id;
    }
    subjectSelect.onchange = () => {
      currentTeacherState.subjectId = subjectSelect.value;
      loadTeacherRoster();
    };
  }

  function loadTeacherRoster() {
    const students = window.attendxStore.getStudents(currentTeacherState.classId);
    const existing = window.attendxStore.getAttendanceForSession(
      currentTeacherState.classId,
      currentTeacherState.subjectId,
      currentTeacherState.date
    );

    currentTeacherState.rosterRecords = {};

    students.forEach(s => {
      if (existing && existing.records && existing.records[s.id]) {
        currentTeacherState.rosterRecords[s.id] = existing.records[s.id];
      } else {
        // Defaults: if student is low attendance (<75%), preset absent for demo; otherwise present
        currentTeacherState.rosterRecords[s.id] = s.overallAttendance < 75 ? "absent" : "present";
      }
    });

    renderRosterDOM();
    updateRosterTally();
  }

  function renderRosterDOM() {
    const container = document.getElementById("teacherRosterContainer");
    if (!container) return;

    const students = window.attendxStore.getStudents(currentTeacherState.classId);

    if (students.length === 0) {
      container.innerHTML = `<tr><td colspan="5" style="text-align:center; padding:30px; color:var(--text-muted);">No enrolled students in this class section.</td></tr>`;
      return;
    }

    container.innerHTML = students.map((s, idx) => {
      const status = currentTeacherState.rosterRecords[s.id] || "present";
      return `
        <tr>
          <td><span style="font-family:var(--font-mono); color:var(--text-muted);">${idx + 1}</span></td>
          <td>
            <div class="student-row-pill">
              <img src="${s.avatar}" class="student-table-avatar" />
              <div>
                <div style="font-weight:600; color:var(--text-primary);">${s.name}</div>
                <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${s.rollNo} • Parent: ${s.parentName || 'Rajaram Chavan'}</div>
              </div>
            </div>
          </td>
          <td>
            <span style="font-family:var(--font-mono); font-weight:600; color:${s.overallAttendance < 75 ? 'var(--coral)' : 'var(--cyan)'};">
              ${s.overallAttendance}%
            </span>
          </td>
          <td>
            <div class="btn-status-group" data-student-id="${s.id}">
              <button type="button" class="btn-status ${status === 'present' ? 'active-present' : ''}" onclick="setStudentStatus('${s.id}', 'present')">
                <i data-lucide="check" style="width:14px;height:14px;"></i> Present
              </button>
              <button type="button" class="btn-status ${status === 'absent' ? 'active-absent' : ''}" onclick="setStudentStatus('${s.id}', 'absent')">
                <i data-lucide="x" style="width:14px;height:14px;"></i> Absent
              </button>
              <button type="button" class="btn-status ${status === 'late' ? 'active-late' : ''}" onclick="setStudentStatus('${s.id}', 'late')">
                <i data-lucide="clock" style="width:14px;height:14px;"></i> Late
              </button>
            </div>
          </td>
          <td>
            <span id="badge-status-${s.id}" class="badge badge-${status}">
              ${status.toUpperCase()}
            </span>
          </td>
        </tr>
      `;
    }).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  window.setStudentStatus = function(studentId, status) {
    currentTeacherState.rosterRecords[studentId] = status;

    const group = document.querySelector(`.btn-status-group[data-student-id="${studentId}"]`);
    if (group) {
      group.querySelectorAll(".btn-status").forEach(btn => {
        btn.classList.remove("active-present", "active-absent", "active-late");
      });
      const activeBtn = group.querySelector(`.btn-status:nth-child(${status === 'present' ? 1 : status === 'absent' ? 2 : 3})`);
      if (activeBtn) activeBtn.classList.add(`active-${status}`);
    }

    const badge = document.getElementById(`badge-status-${studentId}`);
    if (badge) {
      badge.className = `badge badge-${status}`;
      badge.textContent = status.toUpperCase();
    }

    updateRosterTally();
  };

  function updateRosterTally() {
    let presentCount = 0;
    let absentCount = 0;
    let lateCount = 0;

    Object.values(currentTeacherState.rosterRecords).forEach(st => {
      if (st === "present") presentCount++;
      else if (st === "absent") absentCount++;
      else if (st === "late") lateCount++;
    });

    const pEl = document.getElementById("tallyPresent");
    const aEl = document.getElementById("tallyAbsent");
    const lEl = document.getElementById("tallyLate");
    const totEl = document.getElementById("tallyTotal");

    if (pEl) pEl.textContent = presentCount;
    if (aEl) aEl.textContent = absentCount;
    if (lEl) lEl.textContent = lateCount;
    if (totEl) totEl.textContent = presentCount + absentCount + lateCount;
  }

  window.teacherMarkAllPresent = function() {
    const students = window.attendxStore.getStudents(currentTeacherState.classId);
    students.forEach(s => {
      currentTeacherState.rosterRecords[s.id] = "present";
    });
    renderRosterDOM();
    updateRosterTally();
    showToast("Updated", "All students marked Present.", "info");
  };

  window.teacherSaveAttendance = function() {
    window.attendxStore.saveAttendance(
      currentTeacherState.classId,
      currentTeacherState.subjectId,
      currentTeacherState.date,
      currentTeacherState.rosterRecords,
      currentTeacherState.teacherName
    );

    showToast("Attendance Saved", `Attendance logged for Class ${currentTeacherState.classId} by Prof. ${currentTeacherState.teacherName}.`, "success");
    renderAttendanceHistory();
  };

  window.teacherNotifyParents = function() {
    teacherSaveAttendance();

    const count = window.attendxStore.notifyParentsForSession(
      currentTeacherState.classId,
      currentTeacherState.subjectId,
      currentTeacherState.date,
      currentTeacherState.rosterRecords
    );

    showToast("Parents Notified", `Dispatched automated real-time alerts to ${count} guardians.`, "success");
    playCyberTone("alert");
  };

  function renderAttendanceHistory() {
    const historyList = document.getElementById("teacherAttendanceHistoryList");
    if (!historyList) return;

    const records = window.attendxStore.getAttendanceRecords({ classId: currentTeacherState.classId });
    if (records.length === 0) {
      historyList.innerHTML = `<div style="text-align:center; padding:20px; color:var(--text-muted);">No archived sessions logged yet.</div>`;
      return;
    }

    historyList.innerHTML = records.slice(0, 5).map(r => {
      const recs = r.records || {};
      const pres = Object.values(recs).filter(s => s === "present").length;
      const abs = Object.values(recs).filter(s => s === "absent").length;
      return `
        <div style="display:flex; justify-content:space-between; align-items:center; padding:12px 14px; background:rgba(6, 11, 28, 0.6); border-radius:var(--radius-sm); border:1px solid var(--border-glass-subtle); margin-bottom:8px;">
          <div>
            <div style="font-weight:600; font-size:0.9rem;">${r.subjectName || "Lecture Session"} (${r.classId})</div>
            <div style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${r.date} • Logged by ${r.markedBy}</div>
          </div>
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge badge-present">${pres} Present</span>
            <span class="badge badge-absent">${abs} Absent</span>
          </div>
        </div>
      `;
    }).join("");
  }

  // =========================================================================
  // 11. PARENT PORTAL & MONTHLY CALENDAR (Requirements 3, 7, 8, 9)
  // =========================================================================
  function renderParentDashboard() {
    const currentUser = window.attendxStore.getCurrentUser();
    const studentId = currentUser?.studentId || currentUser?.childId || "STD-CS01";
    const stats = window.attendxStore.getStudentStats(studentId, 2026, 9); // October 2026
    const student = stats.student;

    const childNameEl = document.getElementById("parentChildName");
    const parentGuardianEl = document.getElementById("parentGuardianName");
    const childRollEl = document.getElementById("parentChildRoll");
    const childDeptEl = document.getElementById("parentChildDept");
    const childClassEl = document.getElementById("parentChildClass");
    const childAvatarEl = document.getElementById("parentChildAvatar");
    const radialPctEl = document.getElementById("parentRadialPct");
    const radialCircle = document.getElementById("parentRadialCircle");

    if (childNameEl) childNameEl.textContent = student.name;
    if (parentGuardianEl) parentGuardianEl.textContent = currentUser?.name || stats.parentName || student.parentName || "Rajaram Chavan";
    if (childRollEl) childRollEl.textContent = "Roll No: " + student.rollNo;
    if (childDeptEl) childDeptEl.textContent = "Dept: " + student.department;
    if (childClassEl) childClassEl.textContent = "Class: " + student.classId;
    if (childAvatarEl) childAvatarEl.src = student.avatar;

    if (radialPctEl) radialPctEl.textContent = student.overallAttendance + "%";
    if (radialCircle) {
      const offset = 440 - (440 * (student.overallAttendance / 100));
      radialCircle.style.strokeDashoffset = offset;
    }

    // Monthly Calendar with Blue Holidays & Sundays
    renderParentCalendar(stats.calendarDays);

    // Alerts Feed & Chat
    renderParentNotifications(studentId);
    renderParentMessages(studentId);
  }

  function renderParentCalendar(calendarDays) {
    const grid = document.getElementById("parentCalendarGrid");
    if (!grid) return;

    grid.innerHTML = calendarDays.map(d => {
      if (d.isPad) {
        return `<div class="calendar-day-cell day-empty"></div>`;
      }

      // Build CSS class list
      let cellClasses = `calendar-day-cell day-${d.status}`;
      if (d.isSunday) cellClasses += " day-sunday";
      if (d.isHoliday) cellClasses += " day-holiday";
      if (d.isEvent) cellClasses += " day-event";
      if (d.isToday) cellClasses += " day-today";

      return `
        <div class="${cellClasses}" onclick="inspectDayDetails(${d.day}, '${d.status}', '${d.date}')" title="${d.holidayName || d.statusLabel}">
          <span class="day-number">${d.day}</span>
          <div class="day-indicator"></div>
        </div>
      `;
    }).join("");
  }

  window.inspectDayDetails = function(day, status, date) {
    const modal = document.getElementById("dayDetailsModal");
    const titleEl = document.getElementById("dayDetailsTitle");
    const bodyEl = document.getElementById("dayDetailsBody");
    const currentUser = window.attendxStore.getCurrentUser();
    const studentId = currentUser?.studentId || currentUser?.childId || "STD-CS01";
    const stats = window.attendxStore.getStudentStats(studentId, 2026, 9);
    const dayObj = stats.calendarDays.find(d => d.day === day && !d.isPad) || {
      date,
      statusLabel: status.toUpperCase(),
      description: "Class session",
      sessions: []
    };

    if (titleEl) titleEl.textContent = `Attendance Log: ${date}`;
    if (bodyEl) {
      let badgeHtml = "";
      if (dayObj.isSunday) {
        badgeHtml = `<span class="badge" style="background:#0284C7; color:#FFFFFF; font-size:0.95rem; padding:6px 14px;">🔵 Sunday Holiday</span>`;
      } else if (dayObj.isHoliday) {
        badgeHtml = `<span class="badge" style="background:#0284C7; color:#FFFFFF; font-size:0.95rem; padding:6px 14px;">🔵 Official Holiday: ${dayObj.holidayName}</span>`;
      } else if (dayObj.isEvent) {
        badgeHtml = `<span class="badge badge-warning" style="font-size:0.95rem; padding:6px 14px;">🟡 Event: ${dayObj.holidayName}</span>`;
      } else if (status === "present") {
        badgeHtml = `<span class="badge badge-present" style="font-size:0.95rem; padding:6px 14px;">🟢 Present All Sessions</span>`;
      } else if (status === "absent") {
        badgeHtml = `<span class="badge badge-absent" style="font-size:0.95rem; padding:6px 14px;">🔴 Marked Absent</span>`;
      } else if (status === "late") {
        badgeHtml = `<span class="badge badge-late" style="font-size:0.95rem; padding:6px 14px;">🟡 Late Arrival</span>`;
      } else {
        badgeHtml = `<span class="badge" style="background:#64748B; color:#FFFFFF; font-size:0.95rem; padding:6px 14px;">⚪ No Attendance / Future Date</span>`;
      }

      bodyEl.innerHTML = `
        <div style="text-align:center; padding:12px 0 20px;">
          ${badgeHtml}
          <p style="color:var(--text-secondary); font-size:0.88rem; margin-top:10px;">${dayObj.description}</p>
        </div>

        <div style="display:flex; flex-direction:column; gap:12px;">
          ${dayObj.isHoliday ? `
            <div style="padding:16px; background:rgba(14,165,233,0.12); border-radius:var(--radius-sm); border:1px solid rgba(56,189,248,0.4); text-align:center;">
              <i data-lucide="calendar" style="width:28px;height:28px;color:#38BDF8;margin-bottom:6px;"></i>
              <div style="font-weight:700; color:#38BDF8;">Campus Closed • Holiday</div>
              <div style="font-size:0.8rem; color:var(--text-secondary); margin-top:4px;">No academic lectures scheduled on this date.</div>
            </div>
          ` : dayObj.sessions && dayObj.sessions.length > 0 ? dayObj.sessions.map(s => `
            <div style="padding:14px; background:rgba(6,11,28,0.7); border-radius:var(--radius-sm); border:1px solid var(--border-glass-subtle);">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-weight:700; color:var(--text-primary); font-size:0.95rem;">${s.subject}</div>
                <span class="badge badge-${s.status === 'present' ? 'present' : (s.status === 'absent' ? 'absent' : 'late')}">${s.status.toUpperCase()}</span>
              </div>
              <div style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Time: ${s.time} • Instructor: ${s.teacher}</div>
            </div>
          `).join("") : `
            <div style="text-align:center; color:var(--text-muted); padding:20px;">No specific session logs recorded for this date.</div>
          `}
        </div>

        <div style="margin-top:20px; padding-top:14px; border-top:1px solid var(--border-glass-subtle); display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; color:var(--text-muted);">
          <span>Student: <strong>${stats.student.name}</strong> (${stats.student.rollNo})</span>
          <span>Guardian: <strong>${stats.student.parentName || stats.parentName || 'Guardian'}</strong></span>
        </div>
      `;
    }

    if (modal) modal.classList.add("active");
    if (window.lucide) window.lucide.createIcons();
  };

  function renderParentNotifications(studentId = null) {
    const list = document.getElementById("parentAlertsList");
    if (!list) return;

    const currentUser = window.attendxStore.getCurrentUser();
    const targetStudentId = studentId || currentUser?.studentId || currentUser?.childId || "STD-CS01";
    const notifs = window.attendxStore.getNotifications("parent", targetStudentId);
    if (notifs.length === 0) {
      const student = window.attendxStore.getStudentById(targetStudentId);
      list.innerHTML = `<div style="text-align:center; padding:20px; color:var(--text-muted);">No active absence notices for ${student?.name || 'this student'}.</div>`;
      return;
    }

    list.innerHTML = notifs.map(n => `
      <div class="notif-card ${n.severity}">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div style="font-weight:700; color:var(--text-primary); font-size:0.92rem;">${n.title}</div>
          <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${n.date}</span>
        </div>
        <div style="font-size:0.85rem; color:var(--text-secondary); margin-top:6px; line-height:1.5;">${n.message}</div>
        <div style="margin-top:10px; display:flex; justify-content:flex-end;">
          <button class="btn btn-sm btn-ghost" onclick="acknowledgeAlert('${n.id}')">
            <i data-lucide="check" style="width:14px;height:14px;"></i> Acknowledge
          </button>
        </div>
      </div>
    `).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  window.acknowledgeAlert = function(id) {
    window.attendxStore.markNotificationRead(id);
    showToast("Acknowledged", "Receipt of attendance alert confirmed.", "info");
    const currentUser = window.attendxStore.getCurrentUser();
    renderParentNotifications(currentUser?.studentId || currentUser?.childId);
  };

  function renderParentMessages(studentId = null) {
    const container = document.getElementById("parentChatContainer");
    if (!container) return;

    const currentUser = window.attendxStore.getCurrentUser();
    const targetStudentId = studentId || currentUser?.studentId || currentUser?.childId || "STD-CS01";
    const messages = window.attendxStore.getMessages(targetStudentId);
    container.innerHTML = messages.map(m => `
      <div style="display:flex; flex-direction:column; align-items:${m.isSelf ? 'flex-end' : 'flex-start'}; margin-bottom:12px;">
        <div style="font-size:0.75rem; color:var(--text-muted); margin-bottom:3px;">${m.from} • ${m.time}</div>
        <div style="max-width:80%; padding:10px 14px; border-radius:14px; background:${m.isSelf ? 'linear-gradient(135deg, var(--cyan), #0284C7)' : 'rgba(255,255,255,0.08)'}; color:${m.isSelf ? '#030712' : '#FFFFFF'}; font-weight:${m.isSelf ? '600' : '400'}; font-size:0.88rem; box-shadow:0 4px 12px rgba(0,0,0,0.2);">
          ${m.text}
        </div>
      </div>
    `).join("");

    container.scrollTop = container.scrollHeight;
  }

  window.sendParentMessage = function() {
    const input = document.getElementById("parentChatInput");
    if (!input || !input.value.trim()) return;

    const text = input.value.trim();
    input.value = "";

    const currentUser = window.attendxStore.getCurrentUser();
    const targetStudentId = currentUser?.studentId || currentUser?.childId || "STD-CS01";
    const parentName = currentUser?.name ? `${currentUser.name} (Parent)` : "Parent";

    window.attendxStore.sendMessage({
      from: parentName,
      fromRole: "parent",
      to: "Swapnali Jadhav",
      studentId: targetStudentId,
      text,
      isSelf: true
    });

    renderParentMessages(targetStudentId);
    showToast("Message Sent", "Direct inquiry dispatched to faculty instructor.", "info");
  };

  // =========================================================================
  // 12. STUDENT DASHBOARD (Dynamic for any logged in student)
  // =========================================================================
  function renderStudentDashboard() {
    const currentUser = window.attendxStore.getCurrentUser();
    const studentId = currentUser?.studentId || currentUser?.id || "STD-CS01";
    const stats = window.attendxStore.getStudentStats(studentId);
    const student = stats.student;

    const nameEl = document.getElementById("studentGreetingName");
    const streakEl = document.getElementById("studentStreakValue");
    const overallEl = document.getElementById("studentOverallPct");
    const attendedEl = document.getElementById("studentAttendedLectures");
    const missedEl = document.getElementById("studentMissedLectures");
    const warningBanner = document.getElementById("studentWarningBanner");

    if (nameEl) nameEl.textContent = student.name;
    if (streakEl) streakEl.textContent = `🔥 ${student.streak || 1} Days Streak`;
    if (overallEl) overallEl.textContent = student.overallAttendance + "%";
    if (attendedEl) attendedEl.textContent = stats.attendedLectures;
    if (missedEl) missedEl.textContent = stats.missedLectures;

    if (warningBanner) {
      warningBanner.style.display = student.overallAttendance < 75 ? "flex" : "none";
    }

    const subjectListEl = document.getElementById("studentSubjectList");
    if (subjectListEl && student.subjects) {
      subjectListEl.innerHTML = student.subjects.map(sub => {
        const isLow = sub.attendance < 75;
        return `
          <div style="padding:16px 20px; background:rgba(6, 11, 28, 0.6); border-radius:var(--radius-md); border:1px solid ${isLow ? 'var(--coral)' : 'var(--border-glass-subtle)'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
              <div>
                <span style="font-weight:700; color:var(--text-primary); font-size:0.95rem;">${sub.name}</span>
                <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono); margin-left:8px;">${sub.code} • ${sub.teacher || 'Faculty'}</span>
              </div>
              <div style="display:flex; align-items:center; gap:10px;">
                <span style="font-size:0.8rem; color:var(--text-secondary);">${sub.attended} / ${sub.total} sessions</span>
                <span class="badge ${isLow ? 'badge-warning' : 'badge-present'}">${sub.attendance}%</span>
              </div>
            </div>
            <div class="progress-bar-container">
              <div class="progress-bar-fill ${isLow ? 'warning' : ''}" style="width: ${sub.attendance}%;"></div>
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // =========================================================================
  // 13. STUDENT ROSTER TABLE & SEARCH/FILTER (Requirements 4, 5, 12, 13)
  // =========================================================================
  function renderStudentTable() {
    const classFilter = document.getElementById("studentClassFilter")?.value || "ALL";
    const searchQuery = document.getElementById("studentSearchInput")?.value || "";
    const tbody = document.getElementById("studentsTableBody");
    if (!tbody) return;

    const list = window.attendxStore.getStudents(classFilter, searchQuery);

    if (list.length === 0) {
      tbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding:32px; color:var(--text-muted);">No student records found matching search criteria.</td></tr>`;
      return;
    }

    const currentUser = window.attendxStore.getCurrentUser();
    const role = currentUser ? currentUser.role : "admin";
    const canView = true;
    const canEdit = (role === "admin" || role === "teacher");
    const canDelete = (role === "admin");

    tbody.innerHTML = list.map(s => {
      const isLow = s.overallAttendance < 75;

      const viewBtn = canView ? `
        <button class="action-btn action-btn-view" onclick="inspectStudentProfile('${s.id}')" aria-label="View" data-tooltip="View" title="View">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-eye"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg>
        </button>
      ` : "";

      const editBtn = canEdit ? `
        <button class="action-btn action-btn-edit" onclick="openEditStudentModal('${s.id}')" aria-label="Edit" data-tooltip="Edit" title="Edit">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pencil"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg>
        </button>
      ` : "";

      const deleteBtn = canDelete ? `
        <button class="action-btn action-btn-delete" onclick="deleteStudentRecord('${s.id}')" aria-label="Delete" data-tooltip="Delete" title="Delete">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-trash-2"><path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/></svg>
        </button>
      ` : "";

      return `
        <tr>
          <td><span style="font-family:var(--font-mono); font-size:0.85rem; color:var(--cyan);">${s.id}</span></td>
          <td>
            <div class="student-row-pill">
              <img src="${s.avatar}" class="student-table-avatar" />
              <div>
                <div style="font-weight:600; color:var(--text-primary);">${s.name}</div>
                <div style="font-size:0.75rem; color:var(--text-muted);">${s.email}</div>
              </div>
            </div>
          </td>
          <td><span class="badge badge-cyan">${s.classId} (${s.departmentCode})</span></td>
          <td><span style="font-family:var(--font-mono); font-weight:700;">${s.rollNo}</span></td>
          <td>
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-family:var(--font-mono); font-weight:700; color:${isLow ? 'var(--coral)' : 'var(--emerald)'};">${s.overallAttendance}%</span>
              <div class="progress-bar-container" style="width:80px; height:6px; margin-top:0;">
                <div class="progress-bar-fill ${isLow ? 'warning' : ''}" style="width:${s.overallAttendance}%;"></div>
              </div>
            </div>
          </td>
          <td>
            <div style="font-size:0.85rem; color:#FFFFFF; font-weight:600;">${s.parentName || 'Rajaram Chavan'}</div>
            <div style="font-size:0.72rem; color:var(--text-muted);">${s.parentPhone || ''}</div>
          </td>
          <td class="actions-col-cell">
            <div class="action-buttons-group">
              ${viewBtn}
              ${editBtn}
              ${deleteBtn}
            </div>
          </td>
        </tr>
      `;
    }).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  const studentClassFilter = document.getElementById("studentClassFilter");
  if (studentClassFilter) {
    studentClassFilter.addEventListener("change", renderStudentTable);
  }
  const studentSearchInput = document.getElementById("studentSearchInput");
  if (studentSearchInput) {
    studentSearchInput.addEventListener("input", renderStudentTable);
  }

  window.openAddStudentModal = function() {
    const modal = document.getElementById("studentFormModal");
    document.getElementById("studentModalTitle").textContent = "Register New Student (CS or IT)";
    document.getElementById("studentFormId").value = "";
    document.getElementById("studentFormName").value = "";
    document.getElementById("studentFormRoll").value = "";
    document.getElementById("studentFormEmail").value = "";
    document.getElementById("studentFormParentName").value = "";
    document.getElementById("studentFormParentPhone").value = "";
    if (modal) modal.classList.add("active");
  };

  window.openEditStudentModal = function(id) {
    const currentUser = window.attendxStore.getCurrentUser();
    const role = currentUser ? currentUser.role : "admin";
    if (role !== "admin" && role !== "teacher") {
      showToast("Access Denied", "You do not have permission to edit student records.", "danger");
      return;
    }
    const s = window.attendxStore.getStudentById(id);
    if (!s) return;
    const modal = document.getElementById("studentFormModal");
    document.getElementById("studentModalTitle").textContent = `Edit Student: ${s.name}`;
    document.getElementById("studentFormId").value = s.id;
    document.getElementById("studentFormName").value = s.name;
    document.getElementById("studentFormRoll").value = s.rollNo;
    document.getElementById("studentFormEmail").value = s.email;
    document.getElementById("studentFormClass").value = s.classId;
    document.getElementById("studentFormParentName").value = s.parentName || "";
    document.getElementById("studentFormParentPhone").value = s.parentPhone || "";
    if (modal) modal.classList.add("active");
  };

  window.closeStudentModal = function() {
    const modal = document.getElementById("studentFormModal");
    if (modal) modal.classList.remove("active");
  };

  const studentForm = document.getElementById("studentForm");
  if (studentForm) {
    studentForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const id = document.getElementById("studentFormId").value;
      const data = {
        name: document.getElementById("studentFormName").value.trim(),
        rollNo: document.getElementById("studentFormRoll").value.trim(),
        email: document.getElementById("studentFormEmail").value.trim(),
        classId: document.getElementById("studentFormClass").value,
        parentName: document.getElementById("studentFormParentName").value.trim(),
        parentPhone: document.getElementById("studentFormParentPhone").value.trim()
      };

      if (id) {
        window.attendxStore.updateStudent(id, data);
        showToast("Student Updated", `Record for ${data.name} saved.`, "success");
      } else {
        window.attendxStore.addStudent(data);
        showToast("Student Registered", `${data.name} enrolled in Class ${data.classId}.`, "success");
      }

      closeStudentModal();
      renderStudentTable();
      renderAdminDashboard();
    });
  }

  window.deleteStudentRecord = function(id) {
    const currentUser = window.attendxStore.getCurrentUser();
    const role = currentUser ? currentUser.role : "admin";
    if (role !== "admin") {
      showToast("Access Denied", "Only administrators have permission to delete student records.", "danger");
      return;
    }
    if (confirm("Are you certain you wish to delete this student record? This action cannot be reversed.")) {
      window.attendxStore.deleteStudent(id);
      showToast("Record Removed", "Student record was removed from the campus database.", "danger");
      renderStudentTable();
      renderAdminDashboard();
    }
  };

  window.inspectStudentProfile = function(id) {
    const s = window.attendxStore.getStudentById(id);
    if (!s) return;

    const modal = document.getElementById("dayDetailsModal");
    const title = document.getElementById("dayDetailsTitle");
    const body = document.getElementById("dayDetailsBody");

    if (title) title.textContent = `Student Profile: ${s.name}`;
    if (body) {
      body.innerHTML = `
        <div style="display:flex; align-items:center; gap:20px; margin-bottom:20px; padding-bottom:16px; border-bottom:1px solid var(--border-glass-subtle);">
          <img src="${s.avatar}" style="width:72px;height:72px;border-radius:50%;object-fit:cover;border:2px solid var(--cyan);" />
          <div>
            <h3 style="font-size:1.25rem;">${s.name}</h3>
            <p style="color:var(--text-secondary); font-size:0.85rem;">${s.email}</p>
            <p style="color:var(--cyan); font-family:var(--font-mono); font-size:0.85rem; margin-top:2px;">Roll: ${s.rollNo} • Class: ${s.classId} (${s.department})</p>
          </div>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:16px;">
          <div style="padding:12px; background:rgba(6,11,28,0.7); border-radius:var(--radius-sm);">
            <div style="font-size:0.75rem; color:var(--text-muted);">OVERALL ATTENDANCE</div>
            <div style="font-size:1.5rem; font-weight:800; color:${s.overallAttendance < 75 ? 'var(--coral)' : 'var(--cyan)'};">${s.overallAttendance}%</div>
          </div>
          <div style="padding:12px; background:rgba(6,11,28,0.7); border-radius:var(--radius-sm);">
            <div style="font-size:0.75rem; color:var(--text-muted);">ACTIVE STREAK</div>
            <div style="font-size:1.5rem; font-weight:800; color:var(--amber);">🔥 ${s.streak} Days</div>
          </div>
        </div>
        <div style="font-size:0.85rem; color:var(--text-secondary); line-height:1.6;">
          <strong>Guardian:</strong> ${s.parentName || "Rajaram Chavan"}<br/>
          <strong>Guardian Contact:</strong> ${s.parentPhone || "+91 98201 00000"}<br/>
          <strong>Dean Authority:</strong> Dr. Vidya Mohod Ma’am<br/>
          <strong>Academic Standing:</strong> ${s.overallAttendance < 75 ? '<span class="text-coral">Critical Debarment Risk (<75%)</span>' : '<span class="text-emerald">Good Academic Standing</span>'}
        </div>
      `;
    }
    if (modal) modal.classList.add("active");
    if (window.lucide) window.lucide.createIcons();
  };

  // =========================================================================
  // 14. NOTIFICATION CENTER & BROADCAST DISPATCHER
  // =========================================================================
  function renderNotificationCenter() {
    const listEl = document.getElementById("notificationsListFull");
    if (!listEl) return;

    const notifs = window.attendxStore.getNotifications("all");
    listEl.innerHTML = notifs.map(n => `
      <div class="glass-card notif-card ${n.severity} ${!n.read ? 'unread' : ''}" style="margin-bottom:12px; padding:18px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div style="display:flex; align-items:center; gap:10px;">
            <span class="badge ${n.severity === 'danger' ? 'badge-absent' : n.severity === 'warning' ? 'badge-late' : 'badge-present'}">
              ${n.type.toUpperCase()}
            </span>
            <span style="font-weight:700; color:#FFFFFF; font-size:1rem;">${n.title}</span>
          </div>
          <span style="font-size:0.75rem; color:var(--text-muted); font-family:var(--font-mono);">${n.date}</span>
        </div>
        <div style="margin-top:10px; color:var(--text-secondary); font-size:0.9rem; line-height:1.5;">${n.message}</div>
      </div>
    `).join("");

    if (window.lucide) window.lucide.createIcons();
  }

  window.openComposeNotificationModal = function() {
    const modal = document.getElementById("composeNotificationModal");
    if (modal) modal.classList.add("active");
  };

  window.closeComposeNotificationModal = function() {
    const modal = document.getElementById("composeNotificationModal");
    if (modal) modal.classList.remove("active");
  };

  const composeNotifForm = document.getElementById("composeNotifForm");
  if (composeNotifForm) {
    composeNotifForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const type = document.getElementById("notifFormType").value;
      const title = document.getElementById("notifFormTitle").value.trim();
      const message = document.getElementById("notifFormMessage").value.trim();
      const classId = document.getElementById("notifFormTarget").value;

      let severity = "info";
      if (type === "absent" || type === "warning") severity = "danger";
      if (type === "late") severity = "warning";
      if (type === "present") severity = "success";

      window.attendxStore.sendNotification({
        type,
        severity,
        title,
        message,
        classId: classId === "ALL" ? null : classId
      });

      closeComposeNotificationModal();
      showToast("Notification Broadcast", "Campus alert dispatched successfully.", "success");
      renderNotificationCenter();
    });
  }

  window.toggleNotificationDrawer = function() {
    const drawer = document.getElementById("notificationDrawer");
    if (drawer) {
      drawer.classList.toggle("active");
      if (drawer.classList.contains("active")) {
        renderDrawerNotifications();
      }
    }
  };

  function renderDrawerNotifications() {
    const container = document.getElementById("drawerNotifContainer");
    if (!container) return;

    const notifs = window.attendxStore.getNotifications("all");
    container.innerHTML = notifs.map(n => `
      <div class="notif-card ${n.severity} ${!n.read ? 'unread' : ''}">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div style="font-weight:700; font-size:0.88rem; color:#FFFFFF;">${n.title}</div>
          <span style="font-size:0.7rem; color:var(--text-muted); font-family:var(--font-mono);">${n.date}</span>
        </div>
        <div style="font-size:0.8rem; color:var(--text-secondary); margin-top:4px;">${n.message}</div>
      </div>
    `).join("");
  }

  // =========================================================================
  // 15. ANALYTICS PAGE (CS & IT)
  // =========================================================================
  function renderAnalyticsView() {
    setTimeout(() => {
      if (window.attendxCharts) {
        window.attendxCharts.renderAnalyticsCharts();
      }
    }, 50);
  }

  // =========================================================================
  // 16. REPORTS PAGE & EXPORTS (CS & IT Only)
  // =========================================================================
  function initReportsPage() {
    generateFilteredReport();
  }

  window.generateFilteredReport = function() {
    const classId = document.getElementById("reportClassSelect")?.value || "ALL";
    const status = document.getElementById("reportStatusSelect")?.value || "ALL";
    const tbody = document.getElementById("reportTableBody");
    if (!tbody) return;

    let students = window.attendxStore.getStudents(classId, "", status);

    tbody.innerHTML = students.map((s, idx) => `
      <tr>
        <td>${idx + 1}</td>
        <td><strong>${s.name}</strong></td>
        <td><span style="font-family:var(--font-mono);">${s.rollNo}</span></td>
        <td>${s.classId} (${s.departmentCode})</td>
        <td><strong style="color:${s.overallAttendance < 75 ? 'var(--coral)' : 'var(--emerald)'};">${s.overallAttendance}%</strong></td>
        <td>${s.parentName || "Rajaram Chavan"} (${s.parentPhone || "+91 98201 44521"})</td>
        <td><span class="badge ${s.overallAttendance < 75 ? 'badge-warning' : 'badge-present'}">${s.overallAttendance < 75 ? 'RISK (<75%)' : 'ELIGIBLE'}</span></td>
      </tr>
    `).join("");

    if (window.lucide) window.lucide.createIcons();
  };

  window.printOfficialReport = function() {
    window.print();
  };

  window.exportReportCSV = function() {
    const students = window.attendxStore.getStudents();
    let csvContent = "data:text/csv;charset=utf-8,Student ID,Name,Roll Number,Class,Department,Overall Attendance,Guardian,Contact\n";

    students.forEach(s => {
      csvContent += `${s.id},"${s.name}",${s.rollNo},${s.classId},${s.department},${s.overallAttendance}%,"${s.parentName || 'Rajaram Chavan'}","${s.parentPhone || ''}"\n`;
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `AttendX_Official_Report_${new Date().toISOString().slice(0, 10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast("Report Exported", "Downloaded official attendance CSV digest for CS & IT.", "success");
  };

  // =========================================================================
  // 17. REACTIVE STORE SUBSCRIPTIONS (Requirement 13: Data Consistency)
  // =========================================================================
  window.attendxStore.subscribe("studentsChanged", () => {
    if (currentActiveView === "admin-dashboard") renderAdminDashboard();
    else if (currentActiveView === "campus-classes") renderCampusClassesView();
    else if (currentActiveView === "students") renderStudentTable();
    else if (currentActiveView === "reports") generateFilteredReport();
    else if (currentActiveView === "parent-dashboard") renderParentDashboard();
    else if (currentActiveView === "student-dashboard") renderStudentDashboard();
  });

  window.attendxStore.subscribe("teachersChanged", () => {
    if (currentActiveView === "teachers-dir") renderTeachersDirectory();
    if (currentActiveView === "admin-dashboard") renderAdminDashboard();
  });

  window.attendxStore.subscribe("attendanceSaved", () => {
    if (currentActiveView === "admin-dashboard") renderAdminDashboard();
    if (currentActiveView === "parent-dashboard") renderParentDashboard();
    if (currentActiveView === "student-dashboard") renderStudentDashboard();
  });

  // =========================================================================
  // 17B. FIREBASE CLOUD DATABASE CONTROLLERS
  // =========================================================================
  function updateFirebaseUIStatus(status) {
    const pill = document.getElementById("firebaseStatusPill");
    const dot = document.getElementById("firebaseStatusDot");
    const text = document.getElementById("firebaseStatusText");
    const modalDot = document.getElementById("fbModalStatusDot");
    const modalLabel = document.getElementById("fbModalStatusLabel");
    const modalProjectId = document.getElementById("fbModalProjectId");
    const modalLastSync = document.getElementById("fbModalLastSync");

    const isConnected = status && status.isConnected;
    const color = isConnected ? "#10B981" : "#F59E0B";

    if (dot) {
      dot.style.background = color;
      dot.style.boxShadow = `0 0 8px ${color}`;
    }
    if (text) {
      text.textContent = isConnected ? "Cloud Synced" : "Local Mode";
    }
    if (pill) {
      pill.title = isConnected
        ? `Connected to Firebase Cloud Firestore (${status.projectId})`
        : "Running in Local Offline Fallback Mode. Click to view / connect Firebase.";
    }

    if (modalDot) {
      modalDot.style.background = color;
      modalDot.style.boxShadow = `0 0 8px ${color}`;
    }
    if (modalLabel) {
      modalLabel.textContent = isConnected ? "Cloud Firestore Active" : "Local Fallback Mode";
      modalLabel.style.color = color;
    }
    if (modalProjectId && status) {
      modalProjectId.textContent = status.projectId || "attendx-smart-campus";
    }
    if (modalLastSync && status && status.lastSyncTime) {
      modalLastSync.textContent = new Date(status.lastSyncTime).toLocaleTimeString();
    }
  }

  window.attendxStore.subscribe("firebaseStatusChanged", (status) => {
    updateFirebaseUIStatus(status);
  });

  function openFirebaseModal() {
    const modal = document.getElementById("firebaseSettingsModal");
    if (!modal) return;

    if (window.AttendXFirebaseConfig) {
      const config = window.AttendXFirebaseConfig.get();
      const apiKeyEl = document.getElementById("fbInputApiKey");
      const projIdEl = document.getElementById("fbInputProjectId");
      const authDomainEl = document.getElementById("fbInputAuthDomain");
      const appIdEl = document.getElementById("fbInputAppId");

      if (apiKeyEl) apiKeyEl.value = config.apiKey || "";
      if (projIdEl) projIdEl.value = config.projectId || "";
      if (authDomainEl) authDomainEl.value = config.authDomain || "";
      if (appIdEl) appIdEl.value = config.appId || "";
    }

    if (window.firebaseService) {
      updateFirebaseUIStatus(window.firebaseService.getStatus());
    }

    modal.classList.add("active");
    if (window.lucide) window.lucide.createIcons();
  }
  window.openFirebaseModal = openFirebaseModal;

  function closeFirebaseModal() {
    const modal = document.getElementById("firebaseSettingsModal");
    if (modal) modal.classList.remove("active");
  }
  window.closeFirebaseModal = closeFirebaseModal;

  async function saveCustomFirebaseConfig() {
    try {
      const apiKey = document.getElementById("fbInputApiKey")?.value.trim();
      const projectId = document.getElementById("fbInputProjectId")?.value.trim();
      const authDomain = document.getElementById("fbInputAuthDomain")?.value.trim();
      const appId = document.getElementById("fbInputAppId")?.value.trim();

      if (!projectId) {
        showToast("Configuration Error", "Project ID is required to connect to Firebase.", "danger");
        return;
      }

      const newConfig = {
        apiKey: apiKey || "AIzaSyDemo-Key",
        authDomain: authDomain || `${projectId}.firebaseapp.com`,
        projectId: projectId,
        storageBucket: `${projectId}.appspot.com`,
        messagingSenderId: "109827364521",
        appId: appId || "1:109827364521:web:demo"
      };

      if (window.AttendXFirebaseConfig) {
        window.AttendXFirebaseConfig.save(newConfig);
      }

      showToast("Connecting to Cloud", `Connecting to Firebase Project: ${projectId}...`, "info");

      if (window.firebaseService) {
        const ok = await window.firebaseService.init();
        updateFirebaseUIStatus(window.firebaseService.getStatus());
        if (ok) {
          playCyberTone("success");
          showToast("Cloud Connected", `Successfully connected to Firebase Project: ${projectId}`, "success");
        } else {
          showToast("Hybrid Mode", "Config saved. System operating with local & cloud fallback.", "warning");
        }
      }
      closeFirebaseModal();
    } catch (e) {
      showToast("Error", e.message || "Failed to save Firebase config", "danger");
    }
  }
  window.saveCustomFirebaseConfig = saveCustomFirebaseConfig;

  function resetFirebaseToDefaults() {
    if (window.AttendXFirebaseConfig) {
      window.AttendXFirebaseConfig.reset();
      const def = window.AttendXFirebaseConfig.defaultConfig;
      const apiKeyEl = document.getElementById("fbInputApiKey");
      const projIdEl = document.getElementById("fbInputProjectId");
      const authDomainEl = document.getElementById("fbInputAuthDomain");
      const appIdEl = document.getElementById("fbInputAppId");

      if (apiKeyEl) apiKeyEl.value = def.apiKey;
      if (projIdEl) projIdEl.value = def.projectId;
      if (authDomainEl) authDomainEl.value = def.authDomain;
      if (appIdEl) appIdEl.value = def.appId;

      showToast("Defaults Restored", "Firebase configuration reset to default template.", "info");
    }
  }
  window.resetFirebaseToDefaults = resetFirebaseToDefaults;

  async function seedFirebaseCloudData() {
    if (!window.firebaseService || !window.firebaseService.isConnected) {
      showToast("Cloud Offline", "Connect to Firebase Cloud first before seeding data.", "warning");
      return;
    }

    try {
      showToast("Uploading Dataset", "Uploading students, teachers, and rosters to Cloud Firestore...", "info");
      await window.firebaseService.seedCloudDatabase(window.SEED_DATA);
      playCyberTone("success");
      showToast("Cloud Seed Complete", "All campus collections populated in Cloud Firestore!", "success");
      updateFirebaseUIStatus(window.firebaseService.getStatus());
    } catch (e) {
      showToast("Seed Error", e.message || "Failed to seed cloud database.", "danger");
    }
  }
  window.seedFirebaseCloudData = seedFirebaseCloudData;

  // =========================================================================
  // 18. INITIAL APP BOOTSTRAP
  // =========================================================================
  clearLoginFields(true);
  const currentUser = window.attendxStore.getCurrentUser();
  if (currentUser) {
    updateSidebarNavigation(currentUser.role);
    updateUserInterfaceSession(currentUser);
    if (currentUser.role === "admin") switchView("admin-dashboard");
    else if (currentUser.role === "teacher") switchView("teacher-dashboard");
    else if (currentUser.role === "parent") switchView("parent-dashboard");
    else if (currentUser.role === "student") switchView("student-dashboard");
  } else {
    // Default to Landing Page
    updateSidebarNavigation("admin");
    switchView("landing");
  }

  if (window.lucide) window.lucide.createIcons();
});
