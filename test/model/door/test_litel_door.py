from model.door import LintelDoor, LintelDoorComponents


def test_draw_lintel_door():
    door = LintelDoor(1830, 2170, 2630)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "litel_door.png" 
    td = TestDraw(file_path.as_posix())
    
    door_cpnt: LintelDoorComponents = door.components
    td.prepare(door.top_plate)
    td.prepare(door.bottom_plate)
    td.prepare(door.left_king_stud)
    td.prepare(door.right_king_stud)
    td.prepare(door_cpnt.left_trimmer_stud)
    td.prepare(door_cpnt.right_trimmer_stud)
    td.prepare(door_cpnt.lintel)

    for cripple in door_cpnt.top_cripples:
        td.prepare(cripple)

    td.draw_it()
