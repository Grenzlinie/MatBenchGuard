IOP Conference Series: Earth and Environmental Science

PAPER • OPEN ACCESS

# Molecular Simulation of bioalcohol purification in ZIF-1, -3, -7 and -9 frameworks

To cite this article: Xiuying Liu and Junpeng Yuan 2019 *IOP Conf. Ser.: Earth Environ. Sci.* **358** 052069

View the [article online](https://) for updates and enhancements.

---

You may also like

- [Effect of Ammonia on the Electrocatalysis of Oxygen Reduction Reaction in Base](https://)
Reza Abbasi, Huanhuan Wang, Judith R. C. Lattimer et al.

- [Co-Embedded Carbon Nano-Polyhedron Supported on Functionalized Graphene Oxide for Efficient Oxygen Reduction Reaction](https://)
Ziqi Liu, Angela Macedo Andrade, Simranjit Grewal et al.

- [Core–shell Cu@C@ZIF-8 composite: a high-performance electrode material for electrochemical sensing of nitrite with high selectivity and sensitivity](https://)
Feng Gao, Xiaolong Tu, Yongfang Yu et al.

![](./images/812700629603450880_1.jpg)

This content was downloaded from IP address 123.180.255.18 on 29/01/2024 at 11:37

# Molecular Simulation of bioalcohol purification in ZIF-1, -3, -7 and -9 frameworks

Xiuying Liu* and Junpeng Yuan

College of Science, Henan University of Technology, Zhengzhou, Henan, 450000,
China

*Corresponding author's e-mail: liuxiuyingzx@126.com

**Abstract.** Using the Grand Canonical Monte Carlo (GCMC) method, the adsorption properties of ethanol and water on the four ZIFs (ZIF-1, -3, -7 and -9) have been investigated with different conditions. Their storage capacities of pure ethanol and water at different temperatures and pressures have been compared. And the mixture adsorption of ethanol and water and the adsorption selectivity of ethanol over water in these ZIFs have also been investigated. The following conclusions are obtained: (1) the order of the adsorbed amounts of ethanol is ZIF-9>-7>-3>-1 at the same condition. And there are the same trend for water adsorption. (2) ZIF-1 and -3 have preferable selectivity of ethanol over water than ZIF-7 and ZIF-9 owing to the hydrophobic structure of the former.

## 1. Introduction
As a renewable energy source, biofuels are considered as an alternatives to fossil-fuels $^{[1]}$. Bio-ethanol is the most common fuel. However, the presence of water may affect the performance of ethanol, thus the water-free fuel-grade ethanol must be produced $^{[2]}$. Therefore, developing the technologies of separating the water from biofuels is very important for the practical application of biofuels. Among the methods of separating the water-ethanol in biofuels, membrane technology is considered as one of the feasible owing to its advantages of high selectivity and low energy cost $^{[3]}$. Pervaporation and vapor permeation are two typical processes of membrane separation, whose separation factor is mainly determined by the adsorption and diffusion properties of water and ethanol in the membrane.

As a new class of crystalline porous materials, metal-organic frameworks (MOFs) are consisted of inorganic metal or metal oxide unit and organic linkers $^{[4]}$. MOFs have very large diversity caused by changing the metal atoms or the organic linkers, which have great application potentials, such as hydrogen storage $^{[5]}$, carbon dioxide capture $^{[6]}$, sensors $^{[7]}$, and chemical separations $^{[8]}$. Chemically stable MOFs are needed in order to achieve practical applications in organic solvents. However, many Zn- or Cu-based can not meet this requirement. Due to the the strong interaction between metals and azolate linkers relative to carboxylic linkers, several azolated-based MOFs have good thermal and chemical stability $^{[9]}$. Especially, zeolitic-imidazolate frameworks (ZIFs) exhibit exceptional stability $^{[10]}$. Therefore, we have investigated four different ZIFs (ZIF-1, -3, -7, and -9). The adsorption properties of ethanol and water on these four ZIFs have been simulated employing Grand Canonical Monte Carlo (GCMC) method. Moreover, the mixture adsorption of ethanol/water in ZIFs are also investigated at different conditions. These results can reveal the mechanism of adsorption and separation of ethanol/water in ZIFs, which may provide some guideline for synthesizing new materials in experiment.

![](./images/812700629603450880_2.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Published under licence by IOP Publishing Ltd

## 2. Models and computational methods
The atomic structures of ZIF-1, -3, -7, and -9 are illustrated in Fig.1. Lennard-Jones (LJ) and Coulombic potentials represent the framework atoms of ZIFs.

$$
U_{nonbonded} = \sum 4\varepsilon_{ij} \left[ \left( \frac{\sigma_{ij}}{r_{ij}} \right)^{12} - \left( \frac{\sigma_{ij}}{r_{ij}} \right)^6 \right] + \sum \frac{q_i q_j}{4\pi\varepsilon_0 r_{ij}} \tag{1}
$$

Where $\varepsilon_{ij} , \sigma_{ij} , r_{ij} , q_i$ and $\varepsilon_0$ are the well depth, the collision diameter, the distance between atoms $i$ and $j$, the atomic charge of atom $i$ and the permittivity of vacuum, respectively. The atomic charges of ZIF-1, -3, -7, and -9 were calculated using the DFT method. The LJ potentials of MOFs is mimicked by the UFF force field. A united-atom model with each $\text{CH}_x$ as a singe interaction site represents ethanol model. The transferable potentials for the phase equilibria (TraPPE) force field was used to fit the measured critical properties and equilibrium data $^{[11]}$. The three-point transferable interaction potential model (TIP3P) was used to mimic water model $^{[12]}$.

The adsorption isotherms of pure ethanol and water as well as their mixtures were simulated using the GCMC method. The simulation boxes are 2×2×2 supercells for ZIF-1, -3, and 1×1×2 supercells for ZIF-7, -9, respectively. During the simulation, the frameworks were rigid, and the unit cell was divided into fine grids with the potential energies pre-tabulated and subsequently used by interpolation. A spherical cutoff of $12\mathrm{\mathring{A}}$ was evaluated the LJ interactions and the long-range corrections were added beyond the cutoff. The Coulombic interactions was described by Ewald summation. $2×10^7$ steps was moved in a typical simulation, in which the first $10^7$ moves were used for equilibration and the subsequent $10^7$ moves for ensemble averages.

![](./images/812700629603450880_3.jpg)
![](./images/812700629603450880_4.jpg)

ZIF-1
ZIF-3

![](./images/812700629603450880_5.jpg)
ZIF-7

![](./images/812700629603450880_6.jpg)
ZIF-9

Figure 1. Atomic structures of ZIF-1, -3, -7 and -9. Where Zn is orange, Co is purple,
C is cray, N is blue, and H is white.

## 3. Results and discussion

### 3.1. Adsorption of ethanol in MOFs
The adsorption isotherms of the four different ZIFs (ZIF-1, -3, -5, and -9) were simulated using GCMC method, which are shown in Fig.2. Their ethanol storage capacities were compared according to their adsorption uptakes at different temperatures and pressures. As can be seen from Fig.2, with the increase of pressure, the adsorption uptakes gradually increase and achieve to saturation. However, when the temperature decreases, the adsorption amounts increase. The order of uptake is ZIF-9 > -7 > -3 >-1 at both 323K and 373K. Apparently, ethanol adsorption in ZIF-9 and -7 is much stronger than in ZIF-1 and -3. For ZIF-9 and -7 contains nonpolar group $C_6H_4$ and bigger pore volume. Differently, for ZIF-1 and -3, the adsorbed amounts of ethanol at 323K is much larger those at 373K, however, the adsorbed amounts of ethanol are similar at these two temperatures for ZIF-7 and -9. This indicates that ZIF-7 and -9 are more suitable for ethanol adsorption at room temperature or high temperature than ZIF-1 and -3.

### 3.2 .Adsorption of water in MOFs
The adsorption isotherms of water in ZIF-1, -3, -7, and -9 at 323K and 373K with the pressure of 0-100kPa are shown in Fig.3. It can be seen that the water uptake in ZIF-1 and ZIF-3 is nearly zero. However, at a lower pressure, water uptake is negligible but increases sharply above 1Kpa in ZIF-7 and -9. Therefore, ZIF-1 and -3 should be hydrophobic, At the same time, ZIF-7 and -9 should be hydrophilic because of substantial adsorption uptakes. ZIF-9 possesses the highest water uptakes due to its largest free volume.

![](./images/812700629603450880_7.jpg)

Figure 2. The adsorption isotherms of ethanol in ZIF-1, -3, -7, and -9 at 323K and 373K.

![](./images/812700629603450880_8.jpg)

Figure 3. The adsorption isotherms of water in ZIF-1, -3, -7, and -9 at 323K and 373K.

### 3.3 .Mixture adsorption of ethanol and water in MOFs
We also investigated the mixture adsorption of ethanol and water in the ZIF-1, -3, -7, and -9 at 323K and 373K with the pressure range of 0-100kPa. The separation performance is quantified by selectivity [9]

$$
S_{a d(i / j)}=\left(Y_{i} / Y_{j}\right) /\left(X_{i} / X_{j}\right) \tag{2}
$$

Where $Y_{i}$ and $X_{i}$ are the compositions of component $i$ in adsorbed and bulk phase, respectively.

Fig.4 plots the selectivity of ethanol over water in the ZIF-1, -3, -7, and -9 at 323K and 373K. It can be seen that, the selectivity of these four ZIFs has the same trend at both 323K and 373K. That is, with increasing the pressure, the selectivity in each ZIF drops. At a given lower pressure, the selectivity decreases as ZIF-1>ZIF-3>ZIF-7≈ZIF-9. However, at a given higher pressure, the selectivity is in the order of ZIF-3>ZIF-1>ZIF-7≈ZIF-9. Therefore, ZIF-1 and -3 has better separation performance than ZIF-7 and -7, although ZIF-7 and -9 has a preferable adsorption capacity of ethanol.

![](./images/812700629603450880_9.jpg)

Figure 4. The adsorption selectivity of ethanol-water equimolar mixture
in ZIF-1, -3, -7, and 9 at 323K and 373K.

### 4. Conclusions
Adsorption of ethanol/water in ZIF-1, -3, -7 and -9 has been investigated by the GCMC method. The adsorption isotherms of pure ethanol, pure water and ethanol/water mixture in these four ZIFs at different temperatures were obtained. The investigated results show that, compared with ZIF-7 and -9, although ZIF-1 and -3 possess worse adsorption performance of pure ethanol and water, they have better adsorption selectivity of ethanol over water due to their hydrophobic structures.

### Acknowledgments
Authors are grateful to the Science and Technology Research Project of Henan Science and Technology Department (Grant No. 182102410076) and the Foundation for Young Core Teachers of Henan University of Technology (Grant No. hgdqg14028).

### References
[1] Balat, M., Balat, H., Öz, C. (2008) Progress in bioethanol processing. Prog. Energy Combust. Sci., 34: 551–573.
[2] Frolkova, A. K., Raeva, V. M. (2010) Bioethanol dehydration: State of the art. Theor. Found. Chem. Eng., 44: 545-556.
[3] Lipnizki, F. (2010) Membrane process opportunities and challenges in the bioethanol industry. Desalination, 250: 1067-1069.
[4] Long, J. R., Yaghi, O. M. (2009) The pervasive chemistry of meta-organic frameworks. Chem. Soc. Rev., 38: 1213-1214.
[5] Suh, M. P., Park, H. J., Prasad, T. K., Lim, D. -W. (2012) Hydrogen storage in metal-organic frameworks. Chem. Rev., 112: 782-835.
[6] Sumida, K., Rogow, D. L., Mason, J. A., McDonald, T. M., Bloch, E. D., Herm, Z. R., Bae, T.-H., Long, J. R. (2012) Carbon dioxide capture in metal-organic frameworks. Chem. Rev., 112: 724-781.
[7] Kreno, L. E., Leong, K., Farha, O. K., Allendorf, M., Van Duyne, R. P., Hupp, J. T. (2012) Metal-organic framework materials as chemical sensors. Chem. Rev., 112: 1105-1125.

[8] Li, J. -R., Sculley, J., Zhou, H. -C. (2012) Metal-organic frameworks for separations. Chem. Rev., 112: 869-932.

[9] Nalaparaju, A., Zhao, X. S., Jiang, J. W. (2011) Biofuel purification by pervaporation and vapor permeation in metal-organic frameworks: a computational study. Energy Environ. Sci., 4: 2107-2116.

[10] Peralta, D., Chaplais, G., Simon-Masseron, A., Barthelet, K., Chizallet, C., Quoineaud, A. -A., Pirngruber, G. D. (2012) Comparison of the behavior of metal-organic frameworks and zeolites for hydrocarbon separations. J. Am. Chem. Soc., 134: 8115-8126.

[11] Chen, B., Potoff, J. J., Siepmann, J. I. (2001) Monte carlo calculations for alcohols and their mixtures with alkanes. Transferable potentials for phase equilibria. 5. United-atom description of primary, secondary, and tertiary alcohols. J. Phys. Chem. B, 105: 3093-3104.

[12] Jorgensen, W. L., Chandrasekhar, J., Madura, J.D., Impey, R.W., Klein, M. L. (1983) Comparison of simple potential functions for simulating liquid water. J. Chem. Phys., 79: 926-935.