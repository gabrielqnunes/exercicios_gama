from typing import List
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from utils import input, screen

console = Console()
console.height = 3


class App:
    def run(self):
        numbers = self.input_numbers()
        self.print_result(numbers)

    def input_numbers(self) -> List[int]:
        numbers = []

        layout = Layout()

        for i in range(1, 11):
            screen.clear()

            message = f'Insert the {i} integer number'
            console.width = len(message) + 4
            layout.update(Panel(message))
            console.print(layout)

            number = input.integer_number_positive(
                f'[underline]Number:[/underline]'
            )
            numbers.append(number)
        return numbers

    def print_result(self, numbers: List[int]) -> None:
        sum_message = ''
        sum_result = 0
        for number in numbers:
            if numbers.index(number) == 0:
                sum_message = f'{number**2}'
            else:
                sum_message = f'{sum_message} + {number**2}'
            sum_result += number**2
        sum_message = f'{sum_message} = [underline]{sum_result}[/underline]'

        screen.clear()
        console.width = len(sum_message) - 19
        layout = Layout(Panel(sum_message))
        console.print(layout)


app = App()
app.run()
