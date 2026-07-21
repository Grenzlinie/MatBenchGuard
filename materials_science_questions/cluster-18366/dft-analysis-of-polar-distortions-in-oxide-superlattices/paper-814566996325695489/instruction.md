# Geometric strain analysis of (111)-oriented ZrO₂ polymorphs on a TiN/MgO(001) substrate

## Problem background
ZrO₂ thin films can exhibit ferroelectricity when the polar orthorhombic (Pca2₁) phase is stabilized. Four major polymorphs exist — cubic, tetragonal, monoclinic, and orthorhombic — and the formation of the ferroelectric o-phase is known to be influenced by substrate-induced strain. When (111)-textured ZrO₂ films are grown on a TiN/MgO(001) template, the in-plane lattice matching between the ZrO₂ (111) atomic arrangement and the underlying TiN layer imposes an anisotropic strain. This task reproduces the geometric strain analysis that quantifies how the in-plane deformation of the ZrO₂ (111) atomic triangles compares to the substrate-matched dimension of 5.996 Å, providing a prediction of which polymorphs are most favorable under the strain.

## Approach
The analysis is performed for the four polymorphs using their lattice constants and Zr atomic positions obtained from the literature. For each polymorph, the (111) plane geometry is constructed. The Zr atoms define upward and downward unit triangles; for each triangle the effective in-plane repeat distances a_{⟨1-10⟩} and a_{⟨11-2⟩} and the internal angle α are computed. From these, two mismatch parameters are defined: Δa = |a_{⟨1-10⟩} - 5.996 Å| + |a_{⟨11-2⟩} - 5.996 Å| (tensile/compressive mismatch) and Δα = |α - 90°| (shear deformation). The values for the two triangles are averaged to obtain Δa_avg and Δα_avg for the polymorph. For the orthorhombic structure, the specific in-plane distances a_{[-211]} and a_{[1-21]} are also determined. The resulting numbers characterize how well each phase can accommodate the strain from the TiN/MgO(001) substrate.

## Reproduction target
Compute the strain mismatch parameters (Δa_avg, Δα_avg) for the cubic, tetragonal, monoclinic, and orthorhombic ZrO₂ (111) planes matched to a TiN/MgO(001) substrate with a reference length of 5.996 Å. Additionally, report the specific orthorhombic distances a_{[-211]} and a_{[1-21]}. The computed values will be compared to the strain model’s predictions of phase accommodation preferences — i.e., which polymorphs are predicted to be most favored under the substrate-imposed strain.

## Assets

- numpy: numpy
- Cubic ZrO₂ structure (Namavar et al., 2007): 10.1088/0957-4484/18/41/415702
- Tetragonal ZrO₂ structure (Kisi & Howard, 1998)
- Monoclinic ZrO₂ structure (Wang et al., 1999)
- Orthorhombic ZrO₂ structure (Kisi et al., 1989): 10.1111/j.1151-2916.1989.tb06301.x

## Workflow steps

### Step 1: Compile structural parameters for the four ZrO₂ polymorphs
- Role: process
- Action: Obtain the lattice constants and Zr atomic positions for the cubic, tetragonal, monoclinic, and orthorhombic polymorphs of ZrO₂ from the cited public literature (Refs. 29, 25, 30, 21). These structural inputs are required for the subsequent geometric strain analysis.
- Evidence: `/app/outputs/structural_parameters.txt`

