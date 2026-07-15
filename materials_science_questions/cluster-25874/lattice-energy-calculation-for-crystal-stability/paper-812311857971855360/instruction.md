# Lattice Energy Minimization of Maleic Hydrazide Crystal Packing Alternatives

## Problem background
Maleic hydrazide (1,2-dihydropyridazine-3,6-dione) crystallizes in a triclinic structure with hydrogen-bonded layers. In the observed structure, molecules are linked by O–H···O and N–H···O hydrogen bonds. An alternative layer packing based on a chain motif (type II) can be constructed from the same molecules, where O–H···N and N–H···O hydrogen bonds would replace the O–H···O bonds. The alternative layer packs well in two dimensions, so the question arises: why is the observed structure preferred? Is it because the O–H···O bond is intrinsically stronger, because the van der Waals packing of the observed layer is more efficient, or because the layers stack more favourably? A lattice-energy analysis can answer this question by computing the total lattice energy and its decomposition into van der Waals, Coulombic, and hydrogen-bond contributions for both the observed crystal structure and a representative alternative triclinic packing derived from the chain-motif layer.

## Approach
Use the empirical force field of Momany et al. (J. Chem. Phys. 43, 5136, 1965) to compute the lattice energy as:

U = Σ [ –A r⁻⁶ + B r⁻¹² + (qᵢqⱼ / D) r⁻¹ – G r⁻¹⁰ ]

with dielectric constant D = 2.0. The Lennard-Jones parameters A and B apply to all atom pairs; the hydrogen-bond term G is non‑zero only for selected donor–acceptor pairs. Partial atomic charges are taken from a CNDO/2 calculation (provided in the paper’s Figure 3). The molecule is treated as a rigid planar body, and the energy is minimized with respect to the six triclinic unit-cell parameters and the six rigid-body molecular parameters (translations and rotations). The calculation is performed for two structures:
- The experimentally observed triclinic structure (space group P 1̅) with initial cell parameters a=5.83 Å, b=5.78 Å, c=7.31 Å, α=79.0°, β=99.5°, γ=107.2°.
- One representative alternative triclinic structure built from the chain-motif II layer (a=9.415 Å, b=7.935 Å, γ=86.3°), stacked with α=90°, β=90°, and a c‑axis length that gives the same volume per molecule as the observed structure (≈114.5 Å³/molecule). For this alternative, the O–H···N hydrogen bonds are treated using the N–H···O parameters.

For each structure the final minimized cell parameters are recorded, and the total lattice energy is decomposed into van der Waals (A,B terms), Coulombic (qᵢqⱼ term), and hydrogen‑bond (G term) contributions.

## Reproduction target
Produce three JSON files under `/app/outputs`:
1. `observed_lattice_energy.json` – total, van_der_Waals, Coulombic, and hydrogen_bond energies (in kJ/mol) for the minimized observed structure.
2. `alternative_lattice_energy.json` – the same four energy components for the minimized alternative triclinic structure.
3. `minimized_cell_parameters.json` – the final unit-cell parameters (a, b, c in Å; α, β, γ in degrees) for both the observed and alternative structures after energy minimization.

The hidden verifier will read these files and evaluate them against expected reference values and physical requirements. A correct submission will reproduce energy components and cell parameters that are internally consistent and that faithfully reflect the lattice-energy minimization of the two crystal packings.

## Assets

- Momany et al. potential parameters (J. Chem. Phys. 43, 5136, 1965): https://doi.org/10.1063/1.1692863
- Crystal structure of maleic hydrazide (Cradwick, J. Chem. Soc. Perkin Trans. 2, 1386, 1976): https://doi.org/10.1039/P29760001386

## Workflow steps

### Step 1: Prepare observed crystal structure
- Role: process
- Action: Obtain the atomic coordinates of maleic hydrazide from the Cradwick (1976) crystal structure via the provided DOI. Construct the rigid planar molecule using the non‑hydrogen bond lengths and angles from that structure, and place hydrogen atoms at the bond lengths recommended by Momany et al. (1965). Build a triclinic unit cell with space group P‑1, Z=2, cell dimensions a=5.83, b=5.78, c=7.31 Å, α=79.0°, β=99.5°, γ=107.2°, placing the molecule in the asymmetric unit according to the published fractional coordinates.
- Evidence: `/app/outputs/observed_initial.pdb`

