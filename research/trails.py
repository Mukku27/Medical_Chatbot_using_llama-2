import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trails.py",
    "app.py",
    "store_index.py",
    "static/.gitkeep",  # Ensure .gitkeep is handled as a file
    "templates/chat.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    # Check if it's a file and not a directory
    if not filepath.is_dir():
        # Create the file only if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, 'w') as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} already exists and is non-empty")
