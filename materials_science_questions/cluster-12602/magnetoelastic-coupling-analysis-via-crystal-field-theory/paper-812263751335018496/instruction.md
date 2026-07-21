# Crystal Electric Field Level Scheme and Elastic Constant Calculation from Magnetoelastic Coupling

## Problem background
The temperature dependence of elastic constants in rare-earth intermetallic compounds often deviates from simple phonon-like behavior. In particular, the shear modulus C55 can show unusual temperature variations due to coupling between the lattice strain and the crystal electric field (CEF) levels of the rare-earth or actinide ion. Understanding such magnetoelastic coupling provides insight into the driving mechanisms behind structural and magnetic phase transitions. In the compound U2Rh3Si5, elastic constant data indicate strong coupling to CEF levels, making it a test case to compute the CEF level scheme and the resulting C55(T) curve from a model that includes both the crystal field and strain coupling.

## Approach
The theoretical model treats the uranium 5f^2 ion (J=4) in a cubic crystal field using Stevens operators O_4^0 and O_4^4. In the |J,m⟩ basis (m = 4,3,…,−4) the angular-momentum operators are:

- J_z is diagonal: ⟨m|J_z|m⟩ = m.
- J_±|m⟩ = √[J(J+1) − m(m±1)] |m±1⟩.
- J_x = (J_+ + J_-)/2, J_y = (J_+ − J_-)/(2i).

The Stevens operators for the fourth-order cubic crystal field are explicitly

O_4^0 = 35 J_z⁴ − [30 J(J+1) − 25] J_z² + [3 J²(J+1)² − 6 J(J+1)] I  ,
O_4^4 = ½ ( J_+⁴ + J_-⁴ ),

where I is the identity matrix of dimension (2J+1)=9.

The crystal-field Hamiltonian at zero strain is

H_CEF = B₄ ( O_4^0 + 5 O_4^4 ),   with B₄ = −20.8×10⁻³ meV.

Diagonalisation of H_CEF lifts the ninefold degeneracy, yielding a singlet (Γ₁), two triplets (Γ₄ and Γ₅), and a doublet (Γ₃). For the negative B₄ value used here the levels are ordered in energy as:

Γ₁ (singlet) < Γ₄ (triplet) < Γ₃ (doublet) < Γ₅ (triplet).

To compute the elastic constant C₅₅(T) a magnetoelastic strain coupling is added:

H_coupling = η₃ e_{xy} (J_x J_y + J_y J_x),   with η₃ = 21 meV,

where e_{xy} is the dimensionless shear strain. The full Hamiltonian at strain e = e_{xy} is

H(e) = H_CEF + η₃ e (J_x J_y + J_y J_x).

For a small strain e = ±h the nine eigenvalue curves E_i(e) are obtained by diagonalising H(e). The centre‑difference step size is h = 1×10⁻⁶. The first and second derivatives at e = 0 are

∂E_i/∂e ≈ [E_i(+h) − E_i(−h)]/(2h),
∂²E_i/∂e² ≈ [E_i(+h) − 2E_i(0) + E_i(−h)] / h².

The contribution of the CEF coupling to C₅₅ is derived from the free energy F = −N k_B T ln(Z):

ΔC₅₅ = N { (1/Z) Σᵢ (∂²E_i/∂e²) exp(−E_i/(k_B T))
               − (1/(k_B T)) Σᵢ (∂E_i/∂e)² exp(−E_i/(k_B T)) },

where the cross‑term involving (Σᵢ ∂E_i/∂e exp(−E_i/kT))² evaluates to zero and is omitted. N = 1.227×10²⁸ m⁻³ is the uranium atom density. The conversion from meV·m⁻³ to GPa uses

1 meV = 1.602176634×10⁻²² J,   1 GPa = 10⁹ J/m³   ⇒   1 meV·m⁻³ = 1.602176634×10⁻³¹ GPa.

The background elastic constant (uncoupled phonon contribution) is given by the Varshni formula:

C_bg(T) = C₀ − s / [exp(T_E / T) − 1],

with C₀ = 73.9 GPa, s = 18.3 GPa, T_E = 783 K. The total C₅₅ is

C₅₅(T) = C_bg(T) + ΔC₅₅(T).

## Reproduction target
1. Compute the CEF level scheme for J = 4 using H_CEF. Output nine levels with degeneracy and irrep label (Γ₁, Γ₄, Γ₃, Γ₅), energies converted to Kelvin (1 meV = 11.604 K), sorted by increasing energy.

2. Using the full magnetoelastic model, compute C₅₅(T) at the temperatures T = 50, 100, 150, 200, 250, 300 K. Follow the finite‑difference procedure with h = 1×10⁻⁶ and the free‑energy expression above.

