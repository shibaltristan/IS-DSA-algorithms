from storage import StudentStorage
from student import Student

PROMPT = "[students] > "


def print_student(s: Student) -> None:
    print(f"ID: {s.id} | Name: {s.name} | Grade: {s.grade}")


def run_cli():
    store = StudentStorage()
    print("CLI Student Manager — type 'help' for commands")
    while True:
        try:
            cmd = input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting")
            break
        if not cmd:
            continue
        parts = cmd.split()
        op = parts[0].lower()
        args = parts[1:]

        if op == "help":
            print("Commands: add, edit, delete, list, sort_name, sort_grade, sort_id, search, save, load, exit")
            print("Examples:")
            print("  add 123 'Alice' 85.5")
            print("  edit 123 name='Alice B' grade=88")
            continue

        if op == "add":
            if len(args) < 3:
                print("Usage: add <id> <name> <grade>")
                continue
            sid = args[0]
            name = args[1]
            try:
                grade = float(args[2])
            except ValueError:
                print("Grade must be a number")
                continue
            try:
                store.add_student(Student(sid, name, grade))
                print("Added")
            except ValueError as e:
                print(e)
            continue

        if op == "edit":
            if len(args) < 2:
                print("Usage: edit <id> name=<name> grade=<grade>")
                continue
            sid = args[0]
            name = None
            grade = None
            for token in args[1:]:
                if token.startswith("name="):
                    name = token.split("=", 1)[1]
                if token.startswith("grade="):
                    try:
                        grade = float(token.split("=", 1)[1])
                    except ValueError:
                        print("grade must be numeric")
                        grade = None
            ok = store.edit_student(sid, name=name, grade=grade)
            print("Edited" if ok else "Not found")
            continue

        if op == "delete":
            if len(args) < 1:
                print("Usage: delete <id>")
                continue
            ok = store.delete_student(args[0])
            print("Deleted" if ok else "Not found")
            continue

        if op == "list":
            for s in store.list_students():
                print_student(s)
            continue

        if op == "sort_name":
            sorted_list = store.sort_by_name()
            for s in sorted_list:
                print_student(s)
            continue

        if op == "sort_grade":
            sorted_list = store.sort_by_grade()
            for s in sorted_list:
                print_student(s)
            continue

        if op == "sort_id":
            sorted_list = store.sort_by_id()
            for s in sorted_list:
                print_student(s)
            continue

        if op == "search":
            if len(args) < 1:
                print("Usage: search <id>")
                continue
            s = store.search_by_id(args[0])
            if s:
                print_student(s)
            else:
                print("Not found")
            continue

        if op == "save":
            if len(args) < 1:
                print("Usage: save <path>")
                continue
            store.save_to_json(args[0])
            print("Saved")
            continue

        if op == "load":
            if len(args) < 1:
                print("Usage: load <path>")
                continue
            try:
                store.load_from_json(args[0])
                print("Loaded")
            except Exception as e:
                print("Error loading:", e)
            continue

        if op in ("exit", "quit"):
            print("Goodbye")
            break

        print("Unknown command. Type 'help' for commands.")
