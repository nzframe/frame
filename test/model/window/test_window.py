from model.window import Window, WindowComponents


def test_draw_dry_door():
    window = Window(2170, 1095, 630, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "window_door.png" 
    td = DrawIT(file_path.as_posix())
    
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

def test_pairwise():
    from more_itertools import pairwise
    a = [1,2,3]
    assert [(x, y) for x, y in pairwise(a)] == [(1, 2), (2, 3)]
