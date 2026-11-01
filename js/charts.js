/**
 * AttendX - Smart Attendance Monitoring & Parent Notification System
 * Holographic Chart.js Initializer
 * Configured for CS & IT Departments
 */

class AttendXCharts {
  constructor() {
    this.instances = {};
  }

  // Helper to create neon gradient fills
  createGradient(ctx, colorStart, colorEnd) {
    const gradient = ctx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, colorStart);
    gradient.addColorStop(1, colorEnd);
    return gradient;
  }

  // Safe destroy if chart already exists
  destroyChart(id) {
    if (this.instances[id]) {
      this.instances[id].destroy();
      delete this.instances[id];
    }
  }

  // 1. Admin Attendance Trend Line Chart
  renderAttendanceTrend(canvasId = "trendChart") {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    this.destroyChart(canvasId);

    const ctx = canvas.getContext("2d");
    const fillGradient = this.createGradient(ctx, "rgba(0, 240, 255, 0.25)", "rgba(139, 92, 246, 0.0)");

    this.instances[canvasId] = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Today"],
        datasets: [
          {
            label: "Campus Attendance %",
            data: [92.0, 94.5, 91.8, 95.2, 93.4, 96.0, 93.3],
            borderColor: "#00F0FF",
            borderWidth: 3,
            pointBackgroundColor: "#00F0FF",
            pointBorderColor: "#060919",
            pointBorderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 8,
            pointHoverBackgroundColor: "#FFFFFF",
            pointHoverBorderColor: "#00F0FF",
            pointHoverBorderWidth: 3,
            fill: true,
            backgroundColor: fillGradient,
            tension: 0.4
          },
          {
            label: "Target Benchmark (75%)",
            data: [75, 75, 75, 75, 75, 75, 75],
            borderColor: "rgba(239, 68, 68, 0.4)",
            borderWidth: 1.5,
            borderDash: [6, 6],
            pointRadius: 0,
            fill: false,
            tension: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            backgroundColor: "rgba(11, 17, 44, 0.9)",
            titleColor: "#00F0FF",
            bodyColor: "#F8FAFC",
            borderColor: "rgba(0, 240, 255, 0.3)",
            borderWidth: 1,
            padding: 12,
            displayColors: false,
            callbacks: {
              label: function (context) {
                return `Attendance: ${context.parsed.y}%`;
              }
            }
          }
        },
        scales: {
          y: {
            min: 60,
            max: 100,
            grid: {
              color: "rgba(255, 255, 255, 0.05)",
              drawBorder: false
            },
            ticks: {
              color: "#94A3B8",
              font: { family: "Inter", size: 11 },
              callback: val => val + "%"
            }
          },
          x: {
            grid: {
              display: false,
              drawBorder: false
            },
            ticks: {
              color: "#94A3B8",
              font: { family: "Inter", size: 12 }
            }
          }
        }
      }
    });
  }

  // 2. Present vs Absent vs Late Doughnut Chart
  renderStatusDoughnut(canvasId = "statusDoughnutChart") {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    this.destroyChart(canvasId);

    const stats = window.attendxStore ? window.attendxStore.getCampusStats() : { presentToday: 13, absentToday: 2, lateToday: 0 };
    const ctx = canvas.getContext("2d");

    this.instances[canvasId] = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: ["Present Today", "Absent Today", "Late Arrival"],
        datasets: [
          {
            data: [stats.presentToday, stats.absentToday, stats.lateToday || 0],
            backgroundColor: [
              "rgba(16, 185, 129, 0.85)",  // Emerald
              "rgba(239, 68, 68, 0.85)",   // Coral Red
              "rgba(245, 158, 11, 0.85)"   // Solar Amber
            ],
            borderColor: [
              "#10B981",
              "#EF4444",
              "#F59E0B"
            ],
            borderWidth: 2,
            hoverOffset: 8
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "76%",
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              color: "#94A3B8",
              font: { family: "Inter", size: 12 },
              usePointStyle: true,
              pointStyle: "circle",
              padding: 18
            }
          },
          tooltip: {
            backgroundColor: "rgba(11, 17, 44, 0.9)",
            titleColor: "#00F0FF",
            bodyColor: "#F8FAFC",
            borderColor: "rgba(0, 240, 255, 0.3)",
            borderWidth: 1,
            padding: 12,
            callbacks: {
              label: function (ctx) {
                const total = stats.totalStudents || 15;
                const pct = ((ctx.parsed / total) * 100).toFixed(1);
                return ` ${ctx.label}: ${ctx.parsed} students (${pct}%)`;
              }
            }
          }
        }
      }
    });
  }

  // 3. Class-wise Comparative Bar Chart (Only CS & IT)
  renderClassComparison(canvasId = "classBarChart") {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    this.destroyChart(canvasId);

    const stats = window.attendxStore ? window.attendxStore.getCampusStats() : { csAvg: 90.2, itAvg: 89.9 };
    const ctx = canvas.getContext("2d");
    const barGradient = this.createGradient(ctx, "#00F0FF", "#8B5CF6");

    this.instances[canvasId] = new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["CS (Computer Science)", "IT (Information Technology)"],
        datasets: [
          {
            label: "Average Attendance %",
            data: [stats.csAvg || 90.2, stats.itAvg || 89.9],
            backgroundColor: barGradient,
            borderRadius: 8,
            borderSkipped: false,
            barThickness: 42
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: "rgba(11, 17, 44, 0.9)",
            titleColor: "#00F0FF",
            bodyColor: "#F8FAFC",
            borderColor: "rgba(0, 240, 255, 0.3)",
            borderWidth: 1,
            padding: 12,
            callbacks: {
              label: ctx => `Average Attendance: ${ctx.parsed.y}%`
            }
          }
        },
        scales: {
          y: {
            min: 60,
            max: 100,
            grid: {
              color: "rgba(255, 255, 255, 0.05)",
              drawBorder: false
            },
            ticks: {
              color: "#94A3B8",
              font: { family: "Inter", size: 11 },
              callback: val => val + "%"
            }
          },
          x: {
            grid: { display: false, drawBorder: false },
            ticks: {
              color: "#94A3B8",
              font: { family: "Inter", size: 12 }
            }
          }
        }
      }
    });
  }

  // 4. Analytics Suite Multi-Charts (CS vs IT)
  renderAnalyticsCharts() {
    // Multi-week CS vs IT Trajectory
    const dailyCanvas = document.getElementById("analyticsDailyChart");
    if (dailyCanvas) {
      this.destroyChart("analyticsDailyChart");
      const ctx = dailyCanvas.getContext("2d");
      const gradCS = this.createGradient(ctx, "rgba(56, 189, 248, 0.3)", "rgba(56, 189, 248, 0)");
      const gradIT = this.createGradient(ctx, "rgba(168, 85, 247, 0.3)", "rgba(168, 85, 247, 0)");

      this.instances["analyticsDailyChart"] = new Chart(ctx, {
        type: "line",
        data: {
          labels: ["Wk 1", "Wk 2", "Wk 3", "Wk 4", "Wk 5", "Wk 6", "Wk 7", "Wk 8"],
          datasets: [
            {
              label: "CS Department (10 Students)",
              data: [90.5, 91.8, 89.2, 92.4, 93.0, 91.5, 92.8, 93.2],
              borderColor: "#38BDF8",
              backgroundColor: gradCS,
              fill: true,
              tension: 0.35,
              pointRadius: 4
            },
            {
              label: "IT Department (5 Students)",
              data: [88.5, 89.8, 91.2, 90.0, 91.4, 89.9, 91.8, 92.0],
              borderColor: "#A855F7",
              backgroundColor: gradIT,
              fill: true,
              tension: 0.35,
              pointRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              labels: { color: "#94A3B8", usePointStyle: true }
            }
          },
          scales: {
            y: {
              min: 75,
              max: 100,
              grid: { color: "rgba(255, 255, 255, 0.05)" },
              ticks: { color: "#94A3B8", callback: v => v + "%" }
            },
            x: {
              grid: { display: false },
              ticks: { color: "#94A3B8" }
            }
          }
        }
      });
    }

    // Analytics Subject Radar Chart (Core Subjects from CS & IT)
    const subjectCanvas = document.getElementById("analyticsSubjectChart");
    if (subjectCanvas) {
      this.destroyChart("analyticsSubjectChart");
      const ctx = subjectCanvas.getContext("2d");

      this.instances["analyticsSubjectChart"] = new Chart(ctx, {
        type: "radar",
        data: {
          labels: [
            "Data Structures",
            "Database Systems",
            "Software Eng.",
            "Web Technologies",
            "Network Security",
            "Data Analytics"
          ],
          datasets: [
            {
              label: "Campus Attendance %",
              data: [93.5, 92.1, 91.8, 92.0, 91.5, 92.8],
              backgroundColor: "rgba(0, 240, 255, 0.2)",
              borderColor: "#00F0FF",
              pointBackgroundColor: "#00F0FF",
              pointBorderColor: "#fff",
              pointHoverBackgroundColor: "#fff",
              pointHoverBorderColor: "#00F0FF"
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false }
          },
          scales: {
            r: {
              angleLines: { color: "rgba(255, 255, 255, 0.1)" },
              grid: { color: "rgba(255, 255, 255, 0.08)" },
              pointLabels: {
                color: "#94A3B8",
                font: { family: "Inter", size: 11 }
              },
              ticks: {
                backdropColor: "transparent",
                color: "#64748B",
                showLabelBackdrop: false
              },
              min: 70,
              max: 100
            }
          }
        }
      });
    }
  }
}

// Global Chart Manager Instance
window.attendxCharts = new AttendXCharts();
