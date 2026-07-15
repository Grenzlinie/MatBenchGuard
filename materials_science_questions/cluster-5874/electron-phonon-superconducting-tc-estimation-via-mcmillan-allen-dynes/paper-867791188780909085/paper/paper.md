
# Phase diagram and superconductivity of Calcium Alanates under pressure

Simone Di Cataldo \( ^{1,2} \) 

Lilia Boeri \( ^{2,3} \) 

 \( ^{1} \)  Institut für Festkörperphysik, Wiedner Hauptstraße 8-10, 1040 Wien, Austria

 \( ^{2} \)  Dipartimento di Fisica, Sapienza Università di Roma, 00185 Roma, Italy

 \( ^{3} \)  Centro Ricerche Enrico Fermi, Via Panisperna 89 A, 00184 Rome, Italy

E-mail: simone.cataldo@tuwien.ac.at, lilia.boeri@uniroma1.it

Abstract. In this paper we present a first-principles study of the high-pressure superconducting phase diagram of calcium alanates (Ca-Al-H), based on ab-initio crystal structure prediction and anisotropic Migdal-Eliashberg Theory. Calcium alanates have been intensively studied at ambient pressure for their hydrogen-storage properties, but their high-pressure behavior is largely unknown. By performing a full scan of the ternary convex hull at several pressures between 0 and 300 GPa, we identify several new structural motifs, characterized by a high Al-H coordination, where Al d orbitals participate in the bonding. Among all new phases thus identified, we focus in particular on a phase with  \( CaAlH_{7} \)  composition, which lies on the convex hull at 300 GPa, and remains dynamically stable down to 50 GPa, with a predicted superconducting  \( T_{c} \)  of 88 K, which likely represents a new promising template to achieve increase chemical precompression in ternary hydrides. Our findings reveal important insights into the structure-property relationships of calcium alanates under high pressure, and highlight a possible strategy to achieve conventional superconductivity at low pressures.

Keywords: Superconductivity, Condensed matter physics, Electronic structure, Electron-phonon coupling

Submitted to: J. Phys.: Condens. Matter
 

## 1. Introduction

The discovery of high-temperature superconductivity at 203 K in  \( H_{3}S \)  in 2014 [1, 2] at Megabar pressures brought hydrides into the spotlight of superconducting materials research. Their extremely high  \( T_{c} \) s deriving from an electron-phonon mechanism finally demonstrated that conventional superconductors can, in fact, achieve high  \( T_{c} \) , contrary to previous misconceptions.

In this context, computational predictions based on ab-initio calculations have become an invaluable tool for materials discovery, often anticipating and guiding experiments towards the most promising materials  \( [3, 4, 5] \) . In the span of just eight years, all possible combinations of a single element plus hydrogen (binary hydrides) have been computationally explored  \( [4, 3, 6] \)  seeking novel high-temperature superconductors, several of which were also experimentally confirmed  \( [7, 8, 9, 10, 11, 12, 13] \) . Computational studies of high-pressure hydrides not only permitted to identify unknown materials, but also to gain a much deeper understanding of the relationship between chemical bonding and conventional superconductivity  \( [14, 15, 16, 17, 18] \) , instrumental to the design of new materials with improved superconducting properties.

In the last three years, the focus of hydride research has shifted towards identifying materials which can form and remain stable at more accessible pressure than record superhydrides, even at the cost of a reduced  \( T_{c} \) , as this would open up the possibility of more practical applications. One possible route is to explore ternary hydrides, i.e. compounds that contain hydrogen and two other elements. Indeed, the presence of two different elements permits to realize a much wider variety of chemical environments for hydrogen. For example, we have shown that in lanthanum hydrides the addition of a third element stabilizes a high- \( T_{c} \)  structure with  \( LaBH_{8} \)  composition down to 35 GPa [19, 20, 21]. We later demonstrated that the stabilization pressure could be further reduced with a careful choice of the elements in the La/B site within the same structural template down to 3 GPa in  \( BaSiH_{8} \) . [22, 23] It is very likely that other mechanism of increased chemical precompression may be identified in other ternary hydrides, which offer an unexplored playground of more than 7000 potential combinations.

