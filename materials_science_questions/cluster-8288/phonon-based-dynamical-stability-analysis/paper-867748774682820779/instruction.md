# First-principles prediction of piezoelectric and topological quantum spin Hall insulator properties of Janus VCClBr monolayer

## Problem background
Two-dimensional (2D) materials that lack inversion symmetry can simultaneously exhibit piezoelectricity and nontrivial topological electronic order, forming a piezoelectric quantum spin Hall insulator (PQSHI). The Janus monolayer VCClBr, constructed by replacing one Cl layer of the centrosymmetric parent VCCl₂ with Br atoms, is proposed as a candidate for such multifunctional behavior. This task reproduces the first-principles predictions of its structural, elastic, electronic, piezoelectric, and topological properties, thereby testing whether the claimed coexistence of piezoelectricity and a nontrivial topological phase emerges from the calculations.

## Approach
The reproduction uses density functional theory (DFT) with a plane-wave/pseudopotential approach and the generalized gradient approximation (GGA), including spin–orbit coupling (SOC) for electronic and topological properties. The workflow proceeds through several stages: (1) construct the Janus VCClBr structure and relax the lattice constants and atomic positions to obtain the equilibrium geometry; (2) compute the phonon dispersion to assess dynamical stability; (3) perform a non-self-consistent electronic band structure calculation with SOC to determine the band gap; (4) extract the two-dimensional elastic constants from the stress–strain response under small deformations; (5) run density functional perturbation theory (DFPT) to obtain the piezoelectric stress coefficients, decomposed into electronic and ionic contributions; (6) derive the piezoelectric strain coefficients from the elastic constants and stress coefficients; (7) construct maximally localized Wannier functions and compute the Z₂ topological invariant via the evolution of Wannier charge centers. All calculations are performed with open-source tools (Quantum ESPRESSO, Phonopy, Wannier90, WannierTools) and suitable pseudopotentials for V, C, Cl, and Br.

## Reproduction target
Compute the following quantitative properties for the VCClBr monolayer and write them to a single JSON file at /app/outputs/results.json:
- relaxed lattice constants a and b (Å).
- GGA+SOC electronic band gap (meV).
- 2D elastic constants C11, C22, C12, C66 (N/m).
- piezoelectric stress coefficients e31 and e32 (10⁻¹⁰ C/m), along with their electronic and ionic contributions.
- derived piezoelectric strain coefficients d31 and d32 (pm/V).
- Z₂ topological invariant (0 or 1).
- a boolean indicating whether the phonon dispersion is dynamically stable (true if no imaginary modes).
The JSON schema and units are specified in the output contract. Every field must be present and correctly typed.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Wannier90: https://wannier.org/
- WannierTools: http://www.wanniertools.com/
- Pseudopotentials (V, C, Cl, Br): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Build the VCClBr Janus monolayer by replacing one Cl layer of VCCl₂ with Br atoms; relax lattice constants and atomic positions using DFT-GGA.
- Evidence: `/app/outputs/vcclbr_relaxed.out`

### Step 2: Phonon dispersion calculation
- Role: process
- Action: Compute the phonon band structure of the relaxed VCClBr monolayer using Phonopy (finite-displacement or DFPT) and verify the absence of imaginary modes.
- Evidence: `/app/outputs/phonon_band.dat`

### Step 3: Electronic band structure with spin-orbit coupling
- Role: process
- Action: Perform a non-self-consistent DFT calculation including spin-orbit coupling on the relaxed structure; extract the GGA+SOC band gap.
- Evidence: `/app/outputs/vcclbr_bands.dat`

### Step 4: Elastic constants
- Role: process
- Action: Apply small strain tensors to the relaxed cell, compute the stress tensor, and extract the 2D elastic constants C11, C22, C12, C66 renormalized by the vacuum thickness.
- Evidence: `/app/outputs/elastic.out`

### Step 5: Piezoelectric stress coefficients via DFPT
- Role: process
- Action: Run density functional perturbation theory (DFPT) to obtain the clamped-ion and relaxed-ion piezoelectric stress tensors; extract e31 and e32 (total, electronic, ionic contributions).
- Evidence: `/app/outputs/piezo.out`

### Step 6: Wannierisation and Z2 invariant
- Role: process
- Action: Construct maximally localized Wannier functions from the DFT wavefunctions (V d-orbitals, C/Cl/Br p-orbitals) using Wannier90; compute the evolution of Wannier charge centers with WannierTools and determine the Z2 topological invariant.
- Evidence: `/app/outputs/wannier90.wout`

