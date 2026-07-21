import numpy as np
import scipy.special as sp
import csv

def riccati_psi(n, z):
    j, jd = sp.spherical_jn(n, z, derivative=True)
    psi = z * j
    psid = j + z * jd
    return psi, psid

def riccati_xi(n, z):
    j, jd = sp.spherical_jn(n, z, derivative=True)
    y, yd = sp.spherical_yn(n, z, derivative=True)
    h1 = j + 1j*y
    h1d = jd + 1j*yd
    xi = z * h1
    xid = h1 + z * h1d
    return xi, xid

def Mie_coeffs(n, m, x):
    psi_x, psid_x = riccati_psi(n, x)
    psi_mx, psid_mx = riccati_psi(n, m*x)
    xi_x, xid_x = riccati_xi(n, x)
    denom_a = m * psi_mx * xid_x - xi_x * psid_mx
    denom_b = psi_mx * xid_x - m * xi_x * psid_mx
    num_c = m * (psi_x * psid_mx - psid_x * psi_mx)
    num_d = psi_x * psid_mx - psid_x * psi_mx
    c_n = num_c / denom_a
    d_n = num_d / denom_b
    return c_n, d_n

n_ref = 1.33
alphas = [2, 4, 6, 8, 10]

output_rows = []
for alpha in alphas:
    x = alpha
    mx = n_ref * alpha
    c1, d1 = Mie_coeffs(1, n_ref, x)
    xr = mx
    # I1
    I1 = (2*xr**4 - 2*xr**2 - 1 + np.cos(2*xr) + 2*xr*np.sin(2*xr)) / (8*xr**4)
    # I2
    from scipy.special import sici
    Si, Ci = sici(2*xr)
    gamma = sp.euler_gamma
    term1 = gamma - 1 - Ci + np.log(2*xr)
    term2 = (2*xr*np.cos(xr) - np.sin(xr)) * np.sin(xr) / xr**2
    I2 = 0.5 * (term1 + term2)
    # I3
    I3 = I1 + I2 - (xr**2 - 3*np.sin(xr)**2 + xr*np.sin(2*xr)) / (2*xr**2)
    output_rows.append([alpha, c1.real, c1.imag, d1.real, d1.imag, I1, I2, I3])

with open('/app/outputs/mie_internal_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha', 'c1_real', 'c1_imag', 'd1_real', 'd1_imag', 'I1', 'I2', 'I3'])
    for row in output_rows:
        writer.writerow(row)