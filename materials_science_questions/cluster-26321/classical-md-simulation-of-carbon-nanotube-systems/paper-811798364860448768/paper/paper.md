![](./images/811798364860448768_1.jpg)

Copyright © 2010 American Scientific Publishers
All rights reserved
Printed in the United States of America

Journal of
Computational and Theoretical Nanoscience
Vol. 7, 379-387, 2010

# Confined Liquid Flow in Nanotube: A Numerical Study and Implications for Energy Absorption

Jianbing Zhao¹, Yu Qiao²,³, Patricia J. Culligan¹, and Xi Chen¹,⁴,⁵, *

¹School of Engineering and Applied Sciences, Columbia University, New York, NY 10027, USA
²Department of Structural Engineering, University of California – San Diego, La Jolla, CA 92093-0085, USA
³Program of Materials Science and Engineering, University of California – San Diego, La Jolla, CA 92093, USA
⁴Department of Earth and Environmental Engineering, Columbia University, New York, NY 10027, USA
⁵Department of Civil and Environmental Engineering, Hanyang University, Seoul, 133-791, Korea

Understanding nanofluidic behavior is of fundamental value to the development of many potential nano-technology applications, including high-performance energy absorption. We carry out non-equilibrium molecular dynamics (NEMD) simulations to study the transport characteristics of liquids in a confined nano-environment. It is shown that the distributed electric field arising from either an electrolyte water solution (due to the dissolved ions) or a partially charged solid surface, could lead to nanofluidic properties that are significantly different to those associated with pure water or a neutral nanotube. In addition, the nanopore size and the transport rate are shown to be important factors that strongly influence the flow process. The nominal viscosity and the shearing stress between the nanofluid and tube wall, which characterize the ease for nanofluid transport under an external driving force, are found to be dependent on the liquid phase and solid phase properties, as well as liquid flow rate and nanotube size. By varying properties of liquid phase and solid phase, liquid flow rate and nanotube size, the energy absorption characteristics of nanofluidic devices might be adjusted.

**Keywords:** Nanofluid, Transport, Numerical Simulation.

## 1. INTRODUCTION

With nanostructures, including nanotubes and nanoporous materials, being used as the next-generation sensors, filters, actuators, reactors, and transporters, increasing attention is focused on the flow and transport behaviors of gas and liquid inside such a confined nanoenvironment. For example, extensive studies have been carried out on water transport in nanotubes, owing to its potential significance to engineering the selective transportation of water, proton, ions and macromolecules, which are ubiquitous in biology, chemistry and pharmaceutical industries.¹⁻⁴ Recently, high performance nanoporous energy absorption systems (NEASs) has been proposed,⁵,⁶ based on the following concept: when a water or water-based solution is forced to infiltrate and fill hydrophobic nanopores, the external mechanical energy is dissipated via the extensive solid–liquid interface energy and “frictional” force with the system. Due to the ultrahigh surface-to-volume ratio of the nanoporous solid, the energy absorption efficiency of NEAS can be orders of magnitude higher than conventional energy absorption materials and structures. In order to fulfill the promise of these new nanodevices, it is important to understand the intrinsic behavior of confined liquid flow in a model nanotube, which may in turn to assist the design and optimization of the performance of NEAS and other nanofluidic devices.

Among various nanofluidic studies, water conduction through a carbon nanotube (CNT) represents one of the most fundamental studies. Majumder et al. reported that the flow rate of water in a 7-nm diameter CNT is four to five orders of magnitude faster than that predicted by the conventional fluid flow theory.⁷ For water flowing through a membrane consisting of CNTs of 2 nm diameter, Holt et al.⁸ found that the flow rate exceeded the predictions of the Knudsen diffusion model by more than one order of magnitude, and it exceeded the prediction of a continuum hydrodynamics model by more than three orders of magnitude. Due to the tremendous challenges encountered in experimental studies at the nanoscale, molecular dynamic (MD) simulation is a convenient tool for understanding the unique characteristics of nanoscale fluid flow.⁹ Hummer et al. showed that the flow rate of water inside a hydrophobic CNT was indeed orders of magnitude

*Author to whom correspondence should be addressed.

J. Comput. Theor. Nanosci. 2010, Vol. 7, No. 2
1546-1955/2010/7/379/009
doi:10.1166/jctn.2010.1369

higher than classical macroscale flow rate, $^{10,11}$ and similar findings were reported by Skoulidas et al. on light gas transport. $^{4}$ Hanasaki and Nakatani $^{12}$ simulated water transport in CNTs with diameters from (6, 6) to (60, 60) and identified plug-like velocity profile of water flow with very high transport speed; the reported results were consistent with another MD investigation in Ref. [13]. The unusual high-speed transport of water may be related to the fact that the structure of the confined water molecules is distinct from their bulk counterpart. $^{14-17}$