In this study, we focus on calcium alanates (CAH), a class of widely-available materials which has been extensively investigated at ambient pressure because of their hydrogen storage properties  \( [24, 25, 26, 27] \) . CAH are also closely related to calcium borohydrides (CBH), which we studied in a previous publication  \( [28] \) , without finding viable candidates for increased chemical precompression.

At ambient pressure, both CBH and CAH form hydrogen-rich molecular crystals containing  \( Ca^{++} \)  and  \( (YH_{x})_{2}^{-} \)  anions (Y = B, Al; x = 4 for Al, x = 2, 3, 4 for B) [29, 27], which can absorb/desorb large amounts of hydrogen. Despite sharing the same valence, Al differs from B because of the presence of empty 3d orbitals, which lie close in energy to the 2p states, and can participate in the bonding. Already at ambient pressure, partial occupation Al-d orbitals stabilize a  \( CaAlH_{5} \)  phase with corner-sharing octahedra [24, 25], which is absent in the phase diagram of CBH. Since it is well known that high pressures (forbidden chemistry) phases, i.e. phases with unusual compositions and configurations, particularly for elements with low-lying unoccupied orbitals, we expect that also in CAH Al-d orbitals will play an
 
![](./images/867791188780909085_1.jpg)

Figure 1. Convex hull diagrams for the Ca-Al-H system at 0, 50, 100 and 300 GPa. Thermodynamically stable compositions are indicated as orange circles. Compositions within 25 meV/atom of the hull are shown as red squares. Crystal structures for all thermodynamically stable ternary alanates at 0, 50, 100, and 300 GPa. Ca, Al, and H atoms are shown as grey, red, and blue spheres, respectively.

increasing role in the bonding, leading to a phase diagram substantially different from that of CBH. This is indeed confirmed by our calculations, which show that CAH tends to form very complex high-pressure phases, with high Al-H coordination.

In particular, we identify a high- \( T_{c} \)  (82 K)  \( CaAlH_{7} \)  phase, which should form at high pressures and remain dynamically stable down to 50 GPa, with an unusual structural template, in which planes of H-cages are connected by H-H bonds. It is very likely that also this new  \( XYH_{7} \)  could be further optimized by a careful substitution of other elements in place of calcium, leading to higher  \( T_{c} \)  and/or lower stabilization pressures.

The paper is structured as follows: first we describe the ternary phase diagram at 0, 50, 100, and 300 GPa, and describe the thermodynamically stable structures. Second, we discuss the electronic properties of those structures. Third, we compare the low- and high-pressure structures of CAH and CBH. Finally, we discuss in detail the superconducting properties of the high-pressure  \( CaAlH_{7} \)  structure.

## 2. Results and discussion

## 2.1. Phase Diagram

The phase diagram of CAH as a function of pressure was obtained computing the ternary convex hull, using ab-initio evolutionary crystal structure prediction as implemented in the USPEX code [30, 31]. For the underlying total energy calculations and relaxations we employed the DFT Vienna ab-initio simulation package (VASP) [32], with Projector-Augmented Wave pseudopotentials [33] and PBE exchange-correlation functional. Further details can be found in the SM.

The left panel of figure 1 shows the convex hulls obtained at 0, 50, 100, and 300 GPa, for each of these pressures, we sampled over 5000 structures and over a hundred unique
 
![](./images/867791188780909085_2.jpg)

![](./images/867791188780909085_3.jpg)

![](./images/867791188780909085_4.jpg)

![](./images/867791188780909085_5.jpg)

![](./images/867791188780909085_6.jpg)

![](./images/867791188780909085_7.jpg)

Figure 2. Electronic band structure for four selected calcium alanates. Black and colored lines indicate the DFT and Wannierized bands, respectively. The Wannier orbital onto which the band projection is carried out is indicated on the right side of each figure.

compositions. These values of pressures were chosen to ensure a reasonable sampling of low and intermediate/high-pressure phases, based on our previous experience on binary and ternary hydrides. The right panel of the figure shows the crystal structures of the phases corresponding to stable compositions.

