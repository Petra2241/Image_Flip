import os
import sys
import copy

from PIL import Image

def flipimg(indir, outdir):
    for fname in os.listdir(indir):
        f = os.path.join(indir, fname)
        if os.path.isfile(f):
            try:
                im = Image.open(f)
                #print(f + " is a valid image file")
                print("Processing " + f)
                v_img = im.transpose(method=(Image.FLIP_TOP_BOTTOM))
                v_img.save(outdir + "\\" + fname)
            except IOError:
                print(f + " is not an image file")

def main():
    indir = sys.argv[1]
    #indir = "E:\\Development\\Granblue Fantasy Relink\\Junk"
    if os.path.isfile(indir):
        print("That is not a folder")
    else:
        if os.path.isdir(indir):
            try:
                outdir = indir + "\\_flipped"
                os.mkdir(outdir)
                flipimg(indir, outdir)
            except Exception as e:
                print(str(e))
                print("_flipped folder may already exist")


if __name__ == "__main__":
    main()
    input("\nPress any key to exit...")