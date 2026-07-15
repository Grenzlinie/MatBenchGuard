# Interplay between Gd and oxygen vacancy on the electronic properties and defect chemistry of Gd-doped $CeO_2$: A DFT + U study

Xiaoping Han$^{a,b}$, Noureddine Amrane$^{a,b}$, Zongsheng Zhang$^{c}$, Maamar Benkraouda$^{a,b,*}$

$^{a}$ Department of Physics, United Arab Emirates University, Al-Ain, P.O.Box 15551, United Arab Emirates
$^{b}$ Emirates Center for Energy and Environmental Research, United Arab Emirates University, Al-Ain, P.O.Box 15551, United Arab Emirates
$^{c}$ School of Energy and Power Engineering, North University of China, Taiyuan 030051, China

---

## ARTICLE INFO

**Keywords:**
Gd-doped $CeO_2$
Electronic properties
Defect chemistry
First-principles calculation

## ABSTRACT

The electronic properties and defect chemistry of Gd-doped $CeO_2$ have been systematically investigated using the density functional theory with the Hubbard $U$ correction. Three types of doping are considered in $2 \times 2 \times 2$ $CeO_2$ supercell: one Gd substitution for Ce, one Gd substitution and one oxygen vacancy, and 2 Gd substitutions and an oxygen vacancy. Detailed thermodynamic and kinetic investigations have been conducted to elaborate the favorability for the formation of these dopants in $CeO_2$. Results show that Gd substitutions and oxygen vacancy tend to cluster in the form of Gd-$V_O$-Gd via strong interaction between donor ($V_O$) and acceptor (substitutional Gd) states. Such a donor-acceptor interaction is found to lead to charge compensation. In contrast, a single or isolated Gd substitution hardly influences the defect chemistry of oxygen vacancy. This work is expected to offer valuable insights into the Gd-doped $CeO_2$, beneficial for widening the practical applications of $CeO_2$-based materials and devices.

---

### 1. Introduction

$CeO_2$ has become a technologically important material due to its wide applications for the production and purification of hydrogen, the purification of exhaust gases, the electrolytes in solid oxide fuel cells, and so on [1-6]. These applications have been well known to be strongly dependent on the performance of oxygen vacancy ($V_O$). In practice, various dopants have been used to dope $CeO_2$ to increase the amount of oxygen vacancy, so as to enhance the material functionalities. Some experimental and theoretical studies have showed that the oxygen vacancy formation and migration in $CeO_2$ can be promoted by doping with transition metals like Mn [7-12] and rare earth metals (like Y, Pr, Gd, Sm and Yb) [7,8,13-18], thus improving the oxygen storage capacity and ionic conductivity. The ionic conductivity of $CeO_2$ was also reported to increase in another study [19], where the doping with rare earth elements La, Nd, Sm, Gd, Tb, Dy and Er introduces more oxygen vacancies. The surface properties of $CeO_2$ doped with Sm, Gd, Pr, and Tb were also investigated using the UV and visible Raman spectroscopy [20], and many oxygen vacancies were found to be at the surface of the rare-earth-doped $CeO_2$, remarkably influencing the optical absorption properties.

Among these $CeO_2$ compounds, Gd-doped $CeO_2$ has shown great potential in various applications due to its excellent electrical, optical, magnetic, and catalytic properties. For example, Gd doping has been found to significantly increase the ionic conductivity in $CeO_2$ [21,22]. The similar result was reported in other investigations [23-25], where incorporation of Gd into $CeO_2$ has enhanced the ionic conduction by decreasing the activation energy barrier required for oxide ion movement in the lattice. Recently, the ordering of Gd and oxygen vacancy in Gd-doped $CeO_2$ was studied using the combined density functional theory (DFT), cluster expansion and Monte Carlo simulations [26], and $V_O$ was found to prefer to be in the nearest neighbor of Gd and form Gd-$V_O$ cluster. Additionally, Rushton et al examined the co-doping of Y and Gd in $CeO_2$ using static and dynamic atomic scale computer simulation techniques, and an evident increase in oxygen ion conductivity was observed [27]. Especially, in some explorations the doping of 10% Gd brought the maximum electrical conductivity to $CeO_2$ [28-32]. Also, the incorporation of Gd was reported to remarkably enhance the optical, magnetic properties, and the catalytic activity toward CO oxidation of $CeO_2$ [33].

