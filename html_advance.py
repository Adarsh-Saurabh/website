import os
import random

def generate_gallery_html(input_folder, num_images):
    # Get a list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Shuffle the image files randomly
    random.shuffle(image_files)

    # Select the specified number of random distinct images
    selected_images = image_files[:num_images]

    # Generate the HTML code for the gallery
    gallery_html = ""
    for i, image_file in enumerate(selected_images, start=1):
        image_path = os.path.join(input_folder, image_file)
        gallery_html += f'''
          <div class="col-xl-3 col-lg-4 col-md-6">
            <div class="gallery-item h-100">
              <img src="{image_path}" class="img-fluid" alt="">
              <div class="gallery-links d-flex align-items-center justify-content-center">
                <a href="{image_path}" title="Gallery {i}" class="glightbox preview-link"><i class="bi bi-arrows-angle-expand"></i></a>
                <a href="gallery-single.html" class="details-link"><i class="bi bi-link-45deg"></i></a>
              </div>
            </div>
          </div><!-- End Gallery Item -->
        '''

    return gallery_html

# Example usage
if __name__ == '__main__':
    input_folder = r"assets\img\gates"
    num_images = 20

    gallery_html = generate_gallery_html(input_folder, num_images)
    output_file = "gallery.txt"

    with open(output_file, 'w') as file:
        file.write(gallery_html)

    print(f"Gallery HTML saved to {output_file}")
