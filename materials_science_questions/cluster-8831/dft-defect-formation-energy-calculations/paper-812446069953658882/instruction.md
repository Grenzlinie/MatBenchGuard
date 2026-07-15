# Pseudopotential Self-Interstitial Formation Energy in FCC Metals

## Problem background
Defects such as interstitials in crystalline materials control many physical properties including diffusion. Understanding the energy cost to create self-interstitials in different configurations is important for interpreting experiments and modelling fast-diffuser systems. This task addresses the calculation of self-interstitial formation energies in face-centred cubic (f.c.c.) metals using first-principles pseudopotential theory. The goal is to compute the formation energy for three interstitial configurations (octahedral, tetrahedral, crowdion) in copper, silver, and gold. The results are a set of nine numbers that reflect the relative stability of these defect types and serve as a quantitative test of the theoretical method.

## Approach
Implement a pseudopotential-based total-energy calculation for f.c.c. metals containing a single self-interstitial. For a perfect lattice, compute the electrostatic energy per ion using Ewald summation and the band-structure energy via the energy-wave-number characteristic F(q). Introduce an interstitial at a specified position (octahedral, tetrahedral, or crowdion) and compute the changes in electrostatic and band-structure energy using the expressions derived from the structure factor of the defective lattice. These changes are summed to obtain the self-interstitial formation energy. The calculation uses the Ashcroft empty-core pseudopotential with Hubbard exchange-correlation screening. The core radius parameter r_c for each metal is a required input: Cu 1.28 a.u., Ag 1.47 a.u., Au 1.43 a.u. Lattice constants and derived quantities (atomic volume, Fermi wave number, Fermi energy) should be taken from standard references for the respective f.c.c. metals. The integration over q-space must be handled numerically.

## Reproduction target
Produce a CSV file containing the self-interstitial formation energy (in eV) for every combination of metal (Cu, Ag, Au) and interstitial configuration (octahedral, tetrahedral, crowdion). The computed energies should be physically reasonable.

## Assets

- numpy: numpy
- scipy: scipy
- Standard lattice constants for Cu, Ag, Au

## Workflow steps

### Step 1: Compute formation energies
- Role: scored (load-bearing)
- Action: Implement the pseudopotential formalism using the Ashcroft potential with Hubbard exchange-correlation to calculate the electrostatic and band-structure energy changes for an interstitial in f.c.c. Cu, Ag, and Au. Compute self-interstitial formation energies for octahedral, tetrahedral, and crowdion configurations using the rc parameters from the paper (Cu 1.28 a.u., Ag 1.47 a.u., Au 1.43 a.u.) and standard lattice constants. Include Ewald summation over reciprocal lattice vectors and integration over q-space for the band-structure term. Produce the formation energies in eV.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: metal (string, one of: Cu, Ag, Au), configuration (string, one of: octahedral, tetrahedral, crowdion), formation_energy_ev (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self-interstitial formation energies in eV for each metal and configuration. The checker compares each row's formation energy to hidden reference values within a tolerance and applies additional structural checks.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `configuration`, `formation_energy_ev`
  - `units`:
    - `formation_energy_ev`: eV

Notes: The formation energies must be computed from first principles using the described pseudopotential method. No external training or data fitting is required beyond the specified parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "configuration",
          "formation_energy_ev"
        ],
        "units": {
          "formation_energy_ev": "eV"
        }
      },
      "description": "Self-interstitial formation energies in eV for each metal and configuration. The checker compares each row's formation energy to hidden reference values within a tolerance and applies additional structural checks."
    }
  ],
  "notes": "The formation energies must be computed from first principles using the described pseudopotential method. No external training or data fitting is required beyond the specified parameters."
}
```

## How you are scored
A hidden verifier will independently read your `formation_energies.csv` and compare each entry to a set of reference values within a tolerance. Additional hidden structural conditions may also be applied. The final reward is the fraction of metals (out of three) for which the value agreement and any structural checks are satisfied. Producing the exact paper-reported numbers is not required; the tolerance absorbs legitimate implementation differences. The verifier runs automatically and does not require manual inspection.
