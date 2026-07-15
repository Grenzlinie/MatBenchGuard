![](./images/813054246575407106_1.jpg)

Subscriber access provided by UNIV OF SCIENCES PHILADELPHIA

Article

# Inverse band structure design via materials database screening: application to square planar thermoelectrics

Eric B Isaacs, and Chris Wolverton

*Chem. Mater.*, Just Accepted Manuscript • DOI: 10.1021/acs.chemmater.7b04496 • Publication Date (Web): 26 Feb 2018

Downloaded from http://pubs.acs.org on February 26, 2018

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/813054246575407106_2.jpg)

Chemistry of Materials is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Inverse band structure design via materials database screening: application to square planar thermoelectrics

Eric B. Isaacs and Chris Wolvererton*

Department of Materials Science and Engineering, Northwestern University, Evanston, Illinois 60208, United States

E-mail: c-wolverton@northwestern.edu

## Abstract
Electronic band structure contains a wealth of information on the electronic properties of a solid and is routinely computed. However, the more difficult problem of designing a solid with a desired band structure is an outstanding challenge. In order to address this inverse band structure design problem, we devise an approach using materials database screening with materials attributes based on the constituent elements, nominal electron count, crystal structure, and thermodynamics. Our strategy is tested in the context of thermoelectric materials, for which a targeted band structure containing both flat and dispersive components with respect to crystal momentum is highly desirable. We screen for thermodynamically stable or metastable compounds containing $d^8$ transition metals coordinated by anions in a square planar geometry in order to mimic the properties of recently identified oxide thermoelectrics with such a band structure. In doing so, we identify 157 compounds out of a total of over half a million candidates. After further screening based on electronic band gap and structural anisotropy, we explicitly compute the band structures for the several of the candidates in order to validate the approach. We successfully find two new oxide systems that achieve the targeted band structure. Electronic transport calculations on these two compounds, $\text{Ba}_2\text{PdO}_3$ and $\text{La}_4\text{PdO}_7$, confirm promising thermoelectric power factor behavior for the compounds. This methodology is easily adapted to other targeted band structures and should be widely applicable to a variety of design problems.

## Introduction
Electronic band structure, the energy $\epsilon$ as a function of crystal momentum $\mathbf{k}$ for each electron band, encapsulates a wealth of fundamental information on the electronic properties of a crystalline material. Simple examples include the nature and magnitude of the fundamental band gap and the carrier effective masses (for a semiconductor) and the Fermi surface (for a metal). Band structure impacts virtually all aspects of material properties, including electronic, thermal, optical, magnetic, and mechanical behavior.

It has now become a routine task to compute the band structure for a given crystal structure, in particular using Kohn-Sham density functional theory (DFT).$^{1,2}$ However, the inverse problem of finding or designing a compound with a targeted band structure is a much more difficult challenge. Franceschetti and Zunger devised an approach to this inverse problem relying on the rapid, approximate evaluation of the forward problem.$^{3}$ In this work, an optimization algorithm (simulated annealing) was used to achieve a targeted band struc-

ture property (maximum band gap) within the configurational space of a specific superlattice or alloy system. Variants of this approach involve other optimization algorithms (e.g., genetic algorithms, particle swarm optimization), other targeted properties (e.g., minimum band gap, direct band gap, large optical transition oscillator strength), and expanded structural spaces. $^{4-6}$

In this work, we take a different approach to the inverse band structure design problem via a materials database screening based on several materials attributes. Whereas the search space in the approach of Franceschetti and Zunger is all the possible substitutional decorations of a given structure type for a particular chemistry, we search over different stoichiometries, chemistries, and a wide variety of known crystal structures. Our chemical and structural space is the more than half a million inorganic crystalline solids in the Open Quantum Materials Database (OQMD), $^{7,8}$ a database of electronic structure calculations. In addition to $\sim 38,000^{9}$ of the known crystalline solids from the Inorganic Crystal Structure Database (ICSD), $^{10,11}$ the OQMD currently contains electronic structure calculations of $\sim 493,000$ hypothetical crystalline compounds based on decorating known binary and ternary prototype crystal structures. $^{12}$ Our approach takes advantage of this existing, extensive collection of materials data. Though this database contains the electronic structures of all compounds, the band structures along high-symmetry directions in $\mathbf{k}$-space are not computed or stored in the database. In other words, we cannot simply "search" the database directly for the targeted band structure.

