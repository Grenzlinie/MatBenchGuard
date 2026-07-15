Materials Research Express

ACCEPTED MANUSCRIPT

# Molecular dynamics simulation of melting of 2D glassy monatomic system

To cite this article before publication: Thi Nhu Tranh Duong *et al* 2018 *Mater. Res. Express* in press https://doi.org/10.1088/2053-1591/aaa7a5

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2018 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.

As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 184.171.112.49 on 20/01/2018 at 08:54

# Molecular Dynamics Simulation of Melting of 2D Glassy Monatomic System.

Duong Thi Nhu Tranh¹, Vo Van Hoang¹, Tran Thi Thu Hanh²,*

¹Computational Physics Lab., Ho Chi Minh City University of Technology, Vietnam National University – Ho Chi Minh City, Vietnam;268 Ly Thuong Kiet Street, District 10, Ho Chi Minh City, Vietnam,
Email: dtntranh@hcmut.edu.vn

²,*Computational Materials Physics Research Group & Faculty of Applied Sciences, Ton Duc Thang University, Ho Chi Minh City, Vietnam; 19 Nguyen Huu Tho Street, Tan Phong Ward, District 7, Ho Chi Minh City, Vietnam,
Email of corresponding author: tranhithuhanh@tdt.edu.vn

## Abstract

The melting of two-dimensional (2D) glassy monatomic systems is studied using the molecular dynamics (MD) simulation with Lennard–Jones–Gauss (LJG) interaction potential. The temperature dependence of various structural and dynamical properties of the systems during heating is analyzed and discussed via the radial distribution functions (RDFs), the coordination number distributions, the ring statistics, the mobility of atoms and their clustering. Atomic mechanism of melting is also analyzed via tendency to increase mobility and breaking clusters of atoms upon heating. We found that melting of a 2D glass does not follow any theory of the melting of 2D crystals proposed in the past. The melting exhibits a homogeneous nature, i.e. liquid-like atoms occur homogeneously throughout the system and melting proceeds further leading to the formation of an entire liquid phase. In addition, we found a defined transition temperature region in which structural and dynamical properties of systems strongly change with increasing temperature.

Keywords: 2D glassy systems, melting, glass transition, transition temperature.

## 1. Introduction

Surface properties of materials, like thin films, are of great importance in technologies [1-4]. In 2004, single-layer graphene was successfully identified, and has added a new dimension of research and development in the fields of physics, chemistry, technology, and materials science [5]. Due to the enormously important applications, the research effort focused on 2D system is increasing [6-10]. According to the Kosterlitz-Thouless-Halperin-Nelson-Young (KTHNY) theory, the melting of 2D crystals is described by unbinding of topological order defects, i.e. disclinations and dislocations, via two continuous transitions: 2D crystal $\rightarrow$ hexatic phase $\rightarrow$ isotropic liquid [11-15]. The melting of 2D crystal was studied by several experiments [6-8,16-19] and simulations [20-31], however, they gave conflicted conclusions. Some studies supported KTHNY theory [16-19,21-23], some others showed that the 2D systems melt from the solid to liquid via the first order transition without hexatic phase [6,22,27,30]. These contradictory results may suggest that the melting of 2D systems depends sensitively on finite-size effect [20,23,31] and particle interactions [10,24-27]. A. Derzsi et al. concluded that increasing the system size in particle simulations only can be insufficient and can result in misleading conclusions, such as the length of the equilibration period also plays a crucial role in building up the equilibration of the long range correlations [23]. In [27], E.S. Chumakov and et al. calculated the phase diagram of two-dimensional system of particles interacting through the repulsive shoulder potential and concluded that at low densities the system melts through a continuous transition, while at high densities the conventional first order transition takes place.

