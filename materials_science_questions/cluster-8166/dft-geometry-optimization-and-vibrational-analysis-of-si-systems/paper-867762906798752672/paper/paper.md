
# Hydrogen dynamics and light-induced structural changes in hydrogenated amorphous silicon

T. A. Abtew \( ^{*} \)  and D. A. Drabold \( ^{\dagger} \) 

Department of Physics and Astronomy, Ohio University, Athens, OH 45701
(Dated: October 8, 2018)

We use accurate first principles methods to study the network dynamics of hydrogenated amorphous silicon, including the motion of hydrogen. In addition to studies of atomic dynamics in the electronic ground state, we also adopt a simple procedure to track the H dynamics in light-excited states. Consistent with recent experiments and computer simulations, we find that dihydride structures are formed for dynamics in the light-excited states, and we give explicit examples of pathways to these states. Our simulations appear to be consistent with aspects of the Staebler-Wronski effect, such as the light-induced creation of well-separated dangling bonds.

PACS numbers: 61.43.-j, 66.30.-h, 71.23.-k, 78.20.Bh

## I. INTRODUCTION

A variety of experiments and many theoretical studies of light-induced structural changes in hydrogenated amorphous silicon (a-Si:H) reveal the complexity of photoresponse in these materials. Light-induced changes in photoconductivity and defect formation \( ^{1,2,3} \) , enhanced hydrogen diffusion \( ^{4,5,6,7,8} \) , and creation of preferential proton separation \( ^{9} \)  are among the phenomena observed experimentally in a-Si:H. A special feature of these materials is the Jekyll-Hyde behavior of hydrogen as a defect passivator enabling the practical utilization of the material but also as a culprit in light-induced defect creation \( ^{10,11,12,13} \) . A variety of experiments implicate H and its dynamics as being important player to the SWE \( ^{14} \) .

There are various models proposed to explain the light-induced metastability. Chang et al. \( ^{15,16,17} \)  suggested that the dissociation of a two hydrogen interstitial complex,  \( (\mathrm{H}_{2}^{*}) \) , into separate and more mobile H atoms, caused by carriers localized on the  \( H_{2}^{*} \) , is a mechanism for the metastable phenomena. In the hydrogen flip model, Biswas et al. demonstrated a higher energy metastable state is formed when H is flipped to the backside of the Si-H bond at a monohydride sites \( ^{18} \) . In the hydrogen collision model proposed by Branz \( ^{6} \) , the recombination-induced emission of H from Si-H bond creates mobile H and dangling bonds, and these newly created dangling bonds become metastable when two mobile H atoms collide to form a metastable complex containing two Si-H bonds. The two-phase model of Zafar and Schiff \( ^{19,20} \) , explained thermal stability data, exploited the concept of paired hydrogen, and later merged with Branz model and invoked dihydride bonding \( ^{21} \) . Though they have different detailed mechanisms for the formation of the structures, these models share the same notion that the diffusion of H and H pair formation plays a key role in light-induced metastability. From ab initio simulation in a photo-excited state, Fedders, Fu and Drabold showed that changes of charge of well-localized defect states could induce defect creation \( ^{22} \) . Our work can be regarded as a natural extension of Ref. 22 to the case of a hydrogenated system, and with more accurate techniques than those available at the time of the original study.

Our work has been particularly driven by the experimental work of Su et al. \( ^{9} \) , who performed proton NMR experiments in a-Si:H and found preferential creation of H-H distance of  \( 2.3 \pm 0.2 \)  Å. We have shown that  \( SiH_{2} \)  configurations in the solid state are consistent with these observations \( ^{23} \) . More recently, an NMR study by Bobela et al. \( ^{24} \) , indicated a shorter proton-proton distance in a sample of a-Si:H with a somewhat higher defect density.

In a recent paper \( ^{25} \) , we briefly reported the hydrogen dynamics and light-induced formation of a  \( SiH_{2} \)  structure for a small (71 atom) model. In this article, we provide detailed results of simulation on electronic properties, vibrational properties and mechanism of hydrogen diffusion in both the electronic ground state and light excited state in a-Si:H using two different supercell models: a larger 223 atom a-Si:H model (Model-I) and a 71 atom a-Si:H model [Model-II]. We start with small, but topologically credible models of a-Si:H and use a sufficiently accurate method to simulate network dynamics, including the diffusive motion of hydrogen. In a photo-excited MD simulation, we find enhanced H motion and the preferential formation of a paired-H final states, a significant confirmation of aspects of some current influential models \( ^{6} \) . Furthermore, we obtain final states with additional dangling bond defects, well separated from each other, again in agreement with key experiments \( ^{26} \) . Our simula-
 

tions suffer from limitations: small cells and certainly a limited sampling of the possible motions of H, limited simulation times and approximations of various forms described below. Nevertheless, we believe that studies of this type offer significant promise as an “unbiased” means to discover the importance of H motion, its topological and electronic consequences, and provide another needed piece to a complex puzzle.

