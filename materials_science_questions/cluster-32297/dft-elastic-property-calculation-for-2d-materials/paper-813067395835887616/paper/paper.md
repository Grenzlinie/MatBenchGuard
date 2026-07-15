# Charge density wave states in tantalum dichalcogenides
David C. Miller, Subhendra D. Mahanti, and Phillip M. Duxbury*

Physics and Astronomy Department, Michigan State University, East Lansing, Michigan 48824, USA

![](./images/813067395835887616_1.jpg)
(Received 19 June 2017; revised manuscript received 6 November 2017; published 17 January 2018)

Using density functional theory, we explore a range of charge density wave states (CDWs) in tantalum-based transition-metal dichalcogenide monolayers. The high-symmetry states of the $1H$ phases of $TaX_2$ ($X = S$, Se, Te) are lower in total energy compared to the $1T$ variants, while the $1T$ phases exhibit a much stronger tendency for CDW formation. The stability of several CDWs is found to be stronger as the chalcogenide is changed in the sequence (S, Se, Te), with the tellurium-based systems exhibiting several CDWs with binding energy per formula unit in the range of 100 meV. These $1T$ CDW phases are lower in energy than the corresponding $1H$ CDW phases. The diversity of CDWs exhibited by these materials suggests that many "hidden" states may occur on ultrafast excitation or photodoping. Changes in electronic structure across the $TaX_2$ series are also elucidated.

DOI: 10.1103/PhysRevB.97.045133

## I. INTRODUCTION

Transition-metal dichalcogenides (TMDs) are quasi-two- dimensional materials exhibiting a wide variety of tunable properties that are of both fundamental and applied interest [1,2]. Depending on the composition, structure, number of layers, temperature, doping, and strain, these materials exhibit metallic, superconducting, semiconducting, or insulating be- havior. Additionally, they exhibit a rich variety of different charge density wave (CDW) states [3]. The observation of the coexistence of CDW and superconducting phases in tantalum- based TMDs is of particular fundamental interest, providing a new class of materials where the interplay of these phases can be systematically tuned and explored. More recently, new "hidden" CDW phases have been identified using ultrafast pump-probe experiments.

In $TaX_2$ (where $X = S$, Se, and Te) multiple charge density waves have been experimentally observed in either monolayers or in the bulk. Extensive experimental literature indicates that bulk $1T$-TaS$_2$ forms a commensurate CDW (CCDW) at low temperatures that involves a contraction of the 12 Ta atoms about a central Ta atom (see Fig. 1). The six nearest neighbors form the B sites, and the next-nearest neighbors form the C sites around the central A site, forming a Star of David (SoD) unit. Dense packing of SoD units into the hexagonal lattice requires a rotation of the new primitive lattice vectors of around $13.6^\circ$ from the high-symmetry lattice vectors, as illustrated in Fig. 1, and this rotation is clearly evident in diffraction experiments [4]. When heated slowly, the CCDW undergoes a phase transition to a nearly commensurate CDW (NCCDW) at 180 K, then from the NCCDW to an incommensurate CDW (ICCDW) at 350 K, and, finally, from the ICCDW to the high-symmetry, hexagonal phase at 550 K [5-8]. A similar SoD CCDW structure has been observed in $1T$-TaSe$_2$; however, a direct transition to an ICCDW phase is observed at 430 K with no intermediate NCCDW phase [9]. More recently, the role of metastable phases in tantalum-based CDWs has attracted attention due to the observation of "hidden phases" induced by ultrafast excitation or by photon doping of $1T$-TaS$_2$ [8].

Several different CCDWs have been observed in $1T$-TaTe$_2$: A $3 \times 1$ CCDW structure involving contractions of the inter- mediate sites away from the edges of the unit cell has been observed at room temperature [10], and a $3 \times 3$ structure has been observed at 77 K. The bulk $2H$ structures are also known to exhibit CDWs, with $2H$-TaSe$_2$ displaying a $3 \times 3$ structure below 122 K [3]. These and other CDWs can also occur in other TMDs. For example, $1T$-TiSe$_2$ exhibits a CDW below 232 K with a $2 \times 2$ unit cell that involves displacement of both the Ti and the Se atoms [11,12], and $2H$-NbSe$_2$ displays a $3 \times 3$ CDW below 35 K [3].

A number of superconducting transitions have been ob- served at low temperatures under different conditions. Electron doping (using intercalated Fe, Li, or Cu) yields a supercon- ducting transition in $1T$-TaS$_2$[7,13,14], while the application of pressure can result in the coexistence of a NCCDW and a superconducting state in $1T$-TaS$_2$ [5,6]. Varying the ratio of S and Se in $1T$-TaS$_x$Se$_{2-x}$ [15] or Se and Te in $1T$-TaSe$_x$Te$_{2-x}$ [16,17] also results in a superconducting state. Additionally, in $1T$-TaSe$_x$Te$_{2-x}$ there is a transition between two different CCDWs. In $2H$-TaS$_2$, doping with Ni sup- presses the CDW while increasing the superconducting critical temperature [18-20].

Computational and theoretical studies of tantalum-based TMDs have utilized both parametrized tight-binding models and density functional theory (DFT). Tight-binding models have proven effective in predicting CDW states of bulk $1T$-TaS$_2$ and $2H$-TaSe$_2$ [21-23] and in describing many aspects of the fundamental physics of these systems, although parameterized tight-binding models require DFT calculations to be accurate [24]. Additional studies have also included hybrid functionals to study the in-plane gap in bulk $1T$-TaS$_2$ due to the formation of a CDW [25]. Density-functional- based calculations have predominantly focused on one CDW, while the comprehensive early work of Sharma, Nordström, and Johansson [26] examined the $1T$-TaX$_2$ compounds for supercells corresponding to different single-$\bar{q}$ CDW structures. Although that study focused on the Fermi surface of the

*duxbury@pa.msu.edu

![](./images/813067395835887616_2.jpg)

FIG. 1. The Star of David structure (SoD). Labeled are $\vec{a}'$ and $\vec{b}'$, the new lattice vectors of the $\sqrt{13} \times \sqrt{13}$ supercell. Also shown are $\vec{a}$ and $\vec{b}$, the primitive lattice vectors. The three unique sites of Ta atoms in the SoD structure (A, B, and C) are labeled. The CDW contraction involves a shortening of the A-B and A-C distances along with a rotation of $13.6^\circ$ relative to the primitive lattice vectors. Charge accumulation is more pronounced on the A site than the B sites.

