![](./images/812683556378640385_1.jpg)

Subscriber access provided by GRIFFITH UNIVERSITY

Article

# Direct atomic simulations of facet formation
and equilibrium shapes of SiC nanoparticles

Henrik Andersen Sveinsson, Anders Hafreager, Rajiv K. Kalia,
Aiichiro Nakano, Priya Vashishta, and Anders Malthe-Sorenssen

*Cryst. Growth Des.*, **Just Accepted Manuscript** • DOI: 10.1021/acs.cgd.9b00612 • Publication Date (Web): 30 Jan 2020
Downloaded from pubs.acs.org on February 15, 2020

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W.,
Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Direct atomic simulations of facet formation and equilibrium shapes of SiC nanoparticles

Henrik Andersen Sveinsson, $^\dagger$ Anders Hafreager, $^\dagger$ Rajiv K. Kalia, $^\ddagger$ Aiichiro Nakano, $^\ddagger$ Priya Vashishta, $^\ddagger$ and Anders Malthe-Sørenssen$^{*, \dagger}$

$^\dagger$The Njord Centre, Department of Physics, University of Oslo, Sem Sælands vei 24, NO-0316, Oslo, Norway
$^\ddagger$Collaboratory for Advanced Computing and Simulations, University of Southern California, Los Angeles, CA 90089-0241, USA

E-mail: malthe@fys.uio.no

## Abstract
Understanding the shapes of nanoparticles is an important interdisciplinary problem because particle shapes can affect their properties, functionality and applications. Advances in nanoscale imaging probes have revealed exquisite details of nano-faceting phenomena. However, quantitative theoretical predictions have not kept up pace with experimental advances, and the atomic pathways of facet formation are largely unknown due to a lack of direct observations and simulations. Here we examine facet formation in spherical and cubic SiC nanoparticles and in SiC nanowires using molecular dynamics simulations reaching microseconds. We characterize layer-by-layer formation, diffusional motion along edges and corners, and determine energy barriers. We find that the equilibrium shapes are identical regardless of the initial shape of SiC nanoparticles or nanowires. For spherical and cubic nanoparticles, (110) facets form within 10 ns by lateral liquid-like diffusion of atoms. In contrast, faceting in SiC nanowires also involves normal diffusional motion with a higher energy barrier and hence much longer faceting times. These results have important implications for molecular-level understanding of the synthesis and stability of ceramic nanocrystals and nanowires.

## Introduction
Ceramic nanocrystals such as SiC are widely used in electronics, $^{1}$ photonics, $^{2}$ biosensors, drug delivery$^{3,4}$ and in structural applications. $^{5}$ Silicon carbide is attractive due to its high mechanical strength. Accordingly, mechanisms and transitions during mechanical loading of silicon carbide have been studied in experiments$^{6,7}$ and molecular simulations. $^{8-11}$ On the nanoscale, the shape of crystals directly affect their propeties.$^{12-15}$ Despite advances in nanoscale imaging$^{16-20}$ and modeling, the detailed atomic mechanisms of nanocrystal formation has not been directly observed in experiments or simulation.$^{16,21,22}$ The transformation of a crystalline particle from any initial shape to its equilibrium crystal shape involves a series of complex processes.$^{23-26}$ The final equilibrium shape has facets resulting from the minimization of surface free energy for a given volume.$^{27}$ The equilibrium shape of a nanocrystal is uniquely determined by the Wulff construction$^{28}$ according to the surface free energy associated with all crystal directions, resulting in certain planes being preferred. For instance, the expected equilibrium shape for a crystal with (110) planes having the lowest surface energy is a rhombic dodecahedron, possibly truncated by other facets if they have sufficiently low surface energy to intersect at the edges or

corners. At finite temperature, a facet can grow either in the lateral or normal direction via the formation of steps and kinks. The latter results from the diffusion of adatoms from edges and corners. $^{29}$ The edges and corners between facets can become rounded, but the dominant facetsremain intact. $^{30}$

