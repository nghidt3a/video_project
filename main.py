"""Orchestrator for the SVD video project.

Usage:
    python main.py --list
    python main.py --scene SVDOpeningHook [--quality l|m|h|k]
    python main.py --all [--quality m]
    python main.py --chapter ch1 [--quality m]
    python main.py --all --profile ver2 [--quality m]

It shells out to the Manim CLI so rendering runs exactly like calling
``manim -qm scenes/.../file.py ClassName`` per scene.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# (chapter_dir, file_stem, ClassName)
SCENE_ORDER_CURRENT: list[tuple[str, str, str]] = [
    # Chapter 1 — Space Transform
    ("ch1_space_transform", "ch1_00_trans1",      "SVDChapter01Transition"),
    ("ch1_space_transform", "ch1_03_transform",    "SVDMatrixTransform2D"),
    ("ch1_space_transform", "ch1_04_messy",        "MessyTransformation"),
    ("ch1_space_transform", "ch1_01_opening",      "SVDOpeningHook"),
    ("ch1_space_transform", "ch1_02_overview",     "SVDOverviewScene"),
    # Chapter 2 — SVD Reveal
    ("ch2_svd_reveal",      "ch2_00_trans2",       "SVDChapter02Transition"),
    ("ch2_svd_reveal",      "ch2_05_why",          "SVDWhyQuestion"),
    ("ch1_space_transform", "ch1_04_messy",        "MessyTransformation"),
    ("ch2_svd_reveal",      "ch2_07_reveal",       "SVD_Reveal"),
    # Chapter 3 — Algebra & Proof
    ("ch3_algebra_proof",   "ch3_13_trans1",       "SVDChapter03Transition"),
    ("ch3_algebra_proof",   "ch3_08_numerical",    "SVDNumericalExample"),
    ("ch3_algebra_proof",   "ch3_09_decomp",       "SVDDecompIntro"),
    ("ch3_algebra_proof",   "ch3_10_compute_v",    "SVDComputeStepByStep"),
    ("ch3_algebra_proof",   "ch3_11_compute_u",    "SVDComputeU"),
    ("ch3_algebra_proof",   "ch3_12_assemble",     "SVDResultAssemble"),
    ("ch3_algebra_proof",   "ch3_14_proof_ata",    "SVDProofAtA"),
    ("ch3_algebra_proof",   "ch3_15_proof_aat",    "SVDProofAAt"),
    ("ch3_algebra_proof",   "ch3_16a_rect_intro",  "SVDRectIntro"),
    ("ch3_algebra_proof",   "ch3_16_rect_demo",    "SVDRectangularDemo"),
    ("ch3_algebra_proof",   "ch3_17_ortho",        "SVDOrthogonalityExplained"),
    ("ch3_algebra_proof",   "ch3_17b_diag_intro",  "SVDDiagIntro"),
    ("ch3_algebra_proof",   "ch3_17c_diag_steps",  "SVDDiagSteps"),
    ("ch3_algebra_proof",   "ch3_18_spectral",     "SVDSpectralDecomposition"),
    ("ch3_algebra_proof",   "ch3_19_spec_to_svd",  "SVDSpectralToSVD"),
    ("ch3_algebra_proof",   "ch3_20_summary",      "SVDComponentsSummary"),
    # Chapter 4 — Geometry Compare
    ("ch4_geometry_compare", "ch4_21_trans2",      "SVDChapter04Transition"),
    ("ch4_geometry_compare", "ch4_22_sphere3d",    "SVDSphereTransform3D"),
    ("ch4_geometry_compare", "ch4_23_diag_vs_ortho","SVDDiagonalVsOrthogonal"),
    ("ch4_geometry_compare", "ch4_24_step_vt",     "SVDStep1VTranspose"),
    ("ch4_geometry_compare", "ch4_25_step_sigma",  "SVDStep2Sigma"),
    ("ch4_geometry_compare", "ch4_26_step_u",      "SVDStep3U"),
    ("ch4_geometry_compare", "ch4_27_ellipsoid",   "SVDEllipsoidPrinciple"),
    ("ch4_geometry_compare", "ch4_28_sidebyside_ver2",  "SideBySideCompareVer2"),
    # Chapter 5 — Applications
    ("ch5_applications",    "ch5_29_trans3",       "SVDChapter05Transition"),
    ("ch5_applications",    "ch5_30_rankk",        "SVDRank1Approximation"),
    ("ch5_applications",    "ch5_31_pca",          "SVDPCADeepDive"),
    ("ch5_applications",    "ch5_32_closing",      "SVDClosingSummary"),
]

# Curated order for the complete ver2 narrative.
SCENE_ORDER_VER2: list[tuple[str, str, str]] = [
    # Opening
    ("ch0_intro",         "ch0_00_opening",    "SVDProjectOpening"),
    # Part 1 — Ma trận và sự tác động của ma trận lên không gian
    ("ch1_space_transform", "ch1_00_trans1",      "SVDChapter01Transition"),
    ("ch1_space_transform", "ch1_03_transform",   "SVDMatrixTransform2D"),
    ("ch1_space_transform", "ch1_04_messy",       "MessyTransformation"),
    ("ch1_space_transform", "ch1_01_opening",     "SVDOpeningHook"),
    ("ch1_space_transform", "ch1_02_overview",    "SVDOverviewScene"),
    # Part 2 — Sử dụng SVD, cách phân rã ma trận A qua SVD, áp dụng
    ("ch2_svd_reveal",      "ch2_00_trans2",      "SVDChapter02Transition"),
    ("ch2_svd_reveal",      "ch2_05_why",         "SVDWhyQuestion"),
    ("ch1_space_transform", "ch1_04_messy",       "MessyTransformation"),
    ("ch2_svd_reveal",      "ch2_07_reveal",      "SVD_Reveal"),
    ("ch3_algebra_proof",   "ch3_08_numerical",   "SVDNumericalExample"),
    ("ch3_algebra_proof",   "ch3_09_decomp",      "SVDDecompIntro"),
    ("ch3_algebra_proof",   "ch3_12_assemble",    "SVDResultAssemble"),
    # Part 3 — Chứng minh SVD bằng A.A^T và A^T.A
    ("ch3_algebra_proof",   "ch3_13_trans1",      "SVDChapter03Transition"),
    ("ch3_algebra_proof",   "ch3_10_compute_v",   "SVDComputeStepByStep"),
    ("ch3_algebra_proof",   "ch3_11_compute_u",   "SVDComputeU"),
    ("ch3_algebra_proof",   "ch3_14_proof_ata",   "SVDProofAtA"),
    ("ch3_algebra_proof",   "ch3_15_proof_aat",   "SVDCompareProofATAATA"),
    ("ch3_algebra_proof",   "ch3_17_ortho",       "SVDOrthogonalityExplained"),
    ("ch3_algebra_proof",   "ch3_17b_diag_intro", "SVDDiagIntro"),
    ("ch3_algebra_proof",   "ch3_17c_diag_steps", "SVDDiagSteps"),
    ("ch3_algebra_proof",   "ch3_18_spectral",    "SVDSpectralDecomposition"),
    ("ch3_algebra_proof",   "ch3_19_spec_to_svd", "SVDSpectralToSVD"),
    ("ch3_algebra_proof",   "ch3_20_summary",     "SVDComponentsSummary"),
    # Part 4 — Minh họa trực quan
    ("ch4_geometry_compare", "ch4_21_trans2",      "SVDChapter04Transition"),
    ("ch4_geometry_compare", "ch4_22_sphere3d",    "SVDSphereTransform3D"),
    ("ch4_geometry_compare", "ch4_24_step_vt",     "SVDStep1VTranspose"),
    ("ch4_geometry_compare", "ch4_25_step_sigma",  "SVDStep2Sigma"),
    ("ch4_geometry_compare", "ch4_26_step_u",      "SVDStep3U"),
    ("ch4_geometry_compare", "ch4_27_ellipsoid",   "SVDEllipsoidPrinciple"),
    ("ch4_geometry_compare", "ch4_28_sidebyside_ver2", "SideBySideCompareVer2"),
    # Part 5 — Ứng dụng & Kết luận
    ("ch5_applications",    "ch5_29_trans3",      "SVDChapter05Transition"),
    ("ch5_applications",    "ch5_30_rankk",       "SVDRank1Approximation"),
    ("ch5_applications",    "ch5_31_pca",         "SVDPCADeepDive"),
    ("ch5_applications",    "ch5_32_closing",     "SVDClosingSummary"),
    ("ch5_applications",    "ch5_33_thank_you",   "SVDThankYou"),
]

# Backward compatibility alias for existing integrations.
SCENE_ORDER = SCENE_ORDER_CURRENT

QUALITY_FLAGS = {"l": "-ql", "m": "-qm", "h": "-qh", "k": "-qk"}


def _entries_for(scene: str | None, chapter: str | None, scene_order):
    if scene:
        hits = [e for e in scene_order if e[2] == scene]
        if not hits:
            sys.exit(f"Unknown scene: {scene}")
        return hits
    if chapter:
        hits = [e for e in scene_order if e[0].startswith(chapter)]
        if not hits:
            sys.exit(f"Unknown chapter: {chapter}")
        return hits
    return scene_order


def _scene_order_for(profile: str):
    if profile == "ver2":
        return SCENE_ORDER_VER2
    return SCENE_ORDER_CURRENT


def render(entries, quality: str, dry: bool):
    flag = QUALITY_FLAGS.get(quality, "-qm")
    env = os.environ.copy()
    root_str = str(ROOT)
    env["PYTHONPATH"] = (
        root_str if not env.get("PYTHONPATH") else f"{root_str}{os.pathsep}{env['PYTHONPATH']}"
    )
    for chap, stem, cls in entries:
        rel = f"scenes/{chap}/{stem}.py"
        cmd = ["manim", flag, rel, cls]
        if dry:
            cmd.insert(2, "--dry_run")
        print(">>", " ".join(cmd))
        r = subprocess.run(cmd, cwd=ROOT, env=env)
        if r.returncode != 0:
            sys.exit(f"Manim failed on {cls}")


def main():
    p = argparse.ArgumentParser(description="SVD video orchestrator")
    p.add_argument("--list", action="store_true", help="List all scenes in order")
    p.add_argument("--all", action="store_true", help="Render every scene in order")
    p.add_argument("--scene", help="Render a single scene by class name")
    p.add_argument("--chapter", help="Render every scene of a chapter (e.g. ch1)")
    p.add_argument("--profile", choices=["current", "ver2"], default="ver2",
                   help="Choose scene timeline profile")
    p.add_argument("--quality", choices=list(QUALITY_FLAGS), default="m")
    p.add_argument("--dry", action="store_true", help="Run manim --dry_run only")
    a = p.parse_args()

    scene_order = _scene_order_for(a.profile)

    if a.list:
        for chap, stem, cls in scene_order:
            print(f"{chap:26s} {stem:26s} {cls}")
        return
    if not (a.all or a.scene or a.chapter):
        p.print_help()
        return
    render(_entries_for(a.scene, a.chapter, scene_order), a.quality, a.dry)


if __name__ == "__main__":
    main()
