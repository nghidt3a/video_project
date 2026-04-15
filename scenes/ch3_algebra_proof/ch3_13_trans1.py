from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDChapterTransition1(BaseScene):
    def construct(self):
        group, anims = build_transition(
            "Đại số",
            "Tại sao SVD tồn tại?",
            color=COLOR_U,
        )
        self.play(*anims, run_time=1.8)
        eq = MathTex(r"A^TA = VDV^T \quad AA^T = UEU^T", font_size=32, color=COLOR_MUTED)
        eq.next_to(group, DOWN, buff=0.45)
        safe_fit(eq)
        self.play(FadeIn(eq, shift=UP * 0.1), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(VGroup(group, eq)), run_time=0.7)
        self.end_pause(1)
