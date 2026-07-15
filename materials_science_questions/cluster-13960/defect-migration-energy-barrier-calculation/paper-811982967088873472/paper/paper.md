This article was downloaded by: [University of Auckland Library]
On: 29 October 2014, At: 19:18
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954
Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811982967088873472_1.jpg)

# Molecular Simulation
Publication details, including instructions for
authors and subscription information:
http://www.tandfonline.com/loi/gmos20

# Oxygen Adsorption on Zr(0001): An ab Initio Study
G. Jomard $^{a b}$ , T. Petit $^{b}$ , L. Magaud $^{c}$ , A. Pasturel $^{a}$ , G. Kresse $^{d}$ & J. Hafner d

$^{a}$ Laboratoire de Physique et Modélisation des Milieux Condensés B.P. 166 CNRS, 38042, Grenoble-Cedex, France
$^{b}$ CEA-Grenoble/DRN/DEC/SESC 17 rue des Martyrs, 38054, Grenoble Cedex 9, France
$^{c}$ Laboratoire d'Etudes des Propriétés Electroniques des Solides B.P. 166 CNRS, 38042, Grenoble-Cedex, France
$^{d}$ Institut für Theoretische Physik, Technische Universität Wien, Wiedner Haupstrasse 8-10, A-1040, Wien, Austria

Published online: 23 Sep 2006.

To cite this article: G. Jomard, T. Petit, L. Magaud, A. Pasturel, G. Kresse & J. Hafner (2000) Oxygen Adsorption on Zr(0001): An ab Initio Study, Molecular Simulation, 24:1-3, 111-129, DOI:  10.1080/08927020008024191

To link to this article: http://dx.doi.org/10.1080/08927020008024191

---

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the

Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# OXYGEN ADSORPTION ON Zr(0001): AN *AB INITIO* STUDY

G. JOMARD${}^{\text{a,b}}$, T. PETIT${}^{\text{b}}$, L. MAGAUD${}^{\text{c}}$, A. PASTUREL${}^{\text{a}}$, G. KRESSE${}^{\text{d}}$ and J. HAFNER${}^{\text{d},*}$

${}^{\text{a}}$Laboratoire de Physique et Modélisation des Milieux Condensés B.P. 166 CNRS, 38042 Grenoble-Cedex, France; ${}^{\text{b}}$CEA-Grenoble/DRN/DEC/SESC 17 rue des Martyrs, 38054 Grenoble Cedex 9, France; ${}^{\text{c}}$Laboratoire d'Etudes des Propriétés Electroniques des Solides B.P. 166 CNRS, 38042 Grenoble-Cedex, France;
${}^{\text{d}}$Institut für Theoretische Physik, Technische Universität Wien, Wiedner Haupstrasse 8-10, A-1040 Wien, Austria

(Received April 1999; accepted May 1999)

The main goal of this paper is to study the oxygen adsorption on the Zr(0001) surface using first-principles total-energy calculations based on density-functional theory. We present preliminary results which concern the atomic oxygen adsorption on the Zr(0001) surface. We first report a static study where we calculate the atomic structure and adsorption energy for oxygen occupying various surface and subsurface sites at three different coverages: $\Theta=1/4$, $1/2$, and 1 ML. We find that oxygen atoms are preferentially adsorbed into the octahedral holes between the 2nd and 3rd metallic layers. We secondly perform *ab initio* molecular dynamics calculations for the $\text{Zr(0001)}-(3\times3)-\text{O}$ system to show how the oxygen can penetrate through the surface and how it finally reaches its equilibrium position, trapped between the 1st and 2nd zirconium layers.

Keywords: Oxygen adsorption; zirconium

## INTRODUCTION

Understanding the mechanisms of the oxidation of the zirconium surface is a great challenge since this metal and its alloys are widely used in nuclear industry, mainly as fuel cells in pressurized water nuclear reactors (PWR). In such an environment, a thin oxide film grows on zirconium and plays an

*Corresponding author.

important role of media between the metal and the operating system. But owing to the huge difficulty involved in such an investigation, we may first study more academic systems. It is the purpose of this work where we present a recent study of the oxygen interaction with the clean Zr(0001) surface.

As for many other metals, it is well known that dissociative adsorption of oxygen takes place on the zirconium surface, but the interaction of oxygen adatoms with the metal surface is very uncommon since various Auger Electrons Spectroscopy (AES), Low Energy Electrons Diffraction (LEED), and work-function measurements favor subsurface adsorption models. Foord *et al.* [1] who studied the adsorption and absorption of diatomic gases by polycristalline zirconium at 300 K by means of Auger and $\Delta\phi$ measurements (work-function measurements) show that in case of oxygen, the adsorption is almost entirely dissociative. They also observed a rapid surface-to-bulk diffusion when heating these adsorbed phases. The same conclusions are reported by Hoflund *et al.* [2]. Many experiments have also been carried out on monocrystalline zirconium, the system of interest being Zr(0001) – O [3–10]. For example, Hui *et al.*, observed a $(2 \times 2)$ LEED pattern at a 0.5 monolayers (ML) coverage [3]. As it is generally done, they used multiple scattering calculations to find the structural model which gives the best agreement with their experimental results. All surface models in which adsorbed O atoms are bonded above the zirconium surface give essentially no correspondence. The best agreement is found for a model where the O atoms occupy the subsurface octahedral sites. The low temperature experiments of Griffiths [5] indicate that even at $T = 82\,\text{K}$, there is a transfer of oxygen atoms from the surface to subsurface sites and that oxygen remains below the surface region for temperatures up to $\sim 570\,\text{K}$ resulting in the formation of a $(2 \times 2)$ LEED pattern. More recently, Zhang *et al.*, combining LEED, AES, and NRA (Nuclear Reaction Analysis) measurements have shown that this $(2 \times 2)$ LEED pattern (observed at 0.5 ML oxygen coverage) originates from three domains of $(1 \times 2)$ superstructure rotated by $120^\circ$ to each other [6]. Moreover, both their Auger and $\Delta\phi$ results are consistent with the hypothesis that the $(1 \times 2)$ superstructure arises from the filling of half of the octahedral sites between the first and the second surface layers of zirconium. Wang *et al.*, have also made a tensor LEED analysis for the half monolayer structure formed by O adsorbed at the Zr(0001) surface [9]. They conclude that O atoms occupy octahedral holes in an unreconstructed metallic structure, with 0.25 ML between the 1st and 2nd metal layers, and another 0.25 ML between the 2nd and 3rd metal layers. These two $(2 \times 2) - \text{O}$ arrays are displaced laterally

from one another by an unit translational vector of the Zr(0001) substrate.
For the 1 ML structure formed by O at this surface, the same authors have
shown that the observed $(1\times1)$-type LEED pattern may be explained by
a structural model where a half monolayer of O is distributed statistically
over the octahedral sites between the 1st and 2nd metal layers, and a fur-
ther half monolayer resides between the 2nd and 3rd Zr layers [10].

On the theoretical point of view, investigations of the O/Zr(0001) systems
are scarce. To our knowledge there is only one such study [11]; Yamamoto
*et al.*, performed first-principles total energy calculations for the subsurface
adsorption of oxygen on the Zr(0001) surface using a mixed-basis pseudo-
potential method within the local-density approximation. They studied both
the $\mathrm{Zr}(0001)-(1\times1)-\mathrm{O}$ and $\mathrm{Zr}(0001)-(2\times1)-\mathrm{O}$ systems and found
that the energetically most favorable occupation sites for oxygen are the
octahedral ones between the 2nd and 3rd layers (with a single oxygen layer
model). Their study is restricted to static calculations, but to explain how
oxygen atoms can reach the subsurface sites, a dynamic approach is needed.
In this contribution we employ both static and dynamic calculations to
address the question of how the oxygen atoms penetrate through the
compact Zr(0001) surface.

