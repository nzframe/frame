from typing import List

from model.timber import CuttedTimber, Orientation, TimberTag

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
