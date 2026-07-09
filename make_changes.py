import re
import glob

html_files = glob.glob("*.html")

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
        
    original = content
    
    # Change 2 & 4: Remove numbering 01 to 04 from Our Approach
    content = re.sub(r'<div class="step-num">0[1-9]</div>', '', content)
    # Also handle if it was an h3 with 01. or similar? Wait, I will check the HTML structure.
    
    # Change 3: Add Aurelius Leaders to the footer programs list
    # The list looks like:
    # <li><a href="programs.html#scholars">Aurelius Scholars</a></li>
    # <li><a href="programs.html#signature">Aurelius Signature</a></li>
    # <li><a href="programs.html#ap">Aurelius AP Excellence</a></li>
    # <li><a href="programs.html#global">Aurelius Global</a></li>
    # Wait, the user said: "we have a list of 4 programs from Aurelius Scholars to Aurelius Global. Add Aurelius Leaders in the 4th place."
    # Let's replace the list entirely in the yellow footer (which is under "Start your Application Journey Today").
    
    # Change 6: Change the text in the yellow footer
    content = content.replace("Book a free 30-minute consultation with our counselling team.", "Schedule a consultation with our counselling team.")
    
    # Change 5: Remove ‘Why Families Choose Aurelius’ section in university.html
    if f == 'university.html':
        # Let's identify the section to remove. Usually it's <section class="why-choose"> or similar.
        pass
        
    if f == 'index.html':
        pass
        
    if content != original:
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")

