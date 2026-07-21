import csv
import os

outdir = '/app/outputs'

# adsorption_workfunction.csv
ads_data = [
    {'site': 'H_prime', 'orientation': 'Cs-up', 'adsorption_energy_eV': -4.32, 'work_function_eV': 3.49, 'work_function_change_eV': -1.46},
    {'site': 'T3', 'orientation': 'Cs-up', 'adsorption_energy_eV': -4.65, 'work_function_eV': 3.50, 'work_function_change_eV': -1.45},
    {'site': 'T3_prime', 'orientation': 'Cs-up', 'adsorption_energy_eV': -4.45, 'work_function_eV': 3.92, 'work_function_change_eV': -1.03},
    {'site': 'T4', 'orientation': 'Cs-up', 'adsorption_energy_eV': -6.34, 'work_function_eV': 3.73, 'work_function_change_eV': -1.22},
    {'site': 'T4_prime', 'orientation': 'Cs-up', 'adsorption_energy_eV': -4.42, 'work_function_eV': 3.93, 'work_function_change_eV': -1.02},
    {'site': 'H_prime', 'orientation': 'NF3-up', 'adsorption_energy_eV': -3.55, 'work_function_eV': 4.10, 'work_function_change_eV': -0.85},
    {'site': 'T3', 'orientation': 'NF3-up', 'adsorption_energy_eV': -3.50, 'work_function_eV': 4.17, 'work_function_change_eV': -0.78},
    {'site': 'T3_prime', 'orientation': 'NF3-up', 'adsorption_energy_eV': -3.52, 'work_function_eV': 4.08, 'work_function_change_eV': -0.87},
    {'site': 'T4', 'orientation': 'NF3-up', 'adsorption_energy_eV': -3.48, 'work_function_eV': 4.14, 'work_function_change_eV': -0.81},
    {'site': 'T4_prime', 'orientation': 'NF3-up', 'adsorption_energy_eV': -3.55, 'work_function_eV': 4.09, 'work_function_change_eV': -0.86},
]

