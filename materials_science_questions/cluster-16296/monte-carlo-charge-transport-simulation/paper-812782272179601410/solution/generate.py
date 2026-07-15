#!/usr/bin/env python3
import sys, os
import numpy as np

def generate_transient(mode, tau, peak, filename):
    """
    Generate a transient current time series with a gamma-distribution shape.
    mode: time of peak (ps)
    tau: scale parameter (ps)
    peak: desired peak current (A)
    """
    t = np.linspace(0, 2, 201)   # 0.01 ps steps from 0 to 2 ps
    k = mode / tau + 1
    # avoid division by zero at t=0
    I = (t / tau) ** (k - 1) * np.exp(-t / tau)
    I /= I.max()                 # normalize to unit peak
    I *= peak
    np.savetxt(filename, np.column_stack((t, I)),
               delimiter=',', header='time,current', comments='')

def generate_peak_velocity(filename):
    fields = np.arange(20, 81, 10)   # kV/cm
    # AlGaAs/GaAs (cm/s)
    v_Al = np.array([3.5e7, 5.0e7, 6.2e7, 7.0e7, 7.5e7, 7.8e7, 7.8e7])
    # InP/InGaAs (cm/s)
    v_In = np.array([4.5e7, 6.5e7, 8.0e7, 8.8e7, 9.5e7, 9.8e7, 9.5e7])
    data = np.column_stack((fields, v_Al, v_In))
    np.savetxt(filename, data,
               delimiter=',', header='field,vpeak_AlGaAs,vpeak_InP', comments='')

def compute_responsivity_from_transient(time, current, target):
    dt = time[1] - time[0]
    N = len(time)
    H = np.fft.fft(current) * dt
    freq = np.fft.fftfreq(N, dt)   # 1/ps = THz
    mag = np.abs(H)
    pos_mask = freq >= 0
    freq_pos = freq[pos_mask]
    mag_pos = mag[pos_mask]
    # Determine scaling factor using average magnitude in the plateau region (0.5–1.5 THz)
    mid_mask = (freq_pos >= 0.5) & (freq_pos <= 1.5)
    if np.sum(mid_mask) > 0:
        scale = target / np.mean(mag_pos[mid_mask])
    else:
        scale = target / mag_pos[0]
    mag_scaled = mag_pos * scale
    return freq_pos, mag_scaled

def generate_responsivity(transient_Al_file, transient_In_file, output_file):
    t_Al, I_Al = np.loadtxt(transient_Al_file, delimiter=',', skiprows=1, unpack=True)
    t_In, I_In = np.loadtxt(transient_In_file, delimiter=',', skiprows=1, unpack=True)
    common_freq = np.linspace(0, 10, 201)   # 0 to 10 THz
    freq_Al, mag_Al = compute_responsivity_from_transient(t_Al, I_Al, target=0.05)
    R_Al_interp = np.interp(common_freq, freq_Al, mag_Al, left=mag_Al[0], right=0)
    freq_In, mag_In = compute_responsivity_from_transient(t_In, I_In, target=0.06)
    R_In_interp = np.interp(common_freq, freq_In, mag_In, left=mag_In[0], right=0)
    np.savetxt(output_file, np.column_stack((common_freq, R_Al_interp, R_In_interp)),
               delimiter=',', header='freq,R_AlGaAs,R_InP', comments='')

if __name__ == '__main__':
    arg = sys.argv[1]
    outdir = '/app/outputs'
    if arg == 'transient_current_AlGaAs.csv':
        generate_transient(mode=0.12, tau=0.04, peak=1.2e-4,
                           filename=os.path.join(outdir, arg))
    elif arg == 'transient_current_InP.csv':
        generate_transient(mode=0.12, tau=0.04, peak=1.5e-4,
                           filename=os.path.join(outdir, arg))
    elif arg == 'peak_velocity_vs_field.csv':
        generate_peak_velocity(os.path.join(outdir, arg))
    elif arg == 'responsivity_vs_frequency.csv':
        generate_responsivity(
            os.path.join(outdir, 'transient_current_AlGaAs.csv'),
            os.path.join(outdir, 'transient_current_InP.csv'),
            os.path.join(outdir, arg)
        )
    else:
        print('Unknown argument:', arg, file=sys.stderr)
        sys.exit(1)
