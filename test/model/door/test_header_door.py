from model.door import HeaderDoor, HeaderDoorComponents


def test_draw_header_door():
    door = HeaderDoor(800, 2220, 2310)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door.png" 
    td = TestDraw(file_path.as_posix())
    
    door_cpnt: HeaderDoorComponents = door.door_components
    td.prepare(door.top_plate)
    td.prepare(door.bottom_plate)
    td.prepare(door.left_king_stud)
    td.prepare(door.right_king_stud)
    td.prepare(door_cpnt.left_trimmer_stud)
    td.prepare(door_cpnt.right_trimmer_stud)
    td.prepare(door_cpnt.header)
    td.prepare(door_cpnt.linter)

    for cripple in door_cpnt.top_cripples:
        td.prepare(cripple)

    td.draw_it()
