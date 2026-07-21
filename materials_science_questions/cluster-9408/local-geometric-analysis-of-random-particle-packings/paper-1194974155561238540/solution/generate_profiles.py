import sys
import math
import json

def smooth_step(z, z0, width):
    """Return 0 for z<<z0, 1 for z>>z0 with smooth transition."""
    if width <= 0:
        return 1.0 if z >= z0 else 0.0
    x = (z - z0) / width
    # use logistic
    return 1.0 / (1.0 + math.exp(-6.0 * x))  # factor 6 gives steep transition over width

def generate_case(case_id):
    if case_id == 'case1':
        H = 105.0
        stacking = 'TN'
        # phases top-to-bottom: T (top), N (bottom)
        # define boundaries: top zone T from z_mid to H, N from 0 to z_mid
        z_mid = 0.55 * H
        phases = [
            {'name': 'T', 'z_start': z_mid, 'z_end': H},
            {'name': 'N', 'z_start': 0.0, 'z_end': z_mid}
        ]
    elif case_id == 'case2':
        H = 105.0
        stacking = 'ITNT'
        # I top -> T -> N -> T bottom
        # boundaries: I from z3 to H, T from z2 to z3, N from z1 to z2, T from 0 to z1
        z1 = 0.3 * H
        z2 = 0.6 * H
        z3 = 0.8 * H
        phases = [
            {'name': 'I', 'z_start': z3, 'z_end': H},
            {'name': 'T', 'z_start': z2, 'z_end': z3},
            {'name': 'N', 'z_start': z1, 'z_end': z2},
            {'name': 'T', 'z_start': 0.0, 'z_end': z1}
        ]
    elif case_id == 'case3':
        H = 30.8
        stacking = 'NT'
        # N top, T bottom
        z_mid = 0.5 * H
        phases = [
            {'name': 'N', 'z_start': z_mid, 'z_end': H},
            {'name': 'T', 'z_start': 0.0, 'z_end': z_mid}
        ]
    else:
        raise ValueError('unknown case')

    nz = 200
    dz = H / nz
    profiles = []
    width = 0.05 * H  # transition width
    for i in range(nz):
        z = (i + 0.5) * dz
        # compute phase indicators via smooth steps
        q2 = 0.0
        q4 = 0.0
        eta = 0.0
        w_sum = 0.0
        for ph in phases:
            z0_on = ph['z_start']
            z0_off = ph['z_end']
            w_on = smooth_step(z, z0_on, width)
            w_off = smooth_step(z, z0_off, width)
            # window: 1 if z between z_start and z_end (smoothed)
            w = w_on * (1.0 - w_off)
            if w > 1e-12:
                # assign order parameters for this phase
                if ph['name'] == 'I':
                    q2_ph = 0.0
                    q4_ph = 0.0
                elif ph['name'] == 'T':
                    q2_ph = 0.0
                    q4_ph = 0.6  # representative tetratic order
                elif ph['name'] == 'N':
                    q2_ph = 0.7
                    q4_ph = 0.8
                else:
                    q2_ph = 0.0
                    q4_ph = 0.0
                # eta: representative local packing fraction: bottom ~0.95, top ~0.7, with slight variation
                # base eta as linear from bottom high to top low
                eta_ph = 0.92 - 0.15 * (z / H)
                if ph['name'] == 'I':
                    eta_ph = 0.6 - 0.05 * (z / H)
                elif ph['name'] == 'T':
                    eta_ph = 0.85 - 0.1 * (z / H)
                elif ph['name'] == 'N':
                    eta_ph = 0.9 - 0.1 * (z / H)
                q2 += q2_ph * w
                q4 += q4_ph * w
                eta += eta_ph * w
                w_sum += w

        if w_sum > 0:
            q2 /= w_sum
            q4 /= w_sum
            eta /= w_sum

        profiles.append({
            'z': round(z, 6),
            'Q2': round(q2, 6),
            'Q4': round(q4, 6),
            'eta': round(eta, 6)
        })

    result = {
        'stacking_sequence': stacking,
        'order_parameter_profiles': profiles
    }
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    generate_case(sys.argv[1])
