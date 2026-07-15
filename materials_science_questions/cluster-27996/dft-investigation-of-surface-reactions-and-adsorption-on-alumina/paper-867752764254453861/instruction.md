# Site-resolved aluminum chemisorption on Ga-rich GaAs(100) surfaces using unrestricted MP2

## Problem background
Metal-semiconductor interfaces are central to the performance of electronic and optoelectronic devices. Aluminum on gallium arsenide (GaAs) is a widely examined system because of its use in contacts and integrated circuits. The interaction of atomic Al with the Ga-rich GaAs(100) surface determines adsorption sites, charge transfer, structural distortions, and changes in electronic properties. A detailed microscopic understanding of these effects can be obtained from first-principles electronic structure calculations. This task focuses on reproducing the computed chemisorption energies, bond lengths, HOMO-LUMO gaps, and Mulliken charges for selected Al adsorption sites on hydrogen-saturated cluster models of the Ga-rich GaAs(100)-(2×1) and β(4×2) surfaces, using second-order Møller-Plesset perturbation theory (UMP2).

## Approach
The surface is represented by finite zinc-blende clusters terminated with hydrogen atoms. The Ga and As atoms are described by Hay-Wadt effective core potentials (HWECP) augmented with a single d polarization function whose exponents were optimized for the corresponding dimers (d_Ga=0.170, d_As=0.280). For aluminum, two representations are employed to assess the role of core electrons: the same HWECP with a d exponent of 0.218, and the all-electron 6-311++G** basis set. All total energies are obtained at the unrestricted MP2 (UMP2) level. The surface Ga dimer bond length is first optimized in the smallest cluster (Ga₄As₄H₁₂) while keeping the remaining atoms fixed at bulk lattice positions. Using this optimized dimer length, bare cluster energies are computed for the target clusters. Chemisorption properties are then determined by scanning the Al adatom height above the top Ga layer for selected high-symmetry sites – top, cage, and trough – to locate the maximum chemisorption energy, defined as E_c = E(Al) + E(cluster) – E(cluster+Al). At the optimal geometry, the nearest Al–Ga bond length, HOMO-LUMO gap, and Mulliken charge on Al are extracted.

## Reproduction target
Produce a JSON file containing the chemisorption energies, Al–Ga bond lengths, HOMO-LUMO gaps, and Mulliken charges on Al for the following six system–basis combinations: (1) Ga₄As₄H₁₂ cluster + Al at the cage site with HWECP on Al, (2) Ga₄As₄H₁₂ cluster + Al at the cage site with 6-311++G** on Al, (3) Ga₄As₄H₁₂ cluster + Al at the top site with HWECP on Al, (4) Ga₄As₄H₁₂ cluster + Al at the top site with 6-311++G** on Al, (5) Ga₁₉As₁₅H₃₉ cluster + Al at the trough 5a site with HWECP on Al, (6) Ga₁₉As₁₅H₃₉ cluster + Al at the trough 5a site with 6-311++G** on Al. All computations must be performed at the unrestricted MP2 level using the basis sets, effective core potentials, and structural parameters specified in the workflow steps. The output must adhere to the schema described under the output contract.

## Assets

- Open-source quantum chemistry software (ORCA or Psi4): https://orcaforum.kofo.mpg.de or https://psicode.org
- Hay-Wadt effective core potentials and basis sets with d-augmentation for Ga, As, Al: Built into many quantum chemistry packages; d-exponents: d_Ga=0.170, d_As=0.280, d_Al=0.218 as given in the paper.
- 6-311++G** basis set for aluminum: https://www.basissetexchange.org
- Experimental lattice constant and bond lengths for GaAs and constituent dimers

## Workflow steps

### Step 1: Build cluster models and basis sets
- Role: process
- Action: Construct the required cluster models Ga4As4H12 and Ga19As15H39 using zinc-blende structure with experimental lattice constant 5.654 Å, top layer terminated by Ga atoms, and saturating H atoms at bond length 1.511 Å. Set up the Hay-Wadt effective core potentials augmented with d-functions (d_Ga=0.170, d_As=0.280, d_Al=0.218) for Ga, As, Al and the all-electron 6-311++G** basis for Al.
- Evidence: none

