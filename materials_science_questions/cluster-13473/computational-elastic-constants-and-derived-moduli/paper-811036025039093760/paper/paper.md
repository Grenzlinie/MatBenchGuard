![](./images/811036025039093760_1.jpg)

# Free energy of steps at faceted (111) solid-liquid interfaces in the Si-Al system calculated using capillary fluctuation method

P. Saidi ${ }^{a, *}$, R. Freitas ${ }^{b, c}$, T. Frolov ${ }^{c}$, M. Asta ${ }^{b}$, J.J. Hoyt ${ }^{a}$

${ }^{a}$ Department of Materials Science and Engineering, McMaster University, Hamilton, ON, Canada
${ }^{b}$ Department of Materials Science and Engineering, University of California, Berkeley, CA 94720, USA
${ }^{c}$ Lawrence Livermore National Laboratory, Livermore, CA 94550, USA

## ARTICLE INFO

Article history:
Received 6 February 2017
Received in revised form 23 March 2017
Accepted 24 March 2017

Keywords:
Step free energy
Molecular dynamics
Al-Si
AEAM

## ABSTRACT

Molecular-dynamics simulations using interatomic potentials of the angular embedded atom method form have been performed on the Al-Si system to compute the excess free energy of steps on the (111) solid-liquid interface. The solid-liquid step free energy was obtained by monitoring equilibrium fluctuations in the step position for Si solids in contact with Al-Si liquids of compositions Al-87.4at.%Si and Al-59.4at.%Si at two step orientations, [1 1 $\overline{2}]$ and $[\overline{1} 10]$. No anisotropy in the step free energy was observed for these two alloying systems, and also, the step free energy for the high concentration and high temperature $87 \%$ Si alloy was found to be greater than that of the Al-59.4% alloy. For the low temperature case of Al-30at.%Si the capillary fluctuation method can no longer be applied to extract the step free energy due to smoothness of the steps.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

The mechanical properties of casting and welding products depend significantly on the dendritic microstructure and morphology and the motion of crystal-melt interfaces is a key process in microstructural evolution. Therefore, the thermodynamics and kinetics of interfaces are of both fundamental and practical importance. The microscopic solvability theory of dendrite growth predicts [1,2], that a dendrite tip radius and growth velocity are sensitive functions of the anisotropy in the crystal-melt interfacial free energy, $\gamma$, as well as the kinetic coefficient. The crystal-melt interfacial free energy, defined as the reversible work required to form a unit area of interface between a crystal and a coexisting fluid, has been the subject of many studies for rough interfaces.

Direct experimental measurements of crystal-melt free energy are quite difficult and relatively few in number [3]. They typically involve contact angle studies and, with the exception of a small number of studies on transparent organic materials [4,5], are not precise enough to capture anisotropy. This inherent difficulty associated with direct experimental measurements motivated the development of a variety of novel computational methods to determine $\gamma$ via molecular simulation. These methods include ab initio computations [6], classical nucleation theory based models [7,8], free energy integration method [9,10], cleaving wall molecular dynamics simulation method [11-13] and analysis of equilibrium capillary fluctuations in interfacial position for complicated molecules [14], grain boundaries [15] pure metals [16-21], binary [22-25] and ternary [26] alloying systems.

In the classification of interfaces, beside the rough interface, where atom attachment to the growing phase occurs readily at any point on the boundary, faceted interfaces form some energetically favourable sites for adatoms. These smooth interfaces are identified by the presence of immobile terraces separated by steps of roughly atomic height. This type of system has been addressed in a very few studies [27,28]. Buta et al. [27] used nonequilibrium MD simulations of crystal growth to calculate the step kinetic coefficient at crystal melt interfaces, as well as the effect of step separation on the kinetic coefficient. Frolov and Asta [28] used a classical nucleation theory based model for two dimensional nucleation of silicon liquid pools to calculate the step free energies, $\gamma$, at faceted crystal-melt interfaces from equilibrium MD simulations. In both of these studies, the Stillinger-Weber (SW) [29] potential has been used to approximate the interactions between silicon atoms. However, Frolov and Asta [28] observed that the SW Si potential solidifies in the wurtzite crystal structure, rather than the experimentally observed diamond cubic structure. They suggested that wurtzite formation might be due to the lower step free energy of the wurtzite crystal structure compared to that of the diamond cubic crystal structure. Beaucage and Mousseau