Evidently, many works of Gd-doped $CeO_2$ have been directed towards enhancing the material properties, while few have been done to probe into the interplay between the dopant and oxygen vacancy. The interaction between Gd and $V_O$, as well as its effect on the energetics and electronic properties, is an unavoidable subject matter in Gd-doped $CeO_2$. Another fundamental issue is the defect chemistry of oxygen

---

* Corresponding author at: Department of Physics, United Arab Emirates University, Al-Ain, P.O.Box 15551, United Arab Emirates.
E-mail address: maamar@uaeu.ac.ae (M. Benkraouda).

https://doi.org/10.1016/j.chemphys.2020.110741
Received 26 June 2019; Received in revised form 13 January 2020; Accepted 5 March 2020
Available online 06 March 2020
0301-0104/ © 2020 Published by Elsevier B.V.

![](./images/812668327036977152_1.jpg)

Fig. 1. (a) Unit cell of CeO₂. (b) 2 × 2 × 2 CeO₂ supercell with a Gd substitution for Ce. The Ce, O and Gd atoms are represented by green, red and purple spheres, respectively.

vacancy. When an oxygen vacancy is created from CeO₂, two excess electrons are left behind and transfer to and localize at the 4f orbitals of two nearest Ce ions, which changes the formal valence of these two Ce ions from +4 to +3 [34-36]. The incorporation of Gd dopants into CeO₂ is bound to influence the transfer of excess charges from oxygen vacancy. How to influence and the extent to influence charge transfer are of fundamental importance to the performance of the system. In the present work, we explore the electronic properties of CeO₂ doped with various combinations of Gd dopants and oxygen vacancy using the DFT + U method, aiming at in-depth understanding of the interplay between oxygen vacancy defect and the dopant Gd, and the defect chemistry as well. Results show that the Gd-V₀-Gd cluster is the most probable dopant-defect combination in Gd-doped CeO₂, which offers a valuable insight into the Gd-doped CeO₂.

## 2. Model and method

Stoichiometric CeO₂ has a cubic fluorite lattice (Fm3m) with four cerium atoms and eight oxygen atoms per unit cell, as shown in Fig. 1(a). While studying defects or impurities, it is necessary to minimize the direct defect-defect or dopant-dopant interaction between two neighboring supercells. To investigate the effect of supercell size, we have calculated the band structures of 2 × 2 × 2 (96 atoms) and 3 × 3 × 3 (324 atoms) supercells with an oxygen vacancy. Results show that for each case oxygen vacancy creates a state within the band gap, and that the location and curvature of the gap state in both cases are nearly the same. Evidently, a remarkable enlargement of supercell size from 2 × 2 × 2 to 3 × 3 × 3 supercells hardly change the defect behaviour. This allows us to believe that the nature of the defect or dopant state can be well addressed in the 2 × 2 × 2 supercell, without needing a bigger supercell. Therefore, we use a 2 × 2 × 2 supercell with eight unit cells (Ce₃₂O₆₄) to construct the doped structures. The investigations are initiated on a Gd substitution by replacing a Ce atom with a Gd atom in a 2 × 2 × 2 CeO₂ supercell, and is further proceeded at the introduction of one O vacancy, followed by the second Gd substitution. Their molecular compositions are Ce₃₁GdO₆₄, Ce₃₁GdO₆₃ and Ce₃₀Gd₂O₆₃, corresponding to GdₓCe₁₋ₓO₂, GdₓCe₁₋ₓO₂₋ₓ and Gd₂ₓCe₁₋₂ₓO₂₋ₓ (x = 0.031), respectively. As an example, Fig. 1(b) shows a 2 × 2 × 2 CeO₂ supercell with a Gd substitution for Ce.

