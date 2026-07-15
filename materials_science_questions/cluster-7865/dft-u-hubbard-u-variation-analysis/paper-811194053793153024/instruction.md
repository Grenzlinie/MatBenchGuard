# Band inversion and topological aspects of a TiNI monolayer

## Problem background
Two-dimensional topological insulators (2D-TIs) that can support the quantum spin Hall (QSH) effect at elevated temperatures are of great interest for low-power spintronics and quantum computing. A key requirement is a sizeable bulk band gap opened by spin-orbit coupling (SOC). Layered transition metal nitride halides are a promising material family, and the monolayer form of titanium nitride iodide (TiNI), which can be obtained by mechanical exfoliation from the bulk crystal, has been put forward as a candidate 2D-TI. Determining whether this monolayer indeed exhibits the necessary properties — a non-trivial band topology, an SOC‑induced gap large enough for room‑temperature operation, and robust edge states — hinges on first‑principles calculations of several inter‑related quantities. This task reproduces the core set of computed properties that characterise the TiNI monolayer as a topological insulator.

## Approach
The evaluation relies on plane‑wave density functional theory (DFT) within the generalized gradient approximation (PBE functional) and projector augmented‑wave (PAW) pseudopotentials. All calculations are performed with the open‑source Quantum ESPRESSO suite and the SSSP pseudopotential library (PBE accuracy) for Ti, N, and I. The workflow proceeds through two preparatory relaxations (bulk α‑TiNI and isolated monolayer) followed by five targeted property calculations: (i) a four‑slab model to map the total energy as a function of interlayer separation, from which the minimum cleavage energy per area and the maximum derivative (cleavage strength) are extracted; (ii) a band structure calculation including SOC that identifies the Dirac point and yields the SOC‑induced band gap; (iii) from the SOC band structure, parity eigenvalues of the occupied bands at the four time‑reversal invariant momenta (Γ, X, R, Y) are used in the Fu‑Kane formula to obtain the Z₂ topological invariant; (iv) a hydrogen‑passivated nanoribbon of width ~12 nm is constructed and its band structure computed to reveal any topological edge states; (v) uniaxial strain is applied along the x and y directions, and the band gap at the Γ point (without SOC) is tracked to assess the robustness and tuneability of band inversion. All output files must be written according to the formats specified in the steps below.

## Reproduction target
Produce the following specific, independently checkable results for the TiNI monolayer:

1. **Cleavage energy and strength** – the minimum exfoliation energy per unit area (J/m²) and the cleavage strength (GPa), written to `cleavage_results.json`.
2. **SOC‑induced band gap** – the band gap at the Dirac point obtained from the PBE+SOC calculation (meV), written to `band_gap_soc.txt`.
3. **Z₂ topological invariant** – the value (0 or 1) computed via the Fu‑Kane parity criterion, written to `z2_invariant.txt`.
4. **Edge‑state band structure** – the k‑resolved electronic structure of a hydrogen‑passivated nanoribbon, stored in a two‑column file `edge_states_bandstructure.dat` that clearly marks the Fermi level and any in‑gap edge states.
5. **Strain‑dependent band gap** – the Γ‑point band gap (without SOC, negative values allowed to indicate band inversion) for uniaxial strains from −5% to +5% along the x and y directions, written to `strain_gap_results.csv` with columns `strain_percent,direction,gap_eV`.

No other documents or references are needed; the task is self‑contained.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotential library (PBE accuracy): https://www.materialscloud.org/discover/sssp/table/precision
- Experimental structure of α-TiNI

## Workflow steps

### Step 1: Bulk relaxation
- Role: process
- Action: Perform DFT relaxation of bulk α-TiNI using the experimental structure as starting point, to optimize lattice constants and atomic positions.
- Evidence: `/app/outputs/bulk_relax.log`

### Step 2: Monolayer relaxation
- Role: process
- Action: Extract a monolayer from the relaxed bulk, add a vacuum layer of at least 15 Å, and relax the monolayer lattice constants and atomic positions.
- Evidence: `/app/outputs/monolayer_relax.log`

### Step 3: Cleavage energy
- Role: scored (load-bearing)
- Action: Construct a four-slab model from the relaxed bulk. Compute total energy as a function of interlayer distance D, extract the minimum cleavage energy E_cl (J/m²) and the maximum derivative σ (GPa), and write the results to cleavage_results.json.
- Output file: `/app/outputs/cleavage_results.json`
- Format: json
- Contract: { "cleavage_energy_Jm2": float, "cleavage_strength_GPa": float }
- Scoring: scored by hidden verifier

### Step 4: SOC band gap
- Role: scored
- Action: Perform a DFT band structure calculation on the relaxed monolayer with spin‑orbit coupling. Identify the Dirac point and extract the SOC‑induced band gap (meV). Write the PBE gap to band_gap_soc.txt. Optionally compute the HSE gap and append it.
- Output file: `/app/outputs/band_gap_soc.txt`
- Format: txt
- Contract: Line: PBE_SOC_gap_meV: <float>; optional line: HSE_SOC_gap_meV: <float>
- Scoring: scored by hidden verifier

