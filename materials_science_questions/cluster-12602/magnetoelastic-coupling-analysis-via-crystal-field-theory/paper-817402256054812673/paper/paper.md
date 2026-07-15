PHYSICAL REVIEW B 99, 205125 (2019)

First-principles investigation of the effect of substitution and surface adsorption
on the magnetostrictive performance of Fe-Ga alloys

Hui Wang and Ruqian Wu

Department of Physics and Astronomy, University of California, Irvine, California 92697, USA

![](./images/817402256054812673_1.jpg)
(Received 10 October 2018; revised manuscript received 17 April 2019; published 15 May 2019)

Materials with large magnetostriction are widely used in sensors, actuators, microelectromechanical systems, and energy harvesters. Binary Fe-Ga alloys (Galfenol) are the most promising rare-earth-free candidates combining numerous advantages such as low saturation magnetic field (~200 Oe), excellent ductility, and low cost, while further improving their performance is imperative for practical applications. Using density functional theory calculation, we report the results of the effect of substituting small amounts of additional elements $X$ (e.g., $X=\text{Ag}$ or $\text{Cu}$) on magnetostriction of Fe-Ga alloys, and we find that it may double the magnetostriction with a substitutional percentage of only 1.6%. Moreover, adsorbents with high chemical activity (e.g., O or Os atoms) may affect the surface energy of different face orientations of Fe-Ga alloys, indicating that proper surface treatments are necessary to tune the alignment of Fe-Ga grains to achieve better performance. These results may be helpful to further optimize the magnetostrictive properties of Fe-Ga alloys for device applications.

DOI: 10.1103/PhysRevB.99.205125

## I. INTRODUCTION

Exploring novel magnetostrictive materials that can change their dimension with a small magnetic field is crucial for both fundamental research and technological exploitations [1,2]. One of the most successful magnetostrictive materials up to now is Terfenol-D ($\text{Tb}_{0.3}\text{Dy}_{0.7}\text{Fe}_{2}$), which shows giant magnetostriction up to 2000 ppm (parts per million), and it has been widely used in different devices such as sensors, actuators, microelectromechanical systems, energy harvesters [3,4], etc. However, their applications have been somehow limited due to the shortage of rare-earth supplies and mechanical brittleness. This inspired a new wave of interdisciplinary searches for rare-earth-free and ductile magnetostrictive materials. Fe-based materials, especially $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys (Galfenol with $x\sim19\%$), are the most promising candidates as they exhibit excellent mechanical properties, low saturation magnetic field (~200 Oe), and low cost and a large tetragonal magnetostrictive coefficient ($\lambda_{001}\sim280$ ppm) [5–8], which is comparable to spinels $\text{CoFe}_{2}\text{O}_{4}$ and $\text{NiFe}_{2}\text{O}_{4}$ [9,10]. Further development of these alloys for practical utilizations requires a comprehensive understanding of the mechanism [6,11–19] that governs the magnetostriction in transition-metal alloys, from which we can develop viable approaches to further improve their magnetostrictive performance.

