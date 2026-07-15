ISSN 0031-918X, Physics of Metals and Metallography, 2019, Vol. 120, No. 1, pp. 50–59. © Pleiades Publishing, Ltd., 2019.
Russian Text © A.V. Weckman, B.F. Dem’yanov, 2019, published in Fizika Metallov i Metallovedenie, 2019, Vol. 120, No. 1, pp. 53–62.

# STRUCTURE, PHASE TRANSFORMATIONS, AND DIFFUSION

## Structural Vacancy Model of Grain Boundaries

### A. V. Weckman$^{a, *}$ and B. F. Dem’yanov$^{a}$
$^{a}$Altai State Technical University, Barnaul, 656038 Russia
*e-mail: weckman@list.ru

Received January 17, 2018; revised June 5, 2018

Abstract—A structural vacancy model of tilt grain boundaries in metals has been developed. For construction of the stable structure of the boundary, the initial pattern was chosen according to the CSL model. The introduction of additional atoms and vacancies into the boundary region and shifting of atoms by the interatomic forces stabilize its structure. The criterion of a stable structure is the grain-boundary energy. The comparison of two main approaches to the stabilization of the grain structure demonstrated that changing the number of atoms at the boundary is more energetically advantageous than the relative shift of grains. The stability of the structure obtained has been studied under the shear stress. In the model developed, atomic structures obtained with pair and many-body potentials have been compared. The comparative analysis has shown that the grain-boundary structure does not depend on the choice of potential; atomic positions differ by less than 0.1 Å, which is 2.5% of the lattice parameter. The atomic structure is in agreement with experimental images of grain boundaries.

Keywords: grain boundary, computer simulation, structural vacancy model

DOI: 10.1134/S0031918X18110200

## INTRODUCTION

Investigating grain boundaries (GBs) is important because they both affect and control many properties of material, whereas the properties of the grains are governed by their atomic structure and chemical composition. It is necessary therefore to consider the structure and properties of the GBs in order to understand many basic properties of polycrystals.

The study of the defect structure of polycrystals began with GB study. The first investigations considered the boundary to be an amorphous region without structure. In 1949, the development of investigation methods resulted in the coincidence-lattice model (CSL) [1] which suggested that the GB had a periodic structure. This model is based on a simple geometric principle, i.e., certain parameters of misorientation of one crystal with respect to another lead to the coincidence of some sites of misoriented lattices. In this case, it was assumed that the boundary between these crystals had an ordered structure and special properties. The parameter which characterizes the density of coincidence sites ($\Sigma$) is equal to the ratio of the volume of a unit cell of coincident-sites lattices (CSL) to the atomic volume; when the model was invented, the parameter was very significant, namely, the less it was, the more special the properties of the boundary were, e.g., reduced energy and high mobility.

Figure 1 demonstrates two cubic crystals turned about the [100] axis to the angle $\Theta = 36.87^\circ$, which results in the formation of the $\Sigma5(013)$ GB. As we can see from the figure, for each five sites of the unit cell, there is one coincident site. In this case, some atoms close to the GB are located at the distance $r$ which is different from the equilibrium one. The change in spacing between atoms close the boundary plane inevitably increases their potential energy. It is seen from the figure that some atoms are in a tight state (the distance $r$ is less than the equilibrium one), and other atoms are in a loose state (the distance $r$ is greater than the equilibrium one). It is therefore logical to introduce the parameter $r/r_1$ ($r_1$ is the radius of the first

![](./images/817355139114336259_1.jpg)

Fig. 1. Structure of the special $\Sigma5(013)[100]$ GB in the CSL model.

coordination shell) which characterizes the degree of proximity of atoms. In the case of $r/r_i < 1$, the GB regions are under compression, otherwise, $r/r_i > 1$, they are subjected to extension. In terms of energy, both states of atoms, namely, tight and loose, have an increase in potential energy. As a result, the majority of boundaries in the CSL model have high energy. For instance, in [2–5] it was demonstrated that in the CSL model the GB energy differs from the experimental one by an order of magnitude. In addition, in this model, the GBs do not have an excess volume, which contradicts the modern viewpoint on polycrystal structure.

Two interpenetrating lattices form a pattern characteristic of a certain boundary. If one of the lattices is displaced to the vector $\mathbf{d}$ relative to the other lattice (Fig. 1), different coincident sites will occur, whereas the sites that have been coincident will separate. In this case, the characteristic pattern remains the same. Unit translation vectors that do not change the pattern form a supplementary lattice, called the displacement-shift complete lattice (DSCL). The period of DSCL is less than the periods of the interpenetrating lattices and CSL.

