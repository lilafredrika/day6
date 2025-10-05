#!/usr/bin/env bash
set -e
REPO_NAME=${1:-sphinx-template}
DESCRIPTION=${2:-"Sphinx docs template (private)"}
OWNER="lilafredrika"

if command -v gh >/dev/null 2>&1; then
  echo "Creating private repo on GitHub via gh..."
  gh repo create "$OWNER/$REPO_NAME" --private --description "$DESCRIPTION" --source=. --remote=origin --push
  echo "Repository created and pushed: https://github.com/$OWNER/$REPO_NAME"
else
  cat <<MSG
GitHub CLI (gh) not found. To create a private repo and push, run these steps manually:

1) Create a new private repository on GitHub (https://github.com/new) named: $REPO_NAME
2) In this directory run:
   git remote add origin git@github.com:$OWNER/$REPO_NAME.git
   git branch -M main
   git push -u origin main

Or run this script again after installing the GitHub CLI (https://cli.github.com/).
MSG
fi