The formation of a fully-grown step or layer may require multiple events to occur, and in- volve energy barriers that prevent the par- ticle from reaching its equilibrium shape if the surface area of the facet is sufficiently large. $^{31,32}$ In the absence of step-producing de fects, Mullins $^{32}$ has shown that the nucleation energy for growing layers on a facet is pro- hibitively large and the particle may become ki- netically immobilized if the facet is larger thana nanometer. Kinetic Monte Carlo simulationshave revealed a similar nucleation barrier. $^{33}$  However, the detailed atomic mechanisms of facet formation in nanocrystals have not yet been observed experimentally or computation- ally with a model where all atomistic mecha- nisms are available. In this article, we show that facet formation on a ceramic, silicon carbide, can be obtained in direct molecular dynamics simulations, and study the detailed mechanisms involved in the faceting process.

## Results and Discussion

Here we examine how spherical, cubic and cylindrical silicon carbide nanoparticles in vacuum undergoing volume-preserving shape changes reach the same equilibrium shape by different dynamical mechanisms, crossing sig- nificantly different energy barriers over time scales varying by three orders of magnitude. Figure 1 shows how a (110) facet forms in an SiC particle that was initially a sphere of diam- eter 8 nm. Figure 1(a) shows the onset of facet formation in the spherical SiC nanoparticle at $T=2200$ K after 0.02 ns. The different colors indicate the layer depth: atoms in the first five layers from the top are colored blue, red, yellow, purple and green. In the early stages, Si andC atoms diffuse in these layers to expose (110) facets. The diffusion coefficients for Si and C atoms in the early stages of facet formation are close to $7 ×10^{-6} cm^{2} / s$ and $1.0 ×10^{-5} cm^{2} / s$ , respectively. Figures 1(d) and (e) indicate thatthe participation of the topmost layer (green) in the facet growth ceases after a short durationof less than 10 ns. The snapshot in Fig. 1(b) shows partial formation of a (110) facet after139 ns. Atoms in the second layer (purple)participate in the facet growth for another 125 ns and subsequently their participation tails off to zero after 265 ns. These atoms are mostly in the central part of the facet, and they are surrounded by atoms in the third layer. Atoms in the bottom two layers (red and blue) partici- pate in the edges between facets. The snapshot in Fig. 1(c) shows a fully grown (110) facet after 400 ns. Atoms in the bottom two layers(blue and red) continue to diffuse, mostly at the edges and corners of the facet, even after the facet growth stops. The participation of atoms from the bottom three layers remains nearly constant over the entire duration of the facet formation, see Fig. 1(e). After 400 ns, the SiC nanoparticle is transformed from a sphere to faceted nanocrystal with twelve (110) and eight (111) facets. These are all the (110) and(111) facets that combinatorics on the miller indices allow for, and it is a different set of facets than those appearing for example in sim- ulations of platinum nanoparticles, $^{34}$ which has(111) and (100) facets. According to the Wulff construction, this means that these substances have different ratios of surface energies between their (100), (110), (111) crystal surfaces. Be- tween the facets on the n-SiC, there are edges and corners along which surface Si and C diffusewith diffusion constants around $3.1(2) ×10^{-6}$  $cm^{2} / s$ and $4.4(3) ×10^{-6} cm^{2} / s$ , respectively.

To examine the effect of the initial nanocrys- tal shape, we also simulated a cubic nanocrys-tal with length 8 nm and faces in the (001) directions, and a cylindrical nanocrystal of di-ameter 4 nm and length 8 nm along the [011] crystal direction. These were also performed at $T=2200$ K. The particle shapes are nearlyidentical for the sphere and the cube after 1 μs, but the cylindrical particle differs. Figure2 shows the initial shapes (a-c), final shapes(d-f) and the fraction of the surface area be-

![](./images/812683556378640385_2.jpg)

