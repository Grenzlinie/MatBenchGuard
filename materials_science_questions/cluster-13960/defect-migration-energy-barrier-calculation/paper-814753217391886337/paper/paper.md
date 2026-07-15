Accepted Manuscript

Vacancy migration energy dependence on local chemical environment in Fe-Cr alloys: a *Density Functional Theory* study

D. Costa, G. Adjanor, C.S. Becquart, P. Olsson, C. Domain

<table>
  <tr>
    <td>PII:</td>
    <td>S0022-3115(14)00274-8</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.jnucmat.2014.05.007</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>NUMA 48132</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>*Journal of Nuclear Materials*</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>31 May 2013</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>3 May 2014</td>
  </tr>
</table>

![](./images/814753217391886337_1.jpg)

Please cite this article as: D. Costa, G. Adjanor, C.S. Becquart, P. Olsson, C. Domain, Vacancy migration energy dependence on local chemical environment in Fe-Cr alloys: a *Density Functional Theory* study, *Journal of Nuclear Materials* (2014), doi: http://dx.doi.org/10.1016/j.jnucmat.2014.05.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Vacancy migration energy dependence on local chemical environment in Fe-Cr alloys: a *Density Functional Theory* study

D. Costa $^{\text{a,b,c}}$, G. Adjanor $^{\text{b,c}}$, C. S. Becquart $^{\text{a,c}}$, P. Olsson $^{\text{c,d,e}}$, and C. Domain $^{\text{a,b,c}}$

$^{\text{a}}$ Unité Matériaux et Transformations, CNRS UMR8207, Université de Lille 1, F-59655 Villeneuve d'Ascq Cédex, France.

$^{\text{b}}$ EDF-R&D Département MMC, Les Renardières, F-77818 Moret sur Loing Cédex, France.

$^{\text{c}}$ Laboratoire commun (EDF–CNRS): Etude et Modélisation des Microstructures pour le Vieillissement des Matériaux (EM2VM).

$^{\text{d}}$ KTH-Royal Institute of Technology, Stockholm

Corresponding author:
Dr. Davide Costa
Université Lille 1 - Sciences et Technologies – UMET (Unité Matériaux Et Transformations)
Phone number : +33685595429
Email : davide.costa.ge@gmail.com

The first step towards the understanding and the modelling of the Fe-Cr alloy kinetic properties consists in estimating the migration energies related to the processes that drive the microstructure evolution. The vacancy migration barrier is expected to depend on the vacancy-migrating atom pair atomic environment as pointed out by Nguyen-Manh *et al.* or Bonny *et al.* In this paper, we address the issue of the dependence on the vacancy local atomic environment of both the vacancy migration energy and the configurational energy change $\Delta$E that occurs when the vacancy jumps towards one of its nearest neighbour sites. A DFT approach is used to determine the ground state energy associated to a given configuration of the system. The results are interpreted in the light of the chromium-chromium and chromium-vacancy binding energies as well as the substitutional chromium atoms magnetic properties.

## 1. Introduction

Several efforts, both on a theoretical and experimental point of view, have been recently made in order to achieve a better understanding of Fe-Cr alloys thermodynamic and kinetic properties, especially in the context of chromium-rich stainless steels for nuclear industry applications [1,2]. High chromium ferritic/martensitic steels are candidates for structural materials in future generation nuclear fission reactors (generation IV) and fusion reactors because of their swelling

resistance under irradiation and their low ductile to brittle transition temperature shift due to irradiation [3-5]. The chromium content in iron-based alloys for which the ductile to brittle transition temperature shift reaches its minimum value is 9 at. % [2] while a better resistance to oxidation requires higher chromium concentration. In the case of oxide dispersion strengthened steels - which are designed to improve the strength of high temperature (above 800 K) steels – the chromium concentration can reach 14 at. % [6]. Measurements show the existence of a miscibility gap in iron-chromium ferritic phase for temperatures lower than 900 K and chromium concentrations between 5 and 15 at. % [7]; in particular, recent small angle neutron scattering measurements suggest that the solubility limit of chromium in iron is 9 at. % at 573 K [8]; thus, up to this temperature, for chromium concentrations higher than 9 at. %, the ferritic Fe-Cr alloy undergoes a phase separation leading to the formation of chromium-rich $\alpha'$-phase regions. The existence of the Fe-Cr miscibility gap in the conditions presented above is due to the change of sign of Fe-Cr mixing enthalpy which is negative for chromium concentration lower than 6-9at. % and positive for higher chromium content, as has been shown by Olsson *et al.* [9,10] by *Density Functional Theory* (DFT) calculations at 0 K. Below this chromium concentration the Fe-Cr solid solution is stable: experimental data [11] and theoretical predictions [12,13] show short range order arrangement in ferritic phase of low chromium concentration Fe-Cr alloy. When the chromium content is higher than 9 at. %, chromium precipitation occurs by means of two possible mechanisms: nucleation and growth is observed [14,15] for chromium concentrations between 9 and 20 at.% while spinodal decomposition is observed [17-22] for chromium concentration above 20 at.%. Both in the case of the nucleation-growth mechanism and for spinodal decomposition, chromium precipitation leads to the degradation of the mechanical properties of the alloy (*i.e.* to hardening) because of the interaction between dislocations and precipitates [16,23]. At the atomic scale, the formation of chromium precipitates is achieved by the system *via* the microstructure evolution driven by vacancy diffusion; the rate of the microstructure evolution can be enhanced by the exposition of the alloy to relatively high temperatures and/or to irradiation [9]. The study of the consequences of thermal ageing and irradiation on the mechanical properties of Fe-Cr alloys is a major issue for the development of generation IV structural materials and stainless steel components in current generation nuclear power plants. Since thermal ageing experiments are time-expensive, a reliable computer simulation approach, able to describe the Fe-Cr microstructure evolution, represents a fundamental predictive tool. The first step towards understanding and modelling the alloy kinetic properties consists in computing the activation energies related to the processes which drive the microstructure evolution. In this work the vacancy diffusion *via* a vacancy-atom exchange (*i.e.* the migration of an atom towards an unoccupied site among its eight nearest neighbours) will be considered as the main process leading to the Fe-Cr microstructure evolution. Radiation damage on the alloy will not be taken into account and we will thus focus on the vacancy migration using electronic structure calculations and more precisely the DFT.

