# Bond-order potential validation for W-H: defect, surface, diffusion, and melting properties

## Problem background
Tungsten (W) is a prime candidate for plasma-facing components in future fusion reactors, where it will be subjected to intense fluxes of hydrogen (H) isotopes. Understanding how H interacts with native defects in W—such as vacancies and surfaces—is critical for predicting material performance and lifetime. Molecular dynamics (MD) simulations are a key tool for these studies, but their reliability depends on the accuracy of the underlying interatomic potentials. This work develops a new analytical bond-order potential (BOP) for W–W and W–H interactions that is specifically designed to improve the description of defect-related properties compared to earlier potentials for this system. The potential is validated by computing a set of key physical quantities: bulk W defect formation energies, surface energies of low-index W surfaces, the melting point of W, H interstitial formation energies, and the H diffusion barrier in W.

## Approach
The total energy is expressed as a sum over bonds with pair-like repulsive and attractive Morse-type terms, modulated by a bond-order parameter that captures the local atomic environment and angular dependence. Interactions are smoothly cut off between the first and second neighbor shells. The analytical BOP form is implemented in LAMMPS (using the `pair_style bop` or an equivalent custom implementation) with the provided parameter sets: a W–W potential (fitted to bulk properties and point-defect energies), a W–H potential (fitted to H formation energies and small WH molecules), and Brenner's H–H potential. Using these potentials, the following computational workflow is performed: (i) bulk W calculations—lattice relaxations and static energy calculations to obtain cohesive energy, lattice constant, elastic constants, and formation energies of vacancies, self-interstitials in various configurations, and alternative crystal phases; (ii) surface calculations—construction of slab models for the (100), (110), and (211) surfaces to extract surface energies and interlayer relaxations; (iii) melting point—solid–liquid interface MD simulation at ambient pressure; (iv) H defect calculations—formation energies of H at tetrahedral, octahedral, and substitutional sites in bcc W; (v) H diffusion—energy barrier along the TIS–TIS path using a drag method. The final required quantities are then aggregated into a single JSON file.

## Reproduction target
Using the provided bond-order potential parameters, recompute the following validation properties and write them into a JSON file `/app/outputs/computed_properties.json`:

- vacancy_formation_energy (eV) – formation energy of a single vacancy in bcc W
- SIA_d111_formation_energy (eV) – formation energy of a ⟨111⟩ dumbbell self-interstitial
- H_TIS_formation_energy (eV) – formation energy of one H atom at the tetrahedral interstitial site in bcc W
- surface_energy_100 (J/m²) – surface energy of the (100) surface
- surface_energy_110 (J/m²) – surface energy of the (110) surface
- surface_energy_211 (J/m²) – surface energy of the (211) surface
- melting_point (K) – melting point of W
- diffusion_barrier_TIS_TIS (eV) – energy barrier for H diffusion along the TIS–TIS path

The JSON object must contain exactly these eight keys, each mapping to a numeric value in the indicated unit. All properties are to be computed from the same set of potentials and simulation protocols described in the workflow steps.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- Potential parameters for W–W, W–H, and H–H interactions (see table below)

## Potential parameters

The interatomic potentials for W–W, W–H, and H–H interactions follow the analytical bond-order form described in the approach section. The parameter sets are listed below. The H–H parameters are taken from Brenner's potential [Brenner, Phys. Rev. B 42, 9458 (1990)]. The Fermi function parameters are used to smoothly connect the repulsive wall to a universal repulsive potential at short distances.

| Parameter | W–W | W–H | H–H (Brenner) |
|---|---|---|---|
| $D_0$ (eV) | 2.87454 | 3.035928 | 4.7509 |
| $r_0$ (nm) | 0.238631 | 0.176306 | 0.074144 |
| $\beta$ (nm$^{-1}$) | 13.3682 | 13.54368 | 19.436 |
| $S$ | 1.25348 | 1.031565 | 2.3432 |
| $\gamma$ | 8.3879×10$^{-4}$ | 8.595×10$^{-3}$ | 12.33 |
| $c$ | 0.850284 | 0.146902 | 0.0 |
| $d$ | 0.144317 | 0.393100 | 1.0 |
| $h$ | −0.36846 | 0.558936 | 1.0 |
| $R$ (nm) | 0.4131580 | 0.2568113 | 0.140 |
| $D$ (nm) | 0.0930180 | 0.0133729 | 0.030 |
| Fermi $r_f$ (nm) | 0.13 | 0.05 | 0.035 |
| Fermi $b_f$ (nm$^{-1}$) | 120 | 70 | 150 |

Additional parameters for the bond-order term: $\alpha_{ijk}=0$ except $\alpha_{WHW}=0.451823$ and $\alpha_{HHH}=4.0$. The cutoff function uses $R$ and $D$ as defined in Eq. (4) of the approach.

## Workflow steps

### Step 1: Compute bulk W properties
- Role: process
- Action: Using LAMMPS with the provided W–W potential parameters, perform lattice relaxations and static calculations to determine cohesive energy, equilibrium lattice constant, bulk modulus, elastic constants (c11, c12, c44), vacancy formation energy, vacancy migration energy, divacancy formation energies, self-interstitial formation energies for <100>, <110>, <111>, tetrahedral, and octahedral configurations, dimer properties, and energies of fcc, sc, diamond phases. Write the computed values to a text file for later aggregation.
- Evidence: `/app/outputs/w_bulk.txt`

