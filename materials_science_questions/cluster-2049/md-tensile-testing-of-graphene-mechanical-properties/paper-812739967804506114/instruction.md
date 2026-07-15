# Self-Assembly of Graphene Nanoscroll from Submerged Nanoribbon under Rotating Electric Field

## Problem background
Graphene nanoscrolls (GNS) are spiral-like rolled-up graphene sheets with a hollow core. They offer large tunable interlayer galleries and open ends, making them attractive for energy storage, nanofluidic channels, and nanoelectronics. However, existing fabrication routes—arc discharge, chemical intercalation, ball milling, mechanical rolling—suffer from impurities, low yield, harsh conditions, or dependence on nanotemplates that are difficult to remove afterwards. A purely physical, room-temperature method that yields pure nanoscrolls from a graphene nanoribbon (GNR) would be a significant advance. This task investigates a proposed method in which a water‑submerged GNR with one edge fixed is subjected to a rotating electric field; the field is hypothesised to induce self‑assembly into a stable nanoscroll. The central quantities to determine are the interlayer distances and the inner and outer diameters of the final structure, obtained from atomic concentration profiles along the two axes perpendicular to the scroll axis.

## Approach
The approach uses all‑atom molecular dynamics (MD) with the GROMACS engine, the OPLS‑AA force field for sp² carbon, and the TIP3P explicit water model. A zigzag GNR (100.3 Å × 94.5 Å) with prolonged edges that remain fixed during the whole simulation is placed in a water box. After energy minimisation, the system is equilibrated first in the NVT ensemble (target 300 K) and then in the NPT ensemble (target 1 bar). During production MD, a rotating electric field is applied in the YZ plane with field components E_y(t) = E₀ sin(ωt) and E_z(t) = E₀ sin(ωt + π/2), where E₀ = 1.0 V nm⁻¹ and the angular frequency ω corresponds to 90 Gr.p.m. The field is kept on for 10 ns, then switched off for a further 5 ns, after which all water molecules are removed and a final 5 ns simulation is run. The central idea is that the field aligns the water dipoles, which in turn rotate the free end of the GNR around the fixed edge, leading to folding and—if the method succeeds—scroll formation. The final carbon‑atom configuration is then analysed by computing one‑dimensional concentration profiles along the Y and Z axes. Peaks in these profiles correspond to scroll layers; the distances between adjacent peaks give the interlayer separations, and the inner and outer diameters are measured between the innermost and outermost peaks. The results are saved as a JSON file.

## Reproduction target
Given the 100.3 Å × 94.5 Å zigzag GNR geometry, the fixed prolonged edges, the TIP3P water solvation, and the rotating electric field described above, execute the complete MD workflow to obtain the final dry configuration. From that configuration, compute the atomic concentration profiles of carbon atoms along the Y and Z directions. Identify the peaks in each profile; there must be at least three distinct peaks along each axis to indicate that a scroll has formed. Measure the distances between adjacent peaks (d₁, d₂, d₃) following the convention of starting from the negative axis direction, and determine the inner diameter (distance between the innermost peaks) and outer diameter (distance between the outermost peaks). The small irregular peak that may appear along Y at the scroll termination should be ignored. Write all measured values—in nanometres—into the single JSON output file interlayer_distances.json with the exact keys and structure shown in the output contract.

## Assets

- GROMACS: https://www.gromacs.org
- OPLS-AA force field: gromacs
- TIP3P water model: gromacs

## Workflow steps

### Step 1: System preparation
- Role: process
- Action: Construct a simulation box containing a 100.3 Å × 94.5 Å zigzag graphene nanoribbon with fixed prolonged edges along the X axis, passivate dangling bonds with hydrogen, solvate with TIP3P water molecules in a ~12×12×12 nm³ box, and assign OPLS-AA force field parameters for carbon atoms and cross-interactions. The edges of the prolonged region must remain fixed throughout all subsequent simulations.
- Evidence: `/app/outputs/initial.gro`

### Step 2: NVT/NPT equilibration
- Role: process
- Action: Equilibrate the solvated GNR system in two stages: NVT ensemble for 5 ns to reach 300 K, followed by NPT ensemble for 5 ns to reach 1 bar, using standard thermostat and barostat settings.
- Evidence: `/app/outputs/equilibrated.gro`

### Step 3: Nanoscroll formation simulation
- Role: process
- Action: Run production MD with a rotating electric field in the YZ plane: Ey(t)=E0 sin(ωt), Ez(t)=E0 sin(ωt+π/2) with E0=1.0 V/nm and ω corresponding to 90 Gr.p.m. Simulate for 10 ns with the field on, then remove the field and simulate for an additional 5 ns, then remove all water molecules and simulate for a final 5 ns. Maintain temperature at 300 K and pressure at 1 bar. The prolonged edges of the GNR remain fixed throughout.
- Evidence: `/app/outputs/scroll_final.gro`