These numerical studies, however, were mostly limited to spontaneous water transport through CNTs. In view of the potential applications of the nanofluidic devices, it is of fundamental value to understand the various factors $^{18}$ that may govern the characteristics of the confined nanofluid behaviors under external loads, which might, in turn, enable better control of nanofluidic devices. For example, in order to absorb more energy in NEAS, it is desirable to increase the resistance to liquid flow in a solid nanotube. Therefore, one could improve the energy absorption performance by varying several important material and system parameters, such as the nanopore size, liquid flow rate, liquid constituents, and solid phase properties. It has been shown experimentally, that the energy absorption characteristics of different nanoporous solids (e.g., silica, zeolite, carbon) are different, $^{19-21}$ and that energy absorption is also highly dependent on the treatment of nanoporous surfaces, $^{18,22}$ as well as nanopore sizes. $^{23,24}$ By adding different chemical admixtures with varying concentrations $^{21,25}$ or introducing gas phases, $^{24}$ the energy absorption efficiency can be adjusted over wide ranges. Moreover, the NEAS performance is also likely to be affected by the mechanical loading rate, $^{26,27}$ as well as being sensitive to applied charges (electrical field) $^{28,29}$ and thermal fields (temperature variations); $^{21,28}$ thus, external perturbation such as applied loading rate and electrical and thermal fields might also be employed to tailor NEAS's performance. In order to guide the development of high-performance NEAS, it is critical to understand why and how some of these factors affect fundamental nanofluidic behaviors.

This paper uses nonequilibrium molecular dynamics (NEMD) simulations to address the issue by exploring the roles of fluid and solid phase properties, as well as flow rate and nanotube size, on nanofluidic behaviors. Results from the simulations provide useful insight into enhancing the enhancing the energy absorption performances of NEASs.

## 2. MODEL AND METHODS
### 2.1. Variation of Liquids Phase
For the water molecules, the extended simple point charge (SPC/E) model was adopted and the interatomic potential was described as: $^{30}$

$$
\begin{aligned}
E_{\text {total }}= & k_{2}^{b}\left(b-b_{0}\right)^{2}+k_{2}^{\theta}\left(\theta-\theta_{0}\right)^{2}+\sum_{i, j} \frac{q_{i} q_{j}}{4 \pi \varepsilon_{0} \sigma_{i j}} \\
& +\sum_{i, j} \varepsilon_{i j}\left[2\left(\frac{\sigma_{i j}^{0}}{\sigma_{i j}}\right)^{9}-3\left(\frac{\sigma_{i j}^{0}}{\sigma_{i j}}\right)^{6}\right]
\end{aligned} \tag{1}
$$

The first term on the right hand side of Eq. (1) is a Morse potential to describe the interatomic bonding. The second term is a valence angle potential specifying the angle deflections between two O–H bonds of the water molecule. The third term is Columbic potential, the derivative of which is the electrostatic interaction among the electropholar water molecules or between the water molecules and a partially charged tube wall. The final term is the Lennard-Jones potential that accounts for steric and van der Waals (vdW) interactions. The cutoff distance of vdW interaction and the real-space part of the Coulomb interactions were set to be $10$ Å; and, to handle the long range Coulomb interactions, the particle–particle particle–mesh technique (PPPM) $^{31}$ was adopted with a root mean square accuracy of $10^{-4}$. The force constants and geometric parameters used are listed in Table I.

Electrolytes are often used to adjust NEAS performance. $^{18}$ To explore the influence of the distributed ionic charges on the transport behavior of the liquid phase, flows of sodium chloride water solution in a neutral nanotube were compared to that of pure water. The interionic potential used for this comparison is of the Huggins-Mayer form $^{32}$

$$
E_{i j}(r)=\frac{q_{i} q_{j}}{r}+B_{i j} e^{-r / \rho_{i j}}-\frac{C_{i j}}{r^{6}} \tag{2}
$$

where $q_{i}$ is the charge of the $i$th ion. The ion-solvent potential was described with Lennard-Jones 9-6 form. The values of the above potential parameters are listed in Table II. The concentration of NaCl was varied over a wide range.

### 2.2. Variation of Solid Phase
CNT has been widely employed as a model nanochannel in nanofluidic studies. In this paper, a rigid and defect-free (18, 18) single-walled CNT was employed as an example

<table>
<caption>Table I. Parameters for SPC/E water model and SiO₂ nanotube.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon_{OO}$</td>
<td>0.2848 Kcal/mole</td>
<td>$\varepsilon_{OO^{a}}$</td>
<td>0.2139 Kcal/mole</td>
</tr>
<tr>
<td>$\sigma_{OO}^{0}$</td>
<td>3.6001 Angstrom</td>
<td>$\sigma_{OO^{a}}^{0}$</td>
<td>3.6020 Angstrom</td>
</tr>
<tr>
<td>$\varepsilon_{OC}$</td>
<td>0.1157 Kcal/mole</td>
<td>$\varepsilon_{OSi}$</td>
<td>0.1894 Kcal/mole</td>
</tr>
<tr>
<td>$\sigma_{OC}^{0}$</td>
<td>3.8351 Angstrom</td>
<td>$\sigma_{OSi}^{0}$</td>
<td>4.1332 Angstrom</td>
</tr>
<tr>
<td>$q_{O}$</td>
<td>−0.82 e</td>
<td>$q_{O^{a}}$</td>
<td>−0.445 e</td>
</tr>
<tr>
<td>$q_{H}$</td>
<td>0.41 e</td>
<td>$q_{Si}$</td>
<td>0.890 e</td>
</tr>
<tr>
<td>$k_{2}^{b}$</td>
<td>450.0 Kcal/mole</td>
<td>$k_{2}^{\theta}$</td>
<td>55.0 Kcal/mole</td>
</tr>
<tr>
<td>$b_{0}$</td>
<td>0.9572 Angstrom</td>
<td>$\theta_{0}$</td>
<td>109.47°</td>
</tr>
</tbody>
</table>

