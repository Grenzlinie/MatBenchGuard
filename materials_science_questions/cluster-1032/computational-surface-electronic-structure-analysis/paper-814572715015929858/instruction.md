# Energetic stability and spin-split band structure of a 2D surface alloy

## Problem background
The (Au,Al)/Si(111) 2×2 surface is a two-dimensional compound formed by co-depositing Au and Al on a Si(111) substrate. Density functional theory (DFT) calculations can be used to predict the most stable atomic arrangement and to compute its electronic band structure, including spin-split metallic surface states. This task focuses on reproducing the core computational DFT results: the energetic ordering of candidate Au–Al–Si compositions, the metallic character of the ground-state phase, and the spin-splitting parameters of its bands.

## Approach
Build slab models for four candidate surface compositions (4Au 1Al, 3Au 1Al, 4Au 2Al, 4Au 3Al per 2×2 unit cell) using the structural motif of a rectangular unit of four Au atoms with an Al centre, surrounded by Si adatoms and dimers. Relax each structure with spin–orbit-coupled DFT using PAW pseudopotentials. From the relaxed total energies, compute relative formation energies with the 4Au 1Al composition as the reference. Then perform non‑self‑consistent band‑structure calculations for the 1‑, 2‑ and 3‑Al compositions and analyse the bands to determine metallicity of the 4Au 3Al phase, the trend of band‑edge shifts with increasing Al content, and the spin‑splitting parameters (momentum splitting and energy splitting) along specific high‑symmetry directions.

## Assets

- Any DFT code supporting PAW and spin-orbit coupling (e.g., Quantum ESPRESSO, VASP): https://www.quantum-espresso.org/
- PAW pseudopotentials for Au, Al, Si, H (e.g., SSSP library): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct Si(111) slab models for four candidate compositions: 4Au_1Al, 3Au_1Al, 4Au_2Al, 4Au_3Al per 2×2 cell. Use a slab of 5 Si bilayers, bottom two layers fixed and H‑terminated, ~15 Å vacuum. The in‑plane lattice vectors for the 2×2 supercell are (in Bohr):
  ```
  v1 =  7.895710  0.000000  0.000000
  v2 = -3.947855  6.837957  0.000000
  ```
  Place atoms according to the rectangular motif: four Au atoms form a rectangle with an Al atom at its centre; Si adatoms sit on the short sides and Si dimers on the long sides. The initial (unrelaxed) fractional coordinates for the **4Au_1Al** composition are listed below. All atoms are in the surface region above the Si substrate; the substrate itself consists of five Si bilayers with the two lowest bilayers fixed at bulk positions and the bottom face saturated with hydrogen.

  **Fractional coordinates for 4Au_1Al (initial, surface atoms only):**
  ```
  Au   0.7012  0.7111  0.5045
  Au   0.7012  0.2111  0.5045
  Au   0.2012  0.7111  0.5045
  Au   0.2012  0.2111  0.5045
  Al   0.4512  0.4611  0.5045
  Si   0.9300  0.7111  0.5045   # adatom short side
  Si   0.9300  0.2111  0.5045   # adatom short side
  Si   0.4512  0.9500  0.5045   # dimer long side
  Si   0.4512  0.8300  0.5045   # dimer long side
  Si   0.4512  0.0800  0.5045   # dimer long side
  Si   0.4512  0.2000  0.5045   # dimer long side
  ```
  The c‑axis lattice parameter is `c = 30.0 Bohr`. The first five Si bilayers (positions not shown here) must be built from bulk Si(111) coordinates with lattice constant 5.43 Å and the bottom two bilayers fixed; the dangling bonds of the lowest Si layer are saturated with H atoms at a bond length of ~1.5 Å.

  For the other compositions, modify the 4Au_1Al model as follows:
  - **3Au_1Al**: Remove the Au atom at (0.2012, 0.2111, 0.5045).
  - **4Au_2Al**: Replace the Si dimer atom at (0.4512, 0.9500, 0.5045) with an Al atom.
  - **4Au_3Al**: Starting from 4Au_2Al, also replace the Si dimer atom at (0.4512, 0.0800, 0.5045) with an Al atom.

  Apply these modifications before relaxation.

### Step 2: DFT geometry relaxation
- Role: process
- Action: For each slab model, perform geometry relaxation using the chosen DFT code with PAW pseudopotentials, spin-orbit coupling, plane-wave cutoff 400 eV, Monkhorst-Pack 6×6×1 k‑mesh. Relax atomic positions until forces < 0.01 eV/Å. Record total energies for all four compositions.

### Step 3: Compute relative formation energies
- Role: scored
- Action: From the relaxed total energies, compute relative formation energies per 2×2 cell using the 4Au_1Al composition as the zero reference. Write the results to formation_energies.csv with columns for composition, total energy per cell (eV), and relative energy (eV).
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: composition (string), total_energy_per_cell_eV (float), relative_energy_eV (float). Four rows for '4Au_1Al', '3Au_1Al', '4Au_2Al', '4Au_3Al'.
- Scoring: scored by hidden verifier

### Step 4: Band structure calculation
- Role: process
- Action: For the relaxed structures of the compositions with 1, 2, and 3 Al atoms, perform non‑self‑consistent band structure calculations using a 9×9×1 k‑mesh and a slab thickness of 6 Si bilayers, including spin‑orbit coupling. Extract electronic dispersion curves and surface character weights.

