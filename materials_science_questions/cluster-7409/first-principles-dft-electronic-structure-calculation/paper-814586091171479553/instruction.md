# DFT bandgap reduction and polaron mobility in N-doped BiVO4

## Problem background
Bismuth vanadate (BiVO4) is a leading photoanode material for solar water splitting, but its bandgap of approximately 2.5 eV limits the fraction of the solar spectrum it can absorb. Introducing nitrogen dopants and oxygen vacancies into the BiVO4 lattice has been proposed as a way to lower the bandgap and improve charge transport. This computational study examines the electronic structure of pristine and nitrogen-doped BiVO4 with varying levels of oxygen vacancies, using density functional theory (DFT) to compute band structures, dielectric properties, and polaron-related transport quantities, in order to determine whether and how much these defects affect the band gap and electron mobility.

## Approach
The approach is to perform first-principles periodic density functional theory (DFT) calculations using the PBE exchange-correlation functional and ultrasoft pseudopotentials. The crystal structure of pristine monoclinic BiVO4 is taken from a public database. Three systems are studied: (1) pristine BiVO4; (2) charge-balanced N-doped BiVO4, where a fraction of oxygen atoms are replaced by nitrogen and compensating oxygen vacancies are introduced to maintain overall charge neutrality; and (3) N-doped BiVO4 with additional (excess) oxygen vacancies beyond charge balance. For each system, the geometry is optimized and the electronic band structure is computed. The band gap of each system is determined from the band eigenvalues. Following the DFT calculations, the high-frequency and static dielectric constants are obtained using density functional perturbation theory (DFPT). Using the dielectric constants, the small polaron model is employed to estimate polaron binding energies and hopping activation energies for the pristine and charge-balanced N-doped cases, and from these the relative change in electron mobility is estimated. Finally, the optical absorption onset is evaluated from the computed imaginary part of the dielectric function within the random phase approximation, and the redshift of the absorption edge between pristine and N-doped BiVO4 is determined.

## Reproduction target
The reproduction target is to compute the electronic and transport properties of pristine and nitrogen-doped BiVO4 as described in the workflow steps, and to produce the following quantitative results:
- The band gap of pristine BiVO4 and its reduction in the two N-doped cases (charge-balanced and excess vacancies), derivable from the band structure files.
- The high-frequency and static dielectric constants for pristine and charge-balanced N-doped BiVO4.
- The polaron binding energy, hopping activation energies, and the estimated percent enhancement in electron mobility for the charge-balanced N-doped case relative to pristine, based on the small polaron model and the computed dielectric constants and structural parameters.
- The optical absorption onset energies for pristine and charge-balanced N-doped BiVO4 and their difference (redshift).
All results are to be saved in the designated output files under /app/outputs. These quantities should be computed from first principles using the DFT protocol described in the workflow, without requiring any pre-trained model or external experimental input.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE ultrasoft pseudopotentials for Bi, V, O, N: https://www.materialscloud.org/discover/sssp
- Monoclinic BiVO4 crystal structure: ICSD 1006035

## Workflow steps

### Step 1: Pristine BiVO4 band structure
- Role: scored
- Action: Perform periodic DFT calculation (PBE, ultrasoft pseudopotentials) for pristine monoclinic BiVO4: optimize geometry, compute band structure along a high-symmetry path, and save the band eigenvalues.
- Output file: `/app/outputs/bandstructure_pristine.dat`
- Format: txt
- Contract: Each line contains five space-separated fields: k_x k_y k_z spin_index eigenvalue (eV). spin_index is 0 (the calculation is non-spin-polarized). Eigenvalues are referenced so that occupied states have eigenvalue ≤ 0, unoccupied > 0. Bands are separated by blank lines.
- Scoring: scored by hidden verifier

### Step 2: Charge-balanced N-doped BiVO4 band structure
- Role: scored
- Action: Perform DFT calculation for BiVO4 with charge-balanced nitrogen doping (approximately 6% N substitution and 3% O vacancy per supercell, e.g., 48-atom cell). Compute band structure and save eigenvalues.
- Output file: `/app/outputs/bandstructure_N_charge_balanced.dat`
- Format: txt
- Contract: Same format as bandstructure_pristine.dat: each line k_x k_y k_z spin_index eigenvalue (eV) with spin_index=0; occupied ≤ 0, unoccupied > 0; bands separated by blank lines.
- Scoring: scored by hidden verifier