Figure 1: Faceting of silicon carbide nanoparticles. (a-c) Snapshots of silicon carbide nanoparticle (n-SiC) with diameter 8 nm faceting during a molecular dynamics simulation. (a) Initial configuration taken at 0.02 ns, (b) partly faceted particle after 139 ns and (c) fully faceted particle after 400 ns. In (b) and (c) we see (110) facets, and also island-like (111) facets. In the final configuration, the mean distance from the center of the particle to the (110) planes is 3.73 nm and to the (111) plane 3.90 nm, which by Wulff construction gives the ratio of surface energies $E_{110}/E_{111}=0.956$, and that the equilibrium shape is a rhombic dodecahedron truncated by a regular octahedron. Colours in (a-c) indicate layer depth on one of the (110) facets, and correspond to the colours in (d-e). (d) scatters the height distribution of particles in the 5 top layers of the crystal through time, and shows that the interplay between rows on the facet is important in the faceting process. (e) shows the numbers of particles in each layer of the coloured facet through time, and guides the interpretation of (d). (d-e) Only shows the number of atoms in the crystal layers on the facet indicated by colors in (a-c), and thus, even though the number of atoms of the particle as a whole is conserved, the number of atoms in (e) is not conserved.

ing (110) or (111) facets (g) for the sphere, the cube and the cylinder. Just like the sphere, the cube transforms into a nanocrystal with twelve (110) and eight (111) facets. In Figure 2(g) we use the facet area fraction as an indication of the facet formation. We observe that this fraction stabilizes in $0.1\ \mu\text{s}$ for the cube and $0.6\ \mu\text{s}$ for the sphere. The cylindrical nanoparticle also develops (110) and (111) facets, and its facet area fraction stabilizes after $0.3\ \mu\text{s}$, but the shape of this nanoparticle is different from the other ones even after $1\ \mu\text{s}$. Note that the faceting times are not directly comparable since the nanoparticles have different volumes.

![](./images/812683556378640385_3.jpg)

Figure 2: Effects of changing the initial shape of n-SiC. A spherical particle (a) and a cubic particle (b) facets to the same shape (d-e), during simulation at 2200 K. A cylindrical particle (c) does not reach the same shape, and is locked into a metastable shape (f). (g) shows the evolution of the sum of the (110) and (111) facet area through time, and shows that all particles have reached a steady state during the simulation time.

To investigate the faceting of the cylindrical nanocrystal in more detail, we plot the distance between opposing (110) planes. This, along with snapshots of the particle at various stages of the facet formation is shown in Figure 3. We again observe the initial faceting phase of $0.3\ \mu\text{s}$. During this time, pairs of facets inclined with respect to the major axis move closer to each other, reaching approximately the same value (5.5 nm) after $0.1\ \mu\text{s}$. The planes normal to the major axis converge to a higher separation distance (6.3 nm) after $0.3\ \mu\text{s}$. However, the distance between the facet pair parallel to the major axis remains constant through $1\ \mu\text{s}$ at 2200 K. These are the largest facets. The volume freed by facet pairs only moving towards each other is taken up as lateral growth of facets, ultimately resulting in the formation of corners. Lateral movement and facet area growth results in the formation of two relatively sharp (100) corners, which can be seen in the snapshot after $1\ \mu\text{s}$.

The oblate shape of the nanocrystal has to be metastable because it is asymmetric in the (110) planes. Contrary to the sphere and the cube, the cylinder has reached a shape where it cannot get closer to the equilibrium shape by removing atoms from a layer and using them for lateral growth of other facets. It has to grow new layers on top of the largest facets to get closer to equilibrium, and at this point it seems stuck in a metastable state. In order to kick the system out of its metastable shape, the temperature is raised to 2361 K to see whether it reaches the equilibrium shape. This heating causes a shape-change, as can be seen in the shaded part of Figure 3. After 200 ns at 2361 K, all facet pairs converge to same separation distance, and the particles reach the equilibrium shape. The dark blue facet pair takes about $0.2\ \mu\text{s}$ before it also converges to the same separation distance 5.5 nm. The nanocrystal shape is monitored for $0.6\ \mu\text{s}$ at 2,361 K, and we do not observe any changes in the shape of the nanocrystal. The final shape resembles the final shapes of nanocrystals with spherical and cubic initial configurations.

