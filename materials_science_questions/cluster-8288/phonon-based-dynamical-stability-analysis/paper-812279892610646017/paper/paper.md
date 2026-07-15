PHYSICAL REVIEW B 71, 195302 (2005)

# Isostructural phase transitions in GaN/ScN and InN/ScN superlattices

V. Ranjan, S. Bin-Omran, and L. Bellaiche
Physics Department, University of Arkansas, Fayetteville, Arkansas 72701, USA

Ahmad Alsaad
Jordan University of Science and Technology, Department of Physical Sciences, P.O. Box 3030, Irbid, Jordan

(Received 27 January 2005; published 3 May 2005)

We predict the existence of pressure-induced isostructural phase transitions (IPTs) in GaN/ScN and InN/ScN superlattices from first principles. The IPTs in these superlattices are anomalous in the sense that they are associated with trivial order parameters and generate a dramatic change in many physical quantities. Furthermore, the order of the phase transition is found to be dependent on the superlattice period and on the nontransition-metal cation. We also reveal the reason behind, and consequences of, these unusual dependencies and IPTs.

DOI: 10.1103/PhysRevB.71.195302
PACS number(s): 61.50.Ks, 64.60.-i, 64.70.Kb, 71.20.Nr

## I. INTRODUCTION

The so-called isostructural phase transitions (IPTs) are particularly remarkable, partly because of the difficulty in characterizing and understanding them. For example, the fact that such peculiar phase transitions leave the crystal symmetry unchanged makes the choice of the order parameter—which is the preliminary step for the theoretical description of a phase transition $^{1}$—a nontrivial task. Order parameters that have been proposed in the literature for IPTs are rather unusual and vary from a function involving defects concentrations $^{2}$ to atomic positions changing in disordered and/or subtle fashion, $^{3,4}$ via an electronic-induced change in compressibility $^{1}$ and a tiny modification in bond angle. $^{4,5}$ Similarly, observing IPTs, especially, if they are of second-order, is usually challenging, because many properties are only slightly affected by these transitions. $^{3}$ These difficulties and the relative rarity of IPTs are the two main reasons why these latter are in overall much less studied and thus less understood than the "more usual" symmetry-breaking phase transitions.

The aim of this paper is to report first-principles calculations predicting that GaN/ScN and InN/ScN superlattices undergo a pressure-induced isostructural phase transition that is anomalous in the sense (1) it is associated with "trivial" order parameters, (2) it leads to a dramatic change in various properties, and (3) the character of the transition depends on the period of the superlattice, as well as, on the nontransition-metal cation. Our simulations also reveal driving forces responsible for these anomalous features.

The organization of this article is as follows. The computational method we have adopted for the calculations is described in Sec. II. We present our results in Sec. III. Finally conclusions are given in Sec. IV.

## II. METHODOLOGY

The primitive lattice vectors of the parent compounds GaN, InN, and ScN, in their most stable hexagonal form, $^{6-8}$ are given by

$$
\begin{aligned}
\mathbf{a}_{1} & =a\left(\frac{1}{2} \mathbf{x}-\frac{\sqrt{3}}{2} \mathbf{y}\right), \\
\mathbf{a}_{2} & =a\left(\frac{1}{2} \mathbf{x}+\frac{\sqrt{3}}{2} \mathbf{y}\right), \\
\mathbf{a}_{3} & =c \mathbf{z},
\end{aligned}
\tag{1}
$$

where $a$ and $c$ are the in-plane and out-of-plane lattice parameters, respectively, and where $c/a$ is the axial ratio. The unit vectors along the Cartesian axes are denoted as $\mathbf{x}$, $\mathbf{y}$, and $\mathbf{z}$. The primitive unit cell for such systems contains four atoms: two N atoms located at $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$, and two cations of the same type (e.g., Ga) located at $\mathbf{r}_{3}$ and $\mathbf{r}_{4}$, with

$$
\begin{aligned}
\mathbf{r}_{1} & =0 \\
\mathbf{r}_{2} & =\frac{2}{3} \mathbf{a}_{1}+\frac{1}{3} \mathbf{a}_{2}+\frac{1}{2} \mathbf{a}_{3}, \\
\mathbf{r}_{3} & =u \mathbf{a}_{3}, \\
\mathbf{r}_{4} & =\frac{2}{3} \mathbf{a}_{1}+\frac{1}{3} \mathbf{a}_{2}+\left(\frac{1}{2}+\mathbf{u}\right) \mathbf{a}_{3}.
\end{aligned}
\tag{2}
$$

