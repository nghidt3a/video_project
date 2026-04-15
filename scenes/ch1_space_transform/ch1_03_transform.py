from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class SVDMatrixTransform2D(BaseScene):
    def construct(self):
        A = np.array(A_DEMO)

        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.4},
        )

        e1, e2 = tracked_basis(plane, colors=(COLOR_U, COLOR_V))
        e1_label = MathTex(r"e_1", font_size=28, color=COLOR_U).add_updater(
            lambda m: m.next_to(e1.get_end(), DR, buff=0.1)
        )
        e2_label = MathTex(r"e_2", font_size=28, color=COLOR_V).add_updater(
            lambda m: m.next_to(e2.get_end(), UL, buff=0.1)
        )

        right_angle = RightAngle(e1, e2, length=0.35, quadrant=(1, 1), color=COLOR_ACCENT)

        mat_A = MathTex(
            r"A = \begin{pmatrix} 2.5 & 1.2 \\ 0.8 & 1.5 \end{pmatrix}",
            font_size=36,
        ).to_corner(UL).add_background_rectangle(color=COLOR_BG, opacity=0.7)

        title = vn_text("Ma trận = Phép biến đổi", size=36).to_edge(UP)

        self.play(Create(plane), run_time=1)
        self.play(
            GrowArrow(e1), GrowArrow(e2),
            FadeIn(e1_label), FadeIn(e2_label),
            Create(right_angle),
            run_time=1.5,
        )
        self.play(FadeIn(title), run_time=0.5)
        self.wait(1)

        self.play(FadeIn(mat_A), run_time=0.5)
        self.wait(1)

        self.play(
            plane.animate.apply_matrix(A),
            e1.animate.put_start_and_end_on(ORIGIN, plane.c2p(A[0, 0], A[1, 0])),
            e2.animate.put_start_and_end_on(ORIGIN, plane.c2p(A[0, 1], A[1, 1])),
            FadeOut(right_angle),
            run_time=3,
        )

        deformed_angle = Angle(e1, e2, radius=0.5, color=COLOR_WARN)
        self.play(Create(deformed_angle), run_time=0.8)
        self.wait(2)

        note = VGroup(
            vn_text("Vector bị kéo dãn và quay", size=26),
            MathTex(r"v \mapsto Av", font_size=30),
        ).arrange(DOWN).to_corner(DR)
        note.add_background_rectangle(color=COLOR_BG, opacity=0.7)

        self.play(FadeIn(note), run_time=0.8)
        self.wait(2)

        e1_label.clear_updaters()
        e2_label.clear_updaters()
        self.play(
            FadeOut(VGroup(plane, e1, e2, e1_label, e2_label,
                           deformed_angle, mat_A, title, note)),
            run_time=0.8,
        )
        self.end_pause(1)