Glasses are an important class of materials, they are found in a variety of commercial products and applications [4,32]. In contrast, limited information about melting of 2D amorphous solids can be found while main attention has been paid on glass formation or related problems in various 2D systems. For example, we can find information about the transition from a liquid to a glass [33-36], structure and dynamics of 2D glassy systems [34-41], fundamental difference between glassy dynamics in 2D and 3D glasses [41]. The glass formation in 2D supercooled monatomic liquid is homogeneous and it proceeds via several intermediate phases [34]. However, there is no information related to the melting of 2D glass can be found. It motivates us to carry out this study. In this study,

we present the MD simulation of melting of a 2D glassy monatomic system. The main aims here are given as follows: investigation of structural and dynamical heterogeneities occurred during heating, atomic mechanism of melting process and heating rate dependence of observed quantities.

## 2. Calculation

Molecular dynamics (MD) simulations were carried out in a monatomic system containing $N=6400$ particles with initially simple squared lattice structure of the size of $S=80.0r_{o} \times 80.0r_{o}$ and at the fixed density $\rho=(N/S)=1.0$ interacted via Lennard-Jones-Gauss (LJG) interatomic potential under periodic boundary conditions. The LJG potential form is given below [42]:

$$
V(r)=\varepsilon_{0}\left[\left(\frac{r_{0}}{r}\right)^{12}-2\left(\frac{r_{0}}{r}\right)^{6}\right]-\varepsilon \exp \left[-\frac{\left(r-r_{G}\right)^{2}}{2 \sigma^{2}}\right]
$$

In this study, the parameters for LJG potential are taken as in Ref. 43. Here, $r_{o}$ is an atomic diameter, $\varepsilon_{o}$ is a depth of LJ part of LJG potential, $r_{G}$ is a position, $\varepsilon$ is a depth, and $\sigma$ is a width of well of Gauss part one. We employ the LJ reduced units as follows [34]: energy is in units of $\varepsilon_{o}$, length is in units of $r_{o}$, temperature T is in units of $\varepsilon_{o}/k_{B}$, and time is in units of $\tau_{o}=r_{o}(m/\varepsilon_{o})^{1/2}$ where $k_{B}$ is the Boltzmann constant, m is an atomic mass. If taking Ar for testing (atomic mass of Ar is $m=0.66 \times 10^{-25} kg$ and atomic diameter of one is $r_{o}=3.84Å$ ), temperature T is in units of $\varepsilon_{o}/k_{B}=118\ K$ and time is in units of $\tau_{o}=r_{o}(m/\varepsilon_{o})^{1/2}=2.44 ps$. The Verlet algorithm is used with the MD time step of $dt=0.001\tau_{o}=2.44 fs$. "NVT" ensemble is used in this MD simulation.

Initially, the atomic configuration has been relaxed at a temperature $T=2.5$ for $2 \times 10^{6}$ MD steps in order to get an equilibrium liquid state. Then the system is cooled down to $T=0.1$ at a cooling rate $\gamma=10^{-6}$ per MD step ($4.836 \times 10^{10} K/s$ if taking Ar for testing) and the temperature is decreased linearly with time as $T=T_{o}-\gamma \times n$ via the simple atomic

velocity rescaling until reaching $T=0.1$ [34]. Here, $\gamma$ is the cooling rate and n is the number of MD steps. After cooling, the system obtained in glassy state is heated up to initial temperature at $T=2.5$ at two heating rates, $\gamma=10^{-6}$ and $\gamma=10^{-5}$ per MD step ( $4.836 \times 10^{10} \mathrm{~K} / \mathrm{s}$ and $4.836 \times 10^{11} \mathrm{~K} / \mathrm{s}$ if taking Ar for testing, respectively) via formula $T=T_{o}+\gamma \times n$. In order to improve the statistics, we average results over two independent runs.

## 3. Results and discussions

### 3.1. Thermodynamics

