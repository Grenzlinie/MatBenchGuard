# DFT+U Hubbard U Variation: Surface-Relaxation-Induced Insulator on Bilayer Ruthenate

## Problem background
Ca3Ru2O7 is a bilayer ruthenate that hosts a polar metallic ground state. Previous studies have shown that subtle structural distortions, such as rotations and tilts of RuO6 octahedra, can strongly influence the electronic properties and drive the system towards an insulating state. At a crystal surface, atoms relax from their bulk positions, altering the local octahedral environment. This work investigates whether such surface structural relaxations can modify the electronic correlations enough to produce a distinct surface phase, changing the metal–insulator balance compared to the bulk.

## Approach
We use density-functional theory with an on-site Hubbard U correction (DFT+U) to model two free-standing bilayer slabs of Ca3Ru2O7: a bulk-like bilayer with the experimental bulk atomic positions, and a surface-relaxed bilayer where the atoms are displaced according to experimentally determined surface relaxation parameters. Both models include spin-orbit coupling and an antiferromagnetic spin arrangement with spins along the b-axis (AFM_b). By varying the effective Hubbard U applied to Ru 4d states and calculating the resulting band gap at the Fermi level, we determine whether the bulk-like and surface-relaxed bilayers undergo a metal–insulator transition, and at which U values this occurs.

## Reproduction target
Construct the two bilayer structural models (bulk-like and surface-relaxed) using the provided surface displacements. Run self-consistent DFT+U calculations (LDA functional, SOC, AFM_b order) for each geometry at four Hubbard U values: 0.0, 2.5, 2.625, and 2.75 eV. From the computed total density of states, extract the band gap at the Fermi level and determine whether the system is insulating (gap > 0) or metallic (no gap). Compile all results into `/app/outputs/step_01_band_gaps.json`, containing an array of objects with fields `geometry` ("bulk-like" or "surface-relaxed"), `U_eV`, `band_gap_eV`, and `is_insulator`.

## Assets

- Bulk crystal structure of Ca3Ru2O7 (Yoshida et al., Phys. Rev. B 72, 054412, 2005): https://doi.org/10.1103/PhysRevB.72.054412
- Quantum ESPRESSO (or any open-source DFT code supporting LDA+U, SOC, noncollinear magnetism): https://www.quantum-espresso.org/
- LDA pseudopotentials for Ca, Ru, O (e.g., SSSP LDA library): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Construct bilayer structural models
- Role: process
- Action: Obtain the bulk crystal structure of Ca3Ru2O7 from Yoshida et al. (2005). Using the surface atomic displacements from quantitative LEED analysis — octahedral rotation angle θ_surface = 13° (increased from bulk ~10.9°), tilt angle φ_surface = 13°, and out-of-plane vertical shifts Δc: Ca_A = −12.5 pm, O_A = −5.7 pm, Ru = −2.5 pm, Ca_B = −3.3 pm, O_C = −6.4 pm — create two free-standing bilayer models: a bulk-like bilayer (using bulk atomic positions) and a surface-relaxed bilayer (with the displacements applied). Include a vacuum gap of about 15 Å between periodic images. Set up the initial magnetic order as AFM_b (spins along the b-axis). Output the two structural models (e.g., in CIF or POSCAR format) as evidence that the geometry preparation was performed.
- Evidence: `/app/outputs/bilayer_structures.zip`

### Step 2: Run DFT+U sweeps and extract band gaps
- Role: scored (load-bearing)
- Action: For each of the two bilayer geometries (bulk-like and surface-relaxed) and each Hubbard U value in {0.0, 2.5, 2.625, 2.75} eV, perform a self-consistent DFT+U calculation using the LDA functional, spin-orbit coupling, and AFM_b magnetic order. Apply the U parameter to Ru 4d states within the Dudarev approximation. Use a suitable k-point grid and plane-wave energy cutoff to converge the band gap. After convergence, compute the total density of states (DOS) and determine the band gap at the Fermi level. If a gap exists (e.g., DOS at Ef below 0.01 eV), set band_gap_eV > 0 and is_insulator=true; otherwise set band_gap_eV ≈ 0 and is_insulator=false. Write all results into /app/outputs/step_01_band_gaps.json as an object with a 'calculations' array containing objects with keys geometry, U_eV, band_gap_eV, is_insulator.
- Output file: `/app/outputs/step_01_band_gaps.json`
- Format: json
- Contract: {"calculations": [{"geometry": "bulk-like"|"surface-relaxed", "U_eV": number, "band_gap_eV": number, "is_insulator": boolean}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gaps.json
- path: `/app/outputs/step_01_band_gaps.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Band gap results for each bilayer geometry and Hubbard U value. The checker verifies that the surface bilayer is insulating (gap > 0.05 eV) at U=2.625 eV while the bulk-like bilayer remains metallic, and that the critical U for the surface is lower than for the bulk.
- schema:
  - `type`: object
  - `required`:
    - `calculations`: array of objects
  - `items`:
    - `geometry`: string (one of 'bulk-like' or 'surface-relaxed')
    - `U_eV`: number
    - `band_gap_eV`: number
    - `is_insulator`: boolean

Notes: All values are computed from first-principles DFT+U. No experimental data is used except the bulk crystal structure and the surface displacement parameters which are provided in the task instructions. The hidden checker uses threshold-or-better scoring: meeting or exceeding the required gap / metallic condition earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "calculations": "array of objects"
        },
        "items": {
          "geometry": "string (one of 'bulk-like' or 'surface-relaxed')",
          "U_eV": "number",
          "band_gap_eV": "number",
          "is_insulator": "boolean"
        }
      },
      "description": "Band gap results for each bilayer geometry and Hubbard U value. The checker verifies that the surface bilayer is insulating (gap > 0.05 eV) at U=2.625 eV while the bulk-like bilayer remains metallic, and that the critical U for the surface is lower than for the bulk."
    }
  ],
  "notes": "All values are computed from first-principles DFT+U. No experimental data is used except the bulk crystal structure and the surface displacement parameters which are provided in the task instructions. The hidden checker uses threshold-or-better scoring: meeting or exceeding the required gap / metallic condition earns full credit."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/step_01_band_gaps.json` and independently check whether your computed band gaps correctly reflect the insulating vs metallic character of each bilayer at the specified U values. The verifier compares your reported band gaps against scientifically motivated thresholds and relative trends derived from the reference study. It does not require exact numerical agreement with any particular published value, but it does expect that the opening of a gap (or its absence) for each geometry–U combination matches the expected physical behaviour. Meeting or exceeding the required gap conditions earns full credit for that check; the checks are weighted according to their importance for the overall reproduction.
