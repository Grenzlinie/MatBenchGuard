# Ironene – A new 2D material

Vo Van Hoang $^{a}$, Vuong Phu Tai $^{a}$, Tran Ky Thinh $^{a}$, Nguyen Hoang Giang $^{b,*}$, Le Ngoc Qui $^{c}$

$^{a}$ Comp. Physics Lab, Ho Chi Minh City Univ. of Technology, Vietnam Natl. University – HochiMinh City, Viet Nam
$^{b}$ Computational Materials Physics Research Group & Faculty of Applied Sciences, Ton Duc Thang University, 19 Nguyen Huu Tho Street, Tan Phong Ward, District 7, Ho Chi Minh City, Viet Nam
$^{c}$ Hung Thuan High School, Can Tho City, Viet Nam

---

## ARTICLE INFO

**Article history:**
Received 12 May 2016
Received in revised form 24 August 2016
Accepted 3 September 2016

**Keywords:**
2D iron
Ironene
2D metal
Solidification of 2D liquid

---

## ABSTRACT

Discovery of 2D iron with a square lattice structure suspended in pores of graphene sheet by experiment (Zhao et al., 2014) has stimulated the researches related to 2D iron and other 2D metals by both experiments and computer simulations in general. However, our understanding of structure and thermodynamics of 2D iron is completely lacking since main attention has focused on its thermal stability, magnetic behaviors and/or possibility of applications in practice. A comprehensive molecular dynamics (MD) simulation of structure and thermodynamics of 2D liquid and crystalline Fe including 'a natural formation' of 2D Fe from the liquid state is done in the present work. We find that 2D Fe with a triangle lattice structure spontaneously forms from the liquid state instead of that with a square lattice structure although a set of atomic potentials for Fe have been used in MD simulation. Both structure and thermodynamics of 2D liquid and crystalline Fe are close to those found by DFT calculations or experiments. We find that crystallization of 2D liquid Fe exhibits a first-order-like phase transition behavior and it follows classical nucleation theory.

© 2016 Published by Elsevier B.V.

---

## 1. Introduction

It is well-known that the bond between atoms in metals is mediated by conduction electrons which can move in any direction, i.e. the system has a tendency to form 3D structure rather than 2D sheet. Therefore, the formation of a free-standing 2D metal seems to be impossible. However, the situation has changed due to the recent discovery of 2D iron with a square lattice structure suspended in graphene pores via in situ low-voltage aberration-corrected TEM and supporting image simulation [1]. This is not a free-standing 2D iron sheet and the role of graphene pores for the formation of 2D iron cannot be ignored. Indeed, the dangling edge C atoms of pores in graphene are highly reactive, and therefore, mobile Fe atoms have a tendency to bond to these C atoms. Then, these Fe atoms bond to the other Fe atoms around the edge leading to the formation of 2D Fe sheet in the pores of graphene. Moreover, it is found by DFT calculations that atomic magnetic moment of 2D Fe monolayer is of around $3.1\ \mu_{B}$ which is much higher than $2.2\ \mu_{B}$ of the bulk counterpart [1]. It promises possible applications of this material for magnetic nano-electronic devices such as magnetic recording media [1]. In contrast, formation of 2D iron with a triangle lattice structure supported by graphene edges has been found by both experiment and computer simulation [2]. 2D iron sheet is called 'ironene' [2]. Here-and-after we also call it ironene. It raises a question about the most stable structure of a free-standing 2D iron: square or triangle lattice? Subsequent investigations by both experiments and computer simulations for this 2D metal can be found [3–5], including Fe-C layers with different Fe/C ratios [5] and monolayer pyrite (FeS₂) [6]. In particular, electronic structure and magnetic behaviors of graphene edge supported ironene are studied by DFT calculations, which are found to be different from those of 3D counterpart [3]. Note that the DFT-optimized model of constrained ironene has a triangle lattice not a square one unlike that found in Ref. [1]. Similarly, via DFT calculations it is found that free-standing monolayer Fe with a triangle lattice structure is more stable compared to that with both square and honeycomb ones [4]. However, embedded Fe membranes in graphene perforations can be more stable in a square lattice configuration compared to that with a triangle one. It indicates an important role of the graphene in the formation of Fe membranes with different atomic structures [4]. In addition, also via DFT calculations stability of 2D Fe-C sheets with various Fe/C ratios suspended in graphene pores is systematically studied in order to highlight the situation [5]. It is found that embedded Fe₁C₁ in graphene pores with a square lattice structure is formed instead of a pure Fe monolayer [5]. It is suggested that square lattice in graphene

