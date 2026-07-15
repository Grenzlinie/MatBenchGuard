# Simulation of SrO Partial Schottky Disorder in SrTiO₃ with Ruddlesden-Popper Phases

## Problem background
The perovskite oxide SrTiO₃ can dissolve excess SrO by forming Ruddlesden-Popper (R-P) phases, which consist of alternating perovskite and rock-salt layers and have the general formula Sr_{n+1}Ti_nO_{3n+1}. Understanding how these phases influence point-defect thermodynamics is important, because earlier computational studies that treated pure SrO as the precipitate obtained SrO partial Schottky disorder energies that were significantly higher than the experimental estimate. This task re-examines that discrepancy by allowing the second phase to be an R-P compound. The question is whether the SrO partial Schottky disorder energy is materially altered when the precipitate is changed from pure SrO (n=0) to an R-P phase (n=1,…,4).

## Approach
The approach uses classical atomistic simulations based on the Born–shell model. Ions carry formal charges and interact through long-range Coulomb forces plus short-range Buckingham-type pair potentials; polarisation is treated with a shell model. All calculations are performed with the GULP code, using one of the published empirical potential sets (the parameters are provided in the task instructions).

First, the lattice energies of the bulk phases — SrO (rock‑salt), TiO₂ (rutile), SrTiO₃ (cubic perovskite), and the R-P phases 1_p (Sr₂TiO₄), 2_p (Sr₃Ti₂O₇), 3_p (Sr₄Ti₃O₁₀), and 4_p (Sr₅Ti₄O₁₃) — are obtained by full lattice relaxation to zero strain at constant pressure. In a separate calculation, the formation energies of an isolated Sr vacancy and an isolated O vacancy in SrTiO₃ are determined with the Mott–Littleton two‑region method (region‑1 radius 10 Å, region‑2 radius 20 Å).

Next, the formation energy Δ_fU_{p+r} of each R-P phase is computed via the perovskite‑plus‑rock‑salt reaction: the lattice energy of a phase of stoichiometry n_p is compared to the sum of n times the SrTiO₃ energy plus the SrO energy. Finally, the SrO partial Schottky disorder energy U_Sch for a given precipitate choice n_p is obtained by adding the Sr vacancy energy, the O vacancy energy, the lattice energy of SrO, and the formation energy Δ_fU_{p+r} (where Δ_fU_{p+r} is taken as zero for n=0). The procedure tests whether the resulting U_Sch values are sensitive to the choice of precipitate stoichiometry.

## Reproduction target
The goal is to run the full simulation pipeline for one potential set and deliver a set of numerical outputs that answer the question above. Specifically, you must:
- compute the lattice energies of SrO, TiO₂, SrTiO₃, and the four R-P phases;
- compute the Sr and O vacancy formation energies in SrTiO₃;
- from these, calculate the perovskite‑plus‑rock‑salt formation energies Δ_fU_{p+r} for each R-P phase;
- finally, calculate the SrO partial Schottky disorder energies U_Sch(n_p) for n = 0, 1, 2, 3, 4.

The variation of U_Sch with n — the difference between the largest and smallest value across the five n — should be small, at most 0.3 eV, demonstrating that the identity of the precipitate phase has negligible effect on the disorder energy. The absolute values of U_Sch for each n must also be physically reasonable and will be checked against reference expectations by the hidden verifier.

## Assets

- GULP (General Utility Lattice Program): http://gulp.curtin.edu.au/gulp/
- Crystallographic structures of SrO, TiO2, SrTiO3, and Ruddlesden-Popper phases 1p-4p: https://materialsproject.org
- Empirical pair-potential parameters (Buckingham + shell model)
- Python (>=3.8) with json, numpy (optional): python3 numpy

## Workflow steps

### Step 1: Prepare crystal structures and GULP input files
- Role: process
- Action: Build atomic structures for SrO (rock-salt), TiO2 (rutile), SrTiO3 (cubic perovskite), and Ruddlesden-Popper phases 1p (Sr2TiO4), 2p (Sr3Ti2O7), 3p (Sr4Ti3O10), and 4p (Sr5Ti4O13) using public crystallographic data. Write GULP input files (.gin) that include the shell model, the chosen Buckingham potential set (provided in the task instructions), and the required geometry. For the Schottky disorder analysis, also prepare a GULP input for the SrTiO3 Mott-Littleton defect calculation (region1 radius 10 Å, region2 radius 20 Å).
- Evidence: `/app/outputs/input_files.tar.gz`

### Step 2: Compute perfect-lattice energies
- Role: scored
- Action: Run GULP on each compound to relax the lattice (convergence to zero strain at constant pressure) and extract the total lattice energy. Collect the results into a single JSON file.
- Output file: `/app/outputs/lattice_energies.json`
- Format: json
- Contract: JSON array of objects: [{ "compound": "<SrO|TiO2|SrTiO3|1_p|2_p|3_p|4_p>", "energy": <float> }]
- Scoring: scored by hidden verifier

