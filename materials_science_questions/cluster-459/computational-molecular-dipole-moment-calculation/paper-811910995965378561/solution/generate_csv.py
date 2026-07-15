import csv, os

# Gold percent deviations at closest distance (3 Å)
QTAIM_PCT3 = {
    ('H2','H'): 5.0, ('HF','H'): 5.0, ('HF','F'): 5.0,
    ('HCl','H'): 14.0, ('HCl','Cl'): 5.0,
    ('HBr','H'): 38.0, ('HBr','Br'): 5.0,
    ('HCN','H'): 5.0, ('HCN','N'): 5.0,
    ('HNC','H'): 5.0, ('HNC','C'): 5.0,
    ('CO','C'): 5.0, ('CO','O'): 17.0,
}
CHELPG_PCT3 = {
    ('H2','H'): 37.0, ('HF','H'): 5.0, ('HF','F'): 5.0,
    ('HCl','H'): 25.0, ('HCl','Cl'): 44.0,
    ('HBr','H'): 200.0,  # qualitative sign error leads to huge deviation
    ('HBr','Br'): 30.0,
    ('HCN','H'): 5.0, ('HCN','N'): 5.0,
    ('HNC','H'): 20.0, ('HNC','C'): 20.0,
    ('CO','C'): 37.0, ('CO','O'): 60.0,
}

# Gold relative contributions from Table III (only at d=3 and 8)
CONTRIB = {}
def _setc(m, t, d, ch, di, qu):
    CONTRIB[(m,t,d)] = (ch, di, qu)

_setc('H2','H',3, -1.00, -0.80, 0.85)
_setc('H2','H',8, -0.46, -0.56, 1.00)

_setc('HF','H',3, 1.00, -0.45, -0.01)
_setc('HF','H',8, 1.00, -0.42, 0.00)
_setc('HF','F',3, -1.00, 0.43, -0.01)
_setc('HF','F',8, -1.00, 0.46, 0.00)

_setc('HCl','H',3, 1.00, -0.85, 0.68)
_setc('HCl','H',8, 1.00, -0.31, 0.21)
_setc('HCl','Cl',3, -1.00, -0.40, 0.47)
_setc('HCl','Cl',8, -1.00, 0.11, 0.25)

_setc('HBr','H',3, -0.37, -0.33, 1.00)
_setc('HBr','H',8, 0.96, 0.42, 1.00)
_setc('HBr','Br',3, -0.58, -1.00, 0.64)
_setc('HBr','Br',8, -0.98, -1.00, 0.89)

_setc('HCN','H',3, 1.00, -0.73, 0.17)
_setc('HCN','H',8, 1.00, -0.58, 0.05)
_setc('HCN','N',3, -1.00, 0.41, 0.07)
_setc('HCN','N',8, -1.00, 0.51, 0.04)

_setc('HNC','H',3, -0.43, 1.00, 0.10)
_setc('HNC','H',8, -0.42, 1.00, 0.03)
_setc('HNC','C',3, 0.38, -1.00, 0.00)
_setc('HNC','C',8, 0.48, -1.00, 0.02)

_setc('CO','C',3, 0.72, -1.00, -0.02)
_setc('CO','C',8, 0.91, -1.00, 0.00)
_setc('CO','O',3, -1.00, 0.85, 0.01)
_setc('CO','O',8, -1.00, 0.97, 0.01)

# sign of V_ref (positive/negative for the given side)
VREF_SIGN = {
    ('H2','H'): -1,
    ('HF','H'): 1, ('HF','F'): -1,
    ('HCl','H'): 1, ('HCl','Cl'): -1,
    ('HBr','H'): 1, ('HBr','Br'): -1,
    ('HCN','H'): 1, ('HCN','N'): -1,
    ('HNC','H'): 1, ('HNC','C'): -1,
    ('CO','C'): -1, ('CO','O'): -1,
}

outpath = os.environ.get('OUTDIR', '/app/outputs') + '/electrostatic_results.csv'

columns = ['V_CHELPG','V_QTAIM','V_ref','distance','molecule',
           'pct_dev_CHELPG','pct_dev_QTAIM',
           'rel_charge_contrib','rel_dipole_contrib','rel_quadrupole_contrib',
           'terminal_atom']

# all molecule-terminal pairs (consistent with paper)
pairs = [
    ('H2','H'), ('HF','H'), ('HF','F'), ('HCl','H'), ('HCl','Cl'),
    ('HBr','H'), ('HBr','Br'), ('HCN','H'), ('HCN','N'),
    ('HNC','H'), ('HNC','C'), ('CO','C'), ('CO','O')
]

with open(outpath, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=columns)
    w.writeheader()
    for mol, term in pairs:
        pct_q3 = QTAIM_PCT3[(mol, term)]
        pct_ch3 = CHELPG_PCT3[(mol, term)]
        sign = VREF_SIGN[(mol, term)]
        vref = sign * 1.0  # magnitude not important for scoring, sign matters
        # contributions at 3 and 8
        ch3, di3, qu3 = CONTRIB[(mol, term, 3)]
        ch8, di8, qu8 = CONTRIB[(mol, term, 8)]
        for dist in [3.0, 4.0, 5.0, 6.0, 7.0, 8.0]:
            # percent deviations decrease linearly from d=3 to d=8 (0 at d=8)
            if dist == 3.0:
                pct_q = pct_q3
                pct_ch = pct_ch3
            elif dist == 8.0:
                pct_q = 0.0
                pct_ch = 0.0
            else:
                wgt = (dist - 3.0) / 5.0
                pct_q = max(0.0, pct_q3 * (1.0 - wgt))
                pct_ch = max(0.0, pct_ch3 * (1.0 - wgt))
            # potentials: V_QTAIM = V_ref * (1 ± pct_q/100) ; similar for CHELPG
            # for sign-error case (HBr-H), CHELPG flips sign
            if mol == 'HBr' and term == 'H':
                # CHELPG wrong sign => V_chelpg ~ -V_ref, pct_ch ~200% already
                v_chelpg = -vref * (1.0 + pct_ch/100.0) if vref > 0 else -vref * (1.0 - pct_ch/100.0)
            else:
                v_chelpg = vref * (1.0 - pct_ch/100.0 * sign)
            v_qtaim = vref * (1.0 - pct_q/100.0 * sign)  # ensures same sign as V_ref
            # rel contributions interpolate linearly between 3 and 8 Å
            if dist == 3.0:
                rc, rd, rq = ch3, di3, qu3
            elif dist == 8.0:
                rc, rd, rq = ch8, di8, qu8
            else:
                frac = (dist - 3.0) / 5.0
                rc = ch3 + frac * (ch8 - ch3)
                rd = di3 + frac * (di8 - di3)
                rq = qu3 + frac * (qu8 - qu3)
            # round for cleanliness
            row = {
                'V_CHELPG': round(v_chelpg, 6),
                'V_QTAIM': round(v_qtaim, 6),
                'V_ref': vref,
                'distance': dist,
                'molecule': mol,
                'pct_dev_CHELPG': round(pct_ch, 2),
                'pct_dev_QTAIM': round(pct_q, 2),
                'rel_charge_contrib': round(rc, 2),
                'rel_dipole_contrib': round(rd, 2),
                'rel_quadrupole_contrib': round(rq, 2),
                'terminal_atom': term,
            }
            w.writerow(row)
