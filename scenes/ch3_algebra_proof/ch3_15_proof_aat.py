from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDProofAAt(BaseScene):
    def construct(self):
        title = self.title_banner("Chứng minh AAᵀ = UΣ²Uᵀ")
        self.play(FadeIn(title), run_time=0.5)

        chain = VGroup(
            MathTex(r"A = U\Sigma V^T", font_size=40),
            MathTex(r"A^T = V\Sigma^T U^T", font_size=40),
            MathTex(r"AA^T = (U\Sigma V^T)(V\Sigma^T U^T)", font_size=36),
            MathTex(r"AA^T = U\Sigma (V^TV)\Sigma^T U^T", font_size=36),
            MathTex(r"AA^T = U\Sigma^2U^T", font_size=42, color=COLOR_U),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.1)
        safe_fit(chain)

        for i, line in enumerate(chain):
            self.play(Write(line), run_time=0.8 if i < 3 else 1.0)
            self.wait(0.35)
            if i == 3:
                box = SurroundingRectangle(line, color=COLOR_ACCENT, buff=0.08)
                note = MathTex(r"V^TV = I", font_size=30, color=COLOR_ACCENT).next_to(line, RIGHT, buff=0.35)
                self.play(Create(box), FadeIn(note), run_time=0.7)
                self.wait(0.7)
                self.play(FadeOut(box), FadeOut(note), run_time=0.4)

        spectrum_note = vn_text("AAᵀ đối xứng thực => chéo hóa trực giao", size=24, color=COLOR_MUTED)
        spectrum_note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(spectrum_note), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)


class SVDCompareProofATAATA(BaseScene):
    def construct(self):
        title = self.title_banner("Chứng minh song song: AᵀA và AAᵀ")
        self.play(FadeIn(title), run_time=0.5)

        left_title = vn_text("Nhánh AᵀA", size=28, color=COLOR_V)
        right_title = vn_text("Nhánh AAᵀ", size=28, color=COLOR_U)
        left_chain = VGroup(
            MathTex(r"A = U\Sigma V^T", font_size=30),
            MathTex(r"A^TA = (V\Sigma^T U^T)(U\Sigma V^T)", font_size=28, color=COLOR_V),
            MathTex(r"A^TA = V\Sigma^2V^T", font_size=32, color=COLOR_V),
        ).arrange(DOWN, buff=0.28)
        right_chain = VGroup(
            MathTex(r"A = U\Sigma V^T", font_size=30),
            MathTex(r"AA^T = (U\Sigma V^T)(V\Sigma^T U^T)", font_size=28, color=COLOR_U),
            MathTex(r"AA^T = U\Sigma^2U^T", font_size=32, color=COLOR_U),
        ).arrange(DOWN, buff=0.28)

        left_group = VGroup(left_title, left_chain).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_group = VGroup(right_title, right_chain).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        left_group.move_to(LEFT * 3.7 + UP * 0.2)
        right_group.move_to(RIGHT * 3.7 + UP * 0.2)
        safe_fit(left_group, max_w=5.2)
        safe_fit(right_group, max_w=5.2)

        divider = DashedLine(UP * 2.6, DOWN * 1.8, color=COLOR_MUTED, dash_length=0.12)
        self.play(Create(divider), FadeIn(left_title, shift=DOWN * 0.1), FadeIn(right_title, shift=DOWN * 0.1), run_time=0.7)

        for line in left_chain:
            self.play(Write(line), run_time=0.8)
            self.wait(0.25)
        for line in right_chain:
            self.play(Write(line), run_time=0.8)
            self.wait(0.25)

        shared = VGroup(
            MathTex(r"\lambda_i(A^TA) = \lambda_i(AA^T)", font_size=30),
            vn_text("các trị riêng khác 0 trùng nhau", size=24, color=COLOR_MUTED),
            MathTex(r"\sigma_i = \sqrt{\lambda_i}", font_size=32, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.22)
        shared.to_edge(DOWN, buff=0.45)
        safe_fit(shared)
        self.play(FadeIn(shared[0]), FadeIn(shared[1]), Write(shared[2]), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
