# Electrostatic Potential Comparison Using QTAIM Atomic Multipoles and CHELPG Charges

## Problem background
The electrostatic potential (ESP) around a molecule governs how it interacts with external charges, ions, and other molecules. A common practical approximation replaces the full continuous charge density with a set of atomic point charges, but this discards the anisotropy created by chemical bonds and lone pairs. An alternative is to expand the molecular charge distribution into atomic multipoles — charges, dipole moments, traceless quadrupole moments — computed from the quantum-mechanical wavefunction using the Quantum Theory of Atoms in Molecules (QTAIM). This task investigates whether the inclusion of atomic dipoles and quadrupoles produces ESP values that agree more closely with a direct density-functional theory (DFT) reference than those obtained from electrostatic-potential-fitted CHELPG charges. The study focuses on seven small linear molecules (H₂, HF, HCl, HBr, HCN, HNC, CO) and examines the role of the charge, dipole, and quadrupole terms separately.

## Approach
The conceptual workflow consists of three stages. First, geometry optimization of each isolated molecule is performed at the B3LYP/6‑311G(3d,3p) level of theory. Second, for each molecule a proton is placed on the molecular axis at distances of 3, 4, 5, 6, 7, and 8 Å from every terminal atom; the orientation places hydrogen (or carbon in CO) on the negative z‑axis. Third, for every proton‑molecule geometry a single‑point B3LYP/6‑311G(3d,3p) calculation is carried out to obtain the reference ESP at the proton position directly from the SCF density, and the wavefunction is analysed with Multiwfn to extract (a) QTAIM atomic charges, atomic dipole moments (z‑component), and atomic traceless quadrupole moments (zz‑component), and (b) CHELPG atomic charges. The QTAIM multipole electrostatic potential V_QTAIM is computed via the standard expansion truncated at quadrupole (charge + dipole + quadrupole terms), while V_CHELPG uses only the charge term. Both are compared to the direct reference V_ref by the percent deviation 100 |V_method − V_ref| / |V_ref|. Additionally, the relative contributions of the charge, dipole, and quadrupole sums to V_QTAIM are normalised so that the largest absolute contribution equals unity. The entire analysis is performed for both sides of every molecule.

## Reproduction target
Compute and report, for every molecule and terminal atom, the electrostatic potentials V_QTAIM, V_CHELPG, and V_ref at the proton position for all distances 3–8 Å. From these, calculate the percent deviation of each method from V_ref. Also calculate the normalized relative contributions of the charge, dipole, and quadrupole terms to V_QTAIM. The final deliverable is a single CSV file (`/app/outputs/electrostatic_results.csv`) whose schema is described in the workflow step 3 contract. The evaluation will focus on:

- The percent deviations at the smallest probed distance (3 Å) for each method and each molecular end.
- The relative contributions of the three multipole terms to V_QTAIM at 3 Å and 8 Å for each end.

Producing the full grid of distances and reporting all quantities is required, because the verifier may also perform sanity checks on the distance dependence.

## Assets

- Psi4: https://psicode.org/
- Multiwfn: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Geometry optimization of isolated molecules
- Role: process
- Action: Perform B3LYP/6-311G(3d,3p) geometry optimization for each molecule: H2, HF, HCl, HBr, HCN, HNC, CO. Save optimized coordinates for all subsequent steps.
- Evidence: none

### Step 2: Generate proton positions along the molecular axis
- Role: process
- Action: For each molecule, define the molecular axis along the bond direction. Place a proton at distances 3, 4, 5, 6, 7, 8 Å from each terminal atom along the axis, using the orientation where hydrogen (or carbon in CO) is on the negative side of the axis. Create the full set of proton-molecule geometries.
- Evidence: none

