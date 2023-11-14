import os
import json
from pathlib import Path
from gpt_vision import GPTVision


def get_folder_path(root: str, code: str):
    sub_folder = code[:2] + "--"
    folder_path = os.path.join(root, sub_folder, code)

    if os.path.exists(folder_path):
        return folder_path
    else:
        return ""


def get_image_paths(folder_path: str):
    paths = []
    if os.path.exists(folder_path):
        images = Path(folder_path).glob('*.jpg')
        for image in images:
            paths.append(os.path.normpath(image))
    return paths


def write_results(ocr_response, folder_path):
    response_data = ocr_response.json()
    with open(os.path.join(folder_path, 'ocr_results.txt'), 'at+') as file:
        file.write(f"'created': {response_data['created']}\n")
        file.write(f"'model': {response_data['model']}\n")
        file.write(f"'usage': {str(response_data['usage'])}\n\n")
        file.write(response_data['choices'][0]['message']['content'])
        file.write("\n")


if __name__ == '__main__':

    ocr = GPTVision()
    test_root = "test_stories"
    test_no = "3212"
    folder = get_folder_path(test_root, test_no)

    if folder:
        image_paths = get_image_paths(folder)
        response = ocr(image_paths)
        print(response.json())
        write_results(response, folder)