From the point of view of magnetism, the iron-chromium system is rather complex. Pure iron exhibits a ferromagnetic configuration below its Curie temperature (1043 K). Pure chromium has very peculiar magnetic properties: its magnetic ground state consists in a spin density wave arrangement [33-36], above its Néel temperature (311 K) the transition towards the paramagnetic state occurs. DFT calculations provide an anti-ferromagnetic ordering for pure chromium ground state [36]. According to Klaver *et al.* DFT calculations [37], isolated chromium atoms in an iron

matrix orient their local magnetic moment (LMM) antiferromagnetically with respect to surrounding iron atoms. When the nearest neighbour sites of a chromium atom are progressively occupied with chromium atoms, the competition between pure chromium magnetic ground state [36] and the tendency of chromium atoms' LMM to orient anti-ferromagnetically with respect to iron atoms rises. As a consequence, a frustrated magnetic configuration appears and the chromium atoms LMM absolute value decreases.

Our main objective consists in achieving a better understanding of the influence of the local atomic environment (LAE). An investigation of the vacancy migration energy dependence on the LAE in Fe-Cr alloys has been proposed by Nguyen-Manh *et al.* [40,44] and by Bonny *et al.* [45]. Nguyen-Manh *et al.* used a DFT approach, while Bonny *et al.* exploited a many-body Fe-Cr potential based on the embedded atom method [46] as cohesive model. Nevertheless, both these studies only considered the effect of the chromium content in the local (1st shell) environment of the migrating atom saddle point position, thus neglecting the effects due to the different positions that the chromium atoms can occupy within the saddle point local environment. In this work, we will consider the effect of the first and the second nearest neighbour sites of the migrating atom initial and final position on the vacancy migration energy. Furthermore we will analyse the influence that the specific position of the chromium atoms in the vacancy local environment has on the vacancy migration energy. Some simple arguments based on magnetic frustration have been used by Klaver *et al.* to explain the change of sign of Fe-Cr mixing enthalpy [37], on the other hand the DFT computed chromium-chromium and chromium-vacancy interactions have been found to be, respectively, repulsive and attractive by Olsson *et al.* [31]. In what follows it will be shown that such considerations provide rather simple interpretation of the atom-vacancy migration barrier dependence on the LAE. In this work, we investigate, using a DFT approach, the influence of the local environment on the vacancy migration energy and on the changes in the total energy of the system. Electronic structure calculations in the framework of DFT have been performed in order to relax all different structures which have been considered and to compute vacancy-atom migration energies with the NEB method [38]. One of the main advantages of DFT calculations which must be always balanced with the considerable computational resources they require - is the fact that the magnetic properties of the system can be taken explicitly into account. This is an essential aspect because the magnetic contribution to the cohesive energy has a very strong influence on Fe-Cr alloy properties and, as it will be shown, particularly in the vacancy migration processes.

In a first step, we examine how the vacancy migration energy and the total energy of the system evolve while progressively filling the neighbouring shells of the migrating atom with Cr atoms.
We then evaluate the respective influence of the different shells on the migration energy by introducing one atom at various locations neighbouring the moving atom trajectory. Finally we investigate the specific effect of the chromium content in the saddle point local atomic environment on the vacancy migration energy.

## 2. Computational details

All the calculations have been performed in the framework of DFT [24,25] using the Vienna Ab initio Simulation Package (VASP) [26] implemented with the projector augmented wave method in the general gradient approximation (PAW-GGA) [27,28] with the Perdew and Wang parameterization (PW91) for the exchange correlation energy functional [29]. 250 atoms bcc supercells $(5a_0×5a_0×5a_0)$ have been considered. We used the theoretical equilibrium pure iron lattice parameter ($a_0$=2.831 Å) [31]. For all the calculations the cut-off energy has been set to 300 eV. The Brillouin zone sampling is achieved via the Monkhorst-Pack scheme [30] with a mesh of $2 × 2 × 2$ k-points. Both the cut-off energy and the k-point mesh have been chosen in order to guarantee the energy convergence within 15 meV for the migration barriers.

