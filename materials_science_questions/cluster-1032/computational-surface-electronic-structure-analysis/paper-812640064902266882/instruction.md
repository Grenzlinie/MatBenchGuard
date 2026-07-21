# Monolayer Electronic Band Structure via All-Numerical LCAO

## Problem background
In transition metals, breaking the bulk translational symmetry at a surface alters the electronic structure, especially the d-electrons. Understanding how the descent in symmetry from the bulk (O_h) to the surface (C_4v) splits and reorders the d-orbitals is fundamental for interpreting surface-sensitive spectroscopies such as photoemission. The monolayer limit provides an upper bound on these effects and isolates the essential bonding physics.

This task is based on first‑principles all‑numerical linear variational LCAO results for a Cu(001) monolayer. The paper reports the band eigenvalues and splittings at high‑symmetry points of the surface Brillouin zone. Instead of performing the full first‑principles calculation, you are provided with the key energy values extracted from the paper’s band‑structure plot (Fig. 2) in units of electron‑volts (eV). Your job is to convert them to Rydberg (Ry) and write the results in a specified JSON format.

## Approach
The method uses the numerical values read from the paper’s Fig. 2 along the Γ–M direction. The energies are given for the following symmetry‑labeled states:

- Γ1   (s‑like)
- Γ3   (d_xy)
- Γ4   (d_x²−y²)
- Γ5   (doubly degenerate d_xz, d_yz)
- M3   (d_xy)
- M4   (d_x²−y²)
- M5   (d_xz, d_yz)

The two energy splittings that characterise the descent in symmetry are defined as  

```
Δ(Γ25′) = E(Γ5) − E(Γ3)   (splitting of the state derived from bulk Γ25′)
Δ(Γ12)  = E(Γ4) − E(Γ1)   (splitting of the state derived from bulk Γ12)
```

## Reproduction target
Convert the following energy values (in eV) to Rydberg using the conversion factor **1 Ry = 13.605693 eV** and write them into the file `/app/outputs/band_eigenvalues_ry.json`. Use the same symmetry labels as listed below and compute the two splittings directly from the converted Ry energies.

### Provided band energies (eV) from the paper’s Fig. 2
| Label        | Energy (eV) |
|--------------|-------------|
| Γ1_s         | –11.56      |
| Γ3_dxy       |  –9.25      |
| Γ4_dx²−y²    |  –5.99      |
| Γ5_dxz,dyz   |  –7.89      |
| M3_dxy       |  –8.71      |
| M4_dx²−y²    |  –5.71      |
| M5_dxz,dyz   |  –7.62      |