Recent experimental and theoretical studies suggest that the availability of nonbonding electronic states around the Fermi level is important for the initial quadratic increase of $\lambda_{001}$ of $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys against $x$. Ga atoms avoid forming first neighbors in the Fe lattice, and, as a result, the presence of each Ga atom effectively breaks eight Fe-Fe bonds in Galfenol and hence many nonbonding Fe $d$ states are induced [14–17]. The dangling Fe $d$ states around the Fermi level allow strong spin-orbit coupling (SOC) interactions among them, and hence lead to a monotonic increase of the magnetoelastic coupling ($B_{1}$) with $x$ up to $x\sim15\%$. Meanwhile, the loss of Fe-Fe bonds reduces the tetragonal shear modulus ($C'$) from 60 GPa for the pure bulk Fe to about 10 GPa for $\text{Fe}_{81}\text{Ga}_{19}$ alloys. Since the tetragonal magnetostrictive coefficient $\lambda_{001}$ is simply the ratio of $B_{1}$ and $C'$ ($\lambda_{001}=2B_{1}/3C'$), it is apparent that both factors above contribute to the enhancement of $\lambda_{001}$ [20].

In this paper, we report results of systematic density functional theory (DFT) calculations for the effect of substitution of several transition-metal elements (e.g., Ag or Cu) on the magnetostrictive properties of $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys with $x\sim19\%$. Interestingly, we found that a small substitutional amount of these elements may significantly enhance the magnetostriction of Galfenol by a factor of $>200\%$. Surface doping with chemically active elements (such as heavy Os atoms, oxygen atoms, etc.) provides unique ways of tuning the physical properties of parent materials [21,22]. To provide useful guidance for the choice of a chemical environment for the postsynthesis treatment of Galfenol samples, we also investigated the effect of different adsorbents (such as O or Os atoms) on the surface energies of Galfenol, particularly for the preferential alignment of Fe-Ga grains along the (001) direction. These results provide additional insights for the development of Galfenol with optimal performance in devices.

## II. METHODOLOGY

Our DFT calculations were performed using the Vienna *ab initio* simulation package (VASP) [23,24]. The exchange-correlation interactions were included using the spin-polarized generalized-gradient approximation (GGA) with the Perdew-Burke-Ernzerhof (PBE) functional [25]. We treated Fe-$3d4s4p$, Ga-$4s4p$, Cu-$3d4s$, Ag-$4d5s$, H-$1s$, O-$2s2p$, S-$3s3p$, and Os-$5d6s$ as valence states, and we adopted the projector augmented wave method (PAW) to describe the valence-core interaction [26,27]. $5\times5\times5$ and $7\times7\times1$ Monkhorst-Pack $k$-meshes [28] were used to sample the

2469-9950/2019/99(20)/205125(7)
205125-1
©2019 American Physical Society

Brillouin zones of the bulk and surface models. The structures were fully relaxed with the following criteria: (i) the force acting on each atom is less than $0.01\ \text{eV}/\mathring{\text{A}}$, and (ii) total energy convergence is better than $10^{-5}\ \text{eV}$. The energy cutoff for the plane-wave expansion was set to $500\ \text{eV}$, which is sufficient for calculations of bulk Fe-Ga alloys and their surface adsorption according to our previous studies [21,29].

To determine the magnetocrystalline anisotropic energy ($E_{\text{MCA}}$) we used the torque method [30], which calculates $E_{\text{MCA}}$ as the expectation value of the angular derivative of the SOC Hamiltonian with respect to the polar angle $\theta$ of the spin moment, i.e., $\tau(\theta)=\partial E_{\text{tot}}(\theta)/\partial\theta=\sum_{\text{occ}}\langle\psi_{i,k}|\partial\text{H}_{\text{SO}}/\partial\theta|\psi_{i,k}\rangle$. This approach has been successfully applied for studies of magnetic anisotropy of a variety of magnetic materials and molecules as well as for magnetostriction of many transition-metal alloys [15,31,32]. The bulk Fe-Ga alloys were simulated by a $4\times4\times4$ supercell, which has 128 atoms in a cubic box. Their surfaces were mimicked by building up a slab model that consists of nine atomic layers and a vacuum gap of about $12\mathring{\text{A}}$ thickness to avoid the spurious interaction between periodic images. Different growth and annealing conditions were considered and simulated by varying the surface orientations and chemical adsorbents.

## III. RESULTS AND DISCUSSION

### A. Substitutional effects on magnetostriction of Fe-Ga alloys

For the binary $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys, the monotonic decrease of the tetragonal shear modulus continues up to $x\sim25\%$, whereas the increasing trend of the magnetoelastic coupling coefficient only sustains to $x\sim15\%$. This causes the rapid drop of the magnetostriction after it reaches its maximum at $x\sim19\%$ [15]. Therefore, one needs to extend the uptrend of $B_{1}$ and keep $C'$ relatively small beyond the critical Ga concentration. To this end, adding a small amount of the other elements is a promising way, and many elements including transition metals (e.g., Mn, Co, Ni, Cr, and Zn) and metalloids (e.g, Ge and Si) have been used in previous studies [1,5,6,16,33–36]. Here, we choose the most stable $\text{Fe}_{79.7}\text{Ga}_{20.3}$ atomic structure obtained from our previous studies as the template, and we study the effect of Ag or Cu substitution on the magnetostrictive properties of Galfenol [15]. The unit cell includes 102 Fe atoms and 26 Ga atoms, and we substitute two Ga atoms with $X$ atoms ($X=\text{Ag}$ or Cu) to form the $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ternary alloys. To figure out the preferential configuration of substitution, we change the separation between two $X$ atoms from 2.45, 2.91, and 4.09–$10.02\ \mathring{\text{A}}$, respectively, as marked by red in Fig. 1(a).

We found that the total energy of $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ternary alloys ($X=\text{Ag},\text{Cu}$) remains almost constant when the distance of two $X$ atoms ($d$) is larger than $4.09\ \mathring{\text{A}}$, indicating the weak interaction between them at this region as shown in Fig. 1(b). Two $X$ atoms behave similarly to Ga atoms when bond to adjacent Fe atoms, and they show small tails of their $d$ states near the Fermi level which is not found for Ga [inset of Fig. 1(b)]. However, the total energy decreases significantly up to $0.3$–$0.5\ \text{eV}/X$ atom as two $X$ atoms become the second or first nearest neighbors, due to their strong hybridization with each other. These results clearly indicate that the substitutional Ag and Cu elements prefer to stay together and may form clusters if the thermodynamical process is slow enough, in line with the poor solubility of these elements in the bcc Fe matrix [37]. Since clustering of these elements is detrimental to the magnetostriction according to our calculations, one may use a fast cooling or quenching method to freeze the metastable distribution patterns of $X$ elements

![](./images/817402256054812673_2.jpg)

FIG. 1. (a) Schematic models for $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys with a small amount of $X$ elements at different distance varying from first $(X_{0},X_{1})$, second $(X_{0},X_{2})$, third nearest neighbors $(X_{0},X_{3})$, and even further $(X_{0},X_{4})$. The light blue, yellow, and red represent Fe, Ga, and $X$ elements ($X=\text{Ag},\text{Cu}$), respectively. (b) The relative energy difference of $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ alloys as a function of the distance between two $X$ atoms in the Fe-Ga matrix as shown in (a); the fitted solid line is a guide for the eyes. The inset demonstrates the partial charge density $(e/\mathring{\text{A}}^{3})$ of $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ($X=\text{Ag}$) near the Fermi level along the [110] plane; $\text{Fe}_{1}$ and $\text{Fe}_{2}$ represent the first and second nearest neighbors of Ga/Ag atoms, respectively.

![](./images/817402256054812673_3.jpg)

FIG. 2. (a) Calculated $E_{\text{MCA}}$ with $\varepsilon_{z} = \pm 1\%$ for $\text{Fe}_{79.7}\text{Ga}_{20.3}$ (black solid line), $\text{Fe}_{79.9}\text{Ga}_{18.7}\text{Cu}_{1.6}$ (blue solid line), and $\text{Fe}_{79.9}\text{Ga}_{18.7}\text{Ag}_{1.6}$ (red solid line) vs the number of valence electrons $(N_{e})$ in the unit cell. The upper and lower curves represent $\varepsilon_{z} = +1\%$ and $-1\%$ as marked by the gray dashed arrows, respectively. The vertical dashed lines show corresponding positions of their actual $N_{e}$. The green solid arrows indicate taking away or adding electrons to the unit cell. (b) Calculated strain-dependent $E_{\text{MCA}}$ of FeGaX, where $X$ represents Ag and Cu, respectively.

in the $\text{Fe}_{79.7}\text{Ga}_{20.3}$ matrix to obtain high magnetostriction in $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ternary alloys.

Now we want to discuss the possibility of increasing tetragonal magnetostriction $\lambda_{001}$ with these substituents. For cubic materials, the tetragonal magnetostriction $\lambda_{001}$ can be determined from the strain $(\varepsilon)$ dependences of magnetocrystalline anisotropy energy $E_{\text{MCA}}$ and total energy $E_{\text{tot}}$ as $\lambda_{001} = \frac{2dE_{\text{MCA}}/d\varepsilon}{3d^{2}E_{\text{tot}}/d\varepsilon^{2}}$ [30,38]. The criterion for choosing possible substitutional impurities is mainly based on the rigid-band model calculations [16], from which one may control the magnetostrictive properties by tuning the total number of electrons in the system. We first analyze the dependence of $E_{\text{MCA}}$ of a strained $\text{Fe}_{79.7}\text{Ga}_{20.3}$ lattice ($\pm 1\%$ along the $z$-axis, while the lattice size in the lateral plane was adjusted according to the constant-volume mode: $\varepsilon_{z} = -2\varepsilon_{x} = -2\varepsilon_{y}$) on the total number of electrons in the supercell, as shown in the lower panel of Fig. 2(a). Note that the Fermi level $(N_{e} = 1154)$ touches the intersection of the two $E_{\text{MCA}}(N_{e})$ curves, suggesting a weak magnetoelastic coupling (or small $B_{1}$) of $\text{Fe}_{79.7}\text{Ga}_{20.3}$ alloys. It is clear that the strain-induced $E_{\text{MCA}}$ (or $B_{1}$) of $\text{Fe}_{79.7}\text{Ga}_{20.3}$ alloys can be further enhanced by either taking away (for positive $\lambda_{001}$) or adding (for negative $\lambda_{001}$) electrons to the unit cell, as shown by the green arrows in the lower panel of Fig. 2(a). Practically, this can be done through Ag,Cu or Ge,Si substitution for Ga atoms, respectively, assuming that they do not significantly affect the band structure of the Fe-Ga alloys near the Fermi level.

There are two kinds of layers in an Fe-Ga matrix, namely pure Fe layers and Fe-Ga mixing layers. For small amounts of substitutional $X$ atoms, they prefer to stay in the Fe-Ga mixing layers to maintain the pure Fe layers [11]. To verify our proposal through the rigid-band model, we conduct DFT calculations for $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ternary alloys by replacing two Ga atoms in the 128-atom supercell with noble metal Ag and Cu atoms, respectively. Indeed, the trends of strain-dependent $E_{\text{MCA}}$ of these alloys are very similar, indicating that the uniform substitution of $X$ for Ga rarely affects the band structure near the Fermi level. Meanwhile, impurities such as Ag and Cu induce nonbonding $dxz, yz$ states near the Fermi level, leading to the enhanced SOC interaction between occupied and unoccupied states according to the second-order perturbation approach [39]. As depicted in the upper panels of Fig. 2(a), one can see that the Fermi levels of $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Ag}_{1.6}$ and $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Cu}_{1.6}$ move to the left side by four electrons compared with $\text{Fe}_{79.7}\text{Ga}_{20.3}$ since both the Ag and the Cu atom have two fewer electrons than the Ga atom. As guided by the rigid-band analysis, the strain-induced $E_{\text{MCA}}$ at the Fermi level (or the magnetoelastic coupling coefficient $B_{1}$) is significantly larger than that of pristine $\text{Fe}_{79.7}\text{Ga}_{20.3}$ alloys, as demonstrated in Fig. 2(b). We also studied the substitution of the transition metal (e.g., Pd); the enhancement of magnetoelastic coupling is not as strong as Ag or Cu. These results show the usefulness of appropriately manipulating the number of electrons for the design of novel rare-earth-free magnetostrictive materials.

