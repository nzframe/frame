import drawSvg as draw
from model.door import HeaderDoor
from model.timber import CuttedTimber
from model.generic_wall import GenericWall


class TestDraw:
    def __init__(self, file_name: str) -> None:
        ##TODO fix hard code
        self.d = draw.Drawing(3000, 3000, origin=(0,0), displayInline=False)
        self.file_name = file_name
    
    def prepare(self, timber: CuttedTimber):
        if timber is None:
            return 
            
        x, y = timber.a_cord.to_list()
        width =  (timber.b_cord - timber.a_cord).norm()
        height = (timber.c_cord - timber.b_cord).norm()
        # Draw a rectangle
        r = draw.Rectangle(x,y,width,height, fill='#3b3a47', stroke_width=2, stroke='black')
        r.appendTitle("Our first rectangle")  # Add a tooltip

        self.d.append(r)

    def draw_it(self):
        self.d.setPixelScale(2)  # Set number of pixels per geometry unit
        #d.setRenderSize(400,200)  # Alternative to setPixelScale
        self.d.savePng(self.file_name)


# def test_draw(file_name: str, component: Component):
#     d = draw.Drawing(3000, 3000, origin=(0,0), displayInline=False)

#     door: HeaderDoor = HeaderDoor(800, 2220, 2310)
#     door.create()

#     def draw_timber(timber: CuttedTimber):
#         if timber is None:
#             return 
            
#         x, y = timber.a_cord.to_list()
#         width =  (timber.b_cord - timber.a_cord).norm()
#         height = (timber.c_cord - timber.b_cord).norm()
#         # Draw a rectangle
#         r = draw.Rectangle(x,y,width,height, fill='#3b3a47', stroke_width=2, stroke='black')
#         r.appendTitle("Our first rectangle")  # Add a tooltip

#         d.append(r)

#     draw_timber(door.door_components.top_plate)
#     draw_timber(door.door_components.bottom_plate)
#     draw_timber(door.door_components.left_king_stud)
#     draw_timber(door.door_components.right_king_stud)
#     draw_timber(door.door_components.left_trimmer_stud)
#     draw_timber(door.door_components.right_trimmer_stud)
#     draw_timber(door.door_components.header)
#     draw_timber(door.door_components.linter)

#     for timber in door.door_components.top_cripples:
#         draw_timber(timber)

#     d.setPixelScale(2)  # Set number of pixels per geometry unit
#     #d.setRenderSize(400,200)  # Alternative to setPixelScale
#     d.saveSvg('example.svg')
#     d.savePng('example.png')

#     d.rasterize()  # Display as PNG
#     d  # Display as SVG

