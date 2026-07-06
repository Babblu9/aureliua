import re

def get_section(content, start_marker, end_marker=None):
    if end_marker:
        pattern = re.compile(rf"({start_marker}.*?)(?={end_marker})", re.DOTALL)
    else:
        # If no end marker, just get the rest (or adapt as needed)
        pass
    match = pattern.search(content)
    if match:
        return match.group(1)
    return ""

def main():
    # 1. Read index.html
    with open('index.html', 'r') as f:
        idx_content = f.read()

    # Extract all sections from index.html
    navbar = get_section(idx_content, r'<!-- NAVBAR -->', r'<!-- HERO -->')
    hero = get_section(idx_content, r'<!-- HERO -->', r'<!-- 1 · ABOUT')
    about = get_section(idx_content, r'<!-- 1 · ABOUT', r'<!-- 2 · GLOBAL OUTLOOK')
    global_outlook = get_section(idx_content, r'<!-- 2 · GLOBAL OUTLOOK', r'<!-- 3 · ADVISORY PROCESS')
    advisory = get_section(idx_content, r'<!-- 3 · ADVISORY PROCESS', r'<!-- 4 · HOLISTIC DEVELOPMENT')
    holistic = get_section(idx_content, r'<!-- 4 · HOLISTIC DEVELOPMENT', r'<!-- 5 · PROGRAMS')
    programs = get_section(idx_content, r'<!-- 5 · PROGRAMS', r'<!-- 6 · WHY AURELIUS')
    why = get_section(idx_content, r'<!-- 6 · WHY AURELIUS', r'<!-- 7 · GLOBAL PATHWAYS')
    pathways = get_section(idx_content, r'<!-- 7 · GLOBAL PATHWAYS', r'<!-- 8 · FOUNDER')
    founder = get_section(idx_content, r'<!-- 8 · FOUNDER', r'<!-- ADMISSIONS CTA')
    cta = get_section(idx_content, r'<!-- ADMISSIONS CTA', r'<!-- 9 · CONTACT')
    contact_and_rest = get_section(idx_content, r'<!-- 9 · CONTACT', r'</body>') + "</body>\n</html>\n"

    # 2. Rebuild index.html
    new_idx_content = (
        navbar + 
        hero + 
        founder + 
        programs + 
        holistic + 
        global_outlook + 
        advisory + 
        pathways + 
        cta + 
        contact_and_rest
    )
    with open('index.html', 'w') as f:
        f.write(new_idx_content)
    print("Rebuilt index.html")

    # 3. Update about.html
    with open('about.html', 'r') as f:
        abt_content = f.read()
    
    # insert `about` right before <!-- PHILOSOPHY -->
    abt_content = abt_content.replace('  <!-- PHILOSOPHY -->', about + '\n  <!-- PHILOSOPHY -->')
    
    with open('about.html', 'w') as f:
        f.write(abt_content)
    print("Updated about.html")

    # 4. Update university.html
    with open('university.html', 'r') as f:
        uni_content = f.read()

    # insert `why` right before <!-- THE AURELIUS DIFFERENCE -->
    uni_content = uni_content.replace('  <!-- THE AURELIUS DIFFERENCE -->', why + '\n  <!-- THE AURELIUS DIFFERENCE -->')
    
    with open('university.html', 'w') as f:
        f.write(uni_content)
    print("Updated university.html")

if __name__ == '__main__':
    main()