All studies of Gd-doped CeO₂ are implemented in the VASP (Vienna ab-initio simulation package) [37,38], with spin-polarization included. The projector augmented wave method (PAW) [39,40] is used to describe the ion-electron interactions. The generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE) functional [41] is chosen to describe the exchange-correlation interactions. The plane-wave basis is generated with valence configurations of Ce-5s²5p⁶4f¹5d¹6s², O-2s²2p⁴ and Gd-5s²5p⁶4f⁷5d¹6s². Owing to the strong Coulomb correlation of the localized Ce 4f and Gd 4f electrons, the nonlocal effect is considered through combining the standard DFT with a Hubbard U correction on the 4f electrons, i.e., DFT + U method [42-44]. Here, the DFT + U approach of Dudarev et al [44] is used, where the local part is described by the Ceperley-Alder functional [45] and the Coulomb and exchange interactions are treated by a single effective parameter $U_{\text{eff}} = U$-$J$. Because it is hard to use a single $U_{\text{eff}}$ value to simultaneously reproduce more than one crucial parameter, the choice of $U_{\text{eff}}$ value is always dependant on the physical properties of interest. Especially, even the same $U_{\text{eff}}$ values in different softwares often lead to the different calculation results. In this work the $U_{\text{eff}} = 5$ eV for both Ce and Gd-4f orbitals is employed considering this value has been found to be effective in improving the prediction of the electronic structures and properties of doped CeO₂ while using VASP [46-51]. Sampling of the irreducible wedge of the Brillouin zone is performed on Monkhorst-Pack k-points grids. A number of tests have been carried out to ensure convergence with respect to the number of energy cutoffs and k-points. We choose a plane-wave energy cutoff of 500 eV, with the k-grids of 8 × 8 × 8 points and 2 × 2 × 2 points in the full Brillouin zone for the calculations of the primitive cell and 2 × 2 × 2 supercells, respectively. The effort has been made to optimize all above structures until the total force on each ion is converged to 0.01 eV/Å. All investigations of doped CeO₂ are performed on the basis of the theoretical equilibrium lattice parameter of pure CeO₂ unit cell ($a = 5.49$ Å), which is in excellent agreement with the experimental value ($a = 5.41$ Å) [52].

## 3. Results and discussions

We start the study with a Gd substitution in 2 × 2 × 2 CeO₂ supercell, where a Ce atom is replaced with a Gd atom. The optimized supercell shows a very small increase in the lattice constant, which is consistent with the bigger ionic radius of Gd (1.053 Å) with respect to that of Ce (0.97 Å) [53,54]. The eight nearest O ions of Gd move away from the substitutional Gd by about 0.3 Å, while the twelve nearest neighbor host ions (Ce ions) deviate by 0.12 Å from their initial positions. Other ions hardly move relative to their initial positions. Fig. 2 shows the total density of states (DOS) and partial DOS (PDOS) of the optimized structure. It is clear from the figure that the valence band (VB) for both spin-up and spin-down channels is mainly composed of O 2p states (with some hybridization with Ce 5d and 4f orbitals) while the spin-up and spin-down states of conduction band (CB) dominantly consist of the Ce 4f orbitals. Although Gd has a very small contribution to both VB and CB, it induces polarization in the system. Fig. 3 shows the spin density of CeO₂ with a Gd substitution, which is mainly localized at the Gd atom and 8 surrounding O atoms. The total magnetic moment is calculated to be 6.80 μ_B. This is consistent with the outer electron configuration of Gd atom ($4f^75d^16s^2$), which leads to the ease of losing three electrons on 5d and 6 s orbitals to achieve the stable state with the half-filled state on the 4f shell.

Examining Fig. 2(a), the Fermi level is still in the band gap, meaning that incorporating Gd substitution does not give rise to the evident change in electrical property. This seems inconsistent with the trivalent Gd: In general, when the trivalent Gd substitutes the tetravalent Ce in CeO₂, the hole conduction will be induced. In order to explain this abnormality, we calculate the electronic population at each atomic site by integrating the total electronic charges inside a sphere centered on each atom with effective ionic radii, the so-called Shannon-Prewitt radii [53,54]. They are 1.053, 0.97 and 1.38 Å for Gd, Ce and O ions, respectively. The comparison between the cases with and without Gd reveals that only the Ce and O ions surrounding Gd have slight change in the electron population, while those far away from Gd remain nearly unchanged. Apparently, the electron redistribution induced by Gd substitution only occurs on the local Ce and O atoms, with little influence on the behaviors of the system. This phenomenon ought to be closely associated with the mixture of the ionicity and covalency in CeO₂. In CeO₂, four valence electrons of each Ce atom ($4f^15d^16s^2$) just nominally leave the host atoms and transfer into the p orbitals of two O atoms. Indeed, CeO₂ is not a fully ionic crystal, with a substantial part

![](./images/812668327036977152_2.jpg)

