from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDSpectralToSVD(BaseScene):
    def construct(self):
        title = self.title_banner("Từ Spectral đến SVD")
        self.play(FadeIn(title), run_time=0.5)

        limit_group = VGroup(
            MathTex(r"A = PDP^T", font_size=40),
            vn_text("CHỈ cho ma trận đối xứng", size=28, color=COLOR_WARN),
            MathTex(
                r"A = \begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}"
                r"\quad\Rightarrow\quad A \neq A^T",
                font_size=28, color=COLOR_WARN,
            ),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.3)
        self.play(Write(limit_group[0]), run_time=0.8)
        self.play(FadeIn(limit_group[1]), run_time=0.6)
        self.play(Write(limit_group[2]), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(limit_group), run_time=0.5)

        solution_label = vn_text("Giải pháp: SVD", size=30, color=COLOR_SIGMA).next_to(title, DOWN, buff=0.4)
        steps = VGroup(
            VGroup(vn_text("Tìm V:", size=30), MathTex(r"AV = U\Sigma", font_size=32)).arrange(RIGHT, buff=0.15),
            MathTex(r"\Downarrow", font_size=28, color=COLOR_MUTED),
            MathTex(r"A = U\Sigma V^T", font_size=40, color=COLOR_SIGMA),
            vn_text("Áp dụng cho MỌI ma trận m×n", size=28, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 0.3)
        self.play(FadeIn(solution_label), run_time=0.5)
        for step in steps:
            self.play(FadeIn(step, shift=UP * 0.15), run_time=0.5)
            self.wait(0.6)

        self.play(FadeOut(solution_label), FadeOut(steps), run_time=0.5)

        insight_title = vn_text("Mấu chốt:", size=26, color=COLOR_ACCENT).next_to(title, DOWN, buff=0.4)
        insight_body = VGroup(
            MathTex(r"A^TA = VD V^T \Rightarrow V,\;\sigma_i", font_size=30, color=COLOR_V),
            MathTex(r"AA^T = UEU^T \Rightarrow U", font_size=30, color=COLOR_U),
            MathTex(r"\Downarrow", font_size=30, color=COLOR_MUTED),
            MathTex(r"A = U\Sigma V^T", font_size=38, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 0.2)
        self.play(FadeIn(insight_title), run_time=0.4)
        for line in insight_body:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.6)
        self.wait(1.8)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
