# DFT electronic structure of ordered and 12.5% antisite-disordered Co2TiSn

## Problem background
The Heusler compound Co₂TiSn is a candidate half‑metallic ferromagnet: a material where one spin channel is metallic while the other has a band gap at the Fermi level, resulting in 100% spin polarization. Bulk measurement techniques suggest perfect order, but local probes such as nuclear magnetic resonance and Mössbauer spectroscopy reveal that a significant fraction (~9%) of Co and Ti atoms exchange their lattice sites even in well‑annealed samples. Whether a density‑functional theory calculation can correctly capture the half‑metallic ground state of both perfectly ordered and partially antisite‑disordered Co₂TiSn remains an important question. This task requires computing the electronic structure and magnetic properties for the ordered compound and for a structure with 12.5% Co/Ti antisite disorder, using a full‑potential DFT method with the generalized gradient approximation, in order to determine whether the calculated magnetic moment and the minority‑spin density of states at the Fermi level agree with a half‑metallic picture.

## Approach
Use an open‑source full‑potential DFT code (for example, Quantum ESPRESSO) with the GGA exchange‑correlation functional. For the perfectly ordered Co₂TiSn crystal (cubic space group Fm3̅m, lattice constant 6.0718 Å; Co at 8a (¼,¼,¼), Ti at 4b (0,0,0), Sn at 4a (½,½,½)), perform a self‑consistent electronic structure calculation and obtain the total magnetic moment per formula unit and the density of states. Then construct a 2×2×2 supercell (32 atoms) of the same compound and introduce 12.5% Co/Ti antisite disorder by swapping one Co atom and one Ti atom, re‑run the same DFT procedure, and compute the corresponding magnetic moment and DOS. The central comparison is between the ordered and disordered cases: whether the minority‑spin channel remains gapped at the Fermi level, and whether the total magnetic moment stays close to the value expected for a half‑metal. The calculations should be performed with settings that ensure convergence, but the precise choice of kinetic‑energy cutoffs, k‑point grids, and smearing parameters is left to the solving agent.

## Reproduction target
For both the ordered structure and the 12.5% Co/Ti antisite‑disordered supercell, produce the following two artifacts:
1. A text file containing the total magnetic moment per formula unit (units: μ_B).
2. A JSON file with the minority‑spin density of states (DOS) on a fine energy grid that includes the Fermi level (energy=0). The DOS must be given in states per electron‑volt per formula unit.
The objective is to verify that the computed magnetic moment for the ordered structure is consistent with a half‑metallic ground state and that for both the ordered and disordered cases the minority‑spin DOS at the Fermi level is low enough to indicate a persisting half‑metallic gap. The acceptable value of the DOS at E_F will be determined by a hidden verifier; the task is to perform the DFT calculation honestly and report the resulting numbers.

## Assets

- Co2TiSn Heusler crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Ordered magnetic moment
- Role: scored
- Action: Using an open-source full-potential DFT code (e.g., Quantum ESPRESSO) with the GGA exchange-correlation functional, compute the electronic structure of perfectly ordered Co2TiSn (cubic Fm-3m, a=6.0718 Å, Co at 8a, Ti at 4b, Sn at 4a). Extract the total magnetic moment per formula unit (in μ_B).
- Output file: `/app/outputs/ordered_magnetic_moment.txt`
- Format: txt
- Contract: A single float value (units: μ_B per formula unit).
- Scoring: scored by hidden verifier

### Step 2: Ordered minority DOS
- Role: scored (load-bearing)
- Action: Using the same DFT setup as the previous step, compute the density of states (DOS) for ordered Co2TiSn. Output the minority-spin DOS on a fine energy grid around the Fermi level.
- Output file: `/app/outputs/ordered_dos.json`
- Format: json
- Contract: JSON object with keys 'energy' (array of floats in eV relative to Fermi level) and 'minority_dos' (array of floats in states/eV/f.u.). Must include the value at E_F (energy=0).
- Scoring: scored by hidden verifier

### Step 3: Disordered magnetic moment
- Role: scored
- Action: Construct a 2×2×2 supercell (32 atoms) of Co2TiSn. Introduce 12.5% Co/Ti antisite disorder by swapping one Co atom and one Ti atom. Run the same DFT calculation (full-potential, GGA) and output the total magnetic moment per formula unit (μ_B).
- Output file: `/app/outputs/disordered_magnetic_moment.txt`
- Format: txt
- Contract: A single float value (units: μ_B per formula unit).
- Scoring: scored by hidden verifier

