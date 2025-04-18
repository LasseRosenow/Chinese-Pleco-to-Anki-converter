import genanki
from typing import TypedDict
from pathlib import Path


class Vocabulary(TypedDict):
    hanzi: str
    pinyin: str
    translations: list[str]


def export_to_apkg_file(vocabularies: list[Vocabulary], file_path: Path):
    # Create model
    model = genanki.Model(
        model_id=1363295007,
        model_type=genanki.Model.FRONT_BACK,
        name="Hanzi -> English (Basic)",
        fields=[{"name": "Hanzi"}, {"name": "Pinyin"}, {"name": "Translations"}],
        templates=[
            {
                "name": "Basic",
                "qfmt": "{{Hanzi}}",
                "afmt": "{{FrontSide}}<hr>{{Pinyin}}<hr>{{Translations}}",
            }
        ],
    )

    # Create deck
    deck = genanki.Deck(deck_id=1176987201, name="Chinese", description="")

    # Add vocabularies to deck
    for vocabulary in vocabularies:
        deck.add_note(
            genanki.Note(
                model=model,
                guid=vocabulary["hanzi"] + vocabulary["pinyin"],
                fields=[
                    vocabulary["hanzi"],
                    vocabulary["pinyin"],
                    str(vocabulary["translations"]),
                ],
            )
        )

    # Write deck package to disk
    genanki.Package(deck).write_to_file(file_path)
