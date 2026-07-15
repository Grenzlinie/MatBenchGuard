# DFT Investigation of K Doping Effects on CO Oxidation over MnO₂ Surfaces

## Problem background
Catalytic CO oxidation is of great importance for air purification and exhaust treatment. MnO₂‑based catalysts are promising low‑cost alternatives to noble metals, and doping with alkali metals can further improve their activity. Experimental studies have shown that adding a small amount of K to β‑MnO₂ enhances CO oxidation, while excessive K triggers a phase transformation to α‑MnO₂ and a drop in performance. The goal of this task is to use density functional theory (DFT) to compute the adsorption energetics, charge transfer, and reaction barriers on these two MnO₂ surfaces, with and without K, in order to understand the electronic‑structure factors that govern the catalytic activity.

## Approach
The computational approach employs spin‑polarised DFT+U calculations with the Perdew‑Burke‑Ernzerhof (PBE) exchange‑correlation functional and a Hubbard‑U correction on the Mn d electrons. Bulk structures of β‑MnO₂ (rutile) and α‑MnO₂ (hollandite) are obtained from public databases; their lattice parameters are first optimised. From the optimised bulk, symmetric slab models are built for the most stable surfaces – β‑MnO₂(110) and α‑MnO₂(100) – with a (2×3) and (1×3) surface supercell, respectively, and a vacuum gap of 10 Å. In each slab the bottom layers are frozen to represent the bulk, and the remaining ions are relaxed.

Potassium is introduced in two ways: as an adsorbate at the bridge site on β‑MnO₂(110), and as a dopant inside the 2×2 tunnel of α‑MnO₂(100). Adsorption energies are defined as E_ad = E_slab+A – E_slab – E_A, where A is the isolated K, CO or O₂ molecule. Bader charge analysis quantifies the electron transfer from K to the surface. For CO oxidation, the reaction CO + lattice O_br → CO₂ + O_vacancy is investigated by locating the transition state (TS) on the clean β‑MnO₂(110), on the K‑adsorbed β‑MnO₂(110), and on the K‑doped α‑MnO₂(100) surface. On β‑MnO₂(110), O₂ adsorption at an O_br vacancy is also studied on both the clean and the K‑adsorbed surface to assess how K affects O₂ activation.

All calculations can be performed with an open‑source plane‑wave DFT code such as Quantum ESPRESSO, using standard pseudopotentials from the SSSP library. The workflow is organised as a sequence of independent calculations whose outputs are finally collected into a single JSON file.

## Reproduction target
Using the above protocol, compute the following quantities and write them to `/app/outputs/dft_results.json`:

- Bulk lattice parameters a and c for both β‑MnO₂ and α‑MnO₂ (Å).
- Adsorption energy of K on β‑MnO₂(110) at the bridge site (eV).
- Net Bader charge transferred from K to the surface O_br atoms (e).
- CO adsorption energy on clean β‑MnO₂(110) at the Mn₅c site (eV).
- CO adsorption energy on K‑adsorbed β‑MnO₂(110) at the Mn₅c site (eV).
- O₂ adsorption energy at an O_br vacancy on clean β‑MnO₂(110) (eV) and the O–O bond length (Å).
- O₂ adsorption energy at an O_br vacancy on K‑adsorbed β‑MnO₂(110) (eV) and the O–O bond length (Å).
- Energy barrier for CO + O_br → CO₂ + oxygen vacancy on clean β‑MnO₂(110) (eV).
- Energy barrier for CO + O_br → CO₂ + oxygen vacancy on K‑adsorbed β‑MnO₂(110) (eV).
- Adsorption energy of K inside the 2×2 tunnel of α‑MnO₂(100) (eV).
- CO adsorption energy on K‑doped α‑MnO₂(100) at the Mn₅c site (eV).
- Energy barrier for CO + O_br → CO₂ + oxygen vacancy on K‑doped α‑MnO₂(100) (eV).

The JSON keys match those in the output contract; every value must be numeric and in the specified units (eV, Å, e).

## Assets

- Bulk MnO₂ crystal structures (α and β): https://www.crystallography.net/cod/
- Quantum ESPRESSO DFT package: quantum-espresso
- Bader charge analysis code: https://theory.cm.utexas.edu/henkelman/code/bader/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk optimization of MnO₂ phases
- Role: process
- Action: Perform spin-polarized DFT+U optimization of bulk α-MnO₂ and β-MnO₂ unit cells to obtain equilibrium lattice parameters.
- Evidence: none

### Step 2: Surface slab construction
- Role: process
- Action: From optimized bulk parameters, construct (2×3) β-MnO₂(110) and (1×3) α-MnO₂(100) symmetric slabs with bottom layers frozen and 10 Å vacuum.
- Evidence: none

### Step 3: Slab relaxation
- Role: process
- Action: Relax ionic positions for both slab models keeping bottom layers fixed.
- Evidence: none