### Step 2: Compute W surface properties
- Role: process
- Action: Construct slab models for (100), (110), and (211) surfaces using the W–W potential in LAMMPS; compute surface energies and interlayer relaxations. Output the surface energies (J/m²) to a text file.
- Evidence: `/app/outputs/surface.txt`

### Step 3: Compute W melting point
- Role: process
- Action: Perform a solid-liquid interface molecular dynamics simulation using the W–W potential to estimate the melting point at ambient pressure. Record the value in a text file.
- Evidence: `/app/outputs/melting_point.txt`

### Step 4: Compute H defect formation energies
- Role: process
- Action: Using the W–W, W–H, and H–H potentials in LAMMPS, calculate the formation energies of a single hydrogen atom at tetrahedral, octahedral, and substitutional sites in bcc tungsten. Write the tetrahedral (TIS) formation energy to a text file.
- Evidence: `/app/outputs/h_defects.txt`

### Step 5: Compute H diffusion barrier
- Role: process
- Action: Apply the drag method with the full potential set to determine the energy barrier for H migration along the TIS–TIS path. Write the barrier value (eV) to a text file.
- Evidence: `/app/outputs/diffusion_barrier.txt`

### Step 6: Aggregate final properties into scored JSON
- Role: scored (load-bearing)
- Action: Collect the required property values from the evidence files produced in steps s1–s5 and write a single JSON file computed_properties.json containing: vacancy_formation_energy (eV), SIA_d111_formation_energy (eV), H_TIS_formation_energy (eV), surface_energy_100 (J/m²), surface_energy_110 (J/m²), surface_energy_211 (J/m²), melting_point (K), diffusion_barrier_TIS_TIS (eV).
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: object with keys: vacancy_formation_energy (number, eV), SIA_d111_formation_energy (number, eV), H_TIS_formation_energy (number, eV), surface_energy_100 (number, J/m^2), surface_energy_110 (number, J/m^2), surface_energy_211 (number, J/m^2), melting_point (number, K), diffusion_barrier_TIS_TIS (number, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the key validation properties recomputed by the agent. Each field is a numeric value with the indicated unit.
- schema:
  - `type`: object
  - `required`: `vacancy_formation_energy`, `SIA_d111_formation_energy`, `H_TIS_formation_energy`, `surface_energy_100`, `surface_energy_110`, `surface_energy_211`, `melting_point`, `diffusion_barrier_TIS_TIS`
  - `properties`:
    - `vacancy_formation_energy`:
      - `type`: number
    - `SIA_d111_formation_energy`:
      - `type`: number
    - `H_TIS_formation_energy`:
      - `type`: number
    - `surface_energy_100`:
      - `type`: number
    - `surface_energy_110`:
      - `type`: number
    - `surface_energy_211`:
      - `type`: number
    - `melting_point`:
      - `type`: number
    - `diffusion_barrier_TIS_TIS`:
      - `type`: number
  - `units`:
    - `vacancy_formation_energy`: eV
    - `SIA_d111_formation_energy`: eV
    - `H_TIS_formation_energy`: eV
    - `surface_energy_100`: J/m^2
    - `surface_energy_110`: J/m^2
    - `surface_energy_211`: J/m^2
    - `melting_point`: K
    - `diffusion_barrier_TIS_TIS`: eV

Notes: The hidden checker compares each numeric value to the paper-reported gold values with pre-defined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "vacancy_formation_energy",
          "SIA_d111_formation_energy",
          "H_TIS_formation_energy",
          "surface_energy_100",
          "surface_energy_110",
          "surface_energy_211",
          "melting_point",
          "diffusion_barrier_TIS_TIS"
        ],
        "properties": {
          "vacancy_formation_energy": {
            "type": "number"
          },
          "SIA_d111_formation_energy": {
            "type": "number"
          },
          "H_TIS_formation_energy": {
            "type": "number"
          },
          "surface_energy_100": {
            "type": "number"
          },
          "surface_energy_110": {
            "type": "number"
          },
          "surface_energy_211": {
            "type": "number"
          },
          "melting_point": {
            "type": "number"
          },
          "diffusion_barrier_TIS_TIS": {
            "type": "number"
          }
        },
        "units": {
          "vacancy_formation_energy": "eV",
          "SIA_d111_formation_energy": "eV",
          "H_TIS_formation_energy": "eV",
          "surface_energy_100": "J/m^2",
          "surface_energy_110": "J/m^2",
          "surface_energy_211": "J/m^2",
          "melting_point": "K",
          "diffusion_barrier_TIS_TIS": "eV"
        }
      },
      "description": "JSON file containing the key validation properties recomputed by the agent. Each field is a numeric value with the indicated unit."
    }
  ],
  "notes": "The hidden checker compares each numeric value to the paper-reported gold values with pre-defined tolerances."
}
```

## How you are scored
A hidden verifier will read your submitted `/app/outputs/computed_properties.json` and compare each reported quantity to reference values derived from the original validation study. Each quantity is checked within a numerical tolerance that accounts for legitimate differences arising from using different LAMMPS versions, optimizer settings, k-point/box-size choices, or convergence criteria. The verifier computes the fraction of properties that fall within the expected tolerance, and this fraction (weighted appropriately) determines your reward. You must produce the JSON file with the exact keys, units, and numeric values as described; incomplete or malformed outputs will receive partial or zero credit. Meeting or exceeding the expected tolerance on all scored properties yields full credit; larger deviations reduce the score proportionally.