* Corresponding author.
E-mail address: saidip@mcmaster.ca (P. Saidi.)

http://dx.doi.org/10.1016/j.commatsci.2017.03.044
0927-0256/© 2017 Elsevier B.V. All rights reserved.

[30] have reported the formation of a random mixture of stacking sequences of crystalline silicon layers during solidification using SW as well. In order to solve this problem Saidi et al. [31] extended the cut off distance of the pair interaction in the original SW up to the third nearest neighbour and stabilized the diamond crystal structure with respect to the wurtzite crystal structure.

Systems that include chemically dissimilar components are another class of systems that, despite their technological importance, have been considered in relatively few fundamental studies [32,33]. This gap in understanding is more significant for alloy systems exhibiting mixed bonding types, such as metallic and covalently bonded species. In mixed bonding systems the main difficulty is the lack of a reliable interatomic potential model to include all types of interactions, as well as an accurate description of cross species interaction. However, in 2009, Dongare et al. [34] developed the angular-EAM (AEAM) interatomic potential model, which is specifically designed to model alloys of a metal species combined with covalently bonded materials such as silicon. Using this model, Saidi et al. [31] developed a potential for the case of Al-Si, which reproduces quite accurately the phase diagram with almost zero solubility of either component for the solid phases at the Al-rich and Si-rich ends of the phase diagram, which is an important feature of this alloying system. Using this potential they predicted the kinetic coefficient of silicon steps [35].

In the present study we employ equilibrium molecular dynamics (MD) simulations, the AEAM based Al-Si potential and the capillary-fluctuations method (CFM) to calculate crystal-melt step free energies at three different melt compositions. The anisotropy of the step energy is investigated by setting up systems with different crystal orientations of steps on the high-symmetry interface plane, (1 1 1) in this case. Using these results, we identify the range of composition and temperature where steps are smooth and the capillary fluctuation method for computing step stiffnesses breaks down.

### 2. Methodology of atomistic simulation

In the CFM, step free energies are derived through an analysis of equilibrium step-height fluctuations obtained from MD simulations for coexisting crystal-melt system that includes an active step. This method is based on the relationship between the static height-fluctuation spectrum of a rough step and its effective Hamiltonian [36].

$$
\left\langle\left|A\left(k_{\mathrm{n}}\right)\right|^{2}\right\rangle=\frac{k_{\mathrm{B}} T_{\mathrm{Eq}}}{l_{\mathrm{step}}\left(\gamma+\gamma^{\prime \prime}\right) k_{\mathrm{n}}^{2}} \tag{1}
$$

where $A(k_{\mathrm{n}})$ is the Fourier amplitude of the step height fluctuation with wave number $k_{\mathrm{n}}=\frac{2 \pi n}{l_{\mathrm{step}}}$, where for even counter $N$, $n=-N / 2+1,-N / 2, \ldots,-1,0,1, \ldots, N / 2$, $k_{\mathrm{B}}$ is Boltzmann constant, $T_{\text {Eq }}$ is the equilibrium temperature of coexistence of crystal and melt at the composition of interest and $l_{\text {step }}$ is the length of the system in the direction of the step. The term $(\gamma+\gamma^{\prime \prime})$ corresponds to the step stiffness, where $\gamma^{\prime \prime}$ is the second derivative of step effective Hamiltonian as a function of the angle between the instantaneous and average step normal.