### Step 4: K adsorption on β-MnO₂(110)
- Role: process
- Action: Place K atom at bridge site, relax geometry, and compute adsorption energy.
- Evidence: none

### Step 5: Bader charge analysis
- Role: process
- Action: Compute Bader charges for K-adsorbed β-MnO₂(110) and the clean surface, determine net electron transfer to Obr.
- Evidence: none

### Step 6: CO adsorption on clean β-MnO₂(110)
- Role: process
- Action: Adsorb CO at Mn5c site on clean surface, relax, compute adsorption energy.
- Evidence: none

### Step 7: CO oxidation TS on clean β-MnO₂(110)
- Role: process
- Action: Locate transition state for CO + lattice Obr → CO₂ + oxygen vacancy, compute energy barrier.
- Evidence: none

### Step 8: O₂ adsorption at Obr vacancy on clean β-MnO₂(110)
- Role: process
- Action: Create Obr vacancy, adsorb O₂, optimize geometry, obtain adsorption energy and O–O bond length.
- Evidence: none

### Step 9: CO adsorption on K-adsorbed β-MnO₂(110)
- Role: process
- Action: On the K-bridge adsorbed surface, adsorb CO at Mn5c, relax, compute adsorption energy.
- Evidence: none

### Step 10: O₂ adsorption at vacancy on K-adsorbed β-MnO₂(110)
- Role: process
- Action: Create Obr vacancy on K-adsorbed surface, adsorb O₂, optimize, obtain adsorption energy and O–O bond length.
- Evidence: none

### Step 11: CO oxidation TS on K-adsorbed β-MnO₂(110)
- Role: process
- Action: Locate transition state for CO oxidation on K-adsorbed surface, compute energy barrier.
- Evidence: none

### Step 12: K adsorption in α-MnO₂(100) tunnel
- Role: process
- Action: Insert K atom into the 2×2 tunnel of α-MnO₂(100), relax geometry, compute adsorption energy.
- Evidence: none

### Step 13: CO adsorption on K-doped α-MnO₂(100)
- Role: process
- Action: Adsorb CO at Mn5c on K-doped α surface, relax, compute adsorption energy.
- Evidence: none

### Step 14: CO oxidation TS on K-doped α-MnO₂(100)
- Role: process
- Action: Locate transition state for CO oxidation by lattice O on K-doped α surface, compute energy barrier.
- Evidence: none

### Step 15: Compile all DFT results into JSON
- Role: scored (load-bearing)
- Action: Gather all computed quantities (adsorption energies, barriers, bond lengths, charge transfer, lattice parameters) and write dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: Keys: k_adsorption_energy_beta, bader_charge_transfer, co_adsorption_energy_clean_beta, co_adsorption_energy_k_beta, o2_adsorption_energy_clean_vacancy_beta, o2_adsorption_energy_k_vacancy_beta, o2_bond_length_clean_vacancy_beta, o2_bond_length_k_vacancy_beta, barrier_co_obr_clean_beta, barrier_co_obr_k_beta, k_adsorption_energy_alpha, co_adsorption_energy_alpha, barrier_co_obr_alpha, bulk_alpha_a, bulk_alpha_c, bulk_beta_a, bulk_beta_c. All values in eV or Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing all computed DFT values needed to score the reproduction. Checker compares each value to hidden gold within tolerances and verifies structural trends.
- schema:
  - `type`: object
  - `required`: `k_adsorption_energy_beta`, `bader_charge_transfer`, `co_adsorption_energy_clean_beta`, `co_adsorption_energy_k_beta`, `o2_adsorption_energy_clean_vacancy_beta`, `o2_adsorption_energy_k_vacancy_beta`, `o2_bond_length_clean_vacancy_beta`, `o2_bond_length_k_vacancy_beta`, `barrier_co_obr_clean_beta`, `barrier_co_obr_k_beta`, `k_adsorption_energy_alpha`, `co_adsorption_energy_alpha`, `barrier_co_obr_alpha`, `bulk_alpha_a`, `bulk_alpha_c`, `bulk_beta_a`, `bulk_beta_c`
  - `properties`:
    - `k_adsorption_energy_beta`:
      - `type`: number
      - `units`: eV
    - `bader_charge_transfer`:
      - `type`: number
      - `units`: e
    - `co_adsorption_energy_clean_beta`:
      - `type`: number
      - `units`: eV
    - `co_adsorption_energy_k_beta`:
      - `type`: number
      - `units`: eV
    - `o2_adsorption_energy_clean_vacancy_beta`:
      - `type`: number
      - `units`: eV
    - `o2_adsorption_energy_k_vacancy_beta`:
      - `type`: number
      - `units`: eV
    - `o2_bond_length_clean_vacancy_beta`:
      - `type`: number
      - `units`: Å
    - `o2_bond_length_k_vacancy_beta`:
      - `type`: number
      - `units`: Å
    - `barrier_co_obr_clean_beta`:
      - `type`: number
      - `units`: eV
    - `barrier_co_obr_k_beta`:
      - `type`: number
      - `units`: eV
    - `k_adsorption_energy_alpha`:
      - `type`: number
      - `units`: eV
    - `co_adsorption_energy_alpha`:
      - `type`: number
      - `units`: eV
    - `barrier_co_obr_alpha`:
      - `type`: number
      - `units`: eV
    - `bulk_alpha_a`:
      - `type`: number
      - `units`: Å
    - `bulk_alpha_c`:
      - `type`: number
      - `units`: Å
    - `bulk_beta_a`:
      - `type`: number
      - `units`: Å
    - `bulk_beta_c`:
      - `type`: number
      - `units`: Å

