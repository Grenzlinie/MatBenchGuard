import math
import csv

R = 8.31434

def calc_Wg(Wh, Ws, Wv, T_C):
    return Wh - (T_C + 273.15) * Ws + 1000.0 * Wv

def calc_Ge(X1, X2, X3, W23, W32, W31, W13, W21, W12, W123):
    Tmp = X3 * X2 * (0.5 - X1)
    Ge = W123 * (X2 * X3 * (1.0 - 2*X1))
    Ge += W23 * (X3 * X2 * (0.5 - X1 - 2*X3))
    Ge += W32 * (X3 * X2 * (0.5 - X1 - 2*X2))
    Ge += W31 * (2.0 * X3 * X1 * (1.0 - X1) + Tmp)
    Ge += W21 * (2.0 * X2 * X1 * (1.0 - X1) + Tmp)
    Ge += W13 * (X3 * X3 * (1.0 - 2.0 * X1) + Tmp)
    Ge += W12 * (X2 * X2 * (1.0 - 2.0 * X1) + Tmp)
    return Ge

def gibbs(Xor, Xab, T_C):
    Xan = 1.0 - Xor - Xab
    if Xor < 0.0 or Xor > 1.0 or Xab < 0.0 or Xab > 1.0 or Xan < 0.0 or Xan > 1.0:
        return float('inf')
    rt = R * (T_C + 273.15)
    # Margules parameters from Elkins & Grove (1990) Table 4
    Wabor   = calc_Wg(18810.0, 10.3,  0.4602, T_C)
    Worab   = calc_Wg(27320.0, 10.3,  0.3264, T_C)
    Waban   = calc_Wg( 7924.0,  0.0,  0.0, T_C)
    Wanab   = calc_Wg(    0.0,  0.0,  0.0, T_C)
    Woran   = calc_Wg(40317.0,  0.0,  0.0, T_C)
    Wanor   = calc_Wg(38974.0,  0.0, -0.1037, T_C)
    Waboran = calc_Wg(12545.0,  0.0, -1.095, T_C)
    # Ideal mixing terms
    Lan = 0.0 if Xan == 0.0 else Xan * math.log(Xan)
    Lab = 0.0 if Xab == 0.0 else Xab * math.log(Xab)
    Lor = 0.0 if Xor == 0.0 else Xor * math.log(Xor)
    # Excess terms
    Ge_an = calc_Ge(Xan, Xor, Xab, Worab, Wabor, Waban, Wanab, Woran, Wanor, Waboran)
    Ge_ab = calc_Ge(Xab, Xan, Xor, Wanor, Woran, Worab, Wabor, Wanab, Waban, Waboran)
    Ge_or = calc_Ge(Xor, Xab, Xan, Waban, Wanab, Wanor, Woran, Wabor, Worab, Waboran)
    g = rt * (Lab + Lan + Lor) + Xab * Ge_ab + Xan * Ge_an + Xor * Ge_or
    return g

def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def binary_search(xa, ya, xb, yb, T, stp, tst1=1e-3, max_inner=30):
    """Binary search along the tie-line: adjust xa and xb alternately while keeping midpoint fixed."""
    xo = (xa + xb) / 2.0
    yo = (ya + yb) / 2.0
    for _ in range(max_inner):
        xa_old, ya_old = xa, ya
        xb_old, yb_old = xb, yb

        # distances from midpoint
        da = dist(xa, ya, xo, yo)
        db = dist(xb, yb, xo, yo)
        if da < 1e-12 or db < 1e-12:
            break

        # ----- search for xa along direction from midpoint toward a -----
        ux = (xa - xo) / da
        uy = (ya - yo) / da

        ga = gibbs(xa, ya, T)
        gb = gibbs(xb, yb, T)

        def G0_a(da_val):
            x = xo + ux * da_val
            y = yo + uy * da_val
            g = gibbs(x, y, T)
            fa = db / (da_val + db)
            fb = da_val / (da_val + db)
            return fa * g + fb * gb, x, y, g

        best_g, best_x, best_y, best_ga = G0_a(da)
        best_da = da

        # Try increasing da (away from midpoint)
        for sign in (1, -1):
            da_try = da + sign * stp
            if da_try <= 0:
                continue
            g_try, x_try, y_try, ga_try = G0_a(da_try)
            if g_try < best_g:
                # descend in this direction
                da = da_try
                best_g, best_x, best_y, best_ga = g_try, x_try, y_try, ga_try
                best_da = da
                while True:
                    da += sign * stp
                    if da <= 0:
                        break
                    g_try, x_try, y_try, ga_try = G0_a(da)
                    if g_try >= best_g:
                        break
                    best_g, best_x, best_y, best_ga = g_try, x_try, y_try, ga_try
                    best_da = da
                break   # only first sign that improves is used

        xa, ya, ga = best_x, best_y, best_ga
        da = best_da

        # ----- search for xb along direction from midpoint toward b -----
        db = dist(xb, yb, xo, yo)
        vx = (xb - xo) / db
        vy = (yb - yo) / db

        def G0_b(db_val):
            x = xo + vx * db_val
            y = yo + vy * db_val
            g = gibbs(x, y, T)
            fa = db_val / (da + db_val)
            fb = da / (da + db_val)
            return fa * ga + fb * g, x, y, g

        best_g, best_x, best_y, best_gb = G0_b(db)
        best_db = db

        for sign in (1, -1):
            db_try = db + sign * stp
            if db_try <= 0:
                continue
            g_try, x_try, y_try, gb_try = G0_b(db_try)
            if g_try < best_g:
                db = db_try
                best_g, best_x, best_y, best_gb = g_try, x_try, y_try, gb_try
                best_db = db
                while True:
                    db += sign * stp
                    if db <= 0:
                        break
                    g_try, x_try, y_try, gb_try = G0_b(db)
                    if g_try >= best_g:
                        break
                    best_g, best_x, best_y, best_gb = g_try, x_try, y_try, gb_try
                    best_db = db
                break

        xb, yb, gb = best_x, best_y, best_gb

        # Check convergence of inner binary search
        if (abs(xa - xa_old) + abs(ya - ya_old) + abs(xb - xb_old) + abs(yb - yb_old)) < 4 * tst1:
            break
    return xa, ya, xb, yb