The materials attributes that we use in our design/screening strategy include (1) the elements contained in the material, (2) nominal valence electron count for each element, (3) the local coordination geometry of atoms in the crystal structure, and (4) thermodynamic stability. For example, here we focus (for reasons described below) on (1) compounds containing transition metals and anions, (2) transition metals in a $d^{8}$ electronic configuration, (3) transition metals coordinated by anions in a square planar arrangement, and (4) compounds that are thermodynamically stable or metastable. We design the targeted band structure by querying for any crystal that simultaneously possesses all the specified materials attributes. In our approach, full computation of the band structure (the forward problem) is only necessary for a small number of candidate compounds as a validation. This is highly advantageous since band structures require additional DFT calculations and a quantitative figure of merit for a candidate band structure is not always easily computed.

![](./images/813054246575407106_3.jpg)

Figure 1: (a) Geometry and (b) corresponding crystal field splitting of $d$ orbitals of a transition metal in square planar coordination ($D_{4h}$ point group). The $d^{8}$ electronic configuration is shown as an example. Note that the order of the $A_{1g}$ and $B_{2g}$ levels is sometimes reversed, as in the case of $\text{Bi}_2\text{PdO}_4$ in Ref. 13.

We test our design strategy in the context of thermoelectric materials, which can enable waste heat capture via the conversion of a temperature gradient into a electrical current. $^{14}$ The thermoelectric figure of merit is proportional to the power factor $\sigma S^{2}$, where $\sigma$ is the electronic conductivity and $S$ is the Seebeck coefficient. Since the power factor is strongly dependent on band structure, thermoelectrics provides an excellent context to study band structure design. In particular, as discussed below, a band structure containing both flat and dispersive parts with respect to $\mathbf{k}$ leads to large power factor. In our case, the materials attributes specified above related to constituent elements, nominal electron count, and structure ($d^{8}$ transition metals coordinated by anions in square planar geometry, shown in Fig. 1) are chosen to mimic those of $\text{Bi}_2\text{PdO}_4^{13}$ and

$PbPdO_2$, $^{15,16}$ two oxide thermoelectrics which were recently found to exhibit such a band structure. Screening the entire OQMD, we find 157 candidates for this targeted band structure. After further screening based on electronic band gap and structural anisotropy, we compute the band structures for several compounds to verify our approach. We identify two existing oxide compounds ($Ba_2PdO_3$ and $La_4PdO_7$) that successfully achieve the targeted band structure, providing validation to our inverse band structure design approach. Additionally, electronic transport calculations indicate promising power factor behavior in these compounds, particularly for $n$-type doping

## Computational Details

Using a Boltzmann transport approach, Kuroki and Arita showed that a band with both flat (small $
abla_{\mathbf{k}}\epsilon$) and dispersive (large $
abla_{\mathbf{k}}\epsilon$) parts along a direction in $\mathbf{k}$-space can lead to high power factor if the electronic chemical potential $\mu$ lies at an energy separating the two. $^{17}$ For this special “pudding-mold” band structure, the band velocity difference across $\mu$ (proportional to $S$) is large, and the high band velocity of the dispersive part and large Fermi surface enable a large $\sigma$. In addition to leading to the exceptionally high power factor of $Na_xCoO_2$, $^{17}$ the pudding-mold band structure has been suggested to contribute to the record-breaking thermoelectric performance of $SnSe^{18–20}$ and to the large computed power factors of recently proposed Fe-based Heusler compounds. $^{21}$

While the original pudding-mold band structure concept corresponds to regions of small and large $
abla_{\mathbf{k}}\epsilon$ along the *same* direction in $\mathbf{k}$-space, one can consider a broader definition in which the flat and dispersive regions can occur along in *different* directions in $\mathbf{k}$-space. Such a band structure naturally emerges from a low-dimensional (e.g. one- or two-dimensional) crystal structure, which can be thought of as analogous to the low-dimensional nanostructures proposed by Hicks and Dresselhaus to exhibit high thermoelectric performance. $^{22,23}$ Usui and Kuroki showed that one-dimensional crystal structures in particular can lead to a large power factor due to the enhanced density of states at the band edge. $^{24}$

