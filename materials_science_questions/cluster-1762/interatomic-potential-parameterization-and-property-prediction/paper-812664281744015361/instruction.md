# Hyperfine Interaction Tensors of P_Ga Antisite in GaP via Extended Tight-Binding Defect Theory

## Problem background
The task addresses the electronic structure and hyperfine interaction of a phosphorus antisite defect (P_Ga) in gallium phosphide (GaP), where a phosphorus atom substitutes for a gallium atom. Electron spin resonance (ESR) and optically detected magnetic resonance (ODMR) experiments have resolved the hyperfine interaction of the unpaired electron with the antisite phosphorus and with four equivalent nearest-neighbor phosphorus atoms. The objective of this reproduction is to compute the hyperfine-interaction tensors and associated wavefunction properties from first-principles tight-binding theory, including the effect of lattice relaxation around the defect. This requires determining the nearest-neighbor outward relaxation that yields the best agreement with experimental hyperfine constants, providing a quantitative test of the extended tight-binding defect model.

## Approach
The method uses the theory of deep defects by Hjalmarson et al., extended to include the diagonal defect potential on nearest-neighbor sites and lattice relaxation. The host crystal is described by an empirical tight-binding Hamiltonian for GaP. Host Green's function matrix elements in the A1 symmetric basis are computed over a special k-point mesh. The defect potential is parameterized: the diagonal element on the antisite (V00) is set from atomic s-orbital energy differences; the off-diagonal coupling between antisite and nearest neighbors (V01) follows Harrison's d⁻² scaling law. The bound-state energy is fixed to the experimental defect energy obtained from photoresponse ESR. For each trial relaxation ratio dI/dH, the determinantal equation is solved to obtain the nearest-neighbor diagonal potential V11. The linear equations and normalization condition then yield the symmetric amplitudes, which are expanded in atomic orbitals to give site probabilities (η²) and s/p characters (α²). Using free-ion hyperfine constants for ³¹P and ⁶⁹Ga, the probability amplitudes are converted into hyperfine interaction tensors: isotropic a, anisotropic b, parallel A∥, perpendicular A⊥, and the direction angle θ of the principal axis for each atom. A sweep over dI/dH is performed, and the optimum relaxation ratio is selected by comparing the computed hyperfine constants for the antisite phosphorus (P_Ga) and the four nearest-neighbor phosphorus atoms (P₄) with the available experimental data. At the optimum relaxation, the final hyperfine parameters and the two symmetric defect-state amplitudes are recorded.

## Reproduction target
Given the tight-binding parameters, atomic hyperfine constants, and the experimental defect energy level, implement the extended tight-binding defect calculation to produce:

(1) The hyperfine interaction tensors (isotropic component a, anisotropic component b, parallel component A∥, perpendicular component A⊥, and direction angle θ) for the antisite phosphorus atom (P_Ga), for each of the four nearest-neighbor phosphorus atoms (P₄), and for each of the twelve next-nearest-neighbor gallium atoms (Ga₁₂) — all evaluated at the relaxation ratio that best matches the experimental hyperfine data.

(2) The optimal lattice relaxation ratio dI/dH (impurity bond length over host bond length).

(3) The symmetric wavefunction amplitudes ⟨A1 01|ψ⟩ and ⟨A1 11|ψ⟩ at that optimal relaxation.

These results must be written to /app/outputs/results.json and /app/outputs/wavefunction_amplitudes.json, following the schemas detailed in the output contract.

## Assets

- Empirical tight-binding parameters for GaP (Talwar & Ting, 1982): 10.1103/PhysRevB.25.2660
- Atomic s-orbital energies for P and Ga (Hjalmarson et al., 1980): 10.1103/PhysRevLett.44.810
- Harrison universal tight-binding parameter W
- Atomic hyperfine constants for 31P (Watkins & Corbett, 1964): 10.1103/PhysRev.136.A1359
- Atomic hyperfine constants for 69Ga (Jeon et al., 1989): 10.1103/PhysRevB.39.3207
- Experimental defect energy level for P_Ga in GaP: 10.1088/0022-3719/14/33/005
- Special k-points method (Chadi & Cohen, 1973): 10.1103/PhysRevB.8.5747

## Workflow steps

### Step 1: Compute host Green's function matrix elements
- Role: process
- Action: Using the empirical tight-binding Hamiltonian for GaP and the special k-point method, compute the host crystal Green's function matrix elements G00(E), G01(E), G10(E), G11(E) and their energy derivatives in the A1 symmetric basis as functions of energy E across the band gap.
- Evidence: `/app/outputs/green_functions.npy`

### Step 2: Defect potential parameterization and solve for V11
- Role: process
- Action: Set the antisite diagonal potential V00 using atomic s-orbital energies. Compute off-diagonal coupling V01/V10 as a function of lattice relaxation ratio dI/dH using Harrison's bond-length scaling. For a sweep of relaxation ratios, use the experimental defect energy and the Green's function matrix elements to solve the determinantal equation for the nearest-neighbor diagonal potential V11. Save arrays of dI/dH and corresponding V11.
- Evidence: `/app/outputs/defect_potentials.npy`

### Step 3: Solve defect wavefunction amplitudes
- Role: process
- Action: For each relaxation ratio, solve the linear equations and normalization condition to obtain the symmetric amplitudes, and expand to atomic orbital coefficients. Compute probabilities η² and s-character percentages α² for the antisite phosphorus, nearest-neighbor phosphorus, and next-nearest-neighbor gallium atoms as functions of dI/dH.
- Evidence: `/app/outputs/wavefunction_results.npy`

