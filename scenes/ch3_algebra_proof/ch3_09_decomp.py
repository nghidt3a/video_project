from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDDecompIntro(BaseScene):
    def construct(self):
        # VO cue: problem statement
        title = self.title_banner("Phân rã SVD — Ví dụ số cụ thể")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)

        A_tex = MathTex(
            r"A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=52,
        ).move_to(UP * 0.8)
        self.play(Write(A_tex), run_time=1.2)
        self.wait(1.5)

        # VO cue: unknowns with role badges
        formula_q = MathTex(
            r"A \;=\; ",
            r"\underbrace{?}_{U}", r"\;\cdot\;",
            r"\underbrace{?}_{\Sigma}", r"\;\cdot\;",
            r"\underbrace{?}_{V^T}",
            font_size=48,
        )
        formula_q[1].set_color(COLOR_U)
        formula_q[3].set_color(COLOR_SIGMA)
        formula_q[5].set_color(COLOR_V)
        formula_q.move_to(DOWN * 0.3)
        safe_fit(formula_q)

        self.play(FadeIn(formula_q, shift=UP * 0.2), run_time=1)
        self.wait(1)

        # VO cue: method badges via make_badge
        b_v = make_badge("AᵀA ⇒ V, σᵢ", color=COLOR_V)
        b_u = make_badge("AAᵀ ⇒ U", color=COLOR_U)
        b_sigma = make_badge("Σ = diag(σᵢ)", color=COLOR_SIGMA)
        badges = VGroup(b_v, b_sigma, b_u).arrange(RIGHT, buff=0.4)
        badges.to_edge(DOWN, buff=0.7)
        safe_fit(badges)

        method_label = vn_text("Phương pháp giải:", size=24, color=COLOR_ACCENT)
        method_label.next_to(badges, UP, buff=0.25)

        self.play(FadeIn(method_label, shift=UP * 0.1), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in badges], lag_ratio=0.2),
            run_time=1.2,
        )
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
