# Kinetic Monte Carlo Center Shift Simulation

## Problem background
Template-directed growth of organic molecules on prepatterned surfaces (e.g., Au squares on SiO₂) offers a route to high-resolution patterning for organic electronics. The technique relies on binding-energy differences to guide molecules to predefined areas, but a persistent problem is the **center shift**: the final organic aggregate is often offset from the center of the template, reducing pattern precision. This task reproduces a kinetic Monte Carlo (KMC) simulation study that investigates how the center deviation \(r\) (the lateral distance between the aggregate center and the template center) depends on inter-particle interactions (\(\varepsilon_{pp}\), \(\varepsilon_{ps}\)) and on the template’s geometrical height, with the aim of identifying the microscopic mechanisms that govern the shift.

## Model and Simulation Details (everything you need to implement)

### 1. Lattice and geometry
- The simulation uses a **3‑D cubic lattice** with lattice constant \(a = 1\).
- **Lateral dimensions**: \(100a \times 100a\) with **periodic boundary conditions** in the \(x\) and \(y\) directions.
- **Vertical dimension** (\(z\)): the box extends from \(z = 0\) to \(z = 5\) (6 lattice layers).  
  - \(z = 0, 1\) are the **SiO₂ substrate** (grey balls, fixed, never move).  
  - \(z = 2,3,4,5\) are the layers where **organic particles** can exist.  
  - The \(z\) (vertical) direction is **not periodic**; a hop that would place a particle at \(z < 2\) or \(z > 5\) is always rejected.

### 2. Template (Au squares)
- Gold squares are placed on top of the substrate, starting at \(z = 2\).  
- Each square has a width of \(14a\) and a default height of \(4a\) (occupying layers \(z = 2,3,4,5\) inside the square region).  
- The squares are repeated with a period of \(50a\) in both \(x\) and \(y\).  
- The lattice positions of the centre of each square are:  
  \((25a, 25a),\;(25a, 75a),\;(75a, 25a),\;(75a, 75a)\).  
  **Use the square centred at \((25a, 25a)\) as the reference centre** for computing the centre deviation \(r\) (see below).  
- Gold (pattern) particles are **fixed** and never move; they only provide interaction energy to organic particles.

### 3. Interaction energies
Three types of pair interactions exist:
- \(\varepsilon_{pp}\) : organic‑organic interaction.
- \(\varepsilon_{ps}\) : organic‑substrate interaction (substrate = grey particles at \(z = 0,1\)).
- \(\varepsilon_{pg}\) : organic‑pattern interaction (pattern = gold particles that form the squares).

Default values (in units of \(k_B T\)):
- \(\varepsilon_{ps} = 0.3\)
- \(\varepsilon_{pg} = 1.3\)
- \(\varepsilon_{pp}\) is varied in the tasks below.

The interaction between any two particles \(i\) and \(j\) of types \(t(i), t(j)\) depends on their distance \(r_{ij}\):

\[
E_{ij} = -\varepsilon_{t(i)t(j)} f(r_{ij})
\]

where the weight function \(f(r)\) is defined **exactly** as follows (cut‑off distance = \(\sqrt{3}a\)):

\[
f(r) = 
\begin{cases}
1.0 & \text{for } r \le \sqrt{2}a \quad (\text{nearest neighbours}), \\
0.5 & \text{for } \sqrt{2}a < r \le \sqrt{3}a \quad (\text{next‑nearest neighbours}), \\
0.0 & \text{otherwise}.
\end{cases}
\]

The total energy of an organic particle at a given site is the sum over all surrounding particles (organic, substrate, pattern) within the cut‑off:

\[
E_i = \sum_{j} -\varepsilon_{t(i)t(j)} f(r_{ij}).
\]

### 4. Diffusion (hopping) and Metropolis step
Only organic particles can move. In each **diffusion MC step**:
1. Randomly select one organic particle.
2. From its 6 nearest‑neighbour sites, randomly choose one that is **empty** and satisfies the \(z\) bounds above.
3. Compute the old‑site energy \(E_{i,\text{old}}\) and the new‑site energy \(E_{i,\text{new}}\) using the energy formula above.
4. Compute the diffusion barrier using the full‑diffusion bond‑counting model with \(\alpha = 0.5\):

\[
E_{\text{barrier}} = \alpha\,(E_{i,\text{new}} + E_{i,\text{old}}) - E_{i,\text{old}}.
\]

5. Accept the hop with probability

\[
P_{\text{accept}} = \min\!\big(1,\; \exp(-E_{\text{barrier}} / k_B T)\big).
\]

(Use \(k_B T = 1\) throughout the simulation; all energies are already expressed in units of \(k_B T\).)

### 5. Particle deposition
- Every **10 000 MC steps** one new organic particle is added to the system.
- **Deposition rule**: randomly choose an unoccupied lattice site anywhere in the box (\(x,y\) periodic bounds, \(z\) from 2 to 5), and place the new particle there. If no empty site exists, retry (in practice the lattice is large enough that this never happens).

### 6. Centre deviation \(r\)
At any moment, the centre of mass of the deposited organic particles is

\[
x_{\text{pattern}} = \frac{1}{N}\sum_{i} x_i,\qquad
y_{\text{pattern}} = \frac{1}{N}\sum_{i} y_i,
\]

where the sum runs over all organic particles. The **reference square centre** is \((x_{\text{square}}, y_{\text{square}}) = (25a, 25a)\). The centre deviation (in units of \(a\)) is

