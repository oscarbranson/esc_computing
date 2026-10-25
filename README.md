# esc_computing

Earth Sciences Part II Computing Course: six weekly practical sessions that teach Python from scratch, using Jupyter notebooks and Earth Sciences examples.
Students are assumed to have no previous Python experience.

## What's in the repo

| Path | What it is |
|---|---|
| `exercises/` | The student notebooks (`Exercise0` to `Exercise6`), their `data/` and `img/` folders, and `check.py`. This folder is what students get. |
| `solutions/` | One solution notebook per exercise, covering the independent-coding task, plus model answers to every **Your turn** and **Fix the bug** task. |
| `Instructions.typ` / `Instructions.pdf` | Setup instructions for students: Anaconda, Cartopy and VS Code, on Windows, macOS and Linux. |
| `DEMONSTRATORS.md` | Notes for demonstrators: how to run a session, and where students get stuck. |
| `REVIEW.md` | A review of the exercises, with improvements planned for future years. |
| `STUDENT_REVIEW.md` | A read-through from a beginner's point of view, with a status section saying what has been fixed. |

## The exercises

| Notebook | Topic |
|---|---|
| `Exercise0` | How the sessions work, and where to get help |
| `Exercise1` | The elements of Python: arithmetic, variables, lists, `if` statements and loops |
| `Exercise2` | Libraries (NumPy), arrays and functions |
| `Exercise3` | Reading in, selecting and plotting data with pandas and matplotlib |
| `Exercise4` | Making maps with Cartopy |
| `Exercise5` | Fitting models to data |
| `Exercise6` | Random numbers and Monte Carlo error propagation |

Each notebook mixes worked examples with short tasks:
- **Predict** prompts, where students decide what a cell will do before running it;
- **Your turn** cells, with `___` blanks to fill in;
- a **Fix the bug** task;
- an **independent coding** task at the end, broken into checkpoints.

Students check their **Your turn** answers with `check('task name', answer)`, which prints ✓, or a hint without giving the answer away.

## Giving the course to students

1. Zip the `exercises` folder from the committed version of the repo, so that files created by running the notebooks (saved figures, `.ipynb_checkpoints`, `__pycache__`) are left out:

   ```bash
   git archive -o python_course.zip HEAD exercises
   ```

1. Put `python_course.zip` and `Instructions.pdf` on Moodle.
   Students unzip the folder, set up their computer using the instructions, and open the folder in VS Code.
1. Release the solutions when you're ready.
   They read their data from `../exercises/data`, so keep them in a folder beside `exercises`.

The notebooks must stay in the same folder as `check.py`, `data/` and `img/`.

## Editing the course

- **Save exercises without outputs, and solutions with outputs.**
  After changing a solution, re-run it from the `solutions` folder (for example with `jupyter nbconvert --to notebook --execute --inplace Exercise1_solution.ipynb`).
- **Some cells are meant to give an error,** so run the exercises cell by cell, not with Run All.
- **Answers to the `check()` tasks** are stored in `exercises/check.py`, base64-encoded, so that they aren't visible at a glance.
  To add or change one, run this in the `exercises` folder, then paste the printed text into `check.py` in place of the old encoded string:

  ```python
  import base64, json
  from check import _ANSWERS
  _ANSWERS['task name'] = {'expected': 42, 'tol': 0.01, 'hint': 'A hint that does not give the answer away.'}
  print(base64.b64encode(json.dumps(_ANSWERS).encode()).decode())
  ```

  `tol` is the relative tolerance, and is 0.01 if left out.
  If you change a task, update its model answer at the end of the matching solution notebook as well.
- **Rebuild the setup instructions** after editing `Instructions.typ` with `typst compile Instructions.typ`.
- **Conventions:** British spelling; `fig, ax = plt.subplots()` for figures (`fig, axs` with `axs[i]` for several panels), except for Cartopy maps in Exercise 4; f-strings for printing.