### Step 4: Concentration profile analysis and distance extraction
- Role: scored (load-bearing)
- Action: From the final configuration after water removal, compute the atomic concentration profile of carbon atoms along the Y and Z axes. Identify the peaks in each profile, measure the distances between adjacent peaks (d1,d2,d3) as defined in the paper (starting from the negative axis direction), and determine the inner diameter (distance between innermost peaks) and outer diameter (distance between outermost peaks). Ignore the small irregular peak that may appear along Y at the scroll termination. Write the measured values to interlayer_distances.json.
- Output file: `/app/outputs/interlayer_distances.json`
- Format: json
- Contract: {"Y_d1": <number | null>, "Y_d2": <number>, "Y_d3": <number>, "Y_d_i": <number>, "Y_d_o": <number>, "Z_d1": <number>, "Z_d2": <number>, "Z_d3": <number>, "Z_d_i": <number>, "Z_d_o": <number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interlayer_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interlayer_distances.json
- path: `/app/outputs/interlayer_distances.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Interlayer distances and inner/outer diameters of the final nanoscroll along Y and Z axes, extracted from atomic concentration profiles after field and water removal. Y_d1 may be null if the irregular scroll termination peak is absent.
- schema:
  - `type`: object
  - `required`: `Y_d1`, `Y_d2`, `Y_d3`, `Y_d_i`, `Y_d_o`, `Z_d1`, `Z_d2`, `Z_d3`, `Z_d_i`, `Z_d_o`
  - `properties`:
    - `Y_d1`:
      - `type`: number
      - `unit`: nm
      - `nullable`: True
    - `Y_d2`:
      - `type`: number
      - `unit`: nm
    - `Y_d3`:
      - `type`: number
      - `unit`: nm
    - `Y_d_i`:
      - `type`: number
      - `unit`: nm
    - `Y_d_o`:
      - `type`: number
      - `unit`: nm
    - `Z_d1`:
      - `type`: number
      - `unit`: nm
    - `Z_d2`:
      - `type`: number
      - `unit`: nm
    - `Z_d3`:
      - `type`: number
      - `unit`: nm
    - `Z_d_i`:
      - `type`: number
      - `unit`: nm
    - `Z_d_o`:
      - `type`: number
      - `unit`: nm

Notes: All distances in nanometers. The scored target is the set of ten scalar values; each is compared to a hidden reference within an allowed tolerance. The presence of at least three distinct peaks along each axis is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interlayer_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Y_d1",
          "Y_d2",
          "Y_d3",
          "Y_d_i",
          "Y_d_o",
          "Z_d1",
          "Z_d2",
          "Z_d3",
          "Z_d_i",
          "Z_d_o"
        ],
        "properties": {
          "Y_d1": {
            "type": "number",
            "unit": "nm",
            "nullable": true
          },
          "Y_d2": {
            "type": "number",
            "unit": "nm"
          },
          "Y_d3": {
            "type": "number",
            "unit": "nm"
          },
          "Y_d_i": {
            "type": "number",
            "unit": "nm"
          },
          "Y_d_o": {
            "type": "number",
            "unit": "nm"
          },
          "Z_d1": {
            "type": "number",
            "unit": "nm"
          },
          "Z_d2": {
            "type": "number",
            "unit": "nm"
          },
          "Z_d3": {
            "type": "number",
            "unit": "nm"
          },
          "Z_d_i": {
            "type": "number",
            "unit": "nm"
          },
          "Z_d_o": {
            "type": "number",
            "unit": "nm"
          }
        }
      },
      "description": "Interlayer distances and inner/outer diameters of the final nanoscroll along Y and Z axes, extracted from atomic concentration profiles after field and water removal. Y_d1 may be null if the irregular scroll termination peak is absent."
    }
  ],
  "notes": "All distances in nanometers. The scored target is the set of ten scalar values; each is compared to a hidden reference within an allowed tolerance. The presence of at least three distinct peaks along each axis is also verified."
}
```

## How you are scored
A hidden verifier will examine your interlayer_distances.json file. It checks that the file contains all required keys and that each reported distance and diameter is numerically close to a hidden reference value, using a tolerance that accommodates legitimate run‑to‑run variability from different hardware, compilations, or MD implementations. A result that meets or exceeds the expected precision (i.e. falls within the tolerance) earns full credit for that quantity, and partial credit is awarded when some values are farther off. In addition, the verifier confirms that at least three well‑defined peaks are present in both the Y and Z concentration profiles—evidence that a scrolled structure indeed formed. The overall reward is the weighted sum of these checks; simply reporting the hidden reference numbers without performing the simulation will not pass because the verifier also inspects structural consistency. The tolerances are not disclosed to you, so your best strategy is to follow the protocol faithfully.
