# Non‑retarded Hamaker constants and retarded Casimir‑Lifshitz free energy for gapped metal–liquid–PTFE systems

## Problem background
Casimir-Lifshitz forces arise from quantum fluctuations of the electromagnetic field and depend on the dielectric properties of the interacting materials. In a three-layer planar system — a gapped metal (Ca_{6-x}Al_7O_{16}), an intervening liquid (methanol), and a PTFE surface — the force can be attractive or repulsive depending on the relative magnitudes of the dielectric functions. The gapped metal can exhibit different electronic behavior depending on its stoichiometry (x = 0, 0.25, or 0.5), ranging from metallic to insulating. The non-retarded Hamaker constant describes the interaction at very short separations, while the fully retarded Casimir-Lifshitz theory accounts for the finite speed of light and can alter the balance between attractive and repulsive contributions. The zero-frequency (static) dielectric response plays a crucial role in determining the sign of the force at nanoscale distances. This task requires computing these quantities for three stoichiometries of Ca_{6-x}Al_7O_{16} interacting with PTFE across methanol at room temperature.

## Approach
The dielectric functions ε(iξ) on the imaginary frequency axis are constructed for each material using a damped Lorentz oscillator model. The oscillator parameters (frequencies and strengths) for the three Ca_{6-x}Al_7O_{16} compositions are provided, as are those for methanol and PTFE. These are analytically continued to the Matsubara frequencies ξ_m = 2πkT m / ℏ with a damping parameter. From these, the non-retarded Hamaker constant is computed by evaluating the product of the non-retarded TM reflection coefficients (which depend only on the dielectric contrasts) and performing a double sum over the Matsubara index m (with half weight at m=0) and the image-charge expansion index j. The zero-frequency contribution A_{m=0} is isolated from the m=0 term alone. The fully retarded Casimir-Lifshitz free energy F(d) is obtained from the Lifshitz formula: a sum over Matsubara frequencies and an integral over the transverse wave vector q that includes both TM and TE polarization contributions, with the retardation encoded through the exponential factor exp(-2κ₂ d). The reflected Fresnel coefficients for each polarization and the wave-vector-dependent κ_i are evaluated using the computed ε(iξ_m). All calculations are performed at T = 300 K, using sufficient frequency and q ranges to reach convergence.

## Reproduction target
1. Compute the non-retarded Hamaker constant A^{NR} (in eV) and its zero-frequency contribution A_{m=0} (in eV) for each of the three compositions: Ca6Al7O16, Ca5.75Al7O16, and Ca5.5Al7O16 interacting with PTFE across methanol at 300 K. Write the results to hamaker_constants.csv. 2. Compute the fully retarded Casimir-Lifshitz free energy F(d) (in eV) for the same three systems at 100 logarithmically spaced distances d ranging from 0.5 nm to 100 nm, using the same temperature. Report the results (stoichiometry, distance_nm, F_retarded_eV) in free_energy_data.csv. The free energy sign convention should be such that a positive F(d) indicates a repulsive interaction.

## Assets

- Oscillator parameters for Ca_{6-x}Al_7O_{16} dielectric functions
- Oscillator parameters for Methanol and PTFE
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare dielectric functions on imaginary frequency axis
- Role: process
- Action: Read the provided oscillator parameter files for Ca_{6-x}Al_7O_{16}, methanol, and PTFE. For each material, construct the complex dielectric function ε(iξ) at the required Matsubara frequencies ξ_m = 2πkT/ℏ using a Lorentz oscillator model with damping. Implement the analytic continuation to imaginary frequencies. Store the evaluated ε(iξ_m) arrays.
- Evidence: `/app/outputs/dielectric_functions.json`

### Step 2: Compute non‑retarded Hamaker constants and zero‑frequency contributions
- Role: scored
- Action: Using the prepared dielectric functions, evaluate the non‑retarded reflection product r_NR^{12} r_NR^{32} = (ε_1-ε_2)/(ε_1+ε_2) × (ε_3-ε_2)/(ε_3+ε_2) at each Matsubara frequency. Compute the Hamaker constant A^{NR} = (3/2) k_B T sum_{m=0}^{∞}′ sum_{j=1}^{∞} [r^{21} r^{23}]^j / j^3. Extract the zero‑frequency contribution A_{m=0} from the m=0 term alone. Perform the sums until convergence. Write the results in hamaker_constants.csv.
- Output file: `/app/outputs/hamaker_constants.csv`
- Format: csv
- Contract: CSV with columns: stoichiometry (string), A_NR_eV (float), A_m0_eV (float). Three rows for Ca6Al7O16, Ca5.75Al7O16, Ca5.5Al7O16.
- Scoring: scored by hidden verifier