A previous computational study proposed $Bi_2PdO_4$ as a possibly promising thermoelectric oxide due in part to large power factor. $^{13}$ A key component to the promising electrical properties was the pudding-mold band structure, which relates to the square planar coordination (illustrated in Fig. 1(a)) of $d^8$ Pd by oxygen. As shown in Fig. 1(b), a $d^8$ (as well as $d^4$ or $d^6$, in principle) electronic configuration of the metallic element in this coordination can lead to a semiconducting compound according to crystal field theory, $^{25}$ as is the case for $Bi_2PdO_4$. In this particular compound, the stacked arrangement of square planar $PdO_4$ units with $d_{3z^2-r^2}$ highest-occupied orbitals (whose $z$ axis is aligned with the stacking direction) leads to a valence band that is dispersive in the stacking direction and flat in the other directions (a quasi-one-dimensional crystal structure). Although it has a distinct structure, $PbPdO_2$ also has a $d^8$ Pd square planar coordination, pudding-mold-like band structure, and promising thermoelectric properties, $^{15,16}$ which is suggestive of a connection between square planar coordination and pudding-mold band structure. We note that Co-doped $PbPdO_2$ has also been studied as a possible spin-gapless semiconductor. $^{26–28}$

Therefore, we choose our materials attributes to mimic those of $Bi_2PdO_4$ and $PbPdO_2$ and screen the OQMD based on the following criteria:

- **Chemistry** – Compound must contain TM and anion elements, and (for practicality) no radioactive elements.
- **Structure** – In the compound, TMs must be coordinated by anions in square planar coordination (4 nearest neighbors and bond angles $4 \times 85-95^\circ, 2\times \geq 175^\circ$). $^{29}$
- **Electron count** – All TM in the compound must have $d^4$, $d^6$, or $d^8$ configuration. As shown in Fig. 1(b), for a TM in square planar coordination, such nominal

electron counts can lead to a semiconduc- tor based on crystal field theory.

- Thermodynamics – Compound must be thermodynamically stable, metastable (within 25 meV/atom of the convex hull), or unstable but in ICSD. This attribute relates the desired synthesizability of the compound, rather than the band structure.

Since the OQMD and the associated qmpy framework $^{30}$ do not intrinsically compute or store the coordination environments of different atoms in a crystal structure, we wrote a separate code to enable the assessment of our structural criterion. To query for a particular coordination environment, this code first computes all the distances between TMs and anions (taking into account translation vectors) to check if the coordination number is a desired value, e.g. 4 for square planar. If so, the bond lengths and bond angles for the nearest-neighbor shell are computed to enable any local structural query. Details on the parameters we employ in this code, including how the coordination number is computed, are included in the Supporting Information.

Additional DFT calculations are performed for the most promising candidate materials using VASP. $^{31-34}$ The generalized gradient approximation $^{35}$ is employed and the Kohn-Sham equations are solved using a 500 eV plane wave basis with the projector augmented wave (PAW) method $^{36,37}$ and uniform $k$-point meshes of $k$-point density $\geq 700/\mathrm{\AA}^{-3}$. The total energy and ionic forces are converged to within $10^{-6}$ eV and $0.001$ eV/Å, respectively. Electronic band structures are computed for high-symmetry $k$-paths based on the conventions of Setwayan et al. $^{38}$ Semiclassical electronic transport calculations within the constant relaxation time approximation are performed in BOLTZTRAP with $k$-point density $\geq 2300/\mathrm{\AA}^{-3}.^{39}$

# Results and Discussion

## Characterization of identified compounds

![](./images/813054246575407106_4.jpg)

Figure 2: Total number of compounds (thick bars) as a function of consecutive screening filters on a logarithmic scale, with breakdown in terms of thermodynamic categories (thin bars). Unstable compounds are only included if they are reported in ICSD.

Figure 2 summarizes the number of compounds found in the OQMD to satisfy the screening criteria. As different criteria are applied successively, the number of candidates decreases from the total of over half a million to just 157. The largest fractional decreases in candidate compounds come from the thermodynamics criterion (reduction by factor of 7) and the square planar structural criterion (reduction by factor of 21).

The vast majority of the compounds identified (150/157) turn out to be present in ICSD (including stable and metastable compounds). 68 of the these compounds have one of 32 structural prototypes listed in the ICSD, which are included in the Supporting Information. The structural prototypes corresponding to the most compounds are $\mathrm{KBrF_{4}}$-type (9, e.g. $\mathrm{PbPdF_{4}}$), $\mathrm{La_{2}Sb}$-type (8, e.g. $\mathrm{GdZrSb}$), $\mathrm{Rb_{3}PdF_{5}}$-type (7, e.g. $\mathrm{BaLa_{2}PtO_{5}}$), and $\mathrm{K_{2}PtCl_{4}}$-type (5, e.g. $\mathrm{Tl_{2}PdCl_{4}}$).

