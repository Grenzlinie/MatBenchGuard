# Capillary Phase Transitions of Linear and Branched Alkanes in Carbon Nanotubes from Molecular Simulation

Jianwen Jiang*,† and Stanley I. Sandler‡

Department of Chemical & Biomolecular Engineering, National University of Singapore, 4 Engineering Drive 4, Singapore 117576, and Department of Chemical Engineering, University of Delaware, Newark, Delaware 19716

Received March 31, 2006. In Final Form: May 23, 2006

Capillary phase transitions of linear (from $C_1$ to $C_{12}$) and branched ($C_5$ isomers) alkanes in single-walled carbon nanotubes have been investigated using the gauge-cell Monte Carlo simulation. The isotherm at a supercritical temperature increases monotonically with chemical potential and coincides with that from the traditional grand canonical Monte Carlo simulation, whereas the isotherm at a subcritical temperature exhibits a sigmoid van der Waals loop including stable, metastable, and unstable regions. Along this loop, the coexisting phases are determined using an Maxwell equal-area construction. A generic confinement effect is found that reduces the saturation chemical potential, lowers the critical temperature, increases the critical density, and shrinks the phase envelope. The effect is greater in a smaller diameter nanotube and is greater in a nanotube than in a nanoslit.

## 1. Introduction

Fluids in confined spaces show phase transitions that differ significantly from bulk fluids as a consequence of the spatial confinement and the interaction with the substrate. Understanding confined phase transitions is not only of interest in the physical and surface sciences but of practical importance for a variety of applications.

Historically, the study of fluids in a confined domain dates back to the 18th century. In Opticks,¹ Sir Isaac Newton recorded the rise of a liquid in a capillary tube. The Kelvin equation proposed in the early 1870s,²,³ which relates the vapor pressure of a liquid to the curvature of its meniscus, was first used by Zsigmondy⁴ in 1911 to elucidate capillary condensation. The Kelvin equation is generally applied to infer a tube radius from low-temperature isotherms. However, the Kelvin equation is not accurate in small pores.⁵,⁶ Despite the attempts to extend the applicability of Kelvin equation,⁷ the macroscopic nature prevents its use in nanosized pores.

In the past a few decades, remarkable advances have been achieved in elucidating capillary phase transitions from molecular aspect by statistical mechanics methods. A large number of studies have used the density functional theory (DFT). Evans, Tarazona, and Marconi⁸⁻¹² investigated the capillary condensation of simple fluids in cylindrical and slit pores, and the prewetting transition on a single planar wall. Henderson and Sokolowski¹³ examined the phase behavior of a Lennard-Jones (LJ) fluid confined in spherical cavities and found a shifted transition toward lower density in a smaller cavity. Zgorski et al.¹⁴ calculated the phase behavior of a LJ fluid in a slitlike pore and found that the change in the interaction with surface can lead to a substantial change in the phase behavior compared to the bulk fluid. Salinger and Frink¹⁵,¹⁶ presented three algorithms for the rapid analysis of phase behavior of confined fluids, with a detailed case study in disordered porous media. Patrykiwjew et al.¹⁷ studied the confinement effect of a slit pore on the closed loop immiscibility in symmetric binary model mixtures. Pizio et al.¹⁸ considered the vapor−liquid equilibria (VLE) of the restricted primitive model for ionic fluids within charged and uncharged slit pores. Li et al.¹⁹ examined the layering, condensation, and evaporation of short LJ chains in narrow slits. Bryk et al.²⁰ investigated the capillary condensation of LJ chains confined in slit pores and found anomalous behavior of the critical temperature for long chains. Other theoretical methods have also been used to study the phase transitions in confined media. One example is the replica Ornstein−Zernike integral equation developed by Given and Stell.²¹,²² With this, Pitard et al.²³ predicted the VLE of a lattice gas in disordered porous media, Paschinger et al.²⁴,²⁵ studied the phase separation of a symmetric binary fluid in a porous matrix.

Computer simulations have been widely used to investigate the behavior of confined fluids. With ever-increasing computational power, simulation can provide an improved and detailed

* Corresponding author. E-mail: chejj@nus.edu.sg. Tel: (65) 6516 5083. Fax: (65) 6779 1936.
† National University of Singapore.
‡ University of Delaware.

(1) Newton, I. Opticks, or, a Treatise of the Reflections, Refractions, IrMlections and Colours of Light; London, 1730.
(2) Thomson, W. Proc. R. Soc. Edinburgh 1870, 7, 63.
(3) Thomson, W. Proc. R. Soc. Edinburgh 1871, 42, 448.
(4) Zsigmondy, R. Z. Anorg. Allg. Chem. 1911, 71, 356.
(5) Fisher, L. R.; Israelachvili, J. N. Nature 1979, 277, 548.
(6) Fisher, L. R.; Gamble, R. A.; Middlehurst, J. Nature 1981, 290, 575.
(7) Gregg, S. J.; Sing, K. S. W. Adsorption, Surface Area and Porosity; Academic: London, 1982.
(8) Evans, R.; Tarazona, P. Phys. Rev. Lett. 1984, 52, 557.
(9) Evans, R.; Marconi, U.; Tarazona, P. J. Chem. Phys. 1985, 84, 2376.
(10) Evans, R.; Marconi, U.; Tarazona, P. J. Chem. Soc., Faraday Trans. 2 1986, 82, 1763.
(11) Tarazona, P.; Marconi, U.; Evans, R. Mol. Phys. 1987, 60, 573.
(12) Evans, R. J. Phys. Condens. Matter 1990, 2, 8989.

(13) Henserson, D.; Sokolowski, S. Phys. Rev. E 1995, 52, 758.
(14) Zagorski, R.; Patrykiejew, A.; Sokolowski, S. J. Phys. Condens. Matter 2002, 14, 165.
(15) Salinger, A. G.; Frink, L. J. D. J. Chem. Phys. 2003, 118, 7457.
(16) Frink, L. J. D.; Salinger, A. G. J. Chem. Phys. 2003, 118, 7466.
(17) Patrykiejew, A.; Pizio, O.; Pusztai, L.; Sokolowski, S. Mol. Phys. 2003, 101, 2219.
(18) Pizio, O.; Patrykiejew, A.; Sokolowski, S. J. Chem. Phys. 2004, 121, 11957.
(19) Li, Z. D.; Cao, D. P.; Wu, J. Z. J. Chem. Phys. 2005, 122, 224701.
(20) Bryk, P.; Pizio, O.; Sokolowski, S. J. Chem. Phys. 2005, 122, 194904.
(21) Given, J. A.; Stell, G. Phys. Rev. A 1992, 45, 816.
(22) Given, J. A.; Stell, G. J. Chem. Phys. 1992, 96, 2287.
(23) Pitard, E.; Rosinberg, M. L.; Tarjus, G. Mol. Simul. 1996, 17, 399.
(24) Paschinger, E.; Kahl, G. Phys. Rev. E 2000, 61, 5330.
(25) Paschinger, E.; Levesque, D.; Weis, J.-J. Europhys. Lett. 2001, 55, 178.

10.1021/la0608720 CCC: $33.50
© 2006 American Chemical Society
Published on Web 07/13/2006

