# Isochoric heat capacity of diamond, silicon, and germanium using Morse-potential anharmonic model

## Problem background
The isochoric heat capacities of diamond, silicon, and germanium are calculated using a quantum‑statistical model that accounts for lattice anharmonicity through the Morse potential. The model yields anharmonic phonon energies E_n(ω) and a finite set of vibrational modes cut off at the Debye temperature. The resulting C_V(T) curves are compared with the standard harmonic Debye model to investigate how anharmonicity affects the heat capacity across a wide temperature range.

## Approach
The method uses the Morse pair potential to describe interatomic bonds and the exact energy eigenvalues of the anharmonic oscillator. For each material, the maximum vibrational quantum number N is determined from the Debye temperature and the potential‑well depth D. The partition function Z(ω,T) is constructed by summing over the allowed modes, and the mean free energy ⟨F(T)⟩ is obtained by integrating ln Z over the Debye frequency spectrum. The isochoric heat capacity is then obtained from the second temperature derivative of ⟨F⟩. The harmonic Debye model (D → ∞ limit) serves as a baseline for comparison. You will implement this procedure using the given parameters for diamond, silicon, and germanium, and compute C_V on a temperature grid.

## Reproduction target
Compute the isochoric heat capacity C_V(T) for diamond (0–2000 K), silicon (0–1500 K), and germanium (0–1500 K) at intervals of roughly 5–10 K using the anharmonic Morse‑potential model. Write the results to cv_curves.csv with columns: material, temperature_K, Cv_J_per_mol_K. The temperature range and material set are fixed; you must produce the three curves as specified.

## Assets

- Python with NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Compute isochoric heat capacity using Morse model
- Role: scored (load-bearing)
- Action: Implement the quantum-statistical model with the Morse potential: for each material (diamond, silicon, germanium), compute energy eigenvalues E_n(omega), determine the finite number of vibrational modes N, build the partition function Z(omega,T), evaluate the mean free energy integral over the Debye frequency, and obtain the isochoric heat capacity C_V(T) via numerical second derivative. Use the model parameters (Debye temperature, Debye frequency, potential-well depth, N) given in the instruction for each material. Compute C_V on a temperature grid from 0 K to at least 2000 K for diamond and to at least 1500 K for Si and Ge, with steps of approximately 5–10 K.
- Output file: `/app/outputs/cv_curves.csv`
- Format: csv
- Contract: CSV with columns: material (str, one of 'diamond', 'silicon', 'germanium'), temperature_K (float, Kelvin), Cv_J_per_mol_K (float, J/(mol·K)). Each row corresponds to one material-temperature point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cv_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cv_curves.csv
- path: `/app/outputs/cv_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed isochoric heat capacity C_V in J/(mol·K) for diamond, silicon, and germanium as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `material`, `temperature_K`, `Cv_J_per_mol_K`
  - `units`:
    - `temperature_K`: K
    - `Cv_J_per_mol_K`: J/(mol·K)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cv_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "temperature_K",
          "Cv_J_per_mol_K"
        ],
        "units": {
          "temperature_K": "K",
          "Cv_J_per_mol_K": "J/(mol·K)"
        }
      },
      "description": "Computed isochoric heat capacity C_V in J/(mol·K) for diamond, silicon, and germanium as a function of temperature."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks your cv_curves.csv. It selects a set of hidden temperature points for each material, compares your reported C_V values to reference values obtained from the anharmonic model under the same parameters, and computes the fraction of points whose deviation falls within a hidden tolerance. Your final reward is that fraction (a number between 0 and 1). To earn full credit, your computed heat capacities must be numerically accurate — simply reporting the paper’s numbers without actual computation will not pass the hidden check.