At ambient pressure (0 GPa) we find that the most stable ternary composition is  \( CaAlH_{5} \) , although  \( \mathrm{Ca(AlH_{4})_{2}} \)  is only 22 meV/atom above the hull, in agreement with calculations from Ref. [25], as well as experiment, since both phases can be synthesized [34, 35]. The two structures are characterized by a qualitatively different geometry of the Al-H bonds: corner-sharing  \( AlH_{6} \)  octahedra in  \( CaAlH_{5} \) , and  \( AlH_{4} \)  tetrahedra in  \( \mathrm{Ca(AlH_{4})_{2}} \) , in both cases with interstitial calcium atoms.

At 50 GPa,  \( CaAlH_{5} \)  remains the only stable composition, and the stable structure contains face- and corner-sharing  \( AlH_{8} \)  polyhedra with square antiprismatic geometries, alternating with Ca in a body-centered orthorhombic sublattice.

At 100 GPa, the stable compositions are  \( CaAlH_{5} \) ,  \( CaAl_{2}H_{8} \) , and  \( Ca_{2}AlH_{11} \) . The structure of  \( CaAlH_{5} \)  contains the same  \( AlH_{8} \)  square antiprisms seen at 50 GPa, but now arranged in a corner- and edge-sharing pattern which compenetrates the calcium sublattice. In  \( \mathrm{Ca(AlH_{4})_{2}} \) , which re-enters as a stable composition, the structure is radically different
 

from the ambient pressure one, as it shows a sublattice of corner- and edge-sharing  \( AlH_{8} \)  distorted snub disphenoids encaging Ca atoms. The ground-state structure of  \( Ca_{2}AlH_{11} \)  is characterized by a lattice of  \( AlH_{10} \)  elongated square bipyramids which sharing the top vertex, alternated with interstitial Ca atoms and trapped  \( H_{2} \)  molecules.

Finally, at 300 GPa the only stable ternary composition is  \( CaAlH_{7} \) . The crystal structure contains a combination of side-sharing  \( AlH_{12} \)  cuboctahedra which share faces with  \( CaH_{16} \)  truncated cubes capped with square pyramids. The two combined polyhedra fully tessellate the space. The  \( AlH_{12} \)  cuboctahedra lie in separate planes, connected by a H–H bond, highlighted by green hydrogen atoms in Fig. 1 (right panel). The H-H bond distance increases with increasing pressure, going from 0.86 to 0.95 Å from 50 to 300 GPa. This value indicates delocalized atomic H-H bonds rather than molecular ones.

Overall, the structural changes in ternary calcium alanates (CAH) with increasing pressure suggest a profound change in the orbital hybridization. At ambient pressure, the presence of octahedral  \( AlH_{6} \)  motifs indicates that H partially hybridizes with Al–d states, whereas the  \( AlH_{4}^{-} \) motifs indicate  \( H-Al sp^{3} \)  hybridization. The tetrahedral geometry is also observed in  \( \mathrm{Ca(BH_{4})_{2}} \) , while stable  \( \mathrm{Ca(BH_{3})_{2}} \)  and  \( \mathrm{Ca(BH_{2})_{2}} \)  compositions correspond to  \( sp^{2} \)  and sp hybridization [36, 28].

As pressure increases, however, CAH behaves in a substantially different way from CBH, as Al–d states are effectively pulled down in energy compared to s,p states. In the CBH phase diagram only structures with sp,  \( sp^{2} \) , and  \( sp^{3} \)  hybridization are stable or weakly metastable up to 150 GPa, and some survive up to 300 GPa; even at 300 GPa, the B–H coordination is never larger than six. In CAH, already at 50 GPa, stable structures exhibit complex polyhedral structures; the average number of vertices and faces increases with pressure, up to a 12-coordinated Al–H polyhedron in  \( CaAlH_{7} \) .

## 2.2. Electronic properties

The trend in crystal structures suggests that in many CAH structures Al-d orbitals participate in the chemical bond with H. To make the argument less qualitative, in Fig. 2 we show the partial density of states (pDOS) [37], calculated for all the thermodynamically stable structures:  \( \mathrm{Ca}(\mathrm{AlH}_{4})_{2} \)  and  \( CaAlH_{5} \)  at 0 GPa,  \( CaAlH_{5} \)  at 50 GPa,  \( CaAlH_{5} \)  and  \( Ca_{2}AlH_{11} \)  at 100 GPa, and  \( CaAlH_{7} \)  at 300 GPa. Note that in the Figure the Fermi energy (for metals) and the valence band maximum (for insulators) is taken as zero.

