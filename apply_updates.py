import re
import glob

for f in glob.glob("*.html"):
    with open(f, 'r') as file:
        content = file.read()
        
    original = content
    
    # Change 2 & 4: Remove numbering 1 to 4 from Our Approach
    content = re.sub(r'\s*<div class="step-num">\d+</div>', '', content)
    
    # Change 3: Add Aurelius Leaders to the footer programs list
    old_badges = """<span class="cta-badge">Aurelius Scholars</span>
          <span class="cta-badge">Aurelius Signature</span>
          <span class="cta-badge">Aurelius AP Excellence</span>
          <span class="cta-badge">Aurelius Global</span>"""
          
    new_badges = """<span class="cta-badge">Aurelius Scholars</span>
          <span class="cta-badge">Aurelius Signature</span>
          <span class="cta-badge">Aurelius AP Excellence</span>
          <span class="cta-badge">Aurelius Leaders</span>
          <span class="cta-badge">Aurelius Global</span>"""
    
    content = content.replace(old_badges, new_badges)
    
    # Change 5: Remove 'Why Families Choose Aurelius' section in university.html
    if f == 'university.html':
        content = re.sub(r'<!-- WHY FAMILIES CHOOSE AURELIUS -->\s*<section style="background:var\(--cream\)">.*?</section>', '', content, flags=re.DOTALL)
        
    # Change 6: Change text in footer
    content = content.replace("Book a free 30-minute consultation with our counselling team.", "Schedule a consultation with our counselling team.")
    
    # Change 1: Insert Founders.JPG in index.html
    if f == 'index.html':
        founder_image_html = """
      <div style="margin: 40px 0; border-radius: var(--radius); overflow: hidden; box-shadow: 0 16px 40px rgba(0,0,0,0.1);">
        <img src="gallery/Founders.JPG" alt="Aurelius Founders" style="width: 100%; height: auto; display: block; aspect-ratio: 16/9; object-fit: cover;">
      </div>
      <blockquote class="founder-pullquote" style="text-align: center;">"We do not simply prepare students for examinations. We prepare them for the lives those examinations make possible."</blockquote>"""
        
        # Replace the existing blockquote line to include the image right before it.
        content = re.sub(r'\s*<blockquote class="founder-pullquote".*?</blockquote>', founder_image_html, content, count=1)
    
    if content != original:
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")