Three parameters, $a$, $c/a$, and the internal parameter $u$ which determines the relative position of atoms inside the unit cell, are thus needed to fully characterize the binary hexagonal parents. Our previous local-density-approximation (LDA) calculations predicted that (1) $c/a$=1.631 and $u$=0.376 for GaN, and (2) $c/a$=1.620 and $u$=0.378 for InN (Ref. 8), which agree very well with measurements. $^{9}$ The resulting ground-state, in both GaN and InN, is thus the wurtzite phase, is associated with the polar $P6_{3}mc$ ($C_{6v}$) space group and is four-times coordinated. On the other hand, we recently predicted that the equilibrium value of $u$ and $c/a$ are dramatically different in hexagonal ScN, namely 0.5 and $\approx$1.207, respectively. $^{6,7}$ This specific combination of lattice parameters leads to a layered structure, denoted by

1098-0121/2005/71(19)/195302(6)/$23.00
195302-1
©2005 The American Physical Society

$h$-ScN in earlier works, by the authors, $^{6,7}$ that is nearly five-times coordinated and that is associated with another space group: $P6_{3}/mmc$ ($D_{6h}$), which is nonpolar. Recent experiments support the existence of this unusual $h$-phase. $^{10}$

The unit cells for the ternary alloys, (Sc,Ga)N and (Sc,In)N, under study in the present paper are supercells, that consist in stacking different layers along the [0001] direction. For instance, $n$ layers of GaN are stacked on top of $m$ layers of ScN along $\mathbf{a}_{3}$, resulting in a structure that we denote as either $(GaN)_{n}/(ScN)_{m}$ or $n\times m$ superlattice. Note that these ordered structures can be thought as exhibiting two different kinds of $u$ parameter [see Eq. (2)]: the ones connecting the Ga and N atoms that are nearest neighbors along the $c$-axis, for which the average over all Ga atoms is denoted by $\langle u_{\text{GaN}}\rangle$, and the one binding the Sc and its closest N atoms along $\mathbf{a}_{3}$, for which the average over all Sc atoms is referred to as $\langle u_{\text{ScN}}\rangle$ (see Fig. 1). All the superlattices investigated in this article have a $P3m1$ ($C_{3v}$) group resulting from this stacking. $P3m1$ is a subgroup of both $P6_{3}mc$ and $P6_{3}/mmc$. As we will see below, hydrostatic pressure is able to change the axial ratio and internal atomic parameters from the wurtzitelike to the hexagonal-like values in these superlattices within the same $(P3m1)$ space group! In other words hydrostatic pressure leads to an isostructural phase transition in $n\times m$ GaN/ScN and InN/ScN.

Technically, total-energy calculations are performed using the first-principles density functional theory (DFT) within the local density approximation (LDA) (Ref. 11) and the Vanderbilt ultrasoft pseudopotentials. $^{12}$ The valence states for the Sc, Ga, In, and N are taken as, $3s^{2}3p^{6}3d^{1}4s^{2}$, $3d^{10}4s^{2}4p^{1}$, $4d^{10}5s^{2}5p^{1}$, and $2s^{2}2p^{3}$, respectively. We use the Ceperley-Alder $^{13}$ exchange-correlation functional as parameterized by Perdew and Zunger. $^{14}$ We chose the plane-wave cutoff to be 25 Ry, which leads to converged results of physical properties of interest. We also use a $6\times 6\times 4$ (6 $\times 6\times 2$) Monkhorst-Pack $^{15}$ $k$-point grid for Brillouin-zone integration of 4 atoms (8 atoms) per unit cell. All the structural degrees of freedom are fully relaxed in every considered structure by following the total energy and Hellman-Feynman forces (these latter being smaller than $0.051$ meV/Å at convergence).

We also compute the spontaneous polarization $\mathbf{P}$ as a Berry phase of the Bloch states. $^{16}$ Piezoelectric coefficients are derived from the knowledge of $\mathbf{P}$ via $^{17}$

$$
e_{ij}=\frac{1}{2\pi\Omega}\sum_{\alpha}R_{\alpha,i}\frac{d}{d\eta_{j}}(\Omega\mathbf{G}_{\alpha}.\mathbf{P}), \tag{3}
$$

