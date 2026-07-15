# Band gap and band edge shifts of reduced TiO₂(110) surface from DFT+U calculations

## Problem background
The rutile TiO₂ (110) surface is a prototypical system for photocatalytic water splitting. Surface reduction defects — bridging oxygen vacancies (O-vac), bridging hydroxyl groups (O-H), and titanium interstitials (Ti-int) — donate electrons and modify the surface electronic structure. Understanding how these defects alter the band edges, band gap, and surface dipole is essential for interpreting changes in photocatalytic activity. This task aims to compute the shifts of the valence and conduction band edges, the band gap change, the energy range of defect-induced gap states, and the out-of-plane dipole moment induced by each of these three defects, using first-principles DFT+U calculations.

## Approach
Spin-polarized density functional theory with a Hubbard U correction applied to Ti 3d orbitals (LDA+U) is employed, together with projector-augmented wave pseudopotentials. The rutile TiO₂(110) surface is modeled as a periodically repeated slab with a vacuum gap. Vacuum-level alignment is performed by referencing all eigenenergies to the electrostatic potential in the vacuum region, obtained from the planar-averaged potential. For the stoichiometric surface and each defective surface, the projected density of states (pDOS) on the surface atoms is computed after geometry relaxation and a subsequent static self-consistent calculation. From the pDOS, the valence band maximum and conduction band minimum are identified, enabling the calculation of band-edge shifts and band gap change relative to the pure surface. The energy range of defect states in the band gap is recorded, and the out-of-plane dipole moment is extracted from the relaxed total charge density and ionic positions.

## Reproduction target
Using an open-source DFT implementation (e.g., Quantum ESPRESSO) with LDA+U (U=5.5 eV on Ti 3d), construct the four slab models (stoichiometric, O-vac, O-H, Ti-int) as described in the workflow steps, relax their geometries, perform static calculations with vacuum correction and vacuum-level alignment, and then extract the projected density of states. From these you must derive, for each reduced surface, the defect state energy range, the valence band edge shift ΔE_V, the conduction band edge shift ΔE_C, the band gap change ΔE_g, and the out-of-plane dipole moment p_z. Write all values to `/app/outputs/band_edge_shifts.csv` with the exact columns and row ordering specified in the output contract.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org

## Workflow steps

### Step 1: Build surface slab models
- Role: process
- Action: Construct a (3×2) periodically repeated slab of four trilayers of rutile TiO₂(110) using experimental bulk lattice parameters, with approximately 11 Å vacuum space. Fix atoms in the third and fourth trilayers at bulk positions. After relaxing the stoichiometric surface, create three defective slabs: O‑vac by removing a bridging oxygen, O‑H by adding an H atom atop a bridging oxygen, and Ti‑int by inserting a Ti atom into an interstitial cavity in the first trilayer.
- Evidence: none

### Step 2: Geometry relaxation
- Role: process
- Action: Relax the atomic positions of the stoichiometric and the three defective slabs using spin‑polarized LDA+U (U=5.5 eV on Ti 3d) with Γ‑point sampling, force convergence 0.01 eV/Å, and an energy cutoff of 450 eV. Use PAW pseudopotentials and appropriate dipole corrections.
- Evidence: none

### Step 3: Static DFT+U calculation with dipole corrections
- Role: process
- Action: Perform static self-consistent calculations on the relaxed slabs using a 3×2×1 Monkhorst‑Pack k‑mesh, the same functional, pseudopotentials, and energy cutoff, with monopole/dipole/quadrupole corrections to eliminate spurious slab-slab interactions. Output Kohn–Sham eigenvalues, the electrostatic potential, and the charge density for each surface.
- Evidence: none

### Step 4: Vacuum level alignment and pDOS calculation
- Role: process
- Action: Determine the vacuum energy level from the planar‑averaged electrostatic potential in the vacuum region. Shift all eigenenergies so that the vacuum level is at 0 eV. For each surface, compute the projected density of states (pDOS) onto atoms of the first two trilayers.
- Evidence: none

### Step 5: Extract band edges, shifts, and dipole moment
- Role: scored (load-bearing)
- Action: From the pDOS of the pure surface, determine the valence band edge (VBE) and conduction band edge (CBE). For each reduced surface (O‑H, O‑vac, Ti‑int), similarly determine VBE and CBE, identify the defect state energy range, and compute ΔE_V = VBE(reduced) – VBE(pure), ΔE_C = CBE(reduced) – CBE(pure), ΔE_g = ΔE_C – ΔE_V. Compute the out‑of‑plane dipole moment p_z (Debye) from the total charge density and ionic positions of the reduced slab. Write all quantities for the three defects into `band_edge_shifts.csv`.
- Output file: `/app/outputs/band_edge_shifts.csv`
- Format: csv
- Contract: Columns: defect (string, one of O-H, O-vac, Ti-int), def_state_min (float, eV), def_state_max (float, eV), ΔE_V (float, eV), ΔE_C (float, eV), ΔE_g (float, eV), p_z (float, Debye). Rows ordered as O-H, O-vac, Ti-int.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_edge_shifts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_edge_shifts.csv
- path: `/app/outputs/band_edge_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the band‑edge shifts, band gap change, defect state energy range, and dipole moment for each of the three reduced surfaces (O‑H, O‑vac, Ti‑int).
- schema:
  - `type`: table
  - `required_columns`: `defect`, `def_state_min`, `def_state_max`, `ΔE_V`, `ΔE_C`, `ΔE_g`, `p_z`
  - `units`:
    - `def_state_min`: eV
    - `def_state_max`: eV
    - `ΔE_V`: eV
    - `ΔE_C`: eV
    - `ΔE_g`: eV
    - `p_z`: Debye

Notes: The hydroxyl coverage dependence study and the U‑dependence analysis are omitted from the scored task per the taskability scope; only the three defects at U=5.5 eV are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_edge_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "def_state_min",
          "def_state_max",
          "ΔE_V",
          "ΔE_C",
          "ΔE_g",
          "p_z"
        ],
        "units": {
          "def_state_min": "eV",
          "def_state_max": "eV",
          "ΔE_V": "eV",
          "ΔE_C": "eV",
          "ΔE_g": "eV",
          "p_z": "Debye"
        }
      },
      "description": "Scored artifact containing the band‑edge shifts, band gap change, defect state energy range, and dipole moment for each of the three reduced surfaces (O‑H, O‑vac, Ti‑int)."
    }
  ],
  "notes": "The hydroxyl coverage dependence study and the U‑dependence analysis are omitted from the scored task per the taskability scope; only the three defects at U=5.5 eV are required."
}
```

## How you are scored
A hidden verifier reads your `band_edge_shifts.csv` and compares each row's quantities (defect state energy range, ΔE_V, ΔE_C, ΔE_g, p_z) against reference values. It applies tolerances that account for legitimate differences between DFT implementations while requiring faithful reproduction of the paper's protocol. It also checks that every reported |ΔE_g| remains below a small threshold. The final reward is a weighted combination of how many of the reported quantities fall within the allowed tolerances and whether the structural condition holds; higher weight is assigned to the band-edge shifts and band gap change. Your submission must be generated by executing the full DFT workflow; a hand-crafted CSV will not pass the verifier's checks.
