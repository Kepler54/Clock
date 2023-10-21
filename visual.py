from bext import goto
from ast import literal_eval
from rich.console import Console

color = Console()

try:
    with open("settings.spec") as read_settings:
        settings = literal_eval(read_settings.read())
except (FileNotFoundError, NameError):
    with open("settings.spec", mode="w") as write_settings:
        write_settings.write("['[purple]', '3']")
    input("Перезапустите приложение!")


class Visual:
    """Visualization class"""

    @staticmethod
    def get_graphic_number(value, x, y) -> None:
        """Visualization function"""
        coord = (39, 79, 13, 17)

        goto(coord[0], coord[2])
        color.print(settings[0] + '██')
        goto(coord[0], coord[3])
        color.print(settings[0] + '██')
        goto(coord[1], coord[2])
        color.print(settings[0] + '██')
        goto(coord[1], coord[3])
        color.print(settings[0] + '██')

        if int(value) == 0:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 7)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 1:
            goto(x, y)
            color.print(settings[0] + '  ████████    ')
            goto(x, y + 1)
            color.print(settings[0] + '  ██░░░░██    ')
            goto(x, y + 2)
            color.print(settings[0] + '  ████░░██    ')
            goto(x, y + 3)
            color.print(settings[0] + '    ██░░██    ')
            goto(x, y + 4)
            color.print(settings[0] + '    ██░░██    ')
            goto(x, y + 5)
            color.print(settings[0] + '    ██░░██    ')
            goto(x, y + 6)
            color.print(settings[0] + '    ██░░██    ')
            goto(x, y + 7)
            color.print(settings[0] + '    ██░░██    ')
            goto(x, y + 8)
            color.print(settings[0] + '  ████░░████  ')
            goto(x, y + 9)
            color.print(settings[0] + '  ██░░░░░░██  ')
            goto(x, y + 10)
            color.print(settings[0] + '  ██████████  ')

        if int(value) == 2:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 7)
            color.print(settings[0] + '██░░██        ')
            goto(x, y + 8)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 3:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 4:
            goto(x, y)
            color.print(settings[0] + '██████  ██████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 9)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 10)
            color.print(settings[0] + '        ██████')

        if int(value) == 5:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██        ')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 6:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██        ')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██████████')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 7:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 5)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 6)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 7)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 9)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 10)
            color.print(settings[0] + '        ██████')

        if int(value) == 8:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')

        if int(value) == 9:
            goto(x, y)
            color.print(settings[0] + '██████████████')
            goto(x, y + 1)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 2)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 3)
            color.print(settings[0] + '██░░██  ██░░██')
            goto(x, y + 4)
            color.print(settings[0] + '██░░██████░░██')
            goto(x, y + 5)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 6)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 7)
            color.print(settings[0] + '        ██░░██')
            goto(x, y + 8)
            color.print(settings[0] + '██████████░░██')
            goto(x, y + 9)
            color.print(settings[0] + '██░░░░░░░░░░██')
            goto(x, y + 10)
            color.print(settings[0] + '██████████████')