---

* Corresponding author.
E-mail address: nguyenhoanggiang@tdt.edu.vn (N.H. Giang).

http://dx.doi.org/10.1016/j.commatsci.2016.09.011
0927-0256/© 2016 Published by Elsevier B.V.

pores observed previously in TEM image by Zhao et al. may be a mixture of $Fe_1C_1$ and $Fe_2C_2$ instead of pure Fe monolayer [1,5]. It is noted that C atoms near Fe ones cannot be 'seen' in TEM images because of a large different contrast of atoms of two elements [5]. In contrast, it is found that monolayer $FeS_2$ with several atomic thicknesses constructed by cleaving from the bulk exhibits a square lattice structure and advanced magnetic behaviors [6]. A large number of studies related to the Fe monolayer supported on various substrates can be found (see for example [7,8]). However, it is not a real 2D iron due to strong substrate effects and it maybe a multilayer, not a single one. Therefore, it is out of scope of our paper and we do not pay more attention on Fe monolayer on substrate in the present work.

Besides ironene, 2D membranes of various metals or alloys have been under much attention due to their enormous importance in science and technology (see for example [9-18]). In particular, ultrathin Rh nanosheets with the thickness less than $4\ \mathring{A}$ containing some planar 2D Rh monolayers have been found by experiment and DFT calculations [9]. The existence of 2D liquid Au membrane suspended in graphene pores has been studied based on quantum MD and density-functional-tight-binding (DFTB) methods [10]. Planar stability of Au membrane is suggested due to relativistic effects and existence of 2D liquid Au membrane shows an extreme fluxionality of metal nanostructures in general [10]. DFT calculations and ab initio MD simulation also predict the stability of free-standing 2D solid Ag and Au monolayers which exhibit a hexagonal close-packed atomic structure [13,14]. It is found that 2D solid Ag monolayer is stable in ab MD simulations for 10 ps up to 800 K while Au monolayer is stable for the same annealing time up to a much higher temperature of 1400 K [14]. Similarly, the early melting stages of free-standing Pt, Ag, Au and Cu monolayers have been studied based on quantum calculation methods [17]. These four monolayers can form stable quasi-2D liquid layers with a significant amount of out-of-plane motion and in-plane diffusion up to 2300-2400 K, 1050 K, 1600 K and 1320-1400 K, respectively [17]. In addition, properties of free-standing 2D copper monolayers have been recently studied [18]. Based on the results described above, one important point should be emphasized that the transition metal atoms prefer being in close-packed atomic configuration with hexa-coordination in 2D space. It is contrary to the honeycomb structure of prototypical graphene with tri-coordination. Thermal stability of 2D planar monolayers of various alloys also has been found by the quantum calculation methods. Planar 2D hyper-coordinate $Cu_2Si$, $Cu_2Ge$, $Ni_2Ge$, $Ni_2Si$, $Cu_2P$, $Cu_2As$ alloys have been found [11,12,15,16]. Due to difficulty of stabilization of planar hyper-coordinate atomic configurations, 2D materials with hyper-coordinate structure are rarely found. Therefore, existence of planar hyper-coordinate 2D materials predicted by quantum calculations is of great interest. Indeed, two-dimensional $Cu_2Si$ monolayer with planar hexa-coordinate Cu and Si bonding is found to be stable for short annealing up to 1200 K and it is a non-magnetic alloy [11]. This material is metallic and in this alloy, each Si atom is coordinated to six Cu atoms while each Cu atom is coordinated to three Cu and three Si ones. It is found that this planar $Cu_2Si$ monolayer has a strong chemical bonding and high in-plane stiffness [11]. Similarly, planar 2D hyper-coordinate $Cu_2Ge$ has been found and this 2D monolayer is also stable for 10 ps of annealing up to 1200 K [12]. This is the first stable planar hexa-coordinate germanium material in 2D space and its structure or chemical bonding are similar to those found for $Cu_2Si$ given above [11]. Existence of 2D hyper-coordinate crystalline planar $Ni_2Ge$ or quasi-planar $Ni_2Si$ has been found by quantum calculations [15]. Planar $Ni_2Ge$ is stable up to 1500 K while quasi-planar $Ni_2Si$ is stable to around 900 K. It is found that planar $Ni_2Ge$ and quasi-planar $Ni_2Si$ are more stable than germanene and silicene, respectively [15]. Other new 2D materials such as $Cu_2P$, $Cu_2As$ have been found by quantum methods [16]. The former is found to be slightly buckled while the latter is true planar 2D and both are diamagnetic 2D materials [16]. It is clear that the binary 2D materials mentioned above have planar or quasi-planar hyper-coordinate motifs, i.e. some have exactly planar while other have slightly buckled structure. Interestingly, while chemical bondings of $Cu_2Si$ and $Cu_2Ge$ are similar each to other, $Ni_2Si$ and $Ni_2Ge$ have quite different chemical bondings. In general, the works related to various monolayers with planar and/or quasi-planar hexa-coordination mentioned above open a new branch of hyper-coordinated 2D materials for study.

