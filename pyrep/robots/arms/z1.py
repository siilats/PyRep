from pyrep.robots.arms.arm import Arm


class Z1(Arm):

    def __init__(self, count: int = 0):
        super().__init__(count, 'z1', 6)
