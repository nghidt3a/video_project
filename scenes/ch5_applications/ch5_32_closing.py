from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene


class SVDClosingSummary(BaseScene):
    def construct(self):
        title = self.title_banner("Ứng dụng thực tiễn")

        icons_data = [
            ("📷", "Ảnh"),
            ("🎬", "Video"),
            ("📊", "PCA"),
            ("🔢", "Số học"),
        ]
        icon_groups = VGroup()
        for emoji, label in icons_data:
            icon = Text(emoji, font=VN_FONT, font_size=72)
            lbl = vn_text(label, font_size=26)
            g = VGroup(icon, lbl).arrange(DOWN, buff=0.2)
            icon_groups.add(g)
        icon_groups.arrange(RIGHT, buff=1.0).move_to(UP * 0.5)
        safe_fit(icon_groups)
        self.fix(icon_groups)

        self.play(Write(title), run_time=0.6)
        self.wait(0.3)
        for g in icon_groups:
            self.play(FadeIn(g, shift=UP * 0.15), run_time=0.6)
            self.wait(0.4)
        self.wait(1.5)

        apps = VGroup(
            VGroup(
                MarkupText("<b>1. Nén ảnh</b>", font=VN_FONT, font_size=28),
                MathTex(r"A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T \approx A", font_size=26),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(
                MarkupText("<b>2. Hệ thống gợi ý</b>", font=VN_FONT, font_size=28),
                vn_text("Netflix, Spotify: SVD của ma trận user-item", font_size=22),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(
                MarkupText("<b>3. Giả nghịch đảo</b>", font=VN_FONT, font_size=28),
                MathTex(r"A^+ = V \Sigma^+ U^T", font_size=26),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(
                MarkupText("<b>4. PCA</b>", font=VN_FONT, font_size=28),
                vn_text("SVD của ma trận dữ liệu đã trừ mean", font_size=22),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 0.8)
        safe_fit(apps)
        self.fix(apps)

        self.play(FadeOut(icon_groups), run_time=0.5)
        for app in apps:
            self.play(FadeIn(app, shift=RIGHT * 0.15), run_time=0.7)
            self.wait(2)

        self.play(FadeOut(apps), FadeOut(title), run_time=0.7)

        tex = MathTex("A = U", "\\Sigma", "V^T", font_size=72)
        color_mathtex_parts(tex, {1: COLOR_U, 2: COLOR_SIGMA, 3: COLOR_V})
        tex.scale(1.8).move_to(ORIGIN)
        safe_fit(tex)
        self.fix(tex)

        tex.set_opacity(0)
        self.add(tex)
        self.play(tex.animate.set_opacity(1), run_time=1.5)
        self.play(Flash(tex, color=COLOR_ACCENT, flash_radius=2.0), run_time=1)
        self.wait(2.5)
        self.play(FadeOut(tex), run_time=1.5)
        self.end_pause(1)