The DSCL is determined by the parameters of the misorientations of parts of the bicrystal, whereas the GB-plane position is not taken into account upon its construction. The projections of DSCL vectors on the GB plane define the so-called grain-boundary-shift lattice (GBSL) [6, 7]. Evidently, if the plane of the GB is a close packed plane of the CSL, the GBSL coincides with the DSCL. Otherwise, the period of GBSL is less than the period of DSCL, and the latter is a sublattice of the GBSL. The DSCL and GBSL are supplementary and allow one to analyze the defect structure of the boundary; in particular, the fact that at the boundary the period of the energy profile is equal to that of the supplementary lattices. However, this is true only if the amplitude of thermal vibrations does not exceed the period of the supplementary lattices. Otherwise, the usage of the supplementary lattices does not have any physical meaning, because there is a maximum temperature above which the special GBs become random.

The random GB consists of the fragments of "good" matching corresponding to the CSL model, between which there are fragments of "bad" matching. Design of these boundaries can be determined by the method of the so-called 0-lattice [8]. The lattice is composed by an array of points which belong to a misorientation axis of crystals and have the equivalent positions in a crystal, which transform one lattice into another, whereas these equivalent positions do not necessarily coincide with lattice sites. The 0-lattice exists at any angle of rotation of the crystals; however, in the case of a special angle, some of its sites are coincidence sites.

Even if the angle of the GB misorientation does not correspond to the boundary in the CSL model, its atomic structure repeats with the period equal to a certain spacing between the sites in the boundary plane. These fragments can be regarded as units of the boundary structure, which are called the structural units (SU) [9, 10], and the model in which the boundary is represented by an array of such structures is called the model of structural units. Then, if in each structural unit the positions of atoms are known, the atomic structure of the boundary is also known. At small deviations of the misorientation angle from the special one, the GB has a structure of fragments containing the SUs which are interbedded with the fragments of the bad matching. In some cases, it is more convenient to consider the fragment of a certain length as a peculiar structural unit [11]. Now, it is assumed that at deviation of the angle $\Theta$ from the special values, the GB is composed of an array of the alternating SUs of special misorientations whose angles are most close to a set value. Such a pattern produces the elastic strain of disclination dipoles in boundary layers; however, the energy of such boundary can be lower than of the boundary that is not partitioned to the SUs. The main problem of the SU model is that it is difficult to predict in advance both the structure of the structural units and their sequence of order.

The study of the random boundaries in the SU model naturally led researchers to the GB construction with Bernal polyhedra [12, 13]. In this model, the boundary is composed of alternating polyhedra which were used earlier for the description of structure of liquids [14]. Contrary to the amorphous structure, where the polyhedra are disordered, they compose a strictly ordered layer in the boundary. The problem of this model application is similar to that of the SU model, i.e., it is difficult to place them in order to obtain a boundary with a certain misorientation angle.

## CONTEMPORARY COMPUTER MODELS OF GRAIN BOUNDARIES

The CSL model is historically one of the most applied in the computer simulation of the GBs. The main reason for this popularity lies in the fact that the majority of computer-simulation investigations study the special GBs with the small value of $\Sigma$. However, the application of this model in its original form does not result in a stable structure which corresponds to the minimum of the potential energy. Therefore, several relaxation procedures were developed which allowed a lowering of the defect energy in the simulation. The procedures can be divided into two types, i.e., the first retains the number of atoms and the second one does not. The most often employed procedure without changing the number of atoms is the relative shift of grains parallel and perpendicular to the boundary plane. Upon the relative shift, atoms that are in a tight state move apart which stabilizes the bound-

ary. In 1968, Vitek suggested a method for determining stable states upon the relative shift of grains [15]. This method was called the method of construction of $\gamma$-energy surfaces. It implies that the conjugate crystals shift relative to one another to different vectors $\vec{R}$ that lie in the GB plane. For each shift, the potential energy of the boundary is calculated. The high energy corresponds to instable states, and the minimum of energy, to stable and metastable states. The formation of the stable atomic structure of the boundary upon the relative shift was noted in [16–19].

The procedure of changing the number of atoms employs the structure relaxation by the removal of some atoms from the boundary region. It is mainly used if the atoms are closely packed. As shown in one of the first articles [20], which estimates effects of var- ious relaxations on the energy of special boundaries, the introduction of vacancies is the most efficient method to decrease the defect energy. The removal of atoms is often preceded or followed by the relative shift.

