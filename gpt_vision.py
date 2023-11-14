import os
import base64
import requests
from dotenv import load_dotenv


class GPTVision:
    # OpenAI API Key
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    def __call__(self, image_paths: list[str]):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        if len(image_paths) == 1:
            content = [
                {
                    "type": "text",
                    "text": "OCR this image for me. Do not warn about any difficulties interpreting the image."
                }
            ]
        else:
            content = [
                {
                    "type": "text",
                    "text": "OCR these images for me and concatenate the results together. Do not warn about any difficulties interpreting the images."
                }
            ]

        for image_path in image_paths:
            base64_image = self.encode_image(image_path)
            img_dict = {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
            content.append(img_dict)

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "max_tokens": 2048,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
        )
        return response

    # Function to encode the image
    @staticmethod
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