### Step 3: N-doped BiVO4 with excess O vacancies band structure
- Role: scored
- Action: Perform spin-polarized DFT calculation for BiVO4 with 6% N substitution and 6% O vacancies (excess vacancies). Compute spin-polarized band structure and save eigenvalues.
- Output file: `/app/outputs/bandstructure_N_excess_Vac.dat`
- Format: txt
- Contract: Each line contains five space-separated fields: k_x k_y k_z spin_index eigenvalue (eV). spin_index=0 for spin-up, 1 for spin-down. Eigenvalues are referenced so that occupied states ≤ 0, unoccupied > 0. Bands are separated by blank lines.
- Scoring: scored by hidden verifier

### Step 4: Dielectric constants (pristine and N-doped)
- Role: scored
- Action: For pristine BiVO4 and charge-balanced N-doped BiVO4 (same composition as step02), compute the high-frequency (ε∞) and static (ε0) dielectric constants using density functional perturbation theory (DFPT) with PBE functional. Average over the three lattice directions and save the values.
- Output file: `/app/outputs/dielectric_constants.json`
- Format: json
- Contract: JSON object with keys: pristine_epsilon_inf (float), pristine_epsilon_0 (float), N_doped_epsilon_inf (float), N_doped_epsilon_0 (float).
- Scoring: scored by hidden verifier

### Step 5: Polaron properties and mobility enhancement
- Role: scored (load-bearing)
- Action: Using the dielectric constants from step04 and the small polaron model: compute polaron binding energy W_p = e²/(2 ε_p r_p) with ε_p from 1/ε_p = 1/ε∞ - 1/ε0 and r_p obtained from DFT structural data (≈1.73 Å). Compute small polaron hopping activation energy W_H using the formula W_H = e²/(4π ε_p) * (1/r_p - 1/R) where R is the nearest V–V distance from the supercell. Estimate the relative change in electron mobility (μ ∝ exp(-W_H/kT)). Save all quantities.
- Output file: `/app/outputs/polaron_properties.json`
- Format: json
- Contract: JSON object with keys: W_p_eV (float), W_H_pristine_eV (float), W_H_doped_eV (float), mobility_enhancement_percent (float).
- Scoring: scored by hidden verifier

### Step 6: Optical absorption edge shift
- Role: scored
- Action: Using the DFT wavefunctions of pristine and charge-balanced N-doped BiVO4, compute the imaginary part of the dielectric function ε₂ within the random phase approximation (including local field effects), average over the three lattice directions. Determine the absorption onset energy (the energy at which ε₂ begins to rise) for each system and report the redshift.
- Output file: `/app/outputs/absorption_edge.json`
- Format: json
- Contract: JSON object with keys: pristine_bandgap_edge_eV (float), N_doped_bandgap_edge_eV (float), redshift_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandstructure_pristine.dat`
- `/app/outputs/bandstructure_N_charge_balanced.dat`
- `/app/outputs/bandstructure_N_excess_Vac.dat`
- `/app/outputs/dielectric_constants.json`
- `/app/outputs/polaron_properties.json`
- `/app/outputs/absorption_edge.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandstructure_pristine.dat
- path: `/app/outputs/bandstructure_pristine.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Band structure of pristine BiVO4 from DFT.
- schema:
  - `type`: text
  - `description`: Space-separated columns: k_x k_y k_z spin_index eigenvalue (eV). spin_index=0 (non-spin-polarized). Eigenvalues are referenced so that occupied states ≤ 0, unoccupied > 0. Bands separated by blank lines.

### bandstructure_N_charge_balanced.dat
- path: `/app/outputs/bandstructure_N_charge_balanced.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Band structure of charge-balanced N-doped BiVO4.
- schema:
  - `type`: text
  - `description`: Same format as bandstructure_pristine.dat: k_x k_y k_z spin_index(0) eigenvalue (eV); occupied ≤ 0, unoccupied > 0; bands separated by blank lines.

### bandstructure_N_excess_Vac.dat
- path: `/app/outputs/bandstructure_N_excess_Vac.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Band structure of N-doped BiVO4 with excess O vacancies (spin-polarized).
- schema:
  - `type`: text
  - `description`: Space-separated columns: k_x k_y k_z spin_index eigenvalue (eV). spin_index=0 for spin-up, 1 for spin-down. Eigenvalues referenced so that occupied states ≤ 0, unoccupied > 0. Bands separated by blank lines.

### dielectric_constants.json
- path: `/app/outputs/dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: High-frequency and static dielectric constants for pristine and N-doped BiVO4.
- schema:
  - `type`: object
  - `required_keys`: `pristine_epsilon_inf`, `pristine_epsilon_0`, `N_doped_epsilon_inf`, `N_doped_epsilon_0`
  - `units`:
    - `all`: dimensionless

