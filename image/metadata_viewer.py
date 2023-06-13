from PIL import Image

def view_image_metadata(image_path):
    try:
        image = Image.open(image_path)

        metadata = image.info
        for key, value in metadata.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

image_path = input("Enter the image path: ")
view_image_metadata(image_path)
