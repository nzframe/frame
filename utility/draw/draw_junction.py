from utility.draw import DrawIT
from model.junction import Junction, JunctionComponents


def draw_junction(td: DrawIT, junction: Junction):    
    td.prepare(junction.top_plate)
    td.prepare(junction.bottom_plate)
    components: JunctionComponents = junction.components
    for component in components:
        td.prepare(component)

    td.draw_it()

