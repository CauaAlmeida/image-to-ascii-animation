# Image to ASCII Converter

This is a Python script that converts images to ASCII art and plays them as an animation. The script utilizes the Python Imaging Library (PIL) to process the images and generate the ASCII representation.

## TOC
<!--ts-->
   * [Requirementes](#Requirements)
   * [Usage](#Usage)
   * [Functionality](#Functionality)
      * [convert_image_to_ascii(filepath)](#convert_image_to_ascii(filepath))
      * [play_ascii_animation(folder_path)](#play_ascii_animation(folder_path))
   * [Example](#Example)
   * [Contributing](#Contributing)
<!--te-->

## Requirements
- Python 3.x
- PIL (Python Imaging Library)

## Usage
1. Make sure you have Python installed on your system.
2. Install the required PIL library by running the following command:
```
 pip install pillow
```
3. Save the script to a file with a .py extension, e.g., image_to_ascii.py.
4. Create a folder named images in the same directory as the script.
5. Place the images you want to convert to ASCII art in the images folder. Ensure that the images are in .jpg format.
6. Open a command prompt or terminal and navigate to the directory containing the script and the images folder.
7. Run the script using the following command:
```
python image_to_ascii.py
```
8. The script will convert the images in the images folder to ASCII art and display them as an animation in the console.

Note: The ASCII animation may vary in appearance depending on the console or terminal used.

## Functionality

The script provides the following functions:

### convert_image_to_ascii(filepath)
This function takes the path to an image file as input and converts the image to ASCII art.

Parameters
- filepath (str): The path to the image file to be converted.
Returns
- ascii_image (str): The converted ASCII art image.

### play_ascii_animation(folder_path)

This function plays an ASCII art animation using a folder of images. It converts each image in the folder to ASCII art and displays them in sequence.

Parameters
- folder_path (str): The path to the folder containing the images.

## Example

```python

from image_to_ascii import play_ascii_animation

if __name__ == "__main__":
    folder_path = "images"
    play_ascii_animation(folder_path)

```
In this example, the script is imported as a module, and the play_ascii_animation function is called with the path to the images folder. The script will convert the images in the folder to ASCII art and play them as an animation.

## Contributing
Contributions to this repository are welcome. If you find any issues or want to propose improvements, feel free to create a pull request or submit an issue.


## License
VIRAL PUBLIC LICENSE
Copyleft (ɔ) All Rights Reversed

This WORK is hereby relinquished of all associated ownership, attribution and copy rights, and redistribution or use of any kind, with or without modification, is permitted without restriction subject to the following conditions:

1. Redistributions of this WORK, or ANY work that makes use of ANY of the contents of this WORK by ANY kind of copying, dependency, linkage, or ANY other possible form of DERIVATION or COMBINATION, must retain the ENTIRETY of this license.
2. No further restrictions of ANY kind may be applied.



https://user-images.githubusercontent.com/60367135/200193332-058798fb-6775-4295-81c7-01f764a7c69a.mp4

![20220905_153515](https://user-images.githubusercontent.com/60367135/200193368-dc2675c5-15b1-40dc-993a-2855636d33e6.jpg)
