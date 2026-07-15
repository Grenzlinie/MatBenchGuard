# Non‑local electric field gradient analysis of an iron‑porphyrin complex

## Problem background
The iron‑porphyrin complex hemin chloride exhibits a Mössbauer quadrupole splitting that cannot be correctly reproduced (in sign or magnitude) when only the local contribution from iron 3d electrons to the electric field gradient is included. This task aims to compute a more complete electric field gradient by adding non‑local contributions from the axial chlorine ligand and the four in‑plane porphyrin nitrogens, whose electron density also generates a gradient at the iron nucleus. The calculation also yields the quadrupole coupling at the chlorine ligand nucleus. Understanding these effects is important for assessing the quality of extended Hückel wavefunctions in iron‑porphyrin systems.

## Approach
The molecular orbitals of hemin chloride are obtained by an extended Hückel calculation using publicly available geometries and parameters. The electric field gradient at iron is then computed from three components: (1) a local contribution formed from the iron 3d orbital populations using Clementi radial expectation values; (2) a non‑local chlorine contribution from two‑center integrals between Fe 3d and Cl 3s/3p orbitals, evaluated with the alpha‑function expansion technique; and (3) a non‑local nitrogen contribution obtained similarly after rotating the Fe–N bonds to align with a local z‑axis. The four nitrogen atoms are treated individually with the same expansion method. The total non‑local gradient is the sum of the chlorine and nitrogen parts. Antishielding factors and the nuclear quadrupole moment of Fe‑57m are applied to convert the total field gradient into a Mössbauer quadrupole splitting (mm/sec). Separately, the local electric field gradient at chlorine is estimated from the imbalance between Cl 3pz and 3px populations, yielding quadrupole splitting values by two different methods (direct Clementi integral and the Townes‑Dailey atomic coupling constant). All required atomic radial functions, molecular geometry, and extended Hückel parameters are taken from standard literature sources.

## Reproduction target
Produce a single JSON file `/app/outputs/results.json` that contains the following quantities computed from the extended Hückel molecular orbitals: the non‑local gradient contribution from chlorine (q_nonlocal_Cl, in a.u.), the non‑local contribution from the four nitrogens (q_nonlocal_N, a.u.), the total non‑local gradient (q_nonlocal_total, a.u.), the local iron gradient (q_local, a.u.), the total field gradient at iron (q_total, a.u.), the resulting Fe‑57m Mössbauer quadrupole splitting (delta_E_Fe_mm_per_sec, mm/sec), the local field gradient at chlorine (q_Cl_local, a.u.), two estimates of the chlorine quadrupole splitting — one from Clementi radial integrals (delta_E_Cl_mc_per_sec, Mc/sec) and one from the Townes‑Dailey approach (delta_E_Cl_mc_per_sec_TownesDailey, Mc/sec), and the contraction analysis results: the scale factor χ (chi_d_contraction, dimensionless) and the contracted in‑plane <1/r³> expectation values for the dx²‑y² and dxy orbitals (contracted_1_over_r3_dx2_y2 and contracted_1_over_r3_dxy, both in a.u.). All values must be reported to at least five significant digits.

## Assets

- Clementi atomic radial functions (Fe 3d, Cl 3s, Cl 3p, N 2s, N 2p): Published in Clementi E. Tables of atomic functions. IBM Corp. 1965. Available in standard quantum chemistry libraries.
- Molecular geometry of hemin chloride: Crystal structure from Koenig (1965) or constructed from standard porphyrin coordinates: Fe in plane, Fe–N ≈ 2.07 Å, axial Fe–Cl ≈ 2.32 Å along z‑axis. Geometry details are publicly available.
- Extended Hückel parameters (ionisation potentials, Slater exponents for Fe, N, C, H, Cl): Standard parameters from Rettig et al. (1968) and Zerner & Gouterman (1966), available in the computational chemistry literature.

## Workflow steps

### Step 1: Extended Hückel MO calculation for hemin chloride
- Role: process
- Action: Using the published molecular geometry and standard extended Hückel parameters, build the overlap and Hamiltonian matrices and solve the generalised eigenvalue problem to obtain the molecular orbital coefficients and occupation numbers for the 66 occupied molecular orbitals.
- Evidence: `/app/outputs/eh_coefficients.json`

