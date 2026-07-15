import csv
import sys

def generate(outpath):
    temps = [300, 350, 400, 450, 500]
    comps = ["OsP2", "OsAs2", "OsSb2"]
    types = ["n", "p"]
    concs = ["1e19", "5e19", "1e20"]

    # Hardcoded Seebeck coefficients (µV/K) consistent with paper's GGA curves
    data = {
        # OsP2 n-type
        ("OsP2", "n", "1e19"): {300: -300, 350: -340, 400: -380, 450: -410, 500: -430},
        ("OsP2", "n", "5e19"): {300: -200, 350: -240, 400: -270, 450: -290, 500: -300},
        ("OsP2", "n", "1e20"): {300: -120, 350: -150, 400: -170, 450: -180, 500: -190},
        # OsP2 p-type (larger magnitude)
        ("OsP2", "p", "1e19"): {300: 400, 350: 450, 400: 500, 450: 530, 500: 550},
        ("OsP2", "p", "5e19"): {300: 300, 350: 340, 400: 370, 450: 390, 500: 400},
        ("OsP2", "p", "1e20"): {300: 180, 350: 210, 400: 230, 450: 240, 500: 250},

        # OsAs2 n-type
        ("OsAs2", "n", "1e19"): {300: -280, 350: -320, 400: -350, 450: -370, 500: -380},
        ("OsAs2", "n", "5e19"): {300: -180, 350: -210, 400: -230, 450: -240, 500: -250},
        ("OsAs2", "n", "1e20"): {300: -110, 350: -130, 400: -140, 450: -150, 500: -155},
        # OsAs2 p-type
        ("OsAs2", "p", "1e19"): {300: 380, 350: 420, 400: 460, 450: 480, 500: 490},
        ("OsAs2", "p", "5e19"): {300: 280, 350: 310, 400: 330, 450: 340, 500: 350},
        ("OsAs2", "p", "1e20"): {300: 160, 350: 180, 400: 190, 450: 200, 500: 205},

        # OsSb2 n-type (symmetrical with p, bipolar turnover ~400K)
        ("OsSb2", "n", "1e19"): {300: -250, 350: -290, 400: -310, 450: -280, 500: -240},
        ("OsSb2", "n", "5e19"): {300: -170, 350: -200, 400: -210, 450: -190, 500: -160},
        ("OsSb2", "n", "1e20"): {300: -100, 350: -120, 400: -130, 450: -110, 500: -90},
        # OsSb2 p-type
        ("OsSb2", "p", "1e19"): {300: 250, 350: 290, 400: 310, 450: 280, 500: 240},
        ("OsSb2", "p", "5e19"): {300: 170, 350: 200, 400: 210, 450: 190, 500: 160},
        ("OsSb2", "p", "1e20"): {300: 100, 350: 120, 400: 130, 450: 110, 500: 90},
    }

    with open(outpath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["temperature_K", "seebeck_uV_K", "compound", "carrier_type", "carrier_concentration_cm3"])
        for comp in comps:
            for typ in types:
                for conc in concs:
                    key = (comp, typ, conc)
                    if key not in data:
                        continue
                    for T in temps:
                        s = data[key][T]
                        writer.writerow([T, s, comp, typ, conc])

if __name__ == "__main__":
    outpath = sys.argv[1]
    generate(outpath)