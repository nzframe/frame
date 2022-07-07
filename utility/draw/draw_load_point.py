from utility.draw import DrawIT
from model.load_point import LoadPoint, LoadPointComponents


def draw_load_point(td: DrawIT, load_point: LoadPoint):    
    td.prepare(load_point.top_plate)
    td.prepare(load_point.bottom_plate)
    td.prepare(load_point.left_king_stud)
    td.prepare(load_point.right_king_stud)
    components: LoadPointComponents = load_point.components
    for component in components:
        td.prepare(component)

    td.draw_it()

def draw_load_point_without(td: DrawIT, load_point: LoadPoint):    
    td.prepare(load_point.left_king_stud)
    td.prepare(load_point.right_king_stud)
    components: LoadPointComponents = load_point.components
    for component in components:
        td.prepare(component)

    td.draw_it()