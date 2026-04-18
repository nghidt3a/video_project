from manim import *
from config.constants import *
from utils.helpers import *
from utils.base_scene import BaseScene, BaseThreeDScene
import numpy as np
import json
import time

_DEBUG_LOG_PATH = r"d:\Documents\HCMUS-LAB\Final_Manim_SVD\debug-9282c1.log"


def _agent_log(hypothesis_id: str, location: str, message: str, data: dict):
    # #region agent log
    with open(_DEBUG_LOG_PATH, "a", encoding="utf-8") as _f:
        _f.write(
            json.dumps(
                {
                    "sessionId": "9282c1",
                    "runId": "initial",
                    "hypothesisId": hypothesis_id,
                    "location": location,
                    "message": message,
                    "data": data,
                    "timestamp": int(time.time() * 1000),
                },
                ensure_ascii=False,
            )
            + "\n"
        )
    # #endregion


class SVDRank1Approximation(BaseScene):
    def construct(self):
        _agent_log(
            "H4",
            "scenes/ch5_applications/ch5_30_rankk.py:SVDRank1Approximation.construct",
            "Before first self.fix call",
            {
                "className": self.__class__.__name__,
                "hasFixMethod": hasattr(self, "fix"),
                "baseClass": BaseScene.__name__,
            },
        )
        title = self.title_banner("Xấp xỉ rank-k")
        formula = MathTex(
            r"A_k = \sum_{i=1}^{k} \sigma_i\, u_i v_i^T",
            font_size=32, color=COLOR_SIGMA,
        ).next_to(title, DOWN, buff=0.1).shift(UP * 1.2)
        self.fix(formula)

        self.play(FadeIn(formula), run_time=0.6)

        try:
            img = ImageMobject("assets/logo.png")
            img.set(height=3.2)
            arr = np.array(img.pixel_array, dtype=float)
            if arr.ndim == 3:
                arr = arr[..., :3].mean(axis=2)
            A = arr / max(arr.max(), 1.0)
        except Exception:
            A = np.random.rand(16, 16)

        U, S, Vt = np.linalg.svd(A, full_matrices=False)
        r = len(S)
        total_energy = float(np.sum(S ** 2))

        def approx(k):
            return np.clip(U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :], 0, 1)

        def arr_to_image(arr, height=2.75):
            gray = (np.clip(arr, 0, 1) * 255).astype(np.uint8)
            rgb = np.stack([gray] * 3, axis=-1)
            mob = ImageMobject(rgb)
            mob.set(height=height)
            return mob

        orig_label = vn_text("Ảnh gốc", font_size=26)
        approx_label = vn_text("Rank-k", font_size=26)

        orig_mob = arr_to_image(A).move_to(LEFT * 3.2 + DOWN * 0.05)
        cur_mob  = arr_to_image(A).move_to(RIGHT * 3.2 + DOWN * 0.05)

        orig_label.next_to(orig_mob, UP, buff=0.2)
        approx_label.next_to(cur_mob, UP, buff=0.2)

        self.play(FadeIn(orig_mob), FadeIn(orig_label),
                  FadeIn(cur_mob), FadeIn(approx_label), run_time=1.2)
        self.wait(0.8)

        bar_w = 8.0
        bar_h = 0.3
        track = Rectangle(width=bar_w, height=bar_h, stroke_color=COLOR_MUTED,
                          stroke_width=2, fill_opacity=0).to_edge(DOWN, buff=0.35)
        fill = Rectangle(width=0.01, height=bar_h, stroke_width=0,
                         fill_color=COLOR_ACCENT, fill_opacity=1.0)
        fill.align_to(track, LEFT).align_to(track, DOWN)
        self.fix(track, fill)
        self.play(Create(track), run_time=0.4)

        pct_label = vn_text("Năng lượng: 0%", font_size=24).next_to(track, UP, buff=0.1)
        self.fix(pct_label)
        self.play(FadeIn(pct_label), run_time=0.3)

        steps = list(range(1, r + 1))
        if len(steps) > 12:
            steps = sorted(set(list(range(1, 6)) + list(np.linspace(6, r, 8, dtype=int))))

        for k in steps:
            Ak = approx(k)
            pct = float(np.sum(S[:k] ** 2) / total_energy)

            new_mob = arr_to_image(Ak).move_to(cur_mob.get_center())

            new_fill = Rectangle(
                width=max(bar_w * pct, 0.01), height=bar_h,
                stroke_width=0, fill_color=COLOR_ACCENT, fill_opacity=1.0,
            )
            new_fill.align_to(track, LEFT).align_to(track, DOWN)
            self.fix(new_fill)

            new_pct = vn_text(f"Năng lượng: k={k}  {pct:.0%}", font_size=24).move_to(pct_label.get_center())
            self.fix(new_pct)

            self.play(
                FadeOut(cur_mob), FadeIn(new_mob),
                Transform(fill, new_fill),
                Transform(pct_label, new_pct),
                run_time=0.7,
            )
            cur_mob = new_mob
            self.wait(0.3)

        self.wait(1.5)
        self.play(
            FadeOut(formula), FadeOut(orig_mob), FadeOut(orig_label),
            FadeOut(cur_mob), FadeOut(approx_label),
            FadeOut(track), FadeOut(fill), FadeOut(pct_label),
            run_time=0.8,
        )
        self.end_pause(1)
