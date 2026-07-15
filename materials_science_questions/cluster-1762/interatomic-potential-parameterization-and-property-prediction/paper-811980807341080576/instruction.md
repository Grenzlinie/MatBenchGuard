# Zeroth-order vacancy migration energy calculations for alkali halides using Born-Mayer potential

## Problem background
The mobility of ions in alkali halide crystals is governed by the energy barriers, or activation energies, for vacancy migration. Reliable predictions of these barriers are important for understanding ionic conductivity and diffusion. This work presents a simplified, zeroth-order computational approach that avoids costly lattice relaxation: it estimates migration energies for cations and anions moving via single vacancies and via vacancy pairs, using only a repulsive potential and a continuum treatment of the surrounding lattice.

## Approach
The energy of a defect configuration is computed using the Mott-Littleton continuum approximation. Ions near the defect are treated explicitly, while the rest of the crystal is replaced by a polarizable dielectric continuum. All ion-ion repulsion is modeled with a Born-Mayer potential whose parameters (decay length ρ and pre-factor b) are fixed to values commonly used for alkali halides.

For the ground state, every ion occupies a perfect rock-salt lattice site. For the saddle-point, the following configurations are used:
- Cation single vacancy jump: place the jumping cation at the midpoint between two nearest-neighbor cation sites along [110]. Displace the two nearest anions outward along the lines from the midpoint to each anion until the distance from the jumping cation to each anion equals 0.85 r0. All other ions remain at lattice sites.
- Anion single vacancy jump: similarly, place the jumping anion at the midpoint between two nearest-neighbor anion sites along [110]; displace the two nearest cations to 0.85 r0.
- Cation vacancy pair jump: one of the two nearest anion sites adjacent to the midpoint is vacant (the anion vacancy of the pair). Displace the remaining anion to 0.85 r0 from the jumping cation; all other ions (except the vacant site) remain at lattice sites.
- Anion vacancy pair jump: one of the two nearest cation sites is vacant; displace the remaining cation to 0.85 r0. No additional lattice relaxation is performed. The activation (migration) energy for a given type of jump is the difference between the computed saddle-point energy and the ground-state energy. The same energy expressions also yield formation energies of a vacancy pair and of a Schottky pair, from which diffusion activation energies can be derived. The calculations are repeated for a set of 16 alkali halides covering the Li, Na, K, and Rb families with F, Cl, Br, and I anions.

## Reproduction target
Implement the zeroth-order calculation method and compute migration (activation) energies for cation and anion movement via single vacancies and via vacancy pairs for all 16 compounds: LiF, LiCl, LiBr, LiI, NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI, RbF, RbCl, RbBr, RbI.  Additionally, compute defect formation and diffusion activation energies for NaCl using the same method.

Write the 16-compound results as a CSV with exactly the columns: compound, cation_single, anion_single, cation_pair, anion_pair (all energies in eV).  Write the NaCl-specific results as a second CSV with exactly the columns: formation_vacancy_pair, formation_schottky_pair, diffusion_vacancy_pair, diffusion_anion_vacancy (all in eV).  Both files must be placed under `/app/outputs`.

## Assets

- Alkali halide material parameters (r0, ionic radii, TKS polarizabilities) from Kittel 1968
- Python programming environment with numerical capabilities: python3, numpy

## Workflow steps

### Step 1: Parameter assembly
- Role: process
- Action: Assemble the physical constants (r0, ionic radii, TKS polarizabilities) for the 16 alkali halides from Kittel (1968) or equivalent public references. Adopt the Born-Mayer repulsive potential parameters (ρ=0.345 Å, b=0.1429 eV).
- Evidence: none