## COMPUTATIONAL METHOD

For our investigation, we use the Vienna *ab initio* simulation program VASP
which is based on the following principles. A finite-temperature density-
functional approximation is used to solve the generalized Kohn-Sham
equations with an efficient iterative matrix diagonalization scheme based
on a conjugate gradient technique and optimized density mixing routines.
Within this framework, the free energy is the variational functional and a
fractional occupancy of the eigenstates is allowed which eliminates all insta-
bilities resulting from level crossing and quasi-degeneracies in the vicinity
of the Fermi level in metallic systems. The exchange-correlation functional
given by Ceperley and Alder is used in the parametrization of Perdew and
Zunger [12]. Non-local exchange-correlation effects are considered in the
form of generalized-gradient corrections (GGCs). We used the Perdew-
Wang [13] GGC functional. The GGCs are applied self-consistently in
the construction of the pseudopotentials as well as in the calculations of
the Kohn-Sham ground state. Forces on the atoms and stresses on the
unit cell are calculated through the Hellmann-Feynman theorem as the
variational derivative of the free energy with respect to atomic positions

and cell parameters. The geometry optimization can be readily carried out by using the conjugate-gradient method again. The calculations have been performed using fully non-local optimized ultrasoft pseudopotentials [14,15] allowing small energy cut-offs. For the present calculation of ultrasoft pseudopotentials, the atomic reference configurations were $4 p^{6}$  $5 s^{1} 4 d^{3}$ for Zr, and $2 s^{2} 2 p^{4}$ for O. The accuracy of these two pseudo potentials has been checked elsewhere for bulk $ZrO_{2}$ [16] and for clean Zr(0001) surface [17].

Since we are interested in the subsurface adsorption of oxygen atoms, a sufficiently thick slab must be used for modelling the Zr surface. We use a periodic slab of twelve atomic layers separated by a vacuum region corresponding to the thickness of four such atomic layers. Such a slab is thick enough to guarantee a good convergence of the calculations with respect to (i) the number of surface layers that are allowed to relax, (ii) the total number of layers in the slab, and (iii) the thickness of the vacuum layer separating the repeated slabs. All the atoms are allowed to move except the atoms of the two central layers which are fixed at their bulk positions. The tetrahedron method combined with Blöchl corrections has been used for the Brillouin zone integration. The convergence of the adsorp- tion energy with the k-mesh has been obtained for 3 irreducible k points in the Brillouin zone for the $Zr(0001)-(2 ×2)-O$ system, 25 irreducible k points for the $Zr(0001)-(2 ×1)-O$ system, and 19 irreducible k points for the $Zr(0001)-(1 ×1)-O$ system. Atomic positions are optimized by means of the Hellmann-Feynman theorem which gives forces on the atoms, combined with a minimization procedure of conjugate-gradient- type. For these calculations, we used the equilibrium lattice parameters obtained for bulk Zr, i.e., within LDA $a=3.158 \AA, c / a=1.615$ , and with Perdew-Wang GGCs $a=3.235 \AA, c / a=1.605$ .

The ab initio molecular dynamics are performed using the same code. The atomic motion is described in a microcanonical statistical ensemble. The equations of motion are integrated using a fourth-order predictor-corrector algorithm which allows the use of time steps as large as $3 \times$ 10-15s with good energy conservation. After moving the atoms, the new wave functions are estimated by using the subspace alignment proposed by Arias, Payne, and Joannopoulos [18]. The calculations are performed with the same non-local pseudopotentials as for the static study. For our simu- lations, we use a temperature T = 573 K, the oxygen atom landing normal to the Zr(0001) surface with an initial kinetic energy of 3.5eV. The slab modelling the surface is composed of 6 metal layers separated by a vacuum region of thickness corresponding to 6 such layers repeated periodically

in space. The lower two slab layers are kept fixed in their bulk atomic arrangement and the upper four layers are allowed to relax in the pres- ence of oxygen. To avoid interactions between the different oxygen atoms involved by the use of periodic boundary conditions in the plane of the surface, we use an oxygen coverage as small as $\Theta=1 / 9$ leading to a 55 atoms supercell.

The time step for the integration of the atomic equations of motion is1 fs. We only work within the local density approximation of the DFT, the Methfessel-Paxton method is used for the Brillouin zone integration and a set of 3 irreducible $k$ points is sufficient to achieve convergence of the energy.

# RESULTS AND DISCUSSION

## Energetics of Oxygen Adsorption: A Static Approach

In the following, we will use the same symbols as ones given by Yamamoto and coworkers [11] to define the adsorption sites. An octahedral site locat- ed between the $i$ th and $j$ th metal layers will be denoted $O(i j)$ ; whereas a tetrahedral site will be described by $T(i j: a$ (or $b) k)$ if it is located between the $i$ th and $j$ th metal layers just above (or below) the $k$ th $Zr$ layer. For a better understanding of these symbols, we present in Figure 1 the two slabsused to modelize the $Zr(0001)-(1 \times 1)-O$ and $Zr(0001)-(2 \times 1)-O$  systems. We study sites from surface positions to subsurface ones located between the 4th and 5th metal layers, computing for each one the bindingand adsorption energies defined by:

$$
E_{b}(\Theta)=\frac{\left[E_{\text {total }}^{\text {slab }}(\Theta)-E_{\text {total }}^{\text {Zr slab }}\right]}{N_{\text {oxygen }}}-E_{\text {total }}^{\text {oxygen atom }}
\tag{1}
$$

and,

$$
E_{a d}(\Theta)=E_{b}(\Theta)+\frac{D}{2}
\tag{2}
$$

Here $E_{total }^{slab }(\Theta)$ is the total energy of the slab with an oxygen coverage $\Theta$ corresponding to the ratio of the number of oxygen atoms $N_{oxygen }$ to the number of zirconium surface atoms in the cell. $E_{total }^{Zr slab }$ is the total energy of the clean $Zr(0001)$ surface slab. The $E_{total }^{oxygen atom }$ is the total energy of an isolated oxygen atom, and $D$ is the dissociation energy of the $O_{2}$ molecule. A spin-polarized calculation is needed to compute these

![](./images/811982967088873472_2.jpg)

FIGURE 1 Representation of the slabs used to modelize the $Zr(0001)-(1 \times 1)-O$ and $Zr(0001)-(2 \times 1)-O$ systems.

two values. However we have checked that spin-polarization has no effect on $E_{total}^{slab}(\Theta)$ and $E_{total}^{Zr slab}$. Whereas Yamamoto and coworkers have included the experimental value 5.116 eV [19] in their calculations, we use our own *ab initio* dissociation energy which is 6.72 eV within LDA and 6.05 eV adding gradient corrections of PW91-type. The overestimation of $D$ is a well-known deficiency of DFT but it does not affect the main conclusions of the present study.

Our calculated binding energies are given in Tables I and II. They are also plotted versus the distance between the oxygen plane and the Zr surface plane in Figures 2 and 3. We will first discuss the LDA-based results; within this approximation, the most favorable adsorption site is the O(23) one both for 0.5 ML and 1 ML oxygen coverages. This is consistent with the conclusion given by Yamamoto *et al.* [11] (with almost the same method), and with the subsurface adsorption reported experimentally. We note however a significant difference with their results

