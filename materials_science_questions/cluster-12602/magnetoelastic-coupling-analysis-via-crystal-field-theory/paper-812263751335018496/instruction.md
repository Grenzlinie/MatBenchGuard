# Crystal Electric Field Level Scheme and Elastic Constant Calculation from Magnetoelastic Coupling

## Problem background
The temperature dependence of elastic constants in rare-earth intermetallic compounds often deviates from simple phonon-like behavior. In particular, the shear modulus C55 can show unusual temperature variations due to coupling between the lattice strain and the crystal electric field (CEF) levels of the rare-earth or actinide ion. Understanding such magnetoelastic coupling provides insight into the driving mechanisms behind structural and magnetic phase transitions. In the compound U2Rh3Si5, elastic constant data indicate strong coupling to CEF levels, making it a test case to compute the CEF level scheme and the resulting C55(T) curve from a model that includes both the crystal field and strain coupling.

## Approach
The theoretical model treats the uranium 5f^2 ion (J=4) in a cubic crystal field using Stevens operators O4^0 and O4^4. The Hamiltonian H_CEF = B4 (O4^0 + 5 O4^4) is diagonalized to obtain the CEF level scheme. The levels are labeled by their degeneracy and irreducible representations (Γ1, Γ3, Γ4, Γ5). to compute the elastic constant C55(T), a magnetoelastic strain coupling term η3 e_xy (J_x J_y + J_y J_x) is added to the Hamiltonian. By diagonalizing the full Hamiltonian for a small applied strain e_xy and using finite differences, one obtains the strain derivatives of the energy levels. The contribution ΔC55 is calculated from the second strain derivative of the free energy through the partition function over the nine CEF levels. This ΔC55 is then added to a background elastic constant described by the Varshni formula C_bg(T) = C0 - s/(exp(T_E/T)-1). The computation requires only the given parameters (B4, η3, N, C0, s, T_E) and standard linear algebra and thermodynamics.

## Reproduction target
Compute the CEF level scheme for a J=4 ion in a cubic crystal field with parameter B4 = −20.8×10⁻³ meV: the nine eigenvalues with their degeneracies and irreducible representation labels (Γ1, Γ3, Γ4, Γ5), with energies converted to Kelvin. Then, using the full model with magnetoelastic coupling (η3 = 21 meV, atom density N = 1.227×10²⁸ m⁻³) and the Varshni background (C0 = 73.9 GPa, s = 18.3 GPa, T_E = 783 K), compute the temperature-dependent shear modulus C55 at the specific temperatures 50 K, 100 K, 150 K, 200 K, 250 K, and 300 K. The output artifacts must be formatted exactly as specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute CEF levels
- Role: scored (load-bearing)
- Action: Build the 9×9 Hamiltonian matrix for a J=4 ion in a cubic crystal field using Stevens operators O_4^0 and O_4^4 with the given parameter B4. Diagonalize to obtain nine eigenvalues. Convert energies to Kelvin (1 meV = 11.604 K). Identify irreducible representations: singlet Γ1, doublet Γ3, triplet Γ4, triplet Γ5 based on degeneracy. Sort by increasing energy. Write array to cef_levels.json.
- Output file: `/app/outputs/cef_levels.json`
- Format: json
- Contract: JSON array of objects, each with keys: energy_K (number), degeneracy (integer), irrep (string). Nine entries sorted by energy.
- Scoring: scored by hidden verifier

### Step 2: Compute C55(T) curve
- Role: scored (load-bearing)
- Action: Construct the full Hamiltonian including the magnetoelastic coupling term with η3 = 21 meV and strain e_xy. Diagonalize for small strain and use finite differences to compute first and second derivatives of the nine eigenvalues with respect to e_xy at zero strain. Using the partition function over these nine levels, calculate ΔC55(T) via the formula that includes the strain derivatives (the squared term is zero). Add the Varshni background C_bg(T) = C0 - s/(exp(TE/T) - 1) with C0=73.9 GPa, s=18.3 GPa, TE=783 K. Compute total C55 at temperatures 50, 100, 150, 200, 250, 300 K. Write CSV with columns T_K and C55_GPa.
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
