# Wannier Hamiltonian Parameterization for O–O Distance in Li2O2

## Problem background
Lithium peroxide (Li2O2) is the primary discharge product in non-aqueous lithium-air batteries. The accumulation of this insulating material at the cathode can block charge flow, and understanding its charge transport properties is crucial for improving battery performance. Previous studies have indicated that both electron and hole polarons form in Li2O2, and their mobility is governed by strong electron-lattice coupling. To develop realistic models of polaron dynamics, one needs an efficient, localized description of the electronic states and a quantitative characterization of how they depend on the atomic geometry. In this work, we focus on the oxygen–oxygen dimer distance as the key structural degree of freedom that modulates the electronic structure, and we derive a compact one-electron Hamiltonian in a Wannier basis that captures this dependence.

## Approach
The calculations are based on density functional theory (DFT) using the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the SIESTA code with a TZP (triple-ζ polarized) basis set of numerical atomic orbitals. Core electrons are replaced by norm-conserving pseudopotentials. First, the crystal structure (space group P63/mmc) is relaxed until forces and stress are well converged. Using the relaxed geometry, the electronic band structure is computed and the direct band gap at the Γ point is extracted for both the PBE functional and the HSE06 screened hybrid functional (25% exact exchange).

To build a minimal electron-lattice model, maximally projected Wannier functions are constructed from the Kohn-Sham bands using WANNIER90. Two types of Wannier bases are considered: (i) quasi-atomic p-type Wannier functions obtained by projecting onto the twelve O-2p atomic orbitals of the cell, and (ii) molecular Wannier functions that isolate the bands associated with the σg, πu, πg*, and σu* molecular orbitals of the O₂²⁻ dimers. A series of self-consistent DFT calculations is carried out for structures in which the oxygen–oxygen dimer distance is varied by small deviations Δd_OO away from the equilibrium value. For each distance, the one-electron Wannier Hamiltonian matrix elements (diagonal self-energies and off-diagonal hopping terms) are computed in both bases. Finally, the diagonal self-energies of the molecular Wannier bands are fitted to low-order polynomials in Δd_OO to obtain a compact analytical description of the electron-vibration coupling.

## Reproduction target
The task is to reproduce the key quantitative results of this computational study by running the full DFT–Wannier pipeline with the specified codes, pseudopotentials, and basis sets. The following quantities must be computed from the raw DFT and Wannier data and written to the indicated output files under `/app/outputs`:

1. **PBE band gap at Γ** – a single number (eV) written to `step_01_pbe_band_gap.txt`.
2. **HSE06 band gap at Γ** – a single number (eV) written to `step_02_hse06_band_gap.txt`.
3. **Equilibrium off-diagonal matrix elements in the quasi-atomic p-basis** – at Δd_OO = 0.0, the intra-dimer hopping term for the p_z pair and the (degenerate) p_x/p_y pair, formatted as a JSON object `{"pz_offdiagonal_eV": ..., "px_py_offdiagonal_eV": ...}` and written to `step_03_off_diagonals.json`.
4. **Polynomial fits of the molecular-Wannier diagonal energies** – using the self-energies of the σ_g, π_u, π_g*, and σ_u* bands at the five Δd_OO points, perform a second‑order polynomial fit (quadratic) for all four bands and, for the band that shows the strongest deviation from a parabola, add a third‑order term (cubic). Store the fit coefficients as 4‑element arrays (the cubic term set to zero for the quadratic fits) in a JSON object with keys "sigma_g", "pi_u", "pi_g_star", "sigma_u_star" and write it to `step_04_polynomial_coefficients.json`.

All values must be derived from your own SIESTA and WANNIER90 calculations.

## Assets

- SIESTA code (version ≥ 4.1): https://gitlab.com/siesta-project/siesta
- WANNIER90 code (version ≥ 3.1): http://www.wannier.org
- PseudoDojo ONCVPSP pseudopotentials v0.4.1 (scalar relativistic, stringent accuracy): http://www.pseudo-dojo.org
- LIBXC library (version ≥ 5.0): https://gitlab.com/libxc/libxc

