# DFT+U Hubbard U Variation Analysis of LaCoO3

## Problem background
LaCoO3 is a perovskite oxide with temperature-dependent spin-state transitions that are critical for catalytic applications. Standard GGA (PBE) fails to open a band gap, predicting a metallic ground state contrary to experiment. Two common corrections are the DFT+U approach (on-site Hubbard U correction) and the HSE06 screened hybrid functional (mixing a fraction of exact exchange). How the choice of the Hubbard U parameter and the mixing factor α influences the low-spin band gap and the relative energies of spin configurations is essential for modeling the room-temperature electronic structure of this material.

## Approach
We use plane-wave DFT with the PBE functional corrected via the Dudarev PBE+U scheme and with the HSE06 hybrid functional. All calculations are performed on the experimental rhombohedral R3c crystal structure at 293 K using a 2 formula unit supercell (4 Co atoms) to allow different spin arrangements. The workflow computes: (1) the low-spin (S=0) band gap for PBE+U at effective Hubbard U = 3.0, 5.0, 7.0 eV; (2) the low-spin band gap for HSE06 at Hartree-Fock mixing factors α = 0.05, 0.15, 0.25; (3) the total electronic energies of the low-spin (LS, S=0), intermediate-spin ferromagnetic (IS_FM, S=1), and LS-HS 1:1 mixture ferromagnetic configurations at U=3.0 eV. The results are then aggregated into a single JSON artifact.

## Reproduction target
Compute and report precise band gap values (eV) for each condition listed above and total electronic energies (eV per supercell) for the three spin configurations at U=3.0 eV, using the given crystal structure and the Quantum ESPRESSO code with SSSP pseudopotentials. The target is to produce the file `dft_results.json` under `/app/outputs` containing an array of objects with fields: `method` ("PBE+U" or "HSE"), `parameter` (float, U in eV or α), `spin_state` (string), `band_gap_eV` (float, or null if not applicable), `total_energy_eV` (float, or null if not applicable).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency
- LaCoO3 experimental crystal structure (R3c, 293 K): 10.1016/0022-4596(86)90029-0

## Workflow steps

### Step 1: Crystal structure setup
- Role: process
- Action: Generate the input file for a LaCoO3 supercell (2 formula units, 4 Co atoms) in the rhombohedral R3c space group with lattice parameters a=b=c=5.3778 Å, α=β=γ=60.798°. Use a 2×1×1 supercell to accommodate different spin configurations.
- Evidence: none

### Step 2: PBE+U low-spin band gaps
- Role: process
- Action: Run PBE+U (Dudarev scheme) self-consistent field calculations for the low-spin (S=0) state at Ueff=3.0, 5.0, and 7.0 eV. For each converged calculation, extract the band gap (difference between valence band maximum and conduction band minimum). Save the three band gaps in a JSON file 'pbeu_ls_bandgaps.json' with structure [{"U": <value>, "band_gap_eV": <value>}].
- Evidence: `/app/outputs/pbeu_ls_bandgaps.json`

### Step 3: HSE low-spin band gaps
- Role: process
- Action: Run HSE06 hybrid functional calculations for the low-spin state at mixing factors α=0.05, 0.15, and 0.25. Extract the band gap for each. Save in 'hse_ls_bandgaps.json' with structure [{"alpha": <value>, "band_gap_eV": <value>}].
- Evidence: `/app/outputs/hse_ls_bandgaps.json`

### Step 4: Spin-state energies at U=3.0 eV
- Role: process
- Action: Run PBE+U (U=3.0 eV) spin-polarized calculations for the low-spin (LS, S=0), intermediate-spin (IS, ferromagnetic, S=1), and LS-HS 1:1 mixing (ferromagnetic) configurations. For each converged state, extract the total electronic energy and divide by 2 to obtain energy per formula unit (eV per formula unit). Save in 'spin_energies_u3.json' with structure [{"spin_state": "LS"/"IS_FM"/"LS-HS_1:1_FM", "total_energy_eV": <value>}].
- Evidence: `/app/outputs/spin_energies_u3.json`

