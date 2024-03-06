def visualize_opencv_image(img):
    import cv2
    import matplotlib.pyplot as plt

    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

def add_to_end_of_filename(filename, addition):
    import os
    name, ext = os.path.splitext(filename)
    return f"{name}_{addition}{ext}"

