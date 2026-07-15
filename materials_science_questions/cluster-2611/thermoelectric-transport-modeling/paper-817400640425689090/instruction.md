# Thermoelectric Transport Modeling for 2D Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃

## Problem background
Thermoelectric (TE) materials can convert waste heat into electricity; their efficiency is measured by the dimensionless figure of merit ZT = S²σT/(κₑ+κₗ), which depends on the Seebeck coefficient S, electrical conductivity σ, and thermal conductivities. The power factor PF = S²σ is a key quantity to maximize. Certain two-dimensional materials, such as single and double quintuple-layer Bi₂Te₃, Bi₂Se₃, and Sb₂Te₃, possess ring-shaped valence band maxima that provide an abrupt increase in conducting channels near the band edge, potentially boosting PF. The exact enhancement depends sensitively on the assumed electron scattering model: constant mean free path (cmfp), constant relaxation time (crt), or scattering rates proportional to the density of states (DOS model). This task investigates the thermoelectric performance of these six materials by computing the electronic structure from first principles and evaluating transport under each scattering approximation.

## Approach
Density functional theory (DFT) calculations are performed using the PBE functional with spin-orbit coupling and Grimme-D2 van der Waals corrections, employing experimental in-plane lattice constants. For each material, the Kohn-Sham eigenvalues are obtained on two k-point grids: one for the density of states (DOS) and another, rectangular supercell grid for band counting. From these eigenvalues, the distribution of modes M(E), average velocity V_λ(E), and density of states D(E) are extracted using band counting and tetrahedron integration. For the transport calculations, the DFT band gaps are corrected to known GW values via a scissor shift. The transport distribution Σ(E) is then constructed for three scattering models: cmfp (Σ ∼ M), crt (Σ ∼ M·V_λ), and DOS (Σ ∼ M·V_λ/D). The adjustable scattering parameters (λ₀, τ₀, K₀) are determined by imposing that the average mean free path for backscattering equals 20 nm when the Fermi level lies at the valence band edge. The lattice thermal conductivity is taken as 1.5 W/m·K and the 2D transport quantities are converted to 3D using the film thicknesses. Finally, the Fermi-level-dependent power factor and ZT are computed at 300 K, and the maximum values are recorded for each (material, scattering) pair. For single quintuple-layer materials, the energies of the inner ring, outer ring, and moat features relative to the valence-band edge are identified from the electronic distributions.

## Reproduction target
Compute the peak power factor (in W/m-K²) and peak ZT (dimensionless) at T = 300 K for every combination of material (1QL and 2QL Bi₂Te₃, Bi₂Se₃, Sb₂Te₃) and scattering model (cmfp, crt, dos). For the single quintuple-layer materials, additionally determine the energies (in eV) of the two ring-shaped valence-band maxima and the ring-shaped local minimum (moat) relative to the valence-band edge. Organize all results in the JSON file /app/outputs/te_results.json with one entry per (material, scattering) pair.

## Assets

- Quantum ESPRESSO (DFT package): https://www.quantum-espresso.org/download
- PBE PAW pseudopotentials (Bi, Te, Se, Sb): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT electronic structure calculations
- Role: process
- Action: For each of the six materials (1QL and 2QL Bi₂Te₃, Bi₂Se₃, Sb₂Te₃), perform self-consistent field (SCF) and non-self-consistent (NSCF) DFT calculations using Quantum ESPRESSO with the PBE functional, spin-orbit coupling, Grimme-D2 van der Waals correction, and the specified experimental in-plane lattice constants. Relax atomic coordinates. Compute eigenvalues on the required k-point grids for DOS and band counting.
- Evidence: `/app/outputs/eigenvalues.zip`

### Step 2: Band counting and electronic property extraction
- Role: process
- Action: From the DFT eigenvalues, compute the distribution of modes M(E), average velocity V_λ(E), and density of states D(E) using band counting and tetrahedron integration on the specified k-grids.
- Evidence: `/app/outputs/electronic_properties.json`

