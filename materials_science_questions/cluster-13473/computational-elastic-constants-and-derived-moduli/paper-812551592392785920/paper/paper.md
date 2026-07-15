# A Computer Simulation Study of Thermal and Mechanical Properties of Poly(Ionic Liquid)s

Youngseon Shim *, Munbo Shim and Dae Sin Kim

Innovation Center, Samsung Electronics Co., Ltd., 130 Samsungjeonja-ro, Hwaseong-si 16678, Gyeonggi-do, Korea;
munbo.shim@samsung.com (M.S.); daesin.kim@samsung.com (D.S.K.)
* Correspondence: ys1231.shim@samsung.com

**Abstract:** Thermal and mechanical properties of poly(ionic liquid)s (PILs), an epoxidized ionic liquid-amine network, are studied via molecular dynamics simulations. The poly(ionic liquid)s are designed with two different ionic liquid monomers, 3-[2-(Oxiran-2-yl)ethyl]-1-{4-[(2-oxiran-2-yl)ethoxy]phenyl}imidazolium (EIM2) and 1-{4-[2-(Oxiran-2-yl)ethyl]phenyl}-3-{4-[2-(oxiran-2-yl)ethoxy]benzyl}imidazolium (EIM1), each of which is networked with tris(2-aminoethyl)amine, paired with different anions, bis(trifluoromethanesulfonyl)imide (TFSI⁻) and chloride (Cl⁻). We investigate how ionic liquid monomers with high ionic strength affect structures of the cross-linked polymer networks and their thermomechanical properties such as glass transition temperature (T<sub>g</sub>) and elastic moduli, varying the degree of cross-linking. Strong electrostatic interactions between the cationic polymer backbone and anions build up their strong structures of which the strength depends on their molecular structures and anion size. As the anion size decreases from TFSI⁻ to Cl⁻, both T<sub>g</sub> and elastic moduli of the PIL increase due to stronger electrostatic interactions present between their ionic moieties, making it favorable for the PIL to organize with stronger bindings. Compared to the EIM2 monomer, the EIM1 monomers and TFSI⁻ ions generate a PIL with higher T<sub>g</sub> and elastic moduli. This attributes to the less flexible structure of the EIM1 monomer for the chain rotation, in which steric hindrance by ring moieties in the EIM1-based PIL enhances their structural rigidity. The π-π stacking structures between the rings are found to increase in EIM1-based PIL compared to the EIM2-based one, which becomes stronger with smaller Cl⁻ ion rather than TFSI⁻. The effect of the degree of cross-linking on thermal and mechanical properties is also examined. As the degree of cross-linking decreases from 100% to 60%, T<sub>g</sub> also decreases by a factor of 10–20%, where the difference among the given PILs becomes decreased with a lower degree of cross-linking. Both the Young’s (E) and shear (G) moduli of all the PILs decrease with degree of cross-linking, which the reduction is more significant for the PIL generated with EIM2 monomers. Transport properties of anions in PILs are also studied. Anions are almost immobilized globally with very small structural fluctuations, in which Cl⁻ presents lower diffusivity by a factor of ~2 compared to TFSI⁻ due to their stronger binding to the cationic polymer backbone.

**Keywords:** poly(ionic liquid)s; glass transition temperature; mechanical modulus; molecular dynamics simulation

## 1. Introduction

Supported ionic liquid phases have been extensively emerging as a new class of functional materials, where ionic liquids with low volatility, chemical and thermal stability, and ionic conductivity are immobilized on polymers or inorganic supports [1–7]. A polymer-supported ionic liquid has important implications for advanced materials in the area of catalysis as well as energy applications. It was found that supported ionic liquid phases yield similar or even better catalytic performance in terms of activity, selectivity, and stability than conventional organic solvents [8–10]. Poly(ionic liquid)s (PILs) attract

---

Citation: Shim, Y.; Shim, M.; Kim, D.S. A Computer Simulation Study of Thermal and Mechanical Properties of Poly(Ionic Liquid)s. *Membranes* 2022, 12, 450. https://doi.org/10.3390/membranes12050450

Academic Editors: Mohammad Afsar Uddin and Faiz Ahmed

Received: 17 March 2022
Accepted: 19 April 2022
Published: 21 April 2022

Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812551592392785920_1.jpg)

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland.
This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).


more attention as alternative polymer electrolytes in various applications such as in elec- trochemical, energy storage, and conversion devices [11–17]. Despite their high thermal stability and wide electrochemical window as electrolytes in lithium-based batteries, their commercial market is restricted because of low ionic conductivities at ambient temperature. An electrolyte for lithium batteries requires an ionic conductivity above $10^{-1}$ S/m, while polymer electrolytes appear to reach an upper limit below $10^{-2}$ S/m at room temperature. The performance of PILs can be further enhanced by adding ILs in the solvent to increase the mobility of PIL chains [18–21]. The ionic conductivity of PILs should be improved in a future direction towards the design of mobile ionic moieties with more flexibility in a robust macromolecular structure, and practical synthetic strategies.

Thermosetting polymers enable the high-temperature applications with strong me- chanical properties due to their three-dimensional network structure by cross-linking. To take advantage of ionic properties for thermosetting polymers, new ionic liquid monomers were designed and polymerized to generate eco-friendly PILs with novel physical proper- ties for potential electrochemical and biomedical applications [22–28]. Considerable efforts have already been exerted on the polymerization using ionic liquid monomers with high ionic conductivity, thermal and electrochemical stability, low vapor pressure, and non- flammability, targeting the sustainable polymer networks with improved properties [29–34]. In recent years, there have been several research developments on the polymerization us- ing ionic liquid monomers with antibacterial and mechanical functions. Epoxy-amine networks designed from imidazolium ionic liquid-based monomers were found to play a crucial role in the hydrophobic behavior for antibacterial functions due to the chemical structure of ionic liquids [35,36]. Livi et al., investigated the reaction and kinetics between the imidazolium ionic liquid monomer and poly(oxypropylene diamine) using differential scanning calorimetry analyses (DSC), Fourier-transform infrared (FTIR) and “in situ” NMR spectroscopy and their physical properties such as the thermal stability, thermomechanical behavior, and ionic conductivity ($2.4 \times 10^{-3}$ S/m at 373 K) were also demonstrated using transmission electronic microscopy (TEM), thermogravimetric analysis (TGA), dynamical mechanical analysis (DMA), and dielectric spectroscopy [36]. Polymer networks, polymer- ized between the bis(imidazolium) ionic liquid and isophorone diamine, were reported by Radchenko et al., in which their hydrophobic behavior, thermal and mechanical prop- erties were examined using TGA, DMA, and DSC [37]. Dzienia et al., demonstrated the cure kinetics of DGEBA using imidazolium-based ionic liquid curing agents, in which the presence of the salicylate anion results in a highly cross-linked polymerization compared to chloride anion [38]. Radchenko et al., reported the synthesis of PIL networks based on cycloaliphatic epoxidized ionic liquids with thermomechanical and potential shape memory behaviors [39,40].

