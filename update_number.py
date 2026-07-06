import glob

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to replace the display text, not the href.
    # Typically it looks like: >+91 9121473399<
    content = content.replace("+91 9121473399", "+91 91214 73399")
    content = content.replace(">+919121473399<", ">+91 91214 73399<")
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")
