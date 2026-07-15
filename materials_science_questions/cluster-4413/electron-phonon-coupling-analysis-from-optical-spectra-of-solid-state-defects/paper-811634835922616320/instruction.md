# Crystal-field parameter calculation for CuB2O4 and scaling to related cuprates

## Problem background
CuB₂O₄ is a tetragonal copper metaborate where Cu²⁺ ions occupy two distinct crystallographic sites (4b and 8d). High-resolution optical absorption reveals six sharp zero-phonon (ZP) lines attributed to pure electronic d–d transitions. A symmetry analysis in the D₄ₕ point group assigns each ZP line to a specific transition from the ground state (x²−y²) to excited states (xy, xz,yz, and 3r²−z²) for both sites. From these assignments, the genuine crystal-field parameters Dq, Ds, Dt (the cubic and tetragonal splittings) can be determined. Because these parameters depend primarily on Cu–O bond lengths, they can serve as a reference to estimate crystal-field splittings in other cuprates with known bond lengths using a point-charge scaling model.

## Approach
We treat the Cu²⁺ ions within D₄ₕ symmetry. The energies of the four d‑hole states (x²−y², xy, xz/yz, 3r²−z²) are expressed as linear combinations of Dq, Ds, Dt via known matrix elements. For each site (4b and 8d), the three measured excitation energies provide a 3×3 linear system that directly yields Dq, Ds, Dt. The ground state is always the x²−y² orbital, and the excited-state ordering follows from the matrix elements. 

Once the reference parameters for CuB₂O₄ are obtained, they are scaled to other cuprates (La₂CuO₄, Nd₂CuO₄, CuGeO₃, Sr₂CuO₂Cl₂, Cu₃B₇O₁₃Cl) using the point‑charge model. In this model the scaling relations are:

  Dq_target = Dq_ref * (d_e,ref / d_e,target)^5

  Ds_target = Ds_ref * (Z_target / Z_ref) * ( (1/d_e,target^3 - 1/d_a,target^3) / (1/d_e,ref^3 - 1/d_a,ref^3) )

  Dt_target = Dt_ref * (Z_target / Z_ref) * ( (1/d_e,target^5 - 1/d_a,target^5) / (1/d_e,ref^5 - 1/d_a,ref^5) )

where:
- d_e,ref and d_a,ref are the equatorial and apical bond lengths of the appropriate CuB2O4 reference site (4b for planar-square compounds, 8d for octahedral compounds).
- Dq_ref, Ds_ref, Dt_ref are the crystal‑field parameters of that reference site from step_01.
- Z_ref is the apical ligand charge of the reference site (Z_ref = -2 for O²⁻).
- Z_target is the apical ligand charge for the target compound: Z_target = -2 for O²⁻, Z_target = -1 for Cl⁻.
- For planar‑square reference or target with d_a = ∞, the terms 1/d_a^3 and 1/d_a^5 are taken as 0.

## Reproduction target
Compute the genuine crystal‑field parameters Dq, Ds, Dt for the 4b and 8d Cu²⁺ sites in CuB₂O₄ from the six provided zero‑phonon line energies (in eV) and their polarization‑based site/state assignments. Then, using these CuB₂O₄ parameters as reference and the supplied Cu–O bond lengths (equatorial dₑ and apical dₐ) for La₂CuO₄, Nd₂CuO₄, CuGeO₃, Sr₂CuO₂Cl₂, and Cu₃B₇O₁₃Cl, estimate Dq, Ds, Dt for each compound via the point‑charge scaling relations. Write the results to the two specified JSON output files.

## Assets

- NumPy: numpy

### Provided data

**Zero-phonon line energies and assignments**

Six ZP lines from the absorption spectra, with their energies, Cu site assignment, and the corresponding excited state:

| Energy (eV) | Site | Excited state       |
|-------------|------|---------------------|
| 1.4027      | 4b   | Γ₄⁺ (xy)           |
| 1.5767      | 8d   | Γ₄⁺ (xy)           |
| 1.6667      | 4b   | Γ₅⁺ (xz,yz)        |
| 1.8727      | 8d   | Γ₅⁺ (xz,yz)        |
| 1.9133      | 4b   | Γ₁⁺ (3r²−z²)      |
| 2.1198      | 8d   | Γ₁⁺ (3r²−z²)      |

**Matrix elements (D₄ₕ crystal-field energies for a single d hole)**

The ground state is Γ₃⁺ (x²−y²). The ZP line energies correspond to the difference between the energy of the excited state and the ground state.

| State              | Energy expression   |
|--------------------|---------------------|
| Γ₃⁺ (x²−y²)        | 6Dq + 2Ds − Dt      |
| Γ₄⁺ (xy)           | −4Dq + 2Ds − Dt     |
| Γ₅⁺ (xz, yz)       | −4Dq − Ds + 4Dt     |
| Γ₁⁺ (3r²−z²)      | 6Dq − 2Ds − 6Dt     |

**Bond lengths for other cuprates**

Equatorial (dₑ) and apical (dₐ) bond lengths (in Å) for the five target cuprates. For planar-square compounds, dₐ is effectively infinite. For compounds with apical Cl⁻ instead of O²⁻, the ligand charge is halved.

| Compound      | dₑ (Å)  | dₐ (Å)  | Apical ligand |
|---------------|---------|---------|---------------|
| La₂CuO₄       | 1.8971  | 2.4289  | O²⁻           |
| Nd₂CuO₄       | 1.971   | ∞       | —             |
| CuGeO₃        | 1.9326  | 2.7549  | O²⁻           |
| Sr₂CuO₂Cl₂   | 1.986   | 2.859   | Cl⁻ (Z=−1)    |
| Cu₃B₇O₁₃Cl   | 2.023   | 3.025   | Cl⁻ (Z=−1)    |