The potential application of PILs as functional materials in energy storage and electro- chemical devices is promising as the new types of ionic liquids are being developed with the advances in polymer chemistry. The synthesis of PILs has been extensively studied in recent decades, but fundamental understanding of the mechanisms underlying structure– property relations in PILs is still far from the requirements of practical energy storage and electrochemical devices. The key issue we examine in this article is how thermal and mechanical properties of PILs are influenced by their microscopic structures. To address this issue, we investigate how different ionic liquid monomers affect glass transition tem- peratures and elastic moduli of their polymer networks, varying the degree of cross-linking. The effects of anions on the structures and properties of the PILs are also examined. Finally, we also demonstrate transport dynamics of the anions in the PILs. The outline of this paper is as follows: In Section 2, we give a brief description of the models and methods employed in this study. Equilibrium structural properties and dynamics of the PILs are analyzed and compared with other recent experimental studies in Section 3. Concluding remarks are offered in Section 4.

## 2. Models and Methods

The model PIL systems composed of bis(epoxidized) imidazolium monomers networked with tris(2-aminoethyl)amine (TAEA), paired with either bis(trifluoromethanesulfonyl) imide (TFSI⁻) or chloride (Cl⁻), were studied using molecular dynamics (MD) simulations. We considered two different imidazolium-based cationic monomers, 3-[2-(Oxiran-2-yl)ethyl]-1-{4-[(2-oxiran-2-yl)ethoxy]phenyl}imidazolium (EIM2) and 1-{4-[2-(Oxiran-2-yl)ethyl]phenyl}-3-{4-[2-(oxiran-2-yl)ethoxy]benzyl}imidazolium (EIM1), where the cationic monomers are paired with either TFSI⁻ or Cl⁻ anions to be electronically neutral. All molecular structures of cationic monomers, TFSI⁻, and TAEA curing agent are described in Figure 1. All simulations were performed using Schrodinger's Materials Science Suite program [41]. The OPLS3e force field parameters [42,43] were used to describe the PILs. Each system was initially set by randomly packing the 800 molecules in a simulation box with a stoichiometry of 3:2 for ionic liquid monomers and TAEA. We utilized a cross-linking simulation based on distance-based reaction criteria to mimic curing processes of PILs, employing the TAEA curing agent. The ratio of reaction rates, epoxy-primary amine reactions k₁ and epoxy-secondary amine reactions k₂, was set as 1. The cross-linked topologies after curing processes and the final properties could be significantly changed by the ratio of reaction rates. However, it was confirmed that no significant difference between the Tg predicted for k₂/k₁ = 1 and k₂/k₁ = 0.01 was observed for the systems composed of diglycidyl-ether of bisphenol F (DGEBF) and 4,4'-diaminodiphenyl sulphone (44DDS) [44]. One of the cross-linked reaction structures between cationic monomers and TAEA is displayed in Figure 2. To examine the effect of degree of cross-linking φ for PILs, the cross-linking iterations were φ = 60 - 100% in 10% increments. One of the cross-linked structures between cationic monomers and TAEA is displayed in Figure 2. As for φ = 100%, 300 cationic monomers are completely cross-linked together as a single cationic polymer backbone by 200 TAEA curing molecules, paired with 300 anions to neutralize the system.

![](./images/812551592392785920_2.jpg)

Figure 1. Molecular structures of cationic (a) EIM2 and (b) EIM1 monomers, (c) tris(2-aminoethyl)amine (TAEA) curing agent, and (d) bis(trifluoromethanesulfonyl)imide (TFSI⁻) anion.

![](./images/812551592392785920_3.jpg)

Figure 2. A representation of the cross-linking processes and their networked structures, obtained by reactions of cationic EIM2 monomers and tris(2-aminoethyl)amine (TAEA) curing agent. The network structure propagates by cross-linking processes in the three-dimensional space, where the stoichiometry for EIM2 monomers and TAEA is set to be 3:2 in the system, paired with anions to neutralize the total system.

For the PILs cross-linked at each degree of cross-linking $\varphi$, MD simulations for 20 ns were performed using NPT ensemble at 700 K and 1 atm and then five different configurations with a time interval of 1 ns were collected to make five annealing cycles. To evaluate $T_g$ of the PILs at each degree of cross-linking $\varphi$, the annealing cycles of each system were conducted over a temperature range from 700 to 200 K, in 20 K decrements. At each temperature, the densities were determined using NPT ensemble over the last 2 ns trajectories of the total 20 ns trajectories, averaged over the five samples. The long-range electrostatic interactions were computed via the Ewald method, resulting in essentially no truncation of these interactions. The trajectories were integrated via RESPA algorithm using a time step of 1 fs [45]. The Nosé–Hoover thermostat [46] and Martyna–Tobias–Klein barostat [47] methods were used.

The hyperbolic-regression model of the density $\rho$ averaged over the five cooling cycles, as a function of temperature T [48],

$$
\rho(\mathrm{T})=\rho_{0}-a\left(T-T_{0}\right)-b H_{0}\left(T-T_{0}, c\right)
\tag{1}
$$

$$
H_{0}\left(T-T_{0}, c\right)=\frac{1}{2}\left(T-T_{0}\right)+\sqrt{\frac{\left(T-T_{0}\right)^{2}}{4}+e^{c}}
\tag{2}
$$

is utilized to evaluate the glass transition temperature $T_g$, where $T_0$, $\rho_0$, a, b, and c are determined to fit $\rho(\mathrm{T})$. The constants -a and -a-b are the slopes of the asymptotic low and high temperature regimes, and c smoothens the discontinuity in the slope close to $T=T_0$. The $T_g$ is estimated by the intersection of low and high temperature asymptotes of the hyperbola.

