# Theory Study of AlCl Disproportionation Reaction Mechanism on Al (110) Surface

XIU-MIN CHEN, BIN YANG, DONG-PING TAO, and YONG-NIAN DAI

The surface disproportionation reaction mechanism of aluminum subchloride on aluminum (110) surfaces has been investigated using the plane-wave density functional theory (DFT). Three possible reaction mechanisms of AlCl disproportionation reaction on aluminum (110) surfaces have been taken into account; the reactants and products structures have been optimized, transition states have been confirmed, and activation energy has been calculated. The adsorption energy of reactants and the desorption energy of products also have been calculated. All of these calculations have been employed to confirm the reaction mechanism and the rate-determining step of AlCl disproportionation reaction on aluminum (110) surfaces.

DOI: 10.1007/s11663-009-9321-4
© The Minerals, Metals & Materials Society and ASM International 2009

## I. INTRODUCTION

DURING the past 50 years, numerous attempts have been made to produce aluminum using carbothermic reduction to take the place of the traditional Hall cell. The major driving force to develop carbothermic reduction is a decrease in energy consumption. The Pechiney and Reynolds processes reached a significant level of development, although Aloca technologies should be noted in particular. $^{[1]}$ Recently, Kunming University of Science and Technology with support from Joint Funds of the National Natural Science Foundation of China has been researching and developing the technology to produce aluminum by carbothermic reduction as well as by chlorination of alumina under vacuum condition, which consists of two stages. In stage 1, AlCl gas is formed by carbon reduction and $AlCl_{3}$ chlorination of alumina at about $1110{^\circ}C$ and 60 Pa. In stage 2, the Al metal is formed by a disproportionation reaction of AlCl gas at lower temperatures. It can be shown by the following reactions $^{[2,3]}$:

$$
\mathrm{AlCl}_{3}(\mathrm{g})+3 \mathrm{C}(\mathrm{s})+\mathrm{Al}_{2} \mathrm{O}_{3}(\mathrm{s}) \rightarrow 3 \mathrm{CO}(\mathrm{g})+3 \mathrm{AlCl}(\mathrm{g})
\tag{1}
$$

$$
3 \mathrm{AlCl}(\mathrm{g}) \rightarrow 2 \mathrm{Al}(\mathrm{s})+\mathrm{AlCl}_{3}(\mathrm{g})
\tag{2}
$$

This method is different from direct carbothermic reduction of alumina to produce aluminum. In any direct carbothermic reduction process for aluminum, species like $\mathrm{Al}_{4} \mathrm{C}_{3}$, $\mathrm{Al}_{4} \mathrm{O}_{4} \mathrm{C}$, $\mathrm{Al}_{2} \mathrm{O}_{3}$, and carbon—which usually cannot react completely—are associated with aluminum, and aluminum cannot be separated from the mixture. So, using direct carbothermic reduction of alumina to produce aluminum is too difficult to realize under regular conditions. Carbothermic reduction and chlorination of alumina have solved the problem of separating aluminum from the mixture by chlorinating aluminum into AlCl gas, which is easy to separate from the mixture in a vacuum. $^{[4]}$

Using AlCl disproportionation to produce Al at a lower temperature is a key step to producing aluminum through carbothermic reduction and chlorination of alumina under a vacuum condition, so it is important to study the reaction mechanism of AlCl disproportionation to control the disproportionation reaction process effectively.

A large amount of experimental and theory studies exist for low-valent aluminum compounds. The enthalpies of formation $^{[5]}$ and the electric quadrupole moment $^{[6]}$ for AlCl and AlF were calculated with quantum chemistry methods. The results of high-level quantum chemical calculations on the $[\mathrm{AlHF}]^{+}$ (protonation of gas-phase compounds AlF yields a complex of $\mathrm{Al}^{+}$ with a hydrogenated ligand $[\mathrm{AlHF}]^{+}$) potential energy surface indicate that aluminum, not the halogen atom, is the preferred protonation site in AlCl and AlBr. $^{[7]}$ Schnockel *et al.* have used this special method for molecules like AlCl and its disproportionation on the way to nanoscaled metal and have been carrying out a large amount of experimental and theory studies on low-valent aluminum compounds. These works indicate that (1) molecules like the low-valent Al and Ga compounds are disproportionate to nanoscaled metalloid Al clusters like $\mathrm{Al}_{12}$ ($\mathrm{AlBr}_{2}\cdot \mathrm{THF}$) (tetrahydrofuran, THF) as intermediates on the way to nanoscaled metal. $^{[8-14]}$ (2) Oligomers of AlCl have been studied using the matrix isolation technique and were analyzed by infrared (IR) and Raman spectra in combination with quantum chemical calculations. The structures of the trimer and tetramer have also been evaluated. $^{[15]}$ (3) An $[\mathrm{Al}]_{\mathrm{n}}$ cluster can dissolute in the $\mathrm{Cl}_{2}$, $\mathrm{O}_{2}$ gas phase or HCl and become low-valent

XIU-MIN CHEN, Associate Professor, and BIN YANG and YONG-NIAN DAI, Professors, are with the National Engineering Laboratory of Vacuum Metallurgy, Kunming University of Science and Technology, Kunming 650093, P.R. China. Contact e-mail: chenxiumin9@hotmail.com DONG-PING TAO, Professor, is with the Faculty of Materials and Metallurgy Engineering, Kunming University of Science and Technology, Kunming 650093, P.R. China.

Manuscript submitted July 30, 2009.
Article published online November 24, 2009.

METALLURGICAL AND MATERIALS TRANSACTIONS B
VOLUME 41B, FEBRUARY 2010—137

aluminum compounds. $^{[16-18]}$ We have used the density functional theory (DFT) study on the geometry structure, energy, and transition state of the $[AlCl]_n$ (n = 1~10) clusters. The results indicate that AlCl tends to form $[AlCl]_n$ clusters during the process of AlCl disproportionation to produce Al metal at a lower temperature. The AlCl adsorb on the surface of $[AlCl]_n$ cluster would disproportionate into $AlCl_3$ gas and nanoscaled Al metal, and the nanoscaled Al metal is the crystal core of metal aluminum.

According to the experiment and the theory study mentioned as well as the thermodynamic calculation results, three reaction mechanisms would take place for reaction (2), which are shown in Table I.

