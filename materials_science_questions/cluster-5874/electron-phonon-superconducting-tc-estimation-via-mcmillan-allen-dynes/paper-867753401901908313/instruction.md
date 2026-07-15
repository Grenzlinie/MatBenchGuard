# DFT+U Electron-Phonon Superconducting Tc Estimation for LaRu₃Si₂

## Problem background
LaRu₃Si₂ is a layered compound that contains a distorted kagome lattice of ruthenium atoms. Experimentally it becomes superconducting with a critical temperature near 7 K. First‑principles electronic‑structure calculations reveal that a kagome flat band, a Dirac point and a van Hove singularity reside close to the Fermi level. The central computational question is whether the electron‑phonon interaction alone can provide the pairing mechanism that explains the observed superconducting transition. This task reproduces the density‑functional‑theory (DFT) part of the study: it carries out geometry optimization, phonon calculations and electron‑phonon coupling analysis, and finally evaluates the superconducting critical temperature that results from electron‑phonon coupling only.

## Approach
We use density functional theory with a Hubbard‑U correction (U = 1 eV applied to Ru 4d states) to perform a full geometry optimization of bulk LaRu₃Si₂ in the P6₃/m space group. From the relaxed structure we compute the electronic band dispersion along the high‑symmetry k‑path and locate the energies of the characteristic kagome features: the flat band, the Dirac point at K, and the van Hove singularity near M. In parallel we compute the phonon dispersion on a 2 × 2 × 2 supercell using density‑functional perturbation theory. The electron‑phonon coupling constant λ is then derived from the Eliashberg spectral function. Finally, the superconducting critical temperature Tc is estimated with the McMillan–Allen–Dynes formula using the computed λ, the Debye temperature θ_D = 280 K and the Coulomb pseudopotential μ* = 0.12. The entire workflow is built with open‑source codes (Quantum ESPRESSO and Phonopy) and produces numerical results that can be compared against reference values.

## Reproduction target
From the DFT+U workflow you must compute and write to the prescribed output files:
- The optimized lattice constants a and c (in Å) after full ionic and cell relaxation.
- The energies (relative to the Fermi level, in eV) of the kagome flat band, the Dirac point at K, and the van Hove singularity near M.
- The electron‑phonon coupling constant λ.
- The superconducting critical temperature Tc (in K) obtained from the McMillan–Allen–Dynes formula with θ_D = 280 K and μ* = 0.12.
All outputs are to be placed under /app/outputs as specified in the workflow steps.

## Assets

- LaRu3Si2 crystal structure (P6_3/m) CIF/POSCAR
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/
- Python (standard data processing): python

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored
- Action: Perform DFT+U (GGA+U with U=1 eV on Ru 4d) geometry optimization of bulk LaRu3Si2 in P6_3/m space group. Optimize lattice parameters and atomic positions until forces are below 0.01 eV/Å. Output the final optimized lattice constants a and c (in Å).
- Output file: `/app/outputs/optimized_lattice.txt`
- Format: txt
- Contract: Two numbers (a and c, in Å) separated by whitespace.
- Scoring: scored by hidden verifier

### Step 2: Electronic band structure and feature energies
- Role: scored
- Action: Compute the electronic band structure of the optimized LaRu3Si2 using DFT+U (U=1 eV) along the high-symmetry k-path. Identify the energies of the flat band (the nearly dispersionless band nearest the Fermi level), the Dirac point (band crossing at K point), and the van Hove singularity (peak in DOS near the M point), and output their energies relative to the Fermi level in eV.
- Output file: `/app/outputs/band_feature_energies.json`
- Format: json
- Contract: JSON object with keys: flat_band_energy (float, eV), dirac_point_energy (float, eV), van_hove_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion calculation
- Role: process
- Action: Calculate the phonon dispersion of LaRu3Si2 using density functional perturbation theory (DFPT) or the finite displacement method with a 2×2×2 supercell and the GGA+U functional (U=1 eV).
- Evidence: `/app/outputs/phonon_band.dat`