### Step 3: Compute fully retarded Casimir‑Lifshitz free energy vs. separation
- Role: scored (load-bearing)
- Action: Implement the full Lifshitz formula including both TE and TM polarizations with correct Fresnel coefficients, a momentum integral over q, and a distance‑dependent exponential factor. For each stoichiometry, compute the free energy F(d) at 100 logarithmically spaced distances from 0.5 nm to 100 nm at T=300 K. Use sufficient Matsubara frequencies and q‑range to achieve convergence. Write the (stoichiometry, distance, F) data to free_energy_data.csv.
- Output file: `/app/outputs/free_energy_data.csv`
- Format: csv
- Contract: CSV with columns: stoichiometry (string), distance_nm (float), F_retarded_eV (float). Separate sections for each stoichiometry, with at least 100 logarithmically spaced distances from 0.5 nm to 100 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hamaker_constants.csv`
- `/app/outputs/free_energy_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hamaker_constants.csv
- path: `/app/outputs/hamaker_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Non‑retarded Hamaker constants and zero‑frequency contributions for Ca6Al7O16, Ca5.75Al7O16, and Ca5.5Al7O16. Values are deterministic given the inputs; scored by exact comparison with paper‑reported numbers within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `stoichiometry`, `A_NR_eV`, `A_m0_eV`
  - `units`:
    - `A_NR_eV`: eV
    - `A_m0_eV`: eV

### free_energy_data.csv
- path: `/app/outputs/free_energy_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Distance‑dependent Casimir‑Lifshitz free energy for each stoichiometry. The checker will verify structural properties: existence and approximate location of sign changes (repulsion) for the metallic phases, and attractiveness for all distances for the insulating phase.
- schema:
  - `type`: table
  - `required_columns`: `stoichiometry`, `distance_nm`, `F_retarded_eV`
  - `units`:
    - `distance_nm`: nm
    - `F_retarded_eV`: eV

Notes: The Hamaker constants are compared against the paper’s Table II; the free‑energy curves are audited for sign‑reversal distances consistent with the paper’s reported transitions. All values are computed from the same provided dielectric parameter files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hamaker_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stoichiometry",
          "A_NR_eV",
          "A_m0_eV"
        ],
        "units": {
          "A_NR_eV": "eV",
          "A_m0_eV": "eV"
        }
      },
      "description": "Non‑retarded Hamaker constants and zero‑frequency contributions for Ca6Al7O16, Ca5.75Al7O16, and Ca5.5Al7O16. Values are deterministic given the inputs; scored by exact comparison with paper‑reported numbers within a hidden tolerance."
    },
    {
      "file": "free_energy_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "stoichiometry",
          "distance_nm",
          "F_retarded_eV"
        ],
        "units": {
          "distance_nm": "nm",
          "F_retarded_eV": "eV"
        }
      },
      "description": "Distance‑dependent Casimir‑Lifshitz free energy for each stoichiometry. The checker will verify structural properties: existence and approximate location of sign changes (repulsion) for the metallic phases, and attractiveness for all distances for the insulating phase."
    }
  ],
  "notes": "The Hamaker constants are compared against the paper’s Table II; the free‑energy curves are audited for sign‑reversal distances consistent with the paper’s reported transitions. All values are computed from the same provided dielectric parameter files."
}
```

## How you are scored
Your outputs are scored by a hidden verifier. For hamaker_constants.csv, the verifier compares each computed Hamaker constant and zero-frequency contribution to reference values obtained from the same input oscillator parameters using a tight numerical tolerance. For free_energy_data.csv, the verifier performs a structural audit: it verifies that the free energy is reported over the full distance range and checks for the presence and approximate location of sign reversals (if any) as well as overall sign consistency. The final reward is a weighted combination of the scores from the two output files. Providing the correct values from the paper’s tables without following the prescribed computational workflow will not yield full credit.
