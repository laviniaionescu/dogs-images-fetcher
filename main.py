import json

import cv2
import requests
import image_functions as img
import pdf_functions as pdf

def initialise_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialize project {e}")
        exit(1)
    return config


MENU = """
1. Generate new image
2. See all images
3. Pick an image from the list to see
"""




if __name__ == '__main__':

    config = initialise_config("config.json")
    # image_url = img.get_dog_image_url(config['rest_api_url'])
    # img.save_image(image_url)
    # img.show_images()

    # print(image_url)
    # pdf.create_pdf("pdf1.pdf")

    user_pick = int(input(MENU))
    if user_pick == 1:
        image_url = img.get_dog_image_url(config['rest_api_url'])
        img.save_image(image_url)