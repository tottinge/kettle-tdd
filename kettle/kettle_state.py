from abc import ABC


class State(ABC):
    def enter(self, kettle):
        ...

    def exit(self, kettle):
        ...

    def on_button_press(self, kettle):
        return self

    def on_temp_reached_or_exceeded(self, kettle):
        return self

    def on_pot_lifted(self, kettle):
        return self


class Heating(State):
    def enter(self, kettle):
        kettle.start_heater()
        kettle.light_on()

    def exit(self, kettle):
        kettle.stop_heater()
        kettle.light_off()

    def on_temp_reached_or_exceeded(self, kettle):
        return KettleState.IDLE

    def on_pot_lifted(self, kettle):
        return KettleState.IDLE


class Idle(State):

    def enter(self, kettle):
        kettle.stop_heater()
        kettle.light_off()


class KettleState:
    NullState = State()
    IDLE = Idle()
    HEATING = Heating()