<table>
<caption>TABLE I Calculated binding energy and adsorption energy per oxygen atom VASP LDA. Atomic positions of the oxygen adsorbed system are not relaxed</caption>
<thead>
<tr>
<th rowspan="2">Adsorption site</th>
<th colspan="2">$Zr(0001)-(2×1)-O$, $\Theta=1/2$</th>
<th colspan="2">$Zr(0001)-(1×1)-O$, $\Theta=1$</th>
</tr>
<tr>
<th>$E_{b}(eV)$</th>
<th>$E_{ad}(eV)$</th>
<th>$E_{b}(eV)$</th>
<th>$E_{ad}(eV)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>O(top)</td>
<td>$-9.24$</td>
<td>$-5.88$</td>
<td>$-8.68$</td>
<td>$-5.32$</td>
</tr>
<tr>
<td>O(12)</td>
<td>$-9.47$</td>
<td>$-6.11$</td>
<td>$-9.09$</td>
<td>$-5.72$</td>
</tr>
<tr>
<td>O(23)</td>
<td>$-9.90$</td>
<td>$-6.54$</td>
<td>$-9.46$</td>
<td>$-6.10$</td>
</tr>
<tr>
<td>O(34)</td>
<td>$-9.80$</td>
<td>$-6.43$</td>
<td>$-9.36$</td>
<td>$-6.00$</td>
</tr>
<tr>
<td>O(45)</td>
<td>$-9.77$</td>
<td>$-6.41$</td>
<td>$-9.35$</td>
<td>$-5.99$</td>
</tr>
<tr>
<td>T(top)</td>
<td>$-9.06$</td>
<td>$-5.70$</td>
<td>$-8.54$</td>
<td>$-5.17$</td>
</tr>
<tr>
<td>$T(12:a2)$</td>
<td>$-6.16$</td>
<td>$-2.80$</td>
<td>$-5.81$</td>
<td>$-2.45$</td>
</tr>
<tr>
<td>$T(12:b1)$</td>
<td>$-6.48$</td>
<td>$-3.12$</td>
<td>$-6.31$</td>
<td>$-2.95$</td>
</tr>
<tr>
<td>$T(23:a3)$</td>
<td>$-6.26$</td>
<td>$-2.90$</td>
<td>$-5.93$</td>
<td>$-2.57$</td>
</tr>
<tr>
<td>$T(23:b2)$</td>
<td>$-6.32$</td>
<td>$-2.96$</td>
<td>$-6.03$</td>
<td>$-2.67$</td>
</tr>
<tr>
<td>$T(34:a4)$</td>
<td>$-6.27$</td>
<td>$-2.91$</td>
<td>$-5.95$</td>
<td>$-2.59$</td>
</tr>
<tr>
<td>$T(34:b3)$</td>
<td>$-6.28$</td>
<td>$-2.92$</td>
<td>$-5.99$</td>
<td>$-2.63$</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE II Calculated binding energy and adsorption energy per oxygen atom VASP PW91. Atomic positions of the oxygen adsorbed system are not relaxed</caption>
<thead>
<tr>
<th rowspan="2">Adsorption site</th>
<th colspan="2">$Zr(0001)-(2×2)-O$,
$\Theta=1/4$</th>
<th colspan="2">$Zr(0001)-(2×1)-O$,
$\Theta=1/2$</th>
<th colspan="2">$Zr(0001)-(1×1)-O$,
$\Theta=1$</th>
</tr>
<tr>
<th>$E_{b}(eV)$</th>
<th>$E_{ad}(eV)$</th>
<th>$E_{b}(eV)$</th>
<th>$E_{ad}(eV)$</th>
<th>$E_{b}(eV)$</th>
<th>$E_{ad}(eV)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>O(top)</td>
<td>$-8.50$</td>
<td>$-5.47$</td>
<td>$-8.45$</td>
<td>$-5.43$</td>
<td>$-7.91$</td>
<td>$-4.89$</td>
</tr>
<tr>
<td>O(12)</td>
<td>$-8.37$</td>
<td>$-5.34$</td>
<td>$-8.39$</td>
<td>$-5.37$</td>
<td>$-7.99$</td>
<td>$-4.96$</td>
</tr>
<tr>
<td>O(23)</td>
<td>$-8.82$</td>
<td>$-5.80$</td>
<td>$-8.81$</td>
<td>$-5.79$</td>
<td>$-8.44$</td>
<td>$-5.41$</td>
</tr>
<tr>
<td>O(34)</td>
<td>$-8.69$</td>
<td>$-5.67$</td>
<td>$-8.72$</td>
<td>$-5.69$</td>
<td>$-8.33$</td>
<td>$-5.31$</td>
</tr>
<tr>
<td>O(45)</td>
<td>$-8.68$</td>
<td>$-5.65$</td>
<td>$-8.68$</td>
<td>$-5.66$</td>
<td>$-8.32$</td>
<td>$-5.29$</td>
</tr>
<tr>
<td>T(top)</td>
<td>$-8.29$</td>
<td>$-5.26$</td>
<td>$-8.25$</td>
<td>$-5.22$</td>
<td>$-7.76$</td>
<td>$-4.73$</td>
</tr>
<tr>
<td>$T(12:a2)$</td>
<td>$-5.66$</td>
<td>$-2.63$</td>
<td>$-5.66$</td>
<td>$-2.63$</td>
<td>$-5.30$</td>
<td>$-2.27$</td>
</tr>
<tr>
<td>$T(12:b1)$</td>
<td>$-5.87$</td>
<td>$-2.84$</td>
<td>$-5.92$</td>
<td>$-2.90$</td>
<td>$-5.78$</td>
<td>$-2.75$</td>
</tr>
<tr>
<td>$T(23:a3)$</td>
<td>$-5.71$</td>
<td>$-2.68$</td>
<td>$-5.72$</td>
<td>$-2.69$</td>
<td>$-5.43$</td>
<td>$-2.40$</td>
</tr>
<tr>
<td>$T(23:b2)$</td>
<td>$-5.75$</td>
<td>$-2.72$</td>
<td>$-5.76$</td>
<td>$-2.74$</td>
<td>$-5.49$</td>
<td>$-2.46$</td>
</tr>
<tr>
<td>$T(34:a4)$</td>
<td>$-5.73$</td>
<td>$-2.70$</td>
<td>$-5.72$</td>
<td>$-2.70$</td>
<td>$-5.45$</td>
<td>$-2.42$</td>
</tr>
<tr>
<td>$T(34:b3)$</td>
<td>$-5.76$</td>
<td>$-2.73$</td>
<td>$-5.73$</td>
<td>$-2.70$</td>
<td>$-5.47$</td>
<td>$-2.45$</td>
</tr>
</tbody>
</table>

for the specific $T(12:a2)$ site of the $(2×1)$ structure which is found to be very unstable. In fact, when the atoms are allowed to relax, we observed that the oxygen atom initially located in the $T(12:a2)$ tetrahedral site moves up to the surface and falls in the $T$(top) surface site. The same feature is observed for coverages smaller than 1 ML for both LDA-based calcula- tions and GGCS-based ones. We propose that this is due to the strain induced in the plane of the surface by the presence of oxygen. This strain can be easily relaxed when the oxygen coverage is small, allowing the oxygen atom to pass through the surface via the $T(12:a2)\to T$(top) channel.

A detailed analysis of the curves presented in Figures 2 and 3 reveals that, if oxygen is adsorbed on-top of the Zr surface, it would prefer to

![](./images/811982967088873472_3.jpg)

FIGURE 2 Comparison of binding energies obtained for unrelaxed, and relaxed atomic positions (VASP LDA).

reside in the fcc hollow-site (O(top)) than in the hcp hollow-one ($T$(top)). Indeed, the fcc-type surface site is slightly more favorable by about 0.22 eV for the $(2\times1)$ and about 0.19 eV for the $(1\times1)$ structure. For the sub-surface adsorption sites, we see that the tetrahedral holes are always less stable than the octahedral ones. The energy difference between these two different sites increases when the oxygen coverage decreases as it is the case for the fcc and hcp surface sites. This indicates that at the early stages of the zirconium oxidation, the octahedral adsorption sites will be the preferred ones. Before relaxation, we can see that the curves for the octahedral sites have only one minimum for O(23). When relaxation effects are introduced, the fcc-type surface site is strongly stabilized, and then O(12) becomes the less stable site. It is 0.31 eV above the O(23) site in the $(2\times1)$ structure, and 0.32 eV in the $(1\times1)$ structure. Then we can conclude that the oxygen atom cannot be adsorbed directly between the 1st and 2nd Zr layers at a fictitious temperature of $T=0$ K. For the octahedral sites located deeper in the bulk, a constant adsorption energy

