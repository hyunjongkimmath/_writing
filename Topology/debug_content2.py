with open('content.tex', 'r') as f:
    content = f.read()
content = content.replace('\r\n', '\n')

idx = content.find('Basis of a topological space}')
# Print more
for i, c in enumerate(content[idx:idx+350]):
    if c == '\n':
        print(f'{i}: \\n')
    else:
        print(f'{i}: {c}')