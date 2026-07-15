# Monte Carlo Charge Transport in Double Quantum Well Heterostructures

## Problem background
In double quantum well heterostructures, population inversion between quantum‑confinement subbands can be induced by intervalley electron transfer under high lateral electric fields. This phenomenon is of fundamental interest for mid‑infrared semiconductor lasers, and determining the threshold electric field at which inversion sets in is essential for device design. This task computes those inversion thresholds for a specific AlGaAs/GaAs/InGaAs double‑well structure using a Monte Carlo simulation of hot electron transport that includes polar optical and intervalley phonon scattering.

## Approach
The workflow begins by solving the 1D Schrödinger equation within the effective mass approximation to obtain the subband energies and envelope wavefunctions in the Γ and L valleys of the given heterostructure. Next, energy‑dependent scattering rates for polar optical phonons and intervalley phonons are computed using standard III‑V material parameters. These rates feed an ensemble Monte Carlo transport simulation that tracks the electron distribution in lateral electric fields spanning 0 to 10 kV cm⁻¹ at the two lattice temperatures of interest. The simulation yields the steady‑state relative populations of the two lowest Γ subbands and the lowest L subband as a function of field, from which the population‑inversion threshold is extracted.

## Reproduction target
For the specified Al`0.4Ga`0.6As/GaAs/In`0.25Ga`0.75As double quantum well heterostructure, execute the electronic structure calculation, scattering rate computation, and Monte Carlo simulation detailed in the workflow steps. From the resulting field‑dependent subband populations, determine the lowest lateral electric field (in kV cm⁻¹) at which the population of the second Γ subband (n_Γ2) first exceeds that of the first subband (n_Γ1) at lattice temperatures of 77 K and 300 K. Write these two threshold fields to `/app/outputs/threshold_fields.json` with keys `threshold_77K` and `threshold_300K`. Provide the intermediate population data in `/app/outputs/populations_vs_field.json` as supporting evidence.

## Assets

- GaAs, Al0.4Ga0.6As, In0.25Ga0.75As Standard Material Parameters

## Workflow steps

### Step 1: Electronic structure calculation
- Role: process
- Action: Compute subband energies and envelope wavefunctions for Γ and L valleys in the specified double quantum well heterostructure (Al0.4Ga0.6As barriers, GaAs well 39 Å, Al0.4Ga0.6As barrier 25 Å, In0.25Ga0.75As well 30 Å) using effective mass approximation, solving the 1D Schrödinger equation along the growth direction.
- Evidence: none

### Step 2: Scattering rate computation
- Role: process
- Action: Compute energy-dependent polar optical phonon and intervalley phonon scattering rates using the wavefunctions from Step 1 and standard GaAs material parameters, assuming bulk-like polar optical phonon dispersion and an equilibrium phonon gas.
- Evidence: none

### Step 3: Monte Carlo transport simulation
- Role: process
- Action: Run an ensemble Monte Carlo simulation of electron transport under lateral electric fields from 0 to 10 kV/cm at lattice temperatures 77 K and 300 K using the computed scattering rates. Save steady-state relative subband populations (n/n0) for Γ1, Γ2, and L1 as a function of electric field.
- Evidence: `/app/outputs/populations_vs_field.json`

### Step 4: Population inversion threshold extraction
- Role: scored
- Action: From the simulated subband populations, determine the lowest lateral electric field (in kV/cm) at which n_Γ2 > n_Γ1 for each temperature (77 K and 300 K). Save the two threshold fields.
- Output file: `/app/outputs/threshold_fields.json`
- Format: json
- Contract: {"threshold_77K": float, "threshold_300K": float}  # units: kV/cm
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/threshold_fields.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### threshold_fields.json
- path: `/app/outputs/threshold_fields.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lowest lateral electric field at which the relative population of the second Γ subband exceeds that of the first, indicating population inversion, at lattice temperatures 77 K and 300 K.
- schema:
  - `type`: object
  - `required`:
    - `threshold_77K`: float (kV/cm)
    - `threshold_300K`: float (kV/cm)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "threshold_fields.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "threshold_77K": "float (kV/cm)",
          "threshold_300K": "float (kV/cm)"
        }
      },
      "description": "Lowest lateral electric field at which the relative population of the second Γ subband exceeds that of the first, indicating population inversion, at lattice temperatures 77 K and 300 K."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier evaluates your submission. For the scored step, it reads `threshold_fields.json` and compares your reported thresholds to reference thresholds derived from the device‑level design study. The comparison uses a tolerance that accounts for legitimate implementation differences and stochastic variation in the Monte Carlo simulation. Optionally, the verifier may inspect `populations_vs_field.json` to check that the population‑inversion condition n_Γ2 > n_Γ1 holds at the claimed fields. Your final reward is a weighted combination of the scores from all stages, with the population‑inversion threshold extraction carrying the largest weight.