In this study the interactions between the components of the Al-Si system are approximated by the (AEAM) empirical potential developed by Saidi et al. [31]. In order to prepare systems with an active step at coexistence of a pure silicon crystal in contact with an alloying liquid, a non-orthogonal box is considered which is periodic in three dimensions. A non-orthogonal coordinate system allows us to prepare the system in such a way that the component of stress in the step plane remains zero and thus does not affect the fluctuation of the step. Fig. 1 shows the crystal and melt and two interfaces, each one including one active step. The $xz$ plane of simulation box is tilted around the step axes in a way that guarantees a displacement at the periodic image is equal to the height of the step $(h)$. System preparation starts with the equilibration of pure silicon in the solid state using the NPT ensemble at the desired temperature $T$ and pressure $P=0$. After equilibration of the system, the identity of some atoms, which are meant to be in the liquid state, changes to reach the corresponding composition of the liquid in contact with solid silicon crystal. The liquid region develops in a way that two steps form. The output of this level of simulation is used as the initial condition for the subsequent simulations. In the next level an $NA_{xz}P_{y}T$ ensemble is employed, which means that the system size is fixed in the $x$ and $z$ directions parallel to the interface, and the pressure is controlled by changes in the $y$, ([1 1 1]), direction normal to the interface.

![](./images/811036025039093760_2.jpg)

Fig. 1. Illustration of the geometry of the simulation cells employed in CFM calculations of the step free energies. Si atoms are coloured blue and Al atoms, which appear in the liquid only, are red. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Table 1 shows the list of the systems which were considered in this study. Three liquid compositions at three temperatures dictated by the phase diagram were selected. For each temperature, steps are designed in two orientations, $[\overline{1} 10]$ and $[11 \overline{2}]$. The time step of the simulations were 1 fs and snapshots of the systems were saved every 50 ps during this simulation. 200 snapshots were saves for each system, which contained positions of atoms, energies, and stresses, and used for post processing.

In order to capture the fluctuations of the step, we need to determine the position of the interface between crystal and melt. Therefore the state of all atoms in the system are determined using the order parameter proposed by Buta [27] for diamond crystal structures. This criterion is based on the symmetry of the second neighbour atoms of each individual atom and four first nearest neighbours. The discrimination function $\psi(i)$ of an atom $i$ defined as:

$$
\psi(i)=\left|\frac{1}{Z N_{\mathbf{q}}} \sum_{\mathbf{q}_{i}} \sum_{j=1}^{Z} \exp \left(-i \mathbf{q}_{i} \cdot \mathbf{r}_{j}\right)\right|^{2} \tag{2}
$$

where $Z$ is the number of neighbouring atoms found in a sphere of radius $2.8 \AA$ surrounding atom $i$. $\mathbf{r}_{j}$ is the vector from atom $i$ to the immediate $N_{\mathbf{q}}=12$ atoms found within the cut-off distance of first nearest neighbours, and $\mathbf{q}_{i}$ are the reciprocal lattice of the second nearest neighbours in a perfect diamond cubic crystal structure. By design, $\psi(i)=1$ for a perfect diamond crystal structure and $\psi(i) \approx 0$ for an atom in a liquid phase. The accuracy of the discrimination factor is improved by calculating the average order parameter $\bar{\psi}$ for each atom with the order parameter of the $Z$ nearest neighbours. Fig. 2 shows the atoms coloured based on their state and type. 2(a) is the illustration of a simulation box where a silicon crystal (blue part) is in contact with the melt on two sides where yellow particles represent silicon in liquid state and red particles are aluminium. Fig. 2(b)-(d) are snapshots of atomic planes

<table><thead><tr><th>Liquid composition</th><th>Step direction</th><th>$l_{step}$ (Å)</th><th>$l_{z}$ (Å)</th><th>$l_{[111]}$ (Å)</th><th>$N_{atoms}$</th><th>Temperature (K)</th></tr></thead><tbody><tr><td>Al-87.4at.%Si</td><td>$[\overline{1}10]$</td><td>92.65</td><td>142.66</td><td>113.48</td><td>73704</td><td>1570</td></tr><tr><td>Al-87.4at.%Si</td><td>$[11\overline{2}]$</td><td>133.74</td><td>92.65</td><td>113.48</td><td>69,120</td><td>1570</td></tr><tr><td>Al-59.4at.%Si</td><td>$[\overline{1}10]$</td><td>92.65</td><td>142.66</td><td>113.48</td><td>73,704</td><td>1230</td></tr><tr><td>Al-59.4at.%Si</td><td>$[11\overline{2}]$</td><td>133.74</td><td>92.65</td><td>113.48</td><td>69,120</td><td>1230</td></tr><tr><td>Al-30at.%Si</td><td>$[\overline{1}10]$</td><td>92.65</td><td>142.66</td><td>113.48</td><td>73,704</td><td>920</td></tr><tr><td>Al-30at.%Si</td><td>$[11\overline{2}]$</td><td>133.74</td><td>92.65</td><td>113.48</td><td>69,120</td><td>920</td></tr></tbody></table>

