# Oxygen Binding Energy on Zr(0001): Coverage Dependence from DFT

## Problem background
Zirconium and its alloys are used in nuclear fuel cladding, where oxidation at the metal surface is a critical process. Understanding how oxygen binds to the Zr(0001) surface is essential for modelling corrosion. First-principles density-functional theory (DFT) can determine the energetics of oxygen adsorption on this surface. This task addresses the question: how does the binding energy of an oxygen atom at subsurface octahedral sites of Zr(0001) change with oxygen surface coverage?

## Approach
The work uses plane-wave DFT calculations with slab models of the Zr(0001) surface. Both the local-density approximation (LDA) and the Perdew-Wang 91 (PW91) gradient-corrected exchange-correlation functional are employed. For each functional, the clean Zr slab and an isolated oxygen atom serve as reference energies. Oxygen is placed at the octahedral subsurface site between the second and third Zr layers (site O(23)). Total-energy calculations are performed at three coverages (Θ = 1/4, 1/2, 1 monolayer) using appropriately sized supercells. The binding energy per oxygen atom is then computed as E_b = (E_slab(O) - E_clean_slab)/N_O - E_O_atom. The task is to perform these computations using an open-source plane-wave code (e.g., Quantum ESPRESSO) with public pseudopotentials, and to report the resulting binding energies so that the coverage dependence can be examined.

## Reproduction target
Compute the binding energy per oxygen atom (E_b) for the O(23) octahedral subsurface site on Zr(0001) at coverages Θ = 1/4 (using a 2×2 supercell), Θ = 1/2 (2×1), and Θ = 1 monolayer (1×1) using the PW91 functional. Additionally, compute E_b at Θ = 1/2 and 1 ML using the LDA functional. Report all E_b values in a JSON file named binding_energies.json with the exact structure specified in the output contract.

## Assets

- Quantum ESPRESSO (pw.x for single-point calculations): https://www.quantum-espresso.org/
- SSSP pseudopotentials for Zr and O (LDA and PW91): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Reference total-energy calculations
- Role: process
- Action: Construct clean 12-layer Zr(0001) slab models using the bulk hcp lattice parameters (LDA: a=3.158 Å, c/a=1.615; PW91: a=3.235 Å, c/a=1.605). Perform single-point DFT calculations with fixed in-plane lattice constants and a vacuum region of at least four interlayer spacings to obtain the total energy of the clean slab for each functional. Separately perform spin-polarized calculation for an isolated oxygen atom in a large supercell to obtain the oxygen reference energy, using the same functionals. Save the reference energies (E_clean_slab and E_O_atom for each functional) in a reference file.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 2: Binding energies for O(23) site at various coverages
- Role: scored (load-bearing)
- Action: For each combination of functional (PW91, LDA) and supercell corresponding to coverage (Θ=1/4 (2×2), Θ=1/2 (2×1), Θ=1 (1×1)), place a single oxygen atom at the octahedral subsurface site O(23) between the 2nd and 3rd Zr layers in an unrelaxed slab with fixed in-plane lattice constants. Perform single-point DFT calculations to obtain total energy E_slab(O). Compute the binding energy per oxygen atom using the formula E_b = (E_slab(O) - E_clean_slab)/N_O - E_O_atom, where N_O=1. Repeat for LDA only at Θ=1/2 and Θ=1. Output the binding energies in binding_energies.json with keys for each functional and coverage.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"PW91": {"1/4": E_b, "1/2": E_b, "1": E_b}, "LDA": {"1/2": E_b, "1": E_b}} where E_b are numeric values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed binding energies per oxygen atom for the O(23) subsurface site. The checker compares each value to a hidden reference with an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `PW91`:
      - `1/4`: number (eV)
      - `1/2`: number (eV)
      - `1`: number (eV)
    - `LDA`:
      - `1/2`: number (eV)
      - `1`: number (eV)

Notes: The agent must use open-source DFT code with appropriate pseudopotentials; the exact numerical values will differ slightly from the paper due to implementation differences. The hidden tolerance accounts for this spread. The reference energies from step_01 are not scored but are necessary for step_02.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "PW91": {
            "1/4": "number (eV)",
            "1/2": "number (eV)",
            "1": "number (eV)"
          },
          "LDA": {
            "1/2": "number (eV)",
            "1": "number (eV)"
          }
        }
      },
      "description": "Computed binding energies per oxygen atom for the O(23) subsurface site. The checker compares each value to a hidden reference with an absolute tolerance."
    }
  ],
  "notes": "The agent must use open-source DFT code with appropriate pseudopotentials; the exact numerical values will differ slightly from the paper due to implementation differences. The hidden tolerance accounts for this spread. The reference energies from step_01 are not scored but are necessary for step_02."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier independently inspects your binding_energies.json. It compares each reported binding energy to the known reference value (hidden) with an allowed absolute tolerance, and it also checks that the dependence on coverage is physically correct. The final reward is a weighted combination of these checks. Simply reporting a number is not sufficient; the values must result from the required DFT calculations and must pass the verifier's criteria.