Equilibration simulations for $1\ \mu$s at each cross-linking $\varphi$ were performed in the canonical ensemble at 300 K, followed by 20 ns production trajectories from which ensemble averages were computed to calculate the structure and dynamic properties. Mechanical properties of PILs were examined with elastic constants to characterize their stiffness. The linear stress–strain relation in the limit of infinitesimal deformation is given by

$$
\sigma_{i j}=C_{i j k l} \epsilon_{k l}
\tag{3}
$$

$$
\sigma_{i j}=\frac{1}{V} \sum_{\alpha=1}^{N}\left[-m_{\alpha} v_{i}^{\alpha} v_{j}^{\alpha}+\sum_{\beta<\alpha}\left(r_{i}^{\beta}-r_{i}^{\alpha}\right) f_{i}^{\alpha \beta}\right]
\tag{4}
$$

where $\sigma_{ij}$ and $\epsilon_{kl}$ represent the elements of the symmetric stress and strain tensor, and $C_{ijkl}$ are the elements of the fourth rank elasticity tensor. The instantaneous stress $\sigma_{ij}$ is computed based on the virial theorem, where indices $\alpha$, $\beta$ refer to atoms and $f_i^\alpha$, $v_i^\alpha$, and $r_i^\alpha$ are the $i$-th force, velocity, and position component of atom $\alpha$. $V$ is the volume of the atomic system and N is the number of atoms in the system. MD simulations at each degree of cross-linking were performed using NVT ensemble at 300 K and 1 atm by applying a constant strain rate of $2 \times 10^6$/s under uniaxial and biaxial tensions. The stress and strain data were averaged over each direction and last 20% of 2 ns trajectories and elastic moduli were calculated using the tensile stress-strain curve up to 1.6%.

## 3. Results and Discussion

We first demonstrate the molecular structure of the PILs. The model PIL systems composed of bis(epoxidized) imidazolium monomers networked with tris(2-aminoethyl)amine (TAEA), paired with either bis(trifluoromethanesulfonyl)imide (TFSI-) or chloride (Cl-), are presented in snapshots of Figure 3. To examine the intermolecular structure between the cationic polymer backbone and anions, their radial distribution functions g(r) are displayed in Figure 4a, where r is a distance between the center-of-mass of the anions and nitrogen atoms of the imidazolium ring in the PIL backbone. It is remarkable that anions in the three PILs make a strong structure (in solid lines) over $\text{r} = 4 \sim 6$ Å, followed by the minimum structure around $\text{r} = 7 \sim 9$ Å, regardless of $\varphi$. To be specific, TFSI$^-$ and Cl$^-$ build up their maximum distribution at $\text{r} = 4.4$ and 4.8 Å, respectively, from nitrogens of the EIM2-based backbone. This is ascribed to the fact that smaller Cl$^-$ anions more strongly interact with cationic imidazolium rings in a shorter interionic distance, compared to TFSI$^-$. It is also found that TFSI$^-$ anions organize stronger structures at the EIM1-based backbone rather than the EIM2-based one. A decrease in the interionic distance in Figure 4a gives rise to the increase in the electrostatic interaction strength. Compared to cationic imidazolium-anion structures, TFSI$^-$ and Cl$^-$ ions exhibit broad anion-anion distributions (in dashed lines) over $\text{r} = 7 \sim 10$ Å and $\text{r} = 5 \sim 10$ Å, respectively. We note that cationic imidazoliums and anions are distributed in an alternative layered manner, in similarity with room temperature ionic liquids [49]. As a result, the difference in ion sizes and their molecular structures determine the strength of their electrostatic interactions. On the other hand, the backbones of all three PILs are found to connect by hydrogen bonds to ether oxygens of the EMI2/EIM1, where a hydrogen bond is defined to exist if the distance between the two heavy atoms (O-O) is less than 2.8 Å and the angle of H-O-O is less than $30^\circ$. The amount of the ether oxygens forming hydrogen bonds decreases in order of PIL system generated with EIM2/TFSI$^-$ (88-91%), EIM1/TFSI$^-$ (76-80%), and EIM2/Cl$^-$ (28-35%), respectively, over $\varphi = 60$-$90\%$. We note that the hydrogen bonding characteristic has dramatically reduced for EIM2/Cl$^-$, in which Cl$^-$ ions have a tendency to make a strong peak with oxygen atoms replacing the hydrogen bonds, displayed in Figure 4b.

![](./images/812551592392785920_4.jpg)

Figure 3. Snapshots of the PILs generated with EIM2 cationic monomers and different anions, TFSI$^-$ (left-hand side) and Cl$^-$ (right-hand side), obtained at 300 K. Van der Waals representations of the molecules are employed, where green, purple, orange, and pink symbols represent the atoms of the EIM2, TAEA, TFSI$^-$, and Cl$^-$.

![](./images/812551592392785920_5.jpg)

Figure 4. Radial distributions g(r) of (a) the cationic EIM2/EIM1 (in solid lines) and TFSI⁻/Cl⁻ ions (in dashed lines) around the TFSI⁻/Cl⁻ ions in the PILs, and g(r) of (b) TFSI⁻/Cl⁻ ions around the ether oxygens (O3) of EIM2/EIM1, obtained 300 K, where r (in units of Å) is a distance between the center-of-mass of the anions and (a) nitrogen (imidazolium)/(b) oxygen (ether) atoms of the EIM2/EIM1.