### Step 5: Spin-state energies at U=5.0 and 7.0 eV
- Role: process
- Action: Run PBE+U (U=5.0 and 7.0 eV) spin‑polarized calculations for the low-spin (LS, S=0), intermediate-spin (IS, ferromagnetic, S=1), and high-spin (HS, ferromagnetic, S=2) configurations. For each converged state, extract the total electronic energy and divide by 2 to obtain energy per formula unit (eV per formula unit). Save in `spin_energies_u5_7.json` with structure [{"U": <value>, "spin_state": "LS"/"IS_FM"/"HS_FM", "total_energy_eV": <value>}].
- Evidence: `/app/outputs/spin_energies_u5_7.json`

### Step 6: HSE spin-state energies (LS and IS)
- Role: process
- Action: Run HSE06 spin‑polarized calculations for the low-spin (LS, S=0) and intermediate-spin (IS, ferromagnetic, S=1) states at mixing factors α=0.05, 0.15, and 0.25. Extract total electronic energy and divide by 2 to obtain energy per formula unit (eV per formula unit) for each combination. Save in `hse_spin_energies.json` with structure [{"alpha": <value>, "spin_state": "LS"/"IS_FM", "total_energy_eV": <value>}].
- Evidence: `/app/outputs/hse_spin_energies.json`

### Step 7: Aggregate results into scored artifact
- Role: scored (load-bearing)
- Action: Collect the results from steps s02, s03, s04, s05, s06. For each entry create an object with fields: method (string, “PBE+U” or “HSE”), parameter (float, U or α), spin_state (string, e.g. “LS”, “IS_FM”, “LS-HS_1:1_FM”, “HS_FM”), band_gap_eV (float, or null if not applicable), total_energy_eV (float, or null if not applicable). All total energies must be reported per formula unit (divide supercell total energy by 2) as total_energy_eV. Write all objects into a single JSON list file `dft_results.json` under /app/outputs.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: Array of objects, each containing: method (string, e.g. 'PBE+U' or 'HSE'), parameter (float, U or α), spin_state (string, e.g. 'LS'/'IS_FM'/'LS-HS_1:1_FM'/'HS_FM'), band_gap_eV (float|null), total_energy_eV (float|null). Total energies are per formula unit.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled band gaps (eV) and total electronic energies (eV) for LaCoO3 low-spin and spin-excited states computed with PBE+U (U=3.0,5.0,7.0 eV) and HSE (α=0.05,0.15,0.25). The checker compares each quantity to hidden paper-reported reference values using specified tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required_fields`: `method`, `parameter`, `spin_state`, `band_gap_eV`, `total_energy_eV`

Notes: The intermediate evidence files (pbeu_ls_bandgaps.json, hse_ls_bandgaps.json, spin_energies_u3.json) are produced by the process steps but are not part of the scored contract. The solver must run the actual DFT calculations to obtain all entries in dft_results.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required_fields": [
            "method",
            "parameter",
            "spin_state",
            "band_gap_eV",
            "total_energy_eV"
          ]
        }
      },
      "description": "Compiled band gaps (eV) and total electronic energies (eV) for LaCoO3 low-spin and spin-excited states computed with PBE+U (U=3.0,5.0,7.0 eV) and HSE (α=0.05,0.15,0.25). The checker compares each quantity to hidden paper-reported reference values using specified tolerances."
    }
  ],
  "notes": "The intermediate evidence files (pbeu_ls_bandgaps.json, hse_ls_bandgaps.json, spin_energies_u3.json) are produced by the process steps but are not part of the scored contract. The solver must run the actual DFT calculations to obtain all entries in dft_results.json."
}
```

## How you are scored
A hidden verifier reads your `dft_results.json`. For each entry, it compares your reported band gap and total energy to hidden reference values using pre‑specified tolerances. It also checks for expected physical relationships: the band gap should vary systematically with the Hubbard U and mixing parameter α, and the relative energies of the spin configurations at U=3.0 eV should follow a physically plausible pattern. The verifier combines these checks into a final score in [0,1]. Merely including the file without having performed the actual DFT calculations will not satisfy the structural checks.
