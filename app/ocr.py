import pytesseract
from PIL import ImageGrab, Image, ImageDraw
import cv2
import numpy as np
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_extract_text(hide_window_callback=None, show_window_callback=None):
    if hide_window_callback:
        hide_window_callback()
        time.sleep(0.5)

    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

    data = pytesseract.image_to_data(screenshot, lang='eng', output_type=pytesseract.Output.DICT)
    draw = ImageDraw.Draw(screenshot)

    extracted_text = ""

    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60 and data['text'][i].strip() != '':
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            draw.rectangle([(x, y), (x + w, y + h)], outline="red", width=2)
            extracted_text += data['text'][i] + " "

    screenshot_with_boxes_path = "screenshot_highlighted.png"
    screenshot.save(screenshot_with_boxes_path)

    if show_window_callback:
        show_window_callback()

    img = cv2.imread(screenshot_with_boxes_path)
    cv2.namedWindow("OCR Result", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("OCR Result", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("OCR Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return extracted_text.strip()