$^{a}$Stands for the oxygen atoms in SiO₂ nanotube.

<table>
<caption>Table II. Parameters for solute–solvent potential.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon_{\text{ONa}^+}$</td>
<td>0.4324 Kcal/mole</td>
<td>$\varepsilon_{\text{O}^\text{*}\text{Na}^+}$</td>
<td>0.3367 Kcal/mole</td>
</tr>
<tr>
<td>$\sigma_{\text{ONa}^+}^0$</td>
<td>3.8057 Angstrom</td>
<td>$\sigma_{\text{O}^\text{*}\text{Na}^+}^0$</td>
<td>3.8011 Angstrom</td>
</tr>
<tr>
<td>$\varepsilon_{\text{OCl}^-}$</td>
<td>0.2806 Kcal/mole</td>
<td>$\varepsilon_{\text{O}^\text{*}\text{Cl}^-}$</td>
<td>0.2185 Kcal/mole</td>
</tr>
<tr>
<td>$\sigma_{\text{OCl}^-}^0$</td>
<td>3.7770 Angstrom</td>
<td>$\sigma_{\text{O}^\text{*}\text{Cl}^-}^0$</td>
<td>3.7722 Angstrom</td>
</tr>
<tr>
<td>$q_{\text{Na}^+}$</td>
<td>+1.0 e</td>
<td>$\varepsilon_{\text{SiNa}^+}$</td>
<td>0.3529 Kcal/mole</td>
</tr>
<tr>
<td>$q_{\text{Cl}^-}$</td>
<td>−1.0 e</td>
<td>$\sigma_{\text{SiNa}^+}^0$</td>
<td>4.2409 Angstrom</td>
</tr>
<tr>
<td>$B_{\text{Na}^+\text{Na}^+}$</td>
<td>9769.55 Kcal/mole</td>
<td>$\varepsilon_{\text{SiCl}^-}$</td>
<td>0.2239 Kcal/mole</td>
</tr>
<tr>
<td>$\rho_{\text{Na}^+\text{Na}^+}$</td>
<td>0.31700 Angstrom</td>
<td>$\sigma_{\text{SiCl}^-}^0$</td>
<td>4.2243 Angstrom</td>
</tr>
<tr>
<td>$C_{\text{Na}^+\text{Na}^+}$</td>
<td>24.172 Kcal/mole-Å⁶</td>
<td>$B_{\text{Na}^+\text{Cl}^-}$</td>
<td>28920.2 Kcal/mole</td>
</tr>
<tr>
<td>$B_{\text{Cl}^-\text{Cl}^-}$</td>
<td>80285.8 Kcal/mole</td>
<td>$\rho_{\text{Na}^+\text{Cl}^-}$</td>
<td>0.31700 Angstrom</td>
</tr>
<tr>
<td>$\rho_{\text{Cl}^-\text{Cl}^-}$</td>
<td>0.31700 Angstrom</td>
<td>$C_{\text{Na}^+\text{Cl}^-}$</td>
<td>161.15 Kcal/mole-Å⁶</td>
</tr>
<tr>
<td>$C_{\text{Cl}^-\text{Cl}^-}$</td>
<td>1683.4 Kcal/mole-Å⁶</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

of a neutral nanopore. The diameter of the CNT was $D = 24.41$ Å and the length is $L = 60$ Å. A periodical boundary condition was applied in the axial direction, (i.e., the flow direction, Fig. 1). Since $L$ was much larger than the cutoff distance of the Lennard-Jones potential in the SPC/E water model, the length of the computational cell had been verified to have essentially no effect on simulated continuous flow properties.

As mentioned above, liquid transport could be strongly affected by the polarity of molecules, such as water and distributed ions. Likewise, the presence of surface charges on a nanopore solid might also significantly influence the solid–liquid interactions. Since nanoporous silica is widely employed in NEAS,¹⁸·²¹·³³ a rigid and straight SiO₂ nanotube was employed as the model of the partially charged nanotube. The corresponding parameters involved in the forcefield are listed in Table II. The diameter of the SiO₂ nanotube was chosen to be 2.51 nm so as to best match the size of MCM41 silica (with mean pore size $\sim$2.6 nm²²) used in previous experiments; the size of the SiO₂ tube was also close to that of the CNT, allowing us to compare the effect of solid phase properties.

![](./images/811798364860448768_2.jpg)

Fig. 1. A snapshot of the configuration of water molecules and Na⁺, Cl⁻ ions confined in a model neutral (18, 18) carbon nanotube (CNT). Periodic boundary condition is applied in the z-direction. The red-white ribbons stand for water molecules; the blue balls stand for sodium ions; the ochre balls stand for chloride ions and the gray bonds stand for CNT structure.

### 2.3. Size and Rate Effects
Due to different levels of confinement, the resistance force imposed by the solid wall to liquid molecules varies with the tube size and flow rate. In order to explore the size and rate effects of the shearing stress and nominal viscosity, we vary the CNT size from (10, 10) ($D = 1.36$ nm) to (60, 60) ($D = 8.13$ nm), and vary the liquid flow rate from $\sim$80 m/s to $\sim$700 m/s. Appropriate lateral sizes of computational cells were established to encapsulate the water filled nanotubes.

