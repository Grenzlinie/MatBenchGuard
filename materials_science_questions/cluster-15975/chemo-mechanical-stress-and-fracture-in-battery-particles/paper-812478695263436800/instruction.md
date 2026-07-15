# Modeling Void Growth in Lithium Anodes under Power-Law Creep

## Problem background
In solid-state Li-ion batteries, voids can form at the interface between the Li metal anode and the solid electrolyte during lithium stripping, potentially leading to dendrite growth and short-circuit failure. When a small debonded patch exists along the interface, the Li⁺ flux is blocked over that region, causing a concentration of current at the periphery. The anode material (Li) undergoes power-law creep, and its deformation may either open the void or press the anode against the electrolyte. The central question is whether, under typical stripping currents and creep properties of lithium, these interfacial imperfections can grow into voids.

## Approach
The problem is modelled as an axisymmetric cell consisting of a Li electrode and a single-ion conductor solid electrolyte. A circular debonded patch of radius a is located at the centre of the interface. The electric potential in the electroneutral electrolyte obeys Laplace's equation, with a linearised Butler-Volmer relation governing the interfacial flux j of Li⁺ across the bonded portion of the interface. The flux distribution j(r) is computed numerically for a range of normalised patch radii ā = a/(κZ), where κ is the electrolyte conductivity and Z the interfacial resistance. Once the interfacial flux is known, it serves as a prescribed normal velocity on the bonded part of the Li surface. The Li anode is modelled as an incompressible power-law creeping solid with reference stress σ₀ = 1 MPa, reference strain rate ε̇₀ = 0.01 s⁻¹, and power-law exponent m. The steady-state creep deformation is solved for several m values and both frictionless and sticking contact conditions between electrode and electrolyte. From the velocity field, the normalised centre velocity v₀/v∞ is extracted, along with the flux concentration factor kJ = max(j/j∞) at the patch edge. Finally, the threshold patch diameter at which v₀/v∞ becomes negative is determined.

## Reproduction target
Compute and output three CSV files:
- flux_concentration_factor.csv: columns normalized_patch_radius, kJ. Rows for ā ∈ {0.1, 1, 3, 10, 100}.
- center_velocity.csv: columns normalized_patch_radius, creep_exponent_m, contact_type, v0_div_v_inf. All combinations: ā ∈ {0.1,1,3,10,100}, m ∈ {1,5,20}, contact_type ∈ {'frictionless','sticking'}.
- threshold_patch_diameter.csv: columns creep_exponent_m, threshold_diameter_um. For m=5, determine the smallest ā (and physical diameter = 2·ā·κZ with κZ=20 µm) where v0/v∞ becomes negative; if it never becomes negative for ā ≤ 100, report a value > 2000 µm.

## Assets

- Li power-law creep parameters (σ0=1 MPa, ε̇0=0.01 s⁻¹, m≈5) from LePage et al. (2019) and Masias et al. (2019): 10.1149/2.0521902jes
- LLZO electrolyte conductivity and interfacial resistance (κ=0.4 mS/cm, Z=5 Ω·cm²) from Sharafi et al. (2017): 10.1039/C7TA06767A
- Finite element solver (e.g., FEniCS, deal.II, MOOSE, or custom implementation): https://fenicsproject.org

## Workflow steps

### Step 1: Electrolyte flux simulation
- Role: process
- Action: Solve the Laplace equation for the electric potential in the electrolyte with linearised Butler-Volmer boundary conditions over a range of normalized debonded patch radii ā (0.1, 1, 3, 10, 100). Use electrolyte conductivity κ and interfacial resistance Z from LLZO parameters. Save the interfacial flux distribution j/j∞ as a function of normalized radial position for each ā to a reusable file.
- Evidence: `/app/outputs/flux_distribution.json`

### Step 2: Flux concentration factor extraction
- Role: scored
- Action: From the flux distributions produced in step 1, compute the flux concentration factor kJ = max(j/j∞) at the edge of the debonded patch for each ā. Write results to flux_concentration_factor.csv.
- Output file: `/app/outputs/flux_concentration_factor.csv`
- Format: csv
- Contract: Columns: normalized_patch_radius (float), kJ (float). Rows for each ā ∈ [0.1, 1, 3, 10, 100].
- Scoring: scored by hidden verifier