Another relaxation method is the displacement of atoms from lattice sites by interatomic forces. This procedure employs the gradient-descent method and is called the molecular statistics method. In this case, the grain-boundary energy is minimized. Some authors use the crystal-lattice extension combined with the procedures described above.

Detailed reviews of the computer simulation of the GBs in 1960–1980 can be found in [21–24].

From 1984 to 1990, D. Wolf published a number of works on the computer simulation of the GBs, in which he investigated the tilt and twist boundaries in fcc and bcc metals. The special GBs were simulated in a wide range of misorientation angles, which allowed the author to obtain the dependence of the grain energy on the misorientation angle. The struc- ture of the boundary in the CSL model was used as the initial one. Then, for the stress relaxation, minimiza- tion was employed by the gradient-descent method [25], relative shift, and extension or compression of the lattice [26, 27].

In 1996, Rittner and Seidman [28] studied 23 spe- cial GBs with the [110] misorientation axis. After the construction of the boundary in the CSL model, the authors used the relative shift along and perpendicular to the boundary. The displacement of atoms from the crystal-lattice sites completed the sampling of the sta- ble structures. A similar method was used in recent works, e.g., [29, 30].

In [5], the authors simulated a variety of the special GBs, which allowed them to construct a dependence of the boundary energy on the misorientation angle. The method of simulation is based on procedures employed in [28] and described in detail in [31]. The choice of stable-boundary structures includes the fol- lowing steps: the CSL structure of the boundary is rel- atively shifted, then the atoms which get close are removed. In this case, each of the boundaries under consideration has many structures from which the one with the lowest energy is chosen. The final stage of the simulation is shifting of the atoms from the crystal-lat- tice sites.

The removal of the approached atoms was carried out in [32]. The authors studied the special GBs with the [110] misorientation axis and small values of $\Sigma$. The construction of the stable boundary included the following stages: the construction of the boundary in the CSL model, the removal of the atoms, and the relaxation by atom shifts. The removal of the atoms is necessary if they approached closer than 0.8 of the crystal-lattice parameter.

Therefore, despite numerous GB studies, there is an urgent need for a simple and convenient computer model. The aim of this work is to develop such a model.

## CONSTRUCTION OF THE STRUCTURAL VACANCY MODEL OF GB

A simple geometric procedure was used in our model for the construction of the initial atomic pattern close to the GB, i.e., two halves of the bicrystal are rotated about the axis passing through an atomic row. The angles of rotation of conjugate crystals do not cor- relate in this case. This approach can be used for the construction of both the symmetric and asymmetric GBs, and the misorientation angle affects the type of boundary, i.e., special or random. Dimensions of the bicrystal and boundary conditions can be chosen in accordance with the issue under consideration. In the simulation of the structure and energy of the GBs, the following crystal dimensions were used: $80a$ along the boundary plane (axis $Ox$); $20a$ along the misorienta- tion axis (axis $Oy$); $40a$ in the direction perpendicular to the boundary plane (axis $Oz$), where $a$ is the crystal- lattice parameter. The fixed boundary conditions were used for the $xOy$ and $yOz$ axes; and the periodic boundary conditions, for the $xOz$ axis.

After the construction of the boundary, the number of atoms was varied; it implied the introduction of additional atoms and vacancies into the GB region. In the course of the boundary construction, it is impos- sible to predict from the geometry which of the sites of the two conjugate lattices requires a vacancy, and which regions need an additional atom. In addition, it is impossible to predict the necessary number of these elements. This requires an energy calculation. As will be shown below, upon the determination of the stable structure, the type of potential hardly affects atomic patterns close to the GB plane.

Figure 2 demonstrates the stages of the introduc- tion of vacancies and atoms. At the first stage, in the initial structure, there are regions in which spacing between the atoms is greater than the equilibrium one. As can be seen from Fig. 2a, each structural unit con-

![](./images/817355139114336259_2.jpg)

Fig. 2. Stages of the introduction of atoms and vacancies.

tains such regions. In order to fill up these regions, we must extend the atomic planes of one of the conjugate crystals into another one (Fig. 2b). A part of atoms therefore filled the loose regions. The number of atoms that it is necessary to introduce into the GB region can be determined by varying the depth of pen- etration of atoms into the conjugate crystal. At the sec- ond stage, the number pairs of atoms with spacing less than the certain minimum $r_{min}$ are determined. The value of $r_{min}$ also can be varied, which is equivalent to varying the number of vacancies introduced. At the third stage, one of the approached atoms is removed from the core of the GB (Fig. 2c), whereupon the sec- ond atom shifts into the symmetric position at the boundary plane (Fig. 2d), thus forming the distributed vacancy [4]. The atoms filling the loose regions also shift into the GB plane. This procedure is called the vacancy relaxation of the boundary.