Notes: All energies in eV, lengths in Å, charge in e. The verifier also checks trend constraints: barrier_co_obr_k_beta < barrier_co_obr_clean_beta < barrier_co_obr_alpha, o2_adsorption_energy_k_vacancy_beta < o2_adsorption_energy_clean_vacancy_beta, o2_bond_length_k_vacancy_beta > o2_bond_length_clean_vacancy_beta.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "k_adsorption_energy_beta",
          "bader_charge_transfer",
          "co_adsorption_energy_clean_beta",
          "co_adsorption_energy_k_beta",
          "o2_adsorption_energy_clean_vacancy_beta",
          "o2_adsorption_energy_k_vacancy_beta",
          "o2_bond_length_clean_vacancy_beta",
          "o2_bond_length_k_vacancy_beta",
          "barrier_co_obr_clean_beta",
          "barrier_co_obr_k_beta",
          "k_adsorption_energy_alpha",
          "co_adsorption_energy_alpha",
          "barrier_co_obr_alpha",
          "bulk_alpha_a",
          "bulk_alpha_c",
          "bulk_beta_a",
          "bulk_beta_c"
        ],
        "properties": {
          "k_adsorption_energy_beta": {
            "type": "number",
            "units": "eV"
          },
          "bader_charge_transfer": {
            "type": "number",
            "units": "e"
          },
          "co_adsorption_energy_clean_beta": {
            "type": "number",
            "units": "eV"
          },
          "co_adsorption_energy_k_beta": {
            "type": "number",
            "units": "eV"
          },
          "o2_adsorption_energy_clean_vacancy_beta": {
            "type": "number",
            "units": "eV"
          },
          "o2_adsorption_energy_k_vacancy_beta": {
            "type": "number",
            "units": "eV"
          },
          "o2_bond_length_clean_vacancy_beta": {
            "type": "number",
            "units": "Å"
          },
          "o2_bond_length_k_vacancy_beta": {
            "type": "number",
            "units": "Å"
          },
          "barrier_co_obr_clean_beta": {
            "type": "number",
            "units": "eV"
          },
          "barrier_co_obr_k_beta": {
            "type": "number",
            "units": "eV"
          },
          "k_adsorption_energy_alpha": {
            "type": "number",
            "units": "eV"
          },
          "co_adsorption_energy_alpha": {
            "type": "number",
            "units": "eV"
          },
          "barrier_co_obr_alpha": {
            "type": "number",
            "units": "eV"
          },
          "bulk_alpha_a": {
            "type": "number",
            "units": "Å"
          },
          "bulk_alpha_c": {
            "type": "number",
            "units": "Å"
          },
          "bulk_beta_a": {
            "type": "number",
            "units": "Å"
          },
          "bulk_beta_c": {
            "type": "number",
            "units": "Å"
          }
        }
      },
      "description": "JSON file containing all computed DFT values needed to score the reproduction. Checker compares each value to hidden gold within tolerances and verifies structural trends."
    }
  ],
  "notes": "All energies in eV, lengths in Å, charge in e. The verifier also checks trend constraints: barrier_co_obr_k_beta < barrier_co_obr_clean_beta < barrier_co_obr_alpha, o2_adsorption_energy_k_vacancy_beta < o2_adsorption_energy_clean_vacancy_beta, o2_bond_length_k_vacancy_beta > o2_bond_length_clean_vacancy_beta."
}
```

## How you are scored
A hidden verifier reads your `dft_results.json` and scores it automatically. Each numeric quantity is compared against a reference value derived from the original publication, using tolerances that account for the expected spread between different DFT codes, pseudopotentials, and numerical choices. If a value falls within the acceptable range it earns full credit for that key; values substantially outside the range receive partial or no credit.

The verifier also inspects structural trends across your results – for example, the relative ordering of the CO oxidation barriers on the three surface conditions, and the change in O₂ adsorption strength and O–O bond length between the clean and K‑adsorbed β‑MnO₂ surfaces. Inconsistency with physically expected trends reduces the score even if individual numbers are close to the reference.

The final reward is a weighted combination of the per‑key scores, with the largest weights placed on the energy barriers and adsorption energies that are central to the catalytic mechanism. Missing keys or non‑numeric entries are heavily penalised. Merely guessing or copying a correct‑looking number without performing the underlying calculations will almost certainly fail the structural checks, so a genuine DFT workflow is required to obtain a high score.
