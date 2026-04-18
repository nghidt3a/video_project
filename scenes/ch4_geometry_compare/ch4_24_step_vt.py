from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseThreeDScene
import numpy as np


class SVDStep1VTranspose(BaseThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES)
        title = vn_text("Bước 1: Vᵀ — Xoay", size=28, color=COLOR_V)
        self.fix(title)
        title.to_corner(UL, buff=0.4)

        A = np.array(A_DEMO, dtype=float)
        _, _, Vt = np.linalg.svd(A, full_matrices=True)
        V = Vt.T
        v1 = V[:, 0]
        v2 = V[:, 1]
        angle_vt = np.arctan2(v1[1], v1[0])

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2],
            axis_config={"stroke_width": 1, "color": GRAY},
        )
        self.add(axes)

        sphere = Sphere(radius=1.4, resolution=(20, 20))
        sphere.set_fill(opacity=0.18)
        sphere.set_stroke(width=0.8)
        vec_v1 = Arrow3D(ORIGIN, np.array([v1[0], v1[1], 0]) * 1.4, color=COLOR_ACCENT)
        vec_v2 = Arrow3D(ORIGIN, np.array([v2[0], v2[1], 0]) * 1.4, color=COLOR_ACCENT)
        marker = Dot3D(point=np.array([1.4, 0, 0]), color=COLOR_SIGMA, radius=0.06)

        note = VGroup(
            VGroup(MathTex(r"V^T", font_size=30, color=COLOR_V), vn_text("chỉ xoay trong mặt phẳng", size=28)).arrange(RIGHT, buff=0.15),
            VGroup(vn_text("Hình cầu vẫn giữ nguyên hình dạng", size=24), MathTex(r"\checkmark", font_size=24, color=COLOR_SIGMA)).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.18)
        self.fix(note)
        note.to_corner(DR, buff=0.45)

        step_label = vn_text("Bước 1: chỉ quay, không méo", size=22, color=COLOR_V)
        self.fix(step_label)
        step_label.to_corner(DL, buff=0.45)

        self.play(FadeIn(title), FadeIn(sphere), Create(vec_v1), Create(vec_v2), Create(marker), FadeIn(step_label), run_time=1.0)
        self.wait(0.6)

        world = VGroup(sphere, vec_v1, vec_v2, marker)
        self.play(
            Rotate(world, angle=-angle_vt, axis=OUT, about_point=ORIGIN),
            run_time=2.0,
        )
        self.wait(0.8)

        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, note, step_label, world, axes)), run_time=0.8)
        self.end_pause(1)
