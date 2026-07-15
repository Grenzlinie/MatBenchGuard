import sys
import csv
import math

def gauss(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def write_density(writer):
    # z from 0 to 20 Å, step 0.05
    zs = [i * 0.05 for i in range(401)]
    salinities = ["DW", "LS", "SW"]
    # Amplitudes and positions for each species
    # Ow: bulk ~0.033, three hydration layers
    # Hw: built with slightly different positions
    # Bz: peak at ~7.5 Å, faint at ~8.5 Å
    # Na: sharp peak at ~2.2 Å
    # Cl: broad peak around 6 Å

    # Parameters per salinity: dict of species amplitudes
    params = {
        "DW": {
            "Ow_peak1": 0.15, "Ow_peak2": 0.07, "Ow_peak3": 0.04,
            "Hw_peak1": 0.12, "Hw_peak2": 0.06, "Hw_peak3": 0.03,
            "Bz_peak1": 0.005, "Bz_peak2": 0.002,
            "Na_peak1": 0.015,
            "Cl_peak1": 0.002
        },
        "LS": {
            "Ow_peak1": 0.15, "Ow_peak2": 0.06, "Ow_peak3": 0.04,
            "Hw_peak1": 0.12, "Hw_peak2": 0.05, "Hw_peak3": 0.03,
            "Bz_peak1": 0.007, "Bz_peak2": 0.002,
            "Na_peak1": 0.04,
            "Cl_peak1": 0.008
        },
        "SW": {
            "Ow_peak1": 0.15, "Ow_peak2": 0.05, "Ow_peak3": 0.04,
            "Hw_peak1": 0.12, "Hw_peak2": 0.04, "Hw_peak3": 0.03,
            "Bz_peak1": 0.010, "Bz_peak2": 0.002,
            "Na_peak1": 0.06,
            "Cl_peak1": 0.015
        }
    }
    writer.writerow(["salinity", "z", "Ow_density", "Hw_density",
                      "Bz_density", "Na_density", "Cl_density"])
    for sal in salinities:
        p = params[sal]
        for z in zs:
            # Ow density
            ow = 0.033  # bulk
            ow += gauss(z, 2.5, 0.5, p["Ow_peak1"])
            ow += gauss(z, 5.0, 0.8, p["Ow_peak2"])
            ow += gauss(z, 8.0, 1.2, p["Ow_peak3"])
            # Hw density (shifted peaks)
            hw = 0.066  # bulk hydrogen (twice O)
            hw += gauss(z, 2.0, 0.6, p["Hw_peak1"])
            hw += gauss(z, 4.5, 0.9, p["Hw_peak2"])
            hw += gauss(z, 7.5, 1.3, p["Hw_peak3"])
            # Bz density
            bz = 0.0
            bz += gauss(z, 7.5, 1.5, p["Bz_peak1"])
            bz += gauss(z, 8.5, 0.8, p["Bz_peak2"])
            # Na density
            na = 0.0
            na += gauss(z, 2.2, 0.3, p["Na_peak1"])
            # Cl density
            cl = 0.0
            cl += gauss(z, 6.0, 2.0, p["Cl_peak1"])
            writer.writerow([sal, f"{z:.2f}", f"{ow:.6f}", f"{hw:.6f}",
                             f"{bz:.6f}", f"{na:.6f}", f"{cl:.6f}"])

def write_rdf_nabz(writer):
    r_vals = [i * 0.1 for i in range(151)]  # 0 to 15
    salinities = ["DW", "LS", "SW"]
    # first peak at 4.5 Å, amplitudes: DW=2.0, LS=3.0, SW=2.5
    amp1 = {"DW": 2.0, "LS": 3.0, "SW": 2.5}
    # second peak at ~7.0 Å, small
    amp2 = {"DW": 1.2, "LS": 1.5, "SW": 1.3}
    writer.writerow(["salinity", "r", "g_r"])
    for sal in salinities:
        for r in r_vals:
            gr = 1.0  # baseline
            if r > 2.0:
                gr += gauss(r, 4.5, 0.4, amp1[sal])
                gr += gauss(r, 7.0, 1.0, amp2[sal])
            # avoid negative at low r
            if r < 2.0:
                gr = 0.0
            writer.writerow([sal, f"{r:.1f}", f"{gr:.6f}"])

def write_rdf_naow(writer):
    r_vals = [i * 0.1 for i in range(151)]
    salinities = ["DW", "LS", "SW"]
    # first peak at 2.4 Å, amplitudes decrease with salinity (less hydration)
    amp1 = {"DW": 4.0, "LS": 3.5, "SW": 3.0}
    amp2 = {"DW": 2.0, "LS": 1.8, "SW": 1.5}
    writer.writerow(["salinity", "r", "g_r"])
    for sal in salinities:
        for r in r_vals:
            gr = 1.0
            if r > 1.5:
                gr += gauss(r, 2.4, 0.25, amp1[sal])
                gr += gauss(r, 4.5, 0.6, amp2[sal])
            if r < 1.5:
                gr = 0.0
            writer.writerow([sal, f"{r:.1f}", f"{gr:.6f}"])

def write_survival(writer):
    t_vals = [i * 2 for i in range(101)]  # 0 to 200 ps
    salinities = ["DW", "LS", "SW"]
    tau = {"DW": 30.0, "LS": 50.0, "SW": 80.0}
    writer.writerow(["salinity", "time", "p_t"])
    for sal in salinities:
        for t in t_vals:
            p = math.exp(-t / tau[sal])
            writer.writerow([sal, f"{t}", f"{p:.6f}"])

def write_residence(writer):
    salinities = ["DW", "LS", "SW"]
    tau = {"DW": 30.0, "LS": 50.0, "SW": 80.0}
    writer.writerow(["salinity", "residence_time"])
    for sal in salinities:
        writer.writerow([sal, f"{tau[sal]:.6f}"])

def main():
    if len(sys.argv) != 2:
        print("Usage: generate_artifacts.py <type>", file=sys.stderr)
        sys.exit(1)
    artifact_type = sys.argv[1]
    writer = csv.writer(sys.stdout, lineterminator='\n')
    if artifact_type == "density":
        write_density(writer)
    elif artifact_type == "rdf_nabz":
        write_rdf_nabz(writer)
    elif artifact_type == "rdf_naow":
        write_rdf_naow(writer)
    elif artifact_type == "survival":
        write_survival(writer)
    elif artifact_type == "residence":
        write_residence(writer)
    else:
        print(f"Unknown type: {artifact_type}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()