The number of atoms that must be removed to sta- bilize the GB depends on the crystal geometry of the boundary. In the case of small-angle boundaries in particular, the number of approached atoms is greater than that in the case of high-angle boundaries. The extension of strained regions also grows with decreas- ing the misorientation angle. Figure 3 demonstrates examples of changes in the grain-boundary energy in the course of the vacancy relaxation. The curves have two minimums at the different penetration depths $r/r_{1}$, i.e., 1.3–1.5, and different atomic spacings $r/r_{1}$, i.e., 0.65–0.80. The energies were calculated by using the Morse pair potential as follows:

$$
\varphi\left(r_{i j}\right)=D \beta \mathrm{e}^{-\alpha r_{i j}}\left(\beta \mathrm{e}^{-\alpha r_{i j}}-2\right). \tag{1}
$$

The parameters $D$, $\alpha$, and $\beta$ of the potential corre- sponded to aluminum borrowed from [33]. We can see that in the case of the random GBs, the curves are smooth (Fig. 3a), which agrees with their atomic structure. In particular, each point corresponds to the introduction or removal of one atom into or from the GB. On the contrary, in the case of the special GBs, the introduction and removal of atoms are performed in all structural units simultaneously. That is why the curves are step-like (Fig. 3b).

![](./images/817355139114336259_3.jpg)

Fig. 3. Change in the grain-boundary energy in the course of construction of the random (a) and special (b) boundaries.

The procedure of atom and vacancy introduction into the GB region stabilizes the latter, which is proved by the energy surfaces shown in Fig. 4. To demonstrate the validity of simulation, we must simulate the boundary that has been extensively studied by both experiment and theory. This is true for the special $\Sigma 5(012)$ and $\Sigma 5(013)$ GBs. The $\gamma$-energy surfaces cal- culated after the construction of the boundary in the CSL model are shown in Fig. 4a. For the construc- tion, one grain was shifted relative to another by the lattice parameter $(a=4.05\ \mathring{A})$ with the step of $0.1\ \mathring{A}$. Components of the translation vector are directed along the boundary plane and perpendicular $(R_{x})$ and parallel $(R_{y})$ to the misorientation axis. The shape of the surfaces corresponds to the atomic structure of the boundary in the model. The minimums correspond to the stable states; and saddle points characterize the potential barriers of transition from one stable state to another one. Energy maximums occur, if in the course of shifting, atoms approach each other; the distance is determined by the peak height. The relative shift $R_{x}=R_{y}=0$ corresponds to the energy maximum.

![](./images/817355139114336259_4.jpg)

Fig. 4. Transformation of the energy surfaces of the special Σ5(012) and Σ5(013) GBs in the course of the relaxation: (a) the CSL model; (b) after the vacancy relaxation; (c) the stable state of the GB.

After the vacancy relaxation, the surfaces essen- tially change; the unstrained state is characterized by the minimum of potential energy (Fig. 4b). Besides this minimum, the energy surfaces have other local energy minimums which correspond to metastable GB states. The energy of the metastable states of the boundaries is higher than that in the point with the coordinates $R_x = R_y = 0$. Thus, the vacancy-relaxation procedure stabilizes the defect and hampers the rela- tive shift of the grains. In addition, the magnitude of grain-boundary energy is significantly lower than the energy of the stable state in the CSL model.

The atomic structures of the Σ5(012) and Σ5(013) GBs are conventionally designated as an array of the structural units which have a characteristic form of a kite; and they are formed by conjugating two single crystals by the planes (210) or (310). Figure 5a demon- strates the atomic structure of these GBs in the CSL model; and Fig. 5b, that after the vacancy relaxation. As can be seen from the figure, each of the boundaries consists of the same structural units presented by the solid line.

In comparison with that of the CSL model, the structural units of the stable boundary contain two vacancies which occupy interstices near the closest atoms. For the Σ5(012) and Σ5(013) grain boundaries, this distance is $0.63r_1$ and $0.45r_1$, respectively. The atomic structure obtained in this model is in agreement with high-resolution-electron-microscopy images (Fig. 5c).

