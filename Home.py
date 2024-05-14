import os
import streamlit as st
from src.page_format import default_pages_config, main_page_design

# --------------------- LOGO-TEXT AND TITLE
page_title = "AI-driven Tool for Record linkage in HDSS communities Within the INSPIRE Network"
page_description = "By Amos Bationo and Abdoul Aziz Maiga - Team <b><i>Unfold</i></b>"

default_pages_config(_title=page_title)

row_banner = st.columns([2, 12, 1])
row_banner[1].image(image=os.path.join("assets", "images", "banner2.png"))
st.markdown(f"<h3 style='text-align:center; color: gray'>{page_title}</h3>",
            unsafe_allow_html=True)
st.markdown(f"""
<h6 style='text-align: center; color: gray'>
{page_description}
</h6>""", unsafe_allow_html=True)
# add divider
st.markdown("<hr class='main-title-divider'>", unsafe_allow_html=True)
# --------------------- END LOGO-TEXT AND TITLE

# --- Variables
is_form_valid = False
# --- End Variables


main_page_design()

