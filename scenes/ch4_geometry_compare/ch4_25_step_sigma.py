from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDStep2Sigma(BaseThreeDScene):
    def construct(self):
        A = np.array(A_DEMO, dtype=float)
        U_full, s, Vt = np.linalg.svd(A, full_matrices=True)
        s1, s2 = float(s[0]), float(s[1])

        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)

        step_label = vn_text("Bước 2: Σ — Kéo/Nén", size=28, color=COLOR_SIGMA)
        self.fix(step_label)
        step_label.to_corner(UL, buff=0.4)

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2],
            axis_config={"stroke_width": 1, "color": GRAY},
        )

        vec_e1 = Arrow3D(ORIGIN, RIGHT, color=COLOR_U)
        vec_e2 = Arrow3D(ORIGIN, UP, color=COLOR_V)
        basis = VGroup(vec_e1, vec_e2)

        SCALE = 1.0
        unit_circle = Circle(radius=SCALE, color=WHITE, stroke_width=2)
        result_ellipse = Ellipse(width=2 * s1 * SCALE, height=2 * s2 * SCALE,
                                 color=WHITE, stroke_width=2)

        axis_major = Arrow(ORIGIN, RIGHT * s1 * SCALE, color=COLOR_SIGMA, buff=0, stroke_width=3)
        axis_minor = Arrow(ORIGIN, UP * s2 * SCALE, color=COLOR_SIGMA, buff=0, stroke_width=3)
        label_s1 = MathTex(rf"\sigma_1 \approx {s1:.1f}", font_size=26, color=COLOR_SIGMA)
        label_s2 = MathTex(rf"\sigma_2 \approx {s2:.1f}", font_size=26, color=COLOR_SIGMA)
        self.fix(label_s1)
        self.fix(label_s2)
        label_s1.to_edge(RIGHT).shift(UP * 0.8)
        label_s2.to_edge(RIGHT).shift(UP * 0.2)

        note = vn_text("Bước duy nhất đổi hình", color=COLOR_ACCENT)
        self.fix(note)
        note.to_edge(DOWN)

        self.add(axes)
        self.play(FadeIn(step_label), run_time=0.6)
        self.play(Create(unit_circle), *[Create(a) for a in basis], run_time=1)
        self.wait(0.5)

        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.2)
        self.wait(0.3)

        new_e1 = Arrow3D(ORIGIN, RIGHT * s1, color=COLOR_U)
        new_e2 = Arrow3D(ORIGIN, UP * s2, color=COLOR_V)
        self.play(
            Transform(unit_circle, result_ellipse),
            Transform(vec_e1, new_e1),
            Transform(vec_e2, new_e2),
            run_time=2,
        )
        self.wait(0.5)

        self.play(
            GrowArrow(axis_major), FadeIn(label_s1),
            GrowArrow(axis_minor), FadeIn(label_s2),
            run_time=1,
        )
        self.wait(1.2)

        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(step_label), FadeOut(note),
            FadeOut(axis_major), FadeOut(axis_minor),
            FadeOut(label_s1), FadeOut(label_s2),
            run_time=0.7,
        )
        self.end_pause(1)
