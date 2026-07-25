with open('content.tex', 'r') as f:
    content = f.read()
content = content.replace('\r\n', '\n')

idx = content.find('Basis of a topological space}')
print('idx:', idx)
# Print the exact bytes around it
for i, c in enumerate(content[idx:idx+250]):
    if c == '\n':
        print(f'{i}: \\n')
    else:
        print(f'{i}: {c}')