materials, it demonstrated that there are additional metastable phases in $1T$-TaS$_2$ and $1T$-TaSe$_2$. The physical origin of the insulating gap in $1T$-TaS$_2$ has been the topic of several studies [22,24,27], and the effects of strain [28] and doping [16] on this material have been explored. The phonon dispersion of the high-symmetry phases of $1T$-TaS$_2$ [25,27,29], $2H$-TaS$_2$ [25], and $1T$- and $1H$-TaSe$_2$ [20,30,31] has been calculated, showing instabilities with wave vectors that point to the formation of CCDWs.

In this paper we examine the ground-state energy for both $1T$- and $1H$-TaX$_2$ ($X=$ S, Se, Te) monolayers (see Fig. 2) to determine the tendency of tantalum dichalcogenides monolayers to form a range of competing CDW states. The ability to experimentally control such states will provide new avenues to tune and explore the interplay between CDW formation, metal-insulator transitions, and superconductivity.

This paper is arranged as follows. The next section describes the computational methods, Sec. III contains the results and discussion, and Sec. IV provides a summary and outlook. Note that throughout the paper we use "binding energy" as a general term referring to the difference in energy between a state that we are testing and a reference state. We define this difference so that a positive binding energy indicates that the tested state is lower in energy than the reference state.

## II. COMPUTATIONAL METHODS

DFT calculations were performed with the Vienna Ab intio Simulation Package (VASP) [32-35] using projector augmented-wave pseudopotentials [36,37]. For calculation of the lattice parameters the local-density approximation (LDA) using the Ceperley and Alder (CA) exchange and correla- tion functional was implemented [38]. For ionic relaxation and ground-state energy calculations the generalized gradient approximation (GGA) was implemented using the Perdew- Burke-Ernzerhof (PBE) exchange and correlation functional [39]. A variety of other density functionals are available, and the van der Waals interaction is now included in many of them. Several different formulations are available, and some are able to capture the experimental interatomic spacing of layered chalcogenides quite accurately [25,40,41]; most re- cently, better approximations to band gaps have been produced [40]. To test the robustness of our methods, we checked the stability of several cases using the functional optB86b [42-46] which is available in VASP and that has shown promising results for the lattice constants of high-symmetry states of layered chalcogenides [25].

It is well known that the LDA-CA exchange functional typically underestimates lattice parameters, while the GGA- PBE functional typically overestimates them. Consistent with this observation, a recent study found that for $5d$ transition metals LDA-CA provides better lattice parameters, while GGA-PBE typically has a larger percentage error compared to experimental values [47]. Although atomic energies are typically better predicted using GGA-based functionals, there is some uncertainty in deciding the lattice parameters to use in the PBE-GGA calculations. Common choices are the use of experimental lattice parameters and lattice parameters at the LDA-CA minimum and the lattice parameters at the GGA-PBE minimum. Following common protocols, in our calculations we used LDA-CA lattice parameters and GGA-PBE energies. For $1T$-TaX$_2$ systems the calculated lattice parameters were within around $1\%$ of previous theoretical calculations [48], and the systematic energy differences due to changes in lattice parameters of this order are at most a few meV per formula unit.

For the high-symmetry primitive unit cells the in-plane lattice parameter was varied in increments of $10^{-4}$ Å, and for each unit cell the ionic sites were relaxed using the LDA-CA functional such that the ionic forces were less than 0.01 eV/Å. This yielded a local minimum in the LDA-CA energy for the high-symmetry structure. For comparisons of energy the GGA-PBE energy is evaluated using the high-symmetry structure at the LDA-CA minimum. Alternate strategies can and have been used, including using experimental values of the lattice parameters to evaluate the GGA-PBE energy, using the GGA-PBE energy at the GGA-PBE minimum structure, etc. Differences in energy are of the order a few meV, which should be considered a systematic error in the analysis. None

![](./images/813067395835887616_3.jpg)

FIG. 2. The $1T$ (left) and $1H$ (right) primitive structures of TaX$_2$. The $1T$ structure has octahedral symmetry (top left), while the $1H$ structure displays trigonal prismatic symmetry (top right). The bottom illustrations are side views of the first plane of atoms.

<table><caption>Table I. Table of $k$-point grids used for each choice of the unit cell and calculation being performed. An initial relaxation of the lattice is followed by a finer relaxation of the ionic positions and, finally, the electronic relaxation and density of state calculations.</caption>
<tbody><tr><th>Unit cell</th>
<th>Lattice relaxation</th>
<th>Ionic relaxation</th>
<th>Electronic relaxation</th>
<th>Density of states</th></tr>
<tr><td>$1\times1\times1$</td>
<td>$11\times11\times1$</td>
<td>$11\times11\times1$</td>
<td>$25\times25\times1$</td>
<td>$35\times35\times1$</td></tr>
<tr><td>$3\times1\times1$</td>
<td>$4\times12\times1$</td>
<td>$6\times18\times1$</td>
<td>$11\times33\times1$</td>
<td>$15\times45\times1$</td></tr>
<tr><td>$4\times1\times1$</td>
<td>$4\times16\times1$</td>
<td>$4\times16\times1$</td>
<td>$8\times32\times1$</td>
<td>$11\times44\times1$</td></tr>
<tr><td>$2\times2\times1$</td>
<td>$8\times8\times1$</td>
<td>$11\times11\times1$</td>
<td>$21\times21\times1$</td>
<td>$27\times27\times1$</td></tr>
<tr><td>$3\times3\times1$</td>
<td>$6\times6\times1$</td>
<td>$8\times8\times1$</td>
<td>$21\times21\times1$</td>
<td>$25\times25\times1$</td></tr>
<tr><td>$\sqrt{13}\times\sqrt{13}\times1$</td>
<td>$6\times6\times1$</td>
<td>$8\times8\times1$</td>
<td>$15\times15\times1$</td>
<td>$21\times21\times1$</td></tr>
</tbody></table>

of the conclusions drawn in the analysis below are altered by using these different energies definitions, although, of course, the absolute energies differences are different on the scale of a few meV. Use of a coarse $\vec{k}$ mesh or a weaker force convergence criterion can lead to similar energy differences.

