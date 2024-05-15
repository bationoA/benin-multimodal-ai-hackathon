import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key="sk-proj-ebQPBisewWcHcOIEEV5hT3BlbkFJgCiZcvLt5WaKEWn56dGV")


class OpenAiModel:
    def __init__(self, model: str = "", prompt: str = "", user_content: str = "", image_size: str = "1024x1024",
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

        if self.prompt == "" or self.user_content == "":
            print(f"Error: Please provide `prompt` and `user_content`")
            return None

        if "dall" in self.model:
            print(f"Error: {self.model} is only image generation not text generation.")
            return None

        # print(f"self.model: {self.model}")
        # print(f"self.prompt: {self.prompt}")
        # print(f"self.user_content: {self.user_content}")

        completion = client.chat.completions.create(
            model=self.model,  # "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": self.user_content}
            ]
        )
        return completion.choices[0].message

    def get_images_urls(self):
        if self.prompt == "" or self.user_content == "":
            print("Error: Please provide `prompt` and `user_content`")
            return None

        if "dall" not in self.model:
            print(f"Error: {self.model} is only text generation not image generation.")
            return None

        response = client.images.generate(
            model="dall-e-3",
            prompt=self.prompt,
            size=self.image_size,
            quality=self.quality,
            n=self.num_images,
        )

        return response
