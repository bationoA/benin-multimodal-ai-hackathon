import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from src.utils import load_json

load_dotenv()
client = OpenAI()


class OpenAiModel:
    def __init__(self, model: str, prompt: str, user_content: str, image_size: str = "1024x1024",
                 quality: str = "standard", num_images: int = 1):
        """
        param: image_size: ['256x256', '512x512', '1024x1024', '1024x1792', '1792x1024']
        """
        self.model = model
        self.prompt = prompt
        self.user_content = user_content
        self.image_size = image_size
        self.quality = quality
        self.num_images = num_images

    def get_message(self):
        if "dall" in self.model:
            return f"Error: {self.model} is only image generation not text generation."

        completion = client.chat.completions.create(
            model=self.model,  # "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": self.user_content}
            ]
        )
        return completion.choices[0].message

    def get_images_urls(self):
        if not "dall" in self.model:
            return f"Error: {self.model} is only text generation not image generation."

        response = client.images.generate(
            model="dall-e-3",
            prompt=self.prompt,
            size=self.image_size,
            quality=self.quality,
            n=self.num_images,
        )

        return response
        # return [response.data[i].url for i in range(len(response.data))]


print("Done.")