In this article, the research was mainly on the three possible surface disproportionation reaction mechanisms of AlCl disproportionation on aluminum (110) surfaces. To confirm the disproportionation reaction mechanism of AlCl disproportionation reaction and the rate-determining step of $3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)$. But chemical kinetic experiments are expensive and difficult in general to perform for this reaction. In addition, reaction intermediates typically have short lifetimes and low concentrations, which make them difficult to detect by standard analytical methods. The extrapolations of reaction data under ideal conditions, such as ultra-high vacuum (UHV) surface-science experiments, to actual deposition conditions may raise more difficulties. The lack of experimental data makes it desirable to predict reactions from the first principle quantum chemistry computations. Applications of quantum chemistry have risen rapidly with the growth in terms of computational speed and lower cost of computing. These techniques have been effective in studying chemical reactivity and molecular properties of compounds that contain first and second row elements. $^{[19]}$

For the reasons mentioned, the quantum chemistry method has been used in this article. The reactants and product structures have been optimized, transition states have been confirmed, and activation energies have been calculated. The adsorption energy of reactants and desorption energy of products also have been calculated. These calculations have been employed to contribute to mechanism and to find the rate-determining step of AlCl disproportionation reaction on aluminum (110) surfaces. The results contribute to research on aluminum production by carbothermic reduction and by chlorination of alumina under vacuum.

## II. COMPUTATIONAL DETAILS

All calculations were performed with the CASTEP program (Accelrys, San Diego, CA), which provides an efficient implementation of DFT plane-wave pseudopotential method $^{[20,21]}$ to explore surface chemical reactivity and crystal properties. GGA-PBE (generalized gradient approximation, GGA; Perdew-Burke-Ernzerhof, PBE) functionals proposed by Perdew, Burke, and Ernzerh $^{[22-25]}$ were used for the exchange-correlation functionals. GGA provided a better overall description of the electronic subsystem than the LDA functionals. And PBE was recommended for studies of molecules that interact with metal surfaces. Ultrasoft pseudopotentials were used to describe the electro-ion interactions and the convergence of the plane-wave expansion with a cutoff of 270 eV. To eliminate artificial interactions between the slabs, the vacuum slab set was $10.0\ \text{Å}$. $7 \times 7 \times 2$ k-points set were used to define the Brillouin zone sampling accuracy. The geometry optimizations for the minima and other stationary points of the potential energy surface include the molecules adsorbed on the surface and the metal slab.

The Al(110) surface was modeled by the slab supercell methods, which more correctly describe the surface physics rather than the cluster methods. $^{[19]}$ Six-layer slabs and p$(6 \times 3)$ unit cell have been used for more reasonable results. A p$(6 \times 3)$ unit cell is large enough to avoid lateral interaction between the adsorbates in adjacent unit cells. The Al(110) supercell has been used for the calculations, as shown in Figure 1.

To determine the chemisorption energies $E_{\text{ads}}$ and desorption energies $E_{\text{des}}$, the Al(110) surface was geometrically optimized with and without the adsorbate. The energies of the optimized surfaces were calculated subsequently for geometry optimization. The geometry of the adsorbate was optimized within a supercell identical to the cell of the surface, and the energies of

![](./images/811820149316255745_1.jpg)

Fig. 1—The Al(110) supercell used in the calculation.

<table><caption>Table I. Three Possible Reaction Mechanisms of AlCl Disproportionation on Aluminum (110) Surfaces</caption>
<thead>
  <tr>
    <th>Steps</th>
    <th>Mechanism A</th>
    <th>Mechanism B</th>
    <th>Mechanism C</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>$3AlCl(g) \Rightarrow 3AlCl(*)$</td>
    <td>$3AlCl(g) \Rightarrow 3AlCl(*)$</td>
    <td>$4AlCl(g) \Rightarrow 4AlCl(*)$</td>
  </tr>
  <tr>
    <td>2</td>
    <td>$2AlCl(*) \Rightarrow 2Al(*) + 2Cl( *)$</td>
    <td>$2AlCl(*) \Rightarrow AlCl_2(*) + Al(*)$</td>
    <td>$4AlCl(*) \Rightarrow 2AlCl_2(*) + 2Al(*)$</td>
  </tr>
  <tr>
    <td>3</td>
    <td>$AlCl(*) + Cl(*) \Rightarrow AlCl_2(*)$</td>
    <td>$AlCl_2(*) + AlCl(*) \Rightarrow AlCl_3(*) + Al(*)$</td>
    <td>$2AlCl_2(*) \Rightarrow AlCl(*) + AlCl_3(*)$</td>
  </tr>
  <tr>
    <td>4</td>
    <td>$AlCl_2(*) + Cl(*) \Rightarrow AlCl_3(*)$</td>
    <td>$AlCl_3(*) \Rightarrow AlCl_3(g)$</td>
    <td>$AlCl_3(*) \Rightarrow AlCl_3(g)$</td>
  </tr>
  <tr>
    <td>5</td>
    <td>$AlCl_3(*) \Rightarrow AlCl_3(g)$</td>
    <td></td>
    <td>$AlCl(*) \Rightarrow AlCl(g)$</td>
  </tr>
  <tr>
    <td>General reaction</td>
    <td>$3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)$</td>
    <td>$3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)$</td>
    <td>$3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)$</td>
  </tr>
  <tr>
    <td colspan="4">*Indicates the substance was in adsorption state.</td>
  </tr>
</tbody>
</table>

138—VOLUME 41B, FEBRUARY 2010

METALLURGICAL AND MATERIALS TRANSACTIONS B

this optimized adsorbate were calculated subsequently. Finally, the $E_{\text{ads}}$ and $E_{\text{des}}$ were calculated according to the following:

$$
E_{\text{ads}} = E_{\text{surface+adsorber}} - E_{\text{surface}} - E_{\text{adsorber}} \tag{3}
$$

$$
E_{\text{des}} = E_{\text{surface}} + E_{\text{adsorber}} - E_{\text{surface+adsorber}} \tag{4}
$$

The transition state of the surface reaction was located on the potential energy hypersurface (PES) by complete linear synchronous transit/quadratic synchro- nous transit (LST/QST). Complete LST/QST begins by performing an LST optimization calculation. The tran- sition states (TS) approximation obtained then was used to perform a QST maximization. From that point, another conjugate gradient minimization was per- formed. The cycle was repeated until a stationary point was located or the number of allowed QST steps was exhausted. $^{[26]}$

