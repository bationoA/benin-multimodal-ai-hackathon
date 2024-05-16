# Benin Multimodal AI Hackathon


AFE AI is a generative AI system tailored for the promotion of local languages and tourism in Benin. Developed with a user-centric approach, the app offers an intuitive interface for local communities or tourists to prompt and gather information related to culture and tourism in Benin. The APP is built to support local languages such as Yoruba, Fon, and Dendi, which are the most common languages in Benin. It also supports international languages such as English and French. At this stage the system support only Yoruba, English and French; but we are working on fine-tuning LLM models to extends the languages to Fon and Dendi. The technologies under this system are ChatGPT for text generation, Dalle for image generation, and google translate for text translation. 

## Getting Started
There are two ways to access the application. First, follow these steps to starting using the app:

1. Clone the Git repository to your local machine:
```commandline
git clone git@github.com:bationoA/benin-multimodal-ai-hackathon.git
```

2. Navigate to the project directory:
```commandline
cd Team-Unfold-APHRC-DSE-inspire-hackathon-2024
```
3. Install the required packages from `requirements.txt`:
```commandline
pip install -r requirements.txt
```
4. Launch the Streamlit app:
```commandline
streamlit run Home.py
```

NOTE: A valid OpenAI API KEY is required to be able to use the app. 	

The second method is to use the link to the app which is hosted in Streamlit. You must also input a valid OpenAI API KEY to be able to run the app:
[Link to the hosted version](https://benin-multimodal-ai-hackathon-cudzxczsbxxv67jnnkjely.streamlit.app/).

## Key Features
The key features of the system are as follows:
* Generate Text related to tourism and culture in Benin 
* Generate Images to support the context of the generated text
* Use of local languages for Image and text generation.
* Provide a user-friendly interface to promote local languages and tourism in Benin

## Usage
1. Gather information about tourism and culture:
   * Navigate to the "home" page. 
   * Enter a request in the input field. 
   * Submit your request to get a response with the information related to your request followed by AI generated images to support the context of the generated text.
2. Generate only images:
   On the top menu there is link to the image only generation page. It allows you to generate images through prompts in local languages.
3. Explore the existing articles.
The system is designed so that some articles related to coming events, culture or tourism are display for users who would like to have important information or events related to tourism and culture in the country. 

## Some Outputs
![Example - Output 1](https://github.com/bationoA/benin-multimodal-ai-hackathon/blob/main/assets/images/output-1.png)

A result in Yoruba language:
![Example - Output 3](https://github.com/bationoA/benin-multimodal-ai-hackathon/blob/main/assets/images/output-2.png)
## License
This project is licensed under the [Creative Commons Attribution-NonCommercial (CC BY-NC) License](https://github.com/bationoA/Team-Unfold-APHRC-DSE-inspire-hackathon-2024/blob/new_feature_engineering/LICENCE/LICENCE.md).

## Feedback and Support
We welcome any feedback or suggestions for improving AFE AI App. For assistance or inquiries, please contact [amosb.dev@gmail.com](mailto:amosb.dev@gmail.com) or [maigaabdoulaziz000@gmail.com](mailto:maigaabdoulaziz000@gmail.com).
## Acknowledgments
We would like to express our gratitude to all contributors and developers who have contributed to the development and improvement of this app.
Amos BATIONO: [amosb.dev@gmail.com](mailto:amosb.dev@gmail.com)
Aboul-Aziz MAIGA: [maigaabdoulaziz000@gmail.com](mailto:maigaabdoulaziz000@gmail.com).
## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.
