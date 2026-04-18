from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDOpeningHook(BaseScene):
    def construct(self):
        hook = vn_text("Nhưng ma trận A đã thực sự làm gì với không gian", size=34, color=COLOR_ACCENT)
        hook.move_to(ORIGIN)

        formula = MathTex(r"A = U \Sigma V^T", font_size=72)
        formula.move_to(ORIGIN)

        self.play(Write(hook), run_time=1.8)
        self.wait(1.2)
        self.play(FadeOut(hook, shift=UP * 0.1), run_time=0.5)

        self.play(Write(formula), run_time=2.2)
        self.wait(0.8)
        self.play(formula.animate.move_to(UP * 2.8).scale(0.75), run_time=0.9)
        self.wait(1.0)
        self.end_pause(1)
