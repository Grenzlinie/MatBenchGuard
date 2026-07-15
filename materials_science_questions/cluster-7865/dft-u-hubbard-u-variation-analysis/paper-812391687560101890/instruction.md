# Stoner Enhancement Factors of UPt3 and CeAl3 from Frozen Spin-Wave LSDA Calculations

## Problem background
Heavy fermion compounds such as UPt₃ and CeAl₃ exhibit strongly enhanced low-temperature properties driven by magnetic fluctuations. Within the local spin-density approximation (LSDA) to density functional theory, the static interacting spin susceptibility χ(q) can be computed by applying external magnetic fields in frozen spin-wave configurations. The Stoner enhancement factor S(q) = χ(q) / χ_s(q) quantifies how much the interacting susceptibility is enhanced over the single-particle (non-interacting) susceptibility χ_s(q), providing insight into the degree of magnetic correlations. This task aims to compute S(q) at several wavevectors along the c-axis of the hexagonal Brillouin zone for both UPt₃ and CeAl₃, as well as the static uniform susceptibility χ(0).

## Approach
The core idea is to perform self-consistent spin-polarized LSDA calculations for supercells that are commensurate with frozen spin-wave patterns at four wavevectors (q = 0, π/(2c), π/c, 2π/c). For each q, an external magnetic field is applied as a static frozen spin wave (uniform, alternating, etc.) that stabilises a specific magnetic configuration. The induced magnetic moment per formula unit is extracted from the self-consistent charge and spin density, and the interacting susceptibility is obtained as χ(q) = M / H. The single-particle susceptibility χ_s(q) is computed separately from the band structure (or density of states) of the non-spin-polarized system, effectively removing exchange-correlation enhancement. The Stoner enhancement S(q) is then simply the ratio χ(q) / χ_s(q). This approach captures both the spin-flip contributions of states near the Fermi energy and the self-consistent response of the electronic structure to the spin polarization.

## Reproduction target
Produce the Stoner enhancement factors S(q) for UPt₃ and CeAl₃ at the four specified wavevectors along the c-axis (q = 0, π/(2c), π/c, 2π/c), and the static uniform susceptibility χ(0) for both compounds. χ(0) must be reported in units of 10⁻⁴ emu/mol. Write all ten numerical values into a single JSON file `/app/outputs/step_01_results.json` that follows the output schema described in the step contract (fields: UPt3_S_q0, UPt3_S_q_pi2c, UPt3_S_q_pic, UPt3_S_q_2pic, CeAl3_S_q0, CeAl3_S_q_pi2c, CeAl3_S_q_pic, CeAl3_S_q_2pic, UPt3_chi0, CeAl3_chi0).

## Assets

- Crystal structure of UPt3: https://materialsproject.org/materials/mp-541720
- Crystal structure of CeAl3: https://materialsproject.org/materials/mp-9743
- LSDA-capable open-source DFT code (e.g. Quantum ESPRESSO): https://www.quantum-espresso.org
- LSDA pseudopotentials for U, Pt, Ce, Al: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Obtain crystal structures
- Role: process
- Action: Retrieve the hexagonal crystal structures of UPt₃ and CeAl₃ from a public database (Materials Project IDs mp-541720 and mp-9743) and save them in a format suitable for the chosen DFT code.
- Evidence: none

### Step 2: Build supercells with frozen spin‑wave configurations
- Role: process
- Action: Construct the required supercells for the four wavevectors along the c‑axis: q=0 (2 formula units), q=π/(2c) (8 formula units), q=π/c (4 formula units), q=2π/c (2 formula units). Apply external magnetic fields as frozen spin waves: for q=0 a uniform 100 T; for q=2π/c opposite fields of 100 T on the two f‑atom sites; for q=π/c opposite fields of 200 T in a pair of unit cells; for q=π/(2c) a four‑unit‑cell pattern with alternating fields corresponding to 200 T.
- Evidence: none

### Step 3: Self‑consistent LSDA calculations
- Role: process
- Action: For each supercell configuration, run self‑consistent spin‑polarized LSDA calculations to convergence. Extract the induced magnetic moment per formula unit and compute the interacting susceptibility χ(q) = M / H.
- Evidence: none