The rest of the paper is organized as follows. In Sec. II we discuss the approximations used in the ab initio local basis code SIESTA \( ^{27,28,29} \) . describe the procedure for generating the models and also discuss the methods used to simulate both the electronic ground state and the light excited state. In Sec. III we present detailed discussions of the molecular dynamics calculations of Hydrogen dynamics and its consequences both in the electronic ground state and in the presence of light excitation. The change in the electronic structures and vibrational modes are explained in detail. We present conclusions in Sec. IV.

## II. METHODOLOGY

## A. Total energies, electronic structure and dynamical simulation

Simulation of complex a-Si:H models require accurate interatomic interactions (in particular, H energetics is highly delicate in a-Si:H) \( ^{30,31} \) . Therefore, our density functional simulations were performed within the generalized gradient approximation \( ^{32} \)  (GGA) or the local density approximation (LDA) using the first principles code SIESTA \( ^{27,28,29} \) . Norm conserving Troullier-Martins \( ^{33} \)  pseudopotentials factorized in the Kleinman-Bylander \( ^{34} \)  form were used. All calculations in this paper employed optimized double  \( \zeta \)  polarized basis sets (DZP), where two s and three p orbitals for the H valence electron and two s, six p and five d orbitals for Si valence electrons were used. The structures were relaxed until the forces on each atom were less than 0.04 eV/ \( \AA \) . We used a plane wave cutoff of 100 Ry for the grid (used for computing multi-center matrix elements) with  \( 10^{-4} \)  for the tolerance of the density matrix in self consistency steps. We solved the self-consistent Kohn-Sham equations by direct diagonalization of the Hamiltonian and a conventional mixing scheme. The  \( \Gamma \)  point was used to sample the Brillouin zone in all calculations.

Density functional theory in the LDA, or with gradient corrections, maps the ground state many-electron problem onto a system of non-interacting fermions \( ^{35} \) . In principle, the eigenvalues of the resulting single-particle equations are not true excitation energies and the spectral gap between occupied and unoccupied states is well known to be incorrect \( ^{36} \) . Nevertheless, the eigenvectors of the problem (the Kohn-Sham orbitals) have been shown to be very similar to quasiparticle states from “GW” calculations, in which the self-energy is expressed as a product of the single particle Green’s function “G” and the dynamically screened Coulomb interaction “W” as used in many-body calculations \( ^{37} \) . For Si, C and LiCl, Hybertsen and Louie \( ^{38} \)  found 99.9% overlap between “GW” states and the Kohn-Sham orbitals. On an empirical level for amorphous materials, there are many indications that it is profitable to interpret the Kohn-Sham orbitals “literally” for comparisons to experiment \( ^{39,40} \) . This provides some rationale for interpreting the Kohn-Sham orbitals as quasiparticle states, as we shall in some subsequent parts of this paper.

## B. Models

A predictive simulation requires a physically plausible model that represents the topology of the network and yields an accurate description for dynamics of the atoms. In this article we have used two different supercell models: a 223 atom a-Si:H model (Model-I) and a 71 atom a-Si:H model ([Model-II]). These models are generated from a 64 atom and a 216 atom a-Si models which were generated by Barkema and Mousseau \( ^{41} \)  using an improved version of the Wooten, Winer, and Weaire (WWW) algorithm \( ^{42} \)  respectively.

To create the a-Si:H environment a) We started from a 216 atom a-Si model with two dangling bonds, we removed two silicon atoms resulting in the formation of additional vacancies. All of the vacancies except one are then terminated by placing a H atom at about 1.5 Å from the corresponding Si atom. This yield a 223 atom Model-I. b) We started from a defect free 64 atom a-Si model, we removed three silicon atoms resulting in the formation of vacancies. All of the dangling bonds are then terminated by placing a H atom at about 1.5 Å from the corresponding Si atom to generate a 71 atom Model-II. We then repeated this supercell surgery at other sites to generate an ensemble of three configurations to obtain some insight into the formation of the structure and its bonding in solid state. Finally these newly generated structures are well relaxed using conjugate gradient optimization technique. While such a procedure is clearly unphysical, it is worth pointing out that the resulting proton NMR second moments of the clusters created are similar to the broad component of the lineshape observed
 

in experiments \( ^{43} \) .

## C. Excited state dynamics and promotion of carriers

Defects in an amorphous network may lead to localized electron states in the optical gap or in the band tails. If such a system is exposed to band gap light, it becomes possible for the light to induce transitions from the occupied states to unoccupied states. For the present work we will not concern ourselves with the subtleties of how the EM field introduces the transition, we will simply assume that a photo-induced promotion occurs, by depleting the occupied states of one electron “forming a hole” and placing the electron near the bottom of the unoccupied “conduction” states. The idea is that a system initially at equilibrium will not be after the procedure: Hellmann-Feynman forces \( ^{44} \)  due to the occupation change will cause structural rearrangements, which may be negligible or dramatic, depending on the flexibility or stability of the network, and the localization of the states. The changes in force will initially be local to the region in which the orbitals are localized, followed by transport of the thermal energy. In general, it is necessary to investigate photo-structural changes arising from various different initial and final states, though only well localized states near the gap have the potential to induce structural change \( ^{22,45,46,47,48} \) . The simulated light excited state is achieved by implementing: a) starting from the well relaxed model, we make the occupation change by adding an additional electron just above the Fermi level, b) we keep the system in this excited state for 10ps (20000 MD steps with time step  \( \tau=0.5 \)  fs between each MD steps), and maintain a constant temperature T=300K, c) after 10ps, we put the system back into the ground state and relax to minimize the energy. The method has been described in additional detail elsewhere \( ^{45} \) .