Fig. 2. (a) Total DOS and PDOSs for (b) Gd, (c) Ce and (d) O in $2\times2\times2$ CeO₂ supercell with a single Gd substitution. The vertical dot-dashed lines at energy zero represent the Fermi level.

![](./images/812668327036977152_3.jpg)

Fig. 3. Spin densities for a $2\times2\times2$ CeO₂ supercell with a single Gd substitution (only Gd substitution and its surrounding atoms are shown here). Light blue and purple isosurfaces represent positive and negative spin densities ($\pm0.025$ $e/\mathring{\text{A}}^3$), respectively.

of covalent component. The introduction of Gd substitution just induces the adjustment of covalency between Gd and its surrounding O, insufficient to cause the evident change in ionicity of the system.

We proceed the study through further introducing an O vacancy to Ce₃₁GdO₆₄, corresponding to the formula Ce₃₁GdO₆₃. There are four distinctly different ways for distributing the substitutional Gd and oxygen vacancy in $2\times2\times2$ CeO₂ supercell, distinguished from each other by the relative positions, i.e., $V_O$ has four positions relative to Gd substitution: 1st, 2nd, 3rd and 4th nearest neighbors (1NN, 2NN, 3NN and 4NN), as shown in Fig. 4. After fully optimizing these configurations, Configuration A (i.e., 1NN configuration) is found to be the most energetically stable, indicating that the substitutional Gd and O vacancy prefer to form a Gd-$V_O$ cluster. This is consistent with the theoretical study [26], where $V_O$ was reported to energetically be in the nearest neighbor of Gd. Fig. 5(a) shows the total DOS of Configuration A, where there is an apparent change: a localized state appears within the band gap. Further PDOS analyses reveal that this localized gap state is predominantly composed of 4f orbitals of two Ce ions nearest to $V_O$, as shown in the inset of Fig. 5(a). It also gets support from the integration analysis using Bader method [55], which displays 0.81 electrons more on each of these two Ce ions with respect to Ce₃₁GdO₆₄. This indicates that introducing $V_O$ to Ce₃₁GdO₆₄ causes two excess electrons to mostly transfer to two neighboring Ce ions, which is similar to the case of introducing $V_O$ to the perfect CeO₂.

![](./images/812668327036977152_4.jpg)

Fig. 4. Schematic configurations of $2\times2\times2$ CeO₂ supercell with a Gd substitution and $V_O$, with the $V_O$ (a) 1NN, (b) 2NN, (c) 3NN and (d) 4NN to Gd. Here only Gd and $V_O$ are marked using red spheres and cubes, respectively.

It is evident from Fig. 5(a) that the system is insulating, meaning that, like a single Gd substitution, the incorporation of a Gd substitution

![](./images/812668327036977152_5.jpg)

Fig. 5. Total DOSs for $2 \times 2 \times 2$ CeO₂ supercells with (a) Gd-$V_O$ and (b) Gd-$V_O$-Gd clusters. The inset in (a) shows the total DOS (in black) of the localized gap level, together with the PDOS (in red) for the $f$ states of two Ce ions nearest to $V_O$.

together with an oxygen vacancy still cannot change the electrical property. This result is typically inconsistent with the $n$-type property of oxygen vacancy and the $p$-type property of Gd substitution for Ce. Normally, substituting tetravalent Ce with trivalent Gd induces a hole state while introducing an O vacancy brings two excess electrons, which should drive the system to be electron doping as a whole. Apparently, it is not the case. This abnormality can be explained based on the electronic property of Ce₃₁GdO₆₄. As shown above, there is no the hole state in Ce₃₁GdO₆₄. The introduction of an oxygen vacancy into Ce₃₁GdO₆₄ causes two excess electrons not to compensate for the inexistent hole state but to transfer to the lowest-energy 4$d$ orbitals of two nearest Ce ions, yielding the localized state. Therefore, Gd substitution and oxygen vacancy is not effectively involved in the charge compensation. On the other hand, a qualitatively explanation can be done based on Ce₃₂O₆₃, where two electrons from oxygen removal are localized on two nearest Ce atoms (reducing them from +4 to +3 valence) [34-36]. Substituting one Ce with one Gd in Ce₃₂O₆₃ is like substituting one Ce atom with one Gd in Ce₃₂O₆₄, hardly inducing evident changes in the system. As a result, a single or isolated Gd substitution is inadequate to effectively influence the performance of oxygen vacancy.

