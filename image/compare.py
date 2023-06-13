from PIL import Image
from skimage.metrics import structural_similarity as ssim

def compare_images(image1_path, image2_path):
    try:
        image1 = Image.open(image1_path).convert("L")
        image2 = Image.open(image2_path).convert("L")

        similarity = ssim(image1, image2)

        print(f"SSIM: {similarity}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

image1_path = input("Enter the first image path: ")
image2_path = input("Enter the second image path: ")

compare_images(image1_path, image2_path)
