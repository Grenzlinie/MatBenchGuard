# Impurity clustering and impurity-induced bands in PbTe-, SnTe-,
and GeTe-based bulk thermoelectrics

Khang Hoang, $^{1}$ S. D. Mahanti, $^{2}$ and Mercouri G. Kanatzidis $^{3,4}$

$^{1}$Materials Department, University of California,
Santa Barbara, California 93106, USA

$^{2}$Department of Physics and Astronomy,
Michigan State University, East Lansing, Michigan 48824, USA

$^{3}$Department of Chemistry, Northwestern University, Evanston, Illinois 60208, USA

$^{4}$Materials Science Division, Argonne National Laboratory, Argonne, Illinois 60439, USA

(Dated: October 30, 2018)


### Abstract

Complex multicomponent systems based on PbTe, SnTe, and GeTe are of great interest for infrared devices and high-temperature thermoelectric applications. A deeper understanding of the atomic and electronic structure of these materials is crucial for explaining, predicting, and optimizing their properties, and to suggest new materials for better performance. In this work, we present our first-principles studies of the energy bands associated with various monovalent (Na, K, and Ag) and trivalent (Sb and Bi) impurities and impurity clusters in PbTe, SnTe, and GeTe using supercell models. We find that monovalent and trivalent impurity atoms tend to come close to one another and form impurity-rich clusters, and the electronic structure of the host materials is strongly perturbed by the impurities. There are impurity-induced bands associated with the trivalent impurities that split off from the conduction-band bottom with large shifts towards the valence-band top. This is due to the interaction between the $p$ states of the trivalent impurity cation and the divalent anion which tends to drive the systems towards metallicity. The introduction of monovalent impurities (in the presence of trivalent impurities) significantly reduces (in PbTe and GeTe) or slightly enhances (in SnTe) the effect of the trivalent impurities. One, therefore, can tailor the band gap and band structure near the band gap (hence transport properties) by choosing the type of impurity and its concentration or tuning the monovalent/trivalent ratio. Based on the calculated band structures, we are able to explain qualitatively the measured transport properties of the whole class of PbTe-, SnTe-, and GeTe-based bulk thermoelectrics.

PACS numbers: 71.55.-i, 71.20.-b, 72.20.Pa, 71.28.+d


## I. INTRODUCTION

The thermoelectric phenomenon involves direct thermal-to-electric energy conversion, which can be used for both refrigeration and power generation. Together with other technologies for energy generation and conversion, it is expected to play an increasingly important role in meeting the energy demands of the next generations. [1] Although the efficiency efficiency effectiveness efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency efficiency

simplicity. When the relaxation time depends on $\mathbf{k}$ through $\epsilon(\mathbf{k})$, the transport distribution function takes the form [5]

$$
\Sigma(\epsilon)=N(\epsilon) \nu_{x}(\epsilon)^{2} \tau(\epsilon),
\tag{5}
$$

where $N(\epsilon)$ is the electronic density of states (DOS).

As $ZT$ approaches $\infty$, the thermoelectric conversion efficiency approaches its Carnot value. [5] Increasing $ZT$ has been one of the most challenging tasks (increasing $\sigma$ usually reduces $S$ and increases $\kappa_{el}$, the net result being a reduction in $ZT$), although there are no fundamental thermodynamic arguments against achieving very high values of $ZT$. [6] More realistic approaches to increase $ZT$ have followed two different paths. One is to reduce $\sigma$ and $\kappa_{el}$ and increase $S$ by manipulating the DOS near the chemical potential through band-structure engineering or strong correlation effects. The other is to decrease $\kappa_{latt}$ through lattice engineering. Examples of the former are In-doped PbTe, [7] Tl-doped PbTe, [8] and doped cobaltates. [9] Those of the latter are skutterudites [10] and $\text{AgPb}_m\text{SbTe}_{m+2}$ (LAST-$m$; LAST stands for Lead Antimony Silver Tellurium) containing Ag-Sb-rich nanoscale domains. [11] Recently, it has been suggested that one can also achieve high $ZT$ in systems such as $\text{In}_4\text{Se}_{3-\delta}$ by exploiting the intrinsic nanostructural bulk properties induced by charge-density waves. [12]

Discoveries of new thermoelectric materials that can give large $ZT$ values, particularly at high temperatures ($T$$\sim$600–700 K), have created a great deal of excitement. LAST-$m$, which can be considered as a mixture of PbTe and $\text{AgSbTe}_2$, is among these materials. This $n$-type thermoelectric gives $ZT$=1.7 at 700 K for $m$=18. [11] Compared to PbTe, LAST-18 shows reduced thermal conductivity. The increase in $ZT$ in LAST-$m$ has been ascribed to the decrease in $\kappa_{latt}$ resulting from nanostructuring in the system where high-resolution transmission electron microscopy images indicate inhomogeneities in the microstructure of these materials, showing nanoscale domains of a Ag-Sb-rich phase embedded in a PbTe matrix. [11, 13, 14] Other bulk thermoelectrics discovered more recently also have high $ZT$ values and are nanostructured. Examples are $p$-type $\text{Ag(Pb}_{1-y}\text{Sn}_y\text{)}_m\text{SbTe}_{m+2}$ (LASTT-$m$), [15] $p$-type $\text{Ag}_{1-x}\text{SnSb}_{1+x}\text{Te}_3$ (TAST-$m$), [16] $n$-type $\text{Pb}_{1-x}\text{Sn}_x$Te-PbS, [17] $n$-type $\text{Ag}_{1-x}\text{Pb}_m\text{MTe}_{m+2}$ ($M$=Sb, Bi), [18] $p$-type $\text{Na}_{1-z}\text{Pb}_m\text{Sb}_y\text{Te}_{m+2}$ (SALT-$m$), [19] and $n$-type $\text{K}_{1-x}\text{Pb}_{m+\delta}\text{Sb}_{1+\gamma}\text{Te}_{m+2}$ (PLAT-$m$). [20]

It is well known that transport and optical properties of semiconductors are dominated by the electronic states in the neighborhood of the band gap. From Eqs. (1)–(5), clearly

large values of $ZT$ require large values of $S$ and $\sigma$, both of which depend sensitively on the nature of the electronic states near the band gap. Thus it is essential to understand the underlying physics of the band gap formation and the nature of the electronic states in its neighborhood before being able to explain, predict, and optimize the properties of the systems. One, however, needs to know their atomic structures. Unfortunately, there is little, if any, information about the detailed atomic structures of the above mentioned thermoelectrics.

Our approach to understand the properties of LAST-$m$ and similar systems is based on a defect perspective. As a first-order approximation to the real system, LAST-$m$, for example, can be considered as PbTe doped with equal amounts of Ag and Sb, i.e., Ag and Sb being treated as defects (impurities) in PbTe. This approximation is expected to be good at low Ag, Sb concentrations (i.e., large $m$ values, which are of practical interest). One then looks at the electronic states induced by these impurities and their effect on the transport properties. The concentrations of Ag and Sb atoms ($x$~5% for $m$=18) are small enough such that starting from an impurity picture is justified and physically meaningful. Yet they are large enough such that the effects of impurities and impurity-impurity interaction (either directly or indirectly through the host) on the electronic structure near the band gap are significant.

The studies of electronic states associated with impurities in PbTe have been so far mostly based on the single-particle DOS. [21-28] Mahanti and Bilc [21] reported rather limited results on the band structure of doped PbTe, only for PbTe simultaneously doped with Ag and Sb. A detailed analysis of the band structures showing the impurity-induced bands obtained in first-principles calculations is presently lacking. In fact, band structure can provide us with more information on the electronic states, especially on the impurity-induced or impurity-modified electronic states (i.e., the energy bands associated with the impurity in the system) and how they are formed. In addition, the relationship between the transport properties and electronic structure is more subtle and a detailed band structure is needed in order to have a better understanding of the transport properties of the system. Moreover, a general understanding of defect states in narrow band-gap semiconductors is also extremely helpful in searching for materials with desired properties.

In this paper, we present our extensive first-principles studies of the band structures of PbTe, SnTe, and GeTe in the presence of monovalent (Na, K, and Ag) and trivalent (Sb and

Bi) substitutional impurities on the cation (Pb, Sn, or Ge) sites and discuss how the transport properties of these systems can be understood in terms of the calculated band structures, particularly those features which are sensitive to the impurities. We also discuss how the impurities interact with each other leading to impurity clustering and local relaxations near the impurity atoms. The arrangements of this paper is as follows: In Sec. II, we present supercell models for defect calculations and the calculational details. Impurity clustering and local relaxations near the impurity atoms in various systems are discussed in Sec. III. Impurity-induced bands associated with different monovalent and trivalent impurities in PbTe, SnTe, and GeTe are presented in Sec. IV. Also in this section, we show how the changes in the band structures in going from one system to the other can explain the experimental transport data qualitatively. We conclude this paper with a summary in Sec. V.

## II. THEORETICAL MODELING

Among the three IV-VI binary tellurides, PbTe and SnTe are known to crystallize in a NaCl-type structure with face-centered cubic (fcc) unit cell. GeTe also has a NaCl-type structure, but with a slight (rhombohedral) distortion due to a phase transition at low temperature. [29] Since the distortion is small, GeTe is assumed to have the NaCl-type structure in the current studies.

