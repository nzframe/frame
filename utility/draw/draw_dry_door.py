from utility.draw import DrawIT
from model.door import DryDoor, DryDoorComponents


def draw_dry_door(td: DrawIT, door: DryDoor):    
    door_cpnt: DryDoorComponents = door.components
    td.prepare(door.top_plate)
    td.prepare(door.bottom_plate)
    td.prepare(door.left_king_stud)
    td.prepare(door.right_king_stud)
    td.prepare(door_cpnt.linter)

    for cripple in door_cpnt.top_cripples:
        td.prepare(cripple)

    td.draw_it()