In  \( CaAlH_{5} \)  at 0 GPa, the DOS in the valence region is characterized by two peaks; the electronic states can be understood in terms of molecular  \( AlH_{6} \)  octahedra, resulting from  \( Al-sp^{3}d^{2} \)  hybridization. The system is an insulator with a wide bonding/antibonding gap of 2.6 eV. The DOS in the valence region of  \( \mathrm{Ca(AlH_{4})_{2}} \)  is characterized by two well-separated peaks, extending from about -6 to -3 and to -3 to 0 eV. These states exhibit a very small dispersion, and like in  \( \mathrm{Ca(BH_{4})_{2}} \)  [28], correspond to  \( sp^{3} \)  molecular orbitals of the  \( AlH_{4}^{-} \) anion. We note, however, that a small projection of Al-d states is found near the top of the valence band. This system is also insulating, with a wide boding/antibonding gap of 4.5 eV, in line with other calculated values in the literature [38, 39].

 \( CaAlH_{5} \)  at 50 GPa is still insulating, but the gap is reduced to 1.2 eV. Here the occupied states merge into a single peak, and the
 

weight of Al-d states is significantly enhanced compared to lower pressures.

At 100 GPa, the electronic structure of  \( CaAlH_{5} \)  is very similar to the one at 50 GPa, with a gap only slightly reduced to about 1 eV.  \( Ca_{2}AlH_{11} \) , on the other hand, is a compensated semimetal.

The behavior of the only phase stable at 300 GPa is qualitatively very different from what observed at lower pressures.  \( CaAlH_{7} \)  is metallic, with strongly dispersed electronic bands. Here, Al-d states give a non-zero contribution to the DOS down to the bottom of the valence band at -15 eV, indicating a major rearrangement of the bonds.

![](./images/867791188780909085_8.jpg)

Figure 3. Formation enthalpy ranking of different structures with atomic substitution of B (Al) into the Al (B) site. The formation enthalpy is calculated with respect to pure elements. The formation enthalpy is indicated by a colored line, along with the composition. The substitution is indicated by the labels over the x axis (e.g. an Al substitution in the B site is indicated by Al in B). Structures that are dynamically unstable or relax into a different phase are indicated with a red cross.

In order to further elucidate the increasing role of Al-d orbitals in the bonding, we performed an additional analysis, in which we were performed a systematic substitution of Al in CBH structures and vice versa, and evaluated the thermodynamical and dynamical stability of the resulting structures. In Fig. 3 we show the ranking of the resulting structures according to formation enthalpy *.

When Al is substituted in the ambient-pressure structures of B  \( \left(\mathrm{Ca}(\mathrm{BH}_{3})_{2}\right. \)  and  \( \left.\mathrm{Ca}(\mathrm{BH}_{4})_{2}\right) \) , the relaxed structures retain the same qualitative features as the original structure, and turn out to be competitive in energy with the lowest-energy structure for  \( \mathrm{Ca}(\mathrm{AlH}_{4})_{2} \) . This can be easily understood, as Al employs in this structure its s, p valence orbitals. The  \( B \rightarrow Al \)  substitution is, on the other hand, more problematic: while  \( \mathrm{Ca}(\mathrm{AlH}_{4})_{2} \)  also retains its qualitative features upon B substitution,  \( CaAlH_{5} \)  does not, and the structure "breaks down" upon relaxation, giving rise to a distorted combination of  \( BH_{4} \)  anions and atomic hydrogen. In fact, the B 3d orbitals lie too far away in energy from the 2s, 2p valence orbitals to participate in the bonding.

At 300 GPa, we substituted Al in the structures with  \( CaBH_{5} \)  and  \( CaBH_{6} \)  composition that we found to be stable for the Ca-B-H system at the same pressure in our previous work \( ^{[28]} \) . Both structures exhibit unusual B-H bonding: the former is characterized by  \( BH_{5} \)  triangular bipyramids, the latter by  \( BH_{6} \)  6-vertex antiprisms. Al substitution in the  \( CaBH_{5} \)  and  \( CaBH_{6} \)  structures leads to a qualitative change in the crystal structure. In  \( CaBH_{5} \)  the  \( BH_{5} \)  triangular bipyramids drastically rearrange into side-sharing  \( AlH_{10} \)  irregular polyhedra, while in  \( CaBH_{6} \)  the 6-vertex antiprisms become corner-sharing regular cuboctahedra. The opposite process, i.e. B substi-