microscopic picture of a fluid in the interaction field of a confined space and shed light on the underling physics. Grand canonical Monte Carlo (GCMC) simulation is the most commonly used method to explore adsorption and capillary phenomena in nanoscaled media. $^{26}$ GCMC permits fluid molecule exchange with the reservoir at a given chemical potential, which mimics realistic processes. Using GCMC, Peterson et al. $^{27}$ examined the isotherms, phase diagrams, and density profiles of a LJ fluid in cylindrical pores. Kierlik et al. $^{28}$ considered the liquid-liquid equilibria (LLE) of a LJ fluid mixture in a slit pore. Monson and co-workers $^{29-31}$ located the coexistence curve of a LJ fluid in a xerogel of spherical silica particles. Gelb and Gubbins $^{32}$ investigated the adsorption/evaporation process of Xe and $N_2$ in dynamically quenched porous Vycor glasses. Pellenq and co-workers $^{33,34}$ studied the capillary condensation of rare gases in disordered mesoporous silica media of different morphologies and topologies generated by an off-lattice 3D reconstruction method. Gatica and Cole $^{35}$ simulated the capillary condensation of Ar inside infinitely long cylindrical pores with various gas-surface interaction potentials, and discussed the relation to wetting on planar surfaces.

In some of the above-mentioned GCMC simulations, the coexisting phases were located using a thermodynamic integration method. $^{36}$ Alternatively, a histogram-reweighting technique $^{37}$ has been implemented with GCMC simulation to calculate phase transitions. Alvarez et al. $^{38}$ studied the VLE of a quenched-annealed system. Potoff and Siepmann $^{39,40}$ analyzed the effect of branching on the phase equilibria and critical parameters for alkane monolayers on a flat gold surface. Shi et al. $^{41}$ demonstrated capillary condensation, prewetting, and layering transitions for different systems on surfaces. Grandis et al. $^{42}$ presented a study of the phase diagram of a LJ fluid adsorbed in a fractal and highly porous aerogel generated from an off-lattice diffusion-limited cluster-cluster aggregation process. Hehmeyer et al. $^{43}$ examined the phase transitions and structures of lattice homopolymers of up to 1024 beads in strictly 2D and quasi-2D geometries.

An excellent method to simulate phase transitions in bulk fluids is Gibbs ensemble MC (GEMC) simulation developed by Panagiotopoulos, $^{44}$ in which the coexisting phases are determined directly using two separated simulation boxes. GEMC has also been used for phase transitions in confined space. Panagiotopoulos $^{45}$ first investigated the capillary condensation of fluids in cylindrical pores. Siepmann et al. $^{46}$ studied the VLE coexistence in a Langmuir monolayer of pentadecanoic acid. Jiang and Gubbins $^{47}$ studied the VLE of 2D LJ films, and good agreement with experimental data was obtained. Dijkstra $^{48}$ simulated the VLE of normal pentane between two solid plates and found a shift of the critical temperature to lower temperatures with decreasing plate separation. Vishnyakov et al. $^{49}$ considered the critical properties of LJ fluids in narrow slit-shaped pores and found a linear dependence of the critical temperature with inverse pore width. Brennan and Dong $^{50,51}$ simulated the phase transitions of one-component fluid and binary fluid mixtures in random porous media and analyzed in detail the rich phase behavior. Brovchenko et al. $^{52,53}$ determined the coexistence curves of $H_2O$ in cylindrical and slit nanopores and observed a significant change in the critical parameter and the shape of coexistence curve changing with $H_2O$-substrate interactions. Puibasset $^{54,55}$ examined the capillary condensation of a LJ fluid in heterogeneous pores and suggested that pore disorder has a strong influence on the properties of confined fluid.

Other simulation methods have also been used. Hoffmann and Nielaba $^{56}$ studied the condensation of a LJ fluid in cylindrical pores by path integral MC simulation. Dukovski et al. $^{57}$ examined the coexistence curve and critical point of benzene using a two-replica cluster MC algorithm. By means of molecular dynamics simulation, Heinz et al. $^{58}$ reported the phase transitions and structures of alkyl chains on alkylammonium micas. Koga and Tanak $^{59}$ presented the phase transitions among liquid, bilayer, and monolayer ice phases between hydrophobic slit surfaces.

Recently, the gauge-cell MC simulation method has been developed by Neimark and Vishnyakov $^{60,61}$ to investigate the phase transitions of Ar and $N_2$ in smooth nanopores. This method can be used to simulate the complete isotherm, including stable, metastable, and unstable regions, and as a result, the coexisting phases can be determined easily. The key feature is that thermodynamically unstable states, which cannot be observed in experiment, are stabilized in simulation by suppressing density fluctuations. Gauge-cell MC simulation has been adapted in a few studies of capillary phase transitions. Seaton and co-workers $^{62,63}$ investigated the phase coexistence of $H_2O$ and $CH_4$ in slit pores. Jiang et al. $^{64}$ simulated the capillary transition of short linear alkanes (from $C_1$ to $C_4$) in a single-walled carbon nanotube (SWNT). Kowalczyk et al. $^{65}$ examined the condensation/evaporation pressures of $N_2$ in SWNTs and sequentially evaluated the distribution of carbon nanotube sizes in a sample.

In this work, our previous study $^{64}$ has been extended to long linear (up to $C_{12}$) and branched ($C_5$ isomers) alkanes in three SWNTs using the gauge-cell MC. Currently it is of intense interest

(26) Nicholson, D.; Parasonage, N. G. *Computer Simulation and the Statistical Mechanics of Adsorption*; Academic Press: New York, 1982.

(27) Peterson, B. K.; Gubbins, K. E.; Heffelfinger, G. S.; Marconi, U.; Swol, F. v. *J. Chem. Phys.* **1988**, 88, 6487.

(28) Kierlik, E.; Fan, Y.; Monson, P. A.; Rosinberg, M. L. *J. Chem. Phys.* **1995**, 102, 3712.

(29) Page, K. S.; Monson, P. A. *Phys. Rev. E* **1996**, 54, R29.

(30) Page, K. S.; Monson, P. A. *Phys. Rev. E* **1996**, 54, 6557.

(31) Sarisov, L.; Monson, P. A. *Langmuir* **2000**, 16, 9857.

(32) Gelb, L. D.; Gubbins, K. E. *Langmuir* **1998**, 14, 2097.

(33) Pellenq, R. J.-M.; Levitz, P. E. *Mol. Phys.* **2002**, 100, 2059.

(34) Coasne, B.; Pellenq, R. J.-M. *J. Chem. Phys.* **2004**, 121, 3767.

(35) Gatica, S. M.; Cole, M. W. *Phys. Rev. E* **2005**, 72, 041602.

(36) Peterson, B. K.; Gubbins, K. E. *Mol. Phys.* **1987**, 62, 215.

(37) Ferrenberg, A. M.; Swendsen, R. W. *Phys. Rev. Lett.* **1988**, 61, 2635.

(38) Alvarez, M.; Levesque, D.; Weis, J.-J. *Phys. Rev. E* **1999**, 60, 5495.

(39) Potoff, J. J.; Siepmann, J. I. *Phys. Rev. Lett.* **2000**, 85, 3460.

(40) Potoff, J. J.; Siepmann, J. I. *Langmuir* **2002**, 18, 6088.

(41) Shi, W.; Zhao, X. C.; Johnson, J. K. *Mol. Phys.* **2002**, 100, 2139.

(42) Grandis, V. D.; Gallo, P.; Rovere, M. *Phys. Rev. E* **2004**, 70, 061505.

(43) Hehmeyer, O.; Ayra, G.; Panagiotopoulos, A. Z. *J. Phys. Chem. B* **2004**, 108, 6809.

(44) Panagiotopoulos, A. Z. *Mol. Phys.* **1987**, 61, 813.

(45) Panagiotopoulos, A. Z. *Mol. Phys.* **1987**, 62, 701.

