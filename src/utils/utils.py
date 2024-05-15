import base64
import json
import os
import pandas as pd
import streamlit as st
from datetime import datetime


# Function to encode image to base64
@st.cache_resource
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


@st.cache_resource
def get_article_image_base64(filename: str):
    # Path to the image
    image_path = os.path.join('assets', 'images', 'articles', filename)

    return get_image_base64(image_path)


def update_ui_text():
    if "ui-text-lang" not in st.session_state:
        st.session_state["ui-text-lang"] = "english"

        # For jupyter-notebook
        ui_text_df = pd.read_csv(os.path.join("data", "static-translations.csv"))

        st.session_state["ui-text"] = \
            {row["message"]: row["english"] for ind, row in ui_text_df.iterrows()}
        return

    ui_text_df = pd.read_csv(os.path.join("data", "static-translations.csv"))

    st.session_state["ui-text"] = \
        {row["message"]: row[st.session_state["ui-text-lang"]] for ind, row in ui_text_df.iterrows()}


def save_to_json(obj: list | dict, filepath: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def load_json(filepath: str) -> json:
    with open(filepath, 'r') as f:
        file = json.load(f)

    return file


def auto_detect_date_format(date_str):
    """
    Detect and return the format of date.

    :param date_str:
    :return:
    """
    # List of common date formats to try
    common_formats = [
        "%Y-%m-%d %H:%M:%S",  # e.g., 2021-03-27 13:45:00
        "%Y-%m-%d %H:%M",  # e.g., 2021-03-27 13:45
        "%Y-%m-%d",  # e.g., 2021-03-27
        "%d/%m/%Y %H:%M:%S",  # e.g., 27/03/2021 13:45:00
        "%d/%m/%Y %H:%M",  # e.g., 27/03/2021 13:45
        "%d-%m-%Y %H:%M",  # e.g., 27-03-2021 13:45
        "%d/%m/%Y",  # e.g., 27/03/2021
        "%m/%d/%Y",  # e.g., 03/27/2021
        "%d-%m-%Y",  # e.g., 27-03-2021
        "%m-%d-%Y",  # e.g., 03-27-2021
        "%b %d, %Y",  # e.g., Mar 27, 2021
        "%d %b, %Y",  # e.g., 27 Mar, 2021
        "%B %d, %Y",  # e.g., March 27, 2021
        "%d %B, %Y",  # e.g., 27 March, 2021
    ]

    for fmt in common_formats:
        try:
            # If the date string matches the format, return the format
            if datetime.strptime(str(date_str), fmt):
                return fmt
        except ValueError:
            # If the date string does not match the format, try the next format
            continue

    # If no format matches, return None or raise an error
    return None


def value_by_index(list_: list, ind: int):
    return list_[ind]


def get_index_of_max_value(series: list, return_max_val=False) -> int | tuple:
    series = list(series)
    max_value = max(series)
    index_ = series.index(max_value)
    if return_max_val:
        return index_, max_value
    else:
        return index_


def decimal_to_percentage(decimal_number: float) -> str:
    """
    Convert decimal value into percentages (string format)
    :param decimal_number:
    :return:
    """
    # Convert the decimal number to a percentage string with 2 decimal places
    percentage_string = "{:.2%}".format(decimal_number)
    return percentage_string


def missing_in_list(list1: list, list2: list) -> list:
    """
    Return items of list1 that are missing in list2
    :param list1:
    :param list2:
    :return:
    """
    return [ll for ll in list1 if ll not in list2]


def merge_dataframes_on_recnr(df1: pd.DataFrame, df2: pd.DataFrame, pairs_recnr_list: list) -> pd.DataFrame:
    """
    Merge two pandas DataFrames using the pairs of record numbers `recnr`
    :param df1:
    :param df2:
    :param pairs_recnr_list:
    :return:
    """
    # Create an empty DataFrame for the result
    merged_df = pd.DataFrame()

    # Get list of common columns
    common_cols = [c for c in df1.columns if c in df2.columns]

    # Rename the common columns differently with respect to the df1 and df2
    rename_cols_df1 = {c: f"{c}_1" for c in common_cols}
    rename_cols_df2 = {c: f"{c}_2" for c in common_cols}

    df1 = df1.rename(columns=rename_cols_df1)  # Rename for df1
    df2 = df2.rename(columns=rename_cols_df2)  # Rename for df2

    # Loop through each pair in the list
    for recnr1, recnr2 in pairs_recnr_list:
        # Find the row in df1 that matches recnr1
        row_df1 = df1[df1['recnr_1'] == recnr1]

        # Find the row in df2 that matches recnr2
        row_df2 = df2[df2['recnr_2'] == recnr2]

        # Make sure both rows are found
        if not row_df1.empty and not row_df2.empty:
            # Reset index to facilitate the merge
            row_df1.reset_index(drop=True, inplace=True)
            row_df2.reset_index(drop=True, inplace=True)

            # Merge the two rows into one row
            merged_row = pd.concat([row_df1, row_df2], axis=1)

            # Append the merged row to the result DataFrame
            merged_df = pd.concat([merged_df, merged_row], ignore_index=True)

    return merged_df


def get_now_utc_timestamp() -> float:
    return datetime.utcnow().timestamp()  # Get the current timestamp in seconds since the


def get_remaining_time_estimate(start_timestamp: float, total_assessed: int, total_to_assess: int) -> str:
    """
    This function return the elapsed time between a given starting timestamp and the current timestamp.
    The elapsed time is in a str format
    :param start_timestamp:
    :param total_assessed:
    :param total_to_assess:
    :return: y:m:d:h:m:s  # year:month:day:hour:minute:seconds
    """

    estimate_remaining_time = ":hourglass_flowing_sand: "
    if not total_assessed > 0:
        estimate_remaining_time += "..."
    else:

        elapsed_time_sec = get_now_utc_timestamp() - start_timestamp

        average_download_speed = total_assessed / elapsed_time_sec  # number of downloaded files per seconds
        remaining_time_sec = (total_to_assess - total_assessed) / average_download_speed  # in seconds
        estimate_remaining_time += format_remaining_time(time_seconds=remaining_time_sec)

    return estimate_remaining_time


def format_remaining_time(time_seconds: float, next_unite: str = "Y", result: str = "") -> str:
    unites = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "D": 24 * 60 * 60,
        "M": 30 * 24 * 60 * 60,
        "Y": 12 * 30 * 24 * 60 * 60,
    }
    current_unit = next_unite

    unite = unites[current_unit]
    tm = time_seconds / unite

    if int(tm) >= 1:
        tm = int(tm)
        result += f"{tm}{current_unit}:" if tm >= 10 else f"0{tm}{current_unit}:"
        time_seconds -= tm * unite

    if current_unit != "s":
        unite_keys_list = list(unites.keys())
        current_unite_index = unite_keys_list.index(current_unit)
        next_unite = unite_keys_list[current_unite_index - 1]

        return format_remaining_time(time_seconds=time_seconds, next_unite=next_unite, result=result)

    return result.removesuffix(":") if result else "0"