The oblate shape is metastable due to an energy barrier to the normal motion of sufficiently large facets. To estimate the magnitude of this barrier, we measure the growth rate in 63 simulations at varying temperatures between 2275 K and 2385 K. These simulations were run between 200 and 500 ns depending on the time needed to grow new layers. We monitor the

![](./images/812683556378640385_4.jpg)

Figure 3: Distance between facet pairs. Snapshots of (110) facets in different directions during a simulation taken at 0.2 ns, 20 ns, 0.1 $\mu$s, 1.05 $\mu$s and 1.5 $\mu$s. Lines show the distance between opposing facets, and line colours correspond to the colours indicated on the snapshots. The lines are step-like because the removal or addition of a layer results in a discontinuous change in the distance between facets. During the first 1 $\mu$s of the simulation the distance between most facet pairs decreases, but for the major facet pair (dark blue) we do not observe any layer growth nor shrinking, although their areas have increased. Upon heating, new layers grow on the major (110) facet, and the particle reaches its equilibrium shape. The distance between the major planes is constant throughout the first 1 $\mu$s, whereas both the cap plane distance and the minor facet distance are decreasing. In the final state, the distance between all pairs of parallel facets converge to the same value. The yellow, green, red and purple facets are the inclined, the light blue are the normal and the dark blue are the parallel facets with respect to the cylinder major axis.

time dependence of the number of atoms on top
of the largest (110) facet in all of these simula-
tions to determine the nucleation time for new
layers on the facet as function of layer depth
and temperature. This number abruptly grows
when a new layer is nucleated, so it is sharply
defined. Figure 4(a-b) shows how this number
develops for four layers growing in a simula-
tion at 2295 K. Figure 4(c) shows the waiting
times for a single layer height for all simula-
tions. From this Arrhenius plot, we estimate
the energy barrier for each layer height; see
Figure 4(d). This barrier is estimated to 14
eV for the first four layer heights on top of the
metastable oblate shape.

# Conclusions
This study demonstrates that processes such as
faceting and crystal growth can be within the
reach of microsecond molecular dynamics sim-
ulations. Here, we have provided insights into
the detailed faceting mechanisms of SiC. The
results and methods are of general importance
in the synthesis of nanocrystals and nanowires.
Other materials and processes should be stud-
ied using similar approaches to gain insight
into what mechanisms are general and what are
specific to SiC. Molecular dynamics studies of
faceting also open up for more detailed stud-
ies of crystal growth procedures and how they
are related to the resulting nanocrystal geome-
try.16,21 They may also let us address compet-
ing processes between crystal growth and de-
formation during healing and recrystallization
of faceting systems experiencing external me-
chanical forcing.

![](./images/812683556378640385_5.jpg)

Figure 4: Facet layer growth on the major
(110) plane of heated metastable silicon carbide
nanoparticles. (a) Layer growth, i.e. the num-
ber of atoms, in the first four layers after heat-
ing the metastable particle achieved after 1 $\mu$s
at $T = 2200$ K to $T = 2295$ K. The waiting
times $\tau_{1},...,\tau_{4}$ for the four layers are indicated
in the figure. The colours in (a) correspond to
the layers indicated in (b). (c) $\log(1/\tau)$ vs. $1/T$
gives the Arrhenius plot for the growth of the
second (red) layer. Each marker in (c) corre-
sponds to a full simulation of 200-500 ns. A
linear fit to this Arrhenius plot gives the en-
ergy barrier for the second layer. Following
the same procedure, we obtain the energy bar-
rier for layer formation for the first six layers
(d). Error bars in (d) indicate 67% confidence
bounds of linear fits to Arrhenius plots.

