import os
os.getcwd()
collection = "C:/Users/Billy Wei/OneDrive/Documents/GitHub/cheez-it-haar-cascade/pngout4"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:/Users/Billy Wei/OneDrive/Documents/GitHub/cheez-it-haar-cascade/pngout4/" + filename,
              "C:/Users/Billy Wei/OneDrive/Documents/GitHub/cheez-it-haar-cascade/pngout4/" + str(i + 4000) + filename[4:])