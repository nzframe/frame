from model.load_point import LoadPoint, LoadPointComponents


def test_draw_load_point():
    load_point = LoadPoint(2310, 5)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "load_point.png" 
    td = TestDraw(file_path.as_posix())
    
    components: LoadPointComponents = load_point.components
    for component in components:
        td.prepare(component)

    td.draw_it()
