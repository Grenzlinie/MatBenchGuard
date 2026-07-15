# Atomistic simulation of defects, Li mobility, and doping in lithium manganese silicate cathode

## Problem background
Li₂MnSiO₄ is a promising cathode material for rechargeable lithium-ion batteries because it uses abundant, low‑cost elements and can, in principle, deliver a high capacity via a two‑electron redox process (Mn²⁺/Mn⁴⁺). However, the intrinsic defect chemistry, lithium‑ion mobility, and feasibility of aliovalent doping to increase the lithium content are not fully understood. The material crystallises in at least two polymorphs—monoclinic (P2₁/n) and orthorhombic (Pmn2₁)—whose defect and transport properties may differ significantly. This task requires atomistic simulations of both polymorphs to compute key quantities that govern electrochemical behaviour: the formation energies of intrinsic point defects, the activation barriers for lithium migration along distinct paths, and the incorporation energies of trivalent cations (Al³⁺ and Ga³⁺) on the three cation sites.

## Approach
The problem is tackled with classical atomistic simulations based on the Born model of solids. The interactions are described by long‑range Coulombic forces, short‑range Buckingham repulsion and dispersion, a harmonic three‑body term that maintains the tetrahedral O–Si–O angles inside SiO₄ units, and a shell model for Mn²⁺ and O²⁻ to account for electronic polarisation. All defect and migration calculations use the Mott–Littleton two‑region scheme as implemented in the open‑source program GULP.

The required interatomic potential parameters and shell model data are listed in the tables below. These parameters are taken from the published literature and are to be used verbatim.

**Table 1(a). Two‑body Buckingham potentials**

| Interaction | A (eV)  | ρ (Å)  | C (eV·Å⁶) |
|-------------|---------|--------|------------|
| Li⁺–O²⁻    | 632.1018| 0.2906 | 0.00       |
| Mn²⁺–O²⁻   | 2601.394| 0.2780 | 0.00       |
| Si⁴⁺–O²⁻   | 1283.91 | 0.32052| 10.66      |
| O²⁻–O²⁻    | 22764.30| 0.1490 | 27.89      |

**Table 1(b). Shell model parameters**

| Species | Y (e)  | K (eV·Å⁻²) |
|---------|--------|------------|
| Li      | 1.000  | 99999      |
| Mn      | 3.420  | 95.00      |
| Si      | 4.000  | 99999      |
| O       | –2.860 | 74.92      |

**Table 1(c). Three‑body potential for O–Si–O**

| Bonds   | k (eV·rad⁻²) |
|---------|-------------|
| O–Si–O | 2.09724     |

The equilibrium O–Si–O angle (θ₀) is the ideal tetrahedral angle.

**Table 6. Dopant‑oxygen potentials (rigid ion) and oxide lattice energies**

| Interaction | A (eV)  | ρ (Å)  | C (eV·Å⁶) | Oxide lattice energy (eV) |
|-------------|---------|--------|------------|---------------------------|
| Al³⁺–O²⁻   | 1114.9  | 0.3118 | 0.00       | –161.00 (per Al₂O₃)     |
| Ga³⁺–O²⁻   | 2901.12 | 0.2742 | 0.00       | –156.60 (per Ga₂O₃)     |

The oxide lattice energies are used when combining defect energies with the corresponding binary oxide to compute dopant incorporation energies.

