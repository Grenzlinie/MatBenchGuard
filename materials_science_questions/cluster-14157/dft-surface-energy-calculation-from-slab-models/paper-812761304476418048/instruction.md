# DFT Hydrogen Adsorption Free Energies on Pt and Pt₃Sn Surfaces

## Problem background
Photocatalytic water splitting is a promising pathway for solar hydrogen production. Noble-metal cocatalysts loaded onto semiconductor photocatalysts can significantly enhance hydrogen evolution rates. Alloying platinum with tin and engineering the exposed crystal facets of the cocatalyst nanoparticles are strategies to improve performance. Density-functional theory (DFT) calculations of hydrogen adsorption free energies on different surface terminations provide thermodynamic insight into facet-dependent activity. In this task, you will compute the Gibbs free energy of hydrogen adsorption (ΔG_H*) on four relevant surfaces: Pt(100), Pt(110), Pt₃Sn(100), and Pt₃Sn(110).

## Approach
The calculation starts by optimizing the bulk lattice constants of fcc Pt and the intermetallic Pt₃Sn (simple cubic, space group Pm-3m) using plane-wave DFT with the GGA-PBE exchange-correlation functional and PAW pseudopotentials. A plane-wave cutoff energy of 400 eV must be used for all calculations. From the optimized bulk structures, six-layer p(2×2) slab models with 14 Å vacuum are built for each of the four surfaces. The top four layers are relaxed while the bottom two are fixed at bulk positions. For slab calculations on the (100) facets a 4×4×1 Monkhorst-Pack k-point grid is employed, while for the (110) facets a 3×4×1 grid is used. A single hydrogen atom is then placed at the most stable adsorption site on each relaxed slab, and the H atom together with the top layers are re-relaxed; the total energy of an isolated H₂ molecule is also computed. The hydrogen adsorption energy ΔE_H* is obtained from the energy differences, and the Gibbs free energy ΔG_H* is calculated by adding zero-point energy and entropy corrections at T=298 K and pH=0.

## Reproduction target
Using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO or GPAW) with the GGA-PBE functional and PAW pseudopotentials, compute the Gibbs free energy of hydrogen adsorption ΔG_H* on the Pt(100), Pt(110), Pt₃Sn(100), and Pt₃Sn(110) surfaces. Report the four ΔG_H* values in electron-volts and list the surface labels in order of increasing absolute |ΔG_H*| (most thermodynamically favorable first). The result must be saved as `/app/outputs/dG_results.json` with the exact structure shown in the output contract.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org/
- SSSP efficiency PAW pseudopotentials for Pt and Sn: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk lattice optimization of Pt and Pt₃Sn
- Role: process
- Action: Optimize the bulk lattice constants of fcc Pt and Pt₃Sn using DFT with the GGA-PBE functional and PAW pseudopotentials. The Pt₃Sn structure is a simple cubic cell with space group Pm-3m. Use a plane-wave cutoff energy of 400 eV.

### Step 2: Simulated XRD of Pt and Pt₃Sn
- Role: process
- Action: Using the optimized bulk structures, compute powder X-ray diffraction patterns with Cu-Kα radiation (λ = 1.5406 Å) to obtain lists of (2θ, intensity) peaks for both materials.

### Step 3: Slab model construction and relaxation
- Role: process
- Action: Build six-layer p(2×2) slabs for Pt(100), Pt(110), Pt₃Sn(100), and Pt₃Sn(110) using the optimized bulk lattice parameters, with 14 Å vacuum. Relax the top four layers while fixing the bottom two at bulk positions. Use the same functional, pseudopotentials, and 400 eV plane-wave cutoff as for the bulk. For the (100) facets use a Monkhorst-Pack k-point grid of 4×4×1; for the (110) facets use 3×4×1.

### Step 4: Hydrogen adsorption energy calculations
- Role: process
- Action: For each relaxed slab, place a single H atom at the most stable adsorption site (top, bridge, or hollow) and relax the H position together with the top four layers. Also compute the total energy of an isolated H₂ molecule in a periodic box. Calculate the adsorption energy ΔE_H* = E(slab+H*) − E(slab) − ½ E(H₂).

