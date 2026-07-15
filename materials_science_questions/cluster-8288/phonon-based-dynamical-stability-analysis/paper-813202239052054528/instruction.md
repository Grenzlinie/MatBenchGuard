# First-principles structural, electronic, and optical properties of M2N2(NH) compounds

## Problem background
The family of compounds with formula M<sub>2</sub>N<sub>2</sub>(NH), where M = C, Si, Ge, or Sn, crystallises in a base‑centered orthorhombic structure (space group Cmc2<sub>1</sub>). The carbon and silicon members (C<sub>2</sub>N<sub>2</sub>(NH) and Si<sub>2</sub>N<sub>2</sub>(NH)) have been studied experimentally and theoretically, but the germanium and tin analogues (Ge<sub>2</sub>N<sub>2</sub>(NH) and Sn<sub>2</sub>N<sub>2</sub>(NH)) have not yet been characterised. This task investigates the structural, mechanical, electronic, and dielectric properties of all four compounds using first‑principles density functional theory. The results will reveal whether Ge<sub>2</sub>N<sub>2</sub>(NH) and Sn<sub>2</sub>N<sub>2</sub>(NH) are mechanically stable, how their lattice constants, bulk moduli, and elastic constants evolve across the M = C → Si → Ge → Sn series, the nature and magnitude of their electronic band gaps, and the anisotropy of their static dielectric responses. Understanding these properties will assess the potential of the Ge and Sn compounds for optoelectronic applications.

## Approach
The investigation proceeds via density functional theory (DFT) with the GGA‑PBE exchange‑correlation functional, using an open‑source plane‑wave code such as Quantum ESPRESSO. The workflow begins with initial unit cells: known experimental lattice parameters are available for C<sub>2</sub>N<sub>2</sub>(NH) (a ≈ 7.618 Å, b ≈ 4.483 Å, c ≈ 4.038 Å) and Si<sub>2</sub>N<sub>2</sub>(NH) (a ≈ 9.193 Å, b ≈ 5.409 Å, c ≈ 4.819 Å). Starting guesses for Ge<sub>2</sub>N<sub>2</sub>(NH) and Sn<sub>2</sub>N<sub>2</sub>(NH) are constructed by scaling the Si cell by the ratio of atomic radii (Ge/Si ≈ 1.07, Sn/Si ≈ 1.18). Atomic positions are inherited from the isostructural orthorhombic Cmc2<sub>1</sub> prototypes. After structure generation, each compound undergoes a full geometry optimisation (cell vectors and ionic positions) until forces and stress converge. The relaxed cells then serve for three types of post‑processing: (i) finite‑difference elastic constants, from which the Voigt–Reuss–Hill bulk modulus is derived and Born mechanical stability is tested; (ii) a band‑structure calculation yielding the fundamental band gap value and its direct/indirect character; (iii) a frequency‑dependent dielectric function within the random‑phase approximation (RPA, no local‑field corrections) to extract the static dielectric tensor components along the a, b, and c axes and their isotropic average. All results are collected in a single structured JSON output for comparison across the four compounds.

## Reproduction target
Produce a JSON file `/app/outputs/computed_properties.json` that contains, for each of the four compounds C<sub>2</sub>N<sub>2</sub>(NH), Si<sub>2</sub>N<sub>2</sub>(NH), Ge<sub>2</sub>N<sub>2</sub>(NH), and Sn<sub>2</sub>N<sub>2</sub>(NH), the following quantities obtained from the DFT calculations described above:
- optimised lattice constants a, b, c (Å)
- bulk modulus (GPa) evaluated from the elastic constants using the Voigt–Reuss–Hill average
- the full set of independent elastic constants C<sub>11</sub>–C<sub>66</sub> (GPa)
- a boolean Born mechanical stability verdict
- the electronic band gap type ('direct' or 'indirect') and its value (eV)
- static dielectric constants ε<sub>∥a</sub>, ε<sub>∥b</sub>, ε<sub>∥c</sub> (dimensionless) and their polycrystalline average ε<sub>0</sub>.
All numerical values must be reported with two decimal places. The exact JSON schema is specified in the Workflow steps and Output contract sections below; the file must conform to that schema exactly.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials: https://www.materialcloud.org/discover/sssp

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Create base-centered orthorhombic (space group Cmc2_1) unit cells for C2N2(NH), Si2N2(NH), Ge2N2(NH), and Sn2N2(NH). For C and Si, use known experimental lattice parameters (C: a=7.618, b=4.483, c=4.038 Å; Si: a=9.193, b=5.409, c=4.819 Å) with atomic positions derived from isostructural literature. For Ge and Sn, estimate initial cells by scaling Si parameters by the ratio of atomic radii (Ge/Si≈1.07, Sn/Si≈1.18). Write input files ready for DFT geometry optimization.
- Evidence: `/app/outputs/initial_structures.cif`

