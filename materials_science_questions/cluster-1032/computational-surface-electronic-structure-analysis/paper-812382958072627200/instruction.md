# Electronic structure and surface states of a Ca(001) five-layer film from density-functional theory

## Problem background
The electron response of a metal surface to an external electrostatic field governs phenomena such as work-function changes, screening, and the formation of surface electronic states. These effects are sensitive to the metal's electronic structure and can be studied from first principles using density-functional theory (DFT). This task focuses on calcium, a metal with a nearly free-electron character but with notable d-electron contributions near the Fermi level. The goal is to understand how the electronic density of states (DOS) of a thin Ca(001) film differs from that of bulk calcium, and to map the energy positions of occupied and unoccupied surface states that arise when excess charge is added to the film. The quantities of interest—work function, DOS peak shifts, and surface-state energies—provide a detailed picture of the electrostatic response of the Ca(001) surface.

## Approach
The approach is based on self-consistent DFT slab calculations using the local-density approximation (LDA) with the Hedin-Lundqvist exchange-correlation functional and the experimental fcc lattice constant of calcium (10.5296 atomic units). First, a reference bulk Ca calculation provides the total and partial (s, p, d) densities of states. Then a neutral symmetric five-layer Ca(001) slab with sufficient vacuum is simulated to obtain the film DOS and the planar-averaged electrostatic potential. The work function is extracted from the potential profile. To identify surface states, additional calculations are run with small excess charges per unit cell (q = 0.01 and q = 0.03 electrons). For each charge state the total DOS is computed. After applying a Stark shift that aligns the bulk-like features, the difference in the DOS between charged and neutral films (Δn) reveals signatures of surface states: local minima in Δn correspond to maxima in the surface-state density. The workflow yields quantitative values for the work function, the energy shifts of three principal DOS maxima (I, II, III) between bulk and film, and the energies of occupied (a1–a5) and unoccupied (b1–b4) surface states relative to the neutral film's Fermi level.

## Reproduction target
Reproduce the following four scored quantities from the Ca(001) five-layer film DFT calculations:

1. The work function (in eV), extracted from the electrostatic potential of the neutral film.
2. The energy shifts (in eV) of the three main DOS maxima (I, II, III) when going from bulk Ca to the neutral Ca(001) film (positive shift = closer to the Fermi level).
3. The energies (in eV) of occupied surface states a1 through a5, obtained from the Δn analysis at excess charges q = 0.01 and q = 0.03, referenced to the neutral film's Fermi level.
4. The energies (in eV) of unoccupied surface states b1 through b4, obtained from the same Δn analysis at q = 0.01 and q = 0.03, referenced to the neutral film's Fermi level.

All results must be produced by executing the DFT workflow and the subsequent analysis steps; no pre-computed values are provided.

## Assets

- Open-source density-functional-theory code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/download
- LDA pseudopotential for calcium: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Bulk calcium density of states reference calculation
- Role: process
- Action: Perform a self-consistent DFT calculation for bulk fcc calcium using the local-density approximation (Hedin-Lundqvist) and lattice constant 10.5296 au. Compute the total and s, p, d partial densities of states to serve as the reference for film DOS comparison.
- Evidence: `/app/outputs/step_1_bulk_dos.dat`

### Step 2: Neutral Ca(001) five-layer film self-consistent DFT calculation
- Role: process
- Action: Set up a symmetric five-layer Ca(001) slab with fcc(001) surface orientation, lattice constant 10.5296 au, and sufficient vacuum (≥15 Å). Perform a self-consistent DFT calculation with LDA (Hedin-Lundqvist) to obtain the total density of states and the planar-averaged electrostatic potential. Extract the vacuum potential and the Fermi level.
- Evidence: `/app/outputs/step_2_neutral_film.log`

### Step 3: Charged Ca(001) film DFT calculations for q=0.01 and q=0.03
- Role: process
- Action: Starting from the converged neutral film calculation, add excess electrons per unit cell corresponding to q=0.01 and q=0.03. Run separate self-consistent DFT calculations for each charge state, computing the total density of states.
- Evidence: `/app/outputs/step_3_charged_outputs.log`

### Step 4: Extract work function
- Role: scored
- Action: From the neutral film electrostatic potential, compute the work function as W = V_vacuum - E_Fermi (in eV). Write the single number to work_function.txt.
- Output file: `/app/outputs/work_function.txt`
- Format: txt
- Contract: A single floating-point number representing the work function in eV.
- Scoring: scored by hidden verifier