### Step 4: Compute hyperfine interaction tensors
- Role: process
- Action: Using atomic hyperfine constants for 31P and 69Ga, convert wavefunction probabilities and characters into hyperfine interaction parameters (a, b, A_parallel, A_perpendicular, direction angles) for each atom and relaxation ratio. Save the hyperfine parameters as functions of dI/dH.
- Evidence: `/app/outputs/hyperfine_sweep.npy`

### Step 5: Select optimum relaxation and output final hyperfine results
- Role: scored (load-bearing)
- Action: From the sweep of relaxation ratios, determine the optimum lattice relaxation ratio that yields the best agreement with experimental hyperfine data. At that optimum relaxation, assemble the final hyperfine parameters and wavefunction characters into a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: relaxation_ratio (float), P_Ga (object with A, alpha2, beta2, eta2, theta), P4 (array of 4 objects each with A_parallel, A_perp, a, b, alpha2, beta2, eta2, theta), Ga12 (array of 12 objects each with a, b, alpha2, beta2, eta2).
- Scoring: scored by hidden verifier

### Step 6: Output defect wavefunction amplitudes at optimum relaxation
- Role: scored
- Action: At the optimum relaxation ratio, record the symmetric amplitudes ⟨A1 01|ψ⟩ and ⟨A1 11|ψ⟩ and write them to a JSON file.
- Output file: `/app/outputs/wavefunction_amplitudes.json`
- Format: json
- Contract: JSON object with keys: A1_01_amplitude (float), A1_11_amplitude (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/wavefunction_amplitudes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final hyperfine parameters and wavefunction properties at the optimal lattice relaxation for P_Ga, P4, and Ga12.
- schema:
  - `type`: object
  - `required`:
    - `relaxation_ratio`: number
    - `P_Ga`: object
    - `P4`: array
    - `Ga12`: array
  - `items`:
    - `relaxation_ratio`: float
    - `P_Ga.A`: number
    - `P_Ga.alpha2`: number
    - `P_Ga.beta2`: number
    - `P_Ga.eta2`: number
    - `P_Ga.theta`: number
    - `P4[].A_parallel`: number
    - `P4[].A_perp`: number
    - `P4[].a`: number
    - `P4[].b`: number
    - `P4[].alpha2`: number
    - `P4[].beta2`: number
    - `P4[].eta2`: number
    - `P4[].theta`: number
    - `Ga12[].a`: number
    - `Ga12[].b`: number
    - `Ga12[].alpha2`: number
    - `Ga12[].beta2`: number
    - `Ga12[].eta2`: number

### wavefunction_amplitudes.json
- path: `/app/outputs/wavefunction_amplitudes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The two symmetric defect-state amplitudes at the optimal relaxation ratio.
- schema:
  - `type`: object
  - `required`:
    - `A1_01_amplitude`: number
    - `A1_11_amplitude`: number
  - `items`:
    - `A1_01_amplitude`: float
    - `A1_11_amplitude`: float

Notes: The task reproduces the electronic structure and hyperfine calculation of the P_Ga antisite in GaP. The optimal relaxation ratio is determined by matching computed hyperfine constants to experimental data. All physical constants and input parameters are from publicly available sources.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relaxation_ratio": "number",
          "P_Ga": "object",
          "P4": "array",
          "Ga12": "array"
        },
        "items": {
          "relaxation_ratio": "float",
          "P_Ga.A": "number",
          "P_Ga.alpha2": "number",
          "P_Ga.beta2": "number",
          "P_Ga.eta2": "number",
          "P_Ga.theta": "number",
          "P4[].A_parallel": "number",
          "P4[].A_perp": "number",
          "P4[].a": "number",
          "P4[].b": "number",
          "P4[].alpha2": "number",
          "P4[].beta2": "number",
          "P4[].eta2": "number",
          "P4[].theta": "number",
          "Ga12[].a": "number",
          "Ga12[].b": "number",
          "Ga12[].alpha2": "number",
          "Ga12[].beta2": "number",
          "Ga12[].eta2": "number"
        }
      },
      "description": "Final hyperfine parameters and wavefunction properties at the optimal lattice relaxation for P_Ga, P4, and Ga12."
    },
    {
      "file": "wavefunction_amplitudes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A1_01_amplitude": "number",
          "A1_11_amplitude": "number"
        },
        "items": {
          "A1_01_amplitude": "float",
          "A1_11_amplitude": "float"
        }
      },
      "description": "The two symmetric defect-state amplitudes at the optimal relaxation ratio."
    }
  ],
  "notes": "The task reproduces the electronic structure and hyperfine calculation of the P_Ga antisite in GaP. The optimal relaxation ratio is determined by matching computed hyperfine constants to experimental data. All physical constants and input parameters are from publicly available sources."
}
```

## How you are scored
A hidden verifier will independently assess your output files. For each scored artifact, the verifier compares your reported values to reference values derived from the original study. The hyperfine parameters and the relaxation ratio are compared within tolerances that absorb legitimate implementation differences. The symmetric wavefunction amplitudes are checked for correct signs and magnitudes. Scores from the two artifacts are combined into a final reward between 0 (incorrect/no meaningful reproduction) and 1 (good reproduction). Intermediate process evidence files are not scored but are expected to be present to support the pipeline.
