with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="miTabla"')
end = content.find('</table>', start) + len('</table>')
section = content[start:end]
print('thead count:', section.count('<thead>'))
print('thead close:', section.count('</thead>'))
print('tbody count:', section.count('<tbody>'))
print('tbody close:', section.count('</tbody>'))
print('tr open:', section.count('<tr>'))
print('tr close:', section.count('</tr>'))
print('Last 400 chars:', repr(section[-400:]))