After the vacancy relaxation, the energy remains too high. This is because of atoms, excluding those that have been placed in the GB plane, remaining at sites of the crystal lattice. The shift of the atoms by interatomic forces additionally decreases the GB energy. This pro- cedure is called atomic relaxation and was performed using the method of molecular statistics.

Figure 6 shows the field of atomic shifts after the atomic relaxation. The length of dashes corresponds to the shift multiplied by five. We can see that atoms shift to decrease and increase spacing between the extended and approached atoms, respectively. The procedure of atomic relaxation significantly decreases the GB energy. Thus, for Σ5(012) this decrease is $0.393\ \text{J/m}^2$, and for Σ5(013), $0.78\ \text{J/m}^2$. It seems that upon relax- ation, the energy of the Σ5(012) boundary significantly decreases, and the shift of its atoms is more significant than that of the Σ5(013) GB.

After the atomic relaxation, the $\gamma$-surface qualita- tively does not change (see Fig. 4c) in comparison with that after the vacancy relaxation (see Fig. 4b). The

![](./images/817355139114336259_5.jpg)

Fig. 5. Structure of the Σ5(012) (left) and Σ5(013) (right) boundaries: (a) the CSL model; (b) after the vacancy relaxation; (c) high-resolution-electron microscopy images [34, 35].

![](./images/817355139114336259_6.jpg)

Fig. 6. Fields of atomic shifts after the atomic relaxation of the Σ5(012) (a) and Σ5(013) GB (b).

main difference is a decrease in the energy of the stable state and an increase in the height of energy peaks.

To construct a tilt grain boundary in our structural vacancy model, the following is necessary:
- to construct the GB in the CSL model;
- to introduce additional atoms where the spacing between neighboring atoms is $r > 1.4r_1$; to replace atoms with the spacing less than $r < 0.7r_1$ by one atom in the GB plane;
- to stabilize the structure by shifting atoms using the interatomic forces.

## EFFECT OF POTENTIAL

Sensitivity of a model to the type of potential essen- tially decreases its value and arouses doubts of its validity. We must therefore carry out calculations with different interatomic potentials. In the early history of

![](./images/817355139114336259_7.jpg)

Fig. 7. Interaction potentials (a) and atomic potential energy in the perfect crystal (b).

simulation, only pair potentials were used for description of interatomic forces. This was caused by the simplicity of the potentials and insufficient computation capability. For instance, the metallic systems were usually described by short-range potentials such as Lennard-Jones, Born–Mayer, and Morse. An increase in computation capability allowed the application of more complicated many-body potentials. Metallic bonds form due to the collectivization of electrons; and therefore, we must take into account the many-body interaction. There are two approaches to taking the many-body interaction into account. The first implies an addition of the term of electronic-density functional to the pair-interaction term. These potentials are known as embedded-atom potentials [36, 37], potentials of glue models [38, 39], Finnis–Sinclair potentials [40], and long-range modifications of the latter [41, 42]. The second approach includes the transition from the pair to cluster potentials, which introduces interactions of higher order, i.e., between three or four particles; this approach resulted in the invention of the Murrell–Mottram potential [43, 44]. However, the validity of pair-potential calculations is still debatable. Many physical properties of metals and their structure are calculated with these potentials with good agreement. The grain-boundary structure, in particular, almost does not depend on the choice of the potential [45–47].

To check the influence of the potential type on the model, the results of simulation of the special Σ5(013) GB were compared for the case of the Morse potential (1) and the Cleri–Rosato many-body potential which includes the following Born–Mayer pair potential

$$
U_{R}^{i}=\sum_{j} A \exp ^{-p\left(r_{i j} / r_{1}-1\right)}, \tag{2}
$$

for description of the repulsion and the following many-body term

$$
U_{B}^{i}=-\sqrt{\sum_{j} \xi^{2} \exp ^{-2 q\left(r_{i j} / r_{1}-1\right)}}, \tag{3}
$$

for description of the attraction of atoms. Constants $A$, $p$, $q$, and $\xi$ are borrowed from [48] and also correspond to aluminum.

Figure 7a demonstrates the dependence of the potential function on the atomic spacing. Arrows with numbers designate positions of coordination shells in the fcc lattice of aluminum. We can see from the figure that the depth of a potential well corresponds to the Cleri–Rosato potential and is five times higher than that of the Morse potential. In addition, the minimum of the potential corresponds to 2.3 Å which is less than the first coordination shell of aluminum ($r_1 = 2.86$ Å). The minimum of the Morse potential corresponds to $r_1$ value. Figure 7b shows the dependence of the atomic potential energy in the perfect crystal on the cut-off radius of the potential. The dependence demonstrates that to correctly compare the results of simulations with the Morse and Cleri–Rosato potentials, we must take into account the interaction within three coordination shells, because only such cut-off radius of the potentials provides close energies.

