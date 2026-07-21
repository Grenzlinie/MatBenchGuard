# Pressure-Induced Friction Collapse of a Xe Monolayer on Cu(111)

## Problem background
Rare gas monolayers adsorbing on metal surfaces can display *anticorrugation*, where top sites are the energy minima rather than the expected hollow sites. When a normal load is applied, the potential energy surface (PES) sensed by the adatoms changes shape, potentially altering the forces that determine static and kinetic friction. The question addressed here is: for a commensurate √3 Xe monolayer on Cu(111), how do static and kinetic friction vary as a function of applied normal pressure? The answer lies in computing the analytical restoring force from the PES and in classical molecular dynamics simulations that probe the pressure-induced evolution of the PES from an anticorrugated to a flat to a corrugated regime.

## Approach
The core idea is to use an analytical three-dimensional PES, parameterised from DFT-based ab‑initio calculations, to describe the Xe–Cu(111) interaction, and to employ classical MD simulations to measure friction. First, the PES is implemented and its analytical derivative is used to compute the restoring force acting on a single adatom at different adatom–surface distances, serving as a proxy for static friction. Then, two types of MD simulations are performed for a 2048‑atom Xe monolayer at 77 K: (i) static friction is obtained by adiabatically ramping a lateral force until the monolayer centre of mass depins, at various fixed normal loads; (ii) kinetic friction is obtained by sliding a rigid top surface at constant speed and averaging the lateral force on the monolayer, again at several normal loads. Comparing the resulting friction‑vs‑pressure curves reveals whether and how pressure controls friction in this system.

## Reproduction target
Produce three scored artifacts under `/app/outputs`:

1. **`analytical_restoring_force.json`** – the equilibrium adatom–surface distance, the magnitude of the analytical restoring force at that equilibrium, the critical distance where anticorrugation vanishes (and its corresponding pressure), and a list of (z, pressure, restoring force) points for a range of z.

2. **`static_friction_vs_pressure.csv`** – static friction force (in meV/Å) as a function of normal pressure (GPa) obtained from MD depinning simulations; at least 5 pressure points covering from near zero to above the pressure where the PES becomes flat.

3. **`kinetic_friction_vs_pressure.csv`** – kinetic friction force (meV/Å) versus normal pressure (GPa) from sliding MD simulations, covering the same pressure range.

The outputs must follow the exact schemas described in the workflow steps.

## System parameters and PES definition

### Cu(111) surface geometry
- Surface lattice constant: a0 = 2.56 Å (nearest-neighbour distance of Cu atoms on the (111) plane).
- The Xe monolayer forms a commensurate (√3×√3)R30° structure. Its lattice constant is a = √3 a0 ≈ 4.43 Å.
- Area per Xe atom: A_atom = (√3/2) a² = (3√3/2) a0² ≈ 2.598 a0² ≈ 17.0 Å².

### Coordinate system
- Cartesian coordinates (x, y) lie in the surface plane. The x‑axis is along the [1‾1‾0] direction; the y‑axis is perpendicular to x in the plane.
- The origin (0,0) is placed at a top adsorption site (Xe atom directly above a Cu atom).

### Analytical PES for Xe/Cu(111)

The potential energy experienced by a Xe adatom as a function of its lateral position (x,y) and distance z from the outermost Cu layer is

V(x,y,z) = A₀(x,y) exp[−z / A₁(x,y)] − A₂(x,y) / z³ .   (1)

The coefficients A₀, A₁, A₂ are periodic functions with the symmetry of the Cu(111) surface. They are expressed via the function

u(x,y) = 1 − ⅓ [ cos(4π x/(√3 a₀)) + cos(4π y/(3 a₀)) + cos(4π (x/(√3 a₀) − y/(3 a₀)) ) ]

as

Aⱼ(x,y) = Aⱼ_top + ΔAⱼ · u(x,y),   j = 0,1,2,

