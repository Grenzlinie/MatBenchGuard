# Interfacial interactions and dispersion relations in carbon–aluminium nanocomposite systems

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2008 Nanotechnology 19 285701

(http://iopscience.iop.org/0957-4484/19/28/285701)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 130.63.180.147
This content was downloaded on 12/08/2014 at 12:23

Please note that [terms and conditions apply]().

# Interfacial interactions and dispersion relations in carbon-aluminium nanocomposite systems

Woong Lee¹, Soonmin Jang², Min Jun Kim³ and Jae-Min Myoung⁴,⁵

¹ School of Nano and Advanced Materials Engineering, Changwon National University, 9 Sarim-Dong, Changwon, Gyoungnam 641-773, Republic of Korea
² Department of Applied Chemistry, Sejong University, 98 Gunja-Dong, Seoul 143-747, Republic of Korea
³ Department of Mechanical Engineering and Mechanics, Drexel University, 3141 Chestnut Street, Philadelphia, PA19104-2875, USA
⁴ Department of Materials Science and Engineering, Yonsei University, 134 Shinchon-Dong, Seoul 120-749, Republic of Korea

E-mail: jmyoung@yonsei.ac.kr

Received 11 December 2007, in final form 24 March 2008
Published 2 June 2008
Online at stacks.iop.org/Nano/19/285701

## Abstract
The interactions between a graphene sheet and an aluminium (111) layer in carbon-aluminium nanocomposite systems were investigated for various interfacial configurations using an *ab initio* simulation based on density functional theory. Dispersion relations and electron density distributions obtained for various interface registries suggest that the bond strength of the graphene/Al nanocomposite interface can be controlled by the introduction of compressive in-plane strain and/or by the removal of some atomic rows along specific crystallographic directions in the Al(111) layer. Such changes in the interfacial strength accompanied the evolution of C-Al interaction from weak secondary type to partially covalent type with successive removal of Al atom rows until the state of an 'effectively isolated' Al atom is reached. The application of the present simulation results to the selection of suitable material processing was also addressed.

---

## 1. Introduction
One promising field in the application of nanotechnology, exploiting the unique properties of nanostructures, is lightweight high-strength nanocomposites. In the field of nanocomposites, it is expected that when reinforcements are combined with matrices at a molecular level, material properties exceeding those estimated from the simple rules of the mixture are achieved [1]. Among the many candidate nanoreinforcement structures, carbon nanostructures such as carbon nanotubes (CNTs), fullerenes and graphene sheets have drawn attention due to their high elastic moduli, strengths, and chemical stabilities (affinity with the matrix materials) [2]. Thus, attempts have been made to develop nanocomposites based on carbon nanostructures embedded in various types of matrix material, especially polymers [3-6]. In order for any composite materials to function properly with desired strengths and fracture toughnesses, the interfaces between the matrices and the reinforcements must be designed with optimized properties to ensure a sufficient level of load transfer as well as resistance to the propagation of matrix cracks through the operation of crack stopping mechanisms initiated by crack deflection at the interfaces [7].

Whereas interfaces in nanocomposites based on carbon nanostructures and polymer matrices have been the subject of intensive theoretical and experimental research recently [8-11], even experimental works on metal matrix counterparts have been rare. This is primarily because of the difficulty of dispersing CNTs or other carbon nanostructures in metal matrices without chemical reactions between the two,

⁵ Author to whom any correspondence should be addressed.

since most metals for structural applications can easily combine with nanosized carbon structures to form carbides at typical processing temperatures, i.e. above the melting temperature [12, 13]. Considering their stability at elevated temperatures and resistance to wear, the development of metal matrix nanocomposites will find many structural applications in the future. In the design of nanocomposites, characterizing the bonding nature of interface is of fundamental importance from the viewpoint of both the interface design and the choice of suitable material processing since the interfacial interactions between the reinforcements and the matrices determine the overall performance of the composites and the chemical stability of the reinforcements during processing as well as in service.

While it is expected that the interfacial interaction at the nanometre scale would be different from what happens at interfaces in bulk materials, the sizes of the reinforcements in the nanocomposites practically hinders experimental characterizations. Therefore, modelling and simulation techniques can play important roles in the prediction of interactions at nano-interfaces [14]. In this regard, *ab initio* and molecular dynamic (MD) simulations have been carried out on various CNT/polymer interfaces within the framework of multi-scale simulations [9, 10, 15, 16]. In the *ab initio* simulations, interatomic or intermolecular interactions are usually investigated to identify the nature of bonding and to generate potential profiles to be used in the upper level MD simulations for the characterization of interfaces in terms of mechanical behaviour or redistribution of molecules and atoms around the interface [15, 17, 18].

As for the characterization of the interfaces between carbon and aluminium, some pioneering works are available, but these, for the most part, detail the chemical interactions between individual atoms and small-scale nanoclusters [19, 20], or the overall cohesion–separation behaviour of graphite/aluminium interfaces or diamond/aluminium at the bulk scale [21, 22]. Therefore, in the current study, interfacial interactions between carbon and aluminium layers were considered within the framework of density functional theory (DFT) from the viewpoint of the dispersion relations (the bonding energy as a function of interlayer distance) and electronic interactions for various interface registries (arrangement of atoms). This would provide a basic understanding of the interfaces between carbon nanostructures and aluminium at the nanometre scale. First, potential energy variations as a function of separation distances between a graphene sheet and an Al(111) layer are obtained, then the nature of interfacial reactions is discussed based on the fitting of the potential energy profiles to various types of pair potential, and the electron density distribution as well as the wavefunctions of valence electrons around the interfacial region.

## 2. First-principle simulations

A graphene sheet was chosen as the model carbon nanostructure for computational convenience since its electron structure with $\mathrm{sp}^{2}$ hybrid orbitals is closely related to that of CNTs and fullerenes [23, 24], while graphene sheets are themselves regarded as a promising candidate for reinforcements in carbon-based nanocomposites [25]. The geometry used for calculations is based on a graphene sheet and one layer of the Al(111) plane with some modifications to the number of layers wherever necessary. Figure 1 shows the configurations of atoms in the graphene–Al model composite system. Atomic configurations were varied by considering different possible arrangements of Al atoms on the (111) plane with respect to the positions of carbon atoms in the graphene sheet. Since previous works on graphite (0001)/Al(111) systems by other research groups [21, 22] considered the strain-free Al(111) plane matched to the graphite (0001) plane, i.e. graphene sheet, in this study, two such configurations, shown in figure 1(a) and denoted as SFR-1 and SFR-2, respectively, are considered first as reference states. Another possible interfacial configuration accompanies compressive strains on the Al(111) plane. With 14.4% of compressive strain, the Al(111) plane can be matched to graphene sheet coherently. Three possible cases are considered: namely, those denoted as H-1 (Al atoms over the centres of hexagonal rings of the graphene sheet, i.e. hollow sites), T-1 (Al atom over C atoms, i.e. top sites), and B-1 (Al atoms over interatomic bridging sites of the C–C bond), respectively, in figure 1(b). If the strains are excessive, it is also possible that strain relief is achieved by the removal of some atoms from the atomic plane to form a semi-coherent interface. Therefore, based on H-1, T-1 and B-1 geometries, such relaxed configurations were considered by removing one or two atomic rows from the Al(111) plane. For instance, the H-2 and H-3 configurations shown in figure 1(c) represent the cases of missing atomic rows along every other $[\overline{1}10]$ and $[\overline{1}\overline{1}2]$ directions, respectively.

In the *ab initio* simulations in this study, geometry optimizations were carried out first for each registry by allowing the atoms in the model to move freely within the unit cell during the simulation. It was predicted that the changes in the in-plane positions of the atoms after the geometry optimizations were negligible, typically in the range of 0.1 bohr. At the same time, the vertical displacements from the plane of the layers (graphene and Al(111)) were also in a similar range. As these displacements from the original positions are negligibly small compared with the interatomic bond lengths of the component layers, for computational convenience, further calculations were carried out on fixed geometries.

Using the atomic configurations shown in figure 1, dispersion relations and corresponding interfacial interactions for the graphene–aluminium systems were predicted through DFT calculations in which the local density approximation (LDA) is implemented based on a plane wave basis set and separable pseudopotentials. The open source *ab initio* simulation package ABINIT [26, 27] was used with Troullier–Martins-type LDA pseudopotentials [28] for the calculations. Concerning the use of the LDA for the calculations, one may raise a question that the LDA may not be suitable for the calculation of possible long-range interactions between the graphene and the Al layers. Preliminary calculations in this study and the existing work [21] suggest that a higher-level scheme, such as the generalized gradient

![](./images/811917253426544640_1.jpg)

Figure 1. Possible arrangements of constituent atoms in the model graphene/Al(111) nanocomposite system used for the ab initio simulations. (This figure is in colour only in the electronic version)

approximation (GGA), would require potentials based on the all-electron projector-augmented wave method, resulting in computationally intensive jobs. In other preliminary calculations on the well-known system of graphite (to be discussed in the following section), the long-range interaction leading to the secondary bonding between the (0001) layers was successfully handled. Hence, in this study the LDA scheme was adopted as in the previous study on the bulk graphite-aluminium system by Qi et al [22].

In order to obtain the dispersive energy profiles, the system energies were estimated for each graphene-Al(111) distance, $d$, ranging from 2 to 18 bohr with an increment of 0.1 bohr. Taking the case of $d=18$ bohr as the reference state, i.e. the effective infinite separation of the layers, the relative changes in system energies were calculated for each increment of $d$. Once the system energy was obtained, the dispersive relation was fitted to several known classical potentials such as the embedded atom method (EAM) ([32-34]), Morse-type and Mie $(m,n)$ potentials. For this fitting, the total system energy of a unit cell was divided by the number of Al atoms in the unit cell to represent the system energy in the form of the potential energy change 'felt' by an Al atom in the system. Hence, the potential energy profile as a function of the interspecies distance would be an averaged pair-wise sum on all particles. In other words, it would represent an interaction between an Al atom and a small unit of a graphene molecule. Interfacial interactions between the graphene sheet and the Al(111) layer were then estimated by calculating the electron density and the wavefunctions for the lowest potential energy state. Considering the periodicity or translational symmetry of the atomic configurations, all the calculations were carried out for unit cells (marked with dotted lines in figure 1). Infinity in the vertical direction was simulated by taking a sufficient vertical dimension of the unit cell determined from preliminary calculations.

## 3. Results and discussion

Before the detailed discussion on the interfacial interactions in the graphene-Al(111) system, it was first justified that long-range interactions can be handled within the LDA scheme with the ABINIT package by considering the interactions between the (0001) planes of graphite along the [0001] direction.

![](./images/811917253426544640_2.jpg)

Figure 2. (a) Changes in the potential energy of the graphite system with the distance between the (0001) planes and its fitting to the Mie (12, 6) potential; (b) wavefunction plot showing the delocalization of $\pi$-electrons around the hexagonal carbon rings.

![](./images/811917253426544640_3.jpg)

Figure 3. (a) Changes in the potential energy of the system with the distance between the graphene sheet and the Al(111) plane (potential energy profile) for the SFR-1 registry and its fitting to various pair potentials; (b) contour plot showing the electron density distribution near the C-Al interface for the SFR-1 registry at the equilibrium separation distance.

Figure 2(a) shows how the potential energy varies as two (0001) plane of graphite approach each other along the [0001] direction. It can be seen that the cohesive energy, i.e. the interatomic potential energy of the C-C interaction between the graphitic layers, was calculated to be about 20.6 meV at an equilibrium separation distance of about 3.31 Å. These values are consistent with the theoretical and experimental values reported elsewhere [29-31]. Further, the profile of the potential energy curve can be fitted reasonably to the Lennard-Jones potential representing the van der Waals bonding between the (0001) planes of graphite. As for the behaviour of the valence electrons, the *ab initio* simulation successfully predicted the wavefunction for the delocalized $\pi$-electrons around the hexagonal carbon ring, as shown in figure 2(b). Therefore, it is believed that the LDA scheme employed herein would be sufficient to handle the possible long-range interaction between graphene and the Al(111) layers considering that the use of the GGA scheme may require computationally intensive all-electron calculations [21].

Having justified the use of the LDA scheme, interfacial interactions in the C-Al nanocomposite system are now explored. The fundamental unit in the graphite-aluminium nanocomposite system consists of a single graphite (0001) layer, i.e. graphene sheet, and a single Al(111) plane. Assuming the strain-free C-Al interface in this system (SFR-1 and SFR-2 registries in figure 1), the potential energy of the system as the Al(111) plane approaches the graphene sheet (or the latter approaches the former) to close proximity from an (effectively) infinite separation was calculated, and the results are shown in figure 3(a). It can be seen in figure 3(a) that as the distance between the Al(111) layer and the graphene sheet decreases, the potential energy of the system also decreases with respect to the isolation state, meaning that each plane exerts an attractive force on the other. In figure 3, the potential profile for the SFR-2 registry is not shown since it is identical to that for the SFR-1 registry. With closer distance, the system energy decreases further and subsequently reaches a minimum of about $-0.185$ eV at an equilibrium separation distance of about 2.48 Å. Further decrease below the equilibrium distance then results in a predomination of repulsion force, as reflected in a steep increase in the potential energy at very close interspecies distances.

The equilibrium distance between the graphene and the Al(111) layers of 2.48 Å is smaller than the graphitic interlayer

distance of about 3.36 Å and somewhat larger than the Al(111) interplanar distance of about 2.31 Å. Also, the depth of the potential well or the cohesive energy of the C-Al interface, i.e. the difference in the potential energies at equilibrium and at infinite separations, is about 0.185 eV, approximately 4.4 times the reported interfacial cohesive energy of 0.0417 eV for the bulk graphite-Al system [22]. These values of the equilibrium distance and the cohesive energy for the C-Al system herein indicate a possibility that the interface bonding of the C-Al nanostructure at the fundamental unit level is not simply a van der Waals type that often exists in bulk composite systems [7].

For further investigation of the rather 'complex' dispersion relations in the graphene-Al(111) system in this study, the potential energy profile was fitted to various types of interatomic (or intermolecular) potential, and the results are compared with the *ab initio* simulation result in figure 3(a). It can be seen that the potential energy profile can be fitted either to Morse-type potential [32] or to the so-called 'universal equation of state (EOS)' proposed by Rose *et al* [33] to express the EAM potentials for metals. At the same time, it is noticed that the *ab initio* result can be fitted to a Mie potential [34] with (8, 4) exponents rather than (12, 6) exponents for typical van der Waals type bonding. These fitting results imply that the C-Al interaction in the graphene/Al(111) two-layer system is of metallic to semi-metallic nature, reflecting the characteristics of the components of the system and resembling initial wetting in the deposition of metallic films on semi-metallic substrates [35].

Such a deduction is supported by the electron density plots of figure 3(b), which show the contours of electron densities, i.e. electron distribution probabilities, in the vicinity of individual atoms. In this plot, contour bands in red to yellow colour indicate relatively higher electron densities whereas those in green to blue colour represent lower densities. Thus, in figure 3(b), the cylindrical symmetry of the $\sigma$-bond between carbon atoms in the graphene sheet is clearly visible. Simultaneously, 'seas of valence electrons' or 'electron clouds' enveloping the ion cores of the Al(111) layer and the $\sigma$-bonded carbon atoms, respectively, are also noticed. It should be mentioned that core electrons are not plotted in figure 3(b) since the *ab initio* calculation is based on a pseudopotential method in which only the valence electrons are considered. In figure 3(b), it is obvious that there is some overlapping of electron clouds between the Al(111) layer and the graphene sheet while the electron density of the overlapped region is about 0.04 bohr$^{-3}$, which is in the same range as that of the electron cloud in the Al(111) layer. Together with the overlapping of electron clouds between the layers, there are small regions where electron density is almost 0, implying that sharing of electrons in the interfacial region is slightly localized. This partial localization is consistent with the previous work by Qi *et al* on the bulk graphite/Al interface [21]. However, overlapping of electron clouds is neither $\sigma$- nor $\pi$-bond type in this case. This, together with the magnitude of the cohesive energy, i.e. 0.185 eV, and with the fitting results, suggests that the bonding between a graphene sheet and single Al(111) layer is metallic or semi-metallic to a certain degree.

The numerical results in figure 3 indicate that the cohesive energy at the C-Al interface in the current nanosystem is substantially larger than that for the bulk C-Al system reported previously (0.0417 eV) [22]. In order to address this point, two more nanosystems were considered: in one system, an additional Al(111) plane was added in the simulation model following the stacking sequence of face-centred cubic (fcc) Al along the [111] direction; and in the other system, an additional graphene sheet was added following the stacking sequence of graphite along the [0001] direction. In figure 4, potential energy-distance curves and electron density distributions for these systems are presented. Figures 4(a) and (b) represent the potential energy and corresponding electron density for the system constituted of a graphene sheet and double Al layers, respectively, while figures 4(c) and (d) are representative of the system constituted of double graphene layers and a single Al layer.

With the addition of one more Al(111) plane to the system, as shown in figure 4(a), the equilibrium separation distance increased slightly to about 2.65 Å, whereas the cohesive energy decreased somewhat to about 0.158 eV. Again, the dispersion relation can be fitted to the Morse-type potential, the universal EOS and the Mie (8, 4) potential. As for the electron density distributions, figure 4(b) shows that the overlapping of electron clouds in the C-Al interface region is reduced in the system composed of two Al(111) layers and a graphene sheet, which is consistent with weaker interface bonding reflected in the reduced cohesive energy from 0.185 to 0.158 eV. On the other hand, when one more graphene sheet was added, as seen in figure 4(c), the potential energy has the minimum value of $-0.155$ eV at an equilibrium separation distance of 2.54 Å. In this system, although the equilibrium distance is shorter and the decrease in the overlapping of electron clouds in the C-Al interface region is less appreciable, as seen in figure 4(d), the interfacial cohesive energy is almost the same as that of the system with a single graphene sheet and two Al(111) layers. This is attributed to the slightly more delocalized electrons along the plane direction for the double graphene layer and single Al(111) layer.

Comparison of figures 3(a) and (b) with 4(c) and (d) suggests that in composite systems with double-layered carbon nanostructures, e.g. a double-walled nanotube (DWNT), and Al, weaker interfaces are expected as compared to those with single-layered carbon nanostructure such as a single-walled nanotube (SWNT). It is further suggested that the initial wetting behaviour of Al on the graphene-related nanostructure in the C-Al system would be dependent on the type of the carbon structure since the cohesive energy, and therefore the surface energy, varies with the number of graphene layers in the carbon nanostructure. In any case, eventually, the numerical predictions presented in figure 4 indicate that increasing the number of the graphene sheets and/or the Al(111) layers would results in a decrease in the cohesive energy and an increase in the equilibrium C-Al separation distance towards the values for the bulk system. This in turn implies that the bonding of the C-Al interface changes from chemical type to physical type as the structural pair evolves from the nanolayers to the bulk.

![](./images/811917253426544640_4.jpg)

Figure 4. (a) Potential energy profile of the nanocomposite system with a single graphene sheet and two Al(111) layers and its fitting to various pair potentials; and (b) the corresponding electron density distribution plot; (c) potential energy profile of the system with two graphene sheets and a single Al(111) layer and its fitting to various pair potentials; and (d) the corresponding electron density distribution plot.

When interfaces are formed between dissimilar materials, it is natural to assume that the atoms are arranged in such a way to relieve strains, as in the cases discussed so far. However, it is also possible that strained interfaces can be formed with good epitaxial relations. Notable examples include thin film systems [36], quantum dot systems [37], nanowire arrays [38], etc. Thus, changes in the dispersion relation and interfacial bonding, when strained coherent interfaces are formed between the graphene sheet and Al(111) planes, were also considered. In figure 5(a), the potential energy profiles for three possible coherent interface registries, namely hollow (H-1), top (T-1) and bridge (B-1) shown in figure 1(b) are compared. It is noticed that the dispersion relations are almost identical, regardless of the interface registry. More importantly, it is also noticed that the equilibrium separation distance and the cohesive energy are about 3.86 Å and 0.0835 eV, respectively. Compared with the values for the strain-free interface in figure 3(a), the equilibrium distance is significantly larger (even larger than the Al(111) interplanar distance and graphitic (0001) interplanar distance) and the potential well is much shallower and wider, implying weaker C–Al bonding.

In figure 5(b), the potential energy profile for the H-1 registry is compared with the various types of potential fitted to it. It is seen that the ab initio result for the H-1 registry can be fitted almost exactly to the Morse potential or to the universal EOS and roughly to the Mie (8, 4) potential with a large deviation at small separation distances (highly repulsive region). On the other hand, it is not fitted to the Mie (12, 6) or the Lennard-Jones (L-J) potential, as is evident in the substantial differences at most of the separation distances. Compared with the case of the strain-free C–Al interface shown in figure 3(a), both the Morse potential and the universal EOS fit better, but the Mie potential fits poorer. Concerning the electron densities, figure 5(c) (and also figure 5(d) which presents electron density in different contour scales for a detailed view) shows that there is very low possibility of the overlapping of the 'sea of delocalized electrons' between the graphene sheet and the Al(111) layer (the electron density in the interplanar region is below 0.005 bohr⁻³). This point is clarified by considering the wavefunctions of the valence electrons visualized in figures 5(e) and (f). The ab initio simulations predicted the wavefunction for molecular orbitals of the delocalized $\pi$-electrons in the carbon rings of the graphene layer (figure 5(e)) and the 'sea' of free electrons in the Al layer (figure 5(f)). However, no wavefunction corresponding to any bonding orbitals between C and Al atoms was predicted. The electron density and the wavefunction results suggest that the bonding at the C–Al interface in this H-

![](./images/811917253426544640_5.jpg)

![](./images/811917253426544640_6.jpg)

![](./images/811917253426544640_7.jpg)

![](./images/811917253426544640_8.jpg)

![](./images/811917253426544640_9.jpg)

![](./images/811917253426544640_10.jpg)

Figure 5. (a) Comparison of the potential energy profiles for various strained registries; (b) fitting of the potential energy profile for the H-1 registry to various pair potentials; (c) corresponding electron density distribution plot for the H-1 registry; (d) electron density distribution plot in different contour scale for a detailed view; and wavefunctions showing (e) the delocalized $\pi$-electrons in the graphene sheet and (f) the free electrons in the Al(111) layer.

![](./images/811917253426544640_11.jpg)

Figure 6. (a) Potential energy profile of the nanocomposite system with a single graphene sheet and two Al(111) layers based on the H-1 registry and its fitting to various pair potentials; and (b) corresponding electron density distribution plot.

1 registry is of the weak secondary type, perhaps related to van der Waals bonding, even though the potential energy profile is fitted best to the Morse potential or the universal EOS whilst poorly to the Mie (8, 4) and Mie (12, 6) potentials.

Like the case of the strain-free C-Al system in figure 4, the dispersion relation undergoes significant change with the addition of another Al(111) plane to the strained system, as seen in figure 6(a). Now, the cohesive energy is markedly reduced to 0.0309 eV and the equilibrium C-Al separation distance is increased to 4.13 Å. Regarding the electron distributions, the 'sea of valence electrons' in the Al region is separated from the cloud of delocalized electrons belonging to the graphene sheet with very low possibility of sharing, as shown in figure 6(b). Therefore, it is expected that in the graphene-Al system with the strained coherent C-Al interface, the interfacial cohesive energy would become very weak. This prediction implies a possibility of 'controlling' the interfacial bond strength in the graphene-Al system with the introduction of a strained epitaxial graphene/Al(111) interface.

Comparison of the dispersion relations and electron densities shown in figures 3 and 5 raises a question as to the cause of the noticeable differences in the shapes of the potential energy profiles, cohesive energies, and equilibrium separations leading to the differences in the type of interface bonding with minor differences in the interface registry. One possible reason is found from the comparison of the electron densities shown in figures 3(b) and 5(c). In the strained Al(111) layer, the compressive strain means a closer interatomic distance, which would result in higher electron density in the 'sea of valence electrons'. Whereas the electron density in the strain-free Al(111) layer is about $0.04\ \text{bohr}^{-3}$, in the strained Al(111) layer, it is $0.06\ \text{bohr}^{-3}$. In terms of the number of valence electrons (not participating in covalent bonding) in the unit area, there are 1.5 and 1.125 electrons from Al for every electron from C in strained and strain-free systems, respectively. This compares well with the electron densities of $0.06\ \text{bohr}^{-3}$ and $0.04\ \text{bohr}^{-3}$ in the strained and strain-free Al(111) layers, respectively. Increased electron density causes the contribution of repulsion to be larger in the C-Al interaction at the interface since electrons tend to exist away from each other. This in turn would result in the wider equilibrium C-Al separations in the strained system. Thus, it is deduced that compressive strains in the Al(111) plane can reduce the tendency for Al atoms to chemically combine with C atoms to form carbides such as $\text{Al}_4\text{C}_3$ which often exist in C-Al composite systems prepared at relatively higher temperatures comparable to the melting point of Al. From a practical point of view, this deduction suggests that introduction of compressive strains in the aluminium matrix region would provide the means to ensure the chemical stability of reinforcements based on graphene-related carbon nanostructures in the C-Al nanocomposite systems.

The effect of the compressive strain on the C-Al interaction was thus investigated further with the partially relaxed registry, denoted as H-2 in figure 1 (and also with the related displaced registry derived from top and bridge configurations, i.e. T-2 and B-2, respectively). In this interface registry, the strain along the $[\bar{1}\bar{1}2]$ direction is completely relaxed since one row of Al atoms is missing, but there is still about 14.4% of the compressive strain along the $[\bar{1}10]$ direction. In such a case, the ab initio simulation predicts a cohesive energy increase to 0.123 eV and an equilibrium separation distance increase to $4.03\ \text{Å}$ (these values being slightly registry dependent) as shown in figure 7(a), as compared to the case of the strained coherent interface (figure 5). Even in such a case, the potential energy-distance relation can still be represented as both the Morse potential and the universal EOS, as shown in figure 7(b) for the H-2 registry, while the universal EOS shows better fitting. However, the effect of the large equilibrium separation distance is evident in the electron density distribution shown in figure 7(c) for the H-2 registry (and in figure 7(d) with a different contour scale for a detailed view).

In figures 7(c) and (d), it is also noticed that a removal of one row of Al atoms along every other $[\bar{1}10]$ direction resulted in a discontinuity in the 'sea of valence electrons', in other words some degree of electron 'localization', in the relaxed Al(111) layer. It is thus inferred that the partially 'localized' electron would increase the electron density near the Al atoms (up to $0.08\ \text{bohr}^{-3}$), which would in turn

![](./images/811917253426544640_12.jpg)

![](./images/811917253426544640_13.jpg)

![](./images/811917253426544640_14.jpg)

![](./images/811917253426544640_15.jpg)

![](./images/811917253426544640_16.jpg)

![](./images/811917253426544640_17.jpg)

Figure 7. (a) Comparison of the potential energy profiles for various partially relaxed registries; (b) fitting of the potential energy profile for the H-2 registry to various pair potentials; (c) corresponding electron density distribution plot for the H-2 registry; (d) electron density distribution plot in different contour scale for a detailed view; and wavefunctions showing (e) the delocalized $\pi$-electrons in the graphene sheet and (f) the partially localized electrons in the Al layer.

cause stronger repulsion toward the delocalized electrons in the graphene sheet, resulting in the increased equilibrium separation distance to 4.03 Å. Such behaviour of the valence electrons can be clarified in the forms of the wavefunctions. Figures 7(e) and (f) show the delocalized $\pi$-electrons around the carbon rings in the graphene layer and partially localized 'free' electrons in the Al(111) layer, respectively. Some localization of the electrons may endow the Al atoms with the characteristic of somewhat 'isolated' atoms causing a stronger tendency for the Al atoms to react (chemically) with the C atoms, as reflected in the increased cohesive energy of 0.123 eV. However, as in the case of the H-1 registry, no wavefunction corresponding to any bonding orbital between C and Al atoms was predicted, which is reflected in the increased equilibrium separation distance as compared to the case of the H-1 registry.

With further removal of rows of Al atoms along every other $[\overline{1}\overline{1}2]$ direction from the Al(111) plane to relieve the strain completely (registry H-3 in figure 1 and related displaced registry derived from top and bridge configurations, i.e. T-3 and B-3, respectively), the characteristic of the interfacial interaction changes substantially. In this relaxed registry, the nearest-neighbouring atoms in the Al(111) plane are all missing and the interatomic distance between Al atoms are 4.90 Å along the $[\overline{1}10]$ direction and 4.24 Å along the $[\overline{1}\overline{1}2]$ direction, significantly larger than the normal value of 2.86 Å in the (111) plane. Thus, the Al atoms in this relaxed registry may be treated as effectively isolated atoms. In such a case, as shown in figure 8(a), the equilibrium separation distance between the graphene sheet and the Al layer becomes shorter and the cohesive energy becomes larger to form a deep and narrow potential well, as compared to the other cases in figures 3–7. Moreover, the dispersion relations are now dependent on the interface registry. Thus, the equilibrium distances are 2.03, 2.36 and 2.26 Å for the hollow (H-3), top (T-3) and bridge (B-3) registries, respectively, and the corresponding cohesive energies are 0.669, 0.489 and 0.393 eV, respectively. As for the cohesive energy of 0.669 eV for the hollow registry, this value is close to the reported value of the binding energy of 0.8 eV of Al atoms on graphite surfaces by Ganz et al [39]. Whilst shorter equilibrium separation distances and larger cohesive energies are predicted for the (effectively) isolated registry as compared to other registries, the dispersion relation can be represented by either the Morse potential or the universals EOS, as shown in figure 8(b) for the H-3 registry.

The dependence of the equilibrium separations and the cohesive energies on the registries shown in figure 8(a), together with the shortest equilibrium distance and the deepest potential well, indicate that (effectively) isolated Al atoms in the fully relaxed geometry tend to form chemical bonds with the C atoms in the graphene sheet. Indeed, the electron density plot for the H-3 and B-3 registries in figures 8(c) and (d), respectively, shows that there is sharing of electrons between C and Al atoms, which is an indication of the formation of covalent bonding possibly related to the carbide of aluminium, $Al_4C_3$.⁶ The formation of chemical bonds between the C and Al atoms is evident in the wavefunction plots shown in figures 7(e) and (f). From the wavefunctions shown in figures 7(e) and (f), it is deduced that the bondings between the C and the Al atoms are formed by the sharing of electrons between an isolated Al atom and the carbon ring of the graphene layer or between an Al atom and two diagonal C atoms in the carbon ring.

From the viewpoint of material processing, these results can be interpreted in the following manner. If any composite preparation process is chosen so that Al atoms approach the graphene-based nanoreinforcement individually (effectively isolated Al atom), then it is likely that the Al atom will form the carbide. On the other hand, if Al atoms approach the reinforcement in a coplanar group, especially with compressive in-plane strain, it is possible that a relatively weak graphene–Al interface is formed without any decomposition of the graphene-based reinforcement. Therefore, in processing for the preparation of an Al-matrix nanocomposite with carbon nanostructure reinforcement, powder metallurgy or a related technique is preferred to the melting-based techniques.

In addition to the interfacial strengths, the registry- dependent dispersion relations imply the controllability of 'stiffness' properties of the interfaces which are strongly re- lated to the overall mechanical properties of the compos- ites [7, 16]. Whilst the cohesive energy indicates the strength of the interface, the second derivative or the curvature of the potential energy curve near the equilibrium position can be re- lated to the elastic modulus of a material. Hence, in figure 9, dispersion relations for various registries are compared by tak- ing the equilibrium separation distances and the minima in the potential energy as 0, respectively. Figure 9 shows that the po- tential energy profiles are more or less parabolic near the equi- librium position provided that the displacement (deformation) is small, which enables the comparison of the 'stiffness' of the interfaces based on the second derivatives of the potential pro- files. It can be seen in figure 9 that the potential energy curve for the strained registry (H-1 and H-2) has a smaller curva- ture than that for the strain-free registry (SFR-1). In addition, figure 9 shows that the curvature of potential energy profiles increases substantially when the isolated state (H-3 registry) is reached. Hence, it is deduced from figure 9 that the intro- duction of in-plane compressive strains in the Al(111) layer would yield more compliant interfaces, whereas relaxation of the strain tends to form stiffer interfaces in terms of the resis- tance to deformations by external forces. Therefore, it is ex- pected that nanocomposites with tailored interface properties could be obtained via the control of the strains in the Al-matrix region, i.e. the control of interface registry.

⁶ For comparison purposes, the interaction between the graphene sheet and an effectively isolated Mg atom was also considered (result not shown). The equilibrium separation and cohesive energy were predicted to be 3.28 Å and 0.0786 eV, respectively, leading to a wide and shallow potential well in the dispersion relation. At the same time, an electron density plot (not shown) showed no indication of electron sharing between Mg and C atoms. These predictions are consistent with the knowledge that there is no known carbide of magnesium at atmospheric pressure [13].

![](./images/811917253426544640_18.jpg)

![](./images/811917253426544640_19.jpg)

![](./images/811917253426544640_20.jpg)

![](./images/811917253426544640_21.jpg)

![](./images/811917253426544640_22.jpg)

![](./images/811917253426544640_23.jpg)

Figure 8. (a) Comparison of the potential energy profiles for various effectively isolated registries; (b) fitting of the potential energy profile for the H-3 registry to various pair potentials; (c) corresponding electron density distribution plot for the H-3 registry; and (d) electron density distribution plot for the B-3 registry; and (e) and (f) wavefunctions showing the formation of the chemical bondings between C and Al atoms in two forms.

![](./images/811917253426544640_24.jpg)

Figure 9. Comparison of the potential profiles near the equilibrium separation distances for various registries.

## 4. Summary and conclusions

A series of *ab initio* simulations was carried out for nanocomposite systems constituted of a graphene sheet and an Al(111) layer with various registries to investigate their dispersion relations, i.e. the bonding energy as a function of interlayer distance, in combination with the electronic structures. It was predicted that the graphene/Al interface at the fundamental nano-unit level has substantially different characteristics from bulk graphite–Al systems in that its type of bonding is partially localized metallic with a cohesive energy substantially larger than that of typical bulk system graphite/Al interface. With the introduction of in-plane compressive strains in the Al(111) layer, the equilibrium interfacial bond length increased, accompanied by a noticeable decrease in the cohesive energy, while the interface bonding became a weak secondary type. On the other hand, relief of the in-plane strain by the removal of atomic rows in specific crystalline directions resulted in increased cohesive energy with a slight increase in the equilibrium separation distance, possibly related to partial localization of electrons in the Al layer. When the state of effectively isolated Al atoms was reached by further removal of the atomic rows to completely relieve the compressive strain, a chemical type of C–Al bonding was predicted to be formed, implying the formation of a carbide. Such results suggest the possibility of controlling the interfacial strengths in the C–Al nanocomposites by varying the interface registries. Simultaneously, the predicted registry dependence of the electronic structures (or the nature of bonding) of the C–Al interface, varying between weak covalent to weak metallic, would provide some guidelines for the proper choice of material processing in the preparation of nanocomposites with suitable interfacial strengths. Even though more rigorous orbital analysis, such as natural bond order analysis [40], may give quantitative orbital characteristics, it is beyond the scope of the current work. Instead, the present study would help identifying the dispersion strength (well depth) and the equilibrium distance of the graphene and the Al(111) layer, thereby predicting the mechanical and physical properties of the interfaces of Al-matrix nanocomposites with graphene- based carbon nanoreinforcements.

## Acknowledgments

This work was supported by Korea Research Foundation Grant funded by the Korean Government (MOEHRD, Grant No. KRF-2004-206-C00012/R08-2004-000-10193-0). Provision of the technical aids in visualizing the wavefunctions by Professor Michel Côté at the University of Montreal is gratefully acknowledged.

## References

[1] Cao G 2004 *Nanostructures and Nanomaterials: Synthesis, Properties and Applications* (London: Imperial College Press)

[2] Bourgoin J-P, Loiseau A and Nierengarten J-F 2004 *Fullerenes and Carbon Nanotubes Nanoscience: Nanotechnology and Nanophysics* ed C Dupas, P Houdy and M Lahmani (Heidelberg: Springer) pp 279–324

[3] Chen H, Muthuraman H, Stokes P, Zou J, Liu X, Wang J, Huo Q, Khondaker S I and Zhai L 2007 *Nanotechnology* **18** 415606

[4] Wang S, Liang Z, Liu T, Wang B and Zhang C 2006 *Nanotechnology* **17** 1551–7

[5] Zhou S, Zhang X, Ding Z, Min C, Xu G and Zhu W 2007 *Composites A* **38** 301–6

[6] Wondmagegn W T and Curran S A 2006 *Thin Solid Films* **515** 2393–7

[7] Hull D and Clyne T W 1996 *An Introduction to Composite Materials* (Cambridge: Cambridge University Press)

[8] Griebel M and Hamaekers J 2006 Molecular dynamics simulations of the mechanical properties of polyethylene-carbon nanotube composites *Handbook of Theoretical and Computational Nanotechnology* vol 9, ed M Reith and W Schommers (Stevenson Ranch, CA: American Scientific Publishers) pp 409–54

[9] Frankland S J V, Caglar A, Brenner D W and Griebel M 2002 *J. Phys. Chem. B* **106** 3046–8

[10] Frankland S J V, Harik V M, Odegard G M, Brenner D W and Gates T S 2003 *Compos. Sci. Technol.* **63** 1655–61

[11] Liu Y J and Chen X L 2003 *Mech. Matter.* **35** 69–81

[12] Ci L, Ryu Z, Jin-Phillipp N Y and Rühle M 2006 *Acta Mater.* **54** 5367–75

[13] Massalski T B (ed) 1990 *Binary Alloy Phase Diagrams* 2nd edn (Materials Park, OH: ASM International)

[14] Srivastava D, Menon M and Cho K 2001 *Comput. Sci. Eng.* **3** 42–55

[15] Odegard G M, Gates T S, Nicholson L M and Wise K E 2002 *Compos. Sci. Technol.* **62** 1869–80

[16] Namilae S 2004 Deformation mechanisms at atomic scale: role of defects in thermomechanical behavior of materials *PhD Thesis* Florida State University

[17] Walther J H, Jaffe R and Halicioglu T 2001 *J. Phys. Chem. B* **105** 9980–7

[18] Werder T, Walther J H, Jaffe R L, Halicioglu T and Koumoutsakos P 2003 *J. Phys. Chem. B* **107** 1345–52

[19] Moullet I 1995 *Surf. Sci.* **331–333** 697–702

[20] Mola E E, Ranea V A and Vicente J L 1998 *Surf. Sci.* **418** 367–75

[21] Qi Y and Hector L G Jr 2004 *Phys. Rev. B* **69** 235401

[22] Qi Y, Hector L G Jr, Ooi N and Adams J B 2005 *Surf. Sci.* **581** 155–68

[23] Ruoff R S, Qian D and Liu W K 2003 *C. R. Phys.* **4** 993–1008

[24] Latil S, Roche S, Mayou D and Charlier J-C 2004 *Phys. Rev. Lett.* **92** 256805

[25] Stankovich S, Dikin D A, Dommett G H B, Kohlhaas K M,
Zimney E J, Stach E A, Piner R D, Nguyen S T and
Ruoff R S 2006 *Nature* **442** 282–6

[26] Gonze X *et al* 2002 *Comput. Mater. Sci.* **25** 478–92

[27] Gonze X *et al* 2005 *Z. Kristallogr.* **220** 558–62

[28] Troullier N and Martins J L 1991 *Phys. Rev. B* **43** 1993–2006

[29] Charlier J-C, Gonze X and Michenaud J-P 1994 *Europhys. Lett.*
**28** 403–8

[30] Girifalco L A and Lad R A 1956 *J. Chem. Phys.* **25** 693–7

[31] Drickamer H G 1967 *Science* **156** 1183–9

[32] Morse P M 1929 *Phys. Rev.* **34** 57–64

[33] Rose J H, Smith J R, Guinea F and Ferrante J 1984 *Phys. Rev.*
B **29** 2963–9

[34] Ali Mansoori G 2005 *Principles of Nanotechnology:
Molecular-based Study of Condensed Matter in Small
Systems* (Hackensack, NJ: World Scientific)

[35] Rafii-Tabar H 2000 *Phys. Rep.* **325** 239–310

[36] Barnham K and Vvedensky D 2001 *Low-dimensional
Semiconductor Structures: Fundamentals and Device
Applications* (Cambridge: Cambridge University Press)

[37] Harrison P 2005 *Quantum Wells, Wires and Dots* (Hoboken,
NJ: Wiley)

[38] Wu Y, Yan H, Huang M, Messer B, Sing J H and Yang P 2002
*Chem. Eur. J.* **8** 1260–8

[39] Ganz E, Sattler K and Clarke J 1989 *Surf. Sci.* **219** 33–67

[40] Foster P and Weinhold F 1980 *J. Am. Chem. Soc.* **102** 7211–8

13