from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDThankYou(BaseScene):
    def construct(self):
        title = vn_text("Thank You For Watching", size=52, weight="BOLD", color=COLOR_ACCENT)
        title.move_to(ORIGIN + UP * 0.2)
        safe_fit(title, max_w=config.frame_width - 1.4)

        byline = vn_text("By Nhóm 7", size=26, color=COLOR_TEXT)
        byline.next_to(title, DOWN, buff=0.28)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(byline, shift=UP * 0.08), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, byline)), run_time=0.8)
        self.wait(15.6)
        self.end_pause(1)
