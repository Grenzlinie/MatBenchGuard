# First-principles calculation of structural, elastic, and optical properties of BiTeI

## Problem background
The ternary chalcohalides A⁵B⁶C⁷ (A = Sb, Bi; B = Te, Se, S; C = I, Br, Cl) are layered non‑centrosymmetric semiconductors with reported thermoelectric, ferroelectric, and strong Rashba spin‑splitting effects. Their structural, mechanical, electronic, and optical properties are of interest for spintronic and optoelectronic applications. This reproduction exercise targets one representative compound, BiTeI (trigonal P3m1), to compute several key physical quantities from first principles.

## Approach
Use density functional theory (DFT) within the generalized gradient approximation (GGA‑PBE) as implemented in the open‑source plane‑wave code Quantum ESPRESSO. The overall approach is: (1) perform variable‑cell geometry optimization of the BiTeI primitive cell to relax both lattice parameters and atomic positions; (2) compute the five independent second‑order elastic constants by applying small finite strains to the optimized structure; (3) calculate the electronic band structure on a high‑symmetry k‑point path (without spin‑orbit coupling) to obtain the indirect band gap; (4) compute the frequency‑dependent dielectric function (real and imaginary parts) via the random‑phase approximation and Kramers‑Kronig transform, and derive the energy‑loss function and optical sum‑rule quantities (effective number of valence electrons and effective optical dielectric constant). All calculations should be performed with PAW pseudopotentials from the standard PBE library. The final step aggregates the target numbers from the output of the preceding calculations.

## Reproduction target
For BiTeI (trigonal, space group P3m1), produce the following quantities and write them to `/app/outputs/results.json` as a JSON object with the exact keys listed in the output contract below: converged lattice constants a and c (Å); independent elastic constants C11, C12, C13, C33, C44 (GPa); the fundamental indirect electronic band gap (eV); the energies of the main peaks in ε₂ (imaginary part of the dielectric function) for light polarized along the x and z crystal axes; the energies of the main maxima in the energy‑loss function L(ω) for both polarizations; and the saturation energies (in eV) of the effective number of valence electrons N_eff and the effective optical dielectric constant ε_eff from the optical sum rules. All values are numbers; submit only the final aggregated JSON file.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSL or SSSP pseudopotentials for Bi, Te, I (PBE): https://pseudopotentials.quantum-espresso.org/
- Crystal structure of BiTeI: 10.1006/jssc.1995.1058

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of BiTeI to relax atom positions and lattice parameters, obtaining converged a and c lattice constants.
- Evidence: `/app/outputs/bitei_relaxed_structure.txt`

### Step 2: Elastic constants calculation
- Role: process
- Action: Calculate the second-order elastic constants (C11, C12, C13, C33, C44) for the optimized BiTeI using the finite-strain method.
- Evidence: `/app/outputs/elastic_constants.txt`

### Step 3: Band structure and indirect band gap
- Role: process
- Action: Compute the electronic band structure along high-symmetry k-path and extract the indirect band gap of BiTeI.
- Evidence: `/app/outputs/band_gap.dat`

### Step 4: Optical properties calculation
- Role: process
- Action: Calculate the frequency-dependent dielectric function (real and imaginary parts) and energy-loss function via Kramers-Kronig transform, then derive the effective number of valence electrons and effective dielectric constant from optical sum rules. Determine peak positions and saturation energies.
- Evidence: `/app/outputs/optical_properties.txt`

### Step 5: Aggregate all target results
- Role: scored (load-bearing)
- Action: Collect the target quantities from the completed calculations and write them to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys: lattice_a (number), lattice_c (number), C11 (number), C12 (number), C13 (number), C33 (number), C44 (number), band_gap (number), eps2_max_x (number), eps2_max_z (number), Lmax_x (number), Lmax_z (number), Neff_saturation_energy (number), epsilon_eff_saturation_energy (number).
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
- description: JSON file containing the reproduced values for all requested quantities for BiTeI.
- schema:
  - `type`: object
  - `required`:
    - `lattice_a`: number
    - `lattice_c`: number
    - `C11`: number
    - `C12`: number
    - `C13`: number
    - `C33`: number
    - `C44`: number
    - `band_gap`: number
    - `eps2_max_x`: number
    - `eps2_max_z`: number
    - `Lmax_x`: number
    - `Lmax_z`: number
    - `Neff_saturation_energy`: number
    - `epsilon_eff_saturation_energy`: number
  - `units`:
    - `lattice_a`: Å
    - `lattice_c`: Å
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `band_gap`: eV
    - `eps2_max_x`: eV
    - `eps2_max_z`: eV
    - `Lmax_x`: eV
    - `Lmax_z`: eV
    - `Neff_saturation_energy`: eV
    - `epsilon_eff_saturation_energy`: eV

Notes: The agent must execute all process steps and produce this result file; the checker will compare each value against hidden references with appropriate tolerances.

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
          "lattice_a": "number",
          "lattice_c": "number",
          "C11": "number",
          "C12": "number",
          "C13": "number",
          "C33": "number",
          "C44": "number",
          "band_gap": "number",
          "eps2_max_x": "number",
          "eps2_max_z": "number",
          "Lmax_x": "number",
          "Lmax_z": "number",
          "Neff_saturation_energy": "number",
          "epsilon_eff_saturation_energy": "number"
        },
        "units": {
          "lattice_a": "Å",
          "lattice_c": "Å",
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "band_gap": "eV",
          "eps2_max_x": "eV",
          "eps2_max_z": "eV",
          "Lmax_x": "eV",
          "Lmax_z": "eV",
          "Neff_saturation_energy": "eV",
          "epsilon_eff_saturation_energy": "eV"
        }
      },
      "description": "JSON file containing the reproduced values for all requested quantities for BiTeI."
    }
  ],
  "notes": "The agent must execute all process steps and produce this result file; the checker will compare each value against hidden references with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will examine each of your workflow stage artifacts, extract the required quantities, and compare them against a hidden reference. The final score (a float between 0 and 1) is a weighted combination of the scores from each stage, with the aggregated results in `results.json` carrying the most weight. Reporting the expected numbers without executing the actual workflow will not earn credit — all process steps must be completed and their evidence artifacts present.
