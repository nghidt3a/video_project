from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDProofAtA(BaseScene):
    def construct(self):
        title = self.title_banner("Chứng minh AᵀA = VΣ²Vᵀ")
        self.play(FadeIn(title), run_time=0.5)

        chain = VGroup(
            MathTex(r"A = U\Sigma V^T", font_size=40),
            MathTex(r"A^T = V\Sigma^T U^T", font_size=40),
            MathTex(r"A^TA = (V\Sigma^T U^T)(U\Sigma V^T)", font_size=36),
            MathTex(r"A^TA = V\Sigma^T (U^TU)\Sigma V^T", font_size=36),
            MathTex(r"A^TA = V\Sigma^2V^T", font_size=42, color=COLOR_V),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.1)
        safe_fit(chain)

        for i, line in enumerate(chain):
            self.play(Write(line), run_time=0.8 if i < 3 else 1.0)
            self.wait(0.4)
            if i == 3:
                box = SurroundingRectangle(line, color=COLOR_ACCENT, buff=0.08)
                note = MathTex(r"U^TU = I", font_size=30, color=COLOR_ACCENT).next_to(line, RIGHT, buff=0.4)
                self.play(Create(box), FadeIn(note), run_time=0.7)
                self.wait(0.8)
                self.play(FadeOut(box), FadeOut(note), run_time=0.4)

        spectrum_note = vn_text("AᵀA đối xứng thực ⇒ chéo hóa trực giao", size=24, color=COLOR_MUTED).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(spectrum_note), run_time=0.6)
        self.wait(2.2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
