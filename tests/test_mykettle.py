from hamcrest import assert_that, is_

from kettle.mykettle import Kettle
from kettle.kettle_state import KettleState


def test_initial_state():
    kettle = Kettle(KettleState.IDLE)
    assert_that(kettle.is_light_on(), is_(False))
    assert_that(kettle.is_heater_on(), is_(False))


def test_initial_state_button_press():
    kettle: Kettle = Kettle()
    kettle.on_button_press()
    assert_that(kettle.is_light_on(), is_(True))
    assert_that(kettle.is_heater_on(), is_(True))


def test_heating_state_reaches_temperature():
    kettle = Kettle(KettleState.HEATING)
    kettle.on_temp_reached_or_exceeded()  # when kettle is hot...
    assert_that(kettle.is_light_on(), is_(False))
    assert_that(kettle.is_heater_on(), is_(False))


def test_heating_state_and_pot_lifted():
    kettle = Kettle()
    kettle.on_button_press()  # Go to heating state
    kettle.on_pot_lifted()  # when pot is lifted
    assert_that(kettle.is_light_on(), is_(False), "Light left on")
    assert_that(kettle.is_heater_on(), is_(False), "Heater left on!")