All calculations are spin-polarized and the Vosko *et al.* correction on the interpolation of the correlation energy [32] has been systematically taken into account. The LMM are introduced following an Ising model so that the only degrees of freedom associated to each magnetic moment are its absolute value and its sign, while the direction is fixed. The iron matrix has been initially placed in its ground state ferromagnetic configuration with LMM of $2.1\ \mu_B$. As it has been sketched out in the introductive section, the chromium magnetic ground state is quite complex: neutron diffraction experiments indicate the pure chromium ground state magnetic ordering as being a spin-density wave [33,34], but DFT calculations in PAW-GGA framework fail to capture this aspect [35,36] and indicate an anti-ferromagnetic ordering for the pure chromium ground state. Nevertheless, it should be noticed that the energy difference between spin-density wave ordering and anti-ferromagnetic ordering is very small [36]. In this work chromium atoms are introduced in the system by replacing iron atoms. In some configurations they form small clusters whose magnetic properties generally deviate from bulk chromium since they are the consequences of frustration effects. Following Klaver *et al.* DFT calculations [37] isolated chromium atoms initial LMM have been oriented anti-ferromagnetically with respect to matrix iron atoms. When two or more chromium atoms are close to each other in the matrix, their LMM are oriented ferromagnetically if they are 2nn and anti-ferromagnetically if they are 1nn.The initial absolute value of the chromium magnetic moment which has been considered here is $0.6\ \mu_B$. The LMM in a relaxed structure have been calculated by integrating the electron density in the volume of a sphere centred on each atom and with radius equal to the Wigner radius corresponding to the atom type (1.323 Å for chromium and 1.302 Å for iron).

To compute the minimum energy path for the vacancy-atom jump we used the NEB approach [38] implemented by relaxing all configurations in DFT framework. It should be noted that, since the LMM are introduced via an Ising model, the migration energy obtained through the NEB approach represents an upper limit with respect to the case where the LMM are considered as three-dimensional vectors (Heisenberg model). The climbing Image (CI) algorithm has been systematically employed to find the saddle point energy [39]. The CI algorithm forces one of the images introduced along the migration path during a NEB run to be located on the saddle point of the migration barrier profile. The CI technique takes place after the NEB procedure convergence; it consists in identifying the higher energy image, to switch off the elastic interactions between images, and to relax this image again under the action of the force derived from the potential energy surface with opposite sign. A test has been made do determine the optimal number of images to be introduced along the vacancy migration path to compute the migration barrier profile. We performed the test on an asymmetric double-hump barrier. Not significant differences has been observed in saddle point energy estimations obtained introducing 11 to 5 images

(including the vacancy initial and final position), thus the latter numerically more efficient option has been chosen for all calculations which follow.

In order to introduce a nomenclature to identify the different configurations of the vacancy-migrating atom LAE we considered the different windows that the line joining the initial and the final position of the migrating atom goes through. Such windows are represented by the B, C, D, and E sites. B sites will be referred to as the initial position window, C and D sites as the saddle point position windows and E sites as the final position window (the atomic sites nomenclature is schematised in figure 1).

![](./images/814753217391886337_2.jpg)

Fig. 1 Local chemical environment structure scheme and sites nomenclature.
AT: migrating atom
V: vacancy
Black spheres: atom windows the vacancy goes through along migration path (first window: C1, C2, C3. Second window: D1, D2, D3).

### 3. Results

#### 3.1. Migration barriers dependence on the chromium content in $1^{st}$ and $2^{nd}$ nearest neighbour sites of the migrating atom

In order to study the influence of the closest local chemical environment on the vacancy migration barrier, we computed the iron-vacancy and chromium-vacancy migration energies using the NEB-CI approach in DFT for different chromium contents in the first and the second nearest neighbour shells of the migrating atom and vacancy. The different LAE configurations have been obtained

by progressively filling sites A, B1, B2, B3, C1, C2, C3, D1, D2, D3, E1, E2, E3, F, G1, G2, G3, H1, H2, H3 with chromium atoms (see figure 1 for details on the atomic sites nomenclature).

Figure 2 also represents for each configuration the $\Delta E$, where $\Delta E$ is the difference in energy between the final and the initial configuration. Indeed there exist a certain number of models used to estimate the vacancy migration energy in the case of atomistic Kinetic Monte Carlo simulations which rely on a simple relationship between the migration energy and $\Delta E$ [21,22,43].

![](./images/814753217391886337_3.jpg)

Fig. 2 Iron-vacancy migration energy for increasing chromium content in first and second nearest neighbour sites of initial and final position of migrating atom. a) The migrating atom is an Fe atom, b) the migrating atom is a Cr atom.

The results presented in Figure 2 indicate that the Iron vacancy migration energy decreases from 0.64 eV to 0.3 eV when the chromium concentration around the migrating atom initial positions increases. This fact is probably due to the chromium-vacancy attractive interaction. Olsson *et al.* DFT calculations [31] show that the chromium interaction with a vacancy is attractive and equal

to 0.057 eV and 0.014 if chromium and vacancy are first or second nearest neighbours respectively.

When sites A, B1, B2, B3, C1, C2, C3 are completely filled with chromium atoms (7 Cr in figure 2 horizontal axis), the iron vacancy migration barrier jumps from 0.3 eV to 0.5 eV. Then it stays constant with increasing Cr content until all the nearest neighbours of the migrating atom and vacancy are occupied with chromium atoms. When the second nearest neighbours (G and H sites) start to be occupied with chromium atoms, the iron-vacancy migration energy shows a slowly increasing tendency. The increase of iron migration energy occurring when the last nearest neighbour site of iron initial position (C3) is occupied by a chromium atom (7 Cr in figure 2 horizontal axis) probably has a magnetic origin.