As we mentioned above, large magnetostriction relies on two main factors: a strong magnetoelastic coupling coefficient $B_{1}$ and a small tetragonal shear modulus $C'$. As is known, $B_{1}$ and $C'$ are simply proportional to the slope of the $E_{\text{MCA}} \sim \varepsilon$ line and the curvature of the total energy curve near $\varepsilon = 0\%$ [38,40], respectively. From the strain-induced changes of $E_{\text{MCA}}$ and the total energies in Fig. 3, the calculated values of $B_{1}$ for $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Ag}_{1.6}$ and $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Cu}_{1.6}$ are $\sim 17.5$ and $15.8\ \text{MJ}/\text{m}^{3}$, both of which are much larger (about 2.2–2.5 times) than that of the binary $\text{Fe}_{79.7}\text{Ga}_{20.3}$ alloy ($\sim 7.0\ \text{MJ}/\text{m}^{3}$). Meanwhile, the tetragonal shear modulus $C'$ for $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Ag}_{1.6}$ and $\text{Fe}_{79.7}\text{Ga}_{18.7}\text{Cu}_{1.6}$ ternary alloys is 8.6 and 9.7 GPa, respectively. In comparison, $C'$ of the pristine $\text{Fe}_{79.7}\text{Ga}_{20.3}$ alloy is close to 10.0 GPa. Therefore, the increase of the magnetoelastic coupling constant $B_{1}$ is the main reason for the large enhancement of $\lambda_{001}$ in $\text{Fe}_{79.7}\text{Ga}_{18.7}X_{1.6}$ ($X =$ Ag, Cu) ternary alloys.

