# Surface electronic structure and magnetism of NiAs MnAs(0001) and MnSb(0001) from FLAPW-DFT

## Problem background
Transition-metal pnictides like MnAs and MnSb in the NiAs structure are candidate materials for spintronics applications. The (0001) surface can exhibit altered magnetic moments and electronic hybridization compared to the bulk, which is critical for device integration. This task aims to reproduce the surface electronic structure and magnetism of MnAs(0001) and MnSb(0001) by first-principles density functional theory (DFT) using the full-potential linearized augmented plane wave (FLAPW) method within the generalized gradient approximation (GGA).

## Approach
Two slab terminations are considered for each material: Mn-terminated (17 atomic layers) and anion-terminated (15 layers) surfaces built from the NiAs structure using bulk lattice constants and an interlayer spacing of c/4, without surface relaxation or reconstruction. Self-consistent all-electron FLAPW-GGA (PBE) calculations are performed for all four slab systems to obtain the ground-state charge/spin density. From the converged density, layer-resolved magnetic moments are extracted inside muffin-tin spheres, and the spin-polarized layer-projected density of states (LDOS) is computed for the centre Mn atom in the Mn-terminated slabs. The key physical indicator is the energy separation between the two main majority-spin Mn‑d peaks in the LDOS, which reflects the strength of Mn‑d – anion‑p hybridization; a larger separation indicates stronger hybridization. By comparing MnAs and MnSb, the task quantifies how the different anion (As vs Sb) affects surface magnetic moments and electronic structure.

## Reproduction target
Produce two CSV files:
- magnetic_moments.csv: For each of the four slab systems (Mn-terminated MnAs, As-terminated MnAs, Mn-terminated MnSb, Sb-terminated MnSb), report the magnetic moment (in μB) for every atomic layer, with columns: system, layer_label (e.g., Mn(S), Mn(S-2),…), magnetic_moment_muB.
- center_ldos.csv: For the centre Mn atom (Mn(C)) in the Mn-terminated MnAs and MnSb slabs, report the total spin-polarized DOS (states/eV) on a fine energy grid covering -6 to +4 eV relative to the Fermi level (set at 0 eV), with spacing ≤ 0.01 eV. Columns: system, energy_eV, spin (majority or minority), dos_total.

## Assets

- FLEUR (Full-potential Linearized Augmented Plane Wave code): https://www.flapw.de
- Elk (all-electron full-potential LAPW code, alternative to FLEUR): https://github.com/elk-model/elk

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Build slab supercells for MnAs(0001) and MnSb(0001) with Mn-terminated (17 layers) and anion-terminated (15 layers) surfaces using the provided bulk lattice constants and interlayer spacing c/4. Do not apply surface relaxation or reconstruction.
- Evidence: none

### Step 2: Perform FLAPW DFT self-consistent calculations
- Role: process
- Action: Run self-consistent all-electron FLAPW-GGA (PBE) calculations for all four slab systems. Use muffin-tin radii 2.40 a.u. (Mn, Sb) and 2.00 a.u. (As); plane-wave cutoff 13.0 Ry; star-function cutoff 110 Ry; k-point mesh equivalent to 66 irreducible k-points in the 2D BZ; self-consistency threshold 1.0e-4 e/a.u.^3. Obtain converged charge/spin density and Kohn-Sham eigenvalues.
- Evidence: none

### Step 3: Extract layer magnetic moments
- Role: scored
- Action: From the self-consistent spin density, compute the magnetic moment inside each muffin-tin sphere for every atomic layer in all four slab systems. Save the results as magnetic_moments.csv.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: Columns: system (string, one of MnAs_MnTerm, MnAs_AsTerm, MnSb_MnTerm, MnSb_SbTerm), layer_label (string, e.g., Mn(S), Mn(S-2),..., X(S) etc.), magnetic_moment_muB (float). One row per atom layer per system.
- Scoring: scored by hidden verifier

### Step 4: Compute center-layer Mn LDOS
- Role: scored (load-bearing)
- Action: Compute the spin-polarized layer-projected density of states for the center Mn atom (Mn(C)) in the Mn-terminated MnAs and MnSb slabs. Output the total DOS for majority and minority spins on a fine energy grid. Save as center_ldos.csv.
- Output file: `/app/outputs/center_ldos.csv`
- Format: csv
- Contract: Columns: system (one of MnAs_MnTerm, MnSb_MnTerm), energy_eV (float, relative to Fermi level), spin (string: majority or minority), dos_total (float, total DOS in states/eV). Energy range from -6 eV to +4 eV with spacing ≤0.01 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`
- `/app/outputs/center_ldos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored against the paper's published layer magnetic moment values (Table I) with a hidden absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `system`, `layer_label`, `magnetic_moment_muB`
  - `description`: Layer-resolved magnetic moments in μ_B for the four slab systems (Mn-Term MnAs, As-Term MnAs, Mn-Term MnSb, Sb-Term MnSb).

### center_ldos.csv
- path: `/app/outputs/center_ldos.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Scored on the relative ordering of the two main majority-spin Mn-d peak separations: the energy separation for MnAs must be larger than that for MnSb by at least a hidden threshold, consistent with stronger Mn-d – As-p hybridization.
- schema:
  - `type`: table
  - `required_columns`: `system`, `energy_eV`, `spin`, `dos_total`
  - `description`: Spin-polarized layer-projected DOS for the center Mn atom in Mn-terminated MnAs and MnSb slabs.

Notes: The hidden checker verifies magnetic moments against the paper's Table I reference values within a tolerance. For the LDOS, it locates the two main majority-spin Mn-d peaks, computes their energy separation, and confirms that the separation is larger for MnAs than for MnSb by at least a hidden minimum gap. This workflow covers the paper's main experimental results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "layer_label",
          "magnetic_moment_muB"
        ],
        "description": "Layer-resolved magnetic moments in μ_B for the four slab systems (Mn-Term MnAs, As-Term MnAs, Mn-Term MnSb, Sb-Term MnSb)."
      },
      "description": "Scored against the paper's published layer magnetic moment values (Table I) with a hidden absolute tolerance."
    },
    {
      "file": "center_ldos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "energy_eV",
          "spin",
          "dos_total"
        ],
        "description": "Spin-polarized layer-projected DOS for the center Mn atom in Mn-terminated MnAs and MnSb slabs."
      },
      "description": "Scored on the relative ordering of the two main majority-spin Mn-d peak separations: the energy separation for MnAs must be larger than that for MnSb by at least a hidden threshold, consistent with stronger Mn-d – As-p hybridization."
    }
  ],
  "notes": "The hidden checker verifies magnetic moments against the paper's Table I reference values within a tolerance. For the LDOS, it locates the two main majority-spin Mn-d peaks, computes their energy separation, and confirms that the separation is larger for MnAs than for MnSb by at least a hidden minimum gap. This workflow covers the paper's main experimental results."
}
```

## How you are scored
Your outputs are evaluated by a hidden verifier that uses independent reference data and physical criteria. For magnetic_moments.csv, it compares your reported magnetic moments to expected values within a hidden tolerance; full credit for values within tolerance, partial credit otherwise. For center_ldos.csv, the verifier locates the two dominant majority-spin Mn-d peaks, calculates their energy separation, and checks that the separation for MnAs is greater than for MnSb by at least a hidden threshold, confirming the expected hybridization trend. It also verifies that surface Mn moments are enhanced relative to the centre layer (surface moment − centre moment > a hidden minimum). The final score (0–1) is a weighted sum of these checks. Merely reporting the paper’s numbers without correct physical data will not pass.
