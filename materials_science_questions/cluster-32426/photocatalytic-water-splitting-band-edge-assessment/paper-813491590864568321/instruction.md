# Two‑Dimensional Phosphorus Oxide Band Edges and Ferroelectric Polarization

## Problem background
Two-dimensional (2D) materials beyond graphene are actively sought for electronic and energy applications. Phosphorene, monolayer black phosphorus, shows promise but degrades rapidly in humid air due to oxidation. Recently, layered phosphorus oxides (PxOy) with higher oxygen content have been synthesized and are more stable under ambient conditions. Among them, P4O4 is predicted to be a direct-gap semiconductor potentially suitable for photocatalytic water splitting, while P2O3 can adopt ferroelectric phases with spontaneous electric polarization. These properties originate from the unique structural motifs of the oxides, which differ fundamentally from the phosphorene backbone. A reliable reproduction of the electronic band gap, effective mass, band-edge alignment relative to water redox potentials, and the ferroelectric polarization is essential to assess the viability of these materials as functional 2D platforms.

## Approach
The computational workflow employs density functional theory (DFT) as implemented in the open-source Quantum ESPRESSO package. The atomic structures are constructed manually from the published bonding descriptions: P4O4‑I features only bridge-type P–O–P motifs with two P–P dimers per primitive cell; P2O3‑I has a honeycomb phosphorus lattice with oxygen atoms buckled out‑of‑plane; P2O3‑II is derived from a similar honeycomb framework but with in‑plane displacements of the oxygen atoms that break inversion symmetry. The monolayer models are built with the Atomic Simulation Environment (ASE). Once the geometries are prepared, a series of DFT calculations are performed: (i) a hybrid‑functional (HSE06) band‑structure calculation for P4O4‑I to obtain the direct band gap and the vacuum‑referenced band‑edge positions, (ii) a local‑density approximation (LDA) band‑structure calculation to extract the electron effective mass from the curvature near the Γ point, and (iii) Berry‑phase polarization calculations within LDA or PBE for the ferroelectric P2O3 phases to determine the magnitude and direction of the spontaneous polarization. The vacuum alignment is achieved by evaluating the planar‑averaged electrostatic potential of the monolayer slab. The target quantities are reported in four separate JSON files for downstream verification.

## Reproduction target
Produce the following results from the DFT calculations:
- The direct band gap (in eV) of the P4O4‑I monolayer computed with the HSE06 functional, together with a flag indicating that the transition is direct at the Γ point.
- The electron effective mass (in units of the free‑electron mass m₀) of P4O4‑I obtained from the LDA band dispersion near Γ.
- The vacuum‑referenced conduction‑band minimum (CBM) and valence‑band maximum (VBM) energies (in eV) for the HSE06 P4O4‑I calculation, as well as the standard hydrogen‑evolution (HER) and oxygen‑evolution (OER) potentials at pH = 0 (referenced to the vacuum level).
- The spontaneous electric polarization magnitudes (in C/m) and the direction (out‑of‑plane or in‑plane) for the P2O3‑I and P2O3‑II ferroelectric phases, computed with the Berry‑phase method using LDA or PBE.
All outputs must be written to the specified JSON files under `/app/outputs`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- ASE (Atomic Simulation Environment): https://gitlab.com/ase/ase

## Workflow steps

### Step 1: Build Atomic Structures
- Role: process
- Action: Construct the monolayer atomic models of P4O4‑I (bridge‑type P–O–P motifs, two P–P dimers per cell, thickness <3.2 Å), P2O3‑I (honeycomb P lattice, O atoms buckled out‑of‑plane), and P2O3‑II (in‑plane displaced O atoms) using ASE from the published structural descriptions, and save them in a format suitable for Quantum ESPRESSO.
- Evidence: `/app/outputs/structures_p4o4_I.poscar, structures_p2o3_I.poscar, structures_p2o3_II.poscar`

### Step 2: HSE06 Band Gap of P4O4‑I
- Role: scored
- Action: Perform a HSE06 hybrid‑functional band structure calculation for the P4O4‑I monolayer and determine the direct band gap at the Γ point. Output the gap value (eV) and a flag indicating that it is direct.
- Output file: `/app/outputs/step_01_p4o4_band_gap.json`
- Format: json
- Contract: {"method": "string", "functional": "HSE06", "band_gap": "float (eV)", "direct": "bool"}
- Scoring: scored by hidden verifier

### Step 3: LDA Electron Effective Mass of P4O4‑I
- Role: scored (load-bearing)
- Action: Perform LDA geometry optimisation and band structure calculation for P4O4‑I. From the band dispersion near the Γ point, extract the electron effective mass in units of free electron mass and output the result.
- Output file: `/app/outputs/step_02_p4o4_effective_mass.json`
- Format: json
- Contract: {"method": "string", "functional": "LDA", "carrier_type": "electron", "effective_mass": "float (units: m₀)", "reference": "free electron mass"}
- Scoring: scored by hidden verifier