Table 1
Compositions, dimensions, temperature and orientations of the MD simulation systems. $l_{step}$ is the length of the system along the steps, $l_{z}$ is the length of simulation cell in the direction of the step fluctuations. $l_{[111]}$ is the initial length of the simulation box in the [111] direction perpendicular to the interface plane, which changes during solidification. The number of the atoms in each system is "$N_{atoms}$". The composition of the liquid and the temperature of interest are chosen based on the Al-Si phase diagram for the AEAM potential.

![](./images/811036025039093760_3.jpg)

Fig. 2. (a) Structure of steps visualized according to the order parameter described in Eq. (2). Blue particles are Si in solid state. Yellow atoms are Si in liquid state and red ones are Al atoms. (b-d) Snapshots are plan views of (111) layers containing a step where the melt includes 30%, 59.4% and 87.4% silicon, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

containing individual steps in contact with melt with compositions Al-30at.%Si, Al-59.4at.%Si and Al-87.4at.%Si respectively.

Results of the order parameter calculation during fluctuation of steps shows that small solid islands on the melt side of the interface and puddles of liquid in the crystalline step are identified. These local regions are not stable for more than 1 ps. The solid islands melt very quickly while the liquid puddles solidify. Therefore, in a subsequent step in the post processing analysis, the bilayer active steps are separated and the state of these local parts are modified in order to avoid the errors associated to these local defects in the calculation of step position. Different steps of this procedure are depicted in Fig. 3.

Fig. 3(a) shows a section of the slab from the view perpendicular to a step after applying the discrimination factor to each atom. The domain is divided into discrete counterparts. Discrete domains are rectangles with the side size of $0.8a$ and $0.5a$ along and perpendicular to the step, respectively, where $a$ is the lattice parameter of silicon in diamond crystal structures. This size guarantees that there is at least one atom in each domain and that it is smaller perpendicular to the step direction, which allows a more precise determination of interface position. As shown in Fig. 3(b) the state of each domain is determined based on the average order parameters of all atoms contained in the domain. Here domains are considered solid if the average discriminator value is more than 0.2 and the domain is reassigned the value of 1 (red $^{1}$ in Fig. 3(b)). The remaining domains are assigned a value of 0 and correspond to the liquid phase. The threshold of $\psi(i)>0.2$ guarantees that the appropriate state assigns to all atoms including the silicon atoms at the crystal/melt interface, which have a number of broken bonds [35].

The procedure for eliminating the "defects" in the solid and liquid consists of three steps. First, starting from the solid side of the system (lower left corner of the system), an integer ID is assigned to each domain where the integers increase from left to right and from bottom to top. Then the state of each domain, starting from the smallest ID, is checked. If a given domain is in the liquid state but the neighbouring regions with smaller IDs are in the solid state, the state of the respective region is changed to solid. The result of this modification is shown in Fig. 3(c) and the elimination of the liquid "puddles" within the continuous solid is clear. The above algorithm is then applied to the top (liquid) side of the system, where new IDs are assigned, starting in the top-right corner, and eliminates solid islands from the continuous liquid region; solid islands are changed based on neighbouring liquid regions with lower IDs. The results of this second step are shown in Fig. 3(d). Fig. 3(e) shows the merged output of the two separate algorithms, which was obtained as follows. If there was no state change in b to c or b to d, then the state did not change. If liquid became solid from b to c, then solid was assigned to that region for part e. Similarly, if solid became liquid from b to d, then liquid was assigned to that region for part e. Notice in panel e there still remains "overlap" atoms along the solid-liquid interface. Therefore, in the final step of the analysis, each column of domains is traversed (top to bottom) until first crossing into a solid domain, establishing the interfacial position. In this way all horizontal branches are eliminated. The final position of the interface mapped from the original atoms position and atoms state is shown in Fig. 3(f).