It is clear, predictions of the existence of various 2D metals or alloys by quantum methods such DFT or ab initio MD are more reliable compared to those found by classical MD. However, using quantum methods requires a large computation time and therefore, the models used for quantum calculations are rather small of around tens atoms (i.e. mostly 64 atoms [9-17]). Although existence of ironene containing tens of atoms has been found by both experiment and DFT calculations, atomic structure of a free-standing ironene has been under debate [1-4]. Therefore, it is of great interest to carry out a comprehensive MD simulation of structure and thermodynamics of ironene models containing thousands atoms formed from 2D liquid Fe. This is an alternative choice to gain more detailed information of this important 2D material. It motivates us to carry out the MD study in this direction.

### 2. Calculations

MD simulations have been carried out in 2D square models containing 6400 iron atoms interacted via the EAM potential [19,20]. EAM potentials have been widely used for simulations of metals since these potentials describe well interaction in metals and we do not pause here for more discussion. Initial 2D iron atomic configurations with a square lattice structure and with a lattice constant equal to that found by DFT calculation $(2.35\ \mathring{A}$ [1]) have been relaxed for $10^5$ MD steps at 50 K before heating to 4300 K at heating rate of $10^{11}$ K/s and at zero pressure in order to get 2D liquid configuration. Models obtained at 4300 K are relaxed for $10^5$ MD steps before cooling down to 300 K. Periodic boundary conditions (PBCs) are applied in the x and y Cartesian directions while $z=0$ is kept for all simulation procedure (models are in strictly 2D space), i.e. we use NPT zero pressure ensemble for heating procedure. However, for cooling process PBCs are applied only in the x direction while a fixed with reflection behavior boundary is used for y direction. NVT ensemble simulation is used for further simulation including relaxation for $10^5$ MD steps at 4300 K and cooling down to 300 K at the cooling rate of $2\times 10^{10}$ K/s. As a result, the final configurations are obtained in the form of nanoribbons instead of 2D infinite sheets. Final models obtained at 300 K have been relaxed for $10^5$ MD steps at this temperature before carrying out further structural analysis.

The Verlet algorithm and time step of 1.0 fs are used. Temperature is corrected via simple velocity rescaling. LAMMPS software is used for MD simulations [21]. ISAACS software is used for calculating ring statistics [22]. For calculations of rings, the 'Guttmann' rule is applied [22]. VMD software is used for 2D visualization of atomic configurations [23]. The cutoff radius of $3.30\ \mathring{A}$ is taken in order to calculate coordination number, bond-angle and interatomic distance distributions in the system. This cutoff radius is equal to the position of the first minimum after the first peak in radial distribution function (RDF) of models obtained at 300 K. Note that we employ EAM potential implemented in the LAMMPS software that describes well both structure and thermodynamics of liquid and amorphous Fe thin films [24].

## 3. Results and discussion

### 3.1. Thermodynamics and evolution of structure upon cooling from the melt

