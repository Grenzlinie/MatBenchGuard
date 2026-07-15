import sys

# high‑symmetry path Γ–M–K–Γ–A–L–H–A; define break indices
labels = ['Γ', 'M', 'K', 'Γ', 'A', 'L', 'H', 'A']
break_inds = [0, 20, 40, 60, 70, 80, 90, 100]
N = break_inds[-1]  # 100 k‑points

# band energies at break points for a few bands (band_index 1..5)
# energies in eV relative to Fermi level
bands_data = {
    1: [ -0.2, -0.5, -0.2, -0.2, -0.1, -0.3, -0.4, -0.1 ],  # all negative, no crossing
    2: [ +0.1, -0.05,+0.2, +0.1, +0.15,+0.05,+0.08,+0.15], # electron pocket around M (band 2 goes slightly negative)
    3: [ -0.1, -0.2, -0.0,+0.05,-0.05,-0.15,-0.2, -0.05], # hole pocket around second Γ (positive at Γ)
    4: [ +0.3, +0.25,+0.4, +0.3, +0.35,+0.3, +0.28,+0.35],
    5: [ -0.4, -0.6, -0.3, -0.4, -0.35,-0.5,-0.55,-0.35],
}

def interpolate_linear(x, xs, ys):
    # x is kpoint index, xs break indices, ys values
    i = 0
    while i < len(xs)-1 and x > xs[i+1]:
        i += 1
    if i == len(xs)-1:
        return ys[-1]
    x0, x1 = xs[i], xs[i+1]
    y0, y1 = ys[i], ys[i+1]
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

for ik in range(N):
    for band_idx in sorted(bands_data.keys()):
        energy = interpolate_linear(ik, break_inds, bands_data[band_idx])
        print(ik, band_idx, f"{energy:.6f}")