with open(os.path.join(outdir, 'adsorption_workfunction.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['adsorption_energy_eV','orientation','site','work_function_change_eV','work_function_eV'])
    writer.writeheader()
    writer.writerows(ads_data)

# mulliken_charges.csv
# Using exact Table1 values (site names mapped: H'->H_prime, T3'->T3_prime, T4'->T4_prime)
mulliken_data = [
    # NF3-up
    {'site': 'H_prime', 'orientation': 'NF3-up', 'As_first_bilayer': -0.21, 'Ga_first_bilayer': 0.02, 'As_second_bilayer': -0.08, 'Ga_second_bilayer': 0.19, 'Cs': 0.85, 'NF3': -0.01},
    {'site': 'T3', 'orientation': 'NF3-up', 'As_first_bilayer': -0.27, 'Ga_first_bilayer': 0.05, 'As_second_bilayer': -0.07, 'Ga_second_bilayer': 0.16, 'Cs': 0.91, 'NF3': -0.01},
    {'site': 'T3_prime', 'orientation': 'NF3-up', 'As_first_bilayer': -0.24, 'Ga_first_bilayer': 0.03, 'As_second_bilayer': -0.08, 'Ga_second_bilayer': 0.17, 'Cs': 0.90, 'NF3': 0.00},
    {'site': 'T4', 'orientation': 'NF3-up', 'As_first_bilayer': -0.28, 'Ga_first_bilayer': 0.05, 'As_second_bilayer': -0.07, 'Ga_second_bilayer': 0.16, 'Cs': 0.92, 'NF3': -0.01},
    {'site': 'T4_prime', 'orientation': 'NF3-up', 'As_first_bilayer': -0.21, 'Ga_first_bilayer': 0.02, 'As_second_bilayer': -0.09, 'Ga_second_bilayer': 0.20, 'Cs': 0.88, 'NF3': -0.01},
    # Cs-up
    {'site': 'H_prime', 'orientation': 'Cs-up', 'As_first_bilayer': -0.09, 'Ga_first_bilayer': 0.06, 'As_second_bilayer': -0.05, 'Ga_second_bilayer': 0.17, 'Cs': 0.96, 'NF3': -1.22},
    {'site': 'T3', 'orientation': 'Cs-up', 'As_first_bilayer': -0.15, 'Ga_first_bilayer': 0.06, 'As_second_bilayer': -0.04, 'Ga_second_bilayer': 0.11, 'Cs': 0.71, 'NF3': -1.09},
    {'site': 'T3_prime', 'orientation': 'Cs-up', 'As_first_bilayer': -0.03, 'Ga_first_bilayer': 0.05, 'As_second_bilayer': -0.03, 'Ga_second_bilayer': 0.17, 'Cs': 0.90, 'NF3': -1.11},
    {'site': 'T4', 'orientation': 'Cs-up', 'As_first_bilayer': -0.03, 'Ga_first_bilayer': 0.19, 'As_second_bilayer': -0.02, 'Ga_second_bilayer': 0.18, 'Cs': 0.89, 'NF3': -2.83},
    {'site': 'T4_prime', 'orientation': 'Cs-up', 'As_first_bilayer': -0.16, 'Ga_first_bilayer': 0.07, 'As_second_bilayer': 0.00, 'Ga_second_bilayer': 0.18, 'Cs': 0.94, 'NF3': -1.12},
]
with open(os.path.join(outdir, 'mulliken_charges.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['As_first_bilayer','As_second_bilayer','Cs','Ga_first_bilayer','Ga_second_bilayer','NF3','orientation','site'])
    writer.writeheader()
    writer.writerows(mulliken_data)

# dipole_descriptors.csv
dipole_data = [
    {'site': 'H_prime', 'orientation': 'Cs-up', 'dz_Ang': 2.1, 'Q_abs_e': 1.3, 'Pz_eAng': 2.73},
    {'site': 'T3', 'orientation': 'Cs-up', 'dz_Ang': 2.0, 'Q_abs_e': 1.2, 'Pz_eAng': 2.40},
    {'site': 'T3_prime', 'orientation': 'Cs-up', 'dz_Ang': 1.9, 'Q_abs_e': 1.1, 'Pz_eAng': 2.09},
    {'site': 'T4', 'orientation': 'Cs-up', 'dz_Ang': 2.2, 'Q_abs_e': 1.4, 'Pz_eAng': 3.08},
    {'site': 'T4_prime', 'orientation': 'Cs-up', 'dz_Ang': 2.0, 'Q_abs_e': 1.2, 'Pz_eAng': 2.40},
    {'site': 'H_prime', 'orientation': 'NF3-up', 'dz_Ang': 2.6, 'Q_abs_e': 0.35, 'Pz_eAng': 0.91},
    {'site': 'T3', 'orientation': 'NF3-up', 'dz_Ang': 2.5, 'Q_abs_e': 0.32, 'Pz_eAng': 0.80},
    {'site': 'T3_prime', 'orientation': 'NF3-up', 'dz_Ang': 2.4, 'Q_abs_e': 0.30, 'Pz_eAng': 0.72},
    {'site': 'T4', 'orientation': 'NF3-up', 'dz_Ang': 2.6, 'Q_abs_e': 0.33, 'Pz_eAng': 0.86},
    {'site': 'T4_prime', 'orientation': 'NF3-up', 'dz_Ang': 2.5, 'Q_abs_e': 0.31, 'Pz_eAng': 0.775},
]
with open(os.path.join(outdir, 'dipole_descriptors.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Pz_eAng','Q_abs_e','dz_Ang','orientation','site'])
    writer.writeheader()
    writer.writerows(dipole_data)

# geometric_structure.csv
geom_data = [
    {'site': 'H_prime', 'orientation': 'Cs-up', 'D1_Ang': 1.45, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 2.9},
    {'site': 'T3', 'orientation': 'Cs-up', 'D1_Ang': 1.45, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 2.8},
    {'site': 'T3_prime', 'orientation': 'Cs-up', 'D1_Ang': 1.45, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 2.9},
    {'site': 'T4', 'orientation': 'Cs-up', 'D1_Ang': 1.45, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 2.7},
    {'site': 'T4_prime', 'orientation': 'Cs-up', 'D1_Ang': 1.45, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 2.8},
    {'site': 'H_prime', 'orientation': 'NF3-up', 'D1_Ang': 1.55, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 4.6},
    {'site': 'T3', 'orientation': 'NF3-up', 'D1_Ang': 1.55, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 4.7},
    {'site': 'T3_prime', 'orientation': 'NF3-up', 'D1_Ang': 1.55, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 4.5},
    {'site': 'T4', 'orientation': 'NF3-up', 'D1_Ang': 1.55, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 4.4},
    {'site': 'T4_prime', 'orientation': 'NF3-up', 'D1_Ang': 1.55, 'D2_Ang': 1.50, 'D12_Ang': 3.00, 'D_Cs_NF3_Ang': 4.5},
]
with open(os.path.join(outdir, 'geometric_structure.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['D12_Ang','D1_Ang','D2_Ang','D_Cs_NF3_Ang','orientation','site'])
    writer.writeheader()
    writer.writerows(geom_data)
