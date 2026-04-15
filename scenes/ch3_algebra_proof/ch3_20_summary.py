from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDComponentsSummary(BaseScene):
    def construct(self):
        formula = MathTex(r"A \;=\; ", r"U", r"\;\Sigma\;", r"V^T", font_size=54)
        formula[1].set_color(COLOR_U)
        formula[2].set_color(COLOR_SIGMA)
        formula[3].set_color(COLOR_V)
        formula.to_edge(UP, buff=0.35)
        self.play(FadeIn(formula), run_time=0.7)

        col_v = make_card("Vᵀ", [
            r"Kích thước: n \times n",
            "Vector riêng của AᵀA",
            "Trực giao: VᵀV = I",
            "Bước 1: quay đầu vào",
        ], width=4.2, color=COLOR_V)
        col_s = make_card("Σ", [
            r"Kích thước: m \times n",
            "σ₁ ≥ σ₂ ≥ ... ≥ 0",
            r"σᵢ = \sqrt{\lambda_i(A^TA)}",
            "Bước 2: kéo/nén",
        ], width=4.2, color=COLOR_SIGMA)
        col_u = make_card("U", [
            r"Kích thước: m \times m",
            "Vector riêng của AAᵀ",
            "Trực giao: UᵀU = I",
            "Bước 3: quay đầu ra",
        ], width=4.2, color=COLOR_U)

        cols = VGroup(col_v, col_s, col_u).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)
        safe_fit(cols, max_w=config.frame_width - 0.5)
        self.play(FadeIn(col_v, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(col_s, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(col_u, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)

        sigma_note = VGroup(
            MathTex(r"\sigma_i", font_size=30),
            vn_text("là cầu nối chung giữa U và V", size=24),
        ).arrange(RIGHT, buff=0.15).set_color(COLOR_ACCENT).to_edge(DOWN, buff=0.35)
        self.play(
            Indicate(col_v, color=COLOR_ACCENT, scale_factor=1.02),
            Indicate(col_s, color=COLOR_ACCENT, scale_factor=1.02),
            Indicate(col_u, color=COLOR_ACCENT, scale_factor=1.02),
            run_time=1.2,
        )
        self.play(FadeIn(sigma_note, shift=UP * 0.1), run_time=0.8)
        self.wait(2.2)
        self.play(FadeOut(VGroup(formula, cols, sigma_note)), run_time=0.9)
        self.end_pause(1)
