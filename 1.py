import cv2
import pytesseract
from sklearn.feature_extraction.text import CountVectorizer

# Step 1: Preprocess the image
image = cv2.imread('image.jpg', 0)  # Load the image in grayscale

# Step 2: Text detection (using OpenCV)
text_boxes = cv2.east_detect(image, conf_threshold=0.5)  # Perform text detection using EAST

# Step 3: Text recognition (using Tesseract OCR)
extracted_text = []
for box in text_boxes:
    x, y, w, h = box
    cropped_image = image[y:y+h, x:x+w]
    text = pytesseract.image_to_string(cropped_image)
    extracted_text.append(text)

# Step 4: Text processing (using sklearn)
vectorizer = CountVectorizer()
vectorized_text = vectorizer.fit_transform(extracted_text)
features = vectorizer.get_feature_names()

print(features)  # Print the extracted text as features