### Step 5: Z₂ invariant
- Role: scored
- Action: From the SOC band structure, compute the parity eigenvalues of occupied bands at the four time‑reversal invariant momenta (Γ, X, R, Y). Evaluate the Z₂ topological invariant using the Fu‑Kane formula and write the result to z2_invariant.txt.
- Output file: `/app/outputs/z2_invariant.txt`
- Format: txt
- Contract: Line: Z2: <0 or 1>
- Scoring: scored by hidden verifier

### Step 6: Edge states
- Role: scored
- Action: Build a hydrogen‑passivated TiNI nanoribbon from the relaxed monolayer (width ~12 nm). Compute its band structure and output the k‑points vs energy data to edge_states_bandstructure.dat. Indicate the Fermi level.
- Output file: `/app/outputs/edge_states_bandstructure.dat`
- Format: txt
- Contract: Two‑column format: k (dimensionless) energy (eV). Comment lines indicate Fermi level and edge state bands.
- Scoring: scored by hidden verifier

### Step 7: Strain‑dependent band gap
- Role: scored
- Action: Apply uniaxial strain along the x and y directions (e.g., −5% to +5%) to the monolayer. Compute band structures without SOC, extract the band gap at the Γ point, and write the results to strain_gap_results.csv. Negative gaps indicate band inversion.
- Output file: `/app/outputs/strain_gap_results.csv`
- Format: csv
- Contract: CSV with columns: strain_percent, direction (x or y), gap_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cleavage_results.json`
- `/app/outputs/band_gap_soc.txt`
- `/app/outputs/z2_invariant.txt`
- `/app/outputs/edge_states_bandstructure.dat`
- `/app/outputs/strain_gap_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cleavage_results.json
- path: `/app/outputs/cleavage_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Cleavage energy and strength for exfoliation feasibility.
- schema:
  - `type`: object
  - `required`:
    - `cleavage_energy_Jm2`: float
    - `cleavage_strength_GPa`: float

### band_gap_soc.txt
- path: `/app/outputs/band_gap_soc.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: SOC‑induced band gap at the Dirac point (PBE value).
- schema:
  - `type`: text

### z2_invariant.txt
- path: `/app/outputs/z2_invariant.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Z₂ topological invariant (0 or 1).
- schema:
  - `type`: text

### edge_states_bandstructure.dat
- path: `/app/outputs/edge_states_bandstructure.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Nanoribbon band structure showing helical edge states.
- schema:
  - `type`: text

### strain_gap_results.csv
- path: `/app/outputs/strain_gap_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gap evolution under uniaxial strain along x and y directions.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `direction`, `gap_eV`

Notes: Phonon spectrum omitted as per approved plan; HSE band gap is optional; scoring uses PBE gap only. Edge states are checked for Dirac‑like crossing inside the gap; strain trend checks monotonic/ordering of gap under strain.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cleavage_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "cleavage_energy_Jm2": "float",
          "cleavage_strength_GPa": "float"
        }
      },
      "description": "Cleavage energy and strength for exfoliation feasibility."
    },
    {
      "file": "band_gap_soc.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "SOC‑induced band gap at the Dirac point (PBE value)."
    },
    {
      "file": "z2_invariant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Z₂ topological invariant (0 or 1)."
    },
    {
      "file": "edge_states_bandstructure.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Nanoribbon band structure showing helical edge states."
    },
    {
      "file": "strain_gap_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "direction",
          "gap_eV"
        ]
      },
      "description": "Band gap evolution under uniaxial strain along x and y directions."
    }
  ],
  "notes": "Phonon spectrum omitted as per approved plan; HSE band gap is optional; scoring uses PBE gap only. Edge states are checked for Dirac‑like crossing inside the gap; strain trend checks monotonic/ordering of gap under strain."
}
```

## How you are scored
A hidden automated verifier will independently inspect every scored output file you write under `/app/outputs`. Each artifact is checked against a set of pre‑registered criteria, which may include numeric tolerances for the cleavage properties and SOC gap, an exact match for the Z₂ invariant, a structural audit of the nanoribbon band structure (e.g., presence of a gapless crossing inside the bulk gap), and a trend/ordering check on the strain‑dependent gap table. The verifier does not rely on any external paper; it uses internally stored reference values and tolerance rules. The individual scores are weighted and combined into a single final reward between 0 and 1. Simply reporting a set of numbers is not sufficient — the verifier will validate that your submitted files contain the required fields, follow the specified formats, and pass the quantitative checks. Your goal is to compute each property faithfully from the DFT protocol, ensuring that the files contain correct, self‑consistent results.