\[
r = \sqrt{(x_{\text{pattern}} - x_{\text{square}})^2 + (y_{\text{pattern}} - y_{\text{square}})^2}.
\]

### 7. Simulation parameters and required runs
Run the KMC simulation for the following parameter combinations, depositing up to **10 000 particles** each time, and record \(r\) at regular intervals (every 100 deposited particles, i.e., at 100, 200, …, 10 000).

#### Set 1: vary \(\varepsilon_{pp}\) (fix \(\varepsilon_{ps}=0.3\), \(\varepsilon_{pg}=1.3\), height = \(4a\))
\[
\varepsilon_{pp} \in \{0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3\}
\]

#### Set 2: vary \(\varepsilon_{ps}\) (fix \(\varepsilon_{pp}=1.6\), \(\varepsilon_{pg}=1.3\), height = \(4a\))
\[
\varepsilon_{ps} \in \{0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0\}
\]

#### Set 3: vary square height (fix \(\varepsilon_{pp}=2.3\), \(\varepsilon_{ps}=0.3\), \(\varepsilon_{pg}=1.3\))
\[
\text{height} \in \{0a, 2a, 4a\}
\]

### Output file
Write all results to a single CSV file `/app/outputs/center_deviation_data.csv` with the following columns, exactly as specified:

- `condition_label` : a string uniquely identifying the parameter combination.  
  **Mandatory format:** `epp_<value>_eps_<value>_height_<value>`  
  (e.g., `epp_0.9_eps_0.3_height_4`, `epp_1.6_eps_0.2_height_4`, `epp_2.3_eps_0.3_height_0`).  
  Use the numerical values exactly as listed; the height is always an integer (0, 2, 4).
- `particle_count` : integer, number of deposited particles (100, 200, …, 10 000).
- `r` : float, centre deviation in units of \(a\).

The CSV must contain data for **every** parameter combination listed above.

## Assets
- Python 3: https://www.python.org/
- NumPy: https://numpy.org/

## Workflow steps

### Step 1: Run kinetic Monte Carlo simulations and record center deviation
- **Role**: scored (load‑bearing)
- **Action**: Implement the KMC model exactly as described above (lattice, square pattern, interactions, deposition, hopping, centre computation). For each parameter set, run the simulation for 10 000 deposited particles (one particle deposited per 10 000 MC steps). Every 100 deposited particles record `particle_count` and `r`. Output all data to `/app/outputs/center_deviation_data.csv` with the three required columns and the mandatory `condition_label` format.
- **Output file**: `/app/outputs/center_deviation_data.csv`
- **Format**: csv
- **Contract**: CSV with header: `condition_label`, `particle_count`, `r`. `condition_label` must follow `epp_<num>_eps_<num>_height_<int>`. `particle_count` non‑negative integer. `r` float (centre deviation in units of \(a\)).
- **Scoring**: scored by hidden verifier

## Output files
Write under `/app/outputs`:
- `/app/outputs/center_deviation_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### center_deviation_data.csv
- **path**: `/app/outputs/center_deviation_data.csv`
- **format**: csv
- **purpose**: scored
- **target_policy**: structural_audit
- **description**: Centre deviation \(r\) as a function of deposited particle count for various parameter conditions (\(\varepsilon_{pp}\), \(\varepsilon_{ps}\), square height). The checker will assess whether the \(r\) evolution trends correspond to the expected regimes.
- **schema**:
  - `type`: table
  - `required_columns`: `condition_label`, `particle_count`, `r`
  - `units`:
    - `r`: lattice constant \(a\)

**Notes**: The CSV must include data for all conditions: \(\varepsilon_{pp}\) from 0.9 to 2.3 (with \(\varepsilon_{ps}=0.3\), \(\varepsilon_{pg}=1.3\), height=\(4a\)), \(\varepsilon_{ps}\) from 0.2 to 1.0 (with \(\varepsilon_{pp}=1.6\), \(\varepsilon_{pg}=1.3\), height=\(4a\)), and square heights \(0a, 2a, 4a\) (with \(\varepsilon_{pp}=2.3\), \(\varepsilon_{ps}=0.3\), \(\varepsilon_{pg}=1.3\)). The `condition_label` must use the format `epp_<value>_eps_<value>_height_<value>`.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "center_deviation_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_label",
          "particle_count",
          "r"
        ],
        "units": {
          "r": "lattice constant a"
        }
      },
      "description": "Centre deviation r as a function of deposited particle count for various parameter conditions (ε_pp, ε_ps, square height). The checker will assess whether the r evolution trends correspond to the expected regimes."
    }
  ],
  "notes": "The CSV must include data for all conditions: ε_pp from 0.9 to 2.3 (with ε_ps=0.3, ε_pg=1.3, height=4a), ε_ps from 0.2 to 1.0 (with ε_pp=1.6, ε_pg=1.3, height=4a), and square heights 0, 2a, 4a (with ε_pp=2.3, ε_ps=0.3, ε_pg=1.3). Each condition should be clearly distinguishable via the condition_label field."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/center_deviation_data.csv`. For each condition, the verifier examines the sequence of (`particle_count`, `r`) and determines whether the evolution pattern matches the expected regime according to a hidden reference. The final score combines the correctness of these trend classifications across all parameter conditions. Exact numerical agreement with any reference curve is not required, but the `r` vs. `particle_count` curve must be consistent with the physically expected behaviour for each set of interactions and geometry. The steps are weighted so that the simulation data contributes the full score; no other artifact is scored.