The simulation proceeds in five main stages:
1. **Build initial structures**: monoclinic (P2₁/n) using the experimentally determined atomic coordinates from Politaev et al. (2007); orthorhombic (Pmn2₁) based on the isostructural Li₂FeSiO₄ positions from Nyten et al. (2006) together with the unit‑cell parameters from Dominko et al. (2006).
2. **Geometry optimisation**: relax both structures fully (lattice parameters and ion positions) under constant pressure using the potentials in Table 1.
3. **Intrinsic defect energies**: compute energies of isolated vacancies (V_Li′, V_Mn″, V_Si‴′, V_O••) and interstitials (Li_i•, Mn_i••, O_i″) with the Mott–Littleton method; then combine them to obtain formation energies for seven intrinsic defect types: Li Frenkel, Mn Frenkel, O Frenkel, full Schottky, Li/Mn anti‑site, lithium‑deficiency oxidation, and oxygen‑excess oxidation.
4. **Lithium migration barriers**: scan the four migration paths identified in the monoclinic polymorph (labelled A, B, C, D) and the two paths in the orthorhombic polymorph (labelled X, Y) to extract the activation energy for each path.
5. **Trivalent dopant incorporation**: compute the energies for substituting Al³⁺ and Ga³⁺ on each cation site (Li, Mn, Si). Charge compensation follows the scheme: Li interstitial for Si‑site substitution; Mn vacancy for Li‑ and Mn‑site substitution. Defect energies are combined with the oxide lattice energies from Table 6 to yield the final incorporation energies.

## Reproduction target
Using the interatomic potentials and shell model given above, run the atomistic simulations to produce the following four JSON files under `/app/outputs`:

- **`lattice_parameters.json`** – the optimised lattice constants: for monoclinic, `a`, `b`, `c`, `β` (in degrees); for orthorhombic, `a`, `b`, `c` (all in Å).
- **`intrinsic_defect_energies.json`** – the formation energies (in eV) of the seven intrinsic defect types for both monoclinic and orthorhombic polymorphs: Li Frenkel, Mn Frenkel, O Frenkel, full Schottky, Li/Mn anti‑site, lithium‑deficiency oxidation, and oxygen‑excess oxidation.
- **`li_migration_energies.json`** – the migration barriers (in eV) for the monoclinic paths A, B, C, D and the orthorhombic paths X, Y.
- **`dopant_incorporation_energies.json`** – the incorporation energies (in eV) for Al³⁺ and Ga³⁺ substituting on the Li, Mn, and Si sites, separately for the monoclinic and orthorhombic structures.

All energies must be expressed in eV. The exact JSON structure for each file is mandated by the output contract section below; you must adhere to the specified keys and numeric types.

## Assets

- Monoclinic Li₂MnSiO₄ crystal structure: https://doi.org/10.1016/j.jssc.2006.10.034
- Orthorhombic Li₂MnSiO₄ initial structure: https://doi.org/10.1039/B601184E
- GULP simulation code: https://gulp.curtin.edu.au

## Workflow steps

### Step 1: Optimize Li₂MnSiO₄ polymorphs and report lattice parameters
- Role: scored
- Action: Build initial crystal structures from the published literature: monoclinic P2₁/n using coordinates from Politaev et al. (2007); orthorhombic Pmn2₁ using atom positions of isostructural Li₂FeSiO₄ from Nyten et al. (2006) and unit‑cell parameters from Dominko et al. (2006). Perform constant‑pressure geometry optimization with the interatomic potentials (Buckingham, three‑body for SiO₄, shell model) provided in the instruction. Output the relaxed lattice parameters (a, b, c, and β for monoclinic; a, b, c for orthorhombic) in a JSON file.
- Output file: `/app/outputs/lattice_parameters.json`
- Format: json
- Contract: {"monoclinic": {"a": float, "b": float, "c": float, "beta": float}, "orthorhombic": {"a": float, "b": float, "c": float}}
- Scoring: scored by hidden verifier

### Step 2: Calculate isolated point defect energies
- Role: process
- Action: Using the relaxed structures, compute energies of isolated vacancies and interstitials (V_Li′, V_Mn″, V_Si‴′, V_O••, Li_i•, Mn_i••, O_i″) via the Mott‑Littleton method. Save the raw defect energies as intermediate evidence for later combination.
- Evidence: `/app/outputs/isolated_defect_energies.json`