To gain more insight into the PIL structure, the orientational order and ring stacks of the PIL were scrutinized to associate their structural rigidity. The order parameters $< P_2(\cos\theta(t)) >$ for PILs are analyzed, where $\langle\cdots\rangle$ denotes an equilibrium average, $P_2$ is the second order Legendre polynomial, and $\cos\theta(t)$ is the angle between the ring plane and its z-axis of the simulation box at time $t$. We notice that the ring orientation becomes isotropic $P_2 \sim 0$ with smaller orientational fluctuations as the $\varphi$ decreases in Figure 5. The magnitude of $P_2$ is slightly increased for the EIM1-based PIL of which the monomer has one more ring than EIM2. As for the EIM1-based PIL, $P_2 \sim -0.2$ indicates that on average the rings there are tilted from the z-axis by about $65^\circ$. The $\pi-\pi$ stacking structure between the rings such as imidazolium and benzene is also counted when the distance between the center-of-mass of the rings is within $4.4Å$ and the angle between the two ring planes is less than $30^\circ$. The total number of $\pi-\pi$ stacking structures increases for the EIM1-based PIL of which the monomer has one more ring than EIM2. As for the same EIM2, $Cl^-$ anions generate a slightly greater number of $\pi-\pi$ stacking structures. We note that smaller $Cl^-$ make distributions around the cationic backbone with slightly less disturbance of the $\pi-\pi$ stacking orientations between the rings of the backbone compared to TFSI⁻. The ratio of the $\pi-\pi$ stacking structures is denoted as $P_{\pi-\pi}$, averaged over all the rings. For three PILs, $P_{\pi-\pi}$ increases in order of EIM2/TFSI⁻ (53-57%), EIM1/TFSI⁻ (54-60%), and EIM2/Cl⁻ (56-61%) over $\varphi=60$-$90\%$, where $P_{\pi-\pi}$ has a tendency to reduce with increase in $\varphi$. The rotational motions of the ring moieties at the polymer backbone are hindered due to their high dihedral free energy barriers, increasing steric hindrance due to their limited structural reorganization in the local free volume [50]. The structural orientations and rigidity arising from ring moieties would affect thermal and mechanical properties.

To measure the glass transition temperature $T_g$, density profiles of the PILs obtained from the annealing cycles were used over $\varphi=60$-$90\%$ and the values of $T_g$ were determined by Equation (1). Temperature-dependent density behaviors at $\varphi=80$ and $90\%$ are demonstrated in Figure 6. The total density of PILs decreases with increase in the electrostatic interactions between the cationic imidazoliums and anions, in order of system generated with EIM2/TFSI⁻, EIM1/TFSI⁻, and EIM2/Cl⁻. The MD results of glass transition temperature $T_g$ at each degree of cross-linking $\varphi$ are exhibited in Figure 7a and Table 1. Our MD results agree that the glass transition temperature increases with increasing the degree of the cross-linking [51]. The predictions of $T_g$ from MD simulations are usually higher than experimental values because of the discrepancy in their cooling rates. MD simulations typically cool the system by more than 10 K per nanosecond, while cooling rates in experiments are set to be of the order of 10 K per minute. The predictions are commonly corrected to subtract approximately 3 K for each order of magnitude difference in cooling

rates according to the well-established Williams-Landel-Ferry (WLF) equation [52]. As for the EIM2- and EIM1-based PILs paired with TFSI⁻, the corrected $T_g$ of the PILs are estimated to be 317~342 K and 321~364 K, respectively, over the degree of cross-linking 60–90%. As the anion size decreases from TFSI⁻ to Cl⁻ for the EIM2, $T_g$ increases by 20 K at $\varphi=60\%$ to 65 K at $\varphi=90\%$ due to the stronger electrostatic interactions present between their ionic moieties, making it favorable for the PIL to organize with stronger binding. It was also found that $T_g$ for the EIM1 monomer is higher by 22 K at $\varphi=90\%$ compared to the EIM2 monomer and the difference is reduced with decrease in the $\varphi$. This attributes to the fact that dihedral motions of ring moieties in the EIM1-based PIL are hindered to enhance the structural rigidity.

![](./images/812551592392785920_6.jpg)

Figure 5. Order parameters $P_2(\cos\theta(t))$ of the PILs at (a) $\varphi=90$ and (b) 80% at 300 K, where $P_2$ is the second order Legendre polynomial and $\cos\theta(t)$ is the angle between the ring orientation and its z-axis of the simulation box at time $t$.

![](./images/812551592392785920_7.jpg)

Figure 6. Temperature-dependent density profiles of the PILs at (a) $\varphi=90$ and (b) 80%.

![](./images/812551592392785920_8.jpg)

Figure 7. Glass transition temperature (a) $T_g$ and (b) elastic moduli, obtained at 300 K. Young's and shear moduli are displayed in solid and dotted lines, respectively. Error bars are within symbol sizes.

**Table 1.** Glass transition temperatures Tg (in K) and Young's modulus E (in GP) for poly(ionic liquid)s according to the degree of cross-linking $\varphi(\%)$. The poly(ionic liquid)s consist of bis(epoxidized) imidazolium monomers (EIM2/EIM1) networked with TAEA, paired with either bis(trifluoromethanesulfonyl)imide (TFSI⁻) or chloride (Cl⁻) anions. The elastic properties are obtained at 300 K.

<table>
<thead>
<tr>
<th rowspan="2">$\varphi(\%)$</th>
<th colspan="3">$\mathbf{T_g}$ (K)</th>
<th colspan="3">$\mathbf{E}$ (GPa)</th>
</tr>
<tr>
<th>EIM2/TFSI⁻</th>
<th>EIM2/Cl⁻</th>
<th>EIM1/TFSI⁻</th>
<th>EIM2/TFSI⁻</th>
<th>EIM2/Cl⁻</th>
<th>EIM1/TFSI⁻</th>
</tr>
</thead>
<tbody>
<tr>
<td>90</td>
<td>371</td>
<td>436</td>
<td>393</td>
<td>1.21</td>
<td>1.44</td>
<td>1.05</td>
</tr>
<tr>
<td>80</td>
<td>352</td>
<td>419</td>
<td>374</td>
<td>0.78</td>
<td>1.39</td>
<td>1.03</td>
</tr>
<tr>
<td>70</td>
<td>351</td>
<td>399</td>
<td>365</td>
<td>0.40</td>
<td>1.18</td>
<td>0.88</td>
</tr>
<tr>
<td>60</td>
<td>346</td>
<td>366</td>
<td>350</td>
<td>0.36</td>
<td>0.88</td>
<td>0.79</td>
</tr>
</tbody>
</table>

