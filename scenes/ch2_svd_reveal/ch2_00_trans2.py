from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDChapter02Transition(BaseScene):
    def construct(self):
        group, anims = build_transition(
            "Chương 2",
            "Sử dụng SVD, cách phân rã ma trận A qua SVD, áp dụng",
            color=COLOR_SIGMA,
        )
        self.play(*anims)
        self.wait(1.5)
        self.play(FadeOut(group))
        self.wait(13.5)
        self.end_pause(1)
