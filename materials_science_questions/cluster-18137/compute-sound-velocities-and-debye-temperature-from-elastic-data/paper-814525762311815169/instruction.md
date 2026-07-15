# DFT Investigation of Doping Effects on Mechanical, Thermodynamic, and Electronic Properties of AuSn₄-Based Intermetallics

## Problem background
Gold embrittlement in solder joints is often attributed to the formation of (Au,Ni)Sn₄, (Au,Pd)Sn₄ and (Au,Pd,Ni)Sn₄ intermetallic layers at the pad/solder interface. Understanding how substitutional Ni and Pd doping alters the mechanical, thermodynamic, and electronic properties of the parent AuSn₄ compound is essential for assessing the reliability of electronic packaging. This task employs first‑principles density‑functional theory to compute key ground‑state properties of pure AuSn₄ and five doped variants, providing a systematic comparison of structural stability, elastic response, sound velocities, Debye temperature, thermal conductivity, and electronic density‑of‑states across the compositional series.

## Approach
The computational approach uses plane‑wave pseudopotential DFT with the PBE exchange‑correlation functional. Starting from the experimental orthorhombic AuSn₄ crystal structure (space group Aba2), six model compositions are constructed: pure AuSn₄, Au₀.₇₅Ni₀.₂₅Sn₄, Au₀.₅Ni₀.₅Sn₄, Au₀.₇₅Pd₀.₂₅Sn₄, Au₀.₅Pd₀.₅Sn₄, and the codoped Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄, with dopant atoms placed at specific Wyckoff positions as detailed in the workflow steps. For each composition a full geometry relaxation is performed to obtain equilibrium lattice constants and total energy. Reference energies are also computed for the elemental phases fcc Au, fcc Ni, fcc Pd, and β‑Sn. Single‑crystal elastic constants are extracted via the finite‑strain method, and polycrystalline elastic moduli (bulk, shear, Young's, Poisson's ratio, and hardness) are derived using the Voigt–Reuss–Hill averaging scheme. Sound velocities, Debye temperature, and minimum thermal conductivity are subsequently evaluated from the relaxed density and elastic moduli. The total electronic density of states is calculated, and the integrated DOS at the Fermi level, N(Ef), is recorded. The entire procedure is repeated independently for each of the six compositions, and all numerical results are assembled into a single structured CSV file.

## Reproduction target
Using an open‑source DFT code capable of PBE calculations, compute the following quantities for each of the six compositions listed above: optimized lattice constants a, b, c and cell volume V; formation energy ΔH per atom; the nine independent single‑crystal elastic constants C₁₁–C₂₃; polycrystalline bulk modulus K, shear modulus G, Young's modulus E, Poisson's ratio v, Zener anisotropy factor A_Z, K/G ratio, and hardness H; density ρ, transverse, longitudinal, and average sound velocities vt, vl, vm, and Debye temperature θD; minimum thermal conductivity k_min; and integrated DOS at the Fermi level N_Ef. Write a single CSV file named `all_properties.csv` under `/app/outputs/` with one row per composition and the exact column schema specified in the output contract. The file must be produced by genuinely executing the DFT workflow; do not merely copy values from a publication.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency library or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python with numpy (for post‑processing): numpy

## Workflow steps

### Step 1: Structure construction
- Role: process
- Action: Build initial crystal structures for the six compositions: AuSn₄, Au₀.₇₅Ni₀.₂₅Sn₄, Au₀.₅Ni₀.₅Sn₄, Au₀.₇₅Pd₀.₂₅Sn₄, Au₀.₅Pd₀.₅Sn₄, and Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄. Use the orthorhombic PdSn₄ prototype (space group Aba2) with experimental lattice constants a=6.51, b=6.52, c=11.71 Å as starting point, and substitute Au atoms by Ni/Pd at the specific sites required by the paper (Au₂ for x=0.25; Au₁+Au₄ for x=0.5; for codoped: Ni at Au₁, Pd at Au₄). Generate input files suitable for the subsequent DFT relaxation.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT relaxation and total energy
- Role: process
- Action: For each structure, perform spin‑polarized DFT geometry relaxation using the PBE functional (k‑mesh approximately 2×4×4 or finer, plane‑wave cutoff at least 360 eV, total‑energy convergence ≤ 5×10⁻⁶ eV/atom) to obtain optimized lattice constants and total energy. Also compute reference total energies for face‑centered‑cubic Au, fcc Ni, fcc Pd, and β‑Sn.
- Evidence: `/app/outputs/relax.log`

### Step 3: Elastic constants calculation
- Role: process
- Action: Using the relaxed structures, apply finite‑strain method (strain ≤ 2%) within DFT to obtain the nine independent single‑crystal elastic constants C₁₁, C₂₂, C₃₃, C₄₄, C₅₅, C₆₆, C₁₂, C₁₃, and C₂₃ for each composition.
- Evidence: `/app/outputs/elastic.log`

### Step 4: Electronic DOS analysis
- Role: process
- Action: For each relaxed structure, compute total density of states (DOS) and extract the integrated DOS at the Fermi level N(Ef).
- Evidence: `/app/outputs/dos.log`

