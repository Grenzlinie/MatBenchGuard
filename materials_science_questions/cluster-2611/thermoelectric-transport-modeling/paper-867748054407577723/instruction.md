# First‑principles Thermoelectric Transport of Tobermorite Cement Analogues

## Problem background
Buildings waste a substantial amount of energy as heat. Cement-based materials are ubiquitous in construction and could be functionalised to harvest this wasted heat through thermoelectric conversion. Tobermorite minerals are structural analogues of the calcium-silicate-hydrate (C-S-H) gel that gives cement its strength. A first-principles understanding of their electronic transport properties is missing and would guide the design of efficient cement-composite thermoelectrics. This task computes, from first principles, the thermoelectric performance of three tobermorite models (T9Å, T11Å, T14Å) to assess their potential.

## Approach
Density Functional Theory (DFT) calculations within the generalized gradient approximation (PBE functional) and the Grimme D3 dispersion correction are used to relax the crystal structures of the three tobermorite models, starting from their published experimental structures. Non-self-consistent DFT calculations on dense k-point meshes then provide the Kohn-Sham eigenvalues and direct band gaps at the Γ-point. Electronic transport coefficients are obtained by solving the linearized Boltzmann transport equation within the rigid-band and constant relaxation time approximations, using the BoltzTraP code and the previously computed band energies. The electronic figure of merit \(Z_eT = S^2 \sigma T / \kappa_e\) is extracted at specific doping concentrations and temperatures that optimise thermoelectric performance.

## Reproduction target
Using the public experimental crystal structures of tobermorite T9Å, T11Å, and T14Å from the American Mineralogist Crystal Structure Database, perform DFT structural relaxation (PBE+D3 in Quantum ESPRESSO), compute the direct band gaps at the Γ-point, and evaluate the electronic figure of merit \(Z_eT\) at the following optimal conditions: T9Å (400 K, \(10^{17}\) cm\(^{-3}\)), T11Å (400 K, \(10^{17}\) cm\(^{-3}\)), T14Å (225 K, \(10^{19}\) cm\(^{-3}\)).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: https://www.boltztrap.org/
- Tobermorite T9Å crystal structure (riverside): https://rruff.geo.arizona.edu/AMS/amcsd.php
- Tobermorite T11Å crystal structure (tobermorite): https://rruff.geo.arizona.edu/AMS/amcsd.php
- Tobermorite T14Å crystal structure (plombierite): https://rruff.geo.arizona.edu/AMS/amcsd.php

## Workflow steps

### Step 1: Obtain initial crystal structures
- Role: process
- Action: Download the experimental crystal structures of tobermorite T9Å, T11Å, and T14Å from the American Mineralogist Crystal Structure Database (https://rruff.geo.arizona.edu/AMS/amcsd.php). Use the published structures of riverside tobermorite, tobermorite 11 Å, and plombierite.
- Evidence: none

### Step 2: DFT structural relaxation
- Role: scored
- Action: Perform variable-cell structural relaxation using DFT with the PBE functional and Grimme D3 dispersion correction (e.g., via Quantum ESPRESSO) for all three tobermorite models. Optimize lattice parameters and atomic positions with appropriate convergence criteria. Extract the relaxed lattice parameters a, b, c (Å) and α, β, γ (degrees) and write them to the output file.
- Output file: `/app/outputs/relaxed_lattice_parameters.json`
- Format: json
- Contract: {"T9A":{"a":<float>,"b":<float>,"c":<float>,"alpha":<float>,"beta":<float>,"gamma":<float>},"T11A":{...},"T14A":{...}}
- Scoring: scored by hidden verifier

### Step 3: Electronic structure and band gaps
- Role: scored
- Action: Run non‑self‑consistent DFT calculations (e.g., with Quantum ESPRESSO) on a dense k‑point mesh to obtain Kohn‑Sham eigenvalues for each tobermorite model. Determine the direct band gap at the Γ‑point from the eigenvalues and write the values (in eV) to the output file.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"T9A":<float>,"T11A":<float>,"T14A":<float>}
- Scoring: scored by hidden verifier

