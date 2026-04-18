from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDComponentsSummary(BaseScene):
    def construct(self):
        # Title
        title = vn_text("Các bước trong ma trận phân rã", size=48, weight="BOLD", color=COLOR_ACCENT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)

        # Formula
        formula = MathTex(r"A = U \Sigma V^{T}", font_size=60)
        formula[0][0].set_color(COLOR_ACCENT)  # A
        formula[0][2].set_color(COLOR_U)        # U
        formula[0][3:6].set_color(COLOR_SIGMA)  # Sigma
        formula[0][7:9].set_color(COLOR_V)      # V^T
        formula.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(formula), run_time=1.0)
        self.wait(1.0)

        # V^T description (left column) — dùng MathTex cho ký hiệu toán học
        v_title = VGroup(
            MathTex(r"V^T", font_size=38, color=COLOR_V),
            vn_text("- Ma trận đầu vào", size=34, weight="BOLD", color=COLOR_V),
        ).arrange(RIGHT, buff=0.16, aligned_edge=DOWN)
        v_items = VGroup(
            MathTex(r"V \in \mathbb{R}^{n \times n}", font_size=26, color=COLOR_TEXT),
            vn_text("Vector riêng của", size=26, color=COLOR_TEXT),
            MathTex(r"A^T A", font_size=26, color=COLOR_V),
            VGroup(
                MathTex(r"V^T V = I", font_size=26, color=COLOR_TEXT),
                vn_text("(trực giao)", size=22, color=COLOR_MUTED),
            ).arrange(RIGHT, buff=0.15),
            vn_text("Bước 1: quay đầu vào", size=24, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        v_group = VGroup(v_title, v_items).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        v_group.move_to(LEFT * 4.5 + DOWN * 0.4)
        safe_fit(v_group, max_w=4.0)

        # Sigma description (center column)
        s_title = vn_text("\u03a3 - Giá trị kỳ dị", size=34, weight="BOLD", color=COLOR_SIGMA)
        s_items = VGroup(
            MathTex(r"\Sigma \in \mathbb{R}^{m \times n}", font_size=26, color=COLOR_TEXT),
            MathTex(r"\sigma_1 \geq \sigma_2 \geq \cdots \geq 0", font_size=24, color=COLOR_TEXT),
            MathTex(r"\sigma_i = \sqrt{\lambda_i(A^T A)}", font_size=24, color=COLOR_SIGMA),
            vn_text("Bước 2: kéo/nén", size=24, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        s_group = VGroup(s_title, s_items).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        s_group.move_to(ORIGIN + DOWN * 0.4)
        safe_fit(s_group, max_w=4.2)

        # U description (right column)
        u_title = vn_text("U - Ma trận đầu ra", size=34, weight="BOLD", color=COLOR_U)
        u_items = VGroup(
            MathTex(r"U \in \mathbb{R}^{m \times m}", font_size=26, color=COLOR_TEXT),
            vn_text("Vector riêng của", size=26, color=COLOR_TEXT),
            MathTex(r"A A^T", font_size=26, color=COLOR_U),
            VGroup(
                MathTex(r"U^T U = I", font_size=26, color=COLOR_TEXT),
                vn_text("(trực giao)", size=22, color=COLOR_MUTED),
            ).arrange(RIGHT, buff=0.15),
            vn_text("Bước 3: quay đầu ra", size=24, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        u_group = VGroup(u_title, u_items).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        u_group.move_to(RIGHT * 4.5 + DOWN * 0.4)
        safe_fit(u_group, max_w=4.0)

        # Animate in sequence
        self.play(FadeIn(v_group, shift=LEFT * 0.3), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(s_group, shift=DOWN * 0.3), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(u_group, shift=RIGHT * 0.3), run_time=1.0)
        self.wait(1.5)

        # Summary note
        sigma_note = VGroup(
            MathTex(r"\sigma_i", font_size=34, color=COLOR_ACCENT),
            vn_text("là cầu nối chung giữa U và V", size=30, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2)
        sigma_note.to_edge(DOWN, buff=0.6)
        safe_fit(sigma_note)
        self.play(
            Indicate(v_group, color=COLOR_ACCENT, scale_factor=1.02),
            Indicate(s_group, color=COLOR_ACCENT, scale_factor=1.02),
            Indicate(u_group, color=COLOR_ACCENT, scale_factor=1.02),
            run_time=1.2,
        )
        self.play(FadeIn(sigma_note, shift=UP * 0.1), run_time=0.8)
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(VGroup(formula, v_group, s_group, u_group, sigma_note)),
            run_time=0.9,
        )
        self.end_pause(1)