where $\alpha=1,2,3$ denotes the three real-space lattice vectors $\mathbf{R}_{\alpha}$ and three reciprocal-space lattice vectors $\mathbf{G}_{\alpha}$. $\eta_{j}$ is the macroscopic strain. $\Omega$ is the volume of the unit cell and is given by $=\sqrt{3}a^{2}c/2$, where $a$ and $c$ are the lattice constants. Equation (3) is evaluated by finite differences between two configurations: first that of the ground state, and then for an $\eta_{j}$ macroscopic strain relative to this ground state. For this latter configuration the atoms are once again relaxed to respond to the macroscopic strain $\eta_{j}$. In our calculations, we have used $\eta_{j}=\pm 1.5\%$. The final value of $e_{ij}$ is taken as the average of two values obtained for these positive and negative strains. $^{8}$

Phonon calculations are also performed within the density functional perturbation theory (DFPT), $^{18}$ using the ABINIT code $^{19}$ and the Hatwigsen, Goedecker, and Hutter (HGH) pseudopotentials. $^{20}$ Convergence for the ground state total energy is attained at a plane-wave cutoff of 110 Ry while using HGH pseudopotentials (Interestingly, these "hard" HGH pseudopotentials yield equilibrium structural and electronic properties that are remarkably close to those predicted using the "much smoother" Vanderbilt ultrasoft pseudopotentials.).

## III. RESULTS

Figures 1(a)-1(c) depict the resulting total energy of 1 $\times 1$ GaN/ScN (4 atoms per cell), $2\times 2$ GaN/ScN (8 atoms per cell), and $1\times 1$ InN/ScN (4 atoms per cell) superlattices, respectively, as a function of the axial ratio (per 4 atom), for different unit cell volumes. $^{21}$ Figure 1 shows that the axial ratio associated with the equilibrium structures is around 1.55-1.60, i.e., is relatively close to its value in the ideal wurtzite structure (that is, 1.633). Hence, we denote these phases as "wurzite-derived." Such phase is schematically depicted in Fig. 1(e). Furthermore, Fig. 1(a) reveals that $1\times 1$ GaN/ScN exhibits only one minimum in the total energy-versus-$c/a$ curve, for any volume as the axial ratio is varied in the range $[1.2,1.6]$. The $c/a$ associated with the minimum energy for each volume continuously decreases from 1.55 to 1.26, when decreasing the volume from 315 Bohr$^{3}$ and 302 Bohr$^{3}$. This change of $c/a$ characterizes a volume-driven second-order phase transition from a wurtzite-derived structure to a phase we will henceforth call as $h$-derived-based on the fact that its axial ratio is rather close to the one ($\simeq 1.207$) of the $h$ phase of ScN. [Note that the schematic representation of the $h$-derived phase is given in Fig. 1(d).] This phase transition is isostructural in nature since the space group remains unchanged (i.e., $P3m1$) during this transition. The $1\times 1$ GaN/ScN system is thus particularly remarkable since IPTs are particularly rare, especially, when they are of second-order. $^{1}$ Figures 1(b) and 1(c) show that both $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN exhibit a single minimum in their total energy versus $c/a$ curve only for the largest ($c/a\simeq 1.55-1.60$, wurtzite-derived) and the smallest ($c/a\simeq 1.26$, $h$-derived) considered volumes. For intermediate volumes, one can see, unlike $1\times 1$ GaN/ScN, two minima occurring at $c/a$ associated with the $w$-derived and $h$-derived structures. The simultaneous existence of these two minima implies that $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN-unlike $1\times 1$ GaN/ScN-undergo a volume-induced first-order IPT from a wurtzite-derived structure to an $h$-derived phase. This striking difference between $1\times 1$ GaN/ScN and $2\times 2$ GaN/ScN is likely due to a phenomenon also observed in ferroelectrics: $^{23}$ the superlattice with the shortest possible period acts as a single-component system (leading, in $1\times 1$ GaN/ScN, to a single minimum with $c/a$ neither equal to 1.20-1.25 nor 1.55-1.60 for intermediate volumes) while increasing the period allows the superlattice to adopt features associated with each parent compound

![](./images/812279892610646017_1.jpg)

