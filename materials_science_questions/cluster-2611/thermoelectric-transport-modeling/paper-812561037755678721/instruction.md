# Thermoelectric Transport and Plasmonic Properties of Nanoparticle-Bridge Systems

## Problem background
Thermoelectric and plasmonic transport in nanostructures built from metal nanoparticles linked by conductive molecular bridges offers a route to high-efficiency energy conversion and tunable optical response. This task investigates periodic chains of ~Au309~ gold nanoparticles connected by three organic bridge molecules: polyacetylene, polypyrrole, and polythiophene. A hybrid quantum‑classical model treats the charge‑transfer process as an LC circuit in which the nanoparticles provide electrostatic capacitance and the ballistic current in the bridge acts as a quantum inductance. The model relates the effective electron mass, the bridge length, and the nanoparticle radius to two experimentally measurable quantities: the charge‑transfer plasmon (CTP) frequency and the thermoelectric Seebeck coefficient. Combined with a lattice thermal conductivity obtained from molecular dynamics, these quantities yield the dimensionless thermoelectric figure of merit ZT. The goal is to compute these properties for the three bridge systems using open‑source first‑principles and classical simulations together with analytical transport models.

## Approach
The computational approach proceeds in five stages. First, periodic unit cells of Au309 nanoparticles linked by each bridge are constructed and their geometries relaxed using the self‑consistent‑charge density‑functional tight‑binding method (SCC‑DFTB). The band structure is calculated and the effective electron mass m* (relative to the free‑electron mass) and the Fermi energy E_Fermi (measured from the conduction band bottom) are extracted from the curvature of the lowest conduction band. Second, a quantum‑classical LC‑oscillator model is applied to convert the effective masses, bridge lengths, and nanoparticle radii into charge‑transfer plasmon frequencies. The model balances electrostatic energy stored in the oppositely charged nanoparticles against the kinetic energy of the ballistic electrons in the bridge, leading to a frequency that depends on R, L, m*, and the number of conduction electrons n (taken as 2). The frequency is evaluated for all three bridges at five nanoparticle radii. Third, the Seebeck coefficient at 300 K is obtained from the universal one‑dimensional thermopower expression, which depends solely on the Fermi energy for a parabolic conduction band. Fourth, the phonon thermal conductivity of the Au309‑polyacetylene periodic chain at 300 K is computed via classical molecular dynamics (LAMMPS) using the Kubo‑Green method, with the REBO potential for the polymer and an EAM potential for gold. The same phonon conductivity value is later used for all three bridge systems. Finally, the thermoelectric figure of merit ZT is calculated at 300 K by combining the Seebeck coefficients, the phonon conductivity, the electrical quantum conductance G = 2e²/h (ballistic, one spin‑degenerate channel), and the Wiedemann‑Franz law for the electronic thermal conductivity.

## Reproduction target
Produce the five scored output files described in the Workflow Steps, each written under `/app/outputs` with the exact formats and schemas specified there:

- `eff_masses.json`: effective masses (in units of m_e) and Fermi energies (eV) for polyacetylene, polypyrrole, and polythiophene bridges.
- `ctp_frequencies.csv`: CTP frequencies (eV) for each bridge type computed at the five radii 4.69, 7.41, 10.0, 12.0, and 14.0 Å.
- `seebeck.csv`: Seebeck coefficients (µV/K) for each bridge at 300 K.
- `chi_vibr.json`: phonon thermal conductivity (W/(m·K)) for the Au309‑polyacetylene chain at 300 K.
- `zt.csv`: thermoelectric figure of merit ZT (dimensionless) for each bridge at 300 K.

The verifier will check that the computed quantities are physically plausible and consistent with the underlying physical model.

## Assets

- DFTB+ (SCC-DFTB): https://dftbplus.org
- LAMMPS: https://lammps.sandia.gov
- SCC-DFTB parameters for Au-C-H-N-O-S: https://dftb.org/parameters/download
- REBO potential for hydrocarbons: https://www.ctcms.nist.gov/potentials
- EAM potential for gold: https://www.ctcms.nist.gov/potentials

## Workflow steps

### Step 1: DFTB+ band structure calculations
- Role: scored
- Action: Build periodic unit cells for Au309 nanoparticles linked by polyacetylene, polypyrrole, and polythiophene bridges (bridge lengths ~14.3, ~41.48, ~44.64 Å). Perform SCC-DFTB geometry relaxation and band structure calculations for each system. Extract the effective electron mass (from the curvature of the conduction band at the Fermi level) and the Fermi energy measured from the conduction band bottom.
- Output file: `/app/outputs/eff_masses.json`
- Format: json
- Contract: JSON object with keys polyacetylene, polypyrrole, polythiophene; each key holds an object with fields m_eff (float, relative to m_e) and E_Fermi (float, eV).
- Scoring: scored by hidden verifier

