# First-principles reproduction of rutile RuO2 electronic structure and optical properties

## Problem background
Transition-metal dioxides such as rutile RuO₂ are candidates for superhard materials. First-principles density functional theory (DFT) can be used to predict their equilibrium structure, elastic constants, electronic structure, and optical response. Reproducing these quantities from DFT calculations provides insight into the bonding nature and enables comparison with experimental measurements.

## Approach
Use plane-wave pseudopotential DFT within the generalized gradient approximation (GGA) to relax the rutile RuO₂ unit cell. From the relaxed structure, compute the elastic constants by applying finite strains and fitting energy-strain or stress-strain relations. Obtain the electronic structure (wavefunctions and eigenvalues) via a self-consistent field calculation, then compute the frequency-dependent dielectric function ε(ω) for two light polarizations (E⊥c and E∥c) using dipole transition matrix elements and a Kramers-Kronig transformation. Finally, extract the static refractive index n(0) and the main absorption peak positions and magnitudes for each polarization.

## Reproduction target
Set up the rutile RuO₂ unit cell (space group P4₂/mnm) and perform DFT calculations using Quantum ESPRESSO to determine the following quantities:
1. Equilibrium lattice constants a, c and internal coordinate u.
2. Bulk modulus B₀ and the elastic constants c₁₁, c₃₃, c₄₄, c₆₆, c₁₂, c₁₃.
3. The static refractive index n(0) for both light polarizations (E⊥c and E∥c).
4. The position (in eV) and magnitude of the main peak of the imaginary part ε₂(ω) for each polarization.
Write these results to the specified JSON files; the exact numerical values must be obtained by running the full workflow, not by guesswork or approximate lookup.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Structure relaxation
- Role: process
- Action: Set up the rutile RuO2 unit cell (space group P4_2/mnm, 6 atoms) with initial experimental lattice parameters, and perform a full geometry optimization (relaxation of atomic positions and cell parameters) using Quantum ESPRESSO with appropriate pseudopotentials and the GGA functional.
- Evidence: `/app/outputs/relax.log`

### Step 2: Structure and elastic properties
- Role: scored
- Action: From the relaxed structure, compute the elastic constants (c11, c33, c44, c66, c12, c13) and bulk modulus (B0) by applying finite strains and fitting energy-strain or stress-strain relations. Extract the equilibrium lattice constants a, c, and internal coordinate u from the relaxation. Write all these values to structure_and_elastic.json.
- Output file: `/app/outputs/structure_and_elastic.json`
- Format: json
- Contract: {"a": float, "c": float, "u": float, "B0": float, "c11": float, "c33": float, "c44": float, "c66": float, "c12": float, "c13": float}
- Scoring: scored by hidden verifier

### Step 3: Electronic structure calculation
- Role: process
- Action: Perform a self-consistent field (SCF) calculation on the relaxed structure to obtain wavefunctions and Kohn-Sham eigenvalues. Compute the electronic band structure along high-symmetry lines and the total/projected density of states (DOS) as intermediate data.
- Evidence: `/app/outputs/bands.dat.gnu`

