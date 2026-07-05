import glob
import re

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()
    
    # Standardize first to avoid double "Aurelius"
    content = content.replace("Aurelius AP Exams", "AP Exams")
    
    # Replace all "AP Exams" with "Aurelius AP Excellence"
    content = content.replace("AP Exams", "Aurelius AP Excellence")
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")