**CuB2O4 reference bond lengths**

For scaling, we need the bond lengths of the reference CuB2O4 sites:

- 4b site (planar‑square): d_e = 1.999 Å, d_a = ∞
- 8d site (distorted octahedron): d_e = 1.937 Å (average), d_a = 3.069 Å

**Reference site mapping**

When estimating Dq, Ds, Dt for a target compound, use the CuB2O4 reference site whose coordination matches:

- For planar‑square compounds (Nd₂CuO₄), use the 4b parameters.
- For octahedral compounds (La₂CuO₄, CuGeO₃, Sr₂CuO₂Cl₂, Cu₃B₇O₁₃Cl), use the 8d parameters.
- For compounds with apical Cl⁻ (Sr₂CuO₂Cl₂, Cu₃B₇O₁₃Cl), adjust the ligand charge Z as indicated in the bond‑length table (charge factor of 1/2 relative to O²⁻) when computing Ds and Dt from the point‑charge formula.

## Workflow steps

### Step 1: CuB2O4 crystal-field parameters
- Role: scored
- Action: Assign the six provided zero-phonon line energies (in eV) to the appropriate Cu site (4b or 8d) and excited states (Γ4+(xy), Γ5+(xz,yz), Γ1+(3r²−z²)) based on the given polarization assignments. For each site, use the tetragonal crystal-field matrix-element expressions to construct a linear system from the three measured excitation energies and solve for Dq, Ds, Dt. Write the resulting six parameters to a JSON file named cuB2O4_parameters.json.
- Output file: `/app/outputs/cuB2O4_parameters.json`
- Format: json
- Contract: {"4b_Dq": <float (eV)>, "4b_Ds": <float (eV)>, "4b_Dt": <float (eV)>, "8d_Dq": <float (eV)>, "8d_Ds": <float (eV)>, "8d_Dt": <float (eV)>}
- Scoring: scored by hidden verifier

### Step 2: Crystal-field parameter estimates for other cuprates
- Role: scored (load-bearing)
- Action: Using the CuB2O4 Dq, Ds, Dt parameters from step_01 as a reference, and the provided Cu–O bond lengths (equatorial d_e, apical d_a) for La2CuO4, Nd2CuO4, CuGeO3, Sr2CuO2Cl2, and Cu3B7O13Cl, apply the point-charge scaling relations (derived from the crystal-field model, with explicit scaling of Dq ~ 1/d_e⁵ and appropriate charge corrections for apical Cl⁻) to estimate Dq, Ds, Dt for each compound. Write a JSON array of objects, each containing compound name and the three parameters, to estimated_parameters.json.
- Output file: `/app/outputs/estimated_parameters.json`
- Format: json
- Contract: [{"compound": "string", "Dq": <float (eV)>, "Ds": <float (eV)>, "Dt": <float (eV)>}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cuB2O4_parameters.json`
- `/app/outputs/estimated_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cuB2O4_parameters.json
- path: `/app/outputs/cuB2O4_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Genuine crystal-field parameters Dq, Ds, Dt for the two Cu²⁺ sites in CuB2O4. The checker compares each value against the paper's reported genuine parameters with a small tolerance.
- schema:
  - `type`: object
  - `required`:
    - `4b_Dq`: number (eV)
    - `4b_Ds`: number (eV)
    - `4b_Dt`: number (eV)
    - `8d_Dq`: number (eV)
    - `8d_Ds`: number (eV)
    - `8d_Dt`: number (eV)

### estimated_parameters.json
- path: `/app/outputs/estimated_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Estimated Dq, Ds, Dt for five related cuprates (La2CuO4, Nd2CuO4, CuGeO3, Sr2CuO2Cl2, Cu3B7O13Cl). The checker compares each parameter against the paper's point-charge model estimates with a tolerance.
- schema:
  - `type`: array
  - `items`:
    - `compound`: string
    - `Dq`: number (eV)
    - `Ds`: number (eV)
    - `Dt`: number (eV)

Notes: All public required inputs (zero-phonon line energies, bond lengths, assignment rules) are provided in the task instruction. The agent must implement the linear-system solution and the scaling equations itself; no precomputed values are given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cuB2O4_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "4b_Dq": "number (eV)",
          "4b_Ds": "number (eV)",
          "4b_Dt": "number (eV)",
          "8d_Dq": "number (eV)",
          "8d_Ds": "number (eV)",
          "8d_Dt": "number (eV)"
        }
      },
      "description": "Genuine crystal-field parameters Dq, Ds, Dt for the two Cu²⁺ sites in CuB2O4. The checker compares each value against the paper's reported genuine parameters with a small tolerance."
    },
    {
      "file": "estimated_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "compound": "string",
          "Dq": "number (eV)",
          "Ds": "number (eV)",
          "Dt": "number (eV)"
        }
      },
      "description": "Estimated Dq, Ds, Dt for five related cuprates (La2CuO4, Nd2CuO4, CuGeO3, Sr2CuO2Cl2, Cu3B7O13Cl). The checker compares each parameter against the paper's point-charge model estimates with a tolerance."
    }
  ],
  "notes": "All public required inputs (zero-phonon line energies, bond lengths, assignment rules) are provided in the task instruction. The agent must implement the linear-system solution and the scaling equations itself; no precomputed values are given."
}
```

## How you are scored
A hidden verifier independently checks each scored output file. It compares your computed values for CuB₂O₄ and the five other cuprates against expected reference values with predetermined tolerances. Your final reward is a weighted combination of the scores from all scored artifacts. Reporting the paper's numbers without performing the computation is not sufficient—the verifier expects the outputs of a correct implementation.
