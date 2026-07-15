# MD Simulation of DDAB Bilayer Adsorption on Mica

## Problem background
Surfactant adsorption at solid–liquid interfaces is important in many industrial and biological processes. Didodecyldimethylammonium bromide (DDAB) is a dual-chain cationic surfactant that can self-assemble into compact bilayer structures on atomically smooth surfaces such as muscovite mica. The resulting bilayer thickness provides a quantitative fingerprint of the molecular-scale ordering and is of central interest when comparing simulations with experiments. This computational task aims to reproduce the bilayer thickness formed by DDAB on mica by setting up and running all‑atom molecular dynamics simulations under conditions matching those used in the original experimental study, and then computing the thickness from the equilibrated trajectory.

## Approach
The approach is based on all‑atom molecular dynamics using the PCFF‑INTERFACE force field and the LAMMPS simulation package. The simulation cell contains two muscovite mica slabs with the innermost K⁺ ions removed, mimicking the ion‑exchange that occurs in the real system. A solution of DDAB at 39.1 wt% in water fills the space between the slabs. The simulation protocol consists of energy minimization, a short NVE relaxation (0.2 ns), application of a fixed load corresponding to 1 atm on the top slab, and a 50 ns NVT production run at 298 K. After equilibration, atomic density profiles along the surface‑normal are computed from the last 20 ns of the trajectory. The bilayer thickness on each surface is determined from the nitrogen (head‑group) positions: the average z‑coordinate of nitrogen atoms in the layer closest to the mica (outer) and the layer facing the bulk solution (inner) are identified, and their difference (L) is taken as the thickness. This procedure yields two values, one for each surface.

## Reproduction target
Produce a JSON file at /app/outputs/bilayer_thickness.json containing the computed bilayer thicknesses on the top and bottom mica surfaces. The file must be a JSON object with keys 'top_L' and 'bottom_L', each value a number in Å. The thickness is defined as the difference in average z‑coordinates of the outer and inner head‑group layers as described in the workflow. Completing the full simulation protocol and the thickness analysis is required to obtain these values.

## Assets

- LAMMPS Molecular Dynamics Simulator: http://lammps.sandia.gov
- Interface Force Field (PCFF-INTERFACE) toolkit: https://bionanostructures.com/interface-md

## Workflow steps

### Step 1: Prepare initial system
- Role: process
- Action: Generate LAMMPS data files for a system of two muscovite mica slabs (10×6×1 unit cells) with innermost K+ ions removed, 200 DDAB molecules, and 8000 water molecules, representing a 39.1 wt% DDAB solution. Use PCFF-INTERFACE force field parameters and random initial positions for surfactant and water.
- Evidence: none

### Step 2: Run molecular dynamics simulation
- Role: process
- Action: Using LAMMPS, perform energy minimization, followed by NVE relaxation for 0.2 ns, apply a fixed load corresponding to 1 atm on the top mica slab, and then run NVT production at 298 K for 50 ns with a 1 fs timestep. Save trajectory for analysis.
- Evidence: `/app/outputs/lammps.log`

### Step 3: Compute DDAB bilayer thickness
- Role: scored (load-bearing)
- Action: From the last 20 ns of the trajectory, calculate atomic density profiles along z. Identify nitrogen atoms of DDAB headgroups near each surface. Determine average z-coordinates of the 'outer' layer (nitrogens closest to mica) and the 'inner' layer (nitrogens facing bulk) for each surface. Compute bilayer thickness as difference between these averages. Write a JSON object with keys 'top_L' and 'bottom_L' (in Å) to /app/outputs/bilayer_thickness.json.
- Output file: `/app/outputs/bilayer_thickness.json`
- Format: json
- Contract: {"top_L": "float (Å)", "bottom_L": "float (Å)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bilayer_thickness.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bilayer_thickness.json
- path: `/app/outputs/bilayer_thickness.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: DDAB bilayer thickness on top and bottom mica surfaces, and molecular orientation distribution histogram, computed from MD trajectory.
- schema:
  - `type`: object
  - `required`:
    - `top_L`: float (Å)
    - `bottom_L`: float (Å)
  - `optional`:
    - `orientation`:
      - `type`: object
      - `required`:
        - `bins`: list[11] of float
        - `counts`: list[10] of int

Notes: The bilayer thickness is scored against hidden reference values and plausibility checks. The orientation distribution (if present) is scored via structural audit checking the histogram shape.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bilayer_thickness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "top_L": "float (Å)",
          "bottom_L": "float (Å)"
        },
        "optional": {
          "orientation": {
            "type": "object",
            "required": {
              "bins": "list[11] of float",
              "counts": "list[10] of int"
            }
          }
        }
      },
      "description": "DDAB bilayer thickness on top and bottom mica surfaces, and molecular orientation distribution histogram, computed from MD trajectory."
    }
  ],
  "notes": "The bilayer thickness is scored against hidden reference values and plausibility checks. The orientation distribution (if present) is scored via structural audit checking the histogram shape."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that scores the file bilater_thickness.json. The verifier compares your reported 'top_L' and 'bottom_L' against reference values derived from the original experimental study. The comparison uses an allowed tolerance: if your values fall within the tolerance, you receive full credit; if they deviate further, you receive partial credit based on the magnitude of the deviation. In addition, the verifier applies basic physical plausibility checks (e.g., thickness units, expected range, and symmetry between the two surfaces). The total reward is determined by this scored artifact alone; no other artifacts are scored.
