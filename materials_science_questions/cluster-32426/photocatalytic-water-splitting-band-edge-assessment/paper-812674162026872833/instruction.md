# O-1-P Heterostructure Photocatalytic Properties Assessment

## Problem background
Black phosphorus (BP) is a promising two-dimensional semiconductor with tunable direct band gap and high carrier mobility, but it degrades rapidly under ambient conditions, limiting its use in photocatalytic water splitting. Encapsulating BP with atomically thin phosphorus oxide (P4O2) layers can improve stability, while the heterostructure may retain beneficial electronic properties. The O-1-P configuration—a P4O2/BP/P4O2 sandwich with oxygen-rich and phosphorus-rich surfaces exposed—is of particular interest because its asymmetric surfaces create an intrinsic electric field (IEF) that can shift band edges and enhance solar-to-hydrogen efficiency. The key question is what electronic and photocatalytic properties this structure exhibits when computed from first principles.

## Approach
Construct the O-1-P heterostructure as a 2×2 supercell sandwich: one monolayer of P4O2 with the oxygen-rich surface outward, one monolayer of P4O2 with the phosphorus-rich surface outward, and a single BP layer in between. Use first-principles density functional theory (DFT) and many-body perturbation theory to compute its properties. Geometry optimization is performed with the PBE-D3 functional to account for van der Waals interactions. The electronic structure is obtained with the HSE06 hybrid functional to give a reliable band gap (direct at Γ). GW quasiparticle corrections (G0W0) are then applied to the HSE06 wavefunctions to obtain the quasiparticle direct band gap. The exciton binding energy is estimated from the GW gap using a scaling relation. Band edge alignment is determined by computing the planar-averaged electrostatic potential across the heterostructure; the vacuum level difference between the two surfaces (ΔΦ) quantifies the intrinsic electric field and is used to position the conduction and valence band edges relative to each surface's vacuum level. Carrier mobility is calculated via deformation potential theory: the elastic modulus and deformation potential constant are derived from DFT, then the mobility formula is applied at 300 K. Finally, the solar-to-hydrogen (STH) efficiency is calculated from the band gap, the overpotential enhancement from ΔΦ, and the AM1.5 solar spectrum. The workflow produces a single JSON file containing the final computed properties.