As can be seen from Fig. 5a, one period of the Σ5(013)-boundary repetition in fcc metals contains two pairs of approached atoms. The spacing between them is $0.316a$ and $0.632a$, whereas the equilibrium spacing is $r_1 = 0.707a$. In the course of vacancy relaxation, the structure stabilizes when one atom of the first pair of approached atoms is removed. The removal of another atom from the structure increases the energy. In this case, in the CSL model the boundary energy is equal to 7.834 and 14.861 J/m²; and after the vacancy relaxation it is 0.916 and 0.580 J/m² for calculations with the pair and many-body potentials, respectively. As a result, in both cases, the structure shown in Fig. 5b is obtained. The atomic relaxation changes the energy to 0.738 and 0.501 J/m². In order to completely stabilize the structure, we must perform approximately the same number of steps. The experimental values of GB energy in aluminum are approximately 0.60 J/m² [49], i.e., the energy acquired with the pair potential is overestimated and that with the

![](./images/817355139114336259_8.jpg)

![](./images/817355139114336259_9.jpg)

![](./images/817355139114336259_10.jpg)

![](./images/817355139114336259_11.jpg)

Fig. 8. Structural unit of the Σ5(013) GB calculated (a); the spacing between atoms obtained with different potentials (b); the distribution of the excess volume (c), and the radial distribution function of atoms (d).

many-body potential is underestimated. It is interesting that in the CSL model the many-body potential yields two-times higher energy than the pair potential. On the other hand, after the vacancy introduction, the GB energy acquired with the pair potential is higher than that with the many-body potential. Finally, upon the atomic relaxation, in the case of the pair potential, a decrease in the energy is two-times higher than in the case of the many-body potential.

Although the general pattern of the GB structure obtained with the different potentials is mainly the same, atomic positions are different. In Fig. 8a, atoms designated by numbers belong to one structural unit, and circles of different sizes indicate atomic positions calculated by the different potentials, i.e., big ones designate the Morse potential and small, the Cleri–Rosato potential. Figure 8b demonstrates the spacing between atomic positions calculated with the different potentials. As can be seen, the values do not exceed $0.1\ \mathring{A}$ which is approximately 2.5% of the crystal-lattice parameter of aluminum.

Grain boundaries have an excess volume, as any other defect. The distribution of the excess volume over the boundary plane can control the structural peculiarities. Figure 8c demonstrates the excess volumes of the boundary after all stages of the relaxation. As can be seen from the figure, the simulation with the different potentials hardly changes the distribution of the GB excess volume. Another parameter that characterizes the boundary structure is the radial distribution function of atoms (RDF). This parameter determines the degree of crystallinity of the GB structure. Figure 8d demonstrates the RDF of the boundary investigated. The function profiles obtained with the pair (solid line) and many-body (dashed line) potentials qualitatively agree. However, the application of the pair potential results in the higher degree of crystallinity, which is expressed by sharper peaks corresponding to the coordination shells.

Therefore, the comparison of results of the simulation with the pair and many-body potentials demonstrates that they are qualitatively the same.

## CONCLUSIONS

The structural vacancy model of tilt-grain boundaries is developed. The model is based on the CSL model and vacancy and atomic relaxation. The analysis of different methods of searching for the stable states of the boundary shows that the vacancy relax-

ation is more energetically advantageous than the shift one. The grain structures calculated agree with high- resolution-electron-microscopy images.

We studied the influence of the type of potential on the results of simulation of the GB structure in the model under consideration. We have shown that in the cases of the pair and many-body potentials, the boundary structures agree with high accuracy. The energies calculated using the Morse and Cleri-Rosato potentials are overestimated and underestimated in comparison with the experimental value, respectively.

REFERENCES

1. M. L. Kronberg and F. N. Wilson, "Structure of high angle grain boundaries," Trans. AIME 185, 506-508 (1949).

2. V. V. Gorbunov and B. M. Darinskii, "Emission of vacancies by an intercrystallite boundary," Fiz. Tverd. Tela 34, 1059-1063 (1992).

3. M. D. Starostenkov, B. F. Dem'yanov, S. L. Kustov, and E. L. Grakhov, "Symmetric $\Sigma=5$ tilt boundaries in the Ni₃Fe alloy," Phys. Met. Metallogr. 85, 530-535 (1998).

