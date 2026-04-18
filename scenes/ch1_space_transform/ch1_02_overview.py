from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDOverviewScene(BaseScene):
    def construct(self):
        formula = MathTex(
            r"A = U \Sigma V^{T}",
            font_size=64,
        )
        formula[0][0].set_color(COLOR_ACCENT)  # A
        formula[0][2].set_color(COLOR_U)        # U
        formula[0][3:6].set_color(COLOR_SIGMA)  # Sigma
        formula[0][7:9].set_color(COLOR_V)      # V^T
        formula.to_edge(UP, buff=0.4)

        self.play(FadeIn(formula), run_time=1.0)
        self.wait(1.0)

        u_desc = VGroup(
            MathTex(r"U \in \mathbb{R}^{m \times m}", font_size=30, color=COLOR_U),
            MathTex(r"U^T U = I_m", font_size=28, color=COLOR_TEXT),
            vn_text("Ma trận trực giao", size=26, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        u_desc.move_to(LEFT * 4.35 + DOWN * 0.55)

        self.play(FadeIn(u_desc, shift=LEFT * 0.3), run_time=1.0)
        self.wait(1.6)

        sigma_desc = VGroup(
            MathTex(r"\Sigma \in \mathbb{R}^{m \times n}", font_size=30, color=COLOR_SIGMA),
            MathTex(r"\sigma_1 \geq \sigma_2 \geq \cdots \geq 0", font_size=28, color=COLOR_TEXT),
            vn_text("Ma trận đường chéo", size=26, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        sigma_desc.move_to(DOWN * 0.45)

        self.play(FadeIn(sigma_desc, shift=DOWN * 0.3), run_time=1.0)
        self.wait(1.6)

        v_desc = VGroup(
            MathTex(r"V \in \mathbb{R}^{n \times n}", font_size=30, color=COLOR_V),
            MathTex(r"V^T V = I_n", font_size=28, color=COLOR_TEXT),
            vn_text("Ma trận trực giao", size=26, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        v_desc.move_to(RIGHT * 4.35 + DOWN * 0.55)

        self.play(FadeIn(v_desc, shift=RIGHT * 0.3), run_time=1.0)
        self.wait(1.6)

        self.play(
            FadeOut(VGroup(formula, u_desc, sigma_desc, v_desc)),
            run_time=0.8,
        )
        self.end_pause(1)