## Assets
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Convert energies and compute splittings
- Role: scored (load‑bearing)
- Action: Read the above eV energies, convert each to Rydberg using the conversion factor `1 Ry = 13.605693 eV`, compute the splittings `Δ(Γ25′) = E(Γ5) − E(Γ3)` and `Δ(Γ12) = E(Γ4) − E(Γ1)`, and write the results to the JSON file `/app/outputs/band_eigenvalues_ry.json`.
- Output file: `/app/outputs/band_eigenvalues_ry.json`
- Format: json
- Contract: {
  "Gamma": {
    "Gamma1_s": "number (Ry)",
    "Gamma3_dxy": "number (Ry)",
    "Gamma4_dx2y2": "number (Ry)",
    "Gamma5_dxz_dyz": "number (Ry)"
  },
  "M": {
    "M3_dxy": "number (Ry)",
    "M4_dx2y2": "number (Ry)",
    "M5_dxz_dyz": "number (Ry)"
  },
  "splittings": {
    "Delta_Gamma25_prime": "number (Ry)",
    "Delta_Gamma12": "number (Ry)"
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_eigenvalues_ry.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_eigenvalues_ry.json
- path: `/app/outputs/band_eigenvalues_ry.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy eigenvalues (in Ry) for the Cu(001) monolayer at Γ and M points, together with the splittings Δ(Γ25′) and Δ(Γ12). The values are obtained by converting the eV energies listed in the instruction using 1 Ry = 13.605693 eV.
- schema:
  - `type`: object
  - `properties`:
    - `Gamma`:
      - `type`: object
      - `properties`:
        - `Gamma1_s`: number (Ry)
        - `Gamma3_dxy`: number (Ry)
        - `Gamma4_dx2y2`: number (Ry)
        - `Gamma5_dxz_dyz`: number (Ry)
      - `required`: `Gamma1_s`, `Gamma3_dxy`, `Gamma4_dx2y2`, `Gamma5_dxz_dyz`
    - `M`:
      - `type`: object
      - `properties`:
        - `M3_dxy`: number (Ry)
        - `M4_dx2y2`: number (Ry)
        - `M5_dxz_dyz`: number (Ry)
      - `required`: `M3_dxy`, `M4_dx2y2`, `M5_dxz_dyz`
    - `splittings`:
      - `type`: object
      - `properties`:
        - `Delta_Gamma25_prime`: number (Ry)
        - `Delta_Gamma12`: number (Ry)
      - `required`: `Delta_Gamma25_prime`, `Delta_Gamma12`
  - `required`: `Gamma`, `M`, `splittings`

Notes: The hidden checker compares the reported eigenvalues and splittings to reference benchmark values (the paper‑reported Cu(001) monolayer band energies) using a result‑level comparison with appropriate absolute tolerances. The agent must derive the Ry values from the eV list given above; the checker does not read or validate any intermediate calculation artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_eigenvalues_ry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Gamma": {
            "type": "object",
            "properties": {
              "Gamma1_s": {"type": "number", "unit": "Ry"},
              "Gamma3_dxy": {"type": "number", "unit": "Ry"},
              "Gamma4_dx2y2": {"type": "number", "unit": "Ry"},
              "Gamma5_dxz_dyz": {"type": "number", "unit": "Ry"}
            },
            "required": ["Gamma1_s", "Gamma3_dxy", "Gamma4_dx2y2", "Gamma5_dxz_dyz"]
          },
          "M": {
            "type": "object",
            "properties": {
              "M3_dxy": {"type": "number", "unit": "Ry"},
              "M4_dx2y2": {"type": "number", "unit": "Ry"},
              "M5_dxz_dyz": {"type": "number", "unit": "Ry"}
            },
            "required": ["M3_dxy", "M4_dx2y2", "M5_dxz_dyz"]
          },
          "splittings": {
            "type": "object",
            "properties": {
              "Delta_Gamma25_prime": {"type": "number", "unit": "Ry"},
              "Delta_Gamma12": {"type": "number", "unit": "Ry"}
            },
            "required": ["Delta_Gamma25_prime", "Delta_Gamma12"]
          }
        },
        "required": ["Gamma", "M", "splittings"]
      },
      "description": "Energy eigenvalues (in Ry) for the Cu(001) monolayer at Γ and M points, together with the splittings Δ(Γ25′) and Δ(Γ12). The values are obtained by converting the eV energies listed in the instruction using 1 Ry = 13.605693 eV."
    }
  ],
  "notes": "The hidden checker compares the reported eigenvalues and splittings to reference benchmark values (the paper‑reported Cu(001) monolayer band energies) using a result‑level comparison with appropriate absolute tolerances. The agent must derive the Ry values from the eV list given above; the checker does not read or validate any intermediate calculation artifacts."
}
```

## How you are scored
A hidden verifier reads the submitted `band_eigenvalues_ry.json` and extracts the energies and splittings. It compares each value to the paper‑reported reference results for the same monolayer, using a tolerance suitable for the numerical conversion method. The verifier also checks that the relative ordering of the energy levels (e.g., which level lies higher or lower at each k‑point) is consistent with the expected pattern derived from the symmetry analysis. The final reward is the weighted sum of the per‑field scores; simple file existence without correct numerical values will not earn credit.