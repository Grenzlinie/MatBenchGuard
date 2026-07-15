Accepted Manuscript

Cluster formation and eventual mobility of helium in a tungsten grain boundary

C. González, R. Iglesias

![](./images/812825998830600196_1.jpg)

PII:
S0022-3115(18)30817-1

DOI:
https://doi.org/10.1016/j.jnucmat.2018.11.029

Reference:
NUMA 51319

To appear in:
_Journal of Nuclear Materials_

Received Date: 13 June 2018

Revised Date: 15 November 2018

Accepted Date: 20 November 2018

Please cite this article as: C. González, R. Iglesias, Cluster formation and eventual mobility of helium in a tungsten grain boundary, _Journal of Nuclear Materials_ (2018), doi: https://doi.org/10.1016/j.jnucmat.2018.11.029.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Cluster formation and eventual mobility of helium in a tungsten grain boundary

C. González¹, R. Iglesias²

¹ Department of Theoretical Condensed Matter Physics & Condensed Matter Physics Center (IFIMAC), Universidad Autnoma de Madrid, E-28049 Madrid, Spain.
² Departamento de Física, Universidad de Oviedo, E-33007 Oviedo, Spain

## Abstract

An exhaustive analysis based on density functional theory (DFT) simulations of the accumulation of several He atoms has been performed at the vicinity of a non-coherent W⟨110⟩/W⟨112⟩ interface. The He impurities have been placed both at interstitial positions along the grooves present at each side of the interface and inside the most stable interfacial single vacancy. At such areas, the electronic charge density is lower and the repulsion with the metallic atoms is minimized. Our results show much lower formation energies at both positions studied here as compared to the equivalent bulk cases, confirming the effective great attraction exerted on helium by this kind of interfaces. The most stable groove is completely filled before the system prefers to promote the He atoms to other alternative groove. On the other hand, the vacancy can admit at most seven He atoms, but the successive ones find the best accommodation in the surrounding sites thereafter. This result corroborates the well-known picture of vacancies as efficient sinks for He atoms in W. The binding energy estimation suggests a larger attraction between the He atoms and the vacancy. From the low values obtained at the interface and the energy barriers estimated, we can infer a decreasing mobility of the He clusters along the interface for a given temperature. This situation could favor their accumulation in the stable grooves until they are filled and the outgassing process could subsequently take place. Therefore, a tungsten system with many interfaces, the so-called nanostructured W, can be considered as a good candidate for plasma facing material in a future nuclear fusion reactor.

Keywords: Metallic interfaces, defects, formation energy, migration energy, ab-initio simulations, Density Functional Theory

Email address: roberto@uniovi.es (R. Iglesias²)

Preprint submitted to *Journal of Nuclear Materials*
November 22, 2018

### 1. INTRODUCTION

Nuclear fusion energy has been long foreseen as an environmentally clean and virtually inexhaustible energy source. A deep understanding of materials behavior in extreme environments, such as the intense irradiation and high temperature intrinsic to a future fusion reactor, is essential in order to improve the reliability, lifetime, integrity and efficiency of the structural materials building up those advanced reactors. In the aftermath of a nuclear fusion reaction, high-energy neutrons can induce a large number of defects such as vacancies or interstitial clusters and transmutation of reactor elements. Additionally, the significant interaction with plasmas can produce He bubbles and voids coupled to H impurities. All these defects can lead to volume swelling and blistering that result in embrittlement and instability of reactor components, reducing their service life [1-3] (and references therein). Hence, the ability to mitigate radiation-induced defects and control helium bubble growth is crucial to improving the radiation tolerance in nuclear materials. Furthermore, a key strategy for designing such resistant compounds consists in enhancing the efficiency of *self-healing* defect recombination processes [4-6]. Computational simulations can reduce the high costs of the hazardous experiments that should be performed under extreme conditions in order to mimic the environment envisaged within the chamber of an eventual fusion reactor. A limited number of potential materials can be selected with the theoretical calculations, accelerating the choice of more appropriate and resistant compounds [7, 8].

Materials containing a high concentration of interfaces, grain boundaries (GB) and secondary phase features promise to offer very high resistance to radiation damage accumulation [9]. Layered heterointerfaces between incoherent metallic nanosized multilayers characterised by a strong crystal structure and lattice parameter mismatch have shown an enhanced radiation performance acting as effective sinks for defect recombination at intersections between misfit dislocations [10]. Typically, fcc/bcc heterophase interfaces have been designed, even from a more general mathematical [11], elastic [12], electronic [13] or thermodynamic [18] viewpoint, with Cu or Ag as the fcc metals and refractory metals (Nb, Mo, Ta, W) as their bcc counterparts. Experimentally, multilayered Cu/Nb and Cu/W composites with nanodimensional interlayer spacing exhibit a notorious resistance to irradiation-induced damage accumulation [14-16, 20-26]. In these materials, the high mixing energy between the two components results in the rapid annealing of defects. Several theoretical works have also been recently devoted to the examination of Cu/Nb interfaces [27-30]. Only a few [31-35] were based on the Density Functional Theory (DFT) [36, 37] formalism, mostly due

to the heavy computing power load required to simulate realistic interfacial systems. Such DFT works showed that the metallic vacancies as well as the He atoms have a great tendency to find the interface in the three different cases analyzed. The calculated formation energy reveals that the most stable site for a He atom is found inside a Cu monovacancy at the three interfaces mentioned above. The analysis performed shows that helium reduces its repulsive interaction with the metallic surrounding atoms when it is occupying a vacancy at the interface, explaining the preferential accommodation found for these configurations, as suggested in a previous work [38]. Depending on the interfacial reconstruction, a He atom is able to migrate through the interface or it is trapped on the attractive (or less repulsive) sites. These results show the strong influence of the relative orientation between both metals forming the interface, allowing the selection of the most adequate interface to reduce the undesired He bubbles ultimately responsible for detrimental radiation damage in the metallic compound. Subsequently, the applicability of such analysis has been experimentally validated on Cu/W interfaces [39] promoting the attention on this system by other experimental groups [40-44].

On the other hand, the so-called nanostructured tungsten (NW), i.e., W with a great number of grain boundaries (GBs) has been proven to be a superior alternative than the standard coarse- grained tungsten (CGW) for the mitigation of radiation damage [46-50] (and references therein). The superior properties and the behaviour of defects produced by irradiation damage in bulk W have been extensively simulated in the last decade using multiscale modelling methodologies, viz. kinetic Monte Carlo (kMC), Molecular Dynamics (MD) and/or DFT (see [51] for a thorough and recent review), that in turn have been compared to experiments. Furthermore, the He and H behaviour in W/W GBs has been also studied by these methodologies [34, 52, 54, 55], evidenc- ing the great avidity of both light elements to reach the GBs. For example, DFT calculations carried out for symmetric GBs [56] and in realistic non-coherent W (110)/(112) interfaces [57] confirmed the experimental speculation that hydrogen is trapped at GBs [46]. Finally, a recent DFT-parametrised kMC-based theoretical work [47] has concluded that NW would be able to re- sist the deleterious effects of He after irradiation, definitely making it a potential plasma facing material (PFM).

In the present article, we have interpreted the stability and clustering behavior of He atoms at the W (110)/(112) interface previously created in agreement with the experimental evidence [57]. We have found that He atoms tend to be accumulated along the lines or grooves formed by the

clean open spaces in between the atomic rows of both surfaces. When a vacancy is present in the calculation, the first He atom prefers to stay at this hollow area instead of at the pure defectless interface. Approximately within this site, helium is accumulated up to a cluster of seven atoms, but the subsequent ones prefer to accommodate in positions close to the vacancy, leading to an apparent increase on the size of the cluster, that in turn could foster bubble formation. In this situation, the He atoms shall move along the interface promoting the outgassing process. In both cases, we have confirmed that helium tends to move to the regions endowed with a lower electronic density where the He-W repulsion is minimized.

