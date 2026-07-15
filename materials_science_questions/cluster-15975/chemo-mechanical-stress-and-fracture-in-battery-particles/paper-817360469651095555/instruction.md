# KMC and FEM Simulations of Secondary Phases in LLZO Solid Electrolytes

## Problem background
Solid-state batteries using garnet-type LLZO (Li₇La₃Zr₂O₁₂) electrolytes suffer from filament formation and fracture that are linked to microstructural heterogeneity. LLZO can crystallise in two closely related cubic space groups (I-43d, space group 220, and Ia-3d, space group 230) that differ in their local Li coordination environments and, as a consequence, in ion‑migration barriers. This task investigates, through a two‑stage computational workflow, how the presence of a secondary cubic phase affects Li‑ion transport, mechanical stress, and electric potential within the electrolyte. The goal is to produce spatial fields (Li occupancy, hydrostatic stress, electric potential) that capture these effects and to evaluate the resulting structural trends.

## Approach
The workflow consists of two complementary simulations. (1) A **kinetic Monte Carlo (KMC)** model for Li‑ion hops on a 60 nm × 60 nm grid that contains a central 7 nm × 60 nm strip representing the secondary phase. Hopping rates follow an Arrhenius form with a migration‑barrier offset of 0.06 eV between the bulk and secondary phases. Starting from a uniform 2 % occupancy, the evolution is driven by 4 × 10¹⁰ individual migration events, and the final normalised Li occupancy (i/i₀) is recorded at every grid point. (2) A **finite‑element method (FEM)** simulation on an approximately 600 μm × 600 μm domain containing three circular secondary‑phase inclusions (diameter 60 μm). Linear elasticity is solved with Young’s moduli of 161 GPa (bulk) and 156 GPa (secondary), Poisson ratio 0.27, under 1 MPa external pressure on top and bottom boundaries. Electrochemical conduction ( ∇·(k ∇ φ) = 0) is solved with ionic conductivities of 1 mS cm⁻¹ (bulk) and 0.3 mS cm⁻¹ (secondary), Butler‑Volmer kinetics at the Li‑electrode interface, and an applied current density of 0.5 mA cm⁻² at the top boundary. The outputs are the hydrostatic stress (MPa) and electric potential (V) fields over the whole domain. Both stages use only publicly described setups and open‑source tools; the agent builds the models from the problem specification provided in the workflow steps.

## Reproduction target
Implement both computational stages according to the ordered workflow steps below and write the following two files to `/app/outputs`:  

1. `kmc_occupancy.csv` – the final normalised Li occupancy (i/i₀) on the full 60 nm × 60 nm grid after 4 × 10¹⁰ KMC events.  
2. `fem_stress_potential.csv` – the hydrostatic stress (MPa) and electric potential (V) fields from the finite‑element simulation covering the entire ≈600 × 600 μm domain.  

A hidden verifier will subsequently read these files and check for structural trends (e.g., spatial contrasts between the secondary‑phase regions and the surrounding bulk) without requiring exact numeric agreement with any reference. The objective is to produce fields that faithfully reflect the coupling of ion transport, mechanics, and electrochemistry in the specified two‑phase system.

## Assets

- FEniCS Finite Element Library: https://fenicsproject.org/

## Workflow steps

### Step 1: Kinetic Monte Carlo simulation of Li-ion transport
- Role: scored
- Action: Implement a KMC model on a 60 nm × 60 nm grid with a central 7 nm × 60 nm secondary-phase strip (foreign phase, higher migration barrier). Define Arrhenius rate constants using a barrier offset of 0.06 eV between the bulk (lower barrier) and secondary phase. Set initial Li occupancy to 2% everywhere. Evolve the system until 4×10^10 migration events have been completed. Record the final normalized occupancy field i/i0 for every grid point.
- Output file: `/app/outputs/kmc_occupancy.csv`
- Format: csv
- Contract: Comma-separated file with header. Columns: x (nm, float), y (nm, float), occupancy (dimensionless float, normalized i/i0). The grid covers the full 60×60 nm domain.
- Scoring: scored by hidden verifier

