import glob
import re

POPUP_HTML = """
<!-- SIDE POPUP FORM -->
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
          <option>Aurelius AP Exams</option>
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

<script>
  (function() {
    // Re-trigger lucide icons to catch the newly added X icon
    if(typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    // Setup popup logic
    const popupOverlay = document.getElementById('sidePopupOverlay');
    const sidePopup = document.getElementById('sidePopup');
    const closeBtn = document.getElementById('closeSidePopup');
    const floatingBtn = document.getElementById('floatingEnquireBtn');
    
    if (!sessionStorage.getItem('enquiryPopupShown')) {
      setTimeout(() => {
        if(popupOverlay) popupOverlay.classList.add('active');
        if(sidePopup) sidePopup.classList.add('active');
        sessionStorage.setItem('enquiryPopupShown', 'true');
      }, 3500);
    }

    const closePopup = () => {
      if(popupOverlay) popupOverlay.classList.remove('active');
      if(sidePopup) sidePopup.classList.remove('active');
    };

    if(closeBtn) closeBtn.addEventListener('click', closePopup);
    if(popupOverlay) popupOverlay.addEventListener('click', closePopup);

    if(floatingBtn) {
      floatingBtn.addEventListener('click', () => {
        if(popupOverlay) popupOverlay.classList.add('active');
        if(sidePopup) sidePopup.classList.add('active');
      });
    }
  })();
</script>
</body>
"""

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()

    # 1. Remove the nav-cta button from the header
    content = re.sub(r'\s*<li><a href="[^"]*#contact" class="nav-cta">Enquire Now</a></li>', '', content)

    # 2. Strip out the existing side popup block and its scripts in index.html if it exists
    # We will just replace everything from <!-- SIDE POPUP FORM --> to the end of the body with </body>
    content = re.sub(r'<!-- SIDE POPUP FORM -->.*?</body>', '</body>', content, flags=re.DOTALL)
    
    # 3. Strip out the old script block from index.html that contained the side popup logic
    # Since we can't be sure of the exact boundary, we will just rely on the above regex catching it if it was after the html.
    # Wait, in index.html, the side popup was added right before <script src="js/main.js">
    # Let's remove the old JS block targeting Side Popup Logic explicitly
    content = re.sub(r'// Side Popup Logic.*?}\);', '', content, flags=re.DOTALL)

    # 4. Inject the new POPUP_HTML right before </body>
    content = content.replace('</body>', POPUP_HTML)

    with open(file, 'w') as f:
        f.write(content)
    
    print(f"Updated {file}")
