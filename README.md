# Student Record System: Merge Sort (Python desktop app)

A desktop app for managing, sorting and ranking student records, built around a **hand-written merge sort** instead of
Python's built-in `sorted()`. Records persist in a JSON file, and the interface uses Tkinter, so it runs on any Python 3
install with **no dependencies**.

Built as a Data Structures & Algorithms project (March 2026).
A browser version with search and full CRUD is in
[student-record-system-Merge-Sort](https://github.com/TeereraiKagura/student-record-system-Merge-Sort)
([live demo](https://student-record-system-merge-sort.vercel.app)).

## Features

- **Add students:** ID, name, marks and age, with input validation (numeric marks and age; ID and name required).
- **View records** in a table (`ttk.Treeview`).
- **Sort by marks** (high → low) or **by name** (A → Z) using the custom merge sort. The sorted order is saved back to disk.
- **Class rankings** with 🥇🥈🥉 for the top three.
- **Persistence:** every change is written to `students.json`. A missing or corrupted file starts an empty list instead of crashing.

## How the merge sort works

`merge_sort.py` implements divide and conquer, generic over any record field:

```python
merge_sort(students, "marks", reverse=True)   # rankings
merge_sort(students, "name")                  # alphabetical
```

1. **Divide:** split the list in half recursively until each part has one element.
2. **Conquer:** merge pairs of sorted halves by repeatedly taking the smaller (or larger, if `reverse`) front element.

| | |
|---|---|
| Time | **O(n log n)** in every case, with no worst-case quadratic blow-up as in naive quicksort |
| Space | O(n) for the merged lists |
| Stable | **Yes.** On ties the left element wins, so students with equal marks keep their existing order |

The sort prints `DEBUG` lines for each split and merge, so you can watch divide and conquer happen in the terminal during a demo.

## Project structure

```
main.py          Tkinter GUI: menu, add/view/sort/rank windows
merge_sort.py    merge_sort() and merge(), keyed and with optional reverse order
database.py      load/save students.json
students.json    data file, seeded with 4 sample students
```

## Run it

Requires Python 3 (Tkinter is included with the standard Windows and macOS installers).

```bash
git clone https://github.com/TeereraiKagura/Student-Record-System..git
cd Student-Record-System.
python main.py
```

Run it from the project folder, because `students.json` is read from the current directory.
Four sample students are pre-loaded, so sorting and rankings work immediately.

## What I'd improve next

- **Case-insensitive name sorting.** Python compares uppercase before lowercase, so "adam" currently sorts after "Zara".
- **Reject duplicate student IDs** when adding a record.
- **Edit and delete** records from the table.
- **Unit tests** for `merge_sort` (empty list, ties, already-sorted, reverse-sorted), and a flag to turn off the debug output.

## Tech

Python 3 · Tkinter / ttk · JSON · merge sort (divide and conquer)