After calculating the position of the interface, the amplitudes $A(k_{n})$ are obtained through a Fourier transform of the interface location. This is performed for each snapshot and the results are time averaged to obtain $\langle|A(k_{n})|^{2}\rangle$. A fit of $\langle|A(k_{n})|^{2}\rangle$, versus $\frac{1}{k_{n}^{2}}$ is then used to derive values for the step stiffness.

$^{1}$ For interpretation of colour in Fig. 3, the reader is referred to the web version of this article.

![](./images/811036025039093760_4.jpg)

Fig. 3. Preparation of step profiles suitable for CFM analysis involved several steps. (a) Atoms belonging to solid and liquid phases were identified according to the order parameter described in Eq. (2). (b) Discretizing the domain and determining the state of each counterpart based on the average order parameter of the involved atoms. (c) Removing isolated liquid puddles inside the solid terrace by analyzing the state of the neighbouring counterparts in a way that a continuous solid part without liquid puddles forms. (d) Removing isolated solid islands inside the liquid according to the state of the neighbouring counterparts so that a continuous liquid part without solid islands forms. (e) Utilizing the continuous parts of last two steps as the liquid and the solid parts (f) Altering the state of the horizontal branches in each column of counterparts and determining the exact position of the interface in the corresponding column.

## 3. Results and discussions

Fig. 4 shows the fluctuation spectra, $\langle|A(k_{\mathrm{n}})|^{2}\rangle I_{\text{step}}$ vs $k_{\mathrm{n}}$, on a log-log scale for (a) Al-59.4at.%Si and (b) Al-87.4at.%Si. Results include both $[\overline{1}10]$ and $[11\overline{2}]$ step orientations. Standard errors for the quantity $\langle|A(k_{\mathrm{n}})|^{2}\rangle$ are also shown by the error bars in the graphs. The solid lines in these graphs represent slopes of $-2$, which is the value predicted by Eq. (1). For almost all cases the curves show a levelling off for small values of $k_{\mathrm{n}}$.

One of the advantages of the CFM is its application to determine the anisotropy in $\gamma$ to a higher precision than is possible in other methods, including cleaving. This is due to the fact that the CFM determines directly the interfacial stiffness, $\gamma+\gamma''$, which is much more anisotropic than $\gamma$ itself. For a weakly anisotropic system and steps with a three fold symmetry, the relationship between the stiffness with $\theta$, the angle between the normal to the interface and some fixed crystalline axis (e.g. [100]), follows the form $\gamma+\gamma''=\gamma_{0}(1-\epsilon\cos3\theta)$. In this study two independent stiffness value are measured to parameterize $\gamma$. The calculated stiffness are presented in Table 2. Using these results we find coefficient $\epsilon<0.03$, as the measure of the anisotropy. Considering the standard deviation in the calculation of stiffness, which is about 6%, the values calculated for different orientations are equal within statistical uncertainty. In other words, the step free energy is invariant with respect to direction.

Fig. 5 illustrates the effect of composition on the slope of the fit and the fluctuation spectra. The results indicate that the CFM can predict successfully the stiffness of the steps in the Al-59.4at.%Si and Al-87.4at.%Si alloys. Using adiabatic trapping approach, Frolov and Asta [28] computed the value of $1.03\pm0.05\times10^{-11}$ (J/m) for the step free energy of pure silicon. Based on the results of this study we conclude that the step free energy increases with decreasing temperature and/or increasing concentration of Al in the liquid. Previous studies have indicated that the excess free energy of rough solid-liquid interfaces is to a large extent of entropic origin [37] and increases with increasing temperatures [38]. Note the opposite behaviour with temperature is observed here, which suggests that the role of Al additions is playing a crucial role in the free energy of steps.

However, for the low temperature, high Al content alloy (Al-30at.%Si), a line with slope $-2$ cannot be fitted to the $\langle|A(k_{\mathrm{n}})|^{2}\rangle I_{\text{step}}$ vs $k_{\mathrm{n}}$ results. This behaviour develops gradually with decreasing T. For the case of Al-87.4at.%Si the best fit line agrees well with a slope of $-2$, however for the Al-59.4at.%Si alloying system, the slope of the best fit to the amplitude vs wave number results is less than $-2$. As a fundamental assumption, the CFM can be used only for cases where the step is rough. Based on the Al-Si phase diagram, this alloy shows a single eutectic point at 12.6at.% Si. Therefore, the liquidus line decreases by adding Al to the melt and the equilibrium temperature decreases for more Al-rich compositions. Based on these results it can be concluded that

