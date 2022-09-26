from typing import List
from random import uniform
from statistics import mean
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich import box
from utils import screen

console = Console()
layout = Layout()


class Month:
    name: str
    avg_temperature: float

    def __init__(self, name, avg_temperature=0):
        self.name = name
        self.avg_temperature = avg_temperature

    def set_name(self, name: str) -> None:
        self.name = name

    def set_avg_temperature(self, avg_temperature: float):
        self.avg_temperature = avg_temperature

    def get_name(self) -> str:
        return self.name

    def get_avg_temperature(self) -> float:
        return self.avg_temperature


class App:
    def run(self) -> None:
        months = self.get_months_data()
        months = self.get_higher_temperatures(months)
        self.print_result(months)

    def get_months_data(self) -> List[Month]:
        months = [
            Month('January'),
            Month('February'),
            Month('March'),
            Month('April'),
            Month('May'),
            Month('June'),
            Month('July'),
            Month('August'),
            Month('September'),
            Month('Octuber'),
            Month('November'),
            Month('December')
        ]

        for month in months:
            month.set_avg_temperature(uniform(-10, 41))

        return months

    def get_higher_temperatures(self, months: List[Month]) -> List[Month]:
        temperatures = []
        highest_temperature_months = []
        for month in months:
            temperatures.append(month.get_avg_temperature())

        anual_avg_temperature = mean(temperatures)
        for month in months:
            if month.get_avg_temperature() > anual_avg_temperature:
                highest_temperature_months.append(month)

        return highest_temperature_months

    def print_result(self, months: List[Month]) -> None:
        screen.clear()
        table = Table(
            title='Highest Temperatures',
            box=box.ROUNDED
        )
        table.add_column('Name', justify='right')
        table.add_column('Temperature - C°', justify='center')
        for month in months:
            table.add_row(
                f'{month.get_name()}',
                f'{month.get_avg_temperature():.2f}'
            )
        message = 'The highests temperatures are:'
        console.width = len(message) + 4
        console.height = 3
        layout.update(Panel(message))
        console.print(layout)
        console.height = None
        console.width = None
        console.print(table)


app = App()
app.run()
