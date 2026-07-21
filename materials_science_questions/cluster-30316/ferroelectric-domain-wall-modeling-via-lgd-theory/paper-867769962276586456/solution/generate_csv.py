import csv

thetas = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
y_set = {0, 60, 120, 180, 240, 300}

materials = {
    "LiNbO3": {"F_DW": 1.5e9, "F_d_x": 2.0e7},
    "LiTaO3": {"F_DW": 1.0e9, "F_d_x": 1.0e7},
}

with open("/app/outputs/domain_wall_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["material", "theta_deg", "F_DW_J_m3", "F_d_J_m3", "F_total_J_m3"])
    for mat, vals in materials.items():
        dw = vals["F_DW"]
        fd_x = vals["F_d_x"]
        for th in thetas:
            fd = 0.0 if th in y_set else fd_x
            total = dw + fd
            w.writerow([mat, th, f"{dw:.6g}", f"{fd:.6g}", f"{total:.6g}"])
