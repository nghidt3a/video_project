from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDStep1VTranspose(BaseScene):
    def construct(self):
        self.title_banner("Bước 1: Vᵀ — Xoay", color=COLOR_V)

        A = np.array(A_DEMO, dtype=float)
        U, s, Vt = np.linalg.svd(A, full_matrices=True)
        V = Vt.T
        v1 = V[:, 0]
        v2 = V[:, 1]
        angle_vt = np.arctan2(v1[1], v1[0])

        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.4, "stroke_width": 1},
        ).scale(0.9)

        basis = tracked_basis(plane, colors=(COLOR_U, COLOR_V))

        unit_circle = Circle(radius=plane.get_x_unit_size(), color=WHITE, stroke_width=2)
        unit_circle.move_to(plane.get_origin())

        vec_v1 = Arrow(
            plane.get_origin(),
            plane.get_origin() + np.append(v1, 0) * plane.get_x_unit_size(),
            color=COLOR_ACCENT, stroke_width=2.5, buff=0,
        )
        vec_v2 = Arrow(
            plane.get_origin(),
            plane.get_origin() + np.append(v2, 0) * plane.get_x_unit_size(),
            color=COLOR_ACCENT, stroke_width=2.5, buff=0,
        )
        label_v1 = MathTex(r"v_1", font_size=24).next_to(vec_v1.get_end(), UR, buff=0.1)
        label_v2 = MathTex(r"v_2", font_size=24).next_to(vec_v2.get_end(), UL, buff=0.1)

        note = VGroup(
            VGroup(MathTex(r"V^T:", font_size=28, color=COLOR_V),
                   vn_text("quay thuần túy", size=28)).arrange(RIGHT, buff=0.15),
            VGroup(vn_text("Vòng tròn vẫn là vòng tròn", size=26),
                   MathTex(r"\checkmark", font_size=26, color=COLOR_SIGMA)).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(Create(plane), Create(unit_circle), run_time=1.0)
        self.play(*[GrowArrow(a) for a in basis], run_time=0.8)
        self.play(
            GrowArrow(vec_v1), FadeIn(label_v1),
            GrowArrow(vec_v2), FadeIn(label_v2),
            run_time=1,
        )
        self.wait(1.5)

        world = VGroup(plane, unit_circle, vec_v1, vec_v2, label_v1, label_v2)
        self.play(
            Rotate(world, angle=-angle_vt, about_point=plane.get_origin()),
            run_time=2,
        )
        self.wait(1)

        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(note),
            FadeOut(vec_v1), FadeOut(vec_v2),
            FadeOut(label_v1), FadeOut(label_v2),
            run_time=0.7,
        )
        self.end_pause(1)