### Step 3: Compute defect formation energies
- Role: scored
- Action: Using GULP's Mott-Littleton two-region approach with region‑1 radius 10 Å and region‑2 radius 20 Å, calculate the energies of the Sr vacancy (V_Sr'') and O vacancy (V_O··) in SrTiO3. Save the results.
- Output file: `/app/outputs/defect_energies.json`
- Format: json
- Contract: JSON object: { "V_Sr": { "energy": <float> }, "V_O": { "energy": <float> } }
- Scoring: scored by hidden verifier

### Step 4: Compute R-P phase formation energies (perovskite+rock-salt reaction)
- Role: scored
- Action: From the lattice energies, calculate the perovskite+rock-salt formation energy Δ_fU_{p+r} for each R-P phase n=1–4 according to the relation Δ_fU_{p+r}(n_p) = U(n_p) − n·U(SrTiO3) − U(SrO). Write the results.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON array of objects: [{ "compound": "<1_p|2_p|3_p|4_p>", "Delta_U_p+r": <float> }]
- Scoring: scored by hidden verifier

### Step 5: Calculate SrO partial Schottky disorder energies
- Role: scored (load-bearing)
- Action: Using the defect energies, the lattice energy of SrO, and the Δ_fU_{p+r} values, compute the SrO partial Schottky disorder energy U_Sch(n_p) for n=0,1,2,3,4 according to U_Sch(n_p) = U(V_Sr'') + U(V_O··) + U(SrO) + Δ_fU_{p+r}(n_p), with Δ_fU_{p+r}(0_p) ≡ 0. Save the final values.
- Output file: `/app/outputs/schottky_energies.json`
- Format: json
- Contract: JSON array of objects: [{ "n": <int>, "U_Sch": <float> }]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.json`
- `/app/outputs/defect_energies.json`
- `/app/outputs/formation_energies.json`
- `/app/outputs/schottky_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.json
- path: `/app/outputs/lattice_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice energies of bulk phases SrO, TiO2, SrTiO3, and R-P phases 1p-4p.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `energy`
  - `units`:
    - `energy`: eV

### defect_energies.json
- path: `/app/outputs/defect_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of Sr and O vacancies in SrTiO3.
- schema:
  - `type`: object
  - `required`: `V_Sr`, `V_O`
  - `properties`:
    - `V_Sr`:
      - `type`: object
      - `required`: `energy`
    - `V_O`:
      - `type`: object
      - `required`: `energy`
  - `units`:
    - `energy`: eV

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of R-P phases via the perovskite+rock-salt reaction.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `Delta_U_p+r`
  - `units`:
    - `Delta_U_p+r`: eV

### schottky_energies.json
- path: `/app/outputs/schottky_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: SrO partial Schottky disorder energies for different precipitate choices n=0-4.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `n`, `U_Sch`
  - `units`:
    - `U_Sch`: eV

Notes: All energies in eV. The checker compares each value to hidden paper-reported references with appropriate tolerances. The formation and Schottky energies are the primary scored quantities; lattice and defect energies serve as supporting consistency checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "energy"
          ]
        },
        "units": {
          "energy": "eV"
        }
      },
      "description": "Lattice energies of bulk phases SrO, TiO2, SrTiO3, and R-P phases 1p-4p."
    },
    {
      "file": "defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V_Sr",
          "V_O"
        ],
        "properties": {
          "V_Sr": {
            "type": "object",
            "required": [
              "energy"
            ]
          },
          "V_O": {
            "type": "object",
            "required": [
              "energy"
            ]
          }
        },
        "units": {
          "energy": "eV"
        }
      },
      "description": "Formation energies of Sr and O vacancies in SrTiO3."
    },
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "Delta_U_p+r"
          ]
        },
        "units": {
          "Delta_U_p+r": "eV"
        }
      },
      "description": "Formation energies of R-P phases via the perovskite+rock-salt reaction."
    },
    {
      "file": "schottky_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "n",
            "U_Sch"
          ]
        },
        "units": {
          "U_Sch": "eV"
        }
      },
      "description": "SrO partial Schottky disorder energies for different precipitate choices n=0-4."
    }
  ],
  "notes": "All energies in eV. The checker compares each value to hidden paper-reported references with appropriate tolerances. The formation and Schottky energies are the primary scored quantities; lattice and defect energies serve as supporting consistency checks."
}
```

## How you are scored
The hidden verifier examines each scored JSON artifact independently and combines the scores into a final reward (range 0–1) using predefined stage weights. The checks are:

- **Formation energies** (`formation_energies.json`): each Δ_fU_{p+r} value is compared to a hidden reference with an allowed tolerance that absorbs normal toolchain spread.
- **Schottky disorder energies** (`schottky_energies.json`): first, a structural check verifies that the maximum difference between U_Sch values across n=0–4 does not exceed 0.3 eV. Then each U_Sch value is compared to hidden reference values with an appropriate tolerance. The structural check carries significant weight; without it no high reward is possible.
- **Lattice energies** and **defect energies** are sanity‑checked against hidden references; they contribute a small weight and serve mainly as evidence that the pipeline ran correctly.

The verifier never reveals the reference values or tolerances. Reporting the paper’s numbers without actually running the simulations would produce artefacts that fail the structural check or fall outside the hidden tolerances, resulting in little or no reward.