### Step 2: Compute activation energies for 16 alkali halides
- Role: scored (load-bearing)
- Action: Implement the zeroth-order method: for each of the 16 alkali halides (LiF, LiCl, LiBr, LiI, NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI, RbF, RbCl, RbBr, RbI), compute defect ground-state and saddle-point energies using the Mott-Littleton continuum approximation and the specified displacement rule. The saddle-point configurations are:
- Cation single vacancy jump: place the jumping cation at the midpoint between two nearest-neighbor cation sites along [110]; displace the two nearest anions outward until the distance equals 0.85 r0.
- Anion single vacancy jump: place the jumping anion at the midpoint between two nearest-neighbor anion sites along [110]; displace the two nearest cations to 0.85 r0.
- Cation vacancy pair jump: one of the two nearest anion sites adjacent to the midpoint is vacant (the anion vacancy of the pair); displace the remaining anion to 0.85 r0.
- Anion vacancy pair jump: one of the two nearest cation sites is vacant; displace the remaining cation to 0.85 r0.
No lattice relaxation is performed. Calculate activation energies (migration energies) as the difference between saddle-point and ground-state energies for cation and anion via single vacancies and vacancy pairs.
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: CSV with columns: compound (string), cation_single (float, eV), anion_single (float, eV), cation_pair (float, eV), anion_pair (float, eV). 16 rows.
- Scoring: scored by hidden verifier

### Step 3: Compute NaCl defect formation and diffusion activation energies
- Role: scored
- Action: Using the same zeroth-order method and parameters, compute formation energies of a vacancy pair and a Schottky pair in NaCl. Then, using the NaCl migration energies from step_02, derive activation energies for diffusion via vacancy pairs (formation energy of vacancy pair + anion migration via vacancy pair) and for diffusion of anion vacancies (half the Schottky formation energy + anion migration via single vacancy).
- Output file: `/app/outputs/nacl_diffusion_energies.csv`
- Format: csv
- Contract: CSV with columns: formation_vacancy_pair (float, eV), formation_schottky_pair (float, eV), diffusion_vacancy_pair (float, eV), diffusion_anion_vacancy (float, eV). Single row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.csv`
- `/app/outputs/nacl_diffusion_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Activation energies for cation and anion migration via single vacancies and vacancy pairs for 16 alkali halides.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `cation_single`, `anion_single`, `cation_pair`, `anion_pair`
  - `units`:
    - `cation_single`: eV
    - `anion_single`: eV
    - `cation_pair`: eV
    - `anion_pair`: eV

### nacl_diffusion_energies.csv
- path: `/app/outputs/nacl_diffusion_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Defect formation and diffusion activation energies for NaCl.
- schema:
  - `type`: table
  - `required_columns`: `formation_vacancy_pair`, `formation_schottky_pair`, `diffusion_vacancy_pair`, `diffusion_anion_vacancy`
  - `units`:
    - `formation_vacancy_pair`: eV
    - `formation_schottky_pair`: eV
    - `diffusion_vacancy_pair`: eV
    - `diffusion_anion_vacancy`: eV

Notes: The checker compares each activation energy value to hidden reference values from the paper's Table 1 with an absolute tolerance. For NaCl diffusion energies, each value is compared to the paper's reported numbers (1.55, 2.35, 2.57, 2.37 eV) with a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "cation_single",
          "anion_single",
          "cation_pair",
          "anion_pair"
        ],
        "units": {
          "cation_single": "eV",
          "anion_single": "eV",
          "cation_pair": "eV",
          "anion_pair": "eV"
        }
      },
      "description": "Activation energies for cation and anion migration via single vacancies and vacancy pairs for 16 alkali halides."
    },
    {
      "file": "nacl_diffusion_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "formation_vacancy_pair",
          "formation_schottky_pair",
          "diffusion_vacancy_pair",
          "diffusion_anion_vacancy"
        ],
        "units": {
          "formation_vacancy_pair": "eV",
          "formation_schottky_pair": "eV",
          "diffusion_vacancy_pair": "eV",
          "diffusion_anion_vacancy": "eV"
        }
      },
      "description": "Defect formation and diffusion activation energies for NaCl."
    }
  ],
  "notes": "The checker compares each activation energy value to hidden reference values from the paper's Table 1 with an absolute tolerance. For NaCl diffusion energies, each value is compared to the paper's reported numbers (1.55, 2.35, 2.57, 2.37 eV) with a tolerance."
}
```

## How you are scored
A hidden verifier will read your two CSV files and compare every numerical value against reference values obtained from a correct implementation of the described method. The verifier awards credit based on how many of your computed energies fall within an appropriate tolerance of the reference values. The main activation-energy table carries larger weight than the NaCl diffusion table. Simply reporting numbers without performing the computation, or reporting values that do not come from the specified zeroth-order procedure, will not earn credit.
