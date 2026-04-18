from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDProjectOpening(BaseScene):
    def construct(self):
        title = vn_text(
            "Phân Rã Ma Trận và Trực Quan Hóa với Manim",
            size=40,
            weight="BOLD",
            color=COLOR_ACCENT,
        )
        title.move_to(ORIGIN + UP * 0.4)

        subtitle = vn_text("Visual SVD journey", size=26, color=COLOR_MUTED)
        subtitle.next_to(title, DOWN, buff=0.35)

        formula = MathTex(r"A = U\Sigma V^T", font_size=54)
        formula.next_to(subtitle, DOWN, buff=0.5)
        formula[0][2].set_color(COLOR_U)
        formula[0][3:6].set_color(COLOR_SIGMA)
        formula[0][7:9].set_color(COLOR_V)

        accent_left = Line(LEFT * 5.2, LEFT * 1.1, color=COLOR_U, stroke_width=6).shift(UP * 1.7)
        accent_right = Line(RIGHT * 1.1, RIGHT * 5.2, color=COLOR_V, stroke_width=6).shift(UP * 1.7)
        accent_bottom = Line(LEFT * 3.6, RIGHT * 3.6, color=COLOR_SIGMA, stroke_width=4).shift(DOWN * 1.9)

        self.play(Create(accent_left), Create(accent_right), Create(accent_bottom), run_time=0.8)
        self.play(Write(title), run_time=1.3)
        self.play(FadeIn(subtitle, shift=UP * 0.1), run_time=0.6)
        self.play(Write(formula), run_time=1.4)
        self.wait(1.8)
        self.play(FadeOut(VGroup(title, subtitle, formula, accent_left, accent_right, accent_bottom)), run_time=0.8)
        self.wait(19.8)
        self.end_pause(1)
