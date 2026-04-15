"""Reusable building blocks for SVD scenes."""
from __future__ import annotations

import numpy as np
import json
import time
from manim import (
    VGroup, RoundedRectangle, Rectangle, Text, MathTex, Arrow, Line, DashedLine,
    Square, Circle, FadeIn, FadeOut, Write, Create, Indicate, AnimationGroup,
    UP, DOWN, LEFT, RIGHT, ORIGIN, config, WHITE, BLACK, interpolate_color,
    color_gradient, rgb_to_color, Flash,
)

from config.constants import (
    COLOR_CARD, COLOR_CARD_BORDER, COLOR_TEXT, COLOR_MUTED, COLOR_ACCENT,
    COLOR_U, COLOR_SIGMA, COLOR_V, VN_FONT, SAFE_MARGIN, DEFAULT_CARD_WIDTH,
)

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


# ---------------------------------------------------------------------------
def vn_text(text: str, size: float = 32, weight: str = "NORMAL",
            color=COLOR_TEXT, **kwargs) -> Text:
    """Shortcut Text with VN font."""
    if "font_size" in kwargs:
        incoming_font_size = kwargs.pop("font_size")
        resolved_size = size if size != 32 else incoming_font_size
        _agent_log(
            "H6",
            "utils/helpers.py:vn_text",
            "vn_text resolved font_size input",
            {
                "textPreview": text[:30],
                "sizeArg": size,
                "font_size_kwarg": incoming_font_size,
                "resolvedSize": resolved_size,
            },
        )
        size = resolved_size
    return Text(text, font=VN_FONT, weight=weight, color=color,
                font_size=size, **kwargs)


# ---------------------------------------------------------------------------
def safe_fit(mobj, max_w: float | None = None, max_h: float | None = None):
    """Auto-scale mobject to stay inside the safe frame."""
    mw = max_w if max_w is not None else (config.frame_width - SAFE_MARGIN)
    mh = max_h if max_h is not None else (config.frame_height - SAFE_MARGIN)
    if mobj.width > mw:
        mobj.scale_to_fit_width(mw)
    if mobj.height > mh:
        mobj.scale_to_fit_height(mh)
    return mobj


# ---------------------------------------------------------------------------
def make_card(title: str, body: str | list[str] = "", *,
              width: float = DEFAULT_CARD_WIDTH, color=COLOR_ACCENT,
              icon: str | None = None) -> VGroup:
    """Rounded card with title + body text(s). Auto-fitted to frame."""
    if isinstance(body, str):
        body_lines = [body] if body else []
    else:
        body_lines = list(body)

    title_txt = vn_text(title, size=28, weight="BOLD", color=color)
    lines = VGroup(*[vn_text(l, size=22, color=COLOR_TEXT) for l in body_lines])
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

    inner = VGroup(title_txt, lines).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    if icon:
        ic = vn_text(icon, size=32)
        inner = VGroup(ic, inner).arrange(RIGHT, buff=0.3, aligned_edge=UP)

    card_w = max(width, inner.width + 0.6)
    card_h = inner.height + 0.6
    box = RoundedRectangle(corner_radius=0.18, width=card_w, height=card_h,
                           stroke_color=COLOR_CARD_BORDER, stroke_width=2,
                           fill_color=COLOR_CARD, fill_opacity=0.95)
    inner.move_to(box.get_center())
    card = VGroup(box, inner)
    safe_fit(card)
    return card


# ---------------------------------------------------------------------------
def make_badge(text: str, color=COLOR_ACCENT) -> VGroup:
    """Small pill badge."""
    label = vn_text(text, size=20, weight="BOLD", color=color)
    pad_w, pad_h = 0.35, 0.18
    pill = RoundedRectangle(
        corner_radius=(label.height + 2 * pad_h) / 2,
        width=label.width + 2 * pad_w,
        height=label.height + 2 * pad_h,
        stroke_color=color, stroke_width=2,
        fill_color=color, fill_opacity=0.12,
    )
    label.move_to(pill.get_center())
    return VGroup(pill, label)


