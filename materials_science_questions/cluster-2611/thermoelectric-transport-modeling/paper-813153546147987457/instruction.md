# DFT-based Seebeck Coefficient of BaSnO3 and KTaO3

## Problem background
The thermoelectric properties of perovskite oxides are of interest for energy conversion and for understanding two-dimensional electron gases at oxide interfaces. The Seebeck coefficient (thermopower) is a key quantity that reflects the asymmetry of electron transport around the Fermi level and is sensitive to the orbital character and anisotropy of the conduction bands. In cubic BaSnO₃ the conduction band minimum has Sn-s character leading to a highly dispersive isotropic band, whereas in cubic KTaO₃ the conduction bands consist of Ta-t₂g states with strong anisotropy. Computing the Seebeck coefficient as a function of carrier concentration at room temperature for these two compounds provides a quantitative probe of the contrasting transport physics.

## Approach
The Seebeck coefficient will be computed from first-principles using density functional theory (DFT) with the Tran‑Blaha modified Becke‑Johnson (TB‑mBJ) exchange‑correlation potential, which yields accurate band gaps and band dispersions for these insulators. The band structures of cubic BaSnO₃ (Pm‑3m, a=4.116 Å) and cubic KTaO₃ (Pm‑3m, a=3.99 Å) will be calculated with the all‑electron Elk code on a dense k‑point mesh. The resulting eigenenergies will be fed into the BoltzTraP code, which solves the Boltzmann transport equation within the constant scattering time approximation to obtain the Seebeck coefficient at 300 K as a function of n‑type doping level. The transport properties of the two materials will be evaluated at three representative carrier densities: 1×10¹⁹, 1×10²⁰ and 1×10²¹ cm⁻³.

## Reproduction target
Produce a file seesebeck_vs_n.json under /app/outputs containing the computed Seebeck coefficients (in μV/K) for n‑type BaSnO₃ and KTaO₃ at the three specified carrier densities. The JSON structure must have top‑level keys 'BaSnO₃' and 'KTaO₃', each an object with fields 'n1e19', 'n1e20', 'n1e21' holding the corresponding floating‑point values. Because the materials are n‑type, negative Seebeck coefficients are expected.

## Assets

- Elk all-electron DFT code (TB-mBJ capable): https://elk.sourceforge.io/
- BoltzTraP transport code: https://www.boltztra.org/
- Cubic BaSnO3 crystal structure data
- Cubic KTaO3 crystal structure data

## Workflow steps

### Step 1: DFT band structure – BaSnO3
- Role: process
- Action: Compute the electronic band structure of cubic BaSnO3 (space group Pm-3m, a=4.116 Å) using the Elk all-electron DFT code with the TB-mBJ exchange-correlation potential. Use a dense k-point mesh to obtain a converged band structure suitable for transport calculations. Output the DFT charge density and eigenenergies in a format usable by BoltzTraP.
- Evidence: `/app/outputs/basno3_elk.log`

### Step 2: DFT band structure – KTaO3
- Role: process
- Action: Compute the electronic band structure of cubic KTaO3 (space group Pm-3m, a=3.99 Å) using the Elk all-electron DFT code with the TB-mBJ exchange-correlation potential. Use the same k-point grid and convergence settings as for BaSnO3. Output the necessary files for BoltzTraP.
- Evidence: `/app/outputs/ktao3_elk.log`

### Step 3: BoltzTraP transport calculation and Seebeck output
- Role: scored (load-bearing)
- Action: Run BoltzTraP on the band-structure outputs from step_01 and step_02 to calculate the Seebeck coefficient at 300 K as a function of carrier concentration under the constant scattering time approximation. Evaluate S at carrier densities n = 1×10¹⁹, 1×10²⁰, and 1×10²¹ cm⁻³ (assuming n-type doping, negative Seebeck expected). Write the resulting values to seebeck_vs_n.json.
- Output file: `/app/outputs/seebeck_vs_n.json`
- Format: json
- Contract: {"BaSnO3": {"n1e19": "float (negative, μV/K)", "n1e20": "float (negative, μV/K)", "n1e21": "float (negative, μV/K)"}, "KTaO3": {"n1e19": "float (negative, μV/K)", "n1e20": "float (negative, μV/K)", "n1e21": "float (negative, μV/K)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/seebeck_vs_n.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### seebeck_vs_n.json
- path: `/app/outputs/seebeck_vs_n.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Seebeck coefficients for n-type BaSnO3 and KTaO3 at three carrier densities, as computed via DFT+TB-mBJ and BoltzTraP.
- schema:
  - `type`: object
  - `required`: `BaSnO3`, `KTaO3`
  - `properties`:
    - `BaSnO3`:
      - `type`: object
      - `required`: `n1e19`, `n1e20`, `n1e21`
      - `properties`:
        - `n1e19`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e19 cm⁻³
        - `n1e20`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e20 cm⁻³
        - `n1e21`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e21 cm⁻³
    - `KTaO3`:
      - `type`: object
      - `required`: `n1e19`, `n1e20`, `n1e21`
      - `properties`:
        - `n1e19`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e19 cm⁻³
        - `n1e20`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e20 cm⁻³
        - `n1e21`:
          - `type`: number
          - `unit`: μV/K
          - `description`: Seebeck coefficient at carrier concentration 1e21 cm⁻³

Notes: Values must be negative (n-type doping). Hidden scoring compares each of the six entries against paper-derived references within a tolerance appropriate for inter-code differences. The trend |Seebeck(KTaO3)| > |Seebeck(BaSnO3)| at each carrier density is also assessed as a structural consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "seebeck_vs_n.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "BaSnO3",
          "KTaO3"
        ],
        "properties": {
          "BaSnO3": {
            "type": "object",
            "required": [
              "n1e19",
              "n1e20",
              "n1e21"
            ],
            "properties": {
              "n1e19": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e19 cm⁻³"
              },
              "n1e20": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e20 cm⁻³"
              },
              "n1e21": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e21 cm⁻³"
              }
            }
          },
          "KTaO3": {
            "type": "object",
            "required": [
              "n1e19",
              "n1e20",
              "n1e21"
            ],
            "properties": {
              "n1e19": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e19 cm⁻³"
              },
              "n1e20": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e20 cm⁻³"
              },
              "n1e21": {
                "type": "number",
                "unit": "μV/K",
                "description": "Seebeck coefficient at carrier concentration 1e21 cm⁻³"
              }
            }
          }
        }
      },
      "description": "Seebeck coefficients for n-type BaSnO3 and KTaO3 at three carrier densities, as computed via DFT+TB-mBJ and BoltzTraP."
    }
  ],
  "notes": "Values must be negative (n-type doping). Hidden scoring compares each of the six entries against paper-derived references within a tolerance appropriate for inter-code differences. The trend |Seebeck(KTaO3)| > |Seebeck(BaSnO3)| at each carrier density is also assessed as a structural consistency check."
}
```

## How you are scored
A hidden verifier will read the submitted seesebeck_vs_n.json and check that each of the six entries is a valid negative number and matches the expected physical value within a tolerance that accounts for differences between DFT implementations. The final reward is a weighted combination of the per‑value checks; getting the right trend (e.g., larger magnitude for the d‑orbital compound) may also contribute to the score. Reporting the paper's numbers without a proper calculation will not succeed; the file must reflect a genuine DFT+BoltzTraP calculation.
