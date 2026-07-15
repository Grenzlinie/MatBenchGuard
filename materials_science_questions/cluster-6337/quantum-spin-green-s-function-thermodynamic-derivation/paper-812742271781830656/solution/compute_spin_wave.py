import numpy as np
import csv
import sys

output_dir = "/app/outputs"
output_file = f"{output_dir}/results.csv"

def integ_1d(z, N=10000):
    """Compute quantities for 1D lattice using grid integration."""
    kx = np.linspace(-np.pi, np.pi, N, endpoint=False)
    S = 2 * np.cos(kx)
    
    # Energy: E/(NJ) = -z/8 + (z/4)*( <sqrt(1-S/z)> - 1 )
    sqrt_term = np.sqrt(np.maximum(1 - S / z, 0))
    I_sqrt = np.mean(sqrt_term)
    energy = -z / 8 + (z / 4) * (I_sqrt - 1.0)
    
    # Occupation: diverges in 1D -> set to Inf
    occupation = float('inf')
    
    # Out-of-plane correlation: (1/(4z)) * < S(k) * sqrt(1-S(k)/z) >
    corr = np.mean(S * sqrt_term) / (4 * z)
    
    # Squared magnetization: for 1D the exact order parameter is zero,
    # and the spin-wave value diverges; we output 0.0 as a placeholder.
    sq_mag = 0.0
    
    return energy, occupation, corr, sq_mag

def integ_2d(z, N=200):
    """Compute quantities for 2D square lattice."""
    kx = np.linspace(-np.pi, np.pi, N, endpoint=False)
    ky = np.linspace(-np.pi, np.pi, N, endpoint=False)
    KX, KY = np.meshgrid(kx, ky, indexing='ij')
    S = 2 * (np.cos(KX) + np.cos(KY))
    
    sqrt_term = np.sqrt(np.maximum(1 - S / z, 0))
    I_sqrt = np.mean(sqrt_term)
    energy = -z / 8 + (z / 4) * (I_sqrt - 1.0)
    
    # Occupation
    t = (S / (2 * z)) / np.maximum(1 - S / (2 * z), 1e-12)
    t = np.clip(t, -1 + 1e-14, 1 - 1e-14)
    u = 0.5 * np.arctanh(t)
    n_matrix = np.sinh(u) ** 2
    n_val = np.mean(n_matrix)
    
    # Correlation
    corr = np.mean(S * sqrt_term) / (4 * z)
    
    # Squared magnetization: <M_z^2>/N^2 = n^2 + 1/4 (from derivation)
    sq_mag = n_val ** 2 + 0.25
    
    return energy, n_val, corr, sq_mag

def integ_3d(z, N=60):
    """Compute quantities for 3D simple cubic lattice."""
    kx = np.linspace(-np.pi, np.pi, N, endpoint=False)
    ky = np.linspace(-np.pi, np.pi, N, endpoint=False)
    kz = np.linspace(-np.pi, np.pi, N, endpoint=False)
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
    S = 2 * (np.cos(KX) + np.cos(KY) + np.cos(KZ))
    
    sqrt_term = np.sqrt(np.maximum(1 - S / z, 0))
    I_sqrt = np.mean(sqrt_term)
    energy = -z / 8 + (z / 4) * (I_sqrt - 1.0)
    
    # Occupation
    t = (S / (2 * z)) / np.maximum(1 - S / (2 * z), 1e-12)
    t = np.clip(t, -1 + 1e-14, 1 - 1e-14)
    u = 0.5 * np.arctanh(t)
    n_matrix = np.sinh(u) ** 2
    n_val = np.mean(n_matrix)
    
    # Correlation
    corr = np.mean(S * sqrt_term) / (4 * z)
    
    # Squared magnetization
    sq_mag = n_val ** 2 + 0.25
    
    return energy, n_val, corr, sq_mag

def main():
    # Linear chain (z=2)
    e1, n1, c1, m1 = integ_1d(z=2, N=10000)
    # Square lattice (z=4)
    e2, n2, c2, m2 = integ_2d(z=4, N=200)
    # Simple cubic (z=6)
    e3, n3, c3, m3 = integ_3d(z=6, N=60)
    
    # Write CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['lattice', 'energy_per_site', 'occupation_number',
                         'out_of_plane_correlation', 'squared_magnetization'])
        writer.writerow(['linear_chain', f'{e1:.6f}', 'Inf', f'{c1:.6f}', f'{m1:.6f}'])
        writer.writerow(['square_lattice', f'{e2:.6f}', f'{n2:.6f}', f'{c2:.6f}', f'{m2:.6f}'])
        writer.writerow(['simple_cubic', f'{e3:.6f}', f'{n3:.6f}', f'{c3:.6f}', f'{m3:.6f}'])

if __name__ == "__main__":
    main()