class ImageManager():
    def __init__(self):
        print("Starting the transformation of images...")

    def transpose_image_left(self, image_path:str, output_name:str)->None:
        from PIL import Image
        Image.open(image_path)
        output_image = Image.open(image_path)
        mirror_image = output_image.transpose(Image.FLIP_LEFT_RIGHT)
        mirror_image.save(output_name)
    
    def flip_image_down(self, image_path:str, output_name:str)->None:
        from PIL import Image
        Image.open(image_path)
        output_image = Image.open(image_path)
        mirror_image = output_image.transpose(Image.FLIP_TOP_BOTTOM)
        mirror_image.save(output_name)  

    def change_size(self, image_path:str, output_name:str, size_left:int, size_right:int)->None:
        from PIL import Image, ImageOps
        size = (size_left, size_right)
        with Image.open(image_path) as im:
            ImageOps.contain(im, size).save(output_name)
    
    def change_contrast(self, image_path:str, contrast:float)->None:
        from PIL import ImageEnhance
        enh = ImageEnhance.Contrast(image_path)
        enh.enhance(contrast).show("{}% more contrast".format(contrast))

    def __del__(self):
        print("Finished the image transformation...")