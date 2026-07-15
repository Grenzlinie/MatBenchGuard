# Si@C24N24 Catalyst for NO Reduction: Adsorption and Barrier Calculations

## Problem background
Nitric oxide (NO) is a hazardous atmospheric pollutant produced by combustion processes. Catalytic reduction of NO, particularly with carbon monoxide (CO) as a reducing agent, is an important strategy for emission control. Traditional noble-metal catalysts are effective but costly and scarce, motivating the search for metal-free alternatives. Porous nitrogen-doped carbon nanomaterials, such as porphyrin-like C24N24 fullerene, can be functionalized with a single silicon (Si) atom to create a stable, metal-free active site. This study explores whether Si-decorated C24N24 (Si@C24N24) can catalyse NO reduction by CO through a dimer mechanism, where two NO molecules combine and dissociate into N2O and an adsorbed oxygen atom (O_ads), followed by removal of O_ads by CO. The key open question is whether the computed binding strengths and activation barriers are compatible with catalytic activity at low temperature.

## Approach
The investigation uses dispersion-corrected density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) functional combined with Grimme's D3 van der Waals correction. An open-source plane-wave/pseudopotential DFT code (e.g., Quantum ESPRESSO) is employed to perform all calculations within a periodic supercell approach. The Si@C24N24 catalyst is built by placing a single Si atom into one of the N4 cavities of the known C24N24 fullerene. Reference energies are obtained for isolated NO and CO molecules. The adsorption of NO and CO on the catalyst is examined in two orientations each (via N or O for NO; via C or O for CO), yielding adsorption energies, Hirshfeld charge transfers, and Si–adsorbate bond lengths. The most stable co-adsorption structure of two NO molecules (the (NO)2 dimer) is then optimized. Minimum-energy pathways are computed using the nudged elastic band (NEB) method (or a comparable chain-of-states method) to locate transition states and activation barriers for (i) dissociation of the (NO)2 dimer into N2O + O_ads and (ii) the reaction O_ads + CO → CO2. All computed quantities are reported in kcal/mol (energies) and electrons (charges).

## Reproduction target
Produce the following three artifacts by performing DFT calculations with the PBE+D3 functional, a periodic supercell of at least 25 Å, and Γ-point Brillouin zone sampling:

1. A CSV file (`adsorption_energies.csv`) containing for four monomer adsorption configurations — NO (N‑site), NO (O‑site), CO (C‑site), CO (O‑site) — the adsorption energy (kcal/mol), net Hirshfeld charge transfer (e), and Si–adsorbate bond length (Å).
2. A text file (`dimer_dissociation_barrier.txt`) containing a single floating-point number: the activation energy (kcal/mol) for the dissociation of the (NO)2 dimer (D1 configuration) into N2O + O_ads on Si@C24N24.
3. A text file (`o_removal_barrier.txt`) containing a single floating-point number: the activation energy (kcal/mol) for the reaction O_ads + CO → CO2 on the same catalyst.

The target is to obtain these quantities by re-running the computational protocol with an open-source DFT implementation; the results should reflect the genuine physics of the system at the PBE+D3 level.

## Assets

- Quantum ESPRESSO open-source DFT code: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/pbe
- C24N24 porous fullerene initial geometry: 10.1021/jp3077586

## Workflow steps

### Step 1: Optimize isolated NO and CO molecules
- Role: process
- Action: Perform geometry optimization of isolated NO and CO molecules using the PBE functional with dispersion correction to obtain reference total energies and equilibrium bond lengths.
- Evidence: `/app/outputs/isolated_NO_CO_energies.txt`

### Step 2: Relax Si@C24N24 catalyst
- Role: process
- Action: Build the Si@C24N24 structure by placing a Si atom in the N4 cavity of C24N24 and perform geometry optimization to obtain the relaxed structure and total energy.
- Evidence: `/app/outputs/catalyst_relaxed.xyz`

### Step 3: Compute monomer NO and CO adsorption energies and Hirshfeld charges
- Role: scored (load-bearing)
- Action: For each of the four binding configurations (NO N-site, NO O-site, CO C-site, CO O-site), build the adsorbate-catalyst complex, optimize its geometry, and compute the adsorption energy E_ads = E_complex - E_adsorbate - E_catalyst. Use Hirshfeld charge analysis to obtain the net charge transfer q_CT and extract the Si-X bond distance.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: configuration (string), adsorption_energy_kcal_mol (float), hirshfeld_charge_transfer_e (float), bond_length_si_x_A (float). Rows: NO(N-site), NO(O-site), CO(C-site), CO(O-site).
- Scoring: scored by hidden verifier