### Step 5: Compile all computed properties
- Role: scored (load-bearing)
- Action: From the data obtained in the previous steps, calculate for each composition: (1) final lattice constants a, b, c and cell volume V; (2) formation energy ΔH per atom using total energies and elemental references; (3) single‑crystal elastic constants; (4) polycrystalline elastic moduli (bulk modulus K, shear modulus G, Young’s modulus E, Poisson’s ratio v, Zener anisotropy factor A_Z, K/G ratio, and hardness H) via VRH averaging; (5) density ρ, transverse vt, longitudinal vl, and average vm sound velocities, and Debye temperature θD; (6) minimum thermal conductivity k_min via the Cahill‑Pohl model; (7) integrated DOS at Fermi level N_Ef. Write all values to a CSV file with the required schema.
- Output file: `/app/outputs/all_properties.csv`
- Format: csv
- Contract: CSV with one row per composition (6 rows). Columns: composition (string), a (Å), b (Å), c (Å), V (Å³), Delta_H (kJ/mol atoms), C11 (GPa), C22 (GPa), C33 (GPa), C44 (GPa), C55 (GPa), C66 (GPa), C12 (GPa), C13 (GPa), C23 (GPa), K (GPa), G (GPa), E (GPa), v (dimensionless), A_Z (dimensionless), K_over_G (dimensionless), H (GPa), rho (kg/m³), vt (m/s), vl (m/s), vm (m/s), theta_D (K), k_min (W/m·K), N_Ef (electrons/eV). All numeric values as floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/all_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### all_properties.csv
- path: `/app/outputs/all_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Compiled computed properties for the six AuSn₄‑based intermetallic compounds: pure AuSn₄, Au₀.₇₅Ni₀.₂₅Sn₄, Au₀.₅Ni₀.₅Sn₄, Au₀.₇₅Pd₀.₂₅Sn₄, Au₀.₅Pd₀.₅Sn₄, and Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄. Contains lattice constants, formation energy, single‑crystal elastic constants, polycrystalline moduli, sound velocities, Debye temperature, minimum thermal conductivity, and integrated DOS at the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `a`, `b`, `c`, `V`, `Delta_H`, `C11`, `C22`, `C33`, `C44`, `C55`, `C66`, `C12`, `C13`, `C23`, `K`, `G`, `E`, `v`, `A_Z`, `K_over_G`, `H`, `rho`, `vt`, `vl`, `vm`, `theta_D`, `k_min`, `N_Ef`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `V`: Å³
    - `Delta_H`: kJ/mol atoms
    - `C11`: GPa
    - `C22`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C23`: GPa
    - `K`: GPa
    - `G`: GPa
    - `E`: GPa
    - `v`: dimensionless
    - `A_Z`: dimensionless
    - `K_over_G`: dimensionless
    - `H`: GPa
    - `rho`: kg/m³
    - `vt`: m/s
    - `vl`: m/s
    - `vm`: m/s
    - `theta_D`: K
    - `k_min`: W/m·K
    - `N_Ef`: electrons/eV

Notes: Each property is scored by comparing the reported value to a hidden paper‑derived reference with a per‑property relative tolerance; tolerances are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "all_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "a",
          "b",
          "c",
          "V",
          "Delta_H",
          "C11",
          "C22",
          "C33",
          "C44",
          "C55",
          "C66",
          "C12",
          "C13",
          "C23",
          "K",
          "G",
          "E",
          "v",
          "A_Z",
          "K_over_G",
          "H",
          "rho",
          "vt",
          "vl",
          "vm",
          "theta_D",
          "k_min",
          "N_Ef"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "V": "Å³",
          "Delta_H": "kJ/mol atoms",
          "C11": "GPa",
          "C22": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C23": "GPa",
          "K": "GPa",
          "G": "GPa",
          "E": "GPa",
          "v": "dimensionless",
          "A_Z": "dimensionless",
          "K_over_G": "dimensionless",
          "H": "GPa",
          "rho": "kg/m³",
          "vt": "m/s",
          "vl": "m/s",
          "vm": "m/s",
          "theta_D": "K",
          "k_min": "W/m·K",
          "N_Ef": "electrons/eV"
        }
      },
      "description": "Compiled computed properties for the six AuSn₄‑based intermetallic compounds: pure AuSn₄, Au₀.₇₅Ni₀.₂₅Sn₄, Au₀.₅Ni₀.₅Sn₄, Au₀.₇₅Pd₀.₂₅Sn₄, Au₀.₅Pd₀.₅Sn₄, and Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄. Contains lattice constants, formation energy, single‑crystal elastic constants, polycrystalline moduli, sound velocities, Debye temperature, minimum thermal conductivity, and integrated DOS at the Fermi level."
    }
  ],
  "notes": "Each property is scored by comparing the reported value to a hidden paper‑derived reference with a per‑property relative tolerance; tolerances are not disclosed to the agent."
}
```

## How you are scored
Your submitted `all_properties.csv` will be evaluated by a hidden automated verifier. For each composition, the verifier compares every numeric property in the file against hidden reference values using per‑property relative tolerances. Additionally, the verifier checks whether certain qualitative physical trends that are expected to hold among the compositions (e.g., monotonic variation with doping level) are satisfied by your reported numbers. The overall reward is a weighted average of the scores across all checked properties. Producing values that are physically consistent and fall within the undisclosed tolerances yields the highest score; the tolerances are chosen to accommodate legitimate variation between different DFT implementations while requiring a faithful reproduction of the computational procedure.