(46) Siepmann, J. I.; Karaborni, S.; Klein, M. L. *J. Phys. Chem.* **1994**, 98, 6675.

(47) Jiang, S.; Gubbins, K. E. *Mol. Phys.* **1995**, 86, 599.

(48) Dijkstra, M. *J. Chem. Phys.* **1997**, 107, 3277.

(49) Vishnyakov, A.; Piotrovakaya, E. M.; Brodakaya, E. N.; Votyakov, E. V.; Tobvin, Y. K. *Langmuir* **2001**, 17, 4451.

(50) Brennan, J. K.; Dong, W. *J. Chem. Phys.* **2002**, 116, 8948.

(51) Brennan, J. K.; Dong, W. *Phys. Rev. E* **2003**, 67, 031503.

(52) Brovchenko, I.; Geiger, A.; Oleinikova, A. *J. Chem. Phys.* **2004**, 120, 1958.

(53) Brovchenko, I.; Geiger, A.; Oleinikova, A. *J. Chem. Phys.* **2005**, 123, 044515.

(54) Puibasset, J. *J. Phys. Chem. B* **2005**, 109, 4700.

(55) Puibasset, J. *J. Chem. Phys.* **2005**, 122, 134710.

(56) Hoffmann, J.; Nielaba, P. *Phys. Rev. E* **2003**, 67, 036115.

(57) Dukovski, I.; Machta, J.; Saravanan, C.; Auerbach, S. M. *J. Chem. Phys.* **2000**, 113, 3697.

(58) Heinz, H.; Castelijns, H. J.; Suter, U. W. *J. Am. Chem. Soc.* **2003**, 125, 9500.

(59) Koga, K.; Tanaka, H. *J. Chem. Phys.* **2005**, 122, 104711.

(60) Neimark, A. V.; Vishnyakov, A. *Phys. Rev. E* **2000**, 62, 4611.

(61) Vishnyakov, A.; Neimark, A. V. *J. Phys. Chem. B* **2001**, 105, 7009.

(62) Jorge, M.; Seaton, N. A. *Mol. Phys.* **2002**, 100, 3803.

(63) Jorge, M.; Schumacher, C.; Seaton, N. A. *Langmuir* **2002**, 18, 9296.

(64) Jiang, J. W.; Sandler, S. I.; Smit, B. *Nano Lett.* **2004**, 4, 241.

(65) Kowalczyk, P.; Holyst, R.; Tanaka, H.; Kaneko, K. *J. Phys. Chem. B* **2005**, 109, 14659.

<table>
<caption>Table 1. Force Field Parameters for Linear and Branched Alkanes</caption>
<tbody>
<tr>
<td>nonbonded LJ⁶⁸,⁶⁹</td>
<td>site</td>
<td>σ (Å)</td>
<td>ϵ/k_B (K)</td>
</tr>
<tr>
<td>
</td>
<td>CH₄</td>
<td>3.73</td>
<td>148.0</td>
</tr>
<tr>
<td>
</td>
<td>CH₃</td>
<td>3.75</td>
<td>98.0</td>
</tr>
<tr>
<td>
</td>
<td>CH₂</td>
<td>3.95</td>
<td>46.0</td>
</tr>
<tr>
<td>
</td>
<td>CH</td>
<td>4.68</td>
<td>10.0</td>
</tr>
<tr>
<td>
</td>
<td>C</td>
<td>6.40</td>
<td>0.5</td>
</tr>
<tr>
<td>bending⁷⁰</td>
<td colspan="3">$k_\theta/k_\text{B}=62500$ K/rad² $\theta_0=113.0^o$</td>
</tr>
<tr>
<td>torsion⁷¹</td>
<td>CHₓ−CH₂−CH₂−CHᵧ</td>
<td colspan="2">CHₓ−CH₂−CH−CHᵧZ</td>
</tr>
<tr>
<td>
</td>
<td>$v_0/k_\text{B}=1009.728$ K</td>
<td colspan="2">$v_0/k_\text{B}=373.0512$ K</td>
</tr>
<tr>
<td>
</td>
<td>$v_1/k_\text{B}=2018.446$ K</td>
<td colspan="2">$v_1/k_\text{B}=919.0441$ K</td>
</tr>
<tr>
<td>
</td>
<td>$v_2/k_\text{B}=136.341$ K</td>
<td colspan="2">$v_2/k_\text{B}=268.1541$ K</td>
</tr>
<tr>
<td>
</td>
<td>$v_3/k_\text{B}=-3164.520$ K</td>
<td colspan="2">$v_3/k_\text{B}=-1737.2160$ K</td>
</tr>
</tbody>
</table>

to determine the applicability of SWNTs as adsorbents, membranes, molecular sieves, and filtering media because of their unique internal nanometric structure. Although there has been considerable literature on fluid adsorption in carbon nanotubes, far less explored are the phase transitions. The fluids under this study, alkanes, are the basic feedstock in chemical industry, and a better understanding of their phase transitions in confined environments would be useful for their storage and in elucidating their behavior in nanoporous catalysis and elsewhere. The phase transitions of three C₅ isomers in a carbon nanoslit have also been simulated here in order to investigate the effect of pore geometry. For comparison with the gauge-cell MC, GCMC was also used to determine the adsorption and desorption isotherms of C₁ in a SWNT. In addition, GEMC was used to calculate the coexistence curves of bulk C₅ isomers. In section II, we briefly introduce the models used for alkanes, SWNTs, and nanoslit, as well as the interaction potentials used. In section III, the gauge-cell MC, GCMC, and GEMC simulation methods are described. Results are presented in section IV, including isotherms, phase coexistence curves, and fluid structures within SWNT. Finally, concluding remarks are given in section V.

### 2. Models

Two prototypes are commonly adapted to represent alkane molecules, the united-atom model and the all-atom model.⁶⁶ Both models were found to give comparable adsorption isotherms for alkane adsorption in silicalite; however, the simpler united-atom model is computationally faster.⁶⁷ Consequently, the united-atom model, representing every CHₓ group as a single interaction site, was used in this work. The C−C bonds were assumed to be rigid and fixed at 1.53 Å.

The nonbonded dispersive interactions between sites of different molecules and four sites apart within a molecule were modeled using the Lennard-Jones (LJ) potential⁶⁸,⁶⁹

$$
u_{\text{LJ}}(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^6] \tag{1}
$$

For C₃ and longer alkanes, the intramolecular bond bending between three successive sites was modeled using a harmonic potential⁷⁰

$$
u_{\text{bending}}(\theta)=0.5k_\theta(\theta-\theta_0)^2 \tag{2}
$$

For C₄ and longer alkanes, the intramolecular dihedral torsion between four successive sites was modeled using a cosine potential⁷¹

$$
u_{\text{torsion}}(\phi)=\sum_{k=0}^{3}v_k(\cos\phi)^k \tag{3}
$$

Table 1 gives the force field parameters, as optimized by others to accurately reproduce experimental vapor−liquid coexistence curves and critical properties of pure linear and branched alkanes. The cross LJ parameters between the unlike sites were obtained using the Jorgensen combining rules $\sigma_{ij}=(\sigma_i\sigma_j)^{1/2}$ and $\epsilon_{ij}=(\epsilon_i\epsilon_j)^{1/2}$.⁷²