4. A. S. Dragunov, B. F. Dem'yanov, and A. V. Weckman, "Computer simulation of internal interfaces in metals and alloys," Izv. Vyssh. Uchebn. Zaved., Fiz. 53, 82-87 (2010).

5. M. A. Tschopp and D. L. McDowell, "Asymmetric tilt grain boundary structure and energy in copper and alu- minium," Philos. Mag. 87, 3871-3892 (2007).

6. A. N. Orlov, V. N. Perevezentsev, and V. V. Rybin, "Analysis of defects in the crystal structure of a sym- metric tilt boundary," Fiz. Tverd. Tela 17, 1662-1670 (1975).

7. V. V. Rybin and V. N. Perevezentsev, "General theory of grain boundary shifts," Fiz. Tverd. Tela 17, 3188-3193 (1975).

8. W. Bollmann, *Crystal Defects and Crystalline Interfaces* (Springer Verlag, Berlin, 1970).

9. G. H. Bishop and B. Chalmers, "A coincidence-ledge- dislocation description of grain boundaries," Scr. Metall. 2, 133-139 (1968).

10. L. K. Fionova, "Ordinary grain boundaries," Phys. Met. Metallogr., 73, 333-336 (1992).

11. G. Hasson, J. Y. Boos, J. Herbeuval, M. Biscondi, and E. C. Goux, "Theoretical and experimental determina- tion of grain boundary structures and energies: Correla- tion with various experimental results," Surf. Sci. 31, 115-137 (1972).

12. M. F. Ashby, F. Spaepen, and S. Williams, "The struc- ture of grain boundaries described as a packing of poly- hedra," Acta Metall. 26, 1647-1664 (1978).

13. R. C. Pond, D. A. Smith, and V. Vitek, "Computer simulation of $\langle 110\rangle$ tilt boundaries: Structure and sym metry," Acta Metall. 27, 235-241 (1979).

14. J. D. Bernal, "The Bakerian Lecture, 1962. The Struc- ture of Liquids," Proc. R. Soc. London, Ser. A 280 (1382), 299-322 (1964).

15. V. Vitek, "Intrinsic stacking faults in body-centered cubic crystals," Philos. Mag. 18 (154), 773-786 (1968).

16. D. A. Smith, V. V. Vitek, and R. C. Pond, "Computer simulation of symmetrical high angle boundaries in aluminium," Acta Metall. 25, 475-483 (1977).

17. M. J. Weins, H. Gleiter, and B. Chalmers, "Computer calculations of the structure and energy of high-angle grain boundaries," J. Appl. Phys. 42, 2636-2645 (1971).

18. P. D. Bristowe and A. G. Crocker, "A computer simu- lation study of the structures of twin boundaries in body-centered cubic crystals," Philos. Mag. 31, 503-517 (1975).

19. E. Tarnow, P. D. Bristowe, J. P. Joannopoulos, and M. C. Payne, "Predicting the structure and energy of a grain boundary in germanium," J. Phys.: Condens. Matter 1, 327-333 (1989).

20. P. Guyot and J. P. Simon, "Symmetrical high angle tilt boundary energy calculation in aluminium and lith- ium," Phys. Status Solidi A 38, 207-216 (1976).

21. H. Gleiter and B. Chalmers, *High-Angle Grain Bound- aries* (Pergamon, Oxford, U. K. 1972; Mir, Moscow, 1975).

22. A. N. Orlov, V. N. Perevezentsev, and V. V. Rybin, *Grain Boundaries in Metals* (Metallurgiya, Moscow, 1980) [in Russian].

23. O. A. Kaibyshev and R. Z. Valiev, *Grain Boundaries and Properties of Metals* (Metallurgiya, Moscow, 1987) [in Russian].

24. Ch. V. Kopetskii, A. N. Orlov, and L. K. Fionova, *Grain Boundaries in Pure Metals* (Nauka, Moscow, 1987) [in Russian].

25. D. Wolf, "Effect of interatomic potential on the calcu- lated energy and structure of high-angle coincident site grain boundaries-I. (100) twist boundaries in alumi- num," Acta Metall. 32, 242-258 (1984).

26. D. Wolf, "Structure-energy correlation for grain boundaries in fcc metals-I. Boundaries on the (111) and (100) planes," Acta Metall. 37, 1983-1993 (1989).