To determine the reaction energies $(E_{\text{reaction}})$ and the activation barrier $(E_{\text{a}}$ and $E_{\text{a}}^{-1})$ of a surface reaction, the total energies of the reactants as well as the transition state and the products were calculated. The energies were calculated according to the following:

$$
E_{\text{reaction}} = E_{\text{products}} - E_{\text{reactants}} \tag{5}
$$

$$
E_{\text{a}} = E_{\text{transition state}} - E_{\text{reactants}} \tag{6}
$$

$$
E_{\text{a}}^{-1} = E_{\text{products}} - E_{\text{transition state}} \tag{7}
$$

## III. RESULTS AND DISCUSSION

### A. Chemisorption Structures of Reactants

Various chemisorption sites are available for the adsor- bate on Al(110)surfaces, and only the most stable chemi- sorption sites for the adsorbate are given in this article. The atoms labeled in Figure 1, will be discussed in detail.

#### 1. Chemisorption Structures of Reactants on Al(110) Surface in Mechanism A

The reactions that contribute to mechanism A and the reactants involve AlCl, AlCl with Cl, $\text{AlCl}_2$ with Cl, which adsorb on Al(110) surfaces. The most stable chemisorption sites and chemisorption structures of AlCl, AlCl with Cl, $\text{AlCl}_2$ with Cl, on Al(110)surfaces are shown in Figure 2.

The AlCl structure adsorbed to the Al(110)surfaces is shown in Figure 2(a). The fourfold hollow site was the most stable for AlCl adsorbed to the Al(110)surface. To compare $2.130$ Å of AlCl in gas phase with the optimized bond length, the Al(2)-Cl(1) bond in adsorption state was shortened to $2.113$ Å, whereas the bond length of Al(2)- Al(3) was $2.49$ Å, and the bond length of Al(2)-Al(5) was $2.48$ Å. The angle of Cl(1)-Al(2)-Al(3) was 126 deg, and the angle of Cl(1)-Al(2)-Al(5) was 122 deg.

The structure of AlCl and Cl simultaneously adsorbed on Al(110) surfaces is shown in Figure 2(b). The Cl(1) was stable in top-site adsorption, and the distance to the Al atom was $2.15$ Å. The four-fold hollow site was the most stable for AlCl, and the Al(2)-Cl(3) bond was shortened to $2.09$ Å, the bond length of Al(2)-Al(4) was $2.50$ Å, the bond length of Al(2)-Al(5) was $2.48$ Å, the bond length of Al(2)-Al(6) was $3.08$ Å, and the bond length of Al(2)-Al(7) was $2.77$ Å.

The structure of $\text{AlCl}_2$ and Cl, simultaneously adsorbed on Al(110)surfaces are shown in Figure 2(c). The Cl(1) was stable in top-site adsorption, and the distance to the Al atom was $2.15$ Å. The three-fold hollow site was the most stable for $\text{AlCl}_2$ adsorbed on the Al(110)surface. The Al(2)-Cl(3) and the Al(2)-Cl(4) bond were $2.13$ Å. With the optimized bond length $2.13$ Å of AlCl in gas phase, the bond length of Al(2)- Al(5) was $2.63$ Å, the bond length of Al(2)-Al(6) was $3.17$ Å, and the bond length of Al(2)-Al(7) was $2.61$ Å.

#### 2. Chemisorption Structures of Reactants on Al(110) Surface in Mechanisms B and C

In accordance with the reactions that contribute to mechanisms B and C, the reactants involve AlCl with AlCl, AlCl with $\text{AlCl}_2$, and $\text{AlCl}_2$ with $\text{AlCl}_2$, which adsorb on Al(110) surfaces.

The optimized structure of AlCl and AlCl simulta- neously adsorbed on Al(110) surfaces are shown in Figure 3(a). The four-fold hollow site was the most stable for the AlCl Al atom labeled 1. The Al(1)-Cl(3) bond was shortened to $2.10$ Å, the bond length of Al(1)- Al(6) was $2.46$ Å, and the bond length of Al(1)-Al(7) was $2.47$ Å. The angle of Cl(3)-Al(1)-Al(6) was 128 deg, and the angle of Cl(3)-Al(1)-Al(5) was 123 deg. For the AlCl Al atom labeled 2, the five-fold hollow site was the most stable. The Al(2)-Cl(4) bond was shortened to $2.13$ Å, the bond length of Al(2)-Al(7) was $2.71$ Å, the bond length of Al(2)-Al(8) was $2.74$ Å, the bond length

![](./images/811820149316255745_2.jpg)

Fig. 2—Chemisorption structures of AlCl, AlCl with Cl, and $\text{AlCl}_2$ with Cl on Al(110) surfaces.

![](./images/811820149316255745_3.jpg)

Fig. 3—Simultaneous adsorption structures of AlCl with AlCl, AlCl with AlCl₂, and AlCl₂ with AlCl₂ on Al(110) surfaces.

![](./images/811820149316255745_4.jpg)

Fig. 4—Adsorption structures of Al with Cl, AlCl₂, and AlCl₃ on Al(110) surfaces.

of Al(2)–Al(9) was 2.80 Å, and the bond length of Al(2)–Al(10) was 2.71 Å.

The structure of AlCl and AlCl₂ simultaneously adsorbed on Al(110) surfaces are shown in Figure 3(b). The four-fold hollow site was the most stable for the AlCl₂ Al atom labeled 1. The Al(1)–Cl(3) bond was 2.13 Å, the bond length of Al(1)–Al(4) was 2.24 Å, the bond length of Al(1)–Al(6) was 2.55 Å, and the bond length of Al(1)–Al(7) was 2.54 Å. The angle of Cl(3)–Al(1)–Al(4) was 103 deg. For the AlCl Al atom labeled 2, the five-fold hollow site was the most stable. The Al(2)–Cl(5) bond was 2.13 Å, the bond length of Al(2)–Al(8) was 2.78 Å, the bond length of Al(2)–Al(9) was 2.73 Å, the bond length of Al(2)–Al(10) was 2.74 Å, and the bond length of Al(2)–Al (11) was 2.71 Å.

