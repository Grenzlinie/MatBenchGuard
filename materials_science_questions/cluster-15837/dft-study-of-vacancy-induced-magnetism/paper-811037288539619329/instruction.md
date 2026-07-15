# DFT study of substitutionally doped monolayer arsenene: electronic and magnetic properties

## Problem background
Monolayer arsenene, a two-dimensional buckled honeycomb structure of arsenic, has attracted attention as a semiconductor with potential applications in nanoelectronics and spintronics. Its electronic properties can be tuned by substitutional doping—replacing some arsenic atoms with impurity atoms. This task focuses on the effects of gallium (Ga) and germanium (Ge) dopants on the electronic band structure and magnetic properties of monolayer arsenene. Understanding how these dopants modify the band gap, the gap type, and the magnetic state is key to designing arsenene-based devices.

## Approach
Use spin-polarized density functional theory (DFT) with the generalized gradient approximation (GGA) and the Perdew-Burke-Ernzerhof (PBE) functional. Model a 4×4×1 supercell of β-arsenene (32 As atoms) with the known lattice constant a=3.55 Å and initial buckle height h=1.408 Å. First, relax the pristine supercell and compute its band gap as a baseline. Then, for each dopant (Ga, Ge), replace one As atom in the supercell, relax the geometry, and carry out electronic structure and magnetic moment calculations. Use spin polarization throughout. For Ge-doped arsenene, additionally perform a population analysis to extract the atomic magnetic moment on the Ge atom. All calculations must be performed with the open-source Quantum ESPRESSO code and appropriate pseudopotentials.

## Reproduction target
Compute the following scalar quantities from the fully relaxed doped supercells and save them in JSON format as specified in the workflow steps:
- For As₃₁Ga: the band gap (Eg, in eV), the gap type (direct or indirect), and the total magnetic moment (μB).
- For As₃₁Ge: the total magnetic moment (μB), the spin-up band gap (eV), the spin-down band gap (eV), and the magnetic moment on the Ge atom (μB).
The pristine supercell calculations are for your own validation and do not contribute directly to the score.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE) for As, Ga, Ge: https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Build and relax pristine As32 supercell
- Role: process
- Action: Construct a 4×4×1 supercell of buckled β-arsenene using lattice constant a=3.55 Å and initial buckle height h=1.408 Å. Perform spin-polarized DFT geometry optimization (GGA-PBE) to relax atomic positions until forces are below a standard threshold. Save the relaxed structure as evidence.
- Evidence: `/app/outputs/as32_relaxed.xyz`

### Step 2: Compute pristine electronic properties
- Role: process
- Action: Using the relaxed pristine supercell, run a single-point spin-polarized DFT calculation with a dense k-point grid to compute the band structure. Extract the band gap and verify it is indirect and the system is non-magnetic. Write the gap value to a text file as evidence.
- Evidence: `/app/outputs/pristine_gap.txt`

### Step 3: Build and relax As31Ga doped supercell
- Role: process
- Action: Create a doped supercell by replacing one As atom with Ga (site 1). Perform spin-polarized DFT geometry optimization with initial zero magnetic moments. Save the relaxed As31Ga structure as evidence.
- Evidence: `/app/outputs/as31ga_relaxed.xyz`

### Step 4: Compute As31Ga electronic properties
- Role: scored
- Action: Carry out a spin-polarized electronic structure calculation on the relaxed As31Ga supercell. Determine the band gap (Eg), the gap type (direct or indirect), and the total magnetic moment. Write the results to as31ga_properties.json with the keys Eg (eV), Eg_type (string), magnetic_moment (μB).
- Output file: `/app/outputs/as31ga_properties.json`
- Format: json
- Contract: {"Eg": <float>, "Eg_type": <string>, "magnetic_moment": <float>}
- Scoring: scored by hidden verifier

### Step 5: Build and relax As31Ge doped supercell
- Role: process
- Action: Create a doped supercell with one Ge replacing As (site 1). Perform spin-polarized DFT geometry optimization with an initial magnetic moment to encourage spin polarization. Save the relaxed As31Ge structure as evidence.
- Evidence: `/app/outputs/as31ge_relaxed.xyz`

### Step 6: Compute As31Ge electronic properties
- Role: scored (load-bearing)
- Action: Carry out a spin-polarized electronic structure calculation on relaxed As31Ge and perform a population analysis to obtain atomic magnetic moments. Extract total magnetic moment, spin-up band gap, spin-down band gap, and magnetic moment on the Ge atom. Write the results to as31ge_properties.json with keys total_moment (μB), Eg_up (eV), Eg_down (eV), Ge_moment (μB).
- Output file: `/app/outputs/as31ge_properties.json`
- Format: json
- Contract: {"total_moment": <float>, "Eg_up": <float>, "Eg_down": <float>, "Ge_moment": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/as31ga_properties.json`
- `/app/outputs/as31ge_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### as31ga_properties.json
- path: `/app/outputs/as31ga_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored electronic and magnetic properties of As31Ga (band gap, gap type, total magnetic moment).
- schema:
  - `type`: object
  - `required`:
    - `Eg`: number (eV)
    - `Eg_type`: string
    - `magnetic_moment`: number (μB)

### as31ge_properties.json
- path: `/app/outputs/as31ge_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored electronic and magnetic properties of As31Ge (total moment, spin-resolved band gaps, atomic moment on Ge).
- schema:
  - `type`: object
  - `required`:
    - `total_moment`: number (μB)
    - `Eg_up`: number (eV)
    - `Eg_down`: number (eV)
    - `Ge_moment`: number (μB)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "as31ga_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Eg": "number (eV)",
          "Eg_type": "string",
          "magnetic_moment": "number (μB)"
        }
      },
      "description": "Scored electronic and magnetic properties of As31Ga (band gap, gap type, total magnetic moment)."
    },
    {
      "file": "as31ge_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_moment": "number (μB)",
          "Eg_up": "number (eV)",
          "Eg_down": "number (eV)",
          "Ge_moment": "number (μB)"
        }
      },
      "description": "Scored electronic and magnetic properties of As31Ge (total moment, spin-resolved band gaps, atomic moment on Ge)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `as31ga_properties.json` and `as31ge_properties.json` files and compare the reported values against reference results. Each scored artifact carries a weight, and the final reward (a number between 0 and 1) is derived from the accuracy of your reported quantities, allowing for reasonable tolerances that absorb numerical differences from code and pseudopotential choices. The verifier does not inspect intermediate files. You must execute the computational workflow as described; simply reporting the expected values without running the calculations will not succeed because the verifier checks against hidden reference values that you do not know.