### Step 2: Charge-transfer plasmon frequency calculation
- Role: scored
- Action: Using the effective masses from step s1 and the analytical quantum-classical model (energy balance leading to a harmonic oscillator with a modified plasma frequency that depends on nanoparticle radius R, bridge length L, effective mass m*, and number of conduction electrons n), compute CTP frequencies for each bridge type at the fixed nanoparticle radii R = 4.69, 7.41, 10.0, 12.0, 14.0 Å. Use the specific bridge lengths and n=2 conduction electrons.
- Output file: `/app/outputs/ctp_frequencies.csv`
- Format: csv
- Contract: CSV with columns: bridge (string, one of polyacetylene/polypyrrole/polythiophene), R_angstrom (float, radius in Å), frequency_eV (float, plasmon frequency in eV).
- Scoring: scored by hidden verifier

### Step 3: Seebeck coefficient calculation
- Role: scored
- Action: Using the Fermi energies from step s1 and the universal 1D Seebeck equation (derived from the temperature dependence of the chemical potential for a parabolic conduction band), compute the Seebeck coefficient S for each system at T = 300 K.
- Output file: `/app/outputs/seebeck.csv`
- Format: csv
- Contract: CSV with columns: bridge (string), S_uV_per_K (float, Seebeck coefficient in µV/K).
- Scoring: scored by hidden verifier

### Step 4: Molecular dynamics phonon thermal conductivity
- Role: scored
- Action: Set up a periodic chain of Au309-polyacetylene in LAMMPS. Apply the REBO potential to the polymer and the EAM potential to gold. Perform classical molecular dynamics at 300 K and compute the phonon thermal conductivity χ_vibr via the Kubo-Green method.
- Output file: `/app/outputs/chi_vibr.json`
- Format: json
- Contract: JSON object with key chi_vibr_W_per_mK (float, thermal conductivity in W/(m·K)).
- Scoring: scored by hidden verifier

