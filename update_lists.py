import glob

footer_old = """        <ul>
          <li><a href="programs.html#sat">SAT Preparation</a></li>
          <li><a href="programs.html#ielts">IELTS Coaching</a></li>
          <li><a href="programs.html#ap">AP Courses</a></li>
          <li><a href="programs.html#english">English Proficiency</a></li>
          <li><a href="programs.html#enrichment">Academic Enrichment</a></li>
        </ul>"""

footer_new = """        <ul>
          <li><a href="programs.html#sat">SAT</a></li>
          <li><a href="programs.html#ielts">IELTS</a></li>
          <li><a href="programs.html#ap">AP Exams</a></li>
          <li><a href="programs.html#english">Profile Building</a></li>
          <li><a href="programs.html#enrichment">Admission Guidance</a></li>
        </ul>"""

# The footer indent might be different in some files, so let's do a more flexible replacement
def replace_footer(content):
    import re
    # We will match the <ul> under <h3>Offerings</h3>
    pattern = re.compile(r'(<h3>Offerings</h3>\s*<ul>\s*)<li><a href="programs\.html#sat">.*?</ul>', re.DOTALL)
    new_ul = r"""\1<li><a href="programs.html#sat">SAT</a></li>
          <li><a href="programs.html#ielts">IELTS</a></li>
          <li><a href="programs.html#ap">AP Exams</a></li>
          <li><a href="programs.html#english">Profile Building</a></li>
          <li><a href="programs.html#enrichment">Admission Guidance</a></li>
        </ul>"""
    return pattern.sub(new_ul, content)

dropdown_old = """            <option>SAT Preparation</option>
            <option>IELTS Coaching</option>
            <option>AP Courses</option>
            <option>English Proficiency</option>
            <option>Academic Enrichment</option>"""

dropdown_new = """            <option>SAT</option>
            <option>IELTS</option>
            <option>AP Exams</option>
            <option>Profile Building</option>
            <option>Admission Guidance</option>"""

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()
    
    # 1. Update footer
    new_content = replace_footer(content)
    
    # 2. Update dropdown
    new_content = new_content.replace(dropdown_old, dropdown_new)
    
    if content != new_content:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")