### Step 2: Finite element mechanical and electrochemical simulation
- Role: scored (load-bearing)
- Action: Construct a 2D FEM domain of approximately 600×600 μm containing three circular secondary-phase inclusions of diameter 60 μm centered at (480,420), (330,150), (120,330) μm. Solve linear elasticity (Young’s moduli 161 GPa for bulk LLZO, 156 GPa for secondary phase; Poisson’s ratio 0.27 for both) under an applied external pressure of 1 MPa on top/bottom boundaries and zero normal displacement on left/right. Solve electrochemical conduction ∇·(k ∇ φ)=0 using ionic conductivities 1 mS/cm (bulk) and 0.3 mS/cm (secondary) with Butler-Volmer kinetics at the Li-electrode interface and an applied current density of 0.5 mA/cm² at the top boundary; insulating conditions on lateral boundaries. Output the hydrostatic stress (MPa) and electric potential (V) on a regular grid or mesh nodes covering the whole domain.
- Output file: `/app/outputs/fem_stress_potential.csv`
- Format: csv
- Contract: Comma-separated file with header. Columns: x (μm, float), y (μm, float), hydrostatic_stress (MPa, float), electric_potential (V, float). Data points cover the entire ≈600×600 μm domain.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kmc_occupancy.csv`
- `/app/outputs/fem_stress_potential.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kmc_occupancy.csv
- path: `/app/outputs/kmc_occupancy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized Li-ion occupancy after KMC simulation. The checker will verify that the average occupancy inside the secondary-phase strip (central y region of width 7 nm) is substantially lower than in the surrounding bulk.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `occupancy`
  - `units`:
    - `x`: nm
    - `y`: nm
    - `occupancy`: dimensionless

### fem_stress_potential.csv
- path: `/app/outputs/fem_stress_potential.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Hydrostatic stress and electric potential from the coupled FEM simulation. The checker will verify that notable gradients (localized variations around the secondary-phase inclusions) are present relative to the far‑field values.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `hydrostatic_stress`, `electric_potential`
  - `units`:
    - `x`: μm
    - `y`: μm
    - `hydrostatic_stress`: MPa
    - `electric_potential`: V

Notes: The checker performs structural trend verification (T3): it does not enforce exact numeric agreement, as simulation results depend on implementation-specific choices (e.g., discretization, exchange current density in Butler‑Volmer kinetics). Instead, it confirms that the occupancy inside the secondary-phase region is lower than in the bulk and that stress/potential gradients are spatially concentrated around the inclusion boundaries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kmc_occupancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "occupancy"
        ],
        "units": {
          "x": "nm",
          "y": "nm",
          "occupancy": "dimensionless"
        }
      },
      "description": "Normalized Li-ion occupancy after KMC simulation. The checker will verify that the average occupancy inside the secondary-phase strip (central y region of width 7 nm) is substantially lower than in the surrounding bulk."
    },
    {
      "file": "fem_stress_potential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "hydrostatic_stress",
          "electric_potential"
        ],
        "units": {
          "x": "μm",
          "y": "μm",
          "hydrostatic_stress": "MPa",
          "electric_potential": "V"
        }
      },
      "description": "Hydrostatic stress and electric potential from the coupled FEM simulation. The checker will verify that notable gradients (localized variations around the secondary-phase inclusions) are present relative to the far‑field values."
    }
  ],
  "notes": "The checker performs structural trend verification (T3): it does not enforce exact numeric agreement, as simulation results depend on implementation-specific choices (e.g., discretization, exchange current density in Butler‑Volmer kinetics). Instead, it confirms that the occupancy inside the secondary-phase region is lower than in the bulk and that stress/potential gradients are spatially concentrated around the inclusion boundaries."
}
```

## How you are scored
Each of the two workflow steps (KMC and FEM) has a scored artifact. After you write both CSV files to `/app/outputs`, a hidden verifier reads them and evaluates each one independently using predefined, trend‑based criteria.  

- For the KMC occupancy field, the verifier computes aggregate occupancy statistics inside and outside the secondary‑phase strip and assesses whether a meaningful spatial contrast exists.  
- For the FEM stress and potential fields, the verifier computes measures of spatial variation (e.g., differences between points near the secondary‑phase inclusions and points far from them) and checks for the presence of localised gradients.  

The exact reference patterns and tolerance thresholds are hidden, but the verifier scores higher when the agent’s fields exhibit the expected qualitative structure. The per‑step scores are combined with weights (KMC 0.4, FEM 0.6) to produce a final reward in [0,1]. No specific numeric gold value needs to be matched; the scoring is based on the emergent structural trends. Reporting a number without running the simulation will not pass the verifier; the agent must genuinely execute the prescribed computational workflow.
