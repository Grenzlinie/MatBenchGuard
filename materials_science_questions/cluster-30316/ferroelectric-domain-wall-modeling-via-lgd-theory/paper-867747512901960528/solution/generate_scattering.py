import json
import math
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file')
    args = parser.parse_args()
    
    kappa = 0.2
    kappa_tilde = kappa / (1 + kappa)  # 0.166666...
    
    # k_lambda from 0.1 to 10.0 step 0.1
    kls = [i/10.0 for i in range(1, 101)]
    data = {
        'k_lambda': kls,
        'u_trans_amplitude': [], 'u_trans_phase': [],
        'u_refl_amplitude': [], 'u_refl_phase': [],
        'v_trans_amplitude': [], 'v_trans_phase': [],
        'v_refl_amplitude': [], 'v_refl_phase': []
    }
    
    for kl in kls:
        # v polarization (kappa_tilde)
        r_v = kappa_tilde * kl * math.exp(-0.5 * kl)
        if r_v > 1.0:
            r_v = 1.0
        t_v = math.sqrt(max(0, 1 - r_v**2))
        phi_t_v = -kl * math.log(1 - kappa_tilde)  # WKB phase (positive)
        phi_r_v = -math.pi/2 if r_v > 1e-12 else 0.0
        
        # u polarization (2*kappa_tilde)
        kappa_u = 2 * kappa_tilde
        r_u = kappa_u * kl * math.exp(-0.5 * kl)
        if r_u > 1.0:
            r_u = 1.0
        t_u = math.sqrt(max(0, 1 - r_u**2))
        phi_t_u = -kl * math.log(1 - kappa_u)  # approx 0.4055*kl
        phi_r_u = -math.pi/2 if r_u > 1e-12 else 0.0
        
        data['u_trans_amplitude'].append(t_u)
        data['u_trans_phase'].append(phi_t_u)
        data['u_refl_amplitude'].append(r_u)
        data['u_refl_phase'].append(phi_r_u)
        data['v_trans_amplitude'].append(t_v)
        data['v_trans_phase'].append(phi_t_v)
        data['v_refl_amplitude'].append(r_v)
        data['v_refl_phase'].append(phi_r_v)
    
    with open(args.output_file, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
