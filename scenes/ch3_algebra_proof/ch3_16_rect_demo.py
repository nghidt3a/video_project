from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDRectangularDemo(BaseScene):
    def construct(self):
        title = self.title_banner("Ma trận chữ nhật A (2×3)")
        A_tex = MathTex(r"A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 4 \end{pmatrix}", font_size=34).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(title), Write(A_tex), run_time=1.2)

        AAt_group = VGroup(
            MathTex(r"AA^T", font_size=30, color=COLOR_U),
            MathTex(r"= \begin{pmatrix} 6 & 11 \\ 11 & 21 \end{pmatrix}", font_size=28),
            vn_text("2×2", size=22, color=COLOR_U),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 3.5 + DOWN * 0.2)

        AtA_group = VGroup(
            MathTex(r"A^TA", font_size=30, color=COLOR_V),
            MathTex(r"= \begin{pmatrix} 2 & 3 & 6 \\ 3 & 5 & 10 \\ 6 & 10 & 20 \end{pmatrix}", font_size=26),
            vn_text("3×3", size=22, color=COLOR_V),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 3.0 + DOWN * 0.2)
        divider = DashedLine(UP * 1.5, DOWN * 2.2, color=COLOR_MUTED, dash_length=0.12)

        self.play(FadeIn(AAt_group, shift=DOWN * 0.15), Create(divider), FadeIn(AtA_group, shift=DOWN * 0.15), run_time=1.2)

        eig_AAt = VGroup(
            MathTex(r"\lambda_1 \approx 26.79", font_size=22, color=COLOR_SIGMA),
            MathTex(r"\lambda_2 \approx 0.21", font_size=22, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.15).next_to(AAt_group, DOWN, buff=0.35)
        eig_AtA = VGroup(
            MathTex(r"\lambda_1 \approx 26.79", font_size=22, color=COLOR_SIGMA),
            MathTex(r"\lambda_2 \approx 0.21", font_size=22, color=COLOR_SIGMA),
            MathTex(r"\lambda_3 = 0", font_size=22, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.15).next_to(AtA_group, DOWN, buff=0.35)
        self.play(FadeIn(eig_AAt), FadeIn(eig_AtA), run_time=1.2)

        box_left = SurroundingRectangle(eig_AAt[0], color=COLOR_ACCENT, buff=0.1, corner_radius=0.08)
        box_right = SurroundingRectangle(eig_AtA[0], color=COLOR_ACCENT, buff=0.1, corner_radius=0.08)
        connector = DashedLine(box_left.get_right(), box_right.get_left(), color=COLOR_ACCENT, dash_length=0.12)
        self.play(Create(box_left), Create(box_right), Create(connector), run_time=0.9)

        note = VGroup(
            MathTex(r"\sigma_i = \sqrt{\lambda_i}", font_size=26),
            vn_text("và λ₃=0 là chiều bị ép dẹt", size=22, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
