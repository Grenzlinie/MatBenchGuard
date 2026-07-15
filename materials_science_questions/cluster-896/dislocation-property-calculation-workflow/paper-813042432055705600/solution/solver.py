import numpy as np
from scipy.optimize import minimize

def get_hat_Q(N, L, E, nu):
    dx = L / N
    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    kz = np.sqrt(KX**2 + KY**2)
    hat_Q = np.zeros((N, N), dtype=complex)
    mask = kz != 0
    hat_Q[mask] = 2 * (1 - nu**2) / (E * kz[mask])
    return hat_Q, KX, KY

def forward(p, hat_Q):
    p_hat = np.fft.fft2(p)
    uz_hat = hat_Q * p_hat
    return np.fft.ifft2(uz_hat).real

def solve_contact(u_ind, d, hat_Q, maxiter=500):
    N = u_ind.shape[0]
    b = u_ind + d
    def obj(x):
        p = x.reshape((N, N))
        uz = forward(p, hat_Q)
        return 0.5 * np.sum(p * uz) - np.sum(p * b)
    def grad(x):
        p = x.reshape((N, N))
        uz = forward(p, hat_Q)
        grad_ = uz - b
        return grad_.ravel()
    p0 = np.zeros(N * N)
    bounds = [(0, None)] * (N * N)
    res = minimize(obj, p0, jac=grad, bounds=bounds, method='L-BFGS-B',
                  options={'maxiter': maxiter, 'disp': False})
    p = res.x.reshape((N, N))
    p = np.maximum(p, 0)
    return p

def compute_force(p, L):
    dx = L / p.shape[0]
    return np.sum(p) * dx * dx

def compute_stress_slice(p, L, z_vals, E, nu):
    N = p.shape[0]
    dx = L / N
    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    kz = np.sqrt(KX**2 + KY**2)
    mu = E / (2 * (1 + nu))
    lam = E * nu / ((1 + nu) * (1 - 2 * nu))
    C0 = (3 * lam + 5 * mu) / (lam + mu)
    p_hat = np.fft.fft2(p)
    sigma_zz = np.zeros(len(z_vals))
    for iz, z in enumerate(z_vals):
        mask = kz > 0
        contrib = p_hat[mask] * (-kz[mask] * z + C0) * np.exp(kz[mask] * z)
        sigma_zz[iz] = np.sum(contrib).real
    return sigma_zz

def get_indenter(R, L, N):
    dx = L / N
    x = (np.arange(N) - N / 2 + 0.5) * dx
    y = x
    X, Y = np.meshgrid(x, y, indexing='ij')
    return (X**2 + Y**2) / (2 * R)