### Step 4: Electron-phonon coupling constant λ
- Role: scored (load-bearing)
- Action: Using the phonon and electronic data, compute the electron-phonon coupling constant λ (e.g., from the Eliashberg spectral function). Output the value.
- Output file: `/app/outputs/epc_lambda.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

### Step 5: McMillan Tc estimation
- Role: scored
- Action: Using the computed λ, the Debye temperature θ_D = 280 K, and the Coulomb pseudopotential μ* = 0.12, compute the superconducting critical temperature Tc using the McMillan-Allen-Dynes formula. Output the Tc in Kelvin.
- Output file: `/app/outputs/computed_tc.txt`
- Format: txt
- Contract: A single floating-point number in K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice.txt`
- `/app/outputs/band_feature_energies.json`
- `/app/outputs/epc_lambda.txt`
- `/app/outputs/computed_tc.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice.txt
- path: `/app/outputs/optimized_lattice.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants of LaRu3Si2 after DFT+U relaxation.
- schema:
  - `type`: text
  - `description`: Two whitespace-separated numbers: a and c in Å, each to at least 4 decimal places.

### band_feature_energies.json
- path: `/app/outputs/band_feature_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energies of the flat band, Dirac point, and van Hove point from the electronic band structure.
- schema:
  - `type`: object
  - `properties`:
    - `flat_band_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Energy of the kagome flat band relative to the Fermi level
    - `dirac_point_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Energy of the Dirac point at K relative to the Fermi level
    - `van_hove_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Energy of the van Hove singularity near M relative to the Fermi level
  - `required`: `flat_band_energy`, `dirac_point_energy`, `van_hove_energy`

### epc_lambda.txt
- path: `/app/outputs/epc_lambda.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed electron-phonon coupling constant λ.
- schema:
  - `type`: number
  - `description`: A single floating-point number representing the electron-phonon coupling constant λ.

### computed_tc.txt
- path: `/app/outputs/computed_tc.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature estimated from McMillan-Allen-Dynes formula.
- schema:
  - `type`: number
  - `unit`: K
  - `description`: A single floating-point number representing the superconducting critical temperature Tc in Kelvin.

Notes: All outputs are numerical and deterministic for the given DFT+U protocol. The checker will compare submitted values to the paper's reported values within appropriate tolerances (not disclosed here). The phonon_band.dat is process evidence, not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Two whitespace-separated numbers: a and c in Å, each to at least 4 decimal places."
      },
      "description": "Optimized lattice constants of LaRu3Si2 after DFT+U relaxation."
    },
    {
      "file": "band_feature_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "flat_band_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Energy of the kagome flat band relative to the Fermi level"
          },
          "dirac_point_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Energy of the Dirac point at K relative to the Fermi level"
          },
          "van_hove_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Energy of the van Hove singularity near M relative to the Fermi level"
          }
        },
        "required": [
          "flat_band_energy",
          "dirac_point_energy",
          "van_hove_energy"
        ]
      },
      "description": "Energies of the flat band, Dirac point, and van Hove point from the electronic band structure."
    },
    {
      "file": "epc_lambda.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "description": "A single floating-point number representing the electron-phonon coupling constant λ."
      },
      "description": "Computed electron-phonon coupling constant λ."
    },
    {
      "file": "computed_tc.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "unit": "K",
        "description": "A single floating-point number representing the superconducting critical temperature Tc in Kelvin."
      },
      "description": "Superconducting critical temperature estimated from McMillan-Allen-Dynes formula."
    }
  ],
  "notes": "All outputs are numerical and deterministic for the given DFT+U protocol. The checker will compare submitted values to the paper's reported values within appropriate tolerances (not disclosed here). The phonon_band.dat is process evidence, not scored."
}
```

## How you are scored
A hidden verifier reads the output files you produce. For each scored stage — the optimized lattice constants, the band‑feature energies, the electron‑phonon coupling λ, and the McMillan Tc — the verifier compares your computed values against reference values with an appropriate tolerance. A perfect match to all targets yields the maximum reward; larger deviations reduce the score. The final reward is a weighted average of the per‑stage scores. Simply reporting a number without actually executing the DFT, phonon, and electron‑phonon coupling computations is unlikely to succeed, because the verifier expects results that can only be obtained from a correct execution of the prescribed workflow.