Further, we incorporate the second Gd substitution into Ce₃₁Gd₁O₆₃ to consider the effect of 2 Gd substitutions and an oxygen vacancy (2Gd + 1$V_O$). Its molecular composition is Ce₃₀Gd₂O₆₃, corresponding to Ce_{1-2x}Gd_{2x}O_{2-x} with $x = 0.031$. The simultaneous incorporation of two Gd substitutions and one oxygen vacancy makes the configurations become complicated due to the different ways for distributing two Gd ions and one oxygen vacancy: Each substitutional Gd has 1NN, 2NN, 3NN and 4NN positions to $V_O$. The total-energy calculations on all configurations reveal that the configuration with O vacancy nearest neighboring to both Gd substitutions is the most stable configuration is the case with. Namely, two Gd ions and O vacancy tend to form a Gd-$V_O$-Gd cluster. Its total DOS is shown in Fig. 5(b), where one can see two changes induced by the second Gd substitution comparing with Fig. 5(a). First, the Fermi levels shift towards the valence band, suggesting the effect of $p$-doping of the second Gd substitution. Second, the localized state existent in Fig. 5(a) disappears. This indicates that in Ce₃₀Gd₂O₆₃ the two electrons left behind by oxygen vacancy will not any more transfer to and localize on Ce-4$f$ state. In order to unravel the distribution of charges from oxygen vacancy, we further examine the structure with two nearest Gd substitutions. Its calculate band structure shows that the Fermi level is inside the valence band, indicating that two Gd substitutions give rise to the hole state in the system. As a result, we can conclude that the electrons from oxygen vacancy compensate the hole state originating from two Gd substitutions.

Energetically, it is necessary to assess the likelihood of forming the above dopants and dopant clusters Gd, Gd-$V_O$, and Gd-$V_O$-Gd. For example, the formation energy of a substitutional Gd in CeO₂ can be expressed as [56]

$$
\Delta E_{f}=E\left(CeO_{2}: G d\right)+\mu_{C e}-\mu_{G d}-E\left(CeO_{2}\right)
\tag{1}
$$

where $E(CeO_2: Gd)$ and $E(CeO_2)$ are the total energies of the supercells with and without the substitutional Gd. The chemical potential $\mu_{Ce}=\mu_{Ce}^{elem}+\Delta \mu_{Ce}$, where $\mu_{Ce}^{elem}$ refers to the atomic total energy of Ce and the extraneous chemical potential $\Delta \mu_{Ce}$ is subject to the surrounding environment, i.e., O-poor and O-rich conditions. Here $\Delta \mu_{Ce}$ is limited by the constraints: $\Delta \mu_{Ce} \leqslant 0$ and $\Delta \mu_{Ce}+2 \Delta \mu_{O}=E_{f}(CeO_{2})$, where $E_f(CeO_2)$ refers to the formation energy of CeO₂ (using the HSE formalism $E_f(CeO_2)$ is calculated to be $-11.32$ eV per molecule unit, agreeing well with the experimental value of $-11.29$ eV) [57]. Similarly, $\Delta \mu_{Gd}$ is limited by the constraints: $\Delta \mu_{Gd} \leqslant 0$ and $2 \Delta \mu_{Gd}+3 \Delta \mu_{O}=E_{f}(Gd_{2}O_{3})$. The HSE-calculated $E_f(Gd_2O_3)$ is $-19.02$ eV per molecule unit (here $C$-type Gd₂O₃ is used), close to the experimental formation energy of $-18.86$ eV [57]. Under the O-rich condition, $\Delta \mu_{O}=0$, thus $\Delta \mu_{Ce}=E_{f}(CeO_{2})$and $\Delta \mu_{Gd}=\frac{1}{2} E_{f}(Gd_{2}O_{3})$. Under the O-poor condition, CeO₂ is reduced into Ce₂O₃, thus $\Delta \mu_{Ce}$ and $\Delta \mu_{O}$ can be obtained through the constraints: $\Delta \mu_{Ce}+2 \Delta \mu_{O}=E_{f}(CeO_{2})$ and $2 \Delta \mu_{Ce}+3 \Delta \mu_{O}=E_{f}(Ce_{2}O_{3})$. The HSE-calculated $E_f(Ce_2O_3)$ is $-18.54$ eV per molecule unit, very close to its experimental formation energy of $-18.63$ eV [57]. Based on the above $\Delta \mu_{O}$, $\Delta \mu_{Gd}$ is easy to get from $2 \Delta \mu_{Gd}+3 \Delta \mu_{O}=E_{f}(Gd_{2}O_{3})$. Fig. 6 shows the formation energies of Gd, Gd + $V_O$ and2Gd + $V_O$ between the O-rich and poor conditions. Apparently, the O-poor condition encourages the formation of Gd-$V_O$ cluster while the O-rich chemical potential is energetically favourable for Gd substitution for Ce. Especially, the Gd-$V_O$-Gd cluster is unaffected by the O chemical potential. More notably, under the most range between the O-rich and O-poor conditions the Gd-$V_O$-Gd cluster is more thermodynamically stable than a single Gd substitution and a Gd-$V_O$ cluster. Accordingly, it is necessary to further examine their kinetic

