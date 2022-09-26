from typing import List
import numpy as np
from statistics import mean
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich import box
from utils import screen


console = Console()
layout = Layout()


class Student:
    id: int
    age: int
    height: float

    def set_id(self, id: int) -> None:
        self.id = id

    def set_age(self, age: int) -> None:
        self.age = age

    def set_height(self, height: float) -> None:
        self.height = height

    def get_id(self) -> int:
        return self.id

    def get_age(self) -> int:
        return self.age

    def get_height(self) -> float:
        return self.height


class App:
    def run(self) -> None:
        students = self.get_students_data()
        small_students = self.get_small_students(students)
        self.print_result(small_students)

    def get_students_data(self) -> list:
        students = []
        ids = np.array([i for i in range(30)])
        ages = np.random.randint(low=3, high=18, size=30)
        heights = np.random.uniform(low=1.30, high=2.10, size=30)
        for i in range(30):
            student = Student()
            student.set_id(ids[i])
            student.set_age(ages[i])
            student.set_height(round(heights[i], 2))
            students.append(student)

        return students

    def get_small_students(self, students: List[Student]) -> list:
        small_students = []
        heights = []
        for student in students:
            heights.append(student.get_height())

        students_height_avg = mean(heights)
        print(students_height_avg)
        for student in students:
            if student.get_height() < students_height_avg and student.get_age() > 13:
                small_students.append(student)

        return small_students

    def print_result(self, students: List[Student]) -> None:
        screen.clear()
        table_result = Table(box=box.ROUNDED)
        table_result.add_column('id')
        table_result.add_column('age')
        table_result.add_column('height')
        for student in students:
            table_result.add_row(
                f'{student.get_id()}',
                f'{student.get_age()}',
                f'{student.get_height():.2f}'
            )

        message = "The students that have age below the class's average are:"
        console.width = len(message) + 4
        console.height = 3
        layout.update(
            Panel(message))
        console.print(layout)

        console.height = None
        console.width = None
        layout.update(table_result)
        console.print(layout)


app = App()
app.run()