## Workflow steps

### Step 1: DFT geometry optimization of bulk Li2O2
- Role: process
- Action: Relax atomic positions and lattice parameters of bulk Li2O2 in the P6_3/mmc space group using SIESTA with the PBE functional and a TZP basis set. Converge forces and stress. The relaxed structure will be used in subsequent steps.
- Evidence: none

### Step 2: PBE band gap at Γ
- Role: scored
- Action: Using the relaxed structure, compute the electronic band structure with SIESTA (PBE, TZP) and extract the direct band gap at the Γ point. Write the value in eV to step_01_pbe_band_gap.txt.
- Output file: `/app/outputs/step_01_pbe_band_gap.txt`
- Format: txt
- Contract: A single floating-point number in eV (e.g., 0.0).
- Scoring: scored by hidden verifier

### Step 3: HSE06 band gap at Γ
- Role: scored
- Action: Using the relaxed structure, compute the electronic band structure with SIESTA using the HSE06 hybrid functional (25% exact exchange) and TZP basis. Extract the direct band gap at Γ and write the value in eV to step_02_hse06_band_gap.txt.
- Output file: `/app/outputs/step_02_hse06_band_gap.txt`
- Format: txt
- Contract: A single floating-point number in eV (e.g., 0.0).
- Scoring: scored by hidden verifier

### Step 4: DFT scan over O–O distances and Wannierization
- Role: process
- Action: From the relaxed equilibrium structure, generate structures with O–O dimer distance changes Δd_OO = -0.2, -0.1, 0.0, +0.1, +0.2 Å. For each structure, run a self-consistent DFT calculation (PBE, TZP) using SIESTA, then use WANNIER90 to construct quasi-atomic p-type and molecular Wannier functions and compute the one-electron Wannier Hamiltonian matrix elements. Save all data to wannier_scan_data.json.
- Evidence: `/app/outputs/wannier_scan_data.json`

### Step 5: Equilibrium quasi-atomic off-diagonal matrix elements
- Role: scored
- Action: From wannier_scan_data.json, extract the intra-dimer off-diagonal Hamiltonian matrix element for the p_z Wannier orbital pair and for the degenerate p_x/p_y pair at Δd_OO = 0.0 (equilibrium). Write these two values to step_03_off_diagonals.json.
- Output file: `/app/outputs/step_03_off_diagonals.json`
- Format: json
- Contract: {"pz_offdiagonal_eV": <float>, "px_py_offdiagonal_eV": <float>}
- Scoring: scored by hidden verifier

### Step 6: Polynomial fits of molecular Wannier energies
- Role: scored (load-bearing)
- Action: Using the diagonal self-energies of the molecular Wannier orbitals (σ_g, π_u, π_g*, σ_u*) from wannier_scan_data.json at all five Δd_OO points, perform polynomial fits: for σ_g, π_u, and π_g* fit a second-order polynomial h = a0 + a1*Δd_OO + a2*Δd_OO²; for σ_u* fit a third-order polynomial h = a0 + a1*Δd_OO + a2*Δd_OO² + a3*Δd_OO³. Write the coefficients to step_04_polynomial_coefficients.json.
- Output file: `/app/outputs/step_04_polynomial_coefficients.json`
- Format: json
- Contract: {"sigma_g": [a0,a1,a2,0.0], "pi_u": [a0,a1,a2,0.0], "pi_g_star": [a0,a1,a2,0.0], "sigma_u_star": [a0,a1,a2,a3]} (floats in eV, eV/Å, eV/Å^2, eV/Å^3)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_pbe_band_gap.txt`
- `/app/outputs/step_02_hse06_band_gap.txt`
- `/app/outputs/step_03_off_diagonals.json`
- `/app/outputs/step_04_polynomial_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_pbe_band_gap.txt
- path: `/app/outputs/step_01_pbe_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: PBE band gap at Γ point of bulk Li2O2.
- schema:
  - `type`: text
  - `units`:
    - `value`: eV

### step_02_hse06_band_gap.txt
- path: `/app/outputs/step_02_hse06_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: HSE06 band gap at Γ point of bulk Li2O2.
- schema:
  - `type`: text
  - `units`:
    - `value`: eV