## III. HYDROGEN DYNAMICS

We have performed extensive MD simulations of network dynamics of a-Si:H both in an electronic ground state (“light-off”) and a simulated light-excited states (“light-on”) for the two models, Model-I and Model-II described above. In the next sections, we present a detailed calculation of hydrogen diffusion, its mechanisms and consequences on the structural, electronic and vibrational properties in both electronic ground state and light excited state.

## A. Hydrogen motion: Ground State

To analyze the diffusion mechanism in the ground state we performed a MD simulation for five different temperatures, and tracked the trajectories and bonding information of all the H and Si atoms in the network. In all the cases, the MD simulations show diffusion of hydrogen in the cell and as a consequence, the network exhibits bond break and formation processes. The pattern of diffusion differs for individual H atoms depending upon the geometrical constraints around the diffusing H atom.

![](./images/867762906798752672_1.jpg)

FIG. 1: Trajectory for three different hydrogen atoms ( \( H_{219} \)  and  \( H_{220} \) ) in the ground state, which shows the diffusion and trapping of the atom for Model-I model. The total time for the trajectory is 10ps.

In order to characterize the trajectories of H diffusion in the ground state, we have selected two diffusive H atoms, (H_{219} and H_{220}), and plotted their trajectories at T=300K in Fig. 1. The trajectories for both H_{219} and H_{220} atoms show diffusion in which the H atoms spend time being trapped in a small volume of the cell which is followed by rapid emission to another trapping site. In order to examine how the bond rearrangement takes place in the network while the H atom is diffusing, we tracked each hydrogen atoms and computed its bonding statistics.

In Fig. 2 we show the Si-H bond length between one of the diffusing H atoms (namely  \( H_{219} \) ) and relevant Si atoms ( \( Si_{90} \)  and  \( Si_{128} \) ) with which it forms a bond while diffusing and  \( Si_{208} \) . As we can see from Fig. 2, in the
 
![](./images/867762906798752672_2.jpg)

