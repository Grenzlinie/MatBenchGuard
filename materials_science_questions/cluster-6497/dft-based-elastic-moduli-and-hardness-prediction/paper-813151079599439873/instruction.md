# Site preference and elastic properties of transition-metal solutes in B2 RuAl

## Problem background
B2 RuAl intermetallic possesses a high melting point, good high-temperature strength, and promising room-temperature toughness, making it a candidate for demanding structural applications. Adding transition‑metal (TM) solutes alters the site occupancy on the Al and Ru sublattices and modifies the mechanical properties, especially the single‑crystal elastic constants and the derived polycrystalline moduli. Understanding these effects is critical for alloy design. In this task you will reproduce a first‑principles DFT study that determines site preferences of TM solutes in B2 RuAl and quantifies their influence on elastic properties. The workflow also examines the relationship between bulk modulus and electron density, providing a quantitative map of how alloying changes the mechanical response.

## Approach
The approach combines plane‑wave density‑functional theory (DFT) within the generalized gradient approximation (PBE) with a supercell model. You will construct 16‑atom supercells of B2 RuAl and substitute a single TM atom at either an Al or a Ru site. Total energy calculations on these supercells yield transfer energies, from which site preferences are assigned via the Ruban–Skriver rule. For the preferred‑site configurations, single‑crystal elastic constants (C₁₁, C₁₂, C₄₄) are obtained by applying small strains and computing the resulting stress tensors. Voigt–Reuss–Hill averaging then gives the polycrystalline bulk modulus, shear modulus, Young’s modulus, Poisson’s ratio, and Zener anisotropy. Electron densities are calculated from the atomic volume and bonding valence (Rose–Shore model) to explore the correlation with bulk modulus. All calculations are to be performed with an open‑source DFT code (e.g., Quantum ESPRESSO) using publicly available pseudopotentials.

## Reproduction target
Compute transfer energies and site preferences for the solutes Ti, Ni, and W in B2 RuAl using the Ruban–Skriver methodology, and report the exchange antisite formation energy. Then, for pure RuAl and for each ternary alloy with the solute on its preferred site (Ru₈Al₇Ti, Ru₇Al₈Ni, Ru₈Al₇W), compute the single‑crystal elastic constants C₁₁, C₁₂, C₄₄ and the derived polycrystalline moduli: bulk modulus B, Voigt–Reuss–Hill shear modulus G, Young’s modulus E, Poisson’s ratio ν, and Zener anisotropy A_Z. Finally, for the same four compositions, compute electron densities and pair them with the corresponding bulk moduli to verify the near‑linear correlation between electron density and bulk modulus.

## Assets

- B2 RuAl crystal structure: https://materialsproject.org/materials/mp-1218
- Pseudopotentials for Ru, Al, Ti, Ni, W (PBE form): https://www.materialscloud.org/discover/sssp/table/efficiency
- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org
- Bonding valence data for pure elements (Rose-Shore model): 10.1103/PhysRevB.48.18254

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct 16-atom supercells from the B2 RuAl conventional cell: Ru₈Al₈, Ru₉Al₇, and for TM = Ti, Ni, W the substitutional alloys Ru₈Al₇TM (TM on Al site) and Ru₇Al₈TM (TM on Ru site). Use lattice parameter ~3.005 Å as starting point.
- Evidence: `/app/outputs/supercells.cif`

### Step 2: DFT total energy calculations
- Role: process
- Action: Perform DFT geometry optimization and total energy calculation for all supercells of step1 using GGA-PBE, with plane-wave cutoff >= 450 eV, a Monkhorst–Pack k-point mesh appropriate for 16-atom supercells, and self-consistency convergence 10⁻⁶ eV/atom. Use Quantum ESPRESSO (or another open-source DFT code). Save the final total energies.
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Transfer energy and site preference
- Role: scored (load-bearing)
- Action: From the total energies, compute E(Ru_Al) = E(Ru₉Al₇) - E(Ru₈Al₈) and then for each TM the transfer energy E_TM(Al→Ru) = E(Ru₇Al₈TM) - E(Ru₈Al₇TM) + E(Ru_Al). Determine E_Antisite from the formation energy of the exchange antisite. Assign site preference using the Ruban–Skriver rule: negative transfer energy ⇒ strong Ru-site preference; transfer energy > E_Antisite ⇒ strong Al-site preference; otherwise random. Output the results for Ti, Ni, and W as a JSON file.
- Output file: `/app/outputs/site_preference.json`
- Format: json
- Contract: object with keys 'Ti','Ni','W', each containing 'transfer_energy_eV' (float) and 'site_preference' (string: 'Al','Ru','random'), plus top-level key 'E_Antisite_eV' (float).
- Scoring: scored by hidden verifier

### Step 4: DFT elastic constants calculation
- Role: process
- Action: For pure RuAl and for each TM at its preferred site (Ru₈Al₇Ti, Ru₇Al₈Ni, Ru₈Al₇W), apply small strains to the optimized supercells and compute the resulting stress tensors via DFT to obtain single-crystal elastic constants C₁₁, C₁₂, C₄₄. Use the same DFT parameters as in step2.
- Evidence: `/app/outputs/elastic_raw.json`

