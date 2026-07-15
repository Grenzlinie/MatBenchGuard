# Water Wetting and H-Bond Analysis on Metal Surfaces via MD Simulations

## Problem background
The wettability of metal surfaces is critical for applications in catalysis, sensors, and biomedical devices. Despite the general expectation that metals are hydrophilic, experimental and simulation studies report conflicting wetting behaviors that may depend on the metal's lattice constant and the crystal face exposed. Understanding how surface atomic arrangement influences water structuring and wetting at the molecular level is essential but remains incomplete. This computational study investigates nanoscale water wetting on face-centered cubic (FCC) metal surfaces by simulating water films on eight metals (Ni, Cu, Pd, Pt, Al, Au, Ag, Pb) with three crystal faces (100), (110), and (111). By analyzing hydrogen bonding within the interfacial water layers and characterizing the resulting water configurations (film vs. droplet), the aim is to elucidate the coupling between lattice constant, crystal face, and wetting behavior.

## Approach
Classical molecular dynamics (MD) simulations are used to model water films on metal surfaces. The metal atoms are described by Lennard-Jones parameters from the force field of Heinz et al., while water is represented by the SPC/E model. For each of 24 metal/face combinations, a metal slab is solvated with a ~1.2 nm water film, and NVT simulations are run at 300 K for at least 8 ns. The resulting trajectories are then analyzed: water density profiles along the surface normal define the first monolayer; hydrogen bonds are counted using a geometric criterion (O–O distance < 0.35 nm and H–O···O angle < 30°). Two quantities are computed per water molecule in the first monolayer: the average number of hydrogen bonds formed within the monolayer and the average number formed with water molecules in the second layer above. For systems where a stable cylindrical water droplet forms on top of the monolayer, the contact angle is determined via the cylindrical droplet method. By comparing these hydrogen bond statistics and contact angles across all metal/face combinations, we assess the influence of lattice constant and crystal face on wettability.

## Reproduction target
Produce a JSON file, /app/outputs/results.json, containing the computed hydrogen bond counts and contact angles for all 24 systems. The target quantities are: (1) the average number of within-monolayer hydrogen bonds per water molecule in the first monolayer for each metal (Ni, Cu, Pd, Pt, Al, Au, Ag, Pb) and each face ((100), (110), (111)); (2) the average number of monolayer-second-layer hydrogen bonds per water molecule for the same 24 systems; and (3) the contact angle (in degrees) for the three (100) surfaces that exhibit stable droplet formation: Pd(100), Pt(100), and Al(100); for all other systems the contact angle should be reported as null. The output must be an array of objects, each with keys 'metal', 'face', 'within_monolayer_Hbonds', 'monolayer_second_layer_Hbonds', and 'contact_angle'. The objective is to quantitatively capture the wetting descriptors across the parameter space, to be validated against expected trends and reference values.

## Assets

- GROMACS MD simulation package: https://www.gromacs.org/
- Heinz et al. metal Lennard-Jones parameters (σ, ε): 10.1021/jp801931d
- SPC/E water model: Standard SPC/E parameters available in GROMACS or from literature

## Workflow steps

### Step 1: System preparation
- Role: process
- Action: For each of the 8 metals (Ni, Cu, Pd, Pt, Al, Au, Ag, Pb) and the three crystal faces (100), (110), (111), construct a metal slab with periodic boundary conditions, solvate with a ~1.2 nm water film using the SPC/E water model, assign Lennard-Jones parameters (σ, ε) from the Heinz et al. force field (Table 1). Set up GROMACS topology and coordinate files for all 24 systems.
- Evidence: none

### Step 2: Molecular dynamics simulation
- Role: process
- Action: Run NVT molecular dynamics simulations for all 24 systems using GROMACS. Use a time step of 1.0 fs, temperature 300 K maintained by v-rescale thermostat, LJ cutoff 1.0 nm, PME for electrostatics. Simulate for at least 8 ns; collect the last 4 ns of trajectory for analysis.
- Evidence: none

### Step 3: Force field validation (process only)
- Role: process
- Action: From selected trajectories (e.g., Pd(111), Pt(111), Cu(110)), compute average adsorption energy per water molecule and compare to published DFT/experimental benchmarks. Optionally examine water structures on Cu(110) and Pt(111) at low temperature. Document the computed values and comparisons; this step is not scored but ensures force field reliability.
- Evidence: `/app/outputs/validation_summary.txt`

### Step 4: Hydrogen bond and contact angle analysis
- Role: scored (load-bearing)
- Action: For each system, compute the water density profile along z to identify the first monolayer (distance from surface to first density valley). Then count hydrogen bonds using the geometric criterion (O–O < 0.35 nm, angle H–O···O < 30°). Calculate the average number of within-monolayer H-bonds and monolayer‑second‑layer H-bonds per water molecule. For Pd(100), Pt(100), and Al(100) where a stable cylindrical water droplet forms, compute the contact angle using the cylindrical droplet method. Output all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects. Each object has fields: metal (string), face (string, one of '100','110','111'), within_monolayer_Hbonds (float), monolayer_second_layer_Hbonds (float), contact_angle (float or null if no droplet).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hydrogen bond counts and contact angles computed from MD trajectories for all 24 metal/surface systems.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `face`, `within_monolayer_Hbonds`, `monolayer_second_layer_Hbonds`, `contact_angle`
    - `properties`:
      - `metal`: string
      - `face`: string
      - `within_monolayer_Hbonds`: number
      - `monolayer_second_layer_Hbonds`: number
      - `contact_angle`: number

Notes: The force field validation step produces a validation summary (validation_summary.txt) but is not scored. Only results.json is scored, checked against hidden reference values and structural trend criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "face",
            "within_monolayer_Hbonds",
            "monolayer_second_layer_Hbonds",
            "contact_angle"
          ],
          "properties": {
            "metal": "string",
            "face": "string",
            "within_monolayer_Hbonds": "number",
            "monolayer_second_layer_Hbonds": "number",
            "contact_angle": "number"
          }
        }
      },
      "description": "Hydrogen bond counts and contact angles computed from MD trajectories for all 24 metal/surface systems."
    }
  ],
  "notes": "The force field validation step produces a validation summary (validation_summary.txt) but is not scored. Only results.json is scored, checked against hidden reference values and structural trend criteria."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads /app/outputs/results.json. The verifier compares your reported H-bond numbers and contact angles to hidden reference values using a combination of numeric tolerances and structural trend checks. The reward is computed as the fraction of validation checks that pass, with each check contributing equally. Checks may include: proximity of your computed H-bond counts to reference numbers, whether the reported contact angles fall within acceptable ranges, and whether the pattern of H-bond numbers across metal/face combinations follows expected structural trends (e.g., certain surfaces showing higher within-monolayer H-bonding and lower interlayer bonding). Reporting numbers alone is insufficient; your simulation and analysis pipeline must be correctly executed to produce the required quantities. The verifier's scoring is deterministic and based solely on the contents of results.json and the hidden reference data. There is no partial credit for existence or shape; only the correctness of the computed values matters.
