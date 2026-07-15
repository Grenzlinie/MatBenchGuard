# Mulliken Charge Analysis of Carbon-Doped Beta-FeSi2 Clusters

## Problem background
β-FeSi₂ is a semiconductor with a complex crystal structure whose optical properties (photoluminescence, electroluminescence) are sensitive to local impurity potentials. The hypothesis is that substitutional carbon, which has a higher electronegativity than silicon, could introduce a local impurity potential that attracts electrons and potentially forms a bound Wannier exciton, thereby enhancing the oscillator strength. To investigate this, the electronic charge distribution around a substitutional carbon atom in the β-FeSi₂ lattice needs to be quantified and compared to that of the silicon atom it replaces.

## Approach
Two cluster models are constructed from the β-FeSi₂ crystal structure: a reference Fe₁₅Si₃₀ cluster centered on a Si atom, and a carbon-doped CFe₁₅Si₂₉ cluster where the central Si is replaced by C. A self-consistent DFT calculation is performed on each cluster using a quantum chemistry package with the 6-311G(d) basis set and a standard exchange-correlation functional (e.g., B3LYP). Mulliken population analysis is then applied to extract the atomic charge on the central atom in each cluster for comparison.

## Reproduction target
From the β-FeSi₂ crystal structure, build the Fe₁₅Si₃₀ and CFe₁₅Si₂₉ clusters as described. Run DFT calculations on both clusters using a publicly available quantum chemistry package with the 6-311G(d) basis set and a standard functional. Compute the Mulliken atomic charge on the central atom (Si in Fe₁₅Si₃₀, C in CFe₁₅Si₂₉) and save the two charge values with the unit 'e' to /app/outputs/mulliken_charges.json.

## Assets

- β-FeSi₂ crystal structure (Dusausoy et al., Acta Cryst. B27 (1971) 1209): 10.1107/S0567740871002577
- Open-source quantum chemistry package supporting 6-311G(d) basis set and Mulliken population analysis

## Workflow steps

### Step 1: Build cluster models
- Role: process
- Action: From the β-FeSi₂ crystal structure, extract all atoms within a radius of 0.51 nm around a central Si site to form the Fe₁₅Si₃₀ cluster. For the doped cluster, replace the central Si atom by C to obtain CFe₁₅Si₂₉. Output the atomic coordinates in a format suitable for the chosen quantum chemistry code.
- Evidence: `/app/outputs/cluster_coordinates.txt`

### Step 2: Run DFT calculation on clusters
- Role: process
- Action: Perform a self-consistent DFT calculation on each of the two clusters using a quantum chemistry package with the 6-311G(d) basis set and a standard exchange-correlation functional (e.g., B3LYP). Save the output for charge analysis.
- Evidence: `/app/outputs/dft_output.log`

### Step 3: Extract Mulliken charges
- Role: scored (load-bearing)
- Action: Compute Mulliken population charges for the central atom in each cluster (C in CFe₁₅Si₂₉, Si in Fe₁₅Si₃₀) from the DFT wavefunction. Write the two charges and a unit string to /app/outputs/mulliken_charges.json.
- Output file: `/app/outputs/mulliken_charges.json`
- Format: json
- Contract: { "charge_C": <float>, "charge_Si": <float>, "unit": "e" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mulliken_charges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mulliken_charges.json
- path: `/app/outputs/mulliken_charges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken atomic charges of the central atom in the C-doped and reference Si-centered clusters, in units of electron charge.
- schema:
  - `type`: object
  - `required`:
    - `charge_C`: float
    - `charge_Si`: float
    - `unit`: string (always 'e')
  - `units`:
    - `charge_C`: e
    - `charge_Si`: e

Notes: The hidden reference values are obtained from the original paper. The checker verifies that both charges fall within a hidden tolerance and that charge_C < charge_Si, consistent with the electronegativity argument.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mulliken_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "charge_C": "float",
          "charge_Si": "float",
          "unit": "string (always 'e')"
        },
        "units": {
          "charge_C": "e",
          "charge_Si": "e"
        }
      },
      "description": "Mulliken atomic charges of the central atom in the C-doped and reference Si-centered clusters, in units of electron charge."
    }
  ],
  "notes": "The hidden reference values are obtained from the original paper. The checker verifies that both charges fall within a hidden tolerance and that charge_C < charge_Si, consistent with the electronegativity argument."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/mulliken_charges.json and compare the charge values to reference values from the original study. The comparison uses a tolerance appropriate for independent DFT implementations to account for differences in functional, basis set, and code choice. The verifier also confirms that all required workflow steps have produced their evidence artifacts. Your final reward is based on the accuracy of the reported charges; simply writing plausible numbers without executing the DFT calculations will not satisfy the verification.