## 2. METHODOLOGY.

DFT simulations were performed using the well-known plane-wave *Vienna Ab initio Simula- tion Package* (VASP) code [58]. It uses the pseudo-potential approximation following the Pro- jector Augmented Wave (PAW) methodology [59], as well as the Perdew-Burke-Ernzerhof (PBE) parametrisation of the Generalised Gradient Approximation (GGA) for the exchange and correla- tion energy functional [60]. The pseudo-potentials have been taken from the VASP code library, whereby six valence electrons have been considered for W (4 $3d$ and 2 $4s$) and two $1s$ valence electrons for He. Within these approximations, the lattice parameter of W was estimated to be $3.172$ Å for the cutoff energy of 400 eV used for the plane waves, in good agreement with the experimental room temperature result ($3.165$ Å) [61].

To the best of our knowledge, the most favorable relative orientations of the W/W interfaces have not been described experimentally, but it was established that W$\langle 110\rangle$ and W$\langle 112\rangle$ surfaces are commonly found in experiments with NW [57]. We have restricted our calculations to the particular reconstructed configuration that can be found in that reference. Using the lattice pa- rameter previously mentioned, the GB can be built. Since the two surfaces do not fit perfectly and the interface is intrinsically incoherent, the W$\langle 112\rangle$ surface had to be slightly expanded ($\sim 1$ %) in the X-direction of figure 1) when periodic boundary conditions are applied before performing the relaxation of the system.

As recently suggested [32, 35, 57], the inclusion of at least 6 layers of each surface is highly recommended to perform a correct DFT simulation of this kind of interfaces as it is shown in figure 2. The complete system contains a total of 456 W atoms, 288 and 168 in the W$\langle 110\rangle$ and W$\langle 112\rangle$ surfaces, respectively. We have started the calculations from the structure presented in [57] (see

![](./images/812825998830600196_2.jpg)

Figure 1: (color on-line) Frontal view of the W(112)/W(110) interface. The light (dark) blue spheres represent the W atoms in the (112) [(110)] surface. The interfacial atoms are represented by the larger spheres. The red-dashed rectangle corresponds to a two-dimensional view of the the supercell used in the simulations; b) Lateral view of the slab used in the simulation.

the procedure followed there in order to create the initial interface). A vacuum of $12\ \mathrm{\mathring{A}}$ separates the two free surfaces of the slab that contains the interface. Subsequently, all the structures have been fully relaxed until the forces were lower than a pre-fixed tolerance value of $0.025\ \mathrm{eV/\mathring{A}}$. The bottom layer of each surface remained fixed during the calculations in order to simulate atomic bulk positions. Due to the large size of the two-dimensional (2D) supercell, the structure was first relaxed using only the gamma point in the irreducible Brillouin zone (IBZ), as in previous works [32, 35, 57] and a cutoff energy of 400 eV. Subsequently, the calculation was refined by including 8 k-points in the IBZ following the Monkhorst-Pack scheme [62] and the recommended 479 eV for calculations involving He atoms [38] and W surfaces [63]. A slightly lower value in the cutoff energy has led to qualitative good results, see for example [64].

In order to test the stability of the GB, we can estimate the difference between the isolated surfaces and the relaxed structure obtained when they are adjoined to form the interface. This last structure is more stable by 89 eV, i.e., around $2500\ nJ/m^{2}$. We can compare this value with other configurations found in the literature. For example, Wang et al. [53] analyzed the GB $\Sigma$ 3 $\langle 110\rangle$ 111 using the same methodology while Yang and coworkers studied many other coherent sigma interfaces [65] and obtained in all the cases a lower value than the one presented here. In the former article, the authors speculated that a higher GB energy leads to an easier grain growth. From our results, it can thus be inferred that the GB presented here will show a much easier growth than the GBs analyzed in the aforementioned references, reinforcing the interest of the present analysis. Some years ago, von Alfthan *et al.* suggested a methodology to create a GB with

different numbers of vacancies with the aim of finding the most stable initial configuration [66]. Borovikov *et al.* applied such a procedure to three different W GBs and found that the interfaces free of vacancies were the most stable geometries [67]. Taking this result into consideration, our analysis has started with the pure W interface and, in a second step, an energetic study of a metallic vacancy at the GB has been performed. After that, the atomic configuration of the relaxed interface and the most stable vacancy has been fixed in order to calculate the electronic density, defined as $\rho(\mathbf{r}) = |\Psi(\mathbf{r})|^2$. This means that it has a dependence on the wave functions that appear in the Kohn-Sham equations [37].

Generally, the formation energy of a system $E_f(N_{He}n_{vac})$ containing $n_{vac}$ W vacancies and $N_{He}$ helium atoms can be easily estimated using the corresponding energies taken from the DFT simulations. Following the same recipe as in other previous systems involving interfaces, we can define it [32, 35]:

$$
E_f(N_{He}n_{vac}) = E_{Tot}(N_{He}n_{vac}) + n_{vac}E(W) - N_{He}E(He) - E_{W/W}, \tag{1}
$$

where $E_{Tot}(N_{He}n_{vac})$ is the energy obtained in the relaxation of such an interface, $E(W)$ is the energy of one W atom in the perfect bulk and $E(He)$ is the energy of one isolated He atom placed inside a large empty simulation box. Finally $E_{W/W}$ is the energy of the relaxed clean interface. In the present case, we have used only a single vacancy because a larger periodicity in the Y-direction should be required to simulate larger vacancy clusters.

Once the formation energies of all the structures have been calculated, the binding energies $(E_b)$ can be estimated following an atom-by-atom procedure. This means that the $E_b$ is calculated for a system formed when one single He atom is added to an initial structure with $N_{He}-1$ atoms. In general, the number of objects forming the mixed structure can be larger than just two defects (in our case, the initial structure and the upcoming He atom). The expression of the binding energy can be written in terms of the formation energies of the system with the $N_{def}$ objects close together and the system in which all the $i_{def}$ objects are far apart [68-71]:

$$
E_b(N_{def}) = \sum_{i_{def}=1}^{N_{def}} E_f(i_{def}) - E_f(N_{def}) \tag{2}
$$

In a final step, we have analyzed the He mobility in some selected cases. For this purpose, we have used the Nudged Elastic Band (NEB) procedure [72] as implemented in VASP. This methodology finds the path that minimizes the energetic cost for a displacement between two

![](./images/812825998830600196_3.jpg)

Figure 2: a) Lateral view of the unit cell used in the simulations (the X and Z directions have been indicated), b) differential charge distribution of the W⟨110⟩/W⟨112⟩ interface. The dark/white areas mean the lower/higher electronic charge density. A red circle shows the zone for the He1 position.

initial and final geometries by following the most favourable trajectory along the interface. Using this procedure, we can obtain the energy barrier required to jump between the two different configurations.

## 3. RESULTS.

### 3.1. He atoms at the W⟨110⟩/W⟨112⟩ interface.

The starting point of our simulations is the W⟨110⟩/W⟨112⟩ interface that has been extensively studied in a previous work [57]. The most stable position of a single H atom has been analyzed in great detail therein. Here, we follow an essentially similar procedure for the first He impurity atom in order to find its most stable site at the interface. In figure 1, the white spheres represent the different possible He positions obtained in this work after relaxation. These structures have been simulated individually for just one single He atom and in all the cases that He atom has found its preferential accommodation close to the ⟨112⟩ surface. Furthermore, He atoms tend to sit at the grooves formed in between the atomic rows of each surface. The first effect can be explained by the preference shown by helium to stay close to the areas with lower electronic charge density, as recently shown for the well-studied Kurdjumov-Sachs (KS)-Cu/Nb interface [33]. Figure 2 b) shows exactly that situation. The 2D-map shows the charge density of the full interface in a plane perpendicular to the X-direction. The dark zones correspond to the areas where the He tend to move, being the darkest one (indicated with a red circle) the He1 position of figure 2.

