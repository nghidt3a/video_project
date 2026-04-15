from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDNumericalExample(BaseScene):
    def construct(self):
        # VO cue: intro numerical example
        title = self.title_banner("Ví dụ cụ thể")
        self.play(FadeIn(title), run_time=0.5)

        def step_badge(step_num, total=3, color=COLOR_ACCENT):
            return make_badge(f"Bước {step_num}/{total}", color=color).to_corner(UR, buff=0.4)

        mat_A = MathTex(
            r"A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}",
            font_size=56,
        ).move_to(ORIGIN)
        self.play(Write(mat_A), run_time=1.2)
        self.wait(2)

        mat_A_small = mat_A.copy().scale(0.55).to_corner(UL, buff=0.5).shift(DOWN * 0.5)
        self.play(Transform(mat_A, mat_A_small), run_time=0.8)

        # VO cue: energy interpretation
        energy = MathTex(r"\|Ax\|^2 = x^T A^T A x", font_size=40, color=COLOR_ACCENT)
        energy.move_to(UP * 2.2)
        energy_note = vn_text("năng lượng co giãn", size=22, color=COLOR_MUTED).next_to(energy, DOWN, buff=0.2)
        self.play(Write(energy), FadeIn(energy_note), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(energy), FadeOut(energy_note), run_time=0.4)

        # VO cue: phase 1 AtA
        badge1 = step_badge(1)
        self.play(FadeIn(badge1), run_time=0.3)

        ata_expand = MathTex(
            r"A^T A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}^T"
            r"\begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}",
            font_size=36,
        ).move_to(UP * 0.8)
        ata_result = MathTex(
            r"= \begin{pmatrix} 10 & 5 \\ 5 & 5 \end{pmatrix}",
            font_size=44,
        ).next_to(ata_expand, DOWN, buff=0.4)
        sym_note = vn_text("(AᵀA là ma trận đối xứng)", size=22, color=COLOR_MUTED)
        sym_note.next_to(ata_result, DOWN, buff=0.3)

        self.play(Write(ata_expand), run_time=1.2)
        self.wait(0.8)
        self.play(TransformFromCopy(ata_expand, ata_result), run_time=1)
        self.play(FadeIn(sym_note), run_time=0.5)
        self.wait(2)

        self.play(FadeOut(ata_expand), FadeOut(ata_result), FadeOut(sym_note), FadeOut(badge1), run_time=0.5)

        # VO cue: phase 2 eigenvalues
        badge2 = step_badge(2)
        self.play(FadeIn(badge2), run_time=0.3)

        char_poly = MathTex(r"\det(A^TA - \lambda I) = 0", font_size=36).move_to(UP * 1.2)
        poly_expand = MathTex(r"\lambda^2 - 15\lambda + 25 = 0", font_size=38).next_to(char_poly, DOWN, buff=0.4)
        eigvals = MathTex(r"\lambda_1 \approx 13.09 \qquad \lambda_2 \approx 1.91", font_size=40).next_to(poly_expand, DOWN, buff=0.5)
        box_eig = SurroundingRectangle(eigvals, color=COLOR_ACCENT, buff=0.12, corner_radius=0.1)

        self.play(Write(char_poly), run_time=0.8)
        self.wait(0.8)
        self.play(Write(poly_expand), run_time=0.8)
        self.wait(1)
        self.play(Write(eigvals), run_time=1)
        self.play(Create(box_eig), run_time=0.5)
        self.wait(2)

        self.play(FadeOut(char_poly), FadeOut(poly_expand), FadeOut(eigvals), FadeOut(box_eig), FadeOut(badge2), run_time=0.5)

        # VO cue: phase 3 singular values
        badge3 = step_badge(3, color=COLOR_SIGMA)
        self.play(FadeIn(badge3), run_time=0.3)

        sigma_formula = MathTex(r"\sigma_i = \sqrt{\lambda_i}", font_size=44).move_to(UP * 1.0)
        sigma_vals = MathTex(
            r"\sigma_1 = \sqrt{13.09} \approx", r"3.62", r"\qquad",
            r"\sigma_2 = \sqrt{1.91} \approx", r"1.38",
            font_size=36,
        ).next_to(sigma_formula, DOWN, buff=0.5)
        sigma_vals[1].set_color(COLOR_SIGMA)
        sigma_vals[4].set_color(COLOR_SIGMA)

        self.play(Write(sigma_formula), run_time=0.8)
        self.wait(0.5)
        self.play(Write(sigma_vals), run_time=1.2)
        self.wait(2)

        self.play(FadeOut(sigma_formula), FadeOut(sigma_vals), FadeOut(badge3), run_time=0.5)

        # VO cue: final Sigma result
        sigma_matrix = MathTex(
            r"\Sigma = \begin{pmatrix} 3.62 & 0 \\ 0 & 1.38 \end{pmatrix}",
            font_size=46, color=COLOR_SIGMA,
        )
        result_row = VGroup(
            mat_A.copy().scale(1.6),
            MathTex(r"\Longrightarrow", font_size=40),
            sigma_matrix,
        ).arrange(RIGHT, buff=0.5).move_to(UP * 0.3)
        safe_fit(result_row)

        self.play(FadeOut(mat_A), run_time=0.3)
        self.play(FadeIn(result_row), run_time=1)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