### Step 2: Geometric strain analysis of (111) ZrO₂ on TiN/MgO(001)
- Role: scored (load-bearing)
- Action: From the compiled structural parameters, construct the (111) plane geometry for each polymorph. Identify the upward and downward unit triangles formed by Zr atoms and compute the effective in-plane repeat distances a_{⟨1-10⟩} and a_{⟨11-2⟩} and the triangle internal angle α. Compute the tensile/compressive mismatch Δa = |a_{⟨1-10⟩} - 5.996 Å| + |a_{⟨11-2⟩} - 5.996 Å| and the shear deformation Δα = |α - 90°| for each triangle. Average over the two triangles to obtain Δa_avg and Δα_avg for each polymorph. Additionally, for the orthorhombic structure, report the specific in-plane distances a_{[-211]} and a_{[1-21]}. Write all results to step_01_strain_analysis.json.
- Output file: `/app/outputs/step_01_strain_analysis.json`
- Format: json
- Contract: object with keys 'cubic', 'tetragonal', 'monoclinic', 'orthorhombic'. Each value is an object with numeric fields: 'a_1-10' (Å), 'a_11-2' (Å), 'alpha' (deg), 'Delta_a_avg' (Å), 'Delta_alpha_avg' (deg). 'orthorhombic' additionally contains 'a_minus211' (Å) and 'a_1-21' (Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_strain_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_strain_analysis.json
- path: `/app/outputs/step_01_strain_analysis.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed geometric strain mismatch parameters and specific atomic distances for the four ZrO₂ polymorphs on a (111) plane matched to a TiN/MgO(001) substrate.
- schema:
  - `type`: object
  - `required`:
    - `cubic`:
      - `a_1-10`: number (Å)
      - `a_11-2`: number (Å)
      - `alpha`: number (degrees)
      - `Delta_a_avg`: number (Å)
      - `Delta_alpha_avg`: number (degrees)
    - `tetragonal`:
      - `a_1-10`: number (Å)
      - `a_11-2`: number (Å)
      - `alpha`: number (degrees)
      - `Delta_a_avg`: number (Å)
      - `Delta_alpha_avg`: number (degrees)
    - `monoclinic`:
      - `a_1-10`: number (Å)
      - `a_11-2`: number (Å)
      - `alpha`: number (degrees)
      - `Delta_a_avg`: number (Å)
      - `Delta_alpha_avg`: number (degrees)
    - `orthorhombic`:
      - `a_1-10`: number (Å)
      - `a_11-2`: number (Å)
      - `alpha`: number (degrees)
      - `Delta_a_avg`: number (Å)
      - `Delta_alpha_avg`: number (degrees)
      - `a_minus211`: number (Å)
      - `a_1-21`: number (Å)

Notes: The checker will recompute Delta_a_avg and Delta_alpha_avg from the reported a_1-10, a_11-2, and alpha values, and then compare the averages and specific distances to hidden reference values using tolerances. The relational trend (orthorhombic vs monoclinic) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_strain_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "cubic": {
            "a_1-10": "number (Å)",
            "a_11-2": "number (Å)",
            "alpha": "number (degrees)",
            "Delta_a_avg": "number (Å)",
            "Delta_alpha_avg": "number (degrees)"
          },
          "tetragonal": {
            "a_1-10": "number (Å)",
            "a_11-2": "number (Å)",
            "alpha": "number (degrees)",
            "Delta_a_avg": "number (Å)",
            "Delta_alpha_avg": "number (degrees)"
          },
          "monoclinic": {
            "a_1-10": "number (Å)",
            "a_11-2": "number (Å)",
            "alpha": "number (degrees)",
            "Delta_a_avg": "number (Å)",
            "Delta_alpha_avg": "number (degrees)"
          },
          "orthorhombic": {
            "a_1-10": "number (Å)",
            "a_11-2": "number (Å)",
            "alpha": "number (degrees)",
            "Delta_a_avg": "number (Å)",
            "Delta_alpha_avg": "number (degrees)",
            "a_minus211": "number (Å)",
            "a_1-21": "number (Å)"
          }
        }
      },
      "description": "Computed geometric strain mismatch parameters and specific atomic distances for the four ZrO₂ polymorphs on a (111) plane matched to a TiN/MgO(001) substrate."
    }
  ],
  "notes": "The checker will recompute Delta_a_avg and Delta_alpha_avg from the reported a_1-10, a_11-2, and alpha values, and then compare the averages and specific distances to hidden reference values using tolerances. The relational trend (orthorhombic vs monoclinic) is also verified."
}
```

## How you are scored
Your reward is determined by a hidden verifier that reads your step_01_strain_analysis.json. The verifier validates the file structure, recomputes Δa_avg and Δα_avg from your reported a_1-10, a_11-2, and alpha, and then compares the averaged quantities and the specific orthorhombic distances to hidden reference values using absolute tolerances. It also checks the relative ordering between the orthorhombic and monoclinic phases (as predicted by the strain model). The reward is proportional to the fraction of validation checks that pass; full credit requires all checks to succeed. There is no partial credit for the data preparation step, but its evidence file must be present.
