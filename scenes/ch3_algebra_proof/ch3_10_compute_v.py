from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDComputeStepByStep(BaseScene):
    def construct(self):
        # VO cue: step 1 — V and Sigma from AtA
        title = self.title_banner("Bước 1: Tính V và Σ từ AᵀA")
        self.play(FadeIn(title), run_time=0.5)

        def step_badge(text, color=COLOR_ACCENT):
            return make_badge(text, color=color).to_corner(UR, buff=0.4)

        A_small = MathTex(
            r"A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=28,
        ).to_corner(UL, buff=0.45).shift(DOWN * 0.5)
        self.play(FadeIn(A_small), run_time=0.5)

        # VO cue: phase 1 compute AtA
        badge1 = step_badge("Giai đoạn 1 / 3")
        self.play(FadeIn(badge1), run_time=0.3)

        AtA_expand = MathTex(
            r"A^T A = \begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix}"
            r"\begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}",
            font_size=32,
        ).move_to(UP * 1.0)
        AtA_result = MathTex(
            r"= \begin{pmatrix} 17 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{pmatrix}",
            font_size=36,
        ).next_to(AtA_expand, DOWN, buff=0.4)
        self.play(Write(AtA_expand), run_time=1.2)
        self.wait(0.5)
        self.play(TransformFromCopy(AtA_expand, AtA_result), run_time=1)
        self.wait(1.7)

        self.play(FadeOut(AtA_expand), FadeOut(AtA_result), FadeOut(badge1), run_time=0.5)

        # VO cue: phase 2 eigenvalues
        badge2 = step_badge("Giai đoạn 2 / 3")
        self.play(FadeIn(badge2), run_time=0.3)

        AtA_label = MathTex(
            r"A^TA = \begin{pmatrix} 17 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{pmatrix}",
            font_size=26,
        ).move_to(LEFT * 3.5 + UP * 1.5)
        char_poly = MathTex(r"\det(A^TA - \lambda I) = 0", font_size=32).move_to(RIGHT * 2.5 + UP * 1.5)
        eigvals = MathTex(
            r"\lambda_1 = 25,\quad \lambda_2 = 9,\quad \lambda_3 = 0",
            font_size=34,
        ).next_to(char_poly, DOWN, buff=0.5)
        box_eig = SurroundingRectangle(eigvals, color=COLOR_ACCENT, buff=0.15, corner_radius=0.1)

        sigma_vals = MathTex(
            r"\sigma_1 = \sqrt{25} = ", r"5",
            r"\qquad \sigma_2 = \sqrt{9} = ", r"3",
            font_size=34,
        ).next_to(eigvals, DOWN, buff=0.6).shift(LEFT * 1.5)
        sigma_vals[1].set_color(COLOR_SIGMA)
        sigma_vals[3].set_color(COLOR_SIGMA)

        Sigma_mat = MathTex(
            r"\Sigma = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}",
            font_size=38, color=COLOR_SIGMA,
        ).next_to(sigma_vals, DOWN, buff=0.5)

        self.play(FadeIn(AtA_label), run_time=0.6)
        self.play(Write(char_poly), run_time=0.8)
        self.wait(0.5)
        self.play(Write(eigvals), Create(box_eig), run_time=1)
        self.wait(0.5)

        # VO cue: lambda_3 = 0 warning
        zero_note = vn_text("\u03bb=0 \u2192 chiều bị ép dẹt", color=COLOR_WARN).scale(0.9)
        zero_note.next_to(box_eig, DOWN, buff=0.25).shift(RIGHT * 2.0)
        self.play(FadeIn(zero_note, shift=UP * 0.1), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(zero_note), run_time=0.3)

        self.play(Write(sigma_vals), run_time=1)
        self.play(FadeIn(Sigma_mat, shift=UP * 0.1), run_time=0.8)
        self.wait(2)

        self.play(
            FadeOut(AtA_label), FadeOut(char_poly),
            FadeOut(eigvals), FadeOut(box_eig),
            FadeOut(sigma_vals), FadeOut(badge2),
            run_time=0.5,
        )
        self.play(Sigma_mat.animate.to_corner(DL, buff=0.5).scale(0.8), run_time=0.8)

        # VO cue: phase 3 eigenvectors -> V
        badge3 = step_badge("Giai đoạn 3 / 3", color=WHITE)
        self.play(FadeIn(badge3), run_time=0.3)

        ev_title = vn_text("Vector riêng của AᵀA → cột của V", size=26)
        ev_title.move_to(UP * 2.0)
        safe_fit(ev_title)
        self.play(FadeIn(ev_title), run_time=0.5)

        eigvec_group = VGroup(
            MathTex(r"\lambda_1=25:\; v_1 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}", font_size=30, color=WHITE),
            MathTex(r"\lambda_2=9:\; v_2 = \tfrac{1}{\sqrt{2}}\begin{pmatrix}-1\\1\\0\end{pmatrix}", font_size=30, color=WHITE),
            MathTex(r"\lambda_3=0:\; v_3 = \begin{pmatrix}0\\0\\-1\end{pmatrix}", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        V_label = MathTex(r"V =", font_size=44, color=WHITE)
        V_cols = VGroup(
            MathTex(r"\tfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\\0\end{pmatrix}", font_size=34, color=WHITE),
            MathTex(r"\tfrac{1}{\sqrt{2}}\begin{pmatrix}-1\\1\\0\end{pmatrix}", font_size=34, color=WHITE),
            MathTex(r"\begin{pmatrix}0\\0\\-1\end{pmatrix}", font_size=34, color=WHITE),
        ).arrange(RIGHT, buff=0.45)
        V_brackets = MathTex(r"\left(\quad\quad\quad\quad\quad\quad\right)", font_size=64, color=WHITE)
        V_brackets.stretch_to_fit_height(V_cols.height + 0.35)
        V_cols.move_to(V_brackets)
        V_fly = VGroup(V_label, V_brackets).arrange(RIGHT, buff=0.2)

        V_mat_final = MathTex(
            r"V = \begin{pmatrix}"
            r"\tfrac{1}{\sqrt{2}} & \tfrac{-1}{\sqrt{2}} & 0 \\" 
            r"\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} & 0 \\" 
            r"0 & 0 & -1"
            r"\end{pmatrix}",
            font_size=36,
            color=WHITE,
        )
        V_mat_final.move_to(V_fly)

        content_row = VGroup(eigvec_group, V_fly).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        safe_fit(content_row, max_w=config.frame_width - 1.2, max_h=config.frame_height - 3.2)
        content_row.move_to(ORIGIN + DOWN * 0.3)
        V_cols.move_to(V_brackets)
        V_mat_final.move_to(V_fly)

        for vec in eigvec_group:
            self.play(FadeIn(vec, shift=RIGHT * 0.2), run_time=1.0)
        self.wait(0.5)

        self.play(FadeIn(V_fly, shift=RIGHT * 0.1), run_time=0.6)
        self.play(
            LaggedStart(
                AnimationGroup(
                    TransformFromCopy(eigvec_group[0], V_cols[0], run_time=0.9),
                    FadeOut(V_cols[0], run_time=0.9),
                    lag_ratio=0.0,
                ),
                AnimationGroup(
                    TransformFromCopy(eigvec_group[1], V_cols[1], run_time=0.9),
                    FadeOut(V_cols[1], run_time=0.9),
                    lag_ratio=0.0,
                ),
                AnimationGroup(
                    TransformFromCopy(eigvec_group[2], V_cols[2], run_time=0.9),
                    FadeOut(V_cols[2], run_time=0.9),
                    lag_ratio=0.0,
                ),
                lag_ratio=0.15,
            ),
            run_time=1.5,
        )
        self.play(FadeOut(V_fly), FadeIn(V_mat_final), run_time=0.6)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
