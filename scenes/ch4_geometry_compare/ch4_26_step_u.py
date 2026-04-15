from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDStep3U(BaseThreeDScene):
    def construct(self):
        A = np.array(A_DEMO, dtype=float)
        U_full, s, Vt = np.linalg.svd(A, full_matrices=True)
        s1, s2 = float(s[0]), float(s[1])

        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES)

        step_label = vn_text("Bước 3: U — Xoay", size=28, color=COLOR_U)
        self.fix(step_label)
        step_label.to_corner(UL, buff=0.4)

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2],
            axis_config={"stroke_width": 1, "color": GRAY},
        )
        self.add(axes)

        vec_e1 = Arrow3D(ORIGIN, RIGHT * s1, color=COLOR_U)
        vec_e2 = Arrow3D(ORIGIN, UP * s2, color=COLOR_V)

        result_ellipse = Ellipse(
            width=2 * s1, height=2 * s2,
            color=WHITE, stroke_width=2,
        )

        note_u = VGroup(
            VGroup(
                MathTex(r"U:", font_size=24, color=COLOR_U),
                vn_text("quay về không gian", size=24),
                MathTex(r"\mathbb{R}^3", font_size=24),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                vn_text("Hình elip không đổi hình dáng", size=22),
                MathTex(r"\checkmark", font_size=22, color=COLOR_SIGMA),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15)
        self.fix(note_u)
        note_u.to_corner(DR, buff=0.5)

        self.play(FadeIn(step_label), run_time=0.5)
        self.play(Create(result_ellipse), Create(vec_e1), Create(vec_e2), run_time=1.0)

        shape_group = VGroup(result_ellipse, vec_e1, vec_e2)
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

        # Compare final ellipse with direct-A ellipse
        direct_ellipse = Ellipse(
            width=2 * s1, height=2 * s2,
            color=COLOR_ACCENT, stroke_width=2,
        )
        direct_ellipse.rotate(PI / 6, axis=UP, about_point=ORIGIN)
        direct_ellipse.rotate(PI / 8, axis=RIGHT, about_point=ORIGIN)

        compare_title_l = vn_text("Áp dụng A trực tiếp", size=20, color=COLOR_ACCENT)
        compare_title_r = vn_text("Áp dụng UΣVᵀ (3 bước)", size=20)
        equal_sign = MathTex(r"=", font_size=40, color=COLOR_SIGMA)

        for mob in [compare_title_l, compare_title_r, equal_sign]:
            self.fix(mob)
        compare_title_l.move_to(LEFT * 4.5 + UP * 1.2)
        compare_title_r.move_to(RIGHT * 3 + UP * 1.2)
        equal_sign.move_to(ORIGIN + DOWN * 0.2)

        self.play(FadeOut(note_u), run_time=0.3)
        self.play(
            FadeIn(compare_title_l), FadeIn(compare_title_r),
            FadeIn(direct_ellipse),
            FadeIn(equal_sign),
            run_time=1.2,
        )
        self.wait(1.5)

        self.play(
            FadeOut(compare_title_l), FadeOut(compare_title_r),
            FadeOut(direct_ellipse), FadeOut(equal_sign),
            FadeOut(step_label), FadeOut(shape_group),
            run_time=0.6,
        )

        final_confirm = MathTex(r"A = U \Sigma V^T \quad \checkmark", font_size=48,
                                color=COLOR_SIGMA)
        self.fix(final_confirm)
        final_confirm.move_to(ORIGIN)

        self.play(Write(final_confirm), run_time=1.5)
        self.play(Indicate(final_confirm, scale_factor=1.1), run_time=1)
        self.wait(2.0)

        self.play(FadeOut(final_confirm), run_time=0.8)
        self.end_pause(1)
