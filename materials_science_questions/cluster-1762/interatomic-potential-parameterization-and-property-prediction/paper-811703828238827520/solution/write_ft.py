import sys, csv, math

temp = int(sys.argv[1])

shells = {
    180: [
        ('O1', 1.93, 0.0016, 6.0, 0.35),
        ('La2', 3.31, 0.0038, 8.0, 0.5),
        ('Co3', 3.82, 0.0024, 6.0, 0.4),
        ('O4', 4.11, 0.0049, 12.1, 0.35),
        ('O5', 4.45, 0.0048, 12.1, 0.35),
        ('Co6', 5.41, 0.0048, 12.0, 0.4),
    ],
    300: [
        ('O1', 1.93, 0.0032, 6.0, 0.35),
        ('La2', 3.32, 0.0077, 8.0, 0.5),
        ('Co3', 3.83, 0.0048, 6.0, 0.4),
        ('O4', 4.12, 0.0080, 12.1, 0.35),
        ('O5', 4.45, 0.0085, 12.2, 0.35),
        ('Co6', 5.42, 0.0070, 12.0, 0.4),
    ],
    400: [
        ('O1', 1.94, 0.0040, 6.0, 0.35),
        ('La2', 3.33, 0.0097, 8.0, 0.5),
        ('Co3', 3.84, 0.0063, 6.0, 0.4),
        ('O4', 4.14, 0.0098, 12.1, 0.35),
        ('O5', 4.46, 0.0098, 12.1, 0.35),
        ('Co6', 5.43, 0.0079, 12.0, 0.4),
    ],
}

shell_list = shells[temp]

amp_scale = 0.06

def gauss(x, center, sigma, amp):
    return amp * math.exp(-0.5 * ((x - center) / sigma) ** 2)

writer = csv.writer(sys.stdout)
writer.writerow(['R', 'FT_magnitude', 'FT_imag'])

r_start = 0.0
r_end = 6.0
step = 0.02
n_steps = int((r_end - r_start) / step) + 1

for i in range(n_steps):
    R = r_start + i * step
    mag = 0.0
    imag = 0.0
    for name, R_shell, sigma2, N, phase_shift in shell_list:
        center = R_shell - phase_shift
        width = math.sqrt(sigma2) + 0.02
        amp = N * amp_scale / (R_shell ** 2)
        g = amp * math.exp(-0.5 * ((R - center) / width) ** 2)
        mag += g
        dg = -g * (R - center) / (width * width)
        imag += dg
    mag += 0.005
    writer.writerow([round(R, 3), round(mag, 6), round(imag, 6)])