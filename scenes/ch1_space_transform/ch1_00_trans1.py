from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDChapter01Transition(BaseScene):
    def construct(self):
        group, anims = build_transition(
            "Chương 1",
            "Ma trận và sự tác động của ma trận lên không gian",
            color=COLOR_ACCENT,
        )
        self.play(*anims)
        self.wait(1.5)
        self.play(FadeOut(group))
        self.wait(12.4)
        self.end_pause(1)
