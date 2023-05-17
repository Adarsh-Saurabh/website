# from PIL import Image
# import os

# def crop_images(input_folder, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Get a list of image files in the input folder
#     image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

#     for image_file in image_files:
#         # Open the image file
#         image_path = os.path.join(input_folder, image_file)
#         image = Image.open(image_path)

#         # Get the current width and height
#         width, height = image.size

#         # Calculate the new width and height with reversed aspect ratio
#         new_width = int(height * 4 / 3)
#         new_height = height

#         # Calculate the x-coordinate for cropping
#         x = (width - new_width) // 2

#         # Crop the image
#         cropped_image = image.crop((x, 0, x + new_width, new_height))

#         # Save the cropped image
#         output_path = os.path.join(output_folder, image_file)
#         cropped_image.save(output_path)

#         # Close the image
#         image.close()

# # Example usage
# if __name__ == '__main__':
        
#     i = r"C:\Users\adars\OneDrive\Desktop\Website\Image test"
#     output = r"C:\Users\adars\OneDrive\Desktop\Website\Image test1"

#     crop_images(i, output)





from PIL import Image, ImageFilter
import os
from PIL import Image, ImageOps
# import os

# Rest of the code remains the same...


def crop_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        # Open the image file
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        # Get the current width and height
        width, height = image.size

        # Calculate the new width and height with reversed aspect ratio
        new_width = int(height * 4 / 3)
        new_height = height

        # Calculate the x-coordinate for cropping
        x = (width - new_width) // 2

        # Crop the image
        cropped_image = image.crop((x, 0, x + new_width, new_height))

        # Add black padding to adjust aspect ratio
        padded_image = ImageOps.pad(cropped_image, (new_width, new_height))

        # Save the padded image
        output_path = os.path.join(output_folder, image_file)
        padded_image.save(output_path)

        # Close the images
        image.close()
        cropped_image.close()
        padded_image.close()

# Example usage
if __name__ == '__main__':
    input_folder = r"C:\Users\adars\OneDrive\Desktop\Website\Image test"
    output_folder = r"C:\Users\adars\OneDrive\Desktop\Website\Image test1"

    crop_images(input_folder, output_folder)




