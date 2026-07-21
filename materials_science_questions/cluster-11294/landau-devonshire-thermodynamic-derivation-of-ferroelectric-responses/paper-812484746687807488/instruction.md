# Phenomenological model of monoclinic distortion in stressed [111] epitaxial ferroelectric thin films

## Problem background
Phenomenological Landau-Devonshire theory describes ferroelectric materials' thermodynamic potential as a function of polarization and strain. When applied to epitaxial thin films, the free energy can be renormalized to account for substrate-imposed misfit strain and external mechanical load. This task investigates a [111]-oriented PbTiO3 film coherently clamped to a SrTiO3 substrate (in-plane biaxial misfit strain of -0.013) subjected to an additional out-of-plane compressive stress. The question is how stress modifies the equilibrium polarization direction and magnitude, leads to low-symmetry monoclinic states, and affects dielectric and piezoelectric response. The agent will compute the phase stability and property trends without prior knowledge of the paper's conclusions.

## Approach
Use the Landau-Devonshire thermodynamic framework. Starting from the bulk free energy coefficients, elastic compliances, and electrostrictive constants for PbTiO3 (Haun et al., J. Appl. Phys. 62, 3331, 1987), perform a coordinate rotation from the cubic axes to the [1-10], [11-2], [111] crystal frame. Apply a Legendre transformation that incorporates the fixed in-plane biaxial misfit strain and a variable out-of-plane stress to obtain renormalized free energy coefficients a1*, a11*, a12*, A12, A123, A1223, B, C defining the thermodynamic potential F(P1,P2,P3). Then, for a set of out-of-plane stress values, numerically minimize F with respect to the three polarization components to find equilibrium states. From the equilibrium polarization, compute the out-of-plane lattice strain S3' and monoclinic shear strain S4' via the electrostrictive coupling formulas, and compute the out-of-plane dielectric constant ε33' and piezoelectric coefficient d33' from the free energy Hessian. The workflow proceeds in two stages: (1) derive the renormalized coefficients, and (2) minimize the free energy and compute the properties for each stress point. A detailed step-by-step plan is given in the workflow steps below.

## Material Constants (all values at room temperature, SI units)

### Bulk Landau coefficients for PbTiO3 (Haun et al. 1987, T = 298 K)
- α1  = -6.88 × 10^7   J·m·C^{-2}
- α11 = -7.30 × 10^7   J·m^5·C^{-4}
- α12 =  7.50 × 10^8   J·m^5·C^{-4}
- α111 = 2.60 × 10^8   J·m^9·C^{-6}
- α112 = 6.10 × 10^8   J·m^9·C^{-6}
- α123 = -3.70 × 10^9  J·m^9·C^{-6}

### Elastic compliances (Pa^{-1})
- s11 =  8.0 × 10^{-12}
- s12 = -2.5 × 10^{-12}
- s44 =  9.0 × 10^{-12}

### Electrostrictive constants (m^4·C^{-2})
- Q11 =  0.089
- Q12 = -0.026
- Q44 =  0.0675

### Misfit strain
- In-plane biaxial misfit strain: u_m' = u_1' = u_2' = -0.013 (dimensionless)
- The quantity u_m* appearing in the strain formula Eq. (2) is the effective misfit strain; for the present coherently strained film, u_m* = u_m' = -0.013.

## Renormalized free energy

After rotating the bulk elastic Gibbs free energy G(P_i, σ_j) to the [1-10]_{pc}, [11-2]_{pc}, [111]_{pc} frame and applying the Legendre transformation F = G + σ_1' u_1' + σ_2' u_2' with the fixed in-plane strains u_1' = u_2' = u_m', the thermodynamic potential reads (cf. Eq. (1) of the paper):

```
F(P_i, u_k') = a1* (P1^2 + P2^2 + P3^2)
             + A12 (P1 P2 + P1 P3 + P2 P3)
             + a11* (P1^4 + P2^4 + P3^4)
             + a12* (P1^2 P2^2 + P1^2 P3^2 + P2^2 P3^2)
             + A123 [P1^3(P2+P3) + P2^3(P1+P3) + P3^3(P1+P2)]
             + A1223 (P1 P2 P3^2 + P1^3 P2 P3 + P1 P2^2 P3)
             + G6 + B u_m*^2 + C σ_3'^2,
```
where G6 denotes the sixth-order isotropic term α111 (P1^6+P2^6+P3^6) + α112 [P1^4(P2^2+P3^2)+P2^4(P1^2+P3^2)+P3^4(P1^2+P2^2)] + α123 P1^2 P2^2 P3^2.

