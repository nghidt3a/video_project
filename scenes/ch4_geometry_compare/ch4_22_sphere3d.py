from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDSphereTransform3D(BaseThreeDScene):
    def construct(self):
        A = np.array([[2, 0.5, 0], [0.5, 1.5, 0.3], [0, 0.3, 1]])
        U, s, Vt = np.linalg.svd(A)

        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

        title = vn_text("Hình cầu → Ellipsoid trong ℝ³", size=30)
        self.fix(title)
        title.to_edge(UP, buff=0.3)

        sigma_info = VGroup(
            MathTex(rf"\sigma_1 \approx {s[0]:.2f}", font_size=20, color=COLOR_U),
            MathTex(rf"\sigma_2 \approx {s[1]:.2f}", font_size=20, color=COLOR_SIGMA),
            MathTex(rf"\sigma_3 \approx {s[2]:.2f}", font_size=20, color=COLOR_V),
        ).arrange(DOWN, buff=0.2)
        self.fix(sigma_info)
        sigma_info.to_corner(DR, buff=0.5)

        axes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3],
            axis_config={"stroke_width": 1, "color": GRAY},
        )
        sphere = Sphere(radius=1.2, resolution=(20, 20))
        sphere.set_fill(opacity=0.25)
        sphere.set_stroke(width=0.8)

        self.add(axes)
        self.play(FadeIn(title), Create(sphere), run_time=1.2)
        self.wait(0.8)

        step1 = vn_text("① Vᵀ: Căn chỉnh singular vectors", size=20, color=COLOR_U)
        self.fix(step1)
        step1.to_corner(DL, buff=0.5)

        self.play(FadeIn(step1), run_time=0.4)
        self.play(
            Rotate(sphere, angle=PI / 5,
                   axis=np.array([1, 0.5, 0.3]),
                   about_point=ORIGIN),
            run_time=1.8,
        )
        self.wait(0.5)

        step2 = vn_text("② Σ: Kéo giãn theo 3 trục chính", size=20, color=COLOR_SIGMA)
        self.fix(step2)
        step2.to_corner(DL, buff=0.5)

        ellipsoid = Surface(
            lambda u, v: np.array([
                s[0] * 1.2 * np.cos(u) * np.sin(v),
                s[1] * 1.2 * np.sin(u) * np.sin(v),
                s[2] * 1.2 * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(20, 20),
            fill_opacity=0.25, stroke_width=0.8,
        )

        self.play(FadeOut(step1), FadeIn(step2), run_time=0.4)
        self.play(
            ReplacementTransform(sphere, ellipsoid),
            FadeIn(sigma_info),
            run_time=2.5,
        )
        self.wait(0.8)

        step3 = vn_text("③ U: Quay về không gian ℝᵐ", size=20, color=COLOR_V)
        self.fix(step3)
        step3.to_corner(DL, buff=0.5)

        self.play(FadeOut(step2), FadeIn(step3), run_time=0.4)
        self.play(
            Rotate(ellipsoid, angle=PI / 4,
                   axis=np.array([0.5, 1, 0.3]),
                   about_point=ORIGIN),
            run_time=2,
        )
        self.wait(0.5)

        self.play(FadeOut(step3), run_time=0.3)

        self.move_camera(phi=50 * DEGREES, theta=20 * DEGREES, run_time=2.5)
        self.wait(1.0)

        note = vn_text("3 trục = 3 σᵢ", size=28, color=COLOR_SIGMA)
        self.fix(note)
        note.to_edge(DOWN)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
