class Kettle:
    def __init__(self):
        self._heater_on = False
        self._light_lit = False

    def is_light_on(self) -> bool:
        return self._light_lit

    def is_heater_on(self):
        return self._heater_on

    def on_button_press(self):
        self._light_button()
        self._start_heater()

    def on_temp_reached_or_exceeded(self):
        self._light_lit = False
        self._heater_on = False

    def _light_button(self):
        """
       This would be much more interesting in the real world.
       """
        self._light_lit = True

    def _start_heater(self) -> None:
        """
        This would be much more interesting in the real world.
        """
        self._heater_on = True

    def on_pot_lifted(self):
        self._heater_on = False
        self._light_lit = False
