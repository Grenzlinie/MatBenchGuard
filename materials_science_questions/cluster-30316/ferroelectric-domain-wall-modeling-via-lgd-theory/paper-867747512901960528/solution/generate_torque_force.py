import json
import math
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_file')
    args = parser.parse_args()
    
    with open('/app/outputs/scattering_parameters.json', 'r') as f:
        sp = json.load(f)
    
    kls = sp['k_lambda']
    kappa = 0.2
    
    with open(args.output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k_lambda', 'tau_dimless', 'F_dimless', 'tau_approx_dimless', 'F_approx_dimless'])
        for i, kl in enumerate(kls):
            t_u = sp['u_trans_amplitude'][i]
            t_v = sp['v_trans_amplitude'][i]
            r_u = sp['u_refl_amplitude'][i]
            r_v = sp['v_refl_amplitude'][i]
            phi_t_u = sp['u_trans_phase'][i]
            phi_t_v = sp['v_trans_phase'][i]
            phi_r_u = sp['u_refl_phase'][i]
            phi_r_v = sp['v_refl_phase'][i]
            
            delta_phi_t = phi_t_u - phi_t_v
            delta_phi_r = phi_r_u - phi_r_v
            
            tau = 1 - t_u * t_v * math.cos(delta_phi_t) - r_u * r_v * math.cos(delta_phi_r)
            F = r_u**2 + r_v**2
            
            tau_approx = 1 - math.cos(kl * math.log(1 - kappa))
            F_approx = (kappa * kl)**2
            
            writer.writerow([kl, tau, F, tau_approx, F_approx])

if __name__ == '__main__':
    main()