<table>
<thead>
  <tr>
    <th colspan="5">E<sub>f</sub>(eV)</th>
  </tr>
  <tr>
    <th></th>
    <th>Interface</th>
    <th>bulk</th>
    <th>V-interface</th>
    <th>V(bulk)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>He1</td>
    <td>3.07</td>
    <td>6.25</td>
    <td>3.33</td>
    <td>4.65</td>
  </tr>
  <tr>
    <td>He2</td>
    <td>6.08</td>
    <td>11.54</td>
    <td>5.69</td>
    <td>7.67</td>
  </tr>
  <tr>
    <td>He3</td>
    <td>9.04</td>
    <td>16.34</td>
    <td>8.21</td>
    <td>10.76</td>
  </tr>
  <tr>
    <td>He4</td>
    <td>11.90</td>
    <td>20.99</td>
    <td>10.74</td>
    <td>13.74</td>
  </tr>
  <tr>
    <td>He5</td>
    <td>14.80</td>
    <td>26.86</td>
    <td>13.09</td>
    <td>17.75</td>
  </tr>
  <tr>
    <td>He6</td>
    <td>17.65</td>
    <td>32.06</td>
    <td>15.24</td>
    <td>21.21</td>
  </tr>
  <tr>
    <td>He7</td>
    <td>20.25</td>
    <td></td>
    <td>17.85</td>
    <td>25.20</td>
  </tr>
  <tr>
    <td>He8</td>
    <td>23.41</td>
    <td></td>
    <td>20.55</td>
    <td>28.99</td>
  </tr>
  <tr>
    <td>He9</td>
    <td>26.20</td>
    <td></td>
    <td>23.17</td>
    <td>33.12</td>
  </tr>
</tbody>
</table>

Table 1: Formation energies of the most stable structures found for the different He cluster sizes at the interface and within the most stable vacancy at the interface The corresponding bulk values are shown as well for comparison.

The second effect, somehow related to the previous one, can be directly linked to the affinity of helium to move to regions of lower atomic population where the repulsive interactions among He and the metal atoms can be minimized, as we explained in a previous work [38]. The red spheres of figure 1 reflect the areas where He can find a lower electronic charge density, thereby reducing the repulsion with the metallic atoms. The numerical labels presented in figure 1 are related to the energetic ordering of each site, so that He1 denotes the most favourable location with a formation energy of 3.07 eV (see Table 1). Interestingly, the position of the He1 is close to the most stable site for a H atom previously studied [57]. Additionally, as happened with the H atom, the formation energy is much lower than the value obtained for the perfect bulk (6.15 eV [76], namely, 6.25 eV obtained by us with the same methodology [63].) This energetic reduction was already found in other interfaces composed of two elements, such as Cu/W or Cu/Nb [32, 35], and can be considered as a general manifestation of the strong attraction exerted by the interfaces and GBs on the He atoms.

Once the most stable position of the first He atom has been determined, our interest is driven to the analysis of the atomic arrangement in the entire interface in the presence of new He impurity atoms. It is expected that the second He atom could occupy the site labeled as He2 in figure 1 or an He1 equivalent position at the interface belonging to another ×1 unit cell in the Y-direction. In the latter case, this second He atom could be either far away from or as close as possible to the first

![](./images/812825998830600196_4.jpg)

Figure 3: Sketch of the migration mechanism for one He atom separating (joining) to: a) an additional He atom and b) two He atoms; c) the corresponding migration energies with respect to their corresponding more stable structures.

one. Our simulations show that He atoms tend to accumulate in clusters as the latter configuration is 0.05 meV more stable than the arrangement of the two atoms along the same atomic row but at a larger distance. Furthermore, the He2 position leads to a 0.09 meV less stable structure. This can be understood as caused by mechanical effects. The first He produces a deformation on its surrounding atomic environment at the expense of an energy cost. When the second He atom is placed at a distant location, a similar energy cost can be expected, while for a position close to the first atom that value is reduced. Additionally, we have simulated the case with two separated He atoms but a small distance, i.e., the position just before both adjoin, see the sketch in Figure 3 a). The second He has to jump an energy of 0.86 eV to meet the first one due to the strong atomic reconfiguration around the He path. The inverse process (the separation) requires a larger value, estimated in 0.92 eV (see the discussion below).

From the relaxed structures, we can easily estimate the value of the free volume. In recent works, the Voronoi concept was used [33, 34], but here we are going to define such free volume in a more intuitive way as the free open space among the eight first neighboring W atoms in the interface. We have included a sketch in figure 2 a). The volume contained in such geometrical structure is estimated to be $20.7\ \mathrm{\mathring{A}^3}$, much larger than the accessible free volume in the bulk, that is about $16.0\ \mathrm{\mathring{A}^3}$. This great difference clearly justifies the assumption that He atoms move to free areas. In fact, the value is a little bit larger when we take into account the relaxed structure, leading to a volume of $20.9\ \mathrm{\mathring{A}^3}$. Using the result for two He atoms, the accessible free volume grows

to $21.7\ \mathrm{\mathring{A}}^3$, i.e. $10.8\ \mathrm{\mathring{A}}^3$ per atom. Additionally, it is important to notice that the first He atom creates a hole in the charge density around it, favouring the approach of the subsequent atoms [33, 34].

The geometrical effect is confirmed by the inclusion of more He atoms along the same groove at the interface. The third He atom prefers to be aligned in the same row close to the already present He atoms. The formation energy of such a configuration amounts to 9.03 eV, less than three times the value for one single He atom. This third atom is placed on the following $\times1$ unit cell in the Y-direction where more free space is available with a relatively low energetic cost to produce a deformation in the lattice that affects the neighboring atoms. For this reason, the free volume analysis is not directly comparable to the previous cases. On the other hand, the formation energy grows by 0.08 eV for a distant site along the same groove and by 0.13 eV in the He2 position. We can do again a calculation to let a the third He atom join the pre-existing cluster of 2 He atoms. Now, the barrier takes a higher value than before, namely 1.10 eV, while the inverse process is slightly larger (1.14 eV). This value (together with the previous one obtained for two atoms) suggest that, even though this is the best-case scenario, only at high temperatures will He atoms coalesce to form bubbles. A more feasible procedure should be associated with a preference of He atoms to reach the interfacial deformed areas where other He atoms are already present, favouring thus bubble formation.

For the fourth atom we have only tried the position closer to the previous configuration as well as the site at the He2 position. Again, the most stable situation implies the accumulation of He atoms aligned along the selected groove: the formation energy is 11.90 eV, that is 0.33 eV lower than the latter option.

Up to this point, we consider that the quality of our results is guaranteed by the $\times4$ periodicity chosen in the Y-direction, i.e., the He atoms are located in consecutive two $\times1$ unit cells. The deformation induced on the atomic rows in the following cells in the Y-direction is in the limit of the acceptable. Consequently, additional He atoms have been placed along the same atomic row where the energy cost for the deformation of the surrounding atoms is lower than in an area free of He atoms. We can continue adding He atoms until the binding energy of the system takes on a negative value meaning that, although the structure can be stable at 0K temperature, it will certainly be unfavorable at finite temperature. In our system, this happens for 8 He atoms, implying that the $\mathrm{W}\langle 110\rangle/\mathrm{W}\langle 112\rangle$ interface accepts around two He atoms at each groove of the $\times1$

![](./images/812825998830600196_5.jpg)

Figure 4: (color on-line) Lateral view of the charge density distribution of the W⟨110⟩/W⟨112⟩ interface with the most a He atom in the most stable vacancy (indicated with a red circle). The dark/white area correspond to the lower/higher electronic charge density.

