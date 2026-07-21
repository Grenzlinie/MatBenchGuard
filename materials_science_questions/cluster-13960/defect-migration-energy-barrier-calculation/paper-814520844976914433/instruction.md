# Mg migration barrier in cubic Ti₂S₄ spinel

## Problem background
The sluggish mobility of divalent Mg²⁺ ions in solid hosts has been a major bottleneck in the development of rechargeable Mg batteries. Soft anion lattices, such as sulfides, are thought to mitigate this issue by weakening the electrostatic interaction between the mobile cation and the framework. The cubic thiospinel Ti₂S₄ is one such candidate. Its structural simplicity and theoretical studies have highlighted the role of Mg diffusion kinetics in determining cathode performance. A key quantity that governs the Mg diffusion rate is the migration energy barrier for a single Mg²⁺ ion hopping between adjacent sites. First-principles nudged elastic band (NEB) calculations provide a reliable route to compute this barrier, allowing direct comparison with experimental activation energies extracted from electrochemical measurements. This task focuses on computing the Mg migration barrier in cubic Ti₂S₄ for two limiting Mg concentrations — the dilute limit and the concentrated limit — via standard DFT‑NEB methods.

## Approach
The computational approach relies on density functional theory (DFT) within the PBE generalized gradient approximation, coupled with the climbing-image nudged elastic band (CI‑NEB) method to locate the minimum-energy path for Mg diffusion. The crystal structure of cubic Ti₂S₄ adopts the spinel structure (space group Fd‑3m). The dilute limit uses a cubic lattice constant **a = 9.78 Å** (the experimental value for Ti₂S₄ reported in the paper). The concentrated (fully loaded) limit uses a lattice constant **a = 10.05 Å** (the value for the Mg‑inserted phase). For the dilute limit, one Mg atom is placed in an octahedral site of the 8‑formula‑unit supercell (the conventional cubic cell contains exactly 8 formula units); for the concentrated limit, the supercell is filled with 7 Mg atoms (approaching full occupancy). The diffusion mechanism considered is the tri‑vacancy pathway, where a Mg ion hops from an octahedral site through a face‑sharing tetrahedral intermediate to a neighboring vacant octahedral site. The agent must first construct the supercells with the specified lattice constants, relax the endpoint configurations, interpolate a chain of intermediate images, and then perform CI‑NEB to converge the saddle point. The migration barrier is the energy difference between the saddle point and the initial minimum, expressed in meV. Any standard open‑source DFT package that supports the PBE functional and NEB (Quantum ESPRESSO, GPAW, etc.) may be used; the computed barriers for the two concentration limits constitute the primary output.

## Reproduction target
The task objective is to produce a JSON file, `step_01_barrier.json`, containing two fields: `"dilute_barrier_meV"` and `"concentrated_barrier_meV"`. Each is a floating-point number giving the computed Mg migration barrier in meV for the corresponding Mg concentration limit. The barriers must be obtained from proper CI‑NEB calculations on the specified supercells, and the reported values must reflect the energy at the saddle point relative to the initial energy minimum. No additional statistical analysis or comparison with experimental data is required; the two barrier numbers are the sole scored outputs.

## Assets

- **Cubic Ti₂S₄ crystal structure**  
  The spinel structure can be built using any atomic simulation environment (e.g., ASE) with space group Fd‑3m (227), origin choice 2 (origin at -43m). The conventional cubic cell contains 8 formula units (Ti₁₆S₃₂). The atoms occupy the following Wyckoff positions:
  - **Ti**: 16d (octahedral), symmetry-equivalent positions (1/2, 1/2, 1/2) etc. (8 formula units give 16 Ti atoms).
  - **S**: 32e, coordinates (x, x, x) with **x = 0.241** (typical for thiospinels; consistent with earlier refinements of Ti₂S₄).
  - **Interstitial sites for Mg**:
    - **8a** (tetrahedral): (1/8, 1/8, 1/8) and symmetry equivalents.
    - **16c** (octahedral): (0, 0, 0) and symmetry equivalents.
  
  The lattice constant must be set to **9.78 Å** for the dilute limit and to **10.05 Å** for the concentrated limit. Both cases use the conventional cubic cell (8 formula units), which serves directly as the required 8‑formula‑unit supercell. No external structure files are needed; the agent should generate the structures from the space group, Wyckoff positions, and lattice parameters above.