Three arm-chair type $(m,\ m)$ SWNTs were considered separately with $m=30,\ 25$, and 20. Each SWNT was open-ended, 30.74 Å in length, and $1.23\sqrt{3}m/\pi$ in radius. By using the periodic boundary condition in the axial dimension, the SWNT was thereby considered to be infinitely long in the simulations. Note that experimentally produced SWNTs are closed-ended and need to be uncapped to obtain open-ended SWNTs. We assume that the extent of impurities introduced during this process are rather small, and well structured open-ended nanotubes can be obtained. The carbon atoms in each SWNT were taken into account fully atomistically, different from some previous studies which used simplified smooth structureless cylindrical nanopores. During the simulation, the SWNT was assumed to be rigid with carbon atoms frozen. As our study focused on low-energy equilibrium configurations, flexibility of the SWNT allowing local small movements of the carbon atoms would not be expected to give significantly different results. The nonbonded dispersion between the carbon atom in SWNT and the alkane interaction site was also modeled using the LJ potential. The well depth and collision diameter were obtained using the Jorgensen combining rule⁷² with $\epsilon_{\text{C−C}}/k_\text{B}=28.0$ K and $\sigma_{\text{C−C}}=3.4$ Å. A spherical cutoff length of 15.37 Å was used for the calculation of the LJ interaction energies without additional long-range corrections.

For comparison, the capillary phase transitions of alkanes in a carbon nanoslit with a width of 40.68 Å, identical to the diameter of a (30,30) SWNT, was investigated. The carbon nanoslit was modeled as two graphitic basal surfaces separated by a width $w$ in the $z$ dimension. The length of the slit surface in the $x$ or $y$ dimension was assumed to be 40 Å. The periodic boundary conditions were employed in the transverse $xy$ plane parallel to the slit surface. The nonbonded dispersion between a slit surface and an alkane site was modeled using the Steele 10−4−3 potential⁷³,⁷⁴

$$
\begin{aligned}
u_{\text{sa}}(z)=2\pi\rho_{\text{s}}\epsilon_{\text{sa}}\sigma_{\text{sa}}^2\Delta\Bigg[\frac{2}{5}\bigg(\frac{\sigma_{\text{sa}}}{z}\bigg)^{10}-\bigg(\frac{\sigma_{\text{sa}}}{z}\bigg)^4-\\
\bigg(\frac{\sigma_{\text{sa}}^4}{3\Delta(0.61\Delta+z)^3}\bigg)\Bigg],\ (4)
\end{aligned}
$$

where $z$ is the distance from the slit surface, $\rho_{\text{s}}=0.114$ Å⁻³ is the implicit carbon number density of the slit surface, $\epsilon_{\text{sa}}$ and $\sigma_{\text{sa}}$ are the cross interaction well depth and collision diameter

(66) Ryckaert, J. P.; Bellemans, A. *Faraday Discuss. Chem. Soc.* **1978**, 66, 95.
(67) Macedonia, M. D.; Maginn, E. J. *Fluid Phase Equilib.* **1999**, 158−160, 19.
(68) Martin, M. G.; Siepmann, J. I. *J. Phys. Chem. B* **1998**, 102, 2569.
(69) Martin, M. G.; Siepmann, J. I. *J. Phys. Chem. B* **1999**, 103, 4508.
(70) van der Ploeg, P.; Berendsen, H. J. C. *J. Chem. Phys.* **1982**, 76, 3271.
(71) Wang, Y.; Hill, K.; Harris, J. G. *J. Chem. Phys.* **1993**, 100, 3276.
(72) Jorgensen, W. L.; Madura, J. D.; Swenson, C. J. *J. Am. Chem. Soc.* **1984**, 106, 6638.
(73) Steele, W. A. *Chem. Rev.* **1993**, 93, 2355.
(74) Steele, W. A. *The Interaction of Gases with Solid Surfaces*; Pergamon: Oxford, 1974.

![](./images/812071931959312385_1.jpg)

Figure 1. $C_1$ isotherms in a (30, 30) SWNT at 120, 140, 160, and 180 K. The open circles are from gauge-cell MC, the solid circles connected by dashed lines are the coexisting phases. The upward and downward triangles are for adsorption and desorption, respec- tively, from GCMC. The dot-dashed lines indicate capillary condensation and evaporation, respectively, from GCMC.

estimated from the Jorgensen combining rule, $^{72}$ and $\Delta=3.35$ Å is the intersheet distance of graphite. Equation 4 was derived by integrating LJ pair potential over graphene sheets. $^{73,74}$ The overall interaction potential of an alkane site within the slit pore is $u_{sa}(z)+u_{sa}(w-z)$ . As a consequence, the atomic corrugations on graphene sheets are not taken into account; however, their effects on adsorption and phase transition within the slit pore are expected to be negligible.

### 3. Methods
The gauge-cell MC uses two simulation boxes, each of which has a fixed volume. In this work, one box was embedded with a SWNT or a nanoslit, and the other was a gauge cell of $50 \times$  $50 ×50(\AA)^{3}$ for bulk alkane with periodic boundary conditions in all three directions. In this respect, the gauge-cell MC is an NVT ensemble. The limited capacity of the gauge cell restrains the density fluctuations in the pore and allows the fluid in the pore in stable, metastable, or unstable state. As mentioned, GCMC was also used to determine the adsorption isotherm of $C_{1}$ , andGEMC was used to determine the coexistence curves of bulk $C_{5}$  isomers. All three types of simulations ran separately for a total20 000 cycles, in which the first 10 000 cycles were used for equilibration and the second 10 000 cycles to obtain ensembleaverages. Each cycle consisted of a number of the following attempted trial moves:

(a) Translation. A randomly selected alkane molecule was translated with a random displacement in the x, y, or z direction, and the maximum displacement was adjusted to an overall acceptance ratio of $50 \%$ .
(b) Rotation. A randomly selected alkane molecule was rotated around the center-of-mass with a random angle, and the maximum angle was adjusted to an overall acceptance ratio of $50 \%$ .
(c) Partial regrowth. Part of a randomly selected alkane molecule was regrown. Also, it was randomly decided which part of the molecule was to be regrown and from which bead the regrowth was started.
(d) Complete regrowth. A randomly selected alkane molecule was regrown completely at a random position.
(e) Swap between two boxes (only in gauge-cell MC and GEMC). A randomly selected alkane molecule was swapped into the other box at a random position. This type of trial move is in analogy to the Widom test particle method, from which the chemical potential of the fluid in the gauge cell was estimated simultaneously. This procedure is faster than previous gauge- cell simulations, $^{60,61}$ in which the chemical potential in the gauge cell was determined from a series of separated GCMC simulations.
(f) Exchange with the reservoir (only in GCMC). A new alkane molecule was created at a random position, or a randomly selected alkane molecule was deleted. To ensure microscopic reversibility, creation and deletion were attempted at random with equal probability.
(g) Volume change (only in GEMC). While the total volume of the two boxes was kept constant, a small volume change in either box was performed, and the maximum change was adjusted to an overall acceptance ratio of $50 \%$ .

In the gauge-cell MC method, each cycle consisted of 5000 trial moves (a, b, c, d, and e) with the relative probabilities of $10 \%$ translation, $10 \%$ rotation, $10 \%$ partial regrowth, $10 \%$  complete regrowth, and $60 \%$ swap. In GCMC, each cycle consisted of 2000 trial moves (a, b, c, d, and f) with the relative probabilities of $10 \%$ translation, $10 \%$ rotation, $10 \%$ partial regrowth, $10 \%$ complete regrowth, and $60 \%$ exchange with the reservoir. In GEMC, each cycle consisted of 5000 trial moves(a, b, c, d, e, and g) with the relative probabilities of $10 \%$  translation, $10 \%$ rotation, $10 \%$ partial regrowth, $10 \%$ complete regrowth, $55 \%$ exchange with the reservoir, and $5 \%$ volume change. Within the statistical uncertainty, the simulation results were found to be independent of the sequence of the trial moves.

