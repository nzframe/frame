from utility.draw import DrawIT
from model.window import Window, WindowComponents


def draw_window(td: DrawIT, window: Window):    
    componenet: WindowComponents = window.components
    td.prepare(window.top_plate)
    td.prepare(window.bottom_plate)
    td.prepare(window.left_king_stud)
    td.prepare(window.right_king_stud)
    td.prepare(componenet.lintel)
    td.prepare(componenet.still)
    td.prepare(componenet.left_trimmer_stud)
    td.prepare(componenet.right_trimmer_stud)

    for cripple in componenet.top_cripples:
        td.prepare(cripple)

    for jack_stud in componenet.bottom_jack_studs:
        td.prepare(jack_stud)

    for nogging in window.noggings:
        td.prepare(nogging)

    td.draw_it()