### Step 3: Compute intrinsic defect formation energies
- Role: scored
- Action: Combine the isolated defect energies from the previous step using the defect reaction equations (Li Frenkel, Mn Frenkel, O Frenkel, full Schottky, Li/Mn anti‑site, Li deficiency oxidation, oxygen excess oxidation). Compute the formation energies and write them to a JSON file.
- Output file: `/app/outputs/intrinsic_defect_energies.json`
- Format: json
- Contract: {"monoclinic": {"Li_Frenkel": float, "Mn_Frenkel": float, "O_Frenkel": float, "Schottky": float, "LiMn_antisite": float, "Li_deficiency_oxidation": float, "oxygen_excess_oxidation": float}, "orthorhombic": {"Li_Frenkel": float, "Mn_Frenkel": float, "O_Frenkel": float, "Schottky": float, "LiMn_antisite": float, "Li_deficiency_oxidation": float, "oxygen_excess_oxidation": float}}
- Scoring: scored by hidden verifier

### Step 4: Compute lithium‑ion migration energies
- Role: scored (load-bearing)
- Action: Determine the activation energies along the Li‑ion migration paths labelled A, B, C, D for the monoclinic polymorph and X, Y for the orthorhombic polymorph. Report the barrier energies in a JSON file.
- Output file: `/app/outputs/li_migration_energies.json`
- Format: json
- Contract: {"monoclinic": {"path_A": float, "path_B": float, "path_C": float, "path_D": float}, "orthorhombic": {"path_X": float, "path_Y": float}}
- Scoring: scored by hidden verifier