### Step 3: Thermoelectric transport calculation and key results
- Role: scored (load-bearing)
- Action: For each material, apply scissor correction to the DFT band gap using the literature GW gaps. Compute the transport distribution, electrical conductivity, Seebeck coefficient, electronic thermal conductivity, power factor, and ZT as functions of Fermi level for three scattering models (constant MFP, constant relaxation time, DOS-scattering). Set scattering parameters such that the average mean free path for backscattering at the band edge equals 20 nm. Use a lattice thermal conductivity of 1.5 W/m-K and convert 2D to 3D units using the given film thicknesses. Record the peak PF and ZT for each (material, scattering) combination. For 1QL materials, determine the energies of the two ring-shaped maxima and the ring-shaped minimum (moat) relative to the valence-band edge. Write all results to te_results.json.
- Output file: `/app/outputs/te_results.json`
- Format: json
- Contract: A JSON array of objects. Each object has keys: 'material' (string, e.g. '1QL Bi2Te3'), 'scattering' (string, one of 'cmfp', 'crt', 'dos'), 'peak_pf' (float, W/m-K²), 'peak_zt' (float, dimensionless), 'fermi_level' (float, eV). For 1QL materials, additional keys: 'inner_ring_energy' (float, eV, energy relative to valence-band edge; null if not applicable), 'outer_ring_energy' (float, eV), 'moat_energy' (float, eV). For 2QL materials, these fields may be null or absent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/te_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### te_results.json
- path: `/app/outputs/te_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Array of objects, one per (material, scattering) pair. Each object reports the peak power factor (peak_pf), peak ZT (peak_zt), and the Fermi level at which they occur. For single quintuple-layer materials, the energies of the inner ring, outer ring, and moat relative to the valence-band edge are additionally provided (may be null for double quintuple-layer materials).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `scattering`, `peak_pf`, `peak_zt`, `fermi_level`
    - `properties`:
      - `material`:
        - `type`: string
      - `scattering`:
        - `type`: string
        - `enum`: `cmfp`, `crt`, `dos`
      - `peak_pf`:
        - `type`: number
        - `unit`: W/m-K²
      - `peak_zt`:
        - `type`: number
        - `unit`: dimensionless
      - `fermi_level`:
        - `type`: number
        - `unit`: eV
      - `inner_ring_energy`:
        - `type`: number
        - `unit`: eV
      - `outer_ring_energy`:
        - `type`: number
        - `unit`: eV
      - `moat_energy`:
        - `type`: number
        - `unit`: eV

Notes: The agent must compute scattering parameters so that the average mean free path for backscattering equals 20 nm at the respective band edge. The checker will compare peak_pf against a hidden lower bound (paper value −15%), peak_zt against a hidden lower bound (paper value −10%), and ring/moat energies within ±0.01 eV of hidden references. Relative ordering of PF across scattering models will also be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "te_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "scattering",
            "peak_pf",
            "peak_zt",
            "fermi_level"
          ],
          "properties": {
            "material": {
              "type": "string"
            },
            "scattering": {
              "type": "string",
              "enum": [
                "cmfp",
                "crt",
                "dos"
              ]
            },
            "peak_pf": {
              "type": "number",
              "unit": "W/m-K²"
            },
            "peak_zt": {
              "type": "number",
              "unit": "dimensionless"
            },
            "fermi_level": {
              "type": "number",
              "unit": "eV"
            },
            "inner_ring_energy": {
              "type": "number",
              "unit": "eV"
            },
            "outer_ring_energy": {
              "type": "number",
              "unit": "eV"
            },
            "moat_energy": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "Array of objects, one per (material, scattering) pair. Each object reports the peak power factor (peak_pf), peak ZT (peak_zt), and the Fermi level at which they occur. For single quintuple-layer materials, the energies of the inner ring, outer ring, and moat relative to the valence-band edge are additionally provided (may be null for double quintuple-layer materials)."
    }
  ],
  "notes": "The agent must compute scattering parameters so that the average mean free path for backscattering equals 20 nm at the respective band edge. The checker will compare peak_pf against a hidden lower bound (paper value −15%), peak_zt against a hidden lower bound (paper value −10%), and ring/moat energies within ±0.01 eV of hidden references. Relative ordering of PF across scattering models will also be verified."
}
```

## How you are scored
A hidden verifier compares your reported results in te_results.json against independently determined reference values (derived from the scientific literature) using appropriate tolerances for each quantity: a relative tolerance for the power factor and ZT, and an absolute tolerance for the ring/moat energies. It also checks that the relative ordering of the peak power factors across the three scattering models matches the known physical outcome for each material. The overall reward is the fraction of all required comparisons that are met. Merely reporting numbers without performing the full DFT and transport calculation will not satisfy the verifier because the process steps (DFT and band counting) produce intermediate evidence that must be internally consistent with the final scored file.