McDanel et al., studied PILs composed of bis(epoxidized) ionic liquid monomer and TFSI⁻, and networked with TAEA, using differential scanning calorimetry (DSC), where $T_g$ = 311 and 282 K with the epoxy conversion rate of 67 and 80% were measured at different monomer stoichiometric ratios [34]. Their monomer would be more flexible without any aromatic ring compared to our EIM2 and EIM1, resulting in lowering $T_g$. Livi et al., studied PILs composed of the same IL monomers and anions as ours, but networked with different curing agent Jeffamine D-230, using DSC and DMA [35]. It was found to be $T_g$ = 328 and 340 K for PILs generated with EIM2 and EIM1 monomers, respectively, where the epoxy conversion rates were higher than 90%. The trend in $T_g$ between EIM2- and EIM1-based PILs is in agreement with our predicted value above, that is, EIM1 monomers tend to build up stiffer PILs with higher $T_g$. We note that the glass transition temperatures of an epoxy network can be hugely changed more than 140 K by just using different curing agents [53,54]. This can explain larger $T_g$ values obtained in our simulations. It is notable that $T_g$ of PILs could be lower compared to the conventional epoxy networks based on diglycidylether bisphenol A (DGEBA) cured with various amines, where triethylenetetramine (TETA), isophorone diamine (IPD), and diethyltoluene diamine (DETDA) were known to make the epoxy networks with high $T_g$ = ~400 K, ~440 K, and 440~480 K, respectively [54–56]. Whereas, a bisphenol A group composed of two benzene rings connected by a dimethylmethane in DGEBA increase steric hindrance due to their very limited chain rotations in the local free volume and thus $T_g$, ionic liquids monomers such as EIM1 and EIM2 are found to decrease $T_g$ of the polymer networks.

MD results of the elastic moduli are presented in Figure 7b and Table 1. Young's modulus E range is 1.1~1.4 GPa for our three PILs at $\varphi=90\%$, where the values decrease with decrease in $\varphi$ in our PILs. As we increase $\varphi$ up to 100%, E is dramatically increased to be 3.2~3.5 GPs for our PILs paired with TFSI⁻. Our predicted E values can be larger than those measured experimentally due to the discrepancy between the strain rates used in the simulations and experiments. The conventional epoxy networks based on diglycidylether bisphenol A (DGEBA) cured with various amines were known to have Young's modulus of E = 2.4~2.7 GPa [54–56]. The polymer copolymerized between the bisimidazolium ionic liquid monomers and IPD was reported to show E = 1.7 GPa and $T_g$ = 328~338 K at the conversion rate of more than 95%, using DSC and DMA [37]. We notice that our PILs paired with TFSI⁻ have relatively high Young's modulus of 1.1–3.5 GPa at $\varphi=90$–100%, despite lower $T_g$ compared to DEGBA. Analogous to the glass transition temperature, elastic properties of the PILs, both Young's modulus (E), and shear modulus (G), are found to increase with increasing the degree of cross-linking [51].

We take into account translational motions of the anions in the PILs to examine the ion mobility for potential applications to electrolytes. In Figure 8, mean square displacements (MSDs) of TFSI- and Cl- ions in the PILs at $\varphi=90\%$ are displayed. In the long time limit of normal diffusion, they are assumed to increase linearly with time, and a self-diffusion coefficient can be calculated from their slope. We note that translational motions of the anions in the PILs are much slower with diffusion coefficients of about

$5 \times 10^{-5}$~$10^{-4}$ fick (1 fick $= 10^{-9}\ \text{m}^2/\text{s}$) at room temperature, whereas the corresponding value in the ionic liquids, alkyl-imidazolium TFSI⁻, is three orders of magnitude larger at about $10^{-2}$~$10^{-1}$ fick [57,58]. The translational motions of Cl⁻ ions significantly decelerate compared to those of TFSI- ions, attributed to stronger binding to the cationic segments of the PILs in Figure 3 left. TFSI⁻ presents higher diffusivity by factor of ~2 than smaller Cl⁻ due to their weaker binding to the cationic polymer backbone. Analogous to our MD results, recent computational studies have been studied to examine the mechanism of ion transport. The anion diffusivity in poly(1-butyl-3-vinylimidazolium-tetrafluoroborate) was also found to be three orders of magnitude lower than that in ionic liquids, where the hopping of an anion trapped in cages organized by cationic segments of the chain determines their diffusivity [59]. Mogurampelly et al., reported that the ion mobility is strongly correlated to the average lifetimes of the ion associations in poly(ionic liquid)s [60]. Luo et al., also reported that the anion mobility is correlated to both the structural relaxation times and the average lifetime of ion associations [61]. They also observed that a small halide anion has a significantly lower diffusivity with dynamic heterogeneity, ascribed to the stronger bind of the anions with the polymerized cation. Our MD results imply that ion transport of the PILs is governed by intermolecular structures in the PILs and their binding strength between the inter-ions. Recently, a cross-linked epoxy-based solid-state polymer electrolyte combined with ionic liquids, tetraethylene glycol dimethyl ether, and Li salt, was reported to exhibit a high ionic conductivity of ~$10^{-1}\ \text{S/m}$, depending on the Li salt concentration and associated polymerization-induced phase separation [62,63]. It was pointed out that the molecular interactions according to the Li salt concentration cause different phase separation and morphologies, affecting the activation energy for the ion conduction [63].

![](./images/812551592392785920_9.jpg)

Figure 8. Mean square displacements (MSDs) of the center-of-mas of TFSI⁻ and Cl⁻ ions in the PILs, obtained at 300 K. The units of MSDs are $\text{\AA}^2$.

## 4. Conclusions

We investigated thermal and mechanical properties of PILs generated with different ionic liquid monomers using molecular dynamics computer simulations. Effects of microscopic molecular structures on glass transition temperatures and elastic moduli of the polymer networks were examined, varying the degree of cross-linking. Strong electrostatic interactions between the cationic polymer backbone and anions build up their strong structures of which the strength depends on their molecular structures and anion size. As electrostatic interactions present between their ionic moieties increase, the PIL shows strongly binding structures. As either anion size increases from Cl⁻ to TFSI⁻ or cationic monomer becomes flexible, both $\text{T}_\text{g}$ and elastic moduli of their PIL are reduced. It was found that thermal and mechanical properties, $\text{T}_\text{g}$, tensile and shear modulus increase

with degree of cross-linking in the PILs. Anion transport in the PILs was also examined through their translational dynamics. Anions strongly binding to cationic moieties are almost immobilized globally with limited structural fluctuations, where $Cl^-$ presents lower diffusivity by factor of ~2 than $TFSI^-$. Tunable combinations of their cationic moieties and anions allows to develop ionic liquids with improved ionic conductivity in a future direction towards the design of mobile ionic moieties including more flexible spacers, robust macromolecular structures, and practical synthetic strategies. Another strategy to enhance the ionic conductivity is the co-addition of solvent plasticizers into the polymer electrolytes [18-21], resulting in a more flexible one with lower glass transition temperature and mechanical strength. To improve the ionic mobility without any loss of elastic modulus, phase-separated microstructures of the cross-linked polymer networks could be also designed [62,63]. Influence of the microscopic structures at the molecular level on thermomechanical properties should be understood for applications to practical energy storage and electrochemical devices.

