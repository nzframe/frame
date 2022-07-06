from utility.space.rect import XYRectangle
from model.timber import CuttedTimber

class GenericWall():
    """ wall is a combination of Components, window and retailing studs and common structure. """

    def __init__(self):
        self.top_plate: CuttedTimber = None
        self.bottom_plate: CuttedTimber = None

        self.left_king_stud: CuttedTimber = None
        self.right_king_stud: CuttedTimber = None
        self.area: XYRectangle = None

    def register(self, cutted_timber: CuttedTimber):
        """ Each wall component consists of different timbers """
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        """ get the number of timbers belonging to this component"""
        return len(self.cutted_timbers)
