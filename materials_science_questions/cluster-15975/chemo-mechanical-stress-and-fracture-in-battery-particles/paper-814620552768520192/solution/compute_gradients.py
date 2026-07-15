#!/usr/bin/env python3
import math
import os

# Constants
D_S = 3.9e-14       # m^2/s
GAMMA = 7.5
C_MAX = 30555.0      # mol/m^3
SOC_INIT = 0.9
DELTA_SOC = 0.8      # full discharge depth
FARADAY = 96485.0
A_HT_CELL = 2.7      # Ah, assumed total cell throughput

PARTICLE_RADII_UM = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0]
C_RATES = [1, 2, 3, 4, 5, 6, 8, 10]

def rom_A_max(rs_um, crate):
    return -0.5902 + (0.7173 + 0.0027*rs_um + (-0.15/rs_um)) / (1.0 + abs(0.0223*crate - (0.2115 + (-0.002)*rs_um)))

def rom_m_rate(rs_um, crate):
    termC = 1.0 + (-0.2058)*crate + 22.5694/crate + (-21.7787)/(crate*crate)
    termR = 1.0 + (-7.6826)/rs_um + 19.8345/(rs_um*rs_um) + (-0.0544)*rs_um
    return 1.9572 + termC * termR

def simulate_gradient(rs, crate):
    rs_um = rs * 1e6
    # compute ROM parameters
    Amax = rom_A_max(rs_um, crate)
    mrate = rom_m_rate(rs_um, crate)
    # f_bb at end of full discharge
    f_bb = min(Amax * (1.0 - math.exp(-mrate * A_HT_CELL)), Amax)  # stay <= Amax
    if f_bb >= 0.999:
        f_bb = 0.999
    D_eff = D_S * (1.0 - f_bb)**GAMMA

    # flux density
    delta_c_avg = DELTA_SOC * C_MAX
    t_total = 3600.0 / crate
    j_s = (rs * delta_c_avg * crate) / (3.0 * 3600.0)   # mol/m²/s

    # spatial discretisation
    N = 50
    dr = rs / (N - 1)
    r = [i * dr for i in range(N)]
    c = [SOC_INIT * C_MAX] * N

    # time step
    dt_stable = 0.1 * dr*dr / (2.0 * D_eff)
    dt = min(dt_stable, t_total / 1000.0)
    n_steps = int(t_total / dt)
    if n_steps < 1:
        dt = t_total
        n_steps = 1

    # explicit Euler
    for _ in range(n_steps):
        new_c = c[:]
        # interior
        for i in range(1, N-1):
            ri = r[i]
            dcdr = (c[i+1] - c[i-1]) / (2.0 * dr)
            d2cdr2 = (c[i+1] - 2.0*c[i] + c[i-1]) / (dr*dr)
            new_c[i] = c[i] + dt * D_eff * (d2cdr2 + (2.0/ri) * dcdr)
        # r=0 symmetry
        new_c[0] = c[0] + dt * D_eff * 6.0 * (c[1] - c[0]) / (dr*dr)
        # surface boundary condition
        new_c[N-1] = c[N-1] - dt * D_eff * ( (c[N-1] - c[N-2])/dr ) + dt * D_eff * ( -j_s/D_eff )  # integrate flux
        # Actually better: enforce gradient: new_c[N-1] = c[N-2] - (j_s * dr / D_eff)
        c = new_c
        # enforce surface condition after each step
        c[N-1] = c[N-2] - (j_s * dr / D_eff)

    # gradient = c_center - c_surface
    grad = c[0] - c[N-1]
    return grad

def main():
    outdir = "/app/outputs"
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "concentration_gradients.csv")
    with open(outpath, "w") as f:
        f.write("particle_radius_um,C_rate,surface_concentration_gradient_mol_m3\n")
        for rs_um in PARTICLE_RADII_UM:
            rs = rs_um * 1e-6
            for crate in C_RATES:
                grad = simulate_gradient(rs, crate)
                f.write(f"{rs_um},{crate},{grad:.3f}\n")

if __name__ == "__main__":
    main()