![](./images/817402256054812673_4.jpg)

FIG. 3. Calculated strain-dependent total energies of Fe₇₉.₉Ga₁₈.₇X₁.₆ alloys, where X represents Ag and Cu, respectively. The inset demonstrates the applied strain under the condition of constant volume.

### B. The effect of adsorbents on surface energies of Fe-Ga alloys

It is known that the magnetostriction of Fe-Ga alloys is strongly anisotropic, i.e., the tetragonal magnetostrictive coefficient, λ₀₀₁, can reach about 280 ppm while its rhombohedral magnetostrictive coefficient, λ₁₁₁, is one order of magnitude smaller (±20–30 ppm) [33]. Therefore, it is crucial to develop an approach that can align most Fe-Ga grains along the (001) direction in order to achieve an optimal performance. It is believed that the alignment of grains in Fe-Ga films depends mainly on the surface energies (denoted as “γ”) of different facets, which can be controlled by tuning the chemical potential and using different surface adsorbents [19,29]. Here, we consider the surface energy of a facet with adsorbents according to the following equation:

$$
\gamma(N)=\frac{1}{2 A}\left[E_{\text {slab}+M}(N)-N_{\mathrm{Fe}} \mu_{\mathrm{Fe}}-N_{\mathrm{Ga}} \mu_{\mathrm{Ga}}-N_{M} \mu_{M}\right],
\tag{1}
$$

