from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDDiagonalVsOrthogonal(BaseThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        title = vn_text("Đường chéo vs Trực giao", size=30)
        self.fix(title)
        title.to_edge(UP, buff=0.3)

        axes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3],
            axis_config={"stroke_width": 1, "color": GRAY},
        )
        self.add(axes)
        self.play(FadeIn(title), run_time=0.5)

        part1_title = vn_text("Ma trận đường chéo D", size=24, color=COLOR_SIGMA)
        self.fix(part1_title)
        part1_title.to_edge(UP, buff=0.3).shift(LEFT * 3)

        D_tex = MathTex(
            r"D = \begin{pmatrix}3&0&0\\0&2&0\\0&0&1\end{pmatrix}",
            font_size=24,
        )
        self.fix(D_tex)
        D_tex.to_corner(UR, buff=0.5)

        sphere1 = Sphere(radius=1, resolution=(18, 18))
        sphere1.set_fill(opacity=0.25)
        sphere1.set_stroke(width=0.8)

        ellipsoid1 = Surface(
            lambda u, v: np.array([
                3 * np.cos(u) * np.sin(v),
                2 * np.sin(u) * np.sin(v),
                1 * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(18, 18),
            fill_opacity=0.25, stroke_width=0.8,
        )

        note1 = vn_text("Chỉ phóng to — KHÔNG quay!", size=22, color=COLOR_SIGMA)
        self.fix(note1)
        note1.to_corner(DL, buff=0.5)

        self.play(FadeIn(part1_title), FadeIn(D_tex), run_time=0.6)
        self.play(Create(sphere1), run_time=1.2)
        self.wait(0.8)

        self.play(
            ReplacementTransform(sphere1, ellipsoid1),
            FadeIn(note1),
            run_time=2.5,
        )
        self.wait(2)

        self.play(
            FadeOut(part1_title), FadeOut(D_tex),
            FadeOut(ellipsoid1), FadeOut(note1),
            run_time=0.5,
        )

        part2_title = vn_text("Ma trận trực giao Q", size=24, color=COLOR_U)
        self.fix(part2_title)
        part2_title.to_edge(UP, buff=0.3).shift(LEFT * 3)

        Q_tex = MathTex(
            r"Q = \begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}",
            font_size=24,
        )
        self.fix(Q_tex)
        Q_tex.to_corner(UR, buff=0.5)

        sphere2 = Sphere(radius=1, resolution=(18, 18))
        sphere2.set_fill(opacity=0.25)
        sphere2.set_stroke(width=0.8)

        dot_marker = Dot3D(point=RIGHT, color=COLOR_ACCENT, radius=0.1)

        note2 = vn_text("Chỉ quay — KHÔNG đổi kích thước!", size=22, color=COLOR_U)
        self.fix(note2)
        note2.to_corner(DL, buff=0.5)

        self.play(FadeIn(part2_title), FadeIn(Q_tex), run_time=0.6)
        self.play(Create(sphere2), Create(dot_marker), run_time=1.2)
        self.wait(0.8)

        self.play(
            Rotate(sphere2, angle=PI / 2, axis=OUT, about_point=ORIGIN),
            Rotate(dot_marker, angle=PI / 2, axis=OUT, about_point=ORIGIN),
            FadeIn(note2),
            run_time=2.5,
        )
        self.wait(2)

        self.play(
            FadeOut(part2_title), FadeOut(Q_tex),
            FadeOut(sphere2), FadeOut(dot_marker), FadeOut(note2),
            run_time=0.5,
        )

        conclusion = VGroup(
            VGroup(
                MathTex(r"\Sigma:", font_size=30, color=COLOR_SIGMA),
                vn_text("thay đổi hình dạng", size=26),
            ).arrange(RIGHT, buff=0.3, aligned_edge=DOWN),
            VGroup(
                MathTex(r"U, V:", font_size=30, color=COLOR_U),
                vn_text("thay đổi hướng", size=26),
            ).arrange(RIGHT, buff=0.3, aligned_edge=DOWN),
            vn_text("SVD = kết hợp cả hai!", size=28, color=COLOR_ACCENT),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        self.fix(conclusion)
        conclusion.move_to(ORIGIN)

        self.play(FadeOut(axes), run_time=0.3)
        self.play(FadeIn(conclusion), run_time=1)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
