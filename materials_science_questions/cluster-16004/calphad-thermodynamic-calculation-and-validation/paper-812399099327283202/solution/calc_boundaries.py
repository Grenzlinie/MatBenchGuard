#!/usr/bin/env python3
"""Compute Fe-Cu-Ni fcc/liquid phase boundaries using pycalphad.

Hardcodes the Redlich-Kister coefficients (Table 1), ternary interaction
terms, and lattice stabilities (Table 2) from the paper.  Scans a fine
grid of overall compositions at each temperature, performs equilibrium
calculations, records the compositions of coexisting fcc and liquid phases
within the two-phase region, and writes a CSV with columns:
  temperature, phase, x_Cu, x_Fe, x_Ni
"""

import sys
import csv
import numpy as np
from pycalphad import Database, equilibrium, variables as v

# ----------------------------------------------------------------------
# 1. Thermodynamic parameters (exactly from the paper)
# ----------------------------------------------------------------------
# The TDB string below defines:
#   - elements CU, FE, NI, VA
#   - phases FCC_A1 (disordered), LIQUID
#   - pure element lattice stabilities (GHSER for fcc, and GLIQ for liquid)
#   - binary excess parameters (Redlich-Kister) for Cu-Ni, Fe-Ni, Cu-Fe
#   - ternary interaction terms (fcc and liq)
#
# NOTE: The paper gives excess coefficients for fcc and liq as temperature-
# dependent a+b*T.  In TDB syntax we use the form:
#   PARAMETER G(PHASE,COMPONENT;0) 298.15 a + b*T; 6000 N !
# where the reference state for excess mixing is the Redlich-Kister polynomial.
# We preserve the exact numeric values from the paper.
#
# Lattice stabilities: ΔG(fcc→liq) = a + b*T + c*T^2 + d*T*ln(T)
# Therefore GLIQ = GFCC + ΔG.  In the database we set GFCC = GHSER (standard
# SGTE reference) and GLIQ = GHSER + ΔG.  The difference between the liquid and
# fcc phases is exactly the paper's lattice stability expressions.
#
# This TDB is self-contained and does not rely on any external files.

tdb_string = """
ELEMENT CU   BLANK  0  0  0  !
ELEMENT FE   BLANK  0  0  0  !
ELEMENT NI   BLANK  0  0  0  !
ELEMENT VA   BLANK  0  0  0  !

TYPE_DEFINITION % SEQ * !

FUNCTION GHSERCU 298.15
    +13054.1 -9.6232*T +4.1756e-3*T*T +22.03*T*LN(T);
  6000 N !

FUNCTION GHSERFE 298.15
    -11274.0 +163.878*T +4.1756e-3*T*T +22.03*T*LN(T);
  6000 N !

FUNCTION GHSERNI 298.15
    +17614.6 -10.209*T +4.1756e-3*T*T +22.03*T*LN(T);
  6000 N !

FUNCTION GHSERS 298.15
  0; 6000 N !

PHASE FCC_A1 % 1 1  !
   CONSTITUENT FCC_A1 : CU,FE,NI : VA% :  !

PHASE LIQUID % 1 1  !
   CONSTITUENT LIQUID : CU,FE,NI :  !

! ------------------------------------------------------------
! Pure element Gibbs energies: FCC_A1 uses GHSERxx - difference
! so that the lattice stabilities come from the ΔG expressions.
! We set GFCC = 0 for all elements (relative reference) and
! GLIQ = ΔG.  The actual absolute values cancel when computing
! phase equilibria because only differences matter.  This trick
! avoids the need for real SGTE baselines while keeping the
! paper's exact lattice stabilities.
! ------------------------------------------------------------

PARAMETER G(FCC_A1,CU:VA;0) 298.15 0; 6000 N !
PARAMETER G(FCC_A1,FE:VA;0) 298.15 0; 6000 N !
PARAMETER G(FCC_A1,NI:VA;0) 298.15 0; 6000 N !

PARAMETER G(LIQUID,CU:VA;0) 298.15  GHSERCU#; 6000 N !
PARAMETER G(LIQUID,FE:VA;0) 298.15  GHSERFE#; 6000 N !
PARAMETER G(LIQUID,NI:VA;0) 298.15  GHSERNI#; 6000 N !

! ------------------------------------------------------------
! Excess mixing parameters (Redlich–Kister).
! Format: PARAMETER G(PHASE,COMPONENT1,COMPONENT2;v) 298.15 a + b*T; 6000 N !
! ------------------------------------------------------------

! Cu-Ni fcc
PARAMETER G(FCC_A1,CU,NI:VA;0) 298.15  9534.49 + 2.83903*T; 6000 N !
PARAMETER G(FCC_A1,CU,NI:VA;1) 298.15  424.255 - 0.62595*T; 6000 N !
PARAMETER G(FCC_A1,CU,NI:VA;2) 298.15  -1812.93 + 2.12233*T; 6000 N !

! Cu-Ni liquid
PARAMETER G(LIQUID,CU,NI;0) 298.15  32238.7 - 11.1093*T; 6000 N !
PARAMETER G(LIQUID,CU,NI;1) 298.15  -619.65 - 1.08812*T; 6000 N !
PARAMETER G(LIQUID,CU,NI;2) 298.15  -213.489 + 0.97309*T; 6000 N !

! Fe-Ni fcc
PARAMETER G(FCC_A1,FE,NI:VA;0) 298.15  -18298.8 + 5.14894*T; 6000 N !
PARAMETER G(FCC_A1,FE,NI:VA;1) 298.15  14313.6 - 7.65979*T; 6000 N !

! Fe-Ni liquid
PARAMETER G(LIQUID,FE,NI;0) 298.15  -20292.4 + 5.14137*T; 6000 N !
PARAMETER G(LIQUID,FE,NI;1) 298.15  11924.4 - 6.16329*T; 6000 N !

! Cu-Fe fcc
PARAMETER G(FCC_A1,CU,FE:VA;0) 298.15  48206.0 - 8.44645*T; 6000 N !
PARAMETER G(FCC_A1,CU,FE:VA;1) 298.15  -5918.0 + 5.01725*T; 6000 N !

! Cu-Fe liquid
PARAMETER G(LIQUID,CU,FE;0) 298.15  34321.3 - 1.8577*T; 6000 N !
PARAMETER G(LIQUID,CU,FE;1) 298.15  -1811.6 + 1.6401*T; 6000 N !
PARAMETER G(LIQUID,CU,FE;2) 298.15  7564.6 - 2.5857*T; 6000 N !
PARAMETER G(LIQUID,CU,FE;3) 298.15  -2418.3 + 2.3472*T; 6000 N !

! Ternary interaction parameters
! fcc: A = -35982, B = -12.0  ;  liq: A = -45000, B = 0
PARAMETER G(FCC_A1,CU,FE,NI:VA;0) 298.15  -35982 - 12.0*T; 6000 N !
PARAMETER G(LIQUID,CU,FE,NI;0) 298.15  -45000; 6000 N !
"""

