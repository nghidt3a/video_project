from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDPCADeepDive(BaseScene):
    def construct(self):
        title = self.title_banner("PCA = SVD của Data Matrix", color=COLOR_SIGMA)

        step1 = VGroup(
            vn_text("Bước 1: Ma trận dữ liệu X", font_size=30),
            MathTex(r"X \in \mathbb{R}^{n \times d}", font_size=32),
            vn_text("n samples, d features", font_size=24, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.3).move_to(UP * 1.5)
        safe_fit(step1)
        self.fix(step1)

        step2 = VGroup(
            vn_text("Bước 2: Trừ mean", font_size=30),
            MathTex(r"X_c = X - \bar{X}", font_size=32),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        safe_fit(step2)
        self.fix(step2)

        self.play(FadeIn(step1), run_time=1)
        self.wait(1)
        self.play(FadeIn(step2), run_time=1)
        self.wait(1)
        self.play(FadeOut(VGroup(step1, step2)), run_time=0.5)

        svd_part = VGroup(
            vn_text("Bước 3: SVD của X_c", font_size=30),
            MathTex(r"X_c = U\Sigma V^T", font_size=36),
            MathTex(r"\Downarrow", font_size=28),
            VGroup(
                VGroup(MathTex(r"U:", font_size=28, color=COLOR_U),
                       vn_text("thành phần chính", font_size=24)).arrange(RIGHT, buff=0.15),
                VGroup(MathTex(r"\Sigma^2:", font_size=28, color=COLOR_SIGMA),
                       vn_text("phương sai được giải thích", font_size=24)).arrange(RIGHT, buff=0.15),
            ).arrange(DOWN, buff=0.3),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        safe_fit(svd_part)
        self.fix(svd_part)

        self.play(FadeIn(svd_part), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(svd_part), run_time=0.5)

        viz_title = vn_text("Chiếu 2D lên PC1", font_size=32).move_to(UP * 2.5)
        self.fix(viz_title)

        rng = np.random.default_rng(7)
        pts = rng.normal(size=(25, 2)) @ np.array([[2.0, 0.0], [0.6, 0.8]])
        pts -= pts.mean(axis=0)
        C = np.cov(pts.T)
        eigvals, eigvecs = np.linalg.eigh(C)
        pc1 = eigvecs[:, np.argmax(eigvals)]
        pc1 = pc1 / np.linalg.norm(pc1)

        scale = 0.8
        dots = VGroup(*[
            Dot(point=np.array([p[0] * scale, p[1] * scale, 0.0]),
                color=COLOR_U, radius=0.06)
            for p in pts
        ]).move_to(ORIGIN)

        line_len = 5.0
        pc_line = Line(
            -line_len * np.array([pc1[0], pc1[1], 0.0]),
            line_len * np.array([pc1[0], pc1[1], 0.0]),
            color=COLOR_V, stroke_width=3,
        )
        pc_label = MathTex(r"\mathrm{PC}_1", font_size=28, color=COLOR_V).next_to(
            pc_line.get_end(), UR, buff=0.15
        )
        self.fix(dots, pc_line, pc_label)

        self.play(FadeIn(viz_title), run_time=0.4)
        self.play(FadeIn(dots), run_time=1)
        self.wait(0.5)
        self.play(Create(pc_line), FadeIn(pc_label), run_time=0.8)
        self.wait(0.5)

        proj_dots = VGroup()
        proj_lines = VGroup()
        for p in pts:
            v = np.array([p[0] * scale, p[1] * scale])
            t = v @ np.array([pc1[0], pc1[1]])
            q = t * np.array([pc1[0], pc1[1]])
            start = np.array([v[0], v[1], 0.0])
            end = np.array([q[0], q[1], 0.0])
            proj_lines.add(DashedLine(start, end, stroke_width=1.5, color=COLOR_MUTED))
            proj_dots.add(Dot(point=end, color=COLOR_V, radius=0.06))
        self.fix(proj_lines, proj_dots)

        self.play(Create(proj_lines), run_time=1.0)
        self.play(FadeIn(proj_dots), run_time=0.8)
        self.wait(1.5)

        annotation = vn_text("variance explained = σᵢ² / Σσⱼ²",
                             font_size=28, color=COLOR_SIGMA).to_edge(DOWN, buff=0.5)
        safe_fit(annotation)
        self.fix(annotation)
        self.play(FadeIn(annotation), run_time=0.8)
        self.wait(2)

        self.play(
            FadeOut(VGroup(viz_title, dots, pc_line, pc_label,
                           proj_lines, proj_dots, annotation, title)),
            run_time=0.8,
        )
        self.end_pause(1)
