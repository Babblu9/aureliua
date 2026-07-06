/* Aurelius Academy — Main JS */

// Navbar scroll effect
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  });
}

// Active nav link
const currentPage = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html')) {
    link.classList.add('active');
  }
});

// Mobile menu
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    hamburger.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
    const spans = hamburger.querySelectorAll('span');
    if (open) {
      spans[0].style.transform = 'rotate(45deg) translate(5px,5px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px,-5px)';
    } else {
      spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    }
  });
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.setAttribute('aria-label', 'Open navigation menu');
    hamburger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  }));
}

// Animated stat counters
function animateCounters() {
  document.querySelectorAll('.stat-num[data-target]').forEach(el => {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1800;
    const step = Math.ceil(target / (duration / 16));
    let current = 0;
    const inner = el.querySelector('span') || el;
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.innerHTML = current + '<span>' + suffix + '</span>';
      if (current >= target) clearInterval(timer);
    }, 16);
  });
}

// Intersection observer for stat counters and fade-in
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    if (entry.target.classList.contains('stats-bar')) animateCounters();
    entry.target.classList.add('visible');
    observer.unobserve(entry.target);
  });
}, { threshold: 0.15 });

document.querySelectorAll('.stats-bar, .fade-in').forEach(el => observer.observe(el));

// Fade-in on scroll for cards
const cardObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      cardObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.program-card, .pathway-card, .why-card, .uni-card, .uni-detail-card, .outlook-card, .service-card').forEach(el => {
  el.classList.add('fade-card');
  cardObserver.observe(el);
});

// Smooth external link handling
document.querySelectorAll('a[href^="tel"], a[href^="mailto"]').forEach(a => {
  a.addEventListener('click', e => e.stopPropagation());
});

// Contact form -> prefilled email (mailto). The form's action="mailto:" is the no-JS fallback.
const enquiryForm = document.getElementById('enquiryForm');
if (enquiryForm) {
  enquiryForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const val = (name) => {
      const field = enquiryForm.querySelector('[name="' + name + '"]');
      return field ? field.value.trim() : '';
    };
    const fullName = (val('First Name') + ' ' + val('Last Name')).trim();
    const program = val('Program of Interest');
    const subject = 'Enquiry' + (program ? ' — ' + program : '') + (fullName ? ' from ' + fullName : '');
    const body =
      'Name: ' + fullName + '\n' +
      'Email: ' + val('Email') + '\n' +
      'Phone: ' + val('Phone') + '\n' +
      'Program of Interest: ' + program + '\n\n' +
      'Message:\n' + val('Message') + '\n';
    window.location.href = 'mailto:info@aureliusacademy.in'
      + '?subject=' + encodeURIComponent(subject)
      + '&body=' + encodeURIComponent(body);
  });
}

// --- GLOBAL SIDE POPUP ---
document.addEventListener('DOMContentLoaded', () => {
  // Add popup HTML to DOM if not already there
  if (!document.getElementById('sidePopup')) {
    const popupHTML = `
<div id="sidePopupOverlay" class="side-popup-overlay"></div>
<div id="sidePopup" class="side-popup">
  <button id="closeSidePopup" class="side-popup-close" aria-label="Close form"><i data-lucide="x"></i></button>
  <div class="side-popup-content">
    <h3 style="font-family:var(--font-serif); font-size:1.8rem; color:var(--navy); margin-bottom:12px;">Enquire Now</h3>
    <p style="font-size:0.9rem; color:var(--text-mid); margin-bottom:24px; line-height:1.6;">Start your journey with Aurelius. Fill out the form below and our team will get in touch.</p>
    <form class="contact-form" action="mailto:info@aureliusacademy.in" method="post" enctype="text/plain" style="padding:0; border:none; background:transparent;">
      <div class="form-group">
        <label for="popupName">Name</label>
        <input type="text" id="popupName" name="Name" placeholder="Your name" required/>
      </div>
      <div class="form-group">
        <label for="popupEmail">Email</label>
        <input type="email" id="popupEmail" name="Email" placeholder="your@email.com" required/>
      </div>
      <div class="form-group">
        <label for="popupPhone">Phone</label>
        <input type="tel" id="popupPhone" name="Phone" placeholder="+91 XXXXX XXXXX"/>
      </div>
      <div class="form-group">
        <label for="popupProgram">Program of Interest</label>
        <select id="popupProgram" name="Program of Interest">
          <option value="">Select a program</option>
          <option>SAT</option>
          <option>IELTS</option>
          <option>AP Exams</option>
          <option>Profile Building</option>
          <option>Admissions Guidance</option>
          <option>Management Pathways</option>
          <option>University Admissions</option>
          <option>Global Pathways</option>
        </select>
      </div>
      <div class="form-group">
        <label for="popupMessage">Comments</label>
        <textarea id="popupMessage" name="Comments" placeholder="Tell us about your goals and any questions you have..."></textarea>
      </div>
      <button type="submit" class="btn btn-gold" style="width:100%; justify-content:center; margin-top:10px;">Send Enquiry</button>
    </form>
  </div>
</div>
<!-- FLOATING ENQUIRE BUTTON -->
<button id="floatingEnquireBtn" class="floating-enquire-btn">
  Enquire Now
</button>
`;
    document.body.insertAdjacentHTML('beforeend', popupHTML);
  }

  // Side Popup Logic
  const popupOverlay = document.getElementById('sidePopupOverlay');
  const sidePopup = document.getElementById('sidePopup');
  const closeBtn = document.getElementById('closeSidePopup');
  const floatingBtn = document.getElementById('floatingEnquireBtn');

  if (!sessionStorage.getItem('enquiryPopupShown')) {
    setTimeout(() => {
      if (popupOverlay) popupOverlay.classList.add('active');
      if (sidePopup) sidePopup.classList.add('active');
      sessionStorage.setItem('enquiryPopupShown', 'true');
    }, 3500);
  }

  const closePopup = () => {
    if (popupOverlay) popupOverlay.classList.remove('active');
    if (sidePopup) sidePopup.classList.remove('active');
  };

  if(closeBtn) closeBtn.addEventListener('click', closePopup);
  if(popupOverlay) popupOverlay.addEventListener('click', closePopup);

  if(floatingBtn) {
    floatingBtn.addEventListener('click', () => {
      if (popupOverlay) popupOverlay.classList.add('active');
      if (sidePopup) sidePopup.classList.add('active');
    });
  }

  // Ensure the new X icon is rendered by Lucide if it's already loaded
  if (typeof lucide !== 'undefined' && lucide.createIcons) {
    lucide.createIcons();
  }
});

