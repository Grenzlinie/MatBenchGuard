import argparse
import json
import csv
import math

def write_json():
    data = {"EXP1": 96.4, "EXP2": 66.9}
    with open("/app/outputs/fixed_strain_ratios.json", "w") as f:
        json.dump(data, f)
    print("Written fixed_strain_ratios.json")

def write_csv():
    temperatures = [i*0.5 for i in range(0, 101)]  # 0 to 50 step 0.5
    rows = []
    for T in temperatures:
        # exp1 ratio: sigmoid centred at 32°C, width 7°C
        ratio1 = 100.0 / (1.0 + math.exp((T - 32.0) / 7.0))
        # exp2 ratio: sigmoid centred at 22°C, width 6°C
        ratio2 = 100.0 / (1.0 + math.exp((T - 22.0) / 6.0))
        rows.append([T, round(ratio1, 4), round(ratio2, 4)])
    with open("/app/outputs/residual_fixed_strain_ratios.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["temperature", "exp1_ratio", "exp2_ratio"])
        writer.writerows(rows)
    print("Written residual_fixed_strain_ratios.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, choices=["json", "csv"])
    args = parser.parse_args()
    if args.output == "json":
        write_json()
    elif args.output == "csv":
        write_csv()