Thermodynamics of melting of 2D glassy monatomic system is investigated via potential energy and heat capacity. Temperature dependence of potential energy is of great interest, because from its dependence we can investigate important quantities and phenomena, such as phase transition temperature and related phase transitions. Figure 1 exhibits (a) the temperature dependence of potential energy and (b) the heat capacity per atom upon heating from the glass at two heating rates, $\gamma=10^{-6}$ per MD step and $\gamma=10^{-5}$ per MD step. As shown in Figure 1(a), the curves of temperature dependence of potential at given heating rates fall out of linear change in the temperature region $0.2<T<0.8$. It is a behavior of glass transition. The starting point of deviation from the linearity, at $T=0.2$ , is a crossover temperature where the change in mechanism of diffusion occurs. It means that the melting process is started, the dynamics of system rapidly increases until reaching $T=0.8$. The relatively linear part of the high temperature region of the curves is related to the liquid state. Additionally, the curve of the temperature dependence shape obtained by heating rate $\gamma=10^{-6}$ per MD step changes with a larger slope than the other in temperature range $0.2<T<0.8$ (see inset of Figure 1(a)). Transition temperature can be deduced from peak position of heat capacity curve of the system during heating process as it was done in [34]. Heat capacity is approximately calculated via the simple relation: $C_{p}=\Delta E / \Delta T$. Here, $\Delta E$ is a discrepancy of potential energy per atom upon heating from $T_{1}$ to $T_{2}$ [34]. As show in Figure 1(b), the heat capacity curves of the models have a single peak at around

$T_g=0.33$ for model obtained by using $\gamma=10^{-6}$ per MD step and at around $T_g=0.39$ for one obtained by using $\gamma=10^{-5}$ per MD step are determined as the transition temperatures for each heating rates, respectively. Besides, the peak of the model obtained at slower heating rate is higher and narrower than other one. The difference between $T_g$ obtained at two heating rates is small and almost lies within statistical error since $T_g$ slightly depends on heating rate as found in the past. The value $T_g=0.33$ is a little higher than the data obtained previously ($T_g=0.31$ in [34]) when the same system is cooled through the same temperature range. Beside the statistical errors, it may be due to the thermal hysteresis of glass-forming systems in general (see [44,45] and references therein). Indeed, evolution of inherent structure of LJ glass-forming system upon cooling from the melt is studied and a hysteresis is observed upon heating [44]. Similarly, isobaric thermal behaviors of glasses during uniform cooling and heating also exhibit a thermal hysteresis [45]. Additionally, the values of $T_g$ obtained here are much lower than those found for the thin film-like system ($T_g=0.61$) (see [46]).

The evolution of the structure of the system upon heating from the glass can be seen in Figure 2. As shown in Figure 2, the radial distribution function (RDF) of the model at $T=0.1$ is typical for the glass-like behavior, i.e. it has a shape with a high first peak and some additional peaks as that found in [34] and [43]. With increasing temperature, the small peaks have a tendency to disappear and they totally disappear in both obtained models by using different heating rates when temperature is ~ 0.9. It means that the system is totally melted and turns into isotropic liquid state. It is in agreement with the result observed in Figure 1 at transition temperature region $0.2<T<0.8$. We consider $T=0.8$ is the total melting temperature. It will be discussed in more details below. Further, the RDFs obtained by using both heating rates are almost not different. On the other hand, the static diffraction images of the atomic configurations obtained via calculating static structure factor at $T=0.1$ (Figure 2(b)) and at $T=2.5$ (Figure 2(c)) clearly exhibit glassy and liquid nature of the atomic configurations, respectively.

More details about the structure in the system can be seen via coordination number and ring distributions. The temperature dependence curves of the mean coordination number $\bar{Z}$ upon heating indicate the temperature region of the glass-liquid transition ranging from $T=0.2$ to $T=0.8$ as defined above. And both curves of mean coordination numbers $\bar{Z}$ at two heating rates change strongly and rapidly (see Figure 3(a)) in $0.2<T<0.8$. At $T=0.1$, the obtained mean coordination number of the system in the glassy state is about $\bar{Z}=3.73$, the coordination numbers $Z=3$ and $Z=4$ are dominated in the model (about 65.3% of atom have $Z=3$ and 29.27% of ones have $Z=4$) (see Figure 3(b)). With increasing temperature, mean coordination number increases due to decreasing fraction of atoms have $Z=3$, $Z=4$ and increasing fraction of atoms have large coordination number. From $T=0.8$ to higher temperature, $\bar{Z}$ is almost not change with increasing temperature and fluctuates about value $\bar{Z}=4.14$.