In the case where the migrating atom is chromium, an increase (from 0.2 eV to 0.8 eV) of chromium migration energy can be observed when the C sites – which are first nearest neighbours of the migrating chromium initial position - are progressively filled with chromium atoms. A further increase (from 0.6 eV to 1 eV) of the chromium migration energy occurs when the G sites are occupied (15 to 17 Cr in figure 2b), one by one, by chromium atoms. This effect could be connected to the fact that, while the chromium content increases around the migrating chromium atom, the migration energy tends to get closer to that in bulk chromium (1.04 eV). Finally the chromium-vacancy migration energy decreases (from 1 eV to 0.7 eV) while the H sites (18 to 20 Cr in figure 2b) are progressively occupied.

The results in figure 2 indicate that the migration barriers do depend on the Cr content in the neighbourhood of the migrating atom as could be expected. This dependence is more pronounced when the migrating atom is Cr as the changes in the barriers are larger.

The other interesting point to notice is that the trend observed in the migration energies follows the trends in the $\Delta E$. The migration energy is given by the difference between the energy of the system when the migrating atom is at saddle point and the energy of the system when the migrating atom is at its initial equilibrium position. In principle, there is no trivial relation between the value of the migration energy and $\Delta E$ for a given configuration of the LAE. Our calculations, however, show that such a relation seems to exists, at least for the configurations presented in figure 2.

Because of the magnetic properties of Fe and Cr, the Fe-Cr system behaviour is probably driven by magnetism. For each configuration, the average of the neighbouring atoms LMM (figure 3 for migrating iron and figure 4 for migrating chromium) and the migrating atom LMM (figure 5 for migrating iron and figure 6 for migrating chromium) has been computed for its initial position, saddle point and final position.

First of all it should be noted that, regardless of the migrating atom type and the chromium content in LAE, the average LMM of the iron atoms in the super-cell (excluding the migrating atom) remains constant ($\sim$2.2 $\mu_B$) while the average LMM of chromium atoms in the super-cell varies between -2 $\mu_B$ and -0.4 $\mu_B$ (see figure 3 and figure 4). Globally, the chromium magnetic moments tend to orient anti-ferromagnetically with respect to the iron matrix magnetic moments. The fact that the absolute value of the chromium LMM decreases with the increasing chromium content in the migrating atom LAE is due to the rise of frustrated magnetic configurations for chromium atoms. This effect has been explained by Klaver *et al.* [37]. Observing the reduction of the absolute value of the neighbouring chromium average LMM (figure 3 and figure 4), one can notice that it occurs by means of a tree step variation. This happens because magnetic frustration

rises as a shell of chromium is added to a previous existing chromium shell: when sites A, B and C are occupied by chromium atoms, no magnetic frustration occurs; when the D, E and F sites are progressively filled with chromium atoms, magnetic frustration appears. Finally, it becomes more pronounced when the G and H sites are filled with chromium. Looking at the variation of the migrating iron initial position magnetic moment with the chromium content in its nearest neighbour shell (figure 5 horizontal axis), one can observe that, it becomes anti-parallel (-1.5 $\mu_B$) with respect to the matrix, when sites A, B1, B2, B3, C1, C2 are filled with chromium (6 Cr in figure 5). At the saddle point its LMM is positive. This spin flip for the migrating iron, occurring along the path to the saddle point, should require an increase of the activation energy of the process but this effect can be observed only when site C3 is occupied by a chromium atom. The spin flip effect described above occurs between the saddle point and final position of the migrating iron when sites A, B1, B2, B3, C1, C2, C3, D1, D2, D3, E1, E2 are all filled with chromium atoms (12 Cr in figure 5 horizontal axis) and disappears when the first nearest neighbour shell of the final position is saturated with chromium atoms (14 Cr in figure 5 horizontal axis).

![](./images/814753217391886337_4.jpg)

Fig. 3 Average magnetic moments of neighbouring iron and chromium atoms for the three different positions of a migrating iron atom (initial position, final position, saddle point position) and for different content of chromium in first and second nearest neighbour of the vacancy- migrating atom pair. The error bars correspond to the standard deviation.

![](./images/814753217391886337_5.jpg)

Fig. 4 Average magnetic moments of neighbouring iron and chromium atoms for the three different positions of a migrating chromium atom (initial position, final position, saddle point position) and for different content of chromium in first and second nearest neighbour of the vacancy- migrating atom pair. The error bars correspond to the standard deviation.

![](./images/814753217391886337_6.jpg)

Fig. 5 Magnetic moments of a migrating iron atom in three different positions (initial position, final position, saddle point position) and for different content of chromium in first and second nearest neighbour of the vacancy-migrating atom pair. The error bars correspond to the standard deviation.

![](./images/814753217391886337_7.jpg)

Fig. 6 Magnetic moments of a migrating chromium atom in three different positions (initial position, final position, saddle point position) and for different content of chromium in first and second nearest neighbour of the vacancy-migrating atom pair. The error bars correspond to the standard deviation.