![](./images/811982967088873472_4.jpg)

FIGURE 3 Comparison of binding energies obtained for unrelaxed, and relaxed atomic positions (VASP PW91).

value of about $-6.48\mathrm{eV}$ for the $(2\times1)$ structure and $-6.10\mathrm{eV}$ for the $(1\times1)$ structure is obtained. This constant value compares fairly well with the dissolution energy of oxygen into the bulk $\alpha$-Zr which as been re-ported to be $-6.42$ to $-5.85\mathrm{eV}$ per oxygen atom [20]. Moreover, it is a

well-known experimental result that oxygen atoms are dissolved in the octahedral holes of bulk hcp Zr metal.

If we look at the variation of $E_b$ with the oxygen coverage, we find that greater is the coverage, less bound are the oxygen atoms. Moreover, even for the 1 ML coverage, the binding at the subsurface sites is greater than the calculated binding energies of oxygen in bulk zirconia which are $-8.43\mathrm{eV}$, $-8.40\mathrm{eV}$, and $-8.39\mathrm{eV}$ for the monoclinic, tetragonal, and cubic structures respectively (this is within LDA). The GGCs-based corresponding values are $-8.41\mathrm{eV}$, $-8.35\mathrm{eV}$, and $-8.31\mathrm{eV}$ [16]. We defined them as follows:

$$
E_{b}=\frac{E_{\text {total }}^{\mathrm{ZrO}_{2}}-E_{\text {total }}^{\mathrm{Zr} \text { hcp }}}{2}-E_{\text {total }}^{\text {oxygen }} \tag{3}
$$

This result is consistent with various experimental works which report a great incorporation of oxygen into the bulk Zr (up to 30 at%) before the growth of the oxide.

Keeping in mind that our LDA-based results are in good agreement with many experimental studies, we now turn to the discussion of the GGCs based results. The main difference between the results given by these two approaches is the binding energy of the fcc hollow-site. Indeed, within the GGCs, the most stable adsorption site is no longer the octahedral O(23) site but the fcc-type surface site, from $\Theta=0.25\,\text{ML}$ to $1\,\text{ML}$. However, the curves of Figures 2 and 3 still display a secondary minimum for the O(23) adsorption site. The fcc-type surface site is 0.19 eV below the later for the $(2\times2)$ structure, 0.21 eV for the $(2\times1)$ structure, and 0.18 eV for the $(1\times1)$ structure. Actually these results are not in disagreement with a subsurface adsorption of oxygen in Zr(0001)/O systems, but they do not allow to conclude that oxygen is adsorbed directly below the surface. Like for the LDA-based results some energy barrier needs to be jumped to go through the surface. Let us point out here that this conclusion is valid at $T=0\,\text{K}$. But it does not exclude that this barrier could disappear with temperature, or could be crossed by an appropriated reaction channel.

## Zr Interlayer Distances Variation Upon Oxygen Adsorption

For each system studied above, we compute the variation of the interlayer distances with respect to the bulk Zr value. We also calculate the minimal $\text{Zr}—\text{O}$ separation, both in 3D space $(r_{\text{Zr}—\text{O}}^{\text{min}})$ and along the direction normal to the surface $(z_{\text{Zr}—\text{O}}^{\text{min}})$. When $\Theta$ is lower than 1, we observe a corrugation of the zirconium layers. In that case the calculation of

$z_{\mathrm{Zr}-\mathrm{O}}^{\min }$ is done using an average value for the $z$ coordinate of the $\mathrm{Zr}$ planes. Our LDA-based results are shown in Table III while the gradient-corrected ones are given in Table IV. We define $\Delta_{i j}$ as follows:

$$
\Delta_{i j}=\frac{d_{i j}-d_{0}}{d_{0}} \tag{4}
$$

where $d_{i j}$ is the distance between the $i$ th and $j$ th $\mathrm{Zr}$ planes and $d_{0}$ the interlayer distance in bulk $\mathrm{Zr}$.

As the two sets of calculations are very close together, we will only discuss gradient corrected based values. If we compare the different calculated variations among the various oxygen coverages, we can see that the relaxations in the $z$ direction decrease with $\Theta$. This certainly can be explained