unit cell in the Y-direction. This is somehow equivalent to filling an infinite row due to the periodic boundary conditions inherent to the DFT approach. Anyway, as a relevant conclusion of these calculations, we can establish that the He atoms prefer an approximately linear distribution along a groove over the accumulation inside a ×1 unit cell or the dispersion of the atoms in different grooves. Binding energies will be discussed later in the 4 section.

### 3.2. Accumulation of He atoms inside a monovacancy.

Now our attention turns to the accumulation of He atoms in the most stable vacancy found at the W⟨110⟩/W⟨112⟩ interface. In a previous work [57], we found that such vacancy is formed at the W(112) side of the interface and far from the most stable groove (see the circle marked with a yellow cross in figure 1). Moreover, we have tested that this place corresponds to the most stable vacancy where the first He atom can be placed. As happened for the bulk, the He atom tends to occupy the empty space left by the lost W atom, i.e., the area with a lower electronic charge density as shown by figure 4. The red circle indicates the position of the vacancy and it correspond to the darkest area on the image. The formation energy takes a value of 3.33 eV, much lower than the result found for the perfect bulk, namely, 4.75 eV [38]. Surprisingly, this value is yet slightly larger than the energy obtained for the most stable groove at the interface (3.07 eV, see above). This last data is in contradiction with the results obtained for a H atom in the same vacancy on

the same GB and with other metallic interfaces, such as Cu/Nb and Cu/W (see Refs. [32], [35]), probably because, in such last cases, the most stable vacancy was at the fcc-Cu side. Interestingly, if the He atom is placed in the He1 site of figure 1, the energy is 1.05 eV larger, meaning that helium will prefer to stay within the vacancy when it is close enough to the interfacial groove analysed above.

The second He atom forms in the vicinity of the vacancy a $\langle 110 \rangle$ dumbbell-like structure with the first one (see figure 5 a)). The corresponding formation energy reaches a value of 5.69 eV, more than 0.20 eV lower than other three alternative structures tried in this work (not shown). It is important to notice that now the formation energy is lower than the value in the perfect interface, namely 6.08 eV, (and much lower than 7.67 eV in the bulk, see table 1), suggesting that He atoms will prefer to accumulate in the vacancies. This geometry is 0.69 eV more stable than the arrangement with one atom in the vacancy and the second one at the He1 site. When the third atom arrives, the three He atoms form a triangle (figure 5 b)) and the formation energy grows to 8.22 eV, this time 0.51 eV lower than the structure with 2 He atoms in the vacancy and the third at the He1 position. Similar calculations involving the addition of a growing number of He atoms have been performed. In all cases, the accumulation of helium close to the monovacancy undisputedly represents the most favorable configuration. For four, five, six and seven He atoms an internal rearrangement of the He cluster takes place (see the evolution of the most stable structures in figure 5), leading to formation energies of 10.74 eV, 13.10 eV, 15.24 eV and 17.86 eV, respectively. Again, the value grows with the number of He atoms included in the calculation. In all these configurations, we have tried three alternative structures.

The last two panels of figure 5 show the most stable geometry found for a He cluster of 8 and 9 atoms, respectively, out of the three different initial He arrangements attempted. In both cases, some of the He atoms (indicated by a red arrow) have left the volume assigned to the vacancy, or in other words, the empty space in between the site of the missing original W atom and its first nearest neighbors. Both structures are more stable than the geometries generated from the combination of the most stable 7 and 8 He atoms configurations and the addition of an extra He atom at the He1 site by 0.26 and 0.55 eV, respectively. This result has two important implications: first, seven may be defined as the maximum number of He atoms that the vacancy can accommodate and second, the growth mechanism of the He cluster seems to imply a redistribution of the newcoming atoms at the interfacial areas close to the vacancy. The figure 1 can give an explanation to this

![](./images/812825998830600196_6.jpg)

Figure 5: The most stable configurations found for the most stable monovacancy at the W(112)/W(110) interface with: a) 2, b) 3, c) 5, d) 6, e) 7, and f) 9 He atoms, respectively.

behaviour: close to the vacancy analyzed here, there are some very stable sites (labeled as He4 and He5 in the figure with a formation energy only 0.14 eV higher than He1) where the upcoming He atoms can be accommodated. As a consequence, even though the formation energy is lower at some points of the interface as compared to the vacancy site, the latter can be considered as a prominent bubble nucleation site at which the aggregation of He atoms at the interface can begin.

It is important to notice that the number of He atoms accumulated in a monovacancy in the ideal bulk was previously estimated in 9 [38]. In such case, a 5x5x5 supercell was used, while here only a x4 periodicity in the Y-direction is considered. This slight difference could lead to a potential decrease in the number of accepted He atoms because maybe the system can not accommodate the deformation. Thus, it might well be that this number could grow up to 9 with a larger unit cell, but the behavior of the successively added atoms should essentially be the same.

In apparent contradiction with our result, a recent article based on MD simulations performed for a symmetric W GB suggests that the accumulation of He atoms in a vacancy at the interface produces a trap-mutation process by removing surrounding W atoms [77]. As a consequence, the size of the vacancy increases and more He atoms can be added until another W atom is pulled out from the GB. These simulations were performed at a temperature of 1000K. We can speculate that there is a temperature dependence of the expulsion of He or W atoms from the n-vacancy. Probably, at some temperatures both processes would compete. Even there can be a dependence on the type of GB studied. For this reason, a deeper analysis of the effects of temperature on this (and many others) GB should be performed in future works in order to shed light on these ideas.

We can do an estimation of the free volume in all these cases using the same procedure previously followed for the pure interface. In the ideal bulk of a bcc structure, the empty space around a vacancy can be defined as the volume within a cube with a side equivalent to the lattice parameter. In the W case, the volume takes the value $31.9\ \mathring{A}^3$ (the real value is slightly smaller due to the atomic compression of the atoms around the hole). The free volume in the most stable vacancy in the present GB is much larger, namely $40.0\ \mathring{A}^3$ justifying the preference of the He atoms for the open spaces and the lower formation energy of the first He in the vacancy at the interface. In fact, the free volume accessible for the first He atom is lower ($39.1\ \mathring{A}^3$) than the value obtained for the atomic positions of the initial interface (before the vacancy is created). With the inclusion of more atoms, the total space available for the He atoms grows from $39.8$ to $51.0\ \mathring{A}^3$ for two and seven atoms respectively. This growth is due to the gradual displacement of the neighboring W atoms, but the effective free volume per atom is reduced from $19.9$ to $7.3\ \mathring{A}^3$. As the 8th He atom prefers to move to the interface, we can expect that the latter value will be similar regarding the reception of new He atoms in larger n-vacancies at the interface. This limit is much larger than in the bulk, namely about $4.3\ \mathring{A}^3$ (for this calculation we have used the most stable structure previously obtained [38] for 9 He atoms in a monovacancy), suggesting a great influence of the surrounding open spaces at the interface.

## 4. Discussion.

We would like to start this section summarizing some general results obtained for the formation energies. Taking into consideration the data presented in table 1, it is important to remark that all formation energies at the interface are lower than in the bulk for both the ideal defectless and monovacancy systems. The values for the ideal interface are around one half of the values for the perfect bulk. This result shows the great attraction (in fact, the lower repulsion) exerted by the interface on the He atoms. If the great mobility of the He atoms within the bulk is added to the description, we can expect that a great part of the helium inside a tungsten matrix is capable of moving at ease toward the interfaces or GBs. This result has been previously found in other different W GBs using kMC [73]. These regions would thus precisely represent outstanding initial structures that can help reducing irradiation damage in the materials of interest.

Once the first He atom arrives at the interface, our first-principles formation energy data seem to reveal a competition between the most stable vacancy and the positions surrounded by more

![](./images/812825998830600196_7.jpg)

Figure 6: Binding energy obtained via the one-by-one procedure for the cases analyzed in this work for the $N_{He^{-}}$
clusters: along the most stable groove at the interface (black squares) and in the most stable vacancy at the W(110)
surface (red circles).

