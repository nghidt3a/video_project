from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseThreeDScene
import numpy as np


class SVDSpectralDecomposition(BaseThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES)

        A_mat = np.array([[2, 1, 0], [1, 3, 0], [0, 0, 2]])
        eigenvalues, eigenvectors = np.linalg.eigh(A_mat)
        axis_lengths = np.abs(eigenvalues)

        colors = [COLOR_U, COLOR_SIGMA, COLOR_V]
        base_vec_len = 1.2

        align_angle = float(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
        cos_a = np.cos(-align_angle)
        sin_a = np.sin(-align_angle)
        rot_z_neg = np.array(
            [[cos_a, -sin_a, 0], [sin_a, cos_a, 0], [0, 0, 1]],
            dtype=float,
        )

        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-2, 2],
            axis_config={"stroke_width": 1, "color": GRAY},
        )

        title = VGroup(
            MathTex(r"A = P D P^T", font_size=38, color=COLOR_ACCENT),
            vn_text("Định lý phổ cho ma trận đối xứng", size=22, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.08)
        eig_vals_text = VGroup(
            MathTex(rf"\lambda_1 \approx {eigenvalues[0]:.2f}", font_size=22, color=colors[0]),
            MathTex(rf"\lambda_2 \approx {eigenvalues[1]:.2f}", font_size=22, color=colors[1]),
            MathTex(rf"\lambda_3 \approx {eigenvalues[2]:.2f}", font_size=22, color=colors[2]),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        self.fix(title, eig_vals_text)
        title.to_corner(UL, buff=0.35)
        eig_vals_text.next_to(title, DOWN, aligned_edge=LEFT, buff=0.22)

        sphere = Sphere(radius=1.0, resolution=(20, 20))
        sphere.set_fill(color=COLOR_CARD, opacity=0.22)
        sphere.set_stroke(color=WHITE, width=0.8, opacity=0.7)

        arrow_group = VGroup()
        for i in range(3):
            direction = eigenvectors[:, i] / np.linalg.norm(eigenvectors[:, i])
            arrow_group.add(Arrow3D(ORIGIN, direction * base_vec_len, color=colors[i]))

        step1 = VGroup(
            vn_text("1)", size=22, color=COLOR_V),
            MathTex(r"P^T", font_size=30, color=COLOR_V),
            vn_text(": Quay vào eigenbasis", size=22, color=COLOR_V),
        ).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        step2 = VGroup(
            vn_text("2)", size=20, color=COLOR_SIGMA),
            MathTex(r"D", font_size=28, color=COLOR_SIGMA),
            vn_text(": Kéo giãn theo eigenvalues", size=20, color=COLOR_SIGMA),
        ).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        step3 = VGroup(
            vn_text("3)", size=22, color=COLOR_U),
            MathTex(r"P", font_size=30, color=COLOR_U),
            vn_text(": Quay về hệ trục ban đầu", size=22, color=COLOR_U),
        ).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        note = vn_text("Bước 2 là bước duy nhất đổi hình", size=22, color=COLOR_ACCENT)
        self.fix(step1, step2, step3)
        self.fix(note)
        for s in [step1, step2, step3]:
            s.to_corner(DL, buff=0.5)
            s.set_opacity(0)
        note.to_corner(DR, buff=0.45)
        note.set_opacity(0)

        self.add(axes)
        self.play(FadeIn(title), FadeIn(eig_vals_text), run_time=0.6)
        self.play(
            Create(sphere),
            LaggedStart(*[Create(vec) for vec in arrow_group], lag_ratio=0.2),
            run_time=1.4,
        )
        self.wait(0.4)

        world = VGroup(sphere, arrow_group)
        self.play(step1.animate.set_opacity(1), run_time=0.4)
        self.play(Rotate(world, angle=-align_angle, axis=OUT, about_point=ORIGIN), run_time=2.0)

        ellipsoid = Surface(
            lambda u, v: np.array([
                axis_lengths[0] * np.cos(u) * np.sin(v),
                axis_lengths[1] * np.sin(u) * np.sin(v),
                axis_lengths[2] * np.cos(v),
            ]),
            u_range=[0, TAU], v_range=[0, PI],
            resolution=(20, 20), fill_opacity=0.22, stroke_width=0.8,
        )
        ellipsoid.set_fill(color=COLOR_SIGMA, opacity=0.22)
        ellipsoid.set_stroke(color=WHITE, width=0.8, opacity=0.7)

        scaled_arrows = VGroup()
        for i in range(3):
            aligned_dir = rot_z_neg @ eigenvectors[:, i]
            aligned_dir = aligned_dir / np.linalg.norm(aligned_dir)
            scaled_arrows.add(Arrow3D(ORIGIN, aligned_dir * axis_lengths[i], color=colors[i]))

        self.play(step1.animate.set_opacity(0), step2.animate.set_opacity(1), run_time=0.4)
        self.play(
            ReplacementTransform(sphere, ellipsoid),
            Transform(arrow_group, scaled_arrows),
            run_time=2.4,
        )
        self.play(note.animate.set_opacity(1), run_time=0.4)
        self.wait(0.8)

        self.play(step2.animate.set_opacity(0), step3.animate.set_opacity(1), note.animate.set_opacity(0), run_time=0.4)
        transformed_world = VGroup(ellipsoid, arrow_group)
        self.play(Rotate(transformed_world, angle=align_angle, axis=OUT, about_point=ORIGIN), run_time=2.0)

        insight = VGroup(
            vn_text("Trên eigenvector: đổi độ dài theo |λᵢ|, giữ nguyên phương", size=24, color=COLOR_ACCENT),
            MathTex(r"A v_i = \lambda_i v_i", font_size=34),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.fix(insight)

        self.play(FadeOut(step3), FadeOut(transformed_world), FadeOut(axes), run_time=0.6)
        self.play(FadeIn(insight), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.end_pause(1)
