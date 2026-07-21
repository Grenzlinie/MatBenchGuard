# Stabilization of stacking faults by Sn in α‑Zr and δ‑ZrH1.5 via DFT calculations

## Problem background
Hydrogen ingress in zirconium-alloy fuel cladding during service leads to the formation of brittle hydride phases, which can degrade mechanical integrity. The primary alloying element, Sn, is known to influence the microstructure, but its effect on planar defects such as stacking faults within the α-Zr matrix and within the hydrides remains an open question. This work addresses that question by using density-functional-theory (DFT) calculations to quantify the energetics of stacking faults in hcp α-Zr and fcc δ-ZrH1.5, both with and without substitutional Sn atoms in the glide plane, and by evaluating the solution enthalpy of Sn in these phases and at the stacking faults. Understanding these energetics sheds light on the distribution of Sn and its role in the microstructural evolution during hydride growth.

## Approach
The computational approach relies on first-principles DFT calculations with the PBE exchange-correlation functional. The procedure consists of (i) constructing slab supercells for the basal (0001) plane of α-Zr and the (111) plane of δ-ZrH1.5, with periodic in-plane dimensions and a vacuum layer; (ii) introducing substitutional Sn atoms in the glide plane at several coverages, using a single representative configuration per coverage; (iii) for each configuration, rigidly shifting one half of the slab along the glide direction over a fine grid of displacements, allowing only perpendicular ionic relaxation, to map the generalized stacking fault (GSF) energy surface; (iv) extracting the stable stacking fault (SSF) energy at the local minimum and the unstable stacking fault (USF) energy at the preceding maximum for each coverage; and (v) computing the solution enthalpy of Sn in bulk α-Zr, bulk δ-ZrH1.5, and at the stacking-fault sites in both phases from total energy differences relative to the pure host phases and to bulk β-Sn, using the chemical potential of hydrogen determined from a δ-ZrH1.5 calculation. All DFT calculations are to be performed with an open-source plane-wave/PAW code and standard pseudopotentials.

## Reproduction target
The target is to compute and report in structured CSV files: (A) the SSF and USF energies (in eV per Å²) for the basal plane of α-Zr as a function of Sn coverage C = 0, 0.125, 0.25, 0.375, 0.5, 0.75, 1.0; (B) the SSF and USF energies for the (111) plane of δ-ZrH1.5 at C = 0 and at one non-zero coverage; and (C) the solution enthalpy of Sn (in eV) in the bulk and at a stacking fault for both α-Zr and δ-ZrH1.5. These three CSVs constitute the full reproduction artifact.

## Assets

- Open‑source DFT code with PBE exchange‑correlation and PAW or equivalent pseudopotentials (e.g., Quantum ESPRESSO, GPAW, CP2K)
- Standard crystallographic structures of hcp α‑Zr and fcc δ‑ZrH1.5

## Workflow steps

### Step 1: Compute hydrogen chemical potential E(H)
- Role: process
- Action: Using DFT, perform total energy calculations for a δ‑ZrH1.5 supercell and for the same supercell containing one additional H atom. Compute the H chemical potential E(H) as the energy difference E(Zr_nH_{1.5n}+H) − n·E(ZrH_{1.5}). This value is needed later for solution enthalpy calculations.
- Evidence: none

### Step 2: Run DFT GSF total energy calculations for α‑Zr and δ‑ZrH1.5
- Role: process
- Action: Construct slab supercells: (a) α‑Zr (0001) slab with periodic in‑plane axes along [01-10] and [2-1-10], vacuum ~10 Å; (b) δ‑ZrH1.5 (111) slab with periodic in‑plane axes along [1-10] and [11-2], vacuum ~10 Å. For α‑Zr, substitute Sn atoms in the glide plane at coverages C = 0, 0.125, 0.25, 0.375, 0.5, 0.75, 1.0 (one representative configuration per coverage). For δ‑ZrH1.5, introduce Sn at C = 0 and one non‑zero coverage (e.g., C = 0.166). For each structure, rigidly shift the upper block along the glide direction (α‑Zr: [01-10]; hydride: [‑211]) sampling a fine grid of displacements. At each displacement allow only ionic relaxations perpendicular to the fault plane. Record the total energy for every displacement and structure.
- Evidence: none

### Step 3: Extract α‑Zr GSF energies
- Role: scored (load-bearing)
- Action: From the raw DFT energies, compute the generalized stacking fault energy surface E_GSF(f) = (E(f) − E(0))/A, where A is the glide‑plane area. For each coverage, identify the stable stacking fault (SSF) energy at the local minimum at displacement b/3 and the unstable stacking fault (USF) energy at the preceding maximum along the [01-10] path. Report all SSF and USF values.
- Output file: `/app/outputs/step_01_alpha_gsf_energies.csv`
- Format: csv
- Contract: CSV with columns: coverage_C (float, unitless), USF_energy_eV_per_A2 (float), SSF_energy_eV_per_A2 (float).
- Scoring: scored by hidden verifier

### Step 4: Extract δ‑ZrH1.5 GSF energies
- Role: scored (load-bearing)
- Action: Similarly, compute the generalized stacking fault energy curves for the (111) plane of δ‑ZrH1.5 and extract the SSF energy (intrinsic stacking fault minimum) and the USF energy (maximum that precedes it) for each coverage. Report the results.
- Output file: `/app/outputs/step_02_hydride_gsf_energies.csv`
- Format: csv
- Contract: CSV with columns: phase (string: 'delta'), coverage_C (float), USF_energy_eV_per_A2 (float), SSF_energy_eV_per_A2 (float). At least two rows.
- Scoring: scored by hidden verifier

