from pathlib import Path
from typing import List


def get_list_of_md(dir: Path) -> List[Path]:
    mds = []
    for file in dir.iterdir():
        if ".md" in str(file):
            mds.append(file)
        elif file.is_dir():
            mds.extend(get_list_of_md(file))
    return mds