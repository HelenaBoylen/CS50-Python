# command prompt gives 2 arguments - both image names. Open, resize, crop  and overlay one on the other
import sys
from os.path import splitext
from PIL import Image, ImageOps

# check_arguments, check image, edit the image else exit out
def main():
    check_args()
    try:
        editimage()
    except FileNotFoundError:
        sys.exit()

# open the image, resize and paste onto the other image.
# This doesn't appear to work properly. The png pastes top left of other image
# If I add a box and a mask to position the png properly it looks fine but fails check50!
def editimage():
    with Image.open (sys.argv[1]) as photo:
            shirt = Image.open("shirt.png")
            size = shirt.size
            photo = ImageOps.fit(photo, size)
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])

# check the sys.argvs
def check_args():
    # check length of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")yealse:
        sys.exit("Invalid Output")
    if photo1[1] != photo2[1]:
        sys.exit("Input and output have different extensions")

# check the files are image files
def check_image(file):
    if file in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
        return True
    return False


if __name__ == "__main__":
    main()