### Step 5: Elastic constants and polycrystalline moduli
- Role: scored
- Action: From C₁₁, C₁₂, C₄₄ obtained in step4, compute bulk modulus B = (C₁₁+2C₁₂)/3, Voigt–Reuss–Hill shear modulus G, Young's modulus E, Poisson's ratio ν, and Zener anisotropy A_Z. Output the results as a JSON file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: object with keys 'pure_RuAl', 'Ru8Al7Ti', 'Ru7Al8Ni', 'Ru8Al7W'. Each value is an object with numeric fields: 'C11_GPa', 'C12_GPa', 'C44_GPa', 'B_GPa', 'G_GPa', 'E_GPa', 'nu' (float), 'A_Z' (float).
- Scoring: scored by hidden verifier

### Step 6: Electron density and bulk modulus correlation
- Role: scored
- Action: For each composition (pure RuAl, Ru₈Al₇Ti, Ru₇Al₈Ni, Ru₈Al₇W), compute the atomic volume V_M from the optimized lattice parameter, obtain bonding valence Z_B using the Rose–Shore model (literature values), and calculate electron density n = Z_B / V_M. Pair each n with the corresponding bulk modulus B from step5. Output the results as a JSON file.
- Output file: `/app/outputs/electron_density_bulk_modulus.json`
- Format: json
- Contract: object with keys 'pure_RuAl', 'Ru8Al7Ti', 'Ru7Al8Ni', 'Ru8Al7W'. Each value is an object with fields: 'electron_density_el_per_atom' (float) and 'bulk_modulus_GPa' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/site_preference.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/electron_density_bulk_modulus.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### site_preference.json
- path: `/app/outputs/site_preference.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Transfer energies and site preference assignments for representative solutes Ti, Ni, W, plus the exchange antisite formation energy.
- schema:
  - `type`: object
  - `required`:
    - `Ti`: object
    - `Ni`: object
    - `W`: object
    - `E_Antisite_eV`: float
  - `items`:
    - `transfer_energy_eV`: float
    - `site_preference`: string (Al, Ru, random)

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic constants and derived polycrystalline moduli for pure RuAl and three ternary alloys at their preferred sites.
- schema:
  - `type`: object
  - `required`:
    - `pure_RuAl`: object
    - `Ru8Al7Ti`: object
    - `Ru7Al8Ni`: object
    - `Ru8Al7W`: object
  - `items`:
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C44_GPa`: float
    - `B_GPa`: float
    - `G_GPa`: float
    - `E_GPa`: float
    - `nu`: float
    - `A_Z`: float

### electron_density_bulk_modulus.json
- path: `/app/outputs/electron_density_bulk_modulus.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electron densities and bulk moduli for the four compositions; used to verify the linear correlation (Spearman rank ≥0.8) and monotonic increase.
- schema:
  - `type`: object
  - `required`:
    - `pure_RuAl`: object
    - `Ru8Al7Ti`: object
    - `Ru7Al8Ni`: object
    - `Ru8Al7W`: object
  - `items`:
    - `electron_density_el_per_atom`: float
    - `bulk_modulus_GPa`: float

Notes: No gold values or tolerances are disclosed here. The checker compares transfer energies and elastic constants to hidden paper-reported references with tolerances, and evaluates the electron-density–bulk-modulus trend via rank correlation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "site_preference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ti": "object",
          "Ni": "object",
          "W": "object",
          "E_Antisite_eV": "float"
        },
        "items": {
          "transfer_energy_eV": "float",
          "site_preference": "string (Al, Ru, random)"
        }
      },
      "description": "Transfer energies and site preference assignments for representative solutes Ti, Ni, W, plus the exchange antisite formation energy."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pure_RuAl": "object",
          "Ru8Al7Ti": "object",
          "Ru7Al8Ni": "object",
          "Ru8Al7W": "object"
        },
        "items": {
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C44_GPa": "float",
          "B_GPa": "float",
          "G_GPa": "float",
          "E_GPa": "float",
          "nu": "float",
          "A_Z": "float"
        }
      },
      "description": "Single-crystal elastic constants and derived polycrystalline moduli for pure RuAl and three ternary alloys at their preferred sites."
    },
    {
      "file": "electron_density_bulk_modulus.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "pure_RuAl": "object",
          "Ru8Al7Ti": "object",
          "Ru7Al8Ni": "object",
          "Ru8Al7W": "object"
        },
        "items": {
          "electron_density_el_per_atom": "float",
          "bulk_modulus_GPa": "float"
        }
      },
      "description": "Electron densities and bulk moduli for the four compositions; used to verify the linear correlation (Spearman rank ≥0.8) and monotonic increase."
    }
  ],
  "notes": "No gold values or tolerances are disclosed here. The checker compares transfer energies and elastic constants to hidden paper-reported references with tolerances, and evaluates the electron-density–bulk-modulus trend via rank correlation."
}
```

## How you are scored
A hidden verifier independently inspects your three scored output files and compares them against reference results from the original study. Each file is evaluated with tolerances appropriate for computational reproduction: transfer energies, elastic constants, and derived moduli are checked for closeness to the expected values; site preference labels must match exactly; and the electron‑density–bulk‑modulus data are checked for consistency with your own elastic constants and for a clear monotonic trend (the bulk modulus must increase with electron density). The final reward is a weighted combination of these stage scores. You must actually run the DFT workflow; merely copying reference numbers is not sufficient to pass the verification checks.
