# DFT O2 Adsorption on Reduced ZnO(10-10)

## Problem background
Zinc oxide (ZnO) surfaces have attracted significant interest for photocatalysis and gas sensing, with the (10-10) surface being the most stable and abundant. The presence of oxygen vacancies on reduced ZnO surfaces can dramatically alter their reactivity toward ambient gases. Understanding how molecular oxygen (O2) adsorbs at these vacancies, the geometries it adopts, and the resulting adsorption energies is crucial for predicting and controlling ZnO surface chemistry. This task reproduces the density-functional theory (DFT) calculations that determine the adsorption behavior of O2 on a reduced ZnO(10-10) surface with a 0.25 monolayer (ML) oxygen vacancy concentration.

## Approach
The study employs plane-wave DFT with the Perdew-Wang 91 (PW91) generalized gradient approximation (GGA) and projector-augmented wave (PAW) pseudopotentials to model the ZnO(10-10) surface. A periodic slab model is constructed from the relaxed wurtzite ZnO bulk crystal. A stoichiometric slab is first relaxed, then one surface oxygen atom is removed to create a 0.25 ML oxygen vacancy. The clean stoichiometric slab serves as the reference for the bare surface energy, while the reduced slab serves as the substrate for O2 adsorption. Gas-phase reference energies for isolated O2 (triplet) and atomic O are computed separately. Five distinct initial adsorption configurations are considered: two dissociative geometries where one O fills the vacancy and the other binds to surface Zn atoms, and three molecular/complex geometries where an O2 molecule adsorbs intact at the vacancy site, forming an O–O complex. For each, the geometry is relaxed fully, and the total energy is recorded. The per-O2 adsorption energy is then obtained as the difference between the total energy, the reduced slab energy, and the free O2 energy. From these, the most stable adsorption configuration is identified. For that most stable structure, the distance between the two oxygen atoms of the O–O complex is extracted, and the adsorption energy per atomic oxygen is computed using the bare stoichiometric slab and atomic O reference.

## Reproduction target
Using the described DFT protocol and the p(2×2) ZnO(10-10) slab model with one oxygen vacancy per cell, compute the adsorption energy per O2 molecule for each of the five adsorption configurations (labeled 3a through 3e in the following workflow). Determine which configuration is the most stable based on the lowest adsorption energy. For that most stable configuration, report the O–O bond length (in Å) and also compute the adsorption energy per atomic oxygen atom. All energies and the bond length must be saved to the specified output files.

## Assets

- Open-source plane-wave DFT code: https://www.quantum-espresso.org/
- PW91 PAW pseudopotentials: https://www.materialscloud.org/discover/sssp/table/graph

## Workflow steps

### Step 1: Bulk ZnO optimization
- Role: process
- Action: Perform DFT geometry optimization of the wurtzite ZnO bulk unit cell using PW91 GGA, PAW pseudopotentials, spin-polarized calculation, plane-wave cutoff 400 eV, and an appropriate k-point grid to obtain relaxed lattice parameters a and c. Write optimized lattice parameters to lattice_params.json as evidence.
- Evidence: `/app/outputs/lattice_params.json`

### Step 2: Stoichiometric surface slab construction and relaxation
- Role: process
- Action: Using the relaxed a and c from step 1, construct a periodic p(2x2) ZnO(10-10) slab with at least 10 Å vacuum. Relax the ionic positions (top 2 layers free) until all forces are below 0.01 eV/Å, using a 4x5x1 k-point grid. Keep lattice parameters of the slab fixed at bulk optimized values. Write the relaxed slab geometry to stoichiometric_slab.xyz as evidence.
- Evidence: `/app/outputs/stoichiometric_slab.xyz`

### Step 3: Gas-phase reference energies
- Role: process
- Action: Calculate the total energies of an isolated O2 molecule (triplet, spin-polarized) and an isolated oxygen atom using the same functional, pseudopotentials, cutoff, and a large enough cell (e.g., 15x16x17 Å) with Γ-point sampling. Write the reference energies to reference_energies.json as evidence.
- Evidence: `/app/outputs/reference_energies.json`