def perpendicular_search(xa, ya, xb, yb, T, stp):
    """Search perpendicular to the tie-line to lower G0 = 0.5*(Ga+Gb)."""
    xo = (xa + xb) / 2.0
    yo = (ya + yb) / 2.0
    dx = xb - xa
    dy = yb - ya
    len_tie = math.hypot(dx, dy)
    if len_tie < 1e-12:
        return xa, ya, xb, yb
    # unit perpendicular (dy, -dx)
    ux = dy / len_tie
    uy = -dx / len_tie

    ga = gibbs(xa, ya, T)
    gb = gibbs(xb, yb, T)
    best_g = (ga + gb) * 0.5
    best_xa, best_ya = xa, ya
    best_xb, best_yb = xb, yb

    for sign in (1, -1):
        xa_try = xa + sign * stp * ux
        ya_try = ya + sign * stp * uy
        xb_try = xb - sign * stp * ux
        yb_try = yb - sign * stp * uy
        ga_try = gibbs(xa_try, ya_try, T)
        gb_try = gibbs(xb_try, yb_try, T)
        g_try = (ga_try + gb_try) * 0.5
        if g_try < best_g:
            # descend in this direction
            xa, ya = xa_try, ya_try
            xb, yb = xb_try, yb_try
            best_g = g_try
            best_xa, best_ya = xa, ya
            best_xb, best_yb = xb, yb
            while True:
                xa += sign * stp * ux
                ya += sign * stp * uy
                xb -= sign * stp * ux
                yb -= sign * stp * uy
                ga = gibbs(xa, ya, T)
                gb = gibbs(xb, yb, T)
                g = (ga + gb) * 0.5
                if g >= best_g:
                    break
                best_g = g
                best_xa, best_ya = xa, ya
                best_xb, best_yb = xb, yb
            xa, ya = best_xa, best_ya
            xb, yb = best_xb, best_yb
            break  # only the first sign that improves
    return xa, ya, xb, yb

def solve_equilibrium(T_C, stp=5e-4, tst1=1e-3, tst2=1e-3, max_iter=300):
    # initial guess as given in the task
    xa, ya = 0.1, 0.8   # phase A: Xor=0.1, Xab=0.8
    xb, yb = 0.8, 0.1   # phase B: Xor=0.8, Xab=0.1
    for i in range(max_iter):
        xa_prev, ya_prev = xa, ya
        xb_prev, yb_prev = xb, yb

        # binary search along tie-line
        xa, ya, xb, yb = binary_search(xa, ya, xb, yb, T_C, stp, tst1)
        # perpendicular search
        xa, ya, xb, yb = perpendicular_search(xa, ya, xb, yb, T_C, stp)

        if (abs(xa - xa_prev) + abs(ya - ya_prev) + abs(xb - xb_prev) + abs(yb - yb_prev)) < 4 * tst2:
            break
    Xan_a = 1.0 - xa - ya
    Xan_b = 1.0 - xb - yb
    return (xa, ya, Xan_a), (xb, yb, Xan_b)

def main():
    temps = [700, 800, 900]
    with open('/app/outputs/equilibrium_pairs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'phase', 'Xor', 'Xab', 'Xan'])
        for T in temps:
            (Xor_a, Xab_a, Xan_a), (Xor_b, Xab_b, Xan_b) = solve_equilibrium(T)
            writer.writerow([T, 'A', f"{Xor_a:.6f}", f"{Xab_a:.6f}", f"{Xan_a:.6f}"])
            writer.writerow([T, 'B', f"{Xor_b:.6f}", f"{Xab_b:.6f}", f"{Xan_b:.6f}"])

if __name__ == '__main__':
    main()
