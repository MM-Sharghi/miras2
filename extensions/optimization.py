from config.settings import MEDIA_ROOT
from PIL import Image


def photo_optimization(image):
    try:
        image_url = f'{MEDIA_ROOT}\{image}'
        image = Image.open(image_url)
        image.save(image_url, quality=20, optimize=True)
        return 'optimized'
    except:
        return 'not optimized'