<table>
<caption>TABLE III Interlayer relaxations calculated within the local-density-approximation</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="5">Relaxation (%)</th>
<th colspan="2">Distance (Å)</th>
</tr>
<tr>
<th>$\Delta_{12}$</th>
<th>$\Delta_{23}$</th>
<th>$\Delta_{34}$</th>
<th>$\Delta_{45}$</th>
<th>$\Delta_{56}$</th>
<th>$r_{\mathrm{Zr}-\mathrm{O}}^{\min }$</th>
<th>$z_{\mathrm{Zr}-\mathrm{O}}^{\min }$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8">$\mathrm{Zr}(0001)-(2 × 1)-\mathrm{O}, \Theta=1 / 2$, octahedral sites:</td>
</tr>
<tr>
<td>O(top)</td>
<td>+4.3</td>
<td>+1.2</td>
<td>0.0</td>
<td>+0.5</td>
<td>0.0</td>
<td>2.06</td>
<td>1.01</td>
</tr>
<tr>
<td>O(12)</td>
<td>0.0</td>
<td>−0.5</td>
<td>+1.1</td>
<td>−0.4</td>
<td>0.0</td>
<td>2.23</td>
<td>1.25</td>
</tr>
<tr>
<td>O(23)</td>
<td>−2.6</td>
<td>+4.7</td>
<td>−2.0</td>
<td>0.0</td>
<td>−0.2</td>
<td>2.24</td>
<td>1.31</td>
</tr>
<tr>
<td>O(34)</td>
<td>−5.1</td>
<td>0.0</td>
<td>+4.5</td>
<td>−1.4</td>
<td>−0.5</td>
<td>2.24</td>
<td>1.30</td>
</tr>
<tr>
<td>O(45)</td>
<td>−5.2</td>
<td>+1.0</td>
<td>+0.5</td>
<td>+0.2</td>
<td>−0.0</td>
<td>2.23</td>
<td>1.30</td>
</tr>
<tr>
<td colspan="8">$\mathrm{Zr}(0001)-(2 × 1)-\mathrm{O}, \Theta=1 / 2$, tetrahedral sites:</td>
</tr>
<tr>
<td>T(top)</td>
<td>+7.1</td>
<td>+3.1</td>
<td>−1.1</td>
<td>+0.7</td>
<td>−0.2</td>
<td>2.11</td>
<td>1.07</td>
</tr>
<tr>
<td>T(12:a2)</td>
<td>+7.3</td>
<td>+2.9</td>
<td>−2.8</td>
<td>+0.9</td>
<td>−1.1</td>
<td>2.12</td>
<td>1.06</td>
</tr>
<tr>
<td>T(12:b1)</td>
<td>+6.9</td>
<td>+3.7</td>
<td>+1.6</td>
<td>−2.5</td>
<td>+0.3</td>
<td>2.06</td>
<td>0.68</td>
</tr>
<tr>
<td>T(23:a3)</td>
<td>−3.6</td>
<td>+17.9</td>
<td>−0.3</td>
<td>−2.8</td>
<td>−2.5</td>
<td>1.99</td>
<td>0.96</td>
</tr>
<tr>
<td>T(23:b2)</td>
<td>−5.2</td>
<td>+8.7</td>
<td>+6.3</td>
<td>−5.9</td>
<td>0.0</td>
<td>2.07</td>
<td>0.67</td>
</tr>
<tr>
<td>T(34:a4)</td>
<td>−8.1</td>
<td>+3.8</td>
<td>+11.4</td>
<td>−0.6</td>
<td>−2.9</td>
<td>2.03</td>
<td>0.75</td>
</tr>
<tr>
<td>T(34:b3)</td>
<td>−8.0</td>
<td>+2.4</td>
<td>+7.0</td>
<td>+4.8</td>
<td>+0.7</td>
<td>2.03</td>
<td>0.74</td>
</tr>
<tr>
<td colspan="8">$\mathrm{Zr}(0001)-(1 × 1)-\mathrm{O}, \Theta=1$, octahedral sites:</td>
</tr>
<tr>
<td>O(top)</td>
<td>+4.7</td>
<td>+1.5</td>
<td>−0.8</td>
<td>+0.5</td>
<td>0.0</td>
<td>2.05</td>
<td>0.93</td>
</tr>
<tr>
<td>O(12)</td>
<td>+6.6</td>
<td>−0.5</td>
<td>+0.6</td>
<td>−1.0</td>
<td>−0.9</td>
<td>2.26</td>
<td>1.34</td>
</tr>
<tr>
<td>O(23)</td>
<td>−3.0</td>
<td>+6.6</td>
<td>−0.2</td>
<td>−0.5</td>
<td>−1.4</td>
<td>2.27</td>
<td>1.36</td>
</tr>
<tr>
<td>O(34)</td>
<td>−4.1</td>
<td>−0.3</td>
<td>+7.3</td>
<td>−0.9</td>
<td>−1.4</td>
<td>2.28</td>
<td>1.36</td>
</tr>
<tr>
<td>O(45)</td>
<td>−6.3</td>
<td>+2.3</td>
<td>−0.4</td>
<td>+5.5</td>
<td>−1.1</td>
<td>2.26</td>
<td>1.34</td>
</tr>
<tr>
<td colspan="8">$\mathrm{Zr}(0001)-(1 × 1)-\mathrm{O}, \Theta=1$, tetrahedral sites:</td>
</tr>
<tr>
<td>T(top)</td>
<td>+7.3</td>
<td>0.0</td>
<td>−1.0</td>
<td>+0.5</td>
<td>−0.2</td>
<td>2.05</td>
<td>0.94</td>
</tr>
<tr>
<td>T(12:a2)</td>
<td>+28.1</td>
<td>+3.6</td>
<td>+1.4</td>
<td>−0.7</td>
<td>−0.3</td>
<td>2.04</td>
<td>1.23</td>
</tr>
<tr>
<td>T(12:b1)</td>
<td>+27.0</td>
<td>+2.6</td>
<td>+0.1</td>
<td>−0.3</td>
<td>−0.6</td>
<td>1.99</td>
<td>1.24</td>
</tr>
<tr>
<td>T(23:a3)</td>
<td>−2.1</td>
<td>+30.0</td>
<td>+4.5</td>
<td>−1.0</td>
<td>+0.1</td>
<td>2.04</td>
<td>1.27</td>
</tr>
<tr>
<td>T(23:b2)</td>
<td>−2.0</td>
<td>+28.2</td>
<td>+2.3</td>
<td>−1.0</td>
<td>−1.8</td>
<td>2.05</td>
<td>1.22</td>
</tr>
<tr>
<td>T(34:a4)</td>
<td>−5.0</td>
<td>+3.3</td>
<td>+29.0</td>
<td>+4.6</td>
<td>0.0</td>
<td>2.03</td>
<td>1.25</td>
</tr>
<tr>
<td>T(34:b3)</td>
<td>−6.3</td>
<td>+4.5</td>
<td>+29.0</td>
<td>+1.8</td>
<td>+1.3</td>
<td>2.05</td>
<td>1.24</td>
</tr>
<tr>
<td>$(1 × 1)$–Experiment</td>
<td>+3.1</td>
<td>+2.3</td>
<td>+0.4</td>
<td>0.0</td>
<td></td>
<td>2.28</td>
<td>1.31</td>
</tr>
</tbody>
</table>

