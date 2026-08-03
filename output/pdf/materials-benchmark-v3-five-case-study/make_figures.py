#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parent / "figs"
OUT.mkdir(parents=True, exist_ok=True)
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD_PATH if bold else FONT_PATH, size)


def canvas(title):
    image = Image.new("RGB", (1800, 850), "white")
    draw = ImageDraw.Draw(image)
    draw.text((900, 55), title, font=font(38, True), fill="#0f172a", anchor="mm")
    return image, draw


def box(draw, rect, text, fill, size=27):
    draw.rounded_rectangle(rect, radius=22, fill=fill, outline="#475569", width=3)
    x = (rect[0] + rect[2]) // 2
    y = (rect[1] + rect[3]) // 2
    draw.multiline_text((x, y), text, font=font(size, True), fill="#0f172a", anchor="mm", align="center", spacing=7)


def arrow(draw, start, end, color="#64748b"):
    draw.line((start, end), fill=color, width=7)
    x, y = end
    draw.polygon([(x, y), (x - 22, y - 13), (x - 22, y + 13)], fill=color)


# Figure 1
image, draw = canvas("v3.3 baseline-first Review / Repair lifecycle")
xs = [40, 390, 740, 1090, 1440]
labels = ["Source\npackage", "Review\nQ/A correctness", "Stage A\nBaseline", "Independent\nReview", "Optional Stage B\nEnhancement"]
colors = ["#e2e8f0", "#dbeafe", "#dcfce7", "#fef3c7", "#ede9fe"]
for x, label, color in zip(xs, labels, colors): box(draw, (x, 240, x + 300, 390), label, color, 25)
for x in xs[:-1]: arrow(draw, (x + 300, 315), (x + 345, 315))
box(draw, (710, 545, 1050, 675), "Publish\nBASELINE_CORRECT", "#bbf7d0", 24)
box(draw, (1400, 545, 1740, 675), "Publish best\nor fall back", "#ddd6fe", 24)
draw.line((1240, 390, 880, 545), fill="#16a34a", width=6)
draw.line((1590, 390, 1570, 545), fill="#7c3aed", width=6)
draw.text((900, 780), "Correctness first: an enhancement failure never invalidates the reviewed Baseline.", font=font(28, True), fill="#166534", anchor="mm")
image.save(OUT / "fig1_five_routes.png")


# Figure 2
image, draw = canvas("One-way authority and package visibility")
xs = [60, 500, 940, 1380]
labels = ["paper/paper.md\nreview evidence only", "instruction.md\nonly solver-visible task", "steps / manifest\nderived mirrors", "tests\nGold + tolerance"]
colors = ["#e0f2fe", "#dcfce7", "#fef3c7", "#ede9fe"]
for x, label, color in zip(xs, labels, colors): box(draw, (x, 260, x + 360, 430), label, color, 25)
for x in xs[:-1]: arrow(draw, (x + 360, 345), (x + 430, 345))
draw.text((520, 620), "No 'read the paper / figure' instruction", font=font(29, True), fill="#166534", anchor="mm")
draw.text((1320, 620), "Tests cannot secretly fix solver-searchable choices", font=font(27, True), fill="#7c3aed", anchor="mm")
image.save(OUT / "fig2_ssh_condition_groups.png")


# Figure 3
image, draw = canvas("Ferronematic: correctness before optional result enhancement")
box(draw, (70, 210, 520, 620), "SOURCE\n\nMissing free energy\nLoose group handling\nUnsupported tolerance", "#fee2e2", 25)
box(draw, (675, 210, 1125, 620), "STAGE A\nBASELINE\n\nRestore Eqs. 13, 21--24\nAll groups + paper Gold\nGold-only PASS", "#dcfce7", 24)
box(draw, (1280, 210, 1730, 620), "STAGE B\nENHANCED\n\nKeep Baseline unchanged\nAdd eta/S residual\nGold 60% + result 40%", "#ede9fe", 24)
arrow(draw, (520, 415), (655, 415)); arrow(draw, (1125, 415), (1260, 415))
draw.text((900, 750), "Quadrature, initial guesses, scan resolution and solver remain SOLVER_SEARCHABLE.", font=font(27, True), fill="#166534", anchor="mm")
image.save(OUT / "fig3_ferronematic_before_after.png")


# Figure 4
image, draw = canvas("Lightweight checker evidence")
draw.text((450, 150), "Full-scale wall time (seconds)", font=font(29, True), fill="#0f172a", anchor="mm")
wall_labels = ["Ferro B", "Ferro E", "SSH B", "SSH E"]
wall_values = [0.139, 0.182, 0.052, 0.052]
for i, (label, value) in enumerate(zip(wall_labels, wall_values)):
    x = 100 + i * 180
    height = int(value / 0.16 * 360)
    draw.rectangle((x, 600 - height, x + 110, 600), fill="#86efac" if label.endswith("B") else "#c4b5fd")
    draw.text((x + 55, 630), label, font=font(20, True), fill="#0f172a", anchor="mm")
    draw.text((x + 55, 575 - height), f"{value:.3f}", font=font(20), fill="#0f172a", anchor="mm")
draw.text((1320, 150), "SSH Enhanced rewards", font=font(29, True), fill="#0f172a", anchor="mm")
reward_labels = ["valid", "gradient", "wrong", "cross"]
reward_values = [0.925, 0.785, 0.147, 0.224]
for i, (label, value) in enumerate(zip(reward_labels, reward_values)):
    x = 960 + i * 190
    height = int(value * 390)
    draw.rectangle((x, 600 - height, x + 115, 600), fill=["#16a34a", "#60a5fa", "#dc2626", "#f97316"][i])
    draw.text((x + 58, 630), label, font=font(20, True), fill="#0f172a", anchor="mm")
    draw.text((x + 58, 575 - height), f"{value:.3f}", font=font(20), fill="#0f172a", anchor="mm")
draw.line((930, 600 - int(0.6 * 390), 1730, 600 - int(0.6 * 390)), fill="#111827", width=4)
draw.text((1690, 600 - int(0.6 * 390) - 20), "0.6 threshold", font=font(18), fill="#111827", anchor="rm")
image.save(OUT / "fig4_kmc_hacking.png")


# Figure 5
image, draw = canvas("Three independent decisions in v3.3")
box(draw, (80, 220, 550, 410), "CORRECTNESS\nquestion + Gold + tolerance", "#dbeafe", 25)
box(draw, (665, 220, 1135, 410), "QUALITY TIER\nBaseline or Enhanced", "#dcfce7", 25)
box(draw, (1250, 220, 1720, 410), "OPERATIONAL GATE\n<=600 s; no full trajectory", "#fef3c7", 24)
box(draw, (180, 540, 770, 680), "Scientific PASS survives\nan enhancement failure", "#bbf7d0", 25)
box(draw, (1030, 540, 1620, 680), "Cost FAIL blocks publication,\nnot scientific correctness", "#fed7aa", 25)
draw.text((900, 780), "Auditable paper fidelity -- not proof that the paper itself is true.", font=font(29, True), fill="#7c2d12", anchor="mm")
image.save(OUT / "fig5_assurance_boundary.png")
