from typing import List

from model.timber.timber import CuttedTimber, Orientation, TimberTag
from model.components.wall_part import WallPart


class TimberCheck:
    def __init__(self, timber: CuttedTimber) -> None:
        self.timber = timber
    
    def scan(self):
        self.scan_type()

    def scan_type(self):
        if hasattr(CuttedTimber, "orientation"):
            if CuttedTimber.orientation == Orientation.HORIZONTAL:
                self.timber.tag.add(TimberTag.PLATE)
            elif CuttedTimber.orientation == Orientation.VERTICAL:
                self.timber.tag.add(TimberTag.STUD)
        else:
            self.timber.tag.add(TimberTag.UNUSERD)

class Manager:
    def __init__(self, wall: WallPart) -> None:
        self.timbers = wall.cutted_timbers

    def sort(self):
        ''' sort the timbers '''
        sorted(self.timbers)