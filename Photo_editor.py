#https://www.youtube.com/watch?v=vEQ8CXFWLZU
from PIL import Image, ImageEnhance, ImageFilter
import os

#For importing photo and exporting edited photo
path = r"\Users\MEMEMEMEME2\Documents\python_projects\Photo_editor\original"
pathout = r"\Users\MEMEMEMEME2\Documents\python_projects\Photo_editor\edited"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{pathout}/{clean_name}_edited.jpg")