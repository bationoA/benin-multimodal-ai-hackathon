import os
import pandas as pd
import streamlit as st

# from src.utils.utils import get_column_display_name


def default_pages_config(_title=None, layout="wide"):
    st.set_page_config(page_title=_title,
                       page_icon=None,  # os.path.join("src", "images", "banner0.png"),
                       layout="wide" if layout == "wide" else "centered",
                       initial_sidebar_state="auto",
                       menu_items={"Get help": "mailto:amos.bationoo@gmail.com | maigaabdoulaziz000@gmail.com",
                                   "Report a Bug": "mailto:amos.bationoo@gmail.com | maigaabdoulaziz000@gmail.com",
                                   "About": None})

    hide_menu = """
    <style>
        #MainMenu{
            visibility: hidden
        }
        div.stApp > header{
            visibility: hidden #Visible
        }
    </style>
    """
    # st.markdown(hide_menu, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    remove_page_top_padding = """
        <style>
            .st-emotion-cache-z5fcl4{
                padding-top: 0;
            }
        </style>
    """
    st.markdown(remove_page_top_padding, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    content_style = """
        <style>
            h1.custom_title_h1{
                text-align:center;
                color: gray
            }
            h4.custom_setting_section_h4{
                color: gray
            }
            
        </style>
        
    """
    st.markdown(content_style, unsafe_allow_html=True)  # Add style to page content

    hide_footer = """
    <style>
        footer{
            visibility: hidden
        }
    </style>
    """
    st.markdown(hide_footer, unsafe_allow_html=True)  # Hiding the main menu (at the top-right)

    add_html_divider = """
        <style>
            hr {
              display: block;
              margin-top: 0.5em;
              margin-bottom: 0.5em;
              margin-left: auto;
              margin-right: auto;
              border-style: inset;
            }

            .main-title-divider{
              border-width: 10px;
            }

            .section-divider{
              border-width: 1px;
            }

            .domain-divider{
              border-width: 1px;
            }
        </style>
    """

    st.markdown(add_html_divider, unsafe_allow_html=True)


# def display_match(df: pd.DataFrame) -> None:
#     table_style = """
#         <style>
#             .centered_table {
#                 margin-left: auto;
#                 margin-right: auto;
#             }
#             h5{
#                 text-align: center;
#                 color: gray;
#             }
#             table {
#                 width: 50%;
#                 border-collapse: collapse;
#             }
#             table, th, td {
#                 border: 1px solid black;
#                 padding: 8px;
#                 text-align: left;
#             }
#             th {
#                 background-color: #f2f2f2;
#             }
#         </style>
#     """
#     table_content = table_style + f"<div><h5>Matching score: {df['score'].values[0]}</h5>" + \
#                     generate_one_vertical_table(df=df, table_style_classes=['centered_table'],
#                                                 hide_columns=['score']) + "</div>"
#
#     st.write(f"""{table_content}""", unsafe_allow_html=True)


# def generate_one_vertical_table(df: pd.DataFrame, table_style_classes: list = None, hide_columns: list = None) -> str:
#     """
#     Take a single row pandas dataframe and return its vertical-oriented html table representation in string format
#     :param df:
#     :param table_style_classes: List of CSS classes to include into the table
#     :param hide_columns: List of dataframe's columns to not include into the table
#     :return:
#     """
#     table_classes = " ".join(table_style_classes) if table_style_classes is not None else ""  # Extract CSS classes
#     hide_columns = hide_columns if hide_columns is not None else []
#     df = df[[col for col in df.columns if col not in hide_columns]]  # Hide columns in the list of `hide_columns`
#
#     table_start = f"<table class='{table_classes}'><tr><th></th><th>Value</th></tr>"
#     table_end = f"</table>"
#
#     table_rows = ""
#     for col in df.columns:
#         table_rows += "<tr><td>"
#         table_rows += get_column_display_name(col=col)
#         try:
#             table_rows += f"</td><td>{df[col].values[0]}</td></tr>"
#         except BaseException as e:
#             print(e.__str__())
#             st.write(e.__str__())
#
#     table = table_start + table_rows + table_end
#
#     return table


def main_page_design():
    mid_row_cols = st.columns([1, 2, 1, 2, 1])
    with mid_row_cols[1]:
        st.image(image=os.path.join("assets", "images", "form.webp"))

        with st.expander(label="Description"):
            st.write("""
            This feature provides a user-friendly interface for querying individual records within a Health and Demographic 
            Surveillance System (HDSS) dataset. Users can easily fill out a simple form with personal information fields, 
            such as First Name, Last Name, Date of Birth, and other relevant identifiers. Upon submission, the system 
            intelligently searches the HDSS dataset to find and display records that closely match the entered criteria. 
            """)
            # st.page_link(page=os.path.join("pages", "1_Form_Based.py"),
            #              label="CLICK HERE TO START",
            #              use_container_width=True)
        with st.expander(label="How to use"):
            st.write("""
                    <ul> 
                        <li><b>Access the Form</b>: Navigate to the form section of the application.</li>
                        <li><b>Enter Information</b>: Fill in the fields with the relevant information about the 
                    individual you're searching for. The more accurate and complete the information, the better the 
                    chances of finding an exact match.</li>
                        <li><b>Submit the Form</b>: Once you've entered all the necessary information, submit the form.
                        </li>
                        <li><b>Review Results</b>: The application will then present you with a list of matching records
                         from the HDSS dataset. Review the results to find the record that best matches the information 
                         you provided.</li>

                     </ul> 
                    """, unsafe_allow_html=True)


    with mid_row_cols[3]:
        st.image(image=os.path.join("assets", "images", "entries_list.webp"))

        with st.expander(label="Description"):
            st.write("""This advanced feature enables users to merge two separate datasets by identifying and linking 
            records that refer to the same individuals across both datasets. This process, known as record linkage, 
            is crucial for creating comprehensive datasets that can provide more holistic insights into the population's 
            health and demographics. The application employs sophisticated algorithms to accurately match records based 
            on shared attributes, while also allowing for minor discrepancies that may arise from data entry errors or 
            variations in record-keeping formats.
             """)

        with st.expander(label="How to use"):
            st.write("""<ul> 
            <li><b>Upload Datasets</b>: Start by uploading the two datasets you wish to merge. 
            Ensure that both datasets are in a compatible format as specified by the application guidelines.</li> 
            <li><b>Configure Linkage Parameters</b>: Set the parameters for the record linkage process, such as which 
            fields should be considered for matching (e.g., names, dates of birth) and the level of similarity 
            required for a match. This step may involve some trial and error to find the optimal settings for your 
            specific datasets.</li> 
            <li><b>Initiate the Linkage Process</b>: Once the datasets are uploaded and the 
            parameters are set, initiate the record linkage process. The system will process the datasets, 
            comparing records based on the criteria you've established.</li> 
            <li><b>Review and Finalize the Merged Dataset</b>: After the linkage process is complete, the application 
            will present you with a preview of the merged dataset, highlighting the linked records. Review the linkage 
            results for accuracy, making any necessary adjustments. Once satisfied, you can finalize the merged dataset,
             which will then be available for download or further analysis within the application.</li> 
             </ul> 
             """, unsafe_allow_html=True)

    page = f"""
    <p>
    An image as a link: <a href="{os.path.join('assets', 'images', 'banner0.png')}">
    <img border="0" alt="W3Schools" src="logo_w3s.gif" width="100" height="100">
    </a>
    </p>
    """

    # st.markdown(page, unsafe_allow_html=True)
