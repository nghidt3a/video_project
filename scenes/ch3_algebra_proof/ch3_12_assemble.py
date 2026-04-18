from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDResultAssemble(BaseScene):
    def construct(self):
        title = self.title_banner("Kết quả phân rã SVD")
        self.play(FadeIn(title), run_time=0.5)

        formula = MathTex(r"A \;=\; ", r"U", r"\;\Sigma\;", r"V^T", font_size=52)
        formula[1].set_color(COLOR_U)
        formula[2].set_color(COLOR_SIGMA)
        formula[3].set_color(COLOR_V)
        formula.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(formula), run_time=0.6)

        # Gộp khai triển và kiểm tra về cùng một hàng
        expansion = MathTex(
            r"A = "
            r"\begin{pmatrix}\tfrac{1}{\sqrt{2}}&\tfrac{1}{\sqrt{2}}\\\tfrac{1}{\sqrt{2}}&\tfrac{-1}{\sqrt{2}}\end{pmatrix}"
            r"\begin{pmatrix}5&0&0\\0&3&0\end{pmatrix}"
            r"\begin{pmatrix}\tfrac{1}{\sqrt{2}}&\tfrac{1}{\sqrt{2}}&0\\\tfrac{-1}{\sqrt{2}}&\tfrac{1}{\sqrt{2}}&0\\0&0&-1\end{pmatrix}"
            r" = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=38,
        )
        safe_fit(expansion, max_w=config.frame_width - 0.7)
        expansion.move_to(ORIGIN)
        self.play(FadeIn(expansion, shift=UP * 0.1), run_time=1.1)
        self.wait(2.3)

        self.play(FadeOut(expansion), formula.animate.move_to(ORIGIN).scale(1.1), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