FIG. 1. (Color online) Total energy as a function of axial ratio $c/a$ for various volumes in $1\times 1$ GaN/ScN (a), $2\times 2$ GaN/ScN (b), and $1\times 1$ InN/ScN (c). The total energy of the equilibrium structure is set to zero for each material. (d) and (e) depict the hexagonal-derived and the wurtzite-derived structures, respectively, for the $1\times 1$ GaN/ScN system, with the white, black, and shaded spheres representing Sc, N, and Ga atoms, respectively.

(yielding two minima for intermediate volumes in $2\times 2$ GaN/ScN). Moreover, the difference between $1\times 1$ GaN/ScN and $1\times 1$ InN/ScN may result from a competition between two main effects: (i) a size effect: lower volume favors the $h$-derived minimum while higher volume stabilizes the wurtzite-derived minimum in the superlattices (see Fig. 1), and (ii) a chemical effect: hexagonal ScN stabilizes in the $h$-structure while pure GaN and InN ground-states are wurtzite. In fact, item (i) conflicts with item (ii) in $1\times 1$ GaN/ScN because the ionic radius of Ga is smaller than Sc (as it can be deduced from Ref. 6). This forces $1\times 1$ GaN/ScN to act as a "collaborative" material. Such conflict does not exist in $1\times 1$ InN/ScN since In ion is larger than Sc ion,⁶ allowing such superlattice to behave more as a two-component (parentlike) system.

We now wonder how the phase transitions seen in Fig. 1 "translate" when varying the (experimentally-accessible) hydrostatic pressure, rather than the (experimentally-

![](./images/812279892610646017_2.jpg)

FIG. 2. Structural properties of $1\times 1$ GaN/ScN as a function of pressure: (a) in-plane lattice constant, (b) axial ratio per 4 atoms, (c) internal parameters, and (d) volume per 4 atoms. (e)-(h) [respectively, (i)-(l)]: Same as (a)-(d) but for $2\times 2$ GaN/ScN (respectively, $1\times 1$ InN/ScN).

inaccessible) continuous change in $c/a$ at fixed volumes. Practically, for the $1\times 1$ GaN/ScN material, each single minimum energy associated with each volume is collected to derive the relationships between hydrostatic pressure ($P$), enthalpy ($H$), and volume ($V$), via a fit to a Birch equation of state. $^{24}$ On the other hand, two different $P$ vs $V$ equations of state (one for the wurtzite-derived phase and the other for the $h$-derived structure) are derived both for $2\times 2$ GaN/ScN and $1\times 1$ In/ScN. Two distinct $H$ vs $P$ curves are thus obtained from these two separate equations of states. Comparing them reveals the pressure-stability of the two phases: we numerically found that the nearly 4 times coordinated wurtzite-derived phase has the lowest enthalpy and is thus the most stable structure below $\approx$7.5 GPa (respectively, 2 GPa) in $2\times 2$ GaN/ScN (respectively, $1\times 1$ In/ScN), while higher pressure stabilizes the five-time coordinated $h$-derived structure. $^{25}$ Such evolution from equilibrium wurtzite-derived structure to the high pressure hexagonal-derived structure is consistent with the empirical rule stating that the coordination number should increase with pressure. $^{27}$ Interestingly, these transition pressures are within easy reach of experimental capabilities nowadays. This—in addition to the facts that hexagonal (Sc,Ga)N have already been synthesized$^{10}$ and that superlattices have already been grown in nitride semiconductors, $^{22}$ in general, and in GaN/ScN, $^{28}$ in particular—makes us believe that our predictions will soon be experimentally confirmed.

