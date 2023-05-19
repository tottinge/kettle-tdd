from kettle.heater import Heater
from kettle.kettle_state import KettleState
from kettle.light import Light


class Kettle:
    _state: KettleState
    _heater: Heater
    _light: Light

    def __init__(self, initial_state: KettleState = KettleState.IDLE):
        self._heater = Heater()
        self._light = Light()
        self.enter_state(initial_state)

    def enter_state(self, state: KettleState):
        if state is KettleState.IDLE:
            self._stop_heater()
            self._light_off()
        elif state is KettleState.HEATING:
            self._start_heater()
            self._light_on()
        self._state = state

    def is_light_on(self) -> bool:
        return self._light.is_lit()

    def is_heater_on(self):
        return self._heater.is_heating()

    def on_button_press(self):
        if self._state is KettleState.IDLE:
            self.enter_state(KettleState.HEATING)
        else:
            pass

    def on_temp_reached_or_exceeded(self):
        if self._state is KettleState.HEATING:
            self.enter_state(KettleState.IDLE)

    def on_pot_lifted(self):
        if self._state is KettleState.HEATING:
            self.enter_state(KettleState.IDLE)

    def _light_on(self):
        """
        This would be much more interesting in the real world.
        """
        self._light.turn_on()

    def _light_off(self):
        self._light.turn_off()

    def _start_heater(self):
        self._heater.turn_on()

    def _stop_heater(self):
        self._heater.turn_off()
