import os

def generate_readme():
    # Base structure and header of your README portfolio
    content = """# Technical Certifications & Credentials Portfolio

This repository serves as an automated digital ledger of my academic and professional credentials. The catalog below is dynamically compiled directly from verified artifacts stored within this repository.

---

## ─── 📁 Verified Credentials & Achievements ───

| Credential / Event Name | Verification Link |
| :--- | :--- |
"""
    
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        # Sort files alphabetically so the table stays neat
        files = sorted(os.listdir(assets_dir))
        for file in files:
            # Skip hidden system files or placeholder files
            if file.startswith('.') or file.startswith('_'):
                continue
                
            # Isolate the name from its extension
            filename_str, ext = os.path.splittext(file) if hasattr(os, 'splittext') else os.path.splitext(file)
            
            # Formatting logic: replace dashes/underscores with spaces and convert to Title Case
            clean_title = filename_str.replace('-', ' ').replace('_', ' ').title()
            
            # Dictionary mapping to ensure core technical acronyms are perfectly capitalized
            acronyms = {
                "Tcs": "TCS",
                "Ion": "iON",
                "Ai": "AI",
                "Llm": "LLM",
                "Ibm": "IBM",
                "Sih": "SIH",
                "Icat": "ICAT",
                "Gfg": "GeeksforGeeks",
                "Uipath": "UiPath"
            }
            
            # Apply acronym fixes word by word
            words = clean_title.split()
            fixed_words = [acronyms.get(word, word) for word in words]
            final_title = " ".join(fixed_words)
            
            # Append a highly scannable Markdown row to our main layout content string
            content += f"| **{final_title}** | [View Certificate Image](assets/{file}) |\n"
            
    # Open the existing README.md (or create it) and completely overwrite it with fresh data
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🚀 README.md successfully updated and rebuilt based on current assets!")

if __name__ == '__main__':
    generate_readme()
