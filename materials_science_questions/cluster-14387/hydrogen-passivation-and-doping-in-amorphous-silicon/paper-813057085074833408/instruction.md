# Surface free energy and critical size of Si(111) 7x7 DAS domain via cell model

## Problem background
The Si(111) surface undergoes a reconstruction into a complex 7×7 dimer‑adatom‑stacking‑fault (DAS) structure. A key open question is what stabilizes a small DAS domain during its growth. A theoretical model based on the energies of structural elements (stacking‑fault/dimer units and corner‑holes) and the configurational entropy of adatoms in the unreconstructed '1×1' phase can predict the surface free energy change associated with forming a domain of a given size. The goal is to compute this free energy as the number of faulted half‑unit cells increases, and to determine the smallest domain size that becomes thermodynamically stable (the critical nucleus size).

## Approach
Use a cell model that treats the Si(111) surface as half‑cells. The formation energy of a DAS domain, E_DS, is built from element contributions: each faulted half contributes a base energy ε0 = -3.91 eV (stacking‑fault and dimers); each corner‑hole of type CH1, CH2, or CH3 contributes an energy of 1.49 eV, 1.84 eV, or 2.71 eV, respectively. The configurational entropy of the '1×1' phase is modeled by random placement of adatoms on T₄ sites with a density of 0.25 and nearest‑neighbour exclusion, yielding an entropy per T₄ site of s₀ = 0.249 k_B. The entropy contribution to the free energy is thus F_{1×1} = -0.249 * k_B * T * n_f, where n_f is the number of T₄ sites lost when the DAS domain forms. The net surface free energy change relative to the '1×1' phase is F_DAS = E_DS − F_{1×1}. By computing F_DAS for a series of domain configurations with m_F = 1..10 faulted halves at T = 653 K, one can find the critical size where F_DAS becomes negative. The necessary counts of CH1, CH2, CH3 and n_f for each m_F are provided in the workflow step.

## Reproduction target
Implement the cell model at T = 653 K (k_B T = 0.05627 eV). For each domain size m_F = 1 to 10, use the given element energies, the entropy constant s₀ = 0.249 k_B, and the provided counts of corner‑hole types and T₄ site counts (n_f) to compute E_DS, F_{1×1}, and F_DAS. Write the results to a JSON file and identify the critical domain size: the smallest m_F for which F_DAS < 0.

## Assets

- Vanderbilt (1987) Formation energies of DAS elements: https://doi.org/10.1103/PhysRevB.36.6209
- Kato et al. (1998) Cell model and configurational entropy: https://doi.org/10.1016/S0039-6028(98)00413-0

## Workflow steps

### Step 1: Compute DAS domain surface free energy
- Role: scored (load-bearing)
- Action: Using the provided element formation energies (ε0 = -3.91 eV, c1 = 1.49 eV, c2 = 1.84 eV, c = 2.71 eV), the configurational entropy constant (s0 = 0.249 k_B), and the table of corner-hole counts (CH1, CH2, CH3) and number of replaced T4 sites (n_f) for each domain size m_F from 1 to 10 shown below, compute the DAS formation energy E_DS for each m_F, compute the entropy contribution F_{1×1} = -s0 * k_B * T * n_f with T = 653 K (k_B T = 0.05627 eV), and compute the surface free energy difference F_DAS = E_DS - F_{1×1}. Write the results as a JSON array of objects, one per m_F.

**Corner‑hole counts and n_f (extracted from Fig. 4 of the paper):**

| m_F | CH1 | CH2 | CH3 | n_f    |
|-----|-----|-----|-----|--------|
| 1   | 3   | 0   | 0   | 60.5   |
| 2   | 0   | 2   | 1   | 66.5   |
| 3   | 1   | 1   | 2   | 127.0  |
| 4   | 2   | 2   | 2   | 111.5  |
| 5   | 2   | 3   | 2   | 188.0  |
| 6   | 2   | 4   | 2   | 250.0  |
| 7   | 2   | 5   | 2   | 305.0  |
| 8   | 2   | 6   | 2   | 345.5  |
| 9   | 2   | 7   | 2   | 372.0  |
| 10  | 2   | 8   | 2   | 391.0  |
- Output file: `/app/outputs/dass_domain_energies.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"m_F":{"type":"integer"},"E_DS_eV":{"type":"number"},"n_f":{"type":"number"},"F_DAS_eV":{"type":"number"}},"required":["m_F","E_DS_eV","n_f","F_DAS_eV"]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dass_domain_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dass_domain_energies.json
- path: `/app/outputs/dass_domain_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed surface free energy differences for DAS domain sizes m_F=1..10 at T=653 K. The checker recomputes F_DAS from E_DS and n_f, verifies that the absolute deviation is within tolerance, and identifies the critical nucleation size.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `m_F`:
        - `type`: integer
      - `E_DS_eV`:
        - `type`: number
      - `n_f`:
        - `type`: number
      - `F_DAS_eV`:
        - `type`: number
    - `required`: `m_F`, `E_DS_eV`, `n_f`, `F_DAS_eV`

Notes: The element energies, entropy constant, and configuration counts (CH1, CH2, CH3, n_f) for each m_F are provided in the instruction. The agent implements the cell model exactly as described and writes the resulting table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dass_domain_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "m_F": {
              "type": "integer"
            },
            "E_DS_eV": {
              "type": "number"
            },
            "n_f": {
              "type": "number"
            },
            "F_DAS_eV": {
              "type": "number"
            }
          },
          "required": [
            "m_F",
            "E_DS_eV",
            "n_f",
            "F_DAS_eV"
          ]
        }
      },
      "description": "Computed surface free energy differences for DAS domain sizes m_F=1..10 at T=653 K. The checker recomputes F_DAS from E_DS and n_f, verifies that the absolute deviation is within tolerance, and identifies the critical nucleation size."
    }
  ],
  "notes": "The element energies, entropy constant, and configuration counts (CH1, CH2, CH3, n_f) for each m_F are provided in the instruction. The agent implements the cell model exactly as described and writes the resulting table."
}
```

## How you are scored
A hidden verifier will read your output JSON and independently recompute F_DAS from your reported E_DS and n_f using the relation F_DAS = E_DS + 0.249 × k_B T × n_f (since F_{1×1} is already subtracted in your output). It checks that the recomputed values agree with your reported F_DAS to within an allowed tolerance. It also determines the critical m_F from your data and compares it with the expected result. The final reward is based on how well your computed F_DAS values match the reference and whether the critical size is correctly identified. Simply reporting a number without a correct underlying computation will fail the verification.
