from kettle.heater import Heater
from kettle.kettle_state import KettleState, State
from kettle.light import Light


class Kettle:
    _state: State = KettleState.NullState
    _heater: Heater
    _light: Light

    def __init__(self, initial_state: State = KettleState.IDLE):
        self._heater = Heater()
        self._light = Light()
        self._enter_state(initial_state)

    def _enter_state(self, state: State):
        self._state.exit(self)
        state.enter(self)
        self._state = state

    def is_light_on(self) -> bool:
        return self._light.is_lit()

    def is_heater_on(self) -> bool:
        return self._heater.is_heating()

    def on_button_press(self) -> None:
        new_state = self._state.on_button_press(self)
        self._enter_state(new_state)

    def on_temp_reached_or_exceeded(self) -> None:
        new_state = self._state.on_temp_reached_or_exceeded(self)
        self._enter_state(new_state)

    def on_pot_lifted(self) -> None:
        new_state = self._state.on_pot_lifted(self)
        self._enter_state(new_state)

    def light_on(self):
        """
        This would be much more interesting in the real world.
        """
        self._light.turn_on()

    def light_off(self):
        self._light.turn_off()

    def start_heater(self):
        self._heater.turn_on()

    def stop_heater(self):
        self._heater.turn_off()
