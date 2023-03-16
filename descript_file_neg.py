import os

for ftype in ['negative']:
    for img in os.listdir(ftype):
        if ftype == 'negative':
            line = "cheez-it-haar-cascade/" + ftype + '/' + img + '\n'
            with open('bg1.txt', 'a') as f:
                f.write(line)
                f.write("\n")
