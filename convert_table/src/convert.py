import csv
from rich import print
from pathlib import Path
from utils import (
    get_item_info,
    get_metatable,
    get_root_dir,
    load_data,
    print_item_to_table,
)


def main():
    """
    Converts the different Artemis tables into a single TSV file.
    """
    sep = "\t"
    pattern = "artemis-"
    header = ["item", "field", "question", "options", "instructions"]

    output_file = Path(get_root_dir(), "outputs", "artemis.tsv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Initialize TSV file writer
    with open(output_file, "w", newline="") as tsv_file:
        writer = csv.DictWriter(tsv_file, fieldnames=header, delimiter="\t")

        # Write initial metadata description
        writer.writerow(
            {"item": "ARTEM-IS (Agreed Reporting Template for EEG Methodology - International Standard) template for ERP"}
        )
        writer.writeheader()

        # Load metatable schema and filter relevant tables
        metatable = get_metatable()
        tables_to_convert = metatable[metatable["schema"].str.contains(pattern)]
        table_names = tables_to_convert["basename"].tolist()
        table_schemas = tables_to_convert["schema"].tolist()

        # Loop through the tables and process each table's contents
        for schema, table_name in zip(table_schemas, table_names):
            data_frame = load_data(schema)

            # Identify unique activities and process them
            activities = data_frame["activity_order"].dropna().unique()
            for activity_idx in activities:
                activity_id = f"{activity_idx} - {table_name.upper()}"
                print(f"[bold red]{activity_id}[/bold red]")
                writer.writerow({"item": activity_id})

                activity_items = data_frame[data_frame["activity_order"] == activity_idx]
                included_items = activity_items[activity_items["include"] == 1]
                item_orders = included_items["item_order"].unique()

                sub_section = ""
                sub_section_id = 0

                # Process each item order within the activity
                for item_order in item_orders:
                    this_item = included_items[included_items["item_order"] == item_order]
                    item_info = get_item_info(this_item)

                    # Handle sub-section changes
                    if item_info["sub_section"] and item_info["sub_section"] != sub_section:
                        sub_section_id += 1
                        item_id = 0
                        sub_section = item_info["sub_section"]
                        subsection_id = f"{activity_idx}.{sub_section_id} - {sub_section.upper()}"
                        writer.writerow({"item": subsection_id})

                    # Increment item count and write the item to file
                    item_id += 1
                    item_id_str = f"{activity_idx}.{sub_section_id}.{item_id}"
                    item_row = print_item_to_table(item_id_str, this_item, item_info, sep)
                    writer.writerow(item_row)


if __name__ == "__main__":
    main()
