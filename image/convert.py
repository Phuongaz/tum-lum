from PIL import Image

def convert_image(input_path, output_path, output_format):
    try:
        image = Image.open(input_path)

        image.save(output_path, format=output_format)
        print("Image converted successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_path = input("Enter the input image path: ")
output_path = "output_image.png"
output_format = input("Enter the output format: ")
convert_image(input_path, output_path, output_format)