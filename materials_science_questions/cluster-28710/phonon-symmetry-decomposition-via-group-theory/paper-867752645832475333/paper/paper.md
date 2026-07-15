
# Group Theory analysis of phonons in two-dimensional Transition Metal Dichalcogenides

J. Ribeiro-Soares, \( ^{1,2,*} \)  R. M. Almeida, \( ^{1} \)  E. B. Barros, \( ^{2,3} \)  P. T.

Araujo, \( ^{4} \)  M. S. Dresselhaus, \( ^{2,5} \)  L. G. Cançado, \( ^{1} \)  and A. Jorio \( ^{1} \) 

 \( ^{1} \) Departamento de Física, Universidade Federal de Minas Gerais,

Belo Horizonte, MG, 30123-970, Brazil

 \( ^{2} \) Department of Electrical Engineering and Computer Science,

Massachusetts Institute of Technology (MIT), Cambridge, MA 02139, USA

 \( ^{3} \) Departamento de Física, Universidade Federal do Ceará, Fortaleza, CE, 60455-900, Brazil

 \( ^{4} \) Department of Physics and Astronomy,

University of Alabama, Tuscaloosa, Alabama 35487, USA

 \( ^{5} \) Department of Physics, Massachusetts Institute

of Technology (MIT), Cambridge, MA 02139, USA

(Dated: Submitted on July 21, 2014)

## Abstract

Transition metal dichalcogenides (TMDCs) have emerged as a new two dimensional materials field since the monolayer and few-layer limits show different properties when compared to each other and to their respective bulk materials. For example, in some cases when the bulk material is exfoliated down to a monolayer, an indirect-to-direct band gap in the visible range is observed. The number of layers N (N even or odd) drives changes in space group symmetry that are reflected in the optical properties. The understanding of the space group symmetry as a function of the number of layers is therefore important for the correct interpretation of the experimental data. Here we present a thorough group theory study of the symmetry aspects relevant to optical and spectroscopic analysis, for the most common polytypes of TMDCs, i.e. 2Ha, 2Hc and 1T, as a function of the number of layers. Real space symmetries, the group of the wave vectors, the relevance of inversion symmetry, irreducible representations of the vibrational modes, optical selection rules and Raman tensors are discussed.

PACS numbers: 62.25.Jk, 63.22.Np, 68.35.Gy, 78.20.Ek
 

## I. INTRODUCTION

The interest in two-dimensional layered materials was enhanced after the successful isolation of monolayer graphene (the 2D component of graphite) reported in 2004. \( ^{1} \)  The monolayer of hexagonally linked carbon atoms made it possible to study a brand-new set of magnetic, electric and optical phenomena related to the Dirac-like nature of graphene electrons. \( ^{2} \)  The lack of a band gap, however, imposes some difficulties to graphene’s application in electronics, despite its high carrier mobility.

Other classes of 2D materials are now also being intensively studied for many different applications motivated mainly by the need of a band gap. Perovskite-based oxides, van der Waals solids, such as  \( Bi_{2}Se_{3} \) ,  \( Bi_{2}T_{e_{3}} \) , \( ^{3} \)  hexagonal boron nitride (h-BN), \( ^{4} \)  and transition metal dichalcogenides (TMDCs), such as  \( MoS_{2} \)  and  \( WSe_{2} \) , \( ^{5-7} \)  offer a wide range of compounds and combinations with potential use in the emerging field of 2D heterostructures \( ^{8} \)  (for example, tunable optoelectronic properties are obtained by a suitable choice of component layers \( ^{9,10} \) ). The TMDCs are layered materials of the form  \( MX_{2} \) , where “M” stands for groups 4 – 10 of transition metals and “X” stands for the chalcogen atoms S, Se or Te. \( ^{11} \)  The “M” and “X” atoms are strongly linked through covalent bonds to form 2D layers. Two adjacent sheets of chalcogen atoms are separated by a sheet of transition metal atoms in an X-M-X configuration, and the “monolayer” is actually composed of an atomic trilayer (TL) structure. The interaction among these trilayers are weak van der Waals interactions. The difference in the stacking order gives rise to different polytypes, while the combination of these different atoms leads to a variety of more than 30 different layered materials, with different optical, mechanical and electrical properties. \( ^{11-13} \) 

