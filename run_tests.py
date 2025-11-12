from storage import StudentStorage
from student import Student


def run():
    s1 = Student("100", "Alice", 88)
    s2 = Student("101", "Bob", 75)
    s3 = Student("102", "Charlie", 93)
    s4 = Student("103", "Dana", 60)

    store = StudentStorage()
    store.add_student(s3)
    store.add_student(s1)
    store.add_student(s4)
    store.add_student(s2)

    # Test sort by name
    sorted_by_name = store.sort_by_name()
    names = [s.name for s in sorted_by_name]
    assert names == ["Alice", "Bob", "Charlie", "Dana"], f"sort_by_name failed: {names}"

    # Test sort by grade (descending)
    sorted_by_grade = store.sort_by_grade()
    grades = [s.grade for s in sorted_by_grade]
    assert grades == [93, 88, 75, 60], f"sort_by_grade failed: {grades}"

    # Test sort by id and binary search
    store.sort_by_id()
    found = store.search_by_id("101")
    assert found is not None and found.name == "Bob", "binary search by id failed"

    # Test edit
    store.edit_student("103", name="Dana S", grade=65)
    s = store.search_by_id("103")
    assert s is not None and s.name == "Dana S" and s.grade == 65

    # Test delete
    ok = store.delete_student("100")
    assert ok and store.search_by_id("100") is None

    print("All tests passed ✅")

if __name__ == '__main__':
    run()
