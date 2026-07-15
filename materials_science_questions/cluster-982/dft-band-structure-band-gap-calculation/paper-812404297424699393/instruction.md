# First-Principles Positron Transport Properties in Indium Phosphide

## Problem background
Slow‑positron‑beam experiments probe surfaces and near‑surface regions of solids; interpreting their signals requires quantitative knowledge of positron transport. In compound semiconductors such as indium phosphide (InP), the diffusion constant and related transport parameters are key inputs for analysing defect profiles. The positron deformation potential governs the coupling between thermalized positrons and acoustic phonons, and it determines the longitudinal‑acoustic‑phonon‑limited diffusion constant, relaxation time, diffusion length, and mobility. This task computes these quantities for InP from first‑principles electronic structure methods together with the deformation‑potential model, yielding the positron deformation potential, diffusion constant, relaxation time, diffusion length, mobility, and positron and positronium work functions at 300 K.

## Approach
The electron band structure of InP in the zincblende phase is obtained with the empirical pseudopotential method (EPM), using a set of symmetric and antisymmetric form factors at the equilibrium lattice constant and at a slightly expanded lattice constant. The positron band structure is computed in the independent particle model (IPM) for a thermalized positron moving in the same crystal potential augmented by an electron‑positron correlation potential. These calculations yield the electron and positron chemical potentials at both lattice constants, from which the volume derivatives are determined numerically. The positron deformation potential is the sum of the electron and positron volume derivatives. The average longitudinal elastic constant is evaluated from the experimentally known single‑crystal elastic constants C11, C12, and C44 of InP using the standard combination formula. With the deformation potential, the average elastic constant, an adopted positron effective mass (m* = 1.3 mₑ), and the temperature (300 K), the diffusion constant is computed from the deformation‑potential expression for acoustic‑phonon‑limited diffusion. The relaxation time follows from the same scattering theory. The bulk diffusion length is obtained from the diffusion constant and the reported bulk positron lifetime. The mobility is derived via the Einstein relation. Finally, the positron and positronium work functions are calculated from the chemical potentials and the known experimental electron work function.

## Reproduction target
Produce a JSON file `results.json` containing the following seven computed quantities for InP at 300 K:

- `Ed_plus`: positron deformation potential (eV)
- `D_plus`: positron diffusion constant (cm² s⁻¹)
- `iota_LA`: relaxation time for longitudinal‑acoustic‑phonon scattering (s)
- `L_plus`: positron diffusion length (Å)
- `mu`: positron mobility (cm² V⁻¹ s⁻¹)
- `phi_plus`: positron work function (eV)
- `phi_ps`: positronium work function (eV)

The workflow that produces this file must execute the full pipeline: electron band structure (EPM), positron band structure (IPM), and the subsequent analytical derivations that combine the numerical results with the supplied external constants (elastic constants, electron work function, bulk lifetime).

## Assets

- InP elastic constants
- InP electron work function
- InP positron bulk lifetime
- Python scientific stack: numpy scipy

## Workflow steps

### Step 1: Compute electron band structure and chemical potentials
- Role: process
- Action: Implement the empirical pseudopotential method (EPM) for InP in the zincblende structure at the equilibrium lattice constant a0 = 11.09 a.u. and at a slightly expanded lattice constant (e.g. a0 + 0.05 a.u.). Use the symmetric and antisymmetric form factors: Vs(3) = -0.26 Ryd, Vs(8) = 0.01 Ryd, Vs(11) = 0.07 Ryd, Va(3) = 0.02 Ryd, Va(4) = 0.05 Ryd, Va(11) = 0.013 Ryd. Solve the secular equation on a sufficiently fine k-point grid to obtain the electron band structure. Extract the electron chemical potential (Fermi level). Save the equilibrium chemical potential in mu_e_eq.txt and the expanded-lattice value in mu_e_exp.txt.
- Evidence: `/app/outputs/mu_e_eq.txt, mu_e_exp.txt`

### Step 2: Compute positron band structure and chemical potentials
- Role: process
- Action: Using the independent particle model (IPM) for a thermalized positron, compute the positron band structure in the same InP crystal at the two lattice constants from step_01. The positron feels the crystal potential from the electron density obtained in step_01, with an additional electron-positron correlation potential. Determine the lowest positron energy (the positron chemical potential). Save the equilibrium value in mu_p_eq.txt and the expanded-lattice value in mu_p_exp.txt.
- Evidence: `/app/outputs/mu_p_eq.txt, mu_p_exp.txt`

### Step 3: Calculate transport properties and work functions
- Role: scored (load-bearing)
- Action: Read the chemical potentials from step_01 and step_02. Compute the electron and positron volume derivatives numerically (Ω ∂μ/∂Ω). The positron deformation potential E_d^+ is the sum of these derivatives. Using experimental elastic constants C11, C12, C44 (resource res1), compute the average longitudinal elastic constant ⟨Cii⟩ via the formula that combines them. With an adopted positron effective mass m* = 1.3 m_e, temperature T = 300 K, the deformation potential, and the average elastic constant, compute the positron diffusion constant D_+ from the deformation-potential expression for acoustic-phonon-limited diffusion. Determine the relaxation time ι_LA from the same scattering theory. Calculate the bulk diffusion length L_+ = sqrt(D_+ τ) using the bulk lifetime τ = 244 ps (resource res3). Compute the mobility μ from the Einstein relation μ = D_+ e / (k_B T). Finally, compute the positron work function φ_+ = -μ_+ - Δ and the positronium work function φ_ps = -μ_+ - 0.5 Ry, where Δ is obtained from the experimental electron work function φ_- (resource res2) and the electron chemical potential μ_- via Δ = φ_- - μ_-. Write all results to results.json with the exact keys and units specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: Ed_plus (number, eV), D_plus (number, cm^2/s), iota_LA (number, s), L_plus (number, Å), mu (number, cm^2 V^{-1} s^{-1}), phi_plus (number, eV), phi_ps (number, eV)
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
- description: The seven derived positron transport coefficients and work functions for InP at 300 K, obtained from the full band-structure-based workflow.
- schema:
  - `type`: object
  - `required`:
    - `Ed_plus`: number (eV)
    - `D_plus`: number (cm^2/s)
    - `iota_LA`: number (s)
    - `L_plus`: number (Å)
    - `mu`: number (cm^2 V^{-1} s^{-1})
    - `phi_plus`: number (eV)
    - `phi_ps`: number (eV)

Notes: The agent must compute all quantities from the prior band structure steps; the hidden checker compares each value to the paper's reported results with per-field tolerances.

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
          "Ed_plus": "number (eV)",
          "D_plus": "number (cm^2/s)",
          "iota_LA": "number (s)",
          "L_plus": "number (Å)",
          "mu": "number (cm^2 V^{-1} s^{-1})",
          "phi_plus": "number (eV)",
          "phi_ps": "number (eV)"
        }
      },
      "description": "The seven derived positron transport coefficients and work functions for InP at 300 K, obtained from the full band-structure-based workflow."
    }
  ],
  "notes": "The agent must compute all quantities from the prior band structure steps; the hidden checker compares each value to the paper's reported results with per-field tolerances."
}
```

## How you are scored
A hidden verifier reads `results.json` and compares each field to a set of reference values derived from the original study. The comparison uses per‑field tolerances that accommodate legitimate numerical differences between independent implementations. The overall reward reflects how many of the seven quantities fall within those tolerances. Note that the verifier expects the numbers to be the outcome of genuine EPM and IPM computations; simply reporting the published values without performing the required band‑structure calculations will not satisfy the intermediate process steps and may be detected by the verifier’s consistency checks.