The renormalized coefficients a1*, a11*, a12*, A12, A123, A1223, B, C are obtained by combining the bulk Landau parameters with the elastic and electrostrictive constants through the [111] coordinate transformation and the Legendre transform. Their explicit algebraic expressions in terms of the bulk constants, elastic compliances, electrostrictive Q coefficients, and u_m' are standard results of the [111]-oriented thin-film LGD theory and can be derived by:

1. Writing the bulk elastic Gibbs function G in the cubic axis frame (including elastic energy, electrostrictive coupling, and the Landau expansion up to sixth order).
2. Transforming polarization and stress to the new frame using the rotation matrix:
   - x1' = (x1 - x2)/√2  → [1-10]_{pc}
   - x2' = (x1 + x2 - 2x3)/√6 → [11-2]_{pc}
   - x3' = (x1 + x2 + x3)/√3 → [111]_{pc}
3. Applying the mechanical boundary conditions:
   - In-plane strains: u1' = u2' = u_m'
   - All in-plane shear strains: u4' = u5' = u6' = 0 (coherent clamping)
   - Out-of-plane stress σ3' is a free variable (taken as the externally applied compressive stress)
   - All other out-of-plane stress components are zero: σ4' = σ5' = 0
4. Solving for the in-plane stresses σ1', σ2' and the out-of-plane strain u3' from the elastic constitutive relations.
5. Performing the Legendre transform F = G + σ1' u_m' + σ2' u_m' and collecting terms in orders of P1, P2, P3.
6. The resulting coefficient set must satisfy the cubic symmetry constraints of the parent phase, which leads to the form of Eq. (1) with six independent renormalized quadratic and quartic coefficients (a1*, A12, a11*, a12*, A123, A1223) and the constant terms B and C.

**Important numerical note**: In the coefficient a1*, the temperature-dependent term α1 = α_0 (T - T_C) is evaluated at room temperature (298 K) using the Haun et al. values. For the purposes of this task, use α1 = -6.88×10^7 J·m·C^{-2} as provided above. All coefficients should be computed once for the fixed u_m' = -0.013 and then used for all stress points. Only the term C σ_3'^2 in F depends explicitly on the variable stress σ_3' (the coefficient C is a constant derived from the elastic compliances).

## Strain formulas (from the paper, Eqs. (2)-(3))

The out-of-plane lattice strain S3' (= u3') and the monoclinic shear strain S4' (= u4'/√2) are given by:

```
S3' = (4 s11 + 8 s12 - 2 s44)/(4 s11 + 8 s12 + s44) * u_m*
    + (Q11 + 2 Q12) s44/(4 s11 + 8 s12 + s44) * (P1^2 + P2^2 + P3^2)
    + (2 s11 + 4 s12) Q44/(4 s11 + 8 s12 + s44) * (P1 P2 + P1 P3 + P2 P3)
    + (s11/3 + 2 s12/3 + s44/3) * σ3'
```

```
S4' = (√2/2) * (Q11 - Q12) s44/(s11 - s12 + s44) * (P1^2 + P2^2 - 2 P3^2)
    + (√2/2) * (s11 - s12) Q44/(s11 - s12 + s44) * (2 P1 P2 - P1 P3 - P2 P3)
```

where σ3' is the out-of-plane stress in Pa (note: 1 GPa = 1×10^9 Pa), and u_m* = u_m' = -0.013.

