import os

import pandas as pd
import streamlit as st
from src import default_pages_config, update_ui_text

st.session_state["ui-text-lang"] = "french"
update_ui_text()  # Load UI text translations

# --------------------- LOGO-TEXT AND TITLE
app_title = "Afe AI"
page_title = "AI-driven Tool for Record linkage in HDSS communities Within the INSPIRE Network"
page_description = "By Amos Bationo and Abdoul Aziz Maiga - Team <b><i>Unfold</i></b>"

default_pages_config(_title=page_title)

row_horizontal_menu = st.columns([1, 3, 2])
row_horizontal_menu[0].image(image=os.path.join("assets", "images", "benin_mask.png"), width=200)
row_horizontal_menu[1].markdown(f"<a href='#' class='main-horizontal-menu'>"
                                f"<h3 style='text-align:center;'>"
                                f"{st.session_state['ui-text']['tab_generate_image'].title()}</h3></a>"
                                , unsafe_allow_html=True)
row_horizontal_menu[2].markdown(f"<a href='#' class='main-horizontal-menu'>"
                                f"<h3 style='text-align:center;'>"
                                f"{st.session_state['ui-text']['trip_to_benin'].title()}</h3></a>"
                                , unsafe_allow_html=True)

st.markdown(f"<h3 style='text-align:center; color: white; font-size: 2rem'>"
            f"{st.session_state['ui-text']['banner_text'].capitalize()}</h3>",
            unsafe_allow_html=True)
st.markdown(f"""
<h6 style='text-align: center; color: gray'>
{page_description}
</h6>""", unsafe_allow_html=True)
# --------------------- END LOGO-TEXT AND TITLE

url_ = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-uU0tUas5UF6oz8bBffH8ohIl/user-V4pbgWclryyHb9RhiRu8LoLq/img-WwlwPfZius73f582vnNoyiVQ.png?st=2024-05-14T22%3A36%3A40Z&se=2024-05-15T00%3A36%3A40Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-14T22%3A26%3A15Z&ske=2024-05-15T22%3A26%3A15Z&sks=b&skv=2021-08-06&sig=Rt8rqWC1uiIZ09cY9cWZHCAKqMBycIYB%2BJ5BYl4kxy4%3D"
# Display Most popular articles
articles = pd.read_csv(os.path.join("data", "articles_history.csv"))
articles_to_display = []  # Will contain the image of the 1st paragraph and a truncated version of its beginning
for ind, article in articles.iterrows():
    articles_to_display.append(
        {
            "id": article['id'],
            "image_url": article['paragraph1_img_url'],
            "text": article['paragraph1_text'][0:10],  # Only the 1st 10 characters
        }
    )

row_articles_history = st.columns(3)

row_articles_history[0].markdown(f"""
    <div class="card" style="width: 28rem;">
        <img src="{articles_to_display[0]['image_url']}" style="height: 18rem;" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{articles_to_display[0]['text']}</h5>
            <p class="card-text">Starting on...</p>
        </div>
    </div>
""", unsafe_allow_html=True)

row_articles_history[1].markdown(f"""
    <div class="card" style="width: 28rem;">
        <img src="{articles_to_display[1]['image_url']}" style="height: 18rem;" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{articles_to_display[1]['text']}</h5>
            <p class="card-text">Starting on...</p>
        </div>
    </div>
""", unsafe_allow_html=True)

row_articles_history[2].markdown(f"""
    <div class="card" style="width: 28rem;">
        <img src="{articles_to_display[1]['image_url']}" style="height: 18rem;" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">{articles_to_display[1]['text']}</h5>
            <p class="card-text">Starting on...</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ------------ Queries
row_query_suggestions = st.columns(3)
row_query_suggestions[0].button(label=st.session_state['ui-text']['where_to_visit_in_benin'])
row_query_suggestions[1].button(label=st.session_state['ui-text']['can_you_tell_talk_about_benin'])
row_query_suggestions[2].button(label=st.session_state['ui-text']['what_are_tourist_places_in_benin'])

# st.text_input(label="", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")


# main_page_design()
