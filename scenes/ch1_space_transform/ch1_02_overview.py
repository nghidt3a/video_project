from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDOverviewScene(BaseScene):
    def construct(self):
        # VO cue: gioi thieu cong thuc A = U Sigma V^T
        formula = MathTex(
            r"A \;=\; ", r"U", r"\;\Sigma\;", r"V^T",
            font_size=56,
        )
        formula[1].set_color(COLOR_U)
        formula[2].set_color(COLOR_SIGMA)
        formula[3].set_color(COLOR_V)
        formula.move_to(UP * 3.1)

        card_u = make_card(
            title=r"U \in \mathbb{R}^{m \times m}",
            body=[r"U^T U = I_m", r"A v_i = \sigma_i u_i"],
            width=4.2,
            color=COLOR_U,
        )
        card_s = make_card(
            title=r"\Sigma \in \mathbb{R}^{m \times n}",
            body=[
                r"\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0",
                r"\mathrm{diag}(\sigma_1,\sigma_2,\ldots,\sigma_r,0,\ldots)",
            ],
            width=4.6,
            color=COLOR_SIGMA,
        )
        card_v = make_card(
            title=r"V \in \mathbb{R}^{n \times n}",
            body=[r"V^T V = I_n", r"A^T u_i = \sigma_i v_i"],
            width=4.2,
            color=COLOR_V,
        )

        for c in (card_u, card_s, card_v):
            safe_fit(c, max_w=4.6, max_h=2.6)

        card_u.move_to(LEFT * 4.6 + DOWN * 1.1)
        card_s.move_to(ORIGIN + DOWN * 1.1)
        card_v.move_to(RIGHT * 4.6 + DOWN * 1.1)

        sym_u = formula[1]
        sym_s = formula[2]
        sym_v = formula[3]

        def mk_arrow(sym, card, color):
            return Arrow(
                sym.get_bottom() + DOWN * 0.05,
                card.get_top() + UP * 0.05,
                buff=0.10, color=color,
                stroke_width=2.5,
                max_tip_length_to_length_ratio=0.12,
            )

        arr_u = mk_arrow(sym_u, card_u, COLOR_U)
        arr_s = mk_arrow(sym_s, card_s, COLOR_SIGMA)
        arr_v = mk_arrow(sym_v, card_v, COLOR_V)

        # VO cue: xuat hien cong thuc tong quat
        self.play(FadeIn(formula), run_time=0.7)
        self.wait(1.5)

        # VO cue: U - ma tran truc giao, left singular vectors
        self.play(GrowArrow(arr_u), FadeIn(card_u, shift=DOWN * 0.15), run_time=1.0)
        self.wait(4)

        # VO cue: Sigma - singular values giam dan
        self.play(GrowArrow(arr_s), FadeIn(card_s, shift=DOWN * 0.15), run_time=1.0)
        self.wait(4)

        # VO cue: V - ma tran truc giao, right singular vectors
        self.play(GrowArrow(arr_v), FadeIn(card_v, shift=DOWN * 0.15), run_time=1.0)
        self.wait(5)

        # VO cue: tom ket va chuyen canh
        self.play(
            FadeOut(VGroup(arr_u, card_u, arr_s, card_s, arr_v, card_v)),
            run_time=0.8,
        )
        self.end_pause(1)
