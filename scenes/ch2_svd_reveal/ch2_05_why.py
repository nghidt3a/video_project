from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDWhyQuestion(BaseScene):
    def construct(self):
        super().construct()

        q1 = vn_text("Tại sao U và V là các ma trận trực giao?", size=30)
        q2 = vn_text("Tại sao các cột của chúng phải vuông góc nhau?", size=30)
        q3 = vn_text("Và các giá trị kỳ dị sigma_i đến từ đâu?", size=30)

        questions = VGroup(q1, q2, q3).arrange(DOWN, buff=0.35)
        questions.move_to(UP * 0.8)

        ata_question = MathTex(r"A^T A = \;?", font_size=64)
        ata_question.move_to(DOWN * 0.8)

        formula = MathTex(r"A = U \Sigma V^T", font_size=54).move_to(UP * 2.8)
        self.add(formula)
        self.play(FadeOut(formula), run_time=0.5)

        # VO cue: three rhetorical questions appear and are emphasized
        self.play(FadeIn(q1, shift=LEFT * 0.3), run_time=0.7)
        self.play(Indicate(q1, color=COLOR_ACCENT))
        self.wait(1.0)
        self.play(FadeIn(q2, shift=LEFT * 0.3), run_time=0.7)
        self.play(Indicate(q2, color=COLOR_ACCENT))
        self.wait(1.0)
        self.play(FadeIn(q3, shift=LEFT * 0.3), run_time=0.7)
        self.play(Indicate(q3, color=COLOR_ACCENT))
        self.wait(1.5)

        # VO cue: pivot to AᵀA
        self.play(FadeOut(questions, shift=UP * 0.3), run_time=0.8)
        self.play(Write(ata_question), run_time=1)

        self.play(ata_question.animate.set_opacity(0.2), run_time=0.3)
        self.play(ata_question.animate.set_opacity(1.0), run_time=0.3)
        self.play(ata_question.animate.set_opacity(0.2), run_time=0.3)
        self.play(ata_question.animate.set_opacity(1.0), run_time=0.3)
        self.wait(1)

        self.play(
            ata_question.animate.move_to(UP * 2.8).scale(0.6),
            run_time=0.8,
        )

        self.end_pause(1)
