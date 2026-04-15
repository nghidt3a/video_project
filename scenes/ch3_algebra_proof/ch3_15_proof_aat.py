from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDProofAAt(BaseScene):
    def construct(self):
        title = self.title_banner("Chứng minh AAᵀ = UΣ²Uᵀ")
        self.play(FadeIn(title), run_time=0.5)

        left = VGroup(
            vn_text("Nhánh AᵀA", size=26, color=COLOR_V),
            MathTex(r"A^TA = V\Sigma^2V^T", font_size=34, color=COLOR_V),
        ).arrange(DOWN, buff=0.25)

        right = VGroup(
            vn_text("Nhánh AAᵀ", size=26, color=COLOR_U),
            MathTex(r"AA^T = U\Sigma^2U^T", font_size=34, color=COLOR_U),
        ).arrange(DOWN, buff=0.25)

        compare = VGroup(left, right).arrange(RIGHT, buff=1.0).move_to(UP * 1.0)
        divider = DashedLine(UP * 2.4, DOWN * 1.6, color=COLOR_MUTED, dash_length=0.12)
        self.play(FadeIn(left, shift=RIGHT * 0.2), Create(divider), FadeIn(right, shift=LEFT * 0.2), run_time=1.0)

        shared = VGroup(
            MathTex(r"\lambda_i(A^TA) = \lambda_i(AA^T)", font_size=34),
            vn_text("cùng các trị riêng khác 0", size=24, color=COLOR_MUTED),
            MathTex(r"\sigma_i = \sqrt{\lambda_i}", font_size=34, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1.0)
        safe_fit(shared)
        self.play(FadeIn(shared[0]), run_time=0.7)
        self.play(FadeIn(shared[1]), run_time=0.5)
        self.play(Write(shared[2]), run_time=0.8)

        sigma_badge_m = make_badge("σᵢ giống nhau", color=COLOR_SIGMA).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(sigma_badge_m), run_time=0.6)
        self.wait(2.2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