Temperature dependence of total energy per atom and heat capacity of the system upon cooling from the melt can be seen in Fig. 1. Total energy curve has two linear parts: the high temperature one is related to the liquid state of the system while the low temperature part is related to the solid state. A sudden-like change between two linear parts is related to the solidification of the system which exhibits a first-order-like phase transition behavior. In contrast, heat capacity has a sharp peak at around $T_X = 2640$ K which can be considered as a crystallization temperature of the system. Note that experimental melting temperature of 3D bulk iron is $T_m = 1811$ K [25]. It is clear that due to constraint in a strictly 2D space of the simulation in the present work, freezing of 2D liquid iron occurs at temperature much higher than that of 3D counterpart. On the other hand, the starting point of deviation from the linearity of the low temperature part of total energy can be considered as temperature of final freezing of 2D liquid iron ($T_f = 2200$ K). We will use this temperature for defining of solid-like atoms occurred during cooling process and we will return to this problem later. May be due to finite size and free edge (in the $y$ direction) effects, freezing of the system does not occur at a certain temperature. It lasts over a certain temperature region (see Fig. 1). Total energy per atom for model obtained at 300 K is equal to $-3.13$ eV/at. which is close to the binding energy of Fe monolayer with a triangle lattice structure found by DFT calculation for the bond length of $2.45$ Å, which is of around $-2.95$ eV/at [4]. Note that the heat capacity is found approximately via the simple relation: $C_V = \frac{\Delta E}{\Delta T}$, $\Delta E$ is the discrepancy of total energy between $T_1$ and $T_2$ on cooling. Heat capacity of 2D iron model at 300 K is equal to $19.24$ $\frac{J}{mol.K}$ which is not far from the value $25.10$ $\frac{J}{mol.K}$ for the bulk crystalline Fe obtained experimentally at 300 K and at pressure of 100 kPa [25]

Evolution of structure of the system upon cooling from the melt can be seen in Fig. 2. One can see that at 4300 K, RDF of the system exhibits a liquid-like behavior, i.e. it has only two peaks at short distances and the height of the peaks is rather small. At temperature lower than the freezing one ($T_X = 2640$ K), additional peaks at intermediate and far distances occur indicated solidification of the system. At 300 K, RDF has separated peaks pointed out a high degree of crystallinity in the system (Fig. 2). Indeed, diffraction pattern of the atomic configuration obtained at 300 K exhibits a well-ordered crystalline behavior with 6-fold symmetry (Fig. 3). This means that 2D iron obtained by cooling from the melt should have a triangle lattice structure instead of a square lattice one. Detailed information of structure of our 2D iron is given below.

![](./images/811120957644079105_1.jpg)

Fig. 1. Temperature dependence of total energy per atom and heat capacity of models (the inset) upon cooling from liquid to solid state. The dot line is total energy per atom while the straight line is a guide for eyes.

![](./images/811120957644079105_2.jpg)

Fig. 2. Evolution of RDF upon cooling from the melt. The bold line is for $T = 2600$ K which is close to the crystallization temperature $T_X = 2640$ K.

### 3.2. Structural properties of 2D iron obtained at 300 K

Final atomic configurations obtained at 300 K are relaxed at this temperature for $10^5$ MD steps before carrying out further structural analysis. We find that 96% Fe atoms in the models have coordination number $Z = 6$ while around 4% have $Z = 5, 4, 3$ (see Fig. 4). These under-coordinated atoms are mainly related to the edge atoms in the $y$ Cartesian direction (see below). These dangling bonds at the edge are more reactive sites for attraction of impurities which may lead to the modification of atomic and electronic structure of ironene nanoribbons like that found for graphene and silicene nanoribbons [26-28]. In contrast, almost 100% atoms in the 2D iron models are involving into 3-fold rings (see the inset of Fig. 4). Concerning on the rings differed from 3-fold, we find only two 6-fold rings, i.e. their fraction is too small compared to that of

![](./images/811120957644079105_3.jpg)

Fig. 3. Diffraction pattern of model obtained at 300 K.

![](./images/811120957644079105_4.jpg)

Fig. 4. Coordination number and ring distributions (inset) in model obtained at
$T=300$ K.

3-fold ones and their fraction cannot be visible in Fig. 4. Atoms
with $Z \neq 6$ and rings differed from 3-fold plus the dangling bonds
at the edge can be considered as structural defects in ironene
nanoribbons. In general, structural defects of 2D materials are
more reactive sites which may play an important role in perfor-
mance of various physico-chemical behaviors of 2D materials
[26-28]. On the other hand, small fraction of structural defects
found for ironene models indicates a relatively homogeneous
structure of the obtained 2D crystals.

