# Oxygen vacancy formation energy in crystalline and amorphous IGZO using DFT

## Problem background
Oxygen vacancies in indium–gallium–zinc oxide (IGZO) are deep-level defects that strongly impact the electrical characteristics of IGZO-based thin-film transistors. Experiments suggest that increasing crystallinity reduces the density of these defect states, but a direct comparison of vacancy formation in crystalline versus amorphous regions is challenging because separate calculations use different reference energies. This task addresses that gap by constructing a single complex model that contains both a crystalline and an amorphous IGZO region, allowing direct calculation of oxygen vacancy formation energies and a fair comparison of the two phases.

## Approach
The approach is based on first-principles density functional theory (DFT) using the PBE generalized gradient approximation and the projector augmented wave (PAW) method. The workflow begins by building a crystalline IGZO supercell from the InGaO₃(ZnO) m=1 unit cell and relaxing it. An amorphous model of the same size is then generated through ab initio molecular dynamics: the crystalline structure is heated to a molten state and quenched stepwise, followed by structural relaxation. These two models are connected along the crystalline b‑axis to form a 224‑atom complex model with a sharp interface; multiple connection geometries are tried and the one with the lowest total energy is selected. An isolated O₂ molecule is calculated to define the oxygen chemical potential (μ_O = ½ E_tot(O₂)). For each of the 128 oxygen sites in the complex model, a vacancy is introduced, the structure is relaxed, and the formation energy is computed as E_form = E_tot(vacancy) − E_tot(perfect) + μ_O. The signed distance of each oxygen site from the central interface (Interface A, negative into the crystalline side) is recorded. The final output tabulates every vacancy site with its distance and formation energy.

## Reproduction target
Produce a single CSV file (`step_01_formation_energies.csv`) with one row per oxygen vacancy site. Each row must contain: an integer oxygen index, the signed distance from Interface A in Å (negative values for sites in the crystalline region), and the formation energy in eV. The hidden verifier will filter sites with distance < –5 Å to form the crystalline far‑region group and sites with distance > 5 Å to form the amorphous region group, compute the average formation energy in each group, and check whether the crystalline average is strictly greater than the amorphous average. This relative trend is the primary target; additionally, the verifier may check the absolute energy scales against reference values, but those tolerances are not disclosed.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for In, Ga, Zn, O (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency
- InGaO3(ZnO) m=1 crystal structure: COD or ICSD entry for InGaO3(ZnO) m=1

## Workflow steps

### Step 1: Build and relax crystalline IGZO model
- Role: process
- Action: Construct the 112-atom crystalline IGZO supercell based on the InGaO3(ZnO) m=1 unit cell and perform DFT relaxation of ionic positions and cell parameters to obtain the optimized structure.
- Evidence: `/app/outputs/crystalline_structure.cif`

### Step 2: Prepare amorphous IGZO model via ab initio molecular dynamics
- Role: process
- Action: Starting from the crystalline model, run ab initio molecular dynamics (NVT ensemble at 3500 K for 7 ps, then stepwise quench at 500 K/ps) to obtain a molten state, then fully relax the quenched structure to get a 112-atom amorphous IGZO model.
- Evidence: `/app/outputs/amorphous_structure.cif`

### Step 3: Construct and relax the crystalline-amorphous complex model
- Role: process
- Action: Connect the crystalline and amorphous models along the b-axis of the crystalline model, ensuring all interatomic distances > 1.4 Å. Generate 10 candidate configurations, relax them with DFT, and select the one with the lowest total energy as the final 224-atom complex model. Record its total energy E_tot(no_defect).
- Evidence: `/app/outputs/complex_model_energy.json`

### Step 4: Compute O2 reference energy
- Role: process
- Action: Calculate the total energy of an isolated O2 molecule using the same DFT settings to obtain the oxygen chemical potential mu_O = 0.5 * E_tot(O2).
- Evidence: `/app/outputs/o2_energy.json`

### Step 5: Calculate oxygen vacancy formation energies for all 128 sites
- Role: scored (load-bearing)
- Action: For each of the 128 oxygen atoms in the complex model: create an oxygen vacancy, fully relax the structure using DFT, compute the total energy E_tot(vacancy), then calculate the formation energy as E_form = E_tot(vacancy) - E_tot(no_defect) + mu_O (O-rich conditions). Compute the signed distance of each vacancy site from Interface A (negative into crystalline region). Output a CSV with one row per vacancy site.
- Output file: `/app/outputs/step_01_formation_energies.csv`
- Format: csv
- Contract: oxygen_index (int), distance_from_interface_A (float, Angstrom), formation_energy (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.csv
- path: `/app/outputs/step_01_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with one row per oxygen vacancy site. The checker will filter by distance (crystalline: < -5 Å; amorphous: > 5 Å) to compute average formation energies and verify the trend.
- schema:
  - `type`: table
  - `required_columns`: `oxygen_index`, `distance_from_interface_A`, `formation_energy`
  - `units`:
    - `distance_from_interface_A`: Angstrom
    - `formation_energy`: eV

Notes: The averages are recomputed by the checker from the raw data; no gold values are provided here. The trend (crystalline average > amorphous average) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "oxygen_index",
          "distance_from_interface_A",
          "formation_energy"
        ],
        "units": {
          "distance_from_interface_A": "Angstrom",
          "formation_energy": "eV"
        }
      },
      "description": "CSV with one row per oxygen vacancy site. The checker will filter by distance (crystalline: < -5 Å; amorphous: > 5 Å) to compute average formation energies and verify the trend."
    }
  ],
  "notes": "The averages are recomputed by the checker from the raw data; no gold values are provided here. The trend (crystalline average > amorphous average) is also verified."
}
```

## How you are scored
Your submission is scored by an automated verifier that reads `/app/outputs/step_01_formation_energies.csv`, extracts the columns, and performs the regional grouping and averaging described in the reproduction target. The score is primarily determined by whether the computed crystalline‑region average exceeds the amorphous‑region average by a sufficient margin. Additional weight may be given to the absolute formation energies, but the exact tolerance is hidden. The intermediate models you build (crystalline, amorphous, complex, O₂ reference) are required to produce physically meaningful formation energies; the verifier does not directly inspect them, but an incorrect or unconverged intermediate will produce erroneous formation energies that likely fail the trend check. All steps must be executed; shortcutting any step is likely to lead to a score of zero. The final reward is a single float between 0 and 1.