### Step 2: Compute lattice energy of observed structure
- Role: scored
- Action: Implement the lattice energy function U = Σ[-A r^{-6} + B r^{-12} + (q_i q_j / D) r^{-1} - G r^{-10}] with D=2.0, using the Lennard‑Jones and hydrogen‑bond parameters from Momany et al. (1965). Apply the partial atomic charges given in Figure 3 of the analyzed paper. Sum over all atom pairs within 6 Å. Minimize the energy with respect to the six triclinic cell parameters and the six rigid‑body molecular parameters. Record the total lattice energy and its decomposition into van der Waals, Coulombic, and hydrogen‑bond contributions at the minimized geometry.
- Output file: `/app/outputs/observed_lattice_energy.json`
- Format: json
- Contract: {"type":"object","required":["total","van_der_Waals","Coulombic","hydrogen_bond"],"properties":{"total":{"type":"number","description":"total lattice energy in kJ/mol"},"van_der_Waals":{"type":"number","description":"van der Waals component in kJ/mol"},"Coulombic":{"type":"number","description":"Coulombic component in kJ/mol"},"hydrogen_bond":{"type":"number","description":"hydrogen bond component in kJ/mol"}}}
- Scoring: scored by hidden verifier

### Step 3: Construct alternative triclinic structure based on chain motif II
- Role: process
- Action: From the observed layer arrangement, derive the 2D hydrogen‑bond layer corresponding to chain motif II by graphically translating alternate rows of molecules. The resulting planar layer has cell parameters a=9.415, b=7.935 Å, γ=86.3°. Construct a triclinic stacking by setting α=90°, β=90°, and choose the c‑axis length so that the volume per molecule equals that of the observed structure (≈114.5 Å³/molecule). Build the initial triclinic unit cell with these parameters.
- Evidence: `/app/outputs/alternative_initial.pdb`

### Step 4: Compute lattice energy of alternative triclinic structure
- Role: scored (load-bearing)
- Action: Using the same energy function and parameters as in Step 2, but substituting the N—H...O hydrogen‑bond parameters for the O—H...N interactions, minimize the energy of the alternative triclinic structure with respect to all twelve lattice and molecular parameters. Record the total lattice energy and the three component energies at the minimum.
- Output file: `/app/outputs/alternative_lattice_energy.json`
- Format: json
- Contract: {"type":"object","required":["total","van_der_Waals","Coulombic","hydrogen_bond"],"properties":{"total":{"type":"number"},"van_der_Waals":{"type":"number"},"Coulombic":{"type":"number"},"hydrogen_bond":{"type":"number"}}}
- Scoring: scored by hidden verifier