In addition, we find that bond-angle distribution in the system
is relatively narrow which has a sharp peak at around $60^{\circ}$, i.e. the
angle of an equilateral triangle (Fig. 5). However, the distribution of
bond-angle ranged from around $50^{\circ}$ to $70^{\circ}$ indicates a certain
degree of the distorted structure of 2D models obtained by cooling
from the melt (Fig. 5). Moreover, we also find a relatively narrow
interatomic distance distribution as shown in the inset of Fig. 5.
The distribution has a sharp peak at around $2.45$ Å which very
close to the values of $2.41$ Å and $2.44$ Å found by DFT calculations
for 2D iron with a triangle lattice structure [4,5]. Experimentally
found that the lattice constant of 2D iron with a square lattice
structure is $2.65$ Å, while DFT calculations show that the most
stable lattice constant of 2D iron with a square lattice structure
is of around $2.35$ Å [1]. This means that our mean lattice constant
of $2.45$ Å lies between these values. In addition, distribution of
interatomic distance in our 2D iron is ranged from around $2.20$ Å
to around $2.75$ Å indicated the existence of structural defects in
models including distorted triangles, rings differed from 3-fold,
the dangling bonds at the edge (see Fig. 6). It is essential to note
that the nearest interatomic distance in bcc 3D iron is $2.48$ Å [25].

![](./images/811120957644079105_5.jpg)

Fig. 5. Bond-angle and interatomic distance distributions (inset) in model obtained
at $T=300$ K.

In order to get more detailed information of structure of 2D
iron, we also calculate local and global bond-orientation orders
[29-31]. The local bond-orientation order, $\Phi_{6}(\vec{r}_{i})$, measures the
degree of 6-fold-orientation ordering as follows:

$$
\Phi_{6}(\vec{r}_{i})=\frac{1}{n(i)} \sum_{j=1}^{n(i)} \exp \left(i 6 \theta_{i j}\right)
\tag{1}
$$

where $\theta_{i j}$ is the angle of the bond between particles $i$ and $j$ and an
arbitrary but fixed reference axis, the sum over $j$ is calculated over
all $n(i)$ nearest-neighbors. The global bond-orientation order, $\Psi_{6}$, is
calculated via averaging over all atoms in the system $(N)$:

$$
\Psi_{6}=\frac{1}{N} \sum_{i=1}^{N} \Phi_{6}(\vec{r}_{i})
\tag{2}
$$

For a perfect triangle lattice structure $\Psi_{6}=1.0$ and for a full
disordered state $\Psi_{6}$ is equal to zero. As shown in the inset of
Fig. 7, in the high temperature region $(T>T_{X})$ the value of $\Psi_{6}$ is
almost equal to zero indicated a strong disordered structure of
the liquid state. However, it has a sudden increase at around the
freezing point exhibited a first-order-like phase transition. At
$300$ K, $\Psi_{6}$ is almost equal to 1.0 meaning that a well-ordered 2D
crystal is formed (see the inset of Fig. 7). We must choose a
critical-like value for $\Psi_{6}$ in order to define solid-like atoms
occurred in the system upon cooling from the melt. It is well-
known that at a freezing point, a significant amount of atoms in
the system remain in the liquid state. It ranges from $25\%$ to $50\%$
of total number of atoms in the system (see for example [32-
34]). Therefore, it is not a good choice if one takes the value for
$\Psi_{6}$ at a freezing point $(T_{X}=2640$ K) as a critical value for defining
of solid-like atoms. An appropriate choice is the value $\Psi_{6}=0.74$
for $T_{f}=2200$ K (see Fig. 1 and discussion given there for
$T_{f}=2200$ K). If atom has local bond-orientation order $\Phi>0.74$,
it is considered as solid-like-one. As shown in Figs. 6 and 7, below
$T_{X}=2640$ K almost all atoms in the system become solid-like. On
the other hand, via coloring of atoms with different local bond-
orientation-orders we find some important points:

- Structure of the obtained 2D crystal is not perfect but it is rela-
tively homogeneous since most atoms in the system have
$\Phi_{6} \in[0.9-1.0)$. It indicates a high degree of crystallinity with
a triangle lattice structure.
- Atoms with the same or close local bond-orientation-order have
a tendency to aggregate together into clusters which may lead
to 'static heterogeneity' of 2D crystals, i.e. crystals containing
clusters/domains with various bond-orientation orders. This
tendency may be cooling rate dependent (and/or depending
on the synthesis method).
- Main structural defects of the bulk 2D iron are single vacancies
(SV) with a small fraction. For ironene nanoribbons, there is a
significant amount of the dangling bonds and under-
coordinated atoms at the free edge in addition to vacancies
(Fig. 6).

There is no information about structural defects in ironene in
order to compare and discuss. However, 2D crystals with
Lennard-Jones (LJ) interatomic potential also have a triangle lattice
structure like that found for 2D iron in the present work. Therefore,
one can take the data for 2D crystals with LJ potential for

![](./images/811120957644079105_6.jpg)

