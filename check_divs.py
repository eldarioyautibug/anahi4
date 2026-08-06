with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Track div depth from line 408 (seccion-tabla-variables)
depth = 0
for i, line in enumerate(lines[407:1240], start=408):
    opens = line.count('<div')
    closes = line.count('</div>')
    depth += opens - closes
    if 'seccion-tabla-variables' in line or depth == 0 and i > 408:
        print(f"Line {i}: depth={depth} | {line.rstrip()[:100]}")