The structure of AlCl₂ and AlCl₂ simultaneously adsorbed on Al(110) surfaces is shown in Figure 3(c). The four-fold hollow site was the most stable for the AlCl₂ Al atom labeled 1. The Al(1)–Cl(3) bond was shortened to 2.12 Å, the bond length of Al(1)–Al(4) was 2.23 Å, the bond length of Al(1)–Al(7) was 2.55 Å, and the bond length of Al(1)–Al(8) was 2.57 Å. The angle of Cl(3)–Al(1)–Al(4) was 103 deg. For the AlCl₂ Al atom labeled 2, the five-fold hollow site was the most stable. The Al(2)–Cl(5) bond was stretched to 2.24 Å, the bond length of Al(2)–Cl(6) was stretched to 2.16 Å, the bond length of Al(2)–Al(9) was 2.74 Å, Al(2)–Al(10) was 2.83 Å, the bond length of Al(2)–Al (11) was 2.93 Å, and the bond length of Al(2)–Al(12) was 2.85 Å.

### B. Chemisorption Structures of Products
#### 1. Chemisorption Structures of Products on Al(110) Surface in Mechanism A
In light of the reactions that contribute to mechanism A, the products involve Al with Cl, AlCl₂, and AlCl₃, which adsorb on Al(110) surfaces.

The AlCl adsorbed on Al(110) surface and also dissociate into Cl and Al atoms in adsorption state. The structures are shown in Figure 4(a). The top site was the most stable for the Cl atom labeled 1, the Al–Cl(1) bond was stretched to 2.16 Å. The four-fold hollow site was the most stable for the Al atom labeled 2, the bond length of Al(2)–Al(3) was 2.49 Å, the bond length of Al(2)–Al(4) was 2.49 Å, the bond length of Al(2)–Al(5) was 2.98 Å, and the bond length of Al(2)–Al(6) was 2.87 Å.

The structure of AlCl₂ in adsorption state was optimized and is shown in Figure 4(b). The four-fold hollow site was the most stable for AlCl₂, the bond length of Al(1)–Cl(2) was stretched to 2.17 Å, Al(1)–Cl(3) bond was 2.11 Å. The bond length of Al(1)–Al (4) was 2.62 Å, the bond length of Al(1)–Al(5) was 2.86 Å. The angle of Cl(2)–Al(1)–Cl(3) was 100.6 deg.

The optimized structure of AlCl₃ is shown in Figure 4(c). The bridge site was the most stable for AlCl₃, the Al(1)–Cl(2) bond was stretched to 2.14 Å, the Al(1)–Cl(3) bond was 2.11 Å, the Al(1)–Cl(4) bond was stretched to 2.18 Å. The bond length of Al(1)–Al(5) was 3.15 Å, the bond length of Al(1)–Al(6) was 2.60 Å. The angle of Cl(2)–Al(1)–Cl(4) was 101 deg, the angle of Cl(2)–Al(1)–Cl(3) was 114 deg, the angle of Cl(3)–Al(1)–Cl(4) was 111 deg.

### 2. Chemisorption Structures of Products on Al(110) Surface in Mechanism B and C
On the basis of the reactions that contribute to mechanisms B and C, the products involve AlCl₂ with Al, AlCl₃ with Al, and AlCl₃ with AlCl, which adsorb on Al(110) surfaces.

The simultaneous adsorption structure of AlCl₂ and Al are shown in Figure 5(a). The four-fold hollow site was the most stable for AlCl₂, the Al(1)–Cl(3) bond was 2.13 Å, Al(1)–Cl(4) bond was stretched to 2.25 Å. The
---
140—VOLUME 41B, FEBRUARY 2010
METALLURGICAL AND MATERIALS TRANSACTIONS B

![](./images/811820149316255745_5.jpg)

Fig. 5—Simultaneous adsorption structures of AlCl₂ with Al, AlCl₃ with Al, and AlCl₃ with AlCl on Al(110) surfaces.

bond length of Al(1)–Al(5) was 2.52 Å, the bond length of Al(1)–Al(6) was 2.59 Å, the bond length of Al(1)–Al(7) was 2.88 Å, the bond length of Al(1)–Al(8) was 2.72 Å. The four-fold hollow site was the most stable for the Al labeled 2. The bond length of Al(2)–Al(9) was 2.68 Å, the bond length of Al(2)–Al(10) was 2.76 Å, the bond length of Al(2)–Al(11) was 2.71 Å, and the bond length of Al(2)–Al(12) was 2.75 Å.

The simultaneous adsorption structure of AlCl₃ and Al was optimized and is shown in Figure 5(b). The three-fold hollow site was the most stable for the AlCl₃ Al atom labeled 1. The Al(1)–Cl(3) bond was stretched to 2.14 Å, Al(1)–Cl(4) bond was shortened to 2.09 Å, and the Al(1)–Cl(5) bond was stretched to 2.26 Å. The bond length of Al(1)–Al(6) was 3.05 Å, the bond length of Al(1)–Al(7) was 2.61 Å, the bond length of Al(1)–Al(8) was 2.98 Å. The four-fold hollow site was the most stable for the Al labeled 2. The bond length of Al(2)–Al(9) was 2.73 Å, the bond length of Al(2)–Al(10) was 2.72 Å, the bond length of Al(2)–Al(11) was 2.75 Å, Al(2)–Al(12) was 2.70 Å.

The simultaneous adsorption structure of AlCl₃ and AlCl was optimized and is shown in Figure 5(c). The top site was the most stable for AlCl₃. The Al(1)–Cl(3) bond was stretched to 2.15 Å, the Al(1)–Cl(4) bond was shortened to 2.11 Å, and the Al(1)–Cl(5) bond was stretched to 2.29 Å. The bond length of Al(1)–Al(7) was 2.55 Å, the bond length of Cl(5)–Al(12) was 2.33 Å. The four-fold hollow site was the most stable for the AlCl Al atom labeled 2. The Al(2)–Cl(6) bond length was 2.13 Å, the bond length of Al(2)–Al(8) was 2.72 Å, the bond length of Al(2)–Al(9) was 2.82 Å, the bond length of Al(2)–Al(10) was 2.85 Å, and the bond length of Al(2)–Al(11) was 2.71 Å.

### C. Reaction Pathway and Transition States

