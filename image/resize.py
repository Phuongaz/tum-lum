from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    try:
        with Image.open(input_image_path) as image:
            image.thumbnail(size)
            image.save(output_image_path)
            print(f"Image resized successfully. Output: {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_path = input("Enter the input image path: ")
output_path = "output.jpg"
new_size = input("Enter the new size (width, height): ").split(",")

resize_image(input_path, output_path, new_size)