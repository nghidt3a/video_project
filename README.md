# SVD Video — Manim v0.18+ modular project

Tái cấu trúc 25 scene gốc (`svd_final.ipynb`) + 3 scene cầu nối thành 28 scene Python độc lập, theo kịch bản 5 chương.

## 1. Yêu cầu hệ thống

| Thành phần | Phiên bản |
|---|---|
| Python | 3.11+ |
| Manim | `manim-community` ≥ 0.18 |
| FFmpeg | 6.x (trong `PATH`) |
| LaTeX | MiKTeX / TeX Live (gồm `amsmath`, `amssymb`, `vntex`) |
| Font | **Noto Sans** (hỗ trợ tiếng Việt — bắt buộc) |

## 2. Cài đặt

```bash
pip install manim numpy
# Windows: cài Noto Sans từ Google Fonts
# LaTeX: miktex.org (chọn "install packages on the fly = Yes")
```

Kiểm tra:
```bash
manim --version          # phải ≥ 0.18
ffmpeg -version
python -c "import manim; print(manim.__version__)"
```

## 3. Render

Mọi lệnh chạy từ thư mục `svd_video_project/`.

### Một scene
```bash
manim -qh scenes/ch1_space_transform/ch1_01_opening.py SVDOpeningHook
```
Chất lượng: `-ql` (480p15), `-qm` (720p30), `-qh` (1080p60), `-qk` (2160p60).

### Orchestrator
```bash
python main.py --list                          # liệt kê 28 scene theo thứ tự
python main.py --scene SVDOpeningHook -q h     # render 1 scene
python main.py --chapter ch3 --quality m       # render cả chương 3
python main.py --all --quality m               # render toàn bộ
python main.py --all --dry                     # test import, không render
```

Output ghi vào `outputs/video/…`.

### Dry-run tất cả (kiểm tra import/class)
```bash
python main.py --all --dry --quality l
```

## 4. Fix font tiếng Việt

Triệu chứng: chữ Việt vỡ dấu / thiếu ký tự.

1. Cài **Noto Sans** (Google Fonts → tải ZIP → cài tất cả ttf).
2. Windows: logout/login để font được load.
3. Mở `config/constants.py`, kiểm tra `VN_FONT = "Noto Sans"`. Nếu muốn đổi font:
   ```python
   VN_FONT = "Segoe UI"   # hoặc Arial, DejaVu Sans
   ```
4. Xoá cache:
   ```bash
   rm -rf outputs/Tex outputs/text outputs/video
   manim --flush_cache
   ```

LaTeX tiếng Việt: nếu dùng `MathTex` chứa dấu tiếng Việt → đổi sang `Text(..., font=VN_FONT)` (dễ nhất). Bảng `MathTex` chỉ dùng cho ký hiệu toán.

## 5. Debug

| Triệu chứng | Nguyên nhân / Cách khắc phục |
|---|---|
| `ShowCreation not defined` | Đã thay bằng `Create` — rebuild cache: `manim --flush_cache` |
| Text 3D biến mất / quay cùng camera | Scene phải kế thừa `BaseThreeDScene`, gọi `self.fix(mobj)` thay vì `add_fixed_in_frame_mobjects` |
| Card bị cắt mép | Gọi `safe_fit(card)` trong `utils.helpers` — đã auto-áp dụng qua `make_card`, dùng cho heatmap/MathTex lớn |
| LaTeX lỗi: `! Package inputenc Error` | Cài `vntex` hoặc đổi ký tự đặc biệt sang `Text(...)` thay `MathTex` |
| `ModuleNotFoundError: config` | Chạy lệnh từ thư mục `svd_video_project/` (PYTHONPATH mặc định = cwd) |
| `fix_in_frame` không có | Manim < 0.18 — nâng cấp: `pip install -U manim` |
| Render chậm bất thường | Bật cache: `disable_caching = False` trong `manim.cfg`; dùng `-ql` khi phát triển |
| Màu U/Σ/V không đồng nhất | Dùng `COLOR_U / COLOR_SIGMA / COLOR_V` từ `config.constants`, không hardcode BLUE/GREEN/ORANGE |

## 6. Thêm scene mới

1. Tạo `scenes/chX_.../chX_NN_name.py`:
   ```python
   from manim import *
   from config.constants import *
   from utils.helpers import *
   from utils.base_scene import BaseScene, BaseThreeDScene

   class MyScene(BaseScene):
       def construct(self):
           ...
           self.end_pause(1)
   ```
2. Thêm tuple `(chapter, stem, class)` vào `SCENE_ORDER` trong `main.py`.
3. Chạy `python main.py --scene MyScene --quality l`.

## 7. Cấu trúc

```
svd_video_project/
├── manim.cfg              # cấu hình render (1080p60, outputs/, bg #0E1117)
├── main.py                # orchestrator CLI (--list/--scene/--chapter/--all/--dry)
├── README.md
├── config/constants.py    # màu, font, ma trận demo
├── utils/helpers.py       # make_card, make_badge, build_transition, tracked_basis, ...
├── utils/base_scene.py    # BaseScene, BaseThreeDScene (self.fix, self.vn, ...)
├── scenes/
│   ├── ch1_space_transform/   # 4 scene — đặt vấn đề
│   ├── ch2_svd_reveal/        # 3 scene — lộ SVD
│   ├── ch3_algebra_proof/     # 13 scene — chứng minh đại số
│   ├── ch4_geometry_compare/  # 8 scene — hình học & so sánh
│   └── ch5_applications/      # 4 scene — ứng dụng & kết
├── assets/                # logo.png, hình pixel cho rank-k (người dùng cung cấp)
└── outputs/               # video/images/tex được Manim ghi ra
```

## 8. Ghi chú thiết kế

- Mọi scene dùng nền tối `#0E1117` (đã set trong `manim.cfg` và `BaseScene`).
- U = **xanh** (BLUE), Σ = **lục** (GREEN), V = **cam** (ORANGE), highlight = **vàng** (YELLOW) — nhất quán toàn video.
- 3D: luôn gọi `self.fix(mobj)` cho nhãn/công thức để chúng không xoay theo camera.
- Chuyển chương: dùng `build_transition(title, subtitle)` — trả về `(VGroup, [anims])`.
- Tracking vector (scene 24→26): `tracked_basis(plane)` trả về e₁, e₂ có updater tự bám theo `plane` khi `apply_matrix`.