### Step 7: Collect and report all target properties
- Role: scored (load-bearing)
- Action: Gather the computed lattice constants a and b (Å), GGA+SOC band gap (meV), elastic constants C11, C22, C12, C66 (N/m), piezoelectric stress coefficients e31, e32 (total, electronic, ionic) in units of 10⁻¹⁰ C/m, derived strain coefficients d31, d32 (pm/V), Z2 invariant (0 or 1), and a boolean indicating phonon stability (true if no imaginary modes). Write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": {"lattice_constant_a": "float", "lattice_constant_b": "float", "band_gap_SOC": "float", "C11": "float", "C22": "float", "C12": "float", "C66": "float", "e31": "float", "e31_electronic": "float", "e31_ionic": "float", "e32": "float", "e32_electronic": "float", "e32_ionic": "float", "d31": "float", "d32": "float", "Z2": "int", "phonon_stable": "bool"}, "units": {"lattice_constant_a": "Å", "lattice_constant_b": "Å", "band_gap_SOC": "meV", "C11": "N/m", "C22": "N/m", "C12": "N/m", "C66": "N/m", "e31": "10⁻¹⁰ C/m", "e31_electronic": "10⁻¹⁰ C/m", "e31_ionic": "10⁻¹⁰ C/m", "e32": "10⁻¹⁰ C/m", "e32_electronic": "10⁻¹⁰ C/m", "e32_ionic": "10⁻¹⁰ C/m", "d31": "pm/V", "d32": "pm/V"}}
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
- target_policy: threshold_or_better
- description: Single JSON file containing all the computed properties of the VCClBr monolayer that are compared against hidden paper-reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_a`: float
    - `lattice_constant_b`: float
    - `band_gap_SOC`: float
    - `C11`: float
    - `C22`: float
    - `C12`: float
    - `C66`: float
    - `e31`: float
    - `e31_electronic`: float
    - `e31_ionic`: float
    - `e32`: float
    - `e32_electronic`: float
    - `e32_ionic`: float
    - `d31`: float
    - `d32`: float
    - `Z2`: int
    - `phonon_stable`: bool
  - `units`:
    - `lattice_constant_a`: Å
    - `lattice_constant_b`: Å
    - `band_gap_SOC`: meV
    - `C11`: N/m
    - `C22`: N/m
    - `C12`: N/m
    - `C66`: N/m
    - `e31`: 10⁻¹⁰ C/m
    - `e31_electronic`: 10⁻¹⁰ C/m
    - `e31_ionic`: 10⁻¹⁰ C/m
    - `e32`: 10⁻¹⁰ C/m
    - `e32_electronic`: 10⁻¹⁰ C/m
    - `e32_ionic`: 10⁻¹⁰ C/m
    - `d31`: pm/V
    - `d32`: pm/V

Notes: The checker compares each field individually to the paper's Table I and Table II values using per-field tolerances; Z2 must be exactly 1 and phonon_stable must be true. Directional metrics follow threshold_or_better logic.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_a": "float",
          "lattice_constant_b": "float",
          "band_gap_SOC": "float",
          "C11": "float",
          "C22": "float",
          "C12": "float",
          "C66": "float",
          "e31": "float",
          "e31_electronic": "float",
          "e31_ionic": "float",
          "e32": "float",
          "e32_electronic": "float",
          "e32_ionic": "float",
          "d31": "float",
          "d32": "float",
          "Z2": "int",
          "phonon_stable": "bool"
        },
        "units": {
          "lattice_constant_a": "Å",
          "lattice_constant_b": "Å",
          "band_gap_SOC": "meV",
          "C11": "N/m",
          "C22": "N/m",
          "C12": "N/m",
          "C66": "N/m",
          "e31": "10⁻¹⁰ C/m",
          "e31_electronic": "10⁻¹⁰ C/m",
          "e31_ionic": "10⁻¹⁰ C/m",
          "e32": "10⁻¹⁰ C/m",
          "e32_electronic": "10⁻¹⁰ C/m",
          "e32_ionic": "10⁻¹⁰ C/m",
          "d31": "pm/V",
          "d32": "pm/V"
        }
      },
      "description": "Single JSON file containing all the computed properties of the VCClBr monolayer that are compared against hidden paper-reported values with tolerances."
    }
  ],
  "notes": "The checker compares each field individually to the paper's Table I and Table II values using per-field tolerances; Z2 must be exactly 1 and phonon_stable must be true. Directional metrics follow threshold_or_better logic."
}
```

## How you are scored
A hidden verifier reads /app/outputs/results.json and compares each field independently to a set of hidden reference values. Numeric fields are compared with tolerances that absorb the typical spread between different DFT implementations and settings; meeting or exceeding the reference for a directional metric (e.g., a smaller structural deviation or a larger gap) is treated as at least as good as matching within tolerance, so a better-than-paper result is never penalized. The Z₂ invariant and the phonon stability boolean require exact agreement. Per-field scores are averaged to produce a final reward between 0 and 1. Only the correctness and completeness of results.json matter; intermediate artifacts are not scored.
