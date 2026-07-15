# Thermoelectric Properties of Monolayer ZrSe2 and HfSe2

## Problem background
Two-dimensional transition-metal dichalcogenides (TMDCs) have attracted significant interest for thermoelectric applications, as low-dimensional materials may exhibit reduced lattice thermal conductivity compared to their bulk counterparts. This task explores the thermoelectric properties of monolayer ZrSe2 and HfSe2, which belong to the CdI2-type structural family distinct from the more widely studied MoS2-type TMDCs. The goal is to compute the lattice thermal conductivity and thermoelectric figure of merit using first-principles density functional theory (DFT) and Boltzmann transport equations, and to determine how these quantities compare with typical TMDC materials.

## Approach
The thermoelectric figure of merit ZT = S²σT / (κ_e + κ_l) is determined by combining electronic and phononic transport coefficients. Electronic transport properties (Seebeck coefficient S, electrical conductivity σ, and electronic thermal conductivity κ_e) are computed from DFT band energies using Boltzmann transport theory (BoltzTraP2). Carrier relaxation times are estimated from deformation potential theory, using effective masses, 2D elastic modulus, and deformation potential constants extracted from DFT. Lattice thermal conductivity κ_l is obtained through the phonon Boltzmann transport equation (ShengBTE) using harmonic and anharmonic interatomic force constants derived from DFT supercell calculations with Phonopy. All DFT calculations use the PBE exchange-correlation functional and PAW pseudopotentials; Quantum ESPRESSO is the open-source DFT engine. The workflow proceeds from structural optimization through electronic and phononic calculations, culminating in the assembly of ZT as a function of carrier concentration and temperature.

## Reproduction target
Compute the lattice thermal conductivity κ_l as a function of temperature from 300 K to 1000 K for monolayer ZrSe2 and HfSe2, and the thermoelectric figure of merit ZT as a function of carrier concentration at 600 K for both p-type and n-type doping. The produced data will be evaluated by a hidden verifier that checks structural consistency and trend adherence based on the paper's findings.

## Assets

- Monolayer ZrSe2 and HfSe2 crystal structures
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials
- BoltzTraP2: https://bitbucket.org/sousaw/boltztrap2
- ShengBTE: https://www.shengbte.org/
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT structural optimization
- Role: process
- Action: Perform DFT structural optimization of monolayer ZrSe2 and HfSe2 unit cells using PBE functional and PAW pseudopotentials to obtain relaxed lattice parameters and atomic positions.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: Compute band structures along Γ-M-K-Γ path, band gaps, effective masses, and energy eigenvalues on a dense k-mesh for transport.
- Evidence: `/app/outputs/bands.dat`

### Step 3: Elastic modulus and deformation potential constants
- Role: process
- Action: Calculate the 2D elastic modulus C2D and deformation potential constants for electrons and holes via energy-strain and band-edge shift under uniaxial strain.
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 4: Carrier mobility and relaxation time estimation
- Role: process
- Action: Use deformation potential theory to estimate carrier mobilities and relaxation times for holes and electrons using effective masses, C2D, and deformation potentials.
- Evidence: `/app/outputs/mobility_tau.csv`

### Step 5: BoltzTraP electronic transport coefficients
- Role: process
- Action: Run BoltzTraP2 using DFT eigenvalues on a dense k-mesh and the estimated relaxation times to obtain Seebeck coefficient, electrical conductivity, electronic thermal conductivity, and power factor as functions of carrier concentration and temperature.
- Evidence: `/app/outputs/transport.npz`

### Step 6: DFT supercell force calculations for interatomic force constants
- Role: process
- Action: Build 5x5x1 supercells and compute forces using DFT for the finite-displacement method. Use Phonopy to extract second-order IFCs; apply a cut-off to compute third-order IFCs up to third nearest neighbors.
- Evidence: `/app/outputs/FORCE_CONSTANTS`

