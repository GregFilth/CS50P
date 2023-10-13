import sys, os
from PIL import Image, ImageOps

def main():

    if len(sys.argv) == 3:
        # get the extensions
        ext1 = os.path.splitext(sys.argv[1])[1]
        ext2 = os.path.splitext(sys.argv[2])[1]

        # if proper extensions are used
        if not ((ext1 == ".jpg" or ext1 == ".jpeg" or ext1 == ".png") and (
            ext2 == ".jpg" or ext2 == ".jpeg" or ext2 == ".png")
        ):
            sys.exit("Invalid output")

        # if extensions match
        if ext1 == ext2:

            try:
                # open file
                base_picture = Image.open(sys.argv[1])
                shirt = Image.open("shirt.png")

            except FileNotFoundError:
                sys.exit("Input does not exist")
            else:

                # ImageOps.fit
                new_pic = ImageOps.fit(base_picture, (shirt.size))

                # resize()
                new_pic = new_pic.resize((600, 600))


                # paste()
                new_pic.paste(shirt, shirt)

                # save()
                new_pic.save(sys.argv[2])


        else:
            sys.exit("Input and output have different extensions")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