The lack of non-ICSD compounds found might be explained by the fact that few of the structural prototypes used to generate hypothetical compounds in the OQMD contain square planar bonding. Only two of the prototype structures used to systematically and comprehensively (i.e., considering nearly all periodic table elements) generate hypothetical compounds contain any square planar coordination. The only one currently in the OQMD in which all sites for an element are in square planar coordination is the L1₂ structure (e.g. Cu in CuAu₃). The other, the D0₂₂ prototype, has square planar coordination for 1/3 of the sites of one of the elements (e.g. Al in Al₃Ti). The 7 non-ICSD compounds found by our query, (Ce/Pr/Nd/Sm/Gd/Tb/Dy)₂PdO₄, actually correspond to neither the L1₂ nor the D0₂₂ prototype. These compounds have the distinct layered Ca₂RuO₄ prototype structure, which was previously explored for a very small number (~ 25) of Pd oxide compounds to search for and assess the stability of materials similar to Bi₂PdO₄.¹³

The chemistry of the 157 identified compounds is summarized in Fig. 3(a). Oxides are the most prevalent chemistry, with 70 compounds. Note that we include compounds with polyatomic anions in this category if the oxygen of the polyatomic anion is bonded to the transition metal. Examples include iodates, nitrates, sulfates, selenates, and pyrophosphates. There are also a significant number of halides (56). The remaining 31 compounds include sulfides, selenides, phosphides, nitrides, carbonyls, and cyanides. Our query is able to find arbitrarily complex stoichiometries and crystal structures, as exemplified by H₈CrSiO₄F₆. Each Cr is bonded to 2 hydroxide groups and 2 F in this compound, which we choose to count as an oxide in Fig. 3(a). The crystal structure also contains H₂, H₂O₂, and SiF₆ units.

Fig. 3(b) illustrates the particular elements involved in the square planar bonding. Pd oxides are dominant with 37 occurrences, and Pd halides also occur significantly (29 times) in the group of compounds. This is consistent with the prevalence of Pd²⁺ in square planar environments as has been found previously.⁴⁰ Au

![](./images/813054246575407106_5.jpg)

Figure 3: Characterization of the 157 candidate compounds identified. (a) Distribution of stabilities split up in terms of oxides, halides, and other chemistries, (b) Network of chemical bonding of the square planar environment in which node size represents elemental occurrence and edge thickness is proportional to bonding frequency, (c) Histogram of DFT band gaps (greyed out for values larger than 1.1 eV).

oxides and chlorides also feature prominently.
Despite the dominance of Pd oxides, there is still overall a diverse range of transition metals and anions in the 157 compounds.

We also observe significant diversity in structures. There are compounds of all dimensionalities (e.g. 0D PdCl₂, 1D PdBr₂, 2D PdS₂, 3D Mn₃Sb). Here dimensionality refers to the connectivity of the square planar units. For example, in PdBr₂ there are 1D channels of edge-sharing PdBr₄ square planar units. Even within a particular dimensionality of the square planar connectivity, there is significant diversity in structure. For example, for 0D (unconnected) square planar compounds, there are distinct relative orientations of the square planar units (e.g. perpendicular in PbPdF₄ vs. parallel in Tl₂PdCl₄).

## Further screening of oxides based on band gap

The band gap, in addition to the dispersion of the bands, is critically important for thermoelectric materials.⁴¹ In particular, high-efficiency thermoelectric materials such as PbTe, SnSe, and Bi₂Te₃ have band gaps no larger than around 1 eV. As such, to further screen the 157 candidate compounds, we further require a DFT band gap no larger than 1.1 eV. We choose not to put a lower limit on the band gap since semilocal DFT is well known to underestimate the electronic band gap.⁴² As illustrated in the band gap distribution in Fig. 3(c), this leaves 72 remaining compounds.

We focus on the 33 of these compounds that are pure oxides (i.e., containing no other anion element). These candidate compounds are listed in the Supporting Information. The known square planar thermoelectric candidate materials Bi₂PdO₄ and PbPdO₂ are included in these 33, which is a validation of the screening strategy. One of the 33 compounds is CaPd₃O₄, which has been studied as a possible excitonic insulator⁴³,⁴⁴ and topological Dirac semimetal.⁴⁵ The electronic band structures are computed for five of the compounds in which the connectivity of the square planar units is not the same in all spatial directions: NaBi₂AuO₅, Ba₂TlCuO₅, Ba₂PdO₃, LiCuO₂, and La₄PdO₇. We focus on such "non-isotropic" compounds since the difference in bonding in different directions should lead in principle to different $
abla_{\mathbf{k}}\epsilon$ in different directions of $\mathbf{k}$-space as is targeted for the pudding-mold band structure.

## Compounds achieving the targeted band structure

