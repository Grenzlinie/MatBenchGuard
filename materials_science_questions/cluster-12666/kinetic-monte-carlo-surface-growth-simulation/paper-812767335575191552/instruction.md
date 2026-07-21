# Kinetic Monte Carlo Simulation of Au(001) Homoepitaxial Growth: Energetic vs. Conventional Deposition

## Problem background
Energetic atom deposition techniques like ion-beam assisted deposition and laser ablation are widely used to control thin-film morphology. In homoepitaxial growth, the interplay between the transient mobility induced by incident energetic atoms and the thermal diffusion of adatoms is not fully understood. This problem focuses on Au(001) homoepitaxy: using kinetic Monte Carlo simulations, one can investigate how energetic deposition influences the early-stage nucleation, island size distribution, and the evolution of surface roughness compared to conventional low-energy deposition. The central question is whether—and under which temperature conditions—the deposition energy significantly alters the film growth mode and the resulting surface morphology.

## Approach
We model film growth on a Au(001) fcc lattice (lattice constant a₀ = 4.08 Å) using kinetic Monte Carlo (kMC). Two deposition modes are compared: an energetic deposition model derived from molecular dynamics (MD) simulation results, and a conventional downward-funneling model.

**Energetic deposition** (incident atom energy 10 eV):  
Each incident atom impinges at a random surface site and can displace existing surface atoms. The push-out probability of a surface atom with in‑plane coordination number n_b at distance ρ from the impact point is

\[
P_{\text{push}} = 1 - P_{\!D}\,\frac{n_b\,\rho}{a_u},
\qquad
P_{\!D} = 0.2,
\qquad
a_u = 0.5\,a_0 .
\]

- For ρ < a_u the distance is clamped: use ρ = a_u.  
- An atom that is pushed out is removed from its original site (creating a vacancy) and becomes a new adatom.  
- All adatoms created by the impact are redistributed randomly onto vacant lattice sites within a circle of radius  
  \(R_{\text{D}} = 2.83\,a_u\) centered on the impact point.

**Conventional deposition**: incident atoms simply funnel downward to the nearest vacant site (downward funneling model).

**Adatom diffusion** is treated via Arrhenius hopping with an attempt frequency ν = 0.5 × 10¹² Hz. The hopping rate for a specific move is

\[
h = \nu \exp\!\left(-\frac{E_{\text{B}}}{k_{\text{B}}T}\right),
\]

where the diffusion barrier E_B is obtained from the local atomic environment. Barriers are computed with the embedded-atom method (EAM) potential for gold (Foiles et al., publicly available) using a three‑dimensional Newton‑Raphson saddle‑point search as described in the Breeman *et al.* model.  
For each possible hopping event the algorithm locates the saddle point of the EAM energy along the reaction path and determines E_B as the energy difference between the saddle point and the initial state. Typical events include:

- in‑plane hop of an adatom to a nearest‑neighbor vacant site,
- jump of an adatom off a straight step edge onto the lower terrace,
- jump of an adatom off a kink site on a step edge.

(If the computed E_B is negative, set it to zero.)

All simulations are performed on a 160 × 160 × 4 fcc(001) lattice (4 atomic layers deep) with periodic boundary conditions in the surface plane.

## Reproduction target
Your task is to implement a kMC simulation of Au(001) homoepitaxial growth as described, using both the energetic deposition rule (with its MD‑derived push‑out probability, clamping, and redistribution radius) and the conventional downward‑funneling rule. Run simulations at the four substrate temperatures (100, 300, 400, 450 K) at a constant deposition rate of 0.05 monolayers per second (ML s⁻¹). From the simulated surfaces, compute the island size distribution and the monomer fraction after 0.2 ML of deposition for each temperature and deposition type. Separately, compute the evolution of the kinematic Bragg intensity (anti‑Bragg condition) and the RMS surface roughness up to a coverage of 5 ML for all conditions. The comparison between energetic and conventional deposition at each temperature quantifies the influence of the deposition energy on nucleation, island growth, and film smoothness.

## Physical quantities to be computed from the surface configurations

**Island statistics** (after 0.2 ML):  
Identify connected clusters of atoms (in‑plane nearest neighbours). For each cluster size s, record the fraction of the total deposited coverage that belongs to clusters of size s (island coverage). The monomer fraction is the proportion of deposited atoms (out of 0.2 ML) that are in size‑1 islands. A “stable” island is any cluster of size ≥ 2.

**RMS surface roughness**:
\[
w = \sqrt{\frac{1}{N}\sum_{i=1}^{N} (z_i - \bar{z})^2},
\]
where \(z_i\) is the z‑coordinate (layer index) of atom i, \(\bar{z}\) is the mean height, and N is the total number of atoms (substrate atoms included). Express w in units of the lattice constant a₀.

**Kinematic Bragg intensity (anti‑Bragg condition)**:
\[
I_{\text{Bragg}} = \frac{1}{N_{\text{ML}}} \left|\sum_{j} \exp(i\,\mathbf{Q}\cdot\mathbf{r}_j) \right|^2,
\qquad
\mathbf{Q} = \left(0,\,0,\,\frac{2\pi}{a_0}\right).
\]
The sum runs over all atoms (substrate + deposited). The prefactor \(N_{\text{ML}}\) is the number of atoms in one monolayer (160 × 160).  
For a perfect flat layer the intensity is maximal; alternating layer coverages cause oscillations.

## Assets
- Au EAM potential (Foiles et al.): https://www.ctcms.nist.gov/potentials/Download/Au/Au_u3.eam

## Workflow steps