### 2.4. Simulation Procedure
The length of the simulation cell was 60 Å, and its lateral dimension was dependent on the diameter of the tube. Numerical tests were carried out to ensure that the simulation results did not depend on the cell dimensions. The number of water molecules inside the nanotube, $N$, was chosen such that the initial water density inside the CNT was set to be 998 kg/m³. When NaCl solution was simulated, certain water molecules are replaced by Na⁺ or Cl⁻ ions to reach a desired concentration of NaCl solution, as shown in Figure 1.

As mentioned above, a periodical boundary condition was applied in the axial direction to mimic continuous liquid flow in an infinitely long channel. The simulations were performed using LAMMPS³⁴·³⁵ with a time step 1 fs. During simulation, the temperature was maintained at 298.5 K by using a Nose/Hoover thermostat with a time constant of 0.1 ps.ᵃ

After initialization, a NVT simulation was first performed for 100 ps to minimize the system energy. When fully relaxed, an external “gravity” force with magnitude $m_i \tilde{g}$ (where $m_i$ is the mass of the $i$th particle) was applied on each molecule in the axial direction of the tube to drive the flow (Fig. 1). When the average transport rate of the liquid molecules (i.e., the flow rate, see below) reached a desired value, the applied force was removed and the liquid decelerated freely. By computing the initial deceleration $\bar{a}$, the shearing stress at the liquid–solid interface can be obtained as $\tau = \sum m_i \cdot \bar{a}/\pi D L$, where $\sum m_i$ is the summation of the liquid mass in the nanotube, including water and electrolyte ions. $\tau$ is a function of the flow rate and tube size, as well as the liquid and solid phases.

To obtain the averaged flow properties, the inner space of nanotube was evenly divided into a set of concentric

ᵃTo avoid artificial heating caused by the imposed axial displacements of the liquid molecules during simulation, the mean axial velocity of the liquid mass center was subtracted from the axial component of the velocity of each liquid molecule during the calculation of temperature.

annular volumes. In each annular region, the flowing properties of all liquid molecules were averaged to obtain the radial distribution of flowing parameters. Taking the radial distributions of density and axial velocity for example:

$$
\rho(r)=\frac{\sum_{j=J_{N}}^{J_{M}} \sum_{i=1}^{N} m_{i} H_{n}\left(r_{i, j}\right)}{\Delta V_{N}\left(J_{M}-J_{N}+1\right)} \tag{3}
$$

$$
u_{z}(r)=\frac{\sum_{j=J_{N}}^{J_{M}} \sum_{i=1}^{N} H_{n}\left(r_{i, j}\right) u_{i, j}^{z}}{\left(J_{M}-J_{N}+1\right)} \tag{4}
$$

where
$$
H_{n}\left(r_{i, j}\right)=
\begin{cases}
1 & \text{if } (n-1)\Delta r < r_i < n\Delta r \\
0 & \text{else}
\end{cases}
$$
$r_{i}$ is the radial coordinate of the $i$th molecule, $\Delta r$ is the radial thickness of each annular space, $\Delta V_{N}$ is the volume of the $N$th annular space, and $J_{N}$ and $J_{M}$ are the beginning and ending time step used for averaging. $^{36}$ When the axial velocities of all molecules are averaged, the flow rate is obtained.

Although the flow inside the nanotube is not classical, we define a nominal viscosity $\tilde{\eta}$ to effectively characterize the flow property resulting from solid-liquid interaction. Based on continuum fluid theory, the averaged flow velocity (rate) in a pipe (with radius $R$ and length $L$) is $\bar{v}=Q / A=R^{2} \Delta P /(8 \eta L)$, where $Q$ is the volumetric flow, $\Delta P / L$ is the pressure gradient along the flow direction, and $\eta$ is the viscosity. Thus, one can obtain the nominal (apparent) viscosity as $\tilde{\eta}=\tau R /(4 \bar{v})$ by using the equilibrium condition $\tau=\Delta P R /(2 L)$. Although this equation is based on continuum theory, it can be extended to complex flow $^{37,38}$ to obtain the nominal viscosity at the nanoscale (for the purpose of self-comparison, although the most intrinsic nanofluidic characteristic is still the shearing stress as discussed above). Such nominal viscosity was also commonly used in the study of mud and drilling fluid to void complicated formulation of viscosity.

## 3. RESULTS AND DISCUSSION
### 3.1. Effects of Liquid and Solid Phases
#### 3.1.1. Variation of Electrolyte Concentration in Liquid

NaCl/water solution flows with molarities of 3.0 M, 2.0 M, 1.0 M and 0.5 M ($1\ \text{M}=1\ \text{mole/L}$) were studied to represent the effect of variation of liquid phase properties (in particular the ion density of the electrolyte). The flow rate was chosen to be 216 m/s for all cases in this section. Figure 2 shows the profiles of radial density and axial velocity distributions in a neutral (18, 18) CNT. Despite the variation of NaCl concentration, the nanofluid profile always shows a plug-like characteristic, which agrees with the results of several previous studies. $^{12,13}$

![](./images/811798364860448768_3.jpg)

