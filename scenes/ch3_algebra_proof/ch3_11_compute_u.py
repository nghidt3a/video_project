from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDComputeU(BaseScene):
    def construct(self):
        title = self.title_banner("Bước 2: Tính U từ AAᵀ")
        self.play(FadeIn(title), run_time=0.5)

        def step_badge(text, color=COLOR_ACCENT):
            return make_badge(text, color=color).to_corner(UR, buff=0.4)

        A_small = MathTex(
            r"A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=28,
        ).to_corner(UL, buff=0.45).shift(DOWN * 0.5)
        self.play(FadeIn(A_small), run_time=0.5)

        # Phase 1: compute AAᵀ
        badge1 = step_badge("Giai đoạn 1 / 3")
        self.play(FadeIn(badge1), run_time=0.3)

        aat_expand = MathTex(
            r"A A^T = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}"
            r"\begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix}",
            font_size=32,
        ).move_to(UP * 1.0)
        aat_result = MathTex(
            r"= \begin{pmatrix} 17 & 8 \\ 8 & 17 \end{pmatrix}",
            font_size=36,
        ).next_to(aat_expand, DOWN, buff=0.4)

        self.play(Write(aat_expand), run_time=1.2)
        self.wait(0.5)
        self.play(TransformFromCopy(aat_expand, aat_result), run_time=1.0)
        self.wait(1.7)

        self.play(FadeOut(aat_expand), FadeOut(aat_result), FadeOut(badge1), run_time=0.5)

        # Phase 2: eigenvalues
        badge2 = step_badge("Giai đoạn 2 / 3", color=COLOR_U)
        self.play(FadeIn(badge2), run_time=0.3)

        aat_label = MathTex(
            r"AA^T = \begin{pmatrix} 17 & 8 \\ 8 & 17 \end{pmatrix}",
            font_size=28,
        ).move_to(LEFT * 3.0 + UP * 1.5)
        char_poly = MathTex(r"\det(AA^T - \lambda I) = 0", font_size=32).move_to(RIGHT * 2.5 + UP * 1.5)
        eigvals = MathTex(
            r"\lambda_1 = 25,\quad \lambda_2 = 9",
            font_size=34,
        ).next_to(char_poly, DOWN, buff=0.5)
        box_eig = SurroundingRectangle(eigvals, color=COLOR_U, buff=0.15, corner_radius=0.1)

        eig_note = vn_text("Định lý phổ áp dụng trực tiếp cho AAᵀ", size=22, color=COLOR_MUTED)
        eig_note.next_to(eigvals, DOWN, buff=0.3)

        self.play(FadeIn(aat_label), run_time=0.6)
        self.play(Write(char_poly), run_time=0.8)
        self.wait(0.5)
        self.play(Write(eigvals), Create(box_eig), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(eig_note, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(aat_label), FadeOut(char_poly),
            FadeOut(eigvals), FadeOut(box_eig),
            FadeOut(eig_note), FadeOut(badge2),
            run_time=0.5,
        )

        # Phase 3: eigenvectors → U
        badge3 = step_badge("Giai đoạn 3 / 3", color=COLOR_U)
        self.play(FadeIn(badge3), run_time=0.3)

        ev_title = vn_text("Vector riêng của AAᵀ → cột của U", size=26)
        ev_title.move_to(UP * 2.0)
        safe_fit(ev_title)
        self.play(FadeIn(ev_title), run_time=0.5)

        eigvec_group = VGroup(
            MathTex(r"\lambda_1=25:\; u_1 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}", font_size=30, color=COLOR_U),
            MathTex(r"\lambda_2=9:\; u_2 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}", font_size=30, color=COLOR_U),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        U_label = MathTex(r"U =", font_size=44, color=COLOR_U)
        U_cols = VGroup(
            MathTex(r"\tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}", font_size=34, color=COLOR_U),
            MathTex(r"\tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}", font_size=34, color=COLOR_U),
        ).arrange(RIGHT, buff=0.45)
        U_brackets = MathTex(r"\left(\quad\quad\quad\quad\right)", font_size=64, color=COLOR_U)
        U_brackets.stretch_to_fit_height(U_cols.height + 0.35)
        U_cols.move_to(U_brackets)
        U_fly = VGroup(U_label, U_brackets).arrange(RIGHT, buff=0.2)

        U_mat = MathTex(
            r"U = \begin{pmatrix}"
            r"\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} \\\\"
            r"\tfrac{1}{\sqrt{2}} & \tfrac{-1}{\sqrt{2}}"
            r"\end{pmatrix}",
            font_size=38,
            color=COLOR_U,
        )

        content_row = VGroup(eigvec_group, U_fly).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        safe_fit(content_row, max_w=config.frame_width - 1.2, max_h=config.frame_height - 3.2)
        content_row.move_to(ORIGIN + DOWN * 0.3)
        U_cols.move_to(U_brackets)
        U_mat.move_to(U_fly)

        for vec in eigvec_group:
            self.play(FadeIn(vec, shift=RIGHT * 0.2), run_time=1.0)
        self.wait(0.5)

        self.play(FadeIn(U_fly, shift=RIGHT * 0.1), run_time=0.6)
        self.play(
            LaggedStart(
                AnimationGroup(
                    TransformFromCopy(eigvec_group[0], U_cols[0], run_time=0.9),
                    FadeOut(U_cols[0], run_time=0.9),
                    lag_ratio=0.0,
                ),
                AnimationGroup(
                    TransformFromCopy(eigvec_group[1], U_cols[1], run_time=0.9),
                    FadeOut(U_cols[1], run_time=0.9),
                    lag_ratio=0.0,
                ),
                lag_ratio=0.15,
            ),
            run_time=1.5,
        )
        self.play(FadeOut(U_fly), FadeIn(U_mat), run_time=0.6)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