![](./images/812668327036977152_6.jpg)

Fig. 6. The calculated formation energies of Gd, Gd-$V_O$ and Gd-$V_O$-Gd in CeO₂ between O-rich and O-poor conditions.

![](./images/812668327036977152_7.jpg)

Fig. 7. Migration barriers of (a) Gd, (b) Gd-V₀, and (c) Gd-V₀-Gd moving to a neighboring location. The schematic configurations are shown with a cube corresponding to the unit cell of CeO₂. Here only Gd substitutions and oxygen vacancies are marked with red spheres and cubes, respectively.

stabilities.

The kinetic stabilities of a single Gd, Gd-V₀, and Gd-V₀-Gd are analysed by calculating their migration barriers to the corresponding neighboring locations in CeO₂ using the nudged-elastic band (NEB) method [58]. We examine all possible shortest migration paths for them, compare their calculated energy barriers and determine the minimum ones. The migration of a single Gd substitution just has a step, and its calculated migration barrier is 0.81 eV (Fig. 7(a)). The migration of the Gd-V₀ cluster includes two steps: oxygen vacancy first migrates with a barrier of 0.46 eV, followed with Gd migration with a barrier of 1.15 eV, as shown in Fig. 7(b). In contrast, the migration of the Gd-V₀-Gd cluster is complicated with three steps (see Fig. 7(c)), and its maximum barrier occurs at the second step with a barrier of 1.68 eV, much higher than those of the single Gd substitution (0.81 eV) and Gd-V₀ (1.15 eV). The increase in the migration barrier, as well as the multiple steps, is indicative of the high kinetic stability of the Gd-V₀-Gd cluster. The combination of thermodynamic and kinetic investigations allows us to believe that the Gd-V₀-Gd cluster is stable in Gd-doped CeO₂. This is in excellent agreement with the theoretical and experimental studies of Gd-doped CeO₂ [59,60], where the atomic arrangement with the Gd-Gd pair was found to be energetically more stable than the isolated Gd substitutions, and the pair prefers to be next to an oxygen vacancy to form a Gd-V₀-Gd cluster. In fact, from the point of charge compensation or charge neutrality, the Gd-V₀-Gd cluster is also considered as the most probable dopant-defect combination in Gd-doped CeO₂, which could get support from the Kroger-Vink notation [61,62]. Undoubtedly, such an atomic arrangement is helpful to offer a valuable insight into the Gd-doped CeO₂.

## 4. Conclusions

In summary, we have used the DFT + U method to systematically investigate the electronic properties and defect chemistry of Gd-doped CeO₂. The Gd substitution for Ce and the associated complexes with oxygen vacancy have been examined, and their thermodynamic and kinetic stabilities have been addressed in details. Different to the previous report in Ref. 26 (where the Gd-V₀ was preferred), our results show that Gd substitutions and oxygen vacancy tend to form the Gd-V₀-Gd cluster, leading to the charge compensation between donor and acceptor states. Such an atomic arrangement offers a valuable insight into the Gd-doped CeO₂, beneficial for expanding the practical applications of CeO₂-based materials and devices.

## CRediT authorship contribution statement

Xiaoping Han: Writing - original draft, Conceptualization.
Noureddine Amrane: Writing - review & editing, Conceptualization.
Zongsheng Zhang: Writing - review & editing, Conceptualization.
Maamar Benkraouda: Writing - review & editing, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

