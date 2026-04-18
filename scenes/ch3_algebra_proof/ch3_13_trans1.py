from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene


class SVDChapter03Transition(BaseScene):
    def construct(self):
        group, anims = build_transition(
            "Chương 3",
            color=COLOR_U,
        )
        # Re-layout transition so both title and subtitle sit cleanly between two bars.
        title_m = group[1][0]
        group[0].shift(UP * 0.35)
        group[2].shift(DOWN * 0.95)
        title_m.shift(UP * 0.22)

        subtitle = VGroup(
            vn_text("Chứng minh SVD bằng", size=32, color=COLOR_MUTED),
            MathTex(r"AA^{\mathsf T}", font_size=38, color=COLOR_MUTED),
            vn_text("và", size=32, color=COLOR_MUTED),
            MathTex(r"A^{\mathsf T}A", font_size=38, color=COLOR_MUTED),
        ).arrange(RIGHT, buff=0.2)
        safe_fit(subtitle, max_w=config.frame_width - 1.0)
        subtitle.set_x(0)
        subtitle.set_y((title_m.get_bottom()[1] + group[2].get_top()[1]) / 2)
        group.add(subtitle)

        self.play(*anims)
        self.play(FadeIn(subtitle, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(group))
        self.end_pause(1)
