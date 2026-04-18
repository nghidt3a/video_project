from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDWhyQuestion(BaseScene):
    def construct(self):
        # Intro nhắc lại công thức
        formula = MathTex(r"A = U \Sigma V^T", font_size=54).move_to(UP * 2.8)
        formula[0][0].set_color(COLOR_ACCENT)
        formula[0][2].set_color(COLOR_U)
        formula[0][3:6].set_color(COLOR_SIGMA)
        formula[0][7:9].set_color(COLOR_V)
        self.play(FadeIn(formula), run_time=0.7)
        self.wait(0.5)

        # Ba câu hỏi tu từ
        q1 = vn_text("Tại sao U và V là các ma trận trực giao?", size=30)
        q2 = vn_text("Tại sao các cột của chúng phải vuông góc nhau?", size=30)
        # Dùng VGroup để kết hợp text và ký hiệu toán học
        q3_text = vn_text("Và các giá trị kỳ dị", size=30)
        q3_math = MathTex(r"\sigma_i", font_size=34, color=COLOR_SIGMA)
        q3_end = vn_text("đến từ đâu?", size=30)
        q3 = VGroup(q3_text, q3_math, q3_end).arrange(RIGHT, buff=0.15)

        questions = VGroup(q1, q2, q3).arrange(DOWN, buff=0.4)
        questions.move_to(UP * 0.6)

        ata_question = MathTex(r"A^T A = \;?", font_size=64)
        ata_question.move_to(DOWN * 1.2)

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

        # VO cue: pivot to AᵀA — chìa khóa là A^TA
        self.play(FadeOut(questions, shift=UP * 0.3), run_time=0.8)
        self.play(Write(ata_question), run_time=1)

        # Nhấn mạnh một lần duy nhất, gọn gàng
        self.play(Indicate(ata_question, color=COLOR_ACCENT, scale_factor=1.2), run_time=0.8)
        self.wait(1)

        self.play(
            ata_question.animate.move_to(UP * 2.8).scale(0.6),
            run_time=0.8,
        )

        self.end_pause(1)
