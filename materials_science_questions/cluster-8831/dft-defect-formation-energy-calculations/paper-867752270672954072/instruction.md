# Impair Pair Energetics and Band Gap in PbTe, SnTe, GeTe via DFT Supercell Method

## Problem background
Lead chalcogenides PbTe, SnTe, and GeTe are promising thermoelectric materials. Co-doping with monovalent (Ag) and trivalent (Sb) impurities introduces impurity pairs that can cluster and significantly alter the electronic structure. Understanding the energetic preference of such impurity pairs—whether they prefer specific nearest-neighbor distances—and their effect on the host band structure is crucial for explaining transport properties and designing better thermoelectrics. This task aims to determine the pair binding energies for (Ag,Sb) substitutional impurities in PbTe, SnTe, and GeTe at the second and fifth nearest neighbor distances on the cation sublattice, and to compute the direct band gap at the Gamma point for the PbTe (Ag,Sb) 2nd nearest neighbor configuration.

## Approach
The reproduction uses density functional theory (DFT) with supercell models. For each host material, a bulk structural relaxation will provide relaxed lattice constants. Chemical potentials of the relevant elements will be computed from their standard-state elemental solids. Using the relaxed lattice constants, 2×2×2 cubic supercells (64 atoms) are built and defect configurations are generated: an isolated Ag substitutional, an isolated Sb substitutional, and (Ag,Sb) pairs placed at the second and fifth nearest neighbor distances on the cation sublattice. Ionic relaxations are performed (without spin‑orbit coupling) to obtain total energies. Pair binding energies are derived from defect formation energies, which are computed as the difference between the total energy of the defect supercell, the bulk supercell energy, and the sum of chemical potentials of the added/removed atoms; the binding energy is then the formation energy of the pair minus the sum of the formation energies of the two isolated impurities. Finally, for the relaxed PbTe (Ag,Sb) 2nd n.n. supercell, a band structure calculation including spin‑orbit coupling is performed along a high‑symmetry path, and the direct band gap at the Gamma point is extracted.

## Reproduction target
Compute the pair binding energies (in eV) for (Ag,Sb) co‑doped PbTe, SnTe, and GeTe at the second and fifth nearest neighbor distances, and report them in `/app/outputs/pair_energetics.json`. Additionally, compute the direct band gap at the Gamma point (in eV) for the PbTe (Ag,Sb) 2nd n.n. configuration and report it in `/app/outputs/band_gap_report.json`. All calculations must follow the DFT‑based workflow described in the approach and workflow steps.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org
- SSSP pseudopotentials (efficiency set for PBEsol): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Bulk DFT relaxation of host materials
- Role: process
- Action: Perform DFT structural relaxations for bulk PbTe, SnTe, GeTe (NaCl structure) using Quantum ESPRESSO with scalar-relativistic pseudopotentials and the PBE functional. Obtain theoretical lattice constants and bulk total energies.
- Evidence: `/app/outputs/bulk_results.json`

### Step 2: Elemental chemical potential calculations
- Role: process
- Action: Compute total energies of elemental solids (Ag, Sb, Pb, Sn, Ge, Te) using the same DFT setup to obtain per-atom chemical potentials.
- Evidence: `/app/outputs/chem_potentials.json`

### Step 3: DFT relaxations of defect supercells
- Role: process
- Action: Construct 2x2x2 cubic supercells (64 atoms) for PbTe, SnTe, GeTe using relaxed lattice constants. For each host, create configurations: isolated Ag substitutional, isolated Sb substitutional, (Ag,Sb) pair at 2nd nearest neighbor (pair distance = a), and (Ag,Sb) pair at 5th nearest neighbor (pair distance = a√3). Perform ionic relaxations without spin-orbit coupling and obtain relaxed total energies.
- Evidence: `/app/outputs/defect_energies.json`

### Step 4: Compute pair binding energies
- Role: scored (load-bearing)
- Action: Calculate formation energies using the formula E^f = E_tot(defect) - E_tot(bulk) - sum n_i mu_i, then pair binding energy E_b = E^f(pair) - (E^f(isolated Ag) + E^f(isolated Sb)). Report E_b (in eV) for (Ag,Sb) at 2nd n.n. and 5th n.n. distances for each host.
- Output file: `/app/outputs/pair_energetics.json`
- Format: json
- Contract: JSON object with top-level keys 'PbTe', 'SnTe', 'GeTe'. Each value is an object with keys 'Eb_2nd_nn' and 'Eb_5th_nn' (floats, units eV).
- Scoring: scored by hidden verifier

