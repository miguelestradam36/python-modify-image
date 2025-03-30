from pillow_modules.imagemodifier import ImageManager

if __name__ == "__main__":
    Image_modifier = ImageManager()
    #Image_modifier.transpose_image_left(image_path="example.png", output_name="output.png")
    #Image_modifier.flip_image_down(image_path="example.png", output_name="output_1.png")
    Image_modifier.change_size(image_path="example.png", output_name="output_2.png", size_left=200, size_right=300)
    del Image_modifier



