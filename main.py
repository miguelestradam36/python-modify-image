from pillow_modules.imagemodifier import ImageManager

if __name__ == "__main__":
    Image_modifier = ImageManager()
    Image_modifier.transpose_image(image_path="example.png", output_name="output.png")
    del Image_modifier



