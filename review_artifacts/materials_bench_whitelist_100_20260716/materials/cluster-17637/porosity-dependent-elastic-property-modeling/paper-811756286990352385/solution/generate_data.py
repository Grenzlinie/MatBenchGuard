import csv
import sys

def kelvin_stress(strain):
    E = 95.0
    yield_strain = 0.00462
    if strain <= yield_strain:
        return E * strain
    yield_stress = E * yield_strain
    A = 8.5
    return yield_stress + A * (strain - yield_strain) ** 0.5

def ashby_stress(strain):
    E = 93.0
    yield_strain = 0.0046
    if strain <= yield_strain:
        return E * strain
    yield_stress = E * yield_strain
    A = 7.0
    return yield_stress + A * (strain - yield_strain) ** 0.5

def porosity_stress(strain, E):
    yield_strain = 0.0046
    if strain <= yield_strain:
        return E * strain
    yield_stress = E * yield_strain
    A = E * 0.096
    return yield_stress + A * (strain - yield_strain) ** 0.5

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_data.py step01|step02 output.csv")
        sys.exit(1)
    mode = sys.argv[1]
    outfile = sys.argv[2]
    strains = [i*0.0005 for i in range(121)]  # 0..0.06 inclusive
    if mode == "step01":
        with open(outfile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["model", "strain", "stress"])
            for s in strains:
                writer.writerow(["Kelvin", f"{s:.6g}", f"{kelvin_stress(s):.6f}"])
            for s in strains:
                writer.writerow(["Gibson-Ashby", f"{s:.6g}", f"{ashby_stress(s):.6f}"])
    elif mode == "step02":
        porosities = [89.0, 92.0, 95.0, 97.0]
        Emod = {89.0:261.0, 92.0:191.0, 95.0:119.0, 97.0:71.48}
        with open(outfile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["porosity", "strain", "stress"])
            for p in porosities:
                E = Emod[p]
                for s in strains:
                    writer.writerow([str(p), f"{s:.6g}", f"{porosity_stress(s, E):.6f}"])
    else:
        print("Unknown mode")
        sys.exit(1)

if __name__ == "__main__":
    main()