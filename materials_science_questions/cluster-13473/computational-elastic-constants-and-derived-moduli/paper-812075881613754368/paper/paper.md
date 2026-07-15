Molecular dynamics simulation of size and strain rate dependent mechanical response of FCC metallic nanowires

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2006 Nanotechnology 17 3451

(http://iopscience.iop.org/0957-4484/17/14/018)

View the table of contents for this issue, or go to the journal homepage for more

Download details:
IP Address: 157.89.65.129
The article was downloaded on 10/03/2013 at 06:18

Please note that terms and conditions apply.

# Molecular dynamics simulation of size and strain rate dependent mechanical response of FCC metallic nanowires

S J A Koh and H P Lee

Institute of High Performance Computing, 1 Science Park Road, #01-01, The Capricorn,
Singapore Science Park II, Singapore 117528, Singapore
and
Department of Mechanical Engineering, National University of Singapore, 9 Engineering
Drive 1, Singapore 117576, Singapore

Received 18 April 2006, in final form 24 May 2006
Published 20 June 2006
Online at stacks.iop.org/Nano/17/3451

## Abstract
Current computational simulations on metallic nanowires are largely focused on ultrathin wires with characteristic sizes smaller than 2 nm. The electronic, thermal and optical properties form the bulk of these studies, with investigations of the mechanical properties centred on the breaking force of monatomic chains, and the structural evolution of small nanowires subjected to axial, shear, bending and torsional forces. This study seeks to build on the wealth of current knowledge for computational simulation on the mechanical properties of metallic nanowires. The simulation scale will be upped to 24 000 atoms to study a larger metallic nanowire with a 6 nm characteristic size scale. The commonly studied Au nanowire is studied in conjunction with the rarely examined Pt nanowire. The effects that size and strain rate have on the stretching behaviour of these nanowires are investigated through the simulation of nanowires with three characteristic sizes of 2, 4 and 6 nm, subjected to three distinct strain rates of $4.0 × 10^8$, $4.0 × 10^9$ and $4.0 × 10^{10}\ \mathrm{s}^{-1}$. The selected strain rates produce three distinct modes of deformation, namely crystalline-ordered deformation, mixed-mode deformation and amorphous-disordered deformation, respectively. The mechanisms behind the observations of these distinct deformation modes are analysed and explained. A Doppler ‘red-shift’ effect is observed when the nanowires are strained at the highest strain rate of $4.0 × 10^{10}\ \mathrm{s}^{-1}$. This effect is most pronounced for the nanowire subjected to the largest stretch velocity. As a result, a constrained dynamic free-vibration phenomenon is observed during stretching, which eventually leads to delocalized multiple necking, instead of a single localized neck when it is strained at a lower rate. This unique phenomenon is discussed and future research effort is in the pipeline for a more detailed investigation into metallic nanowires strained at a supersonic velocity.

## List of symbols

|  |  |  |  |
|---|---|---|---|
| $a$ | crystal lattice parameter | $E_{\mathrm{FS}}$ | Finnis–Sinclair potential energy |
| $c$ | cohesive energy parameter | $E_{\mathrm{SC}}$ | Sutton–Chen potential energy |
| $\delta$ | percentage variation of system temperature about its mean ($\mu_T$) | $\varepsilon$ | energy parameter |
| $\Delta t$ | time-step | $\varepsilon_{\mathrm{fy}}$ | first yield strain |
| $E$ | Young’s modulus (units in GPa) | $\varepsilon_{\mathrm{r}}$ | rupture strain |
| | | $\varepsilon_{[001]}$ | nominal strain in the [001] direction |
| | | $\dot{\varepsilon}_{[001]}$ | strain rate in the [001] direction |

<table>
<tbody>
<tr>
<td colspan="2">
S J A Koh and H P Lee
</td>
</tr>
<tr>
<td>
$F_{\text{SC}}$
</td>
<td>
Sutton–Chen interatomic force vector
</td>
</tr>
<tr>
<td>
$F_{[001]}^{ij}$
</td>
<td>
[001] vectoral component of the interatomic force vector
</td>
</tr>
<tr>
<td>
$\eta_{[001]}^{i}$
</td>
<td>
localized [001] stress state of atom $i$
</td>
</tr>
<tr>
<td>
$i$
</td>
<td>
atomic index $i$
</td>
</tr>
<tr>
<td>
$j$
</td>
<td>
atomic index $j$
</td>
</tr>
<tr>
<td>
$m$
</td>
<td>
interatomic potential exponent
</td>
</tr>
<tr>
<td>
$\mu_{T}$
</td>
<td>
mean system temperature over final 2000 MD time-steps
</td>
</tr>
<tr>
<td>
$n$
</td>
<td>
interatomic potential exponent
</td>
</tr>
<tr>
<td>
$N$
</td>
<td>
number of atoms
</td>
</tr>
<tr>
<td>
$\Omega^{i}$
</td>
<td>
atomic volume of atom $I$, assuming a hard sphere in a close-packed unit cell
</td>
</tr>
<tr>
<td>
$r_{ij}$
</td>
<td>
interatomic distance between atoms $i$ and $j$
</td>
</tr>
<tr>
<td>
$r_{[001]}^{ij}$
</td>
<td>
[001] vectoral component of the interatomic position vector
</td>
</tr>
<tr>
<td>
$s_{i}$
</td>
<td>
functional for local coordination of atom $i$
</td>
</tr>
<tr>
<td>
$S$
</td>
<td>
total number of time-steps
</td>
</tr>
<tr>
<td>
$\sigma_{\text{fy}}$
</td>
<td>
stress at first yield (or tensile strength, units in GPa)
</td>
</tr>
<tr>
<td>
$\sigma_{T}$
</td>
<td>
standard deviation of system temperature over final 2000 time-steps
</td>
</tr>
<tr>
<td>
$\sigma_{[001]}$
</td>
<td>
average system stress state in the [001] direction
</td>
</tr>
<tr>
<td>
$T$
</td>
<td>
simulation temperature (units in K)
</td>
</tr>
<tr>
<td>
$\tau$
</td>
<td>
Berendsen thermostat coupling constant (units in ps)
</td>
</tr>
</tbody>
</table>

### 1. Introduction

Metallic nanowires have been given significant attention from the nanotechnology research fraternity in the past decade. The rapid scaling down of electronic systems to molecular levels [1–3] requires nanoscale contacts that exhibit excellent ballistic electrical conductance. Metallic nanowires of the transition metal group were found to be excellent candidates for this purpose [4–7]. Furthermore, due to their high sensitivity towards physical stimuli like forces, electricity and heat, coupled with the ability to operate under ultrahigh frequencies, metallic nanowires were also commonly used as nanoelectromechanical systems (NEMS) [8, 9]. The excellent biocompatibility characteristics exhibited by Au nanoclusters and exceptional surface reactivity of Pt nanomaterials for catalysis [10] had opened up useful applications in the biomedical and biochemical fields. The immense potential of metallic nanowires has inevitably called for rigorous research into their electrical [7, 11–13], thermal [14–16], mechanical [17–26], magnetic [27, 28] and optical [29, 30] properties.

Extensive experimental works were performed on metallic nanowires, with particular focus on their electronic properties [6, 12, 31], mechanical properties [32–36] and thermal properties [37]. Helical ultrathin gold and platinum nanowires or nanotubes were discovered by electron-beam irradiation on thin metallic films [38, 39]. Simulated annealing was also performed, which revealed that metallic nanowires undergo a structural rearrangement from an fcc lattice to a helical single- or multi-shell structure for characteristic sizes smaller than 2 nm [26, 40, 41]. Studies on mechanical properties of metallic nanowires were centred on ultrathin [18, 21, 42–45] and monatomic chains [13, 22, 24, 46, 47], with particular focus placed on Au, Cu and Ni nanowires.

This paper presents a molecular dynamics (MD) simulation for solid fcc metallic nanowires. The simulation was performed for the commonly studied Au nanowire and the rarely studied Pt nanowire. Instead of focusing on the quantum-size effects, which are usually investigated for Au nanowires, empirical MD simulation will be employed to study the nanoscale size and strain rate effects for Au and Pt nanowires with characteristic sizes larger than 2 nm, up to the largest size scale of about 6 nm (consisting of more than 24 000 atoms). The focus of this study was centred on the mechanical response of these nanowires, subjected to uniaxial tensile deformation at three strain rates of increasing order of magnitude. The mechanics of slow strain rate crystalline dislocation deformation was analysed from the stress–strain response and atomic structural rearrangements of the nanowires. The strain rate that leads to a transition between crystalline dislocation deformation and disordered amorphous deformation [19, 20] was identified, with the interesting mixed-mode order–disorder deformation examined. Finally, a detailed investigation and analysis into the basic mechanism behind strain-rate amorphized deformation was presented, with the observation of an interesting material- and size-dependent plastic flow necking characteristic of the nanowires at the highest applied strain rate.

### 2. Atomistic simulation methodology and program benchmark

MD simulation was performed on solid fcc Au and Pt nanowires. The nanowires were subjected to uniaxial tensile strain in the [001] crystallographic direction. In this simulation, nanowires with circular cross-sections were studied. Circular cross-sections were selected for this simulation as they presented the most stable and natural cross-sectional configuration [40, 48, 49]. Nanowires with diameters of five lattice constants $(5\phi)$, ten lattice constants $(10\phi)$ and 15 lattice constants $(15\phi)$ were simulated. These diameters corresponded to approximate nanowire sizes of 2, 4 and 6 nm respectively. The nanowire length was set at twice the diameter of the nanowire, maintaining a fixed length-to-diameter aspect ratio of 2. This was to ensure that a non-dimensional size analysis was performed, whereby other effects that are dependent on nanowire length-to-diameter ratio were eliminated. The aspect ratio of 2 was selected in order to prevent the phenomenon of dynamic dislocation and Rayleigh instability occurring at slow strain rates for large aspect ratios of larger than 5 [23, 50], and the columnar formation of concurrent double necking for short stumps with aspect ratio of smaller than 1 [51]. Hence, Au and Pt nanowires with diameter $\times$ length lattice dimensions of $5\phi\times10$, $10\phi\times20$ and $15\phi\times30$ for each material were simulated. This corresponded to atomic systems of 890, 6660 and 24 000 atoms respectively. Figure 1 shows the atomic diagrams for these nanowires.

Nanowire stretching was simulated by displacing the top and bottom fixed atomic planes (brown atoms) in opposite directions at a constant strain rate of $\dot{\varepsilon}$. The nanowires were strained at three different strain rates of $4\times10^{8}\ \text{s}^{-1}$, $4\times10^{9}\ \text{s}^{-1}$ and $4\times10^{10}\ \text{s}^{-1}$. The strain rate magnitudes were chosen

Simulation of mechanical response of metallic nanowires (size and strain rate effects)

![](./images/812075881613754368_1.jpg)

Figure 1. Atomic diagrams for Pt and Au nanowires, with atoms at their original fcc lattice positions. White atoms denote Pt atoms, yellow atoms denote Au atoms, brown atoms denote fixed atomic layers, cyan atoms denote surface atoms and pink atoms denote corner atoms. (a) $\phi \times 10$ (890 atoms); (b) $10\phi \times 20$ (6660 atoms); (c) $15\phi \times 30$ (24 000 atoms). Diagrams alongside the nanowires indicate the respective longitudinal cross-sections.

to correspond to the transition from crystalline deformation at low strain rates $(<10^{9}\ s^{-1})$ to amorphous deformation at very high strain rates $(>10^{10}\ s^{-1})$, as reported in various works [19, 20, 23, 52] for nanowires with characteristic sizes smaller than 2 nm. This study will determine if such transitions take place in nanowires of characteristic sizes larger than 2 nm, and observations on unique phenomena associated with high velocity straining of metallic nanowire will be made.

The Lennard-Jones (LJ) pair potential was conventionally used for MD simulation of fluids and rare gases [53], but was shown to be manifestly inadequate in the description of metallic bonds [54-57]. Various empirical many-body interatomic potentials were therefore developed to address this inadequacy. Amongst these were, in chronological order, the effective medium theory (EMT) [58], the embedded-atom model (EAM) [59], the Finnis-Sinclair (FS) pair functional formulation [60] and the Sutton-Chen (SC) potential [61]. The development of 'many-body' potentials were such that the later model provided a simpler formulation for the pair functional than the earlier one, which enabled a more rapid and efficient computation of the kinematic and kinetic system quantities via time integration. In the process, significant savings in computation time were achieved as each newer model was adopted. Nevertheless, simplicity in the newer models usually led to a compromise in accuracy in predicting the physical quantities. As such, they must be verified against experimental results or existing simulation works for the specific physical quantity to be investigated, before it was employed for further simulations. The SC potential model was selected for verification of its prediction accuracy for the mechanical properties of metallic fcc nanowires.

Based on the second moment approximation of the tight-binding theory, Finnis and Sinclair determined the non-linear functional of the EAM to be a square root expression, as follows:
$$
E_{\mathrm{FS}}=\varepsilon\left[\frac{1}{2} \sum_{i=1}^{N} \sum_{\substack{j=1 \\(j \neq i)}}^{N} V\left(r_{i j}\right)-c \sum_{i=1}^{N} \sqrt{\rho_{i}}\right]. \quad(1)
$$

Sutton and Chen proposed simple power laws for both the repulsive pair potential and the cohesive pair functional in equation (1) to account for long-range interactions, as follows:
$$
E=\varepsilon\left[\frac{1}{2} \sum_{i=1}^{N} \sum_{\substack{j=1 \\(j \neq i)}}^{N}\left(\frac{a}{r_{i j}}\right)^{n}-c \sum_{i=1}^{N} \sqrt{\sum_{\substack{j=1 \\(j \neq i)}}^{N}\left(\frac{a}{r_{i j}}\right)^{m}}\right]. \quad(2)
$$

S J A Koh and H P Lee

**Table 1.** Simple SC potential parameters for Au and Pt.

<table>
  <thead>
    <tr>
      <th rowspan="2">Parameter</th>
      <th colspan="2">Fitted parameter value</th>
    </tr>
    <tr>
      <th>Au</th>
      <th>Pt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$ (Å)</td>
      <td>4.08</td>
      <td>3.92</td>
    </tr>
    <tr>
      <td>$\varepsilon$ (meV)</td>
      <td>12.793</td>
      <td>19.833</td>
    </tr>
    <tr>
      <td>$c$</td>
      <td>34.408</td>
      <td>34.408</td>
    </tr>
    <tr>
      <td>$m$</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <td>$n$</td>
      <td>10</td>
      <td>10</td>
    </tr>
  </tbody>
</table>

Sutton and Chen fitted the potential parameters for ten fcc metals based on the lattice constant, experimental cohesive energy and bulk modulus; this was to be the fundamental form of the SC potential, which was known as the simple SC potential. The simple SC potential provided a good agreement to the experimental bulk modulus and elastic constants ($C_{11}$, $C_{12}$ and $C_{44}$) for most fcc metals, with the exception of Ni and Cu [14, 61, 62]. Rafii-Tabar and Sutton [63] extended the usage of these parameters to study binary alloys of fcc metals. Kimura *et al* [62] re-fitted the SC potential parameters to arrive at the quantum-corrected SC (Q-SC) potential, which accounted for a more accurate depiction of the vacancy formation energy, phonon dispersion energy and surface energy, but resulted in a poorer estimation of the elastic constants compared to the original simple SC parameters. Since this study is focused on the mechanical response of Au and Pt nanowires, the simple SC potential will be adopted as the potential model for atomistic simulation. Table 1 shows the SC parameters for both Au and Pt [61]. The interatomic force expression is given as

$$
\mathbf{F}_{\mathrm{SC}}=-\frac{\varepsilon}{r_{i j}}\left[n\left(\frac{a}{r_{i j}}\right)^{n}-\frac{m c}{2}\left(s_{i}^{-1 / 2}+s_{j}^{-1 / 2}\right)\left(\frac{a}{r_{i j}}\right)^{m}\right] \hat{\mathbf{r}}_{i j}.
\tag{3}
$$

Equation (3) defines the force vector between atomic pair $i$ and $j$. The positions and velocities of the constituent atoms were determined by solving Newton equations of motion, using the Verlet leapfrog algorithm.

In this simulation, the time-step ($\Delta t$) was set at 1.0 fs ($10^{-15}$ s). The nanowire was first allowed to attain a thermal equilibrium steady state at the simulation temperature of 300 K. This was done based on the Nosé–Hoover thermostat [64], while maintaining the nanowires at their unstretched lengths. Thermal equilibrium was completed when the percentage variation ($\delta$) of the system temperature about its mean was less than 5% over the final 2000 steps of system equilibration, where $\delta$ is expressed as follows:

$$
\delta=\frac{\sigma_{T}}{\mu_{T}} \times 100 \%
$$

and

$$
\sigma_{T}=\sqrt{\frac{\sum_{2000}\left(T-\mu_{T}\right)^{2}}{2000}}
\tag{4}
$$

where $\delta$ is the percentage variation, and $\sigma_{T}$ is the standard deviation, which is defined as the root-mean-square (rms) average of the difference between the system temperature ($T$) at each MD step, from the mean system temperature ($\mu_{T}$), over the final 2000 MD steps. From the simulation, thermal equilibrium was typically achieved in about 0.1 ns (or 100 000 time steps).

It was observed that there were some residual tensile stresses in the thermally equilibrated nanowires. This was attributed to surface contraction in the nanowires due to the surface tension effect in nanoscale structures. This effect was most pronounced in the $5\phi \times 10$ nanowires, which contains the highest proportion of surface atoms. This observation will be discussed in greater detail in the following section. At this stage, the nanowires were progressively contracted along their length by reducing the spacing between the fixed atomic planes over a very small interval. Thermal equilibration was repeated for the contracted nanowire. This process was repeated until the nanowire stress (equation (6) below) upon thermal equilibration was within a near-zero range of $\pm 0.05$ GPa, which signifies total relaxation of the nanowire was achieved. Total relaxation of the nanowires was typically completed within five iterations.

Subsequently, the nanowire was axially loaded by applying a constant strain rate along the [001] axis. The atomic system was allowed to expand adiabatically, without any thermal constraints applied. This was to reflect the more realistic internal temperature changes due to structural lattice amorphization under high strain rates [19, 20]. The potential cut-off was set at $2.5a_{\mathrm{nn}}$, where $a_{\mathrm{nn}}$ is the nearest neighbour separation, and $a_{\mathrm{nn}} \approx 0.707a$ in an fcc lattice. At this cut-off value, the interatomic attractive force was less than 0.1% of the interatomic force at $a_{\mathrm{nn}}$.

The localized stress state for atom $i$ at each strain step was taken as an atomic virial expression [65], as follows:

$$
\eta_{[001]}^{i}=\frac{1}{\Omega^{i}} \sum_{\substack{j=1 \\(j \neq i)}}^{N} F_{[001]}^{i j} r_{[001]}^{i j}.
\tag{5}
$$

The axial stress on the nanowire is taken as the average of the local stresses on all atoms:

$$
\sigma_{[001]}=\frac{1}{N} \sum_{i=1}^{N} \eta_{[001]}^{i}.
\tag{6}
$$

Equation (6) was subsequently used to determine the stresses in the nanowire at each strain step, and the constitutive stress–strain response of the nanowire under uniaxial elongation can then be obtained.

The DL_POLY_2 MD simulation package was used in this study. DL_POLY_2 is a parallel MD package developed at Daresbury Laboratory (UK) [66], parallelized based on the message passing interface (MPI) thread, where a hypercube computational architecture [67] was assumed. The program was originally designed to handle equilibrium MD (EMD) simulations, with no options available for handling non-equilibrium MD (NEMD) simulations. The authors had therefore modified the original program to suit the purpose of nanowire straining NEMD simulations. The modified program was benchmarked against two independent works done by Finbow *et al* [17] and Liang and Zhou [23]. The former simulated Pt and Ag nanowire straining by scaling the 1D periodic boundary box along the [001] axis, in a quasi-static manner, at four different temperatures, and the latter performed simulation of Cu nanowires based on constant velocity stretching of fixed atomic layers at extreme ends, at four different strain rates. Finbow *et al* employed the simple

Simulation of mechanical response of metallic nanowires (size and strain rate effects)

Table 2. DL_POLY_2 program benchmark for Pt and Ag nanowire against Finbow *et al*. (Results from Finbow *et al* in parentheses.)

<table>
<thead>
<tr>
<th></th>
<th colspan="2">Pt nanowire</th>
<th colspan="2">Ag nanowire</th>
</tr>
<tr>
<th>$T$ (K)</th>
<th>50</th>
<th>273</th>
<th>43</th>
<th>219</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E$ (nN)</td>
<td>150 (151)</td>
<td>123 (125)</td>
<td>101.3 (105.0)</td>
<td>82.2 (85.0)</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.076 (0.078)</td>
<td>0.052 (0.059)</td>
<td>0.100 (0.103)</td>
<td>0.096 (0.089)</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (nN)</td>
<td>14.76 (15.00)</td>
<td>9.78 (10.30)</td>
<td>13.86 (14.00)</td>
<td>8.50 (8.90)</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.712 (0.720)</td>
<td>0.998 (&gt;1.000)</td>
<td>0.850 (0.940)</td>
<td>0.790 (0.920)</td>
</tr>
</tbody>
</table>

Table 3. DL_POLY_2 program benchmark for Cu nanowire against Liang and Zhou. (Results from Liang and Zhou in parentheses.)

<table>
<thead>
<tr>
<td>$\dot{\varepsilon}$ ($\text{s}^{-1}$)</td>
<td>$1.67\times10^{7}$</td>
<td>$1.67\times10^{8}$</td>
<td>$1.67\times10^{9}$</td>
<td>$1.67\times10^{10}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>$E$ (GPa)</td>
<td>84.26 (76.22)</td>
<td>83.77 (75.81)</td>
<td>86.43 (73.75)</td>
<td>66.36 (60.00)</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.050 (0.062)</td>
<td>0.052 (0.063)</td>
<td>0.067 (0.080)</td>
<td>0.090 (0.100)</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>5.70 (6.20)</td>
<td>5.89 (6.30)</td>
<td>7.32 (7.50)</td>
<td>7.79 (7.60)</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.24 (0.23)</td>
<td>0.26 (0.21)</td>
<td>0.34 (0.32)</td>
<td>0.37 (0.40)</td>
</tr>
</tbody>
</table>

Table 4. Comparison between simple SC predicted and experimental elastic constants for Au and Pt, as contrasted to Cu, at 300 K [14]. The mean deviation denotes the average absolute errors between the predicted and experimental values for the three elastic constants ($C_{11}$, $C_{12}$ and $C_{44}$). $C_{12}/C_{44}$ gives the approximate deviation from the simple Cauchy relation, which directly reflects the propensity toward density-dependent ‘many-body effects’ in transition metals. (All experimental results in parentheses.)

<table>
<thead>
<tr>
<th>Metal</th>
<th>Au</th>
<th>Pt</th>
<th>Cu</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{11}$ (GPa)</td>
<td>191.20 (192.34)</td>
<td>323.51 (346.70)</td>
<td>175.70 (168.39)</td>
</tr>
<tr>
<td>$C_{12}$ (GPa)</td>
<td>151.60 (163.14)</td>
<td>259.85 (250.70)</td>
<td>132.00 (121.42)</td>
</tr>
<tr>
<td>$C_{44}$ (GPa)</td>
<td>47.20 (41.95)</td>
<td>78.16 (76.50)</td>
<td>58.60 (75.39)</td>
</tr>
<tr>
<td>Mean deviation</td>
<td>6.73%</td>
<td>4.17%</td>
<td>11.8%</td>
</tr>
<tr>
<td>$C_{12}/C_{44}$</td>
<td>3.21 (3.89)</td>
<td>3.32 (3.28)</td>
<td>2.25 (1.61)</td>
</tr>
</tbody>
</table>

SC potential for their simulation while Liang and Zhou adopted the EAM. Program benchmarking was performed based on the comparison of first yield stress ($\sigma_{\text{fy}}$) and strain ($\varepsilon_{\text{fy}}$), Young’s modulus before first yield ($E$) and the rupture strain ($\varepsilon_{\text{r}}$) for the Pt, Ag and Cu nanowires. Tables 2 and 3 show the comparison of mechanical properties obtained from DL_POLY_2 and the stated works. It can be seen from table 2 that the agreement was excellent for Pt and Ag nanowires. This should be expected as both simulations adopted the same simple SC potential for nanowire simulation. As for the Cu nanowire, table 3 shows that the agreement was generally good with the exception of the Young’s modulus, where a difference of about 15% was observed for the strain rate of $1.67\times10^{9}$. This was attributed to the poor elastic constant prediction for the simple SC model for Cu [14, 61], whereby the MD predicted values deviated from the experimental elastic constants by up to 12%, as shown in table 4. Therefore, in the case of the Cu nanowire, the EAM would provide a more reliable prediction for its mechanical behaviour [62]. Table 4 also shows the comparison between the elastic constants predicted by the simple SC potential and experimental data for Au and Pt, at a temperature of 300 K. In this case, excellent agreement was found for Au and Pt, with an absolute mean error of less than 7% between the simple SC-predicted MD model and the experimental results. The simple SC potential was therefore verified as a valid potential for simulation of the mechanical response of Au and Pt nanowires. The modified version of DL_POLY_2 was also adequately benchmarked against the MD simulation of mechanical straining of metallic nanowires. Therefore, this simulation will employ the simple SC potential, and MD simulation will be performed by the modified version of DL_POLY_2, running on an eight-CPU parallel hypercube architecture. Atomistic visualization was done using Visual Molecular Dynamics (VMD), developed by the Theoretical Physics Group of the Beckman Institute at UIUC (Illinois, US) [68].

### 3. Simulation results

The nanowires shown in figure 1 were first allowed to attain thermal equilibrium at 300 K based on the Nosé–Hoover thermostat. It was observed that, upon thermal equilibration, initial tensile stresses were present in the unstretched nanowires. The magnitude of initial tensile stresses varied inversely with the proportion of surface atoms in the nanowires, as shown in figure 2(a). Initial tensile stresses in unstretched metallic nanowires were similarly observed in numerous other works [17, 18, 21, 23, 42, 52], but no mention was made of the reasons behind the presence of such stresses in these works.

The presence of initial tensile stresses in the nanowires was attributed to the inward surface relaxation phenomenon in fcc transition metals. Due to the availability of open bonds, surface atoms were at a higher electronic state as compared to atoms situated within the interior bulk and hence possess a higher electronic cohesive energy. This, coupled with asymmetrical bonding of surface atoms with neighbouring atoms, results in surface tension in restrained surfaces and surface contraction in unrestrained surfaces. This effect is usually predominant in nanoscale systems due to the high proportion of surface atoms. It should be noted here that surface atoms were determined to be the atoms that reside within one lattice constant from the surface atomic layer,

![](./images/812075881613754368_2.jpg)

![](./images/812075881613754368_3.jpg)

Figure 2. Surface contraction resulting in (a) initial tensile stress in restrained nanowires and (b) nanowire contraction in unrestrained nanowires.

![](./images/812075881613754368_4.jpg)

Figure 3. Atomic diagrams for $5\phi\times10$ nanowires with fixed layers removed. All colour codes apply as in figure 1. (a) Pt nanowire; (b) Au nanowire. For both diagrams, the left diagrams show the initial configuration at their original fcc lattice positions; the right diagrams show the thermally relaxed configurations based on Nosé–Hoover thermostat.

where the coordination numbers of these atoms were less than 12 in fcc crystals. The proportion of surface atoms in the $5\phi\times10$, $10\phi\times20$ and the $15\phi\times30$ nanowires were therefore determined to be approximately 67%, 36% and 25% respectively, for both Pt and Au nanowires. Total nanowire contraction due to the surface tension effect was determined by allowing the restrained nanowires to relax to a zero initial stress state. This was done by reducing the spacing between the fixed atomic planes in small intervals, until a near-zero stress was achieved upon thermal equilibration. An exact zero stress state could not be achieved for all nanowires due to the occurrence of corner melting in the $5\phi\times10$ nanowires, which will be discussed in the following paragraph. Figure 2(b) shows the relationship between percentage nanowire contraction and the proportion of surface atoms.

In order to ensure that a realistic simulation was performed, it must be verified that the fixed atomic planes do not artificially hold the nanowires in an apparent fcc ordered arrangement, in which, if the restraints were removed, the unrestrained nanowires would take up an alternative order, or even be bulk melted and reduced to an atomic cluster at 300 K. For this purpose, the fixed atomic planes were removed and the unrestrained nanowires were allowed to thermally equilibrate. Figures 3–5 show the atomic structural appearance of the three unrestrained nanowires upon thermal equilibration. It could be seen that the crystalline order, overall cross-sectional geometry and nanowire shape were preserved for all three sizes, with the exception of some small perturbation at the corner atoms. This was due to the smaller coordination numbers of the corner atoms, where kinetic thermal excitations had overcome the total resultant electronic cohesive force, which resulted in corner pre-melting. This phenomenon was especially pronounced in the smallest $5\phi\times10$ nanowires, where long-range interaction between corner atoms and other atoms within the nanowire was restricted to only five lattice constants in the transverse [100] and [010] directions, and therefore cohesive forces for these atoms were significantly smaller as compared to the two larger nanowires. For this reason, corner pre-melting was less pronounced in the larger $10\phi\times20$ and $15\phi\times30$ nanowires (figures 4 and 5). Due to limited long-range interaction in the transverse directions, it could thus be observed from figure 3 that the corner atoms were generally displaced in the transverse directions only during corner pre-melting. Corner pre-melting would generally have a negligible effect on the overall mechanical behaviour of the nanowire. This was because, under low strain rates where crystalline order was maintained during deformation, dislocation necking during uniaxial deformation will only occur within the middle two-thirds of the nanowire length. At high strain rates, where amorphization has taken place, the fcc crystalline order of the nanowire will be broken down, and the nanowire will

![](./images/812075881613754368_5.jpg)

Figure 4. Atomic diagrams for $10\phi\times20$ nanowires with fixed layers removed. All other remarks to be applied here were similar to those in figure 3. No obvious corner melting was observed for both nanowires.

![](./images/812075881613754368_6.jpg)

Figure 5. Atomic diagrams for $15\phi\times30$ nanowires with fixed layers removed. All other remarks to be applied here were similar to those in figures 3 and 4.

deform and neck like an amorphous strand. Due to the overall lack of crystalline order in the nanowire, disorder at the corner atoms will be indifferentiable from other atoms in the nanowire. It was therefore concluded that the fixed atomic planes do not provide artificial restraints to the nanowires at 300 K, and corner melting observed in unrestrained nanowires would not significantly affect the mechanical behaviour in restrained nanowires where corner melting was prevented from occurring.

Next, abrupt energetic drops in the atomic system upon commencement of nanowire straining will be observed and analysed. Figure 6 shows the variation of average cohesive energy per atom over an initial 3% strain for all nanowires. It was first observed that the average cohesive energy per atom for the unstrained $5\phi\times10$ nanowires was 2% and 2.7% larger than the $10\phi\times20$ and the $15\phi\times30$ nanowires respectively. This was expected as the $5\phi\times10$ nanowires contained the largest proportion of surface atoms (67%), and since surface atoms exist at a higher electronic state than interior atoms the $5\phi\times10$ nanowires would logically give the highest average cohesive energy per atom. Next, a sudden drop in cohesive energy was observed upon the commencement of uniaxial strain. It should be noted that due to the fixed sampling interval of 0.4% strain in this study the actual energetic drop profile might not exactly resemble the linear trend as shown in figure 6. The actual profile might occur over a shorter strain interval, with a non-linear trend. Detailed analysis of this topic would be out of line from the theme of this study, and will be reserved as a separate investigation. The focus of this study will be the total energy drop instead of the drop profile.

It was observed from figure 6 that the percentage drop in cohesive energy was dependent on the strain rate, which was found to be about 0.1%, 1.0% and 9.0% for the strain rates of $4.0\times10^{8}\ \text{s}^{-1}$, $4.0\times10^{9}\ \text{s}^{-1}$ and $4.0\times10^{10}\ \text{s}^{-1}$ respectively. The same percentage drop in cohesive energy was observed for both Pt and Au nanowires for all three characteristic sizes. It could therefore be concluded that the percentage drop in average cohesive energy per atom is dependent only on the strain rate at this scale level. The drop in cohesive energy indicated a breakdown in crystalline order of the fcc lattice structure, which is a result of bond energy release due to the breaking of metallic bonds. Bond breaking is a direct consequence of kinetic energy overcoming the interatomic cohesive energy (potential energy), which in turn sets the atoms in random motion. Two sources of kinetic energy were identified, namely thermal excitation and an externally applied momentum. In the former source, the kinetic energy is proportional to $kT$. Hence, at a sufficiently high $T$, thermal kinetic energy could overcome the interatomic cohesion force that holds the atoms together in their crystal lattice positions, which results in the phenomenon of thermal melting. As

![](./images/812075881613754368_7.jpg)

Figure 6. Variation of cohesive energy per atom over an initial 3% strain for (a) Pt nanowires and (b) Au nanowires.

such, a sudden drop in cohesive energy was observed at the onset of melting in metallic nanowires [17]. In the latter source, kinetic energy is proportional to $p^{2}$, where $p$ refers to momentum. Therefore, at a sufficiently high $p$, crystal order will also be broken. This would be possible if a nanowire was stretched at a high strain rate. In this case, the large momentum applied at the ends propagates into the atomic structure of the nanowire, which overcomes the cohesive energy, resulting in a disordered amorphous deformation [19, 20, 52]. It could therefore be said that a fixed drop in cohesive energy per atom is a good indicator that a phase transformation had taken place, and amorphous disorder had set in. It was previously shown that there was a cohesive energy drop of 40 meV per atom in a Pt nanowire at the onset of melting [17]. In this study, a cohesive energy drop of about 60 meV was observed when the Pt nanowire was stretched at the strain rate of $4.0 \times 10^{9} \mathrm{~s}^{-1}$. A parallel could thus be drawn here, that the strain rate of $4.0 \times 10^{9} \mathrm{~s}^{-1}$ produced crystal lattice disorder equivalent to that at the onset of thermal melting. This implied that a transition between crystalline- ordered and amorphous-disordered deformation had taken place at an approximate strain rate of $4.0 \times 10^{9} \mathrm{~s}^{-1}$. The drop of more than 500 meV at $4.0 \times 10^{10} \mathrm{~s}^{-1}$ indicated that complete disorder of the crystal lattice had set in and therefore, the nanowire will undergo amorphous deformation. These observations revealed momentum-induced kinetic energy as the main mechanism behind the phenomenon of amorphous deformation of nanowires at high strain rates, where an abrupt drop of 1.0% in cohesive energy indicates the onset of amorphous-disordered deformation. The same observations were made for the Au nanowire.

Upon strain commencement, the nanowires undergo a stress-hardening process up to the first yield strain where, depending on the applied strain rate, an abrupt or gradual reduction in stress was observed. A linear stress-strain relationship was expected before first yield in crystalline-ordered deformation with zero or negligible crystal imperfections. But, due to the possibility of surface pre- melting in nanowires and the momentum-induced disordered deformation at high strain rates, overall crystalline order may

![](./images/812075881613754368_8.jpg)

Figure 7. Stress-strain response for all nanowires, up to a maximum strain of twice the unstrained length for (a) Pt nanowires and (b) Au nanowires.

<table>
<caption>Table 5. Statistical correlation coefficients computed from linear regression for stress-strain response of nanowires before first yield (for $\dot{\varepsilon} \leqslant 4.0 \times 10^9$ s$^{-1}$) or before attainment of maximum stress (for $\dot{\varepsilon} = 4.0 \times 10^{10}$ s$^{-1}$). Elastic deformation was determined as those with correlation coefficients of larger than 0.950 (or a statistical error of 5% from the ideal linear relationship). Quantities in bold denote non-linear deformation from the commencement of strain.</caption>
<tbody>
<tr>
<th rowspan="2"></th>
<td colspan="3">Pt nanowire</td>
<td colspan="3">Au nanowire</td>
</tr>
<tr>
<td>$4.0 \times 10^8$ s$^{-1}$</td>
<td>$4.0 \times 10^9$ s$^{-1}$</td>
<td>$4.0 \times 10^{10}$ s$^{-1}$</td>
<td>$4.0 \times 10^8$ s$^{-1}$</td>
<td>$4.0 \times 10^9$ s$^{-1}$</td>
<td>$4.0 \times 10^{10}$ s$^{-1}$</td>
</tr>
<tr>
<th>$5\phi \times 10$</th>
<td>0.9991</td>
<td>0.9870</td>
<td>0.9752</td>
<td>0.9965</td>
<td>0.9859</td>
<td>0.9699</td>
</tr>
<tr>
<th>$10\phi \times 20$</th>
<td>0.9996</td>
<td>0.9984</td>
<td>0.9573</td>
<td>0.9990</td>
<td>0.9960</td>
<td><b>0.9074</b></td>
</tr>
<tr>
<th>$15\phi \times 30$</th>
<td>0.9996</td>
<td>0.9970</td>
<td><b>0.8881</b></td>
<td>0.9984</td>
<td>0.9921</td>
<td><b>0.6231</b></td>
</tr>
</tbody>
</table>

not be preserved even at very low strain magnitudes, and hence linear elastic deformation before first yield may not be valid. A measure of linearity was therefore required to differentiate between non-linear and linear deformation for the nanowires. The statistical correlation coefficient was used for this purpose. The correlation coefficient is a non-dimensional quantity, which expresses the 'strength of relation' between an independent and a dependent statistic, whose relation is fitted to an analytical expression. A coefficient of 1.0 implies a 'perfect fit' of the analytical expression to the two statistics, while a coefficient of 0.0 implies no analytical relationship exists between them. The interested reader may refer to existing reference texts [69] for an in-depth exposition on this topic. In this simulation, the independent and dependent statistics were the nanowire strain and stress, respectively. An analysis was performed for the stress-strain response of the nanowires (figure 7) before the first yield for the lower strain rates of $4.0 \times 10^8$ s$^{-1}$ and $4.0 \times 10^9$ s$^{-1}$, and before the attainment of maximum stress for the highest strain rate of $4.0 \times 10^{10}$ s$^{-1}$. The resulting correlation coefficient obtained from this statistical fitting will be a measure of the 'degree of linearity'. Table 5 shows the correlation coefficients for all nanowires at all strain rates, where values larger than 0.950 was considered to satisfy the requirement of statistical linearity and hence determined to have deformed linearly. The converse is also true.

Figure 7 shows the stress-strain response of the Pt and Au nanowires. At the strain rate of $4.0 \times 10^8$ s$^{-1}$, all nanowires showed a linear stress-strain response (table 5) for up to a strain of about 8.4%, before a sudden drop in stress was observed at first yield. At this point, single (111) dislocation planes were developed as shown in figures 8-10. The development of dislocation planes results in a crystal lattice transformation from an fcc structure to a hcp structure

![](./images/812075881613754368_9.jpg)

Figure 8. Structural evolution of $5\phi\times10$ nanowires during stretching, at three different strain rates for (a) Pt nanowire and (b) Au nanowire.

at the dislocation interfaces [70]. This transformation leads to stress relaxation, whereby a portion of the crystal structure was displaced. With the exception of the $5\phi\times10$ Au nanowire, the stresses for other nanowires were abruptly reduced to less than 50% of the first yield stress upon stabilizing into a new atomic configuration, with a single, well defined (111) dislocation plane. Upon full relaxation, the nanowire undergoes a second cycle of linear stress-strain increment, until the development of new dislocations occurs, which causes the whole cycle to repeat itself again. The cyclical stress-strain progression of such heterogeneous plastic deformation produces multiple dislocations in the nanowires. This significantly weakens the nanowire structure, thereby causing a progressively lower peak stress to be achieved at each subsequent cycle. The 60% drop in stress after the first cycle (at first yield), as compared to the smaller stress peaks and stress drops at the subsequent cycles, suggested that the first dislocation plane formed the main slip plane, and subsequent dislocations developed as dislocation branches from main dislocation plane. This would result in dislocation necking, whereby progressive thinning of the nanowire at its neck is a consequence of interfacial slipping of the main dislocation plane. This would determine the eventual location of the neck and rupture point as the point where the main (111) dislocation plane emerges from the surface of the nanowire in the [111] direction. Subsequent slippage along the dislocation fault line results in a neck being formed, as the contact area between the complementary slip interfaces is progressively reduced. From figures 8–10, it could be seen that the point of rupture was rarely found at the mid-height of the nanowire. This was due to the (111) inclination of the main slip plane, which typically developed in the middle two-thirds region of the nanowire. With the two-to-one aspect ratio of

Simulation of mechanical response of metallic nanowires (size and strain rate effects)

the nanowire, formation of the neck was typically found at the one-third or two-thirds height of the nanowire.

Stress-strain linearity was also observed when the nanowires were strained at the higher strain rate of $4.0 \times 10^{9} \ \text{s}^{-1}$. This linearity was sustained to a larger strain of about 11%, with a first yield stress of up to 15% larger than that when the nanowire was subjected to a lower strain rate, after which simultaneous formation of multiple slip planes was observed, as shown in figures 8-10. In this formation, multiple twinning planes were developed along the entire length of the nanowire, which was particularly evident in the cross-sectional diagrams shown in figures 9 and 10, for the larger $10\phi \times 20$ and $15\phi \times 30$ nanowires respectively. This was unlike the single (111) dislocation plane formation when the nanowire was strained at a slower rate of $4.0 \times 10^{8} \ \text{s}^{-1}$. This was attributed to the momentum-induced disorder in the nanowire when it was stretched at this strain rate. The disorder weakens the crystal lattice structure and disrupts the discrete lattice order, and the nanowire goes into a mixed-mode heterogeneous-homogeneous plastic flow deformation. Momentum-induced lattice disorder reduces the average cohesive energy by about 60 meV (figure 6) and hence encourages simultaneous formation of multiple dislocation planes in the crystallographically weakened nanowire. This mixed-mode deformation was also evident from the abrupt drop in stress upon first yield, which was a characteristic of low strain rate deformation, and the subsequent absence of cyclical stress-strain response after first yield, where the nanowire displayed a homogeneous plastic flow behaviour commonly observed in high strain rate deformation.

It was noted that the small $5\phi \times 10$ nanowire displayed irregular, cyclical stress-strain behaviour, which indicated the stronger presence of crystalline dislocation slippage after first yield, as compared to the larger nanowires. This was attributed to the higher proportion of surface atoms, whereby a larger momentum was required to induce overall lattice disorder in the nanowire. At this strain rate, the surface atoms would have maintained average crystalline order, which results in the evidence of dislocation slippage after first yield. Momentum-induced disorder in the interior atoms resulted in a marginally more ductile slippage at first yield as compared to the lower strain rate of $4.0 \times 10^{8} \ \text{s}^{-1}$. The increased ductility showed up in the attainment of a larger first yield strain, a more rounded peak stress at first yield, and a lower 50% drop in stress after first yield. The presence of 'noise spikes' was also observed for both $5\phi \times 10$ Pt and Au nanowires, as shown in figure 7. This was due to pre-melting of surface atoms due to thermal excitation, which results in the migration of these atoms away from their equilibrium lattice positions, thus causing perturbations in interatomic forces during stretching. Due to the large proportion of surface atoms in the $5\phi \times 10$ nanowires, the effect of surface pre-melting that leads to 'noise spike' fluctuations in nanowire stress was significant as compared to the larger nanowires. The Au nanowire displayed a non-cyclical stress-strain response after first yield, with the presence of a significant number of 'noise spikes' during straining, as seen in figure 7(b). This was due to the increased thermal perturbation in Au atoms as compared to Pt atoms. The increased perturbation was a result of smaller interatomic cohesive force in Au as compared to Pt. The cohesive force was estimated to be about 35% smaller in Au, estimated from the value of the energy parameter $\varepsilon$ in table 1, and the SC interatomic force expression in equation (3). As such, the Au atoms undergo larger atomic oscillations due to thermal excitation, which showed up as the 'noise spikes' in the stress-strain response.

Finally, it was noted that the necks and rupture point of the nanowires subject to the strain rate of $4.0 \times 10^{9} \ \text{s}^{-1}$ were generally located at the mid-height of the nanowire. This was a direct consequence of the mixed-mode deformation. Formation of multiple twinning planes during initial dislocation was encouraged by the momentum-induced structural disorder. This results in the lack of a clearly defined plane of slippage, which, coupled with amorphous disorder in the regions of dislocation, led to a homogeneous plastic failure at the mid-height of the nanowires.

When the nanowires were subjected to the highest strain rate of $4.0 \times 10^{10} \ \text{s}^{-1}$, their fcc crystalline order was completely lost upon strain commencement. A prior study reported that an fcc crystal-to-glass transformation was observed for Ni nanowires at the strain rate of $5.0 \times 10^{10} \ \text{s}^{-1}$ [19]. A similar order-to-disorder transformation was observed in this study for both Pt and Au nanowires. The mechanism behind this transformation was determined to be momentum induced, as seen in the drop in cohesive energy upon strain commencement in figure 6. From table 5, the smallest $5\phi \times 10$ nanowires and the $10\phi \times 20$ Pt nanowire deformed linearly up to the attainment of maximum stress. On the other hand, the $10\phi \times 20$ Au nanowire and the large $15\phi \times 30$ nanowires deformed in a non-linear fashion upon strain commencement. Due to the homogeneous plastic flow of the disordered structure, the $5\phi \times 10$ Pt and Au nanowires attained a 20% and 45% larger maximum stress respectively as compared to that strained at the slowest strain rate of $4.0 \times 10^{8} \ \text{s}^{-1}$, as shown in figure 7. Correspondingly, the nanowire could be stretched up to about 13% strain before an overall reduction of nanowire strength was observed, as compared to 8% and 11% for the strain rates of $4.0 \times 10^{8}$ and $4.0 \times 10^{9} \ \text{s}^{-1}$, respectively. The disordered nature of the crystal lattice did not allow the formation of well defined slip planes. Instead, a glass-like homogeneous plastic flow behaviour was observed. Due to the absence of dislocation planes, there was no abrupt transformation of the crystal lattice structure during deformation, which would otherwise significantly reduce the interatomic spacing along these slip planes and thereby result in a sudden stress reversal. This allowed interatomic cohesive forces to reach their maximum value during straining, before gradually reducing as the average interatomic distance was increased upon further strain. This also accounts for the gradual rounding of the stress-strain curve at maximum stress in disordered deformation.

An interesting phenomenon was observed when the larger $10\phi \times 20$ and $15\phi \times 30$ nanowires were strained at $4.0 \times 10^{10} \ \text{s}^{-1}$. The stress-strain response showed a stress rebound at an intermediate point between zero-stress and maximum stress for both nanowires. During the stress rebound, a stress plateau was observed for the $10\phi \times 20$ nanowires and stress drops of 0.47 and 1.15 GPa were observed for the $15\phi \times 30$ Pt and Au nanowires respectively, as shown in figure 7. The nanowire stress recovered upon further strain after the rebound,

![](./images/812075881613754368_10.jpg)

Figure 9. Structural evolution of $10\phi\times20$ nanowires during stretching, at three different strain rates for (a) Pt nanowire and (b) Au nanowire.

until maximum stress was attained. The stress rebound indicated that a certain portion of the nanowire was compressed instantaneously, and then relaxed upon further strain. This was attributed to longitudinal strain waves propagating from the strain source into the nanowire. The reason for the effect of wave propagation being observed at this strain rate was due to the high stretch velocities of $310\ \text{m s}^{-1}$ in the $10\phi\times20$ nanowires, and $460\ \text{m s}^{-1}$ in the $15\phi\times30$ nanowires. At such high stretch velocities, the velocity of the fixed atomic planes (the applied strain) was comparable to the resulting strain waves propagating into the nanowire medium. This would result in a Doppler 'red shift' taking place at the strain source. In the Doppler 'red-shift' the shock-wave effect of the applied strain and the propagating strain waves travelling

![](./images/812075881613754368_11.jpg)

![](./images/812075881613754368_12.jpg)

Figure 10. Structural evolution of $15\phi \times 30$ nanowires during stretching, at three different strain rates for (a) Pt nanowire and
(b) Au nanowire.

![](./images/812075881613754368_13.jpg)

Figure 11. Regression analysis for stress-strain response of $10\phi\times20$ nanowires up to $12\%$ strain for (a) Pt nanowire and (b) Au nanowire.

in opposite directions causes interaction between dynamic vibration along the longitudinal axis of the nanowire and the applied axial strain on the nanowire. During the vibration, stress reversals due to the inertial compression of a portion of the nanowire were manifested in the stress-strain response as stress rebounds. This effect was more pronounced and found to occur at approximately regular intervals for the $15\phi\times30$ nanowires, as shown in figure 7. On the other hand, the vibration was damped upon the attainment of maximum stress for the $10\phi\times20$ nanowires.

It was further observed that the $10\phi\times20$ Pt nanowire displayed a dip in the stress-strain response at a strain of about $33\%$, where the nanowire stress dropped to a near zero value, and subsequently recovered to a peak value of $2.36$ GPa at $47\%$ strain. This peculiar phenomenon hinted at an atomic structural rearrangement occurring after the attainment of maximum stress at $12\%$ strain. An investigation into the cross-section of the atomic structure at $50\%$ strain (as shown in figure 9) showed that necking was highly localized within the middle third of the nanowire, with good crystalline order maintained at the end thirds. This indicated some atomic realignment in the undisturbed end thirds from a disordered to an ordered arrangement during straining, as could be seen from the comparison of the cross-sectional diagrams at maximum stress and at $50\%$ strain in figure 9. This observation was absent from the Au nanowire counterpart, where no such stress dips were found; the Au nanowire remained in amorphous disorder during straining, and necking was delocalized at $50\%$ strain. The postulation for this observed phenomenon was that the strain waves would travel a larger distance from the ends into the Pt nanowire, before dissipating at the neck when necking begins to develop at about $12\%$ strain for both Pt and Au nanowires. The reason for strain waves to travel a larger distance in the Pt nanowire before being dissipated was the larger strain wave propagation velocity in Pt, as compared to Au. Following elastic wave analysis, the wave speed of a strain wave ($v_{\text{s}}$) travelling in an elastic medium is

$$
v_{\text{s}}=\sqrt{\frac{E}{\rho}} \tag{7}
$$

where $E$ is the Young's modulus of the medium, and $\rho$ is the density of the medium. In this study, the stress-strain response for the $10\phi\times20$ Pt nanowire displayed a strong linear behaviour before maximum stress was attained, while the Au counterpart showed a non-linear response. Nevertheless, the correlation coefficient of $0.91$ for the Au nanowire was a reasonably good linear fit, and an average $E$ could be obtained for both nanowires from the regression analysis shown in figure 11. From the analysis, it was found that $E$ for the Pt nanowire was $109.90$ GPa, and $53.27$ GPa for the Au nanowire. The average density before nanowire necking for both nanowires was computed to be $23\,620$ and $21\,079$ kg m$^{-3}$ for Pt and Au respectively. The theoretical linear strain wave speed was therefore estimated to be $2157$ and $1590$ m s$^{-1}$ in the $10\phi\times20$ Pt and Au nanowires respectively. The $36\%$ higher wave propagation speed in Pt therefore allowed the strain waves to be propagated deeper into the nanowire before necking commenced at the same time for both Pt and Au nanowires. This accounted for the localized necking effect observed in the Pt nanowire, as the strain waves had travelled all the way into the mid-height of the nanowire before wave dissipation at the neck commenced. On the other hand, the strain waves did not have enough time to travel to the mid-height of the Au nanowire before necking began, and hence were dissipated at a location away from the mid-height of the nanowire. The dissipated energy of the strain waves was converted into kinetic energy for the atoms at the neck, hence inducing further disorder that resulted in structural weakening and further necking of the nanowire. Therefore, due to the different points of strain wave dissipation for Pt and Au nanowires, localized necking was observed for the Pt at the middle third of the nanowire, and a more globalized and homogeneous necking was observed for the Au nanowire.

The stretch velocity of $460$ m s$^{-1}$ for the $15\phi\times30$ nanowires resulted in the formation of multiple necks in the nanowires, instead of a single neck as observed for the other nanowires, as shown in figure 10. Double necking was observed at approximately $15$ and $8$ Å away from the nanowire ends for the Pt and Au nanowires respectively. Some

necking also appeared at the mid-height of the nanowires. An investigation into the stress-strain response of the nanowires showed that there was a cyclical variation of stress as the nanowire was stretched, which resembled a free-vibration response constrained by nanowire stretching. This cyclical stress variation was more pronounced and spaced out in the Au nanowire compared to the Pt nanowire. This was due to the smaller strain wave propagation speed in Au nanowire, which results in a lower propagation frequency and longer strain wavelength due to the more significant 'red-shift' at the strain source. This leads to a lower frequency constrained free-vibration response in the Au nanowire, as shown in figure 7. The double-neck observation was due to the damping out of the strain waves due to the significant 'red-shift' at the strain source, before the waves could be propagated to the mid-height of the nanowires. Strain wave damping could be attributed to the homogeneous imperfections introduced by the amorphous disorder in the nanowire subjected to this strain rate. Due to the lower strain wave speed in the Au nanowire, the strain waves were completely damped at a location nearer to the ends of the nanowire as compared to that in the Pt nanowire. This led to the development of nanowire necks nearer to the ends of the Au nanowire. In the limit, a complete delamination of the fixed atomic planes from the nanowire could be observed at very high strain speeds, where the strain rate approaches the strain wave propagation speed. This is an interesting phenomenon, which would call for a separate investigation into high speed stretching of nanowires. The presence of some necking at the mid-height of the nanowires was due to the transmission of strain waves beyond the 15 and $8\ \mathring{A}$ point from the ends during initial straining, where the double necks would form for the Pt and Au nanowires respectively. The faster strain wave speed in Pt nanowire allowed a more pronounced neck at mid-height to be formed as compared to that in the Au nanowire. Dynamic free-vibration effects also result in a smaller maximum stress attained for the nanowires, which could be seen from the 15% smaller peak stress for the $15\phi\times30$ Pt nanowire, and a 17% smaller peak stress for the $15\phi\times30$ Au nanowire, as compared to their $10\phi\times20$ counterparts. This could be attributed to the dynamic load magnification effect due to the longitudinal vibration, which would lead to overall structural weakening at a smaller stress magnitude.

Finally, the material properties for Pt and Au nanowires were computed and tabulated in table 6. It could be seen that the Young's modulus values for Pt nanowire were between 6.4% to 16.8% smaller than the theoretical bulk value of 168 GPa, while those for the Au nanowire were about 10% smaller than the theoretical bulk value of 78 GPa for the $5\phi\times10$ nanowire. The difference could be attributed mainly to the shortcomings of the simple SC model in predicting the elastic properties. Barring the inadequacy of the SC model, it could be observed that the Young's modulus was smallest for the $5\phi\times10$ nanowires. As the nanowires increase in size, the Young's modulus approaches the theoretical bulk values. The smaller Young's modulus for the $5\phi\times10$ nanowires was due to surface pre-melting that had occurred at 300 K. Surface melting significantly reduced the stiffness of the nanowires as, at this size scale, the nanowires consist of about 67% surface atoms. On the other hand, due to the smaller proportion of surface atoms of 36% and 25% for the $10\phi\times20$ and $15\phi\times$ 30 nanowires respectively, the Young's modulus values were progressively larger. Due to momentum-induced disorder, the Young's modulus was also significantly smaller at the higher strain rates of $4.0\times10^{9}$ and $4.0\times10^{10}\ \text{s}^{-1}$. Non-linear stress-strain response was observed for the $10\phi\times20$ Au nanowire and the $15\phi\times30$ nanowires strained at $4.0\times$ $10^{10}\ \text{s}^{-1}$, due to significant Doppler 'red-shift' at the strain source, resulting in constrained dynamic free-vibration for the nanowire during stretching that led to the observed non-linearity. The nanowires could also be stretched up to 10% strain before first yield occurs, as compared to the 0.14% and 0.28% strain at first yield for bulk Pt and Au respectively. The tensile strength of the nanowires was about 50 times larger than their bulk counterparts. Besides possessing exceptional strength, the nanowires also exhibited superplasticity during low rate straining, whereby a strain in excess of 60% could be achieved before rupture occurs. Such a combination of exceptional material strength and ductility has rarely been seen in bulk materials.

<table>
<caption>Table 6. Mechanical properties of (a) Pt nanowire and (b) Au nanowire.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$\dot{\varepsilon}\ (\text{s}^{-1})$
</td>
<td>
$4.0\times10^{8}$
</td>
<td>
$4.0\times10^{9}$
</td>
<td>
$4.0\times10^{10}$
</td>
</tr>
<tr>
<td>(a)</td>
<td colspan="4">Pt nanowire</td>
</tr>
<tr>
<td rowspan="4">$5\phi\times10$</td>
<td>$E$ (GPa)</td>
<td>139.75</td>
<td>137.27</td>
<td>119.96</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.096</td>
<td>0.108</td>
<td>0.132</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>13.13</td>
<td>14.07</td>
<td>15.77</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.896</td>
<td>$&gt;1.000$</td>
<td>$&gt;1.000$</td>
</tr>
<tr>
<td rowspan="4">$10\phi\times20$</td>
<td>$E$ (GPa)</td>
<td>151.66</td>
<td>149.89</td>
<td>109.90</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.084</td>
<td>0.096</td>
<td>0.120</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>12.35</td>
<td>14.06</td>
<td>14.35</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.732</td>
<td>0.552</td>
<td>$&gt;1.000$</td>
</tr>
<tr>
<td rowspan="4">$15\phi\times30$</td>
<td>$E$ (GPa)</td>
<td>157.31</td>
<td>152.94</td>
<td>NA</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.080</td>
<td>0.096</td>
<td>$0.116^{\text{a}}$</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>12.82</td>
<td>14.50</td>
<td>$12.14^{\text{a}}$</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>$\approx1.000$</td>
<td>0.960</td>
<td>$&gt;1.000$</td>
</tr>
<tr>
<td>(b)</td>
<td colspan="4">Au nanowire</td>
</tr>
<tr>
<td rowspan="4">$5\phi\times10$</td>
<td>$E$ (GPa)</td>
<td>70.36</td>
<td>66.54</td>
<td>55.74</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.080</td>
<td>0.108</td>
<td>0.136</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>5.62</td>
<td>6.88</td>
<td>8.13</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.788</td>
<td>0.836</td>
<td>$&gt;1.000$</td>
</tr>
<tr>
<td rowspan="4">$10\phi\times20$</td>
<td>$E$ (GPa)</td>
<td>79.75</td>
<td>78.73</td>
<td>NA</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.084</td>
<td>0.096</td>
<td>$0.104^{\text{a}}$</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>6.51</td>
<td>7.47</td>
<td>$6.94^{\text{a}}$</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.620</td>
<td>0.680</td>
<td>$&gt;1.000$</td>
</tr>
<tr>
<td rowspan="4">$15\phi\times30$</td>
<td>$E$ (GPa)</td>
<td>81.71</td>
<td>77.78</td>
<td>NA</td>
</tr>
<tr>
<td>$\varepsilon_{\text{fy}}$</td>
<td>0.084</td>
<td>0.100</td>
<td>$0.156^{\text{a}}$</td>
</tr>
<tr>
<td>$\sigma_{\text{fy}}$ (GPa)</td>
<td>6.57</td>
<td>7.35</td>
<td>$5.75^{\text{a}}$</td>
</tr>
<tr>
<td>$\varepsilon_{\text{r}}$</td>
<td>0.760</td>
<td>0.960</td>
<td>$&gt;1.000$</td>
</tr>
</tbody>
</table>

$^{\text{a}}$ Stresses and strains taken at maximum tensile stress.

## 4. Conclusion

This paper presents an MD simulation of Pt and Au nanowires with three characteristics sizes of $5\phi\times10$ (890 atoms), $10\phi\times$ 20 (6660 atoms) and $15\phi\times30$ (24000 atoms). They were subjected to three different strain rates of $4.0\times10^{8}\ \text{s}^{-1}$, $4.0\times10^{9}\ \text{s}^{-1}$ and $4.0\times10^{10}\ \text{s}^{-1}$. At the lowest strain rate of $4.0\times10^{8}\ \text{s}^{-1}$, the nanowires displayed crystalline-ordered deformation governed by the formation of a main dislocation

S J A Koh and H P Lee

plane and the development of sub-planes around the main plane. The crystalline deformation was reflected in the cyclical stress–strain response, where periodic hardening and a sudden stress drop were observed. The higher strain rate of $4.0 \times 10^9$ s⁻¹ indicated the transition strain rate magnitude between crystalline-ordered and amorphous-disordered deformation. This was observed from the 60 meV drop in the cohesive energy per atom in the Pt nanowire, which corresponded to a similar drop of 50 meV during the onset of nanowire melting. The mechanism behind strain rate disordered deformation was determined to be momentum induced. A mixed-mode order–disorder deformation was observed at the strain rate of $4.0 \times 10^9$ s⁻¹, where multiple twinning planes were formed at first yield, encouraged by the weakened atomic structure of the nanowire due to momentum-induced disorder. At the highest strain rate of $4.0 \times 10^{10}$ s⁻¹, dynamic constrained free vibration was observed in the $15\phi \times 30$ nanowires due to the high stretch velocity of $460$ m s⁻¹ at the fixed atomic planes, which was comparable to the estimated strain wave speeds in Pt and Au nanowires. This paper has revealed that, since thermal-induced disorder mainly affects the surface atoms, this effect was predominant in the smallest $5\phi \times 10$ nanowires, which has the largest proportion of surface atoms. On the other hand, momentum-induced disorder played an important role in the overall phase transformation of the nanowire from crystalline to amorphous during strain deformation. Finally, the effect of strain wave propagation in the nanowire was significant at $4.0 \times 10^{10}$ s⁻¹, which led to a radically different stress–strain response of the nanowire that consists of periodic stress rebounds, with the formation of multiple necks. The insights from this computational simulation presented an unexplored field for metallic nanowires, doubly strained dynamically at high strain rates. The advent of laser-induced shock—produced from high-powered laser facilities [71]—coupled and applied on AFM tip retraction experiments [32] enable strain rates of up to and above $10^{10}$ s⁻¹ to be produced [72]. This presented an opportunity for the reported phenomena in this work to be observed and verified experimentally. The phenomenon of momentum-induced disorder and strain wave propagation during high-speed amorphous deformation are topics of great interest, which could be further pursued in subsequent simulation works.

## Acknowledgments
This work was funded by the Agency for Science, Research and Technology (A*STAR), Science and Engineering Research Council (SERC). Molecular images were made with VMD, which is owned by the Theoretical and Computational Biophysics Group; an NIH Resource for Macromolecular Modeling and Bioinformatics, at the Beckman Institute, University of Illinois at Urbana-Champaign. The DL_POLY_2 code for the MD simulation was developed by W Smith and T R Forester at CCLRC, Daresbury Laboratory, Warrington, UK.

## References
[1] Moore G E 1965 *Electronics* **38** 114
[2] Rodrigues V and Ugarte D 2001 *Phys. Rev. B* **63** 073405
[3] Semiconductor Industry Association 2005 *International Technology Roadmap for Semiconductors* http://www.itrs.net/Common/2005ITRS/Home2005.htm
[4] Kondo Y and Takayanagi K 2000 *Science* **289** 606
[5] Glavin B A 2001 *Phys. Rev. Lett.* **86** 4318
[6] Iijima S, Qin L C, Hong B H, Bae S C, Youn S J and Kim K S 2002 *Science* **296** 611
[7] Melosh N A, Boukai A, Diana F, Gerardot B, Badolato A, Petroff P M and Heath J R 2003 *Science* **300** 112
[8] Husain A, Hone J, Postma H W C, Huang X M H, Drake T, Barbic M, Scherer A and Roukes M L 2003 *Appl. Phys. Lett.* **83** 1240
[9] Postma H W C, Kozinsky I, Husain A and Roukes M L 2005 *Appl. Phys. Lett.* **86** 223105
[10] Bauer L A, Birenbaum N S and Meyer G J 2004 *J. Mater. Chem.* **14** 517
[11] Dubois S, Piraux L, George J M, Ounadjela K, Duvail J L and Fert A 1999 *Phys. Rev. B* **60** 477
[12] Mehrez H, Wlasenko A, Larade B, Taylor J, Grütter P and Guo H 2002 *Phys. Rev. B* **65** 195419
[13] Picaud F, Pouthier V, Girardet C and Tosatti E 2003 *Surf. Sci.* **547** 249
[14] Çağin T, Dereli G, Uludoğan and Tomak M 1999 *Phys. Rev. B* **59** 3468
[15] Kang J W and Hwang H J 2002 *J. Korean Phys. Soc.* **40** 946
[16] Miao L, Bhethanabotla V R and Joseph B 2005 *Phys. Rev. B* **72** 134109
[17] Finbow G M, Lynden-Bell R M and McDonald I R 1997 *Mol. Phys.* **92** 705
[18] Mehrez H and Ciracı S 1997 *Phys. Rev. B* **56** 12632
[19] Ikeda H, Qi Y, Çağin T, Samwer K, Johnson W L and Goddard W A III 1999 *Phys. Rev. Lett.* **82** 2900
[20] Branício P S and Rino J 2000 *Phys. Rev. B* **62** 16950
[21] Kang J W and Hwang H J 2000 *J. Korean Phys. Soc.* **38** 695
[22] da Silva E Z, da Silva A J R and Fazzio A 2001 *Phys. Rev. Lett.* **87** 256102
[23] Liang W and Zhou M 2003 *Proc. Inst. Mech. Eng.* **218** 599
[24] da Silva E Z, da Silva A J R and Fazzio A 2004 *Comput. Mater. Sci.* **30** 73
[25] Park H S and Zimmerman J A 2005 *Phys. Rev. B* **72** 054106
[26] Wang B L, Zhao J J, Shi D N, Jia J M and Wang G H 2005 *Chin. Phys. Lett.* **22** 1195
[27] Reich D H, Tanase M, Hultgren A, Bauer L A, Chen C S and Meyer G J 2003 *J. Appl. Phys.* **93** 7275
[28] Alexandrov A S and Kabanov V V 2005 *Phys. Rev. Lett.* **95** 076601
[29] Mock J J, Oldenburg S J, Smith D R, Schultz D A and Schultz S 2002 *Nano Lett.* **2** 465
[30] Christ A, Zentgraf T, Kuhl J, Tikhodeev S G, Gippius N A and Giessen H 2004 *Phys. Rev. B* **70** 125113
[31] Ohnishi H, Kondo Y and Takayanagi K 1998 *Nature* **395** 780
[32] Landman U, Luedtke W D, Burnham N A and Colton R J 1990 *Science* **248** 454
[33] Rubio G, Agraït N and Vieira S 1996 *Phys. Rev. Lett.* **76** 2302
[34] Marszalek P E, Greenleaf W J, Li H B, Oberhauser A F and Fernandez J M 2000 *Proc. Natl Acad. Sci.* **97** 6282
[35] Lu L, Li S X and Lu K 2001 *Scr. Mater.* **45** 1163
[36] Wang Z L 2004 *Dekker Encyclopedia of Nanoscience and Nanotechnology* (New York: Dekker) p 1773
[37] Gülseren O, Ercolessi F and Tosatti E 1995 *Phys. Rev. B* **51** 7377
[38] Oshima Y, Koizumi H, Mouri K, Hirayama H and Takayanagi K 2002 *Phys. Rev. B* **65** 121401(R)
[39] Oshima Y and Onga A 2003 *Phys. Rev. Lett.* **91** 205503
[40] Wang B L, Yin S Y, Wang G H, Buldum A and Zhao J J 2001 *Phys. Rev. Lett.* **86** 2046
[41] Zhang H Y, Gu X, Zhang X H, Ye X and Gong X G 2004 *Phys. Lett. A* **331** 332
[42] Kang J W and Hwang H J 2001 *Nanotechnology* **12** 295
[43] Wang J L, Chen X S, Wang G H, Wang B L, Lu W and Zhao J J 2002 *Phys. Rev. B* **66** 085408

Simulation of mechanical response of metallic nanowires (size and strain rate effects)

[44] Wang B L, Wang G H, Chen X S and Zhao J J 2003 *Phys. Rev.* **B 67** 193403

[45] Ju S P, Lin J S and Lee W J 2004 *Nanotechnology* **15** 1221

[46] Bürki J, Goldstein R E and Stafford C A 2003 *Phys. Rev. Lett.* **91** 254501

[47] Novaes F D, da Silva E Z, da Silva A J R and Fazzio A 2004 *Surf. Sci.* **566** 367

[48] Diao J K, Gall K and Dunn M L 2003 *Nat. Mater.* **2** 656

[49] Gülseren O, Ercolessi F and Tosatti E 1995 *Phys. Rev. B* **51** 7377

[50] Kassubek F, Stafford C A, Grabert H and Goldstein R E 2001 *Nonlinearity* **14** 167

[51] Sato F, Moreira A S, Coura P Z, Dantas S O, Legoas S B, Ugarte D and Galvão D S 2005 *Appl. Phys. A* **81** 1527

[52] Koh S J A, Lee H P, Lu C and Cheng Q H 2005 *Phys. Rev. B* **72** 085414

[53] Haile J M 1997 *Molecular Dynamics Simulation* (Singapore: Wiley) chapter 5

[54] Ercolessi F, Parinello M and Tosatti E 1988 *Phil. Mag. A* **58** 213

[55] Rosato V, Guillope M and Legrand B 1989 *Phil. Mag. A* **59** 321

[56] Krüger J K *et al* 2005 *J. Physique IV* **129** 45

[57] Ladd A J C and Woodcock L V 1978 *Mol. Phys.* **36** 611

[58] Nørskov J K 1982 *Phys. Rev. B* **26** 2875

[59] Daw M S and Baskes M I 1984 *Phys. Rev. B* **29** 6443

[60] Finnis M W and Sinclair J F 1984 *Phil. Mag. A* **50** 45

[61] Sutton A P and Chen J 1990 *Phil. Mag. Lett.* **61** 139

[62] Kimura Y, Qi Y, Çağin T and Goddard W A III 1998 unpublished

[63] Rafii-Tabar H and Sutton A P 1991 *Phil. Mag. Lett.* **63** 217

[64] Nosé S 1984 *J. Chem. Phys.* **81** 511
Hoover W G 1985 *Phys. Rev. A* **31** 1695

[65] Horstmeyer M F, Baskes M I and Plimpton S J 2001 *Acta Mater.* **49** 4363

[66] Smith W, Yong C W and Rodger P M 2002 *Mol. Sim.* **28** 385

[67] Smith W 1991 *Comput. Phys. Commun.* **62** 229

[68] Caddigan E, Cohen J, Gullingsrud J and Stone J 2003 *VMD User's Guide* (Urbana, IL: University of Illinois and Beckman Institute) http://www.ks.uiuc.edu/

[69] Ezekiel M and Fox K A 1959 *Methods of Correlation and Regression Analysis, Linear and Curvilinear* (New York: Wiley)
Mari D D and Kotz S 2001 *Correlation and Dependence* (River Edge, NJ: Imperial College Press)

[70] Wen Y H, Zhu Z Z, Shao G F and Zhu R Z 2005 *Physica E* **27** 113

[71] Kalantar D H *et al* 2000 *Phys. Plasmas* **7** 1999

[72] Bringa E M *et al* 2004 *J. Appl. Phys.* **96** 3793

3467