Fig. 6. 2D visualization of atomic configuration obtained at $T=300$ K. Atoms of different local bond-orientation orders ($\Phi_6$) are colored as follows: cyan for $\Phi_6\in[0.9-1.0)$, pink for $\Phi_6\in[0.8-0.9)$, blue for $\Phi_6\in[0.7-0.8)$, red for $\Phi_6\in[0.6-0.7)$, gray for $\Phi_6\in[0.5-0.6)$, yellow for $\Phi_6\in[0.4-0.5)$, orange for $\Phi_6\in[0.3-0.4)$, tan for $\Phi_6\in[0.2-0.3)$, silver for $\Phi_6\in[0.1-0.2)$, green for $\Phi_6\in[0.0-0.1)$. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

discussion. Indeed, the main structural defects in 2D crystals with LJ potential are also vacancies and their behaviors have been under much attention (see for example [35,36]). It is found that SVs are the most mobile and two SVs have a tendency to coalesce into one di-vacancy in order to lower energy [37]. In addition, SVs may transform semi-metallic silicene into metallic one or vacancies may induce a small band gap in silicene [37]. Important effects of SVs on behaviors of 2D iron can be suggested, however, main effects of SVs in 2D iron maybe those on the thermal stability and on magnetic behaviors of material. Indeed, DFT calculations show that ferromagnetism can be introduced in graphene by adding vacancies [38,39]. Therefore, significant effects of vacancies on magnetic behaviors of ironene can be suggested. Fig. 6 shows that free edge of 2D iron exhibits a more complicated type although fraction of the zig-zag edge dominates. The type of the edge may have a strong effect on behaviors of 2D materials including electronic structure like that found for other 2D materials [26-28].

### 3.3. Atomic mechanism of solidification

In order to highlight atomic mechanism of solidification of the system upon cooling from the melt, we present temperature dependence of fraction of solid-like atoms occurred during cooling including 2D visualization (Figs. 7 and 8). We find that fraction of solid-like atoms is small and almost constant in the high temperature region (Fig. 7). This means that these atoms maybe not real solid-like in the high temperature region since their lifetime is short, i.e. the frequent transformation from solid-like atoms into liquid-like ones and vice versa should frequently occur. However, fraction of solid-like atoms suddenly increases at around the freezing point and reaches almost 1.0 at 300 K (Fig. 7). This confirms again a first-order behavior of crystallization of 2D liquid iron. Note that it is very difficult for experimentalists to observe the phase transitions in 2D materials using traditional calorimetric methods. Therefore, our MD simulation provides a deeper understanding of the problem. Note that at a freezing point, fraction of solid-like atoms in the system is around 0.59 which is close to the range from 0.50 to 0.56 found for simple 2D system in [34].

On the other hand, we find that solid-like atoms occur almost homogeneously in the system and they have a tendency to aggregate into local clusters (Fig. 8a). Solidification proceeds further with cooling via occurrence/growth of solid-like clusters with a triangle lattice structure following classical theory of nucleation. However, occurrence/growth of solid-like clusters does not proceed by the same manner throughout the model due to free edge effects in the y direction (Fig. 8b). Free edge effects on structure and thermodynamics of 2D iron are out of scope of the paper.

![](./images/811120957644079105_7.jpg)

Fig. 7. Temperature dependence of the fraction of solid-like atoms occurred upon cooling from the melt ($N_S/N$) and global bond-orientation-order (inset).

In addition, we find no evidence of the formation of an intermediate phase during crystallization of 2D liquid iron. It may be due to a finite size of the models used in the present work. It is essential to note that we have employed the same simulation procedure for all potentials for Fe and/or Fe based alloys implemented in LAMMPS software [21] and final 2D iron with a triangle lattice structure is formed (not shown). On the other hand, we also find relaxation induced square lattice $\rightarrow$ triangle lattice transition in 2D iron even at very low temperature of 50 K. That is, if initial atomic configurations of 2D iron with a square lattice structure (the lattice constant of $2.35\ \mathring{A}$) are relaxed at 50 K using all interatomic potentials for Fe or Fe based alloys implemented in LAMMPS, square lattice eventually transforms into triangle one

![](./images/811120957644079105_8.jpg)

(a) $T=2700 \mathrm{~K}$

![](./images/811120957644079105_9.jpg)

(b) $T=2600 \mathrm{~K}$

Fig. 8. 2D visualization of configuration of solid-like atoms in models obtained at temperatures above/below $T_{\mathrm{X}}=2640 \mathrm{~K}$.

