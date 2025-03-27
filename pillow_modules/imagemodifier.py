class ImageManager():
    def __init__(self):
        print("Starting the transformation of images...")

    def transpose_image(self, image_path:str, output_name:str)->None:
        from PIL import Image
        Image.open(image_path)
        output_image = Image.open(image_path)
        mirror_image = output_image.transpose(Image.FLIP_LEFT_RIGHT)
        mirror_image.save(output_name)

    def __del__(self):
        print("Finished the image transformation...")