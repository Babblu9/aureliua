import glob
import re

# Update all HTML files
for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()

    # Find the Profile Building list item and insert IPMAT before it
    ipmat_link = '          <li><a href="programs.html#ipmat">IPMAT</a></li>\n'
    if ipmat_link not in content:
        content = re.sub(
            r'(\s*<li><a href="programs\.html#english">Profile Building</a></li>)',
            r'\n' + ipmat_link + r'\1',
            content
        )
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")

# Update js/main.js
with open('js/main.js', 'r') as f:
    main_js = f.read()

ipmat_option = '          <option>IPMAT</option>\n'
if ipmat_option not in main_js:
    main_js = re.sub(
        r'(\s*<option>Profile Building</option>)',
        r'\n' + ipmat_option + r'\1',
        main_js
    )

with open('js/main.js', 'w') as f:
    f.write(main_js)
print("Updated js/main.js")