where
- Aⱼ_top are the values at the top site (x=0, y=0, u=0),
- Aⱼ_hollow are the values at the hollow site located at (x = a₀/(2√3), y = a₀/2) (where u=1),
- ΔAⱼ = Aⱼ_hollow − Aⱼ_top.

Parameters (energies in meV, lengths in Å):

|             |   A₀     |   A₁    |    A₂     |
|-------------|----------|---------|-----------|
| Top site    | 1076.0   | 0.416   | 2862.0    |
| Hollow site | 1249.0   | 0.388   | 2960.0    |
| Δ           |  173.0   | –0.028  |   98.0    |

These parameters reproduce the physisorption wells shown in the original ab‑initio study.

### Connection between z and pressure

When the monolayer is squeezed, each adatom experiences a vertical force F_z. A natural estimate for the normal pressure at a given adatom–surface distance z is obtained from the derivative of the potential:

P(z) = −(1/A_atom) · (∂V/∂z)

evaluated at a representative lateral position, e.g., the top site (0,0). This allows the substitution of a normal load by an equivalent adatom–surface distance. At the equilibrium distance (where ∂V/∂z vanishes) the pressure is zero; as z decreases, the pressure becomes positive and increases. Use this relation to convert between z and pressure in all outputs that require a pressure value.

**Unit conversion note:** The PES is given in meV and lengths in Å. To obtain pressure in GPa, evaluate the force F_z in meV/Å, divide by A_atom in Å² to get a value in meV/Å³, and then convert to Pa using the exact equivalence:
1 meV/Å³ = 1.60218×10⁸ Pa.
Then scale to GPa (1 GPa = 10⁹ Pa). For example, a pressure of 5 GPa corresponds to approximately 31.2 meV/Å³.

The critical adatom–surface distance z_c where the PES flattens corresponds to the separation at which the adsorption wells of the top and hollow sites cross. Therefore you can determine z_c by finding the z for which V(0,0,z) = V(x_hollow, y_hollow, z). The corresponding critical pressure P_c is obtained by evaluating the pressure relation at z_c.

### Other parameters
- Lennard‑Jones Xe–Xe parameters: σ = 3.95 Å, ε = 20 meV.
- Temperature: T = 77 K.
- Sliding speed for kinetic friction: v = 10 nm/ns.

## Workflow steps

### Step 1: Implement the Xe/Cu(111) analytical PES
- Role: process
- Action: Implement the function V(x,y,z) defined by Eq. (1) together with the coefficient expressions and the numerical parameters given above. The implementation must provide both the potential and its x‑derivative (∂V/∂x) at arbitrary (x,y,z) positions. It will be used for the analytical restoring force calculation and as the substrate potential in subsequent MD simulations.
- Save the implemented PES as a callable module or script (any internal evidence log is optional).

### Step 2: Compute analytical restoring force vs. pressure
- Role: scored
- Action: Using the implemented PES:
  - Determine the equilibrium adatom–surface distance z_eq by minimising V at the top site (x=0,y=0).
  - Calculate the magnitude of −∂V/∂x at (x = a/4, y = 0, z_eq), where a = √3 a₀ ≈ 4.43 Å. This is the analytical restoring force at equilibrium.
  - Determine the critical distance z_c by solving V(0,0,z) = V(x_hollow, y_hollow, z) with the hollow coordinates given above.
  - For each z, compute the vertical force F_z = −∂V/∂z at the top site (0,0) and convert to pressure using P = F_z / A_atom, with the unit conversion described above.
  - Evaluate the restoring force −∂V/∂x at (x = a/4, y = 0, z) for a range of z values from z_eq down to slightly below z_c. Collect at least 10 points.
  - Produce a JSON file containing:
    - `z_eq_Ang` (in Å)
    - `restoring_force_at_equilibrium_meV_per_Ang` (magnitude, meV/Å)
    - `critical_z_Ang` (Å)
    - `critical_pressure_GPa` (GPa)
    - `z_vs_F` : list of objects `{z_Ang, pressure_GPa, restoring_force_meV_per_Ang}` for the chosen z values.
