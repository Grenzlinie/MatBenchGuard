# Electronic, vibrational, and transport properties of pnictogen-substituted ternary skutterudites

Dmitri Volja,¹,∗ Boris Kozinsky,² An Li,²,¹ Daehyun Wee,³,† Nicola Marzari,⁴,¹ and Marco Fornari⁵

¹Department of Materials Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA
²Research and Technology Center, Robert Bosch LLC, Cambridge, Massachusetts 02142, USA
³Department of Environmental Science and Engineering, Ewha Womans University, Seoul, 120-750, Korea
⁴Theory and Simulation of Materials, École Polytechnique Fédéral de Lausanne, 1005 Lausanne, Switzerland
⁵Department of Physics, Central Michigan University, Mount Pleasant, Michigan 48859, USA

(Received 2 November 2011; revised manuscript received 27 March 2012; published 22 June 2012)

First principles calculations are used to investigate electronic band structure and vibrational spectra of pnictogen-substituted ternary skutterudites. We compare the results with the prototypical binary composition CoSb₃ to identify the effects of substitutions on the Sb site, and evaluate the potential of ternary skutterudites for thermoelectric applications. Electronic transport coefficients are computed within the Boltzmann transport formalism assuming a constant relaxation time, using a methodology based on maximally localized Wannier function interpolation. Our results point to a large sensitivity of the electronic transport coefficients to carrier concentration and to scattering mechanisms associated with the enhanced polarity. The ionic character of the bonds is used to explain the detrimental effect on the thermoelectric properties.

DOI: 10.1103/PhysRevB.85.245211
PACS number(s): 72.20.Pa, 63.20.D–, 71.15.Mb

## I. INTRODUCTION