Based on the optimized structures of the reactants as well as the products of the reactions in mechanisms A, B, and C, the reaction energies ($E_{\text{reaction}}$) and the activation barrier ($E_{\text{a}}$ and $E_{\text{a}}^{-1}$) of a surface reaction were calculated. The transition state of the surface reaction was located by complete LST/QST.

#### 1. Reaction Pathway and Transition States of Reactions in Mechanism A

The dissociation pathway of $\text{AlCl}(*) \Rightarrow \text{Al}(*) + \text{Cl}(*)$ is shown in Figure 6, The AlCl that adsorbed with a four-fold hollow site on Al(110) surface went through transition state TS1, dissociated into Al and Cl atoms, and finished with the Cl atom in the top-site adsorption. The effective activation energy was 2.05849 eV, and the reaction was calculated to be endothermic with a reaction energy of 0.34551 eV. The optimized geometries of the corresponding transition state are shown in Figure 6. In the TS1 transition state geometry, the distance between Cl(2) and Al(1) was 3.47 Å, and the distance between Cl(2) and the Al atom on which the Cl(2) will adsorb when the dissociation completed was 3.47 Å.

![](./images/811820149316255745_6.jpg)

Fig. 6—Dissociation pathway of AlCl on an Al (110) surface.

The reaction pathway of $\text{AlCl}(*) + \text{Cl}(*) \Rightarrow \text{AlCl}_{2}(*)$ is shown in Figure 7, The AlCl (which adsorbed with a four-fold hollow site) reacted with the Cl atom (which adsorbed with the top site on the Al(110) surface), went through a transition state TS2, and the $Cl$ bonded with

![](./images/811820149316255745_7.jpg)

Fig. 7—Reaction pathway of AlCl and Cl on an Al(110) surface.

METALLURGICAL AND MATERIALS TRANSACTIONS B
VOLUME 41B, FEBRUARY 2010—141

![](./images/811820149316255745_8.jpg)

Fig. 8—Reaction pathway of $\text{AlCl}_2$ and Cl on an Al(110) surface.

the Al atom of AlCl, and finished with the $\text{AlCl}_2$ in the bridge-site adsorption. The effective activation energy was 1.49 eV, and the reaction was calculated to be endothermic with a reaction energy of 0.54147 eV. The optimized geometries of the corresponding transition state are shown in Figure 7. In the TS2 transition state geometry, the distance between Cl(3) and Al(1) was 3.42 Å, and the distance between Cl(3) to the Al atom on which Cl(3) adsorbed before the reaction began was 3.42 Å.

The reaction pathway of $\text{AlCl}_2(*) + \text{Cl}(*) \Rightarrow \text{AlCl}_3(*)$ is shown in Figure 8. The AlCl (which adsorbed with bridge site) reacted with the Cl atom (which adsorbed with top site on Al(110) surface) went through a transition state TS3, the Cl atom bonded with the Al atom of $\text{AlCl}_2$, and finished with the $\text{AlCl}_3$ in the bridge-site adsorption. The effective activation energy was 1.58 eV, and the reaction was calculated to be endothermic with a reaction energy of 0.21274 eV. The optimized geometries of the corresponding transition state are shown in Figure 8. In the TS3 transition state geometry, the distance between Cl(4) and Al(1) was 3.46 Å, and the distance between Cl(4) and the Al atom on which the Cl atom adsorbed before the reaction began was 3.43 Å.

### 2. Reaction Pathway and Transition States of Reactions in Mechanism B
The reaction pathway of $2\text{AlCl}(*) \Rightarrow \text{AlCl}_2(*) + \text{Al}(*)$ is shown in Figure 9. The AlCl (which was the Al atom labeled 2) adsorbed with the four-fold hollow site, went through a transition state TS4, and dissociated into Al and Cl atoms. The Cl atom bonded with Al(1) and finished with the $\text{AlCl}_2$ (Al(2) still in adsorption state). The effective activation energy was 2.02521 eV. The reaction was calculated to be endothermic with a reaction energy of 0.49001 eV. The optimized geometries of the corresponding transition state are shown in Figure 9. In the TS4 transition state geometry, the distance between Cl(4) and Al(2) was 3.77 Å, and the distance between Cl(4) and the Al (1) was 4.23 Å.

![](./images/811820149316255745_9.jpg)

Fig. 9—Reaction pathway of AlCl and AlCl on an Al(110) surface.

The reaction pathway of $\text{AlCl}_2(*) + \text{AlCl}(*) \Rightarrow \text{AlCl}_3(*) + \text{Al}(*)$ on Al(110) surface is shown in Figure 10. The AlCl (which the Al atom labeled 2) adsorbed with the four-fold hollow site, went through a transition state TS5, and dissociated into Al and Cl atoms. The Cl atom bonded with $\text{AlCl}_2$ (which the Al atom labeled 1) and finished with the $\text{AlCl}_3$ in the adsorption state. The effective activation energy was 2.69116 eV, and the reaction was calculated to be exothermic with a reaction energy of –0.24721 eV. The optimized geometries of the corresponding transition state are shown in Figure 10. In the TS5 transition state geometry, the distance between Cl(5) and Al(2) was 4.58 Å, and the distance between Cl(5) and Al (1) was 4.39 Å.

![](./images/811820149316255745_10.jpg)

Fig. 10—Reaction pathway of AlCl and $\text{AlCl}_2$ on an Al(110) surface.

### 3. Reaction Pathway and Transition States of Reaction in Mechanism C
The reaction pathway of $\text{AlCl}^* + \text{AlCl}^* \rightarrow \text{AlCl}_2 * + \text{Al}^*$ in mechanism C was the same as that of mechanism B shown in Figure 9, so the pathway of this reaction was not listed again.

The reaction pathway of $2\text{AlCl}_2(*) \Rightarrow \text{AlCl}(*) + \text{AlCl}_3(*)$ on the Al(110) surface is shown in Figure 11, The $\text{AlCl}_2$ (which was labeled 2) adsorbed with the four-fold hollow site, went through a transition state TS6, and dissociated Cl atoms. The Cl atom bonded with the Al atom of $\text{AlCl}_2$ (labeled 1) and resulted in $\text{AlCl}_3$, with AlCl in the adsorption state. The effective activation energy was 1.43063 eV, and the reaction was calculated to be exothermic with a reaction energy of –0.82655 eV.

