from parse_md import get_word_cards
from iterate_obsidian_dir import get_list_of_md
from anki_creator import AnkiCreator

from pathlib import Path

path_to_md_dir = Path("sample_files")

dir_name = path_to_md_dir.name
mds = get_list_of_md(path_to_md_dir)

print(f"Creating anki package for: {', '.join([md.name for md in mds])}")

cards = []
for md in mds:
    cards.extend(get_word_cards(md))

ak = AnkiCreator(cards, dir_name)
ak.create()