### Step 2: Optimize Ga–Ga surface dimer bond length
- Role: process
- Action: Using the Ga4As4H12 cluster with fixed bulk coordinates, perform an unrestricted MP2 geometry optimization of the surface Ga dimer bond length. Output the optimized bond length.
- Evidence: `/app/outputs/dimer_bond_length.json`

### Step 3: Compute bare cluster total energies
- Role: process
- Action: For the Ga4As4H12 and Ga19As15H39 clusters with the optimized dimer bond length, perform single-point unrestricted MP2 energy calculations for each cluster using each basis set representation for the Al adatom (HWECP with d-augmentation and 6-311++G**). Record the total energies.
- Evidence: `/app/outputs/bare_cluster_energies.json`

### Step 4: Compute chemisorption energies, bond lengths, HOMO-LUMO gaps, and Mulliken charges
- Role: scored (load-bearing)
- Action: For the target clusters and sites (Ga4As4H12 + Al cage, Ga4As4H12 + Al top, Ga19As15H39 + Al trough 5a) with both Al basis representations (HWECP and 6-311++G**), scan the Al height above the top Ga layer at unrestricted MP2 level to locate the maximum chemisorption energy Ec = E(Al) + E(cluster) - E(cluster+Al). At the optimal geometry, compute the nearest Al–Ga bond length, HOMO-LUMO gap, and Mulliken charge on Al. Output all results in a JSON file.
- Output file: `/app/outputs/al_chemisorption_results.json`
- Format: json
- Contract: Array of objects, each with keys: cluster (string), site (string), basis (string), Ec (float, eV), bond_length (float, Å), HOMO_LUMO_gap (float, eV), Mulliken_charge_Al (float, e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/al_chemisorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### al_chemisorption_results.json
- path: `/app/outputs/al_chemisorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Chemisorption properties for three cluster-site combinations, each with two Al basis set representations (HWECP and 6-311++G**).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `cluster`, `site`, `basis`, `Ec`, `bond_length`, `HOMO_LUMO_gap`, `Mulliken_charge_Al`
    - `properties`:
      - `cluster`:
        - `type`: string
      - `site`:
        - `type`: string
      - `basis`:
        - `type`: string
      - `Ec`:
        - `type`: number
        - `unit`: eV
      - `bond_length`:
        - `type`: number
        - `unit`: angstrom
      - `HOMO_LUMO_gap`:
        - `type`: number
        - `unit`: eV
      - `Mulliken_charge_Al`:
        - `type`: number
        - `unit`: e
  - `minItems`: 6
  - `maxItems`: 6

Notes: The checker compares each field to hidden reference values with appropriate tolerances; do not fabricate numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "al_chemisorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "cluster",
            "site",
            "basis",
            "Ec",
            "bond_length",
            "HOMO_LUMO_gap",
            "Mulliken_charge_Al"
          ],
          "properties": {
            "cluster": {
              "type": "string"
            },
            "site": {
              "type": "string"
            },
            "basis": {
              "type": "string"
            },
            "Ec": {
              "type": "number",
              "unit": "eV"
            },
            "bond_length": {
              "type": "number",
              "unit": "angstrom"
            },
            "HOMO_LUMO_gap": {
              "type": "number",
              "unit": "eV"
            },
            "Mulliken_charge_Al": {
              "type": "number",
              "unit": "e"
            }
          }
        },
        "minItems": 6,
        "maxItems": 6
      },
      "description": "Chemisorption properties for three cluster-site combinations, each with two Al basis set representations (HWECP and 6-311++G**)."
    }
  ],
  "notes": "The checker compares each field to hidden reference values with appropriate tolerances; do not fabricate numbers."
}
```

## How you are scored
Each step in the workflow produces one or more output artifacts. The hidden verifier independently inspects these artifacts. The main scored artifact is `al_chemisorption_results.json`. The verifier compares every reported field – chemisorption energy, bond length, HOMO-LUMO gap, and Mulliken charge – against hidden reference values that correspond to the same system–basis combinations. The comparison uses appropriate numerical tolerances that account for differences between quantum chemistry codes and convergence settings. Simply copying numbers from a published table is not sufficient; you must execute the described computational protocol to generate the results. The final reward is a weighted combination of the scores assigned to each scored artifact, with the chemisorption energy and associated properties carrying the largest weight.