---

142—VOLUME 41B, FEBRUARY 2010

METALLURGICAL AND MATERIALS TRANSACTIONS B

The optimized geometries of the corresponding transition state are shown in Figure 11. In the TS6 transition state geometry, the distance between Cl(5) and Al(2) was 3.53 Å, and the distance between Cl(5) and Al (1) was 4.29 Å.

According to the calculation results, the energy of the reactants, products and transition states, as well as the reaction energies ($\mathrm{E_{reaction}}$) and the activation barrier ($\mathrm{E_a^1}$ and $\mathrm{E_a^{-1}}$) of the reactions that contributed to mechanisms A, B, and C have been calculated and are listed in Table II.

### 4. Reaction Energies of Mechanisms A, B, and C
To calculate the general reaction energies of mechanisms A, B, and C, the adsorption energy of AlCl and the desorption energies of AlCl and $\mathrm{AlCl_3}$ were calculated. The energies of the substances used to calculate the adsorption and desorption energies of AlCl and $\mathrm{AlCl_3}$ are listed in Table III.

Based on the energy values in Table III, the adsorption energy of AlCl was calculated to be –9.355 eV, the desorption energy of AlCl was 9.355 eV, and the desorption energy of $\mathrm{AlCl_3}$ was 8.054 eV. The values of the adsorption energy of AlCl and desorption energy of $\mathrm{AlCl_3}$ indicated that the sorption of AlCl and $\mathrm{AlCl_3}$ on Al(110) surface were in chemisorption.

![](./images/811820149316255745_11.jpg)

Fig. 11—Reaction pathway of $\mathrm{AlCl_2}$ and $\mathrm{AlCl_2}$ on an Al(110) surface.

<table>
<thead>
<tr>
<th colspan="10">Table II. The Energy of the Reactants, Products, and Transition States, $\mathrm{E_{reaction}}$, $\mathrm{E_a^1}$, and $\mathrm{E_a^{-1}}$ of the Reactions in Mechanisms A, B, and C</th>
</tr>
<tr>
<th>Steps</th>
<th>Reactions on Al(110) Surface</th>
<th>Energy of Reactants (eV)</th>
<th>Energy of Products (eV)</th>
<th>Energy of Transition States (eV)</th>
<th>$\mathrm{E_a}$ (eV)</th>
<th>$\mathrm{E_a^{-1}}$ (eV)</th>
<th>Reaction Energy</th>
</tr>
</thead>
<tbody>
<tr>
<td>A2</td>
<td>$\mathrm{AlCl(*) \Rightarrow Al(*) + Cl(*)}$</td>
<td>–6624.081</td>
<td>–6623.736</td>
<td>–6622.023</td>
<td>2.059</td>
<td>1.713</td>
<td>0.346</td>
</tr>
<tr>
<td>A3</td>
<td>$\mathrm{AlCl(*) + Cl(*) \Rightarrow AlCl_2(*)}$</td>
<td>–7035.637</td>
<td>–7035.096</td>
<td>–7034.150</td>
<td>1.487</td>
<td>0.945</td>
<td>0.541</td>
</tr>
<tr>
<td>A4</td>
<td>$\mathrm{AlCl_2(*) + Cl(*) \Rightarrow AlCl_3(*)}$</td>
<td>–7446.873</td>
<td>–7446.659</td>
<td>–7445.294</td>
<td>1.578</td>
<td>1.365</td>
<td>0.213</td>
</tr>
<tr>
<td>B2C2</td>
<td>$\mathrm{2AlCl(*) \Rightarrow AlCl_2(*) + Al(*)}$</td>
<td>–7092.658</td>
<td>–7092.168</td>
<td>–7090.632</td>
<td>2.025</td>
<td>1.535</td>
<td>0.490</td>
</tr>
<tr>
<td>B3</td>
<td>$\mathrm{AlCl_2(*) + AlCl(*) \Rightarrow AlCl_3(*) + Al(*)}$</td>
<td>–7503.695</td>
<td>–7503.942</td>
<td>–7501.004</td>
<td>2.691</td>
<td>2.938</td>
<td>–0.247</td>
</tr>
<tr>
<td>C3</td>
<td>$\mathrm{2AlCl_2(*) \Rightarrow AlCl(*) + AlCl_3(*)}$</td>
<td>–7914.991</td>
<td>–7915.818</td>
<td>–7913.561</td>
<td>1.431</td>
<td>2.257</td>
<td>–0.827</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="6">Table III. The Energies Used to Calculate the Adsorption and Desorption Energy of AlCl and $\mathrm{AlCl_3}$</th>
</tr>
<tr>
<th>Substance</th>
<th>AlCl</th>
<th>$\mathrm{AlCl_3}$</th>
<th>Al(110) Supercell</th>
<th>$\mathrm{AlCl_3 + Al(110)}$ Supercell</th>
<th>$\mathrm{AlCl + Al(110)}$ Supercell</th>
</tr>
</thead>
<tbody>
<tr>
<td>Energy (eV)</td>
<td>–466.922</td>
<td>–1291.013</td>
<td>–6148.487</td>
<td>–7447.554</td>
<td>–6624.764</td>
</tr>
</tbody>
</table>

The energies of the general reaction $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ of mechanisms A, B, and C were calculated based on the reaction energies that took place in mechanisms A, B, and C. The adsorption energy of AlCl, the desorption energy of $\mathrm{AlCl_3}$ and AlCl, and the surface reaction energies of the reactions without desorption and adsorption energies also were calculated. All these energies are shown in Table IV.