### Step 5: Band structure calculation for PbTe (Ag,Sb) 2nd n.n.
- Role: process
- Action: Using the relaxed PbTe (Ag,Sb) 2nd n.n. supercell, perform a DFT band structure calculation with spin-orbit coupling (fully relativistic pseudopotentials) along a high-symmetry path that includes the Gamma point. Output Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/band_data.json`

### Step 6: Extract band gap at Gamma
- Role: scored (load-bearing)
- Action: From the band structure eigenvalues, determine the direct band gap at the Gamma point (energy difference between highest occupied and lowest unoccupied eigenvalues at Gamma) and report it in eV.
- Output file: `/app/outputs/band_gap_report.json`
- Format: json
- Contract: JSON object with key 'PbTe_AgSb_2nd_nn_bandgap' (float, units eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pair_energetics.json`
- `/app/outputs/band_gap_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pair_energetics.json
- path: `/app/outputs/pair_energetics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pair binding energies for (Ag,Sb) in each host. Hidden checker compares reported values to reference values within tolerances and checks that Eb_2nd_nn > Eb_5th_nn for each host.
- schema:
  - `type`: object
  - `required`:
    - `PbTe`:
      - `Eb_2nd_nn`: number
      - `Eb_5th_nn`: number
    - `SnTe`:
      - `Eb_2nd_nn`: number
      - `Eb_5th_nn`: number
    - `GeTe`:
      - `Eb_2nd_nn`: number
      - `Eb_5th_nn`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `PbTe.Eb_2nd_nn`: eV
    - `PbTe.Eb_5th_nn`: eV
    - `SnTe.Eb_2nd_nn`: eV
    - `SnTe.Eb_5th_nn`: eV
    - `GeTe.Eb_2nd_nn`: eV
    - `GeTe.Eb_5th_nn`: eV

### band_gap_report.json
- path: `/app/outputs/band_gap_report.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Gamma for PbTe (Ag,Sb) 2nd n.n. configuration. Compared to expected value within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `PbTe_AgSb_2nd_nn_bandgap`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `PbTe_AgSb_2nd_nn_bandgap`: eV

Notes: All energies in electronvolts (eV). Agent must run DFT calculations using the public resources listed. The hidden checker performs result‑level comparison with tolerances and a structural ordering check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pair_energetics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "PbTe": {
            "Eb_2nd_nn": "number",
            "Eb_5th_nn": "number"
          },
          "SnTe": {
            "Eb_2nd_nn": "number",
            "Eb_5th_nn": "number"
          },
          "GeTe": {
            "Eb_2nd_nn": "number",
            "Eb_5th_nn": "number"
          }
        },
        "items": {},
        "required_columns": [],
        "units": {
          "PbTe.Eb_2nd_nn": "eV",
          "PbTe.Eb_5th_nn": "eV",
          "SnTe.Eb_2nd_nn": "eV",
          "SnTe.Eb_5th_nn": "eV",
          "GeTe.Eb_2nd_nn": "eV",
          "GeTe.Eb_5th_nn": "eV"
        }
      },
      "description": "Pair binding energies for (Ag,Sb) in each host. Hidden checker compares reported values to reference values within tolerances and checks that Eb_2nd_nn > Eb_5th_nn for each host."
    },
    {
      "file": "band_gap_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "PbTe_AgSb_2nd_nn_bandgap": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "PbTe_AgSb_2nd_nn_bandgap": "eV"
        }
      },
      "description": "Direct band gap at Gamma for PbTe (Ag,Sb) 2nd n.n. configuration. Compared to expected value within tolerance."
    }
  ],
  "notes": "All energies in electronvolts (eV). Agent must run DFT calculations using the public resources listed. The hidden checker performs result‑level comparison with tolerances and a structural ordering check."
}
```

## How you are scored
A hidden verifier independently examines your submitted artifacts. It reads the pair binding energies from `pair_energetics.json` and the band gap from `band_gap_report.json`, then compares them against reference values derived from the original study. The verifier checks both the absolute energies and the relative ordering of the binding energies between the 2nd and 5th nearest neighbor configurations. The final reward combines the scores from both artifacts; reporting only the correct trends or approximate values without fully executing the workflow will not yield a high score.