In the following, we report various physical properties in the pressure range corresponding to the phase stability, i.e., for the wurtzite derived ($h$-derived) structure below (above) the critical pressure. Figures 2(a)-2(d) depict the in-plane lattice constant $a$, the axial ratio $c/a$, the internal coordinates ($\langle u_{\text{ScN}}\rangle$ and $\langle u_{\text{GaN}}\rangle$) and the volume per 4 atoms, respectively, as a function of pressure in $1\times 1$ GaN/ScN. Figures 2(e)-2(h) [respectively, (i)-(l)] display the same information, but for the $2\times 2$ GaN/ScN (respectively, $1\times 1$ InN/ScN) superlattice. The pressure evolution of $a$, $c/a$, $\langle u_{\text{ScN}}\rangle$, and $\langle u_{\text{GaN}}\rangle$ depict that a sharp, but continuous, transition takes place at $\approx$12 GPa in $1\times 1$ GaN/ScN. The equilibrium structures below 12 GPa are wurtzite-derived, as emphasized by the facts that $c/a$ is close to 1.55 and that both $\langle u_{\text{GaN}}\rangle$ and $\langle u_{\text{ScN}}\rangle$ are around 0.375. At higher pressure, the equilibrium structures are $h$-derived with $c/a\simeq1.25$ and the internal parameters being very close to 0.5. The second-order character of this pressure-induced IPT is undoubtedly confirmed by the fact that the volume does not exhibit any noticeable jump [see Fig. 2(d)], even for pressures around 12 GPa—for which $a$ and $c/a$ dramatically depend on pressure. On the other hand, Figs. 2(e)-2(l) show that $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN both undergo a pressure-induced IPT between a wurtzite-derived and a $h$-derived phase with a first-order character, since all the structural data exhibit a sudden jump at the transition pressure. For instance, the volume decreases by $\approx$5% (respectively, 9%) when passsing from below a pressure $\approx$7.5 (respectively, 2 GPa), in the Ga-mixed (respectively, In-mixed) alloy, which are quantitative

![](./images/812279892610646017_3.jpg)

FIG. 3. Lowest transverse optical zone-center $A_1$ phonon frequency in $1\times 1$ GaN/ScN (a) and piezoelectric coefficients in $1\times 1$ GaN/ScN (b), $2\times 2$ GaN/ScN (c), and $1\times 1$ InN/ScN (d), as a function of pressure. Note that we did not find any negative phonon frequency in any stable structure discussed in this article. In particular, the negative phonon frequency of (a) is reported just to show that the $h$-derived phase (but not the wurztite-derived state) is dynamically unstable around 12 GPa.

changes typical of first-order transitions. $^1$ From a fundamental point of view, Fig. 2 also clearly reveals that the axial ratio (which is related to the strain) and the internal $u$ parameters (which are related to optical phonon modes) act as order parameters of IPT in GaN/ScN and InN/ScN superlattices. These order parameters are "trivial" in the sense that they are less unusual, and easier to detect, than those proposed and/or observed in previously reported IPTs. $^{1-5}$

To gain deeper understanding of the driving forces responsible for these IPTs, we performed phonon calculations within the density functional perturbation theory. $^{18}$ Figure 3(a) shows that the zone-center $A_1$(TO) mode—which is associated with the identity representation and thus preserves the symmetry—is a soft-mode in $1\times 1$ GaN/ScN: as the pressure approaches the critical point (12 GPa) from either side, the frequency of this mode dramatically decreases, and the system undergoes a (lattice-dynamics-driven) second-order IPT to avoid the frequency of this $A_1$(TO) mode to become negative. On the other hand, we did not find any soft mode in $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN, indicating that the first-order IPT in these systems is static in nature, and "solely" arises from the formation of the two total-energy minima shown in Figs. 1(b) and 1(c). This difference in phonon behaviors between $1\times 1$ GaN/ScN and both $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN has dramatic consequence for some physical properties, such as piezoelectricity and dielectric constant. For instance, Figs. 3(b)-3(d) show that the $e_{33}$ piezoelectric coefficient—as predicted within the modern theory of polarization $^{16}$—adopts huge values around the critical pressure in $1\times 1$ GaN/ScN—as consistent with the softening of the zone-center transverse optical phonon— while the first-order character of the IPT in $2\times 2$ GaN/ScN and $1\times 1$ InN/ScN prevents the piezoelectricity from being very large in these two systems. Figures 3(b)-3(d) also show that the $e_{33}$ piezoelectric coefficient of the three studied systems is $\approx 2$ C/m$^2$ at atmospheric pressure (for which the wurtzite phase is stable), while it becomes negligibly small for much larger pressures (as consistent with the fact that the high-pressure structure is derived from the nonpolar $h$-phase).

## IV. CONCLUSION
In conclusion, our first-principles calculations predict that GaN/ScN and InN/ScN superlattices undergo a pressure-induced isostructural phase transition. These IPTs are associated with trivial order parameters and generate dramatic changes in structural, dynamical, and piezoelectric properties.

We also found (not shown here) rather distinct behaviors and values, at low vs high pressure, for other physical quantities, e.g., total and electronic dielectric constant, optical band gap and Born effective charges. These facts should help in observing the IPTs in GaN/ScN and InN/ScN superlattices via various experimental techniques. We also hope that our reported first-principles calculations and analysis will encourage more work in the fascinating topic of IPT, in general, and will help in further developing theory of these phase transitions, in particular.

