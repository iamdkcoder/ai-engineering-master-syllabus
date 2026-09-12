# AI/ML Senior/Lead Engineer Master Syllabus

Problem-driven, just-in-time-mathematics curriculum designed for deep LLM expertise, then Recommendation/Retail, then Computer Vision.

This repository is a **syllabus inventory**, not a textbook. It contains ~299 Markdown modules across 33 numbered curriculum sections, published as a documentation website.

## Documentation architecture

```text
Markdown
  -> MkDocs
  -> Material for MkDocs
  -> GitHub Actions
  -> GitHub Pages
```

All curriculum content lives under [`docs/`](docs/index.md) and is built into a static site with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, then deployed to GitHub Pages automatically by GitHub Actions on every push to `main`.

## Local setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Serve locally

```bash
mkdocs serve
```

The site becomes available at <http://127.0.0.1:8000/>.

## Build

```bash
mkdocs build --strict
```

The static site is generated into `site/` (ignored by Git).

## Deployment

Pushes to the `main` branch trigger [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml), which builds the site with `mkdocs build --strict` and deploys it to GitHub Pages. The workflow can also be run manually via `workflow_dispatch`.

The site is intended to be hosted as a GitHub Pages **project site**:

```text
https://<username>.github.io/<repository-name>/
```

**One manual step required:** after creating the GitHub repository, uncomment and set `site_url` in [`mkdocs.yml`](mkdocs.yml) (and optionally `repo_url`) to match your actual GitHub username/repository name. `site_url` only affects canonical links and the sitemap — it is left unset by default so that `mkdocs serve` serves locally at the site root.

### Custom domain (optional)

GitHub Pages custom domains are configured via a `CNAME` file placed in `docs/` (MkDocs copies everything in `docs/` into the built site) plus the repository's Pages settings. No custom domain is configured by default.

## Editing curriculum

Curriculum content lives under [`docs/`](docs/index.md), organized into numbered section folders (`00_...` through `32_...`). Each section folder has an `index.md` landing page and one Markdown file per module. Edit files there and push through Git — folder/file numeric prefixes define ordering and must be preserved.

## Validating content

```bash
python scripts/validate_docs.py
```

Checks for duplicate filenames, missing section indexes, broken local Markdown links, missing H1 headings, and empty files.

## Repository layout

```text
repository-root/
├── README.md
├── mkdocs.yml
├── requirements.txt
├── .gitignore
├── docs/
│   ├── index.md
│   ├── 00_Curriculum_System/
│   ├── 01_Thinking_Like_an_AI_ML_Engineer/
│   └── ... (33 numbered curriculum sections)
├── scripts/
│   └── validate_docs.py
└── .github/
    └── workflows/
        └── deploy-docs.yml
```