Thermoelectric materials with a filled skutterudite structure are considered to be a prototypical realization of the phonon-glass electron-crystal paradigm (PGEC) proposed by Slack.¹,² Indeed, many compositions in this structural family exhibit low thermal conductivities ($k \simeq 0.5$–5 W m⁻¹ K⁻¹), Seebeck coefficients ($S$) from $-200$ to $200$ $\mu$V/K, and electrical resistivities ($\rho$) in the range from $10^{-4}$ to $10^{-3}$ $\Omega$ cm at room temperature, depending on doping levels.³ Their figure of merit $ZT$ ($ZT = TS^{2}/\rho k$ is used to characterize the material's performance)⁴ reaches values in excess of 1.4 at high temperature in the bulk form.⁵,⁶ Skutterudites have been investigated for use in high-reliability thermoelectric modules designed for space applications,⁵ owing to their good thermal stability and mechanical strength throughout the operating temperature range. Mechanical strength is of particular importance in automotive and household applications,⁷ where stress due to repeated thermal cycling is a major engineering challenge. The chemical robustness and stability of the skutterudite crystal structure allows for composition modifications across a wide chemical space, which in turn provides freedom in optimizing electronic and thermal transport properties. In this paper, we explore one such variation: heterogeneous pnictogen substitution in the absence of filling.

The conventional cubic unit cell of a binary skutterudite such as CoSb₃ (four formula units, space group no. 204) consists of a simple cubic transition metal ($M =$ Co) sublattice intertwined with square rings formed by covalently bonded pnictogen ($X_{4} =$ Sb₄) ions and oriented along (100), (010), and (001) crystallographic directions (Fig. 1). Each transition metal sits at the center of a distorted pnictogen octahedron. In general, the six pnictogens share nine electrons with the transition metals and two other electrons with the two nearest pnictogen ions. Charge balance constrains the transition metal atom to have nine electrons ($d^{7}s^{2}$), thus leaving a limited choice of binaries with Co, Rh, or Ir as $M$ and P, As, or Sb as $X$, in the absence of a filler ion. Substitutions and filling have a strong effect not only on the lattice thermal conductivity but also on the electronic band structure and associated transport properties. This was pointed out both experimentally,⁵ and by first principles band structure calculations.⁸⁻¹⁷

![](./images/813301428108918786_1.jpg)

FIG. 1. (Color online) Rhombohedral ($R\overline{3}$) unit cell of a PSTS, such as a $CoX_{1.5}Y_{1.5}$ compound containing $CoX_{3}Y_{3}$ octahedra. Co centered octahedra are linked by nearly rectangular $X$-$Y$ four-member rings (light gray lines), a characteristic feature of ternaries skutterudites. Black lines represent the unit cell (figure produced with CrystalMaker).

From a thermoelectricity point of view, binary skutterudites have a comparatively large thermal conductivity $k$. Alloying on the transition metal site and filling has also been explored as a strategy to decrease thermal conductivity and control electronic transport.¹,¹⁸⁻³² However, the effect of chemical substitution on the pnictogen site remains largely unexplored.

In this paper we focus primarily on recently synthesized $CoGe_{1.5}S_{1.5}$, $CoSn_{1.5}Te_{1.5}$, and $CoGe_{1.5}Te_{1.5}$ where the substitution is occurring on the pnictogen site of the prototypical CoSb₃. We call these materials pnictogen-substituted ternary skutterudites (PSTSs). In order to obtain a complete comparison we also studied $CoGe_{1.5}Se_{1.5}$, $CoSn_{1.5}S_{1.5}$, and


CoSn₁.₅Se₁.₅. PSTSs are experimentally observed to have a significantly lower thermal conductivity than CoSb₃,³³⁻³⁶ and thus are attractive to be investigated as potential thermoelectric materials. The features of the band structure and of the phonon dispersion need to be investigated in detail.

This paper is organized as follows. In Sec. II we briefly discuss the first principles methodology used to compute the electronic and transport properties as well as the phonon dispersion. Section III is devoted to the main results on the structural features, Sec. IV contains the discussion on the electronic bands, Sec. V presents the phonon dispersions, and Sec. VI discusses the electronic transport coefficients. In Sec. VII we draw our conclusions.

## II. METHODOLOGY

All presented data are obtained by *ab initio* calculations within density function theory (DFT) formalism³⁷,³⁸ using the Perdew-Zunger local density approximation (LDA) exchange-correlation energy functional.³⁹,⁴⁰ The effect of the core electrons is treated within the pseudopotential approach with both ultrasoft (Co, S),⁴¹ and separable norm-conserving (Ge, Sn, Te) pseudopotentials. A plane-wave basis was employed for the expansion of the valence electron wave functions and charge densities with the kinetic-energy cutoffs of 30 and 240 Ry, respectively. All calculations were performed using a 4 × 4 × 4 Monkhorst-Pack *k*-point mesh to sample the Brillouin zone. All internal atomic coordinates were relaxed within the Broyden-Fletcher-Goldfarb-Shanno method until the forces on the nuclei were below 0.025 eV/Å. The theoretically optimized lattice provides a residual stress smaller than 5.8 kbar. Spin-orbit (SO) effects are not included in our calculations since the effect of spin-orbit interactions is known to have relatively minor consequences on the band structure of CoSb₃ and related unfilled skutterudites.⁸ Using the WIEN2K software⁴⁴ we found that without additional structural relaxation the gap decreases by only 7 meV upon inclusion of SO coupling. The changes on the band structure are very small near the energy gap that is the region of interest with the respect to transport. The size of the Seebeck at the optimal doping slightly changes (within approximately 10%–15% of the original value). Our results are consistent with the literature.⁴⁵

Phonons were computed using density functional perturbation theory (DFPT).⁴⁶ The dynamical matrix was Fourier interpolated on a fine **q**-point mesh starting from a 2 × 2 × 2 grid. All calculations were performed with the QUANTUM ESPRESSO software.⁴⁷

Electronic transport coefficients are computed within the BOLTZWAN code⁴⁸ using the Boltzmann transport equation (BTE) in the constant scattering time approximation. Our methodology differs from other approaches (see, for instance, Ref. 49) in that we employ maximally localized Wannier functions (MLWFs, Ref. 50) to map the first principles electronic structure on a tight-binding model and obtain band derivatives following the work of Yates *et al*.⁵¹ The method is not sensitive to band crossings and provides an efficient way to integrate Fermi velocities over the Brillouin zone. The computation of MLWFs has been performed within the WANNIER90 package⁵² using the Bloch states obtained with the QUANTUM ESPRESSO distribution. Relevant procedures for obtaining the band derivatives are described in the Appendix and examples of MLWF for CoSb₃ are shown in Fig. 12. We used also the BOLTZTRAP package⁴⁹ of Madsen and Singh to compare with previous calculations.

## III. STRUCTURAL FEATURES

The two main structural units in prototypical CoSb₃ are transition metal centered pnictogen octahedra and pnictogen rings. In PSTSs the symmetry decreases with respect to CoSb₃ and two different kinds of octahedra and rings can be identified. The structure of the pnictogen rings is known to have a strong influence on electronic bands, phonons, and consequently transport properties of binary and filled skutterudites.⁹,¹⁶,⁵³,⁵⁴ The typical PSTS structure, $MX_{1.5}Y_{1.5}$ (space group no. 148) is derived from the binary counterpart by a substitution of the pnictogen ion with a pair of elements from 14 (Ge, Sn) and 16 (S, Se, Te) groups. The stoichiometry is preserved but heterogeneity is introduced in the rectangular rings in which the two different ions are opposite (*trans*) to each other. The rhombohedral primitive cell contains 32 atoms and can be described as a corner sharing octahedral network that contains two nonequivalent Co sites ($2c$ and $6f$ Wyckoff positions, $2c$ along the diagonal of the cube), two nonequivalent $X$ sites ($6f$ and $6f$), and two nonequivalent $Y$ sites ($6f$ and $6f$). Each tilted octahedron is formed by group 14 and 16 ions ordered in alternating layers perpendicular to the [111] direction. In general, the pattern of Co off-center displacements is such that the structure is centrosymmetric. For all three compounds we have analyzed, Co($2c$) is off center in their respective octahedra and displaced along the [111] direction toward the smaller surrounding ions; Co($6f$) is also slightly displaced toward the smaller ions (this true for all cases except CoGe₁.₅Se₁.₅, where the covalent radii are very similar) but in a more complex pattern compatible with the symmetry. The octahedral units are deformed and tilted ($a^+a^+a^+$ in Glazer notation). The tilting is established to form the bonds of the two nonequivalent four-member rings involving $Y_A$ and $X_A$ or with $Y_B$ and $X_B$ in the PSTS structure and involves a doubling of the unit cell with respect to an ideal ReO₃ network. Shorter bonds are formed along a preferred Cartesian direction and, to accommodate the rigidity of the octahedra, longer bonds result in one of the perpendicular directions. The relative length of these bonds determines the deviations from the ideal square shape (Oftedal's law) of the pnictogen rings. In PSTSs such deviations are larger than in CoSb₃ since the bonds have additional ionicity that tends to decrease the interatomic distances (Schomaker-Stevenson rule). The dihedral angle in the rings changes from 90.0° in CoSb₃ to smaller values ranging from 81.7° to 89.8° for all the compounds except CoSn₁.₅S₁.₅ and CoSn₁.₅Se₁.₅. Our computed structural parameters are given in Table I and are within 2% of the experimental data.²⁸,³³,³⁴,³⁶,⁴²,⁴³ The lattice parameter correlates well with the covalent radii of the main group elements and the cell remains pseudocubic with rhombohedral angles close to 90°. Our data shows the expected correlation between the lattice parameter and the size of the substitution atoms on both pnictogen sites. For example, among the Ge-substituted compounds CoGe₁.₅S₁.₅

<table><thead><tr><th></th><th>CoGe₁.₅S₁.₅</th><th>CoGe₁.₅Se₁.₅</th><th>CoGe₁.₅Te₁.₅</th><th>CoSn₁.₅S₁.₅</th><th>CoSn₁.₅Se₁.₅</th><th>CoSn₁.₅Te₁.₅</th><th>CoSb₃</th></tr></thead><tbody><tr><td>$a_L$ (Å)</td><td>7.888 (8.010)</td><td>8.186</td><td>8.622 (8.699)</td><td>8.311</td><td>8.610</td><td>9.023 (9.122)</td><td>8.972 (9.038)</td></tr><tr><td>α (deg)</td><td>89.90 (89.94)</td><td>89.83</td><td>89.95 (89.99)</td><td>89.87</td><td>89.98</td><td>89.97 (90.06)</td><td>90.0</td></tr><tr><td>Co (2c) $x$</td><td>0.258 (0.258)</td><td>0.251</td><td>0.243 (0.247)</td><td>0.267</td><td>0.260</td><td>0.253 (0.250)</td><td>0.25</td></tr><tr><td>Co (6f) $x$</td><td>0.258 (0.262)</td><td>0.253</td><td>0.249 (0.249)</td><td>0.262</td><td>0.260</td><td>0.255 (0.250)</td><td>0.25</td></tr><tr><td>Co (6f) $y$</td><td>0.762 (0.755)</td><td>0.753</td><td>0.745 (0.745)</td><td>0.773</td><td>0.764</td><td>0.756 (0.750)</td><td>0.75</td></tr><tr><td>Co (6f) $z$</td><td>0.754 (0.750)</td><td>0.752</td><td>0.747 (0.749)</td><td>0.758</td><td>0.755</td><td>0.751 (0.750)</td><td>0.75</td></tr><tr><td>$X_A(6f)$ $x$</td><td>0.999 (0.000)</td><td>0.998</td><td>0.996 (0.995)</td><td>0.001</td><td>0.999</td><td>0.998 (0.998)</td><td>0.000</td></tr><tr><td>$X_A(6f)$ $y$</td><td>0.335 (0.336)</td><td>0.327</td><td>0.318 (0.318)</td><td>0.333</td><td>0.328</td><td>0.321 (0.319)</td><td>0.334 (0.335)</td></tr><tr><td>$X_A(6f)$ $z$</td><td>0.151 (0.148)</td><td>0.158</td><td>0.167 (0.166)</td><td>0.149</td><td>0.156</td><td>0.165 (0.162)</td><td>0.159 (0.158)</td></tr><tr><td>$X_B(6f)$ $x$</td><td>0.499 (0.498)</td><td>0.500</td><td>0.501 (0.501)</td><td>0.499</td><td>0.500</td><td>0.501 (0.500)</td><td>0.5</td></tr><tr><td>$X_B(6f)$ $y$</td><td>0.835 (0.836)</td><td>0.827</td><td>0.818 (0.829)</td><td>0.834</td><td>0.828</td><td>0.821 (0.823)</td><td>0.834 (0.835)</td></tr><tr><td>$X_B(6f)$ $z$</td><td>0.349 (0.350)</td><td>0.341</td><td>0.332 (0.338)</td><td>0.351</td><td>0.343</td><td>0.335 (0.337)</td><td>0.341 (0.342)</td></tr><tr><td>$Y_A(6f)$ $x$</td><td>0.000 (0.001)</td><td>0.00</td><td>0.999 (0.001)</td><td>0.001</td><td>0.001</td><td>0.000 (0.001)</td><td>0.00</td></tr><tr><td>$Y_A(6f)$ $y$</td><td>0.344 (0.347)</td><td>0.344</td><td>0.345 (0.346)</td><td>0.337</td><td>0.328</td><td>0.339 (0.338)</td><td>0.334 (0.335)</td></tr><tr><td>$Y_A(6f)$ $z$</td><td>0.849 (0.856)</td><td>0.850</td><td>0.851 (0.854)</td><td>0.840</td><td>0.843</td><td>0.845 (0.845)</td><td>0.841 (0.842)</td></tr><tr><td>$Y_B(6f)$ $x$</td><td>0.502 (0.505)</td><td>0.503</td><td>0.505 (0.501)</td><td>0.501</td><td>0.502</td><td>0.503 (0.503)</td><td>0.5</td></tr><tr><td>$Y_B(6f)$ $y$</td><td>0.844 (0.846)</td><td>0.844</td><td>0.845 (0.842)</td><td>0.837</td><td>0.838</td><td>0.839 (0.841)</td><td>0.834 (0.835)</td></tr><tr><td>$Y_B(6f)$ $z$</td><td>0.650 (0.646)</td><td>0.649</td><td>0.648 (0.652)</td><td>0.659</td><td>0.657</td><td>0.655 (0.655)</td><td>0.659 (0.658)</td></tr></tbody></table>

has the smallest lattice size while CoGe₁.₅Te₁.₅ has the largest and the same trend also appears in the other substitution site.

## IV. ELECTRONIC STRUCTURE AND TRANSPORT
We calculate the electronic band structures (Fig. 2) and compare them with the one of CoSb₃ (under equivalent symmetry representations) in order to investigate the effect of the pnictogen substitution. In all cases the valence bands consist of three separate manifolds. The lowest two are primarily derived from the unmixed $s$ states of two pnictogen types, and the splitting of the bands observed in PSTS is due to the different chemical nature and electronegativity of the pnictogen ions forming the rings. By comparison, in CoSb₃ the Sb-$s$ states contribute one single manifold. Both top valence and bottom conduction bands consist primarily of a mixture of Co $d$ states and pnictogen $p$ states with the majority of $d$ states lying below the top of the valence band.

Although the value of the computed band gap depends on the type of the exchange-correlation functional used,⁸,¹⁵,⁵⁵ in all our cases the direct gap is two to three times larger than in CoSb₃ (it ranges from 0.41 eV in CoSn₁.₅Se₁.₅ to 0.61 in CoGe₁.₅S₁.₅). For comparison our calculations for CoSb₃ give an energy gap of 0.22 eV in our DFT LDA calculations, while the experimentally measured values exhibit a wide variation.²⁸,⁵⁵⁻⁶²

Several effects contribute to the change in the band gap, mainly the $t_{2g}^{*}$-$e_{g}^{*}$ derived manifold splitting and the flattening of the band dispersion in PSTSs induced by the more ionic bonding. Skutterudite systems typically possess a single band that disperses away from the $t_{2g}^{*}$ valence manifold and reaches its maximum at the $\Gamma$ point (the highest occupied band). This band controls the lower edge of the energy gap and is important due to its role in transport in $p$-type materials because it provides carriers with small effective mass. In CoSn₁.₅Te₁.₅ the top of the valence band is about 170 meV above the low lying $d$ bands. This separation increases in CoSn₁.₅Te₁.₅ (220 meV), in CoGe₁.₅Se₁.₅ (250 meV), and in the other PSTSs, reaching values higher than in CoSb₃ (370 meV). The second higher energy valence bands (from the $t_{2g}^{*}$ manifold) of PSTSs have a multivalley character with heavy effective masses. Particularly in CoGe₁.₅Te₁.₅ and in CoSn₁.₅Te₁.₅ the top of the valence band is relatively close in energy to the bands below it; if this energy difference could be further reduced, the contribution from heavier carriers would enhance the $p$-type Seebeck coefficient favoring the thermoelectric performance. For comparison, in La filled CoSb₃ the first heavy valence band is about 70 meV below the top of the valence band due to an interaction between filler $f$ states and the highest valence band.¹⁰

In order to investigate the effects of ternary substitution on transport properties, we first evaluate the inverse of the hole effective mass tensor in the Wannier representation (see the Appendix). The inverse of the effective mass is then defined as an average of the diagonal elements of the tensor, $1/m^{*} = \frac{1}{3}\sum_{i}1/m_{i}$. The corresponding values are $0.196m_{e}$, $0.169m_{e}$, and $0.134m_{e}$ for CoGe₁.₅S₁.₅, CoGe₁.₅Te₁.₅, and CoSn₁.₅Te₁.₅, respectively, where $m_{e}$ is the electron mass. These values are larger than reported $\approx 0.07m_{e}$ for CoSb₃ (our theoretical value is in agreement with previous calculations).²⁸,⁵⁵,⁶³ In $p$-type PSTS samples higher effective masses of carriers are presumably responsible for the larger Seebeck coefficient values observed experimentally. We find that the dispersion of the top valence band is also affected by the pnictogen substitutions; it is more parabolic than in CoSb₃ although it also exhibits a linear character of the dispersion close to $\Gamma$. This linearity has been suggested in earlier work to affect hole transport and deviate from traditional semiconducting behavior.⁸

The lowest conduction energy levels also exhibit different features in PSTSs. Several nonequivalent minima in $\Gamma$-$L$ and

![](./images/813301428108918786_2.jpg)
![](./images/813301428108918786_3.jpg)

FIG. 2. (Color online) First principles band structure of $CoX_{1.5}Y_{1.5}$ with $(X,Y)=(Ge,S),(Sn,S),(Ge,Se),(Sn,Se),(Ge,Te),(Sn,Te)$ (dashed) compared to binary $CoSb_3$. $CoSb_3$ has been represented with $R\overline{3}$ symmetry for comparative purposes.

$\Gamma$-$X$ directions can provide pockets of carriers with large effective masses upon $n$-type doping. This effect is also due to the decreased dispersion of pnictogen $p$ bands due to stronger ionicity.

We derive the electrical conductivity and the Seebeck coefficient by solving the Boltzmann transport equation (BTE) in the constant relaxation time ($\tau$) approximation. We assume $\tau=10$ fs in this paper, which is commonly used for studying semiconductors. $^{64}$ This is an arbitrary choice since the scattering time for the PSTS is not known but it allows to establish the trends associated with band structure effects. Within the constant relaxation time approximation the Seebeck coefficient does not depend on $\tau$ and computed values can be compared directly with experimental data, as we have done in Figs. 6–8.

At room temperature the Seebeck coefficient of $CoGe_{1.5}S_{1.5}$ ranges from 39 to $258\ \mu$V/K for $p$-type doping in the range of $10^{18}$-$10^{20}$ electrons/cm$^3$. Since the experimental value of the

carrier concentration is not available for the samples under investigation, we performed computations of the Seebeck coefficient in a range of possible carrier concentrations by varying the position of the electron chemical potential. For a carrier concentration of $10^{20}$ holes per cm$^3$ our results agree with the experimentally reported thermopower of $CoGe_{1.5}S_{1.5}$. In the case of $CoGe_{1.5}Te_{1.5}$ and $CoSn_{1.5}Te_{1.5}$, following the experimental findings, we tested $n$-type doping in the limits of $10^{18}$-$10^{20}$ electrons/cm$^3$. At room temperature $S$ varies between $-646$ and $-257$ $\mu$V/K for $CoGe_{1.5}Te_{1.5}$ and from $-695$ to $-307$ $\mu$V/K for $CoSn_{1.5}Te_{1.5}$. While computed values for $CoSn_{1.5}Te_{1.5}$ are in reasonable agreement with experimental data at a carrier concentration of $10^{20}$ per cm$^3$, our results differ from the experimental data for $CoGe_{1.5}Te_{1.5}$ at low temperatures. The Seebeck value reaches its minimum of nearly $-800$ $\mu$V/K at 115 K, exhibiting an apparent dip and a subsequent increase in the magnitude. It may be tempting to explain such a trend reversal by the bipolar effect, i.e., decrease of $S$ due to thermal activation of minority carriers across the band gap. However, we argue that this feature derives only from the electronic structure of the valence manifold at the experimental carrier concentration. The first reason is that the bipolar effect typically sets in at temperatures where $k_BT$ is comparable to the band gap, and in PSTSs the band gap is comparably large. The experimental values of $S$ for $CoGe_{1.5}S_{1.5}$, whose atomic and electronic structure is similar, exhibit the expected trend of increasing $S$ with temperature. The second and most compelling reason is the appearance of such a nonmonotonic dip feature in the computed Seebeck coefficient temperature dependence of $CoSn_{1.5}Te_{1.5}$ (Fig. 8) at $n=10^{18}$ cm$^{-3}$. From the computed electronic band structure of $CoSn_{1.5}Te_{1.5}$ (Fig. 2) we readily conclude that this nonmonotonic feature is due to the intertwining and nondispersive character of the valence band manifold. The deviation from the experimental behavior at higher temperatures is likely due to the variation of the actual carrier concentration with temperature and the inaccuracy of the constant $\tau$ approximation.$^{28}$ At low temperatures impurity states may also account for the observed strong dependence of transport properties on temperature.$^{65}$ For $CoGe_{1.5}Se_{1.5}$, $CoSn_{1.5}Se_{1.5}$, and $CoSn_{1.5}Te_{1.5}$ we find values of $S$ to be between 200 and 400 $\mu$V/K for $n$-type doping and between 400 and 600 $\mu$V/K at room temperature. The general trend, as shown in Fig. 3, is that the Seebeck coefficient in all six PSTSs increases substantially with respect to $CoSb_3$ both for $p$- and $n$-type doping; this reflects the decreased band dispersion.

Experimental values of electronic resistivities at the room temperature are reported as $30.6$ $\Omega$ cm (Ref. 33) for $p$-type $CoGe_{1.5}S_{1.5}$, $5.1$ $\Omega$ cm (Ref. 34) for $n$-type $CoGe_{1.5}Te_{1.5}$, and $0.33$ $\Omega$ cm (Ref. 35) for $n$-type $CoSn_{1.5}Te_{1.5}$. The theoretical results for conductivity at room temperature span over several orders of magnitude depending on the carrier concentration. Our approach is to determine the carrier concentration as the one that produces the best match with the temperature dependence of the thermopower to experimental measurements.

Selecting this doping level, we compute the room temperature electrical conductivity that is about two orders of magnitude larger than experimental values. It must be noted that our methodology reproduces the experimental results in a wide range of temperature for the conductivity of $CoSb_3$ assuming $\tau=2.5\times10^{-14}$ s (Ref. 16) when we use the experimentally determined carrier concentration values. Within the constant relaxation time approximation, where thermopower $S$ is independent of $\tau$, this approach provides a way to separate possible contributions to the discrepancy between theory and measurements. We can reasonably conclude that the features of the electronic structure alone are only partially responsible for much larger electrical conductivity with respect to experiment. Three quantities contribute to the electronic conductivity: effective masses, carrier concentration, and scattering time $\tau$. The reasons for the discrepancy between experiment and theory could include inaccurate carrier concentrations and/or an anomalously short carrier lifetime. Impurity phases and defects in the experimental samples may also contribute to the discrepancy with the computed results. The simple scattering model used in our approach may be oversimplified and inadequate to capture fully all relevant scattering mechanisms.

![](./images/813301428108918786_4.jpg)

FIG. 3. (Color online) Seebeck coefficients of ternary skutterudites at 300 K as functions of the electron chemical potential (Fermi energy).

In order to evaluate the potential of PSTSs as active materials in thermoelectric devices, we compare their performance

![](./images/813301428108918786_5.jpg)

FIG. 4. (Color online) Electrical conductivity of ternary skutterudites at 300 K as a function of the electron chemical potential (Fermi energy).

![](./images/813301428108918786_6.jpg)

FIG. 5. (Color online) Power factor of ternary skutterudites at 300 K as a function of the electron chemical potential (Fermi energy).

with the well-known $CoSb_3$ material. All PSTSs have a lower electronic conductivity than in a wide range of doping levels, as shown in Fig. 4. Since the value of $\tau$ is taken to be the same, this reflects the larger band gap, decreased band dispersion, and larger carrier effective masses. In Fig. 5 we show the full power factors of all compositions as a function of doping level, and these results show a noticeably lower power factor for PSTSs as compared with $CoSb_3$ in the $p$-type region and most of the $n$-type region. We conclude that, in the electronic transport aspect, PSTSs are not likely to surpass the performance of $CoSb_3$-based systems, particularly for $p$-type materials, assuming the same carrier lifetimes. Furthermore, as we discuss below, carrier lifetimes in PSTSs are likely reduced by the enhanced ionicity.

In an ideal crystal the scattering time includes contributions from the electron-phonon coupling, with the larger contri- bution associated with deformation potential and Fröhlich scattering. The enhanced ionicity in PSTSs suggests to consider effects associated with the Fröhlich interaction. We have qualitatively analyzed this contribution by evaluating the mode-resolved Born effective charges, defined by

$$
z_{\alpha}^{*}(\omega, \mathbf{k})=\frac{\sum_{N, \beta} Z_{N, \alpha \beta}^{*} e_{N, \beta}(\omega, \mathbf{k})}{\sqrt{\sum_{N, \beta} e_{N, \beta}(\omega, \mathbf{k}) e_{N, \beta}(\omega, \mathbf{k})}},\qquad(1)
$$

to estimate the polarization arising from the vibrational displacements and, consequently, the strength of electronic scattering (Table II). $^{66}$

![](./images/813301428108918786_7.jpg)

FIG. 6. (Color online) Temperature and doping dependence of the Seebeck coefficient of $CoGe_{1.5} S_{1.5}$ compared to experimental intrinsic data (Ref. 33).

![](./images/813301428108918786_8.jpg)

FIG. 7. (Color online) Temperature and doping dependence of the Seebeck coefficient of $CoGe_{1.5} Te_{1.5}$ compared to experimental intrinsic data (Ref. 34).

Due to the smaller primitive cell and weak ionicity, $CoSb_3$ has a few (7) vibrational frequencies that exhibit nonzero $z_{\alpha}(\omega, k)$ at the Brillouin zone center (see Sec. V for the phonon dispersions). In the low frequency region below $120 \mathrm{~cm}^{-1}$ the mode resolved effective charges are less than 1 and the vibrational modes do not effectively scatter electrons. More significant scattering is expected when the modes above $250 \mathrm{~cm}^{-1}$, with $z_{\alpha}(\omega, \Gamma) \simeq 8$, become active. In PSTS the situation is quite different: We computed, in fact, many "polar modes" with a two to three times larger $z_{\alpha}$ than in $CoSb_3$. These modes are distributed across the entire frequency spectrum. This indicates that the enhanced polar scattering, especially at low frequency, may affect strongly the electrical conductivity,

![](./images/813301428108918786_9.jpg)

FIG. 8. (Color online) Thermopower of $CoSn_{1.5} Te_{1.5}$ (bottom) compared to the experimental intrinsic data (Ref. 36). Note the dip at low temperature as discussed in the text.

<table>
<caption>TABLE II. Transverse effective charges $Z^{*}$ computed with density functional perturbation theory. The full tensors are used to compute the electron-phonon polar scattering contribution but only $\frac{1}{3}\text{Tr} Z^{*}$ is reported here.</caption>
<tbody><tr><td></td><td>$\text{CoGe}_{1.5}\text{S}_{1.5}$</td><td>$\text{CoGe}_{1.5}\text{Te}_{1.5}$</td><td>$\text{CoSn}_{1.5}\text{Te}_{1.5}$</td><td>$\text{CoSb}_{3}$</td></tr>
<tr><td>$\text{Co}({2c})$</td><td>$-5.140$</td><td>$-6.021$</td><td>$-5.914$</td><td>$-6.678$</td></tr>
<tr><td>$\text{Co}({6f})$</td><td>$-4.895$</td><td>$-5.900$</td><td>$-5.810$</td><td></td></tr>
<tr><td>$X_{A}$</td><td>$+3.227$</td><td>$+3.463$</td><td>$+3.506$</td><td>$+2.229$</td></tr>
<tr><td>$X_{B}$</td><td>$+3.195$</td><td>$+3.462$</td><td>$+3.480$</td><td></td></tr>
<tr><td>$Y_{A}$</td><td>$-0.035$</td><td>$+0.439$</td><td>$+0.334$</td><td></td></tr>
<tr><td>$Y_{B}$</td><td>$-0.006$</td><td>$+0.430$</td><td>$+0.353$</td><td></td></tr>
</tbody></table>

as compared to $\text{CoSb}_{3}$. It is important to notice that the polar scattering contribution affects the thermal conductivity as well.

### V. PHONONS
First principles phonon dispersion for filled and unfilled skutterudites was studied by Feldman *et al.*,9,12 Ghosez *et al.*,59 and Wee *et al.*16 The vibrational spectrum of PSTSs is an essential starting point to understand the role of the chemical substitutions in PSTS and develop models for the low thermal conductivity observed in these materials. We present here the vibrational dispersions at the theoretically optimized structural parameters (See Figs. 9–11). For comparison, in $\text{CoSb}_{3}$ there are two main manifolds associated, respectively, with the vibration of the transition metal (between 250 and $300\ \text{cm}^{-1}$) and of the pnictogens (below about $200\ \text{cm}^{-1}$). In $\text{CoGe}_{1.5}\text{S}_{1.5}$ (Fig. 9) the comparable masses of Co and Ge result in the formation of vibrational modes that are mixed in character. The dispersion shows an additional manifold associated mainly with sulfur vibration above $350\ \text{cm}^{-1}$. The motion of Co contributes across all frequencies with a larger contribution near $300\ \text{cm}^{-1}$. The frequency of the lowest optical mode (mainly Ge) at $\Gamma$ is at about $100\ \text{cm}^{-1}$, only slightly higher than the Sb modes in $\text{CoSb}_{3}$. Similar features are observed in the dispersion of $\text{CoSn}_{1.5}\text{S}_{1.5}$ (not shown) where, of course, the Sn-derived modes extend to lower frequencies (about 75 $\text{cm}^{-1}$). The phonon dispersions of $\text{CoGe}_{1.5}\text{Te}_{1.5}$ (Fig. 10) and $\text{CoSn}_{1.5}\text{Te}_{1.5}$ (Fig. 11) exhibit two manifolds, similar to $\text{CoSb}_{3}$:

![](./images/813301428108918786_10.jpg)

FIG. 9. (Color online) Calculated phonon dispersion and atom projected vibrational densities of states of $\text{CoGe}_{1.5}\text{S}_{1.5}$.

![](./images/813301428108918786_11.jpg)

FIG. 10. (Color online) Calculated phonon dispersion and atom projected vibrational densities of states of $\text{CoGe}_{1.5}\text{Te}_{1.5}$.

The highest manifold is mostly from Co motion. The lowest frequency optical modes are at $65\ \text{cm}^{-1}$ in $\text{CoGe}_{1.5}\text{Te}_{1.5}$ and $50\ \text{cm}^{-1}$ in $\text{CoSn}_{1.5}\text{Te}_{1.5}$. This is the frequency region where modes from filler atom vibrations are found in $\text{BaCo}_{4}\text{Sb}_{12}$ (Ref. 16) and may point to the phonon scattering channel responsible for the low thermal conductivity.

The group velocity of acoustic modes near $\Gamma$ determines the thermal conductivity and, in our calculations, correlates with the mass of the specific pnictogen substituted ions. It is interesting to notice that the sound velocities in $\text{CoSn}_{1.5}\text{Te}_{1.5}$ are very similar to those of $\text{CoSb}_{3}$. In other PSTSs we found values higher than those of $\text{CoSb}_{3}$. Based on these results and the overall phonon dispersions, it is reasonable to argue that scattering phenomena differ substantially between $\text{CoSb}_{3}$ and PSTSs probably due to the different character of the bonding in the rings. Phonon dispersions alone cannot explain the low thermal conductivity values of observed experimentally for PSTSs. More work in the direction of understanding the anharmonic scattering in these materials is required.

![](./images/813301428108918786_12.jpg)

FIG. 11. (Color online) Calculated phonon dispersion and atom projected vibrational densities of states of $\text{CoSn}_{1.5}\text{Te}_{1.5}$.

## VI. CONCLUSIONS

We discussed structural aspects, electronic structure and transport, and phonon dispersions of pnictogen-substituted ternary skutterudites (PSTSs). These materials are potentially interesting for thermoelectric applications due to the exhibited low lattice thermal conductivity. Unfortunately the electronic transport is not as favorable because of the low electrical conductivities.

We justified the large Seebeck coefficients by analyzing the electronic band structures: a decreased dispersion compared with $CoSb_3$ as well as a multivalley character with heavy carrier effective masses. The values of electronic conductivity are lower than for $CoSb_3$ and have a strong dependence upon carrier concentration. We explored the upper limits on the power factor of PSTSs in a wide range of carrier concentrations and found that they are unlikely to surpass those of $CoSb_3$. More effort should be invested in understanding the reasons for low measured values and find a way to increase electronic conductivity in these materials.

## ACKNOWLEDGMENTS

The authors are grateful to Z. F. Ren and G. Chen for valuable discussions. This work was carried out as part of the MIT Energy Initiative, with financial support from Robert Bosch LLC. Additional funding was provided by the NSF-DOE Partnership in Thermoelectrics (CBET-0853350).

## APPENDIX: BOLTZMANN TRANSPORT FROM WANNIER FUNCTION INTERPOLATION

The prediction of electronic transport properties, using the Boltzmann transport equation (BTE), depends on the ability to accurately compute and integrate band derivatives over the Brillouin zone. Usually this is achieved by fitting the electronic band to a smooth curve and performing numerical derivatives, an approach that is sensitive to band crossings. The Wannier representation of the electronic structure $^{50,67–69}$ provides an optimized tight-binding model whose Hamiltonian can be directly differentiated to compute band velocities and effective masses. $^{50,51}$ An additional advantage of the approach is the possibility to separate the role of individual bands or band manifolds by projecting on minimal subspaces containing the most relevant degrees of freedom, using the disentanglement procedure. $^{70}$ For transport properties only a certain subset of the Bloch states near the Fermi level is relevant. In this paper we used maximally localized Wannier functions (MLWFs) to derive the necessary ingredients for the BTE in the constant scattering time approximation. As a side product we obtained a description of the bonding states in terms of MLWFs (Fig. 12).

The prototypical $CoSb_3$ is a semiconductor with two isolated valence manifold of 12 and 36 bands, respectively, and a conduction manifold that consists of an infinite number of entangled states above a LDA energy band gap of the order of $\approx$0.22 eV. The lowest manifold of 12 valence states is mainly formed by Sb $s$ states. The top 36-band manifold is constructed iteratively from the initial guess of the atomic Sb $s$ and $p$ states and Co $d$ states. Starting with a combination of on-site Co $d$ states and Sb $s$ or $p$ states we have converted the original combinations of atomic orbitals to a well localized set of Wannier functions with spreads in the range of 1.5–6.65 $\AA^2$. Among all 48 valence states one can distinguish 12 Co states of $t_{2g}$ symmetry, 12 Sb-Sb bonding states, and 24 Co-Sb bonding states (Fig. 12). To construct Wannier states for the conduction manifold for $CoSb_3$ we choose Bloch states in the energy range of 3.2 eV above the Fermi level. MLWF states were obtained by iterative convergence starting with an initial guess of 24 Gaussian-type orbital states placed 1/4 off the Co-Sb bond length away from Co atoms along each of the 24 Co-Sb bonds. Using a similar approach we have also determined the basis of MLWFs for the PSTS systems.

![](./images/813301428108918786_13.jpg)

FIG. 12. (Color online) Contour-surface plots of the maximally localized Wannier functions in $CoSb_3$ for (a) conduction antibonding states, (b) occupied Co $t_{2g}$ states, (c) Sb-Sb bonding states, and (d) Sb-Co bonding states. Oppositely signed lobes are differentiated by color. Blue = Co, gray = Sb.

Given the basis of MLWFs we can express the matrix elements of the Hamiltonian in terms of Wannier functions. Matrix elements of a periodic operator $O$ between Wannier states $n$ and $m$ are written as $O_{nm}^W(R) = \langle n0|O|mR\rangle$. The matrix element of the Hamiltonian at an arbitrary $k$ point in the $k$ space $^{37}$ can be obtained by inverse Fourier transformation (FT) interpolation,

$$
H_{nm}(\mathbf{k}) = \sum_{\mathbf{R}} e^{i\mathbf{kR}} \langle n0|H|mR\rangle.
$$

Due to the strong localization of MLWFs the Hamiltonian in the Wannier basis is sparse and one does not need the original $k$-point mesh (used to construct the Wannier states) to be dense to obtain convergence for an arbitrary $k$ point. For large systems, fast Fourier transform (FFT) scales much faster [$O(N\log(N))$] compared to the scaling of the eigenvalue problem [$O(N^3)$]. The right hand side of the last equation can be differentiated analytically with respect to $k$ to obtain the

matrix elements of the velocity operator:

$$v_{nm,\alpha}(\mathbf{k}) = \frac{\partial H_{nm}}{\partial k_{\alpha}} = \sum_{\mathbf{R}} e^{i\mathbf{kR}} \langle i R_{\alpha} | n0|H|mR \rangle.$$

As a last step, a rotation to the original set of the Bloch states is performed. This, however, requires matrix multiplication of only very small matrices of $M \times M$ size, where $M$ is the number of Wannier states. As a result, this interpolation scheme is faster than the direct solution of the eigenvalue problem, but with the additional complexity of the initial Wannierization. It also resolves a number of difficulties associated with band crossings and avoided crossings which persist in traditional interpolation schemes.

*dvolja@mit.edu
†Present address: Research and Technology Center, Robert Bosch
LLC, Palo Alto, CA 94304.
¹G. Slack, in CRC Handbook of Thermoelectrics, edited by D. Rowe
(CRC, Boca Raton, FL, 1995), Chap. 34.
²D. G. Cahill, S. K. Watson, and R. O. Pohl, Phys. Rev. B 46, 6131
(1992).
³J. P. Fleurial, T. Caillat, and A. Borshchevsky, in Skutterudites,
A New Class of Promising Thermoelectric Materials, Proceedings
of the XIII International Conference on Thermoelectrics, Kansas
City, MO, edited by B. Mathiprakasaru and P. Heenan (American
Institute of Physics, New York, 1995), pp. 40–44.
⁴G. J. Snyder and E. S. Toberer, Nat. Mater. 7, 105 (2008).
⁵J. P. Fleurial, T. Caillat, and A. Borshchevsky, in Proceedings of the
17th International Conference on Thermoelectrics, ICT97 (IEEE,
New York, 1997), pp. 1–11.
⁶C. J. Vineis, A. Shakouri, A. Majumdar, and M. G. Kanatzidis, Adv.
Mater. 22, 3970 (2010).
⁷J. S. Sakamoto, H. Schock, T. Caillat, J. Fleurial, R. Maloney,
M. Lyle, T. Ruckle, E. Timm, and L. Zhang, Science Adv. Mater.
3, 621 (2011).
⁸D. J. Singh and W. E. Pickett, Phys. Rev. B 50, 11235 (1994).
⁹J. L. Feldman and D. J. Singh, Phys. Rev. B 53, 6273 (1996).
¹⁰D. J. Singh and I. I. Mazin, Phys. Rev. B 56, R1650 (1997).
¹¹M. Fornari and D. J. Singh, Phys. Rev. B 59, 9722 (1999).
¹²J. L. Feldman, D. J. Singh, I. I. Mazin, D. Mandrus, and B. C. Sales,
Phys. Rev. B 61, R9209 (2000).
¹³D. J. Singh, in Recent Trends in Thermoelectric Materials Research,
edited by T. Tritt (Academic, San Diego, 2001), Vol. 70.
¹⁴O. M. Lovvik and O. Prytz, Phys. Rev. B 70, 195119 (2004).
¹⁵L. Chaput, P. Pecheur, J. Tobola, and H. Scherrer, Phys. Rev. B 72,
085126 (2005).
¹⁶D. Wee, B. Kozinsky, N. Marzari, and M. Fornari, Phys. B 81,
045204 (2010).
¹⁷M. Zebarjadi, K. Esfarjani, J. Yang, Z. F. Ren, and G. Chen, Phys.
Rev. B 82, 195207 (2010).
¹⁸B. C. Sales, D. Mandrus, and R. K. Williams, Science 272, 1325
(1996).
¹⁹D. T. Morelli and G. P. Meisner, J. Appl. Phys. 77, 3777 (1995).
²⁰G. S. Nolas, G. A. Slack, D. T. Morelli, T. M. Tritt, and A. C.
Ehrlich, J. Appl. Phys. 79, 4002 (1996).
²¹A. Kjekshus and T. Rakke, Acta Chem. Scand. A 28, 99 (1974).
²²A. Lyons, R. Gruska, C. Case, S. Subbarao, and A. Wold, Mater.
Res. Bull. 13, 125 (1978).
²³H. Lutz, J. Solid State Chem. 40, 64 (1981).
²⁴G. A. Slack and V. G. Tsoukala, J. Appl. Phys. 76, 1665 (1994).
²⁵H. Kim, M. Kaviany, J. C. Thomas, A. Van der Ven, C. Uher, and
B. Huang, Phys. Rev. Lett. 105, 265901 (2010).

²⁶T. Caillat, A. Borshchevsky, and J. Fleurial, in Proceedings of
the 12th International Conference on Thermoelectrics, Yokohama,
Japan (IEEE, New York, 1994), pp. 132–136.
²⁷A. Borshchevsky, J. Fleurial, E. Allevato, and T. Caillat, in Ref. 3,
p. 36.
²⁸T. Caillat, A. Borshchevsky, and J. Fleurial, J. Appl. Phys. 80, 4442
(1996).
²⁹A. Borshchevsky, T. Caillat, and J. P. Fleurial, in Proceedings of
the 15th International Conference on Thermoelectrics (ICT 96),
Pasadena, CA (IEEE, New York, 1996), pp. 112–116.
³⁰V. Keppens, D. Mandrus, B. C. Sales, B. C. Chakoumakos, P.
Dai, R. Coldea, M. B. Maple, D. A. Gajewski, E. J. Freeman, and
S. Bennington, Nature (London) 395, 876 (1998).
³¹R. Korestein, S. Soled, A. Wold, and G. Collin, Inorg. Chem. 16,
2344 (1977).
³²J. Fleurial, T. Caillat, and A. Borshchevsky, in Proceedings of the
14th International Conference on Thermoelectrics, St. Petersburg,
Russia (IEEE, New York, 1995), pp. 231–235.
³³P. Vaqueiro, G. G. Sobany, and M. Stindl, J. Solid State Chem. 181,
768 (2008).
³⁴P. Vaqueiro, G. G. Sobany, A. V. Powell, and K. S. Knight, J. Solid
State Chem. 179, 2047 (2006).
³⁵Y. Nagamoto, K. Tanaka, and T. Koyanagi, in Proceedings of the
16th International Conference on Thermoelectrics (XVI ICT 97),
Dresden, Germany (IEEE, New York, 1997), pp. 330–333.
³⁶P. Vaqueiro and G. G. Sobany, in Thermoelectric Power Generation,
edited by T. P. Hogan, J. Yang, R. Funahashi, and T. M. Tritt,
MRS Symposia Proceedings No. 1044 (Materials Research Society,
Pittsburgh, PA, 2008), pp. 185–190.
³⁷P. Hohenberg, Phys. Rev. 136, B864 (1964).
³⁸W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).
³⁹D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).
⁴⁰J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).
⁴¹D. Vanderbilt, Phys. Rev. B 41, 7892 (1990).
⁴²F. Laufek, J. Navratil, and V. Golias, Powder Diffr. 23, 15 (2008).
⁴³T. Schmidt, G. Kliche, and H. D. Lutz, Acta Crystallogr. Sect. C
43, 1678 (1987).
⁴⁴K. Schwarz, P. Blaha, and G. Madsen, Comput. Phys. Commun.
147, 71 (2002).
⁴⁵W. Wei, Y. Dai, H. Jin, and B. Huang, J. Phys. D 42, 055401
(2009).
⁴⁶S. Baroni, S. d. Gironcoli, and A. D. Corso, Rev. Mod. Phys. 73,
515 (2001).
⁴⁷P. Giannozzi et al., J. Phys.: Condens. Matter 21, 395502 (2009).
⁴⁸Our code is currently being implemented in the WANNIER90 package
available at [http://www.wannier.org] (in preparation).
⁴⁹G. Madsen and D. Singh, Comput. Phys. Commun. 175, 67 (2006).
⁵⁰N. Marzari and D. Vanderbilt, Phys. Rev. B 56, 12847 (1997).

$^{51}$J. R. Yates, X. Wang, D. Vanderbilt, and I. Souza, *Phys. Rev. B* **75**, 195121 (2007).

$^{52}$A. Mostofi, J. Yates, Y. Lee, I. Souza, D. Vanderbilt, and N. Marzari, *Comput. Phys. Commun.* **178**, 685 (2008).

$^{53}$D. Jung, M. H. Whangbo, and S. Alvarez, *Inorg. Chem.* **29**, 2252 (1990).

$^{54}$M. Llunell, P. Alemany, S. Alvarez, V. P. Zhukov, and A. Vernes, *Phys. Rev. B* **53**, 10605 (1996).

$^{55}$J. O. Sofo and G. D. Mahan, *Phys. Rev. B* **58**, 15620 (1998).

$^{56}$H. Rakoto, *Phys. B* (Amsterdam, Neth.) **246-247**, 528 (1998).

$^{57}$H. Rakoto, *Phys. B* (Amsterdam, Neth.) **269**, 13 (1999).

$^{58}$D. Mandrus, A. Migliori, T. W. Darling, M. F. Hundley, E. J. Peterson, and J. D. Thompson, *Phys. Rev. B* **52**, 4926 (1995).

$^{59}$P. Ghosez and M. Veithen, *J. Phys.: Condens. Matter* **19**, 096002 (2007).

$^{60}$I. Lefebvre-Devos, M. Lassalle, X. Wallart, J. Olivier-Fourcade, L. Monconduit, and J. C. Jumas, *Phys. Rev. B* **63**, 125110 (2001).

$^{61}$E. Z. Kurmaev, A. Moewes, I. R. Shein, L. D. Finkelstein, A. L. Ivanovskii, and H. Anno, *J. Phys.: Condens. Matter* **16**, 979 (2004).

$^{62}$Y. Kawaharada, *J. Alloys Compd.* **315**, 193197 (2001).

$^{63}$E. Arushanov, K. Fess, W. Kaefer, C. Kloc, and E. Bucher, *Phys. Rev. B* **56**, 1911 (1997).

$^{64}$T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding, and J. O. Sofo, *Phys. Rev. B* **68**, 125210 (2003).

$^{65}$J. S. Dyck, Wei Chen, J. Yang, G. P. Meisner, and C. Uher, *Phys. Rev. B* **65**, 115204 (2002).

$^{66}$W. Harrison, *Solid State Theory* (Dover, New York, 1980).

$^{67}$W. G. Yin, D. Volja, and W. Ku, *Phys. Rev. Lett.* **96**, 116405 (2006).

$^{68}$D. Volja, W. Yin, and W. Ku, *Europhys. Lett.* **89**, 27008 (2010).

$^{69}$T. Berlijn, D. Volja, and W. Ku, *Phys. Rev. Lett.* **106**, 077005 (2011).

$^{70}$I. Souza, N. Marzari, and D. Vanderbilt, *Phys. Rev. B* **65**, 035109 (2001).