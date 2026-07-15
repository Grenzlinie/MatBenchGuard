# Defect formation energies in hexagonal BaTiO₃ from first principles

## Problem background
Barium titanate (BaTiO₃) is a perovskite with wide applications. Fe doping stabilizes the hexagonal phase, but the dominant incorporation mechanism is debated. This work uses DFT to compute formation energies of isolated Fe defects and Fe‑vacancy complexes to identify the most stable defect configuration under experimental conditions.

## Approach
Use density functional theory (DFT) calculations to compute defect formation energies in hexagonal BaTiO₃ (h‑BaTiO₃). Construct supercell models for an isolated Fe impurity substituted at a Ti site and for an Fe–V_O complex (Fe substituted at Ti with a nearby oxygen vacancy). Calculate total energies using spin‑polarized GGA+U with a Hubbard correction on Fe 3d states, also for reference compounds (TiO₂, Fe₂O₃, O₂) to derive chemical potentials. Under fixed oxygen chemical potential (air conditions) and Fermi level at the valence band maximum, evaluate the formation energy formula including finite‑size corrections. The output is the formation energies of the two defect configurations, from which their relative stability can be inferred.

## Reproduction target
Compute the formation energies for two defect configurations in h‑BaTiO₃ under air conditions: (1) an isolated Fe defect (electronically compensated) and (2) an Fe–V_O complex (vacancy‑compensated). Report both values in eV as specified in the output contract. The verifier will evaluate a required relative ordering between the two energies and check that the magnitudes lie within a physically plausible range.

## Assets

- host_structure: https://materialsproject.org/materials/mp-7610
- reference_compounds: https://materialsproject.org/
- quantum_espresso: https://www.quantum-espresso.org/
- pseudopotentials: https://www.materialscloud.org/discover/sssp/table/paw

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct 3×3×1 supercell models of h-BaTiO₃ for the pristine host, for an isolated Fe impurity substituted at the Ti(2) site in the +1 charge state (electronically compensated Fe defect), and for an Fe–V_O complex with Fe at Ti(1) and an oxygen vacancy at the U2 position in the +1 charge state (vacancy-compensated complex). Use the hexagonal crystal structure (space group P6₃/mmc, lattice constants a=5.805 Å, c=14.077 Å).
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: DFT total energy calculations
- Role: process
- Action: Perform spin-polarized DFT calculations using the GGA+U method (with Hubbard U correction on Fe 3d states) for the host supercell, the two defect supercells, and the reference compounds TiO₂, Fe₂O₃, and an isolated O₂ molecule. For each structure, carry out geometry relaxation to obtain total energies, and extract the valence band maximum (VBM) of the host supercell.
- Evidence: `/app/outputs/dft_total_energies.json`

### Step 3: Compute formation energies
- Role: scored (load-bearing)
- Action: From the DFT total energies of the host, defect supercells, and reference compounds, compute the oxygen chemical potential under air conditions (Δμ_O = –1.98 eV, with the Fermi level fixed at the valence band maximum ΔE_F = 0). Evaluate the defect formation energies for the isolated Fe defect and the Fe–V_O complex using the standard supercell formation energy formula that includes finite-size corrections (image charge and potential alignment). Report the two formation energies in eV.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"Fe5_Ti2": <float>, "Fe3_VO_U2": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of two defect configurations: Fe⁵⁺ at Ti(2) site (electronically compensated) and Fe³⁺–V_O at U2 configuration (vacancy compensated) evaluated under air conditions.
- schema:
  - `type`: object
  - `required`:
    - `Fe5_Ti2`: number
    - `Fe3_VO_U2`: number
  - `units`:
    - `Fe5_Ti2`: eV
    - `Fe3_VO_U2`: eV

Notes: The checker verifies that Fe5_Ti2 > Fe3_VO_U2 and both values lie in a physically plausible range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Fe5_Ti2": "number",
          "Fe3_VO_U2": "number"
        },
        "units": {
          "Fe5_Ti2": "eV",
          "Fe3_VO_U2": "eV"
        }
      },
      "description": "Formation energies of two defect configurations: Fe⁵⁺ at Ti(2) site (electronically compensated) and Fe³⁺–V_O at U2 configuration (vacancy compensated) evaluated under air conditions."
    }
  ],
  "notes": "The checker verifies that Fe5_Ti2 > Fe3_VO_U2 and both values lie in a physically plausible range."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts submitted at each stage of the workflow. The primary scored artifact is `formation_energies.json`, where the verifier checks that the two formation energies satisfy a required ordering and fall within physically sensible bounds. Intermediate process evidence may also be audited for completeness. The final reward is a weighted combination of scores across all stages; reporting only the paper's numbers without executing the full computational pipeline will not yield a passing score.
