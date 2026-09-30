# grade-tracker

Keep track of marks, see letter grades and a GPA for each student, and export an HTML report. A command-line tool in plain Python with no dependencies. Marks are saved in `data/grades.csv`.

## Running it

You need Python 3.8 or newer.

```
python3 -m grade_tracker list
python3 -m grade_tracker summary CS101
python3 -m unittest discover tests
```

On Windows, use `python` instead of `python3`.

## Commands

| Command | Does |
|---|---|
| `list` | Every mark, with its letter grade |
| `summary <student_id>` | One student's marks and GPA |
| `average <subject>` | The class average for a subject |
| `add <student_id> <subject> <score> <max_score> <date>` | Adds a mark |
| `export [--output path]` | Writes an HTML report, `reports/index.html` by default |

## How it's supposed to work

- Grades go by percentage: 90 and above is A, 80–89 B, 70–79 C, 60–69 D, below 60 F.
- GPA is on a 4-point scale: A 4, B 3, C 2, D 1, F 0.
- A subject's average is the average percentage, so marks out of different totals compare fairly. 35/50 and 70/100 are both 70%.
- `add` refuses a score below 0 or above the maximum, a maximum of 0 or less, and a date that isn't `YYYY-MM-DD`.
- The report has a card for every student in the CSV, and only those.
- Everything in the report is shown as plain text. A subject name containing HTML is displayed, not run.

## Code

- `grade_tracker/calc.py`: letter grades, GPA, averages
- `grade_tracker/cli.py`: the commands, and reading and writing the CSV
- `grade_tracker/export.py`: the HTML report
- `tests/`: tests, run with `python3 -m unittest discover tests`

## Contributing

Fork the repo, make your changes on a new branch, and open a pull request. Run the tests first.

If you find a bug, open an issue with the steps to reproduce it, what you expected, and what happened instead.

Part of Source Start by CSI SPIT. MIT licensed.