Fig. 2. Axial velocity profiles of NaCl/water flows with different molarities of NaCl in a neutral (18, 18) CNT. $1\ \text{M}=1\ \text{mol/L}$. The radial distance is measured from the center axis of the tube.

From the radial density distributions on Figure 3, the first solvation layer (shell) reaches the maximum density at a distance that equals to the equilibrium distance $d^{B}$ (between the O atom in $\text{H}_2\text{O}$ and C atom in the solid wall). The magnitude of the density gradually converges to that of bulk water when the distance from the tube wall is more than three times of $d^{B}$.

The position of the first solvation shell on Figure 3 is correlated with the concentration of NaCl: the higher the concentration, the further the first solvation shell from the nanotube wall, and the higher the density. In essence, the dissolved $\text{Na}^{+}$and $\text{Cl}^{-}$ions intensify the electrical interactions with the polar water molecules. The $\text{Na}^{+}$and $\text{Cl}^{-}$ions could agglomerate water molecules around them, so as to make the flow inside the CNT more

![](./images/811798364860448768_4.jpg)

Fig. 3. Comparisons of the radial density distributions and the position of the first solvation shell inside a (18, 18) CNT for NaCl/water flows with different molarities ($1\ \text{M}=1\ \text{mol/L}$). The radial distance is measured from the center axis of the tube.

![](./images/811798364860448768_5.jpg)

Fig. 4. Variations of the shearing stress and apparent (nominal) viscos- ity as functions of molarity of NaCl/water flow in a neutral (18, 18) CNT at the transport rate of 216 m/s.

coherent. Since there is no electrostatic attraction from the neutral CNT wall, the first solvation shell is attracted away from the wall when the NaCl concentration is higher, and the magnitude of the density of the first solvation layer is also increased due to the reduced volume occupied by the water molecules.

The vdW repulsive force from the nanotube wall, dic- tated by the power-9 term in Eq. (1), is sensitive to the change of the equilibrium distance $d^{B}$—such a repulsive force is also directly related to the shearing stress (resistance) encountered by the water flow in nanoenvironment. In light of this fact, we compare the shearing stress encountered by the NaCl/water solution with various concentrations. In Figure 4, as the concentration of NaCl increases from 0.0 M to 3.0 M, the shearing stress is found to nonlinearly decrease from 1.8 MPa to 0.6 MPa. This trend echoes the position of the first solvation shell in Figure 3, which confirms that the larger the $d^{B}$, the weaker the repulsive force and the smaller the shearing stress. Consequently, according to $\tilde{\eta}=\tau R /(4 \bar{v})$, the apparent viscosity shows a similar decreasing trend with the NaCl concentration, with a magnitude that is much smaller than $2.0 \times 10^{-3}$ centipoises, which are almost three orders of magnitude lower than that of bulk water (about 1.0 cp).

### 3.1.2. Variation of Solid Phase

The transport behavior of pure water in a neutral CNT was compared with that in a partially charged $SiO_{2}$ nanotube of almost the same radius, as presented in Figure 5 for the distribution of water molecules. Figures 6(a) and (b) show the axial velocity and radial density of the flow of polar water molecules in these two tubes, respectively, at a flow rate of 116 m/s. The axial velocity and radial density profiles in the $SiO_{2}$ nanotube share common features with those in the neutral CNT, such as the plug-like velocity profile (Fig. 6(a)) and the undulating distribution of radial density. The difference appears at the position of the first solvation shell: in the $SiO_{2}$ nanotube, the first solvation shell is closer to the tube wall, which suggests that the $SiO_{2}$ nanotube surface is more hydrophilic to water.

Again, the short-range repulsive force, the power-9 term in Eq. (1), decays fast with the increase of the intermolecular distance, as well as the electrostatic interaction. The shorter $d^{B}$ results in a significant increase of the repulsive force and resistance to the water flow in the $SiO_{2}$ tube. Such a statement can be verified from the shearing stress trend in Figure 7, where the shearing stress of the $SiO_{2}$ nanotube under different water transport rates is almost two orders of magnitude higher than that in the neutral CNT with comparable flow rates (e.g., Fig. 4).

In addition, the rate dependency of shearing stress is also revealed. As shown in Figure 6, the shearing stress in $SiO_{2}$ nanotube drops by over 70%

![](./images/811798364860448768_6.jpg)

Fig. 5. A snapshot of water molecules configurations in a (18, 18) carbon nanotube (CNT, Left) and a $SiO_{2}$ nanotube (Right).

![](./images/811798364860448768_7.jpg)

![](./images/811798364860448768_8.jpg)

Fig. 6. (a) Axial velocity and (b) radial density profiles of water as functions of the radius coordinate, in (18, 18) CNT and SiO₂ nanotube with identical diameter, respectively. The thick dash lines in (a) depicts the outline of the average axial velocity profile.

(from $\sim$780 MPa to $\sim$230 MPa) with the transport rate increasing from 180 m/s to 820 m/s. And such trend could be approximately fitted by a power-law curve, $\tau \propto \bar{v}^{m}$, where the value of $m$ is found to be 0.61 in this case. The nominal (apparent) viscosity thus calculated also decreases nonlinearly from 0.45 cp to 0.26 cp, which is not far away from the bulk water viscosity. Further discussion of the rate effect will be given in Section 3.2.