Some semiconducting TMDCs in this so-called monolayer form show a direct band gap in the visible range, which does not exist in their bulk counterparts. \( ^{5-7,14,15} \)  These band gaps open the possibility for flexible and transparent sensor applications, \( ^{11,12,16} \)  and the construction of heterostructures offers the possibility of tuning the TMDC behavior. \( ^{9,10,16} \)  The breaking of inversion symmetry in the monolayer, with the strong spin-orbit interaction coming from the metal d orbitals, gives rise to the spin splitting of the valence band at the high-symmetry K points of the Brillouin Zone (BZ). \( ^{17} \)  Since the K and  \( K' \)  points in the BZ are related to each other by time reversal symmetry, the spin splitting yields distinct symmetries from these two valleys, and the manipulation of this coupling opens the
 

possibility of a variety of valleytronic applications. \( ^{17-22} \) 

The dependence on the number of layers (N) and on the changes of the symmetry group have already been investigated in the characterization of the various TMDC optical properties, by means of Raman spectroscopy and Second Harmonic Generation (SHG). \( ^{[21,23-29]} \)  Group theory provides a valuable theoretical tool that can be used to understand the selection rules for the optical transitions, to find the eigenvectors for the lattice vibrations, and to identify the lifting of degeneracies due to external symmetry-breaking perturbations. \( ^{[30,31]} \)  A detailed study of these symmetry aspects for few-layers TMDCs is valuable to predict interesting characteristics and to properly interpret experimental results for these compounds, since few-layers TMDCs will belong to different space groups according to the number of layers, and their space groups will be different from those of their bulk crystal counterparts.

Group theory has already been used to describe the structure of TMDCs in the bulk form, for different polytypes, \( ^{32,33} \)  in the few-TL 2Hc polytype for zone center phonons (at the  \( \Gamma \)  BZ point) \( ^{23-25} \)  and electronic structure at the  \( \Gamma \)  and K points, \( ^{34} \)  and for more detailed understanding of some non-linear optical processes. \( ^{26} \)  In this work, group theory is applied to TMDCs in both the trigonal prismatic (H) and octahedral (T) metal atom coordinations, considering the stacking order for 2Ha and 2Hc for H, and 1T for T, and the dependence on the number of layers N (even or odd), and considering the full set of wave vectors in the BZ, i.e., going beyond the zone center. In section II, the symmetry analysis in real space is developed for the 2H (section IIA1) and 1T (section IIA2) polytypes, while the reciprocal space treatment is shown in section IIB. The relevance of inversion symmetry for the different TMDCs polytypes is discussed in section IIC. The irreducible representations for vibrational modes for few-TL TMDCs considering the high-symmetry points and lines in the BZ are presented in section IID, and the Raman and infrared selection rules are shown in section IIE, while section IIF gives the Raman tensors. Finally, section III summarizes the main conclusions and comments on the cases of lowering of symmetry induced by strain in  \( MoS_{2} \) , by engineering heterostructures, and by breaking the out-of-plane translational symmetry in  \( WSe_{2} \) .
 

## II. SYMMETRY ANALYSIS

## A. Real space symmetry

The family of layered TMDCs is composed of several polytypes with a different number of TLs, or different metal atom coordination that form the primitive unit cell. The main polytypes under experimental and theoretical consideration nowadays (and analyzed in the present work) are the trigonal prismatic 2H [2 TLs in a trigonal prismatic coordination (H) are required to form the bulk primitive unit cell] and the octahedral 1T [1TL in an octahedral coordination (T) is required to form the bulk primitive unit cell] (see Fig. 1). Each polytype, in turn, has a monolayer (1TL) as a basic 2D building block unit. The bulk crystal is made by piling up these monolayer units, namely 1H (trigonal prismatic or AbA coordination, where upper cases represent chalcogen atoms and lower cases represent metal atoms) and 1T (octahedral or AbC coordination), as can be observed in Figs. 1 (a) and (b), respectively. The blue spheres represent transition metal atoms, and the orange spheres represent the chalcogen atoms. For bulk versions of these layered materials, where the out-of-plane translational symmetry is present, the lateral view of the unit cells are highlighted with red rectangles in Figs. 1 (c), (d) and (e).

There are several other polytypes for stacks of more than two TLs, and at least 11 polytypes where identified in TMDCs. \( ^{33} \)  For example, the unit cell of the 3R- \( MoS_{2} \)  (with the stacking /AbA BcB CaC/) \( ^{32,33} \)  comprises 9 atoms in 3TLs. The treatment of these polytypes with a high number of TLs is beyond the scope of this work but, for the 3R case, Table I summarizes some symmetry considerations and gives representative examples.

## 1. 2H polytype

The 2H bulk polytype can assume two forms with different stacking symmetries: 2Ha (or /AbA CbC/ stacking), \( ^{32,33} \)  and 2Hc (/CaC AcA/ stacking). \( ^{33} \)  In 2Ha stacking, one transition metal atom is always on top of another transition metal atom of the next layer, as shown in Fig. 1 (c). This polytype is reported to occur in  \( NbSe_{2} \) ,  \( NbS_{2} \) , TaS \( _{2} \)  and TaSe \( _{2} \) crystals. \( ^{32} \)  In 2Hc stacking, any transition metal atom is sitting on top of two chalcogenides atoms of the subsequent layer, as shown in Fig. 1 (d). This polytype occurs in  \( MoS_{2} \) ,  \( WS_{2} \) , MoSe \( _{2} \)  and WSe \( _{2} \), crystals. Both polytypes belong to the non-symmorphic hexagonal
 

space group  \( P6_{3}/mmc^{32} \)  ( \( D_{6h}^{4} \) , in Schönflies notation, or #194 in the International Tables for Crystallography \( ^{35} \) ). The primitive unit cell for the bulk has 6 atoms (Z = 2, where Z is the number of structural MX \( _{2} \)  units required to form the primitive unit cell), and 3 atoms in each TL, as can be seen in the red rectangles of Figs. 1 (c) and (d). The Wyckoff positions for the 2H bulk polytypes, as well as the number of structural formulas Z are given in Table I.

The 2Hb polytype is possible and occurs for nonstoichiometric compounds with an excess of metal atoms intercalated in the van der Waals gap. \( ^{33} \)  Table I gives symmetry information and examples for this polytype. Some differences between the definition of 2Hb and 2Hc are found in literature, \( ^{32,33} \)  and the most recent nomenclature is used in this work. \( ^{33,36} \) 

![](./images/867752645832475333_1.jpg)

FIG. 1. (Color online) Transition metal atom coordination for (a) trigonal prismatic (H) and (b) octahedral (T) TMDCs polytypes. The blue spheres represent transition metal atoms and orange ones, chalcogen atoms. In (c), (d) and (e) the top and lateral views (top and bottom in each figure, respectively) of the primitive unit cells for bulk TMDCs materials are shown. The black rhombuses show the top view of the primitive unit cell, and the red rectangles indicate the lateral view. The primitive unit cell of the 2Ha (c) or the 2Hc (d) polytypes comprise 6 atoms, 2 transition metal atoms and 4 chalcogenides (Z = 2) in the trigonal prismatic coordination illustrated in (a), while the 1T polytype shown in (e) has 3 atoms, comprising 2 chalcogenides and 1 transition metal atom (Z = 1) in the octahedral coordination illustrated in (b).
 

For few-layers systems there is a reduction in symmetry due to the lack of translational symmetry along the z axis (the z axis is perpendicular to the basal plane of the TLs). The symmetry operations are reduced from 24 in the bulk to 12 for both even and odd numbers of TLs. Therefore, the few-TLs space groups are different from the bulk space groups and depend on the parity of the number of layers (even or odd number of TLs). Figure 2 illustrates 1TL and 2TL stacking arrangements for the 2Hc polytype. The hexagonal real space for 1TL and 2TLs are given in Figs. 2 (a) and (d), respectively.

The 2Hc polytype symmetry operations are illustrated in Figs. 2 (b) and (e), which are the top-view of the primitive unit cells. In Figs. 2 (c) and (f), the lateral views of the primitive unit cells are given for 1TL and 2TLs, respectively. The 1TL of 2H polytype belongs to the  \( P\bar{6}m2 \)  ( \( D_{3h}^{1} \)  or #187) hexagonal symmorphic space group, as well as to other few-layers compounds with odd number of layers, whose point symmetry operations are E (identity),  \( 2C_{3} \)  [clockwise and anti-clockwise rotations of  \( 120^{\circ} \)  about the axis represented as a black triangle in Fig. 2 (b)],  \( 3C_{2}^{\prime} \)  (two-fold axis in the  \( \sigma_{h} \)  plane),  \( \sigma_{n} \)  (the horizontal reflection plane that passes through the transition metal atom),  \( 2S_{3} \)  ( \( C_{3} \)  clockwise and anti-clockwise rotations, followed by a  \( \sigma_{h} \)  reflection), and  \( 3\sigma_{v} \)  (vertical reflection planes).

The 2TLs of 2H polytype and any other even number of TLs, belong to the  \( D_{3d}^{3} \)  ( \( P\bar{3}m1 \) , #164) symmorphic space group, whose symmetry operations are E,  \( 2C_{3} \) ,  \( 3C_{2}^{\prime} \)  [rotation axes placed in between two adjacent TLs, i. e., in the middle of the van der Waals gap in Fig. 2 (f)], inversion i [red dot in the  \( \sigma_{h} \)  plane of Fig. 2 (f)],  \( 3\sigma_{d} \)  [dihedral vertical mirror planes represented by red lines in Fig. 2 (e)] and  \( 2S_{6} \)  (clockwise and anti-clockwise rotations of  \( 60^{\circ} \)  followed by a  \( \sigma_{h} \)  reflection). For the 3TLs case, when another TL unit is added to the 2TLs shown in Figs. 2 (d), (e) and (f), the symmetry operations are the same as those observed for 1TL, since the  \( \sigma_{h} \)  plane is recovered as a symmetry operation. The addition of subsequent layers will always show symmetry variations depending on whether the number of layers is odd or even, and the difference between these two groups is ultimately given by the presence of the inversion symmetry in 2TLs (which is absent in 1TL) and the presence of the  \( \sigma_{h} \)  plane in 1TL (which is absent in 2TLs).
 

(a)

![](./images/867752645832475333_2.jpg)

(d)

![](./images/867752645832475333_3.jpg)

FIG. 2. (Color online) Primitive unit cell and symmetry operations of the 2Hc polytype. Blue spheres represent transition metal atoms and orange spheres represent chalcogen atoms. (a) and (d) show the top view for the 1TL and 2TLs, respectively.  \( \vec{a}_{1} \)  and  \( \vec{a_{2}} \)  are the primitive unit vectors, indicated in (a), while (b) and (e) represent the symmetry operations for the 1TL and 2TLs, respectively. The  \( C_{3} \)  axes are perpendicular to the xy plane in (b) and (e), and they are represented by black triangles. Three vertical mirror planes  \( \sigma_{v} \)  and three dihedral mirror planes  \( \mathbf{\sigma}_{d} \)  are indicated as red lines in (b) and (e), respectively, while the black lines are the three  \( C_{2}^{\prime} \)  rotation axes in the horizontal mirror  \( \sigma_{h} \) , represented in (c) and (f) together with the primitive unit cell. The  \( \sigma_{h} \)  itself is not a symmetry operation for 2TLs, but it is discussed here since it is part of the  \( S_{6} \)  operation, which is given as a  \( C_{6} \)  rotation followed by a  \( \sigma_{h} \)  reflection in this plane. The red lines in (e) denote the  \( \sigma_{d} \)  mirror planes, and the red dot in the center of (f) indicates the position of the inversion symmetry operation.

## 2. 1T polytype

From a symmetry standpoint, the 1T polytype is constructed by piling up single 1TL units, where each subsequent layer is exactly the same as the previous one, with one transition metal atom (or chalcogen atom) on top of another transition metal atom (or chalcoen atom), in an octahedral coordination. In the bulk TMDC, the stacking is /AbC/AbC/ (see Fig. 1). The bulk form belongs to the  \( D_{3d}^{3} \)  ( \( P\bar{3}m1, \#164 \) ) symmorphic space group. The unit cell comprises 3 atoms of one TL [red rectangle in Fig. 1 (e)]. The Wyckoff positions and number of structural formulas (Z) for the 1T polytype TMDCs are given in Table I.
 

Because all layers are identical, the symmetry operations do not change by increasing the number of TLs, no matter if N is even or odd. Figures 3 (a) and (d) show the 1TL and 2TLs structures, respectively, of the 1T polytype. The symmetry operations of 1TL are: E,  \( 2C_{3} \) ,  \( 3C_{2}^{\prime} \)  [the  \( C_{2}^{\prime} \(  rotation axes are in the reflection plane, between the two chalcogen atoms, dividing in half the transition metal atom, as showed in the black lines in Fig. 3 (c)], inversion i (red dot in the transition metal atom),  \( 3\sigma_{d} \)  [dihedral vertical mirror planes represented by red lines in Fig. 3 (b)] and  \( 2S_{6} \)  (clockwise and anti-clockwise rotations of  \( 60^{\circ} \)  followed by a  \( \sigma_{h} \)  reflection). In the 2TL case, the same operations are still valid, but now the reflection plane (Fig. 3 (f)) for the  \( S_{6} \)  operation is located in the van der Waals gap.

(a)

![](./images/867752645832475333_4.jpg)

(b)

![](./images/867752645832475333_5.jpg)

(d)

![](./images/867752645832475333_6.jpg)

(e)

![](./images/867752645832475333_7.jpg)

FIG. 3. (Color online) Primitive unit cell and symmetry operations of the 1T TMDCs polytype (bulk, 1TL and 2TLs). (a) and (d) show the 1TL and 2TL top view. In (d), chalcogen atoms are on top of chalcogen atoms, and transition metal atoms are on top of transition metal atoms, giving a similar top view to that observed for 1TL. In (b) and (e), the  \( C_{3} \)  rotation axes (represented as black triangles) are perpendicular to the basal plane. The red lines represent  \( \sigma_{d} \)  mirror planes, while the black lines stand for  \( C_{2}^{\prime} \)  rotation axes that lie in the  \( \sigma_{h} \)  plane. The primitive unit cells for 1TL (and bulk) and for 2TLs are shown in (c) and (f), respectively, and the red dot in their centers denotes the inversion operations. Notice that  \( \sigma_{h} \)  is not a symmetry operation for 1TL (or N odd), 2TLs (or N even) or bulk, but the reflection plane is shown here to indicate the reflection in the  \( 2S_{6} \)  operations.
 

## B. The Group of Wave Vector

The reciprocal space high symmetry points and directions for the 2H and 1T polytopes are shown in Fig. 4. Here  \( \vec{a}_{1} \)  and  \( \vec{a}_{\bar{2}} \)  are the primitive vectors of the real 2D lattice described by Eq. (1) and are shown in Fig. 2 (a). Correspondingly,  \( \vec{b}_{1} \)  and  \( \vec{b}_{\bar{2}} \)  [described in Eq. (2)] are the reciprocal lattice vectors shown in Fig. 4.

 \[ \vec{a}_{1}=\frac{a}{2}(\sqrt{3}\;\widehat{x}+\widehat{y}) \quad (1) \] 

 \[ \vec{b}_{1}=\frac{2\pi}{a}(\frac{\sqrt{3}}{3}\widehat{k}_{x}+\widehat{k}_{y}) \quad (2) \] 

![](./images/867752645832475333_8.jpg)

FIG. 4. (Color online) The Brillouin Zone (BZ) symmetries:  \( \Gamma \) , K,  \( K' \)  and M are high symmetry points; the  \( T, T' \)  and  \( \Sigma \)  are high symmetry lines, and the u denotes the symmetry for a generic point.  \( \vec{b}_{1} \)  and  \( \vec{b}_{\bar{2}} \)  denote the in-plane reciprocal lattice vectors.

The differences between the space groups  \( D_{3h}^{1} \)  and  \( D_{3d}^{3} \)  when the number of TLs is odd or even define different symmetries for the Group of the Wave Vectors (GWV) at each high-symmetry point or direction of the reciprocal space. Knowledge of the GWV is important because the invariance of the Hamiltonian under symmetry operations usually leads to degeneracies at these high-symmetry points or directions in the BZ. \( ^{37-39} \)  The GWV for the 2H TMDCs is similar to the GWV found for N-layer graphene and bulk graphite, \( ^{40} \)  since the space groups for bulk, N even, and N odd ( \( N \geq 3 \) ) TLs in the TMDC family resemble the corresponding graphene systems. However, the 1TL case in TMDCs lacks the inversion
 

symmetry and therefore belongs to the same space group  \( (P\bar{6}m2) \)  as that for other N-odd thin layers. Table II shows the point groups that are isomorphic to the GWV for all the BZ high-symmetry points and axes occurring for bulk and for both odd or even number of TLs in 2H polytype.

The 1T polytype has the same GWV regardless of the number of layers in the sample. The bulk is symmorphic, so it has the same GWV. Table III shows the GWV for different high-symmetry points and axes within the BZ for this polytype.

## C. The relevance of inversion symmetry

The presence or absence of inversion symmetry is an important aspect of TMDCs, since it opens the possibility of coupled spin and valley physics. \( ^{[17]} \)  The strong Spin-Orbit Coupling in TMDC materials is due to the d orbitals in their heavy metal atoms. The absence of inversion symmetry lifts the degeneracy of the same energy at the same  \( \vec{k} \)  value, at the K point of the BZ, and spin splitting values on the order of 0.4 eV have been observed in WSe \( _{2} \) . \( ^{[21]} \) 

The inversion symmetry is also important for the Second-Harmonic Generation (SHG) technique, which has been routinely used to probe not only the presence of inversion symmetry, but also the crystal orientation \( ^{26,27} \)  and, recently, the effect in SHG of two artificially stacked TMDCs layers. \( ^{41} \)  For centrosymmetric crystals, the  \( \chi^{(2)} \)  nonlinear susceptibility vanishes, \( ^{42} \)  and SHG signal is not observed. The 2H TMDCs polytype (and in this case, it also includes the 1TL), belong to the non-centrosymmetric space group  \( D_{3h}^{1} \)  and then it is possible to observe the SHG. \( ^{21,26-28,41-43} \)  The N-even TLs for 2H TMDCs do not show SHG, since their space groups are centrosymmetric. For the 1T TMDCs polytype, both N-even and N-odd TLs have the same centrosymmetric space group  \( D_{3d}^{3} \) , and the SHG signal is not expected. In this sense, the SHG mapping (together with other characterization tools) could be used to detect different polytypes in the same sample, since the 2H polytype with an odd number of layers shows SHG, while the layered 1T polytype does not.
 

TABLE II. Space groups and group of the wave vector (GWW) according to the number N of TLS for all high symmetry points and lines in the BZ of the 2H polytype of TMDPCs.

<table><tr><td>N order</td><td>Space group</td><td>T</td><td>\( K_{1}(K^{2}) \)</td><td>M</td><td>\( \pi(\Gamma\Gamma&#x27;) \)</td><td>\( \Sigma \)</td><td>\( \Delta \)</td></tr><tr><td>N even</td><td>\( D_{3h} \) ,  \( (Pbn2, #87) \)</td><td>\( D_{3h} \) ,  \( (Pbn2, #87) \)</td><td>\( C_{3v} \) ,  \( (Pbn2, #58) \)</td><td>\( C_{2}^{2} \) ,  \( (Pbn2, #58) \)</td><td>\( C_{2}^{2} \) ,  \( (Pbn2, #58) \)</td><td>\( C_{2}^{2} \) ,  \( (Pbn2, #58) \)</td><td>\( C_{2}^{2} \) ,  \( (Pbn2, #58) \)</td></tr><tr><td>N odd</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td><td>\( D_{3h} \) ,  \( (Pbn1, #16) \)</td></tr><tr><td>Bulk</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td><td>\( D_{3h} \) ,  \( (P6h/mcm, #194) \)</td></tr></table>

a:  \( \alpha \) - \( \gamma \) : is the  \( \theta \)  s mirror plane.

b:  \( \beta \) - \( \gamma \) : is the  \( \theta \)  s mirror plane.
 

TABLE III. Space group and group of the wave vector (GWW) for the high symmetry points and directions in the BZ for 1T polytype in TMDCs, valid for N-layer (even or odd) and bulk.

<table><tr><td>Space group</td><td>\( \Gamma \)</td><td>\( K(K&#x27;) \)</td><td>M</td><td>\( T(T&#x27;) \)</td><td>\( \Sigma \)</td><td>u</td></tr><tr><td>\( D_{3d}^{3} \)  (P3m1, #164)</td><td>\( D_{3d}^{3} \)  (P3m1, #164)</td><td>\( D_{3}^{3} \)  (P321, #150)</td><td>\( C_{2h}^{3} \)  (C2/m, #12)</td><td>\( C_{2}^{3} \)  (C2, #5)</td><td>\( C_{s}^{xz} \)  (or  \( C_{s}^{3} \) , Cm, #8) \( ^{a} \)</td><td>\( C_{1}^{1} \)  (P1, #1)</td></tr></table>

 \( ^{a} \) “xz” is the  \( \sigma \) ’s mirror plane.

## D. Irreducible representations for vibrational modes

The irreducible representations for the lattice vibrations ( \( \Gamma^{vib} \) ) are given by the direct product  \( \Gamma^{vib}=\Gamma^{eq}\oplus\Gamma^{vec} \) , where  \( \Gamma^{eq} \)  denotes the equivalence representation for the atomic sites, and  \( \Gamma^{vec} \)  is the representation for the x, y and z real space vectors. \( ^{38} \)  The  \( \Gamma^{vec} \)  representation can be written as  \( \Gamma^{vee}=\Gamma^{x}\oplus\Gamma^{y}\oplus\Gamma^{z} \) , or  \( \Gamma^{vec}=\Gamma^{x,y}\oplus\Gamma^{z} \)  when x and y have the same irreducible representation. The  \( \Gamma^{vib} \)  representations for the 2Ha, 2Hc and 1T polytypes are given in Tables IV, V and VI, respectively, for all the BZ high-symmetry points and lines (shown in Fig. 4), and for odd or even numbers of TLs. It is worth noticing that for the 2Hc polytype, the  \( \Gamma^{vib} \)  for the  \( K' \)  point is the complex conjugated form of the  \( \Gamma^{vib} \)  for the K point, while for the 2Ha polytype, the atomic sites are different (due to different Wyckoff positions) and the  \( \Gamma^{vib} \)  of the K and  \( K' \)  points are the same. In the 1T polytype, the  \( \Gamma^{vib} \)  for the K and  \( K' \)  points are also the same. The conversion from the Space Group (SG) to the Point Group (PG) notation for the irreducible representations is indicated in each character table of the Supplementary Material. \( ^{44} \)  The irreducible representations for vibrations for each high-symmetry point and line of the BZ for all the bulk polytypes are also given in Tables SI, SII and SIII of the Supplementary Material. \( ^{44} \) 

TABLE IV. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for N-layer TMDCs 2Ha-polytype (/AbA CbC/), considering all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="3">2Ha-polytype (/AbA CbC/)</td></tr><tr><td colspan="2">N odd</td><td>N even</td></tr><tr><td>Γ</td><td>(3N−1/2)(Γ1† ⊕ Γ3†) ⊕ (3N+1/2)(Γ1† ⊕ Γ2†)</td><td>(3N/2)(Γ1† ⊕ Γ1† ⊕ Γ2† ⊕ Γ3†)</td></tr><tr><td>K(K′)</td><td>(3N−1/2)(K1† ⊕ K2† ⊕ K2∗) ⊕ (3N+1/2)(K3† ⊕ K2†∗ ⊕ K1†)</td><td>(3N/2)(K1 ⊕ K2) ⊕ 3NK3</td></tr><tr><td>M</td><td>3N(M1 ⊕ M4) ⊕ (3N−1/2)M2 ⊕ (3N+1/2)M3</td><td>3N(M1† ⊕ M2†) ⊕ (3N/2)(M2† ⊕ M1†)</td></tr><tr><td>Σ</td><td>3N(Σ1 ⊕ Σ4) ⊕ (3N−1/2)Σ2 ⊕ (3N+1/2)Σ3</td><td>6NΣ1 ⊕ 3NΣ2</td></tr><tr><td>T(T′)</td><td>(9N+1/2)T† ⊕ (9N−1/2)T−</td><td>(9N/2)(T1 ⊕ T2)</td></tr><tr><td>u</td><td>(9N+1/2)u† ⊕ (9N−1/2)u−</td><td>9Nu</td></tr></table>
 

TABLE V. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for the N-layer TMDCs 2Hc-polytpe (/CaC AcA/), considering all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="3">2Hc-polytpe (/CaC AcA/)</td></tr><tr><td colspan="2">N odd</td><td>N even</td></tr><tr><td>\( \Gamma \)</td><td>\( (\frac{3N-1}{2})(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+})\oplus(\frac{3N+1}{2})(\Gamma_{3}^{+}\oplus\Gamma_{2}^{-}) \)</td><td>\( (\frac{3N}{2})(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}\oplus\Gamma{}_{2}^{-}\oplus\Gamma_{4}^{-}) \)</td></tr><tr><td>\( K(K^{\prime*}) \)</td><td>\( (\frac{3N+1}{2})(K_{1}^{+}\oplus K_{2}^{+}\oplus K_{3}^{-*})\oplus(\frac{3N-1}{2})(K_{1}^{-}\oplus K_{2}^{-}\oplus K_{3}^{+*}) \)</td><td>\( (\frac{3N}{2})(K_{1}\oplus K_{2})\oplus3NK_{3} \)</td></tr><tr><td>M</td><td>\( 3N(M_{1}\oplus M_{4})\oplus(\frac{3N-1}{2})M_{2}\oplus(\frac{3{N+1}}{2})M_{3} \)</td><td>\( 3N(M_{1}^{+}\oplus M_{2}^{-})\oplus(\frac{3N}{2})(M_{2}^{+}\oplus M_{1}^{-}) \)</td></tr><tr><td>\( \Sigma \)</td><td>\( 3N(\Sigma_{1}\oplus\Sigma_{4})\oplus(\frac{3N-1}{2})\Sigma_{2}\oplus(\frac{3{N+1}}{2})\Sigma_{3} \)</td><td>\( 6N\Sigma_{1}\oplus3N\Sigma_{2} \)</td></tr><tr><td>\( T(T^{\prime}) \)</td><td>\( (\frac{9N+1}{2})T^{+}\oplus(\frac{9N-1}{2})T^{-} \)</td><td>\( (\frac{9N}{2})(T_{1}\oplus T_{2}) \)</td></tr><tr><td>u</td><td>\( (\frac{9N+1}{2})u^{+}\oplus(\frac{9N-1}{2})u^{-} \)</td><td>\( 9Nu \)</td></tr></table>

TABLE VI. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for the N-layer TMDCs 1T-polytpe (/AbC/AbC/), considering all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="3">1T-polytpe (/AbC/AbC/)</td></tr><tr><td colspan="2">N odd</td><td>N even</td></tr><tr><td>\( \Gamma \)</td><td>\( (\frac{3N-1}{2})(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+})\oplus(\frac{3N+1}{2})(\Gamma_{2}^{-}\oplus\Gamma_{3}^{-}) \)</td><td>\( (\frac{3N}{2})(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}\oplus\Gamma{}_{2}^{-}\oplus\Gamma_{4}^{-}) \)</td></tr><tr><td>\( K(K^{\prime}) \)</td><td>\( (\frac{3N-1}{2})K_{1}\oplus(\frac{3N+1}{2})K{}_{2}\oplus3NK{}_{3} \)</td><td>\( (\frac{3N}{2})(K_{1}\oplus K_{2})\oplus3NK{}_{3} \)</td></tr><tr><td>M</td><td>\( (3N-1)(M_{1}^{+}\oplus M_{1}^{-})\oplus(\frac{3N-1}{2})M_{2}^{+}\oplus(3N+1)M_{2}^{-} \)</td><td>\( 3N(M_{1}^{+}\oplus M_{2}^{-})\oplus(\frac{3N}{2})(M_{2}^{+}\oplus M_{1}^{-}) \)</td></tr><tr><td>\( \Sigma \)</td><td>\( 6N\Sigma_{1}\oplus3N\Sigma_{2} \)</td><td>\( 6N\Sigma_{1}\oplus3N\Sigma_{2} \)</td></tr><tr><td>\( T(T^{\prime}) \)</td><td>\( (\frac{9N-1}{2})T_{1}\oplus(\frac{9N+1}{2})T{}_{2} \)</td><td>\( (\frac{9N}{2})(T_{1}\oplus T_{2}) \)</td></tr><tr><td>u</td><td>\( 9Nu \)</td><td>\( 9N u \)</td></tr></table>

## E. Raman and infrared selection rules

For bulk 2H polytypes (1T polytpe), the lattice vibration irreducible representations  \( \Gamma^{vib} \)  for the 18 (9) zone center phonons are reproduced in the first line of Table VII (see also Tables SI and SII from Supplementary Material). \( ^{44} \)  The classification of the modes as Raman active, infrared (IR) active, acoustic, and silent are given in Table VII.

TABLE VII. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for bulk TMDCs at the  \( \Gamma \)  point within the 2Ha, 2Hc and 1T polytypes. The Raman active, infrared active, acoustic and silent mode irreducible representations are identified.

<table><tr><td rowspan="2">r^{vib}</td><td colspan="2">2Ha and 2Hc polytypes</td><td rowspan="2">1T polytpe</td></tr><tr><td>\( \Gamma_{1}^{+}\oplus2\Gamma_{3}^{+}\oplus\Gamma_{5}^{+}\oplus2\Upsilon_{6}^{+}\oplus2\Gamma_{2}^{-}\oplus\Gamma_{4}^{-}\oplus2\Gamma 5^{-}\oplus\Gamma 6^{-} \)</td><td>\( \Gamma_{1}^{+}\oplus\Gamma_{3}^{+}\oplus2\Gamma_{2}^{-}\oplus2\Gamma 3^{-} \)</td></tr><tr><td>Raman</td><td>\( \Gamma_{1}^{+}\oplus\Gamma_{5}^{+}\oplus2\Gamma 6^{+} \)</td><td>\( \Gamma_{1}^{+}\oplus\Gamma_{3}^{+} \)</td></tr><tr><td>Infrared</td><td>\( \Gamma_{2}^{-}\oplus\Gamma 5^{-} \)</td><td>\( \Gamma_{2}^{-}\oplus\Gamma 3^{-} \)</td></tr><tr><td>Acoustic</td><td>\( \Gamma_{2}^{-}\oplus\Gamma 5^{-} \)</td><td>\( \Gamma_{2}^{-}\oplus\Gamma 3^{-} \)</td></tr><tr><td>Silent</td><td>\( 2\Gamma_{3}^{+}\oplus\Gamma 4^{-}\oplus1\Gamma 6^{-} \)</td><td>-</td></tr></table>

For the 2D polytypes, the Raman and IR active modes show symmetry variations depending on the number of layers, since the high-symmetry  \( \Gamma \)  points have different GWV.
 

The GWV at the  \( \Gamma \)  point is  \( D_{3h}^{1} \)  for N-odd 2H polytypes,  \( D_{3d}^{3} \)  for N-even 2H polytypes, and  \( D_{3d}^{3} \)  for the N-even and N-odd 1T polytype. The total number of modes for N even or N odd layers in the 2H and 1T polytypes, including their classification as Raman active, IR active, acoustic, and silent modes, are given in Tables VIII and IX, respectively.

TABLE VIII. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for the N-layer TMDCs at the  \( \Gamma \)  point within the 2Ha and 2Hc polytypes. Raman active, infrared active, acoustic and silent mode irreducible representations are identified.

<table><tr><td colspan="3">2Ha and 2Hc polytypes</td></tr><tr><td></td><td>N odd</td><td>N even</td></tr><tr><td>\( \Gamma^{vib} \)</td><td>\( \frac{(3N-1)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{-})\oplus(\frac{3N+1}{2})(\Gamma_{3}^{+}\oplus\Gamma_{2}^{-}) \)</td><td>\( \frac{(3N)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}\oplus\Gamma_{\bar{2}}^{-}\oplus\Gamma_{3}^{-}) \)</td></tr><tr><td>Raman</td><td>\( \frac{(3N-1)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{-}\oplus\Gamma_{2}^{+}) \)</td><td>\( \frac{3N}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}) \)</td></tr><tr><td>Infrared</td><td>\( \frac{(3N-1)}{2}(\Gamma_{3}^{+}\oplus\Gamma_{2}^{-}) \)</td><td>\( \frac{(3N-2)}{2}(\Gamma_{2}^{-}\oplus\Gamma_{3}^{-}) \)</td></tr><tr><td>Acoustic</td><td>\( \Gamma_{3}^{+}\oplus\Gamma_{2}^{-} \)</td><td>\( \Gamma_{2}^{-}\oplus\Gamma_{3}^{-} \)</td></tr><tr><td>Silent</td><td>-</td><td>-</td></tr></table>

TABLE IX. Normal vibrational mode irreducible representations ( \( \Gamma^{vib} \) ) for the N-layer TMDCs at the  \( \Gamma \)  point within the 1T-polytype. Raman active, infrared active, acoustic and silent mode irreducible representations are identified.

<table><tr><td colspan="3">1T polytype</td></tr><tr><td></td><td>N odd</td><td>N even</td></tr><tr><td>\( \Gamma^{vib} \)</td><td>\( \frac{(3N-1)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+})\oplus(\frac{3N+1}{2})(\Gamma_{2}^{-}\oplus\Gamma_{3}^{-}) \)</td><td>\( \frac{(3N)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}\oplus\Gamma_{\bar{2}}^{-}\oplus\Gamma_{3}^{-}) \)</td></tr><tr><td>Raman</td><td>\( \frac{(3N-1)}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}) \)</td><td>\( \frac{3N}{2}(\Gamma_{1}^{+}\oplus\Gamma_{3}^{+}) \)</td></tr><tr><td>Infrared</td><td>\( \frac{(3N-1)}{2}(\Gamma_{2}^{-}\oplus\Gamma_{3}^{-}) \)</td><td>\( \frac{(3N-2)}{2}(\Gamma_{2}^{-}\oplus\Gamma_{3}^{-}) \)</td></tr><tr><td>Acoustic</td><td>\( \Gamma_{2}^{-}\oplus\Gamma_{3}^{-} \)</td><td>\( \Gamma_{2}^{-}\oplus\Gamma_{3}^{-} \)</td></tr><tr><td>Silent</td><td>-</td><td>-</td></tr></table>

In the 1T polytype, since the space group is the same in both N-even and N-odd, the representations for the few-TL films of this polytype refer to the same irreducible representations of the group of the wave vector  \( D_{3d}^{3} \)  at the  \( \Gamma \)  point, which, in turn, are the same as those found for its bulk counterpart.

## F. Raman tensors

To define whether or not a specific vibrational mode will be experimentally observed in a given Raman scattering geometry, we use here the Porto notation, \( ^{45,46} \)  which indicates the crystal orientation with respect to the polarization and propagation directions of the laser.
 

Four letters are used in the Porto notation to describe the scattering process in the a(bc)d form: while “a” and “d” are the propagation directions of the incident and scattered light, respectively, “b” and “c” represent the polarization directions for the incident and scattered light, respectively. One common Raman experimental geometry is the backscattering configuration, where the incident and scattered light have an opposite sense. For example, in the  \( \overline{z}(xy)z \)  configuration the  \( \overline{{z}} \)  and z are the directions of the incident and scattered light, with the opposite sense, x is the polarization direction of the incident light, and y is the polarization direction of scattering.

The Raman scattering intensity given by the Hamiltonian perturbation term is proportional to  \( |\widehat{e}_{s} \cdot \overrightarrow{\alpha} \widehat{e}_{i}|^{2} \) , where  \( \widehat{e}_{s} \)  is the unit vector along the polarization direction of the scattered light,  \( \widehat{e}_{i} \)  is the unit vector along the polarization direction of the incident light, and  \( \overleftrightarrow{\alpha} \)  is the Raman tensor. The quadratic functions  \( (xx, xy, xz, yz \ldots) \)  indicate the irreducible representations for the Raman-active modes. Following this procedure, the Raman tensors for all the Raman active modes of N-layer thin films can be found. For the 2H polytype with N-odd few layers ( \( D_{3h}^{1} \)  group of the wave vector for the  \( \Gamma \)  point), the Raman tensors are: \( ^{47} \) 

 \[ \Gamma_{1}^{+}(A_{1}^{\prime}):\begin{pmatrix}a&0&0\\ 0&a&0\\ 0&\mathbf{0}&b\end{pmatrix}, \] 

 \[ \Gamma_{3}^{+}(E^{\prime})_{(x)}:\begin{pmatrix}d&0&0\\ 0&-d&0\\ 0&0&0\end{pmatrix},\quad\Gamma_{3}^{+}(E^{\prime})_{(y)}:\begin{pmatrix}0&-d&0\\ -d&0&0\\ 0&0&0\end{pmatrix}, \] 

 \[ \Gamma_{3}^{-}(E^{\prime\prime}):\begin{pmatrix}0&0&-c\\ 0&0&0\\ -c&0&0\end{pmatrix},\quad\begin{pmatrix}0&0&0\\ 0&0&c\\ 0&c&0\end{pmatrix}. \] 

For the N-even 2H polytype, and for the N even or odd for the 1T polytype, as well as for the 1T bulk crystal ( \( D_{3d}^{3} \)  group of the wave vector for the  \( \Gamma \)  point), the Raman tensors are: \( ^{47} \)
 

 \[ \Gamma_{1}^{+}(A_{1g}):\begin{pmatrix}{{{a}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{a}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{b}}} \\\end{pmatrix}, \] 

 \[ \Gamma_{3}^{+}(E_{g})_{(1)}:\begin{pmatrix}{{{c}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{-c}}}&{{{d}}} \\{{{0}}} &{{{d}}}&{{{0}}}\end{pmatrix}\quad\Gamma_{3}^{+}(E_{g})_{(2)}:\begin{pmatrix}{{{0}}}&{{{-c}}}&{{{-d}}} \\{{{-c}}}&{{{0}}}&{{{0}}} \\{{{-d}}}&{{{0}}} &{{{0}}}\end{pmatrix}. \] 

For the non-symmorphic space group for the bulk 2H polytype, the Raman tensors are: \( ^{47} \) 

 \[ \Gamma_{1}^{+}(A_{1g}):\begin{pmatrix}{{{a}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{a}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{b}}} \\\end{pmatrix}, \] 

 \[ \Gamma_{5}^{+}(E_{1g}):\begin{pmatrix}{{{0}}}&{{{0}}}&{{{0}}}\end{pmatrix},\quad\begin{pmatrix}{{{0}}}&{{{0}}}&{{{-c}}} \\{{{0}}}&{{{0}}}}&{{{0}}} \\{{{-c}}}&{{{0}}}&{{{0}}}\end{pmatrix} \] 

 \[ \Gamma_{6}^{+}(E_{2g}):\begin{pmatrix}{{{d}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{-d}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{00}}}&{{{0}}}\end{pmatrix},\quad\begin{pmatrix}{{{0}}}&{{{-d}}}&{{{0}}} \\{{{-d}}}&{{{{0}}}}&{{{0}}} \\{{{0}}}&{{{00}}}&{{{0}}}\end{pmatrix}. \] 

## III. SUMMARY AND DISCUSSIONS

In this work, symmetry-related aspects of bulk and N-layer 2Ha, 2Hc and 1T TMDCs polytypes were discussed from a group theory perspective. The analysis of the presence of inversion symmetry gives different behaviors (in the case of odd number of TLs) for the same number of layers in a given material, with different polytypes. Therefore, it is possible to design experiments to probe, for example, the presence of different polytypes within the same sample, with the same number of layers. The breaking of inversion symmetry is crucial in materials suitable for specific applications, like the development of valleytronic devices, and group theory predictions give directions to researches on how to design their devices to achieve their desired symmetry-related goals.

Some perturbations can lower the symmetry of these thin films and this approach has been used to tune some characteristics of these materials. In strained  \( MoS_{2} \)  monolayer,
 

where the doubly degenerate Raman active mode  \( E^{\prime} \)  splits into  \( E^{\prime-} \)  and  \( E^{\prime+} \)  peaks (depending on the magnitude and symmetry of the strain), an optical band gap was found and it is approximately linear with strain for both monolayer and bilayer  \( MoS_{2} \)  \( ^{30,31,48} \) . By using different TMDCs, it is possible to engineer the optical band gap of interest to the researcher. Another possibility is the piling of different TMDCs to engineer new heterostructures, where the inversion symmetry is broken with more options made available by using multiple materials. Such heterostructures are expected, for example, to give rise to tunable band gaps from 0.79 to 1.16 eV. \( ^{9} \) 

In the present work, the symmetry properties of the vibrational modes were found for the high symmetry points and lines in the BZ, extending previous knowledge beyond the zone center phonons in TMDCs. One important aspect of this symmetry analysis is that, from symmetry variations, it is possible to predict the difference in phonon modes in these structures. N new Raman-active modes have been observed in few layers TMDCs like in  \( WSe_{2} \) . \( ^{24} \)  Density functional theory (DFT) combined with polarization dependent Raman measurements and group theory were used to understand the first-order Raman spectra. For example, the appearance of the inactive mode  \( B_{2g}^{1} \)  in bulk  \( WSe_{2} \)  and only at specific laser lines is still not well understood and is usually attributed to resonance effects. \( ^{24} \)  However, for N even and N odd few layers,  \( A_{1g} \)  (for N even TLs) and  \( A_{1}^{\prime} \)  (for N odd TLs) are both observed at  \( 310 \, cm^{-1} \) . Furthermore, the  \( E_{1g} \)  mode at around  \( 175 \, cm^{-1} \)  in bulk  \( WSe_{2} \)  (2Hc polytype) is not measurable under the backscattering configuration along the z direction of light propagation, as well as the  \( E^{\prime\prime} \)  mode for 1TL of the same polytype (see the Raman tensors in section II F). In films with  \( N \geq 2 \) , the  \( E^{\prime\prime} \)  mode develops into  \( E_{g} \)  symmetry, for N-even TLs, and into  \( E^{\prime} \)  modes for N-odd layers, which are both detectable under  \( \overline{z}(xx)z \)  and  \( \overline{z} (xy)z \)  polarizations (and these different behaviors are not related to substrate effects, since these modes are also detected in suspended samples). \( ^{24} \)  The mode at  \( 260 \, cm^{-1} \)  in bulk was previously attributed to the Raman active out-of-plane  \( A_{1g} \)  mode, but polarization measurements have shown that even for  \( \overline{z}(xy)z \)  polarization this mode is observed, in contrast with the group theoretical prediction and the previous symmetry assignment. This mode was consequently attributed to second-order Raman scattering. \( ^{24} \)  Similar results were observed for  \( MoTe_{2} \)  \( ^{25} \)  and are expected for other TMDCs. The complete group theory analysis described here should be used to guide researchers in making correct mode assignments using the tables and discussion given in the present work.
 

Acknowledgments The authors acknowledge financial support from CNPq grant 551953/2011-0 and NSF grant DMR-1004147. L.G.C. and A.J. acknowledge support from FAPEMIG.

 \( ^{*} \)  Author to whom correspondence should be addressed: jenainassoares2@gmail.com

 \( ^{1} \)  K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Science 306, 666 (2004).

 \( ^{2} \)  M. I. Katsnelson, K. S. Novoselov, and A. K. Geim, Nat. Phys. 2, 620 (2006).

 \( ^{3} \)  H. Zhang, C. X. Liu, X. L. Qi, X. Dai, Z. Fang, and S. C. Zhang, Nat. Phys. 5, 438 (2009).

 \( ^{4} \)  K. K. Kim, A. Hsu, X. Jia, S. M. Kim, Y. Shi, M. Hofmann, D. Nezich, J. F. Rodriguez-Nieva, M. Dresselhaus, T. Palacios, et al., Nano Lett. 12, 161 (2011).

 \( ^{5} \)  A. Splendiani, L. Sun, Y. Zhang, T. Li, J. Kim, C.-Y. Chim, G. Galli, and F. Wang, Nano Lett. 10, 1271 (2010).

 \( ^{6} \)  H. R. Gutiérrez, N. Perea-López, A. L. Elías, A. Berkdemir, B. Wang, R. Lv, F. López-Urías, V. Crespi, H. Terrones, and M. Terrones, Nano Lett. 13, 3447 (2012).

 \( ^{7} \)  P. Tonndorf et al., Opt. Express 21, 4908 (2013).

 \( ^{8} \)  A. K. Geim and I. V. Grigorieva, Nature 499, 419 (2013).

 \( ^{9} \)  H. Terrones, F. López-Urías, and M. Terrones, Sci. Rep. 3, 1549 (2013).

 \( ^{10} \)  H. Fang et al., P. Natl. Acad. Sci. USA 111, 6198 (2014).

 \( ^{11} \)  M. Chhowalla, H. S. Shin, G. Eda, L. J. Li, K. P. Loh, and H. Zhang, Nature Chem. 5, 263 (2013).

 \( ^{12} \)  Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, Nat. Nanotechnol. 7, 699 (2012).

 \( ^{13} \)  S. Z. Butler, S. M. Hollen, L. Cao, Y. Cui, J. A. Gupta, H. R. Gutiérrez, T. F. Heinz, S. S. Hong, J. Huang, A. F. Ismach, et al., ACS Nano 7, 2898 (2013).

 \( ^{14} \)  J. C. Shaw, H. Zhou, Y. Chen, N. O. Weiss, Y. Liu, Y. Huang, and X. Duan, “Chemical vapor deposition growth of monolayer  \( MoSe_{2} \)  nanosheets,” http://www.thenanoresearch.com/upload/justPDF/0417.pdf (2014), to be published.

 \( ^{15} \)  H. Sahin, S. Tongay, S. Horzum, W. Fan, J. Zhou, J. Li, J. Wu, and F. M. Peeters, Phys. Rev. B 87, 165409 (2013).
 

 \( ^{16} \)  L. Britnell, R. M. Ribeiro, A. Eckmann, R. Jalil, B. D. Belle, A. Mishchenko, Y. J. Kim, R. V. Gorbachev, T. Georgiou, S. V. Morozov, et al., Science 340, 1311 (2013).

 \( ^{17} \)  D. Xiao, G. B. Liu, W. Feng, X. Xu, and W. Yao, Phys. Rev. Lett. 108, 196802 (2012).

 \( ^{18} \)  W. Yao, D. Xiao, and Q. Niu, Phys. Rev. B 77, 235406 (2008).

 \( ^{19} \)  T. Cao, G. Wang, W. Han, H. Ye, C. Zhu, J. Shi, Q. Niu, P. Tan, E. Wang, B. Liu, et al., Nat. Commun. 3, 887 (2012).

 \( ^{20} \)  K. F. Mak, K. He, J. Shan, and T. F. Heinz, Nature Nanotech. 7, 494 (2012).

 \( ^{21} \)  H. Zeng, G. B. Liu, J. Dai, Y. Yan, B. Zhu, R. He, L. Xie, S. Xu, X. Chen, W. Yao, and X. Cui, Scientific Reports 3 (2013).

 \( ^{22} \)  X. Xu, W. Yao, D. Xiao, and T. F. Heinz, Nature Phys. 10, 343 (2014).

 \( ^{23} \)  Y. Zhao, X. Luo, H. Li, J. Zhang, P. T. Araujo, C. K. Gan, J. Wu, H. Zhang, S. Y. Quek, M. S. Dresselhaus, et al., Nano Lett. 13, 1007 (2013).

 \( ^{24} \)  X. Luo, Y. Zhao, J. Zhang, M. Toh, C. Kloc, Q. Xiong, and S. Y. Quek, Phys. Rev. B 88, 195313 (2013).

 \( ^{25} \)  M. Yamamoto, S. T. Wang, M. Ni, Y.-F. Lin, S.-L. Li, S. Aikawa, W.-B. Jian, K. Ueno, K. Wakabayashi, and K. Tsukagoshi, ACS Nano 8, 3895 (2014).

 \( ^{26} \)  L. M. Malard, T. V. Alencar, A. P. M. Barboza, K. F. Mak, and A. M. de Paula, Phys. Rev. B 87, 201401(R) (2013).

 \( ^{27} \)  Y. Li, Y. Rao, K. F. Mak, Y. You, S. Wang, C. R. Dean, and T. F. Heinz, Nano Lett. 13, 3329 (2013).

 \( ^{28} \)  N. Kumar, S. Najmaei, Q. Cui, F. Ceballos, P. M. Ajayan, J. Lou, and H. Zhao, Physical Review B 87, 161403(R) (2013).

 \( ^{29} \)  X. Yin, Z. Ye, D. A. Chenet, Y. Ye, K. O'Brien, J. C. Hone, and X. Zhang, Science 344, 488 (2014).

 \( ^{30} \)  H. J. Conley, B. Wang, J. I. Ziegler, R. F. Haglund Jr., S. T. Pantelides, and K. I. Bolotin, Nano Lett. 13, 3626 (2013).

 \( ^{31} \)  Y. Wang, C. Cong, C. Qiu, and T. Yu, Small 9, 2857 (2013).

 \( ^{32} \)  J. A. Wilson and A. D. Yoffe, Adv. Phys. 18, 193 (1969).

 \( ^{33} \)  H. Katzke, P. Tolédano, and W. Depmeier, Phys. Rev. B. 69, 134111 (2004).

 \( ^{34} \)  A. Kormányos, V. Zólyomi, N. D. Drummond, P. Rakyta, G. Burkard, and V. I. Fal'ko, Phys. Rev. B 88, 045416 (2013).
 

 \( ^{35} \)  T. Hahn, ed., International Tables for Crystallography, 5th ed., Vol. A: Space-Group Symmetry (Springer, Dordrecht, The Netherlands, 2005).

 \( ^{36} \)  L. Hromadová, R. Martonák, and E. Tosatti, Phys. Rev. B 87, 144105 (2013).

 \( ^{37} \)  M. Tinkham, Group Theory and Quantum Mechanics (Dover Publications, Mineola, New York, 2012).

 \( ^{38} \)  M. S. Dresselhaus, G. Dresselhaus, and A. Jorio, Group Theory: Application to the Physics of Condensed Matter (Springer-Verlag Berlin, Heidelberg, Germany, 2008).

 \( ^{39} \)  P. W. M. Jacobs, Group Theory with Applications in Chemical Physics (Cambridge University Press, New York, 2005).

 \( ^{40} \)  L. M. Malard, M. H. D. Guimarães, D. L. Mafra, M. S. C. Mazzoni, and A. Jorio, Phys. Rev. B 79, 125426 (2009).

 \( ^{41} \)  W. T. Hsu, Z. A. Zhao, L. J. Li, C. H. Chen, M. H. Chiu, P. S. Chang, Y. C. Chou, and W. H. Chang, ACS Nano 8, 2951 (2014).

 \( ^{42} \)  R. W. Boyd, Nonlinear Optics (Academic, Burlington, MA, USA, 2008).

 \( ^{43} \)  Y. R. Shen, The Principles of Nonlinear Optics (John Wiley & Sons, Hoboken, New Jersey, 2003).

 \( ^{44} \)  See Supplementary Material at http://www.html (2014), (insert correct link here) for character tables (with the notation conversion from space group to point group, for all the GWV used in this work) and for tables for the irreducible representations for lattice vibrations ( \( \Gamma^{vib} \) ) for bulk 2H and 1T polytypes.

 \( ^{45} \)  B. C. Server, http://www.cryst.ehu.es/cgi-bin/cryst/programs/nph-doc-raman (accessed: 03/30/2014).

 \( ^{46} \)  T. C. Damen, S. P. S. Porto, and B. Tell, Phys. Rev. 142, 570 (1966).

 \( ^{47} \)  B. C. Server, http://www.cryst.ehu.es/cryst/transformtensor.html (accessed: 03/30/2014).

 \( ^{48} \)  A. Castellanos-Gomez, R. Roldán, E. Cappelluti, M. Buscema, F. Guinea, H. S. J. van der Zant, and G. A. Steele, Nano Lett. 13, 5361 (2013).
 

Supplementary Material to “Group Theory analysis of two-dimensional Transition Metal Dichalcogenides”

J. Ribeiro-Soares \( ^{1,2,*} \) , R. M. Almeida \( ^{1} \) , E. B. Barros \( ^{2,3} \) , P. T. Araujo \( ^{4} \) , M. S. Dresselhaus \( ^{2,5} \) , L. G. Cançado \( ^{1} \)  and A. Jorio \( ^{1} \) 

 \( ^{1} \) Departamento de Física, Universidade Federal de Minas Gerais, Belo Horizonte, MG, 30123-970, Brazil

 \( ^{2} \) Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology (MIT), Cambridge, MA 02139, USA

 \( ^{3} \) Departamento de Física, Universidade Federal do Ceará, Fortaleza, CE, 60455-900, Brazil

 \( ^{4} \) Department of Physics and Astronomy, University of Alabama, Tuscaloosa, Alabama 35487, USA

 \( ^{5} \) Department of Physics, Massachusetts Institute of Technology (MIT), Cambridge, MA 02139, USA

 \( ^{*} \) Author to whom correspondence should be addressed: jenainassoares2@gmail.com
 

## Contents

I. Lattice vibration representations for bulk 2Ha, 2Hc and 1T

II. Character tables of spatial groups modified to the group of wave vector (GWW) of each point and line of high symmetry in the BZ.

1. Spacial groups used for bulk of the 2H polytope

2. Spacial groups used for N-odd few layers of the 2H polytope

3. Spacial groups used for N-even few layers of the 2H polytope and for N layer and bulk 1T polytope
 

## I. Lattice vibration representations for bulk 2Ha, 2Hc and 1T

In this appendix we list the lattice vibration irreducible representations  \( \Gamma^{vib} \)  (discussed in section II D of the main manuscript) for each high-symmetry point and line in the BZ for the bulk 2Ha, 2Hc and 1T polytypes in Tables S I, S II and S III, respectively. The character tables of spacial groups modified to the GWV of each high-symmetry point and line of BZ are given with respect to the points and lines indicated in red in Fig. 4 of the main manuscript.

TABLE S I. Wave-vector point-group representations ( \( \Gamma^{vib} \) ) for the bulk of 2Ha-polytype (/AbA CbC/) TMDCs for all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="2">2Ha-polytype (/AbA CbC/)</td></tr><tr><td>BZ point</td><td>Irreducible representation</td></tr><tr><td>\( \Gamma \)</td><td>\( \Gamma_{1}^{+} \oplus 2\Gamma_{3}^{+} \oplus \Gamma_{5}^{+} \oplus 2\Gamma_{6}^{+} \oplus 3\Gamma_{2}^{-} \oplus \Gamma_{4}^{-} \oplus 2\Gamma_{5}^{-} \oplus \Gamma_{6}^{-} \)</td></tr><tr><td>K</td><td>\( K_{1}^{+} \oplus K_{2}^{+} \oplus 4K_{3}^{+} \oplus 2K_{1}^{-} \oplus 2\K_{2}^{-} \oplus 3K_{3}^{-} \)</td></tr><tr><td>M</td><td>\( 3M_{1}^{+} \oplus 2M_{2}^{+} \oplus 3M_{3}^{+} \oplus M_{4}^{+} \oplus M^{-}_{1} \oplus 3M_{2}^{-} \oplus 2M_{3}^{-} \oplus 3M_{4}^{-} \)</td></tr><tr><td>\( \Sigma \)</td><td>\( 6\Sigma_{1} \oplus 2\Sigma_{2} \oplus 4\Sigma_{3} \oplus 6\Sigma_{4} \)</td></tr><tr><td>\( T(T&#x27;) \)</td><td>\( 5T_{1} \oplus 4T_{2} \oplus 5T_{3} \oplus 4T_{4} \)</td></tr><tr><td>u</td><td>\( 10u^{+} \oplus 8u^{-} \)</td></tr></table>

TABLE S II. Wave-vector point-group representations ( \( \Gamma^{vib} \) ) for the bulk of 2Hc-polytype (/CaC AcA/) TMDCs for all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="2">2Hc-polytype (/CaC AcA/)</td></tr><tr><td>BZ point</td><td>Irreducible representation</td></tr><tr><td>\( \Gamma \)</td><td>\( \Gamma_{1}^{+} \oplus 2\Gamma_{3}^{+} \oplus \Gamma_{5}^{+} \oplus 2\Gamma_{6}^{+} \oplus 3\Gamma_{2}^{-} \oplus \Gamma_{4}^{-} \oplus 2\Gamma_{5}^{-} \oplus \Gamma_{6}^{-} \)</td></tr><tr><td>K</td><td>\( 2K_{1}^{+} \oplus 2K_{2}^{+} \oplus 3K_{3}^{+} \oplus K_{1}^{-} \oplus K_{2}^{-} \oplus 3K_{3}^{-} \)</td></tr><tr><td>M</td><td>\( 3M_{1}^{+} \oplus 2M_{2}^{+} \oplus 3M_{3}^{+} \oplus M_{4}^{+} \oplus M^{-}_{1} \oplus 3M_{2}^{-} \oplus 2M_{3}^{-} \oplus 3M_{4}^{-} \)</td></tr><tr><td>\( \Sigma \)</td><td>\( 6\Sigma_{1} \oplus 2\Sigma_{2} \oplus 4\Sigma_{3} \oplus 6\Sigma_{4} \)</td></tr><tr><td>\( T(T&#x27;) \)</td><td>\( 5T_{1} \oplus 4T_{2} \oplus 5T_{3} \oplus 4T_{4} \)</td></tr><tr><td>u</td><td>\( 10u^{+} \oplus 8u^{-} \)</td></tr></table>
 

TABLE S III. Wave-vector point-group representations ( \( \Gamma^{vib} \) ) for the bulk of 1T-polytpe (/AbC/AbC/) TMDCs for all the high-symmetry points and lines in the BZ.

<table><tr><td colspan="2">1T-polytpe (/AbC/AbC/)</td></tr><tr><td>BZ point</td><td>Irreducible representation</td></tr><tr><td>\( \Gamma \)</td><td>\( \Gamma_{1}^{+} \oplus \Gamma_{3}^{+} \oplus 2\Gamma_{2}^{-} \oplus 2 \Gamma_{3}^{-} \)</td></tr><tr><td>K</td><td>\( K_{1} \oplus 2K_{2} \oplus 3K_{3} \)</td></tr><tr><td>M</td><td>\( 2M_{1}^{+} \oplus 2M_{1}^{-} \oplus M_{2}^{+} \oplus 4M_{2}^{-} \)</td></tr><tr><td>\( \Sigma \)</td><td>\( 6\Sigma_{1} \oplus 3\Sigma_{2} \)</td></tr><tr><td>\( T(T&#x27;) \)</td><td>\( 4T_{1} \oplus 5T_{2} \)</td></tr><tr><td>u</td><td>9u</td></tr></table>

II. Character tables of spacial groups modified to the group of the wave vector (GWV) of each point and line of high symmetry in the BZ.

Tables S IV to S IX give the character tables for the GWV for the 2Ha and 2Hc bulk polytpes. Tables S X to S XV give the character tables to the GWV for the 2H polytpe with N-odd layers, while Tables S XVI to S XX give the character tables for the GWV for the 2H polytpe with N-even layers. The space group for the 1T bulk polytpe, as well as that for N-even and N-odd layers (the 1T bulk polytpe is symmorphic) is the  \( P\bar{3}m1 \)  ( \( D_{3d}^{3} \)  or #164) and the GWV for each high-symmetry point or line in the BZ is the same, regardless of the number of layers. The GWV for each high-symmetry point or line in the BZ for the 1T polytpe is the same as that which occurs in the 2H polytpe with an even number of layers, and the Tables S XVI to S XX should be used for this polytpe. The tables contain the Space Group (SG) and Point Group (PG) notation for the irreducible representations, and they are given in the following order:

1. Spacial groups used for bulk of the 2H polytpe

2. Spacial groups used for N-odd few layers of the 2H polytpe

3. Spacial groups used for N-even few layers of the 2H polytpe and for N layer and bulk 1T polytpe.
 

TABLE S VI. Character table for the \(M\) point \([D_{2h}^{17} (Cmcm, \#63)]\).

<table><tr><td>SG</td><td>PG</td><td>\( \{E|0\} \)</td><td>\( \{C_{2}|\tau\}^{a} \)</td><td>\( \{ C_{2}^{\prime A}|0\} \)</td><td>\( \{C_{2}^{\prime\prime A}|0\} \)</td><td>\{i|0\}</td><td>\( \{\sigma_{h}|0\} \)</td><td>\( \{\tau_{d}^{A}|0\} \)</td><td>\{ \tau_{v}^{A}|\tau\}^{a}</td><td>Bases</td></tr><tr><td>\( M_{1}^{+} \)</td><td>\( A_{g} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>\( x^{2}, y^{2}, z^{2} \)</td></tr><tr><td>\( M_{2}^{+} \)</td><td>\( B_{1g} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>11</td><td>-1</td><td>11</td><td>xy</td></tr><tr><td>\( M_{3}^{+} \)</td><td>\( B_{2g} \)</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>11</td><td>-1</td><td>11</td><td>11</td><td>xz</td></tr><tr><td>\( M_{4}^{+} \)</td><td>\( B_{3g} \)</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>11</td><td>-1</td><td>11</td><td>11</td><td>yz</td></tr><tr><td>\( M_{1}^{-} \)</td><td>\( A_{u} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>11</td><td>-1</td><td>1</td><td>11</td><td>1</td></tr><tr><td>\( M_{2}^{-} \)</td><td>\( B_{1u} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>11</td><td>-1</td><td>1</td><td>11</td><td>z</td></tr><tr><td>\( M_{3}^{-} \)</td><td>\( B_{2u} \)</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>11</td><td>-1</td><td>11</td><td>11</td><td>y</td></tr><tr><td>\( M_{4}^{-} \)</td><td>\( B_{3u} \)</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>11</td><td>1</td><td>1</td><td>-1</td><td>x</td></tr></table>

 \( ^{a}\tau \)  is the translation of half of the c lattice parameter along the  \( \hat{z} \)  direction ( \( \tau = (\frac{1}{2})c\hat{z} \) ).

TABLE S VII. Character table for the  \( T(T') \)  line  \( [C_{2v}^{16} (Ama2, \#40)] \) .

<table><tr><td>SG</td><td>PG</td><td>\( \{E|0\} \)</td><td>\( \{C_{2}^{\prime A}|0\} \)</td><td>\{ \( \sigma_{h}|0\} \)</td><td>\( \{\sigma_{v}^{A}|\tau\}^{a} \)</td><td>Bases</td></tr><tr><td>\( T_{1} \)</td><td>\( A_{1} \)</td><td>1</td><td>1</td><td>11</td><td>11</td><td>\( y, x^{2}, y^{2}, z^{2} \)</td></tr><tr><td>\( T_{2} \)</td><td>\( A_{2} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>xz</td></tr><tr><td>\( T_{3} \)</td><td>\( B_{1} \)</td><td>1</td><td>-1</td><td>11</td><td>-1</td><td>x, xy</td></tr><tr><td>\( T_{4} \)</td><td>\( B_{2} \)</td><td>1</td><td>-1</td><td>-1</td><td>11</td><td>z, yz</td></tr></table>

 \( ^{a}\tau \)  is the translation of half of the c lattice parameter along the  \( \hat{z} \)  direction ( \( \tau = (\frac{1}{2})c\hat{z} \) ).

TABLE S VIII. Character table for the  \( \Sigma \)  line  \( [C_{2v}^{14} (Amm2, \#38)] \) .

<table><tr><td>SG</td><td>PG</td><td>\( \{E|0\} \)</td><td>\( \{C_{2}^{\prime\prime A}|0\} \)</td><td>\{ \( \sigma_{h}|0\} \)</td><td>\( \{\sigma_{d}^{A}|0\} \)</td><td>Bases</td></tr><tr><td>\( \Sigma_{1} \)</td><td>\( A_{1} \)</td><td>1</td><td>1</td><td>11</td><td>11</td><td>\( x, x^{2}, y^{2}, z^{2} \)</td></tr><tr><td>\( \Sigma_{2} \)</td><td>\( A_{2} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>yz</td></tr><tr><td>\( \Sigma_{3} \)</td><td>\( B_{1} \)</td><td>1</td><td>-1</td><td>11</td><td>-1</td><td>y, xy</td></tr><tr><td>\( \Sigma_{4} \)</td><td>\( B_{2} \)</td><td>1</td><td>-1</td><td>-1</td><td>11</td><td>z, xz</td></tr></table>
 

TABLE S IX. Character table for the u point  \( [C_{s}^{xy} \)  or  \( C_{s}^{1} \) ,  \( Pm, \#6] \) . The  \( \sigma_{h} \)  mirror plane lies in the xy plane.

<table><tr><td>SG</td><td>PG</td><td>\( \{E|0\} \)</td><td>\( \{\sigma_{h}|0\} \)</td><td>Bases</td></tr><tr><td>\( u^{+} \)</td><td>\( A&#x27; \)</td><td>1</td><td>1</td><td>\( x, y, x^{2}, y^{2}, z^{2}, xy \)</td></tr><tr><td>\( u^{-} \)</td><td>\( A&#x27;&#x27; \)</td><td>1</td><td>-1</td><td>\( z, yz, xz \)</td></tr></table>
 

## 2. Spacial groups used for N-odd few layers of the 2H polytpe

TABLE S X. Character table for the  \( \Gamma \)  point  \( [D_{3h}^{1} \)  ( \( P\bar{6}m2 \) ,  \( \#187) \) ].

<table><tr><td></td><td></td><td></td><td></td><td>C2A</td><td></td><td></td><td>σA</td><td></td></tr><tr><td></td><td></td><td></td><td>C3+</td><td>C2B</td><td></td><td>S3−</td><td>σB</td><td></td></tr><tr><td>SG</td><td>PG</td><td>E</td><td>C3−</td><td>C2C</td><td>σh</td><td>S3+</td><td>σC</td><td>Bases</td></tr><tr><td>Γ1+</td><td>A1′</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td>x2+y2,z2</td></tr><tr><td>Γ2+</td><td>A2′</td><td>1</td><td>1</td><td>−1</td><td></td><td>1</td><td></td><td>−1</td></tr><tr><td>Γ3+</td><td>E′</td><td>2</td><td>−1</td><td></td><td>0</td><td>2</td><td></td><td>0</td></tr><tr><td>Γ1−</td><td>A1′</td><td>1</td><td></td><td>1</td><td></td><td>−1</td><td></td><td>0</td></tr><tr><td>Γ2−</td><td>A2′</td><td>1</td><td></td><td>1</td><td></td><td>−1</td><td></td><td>0</td></tr><tr><td>Γ3−</td><td>E′′</td><td>2</td><td></td><td>−1</td><td></td><td>0</td><td></td><td>0</td></tr></table>

TABLE S XI. Character table for the  \( K(K') \)  point  \( [C_{3h}^{1} \)  ( \( P\bar{6} \) ,  \( \#174) \) ].

<table><tr><td>SG</td><td>PG</td><td>E</td><td>C3+</td><td>C3−</td><td>σh</td><td>S3+</td><td>S3−</td><td>Bases</td></tr><tr><td>K1+</td><td>A&#x27;</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td>x2+y2,z2</td></tr><tr><td>K1−</td><td>A&#x27;&#x27;</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td>z</td></tr><tr><td>K2+</td><td>E&#x27;</td><td>1</td><td>ωa</td><td></td><td>1</td><td></td><td>ω</td><td>ω2</td></tr><tr><td>K2+*</td><td>E&#x27;*</td><td>1</td><td>ω2</td><td></td><td>1</td><td></td><td>ω2</td><td>ω</td></tr><tr><td>K2−</td><td>E&#x27;&#x27;</td><td>1</td><td>ω</td><td></td><td>ω2</td><td></td><td>−ω</td><td>−ω2</td></tr><tr><td>K2−*</td><td>E&#x27;&#x27;*</td><td>1</td><td>ω2</td><td></td><td>ω</td><td></td><td>−ω2</td><td>−ω</td></tr></table>

 \( ^{a}\omega = \exp{(2i\pi/3)} \)
 

TABLE S XII. Character for the M point  \( [C_{2v}^{14} \)  (Amm2, #38)] $ .

<table><tr><td>SG</td><td>PG</td><td>E</td><td>\( C_{2}^{\prime A} \)</td><td>\( \sigma_{h} \)</td><td>\( σ_{v}^{A} \)</td><td>Bases</td></tr><tr><td>\( M_{1} \)</td><td>\( A_{1} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>\( x, x^{2}, y^{2}, z^{2} \)</td></tr><tr><td>\( M_{2} \)</td><td>\( A_{2} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>yz</td></tr><tr><td>\( M_{3} \)</td><td>\( B_{1} \)</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>y, xy</td></tr><tr><td>\( M_{4} \)</td><td>\( B_{2} \)</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>z, xz</td></tr></table>

TABLE S XIII. Character table for the  \( T(T') \)  line  \( [C_{s}^{xy} \)  or  \( C_{s}^{1} \) , Pm, #6]. The  \( \sigma_{h} \)  mirror plane lies on xy plane.

<table><tr><td>SG</td><td>PG</td><td>E</td><td>\( \sigma_{h} \)</td><td>Bases</td></tr><tr><td>\( T^{+} \)</td><td>\( A^{\prime} \)</td><td>1</td><td>1</td><td>\( x, y, x^{2}, y^{2}, z^{2}, xy \)</td></tr><tr><td>\( T^{-} \)</td><td>\( A^{\prime\prime} \)</td><td>1</td><td>-1</td><td>\( z, yz, xz \)</td></tr></table>

TABLE S XIV. Character table for the  \( \Sigma \)  line  \( [C_{2v}^{14} \)  (Amm2, #38)] $ .

<table><tr><td>SG</td><td>PG</td><td>E</td><td>\( C_{2}^{\prime A} \)</td><td>\( \sigma_{h} \)</td><td>\( σ_{v}^{A} \)</td><td>Bases</td></tr><tr><td>\( \Sigma_{1} \)</td><td>\( A_{1} \)</td><td>1</td><td>1</td><td>-1</td><td>1</td><td>\( x, x^{2}, y^{2}, z^{2} \)</td></tr><tr><td>\( \Sigma_{2} \)</td><td>\( A_{2} \)</td><td>1</td><td>1</td><td>-1</td><td>-1</td><td>yz</td></tr><tr><td>\( \Sigma_{3} \)</td><td>\( B_{1} \)</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>y, xy</td></tr><tr><td>\( \Sigma_{4} \)</td><td>\( B_{2} \)</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>z, xz</td></tr></table>

TABLE S XV. Character table for the u point  \( [C_{s}^{xy} \)  or  \( C_{s}^{1} \) , Pm, #6]. The  \( \sigma_{h} \)  mirror lies on xy plane.

<table><tr><td>SG</td><td>PG</td><td>E</td><td>\( \sigma_{h} \)</td><td>Bases</td></tr><tr><td>\( u^{+} \)</td><td>\( A^{\prime} \)</td><td>1</td><td>1</td><td>\( x, y, x^{2}, y^{2}, z^{2}, xy \)</td></tr><tr><td>\( u^{-} \)</td><td>\( A^{\prime\prime} \)</td><td>1</td><td>-1</td><td>\( z, yz, xz \)</td></tr></table>
 

3. Spacial groups used for N-even few layers of the 2H polytpe and for N layer and bulk 1T polytpe

TABLE S XVI. Character table for the  \( \Gamma \)  point  \( [D_{3d}^{3} \)  ( \( P\bar{3}m1,\#164) \) ].

<table><tr><td></td><td></td><td></td><td></td><td>C2A</td><td></td><td></td><td>σA</td><td></td></tr><tr><td></td><td></td><td></td><td>C3+</td><td>C2B</td><td></td><td>S6+</td><td>σB</td><td></td></tr><tr><td>SG</td><td>PG</td><td>E</td><td>C3−</td><td>C2C</td><td>i</td><td>S6−</td><td>σC</td><td>Bases</td></tr><tr><td>Γ1+</td><td>A1g</td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td>x2+y2,z2</td></tr><tr><td>Γ2+</td><td>A2g</td><td>1</td><td>1</td><td>−1</td><td></td><td>1</td><td></td><td>−1</td></tr><tr><td>Γ3+</td><td>Eg</td><td>2</td><td>−1</td><td>0</td><td></td><td>2</td><td></td><td>0</td></tr><tr><td>Γ1−</td><td>A1u</td><td>1</td><td>1</td><td></td><td>−1</td><td></td><td></td><td>−11</td></tr><tr><td>Γ2−</td><td>A2u</td><td>1</td><td>1</td><td></td><td>−1</td><td></td><td></td><td>1</td></tr><tr><td>Γ3−</td><td>Eu</td><td>2</td><td>−1</td><td>0</td><td></td><td>−2</td><td></td><td>0</td></tr></table>

TABLE S XVII. Character table for the  \( K(K') \)  point  \( [D_{3}^{2} \)  (P321, #150)].

<table><tr><td></td><td></td><td></td><td></td><td>C2A</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>C3+</td><td>C2B</td></tr><tr><td>SG</td><td>PG</td><td>E</td><td>C3−</td><td>C2C</td><td>Bases</td></tr><tr><td>K1</td><td>A1</td><td>1</td><td></td><td>1</td><td>x2+y2,z2</td></tr><tr><td>K2</td><td>A2</td><td>1</td><td></td><td>1</td><td>z</td></tr><tr><td>K3</td><td>E</td><td>2</td><td></td><td>0</td><td>(xz,yz)z(x,y)(x2-y2,xy)</td></tr></table>
 

TABLE S XVIII. Character table for the M point  \( [C_{2h}^{3} \)  (C2/m, #12)].

<table><tr><td>SG</td><td>PG</td><td>E</td><td>C1A</td><td>σA</td><td>i</td><td>Bases</td></tr><tr><td>M1+</td><td>Ag</td><td>1</td><td>1</td><td></td><td>1</td><td>x2, y2, z2, xz</td></tr><tr><td>M1−</td><td>Au</td><td>1</td><td>1</td><td>−1</td><td>−1</td><td>y</td></tr><tr><td>M2+</td><td>Bg</td><td>1</td><td>−1</td><td>−1</td><td>1</td><td>xy, yz</td></tr><tr><td>M2−</td><td>Bu</td><td>1</td><td>−1</td><td>1</td><td>-1</td><td>x, z</td></tr></table>

TABLE S XIX. Character table for the  \( T(T') \)  line  \( [C_{2}^{3} \)  (C2, #5)].

<table><tr><td>SG</td><td>PG</td><td>E</td><td>C1A</td><td>Bases</td></tr><tr><td>T1</td><td>A</td><td>1</td><td>1</td><td>y, x2, y2, z2, xz</td></tr><tr><td>T2</td><td>B</td><td>1</td><td>-1</td><td>x, z, xy, yz</td></tr></table>

TABLE S XX. Character table for the  \( \Sigma \)  line  \( [C_{s}^{xz} \)  or  \( C_{s}^{3} \) ,  \( Cm, \#8] \) . The  \( \sigma \)  mirror plane lies in the xz plane.

<table><tr><td>SG</td><td>PG</td><td>E</td><td>\( \sigma_{d}^{A} \)</td><td>Bases</td></tr><tr><td>\( \Sigma_{1} \)</td><td>\( A&#x27; \)</td><td>1</td><td>1</td><td>x, z,  \( x^{2} \) ,  \( y^{2} \) , z \( ^{2} \) , xz</td></tr><tr><td>\( \Sigma_{2} \)</td><td>\( A&#x27;&#x27; \)</td><td>1</td><td>-1</td><td>y, xy, yz</td></tr></table>

TABLE S XXI. Character table for the u point  \( [C_{1}^{1} \)  (P1, #1)].

<table><tr><td>SG</td><td>PG</td><td>E</td><td>Bases</td></tr><tr><td>u</td><td>A</td><td>1</td><td>any  \( f(x,y,z) \)</td></tr></table>
 
