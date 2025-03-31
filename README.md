# Anki Markdown Vocabulary Creator

This script reads markdown files from a specified directory and extracts vocabulary words formatted in a markdown table. It then automatically creates an Anki deck with translations in both directions.


## Expected Directory Structure and Markdown File Format
The script expects a directory that contains markdown files and/or directories that eventually contain markdown files. The markdown files are expected to be in the following format:

```markdown
| English  | Spanish  |
|----------|---------|
| Hello    | Hola    |
| Goodbye  | Adiós   |
```

## Usage
Edit line 7 in ```main.py``` to point towards the directory with the markdown files
```python
# example directory (maybe your language list is contained in an Obsidian vault)
path_to_md_dir = Path("User/Udo/Obsidian/Spanisch")
```

## Installation
Ensure you have Python installed. Then, clone this repository and install dependencies:

```sh
git clone <repository_url>
cd <repository>
pip install -r requirements.txt
python src/main.py
```
## Output
The script generates an Anki package (`.apkg`) file containing all parsed vocabulary words with translations in both directions in the output directory.

## License
This project is licensed under the MIT License.