- **Open‑source DFT package with NEB support**  
  Examples: Quantum ESPRESSO (pw.x + neb.x) or GPAW (with ASE‑NEB). Use the PBE functional and standard scalar‑relativistic pseudopotentials.

## Workflow steps

### Step 1: Compute Mg migration barrier
- **Role**: scored (load‑bearing)
- **Action**: Perform first‑principles NEB calculations to obtain the minimum‑energy migration barrier for Mg²⁺ diffusion in cubic Ti₂S₄ via the tri‑vacancy mechanism.  
  - **Dilute limit**: Build the 8‑formula‑unit supercell (a = 9.78 Å) with Ti at 16d and S at 32e (x=0.241). Place **one Mg atom** at a **16c** octahedral site (e.g., (0,0,0)), leaving the rest of the interstitial sites empty. Relax the endpoint configurations (the initial and final images correspond to the Mg atom occupying two different, neighbouring 16c sites connected by a face‑sharing tetrahedral 8a site).  
  - **Concentrated limit**: Build the supercell (a = 10.05 Å) with the same Ti and S positions. Fill **7 Mg atoms** onto the available interstitial sites. According to experimental refinement of Mg₀.₈Ti₂S₄, about two‑thirds of the Mg occupies octahedral 16c and one‑third occupies tetrahedral 8a. Therefore, place **5 Mg atoms** on **16c** sites and **2 Mg atoms** on **8a** sites. Choose specific Wyckoff positions such that Mg–Mg distances are not shorter than ~2.5 Å (e.g., using a combinatoric assignment; a simple choice is 16c at (0,0,0), (1/2,1/2,0), (1/2,0,1/2), (0,1/2,1/2), (1/4,1/4,1/4) — ensure they are symmetry valid — and 8a at (1/8,1/8,1/8) and (3/8,3/8,3/8)). Relax the endpoint cells (with Mg fixed at their respective sites), then set up a diffusion path: pick **one mobile Mg** occupying a 16c site, and make the neighbouring 16c site empty (the remaining Mg are static spectators). The path connects the two 16c sites through the intervening 8a tetrahedral site. Run climbing‑image NEB keeping the lattice parameters fixed.  
- **Output file**: `/app/outputs/step_01_barrier.json`
- **Format**: json
- **Contract**: `{"dilute_barrier_meV": <float>, "concentrated_barrier_meV": <float>}`
- **Scoring**: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_barrier.json
- path: `/app/outputs/step_01_barrier.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Migration energy barriers for Mg diffusion in cubic Ti₂S₄, computed for the dilute (1 Mg per 8‑formula‑unit supercell, a=9.78 Å) and concentrated (7 Mg per supercell, a=10.05 Å) limits.
- schema:
  - `type`: object
  - `required`: `dilute_barrier_meV`, `concentrated_barrier_meV`
  - `properties`:
    - `dilute_barrier_meV`:
      - `type`: number
      - `unit`: meV
    - `concentrated_barrier_meV`:
      - `type`: number
      - `unit`: meV

Notes: The checker compares the agent's reported barriers to a hidden reference derived from the paper's first‑principles NEB results with a tolerance that accounts for code‑to‑code variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "dilute_barrier_meV",
          "concentrated_barrier_meV"
        ],
        "properties": {
          "dilute_barrier_meV": {
            "type": "number",
            "unit": "meV"
          },
          "concentrated_barrier_meV": {
            "type": "number",
            "unit": "meV"
          }
        }
      },
      "description": "Migration energy barriers for Mg diffusion in cubic Ti2S4, computed for the dilute (1 Mg per 8-formula-unit supercell, a=9.78 Å) and concentrated (7 Mg per supercell, a=10.05 Å) limits."
    }
  ],
  "notes": "The checker compares the agent's reported barriers to a hidden reference derived from the paper's first-principles NEB results with a tolerance that accounts for code-to-code variation."
}
```

## How you are scored
Your submission will be checked by a hidden verifier that reads the file `step_01_barrier.json` and compares your reported barriers to the expected values from a trusted reference computation. The verifier applies a predefined tolerance that accounts for the typical spread introduced by using different DFT codes, pseudopotentials, and numerical settings, while still requiring physically meaningful agreement. Both the dilute and concentrated barriers must fall within tolerance to receive full credit. The final reward is a single number between 0 and 1, reflecting how accurately you reproduced the migration barriers. No further instructions will be given regarding the reference values or the tolerance; simply performing the NEB calculations with standard care should yield a result that passes the check.