The traditional Metropolis MC algorithms are prohibitively expensive in sampling the conformations of long alkane molecules. To accelerate this process, the configurational-bias algorithm $^{75-77}$ has been incorporated into the gauge-cell MC, GCMC, and GEMC simulations. The configurational-bias algorithm is used in simulations of chainlike molecules and has been widely adopted in MC simulations of phase transitions and adsorption of alkanes and polymers. $^{78-84}$ It is orders of magnitude more efficient than the traditional algorithm, in which it is attempted to grow randomly the entire molecule at once. Instead of inserting a molecule at a random position, in the configura- tional-bias algorithm, a molecule is grown site-by-site, biasing energetically favorable configurations while avoiding overlap with other atoms, and the bias is then removed by adjusting the acceptance rules. $^{85}$ In current work, eight trial positions werefirst generated with a probability proportional to $\exp (-\beta$  $U_{internal }^{i}$ ), where $\beta=1 / k_{B} T$ and $U_{internal }^{i}$ is the internal energy at a position i including the intramolecular bond bending and dihedral torsion interactions. One of the trial positions was then chosenfor growing an atom with a probability proportional to $\exp (-\beta$  $U_{external }^{i}) / \sum_{i} \exp (-\beta U_{internal }^{i})$ , where $U_{internal }^{i}$ is the external energy including all nonbonded intramolecular and intermolecular Lennard-Jones interactions. Also, the insertion of molecules was enhanced using the multiple first-bead scheme with fifteen trialpositions. $^{86}$

(75) Siepmann, J. I.: Frenkel, D. Mol. Phys, 1992. 75. 59.
(76) Frenkel, D.; Mooij, G. C. A. M.; Smit, B. J. Phys.. Condensed Matter1992,4,3053.
(77) de Pablo, J. J.; Laso, M.; Suter, U. W. J. Chem. Phys. 1992, 96, 2395.
(78) Siepmann, J. I.; Karaborni, S.; Smit, B. Nature 1993, 365, 330.
(79) Smit, B.: Siepmann. J. I. Science 1994. 264.1118
(80) Smit, B.; Maesen, T. L. M. Nature 1995, 374, 42.
(81) Jiang, J. W.; Yan, Q. L.; Liu, H. L.; Hu, Y. Macromolecules 1997, 30,8459
(82) Jiang. J. W.; Liu, H. L.; Hu, Y. Macromol. Theory Simul. 1998, 7, 105.
(83) Jiang, J. W.; Sandler, S. I.; Schenk, M.; Smit, B. Phys. Rev. B 2005, 72,045447.
(84) Jiang, J. W.: Sandler, S. I. J. Chem, Phys, 2006, 124, 024717.
(85) Frenkel, D.; Smit, B. Understanding Molecular Simulations: From algorithms to applications, 2nd ed.; Academic Press: San Diego, CA, 2002.
(86) Esselink, K.; Loyens, L. D. J. C.; Smit, B. Phys. Rev. E 1995, 51, 1560.

![](./images/812071931959312385_2.jpg)

Figure 2. Saturation chemical potentials of confined and bulk $C_1$.
The solid curves are for confined $C_1$ from gauge-cell MC in (30,
30), (25, 25), and (20, 20) SWNTs, the dashed curve is for bulk $C_1$
predicted from the MBWR equation of state for LJ fluids.⁹³

## Results

Figure 1 shows the isotherms of $C_1$ in a (30, 30) SWNT at 120,
140, 160, and 180 K, respectively. The horizontal axis $\beta\mu^c$ is the
dimensionless configurational chemical potential defined as $\beta\mu^c$
$= \beta\mu - \ln \Lambda^3$, and $\Lambda$ is the de Broglie wavelength. The extent
of adsorption is given by the overall alkane density $\Gamma=2\int_0^R \rho(r)r$
$dr/R^2$ inside the SWNT of radius $R$, where $\rho(r)$ is the local density
at a radial position $r$. The open circles are simulation results from
the gauge-cell MC. At a low temperature, say, 120 K, the isotherm
exhibits a sigmoidal van der Waals loop, which is the signature
of a first-order phase transition, well-known since van der Waals.⁸⁷
A similar loop has been observed for the capillary condensation
of LJ fluids in nanopores predicted by canonical DFT⁸⁸ and for
the confinement-induced phase transition of surfactant layers
predicted by Scheutjens-Fleer theory.⁸⁹ The coexisting vapor–
liquid phases are determined along the isotherm using a Maxwell
equal area construction

$$
\int_{\mu_{\mathrm{V}}}^{\mu_{\mathrm{S}_{\mathrm{V}}}} \Gamma_{\mathrm{A}}(\mu) \mathrm{d} \mu-\int_{\mu_{\mathrm{S}_{\mathrm{L}}}}^{\mu_{\mathrm{S}_{\mathrm{V}}}} \Gamma_{\mathrm{S}}(\mu) \mathrm{d} \mu+\int_{\mu_{\mathrm{S}_{\mathrm{L}}}}^{\mu_{\mathrm{L}}} \Gamma_{\mathrm{D}}(\mu) \mathrm{d} \mu=0
\tag{5}
$$

where V and L are vapor and liquid equilibrated phases at a
saturation chemical potential of $\mu_{\mathrm{V}}=\mu_{\mathrm{L}}$, $S_{\mathrm{V}}$ and $S_{\mathrm{L}}$ are vapor
and liquid spinodals. In this figure, the AV and DL regions are
stable, the $\mathrm{VS_V}$ and $\mathrm{LS_L}$ regions are metastable, and the $\mathrm{S_VS_L}$
region is unstable. The coexisting phases of $C_1$ at 120, 140, and
160 K so determined are shown in Figure 1, and the binodal
curve is shown as the solid line for $C_1$ confined in the (30, 30)
SWNT. However, at 180 K, the isotherm is monotonic with
increasing chemical potential, and no van der Waals loop appears.
This suggests that 180 K is above the critical temperature of $C_1$
in the (30, 30) SWNT.

GCMC simulations were carried out, and the upward and
downward triangles are shown in Figure 1 for adsorption and
desorption, respectively. At 120, 140, and 160 K, irreversible
capillary condensation and evaporation (dot–dashed lines) are
clearly observed from the GCMC simulation with an IUPAC
classified H1 type hysteresis.⁹⁰ This type of hysteresis is the
signature of phase transition in ordered cylindrical pores open
at both ends, as observed experimentally in mesoporous silicas
MCM-41 and SBA-15 with a regular array of cylindrical pores.⁹¹
However, the experimental sample may contain pores with a
wide distribution of sizes and has complex topology and
connectivity. Consequently, the hysteresis behavior may be
smeared out or not visible. The microscopic origin of hysteresis
and its relation with pore structure is currently an issue of debate.
The hysteresis associated with the mechanism of pore filling–
draining is regarded as a consequence of a metastable state, an
important aspect of a first-order phase transition.⁹² The coexisting
phases determined using the gauge-cell MC are between the
capillary condensation and evaporation, i.e., inside the hysteresis
loop. Though the phase transition is located within the hysteresis
loop, to determine the exact position from GCMC is very difficult.
With a very long GCMC run, the hysteresis loop might vanish
so that the phase transition points could be determined. The
salient feature of the gauge-cell MC method is that the phase
transition points can be determined easily from the complete
isotherm.

