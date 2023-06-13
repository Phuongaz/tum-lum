from PIL import Image, ImageEnhance

def enhance_image(input_path, output_path, brightness=1.2, contrast=1.2, sharpness=1.2):
    try:
        # Open the input image
        image = Image.open(input_path)

        # Enhance the image
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)

        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)

        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness)

        # Save the enhanced image
        image.save(output_path)
        print("Image enhanced successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_path = input("Enter the input image path: ")
output_path = "enhanced_image.jpg"
brightness_factor = 1.2
contrast_factor = 1.2
sharpness_factor = 1.2
enhance_image(input_path, output_path, brightness=brightness_factor, contrast=contrast_factor, sharpness=sharpness_factor)