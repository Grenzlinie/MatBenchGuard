# Self-Consistent LAPW Electronic Structure and Relativistic Corrections for GdX (X=N,P,As,Sb)

## Problem background
Gd‑pnictides (GdN, GdP, GdAs, GdSb) crystallize in the NaCl structure and experimentally show a transition from a semiconductor to a metal as the pnictogen becomes heavier. Understanding how the electronic band structures evolve across this series requires first‑principles calculations that capture the interplay between the Gd 5d and pnictogen p states. Self‑consistent all‑electron density‑functional theory (DFT) can predict the band gap, the density of states at the Fermi level, the topology of the Fermi surface (carrier numbers and effective masses), and the effect of relativistic spin–orbit coupling on the band edges. The computational challenge is to reproduce these properties for two representative compounds — GdN and GdSb — using a modern all‑electron full‑potential code, and to confirm whether DFT indeed yields a semiconducting gap for GdN and a metallic electronic structure for GdSb.

## Approach
All calculations are performed with the open‑source full‑potential linearized augmented‑plane‑wave (FP‑LAPW) code Elk using the local‑density approximation (LDA) for exchange‑correlation. The crystal structures are taken from the experimental lattice constants and muffin‑tin sphere radii listed in the source paper: GdN (NaCl, a=9.4223 Bohr, R(Gd)=R(N)=2.3556 Bohr) and GdSb (a=11.7486 Bohr, R(Gd)=2.7038 Bohr, R(Sb)=3.1705 Bohr). For GdN, a self‑consistent nonrelativistic LAPW run is carried out to obtain the Kohn‑Sham eigenvalues along high‑symmetry directions; the band gap is extracted as the energy difference between the valence band maximum and the conduction band minimum. For GdSb, two separate calculations are performed: (i) a self‑consistent nonrelativistic run to produce the scalar‑relativistic eigenvalues and the total density of states (DOS), and (ii) a fully relativistic run (spin–orbit coupling included) to obtain the spin–orbit‑split eigenvalues at the Γ point and elsewhere. From these results, the DOS at the Fermi level, the Γ‑point spin–orbit splitting (energy difference between the Γ₈⁻ and Γ₆⁻ states), and the numbers of hole carriers at Γ and electron carriers at X per primitive cell are computed. The workflow consists of three steps: (1) run the GdN nonrelativistic calculation, (2) run the GdSb nonrelativistic and relativistic calculations, and (3) assemble the extracted quantities into a single JSON file for scoring.

## Reproduction target
Reproduce the self‑consistent DFT electronic structure calculations for GdN and GdSb using the Elk FP‑LAPW code with LDA. Report the following quantities in `/app/outputs/results.json`:

- `GdN_band_gap_ev`: the fundamental band gap of GdN in eV.
- `GdSb_DOS_at_Ef_states_per_Ryd_cell`: the total density of states at the Fermi level for GdSb in units of states/Ryd per primitive cell.
- `GdSb_spin_orbit_splitting_Ryd`: the spin–orbit splitting at the Γ point for GdSb (energy of Γ₈⁻ minus energy of Γ₆⁻) in Rydberg.
- `GdSb_hole_carriers_per_primitive_cell`: the number of hole carriers at Γ per primitive cell for GdSb.
- `GdSb_electron_carriers_per_primitive_cell`: the number of electron carriers at X per primitive cell for GdSb.

The computed band gap should be positive (semiconducting), and the DOS at the Fermi level should be positive (metallic), consistent with the generic chemical trend across the pnictide series.

## Assets

- Elk all-electron FP-LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Self-consistent nonrelativistic DFT calculation for GdN
- Role: process
- Action: Set up and run a self-consistent nonrelativistic LAPW calculation for GdN using Elk with LDA, NaCl structure, lattice constant a=9.4223 Bohr, APW sphere radii R(Gd)=2.3556 Bohr, R(N)=2.3556 Bohr. Converge the electron density and obtain the Kohn-Sham eigenvalues along high-symmetry paths to identify the valence band maximum and conduction band minimum.
- Evidence: `/app/outputs/gdn_elk.out`

