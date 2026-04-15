from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np


class MessyTransformation(BaseScene):
    def construct(self):
        # VO cue: khong gian truoc bien doi - ngay ngan
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        circle = Circle(radius=1.5, color=COLOR_U).move_to(ORIGIN)
        e1, e2 = tracked_basis(plane, colors=(COLOR_U, COLOR_V))

        self.play(Create(plane), Create(circle), GrowArrow(e1), GrowArrow(e2), run_time=1.2)
        self.wait(0.5)

        A = np.array([[2.5, 1.2], [0.8, 1.5]])

        # VO cue: ap dung bien doi - khong gian bi bop meo
        self.play(
            plane.animate.apply_matrix(A),
            circle.animate.apply_matrix(A),
            e1.animate.put_start_and_end_on(ORIGIN, plane.c2p(A[0, 0], A[1, 0])),
            e2.animate.put_start_and_end_on(ORIGIN, plane.c2p(A[0, 1], A[1, 1])),
            run_time=2.5,
        )

        question = MathTex("?", color=COLOR_ACCENT).scale(2)
        question.to_edge(RIGHT, buff=1.0)

        caption = vn_text("Hướng nào là trục chính?", size=36, color=COLOR_ACCENT)
        caption.to_edge(DOWN, buff=0.6)
        caption.add_background_rectangle(color=COLOR_BG, opacity=0.7)

        self.play(FadeIn(question, scale=0.5), FadeIn(caption), run_time=0.8)

        # VO cue: cau hoi trung tam - truc chinh la gi?
        self.play(
            question.animate.scale(1.25),
            rate_func=there_and_back, run_time=0.8,
        )
        self.play(Indicate(caption, color=COLOR_ACCENT), run_time=0.9)
        self.play(
            question.animate.scale(1.25),
            rate_func=there_and_back, run_time=0.8,
        )
        self.play(Indicate(caption, color=COLOR_ACCENT), run_time=0.9)
        self.wait(1.5)

        self.end_pause(1)
