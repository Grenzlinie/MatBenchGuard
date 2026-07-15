# DMAREL Crystal Structure Relaxation for Urea

## Problem background
The crystal packing of organic molecules governs properties such as solubility and bioavailability. Predicting the structures of polar and hydrogen-bonded crystals remains difficult because conventional isotropic atom‑atom potentials fail to capture the anisotropy of electrostatic interactions, including hydrogen bonding. This task investigates whether a realistic distributed multipole electrostatic model, combined with simple transferable repulsion‑dispersion potentials, can accurately relax a crystal structure and reproduce experimental lattice parameters. The target molecule is urea, a small hydrogen-bonded crystal with well-characterized packing. The goal is to compute the relaxed unit cell dimensions and lattice energy by implementing the DMAREL methodology.

## Approach
The DMAREL algorithm treats molecules as rigid bodies. The crystal structure is described by the center‑of‑mass positions and orientations (using quaternion rotations) of each molecule in the unit cell, plus six strain matrix elements that optimise the cell geometry. The intermolecular energy consists of two parts:
- Electrostatic interactions: a distributed multipole model up to hexadecapole at every atomic site, obtained from a distributed multipole analysis (DMA) of an ab initio wavefunction.
- Repulsion‑dispersion interactions: Buckingham (6‑exp) potentials with parameters for homonuclear contacts and fitted values for polar‑hydrogen interactions (C/N/O…Hp).

Lattice energy and its analytic first and second derivatives with respect to all structural variables are calculated. Long‑range charge‑charge, charge‑dipole, and dipole‑dipole terms are handled by Ewald summation; all higher multipole terms and the repulsion‑dispersion interactions use a direct summation cutoff of 20 Å. A Newton‑Raphson minimiser relaxes the structure starting from the experimental geometry. The required steps are:
1. Prepare the experimental urea crystal structure with standardised bond lengths.
2. Compute the distributed multipole moments from a Hartree‑Fock SCF calculation (6‑31G** basis) and DMA.
3. Implement the lattice energy model and minimiser to obtain the relaxed cell parameters and lattice energy.

## Reproduction target
Compute the fully relaxed unit cell dimensions (a, b, c, α, β, γ, in Å and degrees) and the static lattice energy U_r (in kJ mol⁻¹) for the hydrogen-bonded crystal urea using the DMAREL methodology described above. Use the distributed multipole moments derived from a 6‑31G** wavefunction and the repulsion‑dispersion parameters provided in the task. Report the results in the file `urea_relaxed_params.json`.

## Assets

- Experimental crystal structure of urea: 10.1107/S0108768109011201
- Open-source quantum chemistry package (e.g., PySCF, Psi4): pyscf

## Workflow steps

### Step 1: Prepare urea crystal structure
- Role: process
- Action: Obtain the experimental crystal structure of urea (CSD refcode UREAXX09 or equivalent from Crystallography Open Database) and standardize intramolecular C-H bond lengths to 1.08 Å and N-H bond lengths to 1.01 Å. Extract unit cell parameters, space group, and fractional coordinates of all atoms.
- Evidence: `/app/outputs/urea_initial_structure.cif`

### Step 2: Compute distributed multipole moments for urea
- Role: process
- Action: Perform a Hartree-Fock self-consistent field calculation on the isolated urea molecule using the 6-31G** basis set. Run a distributed multipole analysis (DMA) to obtain atomic multipole moments (charge, dipole, quadrupole, etc.) up to hexadecapole at each atomic site. Store the moments in a suitable format.
- Evidence: `/app/outputs/urea_dma_moments.json`

### Step 3: Minimize lattice energy using DMAREL algorithm
- Role: scored (load-bearing)
- Action: Implement the DMAREL lattice energy model: define the intermolecular energy as a sum of multipole-multipole interactions up to hexadecapole and repulsion-dispersion interactions using the Buckingham potential parameters (C...C, H...H, N...N, O...O, and the fitted C/N/O…Hp values from the paper). Compute the lattice energy and its first and second derivatives with respect to the structural variables (center-of-mass positions, molecular orientations, and six strain matrix elements) as described in the paper. Use a Newton-Raphson minimiser to relax the urea crystal structure starting from the prepared experimental geometry. Apply Ewald summation for charge-charge, charge-dipole, and dipole-dipole terms, and a direct cutoff of 20 Å for the remaining multipole and repulsion-dispersion contributions. Output the relaxed cell parameters and lattice energy.
- Output file: `/app/outputs/urea_relaxed_params.json`
- Format: json
- Contract: JSON object with keys: a (float, Å), b (float, Å), c (float, Å), alpha (float, deg), beta (float, deg), gamma (float, deg), U_r (float, kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/urea_relaxed_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### urea_relaxed_params.json
- path: `/app/outputs/urea_relaxed_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed unit cell parameters (a, b, c, alpha, beta, gamma) and lattice energy (U_r) for urea from the DMAREL minimization. All angles in degrees, cell lengths in Å, energy in kJ/mol.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `b`: float
    - `c`: float
    - `alpha`: float
    - `beta`: float
    - `gamma`: float
    - `U_r`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `alpha`: deg
    - `beta`: deg
    - `gamma`: deg
    - `U_r`: kJ/mol

Notes: The relaxed parameters will be compared to hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "urea_relaxed_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "b": "float",
          "c": "float",
          "alpha": "float",
          "beta": "float",
          "gamma": "float",
          "U_r": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "alpha": "deg",
          "beta": "deg",
          "gamma": "deg",
          "U_r": "kJ/mol"
        }
      },
      "description": "Relaxed unit cell parameters (a, b, c, alpha, beta, gamma) and lattice energy (U_r) for urea from the DMAREL minimization. All angles in degrees, cell lengths in Å, energy in kJ/mol."
    }
  ],
  "notes": "The relaxed parameters will be compared to hidden reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage. For the scored artifact `urea_relaxed_params.json`, the verifier compares your reported cell parameters and lattice energy to hidden reference values, using tolerances that accommodate reasonable implementation differences. The final reward is a weighted combination of the stage scores. Providing a plausible final number without completing the required intermediate process steps (structure preparation and DMA computation) will not earn full credit.
