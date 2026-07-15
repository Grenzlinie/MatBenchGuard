# Computational Study of Thermoelectric Transport in RuV-based Half-Heusler Semiconductors

## Problem background
Half-Heusler alloys with 18 valence electrons are promising thermoelectric materials that directly convert waste heat into electricity. Their performance is measured by the dimensionless figure of merit ZT, which depends on the Seebeck coefficient, electrical conductivity, and thermal conductivity (both electronic and lattice). This task targets a set of RuV-based half-Heusler compounds (RuVAs, RuVP, and RuVSb) to computationally predict their mechanical stability, vibrational properties, and thermoelectric transport coefficients using first-principles density functional theory and Boltzmann transport equations. The central goal is to compute these properties and identify which compound offers the highest thermoelectric performance, along with the optimal doping conditions.

## Approach
Use an open-source plane-wave DFT code (e.g. Quantum ESPRESSO) with the PBE functional to perform structural relaxations of RuVAs, RuVP, and RuVSb in the face-centered cubic Fm-3m structure. From the relaxed geometries, compute electronic band structures on a dense k-mesh and elastic constants (C11, C12, C44) using a strain-stress approach. Derive mechanical moduli (bulk, shear, Young’s moduli, Poisson’s ratio, anisotropy, Pugh’s ratio) to assess mechanical stability. Calculate harmonic interatomic force constants via DFPT and use PHONOPY to obtain phonon dispersions, confirming dynamical stability (absence of imaginary modes) and Debye temperatures. Feed the PBE band structures into BoltzTraP2 to obtain charge-carrier transport coefficients (Seebeck coefficient, electrical and electronic thermal conductivities over relaxation time) under constant relaxation time approximation for 300–900 K. Obtain Born effective charges and dielectric tensor from DFPT, then compute third‑order force constants on a 4×4×4 supercell and run shengBTE to get lattice thermal conductivity κ_lat. Finally, combine the BoltzTraP outputs with κ_lat, using fixed relaxation times τ = 245 fs and τ = 121 fs, to compute the true ZT and optimal carrier concentration for both p‑ and n‑type doping at each temperature.

## Reproduction target
Produce three scored artifacts under `/app/outputs`:
1. **elastic_moduli_table.csv** – a table of elastic constants and derived mechanical moduli (C11, C12, C44, B, G, Y, B/G ratio, Poisson’s ratio, anisotropy factor) for all three compounds. The values must satisfy Born‑Huang mechanical stability criteria and indicate ductility (B/G > 1.75).
2. **phonon_stability_report.json** – for each compound, a verified flag that no imaginary phonon frequencies exist anywhere in the Brillouin zone and the computed Debye temperature Θ_D.
3. **ZT_results.csv** – the full figure of merit ZT and the corresponding optimal carrier concentration for both p‑ and n‑type doping at 300 K, 500 K, 700 K, and 900 K. The relative ordering among the three compounds for p‑type ZT must follow a consistent trend, with one compound clearly outperforming the others at high temperature.

## Assets

- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- BoltzTraP2: https://bitbucket.org/sousaw/boltztra_p2
- shengBTE: https://www.shengbte.org/

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Perform PBE structural relaxation (atomic positions and lattice vectors) for RuVAs, RuVP, and RuVSb in the cubic Fm-3m structure, starting from initial Wyckoff positions. Save the optimized lattice constants and atomic coordinates.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: PBE band structure and DOS
- Role: process
- Action: Using the relaxed PBE structures, perform a self-consistent field calculation on a dense k-mesh and obtain the electronic band structure and density of states for each compound. Save the band eigenvalues in a format suitable for BoltzTraP.
- Evidence: `/app/outputs/bands_for_boltztrap.dat`

### Step 3: Elastic constants and derived mechanical properties
- Role: scored
- Action: Compute the elastic constants C11, C12, and C44 for each compound using a strain-stress DFT method. Derive bulk modulus B, shear modulus G, Young's modulus Y, Poisson's ratio ν, anisotropy factor A, and Pugh's ratio B/G. Write these to a CSV file with one row per compound.
- Output file: `/app/outputs/elastic_moduli_table.csv`
- Format: csv
- Contract: CSV with columns: compound, C11_GPa, C12_GPa, C44_GPa, B_GPa, G_GPa, Y_GPa, B_G_ratio, nu, A. Values are numeric; compound is a string.
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion and dynamical stability
- Role: scored
- Action: Calculate harmonic second-order interatomic force constants via DFPT for a 2×2×2 supercell of each compound. Use PHONOPY to obtain the phonon dispersion and confirm that no imaginary frequencies exist. Compute the Debye temperature from elastic constants and average sound velocity. Write a JSON file with the stability flag and Debye temperature for each compound.
- Output file: `/app/outputs/phonon_stability_report.json`
- Format: json
- Contract: JSON object with keys 'RuVAs', 'RuVP', 'RuVSb'. Each value is an object { 'phonon_imaginary_modes': false, 'theta_D_K': <number> }.
- Scoring: scored by hidden verifier

### Step 5: BoltzTraP transport coefficients
- Role: process
- Action: Feed the PBE band structure into BoltzTraP2 for each compound. Compute temperature- and chemical-potential-dependent Seebeck coefficient S, electrical conductivity over relaxation time σ/τ, and electronic thermal conductivity over relaxation time κ_e/τ for T = 300, 500, 700, 900 K. Save the results.
- Evidence: `/app/outputs/boltztrap_results.pkl`

### Step 6: Born effective charges and dielectric tensor
- Role: process
- Action: Use DFPT on the primitive cell of each compound to calculate the Born effective charges and the macroscopic dielectric tensor. These are required inputs for polar corrections in ShengBTE.
- Evidence: `/app/outputs/born_data.json`

