import time
from data import image_names, number_of_images
from PIL import Image, ImageFilter

if __name__ == '__main__':
    start = time.perf_counter()

    for index, image_name in enumerate(image_names):
        print(f'Processing {index + 1}/{number_of_images}')
        with Image.open(f'images/{image_name}') as image:
            (width, height) = (image.width // 3, image.height // 3)
            image = image.filter(filter=ImageFilter.GaussianBlur(5))
            image = image.resize((width, height))
            image.save(f'processed_images/{image_name}')
            print(f'{image_name} was processed!')

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")