### Step 3: Single-point DFT, multipole extraction, and electrostatic potential analysis
- Role: scored (load-bearing)
- Action: For every proton-molecule arrangement: perform a B3LYP/6-311G(3d,3p) single-point calculation. Extract the reference electrostatic potential V_ref at the proton position directly from the DFT output. From the wavefunction, obtain QTAIM atomic charges, atomic dipole moments (z-components), and traceless atomic quadrupole moments (zz-components); also obtain CHELPG atomic charges. Compute the electrostatic potential at the proton: V_QTAIM via the multipole expansion (charge + dipole + quadrupole terms) and V_CHELPG from the charge-only term. Compute percent deviation = 100 * |V_method - V_ref| / |V_ref| for each method. Compute normalized relative contributions of the charge, dipole, and quadrupole sums to V_QTAIM (normalize so the largest absolute contribution equals 1). Write all results to the output file.
- Output file: `/app/outputs/electrostatic_results.csv`
- Format: csv
- Contract: molecule(string), terminal_atom(string), distance(float), V_QTAIM(float), V_CHELPG(float), V_ref(float), pct_dev_QTAIM(float), pct_dev_CHELPG(float), rel_charge_contrib(float), rel_dipole_contrib(float), rel_quadrupole_contrib(float). Units: V in atomic units, deviations dimensionless, contributions dimensionless (normalized).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electrostatic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electrostatic_results.csv
- path: `/app/outputs/electrostatic_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed electrostatic potentials, percent deviations from the B3LYP reference, and normalized relative contributions of charge, dipole, and quadrupole terms to the QTAIM potential, for all proton-molecule arrangements.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `terminal_atom`, `distance`, `V_QTAIM`, `V_CHELPG`, `V_ref`, `pct_dev_QTAIM`, `pct_dev_CHELPG`, `rel_charge_contrib`, `rel_dipole_contrib`, `rel_quadrupole_contrib`
  - `units`:
    - `distance`: Angstrom
    - `V_QTAIM`: atomic units
    - `V_CHELPG`: atomic units
    - `V_ref`: atomic units
    - `pct_dev_QTAIM`: dimensionless (percent)
    - `pct_dev_CHELPG`: dimensionless (percent)
    - `rel_charge_contrib`: dimensionless (normalized)
    - `rel_dipole_contrib`: dimensionless (normalized)
    - `rel_quadrupole_contrib`: dimensionless (normalized)

Notes: The checker reads this file, groups by molecule and terminal_atom, extracts rows at distances nearest to 3.0 Å and 8.0 Å, and compares the percent deviations and relative contributions to hidden reference values derived from the paper. Tolerance will be set to absorb legitimate method/tool spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electrostatic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "terminal_atom",
          "distance",
          "V_QTAIM",
          "V_CHELPG",
          "V_ref",
          "pct_dev_QTAIM",
          "pct_dev_CHELPG",
          "rel_charge_contrib",
          "rel_dipole_contrib",
          "rel_quadrupole_contrib"
        ],
        "units": {
          "distance": "Angstrom",
          "V_QTAIM": "atomic units",
          "V_CHELPG": "atomic units",
          "V_ref": "atomic units",
          "pct_dev_QTAIM": "dimensionless (percent)",
          "pct_dev_CHELPG": "dimensionless (percent)",
          "rel_charge_contrib": "dimensionless (normalized)",
          "rel_dipole_contrib": "dimensionless (normalized)",
          "rel_quadrupole_contrib": "dimensionless (normalized)"
        }
      },
      "description": "Computed electrostatic potentials, percent deviations from the B3LYP reference, and normalized relative contributions of charge, dipole, and quadrupole terms to the QTAIM potential, for all proton-molecule arrangements."
    }
  ],
  "notes": "The checker reads this file, groups by molecule and terminal_atom, extracts rows at distances nearest to 3.0 Å and 8.0 Å, and compares the percent deviations and relative contributions to hidden reference values derived from the paper. Tolerance will be set to absorb legitimate method/tool spread."
}
```

## How you are scored
A hidden verifier reads your output CSV and extracts the rows relevant to the targets listed above. For each molecule and terminal side, it compares your reported percent deviations at 3 Å and your relative contributions at 3 Å and 8 Å against hidden reference values. The comparison uses tolerances that account for the fact that a different DFT implementation (Psi4 instead of the original software) can shift the absolute numbers slightly. Meeting or exceeding the reference threshold earns full credit for that comparison; larger deviations earn progressively lower credit. The final reward is a weighted sum of these individual scores, resulting in a single number between 0 and 1. The verifier may also perform low‑weight structural checks, for example that percent deviations decrease monotonically with increasing distance. Because scoring is fully automated, you must not attempt to match any particular published value; simply produce the results of an honest re‑computation with the specified protocol.