All required parameters (B₄, η₃, N, C₀, s, T_E) are specified above; no fitting to experimental data is required.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute CEF levels
- Role: scored (load-bearing)
- Action: Build the 9×9 Hamiltonian matrix H_CEF using the Stevens operators defined above. Diagonalise to obtain nine eigenvalues. Convert energies to Kelvin (1 meV = 11.604 K). Identify irreducible representations by degeneracy: Γ₁ (1), Γ₄ (3), Γ₃ (2), Γ₅ (3); for B₄ < 0 the energies increase in order Γ₁, Γ₄, Γ₃, Γ₅. Sort entries by increasing energy. Write array to cef_levels.json.
- Output file: `/app/outputs/cef_levels.json`
- Format: json
- Contract: JSON array of objects, each with keys: energy_K (number), degeneracy (integer), irrep (string). Nine entries sorted by energy.
- Scoring: scored by hidden verifier

### Step 2: Compute C55(T) curve
- Role: scored (load-bearing)
- Action: Construct the full Hamiltonian H(e) = H_CEF + η₃ e (J_x J_y + J_y J_x). Choose finite‑difference step h = 1×10⁻⁶. Diagonalise H(0), H(+h), H(−h) and compute the strain derivatives ∂E_i/∂e and ∂²E_i/∂e² at e=0 using the centre‑difference formulas given above. For each requested temperature T, evaluate ΔC₅₅ using the partition‑function expression with the conversion factor 1.602176634×10⁻³¹ GPa·m³/meV. Add the Varshni background C_bg(T) = C₀ − s/(exp(T_E/T)−1). Write CSV with columns T_K and C55_GPa.
- Output file: `/app/outputs/c55_curve.csv`
- Format: csv
- Contract: CSV with header: T_K, C55_GPa. Rows for T = 50,100,150,200,250,300 K (six rows). Values are floating point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cef_levels.json`
- `/app/outputs/c55_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cef_levels.json
- path: `/app/outputs/cef_levels.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: CEF energy levels (nine entries) with energies in Kelvin, degeneracy, and irrep label. The checker recomputes the eigenvalues from the same Hamiltonian and compares within tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `energy_K`, `degeneracy`, `irrep`
    - `properties`:
      - `energy_K`:
        - `type`: number
      - `degeneracy`:
        - `type`: integer
      - `irrep`:
        - `type`: string
  - `minItems`: 9
  - `maxItems`: 9

### c55_curve.csv
- path: `/app/outputs/c55_curve.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Modeled C55(T) at specified temperatures (50,100,150,200,250,300 K). The checker recomputes C55 using the same model and parameters and compares within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `C55_GPa`
  - `units`:
    - `T_K`: K
    - `C55_GPa`: GPa

Notes: Parameters are as reported in the paper: B4 = −20.8×10⁻³ meV, η3 = 21 meV, N = 1.227×10²⁸ m⁻³, C0 = 73.9 GPa, s = 18.3 GPa, TE = 783 K. The agent must compute the results from these parameters; no experimental data fitting is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cef_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "energy_K",
            "degeneracy",
            "irrep"
          ],
          "properties": {
            "energy_K": {
              "type": "number"
            },
            "degeneracy": {
              "type": "integer"
            },
            "irrep": {
              "type": "string"
            }
          }
        },
        "minItems": 9,
        "maxItems": 9
      },
      "description": "CEF energy levels (nine entries) with energies in Kelvin, degeneracy, and irrep label. The checker recomputes the eigenvalues from the same Hamiltonian and compares within tolerance."
    },
    {
      "file": "c55_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "C55_GPa"
        ],
        "units": {
          "T_K": "K",
          "C55_GPa": "GPa"
        }
      },
      "description": "Modeled C55(T) at specified temperatures (50,100,150,200,250,300 K). The checker recomputes C55 using the same model and parameters and compares within tolerance."
    }
  ],
  "notes": "Parameters are as reported in the paper: B4 = −20.8×10⁻³ meV, η3 = 21 meV, N = 1.227×10²⁸ m⁻³, C0 = 73.9 GPa, s = 18.3 GPa, TE = 783 K. The agent must compute the results from these parameters; no experimental data fitting is required."
}
```

## How you are scored
Your submissions are evaluated by an automated hidden verifier that independently recomputes the expected outputs for each scored workflow stage. The verifier compares your submitted artifacts (cef_levels.json and c55_curve.csv) against its own recomputed reference, grading each stage’s accuracy according to domain-appropriate tolerances. The final reward is a weighted sum of the individual stage scores. Simply reporting expected numbers without performing the required computations will not pass the checks, as the verifier examines the raw artifact content.