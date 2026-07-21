# Molecular Dynamics Simulation of Uniaxial Compression of Glassy Polymethylene

## Problem background
Polymethylene (PM) is a model polymer glass. Understanding the atomic-scale mechanisms of its plastic deformation is key to predicting mechanical properties. Molecular dynamics simulations can reveal whether deformation proceeds via nonaffine chain fragment gliding or conformational unfolding, and quantify the characteristic length scale of these rearrangements.

## Approach
The workflow constructs an amorphous PM sample, equilibrates it at low temperature, and then performs an isothermal uniaxial compression MD simulation. The interatomic interactions are described by a united-atom force field:

- **Bond stretching**: harmonic potential \(U(L)=K_L(L-L_0)^2\), with \(L_0 = 1.53 \, \text{Å}\), \(K_L = 1047.5 \, \text{kJ mol}^{-1} \text{Å}^{-2}\).
- **Angle bending**: harmonic potential \(U(\theta)=K_\theta(\theta-\theta_0)^2\), with \(\theta_0 = 113.0^\circ\), \(K_\theta = 167.6 \, \text{kJ mol}^{-1} \text{rad}^{-2}\).
- **Torsion**: \(U(\varphi) = K_1\left[1 + \cos(3\varphi)\right] + K_2\left[1 + \cos(\varphi)\right]\), with \(K_1 = 6.704 \, \text{kJ mol}^{-1}\), \(K_2 = 1.634 \, \text{kJ mol}^{-1}\).
- **Non-bonded (Lennard-Jones)**: \(U(r) = \varepsilon\left[\left(\frac{R_{\min}}{r}\right)^{12} - 2\left(\frac{R_{\min}}{r}\right)^{6}\right]\), with \(\varepsilon = 0.503 \, \text{kJ mol}^{-1}\), \(R_{\min} = 4.2654 \, \text{Å}\).

From the simulation trajectory, the axial engineering stress and mass density are computed as functions of strain. To analyse cooperative rearrangements, the nonaffine displacement \(D_{\min}\) is calculated for each CH₂ group using the Falk–Langer method on pairs of snapshots separated by a small strain increment. The correlation function of \(D_{\min}\) along each chain is then computed and an exponential decay is fitted to obtain a characteristic correlation length (in number of CH₂ units).

**Nonaffine displacement (\(D_{\min}\)) algorithm**:
Given two atomic configurations of the same set of atoms at times \(t\) and \(t+\Delta t\), for each atom \(i\):
1. Identify its neighbour set \(\mathcal{N}_i\): all atoms \(j\) (including \(i\) itself) such that the initial distance \(r_{ij}^0 = |\mathbf{r}_j(t) - \mathbf{r}_i(t)| < R_c\), where \(R_c = 6\, \text{Å}\).
2. Compute the displacement vector of each neighbour \(j\) relative to atom \(i\): \(\mathbf{d}_{ji} = [\mathbf{r}_j(t+\Delta t) - \mathbf{r}_i(t+\Delta t)] - [\mathbf{r}_j(t) - \mathbf{r}_i(t)]\).
3. Find the \(3\times 3\) affine deformation tensor \(\mathbf{J}_i\) that minimises
   \[
   D_{\min}^2(i) = \frac{1}{N_i} \sum_{j \in \mathcal{N}_i} |\mathbf{d}_{ji} - \mathbf{J}_i \cdot \mathbf{r}_{ji}^0|^2,
   \]
   where \(\mathbf{r}_{ji}^0 = \mathbf{r}_j(t) - \mathbf{r}_i(t)\) and \(N_i\) is the number of neighbours in \(\mathcal{N}_i\).
   The minimisation yields \(\mathbf{J}_i\) and the corresponding residual \(D_{\min}^2(i)\).
4. The nonaffine displacement of atom \(i\) is taken as \(D_{\min}(i) = \sqrt{D_{\min}^2(i)}\).

To compute the spatial correlation of these displacements along a chain, evaluate
\[
C(n) = \langle D_{\min}(i) D_{\min}(i+n) \rangle - \langle D_{\min} \rangle^2,
\]
where the average is taken over all atoms \(i\) and over the two snapshots used. Fit the decay of \(C(n)\) with an exponential function \(\propto \exp(-n/N_c)\) to extract the correlation length \(N_c\) (in monomer units).