### Step 7: ShengBTE phonon transport and lattice thermal conductivity
- Role: scored
- Action: Run ShengBTE using the IFCs to compute phonon dispersion, lifetimes, and lattice thermal conductivity κ_l as a function of temperature from 300 K to 1000 K. Extract κ_l values and write them to kappa_l_vs_T.csv.
- Output file: `/app/outputs/kappa_l_vs_T.csv`
- Format: csv
- Contract: material, temperature_K, kappa_l_W_mK
- Scoring: scored by hidden verifier

### Step 8: Thermoelectric figure of merit ZT calculation
- Role: scored (load-bearing)
- Action: Combine the electronic transport coefficients (S, σ, κ_e) from step 5 and lattice thermal conductivity κ_l from step 7 to compute ZT = S²σT/(κ_e + κ_l) for p-type and n-type at 600 K over a range of carrier concentrations from 1e18 to 1e22 cm⁻³. Write ZT values to ZT_vs_doping.csv.
- Output file: `/app/outputs/ZT_vs_doping.csv`
- Format: csv
- Contract: material, carrier_type, carrier_concentration_cm-3, ZT
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kappa_l_vs_T.csv`
- `/app/outputs/ZT_vs_doping.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kappa_l_vs_T.csv
- path: `/app/outputs/kappa_l_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Lattice thermal conductivity of monolayer ZrSe2 and HfSe2 from 300 K to 1000 K. The checker verifies structural consistency and trend adherence based on the paper's findings (details hidden).
- schema:
  - `type`: table
  - `required_columns`: `material`, `temperature_K`, `kappa_l_W_mK`
  - `units`:
    - `material`: string
    - `temperature_K`: float
    - `kappa_l_W_mK`: float

### ZT_vs_doping.csv
- path: `/app/outputs/ZT_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermoelectric figure of merit ZT as a function of carrier concentration at 600 K for p-type and n-type monolayer ZrSe2 and HfSe2. The checker verifies structural consistency and trend adherence based on the paper's findings (details hidden).
- schema:
  - `type`: table
  - `required_columns`: `material`, `carrier_type`, `carrier_concentration_cm-3`, `ZT`
  - `units`:
    - `material`: string
    - `carrier_type`: string
    - `carrier_concentration_cm-3`: float
    - `ZT`: float

Notes: The checker performs structural/trend audits on the output files; reward is proportional to compliance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kappa_l_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "temperature_K",
          "kappa_l_W_mK"
        ],
        "units": {
          "material": "string",
          "temperature_K": "float",
          "kappa_l_W_mK": "float"
        }
      },
      "description": "Lattice thermal conductivity of monolayer ZrSe2 and HfSe2 from 300 K to 1000 K. The checker verifies structural consistency and trend adherence based on the paper's findings (details hidden)."
    },
    {
      "file": "ZT_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "carrier_type",
          "carrier_concentration_cm-3",
          "ZT"
        ],
        "units": {
          "material": "string",
          "carrier_type": "string",
          "carrier_concentration_cm-3": "float",
          "ZT": "float"
        }
      },
      "description": "Thermoelectric figure of merit ZT as a function of carrier concentration at 600 K for p-type and n-type monolayer ZrSe2 and HfSe2. The checker verifies structural consistency and trend adherence based on the paper's findings (details hidden)."
    }
  ],
  "notes": "The checker performs structural/trend audits on the output files; reward is proportional to compliance."
}
```

## How you are scored
A hidden verifier reads your kappa_l_vs_T.csv and ZT_vs_doping.csv independently and checks them against a set of structural constraints and trend requirements derived from the reference results. The verifier does not depend on your self-reported aggregate numbers; it evaluates the entire data series for compliance. The final reward is a weighted combination of the scores for each output file, with total weight distributed among the verifier checks. Meeting all required trends and threshold conditions yields a maximum reward of 1.0; partial compliance yields a proportional reward. Simply reporting a final number without producing the full data series will result in a low or zero reward.
