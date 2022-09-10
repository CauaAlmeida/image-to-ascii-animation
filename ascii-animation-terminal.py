import glob
import os
from PIL import Image
import time


def convert_image_to_ascii(filepath):
    """
    Converts an image to ASCII art.

    Parameters
    ----------
    filepath : str
        The path to the image to be converted.

    Returns
    -------
    ascii_image : str
        The converted ASCII art image.
    """

    # Open the image and convert it to grayscale.
    image = Image.open(filepath).convert("L")

    # Resize the image.
    width, height = image.size
    aspect_ratio = height / width
    new_width = 100
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((new_width, int(new_height)))

    # Convert the image to ASCII characters.
    pixels = image.getdata()
    chars = '`^\,:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    # Split the ASCII characters into multiple lines.
    new_image = [new_pixels[index: index + new_width] for index in range(0, len(new_pixels), new_width)]

    return "\n".join(new_image)


def play_ascii_animation(folder_path):
    """
    Plays an ASCII art animation from a folder of images.

    Parameters
    ----------
    folder_path : str
        The path to the folder containing the images.
    """

    # Get a list of all the images in the folder.
    image_files = glob.glob(os.path.join(folder_path, "*.jpg"))
    image_files.sort(key=lambda x: int(os.path.split(x)[1].split(".")[0]))

    # Play the animation.
    for image_file in image_files:
        ascii_image = convert_image_to_ascii(image_file)
        print(ascii_image)
        time.sleep(0.1) # Add a delay between frames.
        os.system('cls' if os.name == 'nt' else 'clear')

    return None


if __name__ == "__main__":
    folder_path = "images"
    play_ascii_animation(folder_path)
