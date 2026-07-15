# DFT Projected Density of States and Orbital Analysis of Ferroelectric Crystal

## Problem background
Triglycine sulphate (TGS) is a ferroelectric crystal widely used in detection applications. Its electronic structure and optical properties are closely linked to the bonding character of its constituent glycine groups and sulphate anions. First-principles density functional theory (DFT) can provide the band dispersion, density of states, and frequency-dependent dielectric functions that shed light on the origin of the UV optical spectra. This task computes these properties for the ferroelectric phase of TGS.

## Approach
The calculation uses plane-wave DFT within the generalized gradient approximation (PBEsol functional) and ultrasoft pseudopotentials from the standard SSSP library. The workflow begins by optimizing the atomic positions and computing the ground-state charge density. From this ground state, four property runs are performed: a non-self-consistent band structure along the high-symmetry path Γ–Y–B–D–Γ, the total density of states, the projected density of states (by atomic and orbital contributions), and the frequency-dependent dielectric tensor. For the dielectric function, a scissor shift of 0.9 eV is applied to the conduction bands to bring the theoretical gap into better alignment with experimental measurements.

## Reproduction target
Produce the following four artifacts:

1. **band_structure.csv** – band energies (in eV) at each k‑point along the Γ–Y–B–D–Γ path.
2. **total_dos.csv** – total electronic density of states (states/eV) on a uniform energy grid.
3. **projected_dos.csv** – projected DOS by orbital (s, p) and by element (O, C, N, H, S), all in states/eV.
4. **dielectric_function.csv** – real (ε₁) and imaginary (ε₂) diagonal components of the dielectric tensor, with the 0.9 eV scissor shift applied.

The computed indirect band gap (derived from the band structure), the peak position of ε₂ in the 5–10 eV window, and the orbital character of the valence and conduction band edges (from the DOS files) will be evaluated against hidden reference criteria.

## Assets

