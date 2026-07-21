# Magnetic Ground State of FeMn Monolayer on Co(001) via DFT

## Problem background
Exchange bias at ferromagnet/antiferromagnet interfaces is crucial for spin‑valve devices. The magnetic coupling and the magnitude and orientation of induced moments in an ordered Fe₅₀Mn₅₀ monolayer on a Co(001) FCC substrate are still actively investigated. X‑ray magnetic circular dichroism experiments have detected net magnetic moments on Fe and Mn when in contact with Co, but the ground‑state magnetic configuration — whether the Fe and Mn moments align parallel or antiparallel to the Co magnetization — and the precise values of those induced moments remain to be determined from first principles.

## Approach
We use spin‑polarized density functional theory (DFT) within the generalized gradient approximation of Perdew and Wang (GGA‑PW91) to model the FeMn/Co interface. The system is represented by a periodic slab containing a seven‑layer Co(001) film with an ordered Fe₅₀Mn₅₀ monolayer on each face; five layers of empty spheres are added to describe the vacuum. The relative orientation of the Fe and Mn magnetic moments with respect to the Co magnetization is explored by imposing four collinear spin configurations:

- Fe↑Mn↑ (both moments parallel to Co)
- Fe↑Mn↓ (Fe parallel, Mn antiparallel)
- Fe↓Mn↑ (Fe antiparallel, Mn parallel)
- Fe↓Mn↓ (both antiparallel)

For each configuration a full spin‑polarized DFT total‑energy calculation is performed, and the atomic magnetic moments on Fe and Mn are extracted. Comparing the total energies reveals which spin arrangement is the most stable and quantifies the energetic penalty of the alternative configurations.

## Reproduction target
Run spin‑polarized GGA‑PW91 DFT calculations for the four collinear spin configurations of the Fe₅₀Mn₅₀ monolayer on the Co(001) slab as described above. Determine which configuration has the lowest total energy (the ground state). For all four configurations, report:

- the total‑energy difference relative to the ground state, in mRy,
- the magnetic moments of the Fe and Mn atoms, in μB.

Write the results to a CSV file at `/app/outputs/magnetic_results.csv` with columns: `configuration`, `energy_diff_mRy`, `Fe_moment_muB`, `Mn_moment_muB`. The row corresponding to the ground state must have `energy_diff_mRy = 0.0`.

## Assets

- DFT code with GGA-PW91 (e.g., GPAW, Quantum ESPRESSO, VASP): https://www.quantum-espresso.org

## Workflow steps

### Step 1: Magnetic ground state determination and moment computation
- Role: scored
- Action: Build an ordered Fe50Mn50 monolayer on both faces of a seven‑layer Co(001) slab with two inequivalent atoms per plane and five layers of empty spheres. Run spin‑polarized DFT calculations with GGA‑PW91 for four collinear spin configurations: Fe↑Mn↑, Fe↑Mn↓, Fe↓Mn↑, Fe↓Mn↓ (arrows indicate moment parallel or antiparallel to the Co magnetization). Extract total energies and atomic magnetic moments for Fe and Mn. Identify the configuration with the lowest total energy. Compute energy differences (in mRy) relative to that ground state and output the results.
- Output file: `/app/outputs/magnetic_results.csv`
- Format: csv
- Contract: column headers: configuration,energy_diff_mRy,Fe_moment_muB,Mn_moment_muB. Values: configuration is one of Fe↑Mn↑, Fe↑Mn↓, Fe↓Mn↑, Fe↓Mn↓. energy_diff_mRy is a float; Fe_moment_muB and Mn_moment_muB are floats in units of μB. The ground state row must have energy_diff_mRy = 0.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_results.csv
- path: `/app/outputs/magnetic_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total energy differences and atomic magnetic moments for four collinear spin configurations of Fe50Mn50 / Co(001) computed with GGA‑PW91.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `energy_diff_mRy`, `Fe_moment_muB`, `Mn_moment_muB`
  - `units`:
    - `energy_diff_mRy`: mRy
    - `Fe_moment_muB`: μB
    - `Mn_moment_muB`: μB
  - `notes`: configuration must be one of the four labels: Fe↑Mn↑, Fe↑Mn↓, Fe↓Mn↑, Fe↓Mn↓. The ground state row has energy_diff_mRy = 0.0.

Notes: The output values are compared to hidden reference values from the paper’s Table 1 (PW91 results) with appropriate tolerances. Only the PW91 functional is required; LMH is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "energy_diff_mRy",
          "Fe_moment_muB",
          "Mn_moment_muB"
        ],
        "units": {
          "energy_diff_mRy": "mRy",
          "Fe_moment_muB": "μB",
          "Mn_moment_muB": "μB"
        },
        "notes": "configuration must be one of the four labels: Fe↑Mn↑, Fe↑Mn↓, Fe↓Mn↑, Fe↓Mn↓. The ground state row has energy_diff_mRy = 0.0."
      },
      "description": "Total energy differences and atomic magnetic moments for four collinear spin configurations of Fe50Mn50 / Co(001) computed with GGA‑PW91."
    }
  ],
  "notes": "The output values are compared to hidden reference values from the paper’s Table 1 (PW91 results) with appropriate tolerances. Only the PW91 functional is required; LMH is not scored."
}
```

## How you are scored
A hidden verifier evaluates the submitted `magnetic_results.csv` by comparing your reported energy differences and magnetic moments to reference values from the original study, using tolerance windows that accommodate legitimate differences due to the choice of DFT code, implementation details, and numerical settings. The verifier checks that the ground‑state configuration is correctly identified, that the relative ordering of the total energies is correct, and that the magnetic moments lie within the expected ranges. Partial credit is possible: you receive the maximum score only if all configurations are correctly ordered and all values fall within tolerance. The final reward is based solely on this scored artifact; there is no extra credit for auxiliary files.
