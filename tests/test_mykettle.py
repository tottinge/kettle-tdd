from hamcrest import assert_that, is_

from kettle.kettle_state import KettleState
from kettle.mykettle import Kettle


def test_initial_state_has_devices_off():
    kettle = Kettle(KettleState.IDLE)
    assert_that(kettle._light._lit, is_(False))
    assert_that(kettle._heater._heating, is_(False))


def test_initial_state_button_press_changes_state():
    kettle: Kettle = Kettle()
    kettle.on_button_press()
    assert_that(kettle._state, is_(KettleState.HEATING))


def test_heating_state_turns_on_devices():
    kettle: Kettle = Kettle(KettleState.HEATING)
    assert_that(kettle.is_light_on(), is_(True))
    assert_that(kettle.is_heater_on(), is_(True))


def test_heating_state_temp_reached_returns_to_idle_state():
    kettle = Kettle(KettleState.HEATING)
    kettle.on_temp_reached_or_exceeded()
    assert_that(kettle._state, is_(KettleState.IDLE))


def test_heating_state_reaches_temperature_and_turns_off():
    kettle = Kettle(KettleState.HEATING)
    kettle.on_temp_reached_or_exceeded()
    assert_that(kettle._light._lit, is_(False))
    assert_that(kettle._heater._heating, is_(False))


def test_heating_state_and_pot_lifted():
    kettle = Kettle(KettleState.HEATING)
    kettle.on_pot_lifted()  # when pot is lifted
    assert_that(kettle.is_light_on(), is_(False), "Light left on")
    assert_that(kettle.is_heater_on(), is_(False), "Heater left on!")