Two of the compounds for which the band structure is computed, Ba₂PdO₃ and La₄PdO₇, successfully achieve the targeted band structure. Ba₂PdO₃ (space group Immm) and La₄PdO₇ (space group C2/m) both contain one-dimensional chains of corner-sharing PdO₄ square planar units (shown going into the plane for La₄PdO₇ in Fig. 4). For both of these materials, the number of $d$ electrons (roughly estimated via projection within the PAW sphere) on the transition metal (Pd) site is 8.4, consistent with the nominal $d^8$ configuration.

As shown in Fig. 4, Ba₂PdO₃ and La₄PdO₇ possess the pudding-mold band structure. Both show flat and dispersive parts of the low-energy spectrum both below and above the Fermi energy. For example, for Ba₂PdO₃ the conduction band disperses strongly (weakly) along $\Gamma$-Y ($\Gamma$-Z). The valence band disperses strongly (weakly) along W-R (W-T). La₄PdO₇ similarly shows both dispersive and flat components, though it is seen most strongly in the conduction band. We note that La₄PdO₇ appears to have a smaller valence bandwidth than Ba₂PdO₃ as the highest-occupied band is flat for much of the $k$-path shown in Fig. 4(b). The density of states in Fig. 4 shows strong Pd $d$ character in the band edges. The fact that we find the targeted band structure in these two compounds is a strong success of our inverse design strategy.

Although the square planar unit itself is two-dimensional, the dimensionality of the band structure for the extended system depends strongly on the connectivity of the square planar units. For example, one-dimensional chains of PdO₄ square planar units (e.g. stacked in the case of Bi₂PdO₄, corner-sharing in the case

![](./images/813054246575407106_6.jpg)

Figure 4: Electronic band structure and total and projected density of states of (a) $Ba_2PdO_3$ and (b) $La_4PdO_7$. The dashed red line marks the valence band maximum. In the crystal structures shown in the insets, Pd, O, and Ba/La atoms are shown in blue, red, and green, respectively.

of $Ba_2PdO_3$) lead to a one-dimensional band structure with dispersion primarily in one direction, whereas a two-dimensional layer of square planar $PdO_4$ units (e.g. $La_2PdO_4$) leads to a two-dimensional band structure with dispersion primarily in two directions. This suggests our type of inverse band structure design for pudding-mold thermoelectrics might also have success for other coordinations, in addition to square planar, that lend themselves to low-dimensional crystal structures.

We note that our design strategy did not uncover any candidate compounds with a pudding-mold band structure that contain a lone pair cation, which would also be desirable for a thermoelectric by lowering lattice thermal conductivity. $^{46,47}$ There are several compounds with Zr bonded to Sb in square planar coordination (e.g. GdZrSb), but here Sb is nominally the anion. In nearly all of the other compounds identified, either a metal is found (e.g. $Ba_2TlCuO_5$, $Li_8Bi_2PdO_{10}$) or the electronic band gap is too large (e.g. 1.4 eV for $Pb_2PdCl_6$, 2.3 eV for $Tl_2Ni(CN)_4$). For $NaBi_2AuO_5$, the valence band edge does not primarily corresponding to the TM $d$ orbitals, though it does contain some pudding-mold-like features.

# Electronic transport properties of $Ba_2PdO_3$ and $La_4PdO_7$

Finally, as a confirmation that the designed electronic band structure leads to promising thermoelectric behavior, we perform electronic transport calculations via the constant relaxation time approximation. To isolate the effect of band structure shape, rather than the magnitude of the band gap, we compare the transport properties of $Ba_2PdO_3$ and $La_4PdO_7$ to $Bi_2PdO_4$ at a fixed band gap of 1.41 eV. This value corresponds to the band gap of $Bi_2PdO_4$ from hybrid DFT calculations and was used in Ref. 13.

Figure 5(a) shows the behavior of the power factor (divided by the relaxation time) for these 3 materials as a function of doping at 700 K. Typical doping magnitudes leading to peak thermoelectric performance that can be experimentally achieved are $10^{19}$ to $10^{21}$ cm$^{-3}$. $^{48}$

![](./images/813054246575407106_7.jpg)

Figure 5: Power factor $\sigma S^{2}$ divided by relaxation time $\tau$ for $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ and $\mathrm{La}_{4}\mathrm{PdO}_{7}$ as compared to that of $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$. (a) $\sigma S^{2}/\tau$ as a function of doping at 700 K, (b) $\sigma S^{2}/\tau$ as a function of temperature for $p$ and $n$-type doping of $10^{20}\ \mathrm{cm}^{-3}$. To isolate the effect of band structure shape, for all cases the band gap is scissor shifted to the HSE band gap of $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$ (1.41 eV) as in Ref. 13