FIG. 2: The Si-H bond length between the diffusing H ( \( H_{219} \) ) and three different Si atoms, (Si_{90}, Si_{208}, and Si_{128} as a function of time in the electronic ground state for Model-I. The total time for the trajectory is 10ps.

first 4ps  \( H_{219} \)  is bonded with  \( Si_{90} \)  with a bond length of 1.5 Å and trapped for a while until it breaks and hops to form another bond with  \( Si_{128} \) . In the first  \( \sim \) 4 ps, the bond length between  \( H_{219} \)  and  \( Si_{128} \)  fluctuates between 3.8 Å and 2.5 Å. However, after  \( \sim \) 4 ps we observed a swift bond changes in a very short period of time  \( \sim \) 0.1 ps when the  \( H_{219} \)  atom comes out of the trapping site and hops to form a bond with  \( Si_{128} \)  and trapped there for a very long time period of  \( \sim \) 6 ps. This process of trapping and hopping is typical for the highly diffusive H atoms.

To study atomic diffusion we computed the time average mean squared displacement for both H and Si atoms for a given temperature using

 \[ \langle\sigma^{2}(\alpha,T)\rangle_{t i m e}=\frac{1}{N_{M D}}\frac{1}{N_{\alpha}}\sum_{t=1}^{N_{M D}}\sum_{i=1}^{N_{\alpha}}|\vec{r}_{i}^{\alpha}(t)-\vec{r}_{i}^{\gamma\alpha}(0)|^{2}, \quad (1) \] 

where the sum is over particular atomic species  \( \alpha \)  (Si or H),  \( N_{\alpha} \)  and  \( \vec{r}_{i}^{\alpha}(t) \)  are total number and coordinates of the atomic species  \( \alpha \)  at time t respectively, and  \( N_{MD} \)  is the total number of MD steps.

The time average mean square displacement for Model-II for five different temperatures was calculated using Eq. (1) for H atoms in the supercell in the electronic ground state (light-off) and it is shown in Fig. 3. We

![](./images/867762906798752672_3.jpg)

FIG. 3: Time average mean square displacement for H as a function of temperature of MD simulation in electronic ground state for Model-II model.

have observed a strong temperature dependence of H diffusion. This result will help us to compare the diffusion of H in the electronic ground state with the light excited state to be discussed in the next section.

## B. Hydrogen diffusion: light excited state

Similar to the case of electronic ground state, we analyzed the diffusion of H in the light excited state by performing a MD simulation. We tracked the trajectories and bonding statistics of Si and H atoms in the supercell. Our MD simulation in the light excited state shows enhanced hydrogen diffusion and consequently increased bond breaking and formation that leads to structural changes in the network.

For the purpose of analyzing the difference in the diffusion mechanism of H in the light excited state case as compared with the ground state, we performed similar calculations described in the previous sections for the light excited state case. To see the trajectories of H in the light excited state, we have again selected two diffusive H atoms, ( \( H_{219} \)  and  \( H_{220} \) ) from the larger Model-I, and plotted their trajectories in the light excited state in Fig. 4. The trajectories show the diffusion of H in the presence of different trapping centers, a region where the H atom spends more time before it hops and moves to another trapping site. However, in this case we ob-
 
![](./images/867762906798752672_4.jpg)

FIG. 4: Trajectory for three different hydrogen atoms ( \( H_{219} \)  and  \( H_{220} \) ) which shows the diffusion and trapping of the atom for Model-I in the light excited state. The total time for the trajectory is 10ps.

served enhanced diffusion and more trapping sites and hopping. These trapping and hopping processes continue until two hydrogens form a bond to a single Si atom to form a metastable  \( SiH_{2} \)  conformation or until two hydrogens form a bond to (a) two different Si atoms which are bonded to each other, to form (H-Si-Si-H) structure or (b) two different Si atoms which are not bonded but close to each other to form (H-Si Si-H) structure. This is in agreement with a basic event of the H collision model \( ^{6} \)  and other H-pairing models \( ^{21} \) .

By tracking each H atom, we computed its bonding statistics and examine the bond rearrangements. In Fig. 5 we show Si-H bond length as a function of time between one of the diffusing H atoms ( \( H_{219} \) ) and three other Si atoms ( \( Si_{90} \) ,  \( Si_{128} \) , and  \( Si_{208} \) ) with which it forms a bond while diffusing in the network. The initial trapping time, where  \( H_{219} \)  is bonded with  \( Si_{90} \) , is reduced to  \( \sim1.8 \)  ps when the light is on from  \( \sim4 \)  ps when the ligth is off. This is followed by another trapping site where  \( H_{219} \)  is bonded with  \( Si_{208} \)  for another  \( \sim2.1 \)  ps. The  \( H_{219} \)  hops out of the trapping site and forms a bond with  \( Si_{128} \)  and trapped for  \( \sim4.3 \)  ps before it finally hops out from the trapping site and forms another bond with  \( Si_{208} \)  where it gets trapped again and form a silicon dihydride ( \( SiH_{2} \) ) structure. As we can see from Fig. 5, the pattern of diffusion is quite different from the ground state: In the light excited state case we observed a) more number of trapping sites and less trapping time with frequent hopping, b) enhanced hydrogen diffusion, and c) increasing num-

![](./images/867762906798752672_5.jpg)

FIG. 5: The Si-H bond length between the diffusing H ( \( H_{219} \) ) and three different Si atoms ( \( Si_{90} \) ,  \( Si_{128} \) , and  \( Si_{208} \) ) with which  \( H_{219} \)  forms a bond (one at a time) while it is diffusing as a function of time for Model-I, in the light excited state. The total time for the trajectory is 10ps.

ber of bond rearrangements and newly formed dihydride structural units.

The atomic diffusion in the light excited state case has also been examined using the time average mean squared displacement for both H and Si atoms for different temperatures using Eq. 1 for both Model-I and Model-II. The results from Model-II is shown in Fig. 6. For all the temperatures considered, our simulation results show enhanced diffusion of Hydrogen for the case when the light is “on” as compared with the case where the light is “off”. Consistent with the work of Isoya \( ^{26} \) , the hopping of H is apparently stimulated by the electron-hole pair. The enhanced diffusive motion of H in the photo excited state relative to the electronic ground state arises from the strong electron-lattice interaction of the amorphous network, and an effect of “local heating” and subsequent thermal diffusion \( ^{46} \)  initially in the spatial volume in which the state is localized. The same calculations has also been performed on the larger model Model-I at T=300K in which, the time average mean square displacement for H is 2.66 Å \( ^{2} \)  for the light excited state and 1.10 Å \( ^{2} \)  for the electronic ground state. These results again show and confirm an enhanced hydrogen diffusion for the case of light excited state. In all the cases no enhanced motion for Si is observed
 
![](./images/867762906798752672_6.jpg)

FIG. 6: Time average mean square displacement for Has a function of temperature of MD simulation in the light excited for Model-II.

## C. Consequences of Hydrogen diffusion

## 1. Formation of dihydride structure