We acknowledge grants from United Arab Emirates University Program for Advanced Research (Grant Nos: 31S109, 31R146, 31R109-Research Center-ECEER-9-2016). Partial support is provided by North University of China through the Key R&D Plans of Shanxi Province (No. 201803D421084).

## References

[1] B.C.H. Steele, Solid State Ionics 129 (2000) 95.
[2] G.A. Deluga, J.R. Salge, L.D. Schmidt, X.E. Verykios, Science 303 (2004) 993.
[3] K. Otsuka, T. Ushiyama, I. Yamanaka, Chem. Lett. 22 (1993) 1517.
[4] A. Trovarelli (Ed.), Catalysis by Ceria and Related Materials, Imprial College Press, London, 2002.
[5] S. Park, J.M. Vohs, R.J. Gorte, Nature 404 (2000) 265.
[6] F. Esch, S. Fabris, L. Zhou, T. Montini, C. Africh, P. Fornasiero, G. Comelli, R. Rosei, Science 309 (2005) 752.
[7] A. Gupta, U.V. Waghmare, M.S. Hegde, Chem. Mater. 22 (2010) 5184.
[8] Y.H. Tang, H. Zhang, L.X. Cui, C.Y. Ouyang, S.Q. Shi, W.H. Tang, H. Li, J.S. Lee, L.Q. Chen, Phys. Rev. B 82 (2010) 125104.
[9] W.L. Cen, Y. Liu, Z.B. Wen, H.Q. Wang, X.L. Weng, Phys. Chem. Chem. Phys. 14 (2012) 5769.
[10] H.F. Li, G.Z. Lu, Q.G. Dai, Y.Q. Wang, Y. Guo, Y.L. Guo, Appl. Catal. B-Environ. 102 (2011) 475.
[11] L.C. Hsu, M.K. Tsai, Y.H. Lu, H.T. Chen, J. Phys. Chem. C 117 (2013) 433.
[12] M.D. Krcha, M.J. Janik, Langmuir 29 (2013) 10120.
[13] K. Ahn, D.S. Yoo, D.H. Prasad, H.W. Lee, Y.C. Chung, J.H. Lee, Chem. Mater. 24 (2012) 4261.
[14] P.P. Dholabhai, J.B. Adams, P. Crozier, R. Sharma, J. Chem. Phys. 132 (2010) 094104.
[15] D.A. Andersson, S.I. Simak, N.V. Skorodumova, I.A. Abrikosov, B. Johansson, Proc. Natl. Acad. Sci. 103 (2006) 3518.
[16] H. Inada, R. Sagawa, H. Hayashi, K. Kawamura, Solid State Ionics 122 (1999) 195.
[17] G. Niu, M.A. Schubert, F. Acapito, M.H. Zeollner, T. Schroeder, F. Boscherini, J. Appl. Phys. 116 (2014) 123515.
[18] M. Nakayama, M. Martin, Phys. Chem. Chem. Phys. 11 (2009) 3241.
[19] Q. Sun, Z. Fu, Z. Yang, Ceram. Inter. 44 (2018) 3707.
[20] M. Guo, J. Lu, Y. Wu, Y. Wang, M. Luo, Langmuir 27 (2011) 3872.
[21] V. Esposito, M. Zunic, E. Traversa, Solid State Ionics 180 (2009) 169.
[22] S. Kuharuangrong, J. Powder Sources 171 (2007) 506.
[23] R.G. Anderson, A.S. Nowick, Solid State Ionics 5 (1981) 547.
[24] J.A. Kilner, Solid State Ionics 8 (1983) 201.
[25] T.S. Zhang, J. Ma, S.H. Chan, P. Hing, J.A. Kilner, Solid State Sciences 6 (2004) 565.
[26] P.A. Zguns, A.V. Ruban, N.V. Skorodumov, Phys. Chem. Chem. Phys. 19 (2017) 26606.
[27] M.J.D. Rushton, A. Chroneos, S.J. Skinner, J.A. Kilner, R.W. Grimes, Solid State Ionics 230 (2013) 37.
[28] H. Yahiro, K. Eguchi, H. Arai, Solid State Ionics 36 (1989) 71.
[29] H. Yahiro, Y. Eguchi, K. Eguchi, H. Arai, J. Appl. Electrochem. 18 (1988) 527.
[30] K. Eguchi, T. Setoguchi, T. Inoue, H. Arai, Solid State Ionics 52 (1992) 165.
[31] J. Faber, C. Geoffroy, A. Roux, A. Sylvestre, P. Abelard, Appl. Phys. A 49 (1989)