The resulting energies are shown in Table IV, which indicated (1) that the desorption and adsorption energies of AlCl and $\mathrm{AlCl_3}$ are much higher than the surface reaction energies of the reactions in mechanisms A, B, and C of $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ on Al(110) surface, which means that the adsorption of reactants and the desorption of products affect much more than the disproportionation reaction of AlCl on aluminum (110) surfaces. (2) All general reaction energy values of mechanisms A, B, and C were negative, which means that $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ that reacted on the surface of Al(110) was exothermic. In other words, when the temperature rises, $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ will reverse, whereas when the temperature drops, $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ will proceed as written. The result agrees with the experiment phenomenon that AlCl is stable in high temperature and reduces into Al and $\mathrm{AlCl_3}$ in low temperature. (3) The order of the general reaction energy values of mechanisms A, B, and C is $\mathrm{A(-18.58eV) > B(-19.78eV) > C(-19.86eV)}$, which means that when $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ reacted on aluminum (110) surfaces, it was easy to proceed following the order $C > B > A$. To confirm this result, the order of the surface reaction energies of mechanisms A, B, and C also are listed as $\mathrm{A(1.45eV) > B(0.24eV) > C(0.15eV)}$. It is easy to see the results agreed with the general reaction energies values. It can be concluded that when $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ proceeded normally, the reaction mainly followed mechanism C, then followed mechanism B, and finally followed mechanism A. When $\mathrm{3AlCl(g) \Rightarrow 2Al(*) + AlCl_3(g)}$ proceeded in reverse, the reaction mainly followed mechanism A, then followed mechanism B, and finally followed mechanism C. Finally,

METALLURGICAL AND MATERIALS TRANSACTIONS B

VOLUME 41B, FEBRUARY 2010—143

