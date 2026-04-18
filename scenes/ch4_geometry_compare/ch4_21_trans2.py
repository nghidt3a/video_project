from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDChapter04Transition(BaseScene):
    def construct(self):
        group, anims = build_transition("Chương 4", "Minh họa trực quan", color=COLOR_V)
        self.play(*anims)
        self.wait(1.5)
        self.play(FadeOut(group))
        self.end_pause(1)