- Output file: `/app/outputs/analytical_restoring_force.json`
- Format: json
- Contract: A JSON object with the exact keys listed. All numeric values positive; force is magnitude.
- Scoring: scored by hidden verifier

### Step 3: MD simulation of static friction vs. pressure
- Role: scored (load-bearing)
- Action: Set up a 2048‑atom Xe monolayer in the √3 commensurate structure on the Cu(111) PES. Use Lennard‑Jones interactions (σ=3.95 Å, ε=20 meV) and a thermostat at T=77 K. After annealing at zero lateral force, apply an adiabatically increasing lateral force F_x. For each normal load F_z (varying the ML–surface spacing according to the pressure–z relation), record the F_x value at depinning (centre‑of‑mass velocity becomes nonzero). Repeat for at least 5 normal loads spanning pressures from near zero to at least 6 GPa. Output a CSV with the static friction vs. pressure.
- Output file: `/app/outputs/static_friction_vs_pressure.csv`
- Format: csv
- Contract: CSV with header: `pressure_GPa,static_friction_meV_per_Ang`. Each row is one simulated normal load. Pressure and friction are positive floats. Expected at least 5 data points.
- Scoring: scored by hidden verifier

### Step 4: MD simulation of kinetic friction vs. pressure
- Role: scored (load-bearing)
- Action: Simulate a Xe monolayer between two rigid surfaces, each described by the same Xe/Cu(111) PES, with the top surface moving at v=10 nm/ns in the x‑direction and the bottom fixed. The monolayer occupies the gap; the vertical spacing is varied to impose different normal pressures. Run for 5 ns at T=77 K. Time-average the lateral force F_x exerted on the ML by the sliding surface. For each spacing, record the averaged F_x as the kinetic friction. Output a CSV with kinetic friction vs. pressure.
- Output file: `/app/outputs/kinetic_friction_vs_pressure.csv`
- Format: csv
- Contract: CSV with header: `pressure_GPa,kinetic_friction_meV_per_Ang`. Each row is one simulation condition. Pressure and friction are positive floats. Expected at least 5 data points.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/analytical_restoring_force.json`
- `/app/outputs/static_friction_vs_pressure.csv`
- `/app/outputs/kinetic_friction_vs_pressure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### analytical_restoring_force.json
- path: `/app/outputs/analytical_restoring_force.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the equilibrium adatom–surface distance, the analytical restoring force at equilibrium (proxy for static friction), the critical distance and pressure where anticorrugation vanishes, and a list of force vs. distance/pressure data. The checker compares the equilibrium force and critical values to hidden paper‑derived references, and audits the trend for monotonic decrease.
- schema:
  - `type`: object
  - `required`:
    - `z_eq_Ang`: float (Å)
    - `restoring_force_at_equilibrium_meV_per_Ang`: float (meV/Å)
    - `critical_z_Ang`: float (Å)
    - `critical_pressure_GPa`: float (GPa)
    - `z_vs_F`: array of objects
  - `items`:
    - `z_Ang`: float (Å)
    - `pressure_GPa`: float (GPa)
    - `restoring_force_meV_per_Ang`: float (meV/Å)

### static_friction_vs_pressure.csv
- path: `/app/outputs/static_friction_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Static friction force measured from MD depinning, as a function of applied normal pressure. The checker verifies monotonic decreasing trend and near‑vanishing at high pressure (≤ 20% of the maximum value in the submitted series).
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `static_friction_meV_per_Ang`
  - `units`:
    - `pressure_GPa`: GPa
    - `static_friction_meV_per_Ang`: meV/Å

### kinetic_friction_vs_pressure.csv
- path: `/app/outputs/kinetic_friction_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Kinetic friction force from MD sliding simulations, as a function of applied normal pressure. Checked for monotonic decreasing trend and pressure‑induced reduction analogous to static friction.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `kinetic_friction_meV_per_Ang`
  - `units`:
    - `pressure_GPa`: GPa
    - `kinetic_friction_meV_per_Ang`: meV/Å