![](./images/811036025039093760_5.jpg)

Fig. 4. Log-Log plot of the fluctuation spectra, $\langle|A(k_{n})|^{2}\rangle_{l_{step}}$ vs $k_{n}$, for (a) Al-59.4at.%Si and (b) Al-87.4at.%Si alloys in the $[\overline{1}10]$ and $[11\overline{2}]$ step orientations. The solid line indicates a slope of -2. These graphs illustrate the effect of crystal orientation on the stiffness of steps. The prediction of the CFM is the same for both step orientations and indicates the steps are isotropic in this system.

Table 2
Calculated stiffness values before and after modification as a function of interface orientation for a Al-87.4at.%Si and Al-59.4at.%Si alloy. Error bars represent estimated 95% confidence levels associated with statistical sampling.

<table>
  <thead>
    <tr>
      <th>Composition</th>
      <th>Step direction</th>
      <th>$T_{Eq}(k)$</th>
      <th>$(\gamma+\gamma'')\times10^{-11}\left(\frac{1}{m}\right)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Al-87.4at.%Si</td>
      <td>$[\overline{1}10]$</td>
      <td>1570</td>
      <td>$1.78\pm0.12$</td>
    </tr>
    <tr>
      <td>Al-87.4at.%Si</td>
      <td>$[11\overline{2}]$</td>
      <td>1570</td>
      <td>$1.67\pm0.11$</td>
    </tr>
    <tr>
      <td>Al-59.4at.%Si</td>
      <td>$[\overline{1}10]$</td>
      <td>1230</td>
      <td>$2.61\pm0.13$</td>
    </tr>
    <tr>
      <td>Al-59.4at.%Si</td>
      <td>$[11\overline{2}]$</td>
      <td>1230</td>
      <td>$2.60\pm0.16$</td>
    </tr>
  </tbody>
</table>

## 4. Conclusion

Through an analysis of capillary fluctuations in the interfacial position of (111) step on the crystal-melt interface, we have determined the step free energy for a binary Al-Si mixture at three compositions and two crystal orientations. Our results for the anisotropy in $\gamma$ show complete isotropy of step free energy with step direction for high temperatures. For the Al-30at.%Si alloy, the CFM was found to be unsuccessful and we conclude that at 920 K, which is the liquidus temperature of the Al-30at.%Si system, the steps are either no longer rough or exhibit a very small equilibrium kink density. As shown in this work, at temperatures where steps become very smooth, and the amplitudes of capillary fluctuations for the wavelengths that can be probed in atomistic simulations are very small, the CFM does not provide a viable framework for computing step free energies. For each particular system it is possible identify a range of temperatures or compositions for which CFM can be applied to extract isotropic step free energy. This information provides a reference point for thermodynamic integration techniques to investigate magnitude and anisotropy of step free energy in other regions of phase diagram [40].

at lower temperatures or higher Al concentrations, the step behaviour can no longer be considered rough. However, this observation does not necessarily imply the step is undergoing a roughening transition. Results from previous theoretical studies [39] indicate that in the solid on solid model a roughening transition cannot occur, but the equilibrium kink density can decrease significantly with decreasing temperature. Chernov concluded high surface energies and low temperatures lead to a low density of kinks on steps, which is the case, e.g., in low-temperature epitaxy. A decreasing kink density may also account for the results shown in Fig. 5.

![](./images/811036025039093760_6.jpg)

Fig. 5. Log-Log plot of the fluctuation spectra, $\langle|A(k_{n})|^{2}\rangle_{l_{step}}$ vs $k_{n}$, for (a) $[\overline{1}10]$ and (b) $[11\overline{2}]$ for Al-87.4at.%Si, Al-59.4at.%Si and Al-30at.%Si alloying systems at 1570 K, 1230 K and 920 K, respectively. For the last system the results do not follow the predicted slope of -2.

### Acknowledgment