In the two scenarios that we considered, MD simulation in electronic ground state (light off) and simulated light-excited state (light on) we have observed an important difference. In the light-excited state, in addition to bond rearrangements and enhanced hydrogen diffusion, we have observed a preferential formation of new structure:  \( SiH_{2} \) , with an average distance of 2.39 Å for the pair of hydrogens in the structure, (H-Si-Si-H) and (H-Si Si-H) with H-H separation which ranges from 1.8 Å to 4.5 Å. However, in the electronic ground state, we have obtained rearrangement of atoms including hydrogen diffusion, without formation of  \( SiH_{2} \)  structure in the supercell. The mechanisms for the formation of these structures in the light-excited state follows breaking of H atom from Si-H bond close to the dangling bonds and diffusion to the nearest weakly bonded interstitial sites (or dangling bonds). This mobile H atom then collides (forms a metastable bond) with another Si+DB structure or breaks an Si-Si bond to form another Si-H bond. This is attributed to the fact that the dangling bond site is moving to accommodate the change in force caused by the additional carrier and also because hydrogen is moving through weakly bonded interstitial sites with low activation barrier for diffusion until it is trapped by a defect \( ^{49} \) .

We find that there are two different modes of bond formation for the mobile hydrogen. The first is when two mobile hydrogen atoms,  \( H_{m} \) , collide with two Si atoms and form a metastable (H-Si-Si-H) or (H-Si Si-H) structure and the second one is when the mobile hydrogen moves until it encounters a preexisting Si-H+DB structure and makes a bond to form a  \( SiH_{2} \)  structure.

Consequently, our calculations show two basic ideas for the diffusion of H in the light-excited state: 1) the diffusion of hydrogen doesn’t only break a Si-H bond but it also breaks a Si-Si bond and 2) the possibility that two mobile H atoms might form a bond to a single Si atom to form a metastable  \( SiH_{2} \)  structure in addition to the formation of (H-Si-Si-H) and (H-Si Si-H) structures.

In the Model-II, the two hydrogens involved in the formation of the  \( SiH_{2} \)  structure initially were 5.50 Å apart and bonded to two different Si atoms (Si-H) which were separated by 4.86 Å. With thermal simulation in the light excited state, the two hydrogen atoms dissociate from their original Si atoms and becomes mobile until they form the  \( SiH_{2} \)  structure, in which the H-H distance becomes 2.39 Å. We have observed similar pattern of H diffusion, bond rearrangements and formation of  \( SiH_{2} \)  structure near the DB for the other two configurations considered in the simulation. The same phenomenon is observed in the case of Model-I. The two hydrogens involved in the formation of the  \( SiH_{2} \)  structure initially were 3.29 Å apart and bonded to two different Si atoms (Si-H) which were separated by 3.92 Å. With thermal simulation in the light excited state, the two hydrogen atoms dissociate from their original host and becomes mobile until they form the  \( SiH_{2} \)  structure, in which the H-H distance becomes 2.45 Å. We have summarized the results that show before and after MD calculations of H-H distance (in  \( SiH_{2} \)  structure) for Model-I and three different configurations of Model-II in the case of light excited state in Table I.

## 2. Change in the electronic properties

In order to understand the electron localization we used the inverse participation ratio, I,

 \[ \mathcal{I}=\sum_{i=1}^{N}[q_{i}(E)]^{2} \quad (2) \] 

where  \( q_{i}(E) \)  is the Mulliken charge residing at an atomic site i for an eigenstate with eigenvalue E that satisfies  \( \sum_{i}^{N}[q_{i}(E)] = 1 \)  and N is the total number of atoms in the
 

TABLE I: The H-H distance in the  \( SiH_{2} \)  configurations and the Fermi energy of the system before and after MD simulations in the light excited case.

<table><tr><td rowspan="2">Configurations</td><td colspan="2">H-H distance</td></tr><tr><td>before MD ( \( \textup{\AA} \) )</td><td>after MD ( \( \textdown{\AA} \) )</td></tr><tr><td>1 (Model-II)</td><td>5.50</td><td>2.39</td></tr><tr><td>2 (Model-II)</td><td>3.79</td><td>2.36</td></tr><tr><td>3 (Model-II)</td><td>4.52</td><td>2.36</td></tr><tr><td>4 (Model-I)</td><td>3.29</td><td>2.45</td></tr><tr><td>Average</td><td></td><td>2.39</td></tr></table>

cell. For an ideally localized state, only one atomic site contributes all the charge and so I = 1. For a uniformly extended state, the Mulliken charge contribution per site is uniform and equals 1/N and so I = 1/N. Thus, large I corresponds to localized states. With this measure, we observe a highly localized state near and below the Fermi level and a less localized state near and above the Fermi level. These states, highest occupied molecular orbitals (HOMO) and lowest unoccupied molecular orbitals (LUMO), are centered at the two dangling bonds in the initial configuration of the model. The energy splitting between the HOMO and LUMO states is 1.08 eV. Figure 7 (a) shows the Fermi level and I of these two states and other states as a function of energy eigenvalues in the relaxed electronic ground state.

This picture changes when we excite the system and perform a MD calculation in which we observe enhanced diffusion of hydrogen and subsequent breaking and formation of bonds. Since electron-phonon coupling is large for localized states \( ^{50} \) , the change of occupation causes the forces in the localization volume associated with the DB to change and the system moves to accommodate the changed force. Consequently, the hydrogen atoms close to the DB sites start to move in the vicinity of these defects either to terminate the old DB’s or to break a weak Si-Si bond and by doing so, create new DB defects on nearby sites. As shown in Fig. 7 (b) we observe the formation a highly localized state and appearance of three less localized states, that correspond to the newly formed defect levels after simulated light-soaking. These processes induce transition of electrons from the top of the occupied states to the low-lying unoccupied states which is reflected in the smaller value of I for the initial HOMO state and an increase in the I for the LUMO

