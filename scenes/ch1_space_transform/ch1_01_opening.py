from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDOpeningHook(BaseScene):
    def construct(self):
        # VO cue: mo dau - cong thuc SVD xuat hien
        formula = MathTex(r"A = U \Sigma V^T", font_size=72)
        formula.move_to(ORIGIN)

        subtitle_text = vn_text("Đúng với mọi ma trận", size=28)
        subtitle_formula = MathTex(r"A \in \mathbb{R}^{m \times n}", font_size=32)
        subtitle = VGroup(subtitle_text, subtitle_formula).arrange(RIGHT, buff=0.2)
        subtitle.next_to(formula, DOWN, buff=0.6)

        self.wait(2)

        # VO cue: cau hoi dan dat nguoi xem
        hook = vn_text("Nhưng A thực sự làm gì với không gian?", size=32, color=COLOR_ACCENT)
        hook.next_to(formula, DOWN, buff=0.6)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=1.0)
        self.wait(2)
        self.play(FadeOut(hook), run_time=0.5)

        self.play(Write(formula), run_time=2.5)
        self.wait(0.5)

        self.play(formula.animate.scale(1.1), run_time=0.4)
        self.play(formula.animate.scale(1 / 1.1), run_time=0.3)
        self.wait(1)

        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(3)

        self.play(
            FadeOut(subtitle),
            formula.animate.move_to(UP * 2.8).scale(0.75),
            run_time=1,
        )
        self.end_pause(1)