Support for Timofey Frolov was provided under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344. Work of Rodrigo Freitas and Mark Asta at UC Berkeley was supported by the US National Science Foundation (Grants Nos. DMR-1105409 and DMR-1507033).

### Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.commatsci.2017.03.044.

### References

[1] J.S. Langer, Lectures in the theory of pattern formation, in: J. Souletie, J. Vannimenus, R. Stora (Eds.), Les Houches, North-Holland, Amsterdam, 1987.

[2] D.A. Kessler, J. Koplik, H. Levine, Pattern selection in fingered growth phenomena, Adv. Phys. 37 (1988) 255-339.

[3] J.M. Howe, Interfaces in Materials: Atomic Structure, Thermodynamics and Kinetics of Solid-Vapor, Solid-Liquid and Solid-Solid Interfaces, Wiley, New York, 1997.

[4] M.E. Glicksman, N.B. Singh, Effects of crystal-melt interfacial energy anisotropy on dendritic morphology and growth kinetics, J. Cryst. Growth 98 (1989) 277-284.

[5] M. Muschol, D. Liu, H.Z. Cummins, Surface-tension-anisotropy measurements of succinonitrile and pivalic acid: comparison with microscopic solvability theory, Phys. Rev. A 46 (1992) 1038-1050.

[6] M. Asta, J.J. Hoyt, Thermodynamic properties of coherent interfaces in f.c.c.-based AgAl alloys: a first-principles study, Acta Mater. 48 (2000) 1089-1096.

[7] T. Frolov, Y. Mishin, Liquid nucleation at superheated grain boundaries, Phys. Rev. Lett. 106 (2011) 155702.

[8] H. Zhou, X. Lin, M. Wang, W. Huang, Calculation of crystal-melt interfacial free energies of fcc metals, J. Cryst. Growth 366 (2013) 82-87.

[9] X.-M. Bai, M. Li, Comparing crystalmelt interfacial free energies through homogeneous nucleation rates, J. Phys.: Condens. Matter 20 (2008) 375103.

[10] V.G. Baidakov, S.P. Protsenko, A.O. Tipeev, Surface free energy of the crystal-liquid interface on the metastable extension of the melting curve, JETP Lett. 98 (2014) 801-804.

[11] R.L. Davidchack, B.B. Laird, Direct calculation of the hard-sphere crystal $/$$\text{melt}$ interfacial free energy, Phys. Rev. Lett. 85 (2000) 4751-4754.

[12] R.L. Davidchack, B.B. Laird, Direct calculation of the crystalmelt interfacial free energies for continuous potentials: application to the Lennard-Jones system, J. Chem. Phys. 118 (2003) 7651-7657.

[13] B.B. Laird, R.L. Davidchack, Direct calculation of the crystalmelt interfacial free energy via molecular dynamics computer simulation, J. Phys. Chem. B 109 (2005) 17802-17812.

[14] X. Feng, B.B. Laird, Calculation of the crystal-melt interfacial free energy of succinonitrile from molecular simulation, J. Chem. Phys. 124 (2006) 044707.

[15] S.M. Foiles, J.J. Hoyt, Computation of grain boundary stiffness and mobility from boundary fluctuations, Acta Mater. 54 (2006) 3351-3357.

[16] J.R. Morris, Complete mapping of the anisotropic free energy of the crystal-melt interface in Al, Phys. Rev. B 66 (2002) 144104.

[17] J.J. Hoyt, M. Asta, Atomistic computation of liquid diffusivity, solid-liquid interfacial free energy, and kinetic coefficient in Au and Ag, Phys. Rev. B 65 (2002) 214106.

[18] D.Y. Sun, M. Asta, J.J. Hoyt, M.I. Mendelev, D.J. Srolovitz, Crystal-melt interfacial free energies in metals: fcc versus bcc, Phys. Rev. B 69 (2004) 020102.

[19] J.J. Hoyt, M. Asta, D.Y. Sun, Molecular dynamics simulations of the crystalmelt interfacial free energy and mobility in Mo and V, Phil. Mag. 86 (2006) 3651-3664.