# Methods
SiC-3C was prepared with a lattice constant of
4.358 . To prepare initial nanocrystals, we cre-
ated a block of bulk SiC-3C in a cubic simula-
tion box of $(40\ \text{nm})^{3}$ (sphere), $(30\ \text{nm})^{3}$ (cube)
or $(23.4\ \text{nm})^{3}$ (cylinder), and then deleted
atoms that were outside the region defined by
the geometrical shape of that initial nanocrys-
tal. This method can lead to non-stoichiometry,

which we amended by adding particles to the void to regain stoichiometry. We performed molecular dynamics simulations of the silicon carbide nanocrystal (see. eg. ref.³⁵ for best practices of MD simulations). We used a force field consisting of two-body and three-body terms.³⁶ All simulations were run with periodic boundary conditions using an NVT Nosé–Hoover type thermostat³⁷ with a damping time of 1 ps. Equations of motion were integrated with the Velocity Verlet scheme using a timestep of 2 fs. The simulation box sizes were such that the nanocrystal did not interact with its periodic image. All simulations were run on NVIDIA P100 computing cards using the GPU package in LAMMPS.³⁸ Diffusion coefficients were calculated using the mean squared displacement of the top three surface layers over 100 ps.

Acknowledgement R.K., A.N. and P.V. were supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, Materials Science and Engineering Division, Grant # DE-SC0018195. The simulations were performed at the Argonne Leadership Computing Facility under the DOE IN-CITE program, at the Center for High Performance Computing of the University of Southern California, at the University of Oslo and using NOTUR grant NN9272K. Researcher exchange was financed by the Norwegian Research Council INTPART grant 250140.

Supporting Information Available: Brief descriptions of how the energy barriers for normal growth on facets were measured, and details of facet evolution on cylindrical n-SiC. This material is available free of charge via the Internet at http://pubs.acs.org/.

# References

(1) Capano, M. A.; Trew, R. J. Silicon Carbide Electronic Materials and Devices. *MRS Bull.* **1997**, *22*, 19–23.

(2) Song, B.-S.; Yamada, S.; Asano, T.; Noda, S. Demonstration of two-dimensional photonic crystals based on silicon carbide. *Opt. Express* **2011**, *19*, 11084–11089.

(3) Yakimova, R.; Jr, R. M. P.; Yazdi, G. R.; Vahlberg, C.; Spetz, A. L.; Uvdal, K. Surface functionalization and biomedical applications based on SiC. *J. Phys. D: Appl. Phys.* **2007**, *40*, 6435.

(4) Saddow, S. E. In *Silicon Carbide Biotechnology (Second Edition)*; Saddow, S. E., Ed.; Elsevier, 2016; pp 1–25.

(5) Zhao, J.-C.; Westbrook, J. H. UltrahighTemperature Materials for Jet Engines. *MRS Bull.* **2003**, *28*, 622–630.

(6) Yoshida, M.; Onodera, A.; Ueno, M.; Takemura, K.; Shimomura, O. Pressure-induced phase transition in SiC. *Phys. Rev. B* **1993**, *48*, 10587–10590.

(7) Tangpatjaroen, C.; Grierson, D.; Shannon, S.; Jakes, J. E.; Szlufarska, I. Size dependence of nanoscale wear of silicon carbide. *ACS Appl. Mater. Interfaces* **2017**, *9*, 1929–1940.

(8) Shimojo, F.; Ebbsjö, I.; Kalia, R. K.; Nakano, A.; Rino, J. P.; Vashishta, P. Molecular dynamics simulation of structural transformation in silicon carbide under pressure. *Phys. Rev. Lett.* **2000**, *84*, 3338–3341.

(9) Szlufarska, I.; Nakano, A.; Vashishta, P. Materials science: A crossover in the mechanical response of nanocrystalline ceramics. *Science* **2005**, *309*, 911–914.

(10) Chavoshi, S. Z.; Luo, X. Molecular dynamics simulation study of deformation mechanisms in 3C-SiC during nanometric cutting at elevated temperatures. *Mater. Sci. Eng., A* **2016**, *654*, 400–417.