* The formation enthalpy is considered with respect to the pure elements, e.g.  \( \Delta H(CaAlH_{5}) = H(CaAlH_5) - H(Ca) - H(Al) - \frac{5}{2}H(H_2) \) 

† The data on the crystal structures after the relaxation is available as a compressed file in the Supplementary Material [40]
 

tution in  \( CaAlH_{7} \)  exhibits the same qualitative features, but the structure is dynamically unstable.

![](./images/867791188780909085_9.jpg)

Figure 4. Phonon dispersions, atom-projected phonon density of states  \( (F(\omega)) \)  and Éliashberg function  \( (\alpha^{2}F(\omega)) \)  for  \( CaAlH_{7} \)  at 300 GPa. The total  \( F(\omega) \)  and  \( \alpha^{2}F(\omega) \)  are shown as solid black lines, while their projections onto Ca, Al, and H are shown as green, red, and orange filled curves, respectively.

![](./images/867791188780909085_10.jpg)

Figure 5. Leading edge of the anisotropic superconducting gap at 50 (red) and 300 GPa (blue) as a function of temperature. The corresponding superconducting  \( T_{c} \)  is shown in Tab. 1. The interpolating line is obtained from a fit with the function  \( \Delta(T) = \Delta_{0} \sqrt{k \frac{T_{c} - T}{T}} \)  of the weighted average of the anisotropic gap at  \( \omega = 0 \) .

## 2.3. Superconductivity

Of all the CAH structures predicted in this work,  \( CaAlH_{7} \)  is the only one with the qualitative prerequisites to host high- \( T_{c} \)  superconductivity [41, 4]: a dense hydrogen sublattice, metallic behavior, and a significant fraction of hydrogen DOS at the Fermi level. We computed its electron-phonon coupling properties at 50, 100, and 300 GPa using Density Functional Perturbation Theory [42, 43, 44, 45].

In Fig. 4 we show the phonon dispersions, Eliashberg function and phonon DOS at 300 GPa (The phonon dispersions at the other pressures are shown in the Supplementary Figure 3 [40]). Similarly to most hydrides, the total ep coupling is spread over the whole optical branch, and the Eliashberg function has a predominantly hydrogen character, suggesting that the H-H intraband interactions, rather than Al-H interband ones, are providing most of the coupling. We observe a soft mode in the branch around 100 meV around the X point, and another in the acoustic branch around the R point (See also Supplementary Figure 3 [40]). The latter drives the system dynamical unstable below 50 GPa. Some hydrogen modes between 100 and 200 meV are not strongly dispersive, indicating that these modes correspond to short-range, molecular-like H-H vibrations, while between 200 and 300 meV the larger dispersion indicates collective vibrations of the H cages, analogous to sodalite-like clathrate hydrides [18, 17]. We note that non-dispersive modes correspond to phonon eigenvectors parallel to the c axis, and vice versa.

Using the calculated ep spectrum we calculated the superconducting  \( T_{c} \)  by solving self-consistently the anisotropic Migdal-Eliashberg equations on a fine interpolated grid § at 50, 100 and 300 GPa, using the EPW code [46, 47], and a constant value of the Morel-Anderson § 32 × 32 × 32 for both electrons and phonons
 

pseudopotential  \( \mu^{*}=0.10 \) , further details are available in the Supplementary Materials.

In Fig. 5 we show the calculated leading edge of the superconducting gap at  \( \omega = 0 \)  for different pressures. The superconducting gap is quite isotropic, and spreads over a small energy interval of 2-3 meV. (Further details on the anisotropic gap are provided in the Supplementary Material).

The  \( T_{c} \)  is determined by fitting the average of the leading edge of the superconducting gap with an interpolating function (See caption of Fig. 5), and extrapolating to  \( \Delta = 0 \) . The results are summarized in Tab. 1. The ratio  \( \frac{2\Delta}{T_{c}} \)  is exactly 3.52 at 300 GPa, and it increases with decreasing pressure up to 3.97 at 50 GPa, as a soft-mode boosts coupling at lower pressure and pushes the system away from the weak-coupling limit.