### Step 5: Band structure analysis and summary
- Role: scored (load-bearing)
- Action: Analyze the band structures: determine whether the 4Au_3Al composition is metallic (bands crossing the Fermi level); describe the energy shift trend of the surface resonant band and bulk band edge as Al content increases from 1 to 3 Al atoms per cell. Compute spin splitting parameters for the 4Au_3Al composition. For the spin‑split bands, focus on the inner spin‑split pair closest to the Γ point along the two Γ–M directions that correspond to the short and long sides of the rectangular unit: direction [11–2] (Γ–M short) and direction [2–1–1] (Γ–M long). Extract the momentum offset Δk∥ (in Å⁻¹) between the spin‑polarised bands at the Fermi level **along the [11–2] direction**, where the splitting is maximal. Also extract the energy splitting ΔE_F (in meV) between the two spin branches at the constant momentum where the splitting is maximal, **for each direction separately**: ΔE_F for the [11–2] direction and ΔE_F for the [2–1–1] direction. Write the results to band_structure_summary.json.
- Output file: `/app/outputs/band_structure_summary.json`
- Format: json
- Contract: JSON object with keys: 'metallic' (bool), 'band_shift_trend' (string), 'spin_splitting': { 'delta_k_parallel' (float, Å⁻¹), 'delta_E_meV_11minus2' (float), 'delta_E_meV_2minus1minus1' (float) }.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/band_structure_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total and relative formation energies per 2×2 cell for the four (Au,Al)/Si(111) compositions. The checker compares each relative_energy_eV to a hidden paper-reported reference within an appropriate tolerance and verifies the correct sign (higher/lower).
- schema:
  - `type`: table
  - `required_columns`: `composition`, `total_energy_per_cell_eV`, `relative_energy_eV`
  - `units`:
    - `total_energy_per_cell_eV`: eV
    - `relative_energy_eV`: eV

### band_structure_summary.json
- path: `/app/outputs/band_structure_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic band summary for the 4Au_3Al composition: metallicity, band shift trend, and spin-splitting parameters. The checker compares metallicity (bool), band_shift_trend description, and spin-splitting parameters to hidden paper-reported references.
- schema:
  - `type`: object
  - `required`: `metallic`, `band_shift_trend`, `spin_splitting`
  - `properties`:
    - `metallic`:
      - `type`: boolean
    - `band_shift_trend`:
      - `type`: string
    - `spin_splitting`:
      - `type`: object
      - `required`: `delta_k_parallel`, `delta_E_meV_11minus2`, `delta_E_meV_2minus1minus1`
      - `properties`:
        - `delta_k_parallel`:
          - `type`: number
        - `delta_E_meV_11minus2`:
          - `type`: number
        - `delta_E_meV_2minus1minus1`:
          - `type`: number
  - `units`:
    - `delta_k_parallel`: Å⁻¹
    - `delta_E_meV_11minus2`: meV
    - `delta_E_meV_2minus1minus1`: meV

Notes: The hidden checker compares the agent's reported numeric quantities and metallicity boolean to the paper's published results, with tolerance bands that account for code/pseudopotential differences. The band_shift_trend must describe how the band binding energies change when Al content increases; the description should be consistent with DFT results but no specific phrasing is required beyond the expected qualitative behaviour.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "total_energy_per_cell_eV",
          "relative_energy_eV"
        ],
        "units": {
          "total_energy_per_cell_eV": "eV",
          "relative_energy_eV": "eV"
        }
      },
      "description": "Total and relative formation energies per 2×2 cell for the four (Au,Al)/Si(111) compositions. The checker compares each relative_energy_eV to a hidden paper-reported reference within an appropriate tolerance and verifies the correct sign (higher/lower)."
    },
    {
      "file": "band_structure_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "metallic",
          "band_shift_trend",
          "spin_splitting"
        ],
        "properties": {
          "metallic": {
            "type": "boolean"
          },
          "band_shift_trend": {
            "type": "string"
          },
          "spin_splitting": {
            "type": "object",
            "required": [
              "delta_k_parallel",
              "delta_E_meV_11minus2",
              "delta_E_meV_2minus1minus1"
            ],
            "properties": {
              "delta_k_parallel": {
                "type": "number"
              },
              "delta_E_meV_11minus2": {
                "type": "number"
              },
              "delta_E_meV_2minus1minus1": {
                "type": "number"
              }
            }
          }
        },
        "units": {
          "delta_k_parallel": "Å⁻¹",
          "delta_E_meV_11minus2": "meV",
          "delta_E_meV_2minus1minus1": "meV"
        }
      },
      "description": "Electronic band summary for the 4Au_3Al composition: metallicity, band shift trend, and spin-splitting parameters. The checker compares metallicity (bool), band_shift_trend description, and spin-splitting parameters to hidden paper-reported references."
    }
  ],
  "notes": "The hidden checker compares the agent's reported numeric quantities and metallicity boolean to the paper's published results, with tolerance bands that account for code/pseudopotential differences. The band_shift_trend must describe how the band binding energies change when Al content increases; the description should be consistent with DFT results but no specific phrasing is required beyond the expected qualitative behaviour."
}
```

## How you are scored
A hidden verifier reads your two output files and independently compares the numeric quantities and metallicity determination against a set of expected reference values. Each stage contributes a fraction of the final reward. The verifier checks whether the relative formation energies lie within an allowed tolerance, whether the metallicity boolean is correct, whether the band‑shift description is consistent, and whether the spin‑splitting parameters (momentum and energy splits) match the references. Simply reporting the expected numbers is not sufficient; the verifier rewards outputs that genuinely result from the required DFT workflow.