### Step 4: Single‑particle susceptibility χ_s(q)
- Role: process
- Action: Compute the single‑particle (non‑interacting) susceptibility χ_s(q) for the same supercell geometries. This can be obtained from the paramagnetic (non‑spin‑polarized) band structure or density of states without exchange‑correlation enhancement.
- Evidence: none

### Step 5: Compute Stoner enhancements and χ(0)
- Role: scored (load-bearing)
- Action: Calculate S(q) = χ(q) / χ_s(q) for each of the four q vectors for both UPt₃ and CeAl₃. Also extract the uniform static susceptibility χ(0) from the q=0 calculation (units: 10⁻⁴ emu/mol). Write all results to step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: object with the following numeric fields: UPt3_S_q0, UPt3_S_q_pi2c, UPt3_S_q_pic, UPt3_S_q_2pic, CeAl3_S_q0, CeAl3_S_q_pi2c, CeAl3_S_q_pic, CeAl3_S_q_2pic, UPt3_chi0 (10⁻⁴ emu/mol), CeAl3_chi0 (10⁻⁴ emu/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The computed Stoner enhancement factors S(q) for UPt₃ and CeAl₃ at the four wavevectors, and the static uniform susceptibility χ(0) for both compounds. The hidden checker compares the values to the paper's reported numbers using mean absolute relative error (MARE); full credit is awarded if MARE ≤ 20%, linearly decreasing to 0 at MARE = 50%. The ordering of S(q) across q is also checked as a light structural audit.
- schema:
  - `type`: object
  - `required`:
    - `UPt3_S_q0`: number
    - `UPt3_S_q_pi2c`: number
    - `UPt3_S_q_pic`: number
    - `UPt3_S_q_2pic`: number
    - `CeAl3_S_q0`: number
    - `CeAl3_S_q_pi2c`: number
    - `CeAl3_S_q_pic`: number
    - `CeAl3_S_q_2pic`: number
    - `UPt3_chi0`: number
    - `CeAl3_chi0`: number
  - `units`:
    - `UPt3_chi0`: 10⁻⁴ emu/mol
    - `CeAl3_chi0`: 10⁻⁴ emu/mol
  - `additionalProperties`: False

Notes: The agent must perform all computational steps; the final JSON file is the only scored artifact. Differences in pseudopotential, k‑point mesh, and basis set will cause a natural spread in the computed values, which is absorbed by the tolerant scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "UPt3_S_q0": "number",
          "UPt3_S_q_pi2c": "number",
          "UPt3_S_q_pic": "number",
          "UPt3_S_q_2pic": "number",
          "CeAl3_S_q0": "number",
          "CeAl3_S_q_pi2c": "number",
          "CeAl3_S_q_pic": "number",
          "CeAl3_S_q_2pic": "number",
          "UPt3_chi0": "number",
          "CeAl3_chi0": "number"
        },
        "units": {
          "UPt3_chi0": "10⁻⁴ emu/mol",
          "CeAl3_chi0": "10⁻⁴ emu/mol"
        },
        "additionalProperties": false
      },
      "description": "The computed Stoner enhancement factors S(q) for UPt₃ and CeAl₃ at the four wavevectors, and the static uniform susceptibility χ(0) for both compounds. The hidden checker compares the values to the paper's reported numbers using mean absolute relative error (MARE); full credit is awarded if MARE ≤ 20%, linearly decreasing to 0 at MARE = 50%. The ordering of S(q) across q is also checked as a light structural audit."
    }
  ],
  "notes": "The agent must perform all computational steps; the final JSON file is the only scored artifact. Differences in pseudopotential, k‑point mesh, and basis set will cause a natural spread in the computed values, which is absorbed by the tolerant scoring."
}
```

## How you are scored
A hidden verifier evaluates your `step_01_results.json` against reference values (the published results for the same quantities). The verifier compares your computed S(q) and χ(0) values to the expected ones using a metric that penalizes large relative deviations: full credit is awarded when your values are in close agreement with the reference, and the reward decreases gradually as the deviation grows. In addition, the verifier inspects the ordering of S(q) across the four q points for each compound and checks that it matches the expected trend. The total reward is a weighted combination of these two assessments. You do not need to match any specific pre‑announced tolerance; just produce the most accurate values you can from a correct implementation of the described workflow.