(11) Sun, S.; Peng, X.; Xiang, H.; Huang, C.; Yang, B.; Gao, F.; Fu, T. Molecular dynamics simulation in single crystal 3C-SiC under nanoindentation: Formation of prismatic loops. *Ceram. Int.* **2017**, *43*, 16313–16318.

(12) Kinnear, C.; Moore, T. L.; Rodriguez-
Lorenzo, L.; Rothen-Rutishauser, B.;
Petri-Fink, A. Form Follows Function:
Nanoparticle Shape and Its Implications
for Nanomedicine. *Chem. Rev.* **2017**, *117*,
11476–11521.

(13) Murphy, C. J.; Sau, T. K.; Gole, A. M.;
Orendorff, C. J.; Gao, J.; Gou, L.; Hun-
yadi, S. E.; Li, T. Anisotropic Metal
Nanoparticles: Synthesis, Assembly, and
Optical Applications. *J. Phys. Chem. B*
**2005**, *109*, 13857–13870.

(14) Bruchez, M.; Moronne, M.; Gin, P.;
Weiss, S.; Alivisatos, A. P. Semiconduc-
tor Nanocrystals as Fluorescent Biological
Labels. *Science* **1998**, *281*, 2013–2016.

(15) Burda, C.; Chen, X.; Narayanan, R.; El-
Sayed, M. A. Chemistry and Properties of
Nanocrystals of Different Shapes. *Chem.
Rev.* **2005**, *105*, 1025–1102.

(16) Liao, H.-G.; Zherebetskyy, D.; Xin, H.;
Czarnik, C.; Ercius, P.; Elmlund, H.;
Pan, M.; Wang, L.-W.; Zheng, H. Facet
development during platinum nanocube
growth. *Science* **2014**, *345*, 916–919.

(17) Hansen, P. L.; Wagner, J. B.; Helveg, S.;
Rostrup-Nielsen, J. R.; Clausen, B. S.;
Topse, H. Atom-Resolved Imaging of Dy-
namic Shape Changes in Supported Cop-
per Nanocrystals. *Science* **2002**, *295*,
2053–2055.

(18) Zheng, H.; Smith, R. K.; Jun, Y.-
w.; Kisielowski, C.; Dahmen, U.;
Alivisatos, A. P. Observation of Sin-
gle Colloidal Platinum Nanocrystal
Growth Trajectories. *Science* **2009**, *324*,
1309–1312.

(19) Evans, J. E.; Jungjohann, K. L.; Brown-
ing, N. D.; Arslan, I. Controlled Growth of
Nanoparticles from Solution with In Situ
Liquid Transmission Electron Microscopy.
*Nano Lett.* **2011**, *11*, 2809–2813.

(20) Fei, L.; Ng, S. M.; Lu, W.; Xu, M.;
Shu, L.; Zhang, W.-B.; Yong, Z.;
Sun, T.; Lam, C. H.; Leung, C. W.;
Mak, C. L.; Wang, Y. Atomic-Scale Mech-
anism on Nucleation and Growth of Mo2C
Nanoparticles Revealed by in Situ Trans-
mission Electron Microscopy. *Nano Lett.*
**2016**, *16*, 7875–7881.

(21) Fichthorn, K. A.; Balankura, T.; Qi, X.
Multi-scale theory and simulation of
shape-selective nanocrystal growth. *Crys-
tEngComm* **2016**, *18*, 5410–5417.

(22) Sawada, K.; Iwata, J.-I.; Oshiyama, A.
Magic angle and height quantization in
nanofacets on SiC(0001) surfaces. *Appl.
Phys. Lett.* **2014**, *104*, 051605.

(23) Herring, C. Some Theorems on the Free
Energies of Crystal Surfaces. *Phys. Rev.*
**1951**, *82*, 87–93.

(24) Einstein, T. L. In *Handbook of Crystal
Growth (Second Edition)*; Nishinaga, T.,
Ed.; Elsevier: Boston, 2015; pp 215–264.

