class Heater:
    _heating: bool

    def __init__(self):
        _heating = False

    def turn_on(self) -> object:
        self._heating = True

    def is_heating(self):
        return self._heating

    def turn_off(self):
        self._heating = False
