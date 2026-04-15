from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDOrthogonalityExplained(BaseScene):
    def construct(self):
        title = self.title_banner("Vì sao U và V trực giao?")
        self.play(FadeIn(title), run_time=0.5)

        demo_axes = Axes(
            x_range=[-0.5, 2.2, 1], y_range=[-0.5, 2.2, 1],
            x_length=2.5, y_length=2.5,
            axis_config={"tip_length": 0.12, "stroke_width": 1.5},
        ).scale(0.65).to_corner(UR, buff=0.6)
        origin = demo_axes.c2p(0, 0)
        v1 = Arrow(origin, demo_axes.c2p(1.5, 0), color=COLOR_U, buff=0, stroke_width=3)
        v2 = Arrow(origin, demo_axes.c2p(0, 1.5), color=COLOR_V, buff=0, stroke_width=3)
        dot_eq = MathTex(r"v_1 \cdot v_2 = 0", font_size=20, color=COLOR_ACCENT).next_to(demo_axes, DOWN, buff=0.15)

        self.play(Create(demo_axes), run_time=0.5)
        self.play(GrowArrow(v1), GrowArrow(v2), run_time=0.7)
        self.play(Write(dot_eq), run_time=0.5)

        cards = VGroup(
            make_card("1) AᵀA, AAᵀ", ["đối xứng thực"], width=3.0, color=COLOR_U),
            make_card("2) Định lý phổ", ["chéo hóa trực giao"], width=3.0, color=COLOR_SIGMA),
            make_card("3) λ khác nhau", ["vector riêng vuông góc"], width=3.0, color=COLOR_V),
            make_card("4) Hệ quả", ["VᵀV=I", "UᵀU=I"], width=3.0, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 0.5)
        safe_fit(cards, max_w=config.frame_width - 0.5)

        arrows = VGroup(*[
            Arrow(cards[i].get_right(), cards[i + 1].get_left(), buff=0.06, stroke_width=2, color=WHITE)
            for i in range(3)
        ])

        self.play(FadeIn(cards[0], shift=UP * 0.15), run_time=0.7)
        for i in range(3):
            self.play(GrowArrow(arrows[i]), run_time=0.35)
            self.play(FadeIn(cards[i + 1], shift=UP * 0.15), run_time=0.7)

        self.play(Indicate(cards[3], scale_factor=1.05, color=COLOR_ACCENT), run_time=1.0)
        note = vn_text("Trực giao = hệ quả tất yếu", size=24, color=COLOR_MUTED).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