def get_concurrent_items_list(list_items: list, nbr_simult: int) -> list:
    """
    Take a list returns a list of mutually exclusive sublist of length less or equal to nbr_simult

    :param: list_items: List of documents to be downloaded
    :param: nbr_simult: Maximum number of documents to be downloaded simultaneously
    """

    nbr_simult = 1 if nbr_simult < 1 else nbr_simult

    nbr_iterations = len(list_items) / nbr_simult
    nbr_iterations = int(nbr_iterations) + 1 if nbr_iterations > int(nbr_iterations) else int(nbr_iterations)
    result = []
    for sub_index in range(nbr_iterations):
        start_ind = sub_index * nbr_simult if sub_index > 0 else 0
        sub_list = list_items[start_ind:start_ind + nbr_simult]
        result.append(sub_list)

    return result


def get_column_display_name(col: str) -> str:
    """
    Return the formatted version of columns names
    :param col:
    :return:
    """
    column_display_name_dict = {
        "recnr": "Record Number",
        "firstname": "First Name",
        "lastname": "Last Name",
        "petname": "Pet-Name / Nickname",
        "sex": "Sex",
        "dob": "Date of Birth",
        "hdssid": "HDSS ID",
        "hdsshhid": "HDSSH ID",
        "visitdate": "Visit Date",
        "nationalid": "National ID",
        "patientid": "Patient ID",
    }

    return column_display_name_dict[col] if col in column_display_name_dict else col


def is_defined(var_name: str, gbl, lcl) -> bool:
    """
    Returns True if the provided variable is defined. False otherwise
    :param var_name:
    :param gbl: globals()
    :param lcl: locals()
    :return:
    """
    return var_name in gbl or var_name in lcl


def add_s_plural(num: int) -> str:
    """
    Returns `s` if `num` is greater than 1. Empty string otherwise
    :param num:
    :return:
    """
    return "s" if num > 1 else ""
