import os
import sys
import uuid

import cv2
from flask import current_app
from PIL import Image
import pytesseract


def extract_text(filepath, image_preprocessing=None):
    """Does the image processing.

    Args:
        filepath (str): Path to image file
        image_preprocessing (str): Preprocessing method to apply; 
            can be 'raw', 'thresh', or 'blur'

    Returns:
        str: Extracted text
    """

    # Load the image and convert it to grayscale
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image preprocessing
    if image_preprocessing is not 'raw':

        # Apply threshold preprocessing
        if image_preprocessing is 'thresh':
            gray = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Apply median blurring to remove noise
        elif image_preprocessing is 'blur':
            gray = cv2.medianBlur(gray, 3)

    # Save the grayscale image as temporary PNG file
    fname = '-'.join([str(uuid.uuid4().hex)[:16], '-tmp.png'])
    fpath = os.path.join(
        current_app.config['UPLOAD_FOLDER'],
        fname
    )
    cv2.imwrite(fpath, gray)

    text = None
    try:
        # Load the image as a PIL image
        # then apply OCR
        text = pytesseract.image_to_string(Image.open(fpath))
    except Exception as e:
        print(f'{e}', file=sys.stderr)

    # Clean up
    if os.path.exists(fpath):
        os.remove(fpath)

    return text