In the stable regions AV and DL, and part of the metastable
regions $\mathrm{VS_V}$ and $\mathrm{LS_L}$ where GCMC can be used, it gives identical
results to those obtained with the gauge-cell MC. However,
GCMC cannot access the unstable region $\mathrm{S_VS_L}$. As anticipated,
the hysteresis loop obtained from GCMC shrinks in size with
increasing temperature from 120 to 140 K and then again at 160
K. At 180 K, the GCMC results do not exhibit hysteresis, in
agreement with the gauge-cell MC results, further verifying that
there is no phase transition at 180 K and that the critical
temperature of $C_1$ confined in this SWNT is below 180 K. Above
the capillary critical temperature, the isotherm is reversible,
indicating that the distinction between the vapor and condensed
liquid phases disappears.

Figure 2 shows the saturation chemical potentials of confined
$C_1$ in three SWNTs evaluated from the gauge-cell MC and of
bulk $C_1$ calculated from the MBWR equation of state for LJ
fluids.⁹³ This equation of state has been fitted to simulated data
and very accurately reproduces the phase behavior and $pVT$ data
of LJ fluids. In either the SWNT or the bulk phase, the chemical
potential increases (becomes less negative) as temperature rises.
Compared to the bulk phase, the chemical potential in a SWNT

![](./images/812071931959312385_3.jpg)

Figure 3. Phase diagrams of confined and bulk $C_1$. The solid curves
are the binodals of confined $C_1$ simulated from gauge-cell MC in
(30, 30), (25, 25), and (20, 20) SWNTs, the dashed and dot–dashed
lines are the binodal and spinodal curves, respectively, of the bulk
$C_1$ predicted from the MBWR equation of state for LJ fluids.⁹³ The
squares and crosses are the coexisting phases of bulk $C_1$ from GEMC⁶⁸
and from experiment,⁹⁴ respectively.

(87) van der Waals, J. D. *Over de continuiteit van den gas- en vloeistoftoestand*;
University of Leiden, 1873.
(88) Neimark, A. V.; Ravikovitch, P. I.; Vishnyakov, A. *J. Phys.-Condensed
Matter* **2003**, *15*, 347.
(89) Koopal, L. K.; Leermakers, F. A. M.; Lokar, W. J.; Ducker, W. A. *Langmuir*
**2005**, *21*, 10089.
(90) Rouquerol, F.; Rouquerol, J.; Sing, K. *Adsorption: By Powders and
Porous Solids*; Academic Press: London, 1999.
(91) Grosman, A.; Ortega, C. *Langmuir* **2005**, *21*, 10515.
(92) Gelb, L. D.; Gubbins, K. E.; Radhakrishnan, R.; Sliwinska-Bartkowiak,
M. *Rep. Prog. Phys.* **1999**, *62*, 1573.
(93) Johnson, J. K.; Zollweg, J. A.; Gubbins, K. E. *Mol. Phys.* **1993**, *78*, 591.

![](./images/812071931959312385_4.jpg)

Figure 4. Radial density profiles of $C_1$ in a (30, 30) SWNT at 120 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, 0.240, 0.288, and 0.336 (g/mL).

![](./images/812071931959312385_5.jpg)

Figure 5. Snapshots of $C_1$ in a (30, 30) SWNT at 120 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, 0.240, 0.288, and 0.336 (g/mL). The arrow at the top illustrates the process from gauge-cell MC. The arrows at the bottom illustrate the processes of GCMC for adsorption and desorption, respectively, with the dot−dashed lines indicating the inaccessible regions.

is more negative, showing that the occurrence of phase separation in a confined geometry occurs at a pressure lower than the bulk saturation pressure. With decreasing SWNT diameter, the chemical potential decreases, i.e., the saturation pressure is even lower.

Figure 3 shows the phase diagrams of confined and bulk $C_1$. The gauge-cell MC was used for confined $C_1$ in three SWNTs. For bulk $C_1$, results from GEMC, $^{68}$ the MBWR equation of state, $^{93}$ and the experiment $^{94}$ are plotted in the figure with good mutual agreement. Also shown is the spinodal of bulk $C_1$ predicted from the MBWR equation of state. $^{93}$ The binodal of $C_1$ confined in the (20, 20) SWNT is inside the binodals in the (25, 25) and (30, 30) SWNTs and all are inside the binodal and spinodal of the unconfined bulk $C_1$. Consequently, confinement shrinks the phase envelope, and the effect in a small SWNT is greater than in a large SWNT. The region within the spinodal of the unconfined $C_1$ is unstable, and a phase transition would occur. However, if $C_1$ is confined in a SWNT, the unstable region becomes much smaller, and part of the region unstable for the unconfined $C_1$ is a stable state in the SWNT. This phenomenon may have relevance in the processing and storage of natural gas, in which the major component is $C_1$, and also in interpreting data from nanoporous catalysts.

With the gauge-cell MC, we were not able to simulate coexisting phases very close to the critical point due to the large density fluctuations thereby. Sophisticated algorithms have been proposed to create and destroy large clusters rather than individual particles in order to sample large fluctuations. $^{95}$ In this work, we simply used

$$
\Gamma_{ \pm}=\Gamma_{\mathrm{c}}+A\left(T_{\mathrm{c}}-T\right) \pm 0.5 B\left(T_{\mathrm{c}}-T\right)^{\beta} \tag{6}
$$

based on the renormalization-group theory $^{96}$ to estimate the critical temperature $T_{\mathrm{c}}$ and critical density $\Gamma_{\mathrm{c}}$ by fitting the coexisting phases, where the $+$ sign is for the liquid phase and the $-$ sign is for the vapor phase. The amplitudes $A$ and $B$ and the critical exponent $\beta$ are the adjustable parameters. The uppermost point of each curve in Figure 3 indicates the critical point. Compared to the bulk phase, the capillary $T_{\mathrm{c}}$ in the SWNT is consistently lower, whereas $\Gamma_{\mathrm{c}}$ is higher. The shift of the critical point from that of the bulk phase becomes greater with decreasing SWNT radius. The observed shift in the critical point upon confinement is generic. When a fluid is confined by a surface, the overall fluid−fluid intermolecular attraction becomes weaker since the number of neighbors is reduced; this leads to a lower $T_{\mathrm{c}}$. Moreover, from the figure, the shift in $T_{\mathrm{c}}$ with SWNT radius was found to obey a scaling law

$$
\Delta T_{\mathrm{c}} \propto R^{-y} \tag{7}
$$

with the scaling exponent $y=1.9$, in close agreement with the experimentally determined $y=2.1$ for $\mathrm{SF}_{6}$ in interconnected

![](./images/812071931959312385_6.jpg)

Figure 6. Radial density profiles of $C_1$ in a (30, 30) SWNT at 180 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, and 0.240 (g/mL).

![](./images/812071931959312385_7.jpg)

Figure 7. Snapshots of $C_1$ in a (30, 30) SWNT at 180 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, and 0.240 (g/mL). The arrow at the top illustrates the process from gauge-cell MC. The arrows at the bottom illustrate the processes of adsorption and desorption, respectively, from GCMC.

(94) Smith, B. D.; Srivastava, R. *Thermodynamic Data for Pure Compounds*; Elsevier: Amsterdam, 1986.

(95) Auerbach, S. M. *Int. Rev. Phys. Chem.* **2000**, *19*, 155.

(96) Sengers, J. V.; Sengers, J. M. H. L. In *Progress in Liquid Physics*; Croxton, C. A., Ed.; Wiley: Cichester, U.K., 1978; p 103.