### Step 5: HER free energy diagram computation
- Role: scored (load-bearing)
- Action: From the most stable ΔE_H* site on each surface, compute the Gibbs free energy of hydrogen adsorption according to the formula
  ΔG_H* = ΔE_H* + ΔZPE − TΔS − ΔG_pH,
  where ΔG_pH = kT ln(10) × pH.
  Use T = 298 K and pH = 0. Include zero-point energy and entropy corrections as described in the supporting information of the paper (vibrational frequencies, standard gas-phase entropy of H₂). Report the four ΔG_H* values (in eV) and their ordering from smallest to largest absolute magnitude.
- Output file: `/app/outputs/dG_results.json`
- Format: json
- Contract: {
  "Pt_100_dG": float (eV),
  "Pt_110_dG": float (eV),
  "Pt3Sn_100_dG": float (eV),
  "Pt3Sn_110_dG": float (eV),
  "ordering": [string] sorted from smallest to largest |ΔG_H*| (most favorable first)
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dG_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dG_results.json
- path: `/app/outputs/dG_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The Gibbs free energies of hydrogen adsorption on the four surfaces and their ordering by absolute magnitude. The checker verifies that all values are within a physically plausible range and that the ordering matches the expected theoretical trend. Absolute values may differ from the original paper due to implementation differences; only the relative ordering is scored.
- schema:
  - `type`: object
  - `properties`:
    - `Pt_100_dG`:
      - `type`: number
      - `description`: ΔG_H* on Pt(100) in eV
    - `Pt_110_dG`:
      - `type`: number
      - `description`: ΔG_H* on Pt(110) in eV
    - `Pt3Sn_100_dG`:
      - `type`: number
      - `description`: ΔG_H* on Pt3Sn(100) in eV
    - `Pt3Sn_110_dG`:
      - `type`: number
      - `description`: ΔG_H* on Pt3Sn(110) in eV
    - `ordering`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: Surface labels ordered from smallest to largest |ΔG_H*| (most favorable first).
  - `required`: `Pt_100_dG`, `Pt_110_dG`, `Pt3Sn_100_dG`, `Pt3Sn_110_dG`, `ordering`

Notes: The workflow follows the DFT protocol described in the approach. The final scored artifact is the free energy and ordering. The checker uses structural audit: values must lie in a reasonable range, and the ordering must satisfy the expected trend. The load-bearing step_05 depends on all prior process steps, so they cannot be bypassed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dG_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "Pt_100_dG": {
            "type": "number",
            "description": "ΔG_H* on Pt(100) in eV"
          },
          "Pt_110_dG": {
            "type": "number",
            "description": "ΔG_H* on Pt(110) in eV"
          },
          "Pt3Sn_100_dG": {
            "type": "number",
            "description": "ΔG_H* on Pt3Sn(100) in eV"
          },
          "Pt3Sn_110_dG": {
            "type": "number",
            "description": "ΔG_H* on Pt3Sn(110) in eV"
          },
          "ordering": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Surface labels ordered from smallest to largest |ΔG_H*| (most favorable first)."
          }
        },
        "required": [
          "Pt_100_dG",
          "Pt_110_dG",
          "Pt3Sn_100_dG",
          "Pt3Sn_110_dG",
          "ordering"
        ]
      },
      "description": "The Gibbs free energies of hydrogen adsorption on the four surfaces and their ordering by absolute magnitude. The checker verifies that all values are within a physically plausible range and that the ordering matches the expected theoretical trend. Absolute values may differ from the original paper due to implementation differences; only the relative ordering is scored."
    }
  ],
  "notes": "The workflow follows the DFT protocol described in the approach. The final scored artifact is the free energy and ordering. The checker uses structural audit: values must lie in a reasonable range, and the ordering must satisfy the expected trend. The load-bearing step_05 depends on all prior process steps, so they cannot be bypassed."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/dG_results.json` file and compares its contents against a hidden reference. It checks the ΔG_H* values, their relative ordering, and physical plausibility using numerical tolerances that are not disclosed. The reward is a weighted sum over all scored artifacts; for this task only the final free-energy step is scored. A correct computation earns the highest reward; a submission that merely guesses numbers without a genuine DFT pipeline may score low. The output file must be present and well-formed to be considered.