### Step 5: Thermoelectric figure of merit calculation
- Role: scored (load-bearing)
- Action: Using the Seebeck coefficients from step s3, the phonon thermal conductivity χ_vibr from step s4 (assumed the same for all bridge types), the electrical quantum conductance G = 2e²/h (ballistic, one spin-degenerate channel), and the Wiedemann-Franz law for electronic thermal conductivity, compute the thermoelectric figure of merit ZT for each bridge system at 300 K.
- Output file: `/app/outputs/zt.csv`
- Format: csv
- Contract: CSV with columns: bridge (string), ZT (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eff_masses.json`
- `/app/outputs/ctp_frequencies.csv`
- `/app/outputs/seebeck.csv`
- `/app/outputs/chi_vibr.json`
- `/app/outputs/zt.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eff_masses.json
- path: `/app/outputs/eff_masses.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective electron masses and Fermi energies extracted from SCC-DFTB band structures for the three nanoparticle-bridge systems.
- schema:
  - `type`: object
  - `required`: `polyacetylene`, `polypyrrole`, `polythiophene`
  - `properties`:
    - `polyacetylene`:
      - `type`: object
      - `required`: `m_eff`, `E_Fermi`
      - `properties`:
        - `m_eff`:
          - `type`: number
          - `description`: effective mass relative to free electron mass
        - `E_Fermi`:
          - `type`: number
          - `description`: Fermi energy in eV, measured from conduction band bottom
    - `polypyrrole`:
      - `type`: object
      - `required`: `m_eff`, `E_Fermi`
      - `properties`:
        - `m_eff`:
          - `type`: number
          - `description`: effective mass relative to free electron mass
        - `E_Fermi`:
          - `type`: number
          - `description`: Fermi energy in eV
    - `polythiophene`:
      - `type`: object
      - `required`: `m_eff`, `E_Fermi`
      - `properties`:
        - `m_eff`:
          - `type`: number
          - `description`: effective mass relative to free electron mass
        - `E_Fermi`:
          - `type`: number
          - `description`: Fermi energy in eV

### ctp_frequencies.csv
- path: `/app/outputs/ctp_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Charge-transfer plasmon frequencies computed from the analytical model for each bridge type at five nanoparticle radii (4.69, 7.41, 10.0, 12.0, 14.0 Å).
- schema:
  - `type`: table
  - `required_columns`: `bridge`, `R_angstrom`, `frequency_eV`
  - `units`:
    - `R_angstrom`: Å
    - `frequency_eV`: eV

### seebeck.csv
- path: `/app/outputs/seebeck.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Seebeck coefficients (thermopower) for the three bridge systems at 300 K, obtained from the universal 1D equation.
- schema:
  - `type`: table
  - `required_columns`: `bridge`, `S_uV_per_K`
  - `units`:
    - `S_uV_per_K`: µV/K

### chi_vibr.json
- path: `/app/outputs/chi_vibr.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon (lattice) thermal conductivity of the Au309-polyacetylene periodic chain from LAMMPS molecular dynamics.
- schema:
  - `type`: object
  - `required`: `chi_vibr_W_per_mK`
  - `properties`:
    - `chi_vibr_W_per_mK`:
      - `type`: number
      - `description`: phonon thermal conductivity in W/(m·K)

### zt.csv
- path: `/app/outputs/zt.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermoelectric figure of merit ZT for the three periodic systems at 300 K, combining electrical quantum conductance, Seebeck coefficient, and total thermal conductivity.
- schema:
  - `type`: table
  - `required_columns`: `bridge`, `ZT`
  - `units`:
    - `ZT`: dimensionless

Notes: The verification compares the effective masses, CTP frequency for polyacetylene at R=7.41 Å, Seebeck coefficients, phonon thermal conductivity, and ZT values to expected ranges; it also checks overall physical consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eff_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "polyacetylene",
          "polypyrrole",
          "polythiophene"
        ],
        "properties": {
          "polyacetylene": {
            "type": "object",
            "required": [
              "m_eff",
              "E_Fermi"
            ],
            "properties": {
              "m_eff": {
                "type": "number",
                "description": "effective mass relative to free electron mass"
              },
              "E_Fermi": {
                "type": "number",
                "description": "Fermi energy in eV, measured from conduction band bottom"
              }
            }
          },
          "polypyrrole": {
            "type": "object",
            "required": [
              "m_eff",
              "E_Fermi"
            ],
            "properties": {
              "m_eff": {
                "type": "number",
                "description": "effective mass relative to free electron mass"
              },
              "E_Fermi": {
                "type": "number",
                "description": "Fermi energy in eV"
              }
            }
          },
          "polythiophene": {
            "type": "object",
            "required": [
              "m_eff",
              "E_Fermi"
            ],
            "properties": {
              "m_eff": {
                "type": "number",
                "description": "effective mass relative to free electron mass"
              },
              "E_Fermi": {
                "type": "number",
                "description": "Fermi energy in eV"
              }
            }
          }
        }
      },
      "description": "Effective electron masses and Fermi energies extracted from SCC-DFTB band structures for the three nanoparticle-bridge systems."
    },
    {
      "file": "ctp_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bridge",
          "R_angstrom",
          "frequency_eV"
        ],
        "units": {
          "R_angstrom": "Å",
          "frequency_eV": "eV"
        }
      },
      "description": "Charge-transfer plasmon frequencies computed from the analytical model for each bridge type at five nanoparticle radii (4.69, 7.41, 10.0, 12.0, 14.0 Å)."
    },
    {
      "file": "seebeck.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bridge",
          "S_uV_per_K"
        ],
        "units": {
          "S_uV_per_K": "µV/K"
        }
      },
      "description": "Seebeck coefficients (thermopower) for the three bridge systems at 300 K, obtained from the universal 1D equation."
    },
    {
      "file": "chi_vibr.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "chi_vibr_W_per_mK"
        ],
        "properties": {
          "chi_vibr_W_per_mK": {
            "type": "number",
            "description": "phonon thermal conductivity in W/(m·K)"
          }
        }
      },
      "description": "Phonon (lattice) thermal conductivity of the Au309-polyacetylene periodic chain from LAMMPS molecular dynamics."
    },
    {
      "file": "zt.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bridge",
          "ZT"
        ],
        "units": {
          "ZT": "dimensionless"
        }
      },
      "description": "Thermoelectric figure of merit ZT for the three periodic systems at 300 K, combining electrical quantum conductance, Seebeck coefficient, and total thermal conductivity."
    }
  ],
  "notes": "The verification compares the effective masses, CTP frequency for polyacetylene at R=7.41 Å, Seebeck coefficients, phonon thermal conductivity, and ZT values to expected ranges; it also checks overall physical consistency."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. Each scored output carries a weight, and the final reward (a single float between 0 and 1) is a weighted combination of the scores for all artifacts. The verifier checks that every required file exists, follows the declared format and schema, and contains physically plausible numerical results. For quantities that are subject to a directional metric (e.g., a figure of merit where higher is better), the scoring is monotonic: meeting or surpassing the expected level earns full credit, and credit only decays when the result gets worse. Format errors or missing files can prevent scoring and reduce the reward. Reporting a memorized value without performing the computations will not yield a full reward, because the verifier also validates internal consistency and the dependence on the conditions specified in the workflow.