### 3.2. Implications and Discussion
The presence of external charges, e.g., the higher concentrations of $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$ions in $\mathrm{NaCl} /$ water solution, as well as the $\mathrm{O}^{2-}$ and $\mathrm{Si}^{4+}$ sites on the partially charged $\mathrm{SiO}_{2}$ nanotube wall, significantly increase the intermolecular potential through electrostatic interactions. As a result of minimizing the system energy, the polar water molecules in an electrolyte solution move to their new favorable equilibrium positions. In the neutral CNT the new equilibrium position is further away from the tube wall, and for the $\mathrm{SiO}_{2}$ tube, the water molecules prefer to stay closer to the wall. The different levels of solid-liquid interaction result in different transport behaviors.

![](./images/811798364860448768_9.jpg)

Fig. 7. Variations of the shearing stress and apparent viscosity of water flow in a $24.4 \AA \mathrm{SiO}_{2}$ nanotube, as the transport rate varies.

From the application point of view, the higher the resistance during liquid transport the greater the potential the NEAS. $^{b}$ With higher concentration of ions, the shearing stress is reduced and such a system is inferior in dissipating energy, but could be better conductors. Although common sense suggests that the viscosity of a higher concentration electrolyte solution should be elevated, the nanoscale phenomena reported here, which showed the opposite trend, were observed in infiltration tests of Qiao et al. $^{21,39}$-in that the slope of sorption isotherm curve after infiltration started became flatter with increased electrolyte concentration, which indicated smaller resistance to flow in a nanopore. On the other hand, the partially charged solid tube turns out to be more hydrophilic to water due to electrostatic attraction, which greatly increases the liquid-solid interaction (in comparison with a neutral tube). Therefore, to make high efficiency energy absorption systems using the "friction" between liquid molecules and solid nanopore, it is desirable to employ a charged/polarized nanopore surface and pure water without the addition of ions. $^{c}$

$^{b}$We caution that the overall energy absorption density depends on both the initial infiltration threshold and the slope of infiltration (transportation) curve which is proportional to the shearing stress. The initial threshold has been studied elsewhere, and this paper focuses on the subsequent energy absorption after infiltration.

$^{c}$The overall energy absorption is the superposition of the initial infiltration threshold and subsequent resistance encountered during nanofluidic transport. One should note that the initial barrier is higher in more hydrophobic systems (e.g., pure water and CNT); on the other hand, the present paper shows that in a more hydrophobic system the subsequent transport resistance is lower. Therefore, the balance between the initial barrier and transport shearing stress needs to be considered, in order to achieve the optimum combination of liquids and solid nanopores for maximum energy absorption.

![](./images/811798364860448768_10.jpg)

Fig. 8. (a) Dependency of the shearing stress and apparent viscosity of water on the CNT diameter, with a fixed transport rate of 200 m/s; (b) variations of shearing stress and apparent viscosity as a function of the transport rate in a rigid, neutral (18, 18) CNT.

The studies above also show that in a nanotube, the boundary layer (first solvation shell) is very important and the flow properties are mostly dominated by the shearing stress at the tube wall. The shearing stress and nominal (apparent) viscosity depend on liquid and solid phases, but they also vary with flow rate (as briefly shown in this section) and tube size, explored below via water transport through neutral CNTs.

### 3.3. Size and Rate Effects

#### 3.3.1. Size Effect of Viscosity

We first fix the water transport rate at 200 m/s, and vary CNT sizes from (10, 10) to (60, 60), with the tube diameter varying from 1.36 nm to 8.13 nm. Figure 8(a) shows the relationship between the shearing stress $\tau$ and the nominal (apparent) viscosity $\tilde{\eta}$ with the diameter of the CNT. The magnitudes of the shearing stress are less than 3 MPa (for the current flow rate and size range); whereas, if the water transport in CNT obeys the clas- sic Poiseuille flow, in a (60, 60) CNT the shearing stress should be as high as 196 MPa under the transport rate of 200 m/s. The small shearing stress computed from MD simulations suggests that the neutral, non-defect car- bon nanotube is "ultra-smooth" for water flow. The size effect reveals the climbing trend of the shearing stress with increasing nanotube diameter (Fig. 8(a)). In particular, $\tau$ sharply increases when the tube size varies from 2.0 nm to 4.0 nm, and the variation becomes less significant in larger tubes. The corresponding nominal viscosity $\tilde{\eta}$ is at least two orders smaller than the bulk water, varying from $3.8 \times 10^{-6}$ cp in a (10, 10) tube to $1.52 \times 10^{-2}$ cp in a (60, 60) tube.

The nonlinear size effect of the shearing stress is qualitatively related with the characteristics of the first sol- vation shell: the density magnitude of the first salvation shell scales with $(1-2 d^{B} / D) ;^{40}$ and the shearing stress follows a similar nonlinear trend with the confinement, which further impacts the nominal viscosity through $\tilde{\eta}=\tau D /(8 \bar{v})$. One could expect a similar size effect for the $SiO_{2}$ nanotube since both the van der Waals potential and the Columbic potential are conservative and they can be superimposed on each other. Thus, the general trend of the variation of the density of the first solvation shell should be similar.

#### 3.3.2. Rate Effect of Viscosity