27. D. Wolf, "Structure-energy correlation for grain boundaries in fcc metals-II. Boundaries on the (110) and (113) planes," Acta Metall. 37, 2823-2833 (1989).

28. J. D. Rittner and D. N. Seidman, " $\langle 110\rangle$ symmetric tilt grain-boundary structures in fcc metals with low stack- ing-fault energies," Phys. Rev. B 54, 6999-7015 (1996).

29. J. S. Braithwaite and P. Rez, "Grain boundary impuri- ties in iron," Acta Mater. 53, 2715-2726 (2005).

30. A. G. Lipnitskii, A. V. Ivanov, and Yu. R. Kolobov, "Studying grain-boundary stresses in copper by the molecular-statistics method," Phys. Met. Metallogr. 101, 303-309 (2006).

31. M. A. Tschopp and D. L. McDowell, "Structures and energies of $\Sigma 3$ asymmetric tilt grain boundaries in cop per and aluminium," Philos. Mag. 87, 3147-3173 (2007).

32. R. Matsumoto, M. Riku, S. Taketomi, and N. Miyazaki, "Hydrogen-grain boundary interaction in Fe, Fe-C, and Fe-N systems," Prog. Nucl. Sci. Technol. 2, 9-15 (2011).

33. A. I. Tsaregorodtsev, N. V. Gorlov, B. F. Dem'yanov, and M. D. Starostenkov, "The atomic structure of the antiphase boundary and its effect on the lattice state

near a dislocation in ordered alloys with $L1_2$ superstructure," Fiz. Met. Metalloved. 58, 336-343 (1984).

34. W. Krakow, "Structural multiplicity observed at a $\Sigma5/[001]$ $53.1^\circ$ tilt boundary in gold," Philos. Mag. A 63, 233-240 (1991).

35. F. Cosandey, S.-W. Chan, and P. Stadelmann, "HREM studies of [001] tilt grain boundaries in gold," Colloq. Phys. Colloq. Cl. 51, 109-113 (1990).

36. M. S. Daw and M. I. Baskes, "Embedded-atom method: Derivation and application to impurities, surfaces and other defects in metals," Phys. Rev. B 29, 6443-6453 (1984).

37. M. S. Daw, S. M. Foiles, and M. I. Baskes, "The embedded-atom method: a review of theory and applications," Mater. Sci. Rep. 9, 251-310 (1993).

38. F. Ercolessi, E. Tosatti, and M. Parrinello, "Au (100) surface reconstruction," Phys. Rev. Lett. 57, 719-722 (1986).

39. F. Ercolessi, M. Parrnello, and E. Tosatti, "Simulation of gold in the glue model," Philos. Mag. 58, 213-226 (1988).

40. M. W. Finnis and J. E. Sinclair, "A simple empirical N-body potential for transition metals," Philos. Mag. A 50, 45-55 (1984).

41. A. P. Sutton and J. Chen, "Long-range Finnis-Sinclair potentials," Philos. Mag. Lett. 61, 139-146 (1990).

42. H. Rafii-Tabar and A. P. Sulton, "Long-range Finnis- Sinclair potentials for f.c.c. metallic alloys," Philos. Mag. Lett. 63, 217-224 (1991).

43. B. R. Eggen, R. L. Johnston, S. Li, and J. N. Murrell, "Potential energy functions for atomic solids. IV. Reproducing the properties of more than one solid phase," Mol. Phys. 76, 619-633 (1992).

44. H. Cox, R. L. Johnston, and J. N. Murrell, "Empirical potentials for modelling solid, surfaces and clusters," J. Solid State Chem. 145, 517-540 (1999).

45. D. Wolf, "Correlation between the energy and structure of grain boundaries in bcc metals. I. Symmetrical boundaries on the (110) and (100) planes," Philos. Mag. B 59, 667-680 (1989).

46. J. Th. M. De Hosson and V. Vitek, "Atomic structure of (111) twist grain boundaries in f.c.c metals," Philos. Mag. A 61, 305-327 (1990).

47. N. Takata, K. Ikeda, H. Nakashima, and H. Abe, "Grain boundary energy and atomic structure of symmetric tilt boundaries in copper, Nippon Kinzoku Gakkaishi 68, 240-246 (2004).

48. F. Cleri and V. Rosato, "Tight-binding potentials for transition metals and alloys," Phys. Rev. B 48, 22-33 (1993).

49. J. P. Hirth and J. Lothe, *Theory of Dislocations* (McGraw-Hill, New York, 1967; Atomizdat, Moscow, 1972).

Translated by O. Golovnya