where $N_{\mathrm{Fe}}$, $N_{\mathrm{Ga}}$, and $N_{M}$ denote the numbers of atoms of Fe, Ga, and adsorbent, respectively; $\mu_{\mathrm{Fe}}$, $\mu_{\mathrm{Ga}}$, and $\mu_{M}$ represent their corresponding chemical potentials. $A$ is the surface area of the unit cell, and the factor ½ accounts for the two surfaces in typical slab models. To allow a direct comparison between different nonstoichiometric Fe-Ga facets, we assume an equilibrium growth condition with a constraint of

$$
\mu_{\mathrm{Fe}_{13} \mathrm{Ga}_{3}}=13 \mu_{\mathrm{Fe}}+3 \mu_{\mathrm{Ga}},
\tag{2}
$$

where $\mu_{\mathrm{Fe}_{13} \mathrm{Ga}_{3}}$ is the chemical potential of the bulk Fe₁₃Ga₃ in the $D0_3$ structures, so we may use $\mu_{\mathrm{Ga}}$ as a parameter to represent the different annealing condition.

Since the concentration of substituents that we discussed above is rather low, in principle they should not significantly alter the surface energies. For simplicity, we focus on the changes of surface energies of the Fe₈₁.₂₅Ga₁₈.₇₅ alloy caused by different adsorbents such as oxygen atoms, heavy transition-metal Os atoms, and H₂S molecules. According to the calculated total energies and comparing different adsorption sites, we find that O atoms prefer to take the atop-Ga site and Os atoms strongly bind to the bridge site of surface Ga atoms, with a binding energy of $-4.25\ \mathrm{eV/O\ atom}$ and $-6.23\ \mathrm{eV/Os\ atom}$, respectively; while the H₂S molecule is weakly adsorbed on the atop-Ga site with a binding energy of $-0.21\ \mathrm{eV/H_2S\ molecule}$. The most stable adsorption geometries and important bond distances are demonstrated in Fig. 4.

![](./images/817402256054812673_5.jpg)

FIG. 4. The most preferential adsorption sites of O atoms, Os atoms, and H₂S molecules on the Fe-Ga surface. Light blue, light red, yellow, white, red, and cyan represent Fe, Ga, S, H, O, and Os, respectively.

![](./images/817402256054812673_6.jpg)

FIG. 5. The calculated surface energies for (001), (110), and (111) surfaces with different percentages of Ga coverage. Horizontal dashed-dotted lines indicate zero energy. Left, middle, and right panels represent O/Fe-Ga, Os/Fe-Ga, and H₂S/Fe-Ga, respectively.

