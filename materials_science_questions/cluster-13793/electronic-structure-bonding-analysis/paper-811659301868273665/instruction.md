# Reproduce DFT calculations of structural, electronic, and magnetic properties of ThCr2Si2

## Problem background
The tetragonal compound ThCr2Si2 (space group I4/mmm) crystallizes in a body‑centered structure that serves as the archetype for the vast family of 122‑like ternary phases, which includes many iron‑based superconductors. Despite its structural importance, the magnetic ground state, elastic moduli, and electronic structure of ThCr2Si2 itself have not been systematically determined. First‑principles density functional theory calculations can provide missing reference data for this prototype system by predicting its structural parameters, magnetic ordering, bulk modulus, and density of states. This task asks you to perform these calculations and report the key computed quantities.

## Approach
Using spin‑polarized density functional theory (DFT) with the generalized gradient approximation (PBE), model the body‑centered tetragonal unit cell of ThCr2Si2 (Th 2a, Cr 4d, Si 4e). Consider five collinear magnetic arrangements: non‑magnetic (NM), ferromagnetic (FM), and three in‑plane antiferromagnetic patterns (AFM1, AFM2, AFM3) that differ in the relative alignments of Cr spins within and between [Cr2Si2] slabs. For each configuration, fully relax the lattice vectors and internal coordinates using a plane‑wave DFT code and appropriate pseudopotentials. From the relaxed outputs, extract the total energy per formula unit and the magnetic moments on the chromium atoms. Identify the magnetic ground state as the configuration with the lowest total energy. On this ground‑state phase, compute the six independent elastic constants (C11, C12, C13, C33, C44, C66) by applying small finite strains (±1%) and fitting the resulting stress tensors, then derive the Voigt–Reuss–Hill bulk modulus. Perform an additional self‑consistent calculation for the ground state to obtain the total density of states and extract its value at the Fermi level.

## Reproduction target
Produce a single JSON file `results.json` containing the following quantities:

1. **Total‑energy differences** ΔE (eV per formula unit) of the NM, FM, AFM1, AFM2, and AFM3 configurations relative to the most stable magnetic phase (set ΔE = 0 for that phase).
2. **Chromium magnetic moments** (μB) for FM, AFM1 (as a two‑element list when the two Cr sites are inequivalent), AFM2, and AFM3.
3. **Optimized lattice constants** a and c (Å) of the most stable magnetic phase.
4. **Voigt–Reuss–Hill bulk modulus** B_VRH (GPa) of the most stable magnetic phase.
5. **Total density of states at the Fermi level** N(E_F) (states per eV per formula unit) for the most stable magnetic phase.

All values must be reported in the specified units. The JSON structure must conform to the output contract described below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT relaxations for five magnetic configurations
- Role: process
- Action: Perform spin-polarized density functional theory (DFT) calculations using the GGA-PBE exchange-correlation functional for tetragonal ThCr2Si2 (space group I4/mmm, atomic positions: Th 2a (0,0,0), Cr 4d (0,0.5,0.25), Si 4e (0,0,z_Si) with an initial z_Si ≈ 0.38). Consider five collinear magnetic configurations: non-magnetic (NM), ferromagnetic (FM), and three in-plane antiferromagnetic patterns (AFM1, AFM2, AFM3). In AFM1, Cr spins are ferromagnetically ordered within each [Cr2Si2] block and antiferromagnetically coupled between adjacent blocks. In AFM2, each [Cr2Si2] block contains chains of antiparallel Cr spins, ferromagnetically coupled, with antiferromagnetic coupling between blocks. In AFM3 (stripe-like), each [Cr2Si2] block contains chains of parallel Cr spins that are antiferromagnetically coupled, and adjacent blocks are also antiferromagnetically coupled. For each configuration, fully relax both atomic positions and lattice vectors until forces and pressure are converged according to the codes default criteria. After relaxation, extract the total energy (in eV per formula unit) and the magnetic moments on Cr atoms (in μB) from the output.
- Evidence: `/app/outputs/relax_outputs`

### Step 2: Elastic constants and bulk modulus for AFM3
- Role: process
- Action: Using the relaxed atomic structure of the AFM3 magnetic phase from step_01, compute the six independent elastic stiffness constants C11, C12, C13, C33, C44, C66 by applying a set of small finite deformations (e.g., ±1% strain) to the lattice and calculating the resulting stress tensors via DFT. Fit the stress‑strain relationship to extract the Cij values. From these constants, derive the Voigt–Reuss–Hill (VRH) bulk modulus B_VRH (in GPa) using the Voigt, Reuss, and Hill averaging formulas.
- Evidence: `/app/outputs/elastic_output`