### Step 5: Compute trivalent dopant incorporation energies
- Role: scored (load-bearing)
- Action: For Al³⁺ and Ga³⁺ substitution on the Li, Mn, and Si sites, use the appropriate charge compensation (Li interstitial for Si site; Mn vacancy for Li and Mn sites). Run defect calculations with the dopant oxide potentials and combine with oxide lattice energies using the dopant reaction equations. Compute the incorporation energies and write to a JSON file.
- Output file: `/app/outputs/dopant_incorporation_energies.json`
- Format: json
- Contract: {"monoclinic": {"Al": {"Li_site": float, "Mn_site": float, "Si_site": float}, "Ga": {"Li_site": float, "Mn_site": float, "Si_site": float}}, "orthorhombic": {"Al": {"Li_site": float, "Mn_site": float, "Si_site": float}, "Ga": {"Li_site": float, "Mn_site": float, "Si_site": float}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.json`
- `/app/outputs/intrinsic_defect_energies.json`
- `/app/outputs/li_migration_energies.json`
- `/app/outputs/dopant_incorporation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.json
- path: `/app/outputs/lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters for both polymorphs; compared to paper values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `monoclinic`:
      - `a`: float
      - `b`: float
      - `c`: float
      - `beta`: float
    - `orthorhombic`:
      - `a`: float
      - `b`: float
      - `c`: float

### intrinsic_defect_energies.json
- path: `/app/outputs/intrinsic_defect_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of seven intrinsic defect types; compared to paper values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `monoclinic`:
      - `Li_Frenkel`: float
      - `Mn_Frenkel`: float
      - `O_Frenkel`: float
      - `Schottky`: float
      - `LiMn_antisite`: float
      - `Li_deficiency_oxidation`: float
      - `oxygen_excess_oxidation`: float
    - `orthorhombic`:
      - `Li_Frenkel`: float
      - `Mn_Frenkel`: float
      - `O_Frenkel`: float
      - `Schottky`: float
      - `LiMn_antisite`: float
      - `Li_deficiency_oxidation`: float
      - `oxygen_excess_oxidation`: float

### li_migration_energies.json
- path: `/app/outputs/li_migration_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Li-ion migration barriers for six pathways; compared to paper values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `monoclinic`:
      - `path_A`: float
      - `path_B`: float
      - `path_C`: float
      - `path_D`: float
    - `orthorhombic`:
      - `path_X`: float
      - `path_Y`: float

### dopant_incorporation_energies.json
- path: `/app/outputs/dopant_incorporation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Trivalent dopant incorporation energies; compared to paper values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `monoclinic`:
      - `Al`:
        - `Li_site`: float
        - `Mn_site`: float
        - `Si_site`: float
      - `Ga`:
        - `Li_site`: float
        - `Mn_site`: float
        - `Si_site`: float
    - `orthorhombic`:
      - `Al`:
        - `Li_site`: float
        - `Mn_site`: float
        - `Si_site`: float
      - `Ga`:
        - `Li_site`: float
        - `Mn_site`: float
        - `Si_site`: float

Notes: All energies are in eV. Tolerances are hidden; they are set to absorb legitimate toolchain spread while still requiring a genuine re-run.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monoclinic": {
            "a": "float",
            "b": "float",
            "c": "float",
            "beta": "float"
          },
          "orthorhombic": {
            "a": "float",
            "b": "float",
            "c": "float"
          }
        }
      },
      "description": "Optimized lattice parameters for both polymorphs; compared to paper values with tolerances."
    },
    {
      "file": "intrinsic_defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monoclinic": {
            "Li_Frenkel": "float",
            "Mn_Frenkel": "float",
            "O_Frenkel": "float",
            "Schottky": "float",
            "LiMn_antisite": "float",
            "Li_deficiency_oxidation": "float",
            "oxygen_excess_oxidation": "float"
          },
          "orthorhombic": {
            "Li_Frenkel": "float",
            "Mn_Frenkel": "float",
            "O_Frenkel": "float",
            "Schottky": "float",
            "LiMn_antisite": "float",
            "Li_deficiency_oxidation": "float",
            "oxygen_excess_oxidation": "float"
          }
        }
      },
      "description": "Formation energies of seven intrinsic defect types; compared to paper values with tolerances."
    },
    {
      "file": "li_migration_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monoclinic": {
            "path_A": "float",
            "path_B": "float",
            "path_C": "float",
            "path_D": "float"
          },
          "orthorhombic": {
            "path_X": "float",
            "path_Y": "float"
          }
        }
      },
      "description": "Li-ion migration barriers for six pathways; compared to paper values with tolerances."
    },
    {
      "file": "dopant_incorporation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monoclinic": {
            "Al": {
              "Li_site": "float",
              "Mn_site": "float",
              "Si_site": "float"
            },
            "Ga": {
              "Li_site": "float",
              "Mn_site": "float",
              "Si_site": "float"
            }
          },
          "orthorhombic": {
            "Al": {
              "Li_site": "float",
              "Mn_site": "float",
              "Si_site": "float"
            },
            "Ga": {
              "Li_site": "float",
              "Mn_site": "float",
              "Si_site": "float"
            }
          }
        }
      },
      "description": "Trivalent dopant incorporation energies; compared to paper values with tolerances."
    }
  ],
  "notes": "All energies are in eV. Tolerances are hidden; they are set to absorb legitimate toolchain spread while still requiring a genuine re-run."
}
```

## How you are scored
A hidden verifier examines each of the four scored output files. It compares every reported numerical value against the corresponding reference values from the original study, using pre‑established tolerances that allow for legitimate differences arising from implementation details (compiler, numerical settings, etc.). The verifier also checks that certain expected trends and relative orderings among the quantities are satisfied (for example, the relative ranking of formation energies or the comparison of migration barriers between polymorphs). Each output file contributes a fixed, predetermined weight to the total reward. Partial credit may be awarded if some, but not all, quantities are within tolerance. To obtain full credit you must produce all four files with values that pass the numeric comparisons and the structural trend checks. The reference values and tolerances are not disclosed; therefore, you must perform the genuine atomistic simulation workflow rather than guessing or copying numbers from literature.
