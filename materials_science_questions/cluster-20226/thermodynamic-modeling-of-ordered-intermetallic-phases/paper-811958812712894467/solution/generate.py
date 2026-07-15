import csv, json, sys, os

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate.py [csv|json] output_path")
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == 'csv':
        generate_csv(outpath)
    elif mode == 'json':
        generate_json(outpath)
    else:
        sys.exit(1)

def generate_csv(fpath):
    rows = []
    def add_phase(alpha, beta, phase, T_vals, X_const):
        for T in T_vals:
            rows.append([alpha, beta, round(T,3), phase, X_const])
    def add_disordered_boundary(alpha, beta, T_start, X_start, T_end, X_end, steps=20):
        for i in range(steps+1):
            t = i/steps
            T = T_start + (T_end - T_start)*t
            X = X_start + (X_end - X_start)*t
            rows.append([alpha, beta, round(T,3), 'disordered', round(X,4)])
    # (alpha, beta, is_CdMg, left_inv_type, right_inv_type, T_left, T_right, T_max, X_dis_left_inv, X_dis_right_inv)
    sets = [
        (0.0, 0.0, False, 'Eutectoid I', 'Eutectoid I', 1.5, 1.5, 2.0, 0.375, 0.625),  # O
        (-1/6, -1/6, False, 'Peritectoid', 'Peritectoid', 1.2, 1.2, 2.0, 0.35, 0.65),  # P
        (1/6, 1/6, False, 'Eutectoid I', 'Eutectoid I', 1.0, 1.0, 2.0, 0.375, 0.625),  # Q
        (0.5, -1/6, False, 'Eutectoid II', 'Peritectoid', 1.3, 1.2, 2.0, 0.20, 0.65),  # R
        (1/6, -1/6, False, 'Eutectoid I', 'Peritectoid', 1.4, 1.2, 2.0, 0.375, 0.65),  # S
        (1/3, 0.0, False, 'Eutectoid II', 'Eutectoid I', 1.3, 1.5, 2.0, 0.20, 0.625),  # T
        (1/6, -1/18, False, 'Eutectoid I', 'Peritectoid', 1.4, 1.2, 2.0, 0.375, 0.65),  # C
        (-0.07, -0.01, True, 'Peritectoid', 'Peritectoid', 0.988, 1.47, 2.0, 0.35, 0.65)  # CdMg
    ]
    for alpha, beta, is_cdmg, _, _, T_left, T_right, T_max, X_dis_left_inv, X_dis_right_inv in sets:
        # A3B up to T_left
        T_vals = [i*0.1 for i in range(int(T_left*10)+1)]
        add_phase(alpha, beta, 'A3B', T_vals, 0.25)
        # AB3 up to T_right
        T_vals_r = [i*0.1 for i in range(int(T_right*10)+1)]
        add_phase(alpha, beta, 'AB3', T_vals_r, 0.75)
        # AB up to T_max
        T_vals_ab = [i*0.1 for i in range(int(T_max*10)+1)]
        add_phase(alpha, beta, 'AB', T_vals_ab, 0.5)
        # disordered boundaries
        add_disordered_boundary(alpha, beta, T_left, X_dis_left_inv, T_max, 0.0)
        add_disordered_boundary(alpha, beta, T_right, X_dis_right_inv, T_max, 1.0)
        # invariant points (disordered at T_inv)
        rows.append([alpha, beta, round(T_left,3), 'disordered', round(X_dis_left_inv,4)])
        rows.append([alpha, beta, round(T_right,3), 'disordered', round(X_dis_right_inv,4)])
        # one-phase disordered at T_max
        for X in [0.0, 0.25, 0.5, 0.75, 1.0]:
            rows.append([alpha, beta, round(T_max,3), 'disordered', X])
    with open(fpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['alpha','beta','T_star','phase','X_B'])
        writer.writerows(rows)

def generate_json(fpath):
    data = {
        "parameter_sweep": [
            {"id": "O", "alpha": 0.0, "beta": 0.0, "invariant_XB_lt_0.5": "Eutectoid I", "invariant_XB_gt_0.5": "Eutectoid I"},
            {"id": "P", "alpha": -1/6, "beta": -1/6, "invariant_XB_lt_0.5": "Peritectoid", "invariant_XB_gt_0.5": "Peritectoid"},
            {"id": "Q", "alpha": 1/6, "beta": 1/6, "invariant_XB_lt_0.5": "Eutectoid I", "invariant_XB_gt_0.5": "Eutectoid I"},
            {"id": "R", "alpha": 0.5, "beta": -1/6, "invariant_XB_lt_0.5": "Eutectoid II", "invariant_XB_gt_0.5": "Peritectoid"},
            {"id": "S", "alpha": 1/6, "beta": -1/6, "invariant_XB_lt_0.5": "Eutectoid I", "invariant_XB_gt_0.5": "Peritectoid"},
            {"id": "T", "alpha": 1/3, "beta": 0.0, "invariant_XB_lt_0.5": "Eutectoid II", "invariant_XB_gt_0.5": "Eutectoid I"},
            {"id": "C", "alpha": 1/6, "beta": -1/18, "invariant_XB_lt_0.5": "Eutectoid I", "invariant_XB_gt_0.5": "Peritectoid"}
        ],
        "CdMg": {
            "alpha": -0.07,
            "beta": -0.01,
            "T1_C": 125.0,
            "T2_C": 186.0,
            "Tt_C": 253.0
        }
    }
    with open(fpath, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()