## ACKNOWLEDGMENTS
We are grateful for the financial assistance provided by the NSF Grants Nos. DMR-0080054, DMR-9983678, and DMR-0102755, the ONR Grants Nos. N00014-01-0365, N00014-01-1-0600, and N00014-04-1-0413, and the NATO Grant No. PST.CLG.979025. The authors also acknowledge H. Fu, I. Kornev, and I. Naumov for useful discussions, and A. R. Smith for communicating experimental results before publication. Computational support has been provided by the Center for Piezoelectrics by Design.

---

$^1$P. Tolèdano, K. Knorr, L. Ehm, and W. Depmeier, Phys. Rev. B 67, 144106 (2003).
$^2$A. Alavi, A. Y. Lozovoi, and M. W. Finnis, Phys. Rev. Lett. 83, 979 (1999).
$^3$J. S. Tse, S. Desgreniers, Z. Q. Liu, M. R. Ferguson, and Y. Kawazoe, Phys. Rev. Lett. 89, 195507 (2002).
$^4$J. S. Tse and D. D. Klug, Phys. Rev. Lett. 81, 2466 (1998).
$^5$L. Bellaiche, K. Kunc, and J. M. Besson, Phys. Rev. B 54, 8945 (1996).
$^6$N. Farrer and L. Bellaiche, Phys. Rev. B 66, 201203(R) (2002).
$^7$V. Ranjan, L. Bellaiche, and E. J. Walter, Phys. Rev. Lett. 90, 257602 (2003).


$^{8}$A. Al-Yacoub and L. Bellaiche, Appl. Phys. Lett. 79, 2166 (2001).

$^{9}$M. Leroux and B. Gil, *Gallium Nitride and Related Semiconduc- tors*, No. 23 in emis DATAREVIEWS SERIES (INSPEC, London, 1999), pp. 45–51.

$^{10}$C. Constantin, H. Al-Brithen, M. B. Haider, D. Ingram, and A. R. Smith, Phys. Rev. B 70, 193309 (2004).

$^{11}$P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1964); W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 (1965).

$^{12}$D. Vanderbilt, Phys. Rev. B 41, R7892 (1990).

$^{13}$D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).

$^{14}$J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).

$^{15}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).

$^{16}$R. D. King-Smith and D. Vanderbilt, Phys. Rev. B 47, R1651 (1993).

$^{17}$D. Vanderbilt, J. Phys. Chem. Solids 61, 147 (2000).

$^{18}$S. Baroni, P. Giannozzi, and A. Testa, Phys. Rev. Lett. 58, 1861 (1987); P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, Phys. Rev. B 43, 7231 (1991).

$^{19}$X. Gonze *et al.*, Comput. Mater. Sci. 25, 478 (2002); The ABINIT code is a common project of the Universit Catholique de Louvain, Corning Incorporated, and other contributors (URL http://www.abinit.org).

$^{20}$C. Hartwigsen, S. Goedecker, and J. Hutter, Phys. Rev. B 58, 3641 (1998).

$^{21}$We do not consider here any degree of interface roughness for our superlattices because (a) such consideration would lead to supercells that are too large for first-principles calculations, and (b) grown short-period nitride superlattice can exhibit ideal like interface (Ref. 22).

$^{22}$P. Ruterana *et al.*, Appl. Phys. Lett. 72, 1742 (1998).

$^{23}$M. Sepliarsky, S. R. Phillpot, D. Wolf, M. G. Stachiotti, and R. L. Migoni, Phys. Rev. B 64, 060101(R) (2001).

$^{24}$F. Birch, J. Geophys. Res. 57, 227 (1952).

$^{25}$Note that the use of the generalized gradient approximation (GGA) (Ref. 26), gives results that are qualitatively similar to, as well as of the same order of magnitude than, the LDA ones reported here. In particular, the first order IPT in $1\times 1$ InN/ScN occurs at around 7 GPa within GGA.

$^{26}$J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

$^{27}$N. E. Christensen, S. Satpathy, and Z. Pawlowska, Phys. Rev. B 36, 1032 (1987).

$^{28}$M. E. Little and M. E. Kordesch, Appl. Phys. Lett. 78, 2891 (2001).