For $p$-type doping, the power factor magnitude of $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ and $\mathrm{La}_{4}\mathrm{PdO}_{7}$ is similar to that of $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$ ($\sim 10^{12}\ \mathrm{W/(m\ K^{2}\ s)}$). $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$ achieves a peak in $S^{2}\sigma/\tau$ of $1.36 \times 10^{12}\ \mathrm{W/(m\ K^{2}\ s)}$ for a carrier concentration of $5.3 \times 10^{20}\ \mathrm{cm}^{-3}$. One of the new compounds ($\mathrm{Ba}_{2}\mathrm{PdO}_{3}$) achieves a higher peak value at a higher doping ($3.5 \times 10^{21}\ \mathrm{cm}^{-3}$), but for more reasonable dopings ($< 10^{21}\ \mathrm{cm}^{-3}$), the value for $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$ is larger than those of $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ and $\mathrm{La}_{4}\mathrm{PdO}_{7}$ by roughly 50%. In contrast, for $n$-type doping $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ and $\mathrm{La}_{4}\mathrm{PdO}_{7}$ exhibit larger power factor behavior. $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ has the largest peak value of $1.48 \times 10^{12}\ \mathrm{W/(m\ K^{2}\ s)}$ at doping of $4.4 \times 10^{20}\ \mathrm{cm}^{-3}$. The improved $n$-type behavior of the new compounds can be explained by the presence of pudding-mold band structure in the conduction band, which is lacking in $\mathrm{Bi}_{2}\mathrm{PdO}_{4},{}^{13}$ in addition to the valence band. The corresponding plots of power factor versus temperature for a fixed doping of $10^{20}\ \mathrm{cm}^{-3}$ shown in Fig. 5(b) also illustrate the superior $n$-type performance for the new compounds as compared to $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$.

Such transport calculations confirm that the pudding-mold band structures achieved lead to significant promise for thermoelectric applications, for $p$- and especially $n$-type doping. We performed hybrid DFT calculations (using $\mathrm{HSE}^{49}$) of $\mathrm{Ba}_{2}\mathrm{PdO}_{3}$ and $\mathrm{La}_{4}\mathrm{PdO}_{7}$ exhibit band gaps of $\approx 1.5 - 1.6\ \mathrm{eV}$ (close to the $1.41\ \mathrm{eV}$ of $\mathrm{Bi}_{2}\mathrm{PdO}_{4}$). Therefore, we believe incorporating band gap differences between the three materials to not significantly affect the comparison in Fig. 5.

## Conclusions

Using a materials database and screening criteria based on several material attributes, we have devised a method for inverse band structure design in the search space of chemistry, stoichiometry, and structure. Our method does not require the evaluation of the band structure except as a validation. As an example case, we apply the band structure design to the pudding-mold band structure desirable for thermoelectric materials with high power

factor. Out of the over half a million candidate materials, 157 candidate systems are identified. After further screening based on electronic band gap and structural anisotropy, we compute the band structures for several of the candidate compounds as a validation of the approach. Two palladium oxide systems, $Ba_2PdO_3$ and $La_4PdO_7$, successfully achieve the targeted band structure and are found to exhibit promising thermoelectric power factor behavior. Inverse band structure design via materials database screening represents a powerful, versatile approach for the rational identification and design of materials. This general approach opens up many possibilities for designing desirable band structures for a broad range of applications.

Acknowledgement We acknowledge support from the U.S. Department of Energy under Contracts DE-SC0014520 (overall design strategy and thermoelectric transport calculations) and DE-SC0015106 (development of software tools for high-throughput screening). Computational resources were provided by the Quest high performance computing facility at Northwestern University and the National Energy Research Scientific Computing Center (U.S. Department of Energy Contract DE-AC02-05CH11231).

Supporting Information Available: Additional details on the materials database screening criteria and full list of the 157 candidate compounds identified. This material is available free of charge via the Internet at http://pubs.acs.org/.

# Notes and References

(1) Hohenberg, P.; Kohn, W. Inhomogeneous Electron Gas. *Phys. Rev.* **1964**, 136, B864–B871.

(2) Kohn, W.; Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* **1965**, 140, A1133–A1138.

(3) Franceschetti, A.; Zunger, A. The inverse band-structure problem of finding an atomic configuration with given electronic properties. *Nature* **1999**, 402, 60–63.

(4) Kim, K.; Graf, P. A.; Jones, W. B. A genetic algorithm based inverse band structure method for semiconductor alloys. *J. Comput. Phys.* **2005**, 208, 735–760.

