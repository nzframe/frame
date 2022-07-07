from model.junction import Junction, JunctionComponents


def test_draw_junction():
    junction = Junction(2310, 2)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "junction.png" 
    td = DrawIT(file_path.as_posix())
    td.prepare(junction.top_plate)
    td.prepare(junction.bottom_plate)
    components: JunctionComponents = junction.components
    for component in components:
        td.prepare(component)

    td.draw_it()
