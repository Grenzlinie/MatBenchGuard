# Defect Ionization Energy via Charge-Corrected Jellium Model

## Problem background
Low-dimensional semiconductors, such as two-dimensional monolayer materials, frequently contain point defects that control carrier concentrations and electronic properties. In first-principles defect calculations using periodic supercells, computing formation energies of charged defects has been a long-standing challenge. The standard approach—adding a uniform jellium background charge to neutralize the supercell—works well for three-dimensional bulk materials but fails for low-dimensional systems because the background charge spreads into the vacuum region, causing the total energy and derived defect ionization energies to diverge with vacuum thickness. The paper this task is based on proposes a physically motivated correction: replace the unphysical uniform jellium background charge with the charge density of the appropriate band-edge state (valence band maximum for acceptor defects, conduction band minimum for donor defects). This yields convergent, physically meaningful defect ionization energies without tunable parameters. Your task is to compute the ionization energies of two prototypical defects in monolayer hexagonal boron nitride (h-BN) using this charge-corrected jellium model, and to demonstrate convergence with respect to vacuum thickness.

## Approach
You will implement the charge-corrected jellium model inside an open-source plane-wave density-functional theory (DFT) code. The method consists of the following conceptual steps: 

1. Build a periodic supercell of pristine monolayer h-BN with a vacuum layer. Perform a standard ground-state DFT calculation to obtain the eigenvalues and real-space charge densities of the valence band maximum (VBM) and the conduction band minimum (CBM). 
2. Create neutral defect supercells (nitrogen vacancy V_N and carbon-on-nitrogen substitution C_N) and relax their atomic positions to obtain the neutral total energies. 
3. For a charged defect, add (or remove) electrons and introduce a compensating background charge, as in the conventional jellium model. Then, modify the self-consistent field routine so that the uniform background charge is replaced by the appropriate band-edge charge density: use the CBM density ρ_CBM for donor defects (V_N) and the VBM density ρ_VBM for acceptor defects (C_N). The corrected density must be applied at every electronic iteration, entering the self-consistent loop. 
4. From the corrected total energy of the charged defect supercell, E_corr^{N+1}, and the neutral total energy E^N, compute the ionization energy (IE) using the formula IE = E_corr^{N+1} − E^N − ε_band, where ε_band is ε_CBM for donors and ε_VBM for acceptors. 
5. To verify that the results are free of divergence, repeat the calculation for the acceptor defect at several vacuum thicknesses while keeping the lateral supercell size fixed. A well-converged method will yield an ionization energy that is independent of the vacuum thickness.

## Reproduction target
Your goal is to produce three scored output files using the charge-corrected jellium model for monolayer h-BN: 

1. **V_N_IE_15A.dat**: The ionization energy (in eV) of the nitrogen vacancy (V_N), a donor with charge state +1, computed in a 12×12×1 lateral supercell with a vacuum thickness of 15 Å. 
2. **C_N_IE_15A.dat**: The ionization energy (in eV) of the carbon-on-nitrogen substitutional defect (C_N), an acceptor with charge state -1, computed in the same 12×12×1 supercell with 15 Å vacuum. 
3. **C_N_convergence.dat**: A demonstration that the C_N ionization energy is converged with respect to vacuum thickness. Compute IE(C_N) in 12×12×1 supercells with vacuum thicknesses of 10, 20, and 30 Å, and record the results in a two-column tab-separated file (no header) listing vacuum thickness (Å) and IE (eV). The ionization energy should be essentially unchanged across these thicknesses, confirming the absence of divergence. 

All calculations must follow the full workflow: pristine host DFT to obtain band-edge densities and eigenvalues, neutral defect relaxations, charged defect calculations with the charge correction, and final ionization energy evaluation. The three output files constitute the primary artifacts that will be checked.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm‑conserving PBE pseudopotentials (B, N, C): https://www.materialscloud.org/archive/swedish_screening_sssp/efficiency-nc.html
- Monolayer h‑BN crystal structure: https://materialsproject.org/materials/mp-984/

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Build a 12×12×1 supercell of pristine monolayer h‑BN with a vacuum of 15 Å. Also construct additional supercells with the same lateral size and vacuum thicknesses 10, 20, 30 Å for the convergence study.
- Evidence: `/app/outputs/supercell.log`

### Step 2: Implement charge‑corrected jellium model in Quantum ESPRESSO
- Role: process
- Action: Modify the Quantum ESPRESSO self‑consistent field routine to replace the default uniform jellium background charge with the band‑edge charge density: ρ_VBM for acceptor defects, ρ_CBM for donor defects. The correction must be applied at every electronic iteration so that the corrected density enters the self‑consistent loop.
- Evidence: `/app/outputs/qe_modification.log`

### Step 3: Pristine host DFT
- Role: process
- Action: Run a ground‑state DFT calculation on the pristine 12×12 supercell (15 Å vacuum) with the standard QE build (no background charge). Extract the VBM and CBM eigenvalues (ε_VBM, ε_CBM) and their real‑space charge densities (ρ_VBM(r), ρ_CBM(r)). Store these for later steps. Optionally repeat for vacuum 10, 20, 30 Å if needed for alignment.
- Evidence: `/app/outputs/pristine_dft.log`

### Step 4: Neutral defect DFT
- Role: process
- Action: Create a nitrogen vacancy (V_N) and a carbon‑substitutional (C_N) in the 12×12 supercell (15 Å vacuum). Relax the atomic positions for each neutral defect and compute the ground‑state total energies E^N(V_N,0) and E^N(C_N,0).
- Evidence: `/app/outputs/neutral_defect.log`