Since hybridization between adsorbents and substrates may change the Fe-Ga surface energies, we then focus on calculating the surface energies of the (001), (110), and (111) facets at different Ga concentrations in the topmost layer with the presence of O atoms, Os atoms, and H₂S molecules. As we can see in Fig. 5, Ga atoms prefer to segregate toward the surface (at 100% Ga coverage) in the Ga-rich condition ($\mu_{\text{Ga}} \to 0$) for all orientations. For example, the difference between surface energies of the Fe-terminated (0% Ga coverage) and the Ga-terminated (100% Ga coverage) surfaces is as large as $6.1\,\text{J/m}^2$ for Os atom/Fe-Ga(110) surface. In the Ga poor condition ($\mu_{\text{Ga}} < -3.0\,\text{eV}$), (001) and (110) surfaces with 75% Ga and 50% Ga coverage, respectively, gradually become more stable. The critical condition occurs at $\mu_{\text{Ga}} = -2.6\,\text{eV}$ for O/Fe-Ga (001), $\mu_{\text{Ga}} = -3.2\,\text{eV}$ for Os/Fe-Ga (001), and $\mu_{\text{Ga}} = -3.0\,\text{eV}$ for H₂S/Fe-Ga (001), respectively. It is interesting that the Fe-Ga (111) surface prefer 100% Ga coverage in the entire range of chemical potential. We want to point out that the tendency of Ga segregation toward the surface self-stops as long as a monolayer Ga forms on the top according to our previous studies for the clean Fe-Ga surface [29], and hence the Ga concentration in the interior region of Fe-Ga alloys is stable.

![](./images/817402256054812673_7.jpg)

FIG. 6. Comparison of calculated Fe-Ga surface energies of the most stable configurations for (001), (110), and (111) orientations with adsorbed (a) O atoms, (b) Os atoms, (c) H₂S molecules, and (d) clean surface. The orange arrow indicates the chemical potential of orthorhombic bulk Ga; the black point represents the intersection of surface energies between (001) and (110) orientation.

![](./images/817402256054812673_8.jpg)

FIG. 7. The projected density of states (PDOS) of (a) O/Fe-Ga, (b) Os/Fe-Ga, and (c) H₂S/Fe-Ga for (001) surface orientation with full Ga coverage, respectively. As a reference, the shaded area demonstrates the PDOS of Ga atoms in a clean Fe-Ga surface. The insets demonstrate the corresponding atomic configurations and charge redistribution between adsorbents and Fe-Ga substrate. Red and blue represent charge accumulation and depletion at $0.08\ e/\mathring{\text{A}}^3$, respectively. The blue dashed line indicates the Fermi energy.

To highlight the effect of different adsorbents, we further compare surface energies of the most stable configurations of the three different orientations, i.e., 100% Ga (001), 100% Ga (110), and 100% Ga (111), as demonstrated in Fig. 6. With adsorbed O atoms, Os atoms, and H₂S molecules, all (111) surfaces have much higher energies than their (001) and (110) counterparts, so the formation of grains with (111) orientation is largely suppressed, which is beneficial for the magnetostrictive performance of Fe-Ga films since $\lambda_{111}$ of Fe-Ga alloys is small and sometimes negative. It shows that the (110) surface is more stable in the Ga-rich condition ($\mu_{\text{Ga}} \to 0$) while the (001) surface becomes more favorable in the Ga-poor condition ($\mu_{\text{Ga}} \to -3.0\ \text{eV}$). As shown in Fig. 6(a), the crossover of surface energies between the (001) and (110) orientations with adsorbed O atoms appears at the left side of the normal Ga-poor condition ($\mu_{\text{bulk-Ga}} = -2.7\ \text{eV}$), while for that with adsorbed Os atoms and H₂S molecules it appears at the right side of the Ga-poor condition [shown in Figs. 6(b) and 6(c)]. Among all adsorbents, adsorbed H₂S does not affect the surface energies as compared with the clean Fe-Ga surface, as demonstrated in Figs. 6(c) and 6(d). It is worth noting that adsorbed Os atoms push the intersection of Fe-Ga surface energies between the (001) and (110) orientations to the side of the Ga-rich condition ($\mu_{\text{Ga}} = -1.8\ \text{eV}$), which will be helpful for the formation of grains with (001) orientation and maximize the magnetostrictive properties of Fe-Ga films. In the oxidation condition, one has to use a reservoir that binds to Ga atoms more tightly than the bulk Ga so as to create an environment for aligning Fe-Ga grains along the (001) direction. Nevertheless, the energy difference between (001) and (110) surfaces is rather small in the Ga-poor end ($-3.0 < \mu_{\text{Ga}} < -2.0\ \text{eV}$).