We can gain further insights into the nature of the connectivity of elementary units beyond the nearest neighbors in terms of ring analysis [47]. Ring statistics is mainly used to obtain a snapshot of the connectivity of a network that provides a deeper understanding of amorphous network topology. I.S.A.A.C.S software has been employed for calculating ring statistics following the "shortest path" rule with a cut off radius $R_{C}=1.2r_{o}$ (see [47]). This cutoff radius is equal to the position of the first minimum after the first peak in RDF of a glassy state obtained at $T=0.1$. We find that pentagons (i.e., 5-fold rings) dominate in the model obtained at $T=0.1$ and triangles, squares plus pentagons are the basic structural units in the glassy state (i.e., 3-fold, 4- fold and 5-fold rings, see Figure 4(a) and (c)). It is also consistent with that found previously in Ref. 43. Moreover, we find the existence of larger rings such as 6-fold, 7-fold, 8-fold and 9-fold rings which have not been reported yet. In the temperature region lower than total melting temperature, we find that 3-fold rings increase and 5-fold rings decrease strongly with increasing temperature i.e. mean ring size strongly decreases. From $T=0.8$ to higher one, mean ring size fluctuates about the value 3.64 with increasing temperature (Figure 4(b)). It is related to existence of triangular structure and a small number of large rings of the system in glassy state. Additionally, one can see that the results of the models obtained by using heating rate of $\gamma=10^{-6}$ and $\gamma=10^{-5}$

per MD step are almost the same. So from now, we will only show the results of the model obtained at heating rate $\gamma=10^{-6}$ per MD step below.

### 3.2. Heterogeneous dynamics and atomic mechanism of melting of 2D glassy monatomic system

Dynamic properties of models during heating can be seen via analysis of the temperature dependence of the mobility of atoms and their clustering (Figure 5, Figure 6, Figure 7 Figure 8 and Figure 9). Models obtained by heating from the glass have been relaxed for 5000 MD steps or $5\tau_0$ at a given temperature before further spatio-temporal analysis of configurations based on dynamics of atoms (see [34] and references therein).

The evolution of the mobility of atoms in the system during heating is shown in Figure 5 via temperature dependence of fraction of atoms with different mobilities at a given temperature. There are three main points shown as follows:

i) In low temperature region, the atoms with low mobility and the dependence on the temperature becomes more complicated. In glassy state at $T=0.1$, fraction of atoms with low atomic displacement ($ad$) such as $ad=[0.0-0.2)$ is about 64.6% and they have a tendency to decrease rapidly with increasing temperature while atoms with different higher mobility , $ad\geq0.2$, have tendency to increase first and then decrease. Atoms become more spatially heterogeneous.

ii) The curves of distribution of fraction of atoms with $ad\geq0.2$ has one peak and the peak gradually shifts away in temperature region ranging from $T=0.2$ to $T=0.8$. It means that the system starts to melt from $T=0.2$ and it turns into liquid state almost completely at $T=0.8$. This result is consistent with results obtained above.

iii) In the high temperature region, the fraction of atoms with higher mobility is higher. Atoms with very low mobility are poor.

We use VMD software for 2D visualization of the atomic configurations [48]. Atoms with different atomic displacements (ad) are colored differently (see Figure 6). At $T=0.1$, atoms have low mobility. The blue atoms (i.e., atoms with $ad=[0.0-0.2)$) are considered as solid-like ones that are contributed almost in the whole model, and are

