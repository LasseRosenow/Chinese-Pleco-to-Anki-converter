from src import pleco_import, anki_export
from pathlib import Path

# Import Pleco vocabularies
pleco_input_path = Path("./input/pleco.xml")
chinese_characters = pleco_import.parse_xml_file(pleco_input_path)


# Export to Anki file
output_path = Path("./output")
output_path.mkdir(parents=True, exist_ok=True)
anki_export.export_to_apkg_file(
    vocabularies=[
        {"hanzi": "做", "pinyin": "zuò", "translations": ["work", "make", "act"]}
    ],
    file_path=Path("./output/deck.apkg"),
)