Analysis of CDW states starts by forming unit cells that are commensurate with the target structure. The initial lattice positions and cell volume are found by combining a number of high-symmetry unit cells to form a system having the number of atoms and stoichiometry of the target structure. A random displacement of all Ta atom in-plane coordinates in the ranges $1\%$–$3\%$ and $-1\%$ to $-3\%$ is then imposed on the structure, and full ionic relaxation of the distorted structure is carried out using the parameter (ISIF-tag $=4$) in vasp with a force convergence criterion of $0.1$ eV/Å. During the fixed-volume relaxation the $c$-axis lattice parameter is never smaller than $17$ Å. The change in total energy as a result of this decrease in the interlayer distance is less than $0.5$ meV and thus is not considered consequential for the in-layer relaxation. After convergence, the $c$-axis lattice parameter is reset to $23.6$ Å to prevent interlayer interactions. As in the high-symmetry cells, the structure at the LDA minimum is taken to be the most accurate estimate of the CDW state, and its energy is found by evaluating the GGA energy of this structure. During the ionic relaxation, an energy cutoff of $650$ eV is used. After the supercell relaxation, the volume of the system is fixed, and an addition relaxation of the atomic forces is carried out to less than $0.01$ eV/Å. Finally, the electronic structure was calculated with an energy cutoff of $500$ eV. All energies are converged to within $0.1$ meV, so that numerical convergence errors in the reported energies are small.

Because of the different sizes of the unit cells for different CDW structures, each calculation used a different set of $\vec{k}$-point grids, which are reported in Table I. All calculations were performed allowing for spin polarization. A real-space projection of the charge density was generated after relaxing the lattice vectors of the $\sqrt{13}\times\sqrt{13}\times1$ and $3\times3\times1$ unit cells. Calculations of the binding energy required spin-polarized, atom-only calculations for each element. This was performed using a $\Gamma$-point-only mesh, with an energy cutoff of $500$ eV in a noncubic $12$Å $\times13$Å $\times14$Å unit cell. These energies were subtracted from the ground-state energies of each structure to obtain the binding energies.

CDWs in the $1T$ and $1H$ structures for $TaX_2$, with $X$ representing S, Se, and Te, are analyzed in the next section. In addition to the high-symmetry structures, five different CDWs are studied using supercells of the same symmetry, as listed in Table I. An example of the relaxed in-plane Ta structure and the distortions of the Te atoms in the $3\times3$ CDW of $1T$-TaTe$_2$ are presented in Figs. 3 and 4, respectively. Figure 4 compares the side view of the CDW unit cell in the high-symmetry structure, where the positions of the Te atoms are symmetric, to that of the $3\times3$ CDW, where there are significant distortions in the positions of the Te atoms. Surprisingly, as discussed in the next section, the Ta-Te distance remains unchanged in the CDWs,

![](./images/813067395835887616_4.jpg)

FIG. 3. The distortion of Ta atoms in the $3\times3$ CDW in $1T$-TaTe$_2$. The superlattice vectors ($\vec{a}'$ and $\vec{b}'$) are pictured, and the four sites (A, B, C, and D) are labeled. Charge accumulates around the A site with contraction of the A-B, A-C, and B-C interatomic distances. The C-D distance remains similar to the high-symmetry structure, but the B-D and C-C distances are larger than in the high-symmetry case.

![](./images/813067395835887616_5.jpg)

FIG. 4. Side views of the high symmetry (top) and $3\times3$ CDW (bottom) in 1T-TaTe$_2$. In the bottom plot, the Ta sites are labeled according to the definitions in Fig. 3. This highlights the buckling of the Te sites and the increase in the Te-Te layer thickness.

![](./images/813067395835887616_6.jpg)

FIG. 5. The distortions of Ta atoms in the four-atom striped CDW occurring in $1T$-TaSe$_2$ and $1T$-TaS$_2$. Only the supercell lattice vectors ($\vec{a}'$ and $\vec{b}'$) are given, and the four unique sites (A, B, C, and D) are labeled. This CDW involves a shortening of the B-C distances, while the A-B and C-D distances remain nearly the same as in the high-symmetry structure.

while the bond angles change to accommodate changes in the Ta-Ta distances.

It is also important to note that the CDW states within one class may vary from one system to another, as illustrated for the $4\times1$ CDW, where the internal structure is different for $X=\text{Se}$ compared to the $X=\text{Te}$ case (see Figs. 5 and 6, respectively). In TaX$_2$ there is thus a diversity of CDW states with different symmetries, and within each symmetry class there are differences in the internal CDW structure.

### III. RESULTS

#### A. High-symmetry structures

The total energies of the high-symmetry $1T$ and $1H$ phases along with their binding energies are given in Table II. For all three choices of chalcogen the $1H$ phase displays a larger binding energy, although the Ta-$X$ bond length is essentially the same in the $1H$ and $1T$ phases for each chalcogen atom (see Table III). The lattice parameters for $X=\text{S}$, $\text{Se}$ are somewhat larger in the $1T$ phase, while for $X=\text{Te}$ the $1H$ phase has a slightly larger lattice parameter. Overall, the lattice parameters and the height of the monolayer differ by only a couple of percent between the $1T$ and $1H$ phases. The

![](./images/813067395835887616_7.jpg)

FIG. 6. The distortion of Ta atoms in the four-atom striped CDW occurring in $1T$-TaTe$_2$. Only the supercell lattice vectors ($\vec{a}'$ and $\vec{b}'$) are pictured, and the four unique sites (A, B, C, and D) are labeled. This CDW involves a shortening of the A-B, B-C, and C-D distances; however, the B-C contraction is less than the A-B and C-D contractions. Combined with displacement of Ta atoms in the $y$ direction perpendicular to the $\vec{a}'$ lattice vector (upwards in the figure), this results in a two-stripe internal structure within the $4\times1$ CDW.

TABLE II. Energies (eV/f.u.) of the high-symmetry structures of monolayer TaX$_2$ TMDs. $\Delta E$ is the energy difference between the $1T$ and $1H$ phases. Binding energies (BE) are the energy per formula unit calculated by subtracting the energy of a test structure from the energy of the isolated atoms (see Sec. II for more details). This energy is also commonly called the cohesive energy or atomization energy.

