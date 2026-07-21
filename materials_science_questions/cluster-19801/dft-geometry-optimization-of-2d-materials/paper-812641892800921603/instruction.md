# Equilibrium geometry and relative stability of Bi-covered GaAs(111) surface

## Problem background
The adsorption of group-V elements on III-V semiconductor surfaces leads to a variety of surface reconstructions with different atomic geometries and electronic properties. On the GaAs(111)B surface, prior studies showed that As and Sb adsorbates form trimers and produce distinct surface phases. The Bi-covered GaAs(111)B surface has been observed experimentally to exhibit both (2×2) and c(4×2) reconstructions, but no first-principles study had determined the equilibrium atomic structure and the relative stability of these models. This task reproduces the key ab initio findings for this system: the relaxed atomic parameters of the Bi trimers and their bonding environment, and the energetic preference among competing trimer adsorption sites and reconstruction periodicities.

## Approach
We use density-functional theory (DFT) within the local-density approximation (LDA) and the plane-wave pseudopotential method. The surface is modeled as a repeated slab with six atomic layers, a vacuum gap, and a dipole correction; the bottom Ga dangling bonds are saturated with pseudohydrogen. Four structural models are built: c(4×2) and (2×2) unit cells, each with Bi trimers adsorbed in either T4 or H3 sites. Full geometry relaxation is carried out for all four configurations. From the relaxed c(4×2) T4 model we extract five geometric quantities that characterize the bonding: the Bi–Bi bond length inside a trimer, the Bi–As bond length, the vertical separation between Bi and As along [111], the upward relaxation of the exposed second-layer As rest atoms, and the compression of the Ga–As bond beneath a trimer. Total energies of the relaxed configurations are used to evaluate two energy comparisons: (i) the adsorption site preference (T4 vs H3) per trimer using the c(4×2) cells, and (ii) the reconstruction stability (c(4×2) vs (2×2)) per trimer for the T4 site.

## Reproduction target
Build the slab models, run DFT relaxations with the specified setup, and produce two JSON output files:

- `relaxed_geometry.json`: contains the five structural parameters of the relaxed c(4×2) surface (T4 site): `d_BiBi`, `d_BiAs`, `dz_BiAs`, `dz_As_rest`, and `delta_GaAs` (all in Å).
- `energy_differences.json`: contains `T4_vs_H3_diff_eV_per_trimer` and `c4x2_vs_2x2_diff_eV_per_trimer` (both in eV per trimer).

The target is to obtain these quantities from an independent DFT implementation; the exact values constitute the hidden gold.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Bi, As, Ga, H: http://www.pseudo-dojo.org/
- GaAs bulk lattice constant (5.62 Å theoretical LDA value)

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Build the atomic structures for all four surface configurations: c(4×2) with Bi trimers in T4 sites, (2×2) with Bi trimers in T4 sites, c(4×2) with H3 sites, and (2×2) with H3 sites. Use the theoretical bulk GaAs lattice constant of 5.62 Å. Create a repeated slab with six atomic layers and a vacuum region equivalent to twice the bulk lattice constant. Saturate the bottom surface Ga dangling bonds with pseudohydrogen and apply a dipole correction. Output initial unrelaxed coordinates.
- Evidence: `/app/outputs/constructed_structures.json`

### Step 2: Run DFT geometry relaxation
- Role: process
- Action: Perform full DFT/LDA geometry optimization for all four models using norm-conserving pseudopotentials, a plane-wave kinetic energy cutoff of 12 Ry (or higher), 4 special k-points in the irreducible surface Brillouin zone, dipole correction, and relax the top four atomic layers until forces are smaller than 25 meV/Å. Save the relaxed atomic coordinates and total energies.
- Evidence: `/app/outputs/dft_relaxation_summary.json`

### Step 3: Extract structural parameters of the c(4×2) model
- Role: scored (load-bearing)
- Action: From the relaxed atomic coordinates of the c(4×2) model (T4 site), compute the following five geometric quantities: Bi-Bi bond length within a trimer, Bi-As bond length (top-layer Bi to second-layer As), vertical separation along [111] between Bi and As, upward displacement of the As rest atom relative to its original layer position, and the compression of the Ga-As bond beneath Bi trimers relative to the bulk GaAs bond length.
- Output file: `/app/outputs/relaxed_geometry.json`
- Format: json
- Contract: {"d_BiBi": float (Å), "d_BiAs": float (Å), "dz_BiAs": float (Å), "dz_As_rest": float (Å), "delta_GaAs": float (Å)}
- Scoring: scored by hidden verifier

### Step 4: Compute energy differences between surface models
- Role: scored
- Action: Using the total energies obtained from the relaxed configurations, compute (a) the energy preference of T4 over H3 adsorption site (T4 minus H3, in eV per trimer) using the c(4×2) geometries, and (b) the energy difference between the c(4×2) and (2×2) reconstructions (both in T4 sites) for the same supercell size, in eV per trimer.
- Output file: `/app/outputs/energy_differences.json`
- Format: json
- Contract: {"T4_vs_H3_diff_eV_per_trimer": float, "c4x2_vs_2x2_diff_eV_per_trimer": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_geometry.json`
- `/app/outputs/energy_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_geometry.json
- path: `/app/outputs/relaxed_geometry.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Five structural parameters of the relaxed c(4×2) surface: Bi-Bi bond length, Bi-As bond length, vertical Bi-As separation, As rest atom upward displacement, and Ga-As bond compression beneath Bi trimers.
- schema:
  - `type`: object
  - `required`:
    - `d_BiBi`: float (Å)
    - `d_BiAs`: float (Å)
    - `dz_BiAs`: float (Å)
    - `dz_As_rest`: float (Å)
    - `delta_GaAs`: float (Å)

### energy_differences.json
- path: `/app/outputs/energy_differences.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Two energy differences: (a) T4 vs H3 adsorption site preference per trimer, and (b) c(4×2) vs (2×2) reconstruction stability per trimer.
- schema:
  - `type`: object
  - `required`:
    - `T4_vs_H3_diff_eV_per_trimer`: float (eV)
    - `c4x2_vs_2x2_diff_eV_per_trimer`: float (eV)

Notes: Removed the extraneous band_gap_eV field to align with the hidden checker that does not score it.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "d_BiBi": "float (Å)",
          "d_BiAs": "float (Å)",
          "dz_BiAs": "float (Å)",
          "dz_As_rest": "float (Å)",
          "delta_GaAs": "float (Å)"
        }
      },
      "description": "Five structural parameters of the relaxed c(4×2) surface: Bi-Bi bond length, Bi-As bond length, vertical Bi-As separation, As rest atom upward displacement, and Ga-As bond compression beneath Bi trimers."
    },
    {
      "file": "energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T4_vs_H3_diff_eV_per_trimer": "float (eV)",
          "c4x2_vs_2x2_diff_eV_per_trimer": "float (eV)"
        }
      },
      "description": "Two energy differences: (a) T4 vs H3 adsorption site preference per trimer, and (b) c(4×2) vs (2×2) reconstruction stability per trimer."
    }
  ],
  "notes": "Removed the extraneous band_gap_eV field to align with the hidden checker that does not score it."
}
```

## How you are scored
Your submission is evaluated by an automated checker. It reads your two output JSON files and compares each numeric field to the corresponding reference value (the paper's reported result). The reward is the fraction of structural values that fall within a hidden tolerance, weighted 0.5, plus the fraction of energy values that fall within a hidden tolerance, weighted 0.5. The total reward ranges from 0 to 1. The checker enforces strict format compliance; missing keys or non-numeric values will be treated as zero credit for that field.