### Step 4: Vacuum‑Referenced Band Edges of P4O4‑I
- Role: scored
- Action: From the HSE06 calculation, align the band edges to the vacuum level (e.g., by planar‑averaged electrostatic potential) and output the VBM and CBM energies relative to vacuum, together with the standard hydrogen‑evolution (HER) and oxygen‑evolution (OER) potentials at pH = 0.
- Output file: `/app/outputs/step_03_p4o4_band_edges.json`
- Format: json
- Contract: {"CBM_vs_vacuum": "float (eV)", "VBM_vs_vacuum": "float (eV)", "HER_potential": "float (eV)", "OER_potential": "float (eV)", "pH": 0}
- Scoring: scored by hidden verifier

### Step 5: Berry‑Phase Polarization of P2O3‑I and P2O3‑II
- Role: scored (load-bearing)
- Action: Using a suitable functional (LDA or PBE) and the Berry‑phase method in Quantum ESPRESSO, compute the spontaneous electric polarisation vectors for the ferroelectric structures P2O3‑I and P2O3‑II. Output the magnitude (C/m) and the direction (out‑of‑plane / in‑plane) for each.
- Output file: `/app/outputs/step_04_p2o3_polarization.json`
- Format: json
- Contract: [{"structure": "P2O3‑I", "polarization": "float (C/m)", "direction": "out‑of‑plane"}, {"structure": "P2O3‑II", "polarization": "float (C/m)", "direction": "in‑plane"}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_p4o4_band_gap.json`
- `/app/outputs/step_02_p4o4_effective_mass.json`
- `/app/outputs/step_03_p4o4_band_edges.json`
- `/app/outputs/step_04_p2o3_polarization.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_p4o4_band_gap.json
- path: `/app/outputs/step_01_p4o4_band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: HSE06 direct band gap of P4O4‑I.
- schema:
  - `type`: object
  - `required`:
    - `method`: string
    - `functional`: string
    - `band_gap`: float (eV)
    - `direct`: boolean

### step_02_p4o4_effective_mass.json
- path: `/app/outputs/step_02_p4o4_effective_mass.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: LDA electron effective mass of P4O4‑I.
- schema:
  - `type`: object
  - `required`:
    - `method`: string
    - `functional`: string
    - `carrier_type`: string
    - `effective_mass`: float (units: m₀)
    - `reference`: string

### step_03_p4o4_band_edges.json
- path: `/app/outputs/step_03_p4o4_band_edges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Vacuum‑referenced VBM and CBM energies of P4O4‑I.
- schema:
  - `type`: object
  - `required`:
    - `CBM_vs_vacuum`: float (eV)
    - `VBM_vs_vacuum`: float (eV)
    - `HER_potential`: float (eV)
    - `OER_potential`: float (eV)
    - `pH`: 0

### step_04_p2o3_polarization.json
- path: `/app/outputs/step_04_p2o3_polarization.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spontaneous polarisation of the P2O3 ferroelectric phases.
- schema:
  - `type`: array
  - `items`:
    - `structure`: string
    - `polarization`: float (C/m)
    - `direction`: string

Notes: All output files contain computed quantities compared against hidden reference values derived from the paper. The HER and OER potentials are at pH=0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_p4o4_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "method": "string",
          "functional": "string",
          "band_gap": "float (eV)",
          "direct": "boolean"
        }
      },
      "description": "HSE06 direct band gap of P4O4‑I."
    },
    {
      "file": "step_02_p4o4_effective_mass.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "method": "string",
          "functional": "string",
          "carrier_type": "string",
          "effective_mass": "float (units: m₀)",
          "reference": "string"
        }
      },
      "description": "LDA electron effective mass of P4O4‑I."
    },
    {
      "file": "step_03_p4o4_band_edges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CBM_vs_vacuum": "float (eV)",
          "VBM_vs_vacuum": "float (eV)",
          "HER_potential": "float (eV)",
          "OER_potential": "float (eV)",
          "pH": 0
        }
      },
      "description": "Vacuum‑referenced VBM and CBM energies of P4O4‑I."
    },
    {
      "file": "step_04_p2o3_polarization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "structure": "string",
          "polarization": "float (C/m)",
          "direction": "string"
        }
      },
      "description": "Spontaneous polarisation of the P2O3 ferroelectric phases."
    }
  ],
  "notes": "All output files contain computed quantities compared against hidden reference values derived from the paper. The HER and OER potentials are at pH=0."
}
```

## How you are scored
A hidden verifier independently reads each of your output JSON files and compares the reported quantities to reference benchmarks. The comparisons use tolerance windows appropriate for the method (different functionals or implementations may yield small systematic shifts). For directional quantities where a better value is physically meaningful (e.g., a larger band gap would indicate poorer light absorption for water splitting), the score is monotonic in quality: meeting or exceeding the reference target earns full credit, and credit decreases only as the result deviates unfavorably. Each step carries a weight; the weights are combined into a final reward between 0 and 1. To obtain a high score you must execute the workflow honestly and report the computed values—simply supplying approximate or guessed numbers is insufficient.
