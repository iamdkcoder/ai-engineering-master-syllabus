I have an existing local Markdown knowledge-base / curriculum repository that I want to convert into a professional documentation website using **MkDocs + Material for MkDocs**, and later host for free using **GitHub Pages**.

My existing curriculum folder is located at:

`<LOCAL_CURRICULUM_PATH>`

The repository already contains a large hierarchical folder structure with approximately 299 Markdown files and 260 learning modules.

The content itself is already prepared. Your job is primarily **documentation-site engineering**, not rewriting the curriculum.

# Primary Objective

Transform the existing Markdown repository into a clean, maintainable, production-ready documentation website with this architecture:

```text
GitHub Repository
        ↓
MkDocs
        ↓
Material for MkDocs
        ↓
GitHub Actions
        ↓
GitHub Pages
```

The final site should behave like documentation websites used by major open-source libraries.

Each curriculum folder should behave as a documentation section / URL namespace.

Each Markdown file should render as an individual documentation page.

For example, a source structure such as:

```text
10_Transformers_From_First_Principles/
├── README.md
├── 10.01_Scaled_Dot_Product_Self_Attention.md
├── 10.02_Multi_Head_Attention.md
└── 10.03_Positional_Information.md
```

should result in URLs conceptually similar to:

```text
/10_Transformers_From_First_Principles/

/10_Transformers_From_First_Principles/10.01_Scaled_Dot_Product_Self_Attention/

/10_Transformers_From_First_Principles/10.02_Multi_Head_Attention/
```

Use MkDocs directory-style URLs.

---

# IMPORTANT SAFETY REQUIREMENTS

Before making changes:

1. Inspect the complete existing repository.
2. Do not delete any curriculum content.
3. Do not silently rewrite syllabus content.
4. Do not change topic/subtopic meaning.
5. Preserve the numerical ordering of folders and files.
6. Preserve all existing Markdown files unless a structural change such as `README.md → index.md` is required for MkDocs.
7. If renaming files, make sure no content is lost.
8. Do not overwrite the original repository destructively without first making the changes easy to revert.
9. If the folder is already a Git repository, create a new branch such as:

```text
feature/mkdocs-site
```

before making structural changes.

If it is not a Git repository, initialize Git but do not push anywhere unless a remote repository has explicitly been configured.

---

# Step 1 — Inspect Existing Repository

First recursively inspect:

* folders
* Markdown files
* README files
* internal Markdown links
* naming conventions
* ordering
* root-level files
* curriculum-system files

Generate a short implementation summary before modifying files.

Pay particular attention to files such as:

```text
README.md
TREE.md

00_Curriculum_System/
00.01_Master_Learning_Prompt.md
00.02_How_to_Use.md
00.03_Competency_Levels.md
00.04_Math_Dependency_Index.md
00.05_Progress_Tracker.md
```

Do not treat curriculum content as disposable boilerplate.

---

# Step 2 — Create MkDocs-Compatible Structure

Restructure the project into approximately:

```text
repository-root/
│
├── README.md
├── mkdocs.yml
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── index.md
│   │
│   ├── 00_Curriculum_System/
│   │   ├── index.md
│   │   ├── 00.01_Master_Learning_Prompt.md
│   │   ├── 00.02_How_to_Use.md
│   │   └── ...
│   │
│   ├── 01_Thinking_Like_an_AI_ML_Engineer/
│   │   ├── index.md
│   │   └── ...
│   │
│   ├── 02_.../
│   │   └── ...
│   │
│   └── ...
│
└── .github/
    └── workflows/
        └── deploy-docs.yml
```

The exact implementation may vary slightly if there is a better MkDocs-native solution, but preserve the logical hierarchy.

The repository root `README.md` should describe the project for GitHub visitors.

The documentation homepage should be:

```text
docs/index.md
```

If appropriate, derive it from the existing root README while keeping the original information intact.

---

# Step 3 — Handle Section README Files

Inside curriculum folders, existing `README.md` files currently serve as section indexes.

For documentation folders, prefer:

```text
index.md
```

where appropriate.

Safely convert:

```text
folder/README.md
```

to:

```text
folder/index.md
```

inside the documentation source tree.

Do not lose any README content.

Update internal links if the rename affects them.

Do not rename the main repository-level README unless necessary.

---

# Step 4 — Configure Material for MkDocs

Use:

```text
mkdocs-material
```

as the documentation theme.

Create a clean `mkdocs.yml`.

The site should support at least:

* hierarchical sidebar navigation
* filesystem-based section hierarchy
* search
* right-side page table of contents where supported
* breadcrumbs/navigation path
* previous/next page navigation
* code-copy buttons
* light mode
* dark mode
* responsive mobile layout
* clean directory-style URLs
* heading anchors
* navigation back-to-top
* readable typography
* useful search highlighting

Use Material features where appropriate, for example concepts such as:

```yaml
features:
  - navigation.sections
  - navigation.indexes
  - navigation.top
  - navigation.footer
  - navigation.tracking
  - content.code.copy
  - search.suggest
  - search.highlight
```

Only enable valid features supported by the installed Material version.

Do not invent configuration keys.

---

# Step 5 — Navigation

There are hundreds of pages.

I do NOT want to manually maintain a giant 260-page navigation list if it can be avoided.

Prefer automatic navigation based on the existing filesystem hierarchy.

The numerical prefixes already define curriculum order, such as:

```text
01
02
03
...
10
11
...
```

and:

```text
10.01
10.02
10.03
```

Preserve this ordering.

If MkDocs' default automatic navigation provides a clean result, use it.

If additional configuration or a small generated navigation script is required, implement a maintainable solution.

Do not hard-code hundreds of pages manually unless absolutely necessary.

---

# Step 6 — Page Titles

Markdown page titles should come from their existing first-level headings wherever possible.

Avoid showing ugly raw filenames such as:

```text
10.01_Scaled_Dot_Product_Self_Attention
```

when the page already contains a proper heading such as:

```text
10.01 Scaled Dot Product Self Attention
```

Do not rewrite content just to achieve navigation labels unless necessary.

---

# Step 7 — Styling

Keep the site professional and documentation-focused.

Do not turn it into a marketing website.

Desired feel:

* technical documentation
* clean
* minimal
* excellent readability
* easy navigation through a large curriculum
* similar usability to documentation sites for major developer libraries

Avoid unnecessary custom CSS unless it materially improves readability.

If custom CSS is used, keep it small and maintainable.

---

# Step 8 — Search

Configure MkDocs Material's local search.

Users should be able to search across topics such as:

```text
LoRA
Cross Entropy
Attention
BPR
Forecasting
Gradient Descent
Causal Inference
```

without requiring an external search server.

---

# Step 9 — Internal Links

Validate Markdown links after restructuring.

Fix links that break because of:

```text
README.md → index.md
```

or because files moved under:

```text
docs/
```

Do not unnecessarily convert valid relative links into absolute URLs.

---

# Step 10 — Python Environment

Create a minimal:

```text
requirements.txt
```

containing required documentation dependencies.

At minimum evaluate the need for:

```text
mkdocs
mkdocs-material
```

Avoid unnecessary dependencies.

If `mkdocs-material` already installs the compatible MkDocs dependency, keep the dependency strategy clean.

Pin versions if doing so improves reproducibility.

---

# Step 11 — Local Development

Make sure the website can be launched locally with something similar to:

```bash
python -m venv .venv
```

then environment activation, followed by:

```bash
pip install -r requirements.txt
mkdocs serve
```

The local website should normally become available at:

```text
http://127.0.0.1:8000/
```

Document these commands in the repository README.

---

# Step 12 — Strict Production Build

Before considering the work complete, run:

```bash
mkdocs build --strict
```

Fix:

* broken links
* invalid config
* navigation issues
* duplicate pages
* missing files
* Markdown errors that break the build
* configuration warnings that matter

The final production build must succeed.

---

# Step 13 — GitHub Pages Deployment Workflow

Create:

```text
.github/workflows/deploy-docs.yml
```

Use GitHub Actions to:

1. trigger on pushes to the main branch
2. allow manual workflow dispatch if useful
3. checkout repository
4. set up Python
5. install documentation dependencies
6. run `mkdocs build --strict`
7. package/upload the generated static `site/`
8. deploy it to GitHub Pages

Prefer GitHub's current Pages Actions workflow using the appropriate official GitHub Actions for:

* Pages configuration
* Pages artifact upload
* Pages deployment

The workflow should have only the permissions it needs.

Do not embed credentials or secrets.

---

# Step 14 — GitHub Pages Compatibility

Configure the project so that it works when hosted as a GitHub project site such as:

```text
https://<username>.github.io/<repository-name>/
```

Do not assume the site is hosted at domain root `/`.

Links/assets must work correctly under the repository subpath.

Do not hard-code my GitHub username because it may not yet be known.