(25) Kitayama, M.; Narushima, T.;
Carter, W. C.; Cannon, R. M.;
Glaeser, A. M. The Wulff Shape of
Alumina: I, Modeling the Kinetics of
Morphological Evolution. *J. Am. Ceram.
Soc.* **2000**, *83*, 2561–2531.

(26) Ozdemir, M.; Zangwill, A. Morphological
equilibration of a facetted crystal. *Phys.
Rev. B* **1992**, *45*, 3718–3729.

(27) Gibbs, J. W. *The Collected Works of
J. Willard Gibbs*; Yale University Press,
1948; Google-Books-ID: SvQyAQAA-
IAAJ.

(28) Wulff, G. Zur Frage der Geschwindigkeit
des Wachstums und der Auflsung der
Krystallflagen. *Z. Kristallogr. Mineral.*
**1901**, *34*, 449–530.

(29) Pimpinelli, A.; Villain, J. *Physics of Crys-
tal Growth by Alberto Pimpinelli*; Cam-
bridge Core - Statistical Physics; Cam-
bridge University Press, 1998.

(30) Rottman, C.; Wortis, M. Statistical mechanics of equilibrium crystal shapes: Interfacial phase diagrams and phase transitions. *Phys. Rep.* **1984**, *103*, 59–79.

(31) Mullins, W. W.; Rohrer, G. S. Nucleation Barrier for Volume-Conserving Shape Changes of Faceted Crystals. *J. Am. Ceram. Soc.* **2000**, *83*, 214–16.

(32) Rohrer, G. S.; Rohrer, C. L.; Mullins, W. W. Nucleation Energy Barriers for Volume-Conserving Shape Changes of Crystals with Nonequilibrium Morphologies. *J. Am. Ceram. Soc.* **2001**, *84*, 2099–2104.

(33) Combe, N.; Jensen, P.; Pimpinelli, A. Changing shapes in the nanoworld. *Phys. Rev. Lett.* **2000**, *85*, 110–113.

(34) Wen, Y. H.; Fang, H.; Zhu, Z.; Sun, S. G. Molecular dynamics investigation of shape effects on thermal characteristics of platinum nanoparticles. *Phys. Lett. A* **2009**, *373*, 272–276.

(35) Braun, E.; Gilmer, J.; Mayes, H. B.; Mobley, D. L.; Monroe, J. I.; Prasad, S.; Zuckerman, D. M. Best Practices for Foundations in Molecular Simulations [Article v1.0]. *Living Journal of Computational Molecular Science* **2019**, *1*, 1–28.

(36) Vashishta, P.; Kalia, R. K.; Nakano, A.; Rino, J. P. Interaction potential for silicon carbide: A molecular dynamics study of elastic constants and vibrational density of states for crystalline and amorphous silicon carbide. *J. Appl. Phys.* **2007**, *101*, 103515.

(37) Tuckerman, M. E.; Alejandre, J.; López-Rendón, R.; Jochim, A. L.; Martyna, G. J. A Liouville-operator derived measure-preserving integrator for molecular dynamics simulations in the isothermal-isobaric ensemble. *J. Phys. A: Math. Gen.* **2006**, *39*, 5629–5651.

(38) Plimpton, S. Fast Parallel Algorithms for Short-Range Molecular Dynamics. *J. Comput. Phys.* **1995**, *117*, 1–19.

# For Table of Contents Use Only

Direct atomic simulations of facet formation and equilibrium shapes of SiC nanoparticles

Henrik Andersen Sveinsson, Anders Hafreager, Rajiv K. Kalia, Aiichiro Nakano, Priya Vashishta, Anders Malthe-Sørenssen

![](./images/812683556378640385_6.jpg)

## TOC Synopsis

We present direct molecular dynamics simulations of faceting of silicon carbide nanoparticles. Depending on the initial shape of the nanoparticle, and the temperature it is exposed to, the faceting process may lead to a metastable non-equilibrium shape of the nanoparticle. This metastable shape can be transformed into the equilibrium shape by heating, which pushes the system over an energy barrier to normal growth of crystal layers.