The  \( T_{c} \)  increases from 61 K at 300 GPa, to 82 K at 50 GPa, as a consequence of mode softening. In fact, the e-ph coupling constant  \( \lambda \)  increases from 0.66 to 1.06, while the logarithmic-average frequency  \( \omega_{log} \)  decreases by almost one third (from 150 to 68 meV) in the same interval.

A  \( T_{c} \)  of 82 K at 50 GPa places  \( CaAlH_{7} \)  in the same class as  \( XYH_{8} \)  ternary clathrate hydrides, [19, 22, 21] i.e. that of ternary hydride superconductors, where efficient chemical precompression stabilizes a dense hydrogen sublattice at lower pressures than binary hydrides. It is very likely that  \( T_{c} \)  and stabilization pressure may further be optimized by careful chemical substitution as was shown for  \( LaBH_{8} \)  and  \( BaSiH_{8} \)  [19, 22].

## 3. Conclusions

In conclusion, using ab initio methods based on Density Functional Theory, we studied the phase diagram and the superconducting properties of calcium aluminum hydrides (CAH) under pressures of 0, 50, 100, and 300 GPa. We found several stable phases in which aluminum progressively increases its coordination with hydrogen as pressure increases.

In particular, we find a structure with  \( CaAlH_{7} \)  composition which, to the best of our knowledge, is still unreported. The structural motif comprises layers of  \( AlH_{12} \)  cage-like polyhedra (cubooctahedra), linked by atomic H-H bonds, and is thus structurally analogous to other ternary  \( XYH_{n} \)  hydrides, where H cage-like units can be retained down to relatively low pressures, due to the chemical precompression exerted by the X/Y sublattice.

CaAlH_{7} is thermodynamically stable at 300 GPa, but remains dynamically stable down to 50 GPa, where we predict a superconducting  \( T_{c} \)  of 82 K by self-consistently solving the fully anisotropic Migdal-Eliashberg equations.

Hence,  \( CaAlH_{7} \)  is one of the very few hydrides retaining high- \( T_{c} \)  superconducting properties down below Megbar pressures. Like in  \( LaBH_{8} \) , where we have demonstrated the stabilization pressure can be lowered significantly by Ba/Si substitution, the  \( CaAlH_{7} \)  structure could also be further optimized by replacing Ca with other alkaline metals or earths, and Al with other non-metals such as Ga, In, or Sn.

## 4. Acknowledgments

L.B. and S.D.C. acknowledge funding from the Austrian Science Fund (FWF) P30269-N36 and support from Fondo Ateneo-Sapienza 2018-2021. S.D.C. acknowledges computational resources from CINECA, proj. IsC90-HTS-TECH and IsC99-ACME-C, and the Vienna Scientific Cluster, proj. 71754 "TEST". LB acknowledges support from
 

<table><tr><td>Comp.</td><td>P (GPa)</td><td>\( \lambda \)</td><td>\( \omega_{log}(meV) \)</td><td>\( T_{c}^{MM} \)  (K)</td><td>\( \frac{2\Delta}{T_{c}} \)</td></tr><tr><td>CaAlH \( _{7} \)</td><td>50</td><td>1.06</td><td>68</td><td>60</td><td>3.97</td></tr><tr><td>CaAlH \( _{7} \)</td><td>100</td><td>0.85</td><td>103</td><td>63</td><td>3.65</td></tr><tr><td>CaAlH \( _{7} \)</td><td>300</td><td>0.66</td><td>146</td><td>50</td><td>3.52</td></tr></table>

Table 1. Superconducting properties of the high-pressure  \( CaAlH_{7} \)  phase at various pressures. The critical temperature is obtained by self-consistently solving the anisotropic Éliashberg equations until the gap is converged within  \( 10^{-2} \)  meV ( \( T c^{aniso} \) ), using a value of 0.10 for the Morel-Anderson pseudopotential  \( \mu^{*} \) .

