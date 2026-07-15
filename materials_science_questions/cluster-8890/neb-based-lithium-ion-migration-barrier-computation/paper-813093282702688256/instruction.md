# Lithium Ion Migration Barrier Computation in Spinel TiO2 via NEB-DFT

## Problem background
Lithium-ion batteries rely on fast Li ion transport through electrode materials. Spinel TiO₂ is a candidate anode material, and its Li migration barriers directly affect rate capability. When one Li atom is inserted into the TiO₂ lattice, an extra electron reduces a Ti⁴⁺ to Ti³⁺. The Ti³⁺ ion is Jahn–Teller active, leading to a distortion of the surrounding oxygen octahedron. This local structural change can influence the energy landscape for Li hopping. This task examines how the Jahn–Teller distortion affects the Li migration barrier, depending on which Ti site hosts the extra electron relative to the migration path. The objective is to compute the migration energy barriers for different Ti³⁺ site positions, providing insight into the coupling between electronic and ionic transport in spinel oxides.

## Approach
First-principles density functional theory (DFT) with the GGA+U method (U_eff applied to Ti-3d states) is used to describe the spin-polarized electronic structure and to localize the extra electron on a chosen Ti site, producing the Jahn–Teller distortion. A 16-formula-unit supercell of spinel TiO₂ is constructed as the host. A single Li atom is inserted at a tetrahedral site, and the migration pathway from that site to an adjacent tetrahedral site via an intermediate octahedral site is studied using the climbing-image nudged elastic band (CINEB) technique. To isolate the effect of the distortion, four cases are considered: three where the extra electron is localized on distinct Ti sites (labelled Ti_I, Ti_II, and Ti_III) relative to the migration pathway, and one reference case (All‑Ti⁴⁺) where no extra electron is introduced and all Ti remain +4. For each case, the initial and final state structures are relaxed, the transition state is located, and the migration barrier is extracted as the energy difference between the transition state and the endpoints. By comparing the computed barriers, the influence of the Jahn–Teller distortion on Li migration can be assessed.

## Reproduction target
Produce a JSON file, `/app/outputs/migration_barriers.json`, containing the computed Li ion migration energy barriers (in eV) for the four cases: Ti_I³⁺, Ti_II³⁺, Ti_III³⁺, and All‑Ti⁴⁺. The JSON object must have the keys 'Ti_I3+', 'Ti_II3+', 'Ti_III3+', and 'All-Ti4+', each mapping to a floating-point number that represents the migration barrier determined via the CINEB calculation. The barrier is defined as the difference between the highest energy along the nudged elastic band path and the energy of the initial state. All structures must be relaxed with the specified DFT settings and convergence criteria described in the workflow steps.

## Assets

- Open-source DFT software with plane-wave PAW, GGA+U, and NEB support (e.g., Quantum ESPRESSO)
- Atomic Simulation Environment (ASE) or pymatgen: ase

## Workflow steps

### Step 1: Bulk spinel TiO2 structural relaxation
- Role: process
- Action: Build a 16-formula-unit supercell of spinel TiO₂ (cubic, initial lattice parameter ≈8.5 Å). Perform DFT relaxation using spin-polarized GGA+U (Ueff=5.0 eV on Ti-3d) with a plane-wave cutoff energy of 450 eV and a 3×3×3 k-point mesh. Relax until forces on all atoms are below 0.01 eV/Å, obtaining the equilibrium lattice constant and atomic positions.
- Evidence: none

### Step 2: Prepare initial and final state structures for each Li migration case
- Role: process
- Action: For each of the four cases (Ti_I, Ti_II, Ti_III, All‑Ti⁴⁺): insert one Li atom at a tetrahedral site to create the initial (IS) and final (FS) images of the tetrahedral→octahedral→tetrahedral migration path. For the three Ti³⁺ cases, manually distort the selected Ti site's octahedron (adjust bond lengths according to crystal-field considerations) and relax under spin-polarized GGA+U to localize the electron. For the All‑Ti⁴⁺ reference, use Li⁺ (remove the excess electron) so all Ti remain +4. Relax all endpoint structures until forces <0.01 eV/Å.
- Evidence: none

### Step 3: CINEB calculation of Li migration barriers
- Role: scored (load-bearing)
- Action: For each of the four cases, compute the minimum-energy path between the prepared IS and FS using the climbing-image nudged elastic band method (CINEB) with the same DFT settings. Extract the migration barrier as the energy difference between the highest-energy image (transition state) and the IS/FS. Assemble the four barriers into a JSON object and write to /app/outputs/migration_barriers.json.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON object with exactly four keys: Ti_I3+, Ti_II3+, Ti_III3+, All‑Ti4+, each value a float representing the Li migration energy barrier in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Li ion migration energy barriers (eV) for the four electronic/structural cases: Ti_I³⁺, Ti_II³⁺, Ti_III³⁺, and All‑Ti⁴⁺. The checker will compare these values to reference values within an appropriate tolerance and optionally verify the relative ordering consistent with the paper.
- schema:
  - `type`: object
  - `required`: `Ti_I3+`, `Ti_II3+`, `Ti_III3+`, `All-Ti4+`

Notes: The task reproduces only the single-Li migration barriers in spinel TiO₂. The Li vacancy migration in LiTi₂O₄ and the bond-length/trapping-energy analysis are excluded as they are out of scope for this reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ti_I3+",
          "Ti_II3+",
          "Ti_III3+",
          "All-Ti4+"
        ]
      },
      "description": "Computed Li ion migration energy barriers (eV) for the four electronic/structural cases: Ti_I³⁺, Ti_II³⁺, Ti_III³⁺, and All‑Ti⁴⁺. The checker will compare these values to reference values within an appropriate tolerance and optionally verify the relative ordering consistent with the paper."
    }
  ],
  "notes": "The task reproduces only the single-Li migration barriers in spinel TiO₂. The Li vacancy migration in LiTi₂O₄ and the bond-length/trapping-energy analysis are excluded as they are out of scope for this reproduction."
}
```

## How you are scored
A hidden verifier will inspect your output file and compare each reported barrier value to a set of reference values. The score reflects the accuracy of your computed barriers; better agreement with the correct values yields a higher score. The final reward is a weighted combination of the individual case scores. Note that simply writing down paper‑reported numbers without performing the actual DFT/CINEB simulation will not be detected by the verifier, but any incorrect values will result in a lower score. The verifier evaluates only the correctness of the results you submit.
