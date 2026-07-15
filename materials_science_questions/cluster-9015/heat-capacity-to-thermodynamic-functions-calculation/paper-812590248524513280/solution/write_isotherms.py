import csv, sys

out = sys.argv[1]
rows = []

# Data approximated from Fig. 7
# 450 C
rows.append({"T_C": 450, "region_label": "BCC_A2", "x_Fe": 0.98, "x_Al": 0.02, "x_P": 0.0})
rows.append({"T_C": 450, "region_label": "BCC_A2+AlP", "x_Fe": 0.95, "x_Al": 0.03, "x_P": 0.02})
rows.append({"T_C": 450, "region_label": "BCC_A2+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 450, "region_label": "BCC_B2", "x_Fe": 0.5, "x_Al": 0.5, "x_P": 0.0})
rows.append({"T_C": 450, "region_label": "BCC_B2+AlP", "x_Fe": 0.5, "x_Al": 0.5, "x_P": 0.0})
rows.append({"T_C": 450, "region_label": "BCC_B2+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 450, "region_label": "Me3P+AlP", "x_Fe": 0.6, "x_Al": 0.15, "x_P": 0.25})
rows.append({"T_C": 450, "region_label": "Me3P+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 450, "region_label": "Me2P+AlP", "x_Fe": 0.52, "x_Al": 0.18, "x_P": 0.3})
rows.append({"T_C": 450, "region_label": "Me2P+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 450, "region_label": "Al13Fe4+AlP", "x_Fe": 0.24, "x_Al": 0.76, "x_P": 0.0})
rows.append({"T_C": 450, "region_label": "Al13Fe4+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 450, "region_label": "Al5Fe2+Al13Fe4", "x_Fe": 0.15, "x_Al": 0.85, "x_P": 0.0})
rows.append({"T_C": 450, "region_label": "Al5Fe2+Al13Fe4", "x_Fe": 0.24, "x_Al": 0.76, "x_P": 0.0})

# 650 C
rows.append({"T_C": 650, "region_label": "BCC_A2", "x_Fe": 0.96, "x_Al": 0.04, "x_P": 0.0})
rows.append({"T_C": 650, "region_label": "BCC_A2+AlP", "x_Fe": 0.93, "x_Al": 0.05, "x_P": 0.02})
rows.append({"T_C": 650, "region_label": "BCC_A2+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 650, "region_label": "BCC_B2+AlP", "x_Fe": 0.5, "x_Al": 0.5, "x_P": 0.0})
rows.append({"T_C": 650, "region_label": "BCC_B2+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 650, "region_label": "Me3P+AlP", "x_Fe": 0.58, "x_Al": 0.17, "x_P": 0.25})
rows.append({"T_C": 650, "region_label": "Me3P+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 650, "region_label": "Me2P+AlP", "x_Fe": 0.5, "x_Al": 0.2, "x_P": 0.3})
rows.append({"T_C": 650, "region_label": "Me2P+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 650, "region_label": "Al13Fe4+AlP", "x_Fe": 0.24, "x_Al": 0.76, "x_P": 0.0})
rows.append({"T_C": 650, "region_label": "Al13Fe4+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})

# 800 C (including liquid regions)
rows.append({"T_C": 800, "region_label": "L", "x_Fe": 0.68, "x_Al": 0.15, "x_P": 0.17})
rows.append({"T_C": 800, "region_label": "L+BCC_A2", "x_Fe": 0.7, "x_Al": 0.12, "x_P": 0.18})
rows.append({"T_C": 800, "region_label": "L+BCC_A2", "x_Fe": 0.94, "x_Al": 0.04, "x_P": 0.02})
rows.append({"T_C": 800, "region_label": "L+AlP", "x_Fe": 0.6, "x_Al": 0.25, "x_P": 0.15})
rows.append({"T_C": 800, "region_label": "L+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 800, "region_label": "BCC_A2+AlP", "x_Fe": 0.93, "x_Al": 0.05, "x_P": 0.02})
rows.append({"T_C": 800, "region_label": "BCC_A2+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})
rows.append({"T_C": 800, "region_label": "Me3P+AlP", "x_Fe": 0.58, "x_Al": 0.17, "x_P": 0.25})
rows.append({"T_C": 800, "region_label": "Me3P+AlP", "x_Fe": 0.0, "x_Al": 0.5, "x_P": 0.5})

with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=["T_C", "region_label", "x_Fe", "x_Al", "x_P"])
    w.writeheader()
    w.writerows(rows)
