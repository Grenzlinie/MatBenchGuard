# Monte Carlo Calculation of Thermodynamic Properties for a Molten Alkali Chloride Mixture

## Problem background
This task addresses the thermodynamic properties of the liquid NaCl–KCl system. Molten salt mixtures are important in high-temperature chemistry and electrochemistry. The mixing of NaCl and KCl has been studied experimentally, and theoretical simulations can reveal details of the non-ideal mixing behaviour. Here we aim to compute the molar volume, internal energy, entropy, Gibbs free energy, and the resulting mixing properties for liquid NaCl, KCl, and the equimolar (Na,K)Cl mixture at 1083 K and zero pressure, using Monte Carlo simulations with a realistic effective pair potential. The exercise illustrates whether a classical Huggins‑Mayer potential can reproduce these key thermodynamic observables.

## Approach
The simulation models each molten salt system as a cubic cell containing 216 ions (108 cations, 108 anions) with periodic boundary conditions. Ion interactions are described by the Huggins‑Mayer pair potential:

φ_{ij}(r) = z_i z_j e² r⁻¹ + b_{ij} exp(−r/ρ) + c_{ij} r⁻⁶ + d_{ij} r⁻⁸

where the terms represent Coulomb, Born–Mayer repulsion, dipole–dipole dispersion, and dipole–quadrupole dispersion, respectively. For pure NaCl and KCl, the repulsion and dispersion parameters (b_{ij}, ρ, c_{ij}, d_{ij}) are fixed by literature values (see Step 1). For the equimolar mixture, parameters are derived from the pure‑salt data using prescribed mixing rules: ρ is the arithmetic mean, b_{ij} follows an adjusted Pauling/Tosi–Fumi scheme, and dispersion coefficients come from Mayer’s single‑ion relations with the chloride polarizability averaged between NaCl and KCl.

Long‑range Coulomb interactions are evaluated with the Ewald summation method. Monte Carlo simulations are performed in the canonical (N,V,T) ensemble at T = 1083 K. For each system, two molar volumes are chosen to bracket zero pressure. Starting from an ideal NaCl lattice, a thorough equilibration is carried out followed by production runs (see Workflow steps for the exact sequence). Ensemble averages of the internal energy components (Coulomb, repulsion, and both dispersion contributions) and of the pressure are collected. Entropy is estimated using, for example, the effective free‑volume method or any other reasonable approach that yields comparable values.

Linear interpolation of the data at the two volumes to zero pressure gives the molar volume V, internal energy E, entropy S, and Gibbs free energy G for each system. Finally, the mixing properties ΔV, ΔE, ΔS, ΔG are obtained as the differences between the equimolar mixture and the pure components.

## Reproduction target
Produce a CSV file `thermodynamic_properties.csv` containing the zero‑pressure thermodynamic properties for liquid NaCl, KCl, and (Na,K)Cl at T=1083 K. The file must have columns:

- system: NaCl, KCl, or (Na,K)Cl
- V_cm3mol: molar volume in cm³/mol
- E_kcalmol: internal energy in kcal/mol
- S_calmolK: entropy in cal/(mol·K)
- G_kcalmol: Gibbs free energy in kcal/mol
- delta_V_cm3mol: change in molar volume on mixing (cm³/mol)
- delta_E_kcalmol: change in internal energy on mixing (kcal/mol)
- delta_S_calmolK: change in entropy on mixing (cal/(mol·K))
- delta_G_kcalmol: change in Gibbs free energy on mixing (kcal/mol)

Each row corresponds to one system; the mixture row should include both its pure‑component properties and the mixing quantities. Include estimated standard deviations where they are available. The values must be obtained from the Monte Carlo simulation workflow described in the steps; no other source is acceptable.

## Assets
No external datasets, pre‑trained models, or proprietary tools are required. All necessary potential‑parameter values are provided within the step instructions. The simulation requires a standard scientific computing environment capable of Monte Carlo sampling and linear algebra (e.g., Python with NumPy/SciPy, or C/C++/Fortran). The Ewald summation and the Huggins‑Mayer potential can be implemented directly in such an environment. If using Python, typical packages are numpy, scipy, and the csv standard library. No GPU acceleration is needed.

## Potential Parameters

