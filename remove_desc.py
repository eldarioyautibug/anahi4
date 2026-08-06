import re
import sys

html_file = r"c:\Users\HP\Desktop\anahi4\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div class="card-regresion-info">\s*<h4>.*?</h4>\s*)<p>.*?</p>(\s*<span class="btn-modelo-link">)')
new_content = pattern.sub(r'\1\2', content)

if new_content == content:
    print("No changes made. Pattern not found.")
    sys.exit(1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Descriptions removed successfully.")
