# Electronic structure and carrier mobility of boron-graphdiyne sheet and nanoribbons

## Problem background
Boron-graphdiyne (BGDY) is a recently synthesized two-dimensional carbon‑boron nanomaterial. Its π‑conjugated framework of all‑sp‑hybridized carbon skeletons and boron heteroatoms makes it a promising candidate for nanoelectronic and optoelectronic applications. Understanding its intrinsic electronic properties—particularly the band gap and charge carrier mobility—is essential for assessing its technological potential. This task concerns the first‑principles prediction of the electronic structure and room‑temperature carrier mobility of monolayer BGDY as well as its one‑dimensional zigzag and armchair nanoribbons. The goal is to compute these quantities using density functional theory (DFT) and deformation potential theory, following the published material’s atomic coordinates and computational protocol.

## Approach
The workflow proceeds in five stages. First, atomic structures of monolayer BGDY and hydrogen‑terminated zigzag and armchair nanoribbons of width N=4 and N=8 are built and fully relaxed with DFT using the PBE exchange‑correlation functional. Second, band structures are calculated at the PBE level; for the monolayer sheet, an additional HSE06 hybrid‑functional calculation is performed to obtain the quasiparticle band gap. Third, uniaxial strain is applied along the armchair and zigzag directions of the sheet and along the ribbon axis of each nanoribbon, and the total energies and band‑edge positions (conduction band minimum and valence band maximum) are recorded at each strain value. Fourth, effective masses for electrons and holes are extracted by fitting parabolic dispersions near the band edges; elastic moduli (C2D for the sheet, C1D for nanoribbons) are obtained from quadratic fits to the energy‑strain curves; deformation potential constants E1 are computed from the slopes of the band‑edge shifts versus strain. Finally, room‑temperature carrier mobilities are evaluated using the deformation‑potential mobility formulas for two‑dimensional and one‑dimensional systems, and all results are compiled into a single JSON file.

## Reproduction target
Produce a file `results.json` under `/app/outputs` that contains two top‑level keys: `2D_sheet` and `nanoribbons`. The `2D_sheet` object must report the HSE06 and PBE band gaps, effective masses (in units of free electron mass m0) for electrons and holes along the zigzag and armchair directions, the 2D elastic moduli C2D (N/m) for both directions, the deformation potential constants E1 (eV) for electrons and holes in each direction, and the room‑temperature electron and hole mobilities (cm²/V·s) along the zigzag and armchair directions. The `nanoribbons` array must include entries for zigzag and armchair ribbons of width N=4 and N=8, each giving the ribbon type, width, PBE band gap, effective masses (m0), 1D elastic modulus C1D (eV/cm), E1 for electrons and holes (eV), and the corresponding electron and hole mobilities (cm²/V·s). All numeric fields are mandatory; missing fields or an incomplete ribbon set will result in a low score.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Python3 with numpy, scipy: python3, numpy, scipy

## Workflow steps

### Step 1: Structure generation and optimization
- Role: process
- Action: Generate atomic structures of monolayer BGDY sheet and hydrogen-terminated zigzag (N=4,8) and armchair (N=4,8) nanoribbons. Perform full geometry relaxation using DFT (PBE functional, open-source code such as Quantum ESPRESSO).
- Evidence: `/app/outputs/optimized_structures.log`

### Step 2: Band structure calculations
- Role: process
- Action: Compute band structures at PBE level for the BGDY sheet orthogonal supercell and for each nanoribbon. For the monolayer sheet, additionally perform an HSE06 calculation to obtain the hybrid-functional band gap.
- Evidence: `/app/outputs/band_data.tar.gz`

### Step 3: Strain calculations
- Role: process
- Action: Apply uniaxial strain along the armchair and zigzag directions for the monolayer sheet, and along the ribbon direction for each nanoribbon. For each strain value, compute the total energy and the positions of the conduction band minimum (CBM) and valence band maximum (VBM).
- Evidence: `/app/outputs/strain_data.txt`

### Step 4: Parameter extraction
- Role: process
- Action: Fit parabolic functions to the CBM/VBM of the band structures to extract effective masses for electrons and holes. Fit the energy-strain curves to obtain elastic constants C2D (N/m) and C1D (eV/cm), and compute deformation potentials E1 from the slopes of band-edge versus strain.
- Evidence: `/app/outputs/parameters_extraction.log`

