with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="miTabla"')
chunk = content[max(0, idx-3000):idx]
last_p = chunk.rfind('<p')
last_close_p = chunk.rfind('</p>')
print('Last p opens at offset:', last_p)
print('Last /p at offset:', last_close_p)
if last_p > last_close_p:
    line_num = content[:max(0,idx-3000)+last_p].count('\n')+1
    print('UNCLOSED p at approximately line', line_num)
    print('Context:', chunk[last_p:last_p+300])
else:
    print('No unclosed p before table - p is properly closed')
    
# Also check if the table is directly inside section or something invalid
pre = content[idx-500:idx]
print('\nContext 500 chars before table:')
for i, line in enumerate(pre.split('\n')):
    print(repr(line[:120]))
