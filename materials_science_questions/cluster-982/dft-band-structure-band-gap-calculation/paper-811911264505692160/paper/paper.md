PHYSICAL REVIEW B 78, 035425 (2008)

# Effect of packing on the cohesive and electronic properties of methanofullerene crystals

J. M. Nápoles-Duarte, $^{1}$ M. Reyes-Reyes, $^{1}$ J. L. Ricardo-Chavez, $^{2}$ R. Garibay-Alonso, $^{3}$ and R. López-Sandoval $^{2, *}$

$^{1}$Instituto de Investigación en Comunicación Optica, Universidad Autónoma de San Luis Potosí,
Alvaro Obregón 64, San Luis Potosí 78000, Mexico

$^{2}$Instituto Potosino de Investigación Científica y Tecnológica, Camino a la presa San José 2055, San Luis Potosí 78216, Mexico

$^{3}$Facultad de Ciencias Físico Matemáticas, Universidad Autónoma de Coahuila,
Conjunto Universitario Camporredondo, Edificio D, Saltillo 25000, Mexico

(Received 11 May 2008; revised manuscript received 11 June 2008; published 15 July 2008)

The crystal structure, cohesive energy, and electronic properties of bulk phases of the fullerene derivative [6,
6]-phenyl-$C_{61}$-butyric-acid-methyl-ester (PCBM) have been calculated using $ab$ initio density-functional
theory (DFT) techniques. We have only considered cubic and hexagonal crystal lattices with one PCBM
molecule per primitive cell. It was found that the cohesive properties of these systems are determined mainly
by two types of mechanisms, namely, the van der Waals interaction and the formation of weak hydrogen bonds.
Among the considered crystal structures, the most stable one, which is also the most compact structure, is the
simple cubic which has a cohesive energy difference of 1.27 eV with respect to the isolated PCBM molecule.
Regarding the electronic properties, the simple-cubic PCBM crystal is found to be a semiconductor with an
indirect band gap of 1.21 eV. In addition, we have also investigated the electronic contribution of the phenyl-
butyric-acid-methyl-ester tail to the electronic states of the entire system. By analyzing the projected density of
states (DOS), we found that the states introduced by the tail are too far from the valence and conduction bands,
so that the reduction of the band gap of bulk PCBM compared to PCBM molecule results only from the close
packing. In addition, the tail introduces a splitting of the degenerate states of the molecule reducing the gap by
about 0.2 eV compared to the $C_{60}$ molecule. On the other hand, it is shown that the simple hexagonal structure
presents a layered structure with the separation between layers of 12.6 Å. Furthermore, in the cohesive curve,
there is a nonvanishing cohesive energy for noninteracting layers. The study of the hexagonal monolayers
shows a stable structure with a cohesive energy of 0.72 eV, which indicates that PCBM can form two-
dimensional systems when the PCBM molecules are deposited on the appropriate substrates. The results
provided by this work may be important to improve our understanding concerning the mechanisms of forma-
tion of PCBM supramolecular structures, and how they can be modified to reach a desired particular property.

DOI: 10.1103/PhysRevB.78.035425
PACS number(s): 71.20.Tx, 73.61.Wp

## I. INTRODUCTION

During the last years, there has been an increasing interest
in the fabrication of photovoltaic devices using organic semi-
conductors instead of conventional inorganic semiconduc-
tors. Even if organic photovoltaic devices (OPVDs) made
from organic materials like polymers are predicted to be less
efficient than conventional ones, polymers present several
economical and technological advantages since they are
cheaper, lighter, and easier to mold in comparison with the
inorganic semiconductors. However, to foresee a widespread
use of OPVDs, it is necessary to devise better theoretical and
experimental mechanisms to increase their efficiency in a
significant way.