# ---------------------------------------------------------------------------
def build_transition(title: str, subtitle: str | None = None,
                     color=COLOR_ACCENT) -> tuple[VGroup, list]:
    """Create a chapter-transition title block + list of animations to play."""
    bar = Rectangle(width=config.frame_width, height=0.08,
                    fill_color=color, fill_opacity=1, stroke_width=0)
    title_m = vn_text(title, size=72, weight="BOLD", color=color)
    group_children = [title_m]
    if subtitle:
        sub_m = vn_text(subtitle, size=32, color=COLOR_MUTED)
        group_children.append(sub_m)
    txt = VGroup(*group_children).arrange(DOWN, buff=0.35)
    safe_fit(txt)
    group = VGroup(bar.copy().next_to(txt, UP, buff=0.6),
                   txt,
                   bar.copy().next_to(txt, DOWN, buff=0.6))
    anims = [
        FadeIn(group[0], shift=DOWN * 0.2),
        Write(title_m),
    ]
    if subtitle:
        anims.append(FadeIn(group[1][1], shift=UP * 0.1))
    anims.append(FadeIn(group[2], shift=UP * 0.2))
    return group, anims


# ---------------------------------------------------------------------------
def _viridis(t: float):
    stops = ["#440154", "#3B528B", "#21908C", "#5DC863", "#FDE725"]
    if t <= 0:
        return stops[0]
    if t >= 1:
        return stops[-1]
    seg = t * (len(stops) - 1)
    i = int(seg)
    frac = seg - i
    return interpolate_color(rgb_to_color(_hex(stops[i])),
                             rgb_to_color(_hex(stops[i + 1])), frac)


def _hex(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def make_heatmap(data, *, cell_size: float = 0.3, cmap: str = "viridis") -> VGroup:
    """Grid of colored squares from a 2D array."""
    arr = np.asarray(data, dtype=float)
    vmin, vmax = float(arr.min()), float(arr.max())
    span = (vmax - vmin) or 1.0
    rows, cols = arr.shape
    group = VGroup()
    for i in range(rows):
        for j in range(cols):
            t = (arr[i, j] - vmin) / span
            sq = Square(side_length=cell_size,
                        stroke_width=0.5, stroke_color=COLOR_CARD_BORDER,
                        fill_color=_viridis(t), fill_opacity=1)
            sq.move_to(np.array([
                (j - cols / 2 + 0.5) * cell_size,
                (rows / 2 - i - 0.5) * cell_size,
                0,
            ]))
            group.add(sq)
    safe_fit(group)
    return group


# ---------------------------------------------------------------------------
def tracked_basis(plane, colors=(COLOR_U, COLOR_V)):
    """Return a VGroup containing e1, e2 arrows tied to a NumberPlane.

    Arrows are re-computed from plane.get_origin() to plane.c2p(1,0)/(0,1),
    so applying a matrix to the plane will visually move them.
    """
    o = plane.get_origin()
    e1 = Arrow(o, plane.c2p(1, 0), color=colors[0], buff=0,
               stroke_width=6, max_tip_length_to_length_ratio=0.18)
    e2 = Arrow(o, plane.c2p(0, 1), color=colors[1], buff=0,
               stroke_width=6, max_tip_length_to_length_ratio=0.18)

    def _updater(mob):
        o2 = plane.get_origin()
        mob[0].put_start_and_end_on(o2, plane.c2p(1, 0))
        mob[1].put_start_and_end_on(o2, plane.c2p(0, 1))

    group = VGroup(e1, e2)
    group.add_updater(_updater)
    return group


# ---------------------------------------------------------------------------
def color_mathtex_parts(tex: MathTex, parts_colors: dict[int, str]) -> MathTex:
    """Apply per-part colors on a MathTex split by substrings."""
    for idx, col in parts_colors.items():
        try:
            tex[idx].set_color(col)
        except Exception:
            pass
    return tex


# ---------------------------------------------------------------------------
def sigma_badge(i: int) -> VGroup:
    return make_badge(f"σ{i} khớp ✓", color=COLOR_SIGMA)