### Step 5: Mobility calculation and results compilation
- Role: scored (load-bearing)
- Action: Using the deformation potential theory mobility formulas for 2D and 1D systems, compute electron and hole mobilities at 300 K for the 2D sheet along zigzag and armchair directions, and for each nanoribbon along the ribbon direction. Compile all computed quantities (band gaps, effective masses, elastic moduli, deformation potentials, and carrier mobilities) into a single JSON file results.json according to the output schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"2D_sheet": {"bandgap_HSE06": float (eV), "bandgap_PBE": float (eV), "m_eff_e_zigzag": float (m0), "m_eff_h_zigzag": float (m0), "m_eff_e_armchair": float (m0), "m_eff_h_armchair": float (m0), "C2D_zigzag": float (N/m), "C2D_armchair": float (N/m), "E1_e_zigzag": float (eV), "E1_h_zigzag": float (eV), "E1_e_armchair": float (eV), "E1_h_armchair": float (eV), "mu_e_zigzag": float (cm2/Vs), "mu_h_zigzag": float (cm2/Vs), "mu_e_armchair": float (cm2/Vs), "mu_h_armchair": float (cm2/Vs)}, "nanoribbons": [{"type": "zigzag"|"armchair", "N": int, "bandgap_PBE": float (eV), "m_eff_e": float (m0), "m_eff_h": float (m0), "C1D": float (eV/cm), "E1_e": float (eV), "E1_h": float (eV), "mu_e": float (cm2/Vs), "mu_h": float (cm2/Vs)}]}
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
- target_policy: exact_match
- description: Compiled electronic structure and carrier mobility results for BGDY 2D sheet and nanoribbons. The checker compares all reported numerical values against the paper's published results within tolerances, and verifies that the nanoribbon bandgap decreases with ribbon width (N=4 > N=8 for both zigzag and armchair).
- schema:
  - `type`: object
  - `required`: `2D_sheet`, `nanoribbons`
  - `description`: 2D_sheet: object with fields bandgap_HSE06 (eV), bandgap_PBE (eV), effective masses m_eff_e/h for zigzag/armchair (in units of m0), elastic moduli C2D_zigzag/armchair (N/m), deformation potentials E1_e/h for zigzag/armchair (eV), mobilities mu_e/h for zigzag/armchair (cm2/Vs). nanoribbons: array of objects, each with type (zigzag/armchair), N (integer width), bandgap_PBE (eV), effective masses (m0), C1D (eV/cm), E1_e/h (eV), mu_e/h (cm2/Vs). Must include at least N=4 and N=8 for both zigzag and armchair types.

Notes: The hidden checker uses exact-match-with-tolerance for band gaps and mobilities, and additionally checks the structural trend that nanoribbon bandgap decreases with increasing width N.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "2D_sheet",
          "nanoribbons"
        ],
        "description": "2D_sheet: object with fields bandgap_HSE06 (eV), bandgap_PBE (eV), effective masses m_eff_e/h for zigzag/armchair (in units of m0), elastic moduli C2D_zigzag/armchair (N/m), deformation potentials E1_e/h for zigzag/armchair (eV), mobilities mu_e/h for zigzag/armchair (cm2/Vs). nanoribbons: array of objects, each with type (zigzag/armchair), N (integer width), bandgap_PBE (eV), effective masses (m0), C1D (eV/cm), E1_e/h (eV), mu_e/h (cm2/Vs). Must include at least N=4 and N=8 for both zigzag and armchair types."
      },
      "description": "Compiled electronic structure and carrier mobility results for BGDY 2D sheet and nanoribbons. The checker compares all reported numerical values against the paper's published results within tolerances, and verifies that the nanoribbon bandgap decreases with ribbon width (N=4 > N=8 for both zigzag and armchair)."
    }
  ],
  "notes": "The hidden checker uses exact-match-with-tolerance for band gaps and mobilities, and additionally checks the structural trend that nanoribbon bandgap decreases with increasing width N."
}
```

## How you are scored
A hidden verifier examines your submitted `results.json`. It checks that the file exists, is valid JSON, and contains all required fields with the correct types. The verifier then compares your computed values against independent reference values using tolerances appropriate for the computational methods used (e.g., the HSE06 band gap of the sheet is compared within an allowed deviation, and mobilities are checked with a relative tolerance). For the nanoribbons, the verifier additionally tests the structural trend that the band gap decreases as the ribbon width increases from N=4 to N=8 for each edge type. Each scored quantity contributes a weighted share to the final reward, with the main load‑bearing stage (mobility results) receiving the largest weight. Simply writing numbers that match known literature values is not sufficient; the verifier expects that you have actually executed the DFt workflow and derived the quantities from your own calculations.
