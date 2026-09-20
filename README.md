# Source Start Grade Tracker

Welcome to the **Source Start Grade Tracker** repository! We're excited to have you as a contributor to our student academic performance and grade tracking toolkit built with Python.

As part of **"Source Start"**, an open-source initiative organized by **CSI-SPIT**, this project is tailored to provide first-time contributors with hands-on experience in navigating codebases, fixing bugs, running test suites, and creating meaningful pull requests.

---

## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Fork the Repository](#1-fork-the-repository)
  - [Clone Your Fork](#2-clone-your-fork)
  - [Running the CLI](#3-running-the-cli)
  - [Exporting HTML Reports](#4-exporting-html-reports)
- [CLI Commands Reference](#cli-commands-reference)
- [Running Tests](#running-tests)
- [How to Contribute](#how-to-contribute)
  - [Contribution Workflow](#contribution-workflow)
  - [Issue Labels & Difficulty Tiers](#issue-labels--difficulty-tiers)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

---

## Introduction

**Grade Tracker** is a zero-dependency, CSV-backed academic tracking tool. It enables students and faculty to record test and assignment scores, compute letter grades and Grade Point Averages (GPA) on a standard 4.0 scale, analyze subject-wise performance averages, and export modern, responsive HTML report cards.

Whether you're a first-year student learning Python or an experienced developer looking to mentor and contribute, there is plenty to explore!

---

## Key Features

- 📊 **CSV Data Storage**: Simple, human-readable records stored in `data/grades.csv`.
- 🧮 **GPA & Letter Grade Calculations**: Automated conversions between percentage scores and 4.0 GPA scale.
- 💻 **CLI Dashboard**: Quick terminal commands to list grades, inspect student summaries, and view subject averages.
- 🌐 **Modern HTML Export**: Generates clean, responsive HTML cards with dark mode aesthetics inside `reports/`.
- 🧪 **Unit Test Suite**: Built-in test coverage using Python's native `unittest` module.
- ⚡ **Zero External Dependencies**: Runs out of the box on Python 3.8+ without needing `pip install`.

---

## Project Structure

```text
grade-tracker/
├── README.md               # Project documentation and contributor guide
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules for Python artifacts
├── data/
│   └── grades.csv          # Grade records: student_id, subject, score, max_score, date
├── grade_tracker/
│   ├── __init__.py         # Package initialization
│   ├── __main__.py         # Allows running `python -m grade_tracker`
│   ├── calc.py             # Logic for letter_grade(), gpa(), and subject_average()
│   ├── export.py           # HTML report generation and templating
│   └── cli.py              # Command-line interface and argument parsing
├── reports/                # Output directory for exported HTML reports
└── tests/
    ├── __init__.py
    └── test_calc.py        # Unit test suite for calculation logic
```

---

## Getting Started

### Prerequisites

All you need is **Python 3.8+** installed on your system. No external packages or virtual environments are strictly required!

Verify your Python installation:
```bash
python3 --version
# or
python --version
```

### 1. Fork the Repository

Click the **Fork** button at the top-right corner of the GitHub repository page to create your own copy under your GitHub account.

### 2. Clone Your Fork

Clone your newly created fork to your local computer:

```bash
git clone https://github.com/techcsispit/grade-tracker.git
cd grade-tracker
```

### 3. Running the CLI

Run the tool as a Python module:

```bash
# View all registered grades in a formatted table
python3 -m grade_tracker list

# View summary for a specific student ID
python3 -m grade_tracker summary CS101

# Calculate average for a subject
python3 -m grade_tracker average Mathematics
```

### 4. Exporting HTML Reports

Generate a visual HTML report card for all students:

```bash
python3 -m grade_tracker export
```

Once generated, open `reports/index.html` in your favorite web browser:
- **macOS:** `open reports/index.html`
- **Linux:** `xdg-open reports/index.html`
- **Windows:** `start reports/index.html`

---

## CLI Commands Reference

| Command | Arguments | Description |
|---|---|---|
| `list` | *None* | Displays all grade entries from `data/grades.csv`. |
| `summary` | `<student_id>` | Displays GPA, subject breakdown, and percentage for a student. |
| `average` | `<subject>` | Computes and displays the overall average score in a subject. |
| `export` | `[--output path]` | Exports an HTML dashboard (defaults to `reports/index.html`). |
| `add` | `<id> <subject> <score> <max> <date>` | Appends a new grade entry to `data/grades.csv`. |

Example adding a score:
```bash
python3 -m grade_tracker add CS101 "Data Structures" 94 100 2025-01-20
```

---

## Running Tests

Unit tests are written using Python's standard `unittest` framework.

Run all tests from the repository root:

```bash
python3 -m unittest discover tests
```

To run a specific test file:
```bash
python3 -m unittest tests/test_calc.py
```

> 💡 **Tip for Contributors:** When tackling a bug issue, run the tests first to observe failing test cases, make your fixes in `grade_tracker/`, and re-run the tests to ensure everything passes cleanly!

---

## How to Contribute

We welcome and encourage contributions from everyone participating in **Source Start**!

### Contribution Workflow

1. **Pick an Issue:** Head over to the **Issues** tab and find an open issue that interests you. Comment on the issue to get assigned.
2. **Create a New Branch:** Always make your changes in a dedicated branch:
   ```bash
   git checkout -b fix/issue-description
   ```
3. **Make Your Changes:** Edit code or documentation. Follow existing formatting conventions and keep docstrings intact.
4. **Test Your Changes:**
   - Run tests: `python3 -m unittest discover tests`
   - Test CLI behavior manually: `python3 -m grade_tracker list`
5. **Commit Your Changes:** Write clear, descriptive commit messages:
   ```bash
   git commit -m "fix: resolve issue description"
   ```
6. **Push to Your Fork:**
   ```bash
   git push origin fix/issue-description
   ```
7. **Open a Pull Request:** Go to your fork on GitHub and click **Compare & pull request**. Mention the issue number you resolved (e.g., `Fixes #1`).

### Issue Labels & Difficulty Tiers

- 🔁 `good first issue`: Ideal for beginners and first-time contributors.
- 🐛 `bug`: Fixing logical errors, boundary checks, or edge cases in calculation and export modules.
- ✨ `enhancement`: Introducing new features, options, or reporting functionality.

---

## Code of Conduct

We are dedicated to providing a friendly, inclusive, and welcoming environment for all participants. Please be respectful and supportive in your issue discussions and pull request reviews.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Organized with ❤️ by <b>CSI-SPIT</b> for <b>Source Start</b>.<br>
  Happy Open-Source Hacking! 🎓💻
</p>
