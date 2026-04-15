from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDResultAssemble(BaseScene):
    def construct(self):
        title = self.title_banner("Kết quả: A = UΣVᵀ")
        self.play(FadeIn(title), run_time=0.5)

        formula = MathTex(r"A \;=\; ", r"U", r"\;\Sigma\;", r"V^T", font_size=52)
        formula[1].set_color(COLOR_U)
        formula[2].set_color(COLOR_SIGMA)
        formula[3].set_color(COLOR_V)
        formula.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(formula), run_time=0.6)

        def mat_card(label, mat_tex, color):
            card = make_card(label, "", width=4.0, color=color)
            mat = MathTex(mat_tex, font_size=24)
            content = VGroup(card, mat).arrange(DOWN, buff=0.2)
            safe_fit(content, max_h=5.0)
            return content

        u_card = mat_card(
            "U",
            r"\begin{pmatrix}\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} & \tfrac{-1}{\sqrt{2}}\end{pmatrix}",
            COLOR_U,
        )
        s_card = mat_card(
            "Σ",
            r"\begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}",
            COLOR_SIGMA,
        )
        vt_card = mat_card(
            "Vᵀ",
            r"\begin{pmatrix}\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} & 0 \\ \tfrac{-1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} & 0 \\ 0 & 0 & -1\end{pmatrix}",
            COLOR_V,
        )
        times1 = MathTex(r"\times", font_size=34)
        times2 = MathTex(r"\times", font_size=34)

        row = VGroup(u_card, times1, s_card, times2, vt_card).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.9)
        safe_fit(row, max_w=config.frame_width - 0.6)

        self.play(FadeIn(u_card, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeIn(times1), FadeIn(s_card, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeIn(times2), FadeIn(vt_card, shift=UP * 0.2), run_time=0.8)
        self.wait(1.2)

        verify = VGroup(
            MathTex(r"U\Sigma V^T = ", font_size=30),
            MathTex(r"\begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}", font_size=30),
            MathTex(r"= A\;\checkmark", font_size=34, color=COLOR_SIGMA),
        ).arrange(RIGHT, buff=0.25).to_edge(DOWN, buff=0.35)
        safe_fit(verify)
        verify_box = SurroundingRectangle(verify, color=COLOR_SIGMA, buff=0.15, corner_radius=0.1)

        self.play(FadeIn(verify, shift=UP * 0.15), Create(verify_box), run_time=1.0)
        self.wait(2.3)

        self.play(FadeOut(VGroup(row, verify, verify_box)), formula.animate.move_to(ORIGIN).scale(1.1), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