Recently, it has been shown that the use of blends of
polymers and fullerenes would be a good way to increase the
efficiency of organic solar cells (OSC). $^{1–4}$ However,
fullerenes have limited solubility in most solvents. One way
to overcome this difficulty may be the functionalization
of the fullerenes. For example, adding a functional group
like butyric acid (i.e., a diazo compound) to a $C_{60}$ molecule
such as in the case of the PCBM molecule (see Fig. 1)
increases its solubility in chlorobenzene. Thus, PCBM re-
sults a better candidate than raw $C_{60}$ to fabricate more effi
cient solar cells. In fact, it has been shown that PCBM crys-
tallizes in a polymeric matrix made of poly[2-methoxy-5(3',
7'-dimethyl-octyloxy)] (MDMO:PPV) (Ref. 5) or poly-3-
hexylthiophene (P3HT). $^{6–8}$ However, there exist experimen
tal evidence that the crystallization of $C_{60}$ derivatives depend
strongly on the synthesis process, the organic solvent, and
the attached functional group. $^{5,7,9,10}$ In particular, Rispens $et$
$al.^{5}$ have observed that in solar cells made of MDMO-
PPV:PCBM, it is possible to obtain different crystal struc-
tures using different solvents. Moreover, they discovered a
link between the crystal structure and the efficiency of the
cell. It is important to note that before these reports, very

![](./images/811911264505692160_1.jpg)

FIG. 1. Schematic representation of the PCBM molecule.

1098-0121/2008/78(3)/035425(7)
035425-1
©2008 The American Physical Society

little attention was paid to the mutual arrangement of the functionalized fullerene molecules in these compounds. In fact, one can be tempted to believe that the crystalline structure of functionalized $C_{60}$ molecules would be similar to that of fullerite. $^{10}$ Let us recall however that the addition of a functional group (that we call a tail) may have unpredictable consequences on the bulk properties of the resulting molecule. For instance, regarding PCBM, the presence of the tail breaks the icosahedral symmetry of $C_{60}$ which may alter the way how these molecules pack themselves. As it is well known, adopting a different crystal structure may result in different electronic and optical properties. Moreover, the crystallization process of PCBM may affect the width of the energy gap at the Fermi level compared to the isolated molecule. It is known that in the case of the $C_{60}$ molecule, the energy gap changes from 1.9 eV in the molecule to 1.5 eV in the fcc crystal. $^{11,12}$ Therefore, in order to tailor in a suitable way the efficiency of fullerene based OSC, it would be necessary to perform a detailed theoretical characterization of the interplay between functionalization and crystallization since the behavior of the electronic and optical properties depends strongly on it.

In contrast to the case of $C_{60}$ whose crystallization process, either isolated or on a substrate, has been widely studied, $^{12,13}$ up to now there have been very few studies on the crystallization of functionalized fullerenes. In particular, the adsorption and self-assembly of PCBM on the herringbone-reconstructed Au(111) as a function of coverage has been studied by Ecija et al.; $^{14}$ while at low coverages, PCBM creates 1D wires or 2D networks as dictated almost exclusively by the preference for nucleating at the FCC sites of the reconstruction, at higher coverages intramolecular interactions take over, bypassing the substrate influence and giving rise to islands composed of laterally ordered, parallel 1D double rows of PCBM molecules. Theoretical calculations using DFT were able to explain how the adsorption geometry is modified by the formation of weak hydrogen bonds, removing site selectivity. According to these results, Ecija et al. $^{14}$ proposed a model in which the basic unit is a dimer formed by two PCBM molecules coupled by hydrogen bonds. The distance between the two $C_{60}$ cages was found to be of the order of $20$ Å while that between neighbor dimers is approximately $10$ Å. Additionally, the formation of hydrogen bonds between dimers leads to the organization of the dimers into compact double-row chains. However, this ordering is destroyed by further deposition of the PCBM, producing almost amorphous layers of molecules. Therefore, the dimers are not good candidates to form 3D structures. Although this work clearly shows that PCBM may form 2D arrays with orientational order, the crystallization process of PCBM remains a standing open question to a great extent.

In this work, we study how the functionalization of fullerenes affects their relative assembly into crystals. Particularly, we have considered solids built with one PCBM molecule per lattice point and adopting cubic structures [such as the simple cubic (sc), body-centered-cubic (bcc), and face-centered-cubic (fcc) lattices] as well as 2D and 3D simple hexagonal (HEX) lattices. We performed a self-consistent relaxation of the crystal structure and intramolecular distances using DFT in the local-density approximation (LDA). Then, by computing the band properties and local density of states (DOS) of the optimal crystal structures, we show how the attached functional group modifies the stability of the crystalline phases and the electronic properties, in particular, the value and nature of the energy gap at the Fermi level.

## II. COMPUTATIONAL PROCEDURE

The calculations have been performed using the "Vienna $Ab$ initio Simulation Package" (VASP) (Ref. 15) which provides an efficient plane-wave implementation of the Kohn-Sham scheme of DFT. The interaction between the valence electrons and the ionic cores was taken into account using the projector-augmented wave method (PAW). $^{16}$ Exchange and correlation effects were treated in the LDA approximation using the Ceperley and Alder $^{17}$ exchange-correlation functional as parametrized by Perdew and Zunger. $^{18}$ At a first stage, a structural relaxation of the PCBM molecules was carried out by using the conjugated gradient algorithm to find the minimum of the energy and the interatomic forces within a convergence threshold of $1 \times 10^{-4}$ eV for energy and $1 \times 10^{-2}$ eV/Å for the forces. These thresholds were also used in all the calculations reported in the rest of the paper. Then, at a second stage, we considered several PCBM crystalline arrangements by putting the relaxed PCBM molecule in a sc, bcc, fcc, and HEX lattice and optimizing self-consistently the crystal structure, interatomic distances, and the relative orientation of the molecules at the same $ab$ initio level.

It is well known that, due to its high symmetry and electronic structure, $C_{60}$ crystallizes in compact lattices such as fcc and hexagonal close packed (HCP), stabilized by weak van der Waals interactions. $^{11,19,20}$ Both of these arrangements are the best ways of packing the approximately spherical molecule, maximizing the occupation of the available volume. For this property to govern the crystallization of PCBM, the tails should adopt a relative orientation in such a way that the volume of the unit cell is minimized. However, we cannot rule out a possible covalent bonding between the tails from neighbor molecules or between the tails and the $C_{60}$ cages. In this work, we have only considered the crystallization of PCBM from purely van der Waals packing. Therefore, we have implemented a method to arrange 3D objects in a cell so that it maximizes packing. For instance, in the case of the SC lattice, the resulting preferential orientation of the tails is along the main diagonal of the cell. The lattice constant obtained with this method was used as a starting point for the relaxation process. One can also proceed in a different way, for example, starting from a cubic lattice and then allowing the system to relax the shape and volume of the unit cell as well as the interatomic distances in a self-consistent way, i.e., without imposing any constraint. Nevertheless, the results obtained with the latter method are nearly quantitatively the same as in the case of relaxing only the cell volume.

## III. RESULTS

### A. Cubic structures

In Fig. 2, we show the binding energy $E_b=E-E_{mol}$ of the sc, bcc, and fcc crystalline phases of PCBM as a function of

![](./images/811911264505692160_2.jpg)

FIG. 2. Binding energy of cubic PCBM crystals as a function of the center to center distance $a$ referred to the optimal value $a_0$.

the center to center distance $a$ between neighbor molecules, referred to the total energy $E_{\text{mol}}$ of the isolated PCBM molecule. Note that $a$ is scaled by the optimal value $a_0$ of the corresponding structure, which was found to be $a_0$=9.9 Å, $a_0$=11.1 Å, and $a_0$=12.1 Å for the sc, bcc, and fcc lattices, respectively. These results were obtained by considering only the $\Gamma$ point contribution to the $k$-space integrals over the Brillouin zone, which is a cheap way to compute the potential-energy curves. It is important to note that these values do not change appreciably when a finer grid (for example, a 4×4×4 Monkhorst-Pack grid) is used to sample the Brillouin zone, indicating that the system behaves indeed as a molecular solid. For a matter of comparison, the fully optimized $E_b$ values are shown in Table I.

We found that the most stable crystalline phase of PCBM is the sc, with a binding-energy value of $-1.27$ eV, which is lower than the corresponding values for close-packed 2D and 3D hexagonal lattices. This is in remarkable contrast with the case of $\text{C}_{60}$, which always prefers to adopt a fcc-like crystalline structure. On the other hand, the minimization of the binding energy coincides with a minimization of the cell volume, which is a characteristic feature of the crystallization processes mediated by van der Waals interactions. Note that in all the considered cases, the binding energy is always higher than the reported value of $-1.6$ eV for fcc $\text{C}_{60}$, $^{11,19}$ indicating that PCBM crystals are slightly less stable than $\text{C}_{60}$. However, we cannot rule out the possibility that other crystalline phases having more than one PCBM molecule per unit cell may have a lower binding energy than $\text{C}_{60}$. $^{10}$

<table>
<caption>TABLE I. Binding energy of several PCBM crystalline phase.</caption>
<thead>
  <tr>
    <th rowspan="2">Structure</th>
    <th>$a_0$</th>
    <th>Binding energy</th>
    <th>Volume</th>
  </tr>
  <tr>
    <th>(Å)</th>
    <th>(eV)</th>
    <th>($\text{Å}^3$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>sc</td>
    <td>9.9</td>
    <td>$-1.27$</td>
    <td>970.30</td>
  </tr>
  <tr>
    <td>bcc</td>
    <td>11.1</td>
    <td>$-0.95$</td>
    <td>1052.80</td>
  </tr>
  <tr>
    <td>fcc</td>
    <td>12.1</td>
    <td>$-0.52$</td>
    <td>1252.69</td>
  </tr>
  <tr>
    <td>HEX 3D</td>
    <td>$a$=9.7, $c$=12.6</td>
    <td>$-1.05$</td>
    <td>1026.70</td>
  </tr>
  <tr>
    <td>HEX 2D</td>
    <td>$a$=9.7, $c$=22.0</td>
    <td>$-0.72$</td>
    <td>1959</td>
  </tr>
</tbody>
</table>

It is important to note that in reported experimental works such as that of Hoppe and Sariciftci, $^{10}$ it was assumed that PCBM adopts a fcc structure with a lattice constant of about 14 Å, i.e., a center to center distance of about 10 Å. This was inferred from hexagonal diffraction patterns on toluene cast MDMO-PPV:PCBM blends. $^{10}$ Nevertheless, we found that the fcc structure is the least stable one, with an $a$ value of 12.1 Å. On the other hand, Rispens $et$ $al.^5$ have proposed a packing mechanism of PCBM mediated by solvent molecules, with an $a$ value of about 10 Å. As it is known, the use of solvents may affect the crystallization process of PCBM, however, in this work, we do not consider possible effects coming from the solvent.

We already mentioned that the tail of PCBM may play an important role in its self-organization process through the formation of weak hydrogen bonds between aromatic rings or methyl radicals and oxygen. $^{14}$ Our calculations support this observation, however, the formation of the hydrogen bonds appears just as an additional mechanism, besides the van der Waals interaction, that further stabilizes the crystal.

In order to elucidate how the crystalline structure and relative orientation of the PCBM molecules affect the band-structure properties of the resulting solid, we have studied the behavior of electronic quantities such as the nature and width of the energy gap $E_g$ at the Fermi level and the local density of states (LDOS). For testing purposes, we calculated first the electronic properties of the $\text{C}_{60}$ molecule and its FCC solid. The resulting values of $E_g$ are 1.65 and 1.1 eV, respectively, which are in good agreement with the published theoretical results. $^{19,20}$ We are of course aware that LDA underestimates the value of $E_g$, where the reported values are of 3.5 eV for the molecule and 2.3 eV for the solid, $^{21}$ and overestimates the binding of the structure. Nevertheless, the LDA is known to identify qualitatively the effects of crystallization on the structural, optical, and electronic properties of $\text{C}_{60}$. $^{11,19,20}$ Our calculations also show that the PCBM molecule has an $E_g$ value of 1.46 eV, whereas the experimental value is 2.3 eV. $^{22}$ Thus, the presence of the tail modifies the electronic properties compared to the pristine $\text{C}_{60}$, notably through a reduction of $E_g$. This $E_g$ reduction has consequences on the optical properties; in particular, the PCBM molecule shows a shift of its absorption spectrum toward the infrared. Among several causes, this can result from the loss of icosahedral symmetry.

In the case of the periodic PCBM structures, we calculated the electronic properties at the optimal lattice constant within a precision of $1\times10^{-4}$ eV. The results show that, for all the considered cases, PCBM crystals are semiconductors with an $E_g$ value which depends strongly on the crystalline structure. The electronic structure near the Fermi level of two representative cases, which correspond to opposite behaviors, is shown in Fig. 3. In the case of the sc lattice (a) we observe a strong dispersion, which indicates a significant overlap between orbitals from PCBM molecules in different cells. On the contrary, the fcc crystal (b) presents a very small dispersion, implying a relative lower coupling compared to the SC case. Additionally, the sc crystal is an indirect band-gap semiconductor with an $E_g$ value of 1.21 eV, where the top of the valence band (TVB) is at the $M$ point while the bottom of the conduction band (BCB) is at the $X$

![](./images/811911264505692160_3.jpg)

FIG. 3. Electronic band structure near the Fermi level of (a) the sc and (b) the fcc PCBM crystals.

point of the Brillouin zone. Similarly, the fcc crystal is an indirect band-gap semiconductor whereas the bcc crystal is a direct band-gap semiconductor (see Table II). Note that for all cubic PCBM crystals, the calculated gaps are slightly smaller than that of the isolated molecule, i.e., the crystalli- zation process induces a level broadening and splitting over the entire energy bandwidth.

In previous theoretical works, it has been shown that it may be possible to increase the efficiency of P3HT:PCBM solar cells by tuning the BCB position of P3HT relative to the BCB position of PCBM. Efficiencies up to 8% were ob- tained when the BCB(P3HT)–BCB(PCBM) offset was of the order of 0.5 eV, while the experimental values are of the order of $1.1\ \text{eV}.^{22}$ This offset could therefore be tailored by modifying the crystallization process such that, while the BCB(PCBM) increases the BCB(P3HT) decreases whereas the TVB is maintained constant. In our case, we observe from Fig. 3 that the TVB of the sc PCBM crystal shows a very small dispersion, indicating that the TVB position of the

<table>
<caption>TABLE II. Energy gaps of cubic PCBM crystalline phases.</caption>
<thead>
  <tr>
    <th rowspan="2">Structure</th>
    <th>$E_{g}$</th>
    <th rowspan="2">Gap type</th>
    <th>TVB</th>
    <th>BCB</th>
  </tr>
  <tr>
    <th>(eV)</th>
    <th>(eV)</th>
    <th>(eV)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>sc</td>
    <td>1.21</td>
    <td>Indirect</td>
    <td>0.73 M</td>
    <td>1.94 X</td>
  </tr>
  <tr>
    <td>bcc</td>
    <td>1.32</td>
    <td>Direct</td>
    <td>0.20 H</td>
    <td>1.52 H</td>
  </tr>
  <tr>
    <td>fcc</td>
    <td>1.40</td>
    <td>Indirect</td>
    <td>–0.81 W</td>
    <td>0.59 $\Gamma$</td>
  </tr>
</tbody>
</table>

![](./images/811911264505692160_4.jpg)

FIG. 4. (Color online) Density of states of (a) the sc and (b) the fcc PCBM crystals at the optimal $a$ value. The solid blue line refers to the total DOS of the crystals and the dashed red line corresponds to the LDOS of the PCBM tail.

PCBM molecule is only slightly modified by the crystalliza- tion process, contrary to the case of the BCB which is low- ered by this process. This suggests that solar cells made of sc PCBM crystals should have decreased efficiency. Neverthe- less, it has also been shown that in high-efficiency solar cells, in addition to the PCBM crystallization, $^{7,8}$ there exists a P3HT crystallization $^{3,4,8}$ that may decrease its relative en ergy gap in such a way that the offset of 0.5 eV could be reached. Therefore, it may be possible to obtain experimen- tally the high efficiencies predicted theoretically by Koster et al. $^{22}$ by modifying the interplay between the crystallization process of PCBM mediated by the solvent and the annealing time of the P3HT:PCBM blend.

Further information on the electronic structure of the PCBM crystals and the coupling between the tail and the $C_{60}$ cage may be obtained by analyzing the total and the local DOS. For instance, in Fig. 4 we show the DOS of (a) the SC, and (b) the FCC PCBM crystals. In both cases, the solid blue curve represents the total DOS of the crystal while the dashed red curve is the local DOS of the tail. These curves were calculated by using a Monkhorst-Pack grid consisting of 64 equally-spaced $k$ points to sample the Brillouin zone. The $k$-space integration was performed using Blöchl $^{16}$ tetra hedron method. Regarding the SC structure, we observe an important broadening of the energy levels, resulting from the overlap of neighbor PCBM orbitals due to the packing. On the other hand, for the fcc structure, the energy gap referred to the molecule is of the order of 0.06 eV, suggesting that the system preserves the localized molecular character. By ana-

![](./images/811911264505692160_5.jpg)

FIG. 5. Binding curves for the simple hexagonal systems. The plots show the binding curves for $a$=9.6, 9.7 and 10.0 $\mathring{\text{A}}$ ranging from 12 to 18 $\mathring{\text{A}}$ in the $c$ parameter.

lyzing the behavior of the dashed red curve, i.e., of the local DOS of the tail, we conclude that it contributes only marginally to the states near the Fermi level. Thus, the direct influence of the tail on the electronic properties of the PCBM crystals is negligible. Let us remember however that the tail was introduced in order to increase the solubility of the fullerene in organic solvents and not for its electronic properties. Nonetheless, as we show in this work, the tail plays an important role in the crystallization process of PCBM due to the loss of icosahedral symmetry.

### B. Hexagonal structures
Apart from the cubic structures, we have also explored the crystallization of PCBM on close-packed 2D and simple 3D hexagonal lattices, which compete in stability with the cubic ones, as the reader will see in this section. In fact, previous theoretical works on the crystallization of $C_{60}$ on a silicon surface have shown the formation of stable hexagonal monolayers having little interaction with the substrate.¹²

The calculations of the PCBM hexagonal structures were performed in the same way as in the case of the cubic ones, i.e., using the same model parameters and considering a single PCBM molecule per cell. However, in the case of the 3D HEX lattice, we have to optimize two cell parameters: the in-plane center-to-center distance $a$ between molecules and the interlayer separation $c$. Representative results about the stability of these structures as a function of $a$ and $c$ are shown in Fig. 5. These calculations were done by taking only the $\Gamma$-point contribution to the $k$-space sampling over the Brillouin zone. We observe from the figure that the optimal cell parameters $a$=9.7 $\mathring{\text{A}}$ and $c$=12.6 $\mathring{\text{A}}$ clearly indicate a tendency to form layered structures. This crystallization route is fundamentally different from that of the cubic structures, however, the resulting solid is one of the most stable with a cohesive energy value which is only 0.2 eV above that of the SC lattice and a cell volume of only 5% larger. Note that the in-layer close-packing is comparable to that found in layers of $C_{60}$ deposited on surfaces.²³,²⁴ However, for PCBM, we are not aware of any experimental work about a layered growth. Another feature emerging from Fig. 5 is that, even for a very large separation between the layers, there is still a nonvanishing binding energy, indicating that the hexagonal monolayers are very stable individually. Nonetheless, close to the optimal structure, the binding energy coming from the interlayer interaction contributes significantly (about 30%) to the stability of the crystal.

![](./images/811911264505692160_6.jpg)

FIG. 6. Band plots for (a) the simple hexagonal crystal and (b) the hexagonal layer. The simple hexagonal has the top of the valence band at the $M$ point and the bottom of the conduction band at the $H$ point, whereas for the hexagonal layer, the top of valence and bottom of conduction bands are both at the $K$ point.

Figure 6 shows the band structure of the hexagonal lattices. We note a substantial band dispersion along directions on the layers and nearly flat bands along directions normal to the layers (for example, the $\Gamma$-$A$ direction) which mean that there is only a weak interaction between layers. In a similar way to the cubic lattices, the hexagonal crystal is an indirect band-gap semiconductor where the TVB is at the $M$ point and the BCB at the $H$ point, which gives $E_g$=1.11 eV.

Looking at the DOS plot of the hexagonal lattices (see Fig. 7), we observe many resemblances to the cubic systems. For example, the bands near the Fermi level show a large dispersion both at the valence and conduction states due to the strong overlap of neighbor molecular orbitals. Similarly, the electronic states of the tail have a negligible contribution to the states close to the Fermi level.

Finally, it is worth pointing out the case of an isolated PCBM hexagonal monolayer, but in order to avoid computing the properties of the single 2D HEX, we have made use of the superlattice concept and considered the 3D HEX with

![](./images/811911264505692160_7.jpg)

FIG. 7. (Color online) Density of states of (a) the simple hexagonal crystal and (b) the hexagonal layer. The solid blue curve shows the total DOS of the PCBM crystal, whereas the dashed red curve corresponds to the LDOS coming from the PCBM tail.

a very large interlayer separation of $22$ $\text{\AA}$. Then, the $a$ parameter was varied from $9.6$ to $10.14$ $\text{\AA}$. The minimum of the energy was found to be at $9.7$ $\text{\AA}$ which is the same as in the 3D HEX. However, due to the absence of interlayer interaction, the binding energy of the system with respect to the molecule drops to $-0.72$ eV. The rest of the properties such as the band structure and the DOS (Figs. 6 and 7) are also not very different from the case of the 3D HEX. However, the hexagonal monolayer is a direct-gap semiconductor with an $E_g$ value of $1.11$ eV at the $K$ point.

## IV. SUMMARY AND CONCLUSIONS

In this work, we have presented a study of the manner in which functionalized fullerenes pack together forming crystals and how this process is affected by the nature and interaction of the functional groups with the fullerene cages. This study was motivated by experimental evidence on the importance of crystallization when annealing is introduced in the fabrication of organic-based photodevices and the effect of the solvents on the efficiency of these devices.

Our results indicate that the tail has important consequences on the cohesive properties of the crystalline structure. We have found that the sc crystalline structure is the most stable with a center to center distance of $9.9$ $\text{\AA}$, which is different of the fcc crystalline structure reported for the $\text{C}_{60}$ molecule. In addition, it was shown that the 3D HEX crystals are the second most stable structure with a layered structure. The latter structure has not been yet experimentally reported. In addition, our calculations suggest that one candidate for the most stable PCBM crystal could be that one arranged in a kind of solid with alternate triangular layers. The insight of a solid composed of triangular layers is provided by the results for hexagonal lattices. Thus, exploring the two-dimensional case, we found that it is sufficiently stable by itself ($E_b=-0.72$ eV). The formation of a layered tridimensional structure could be obtained by stacking layers one over the other and introducing a relative rotation until the most stable structure is found. However, the consideration of structures with more than one fullerene molecule per unit cell, although more realistic, is computationally more expensive and it is beyond of the main goal of this work. On the other hand, the tail effect on the electronic properties is small due to the fact that the introduced electronic states are energetically very far from the valence and conduction band. However, the tail eliminates the icosahedral symmetry of the $\text{C}_{60}$ molecule. The loss of this symmetry produces the splitting of some degenerate states and, as consequence, our calculated PCBM $E_g$ is $0.2$ eV smaller than that of the $\text{C}_{60}$ molecule. Moreover, this symmetry loss is reflected in an increased infrared absorption of the PCBM molecule as it has been corroborated by absorption measurements.

The minimum-energy structures that we found show that besides of the expected van der Waals interactions, the formation of weak hydrogen bonds between neighbor molecules in the crystal contributes to the stability of the structures. Hydrogen bonds have been studied in terms of their geometry and intermolecular interaction by Saha et al.,$^{25}$ when they occur in hexagonal host frameworks where the fully ordered structures are ascribed to the numerous heteroatom interactions from host and guest molecules. They show a distance of about $2.6$ $\text{\AA}$ between pairs of $\text{C-H}\cdots\text{O}$ hydrogen bonds for stabilizing their ordered structures. The work of Saha et al.$^{25}$ shows the importance of hydrogen bonds in crystal packing when aromatic/heteroaromatic groups are involved, where hydrogen bonds are the strongest of the noncovalent interactions and they are widely exploited in the design of molecular crystals. From our work, the less stable structure, the fcc, is also the one which does not present this type of interaction. On the other hand, the rest of the minimum-energy-calculated structures show an interaction between at least one of the hydrogen atoms in the phenyl ring with one of the oxygen atoms of the neighboring PCBM molecules. For example, the nearest distance between one hydrogen of the phenyl ring with the oxygen of a neighbor molecule in the SC crystal is about $2.57$ $\text{\AA}$, while for the simple hexagonal structure and for the hexagonal layer, the distances are about $2.3$ and $2.27$ $\text{\AA}$, respectively. This interactions are reasonably expected due to the original goal of the formation of the fullerene derivative PCBM which is to improve the miscibility of $\text{C}_{60}$ in solvents.

Finally, the synthesis of real PCBM crystals will depend on several factors such as the experimental procedure, the use of solvents which may act as guest molecules, etc. In our approach, we wanted to show that the assembly of a molecular crystal is governed by chemical and geometrical factors, which are the basis of solid-state molecular recognition that should be exploited in the design of noncovalent crystals of the fullerene derivative PCBM.

## ACKNOWLEDGMENTS

This work was supported by CONACYT through Grant No. CONACYT 2005-J48897-Y, Fdo. Inst. R. Lopez 67554 S-3125, and for the support of one of the authors (J.M.N.D.). The computational resources that we used for this work have been provided by the National Center of Supercomputing CNS-IPICyT, Mexico.

*sandov@ipicyt.edu.mx

$^{1}$G. Yu, J. Gao, J. C. Hummelen, F. Wudl, and A. J. Heeger, Science **270**, 1789 (1995).

$^{2}$M. Reyes-Reyes, K. Kim, and D. L. Carroll, Appl. Phys. Lett. **87**, 083506 (2005).

$^{3}$W. Ma, C. Yang, X. Gong, K. Lee, and A. J. Heeger, Adv. Funct. Mater. **15**, 1617 (2005).

$^{4}$G. Li, V. Shrotriya, J. Huang, Y. Yao, T. Moriarty, K. Emery, and Y. Yang, Nat. Mater. **4**, 864 (2005).

$^{5}$M. T. Rispens, A. Meetsma, R. Rittberger, C. J. Brabec, N. S. Sariciftci, and J. C. Hummelen, Chem. Commun. (Cambridge) **2003**, 2116.

$^{6}$X. Yang, J. Loos, S. C. Veenstra, W. J. H. Verhees, M. M. Wienk, J. M. Kroon, M. A. J. Michels, and R. A. J. Janssen, Nano Lett. **5**, 579 (2005).

$^{7}$M. Reyes-Reyes, K. Kim, J. Dewald, R. Lopez-Sandoval, A. Avadhanula, S. Curran, and D. L. Carroll, Org. Lett. **7**, 5749 (2005).

$^{8}$M. Reyes-Reyes, R. López-Sandoval, J. Arenas-Alatorre, R. Garibay-Alonso, D. L. Carroll, and A. Lastras-Martínez, Thin Solid Films **516**, 52 (2007).

$^{9}$X. Yang, J. K. J. van Duren, M. T. Rispens, J. C. Hummelen, R. A. J. Janssen, M. A. J. Michels, and J. Loos, Adv. Math. **16**, 802 (2004).

$^{10}$H. Hoppe and N. S. Sariciftci, J. Mater. Chem. **16**, 45 (2006).

$^{11}$S. Saito and A. Oshiyama, Phys. Rev. Lett. **66**, 2637 (1991).

$^{12}$J. Nakamura, T. Nakayama, S. Watanabe, and M. Aono, Phys. Rev. Lett. **87**, 048301 (2001).

$^{13}$E. J. Snyder, M. S. Anderson, W. M. Tong, R. S. Williams, S. J. Anz, M. W. Alvarez, Y. Rubin, F. N. Diederich, and R. L. Whetten, Science **253**, 171 (1991).

$^{14}$D. Écija, R. Otero, L. Sánchez, J. M. Gallego, Y. Wang, M. Alcamí, F. Martín, N. Martín, and R. Miranda, Angew. Chem., Int. Ed. **46**, 7874 (2007).

$^{15}$G. Kresse and J. Hafner, Phys. Rev. B **47**, 558 (1993); G. Kresse and J. Furthmüller, ibid. **54**, 11169 (1996); http://cms.mpi.univie.ac.at/vasp

$^{16}$P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994); G. Kresse and D. Joubert, ibid. **59**, 1758 (1999).

$^{17}$D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. **45**, 566 (1980).

$^{18}$J. P. Perdew and A. Zunger, Phys. Rev. B **23**, 5048 (1981).

$^{19}$N. Troullier and J. L. Martins, Phys. Rev. B **46**, 1754 (1992).

$^{20}$E. L. Shirley and S. G. Louie, Phys. Rev. Lett. **71**, 133 (1993).

$^{21}$R. W. Lof, M. A. van Veenendaal, B. Koopmans, H. T. Jonkman, and G. A. Sawatzky, Phys. Rev. Lett. **68**, 3924 (1992).

$^{22}$L. J. A. Koster, V. D. Mihailetchi, and P. W. M. Blom, Appl. Phys. Lett. **88**, 093511 (2006).

$^{23}$M. K.-J. Johansson, A. J. Maxwell, S. M. Gray, P. A. Brühwiler, D. C. Mancini, L. S. O. Johansson, and N. Mårtensson, Phys. Rev. B **54**, 13472 (1996).

$^{24}$J. G. Hou, Y. Jinlong, W. Haiqian, L. Qunxiang, Z. Changgan, Y. Lanfeng, W. Bing, D. M. Chen, and Z. Qingshi, Nature (London) **409**, 304 (2001).

$^{25}$B. K. Saha, S. Aitipamula, R. Banerjee, A. Nangia, R. K. R. Jetti, R. Boese, C. Lam, and T. C. W. Mak, Mol. Cryst. Liq. Cryst. **440**, 295 (2005).