Project PE0000021, “Network 4 Energy Sustainable Transition – NEST”, funded by the European Union – NextGenerationEU, under the National Recovery and Resilience Plan (NRRP), Mission 4 Component 2 Investment 1.3 - Call for tender No. 1561 of 11.10.2022 of Ministero dell’Università e della Ricerca (MUR).

## References

[1] Drodzov A P, Eremets M I, Troyan I A, Ksenofontov V and Shylin S I 2015 Nature 52573–76

[2] Einaga M, Sakata M, Ishikawa T, Shimizu K, Eremets M, Drodzov A P, Troyan I A, Hirao N and Ohishi Y 2016 Nature Physics 12 835–838

[3] Pickard C J, Errea I and Eremets M 2020 Annual Review of Condensed Matter Physics 11 57–76

[4] Flores-Livas J A, Boeri L, Sanna A, Profeta G, Arita R and Eremets M 2020 Physics Reports 856 1–78

[5] et al L B 2021 J. Phys. Condens. Matter In press

[6] Oganov A R, Pickard C J, Zhu Q and Needs R J 2019 Nature Reviews Materials 4 331–348

[7] Liu H, Haumov I I, Geballe Z M, Somayazulu M, Tse J S and Hemley R J 2018 Phys. Rev. B 98 100102

[8] Somayazulu M, Ahart M, Mishra A K, Geballe Z M, Baldini M, Meng Y, Struzhkin V V and Hemley R J 2019 Phys. Rev. Lett. 122 027001

[9] Drodzov A P, Kong P P, Besedin S P, Kuzonikov M A, Mozaffari S, Balicas L, Balakirev F F, Graf D E, Prakapenka V B, Greenberg E, Knyazev D A, Tkacz M and Eremets M I 2019 Nature 569 528–531

[10] Semenok D V, Kvashin A G, Ivanova A G, Svitlyk V, Fominski V Y, Sadakov A V, Sobolevskiy

O A, Pudalov V M, Troyan I A and Oganov A R 2020 Materials Today 33 36–44

[11] Troyan I A, Semenok D V, Kvashin A G, Sadakov A V, Sobolevskiy O A, Pudalov V M, Ivanova A G, Prakapenka V B, Greenberg E, Gavriliuk A G, Struzhkin V V, Bergara A, Errea I, Bianco R, Calandra M, Mauri F, Monacelli L, Akashi R and Oganov A R 2021 Advanced Materials 332006832

[12] Drodzov A P, Minkov V, Besedin S, Kong P, Kuzovnikov M, Knyazev D and Eremets M 2018 arXiv preprint, arXiv:1808.07039

[13] Chen W, Semenok D V, Huang X, Shu H, Li X, Duan D, Cui T and Oganov A R 2021 Phys. Rev. Lett. 127 117001

[14] An J M and Pickett W E 2001 Phys. Rev. Lett. 86(19) 4366–4369 URL https://link.aps.org/doi/10.1103/PhysRevLett.86.4366

[15] Bernstein N, Hellberg C S, Johannes M D and Mazin I I 2015 Phys. Rev. B 91

[16] Heil C and Boeri L 2015 Phys. Rev. B 92 060508(R)

[17] Heil C, Cataldo S D, Bachelet G B and Boeri L 2019 Phys. Rev. B 220502

[18] Wang H, Tse J S, Tanaka K, Iitaka T and Ma Y 2012 PNAS 109 6463–6466

[19] Cataldo S D, Heil C, von der Linden W and Boeri L 2021 Phys. Rev. B 104 L020511

[20] Liang X, Bergara A, Wei X, Song X, Wang L, Sun R, Liu H, Hemley R J, Wang L, Gao G and Tian Y 2021 Phys. Rev. B 104 134501

[21] Zhang Z, Cui T, Hutcheon M J, Shipley A M, Song H, Du M, Kresin V Z, Duan D, Pickard C J and Yao Y 2022 Physical Review Letters 128

[22] Lucrezi R, Di Cataldo S, von der Linden W, Boeri L and Heil C 2022 NPJ: computational materials 8

[23] Roman Lucrezi Eva Kogler S D M A L B C H 2023 arXiv preprint: arXiv:2212.09789
 

[24] Peles A, Alford J A, Ma Z, Yang L and Chou M Y 2004 Physical Review B 70 165105

