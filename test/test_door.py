from model.door import DoorComponents, create_door, LintelDoor


def test_door_init():
    d: DoorComponents = create_door(1830, 2170, 2630)
    assert d.top_plate is not None