| Material | Energy (eV) | | BE (eV) | | $\Delta E$ (meV) |
| --- | --- | --- | --- | --- | --- |
| | $1T$ | $1H$ | $1T$ | $1H$ | |
| TaS$_2$ | $-23.1112$ | $-23.1759$ | $17.252$ | $17.317$ | $64.7$ |
| TaSe$_2$ | $-21.1380$ | $-21.2087$ | $15.652$ | $15.723$ | $70.7$ |
| TaTe$_2$ | $-18.9682$ | $-19.0006$ | $13.809$ | $13.841$ | $32.4$ |

high-symmetry $1H$ phase is significantly lower in energy than the high-symmetry $1T$ phase, by 64.7, 70.7, and 32.4 meV as the chalcogen is changed across the series for S, Se, and Te, respectively.

Band structures of the $1T$ and $1H$ phases are very different (see Figs. 7 and 8) due to the different symmetries of the two phases. In the $1T$ phase the three bands at or above the Fermi level are a mix of the $d_{x^2-y^2}$, $d_{xy}$, and $d_{z^2}$ states of Ta. In the $1H$ phase, there is only a single band crossing the Fermi energy, and it is predominantly the Ta $d_{z^2}$ state. In both phases of the compound TaS$_2$, the $X$ $p$ states reside well below the Fermi energy (below $-1$ eV). However, as the chalcogen size increases, the energy of the $X$ $p$ states moves closer to the lower Ta $d$ states. This increases the hybridization between these states, and this mixing is pronounced in the Te-based compounds. The bands crossing the Fermi energy have higher dispersion in the $1T$ phase, and the band dispersion at the Fermi energy decreases as the chalcogen size increases, although only weakly for the $1H$ phase. Nevertheless, in all cases the bandwidth of the states crossing the Fermi energy is quite broad, indicating that the high-symmetry $1T$ and $1H$ phases are metallic, which is consistent with experiment.

The inclusion of spin-orbit coupling (SOC) in the band structure calculations has a negligible effect in the $1T$ phase. The SOC removes the degeneracy of the bands, but the overall energy changes are small ($\sim0.2$ eV). In contrast to the $1T$ phase, in the $1H$ phase the spin-orbit interaction is more pronounced due to the different symmetry and band structure. This results in spin splitting along the $M$-$K$ and $K$-$\Gamma$ paths for the S and Se structures. Also, in $1H$-TaTe$_2$ there was already spin splitting

TABLE III. Distances for the high-symmetry structures. The lattice parameter $a$ is equivalent to nearest-neighbor Ta-Ta distance. The nearest-neighbor distance between Ta and $X$ is identical in the $1T$ and $1H$ structures. Finally, $h$ is the height of the monolayer (the distance along the $c$ axis between the two $X$ sites).

| Structure | $a$ (Å) | $D_{\text{Ta-}X}$ (Å) | $h$ (Å) |
| --- | --- | --- | --- |
| $1T$-TaS$_2$ | $3.30$ | $2.47$ | $3.13$ |
| $1T$-TaSe$_2$ | $3.42$ | $2.60$ | $3.40$ |
| $1T$-TaTe$_2$ | $3.57$ | $2.80$ | $3.78$ |
| $1H$-TaS$_2$ | $3.28$ | $2.47$ | $3.16$ |
| $1H$-TaSe$_2$ | $3.40$ | $2.60$ | $3.40$ |
| $1H$-TaTe$_2$ | $3.62$ | $2.80$ | $3.75$ |

![](./images/813067395835887616_8.jpg)

FIG. 7. Band structures of the primitive unit cells for the $1T$-Ta$X_2$ materials for (a) S, (b) Se, and (c) Te. The black lines are the standard GGA-PBE calculation with spin polarization, while the orange lines include spin-orbit coupling.

without SOC and a magnetic moment of $0.631\mu_B$/unit cell. This value is larger than previous theoretical calculations for the bulk material [49]. The inclusion of SOC for this structure again does not appear to have much of an effect.

### B. Charge density wave states

The $1T$ and $1H$ CDW binding energies along with unit cell volumes for four charge density wave states are given in Tables IV and V. Only cases that display a CDW binding energy greater than $1\ \text{meV}/\text{Ta}X_2$ are listed. The binding energy of a $1T$ CDW is defined as the difference (per formula unit) between the energy of the high-symmetry $1T$ phase and the energy of the relaxed CDW supercell, with similar analysis for CDWs in the $1H$ phase. A general trend evident from these results is that the $1T$ phase exhibits an instability to formation of a variety of locally stable states with significant CDW binding energy (15–120 meV/f.u.), while the $1H$ phase also has instabilities to the formation of CDWs, albeit with significantly lower binding energies.

The $3\times1$, $4\times1$, $3\times3$, and $\sqrt{13}\times\sqrt{13}$ supercells all display energetically stable distorted phases for the $1T$-Ta$X_2$ compounds. In $1T$-TaS$_2$ only the $4\times1$ and the well-known SoD structures display stable CDWs. In the $1T$ compounds

TABLE IV. CDW binding energy for the $1T$-Ta$X_2$ monolayer structures with $3\times1$, $4\times1$, $3\times3$, and $\sqrt{13}\times\sqrt{13}$ unit cells. For each structure the first column gives the CDW binding energy (BE; meV), and the second column is the change in volume (CV; %) of the unit cell relative to the high-symmetry cell created by extrapolating the lattice vectors of the primitive high-symmetry unit cell. For unit cells that display a CDW binding energy less than 1 meV, no values are given.

<table>
  <thead>
    <tr>
      <th rowspan="2">Unit cell</th>
      <th colspan="2">1T-TaS₂</th>
      <th colspan="2">1T-TaSe₂</th>
      <th colspan="2">1T-TaTe₂</th>
    </tr>
    <tr>
      <th>BE</th>
      <th>CV</th>
      <th>BE</th>
      <th>CV</th>
      <th>BE</th>
      <th>CV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$3\times1$</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>102.9</td>
      <td>$-0.22\%$</td>
    </tr>
    <tr>
      <td>$4\times1$</td>
      <td>15.2</td>
      <td>$-0.02\%$</td>
      <td>36.3</td>
      <td>$0.18\%$</td>
      <td>115.0</td>
      <td>$0.09\%$</td>
    </tr>
    <tr>
      <td>$3\times3$</td>
      <td></td>
      <td></td>
      <td>1.7</td>
      <td>$0.03\%$</td>
      <td>121.6</td>
      <td>$-0.03\%$</td>
    </tr>
    <tr>
      <td>$\sqrt{13}\times\sqrt{13}$</td>
      <td>29.8</td>
      <td>$-0.06\%$</td>
      <td>55.3</td>
      <td>$-0.08\%$</td>
      <td>94.8</td>
      <td>$0.28\%$</td>
    </tr>
  </tbody>