<table><caption>Table IV. General Reaction Energies and Surface Energies of Mechanism A, B and C of $3\text{AlCl(g)} \Rightarrow 2\text{Al( * )} + \text{AlCl}_3\text{(g)}$ on Al(110) Surface</caption>
<thead>
<tr>
<th>Reaction<br>Mechanism</th>
<th>Steps</th>
<th>Reactions</th>
<th>Energies<br>(eV)</th>
<th>Surface Reaction<br>Energies (Without<br>Desorption and Adsorption<br>Energies) (eV)</th>
<th>General Reaction and<br>Reaction Energies (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>A 1</td>
<td>$3\text{AlCl(g)} \Rightarrow 3\text{AlCl(* )}$ (adsorption)</td>
<td>−28.07</td>
<td rowspan="5">1.45</td>
<td rowspan="5">$3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$<br>−18.58</td>
</tr>
<tr>
<td></td>
<td>A 2</td>
<td>$2\text{AlCl(* )} \Rightarrow 2\text{Al(* )} + 2\text{Cl(* )}$</td>
<td>0.69</td>
</tr>
<tr>
<td></td>
<td>A 3</td>
<td>$\text{AlCl(* )} + \text{Cl(* )} \Rightarrow \text{AlCl}_2\text{(* )}$</td>
<td>0.54</td>
</tr>
<tr>
<td></td>
<td>A 4</td>
<td>$\text{AlCl}_2\text{(* )} + \text{Cl(* )} \Rightarrow \text{AlCl}_3\text{(* )}$</td>
<td>0.21</td>
</tr>
<tr>
<td></td>
<td>A 5</td>
<td>$\text{AlCl}_3\text{(* )} \Rightarrow \text{AlCl}_3\text{(g)}$ (desorption)</td>
<td>8.05</td>
</tr>
<tr>
<td>B</td>
<td>B 1</td>
<td>$3\text{AlCl(g)} \Rightarrow 3\text{AlCl(* )}$ (adsorption)</td>
<td>−28.07</td>
<td rowspan="4">0.24</td>
<td rowspan="4">$3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$<br>−19.78</td>
</tr>
<tr>
<td></td>
<td>B 2</td>
<td>$2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$</td>
<td>0.49</td>
</tr>
<tr>
<td></td>
<td>B 3</td>
<td>$\text{AlCl}_2\text{(* )} + \text{AlCl(* )} \Rightarrow \text{AlCl}_3\text{(* )} + \text{Al(* )}$</td>
<td>−0.25</td>
</tr>
<tr>
<td></td>
<td>B 4</td>
<td>$\text{AlCl}_3\text{(* )} \Rightarrow \text{AlCl}_3\text{(g)}$ (desorption)</td>
<td>8.05</td>
</tr>
<tr>
<td>C</td>
<td>C 1</td>
<td>$4\text{AlCl(g)} \Rightarrow 4\text{AlCl(* )}$ (adsorption)</td>
<td>−37.42</td>
<td rowspan="5">0.15</td>
<td rowspan="5">$3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$<br>−19.86</td>
</tr>
<tr>
<td></td>
<td>C 2</td>
<td>$4\text{AlCl(* )} \Rightarrow 2\text{AlCl}_2\text{(* )} + 2\text{Al(* )}$</td>
<td>0.98</td>
</tr>
<tr>
<td></td>
<td>C 3</td>
<td>$2\text{AlCl}_2\text{(* )} \Rightarrow \text{AlCl(* )} + \text{AlCl}_3\text{(* )}$</td>
<td>−0.83</td>
</tr>
<tr>
<td></td>
<td>C 4</td>
<td>$\text{AlCl}_3\text{(* )} \Rightarrow \text{AlCl}_3\text{(g)}$ (desorption)</td>
<td>8.05</td>
</tr>
<tr>
<td></td>
<td>C 5</td>
<td>$\text{AlCl(* )} \Rightarrow \text{AlCl(g)}$ (desorption)</td>
<td>9.36</td>
</tr>
</tbody>
</table>

mechanism C, the reaction energies of $4\text{AlCl(* )} \Rightarrow 2\text{AlCl}_2\text{(* )} + 2\text{Al(* )}$ was 0.98 eV and for $2\text{AlCl}_2\text{(* )} \Rightarrow \text{AlCl(* )} + \text{AlCl}_3\text{(* )}$ was −0.83 eV. The results indicate that $4\text{AlCl(* )} \Rightarrow 2\text{AlCl}_2\text{(* )} + 2\text{Al(* )}$ was more difficult than $2\text{AlCl}_2\text{(* )} \Rightarrow \text{AlCl(* )} + \text{AlCl}_3\text{(* )}$ to execute on the Al(110) surface, so $4\text{AlCl(* )} \Rightarrow 2\text{AlCl}_2\text{(* )} + 2\text{Al(* )}$ should be the rate-determining step of the general reaction. For mechanism B, the reaction energies of $2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$ was 0.49 eV and for $\text{AlCl}_2\text{(* )} + \text{AlCl(* )} \Rightarrow \text{AlCl}_3\text{(* )} + \text{Al(* )}$ was −0.25 eV. The results indicate that $2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$ was more difficult than $\text{AlCl}_2\text{(* )} + \text{AlCl(* )} \Rightarrow \text{AlCl}_3\text{(* )} + \text{Al(* )}$ to execute on the Al(110) surface, so reaction $2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$ also should be the rate-determining step of the general reaction. In other words, $2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$ was the rate-determining step of $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ in mechanisms B and C.

## IV. CONCLUSIONS

Surface disproportionation reaction mechanism of AlCl on aluminum (110) surfaces were investigated by the plane-wave DFT. Three possible reaction mechanisms of AlCl disproportionation reaction on aluminum (110) surfaces were taken into account, and the results have been employed to confirm the reaction mechanism and the rate-determining step of the AlCl disproportionation reaction on aluminum (110) surfaces. The following conclusions were made:

1. The desorption and adsorption energies of AlCl and $\text{AlCl}_3$ are much bigger than the surface reaction energies in mechanism A, B, and C for $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ on Al(110) surface, which means that the adsorption of reactants and desorption of products greatly affect the disproportionation reaction of AlCl on aluminum (110) surfaces.

2. The results of the general reaction energies and the surface reaction energies for $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ in mechanisms A, B, and C on the Al(110) surface indicate that when $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ proceeded normally, the reaction mainly followed mechanism C, then followed mechanism B, and finally followed mechanism A. When reaction $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ proceed in reverse, the reaction mainly followed mechanism A, then followed mechanism B, and finally followed mechanism C.

3. The calculation results indicated that all general reaction energy values for mechanisms A, B, and C were negative, which means that $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ that reacted on the Al(110) surface is exothermic. In other words, when the temperature rose, $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ will proceed in reverse, whereas when the temperature dropped, $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$ proceeded normally. The result agrees with the experiment phenomenon that AlCl is stable in high temperature and reduces into Al and $\text{AlCl}_3$ in low temperature.

4. To compare the reaction energies of the reactions in mechanisms B and C, the conclusion can be drawn that $2\text{AlCl(* )} \Rightarrow \text{AlCl}_2\text{(* )} + \text{Al(* )}$ is the rate-determining step of the surface reaction $3\text{AlCl(g)} \Rightarrow 2\text{Al(* )} + \text{AlCl}_3\text{(g)}$.

## ACKNOWLEDGMENTS

This research was supported by the Joint Funds of the National Natural Science Foundation of China (Grant No. u0837604) and the State Key Development Program for Basic Research of China (Grant No. 2007CB616908).

## REFERENCES

1. R.J. Fruehan, Y. Li, and G. Carkin: *Metall. Mater. Trans. B*, 2004, vol. 35, pp. 617–23.
2. P.Y. Wang, M.S. Liu, Y.Q. Liu, and Y.N. Dai: *Nonferr. Metals*, 2006, vol. 6, pp. 23–26.
3. P.Y. Wang, M.S. Liu, and Y.N. Dai: *Light Metals*, 2008, vol. 1, pp. 13–16.

---

144—VOLUME 41B, FEBRUARY 2010

METALLURGICAL AND MATERIALS TRANSACTIONS B

4. P.Y. Wang, M.S. Liu, and Y.N. Dai: *Nonferr. Metals*, 2007, vol. 59, pp. 100–02.

5. S. Petrie: *J. Phys. Chem. A*, 1998, vol. 102, pp. 7828–34.

6. V. Kello, A.J. Šadlej, P. Pyykko, D. Sundholm, and M. Tokman: *Chem. Phys. Lett.*, 1999, vol. 304, pp. 414–22.

7. S. Petrie: *Chem. Phys. Lett.*, 2003, vol. 380, pp. 325–29.

8. A. Purath, R. Koppe, and H. Schnockel: *Chem. Commun.*, 1999, vol. 19, pp. 1933–34.

9. G. Linti and H. Schnockel: *Coord. Chem. Rev.*, 2000, vol. 206, pp. 285–319.

10. H. Kohnlein, G. Stosser, E. Baum, E. Mollhausen, U. Huniar, and H. Schnockel: *Angewandte Chemie—Int. Ed.*, 2000, vol. 39, pp. 799–801.

11. H. Schnockel and H. Kohnlein: *Polyhedron*, 2002, vol. 21, pp. 489–501.

12. A. Schnepf and H. Schnockel: *Angew Chem. Int. Ed. Engl.*, 2002, vol. 41, pp. 3532–52.

13. H. Schnockel: *Dalton Trans.*, 2008, vol. 33, pp. 4344–62.

14. H. Schnockel: *Dalton Trans.*, 2005, vol. 19, pp. 3131–36.

15. H.J. Himmel: *Eur. J. Inorg. Chem.*, 2005, vol. 10, pp. 1886–94.

16. R. Burgert, S.T. Stokes, K.H. Bowen, and H. Schnockel: *J. Amer. Chem. Soc.*, 2006, vol. 128, pp. 7904–08.

17. R. Burgert and H. Schnockel: *Chem. Commun.*, 2008, vol. 18, pp. 2075–89.

18. M. Neumaier, R. Koppe, and H. Schnockel: *Nachrichten Aus Der Chemie*, 2008, vol. 56, pp. 999–1004.

19. H. Simka, B.G. Willis, I. Lengyel, and K.F Jensen: *Prog. Crystal Growth Characterization Mater.*, 1997, vol. 35, pp. 117–49.

20. G.P. Francis and M.C. Payne: *J. Phys. Condens. Matter*, 1990, vol. 2, pp. 4395–404.

21. M.C. Payne, M.P. Teter, D.C. Allan, T.A. Arias, and J.D. Joannopoulos: *Rev. Mod. Phys.*, 1992, vol. 64, pp. 1045–97.

22. J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, and C. Fiolhais: *Phys. Rev. B*, 1992, vol. 46, pp. 6671–87.

23. J.P. Perdew, K. Burke, and M. Ernzerhof: *Phys. Rev. Lett.*, 1996, vol. 77, pp. 3865–68.

24. J.P. Perdew and A. Zunger: *Phys. Rev. B*, 1981, vol. 23, pp. 5048–79.

25. N. Govind, M. Petersen, G. Fitzgerald, D. King-Smith, and J. Andzelm: *Comput. Mater. Sci.*, 2003, vol. 28, pp. 250–58.

---

METALLURGICAL AND MATERIALS TRANSACTIONS B

VOLUME 41B, FEBRUARY 2010—145