### Step 1: Kinetic Monte Carlo simulation of Au(001) film growth
- Role: process
- Action: Implement a kMC simulator on a 160 × 160 × 4 fcc(001) lattice with periodic boundaries. For energetic deposition, use the MD‑derived push‑out probability \(P_{\text{push}} = 1 - P_{\!D}\, n_b\, \rho / a_u\) with \(P_{\!D}=0.2\), a_u = 0.5 a₀, clamping ρ → a_u when ρ < a_u, and redistribution radius R_D = 2.83 a_u. For conventional deposition, use downward funneling. Hopping rate \(h = \nu \exp(-E_B/k_{\text{B}}T)\) with ν = 0.5 × 10¹² Hz. Compute barriers E_B using the Breeman *et al.* model together with the Au EAM potential and a three‑dimensional Newton‑Raphson saddle‑point search. Deposit at 0.05 ML s⁻¹ at substrate temperatures 100, 300, 400, and 450 K. Save surface configurations at 0.2 ML and at regular intervals up to 5 ML for later analysis.

### Step 2: Compute island size distribution and monomer fraction after 0.2 ML deposition
- Role: scored (load-bearing)
- Action: From the saved surface configurations at 0.2 ML, extract the island size distribution (coverage per island size), compute the monomer fraction and the stable‑island count for each temperature and deposition type (energetic and conventional). Write the results to step_01_island_stats.json.
- Output file: `/app/outputs/step_01_island_stats.json`
- Format: json
- Contract: JSON object with key 'temperatures' containing an array of objects. Each object: { 'temperature': float (K), 'deposition_type': 'energetic'|'conventional', 'island_size_distribution': [ { 'size': int, 'coverage': float (ML) } ], 'monomer_fraction': float, 'stable_island_count': int }
- Scoring: scored by hidden verifier

### Step 3: Compute Bragg intensity and surface roughness up to 5 ML coverage
- Role: scored
- Action: From the saved surface configurations at multiple coverages (up to 5 ML), compute the kinematic Bragg intensity (anti‑Bragg condition, Q = (0,0,2π/a₀)) and RMS surface roughness as functions of coverage for each temperature and deposition type. Write the results to step_02_bragg_roughness.json.
- Output file: `/app/outputs/step_02_bragg_roughness.json`
- Format: json
- Contract: JSON object with key 'temperatures' containing an array of objects. Each object: { 'temperature': float (K), 'deposition_type': 'energetic'|'conventional', 'coverage': [float (ML)], 'bragg_intensity': [float], 'roughness': [float] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_island_stats.json`
- `/app/outputs/step_02_bragg_roughness.json`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_island_stats.json
- path: `/app/outputs/step_01_island_stats.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Island statistics after 0.2 ML deposition for energetic and conventional deposition at T = 100, 300, 400, 450 K. The checker recomputes the monomer fraction and the relative decrease at 100 K.
- schema:
  - `type`: object
  - `required`:
    - `temperatures`: array
  - `items`:
    - `temperature`: float (K)
    - `deposition_type`: string ('energetic' or 'conventional')
    - `island_size_distribution`: array of objects with 'size' (int) and 'coverage' (float, ML)
    - `monomer_fraction`: float
    - `stable_island_count`: int

### step_02_bragg_roughness.json
- path: `/app/outputs/step_02_bragg_roughness.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Bragg intensity and roughness evolution up to 5 ML for all conditions. The checker recomputes the Bragg intensity at 5 ML and the relative increase at low temperature.
- schema:
  - `type`: object
  - `required`:
    - `temperatures`: array
  - `items`:
    - `temperature`: float (K)
    - `deposition_type`: string ('energetic' or 'conventional')
    - `coverage`: array of floats (ML)
    - `bragg_intensity`: array of floats (arbitrary units)
    - `roughness`: array of floats (a₀ units)

## Self‑check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.  
This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_island_stats.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "temperatures": "array"
        },
        "items": {
          "temperature": "float (K)",
          "deposition_type": "string ('energetic' or 'conventional')",
          "island_size_distribution": "array of objects with 'size' (int) and 'coverage' (float, ML)",
          "monomer_fraction": "float",
          "stable_island_count": "int"
        }
      },
      "description": "Island statistics after 0.2 ML deposition for energetic and conventional deposition at T=100,300,400,450 K. The checker recomputes the monomer fraction and the relative decrease at 100 K."
    },
    {
      "file": "step_02_bragg_roughness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "temperatures": "array"
        },
        "items": {
          "temperature": "float (K)",
          "deposition_type": "string ('energetic' or 'conventional')",
          "coverage": "array of floats (ML)",
          "bragg_intensity": "array of floats (arbitrary units)",
          "roughness": "array of floats (lattice constant units)"
        }
      },
      "description": "Bragg intensity and roughness evolution up to 5 ML for all conditions. The checker recomputes the Bragg intensity at 5 ML and the relative increase at low temperature."
    }
  ],
  "notes": "The checker will recompute the monomer fraction from the island size distribution and the Bragg intensity at 5 ML from the submitted data, then compare the relative differences (energetic vs. conventional) against the paper-reported values with a tolerance. Additional structural checks verify monotonic trends and the presence of oscillations at high temperature."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. The verifier reads the two output JSON files and independently recomputes the monomer fraction from your island size distribution, as well as the Bragg intensity at 5 ML coverage from your evolution data. For each condition, it compares the results against hidden reference thresholds and structural expectations (e.g., temperature‑dependent trends, presence of Bragg oscillations at elevated temperatures). The final score is a weighted sum over these checks, with the two scored artifacts carrying the most weight. Reporting plausible numbers is not enough; the verifier will cross‑check internal consistency and the quantitative relationships between energetic and conventional deposition derived from your raw simulation output.