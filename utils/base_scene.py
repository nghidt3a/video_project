"""BaseScene / BaseThreeDScene with project defaults and shortcuts."""
from __future__ import annotations

from manim import Scene, ThreeDScene, config, UP, DOWN
from config.constants import COLOR_BG, COLOR_ACCENT, COLOR_MUTED
from utils.helpers import vn_text, safe_fit
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


class _Shared:
    """Mixin-like shortcuts used by both 2D and 3D bases."""

    def vn(self, text: str, size: float = 32, **kw):
        return vn_text(text, size=size, **kw)

    def title_banner(self, text: str, color=COLOR_ACCENT):
        t = vn_text(text, size=44, weight="BOLD", color=color)
        t.to_edge(UP, buff=0.5)
        safe_fit(t)
        return t

    def footer_note(self, text: str):
        t = vn_text(text, size=22, color=COLOR_MUTED)
        t.to_edge(DOWN, buff=0.4)
        safe_fit(t)
        return t

    def end_pause(self, t: float = 1.0):
        self.wait(t)


class BaseScene(_Shared, Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _agent_log(
            "H1",
            "utils/base_scene.py:BaseScene.__init__",
            "Initialized BaseScene descendant",
            {
                "className": self.__class__.__name__,
                "hasFixMethod": hasattr(self, "fix"),
                "mro": [c.__name__ for c in self.__class__.__mro__[:4]],
            },
        )
        try:
            self.camera.background_color = COLOR_BG
        except Exception:
            config.background_color = COLOR_BG

    def fix(self, *mobjs):
        # #region agent log
        _agent_log(
            "H5",
            "utils/base_scene.py:BaseScene.fix",
            "Called fix on 2D scene (no-op)",
            {"className": self.__class__.__name__, "count": len(mobjs)},
        )
        # #endregion
        return mobjs[0] if len(mobjs) == 1 else mobjs


class BaseThreeDScene(_Shared, ThreeDScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _agent_log(
            "H2",
            "utils/base_scene.py:BaseThreeDScene.__init__",
            "Initialized BaseThreeDScene descendant",
            {
                "className": self.__class__.__name__,
                "hasFixMethod": hasattr(self, "fix"),
                "mro": [c.__name__ for c in self.__class__.__mro__[:4]],
            },
        )
        try:
            self.camera.background_color = COLOR_BG
        except Exception:
            config.background_color = COLOR_BG

    def fix(self, *mobjs):
        """Prefer mobject.fix_in_frame() (API v0.18+).
        Fallback to add_fixed_in_frame_mobjects for compatibility.
        """
        _agent_log(
            "H3",
            "utils/base_scene.py:BaseThreeDScene.fix",
            "Called fix on 3D scene",
            {"className": self.__class__.__name__, "count": len(mobjs)},
        )
        for m in mobjs:
            if hasattr(m, "fix_in_frame"):
                m.fix_in_frame()
            else:
                self.add_fixed_in_frame_mobjects(m)
        return mobjs[0] if len(mobjs) == 1 else mobjs