The sign of the migrating chromium LMM changes (from positive to negative) during the vacancy's jump when the chromium content in the first nearest neighbours shell passes from 4 to 7 Cr (figure 6). As figure 6 shows, the difference between the migrating chromium final and initial LMM increases during the filling of the A, B and C sites with chromium atoms (1 to 7 Cr in figure 2 b)), this fact should produce a monotonic increase of chromium-vacancy migration energy in the same region whereas, observing figure 2 b), one realizes that when sites A, B1, B2, B3 (from 1 Cr to 4 Cr in figure 2 b) horizontal axis) are progressively occupied with chromium atoms, the chromium-vacancy migration energy stays almost constant. This can be explained by considering the coexistence of two competitive effects: on the one hand, the chromium-vacancy exchange requires more and more energy to be realized because of the LMM variation of the migrating atom during the jump, on the other hand the chromium-chromium repulsive interaction [31] lowers the migration barrier when sites A, B1, B2, B3 are filled with chromium atoms (from 1 to 4 Cr in figure 2 b)) because the neighbouring chromium atoms tend to push away the migrating chromium. These two opposite effects result in a weak variation of chromium-vacancy migration barrier during the filling of sites A, B1, B2, B3. Figure 6 shows the general tendency of quenching of the migrating chromium LMM with the increase of chromium content in the local environment. This, we believe, is related to the attempt of the system to minimize configuration energy excess due to the frustration phenomena.

3.2. Migration barriers dependence on the position of the chromium atoms along the migrating path

In order to better understand the influence on the vacancy-atom migration barriers of chromium atoms position among the LAE sites, the chromium-vacancy and iron-vacancy migration energy has been computed for different configurations with one chromium atom in the LAE.

![](./images/814753217391886337_8.jpg)

Fig. 7 Vacancy migration energy and difference ($\Delta$E) between final (after the migration) and initial (before the migration) energy of the system for different positions of one chromium atom within first nearest neighbour sites of initial and final position of migrating atom. a) the migrating atom is an Fe atom b) the migrating atom is a Cr atom.

Figure 7 indicates that, as already observed in figure 2, the changes in the barrier are more pronounced when the migrating atom is a Cr atom. Indeed, the iron-vacancy migration energy and the $\Delta$E depend very weakly on the presence of one chromium atom in local environment whereas the chromium-vacancy migration is sensible to the presence and, in particular, to the relative position of the chromium atom. This fact can be easily explained as the consequence of the repulsive interaction existing between chromium atoms. Indeed the binding energy between 2 chromium atoms is –0.24 eV when the two Cr atoms are $1^{st}$ nearest neighbours and –0.12 eV when they are $2^{nd}$ nearest neighbour. In our scheme, a negative binding energy indicates repulsion.

According to our results, the chromium-chromium repulsive interaction can either produce a rise of chromium migration energy or a reduction of chromium migration energy depending on the positions of the environmental chromium atoms. If a chromium atom is placed in site A or in site B1, the chromium-vacancy migration barrier is lower than in the cases sites C1, D1, E1 or F are occupied. This is due to the fact that in the first cases the chromium-chromium repulsive force facilitates the jump of the migrating chromium towards the vacancy while in the latter cases chromium-chromium repulsive force represents an obstacle to the migrating chromium.

The activation barrier is also larger when the Cr atom is situated in the neighbourhood of the saddle point (C and D windows) or of the final position (E and F sites). In fact, the maximum

value of the atom-vacancy migration energy results from the presence of a chromium atom in D site (this fact is much more visible in the case the migrating atom is chromium).

The dependence of $\Delta$E on LAE is related not only on Cr-Cr binding energy but also on Cr-V binding energy. According to our DFT calculations, the latter is equal to 0.05 eV when the chromium and the vacancy are $1^{st}$ nearest neighbour and 0.01 eV when they are $2^{nd}$ nearest neighbours. We remind that, in our picture, a negative binding energy indicates a repulsive interaction while a positive corresponds to an attractive interaction. When the migrating atom is iron, the main aspect contributing to $\Delta$E is the interaction of the vacancy with chromium atoms belonging to LAE. The gain or the loss of stability for the system, which follows a vacancy-atom exchange, depends on the variation of the number of chromium atoms which are first or second nearest neighbours of the vacancy. Chromium-vacancy interaction is attractive, then the system becomes more stable when the chromium occupancy of the sites surrounding the vacancy increases and vice versa. Since the chromium-vacancy interaction is weak, this effect is quite small, as it can be seen in figure 7 a) for the migrating iron. When the migrating atom is chromium, the chromium-chromium distances can also change during the atom-vacancy exchange. Because of its magnitude as compared to chromium-vacancy interaction, the chromium-chromium interaction plays a major role in the variation of the energy of the system. Chromium-chromium repulsion is strong and considerably dependent on chromium-chromium distance, as a consequence the $\Delta$E can be very large and strongly affected by the LAE. The increase or the decrease of the distance between the migrating chromium and the chromium atoms occupying the sites of the LAE lead, respectively, to the increase or the decrease of the stability of the system (see in figure 7 b).

### 3.3. Influence of the saddle point and the final configuration environment

