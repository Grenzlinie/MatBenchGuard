# Structural and Electronic Properties of Cubic FAPbI3: DFT-PBE and DFT-vdW Benchmarking

## Problem background
Hybrid organic-inorganic perovskites, such as formamidinium lead iodide (FAPbI₃), are promising materials for photovoltaic applications. A key challenge is accurately describing their structural and electronic properties from first principles. This task focuses on computing the lattice constant, electronic band gap, charge-carrier effective masses, and optical absorption of cubic α-FAPbI₃ using two density functional theory (DFT) methods: standard PBE and PBE with van der Waals corrections. The results aim to establish which functional better captures experimental benchmarks for this material, providing guidance for computational studies of perovskite photovoltaics.

## Approach
The approach uses plane-wave DFT calculations with an open-source code. The cubic unit cell of α-FAPbI₃ with the formamidinium (FA) cation oriented along the ⟨100⟩ direction is used as the initial structure. Two geometry optimizations are performed: one with the PBE functional alone (DFT-PBE), and one with PBE augmented by the Grimme D3 dispersion correction (DFT-vdW). For each relaxed structure, static self-consistent field (SCF) calculations and non-self-consistent band structure calculations are executed, both without and with spin-orbit coupling (SOC). From the band structures, the direct band gap at the R point is extracted, and the effective masses of holes and electrons are obtained by parabolic fitting of the valence band maximum and conduction band minimum along three high-symmetry directions (R-Γ, R-X, R-M), averaged. Additionally, using the DFT-PBE+SOC relaxed geometry, the optical absorption spectrum is computed via the imaginary part of the dielectric function. The numerical results are collected and compared to assess the relative performance of the two functionals against known experimental trends.

## Reproduction target
Using the provided cubic FAPbI₃ structure with FA aligned along ⟨100⟩, perform DFT-PBE and DFT-vdW geometry optimizations. For each optimized structure, run SCF and band structure calculations with and without SOC. Extract:
- Lattice constant a (Å)
- Band gap at the R point without SOC, E_g_noSOC (eV)
- Band gap at the R point with SOC, E_g_SOC (eV)
- Average hole effective mass m_h_avg (in units of free electron mass m₀)
- Average electron effective mass m_e_avg (m₀)

Using the DFT-PBE+SOC optimized structure, compute the optical absorption spectrum (imaginary part of the dielectric function ε₂) as a function of photon energy (eV). Write all results into a single JSON file `/app/outputs/results.json` with the structure described in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/
- Cubic FAPbI3 reference structure (Weller et al.): 10.1021/acs.jpclett.5b01632

## Workflow steps

### Step 1: Prepare initial ⟨100⟩ structure
- Role: process
- Action: Obtain the cubic FAPbI3 unit cell with the FA molecule oriented along the ⟨100⟩ direction from the published Weller et al. structure (or the paper's ESI POSCAR) and convert to Quantum ESPRESSO input format.
- Evidence: `/app/outputs/struc.in`

### Step 2: DFT-PBE and DFT-vdW calculations and properties
- Role: scored (load-bearing)
- Action: Run DFT-PBE and DFT-vdW (PBE + Grimme D3 correction) geometry optimizations for the ⟨100⟩ structure. For each optimized structure, perform static SCF and band structure calculations both without and with spin-orbit coupling (SOC). Extract the lattice constant a, the band gap at the R point (E_g_noSOC, E_g_SOC), and compute the hole and electron effective masses (m_h_avg, m_e_avg) by parabolic fitting along R-Γ, R-X, R-M and averaging. Using the PBE+SOC optimized structure, compute the optical absorption spectrum (imaginary part of the dielectric function, ε₂). Write all results into a single JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"methods": {"DFT-PBE": {"a": number, "E_g_noSOC": number, "E_g_SOC": number, "m_h_avg": number, "m_e_avg": number}, "DFT-vdW": {"a": number, "E_g_noSOC": number, "E_g_SOC": number, "m_h_avg": number, "m_e_avg": number}}, "absorption_spectrum": [{"energy_eV": number, "epsilon2": number}, ...]}
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
- description: All DFT results: lattice constant a (Å), band gaps (eV) without and with SOC, average effective masses (m₀), and optical absorption spectrum (energy in eV vs ε₂).
- schema:
  - `type`: object
  - `required`:
    - `methods`: object
    - `absorption_spectrum`: array
  - `properties`:
    - `methods`:
      - `type`: object
      - `required`:
        - `DFT-PBE`: object
        - `DFT-vdW`: object
      - `properties`:
        - `DFT-PBE`:
          - `type`: object
          - `required`:
            - `a`: number
            - `E_g_noSOC`: number
            - `E_g_SOC`: number
            - `m_h_avg`: number
            - `m_e_avg`: number
        - `DFT-vdW`:
          - `type`: object
          - `required`:
            - `a`: number
            - `E_g_noSOC`: number
            - `E_g_SOC`: number
            - `m_h_avg`: number
            - `m_e_avg`: number
    - `absorption_spectrum`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `energy_eV`: number
          - `epsilon2`: number

Notes: The checker will compare the reported values to the paper's hidden reference numbers with appropriate tolerances for each quantity. The absorption spectrum is checked for the presence and approximate location of its main peak.

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
        "required": {
          "methods": "object",
          "absorption_spectrum": "array"
        },
        "properties": {
          "methods": {
            "type": "object",
            "required": {
              "DFT-PBE": "object",
              "DFT-vdW": "object"
            },
            "properties": {
              "DFT-PBE": {
                "type": "object",
                "required": {
                  "a": "number",
                  "E_g_noSOC": "number",
                  "E_g_SOC": "number",
                  "m_h_avg": "number",
                  "m_e_avg": "number"
                }
              },
              "DFT-vdW": {
                "type": "object",
                "required": {
                  "a": "number",
                  "E_g_noSOC": "number",
                  "E_g_SOC": "number",
                  "m_h_avg": "number",
                  "m_e_avg": "number"
                }
              }
            }
          },
          "absorption_spectrum": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "energy_eV": "number",
                "epsilon2": "number"
              }
            }
          }
        }
      },
      "description": "All DFT results: lattice constant a (Å), band gaps (eV) without and with SOC, average effective masses (m₀), and optical absorption spectrum (energy in eV vs ε₂)."
    }
  ],
  "notes": "The checker will compare the reported values to the paper's hidden reference numbers with appropriate tolerances for each quantity. The absorption spectrum is checked for the presence and approximate location of its main peak."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that compares the contents of your `results.json` to reference values derived from the original study. The verifier assigns partial credit based on the accuracy of each reported quantity:
- Lattice constants, band gaps, and effective masses are compared to expected reference values with appropriate tolerances.
- The optical absorption spectrum is checked to confirm it exhibits a physically reasonable main peak location.
- Consistency between the two methods and adherence to known physical plausibility checks are also verified.

The overall score is a weighted combination of these contributions, with the majority of weight placed on the primary numerical properties (lattice constant, band gaps, effective masses). A complete, well-formatted `results.json` that passes shape validation is a prerequisite for scoring, but the reward is determined by the content, not just its presence.
