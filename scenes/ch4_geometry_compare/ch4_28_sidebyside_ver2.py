from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np

class SideBySideCompareVer2(BaseScene):
    def construct(self):
        main_title = vn_text("So sánh: Phép biến đổi M và Phân rã SVD")

        main_title.to_edge(UP, buff=0.3)
        self.add(main_title)

        # Định nghĩa ma trận M và tính SVD
        M = np.array([
            [1.5, 0.5],
            [0.5, 1.5]
        ])
        U, S, VT = np.linalg.svd(M)
        Sigma = np.diag(S)

        center_left = LEFT * 3.5 + DOWN * 1.0
        center_right = RIGHT * 3.5 + DOWN * 1.0

        plane_left = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.5}
        )
        circle_left = Circle(radius=2, color=YELLOW)
        group_left = VGroup(plane_left, circle_left).scale(0.4).move_to(center_left)

        title_left = vn_text("Áp dụng ma trận M")
        title_left.next_to(group_left, UP, buff=0.8)
        group_title_left = title_left

        plane_right = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.5}
        )
        circle_right = Circle(radius=2, color=GREEN)
        group_right = VGroup(plane_right, circle_right).scale(0.4).move_to(center_right)

        title_right = MathTex(r"U \Sigma V^T", font_size=36)
        title_right.set_color(YELLOW)
        title_right_label = vn_text("Áp dụng SVD:")
        title_right_full = VGroup(title_right_label, title_right).arrange(RIGHT, buff=0.2)
        title_right_full.next_to(group_right, UP, buff=0.8)
        group_title_right = title_right_full

        self.play(
            FadeIn(group_left), FadeIn(group_right),
            FadeIn(group_title_left), FadeIn(group_title_right)
        )
        self.wait(1)

        self.play(
            group_left.animate.apply_matrix(M, about_point=center_left),
            run_time=3
        )
        self.wait(0.5)

        step_label_1 = vn_text("Bước 1: Xoay")
        step_math_1 = MathTex(r"V^T", font_size=28)
        step_math_1.set_color(COLOR_V)
        step_text = VGroup(step_label_1, step_math_1).arrange(RIGHT, buff=0.2)
        step_group = step_text
        step_group.next_to(group_right, DOWN, buff=0.8)

        self.play(FadeIn(step_group))
        self.play(
            group_right.animate.apply_matrix(VT, about_point=center_right),
            run_time=1.5
        )
        self.wait(0.5)

        step_label_2 = vn_text("Bước 2: Co giãn")
        step_math_2 = MathTex(r"\Sigma", font_size=28)
        step_math_2.set_color(COLOR_SIGMA)
        step_text_2 = VGroup(step_label_2, step_math_2).arrange(RIGHT, buff=0.2)
        step_group_2 = step_text_2
        step_group_2.move_to(step_group)

        self.play(Transform(step_group, step_group_2))
        self.play(
            group_right.animate.apply_matrix(Sigma, about_point=center_right),
            run_time=1.5
        )
        self.wait(0.5)

        step_label_3 = vn_text("Bước 3: Xoay")
        step_math_3 = MathTex(r"U", font_size=28)
        step_math_3.set_color(COLOR_U)
        step_text_3 = VGroup(step_label_3, step_math_3).arrange(RIGHT, buff=0.2)
        step_group_3 = step_text_3
        step_group_3.move_to(step_group)

        self.play(Transform(step_group, step_group_3))
        self.play(
            group_right.animate.apply_matrix(U, about_point=center_right),
            run_time=1.5
        )
        self.wait(1)

        self.play(FadeOut(step_group))
        self.wait(2)
        self.wait(10.5)
        self.end_pause(1)