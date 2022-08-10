import gdown
from utils import get_input_dir


def main():

    google_id = "1dlUt8_bHsM5mERFJkVLTVWanSlms6Ba8Wos38Dhmhfo"

    output_dir = get_input_dir()

    output_dir.mkdir(parents=True, exist_ok=True)

    for id in sheet_ids():

        URL = f"https://docs.google.com/spreadsheets/d/{google_id}/export?format=tsv&gid={sheet_ids()[id]}"

        gdown.download(URL, output=str(output_dir.joinpath(f"{id}.tsv")))


def sheet_ids():

    return {
        "study_id": "1498151197",
        "hardware": "759849853",
        "acquisition": "724696342",
        "preprocessing": "1276614777",
        "design_sample": "2021971006",
        "measurement": "867147534",
        "channels": "75463838",
        "visualisation": "1616564910",
    }


if __name__ == "__main__":
    main()