- TGS crystal structure (CIF) – COD ID 1500693: https://www.crystallography.net/cod/1500693.cif
- Quantum ESPRESSO (or other open‑source plane‑wave DFT code): https://www.quantum-espresso.org/
- Pseudopotentials from SSSP library (PBEsol efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT geometry optimization and ground‑state calculation
- Role: process
- Action: Using the TGS crystal structure from COD, perform a full DFT geometry optimization (atomic positions and, if needed, cell parameters) with the PBEsol functional and a plane‑wave cutoff of ~340 eV. Then run a self‑consistent field (SCF) calculation to obtain the ground‑state charge density and wavefunctions. Save the final relaxed structure.
- Evidence: `/app/outputs/relaxed_geometry.cif`

### Step 2: Electronic band structure computation
- Role: scored
- Action: Using the relaxed geometry and ground‑state density, perform a non‑self‑consistent band structure calculation along the high‑symmetry path Γ–Y–B–D–Γ. Write the band energies at each k‑point to band_structure.csv.
- Output file: `/app/outputs/band_structure.csv`
- Format: csv
- Contract: CSV with columns: kpoint_label, kx, ky, kz, band_1, band_2, ..., band_n (one column per sorted energy band; energies in eV).
- Scoring: scored by hidden verifier

### Step 3: Total density of states computation
- Role: scored
- Action: Using the relaxed geometry and ground‑state charge density, compute the total electronic density of states (DOS) on a uniform energy grid and write it to total_dos.csv.
- Output file: `/app/outputs/total_dos.csv`
- Format: csv
- Contract: CSV with columns: energy (eV), total_dos (states/eV).
- Scoring: scored by hidden verifier

### Step 4: Projected density of states computation
- Role: scored
- Action: Using the same ground‑state calculation, compute the projected density of states by orbital (s, p) and by element (O, C, N, H, S) and save the result to projected_dos.csv.
- Output file: `/app/outputs/projected_dos.csv`
- Format: csv
- Contract: CSV with columns: energy (eV), s_dos, p_dos, O_dos, C_dos, N_dos, H_dos, S_dos (states/eV).
- Scoring: scored by hidden verifier

### Step 5: Dielectric function computation with scissor correction
- Role: scored (load-bearing)
- Action: Using the ground‑state wavefunctions, compute the frequency‑dependent dielectric tensor ε_ij(ω). Apply a scissor shift of 0.9 eV to the conduction bands. Write the real (ε1) and imaginary (ε2) diagonal components to dielectric_function.csv.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: CSV with columns: energy (eV), epsilon1_xx, epsilon1_yy, epsilon1_zz, epsilon2_xx, epsilon2_yy, epsilon2_zz (all dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.csv`
- `/app/outputs/total_dos.csv`
- `/app/outputs/projected_dos.csv`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.csv
- path: `/app/outputs/band_structure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band energies along the Γ–Y–B–D–Γ path. The checker recomputes the indirect band gap (VBM at Γ, CBM at D point) and compares it to a hidden reference value.
- schema:
  - `type`: table
  - `required_columns`: `kpoint_label`, `kx`, `ky`, `kz`
  - `additional_columns_pattern`: band_N (one column per sorted energy band, energies in eV)
  - `units`:
    - `kx`: reciprocal lattice units
    - `ky`: reciprocal lattice units
    - `kz`: reciprocal lattice units
    - `band_*`: eV

### total_dos.csv
- path: `/app/outputs/total_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total DOS. The checker verifies the presence of a band gap near the expected energy and the qualitative shape of the valence/conduction bands.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`
  - `units`:
    - `energy`: eV
    - `total_dos`: states/eV

### projected_dos.csv
- path: `/app/outputs/projected_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected DOS by orbital and element. The checker confirms that near the VBM the p‑character dominates (>80%) and that O and C contributions match the paper’s description.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `s_dos`, `p_dos`, `O_dos`, `C_dos`, `N_dos`, `H_dos`, `S_dos`
  - `units`:
    - `energy`: eV
    - `s_dos`: states/eV
    - `p_dos`: states/eV
    - `O_dos`: states/eV
    - `C_dos`: states/eV
    - `N_dos`: states/eV
    - `H_dos`: states/eV
    - `S_dos`: states/eV

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dielectric tensor after scissor shift (0.9 eV). The checker locates the peak of epsilon2_xx in the 5–10 eV window and compares its position to a hidden reference value.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `epsilon1_xx`, `epsilon1_yy`, `epsilon1_zz`, `epsilon2_xx`, `epsilon2_yy`, `epsilon2_zz`
  - `units`:
    - `energy`: eV
    - `epsilon1_xx`: dimensionless
    - `epsilon1_yy`: dimensionless
    - `epsilon1_zz`: dimensionless
    - `epsilon2_xx`: dimensionless
    - `epsilon2_yy`: dimensionless
    - `epsilon2_zz`: dimensionless

Notes: The task reproduces only the DFT computational part of the paper. Experimental ellipsometry, Mulliken population analysis, and effective mass calculations are excluded. The scissor shift of 0.9 eV must be applied in the dielectric step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kpoint_label",
          "kx",
          "ky",
          "kz"
        ],
        "additional_columns_pattern": "band_N (one column per sorted energy band, energies in eV)",
        "units": {
          "kx": "reciprocal lattice units",
          "ky": "reciprocal lattice units",
          "kz": "reciprocal lattice units",
          "band_*": "eV"
        }
      },
      "description": "Band energies along the Γ–Y–B–D–Γ path. The checker recomputes the indirect band gap (VBM at Γ, CBM at D point) and compares it to a hidden reference value."
    },
    {
      "file": "total_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos"
        ],
        "units": {
          "energy": "eV",
          "total_dos": "states/eV"
        }
      },
      "description": "Total DOS. The checker verifies the presence of a band gap near the expected energy and the qualitative shape of the valence/conduction bands."
    },
    {
      "file": "projected_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "s_dos",
          "p_dos",
          "O_dos",
          "C_dos",
          "N_dos",
          "H_dos",
          "S_dos"
        ],
        "units": {
          "energy": "eV",
          "s_dos": "states/eV",
          "p_dos": "states/eV",
          "O_dos": "states/eV",
          "C_dos": "states/eV",
          "N_dos": "states/eV",
          "H_dos": "states/eV",
          "S_dos": "states/eV"
        }
      },
      "description": "Projected DOS by orbital and element. The checker confirms that near the VBM the p‑character dominates (>80%) and that O and C contributions match the paper’s description."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "epsilon1_xx",
          "epsilon1_yy",
          "epsilon1_zz",
          "epsilon2_xx",
          "epsilon2_yy",
          "epsilon2_zz"
        ],
        "units": {
          "energy": "eV",
          "epsilon1_xx": "dimensionless",
          "epsilon1_yy": "dimensionless",
          "epsilon1_zz": "dimensionless",
          "epsilon2_xx": "dimensionless",
          "epsilon2_yy": "dimensionless",
          "epsilon2_zz": "dimensionless"
        }
      },
      "description": "Dielectric tensor after scissor shift (0.9 eV). The checker locates the peak of epsilon2_xx in the 5–10 eV window and compares its position to a hidden reference value."
    }
  ],
  "notes": "The task reproduces only the DFT computational part of the paper. Experimental ellipsometry, Mulliken population analysis, and effective mass calculations are excluded. The scissor shift of 0.9 eV must be applied in the dielectric step."
}
```

## How you are scored
A hidden verifier reads your CSV artifacts, recomputes key quantities (e.g., the indirect band gap from the band energies, the location of the strongest ε₂ peak), and performs structural audits on the DOS files (e.g., verifying dominant p‑character near the valence band maximum and checking element‑resolved contributions). Each scored artifact contributes a portion of the total reward; the final score is a weighted average between 0 and 1. Simply reporting a number without producing the underlying computation artifacts will not satisfy the task.
