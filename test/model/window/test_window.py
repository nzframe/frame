from model.window import Window, WindowComponents


def test_draw_dry_door():
    window = Window(2170, 1095, 630, 2630)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "window_door.png" 
    td = TestDraw(file_path.as_posix())
    
    componenet: WindowComponents = window.components
    td.prepare(componenet.top_plate)
    td.prepare(componenet.bottom_plate)
    td.prepare(componenet.left_king_stud)
    td.prepare(componenet.right_king_stud)
    td.prepare(componenet.lintel)
    td.prepare(componenet.still)
    td.prepare(componenet.left_trimmer_stud)
    td.prepare(componenet.right_trimmer_stud)

    for cripple in componenet.top_cripples:
        td.prepare(cripple)

    for jack_stud in componenet.bottom_jack_studs:
        td.prepare(jack_stud)

    td.draw_it()