The Huggins-Mayer pair potential parameters for NaCl, KCl, and the equimolar (Na,K)Cl mixture are taken from Table 1 of the paper. The mixing rules and adjusted Pauling constants are specified below.

**Adjusted Pauling constants** (used instead of the standard Pauling values):
- c'_++ = 1.11
- c'_+- = 0.96
- c'_-- = 0.75
- The constant b = 0.338 × 10⁻¹² erg = 0.338e-12 erg.

**1/ρ values** (ρ is the repulsion range parameter):
- NaCl: 1/ρ = 3.15 Å⁻¹ → ρ = 0.3175 Å
- KCl: 1/ρ = 2.97 Å⁻¹ → ρ = 0.3367 Å
- (Na,K)Cl mixture: 1/ρ = 3.06 Å⁻¹ → ρ = 0.3268 Å (arithmetic mean of the pure-salt values)

**Table of b_ij, c_ij, d_ij** (energies in erg; multiply by the factor given in the column header):

| System       | i      | j      | b_ij (10⁻⁹ erg) | c_ij (10⁻¹² erg·Å⁶) | d_ij (10⁻¹² erg·Å⁸) |
|--------------|--------|--------|-----------------|----------------------|---------------------|
| NaCl         | Na⁺   | Na⁺   | 0.596           | 1.68                 | 0.8                 |
| NaCl         | Na⁺   | Cl⁻   | 1.906           | 11.2                 | 13.9                |
| NaCl         | Cl⁻   | Cl⁻   | 5.504           | 116.0                | 233.0               |
| KCl          | K⁺    | K⁺    | 2.230           | 24.3                 | 24.0                |
| KCl          | K⁺    | Cl⁻   | 2.772           | 48.0                 | 73.0                |
| KCl          | Cl⁻   | Cl⁻   | 3.110           | 125.0                | 250.0               |
| (Na,K)Cl     | Na⁺   | Na⁺   | 0.483           | 1.68                 | 0.8                 |
| (Na,K)Cl     | Na⁺   | K⁺    | 1.184           | 6.27                 | 4.6                 |
| (Na,K)Cl     | Na⁺   | Cl⁻   | 1.581           | 11.2                 | 13.9                |
| (Na,K)Cl     | K⁺    | K⁺    | 2.903           | 24.3                 | 24.0                |
| (Na,K)Cl     | K⁺    | Cl⁻   | 3.646           | 48.0                 | 73.0                |
| (Na,K)Cl     | Cl⁻   | Cl⁻   | 4.137           | 123.0                | 246.0               |

**Mixing rules for the mixture**:
- ρ(mix) = (ρ(NaCl) + ρ(KCl)) / 2.
- b_ij for the mixture derived from the adjusted Pauling/Tosi–Fumi scheme using the given b constant and ionic radii; the values are listed in the table.
- Dispersion parameters for the mixture: c_{Na⁺K⁺} and d_{Na⁺K⁺} are obtained from Mayer's single-ion relations. For Cl⁻ in the mixture, use the arithmetic mean of the Cl⁻ polarizabilities from NaCl and KCl. The resulting c_ij and d_ij for all mixture pairs are listed above.

## Workflow steps

### Step 1: Construct Huggins-Mayer Potential Parameters
- Role: process
- Action: Using the Potential Parameters section above, assemble the pair potential parameters for NaCl, KCl, and the (Na,K)Cl mixture. The Huggins-Mayer form is φ_ij(r) = z_i z_j e² r⁻¹ + b_ij exp(-r/ρ) + c_ij r⁻⁶ + d_ij r⁻⁸. For each system collect all pair interactions. Write all parameters (ρ, b_ij, c_ij, d_ij with appropriate units) for each ion pair into a JSON file. You may include atomic charges (z_Na = +1, z_K = +1, z_Cl = -1) and the elementary charge e. Provide the full parameter set as evidence.
- Evidence: `/app/outputs/potential_parameters.json`

