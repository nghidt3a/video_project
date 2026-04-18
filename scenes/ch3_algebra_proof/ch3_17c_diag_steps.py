from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDDiagSteps(BaseScene):
    def construct(self):
        # Title kết hợp tiếng Việt + công thức LaTeX
        title = VGroup(
            vn_text("Ví dụ số: chéo hóa", size=36, weight="BOLD", color=COLOR_ACCENT),
            MathTex(r"A = PDP^{-1}", font_size=42, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.3)
        title.to_edge(UP, buff=0.4)
        safe_fit(title)
        self.play(FadeIn(title), run_time=0.5)

        # --- Hiển thị ma trận A ---
        a_label = vn_text("Cho ma trận:", size=26, color=COLOR_TEXT)
        a_mat = MathTex(
            r"A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}",
            font_size=48, color=COLOR_ACCENT,
        )
        a_group = VGroup(a_label, a_mat).arrange(RIGHT, buff=0.4, aligned_edge=DOWN)
        a_group.next_to(title, DOWN, buff=0.55)
        safe_fit(a_group)
        self.play(FadeIn(a_label, shift=UP * 0.1), Write(a_mat), run_time=0.9)
        self.wait(0.8)

        # ------------------------------------------------------------------ #
        # Bước 1: Tìm trị riêng
        # ------------------------------------------------------------------ #
        step1_header = vn_text("Bước 1: Tìm trị riêng (eigenvalues)", size=27, weight="BOLD", color=COLOR_V)
        step1_header.next_to(a_group, DOWN, buff=0.45)
        safe_fit(step1_header)

        char_poly = VGroup(
            MathTex(r"\det(A - \lambda I) = 0", font_size=34),
            MathTex(r"(4-\lambda)(3-\lambda) - 2 = 0", font_size=34),
            MathTex(r"\lambda^2 - 7\lambda + 10 = 0", font_size=34),
            MathTex(r"(\lambda - 5)(\lambda - 2) = 0", font_size=34),
        ).arrange(DOWN, buff=0.22)
        char_poly.next_to(step1_header, DOWN, buff=0.3)
        safe_fit(char_poly)

        self.play(FadeIn(step1_header, shift=UP * 0.1), run_time=0.5)
        for line in char_poly:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)

        eigenval_result = MathTex(
            r"\lambda_1 = 5,\quad \lambda_2 = 2",
            font_size=38, color=COLOR_SIGMA,
        )
        eigenval_result.next_to(char_poly, DOWN, buff=0.3)
        box1 = SurroundingRectangle(eigenval_result, color=COLOR_SIGMA, buff=0.1)
        self.play(Write(eigenval_result), run_time=0.8)
        self.play(Create(box1), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(Group(*self.mobjects[1:])), run_time=0.5)

        # ------------------------------------------------------------------ #
        # Bước 2: Tìm vector riêng
        # ------------------------------------------------------------------ #
        step2_header = vn_text("Bước 2: Tìm vector riêng (eigenvectors)", size=27, weight="BOLD", color=COLOR_V)
        step2_header.next_to(title, DOWN, buff=0.5)
        safe_fit(step2_header)
        self.play(FadeIn(step2_header, shift=UP * 0.1), run_time=0.5)

        # λ₁ = 5
        lam1_label = vn_text("Với λ₁ = 5:", size=24, color=COLOR_SIGMA)
        lam1_sys = MathTex(
            r"(A - 5I)v = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} v = \mathbf{0}",
            font_size=32,
        )
        lam1_sol = MathTex(r"\Rightarrow\; v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}", font_size=34, color=COLOR_V)
        lam1_block = VGroup(lam1_label, lam1_sys, lam1_sol).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        lam1_block.next_to(step2_header, DOWN, buff=0.35)
        lam1_block.shift(LEFT * 2.5)
        safe_fit(lam1_block, max_w=6.0)

        # λ₂ = 2
        lam2_label = vn_text("Với λ₂ = 2:", size=24, color=COLOR_SIGMA)
        lam2_sys = MathTex(
            r"(A - 2I)v = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} v = \mathbf{0}",
            font_size=32,
        )
        lam2_sol = MathTex(r"\Rightarrow\; v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}", font_size=34, color=COLOR_V)
        lam2_block = VGroup(lam2_label, lam2_sys, lam2_sol).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        lam2_block.next_to(step2_header, DOWN, buff=0.35)
        lam2_block.shift(RIGHT * 2.5)
        safe_fit(lam2_block, max_w=6.0)

        self.play(FadeIn(lam1_block, shift=UP * 0.1), run_time=0.9)
        self.wait(0.6)
        self.play(FadeIn(lam2_block, shift=UP * 0.1), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(Group(*self.mobjects[1:])), run_time=0.5)

        # ------------------------------------------------------------------ #
        # Bước 3: Lập P và D
        # ------------------------------------------------------------------ #
        step3_header = vn_text("Bước 3: Lập ma trận P và D", size=27, weight="BOLD", color=COLOR_V)
        step3_header.next_to(title, DOWN, buff=0.5)
        safe_fit(step3_header)
        self.play(FadeIn(step3_header, shift=UP * 0.1), run_time=0.5)

        p_tex = MathTex(
            r"P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}",
            font_size=40, color=COLOR_V,
        )
        p_note = vn_text("(cột = vector riêng)", size=22, color=COLOR_MUTED)
        p_group = VGroup(p_tex, p_note).arrange(DOWN, buff=0.15)

        d_tex = MathTex(
            r"D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}",
            font_size=40, color=COLOR_SIGMA,
        )
        d_note = vn_text("(đường chéo = trị riêng)", size=22, color=COLOR_MUTED)
        d_group = VGroup(d_tex, d_note).arrange(DOWN, buff=0.15)

        pd_row = VGroup(p_group, d_group).arrange(RIGHT, buff=1.4)
        pd_row.next_to(step3_header, DOWN, buff=0.45)
        safe_fit(pd_row)

        self.play(FadeIn(p_group, shift=UP * 0.1), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(d_group, shift=UP * 0.1), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(Group(*self.mobjects[1:])), run_time=0.5)

        # ------------------------------------------------------------------ #
        # Bước 4: Kết luận A = PDP^{-1}
        # ------------------------------------------------------------------ #
        step4_header = vn_text("Bước 4: Kết quả", size=27, weight="BOLD", color=COLOR_ACCENT)
        step4_header.next_to(title, DOWN, buff=0.5)
        safe_fit(step4_header)
        self.play(FadeIn(step4_header, shift=UP * 0.1), run_time=0.5)

        result_chain = VGroup(
            MathTex(
                r"P = \begin{pmatrix}1&1\\1&-2\end{pmatrix},\;"
                r"D = \begin{pmatrix}5&0\\0&2\end{pmatrix},\;"
                r"P^{-1} = \begin{pmatrix}\tfrac{2}{3}&\tfrac{1}{3}\\\tfrac{1}{3}&-\tfrac{1}{3}\end{pmatrix}",
                font_size=28,
            ),
            MathTex(
                r"PDP^{-1} = \begin{pmatrix}4&1\\2&3\end{pmatrix} = A \;\checkmark",
                font_size=38, color=COLOR_ACCENT,
            ),
        ).arrange(DOWN, buff=0.4)
        result_chain.next_to(step4_header, DOWN, buff=0.4)
        safe_fit(result_chain)

        self.play(Write(result_chain[0]), run_time=1.1)
        self.wait(0.4)
        self.play(Write(result_chain[1]), run_time=1.0)
        box_result = SurroundingRectangle(result_chain[1], color=COLOR_ACCENT, buff=0.1)
        self.play(Create(box_result), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(Group(*self.mobjects[1:])), run_time=0.5)

        # ------------------------------------------------------------------ #
        # Lưu ý: P không trực giao => P⁻¹ ≠ Pᵀ => chuyển sang spectral
        # ------------------------------------------------------------------ #
        note_header = vn_text("Lưu ý quan trọng:", size=28, weight="BOLD", color=COLOR_WARN)
        note_header.next_to(title, DOWN, buff=0.55)
        safe_fit(note_header)

        note_body = VGroup(
            MathTex(r"v_1 \cdot v_2 = 1\cdot1 + 1\cdot(-2) = -1 \neq 0", font_size=34),
            vn_text("=> v₁ và v₂ KHÔNG vuông góc => P KHÔNG trực giao", size=24, color=COLOR_WARN),
            MathTex(r"P^{-1} \neq P^T", font_size=38, color=COLOR_WARN),
        ).arrange(DOWN, buff=0.32)
        note_body.next_to(note_header, DOWN, buff=0.4)
        safe_fit(note_body)

        bridge = vn_text(
            "Nếu A đối xứng => các eigenvector VUÔNG GÓC => P trực giao => P⁻¹ = Pᵀ",
            size=23, color=COLOR_SIGMA,
        )
        bridge.next_to(note_body, DOWN, buff=0.45)
        safe_fit(bridge)

        bridge2 = MathTex(r"A = PDP^T \quad \text{(Dinh ly pho)}", font_size=34, color=COLOR_SIGMA)
        bridge2.next_to(bridge, DOWN, buff=0.22)
        safe_fit(bridge2)

        self.play(FadeIn(note_header, shift=UP * 0.1), run_time=0.5)
        for item in note_body:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item, shift=UP * 0.1), run_time=0.8)
            self.wait(0.3)
        self.wait(0.6)
        self.play(FadeIn(bridge, shift=UP * 0.1), run_time=0.7)
        self.play(Write(bridge2), run_time=0.8)
        box_bridge = SurroundingRectangle(bridge2, color=COLOR_SIGMA, buff=0.1)
        self.play(Create(box_bridge), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(2.0)
        self.end_pause(1)
