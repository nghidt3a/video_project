from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseThreeDScene
import numpy as np


class SVDSpectralDecomposition(BaseThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        A_mat = np.array([[2, 1, 0], [1, 3, 0], [0, 0, 2]])
        eigenvalues, eigenvectors = np.linalg.eigh(A_mat)

        axes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3],
            axis_config={"stroke_width": 1, "color": GRAY},
        )

        title = MathTex(r"A = PDP^T", r"\quad", r"\text{(Spectral Theorem)}", font_size=34)
        eig_vals_text = MathTex(
            rf"\lambda_1={eigenvalues[0]:.1f},\;"
            rf"\lambda_2={eigenvalues[1]:.1f},\;"
            rf"\lambda_3={eigenvalues[2]:.1f}",
            font_size=20,
        )
        self.fix(title, eig_vals_text)
        title.to_edge(UP, buff=0.3)
        eig_vals_text.to_corner(UL, buff=0.4)

        sphere = Sphere(radius=1, resolution=(20, 20))
        sphere.set_fill_opacity(0.25)
        sphere.set_stroke(width=0.8)

        self.add(axes)
        self.play(FadeIn(title), FadeIn(eig_vals_text), run_time=0.5)
        self.play(Create(sphere), run_time=1.2)

        colors = [RED, GREEN, BLUE]
        for i in range(3):
            vec_arrow = Arrow(ORIGIN, eigenvectors[:, i] * 1.6, color=colors[i], stroke_width=2.5, buff=0)
            self.play(GrowArrow(vec_arrow), run_time=0.4)

        step1 = vn_text("① Pᵀ: Quay vào eigenbasis", size=20, color=COLOR_U)
        step2 = vn_text("② D: Kéo giãn theo eigenvalues", size=20, color=COLOR_SIGMA)
        step3 = vn_text("③ P: Quay về hướng gốc", size=20, color=COLOR_V)
        self.fix(step1, step2, step3)
        for s in [step1, step2, step3]:
            s.to_corner(DL, buff=0.5)
            s.set_opacity(0)

        self.play(step1.animate.set_opacity(1), run_time=0.4)
        self.play(Rotate(sphere, angle=PI / 6, axis=OUT, about_point=ORIGIN), run_time=1.8)

        ellipsoid = Surface(
            lambda u, v: np.array([
                np.sqrt(abs(eigenvalues[0])) * np.cos(u) * np.sin(v),
                np.sqrt(abs(eigenvalues[1])) * np.sin(u) * np.sin(v),
                np.sqrt(abs(eigenvalues[2])) * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(20, 20), fill_opacity=0.25, stroke_width=0.8,
        )
        self.play(step1.animate.set_opacity(0), step2.animate.set_opacity(1), run_time=0.4)
        self.play(ReplacementTransform(sphere, ellipsoid), run_time=2.5)

        self.play(step2.animate.set_opacity(0), step3.animate.set_opacity(1), run_time=0.4)
        self.play(Rotate(ellipsoid, angle=-PI / 6, axis=OUT, about_point=ORIGIN), run_time=1.8)

        insight = VGroup(
            vn_text("Vectơ riêng: KHÔNG đổi hướng khi nhân A", size=24, color=COLOR_ACCENT),
            MathTex(r"A v_i = \lambda_i v_i", font_size=30),
            vn_text("SVD = tổng quát hóa cho ma trận bất kỳ", size=24, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.fix(insight)

        self.play(FadeOut(step3), FadeOut(ellipsoid), FadeOut(axes), run_time=0.5)
        self.play(FadeIn(insight), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