## Reproduction target
Run the molecular dynamics simulation of glassy polymethylene under uniaxial compression at \(T = 50\) K and strain rate \(\dot\varepsilon = 2\times 10^8 \, \text{s}^{-1}\) to \(\varepsilon = -30\%\). Compute the axial stress and density as functions of strain and write `stress_strain.csv`. From the trajectory near \(\varepsilon = -28\%\), compute the nonaffine displacement correlation length along the chain and save it as `correlation_length.txt`. Submit these two files together with the intermediate simulation data files.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Prepare amorphous polymethylene sample
- Role: process
- Action: Build an amorphous cell with 64 united-atom CH₂ chains of length 100 using periodic boundary conditions and the force field specified above. Equilibrate via NPT MD at 50 K to a target density of approximately \(0.996 \, \text{g/cm}^3\) by adjusting the isotropic pressure. Use a collision thermostat (\(\lambda = 5.5 \, \text{ps}^{-1}\), \(m_0 = 1\) amu) and a Berendsen barostat. Save the equilibrated configuration.
- Evidence: `/app/outputs/sample_config.lammpsdata`

### Step 2: Uniaxial compression MD simulation
- Role: process
- Action: Perform isothermal uniaxial compression on the prepared sample at \(T = 50 \, \text{K}\), constant engineering strain rate \(\dot\varepsilon = -2\times 10^{-4} \, \text{ps}^{-1}\) (\(2\times 10^8 \, \text{s}^{-1}\)) to \(\varepsilon = -30\%\). Maintain constant transverse pressure equal to the pressure determined during equilibration using the Berendsen barostat. Keep the temperature constant with the same collision thermostat. After reaching the final strain, fix the cell dimensions and relax for \(1 \, \text{ns}\). Save snapshot coordinates and stress tensor every \(10 \, \text{ps}\) (corresponding to \(\Delta\varepsilon = 0.2\%\) strain increment).
- Evidence: `/app/outputs/compression_traj.lammpstrj`

### Step 3: Compute stress-strain and density curves
- Role: scored
- Action: From the compression trajectory, extract axial engineering stress \(\sigma\) (MPa) and mass density \(\rho\) (g/cm³) at each saved strain step. Output a CSV with columns: `strain` (negative engineering strain, %), `stress` (MPa), `density` (g/cm³).
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: `strain` (%, negative), `stress` (MPa), `density` (g/cm³) with header row
- Scoring: scored by hidden verifier

### Step 4: Compute nonaffine displacement correlation length
- Role: scored (load-bearing)
- Action: For snapshot pairs separated by \(\Delta\varepsilon \approx 0.2\%\) (10 ps) near \(\varepsilon \approx -28\%\), compute the nonaffine displacement \(D_{\min}\) for each CH₂ group using the Falk–Langer method described above. Calculate the correlation function of \(D_{\min}\) along each chain and fit an exponential decay to obtain the correlation length \(N_c\) (in CH₂ groups). Output the single fitted value.
- Output file: `/app/outputs/correlation_length.txt`
- Format: txt
- Contract: one decimal number
- Scoring: scored by hidden verifier

## Output files
Write all final artifacts under `/app/outputs`:
- `/app/outputs/sample_config.lammpsdata`   (intermediate, used to produce scored outputs)
- `/app/outputs/compression_traj.lammpstrj`  (intermediate, used to produce scored outputs)
- `/app/outputs/stress_strain.csv`           (scored)
- `/app/outputs/correlation_length.txt`      (scored)

The hidden verifier only inspects the two scored files, but the output contract requires all listed files to be present.

## How you are scored
A hidden verifier will independently inspect the submitted artifacts. It will extract key features from `stress_strain.csv`—such as the yield stress, plateau stress, and overall curve shape—and compare them against reference values derived from the original study. The `correlation_length.txt` value will also be compared. The final score is a weighted combination of these checks, rewarding results that reproduce the expected physical behaviour within reasonable tolerance. The exact tolerance thresholds are not disclosed, so rely on accurate execution of the protocol rather than attempting to match a specific published number.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sample_config.lammpsdata",
      "format": "other",
      "purpose": "process",
      "schema": {},
      "description": "Equilibrated configuration in LAMMPS data format."
    },
    {
      "file": "compression_traj.lammpstrj",
      "format": "other",
      "purpose": "process",
      "schema": {},
      "description": "Uniaxial compression trajectory."
    },
    {
      "file": "stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "schema": {
        "type": "table",
        "required_columns": ["strain", "stress", "density"]
      },
      "description": "Stress-strain and density-strain data from simulation."
    },
    {
      "file": "correlation_length.txt",
      "format": "txt",
      "purpose": "scored",
      "schema": {
        "type": "text"
      },
      "description": "Nonaffine displacement correlation length."
    }
  ]
}
```