open space at the perfect interface. Considering the individual calculations separately, helium
prefers to be at the so-called He1 site instead of the vacancy. As we mentioned before, this is in
contradiction with the results in other semi-coherent interfaces. Interestingly, when the vacancy
is present in the configuration, the He atom prefers to occupy the vacancy site instead of the
apparently more convenient He1 site. This means that for the He atom inside the vacancy the
global deformation is less important than when it occupies the He1 site, implying an important
reduction in the energetic cost. The successively inserted He atoms prefer to be accumulated
in the vacancy until the empty space is completely filled, when they start to be distributed in
the competitively stable (He4 and He5) sites of the interface in the vicinity of the vacancy. In
our opinion, this competitive behaviour agrees well with the picture that He will preferentially
segregate at pre-existing sites at the interface [2].

For a deeper analysis of our energetic results, we have estimated the He binding energies at the
interface with and without the monovacancy following the one-by-one procedure explained in the
section 2, i. e., adding the He atoms one by one to the system. The resulting curves can be found
in figure 6. The binding energy can be considered as a measure of the bond established between
two objects, comparing the total energy obtained for the complex when both of them are together
to the case with the objects far apart. Such situation is found by simulating each object in two
different calculations. These energies are essential for the performance and understanding of the

kMC results for much larger systems. In previous kMC simulations, researchers have used only bulk parameters in all the system assuming that the He atoms disappear when they reach a surface or a GB [47, 74]. This collection of parameters can improve the performance of such simulations.

The inclusion of the second He atom at the interface leads to a binding energy of 0.07 eV that can be compared to the value for the ideal W-bulk, namely, 1.03 eV [47]. This small value suggests that it is highly probable that one of the two He atoms may migrate through the interface, but in the previous section we showed that when both atoms are together there is a large energy barrier to split them up. Consequently, for relatively low temperatures one single atom could migrate only if it is not adjacent to the second one. We have estimated the energy barrier of such single He atom migration along the most stable interfacial groove using the NEB methodology [72]. The value is 0.35 eV (see the sketch and the barrier in figure 7), much larger than that in the bulk (0.08 eV) previously found by the authors [75] in very good agreement with the literature [64]. Again, this larger barrier at the interface than in the bulk is in contradiction with the H atom case, where the migration energy was estimated to be 0.12 eV, lower than the 0.21 eV in the bulk [57], so it seems probable that H atoms can move more easily than He atoms along this GB. Moreover, we have calculated the migration energy for both He atoms moving together. The resulting energy grows to 0.45 eV, reflecting a more complex mechanism (see the sketch in Figure 7 b)). In order to complement the analysis, we have performed a similar calculation for three He atoms and the migration energy has grown to 0.54 eV. Furthermore, the calculated energy barriers indicate that for low temperatures the He atoms will be able to move from the bulk to the interfaces, where they accumulate at their most stable grooves. For a certain temperature, the isolated He atoms will migrate through the interface and, as the temperature grows, other different mechanism can be expected. Probably, when the groove ends up completely filled (and consequently all the neighboring arrangement of W atoms has been deformed) the He atoms could move more easily and the outgassing process is favored.

The binding energies of the successively added He atoms (from three to six) slightly rise from 0.12 eV to 0.22 eV. Interestingly, the seventh atom gives rise to an important increase of the binding energy (0.48 eV), while the inclusion of the eighth atom leads to a negative value. As explained in section 3.1, the inclusion of the last atoms simulates an infinite and completely filled groove due to the limited size of our unit cell and the periodicity ($\times 4$ in the Y-direction) used in our simulations. For a more accurate calculation of the binding energy, or at least of these two

![](./images/812825998830600196_8.jpg)

Figure 7: Sketch of the migration mechanism along the most stable groove of the interface for: a) one He atom, b) two He atoms together and c) three He atoms together; d) the corresponding migration energies with respect to their corresponding more stable structures.

latter cases, a larger unit cell is required. Due to the limitations of DFT techniques when dealing with this kind of large unit cells, the MD methodology is highly recommended.

On the other hand, the binding energy of the first atom in the vacancy (0.99 eV) is much larger than at the interface, but more than four times lower than the value for the vacancy in the perfect bulk, namely, 4.67 eV [47], suggesting a higher mobility in the vacancy at the GB comparing to the almost immobility in the bulk. Subsequently, the binding energy decreases to 0.72 eV for two He atoms, while it is stabilized for three and four atoms at 0.55 eV. For the bulk vacancy a similar behaviour is observed, since the binding energy decreases to around 3.20 eV, still much larger than at the corresponding situation for the interface. While in the bulk case the binding energy maintains a decreasing trend, albeit always higher than 2.00 eV, at least up to 9 atoms, for the present interfacial vacancy the value grows back to 0.93 eV for six He atoms. Now, the binding energies oscillate between 0.59 eV and 0.26 eV from 7 to 9 He atoms. As mentioned in the previous section, from the seventh atom onwards, the additional He are distributed at the interfacial sites close to the vacancy. This result explains why the values are close to the case of the most stable groove at the interface. With these binding energies, we can expect that new atoms can be added to this cluster, and that they can migrate along the groove at the interface. We can consider this as a second highly desirable effect that can contribute positively to the He outgassing of the material.

### 5. CONCLUSIONS.

In conclusion, we have studied the accumulation of He atoms at a W⟨110⟩/W⟨112⟩ GB with and without a monovacancy using DFT techniques. We have proven the superior stability of the He atoms at the interface. Contrary to interfaces previously analysed in the literature, the He atom has a lower formation energy at the interface instead of in the vacancy. On the other hand, helium prefers the vacancy when both the most stable site and the vacancy are close enough in the interface. Succesive atoms can be accumulated at the interface with and without the vacancy. From the second He atom onwards, helium has a lower formation energy in the vacancy and for all the He-clusters examined the values are much lower than in the bulk. The He atoms tend to be aligned in the areas with no non-coincident sites for the W atoms on both surfaces, a similar behaviour as in the so-called misfit dislocation intersections of the KS-Cu/Nb interface. He atoms find a better accommodation in those open spaces until the groove is completely filled. Finally, He atoms are accumulated in the monovacancy up to a number of seven. Contrary to the bulk case, here the new He atoms are placed in sites close to the vacancy, thus increasing the cluster size. The binding energies obtained in such cases, as well as in the perfect interface, suggest that the atoms placed in the groove could migrate through the interface, favoring the outgassing process. However, the increasing barriers with the size of the He cluster indicate that probably such outgassing will be done at high temperatures or when the grooves are completely full and deformed, so that the energetic cost could be reduced. Thus, this GB will efficiently adsorb He atoms until the He atoms can move out of the interface. Taking all these features into consideration, we can conclude that this kind of GBs or interfaces in W will positively contribute to the widespread consideration of nanoestructured tungsten as an adequate material for future fusion reactors or, more generally, for high radiation-affected environments.

### Acknowledgements

This work has been funded by MINECO under the projects MAT2017-88258-R and RADIA- FUS ENE-2015-70300-C3-3-R. The authors acknowledge the computer resources provided by the Spanish Supercomputing Network (RES) (projects QCM-2017-2-0012 and QCM-2017-3-0009) re- source Caléndula based at the FCSCL, León, Spain. C.G. acknowledges financial support from the Spanish Ministry of Economy and Competitiveness, through the María de Maeztu Programme for Units of Excellence in R D (MDM-2014-0377).


The raw/processed data required to reproduce these findings cannot be shared at this time as the data also forms part of an ongoing study.

## References

[1] S. J. Zinkle and J. T. Busby, Structural materials for fission & fusion energy, Mater. Today **12** (2009) 12. DOI: 10.1016/S1369-7021(09)70294-9; S. J. Zinkle and G. S. Was, Materials challenges in nuclear energy, Acta Mater. **61** (2013) 735. DOI: 10.1016/j.actamat.2012.11.004

