from src import anki_export
from pathlib import Path

# Export to Anki file
output_path = Path("./out")
output_path.mkdir(parents=True, exist_ok=True)
anki_export.exportApkgFile(
    vocabularies=[
        {"hanzi": "做", "pinyin": "zuò", "translations": ["work", "make", "act"]}
    ],
    file_path=Path("./out/deck.apkg"),
)