## Reproduction target
Compute the following properties of the O-1-P heterostructure and write them to `/app/outputs/o1p_properties.json`: (1) the direct HSE06 band gap (eV), (2) the exciton binding energy from GW (eV), (3) the conduction band minimum (CBM) and valence band maximum (VBM) energies relative to the vacuum level on the oxygen-rich surface (eV), (4) the CBM and VBM energies relative to the vacuum level on the phosphorus-rich surface (eV), (5) the hole mobility along the Y direction (cm² V⁻¹ s⁻¹), and (6) the solar-to-hydrogen efficiency (%). The JSON must contain exactly these keys: `band_gap_hse06`, `exciton_binding_energy`, `CBM_oxygen_vacuum`, `VBM_oxygen_vacuum`, `CBM_phosphorus_vacuum`, `VBM_phosphorus_vacuum`, `hole_mobility_Y`, `STH_efficiency`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Yambo: https://www.yambo-code.eu/
- SSSP pseudopotentials (efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare O-1-P structure
- Role: process
- Action: Construct the O-1-P heterostructure: a 2×2 supercell sandwich consisting of a monolayer P4O2 with oxygen-rich surface exposed on top, a monolayer P4O2 with phosphorus-rich surface exposed on bottom, and a single black phosphorus layer in between. Use known lattice parameters for P4O2 and BP from the literature to build the initial geometry.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: Structural optimization (PBE-D3)
- Role: process
- Action: Perform DFT geometry relaxation with the PBE-D3 functional using Quantum ESPRESSO. Relax atomic positions and cell parameters until forces are converged.
- Evidence: `/app/outputs/qe_optimization.out`

### Step 3: HSE06 band gap calculation
- Role: process
- Action: Using the optimized geometry, perform an HSE06 band structure calculation with Quantum ESPRESSO to determine the direct band gap at the Γ point (in eV).
- Evidence: `/app/outputs/hse06_band_gap.log`

### Step 4: GW quasiparticle gap and exciton binding energy
- Role: process
- Action: Perform a G₀W₀ calculation using Yambo on the HSE06 wavefunctions to obtain the quasiparticle direct band gap (E_g,GW^d). Compute the exciton binding energy as E_b = 0.25 * E_g,GW^d.
- Evidence: `/app/outputs/gw_exciton.log`

### Step 5: Band edge alignment and vacuum level evaluation
- Role: process
- Action: Calculate the planar-averaged electrostatic potential of the O-1-P system to determine vacuum levels on the oxygen-rich and phosphorus-rich surfaces. Align the HSE06 CBM and VBM to these vacuum levels, accounting for the intrinsic electric field (vacuum level difference ΔΦ). Report CBM and VBM energies relative to each vacuum level.
- Evidence: `/app/outputs/band_edges.txt`

### Step 6: Hole mobility calculation
- Role: process
- Action: Compute the hole mobility along the Y direction using deformation potential theory. Obtain the elastic modulus C_2D and deformation potential constant from DFT calculations on the optimized O-1-P structure, then apply the mobility formula at 300 K.
- Evidence: `/app/outputs/mobility_Y.txt`

### Step 7: Solar-to-hydrogen efficiency calculation
- Role: process
- Action: Calculate the STH efficiency using the method described in the paper, based on the band gap, overpotential enhancement from the intrinsic electric field (ΔΦ), and the AM1.5 solar spectrum.
- Evidence: `/app/outputs/sth_efficiency.log`

### Step 8: Compile final properties
- Role: scored (load-bearing)
- Action: Assemble all computed quantities into a single JSON file.
- Output file: `/app/outputs/o1p_properties.json`
- Format: json
- Contract: JSON object with numeric fields: band_gap_hse06 (eV), exciton_binding_energy (eV), CBM_oxygen_vacuum (eV), VBM_oxygen_vacuum (eV), CBM_phosphorus_vacuum (eV), VBM_phosphorus_vacuum (eV), hole_mobility_Y (cm^2 V^{-1} s^{-1}), STH_efficiency (%)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/o1p_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### o1p_properties.json
- path: `/app/outputs/o1p_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduced key properties of the O-1-P heterostructure: HSE06 band gap, exciton binding energy, band edge alignment on both surfaces, hole mobility along Y, and solar-to-hydrogen efficiency.
- schema:
  - `type`: object
  - `required`: `band_gap_hse06`, `exciton_binding_energy`, `CBM_oxygen_vacuum`, `VBM_oxygen_vacuum`, `CBM_phosphorus_vacuum`, `VBM_phosphorus_vacuum`, `hole_mobility_Y`, `STH_efficiency`

Notes: The reproduction is scoped to the champion candidate O-1-P, excluding the full triple screening over 20 structures and other supporting calculations, as permitted by the taskability scope. The agent must run the full DFT+GW workflow; all required codes and pseudopotentials are publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "o1p_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_hse06",
          "exciton_binding_energy",
          "CBM_oxygen_vacuum",
          "VBM_oxygen_vacuum",
          "CBM_phosphorus_vacuum",
          "VBM_phosphorus_vacuum",
          "hole_mobility_Y",
          "STH_efficiency"
        ]
      },
      "description": "Reproduced key properties of the O-1-P heterostructure: HSE06 band gap, exciton binding energy, band edge alignment on both surfaces, hole mobility along Y, and solar-to-hydrogen efficiency."
    }
  ],
  "notes": "The reproduction is scoped to the champion candidate O-1-P, excluding the full triple screening over 20 structures and other supporting calculations, as permitted by the taskability scope. The agent must run the full DFT+GW workflow; all required codes and pseudopotentials are publicly available."
}
```

## How you are scored
A hidden verifier will read the `/app/outputs/o1p_properties.json` file and compare each reported value to reference expectations. The overall reward is computed from the accuracy of all fields combined. Simply outputting plausible numbers is not sufficient; you must execute the full computational workflow to obtain the values from first-principles calculations.
