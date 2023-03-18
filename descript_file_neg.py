import os

for ftype in ['neg1']:
    for img in os.listdir(ftype):
        if ftype == 'neg1':
            line = "cheez-it-haar-cascade/" + ftype + '/' + img + '\n'
            with open('bg1.txt', 'a') as f:
                f.write(line)
                f.write("\n")
