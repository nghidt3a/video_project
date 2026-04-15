"""Project-wide constants: palette, fonts, Tex template, demo matrices."""
from manim import BLUE, GREEN, ORANGE, YELLOW, WHITE, GREY_B, RED, TexTemplate

# --- Palette -----------------------------------------------------------------
COLOR_U = BLUE
COLOR_SIGMA = GREEN
COLOR_V = ORANGE
COLOR_ACCENT = YELLOW
COLOR_WARN = RED

COLOR_BG = "#0E1117"
COLOR_CARD = "#1A1D23"
COLOR_CARD_BORDER = "#2E333B"
COLOR_TEXT = WHITE
COLOR_MUTED = GREY_B

# --- Typography --------------------------------------------------------------
VN_FONT = "Times New Roman"
VN_FONT_FALLBACKS = ["Arial", "DejaVu Sans", "Segoe UI"]

# --- LaTeX (Vietnamese capable) ---------------------------------------------
VN_TEX_TEMPLATE = TexTemplate()
VN_TEX_TEMPLATE.add_to_preamble(r"\usepackage[utf8]{inputenc}")
VN_TEX_TEMPLATE.add_to_preamble(r"\usepackage{amsmath,amssymb,amsfonts}")

# --- Demo matrices -----------------------------------------------------------
A_DEMO = [[2.5, 1.2], [0.8, 1.5]]
A_NUM = [[3, 1], [1, 3]]
A_RECT = [[1, 0, 1], [0, 1, 1]]

# --- Layout ------------------------------------------------------------------
SAFE_MARGIN = 1.0  # keep content within frame_width - SAFE_MARGIN
DEFAULT_CARD_WIDTH = 5.0
