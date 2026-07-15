# Magnetic Anisotropy Energy Computation

## Problem background
Electric-field control of magnetic anisotropy in thin-film oxide/ferromagnet/oxide double-interface structures is a promising route for ultralow-power spintronic devices. The key challenge is to understand how the perpendicular magnetic anisotropy energy (MAE) depends on an applied electric field across the insulating layers, and how the electronic charge at the interface governs that dependence. This work investigates the intrinsic nonlinearity of the MAE under both electron depletion and accumulation conditions, using first-principles density functional theory (DFT) calculations on a MgO/Fe/MgO slab. The target is to determine the MAE as a function of the applied electric field and to correlate it with the number of electrons on the interfacial Fe atom at the right-hand side of the magnetic layer.

## Approach
The approach uses spin-polarized DFT with the generalized gradient approximation (GGA) and spin-orbit coupling (SOC). The system is a periodic slab of MgO(4 atomic monolayers)/Fe(3 atomic monolayers)/MgO(7 atomic monolayers) with vacuum on both sides. An effective screening medium (ESM) is placed adjacent to the right vacuum region to apply an electric field by changing the total electron number of the slab. For seven different net charge states, total energies are computed for magnetization directions along [100] (in-plane) and [001] (out-of-plane). The MAE is obtained from the difference MAE = E[100] - E[001]. The external electric field is estimated from the slope of the electrostatic potential in the vacuum region and corrected by the relative dielectric constant of MgO (εr = 9.8). In addition, the number of electrons on the interfacial Fe atom adjacent to the right MgO layer is extracted from the charge density to examine its correlation with the MAE.

## Reproduction target
Using DFT+SOC calculations (Quantum ESPRESSO with ESM functionality), compute the magnetic anisotropy energy MAE for the MgO(4ML)/Fe(3ML)/MgO(7ML) slab at seven electric-field conditions (corresponding to electron counts ΔNe = -0.02, -0.01, 0.0, 0.005, 0.0075, 0.01, 0.0125). Produce a CSV file mapping the applied electric field (in V/nm) to the MAE (in mJ/m²). Separately, compute the number of electrons on the interfacial Fe atom adjacent to the right MgO layer (Fe(3)) at each electric field and write a second CSV file. The goal is to capture the field-dependent behavior of the MAE and the correlated electron count on Fe(3).

## Assets

- Quantum ESPRESSO: https://gitlab.com/QEF/q-e
- PBE GGA pseudopotentials: https://www.quantum-espresso.org/pseudopotentials
- Effective Screening Medium method reference: 10.1103/PhysRevB.73.115407

## Workflow steps

### Step 1: Slab model construction and structural relaxation at zero electric field
- Role: process
- Action: Build the MgO(4ML)/Fe(3ML)/MgO(7ML) slab with in-plane lattice constant a=0.298 nm, place Fe directly above O at interfaces, and perform DFT structural relaxation at zero electric field using spin-orbit coupling and GGA functional, allowing all atoms except Mg(1) and O(1) to relax along z. Save the relaxed geometry.
- Evidence: `/app/outputs/relaxed_geometry.txt`

### Step 2: DFT total-energy calculations with ESM at seven electric fields
- Role: process
- Action: For each of seven electron counts (ΔNe = -0.02, -0.01, 0.0, 0.005, 0.0075, 0.01, 0.0125 electrons) corresponding to applied electric fields, run spin-polarized DFT+SOC with an effective screening medium (ESM) placed next to the right vacuum. Compute total energy for magnetization along [100] and [001] separately. Record the total energies and the external electric field estimated from the electrostatic potential slope in the vacuum region.
- Evidence: `/app/outputs/total_energies_summary.txt`

### Step 3: Compute MAE vs electric field
- Role: scored (load-bearing)
- Action: From the total energies, calculate MAE = E[100] - E[001] for each electric field (converted to V/nm using the dielectric constant of MgO, εr=9.8). Write a CSV with two columns: field_V_per_nm and mae_mJ_per_m2.
- Output file: `/app/outputs/mae_vs_field.csv`
- Format: csv
- Contract: field_V_per_nm (float), mae_mJ_per_m2 (float)
- Scoring: scored by hidden verifier

### Step 4: Extract number of electrons on Fe(3) vs electric field
- Role: scored
- Action: Using charge density from DFT outputs, compute the number of electrons (NOE) on the interfacial Fe atom adjacent to the right MgO layer (Fe(3)) for each electric field. Write a CSV with columns field_V_per_nm and noe_fe3.
- Output file: `/app/outputs/noe_fe3_vs_field.csv`
- Format: csv
- Contract: field_V_per_nm (float), noe_fe3 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mae_vs_field.csv`
- `/app/outputs/noe_fe3_vs_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mae_vs_field.csv
- path: `/app/outputs/mae_vs_field.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetic anisotropy energy (MAE) as a function of applied electric field, computed from total-energy differences of DFT+SOC calculations under seven charge conditions.
- schema:
  - `type`: table
  - `required_columns`: `field_V_per_nm`, `mae_mJ_per_m2`
  - `units`:
    - `field_V_per_nm`: V/nm
    - `mae_mJ_per_m2`: mJ/m²

### noe_fe3_vs_field.csv
- path: `/app/outputs/noe_fe3_vs_field.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Number of electrons on the interfacial Fe atom Fe(3) adjacent to the right MgO layer, extracted from DFT charge density as a function of electric field.
- schema:
  - `type`: table
  - `required_columns`: `field_V_per_nm`, `noe_fe3`
  - `units`:
    - `field_V_per_nm`: V/nm
    - `noe_fe3`: electrons

Notes: The scoring checker verifies structural trends: for mae_vs_field.csv the MAE must increase under positive fields and exhibit a reversal (increase after an initial decrease) under negative fields; for noe_fe3_vs_field.csv the electron count must show the opposite correlated trend. Absolute values are accepted within a broad range expected from using open-source DFT, but the nonlinear pattern is the primary criterion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mae_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_V_per_nm",
          "mae_mJ_per_m2"
        ],
        "units": {
          "field_V_per_nm": "V/nm",
          "mae_mJ_per_m2": "mJ/m²"
        }
      },
      "description": "Magnetic anisotropy energy (MAE) as a function of applied electric field, computed from total-energy differences of DFT+SOC calculations under seven charge conditions."
    },
    {
      "file": "noe_fe3_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_V_per_nm",
          "noe_fe3"
        ],
        "units": {
          "field_V_per_nm": "V/nm",
          "noe_fe3": "electrons"
        }
      },
      "description": "Number of electrons on the interfacial Fe atom Fe(3) adjacent to the right MgO layer, extracted from DFT charge density as a function of electric field."
    }
  ],
  "notes": "The scoring checker verifies structural trends: for mae_vs_field.csv the MAE must increase under positive fields and exhibit a reversal (increase after an initial decrease) under negative fields; for noe_fe3_vs_field.csv the electron count must show the opposite correlated trend. Absolute values are accepted within a broad range expected from using open-source DFT, but the nonlinear pattern is the primary criterion."
}
```

## How you are scored
A hidden verifier will independently score each submitted artifact. For the MAE and Fe(3) electron-count tables, the verifier checks the structural trends in the data — such as monotonicity, reversals, and the presence of a critical field region — rather than matching exact absolute values, because code and pseudopotential choices can shift absolute numbers. The two scored outputs are combined by weighted sum into the final reward. No single reference value is disclosed; you must genuinely execute the computational workflow described in the steps above and produce the output files.
