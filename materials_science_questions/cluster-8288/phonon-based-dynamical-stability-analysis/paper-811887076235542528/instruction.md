# Phonon-stability analysis of La-H supercell models

## Problem background
The lanthanum-hydrogen system exhibits a concentration-dependent metal-insulator transition near LaH2.8 and the so-called "switchable mirror" phenomenon, both of which depend critically on the crystal structure adopted by the La host lattice. At low temperatures, pure La exists in the double-hexagonal close-packed (dhcp) structure, but as hydrogen is incorporated, the face-centred cubic (fcc) lattice appears and eventually dominates. Which of these two La sublattices is dynamically stable — i.e., supports all harmonic vibrations with real (positive) phonon frequencies — at a given hydrogen content is an open question that must be resolved to understand the phase diagram and the onset of the metal-insulator transition. This task asks you to compute the phonon frequencies for well-defined La-H model supercells at two different hydrogen concentrations and to decide, on the basis of those frequencies, whether each lattice is vibrationally stable or unstable.

## Approach
You will build four La-H supercell models, two for the dhcp lattice and two for the fcc lattice, each containing a single hydrogen atom placed at an octahedral interstitial site (the site that first-principles calculations suggest is energetically favourable at low H content). For each model you will perform first-principles DFT structure relaxation using a plane-wave code with PAW-based pseudopotentials and the GGA-PBE exchange-correlation functional, then compute the harmonic phonon dispersion via the finite-displacement method. From the full list of phonon frequencies you will extract the global minimum frequency and classify each structure as dynamically stable if all frequencies are non-negative (i.e., no imaginary modes, allowing for small numerical noise) or as unstable if imaginary (negative) modes appear. By comparing the stability of dhcp and fcc lattices at the two hydrogen concentrations, you are able to determine how the vibrational stability of the La lattice changes with composition.

## Reproduction target
Reproduce the dynamical stability classification for the following four La-H supercell models: dhcp La36H (36 La atoms, one H), fcc La32H (32 La atoms, one H), dhcp La16H (16 La atoms, one H), and fcc La16H (16 La atoms, one H). For each structure you must (1) compute the full phonon dispersion and save the raw frequencies in /app/outputs/phonon_frequencies.json, and (2) determine the minimum phonon frequency and derive the stability label (true = stable, false = unstable) in /app/outputs/phonon_stability_results.json. The stability criterion is based solely on the computed phonon frequencies: a structure is considered dynamically stable if it exhibits no imaginary modes (all frequencies are non-negative within a tolerance that absorbs numerical noise); otherwise it is unstable.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP efficiency pseudopotentials (PBE PAW for La and H): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE or Pymatgen (optional): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build La-H supercell models
- Role: process
- Action: Construct the four supercell models: dhcp La16H (2x2x1 conventional cell with 16 La atoms), dhcp La36H (3x3x1 with 36 La atoms), fcc La32H (2x2x2 cubic supercell with 32 La atoms), and fcc La16H (rhombohedral 16-atom cell derived from the 32-atom fcc cell). Insert a single hydrogen atom at an octahedral interstitial site in each supercell. Generate input files for DFT calculations (e.g., POSCAR).
- Evidence: `/app/outputs/model_structures.txt`

### Step 2: DFT structure relaxation
- Role: process
- Action: Perform DFT structure optimization (ionic positions and cell parameters) for each of the four La-H models using Quantum ESPRESSO with PAW-PBE pseudopotentials. Save the relaxed atomic positions and cell parameters.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Phonon dispersion calculation
- Role: scored
- Action: Using the relaxed structures, compute phonon frequencies for each model via the finite-displacement method (e.g., Phonopy). Write the complete list of phonon frequencies (in cm⁻¹) at all computed q-points for each structure to /app/outputs/phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with top-level keys: 'dhcp_La36H', 'fcc_La32H', 'dhcp_La16H', 'fcc_La16H'. Each value is an object containing: 'q_points' (list of arrays of three floats, fractional coordinates), 'bands' (list of lists; each inner list gives the frequencies for one band at all q-points, in cm⁻¹), and optionally 'total_energy_per_cell' (float).
- Scoring: scored by hidden verifier

