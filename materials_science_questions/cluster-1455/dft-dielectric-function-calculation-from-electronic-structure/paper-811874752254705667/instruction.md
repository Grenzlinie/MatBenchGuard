# DFT-derived electronic structure and optical dielectric function of CaBi2Ta2O9

## Problem background
Aurivillius-phase ferroelectric oxides such as CaBi₂Ta₂O₉ are promising candidates for non‑volatile memory devices. Understanding their electronic structure, orbital hybridization, and optical properties is essential to rationalising ferroelectricity and optical performance. This task targets a first-principles computational investigation of the indirect band gap, the orbital-resolved density of states that reveals metal–oxygen hybridization, and the frequency‑dependent dielectric function of CaBi₂Ta₂O₉.

## Approach
Perform density‑functional theory (DFT) calculations using an open‑source all‑electron or pseudopotential DFT code (e.g., Elk). Use the generalised gradient approximation (GGA) for the exchange–correlation functional, consistent with the original study. Start from the experimental crystal structure, then relax atomic positions and cell volume to obtain the equilibrium structure. From the converged charge density, compute the band structure to extract the indirect band gap, compute atom‑ and angular‑momentum‑projected densities of states to identify orbital hybridization features, and compute the frequency‑dependent imaginary dielectric function for the three Cartesian directions and the average over photon energies from 0 to 13 eV.

## Reproduction target
The goal is to compute the following quantities:

1. The indirect band gap (in eV) of the compound.
2. Key features of the partial density of states that characterise the Bi–O and Ta–O orbital hybridization: the energy location of the low‑lying Bi–O band, the valence‑band range, the conduction‑band hybridization window, and whether Ta–O hybridization is present at the band edges.
3. The imaginary part of the dielectric function ε₂(ω) as a function of photon energy from 0 to 13 eV. Provide the xx, yy, zz components and the average, capturing the expected variation from nearly isotropic response at low energies to anisotropic response at higher energies.

## Assets

- Elk (all-electron FPLAPW DFT code): https://elk.sourceforge.io/

## Workflow steps

### Step 1: Structure setup
- Role: process
- Action: Construct the orthorhombic unit cell of CaBi2Ta2O9 in space group A21am using the experimental lattice parameters a=5.4625 Å, b=5.4286 Å, c=24.945 Å and the fractional atomic coordinates: Ca (0, 0.2484, 0), Bi (0.4865, 0.7749, 0.19894), Ta (0.5285, 0.751, 0.4168), O1 (0.5575, 0.3175, 0), O2 (0.5299, 0.68, 0.3443), O3 (0.7535, 0.9952, 0.25025), O4 (0.7555, 0.9638, 0.06389), O5 (0.8423, 0.949, 0.58578).
- Evidence: `/app/outputs/crystal_structure.cif`

### Step 2: Geometry optimisation
- Role: process
- Action: Relax atomic positions and cell volume using DFT to obtain the equilibrium structure. Compute the total energy vs. volume curve to confirm the minimum.
- Evidence: `/app/outputs/geometry_optimisation.log`

### Step 3: Self-consistent field calculation
- Role: process
- Action: Perform a self-consistent DFT calculation on the optimized geometry to obtain converged charge density and Kohn-Sham eigenvalues. Use a generalized gradient approximation (GGA) exchange-correlation functional.
- Evidence: `/app/outputs/scf.log`

### Step 4: Band gap extraction
- Role: scored
- Action: Compute the band structure along high-symmetry directions and determine the indirect band gap (difference between valence band maximum and conduction band minimum at different k‑points). Write the gap value to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"indirect_band_gap_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Partial DOS analysis
- Role: scored
- Action: Compute atom- and angular-momentum-projected densities of states (PDOS) from the SCF calculation. Identify the energy location of the low-lying Bi–O band, the valence-band range dominated by Bi 6p, Ta 5d and O 2p, the conduction-band window where strong Bi 6p–O 2p hybridization occurs, and the presence of Ta 5d–O 2p hybridization at the valence-band top/conduction-band bottom. Write these features to pdos_features.json.
- Output file: `/app/outputs/pdos_features.json`
- Format: json
- Contract: {"low_band_peak_eV": float, "valence_band_min_eV": float, "valence_band_max_eV": float, "conduction_hybrid_min_eV": float, "conduction_hybrid_max_eV": float, "ta_o_hybridization": bool}
- Scoring: scored by hidden verifier