like that found in [5]. This means that free-standing 2D iron with a triangle lattice structure may be the most stable form compared to those with square or other lattice ones.

Finally, it is of great interest to carry out stress analysis of the obtained ironene nanoribbon to clarify the edge effects on stress distribution or warping, scrolling of nanoribbon in general. Such calculations should be done in 3D space. It is found that depending on the type of the edge termination, the bonding configurations at the edges of graphene nanoribbons can be different from those found in the interior (or in the bulk). If the atomic bonds at the edges are shorter or longer than those found in the bulk graphene, the edges should be under the state of compressive or tensile stresses [40]. Edge stresses can have a strong effect on morphology of graphene nanoribbons leading to warping and rippling of nanoribbons for reduction of the edge energy at the cost of deformation of the 'bulk' sheet [40]. It is found that compressive edge stresses cause out-of-plane warping of graphene sheet and morphology of warped sheets depends strongly on their size/shape and on magnitude of the edge stresses [40]. It leads to strong effects on electronic structure of 2D material since electronic structure of graphene can be strongly altered by both strain and curvature [41]. Total energy of graphene sheets with compressive edge stresses can be reduced by stretching of the atomic bonds by out-of-plane movement of the atoms leading to the warping and rippling of graphene sheets [40]. On the other hand, depending on the size and shape of the sheets warping can be localized in the boundary region or can influence the entire morphology of nanoribbons [40]. Overall, similar edge stress effects on morphology and various behaviors of Fe nanoribbons including magnetic ones can be suggested. However, it is out of scope of the present paper.

## 4. Conclusions

A comprehensive MD simulation of the formation of freestanding 2D iron from the liquid state has been carried out and some conclusions can be drawn as follows:

- Free-standing 2D iron with a triangle lattice structure spontaneously forms from the liquid state using EAM potential (and/or all potentials for Fe or Fe-based alloys implemented in LAMMPS software [20]). Our MD simulation confirms again that 2D iron with a triangle lattice structure maybe more stable compared to that with a square lattice. It is unlike that found experimentally or by DFT calculation for 2D iron suspended in graphene pores [1]. Note that triangle lattice or hexagonal close-packed structure of ironene found in the present work is in good accordance with that found for various 2D pure metals including Fe, Au, Ag [2-5,13,14].
- 2D iron formed 'naturally' from the liquid state has nearly homogeneous and well-ordered triangle structure. However, a slightly distorted structure of the models should be mentioned including a relatively narrow interatomic distance and bond angle distributions compared to those of the equilateral triangle lattice structure.
- Structural behaviors of 2D iron with a triangle lattice structure including interatomic distance are close to those found for 2D and 3D iron. The main structural defects of 2D iron are single vacancies like that found for a triangle lattice structure of 2D Lennard-Jones crystals.
- Crystallization of 2D liquid Fe exhibits a first-order behavior of phase transition. Both binding energy and heat capacity of 2D iron at 300 K have a reasonable value compared to those found for 2D and 3D counterparts.

## Acknowledgements

This research is funded by Vietnam National Foundation for Science and Technology Development (NAFOSTED) under Grant 103.01-2014.86.

## References

[1] J. Zhao, Q. Deng, A. Bachmatiuk, G. Sandeep, A. Popov, J. Eckert, M.H. Rummeli, Science 343 (2014) 1228.
[2] W. Yang, H. Wang, Proc. IUTAM 10 (2014) 273.
[3] P. Wang, H. Wang, W. Yang, RSC Adv. 4 (2014) 17008.
[4] M.R. Thomsen, S.J. Brun, T.G. Pedersen, Phys. Rev. B 91 (2015) 125439.
[5] Y. Shao, R. Pang, X. Shi, J. Phys. Chem. C 119 (2015) 22954.
[6] H. Zhang, Y.-M. Dai, L.-M. Liu, Comp. Mater. Sci. 101 (2015) 255.
[7] S. Achilli, S. Caravati, M.I. Trioni, J. Phys.: Condens. Matter 19 (2007) 305021.
[8] G. Vogl, E. Partyka-Jankowska, M. Zajac, A.I. Chumakov, Phys. Rev. B 80 (2009) 115406.
[9] H. Duan, N. Yan, R. Yu, C.-R. Chang, G. Zhou, H.-S. Hu, H. Rong, Z. Niu, J. Mao, H. Asakura, T. Tanaka, P.J. Dyson, J. Li, Y. Li, Nat. Comm. 5 (2014) 3093.
[10] P. Koskinen, T. Korhonen, Nanoscale 7 (2015) 10140.
[11] L.M. Yang, V. Bacic, I.A. Popov, A.I. Boldyrev, T. Heine, T. Frauenheim, E. Ganz, J. Am. Chem. Soc. 137 (2015) 2757.
[12] L.M. Yang, I.A. Popov, A.I. Boldyrev, T. Heine, T. Frauenheim, E. Ganz, Phys. Chem. Chem. Phys. 17 (2015) 17545.
[13] L.M. Yang, T. Frauenheim, E. Ganz, Phys. Chem. Chem. Phys. 17 (2015) 19695.
[14] L.M. Yang, M. Dornfeld, T. Frauenheim, E. Ganz, Phys. Chem. Chem. Phys. 17 (2015) 26036.
[15] L.M. Yang, I.A. Popov, T. Frauenheim, A.I. Boldyrev, T. Heine, V. Bacic, E. Ganz, Phys. Chem. Chem. Phys. 17 (2015) 26043.
[16] L.M. Yang, E. Ganz, Phys. Chem. Chem. Phys. 18 (2016) 17586.
[17] L.M. Yang, A.B. Ganz, M. Dornfeld, E. Ganz, Condens. Matter 1 (2016) 1.

