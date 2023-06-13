from PIL import Image

def generate_thumbnail(input_path, output_path, size=(128, 128)):
    try:
        image = Image.open(input_path)
        image.thumbnail(size)
        image.save(output_path)
        print("Thumbnail generated successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_path = input("Enter the input image path: ")
output_path = "thumbnail_image.jpg"
thumbnail_size = input("Enter the thumbnail size (width, height): ").split(",")
generate_thumbnail(input_path, output_path, size=thumbnail_size)