[25] Wolverton C and Ozolins V 2007 Physical Review B 75 064101

[26] Huan T D, Amsler M, Marques M A L, Botti S, Willand A and Goedecker S 2013 Physical Review Letters 110 135502

[27] Milanese C, Garroni S, Gennari F, Marini A, Klassen T, Dornheim M and Pistidda C 2018 Metals 8 ISSN 2075-4701 URL https://www.mdpi.com/2075-4701/8/8/567

[28] Cataldo S D, von der Linden W and Boeri L 2020 Phys. Rev. B 102 014516

[29] Rönnebro E and Majzoub E H 2007 The Journal of Physical Chemistry B 111 12045–12047 pMID: 17914804 (Preprint https://doi.org/10.1021/jp0764541) URL https://doi.org/10.1021/jp0764541

[30] Glass C W, Oganov A R and Hansen N 2006 Computer Physics Communication 175 713–720

[31] Lyakhov A O, Oganov A R, Stokes H T and Zhu Q 2013 Computer Physics Communication 184 1172–1182

[32] Kresse G and Furthmüller J 1996 Phys. Rev. B 54 11169

[33] Kresse G and Joubert D 1999 Phys. Rev. B 59 1758

[34] Iosub V, Matsunaga T, Tange K and Ishikiriyama M 2009 International Journal of Hydrogen Energy 34 906–912

[35] Mamatha M, Bogdanovic B, Felderhoff M, Pommerin A, Schmidt W, Schuth F and Weidenthaler C 2006 Journal of Alloys and Compounds 407 78–86

[36] Zhang Y, Majzoub E, Ozolins V and Wolverton C 2010 Phys. Rev. B 82 171407

[37] The partial dos was obtained by projecting the total DOS onto spherical harmonics centered on each atom, and integrated over a radius equal to the atomic radius.

[38] Jensen C, Wang Y and Chou M 2008 14 - alanates as hydrogen storage materials Solid-State Hydrogen Storage Woodhead Publishing Series in Electronic and Optical Materials ed Walker G (Woodhead Publishing) pp 381–419 ISBN 978-1-84569-270-4 URL https://www.sciencedirect.com/science/article/pii/B9781845692704500144

[39] Paskevicius M, Jepsen L H, Schouwink P, Cerný R, Ravnsbaek D B, Filinchuk Y, Dornheim M,

Besenbacher F and Jensen T R 2017 Chem. Soc. Rev. 46 1565–1634

[40] URL will be inserted by publisher the supplementary material is available at...

[41] Belli F, Novoa T, Contreras-Garcia J and Errea I 2021 Nature Communications 12 5381

[42] Savrasov S Y 1996 Phys. Rev. B 54 16470–16486

[43] Baroni S, de Gironcoli S, Corso A D and Giannozzi P 2001 Rev. Mod. Phys 73 515

[44] Giannozzi P, Baroni S, Bonini N, Calandra M, Car R, Cavazzoni C, Ceresoli D, Chiarotti G L, Cococcioni M and Dabo I 2009 J. Phys.: Condens. Matter 21 395502

[45] Giannozzi P, Andreussi O, Brumme T, Bunau O, Nardelli M B, Calandra M, Car R, Cavazzoni C, Ceresoli D, Cococcioni M, Colonna N, Carnimeo I, Corso A D, de Gironcoli S, Delugas P, DiStasio R A, Ferretti A, Floris A, Fratesi G, Fugallo G, Gebauer R, Gerstmann U, Giustino F, Gorni T, Jia J, Kawamura M, Ko H Y, Kokalj A, Kucukbenli E, Lazzeri M, Marsili M, Marzari N, Mauri F, Nguyen N L, Nguyen H V, dela Roza A O, Paulatto L, Ponce S, Rocca D, Sabatini R, Santra B, Schlipf M, Seitsonen A P, Smogunov A, Timrov I, Thonhauser T, Umari P, Vast N, Wu X and Baroni S 2017 J. Phys.: Condens. Matter 29 465901

[46] Giustino F, Cohen M L and Louie S G 2007 Phys. Rev. B 76 165108

[47] and E R Margine S P, Verdi C and Giustino F 2016 Comp. Phys. Communications 209 116–133
 
