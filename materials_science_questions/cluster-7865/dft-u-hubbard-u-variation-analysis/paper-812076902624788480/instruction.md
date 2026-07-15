# LDA+U Calculation for NaTiSi2O6: Ground State and Exchange Couplings

## Problem background
A spin gap observed in the pyroxene compound NaTiSi2O6 was originally attributed to the formation of singlet Ti–Ti dimers. A later density-functional study using a gradient approximation without explicit correlation corrections argued that the material instead evolves into a Haldane spin-1 chain phase. Because NaTiSi2O6 is a Mott insulator, electronic correlations on the Ti 3d shell are expected to be crucial. Resolving this controversy therefore requires a first-principles treatment that properly accounts for strong on-site Coulomb and Hund exchange interactions. The objective is to determine the magnetic ground state and electronic structure of NaTiSi2O6 at low temperature (100 K) using LDA+U, and to derive the inter- and intra-dimer exchange couplings that govern the low-energy spin physics.

## Approach
The calculation uses the spin-polarized LDA+U method with an on-site Coulomb U = 3.3 eV and Hund’s exchange J_H = 0.8 eV on the Ti 3d states. The crystal structure is taken from the low-temperature (100 K) phase. Four collinear magnetic configurations spanning the two inequivalent Ti–Ti dimers in the unit cell are examined: (i) AFM, with antiferromagnetic coupling both within and between dimers; (ii) F+AF, with ferromagnetic inter-dimer and antiferromagnetic intra-dimer coupling; (iii) AF+F, the reverse; and (iv) FM, with all spins parallel. For each configuration, the total energy, Ti spin moment, and Kohn–Sham band gap are computed. Inter- and intra-dimer exchange coupling constants are then extracted from the total energy differences: J_inter = E(F+AF) − E(AFM) and J_intra = E(AF+F) − E(AFM), converted to kelvin using 1 meV = 11.6045 K. All results are reported in a single JSON file.

## Reproduction target
Compute, for each of the four magnetic configurations (AFM, F+AF, AF+F, FM), the total energy per Ti–Ti dimer (in meV, referenced to the lowest-energy configuration), the local spin magnetic moment on Ti (in μ_B), and the electronic band gap (in eV). From the total energies, derive the inter-dimer exchange coupling J_inter and intra-dimer exchange coupling J_intra in kelvin. Report all quantities in the JSON file /app/outputs/results.json according to the output contract.

## Assets

- Crystal structure of NaTiSi2O6 at 100 K: 10.1107/S0108768103015833
- DFT code with LDA+U capability: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: LDA+U calculations and exchange coupling analysis
- Role: scored (load-bearing)
- Action: Perform spin-polarized LDA+U calculations for the low-temperature (100 K) crystal structure of NaTiSi2O6. Use the on-site Coulomb parameter U = 3.3 eV and Hund's exchange J_H = 0.8 eV for the Ti 3d electrons. Compute four collinear magnetic configurations: AFM (↑–↓↑–↓), F+AF (↑–↓↓–↑), AF+F (↑–↑↓–↓), and FM (↑–↑↑–↑). For each configuration, extract the total energy per Ti–Ti dimer (in meV, relative to the lowest energy), the local spin moment on Ti (in μ_B), and the electronic band gap (in eV). From the total energies, derive the inter-dimer exchange coupling J_inter = E(F+AF) – E(AFM) (convert to K using 1 meV = 11.6045 K) and the intra-dimer exchange coupling J_intra = E(AF+F) – E(AFM). Report all results in a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'configurations' (array of objects, each with 'magnetic_ordering' (string), 'total_energy_meV' (number), 'spin_moment_muB' (number), 'band_gap_eV' (number)), and 'derived_exchange_couplings' (object with 'J_inter_K' (number) and 'J_intra_K' (number)).
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
- description: Total energies, magnetic moments, band gaps for the four magnetic configurations, and the derived exchange couplings J_inter and J_intra. The hidden checker compares these values against the paper's reported reference values with tolerances (exact tolerances not disclosed).
- schema:
  - `type`: object
  - `required`:
    - `configurations`: array
    - `derived_exchange_couplings`: object
  - `items`:
    - `magnetic_ordering`: string
    - `total_energy_meV`: number
    - `spin_moment_muB`: number
    - `band_gap_eV`: number
  - `derived_fields`:
    - `J_inter_K`: number
    - `J_intra_K`: number

Notes: The agent must run the four DFT calculations from scratch; pre-existing outputs from other sources are not permitted. The score is based on agreement with the paper's Table I values and the correct ordering of total energies.

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
        "type": "object",
        "required": {
          "configurations": "array",
          "derived_exchange_couplings": "object"
        },
        "items": {
          "magnetic_ordering": "string",
          "total_energy_meV": "number",
          "spin_moment_muB": "number",
          "band_gap_eV": "number"
        },
        "derived_fields": {
          "J_inter_K": "number",
          "J_intra_K": "number"
        }
      },
      "description": "Total energies, magnetic moments, band gaps for the four magnetic configurations, and the derived exchange couplings J_inter and J_intra. The hidden checker compares these values against the paper's reported reference values with tolerances (exact tolerances not disclosed)."
    }
  ],
  "notes": "The agent must run the four DFT calculations from scratch; pre-existing outputs from other sources are not permitted. The score is based on agreement with the paper's Table I values and the correct ordering of total energies."
}
```

## How you are scored
A hidden verifier will parse /app/outputs/results.json and compare the reported total energies, spin moments, band gaps, and exchange couplings against reference values that correspond to a correct LDA+U calculation for this system at the specified parameters. The verifier will check that the computed total energies exhibit the correct relative ordering across the four magnetic configurations—for example, that one configuration has the lowest energy, another is slightly higher, while the remaining configurations are significantly higher. The score is a weighted combination of correct ordering and numerical agreement within physically reasonable tolerances. Simply reporting a number without performing the calculations is not sufficient; the full workflow must be executed.
