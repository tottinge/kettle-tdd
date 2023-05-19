# Kettle TDD 

This is a simple kettle design, and I'm wanting to use it
to illustrate TDD, bad testing, good testing, several design
principles, and evolutionary design. 

# Okay, I cloned it... now what?
You need to have poetry installed one way or another
In the root of this project, type 
`poetry install`
or use your IDE's equivalent behavior.

Then run all the tests from the root directory (using poetry
or your IDE's equivalent functionality).

Your tests should be green to begin with, and ready to go.

# Now What

Well, today it's early days. You can look for bad code 
examples (especially in the tests) and consider what it 
would be like if we added another state or another device.

But no instructions are ready today. Give me some time 
to complete the bad examples!

The initial bad version is a two-state version, which only goes from idle to heating and back.
This would probably even be sufficient for a kettle, but we wanted to add some special features.


![kettle_1.png](UML%2Fkettle_1.png)

Events:
* Button Pressed - user pressed a button (edge detection)
* At Temp - temperature sensor is at or above the preset temperature (edge detection)
* Pot Lifted - user has lifted the pot off of the heating base (edge detection)

Actions:
* light on/off
* heater on/off

States:
* Idle
* Heating


We hope to evolve this model to something resembling this final diagram:

![kettle_done.png](UML%2Fkettle_done.png)