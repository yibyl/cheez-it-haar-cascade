import os

for ftype in ['negative']:
    for img in os.listdir(ftype):
        if ftype == 'negative':
            line = ftype + '/'+ img + '\n'
            with open('bg.txt', 'a') as f:
                f.write(line)