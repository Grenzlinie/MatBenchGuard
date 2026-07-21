# Compute spin-wave gap and g-factor for a single-chain magnet via exact diagonalization

## Problem background
Single-chain magnets (SCMs) are quasi-one-dimensional materials composed of magnetic units coupled along a chain. Strong uniaxial anisotropy and weak interchain interactions make them ideal systems for studying quantum spin excitations. In the SCM [Mn2(saltmen)2Ni(pao)2(py)2](ClO4)2, each building block is a [Mn(III)-Ni(II)-Mn(III)] trimer with total spin S=3, linked by ferromagnetic interactions. At low temperatures, collective magnetic excitations can propagate along the chain. Understanding these spin-wave excitations and the associated effective g-factor is essential for describing the material's magnetic behavior. This task aims to compute the zero-field spin-wave excitation gap and the effective spectroscopic g-factor from the microscopic spin Hamiltonian using numerical exact diagonalization.

## Approach
The computation is based on a Heisenberg spin Hamiltonian for a periodic chain of L = 4 trimer units. The model uses intratrimer antiferromagnetic coupling J_AF between each Mn(III) (S=2) and the central Ni(II) (s=1), intertrimer ferromagnetic coupling J_F between terminal Mn ions of neighboring trimers, and uniaxial single-ion anisotropy D_Mn on all Mn sites (with D_Ni = 0). Zeeman terms are added for a magnetic field applied along the easy axis. The approach employs exact diagonalization (Lanczos algorithm) of the sparse Hamiltonian matrix to find the lowest energy eigenstates in the total Sz = 3L ground-state subspace and the Sz = 3L−1 first excited subspace at zero field. The spin-wave excitation gap is obtained as the energy difference between these two states. The effective g-factor is extracted from the linear Zeeman splitting of the ground-state multiplet by computing the energy shift at a small applied field and fitting the response.

## Reproduction target
Produce a JSON file, `step_01_spinwave_gap.json`, containing two numbers: the zero-field spin-wave excitation gap in Kelvin and the dimensionless effective g-factor. The gap should be computed from the exact diagonalization of the Hamiltonian with the given parameters (J_AF = -18.6 K, J_F = +1.3 K, D_Mn = -5.1 K, D_Ni = 0 K) using a chain of L = 4 trimer units under periodic boundary conditions. The g-factor should be derived from the Zeeman splitting at small fields along the easy axis.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Exact diagonalization and extraction of spin-wave gap and g-factor
- Role: scored (load-bearing)
- Action: Construct the spin Hamiltonian for a periodic chain of L=4 trimer units of the SCM [Mn2(saltmen)2Ni(pao)2(py)2](ClO4)2. The system contains 8 Mn(III) spins (S=2) and 4 Ni(II) spins (s=1). Use the Hamiltonian with intratrimer antiferromagnetic exchange J_AF = -18.6 K between each Mn and the central Ni, intertrimer ferromagnetic exchange J_F = +1.3 K between adjacent trimer terminal Mn spins, and uniaxial single-ion anisotropy D_Mn = -5.1 K on all Mn sites (D_Ni = 0). Include Zeeman terms for an applied magnetic field along the easy axis to extract the g-factor. Using exact diagonalization (Lanczos algorithm on the sparse Hamiltonian matrix in the total S_z subspace), compute the lowest energy eigenvalues in the S_z = 3L ground state and the S_z = 3L-1 first excited state at zero field. The zero-field spin-wave excitation gap is the energy difference between these two states (in Kelvin). Obtain the effective g-factor from the linear Zeeman splitting of the ground-state multiplet by computing the energy difference at a small applied field and fitting E(B) = E(0) + g μ_B B ΔS_z, treating g as the effective spectroscopic g-factor. Save the computed gap and g-factor in the specified JSON file.
- Output file: `/app/outputs/step_01_spinwave_gap.json`
- Format: json
- Contract: {"type": "object", "required": ["spinwave_gap_K", "g_factor"], "properties": {"spinwave_gap_K": {"type": "number"}, "g_factor": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_spinwave_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_spinwave_gap.json
- path: `/app/outputs/step_01_spinwave_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the computed spin-wave gap and g-factor. The checker compares these values to the paper-reported hidden gold with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `spinwave_gap_K`, `g_factor`
  - `properties`:
    - `spinwave_gap_K`:
      - `type`: number
      - `description`: zero-field spin-wave excitation gap in Kelvin
    - `g_factor`:
      - `type`: number
      - `description`: effective spectroscopic g-factor, dimensionless

Notes: The computation uses the exact diagonalization of a finite-chain Heisenberg Hamiltonian. The hidden checker verifies that the computed values match the paper's reported results within expected numerical precision. No other artifacts are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_spinwave_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "spinwave_gap_K",
          "g_factor"
        ],
        "properties": {
          "spinwave_gap_K": {
            "type": "number",
            "description": "zero-field spin-wave excitation gap in Kelvin"
          },
          "g_factor": {
            "type": "number",
            "description": "effective spectroscopic g-factor, dimensionless"
          }
        }
      },
      "description": "Contains the computed spin-wave gap and g-factor. The checker compares these values to the paper-reported hidden gold with appropriate tolerances."
    }
  ],
  "notes": "The computation uses the exact diagonalization of a finite-chain Heisenberg Hamiltonian. The hidden checker verifies that the computed values match the paper's reported results within expected numerical precision. No other artifacts are required."
}
```

## How you are scored
Your submitted file will be evaluated by a hidden verifier. It will read the values for `spinwave_gap_K` and `g_factor` from your JSON and compare them against reference values derived from the original experimental study. The comparison uses numerical tolerances appropriate for the computational method. The reward is based on how close your computed numbers are to those reference values. To receive full credit, you must honestly implement the Hamiltonian and diagonalization procedure; copying or guessing the answer without performing the required computation will yield incorrect results and a low score.
