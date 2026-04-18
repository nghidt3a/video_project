from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDDiagIntro(BaseScene):
    def construct(self):
        # Title kết hợp tiếng Việt + công thức LaTeX
        title = VGroup(
            vn_text("Chéo hóa ma trận:", size=40, weight="BOLD", color=COLOR_ACCENT),
            MathTex(r"A = PDP^{-1}", font_size=46, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.35)
        title.to_edge(UP, buff=0.4)
        safe_fit(title)
        self.play(FadeIn(title), run_time=0.5)

        # --- Định nghĩa ---
        defn_text = vn_text(
            "Ma trận vuông A chéo hóa được nếu tồn tại P khả nghịch và D đường chéo:",
            size=26, color=COLOR_TEXT,
        )
        defn_text.next_to(title, DOWN, buff=0.55)
        safe_fit(defn_text)

        formula_main = MathTex(r"A = PDP^{-1}", font_size=64, color=COLOR_ACCENT)
        formula_main.next_to(defn_text, DOWN, buff=0.45)

        cond = vn_text(
            "Điều kiện: A có n vector riêng độc lập tuyến tính",
            size=24, color=COLOR_MUTED,
        )
        cond.next_to(formula_main, DOWN, buff=0.4)
        safe_fit(cond)

        self.play(FadeIn(defn_text, shift=UP * 0.1), run_time=0.7)
        self.play(Write(formula_main), run_time=1.1)
        self.play(FadeIn(cond, shift=UP * 0.1), run_time=0.6)
        self.wait(1.4)

        self.play(FadeOut(defn_text), FadeOut(formula_main), FadeOut(cond), run_time=0.5)

        # --- Chứng minh nguồn gốc: Av_i = λ_i v_i => AP = PD => A = PDP^{-1} ---
        proof_title = vn_text("Nguồn gốc:", size=28, weight="BOLD", color=COLOR_ACCENT)
        proof_title.next_to(title, DOWN, buff=0.5)
        safe_fit(proof_title)

        steps = VGroup(
            MathTex(r"Av_i = \lambda_i v_i \quad (i = 1,\ldots,n)", font_size=36),
            MathTex(
                r"A\underbrace{[v_1\;v_2\;\cdots\;v_n]}_{P}"
                r"= \underbrace{[v_1\;v_2\;\cdots\;v_n]}_{P}"
                r"\underbrace{\begin{pmatrix}\lambda_1 & & \\ & \ddots & \\ & & \lambda_n\end{pmatrix}}_{D}",
                font_size=28,
            ),
            MathTex(r"AP = PD", font_size=40),
            MathTex(r"APP^{-1} = PDP^{-1}", font_size=36, color=COLOR_MUTED),
            MathTex(r"A = PDP^{-1}", font_size=46, color=COLOR_ACCENT),
        ).arrange(DOWN, buff=0.32)
        steps.next_to(proof_title, DOWN, buff=0.35)
        safe_fit(steps)

        self.play(FadeIn(proof_title, shift=UP * 0.1), run_time=0.5)
        for i, step in enumerate(steps):
            self.play(Write(step), run_time=0.9 if i < 3 else 1.1)
            self.wait(0.35)
            if i == 2:
                box = SurroundingRectangle(step, color=COLOR_SIGMA, buff=0.08)
                self.play(Create(box), run_time=0.5)
                self.wait(0.5)
                self.play(FadeOut(box), run_time=0.3)
            if i == 4:
                box_final = SurroundingRectangle(step, color=COLOR_ACCENT, buff=0.1)
                self.play(Create(box_final), run_time=0.5)
                self.wait(0.8)
                self.play(FadeOut(box_final), run_time=0.3)

        self.wait(0.8)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)

        # --- Cấu trúc trực quan của P và D ---
        title2 = self.title_banner("Cấu trúc của P và D")
        self.play(FadeIn(title2), run_time=0.5)

        p_label = vn_text("P  =  ma trận các vector riêng (cột):", size=26, color=COLOR_V)
        p_label.shift(UP * 1.4 + LEFT * 0.5)
        safe_fit(p_label)

        p_mat = MathTex(
            r"P = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \cdots & v_n \\ | & | & & | \end{pmatrix}",
            font_size=38, color=COLOR_V,
        )
        p_mat.next_to(p_label, DOWN, buff=0.25)
        safe_fit(p_mat)

        d_label = vn_text("D  =  ma trận đường chéo các trị riêng:", size=26, color=COLOR_SIGMA)
        d_label.next_to(p_mat, DOWN, buff=0.4)
        safe_fit(d_label)

        d_mat = MathTex(
            r"D = \begin{pmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{pmatrix}",
            font_size=38, color=COLOR_SIGMA,
        )
        d_mat.next_to(d_label, DOWN, buff=0.25)
        safe_fit(d_mat)

        self.play(FadeIn(p_label, shift=RIGHT * 0.1), run_time=0.6)
        self.play(Write(p_mat), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(d_label, shift=RIGHT * 0.1), run_time=0.6)
        self.play(Write(d_mat), run_time=1.0)
        self.wait(1.5)

        summary = vn_text(
            "P chứa thông tin hướng (eigenvectors),  D chứa thông tin độ lớn (eigenvalues)",
            size=22, color=COLOR_MUTED,
        )
        summary.to_edge(DOWN, buff=0.4)
        safe_fit(summary)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(2.0)
        self.end_pause(1)
