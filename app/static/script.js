// Create floating particles
function createParticles() {
  const particlesContainer = document.getElementById("particles");
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "%";
    particle.style.animationDelay = Math.random() * 20 + "s";
    particle.style.animationDuration = Math.random() * 10 + 10 + "s";
    particlesContainer.appendChild(particle);
  }
}

// File input UI
document.getElementById("fileInput").addEventListener("change", function (e) {
  const label = document.querySelector(".file-input-label");
  if (e.target.files.length > 0) {
    label.innerHTML = `📄 ${e.target.files[0].name}`;
    label.style.borderColor = "rgba(76, 201, 196, 0.8)";
    label.style.background =
      "linear-gradient(135deg, rgba(76, 201, 196, 0.3), rgba(76, 201, 196, 0.1))";
  }
});

// Form handling
const form = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const summaryBox = document.getElementById("summary-box");
const summaryDiv = document.getElementById("summary");
const progressBar = document.getElementById("progressBar");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const file = fileInput.files[0];
  if (!file) {
    alert("Please select a file.");
    return;
  }

  progressBar.style.display = "block";
  progressBar.style.display = "block";
  progressBar.value = 0;
  summaryBox.classList.remove("show");

  // Simulate summary generation time (5 seconds)
  let duration = 20000; // ms
  let interval = 300; // update every 100ms
  let elapsed = 0;

  const timer = setInterval(() => {
    elapsed += interval;
    progressBar.value = (elapsed / duration) * 100;

    // In case summary finishes early
    if (progressBar.value >= 100) {
      clearInterval(timer);
    }
  }, interval);

  // Send the file
  const formData = new FormData();
  formData.append("file", file);

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/summarize", true);

  xhr.onload = () => {
    clearInterval(timer); // stop simulated progress

    progressBar.value = 100;
    setTimeout(() => {
      progressBar.style.display = "none";
    }, 500);

    try {
      const data = JSON.parse(xhr.responseText);
      summaryDiv.innerHTML = `
      <div class="summary-content">
        <pre>${data.summary}</pre>
        <div class="download-section">
          <a href="/download/${data.filename}" target="_blank" class="download-btn">
            📥 Download Summary
          </a>
        </div>
      </div>
    `;
      summaryBox.classList.add("show");
    } catch (err) {
      summaryDiv.innerHTML = `
      <div class="error-message">
        ❌ Failed to parse server response.
      </div>
    `;
      summaryBox.classList.add("show");
      console.error("Parse error:", err);
    }
  };

  xhr.onerror = () => {
    clearInterval(timer);
    progressBar.style.display = "none";
    summaryDiv.innerHTML = `
    <div class="error-message">
      🔌 Request failed. Server might be down.
    </div>
  `;
    summaryBox.classList.add("show");
  };

  xhr.send(formData);
});

// Initialize particles
document.addEventListener("DOMContentLoaded", createParticles);