![](./images/812071931959312385_8.jpg)

Figure 8. Isotherms of $n$-alkanes $\text{C}_2$, $\text{C}_3$, $\text{C}_4$, $\text{C}_5$, $\text{C}_8$, and $\text{C}_{12}$ in a (30, 30) SWNT. Legend as in Figure 1.

![](./images/812071931959312385_9.jpg)

Figure 9. Binodal curves of confined and bulk linear alkanes $\text{C}_1$, $\text{C}_2$, $\text{C}_3$, $\text{C}_4$, $\text{C}_5$, $\text{C}_8$, and $\text{C}_{12}$. The solid curves with circles are for confined $n\text{C}_n$ in a (30, 30) SWNT from gauge-cell MC, and the dotted curves with squares are for bulk $n\text{C}_n$ from GEMC.⁶⁸

![](./images/812071931959312385_10.jpg)

Figure 10. Ratios of the critical density and critical temperature of linear alkanes in a (30, 30) SWNT to those in bulk.

cylindrical controlled-pore-glass materials.⁹⁷ In slitlike pores, a similar scaling relation was theoretically predicted but with $y = 1.59$ for large slits and $y = 1$ for small slits.¹²

It is generally accepted that a true phase transition does not occur at any nonzero temperatures in an infinite one-dimensional (1D) system with finite-ranged interactions.⁹⁸ This scenario seems applicable to fluid confined in a SWNT as the latter is a 1D nanostructure in the axial direction. However, the SWNT being considered here is sufficiently large, and several alkane molecules can fit in the cross section of the SWNT as will be shown in Figures 5 and 7. Therefore, the confined alkane here is rigorously not an 1D system. In addition, the SWNT in our simulation is finite in length without the periodic images, and the finite-size effect can lead to sharp phase transition between two states of distinctly different densities and structures.⁹⁹ However, we expect that phase transition will not occur in a rather small SWNT. Realistically, fluid molecules cannot enter into an extremely small SWNT.⁸⁴

Figure 4 shows the radial density profiles of $\text{C}_1$ in a (30, 30) SWNT at 120 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, 0.240, 0.288, and 0.336 (g/mL). At the lowest density, the preferred location of $\text{C}_1$ molecules is in a single annular layer near the SWNT wall. With increasing density, the number of layers increases with each subsequent layer being closer to the SWNT center, and the peak in density profile in each layer also increases. At the highest density, there are up to five layers. Figure 5 shows the snapshots of $\text{C}_1$ molecules in these systems obtained by accumulating 50 widely spaced equilibrium configurations (the SWNT is not shown). The solid line and arrow above the snapshots are to indicate that gauge-cell MC can simulate the complete isotherm including the stable, metastable, and unstable regions. The arrows and lines below the snapshots represent the adsorption and desorption processes, respectively, that can be accessed by GCMC. The dot−dashed portions of the

(97) Findenegg, G. H.; Thommes, M. High-Pressure Physisorption of Gases on Planar Surfaces and in Porous Materials. In Physical Adsorption: Experiment, Theory and Applications; Fraissard, J., Ed.; Kluwer Academic Publishers: The Netherlands, 1997; p 151.

(98) Landau, L. D.; Lifshitz, E. M. Statistical Physics I; Pergamon: New York, 1980.

(99) Privman, V.; Fisher, M. E. J. Stat. Phys. 1983, 33, 385.

![](./images/812071931959312385_11.jpg)

Figure 11. Binodal curves of confined and bulk $n$C$_5$, $i$C$_5$, and $neo$C$_5$. The circles and diamonds are for confined C$_5$ in a (30, 30) SWNT and a nanoslit from gauge-cell MC, the squares are for bulk C$_5$ from GEMC, and the dashed curves are for bulk C$_5$ from experiments.$^{102-104}$

<table>
 <thead>
  <tr>
   <th colspan="5">
    Table 2. Critical Temperatures and Densities of $n$C$_n$ in a (30, 30) Nanotube and Bulk Phase
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
   </td>
   <th colspan="2">
    (30,30) SWNT
   </th>
   <th colspan="2">
    bulk$^{68}$
   </th>
  </tr>
  <tr>
   <th>
    $n$C$_n$
   </th>
   <th>
    $T_{\text{c}}$ (K)
   </th>
   <th>
    $\Gamma_{\text{c}}$ (g/mL)
   </th>
   <th>
    $T_{\text{c}}$ (K)
   </th>
   <th>
    $\Gamma_{\text{c}}$ (g/mL)
   </th>
  </tr>
  <tr>
   <td>
    C$_1$
   </td>
   <td>
    169.8
   </td>
   <td>
    0.200
   </td>
   <td>
    191.4
   </td>
   <td>
    0.160
   </td>
  </tr>
  <tr>
   <td>
    C$_2$
   </td>
   <td>
    270.0
   </td>
   <td>
    0.264
   </td>
   <td>
    304
   </td>
   <td>
    0.206
   </td>
  </tr>
  <tr>
   <td>
    C$_3$
   </td>
   <td>
    322.7
   </td>
   <td>
    0.289
   </td>
   <td>
    368
   </td>
   <td>
    0.221
   </td>
  </tr>
  <tr>
   <td>
    C$_4$
   </td>
   <td>
    365.5
   </td>
   <td>
    0.311
   </td>
   <td>
    423
   </td>
   <td>
    0.231
   </td>
  </tr>
  <tr>
   <td>
    C$_5$
   </td>
   <td>
    402.7
   </td>
   <td>
    0.322
   </td>
   <td>
    470
   </td>
   <td>
    0.238
   </td>
  </tr>
  <tr>
   <td>
    C$_8$
   </td>
   <td>
    485.9
   </td>
   <td>
    0.340
   </td>
   <td>
    570
   </td>
   <td>
    0.239
   </td>
  </tr>
  <tr>
   <td>
    C$_{12}$
   </td>
   <td>
    553.2
   </td>
   <td>
    0.356
   </td>
   <td>
    667
   </td>
   <td>
    0.235
   </td>
  </tr>
 </tbody>
</table>

lines indicate those regions inaccessible by GCMC. Consequently, from GCMC, one is unable to access states with three and four annular layers along either the adsorption or desorption path. Capillary condensation or evaporation is commonly regarded as a secondary process, which is always preceded by adsorption or desorption, and a hysteresis loop usually appears in the multilayer range of a physisorption isotherm. All of these feature are observed here in the sequence of simulation snapshots.

Figure 6 shows the radial density profiles of C$_1$ in a (30, 30) SWNT at 180 K and adsorbed densities of 0.048, 0.096, 0.144, 0.192, and 0.240 (g/mL). Analogous to the results at 120 K, the most preferred location of C$_1$ molecules is in a single annular layer near the SWNT wall, and the number of layers increases upon increased density with each subsequent layer being closer to the SWNT center. However, here the layers are less distinct and the peaks are smaller because of the enhanced thermal motion. Figure 7 shows the snapshots of these same systems at 180 K showing that the distribution of C$_1$ molecules is more dispersed than at 120 K. Because 180 K is above the critical temperature of the capillary phase transition, the gauge-cell MC and GCMC give the same results, and the complete isotherm and a series of snapshots can be obtained by both simulation methods.

Figure 8 shows the isotherms of linear alkanes (C$_2$, C$_3$, C$_4$, C$_5$, C$_8$, and C$_{12}$) at various temperatures in a (30, 30) SWNT from the gauge-cell MC. For each alkane, at a low temperature, the complete isotherm shows a van der Waals loop, from which the vapor−liquid coexisting phases were estimated; above the critical temperature, the isotherm does not have a van der Waals loop.