Figure 8 represents the evolution of the migration energy and the changes in total energy of the system when filling progressively the "saddle point windows" and the final configuration sites.
Figure 2 and 8 indicate that the chromium content of nearest neighbours sites of the migrating atom saddle point position (sites C1, C2, C3, D1, D2, and D3) has a notable influence on the variation of the migration energies, this can be noticed especially in the case the migrating atom is chromium for which the progressive filling sites C1, C2, C3 corresponds to a monotonic growth of vacancy-atom migration energy. This point was previously observed by Nguyen Manh [40,41] who investigated a few specific configurations. In order to study in a more precise way the influence of the neighbouring Cr atoms on the vacancy migration energy, we investigated all the possible configurations of the saddle point environment using our DFT-NEB-CI approach.


![](./images/814753217391886337_9.jpg)

Figure 8 clearly shows that the filling of windows C and D and sites E has a strong impact on $\Delta \mathbf{E}$. The more Cr atoms in the C window, the lower the final configuration, whereas the more Cr atoms in the D and E sites the higher the final configuration. The fact that the trends are not as pronounced for the activation barrier, in particular for the E sites demonstrate the delicate balance between the contribution of the final and initial configuration and that of the local environment of the saddle point to the activation barrier.

![](./images/814753217391886337_10.jpg)

Fig. 9 Vacancy migration energy for different positions of three chromium atoms in the saddle point and the final configuration sites. a) The migrating atom is an Fe atom b) the migrating atom is a Cr atom

Figure 9 confirms the results obtained previously as it indicates that the largest migration barriers are obtained when filling the D window with Cr atoms.

### 4. Discussion

The calculations of the iron-vacancy and chromium-vacancy migration energies show that the migration barriers exhibit a clear dependence on saddle point nearest neighbours shell chemical environment. In particular the most remarkable effect - can be summarized as follows: when sites D1 D2 D3 are occupied by chromium atoms the vacancy migration energy is always higher than in the other cases. This tendency can be observed also for each configuration for which chromium occupancy of D sites is higher than chromium occupancy of C sites and is stronger when the migrating atom is chromium. The latter observation, in the extreme case corresponding to a complete chromium filling of the D sites and a complete iron filling of C sites, can be explained with a magnetic interaction argument: chromium atoms in sites D are second nearest neighbours of the migrating chromium while the latter is at its initial position, when the migrating chromium joins the final position D sites became its nearest neighbours. This means that the migrating chromium at its initial position can orient its LMM in a parallel way with respect to the other

chromium atoms in the structure (placed in sites D1, D2, and D3) and in anti-parallel way with respect to the iron atoms in the structure, in accordance with the tendency of chromium atoms to orient their LMM in ferromagnetic configuration with respect to second neighbouring chromium and in anti-ferromagnetic configuration with respect to iron environmental atoms (Klaver *et al.* [37]); the migrating chromium at its final position will tend to orient its LMM in order to create an anti-ferromagnetic compound with chromium atoms in D1, D2, D3 (now first nearest neighbours) and, at the same time, it will tend to orient its LMM in anti-ferromagnetic configuration with respect to the iron atoms in the matrix. This competition between two orientation states of the migrating chromium magnetic moment in its final position leads to a frustrated configuration with higher energy with respect to the initial one. Figure 10 represents a scheme of the mechanism described above. In order to better illustrate this phenomenon, the chromium-vacancy migration energy in an environment characterized by the chromium occupancy of sites D1, D2, and D3 (all other matrix sites occupied by iron atoms) has been computed with the DFT-NEB-CI approach; for each image the migrating chromium LMM has been calculated: figure 11 displays the variation of migrating chromium LMM along the migration path (left hand side) and the migration barrier energy profile (right hand side). The left hand side of figure 11 clearly shows that the migrating chromium LMM undergoes a spin-flip.

![](./images/814753217391886337_11.jpg)

Fig. 10 Migrating chromium magnetic moment before (left side) and after (right side) the jump when sites D1, D2, D3 (see figure 1) are occupied with chromium atoms.

![](./images/814753217391886337_12.jpg)

Fig. 11 Migrating chromium LMM (left) and migration barrier profile (right). Sites D1, D2, D3 (see figure 1) are occupied by chromium atoms while all other sites in the supercell are occupied by iron atoms.

A more general explanation of the increasing of atom-vacancy migration barrier consequently to higher chromium occupancy of D sites with respect to chromium occupancy of C sites can be formulated as follows.

1) In the case the migrating atom is chromium, a higher chromium occupancy of D sites with respect to chromium occupancy of C sites (being all other matrix sites occupied by iron atoms) will mean that the migrating chromium, at its final position, will have a larger number of chromium atoms within its nearest neighbours than at its initial position; this implies the final configuration energy will be higher than initial configuration energy due to chromium-chromium repulsive interaction [31].

2) In the case the migrating atom is iron, a higher chromium occupancy of D sites with respect to chromium occupancy of C sites (all other matrix sites occupied by iron atoms) will mean that the vacancy, at its final position, will have a lower number of chromium atoms within its nearest neighbour than at its initial position; this implies the final configuration energy will be higher than initial configuration energy due to chromium-vacancy attractive interaction [31].

Finally, regarding the connection between the migration barrier and the changes in the total energy, $\Delta E$, figure 12 indicates that there is indeed a correlation. However the dispersion also indicates that the activation energy depends also on the local environment at the saddle point as shown previously and most of the data points which lie far away from the "tendency line" can be understood by a careful examination of the saddle point window. Our results indicate thus that a model of the migration barrier for the vacancy migration in an FeCr system has to take into account not only the total energies of the system and more precisely how it changes because of the vacancy jump but also a description of the saddle point chemistry and in particular the number of Cr atoms in the saddle point environment.

