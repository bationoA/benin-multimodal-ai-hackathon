import json
import os
import streamlit as st
from dotenv import load_dotenv
from src.services import OpenAiModel
from src.utils import load_json
from deep_translator import GoogleTranslator

load_dotenv()

TASKS_PROMPTS = load_json(os.path.join("data", "tasks_prompt.json"))

if "ui-text-lang" not in st.session_state:
    st.session_state["ui-text-lang"] = os.getenv('DEFAULT_LANGUAGE')


def custom_google_trans(text_to_translate: str, language_source: str, language_target: str):
    # By default, source language is detected automatically
    translator = GoogleTranslator(source=language_source, target=language_target)

    # Translate the text
    translated_text = translator.translate(text_to_translate)
    return translated_text


class Pipeline:

    def __init__(self, user_query: str = ""):
        self.user_query = user_query
        self.user_translated_en_query = user_query
        self.text_completion_model = "gpt-3.5-turbo"
        self.image_generation_model = "dall-e-3"
        self.paragraphs = []
        self.texts_only_paragraphs_list = []

    def run(self):
        # Get user query
        if self.user_query == "":
            print("Error: Please provide a query (`user_query`)")
            return "Error: Please provide a query (`user_query`)"

        # Translate user query into English (If already not in English)
        if st.session_state["ui-text-lang"] != "english":
            self.user_translated_en_query = custom_google_trans(text_to_translate=self.user_query,
                                                                language_source=st.session_state["ui-text-lang"],
                                                                language_target="english"
                                                                )
        else:
            self.user_translated_en_query = self.user_query

        # Generate response in paragraphs
        task_prompt = TASKS_PROMPTS["create-maximum-of-3-paragraphs"]
        response = OpenAiModel(model=self.text_completion_model,
                               prompt=task_prompt,
                               user_content=self.user_translated_en_query)
        # response = task.get_message()

        if response is None:
            print("Error: a `None` response was returned")
            return "Error: a `None` response was returned"

        # Extract paragraphs
        try:
            message = response.get_message()
            self.texts_only_paragraphs_list = [prg for prg in json.loads(message.content)]
        except BaseException as e:
            print(f"Error: {e.__str__()}")
            return f"Error: {e.__str__()}"

        # Generate an image for each paragraph
        for paragraph_text in self.texts_only_paragraphs_list:
            # Generate prompt to generate image for each paragraph
            task_prompt = TASKS_PROMPTS["improve-paragraph-image-generation-prompt"]
            task = OpenAiModel(model=self.text_completion_model,
                               prompt=task_prompt,
                               user_content=paragraph_text)
            paragraph_image_generation_prompt = task.get_message()

            if paragraph_image_generation_prompt is None:
                print("Error: a `None` response was returned for paragraph_image_generation_prompt")
                return "Error: a `None` response was returned for paragraph_image_generation_prompt"

            paragraph_image_generation_prompt = paragraph_image_generation_prompt.content
            # -- END: Generate prompt to generate image for each paragraph

            # Generate prompt to generate image for each paragraph
            task_prompt = TASKS_PROMPTS["create-maximum-of-3-paragraphs"]
            task = OpenAiModel(model=self.image_generation_model,
                               prompt=task_prompt,
                               user_content=paragraph_image_generation_prompt)
            response = task.get_images_urls()
            image_url = response.data[0].url

            # Add to paragraphs text and images list
            self.paragraphs.append({
                "image_url": image_url,
                "text": paragraph_text
            })
        # END: Generate an image for each paragraph

        # Translate paragraphs back to selected language
        if st.session_state["ui-text-lang"] != "english":
            paragraphs_copy = self.paragraphs.copy()
            for i, paragraph in enumerate(paragraphs_copy):
                self.paragraphs[i]["text"] = custom_google_trans(text_to_translate=paragraph["text"],
                                                                 language_source="english",
                                                                 language_target=st.session_state["ui-text-lang"]
                                                                 )
        # END: Translate paragraphs back to selected language
        return True