### Step 2: Chlorine non‑local contribution to Fe field gradient
- Role: process
- Action: From the MO coefficients and the Fe–Cl distance, compute the two‑centre integrals between Fe 3d and Cl 3s/3p orbitals with the field gradient operator using the alpha‑function expansion and Clementi neutral‑atom radial functions. Evaluate the non‑local contributions q_nonlocal_Cl(3s), q_nonlocal_Cl(3p) and their sum.
- Evidence: `/app/outputs/cl_nonlocal.json`

### Step 3: Nitrogen non‑local contribution to Fe field gradient
- Role: process
- Action: For each of the four porphyrin nitrogen atoms, perform the necessary coordinate rotations to bring the Fe–N vector along a local z‑axis, then apply the alpha‑function two‑centre expansion using Clementi radial functions for Fe 3d and N 2s/2p. Compute the per‑nitrogen 2s and 2p contributions and sum to obtain total q_nonlocal_N.
- Evidence: `/app/outputs/n_nonlocal.json`

### Step 4: Local Fe electric field gradient from d‑orbital populations
- Role: process
- Action: Using the MO coefficients and the Clementi expectation values of 1/r³ for Fe 3d orbitals, compute the local field gradient q_local at iron from the occupied molecular orbitals.
- Evidence: `/app/outputs/fe_local.json`

### Step 5: Contraction analysis of iron d‑orbitals
- Role: process
- Action: Using the local field gradient q_local from Step 4 and the MO coefficients, compute the scale factor χ according to Eq. (23) of the paper: χ = ( (7/(4×4.978) q_local) + Σ n(μ)(a_{μ,Fe(dz²)}² + a_{μ,Fe(dxy)}²) ) / ( Σ n(μ)(a_{μ,Fe(dx²‑y²)}² + a_{μ,Fe(dxy)}²) ). Then obtain the contracted in‑plane <1/r³> expectation values for the dx²‑y² and dxy orbitals by multiplying the neutral‑atom value (4.978 a.u.) by χ. Write χ and the contracted <1/r³> values to a JSON evidence file.
- Evidence: `/app/outputs/contraction_analysis.json`

### Step 6: Cl‑35 nuclear quadrupole coupling
- Role: process
- Action: From the MO coefficients for chlorine 3p orbitals, compute the population difference between pz and px, then evaluate the local field gradient at chlorine and the quadrupole splitting ΔE using both the Clementi ⟨r⁻³⟩_3p value and the Townes‑Dailey atomic coupling constant, with Cl‑35 quadrupole moment Q = –0.079 barns.
- Evidence: `/app/outputs/cl_quadrupole.json`

