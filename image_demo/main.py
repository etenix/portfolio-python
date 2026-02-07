import cv2
import numpy as np


def process_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found.")
        return

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Save result
    cv2.imwrite("output_edges.jpg", edges)

    print("Processing finished. Saved as output_edges.jpg")


if __name__ == "__main__":
    image_path = "sample.jpg"
    process_image(image_path)