### Step 3: Creep deformation and center velocity computation
- Role: scored (load-bearing)
- Action: Using the interfacial flux distribution from step 1 as the prescribed normal velocity on the bonded part of the Li electrode surface, simulate the power-law creep deformation of the Li anode (incompressible, power-law exponent m, reference stress σ0=1 MPa, reference strain rate ε̇0=0.01 s⁻¹) for m=1,5,20 and normalized patch radii ā∈[0.1,1,3,10,100]. Perform simulations under both frictionless and sticking contact conditions. For each combination, extract the normalized centre velocity v0/v∞ at the centre of the debonded patch. Save all combinations to center_velocity.csv.
- Output file: `/app/outputs/center_velocity.csv`
- Format: csv
- Contract: Columns: normalized_patch_radius (float), creep_exponent_m (int), contact_type (str: 'frictionless' or 'sticking'), v0_div_v_inf (float). Provide all combinations of parameters as listed.
- Scoring: scored by hidden verifier

### Step 4: Threshold patch diameter for void growth
- Role: scored
- Action: From the center_velocity.csv data, determine the smallest normalized patch radius ā for which v0/v∞ becomes negative for m=5 under each contact condition (if separate thresholds). Convert to physical diameter using scaling factor κZ = 20 μm (diameter = 2·ā·κZ). Report the threshold diameter for m=5. If v0/v∞ remains positive for all ā ≤ 100, report a value >2000 μm to indicate no void growth observed. Write results to threshold_patch_diameter.csv.
- Output file: `/app/outputs/threshold_patch_diameter.csv`
- Format: csv
- Contract: Columns: creep_exponent_m (int), threshold_diameter_um (float). For m=5.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flux_concentration_factor.csv`
- `/app/outputs/center_velocity.csv`
- `/app/outputs/threshold_patch_diameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flux_concentration_factor.csv
- path: `/app/outputs/flux_concentration_factor.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Peak flux concentration factor at the edge of the debonded patch for each normalized patch radius ā.
- schema:
  - `type`: table
  - `required_columns`: `normalized_patch_radius`, `kJ`
  - `units`:
    - `normalized_patch_radius`: dimensionless
    - `kJ`: dimensionless

### center_velocity.csv
- path: `/app/outputs/center_velocity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized centre velocity of the Li electrode surface at the centre of the debonded patch for various creep exponents, normalized patch radii, and contact conditions.
- schema:
  - `type`: table
  - `required_columns`: `normalized_patch_radius`, `creep_exponent_m`, `contact_type`, `v0_div_v_inf`
  - `units`:
    - `normalized_patch_radius`: dimensionless
    - `v0_div_v_inf`: dimensionless

### threshold_patch_diameter.csv
- path: `/app/outputs/threshold_patch_diameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Physical threshold patch diameter for void growth (where centre velocity becomes negative) for m=5.
- schema:
  - `type`: table
  - `required_columns`: `creep_exponent_m`, `threshold_diameter_um`
  - `units`:
    - `threshold_diameter_um`: µm

Notes: All scored outputs are compared to hidden reference values derived from the paper's figures and text, using tolerances appropriate for numerical reproduction (relative tolerance for flux concentration factor and centre velocity; absolute tolerance for threshold diameter).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flux_concentration_factor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "normalized_patch_radius",
          "kJ"
        ],
        "units": {
          "normalized_patch_radius": "dimensionless",
          "kJ": "dimensionless"
        }
      },
      "description": "Peak flux concentration factor at the edge of the debonded patch for each normalized patch radius ā."
    },
    {
      "file": "center_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "normalized_patch_radius",
          "creep_exponent_m",
          "contact_type",
          "v0_div_v_inf"
        ],
        "units": {
          "normalized_patch_radius": "dimensionless",
          "v0_div_v_inf": "dimensionless"
        }
      },
      "description": "Normalized centre velocity of the Li electrode surface at the centre of the debonded patch for various creep exponents, normalized patch radii, and contact conditions."
    },
    {
      "file": "threshold_patch_diameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "creep_exponent_m",
          "threshold_diameter_um"
        ],
        "units": {
          "threshold_diameter_um": "µm"
        }
      },
      "description": "Physical threshold patch diameter for void growth (where centre velocity becomes negative) for m=5."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values derived from the paper's figures and text, using tolerances appropriate for numerical reproduction (relative tolerance for flux concentration factor and centre velocity; absolute tolerance for threshold diameter)."
}
```

## How you are scored
Each scored output file is evaluated by a hidden verifier that compares your submitted values against reference results obtained from a faithful implementation of the same physical model. The verifier checks structural correctness (required columns, data types) and then scores the numeric quantities using appropriate tolerances that account for numerical approximations and solver choices. The final reward is a weighted combination of the scores from the three artifacts, with the centre velocity table (center_velocity.csv) carrying the largest weight. Simply reporting the reference numbers without running the required simulations will result in a very low score.
