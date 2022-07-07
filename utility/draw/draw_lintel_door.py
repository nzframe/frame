from utility.draw import DrawIT
from model.door import LintelDoor, LintelDoorComponents


def draw_lintel_door(td: DrawIT, door: LintelDoor):    
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