[2] M. R. Gilbert, S. L. Dudarev, S. Zheng, L. W. Packer, and J.-Ch. Sublet, An integrated model for materials in a fusion power plant: transmutation, gas production, and helium embrittlement under neutron irradiation, Nucl. Fusion **52** (2012) 083019. DOI: 10.1088/0029-5515/52/8/083019

[3] J. W. Coenen, M. Berger , M. J. Demkowicz , D. Matveev, A. Manhard, R. Neu, J. Riesch, B. Unterberg, M. Wirtz, and Ch. Linsmeier, Plasma-wall interaction of advanced materials, Nucl. Mater. Ene **12** (2017) 307. DOI: 10.1016/j.nme.2016.10.008

[4] G. J. Ackland, Controlling radiation damage, Science **327** (2010) 1587. DOI: 10.1126/science.1188088

[5] X.-M. Bai, A. F. Voter, R. G. Hoagland,M. Nastasi, and B. P. Uberuaga, Science **327** (2010) 1631. DOI: 10.1126/science.1183723

[6] X. Zhang, K. Hattar, Y. Chen, L. Shao, J. Li, C. Sun, K. Yu, N. Li, M. L. Taheri, H. Wang, J. Wang, and M. Nastasi, Radiation damage in nanostructured materials, Prog. Mater. Sci. **96** (2018) 217. DOI: 10.1016/j.pmatsci.2018.03.002

[7] D. M. Duffy, Fusion power: a challenge for materials science, Phil. Trans. R. Soc. A **368** (2010) 3315. DOI: 10.1098/rsta.2010.0060

[8] M. Victoria *et al.*, Modelling irradiation effects in fusion materials, Fus. Eng. Des. **82** (2007) 2413. DOI: 10.1016/j.fusengdes.2007.05.079

[9] I. J. Beyerlein, M. J. Demkowicz, A. Misra, and B. P. Uberuaga, Defect-interface interactions, Prog. Mater. Sci. **74** (2015) 125. DOI: 10.1016/j.pmatsci.2015.02.001

[10] M. J. Demkowicz, A. Misra, and A. Caro, The role of interface structure in control- ling high helium concentrations, Curr. Opin. Solid State Mater. Sci. 16 (2012) 101. DOI: 10.1016/j.cossms.2011.10.003

[11] J. Ortún-Palacios, A. M. Locci, S. Fadda, F. Delogu, and S. Cuesta-López, Role of interface in multilayered composites under irradiation: A mathematical investigation, Adv. Mater. Sci. Eng. (2017) 1079735. DOI: 10.1155/2017/1079735

[12] A. Vattre, T. Jourdan, H. Ding, M.-C. Marinica, and M. J. Demkowicz, Non-random walk diffusion enhances the sink strength of semicoherent interfaces, Nat. Commun. 7 (2016) 10424. DOI: 10.1038/ncomms10424.

[13] L. A. Zotti, S. Sanvito, and D. D. O'Regan, A simple descriptor for energetics at fcc-bcc metal interfaces, A simple descriptor for energetics at fcc-bcc metal interfaces, Mater. Des. 142 (2018) 158. DOI: 10.1016/j.matdes.2018.01.019

[14] K. Hattar, M. J. Demkowicz, A. Misra, I. M. Robertson, and R. G. Hoagland, Arrest of He bubble growth in Cu/Nb multilayer nanocomposites, Scripta Mater. 58 (2008) 541. DOI: 10.1016/j.scriptamat.2007.11.007

[15] T. Höchbauer, A. Misra, K. Hattar, and R. G. Hoagland, The influence of interfaces on the storage of ion implanted He in multilayered metallic composites, J. Appl. Phys. 98 (2005) 123516. DOI: 10.1063/1.2149168

[16] A. Misra, M. J. Demkowicz, X. Zhang, and R. G. Hoagland, Radiation damage tolerance of ultra-high strength nanolayered composites, JOM 59 (2007) 62. DOI: 10.1007/s11837-007-0120-6

[17] D. J. Chakrabarti and D.E. Laughlin, The Cu-Nb (Copper-Niobium) system, Bull. Alloy Phase Diagr. 2 (1982) 455. DOI: 10.1007/BF02876162

[18] A. M. Locci, G. Ligiosa, M. Mascia, S. Enzo, and F. Delogu, Influence of temperature on the mechanical alloying of Cu-Nb powder mixtures, Chem. Phys. Lett. 639 (2015) 23. DOI: 10.1016/j.cplett.2015.08.072

[19] K. Kolluri and M. J. Demkowicz, Dislocation mechanism of interface point defect migration, Phys. Rev. B 82 (2010) 193404. DOI: 10.1103/PhysRevB.82.193404

[20] G. Gladyszewski, J. Pacaud, P. Goudeau, C. Jaouen, A. Naudon, and J. Grilhé, Interface of the Cu-W multilayers, Vacuum **45** (1993) 285. DOI: 10.1016/0042-207X(94)90190-2

[21] C. Wang, P. Brault, C. Zaepffel, J. Thiault, A. Pineau, and T. Sauvage, Deposition and structure of W-Cu multilayer coatings by magnetron sputtering, J. Phys. D: Appl. Phys. **36** (2003) 2709. DOI: 10.1088/0022-3727/36/21/018

[22] S. P. Wen, R. L. Zong, F. Zeng, Y. Gao and F. Pan, Evaluating modulus and hard- ness enhancement in evaporated Cu/W multilayers, Acta Mater. **55** (2007) 345. DOI: 10.1016/j.actamat.2006.07.043

[23] N. Q. Vo, S. W. Chee, D. Schwen, X. Zhang, P. Bellon, and R. S. Averback, Microstructural stability of nanostructured Cu alloys during high-temperature irradiation, Scripta Mater. **63** (2010) 929. DOI: 10.1016/j.scriptamat.2010.07.009

[24] Y. Gao, T. Yang, J. Xue, S. Yan, S. Zhou, Y. Wang, D. T. K. Kwok, P. K. Chu, and Y. Zhang, Radiation tolerance of Cu/W multilayered nanocomposites, J. Nucl. Mater. **413** (2011) 11-15. DOI: 10.1016/j.jnucmat.2011.03.030

[25] M. A. Monclús, M. Karlik, M. Callisti, E. Frutos, J. LLorca, T. Polcar, and J. M. Molina- Aldareguía, Microstructure and mechanical properties of physical vapor deposited Cu/W nanoscale multilayers: Influence of layer thickness and temperature, Thin Solid Films **571** (2014) 275. DOI: http://dx.doi.org/10.1016/j.tsf.2014.05.044

[26] K. Tai, R. S. Averback, P. Bellon, N. Vo, Y. Ashkenazy, and S. J. Dillon, Orientation relation- ship formed during irradiation induced precipitation of W in Cu, J. Nucl. Mater. **454** (2014) 126. DOI: 10.1016/j.jnucmat.2014.07.054

[27] M. J. Demkowicz, J. Wang and R. G. Hoagland, *Interfaces Between Dissimilar Crystalline Solids*, in *Dislocation in Solids, Volume 14: A Tribute to F. R. N. Nabarro*, ed. J. P. Hirth. Elsevier B. V. 2008.

[28] A. Kashinath and M. J. Demkowicz, A predictive interatomic potential for He in Cu and Nb, Model. Simul. Mater. Sci. Eng **19** (2011) 035007. DOI: 10.1088/0965-0393/19/3/035007

[29] A. Kashinath, A. Misra, and M. J. Demkowicz, Stable storage of Helium in nanoscale platelets at semicoherent interfaces, Phys. Rev. Lett. 110 (2013) 086101. DOI: 10.1103/Phys-RevLett.110.086101

