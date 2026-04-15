from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDComputeU(BaseScene):
    def construct(self):
        title = self.title_banner("Bước 2: Tính U từ AAᵀ")
        self.play(FadeIn(title), run_time=0.5)

        A_small = MathTex(
            r"A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=26,
        ).to_corner(UL, buff=0.45).shift(DOWN * 0.5)
        self.play(FadeIn(A_small), run_time=0.4)

        AAt_expand = MathTex(
            r"AA^T = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}"
            r"\begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix}",
            font_size=30,
        ).move_to(UP * 1.3)
        AAt_result = MathTex(
            r"= \begin{pmatrix} 17 & 10 \\ 10 & 17 \end{pmatrix}",
            font_size=42,
        ).next_to(AAt_expand, DOWN, buff=0.3)

        self.play(Write(AAt_expand), run_time=1.1)
        self.wait(0.5)
        self.play(TransformFromCopy(AAt_expand, AAt_result), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(AAt_expand), run_time=0.4)
        self.play(AAt_result.animate.move_to(LEFT * 3.5 + UP * 0.8), run_time=0.5)

        eig_AAt = VGroup(
            MathTex(r"\lambda_1(AA^T) = ", r"25", font_size=30),
            MathTex(r"\lambda_2(AA^T) = ", r"9", font_size=30),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        eig_AAt[0][1].set_color(COLOR_ACCENT)
        eig_AAt[1][1].set_color(COLOR_ACCENT)
        eig_AAt.move_to(LEFT * 3.5 + DOWN * 0.4)

        same_note = VGroup(
            MathTex(r"\lambda_1(A^TA) = ", r"25", font_size=30),
            MathTex(r"\lambda_2(A^TA) = ", r"9", font_size=30),
            MathTex(r"\lambda_3(A^TA) = ", r"0", font_size=30, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        same_note[0][1].set_color(COLOR_ACCENT)
        same_note[1][1].set_color(COLOR_ACCENT)
        same_note.move_to(RIGHT * 3.0 + DOWN * 0.4)

        divider = DashedLine(UP * 0.8, DOWN * 2.2, color=COLOR_MUTED, dash_length=0.1)
        left_label = vn_text("AAᵀ (2x2)", size=22, color=COLOR_U).move_to(LEFT * 3.5 + UP * 1.6)
        right_label = vn_text("AᵀA (3x3)", size=22, color=COLOR_V).move_to(RIGHT * 3.0 + UP * 1.6)

        self.play(FadeIn(left_label), FadeIn(right_label), Create(divider), run_time=0.7)
        self.play(FadeIn(eig_AAt, shift=RIGHT * 0.2), run_time=0.8)
        self.play(FadeIn(same_note, shift=LEFT * 0.2), run_time=0.8)
        self.wait(0.8)

        box_l1 = SurroundingRectangle(eig_AAt[0], color=COLOR_ACCENT, buff=0.08)
        box_r1 = SurroundingRectangle(same_note[0], color=COLOR_ACCENT, buff=0.08)
        box_l2 = SurroundingRectangle(eig_AAt[1], color=COLOR_ACCENT, buff=0.08)
        box_r2 = SurroundingRectangle(same_note[1], color=COLOR_ACCENT, buff=0.08)
        conn1 = DashedLine(box_l1.get_right(), box_r1.get_left(), color=COLOR_ACCENT, dash_length=0.09)
        conn2 = DashedLine(box_l2.get_right(), box_r2.get_left(), color=COLOR_ACCENT, dash_length=0.09)
        self.play(
            Create(box_l1), Create(box_r1), Create(conn1),
            Create(box_l2), Create(box_r2), Create(conn2),
            run_time=0.8,
        )

        same_sigma_note = vn_text("σᵢ khớp nhau cho cả U lẫn V", size=24, color=COLOR_ACCENT).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(same_sigma_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                AAt_result, eig_AAt, same_note, divider,
                left_label, right_label,
                box_l1, box_r1, box_l2, box_r2, conn1, conn2,
                same_sigma_note,
            )),
            run_time=0.5,
        )

        ev_title = vn_text("Vector riêng của AAᵀ → cột của U", size=26).move_to(UP * 1.5)
        self.play(FadeIn(ev_title), run_time=0.5)

        eigvec1 = MathTex(
            r"\lambda_1=25:\; u_1 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}",
            font_size=34, color=COLOR_U,
        ).move_to(LEFT * 3.2 + DOWN * 0.1)
        eigvec2 = MathTex(
            r"\lambda_2=9:\; u_2 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}",
            font_size=34, color=COLOR_U,
        ).move_to(RIGHT * 3.2 + DOWN * 0.1)

        self.play(FadeIn(eigvec1, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeIn(eigvec2, shift=LEFT * 0.2), run_time=0.7)
        self.wait(1)

        U_mat = MathTex(
            r"U = \begin{pmatrix}"
            r"\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} \\"
            r"\tfrac{1}{\sqrt{2}} & \tfrac{-1}{\sqrt{2}}"
            r"\end{pmatrix}",
            font_size=36, color=COLOR_U,
        ).move_to(DOWN * 2.1)
        self.play(TransformFromCopy(VGroup(eigvec1, eigvec2), U_mat), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
