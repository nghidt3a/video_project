from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDOrthogonalityExplained(BaseScene):
    def construct(self):
        title = self.title_banner("Vì sao U và V trực giao?")
        self.play(FadeIn(title), run_time=0.5)

        # Điểm 1: A^TA đối xứng → Định lý phổ áp dụng
        point1_header = vn_text("1) A^T.A và A.A^T là ma trận đối xứng:", size=28, weight="BOLD", color=COLOR_U)
        point1_math = MathTex(r"(A^TA)^T = A^T(A^T)^T = A^TA", font_size=32, color=COLOR_TEXT)
        point1_note = vn_text("=> Định lý phổ: chéo hóa trực giao!", size=26, color=COLOR_SIGMA)
        point1 = VGroup(point1_header, point1_math, point1_note).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        point1.move_to(UP * 0.6)
        safe_fit(point1)

        # Điểm 2: Vector riêng ứng với trị riêng khác nhau → vuông góc
        point2_header = vn_text("2) Vector riêng ứng với trị riêng khác nhau:", size=28, weight="BOLD", color=COLOR_V)
        point2_math = MathTex(r"\lambda_i \neq \lambda_j \;\Rightarrow\; v_i \perp v_j", font_size=32, color=COLOR_TEXT)
        point2_note = vn_text("=> Các cột của V (và U) trực giao với nhau!", size=26, color=COLOR_ACCENT)
        point2 = VGroup(point2_header, point2_math, point2_note).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        point2.move_to(DOWN * 1.2)
        safe_fit(point2)

        self.play(FadeIn(point1, shift=UP * 0.15), run_time=0.9)
        self.wait(1.5)
        self.play(FadeIn(point2, shift=UP * 0.15), run_time=0.9)
        self.wait(1.5)

        conclusion = VGroup(
            MathTex(r"V^T V = I,\quad U^T U = I", font_size=34, color=COLOR_ACCENT),
            vn_text("Trực giao = hệ quả tất yếu", size=26, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.2)
        conclusion.to_edge(DOWN, buff=0.55)
        safe_fit(conclusion)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.8)
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