### Step 5: Charged‑defect DFT with correction (V_N)
- Role: process
- Action: Using the modified QE code, compute the corrected total energy E_corr^{N+1}(V_N,+1) for the donor defect. The uniform background is replaced by the CBM charge density ρ_CBM obtained from the pristine host. Perform a self‑consistent calculation under the corrected charge distribution.
- Evidence: `/app/outputs/charged_VN.log`

### Step 6: Charged‑defect DFT with correction (C_N)
- Role: process
- Action: Similarly, compute E_corr^{N+1}(C_N,‑1) for the acceptor defect, replacing the background with the VBM charge density ρ_VBM from the pristine host.
- Evidence: `/app/outputs/charged_CN.log`

### Step 7: Compute V_N ionization energy
- Role: scored
- Action: Calculate the ionization energy for V_N as IE(V_N) = E_corr^{N+1}(V_N,+1) – E^N(V_N,0) – ε_CBM. Write the result to V_N_IE_15A.dat.
- Output file: `/app/outputs/V_N_IE_15A.dat`
- Format: txt
- Contract: A single text line containing a floating‑point number (eV).
- Scoring: scored by hidden verifier

### Step 8: Compute C_N ionization energy
- Role: scored
- Action: Calculate IE(C_N) = E_corr^{N+1}(C_N,‑1) – E^N(C_N,0) – ε_VBM. Write the result to C_N_IE_15A.dat.
- Output file: `/app/outputs/C_N_IE_15A.dat`
- Format: txt
- Contract: A single text line containing a floating‑point number (eV).
- Scoring: scored by hidden verifier

### Step 9: Convergence of C_N IE with vacuum thickness
- Role: scored (load-bearing)
- Action: For the three additional vacuum thicknesses (10, 20, 30 Å, same lateral 12×12 supercell), perform the complete pipeline (pristine host DFT for each thickness to obtain ε_VBM, neutral defect total energy, and charged‑defect DFT with the charge correction) to compute IE(C_N) at each thickness. Write a two‑column TSV file (no header) listing vacuum_thickness (Å) and IE (eV).
- Output file: `/app/outputs/C_N_convergence.dat`
- Format: tsv
- Contract: Two columns separated by a tab: vacuum_thickness (float, Å), IE (float, eV). No header row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/V_N_IE_15A.dat`
- `/app/outputs/C_N_IE_15A.dat`
- `/app/outputs/C_N_convergence.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### V_N_IE_15A.dat
- path: `/app/outputs/V_N_IE_15A.dat`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Ionization energy of the nitrogen vacancy at 15 Å vacuum.
- schema:
  - `type`: text
  - `description`: Single line containing a floating-point value representing the V_N ionization energy in eV.

### C_N_IE_15A.dat
- path: `/app/outputs/C_N_IE_15A.dat`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Ionization energy of the carbon-on-nitrogen substitution at 15 Å vacuum.
- schema:
  - `type`: text
  - `description`: Single line containing a floating-point value representing the C_N ionization energy in eV.

### C_N_convergence.dat
- path: `/app/outputs/C_N_convergence.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Convergence test: IE(C_N) computed at vacuum thicknesses 10, 20, and 30 Å; the IE values must not vary by more than 0.05 eV across rows.
- schema:
  - `type`: table
  - `required_columns`: `vacuum_thickness`, `IE`
  - `units`:
    - `vacuum_thickness`: Å
    - `IE`: eV

Notes: The first two artifacts are single-value floats compared to hidden reference values with a tolerance (±0.10 eV). The convergence table is checked for structural consistency (max variation ≤0.05 eV).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "V_N_IE_15A.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a floating-point value representing the V_N ionization energy in eV."
      },
      "description": "Ionization energy of the nitrogen vacancy at 15 Å vacuum."
    },
    {
      "file": "C_N_IE_15A.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a floating-point value representing the C_N ionization energy in eV."
      },
      "description": "Ionization energy of the carbon-on-nitrogen substitution at 15 Å vacuum."
    },
    {
      "file": "C_N_convergence.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "vacuum_thickness",
          "IE"
        ],
        "units": {
          "vacuum_thickness": "Å",
          "IE": "eV"
        }
      },
      "description": "Convergence test: IE(C_N) computed at vacuum thicknesses 10, 20, and 30 Å; the IE values must not vary by more than 0.05 eV across rows."
    }
  ],
  "notes": "The first two artifacts are single-value floats compared to hidden reference values with a tolerance (±0.10 eV). The convergence table is checked for structural consistency (max variation ≤0.05 eV)."
}
```

## How you are scored
A hidden verifier will inspect the three output files you write to `/app/outputs`. For the two single-value files (`V_N_IE_15A.dat` and `C_N_IE_15A.dat`), the verifier will compare your submitted ionization energy values against reference values derived from the method's published results. Your reward for each of these files depends on how closely your value agrees with the hidden reference. For the convergence table (`C_N_convergence.dat`), the verifier will check that the ionization energy varies very little across the reported vacuum thicknesses (structural audit of convergence), confirming that the charge correction effectively removes the divergence. The final reward is a weighted combination of the scores for the three artifacts, with the two ionization energies carrying the majority of the weight. You must generate all artifacts through the described DFT workflow; reporting numbers without executing the required calculations is not sufficient to achieve a high score.
