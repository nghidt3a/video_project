from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SideBySideCompare(BaseScene):
    def construct(self):
        A = np.array(A_DEMO, dtype=float)
        U, S, Vt = np.linalg.svd(A)
        Sigma = np.diag(S)

        A_mat = np.array([[A[0, 0], A[0, 1], 0],
                          [A[1, 0], A[1, 1], 0],
                          [0, 0, 1]])
        Vt_mat = np.array([[Vt[0, 0], Vt[0, 1], 0],
                           [Vt[1, 0], Vt[1, 1], 0],
                           [0, 0, 1]])
        S_mat = np.array([[S[0], 0, 0],
                          [0, S[1], 0],
                          [0, 0, 1]])
        U_mat = np.array([[U[0, 0], U[0, 1], 0],
                          [U[1, 0], U[1, 1], 0],
                          [0, 0, 1]])

        # Left half
        plane_L = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            background_line_style={"stroke_opacity": 0.35, "stroke_width": 1},
        ).shift(LEFT * 3.5)
        circle_L = Circle(radius=plane_L.get_x_unit_size(), color=WHITE, stroke_width=2)
        circle_L.move_to(plane_L.get_origin())
        label_L = vn_text("A trực tiếp", size=24, color=COLOR_ACCENT)
        label_L.next_to(plane_L, UP, buff=0.2)

        # Right half
        plane_R = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=5, y_length=5,
            background_line_style={"stroke_opacity": 0.35, "stroke_width": 1},
        ).shift(RIGHT * 3.5)
        circle_R = Circle(radius=plane_R.get_x_unit_size(), color=WHITE, stroke_width=2)
        circle_R.move_to(plane_R.get_origin())
        label_R = MathTex(r"V^T \to \Sigma \to U", font_size=32, color=COLOR_SIGMA)
        label_R.next_to(plane_R, UP, buff=0.2)

        self.play(
            Create(plane_L), Create(plane_R),
            Create(circle_L), Create(circle_R),
            FadeIn(label_L), FadeIn(label_R),
            run_time=1.2,
        )
        self.wait(0.5)

        group_L = VGroup(plane_L, circle_L)
        group_R = VGroup(plane_R, circle_R)

        left_anim = ApplyMatrix(A_mat, group_L, about_point=plane_L.get_origin(),
                                run_time=2.5)

        right_seq = Succession(
            ApplyMatrix(Vt_mat, group_R, about_point=plane_R.get_origin(),
                        run_time=0.83),
            ApplyMatrix(S_mat, group_R, about_point=plane_R.get_origin(),
                        run_time=0.83),
            ApplyMatrix(U_mat, group_R, about_point=plane_R.get_origin(),
                        run_time=0.84),
        )

        self.play(AnimationGroup(left_anim, right_seq, lag_ratio=0), run_time=2.5)
        self.wait(0.5)

        badge = make_badge("✓ TRÙNG KHỚP", color=COLOR_SIGMA)
        badge.to_edge(UP, buff=0.3)
        self.play(FadeIn(badge), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.end_pause(1)