[18] L.M. Yang, T. Frauenheim, E. Ganz, J. Nanomater. (2016), Article ID: 8429510.
[19] M.S. Daw, M.I. Baskes, Phys. Rev. B 29 (1984) 6443.
[20] M.S. Daw, S.M. Foiles, M.I. Baskes, Mater. Sci. Rep. 9 (1993) 251.
[21] S. Plimpton, J. Comp. Phys. 117 (1995) 1.
[22] S. Le Roux, V. Petkov, J. Appl. Cryst. 43 (2010) 181.
[23] W. Humphrey, A. Dalke, K. Schulten, J. Molec. Graph. 14 (1996) 33.
[24] V.V. Hoang, N.T. Long, D.N. Son, Comp. Mater. Sci. 95 (2014) 491.
[25] D.R. Lide (Ed.), CRC Handbook of Chemistry and Physics, CRC Press, New York, 1996.

[26] S. Cahangirov, M. Topsakal, S. Ciraci, Phys. Rev. B 81 (2010) 195120.
[27] Y.-L. Song, Y. Zhang, J.-M. Zhang, D.-B. Lu, Appl. Surf. Sci. 256 (2010) 6313.
[28] L. Yang, C.-H. Park, Y.-W. Son, M.L. Cohen, S.G. Louie, Phys. Rev. Lett. 99 (2007) 186801.
[29] P.J. Steinhard, D.R. Nelson, M. Ronchetti, Phys. Rev. B 28 (1983) 784.
[30] P.J. Steinhard, D.R. Nelson, M. Ronchetti, Phys. Rev. Lett. 47 (1983) 1297.
[31] K.J. Strandburg, Rev. Mod. Phys. 60 (1988) 161.

[32] V.V. Hoang, T. Odagaki, J. Phys. Chem. B 115 (2011) 6946.
[33] V.V. Hoang, T.Q. Dong, Phys. Rev. B 84 (2011) 174204.
[34] A.C. Mitus, A.Z. Patashinski, A. Patrykiejew, S. Sokolowski, Phys. Rev. B 66 (2002) 184202.
[35] K. Wierschem, E. Manousakis, Phys. Rev. B 83 (2011) 214108.
[36] O.G. Vinogradov, Int. J. Fract. 171 (2011) 155.
[37] J. Gao, J. Zhang, H. Liu, Q. Zhang, J. Zhao, Nanoscale 5 (2013) 9785.
[38] P.O. Lehtinen, A.S. Foster, Y. Ma, A.V. Krasheninnikov, R.M. Nieminen, Phys. Rev. Lett. 93 (2004) 187202.
[39] S. Haldar, B.S. Pujari, S. Bhandary, F. Cossu, O. Eriksson, D.G. Kanhere, B. Sanyal, Phys. Rev. B 89 (2014) 205411.
[40] V.B. Shenoy, C.D. Reddy, A. Ramasubramaniam, Y.W. Zhang, Phys. Rev. Lett. 101 (2008) 245501.
[41] A.H. Castro Neto, F. Guinea, N.M.R. Peres, K.S. Novoselov, A.K. Geim, Rev. Mod. Phys. 81 (2009) 109.