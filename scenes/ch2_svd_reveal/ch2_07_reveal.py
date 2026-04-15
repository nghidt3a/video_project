from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVD_Reveal(BaseScene):
    def construct(self):
        super().construct()

        # VO cue: reveal the SVD formula A = U Σ Vᵀ
        formula = MathTex("A = U", "\\Sigma", "V^T", font_size=56).to_edge(UP)
        color_mathtex_parts(formula, {1: COLOR_U, 2: COLOR_SIGMA, 3: COLOR_V})

        self.play(Write(formula), run_time=1.5)
        self.wait(0.8)

        # VO cue: three cards for the three geometric operations
        card_V = make_card("Xoay", "Vᵀ", width=3.5, color=COLOR_V)
        card_S = make_card("Kéo / Nén", "Σ", width=3.5, color=COLOR_SIGMA)
        card_U = make_card("Xoay", "U", width=3.5, color=COLOR_U)

        cards = VGroup(card_V, card_S, card_U).arrange(RIGHT, buff=0.5)
        cards.move_to(ORIGIN + DOWN * 0.3)

        self.play(
            FadeIn(card_V, shift=UP * 0.2),
            FadeIn(card_S, shift=UP * 0.2),
            FadeIn(card_U, shift=UP * 0.2),
            run_time=1.2,
        )
        self.wait(0.5)

        # VO cue: arrows from each formula component down to its card
        comp_U = formula[0]  # "A = U" — rightmost char is U; approximate
        comp_S = formula[1]
        comp_V = formula[2]

        arrow_V = Arrow(
            comp_V.get_bottom() + DOWN * 0.05,
            card_V.get_top() + UP * 0.05,
            color=COLOR_V, buff=0.1, stroke_width=4,
        )
        arrow_S = Arrow(
            comp_S.get_bottom() + DOWN * 0.05,
            card_S.get_top() + UP * 0.05,
            color=COLOR_SIGMA, buff=0.1, stroke_width=4,
        )
        arrow_U = Arrow(
            comp_U.get_bottom() + DOWN * 0.05,
            card_U.get_top() + UP * 0.05,
            color=COLOR_U, buff=0.1, stroke_width=4,
        )

        self.play(
            Create(arrow_V), Create(arrow_S), Create(arrow_U),
            run_time=1.2,
        )
        self.wait(0.5)

        # VO cue: pulse cards in reading order Vᵀ → Σ → U
        self.play(Indicate(card_V, color=COLOR_V))
        self.play(Indicate(card_S, color=COLOR_SIGMA))
        self.play(Indicate(card_U, color=COLOR_U))

        # VO cue: bottom caption — "Mọi ma trận A chỉ làm 3 việc đơn giản."
        caption = vn_text(
            "Mọi ma trận A chỉ làm 3 việc đơn giản.",
            size=30, color=COLOR_MUTED,
        ).to_edge(DOWN, buff=0.6)

        self.play(FadeIn(caption, shift=UP * 0.2), run_time=0.8)
        self.wait(2)

        self.end_pause(1)