### Step 5: Report minimized cell parameters
- Role: scored
- Action: After completing the minimizations in Steps 2 and 4, collect the final cell parameters (a,b,c in Å, α,β,γ in degrees) for both the observed and the alternative structures. Write them to a single JSON file.
- Output file: `/app/outputs/minimized_cell_parameters.json`
- Format: json
- Contract: {"type":"object","required":["observed","alternative"],"properties":{"observed":{"type":"object","required":["a","b","c","alpha","beta","gamma"],"properties":{"a":{"type":"number","description":"a in Angstrom"},"b":{"type":"number"},"c":{"type":"number"},"alpha":{"type":"number","description":"alpha in degrees"},"beta":{"type":"number"},"gamma":{"type":"number"}}},"alternative":{"type":"object","required":["a","b","c","alpha","beta","gamma"],"properties":{"a":{"type":"number"},"b":{"type":"number"},"c":{"type":"number"},"alpha":{"type":"number"},"beta":{"type":"number"},"gamma":{"type":"number"}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/observed_lattice_energy.json`
- `/app/outputs/alternative_lattice_energy.json`
- `/app/outputs/minimized_cell_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### observed_lattice_energy.json
- path: `/app/outputs/observed_lattice_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice energy and component breakdown of the observed crystal structure after minimization.
- schema:
  - `type`: object
  - `required`: `total`, `van_der_Waals`, `Coulombic`, `hydrogen_bond`
  - `properties`:
    - `total`:
      - `type`: number
      - `description`: total lattice energy in kJ/mol
    - `van_der_Waals`:
      - `type`: number
      - `description`: van der Waals component in kJ/mol
    - `Coulombic`:
      - `type`: number
      - `description`: Coulombic component in kJ/mol
    - `hydrogen_bond`:
      - `type`: number
      - `description`: hydrogen bond component in kJ/mol

### alternative_lattice_energy.json
- path: `/app/outputs/alternative_lattice_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice energy and component breakdown of the alternative triclinic structure after minimization.
- schema:
  - `type`: object
  - `required`: `total`, `van_der_Waals`, `Coulombic`, `hydrogen_bond`
  - `properties`:
    - `total`:
      - `type`: number
    - `van_der_Waals`:
      - `type`: number
    - `Coulombic`:
      - `type`: number
    - `hydrogen_bond`:
      - `type`: number

### minimized_cell_parameters.json
- path: `/app/outputs/minimized_cell_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Minimized cell parameters for the observed and alternative triclinic structures.
- schema:
  - `type`: object
  - `required`: `observed`, `alternative`
  - `properties`:
    - `observed`:
      - `type`: object
      - `required`: `a`, `b`, `c`, `alpha`, `beta`, `gamma`
      - `properties`:
        - `a`:
          - `type`: number
          - `description`: a axis length in Å
        - `b`:
          - `type`: number
        - `c`:
          - `type`: number
        - `alpha`:
          - `type`: number
          - `description`: alpha angle in degrees
        - `beta`:
          - `type`: number
        - `gamma`:
          - `type`: number
    - `alternative`:
      - `type`: object
      - `required`: `a`, `b`, `c`, `alpha`, `beta`, `gamma`
      - `properties`:
        - `a`:
          - `type`: number
        - `b`:
          - `type`: number
        - `c`:
          - `type`: number
        - `alpha`:
          - `type`: number
        - `beta`:
          - `type`: number
        - `gamma`:
          - `type`: number

Notes: The checker will compare the reported values against hidden reference values from the literature, apply tolerances, and verify that the observed total energy is more negative than the alternative and that the observed hydrogen‑bond term is substantially more stabilizing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "observed_lattice_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "total",
          "van_der_Waals",
          "Coulombic",
          "hydrogen_bond"
        ],
        "properties": {
          "total": {
            "type": "number",
            "description": "total lattice energy in kJ/mol"
          },
          "van_der_Waals": {
            "type": "number",
            "description": "van der Waals component in kJ/mol"
          },
          "Coulombic": {
            "type": "number",
            "description": "Coulombic component in kJ/mol"
          },
          "hydrogen_bond": {
            "type": "number",
            "description": "hydrogen bond component in kJ/mol"
          }
        }
      },
      "description": "Lattice energy and component breakdown of the observed crystal structure after minimization."
    },
    {
      "file": "alternative_lattice_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "total",
          "van_der_Waals",
          "Coulombic",
          "hydrogen_bond"
        ],
        "properties": {
          "total": {
            "type": "number"
          },
          "van_der_Waals": {
            "type": "number"
          },
          "Coulombic": {
            "type": "number"
          },
          "hydrogen_bond": {
            "type": "number"
          }
        }
      },
      "description": "Lattice energy and component breakdown of the alternative triclinic structure after minimization."
    },
    {
      "file": "minimized_cell_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "observed",
          "alternative"
        ],
        "properties": {
          "observed": {
            "type": "object",
            "required": [
              "a",
              "b",
              "c",
              "alpha",
              "beta",
              "gamma"
            ],
            "properties": {
              "a": {
                "type": "number",
                "description": "a axis length in Å"
              },
              "b": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "alpha": {
                "type": "number",
                "description": "alpha angle in degrees"
              },
              "beta": {
                "type": "number"
              },
              "gamma": {
                "type": "number"
              }
            }
          },
          "alternative": {
            "type": "object",
            "required": [
              "a",
              "b",
              "c",
              "alpha",
              "beta",
              "gamma"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "b": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "alpha": {
                "type": "number"
              },
              "beta": {
                "type": "number"
              },
              "gamma": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Minimized cell parameters for the observed and alternative triclinic structures."
    }
  ],
  "notes": "The checker will compare the reported values against hidden reference values from the literature, apply tolerances, and verify that the observed total energy is more negative than the alternative and that the observed hydrogen‑bond term is substantially more stabilizing."
}
```

## How you are scored
Each scored artifact (`observed_lattice_energy.json`, `alternative_lattice_energy.json`, `minimized_cell_parameters.json`) is assessed independently by a hidden verifier. The verifier checks that the reported total and component energies fall within accepted tolerances and obey required trends (e.g., the relative stability and the balance of van der Waals, Coulombic, and hydrogen‑bond contributions). Cell parameters are evaluated for consistency with the energy‑minimized geometries. A weighted combination of the per‑artifact scores yields the final reward (a float between 0 and 1). The verifier does not disclose the reference values or tolerances; simply reporting the paper’s numbers is not enough – your implementation must accurately compute the energies via the prescribed force field and minimization procedure.