bonded to obtain a large cluster (Figure 6(a) and Figure 8). During heating, the mobility of atoms is increased and the largest cluster of solid-like atoms is broken to many small clusters distributing in the whole model. Atoms with $ad=[0.0-0.2)$ (blue atoms) decrease and ones with $ad=[0.2-0.4)$ (red atoms) increase in the temperature region lower than the transition temperature $T_g=0.33$. But above transition temperature, blue and red atoms strongly decrease while gray, orange and yellow atoms (with $ad=[0.4-0.6)$ , $ad=[0.6-0.8)$ and $ad=[0.8-1.0)$ respectively) occur and dominate in the system (see Figure 5, Figure 6(b) at $T=0.3$ and Figure 6(c) at $T=0.4$ ). When the system reaches $T=2.5$, one can see atoms with high mobility (tan, silver ... atoms with $ad \geq 1.0$ ) enhance almost in the whole model. It is related to liquid state of the system (see Figure 6(d)). Atomic mechanism of melting of glass 2D systems is monitored via analyzing spatio- temporal arrangements of the liquid-like atoms occurred during heating process. As described above, one can see that atoms with high mobility as liquid-like ones occur first at temperature far below $T_g=0.33$ like that found in glassy monatomic nanoparticles and thin film-like systems using the same LJG potential (see [49] and Refs therein). In order to highlight the situation, we show 2D visualizations of liquid-like atoms occurred in the system obtained upon heating (Figure 7). We can see that at $T=0.2$ , i.e. below $T_g$ , liquid like atoms also occur in model, and the in transition temperature region, they rapidly grow in the models with increasing temperature (Figure 7(a) - (c)). Liquid-like atoms occur homogeneously throughout the system unlike that found in 3D system with free surface[50]. In high temperature region, system turns into liquid state, liquid-like atoms grow in whole the models (Figure 7(d) - (f)).