[30] A. Y. Dunn, M. G. McPhie, L. Capolungo, E. Martínez, and M. Cherkaoui, Helium bubble formation and retention in Cu-Nb nanocomposites, J. Nucl. Mater. 435 (2013) 141. DOI: 10.1016/j.jnucmat.2012.12.041

[31] E. Metsanurk, A. Tamm, A. Caro, A. Aabloo, and M. Klintenberg, First-principles study of point defects at a semicoherent interface, Sci. Rep. 4 (2014) 7567. DOI: 10.1038/srep07567

[32] C. González, R. Iglesias, and M. J. Demkowicz, Point defect stability in a semicoherent metallic interface, Phys. Rev B 91 (2015) 064103. DOI: 10.1103/PhysRevB.91.064103

[33] U. Saikia, M. B. Sahariah, C. González, and R. Pandey, Vacancy assisted He-interstitial clustering and their elemental interaction at fcc-bcc semicoherent metallic interface, Sci. Rep. (2018) 8:3844. DOI:10.1038/s41598-018-22141-y

[34] W.-H. He, X. Gao, D. Wang, N. Gao, M.-H. Cui, L.-L. Pang, and Z.-G. Wang, First-principles investigation of grain boundary morphology effects on helium solutions in tungsten, Comp. Mater. Sci. 148 (2018) 224. DOI: 10.1016/j.commatsci.2018.02.044

[35] C. González, and R. Iglesias, Energetic analysis of He and monovacancies in Cu/W metallic interfaces, Mater. Des. 91 (2016) 171. DOI: 10.1016/j.matdes.2015.11.097

[36] P. Hohenberg and W. Kohn, Inhomogeneous Electron Gas, Phys. Rev. 136 (1964) B864 DOI: 10.1103/PhysRev.136.B864

[37] W. Kohn and L. J. Sham, Self-Consistent Equations Including Exchange and Correlation Effects, Phys. Rev. 140 (1965) A1133 DOI: 10.1103/PhysRev.140.A1133

[38] C. González, M. A. Cerdeira, S. L. Palacios, and R. Iglesias, Reduction of the repulsive interaction as origin of helium trapping inside a monovacancy in BCC metals, J. Mat. Sci. 50 (2015) 3727. DOI: 10.1007/s10853-015-8935-y

[39] M. Callisti, M. Karlik, and T. Polcar, Bubbles formation in helium ion irradiated Cu/W multilayer nanocomposites: Effects on structure and mechanical properties, J. Nucl. Mater. 473 (2016) 18. DOI: 10.1016/j.jnucmat.2016.02.006

[40] A. v. Müller, D. Ewert, A. Galatanu, M. Milwich, R. Neu, J. Y. Pastor, U. Siefken, E. Tejado, and J. H. You, Melt infiltrated tungsten?copper composites as advanced heat sink materials for plasma facing components of future nuclear fusion devices, Fusion Eng. Des. 124 (2017) 455. DOI: 10.1016/j.fusengdes.2017.01.042

[41] E. Tejado, A. v. Müller, J.-H. You, and J. Y. Pastor, The thermo-mechanical behaviour of W-Cu metal matrix composites for fusion heat sink applications: The influence of the Cu content, J. Nucl. Mater. (2017). DOI: 10.1016/j.jnucmat.2017.08.020

[42] L. R. Brandt, E. Salvati, C. Papadaki, H. Zhang, S. Ying, E. Le Bourhis, I. Dolbnya, T. Sui, and A. M. Korsunsky, Probing the deformation and fracture properties of Cu/W nanomul- tilayers by in situ SEM and synchrotron XRD strain microscopy, Surf. Coat. Technol. **320** (2017) 158. DOI: 10.1016/j.surfcoat.2017.01.065

[43] L. M. Garrison, Y. Katoh, L. L. Snead, T. S. Byun, J. Reiser, and M. Rieth, Irradia- tion effects in tungsten-copper laminate composite, J. Nucl. Mater. **481** (2016) 134. DOI: 10.1016/j.jnucmat.2016.09.020

[44] X. Zhang, J. A. Beach, M. Wang, P. Bellon, and R. S. Averback, Precipitation kinetics of dilute Cu-W alloys during low-temperature ion irradiation, Acta Meter. 120 (2016) 46. DOI: 10.1016/j.actamat.2016.08.043

[45] G. Ackland, Controlling Radiation Damage, Science. **327** 1587-1588 (2010). doi:10.1126/science.1188088

[46] R. González-Arrabal, M. Panizo-Laiz, N. Gordillo, E. Tejado, F. Munnik, A. Rivera, and J. M. Perlado, Hydrogen accumulation in nanostructured as compared to the coarse-grained tungsten, J. Nucl. Mater. 453 (2014) 287. DOI: 10.1016/j.jnucmat.2014.06.057

[47] G. Valles, C. González, I. Martin-Bragado, R. Iglesias, J. M. Perlado, and A. Rivera, The influence of high grain boundary density on helium retention in tungsten, J. Nucl. Mater. 457 (2015) 80. DOI: 10.1016/j.jnucmat.2014.10.038

[48] G. Valles, M. Panizo-Laiz, C. González, I. Martin-Bragado, R. González-Arrabal, N. Gordillo, R. Iglesias, C. L. Guerrero, J. M. Perlado, A. Rivera, Influence of grain boundaries on the

radiation-induced defects and hydrogen in nanostructured and coarse-grained tungsten, Acta Mater. 122 (2017) 277. DOI: 10.1016/j.actamat.2016.10.007

[49] Z. Chen, L.-L. Niu, Z. Wang, L. Tian, L. Kecskes, K. Zhu, and Q. Wei, A comparative study on the in situ helium irradiation behavior of tungsten: Coarse grain vs. nanocrystalline grain, Acta Mater. 147 (2018) 100. DOI: 10.1016/j.actamat.2018.01.015

[50] V. A. Ksenofontov, T. I. Mazilova, E. V. Sadanov, O. V. Dudka, A. A. Mazilov, I. V. Starchenko, and I. M. Mikhailovskij, Helium induced reduction of the grain-boundary ten- sile strength in tungsten, J. Nucl. Ene. Sci. Power Generat. Technol. 3 (2014) 2. DOI: 10.4172/2325-9809.1000120

[51] J. Marian, C. S. Becquart, C. Domain, S. L. Dudarev, M. R. Gilbert, R. J. Kurtz, D. R. Mason, K. Nordlund, A. E. Sand, L. L. Snead, T. Suzudo, and B. D. Wirth, Recent advances in modeling and simulation of the exposure and response of tungsten to fusion energy conditions, Nucl. Fusion 57 (2017) 092008. DOI: 10.1088/1741-4326/aa5e8d

[52] F. Sefta, K. D. Hammond, N. Juslin, and B. D. Wirth, Tungsten surface evolution by helium bubble nucleation, growth and rupture, Nucl. Fusion 53 (2013) 073015, DOI: 10.1088/0029-5515/53/7/073015; L. Hu, K. D. Hammond, B. D. Wirth, and D. Maroudas, Interactions of mobile helium clusters with surfaces and grain boundaries of plasma-exposed tungsten, J. Appl. Phys.115 (2014) 173512, DOI: 10.1063/1.4874675; Z. Chen, L. J. Kecskes, K. Zhu, and Q. Wei,Atomistic simulations of the effect of embedded hydrogen and helium on the tensile properties of monocrystalline and nanocrystalline tungsten, J. Nucl. Mater. 481 (2016) 190, DOI: 10.1016/j.jnucmat.2016.09.024

[53] X.-X. Wang, L.-L. Niu, and S. Wang, Strong trapping and slow diffusion of helium in a tungsten grain boundary, J. Nucl. Mater. 487 (2017) 158, DOI: 10.1016/j.jnucmat.2017.02.010

