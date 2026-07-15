import numpy as np
import scipy.special
import scipy.interpolate
import csv, json

def main():
    N = 16
    x, w = np.polynomial.legendre.leggauss(N)   # nodes on [-1,1]
    # x = cos(theta), w are weights for integral over [-1,1]
    W = w  # diagonal weights for matrix multiplication
    
    pairs = [
        (5.0, 5.0, 'K5'),
        (1.0, 1.0, 'K1'),
        (-1.0, 1.0, 'Kminus1'),
        (-5.0, 5.0, 'Kminus5'),
    ]
    
    free_energies = []
    chi_dict = {}
    
    tol = 1e-12
    max_iter = 50
    
    for K, k, key in pairs:
        # initial matrix and column
        x_mat = x[:, None]
        x_mat2 = x[None, :]
        
        sin_theta = np.sqrt(1.0 - x_mat**2)
        sin_theta2 = np.sqrt(1.0 - x_mat2**2)
        arg = K * sin_theta * sin_theta2
        I0 = scipy.special.i0(arg)
        B = I0 * np.exp(K * (x_mat * x_mat2 - 1.0) + 0.5 * k * (x_mat + x_mat2 - 2.0))
        
        v = np.exp((K + 0.5 * k) * (x - 1.0))
        
        g_list = []
        for n in range(max_iter):
            D = np.sum(w * v**2)
            g_n = K + k + np.log(2.0 * np.pi) + np.log(D)
            g_list.append(g_n)
            
            # new v
            v_new = B.dot(w * v) / D
            # new B
            B_new = B.dot(np.multiply(W[:, None], B)) / D
            
            # check convergence
            diff = np.max(np.abs(B_new - B))
            B = B_new
            v = v_new
            if diff < tol:
                break
        
        # free energy series
        M = len(g_list)
        g_inf = K + k + np.log(4.0 * np.pi)  # asymptotic value
        # sum series up to M-1 plus tail
        sum_series = 0.0
        for i in range(M):
            sum_series += g_list[i] / (2.0 ** (i+1))
        tail = g_inf / (2.0 ** M)
        f_hat = -(sum_series + tail)
        free_energies.append((K, k, f_hat))
        
        # fixed-point f vector
        # choose reference index with largest B_diag
        diag = np.diag(B)
        ref = np.argmax(diag)
        f = B[:, ref] / np.sqrt(diag[ref])
        # f should be positive; clip tiny negatives
        f = np.maximum(f, 1e-15)
        
        # evaluate Heff on 30 equidistant points
        x_eval = np.linspace(-1.0, 1.0, 30)
        # cubic spline interpolation
        spl = scipy.interpolate.CubicSpline(x, f, bc_type='natural')
        f_eval = spl(x_eval)
        f_eval = np.maximum(f_eval, 1e-15)
        Heff = -f_hat - 2.0 * np.log(f_eval)
        
        # parabolic fit
        coeff = np.polyfit(x_eval, Heff, 2)
        a, b, c = coeff
        residual = Heff - (a * x_eval**2 + b * x_eval + c)
        chi = np.sqrt((1.0 / 27.0) * np.sum(residual**2))
        chi_dict[key + '_chi_max'] = chi
    
    # write free_energy_results.csv
    with open('/app/outputs/free_energy_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['K', 'k', 'free_energy_per_spin'])
        for K, k, val in free_energies:
            writer.writerow([K, k, val])
    
    # write chi_max_results.json
    with open('/app/outputs/chi_max_results.json', 'w') as f:
        json.dump(chi_dict, f, indent=2)

if __name__ == '__main__':
    main()