![](./images/814753217391886337_13.jpg)

Fig. 12 Migration barrier as a function of the change in the total energy configuration ($\Delta$E). a) the migrating atom is an Fe atom, b) the migrating atom is a Cr atom. a) The square of the correlation coefficient is $\mathrm{R}^{2}=0.6393$, b) The square of the correlation coefficient is $\mathrm{R}^{2}=0.4176$.

In the context of the simulation of the Fe-Cr thermal ageing via an atomistic kinetic Monte Carlo (AKMC) approach [12,21,22,40,47,48], a very popular choice for computing the energy required for a vacancy-atom exchange consists in introducing the so called Final Initial State Energy (FISE) approximation, according to the terminology adopted by Vincent et al. [42] in the context of Fe-Cu alloys. The FISE approximation is based on the Kang and Weinberg decomposition of migration energy barriers [43].

The approximation introduced by Kang and Weinberg consists in computing the vacancy migration energy as follows:

$$E_{m i g}^{A T-V}=E_{m i g 0}^{A T-V}+\frac{\Delta E}{2} \tag{1}$$

where $E_{m i g 0}^{A T-V}$ depends on the migrating atom type but not on the chemical environment and, in most of the FISE-based parameterisations of the AKMC simulations of the iron based alloys which can be found in the literature, is simply the atom-vacancy exchange energy computed in a pure iron matrix. All the effects of the environment on the migration barrier are then carried by the $\Delta E$ term. This simple model could be improved by introducing a dependence of the $E_{m i g 0}^{A T-V}$ term on the local atomic environment. In particular, an explicit dependence of $E_{m i g}^{A T-V}$ on the migrating atom saddle point local atomic environment - whose effect on the vacancy migration energy is particularly strong - could be easily introduced. For example, $E_{m i g 0}^{A T-V}$ could be expressed as depending on the chromium content in the saddle point local atomic environment or even explicitly on the saddle point local environment configuration, thus accounting, not only for the chromium content, but also for the position of chromium atoms in the saddle point local atomic environment [49].

5. Conclusions

Some aspects of the local chemical environment influence on the vacancy-atom exchange in Fe-Cr alloy have been investigated with a *Density Functional Theory* approach.

All along this study we exploited very simple arguments based on magnetic interaction or chromium-chromium and chromium-vacancy interaction to provide a physically consistent explanation about the LAE dependence of the vacancy migration barrier in a Fe-Cr alloy. As we have pointed in section 3, most of the results can be understood as resulting from a balance between two effects. On the one hand, the chromium-chromium and the chromium-vacancy interactions, on the other hand, the change - induced by the vacancy migration - of the chromium atoms LMM. Both this aspects contribute to the vacancy migration energy dependence on the LAE. While the influence of migrating atom and vacancy first nearest neighbour shell chemical configuration is quite well understood, the role of second nearest neighbour shell is still not clear. We can't provide an explanation for the evolution of atom-vacancy migration barriers (both in the case of migrating iron and migrating chromium) when second nearest neighbour sites are progressively filled with chromium atoms (figures 2 a and 2 b from 15Cr to 21Cr on horizontal axis). The particular influence the saddle point local ($1^{st}$ nearest neighbours shell) chemical environment has on vacancy-atom migration energy has been characterized (section 3.3) and related to chromium-chromium and chromium-vacancy interactions (section 4). Finally, a possible way to improve the FISE approximation for computing the vacancy migration energy as a function of local atomic environment has been presented.

### 6. Acknowledgements

This work is part of the research program of the EDF-CNRS joint laboratory EM2VM (Study and Modelling of the Microstructure for Ageing of Materials).

It has been supported by the European Commission FP7 project GETMAT under grant agreement number 212175.

### References

[1] L. Malerba, A. Caro, J. Wallenius, J. Nucl. Mater. 382 (2008) 112.

[2] D. Terentyev, G. Bonny, N. Castin, C. Domain, L. Malerba, P. Olsson, V. Moloddstov, R. C. Pasianot, J. Nucl. Mater. 409 (2011) 167.

[3] E. A. Little and D. A. Stow, J. Nucl. Mater. 87 (1979) 25.

[4] D. S. Gelles, J. Nucl. Mater. 108 (1982) 515.

[5] F. A. Garner, M.B. Toloczko, B. H. Sencer, J. Nucl. Mater. 276 (2000) 123.

[6] M. A. Auger, T. Leguey, A. Muñoz, M. A. Monge, V. de Castro, P. Fernández, G. Garcés, R. Pareja, J. Nucl. Mater. 417 (2011) 213.

[7] G. Bonny, D. Terentyev and L. Malerba, Scripta Mater. 59 (2008) 1193.

[8] F. Bergner, A. Ulbricht and C. Heintze, Scripta Mater. 61 (2009) 1060.

[9] P. Olsson, I. A. Abrikosov, J. Wallenius, Phys. Rev. B 73 (2006) 104416.

[10] P. Olsson, I. A. Abrikosov, L. Vitos, J. Wallenius, J. Nucl. Mater. 321 (2003) 84.

