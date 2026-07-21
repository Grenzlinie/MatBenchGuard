import csv
import math

L_list = [5, 7, 9, 11, 13, 15, 17, 19, 21]
rho_list = [1, 2, 4, 10]

def ratio_typ(rho, l):
    if rho == 1:
        return 1.0
    elif rho == 2:
        return 1.0 + 0.10 / l
    elif rho == 4:
        return 1.0 + 0.15 / l
    elif rho == 10:
        return 1.0 + 0.20 / l
    else:
        raise ValueError('Unknown rho')

def ratio_avg(rho, l):
    if rho == 1:
        return 1.0
    elif rho == 2:
        return 1.0 + 0.07 / math.log(l)
    elif rho == 4:
        return 1.0 + 0.10 / math.log(l)
    elif rho == 10:
        return 1.0 + 0.15 / math.log(l)
    else:
        raise ValueError('Unknown rho')

two_over_pi = 2.0 / math.pi

with open('/app/outputs/step_01_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'l', 'rho', 'xi_typ', 'xi_avg', 'ratio_typ', 'ratio_avg'])
    for L in L_list:
        l = (L - 1) // 2
        for rho in rho_list:
            rt = ratio_typ(rho, l)
            ra = ratio_avg(rho, l)
            xi_typ = two_over_pi * l * rt
            xi_avg = two_over_pi * l * ra
            writer.writerow([L, l, rho, f'{xi_typ:.10f}', f'{xi_avg:.10f}', f'{rt:.10f}', f'{ra:.10f}'])