Author Contributions: Conceptualization, formal analysis, investigation, writing-original draft preparation, writing-review and editing, visualization, Y.S.; project administration, M.S. and D.S.K. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Not applicable.

Acknowledgments: Computing resources were provided by the Supercomputing Center of Samsung Electronics.

Conflicts of Interest: There are no conflict of interest to declare.

## References

1.  Motokura, K.; Itagaki, S.; Iwasawa, Y.; Miyaji, A.; Baba, T. Silica-supported aminopyridinium halides for catalytic transformations of epoxides to cyclic carbonates under atmospheric pressure of carbon dioxide. *Green Chem.* 2009, 11, 1876-1880. [CrossRef]

2.  Tharun, J.; Hwang, Y.; Roshan, R.; Ahn, S.; Kathalikkattil, A.C.; Park, D.W. A novel approach of utilizing quaternized chitosan as a catalyst for the eco-friendly cycloaddition of epoxides with $CO_2$. *Catal. Sci. Technol.* 2012, 2, 1674-1680. [CrossRef]

3.  Wei-Li, D.; Bi, J.; Sheng-Lian, L.; Xu-Biao, L.; Xin-Man, T.; Chak-Tong, A. Polymer grafted with asymmetrical dication ionic liquid as efficient and reusable catalysts for the synthesis of cyclic carbonates from $CO_2$ and epoxides. *Catal. Today* 2014, 233, 92-99. [CrossRef]

4.  Mousavi, B.; Chaemchuen, S.; Moosavi, B.; Luo, Z.X.; Gholampour, N.; Verpoort, F. Zeolitic imidazole framework-67 as an efficient heterogeneous catalyst for the conversion of $CO_2$ to cyclic carbonates. *New J. Chem.* 2016, 40, 5170-5176. [CrossRef]

5.  Wang, X.C.; Zhou, Y.; Guo, Z.J.; Chen, G.J.; Li, J.; Shi, Y.M.; Liu, Y.Q.; Wang, J. Heterogeneous conversion of $CO_2$ into cyclic carbonates at ambient pressure catalyzed by ionothermal-derived meso-macroporous hierarchical poly(ionic liquid)s. *Chem. Sci.* 2015, 6, 6916-6924. [CrossRef]

6.  Kim, D.W.; Chi, Y. Polymer-supported ionic liquids: Imidazolium salts as catalysts for nucleophilic substitution reactions including fluorinations. *Angew. Chem.* 2004, 116, 489-491. [CrossRef]

7.  Kim, D.W.; Hong, D.J.; Jang, K.S.; Chi, Y. Structural Modification of Polymer-Supported Ionic Liquids as Catalysts for Nucleophilic Substitution Reactions Including Fluorination. *Adv. Synth. Catal.* 2006, 348, 1719-1727. [CrossRef]

8.  Altava, B.; Burguete, M.I.; Garcia-Verdugo, E.; Karbass, N.; Luis, S.V.; Puzary, A.; Sans, A. Palladium N-methylimidazolium supported complexes as efficient catalysts for the Heck reaction. *Tetrahedron Lett.* 2006, 47, 2311. [CrossRef]

9.  Karbass, N.; Sans, V.; Garcia-Verdugo, E.; Burguete, M.I.; Luis, S.V. Pd(0) supported onto monolithic polymers containing IL-like moieties. Continuous flow catalysis for the Heck reaction in near-critical EtOH. *Chem. Commun.* 2006, 3095-3097. [CrossRef]

10. Lozano, P.; Garcia-Verdugo, E.; Piamtongkam, R.; Karbass, N.; Diego, T.; Butguete, M.I.; Luis, S.V. Bioreactors Based on Monolith-Supported Ionic Liquid Phase for Enzyme Catalysis in Supercritical Carbon Dioxide. *Adv. Synth. Catal.* 2007, 349, 1077. [CrossRef]

11. Ohno, H.; Ito, K. Room-temperature molten salt polymers as a matrix for fast ion conduction. *Chem. Lett.* 1998, 27, 751-752. [CrossRef]

12. Mecerreyes, D. Polymeric ionic liquids: Broadening the properties and applications of polyelectrolytes. *Prog. Polym. Sci.* 2011, 36, 1629-1648. [CrossRef]

13. Yuan, J.; Antonietti, M. Poly(ionic liquid)s: Polymers expanding classical property profiles. *Polymer* 2011, 52, 1469-1482. [CrossRef]

14. Nishimura, N.; Ohno, H. 15th anniversary of polymerized ionic liquids. *Polymer* **2014**, *55*, 3289–3297. [CrossRef]

15. Shaplov, A.S.; Marcilla, R.; Mecerreyes, D. Recent advances in innovative polymer electrolytes based on poly(ionic liquid)s. *Electrochim. Acta* **2015**, *175*, 18–34. [CrossRef]

16. Ajjan, F.N.; Ambrogi, M.; Tiruye, G.A.; Cordella, D.; Fernandes, A.M.; Grygiel, K.; Isik, M.; Patil, N.; Porcarelli, L.; Rocasalbas, G.; et al. Innovative polyelectrolytes/poly(ionic liquid)s for energy and the environment. *Polym. Int.* **2017**, *66*, 1119–1128. [CrossRef]

17. Yuan, J.; Antonietti, M. *Applications of Ionic Liquids in Polymer Science and Technology*; Springer: Berlin, Germany, 2015; pp. 47–67.

18. Zhou, D.; Liu, R.; Zhang, J.; Qi, X.; He, Y.-B.; Li, B.; Yang, Q.-H.; Hu, Y.-S.; Kang, F. In situ synthesis of hierarchical poly(ionic liquid)-based solid electrolytes for high-safety lithium-ion and sodium-ion batteries. *Nano Energy* **2017**, *33*, 45–54. [CrossRef]

19. Susan, M.A.B.H.; Kaneko, T.; Noda, A.; Watanabe, M. Ion gels prepared by in situ radical polymerization of vinyl monomers in an ionic liquid and their characterization as polymer electrolytes. *J. Am. Chem. Soc.* **2005**, *127*, 4976–4983. [CrossRef]