### Step 4: Electronic thermoelectric figure of merit
- Role: scored (load-bearing)
- Action: Using the band energies from the electronic structure calculation, solve the Boltzmann transport equation within the rigid‑band and constant relaxation time approximations (e.g., via BoltzTraP) to compute the Seebeck coefficient, electrical conductivity over relaxation time, and electronic thermal conductivity over relaxation time as functions of temperature and chemical potential. Extract the electronic figure of merit ZeT = S²σ/κe at the optimal conditions: T9Å (T=400 K, carrier concentration 10¹⁷ cm⁻³), T11Å (400 K, 10¹⁷ cm⁻³), and T14Å (225 K, 10¹⁹ cm⁻³). Write the results to the output file.
- Output file: `/app/outputs/electronic_ZT.json`
- Format: json
- Contract: {"T9A":{"temperature":400.0,"carrier_concentration":1e17,"Z_eT":<float>},"T11A":{"temperature":400.0,"carrier_concentration":1e17,"Z_eT":<float>},"T14A":{"temperature":225.0,"carrier_concentration":1e19,"Z_eT":<float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_lattice_parameters.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/electronic_ZT.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_lattice_parameters.json
- path: `/app/outputs/relaxed_lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters from DFT structural optimization; compared against published experimental data within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `T9A`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `c`: float (Å)
      - `alpha`: float (deg)
      - `beta`: float (deg)
      - `gamma`: float (deg)
    - `T11A`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `c`: float (Å)
      - `alpha`: float (deg)
      - `beta`: float (deg)
      - `gamma`: float (deg)
    - `T14A`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `c`: float (Å)
      - `alpha`: float (deg)
      - `beta`: float (deg)
      - `gamma`: float (deg)

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gaps at the Γ‑point computed from the electronic structure; compared against paper‑reported values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `T9A`: float (eV)
    - `T11A`: float (eV)
    - `T14A`: float (eV)

### electronic_ZT.json
- path: `/app/outputs/electronic_ZT.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic figure of merit at the claimed optimal doping and temperature conditions; meeting or exceeding the paper's value earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `T9A`:
      - `temperature`: float (K)
      - `carrier_concentration`: float (cm⁻³)
      - `Z_eT`: float (dimensionless)
    - `T11A`:
      - `temperature`: float (K)
      - `carrier_concentration`: float (cm⁻³)
      - `Z_eT`: float (dimensionless)
    - `T14A`:
      - `temperature`: float (K)
      - `carrier_concentration`: float (cm⁻³)
      - `Z_eT`: float (dimensionless)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T9A": {
            "a": "float (Å)",
            "b": "float (Å)",
            "c": "float (Å)",
            "alpha": "float (deg)",
            "beta": "float (deg)",
            "gamma": "float (deg)"
          },
          "T11A": {
            "a": "float (Å)",
            "b": "float (Å)",
            "c": "float (Å)",
            "alpha": "float (deg)",
            "beta": "float (deg)",
            "gamma": "float (deg)"
          },
          "T14A": {
            "a": "float (Å)",
            "b": "float (Å)",
            "c": "float (Å)",
            "alpha": "float (deg)",
            "beta": "float (deg)",
            "gamma": "float (deg)"
          }
        }
      },
      "description": "Relaxed lattice parameters from DFT structural optimization; compared against published experimental data within tolerances."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T9A": "float (eV)",
          "T11A": "float (eV)",
          "T14A": "float (eV)"
        }
      },
      "description": "Direct band gaps at the Γ‑point computed from the electronic structure; compared against paper‑reported values within a tolerance."
    },
    {
      "file": "electronic_ZT.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "T9A": {
            "temperature": "float (K)",
            "carrier_concentration": "float (cm⁻³)",
            "Z_eT": "float (dimensionless)"
          },
          "T11A": {
            "temperature": "float (K)",
            "carrier_concentration": "float (cm⁻³)",
            "Z_eT": "float (dimensionless)"
          },
          "T14A": {
            "temperature": "float (K)",
            "carrier_concentration": "float (cm⁻³)",
            "Z_eT": "float (dimensionless)"
          }
        }
      },
      "description": "Electronic figure of merit at the claimed optimal doping and temperature conditions; meeting or exceeding the paper's value earns full credit."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each of the three scored output files. The relaxed lattice parameters and band gaps are compared to expected reference values within appropriate tolerances. The electronic \(Z_eT\) values are scored using a rule that awards full credit if the computed value meets or exceeds a target performance and proportionally less credit if it falls below. The overall reward is a weighted sum of the individual artifact scores. Simply reporting the paper's numbers is not sufficient; the verifier examines the actual computed outputs.
