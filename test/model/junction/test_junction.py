from model.junction import Junction
from utility.draw.draw_junction import draw_junction

def test_draw_junction():
    junction = Junction(2310, 2)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "junction.png" 
    td = DrawIT(file_path.as_posix())
    draw_junction(td, junction)

    td.draw_it()