### Step 2: Self-consistent DFT calculations for GdSb (nonrelativistic and fully relativistic)
- Role: process
- Action: For GdSb (a=11.7486 Bohr, R(Gd)=2.7038 Bohr, R(Sb)=3.1705 Bohr), perform two calculations with Elk: (i) self-consistent nonrelativistic LAPW to obtain scalar-relativistic eigenvalues and the density of states; (ii) a fully relativistic calculation (spin–orbit coupling included) to obtain the spin–orbit-split eigenvalues at the Γ point and elsewhere.
- Evidence: `/app/outputs/gdsb_elk_nonrel.out, gdsb_elk_rel.out`

### Step 3: Assemble and output final results
- Role: scored (load-bearing)
- Action: From the outputs of the previous steps, compute and write /app/outputs/results.json containing: the band gap of GdN (eV), the total DOS at the Fermi level for GdSb (states/Ryd.cell), the Γ-point spin–orbit splitting for GdSb (Γ₈⁻ − Γ₆⁻ in Ryd), the number of hole carriers (at Γ) per primitive cell for GdSb, and the number of electron carriers (at X) per primitive cell for GdSb.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"GdN_band_gap_ev": <float>, "GdSb_DOS_at_Ef_states_per_Ryd_cell": <float>, "GdSb_spin_orbit_splitting_Ryd": <float>, "GdSb_hole_carriers_per_primitive_cell": <float>, "GdSb_electron_carriers_per_primitive_cell": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregates the reproduced band gap, density of states at Fermi level, spin–orbit splitting, and carrier numbers. The checker compares these values to the paper-reported hidden gold with generous tolerances.
- schema:
  - `type`: object
  - `required`:
    - `GdN_band_gap_ev`: float
    - `GdSb_DOS_at_Ef_states_per_Ryd_cell`: float
    - `GdSb_spin_orbit_splitting_Ryd`: float
    - `GdSb_hole_carriers_per_primitive_cell`: float
    - `GdSb_electron_carriers_per_primitive_cell`: float
  - `units`:
    - `GdN_band_gap_ev`: eV
    - `GdSb_DOS_at_Ef_states_per_Ryd_cell`: states/Ryd.cell
    - `GdSb_spin_orbit_splitting_Ryd`: Ryd
    - `GdSb_hole_carriers_per_primitive_cell`: carriers per primitive cell
    - `GdSb_electron_carriers_per_primitive_cell`: carriers per primitive cell

Notes: The task uses Elk with LDA; the paper originally used APW with Slater exchange. Tolerances absorb these systematic differences. Only GdN and GdSb are required to demonstrate the semiconducting/metallic trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "GdN_band_gap_ev": "float",
          "GdSb_DOS_at_Ef_states_per_Ryd_cell": "float",
          "GdSb_spin_orbit_splitting_Ryd": "float",
          "GdSb_hole_carriers_per_primitive_cell": "float",
          "GdSb_electron_carriers_per_primitive_cell": "float"
        },
        "units": {
          "GdN_band_gap_ev": "eV",
          "GdSb_DOS_at_Ef_states_per_Ryd_cell": "states/Ryd.cell",
          "GdSb_spin_orbit_splitting_Ryd": "Ryd",
          "GdSb_hole_carriers_per_primitive_cell": "carriers per primitive cell",
          "GdSb_electron_carriers_per_primitive_cell": "carriers per primitive cell"
        }
      },
      "description": "Aggregates the reproduced band gap, density of states at Fermi level, spin–orbit splitting, and carrier numbers. The checker compares these values to the paper-reported hidden gold with generous tolerances."
    }
  ],
  "notes": "The task uses Elk with LDA; the paper originally used APW with Slater exchange. Tolerances absorb these systematic differences. Only GdN and GdSb are required to demonstrate the semiconducting/metallic trend."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/results.json`. Each reported quantity is compared to a hidden reference value derived from the source paper’s self‑consistent APW results. Tolerances are set generously to absorb the systematic differences between the original APW method (Slater exchange) and your Elk LAPW LDA implementation. For directional quantities (the band gap must be >0, the DOS at the Fermi level must be >0), meeting or exceeding the reference behavior earns full credit; for scalar quantities (DOS magnitude, spin–orbit splitting, carrier numbers), falling within a wide tolerance window yields full credit, and larger deviations reduce the score linearly. No credit is awarded for simply reporting numbers without genuine calculation — the verifier expects physically plausible values that are consistent with the underlying band‑structure output. The final reward is the weighted sum of the per‑quantity scores, combined into a single float between 0 and 1.
