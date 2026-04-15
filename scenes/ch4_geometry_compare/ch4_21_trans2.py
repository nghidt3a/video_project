from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDChapterTransition2(BaseScene):
    def construct(self):
        group, anims = build_transition("Chương 4", "Hình học & So sánh", color=COLOR_V)
        self.play(*anims)
        self.wait(1.5)
        self.play(FadeOut(group))
        self.end_pause(1)