(5) Dudiy, S. V.; Zunger, A. Searching for Alloy Configurations with Target Physical Properties: Impurity Design via a Genetic Algorithm Inverse Band Structure Approach. *Phys. Rev. Lett.* **2006**, 97, 046401.

(6) Xiang, H. J.; Huang, B.; Kan, E.; Wei, S.-H.; Gong, X. G. Towards Direct-Gap Silicon Phases by the Inverse Band Structure Design Approach. *Phys. Rev. Lett.* **2013**, 110, 118702.

(7) Saal, J. E.; Kirklin, S.; Aykol, M.; Meredig, B.; Wolverton, C. Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD). *JOM* **2013**, 65, 1501–1509.

(8) Kirklin, S.; Saal, J. E.; Meredig, B.; Thompson, A.; Doak, J. W.; Aykol, M.; Rühl, S.; Wolverton, C. The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies. *npj Comput. Mater.* **2015**, 1, 15010.

(9) There are $\sim$ 44,000 unique ICSD compounds without partial occupancy of atomic sites in the crystal structure; $\sim$ 38,000 of these with the smallest number of atoms in the primitive unit cell ($\lesssim 35$ atoms) have been calculated in the OQMD as of April 2017.

(10) Bergerhoff, G.; Hundt, R.; Sievers, R.; Brown, I. D. The inorganic crystal structure data base. *J. Chem. Inf. Comput. Sci.* **1983**, 23, 66–69.

(11) Belsky, A.; Hellenbrandt, M.; Karen, V. L.; Luksch, P. New developments in the Inorganic Crystal

Structure Database (ICSD): accessibility in support of materials research and design. Acta Crystallogr. Sect. B 2002, 58, 364–369.

(12) As of April 2017.

(13) He, J.; Hao, S.; Xia, Y.; Naghavi, S. S.; Ozoliņš, V.; Wolverton, C. ${\rm Bi_2PdO_4}$: A Promising Thermoelectric Oxide with High Power Factor and Low Lattice Thermal Conductivity. Chem. Mater. 2017, 29, 2529–2534.

(14) Goldsmid, H. J. Introduction to Thermoelectricity; Springer Series in Materials Science; Springer: Berlin, Heidelberg, 2010; Vol. 121.

(15) Ozawa, T. C.; Taniguchi, T.; Nagata, Y.; Noro, Y.; Naka, T.; Matsushita, A. Metal–insulator transition and large thermoelectric power of a layered palladium oxide: ${\rm PbPdO_2}$. J. Alloys Comp. 2005, 388, 1–5.

(16) Lamontagne, L. K.; Laurita, G.; Gaultois, M. W.; Knight, M.; Ghadbeigi, L.; Sparks, T. D.; Gruner, M. E.; Pentcheva, R.; Brown, C. M.; Seshadri, R. High Thermopower with Metallic Conductivity in p-Type Li-Substituted ${\rm PbPdO_2}$. Chem. Mater. 2016, 28, 3367–3373.

(17) Kuroki, K.; Arita, R. “Pudding Mold” Band Drives Large Thermopower in ${\rm Na_xCoO_2}$. J. Phys. Soc. Jpn. 2007, 76, 083707.

(18) Zhao, L.-D.; Lo, S.-H.; Zhang, Y.; Sun, H.; Tan, G.; Uher, C.; Wolverton, C.; Dravid, V. P.; Kanatzidis, M. G. Ultralow thermal conductivity and high thermoelectric figure of merit in SnSe crystals. Nature 2014, 508, 373–377.

(19) Kutorasinski, K.; Wiendlocha, B.; Kaprzyk, S.; Tobola, J. Electronic structure and thermoelectric properties of n- and p-type SnSe from first-principles calculations. Phys. Rev. B 2015, 91, 205201.

(20) Wang, Z.; Fan, C.; Shen, Z.; Hua, C.; Hu, Y.; Sheng, F.; Lu, Y.; Fang, H.; Qiu, Z.; Lu, J.; Xu, Z.-A.; Shen, D. W.; Zheng, Y. Defects controlled hole doping and multi-valley transport in SnSe single crystals. arXiv:1706.10054 [cond-mat] 2017,

(21) Bilc, D. I.; Hautier, G.; Waroquiers, D.; Rignanese, G.-M.; Ghosez, P. Low-Dimensional Transport and Large Thermoelectric Power Factors in Bulk Semiconductors by Band Engineering of Highly Directional Electronic States. Phys. Rev. Lett. 2015, 114, 136601.