### Step 5: Compute DOS maxima shifts (I, II, III) between bulk and film
- Role: scored
- Action: Align the energy scales of the bulk Ca DOS (step_1) and the neutral film DOS (step_2) (e.g., by matching the Fermi levels or aligning prominent bulk-like features). Identify the three main maxima I, II, III in the relevant energy region. For each maximum, measure the energy shift (film position minus bulk position, positive = closer to Fermi level). Write the shifts to dos_shifts.csv with columns: maxima (string), shift_eV (float).
- Output file: `/app/outputs/dos_shifts.csv`
- Format: csv
- Contract: CSV with columns: maxima (string, one of 'I','II','III'), shift_eV (float).
- Scoring: scored by hidden verifier

### Step 6: Extract occupied surface state energies (a1–a5)
- Role: scored (load-bearing)
- Action: For each excess charge q=0.01 and 0.03, compute the difference in densities of states Δn(q,E) = n_charged(E + C(q), q) - n_neutral(E,0). Determine the Stark shift C(q) (e.g., from the dipole-moment change or by aligning bulk-like features). Shift the charged DOS by C(q), then subtract the neutral DOS. Identify local minima in Δn(q,E) that correspond to maxima in the surface-state density. For occupied states (energies below the neutral film Fermi level), locate the five features a1–a5. Report their energies (in eV, relative to the neutral film's Fermi level) in occupied_surface_states.csv with columns: feature (string), q (float), energy (float).
- Output file: `/app/outputs/occupied_surface_states.csv`
- Format: csv
- Contract: CSV with columns: feature (e.g., 'a1'), q (0.01 or 0.03), energy (float, eV, negative values).
- Scoring: scored by hidden verifier

### Step 7: Extract unoccupied surface state energies (b1–b4)
- Role: scored (load-bearing)
- Action: Using the same Δn(q,E) procedure as for occupied states, identify the four unoccupied surface-state features b1–b4 (positive energies relative to the neutral film Fermi level). Report their energies in unoccupied_surface_states.csv with the same format.
- Output file: `/app/outputs/unoccupied_surface_states.csv`
- Format: csv
- Contract: CSV with columns: feature (e.g., 'b1'), q (0.01 or 0.03), energy (float, eV, positive values).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/work_function.txt`
- `/app/outputs/dos_shifts.csv`
- `/app/outputs/occupied_surface_states.csv`
- `/app/outputs/unoccupied_surface_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly. The verifier checks only the four output files listed below; intermediate files (step_1_bulk_dos.dat, step_2_neutral_film.log, step_3_charged_outputs.log) are not scored but may be kept for your own records.

### work_function.txt
- path: `/app/outputs/work_function.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Work function of the Ca(001) five-layer film.
- schema:
  - `type`: text
  - `unit`: eV
  - `description`: A single floating-point number representing the work function of the Ca(001) five-layer film.

### dos_shifts.csv
- path: `/app/outputs/dos_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Shifts of the three main DOS maxima from bulk Ca to the Ca(001) film.
- schema:
  - `type`: table
  - `required_columns`: `maxima`, `shift_eV`
  - `columns`:
    - `maxima`: string
    - `shift_eV`: float

### occupied_surface_states.csv
- path: `/app/outputs/occupied_surface_states.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energies of occupied surface states (a1–a5).
- schema:
  - `type`: table
  - `required_columns`: `feature`, `q`, `energy`
  - `columns`:
    - `feature`: string
    - `q`: float
    - `energy`: float

### unoccupied_surface_states.csv
- path: `/app/outputs/unoccupied_surface_states.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energies of unoccupied surface states (b1–b4).
- schema:
  - `type`: table
  - `required_columns`: `feature`, `q`, `energy`
  - `columns`:
    - `feature`: string
    - `q`: float
    - `energy`: float

Notes: The task omits the Cu(001) film calculations of the original paper and focuses solely on the Ca(001) five-layer film. All required input parameters (lattice constant, pseudopotential type, exchange-correlation functional) are publicly available. The solving agent must implement the complete DFT workflow; no pre-computed results are provided.

## How you are scored
Each scored workflow step produces an artifact that is independently evaluated by a hidden verifier. The verifier compares your submitted numbers (work function, peak shifts, and surface-state energies) against a private set of reference values with appropriate tolerances that account for implementation differences. Every artifact carries a weighted share of the total reward. Simply reporting a number without genuinely executing the computations will not pass, because the verifier checks multiple artifacts and internal consistency. The final reward is a single float between 0 and 1 that reflects the overall agreement of your reproduced results with the hidden references.