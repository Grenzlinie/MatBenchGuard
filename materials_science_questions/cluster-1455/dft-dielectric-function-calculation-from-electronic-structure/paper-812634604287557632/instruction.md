# Static Second-Harmonic Generation Susceptibility of GaAs from First-Principles DFT

## Problem background
Second-harmonic generation (SHG) is a nonlinear optical process in which a material irradiated by an intense laser beam emits light at twice the incident frequency. In crystals with no inversion symmetry, this response is described by the second-order nonlinear optical susceptibility tensor χ^(2). For cubic semiconductors such as zinc-blende GaAs, symmetry reduces this tensor to a single independent component, χ^(2)_{123}. First-principles band-structure calculations can predict χ^(2) from the electronic Bloch states, but accurate computation requires a careful treatment of the conduction bands, the momentum matrix elements between states, and a correction for the underestimation of the band gap in density-functional theory. This task focuses on computing the zero-frequency (static) limit χ^(2)(0) for the prototypical III-V semiconductor GaAs.

## Approach
The calculation follows a full band-structure sum-over-states approach. The electronic ground state of zinc-blende GaAs is obtained from a self-consistent density-functional theory (DFT) calculation within the local-density approximation (LDA). Because LDA systematically underestimates the fundamental band gap, a rigid “scissor” shift is applied to all conduction bands to match the known experimental gap. Momentum matrix elements between all relevant pairs of valence and conduction band states are then computed on a suitably dense k-point mesh in the irreducible wedge of the Brillouin zone. The static second-order susceptibility χ^(2)(0) is evaluated by performing a Brillouin-zone integral of the products of three matrix elements, weighted by the energy differences among the involved states, and expressed in units of 10^{-8} esu. The workflow uses the open-source plane-wave pseudopotential code Quantum ESPRESSO as the DFT engine.

## Reproduction target
Compute the static second-order nonlinear susceptibility χ^(2)(0) for zinc-blende GaAs using first-principles DFT-LDA with a scissor correction and a sum-over-states evaluation, and report the result (a single floating-point number) in units of 10^{-8} esu.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- LDA pseudopotentials for Ga and As (PZ81 functional): https://www.quantum-espresso.org/pseudopotentials
- Experimental band gap of GaAs at low temperature (1.52 eV)
- Crystal structure of zinc-blende GaAs

## Workflow steps

### Step 1: Self-consistent DFT calculation for GaAs
- Role: process
- Action: Perform a self-consistent DFT calculation for zinc-blende GaAs using LDA (PZ81) and the open-source Quantum ESPRESSO code. Converge the ground-state charge density and obtain Kohn-Sham eigenvalues and wavefunctions on a k-point mesh with 505 points in the irreducible wedge.
- Evidence: `/app/outputs/dft_scf.log`

### Step 2: Apply scissor correction to conduction bands
- Role: process
- Action: Rigidly shift all conduction band energies upward so that the fundamental direct gap matches the experimental value of 1.52 eV. Use the scissor-corrected energies for all subsequent steps.
- Evidence: `/app/outputs/scissor.log`

### Step 3: Compute momentum matrix elements
- Role: process
- Action: Calculate the momentum matrix elements P_{nm}(k) = -iħ ∫ ψ_n* ∇ ψ_m dr between all relevant valence and conduction band pairs at each k-point of the 505-point mesh. Store components for use in the susceptibility formula.
- Evidence: `/app/outputs/mme.log`

### Step 4: Compute static χ^(2)(0) for GaAs
- Role: scored (load-bearing)
- Action: Evaluate the static second-order nonlinear susceptibility χ^(2)(0) for the GaAs SHG tensor component χ_{123} using the sum-over-states expression with scissor-corrected energies, momentum matrix elements, and k-point mesh. Perform Brillouin-zone integration and write the result in units of 10^{-8} esu to the output file.
- Output file: `/app/outputs/chi2_zero_GaAs.txt`
- Format: txt
- Contract: A single line containing a floating-point number (e.g., 60.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi2_zero_GaAs.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi2_zero_GaAs.txt
- path: `/app/outputs/chi2_zero_GaAs.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Static second-order nonlinear susceptibility χ^(2)(0) for zinc-blende GaAs, reported as a single floating-point number in units of 10^{-8} esu.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: 10^{-8} esu

Notes: The checker reads the reported number, compares it to the hidden gold value (60 × 10^{-8} esu) with a tolerance of ±50%, and verifies it is positive. This accounts for method-dependent spread between OLCAO and Quantum ESPRESSO implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi2_zero_GaAs.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "10^{-8} esu"
        }
      },
      "description": "Static second-order nonlinear susceptibility χ^(2)(0) for zinc-blende GaAs, reported as a single floating-point number in units of 10^{-8} esu."
    }
  ],
  "notes": "The checker reads the reported number, compares it to the hidden gold value (60 × 10^{-8} esu) with a tolerance of ±50%, and verifies it is positive. This accounts for method-dependent spread between OLCAO and Quantum ESPRESSO implementations."
}
```

## How you are scored
Each workflow step produces an artifact that is inspected by a hidden verifier. The final scored output, `chi2_zero_GaAs.txt`, is compared to a hidden reference value derived from the literature. The reward is determined by how closely your reported χ^(2)(0) matches that reference, with a tolerance band that accounts for legitimate differences between DFT implementations. Full credit is awarded when the deviation falls within the tolerance band; larger deviations receive proportionally reduced credit. The intermediate process logs are checked for existence and basic consistency but carry negligible weight. Stating a numerically correct result without a corresponding computational pipeline will not satisfy the scoring requirements.