### Step 7: Assemble all field gradient, contraction and quadrupole splitting results
- Role: scored (load-bearing)
- Action: Collect the computed q_nonlocal_Cl, q_nonlocal_N, total q_nonlocal, q_local, and q_total, and the contraction parameters χ, contracted_1_over_r3_dx2_y2, contracted_1_over_r3_dxy from the contraction analysis. Apply antishielding factors (1‑R=0.32 for local, (1‑γ'∞)/2=5.07 for non‑local) with Fe‑57m nuclear quadrupole moment Q=0.15 barns to obtain the total Fe Mössbauer quadrupole splitting ΔE in mm/sec. Also collect the Cl local field gradient and the two ΔE estimates (Clementi and Townes‑Dailey). Write all quantities with the required keys to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: q_nonlocal_Cl (float, a.u.), q_nonlocal_N (float, a.u.), q_nonlocal_total (float, a.u.), q_local (float, a.u.), q_total (float, a.u.), delta_E_Fe_mm_per_sec (float), delta_E_Cl_mc_per_sec (float), q_Cl_local (float, a.u.), delta_E_Cl_mc_per_sec_TownesDailey (float), chi_d_contraction (float, dimensionless), contracted_1_over_r3_dx2_y2 (float, a.u.), contracted_1_over_r3_dxy (float, a.u.). All values to at least 5 significant digits.
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
- description: The final combined field gradient, contraction, and quadrupole splitting results, compared against hidden reference values (paper‑reported quantities) with absolute tolerances and structural consistency checks.
- schema:
  - `type`: object
  - `properties`:
    - `q_nonlocal_Cl`:
      - `type`: number
      - `units`: a.u.
    - `q_nonlocal_N`:
      - `type`: number
      - `units`: a.u.
    - `q_nonlocal_total`:
      - `type`: number
      - `units`: a.u.
    - `q_local`:
      - `type`: number
      - `units`: a.u.
    - `q_total`:
      - `type`: number
      - `units`: a.u.
    - `delta_E_Fe_mm_per_sec`:
      - `type`: number
      - `units`: mm/sec
    - `delta_E_Cl_mc_per_sec`:
      - `type`: number
      - `units`: Mc/sec
    - `q_Cl_local`:
      - `type`: number
      - `units`: a.u.
    - `delta_E_Cl_mc_per_sec_TownesDailey`:
      - `type`: number
      - `units`: Mc/sec
    - `chi_d_contraction`:
      - `type`: number
      - `description`: scale factor χ for in-plane d-orbital contraction, dimensionless
    - `contracted_1_over_r3_dx2_y2`:
      - `type`: number
      - `units`: a.u.
    - `contracted_1_over_r3_dxy`:
      - `type`: number
      - `units`: a.u.
  - `required`: `q_nonlocal_Cl`, `q_nonlocal_N`, `q_nonlocal_total`, `q_local`, `q_total`, `delta_E_Fe_mm_per_sec`, `delta_E_Cl_mc_per_sec`, `q_Cl_local`, `delta_E_Cl_mc_per_sec_TownesDailey`, `chi_d_contraction`, `contracted_1_over_r3_dx2_y2`, `contracted_1_over_r3_dxy`

Notes: The checker will compare each value to the paper’s reported numbers using absolute tolerances and will verify that q_nonlocal_total = q_nonlocal_Cl + q_nonlocal_N, that the Fe Mössbauer splitting is correctly derived from the given antishielding factors, and that the contraction parameters are internally consistent with q_local and the MO populations.

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
        "properties": {
          "q_nonlocal_Cl": {
            "type": "number",
            "units": "a.u."
          },
          "q_nonlocal_N": {
            "type": "number",
            "units": "a.u."
          },
          "q_nonlocal_total": {
            "type": "number",
            "units": "a.u."
          },
          "q_local": {
            "type": "number",
            "units": "a.u."
          },
          "q_total": {
            "type": "number",
            "units": "a.u."
          },
          "delta_E_Fe_mm_per_sec": {
            "type": "number",
            "units": "mm/sec"
          },
          "delta_E_Cl_mc_per_sec": {
            "type": "number",
            "units": "Mc/sec"
          },
          "q_Cl_local": {
            "type": "number",
            "units": "a.u."
          },
          "delta_E_Cl_mc_per_sec_TownesDailey": {
            "type": "number",
            "units": "Mc/sec"
          },
          "chi_d_contraction": {
            "type": "number",
            "description": "scale factor χ for in-plane d-orbital contraction, dimensionless"
          },
          "contracted_1_over_r3_dx2_y2": {
            "type": "number",
            "units": "a.u."
          },
          "contracted_1_over_r3_dxy": {
            "type": "number",
            "units": "a.u."
          }
        },
        "required": [
          "q_nonlocal_Cl",
          "q_nonlocal_N",
          "q_nonlocal_total",
          "q_local",
          "q_total",
          "delta_E_Fe_mm_per_sec",
          "delta_E_Cl_mc_per_sec",
          "q_Cl_local",
          "delta_E_Cl_mc_per_sec_TownesDailey",
          "chi_d_contraction",
          "contracted_1_over_r3_dx2_y2",
          "contracted_1_over_r3_dxy"
        ]
      },
      "description": "The final combined field gradient, contraction, and quadrupole splitting results, compared against hidden reference values (paper‑reported quantities) with absolute tolerances and structural consistency checks."
    }
  ],
  "notes": "The checker will compare each value to the paper’s reported numbers using absolute tolerances and will verify that q_nonlocal_total = q_nonlocal_Cl + q_nonlocal_N, that the Fe Mössbauer splitting is correctly derived from the given antishielding factors, and that the contraction parameters are internally consistent with q_local and the MO populations."
}
```

## How you are scored
A hidden verifier compares each numerical field in your `/app/outputs/results.json` against reference values using appropriate tolerances. The verifier checks both the magnitude and the sign of each quantity. It also verifies structural relations, for example that the total non‑local gradient equals the sum of the chlorine and nitrogen contributions, and that the Fe‑57m Mössbauer splitting has been correctly derived from the given antishielding factors and nuclear quadrupole moment. The final reward is a weighted combination of checks on all fields in the file, with the primary weight on the correct reproduction of the field gradient and quadrupole splitting values. The intermediate process artifacts (`eh_coefficients.json`, `cl_nonlocal.json`, etc.) are not directly scored but must be generated as part of the computation pipeline.