### Step 4: Stability assessment
- Role: scored
- Action: From the phonon frequencies computed in step3, determine for each structure the global minimum phonon frequency (in cm⁻¹) and assess dynamical stability: if all frequencies are positive (no imaginary modes, or minimum >= -10 cm⁻¹ within numerical noise), mark as stable; otherwise unstable. Write the results to /app/outputs/phonon_stability_results.json.
- Output file: `/app/outputs/phonon_stability_results.json`
- Format: json
- Contract: JSON object with top-level keys: 'dhcp_La36H', 'fcc_La32H', 'dhcp_La16H', 'fcc_La16H'. Each value is an object with fields: 'minimum_phonon_frequency_cm-1' (float), 'stable' (boolean), 'details' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.json`
- `/app/outputs/phonon_stability_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw phonon frequencies for the four La-H supercell models. The checker uses this to recompute stability.
- schema:
  - `type`: object
  - `required`:
    - `dhcp_La36H`: object
    - `fcc_La32H`: object
    - `dhcp_La16H`: object
    - `fcc_La16H`: object
  - `items`: object
  - `description`: Each key's value is an object with: 'q_points' (array of arrays of three floats), 'bands' (array of arrays of floats, frequencies in cm⁻¹), and optional 'total_energy_per_cell'.

### phonon_stability_results.json
- path: `/app/outputs/phonon_stability_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-reported stability classification and minimum phonon frequency for each model. The checker recomputes stability from phonon_frequencies.json and compares for consistency; the main reward is based on comparison of recomputed stability to hidden paper-reported labels.
- schema:
  - `type`: object
  - `required`:
    - `dhcp_La36H`:
      - `minimum_phonon_frequency_cm-1`: float
      - `stable`: boolean
      - `details`: string
    - `fcc_La32H`:
      - `minimum_phonon_frequency_cm-1`: float
      - `stable`: boolean
      - `details`: string
    - `dhcp_La16H`:
      - `minimum_phonon_frequency_cm-1`: float
      - `stable`: boolean
      - `details`: string
    - `fcc_La16H`:
      - `minimum_phonon_frequency_cm-1`: float
      - `stable`: boolean
      - `details`: string
  - `items`: object

Notes: The task is scoped to the four model structures that underpin the dynamical stability crossover. Formation energies, electronic band structures, and other compositions are omitted. The hidden gold consists of paper-reported stability labels (dhcp La36H: stable, fcc La32H: unstable, dhcp La16H: unstable, fcc La16H: stable).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "dhcp_La36H": "object",
          "fcc_La32H": "object",
          "dhcp_La16H": "object",
          "fcc_La16H": "object"
        },
        "items": {},
        "description": "Each key's value is an object with: 'q_points' (array of arrays of three floats), 'bands' (array of arrays of floats, frequencies in cm⁻¹), and optional 'total_energy_per_cell'."
      },
      "description": "Raw phonon frequencies for the four La-H supercell models. The checker uses this to recompute stability."
    },
    {
      "file": "phonon_stability_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "dhcp_La36H": {
            "minimum_phonon_frequency_cm-1": "float",
            "stable": "boolean",
            "details": "string"
          },
          "fcc_La32H": {
            "minimum_phonon_frequency_cm-1": "float",
            "stable": "boolean",
            "details": "string"
          },
          "dhcp_La16H": {
            "minimum_phonon_frequency_cm-1": "float",
            "stable": "boolean",
            "details": "string"
          },
          "fcc_La16H": {
            "minimum_phonon_frequency_cm-1": "float",
            "stable": "boolean",
            "details": "string"
          }
        },
        "items": {}
      },
      "description": "Agent-reported stability classification and minimum phonon frequency for each model. The checker recomputes stability from phonon_frequencies.json and compares for consistency; the main reward is based on comparison of recomputed stability to hidden paper-reported labels."
    }
  ],
  "notes": "The task is scoped to the four model structures that underpin the dynamical stability crossover. Formation energies, electronic band structures, and other compositions are omitted. The hidden gold consists of paper-reported stability labels (dhcp La36H: stable, fcc La32H: unstable, dhcp La16H: unstable, fcc La16H: stable)."
}
```

## How you are scored
The hidden verifier scores your submitted artifacts in two ways. (1) It reads your raw phonon frequencies from /app/outputs/phonon_frequencies.json and independently recomputes the global minimum frequency and stability classification for each structure. It then compares your reported stability labels and minimum frequencies in /app/outputs/phonon_stability_results.json to these recomputed values; a self-consistent report earns partial credit. (2) The verifier also compares the recomputed stability labels against hidden reference labels. The final reward (a single number between 0 and 1) is a weighted sum of the two checks, with the main weight on agreement with the hidden labels. The verifier does not require a reproduction of any particular raw frequency value; it evaluates whether your phonon calculations correctly support your stability conclusions and whether those conclusions match the expected physical outcome.