(22) Hicks, L. D.; Dresselhaus, M. S. Effect of quantum-well structures on the thermoelectric figure of merit. Phys. Rev. B 1993, 47, 12727–12731.

(23) Hicks, L. D.; Dresselhaus, M. S. Thermoelectric figure of merit of a one-dimensional conductor. Phys. Rev. B 1993, 47, 16631–16634.

(24) Usui, H.; Kuroki, K. Enhanced power factor and reduced Lorenz number in the Wiedemann–Franz law due to pudding mold type band structures. J. Appl. Phys. 2017, 121, 165101.

(25) Krishnamurthy, R.; Schaap, W. B. Computing ligand field potentials and relative energies of d orbitals: A simple general approach. J. Chem. Educ. 1969, 46, 799.

(26) Wang, X. L. Proposal for a New Class of Materials: Spin Gapless Semiconductors. Phys. Rev. Lett. 2008, 100, 156404.

(27) Chen, S. W.; Huang, S. C.; Guo, G. Y.; Lee, J. M.; Chiang, S.; Chen, W. C.; Liang, Y. C.; Lu, K. T.; Chen, J. M. Gapless band structure of PbPdO2: A combined first principles calculation and experimental study. Appl. Phys. Lett. 2011, 99, 012103.

(28) Kurzman, J. A.; Miao, M.-S.; Seshadri, R. Hybrid functional electronic structure of PbPdO 2 , a small-gap semiconductor.

J. Phys.: Condens. Matter 2011, 23, 465501.

(29) We do not require, however, that all the anions must be present in this bonding environment.

(30) qmpy. https://github.com/wolverton-research-group/qmpy.

(31) Kresse, G.; Hafner, J. Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium. Phys. Rev. B 1994, 49, 14251-14269.

(32) Kresse, G.; Hafner, J. Ab initio molecular dynamics for liquid metals. Phys. Rev. B 1993, 47, 558-561.

(33) Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 1996, 54, 11169-11186.

(34) Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 1996, 6, 15-50.

(35) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865-3868.

(36) Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 1994, 50, 17953-17979.

(37) Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 1999, 59, 1758-1775.

(38) Setyawan, W.; Curtarolo, S. High-throughput electronic band structure calculations: Challenges and tools. Comput. Mater. Sci. 2010, 49, 299-312.

(39) Madsen, G. K. H.; Singh, D. J. BoltzTraP. A code for calculating band-structure dependent quantities. Comput. Phys. Commun. 2006, 175, 67-71.

(40) Waroquiers, D.; Gonze, X.; Rignanese, G.-M.; Welker-Nieuwoudt, C.; Rosowski, F.; Göbel, M.; Schenk, S.; Degelmann, P.; André, R.; Glaum, R.; Hautier, G. Statistical Analysis of Coordination Environments in Oxides. Chem. Mater. 2017, 29, 8346-8360.

(41) Sofo, J. O.; Mahan, G. D. Optimum band gap of a thermoelectric material. Phys. Rev. B 1994, 49, 4565-4570.

(42) Perdew, J. P. Density functional theory and the band gap problem. Int. J. Quantum Chem. 1985, 28, 497-523.

(43) Hase, I.; Nishihara, Y. $CaPd_3O_4$ as an excitonic insulator. Phys. Rev. B 2000, 62, 13426-13429.

(44) Ichikawa, S.; Terasaki, I. Metal-insulator transition in $Ca_{1-x}Li_xPd_3O_4$. Phys. Rev. B 2003, 68, 233101.

(45) Li, G.; Yan, B.; Wang, Z.; Held, K. Topological Dirac semimetal phase in Pd and Pt oxides. Phys. Rev. B 2017, 95, 035102.

(46) Skoug, E. J.; Morelli, D. T. Role of Lone-Pair Electrons in Producing Minimum Thermal Conductivity in Nitrogen-Group Chalcogenide Compounds. Phys. Rev. Lett. 2011, 107, 235901.

(47) Nielsen, M. D.; Ozoliņš, V.; Heremans, J. P. Lone pair electrons minimize lattice thermal conductivity. Energy Environ. Sci. 2013, 6, 570-578.

(48) Snyder, G. J.; Toberer, E. S. Complex thermoelectric materials. Nat. Mater. 2008, 7, 105-114.

(49) Heyd, J.; Scuseria, G. E.; Ernzerhof, M. Hybrid functionals based on a screened Coulomb potential. J. Chem. Phys. 2003, 118, 8207-8215.

# Graphical TOC Entry

![](./images/813054246575407106_8.jpg)