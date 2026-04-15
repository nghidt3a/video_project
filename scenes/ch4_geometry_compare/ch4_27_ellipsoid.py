from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDEllipsoidPrinciple(BaseThreeDScene):
    def construct(self):
        A = np.array(A_DEMO, dtype=float)
        U_full, s, Vt = np.linalg.svd(A, full_matrices=True)
        s1, s2 = float(s[0]), float(s[1])

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        title = VGroup(
            vn_text("Nguyên lý Ellipsoid", size=30),
            MathTex(r"\mathbb{R}^n \xrightarrow{A} \mathbb{R}^m",
                    font_size=26, color=COLOR_SIGMA),
        ).arrange(RIGHT, buff=0.3)
        self.fix(title)
        title.to_edge(UP, buff=0.35)

        axes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3],
            axis_config={"stroke_width": 1, "color": GRAY},
        )

        # Rank-full sphere
        sphere_full = Sphere(radius=1.0)
        sphere_full.set_fill(opacity=0.2)
        sphere_full.set_stroke(width=0.6)
        sphere_full.move_to(LEFT * 2)

        # Rank-deficient sphere (will collapse one axis)
        sphere_rd = Sphere(radius=1.0)
        sphere_rd.set_fill(opacity=0.2)
        sphere_rd.set_stroke(width=0.6, color=COLOR_WARN)
        sphere_rd.move_to(RIGHT * 2)

        ellipsoid_full = Surface(
            lambda u, v: np.array([
                -2 + s1 * np.cos(u) * np.sin(v),
                s2 * np.sin(u) * np.sin(v),
                0.8 * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(18, 18),
            fill_opacity=0.2, stroke_width=0.5, stroke_color=WHITE,
        )

        ellipsoid_rd = Surface(
            lambda u, v: np.array([
                2 + s1 * np.cos(u) * np.sin(v),
                s2 * np.sin(u) * np.sin(v),
                0.0 * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(18, 18),
            fill_opacity=0.2, stroke_width=0.5, stroke_color=COLOR_WARN,
        )

        lbl_full = vn_text("Rank đầy đủ", size=20, color=COLOR_SIGMA)
        lbl_rd = vn_text("Rank thiếu (một trục = 0)", size=20, color=COLOR_WARN)
        self.fix(lbl_full)
        self.fix(lbl_rd)
        lbl_full.to_corner(DL, buff=0.5)
        lbl_rd.to_corner(DR, buff=0.5)

        self.add(axes)
        self.play(Write(title), run_time=0.6)
        self.play(Create(sphere_full), Create(sphere_rd), run_time=1.5)
        self.wait(0.8)

        self.play(
            ReplacementTransform(sphere_full, ellipsoid_full),
            ReplacementTransform(sphere_rd, ellipsoid_rd),
            FadeIn(lbl_full), FadeIn(lbl_rd),
            run_time=2.5,
        )
        self.wait(1.5)

        note_rank = vn_text("rank(A) = số chiều của ellipsoid", color=COLOR_ACCENT)
        self.fix(note_rank)
        note_rank.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(note_rank), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
