# iHuman Lab Cookiecutter Data Science

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.5+](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/downloads/)
[![cookiecutter](https://img.shields.io/badge/built%20with-cookiecutter-ff69b4.svg)](https://github.com/cookiecutter/cookiecutter)

> _Stop fighting your folder structure. Start doing science._

---

## What Is This?

You know that moment when a data science project starts as a Jupyter notebook named `final_FINAL_v3_ACTUALLY_FINAL.ipynb` and slowly becomes a folder of mystery?

This template fixes that — before it happens.

**iHuman Cookiecutter Data Science** gives you a clean, opinionated, battle-tested project scaffold so your team spends time on the actual science, not on debating where to put the data.

---

## Features

- Sensible folder structure out of the box
- `src/` layout so your code is importable like a real package
- Pre-wired `Makefile` for common tasks
- Configs, docs, tests — all have a home
- Git hooks included (no more committing notebook outputs)
- AWS S3 sync support for data

---

## Requirements

- Python >= 3.5
- [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0

Install cookiecutter:

```bash
pip install cookiecutter
```

or with conda:

```bash
conda config --add channels conda-forge
conda install cookiecutter
```

---

## Quickstart

One command. That's it.

```bash
cookiecutter https://github.com/iHuman-Lab/cookiecutter-data-science.git
```

Answer a few prompts, and you'll have a project that looks like this:

```
your_project/
├── configs/          <- Config files (YAML, TOML, etc.)
├── data/             <- Data lives here (raw, processed, external)
├── docs/             <- Documentation
├── src/              <- Your actual Python source code
├── tests/            <- Tests (yes, write them)
├── Makefile          <- Shortcuts for common tasks
├── project.toml      <- Project metadata
└── README.md         <- You are here
```

---

## Who Is This For?

- Researchers tired of the "works on my machine" problem
- Teams that want consistent project layouts without writing a style guide
- Anyone who has ever opened a colleague's repo and thought *"where do I even start?"*

---

## Contributing

Found a bug? Have an idea? Open an issue or a PR — we're friendly humans over here.

---

## License

MIT — go build something cool.
