from model.door import LintelDoorComponents, create_lintel_door, LintelDoor


def test_door_init():
    d: LintelDoorComponents = create_lintel_door(1830, 2170, 2630)
    assert d.top_plate is not None

