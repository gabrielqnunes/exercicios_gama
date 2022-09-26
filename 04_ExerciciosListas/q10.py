import numpy as np
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()
console.height = 4
layout = Layout()


class App:
    def run(self) -> None:
        (list_1, list_2) = self.get_number_lists()
        new_list = self.intercalate_lists(list_1, list_2)
        layout.update(Panel(f'List 1: {list_1}'))
        console.print(layout)
        layout.update(Panel(f'List 2: {list_2}'))
        console.print(layout)
        layout.update(Panel(f'Intercalated list: {new_list}'))
        console.print(layout)

    def get_number_lists(self) -> tuple:
        list_1 = np.random.randint(1000, size=[10])
        list_2 = np.random.randint(1000, size=[10])

        return (list_1, list_2)

    def intercalate_lists(self, list_1: list, list_2: list) -> list:
        new_list = []
        for i in range(len(list_1)):
            new_list.append(list_1[i])
            new_list.append(list_2[i])
        return new_list


app = App()
app.run()