[20] D.Y. Sun, M.I. Mendelev, C.A. Becker, K. Kudin, T. Haxhimali, M. Asta, J.J. Hoyt, A. Karma, D.J. Srolovitz, Crystal-melt interfacial free energies in hcp metals: a molecular dynamics study of Mg, Phys. Rev. B 73 (2006) 024116.

[21] J.R. Morris, M.I. Mendelev, D.J. Srolovitz, A comparison of crystalmelt interfacial free energies using different Al potentials, J. Non-Cryst. Solids 353 (2007) 3565-3569.

[22] M. Amini, B.B. Laird, Crystal-melt interfacial free energy of binary hard spheres from capillary fluctuations, Phys. Rev. B 78 (2008) 144112.

[23] M. Asta, J.J. Hoyt, A. Karma, Calculation of alloy solid-liquid interfacial free energies from atomic-scale simulations, Phys. Rev. B 66 (2002) 100101.

[24] C.A. Becker, D.L. Olmsted, M. Asta, J.J. Hoyt, S.M. Foiles, Atomistic simulations of crystal-melt interfaces in a model binary alloy: interfacial free energies, adsorption coefficients, and excess entropy, Phys. Rev. B 79 (2009) 054109.

[25] J.J. Hoyt, M. Asta, A. Karma, Method for computing the anisotropy of the solid-liquid interfacial free energy, Phys. Rev. B 79 (2001) 227-233.

[26] A.A. Potter, J.J. Hoyt, A molecular dynamics simulation study of the crystalmelt interfacial free energy and its anisotropy in the CuAgAu ternary system, J. Cryst. Growth 327 (2011) 227-232.

[27] D. Buta, M. Asta, J.J. Hoyt, Kinetic coefficient of steps at the Si(111) crystal-melt interface from molecular dynamics simulations, J. Chem. Phys. 127 (2007) 074703.

[28] T. Frolov, M. Asta, Step free energies at faceted solid-liquid interfaces from equilibrium molecular dynamics simulations, J. Chem. Phys. 137 (2012) 214108.

[29] F.H. Stillinger, T.A. Weber, Computer simulation of local order in condensed phases of silicon, Phys. Rev. B 31 (8) (1985) 5262.

[30] P. Beaucage, N. Mousseau, Nucleation and crystallization process of silicon using the Stillinger-Weber potential, Phys. Rev. B 71 (2005) 094102.

[31] P. Saidi, T. Frolov, J.J. Hoyt, M. Asta, An angular embedded atom method interatomic potential for the aluminum-silicon system, Modell. Simul. Mater. Sci. Eng. 22 (2014) 055010.

[32] Y. Kauffmann, S.H. Oh, C.T. Koch, A. Hashibon, C. Scheu, M. Rhle, W.D. Kaplan, Quantitative analysis of layering and in-plane structural ordering at an alumina aluminum solid-liquid interface, Acta Mater. 59 (2011) 4378-4386.

[33] Y. Yang, D.L. Olmsted, M. Asta, B.B. Laird, Atomistic characterization of the chemically heterogeneous Al-Pb solid-liquid interface, Acta Mater. 60 (2012) 4960-4971.

[34] A. Dongare, M. Neurock, L. Zhigilei, Angular-dependent embedded atom method potential for atomistic simulations of metal-covalent systems, Phys. Rev. B 80 (2009).

[35] P. Saidi, J. Hoyt, Atomistic simulation of the step mobility at the Al-Si (111) crystal-melt interface using molecular dynamics, Comput. Mater. Sci. 111 (2016) 137-147.

[36] J.J. Hoyt, Z.T. Trautt, M. Upmanyu, Fluctuations in molecular dynamics simulations, Math. Comput. Simul. 80 (2010) 1382-1392.

[37] F. Spaepen, A structural model for the solid-liquid interface in monatomic systems, Acta Metall. 23 (6) (1975) 729-743.

[38] F. Spaepen, Solid State Phys. 47 (1994) 1.

[39] A.A. Chernov, Notes on interface growth kinetics 50 years after Burton, Cabrera and Frank, J. Cryst. Growth 264 (4) (2004) 499-518.

[40] T. Frolov, Y. Mishin, Temperature dependence of the surface free energy and surface stress: an atomistic calculation for Cu (110), Phys. Rev. B 79 (4) (2009) 045430.