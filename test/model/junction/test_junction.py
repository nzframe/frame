from model.junction import Junction
from utility.draw.draw_for_test import draw_component

def test_draw_junction():
    junction = Junction(2310, 2)
    junction.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "junction.png" 
    td = DrawIT(file_path.as_posix())
    draw_component(td, junction)