<table><caption>TABLE IV Interlayer relaxations calculated including generalized gradient corrections of Perdew-Wang type (PW91)</caption>
<thead>
<tr>
<th></th>
<th colspan="5">Relaxation (%)</th>
<th colspan="2">Distance ($\mathring{A}$)</th>
</tr>
<tr>
<th></th>
<th>$\Delta_{12}$</th>
<th>$\Delta_{23}$</th>
<th>$\Delta_{34}$</th>
<th>$\Delta_{45}$</th>
<th>$\Delta_{56}$</th>
<th>$r_{Zr-O}^{min}$</th>
<th>$z_{Zr-O}^{min}$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="8">$\text{Zr}(0001)-(2\times2)-\text{O}$, $\Theta=1/4$, octahedral sites:</td>
</tr>
<tr>
<td>O(top)</td>
<td>$-1.0$</td>
<td>$-1.1$</td>
<td>$-1.0$</td>
<td>$-1.1$</td>
<td>$+2.1$</td>
<td>$2.10$</td>
<td>$1.04$</td>
</tr>
<tr>
<td>O(12)</td>
<td>$-2.6$</td>
<td>$-0.4$</td>
<td>$+2.1$</td>
<td>$-1.8$</td>
<td>$+1.2$</td>
<td>$2.25$</td>
<td>$1.22$</td>
</tr>
<tr>
<td>O(23)</td>
<td>$-3.7$</td>
<td>$+1.9$</td>
<td>$+1.1$</td>
<td>$-1.1$</td>
<td>$+1.3$</td>
<td>$2.27$</td>
<td>$1.32$</td>
</tr>
<tr>
<td>O(34)</td>
<td>$-6.6$</td>
<td>$+1.9$</td>
<td>$+2.3$</td>
<td>$-1.4$</td>
<td>$+0.7$</td>
<td>$2.29$</td>
<td>$1.33$</td>
</tr>
<tr>
<td>O(45)</td>
<td>$-7.0$</td>
<td>$+2.3$</td>
<td>$-0.2$</td>
<td>$+2.1$</td>
<td>$-0.6$</td>
<td>$2.29$</td>
<td>$1.33$</td>
</tr>
<tr>
<td colspan="8">$\text{Zr}(0001)-(2\times2)-\text{O}$, $\Theta=1/4$, tetrahedral sites:</td>
</tr>
<tr>
<td>$T(\text{top})$</td>
<td>$+0.3$</td>
<td>$+0.5$</td>
<td>$+0.6$</td>
<td>$-0.6$</td>
<td>$+1.3$</td>
<td>$2.11$</td>
<td>$1.01$</td>
</tr>
<tr>
<td>$T(12:a2)$</td>
<td>$+1.3$</td>
<td>$-0.3$</td>
<td>$0.0$</td>
<td>$-0.8$</td>
<td>$-0.5$</td>
<td>$2.11$</td>
<td>$1.01$</td>
</tr>
<tr>
<td>$T(12:b1)$</td>
<td>$-0.1$</td>
<td>$+2.8$</td>
<td>$+1.6$</td>
<td>$-1.8$</td>
<td>$+1.1$</td>
<td>$2.12$</td>
<td>$0.48$</td>
</tr>
<tr>
<td>$T(23:a3)$</td>
<td>$+0.1$</td>
<td>$+6.1$</td>
<td>$-0.9$</td>
<td>$-1.9$</td>
<td>$-0.2$</td>
<td>$2.08$</td>
<td>$0.69$</td>
</tr>
<tr>
<td>$T(23:b2)$</td>
<td>$-6.3$</td>
<td>$+4.2$</td>
<td>$+3.7$</td>
<td>$-1.7$</td>
<td>$+1.3$</td>
<td>$2.04$</td>
<td>$0.52$</td>
</tr>
<tr>
<td>$T(34:a4)$</td>
<td>$-4.0$</td>
<td>$+2.2$</td>
<td>$+2.6$</td>
<td>$-0.5$</td>
<td>$-0.5$</td>
<td>$2.14$</td>
<td>$0.49$</td>
</tr>
<tr>
<td>$T(34:b3)$</td>
<td>$-6.4$</td>
<td>$+4.0$</td>
<td>$+2.4$</td>
<td>$+1.7$</td>
<td>$+0.4$</td>
<td>$2.11$</td>
<td>$0.57$</td>
</tr>
<tr>
<td colspan="8">$\text{Zr}(0001)-(2\times1)-\text{O}$, $\Theta=1/2$, octahedral sites:</td>
</tr>
<tr>
<td>O(top)</td>
<td>$+4.1$</td>
<td>$+3.9$</td>
<td>$-1.8$</td>
<td>$+1.6$</td>
<td>$-0.5$</td>
<td>$2.09$</td>
<td>$1.01$</td>
</tr>
<tr>
<td>O(12)</td>
<td>$0.0$</td>
<td>$-1.0$</td>
<td>$+2.5$</td>
<td>$-2.2$</td>
<td>$1.8$</td>
<td>$2.24$</td>
<td>$1.26$</td>
</tr>
<tr>
<td>O(23)</td>
<td>$-3.0$</td>
<td>$+1.2$</td>
<td>$+1.7$</td>
<td>$-1.3$</td>
<td>$+1.1$</td>
<td>$2.28$</td>
<td>$1.33$</td>
</tr>
<tr>
<td>O(34)</td>
<td>$-6.5$</td>
<td>$+2.0$</td>
<td>$+1.6$</td>
<td>$-0.3$</td>
<td>$+0.6$</td>
<td>$2.29$</td>
<td>$1.33$</td>
</tr>
<tr>
<td>O(45)</td>
<td>$-7.2$</td>
<td>$+3.0$</td>
<td>$0.0$</td>
<td>$+1.0$</td>
<td>$-1.2$</td>
<td>$2.28$</td>
<td>$1.32$</td>
</tr>
<tr>
<td colspan="8">$\text{Zr}(0001)-(2\times1)-\text{O}$, $\Theta=1/2$, tetrahedral sites:</td>
</tr>
<tr>
<td>$T(\text{top})$</td>
<td>$+7.7$</td>
<td>$+3.4$</td>
<td>$-2.8$</td>
<td>$+1.4$</td>
<td>$-1.0$</td>
<td>$2.09$</td>
<td>$1.04$</td>
</tr>
<tr>
<td>$T(12:a2)$</td>
<td>$+6.6$</td>
<td>$+1.4$</td>
<td>$-4.1$</td>
<td>$+0.3$</td>
<td>$-2.9$</td>
<td>$2.15$</td>
<td>$1.03$</td>
</tr>
<tr>
<td>$T(12:b1)$</td>
<td>$+5.6$</td>
<td>$+3.9$</td>
<td>$+0.7$</td>
<td>$-2.6$</td>
<td>$+1.8$</td>
<td>$2.10$</td>
<td>$0.65$</td>
</tr>
<tr>
<td>$T(23:a3)$</td>
<td>$-2.1$</td>
<td>$+30.3$</td>
<td>$+4.2$</td>
<td>$0.0$</td>
<td>$0.0$</td>
<td>$2.08$</td>
<td>$0.79$</td>
</tr>
<tr>
<td>$T(23:b2)$</td>
<td>$-6.4$</td>
<td>$+6.6$</td>
<td>$+4.2$</td>
<td>$-0.8$</td>
<td>$-1.8$</td>
<td>$2.14$</td>
<td>$0.63$</td>
</tr>
<tr>
<td>$T(34:a4)$</td>
<td>$-8.6$</td>
<td>$+5.3$</td>
<td>$+9.6$</td>
<td>$-0.1$</td>
<td>$-2.0$</td>
<td>$2.10$</td>
<td>$0.69$</td>
</tr>
<tr>
<td>$T(34:b3)$</td>
<td>$-7.1$</td>
<td>$+1.5$</td>
<td>$+8.3$</td>
<td>$+3.2$</td>
<td>$-2.2$</td>
<td>$2.09$</td>
<td>$0.70$</td>
</tr>
<tr>
<td colspan="8">$\text{Zr}(0001)-(1\times1)-\text{O}$, $\Theta=1$, octahedral sites:</td>
</tr>
<tr>
<td>O(top)</td>
<td>$+5.1$</td>
<td>$+1.2$</td>
<td>$-0.5$</td>
<td>$+0.9$</td>
<td>$-0.5$</td>
<td>$2.09$</td>
<td>$0.93$</td>
</tr>
<tr>
<td>O(12)</td>
<td>$+6.3$</td>
<td>$-0.8$</td>
<td>$+1.2$</td>
<td>$-0.9$</td>
<td>$-1.0$</td>
<td>$2.30$</td>
<td>$1.35$</td>
</tr>
<tr>
<td>O(23)</td>
<td>$-4.0$</td>
<td>$+7.4$</td>
<td>$-0.8$</td>
<td>$+0.2$</td>
<td>$-0.4$</td>
<td>$2.33$</td>
<td>$1.39$</td>
</tr>
<tr>
<td>O(34)</td>
<td>$-5.6$</td>
<td>$0.0$</td>
<td>$+7.6$</td>
<td>$-1.5$</td>
<td>$-1.3$</td>
<td>$2.33$</td>
<td>$1.39$</td>
</tr>
<tr>
<td>O(45)</td>
<td>$-6.7$</td>
<td>$+2.7$</td>
<td>$-1.6$</td>
<td>$+6.5$</td>
<td>$-1.8$</td>
<td>$2.32$</td>
<td>$1.38$</td>
</tr>
<tr>
<td colspan="8">$\text{Zr}(0001)-(1\times1)-\text{O}$, $\Theta=1$, tetrahedral sites:</td>
</tr>
<tr>
<td>$T(\text{top})$</td>
<td>$+7.5$</td>
<td>$-0.4$</td>
<td>$-0.5$</td>
<td>$+0.7$</td>
<td>$-0.5$</td>
<td>$2.08$</td>
<td>$0.92$</td>
</tr>
<tr>
<td>$T(12:a2)$</td>
<td>$+27.5$</td>
<td>$+4.5$</td>
<td>$-1.0$</td>
<td>$-0.3$</td>
<td>$0.0$</td>
<td>$2.06$</td>
<td>$1.24$</td>
</tr>
<tr>
<td>$T(12:b1)$</td>
<td>$+25.7$</td>
<td>$+1.1$</td>
<td>$-1.3$</td>
<td>$-1.7$</td>
<td>$-2.1$</td>
<td>$2.00$</td>
<td>$1.26$</td>
</tr>
<tr>
<td>$T(23:a3)$</td>
<td>$-3.1$</td>
<td>$+29.5$</td>
<td>$+1.8$</td>
<td>$-2.1$</td>
<td>$-1.0$</td>
<td>$2.06$</td>
<td>$1.30$</td>
</tr>
<tr>
<td>$T(23:b2)$</td>
<td>$-2.8$</td>
<td>$+28.3$</td>
<td>$+3.1$</td>
<td>$+0.4$</td>
<td>$-0.5$</td>
<td>$2.08$</td>
<td>$1.25$</td>
</tr>
<tr>
<td>$T(34:a4)$</td>
<td>$-5.6$</td>
<td>$+3.0$</td>
<td>$+28.2$</td>
<td>$+3.7$</td>
<td>$-0.4$</td>
<td>$2.05$</td>
<td>$1.27$</td>
</tr>
<tr>
<td>$T(34:b3)$</td>
<td>$-7.0$</td>
<td>$+4.5$</td>
<td>$+28.3$</td>
<td>$+1.2$</td>
<td>$+1.0$</td>
<td>$2.07$</td>
<td>$1.26$</td>
</tr>
<tr>
<td>$(1\times1)-\text{Experiment}$</td>
<td>$+3.1$</td>
<td>$+2.3$</td>
<td>$+0.4$</td>
<td>$0.0$</td>
<td></td>
<td>$2.28$</td>
<td>$1.31$</td>
</tr>
<tr>
<td>$(2\times2)-\text{Experiment}$</td>
<td>$+2.3$</td>
<td>$+1.6$</td>
<td>$-0.8$</td>
<td>$0.0$</td>
<td></td>
<td>$2.24$</td>
<td>$1.30$</td>
</tr>
</tbody>
</table>