### Step 2: DFT calculations and property aggregation
- Role: scored
- Action: For each of the four compounds, use GGA-PBE to: (a) perform full geometry optimization (cell + ions) to obtain relaxed lattice constants; (b) compute elastic constants via finite differences and bulk modulus via Voigt–Reuss–Hill average; (c) compute the band structure and extract the band gap value and its type (direct/indirect); (d) compute the dielectric function (RPA, no local field) for axes a, b, c and extract static dielectric constants ε_∥a, ε_∥b, ε_∥c and their average ε₀. Assemble all results into the output JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: JSON object with keys 'C2N2(NH)', 'Si2N2(NH)', 'Ge2N2(NH)', 'Sn2N2(NH)'. Each value is an object containing: 'lattice_constants': {a: float, b: float, c: float} (Å), 'bulk_modulus': float (GPa), 'elastic_constants': {C11: float, C12: float, C13: float, C22: float, C23: float, C33: float, C44: float, C55: float, C66: float} (GPa), 'born_stable': bool, 'band_gap_type': string ('direct' or 'indirect'), 'band_gap_value': float (eV), 'static_dielectric_constants': {epsilon_parallel_a: float, epsilon_parallel_b: float, epsilon_parallel_c: float, epsilon_0: float}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed structural, elastic, electronic, and dielectric properties for the four M2N2(NH) compounds. The checker compares each numerical value to the paper-reported gold within tolerances.
- schema:
  - `type`: object
  - `keys`: `C2N2(NH)`, `Si2N2(NH)`, `Ge2N2(NH)`, `Sn2N2(NH)`
  - `compound_object`:
    - `type`: object
    - `fields`:
      - `lattice_constants`:
        - `type`: object
        - `fields`:
          - `a`: number (Angstrom)
          - `b`: number (Angstrom)
          - `c`: number (Angstrom)
      - `bulk_modulus`: number (GPa)
      - `elastic_constants`:
        - `type`: object
        - `fields`:
          - `C11`: number (GPa)
          - `C12`: number (GPa)
          - `C13`: number (GPa)
          - `C22`: number (GPa)
          - `C23`: number (GPa)
          - `C33`: number (GPa)
          - `C44`: number (GPa)
          - `C55`: number (GPa)
          - `C66`: number (GPa)
      - `born_stable`: boolean
      - `band_gap_type`: string (direct or indirect)
      - `band_gap_value`: number (eV)
      - `static_dielectric_constants`:
        - `type`: object
        - `fields`:
          - `epsilon_parallel_a`: number (dimensionless)
          - `epsilon_parallel_b`: number (dimensionless)
          - `epsilon_parallel_c`: number (dimensionless)
          - `epsilon_0`: number (dimensionless)

Notes: Phonon calculations and dynamical stability verification are omitted due to high cost; mechanical stability is verified through elastic constants (Born criteria). The agent may choose any open-source DFT implementation capable of GGA-PBE, finite-difference elastic constants, and RPA dielectric function.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "keys": [
          "C2N2(NH)",
          "Si2N2(NH)",
          "Ge2N2(NH)",
          "Sn2N2(NH)"
        ],
        "compound_object": {
          "type": "object",
          "fields": {
            "lattice_constants": {
              "type": "object",
              "fields": {
                "a": "number (Angstrom)",
                "b": "number (Angstrom)",
                "c": "number (Angstrom)"
              }
            },
            "bulk_modulus": "number (GPa)",
            "elastic_constants": {
              "type": "object",
              "fields": {
                "C11": "number (GPa)",
                "C12": "number (GPa)",
                "C13": "number (GPa)",
                "C22": "number (GPa)",
                "C23": "number (GPa)",
                "C33": "number (GPa)",
                "C44": "number (GPa)",
                "C55": "number (GPa)",
                "C66": "number (GPa)"
              }
            },
            "born_stable": "boolean",
            "band_gap_type": "string (direct or indirect)",
            "band_gap_value": "number (eV)",
            "static_dielectric_constants": {
              "type": "object",
              "fields": {
                "epsilon_parallel_a": "number (dimensionless)",
                "epsilon_parallel_b": "number (dimensionless)",
                "epsilon_parallel_c": "number (dimensionless)",
                "epsilon_0": "number (dimensionless)"
              }
            }
          }
        }
      },
      "description": "Computed structural, elastic, electronic, and dielectric properties for the four M2N2(NH) compounds. The checker compares each numerical value to the paper-reported gold within tolerances."
    }
  ],
  "notes": "Phonon calculations and dynamical stability verification are omitted due to high cost; mechanical stability is verified through elastic constants (Born criteria). The agent may choose any open-source DFT implementation capable of GGA-PBE, finite-difference elastic constants, and RPA dielectric function."
}
```

## How you are scored
The submitted `computed_properties.json` will be inspected by an automated verifier hidden from you. Numerical entries (lattice constants, bulk modulus, elastic constants, band gap value, and dielectric constants) are compared to a hidden reference set; credit is awarded when each entry lies within an allowed tolerance window that is appropriate for the spread expected from different DFT implementations. In addition, the verifier checks that the derived Boolean stability flags (Born criteria) are correct for the Ge and Sn compounds, and that certain physical relationships among the computed quantities—such as the expected trend of bulk moduli across the series and the anisotropy pattern of the dielectric constants—are consistent with the results of the source investigation. The overall reward is a weighted sum of the checks passed, with the largest weight placed on the numerical matches for the lattice constants, bulk moduli, band gaps, and dielectric constants, and a smaller weight on the structural/consistency assertions.