</table>

TABLE V. CDW binding energy for the $1H$-Ta$X_2$ monolayer structures with $3\times1$, $4\times1$, $3\times3$, and $\sqrt{13}\times\sqrt{13}$ unit cells. For each structure the first column gives the CDW binding energy (BE; meV), and the second column is the change in volume (CV; %) of the unit cell relative to the high-symmetry cell created by extrapolating the lattice vectors of the primitive high-symmetry unit cell. For unit cells that display a CDW binding energy less than 1 meV, no values are given.

<table>
  <thead>
    <tr>
      <th rowspan="2">Unit Cell</th>
      <th colspan="2">1H-TaS₂</th>
      <th colspan="2">1H-TaSe₂</th>
      <th colspan="2">1H-TaTe₂</th>
    </tr>
    <tr>
      <th>BE</th>
      <th>CV</th>
      <th>BE</th>
      <th>CV</th>
      <th>BE</th>
      <th>CV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$3\times1$</td>
      <td>3.8</td>
      <td>$-0.12\%$</td>
      <td>1.3</td>
      <td>$+0.13\%$</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$4\times1$</td>
      <td></td>
      <td></td>
      <td>3.5</td>
      <td>$+0.04\%$</td>
      <td>5.1</td>
      <td>$-0.03\%$</td>
    </tr>
    <tr>
      <td>$3\times3$</td>
      <td>3.0</td>
      <td>$+0.02\%$</td>
      <td>3.5</td>
      <td>$+0.10\%$</td>
      <td>5.0</td>
      <td>$-0.04\%$</td>
    </tr>
    <tr>
      <td>$\sqrt{13}\times\sqrt{13}$</td>
      <td></td>
      <td></td>
      <td>2.9</td>
      <td>$+0.08\%$</td>
      <td>10.8</td>
      <td>$-0.10\%$</td>
    </tr>
  </tbody>
</table>

![](./images/813067395835887616_9.jpg)

FIG. 8. Band structures of the high-symmetry structure (no CDW) for the $1H$-Ta$X_2$ materials for (a) S, (b) Se, and (c) Te. The solid (dashed) lines represent the majority (minority) spin for spin-degenerate bands. The black lines are the standard GGA-PBE calculation with spin polarization, while the red lines include spin-orbit coupling.

replacing sulfur with selenium results in the $3 \times 3$ structure becoming energetically stable, but with a very small binding energy ($\sim 2$ meV/TaSe$_2$). The greater diversity, and higher binding energies, of $1T$-TaTe$_2$ CDW states is quite remarkable and may be attributed to the greater tendency to bond angle changes due to the higher polarizability of Te. These results are consistent with experimental observations of multiple CCDW states in this material. We checked the robustness of these LDA-PBE results to a change in density functional by calculating the binding energy (meV/f.u.) using optB86b. For the $3 \times 1$ CDW in $1T$-Ta$X_2$ ($X=$ S, Se, Te) the CDW binding energies are 0,0,105.8, respectively and for the $4 \times 1$ CDW of $1T$-TaS$_2$ we find a value of 12.2. These binding energies are within 4 meV/f.u. of the results found using the LDA-PBE calculations. This provides a good indicator of the variability to be expected for CDW binding energy calculations using different density functionals in common use.

In contrast to the $1T$ cases, the $1H$ CDW structures typically have a significantly smaller binding energy, and none of the $1H$ materials display distorted ground states that differ by more than 11 meV/Ta$X_2$ from the energies of the high-symmetry structures. As noted in the previous section (see Table II), the $1H$ high-symmetry phase has lower energy than the $1T$ phase, and this remains true for the CDW phases of the S and Se compounds. However, the Te compound reverses this trend due to the high binding energy of the $1T$ CDW states, which are the global lowest-energy states of this compound found in our calculations.

Interestingly, the $3 \times 1$ structure does not display a stable CDW structure in $1T$-TaSe$_2$, and the $2 \times 1$ CDW never has a significant binding energy. Only $1T$-TaS$_2$ displays a CDW binding energy for the $2 \times 2$ distorted structure like that found in Ti-based TMDs. However, the binding energy is negligible

![](./images/813067395835887616_10.jpg)

FIG. 9. Plot of the energy per formula unit for $1T$-TaS$_2$ in a $\sqrt{13} \times \sqrt{13}$ unit cell for high-symmetry and CDW phases. Energies are plotted relative to the high-symmetry ground-state energy. Zero strain refers to the lattice parameters of the lowest-energy CDW structure, which differ slightly from the lattice parameters of the high-symmetry ground state. The lowest energy for the high-symmetry unit cell occurs at 0.41% compressive strain.

TABLE VI. The distance between Ta atoms. Listed are the nearest-neighbor distances along with some next-nearest-neighbor distances for the $1T$-$TaX_2$ structures where the distortion is at least 1% of the original Ta-Ta distance in the high-symmetry structure (see Table III). As a result, the $1T$-$TaS_2$ $3 \times 1$ and $1T$-$TaSe_2$ $3 \times 3$ structures are not listed since the distortions are less than the 1% cutoff. All distance are given in angstroms and are listed according to the site label defined in Figs. 1–3. For the $\sqrt{13} \times \sqrt{13}$ structure in $1T$-$TaTe_2$ the nonradial contractions of the Ta atoms make it difficult to classify the C sites. As a result only the A-B distance is given.