### Step 2: Monte Carlo Simulation and Thermodynamic Properties
- Role: scored (load-bearing)
- Action: For each system (NaCl, KCl, equimolar (Na,K)Cl), perform canonical Monte Carlo simulations at T=1083 K using a cubic cell with 216 ions, periodic boundary conditions, and Ewald summation for Coulomb energies. For each system, select two molar volumes bracketing zero pressure. Equilibrate from an ideal NaCl lattice: melt over 100,000 configurations; then generate 225,000 configurations per (V,T) point, discarding the first 25,000 for equilibration, using the last 200,000 for averaging. For the mixture, extend pre-equilibration to 1.2×10⁶ configurations and allow 75,000 equilibration before averaging. Compute internal energy components, pressure, and entropy (e.g., effective free volume method). Interpolate linearly to zero pressure to obtain molar volume V, internal energy E, entropy S, Gibbs free energy G. Calculate mixing properties ΔV, ΔE, ΔS, ΔG from pure and mixture values. Output results to thermodynamic_properties.csv.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: CSV with columns: system, V_cm3mol, E_kcalmol, S_calmolK, G_kcalmol, delta_V_cm3mol, delta_E_kcalmol, delta_S_calmolK, delta_G_kcalmol. Each row corresponds to one system (NaCl, KCl, (Na,K)Cl). Include numeric values and estimated uncertainties.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduced zero-pressure thermodynamic properties and mixing properties for liquid NaCl, KCl, and equimolar (Na,K)Cl at T=1083 K.
- schema:
  - `type`: table
  - `required_columns`: `system`, `V_cm3mol`, `E_kcalmol`, `S_calmolK`, `G_kcalmol`, `delta_V_cm3mol`, `delta_E_kcalmol`, `delta_S_calmolK`, `delta_G_kcalmol`
  - `column_descriptions`:
    - `system`: System identifier: NaCl, KCl, or (Na,K)Cl
    - `V_cm3mol`: Molar volume in cm³/mol (with uncertainty)
    - `E_kcalmol`: Internal energy in kcal/mol (with uncertainty)
    - `S_calmolK`: Entropy in cal/(mol·K) (with uncertainty)
    - `G_kcalmol`: Gibbs free energy in kcal/mol (with uncertainty)
    - `delta_V_cm3mol`: Change in molar volume on mixing in cm³/mol
    - `delta_E_kcalmol`: Change in internal energy on mixing in kcal/mol
    - `delta_S_calmolK`: Change in entropy on mixing in cal/(mol·K)
    - `delta_G_kcalmol`: Change in Gibbs free energy on mixing in kcal/mol

Notes: The scored output is compared against hidden reference values from the paper's Monte Carlo results (Tables 2 and 3) with appropriate tolerance windows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "V_cm3mol",
          "E_kcalmol",
          "S_calmolK",
          "G_kcalmol",
          "delta_V_cm3mol",
          "delta_E_kcalmol",
          "delta_S_calmolK",
          "delta_G_kcalmol"
        ],
        "column_descriptions": {
          "system": "System identifier: NaCl, KCl, or (Na,K)Cl",
          "V_cm3mol": "Molar volume in cm³/mol (with uncertainty)",
          "E_kcalmol": "Internal energy in kcal/mol (with uncertainty)",
          "S_calmolK": "Entropy in cal/(mol·K) (with uncertainty)",
          "G_kcalmol": "Gibbs free energy in kcal/mol (with uncertainty)",
          "delta_V_cm3mol": "Change in molar volume on mixing in cm³/mol",
          "delta_E_kcalmol": "Change in internal energy on mixing in kcal/mol",
          "delta_S_calmolK": "Change in entropy on mixing in cal/(mol·K)",
          "delta_G_kcalmol": "Change in Gibbs free energy on mixing in kcal/mol"
        }
      },
      "description": "Reproduced zero-pressure thermodynamic properties and mixing properties for liquid NaCl, KCl, and equimolar (Na,K)Cl at T=1083 K."
    }
  ],
  "notes": "The scored output is compared against hidden reference values from the paper's Monte Carlo results (Tables 2 and 3) with appropriate tolerance windows."
}
```

## How you are scored
A hidden verifier independently checks each workflow step’s output artifact. For the scored step (Step 2), the verifier reads `thermodynamic_properties.csv`, extracts the reported values, and compares them against a confidential reference. The comparison uses appropriate tolerance windows that account for the expected spread of a correct implementation; no prior knowledge of the paper’s numbers is required. Merely reporting the expected numbers without performing the required simulations is detectable and does not pass. The final reward is a number between 0 and 1 that reflects how well the computed quantities agree with the reference. The exact scoring algorithm and the reference values are not disclosed.
