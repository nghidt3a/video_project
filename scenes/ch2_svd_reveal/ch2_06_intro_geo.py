from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene

import numpy as np


class SVDIntroScene(BaseScene):
    def construct(self):
        A = np.array([[3, 1], [1, 2], [1, 0]], dtype=float)
        U_full, s, Vt = np.linalg.svd(A, full_matrices=True)

        # Trục tọa độ đầu vào (input space R^2)
        axes_2d = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=4, y_length=4,
            axis_config={"include_tip": True, "tip_length": 0.15},
        ).move_to(LEFT * 3.5)
        labels_2d = axes_2d.get_axis_labels(x_label="x", y_label="y")

        unit_circle = Circle(
            radius=axes_2d.get_x_unit_size(), color=COLOR_TEXT, stroke_width=2
        ).move_to(axes_2d.get_origin())

        A_matrix = MathTex(
            r"A = \begin{pmatrix} 3 & 1 \\ 1 & 2 \\ 1 & 0 \end{pmatrix}",
            font_size=32,
        ).move_to(ORIGIN + UP * 1.5)

        transform_arrow = MathTex(r"\xrightarrow{\;A\;}", font_size=40).move_to(ORIGIN)

        # Trục tọa độ đầu ra (output space R^3 — chiếu 2D)
        SCALE = 0.7
        axes_out = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=4, y_length=4,
            axis_config={"include_tip": True, "tip_length": 0.12, "color": COLOR_MUTED},
        ).move_to(RIGHT * 3.5)
        labels_out = axes_out.get_axis_labels(
            x_label=MathTex(r"\sigma_1", font_size=20, color=COLOR_SIGMA),
            y_label=MathTex(r"\sigma_2", font_size=20, color=COLOR_SIGMA),
        )

        result_ellipse = Ellipse(
            width=2 * s[0] * SCALE, height=2 * s[1] * SCALE,
            color=COLOR_SIGMA, stroke_width=2,
        ).move_to(axes_out.get_origin())
        label_s1 = MathTex(rf"\sigma_1 \approx {s[0]:.2f}", font_size=22, color=COLOR_SIGMA)
        label_s2 = MathTex(rf"\sigma_2 \approx {s[1]:.2f}", font_size=22, color=COLOR_SIGMA)
        label_s1.next_to(axes_out.get_origin(), RIGHT, buff=s[0] * SCALE + 0.1)
        label_s2.next_to(axes_out.get_origin(), UP, buff=s[1] * SCALE + 0.1)

        # VO cue: show input space — circle in R^2
        self.play(Create(axes_2d), Write(labels_2d), run_time=1)
        self.play(Create(unit_circle), run_time=1)
        self.wait(1.5)

        self.play(FadeIn(A_matrix), run_time=0.8)
        self.wait(1.0)

        # VO cue: apply A → circle becomes ellipse in output space
        self.play(Write(transform_arrow), run_time=0.6)
        self.play(Create(axes_out), Write(labels_out), run_time=0.8)
        self.play(
            Create(result_ellipse),
            FadeIn(label_s1), FadeIn(label_s2),
            run_time=1.5,
        )
        self.wait(2)

        self.play(
            FadeOut(axes_2d), FadeOut(labels_2d), FadeOut(unit_circle),
            FadeOut(A_matrix), FadeOut(transform_arrow),
            FadeOut(axes_out), FadeOut(labels_out),
            FadeOut(result_ellipse), FadeOut(label_s1), FadeOut(label_s2),
            run_time=0.8,
        )

        self.end_pause(1)