### Step 3: Electronic density of states for AFM3
- Role: process
- Action: Perform a self-consistent field (SCF) calculation for the relaxed AFM3 structure to obtain the charge density and wavefunctions. Then compute the total density of states (DOS) using a suitable post-processing tool (e.g., dos.x). Extract the value of the total DOS at the Fermi level, N(E_F), expressed in states per eV per formula unit.
- Evidence: `/app/outputs/dos_output`

### Step 4: Collect and report all computed quantities
- Role: scored (load-bearing)
- Action: Parse the outputs from step_01, step_02, and step_03 and write the following quantities into a single JSON file named results.json: (1) the total‑energy differences ΔE (in eV per formula unit) for NM, FM, AFM1, AFM2, and AFM3 relative to AFM3, with AFM3 ΔE set to 0; (2) the Cr magnetic moments (in μB) for FM, AFM1 (as a two‑element list giving the moments for the two inequivalent Cr atoms when they differ), AFM2, and AFM3; (3) the optimized lattice constants a and c (in Å) for the AFM3 phase; (4) the VRH bulk modulus B_VRH (in GPa) for the AFM3 phase; and (5) the total DOS at the Fermi level N(E_F) (in states per eV per formula unit) for the AFM3 phase.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["delta_E", "magnetic_moments", "lattice_constants_AFM3", "bulk_modulus_AFM3", "dos_at_fermi_total"], "delta_E": {"type": "object", "required": ["NM", "FM", "AFM1", "AFM2", "AFM3"]}, "magnetic_moments": {"type": "object", "required": ["FM", "AFM1", "AFM2", "AFM3"], "AFM1": "array of two numbers"}, "lattice_constants_AFM3": {"type": "object", "required": ["a", "c"]}, "bulk_modulus_AFM3": "number", "dos_at_fermi_total": "number"}
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
- target_policy: reference_match
- description: Aggregated results from DFT calculations: energy differences, magnetic moments, AFM3 lattice constants, bulk modulus, and DOS at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `delta_E`: object containing keys NM, FM, AFM1, AFM2, AFM3, each a numeric value in eV/f.u.
    - `magnetic_moments`: object containing keys FM (number), AFM1 (array of two numbers), AFM2 (number), AFM3 (number); all in μB
    - `lattice_constants_AFM3`: object with keys a and c, both numbers in Å
    - `bulk_modulus_AFM3`: number, in GPa
    - `dos_at_fermi_total`: number, in states/eV per formula unit
  - `notes`: All numeric fields must be finite and match the described units. The JSON structure must exactly follow the required keys.

Notes: The checker will compare each numeric entry in results.json against hidden reference values derived from the paper, with appropriate tolerances that account for the use of a different DFT code (Quantum ESPRESSO vs. VASP) and pseudopotential library. All values are to be reported in the units specified.

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
          "delta_E": "object containing keys NM, FM, AFM1, AFM2, AFM3, each a numeric value in eV/f.u.",
          "magnetic_moments": "object containing keys FM (number), AFM1 (array of two numbers), AFM2 (number), AFM3 (number); all in μB",
          "lattice_constants_AFM3": "object with keys a and c, both numbers in Å",
          "bulk_modulus_AFM3": "number, in GPa",
          "dos_at_fermi_total": "number, in states/eV per formula unit"
        },
        "notes": "All numeric fields must be finite and match the described units. The JSON structure must exactly follow the required keys."
      },
      "description": "Aggregated results from DFT calculations: energy differences, magnetic moments, AFM3 lattice constants, bulk modulus, and DOS at the Fermi level."
    }
  ],
  "notes": "The checker will compare each numeric entry in results.json against hidden reference values derived from the paper, with appropriate tolerances that account for the use of a different DFT code (Quantum ESPRESSO vs. VASP) and pseudopotential library. All values are to be reported in the units specified."
}
```

## How you are scored
A hidden verifier inspects your `results.json` and compares each numerical entry against reference values derived from the original work. The overall score is a weighted combination of agreement across the different physical quantities: energy differences, magnetic moments, lattice constants, bulk modulus, and Fermi‑level density of states. Each quantity is judged with appropriate tolerances that account for the use of a different DFT code and pseudopotential library. Simply reporting the reference numbers is not sufficient; the verifier checks that your computed values are physically consistent and derive from a genuine execution of the workflow.
