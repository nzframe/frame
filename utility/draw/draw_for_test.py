from utility.draw import DrawIT
from model.generic_wall import GenericWall

def draw_component(td: DrawIT, generic_wall: GenericWall):    
    for ele in generic_wall.grouped:
        td.prepare(ele)
    td.prepare(generic_wall.top_plate)
    td.prepare(generic_wall.bottom_plate)
    td.draw_it()