### step_03_off_diagonals.json
- path: `/app/outputs/step_03_off_diagonals.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium intra-dimer off-diagonal Hamiltonian matrix elements for quasi-atomic p_z and p_x/p_y Wannier orbitals.
- schema:
  - `type`: object
  - `required`:
    - `pz_offdiagonal_eV`: float
    - `px_py_offdiagonal_eV`: float
  - `units`:
    - `pz_offdiagonal_eV`: eV
    - `px_py_offdiagonal_eV`: eV

### step_04_polynomial_coefficients.json
- path: `/app/outputs/step_04_polynomial_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Polynomial coefficients (a0,a1,a2,a3) for the Δd_OO dependence of molecular Wannier orbital diagonal energies. σ_g, π_u, π_g_star are second-order (a3=0); σ_u_star is third-order.
- schema:
  - `type`: object
  - `required`:
    - `sigma_g`: array[4]
    - `pi_u`: array[4]
    - `pi_g_star`: array[4]
    - `sigma_u_star`: array[4]
  - `units`:
    - `coefficients`: eV, eV/Å, eV/Å^2, eV/Å^3

Notes: Scoring tolerances and hidden evaluation points are defined in the grading specification. All artifacts must be self-contained under /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_pbe_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "eV"
        }
      },
      "description": "PBE band gap at Γ point of bulk Li2O2."
    },
    {
      "file": "step_02_hse06_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "eV"
        }
      },
      "description": "HSE06 band gap at Γ point of bulk Li2O2."
    },
    {
      "file": "step_03_off_diagonals.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pz_offdiagonal_eV": "float",
          "px_py_offdiagonal_eV": "float"
        },
        "units": {
          "pz_offdiagonal_eV": "eV",
          "px_py_offdiagonal_eV": "eV"
        }
      },
      "description": "Equilibrium intra-dimer off-diagonal Hamiltonian matrix elements for quasi-atomic p_z and p_x/p_y Wannier orbitals."
    },
    {
      "file": "step_04_polynomial_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "sigma_g": "array[4]",
          "pi_u": "array[4]",
          "pi_g_star": "array[4]",
          "sigma_u_star": "array[4]"
        },
        "units": {
          "coefficients": "eV, eV/Å, eV/Å^2, eV/Å^3"
        }
      },
      "description": "Polynomial coefficients (a0,a1,a2,a3) for the Δd_OO dependence of molecular Wannier orbital diagonal energies. σ_g, π_u, π_g_star are second-order (a3=0); σ_u_star is third-order."
    }
  ],
  "notes": "Scoring tolerances and hidden evaluation points are defined in the grading specification. All artifacts must be self-contained under /app/outputs."
}
```

## How you are scored
A hidden verifier reads the four output artifacts you place under `/app/outputs`. For the two band gaps and the two equilibrium off-diagonal matrix elements, the verifier compares your reported numbers to the correct reference values (obtained from a faithful independent implementation) and awards credit according to how close they are within generous tolerances. For the polynomial coefficients, the verifier uses your submitted fits to reconstruct the self-energy curves at several intermediate Δd_OO values not disclosed in these instructions, and then computes the mean absolute deviation between those reconstructed energies and the reference energies at the same points. Your overall score is a weighted combination of the individual stage scores, with the polynomial-fit stage contributing a substantial fraction of the total reward. Simply submitting plausible guesses is not sufficient; the coefficients must be consistent with the electronic structure obtained from the DFT–Wannier pipeline, and all artifacts must be computed from the raw data without referring to pre‑determined target numbers.
