import os
import pandas as pd
import streamlit as st
from openai import OpenAI

from src import default_pages_config, update_ui_text, format_an_upcoming_event_display, Pipeline, \
    format_user_image_display, sample_image_display
from src.page_format import format_article_display

st.session_state["ui-text-lang"] = "english"
update_ui_text()  # Load UI text translations

# --------------------- LOGO-TEXT AND TITLE
app_title = "Afe AI"
page_title = "AI-driven Tool for Record linkage in HDSS communities Within the INSPIRE Network"
page_description = "By Amos Bationo and Abdoul Aziz Maiga - Team <b><i>Unfold</i></b>"

default_pages_config(_title=page_title)

row_horizontal_menu = st.columns([2, 5, 2, 2])
language_names = ["English", "French", "Yoruba", "Fon"]
selected_language_name = row_horizontal_menu[3].selectbox(
    label="language",
    options=language_names,
    index=language_names.index(st.session_state["ui-text-lang"].capitalize()),
    label_visibility="visible"
)
if selected_language_name:
    st.session_state["ui-text-lang"] = selected_language_name.lower()
    update_ui_text()

row_horizontal_menu[0].image(image=os.path.join("assets", "images", "benin_mask.png"), width=200)

st.markdown(f"<h3 style='text-align:center; color: white; font-size: 2rem'>"
            f"{st.session_state['ui-text']['page_user_generate_images'].capitalize()}</h3>",
            unsafe_allow_html=True)
st.markdown(f"""
<h6 style='text-align: center; color: gray'>
{page_description}
</h6>""", unsafe_allow_html=True)
# --------------------- END LOGO-TEXT AND TITLE
pipeline = Pipeline()
if "openai-api-key" in st.session_state:
    pipeline = Pipeline(
        service_type="generate-image",
        openai_client=OpenAI(api_key=st.session_state["openai-api-key"])
    )

# BEGIN: Side bar

with st.sidebar:
    value = ""
    if "openai-api-key" in st.session_state:
        value = st.session_state['openai-api-key']

    with st.form(key="form-openai-api-key", clear_on_submit=False):
        st.text_input(
            label='Enter OpenAI API Key',
            key="openai-api-key",
            type="password",
            value=value
        )

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted and st.session_state['openai-api-key'] != "":
            st.success(f"API key Loaded: "
                       f"{st.session_state['openai-api-key'][0:4]}***{st.session_state['openai-api-key'][-4:]}")
# END: Side bar


# Display upcoming events
coming_events = pd.read_csv(os.path.join("data", "coming_events.csv"))
coming_events_to_display = []  # Will contain the image of the 1st paragraph and a truncated version of its beginning
for ind, event in coming_events.iterrows():
    event_paragraphs = []
    for paragraph_num in range(1, 4):
        if event[f"paragraph{paragraph_num}_text_{st.session_state['ui-text-lang']}"] != "":
            # Collect article' paragraphs
            event_paragraphs.append(
                {
                    "id": event['id'],
                    "image_name": event[f'paragraph{paragraph_num}_img_url'],
                    "text": event[f"paragraph{paragraph_num}_text_{st.session_state['ui-text-lang']}"],
                }
            )

    # Collect coming_events. Each article is a list of paragraphs
    coming_events_to_display.append(event_paragraphs)

row_coming_events = st.columns(len(coming_events_to_display))
for i, coming_event in enumerate(coming_events_to_display):
    first_paragraph = coming_event[0]
    html_ = sample_image_display(event=first_paragraph)
    row_coming_events[i].markdown(html_, unsafe_allow_html=True)

st.markdown(f"<br>", unsafe_allow_html=True)
st.markdown(f"""
<h6 style='text-align: center; color: gray'>{st.session_state['ui-text']['page_user_generate_sample_images']}</h6>""", unsafe_allow_html=True)

st.markdown(f"<br><br><br><br>", unsafe_allow_html=True)

st.markdown(f"""
<h3 style='text-align: center; color: white'>{st.session_state['ui-text']['page_user_generate_creative_images']}</h3>""", unsafe_allow_html=True)


# ------------ Queries
row_query_form = st.columns([1, 5, 1])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# React to user input
if prompt := st.chat_input(st.session_state['ui-text']["how_can_i_help_with_tourism_benin"]):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Collect user's query
    pipeline.user_query = prompt
    with st.spinner(f"{st.session_state['ui-text']['a_moment_please']}..."):
        pipeline.run()

    # response = f"Echo: {prompt}"
    response = format_user_image_display(pipeline.user_image_url)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