# ----------------------------------------------------------------------
# 2. Build the pycalphad Database
# ----------------------------------------------------------------------
db = Database.from_string(tdb_string, fmt='tdb')

# ----------------------------------------------------------------------
# 3. Temperatures to sample (in Kelvin)
# ----------------------------------------------------------------------
temperatures = [1373, 1423, 1473, 1523, 1573, 1623, 1673]

# ----------------------------------------------------------------------
# 4. Composition grid (overall mole fractions)
# ----------------------------------------------------------------------
grid_points = 101  # 0.01 spacing
x_cu_vals = np.linspace(0, 1, grid_points)
x_ni_vals = np.linspace(0, 1, grid_points)

def is_valid(x_cu, x_ni):
    x_fe = 1.0 - x_cu - x_ni
    return x_fe >= -1e-9 and x_fe <= 1.0001

# ----------------------------------------------------------------------
# 5. Function to run equilibrium and extract two-phase tie-line ends
# ----------------------------------------------------------------------
def get_phase_compositions(temp, x_cu, x_ni):
    """Return (fcc_comps, liq_comps) or empty dicts if single phase."""
    try:
        result = equilibrium(db, ['CU', 'FE', 'NI', 'VA'],
                             ['FCC_A1', 'LIQUID'],
                             {v.T: temp, v.P: 101325,
                              v.X('CU'): x_cu, v.X('NI'): x_ni},
                             output='GM')
    except Exception:
        return {}, {}  # numerical issue, skip
    # Identify phases present
    # result.GM has coordinates: (phase, component, ...)
    # We check the phase names and their fractions
    phases = result.Phase.values.flatten()
    phase_fractions = result.NP.values.squeeze()  # shape (n_phases,) ?
    # If only one phase present, skip
    if len(phases) < 2 or np.all(phase_fractions < 1e-6):
        return {}, {}
    # Mole fractions are stored in X
    # X has dimensions: (N_P, T, points, components)
    # We have single point so we can squeeze
    X_data = result.X.squeeze()  # shape (n_phases, n_components)
    compts = result.component.values.flatten()
    # Build dicts for fcc and liq
    fcc_comps = {}
    liq_comps = {}
    for phase, frac, comp_vec in zip(phases, phase_fractions, X_data):
        if frac < 1e-6:
            continue
        comp_dict = {c: val for c, val in zip(compts, comp_vec)}
        if phase == 'FCC_A1':
            fcc_comps = comp_dict
        elif phase == 'LIQUID':
            liq_comps = comp_dict
    # If both phases present, return both; otherwise empty
    if fcc_comps and liq_comps:
        return fcc_comps, liq_comps
    else:
        return {}, {}

# ----------------------------------------------------------------------
# 6. Main collection loop
# ----------------------------------------------------------------------
output_rows = []
# We'll use a deduplication set to avoid near-duplicate points
seen = set()

tol = 1e-3

for T in temperatures:
    print(f"Processing T={T} K...", file=sys.stderr)
    for x_cu in x_cu_vals:
        for x_ni in x_ni_vals:
            if not is_valid(x_cu, x_ni):
                continue
            fcc, liq = get_phase_compositions(T, x_cu, x_ni)
            # If we got compositions for both phases, record them
            if fcc and liq:
                # fcc
                cu_f = round(fcc['CU'], 8)
                fe_f = round(fcc['FE'], 8)
                ni_f = round(fcc['NI'], 8)
                key_f = (T, 'fcc', cu_f, fe_f, ni_f)
                if key_f not in seen:
                    seen.add(key_f)
                    output_rows.append([T, 'fcc', cu_f, fe_f, ni_f])
                # liq
                cu_l = round(liq['CU'], 8)
                fe_l = round(liq['FE'], 8)
                ni_l = round(liq['NI'], 8)
                key_l = (T, 'liq', cu_l, fe_l, ni_l)
                if key_l not in seen:
                    seen.add(key_l)
                    output_rows.append([T, 'liq', cu_l, fe_l, ni_l])

print(f"Total unique points collected: {len(output_rows)}", file=sys.stderr)

# ----------------------------------------------------------------------
# 7. Write CSV
# ----------------------------------------------------------------------
outfile = sys.argv[1]
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'phase', 'x_Cu', 'x_Fe', 'x_Ni'])
    for row in output_rows:
        writer.writerow(row)

print(f"Phase boundaries written to {outfile}", file=sys.stderr)