![](./images/867762906798752672_7.jpg)

FIG. 7: (Color Online) The inverse participation ratio I of the eigenstates versus the energy eigenvalues, (a) in the relaxed electronic ground state and (b) in the relaxed simulated light-excited state (light excited MD followed by relaxation), with their respective Fermi energy in the first configuration of relaxed Model-II. The inset (c) shows the electron density of states with the Fermi level shifted to zero for the relaxed simulated light-excited state.

state.

The I of the HOMO state, where the state is initially localized, decreases from 0.158 to 0.060 after photoexcitation, while the I of the LUMO state increases from 0.045 to 0.142. The splitting energy between the HOMO and LUMO states has also declined to 0.723 eV. The newly formed defects with lower energy splitting between the HOMO and LUMO states suggest a presence of carrier induced bond rearrangements in the supercell. The comparisons for the energy and I of the system before MD (as relaxed) and after MD is given in Table II.

In addition, analysis of the spatial distribution of the configurations shows that the H atoms close to the dangling bonds (< 4.0 Å) are most diffusive and the Si atoms which make most of the bond rearrangements including the Si atom in the  \( SiH_{2} \)  configurations are close (< 5.50 Å) to the dangling bonds. These show the additional charge carrier induces change in the forces around the dangling bonds and consequently rearranges the atoms.
 
![](./images/867762906798752672_8.jpg)

FIG. 8: (Color Online) The energy density of states and the inverse participation ratio I of the eigenstates versus the energy eigenvalues, (a) in the relaxed electronic ground state and (b) in the relaxed simulated light-excited state (light excited MD followed by relaxation), both the electron density of states and the inverse participation ration are plotted with the Fermi level shifted to zero.

TABLE II: The energy and the inverse participation ratio I of localized states HOMO, LUMO, LUMO+1 and LUMO+2 before and after the MD for Model-II.

<table><tr><td></td><td colspan="2">Eigenvalue</td><td colspan="2">&amp;I</td></tr><tr><td></td><td>before MD (eV)</td><td>after MD (eV)</td><td>before MD</td><td>after MD</td></tr><tr><td>HOMO</td><td>-4.32</td><td>-4.40</td><td>0.158</td><td>0.060</td></tr><tr><td>LUMO</td><td>-3.24</td><td>-3.68</td><td>0.045</td><td>0.142</td></tr><tr><td>LUMO+1</td><td>-2.88</td><td>-3.08</td><td>0.037</td><td>0.064</td></tr><tr><td>LUMO+2</td><td>-2.66</td><td>-2.87</td><td>0.030</td><td>0.042</td></tr></table>

around the dangling bond sites and eventually forming an  \( SiH_{2} \)  structure. On average the newly formed defect sites are 3.80 Å and 4.70 Å far away from the two initial defect sites. The newly formed  \( SiH_{2} \)  structure is (on average) 4.11 Å away from the initial defect sites. It is probable that limitations in both length and time scales influence these numbers, but it is clear that the defect creation is not very local because of the high diffusivity of the H.

The same calculation have been performed on Model-II. In Fig. 8 we have plotted both energy density of states and inverse participation ratio as a function of energy in the light excited state case before and after the MD simulation. As can be seen from the figure we obtained more localized states in the middle of the gap which are caused due to an increase in the number of defects upon light excitation. This supports that the diffusion of hydrogen not only forms preferential dihydride structures but also increase the number of defects in agreement with our findings for the smaller cell model of asiH-71.

## 3. Change in the vibrational properties

For an amorphous solid, the vibrational density of state is a sum of 3N (N is the number of atoms) delta functions corresponding to the allowed frequency modes. Starting with the relaxed Model-II subsequent to MD in the light excited state, we computed the vibrational energies (vibrational modes) from the dynamical matrix, which is determined by displacing each atom by 0.02 Å in three orthogonal directions and then performing ab initio force calculations for all the atoms for each displacement to obtain the force constant matrix, and with diagonalization, phonon frequencies and modes.

TABLE III: Frequency for some of the Si-H vibrational modes of the  \( SiH_{2} \)  conformation for the first two configurations of the Model-II obtained from our MD simulations and their corresponding experimental values \( ^{51,52,53} \) .

<table><tr><td>Configurations</td><td>Rocking cm \( ^{-1} \)</td><td>Scissors cm \( ^{-1}\)</td><td>Stretch cm \( ^{-1} \)</td></tr><tr><td>1</td><td>629</td><td>810</td><td>2025</td></tr><tr><td>2</td><td>625</td><td>706</td><td>2047</td></tr><tr><td>Experiment</td><td>630</td><td>875</td><td>2090</td></tr></table>

