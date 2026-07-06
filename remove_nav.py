import glob
import re

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()

    # 1. Remove the nav-cta button from the header
    content = re.sub(r'\s*<li><a href="[^"]*#contact" class="nav-cta">Enquire Now</a></li>', '', content)
    
    # 2. In index.html, remove the inline popup block to avoid duplicates
    if file == 'index.html':
        content = re.sub(r'<!-- SIDE POPUP FORM -->.*?</button>', '', content, flags=re.DOTALL)
        content = re.sub(r'// Side Popup Logic.*?(?=\s*</script>)', '', content, flags=re.DOTALL)
        
        # Cleanup any trailing empty lines in the script block
        content = re.sub(r'\s*// Ensure the new X icon.*?(?=\s*</script>)', '', content, flags=re.DOTALL)

    with open(file, 'w') as f:
        f.write(content)
    
    print(f"Updated {file}")
