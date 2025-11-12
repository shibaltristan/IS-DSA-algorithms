# Student CLI — Data Structures & Algorithms Case Study

A small CLI tool implemented in Python to demonstrate basic data structures and algorithms (lists/dictionaries, sorting, binary search) for a course.

Files:
- `student.py` — Student dataclass
- `storage.py` — In-memory storage and operations (add/edit/delete/list/sort/search)
- `algorithms.py` — bubble sort, quick sort, binary search implementations
- `cli.py` — Simple interactive command-line interface
- `main.py` — Entrypoint to start the CLI
- `run_tests.py` — Small test harness validating core behavior

Usage:
1. Ensure you have Python 3.8+ installed.
2. Run tests:

```powershell
python run_tests.py
```

3. Start the CLI:

```powershell
python main.py
```

Commands (in CLI): add, edit, delete, list, sort_name, sort_grade, sort_id, search, save, load, exit

Notes:
- Data is held in memory; `save` and `load` allow JSON persistence.
- Sorting uses either quick sort or bubble sort implementations in `algorithms.py` (defaults to quick sort).