by the fact that for lower coverages, the strains induced by adsorbed oxygen atoms are smaller and then more easily accomodate by the substrate. When oxygen atoms are adsorbed in the subsurface tetrahedral sites, a huge interlayer distance expansion (of order $+30\%$) between the zircon ium planes which sandwich the oxygen plane can be observed. For com- parison, oxygen atoms located in the octahedral holes below the surface induced an expansion of only $6-7\%$ for the $(1\times1)$ structure, this expan sion being often smaller than $5\%$ for $(2\times1)$ and $(2\times2)$ structures. The fact that relaxations are always stronger for the tetrahedral adsorption holes could probably explain why these sites are less favorable than the octahedral ones. In case of adsorptions on-top of the surface, we show in Tables I-IV that even if the fcc hollow-site is more stable than the hcp hollow-site by an amount as important as 0.3eV, the equilibrium distances between the oxygen atom and the surface-plane ($z_{\text{Zr-O}}^{\text{min}}$) are very close together. So an interpretation of the site-preferences cannot be based on strength of the $\text{Zr-O}$ bonds since usually the strengthening of a bond is associated to a shortening of the bond-length. However, if we look carefully at the $\Delta_{ij}$ values given in Tables III and IV, we can emphasize that adsorption in the fcc hollow-site leads to interlayer distances $d_{12}$ which are shorter than the ones obtained in the case of adsorption in the hcp hollow-site. Then in the later situation, the zirconium atoms of the 1st and 2nd metal layers are less bound and it can be an explanation for the fcc hollow-site preference. Let us mentionned that this result is in very good agreement with the recent paper of Feibelman [21] where the author proposes to interpret the O binding-site preferences on close-packed group-VIII metal surfaces by metal-interatom distances consideration. He concludes that the bonds between each O adatom's first- and second-neighbor metal atoms determine the preferences.

We see in Table IV that, both for the octahedral and tetrahedral sites, $r_{\text{Zr-O}}^{\text{min}}$ is quite independent of the oxygen coverage while $z_{\text{Zr-O}}^{\text{min}}$ is minimum for $\Theta=1$, and more or less constant for $\Theta\leq1/2$. For oxygen atoms located in the octahedral holes below the surface, we find that $r_{\text{Zr-O}}^{\text{min}}$ is close to the experimental value measured in the solid solution $\alpha$ phase: $2.27\mathring{\text{A}}$ to $2.32\mathring{\text{A}}$. In an idealized structure, the octahedral holes should be located just in between two $\text{Zr}$ planes leading to $z_{\text{Zr-O}}^{\text{min}}=d_0/2\sim1.30\mathring{\text{A}}$ which is similar to the GGCs-based value. For the tetrahedral sites, $z_{\text{Zr-O}}^{\text{min}}$ should be equal to $d_0/3$ i.e., $0.87\mathring{\text{A}}$. But, contrary to the octahedral sites which are more or less located at their ideal position, the tetrahedral sites are strongly displaced. This displacement is highest for the $(1\times1)$ structure where it is as important as $45\%$. At least, we find that for the

tetrahedral subsurface sites, $z_{\mathrm{Zr-O}}^{\mathrm{min}}$ decreases with the oxygen coverage while at the same time $r_{\mathrm{Zr-O}}^{\mathrm{min}}$ is constant. This is certainly due to the strong in-plane displacements observed for $\Theta<1$ which are about 5-6% of the zirconium interatomic distance for example for the $(2 \times 2)$ superstructure. Let us notice that this value is in very good agreement with the lateral displacements obtained experimentally by Wang and coworkers: $5.9 \%$.

Together with our calculated $\Delta_{i j}, r_{\mathrm{Zr-O}}^{\mathrm{min}}$, and $z_{\mathrm{Zr-O}}^{\mathrm{min}}$, we give the experimental results obatined by Wang *et al.* [9, 10] for the $(1 \times 1)$ and $(2 \times 2)$ structures in Tables III and IV. Let us remember here that their values come from multiple scattering calculations fitted to their experimental LEED curves, and correspond to a model where oxygen atoms occupy octahedral sites and are distributed on two layers, one located between the 1st and 2nd layers of metal, and another one between the 2nd and 3rd layers of metal. Even if the used slabs are built with oxygen atoms all located in the same plane, we can say that $r_{\mathrm{Zr-O}}^{\mathrm{min}}$ and $z_{\mathrm{Zr-O}}^{\mathrm{min}}$ are in good agreement with the experimental results (in the case where oxygen atoms are located in the subsurface octahedral sites).

### Molecular Dynamics Approach of the Penetration of Oxygen through the Surface

In this part of our work, we study more precisely the mechanism of oxygen penetration through the Zr(0001) surface. As shown in Section A, the tetrahedral and octahedral adsorption sites located between the 1st and 2nd metal layers are locally stable as well as the two hcp hollow and fcc hollow surface sites respectively. This indicates that it must exist an energy barrier against the motion of the oxygen atom from a surface site to the subsurface site located just below. Our goal is to calculate this energy barrier for the early stages of the Zr oxidation. Owing to the fact that such *ab initio* calculations are great time-consuming and required so much computer memory, we restrict our investigations to two oxygen coverages, $\Theta=1 / 2$ and $1 / 9 \mathrm{ML}$. This corresponds to $(2 \times 1)$ and $(3 \times 3)$ superstructures. In fact the reason for studying two different oxygen coverages is to make a comparison of what happens when interactions between oxygen atoms are present or not. Indeed, after check-up, the $\mathrm{Zr}(0001)-(3 \times 3)-\mathrm{O}$ appears to be sufficiently big to prevent from important effects due to the oxygen atoms interactions. In this system, oxygen atoms periodically repeated are distant from each other by about $10 \mathring{A}$ in the plane of the surface. The computation of the energy barrier was done as follows: we calculate the energy of the slab for different vertical positions of the oxygen

atoms (keeping its in-plane coordinates fixed) going from the surface site (hcp hollow- or fcc hollow-site) to the subsurface position ($T(12:a2)$ or $O(12)$ respectively). The calculation of the barriers is done within LDA using the lattice parameters previously determined: $a_0 = 3.15825\,\text{\AA}$ and $c/a = 1.615$. We use 3 irreducible $\mathbf{k}$ points for the Brillouin zone integration which is sufficient to converge the surface energy and the interlayer distances relaxation for the clean $(3 \times 3)$ Zr(0001) surface. The so obtained curves are represented in Figures 4 and 5. The deduced energy barriers are $E_{\text{barrier}} = 2.50\,\text{eV}$ for the channel hcp-hollow $\rightarrow T(12:a2)$, and $E_{\text{barrier}} = 3.43\,\text{eV}$ for the channel fcc-hollow $\rightarrow O(12)$ in the case where $\Theta = 1/2$; while $E_{\text{barrier}} = 2.50\,\text{eV}$ and $3.50\,\text{eV}$ both for $\Theta = 1/9$ and $\Theta = 1/2$. Let us remember that these calculations are done for unrelaxed slabs, and for $T = 0\,\text{K}$. Then we may expect a decrease of these two barriers when relaxing atoms at non-zero temperature. These values can be compared to the experimental energy barrier against O diffusion along the [0001] axis of bulk Zr measured by Flinn *et al.* [7], namely $E_a = 2.1\,\text{eV}$ at $573\,\text{K}$. Let us point out that the calculated values are not too far from the experimental one. We have also calculated the relaxed binding energy for oxygen atoms adsorbed in the $O(\text{top})$ and $T(\text{top})$ surface sites. We find that even for $\Theta = 1/9$, the $O(\text{top})$ site is more stable than the $T(\text{top})$ one; the energy difference is about $0.39\,\text{eV}$ and is increased in comparison to what we obtained for the $(2 \times 1)$ and $(1 \times 1)$ structures. The same trend is observed for the $z_{\text{Zr--O}}^{\text{min}}$ distances which are $1.03\,\text{\AA}$ and $1.17\,\text{\AA}$ respectively.

