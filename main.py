from src import anki_export

anki_export.exportApkgFile(
    vocabularies=[
        {"hanzi": "做", "pinyin": "zuò", "translations": ["work", "make", "act"]}
    ],
    file="./asdf.apkg",
)