In our calculations, the VDOS shows H modes of vibrations in the range (600-900) cm \( ^{-1} \)  and also in the range (1800-2100) cm \( ^{-1} \) . We have examined the vibrational modes to pick out those modes arising only from SiH \( _{2} \) . We reproduce the vibrational modes of SiH \( _{2}^{-} \)  and their corresponding experimental values \( ^{51,52,53} \)  in Table
 

III. The first mode is the rocking mode at  \( 629 \, cm^{-1} \)  and  \( 625 \, cm^{-1} $ ; the second is the scissors mode at  \( 810 \, cm^{-1} \)  and  \( 706 \, cm^{-1} $  and the last is the asymmetric stretching mode that occur at  \( 2025 \, cm^{-1} \)  and  \( 2047 \, cm^{-1} $  for the first and second configurations respectively. These results are in good agreement with the IR absorption spectra for the  \( SiH_{2} \)  structure. The comparison of our results for the vibrational modes of  \( SiH_{2} \)  with the experiment is summarized in Table III. The results shown in Table III are sensitive to the basis sets used in the calculation, in agreement with other work emphasizing the delicacy of H dynamics \( ^{30} \) .

## IV. CONCLUSION

We have presented a direct ab-initio calculation of network dynamics and diffusion both for the electronic ground state and light-excited state for a-Si:H. We computed the preferential diffusion pathways of hydrogen in the presence of photo-excited carriers. In the light-excited state, we observe enhanced hydrogen diffusion and formation of new silicon dihydride configurations, (H-Si-Si-H), (H-Si Si-H), and SiH \( _{2} \) . The two hydrogens in the SiH \( _{2}^{-} \)  unit show an average proton separation of

* Electronic address: abtew@phy.ohiou.edu

 \( ^{\dagger} \)  Electronic address: drabold@ohio.edu

 \( ^{1} \)  D. L. Staebler and C. R. Wronski, Appl. Phys. Lett. 31, 292 (1977).

 \( ^{2} \)  M. Stutzmann, W. B. Jackson, and C. C. Tsai, Phys. Rev. B 32, 23 (1985).

 \( ^{3} \)  D. Han, J. Baugh, G. Yue, and Q. Wang, Phys. Rev. B 62, 7169 (2000).

 \( ^{4} \)  W. B. Jackson and J. Kakalios, Phys. Rev. B 37, 1020 (1988).

 \( ^{5} \)  P. V. Santos, N. M. Johnson, and R. A. Street, Phys. Rev. B 67, 2686 (1991).

 \( ^{6} \)  H. M. Branz, Phys. Rev. B 59, 5498 (1999).

 \( ^{7} \)  H. M. Branz, S. Asher, H. Gleskova, and S. Wagner, Phys. Rev. B 59, 5513 (1999).

 \( ^{8} \)  H. M. Cheong, S. Lee, B. P. Nelson, A. Mascarenhas, and S. K. Deb, Appl. Phys. Lett. 77, 2686 (2000).

 \( ^{9} \)  T. Su, P. C. Taylor, G. Ganguly, and D. E. Carlson, Phys. Rev. Lett. 89, 015502 (2002).

 \( ^{10} \)  K. Zellama, P. Germain, S. Squelard, B. Bourdon, J. Fontenille, and R. Danielou, Phys. Rev. B 23, 6648 (1981).

 \( ^{11} \)  M. Kemp and H. M. Branz, Phys. Rev. B 52, 13946 (1995).

 \( ^{12} \)  B. Tuttle, C. G. Van de Walle, and J. B. Adams, Phys. Rev. B 59, 5493 (1999).

2.39 Å. The results are consistent (a) with the recent NMR experiments and our previous studies, and (b) with the hydrogen collision model of Branz and other paired hydrogen model in the basic diffusion mechanism and formation of dihydride structures. In contrast, simulations in the electronic ground state do not exhibit the tendency to  \( SiH_{2} \)  formation. Undoubtedly, other H diffusion pathways exist, and the importance of larger simulation length and time scales as well as effects of promotions involving different states (which could include strain defects and floating bonds \( ^{54} \) ) should be undertaken. For the first time, we show the detailed dynamic pathways that arise from light-induced occupation changes, and provide one explicit example of defect creation and paired H formation.

## ACKNOWLEDGMENTS

We acknowledge support from the National Science Foundation under NSF-DMR 0310933, 0205858 and the Army Research Office (ARO). We thank Prof. E. A. Schiff for many helpful conversations and suggestions, and Profs. P. A. Fedders and P. C. Taylor for collaboration and discussions.

 \( ^{13} \)  Y. -S. Su and S. T. Pantelides, Phys. Rev. Lett. 88, 165503 (2002).

 \( ^{14} \)  R. A. Street, Hydrogenated amorphous silicon (Cambridge, UK, 1991).

 \( ^{15} \)  K. J. Chang and D. J. Chadi, Phys. Rev. Lett. 62, 937 (1989).

 \( ^{16} \)  K. J. Chang and D. J. Chadi, Phys. Rev. B 40, 11644 (1989).

 \( ^{17} \)  S. B. Zhang, W. B. Jackson, and D. J. Chadi, Phys. Rev. Lett. 65, 2575 (1990).

 \( ^{18} \)  R. Biswas and Y. -P. Li, Phys. Rev. Lett. 82, 2512 (1999).

 \( ^{19} \)  S. Zafar and E. A. Schiff, Phys. Rev. B 40, 5235 (1989).

 \( ^{20} \)  S. Zafar and E. A. Schiff, Phys. Rev. Lett. 66, 1493 (1991).

 \( ^{21} \)  N. Kopidakis and E. A. Schiff, J. Non. Cryst. Solids 266-269, 415 (2000).

 \( ^{22} \)  P. A. Fedders, Y. Fu, and D. A. Drabold, Phys. Rev. Lett. 68, 1888 (1992).

 \( ^{23} \)  T. A. Abtew, D. A. Drabold, and P. C. Taylor, Appl. Phys. Lett. 86, 241916 (2005).

 \( ^{24} \)  D. Bobela, T. Su, P. C. Taylor, and G. Ganguly, to be published.

 \( ^{25} \)  T. A. Abtew and D. A. Drabold, J. Phys.: Condens. Matter Lett. 18 L1 (2006).

 \( ^{26} \)  J. Isoya, S. Yamasaki, H. Oshuhi, A. Matsuda, and K.
 

Tanaka, Phys. Rev. B 47, 7013 (1993).

 \( ^{27} \)  P. Ordejón, E. Artacho, and J. M. Soler, Phys. Rev. B 53, 10441 (1996).

 \( ^{28} \)  D. Sánchez-Portal, P. Ordejón, E. Artacho, and J. M. Soler, Int. J. Quantum Chem. 65, 453 (1997).

 \( ^{29} \)  J. M. Soler, E. Artacho, J. D. Gale, A. García, J. Junquera, P. Ordejón, and D. Sánchez-Portal, J. Phys.: Condens. Matter 14, 2745 (2002).

 \( ^{30} \)  C. G. Van de Walle, Phys. Rev. B 49, 4579 (1994).

 \( ^{31} \)  R. Atta-Fynn, P. Biswas, P. Ordejón and D. A. Drabold, Phys. Rev. B 69, 085287 (2004).

 \( ^{32} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

 \( ^{33} \)  N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).

 \( ^{34} \)  L. Kleinman and D. M. Bylander, Phys. Rev. Lett. 48, 1425 (1982).

 \( ^{35} \)  P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 (1965).

 \( ^{36} \)  R. M. Martin, Electronic Structure, Basic Theory and Practical Methods (Cambridge, UK, 2004) p. 145.

 \( ^{37} \)  L. Hedin, Phys. Rev. 139, A796 (1965).

 \( ^{38} \)  M. S. Hybertsen and S. G. Louie, Phys. Rev. B 34, 5390 (1986).

 \( ^{39} \)  D. A. Drabold, P. A. Fedders, S. Klemm, and O. F. Sankey, Phys. Rev. Lett. 67, 2179 (1991).

 \( ^{40} \)  F. Mauri and R. Car, Phys. Rev. Lett. 75, 3166 (1995).

 \( ^{41} \)  G. T. Barkema and N. Mousseau, Phys. Rev. B 62, 4985 (2000).

 \( ^{42} \)  F. Wooten, K. Winer, and D. Weaire, Phys. Rev. Lett. 54, 1392 (1985).

 \( ^{43} \) , P. A. Fedders and D. A. Drabold, Phys. Rev. B 47, 13277 (1993).

 \( ^{44} \)  R. P. Feynman, Phys. Rev. 56, 340 (1939).

 \( ^{45} \)  D. A. Drabold, S. Nakhmanson, and X. Zhang, in Proceedings of NATO advanced study institute on Properties and applications of amorphous materials, Czech, 2001 edited by M. F. Thorpe and L. Tichy (Kluwer, London, 2001), p. 221.

 \( ^{46} \)  X. Zhang and D. A. Drabold, Phys. Rev. Lett. 83, 5042 (1999).

 \( ^{47} \)  X. Zhang and D. A. Drabold, Intl. J. Mod. Phys. 15, 3190 (2001).

 \( ^{48} \)  J. Li and D. A. Drabold, Phys. Rev. Lett. 85, 2785 (2000).

 \( ^{49} \)  P. V. Santos and W. B. Jackson, Phys. Rev. B 46, 4595 (1992).

 \( ^{50} \)  R. Atta-Fynn, P. Biswas and D. A. Drabold, Phys. Rev. B 69, 245204 (2004).

 \( ^{51} \)  M. H. Brodsky, M. Cardona, and J. J. Cuomo, Phys. Rev. B 16, 3556 (1977).

 \( ^{52} \)  G. Lucovsky, R. J. Nemanich, and J. C. Knights, Phys. Rev. B 19, 2064 (1979).

 \( ^{53} \)  W. P. Pollard and G. Lucovsky, Phys. Rev. B 26, 3172 (1982).

 \( ^{54} \)  D. A. Drabold, P. A. Fedders, O. F. Sankey, and J. D. Dow, Phys. Rev. B 42, 5135(1990).
 
