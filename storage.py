from typing import List, Optional
from student import Student
from algorithms import bubble_sort, quick_sort, binary_search_by_key
import json

class StudentStorage:
    """In-memory student storage. Provides add/edit/delete/list and search operations."""

    def __init__(self):
        self.students: List[Student] = []
        # track if last sort key was 'id' to allow binary search
        self._last_sorted_key = None

    def add_student(self, student: Student) -> None:
        if any(s.id == student.id for s in self.students):
            raise ValueError(f"Student with id {student.id} already exists")
        self.students.append(student)
        self._last_sorted_key = None

    def edit_student(self, student_id: str, *, name: Optional[str] = None, grade: Optional[float] = None) -> bool:
        for s in self.students:
            if s.id == student_id:
                if name is not None:
                    s.name = name
                if grade is not None:
                    s.grade = float(grade)
                self._last_sorted_key = None
                return True
        return False

    def delete_student(self, student_id: str) -> bool:
        for i, s in enumerate(self.students):
            if s.id == student_id:
                del self.students[i]
                self._last_sorted_key = None
                return True
        return False

    def list_students(self) -> List[Student]:
        return list(self.students)

    def sort_by_name(self, method: str = "quick", reverse: bool = False) -> List[Student]:
        key = lambda s: s.name.lower()
        if method == "bubble":
            sorted_list = bubble_sort(self.students, key=key, reverse=reverse)
        else:
            sorted_list = quick_sort(self.students, key=key, reverse=reverse)
        self._last_sorted_key = ("name", reverse)
        return sorted_list

    def sort_by_grade(self, method: str = "quick", reverse: bool = True) -> List[Student]:
        # default: descending grade
        key = lambda s: s.grade
        if method == "bubble":
            sorted_list = bubble_sort(self.students, key=key, reverse=reverse)
        else:
            sorted_list = quick_sort(self.students, key=key, reverse=reverse)
        self._last_sorted_key = ("grade", reverse)
        return sorted_list

    def sort_by_id(self, method: str = "quick", reverse: bool = False) -> List[Student]:
        key = lambda s: s.id
        if method == "bubble":
            sorted_list = bubble_sort(self.students, key=key, reverse=reverse)
        else:
            sorted_list = quick_sort(self.students, key=key, reverse=reverse)
        self._last_sorted_key = ("id", reverse)
        return sorted_list

    def search_by_id(self, student_id: str) -> Optional[Student]:
        # use binary search if sorted by id ascending
        if self._last_sorted_key == ("id", False):
            idx = binary_search_by_key(self.students, student_id, key=lambda s: s.id)
            if idx is not None:
                return self.students[idx]
        # fallback linear search
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def save_to_json(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def load_from_json(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            arr = json.load(f)
        self.students = [Student.from_dict(d) for d in arr]
        self._last_sorted_key = None