### Step 4: Disordered minority DOS
- Role: scored (load-bearing)
- Action: Using the disordered supercell setup from the previous step, compute the density of states and output the minority-spin DOS data.
- Output file: `/app/outputs/disordered_dos.json`
- Format: json
- Contract: JSON object with keys 'energy' (array of floats in eV relative to Fermi level) and 'minority_dos' (array of floats in states/eV/f.u.). Must include the value at E_F (energy=0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ordered_magnetic_moment.txt`
- `/app/outputs/ordered_dos.json`
- `/app/outputs/disordered_magnetic_moment.txt`
- `/app/outputs/disordered_dos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ordered_magnetic_moment.txt
- path: `/app/outputs/ordered_magnetic_moment.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total magnetic moment of ordered Co2TiSn, compared to a fixed hidden gold value with tolerance.
- schema:
  - `type`: text
  - `units`: μ_B per formula unit

### ordered_dos.json
- path: `/app/outputs/ordered_dos.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minority-spin DOS of ordered Co2TiSn; the checker recomputes the DOS at the Fermi level (value at energy=0) and verifies it is below the half-metallic threshold.
- schema:
  - `type`: object
  - `required`:
    - `energy`: array of float (eV, relative to Fermi level)
    - `minority_dos`: array of float (states/eV/f.u.)

### disordered_magnetic_moment.txt
- path: `/app/outputs/disordered_magnetic_moment.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total magnetic moment of disordered Co2TiSn, compared to a fixed hidden gold value with tolerance.
- schema:
  - `type`: text
  - `units`: μ_B per formula unit

### disordered_dos.json
- path: `/app/outputs/disordered_dos.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minority-spin DOS of disordered Co2TiSn; the checker recomputes the DOS at the Fermi level and verifies it is below the half-metallic threshold.
- schema:
  - `type`: object
  - `required`:
    - `energy`: array of float (eV, relative to Fermi level)
    - `minority_dos`: array of float (states/eV/f.u.)

Notes: All output files are used to verify the main computational claims: the magnetic moment of the ordered structure and the persistence of the half-metallic gap in both ordered and disordered cases. The checker recomputes the minority-spin DOS at the Fermi level from the raw energy-DOS arrays and compares the submitted magnetic moments to the paper-reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ordered_magnetic_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "μ_B per formula unit"
      },
      "description": "Total magnetic moment of ordered Co2TiSn, compared to a fixed hidden gold value with tolerance."
    },
    {
      "file": "ordered_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "energy": "array of float (eV, relative to Fermi level)",
          "minority_dos": "array of float (states/eV/f.u.)"
        }
      },
      "description": "Minority-spin DOS of ordered Co2TiSn; the checker recomputes the DOS at the Fermi level (value at energy=0) and verifies it is below the half-metallic threshold."
    },
    {
      "file": "disordered_magnetic_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "μ_B per formula unit"
      },
      "description": "Total magnetic moment of disordered Co2TiSn, compared to a fixed hidden gold value with tolerance."
    },
    {
      "file": "disordered_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "energy": "array of float (eV, relative to Fermi level)",
          "minority_dos": "array of float (states/eV/f.u.)"
        }
      },
      "description": "Minority-spin DOS of disordered Co2TiSn; the checker recomputes the DOS at the Fermi level and verifies it is below the half-metallic threshold."
    }
  ],
  "notes": "All output files are used to verify the main computational claims: the magnetic moment of the ordered structure and the persistence of the half-metallic gap in both ordered and disordered cases. The checker recomputes the minority-spin DOS at the Fermi level from the raw energy-DOS arrays and compares the submitted magnetic moments to the paper-reported values with appropriate tolerances."
}
```

## How you are scored
Each output file is evaluated by a hidden verifier that runs after the task is submitted. For the magnetic moment files, the verifier compares the submitted value to a reference value (derived from published results) with an appropriate tolerance. For the DOS files, the verifier extracts the minority‑spin DOS at the Fermi level from the supplied energy‑DOS arrays and checks whether it falls below a threshold that defines the half‑metallic gap. Each of the four scored steps carries a weight, and the final reward (a float between 0 and 1) is the weighted sum of the per‑step scores. No single reported number guarantees a full score; the verifier independently recomputes the DOS at E_F and compares the magnetic moments to a hidden reference, so fabricating values that merely look plausible cannot reliably bypass the checking logic.
