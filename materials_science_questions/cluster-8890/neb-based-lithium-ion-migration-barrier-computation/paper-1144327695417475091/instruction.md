# BVSE oxide-ion migration barriers for Ba3Ti0.7Mo1.3O8.3

## Problem background
Oxide-ion conductors are key materials for solid-oxide fuel cells and intermediate-temperature electrolytes. Bond valence site energy (BVSE) calculations are widely used to map ion migration pathways and quantify energy barriers for oxide-ion diffusion in crystalline solids. Understanding the conduction mechanism in hexagonal perovskite derivatives, particularly the 2D oxide-ion migration along oxygen-disordered layers, can guide the design of improved electrolytes. This task focuses on computing the migration barriers for oxide-ion hopping in a specific hexagonal perovskite structure.

## Approach
The bond valence site energy (BVSE) method evaluates the energy landscape experienced by a probe ion as it moves through a static crystal framework. By summing bond-valence contributions, site energies are calculated and used to trace the lowest-energy diffusion pathways. The softBV software (open source, available at the provided URL) implements this approach. Given a crystal structure (CIF) of a hybrid hexagonal perovskite, you will run softBV to map the two-dimensional oxide-ion migration network within the oxygen-disordered c′-BaO2.3 layer. The key outputs are two energy barriers: E1, corresponding to in-plane O2↔O3 hopping, and E2, associated with relaxation along the c-axis. The calculation requires the lattice parameters, atomic positions, site occupancies, and thermal parameters, all extracted from the published structure and provided as a CIF file. No external datasets are needed; the sole input is the crystal structure.

## Reproduction target
Using the crystal structure defined in Step 1, run the softBV tool to map the 2D oxide-ion conduction pathways and extract the energy barriers E1 (ab-plane O2↔O3 hopping) and E2 (c-axis relaxation) in electron volts (eV). Write a single JSON file containing these two numerical values.

## Assets

- softBV (Bond Valence Site Energy tool): https://github.com/lsmo-bv/softBV

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Construct a CIF file for Ba3Ti0.7Mo1.3O8.3 in space group R-3m (hexagonal setting) with lattice parameters a=b≈5.93 Å, c≈21.25 Å, and atomic positions, occupancies, and thermal parameters as given in the published crystallographic table. The M1 and M2 sites are mixed Mo/Ti; O1 fully occupied; O2 and O3 partially occupied with occupancies 0.238 and 0.1323 per site. The CIF must include the correct atom labels and symmetry.
- Evidence: `/app/outputs/structure.cif`

### Step 2: Compute BVSE migration barriers
- Role: scored
- Action: Run the softBV tool on the prepared CIF to map the 2D oxide-ion migration pathways along the c'-BaO2.3 layer and extract the energy barriers E1 (for O2↔O3 hopping in the ab-plane) and E2 (for relaxation along the c-axis). Write a JSON file with keys 'E1' and 'E2' (values in eV).
- Output file: `/app/outputs/computed_barriers.json`
- Format: json
- Contract: {"E1": number (eV), "E2": number (eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_barriers.json
- path: `/app/outputs/computed_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed migration energy barriers for oxide-ion diffusion: E1 (ab-plane O2↔O3 hopping) and E2 (c-axis relaxation) in eV.
- schema:
  - `type`: object
  - `required`:
    - `E1`: number
    - `E2`: number
  - `units`:
    - `E1`: eV
    - `E2`: eV

Notes: The hidden checker will compare the submitted E1 and E2 values against reference values within a tolerance. The tolerance is not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E1": "number",
          "E2": "number"
        },
        "units": {
          "E1": "eV",
          "E2": "eV"
        }
      },
      "description": "Computed migration energy barriers for oxide-ion diffusion: E1 (ab-plane O2↔O3 hopping) and E2 (c-axis relaxation) in eV."
    }
  ],
  "notes": "The hidden checker will compare the submitted E1 and E2 values against reference values within a tolerance. The tolerance is not disclosed to the agent."
}
```

## How you are scored
A hidden verifier will evaluate your work. It first validates that the required output file exists, is valid JSON, and contains the keys E1 and E2 as numeric values. It then compares your reported barriers to a hidden reference with an appropriate tolerance. The verifier independently scores each workflow stage and combines the scores into a final reward; simply reporting numbers without genuinely running the BVSE calculation will not pass. You must execute the steps as described to obtain the barriers.
