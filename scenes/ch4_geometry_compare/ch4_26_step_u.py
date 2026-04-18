from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDStep3U(BaseThreeDScene):
    def construct(self):
        A = np.array(A_DEMO, dtype=float)
        _, s, _ = np.linalg.svd(A, full_matrices=True)
        s1, s2 = float(s[0]), float(s[1])
        z_scale = 0.9

        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)

        title = vn_text("Bước 3: U — Xoay", size=28, color=COLOR_U)
        self.fix(title)
        title.to_corner(UL, buff=0.4)

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2],
            axis_config={"stroke_width": 1, "color": GRAY},
        )
        self.add(axes)

        vec_e1 = Arrow3D(ORIGIN, RIGHT * s1, color=COLOR_U)
        vec_e2 = Arrow3D(ORIGIN, UP * s2, color=COLOR_V)

        result_ellipsoid = Surface(
            lambda u, v: np.array([
                s1 * np.cos(u) * np.sin(v),
                s2 * np.sin(u) * np.sin(v),
                z_scale * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(20, 20),
            fill_opacity=0.2, stroke_width=0.8,
        )

        note_u = VGroup(
            VGroup(
                MathTex(r"U:", font_size=24, color=COLOR_U),
                vn_text("quay về không gian", size=24),
                MathTex(r"\mathbb{R}^3", font_size=24),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                vn_text("Ellipsoid không đổi hình dáng", size=22),
                MathTex(r"\checkmark", font_size=22, color=COLOR_SIGMA),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15)
        self.fix(note_u)
        note_u.to_corner(DR, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(result_ellipsoid), Create(vec_e1), Create(vec_e2), run_time=1.0)

        shape_group = VGroup(result_ellipsoid, vec_e1, vec_e2)
        self.play(
            Rotate(shape_group, angle=PI / 6, axis=UP, about_point=ORIGIN),
            run_time=2,
        )
        self.play(
            Rotate(shape_group, angle=PI / 8, axis=RIGHT, about_point=ORIGIN),
            run_time=1.5,
        )
        self.wait(0.8)

        self.play(FadeIn(note_u), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(note_u), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(shape_group), run_time=0.6)
        self.end_pause(1)