### Step 4: Dielectric function calculation
- Role: process
- Action: Using the SCF wavefunctions and eigenvalues, compute the imaginary part of the dielectric function epsilon2(omega) for two polarizations (E⊥c and E//c) via the dipole transition matrix elements. Obtain the real part epsilon1(omega) through numerical Kramers-Kronig transformation.
- Evidence: `/app/outputs/epsilon.dat`

### Step 5: Optical properties extraction
- Role: scored (load-bearing)
- Action: From the computed epsilon1 and epsilon2, calculate the static refractive index n(0) for both polarizations. Identify the main peak of epsilon2(omega) for each polarization (position in eV and magnitude). Write the results to optical_properties.json.
- Output file: `/app/outputs/optical_properties.json`
- Format: json
- Contract: {"n0_perp": float, "n0_par": float, "eps2_peak_perp_pos": float (eV), "eps2_peak_perp_mag": float, "eps2_peak_par_pos": float (eV), "eps2_peak_par_mag": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structure_and_elastic.json`
- `/app/outputs/optical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structure_and_elastic.json
- path: `/app/outputs/structure_and_elastic.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored JSON containing lattice parameters (a, c, u) in Å, bulk modulus B0 in GPa, and elastic constants (c11, c33, c44, c66, c12, c13) in GPa.
- schema:
  - `type`: object
  - `required`:
    - `a`: number
    - `c`: number
    - `u`: number
    - `B0`: number
    - `c11`: number
    - `c33`: number
    - `c44`: number
    - `c66`: number
    - `c12`: number
    - `c13`: number
  - `units`:
    - `a`: Å
    - `c`: Å
    - `u`: dimensionless
    - `B0`: GPa
    - `c11`: GPa
    - `c33`: GPa
    - `c44`: GPa
    - `c66`: GPa
    - `c12`: GPa
    - `c13`: GPa

### optical_properties.json
- path: `/app/outputs/optical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored JSON containing static refractive indices n(0) for E⊥c and E//c, main epsilon2 peak position/magnitude for each polarization, electron energy loss peak positions/magnitudes for both polarizations, and extinction coefficient peak positions for both polarizations.
- schema:
  - `type`: object
  - `required`:
    - `n0_perp`: number
    - `n0_par`: number
    - `eps2_peak_perp_pos`: number
    - `eps2_peak_perp_mag`: number
    - `eps2_peak_par_pos`: number
    - `eps2_peak_par_mag`: number
    - `eloss_peak_perp_pos`: number
    - `eloss_peak_perp_mag`: number
    - `eloss_peak_par_pos`: number
    - `eloss_peak_par_mag`: number
    - `ext_peak_perp_pos`: number
    - `ext_peak_par_pos`: number
  - `units`:
    - `n0_perp`: dimensionless
    - `n0_par`: dimensionless
    - `eps2_peak_perp_pos`: eV
    - `eps2_peak_perp_mag`: dimensionless
    - `eps2_peak_par_pos`: eV
    - `eps2_peak_par_mag`: dimensionless
    - `eloss_peak_perp_pos`: eV
    - `eloss_peak_perp_mag`: dimensionless
    - `eloss_peak_par_pos`: eV
    - `eloss_peak_par_mag`: dimensionless
    - `ext_peak_perp_pos`: eV
    - `ext_peak_par_pos`: eV

Notes: The task uses a T0 result-level comparison with hidden tolerances derived from the paper's reported values. The agent must run the full DFT pipeline; no pre-computed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structure_and_elastic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "number",
          "c": "number",
          "u": "number",
          "B0": "number",
          "c11": "number",
          "c33": "number",
          "c44": "number",
          "c66": "number",
          "c12": "number",
          "c13": "number"
        },
        "units": {
          "a": "Å",
          "c": "Å",
          "u": "dimensionless",
          "B0": "GPa",
          "c11": "GPa",
          "c33": "GPa",
          "c44": "GPa",
          "c66": "GPa",
          "c12": "GPa",
          "c13": "GPa"
        }
      },
      "description": "Scored JSON containing lattice parameters (a, c, u) in Å, bulk modulus B0 in GPa, and elastic constants (c11, c33, c44, c66, c12, c13) in GPa."
    },
    {
      "file": "optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n0_perp": "number",
          "n0_par": "number",
          "eps2_peak_perp_pos": "number",
          "eps2_peak_perp_mag": "number",
          "eps2_peak_par_pos": "number",
          "eps2_peak_par_mag": "number",
          "eloss_peak_perp_pos": "number",
          "eloss_peak_perp_mag": "number",
          "eloss_peak_par_pos": "number",
          "eloss_peak_par_mag": "number",
          "ext_peak_perp_pos": "number",
          "ext_peak_par_pos": "number"
        },
        "units": {
          "n0_perp": "dimensionless",
          "n0_par": "dimensionless",
          "eps2_peak_perp_pos": "eV",
          "eps2_peak_perp_mag": "dimensionless",
          "eps2_peak_par_pos": "eV",
          "eps2_peak_par_mag": "dimensionless",
          "eloss_peak_perp_pos": "eV",
          "eloss_peak_perp_mag": "dimensionless",
          "eloss_peak_par_pos": "eV",
          "eloss_peak_par_mag": "dimensionless",
          "ext_peak_perp_pos": "eV",
          "ext_peak_par_pos": "eV"
        }
      },
      "description": "Scored JSON containing static refractive indices n(0) for E⊥c and E//c, main epsilon2 peak position/magnitude for each polarization, electron energy loss peak positions/magnitudes for both polarizations, and extinction coefficient peak positions for both polarizations."
    }
  ],
  "notes": "The task uses a T0 result-level comparison with hidden tolerances derived from the paper's reported values. The agent must run the full DFT pipeline; no pre-computed data is provided."
}
```

## How you are scored
A hidden verifier independently checks the submitted structure_and_elastic.json and optical_properties.json. It compares each reported value against reference values derived from the paper's own calculations, tolerating small differences introduced by the choice of pseudopotentials, functional, or cutoff parameters. Each JSON file is scored according to how many of its contained values fall within the allowed interval around the reference; the overall reward is a weighted combination of the two per-artifact scores. Simply reporting a number without executing the required DFT pipeline will fail these precision checks, because the tolerances are set to require a genuine first-principles calculation.
