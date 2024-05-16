import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# if "openai-api-key" not in st.session_state:
#     st.session_state["openai-api-key"] = ""


class OpenAiModel:
    def __init__(self, model: str = "", prompt: str = "", user_content: str = "", image_size: str = "1024x1024",
                 quality: str = "standard", num_images: int = 1, client: OpenAI = None):
        """
        param: image_size: ['256x256', '512x512', '1024x1024', '1024x1792', '1792x1024']
        """
        self.client = client
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

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": self.user_content}
            ]
        )
        return completion.choices[0].message

    def get_images_urls(self):
        if self.prompt == "" and self.user_content == "":
            print("Error: Please provide `prompt` and/or `user_content`")
            return None

        if "dall" not in self.model:
            print(f"Error: {self.model} is only text generation not image generation.")
            return None

        print(f"get_images_urls-model: {self.model}")
        print(f"guser_content: {self.user_content}")
        response = self.client.images.generate(
            model=self.model,  # "dall-e-3",
            prompt=self.user_content,
            size=self.image_size,
            quality=self.quality,
            n=self.num_images,
        )

        return response
