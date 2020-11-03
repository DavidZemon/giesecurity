import typing

from django.shortcuts import render

try:
    from gpiozero import Button
except ImportError:
    class Button:
        def __init__(self, pin: int) -> None:
            self.pin = pin

        def is_active(self) -> bool:
            return (self.pin % 2) == 0


class Sensor:
    def __init__(self, name: str, pin: int) -> None:
        self.name = name
        self.button = Button(pin)

    def render(self) -> typing.Dict[str, typing.Union[str, bool]]:
        return {
            'name': self.name,
            'state': self.button.is_active()
        }


SENSORS = [
    Sensor('Sensor 1', 1),
    Sensor('Sensor 2', 2)
]


def index(request):
    return render(
        request,
        'index.html',
        {
            'sensors': [sensor.render() for sensor in SENSORS]
        }
    )