To understand the role of different adsorbents, we calculated the projected density of states (PDOS) of O atoms, Os atoms, and H₂S molecules adsorbed on the Fe-Ga (001) surface with 100% Ga coverage. Adsorbed O atoms interact with the underneath Ga atoms, which are pulled up by $\sim 0.43\ \mathring{\text{A}}$ compared to their positions on the clean surface. As shown by the PDOS and charge redistribution in Figs. 7(a) and 7(b), O atoms strongly hybridize with $\text{Ga}_{\text{surf}}$ orbitals near the Fermi level, and the PDOS of surface Ga in O/Fe-Ga(001) is shifted to higher energy due to electron transfer from Ga to O. As a result, O adatoms significantly affect the surface energies of Fe-Ga alloys, and the crossover of surface energies between the (001) and (110) orientations in O/Fe-Ga moves to the extreme Ga-poor condition. In contrast, adsorbed Os atoms transfer electrons from Os to Ga and interact with the substrate significantly, pushing the crossover of Fe-Ga surface energies between the (001) and (110) orientations to Ga-rich condition. As also demonstrated in Fig. 7(c), H₂S is adsorbed on the Fe-Ga surface with a distance of $\sim 2.5\ \mathring{\text{A}}$, and its electronic states mainly lie at $-7.0\ \text{eV}$, far below the Fermi level. The PDOS of surface Ga in H₂S/Fe-Ga(001) and clean Fe-Ga(001) remain almost unchanged below the Fermi level, indicating a rather weak interaction between H₂S and the Fe-Ga substrate. Therefore, the surface energies in H₂S/Fe-Ga and clean Fe-Ga are not much different. These results suggest that one may need to anneal Fe-Ga samples in the Ga-poor condition and make proper surface treatments to promote the most grain alignment along the (001) direction for a better performance.

## IV. CONCLUSIONS

In summary, we performed systematic DFT calculations to find possible ways of further improving the magnetostrictive properties of $\text{Fe}_{1-x}\text{Ga}_{x}$ alloys at $x \sim 19\%$. Rigid-band theory analysis suggests that this is realizable by substituting a small amount of Ag or Cu for Ga atoms in the Fe-Ga matrix, which is confirmed by DFT calculations with a large unit cell. Furthermore, the effect of different adsorbents on the surface energies of Fe-Ga alloys was also investigated, which may guide the design of growth and annealing conditions for the preferential (001) alignment of Fe-Ga grains in films. These results show the feasibility of engineering the magnetostrictive properties of transition-metal alloys by tuning their electronic properties and surface environment for the optimal performance of these materials for device applications.

## ACKNOWLEDGMENTS

We are grateful to A. E. Clark, M. Wun-Fogle, K. B. Hathaway, and A. B. Flatau for insightful discussions. This work was supported by the Office of Naval Research (Grants No. N00014-13-1-0445 and No. N00014-17-1-2905).

205125-6

[1] A. Clark, *Handbook of Ferromagnetic Materials* (North- Holland, Amsterdam, 1980), Vol. 1, p. 531.

[2] I. D. Mayergoyz, *Handbook of Giant Magnetostrictive Materi- als* (Elsevier, Amsterdam, 1999).

[3] L. Sandlund, M. Fahlander, T. Cedell, A. Clark, J. Restorff, and M. Wun-Fogle, J. Appl. Phys. **75**, 5656 (1994).

[4] F. Jerems, C. M. Mahon, A. Jenner, and R. Greenough, Ferroelectrics **228**, 333 (1999).

[5] E. Summers, T. Lograsso, and M. Wun-Fogle, J. Mater. Sci. **42**, 9582 (2007).

[6] A. E. Clark, J. B. Restorff, M. Wun-Fogle, T. A. Lograsso, and D. L. Schlagel, IEEE Trans. Magn. **36**, 3238 (2000).

[7] A. E. Clark, M. Wun-Fogle, J. B. Restorff, T. A. Lograsso, and J. R. Cullen, IEEE Trans. Magn. **37**, 2678 (2001).

[8] J. Cullen, A. Clark, M. Wun-Fogle, J. Restorff, and T. Lograsso, J. Magn. Magn. Mater. **226-230**, 948 (2001).