The transport rate also plays a substantial role in nanoflu- idics. In Figure 8(b), the shearing stress $\tau$ is shown to increase nonlinearly with $\bar{v}$ in an example (18, 18) CNT, with the slope of increase declining at higher $\bar{v}$. In essence, a higher transport rate gives some liquid molecules more momentum and also less time to optimize their positions (so as to relieve the shearing resistance); hence, at higher flow rates the first solvation shell is closer to the tube wall. $^{27}$ This results in stronger repulsive forces and as the water molecules continuously overcome energy barriers, the shearing stress $\tau$ varies with transport rate $\bar{v}$ as $\tau \propto \bar{v}^{m}$. In Figure 8(b), $m$ is found to be 0.4367 for the current system under investigation.

The variation in shearing stress directly causes the dependence of the effective liquid viscosity on the flow transport rate. For the model (18, 18) CNT, as $\bar{v}$ ranges from 80 m/s to 700 m/s, the apparent shear viscosity reduces continuously with higher transport rate. Overall, the magnitude of $\tilde{\eta}$ is three orders lower than the bulk water viscosity, which is phenomenally consistent with the high transport rate at nanoscale observed in other MD simulations. $^{7,10}$ And the descending trend suggests a shear thinning property of the nanotube water flow.

Figure 9 superimposes the $\tau-\bar{v}$ curves for both par tially charged $SiO_{2}$ nanotube and neutral CNT with close geometric size. Both curves show apparent power law

![](./images/811798364860448768_11.jpg)

Fig. 9. Comparison of shearing stress occurring in water flow in a (18,18) CNT and a $SiO_{2}$ nanotube with identical dimensions.

relationship with the rising transport rate, except that the magnitude of $\tau$ in the $SiO_{2}$ tube is comparably much higher. The variation of $\tau$ versus $\bar{v}$ is also faster in the $SiO_{2}$ nanopore, which can be explained by the stronger electrical interaction between $SiO_{2}$ and water molecules (compared to that of CNT). The electrostatic force decays slowly and has no equilibrium position (as the van der Waals force does), and it attracts the first solvation shell closer to the wall surface, which intensifies the repulsive force.

### 3.3.3. Implication for Energy Absorption

Based on the presented MD simulation analyses, for energy absorption purposes, nanoporous materials with larger nanopore size seems to be more efficient to dissipate external mechanical energy via the "friction" encountered during the transport. Although a larger nanopore size implies less specific surface area, the energy absorption efficiency is not likely to be hampered too much due to the fact that, for a given porosity, the specific inner surface of nanoporous materials, which is proportional to $D^{-1}$, varies in the same pace as $D$; however, the simple several fold increases in $D$ can lead to orders of elevation in the magnitude of the effective viscosity $\tilde{\eta}$. Thus, high performance of NEASs is expected, which is consistent with the experimental observation, where when silica gel of larger nanopore size was used, the energy absorption density was higher. $^{21,24,41}$ On the other hand, the transport rate does affect the flowing properties inside nanotubes, but its significance is less pronounced than the size effect, although higher rate could dissipate more energy which agrees with experiment observations. $^{42}$

## 4. CONCLUSION

In summary, non-equilibrium molecular dynamics (NEMD) simulations have been carried out in the current paper to explore fundamental nanofluidic transport behaviors as the solid phase, liquid phase, pore size and flow rate are varied. Models of smooth and straight carbon nanotube and $SiO_{2}$ nanotube are employed (although it is known that surface roughness may enhance wettability, such phenomenon will be explored in future). The numerical analyses reveal that the shearing stress, which is a dominant factor governing nanofluidics, is a strong function of these system properties. The shearing stress is governed by the characteristics of the first solvation shell formed at the "boundary layer" of the liquid. A nomi- nal shear viscosity is introduced to phenomenologically describe the flow behavior. In order to dissipate more energy during fluid transport at the nanoscale, it is desir- able to employ charged/polarized tube with pure water (without the addition of ions), a larger tube and a higher flow rate. The study may shed some light on designing and optimizing the performance of NEAS, which will be quantitatively compared with experiments in future studies. The fundamental study of nanofluidic behavior is alsorelevant to liquid/ion transport in biological channels. $^{43-45}$

**Acknowledgment:** Yu Qiao is supported by ARO under Grant No. W911NF-05-1-0288, NSF and Sandia National Lab under Grant No. CMMI-0623973. Patricia J. Culligan is supported by NSF under grant No. CMS-04-09521. Xi Chen is supported by NSF under Grant No. CMMI-0643726. Xi Chen is also supported by a WCU (World Class University) program through the National Research Foundation of Korea funded by the Ministry of Educa- tion, Science and Technology of Korea (R32-2008-000-20042-0), and by the National Natural Science Foundation of China (Grant No. 50928601).

## References

