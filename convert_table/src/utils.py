import os
import re
from pathlib import Path

import pandas as pd
from rich import print


def load_data(this_schema):

    if not Path(this_schema).is_file():
        schema_info = get_schema_info(this_schema)
        input_file = get_input_file(schema_info)

    else:
        input_file = this_schema

    input_file = Path(input_file).resolve()

    print(f"[bold green]Loading: {str(input_file)}[/bold green]\n")

    return pd.read_csv(input_file, sep="\t")


def get_root_dir() -> Path:
    this_path = Path(__file__).parent.resolve()
    return this_path.joinpath("..", "..")


def get_input_dir(dir: Path = get_root_dir()) -> Path:
    return dir.joinpath("inputs", "tsv")


def get_input_file(schema_info: dict):
    input_dir = get_input_dir()
    basename = schema_info["basename"].tolist()[0]
    return os.path.join(input_dir, basename + ".tsv")


def get_metatable():
    metatable_file = get_input_dir().parent.joinpath("spreadsheet_google_id.tsv")
    return pd.read_csv(metatable_file, sep="\t")


def get_schema_info(this_schema):

    df = get_metatable()

    is_this_schema = df["schema"] == this_schema
    return df[is_this_schema]


def convert_to_str(df_field):
    return df_field.tolist()[0]


def convert_to_int(df_field):
    return int(df_field.tolist()[0])


def snake_case(input: str):
    return input.replace("\n", "").replace(" ", "_").replace(",", "")


def print_item_to_table(item_id: str, this_item: dict, item_info: dict, sep=" "):

    details = convert_to_str(this_item["details"])
    if isinstance(details, float):
        details = [str(details)]
    if details == ["nan"]:
        details = ""

    choices = item_info["choices"]
    if isinstance(choices, float):
        choices = [str(choices)]
    if "preset:boolean" in choices:
        choices = ["yes", "no"]
    if isinstance(choices, list):
        choices = "- " + "\n- ".join(choices)
    if choices == "- nan":
        choices = ""

    dict_to_print = {
        "item": item_id,
        "field": item_info["pref_label"],
        "question": item_info["question"],
        "options": choices,
        "instructions": details,
    }

    print(
        dict_to_print["item"]
        + sep
        + dict_to_print["field"]
        + sep
        + dict_to_print["question"]
        + sep
        + dict_to_print["options"]
        + sep
        + dict_to_print["instructions"]
    )

    return dict_to_print


def get_item_info(this_item: dict) -> dict:

    sub_section = ""
    if "sub_section" in this_item and this_item["sub_section"].any():
        sub_section = convert_to_str(this_item["sub_section"])

    item_name = set_item_name(this_item)
    if "item_pref_label" in this_item:
        pref_label = convert_to_str(this_item["item_pref_label"])
    else:
        pref_label = item_name

    pref_label = pref_label.replace("_", " ")

    description = pref_label
    if "item_description" in this_item and this_item["item_description"].any():
        description = convert_to_str(this_item["item_description"])

    unit = ""
    if "unit" in this_item and this_item["unit"].any():
        unit = convert_to_str(this_item["unit"])
        unit = split_choices(unit)

    details = ""
    if "details" in this_item and this_item["details"].any():
        details = convert_to_str(this_item["details"])

    question = convert_to_str(this_item["question"])
    question = question.replace("\n", "")

    field_type = convert_to_str(this_item["field_type"])
    if field_type == "integer":
        field_type = "int"

    choices = convert_to_str(this_item["choices"])
    choices = split_choices(choices)

    visibility = get_visibility(this_item)

    mandatory = get_mandatory(this_item)

    return {
        "name": item_name,
        "pref_label": pref_label,
        "description": description,
        "question": question,
        "details": details,
        "field_type": field_type,
        "choices": choices,
        "unit": unit,
        "visibility": visibility,
        "mandatory": mandatory,
        "sub_section": sub_section,
    }


def split_choices(choices) -> list:
    if type(choices) == str:
        choices = choices.split(" | ")
    return choices


def get_visibility(this_item: dict):

    visibility = convert_to_str(this_item["visibility"])

    if visibility in ["1", 1]:
        visibility = True

    elif visibility in ["0", 0]:
        visibility = False

    elif isinstance(visibility, float) and isnan(visibility):
        visibility = True

    else:
        # TODO
        # help with javascript expression input and validation
        return visibility

    return visibility


def get_mandatory(this_item: dict) -> bool:

    mandatory = convert_to_int(this_item["mandatory"])

    mandatory = mandatory >= 0

    return mandatory


def set_item_name(this_item: dict):

    if "item" not in this_item.keys():
        item_name = convert_to_str(this_item["item_pref_label"])

    elif isinstance(convert_to_str(this_item["item"]), float):
        item_name = convert_to_str(this_item["item_pref_label"])

    elif convert_to_str(this_item["item"]) == "":
        item_name = convert_to_str(this_item["item_pref_label"])

    else:
        item_name = convert_to_str(this_item["item"])

    item_name = snake_case(item_name)
    item_name = re.sub("[^-_a-zA-Z0-9]+", "", item_name)

    return item_name
