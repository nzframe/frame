from model.door import DryDoor, DryDoorComponents


def test_draw_dry_door():
    door = DryDoor(800, 2310, 2310)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "dry_door.png" 
    td = DrawIT(file_path.as_posix())
    
    door_cpnt: DryDoorComponents = door.components
    td.prepare(door.top_plate)
    td.prepare(door.bottom_plate)
    td.prepare(door.left_king_stud)
    td.prepare(door.right_king_stud)
    td.prepare(door_cpnt.linter)

    for cripple in door_cpnt.top_cripples:
        td.prepare(cripple)

    td.draw_it()