### Step 4: Reduced surface (oxygen vacancy) construction and relaxation
- Role: process
- Action: Create a reduced p(2x2) slab by removing one surface oxygen atom from the relaxed stoichiometric slab to form an oxygen vacancy (0.25 ML). Relax the geometry again until forces < 0.01 eV/Å, using the same k-points. Write the relaxed reduced slab geometry to reduced_slab.xyz as evidence.
- Evidence: `/app/outputs/reduced_slab.xyz`

### Step 5: O2 adsorption configurations and adsorption energies
- Role: scored (load-bearing)
- Action: Place one O2 molecule on the reduced slab in the five distinct initial geometries corresponding to structures 3a–3e: (3a,3b) dissociative with one O filling the vacancy and the other bound to surface Zn atom(s); (3c,3d,3e) O–O complexes at the vacancy site. For each, perform a full geometry relaxation (same DFT settings as before) and record the total energy. Compute the per-O2 adsorption energy using E_ads = (E_total - E_reduced - E_O2). Identify the most stable geometry (lowest E_ads). Using the most stable geometry (3e), compute the atomic oxygen adsorption energy as E_ads_atomic_O = E_total - E_bare - E_atomic_O. Output all total energies, reference energies, and computed adsorption energies in a JSON file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys: configurations (object mapping configuration keys '3a'..'3e' to objects with fields E_total (number, eV) and E_ads_per_O2_eV (number)), most_stable (string), E_ads_atomic_O_eV (number), E_O2 (number), E_atomic_O (number), E_reduced (number), E_bare (number).
- Scoring: scored by hidden verifier

### Step 6: O–O bond length of the most stable configuration
- Role: scored (load-bearing)
- Action: From the relaxed geometry of the most stable O2 adsorption configuration (3e, identified in step 5), extract the distance between the two oxygen atoms that constitute the O–O complex (the O–O bond length in Å). Write this single floating-point number to a text file.
- Output file: `/app/outputs/O-O_bond_length.txt`
- Format: txt
- Contract: A single line containing the O–O bond length in Å as a floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/O-O_bond_length.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored adsorption energies and supporting raw energies; checker recomputes from raw totals and compares to paper values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `configurations`: object
    - `most_stable`: string
    - `E_ads_atomic_O_eV`: number
    - `E_O2`: number
    - `E_atomic_O`: number
    - `E_reduced`: number
    - `E_bare`: number
  - `description`: Adsorption energies per O2 molecule for five configurations on reduced ZnO(10-10) surface with 0.25 ML oxygen vacancy, plus atomic oxygen adsorption energy for the most stable structure.

### O-O_bond_length.txt
- path: `/app/outputs/O-O_bond_length.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: O–O bond length of the O–O complex formed at the oxygen vacancy site.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing the O–O bond length in Å for the most stable O2 adsorption configuration (structure 3e).

Notes: All energies are in eV and bond lengths in Å. The checker uses the paper's reported adsorption energies and bond length as hidden gold with fixed tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "configurations": "object",
          "most_stable": "string",
          "E_ads_atomic_O_eV": "number",
          "E_O2": "number",
          "E_atomic_O": "number",
          "E_reduced": "number",
          "E_bare": "number"
        },
        "description": "Adsorption energies per O2 molecule for five configurations on reduced ZnO(10-10) surface with 0.25 ML oxygen vacancy, plus atomic oxygen adsorption energy for the most stable structure."
      },
      "description": "Scored adsorption energies and supporting raw energies; checker recomputes from raw totals and compares to paper values with tolerance."
    },
    {
      "file": "O-O_bond_length.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing the O–O bond length in Å for the most stable O2 adsorption configuration (structure 3e)."
      },
      "description": "O–O bond length of the O–O complex formed at the oxygen vacancy site."
    }
  ],
  "notes": "All energies are in eV and bond lengths in Å. The checker uses the paper's reported adsorption energies and bond length as hidden gold with fixed tolerances."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that independently recomputes the adsorption energies from the raw total energies you provide in adsorption_energies.json, then compares them against hidden reference values. The verifier also checks that the declared most stable configuration is correct and that the extracted O–O bond length matches the reference within an appropriate tolerance. Each scored output file contributes to a weighted total reward; simply providing a number without having executed the required calculations will not suffice. The verifier ensures that your results are consistent with the underlying physics; running the full DFT workflow as outlined is essential to achieve a passing score.
