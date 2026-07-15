# DFT Investigation of Half-Metallic Properties in Ti2YZ Heusler Alloys

## Problem background
Half-metallic materials that are 100% spin-polarized at the Fermi level are highly desirable for spintronic applications. A family of Ti₂-based full-Heusler alloys with the Li₂AgSb-type structure has been proposed as potential half-metals. In these compounds the total spin magnetic moment (Mₜ) is predicted to obey a simple Slater–Pauling relation with the total number of valence electrons per unit cell (Zₜ): Mₜ = Zₜ − 18. The presence of the s‑p element Z is thought to be essential for structural stability and for maintaining a minority-spin band gap. This task investigates the half-metallic character of a representative subset of Ti₂YZ (Y = Fe, Co, Ni; Z = Al, Ga, In) alloys by computing their total magnetic moments and minority-spin gaps from first principles, and by testing whether the proposed Slater–Pauling rule holds. The role of the Z atom will be probed by removing it from the lattice, and the sensitivity of the minority gap to lattice constant will be examined.

## Approach
All calculations are performed with spin-polarized density functional theory (DFT) using the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA‑PBE) as implemented in the Quantum ESPRESSO package. The crystal structure is taken as the Li₂AgSb type, with Ti atoms occupying the 4a and 4c Wyckoff positions and the Y (Fe, Co, Ni) and Z (Al) atoms occupying the 4b and 4d positions, respectively. The magnetic ground state is ferromagnetic, and full lattice-constant optimization is carried out for each compound. From the self-consistent charge density, the total spin magnetic moment and the minority-spin band gap (the gap in the density of states around the Fermi level for the minority-spin channel) are extracted. Three comparisons are performed: (i) the properties of Ti₂FeAl, Ti₂CoAl, and Ti₂NiAl are compared to test the Slater–Pauling rule across different valence electron counts; (ii) the Z-atom is removed (a vacant site) in Ti₂Co, and the resulting magnetic moment and minority gap are computed at the equilibrium lattice constant of Ti₂CoAl to assess the impact of the s‑p element; (iii) for Ti₂CoAl only, the minority gap is computed at two fixed lattice constants (5.80 Å and 6.40 Å) to probe its robustness to lattice distortion. All results are aggregated in a structured JSON file for automated verification.

## Reproduction target
Using Quantum ESPRESSO with GGA‑PBE and publicly available pseudopotentials, perform the following computations and write all quantities to `/app/outputs/results.json`:

- **Lattice optimizations**: For Ti₂FeAl, Ti₂CoAl, and Ti₂NiAl, report the optimized lattice constant `a_opt_angstrom`, the total spin magnetic moment `total_moment_muB`, and the minority-spin band gap `minority_gap_eV`.
- **Z‑removal test**: For Ti₂Co (Z site vacant), report the lattice constant used (`a_angstrom`, which must be the optimized value of Ti₂CoAl), the total spin magnetic moment `total_moment_muB`, and the minority‑spin band gap `minority_gap_eV`.
- **Lattice‑parameter effect**: For Ti₂CoAl, report the minority‑spin band gap `gap` at the two fixed lattice constants 5.80 Å and 6.40 Å (single‑point SCF calculations at those cell parameters).

The JSON file must match the structure described in the output contract. The goal is to produce these values by genuinely executing the DFT workflow; they will be scored against independently determined reference data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT calculations and result collection
- Role: scored
- Action: Perform spin-polarized DFT calculations with Quantum ESPRESSO using GGA-PBE exchange-correlation. (1) Optimize the lattice constant of Ti2FeAl, Ti2CoAl, and Ti2NiAl in the Li2AgSb-type structure (4a,4c,4b,4d Wyckoff positions) and compute their total spin magnetic moments and minority-spin band gaps at equilibrium. (2) Optimize the lattice constant of Ti2Co (with a vacant Z site) in the same structure, then compute its total spin magnetic moment and minority gap at the Ti2CoAl equilibrium lattice constant. (3) For Ti2CoAl, perform single-point SCF calculations at fixed lattice constants 5.80 Å and 6.40 Å and extract the minority-spin gap. Collect all results in results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"lattice_optimizations": [{"compound": "Ti2FeAl"|"Ti2CoAl"|"Ti2NiAl", "a_opt_angstrom": float, "total_moment_muB": float, "minority_gap_eV": float}], "z_removal": {"a_angstrom": float, "total_moment_muB": float, "minority_gap_eV": float}, "lattice_parameter_effect": [{"a": 5.80, "gap": float}, {"a": 6.40, "gap": float}]}
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
- description: The file must contain three top-level keys: 'lattice_optimizations' (list of three objects, one per compound with keys compound, a_opt_angstrom, total_moment_muB, minority_gap_eV), 'z_removal' (an object with keys a_angstrom, total_moment_muB, minority_gap_eV for Ti2Co), and 'lattice_parameter_effect' (a list of two objects with keys a and gap for Ti2CoAl at a=5.80 and 6.40).
- schema:
  - `type`: object
  - `required`:
    - `lattice_optimizations`: array of objects
    - `z_removal`: object
    - `lattice_parameter_effect`: array of objects
  - `items`:
    - `compound`: string
    - `a_opt_angstrom`: float (Å)
    - `total_moment_muB`: float (μB)
    - `minority_gap_eV`: float (eV)
    - `a_angstrom`: float (Å)
    - `a`: float (Å)
    - `gap`: float (eV)

Notes: All values are obtained from DFT GGA-PBE calculations using Quantum ESPRESSO. The solver is expected to select appropriate pseudopotentials and convergence settings; the checker compares the reported values against hidden reference data with numerical tolerances.

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
          "lattice_optimizations": "array of objects",
          "z_removal": "object",
          "lattice_parameter_effect": "array of objects"
        },
        "items": {
          "compound": "string",
          "a_opt_angstrom": "float (Å)",
          "total_moment_muB": "float (μB)",
          "minority_gap_eV": "float (eV)",
          "a_angstrom": "float (Å)",
          "a": "float (Å)",
          "gap": "float (eV)"
        }
      },
      "description": "The file must contain three top-level keys: 'lattice_optimizations' (list of three objects, one per compound with keys compound, a_opt_angstrom, total_moment_muB, minority_gap_eV), 'z_removal' (an object with keys a_angstrom, total_moment_muB, minority_gap_eV for Ti2Co), and 'lattice_parameter_effect' (a list of two objects with keys a and gap for Ti2CoAl at a=5.80 and 6.40)."
    }
  ],
  "notes": "All values are obtained from DFT GGA-PBE calculations using Quantum ESPRESSO. The solver is expected to select appropriate pseudopotentials and convergence settings; the checker compares the reported values against hidden reference data with numerical tolerances."
}
```

## How you are scored
A hidden verifier reads your `results.json` and scores each of the three sets of quantities independently. Every computed value (magnetic moment, minority gap) is compared to a reference with a fixed numerical tolerance; results that fall within the tolerance receive full credit for that quantity, and credit degrades as the deviation grows. The total reward is a weighted sum of all quantity scores, with the lattice‑optimized properties of the three compounds receiving the highest weight, the Z‑removal gap and moment receiving intermediate weight, and the lattice‑parameter‑effect gaps receiving lower weight. The verifier does not expect exact bitwise agreement with a particular code, only that the values produced by a correct GGA‑PBE calculation lie within the tolerance. Reporting the paper’s numbers without actually running the DFT calculations will not produce the required internal consistency and will not earn credit; the scoring is designed to reward honest reproduction of the computational experiment.