### polaron_properties.json
- path: `/app/outputs/polaron_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Small polaron properties and computed mobility enhancement.
- schema:
  - `type`: object
  - `required_keys`: `W_p_eV`, `W_H_pristine_eV`, `W_H_doped_eV`, `mobility_enhancement_percent`
  - `units`:
    - `W_p_eV`: eV
    - `W_H_pristine_eV`: eV
    - `W_H_doped_eV`: eV
    - `mobility_enhancement_percent`: %

### absorption_edge.json
- path: `/app/outputs/absorption_edge.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Absorption onset energies and redshift.
- schema:
  - `type`: object
  - `required_keys`: `pristine_bandgap_edge_eV`, `N_doped_bandgap_edge_eV`, `redshift_eV`
  - `units`:
    - `all`: eV

Notes: All outputs are re-derivable from first-principles calculations. The band structure files allow recomputation of band gaps; dielectric constants and polaron quantities are directly compared to hidden paper values. The optical absorption redshift is a result-level comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandstructure_pristine.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Space-separated columns: k_x k_y k_z spin_index eigenvalue (eV). spin_index=0 (non-spin-polarized). Eigenvalues are referenced so that occupied states ≤ 0, unoccupied > 0. Bands separated by blank lines."
      },
      "description": "Band structure of pristine BiVO4 from DFT."
    },
    {
      "file": "bandstructure_N_charge_balanced.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Same format as bandstructure_pristine.dat: k_x k_y k_z spin_index(0) eigenvalue (eV); occupied ≤ 0, unoccupied > 0; bands separated by blank lines."
      },
      "description": "Band structure of charge-balanced N-doped BiVO4."
    },
    {
      "file": "bandstructure_N_excess_Vac.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Space-separated columns: k_x k_y k_z spin_index eigenvalue (eV). spin_index=0 for spin-up, 1 for spin-down. Eigenvalues referenced so that occupied states ≤ 0, unoccupied > 0. Bands separated by blank lines."
      },
      "description": "Band structure of N-doped BiVO4 with excess O vacancies (spin-polarized)."
    },
    {
      "file": "dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "pristine_epsilon_inf",
          "pristine_epsilon_0",
          "N_doped_epsilon_inf",
          "N_doped_epsilon_0"
        ],
        "units": {
          "all": "dimensionless"
        }
      },
      "description": "High-frequency and static dielectric constants for pristine and N-doped BiVO4."
    },
    {
      "file": "polaron_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required_keys": [
          "W_p_eV",
          "W_H_pristine_eV",
          "W_H_doped_eV",
          "mobility_enhancement_percent"
        ],
        "units": {
          "W_p_eV": "eV",
          "W_H_pristine_eV": "eV",
          "W_H_doped_eV": "eV",
          "mobility_enhancement_percent": "%"
        }
      },
      "description": "Small polaron properties and computed mobility enhancement."
    },
    {
      "file": "absorption_edge.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "pristine_bandgap_edge_eV",
          "N_doped_bandgap_edge_eV",
          "redshift_eV"
        ],
        "units": {
          "all": "eV"
        }
      },
      "description": "Absorption onset energies and redshift."
    }
  ],
  "notes": "All outputs are re-derivable from first-principles calculations. The band structure files allow recomputation of band gaps; dielectric constants and polaron quantities are directly compared to hidden paper values. The optical absorption redshift is a result-level comparison."
}
```

## How you are scored
The hidden verifier independently evaluates each of the six scored artifacts produced by the workflow. For the three band structure files, the verifier recomputes the band gap and checks the reduction relative to pristine. For the dielectric constants, the verifier compares the reported values to hidden reference values (within an appropriate tolerance). For the polaron properties, the verifier recomputes the mobility enhancement from the dielectric constants and structural distances and checks that the enhancement meets or exceeds a hidden threshold. For the optical absorption edge, the verifier compares the computed redshift to a hidden reference value. The final reward is a weighted sum of the scores from each artifact, so it is essential to correctly execute the entire workflow and produce valid output files. The verifier does not simply accept reported numbers; it validates the content and re-derives quantities where possible.
