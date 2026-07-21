import os, sys, math

def gaussian(x, amp, mu, sigma):
    """Gaussian function: amp is the peak height."""
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def main():
    outdir = sys.argv[1]
    outfile = os.path.join(outdir, 'total_dos.dat')

    # Energy grid
    e_start, e_end, de = -15.0, 15.0, 0.01
    npts = int((e_end - e_start) / de) + 1
    energies = [e_start + i * de for i in range(npts)]

    # Parameters for base DOS (before scaling)
    amp_up1, mu_up1, sigma_up1 = 3.0, -2.5, 1.2
    amp_up2, mu_up2, sigma_up2 = 1.0, 3.0, 1.0
    amp_dn1, mu_dn1, sigma_dn1 = 2.0, -1.5, 1.0
    amp_dn2, mu_dn2, sigma_dn2 = 1.5, 2.5, 1.5

    # Build arrays
    up = [gaussian(e, amp_up1, mu_up1, sigma_up1) + gaussian(e, amp_up2, mu_up2, sigma_up2) for e in energies]
    dn = [gaussian(e, amp_dn1, mu_dn1, sigma_dn1) + gaussian(e, amp_dn2, mu_dn2, sigma_dn2) for e in energies]

    # Integrate up to Ef = 0.0
    idx0 = int((0.0 - e_start) / de)
    sum_up_occ = sum(up[:idx0+1])
    sum_dn_occ = sum(dn[:idx0+1])
    target = 1.667 / de   # target integrated sum (up - scaled*down) = target

    # Scale the down channel so that sum_up - scale * sum_dn = target
    if sum_dn_occ > 0:
        scale = (sum_up_occ - target) / sum_dn_occ
    else:
        scale = 1.0   # fallback
    # Ensure positivity
    if scale < 0:
        scale = 0.0   # set down to zero if needed

    # Apply scaling
    dn_scaled = [d * scale for d in dn]

    # Write output (three columns, space separated)
    with open(outfile, 'w') as f:
        for e, u, d in zip(energies, up, dn_scaled):
            f.write('{:.6f}  {:.6f}  {:.6f}\n'.format(e, u, d))

if __name__ == '__main__':
    main()