To understand how each impurity perturbs the electronic structure of the host and how two impurities in a pair interfere with each other, first-principles calculations for single im- purities and impurity pairs in $R$Te, where $R$={Pb, Sn, Ge}, were carried out using supercell models. These calculations mainly made use of (2×2×2) cubic supercells, which contains 64 atoms/cell and requires lattice constant doubling in all the three directions with respect to that of the bulk materials. For a single impurity $M$, the supercell corresponds to the composition $MR_{m+1}$Te$_{m+2}$, $m$=30. The composition in the supercell for an impurity pair ($M$,$M'$) is $MM'R_{m}$Te$_{m+2}$.

The two impurity atoms in a ($M$,$M'$) pair are arranged with different distances and dif- ferent geometries *vis-à-vis* the intervening Te atoms. They are arranged as the first, second, third, fourth, or fifth nearest neighbors (n.n.) of one another on the Pb sublattice with the impurity-impurity distance taking values $a/\sqrt{2}$, $a$, $a\sqrt{3/2}$, $a\sqrt{2}$, and $a\sqrt{3}$, respectively, where $a$ is the theoretical lattice constant of the bulk materials. The calculated values of


the lattice constant are $a$=6.55 Å (PbTe), 6.40 Å (SnTe), and 6.02 Å (GeTe). This supercell model has been used by Bilc *et al.* [22] and by Hazama *et al.* [24] for $(M,M')$=(Ag,Sb) in PbTe. Besides the (2×2×2) supercells, we also made use of (3×3×3) supercells which contains 216 atoms/cell ($m$=106).

Structural optimization, total energy and electronic structure calculations were performed within the DFT formalism, using the generalized-gradient approximation (GGA) [30] and the projector-augmented wave method [31, 32] as implemented in the VASP code. [33–35] Scalar relativistic effects (mass-velocity and Darwin terms) and spin-orbit interaction (SOI) were included, except in ionic optimization. In this case, only the scalar relativistic effects were taken into account since we found that the inclusion of SOI did not have a significant influence on the atomic structure. For the (2×2×2) supercells, we used a 5×5×5 Monkhorst-Pack [36] **k**-point mesh in the self-consistent run; whereas for the (3×3×3) ones, 5 **k**-points were used in the irreducible BZ. The energy cutoff was set to 300 eV and convergence with respect to self-consistent iterations was assumed when the total energy difference between consecutive cycles was less than $10^{-4}$ eV.

It is known that there are fundamental issues with DFT and the use of supercell method in studying defects in semiconductors. [37] These include the tendency of DFT-GGA to underestimate the band gaps of semiconductors (the so-called "band-gap problem") and the finite size and artificial periodicity of the supercells. The former problem is severe, e.g., in PbTe where the calculated band gap is smaller than the experimental one by more than 50% the defect states may artificially overlap with the valence- and/or conduction-band edges. [38] Although supercell calculations using methods which go beyond DFT-GGA, such as screened-exchange local-density approximation, [39] hybrid functional approximation, [40] and $GW$ approximation, [41] may help fix this problem, they are, however, still not affordable computationally due to the large supercell sizes and the heavy elements present in our systems. [42]

## III. IMPURITY CLUSTERING IN BULK THERMOELECTRICS

As a first step towards understanding the energetics of nanostructuring in telluride-based bulk thermoelectrics, we investigated various impurity pairs in different pair configurations embedded in the host materials. The formation energy of an impurity pair as a function of

the pair distance can help identify the most stable configuration energetically and provide valuable information on how the impurity atoms are likely to arrange themselves in the host under certain synthesis conditions.

The formation energy $E^f$ of a defect X in neutral charge state is defined as [43]

$$
E^f = E_{\text{tot}}(\text{X}) - E_{\text{tot}}(\text{bulk}) - \sum_{i} n_i \mu_i, \tag{6}
$$

where $E_{\text{tot}}(\text{X})$ and $E_{\text{tot}}(\text{bulk})$ are the total energies of a supercell containing X and of a supercell containing only bulk materials; $\mu_i$ is the chemical potential of species $i$ (host atoms or impurity atoms) which corresponds to the energy of the reservoir with which atoms of species $i$ are being exchanged, and $n_i$ denotes the number of atoms of species $i$ that have been added ($n_i$>0) or removed ($n_i$<0) to create the defect. Since we are interested mostly in the relative formation energies of a given pair for different spatial configurations, the precise values of the chemical potentials are not important. For simplicity we have fixed their values to the total energy (per atom) of the bulk in their standard metallic states.

### A. Impurity Clustering

Figures 1(a)-1(i) show the formation energy plots of X=(Ag,Ag), (Sb,Sb), (Ag,Sb), (Bi,Bi), (Ag,Bi), (Na,Na), (Na,Sb), (K,K), and (K,Sb) in PbTe as a function of the pair distance. The formation energies of the pairs at infinite pair distance are also given. These were obtained by adding up the formation energies of the isolated impurities. The pair binding energy $(E_b)$ is calculated as the difference between the formation energy at a given pair distance and that at infinite pair distance.

We find that different impurity atoms behave quite differently. Let us look at the case when both the impurities are same (homo pairs). The monovalent and trivalent pairs show qualitatively different behavior. The monovalent alkali impurities tend to repel weakly whereas two monovalent Ag atoms and the trivalent pairs (Sb,Sb) and (Bi,Bi) tend to attract. There is a strong repulsion between two alkali atoms when they flank a Te atom. On the other hand, two Ag atoms repel most when they are the fourth n.n. of each other.

The energy landscapes of (Sb,Sb) and (Bi,Bi) pairs are similar; see Figs. 1(b) and 1(e). Both Sb and Bi, however, show completely different behavior compared to the monovalent impurities. The most notable feature is a large drop in $E^f$ at the second n.n. distance. This

![](./images/867752270672954072_1.jpg)

FIG. 1: (Color online) Formation energies of various impurity pairs in PbTe as a function of the pair distance. The results were obtained in calculations using (2×2×2) supercells; SOI was not included (see the text). The values given with the arrows are the formation energies of the pairs at infinite pair distance (obtained by adding up the formation energies of the isolated impurities).

feature is also apparent for pairs made from one monovalent atom and one trivalent atom (hetero pairs), they all have a minimum in $E^f$ at the second n.n. distance; see Figs. 1(c), 1(f), 1(h), and 1(i). For (Ag,Sb) pair, $E^f$ for the first and the second n.n. distances are comparable, which is in agreement with the results reported by Hazama *et al.* [24] For all the hetero pairs we find the binding energy $E_b \sim$1.0 eV at the second n.n. distance.

For SnTe and GeTe, we have studied the impurity pairs made of monovalent Ag and/or trivalent Sb and Bi; see Figs. 2(a)–2(i). The formation energies of (Ag,Ag) in SnTe and GeTe do not change much as one varies the pair distance, although the Ag atoms in SnTe tend to repel each other or show a shallow minimum in GeTe. The (Sb,Sb) and (Bi,Bi) pairs in SnTe, on the other hand, have a large drop in $E^f$ at the second n.n. distance, similar to what has been observed in PbTe. The minimum of $E^f$ at the second n.n. distance for (Sb,Sb) in GeTe is much less pronounced. The formation energy of the (Bi,Bi) pair in GeTe, on the other hand, has a maximum at the second n.n. distance.

Although the energy landscape of different homo pairs in SnTe and GeTe can be very different, any combination of one monovalent and one trivalent impurity has the lowest $E^f$ at the second n.n. distance. This seems to be a robust characteristic of simultaneous doping

![](./images/867752270672954072_2.jpg)

FIG. 2: (Color online) Formation energy of various impurity pairs in SnTe and GeTe as a function of pair distance. The results were obtained in calculations using $(2×2×2)$ supercells; SOI was not included (see the text). The values given with the arrows are the formation energies of the pairs at infinite pair distance (obtained by adding up the formation energies of the isolated impurities).

of two impurities which are valence-compensated. The binding energy $E_b$ of the hetero pairs at the second n.n. distance in SnTe and GeTe is $\sim$0.5 eV, which is smaller than in PbTe. Quantitative differences in the energy landscape of different impurity pairs in different host materials may result in different nanostructuring patterns. Of course, synthesis conditions should also play an important role in the formation of the embedded nano-domains.

We note that the above results were obtained in calculations where SOI was not included. Although the inclusion of SOI is not likely to change the energy landscapes we have presented, it may change the magnitude of the formation energy in some cases. Besides, one should be aware that SOI makes the band gap problem in PbTe and SnTe more seri- ous by significantly reducing the gap and possibly causing an artificial overlap between the impurity-induced band and the valence band (see Sec. IV). As a result, the total energies obtained from the calculations may not be accurate.

In order to see how the energy landscape looks like in larger supercell sizes, we carried out calculations for (Ag,Sb) and (Sb,Sb) pairs in PbTe using $(3×3×3)$ supercells. Like in the case of $(2×2×2)$ supercells, we also find that both (Ag,Sb) and (Sb,Sb) have a minimum in $E^f$ at the second n.n. distance. For the (Ag,Sb) pair, $E^f$ at the second n.n. distance

is lower than that at the first, third, and fifth n.n. distances by 41, 95, and 91 meV/pair; these numbers are 40, 90, and 135 meV/pair in (2×2×2) supercells. For (Sb,Sb), $E^f$ at the second n.n. distance is lower than that at the first, third, and fifth n.n. distances by 215, 222, and 232 meV/pair; these numbers are 245, 274, 291 meV/pair in (2×2×2) supercells. This suggests that, as far as the energy landscape is concerned, (2×2×2) supercells give reliable results.

To summarize, formation energy calculations of impurity pairs show that many impurity atoms in PbTe, SnTe, and GeTe tend to come close to one another and form impurity-rich clusters. This observation is consistent with our previous study of the systems using an ionic model,[44] and with experiments where nanostructuring has been found in PbTe- and SnTe-based bulk thermoelectrics such as LAST-$m$, [11, 13, 14] $\mathrm{Ag_{1-x}Pb_m MTe_{m+2}}$ ($M$=Sb and Bi), [18] TAST-$m$, [16] SALT-$m$, [19] and PLAT-$m$. [20] For GeTe-based systems such as $(\mathrm{AgSbTe_2})_{1-x}(\mathrm{GeTe})_x$, in addition to the solid-solution-like distribution of impurities [45, 46] and microstructures (which were ascribed to twinning), [47] *in situ* formed inhomogeneities and nanoscale domains were also reported. [48] Our results are also in agreement with very recent first-principles studies for (Ag,Sb)-doped PbTe by *Ke et al.* [49] that show: (i) Ag and Sb prefer to form Ag-Te-Sb-Te units along the (010) direction of the PbTe matrix and (ii) these units tend to form a maximal number of Ag-Sb pairings.

## B. Local Relaxations Caused by Impurity Clustering

Local geometry in the neighborhood of an impurity pair can be strongly distorted from an average structure (as measured in a diffraction measurement) when the two atoms in a pair are made of one monovalent and one trivalent atom, especially when they are close to one another. Local relaxation effects are relatively small when the impurities are far away from each other. We observe that some Te atoms that are the neighbors of the ($M$,$M'$) pair in PbTe and, in some cases, the impurity atoms themselves go "off-center" (i.e., not on the regular lattice sites). This results in two or more $M$-Te and $M'$-Te bond lengths. The off-centering occurs when the two atoms in a pair are the first, second, and/or third n.n. of one another. In Table I, we list cases where bond lengths in a given pair configuration are different by $\gtrsim 0.2$ Å.

Figure 3 shows the relaxed structure of (Ag,Sb)-doped PbTe where the two impurity

TABLE I: Different bond lengths (in Å) observed in PbTe simultaneously doped with monovalent and trivalent atoms. The two atoms in a pair are either the first, second, or third n.n. of one another. Cases where bond lengths are different by $\sim$0.2 Å or more in a given configuration are listed. The results were obtained in calculations using (2$\times$2$\times$2) supercells. For reference, Pb-Te bond length in bulk PbTe is 3.275 Å.

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>1st n.n.</th>
      <th>2nd n.n.</th>
      <th>3rd n.n.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(Ag,Sb)</td>
      <td>Ag-Te</td>
      <td>3.07, 3.20, 3.31</td>
      <td>3.12, 3.41</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Sb-Te</td>
      <td>2.93, 3.19, 3.44</td>
      <td>-</td>
      <td>2.96, 3.18, 3.38</td>
    </tr>
    <tr>
      <td>(Ag,Bi)</td>
      <td>Ag-Te</td>
      <td>-</td>
      <td>3.14, 3.33</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Bi-Te</td>
      <td>3.09, 3.22, 3.33</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>(Na,Sb)</td>
      <td>Na-Te</td>
      <td>-</td>
      <td>3.26, 3.45</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Sb-Te</td>
      <td>2.93, 3.18, 3.42</td>
      <td>-</td>
      <td>2.96, 3.18, 3.37</td>
    </tr>
    <tr>
      <td>(K,Sb)</td>
      <td>K-Te</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>Sb-Te</td>
      <td>2.94, 3.18, 3.41</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

![](./images/867752270672954072_3.jpg)

FIG. 3: (Color online) Relaxed structure of (Ag,Sb)-doped PbTe where the two impurity atoms are the first nearest neighbors of one another in a (2$\times$2$\times$2) supercell. Large spheres are Ag (red) and Sb (blue), medium (gray) spheres Pb, and small (dark gray) spheres Te. The two Te atoms (marked by the arrows) in between Ag and Sb are shifted towards Sb by $\sim$0.2 Å, resulting in different Ag-Te and Sb-Te bond lengths; see Table I.

![](./images/867752270672954072_4.jpg)

FIG. 4: (Color online) Relaxed structure of (Ag,Sb)-doped PbTe where the two impurity atoms are the second nearest neighbors of one another in a (3×3×3) supercell. Large spheres are Ag (red) and Sb (blue), medium (gray) spheres Pb, and small (dark gray) spheres Te. The Te atom (marked by the arrow) in the Ag-Te-Sb chain is shifted towards Sb by $\sim$0.3 Å, resulting in different Ag-Te and Sb-Te bond lengths.

atoms are at the first n.n. distance in a (2×2×2) supercell. We find that the two Te atoms in between Ag and Sb are shifted towards Sb by $\sim$ 0.2 Å, resulting in three Ag-Te bond lengths and three Sb-Te bond lengths (see Table I).

In the configuration where the two impurity atoms are at the second n.n. distance in a (2×2×2) supercell, the Te atoms in the Ag-Te-Sb chain are slightly shifted toward Sb, resulting in two Ag-Te bond lengths (3.12 and 3.41 Å). Note that in this case, Ag and Sb form an infinite Ag-Te-Sb-Te chain. This imposes an artificial constraint on the relaxation of Ag, Sb, and their neighboring Te atoms, and the bond lengths may not be given accurately. Our calculations using larger supercells indeed show that there are stronger relaxations. In Fig. 4 we show the relaxed structure of (Ag,Sb)-doped PbTe where the two impurity atoms are at the second n.n. distance in a (3×3×3) supercell. The Te atom in between Ag and Sb is shifted towards Sb by $\sim$0.3 Å, resulting in three Ag-Te bond lengths (3.00, 3.10, and 3.74 Å) and three Sb-Te bond lengths (2.98, 3.15, and 3.33 Å).

Off-centering is also found with other impurity pairs and pair configurations in PbTe, SnTe, and GeTe. However, the bond length differences are usually smaller (<0.2 Å). These

small distortions may not be detected, for instance, in x-ray absorption fine structure (XAFS) analysis. [50] The changes in the local bond length results from a combination of (i) the difference in the atomic radii of the impurity and the host (Pb, Sn, or Ge) atoms which causes the relaxation of the neighboring Te atoms and (ii) the strong and directional interaction between the trivalent impurity $p$ states and Te $p$ states (see Sec. IV) which tends to pull Te atoms towards the trivalent impurity. These local distortions in the lattice geometry can potentially assist the formation of impurity-rich domains (e.g., Ag-Sb-rich nanoscale domains) in PbTe-, SnTe-, and GeTe-based systems. Besides, the off-centering observed in the systems is expected to have effects on their transport properties. The degree of off-centering may depend sensitively on the lattice constant (pressure).

Careful experimental studies are needed to confirm if there is off-centering and further experimental and theoretical studies are needed to understand the effects of off-centering on the transport properties of these systems.

## IV. IMPURITY-INDUCED BANDS

The electronic structure of a semiconductor can be strongly disturbed in the presence of impurities. In this section, we present our comprehensive first-principles studies of the band structures of PbTe, SnTe, and GeTe doped with monovalent (Ag, Na, and K) and trivalent (Sb and Bi) impurities and discuss how different impurity-related properties of these systems can be understood in terms of the calculated band structures. The investigations focus mainly on the highest valence band and/or the lowest conduction band induced by the impurities, hereafter called impurity-induced bands, since they are most relevant to understanding the transport properties of these PbTe-, SnTe-, and GeTe-based bulk thermoelectrics. In the limit of extreme dilution, these bands approach the host bands.

### A. PbTe

Before presenting the band structures of LAST-$m$ (PbTe doped with Ag and Sb) and other PbTe-based systems, let us summarize some of the important features of the band structure of undoped PbTe focusing on the highest valence band and the lowest conduction band. In PbTe, the valence $p$ states of Pb and Te play a dominant role in the formation of

the valence and conduction bands. These bands are predominantly bonding and antibonding states of Te $p$ and Pb $p$ states. The conduction- and valence-band edges are almost symmetric through the band gap and both the maximum and the minimum occur at the same point in the $\mathbf{k}$ space.

In the fcc BZ, the direct band gap is at the $L$ point and the valence-band maximum (VBM) and the conduction-band minimum (CBM) are nondegenerate (disregarding spin degeneracy). The four inequivalent $L$ points in the fcc BZ are mapped into the $\Gamma$ point in the simple cubic (sc) BZ of the (2×2×2) supercell. The band extrema are, therefore, fourfold degenerate at $\Gamma$; see Fig. 5(a). With spin, the CBM (VBM) at $\Gamma$ has eightfold degeneracy. The band gap of PbTe gets reduced significantly (from 0.816 eV to 0.105 eV) in the presence of SOI due to the large lowering in energy of the Pb $p$ bands (dominant near the conduction-band bottom) and a smaller change in the Te $p$ bands (dominant near the valence-band top). [38] In the following sections, we will discuss how the eightfold degeneracy of the CBM and VBM is lifted in the presence of an impurity and what are its implications on the transport properties.

### 1. Band structures of PbTe doped with Ag, Sb, and Bi

First, we consider the effects of each impurity on the band structure separately. Figures 5(b)–5(d) show the band structures of $M$Pb₃₁Te₃₂ for $M$=Ag, Sb, or Bi. The highest Ag-induced band [the dash-dotted curve in Fig. 5(b)] is the nearly flat band (along $\Gamma$-$X$-$M$-$\Gamma$) splitting off from the rest of the valence band. This impurity-induced band overlaps with the states near the valence-band top. An examination of the partial charge density associated with this band shows that it is predominantly Ag $d$ states hybridizing with Te $p$ states, see Fig. 6(a). This band, therefore, can be identified with the resonant state in the single-particle electronic DOS which has been discussed earlier. [25] The Fermi level lies below the VBM (by $\sim$40 meV) indicating that the system is hole-doped. Note that the Ag $s$ state is high up in the conduction band. The Ag impurity at this concentration ($\sim$3%) reduces the PbTe band gap from 105 meV to 73 meV. The conduction-band degeneracy (fourfold, without spin) is lifted near the CBM (at $\Gamma$) in the presence of the Ag impurity. However the lowest conduction band(s) are almost identical to that seen in pure PbTe.

The impurity-induced bands associated with Sb and Bi [the dash-dotted curves in

![](./images/867752270672954072_5.jpg)

FIG. 5: Band structures of undoped PbTe and PbTe doped with Ag, Sb, Bi, (Ag,Sb), and (Ag,Bi).
The impurity-induced bands are represented by the dash-dotted curves. The results were obtained
in calculations using the (2×2×2) cubic supercell with SOI included. The two impurity atoms in
a pair are either the second (2nd n.n.) or fifth (5th n.n.) nearest neighbors of one another. The
Fermi level (0 eV) is set to the highest occupied states or in the band gap.

Figs. 5(c) and 5(d)] arise from strong interaction between the impurity $p$ level (which lies
$\sim$0.6 eV above the CBM) and the conduction-band states. This results in the splitting of
the fourfold degenerate conduction band of PbTe [the lowest conduction band in Figs. 5(c)
and 5(d)]. The CBM of PbTe, which originally has eightfold degeneracy (including spin) at
$\Gamma$, now splits into a sixfold degenerate level (at $-0.11$ eV) and the twofold degenerate level
(at $-0.23$ eV) which belongs to the impurity-induced band. Partial charge density analysis
shows that the impurity-induced band associated with Sb is predominantly Sb $p$ hybridizing
with Pb $p$ and some contribution from Te $p$ states; see Fig. 6(b). Similar characteristics are
seen in the case of Bi.

For both Sb and Bi, the impurity-induced bands come down and close the band gap.
Since they have one more electron than Pb, the Fermi level lies in the conduction band and

![](./images/867752270672954072_6.jpg)

FIG. 6: (Color online) Band-decomposed charge densities associated with the impurity-induced bands in PbTe doped with (a) Ag and (b) Sb. These partial densities were calculated from a preconverged wavefunction file for the specified bands. Contributions from all 10 $\boldsymbol{k}$-points in the irreducible BZ were included. The Ag-induced band is predominantly Ag $d$ states hybridizing with Te $p$ states, whereas the Sb-induced one is Sb $p$ and Pb $p$ states with some contribution from Te $p$ states.

is above the CBM by $\sim$114 meV (Sb) or by $\sim$94 meV (Bi), which indicates that the systems are electron-doped. Although the Sb(Bi)-induced band is a result of the Sb(Bi) $p$ and Pb $p$ interaction, it is the highly directional interaction between the Sb(Bi) $p$ states and the Te $p$ states that drives the system towards metallicity, a phenomenon that has been observed in many chalcogenides. [51-54] The splitting between the impurity-induced band and the rest of the bands above it is affected by SOI and is, therefore, larger for Bi. This makes the Bi-induced band overlap with the VBM (of PbTe) near $\Gamma$, see Fig. 5(d). Both Sb and Bi leave the valence-band top almost unaffected except near the $\Gamma$ point.

As we mentioned in Sec. II, the band gap of PbTe is underestimated by $\sim$50% in DFT-GGA calculations. This means that the overlap between the Bi-induced band and the valence band as seen in Fig. 5(c) can be an artifact of DFT-GGA and that between the Sb-induced band and the valence band [Fig. 5(d)] there may be a finite energy gap. In addition, the curvature of the energy bands near the VBM and CBM might not be given correctly. In spite of these limitations, our first-principles calculations do show clear trends in the change of the electronic structure of PbTe when doped with different impurities whose concentration is of the order of a few percent. These findings can still be extremely useful

![](./images/867752270672954072_7.jpg)

FIG. 7: Band structures of PbTe doped with (a) Sb and (b) Bi obtained in calculations using (3×3×3) supercells with SOI included. The impurity-induced bands are represented by the dash-dotted curves. Note that the zero of the energy may not be given accurately because the calculations scanned only a very small part of the BZ.

in understanding the physical properties of these materials (as we will discuss below and in the next sections). Besides, it is not unreasonable to assume that the conduction band can be shifted rigidly when one makes corrections to the band gap. In that case, since Sb- and Bi-induced bands are derived from the lowest PbTe conduction-band states, they are expected to shift in the same direction with the conduction band, whereas the Ag-induced band, since it is split off from the valence-band top, is expected to go with the valence band.

To illustrate how the band structures change in going to lower impurity concentrations, we show in Figs. 7(a) and 7(b) the band structures of PbTe doped with Sb and Bi obtained in calculations using (3×3×3) supercells (the impurity concentration being ~1%). For this supercell, the band extrema occur at the $R$ point of the cubic BZ. We find that there are finite band gaps between the impurity-induced bands and the VBM; 60 meV (in the case of Sb) and 20 meV (Bi). Splittings near the conduction-band bottom are smaller compared to the (2×2×2) supercell (the impurity concentration being ~3%), because the effect of the impurity on the host PbTe becomes weaker in the larger supercell. For example, the splitting between the Sb-induced band and the rest of the conduction band is 118 meV in the (2×2×2) supercell, but only 52 meV in the (3×3×3) one; for Bi, the splitting goes, respectively, from 178 meV to 88 meV. Changing the impurity concentration, therefore, does not only change the band gap but also alters the arrangement of the energy bands near the

band gap region.

Our first-principles studies thus gives a physical picture of how different impurities affect the electronic structure of the host material. Clearly, a simple rigid band picture where one simply populates the host PbTe bands with electrons or holes is not appropriate for these PbTe-based systems, particularly for impurity concentrations >1 at%. From a materials design perspective, this opens up an opportunity to tune the band gap and band structure in the neighborhood of the band gap (hence transport properties) by choosing the type of impurity and its concentration. One can also combine different types of impurities to achieve the desired properties.

Note that, although the trivalent impurities tend to come close and form some sort of impurity-rich cluster (see our discussions in Sec. III), the average distance between impurities at the impurity concentration $\sim 1$ at% is relatively large and hence the direct impurity-impurity interaction is weak. Even in this case, our calculations using a periodic defect model (similar to virtual crystal model for a disordered system) shows that electronic states near the band extrema can be significantly perturbed [see Figs. 7(a) and 7(b)]. Fluctuations from this periodic impurity model will however affect the electronic states near the band extrema, sometimes localizing them near the defects if these fluctuations are strong enough. In this case a localized picture for the electronic states near the band extrema will be more meaningful. These states will not contribute much to transport. The states contributing to transport can be handled through a simple rigid band picture.

Experimentally, $\text{Pb}_{1-x}\text{Sb}_x\text{Te}$ ($x$=0.25, 0.50, and 1.00%) samples were reported to have $n$-type conductivity and degenerate doping. [55] In a supercell description, these concentrations correspond roughly to ($5{\times}5{\times}5$), ($4{\times}4{\times}4$), and ($3{\times}3{\times}3$) supercells, respectively. For the largest supercell ($x{\sim}0.25\%$), we expect the impurity-induced bands to approach the host PbTe bands and a simple carrier doping of the host bands by electrons is a reasonable picture. However, for the ($3{\times}3{\times}3$) supercell corresponding to $x{\sim}1.00\%$, the band structure near the band gap region gets modified and the simple carrier doping picture starts to break down. Transport measurements carried out on these samples showed that increasing the Sb content ($x$) resulted in an increase in the carrier concentration and decrease in the magnitude of thermopower. [55] This can be understood in terms of the calculated band structures presented above, where increasing the impurity (Sb) concentration results in a larger band splitting and smaller band gap. The electrical conductivity was also reported

to increase with increasing $x$ from 0.25 to 0.50%, which is consistent with the increase in the carrier concentration. It, however, decreases in going from $x$=0.50 to 1.00%; this was ascribed to scattering. [55]

### 2. Simultaneous doping with monovalent and trivalent impurities

Figures 5(e)–5(h) show the band structures of PbTe when simultaneously doped with Ag and Sb (or Bi). In our formation energy calculations (Sec. III) we find that indeed it is energetically favorable to dope PbTe simultaneously with monovalent (Ag, Na, and K) and trivalent (Sb and Bi) impurities. In these cases, we also identify impurity-induced bands. We observe bands which are split off from the valence-band top and the conduction- band bottom. The lowest conduction bands which were pushed down in the presence of the trivalent atoms are found to be pushed up in energy (with respect to the VBM) and the band gap opens up at the $\Gamma$ point (in the sc BZ) for certain pair configurations. The upward shift of the trivalent impurity-induced band is larger when the separation between the impurities is smaller, which can be seen more clearly in Figs. 5(f) and 5(h) for the case of (Ag,Bi).

The introduction of Ag (in the presence of Sb or Bi) to PbTe, therefore, has an effect opposite to that of Sb(Bi). Since the tendency to drive the system towards metallicity when only Sb and Bi are present depends on the interaction between Sb(Bi) $p$ and Te $p$ (which are hybridized with the neighboring Pb $p$), the addition of Ag stabilizes the hybridized Te $p$ states and pushes the Sb(Bi)-induced band back towards the other conduction bands. An examination of the partial charge densities associated with the Ag-induced band [the highest valence band in Fig. 5(e)] and the Sb-induced band [the lowest conduction band in Fig. 5(e)] in PbTe simultaneously doped with Ag and Sb shows that this is indeed the case. The contour plot shown in Fig. 8 clearly indicates that the hybridized $p$ states coming from the two Te atoms in the Ag-Te-Sb-Te chain are stabilized by Ag. This results in lowering the total energy of the system. The effect is strong for configurations with small pair distances and when the monovalent atom is in the direction of Sb(Bi) $p$-Te $p$ interaction, which is consistent with the energy landscapes for impurity pairs made of monovalent and trivalent atoms reported in Sec. III.

Band gaps (at $\Gamma$) in the case of (Ag,Sb) are 94.1, 78.2, 81.5, 83.3 meV when the two

![](./images/867752270672954072_8.jpg)

FIG. 8: (Color online) Band-decomposed charge density associated with the Sb-induced band in (Ag,Sb)-doped PbTe. This partial density was calculated from a preconverged wavefunction file for the specified band. Contributions from all 18 $\mathbf{k}$-points in the irreducible BZ were included. The Sb-induced band is predominantly Sb $p$ and Pb $p$ states with some contribution from the $p$ states of the Te atoms which are the nearest-neighbor atoms of Sb. The hybridized $p$ states coming from the two Te atoms in the Ag-Te-Sb-Te chain and part of Sb are stabilized by Ag.

atoms in the pair are at the first, second, third, and fifth n.n., respectively. For comparison, the calculated band gap for bulk PbTe is 105 meV. For (Ag,Bi), the gaps at $\Gamma$ are 43.4 and 0 meV for the second and fifth n.n. distances, respectively, and negative for other distances. Since the splitting of the conduction band is caused by the spin-orbit part of the impurity potential, this splitting is larger and hence the band gap is smaller (or even negative) in the (Ag,Bi) case because SOI is much stronger for Bi. Also DFT-GGA underestimates the band gap of pure PbTe, it is most likely that the actual gaps in the presence of (Ag,Sb) and (Ag,Bi) pairs should be larger than those given here.

Experimentally, diffuse reflectance measurements carried out on $\mathrm{Ag}_{1-x} \mathrm{Pb}_{18} M \mathrm{Te}_{20}$ ($M$=Bi and Sb) samples give an apparent gap of 0.25 eV for $M$=Bi and 0.28 eV for $M$=Sb; [18] both for $x$=0. The difference of $\sim$30 meV in the band gap is consistent with the above calculated values when the two atoms in a pair are at the second n.n. distance; 43.4 meV for (Ag,Bi) and 78.2 meV for (Ag,Sb). If the conduction-band states are shifted rigidly upward in energy by $\sim$0.2 eV (to correct for DFT-GGA), then there appear to be a good agreement between experiment and our theoretical calculations.

In the current model $(MM'Pb_{30}Te_{32})$, the impurity concentration is $\sim 3\%$, whereas in experiments, typically it is $\sim 5\%$. [11, 18] One, therefore, should expect that a monovalent atom (Ag) can easily find itself close enough to a trivalent atom (Sb or Bi) to have an impact on the latter. In addition, our first-principles study of the energetics of different pairs of impurities (see Sec. III) also shows that an impurity pair made of a monovalent atom and a trivalent atom is most stable when the two atoms are the second n.n. of one another. There is, however, still a finite chance for an impurity atom to be isolated or closer to another atom of the same kind, depending on the actual distribution of the impurity atoms in the samples and the ratio between the monovalent and trivalent atoms. This suggests that one can tune the band structure (hence transport properties) of the doped PbTe systems by tuning the Ag/Sb(Bi) ratio.

### 3. Tuning the transport properties via the Ag/Sb(Bi) ratio
Transport properties measurements carried out on $n$-type $Ag_{1-x}Pb_{18}SbTe_{20}$ ($x$=0, 0.14, and 0.30) by Han *et al.* [18] showed that the electrical conductivity increases and the absolute value of the thermopower decreases with decreasing Ag concentration (i.e., with increasing $x$) at a given temperature. The experimental data clearly indicate that the transport properties of the system depend on the Ag/Sb ratio. The magnitude of thermopower is largest and the electrical conductivity is smallest when Sb/Ag=1. We now discuss how these data can be understood in terms of the calculated band structures.

Let us look at the physics of the above situation using our band structure calculations. The stoichiometric compound ($x$=0) is charge-compensated and should be a semiconductor. The electron doping in this case comes most likely from intrinsic defects like Te vacancies. Concentration of such native defects is however small ($\sim$parts/million). Although Te vacancies do perturb the conduction-band bottom significantly, [53] in this very dilute limit we do not expect a significant change in the band structure of PbTe. The concentrations of Ag and Sb are, on the other hand, sufficiently large such that changing the Ag/Sb ratio not only changes the electrons donated to the network but, more significantly, changes the band structure near the band gap. The observed behavior of the electrical conductivity and thermopower can be understood as follows: Increasing the Ag content increases the number of (Ag,Sb) pairs with short pair distances and reduces the number of isolated Sb impurities.


![](./images/867752270672954072_9.jpg)

FIG. 9: (Color online) Band structures of PbTe doped with (Ag,Sb) and (Ag,Bi) impurity pairs showing the differences in the band gap and in the arrangement of the energy bands near the $\Gamma$ point. The impurity-induced bands are represented by the dash-dotted curves. The Fermi level (0 eV) is set to the highest occupied states or in the band gap.

This results in the widening of the band gap and reduction in the active carrier concentra- tion, which leads to a decrease in the electrical conductivity and increase in the magnitude of thermopower.

The $Ag_{1-x}Pb_{18}BiTe_{20}$ system was also reported to produce similar behavior. [18] The dependence of electrical conductivity and thermopower on $x$ is, however, weaker in the Bi analog. The difference between (Ag,Sb) and (Ag,Bi) in PbTe-based thermoelectrics will be discussed in more detail in the next section. Studies of Zhu *et al.* [56] on quenched $AgPb_{18}Sb_{1-y}Te_{20}$ ($y$=0.0, 0.1, 0.3, and 0.5) samples also showed that increasing the Sb content (i.e., with decreasing $y$) results in reduced electrical conductivity and increase in thermopower. Again, the magnitude of thermopower is largest and the electrical conduc- tivity is smallest when Sb/Ag=1. In this case, the increase of the Sb/Ag ratio (up to 1) increases the probability of having (Ag,Sb) impurity pairs with the Ag and Sb atoms being close to one another and reduces the number of isolated Sb impurities.

### 4. Why the Bi analog of LAST-m is an inferior thermoelectric?

In order to understand the difference between the two systems, (Ag,Sb)- and (Ag,Bi)- doped PbTe, we show in Figs. 9(a)-9(d) the blow ups of the band structures near the band

gap at the $\Gamma$ point. Since LAST-$m$ and its Bi analog are $n$-type thermoelectrics (obtained by suitable adjustments of Ag concentration and the presence of unknown intrinsic defects, probably anion vacancies), [11, 18] we focus on the region near the conduction-band bottom.

In addition to the difference in the band gap between these two systems, there are other differences in the ordering of the energy bands and their multiplicity. For (Ag,Sb) at the second n.n. distance, there is a group of three bands (each band is a doublet when spin is included) which are close in energy at the $\Gamma$ point, see Fig. 9(a); $\sim$42 meV above the highest band in this group is another band (which is also a doublet). The splitting of the bands is much smaller for (Ag,Sb) at the fifth n.n. distance, see Fig. 9(c). The arrangement of the bands in the (Ag,Bi) case is, however, in the reverse order; the doublet is below the sextet by $\sim$37 meV and the band splittings are larger, see Figs. 9(b) and 9(d). This means that, for the same carrier (electron) concentration, the chemical potential in the (Ag,Sb) case is lower (closer to the CBM) than in the (Ag,Bi) case. This and the larger band gap for (Ag,Sb) which helps reduce the contribution from the minority carriers (holes) will result in a larger thermopower (magnitude) for (Ag,Sb)-doped PbTe.

Experimentally, transport properties measurements of $\text{Ag}_{1-x}\text{Pb}_{18}M\text{Te}_{20}$ ($M$=Bi and Sb) showed that thermopower decreases dramatically when Sb is replaced by Bi; from $-100$ $\mu$V/K at 300 K and $-250$ $\mu$V/K at 700 K for $M$=Sb to $-40$ $\mu$V/K at 300 K and $-160$ $\mu$V/K at 600 K for $M$=Bi. [18] The lattice thermal conductivity of the Bi analog is, however, larger than that of Sb because of the smaller mass fluctuation in this system (Bi and Pb are comparable, whereas Sb is much lighter than Pb). This higher thermal conductivity, coupled with the lower values of the thermopower, results in much lower $ZT$ in $\text{Ag}_{1-x}\text{Pb}_{18}\text{BiTe}_{20}$, $ZT$=0.44 at 665 K ($x$=0.3), compared to $ZT$$\sim$1.0 at 650 K for its Sb analog. [18]

Finally, looking at the calculated band structures presented in Figs. 5(e)$-$5(h), we expect that $p$-type LAST-$m$, if it can be successfully synthesized, will give a large thermopower. As far as the band structure is concerned, the thermopower can be even larger for the $p$-type system than the $n$-type one because the energy bands near the VBM (which are predominantly the hybridized states of Ag $d$ and Te $p$) are flatter than those near the CBM. Likewise, the $p$-type Bi analog may give larger thermopower than the $n$-type one.

![](./images/867752270672954072_10.jpg)

FIG. 10: Band structures of undoped PbTe and PbTe doped with Na, K, Sb, (Na,Sb), and (K,Sb).
The impurity-induced bands are represented by the dash-dotted curves. The results were obtained
in calculations using the (2×2×2) supercell with SOI included. The two impurity atoms in a pair
are either the second (2nd n.n.) or fifth (5th n.n.) nearest neighbors of one another. The Fermi
level (0 eV) is set to the highest occupied states or in the band gap.

### 5. Why Na and K are good substitutes for Ag?

The substitution of Ag in LAST-$m$ by Na or K have shown that these Ag-free thermo-
electrics are also very promising. [19, 20] The $p$-type $\mathrm{Na}_{1-x}\mathrm{Pb}_{m}\mathrm{Sb}_{y}\mathrm{Te}_{m+2}$ gives $ZT$~1.7 at
650 K for $m$=20, $x$=0.05, and $y$=1, [19] whereas the $n$-type $\mathrm{K}_{1-x}\mathrm{Pb}_{m+\delta}\mathrm{Sb}_{1+\gamma}\mathrm{Te}_{m+2}$ gives
$ZT$~1.6 at 750 K for $m$=20, $x$=0.05, $\delta$=0, and $\gamma$=0.2. [20] These systems are good ther-
moelectrics because of their large thermopower and low thermal conductivity. The latter
is believed to be due to the nanostructuring observed in the systems, [19, 20] which is also
consistent with the our energetic studies presented in Sec. III. In order to understand the
large thermopower values observed experimentally, we have analyzed the electronic struc-
tures of PbTe doped with Na, K, (Na,Sb), and (K,Sb). The calculated band structures are
presented in Figs. 10(a)–10(h).


Let us first examine the band structure for a single Na or K substituting for a Pb in a (2×2×2) cubic supercell model. Although thought to be ideal acceptors, [25] Na and K indeed produce significant changes in the band structure of PbTe, with band splittings near the valence-band top and conduction-band bottom, see Figs. 10(b) and 10(c). The VBM (CBM) of PbTe, which originally has eightfold degeneracy, now splits into a group of three nearly degenerate bands and a stand alone band (a doublet) at the $\Gamma$ point. The band nominally associated with Na (or K) [the dash-dotted bands in Figs. 10(b) and 10(c)], in fact, does not have any Na (K) character since the Na (K) $s$ level is high up in the conduction band. It is, however, formed primarily out of $p$-orbitals associated with Te atoms which are the n.n. of the Na (K) atom. This band will still be called the "impurity-induced band" since it is induced by Na(K) and split off from the top-most valence band and the rest of the PbTe valence bands.

The band structure for Sb-doped PbTe has already been discussed but is given in Fig. 10(d) for comparison. Simultaneous doping with Sb and Na (or K) helps push the Sb-induced bands upwards in energy, resulting in a band gap at $\Gamma$. Na (K) acts just like Ag in this regard, i.e, stabilizing the hybridized Te $p$ states resulting from the interaction between Sb $p$ and Te $p$. The Sb-induced band is, however, pushed to higher energy in the case of Na (and K), compared to Ag; and the new band gap can be even be larger than that of the undoped PbTe; 114 meV and 112 meV for the (Na,Sb) and 100 meV and 122 meV for the (K,Sb) pair at the second and the fifth n.n. distances, respectively, as compared to 105 meV for the undoped PbTe. This is qualitatively consistent with experiment where $\text{K}_{1-x}\text{Pb}_{m+\delta}\text{Sb}_{1+\gamma}\text{Te}_{m+2}$ ($m$=19, 20, and 21) was found to have ($\sim$0.03 eV) larger band gap than pure PbTe. [20] This suggests that Na and K, which are more ionic than Ag, compensate almost completely the charge perturbation created by Sb. In addition, K and Sb atoms may come close and locally form $\text{KSbTe}_2$ (whose band gap is $\sim$0.55 eV),[20] which may explain the increased band gap of $\text{K}_{1-x}\text{Pb}_{m+\delta}\text{Sb}_{1+\gamma}\text{Te}_{m+2}$.

There are other differences in the band structures of PbTe doped with Na, K, and Ag. The splitting between the threefold nearly degenerate band and the nondegenerate band near the conduction-band bottom at the $\Gamma$ point increases in going from Ag [Figs. 9(a) and 9(c)] to Na [Figs. 11(a) and 11(c)] to K [Figs. 11(b) and 11(d)]; see also Table II. The trend in the splitting near the conduction-band bottom reflects the positions of the $s$ level of Ag, Na, and K given by the Harrison's table; which are respectively at $-5.99$ eV (Ag), $-4.96$ eV

![](./images/867752270672954072_11.jpg)

FIG. 11: (Color online) Band structures of PbTe doped with (Na,Sb) and (K,Bi) impurity pairs showing the arrangement of the energy bands near the $\Gamma$ point. The impurity-induced bands are represented by the dash-dotted curves. The Fermi level (0 eV) is in the band gap.

TABLE II: The splitting (in meV) between the group of three nearly degenerate bands and the single band at the conduction-band minimum (CBM) and valence-band maximum (VBM) (at the $\Gamma$ point in the simple cubic BZ) of PbTe simultaneously doped with Sb and either Ag, Na, or K. The two atoms in a pair are either the second or fifth n.n. of one another. The results were obtained in calculations using the $(2{\times}2{\times}2)$ supercell with SOI included.

<table>
<thead>
  <tr>
    <th></th>
    <th colspan="2">(Ag,Sb)</th>
    <th colspan="2">(Na,Sb)</th>
    <th colspan="2">(K,Sb)</th>
  </tr>
  <tr>
    <th></th>
    <th>2nd n.n.</th>
    <th>5th n.n.</th>
    <th>2nd n.n.</th>
    <th>5th n.n.</th>
    <th>2nd n.n.</th>
    <th>5th n.n.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CBM</td>
    <td>42</td>
    <td>0</td>
    <td>96</td>
    <td>58</td>
    <td>157</td>
    <td>112</td>
  </tr>
  <tr>
    <td>VBM</td>
    <td>167</td>
    <td>160</td>
    <td>165</td>
    <td>166</td>
    <td>132</td>
    <td>136</td>
  </tr>
</tbody>
</table>

(Na), and $-4.01$ eV (K). [57] The trend in the splitting near the valence-band top is probably due the difference in the dopants (Ag, Na, and K) and the host (Pb) potentials. Since the difference in the splitting between Ag, Na, and K is small near the valence-band top and large near the conduction-band bottom, one expects that the difference in the thermopower (at a given carrier concentration) is small for $p$-type systems but larger for the $n$-type ones.

Experimentally, $\text{Na}_{0.8}\text{Pb}_{20}\text{Sb}_{y}\text{Te}_{22}$ compositions with $y{=}0.4$, 0.6, and 0.8 was found to have the ($p$-type) electrical conductivity decrease and thermopower increase as one increases

![](./images/867752270672954072_12.jpg)

FIG. 12: Band structures of undoped GeTe and GeTe doped with Ag, Sb, Bi, (Ag,Sb), and (Ag,Bi). The impurity-induced bands are represented by the dash-dotted curves. The results were obtained in calculations using the (2×2×2) supercell with SOI included. The two impurity atoms in a pair are either the second (2nd n.n.) or fifth (5th n.n.) nearest neighbors of one another. The Fermi level (0 eV) is set to the highest occupied states or in the band gap.

pushed down (by $\sim$0.096 eV) in energy. We note that the lattice distortion is not present in our current calculations. It is most likely that if we take into account the effects of lattice distortion the calculated band gap will be smaller than that of experiment, consistent with the known limitations of DFT-GGA.

The introduction of Ag into GeTe (Ag substitutes for Ge) results in a $p$-type system with the Fermi level below the VBM. Ag-induced band is the one that splits off from the valence-band top (of GeTe), presented by the dash-dotted curve in Fig. 12(b). Sb and Bi, on the other hand, make GeTe $n$-type. Impurity-induced bands associated with Sb and Bi which are split off from the GeTe conduction-band bottom significantly reduce the band gap (in the case of Sb) or even close the gap (Bi), see Figs. 12(c) and 12(d). These observations are similar to what was seen for Ag, Sb, and Bi in PbTe, except that band crossing is less

severe for GeTe because it has a larger band gap.

Simultaneous doping of Ag and Sb (or Bi) also helps lift the impurity-induced band associated with Sb (or Bi) up in energy and increases (or even opens up) the gap, see Figs. 12(e)-12(h); again similar to what was seen in PbTe [Figs. 5(e)-5(h)]. The arrangement of the energy bands near the CBM of (Ag,Sb) doped GeTe is, however, in the reverse order compared to that in PbTe. The nondegenerate (disregarding spins) band is now at a lower energy than the nearly threefold degenerate band. This is because the nondegenerate band is spin-orbit-induced and the effects is much larger for Sb and Bi than for Ge.

Although (Ag,Sb)- and (Ag,Bi)-doped GeTe have the same band arrangements near the CBM, the splitting between the threefold degenerate band and the nondegenerate impurity-induced band is smaller in the (Ag,Sb)-doped system; 82.8 meV and 143.8 meV at the second and fifth n.n. distances, respectively, compared to 194.9 meV and 219.4 meV in the (Ag,Bi)-doped system. For $n$-type thermoelectrics, contribution to the transport properties largely comes from the lowest conduction bands. The (Ag,Sb)-doped system is, therefore, expected to give higher thermopower compared to the (Ag,Bi)-doped one, as far as the band structures are concerned, because the former has a larger band gap.

The arrangement of the energy bands near the conduction-band bottom is expected not to affect the $p$-type system much. However, the larger band gap should also result in larger thermopower in the (Ag,Sb)-doped case, compared to the (Ag,Bi); again, due to reduced intrinsic contributions in the (Ag,Sb)-doped system. The system with Bi, on the other hand, has lower lattice thermal conductivity because of the larger mass difference between Bi and Ge. Taking into account these different factors, one might expect that the $p$-type TAGS system and its Bi analog, if made under the same synthesis conditions, have comparable $ZT$ values.

### C. SnTe

Besides the PbTe- and GeTe-based systems, complex quaternary systems based on SnTe have also shown to be promising for thermoelectric applications. Androulakis *et al.* [16] have reported an unusual coexistence of large thermopower and degenerate doping in the nanostructured material $\text{Ag}_{1-x}\text{SnSb}_{1+x}\text{Te}_{3}$ ($x$=0.15). This system shows a positive thermopower of $\sim$160 $\mu$V/K at 600 K and an almost metallic carrier concentration of $\sim$5$\times$10$^{21}$ cm$^{-3}$. In

![](./images/867752270672954072_13.jpg)

FIG. 13: Band structures of undoped SnTe and SnTe doped with Ag, Sb, (Ag,Sb), and (Ag,Bi). The impurity-induced bands are represented by the dash-dotted curves. The results were obtained in calculations using the (2×2×2) supercell with SOI included. The two impurity atoms in a pair are either the second (2nd n.n.) or fifth (5th n.n.) nearest neighbors of one another. The Fermi level (at 0 eV) is set to the highest occupied states or in the band gap.

order to fully understand the role Ag and Sb play in these and other SnTe-based systems, especially those at low impurity concentration (lightly doped) limit ($\sim$3%), band structure calculations were also carried out where Ag and Sb were treated as defects in SnTe.

It is well known that the electronic structure of SnTe is anomalous compared to that of PbTe. [60] The main differences between these two systems are: (i) SnTe has a direct gap which is slightly away from the $L$ point (along $L$-$W$) of the fcc BZ if SOI is included, but is a zero-gap semiconductor if SOI is excluded; whereas PbTe has a direct gap at the $L$ point even in the absence of SOI. (ii) The symmetry of the band-edge states at and near the $L$ point changes in going from PbTe to SnTe, resulting in the so-called "band inversion" phenomenon in SnTe. [60-62] Figure 13(a) shows the band structure of undoped SnTe along high symmetry directions of the sc BZ, obtained in calculations using the (2×2×2) supercell. In the sc BZ, the band gap of SnTe occurs near the $\Gamma$ point. The $\Gamma$ point is actually a saddle

point, although the feature is not so evident from Fig. 13(a) where the band structure is plotted only along $\Gamma$-$R$ and $\Gamma$-$X$. The calculated band gap at $\Gamma$ is $\sim$0 eV (without SOI) and 0.105 eV (with SOI). Experimentally, SnTe was reported to have a band gap of 0.3 eV at 0 K. [63]

The band structure of SnTe doped with Ag is shown in Fig. 13(b). The impurity-induced band associated with Ag [the dashed-dotted curve in Fig. 13(b)] is predominantly Ag $d$ and Te $p$ states, splitting off from the valence-band top. The impurity-induced band associated with Sb [the dash-dotted curve in Fig. 13(c)], on the other hand, splits off from the conduction-band bottom and is predominantly Sb $p$ and Sn $p$ with some contribution from the hybridized $p$ states of the n.n. Te atoms of Sb. This hybridized impurity-induced band comes down and closes the gap. These observations are similar to those in PbTe and GeTe containing Ag and Sb. There are, however, noticeable differences near the conduction-band bottom. The saddle-point feature of $\Gamma$ is more pronounced (compared to undoped SnTe) along the $\Gamma$-$R$ and $\Gamma$-$X$ directions. The separation between the maximum at $\Gamma$ and the VBM is $\sim$3 meV for SnTe doped with Ag.

The electronic structure in the case of simultaneous doping is also different from what has been observed in PbTe and GeTe. The introduction of Ag does lift the Sb- and Bi-induced bands up in energy, but not the part near the $\Gamma$ point; see Figs. 13(e)-13(h). It, actually, seems to pull the impurity-induced bands near the $\Gamma$ point further down in energy resulting in a larger overlap with the valence band. Based on the calculated band structures, one expects to see the (Ag,Sb)-doped SnTe systems to exhibit highly degenerate semiconducting or even metallic conduction. However, large thermopower for the $p$-type SnTe-based systems is also possible because of the high degeneracy of the bands near the VBM. This is consistent with the observation of large thermopower and high carrier concentration in experiment. [16]
We note that the overlap between the impurity-induced bands and the valence band in these SnTe-based systems can be smaller or the systems may actually have small but finite gaps if one makes corrections to DFT-GGA calculations.

## V. SUMMARY

In summary, the energetics of impurity clustering and the impurity-induced bands as- sociated with various monovalent (Na, K, and Ag) and trivalent (Sb and Bi) impurities in

32

PbTe, SnTe, and GeTe were studied using first-principles calculations and supercell models. Our results showed that the impurity pairs formed out of monovalent and trivalent atoms in PbTe, SnTe, and GeTe have the lowest energy when they are the second nearest neighbors of one another. The Te atoms near an impurity pair (and some impurity atoms themselves) tend to go "off-center," mainly because of the strong and directional interaction between the $p$ states of the trivalent impurity cations (Sb and Bi) and the divalent anion (Te). One should carry out experimental studies to see if there is indeed off-centering in the real samples and how it impacts the transport properties of these systems.

The electronic structures of PbTe, SnTe, and GeTe are strongly perturbed by the impurities (in the concentration range $>1\%$) and the degree of perturbation depends on the relative separation between the impurities. Band degeneracy at the VBM and CBM of the host materials is removed and there are band splittings in the presence of an impurity. We found that the impurity-induced bands associated with the monovalent impurities (Na, K, and Ag) split off from the valence-band top but overlap with the other valence bands near the VBM. All these bands, however, constitute the valence band and the systems are hole-doped. The impurity-induced bands associated with the trivalent impurities (Sb and Bi), on the other hand, split off from the conduction-band bottom with large shifts towards the valence band. These bands reduce or even close the band gap. This is due to the strong interaction between the $p$ states of the trivalent impurity cation (Sb and Bi) and the divalent anion (Te) which tends to introduce electronic states in the band gap region and drive the systems towards metallicity.

The simultaneous doping of monovalent and trivalent impurities, however, pushes the impurity-induced band associated with the trivalent impurity to higher energies and the band gap increases or opens up, except for the SnTe-based systems. One, therefore, can tune the monovalent/trivalent ratio to tune the band gap and the band structure near the band edges in PbTe and GeTe-based systems. SnTe behaves rather anomalously in the sense that the introduction of the monovalent impurity does not lift the trivalent impurity-induced band near the CBM up in energy but slightly pulls it further down towards the valence band. Based on the calculated band structures, we have been able to explain qualitatively the observed transport properties of the whole class of PbTe-, SnTe-, and GeTe-based bulk thermoelectrics.

In spite of the known limitations of DFT-GGA and supercell methods, [37] our first-

principles studies thus provide a clear physical picture of how different impurities affect the lattice geometry and electronic structure of the host materials. These results provide a qualitative understanding of the atomic and transport properties of complex multicomponent PbTe-, SnTe-, and GeTe-based thermoelectrics. The approach described here however is not limited to these systems but can be extended to other classes of materials. The "band-gap problem" can, in principle, be addressed by using more advanced methods which go beyond DFT-GGA. [39-41] These calculations for our systems are currently too demanding computationally; however, they are very desirable since having accurate electronic structures of the materials is an important step towards a quantitative understanding of their transport properties.

### Acknowledgments

This work was partially supported by the U.S. Office of Naval Research and made use of the computing facilities of Michigan State University High Performance Computing Center.

[1] Committee on CMMP 2010, National Research Council, *Condensed-Matter and Materials Physics: The Science of the World Around Us* (The National Academies Press, Washington D.C., 2007).

[2] J. R. Sootsman, D.-Y. Chung, and M. G. Kanatzidis, Angew. Chem. Int. Ed. **48**, 8616 (2009).

[3] G. S. Nolas, J. Poon, and M. Kanatzidis, MRS Bull. **31**, 199 (2006).

[4] J. Hafner, C. Wolverton, and G. Ceder, MRS Bull. **31**, 659 (2006).

[5] G. D. Mahan and J. O. Sofo, Proc. Natl. Acad. Sci. U.S.A. **93**, 7436 (1996).

[6] G. D. Mahan, Solid State Physics **51**, 81 (1998).

[7] Y. Gelbstein, Z. Dashevsky, and M. P. Dariel, Physica B **363**, 196 (2005).

[8] J. P. Heremans, Vla. Jovovic, E. S. Toberer, A. Saramat, K. Kurosaki, A. Charoenphakdee, S. Yamanaka, and G. J. Snyder, Science **321**, 554 (2008).

[9] K. Takahata and I. Terasaki, Jpn. J. Appl. Phys. **41**, 763 (2002).

[10] G. S. Nolas, D. T. Morelli, and T. M. Tritt, Ann. Rev. Mater. Sci. **29**, 89 (1999).

[11] K.-F. Hsu, S. Loo, F. Guo, W. Chen, J. S. Dyck, C. Uher, T. Hogan, E. K. Polychroniadis,

and M. G. Kanatzidis, Science **303**, 818 (2004).

[12] J.-S. Rhyee, K. H. Lee, S. M. Lee, E. Cho, S. I. Kim, E. Lee, Y. S. Kwon, J. H. Shim, and G. Kotliar, Nature **459**, 965 (2009).

[13] E. Quarez, K.-F. Hsu, R. Pcionek, N. Frangis, E. K. Polychroniadis, and M. G. Kanatzidis, J. Am. Chem. Soc. **127**, 9177 (2005).

[14] L. Wu, J.-C. Zheng, J. Zhou, Q. Li, J. Yang, and Y. Zhu, J. Appl. Phys. **105**, 094317 (2009)

[15] J. Androulakis, K. F. Hsu, R. Pcionek, H. Kong, C. Uher, J. J. D'Angelo, A. Downey, T. Hogan, and M. G. Kanatzidis, Adv. Mater. **18**, 1170 (2006).

[16] J. Androulakis, R. Pcionek, E. Quarez, J.-H. Do, H. Kong, O. Palchik, C. Uher, J. J. D'Angelo, J. Short, T. Hogan, and M. G. Kanatzidis, Chem. Mater. **18**, 4719 (2006).

[17] J. Androulakis, C. Lin, H. Kong, C. Uher, C. Wu, T. Hogan, B. A. Cook, T. Caillat, K. M. Paraskevopoulos, and M. G. Kanatzidis, J. Am. Chem. Soc. **129**, 9780 (2007).

[18] M.-K. Han, K. Hoang, H. Kong, R. Pcionek, C. Uher, K. M. Paraskevopoulos, S. D. Mahanti, and M. G. Kanatzidis, Chem. Mater. **20**, 3512 (2008).

[19] P. F. P. Poudeu, J. D'Angelo, A. D. Downey, J. L. Short, T. P. Hogan, and M. G. Kanatzidis, Angew. Chem. Int. Ed. **45**, 3835 (2006).

[20] P. F. P. Poudeu, A. Guéguen, C.-I. Wu, T. Hogan, and M. G. Kanatzidis, Chem. Mater. (in press, 2009). (DOI: 10.1021/cm902001c).

[21] S. D. Mahanti and D. Bilc, J. Phys.: Condens. Matter. **16**, S5277 (2004).

[22] D. Bilc, S. D. Mahanti, K.-F. Hsu, E. Quarez, R. Pcionek, and M. G. Kanatzidis, Phys. Rev. Lett. **93**, 146403 (2004).

[23] S. Ahmad, K. Hoang, and S. D. Mahanti, Phys. Rev. Lett. **96**, 056403 (2006).

[24] H. Hazama, U. Mizutani, and R. Asahi, Phys. Rev. B **73**, 115108 (2006)

[25] S. Ahmad, S. D. Mahanti, K. Hoang, and M. G. Kanatzidis, Phys. Rev. B **74**, 155205 (2006).

[26] I. Hase and T. Yanagisawa, Physica C **445-448**, 61 (2006).

[27] K. Hoang, S. D. Mahanti, and P. Jena, Phys. Rev. B **76**, 115432 (2007).

[28] S. D. Mahanti, K. Hoang, and S. Ahmad, Physica B **401-402C**, 291 (2007.

[29] O. Madelung, *Semiconductors: Data Handbook*, 3rd ed. (Springer, Berlin, 2004).

[30] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

[31] P. E. Blöchl, Phys. Rev. B **50**, 17953 (1994).

[32] G. Kresse and D. Joubert, Phys. Rev. B **59**, 1758 (1999).

35

[33] G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).

[34] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[35] G. Kresse and J. Furthmüller, Comput. Mat. Sci. 6, 15 (1996).

[36] H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).

[37] R. M. Nieminen, in Theory of Defects in Semiconductors, edited by D. A. Drabold and S. Estreicher (Springer, Berlin, 2007).

[38] K. Hoang and S. D. Mahanti, Phys. Rev. B 78, 085111 (2008).

[39] D. M. Bylander and L. Kleinman, Phys. Rev. B 41, 7868 (1990).

[40] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).

[41] W. G. Aulber, L. Jonsson, and J. W. Wilkins, Solid State Physics 54, 1 (2000).

[42] We note that, even within DFT-GGA, our calculations have already required an excessive amount of computer memory and processing time. A typical calculation (with spin-orbit interaction included) requires from several gigabytes of memory for the $(2×2×2)$ supercell to several tens of gigabytes of memory for the $(3×3×3)$ one. It takes about one week on a SGI Altix 3700 Bx2 machine to finish a self-consistent run that generates charge density, e.g., for Sb-doped PbTe using the $(3×3×3)$ supercell.

[43] C. G. Van de Walle and J. Neugebauer, J. Appl. Phys. 95, 3851 (2004).

[44] K. Hoang, K. Desai, and S. D. Mahanti, Phys. Rev. B 72, 064102 (2005).

[45] C. Wood, Rep. Prog. Phys. 51, 459 (1988).

[46] S. K. Plachkova and I. A. Avramova, phys. stat. sol. (a) 184, 195 (2001).

[47] B. A. Cook, X. Wei, J. L. Harringa, and M. J. Kramer, J. Mater. Sci. 42, 7643 (2007).

[48] S. H. Yang, T. J. Zhu, T. Sun, J. He, S. N. Zhang, and X. B. Zhao, Nanotechnology 19, 245707 (2008).

[49] X. Ke, C. Chen, J. Yang, L. Wu, J. Zhou, Y. Zhu, and P. R. C. Kent, Phys. Rev. Lett. 103, 145502 (2009).

[50] J. J. Rehr and R. C. Albers, Rev. Mod. Phys. 72, 621 (2000).

[51] K. Hoang, J. R. Salvador, S. D. Mahanti, and M. G. Kanatzidis, Phys. Rev. Lett. 99, 156403 (2007).

[52] K. Hoang and S. D. Mahanti, Phys. Rev. B 77, 205107 (2008).

[53] K. Hoang, Atomic and electronic structure of novel ternary and quaternary narrow band-gap semiconductors, Ph.D. Thesis (Michigan State University, 2007).

[54] K. Hoang, A. Tomic, S. D. Mahanti, T. Kyratsi, D.-Y. Chung, S. H. Tessmer, and M. G. Kanatzidis, Phys. Rev. B 80, 125112 (2009).

[55] C. M. Jaworski, J. Tobola, E. M. Levin, K. Schmidt-Rohr, and J. P. Heremans, Phys. Rev. B 80, 125208 (2009).

[56] T. J. Zhu, F. Fan, S. N. Zhang, and X. B. Zhao, J. Phys. D: Appl. Phys. 40, 3537 (2007).

[57] W. A. Harrison, *Elementary Electronic Stucture* (World Scientific, Singapore, 2004).

[58] J. R. Salvador, J. Yang, X. Shi, H. Wang, A. A. Wereszczak, J. Solid State Chem. 182, 2088 (2009).

[59] L. L. Chang, P. J. Stiles, and L. Esaki, IBM J. Res. Develop. 10, 484 (1966).

[60] Y. W. Tung and M. L. Cohen, Phys. Rev. 180, 823 (1969).

[61] Y. W. Tsang and M. L. Cohen, Phys. Rev. B 3, 1254 (1971).

[62] N. S. Dantas, A. F. da Silva, and C. Persson, Optical Materials 30, 1451 (2008).

[63] L. Esaki and P. J. Stilles, Phys. Rev. Lett. 16, 1108 (1966).