If `site_url` requires the final username/repository information, clearly mark the single place I must update later.

---

# Step 15 — Optional Custom Domain Readiness

Do not configure a fake custom domain.

But keep the structure compatible with adding a GitHub Pages custom domain later.

Document where a custom domain would be configured if I choose to add one.

---

# Step 16 — Git Ignore

Create an appropriate `.gitignore`.

At minimum consider ignoring:

```text
.venv/
site/
__pycache__/
.DS_Store
```

and relevant IDE/cache artifacts.

Do not ignore actual curriculum source files.

---

# Step 17 — Preserve GitHub-Friendly Markdown

The Markdown files should continue to remain readable directly inside GitHub.

Do not introduce proprietary formatting everywhere that makes the `.md` files unusable outside MkDocs.

MkDocs-specific enhancements are acceptable where useful, but Markdown portability is preferred.

---

# Step 18 — Validation Script

If useful, create a lightweight script such as:

```text
scripts/validate_docs.py
```

that checks things such as:

* duplicate filenames
* missing section index files
* broken local Markdown links
* missing H1 headings
* unexpected empty Markdown files

Do not overengineer this.

---

# Step 19 — Repository Documentation

Update the root `README.md` to explain:

## What this repository is

AI/ML Senior/Lead Engineer Master Syllabus.

## Documentation architecture

```text
Markdown
→ MkDocs
→ Material for MkDocs
→ GitHub Actions
→ GitHub Pages
```

## Local setup

Exact commands.

## Build

```bash
mkdocs build --strict
```

## Serve

```bash
mkdocs serve
```

## Deployment

Explain that pushes to the configured main branch trigger the GitHub Pages workflow.

## Editing curriculum

Explain that curriculum should be edited inside:

```text
docs/
```

and pushed through Git.

---

# Step 20 — Quality Assurance

Before finishing, verify at least:

### Homepage

* renders correctly

### Section page

* section index renders correctly

### Individual module

* Markdown renders correctly

### Navigation

* folders appear in correct numerical order

### Search

* finds module content

### Theme

* light/dark switching works

### Links

* internal navigation works

### Mobile

* navigation is usable

### Build

* `mkdocs build --strict` succeeds

### GitHub Actions

* workflow YAML is syntactically correct

---

# Expected URL Behaviour

With a future repository such as:

```text
ai-engineering-master-syllabus
```

a source file:

```text
docs/10_Transformers_From_First_Principles/10.01_Scaled_Dot_Product_Self_Attention.md
```

should ideally render as a URL resembling:

```text
https://<username>.github.io/ai-engineering-master-syllabus/10_Transformers_From_First_Principles/10.01_Scaled_Dot_Product_Self_Attention/
```

Directory-style clean URLs are preferred.

---

# Do Not Do These Things

Do not:

* rewrite the whole syllabus
* summarize curriculum modules
* merge topic files merely to reduce page count
* delete numerical prefixes
* flatten the directory structure
* put every page in one directory
* introduce a database
* introduce a backend server
* use React/Next.js unless there is a compelling technical requirement
* replace MkDocs with another framework without a very strong reason
* require paid hosting
* require an external search service
* put generated HTML in source-control unless deployment design genuinely requires it
* commit `.venv`
* expose secrets
* push to a remote GitHub repository without my explicit authorization

---

# Acceptance Criteria

The task is complete only when:

1. All existing curriculum content is preserved.
2. Every curriculum Markdown module is accessible through the MkDocs source tree.
3. Folder hierarchy maps naturally to site navigation.
4. Folder indexes render as section landing pages.
5. Individual `.md` modules render as proper documentation pages.
6. Search works.
7. Numerical curriculum ordering is preserved.
8. Light/dark Material theme works.
9. Local `mkdocs serve` works.
10. `mkdocs build --strict` succeeds.
11. A GitHub Pages deployment workflow exists.
12. Repository documentation explains exactly how to run and deploy it.
13. No paid infrastructure is required.
14. The original curriculum meaning/content has not been altered.

---

# Working Style

Do not just tell me what commands I should run.

Actually perform the file restructuring and configuration on the local repository.

Inspect first, then implement, then run validation/build commands, then fix issues.

At the end, give me a concise report containing:

1. files created
2. files moved/renamed
3. important configuration decisions
4. build/test results
5. anything I still need to manually configure
6. exact Git commands required to push it to a new GitHub repository
7. exact GitHub Pages setting I should select after pushing

Do not push anything remotely unless I explicitly authorize it.
