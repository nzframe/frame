from dataclasses import dataclass
from model.generic_wall import GenericWall
from model.timber import Cutted2BY4, Orientation

@dataclass
class CommonWallComponents:
    pass

class CommonWall(GenericWall):
    def __init__(self, wall_width: float, floor_height: float):
        super().__init__()
        self.wall_width = wall_width
        self.components: CommonWallComponents = []
        self.floor_height = floor_height
        self.__create__()

    def __create__(self):
        self.add_top_plate(self.wall_width, self.floor_height)
        self.add_bottom_plate(self.wall_width)
        self.add_left_king_stud(self.floor_height)
        self.add_right_king_stud(self.floor_height, self.wall_width)

    def add_top_plate(self, wall_width: float, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            wall_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(wall_width, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self, wall_width: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(wall_width, Orientation.HORIZONTAL)
        self.bottom_plate = timber

    def add_left_king_stud(self, floor_height: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        self.left_king_stud = timber

    def add_right_king_stud(self, floor_height: float, wall_width: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(wall_width - Cutted2BY4.HEIGHT)
        self.right_king_stud = timber