### Step 5: Compute Sn solution enthalpies
- Role: scored (load-bearing)
- Action: Run additional DFT total energy calculations: bulk hcp α‑Zr (perfect supercell), bulk hcp α‑Zr with one substitutional Sn atom, bulk δ‑ZrH1.5 (perfect supercell), bulk δ‑ZrH1.5 with one substitutional Sn atom, bulk β‑Sn, and the stacking‑fault supercells (with and without Sn) from the α‑Zr and δ‑ZrH1.5 GSF calculations. Using E(H) from step 0, compute the solution enthalpy of Sn in (i) bulk α‑Zr, (ii) α‑Zr stacking fault, (iii) bulk δ‑ZrH1.5, and (iv) δ‑ZrH1.5 stacking fault. Report these four values.
- Output file: `/app/outputs/step_03_solution_enthalpies.csv`
- Format: csv
- Contract: CSV with columns: phase (string: 'alpha' or 'delta'), location (string: 'bulk' or 'stacking_fault'), solution_enthalpy_eV (float). Four rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_alpha_gsf_energies.csv`
- `/app/outputs/step_02_hydride_gsf_energies.csv`
- `/app/outputs/step_03_solution_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_alpha_gsf_energies.csv
- path: `/app/outputs/step_01_alpha_gsf_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stable and unstable stacking fault energies for α‑Zr at each Sn coverage. Values are compared to the paper’s reference values with tolerances, and the required monotonic trend (decrease up to C≈0.375, increase beyond) is also checked.
- schema:
  - `type`: table
  - `required_columns`: `coverage_C`, `USF_energy_eV_per_A2`, `SSF_energy_eV_per_A2`
  - `units`:
    - `coverage_C`: unitless
    - `USF_energy_eV_per_A2`: eV per Å²
    - `SSF_energy_eV_per_A2`: eV per Å²

### step_02_hydride_gsf_energies.csv
- path: `/app/outputs/step_02_hydride_gsf_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: SSF and USF energies for δ‑ZrH1.5 at C=0 and one non‑zero coverage. Numeric comparison to paper reference values; additionally the SSF at non‑zero coverage must be lower than at C=0.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `coverage_C`, `USF_energy_eV_per_A2`, `SSF_energy_eV_per_A2`
  - `units`:
    - `phase`: string
    - `coverage_C`: unitless
    - `USF_energy_eV_per_A2`: eV per Å²
    - `SSF_energy_eV_per_A2`: eV per Å²

### step_03_solution_enthalpies.csv
- path: `/app/outputs/step_03_solution_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Solution enthalpies of Sn in bulk and at stacking faults for α‑Zr and δ‑ZrH1.5. The checker verifies the ordering requirements: bulk α‑Zr < bulk δ‑ZrH1.5, stacking‑fault α‑Zr < bulk α‑Zr, stacking‑fault δ‑ZrH1.5 < bulk δ‑ZrH1.5. Absolute values are not required to match paper numbers exactly.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `location`, `solution_enthalpy_eV`
  - `units`:
    - `phase`: string
    - `location`: string
    - `solution_enthalpy_eV`: eV

Notes: All outputs are produced by the agent from DFT calculations; the hidden checker uses the paper’s reported values as reference (with method‑appropriate tolerances) and verifies the required structural trends. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_alpha_gsf_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coverage_C",
          "USF_energy_eV_per_A2",
          "SSF_energy_eV_per_A2"
        ],
        "units": {
          "coverage_C": "unitless",
          "USF_energy_eV_per_A2": "eV per Å²",
          "SSF_energy_eV_per_A2": "eV per Å²"
        }
      },
      "description": "Stable and unstable stacking fault energies for α‑Zr at each Sn coverage. Values are compared to the paper’s reference values with tolerances, and the required monotonic trend (decrease up to C≈0.375, increase beyond) is also checked."
    },
    {
      "file": "step_02_hydride_gsf_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "coverage_C",
          "USF_energy_eV_per_A2",
          "SSF_energy_eV_per_A2"
        ],
        "units": {
          "phase": "string",
          "coverage_C": "unitless",
          "USF_energy_eV_per_A2": "eV per Å²",
          "SSF_energy_eV_per_A2": "eV per Å²"
        }
      },
      "description": "SSF and USF energies for δ‑ZrH1.5 at C=0 and one non‑zero coverage. Numeric comparison to paper reference values; additionally the SSF at non‑zero coverage must be lower than at C=0."
    },
    {
      "file": "step_03_solution_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "location",
          "solution_enthalpy_eV"
        ],
        "units": {
          "phase": "string",
          "location": "string",
          "solution_enthalpy_eV": "eV"
        }
      },
      "description": "Solution enthalpies of Sn in bulk and at stacking faults for α‑Zr and δ‑ZrH1.5. The checker verifies the ordering requirements: bulk α‑Zr < bulk δ‑ZrH1.5, stacking‑fault α‑Zr < bulk α‑Zr, stacking‑fault δ‑ZrH1.5 < bulk δ‑ZrH1.5. Absolute values are not required to match paper numbers exactly."
    }
  ],
  "notes": "All outputs are produced by the agent from DFT calculations; the hidden checker uses the paper’s reported values as reference (with method‑appropriate tolerances) and verifies the required structural trends. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each of the three output files, weighting them according to their contribution to the main claim. The verifier checks trends among the computed quantities, such as the dependence of fault energies on Sn coverage and the relative ordering of solution enthalpies, and compares the reported values to previously published reference values with tolerances appropriate for DFT PBE calculations. The final reward is a combined score reflecting how well the computed results match the expected physical trends and the reference data. A simple textual match to previously published numbers is neither required nor sufficient; the agent must perform the full DFT workflow to produce the results.