[54] G. Nandipati, W. Setyawan, H. L. Heinisch, K. J. Roche, R. J. Kurtz, and B. D. Wirth, Displacement cascades and defect annealing in tungsten, Part II: Object kinetic Monte Carlo simulation of tungsten cascade aging, J. Nucl. Mater. 462 (2015) 338, DOI: 10.1016/j.jnucmat.2014.09.067; A. M. Ito, A. Takayama, Y. Oda, T. Tamura, R. Kobayashi, T. Hattori, S. Ogata, N. Ohno, S. Kajita, M. Yajima, Y. Noiri, Y. Yoshimoto, S. Saito, S. Takamura, T. Murashima, M. Miyamoto, and H. Nakamura, Molecular dynamics and Monte

Carlo hybrid simulation for fuzzy tungsten nanostructure formation, Nucl. Fusion **55** (2015) 073013, DOI: 10.1088/0029-5515/55/7/073013; T. Oda, D. Zhu, and Y. Watanabe, Kinetic Monte Carlo simulation on influence of vacancy on hydrogen diffusivity in tungsten, J. Nucl. Mater. **467** (2015) 439, DOI: 10.1016/j.jnucmat.2015.07.054

[55] H.-B. Zhou, Y.-L. Liu, Y. Zhang, S. Jin, and G.-H. Lu, First-principles investigation of energet- ics and site preference of He in a W grain boundary, Nucl. Instrum. Meth. B **267** (2009) 3189, DOI: 10.1016/j.nimb.2009.06.067; H.-B. Zhou, Y.-L. Liu, S. Jin, Y. Zhang, G.-N. Luo, and G.-H. Lu, Towards suppressing H blistering by investigating the physical origin of the H?He interaction in W, Nucl. Fusion **50** (2010) 115010, DOI: 10.1088/0029-5515/50/11/115010

[56] H.-B. Zhou, Y.-L. Liu, S. Jin, Y. Zhang, G.-N. Luo, and G.-H. Lu, Investigating behaviours of hydrogen in a tungsten grain boundary by first principles: from dissolution and diffusion to a trapping mechanism, Nucl. Fusion **50** (2010) 025016. DOI: 10.1088/0029-5515/50/2/025016

[57] C. González, M. Panizo-Laiz, N. Gordillo, C. L. Guerrero, E. Tejado, F. Munnik, P. Pi- aggi, E. Bringa, R. Iglesias, J. M. Perlado, and R. Gonzlez-Arrabal, H trapping and mobility in nanostructured tungsten grain boundaries: A combined experimental and theoretical ap- proach, Nucl. Fusion **55** (2015) 113009. DOI: 10.1088/0029-5515/55/11/113009

[58] G. Kresse and J. Hafner, *Ab initio* molecular dynamics for liquid metals, Phys. Rev. B **47** (1993) R558 DOI: 10.1103/PhysRevB.47.558; G. Kresse and J. J. Furthmuller, Efficient iter- ative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B **54** (1996) 11169 DOI: 10.1103/PhysRevB.54.11169; G. Kresse and D. Joubert, From ul- trasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B **59** (1999) 1758. DOI: 10.1103/PhysRevB.59.1758

[59] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B **50** (1994) 17953. DOI: 10.1103/PhysRevB.50.17953

[60] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. **77** (1996) 3865. DOI: 10.1103/PhysRevLett.77.3865

[61] A. M. James and M. P. Lord, *Macmillan's Chemical and Physical Data*, Macmillan, London, UK (1992) http://www.webelements.com/.


[62] M. J. Monkhorst and J. D. Pack, Special kpoints for Brilloiun zone integrations, Phys. Rev. B **13** (1976) 5188

[63] C. L. Guerrero, N. Gordillo, R. Iglesias, J. M. Perlado, and C. González, Ab initio study of tungsten defects near the surface, Modelling Simul. Mater. Sci. Eng. 24 (2016) 045006. DOI: 10.1088/0965-0393/24/4/045006

[64] C. S. Becquart, and C. Domain, Migration Energy of He in W Revisited by Ab Initio Calcu- lations, Phys. Rev. Lett. **97** (2006) 196402. DOI: 10.1103/PhysRevLett.97.196402

[65] Z. Yang, L. Hu, D. Maroudas, and K. D. Hammond, Helium segregation and transport be- havior near ¡100¿ and ¡110¿ symmetric tilt grain boundaries in tungsten, J. Appl. Phys. **123** (2018) 225104. DOI: 10.1063/1.5026617; Z. Yang and K. D. Hammond, Helium in-plane mi- gration behavior on ¡100¿ symmetric tilt grain boundaries in tungsten, J. Phys.: Condens. Matter **30** (2018) 325002. DOI: 10.1088/1361-648X/aad0bc

[66] S. von Alfthan, P. D. Haynes, K. Kaski and A. P. Sutton, Phys. Rev. Lett. **96** (2006) 055505

[67] V. Borovikov, X.-Z. Tang, D. Perez, X.-M. Bai, B. P. Uberuaga, and A. F. Voter, Coupled motion of grain boundaries in bcc tungsten as a possible radiation-damage healing mechanism under fusion reactor conditions, Nucl. Fusion **53** (2013) 063001

[68] C. S. Becquart and C. Domain, An object Kinetic Monte Carlo Simulation of the dynamics of helium and point defects in tungsten, J. Nucl. Mater. **385** (2009) 223-227

[69] T. P. C. Klaver, D. J. Hepburn, and G. J. Ackland, Defect and solute properties in dilute Fe-Cr-Ni austenitic alloys from first principles, Phys. Rev. B **85** (2012) 174111

[70] N. Juslin and B. D. Wirth, Interatomic potentials for simulation of He bubble formation in W, J. Nucl. Mater. **432**, (2013) 61-66

[71] C. González, D. Fernández-Pello, M. A. Cerdeira, S. L. Palacios, and R. Iglesias, Helium bubble clustering in copper from first principles, Model. Simul. Mater. Sci. Eng. **22** (2014) 035019. DOI: 10.1088/0965-0393/22/3/035019

[72] H. Jonsson, G. Mills and K. W. Jacobsen, *Nudged Elastic Band Method for Finding Mini- mum Energy Paths of Transitions*, in *Classical and Quantum Dynamics in Condensed Phase Simulations*, ed. B. J. Berne, G. Ciccotti and D. F. Coker. World Scientific, (1998).

[73] E. Martínez, B. P. Uberuaga, and B. D. Wirth, Atomistic modeling of helium segregation to grain boundaries in tungsten and its effect on de-cohesion, Nucl. Fusion 57, 086044 (2017)

[74] C. S. Becquart and C. Domain, An object Kinetic Monte Carlo Simulation of the dy- namics of helium and point defects in tungsten, J. Nucl. Mater. 385 (2009) 223. DOI: 10.1016/j.jnucmat.2008.11.027; C. S. Becquart, C. Domain, U. Sarkar, A. DeBacker, and M. Hou, Microstructural evolution of irradiated tungsten: Ab initio parameterisation of an OKMC model, J. Nucl. Mater. 403 (2010) 75. DOI: 10.1016/j.jnucmat.2010.06.003

[75] C. González and R. Iglesias, Migration mechanisms of helium in copper and tungsten, J. Mater. Sci. 49 (2014) 8127. DOI: 10.1007/s10853-014-8522-7

[76] T. Seletskaia, Y. Osetsky, R. E. Stoller, and G. M. Stocks, First-principles theory of the energetics of He defects in bcc transition metals, Phys. Rev. B 78, (2008) 134103. DOI:10.1103/PhysRevB.78.134103

[77] X. Y. Liu, B. P. Uberuaga, D. Perez, and A. F. Voter, New helium bubble growthmode at a symmetric grain-boundary in tungsten: accelerated molecular dynamics study, Mat. Res. Lett. 6, (2018) 522-530. DOI: 10.1080/21663831.2018.1494637