1. M. S. P. Sansom and P. C. Biggin, *Nature* 414, 156 (2001).
2. D. J. Mann and M. D. Halls, *Phys. Rev. Lett.* 90, 195503 (2003).
3. Y. C. Liu and Q. Wang, *Phys. Rev. B* 72, 085420 (2005).
4. A. I. Skoulidas, D. M. Ackerman, J. K. Johnson, and D. S. Sholl, *Phys. Rev. Lett.* 89, 185901 (2002).
5. F. B. Surani and Y. Qiao, *J. Appl. Phys.* 100, 034311 (2006).
6. X. Chen, F. B. Surani, X. G. Kong, V. K. Punyamurtula, and Y. Qiao, *Appl. Phys. Lett.* 89, 241918 (2006).
7. M. Majumder, N. Chopra, R. Andrews, and B. J. Hinds, *Nature*438, 44 (2005).
8. J. K. Holt, H. G. Park, Y. Wang, M. Stadermann, A. B. Artyukhin,C. P. Grigoropoulos, A. Noy, and O. Bakajin, *Science* 312, 1034(2006).
9. A. I. Kolesnikov, J. M. Zanotti, C. K. Loong, and P. Thiyagarajan,*Phys. Rev. Lett.* 93, 035503 (2004).
10. G. Hummer, J. C. Rasaiah, and J. P. Noworyta, *Nature* 414, 188(2001).
11. A. Kalra, S. Garde, and G. Hummer, *Proc. Natl. Acad. Sci.* 100,10175 (2003).
12. I. Hanasaki and A. Nakatani, *J. Chem. Phys.* 124, 144708 (2006).
13. S. Joseph and N. R. Aluru, *Nano Lett.* 8, 452 (2008).
14. M. Rauscher and S. Dietrich, *Annu. Rev. Mater. Res.* 38, 143 (2008).

15. J. Maranon Di Leo and J. Maranon, _J. Mol. Struc.-Theochem_ 623, 159 (2003).

16. J. Zou, X. Q. Feng, B. Ji, and H. Gao, _Small_ 2, 1348 (2007).

17. K. Koga, X. C. Zeng, and H. Tanaka, _Phys. Rev. Lett._ 79, 5262 (1997).

18. A. Han and Y. Qiao, _Chem. Lett._ 36, 882 (2007).

19. A. Han and Y. Qiao, _J. Mater. Res._ 22, 3538 (2007).

20. V. K. Punyamurtula and Y. Qiao, _Mater. Res. Innovations_ 11, 37 (2007).

21. A. Han, X. Chen, and Y. Qiao, _Langmuir_ 24, 7044 (2008).

22. A. Han and Y. Qiao, _J. Phys. D: Appl. Phys._ 40, 5743 (2007).

23. A. Han and Y. Qiao, _Langmuir_ 23, 11396 (2007).

24. Y. Qiao, G. Cao, and X. Chen, _J. Am. Chem. Soc._ 129, 2355 (2007).

25. L. Liu, X. Chen, A. Han, and Y. Qiao, _Phys. Rev. Lett._ 102, 184501 (2009).

26. G. Cao, Y. Qiao, Q. Zhou, and X. Chen, _Philos. Mag. Lett._ 88, 371 (2008).

27. G. Cao, Y. Qiao, Q. Zhou, and X. Chen, _Mol. Simul._ 34, 1267 (2008).

28. S. Vaitheeswaran, J. C. Rasaiah, and G. Hummer, _J. Chem. Phys._ 121, 7955 (2004).

29. L. Liu, Y. Qiao, and X. Chen, _Appl. Phys. Lett._ 92, 101927 (2008).

30. M. J. Hwang, T. P. Stockffisch, and A. T. Hagler, _J. Am. Chem. Soc._ 116, 2515 (1994).

31. R. Hockney and J. Eastwood, _Computer Simulation Using Particles_, Taylor and Francis Inc., Bristol, PA, USA (1981).

32. B. M. Pettitt, _J. Chem. Phys._ 84, 5836 (1986).

33. X. Kong, F. B. Surani, and Y. Qiao, _Phys. Scr._ 74, 531 (2006).

34. S. J. Plimpton, _J. Chem. Phys._ 117, 1 (1995).

35. http://lammps.sandia.gov

36. J. L. Xu, Z. Q. Zhou, and X. D. Xu, _Int. J. Num. Methods Heat Fluid Flow_ 14, 664 (2004).

37. J. P. Rothstein and G. H. McKinley, _J. Non-Newtonian Fluid Mech._ 86, 61 (1999).

38. D. Semwogerere, J. F. Morris, and E. R. Weeks, _J. Fluid Mech._ 581, 437 (2007).

39. T. Kim, V. K. Punyamurtula, W. Lu, A. Han, X. Chen, and Y. Qiao, _Appl. Phys. Lett._ 94, 013105 (2009).

40. X. Chen, G. Cao, A. Han, V. K. Punyamurtula, L. Liu, P. J. Culligan, T. Kim, and Y. Qiao, _Nano Lett._ 8, 2988 (2008).

41. A. Han, V. K. Punyamurtula, and Y. Qiao, _Appl. Phys. Lett._ 92, 153117 (2008).

42. F. B. Surani, X. Kong, D. B. Panchal, and Y. Qiao, _Appl. Phys. Lett._ 87, 16311 (2005).

43. X. Chen, Q. Cui, Y. Tang, J. Yoo, and A. Yethiraj, _Biophys. J._ 95, 563 (2008).

44. Y. Tang, J. Yoo, A. Yethiraj, Q. Cui, and X. Chen, _Biophys. J._ 95, 581 (2008).

45. Y. Tang, G. Cao, X. Chen, J. Yoo, A. Yethiraj, and Q. Cui, _Biophys. J._ 91, 1248 (2006).

Received: 30 September 2008. Accepted: 2 November 2008.

![](./images/811798364860448768_12.jpg)

J. Comput. Theor. Nanosci. 7, 379-387, 2010
387