### Step 4: Optimize D1 (NO)2 co-adsorption structure
- Role: process
- Action: Starting from the most stable NO monomer adsorbed state (N-site), add a second NO molecule and optimize the co-adsorption geometry to obtain the D1 (NO)2 dimer configuration.
- Evidence: `/app/outputs/dimer_D1_structure.xyz`

### Step 5: Compute D1 dimer dissociation barrier to N2O + O_ads
- Role: scored
- Action: Using the D1 co-adsorption structure, locate the transition state for dissociation into N2O + O_ads using NEB or comparable minimum-energy path method. Calculate the activation energy as the energy difference between the transition state and the D1 state.
- Output file: `/app/outputs/dimer_dissociation_barrier.txt`
- Format: txt
- Contract: Single floating-point number in kcal/mol.
- Scoring: scored by hidden verifier

### Step 6: Compute O_ads removal barrier by CO to form CO2
- Role: scored
- Action: From the O_ads-covered catalyst (post N2O desorption), build the co-adsorbed state with a CO molecule and locate the transition state for CO + O_ads -> CO2 using NEB or comparable method. Calculate the activation energy.
- Output file: `/app/outputs/o_removal_barrier.txt`
- Format: txt
- Contract: Single floating-point number in kcal/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/dimer_dissociation_barrier.txt`
- `/app/outputs/o_removal_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Four rows with adsorption energetics, charge transfer and Si-X bond distances for NO (N-site, O-site) and CO (C-site, O-site).
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `adsorption_energy_kcal_mol`, `hirshfeld_charge_transfer_e`, `bond_length_si_x_A`
  - `units`:
    - `adsorption_energy_kcal_mol`: kcal/mol
    - `hirshfeld_charge_transfer_e`: e
    - `bond_length_si_x_A`: angstrom

### dimer_dissociation_barrier.txt
- path: `/app/outputs/dimer_dissociation_barrier.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Activation energy in kcal/mol for D1 (NO)2 dimer dissociation into N2O + O_ads.
- schema:
  - `type`: text
  - `format`: single_float_kcal_mol

### o_removal_barrier.txt
- path: `/app/outputs/o_removal_barrier.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Activation energy in kcal/mol for O_ads removal by CO to form CO2.
- schema:
  - `type`: text
  - `format`: single_float_kcal_mol

Notes: All scored artifacts are compared against hidden reference values from the paper. Adsorption energies are more favourable when more negative; barriers are better when lower. The checker uses threshold_or_better with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "adsorption_energy_kcal_mol",
          "hirshfeld_charge_transfer_e",
          "bond_length_si_x_A"
        ],
        "units": {
          "adsorption_energy_kcal_mol": "kcal/mol",
          "hirshfeld_charge_transfer_e": "e",
          "bond_length_si_x_A": "angstrom"
        }
      },
      "description": "Four rows with adsorption energetics, charge transfer and Si-X bond distances for NO (N-site, O-site) and CO (C-site, O-site)."
    },
    {
      "file": "dimer_dissociation_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "format": "single_float_kcal_mol"
      },
      "description": "Activation energy in kcal/mol for D1 (NO)2 dimer dissociation into N2O + O_ads."
    },
    {
      "file": "o_removal_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "format": "single_float_kcal_mol"
      },
      "description": "Activation energy in kcal/mol for O_ads removal by CO to form CO2."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values from the paper. Adsorption energies are more favourable when more negative; barriers are better when lower. The checker uses threshold_or_better with appropriate tolerances."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier that independently inspects each of the three scored output files. The verifier compares your reported numbers against hidden reference values (obtained from a reliable source) using a threshold-or-better policy:
- For adsorption energies (where more negative indicates stronger binding), a value more negative than or equal to the reference (within a tolerance) earns full credit; less negative values receive proportionally lower credit.
- For activation barriers (where lower is better), a value lower than or equal to the reference (within a tolerance) earns full credit; higher barriers receive proportionally lower credit.
- Structural checks (e.g., valid file format, correct number of rows/entries) carry small weight.
The three scored artifacts are weighted to produce a final reward between 0 and 1. You must genuinely execute the DFT workflow to obtain the submitted quantities; simply copying reference values will likely miss the tolerance and yield a low reward. The exact tolerance is not disclosed.
