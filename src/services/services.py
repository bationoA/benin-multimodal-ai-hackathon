import os
import json
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from src.utils import load_json
from src.services import OpenAiModel
from deep_translator import GoogleTranslator

load_dotenv()

TASKS_PROMPTS = load_json(os.path.join("data", "tasks_prompt.json"))

if "ui-text-lang" not in st.session_state:
    st.session_state["ui-text-lang"] = "yoruba"


def custom_google_trans(text_to_translate: str, language_source: str, language_target: str):
    # By default, source language is detected automatically
    translator = GoogleTranslator(source=language_source, target=language_target)

    # Translate the text
    translated_text = translator.translate(text_to_translate)
    return translated_text


class Pipeline:
    def __init__(self, service_type: str = "info", user_query: str = "", openai_client: OpenAI = None):
        self.service_type = service_type
        self.openai_client = openai_client
        self.user_query = user_query
        self.user_translated_en_query = user_query
        self.text_completion_model = "gpt-3.5-turbo"
        self.image_generation_model = "dall-e-3"
        self.paragraphs = []
        self.texts_only_paragraphs_list = []
        #  Image to display when DALL-E rejects an image generation request
        self.default_url = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQAqAMBIgACEQEDEQH/xAAbAAEBAAMBAQEAAAAAAAAAAAAAAQQFBgMCB//EADYQAAIBAwICBwgABQUAAAAAAAABAgMEEQUhEjETFTVBcZKxIjJRVFVhc4EGM3KR0RQjRFJi/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AP0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZMlZMAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABk+K9WNGjOrPaMIuT/AEa2Oq3FSMZ09MryhJZi+JboDa5Bq+srv6VceZB6ld/SrjzIDaDJq+s7v6VceZDrK7+lXHmQG0yDVrUrv6VceZB6ndpNvS66SW/tIDZvmVI8LS4jd20K9NNRms4Z7pgGEGEBMFQCYBoBsAAMjIAAAAABjap2bdfil6HzpfZtr+KPofWqdm3X4peh86X2ba/iiBloMwdT1Gjp9LM/aqS92C7/ABNBa6/dwu+Ou1OjJ7wSxwr7AdY2km28YOUvNfu53D/08lTpReEuHLZ1FGrTuKUalKSnTmsprvOYvP4euVXm7XgnTk8rLw0ButF1B6hbSlUSVWDxLHJ/cza/8mp/S/Qw9H0/q+2cZSUqk3mbXLwMyt/Jqf0v0AwtB7Jt/B+psFzMDQOyrfwfqbAAwuQAE3KgAIygAQAAUEyVAARhAY+qdm3X4pehq56tSsNLtqcMTrulHEe6O3Nm01Ts26/FL0ODA9K9apXqyq1puc5Pds8wANjo+qT0+qoyzKhJ+1H4fdHXuvSVv07qR6HGePOx+fn30tTolS45dGnlRztkDdah/ENaVXhsv9unF+81lyNjp+r0r6hOnUxTr8D9nultzRyOCptbp4YHaaB2Vb+D9WbA1+gdlW/g/U2AAAAAAAAAEAAFAfIIAMkZ5qvTzPM1FQlwtyeN8ZA+b+nKtZV6UPenTkl44ON6p1Bf8Wq/0ds6tNRbdSCitm+JYQ6SntmpBcXu+0t/ADieqr/5Sr/YdVah8pV8p2/HBtxU4uS5pS3R5yuKajVlvik8S2A4zqrUPlKvlL1VqHylXynaqcOLhU4OS5riWUI1Kc/cnGS/8tMDieqtQ+Uq+UdVah8nV8p2yqU3JRVSGXyXEt/A843FNqTcuBRxly25geWkUKlvp1GlVWJxjuv2Zh5Rr0nUdNTXFs1vzT+BadenUjFqSXFnCk8NgegAAAAAAAIAAKCFQEZgyspSqTnJwcW5tJ/eKS9GZzCAwHZVI8PR9H7sE0tuSa54MaVvUo01Q4FOclFcm8e03tt/g3LCAwbaznSrqUsNRcnxcXPP2wWrb15SrU4dG6daSbk5Ycdl3d/IzQBgTsp8MnDo1NyqPLX/AGWx5qyrqNWUZRjUlKMoPOcYWH3fBmzJ3ga+VjU6Wn0fAqcJQcd+6P2xz/Z8xsa8Yxw4NJRT3w9ljng2YA1lGwrRioNUvdppzzvHh+A6vqcW7i00s+01jDb+BsyICgAAAAAAAjQAAr5BEyVAAGyZAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI+YXMrQSAMLkGEBComCoCMoaABkyUAAAAAAANgAO4mSgAMgATIyUATJUwADCAAmSpgAGwAB/9k="
        self.user_image_url = None

    def run(self):
        if self.service_type == "generate-image":
            # Generate an image for the paragraph
            try:
                task_prompt = TASKS_PROMPTS["user-generate-an-image"]

                task = OpenAiModel(
                    client=self.openai_client,
                    model=self.image_generation_model,
                    user_content=task_prompt + " " + self.user_query
                )
                # print(f"user-generate-an-image task: {task}")
                response = task.get_images_urls()
                self.user_image_url = response.data[0].url
            except BaseException as e:
                print(f"Error - generate-an-image: {e.__str__()}. Using default image for 'image not available'.")
                self.user_image_url = self.default_url

            return True

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
        response = OpenAiModel(
            client=self.openai_client,
            model=self.text_completion_model,
            prompt=task_prompt,
            user_content=self.user_translated_en_query)
        # response = task.get_message()

        if response is None:
            print("Error: a `None` response was returned")
            return "Error: a `None` response was returned"

        # Extract paragraphs
        print(f"task_prompt: {task_prompt}")
        print(f"user_translated_en_query: {self.user_translated_en_query}")
        is_paragraphs_extraction_succeed = True
        try:
            message = response.get_message()

            print(f"user_translated_en_query: {self.user_translated_en_query}")
            self.texts_only_paragraphs_list = [prg for prg in json.loads(message.content)]
        except:
            is_paragraphs_extraction_succeed = False

        if not is_paragraphs_extraction_succeed:
            try:
                message = response.get_message()
                self.texts_only_paragraphs_list = message.content.split("\n")
            except BaseException as e:
                print(f"Error - Extract paragraphs: {e.__str__()}")
                return f"Error - Extract paragraphs: {e.__str__()}"

        # Generate an image for each paragraph
        for paragraph_text in self.texts_only_paragraphs_list:
            # Generate prompt to generate image for each paragraph
            task_prompt = TASKS_PROMPTS["improve-paragraph-image-generation-prompt"]
            image_prompt_task = OpenAiModel(
                client=self.openai_client,
                model=self.text_completion_model,
                prompt=task_prompt,
                user_content=paragraph_text)
            paragraph_image_generation_prompt = image_prompt_task.get_message()

            if paragraph_image_generation_prompt is None:
                print("Error: a `None` response was returned for paragraph_image_generation_prompt")
                return "Error: a `None` response was returned for paragraph_image_generation_prompt"

            paragraph_image_generation_prompt = paragraph_image_generation_prompt.content
            # -- END: Generate prompt to generate image for each paragraph

            # Generate an image for the paragraph
            try:
                task_prompt = TASKS_PROMPTS["generate-an-image"]

                print(f"task_prompt: {task_prompt}")
                print(f"paragraph_image_generation_prompt: {paragraph_image_generation_prompt}")

                task = OpenAiModel(
                    client=self.openai_client,
                    model=self.image_generation_model,
                    prompt=task_prompt,
                    user_content=paragraph_image_generation_prompt
                )
                response = task.get_images_urls()
                image_url = response.data[0].url
            except BaseException as e:
                print(f"Error - generate-an-image: {e.__str__()}. Using default image for 'image not available'.")
                image_url = self.default_url

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
