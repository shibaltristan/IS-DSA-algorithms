from dataclasses import dataclass
from typing import Dict

@dataclass
class Student:
    id: str
    name: str
    grade: float

    def to_dict(self) -> Dict:
        return {"id": self.id, "name": self.name, "grade": self.grade}

    @staticmethod
    def from_dict(d: Dict) -> "Student":
        return Student(id=str(d["id"]), name=d["name"], grade=float(d["grade"]))

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, name={self.name!r}, grade={self.grade!r})\n"