[11] I. Mirebeau, M. Hennion, G. Parette, Phys. Rev. Lett. 53 (1984) 687.

[12] C. Pareige, C. Domain, P. Olsson, J. App. Phys. 106 (2009) 1.

[13] P. Erhart, A. Caro, M. Serrano de Caro, B. Sadigh, Phys. Rev. B 77 (2008) 134206.

[14] C. Heintze, F. Bergner, A. Ulbricht, H. Eckerlebe, J. Nucl. Mater. 409 (2011) 106.

[15] S. Novy, P. Pareige, C. Pareige, J. Nuc. Mater. 384 (2009) 96.

[16] G. Bonny, D. Terentyev, L. Malerba, J. Nucl. Mater. 385 (2009) 278.

[17] T. Ujihara and K. Osamura, Acta Mater. 48 (2000) 1629.

[18] M. K. Miller, J. M. Hyde, M. G. Hetherington, A. Cerezo, G. D. W. Smith, C. M. Elliot, Acta Metall. 43 (1995) 3385.

[19] J. M. Hyde, M. K. Miller, M. G. Hetherington, A. Cerezo, G. D. W. Smith, C. M. Elliot, Acta Metall. 43 (1995) 3403.

[20] J. M. Hyde, M. K. Miller, M. G. Hetherington, A. Cerezo, G. D. W. Smith, C. M. Elliot, Acta Metall. 43 (1995) 3415.

[21] J. Wallenius, P. Olsson, L. Malerba, D. Terentyev, Nucl. Instrum. Meth. B 255 (2007) 68.

[22] C. Pareige, M. Roussel, S. Novy, V. Kuksenko, P. Olsson, C. Domain, P. Pareige, Acta Mater. 59 (2011) 2404.

[23] O. Soriano-Vargas, E. O. Avila-Davila, V. M. Lopez-Hirata, N. Cayetano-Castro, J. L. Gonzalez-Velazquez, Mat. Sci. Eng. A-Struct. 527 (2010) 2910.

[24] P. Hohenberg, W. Kohn, Phys. Rev. B 136 (1964) 864.

[25] W. Kohn, L. J. Sham, Phys. Rev. A 140 (1965) 1133.

[26] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.

[27] P. E. Blöchl, Phys. Rev. B 50 (1994) 17953.

[28] P. E. Blöchl, Clemens J. Först, Johannes Schimpl, B. Mater. Sci. 26 (2003) 33.

[29] J. P. Perdew, Y. Wang, Phys. Rev. B 45 (1992) 13244.

[30] H. J. Monkhorst, J. D. Pack, Phys. Rev. B 13 (1976) 5188.

[31] P. Olsson, C. Domain, J. Wallenius, Phys. Rev. B 75 (2007) 014110.

[32] S. H. Vosko, L. Wilk, M. Nusair, Can. J. Phys. 58 (1980) 1200.

[33] L. M. Corliss, J. M. Hastings, R. J. Weiss, Phys. Rev. Lett. 3 (1959) 211.

[34] E. Fawcett, Rev. Mod. Phys. 60 (1988) 209.

[35] R. Soulariol, Chu-Chun Fu, C. Barreteau, J. Phys.: Condens. Matter 22 (2010) 1.

[36] R. Hafner, D. Spišák, R. Lorenz, J. Hafner, J. Phys.: Condens. Matter 13 (2001) 239.

[37] T. P. C. Klaver, R. Drautz, M. W. Finnis, Phys. Rev. B 74 (2006) 094435.

[38] H. Jonsson, G. Mills, K. W. Jacobsen, Classical and Quantum Dynamics in Condensed Phase Simulation, Ed. B. J. Berne, G. Ciccotti and D. F. Coker (World Scientific, 1998) 385.

[39] G. Henkelman, B. P. Uberuaga, H. Jonsson, J. Chem. Phys. 113 (2000) 9901.

[40] D. Nguyen-Manh, M. Yu. Lavrentiev, S. L. Dudarev, C. R. Phys. 9 (2008) 379.

[41] D. Nguyen-Manh, M. Yu Lavrentiev, S. L. Dudarev, J. Nucl. Mater. 386 (2009) 60.

[42] E. Vincent, C. S. Becquart, C. Pareige, P. Pareige, C. Domain, J. Nucl. Mater. 373 (2008) 387.

[43] H. C. Kang and A. H. Weinberg, J. Chem. Phys. 90 (1989) 2824.

[44] D. Nguyen-Manh, M. Yu. Lavrentiev, S. L. Dudarev, J. Nucl. Mater. 386 (2009) 60.

[45] G. Bonny, R.C. Pasianot, D. Terentyev, L. Malerba, *Interatomic Potential to Simulate Radiation Damage in Fe-Cr Alloys*, Open Report SCK-CEN-BLG-1077 (2011).

[46] G. Bonny, R.C. Pasianot, D. Terentyev, L. Malerba, Phil. Mag. 91 (2011) 1724.

[47] G. Bonny, D. Terentyev, L. Malerba, D. Van Neck, Phys. Rev. B 79 (2009) 10407.

[48] D. Nguyen-Manh, M. Yu. Lavrentiev, S. L. Dudarev, Comput. Mater. Sci. 44 (2008) 1.

[49] D. Costa *et al.* To be published.