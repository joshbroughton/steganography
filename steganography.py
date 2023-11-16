"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image

def decode_image(path_to_png):
    """
    Decodes the secret message from an image in which the the LSB of each pixel in the red
    channel maps directly to the pixel in the decoded image; that is, if the LSB is 0, the
    corresponding decoded pixel is (0, 0, 0), and if the LSB is 1, the decoded pixel is
    (255, 255, 255)
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]
    red_pixels = red_channel.load()

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    print(red_channel)  # Start coding here!
    for x in range(0, x_size):
        for y in range(0, y_size):
            if bin(red_pixels[x, y])[-1] == "0":
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x,y] = (255, 255, 255)

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

decode_image("encoded_sample.png")
