from typing import List
from rich import box
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from utils import screen, input

console = Console(height=3, width=50)
layout = Layout()


class Person:

    def __init__(self, age=0, height=0) -> None:
        self._age = age
        self._height = height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        self._age = new_age

    def set_height(self, new_height: float) -> None:
        self._height = new_height


class Main:

    def run(self) -> None:
        people = self.input_people()
        self.print_people_data(people)

    def input_people(self) -> list:
        people = []

        for i in range(1, 6):
            screen.clear()

            person = Person()

            input_message = "Insert the {} person's age and height.".format(i)
            console.width = len(input_message) + 4

            layout.update(Panel(input_message))
            console.print(layout)

            person.set_age(input.integer_number_positive(
                'Age:'
            ))
            person.set_height(input.float_number_positive(
                'Height:'
            ))
            people.append(person)
        return people

    def print_people_data(self, people: List[Person]) -> None:
        screen.clear()
        table = Table(title='People Data', box=box.ROUNDED)

        table.add_column('Person ID', justify='center',
                         style='bold', no_wrap=True)
        table.add_column('Age', justify='center',
                         style='bold', no_wrap=True)
        table.add_column('Height', justify='center',
                         style='bold', no_wrap=True)

        for person in people[::-1]:
            table.add_row(
                str(people.index(person)),
                str(person.get_age()),
                '{:.2f}'.format(person.get_height()))

        console.print(table, highlight=False)


main = Main()
main.run()