We now turn to the investigation of the mechanism of oxygen penetration through the Zr(0001) surface. We will focus only on channels which start from the two surface sites discussed above. If we just look at the energy barrier values calculated in each case, we can conclude that the oxygen atom penetrates below the metal surface passing through the hcp hollow-site since $E_{\text{barrier}}$ is smaller in that case. But looking at the binding energy of the $T(12:a2)$ site and $O(12)$ site, the conclusion would be a penetration through the fcc-type surface site. To decide between these two mechanisms, we perform *ab initio* molecular dynamics of these two different channels, the starting point being an oxygen atom located $3\,\text{\AA}$ above the Zr(0001) surface (on-top of the fcc hollow or hcp hollow) with a speed normal to the surface corresponding to a kinetic energy of $3.5\,\text{eV}$ slightly greater than the biggest calculated energy barrier. The temperature of the dynamics is chosen to be $573\,\text{K}$ for consistency with the experimental study of Flinn *et al.* [7]. Firstly, we observed that the oxygen atom arriving on-top of the hcp hollow-site penetrates through the surface but is then pushed back by the 2nd Zr layer, and desorbs in

![](./images/811982967088873472_5.jpg)

FIGURE 4 Calculated energy barriers against penetration of oxygen atoms under the
Zr(0001) surface via (a) fcc-hollow surface site, and (b) hcp-hollow surface site for the $(2 \times 1)$
structure (LDA calculations).

![](./images/811982967088873472_6.jpg)

FIGURE 5 Calculated energy barriers against penetration of oxygen atoms under the Zr(0001) surface via (a) fcc-hollow surface site, and (b) hcp-hollow surface site for the $(3 \times 3)$ structure (LDA calculations).

the vacuum region. If the oxygen atom arrives on-top of the fcc hollow-site, not only does it pass through the surface but after that it is trapped between the 1st and 2nd Zr layers. When the oxygen atom reaches the surface a great perturbation due to the displacement of the zirconium atoms from their equilibrium positions occurs and allows the oxygen atom to penetrate below the surface. Then we can imagine that if another oxygen atom arrives just after in the same surface region, it will cross the surface more easily, the energy barrier being lowered. In parallel, we do the same calculation without initial kinetic energy for the oxygen atom. We find that whatever the initial position, the atom does not go through the surface. It reaches an equilibrium position which is either the O(top) site or the $T$(top) site, depending on its initial position. Then we show that if oxygen atoms have sufficient incident energy, they can penetrate under the Zr(0001) surface *via* the fcc hollow and stay between the 1st and 2nd metal layers into octahedral holes. This is highly consistent with the various LEED experiments reported above. Actually to go further we would have to study the mechanism of oxygen penetration with an incident oxygen atom having a lower kinetic energy since 3.5 eV is a quite high value compared to what is observed in adsorption experiments. It is the purpose of our current work together with the investigation of the di-atomic oxygen adsorption.

## CONCLUSION

We have shown that first-principles total-energy calculations based on density-functional theory are able to give a correct description of the Zr(0001) surface oxidation. Our calculations agree well with the subsurface adsorption of oxygen reported by experimental works, the more favorable adsorption site being the octahedral one located between the 2nd and 3rd metal layers. We have pointed out that LDA and GGCs lead to different behaviours of the oxygen binding in Zr(0001)/O systems, especially in the case of the $T(12:a2)$ site. Both set of calculations are consistent with an oxygen dissolution in bulk zirconium before the growth of the oxide since oxygen atoms are more strongly bond in bulk Zr than in zirconia. Finally we found that an energy barrier surface exits against oxygen penetration below the zirconium surface which we estimate to be of order 3.43 eV for $T=0$ K. Then we show, using an *ab initio* molecular dynamics approach, that oxygen atoms can reach the O(12) subsurface site crossing the surface *via* the fcc-hollows if they have a required incident kinetic energy.

### References

[1] Foord, J. S., Goddard, P. J. and Lambert, R. M. (1980). *Surf. Sci.*, **94**, 339.

[2] Hoflund, G. B., Asbury, D. A., Cox, D. F. and Gilbert, R. E. (1985). *Applications of Surf. Sci.*, **22/23**, 252.

[3] Hui, K. C., Milne, R. H., Mitchell, K. A. R., Moore, W. T. and Zhou, M. Y. (1985). *Solid State Comm.*, **56**, 83.

[4] Wong, P. C. and Mitchell, K. A. R. (1987). *Can. J. Phys.*, **65**, 464.

[5] Griffiths, K. (1988). *J. Vac. Sci. Technol. A*, **6**, 210.

[6] Zhang, C.-S., Flinn, B. J., Mitchell, I. V. and Norton, P. R. (1991). *Surf. Sci.*, **245**, 373.

[7] Flinn, B. J., Zhang, C.-S. and Norton, P. R. (1993). *Phys. Rev. B*, **47**, 16499.

[8] Wong, P. C., Hui, K. C., Zhong, B. K. and Mitchell, K. A. R. (1987). *Solid State Commun.*, **62**, 293.

[9] Wang, Y. M., Li, Y. S. and Mitchell, K. A. R. (1995). *Surf. Sci.*, **342**, 272.

[10] Wang, Y. M., Li, Y. S. and Mitchell, K. A. R. (1995). *Surf. Sci.*, **343**, L1167.

[11] Yamamoto, M., Chan, C. T., Ho, K. M. and Naito, S. (1996). *Phys. Rev. B*, **54**, 14111.

[12] Perdew, J. P. and Zunger, A. (1981). *Phys. Rev. B*, **23**, 5048.

[13] Perdew, J. P. and Wang, Y. (1986). *Phys. Rev. B*, **33**, 8800.

[14] Vanderbilt, D. (1990). *Phys. Rev. B*, **41**, 7892.

[15] Kresse, G. and Hafner, J. (1994). *J. Phys.: Condens. Matter*, **6**, 8245.

[16] Jomard, G., Petit, T., Magaud, L., Kresse, G., Hafner, J. and Pasturel, A. (1999). *Phys. Rev. B*, **59**, 4044.

[17] Jomard, G., Petit, T., Magaud, L., Kresse, G., Hafner, J. and Pasturel, A. (1999). *Phys. Rev. B*, **60**, 15624.

[18] Arias, T. A., Payne, M. C. and Joannopoulos, J. D. (1992). *Phys. Rev. B*, **45**, 1538.

[19] Kittel, C., *Introduction to solid states physics*, Edited by J. Whiley & Sons, Inc. (New York, 1976).

[20] *Gase und Kohlenstoff in Metallen*, Edited by Fromm, E. and Gebhardt, E. (Springer, Berlin, 1976).

[21] Feibelman, P. J. (1999). *Phys. Rev. B*, **59**, 2327.