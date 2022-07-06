from dataclasses import dataclass
from model.timber import CuttedTimber
from model.component import Component


@dataclass
class LoadPointComponents():
    stud1: CuttedTimber
    stud2: CuttedTimber
    stud3: CuttedTimber
    stud4: CuttedTimber
    stud5: CuttedTimber

class LoadPoint(Component):
    pass