Clustering of atoms with the same or close mobility can be seen in Figure 8 and Figure 9. We find that temperature dependence of size of the largest cluster $(S_{max}$ , Figure8) of atoms with very slow dynamics (e.g., atoms with $ad=[0.0-0.2)$ exhibit the same behavior like that found for the fraction of atoms with same mobility. During heating, atoms in model have a tendency to increase mobility and the largest cluster of glassy state is broken when model is heated up to liquid. Cluster of atoms with $ad=[0.4-0.6)$ has a tendency to increase first and then it decreases down to zero passing over a maximum (see

inset). However, the minimum is lower than one observed in Ref. 34 when the same system is cooled by the same method. In the temperature region higher than that of transition temperature, clusters of all atoms fluctuate about zero. But one can see that cluster of atoms with higher mobility is larger (see inset). In addition, Figure 9 shows that mean cluster size rapidly decreases in temperature region below $T_g$. In high temperature region, mean cluster size is about zero. Almost atoms with the high mobility in models don't have any tendency to form cluster or only form clusters with few atoms.

### 4. Conclusions

The MD simulation of the melting of a 2D glassy monatomic system has been carried out. We found that: (i) There is almost not different in results obtained by using the two different heating rates, (ii) The transition temperature region of 2D glassy monatomic system using LJG potential is ranged from 0.2 to 0.8. In this region, the dynamical properties of the system strongly depend on the temperature, (iii) The melting of a 2D glass exhibits a homogeneous nature, i.e. liquid-like atoms occur homogeneously throughout the system. They are clustered and clusters grow with further heating leading to the formation of a single liquid phase of glass-liquid phase transition behavior. (iv) Melting of 2D glass does not follow any theory of the melting of 2D crystals proposed in the past.

### Acknowledgements:
We thanks for financial support from the Vietnam National University - Ho Chi Minh City (VNU-HCM) under grant number B2017-20- 02.

### References

[1]. Li X and Bhushan B 2002 A review of nanoindentation continuous stiffness measurement technique and its applications *Mater. Charact.* **48** 11

[2]. Legrand A P 1998 *The Surface Properties of Silica* (Wiley, New York)

[3]. Liu X, Chu P K and Ding C 2004 Surface modification of titanium, titanium alloys, and related materials for biomedical applications *Mater. Sci. Eng. R* **47** 49

[4]. Castanié S, Carlier T, Mear F O, Saitzek S, Blach J-F, Podor R and Montagne L 2016 Self-healing glassy thin-coating for high temperature applications *ACS Appl. Mater. Interfaces* **8** 4208

[5]. Novoselov K S, Geim A K, Morozov S V, Jiang D, Zhang Y, Dubonos S V, Grigorieva I V and Firsov A A 2004 Electric field effect in atomically thin carbon films *Science* **306** 666

[6]. Angelescu D E, Harrison C K, Trawick M L, Register R A and Chaikin P M 2005 Two-dimensional melting transition observed in a block copolymer *Phys. Rev. Lett.* **95** 025702

[7]. Deutschländer S, Horn T, Löwen H, Maret G and Keim P 2013 Two-dimensional melting under quenched disorder *Phys. Rev. Lett.* **111** 098301

[8]. Han Y, Ha N Y, Alsayed A M and Yodh A G 2008 Melting of two-dimensional tunable-diameter colloidal crystals *Phys. Rev. E* **77** 041406

[9]. Deutschländer S, Puertas A M, Maret G and Keim P 2014 Specific heat in two- dimensional melting *Phys. Rev. Lett.* **113** 127801

[10]. Mak C H 2006 Large-scale simulations of the two-dimensional melting of hard disks *Phys. Rev. E* **73** 065104

[11]. Berezinsky V L 1971 Destruction of long-range order in one-dimensional and two- dimensional systems having a continuous symmetry group I. classical systems *Sov. Phys. JETP* **32** 493; 1972 Destruction of long-range order in one-dimensional and two- dimensional systems having a continuous symmetry group. II. quantum systems *Sov. Phys. JETP* **34** 610

[12]. Kosterlitz J M and Thouless D J 1973 Ordering metastability and phase transitions in two-dimensional systems *J. Phys. C: Solid State Phys.* **6** 1181

[13]. Halperin B I and Nelson D R 1978 Theory of two-dimentional melting *Phys. Rev. Lett.* **41** 121

[14]. Young A P 1978 On the theory of the phase transition in the two-dimentional planar spin model J. Phys. C: Solid State Phys. 11 L453; 1979 Melting and the vector Coulomb gas in two dimensions Phys. Rev. B 19 1855

[15]. Nelson D R and Halperin B I 1979 Dislocation-mediated melting in two dimensions Phys. Rev. B 19 2457

[16]. Brodin A, Nych A, Ognysta U, Lev B, Nazarenko V, Skarabot M and Musevic I 2010 Melting of 2D liquid crystal colloidal structure Condens. Matter Phys. 13 33601

[17]. Horn T, Deutschländer S, Löwen H, Maret G and Keim P 2013 Fluctuations of orientational order and clustering in a two-dimensional colloidal system under quenched disorder Phys. Rev. E 88 062305

[18]. Schockmel J, Mersch E, Vandewalle N and Lumay G 2013 Melting of a confined monolayer of magnetized beads Phys. Rev. E 87 062201

[19]. Zahn K and Maret G 2000 Dynamic criteria for melting in two dimensions Phys. Rev. Lett. 85 3656

[20]. Patashinski A Z, Orlik R, Mitus A C, Grzybowski B A and Ratner M A 2010 Melting in 2D Lennard-Jones systems: What type of phase transition? J. Phys. Chem. C 114 20749

[21]. Wei-Kai Qi, Ziren Wang, Yilong Han and Yong Chen 2010 Melting in two-dimensional Yukawa systems: A Brownian dynamics simulation J. Chem. Phys. 133 234508

[22]. Gribova N, Arnold A, Schilling T and Holm Ch 2011 How close to two dimensions does a Lennard-Jones system need to be to produce a hexatic phase? J. Chem. Phys. 135 054514

[23]. Derzsi A, Kovacs A Zs, Donko Z and Hartmann P 2014 On the metastability of the hexatic phase during the melting of two-dimensional charged particle solids Phys. Plasmas 21 023706

[24]. Dudalov D E, Tsiok E N, Fomin Yu D and Ryzhov V N 2014 Effect of a potential softness on the solid-liquid transition in a two-dimensional core softened potential system J. Chem. Phys. 141 18C522

[25]. Dudalov D E, Fomin Yu D, Tsiok E N and Ryzhov V N 2014 Melting scenario of the two-dimensional core-softened system: first-order or continuous transition? *J. Phys.: Conf. Ser.* **510** 012016

[26]. Binder K, Sengupta S and Nielaba P 2002 The liquid–solid transition of hard discs: first-ordertransition or Kosterlitz–Thouless–Halperin–Nelson–Young scenario? *J. Phys.: Condens. Matter* **14** 2323

[27]. Chumakov E S, Fomin Yu D, Shangina E L, Tareyeva E E, Tsiok E N and Ryzhov V N 2015 Phase diagram of the system with the repulsive shoulder potential in two dimensions: Density functional approach *Physica A* **432** 279

[28]. Chen K, Kaplan T and Mostroller M 1995 Melting in two-dimensional Lennard-Jones systems: Observation of a metastable hexatic phase *Phys. Rev. Lett.* **74** 4019

[29]. Bagchi K, Andersen H C and Swope W 1996 Computer simulation study of the melting transition in two dimensions *Phys. Rev. Lett.* **76** 255

[30]. Weber H, Marx D and Binder K 1995 Melting transition in two dimensions: A finite-size scaling analysis of bond-orientational order in hard disks *Phys. Rev. B* **51** 14636

[31]. Wierschem K and Manousakis E 2010 Simulation of two-dimensional melting of Lennard-Jones solid *Phys. Procedia* **3** 1515

[32]. Kalogeras I M and Lobland H E H 2012 The nature of the glassy state: structure and glass transitions *J. Mater. Educ.* **34** 69

[33]. Mizuguchi T and Odagaki T 2009 Vitrification of a monatomic 2D simple liquid *Cent. Eur. J. Phys.* **7** 479

[34]. Hoang V V 2015 New scenario of dynamical heterogeneity in supercooled liquid and glassy states of 2D monatomic system *J. Phys. Chem. B* **119** 15752

[35]. Sim E, Patashinski A Z and Ratner M A 1997 Supercooling in a two-dimensional Lennard-Jones mixture *J. Chem. Phys.* **107** 6887

[36]. Brüning R, St-Onge D A, Patterson S and Kob W 2009 Glass transitions in one-, two- , three-, and four-dimensional binary Lennard-Jones systems *J. Phys.: Condens. Matter* **21** 035117

[37]. Mazoyer S, Ebert F, Maret G and Keim P 2011 Correlation between dynamical heterogeneities, structure and potential-energy distribution in a 2D amorphous solid *Eur. Phys. J. E* **34** 11101

[38]. Kawasaki T and Tanaka H 2011 Structural signature of slow dynamics and dynamic heterogeneity in two-dimensional colloidal liquids: glassy structural order *J. Phys.: Condens. Matter* **23** 194121

[39]. Tsamados M 2010 Plasticity and dynamical heterogeneity in driven glassy materials *Eur. Phys. J. E* **32** 165

[40]. Buchner C, Schlexer P, Linchtenstein L, Stucenholz S, Heyde M and Freund H-J 2014 Topological investigation of two-dimentional amorphous materials *Z. Phys. Chem.* **228** 587

[41]. Flenner E and Szamel G 2015 Fundamental differences between glassy dynamics in two and three dimensions *Nat. Commun.* **6** 7392

[42]. Engel M and Trebin H-R 2007 Self-assembly of monatomic complex crystals and quasicrystals with a double-well interaction potential *Phys. Rev. Lett.* **98** 225505

[43]. Mizuguchi T and Odagaki T 2009 Glass formation and crystallization of a simple monatomic liquid *Phys. Rev. E* **79** 051501

[44]. Jonsson H and Andersen H C 1988 Icosahedral ordering in the Lennard-Jones liquid and glass *Phys. Rev. Lett.* **60** 2295

[45]. Kovacs A J and Hutchinson J M 1979 Isobaric thermal behavior of glasses during uniform cooling and heating: Dependence of the characteristic temperatures on the relative contributions of temperature and structure to the rate of recovery. II. A one-parameter model approach *J. Polymer Sci.* **17** 2031

[46]. Hoang V V and Dong T Q 2011 Melting of monatomic glass with free surfaces *Phys. Rev. B* **84** 174204

[47]. Roux S L and Petkov V 2010 ISAACS - Interactive structure analysis of amorphous and crystalline systems J. Appl. Crystallogr. **43** 181

[48]. Humphrey W, Dalke A and Schulten K 1996 VMD: Visual molecular dynamics J. Mol. Graphics **14** 33

[49]. Hoang V V 2012 Melting of simple monatomic amorphous nanoparticles J. Phys. Chem. C **116** 14728

[50]. Swallen S F, Kearns K L, Satija S, Traynor K, McMahon R J and Ediger M D 2008 Molecular view of the isothermal transformation of a stable glass to a liquid J. Chem. Phys. **128** 214514

![](./images/813066898102026242_1.jpg)

Figure 1. Temperature dependences of potential energy per atom (a), and heat capacity per atom (b) upon heating from the glass. Inset shows temperature dependence of potential energy per atom in the temperature region around the transition temperature.

![](./images/813066898102026242_2.jpg)

Figure 2. Radial distribution functions upon heating from the glass for temperature ranged from 0.1 to 2.5 with increment of 0.4 from bottom to top (a), static diffraction image of atomic configuration obtained at $T=0.1$ (b) and $T=2.5$ (c) by using heating rate $\gamma=10^{-6}$ per MD step.

![](./images/813066898102026242_3.jpg)

Figure 3. Temperature dependences of mean coordination number upon heating from the glass (a), and coordination number distributions at given temperatures (b).

![](./images/813066898102026242_4.jpg)

Figure 4. Temperature dependences of ring sizes (a), and mean ring size (b) upon heating from the glass. (c) A 2D visualization of the atomic configuration of the system at temperature $T=0.1$. Rings are filled by the color as follows: grey for triangles, red for squares and blue for pentagons. The white color is for larger rings.

![](./images/813066898102026242_5.jpg)

Figure 5. Temperature dependence of fraction of atoms with various atomic displacements after relaxation at a given temperature for 5000 MD steps.

Figure 6

![](./images/813066898102026242_6.jpg)
(a) T = 0.1

![](./images/813066898102026242_7.jpg)
(b) T = 0.3

![](./images/813066898102026242_8.jpg)
(c) T = 0.4

![](./images/813066898102026242_9.jpg)
(d) T = 2.5

Figure 6. 2D visualization of atoms with the same (or close) atomic displacement (ad, in LJ reduced unit) after relaxation for 5000 MD steps at a given temperature, atoms are colored as follows: blue for $ad=[0.0-0.2)$, red for $ad=[0.2-0.4)$, gray for $ad=[0.4-0.6)$ , orange for $ad=[0.6-0.8)$ , yellow for $ad=[0.8-1.0)$, tan for $ad=[1.0-1.2)$, silver for $ad=[1.2-1.4)$, green for $ad=[1.4-1.6)$, white for $ad=[1.6-1.8)$, pink for $ad=[1.8-2.0)$ , and cyan for $ad \geq 2.0$.

![](./images/813066898102026242_10.jpg)

Figure 7. 2D visualization of the appearance of liquid-like atoms in the system at a given temperature upon heating.

Figure 8

![](./images/813066898102026242_11.jpg)

Figure 8. Temperature dependence of size of the largest cluster ($S_{max}$/N) of atoms with 03 selected atomic displacement ranges after relaxation at a given temperature for 5000 MD steps. Inset shows the low fraction region.

![](./images/813066898102026242_12.jpg)

Figure 9. Temperature dependence of the mean cluster size of atoms with 03 selected atomic displacements after relaxation at a given temperature for 5000 MD steps.