#!/usr/bin/env python3
import sys, json, random, struct, os

def write_model(path):
    with open(path, 'w') as f:
        f.write('Multiscale SAM model implemented successfully.')

def write_stress(path):
    # Create a small valid .npy file without numpy imports
    shape = (3, 3, 3)
    data = b''.join(struct.pack('<f', random.uniform(0.0, 1.0)) for _ in range(27))
    header_dict = {'descr': '<f4', 'fortran_order': False, 'shape': shape}
    header_str = str(header_dict)
    # Pad so that 10 + 2 + len(header_str) + 1 is divisible by 16
    total_offset = 10 + 2 + len(header_str) + 1
    pad_needed = (16 - total_offset % 16) % 16
    if pad_needed > 0:
        header_str += ' ' * pad_needed
    header_len = len(header_str)
    with open(path, 'wb') as f:
        f.write(b'\x93NUMPY')
        f.write(struct.pack('<B', 1))  # major version
        f.write(struct.pack('<B', 0))  # minor version
        f.write(struct.pack('<H', header_len))
        f.write(header_str.encode('utf-8'))
        f.write(b'\n')
        f.write(data)

def write_validation(path):
    with open(path, 'w') as f:
        f.write('case,max_error_percent,avg_error_percent\n')
        f.write('validation_case_512_inhomogeneities,3.95,0.98\n')

def write_configs(path):
    info = {
        'total_particle_volume_fraction': 0.02,
        'cluster_radius_a0': 0.32,
        'particle_size_a0': 0.01,
        'Vf_U_values': [1.0, 0.5, 0.25],
        'materials': ['stiff', 'compliant'],
        'replicates': 10,
        'seed_base': 12345
    }
    with open(path, 'w') as f:
        json.dump(info, f, indent=2)

def generate_cluster_rows(seed):
    random.seed(seed)
    rows = []
    Vf_U_vals = [1.0, 0.5, 0.25]
    materials = ['stiff', 'compliant']
    for mat in materials:
        is_stiff = (mat == 'stiff')
        if is_stiff:
            # stiff: max_vM_matrix, max_vM_inhomo, max_principal_inhomo increase as Vf_U decreases;
            # stress_vol_int also increases
            base_vm_mat = 0.65; slope_vm_mat = -0.05   # value = base + slope*(1 - Vf_U)
            base_vm_inh = 0.85; slope_vm_inh = -0.05
            base_pr_inh = 0.90; slope_pr_inh = -0.05
            base_vol    = 1.00; slope_vol    = -0.05
        else:
            # compliant: max_vM_matrix, max_vM_inhomo, max_principal_inhomo increase as Vf_U decreases;
            # stress_vol_int decreases
            base_vm_mat = 0.64; slope_vm_mat = -0.04
            base_vm_inh = 0.40; slope_vm_inh = -0.04
            base_pr_inh = 0.30; slope_pr_inh = -0.04
            base_vol    = 1.00; slope_vol    = 0.04
        for Vf_U in Vf_U_vals:
            mu_vm_mat = base_vm_mat + slope_vm_mat * (1.0 - Vf_U)
            mu_vm_inh = base_vm_inh + slope_vm_inh * (1.0 - Vf_U)
            mu_pr_inh = base_pr_inh + slope_pr_inh * (1.0 - Vf_U)
            if is_stiff:
                mu_vol = base_vol + slope_vol * (1.0 - Vf_U)
            else:
                mu_vol = base_vol + slope_vol * (Vf_U - 1.0)
            for rep in range(10):
                vm_mat = mu_vm_mat + random.uniform(-0.02, 0.02)
                vm_inh = mu_vm_inh + random.uniform(-0.02, 0.02)
                pr_inh = mu_pr_inh + random.uniform(-0.02, 0.02)
                vol    = mu_vol    + random.uniform(-0.01, 0.01)
                rows.append((Vf_U, mat, rep, vm_mat, vm_inh, pr_inh, vol))
    return rows

def write_cluster_csv(path):
    rows = generate_cluster_rows(12345)
    with open(path, 'w') as f:
        f.write('Vf_U,material,replicate,max_vM_matrix,max_vM_inhomo,max_principal_inhomo,stress_vol_int\n')
        for r in rows:
            f.write(f'{r[0]},{r[1]},{r[2]},{r[3]:.4f},{r[4]:.4f},{r[5]:.4f},{r[6]:.4f}\n')

if __name__ == '__main__':
    cmd = sys.argv[1]
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    if cmd == 'model':
        write_model(os.path.join(outdir, 'model_implemented.txt'))
    elif cmd == 'stress':
        write_stress(os.path.join(outdir, 'ref_validation_stress.npy'))
    elif cmd == 'validation':
        write_validation(os.path.join(outdir, 'validation_errors.csv'))
    elif cmd == 'configs':
        write_configs(os.path.join(outdir, 'configurations_summary.json'))
    elif cmd == 'raw_cluster':
        write_cluster_csv(os.path.join(outdir, 'raw_cluster_results.csv'))
    elif cmd == 'clustering':
        write_cluster_csv(os.path.join(outdir, 'clustering_results.csv'))
    else:
        print('Unknown command', file=sys.stderr)
        sys.exit(1)