### Step 7: ShengBTE lattice thermal conductivity
- Role: process
- Action: Compute second-order (harmonic) and third-order (anharmonic) interatomic force constants using finite displacements on a 4×4×4 supercell (Γ-point only). Run shengBTE with these force constants and the Born charges/dielectric tensor to obtain the lattice thermal conductivity κ_lat as a function of temperature (300–900 K).
- Evidence: `/app/outputs/klat_vs_T.csv`

### Step 8: Final ZT calculation and carrier concentration
- Role: scored (load-bearing)
- Action: Combine the BoltzTraP outputs (S, σ/τ, κ_e/τ) with the ShengBTE κ_lat, using fixed relaxation times τ = 245 fs and τ = 121 fs, to compute the true figure of merit ZT for n- and p-type doping of all three compounds at 300, 500, 700, and 900 K. Report the ZT and the corresponding optimal carrier concentration. Write a CSV file with one row per compound, doping type, and temperature.
- Output file: `/app/outputs/ZT_results.csv`
- Format: csv
- Contract: CSV with columns: compound, doping, temp_K, ZT, optimal_carrier_concentration_cm-3. Doping is 'p' or 'n'. ZT is float. Optimal_carrier_concentration_cm-3 is float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli_table.csv`
- `/app/outputs/phonon_stability_report.json`
- `/app/outputs/ZT_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli_table.csv
- path: `/app/outputs/elastic_moduli_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed elastic constants and derived mechanical moduli for all three compounds, to be compared with paper-reported values (Table 2).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11_GPa`, `C12_GPa`, `C44_GPa`, `B_GPa`, `G_GPa`, `Y_GPa`, `B_G_ratio`, `nu`, `A`
  - `items`: object
  - `units`:
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa
    - `B_GPa`: GPa
    - `G_GPa`: GPa
    - `Y_GPa`: GPa
    - `B_G_ratio`: dimensionless
    - `nu`: dimensionless
    - `A`: dimensionless

### phonon_stability_report.json
- path: `/app/outputs/phonon_stability_report.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reports dynamical stability (no imaginary phonon modes) and Debye temperature for each compound, to be compared with paper values (Table 3).
- schema:
  - `type`: object
  - `required`:
    - `RuVAs`: object
    - `RuVP`: object
    - `RuVSb`: object
  - `items`:
    - `phonon_imaginary_modes`: boolean
    - `theta_D_K`: number

### ZT_results.csv
- path: `/app/outputs/ZT_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final thermoelectric figure of merit ZT and optimal carrier concentration for p- and n-type doping, covering the paper's main claim.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `doping`, `temp_K`, `ZT`, `optimal_carrier_concentration_cm-3`
  - `items`: object
  - `units`:
    - `doping`: p or n
    - `temp_K`: K
    - `ZT`: dimensionless
    - `optimal_carrier_concentration_cm-3`: cm^{-3}

Notes: The checker will compare the agent's computed elastic constants, phonon stability report, and ZT values to the paper's reported numbers (Table 2, Table 3, and referenced ZT values) with domain-appropriate tolerances. The relative ordering among compounds and stability criteria (Born-Huang, no imaginary modes) will also be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa",
          "B_GPa",
          "G_GPa",
          "Y_GPa",
          "B_G_ratio",
          "nu",
          "A"
        ],
        "items": {},
        "units": {
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa",
          "B_GPa": "GPa",
          "G_GPa": "GPa",
          "Y_GPa": "GPa",
          "B_G_ratio": "dimensionless",
          "nu": "dimensionless",
          "A": "dimensionless"
        }
      },
      "description": "Computed elastic constants and derived mechanical moduli for all three compounds, to be compared with paper-reported values (Table 2)."
    },
    {
      "file": "phonon_stability_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "RuVAs": "object",
          "RuVP": "object",
          "RuVSb": "object"
        },
        "items": {
          "phonon_imaginary_modes": "boolean",
          "theta_D_K": "number"
        }
      },
      "description": "Reports dynamical stability (no imaginary phonon modes) and Debye temperature for each compound, to be compared with paper values (Table 3)."
    },
    {
      "file": "ZT_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "doping",
          "temp_K",
          "ZT",
          "optimal_carrier_concentration_cm-3"
        ],
        "items": {},
        "units": {
          "doping": "p or n",
          "temp_K": "K",
          "ZT": "dimensionless",
          "optimal_carrier_concentration_cm-3": "cm^{-3}"
        }
      },
      "description": "Final thermoelectric figure of merit ZT and optimal carrier concentration for p- and n-type doping, covering the paper's main claim."
    }
  ],
  "notes": "The checker will compare the agent's computed elastic constants, phonon stability report, and ZT values to the paper's reported numbers (Table 2, Table 3, and referenced ZT values) with domain-appropriate tolerances. The relative ordering among compounds and stability criteria (Born-Huang, no imaginary modes) will also be verified."
}
```

## How you are scored
A hidden verifier independently inspects each of the three scored artifacts. The verifier checks that: the elastic constants satisfy all mechanical stability criteria (C11−C12>0, C11+2C12>0, C44>0) and that derived ratios correctly classify ductility and anisotropy; the phonon report confirms strictly zero imaginary modes and provides Debye temperatures consistent with the computed sound velocities; and the ZT results show a physically meaningful trend where p‑type ZT of one compound is the highest among the three at 900 K and the overall ordering across compounds follows the physics‑driven expectation. The verifier does not compare to a single hard‑coded threshold; instead it evaluates correctness through a combination of structural criteria and trend consistency. The final reward is a weighted sum of these checks, with the main weight on the ZT artifact. There is no partial credit for simply printing values; the agent must execute the full computational pipeline.
