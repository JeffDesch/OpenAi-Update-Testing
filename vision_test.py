import os
from gpt_vision import GPTVision


def get_path(code: str):
    folder = code[:2] + "--"

    if os.path.exists(f"test_stories/{folder}/{code}"):
        if os.path.exists(f"test_stories/{folder}/{code}/Photo {code}.jpg"):
            return f"test_stories/{folder}/{code}/Photo {code}.jpg"
        elif os.path.exists(f"test_stories/{folder}/{code}/Photo {code} pg1.jpg"):
            return f"test_stories/{folder}/{code}/Photo {code} pg1.jpg"
    else:
        return ""


if __name__ == '__main__':
    test_no = "3212"
    ocr = GPTVision()
    img_path = get_path(test_no)
    if img_path:
        response = ocr(img_path)
        print(response.json())