## Reproduction target
For a [111]-oriented PbTiO3 film coherently strained to a SrTiO3 substrate (in-plane biaxial misfit strain u_m' = -0.013), compute the equilibrium polarization components (P1, P2, P3 in C/m²), out-of-plane lattice strain S3', monoclinic shear strain S4', out-of-plane dielectric constant ε33', and piezoelectric coefficient d33' at the following out-of-plane compressive stress points: σ3' = -3.535, -3.56, -4.36, -4.565, and -4.65 GPa. Write the results to /app/outputs/results_at_stress_points.json. The output must contain at least these five stress points, ordered from least to most compressive. The values will be compared to reference results and the structural trends (e.g., polarization rotation direction, sign of shear strain, emergence of monoclinic states) will be verified.

## Assets

- Bulk Landau-Ginzburg-Devonshire coefficients, elastic compliances, and electrostrictive constants for PbTiO3 (Haun et al., J. Appl. Phys. 62, 3331, 1987). Numerical values are provided in the Material Constants section above.
- SciPy numerical optimization library: pip install scipy
- NumPy: pip install numpy
- Matplotlib (optional): pip install matplotlib

## Workflow steps

### Step 1: Derive renormalized free energy coefficients for [111] epitaxial film
- Role: process
- Action: Using the bulk Landau coefficients, elastic compliances, and electrostrictive constants provided above, perform the coordinate rotation to the [1-10]/[11-2]/[111] frame and the Legendre transformation incorporating the fixed in-plane biaxial misfit strain u_m' = -0.013. Compute the renormalized free energy coefficients a1*, a11*, a12*, A12, A123, A1223, B, C that define the thermodynamic potential F(P1,P2,P3) used in the minimization step. The coefficients are constants for the given misfit strain and material; only the term C σ_3'^2 in F depends on the applied stress. Retain the coefficients for use in Step 2.
- Evidence: (internal use only, not part of the scored output)

### Step 2: Minimize free energy and compute properties at specified stress points
- Role: scored (load-bearing)
- Action: Using the derived renormalized coefficients, for at least the out-of-plane compressive stress values σ3' = -3.535, -3.56, -4.36, -4.565, and -4.65 GPa, numerically minimize F(P1,P2,P3) to find stable equilibrium polarization states. For each stress point, compute the out-of-plane lattice strain S3' and monoclinic shear strain S4' via the electrostrictive relations given in the Strain formulas section, and the out-of-plane dielectric constant ε33' and piezoelectric coefficient d33' from the free energy Hessian. Write the complete results to the output file.
- Output file: `/app/outputs/results_at_stress_points.json`
- Format: json
- Contract: JSON object with keys: "stress_points" (list of float in GPa), "results" (list of objects, each with keys "P1", "P2", "P3" (float C/m^2), "S3" (float, dimensionless), "S4" (float, dimensionless), "d33" (float pm/V), "epsilon33" (float dimensionless), in the same order as the stress points).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_at_stress_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_at_stress_points.json
- path: `/app/outputs/results_at_stress_points.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium polarization components, out-of-plane strain, shear strain, piezoelectric coefficient d33', and dielectric constant ε33' for the stable state at various out-of-plane stress values. The hidden checker compares these values to the paper's reported numbers and also verifies structural trends (monotonic polarization rotation, sign of shear, phase sequence).
- schema:
  - `type`: object
  - `required`:
    - `stress_points`: array of float (GPa)
    - `results`: array of objects
  - `items`:
    - `P1`: float (C/m^2)
    - `P2`: float (C/m^2)
    - `P3`: float (C/m^2)
    - `S3`: float (dimensionless)
    - `S4`: float (dimensionless)
    - `d33`: float (pm/V)
    - `epsilon33`: float (dimensionless)
  - `units`:
    - `P1`: C/m^2
    - `P2`: C/m^2
    - `P3`: C/m^2
    - `S3`: 1
    - `S4`: 1
    - `d33`: pm/V
    - `epsilon33`: 1

Notes: Energy barrier quantification is not included in the scored output; the scoring focuses on the equilibrium polarization, strain, and response properties which are the primary quantitative claims. The phase sequence and critical stress transitions are inferred from the polarization data and included in the structural checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_at_stress_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "stress_points": "array of float (GPa)",
          "results": "array of objects"
        },
        "items": {
          "P1": "float (C/m^2)",
          "P2": "float (C/m^2)",
          "P3": "float (C/m^2)",
          "S3": "float (dimensionless)",
          "S4": "float (dimensionless)",
          "d33": "float (pm/V)",
          "epsilon33": "float (dimensionless)"
        },
        "units": {
          "P1": "C/m^2",
          "P2": "C/m^2",
          "P3": "C/m^2",
          "S3": "1",
          "S4": "1",
          "d33": "pm/V",
          "epsilon33": "1"
        }
      },
      "description": "Equilibrium polarization components, out-of-plane strain, shear strain, piezoelectric coefficient d33', and dielectric constant ε33' for the stable state at various out-of-plane stress values. The hidden checker compares these values to the paper's reported numbers and also verifies structural trends (monotonic polarization rotation, sign of shear, phase sequence)."
    }
  ],
  "notes": "Energy barrier quantification is not included in the scored output; the scoring focuses on the equilibrium polarization, strain, and response properties which are the primary quantitative claims. The phase sequence and critical stress transitions are inferred from the polarization data and included in the structural checks."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results_at_stress_points.json file. It checks that the JSON schema matches the output contract, then compares your computed polarization, strain, dielectric constant, and piezoelectric coefficient at each specified stress point against reference values extracted from the literature. Additionally, it inspects structural trends: whether the polarization rotates monotonically in the expected direction as stress increases, whether the shear strain acquires the physically correct sign, and whether the sequence of monoclinic phases appears at the anticipated critical stresses. The verifier does not reveal the reference values or tolerances. You must execute the full workflow as described; reporting numbers without deriving them from the actual free energy minimization will not pass the structural checks.