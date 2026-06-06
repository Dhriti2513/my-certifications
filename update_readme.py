import os

def generate_readme():
    content = """# Technical Certifications & Credentials Portfolio

This repository serves as an automated digital ledger of my academic and professional credentials. The catalog below is dynamically compiled directly from verified artifacts stored within this repository.

---

## ─── 📁 Verified Credentials & Achievements ───

| Credential / Event Name | Verification Link |
| :--- | :--- |
"""
    
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        files = sorted(os.listdir(assets_dir))
        for file in files:
            if file.startswith('.') or file.startswith('_'):
                continue
                
            filename_str, ext = os.path.splitext(file)
            clean_title = filename_str.replace('-', ' ').replace('_', ' ').title()
            
            # Expanded acronym mapping to cover your new competition certificates perfectly
            acronyms = {
                "Tcs": "TCS",
                "Ion": "iON",
                "Ai": "AI",
                "Llm": "LLM",
                "Ibm": "IBM",
                "Sih": "SIH",
                "Icat": "ICAT",
                "Gfg": "GeeksforGeeks",
                "Uipath": "UiPath",
                "Comsoc": "ComSoc",          # Correct capitalization for IEEE Computer Society context
                "Hacksynthesis": "HackSynthesis",
                "Tatacrucible": "Tata Crucible"
            }
            
            words = clean_title.split()
            fixed_words = [acronyms.get(word, word) for word in words]
            final_title = " ".join(fixed_words)
            
            content += f"| **{final_title}** | [View Certificate Image](assets/{file}) |\n"
            
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🚀 README.md successfully updated with all old and new milestones!")

if __name__ == '__main__':
    generate_readme()
