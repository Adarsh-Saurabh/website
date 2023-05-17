import os

def rename_images(folder_path):
    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg'))]

    # Rename the images
    for i, image_file in enumerate(image_files, start=1):
        original_path = os.path.join(folder_path, image_file)
        new_file_name = f"gallery-{i}.jpg"
        # new_file_name = f"gal-{i}.jpg"

        new_path = os.path.join(folder_path, new_file_name)
        os.rename(original_path, new_path)

# Example usage
if __name__ == '__main__':
    folder_path = r"C:\Users\adars\OneDrive\Desktop\Website\PhotoFolio\assets\img\gallery"

    rename_images(folder_path)





# ############################################################################

# import os
# import random
# import shutil

# def select_random_images(input_folder, output_folder, num_images=20):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Get a list of image files in the input folder
#     image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

#     # Select random distinct images
#     selected_images = random.sample(image_files, min(num_images, len(image_files)))

#     # Move the selected images to the output folder
#     for image_file in selected_images:
#         image_path = os.path.join(input_folder, image_file)
#         output_path = os.path.join(output_folder, image_file)
#         shutil.move(image_path, output_path)

# # Example usage
# if __name__ == '__main__':
#     input_folder = r"C:\Users\adars\OneDrive\Desktop\Website\Image test1"
#     output_folder = r"C:\Users\adars\OneDrive\Desktop\Website\PhotoFolio\assets\img\gallery"

#     select_random_images(input_folder, output_folder, num_images=20)
