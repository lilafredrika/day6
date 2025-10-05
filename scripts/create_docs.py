#!/usr/bin/env python3
"""
Simple script to scaffold docs from the local sphinx-template into a target project.
Usage: python scripts/create_docs.py /path/to/your/project "Project Name" "Author Name"
"""
import shutil
import sys
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / 'sphinx-template' / 'docs'


def main():
    if len(sys.argv) < 4:
        print("Usage: create_docs.py <target_dir> <project_name> <author_name>")
        sys.exit(1)
    target = Path(sys.argv[1])
    project_name = sys.argv[2]
    author_name = sys.argv[3]

    dest = target / 'docs'
    if dest.exists():
        print(f"Error: {dest} already exists")
        sys.exit(1)
    shutil.copytree(TEMPLATE_DIR, dest)

    # Replace placeholders in conf.py
    conf = dest / 'conf.py'
    text = conf.read_text()
    text = text.replace("PROJECT_NAME", project_name).replace("AUTHOR_NAME", author_name)
    conf.write_text(text)

    print(f"Docs scaffolded to {dest}")


if __name__ == '__main__':
    main()
