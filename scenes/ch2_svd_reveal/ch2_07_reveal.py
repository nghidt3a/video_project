from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVD_Reveal(BaseScene):
    def construct(self):
        formula = MathTex(r"A \;=\; ", r"U", r"\;\Sigma\;", r"V^T", font_size=56)
        formula.to_edge(UP, buff=0.55)

        comp_U = formula[1]
        comp_S = formula[2]
        comp_V = formula[3]

        comp_U.set_color(COLOR_U)
        comp_S.set_color(COLOR_SIGMA)
        comp_V.set_color(COLOR_V)

        self.play(Write(formula), run_time=1.5)
        self.wait(0.8)

        def make_flat_col(title, symbol, color):
            title_text = vn_text(title, size=30, weight="BOLD", color=color)
            symbol_tex = MathTex(symbol, font_size=40, color=color)
            return VGroup(title_text, symbol_tex).arrange(DOWN, buff=0.4)

        col_V = make_flat_col("Xoay", "V^T", COLOR_V)
        col_S = make_flat_col("Kéo / Nén", r"\Sigma", COLOR_SIGMA)
        col_U = make_flat_col("Xoay", "U", COLOR_U)

        cols = VGroup(col_U, col_S, col_V).arrange(RIGHT, buff=1.8)
        cols.move_to(DOWN * 0.25)

        self.play(
            FadeIn(col_U, shift=UP * 0.2),
            FadeIn(col_S, shift=UP * 0.2),
            FadeIn(col_V, shift=UP * 0.2),
            run_time=1.2,
        )
        self.wait(0.5)

        arrow_U = Arrow(
            comp_U.get_bottom() + DOWN * 0.05,
            col_U.get_top() + UP * 0.1,
            color=COLOR_U, buff=0.1, stroke_width=4,
        )
        arrow_S = Arrow(
            comp_S.get_bottom() + DOWN * 0.05,
            col_S.get_top() + UP * 0.1,
            color=COLOR_SIGMA, buff=0.1, stroke_width=4,
        )
        arrow_V = Arrow(
            comp_V.get_bottom() + DOWN * 0.05,
            col_V.get_top() + UP * 0.1,
            color=COLOR_V, buff=0.1, stroke_width=4,
        )

        self.play(
            Create(arrow_U),
            Create(arrow_S),
            Create(arrow_V),
            run_time=1.2,
        )
        self.wait(0.5)

        self.play(Indicate(col_V, color=COLOR_V, scale_factor=1.15))
        self.play(Indicate(col_S, color=COLOR_SIGMA, scale_factor=1.15))
        self.play(Indicate(col_U, color=COLOR_U, scale_factor=1.15))

        caption = vn_text(
            "Mọi ma trận A chỉ làm 3 việc đơn giản.",
            size=30, color=COLOR_MUTED,
        ).to_edge(DOWN, buff=0.9)

        self.play(FadeIn(caption, shift=UP * 0.2), run_time=0.8)
        self.wait(2)
        self.end_pause(1)
