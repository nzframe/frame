from model.load_point import LoadPoint, LoadPointComponents


def test_draw_load_point():
    load_point = LoadPoint(2310, 5)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "load_point.png" 
    td = DrawIT(file_path.as_posix())
    td.prepare(load_point.top_plate)
    td.prepare(load_point.bottom_plate)
    td.prepare(load_point.left_king_stud)
    td.prepare(load_point.right_king_stud)
    components: LoadPointComponents = load_point.components
    for component in components:
        td.prepare(component)

    td.draw_it()

def test_python_range():
    assert [i for i in range(1, 4)] == [1, 2, 3]