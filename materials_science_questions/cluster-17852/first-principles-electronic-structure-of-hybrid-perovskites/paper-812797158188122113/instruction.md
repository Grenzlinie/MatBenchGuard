# Interface Formation Energy and Band Gap of 2D/3D Perovskite Heterostructures

## Problem background
Organic–inorganic hybrid perovskite solar cells (PSCs) deliver high efficiency but suffer from instability under moisture and oxygen. Layered two-dimensional (2D) perovskites exhibit better stability, while three-dimensional (3D) perovskites offer high absorption and charge transport. 2D/3D perovskite heterostructures aim to combine both advantages, but the interfacial electronic properties — band alignment, band gap, and formation energy — critically determine charge separation and recombination. Understanding how the type of contacting interface (PbI- or I-terminated) modulates these properties is essential for designing stable, high-performance devices.

## Approach
Use density‑functional theory (DFT) at the PBE level with a Grimme D3 van‑der‑Waals correction to construct and relax 1×1 supercells of the 2D BA₂PbI₄ monolayer, the 3D MAPbI₃ slabs with PbI- and I‑terminations, and the two heterostructures (2D/PbI and 2D/I). The in‑plane lattice constant is taken as the average of the relaxed 2D and 3D values. After full atomic relaxation, compute the total energies of each component in the heterostructure lattice and the relaxed vertical interlayer distances. The interface formation energy ΔE is computed as the energy difference between the heterostructure and the sum of the isolated components, normalized by the in‑plane supercell area. Finally, determine the PBE band gaps of the relaxed heterostructures. The comparison of band gaps and formation energies between the two interfaces quantifies their suitability for carrier separation.

## Reproduction target
For both the 2D/PbI and 2D/I heterostructures, compute and report the following six PBE‑level quantities: interface formation energies ΔE (in meV/Å²), relaxed vertical interlayer distances l₁ (2D–PbI) and l₂ (2D–I) (in Å), and band gaps (in eV). The goal is to produce a results.json containing these six values. The relative ordering of the band gaps (I‑interface vs PbI‑interface) and the sign/magnitude of the formation energies provide the decisive comparison.

## Assets

- Quantum ESPRESSO (or another open-source DFT code capable of PBE+vdW-D3): https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE precision) for Pb, I, C, N, H: https://www.materialscloud.org/discover/sssp/table
- Grimme D3 van-der-Waals correction: dftd3 or built-in D3 in Quantum ESPRESSO
- Experimental lattice parameters (used as starting points for DFT relaxation):
  * 2D BA₂PbI₄ monolayer: a = 8.855 Å, b = 8.863 Å, c = 31.207 Å, α = β = γ = 90° (Mitzi, Chem. Mater. 1996, 8, 791)
  * 3D MAPbI₃ bulk: a = 8.855 Å, c = 12.685 Å, α = β = γ = 90° (Leguy et al., Chem. Mater. 2015, 27, 3397)

## Workflow steps

### Step 1: DFT geometry relaxation of isolated components and heterostructures
- Role: process
- Action: Using the provided lattice parameters for 2D BA2PbI4 and 3D MAPbI3, construct 1×1 supercells containing one monolayer of BA2PbI4 and a three-layer MAPbI3 slab for both PbI-terminated and I-terminated surfaces. The in-plane lattice constant is the average of the 2D and 3D values. Run spin-polarised PBE-level DFT calculations with Grimme D3 van-der-Waals correction for: (a) the isolated 2D monolayer in the heterostructure lattice; (b) the isolated 3D slabs (each termination) in the same lattice; (c) the two heterostructure supercells (2D/PbI and 2D/I). Perform full atomic relaxation until forces and energy are converged. Record the final total energies E2D, E3D(PbI), E3D(I), E2D/3D(PbI), E2D/3D(I) and the relaxed vertical interlayer distances l1 (2D-PbI) and l2 (2D-I). Use a plane-wave cutoff and k-point mesh suitable for PBE convergence. A vacuum layer of ≥15 Å along the surface normal must be used.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 2: Compute interface formation energies and band gaps, write results.json
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_01, compute the interface formation energies ΔE for the PbI-terminated and I-terminated heterostructures using ΔE = (E2D + E3D(interface) − E2D/3D(interface)) / S, where S is the in-plane supercell area. Compute the PBE band gaps for the relaxed heterostructures (e.g. from band structure analysis). Write the following six values into /app/outputs/results.json: delta_E_PbI (meV/Å²), delta_E_I (meV/Å²), l1 (Å), l2 (Å), band_gap_PbI (eV), band_gap_I (eV).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_E_PbI": <float, meV/Å²>, "delta_E_I": <float, meV/Å²>, "l1": <float, Å>, "l2": <float, Å>, "band_gap_PbI": <float, eV>, "band_gap_I": <float, eV>}
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
- description: Scored artifact containing the six PBE-level computed properties for the 2D/PbI and 2D/I heterostructures.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_PbI`: float (meV/Å²)
    - `delta_E_I`: float (meV/Å²)
    - `l1`: float (Å)
    - `l2`: float (Å)
    - `band_gap_PbI`: float (eV)
    - `band_gap_I`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `delta_E_PbI`: meV/Å²
    - `delta_E_I`: meV/Å²
    - `l1`: Å
    - `l2`: Å
    - `band_gap_PbI`: eV
    - `band_gap_I`: eV

Notes: The hidden checker compares the submitted numeric values to the paper's reported PBE-level values with appropriate tolerances, and verifies the relative ordering (band_gap_I > band_gap_PbI) and positivity of both formation energies.

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
          "delta_E_PbI": "float (meV/Å²)",
          "delta_E_I": "float (meV/Å²)",
          "l1": "float (Å)",
          "l2": "float (Å)",
          "band_gap_PbI": "float (eV)",
          "band_gap_I": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "delta_E_PbI": "meV/Å²",
          "delta_E_I": "meV/Å²",
          "l1": "Å",
          "l2": "Å",
          "band_gap_PbI": "eV",
          "band_gap_I": "eV"
        }
      },
      "description": "Scored artifact containing the six PBE-level computed properties for the 2D/PbI and 2D/I heterostructures."
    }
  ],
  "notes": "The hidden checker compares the submitted numeric values to the paper's reported PBE-level values with appropriate tolerances, and verifies the relative ordering (band_gap_I > band_gap_PbI) and positivity of both formation energies."
}
```

## How you are scored
A hidden verifier compares the six numeric entries in your submitted results.json against a set of reference values derived from the original study. The comparison uses per‑quantity tolerances that account for differences between DFT codes and pseudopotentials. Additionally, the verifier checks structural constraints: the band gap of the I‑interface heterostructure must be larger than that of the PbI‑interface heterostructure, and both interface formation energies must be positive and small. Each correct value and satisfied constraint contributes to the final score in a weighted fashion. Reporting plausible numbers without performing the required DFT calculations will not pass these checks.