Figure 9 shows the binodal curves of confined and bulk linear alkanes (C$_1$, C$_2$, C$_3$, C$_4$, C$_5$, C$_8$, and C$_{12}$). The circles are the confined alkanes obtained from gauge-cell MC, and the squares are the bulk alkanes from GEMC.$^{68}$ As we could not simulate the coexisting phases close to the critical point, the critical parameters were estimated by fitting to the coexisting phases away from the critical point. Table 2 lists the estimated critical temperatures and densities of C$_1$−C$_{12}$ in a (30, 30) SWNT and in the bulk. Compared to the bulk, the confined fluid has a critical temperature that is consistently lower, a critical density that is higher, and binodal curve that is narrower.

<table>
 <thead>
  <tr>
   <th colspan="6">
    Table 3. Critical Temperatures and Densities of C$_5$ Isomers in a (30, 30) Nanotube, a Nanoslit, and Bulk Phase
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
   </td>
   <th colspan="2">
    (30,30) SWNT
   </th>
   <th colspan="2">
    nanoslit
   </th>
   <th colspan="2">
    bulk$^{102-104}$
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    $T_{\text{c}}$ (K)
   </th>
   <th>
    $\Gamma_{\text{c}}$ (g/mL)
   </th>
   <th>
    $T_{\text{c}}$ (K)
   </th>
   <th>
    $\Gamma_{\text{c}}$ (g/mL)
   </th>
   <th>
    $T_{\text{c}}$ (K)
   </th>
   <th>
    $\Gamma_{\text{c}}$ (g/mL)
   </th>
  </tr>
  <tr>
   <td>
    $n$C$_5$
   </td>
   <td>
    402.7
   </td>
   <td>
    0.322
   </td>
   <td>
    424.0
   </td>
   <td>
    0.354
   </td>
   <td>
    469.7
   </td>
   <td>
    0.237
   </td>
  </tr>
  <tr>
   <td>
    $i$C$_5$
   </td>
   <td>
    391.6
   </td>
   <td>
    0.329
   </td>
   <td>
    422.1
   </td>
   <td>
    0.352
   </td>
   <td>
    460.4
   </td>
   <td>
    0.235
   </td>
  </tr>
  <tr>
   <td>
    $neo$C$_5$
   </td>
   <td>
    376.7
   </td>
   <td>
    0.334
   </td>
   <td>
    398.5
   </td>
   <td>
    0.358
   </td>
   <td>
    433.8
   </td>
   <td>
    0.232
   </td>
  </tr>
 </tbody>
</table>

Figure 10 shows the ratios of the critical parameters (density and temperature) of linear alkanes (C$_1$, C$_2$, C$_3$, C$_4$, C$_5$, C$_8$, and C$_{12}$) in a (30, 30) SWNT relative to those in bulk. The ratio of nanotube-to-bulk critical density increases and the ratio of critical temperature decreases as a function of carbon number. Two linear relations were used to correlate these trends

$$
\Gamma_{\mathrm{c}}^{\text{nanotube}}/\Gamma_{\mathrm{c}}^{\text{bulk}} = 1.2385 + 0.0236N_{\mathrm{c}} \tag{8}
$$

$$
T_{\mathrm{c}}^{\text{nanotube}}/T_{\mathrm{c}}^{\text{bulk}} = 0.8916 - 0.0053N_{\mathrm{c}} \tag{9}
$$

where $N_{\text{c}}$ is the carbon number of the alkane molecule. From these, the critical parameters of longer linear alkanes in the (30, 30) SWNT can be predicted approximately. We expect that similar trends with different values may be found for linear alkanes in other SWNTs.

The phase transitions of three C$_5$ isomers in a carbon nanoslit of $w = 40.68$ Å were simulated to investigate the difference from those in a (30, 30) SWNT which has a diameter of 40.68 Å. Figure 11 shows the binodals of $n$C$_5$, $i$C$_5$, and $neo$C$_5$ in the SWNT, nanoslit, and bulk, with the corresponding critical temperatures and densities listed in Table 3. Whether in the SWNT, the nanoslit, or the bulk, the critical densities of the three isomers are close in value, but $n$C$_5$ has the highest critical temperature and $neo$C$_5$ has the lowest. Due to configurational variations, the linear $n$C$_5$ is the most densely packed, whereas the branched $neo$C$_5$ is the least densely packed among the three isomers. Consequently, $n$C$_5$ has the strongest self-interactions and hence the highest critical temperature. This also suggests that the minimal surface area of a spherical structure results in weaker van der Waals attractive forces between fluid molecules compared to an elongated isomer structure. Such a branching effect is well demonstrated in the normal boiling temperatures of bulk C$_5$ isomers (309.2, 301.1, and 282.6 K, respectively, for $n$C$_5$, $i$C$_5$, and $neo$C$_5$).$^{94}$ Monte Carlo simulation of lattice homopolymers$^{100}$ and experimental study of star polystyrenes$^{101}$ reveal a similar effect. For each isomer, the critical temperature

(100) Arya, G.; Panagiotopoulos, A. Z. Macromolecules 2005, 38, 10596.
(101) Alessi, M. L.; Bittner, K. C.; Greer, S. C. J. Polym. Sci. B 2004, 42, 129.

in the SWNT is lower than in the nanoslit, and both are lower than in the bulk. For a cylindrical SWNT with a diameter of $2R$, the ratio of surface area to volume is $2/R$; for a nanoslit with a width of $2R$, the ratio is $1/R$; for bulk, there is no surface, and therefore, the ratio is 0. The smaller this ratio, the weaker the pore effect, and the less the shift of the phase boundary from the bulk. As already shown in Figure 3, with an increased SWNT radius and consequently a smaller ratio of surface area to volume, the confined phase behavior gradually approaches that of the bulk fluid.

## 5. Conlusions

We have investigated the capillary phase transitions of linear and branched alkanes in nanopores. Using the gauge-cell MC simulation, not only are the complete isotherms over stable, metastable, and unstable regions obtained, but also the coexisting phases are determined easily. In the regions where GCMC is applicable, consistent results with the gauge-cell MC are obtained.

(102) Das, T. R.; Reed, C. O.; Eubank, P. T. *J. Chem. Eng. Data* **1977**, 22, 3.
(103) Das, T. R.; Reed, C. O.; Eubank, P. T. *J. Chem. Eng. Data* **1977**, 22, 9.
(104) Das, T. R.; Reed, C. O.; Eubank, P. T. *J. Chem. Eng. Data* **1977**, 22, 16.

The capillary phase transition can be regarded as a surface-driven phase transition at a lower saturation pressure than the bulk fluid. Due to geometry constraints and surface interactions, the critical point in a confined space is shifted from the bulk phase with a lowered critical temperature, an increased critical density, and a shrunken binodal curve. The effect of confinement can be qualitatively characterized by the ratio of the surface area to volume of the nanopores. The larger this ratio, the stronger the effect.

The gauge-cell MC used in this work can be extended further to study phase transitions in 3D porous media, such as nanotube bundles, porous glasses, aerogels, zeolites, etc. Note that for 3D periodic structures, the application of GEMC is formidable, in which the volume change of the simulation boxes leads to the destruction of periodicity. However, GCMC can still be used in conjugation with the thermodynamic integration or histogram-reweighting technique.

**Acknowledgment.** Support from the National University of Singapore to J.J. and from the U.S. Department of Energy and U.S. National Science Foundation to S.I.S. is graciously acknowledged.

LA0608720