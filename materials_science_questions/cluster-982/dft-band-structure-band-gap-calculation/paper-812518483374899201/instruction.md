# DFT Band Gaps and Static Dielectric Constants of Orthorhombic CsPbCl3

## Problem background
The perovskite halide CsPbCl3 is a promising material for optoelectronic applications. Accurate knowledge of its electronic band gap and optical dielectric response is essential for device design. Density functional theory (DFT) calculations with different exchange-correlation functionals can yield varying predictions of these properties. This task requires you to compute the band gap of orthorhombic CsPbCl3 under several DFT approaches and to determine the static dielectric constants from the approach that includes spin-orbit coupling and a Hubbard correction. The goal is to produce a set of band gap values and directional dielectric constants that can be compared against reference data.

## Approach
You will perform DFT calculations on the orthorhombic crystal structure of CsPbCl3 (lattice parameters a=7.8600 Å, b=7.9260 Å, c=11.2451 Å, space group Pbnm) using an open-source DFT code such as Elk, Quantum ESPRESSO, or ABINIT. Four exchange-correlation treatments are applied: (i) standard PBE (GGA), (ii) modified Becke-Johnson (mBJ), (iii) PBE+U with a Hubbard U correction of 0.294 Ry applied to Pb 5d electrons, and (iv) mBJ+U+SO, which adds spin-orbit coupling to the mBJ+U scheme. For each treatment, a self-consistent charge density is obtained, the electronic band structure is computed, and the direct band gap at the Γ point is extracted. For the mBJ+U+SO calculation only, a subsequent optical calculation is performed to derive the dielectric function, from which the static dielectric constant ε₁(0) is taken in each Cartesian direction (xx, yy, zz). The Hubbard U value is a fixed input and does not need to be refitted.

## Reproduction target
Produce two scored output files. First, compute the band gap (in eV) from each of the four DFT treatments and write them to 'band_gaps.json' as an object with keys "pbe", "mbj", "pbe_u", and "mbj_u_so". Second, from the mBJ+U+SO calculation, extract the static dielectric constants ε₁(0) along the xx, yy, and zz directions and write them to 'static_dielectric.json' as an object with keys "xx", "yy", "zz". Both files must strictly follow the JSON schema described in the workflow steps.

## Assets

- CsPbCl3 orthorhombic crystal structure: 10.1021/acs.jpcc.8b04327
- Open-source DFT code (ELK, Quantum ESPRESSO, ABINIT, etc.)
- Pseudopotentials / PAW datasets for Cs, Pb, Cl

## Workflow steps

### Step 1: Prepare crystal structure
- Role: process
- Action: Construct the crystal structure of orthorhombic CsPbCl3 (lattice parameters a=7.8600 Å, b=7.9260 Å, c=11.2451 Å, space group Pbnm) using the atomic positions from the literature. Write a suitable input file for the chosen DFT code.
- Evidence: `/app/outputs/structure.txt`

### Step 2: DFT band-gap computation
- Role: scored
- Action: Run self-consistent DFT calculations on the prepared structure using four exchange-correlation treatments: (i) GGA-PBE, (ii) mBJ, (iii) GGA+U with Hubbard U=0.294 Ry on Pb 5d electrons, (iv) mBJ+U+SO (with spin-orbit coupling). Use converged k-point mesh and appropriate convergence criteria. Compute the electronic band structure and identify the band gap (direct at Γ). Write the four band-gap values (in eV) to /app/outputs/band_gaps.json as a JSON object with keys "pbe", "mbj", "pbe_u", "mbj_u_so".
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"type":"object", "required":["pbe","mbj","pbe_u","mbj_u_so"], "properties":{"pbe":{"type":"number"},"mbj":{"type":"number"},"pbe_u":{"type":"number"},"mbj_u_so":{"type":"number"}}}
- Scoring: scored by hidden verifier

### Step 3: Static dielectric constants from mBJ+U+SO
- Role: scored (load-bearing)
- Action: Using the wavefunctions from the mBJ+U+SO calculation, compute the dielectric function with a dense k-point mesh. Extract the static dielectric constant ε₁(0) for each Cartesian direction (xx, yy, zz). Write the three values to /app/outputs/static_dielectric.json as a JSON object with keys "xx", "yy", "zz".
- Output file: `/app/outputs/static_dielectric.json`
- Format: json
- Contract: {"type":"object", "required":["xx","yy","zz"], "properties":{"xx":{"type":"number"},"yy":{"type":"number"},"zz":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/static_dielectric.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap values in eV obtained from the four DFT functionals.
- schema:
  - `type`: object
  - `required`: `pbe`, `mbj`, `pbe_u`, `mbj_u_so`
  - `properties`:
    - `pbe`:
      - `type`: number
    - `mbj`:
      - `type`: number
    - `pbe_u`:
      - `type`: number
    - `mbj_u_so`:
      - `type`: number

### static_dielectric.json
- path: `/app/outputs/static_dielectric.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constants ε₁(0) from the mBJ+U+SO calculation.
- schema:
  - `type`: object
  - `required`: `xx`, `yy`, `zz`
  - `properties`:
    - `xx`:
      - `type`: number
    - `yy`:
      - `type`: number
    - `zz`:
      - `type`: number

Notes: The Hubbard U correction parameter (0.294 Ry for Pb 5d) is provided as a fixed input and does not need to be refitted. The task does not require reproducing the experimental XPS comparison or the full optical constants curves.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "pbe",
          "mbj",
          "pbe_u",
          "mbj_u_so"
        ],
        "properties": {
          "pbe": {
            "type": "number"
          },
          "mbj": {
            "type": "number"
          },
          "pbe_u": {
            "type": "number"
          },
          "mbj_u_so": {
            "type": "number"
          }
        }
      },
      "description": "Band gap values in eV obtained from the four DFT functionals."
    },
    {
      "file": "static_dielectric.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "xx",
          "yy",
          "zz"
        ],
        "properties": {
          "xx": {
            "type": "number"
          },
          "yy": {
            "type": "number"
          },
          "zz": {
            "type": "number"
          }
        }
      },
      "description": "Static dielectric constants ε₁(0) from the mBJ+U+SO calculation."
    }
  ],
  "notes": "The Hubbard U correction parameter (0.294 Ry for Pb 5d) is provided as a fixed input and does not need to be refitted. The task does not require reproducing the experimental XPS comparison or the full optical constants curves."
}
```

## How you are scored
A hidden verifier reads your 'band_gaps.json' and 'static_dielectric.json' files. It compares each reported value to a hidden reference and checks a relative ordering among the band gaps. The reward is based on the number of values that fall within a hidden tolerance and whether the ordering requirement is satisfied. Simply writing down guessed numbers without performing the DFT calculations will not match the references and will result in a low reward. The verifier runs instantly and does not repeat the DFT computations.
