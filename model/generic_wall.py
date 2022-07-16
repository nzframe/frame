from utility.space.rect import XYRectangle
from model.timber import CuttedTimber


class GenericWall:
    """ wall is a combination of Components, window and retailing studs and common structure. """

    def __init__(self):
        self.top_plate: CuttedTimber = None
        self.bottom_plate: CuttedTimber = None

        self.left_king_stud: CuttedTimber = None
        self.right_king_stud: CuttedTimber = None
        self.area: XYRectangle = None
        self.grouped = []

    def register(self, cutted_timber: CuttedTimber):
        """ Each wall component consists of different timbers """
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        """ get the number of timbers belonging to this component"""
        return len(self.cutted_timbers)
    
    @property
    def get_area(self):
        if self.top_plate is None or self.bottom_plate is None:
            raise ValueError("top_plate and bottom_plate doesn't exist so can't build the area")
        self.area = XYRectangle(self.bottom_plate.a_cord, self.bottom_plate.b_cord, self.top_plate.c_cord, self.top_plate.d_cord)        
        return self.area        
    
    def export_data(self):
        pass

    def move_right(self, value: float):
        for ele in self.grouped:    
            ele.move_right(value)

        return self


    def transform(self):
        pass

    def group(self):
        """ group all the timbers into one array (except the top_plate and bottom_plate, but still can use it by instance variable)
            will be used later in transform, data export, draw later on. 
        """        
        #self.grouped.append(self.top_plate)
        #self.grouped.append(self.bottom_plate)


        self.grouped.append(self.left_king_stud)
        self.grouped.append(self.right_king_stud)