import drawSvg as draw
from model.wall_part import WallPart, WallInfo
from model.timber import CuttedTimber

d = draw.Drawing(1024, 768, origin=(0,0), displayInline=False)

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