### Step 6: Imaginary dielectric function
- Role: scored (load-bearing)
- Action: Compute the frequency‑dependent imaginary part of the dielectric function ε₂(ω) from the SCF eigenvalues and dipole matrix elements. Produce the xx, yy, zz components and the average for photon energies 0–13 eV with a step no larger than 0.1 eV. Save as CSV.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: CSV with columns: energy_eV (float), epsilon2_avg (float), epsilon2_xx (float), epsilon2_yy (float), epsilon2_zz (float). Energy range 0-13 eV, step ≤0.1 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/pdos_features.json`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed indirect band gap of CaBi2Ta2O9.
- schema:
  - `type`: object
  - `required`:
    - `indirect_band_gap_eV`: float (eV)

### pdos_features.json
- path: `/app/outputs/pdos_features.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Extracted features from the partial density of states that verify orbital hybridization patterns.
- schema:
  - `type`: object
  - `required`:
    - `low_band_peak_eV`: float (eV)
    - `valence_band_min_eV`: float (eV)
    - `valence_band_max_eV`: float (eV)
    - `conduction_hybrid_min_eV`: float (eV)
    - `conduction_hybrid_max_eV`: float (eV)
    - `ta_o_hybridization`: bool

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Imaginary dielectric function components for photon energies 0-13 eV. The checker will recompute peak positions and anisotropy metrics.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `epsilon2_avg`, `epsilon2_xx`, `epsilon2_yy`, `epsilon2_zz`
  - `units`:
    - `energy_eV`: eV
    - `epsilon2_avg`: dimensionless
    - `epsilon2_xx`: dimensionless
    - `epsilon2_yy`: dimensionless
    - `epsilon2_zz`: dimensionless

Notes: The original study used Wien2k; this task is scoped to open-source DFT codes. Tolerances are chosen to absorb method/code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "indirect_band_gap_eV": "float (eV)"
        }
      },
      "description": "Computed indirect band gap of CaBi2Ta2O9."
    },
    {
      "file": "pdos_features.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "low_band_peak_eV": "float (eV)",
          "valence_band_min_eV": "float (eV)",
          "valence_band_max_eV": "float (eV)",
          "conduction_hybrid_min_eV": "float (eV)",
          "conduction_hybrid_max_eV": "float (eV)",
          "ta_o_hybridization": "bool"
        }
      },
      "description": "Extracted features from the partial density of states that verify orbital hybridization patterns."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "epsilon2_avg",
          "epsilon2_xx",
          "epsilon2_yy",
          "epsilon2_zz"
        ],
        "units": {
          "energy_eV": "eV",
          "epsilon2_avg": "dimensionless",
          "epsilon2_xx": "dimensionless",
          "epsilon2_yy": "dimensionless",
          "epsilon2_zz": "dimensionless"
        }
      },
      "description": "Imaginary dielectric function components for photon energies 0-13 eV. The checker will recompute peak positions and anisotropy metrics."
    }
  ],
  "notes": "The original study used Wien2k; this task is scoped to open-source DFT codes. Tolerances are chosen to absorb method/code differences."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file. For the band gap, the verifier compares your reported value against a hidden reference. For the PDOS features, the verifier checks that the reported energy ranges and hybridization flag are structurally consistent with expected orbital character. For the dielectric function, the verifier recomputes peak positions and anisotropy metrics from your CSV data and compares them to reference behaviour. Each artifact contributes a weighted share to a final reward between 0 and 1. Simply reporting expected numbers is not enough; you must produce the requested data files by executing the workflow.
