from utility.space.rect import XYRectangle
from model.timber import CuttedTimber

class Component(XYRectangle):
    """ wall is a combination of Components, window and retailing studs and common structure. """

    def register(self, cutted_timber: CuttedTimber):
        """ Each wall component consists of different timbers """
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        """ get the number of timbers belonging to this component"""
        return len(self.cutted_timbers)
