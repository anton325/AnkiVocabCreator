from word import Word
from typing import List
import random
import genanki
from pathlib import Path

class AnkiCreator:
    def __init__(self, cards: List[Word], dir_name: str) -> None:
        self._cards = cards
        self._id = random.randint(0, 1000000000)
        self._dir_name = dir_name
        self._output_dir = Path("output")
        self._create_output_dir_if_necessary()

        self._model = genanki.Model(
            self._id,
            self._dir_name,
            fields=[{"name": "Frage"}, {"name": "Antwort"}],
            templates=[
                {
                    "name": "Karte 1",
                    "qfmt": "{{Frage}}",
                    "afmt": "{{FrontSide}}<hr id='answer'>{{Antwort}}",
                }
            ],
        )
    
    def _create_output_dir_if_necessary(self) -> None:
        if not self._output_dir.exists():
            self._output_dir.mkdir()
    
    def _generate_deck(self) -> None:
        self.deck = genanki.Deck(self._id, self._dir_name)

        # add words in both directions (i.e. native -> foreign language but also a card with foreign -> native language)
        notes = [genanki.Note(model=self._model, fields=[
            word_card.get_left_word(), word_card.get_right_word()]) for word_card in self._cards
            ]
        notes.extend([genanki.Note(model=self._model, fields=[
            word_card.get_right_word(), word_card.get_left_word()]) for word_card in self._cards
            ])
        for note in notes:
            self.deck.add_note(note)
    
    def _export_deck(self) -> None:
        genanki.Package(self.deck).write_to_file(Path(self._output_dir,f"{self._dir_name}.apkg"))

    def create(self):
        self._generate_deck()
        self._export_deck()