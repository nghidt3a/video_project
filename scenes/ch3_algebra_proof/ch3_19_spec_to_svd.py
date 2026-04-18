from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDSpectralToSVD(BaseScene):
    def construct(self):
        title = self.title_banner("Từ định lý phổ đến SVD")
        self.play(FadeIn(title), run_time=0.5)

        left_group = VGroup(
            MathTex(r"A = PDP^T", font_size=44, color=COLOR_WARN),
            vn_text("Chỉ áp dụng cho ma trận đối xứng", size=24, color=COLOR_WARN),
        ).arrange(DOWN, buff=0.2)
        right_group = VGroup(
            MathTex(r"A = U\Sigma V^T", font_size=44, color=COLOR_SIGMA),
            vn_text("Áp dụng cho mọi ma trận", size=28, color=COLOR_SIGMA),
        ).arrange(DOWN, buff=0.22)
        flow_arrow = Arrow(
            start=LEFT * 0.9,
            end=RIGHT * 0.9,
            buff=0,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.12,
            color=GREY_B,
        )
        flow_group = VGroup(left_group, flow_arrow, right_group).arrange(RIGHT, buff=0.85)
        flow_group.move_to(DOWN * 0.2)

        self.play(Write(left_group[0]), run_time=0.8)
        self.play(FadeIn(left_group[1], shift=UP * 0.1), run_time=0.45)
        self.play(GrowArrow(flow_arrow), run_time=0.6)
        self.play(FadeIn(right_group[0], shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(right_group[1], shift=UP * 0.12), run_time=0.5)
        self.wait(1.4)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
