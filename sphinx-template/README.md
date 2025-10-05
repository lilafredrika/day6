sphinx-template
================

This repository folder is a reusable Sphinx project template you can copy into new projects.

Contents
- `docs/` : Sphinx source (conf.py, index.rst, Makefile)
- `.github/workflows/docs.yml` : CI workflow to build and (optionally) deploy docs
- `docs/requirements.txt` : pinned dependencies for reproducible builds

How to use
1. Option A — new repo from this template (recommended):
   - On GitHub, create a new repository and copy the contents of this `sphinx-template` folder into it, or create an actual Template repository on GitHub and use "Use this template" to make new repos pre-populated.

2. Option B — copy into an existing project locally:
   ```bash
   cp -r sphinx-template/docs yourproject/
   cp -r sphinx-template/.github .github  # optional: copy CI workflow
   git add docs .github/workflows/docs.yml
   git commit -m "Add Sphinx docs from template"
   git push
   ```

3. Option C — use this folder as a starting point and edit `docs/conf.py` to set `project` and `author`.

Notes
- The CI workflow uses `docs/requirements.txt` to install pinned packages. Adjust versions as needed.
- To make a GitHub Template repo so others (or you) can click "Use this template" on GitHub, create a repository on GitHub and enable the "Template repository" option in the repository settings.

License: copy the license you want into new projects.