<table>
  <thead>
    <tr>
      <th>Structure</th>
      <th>Unit cell</th>
      <th>$D_{AB}$</th>
      <th>$D_{BC}$</th>
      <th>$D_{CD}$</th>
      <th>$D_{AD}$</th>
      <th>$D_{AC}$</th>
      <th>AB (%)</th>
      <th>BC (%)</th>
      <th>CD (%)</th>
      <th>AD (%)</th>
      <th>AC (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1T-TaS2</td>
      <td>$4 \times 1$</td>
      <td>3.282</td>
      <td>3.113</td>
      <td>3.281</td>
      <td>3.547</td>
      <td></td>
      <td>$-0.69\%$</td>
      <td>$-5.82\%$</td>
      <td>$-0.72\%$</td>
      <td>$7.34\%$</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>$\sqrt{13} \times \sqrt{13}$</td>
      <td>3.120</td>
      <td>3.210</td>
      <td></td>
      <td></td>
      <td>5.510</td>
      <td>$-5.59\%$</td>
      <td>$-2.87\%$</td>
      <td></td>
      <td></td>
      <td>$-3.74\%$</td>
    </tr>
    <tr>
      <td>1T-TaSe2</td>
      <td>$4 \times 1$</td>
      <td>3.346</td>
      <td>3.131</td>
      <td>3.346</td>
      <td>3.801</td>
      <td></td>
      <td>$-2.04\%$</td>
      <td>$-8.32\%$</td>
      <td>$-2.04\%$</td>
      <td>$11.29\%$</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>$\sqrt{13} \times \sqrt{13}$</td>
      <td>3.120</td>
      <td>3.156</td>
      <td></td>
      <td></td>
      <td>5.603</td>
      <td>$-8.64\%$</td>
      <td>$-7.59\%$</td>
      <td></td>
      <td></td>
      <td>$-5.28\%$</td>
    </tr>
    <tr>
      <td>1T-TaTe2</td>
      <td>$3 \times 1$</td>
      <td>3.190</td>
      <td>3.190</td>
      <td>4.371</td>
      <td></td>
      <td></td>
      <td>$-10.66\%$</td>
      <td>$-10.66\%$</td>
      <td>$22.42\%$</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>$3 \times 3$</td>
      <td>3.223</td>
      <td>3.099</td>
      <td>3.389</td>
      <td>5.939</td>
      <td>3.238</td>
      <td>$-9.73\%$</td>
      <td>$-13.91\%$</td>
      <td>$-5.08\%$</td>
      <td>$-3.97\%$</td>
      <td>$-9.30\%$</td>
    </tr>
    <tr>
      <td></td>
      <td>$4 \times 1$</td>
      <td>3.273</td>
      <td>3.295</td>
      <td>3.273</td>
      <td>4.370</td>
      <td></td>
      <td>$-8.35\%$</td>
      <td>$-7.72\%$</td>
      <td>$-8.35\%$</td>
      <td>$22.38\%$</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>$\sqrt{13} \times \sqrt{13}$</td>
      <td>3.233</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>$-9.47\%$</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

($\sim 1$ meV/$TaS_2$), and the contraction of the tantalum atoms in the distorted structure is also small ($< 1\%$ of the original Ta-Ta distance).

The volume change on going from the high-symmetry phases to the CDW phases is quite small, and the effects of volume change on the CDW energy are therefore small compared to the effects of the detailed changes in interatomic distances within the supercell. This is illustrated in Fig. 9 for the SoD CDW of the $1T$ phase. In Fig. 9 the minima of the CDW and high-symmetry phases are offset by a small strain (cell volume); however, this does not play a significant role in the binding energy of the CDW. The important internal CDW structural parameters are given in Table VI, which gives the relative distortions for the Ta-Ta distances between various sites in each distorted phase. Despite the small cell volume changes, formation of a CDW is accompanied by significant changes in interatomic distances of the Ta atoms, and these changes are particularly large for $1T$ Te systems (up to on the order of 10%). The $4 \times 1$ CDWs for the S and Se structures have very similar CDW structures. These cases have a single-striped CDW internal structure (see Fig. 5). However, this disappears when the chalcogen is changed to Te, and instead, a double-striped CDW distortion occurs, where the A-B and C-D distances are most significantly contracted (see Fig. 6). Additionally, the Ta displacement is larger perpendicular to the $\vec{a}'$ lattice vector than in the S and Se cases.

In closing this section we note that there are differences in the CDW binding energy for monolayer $1T$-$TaS_2$ reported here compared to previous calculations, which have reported CDW binding energies per formula unit ranging from 19 meV/$TaS_2$ [24] to 31 meV/$TaS_2$ [28]. The value we have calculated lies at the upper end of this range, but this discrepancy points to a dependence of this energy on the exact lattice parameters, coordinates, and computational parameters. Additionally, since relaxed lattice parameters for the high-symmetry cell and the distorted cell may differ, the comparison of these energies can

![](./images/813067395835887616_11.jpg)

FIG. 10. Decomposed density of states for the SoD structures in $1T$-$TaS_2$ and $1T$-$TaSe_2$. The solid black line is the total density of states about the Fermi energy, while the dashed red and dot-dashed green lines are the contributions from the Ta $d$ orbitals and the chalcogen $p$ orbitals. In $1T$-$TaS_2$ the contribution at the Fermi energy is mostly from the Ta $d$ orbitals, while in $1T$-$TaSe_2$ there is a significant contribution from the Se $p$ orbitals. This leads to the exchange splitting of $\sim 0.25$ eV in $1T$-$TaS_2$.


![](./images/813067395835887616_12.jpg)

FIG. 11. Band structure for the SoD structure in (a) $1T$-TaS$_2$, (b) $1T$-TaSe$_2$, and (c) $1T$-TaTe$_2$. where solid (dashed) lines represent majority (minority) spin in cases where this is net spin polarization. The energy is plotted with respect to the Fermi energy.

depend on whether the same cell was used for both calculations. For the protocol used here, i.e., finding lattice parameters using LDA and energies using PBE-GGA, the systematic errors are typically no more than 1 meV/f.u., which is negligible compared to the CDW binding energies discussed above.

### C. Selected band structures

The projected densities of states and band structures of $1T$ Ta$X_2$ SoD CDWs are presented in Figs. 10 and 11 respectively. The most pronounced effect of the CDW distortions is on the TaS$_2$ system even though the binding energies of the Se and Te systems are higher and their CDW distortions are larger. This is due to the fact that in the TaS$_2$ system the band at the Fermi energy in the primitive cell is almost purely $d_{z^2}$, while in the Se and Te cases, there is considerable mixing with the $p$ states of the chalcogen. In the SoD phase of TaS$_2$ the $d_{z^2}$ state splits into 13 subbands, with the subband centered on the A cites at the Fermi energy. This band is very flat and is spin split, so it is expected that many-body Coulomb interactions lead to further spin splitting and hence a Mott insulating behavior in the monolayer. For the bulk TaS$_2$ system the $d_{z^2}$ band has a significant dispersion due to orbital overlap with adjacent layers, and the nature of transport along the $c$ axis is predicted to depend on the CDW stacking [50]. Calculations for the bulk SoD CDW using hybrid functionals (HSE06) have shown an increase of the in-plane gap compared to the calculations using the PBE functional [25]. Experimentally, it is observed that the low-temperature SoD phase of TaS$_2$ is insulating, although there is debate about whether the $c$-axis transport is limited by Mott physics or by other mechanisms .

The $1T$-TaSe$_2$ SoD system displays a similar CDW structure with an increased CDW binding energy and a larger distortion of the Ta-Ta distances. However, the band structure does not resemble that of the sulfur-based system [see Figs. 11(a) and 11(b)]. Comparing the primitive band structures for the $1T$-Ta$X_2$ structures [see Figs. 7(a) and 7(b)], one observes that for increasing chalcogen mass the energy of the highest $X$ $p$ states also increases and is closer in energy to the Ta $d$ states. The resulting band structure for $1T$-TaSe$_2$ has a lower dispersion than the high-symmetry structure but still remains quite dispersive and is expected to be more resistant to a Mott transition, unlike the $1T$-TaS$_2$ SoD case. Additionally, the band structure for the $\sqrt{13} \times \sqrt{13}$ CDW for $1T$-TaTe$_2$ [shown in Fig. 11(c)] shows further differences from the band structures of S and Se. We again attribute these differences to the change in chalcogen and as a result the relative shift in energy for the Te $p$ states.

Shown in Fig. 12 is the band structure for the $4 \times 1$ CDWs in the $1T$-Ta$X_2$ monolayers. In these cases, the CDW distortion results in less dispersive bands, corresponding to more localized states, associated with the distortion of the Ta atoms. However, when compared with the high-symmetry band structures (see Fig. 7) the differences are less significant

![](./images/813067395835887616_13.jpg)

FIG. 12. Band structure for the $4\times1$ CDW structure in (a) $1T$-TaS$_2$, (b) $1T$-TaSe$_2$, and (c) $1T$-TaTe$_2$, where solid (dashed) lines represent majority (minority) spin. The energy is plotted with respect to the Fermi energy.

compared to those occurring in the SoD case. Thus, it is expected that the $4\times1$ structures remain metallic with moderate dispersion ($\sim$1 eV) of the bands near the Fermi energy for all three chalcogens.

## IV. CONCLUSION
We have presented results for the binding energies of a range of CDW states that have been experimentally observed in TMDs. The Ta-based TMD monolayers have a propensity to form CDWs, providing a unique class of materials in which to probe the interplay between superconductivity, CDW formation, metal-insulator transitions, and magnetism. Our calculations show strong evidence for a diversity of metastable phases in both the $1T$ and $1H$ phases of Ta$X_2$ systems, with the $1T$ variant showing a remarkable tendency to form a variety of strongly bound CDW states. The $1H$ phase is the ground state for $X=S$, Se for both the primitive cells and for the CDW states that were studied. However, for $X=$ Te, although the $1H$ primitive cell is lower in energy than the $1T$ primitive cell, there are a variety of $1T$ CDWs that have lower energy than their $1H$ counterparts.

An interesting feature of the CDW structures is that the Ta-$X$ bond length is relatively unchanged by the CDW distortions, and the overall volume of the unit cells also exhibits small changes. In contrast, there are large changes in some of the Ta-Ta distances in the CDWs, with changes on the of order 10% in some of these distances for the Te compounds. There are also strong bond angle changes associated with the Ta-$X$ bond, which provides evidence that the higher polarizability of Te compounds may provide an explanation for their propensity to CDW formation.

Band structure calculations suggest that the $1T$-TaS$_2$ SoD monolayer is expected to be a Mott insulator due to a fairly pure $d_{z^2}$ flat band at the Fermi energy, while all of the other monolayer systems studied are expected to be metallic due to significant dispersion from mixing with the chalcogen $p$ states.

Our study supports the contention that Ta$X_2$ provides an interesting system in which to study the interplay between CDW states and superconductivity, as most of these materials remain conducting in the presence of significant CDW distortions. The exception is TaS$_2$, which is predicted to be a Mott insulator for monolayers, providing an additional avenue to study the interplay between strong electron-electron interactions, CDW states, and superconductivity.

## ACKNOWLEDGMENTS
Computational resources for this work were provided by the High Performance Computing Center at Michigan State University. Funding from the Department of Education through the Graduate Assistantships in Areas of National Need (GAANN) award P200A140215 is gratefully acknowledged. This work was also supported by a Strategic Partnership Grant from the MSU foundation.

[1] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, *Nat. Nanotechnol.* **7**, 699 (2012).

[2] J. Wilson and A. Yoffe, *Adv. Phys.* **18**, 193 (1969).

[3] D. Moncton, J. Axe, and F. DiSalvo, *Phys. Rev. Lett.* **34**, 734 (1975).

[4] P. Williams, C. B. Scruby, W. B. Clark, and G. S. Parry, *J. Phys. Colloq.* **37**, C4-139 (1976).

[5] B. Sipos, A. F. Kusmartseva, A. Akrap, H. Berger, L. Forró, and E. Tutis, *Nat. Mater.* **7**, 960 (2008).

[6] T. Ritschel, J. Trinckauf, G. Garbarino, M. Hanfland, M. V. Zimmermann, H. Berger, B. Büchner, and J. Geck, *Phys. Rev. B* **87**, 125135 (2013).

[7] Y. Yu, F. Yang, X. F. Lu, Y. J. Yan, Y.-H. Cho, L. Ma, X. Niu, S. Kim, Y.-W. Son, D. Feng, S. Li, S.-W. Cheong, X. H. Chen, and Y. Zhang, *Nat. Nanotechnol.* **10**, 270 (2015).

[8] T.-R. T. Han, F. Zhou, C. D. Malliakas, P. M. Duxbury, S. D. Mahanti, M. G. Kanatzidis, and C.-Y. Ruan, *Sci. Adv.* **1**, e1400173 (2015).

[9] K. Horiba, K. Ono, J. H. Oh, T. Kihara, S. Nakazono, M. Oshima, O. Shiino, H. W. Yeom, A. Kakizaki, and Y. Aiura, *Phys. Rev. B* **66**, 073106 (2002).

[10] J. Feng, A. Tan, S. Wagner, J. Liu, Z. Mao, X. Ke, and P. Zhang, *Appl. Phys. Lett.* **109**, 021901 (2016).

[11] P. Chen, Y.-H. Chan, X.-Y. Yang, Y. Zhang, M. Y. Chou, S.-K. Mo, Z. Hussain, A.-V. Fedorov, and T.-C. Chiang, *Nat. Commun.* **6**, 8943 (2015).

[12] K. Sugawara, Y. Nakata, R. Shimizu, P. Han, T. Hitosugi, T. Sato, and T. Takahashi, *ACS Nano* **10**, 1341 (2016).

[13] K. E. Wagner, E. Morosan, Y. S. Hor, J. Tao, Y. Zhu, T. Sanders, T. M. McQueen, H. W. Zandbergen, A. J. Williams, D. V. West, and R. J. Cava, *Phys. Rev. B* **78**, 104520 (2008).

[14] L. J. Li, W. J. Lu, X. D. Zhu, L. S. Ling, Z. Qu, and Y. P. Sun, *Europhys. Lett.* **97**, 67005 (2012).

[15] Y. Liu, R. Ang, W. J. Lu, W. H. Song, L. J. Li, and Y. P. Sun, *Appl. Phys. Lett.* **102**, 192602 (2013).

[16] Y. Liu, D. F. Shao, W. J. Lu, L. J. Li, H. Y. Lv, X. D. Zhu, S. G. Tan, B. Yuan, L. Zu, X. C. Kan, W. H. Song, and Y. P. Sun, arXiv:1412.4449.

[17] Y. Liu, D. F. Shao, L. J. Li, W. J. Lu, X. D. Zhu, P. Tong, R. C. Xiao, L. S. Ling, C. Y. Xi, L. Pi, H. F. Tian, H. X. Yang, J. Q. Li, W. H. Song, X. B. Zhu, and Y. P. Sun, *Phys. Rev. B* **94**, 045131 (2016).

[18] L. J. Li, X. D. Zhu, Y. P. Sun, H. C. Lei, B. S. Wang, S. B. Zhang, X. B. Zhu, Z. R. Yang, and W. H. Song, *Phys. C (Amsterdam, Neth.)* **470**, 313 (2010).

[19] L. F. Mattheiss, *Phys. Rev. B* **8**, 3719 (1973).

[20] J.-A. Yan, M. A. Dela Cruz, B. Cook, and K. Varga, *Sci. Rep.* **5**, 16646 (2015).

[21] N. V. Smith, S. D. Kevan, and F. J. DiSalvo, *J. Phys. C* **18**, 3175 (1985).

[22] K. Rossnagel and N. V. Smith, *Phys. Rev. B* **73**, 073106 (2006).

[23] K. Rossnagel and N. V. Smith, *Phys. Rev. B* **76**, 073102 (2007).

[24] P. Darancet, A. J. Millis, and C. A. Marianetti, *Phys. Rev. B* **90**, 045134 (2014).

[25] P. Lazar, J. Martincová, and M. Otyepka, *Phys. Rev. B* **92**, 224104 (2015).

[26] S. Sharma, L. Nordström, and B. Johansson, *Phys. Rev. B* **66**, 195101 (2002).

[27] Q. Zhang, L.-Y. Gan, Y. Cheng, and U. Schwingenschlögl, *Phys. Rev. B* **90**, 081103(R) (2014).

[28] L.-Y. Gan, L.-H. Zhang, Q. Zhang, C.-S. Guo, U. Schwingen- schlögl, and Y. Zhao, *Phys. Chem. Chem. Phys.* **18**, 3080 (2016).

[29] A. Y. Liu, *Phys. Rev. B* **79**, 220515(R) (2009).

[30] Y. Ge and A. Y. Liu, *Phys. Rev. B* **82**, 155133 (2010).

[31] Y. Ge and A. Y. Liu, *Phys. Rev. B* **86**, 104101 (2012).

[32] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

[33] G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**, 15 (1996).

[34] G. Kresse and J. Hafner, *Phys. Rev. B* **49**, 14251 (1994).

[35] G. Kresse and J. Hafner, *Phys. Rev. B* **47**, 558 (1993).

[36] P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

[37] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[38] J. P. Perdew and A. Zunger, *Phys. Rev. B* **23**, 5048 (1981).

[39] J. P. Perdew, K. Burke, and Y. Wang, *Phys. Rev. B* **54**, 16533 (1996).

[40] H. Peng, Z.-H. Yang, J. P. Perdew, and J. Sun, *Phys. Rev. X* **6**, 041005 (2016).

[41] T. Björkman, A. Gulans, A. V. Krasheninnikov, and R. M. Nieminen, *J. Phys. Condens. Matter* **24**, 424218 (2012).

[42] G. Román-Pérez and J. M. Soler, *Phys. Rev. Lett.* **103**, 096102 (2009).

[43] M. Dion, H. Rydberg, E. Schröder, D. C. Langreth, and B. I. Lundqvist, *Phys. Rev. Lett.* **92**, 246401 (2004).

[44] J. Fink, V. Soltwisch, J. Geck, E. Schierle, E. Weschke, and B. Büchner, *Phys. Rev. B* **83**, 092503 (2011).

[45] T. Thonhauser, V. R. Cooper, S. Li, A. Puzder, P. Hyldgaard, and D. C. Langreth, *Phys. Rev. B* **76**, 125112 (2007).

[46] J. Klimeš, D. R. Bowler, and A. Michaelides, *J. Phys.: Condens. Matter* **22**, 022201 (2010).

[47] P. Haas, F. Tran, and P. Blaha, *Phys. Rev. B* **79**, 085104 (2009).

[48] Y. Ding, Y. Wang, J. Ni, L. Shi, S. Shi, and W. Tang, *Phys. B (Amsterdam, Neth.)* **406**, 2254 (2011).

[49] P. Manchanda, V. Sharma, H. Yu, D. J. Sellmyer, and R. Skomski, *Appl. Phys. Lett.* **107**, 032402 (2015).

[50] T. Ritschel, J. Trinckauf, K. Koepernik, B. Büchner, M. v. Zimmermann, H. Berger, Y. I. Joe, P. Abbamonte, and J. Geck, *Nat. Phys.* **11**, 328 (2015).