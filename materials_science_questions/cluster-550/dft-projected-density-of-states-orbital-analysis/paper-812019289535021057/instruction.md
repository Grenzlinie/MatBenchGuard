# DFT Equilibrium Properties of Fe-Mn-Al Medium Entropy Alloy Configurations

## Problem background
Medium entropy alloys (MEAs) and high entropy alloys possess complex local chemical environments that can strongly influence their mechanical and magnetic properties. Understanding how local lattice distortion and configurational microstates affect quantities such as equilibrium volume, magnetic moment, and electron work function is central to designing advanced multi-component alloys. In the ternary Fe-Mn-Al MEA system, distinct local atomic arrangements can lead to variations in these properties, providing a testbed for first-principles studies of the relationship between atomic-scale structure and macroscopic response. This task investigates such configurational effects by computing equilibrium properties from density functional theory for a set of representative random configurations of the alloy.

## Approach
The Similar Atomic Environment (SAE) method is used to generate representative random configurations of the BCC Fe-28Mn-18.5Al (wt%) alloy within a 3×3×6 supercell. The SAE objective function quantifies how well a configuration approximates a disordered solid solution, and Monte Carlo sampling yields 10 candidate structures. After a preliminary single-point DFT energy screening of the 10 candidates, the five with the lowest total energy are selected for detailed property calculations. For each of these five configurations a full DFT relaxation of volume and ionic positions is performed, followed by a static calculation to extract the total energy, Fermi energy, and magnetic moment. The electron work function is then estimated from the equilibrium density using the Halas-Durakiewicz model (Φ = 6.15 (r_s / a0)^{-1/2}, where r_s is derived from the composition-weighted atomic mass, valence, and the relaxed equilibrium density). All DFT calculations employ the GGA-PBE exchange-correlation functional and PAW pseudopotentials; an open-source plane-wave DFT code (e.g., Quantum ESPRESSO, ABINIT, or GPAW) is used.

## Reproduction target
Produce a CSV file named step_01_table.csv containing the following properties for the five best configurations (labelled Best-1 through Best-5): lattice constant a (Å), equilibrium volume V0 (Å³), total energy E0 (eV), Fermi energy EF (eV), magnetic moment μMag (μB per supercell), and electron work function Φ (eV). The columns must be exactly: config (string), a (float), V0 (float), E0 (float), EF (float), mu_Mag (float), Phi (float). The values must be computed by following the SAE+DFT workflow described above.

## Assets

- Similar Atomic Environment (SAE) method
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- SSSP PBE pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/
- Python 3 with pandas and numpy: pandas

## Workflow steps

### Step 1: SAE configuration generation
- Role: process
- Action: Construct a 3x3x6 supercell of BCC Fe-28Mn-18.5Al (wt%) with initial lattice parameter a=2.86 Å. Use the similar atomic environment (SAE) method to perform Monte Carlo sampling and generate 10 best candidate configurations according to the SAE objective function.
- Evidence: `/app/outputs/sae_candidates.json`

### Step 2: Preliminary DFT energy screening
- Role: process
- Action: For each of the 10 candidate configurations, perform a single-point DFT energy calculation using a plane-wave cutoff of 400 eV and a Γ-centered 5x5x3 k-point mesh. Select the five configurations with the lowest total energy.
- Evidence: `/app/outputs/selected_configs.json`

### Step 3: DFT relaxation and property calculation
- Role: process
- Action: For each of the five selected configurations, relax the structure (volume and ionic positions) using DFT (Methfessel-Paxton smearing), then perform a static calculation (tetrahedron method with Blöchl corrections) to obtain total energy, Fermi energy, magnetic moment, and equilibrium volume. Use a plane-wave cutoff of 400 eV and a Γ-centered 5x5x3 k-point mesh.
- Evidence: `/app/outputs/dft_log.txt`

### Step 4: Electron work function calculation
- Role: process
- Action: For each configuration, compute the electron work function Φ from the equilibrium density using the Halas-Durakiewicz model: Φ = 6.15 (r_s / a0)^{-1/2} where r_s = 1.3882 (M / (Z ρ))^{1/3}. Use the equilibrium density ρ from the relaxed volume and elemental atomic masses M and valences Z weighted by composition.
- Evidence: none

### Step 5: Output equilibrium properties
- Role: scored (load-bearing)
- Action: Collect the lattice constant a (Å), equilibrium volume V0 (Å³), total energy E0 (eV), Fermi energy EF (eV), magnetic moment μMag (μB per supercell), and electron work function Φ (eV) for each of the five configurations in the order Best-1 to Best-5. Write the results to step_01_table.csv.
- Output file: `/app/outputs/step_01_table.csv`
- Format: csv
- Contract: config (string), a (float, Å), V0 (float, Å³), E0 (float, eV), EF (float, eV), mu_Mag (float, μB/supercell), Phi (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_table.csv
- path: `/app/outputs/step_01_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing the computed equilibrium properties for the five best configurations (Best-1 to Best-5).
- schema:
  - `type`: table
  - `required_columns`: `config`, `a`, `V0`, `E0`, `EF`, `mu_Mag`, `Phi`
  - `items`:
    - `config`: string
    - `a`: float
    - `V0`: float
    - `E0`: float
    - `EF`: float
    - `mu_Mag`: float
    - `Phi`: float
  - `units`:
    - `a`: Å
    - `V0`: Å³
    - `E0`: eV
    - `EF`: eV
    - `mu_Mag`: μB/supercell
    - `Phi`: eV

Notes: Properties are compared to reference DFT values with appropriate tolerances to account for code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "config",
          "a",
          "V0",
          "E0",
          "EF",
          "mu_Mag",
          "Phi"
        ],
        "items": {
          "config": "string",
          "a": "float",
          "V0": "float",
          "E0": "float",
          "EF": "float",
          "mu_Mag": "float",
          "Phi": "float"
        },
        "units": {
          "a": "Å",
          "V0": "Å³",
          "E0": "eV",
          "EF": "eV",
          "mu_Mag": "μB/supercell",
          "Phi": "eV"
        }
      },
      "description": "CSV containing the computed equilibrium properties for the five best configurations (Best-1 to Best-5)."
    }
  ],
  "notes": "Properties are compared to reference DFT values with appropriate tolerances to account for code differences."
}
```

## How you are scored
A hidden verifier reads step_01_table.csv and compares every entry for the five configurations and six properties to independently held reference values using absolute tolerances appropriate for the quantity. The reward is the fraction of those configuration–property pairs that fall within the required tolerance; full credit is awarded when all thirty pairs are within tolerance. You do not need to match any specific table or figure from a publication; only the computed values in the CSV are judged.