225.

[32] H. Inaba, H. Tagawa, Solid State Ionics 83 (1996) 1.
[33] G.R. Li, D.L. Qu, L. Arurault, Y.X. Tong, J. Phys. Chem. C 113 (2009) 1235.
[34] N.V. Skorodumova, S.I. Simak, B.I. Lundqvist, I.A. Abrikosov, B. Johansson, Phys. Rev. Lett. 89 (2002) 166601.
[35] S. Fabris, S. Gironcoli, S. Baroni, G. Vicario, G. Balducci, Phys. Rev. B 71 (2005) 041102.
[36] X. Han, N. Amrane, Z. Zhang, M. Benkraouda, J. Phys. Chem. C 120 (2016) 13325.
[37] G. Kresse, J. Furthmuller, Comp. Mater. Sci. 6 (1996) 15.
[38] G. Kresse, J. Furthmuller, Phys. Rev. B 54 (1996) 11169.
[39] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.
[40] P.E. Blochl, Phys. Rev. B 50 (1994) 17953.
[41] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[42] V.I. Anisimov, J. Zaanen, O.K. Andersen, Phys. Rev. B 44 (1991) 943.
[43] V.I. Anisimov, I.V. Solovyev, M.A. Korotin, M.T. Czyzyk, G.A. Sawatzky, Phys. Rev. B 48 (1993) 16929.
[44] S.L. Dudarev, G.A. Botton, S.Y. Savrasov, C.J. Humphreys, A.P. Sutton, Phys. Rev. B 57 (1998) 1505.
[45] D.M. Ceperley, B.J. Alder, Phys. Rev. Lett. 45 (1980) 566.
[46] D.A. Andersson, S.I. Simak, B. Johansson, I.A. Abrikosov, N.V. Skorodumova, Phys. Rev. B 75 (2007) 035109.
[47] M. Nolan, S. Grigoleit, D.C. Sayle, S.C. Parker, G.W. Watson, Surf. Sci. 576 (2005) 217.

[48] Z. Yang, G. Luo, Z. Lu, T.K. Woo, K. Hermansson, J. Phys.: Condens. Matter 20 (2008) 035210.
[49] Z. Yang, G. Luo, Z. Lu, K. Hermansson, J. Chem. Phys. 127 (2007) 074704.
[50] M. Nolan, V.S. Verdugo, H. Metiu, Surf. Sci. 602 (2008) 2734.
[51] E.L. Wilson, R. Grau-Crespo, C. Pang, G. Cabailh, Q. Chen, J.A. Purton, C.R.A. Catlow, W.A. Brown, N.H. de Leeuw, G. Thornton, J. Phys. Chem. C 112 (2008) 10918.
[52] K.A. Gschneider, L. Eyring, Handbook on the Physics and Chemistry of Rare Earths, North-Holland, Amsterdam, Netherlands, 1979.
[53] R.D. Shannon, C.T. Prewitt, Acta Crystallogr. B 25 (1969) 925.
[54] R.D. Shannon, Acta Crystallogr. A 32 (1976) 751.
[55] G. Henkelman, A. Arnaldsson, H. Jonsson, Comput. Mater. Sci. 36 (2006) 354.
[56] S.B. Zhang, J.E. Northrup, Phys. Rev. Lett. 67 (1991) 2339.
[57] D.R. Lide, CRC Handbook of Chemistry and Physics, CRC Press, London, U.K., 1999.
[58] G. Mills, H. Jonnson, G.K. Schenter, Surf. Sci. 324 (1995) 305.
[59] H. Inaba, R. Sagawa, H. Tagawa, K. Kawamura, Solid State Ionics 122 (1999) 95.
[60] K.A. Gschneider, L. Eyring (Eds.), Handbook on the Physics and Chemistry on Rare Earths, Vol. 4 North-Holland, Amsterdam, 1979.
[61] F.A. Kroger, H.J. Vink, Solid State Phys. 3 (1956) 307.
[62] C.B. Cater, M.G. Norton, Ceramic Materials: Science and Engineering, Springer, New York, 2007.