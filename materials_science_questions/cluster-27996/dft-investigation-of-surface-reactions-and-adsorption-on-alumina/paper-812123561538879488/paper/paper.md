# THEORETICAL STUDY OF REACTIONS CATALYZED BY ACIDIC ZEOLITE.

Xavier Rozanska, Rutger A. van Santen and Fran\c{c}ois Hutschka\textsuperscript{#}

Schuit Institute of Catalysis, Technical University of Eindhoven, PO. Box 513, 5600MB Eindhoven, The Netherlands
\textsuperscript{#}TotalFinaElf, European Research and Technical Center, B.P. 27, 76700 Harfleur, France

**Abstract**

After a general introduction on zeolites and their properties, we will show how the current quantum chemical methods allow nowadays the simulation of catalytic models that become more and more realistic. Predictability of activity, selectivity and stability based on known structures of catalysts can be considered the main aim of the theoretical approach to catalysis. Here for a particular class of heterogeneous catalysts, the acidic zeolites, and for a particular class of reactions, the aromatics isomerization reactions, we will describe a quantum mechanic study of a reaction pathway investigation. The cluster approach method as well as electronic structure periodic method will be used for this purpose.

## 1. INTRODUCTION

### 1.1 Zeolite Crystals

The Greek name zeolite has been given to a class of mineral. Zeolite means "boiling stone" in allusion to the behavior of some silicate minerals on heating. This relates to a well-known property of a zeolite that is to adsorb large quantity of water and gases. This is permitted by the microporous structure of zeolite, which can accept an important amount of guest molecules. Zeolites are silicon oxides crystals that show various and well defined microporous structures (see Figure 1). It is this characteristic which makes them interesting molecular sieves for which application they have been employed for many years.\textsuperscript{1}

The zeolite framework is constituted of the assembly of $SiO_4$ tetrahedra which link together by sharing an oxygen atom. The potential energy surface of the zeolite Si-O-Si angle is rather flat,\textsuperscript{2} which explains the large variety of accessible structure that can be accommodated by zeolites.\textsuperscript{3}

The zeolites have been first used as catalyst in the 1960s for alkane cracking reactions in petroleum industry.\textsuperscript{3b} They replaced favorably previously employed alumina based catalysts because of their better thermal and mechanical stability. Moreover, they showed higher selectivity. The selectivity finds its source in the zeolite micropore structure with different

---

M.A. Chaer Nascimento (ed.), *Theoretical Aspects of Heterogeneous Catalysis*, 1-28.
\textcopyright{} 2001 Kluwer Academic Publishers. Printed in the Netherlands.

consequences on the course of a reaction$^{3b,4}$

![](./images/812123561538879488_1.jpg)

Figure 1. Some examples of zeolite structures (the dots depict the Connolly surfaces).

A first, rather obvious reason is the reactant selectivity. As the zeolite micropore channels have a well defined diameter, reactants bigger than this diameter cannot enter within the micropores to react, in case external catalytic active sites of zeolite have been deactivated.$^{4a}$ Smaller reactants than the micropores will be the only ones to get involved in reactions.

Once a reactant molecule has adsorbed within the zeolite mouth, it needs to diffuse toward the active sites in contact of which reactions will occur. This diffusion can be very dependent on the size and shape of the zeolite micropores as well as on the size of the reactants or products. This becomes especially true when the reactants or products have similar size to the micropores diameter.$^{4a}$ After reaction, it is the turn of the products to diffuse away from the micropores.

These stereo-selectivity properties do not only apply to the case of zeolite catalysts but also in the case of zeolite molecular sieves.

After reactants have adsorbed within the zeolite mouth and have diffused towards the actives sites, they must react. Selective adsorption depends on the local topology of the active site, its immediate neighborhood, and on size and shape of the reactant. One may say that a similar behavior as the lock and key principle of molecular recognition known from biochemistry applies. In this sense zeolites can be viewed as analog of enzymatic catalysts.\textsuperscript{5} This adsorption selectivity of the reactants to the active sites favors preferential reaction pathways.

Elementary reaction steps proceed via transition states. Transition state requires a specific geometry that differs for each reactions step. Reaction steps can be favored or prohibited as a function of the available space around the catalytic active site.\textsuperscript{4} This effect is designated as the transition state selectivity.

Whereas selective diffusion can be better investigated using classical dynamic or Monte Carlo simulations,\textsuperscript{6} or experimental techniques,\textsuperscript{7} quantum chemical calculations are required to analyze molecular reactivity. Quantum chemical dynamic simulations provide with information with a too limited time scale range (of the order of several hundreds of ps)\textsuperscript{8} to be of use in diffusion studies which require time scale of the order of ns to s.\textsuperscript{6,7} However, they constitute good tools to study the behavior of reactants and products adsorbed in the proximity of the active site, prior to the reaction. Concerning reaction pathways analysis, static quantum chemistry calculations with molecular cluster models, allowing estimates of transition states geometries and properties, have been used for years.\textsuperscript{9} The application to solids is more recent.

But before continuing the discussion on the quantum chemical simulations, we will give a deeper description of the current understanding of physical chemistry properties of zeolites. We will be using experimental as well as theoretical studies to support the discussion.

### 1.2 Zeolite Properties

It has already been mentioned that zeolites are shape selective with respect to molecular adsorption. This property relates to their micropores structure. The zeolite framework shows a limited flexibility, which is essential. For instance, Yashonath et al.\textsuperscript{10} have shown in their classical dynamic simulations study of molecular diffusion within zeolite micropore that the zeolite framework flexibility affects significantly diffusion when the molecules have a size comparable with the micropore size. To get an idea of the order of magnitude of this flexibility, one can consider the hybrid semi-empirical DFT periodic study of chabazite zeolite of Ugliengo et al.\textsuperscript{11}. They introduced in the unit cell of chabazite Br\textsuperscript{o}nsted acidic sites which are known to induce an increase of the volume of around $10\ \mathring{A}^3$.\textsuperscript{21,12} This increase of the volume relates with the difference of volume between a $SiO_4$ tetraheron and a

$AlO_3(OH)$ tetrahedron. Ugliengo et al. found that a linear relationship between the volume of the unit cell as a function of the number of introduced Br\textsuperscript{o}nsted acidic sites is not anymore followed only above a Si/Al ratio of 3.

In this last example, we mentioned that zeolite framework silicon atoms could be substituted. This substitution is naturally found in zeolites. Silicon atoms can be replaced with +III valence atoms, such as $Al^{+III}$ or $Ga^{+III}$, or +V valence atoms, such as $P^{+V}$. Then, cations or anions are introduced to neutralize the charge of the framework (see Figure 2). The only known limitation of the silicon substitutions is the Lowenstein rule which states that substitutions cannot be found into two adjacent tetrahedra.\textsuperscript{13} The presence of cations or anions within zeolites allows the zeolite crystals to be used in ion exchanged processes.\textsuperscript{14}

![](./images/812123561538879488_2.jpg)

Figure 2. Proton bonded to bridging O-atom in the neighborhood of a silicon atom substitution with an aluminum atom in H-Mordenite.

Zeolite crystals are insulators. However, they are ionic crystals, and the radii of the zeolite oxygen and silicon atoms is close to that of the ones observed for $O^{-II}$ and $Si^{+IV}$ ions from others crystals.\textsuperscript{15} Despite this, long range electrostatic contributions play a limited role, and the bonding within the zeolite framework is mainly covalent with the ionic bonding contributing only for around 10%.\textsuperscript{16} Zeolite crystals are characterized with small dielectric constant: $\varepsilon_1$ is generally between 2 to 7 for full silicon zeolites.\textsuperscript{17} Therefore, the short range electrostatic contributions dominate over the interaction energy of molecules with the zeolite host, where dispersion Van der Waals contribution plays the main role.\textsuperscript{18} As the zeolitic oxygen atoms have a large radius, adsorbing molecules experience interactions only with the zeolitic oxygen atoms (see Figure 3).

![](./images/812123561538879488_3.jpg)

Figure 3. Hexane occlude in a mordenite zeolite micropore. The hydrocarbon molecule can only interact with zeolitic oxygen atoms.

Kiselev et al.\textsuperscript{19} defined a classical force field for which zeolite silicon atoms are not explicitly considered. The dynamic simulations they performed using this force field succeeded well in describing molecules diffusion within zeolite micropores.\textsuperscript{19,20}

We will now consider more specifically the properties of zeolite catalysts.

### 1.3 Zeolite Catalysts

Zeolites can be used as inert support for small metallic clusters catalysts or can be used themselves as catalysts. For the later case, silicon substitutions by another cation have to occur. The catalytic activity of zeolites will be dependent upon the nature of the introduced cations (viz. $Fe^{3+}$, $Zn^{2+}$, $Fe^{2+}$, $Cu^{2+}$, $H^{+}$, $Li^{+}$, $Na^{+}$, etc...) or anions (viz. $F^{-}$, $OH^{-}$ etc...).\textsuperscript{21} Lewis basic and/or acid sites and/or acid Br\textsuperscript{o}nsted sites are created. We will only describe the zeolites with silicon substituted by Al and a proton as cation to neutralize for the framework charge. In this case, a zeolite is a solid acid catalyst, which acts as more environmentally friendly acid catalyst than the classical ones. Such catalysts are obtained when the $M^{+}$ cation of a $M_x[Al_xSi_{1-x}O_2]\ nH_2O$ zeolite is ion exchanged with $NH_4^{+}$. The heating of the $NH_4^{+}$ exchanged zeolite induces $NH_3$ to desorb, and a proton is left behind. The proton binds to an oxygen atom that bridges an aluminum atom and a silicon atom (see Figure 2). As for other zeolitic bonds, the proton - zeolite oxygen atom shows a strong covalent

behavior. $^{22}$

Solid acid zeolites, beside inducing reactions known from superacids, $^{23}$ are indeed moderate acids. $^{24}$ The moderate acidity allows zeolite catalyzed reactions to not suffer from side chains reactions. $^{4}$ Enthalpies of reaction compare actually more closely with gas phase reactions than with reactions catalyzed by homogeneous high dipolar acids. $^{25}$ However, zeolite micropores have been shown to have a stabilizing effect on the carbocationic transition states with respect to gas phase results, which can reach 10 to 30 % of the activation energies. $^{26}$ This stabilization has been demonstrated to be mainly of short range electrostatic nature. $^{26a}$

A famous example, which illustrates the reaction mechanisms that happen with the acidic zeolite catalysts, is the chemisorption reaction of olefins (see Figure 4).

![](./images/812123561538879488_4.jpg)

Figure 4. Reaction steps involved in the chemisorption of propylene catalyzed by an acidic zeolite.

This reaction has been the subject of many experimental, $^{24,27}$ and theoretical $^{28}$ studies. The reaction, which initiates from a propylene physisorbed to the acidic proton, leads to the formation of a more stable chemisorbed propylene, or alkoxy species. Such reaction has been shown experimentally to occur readily at room temperature within an acidic zeolite. $^{27}$ Whereas this reaction in principle can produce two different alkoxy species (viz. a primary and a secondary alkoxy species), experiment reports that only the secondary alkoxy species can be formed. $^{27}$ This is explained by the fact that the formation of a transient primary carbenium ion is energetically more demanding than the formation of a secondary carbenium ion. $^{28c}$ As already

mentioned, the zeolite framework stabilizes partially the carbocationic transition state. This stabilization is however not sufficient to allow carbocations to exist as stable intermediates, and carbocations become covalently bonded to a zeolite framework oxygen atom.

Solid acid zeolites are used as catalysts for a large range of reactions on hydrocarbons.\textsuperscript{29} They can for instance induce alkylation, transalkylation, isomerization and cracking reactions. Moreover, they are also used to achieve fine organic reactions.\textsuperscript{5,30} We will not describe all these mechanisms, and we will only consider the case of aromatics isomerization reactions catalyzed by acidic zeolite. These reactions have been used for years as a support in the discussion on the zeolite catalysts selectivity.\textsuperscript{4,29} They allow us to show how modern quantum chemical tools can be used to describe zeolite framework effects on the course of a reaction. These effects include the zeolite framework steric constraints and electrostatic contributions. Before discussing the reaction, we will first give a short description of the available quantum chemistry tools.

## 1.4 Quantum Chemistry Applied to Zeolite Catalysis

In this part, we will not give an overview of the quantum chemistry theory that has led to the current state of affairs, as excellent introductions can be found elsewhere.\textsuperscript{8b,31} We will rather shortly describe which methodology can be followed to describe acid zeolite catalyzed reactions.

Because of the size of the reaction centers to be considered, a breakthrough in quantum-chemistry has been necessary to make computational studies feasible on systems of catalytic interest. The Density Functional Theory (DFT) has provided this breakthrough.\textsuperscript{32} Whereas in the Hartree-Fock based methods, mainly used before the introduction of Density Functional Theory, electron-exchange had to be accounted for by computation of integrals that contain products of four occupied orbitals, in Density Functional Theory these integrals are replaced by functionals that only depend on the electron density. This allows a consequent reduction of the computational costs. An exchange-correlation functional can be defined that accounts for exchange as well as correlation-energy. Correlation energy is the error made in Hartree-Fock type theories by the use of the mean-field approximation for electronic motion.

The unresolved problem yet is the determination of a rigorously exact functional. For this reason all of the currently used functionals are approximate. Furthermore, one of the main problem of DFT methods is that Van der Waals dispersion contribution is not explicitly considered in the equations, which leads to some severe errors for the description of the zeolitic guest-host interaction.\textsuperscript{33} We will give further details on this point later in the discussion.

### 1.4.1 The Cluster Approach

We mentioned that bonding in zeolites is dominated by covalent bonding. Therefore, zeolite properties can be described as being mainly locally dependent. For instance, it is known that Br\textsuperscript{o}nsted acidic sites induce important distortions in the zeolite framework (see Figure 3). However, these distortions remain local. $^{2,34}$ A direct application of this property is the validity of the use of small fragments to describe catalytic active sites (see Figure 5).

![](./images/812123561538879488_5.jpg)

Figure 5. The principle of the cluster approach method. The small cluster model (right) aims to model an acidic zeolite catalyst (left).

This model approximation is known as the cluster approach. $^{35}$ The fragment extracted from a zeolite framework is terminated with hydrogen atoms. Such method has been used with success for the estimate of properties such as frequencies of vibration, $^{36}$ NMR shielding constants, $^{37}$ or reactivity. $^{2}$ Another mandatory reason of the use of this method was the too heavy computational cost to simulate larger systems.

In recent years, progress in computer power as well as in theoretical methods allowed studies with increasingly larger clusters. $^{38}$ A large cluster model can partly allow for the zeolite framework description. Especially, Zygmunt et al. $^{26a}$ provided with large cluster studies which led to a deeper insight into reactions catalyzed by acidic zeolites. These large cluster models can however partly described the effect of the zeolite framework over the properties of interest. $^{39}$ If long range electrostatic contributions have a limited impact within zeolite, they still do exist, and should not be simply not considered as they can alter some properties. On the other hand, even small cluster calculations give valuable and useful information, as it will be described in a future section. Alternatively to the cluster approach, others methods have been developed.

### 1.4.2 Beyond the Cluster Approach

A way to describe the zeolite framework at a low computational cost is to use quantum mechanic - molecular mechanic methods (QM/MM) (see Figure 6).\textsuperscript{39} With QM/MM, only the site of interest (viz. reactants and catalytic active site) are treated at a quantum mechanic level, whereas the zeolite framework is described using force field equations of molecular mechanic.\textsuperscript{40}

![](./images/812123561538879488_6.jpg)

Figure 6. Principle of the QM/MM method applied to a zeolitic case. Here, the adsorption of methanol on a Br\textsuperscript{o}nsted site proton within a 8-membered ring zeolite.

The quality of these methods depends on the force fields parameters, the way the QM and MM parts are linked, and how QM and MM parts affect each other. The main advantages of QM/MM are to present a limited increase of required computer power as a function of the size of the system. The MM part can be constituted by up to thousands of atoms.\textsuperscript{12,28b,38} A drawback is that it is not easy to define a priori what should be the size of the QM and MM parts. Ramanchandran et al.\textsuperscript{41} observed in their periodic study that during transition state electron delocalization from the Br\textsuperscript{o}nsted site to others zeolite framework oxygen atoms was an important phenomenon. Then, large QM part is required which makes more costly calculations. Furthermore, another drawback of QM/MM is the complexity of the tuning which can lead to misleading results.\textsuperscript{28b}

The periodic electronic structure calculations methods constitute the other available approach.\textsuperscript{42} These methods require a relative high computational effort, beside progress in computer power allows calculations on systems of size of interest.\textsuperscript{43} The advantage of periodic approach method is that the entire

system is described at a quantum chemical level. The disadvantages are the heavy computational cost which limits currently the size of the unit cell to systems below 300 atoms, and the usual artifacts that are associated with periodic boundary conditions.\textsuperscript{44} Next, others problems originate from the DFT,\textsuperscript{33} and they will be explained in a next section.

We will give further details about the periodic electronic structure calculations method as we will use results obtained with this method to support the discussion.\textsuperscript{45} First, we will describe how cluster approach can be used to investigate reactions catalyzed by acidic zeolites. Next, periodic electronic structure calculations will be used to enlighten the effects of the approximations of the cluster approach. These approximations relate mainly with the missing description of the zeolite framework contributions on the molecules involved in the reactions. Finally, by increasing the size of the aromatics involved in the isomerization reactions, we will show how steric constraints affect the course of a reaction.

Before this, we will give details of the methods employed for the calculations realized in this study.

### 1.4.3 Methods and Models Employed in this Study

The cluster approach calculations have been performed using Gaussian98\textsuperscript{46} with the B3LYP method.\textsuperscript{47} This DFT method appears to be the optimum choice for treatment of zeolite cluster systems and presents results comparable with MP2 method.\textsuperscript{48} In order to describe the Br\textsuperscript{o}nsted acidic site, a 4 tetrahedra cluster $(Al(OHSiH_{3})(OSiH_{3})_{2}(OH))$ has been chosen. We selected the basis set d95. Geometry optimization calculations have been carried out to obtain local minima for reactants, adsorption complexes and products and to determine the saddle point for transition states (TS). Frequency calculations have been computed in order to check that the stationary points exhibit the proper number of imaginary frequencies: none for a minimum and one for a transition state. Zero point energy (ZPE) corrections have been calculated for all optimized structures.

The Vienna Ab Initio Simulation Package (VASP) has been used to perform the periodic structure calculations.\textsuperscript{42a,b,43} All atoms have been allowed to relax completely within the periodic unit cell. The large 12-membered ring Mordenite has been used for this study as this zeolite has a relatively small unit cell (i.e. 146 atoms). It has previously been studied by Demuth et al.\textsuperscript{50}. For our zeolite model, the Si/Al ratio is 23, and the geometry of the unit cell is described by $a = 13.648$ \AA{}, $b = 13.672$ \AA{}, $c = 15.105$ \AA{}, $\alpha = 96.792$ \textdegree{}, $\beta = 90.003$ \textdegree{} and $\gamma = 90.022$ \textdegree{}. With VASP, the energy is obtained solving the Kohn-Sham equation with the Perdew-Zunger exchange-correlation functional.\textsuperscript{51} The results are corrected for non-locality within the generalized gradient approximation (GGA) with the Perdew-Wang 91 functional.\textsuperscript{52} This functional is currently the only available in VASP. This program uses plane-

waves and pseudopotentials, which allow a consequent reduction of computational costs. A cut-off of 300 eV and a Brillouin zone sampling restricted to the $\Gamma$-point have been used. A quasi-Newton forces minimization algorithm has been employed: convergence was assumed to be reached when forces were below 0.05 eV/\AA{}. The TS search method in VASP is the nudged elastic band (NEB) method.\textsuperscript{53} Several images of the system are defined along the investigated reaction pathway. These images are optimized but only allowed to move perpendicularly to the hyper-tangent defined by the normal vector between the neighboring images. We employed up to 8 images to analyze transition states. When forces of the images atoms were below 0.08 eV/\AA{}, the forces of the maximum energy image were minimized separately.

## 2. TOLUENE ISOMERIZATION

In this part, we will summarize some of our results on the investigation of the toluene intramolecular isomerization pathways.\textsuperscript{45,54} Both cluster approach and periodic approach methods have been employed which allow giving an illustration of the consequence of the simplistic model in the cluster approach. H-Mordenite (H-MOR) zeolite is used for the periodic calculations. The toluene molecule does not have a problem to fit within the large 12-membered ring channels of this zeolite.\textsuperscript{18} Furthermore, the intramolecular transition states do not suffer from steric constraints.\textsuperscript{4} It is known that intramolecular aromatics isomerization can proceed via two different reaction pathways (see Figure 7).\textsuperscript{4,55} The first route proceeds through a methyl shift isomerization, whereas the second route involves a dealkylation or disproportionation reaction which results in the formation of a methoxy species and benzene as intermediate.

![](./images/812123561538879488_7.jpg)

Figure 7. Catalytic cycles and description of the mechanisms of the intramolecular isomerization reactions of toluene catalyzed by an acidic zeolite.\textsuperscript{55}

The initial step of this investigation is to analyze the reaction pathways using the low computational cost cluster approach. The small cluster model aims to model a zeolitic Br\textsuperscript{o}nsted acidic site, and has been demonstrated to fill successfully this task. $^{2}$ On the other hand, a small cluster cannot describe the zeolite framework. By comparison of reaction pathways taking and not taking into account the zeolite framework, we will be able to evaluate this effect on reactivity.

### 2.1 Cluster Approach

The investigation of the shift isomerization reaction pathway led to the establishment of the reaction energy diagram plotted in Figure $8.^{54}$ The geometries of the intermediates and transition states are also summarized in this figure. Prior to reach the shift isomerization transition state, toluene needs to be activated by proton attack. This activation proceeds via a transition state very similar to the one obtained from propylene chemisorption in acidic zeolite (see Figure 4). It leads to the formation of a phenoxy intermediate which is less stable than the physisorbed toluene. This is expected from the chemical properties differences between propylene and toluene. $^{56}$

![](./images/812123561538879488_8.jpg)

Figure 8. Reaction energy diagram and description of the mechanisms of the shift isomerization reaction of toluene catalyzed by acidic zeolite (all data in kJ/mol). $^{54}$

The phenoxy species is released from the cluster with no activation energy barrier to overcome but a constant increase in energy to a Wheland complex from which shift isomerization transition state takes place. With respect to physisorbed toluene, the activation energy to achieve this transition state is $E_{act}=+282$ kJ/mol. In the transition state, the shifting methyl group occupies an intermediate position between the aromatic ring carbon atom it was connected to, and the carbon atom it will connect to. The shift methyl

group carbon atom is located in a position almost orthogonal with respect to the plane defined by the aromatic ring. Extra weak hydrogen bonds with the cluster oxygen atoms stabilize the transition state with this structure.

For the isomerization of toluene via methoxy and benzene intermediate, the similar proton activation, which results in the formation of a phenoxy intermediate, is achieved (see Figure 9). As previously, the bond between the zeolitic oxygen atom and the aromatic carbon atom stretches out. A "free" Wheland complex is eventually reached which can reorient to favor the position of the toluene methyl group with the demethylation transition state.

The geometry of this transition state can be described as a methenium carbocation sandwiched in between a benzene molecule and a deprotonated Br\textsuperscript{o}nsted site. The methenium ion is planar, and its carbon atom is located along the line defined by the zeolitic oxygen atom to which it will be bonded and the aromatic carbon atom to which it was bonded. The activation energy which is required to achieve this reaction is $E_{act}=+279$ kJ/mol.

![](./images/812123561538879488_9.jpg)

Figure 9. Reaction energy diagram and description of mechanisms of the disproportionation via methyl alkoxy isomerization reaction of toluene catalyzed by an acidic zeolite (all data in kJ/mol).\textsuperscript{54}

This transition state results in the formation of a methoxy species and benzene. Benzene can desorb from the methoxy species, or can change its orientation. The energy level of this intermediate is + 70 kJ/mol with respect to physisorbed toluene. The regeneration of toluene from this intermediate follows the reverse transition state.

Interestingly, the two reaction routes require similar activation energy, and further consideration of the entropies of activation cannot decide as well whether a route has preeminence on the other (the entropies of activation are $\Delta_{298K}S_{act}=-13$ and - 17 J/mol/K for the shift and via disproportionation isomerizations respectively).

## 2.2 Periodic Approach

We will now describe shortly our results of the investigation of the toluene intramolecular isomerization catalyzed by H-Mordenite using an electronic periodic structure method.\textsuperscript{45} Let us consider first the shift isomerization transition (see Figure 10). As it can be seen in this figure, the geometries of the transition states from cluster approach and from periodic approach are very similar. The large difference between these transition states is that the activation energy from periodic approach is $E_{\text{act}} = + 179\ \text{kJ/mol}$ whereas it is $E_{\text{act}} = + 282\ \text{kJ/mol}$ from the cluster approach. Such a decrease of the activation energy, when a more realistic zeolite model is employed, has already been notified.\textsuperscript{28b}

![](./images/812123561538879488_10.jpg)

Figure 10. Geometries of the shift isomerization transition states of toluene catalyzed by acidic zeolite as obtained from the cluster approach method (left) and the periodic structure method (right).\textsuperscript{45,54}

This important stabilization has other consequences on the reaction pathway of isomerization (see Figure 11). The investigation of the activation of toluene by proton attack reveals a completely different picture than the one obtained with the cluster approach. The protonation step of toluene becomes an inflection point in the reaction pathway, which gives as product a metastable Wheland complex.

The formation of the phenoxy intermediate turns to be unlikely to occur as this intermediate remains at similar energy level as observed from the cluster approach (i.e. + 150 kJ/mol), whereas protonation step and Wheland complex energy levels are around + 110 kJ/mol with respect to physisorbed toluene.

Zeolite framework stabilization effects uniformly all transition states and charged transient intermediates, and does not effect the neutral intermediates. Similar effect of the zeolite framework has been described by Corma et al.\textsuperscript{58} for another reaction.

Exactly the same trend is obtained for the second isomerization route. An important consequence of this is that the activation energy barrier for the isomerization via methoxy and benzene transition state is found to be $E_{\text{act}} = +$

182 kJ/mol. This means that a periodic approach method predicts as well as the cluster periodic method that the two alternative isomerization routes are competitive pathways. Qualitatively, cluster and periodic methods give the same result.

![](./images/812123561538879488_11.jpg)

Figure 11. Reaction energy diagrams of the shift isomerization reaction of toluene catalyzed by acid zeolite. The diagrams using black lines refer to the cluster approach results, and the ones using gray lines to the periodic calculations results (in kJ/mol).\textsuperscript{45,54,57}

However, the zeolite framework effect on the reaction is not limited only to a stabilization of charged species. We saw already that a transition state from the cluster approach turns to be an inflection point when the zeolite framework contribution is considered. An effect exists also on transition state. In the case of the shift isomerization transition state, it is found an alternative geometry. Before protonated toluene changes its orientation with respect to the deprotonated Br\textsuperscript{o}nsted site, the methyl shift reaction step can be achieved (see Figure 12).

![](./images/812123561538879488_12.jpg)

Figure 12. Front view of the alternative geometry of the methyl shift isomerization transition state as obtained from the periodic structure calculations.\textsuperscript{45}

For this other transition state, the shifting methyl group is stabilized because of the formation of several weak hydrogen bonds with the zeolitic oxygen atoms located to the opposite side of the channel with respect to the Br\textsuperscript{o}nsted site. A striking feature about this methyl shift isomerization transition state is that it has a similar activation energy as the other isomerization transition states with $E_{\text{act}} = + 179$ kJ/mol. Of course, this result is strongly dependent with the local zeolite framework topology, as we will see in the next section.

### 3. XYLENE ISOMERIZATION

Recently, we investigated the associative alkylation reaction of toluene with methanol catalyzed by an acidic Mordenite (see Figures 13 and 14) by means of periodic ab initio calculations.\textsuperscript{43} We observed that for this reaction some transition selectivity occurred, and induced sufficiently large differences in activation energies to explain the small changes in the *para/meta/ortho* distribution experimentally observed on large pore zeolites.\textsuperscript{59} The *para* isomer is the more valuable product as it is an important intermediate for terphthalic acid, an important polymer monomer.\textsuperscript{4d} The steric constraints obtained for the transition state structures could be estimated from local intermediates for which the orientations of the toluene molecule were similar as the ones observed for the transition states (see Figure 14).

![](./images/812123561538879488_13.jpg)

Figure 13. Geometries of the associative mechanism transition states of the alkylation reaction of toluene with methanol catalyzed by H-MOR as obtained from the DFT periodic structure calculations that lead to the formation of the different xylene isomers and water.\textsuperscript{43}

![](./images/812123561538879488_14.jpg)

Figure 14. Reaction energy diagrams of the reactions of alkylation of toluene with methanol catalyzed by H-MOR, which give as products p-xylene, m-xylene, or o-xylene, and water (all values in kJ/mol). The values correspond to energies at 0K (American Chemical Society, 2001).\textsuperscript{43}

We will use now the same method and Mordenite zeolite model as in the previous part, and investigate the isomerization of xylene isomers.\textsuperscript{45} As described in the previous part, this reaction can proceed via two alternative routes, viz. a methyl shift isomerization, and disproportionation reactions. Moreover, we observed than in the case of toluene isomerization, the location of toluene with respect to the Br\textsuperscript{o}nsted acidic site for the shift isomerization was of no consequence for the activation energy barrier. We will check these mechanisms for the three xylenes.

It is known from experiment that xylenes do not have different adsorption energies when adsorbed within fully dealuminated mordenite.\textsuperscript{18} In our case, we found however that xylenes adsorption to the acidic proton show slight energy differences which are correlated with the local topology of the Br\textsuperscript{o}nsted acidic site as well as the geometry of the considered xylene isomer. The computed adsorption energies are - 37 kJ/mol, - 30 kJ/mol, and - 33 kJ/mol for para-xylene, meta-xylene, and ortho-xylene respectively. One notes that these adsorption energies are crude underestimates of the experimental adsorption energies, which have been reported to be around - 130 kJ/mol.\textsuperscript{18} This is a direct consequence of the use of DFT method, which are known to not have the ability to describe properly Van der Waals dispersion contribution.\textsuperscript{33}

For a study of reactivity within zeolite, it is hopefully a good approximation to not consider Van der Waals dispersion contribution. In a classical dynamic simulation of benzene and toluene within Y zeolite pores, Klein et al.\textsuperscript{60} decomposed the guest-host interaction energy. They showed that Van der Waals dispersion contribution was almost constant along diffusion pathways, and that the electrostatic contributions could explain alone the preferred adsorption site locations of aromatics within zeolite. The importance

of the electrostatic contribution is enhanced when acidic sites are present. Furthermore, in the case of hydrocarbon molecules reactions within zeolite, it is well understood that transition states are of carbocationic nature. $^{2}$

The main reason of a proper estimate of the adsorption energy is to allow the comparison with experimental. Since the pioneering work of Haag, $^{61}$ it is well understood that in zeolites a measured activation energy is actually an apparent activation energy which can be expressed in the case of a first order reaction as:

$$
E_{\text{act}}^{\text{app}} = E_{\text{act}} + (1 - \theta) E_{\text{ads}} \tag{1}
$$

where $E_{\text{act}}$ is the activation energy, $\theta$ the coverage of the reactant to the active site, and $E_{\text{ads}}$ the adsorption energy of the reactant adsorbed to the active site.

To evaluate the Van der Waals interaction energy in the case of our systems, we used the force field parameters provided by Deka et al., $^{18}$ and defined to describe the aromatics adsorption within zeolites. The Van der Waals interaction is then computed between the aromatic guest and the zeolite host, $^{43,45}$ and the DFT adsorption energy is corrected with this value as:

$$
E_{\text{ads}}^{\text{corrected}} = E_{\text{ads}} + E_{\text{VdW}} \tag{2}
$$

In this way, one gets the adsorption energy of the aromatic molecule adsorbed to the acidic proton within the zeolite micropore. It is $E_{\text{ads}}^{\text{corrected}}$ that is used in (1). Interestingly, the evaluation of $E_{\text{VdW}}$ for all our systems gives within few kJ/mol the same value, and we could assume as observed from ref. 60 that the dispersion contribution is a constant contribution for a given adsorbate size. For xylene isomers, this Van der Waals correction is $E_{\text{VdW}} = \text{- 95 kJ/mol}$. Then, the adsorption energies for *para*-xylene, *meta*-xylene, and *ortho*-xylene are - 132 kJ/mol, - 125 kJ/mol, and - 128 kJ/mol respectively.

Let us now consider the methyl shift isomerizations that lead from *para*-xylene to *meta*-xylene (see Figure 15).

![](./images/812123561538879488_15.jpg)

Figure 15. Front views of the transition states of shift isomerization that occur with (right) and without (left) reorientation of the xylene molecule after protonation as obtained from the periodic structure calculations (American Chemical Society, 2001). $^{45}$

As it can be observed in Figure 15, in the case of the methyl shift isomerization transition state for which the orientation of the aromatic ring with respect to the Br\textsuperscript{o}nsted site is as the one obtained from the cluster calculations, the non-participating methyl group experiences short interactions with the zeolitic wall. For the transition state structure that is reached without reorientation of the aromatic ring after it became protonated, the non-participating methyl group is oriented in the same direction as the large 12-membered ring channel, and therefore does not suffer from steric constraints with the zeolite wall. This results in two very different activation energies, which prohibit with the achievement of the transition state with an aromatic ring orientation as for the cluster approach transition state. The difference in activation energies is $\Delta E_{\text{act}} = + 63$ kJ/mol, and the activation energy for the methyl shift isomerization without reorientation of the aromatic ring after protonation occurred is $E_{\text{act}} = + 171$ kJ/mol.

In the case of the ortho to meta-xylene methyl shift isomerization transition states, the steric constraints are less important as the non-participating methyl group has more available space because of the ellipsoidal shape of the 12-membered ring channel (see Figure 15). Then, the activation energies are + 168 kJ/mol, and + 184 kJ/mol for the transition state which follows immediately the xylene protonation, and for the transition state which occurs after xylene overcame a rotation energy barrier to change its orientation with respect to the Br\textsuperscript{o}nsted site respectively.

![](./images/812123561538879488_16.jpg)

Figure 16. Front and side views of the transition states and intermediate for the isomerization reaction via disproportionation reaction pathway of xylene molecules catalyzed by an acidic Mordenite as obtained from the periodic calculations (American Chemical Society, 2001).\textsuperscript{45}

Concerning the disproportionation isomerization reactions, the activation energies follow the predictions of Corma et al.\textsuperscript{62} using the HSAB principle of Pearson. In their study, Corma et al. predicted that the activation energies for the alkylation of toluene with methoxy follow the ordering ortho < para. They estimated these data for zeolitic systems in absence of steric constraints.

It can be seen in Figure 16 that the non-participating methyl group for each of the disproportionation transition states has enough room to avoid steric constraints with the zeolite wall. The activation energies are + 164 kJ/mol, + 174 kJ/mol, and + 187 kJ/mol for an alkylation/dealkylation to the *ortho*, *meta*, and *para* position respectively.

![](./images/812123561538879488_17.jpg)

Figure 17. Reaction energy diagrams of the intramolecular isomerization of *ortho*-xylene (top), *para*-xylene (middle) and *meta*-xylene (bottom) catalyzed by H-MOR as obtained from the periodic structure calculations (in kJ/mol) (American Chemical Society, 2001).\textsuperscript{45}

These data support the experimental study of Ivanova et al.\textsuperscript{63} or the theoretical cluster approach study of Blaszkowski et al.\textsuperscript{64}. It is known that the alkylation of toluene with methanol can proceed via two reaction routes. The first one involves an associative protonation of methanol, which induces the methyl jump to toluene (see Figures 13 and 14), whereas the second one is a consecutive reaction pathway, which initiates with the formation of a methoxy species and a water molecule. The second step in the consecutive reaction is an alkylation reaction between toluene and the methoxy species. However,

this conclusion has to be toned down as in the present study of the alkylation of toluene with methoxy, the ancillary effect of water is not considered.\textsuperscript{5} It has been showed that water has an ancillary and stabilizing effect on transition state. These can decrease the activation energy barrier for carbocationic nature transition state by around 20-30 kJ/mol.\textsuperscript{5}

The different isomerization reaction pathways considered in this part are summarized in the reaction energy diagrams in Figure 17.

From Figure 17, one can conclude in total that the differences in activation energies for the isomerization of *ortho, meta*, and *para*-xylene are not large enough to induce transition state selectivity. However, transition state selectivity exists and prevents with the isomerization to proceed through some reaction pathways with respect to others. This absence of transition state selectivity when all possible isomerization reaction routes are considered is indeed expected from experimental and dynamic simulation diffusion studies. Deka et al.\textsuperscript{18} reported that differences in the diffusion of the three xylene isomers within mordenite are sufficient to explain for the distribution of products as observed from experimental. On the other hand, the computed activation energies provided with this study are in very good match with experimental apparent activation energies after (1) and (2) are applied.\textsuperscript{55,65}

In the next part, we will briefly consider a larger aromatic molecule, viz. dimethyldibenzothiophene (DMDBT).\textsuperscript{66} This will give us the opportunity to describe the zeolite selectivity that is induced by the adsorption behavior of reactants to the catalytic active site on the products distribution.

## 4. DMDBT ISOMERIZATION

Hydrodesulfurization (HDS) is an important process in petrochemical refinery as it allows decreasing the sulfur content in diesel fuel.\textsuperscript{67} Compounds such as alkylated dibenzothiophene (DBT) raise some problems in HDS. The alkyl groups, especially when located in the 4 and 6 positions of the ring (see Figure 18) make alkylated DBT resistant to classical HDS catalysts because of the methyl groups that prevent the thiophenic sulfur atom to be in contact with the active site of the catalyst.

![](./images/812123561538879488_18.jpg)

Figure 18. Dimethylated dibenzothiophene derivatives.

However, Michaud et al.\textsuperscript{68} and Landau et al.\textsuperscript{69} reported that the use of an acid zeolite catalyst and classical HDS catalyst bifunctional catalyst was a very efficient way to desulfurize alkylated DBT. In this case, they observed that acid zeolite catalyst achieves isomerization of the more hindered sulfur atom alkylated DBT (viz. 46DMDBT) to compounds for which the sulfur atom is not anymore hindered by the methyl groups (viz. 37DMDBT).

We will analyze the intramolecular isomerization of 46DMDBT to 37DMDBT catalyzed by H-MOR.\textsuperscript{70} Obviously, the large size of DMDBTs prevents with change in the orientation of the molecule within the narrow pore of the zeolite catalyst (see Figure 19). Therefore, only the shift isomerization reactions without reorientation of the DMDBT molecules after they became protonated have been considered.

![](./images/812123561538879488_19.jpg)

Figure 19. Geometries of 46, 36, and 37DMDBT adsorbed to the acidic site, and of the transition states of the shift isomerization of 46 to 36DMDBT and of 36 to 37DMDBT as obtained from the periodic structure calculations.\textsuperscript{70}

The geometries of the shift isomerization transition states of 46 to 36DMDBT and 36 to 37DMDBT and of the physisorbed 46, 36, and 37DMDBT are shown in Figure 19. In the transition states, the shifting methyl groups are located between the carbon atoms it was bonding/will bond. As for the mechanisms obtained for toluene and xylene isomers, here, the zeolitic oxygen atoms that belong to an 8-membered ring side-pocket of MOR stabilize the shifting methyl.

The activation energy of the 46DMDBT to 36DMDBT isomerization with respect to adsorbed 46DMDBT is $E_{\text{act}} = + 137$ kJ/mol. It is $E_{\text{act}} = + 142$ kJ/mol for the 36DMDBT to 37DMDBT reaction with respect to adsorbed 36DMDBT. Interestingly, the activation energies for these two reactions are similar. The same is observed for the isomerizations from 36 to 46DMDBT and 37 to 36DMDBT. In this case, the computed activation energies are $E_{\text{act}} = + 155$ kJ/mol and + 156 kJ/mol respectively.

However, further consideration of the full reaction energy diagram reveals an interesting situation (see Figure 20). The energy levels of the different physisorbed DMDBTs are very different from each other because of more or less sterically hampered DBT methyl groups within the narrow mordenite pore (see Figure 19).

![](./images/812123561538879488_20.jpg)

Figure 20. Reaction energy diagram of the intramolecular isomerization reactions of the DMDBT molecules catalyzed by H-MOR as obtained from the periodic structure calculations (all values in kJ/mol).\textsuperscript{70}

With respect to adsorbed 46DMDBT energy level, the energy levels of adsorbed 36DMDBT and adsorbed 37DMDBT are - 18 kJ/mol and - 32 kJ/mol respectively. One can estimate using the Polanyi-Br\textsuperscript{o}nsted relation,\textsuperscript{71} which states that the changes in activation energy are proportional to the changes in reaction energy, that the activation energy for a methyl shift isomerization of DMDBT is $E_{\text{act}} = + 148$ kJ/mol. Then, the selective adsorption behavior of the different DMDBT isomers induces with transition

state selectivity. For 36DMDBT, it is more likely that isomerization leads to formation of 37DMDBT than 46DMDBT as the $\Delta E_{\text{act}}$ is 13 kJ/mol. This is the result that is experimentally observed. $^{68,69}$

## 5. CONCLUSION

We started this paper with a rather long introduction. This was very important as it allows understanding zeolites minerals and their use as catalysts. Based on experimental information, it becomes possible to define inputs to the calculations. Moreover, we discussed which data can and cannot be accessed by means of quantum chemistry calculations.

The study of reactivity by QM calculations concerns only a small part of a catalytic event, as phenomena such as macro and micro diffusion of the reactants and products outside and inside the zeolite micropores cannot be investigated. On the other hand, QM methods are the only theoretical methods available that provide information on the reactivity.

The shape selectivity of zeolites in diffusion processes is now rather well understood. $^{72}$ There remains a gap in the description of the reactive events. With methods such as the small cluster approach, the reactivity is relatively well described. But, such a system cannot model the zeolite framework. Progress in computer power permits for the emergence of increasingly larger cluster studies. The large cluster models provide a useful analysis of the short-range electrostatic effect of the zeolite framework on transition state structures. But it remains questionable whether the large cluster method can describe transition state selectivity properly. In order to keep these molecular clusters in shape, generally fixed geometry models are used. How far can the limited flexibility of the zeolite framework smooth the large energy differences that are due to steric constraints? It is because of this that quantum chemical periodic methods constitute an adequate tool to investigate selective reactivity within zeolites. Of course, QM/MM methods are also useful, especially for a more basic (MM level) analysis of the zeolite selective reactivity. However, considering computational cost criteria, QM/MM methods are often to be preferred over periodic structure QM calculations. Another advantage of QM/MM methods is that Van der Waals dispersion contributions can be modeled.

We have shown here, with the support of selected examples, that periodic calculations have become possible on systems of interest. This allows for a deeper understanding of zeolite catalyst reactivity. The full range of the zeolite selectivity can now be investigated by theoretical methods.

We have shown in the first part what are the consequences of the absence of the zeolite framework on a reaction. This has an important energetic effect. The reaction mechanisms predicted by the cluster approach appear to be very similar to periodic method ones.

Then, we investigated a reaction for which transition state selectivity is important. It appears that several alternative reaction pathways can be followed among which some lead to a minimization of the steric constraints. These steric constraints are strongly dependent on the local topology of the zeolite framework as well as on the geometry of the transition state.

We observed a very good agreement of the computed activation energies with experiment.

Finally, we presented a case for which the large size of reactants and products induces transition state selectivity mainly due to differences in adsorption. The reactivity behavior is shown to follow the Polaniy-Br\textsuperscript{o}nsted relation.

# ACKNOWLEDGEMENTS

The studies described here have been performed within the European Research Group *"Ab Initio Molecular Dynamics Applied to Catalysis"*, supported by the *Centre National de la Recherche Scientifique* (CNRS), the *Institut Fran\c{c}ais du P\textsuperscript{e}trole* (IFP) and TotalFinaElf. X. R. thanks TotalFinaElf for the support.

# REFERENCES

1.  Barrer, R. M. *Zeolite and Clay Minerals as Sorbents and Molecular Sieves*; Ed.; Academic Press: London, New York, San Fransisco, 1978.
2.  Van Santen, R. A.; Kramer, G. J. *Chem. Rev.* **1995**, *3*, 637-660.
3.  (a) Meier, W. M.; Olson, D. H.; Baerlocher, C. *Zeolites* **1996**, *17*, 1-230. (b) Thomas, J. M.; Thomas, W. J. *Principles and Practice ofHeterogeneous Catalysis*; Eds.; VCH: Weinheim, New York, 1997; pp 6-10.
4.  (a) Csicsery, S. M. *Zeolites* **1984**, *4*, 202-213. (b) Fraenkel, D.; Levy, M. J. *Catal.* **1989**, *118*, 10-21. (c) Chen, N. Y.; Degnan, T. F. Jr.; Smith, C. M. *Molecular Transport and Reaction in Zeolites, Design and Application of Shape Selective Catalyst*; Eds.; VCH Publishers: New York, 1994; pp 195-289. (d) Tsai, T.-C.; Liu, S.-B.; Wang, I. *Appl. Catal. A* **1999**, *181*, 355-398.
5.  Barbosa, L. A. M. M.; Van Santen, R. A. *J. Catal.* **2000**, *191*, 200-217.
6.  (a) Frenkel, D. *Proceeding of the Euroconference on Computer Simulation in Condensed Matter Physics and Chemistry, Como 1995*; Binder, K., Ciccotti, A., Eds.; Italian Physical Society: Bolognia, 1995; chapter 7. (b) Schuring, D.; Jansen, A. P. J.; Van Santen, R. A. *J. Phys. Chem. B* **2000**, *104*, 941-948. (c) Smit, B.; Siepmann, J. I. *J. Phys. Chem.* **1994**, *98*, 8442-8452. (d) Smit, B. *Mol. Phys.* **1995**, *85*, 153-172. (e) Smit, B.; Maesen, T. L. M. *Nature* **1995**, *374*, 42-44.
7.  Schumacher, R. R.; Anderson, B. G.; Noordhoek, N. J.; De Gauw, F. J. M. M.; De Jong, A. M.; De Voigt, M. J. A.; Van Santen, R. A. *Microporous Mesoporous Mater.* **2000**, *35-36*, 315-326.
8.  (a) Jeanvoine, Y.; \'{A}ngy\'{a}n, J. G.; Kresse, G.; Hafner, J. *J. Phys. Chem. B* **1998**, *102*, 7307-7310. (b) Sandr\'{e}, E.; Pasturel, A. *Mol. Simul.* **1997**, *20*, 63-77.
9.  (a) Nicholas, J. B. *Topics Catal.* **1997**, *4*, 157-171. (b) Bernadi, F.; Robb, M. A. *Ab Initio Methods in Quantum Chemistry - I*; Lawley, K. P., Ed.; John Wiley & Sons

Ltd., 1987; pp 155-248.

10.
(a) Yashonath, S.; Santikary, P. *J. Phys. Chem.* **1993**, *97*, 3849-3857. (b) Yashonath,
S.; Santikary, P. *Mol. Phys.* **1993**, *78*, 1-6. (c) Yashonath, S.; Santikary, P. *J. Chem.
Phys.* **1994**, *100*, 4013-4016.

11.
Ugliengo, P.; Civalleri, B.; Zicovich-Wilson, C. M.; Dovesi, R. *Chem. Phys. Lett.*
**2000**, *318*, 247-255.

12.
Brandle, M.; Sauer, J.; Dovesi, R.; Harrison, N. M. *J. Chem. Phys.* **1998**, *109*,
10379-10389.

13.
Lowenstein, W. *Am. Mineral.* **1942**, *39*, 92.

14.
Barrer, R. M. *Zeolite and Clay Minerals as Sorbents and Molecular Sieves*; Ed.;
Academic Press: London, New York, San Fransisco, 1978; pp 18-19.

15.
Fricke, R.; Kosslick, H.; Lischke, G.; Richter, M. *Chem. Rev.* **2000**, *100*, 2303-2405.

16.
(a) De Man, A. J. M.; Van Santen, R. A. *Zeolites* **1992**, *12*, 269-279. (b) Lee, C.;
Parrillo, D. J.; Gorte, R. J.; Farneth, W. E. *J. Am. Chem. Soc.* **1996**, *118*, 3262-3268.

17.
(a) Levien, L.; Previtt, C. T.; Weider, D. J. *Am. Mineral.* **1980**, *65*, 925. (b) De Man,
A. J. M.; Van Beest, B. W. H.; Leslie, M.; Van Santen, R. A. *J. Phys. Chem.* **1990**,
*94*, 2524-2564. (c) Schroder, K.-P.; Sauer, J. *J. Phys. Chem.* **1996**, *100*, 11043-
11049.

18.
Deka, R. C.; Vetrivel, R.; Miyamoto, A. *Topics Catal.* **1999**, *9*, 225-234.

19.
Bezuz, A. A.; Kiselev, A. G.; Loptakin, A. A.; Quang Du, P. *J. Chem. Soc., Faraday
Trans. II* **1978**, *74*, 367-379.

20.
Bezuz, A. A.; Kocirik, M.; Kiselev, A. V.; Lopatkin, A. A.; Vasilyena, E. A. *Zeolites*
**1986**, *6*, 101-106.

21.
Coombs, D. S.; Alberti, A.; Armsbruster, T.; Artioli, G.; Colella, C.; Galli, E.; Grice,
J. D.; Liebau, F.; Mandarino, J. A.; Minato, H.; Nickel, E. H.; Passaglia, E.; Peacor,
D. R.; Quartieri, S.; Rinaldi, R.; Ross, M.; Sheppard, R. A.; Tillmanns, E.;
Vezzalini, G. *Am. Mineral.* **1998**, *83*, 917-935.

22.
(a) Nicholas, J. B. *Topics Catal.* **1997**, *4*, 157-171. (b) Rigby, A. M.; Kramer, G. J.;
Van Santen, R. A. *J. Catal.* **1997**, *170*, 1-10. (c) Van Santen, R. A. *Catal. Today*
**1997**, *38*, 377-390.

23.
(a) Olah, G. A.; Donovan, D. J. *J. Am. Chem. Soc.* **1977**, *99*, 5026-5039. (b) Olah, G.
A.; Prakash, G. K. S.; Sommer, J. *Superacids*; Eds.; Wiley Interscience: New York,
1985. (c) Olah, G. A.; Prakash, G. K. S.; Williams, R. E.; Field, L. D.; Wade, K.
*Hypercarbon Chemistry* ; Eds.; Wiley Interscience: New York, 1987.

24.
(a) Haw, J. F.; Richardson, B. R.; Oshiro, I. S.; Lazo, N. D.; Speed, J. A. *J. Am.
Chem. Soc.* **1989**, *111*, 2052-2058. (b) Haw, J. F.; Nicholas, J. B.; Xu, T.; Beck, L.
W.; Ferguson, D. B. *Ace. Chem. Res.* **1996**, *29*, 259-267. (c) Haw, J. F.; Xu, T.;
Nicholas, J. B.; Goguen, P. W. *Nature* **1997**, *389*, 832-835.

25.
Gorte, R. J. *Catal. Lett.* **1999**, *62*, 1-13.

26.
(a) Zygmunt, S. A.; Curtiss, L. A.; Zapol, P.; Iton, L. E. *J. Phys. Chem. B* **2000**, *104*,
1944-1949. (b) Sauer, J.; Sierka, M.; Haase, F. *Transition State Modeling for
Catalysis*; Truhlar, D. G., Morokuma, K., Eds.; ACS Symp. Ser. No 721; American
Chemical Society: Washington, **1999**; pp 358-367.

27.
Derouane, E. G.; He, H.; Hamid, S. B. D.-A.; Ivanova, I. I. *Catal. Lett.* **1999**, *58*, 1-
18.

28.
(a) Kazansky, V. B.; Senchenya, I. N. *J. Catal.* **1989**, *119*, 108-120. (b) Sinclair, P.
E.; De Vries, A.; Sherwood, P.; Callow, C. R. A.; Van Santen, R. A. *J. Chem. Soc.,
Faraday Trans.* **1998**, *94*, 3401-3408. (c) Rigby, A. M.; Frash, M. V. *J. Mol. Catal.
A* **1997**, *126*, 61-72.

29.
(a) H\"{o}lderich, W. F.; Van Bekkum, H. *Introduction to Zeolite Science and Practice*;
Van Bekkum, H., Flaningen, E. M., Jansen, J. C., Eds.; Elsevier: Amsterdam, 1991;
pp 631-726, vol. 58. (b) Venuto, P. B. *Microporous Mater.* **1994**, *2*, 297-411.

30.
(a) Fernandez, L.; Marti, V.; Garcia, H. *Phys. Chem. Chem. Phys.* **1999**, *1*, 3689-
3695. (b) Laszlo, P. *J. Phys. Org. Chem.* **1998**, *11*, 356-361.

31.
Schleyer, P. v. R. *Encyclopedia of Computational Chemistry*; Ed.; John Wiley &

Sons: New York, 1998.

32.
Perdew, J. P. *Density Functional Theory, a Bridge Between Chemistry and Physics*;
Geerlings, P., De Proft, F., Langenaeker, W., Eds.; VUB University Press: Brussels,
1999; pp 87-109.

33.
(a) Kristyan, S.; Pulay, P. *Chem. Phys. Lett.* 1994, 229, 175-180. (b) Sauer J.;
Ugliengo, P.; Garrone, E.; Saunders, V. R. *Chem. Rev.* 1994, 94, 2095-2160. (c)
Lein, M; Dobson, J.F.; Gross, E. K. U. *J. Comp. Chem.* 1999, 20, 12-22. (d)
Pelmenschikov, A.; Leszczynski, J. *J. Phys. Chem. B* 1999, 103, 6886-6890.

34.
Kramer, G. J.; De Man, A. J. M.; Van Santen , R. A. *J. Am. Chem. Soc.* 1991, 113,
6435-6441.

35.
(a) Sauer, J. *Chem. Rev.* 1989, 89, 199-255. (b) Gale, J. D. *Topics Catal.* 1996, 3,
169-194. (c) Frash, M. V.; Van Santen, R. A. *Topics Catal.* 1999, 9, 191-205.

36.
(a) Datka, J.; Broclawik, E.; Gil, B.; Sierka, M. *J. Chem. Soc., Faraday Trans.* 1996,
92, 4643-4646. (b) Ugliengo, P.; Ferrari, A. M.; Zecchina, A.; Garrone, E. *J. Phys.
Chem.* 1996, 100, 3632-3645. (c) Frash, M. V.; Makarova, M. A.; Rigby, A. M. *J.
Phys. Chem. B* 1997, 101, 2116-2119. (d) Zygmunt, S. A.; Curtiss, L. A.; Iton, L. E.;
Erhardt, M. K. *J. Phys. Chem.* 1996, 100, 6663-6671.

37.
(a) Koller, H.; Overweg, A. R.; Van Santen, R. A.; De Haan, J. W. *J. Phys. Chem. B*
1997, 101, 1754-1761. (b) Koller, H.; Meijer, E. L.; Van Santen, R. A. *Solid State
Nuc. Magn. Res.* 1997, 9, 165-175. (c) Koller, H.; Engelhardt, G.; Van Santen, R. A.
*Topics Catal.* 1999, 9, 163-180. (d) Bull, L. M.; Bussemer, B.; Anup\~{o}ld, T.;
Reinhold, A.; Samoson, A.; Sauer, J.; Cheetham, A. K.; Dupree, R. *J. Am. Chem.
Soc.* 2000, 122, 4948-4958.

38.
Sauer, J.; Eichler, U.; Meier, U.; Sch\"{a}fer, A.; Von Arnim, M.; Ahlrichs, R. *Chem.
Phys. Lett.* 1999, 308, 147-154.

39.
(a) Sherwood, P.; De Vries, A. H.; Collins, S. J.; Greatbanks, S. P.; Burton, S. A.;
Vincent, M. A.; Hillier, I. H. *Faraday Discuss.* 1997, 106, 79-92. (b) Sierka, M.;
Sauer, J. *Faraday Discuss.* 1997, 106, 41-62.

40.
Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*; Eds.; Oxford Science
Publications: New York, 1987.

41.
Ramachandran, S.; Lenz, T. G.; Skiff, W. M.; Rapp\'{e}, A. K. *J. Phys. Chem.* 1996,
100, 5898-5907.

42.
(a) Kresse, G.; Furthm\"{u}ller, J. *Comput. Matter. Sci.* 1996, 6, 15-50. (b) Kresse,
G.; Furthm\"{u}ller, J. *Phys. Rev. B* 1996, 54, 11169-11186. (c) Civalleri, B.;
Zicovich-Wilson, C. M.; Ugliengo, P.; Saunders, V. R.; Dovesi, R. *Chem. Phys.
Lett.* 1998, 292, 394-402.

43.
Vos, A. M.; Rozanska, X.; Schoonheydt, R. A.; Van Santen, R. A.; Hutschka, F.;
Hafner, J. *J. Am. Chem. Soc.* 2001, 123, 2799-2809.

44.
Makov, G.; Payne, M. C. *Phys. Rev. B* 1995, 51, 4014-4022.

45.
Rozanska, X.; Van Santen, R. A.; Hutschka, F.; Hafner, J. to appear.

46.
Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, M. A.; Robb, M. A.;
Cheeseman, J. R.; Zakrzewski, V. G.; Montgomery, J. A.; Stratmann, R. E.; Burant,
J. C.; Dapprich, S.; Millam, J. M.; Daniels, A. D.; Kudin, K. N.; Strain, M. C.
Farkas, O.; Tomasi, J.; Barone, V.; Cossi, M.; Cammi, R.; Mennucci, B.; Pomelli
C.; Adamo, C.; Clifford, S.; Ochterski, J.; Petersson, G. A.; Ayala, P. Y.; Cui, Q.
Morokuma, K.; Malick, D. K.; Rabuck, D. K.; Raghavachari, K.; Foresman, J. B.
Cioslowski, J.; Ortiz, J. V.; Stefanov, B. B.; Liu, G.; Liashenko, A.; Piskorz, P.;
Komaromi, I.; Gomperts, R.; Martin, R. L.; Fox, D. J.; Keith, T.; Al-Laham, M. A.
Peng, C. Y.; Nanayakkara, A.; Gonzales, C.; Challacombe, M.; Gill, P. M. W.
Johnson, B. G.; Chen, W.; Wong, M. W.; Andress, J. L.; Head-Gordon, M.
Replogle, E. S.; Pople, J. A. Gaussian 98 (revision A.1) Gaussian, Inc.: Pittsburg
PA, 1998.

47.
(a) Becke, A. D. *Phys. Rev. A* 1988, 38, 3098-3100. (b) Lee, C.; Yang, W.; Parr, R.
G. *Phys. Rev. B* 1988, 37, 785-789. (c) Becke, A. D. *J. Chem. Phys.* 1993, 98,
5648-5652.

48.
Zygmunt, S. A.; Mueller, R. M.; Curtiss, L. A.; Iton, L. E. *J. Mol. Struct.* 1998, 430,
9-16.

49.
(a) Kresse, G.; Hafner, J. *Phys. Rev. B* **1993**, 48, 13115-13126. (b) Kresse, G.;
Hafner, J. *Phys. Rev. B* **1994**, 49, 14251-14269. (c) Kresse, G.; Hafner, J. *J. Phys.*
*Condens. Matter.* **1994**, 6, 8245-8257.

50.
Demuth, T.; Hafner, J.; Benco, L.; Toulhoat, H. *J. Phys. Chem. B* **2000**, 104, 4593-
4607.

51.
Perdew, J. P.; Zunger, A. *Phys. Rev. B* **1981**, 23, 5048-5079.

52.
Perdew, J. P.; Burke, K.; Wang, Y. *Phys. Rev. B* **1996**, 54, 16533-16539.

53.
Mills, G.; J\'{o}nsson, H.; Schenter, G. K. *Surf. Sci.* **1995**, 324, 305-337.

54.
Rozanska, X.; Saintigny, X.; Van Santen, R. A.; Hutchska, F. to appear.

55.
(a) Kumar, R.; Ratnasamy, P. *J. Catal.* **1989**, 116, 440-448. (b) Mirth, G.; Cejka, J.;
Lercher, J. A. *J. Catal.* **1993**, 139, 24-33. (c) Cortes, A.; Corma, A. *J. Catal.* **1978**,
51, 338-344. (d) Young, L. B.; Butter, S. A.; Kaeding, W. W. *J. Catal.* **1982**, 76,
418-432. (e) Beschmann, K.; Riekert, L. *J. Catal.* **1993**, 141, 548-565. (f) P\'{e}rez-
Pariente, J.; Sastre, E.; Forn\'{e}s V.; Martens, J. A.; Jacobs, P. A.; Corma, A. *Appl.*
*Catal.* **1991**, 69, 125-137. (g) Morin, S.; Gnep, N. S.; Guisnet, M. *J. Catal.* **1996**,
759, 296-304. (h) Guisnet, M.; Gnep, N. S.; Morin, S. *Microporous Mesoporous*
*Mater.* **2000**, 35-36, 47-59.

56.
Paukshtis, E. A.; Malysheva, L. V.; Stepanov, V. G. *React. Kinet. Catal. Lett.* 1998,
65, 145-152.

57.
Rozanska, X.; Van Santen, R. A.; Hutschka, F.; Hafner, J. *Stud. Surf Sci. Catal.* to
appear.

58.
Boronat, M.; Zicovich-Wilson, C. M.; Corma, A.; Viruela, P. *Phys. Chem. Chem.*
*Phys.* **1999**, 1, 537-543.

59.
Corma, A.; Sastre, G.; Viruella, P. M. *J. Mol. Catal. A* **1995**, 100, 75-85.

60.
Klein, H.; Kirschhoch, C.; Fuess, H. *J. Phys. Chem.* **1994**, 98, 12345-12360.

61.
Haag, W. O. *Zeolites and Related Materials, State of the Art 1994*; Weitkamp, H. G.,
Karge, H., Pfeifer, H., H\"{o}lderich, W., Eds.; Elsevier Science: Amsterdam, 1994; pp
1375-1394.

62.
Corma, A.; Llopis, F.; Viruela, P.; Zicovich-Wilson, C. *J. Am. Chem. Soc.* **1994**,
116, 134-142.

63.
Ivanova, I.I.; Corma, A. *J. Phys. Chem. B* **1997**, 101, 547-551.

64.
Blaszkowski, S. R.; Van Santen, R. A. *Transition State Modeling for Catalysis*;
Truhlar, D. G., Morokuma, K., Eds.; ACS Symp. Ser. No. 721; American Chemical
Society: Washington, DC, 1999; Chapter 24

65.
Norman, G. H.; Shigemura, D. S.; Hopper, J. R. *Ind. Eng. Chem., Prod. Res. Dev.*
**1976**, 15, 41-45.

66.
Rozanska, X.; Van Santen, R. A.; Hutschka, F.; Hafner, J. to appear.

67.
Weber, T.; Prins, R.; Van Santen, R. A. *Transition Metal Sulphides, Chemistry and*
*Catalysis*; Eds.; NATO ASI Series 3, 1998; Vol. 60.

68.
Michaud, P.; Lemberton, J. L.; P\'{e}rot, G. *Appl. Catal. A* **1998**, 169, 343-353.

69.
Landau, M. V. *Catal. Today* **1997**, 36, 393-429.

70.
Rozanska, X.; Van Santen, R. A.; Hutschka, F. to appear.

71.
Van Santen, R. A. *J. Mol. Catal. A* **1997**, 115, 405-419.

72.
Bates, S.; Van Santen, R. A. *Adv. Catal.* **1998**, 42, 1-114.
