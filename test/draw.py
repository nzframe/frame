import drawSvg as draw
from action.actions import create_wall
from model.wall import Wall, WallInfo
from model.timber import CuttedTimber


wall: Wall = create_wall(Wall(WallInfo(800, 330)))

d = draw.Drawing(1024, 768, origin=(0,0), displayInline=False)

for timber in wall.timbers():
    timber: CuttedTimber = timber
    x, y = timber.a_cord.to_list()
    width =  (timber.b_cord - timber.a_cord).norm()
    height = (timber.c_cord - timber.b_cord).norm()
    # Draw a rectangle
    r = draw.Rectangle(x,y,width,height, fill='#3b3a47', stroke_width=2, stroke='black')
    r.appendTitle("Our first rectangle")  # Add a tooltip

    d.append(r)

d.setPixelScale(2)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')
d.savePng('example.png')

d.rasterize()  # Display as PNG
d  # Display as SVG

