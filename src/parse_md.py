from typing import List
from pathlib import Path
from word import Word

def get_word_cards(md_path: Path) -> List[Word]:
    string = _read_md(md_path)
    return _parse_str(string)

def _read_md(md_path: Path) -> str:
    with open(md_path) as f:
        return f.read()

def _parse_str(md_str: str) -> List[Word]:
    lines = md_str.strip().split("\n")[2:]  # Erste zwei Zeilen überspringen (Header + Trennlinie)
    cards = [line.split("|")[1:-1] for line in lines]  # Spalten extrahieren und Rand-Spalten entfernen
    cards = [[q.strip(), a.strip()] for q, a in cards]  # Leerzeichen entfernen
    cards_words = [Word(s1, s2) for (s1,s2) in cards]
    return cards_words

if __name__ == "__main__":
    s = _read_md(Path("Adjektive.md"))
    cw = _parse_str(s)
