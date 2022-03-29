from PIL import Image

widthinput = int(200)  # <------ This is the size of the image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=widthinput):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return (characters)


def main(new_width=widthinput):
    path = input("Enter a valid pathname to an image:\n")

    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pix = len(new_image_data)
    newimage = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pix, new_width)])

    print(newimage)

    with open("ascii_image.txt", "w") as f:
        f.write(newimage)


main()
