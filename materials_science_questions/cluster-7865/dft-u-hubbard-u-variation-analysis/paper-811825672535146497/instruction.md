# DFT Electronic Structure and Magnetic Properties of Sr3NiPtO6

## Problem background
Sr3NiPtO6 is a quasi-one-dimensional oxide whose crystal structure contains alternating face-sharing NiO6 trigonal prisms and PtO6 octahedra along the c-axis, with chains arranged on a triangular lattice in the ab-plane. Experiments find that it remains magnetically disordered down to 1.8 K, displaying spin‑liquid‑like behavior unlike analogous compounds that order. Electronic structure calculations can reveal the insulating character, the size of the magnetic moments, and the sign and strength of the intra‑chain magnetic coupling, which together help explain why long‑range order is absent.

## Approach
Perform density functional theory calculations using the generalized gradient approximation (Wu‑Cohen functional) within a full‑potential linearized augmented plane wave method. Starting from the experimental crystal structure, compute the total energies and magnetic properties for four distinct spin configurations: (1) non‑magnetic, (2) ferromagnetic with all Ni spins parallel, (3) antiferromagnetic with alternating Ni spins along the chain direction, and (4) ferromagnetic including spin‑orbit coupling on Ni and Pt. From the converged runs extract the down‑spin band gap, the spin magnetic moment on Ni, the total spin moment per formula unit, the energy difference between the antiferromagnetic and ferromagnetic solutions, the Heisenberg intra‑chain exchange coupling J (obtained by mapping the energy difference to a Heisenberg model with spin quantum number S = 1), and the orbital moments on Ni and Pt induced by spin‑orbit coupling.

## Reproduction target
Produce a single JSON file `results.json` containing the following numeric fields computed from the DFT runs:
- `band_gap`: the insulating gap in the down‑spin channel, in eV
- `Ni_spin_moment`: spin magnetic moment on Ni, in μB
- `total_spin_moment`: total spin moment per formula unit, in μB
- `FM_AFM_energy_diff`: E_AFM − E_FM, in meV per formula unit (positive when AFM is lower in energy)
- `exchange_J`: Heisenberg intra‑chain coupling constant in Kelvin, computed from J = (E_AFM − E_FM) / (3·S²) with S=1, using the conversion 1 meV = 11.6045 K
- `Ni_orbital_moment`: orbital magnetic moment on Ni from the SOC run, in μB
- `Pt_orbital_moment`: orbital magnetic moment on Pt from the SOC run, in μB
All values must be numbers; the units are those specified above.

## Assets

- Crystal structure of Sr3NiPtO6
- Elk full-potential LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Run all DFT calculations
- Role: process
- Action: Perform density functional theory (DFT) calculations for Sr3NiPtO6 using the Elk full-potential LAPW code (or another open-source FPLAPW code) with the Wu-Cohen GGA functional. Use the experimental crystal structure from Claridge et al. (1999). Run four separate configurations: (1) non-magnetic, (2) ferromagnetic (all Ni spins parallel), (3) antiferromagnetic (alternating Ni spins along the chain direction), and (4) ferromagnetic with spin-orbit coupling. For the SOC run, include spin-orbit coupling on both Ni and Pt. Retain all raw output files for subsequent extraction.
- Evidence: none

### Step 2: Extract scored properties
- Role: scored (load-bearing)
- Action: From the completed DFT runs, compute and write the following quantities into results.json: band_gap (the down-spin channel insulating gap, in eV); Ni_spin_moment (spin magnetic moment on Ni, in μB); total_spin_moment (total spin moment per formula unit, in μB); FM_AFM_energy_diff (E_AFM - E_FM, in meV per formula unit, positive if AFM lower); exchange_J (Heisenberg intra-chain coupling constant in Kelvin, derived from J = (E_AFM - E_FM) / (3*S^2) with S=1, using the conversion 1 meV = 11.6045 K); Ni_orbital_moment (orbital magnetic moment on Ni from SOC run, in μB); Pt_orbital_moment (orbital magnetic moment on Pt from SOC run, in μB). All values must be numeric, with the units as specified.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: band_gap (number, eV), Ni_spin_moment (number, μB), total_spin_moment (number, μB), FM_AFM_energy_diff (number, meV/f.u.), exchange_J (number, K), Ni_orbital_moment (number, μB), Pt_orbital_moment (number, μB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated electronic and magnetic properties derived from the DFT calculations. Checker compares each field to the paper-reported reference within a hidden tolerance; structural checks (AFM energy lower than FM, band gap positive, Ni spin moment > 1 μB) are also applied.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: number (eV)
    - `Ni_spin_moment`: number (μB)
    - `total_spin_moment`: number (μB)
    - `FM_AFM_energy_diff`: number (meV/f.u.)
    - `exchange_J`: number (K)
    - `Ni_orbital_moment`: number (μB)
    - `Pt_orbital_moment`: number (μB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `band_gap`: eV
    - `Ni_spin_moment`: μB
    - `total_spin_moment`: μB
    - `FM_AFM_energy_diff`: meV/f.u.
    - `exchange_J`: K
    - `Ni_orbital_moment`: μB
    - `Pt_orbital_moment`: μB

Notes: All quantities are from the GGA (Wu-Cohen) functional. The GGA+U robustness check and the derived paramagnetic moment are excluded per task scope. Tolerances are not disclosed here but are based on expected spread from using a different FPLAPW code (Elk vs WIEN2k).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "number (eV)",
          "Ni_spin_moment": "number (μB)",
          "total_spin_moment": "number (μB)",
          "FM_AFM_energy_diff": "number (meV/f.u.)",
          "exchange_J": "number (K)",
          "Ni_orbital_moment": "number (μB)",
          "Pt_orbital_moment": "number (μB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "band_gap": "eV",
          "Ni_spin_moment": "μB",
          "total_spin_moment": "μB",
          "FM_AFM_energy_diff": "meV/f.u.",
          "exchange_J": "K",
          "Ni_orbital_moment": "μB",
          "Pt_orbital_moment": "μB"
        }
      },
      "description": "Aggregated electronic and magnetic properties derived from the DFT calculations. Checker compares each field to the paper-reported reference within a hidden tolerance; structural checks (AFM energy lower than FM, band gap positive, Ni spin moment > 1 μB) are also applied."
    }
  ],
  "notes": "All quantities are from the GGA (Wu-Cohen) functional. The GGA+U robustness check and the derived paramagnetic moment are excluded per task scope. Tolerances are not disclosed here but are based on expected spread from using a different FPLAPW code (Elk vs WIEN2k)."
}
```

## How you are scored
After you submit `results.json`, a hidden verifier will compare each reported quantity against independently obtained reference values. For every numeric field, your value must fall within a hidden tolerance range. In addition to the numeric comparisons, the verifier checks several physical constraints: the antiferromagnetic configuration must have lower energy than the ferromagnetic one (FM_AFM_energy_diff > 0), the band gap must be positive (i.e., the system is insulating), and the Ni spin moment must exceed 1 μB. Each checked item contributes to the final score, which is the fraction of conditions satisfied. The tolerances and reference values are not revealed to you; you must compute the properties from first‑principles calculations to satisfy the checker.