20. Carlisle, T.K.; McDanel, W.M.; Cowan, M.G.; Noble, R.D.; Gin, D.L. Vinyl-Functionalized Poly(imidazolium)s: A Curable Polymer Platform for Cross-Linked Ionic Liquid Gel Synthesis. *Chem. Mater.* **2014**, *26*, 1294–1296. [CrossRef]

21. Mogurampelly, S.; Ganesan, V. Ion Transport in Polymerized Ionic Liquid–Ionic Liquid Blends. *Macromolecules* **2018**, *51*, 9471–9483. [CrossRef]

22. Koch, V.R.; Nanjundiah, C.; Appetecchi, G.B. The interfacial stability of Li with two new solvent-free ionic liquids: 1,2-dimethyl-3-propylimidazolium imide and methide. *J. Electrochem. Soc.* **1995**, *142*, 116–118. [CrossRef]

23. Papageorgiou, N.; Athanassov, Y.; Armand, M.; Bonhote, P.; Pettersson, H.; Azam, A.; Grätzel, M. The Performance and Stability of Ambient Temperature Molten Salts for Solar Cell Applications. *J. Electrochem. Soc.* **1996**, *143*, 3099–3108. [CrossRef]

24. Matsumoto, K.; Endo, T. Design and Synthesis of ionic–conductive epoxy–based networked Polymers. *React. Funct. Polym.* **2013**, *73*, 278–282. [CrossRef]

25. Joo, M.; Shin, J.; Kim, J.; You, J.B.; Yoo, Y.; Kwak, M.J.; Oh, M.S.; Gap, S. One-Step Synthesis of Cross-Linked Ionic Polymer Thin Films in Vapor Phase and Its Application to an Oil/Water Separation Membrane. *J. Am. Chem. Soc.* **2017**, *139*, 2329–2337. [CrossRef] [PubMed]

26. Dou, H.; Jiang, B.; Xiao, X.; Xu, M.; Tantai, X.; Wang, B.; Sun, Y.; Zhang, L. Novel Protic Ionic Liquid Composite Membranes with Fast and Selective Gas Transport Nanochannels for Ethylene/Ethane Separation. *ACS Appl. Mater. Interfaces* **2018**, *10*, 13963–13974. [CrossRef]

27. Yuan, J.; Mecerreyes, D.; Antonietti, M. Poly(ionic liquid)s: An update. *Prog. Polym. Sci.* **2013**, *38*, 1009–1036. [CrossRef]

28. Eshetu, G.G.; Mecerreyes, D.; Forsyth, M.; Zhang, H.; Armand, M. Polymeric ionic liquids for lithium-based rechargeable batteries. *Mol. Syst. Des. Eng.* **2019**, *4*, 294–309. [CrossRef]

29. Matsumoto, K.; Endo, T. Synthesis of Ion Conductive Networked Polymers Based on an Ionic Liquid Epoxide Having a Quaternary Ammonium Salt Structure. *Macromolecules* **2009**, *42*, 4580–4584. [CrossRef]

30. Zhang, W.; Yuan, J. Poly(1-Vinyl-1,2,4-triazolium) Poly(Ionic Liquid)s: Synthesis and the Unique Behavior in Loading Metal Ions. *Macromol. Rapid Commun.* **2016**, *37*, 1124–1129. [CrossRef]

31. McDanel, W.M.; Cowan, M.G.; Chisholm, N.O.; Gin, D.L.; Noble, R.D. Fixed-site-carrier facilitated transport of carbon dioxide through ionic-liquid-based epoxy-amine ion gel membranes. *J. Membr. Sci.* **2015**, *492*, 303–311. [CrossRef]

32. McDanel, W.M.; Cowan, M.G.; Barton, J.A.; Gin, D.L.; Noble, R.D. Effect of Monomer Structure on Curing Behavior, CO₂ Solubility, and Gas Permeability of Ionic Liquid-Based Epoxy–Amine Resins and Ion-Gels. *Ind. Eng. Chem. Res.* **2015**, *54*, 4396–4406. [CrossRef]

33. Nguyen, T.K.L.; Obadia, M.M.; Serghei, A.; Livi, S. 1,2,3-Triazolium-Based Epoxy-Amine Networks: Ion-Conducting Polymer Electrolytes. *Macromol. Rapid Commun.* **2016**, *37*, 1168–1174. [CrossRef]

34. McDanel, W.M.; Cowan, M.G.; Carlisle, T.K.; Swanson, A.K.; Noble, R.D.; Gin, D.L. Cross-linked ionic resins and gels from epoxide-functionalized imidazolium ionic liquid monomers. *Polymer* **2014**, *55*, 3305–3313. [CrossRef]

35. Livia, S.; Lins, L.C.; Capeletti, L.B.; Chardin, C.; Halawani, N.; Baudoux, J.; Cardoso, M.B. Antibacterial surface based on new epoxy-amine networks from ionic liquid monomers. *Eur. Polym. J.* **2019**, *116*, 56–64. [CrossRef]

36. Livi, S.; Chardin, C.; Lins, L.C.; Halawani, N.; Pruvost, S.; Duchet-Rumeau, J.; Gérard, J.-F.; Baudoux, J. From Ionic Liquid Epoxy Monomer to Tunable Epoxy–Amine Network: Reaction Mechanism and Final Properties. *ACS Sustain. Chem. Eng.* **2019**, *7*, 3602–3613. [CrossRef]

37. Radchenko, A.V.; Chabane, H.; Demir, B.; Searles, D.J.; Duchet-Rumeau, J.; Gérard, J.-F.; Baudoux, J.; Livi, S. New Epoxy Thermosets Derived from a Bisimidazolium Ionic Liquid Monomer: An Experimental and Modeling Investigation. *ACS Sustain. Chem. Eng.* **2020**, *8*, 12208–12221. [CrossRef]

38. Dzienia, A.; Tarnacka, M.; Koperwas, K.; Maksym, P.; Zięba, A.; Feder-Kubis, J.; Kamiński, K.; Paluch, M. Impact of Imidazolium-Based Ionic Liquids on the Curing Kinetics and Physicochemical Properties of Nascent Epoxy Resins. *Macromolecules* **2020**, *53*, 6341–6352. [CrossRef]

39. Radchenko, A.V.; Duchet-Rumeau, J.; Gérard, J.F.; Baudoux, J.; Livi, S. Cycloaliphatic epoxidized ionic liquids as new versatile monomers for the development of shape memory PIL networks by 3D printing. *Polym. Chem.* **2020**, *11*, 5475–5483. [CrossRef]

