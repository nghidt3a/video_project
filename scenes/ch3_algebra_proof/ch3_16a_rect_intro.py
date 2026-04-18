from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDRectIntro(BaseScene):
    """Scene dẫn dắt: mở rộng SVD sang ma trận chữ nhật tổng quát."""

    def construct(self):
        title = self.title_banner("Mở rộng: Ma trận chữ nhật")
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)

        # Đến nay chúng ta dùng ma trận vuông làm ví dụ
        note_square = VGroup(
            vn_text("Đến nay:", size=26, color=COLOR_MUTED),
            MathTex(r"A \in \mathbb{R}^{2 \times 2}", font_size=36, color=COLOR_TEXT),
            vn_text("(ma trận vuông)", size=24, color=COLOR_MUTED),
        ).arrange(RIGHT, buff=0.3)
        note_square.move_to(UP * 1.2)

        # Thực ra SVD áp dụng cho mọi m × n
        note_rect = VGroup(
            vn_text("Thực ra SVD áp dụng cho:", size=26, color=COLOR_ACCENT),
            MathTex(r"A \in \mathbb{R}^{m \times n}", font_size=40, color=COLOR_ACCENT),
            vn_text("(bất kỳ m, n)", size=24, color=COLOR_MUTED),
        ).arrange(RIGHT, buff=0.3)
        note_rect.move_to(DOWN * 0.2)

        # Kích thước từng thành phần
        dim_table = VGroup(
            VGroup(
                MathTex(r"U:", font_size=30, color=COLOR_U),
                MathTex(r"m \times m", font_size=30, color=COLOR_TEXT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\Sigma:", font_size=30, color=COLOR_SIGMA),
                MathTex(r"m \times n", font_size=30, color=COLOR_TEXT),
                vn_text("(hình chữ nhật)", size=22, color=COLOR_MUTED),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"V^T:", font_size=30, color=COLOR_V),
                MathTex(r"n \times n", font_size=30, color=COLOR_TEXT),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        dim_table.move_to(DOWN * 1.8)
        safe_fit(dim_table)

        self.play(FadeIn(note_square, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(0.8)

        self.play(
            note_square.animate.set_opacity(0.4),
            FadeIn(note_rect, shift=UP * 0.2),
            run_time=0.8,
        )
        self.wait(0.8)

        self.play(FadeIn(dim_table, shift=UP * 0.1), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