[9] D. Fritsch and C. Ederer, Phys. Rev. B **82**, 104117 (2010).

[10] D. Fritsch and C. Ederer, Phys. Rev. B **86**, 014406 (2012).

[11] H. Wang, Y. N. Zhang, T. Yang, Z. D. Zhang, L. Z. Sun, and R. Q. Wu, Appl. Phys. Lett. **97**, 262505 (2010).

[12] S. Bhattacharyya, J. R. Jinschek, A. Khachaturyan, H. Cao, J. F. Li, and D. Viehland, Phys. Rev. B **77**, 104107 (2008).

[13] H. Wang, Z. D. Zhang, R. Q. Wu, and L. Z. Sun, Acta Mater. **61**, 2919 (2013).

[14] Y. Zhang, H. Wang, and R. Wu, Phys. Rev. B **86**, 224410 (2012).

[15] H. Wang, Y. N. Zhang, R. Q. Wu, L. Z. Sun, D. S. Xu, and Z. D. Zhang, Sci. Rep. **3**, 3521 (2013).

[16] Y. Zhang, J. Cao, and R. Wu, Appl. Phys. Lett. **96**, 062508 (2010).

[17] H. Cao, P. M. Gehring, C. P. Devreugd, J. A. Rodriguez-Rivera, J. Li, and D. Viehland, Phys. Rev. Lett. **102**, 127201 (2009).

[18] G. Raghunath, A. B. Flatau, H. Wang, and R. Wu, Phys. Status Solidi B **253**, 1440 (2016).

[19] M. Van Order, S. Sinha, H. Wang, R. Wu, K. Gaskell, and A. Flatau, Adv. Theor. Simul. **2**, 1800043 (2019).

[20] C. Kittel, Rev. Mod. Phys. **21**, 541 (1949).

[21] J. Hu, J. Alicea, R. Wu, and M. Franz, Phys. Rev. Lett. **109**, 266801 (2012).

[22] K. Reuter and M. Scheffler, Phys. Rev. B **65**, 035406 (2001).

[23] G. Kresse and J. Furthmuller, Phys. Rev. B **54**, 11169 (1996).

[24] G. Kresse and J. Hafner, Phys. Rev. B **49**, 14251 (1994).

[25] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[26] G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

[27] P. E. Blochl, Phys. Rev. B **50**, 17953 (1994).

[28] H. J. Monkhorst and J. D. Pack, Phys. Rev. B **13**, 5188 (1976).

[29] M. Costa, H. Wang, J. Hu, R. Wu, S.-M. Na, H. Chun, and A. B. Flatau, Surf. Sci. **647**, 26 (2016).

[30] X. Wang, R. Wu, D.-S. Wang, and A. J. Freeman, Phys. Rev. B **54**, 61 (1996).

[31] J. Hu and R. Q. Wu, Phys. Rev. Lett. **110**, 097202 (2013).

[32] H. Wang, C. Shi, J. Hu, S. Han, C. C. Yu, and R. Q. Wu, Phys. Rev. Lett. **115**, 077002 (2015).

[33] G. Petculescu, R. Wu, and R. McQueeney, in *Handbook of Magnetic Materials* (Elsevier, Amsterdam, 2012), pp. 123.

[34] S.-M. Na and A. B. Flatau, J. Appl. Phys. **103**, 07D304 (2008).

[35] A. E. Clark, K. B. Hathaway, M. Wun-Fogle, J. Restorff, T. A. Lograsso, V. Keppens, G. Petculescu, and R. Taylor, J. Appl. Phys. **93**, 8621 (2003).

[36] M. Huang, Y. Du, R. J. McQueeney, and T. A. Lograsso, J. Appl. Phys. **107**, 053520 (2010).

[37] T. B. Massalski, H. Okamoto, P. Subramanian, and L. Kacprzak, *Binary Alloy Phase Diagrams*, 2nd ed. (ASM International, Materials Park, OH, 1990),Vol. 3, p. 3589.

[38] R. Wu and A. Freeman, J. Magn. Magn. Mater. **200**, 498 (1999).

[39] D.-S. Wang, R. Wu, and A. J. Freeman, Phys. Rev. B **47**, 14932 (1993).

[40] R. Wu, J. Appl. Phys. **91**, 7358 (2002).