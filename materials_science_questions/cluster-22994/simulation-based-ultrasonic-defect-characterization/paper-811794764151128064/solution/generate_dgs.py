import numpy as np
import sys, csv, os

def compute_DGS(probe_type, out_path):
    c = 5920.0  # m/s
    if probe_type == 'square':
        freq = 2.0e6
        width = 18e-3
        height = 18e-3
        nx = 10
        ny = 10
        xs = np.linspace(-width/2, width/2, nx)
        ys = np.linspace(-height/2, height/2, ny)
        dx = width / nx
        dy = height / ny
    elif probe_type == '32element':
        freq = 2.25e6
        pitch = 1.4e-3
        num_elems = 32
        elem_len = 10e-3
        width = num_elems * pitch
        height = elem_len
        xs = np.linspace(-width/2 + pitch/2, width/2 - pitch/2, num_elems)
        ys = np.array([0.0])
        dx = pitch
        dy = elem_len
    elif probe_type == '16element':
        freq = 2.25e6
        pitch = 1.4e-3
        num_elems = 16
        elem_len = 10e-3
        width = num_elems * pitch
        height = elem_len
        xs = np.linspace(-width/2 + pitch/2, width/2 - pitch/2, num_elems)
        ys = np.array([0.0])
        dx = pitch
        dy = elem_len
    else:
        raise ValueError('Unknown probe type')

    probe_area_elem = dx * dy

    distances_mm = np.arange(5, 601, 5)
    diameters_mm = np.arange(0.5, 20.1, 0.5)
    distances = distances_mm * 1e-3
    diameters = diameters_mm * 1e-3

    max_S = 0.0
    results = []

    for z in distances:
        for D in diameters:
            nr = 5
            ntheta = 12
            rho_edges = np.linspace(0, D/2, nr+1)
            rho_centers = (rho_edges[:-1] + rho_edges[1:]) / 2
            drho = np.diff(rho_edges)
            dtheta = 2*np.pi / ntheta

            theta = np.linspace(0, 2*np.pi, ntheta, endpoint=False)
            R, TH = np.meshgrid(rho_centers, theta, indexing='ij')
            x_refl = (R * np.cos(TH)).ravel()
            y_refl = (R * np.sin(TH)).ravel()
            drho_m = np.repeat(drho, ntheta)

            Xp, Yp = np.meshgrid(xs, ys, indexing='ij')
            Xp_f = Xp.ravel()
            Yp_f = Yp.ravel()

            dx_mat = Xp_f[None, :] - x_refl[:, None]
            dy_mat = Yp_f[None, :] - y_refl[:, None]
            dist = np.sqrt(dx_mat**2 + dy_mat**2 + z**2)

            w = (z / dist)**4

            k = 2 * np.pi * freq / c
            phase = -1j * k * dist + 0j
            exp_term = np.exp(phase)
            A = (w * exp_term / dist) * probe_area_elem * drho_m[:, None] * dtheta

            C = np.sum(A, axis=1)
            S = np.abs(np.sum(C**2))

            results.append((z*1e3, D*1e3, S))
            if S > max_S:
                max_S = S

    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['distance_mm', 'diameter_mm', 'signal_dB'])
        for dist_mm, diam_mm, S in results:
            dB = 20 * np.log10(S / max_S) if max_S > 0 else 0.0
            writer.writerow([f"{dist_mm:.1f}", f"{diam_mm:.1f}", f"{dB:.6f}"])
    print(f"Written {out_path}")

if __name__ == '__main__':
    probe_type = sys.argv[1]
    out_path = sys.argv[2]
    compute_DGS(probe_type, out_path)