40. Demir, B.; Perli, G.; Chan, K.Y.; Duchet-Rumeau, J.; Livi, S. Molecular-Level Investigation of Cycloaliphatic Epoxidized Ionic Liquids as a New Generation of Monomers for Versatile Poly(Ionic Liquids). *Polymers* **2021**, *13*, 1512. [CrossRef]

41. D. E. Shaw Research. *Materials Science Suite, Desmond*; D.E. Shaw Research, LLC.: New York, NY, USA, 2020.

42. Roos, K.; Wu, C.; Damm, W.; Reboul, M.; Stevenson, J.M.; Lu, C.; Dahlgren, M.K.; Mondal, S.; Chen, W.; Wang, L.; et al. OPLS3e: Extending Force Field Coverage for Drug-Like Small Molecules. *J. Chem. Theory Comput.* 2019, 15, 1863–1874. [CrossRef]

43. Harder, E.; Damm, W.; Maple, J.; Wu, C.; Reboul, M.; Xiang, J.Y.; Wang, L.; Lupyan, D.; Dahlgren, M.K.; Knight, J.L.; et al. OPLS3: A Force Field Providing Broad Coverage of Drug-like Small Molecules and Proteins. *J. Chem. Theory Comput.* 2016, 2, 281–296. [CrossRef]

44. Estridge, C.E. The effects of competitive primary and secondary amine reactivity on the structural evolution and properties of an epoxy thermoset resin during cure: A molecular dynamics study. *Polymer* 2018, 141, 12–20. [CrossRef]

45. Tuckerman, M.; Berne, B.J.; Martyna, G.J. Reversible multiple time scale molecular dynamics. *J. Chem. Phys.* 1992, 97, 1990–2001. [CrossRef]

46. Martyna, G.J.; Klein, M.L.; Tuckerman, M. Nosé–Hoover chains: The canonical ensemble via continuous dynamics. *J. Chem. Phys.* 1992, 97, 2635–2643. [CrossRef]

47. Martyna, G.J.; Tobias, D.J.; Klein, M.L. Constant pressure molecular dynamics algorithms. *J. Chem. Phys.* 1994, 101, 4177–4189. [CrossRef]

48. Patrone, P.N.; Dienstfrey, A.; Browning, A.R.; Tucker, S.; Christensen, S. Uncertainty quantification in molecular dynamics studies of the glass transition temperature. *Polymer* 2016, 87, 246–259. [CrossRef]

49. Shim, Y.; Choi, M.Y.; Kim, H.J. A molecular dynamics computer simulation study of room-temperature ionic liquids. I. Equilibrium solvation structure and free energetics. *J. Chem. Phys.* 2005, 122, 044510. [CrossRef]

50. Chantawansri, T.L.; Yeh, I.-C.; Hsieh, A.J. Investigating the glass transition temperature at the atom-level in select model polyamides: A molecular dynamics study. *Polymer* 2015, 81, 50–61. [CrossRef]

51. Bandyopadhyay, A.; Valavala, P.K.; Clancy, T.C.; Wise, K.E.; Odegard, G.M. Molecular modeling of crosslinked epoxy polymers: The effect of crosslink density on thermomechanical properties. *Polymer* 2011, 52, 2445–2452. [CrossRef]

52. Williams, M.L.; Landel, R.F.; Ferry, J.D. he Temperature Dependence of Relaxation Mechanisms in Amorphous Polymers and Other Glass-Forming Liquids. *J. Am. Chem. Soc.* 1955, 77, 3701–3707. [CrossRef]

53. Lee, A.; McKenna, G.B. Effect of crosslink density on physical ageing of epoxy networks. *Polymer* 1988, 29, 1812–1817. [CrossRef]

54. Garcia, G.; Soares, B.G.; Pita, V.J.R.R.; Sanchez, R.; Rieumont, J. Mechanical properties of epoxy networks based on DGEBA and aliphatic amines. *J. Appl. Polym. Sci.* 2007, 106, 2047–2055. [CrossRef]

55. Vignoud, L.; David, L.; Sixou, B.; Vigier, G. Influence of electron irradiation on the mobility and on the mechanical properties of DGEBA/TETA epoxy resins. *Polymer* 2001, 42, 4657–4665. [CrossRef]

56. Sindt, O.; Perez, J.; Gerard, J.F. Molecular architecture-mechanical behaviour relationships in epoxy networks. *Polymer* 1996, 37, 2989–2997. [CrossRef]

57. Tokuda, H.; Hayamizu, K.; Ishii, K.; Susan, M.A.B.H.; Watanabe, M. Physicochemical Properties and Structures of Room Temperature Ionic Liquids. 2. Variation of Alkyl Chain Length in Imidazolium Cation. *J. Phys. Chem. B* 2005, 109, 6103–6110. [CrossRef]

58. Tokuda, H.; Tsuzuki, S.; Susan, M.A.B.H.; Watanabe, M. How Ionic Are Room-Temperature Ionic Liquids? An Indicator of the Physicochemical Properties. *J. Phys. Chem. B* 2006, 110, 19593–19600. [CrossRef]

59. Xiao, W.; Yang, Q.; Zhu, S. Comparing ion transport in ionic liquids and polymerized ionic liquids. *Sci. Rep.* 2020, 10, 7825. [CrossRef]

60. Mogurampelly, S.; Keith, J.R.; Ganesan, V. Mechanisms Underlying Ion Transport in Polymerized Ionic Liquids. *J. Am. Chem. Soc.* 2017, 139, 9511–9514. [CrossRef]

61. Luo, X.; Liu, H.; Paddison, S.J. Molecular Dynamics Simulations of Polymerized Ionic Liquids: Mechanism of Ion Transport with Different Anions. *ACS Appl. Polym. Mater.* 2021, 3, 141–152. [CrossRef]

62. Kwon, S.J.; Kim, T.; Jung, B.M.; Lee, S.B.; Choi, U.H. Multifunctional Epoxy-Based Solid Polymer Electrolytes for Solid-State Supercapacitors. *ACS Appl. Mater. Interfaces* 2018, 10, 41. [CrossRef]

63. Song, Y.H.; Kim, T.; Choi, U.H. Tuning Morphology and Properties of Epoxy-Based Solid-State Polymer Electrolytes by Molecular Interaction for Flexible All-Solid-State Supercapacitors. *Chem. Mater.* 2020, 32, 3879–3892. [CrossRef]