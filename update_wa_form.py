import glob

wa_script = """
    // Handle WhatsApp form submission
    document.querySelectorAll('.contact-form').forEach(form => {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        let name = form.querySelector('[name="Name"]')?.value || '';
        let email = form.querySelector('[name="Email"]')?.value || '';
        let phone = form.querySelector('[name="Phone"]')?.value || '';
        let program = form.querySelector('[name="Program of Interest"]')?.value || '';
        let comments = form.querySelector('[name="Comments"]')?.value || '';
        
        let text = `Hello Aurelius Academy, I have an enquiry:\n\n*Name:* ${name}\n*Email:* ${email}\n*Phone:* ${phone}\n*Program of Interest:* ${program}\n*Comments:* ${comments}`;
        
        let waUrl = `https://wa.me/919121473399?text=${encodeURIComponent(text)}`;
        window.open(waUrl, '_blank');
        
        const popupOverlay = document.getElementById('sidePopupOverlay');
        const sidePopup = document.getElementById('sidePopup');
        if(popupOverlay) popupOverlay.classList.remove('active');
        if(sidePopup) sidePopup.classList.remove('active');
        
        form.reset();
      });
    });
"""

for f in glob.glob("*.html"):
    with open(f, "r") as file_in:
        c = file_in.read()
    
    if "// Handle WhatsApp form submission" not in c:
        c = c.replace("})();\n</script>", wa_script + "\n  })();\n</script>")
        with open(f, "w") as file_out:
            file_out.write(c)
        print(f"Updated {f}")

