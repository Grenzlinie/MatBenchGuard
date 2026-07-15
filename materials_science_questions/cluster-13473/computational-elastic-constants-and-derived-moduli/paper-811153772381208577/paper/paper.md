# Computer simulation of the mechanical properties of metamaterials

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 J. Phys.: Conf. Ser. 738 012100

(http://iopscience.iop.org/1742-6596/738/1/012100)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 195.34.78.252
This content was downloaded on 18/10/2016 at 08:15

Please note that terms and conditions apply.

You may also be interested in:

Superresolution and enhancement in metamaterials
Andrei N Lagarkov, Andrei K Sarychev, V N Kissel et al.

Local field effects in periodic metamaterials
O V Porvatkina, A A Tishchenko and M N Strikhanov

Local field effects and metamaterials based on colloidal quantum dots
O V Porvatkina, A A Tishchenko and M N Strikhanov

Mechanical properties of different types of space maintainers
M-A Beldiman, I Mâru, B Leioiu et al.

Mechanical Properties of Heat Affected Zone of High Strength Steels
K Sefcikova, T Brtnik, J Dolejs et al.

Second harmonic generation in left-handed metamaterials
A K Popov, V V Slabko and V M Shalaev

Optical cloaks edge closer

5th International Conference on Mathematical Modeling in Physical Sciences (IC-MSsquare 2016) IOP Publishing
Journal of Physics: Conference Series **738** (2016) 012100
doi:10.1088/1742-6596/738/1/012100

# Computer simulation of the mechanical properties of metamaterials

R A Gerasimov¹, V A Eremeyev¹, T O Petrova¹, V I Egorov², O G Maksimova²
and A V Maksimov²

¹ Southern Federal University, 105/42 Bolshaya Sadovaya Str., Rostov-on-Don,
344006, Russian Federation

² Cherepovets State University, 5 Lunacharskii Av., Cherepovets, 162600, Russian
Federation

E-mail: roman-gerasimoff@yandex.ru

**Abstract.** For a hybrid discrete-continual model describing a system which consists of a substrate and polymer coating, we provide computer simulation of its mechanical properties for various levels of deformations. For the substrate, we apply the elastic model with the Hooke law while for the polymeric coating, we use a discrete model. Here we use the Stockmayer potential which is a Lennard-Jones potential with additional term which describes the dipole interactions between neighbour segments of polymer chains, that is Keesom energy. Using Monte-Carlo method with Metropolis algorithm for a given temperature the equilibrium state is determined. We obtain dependencies of the energy, force, bending moment and Young's modulus for various levels of deformations and for different values of temperature. We show that for the increase of the deformations level the influence of surface coating on the considered material parameters is less pronounced. We provide comparison of obtained results with experimental data on deformations of crystalline polymers (gutta-percha, etc.)

## 1. Introduction
Nowadays the interest grows to design and control of surface properties of materials. In particular, surface properties related with wetting and dewetting are important in order to obtain super-hydrophobic or super-hydrophilic properties [1-6]. Among physical and chemical methods of surface enhancements, it is worse to mention the plasma treatment, electroplating, lithography, etching, polymers grafting [7-9]. Especially, the methods of grafting of polymeric chains are attractive. These methods give the possibility to change the effective surface properties of a substrate such as adhesion, wetting, tribological properties, etc, without changing of the bulk properties of substrate. In other words, the substrate surface may inherit the properties of attached polymer [1, 7]. Wide choice of existing polymers possesses the design of the surface properties and manufacturing of new hybrid materials. In addition, these methods may produce rough and porous surface to obtain self-cleaning coatings such as lotus leaves. In this case the wetting of the surface is determined by both chemical properties of polymer and microstructure of the coating [1].

![](./images/811153772381208577_1.jpg)
Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Published under licence by IOP Publishing Ltd

Particular attention is recently paid to polymeric brushes as a way of producing of smart surfaces [10]. A polymer brush is a monolayer of polymer chains connected with an impermeable surface (substrate) by terminal ends (figure 1).

As a substrate the aluminium, its alloys and oxides are widely used [1]. Modifications of the aluminium based substrates are performed in order to decrease contact friction, adhesion, and to improve corrosion resistance. Enhancements of textile fibres also may lead to new materials. Formed on a substrate surface nano-rough polymer film results in hydro- and oleophobic properties of fibres that may be used for manufacturing of protective and bactericidal clothes [11]. The aim of this paper is to simulation of such kind surface metamaterials.

![](./images/811153772381208577_2.jpg)

**Figure 1.** Plane polymer brush with chain height H.

## 2. Model
In figure 2 the hybrid discrete-continual system is shown. The system consists of plane rotators of length $l$ attached to a substrate which is considered within the continuum model. The presented system is subjected by external tensile force $F$ applied to both substrate and coating.

Within the framework of multiparticle models of polymers [12-17] $N_1N_2N_3$ rigid kinematical units, so-called rotators, of length $l$ forms quasi-lattice $\vec{n}=(n_1,n_2,n_3)$, where indices $n_1$, $n_2$, $n_3$ take the following values: $n_1=1,\dots,N_1; n_2=1,\dots,N_2; n_3=1,\dots,N_3$.

![](./images/811153772381208577_3.jpg)

**Figure 2.** (a) Discrete-continuum model: model of 3D ordered $N_2N_3$ chains consisting of $N_1$ rigid kinematic elements, so-called rotators of length $l$ connected with the substrate (here $N_2$ and $N_3$ are the numbers of chains along two orthogonal directions of cross-section of the system). The system is stretched by applied force $\vec{F}$ .

(b) Vector $\vec{l}_{\vec{n}}$ of orientation of a chain segment located in the node $\vec{n}$ with Cartesian $(x,y,z)$ and spherical $(\varphi,\ \theta)$ coordinates.

5th International Conference on Mathematical Modeling in Physical Sciences (IC-MSQuare 2016) IOP Publishing
Journal of Physics: Conference Series **738** (2016) 012100
doi:10.1088/1742-6596/738/1/012100

We assume that the energy of orientational interactions $H_{\vec{n}, \vec{m}}^{(i)}$ between segments located in nodes $\vec{n}$ and $\vec{m}$ of quasi-lattice depends only on the angle of their relative orientation (Keesom's energy). For the potential of dipole type $H_{\vec{n}, \vec{m}}^{(i)}=-K_{i} \cos \Phi_{\vec{n}, \vec{m}}$ the energy is proportional to cosine of spatial angle $\Phi_{\vec{n}, \vec{m}}$ between their axis as in Gotlib-Maksimov models for polymer systems [12]

$$
H_{\vec{n}, \vec{m}}^{(i)}=-K_{i} \frac{\left(\vec{l}_{\vec{n}}, \vec{l}_{\vec{m}}\right)}{l^{2}}=-K_{i} \frac{\left(u_{\vec{n}} u_{\vec{m}}+v_{\vec{n}} v_{\vec{m}}+w_{\vec{n}} w_{\vec{m}}\right)}{l^{2}},
\tag{1}
$$

where $u_{\vec{n}}, v_{\vec{n}}$ and $w_{\vec{n}}$ are projections on the coordinate axis of vector $\vec{l}_{\vec{n}}$ oriented along the kinematic unit located in the node $\vec{n}$ $(i=1,2,3)$.

Energetic-type parameter $K_{1}$ along "longitudinal" curvilinear direction $n_{1}$ of quasi-lattice describes the longitudinal orientational interactions and determines mean cosine of the angle between neighbour kinematic units [12-14]. Energetic-type parameters $K_{2}$ and $K_{3}$ characterize orientational interactions of neighbour kinematic units in transversal interactions $n_{2}$ and $n_{3}$ of quasi-lattice [13, 14]. Characteristic values for rigid as well as for flexible polymeric chains have been estimated in ref. [18]. During the deformations, parameter $K_{2}$ was calculated taking into account the dependence of chains interactions energy on relative displacements of chain segments [18]:

$$
K_{2}=K_{3}\left(\frac{r}{r_{0}}\right)^{-3}.
\tag{2}
$$

In equation (2) the parameter $r_{0}$ is the mean distance between neighbour segments of polymer in direction of force action that is along $n_{2}$ assuming equilibrium of configuration, $r=r_{0}+\Delta r$, where $\Delta r$ characterizes the change of segments' position during deformations. Energetic-type parameter $K_{3}$ keeps constant value during deformations.

Potential energy of the whole system taking into account elastic deformations of the substrate $H_{subs.}$ and interactions between nearest segments is described by the Stockmayer potential that is Lennard- Jones potential plus energy of dipole interactions is given by

$$
H=\sum_{i=1}^{3} \sum_{\vec{n}, \vec{m}} H_{\vec{n}, \vec{m}}^{(i)}+4 \varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right]+H_{\text {subs. }}.
\tag{3}
$$

In equation (3) $\varepsilon$ is the depth of the Lennard-Jones potential pit, $r$ is the distance between nearest segments of the polymer chains, $\sigma$ is the distance where the energy of interactions is zero.

### 3. Simulation algoritm

Within the framework of Monte-Carlo method we generate random process consisting of sequence of the system configurations. Using ensembles with the large enough number of configurations, one can calculate mean values of almost all equilibrium physical quantities.

Input parameters for the simulation of the system shown in figure 2 are chosen the following parameters: dimensions $N_{1}, N_{2}$ and $N_{3}$ of quasi-lattice (number of segments in the directions $n_{1}, n_{2}$ and $n_{3}$ ), the interaction parameters $K_{1}, K_{2}$ and $K_{3}$, and the number of Monte-Carlo steps. For calculations, all parameters having dimension of energy were normalized with respect to the parameter $K_{1} \sim 10^{-20} \mathrm{~J}$ [18], while all quantities determining the system dimensions were normalized using mean interatomic distance in the substrate $a \sim 10^{-10} \mathrm{~m}$. The normalized temperature is defined as $T^{*}=k_{\mathrm{B}} T / K_{1}=0.1$, where $k_{\mathrm{B}}$ is the Boltzmann constant, that corresponds to the value $T \sim 10^{2} \mathrm{~K}$.

For the simulation, we use the following method:
- The initial configuration of the system is determined by the following parameters: position of segments attached to the substrate are given as well as at the system boundary in the direction $n_{2}$ are prescribed, at the upper boundary that is in the direction $n_{1}$ the segments

are free. In the direction $n_3$ we assumed the periodic boundary conditions. So, in the $n_3$-direction the system is infinite. For a more rapid achievement of equilibrium state of the system at low temperatures, we assume parallel distributions of the chain segments, while for high temperatures the distribution is chaotic.

- The cycles of the Monte-Carlo steps with the Metropolis algorithm are given. We assume the quasistatic loading that is the system tends to equilibrium state at each step. Therefore, the calculated displacement of each segment under action of the external force $F$ is independent on its place in the quasi-lattice.
- Taking into account random re-orientations of segments (rotators) at each step of deformation, we determine the equilibrium state and calculate the energy of polymer part of the system for given temperature. For the simplicity, the energy of elastic strains of the substrate is assumed to be $H_{\text{subs.}} = k(\Delta x)^2/2$, where $k$ is the effective stiffness parameter.
- For small deformations, the applied force $F$ is proportional to the displacement of chain segments from their initial positions, in other words $F \sim \Delta x$. The work of external loads during deformations transforms to the energy change of the system: $A = -\Delta H$, where

$$
A = -\frac{F\Delta x}{2} = -\frac{E}{2} \cdot \left( \frac{\Delta x}{x_0} \right)^2 . \tag{4}
$$

In equation (4) $E$ is Young modulus, $x_0$ is the initial length of the system along the action of force $F$. As a result, using (4) it is possible to calculate $F$ and Young's modulus $E$ of the system in dependence on the deformation $\Delta x$.

## 4. Results and discussion
The calculated dependencies of force and Young's modulus on stretching of the system are presented in figures 3 and 4. It is clear that with the increase of deformations the surface coating gradually ceases to have an effect on the investigated parameters. With the decrease of the value of chain interactions $K_3$ along the direction, that is not subjected to extension the influence of the coating disappears more quickly, see figures 3 and 4.

![](./images/811153772381208577_4.jpg)

Figure 3. Applied normalized force $F \cdot a/K_1$ vs. relative strain $\Delta x/x_0$ for given values of parameters $K_1 = 1$ and: $K_3 = 0.1$ (curve 1), 0.05 (curve 2), 0.01 (curve 3); force $F \cdot a/K_1$ vs. strain $\Delta x/x_0$ with the Hooke law (curve 4).

![](./images/811153772381208577_5.jpg)

Figure 4. Normalized Young's modulus $E/E_0$ ($E_0$ is Young's modulus of the substrate) vs. relative strains $\Delta x/x_0$ for given values of the parameters $K_1 = 1$ and: $K_3 = 0.1$ (curve 1), 0.05 (curve 2), 0.01 (curve 3).

5th International Conference on Mathematical Modeling in Physical Sciences (IC-MSquare 2016) IOP Publishing
Journal of Physics: Conference Series **738** (2016) 012100
doi:10.1088/1742-6596/738/1/012100

Areas after the peaks in figure 3 can be explained by the break of bonds between adjacent polymer chains of the coating and increasing role during deformation of the substrate system. Similar curves "strain-stress" can be observed during the stretching of thin films of crystalline polymers such as gutta-percha and caoutchouc [19], where the behaviour is also related with the structural changes from ordered structure to amorphous one. The following coincidence of curves with lines is related with a dominant role of the substrate that is with Hooke's law and negligible influence of the coating. Effective Young's modulus of such systems decreases and tends to Young's modulus of the substrate (figure 4).

Changing the length of attached to substrate chains and their density it is possible to analyse the dependencies of elastic parameters on size of the system in one direction or on the number of the attached polymer chains per unit area of the surface. In the forthcoming works, we intend to analyse the system not only for tension and compression but also for the bending, that may be important for flexible substrates.

### Acknowledgements
The work is performed within the framework of the project "Methods of microstructural nonlinear analysis, wave dynamics and mechanics of composites for research and design of modern metamaterials and elements of structures made on its base" (grant № 15-19-10008 of by the Russian Science Foundation).

### References
[1] Boinovich L B, Emelyanenko A M 2008 *Russian Chemical Reviews* **77(7)** 583
[2] Vinogradova O I, Belyaev A V 2011 *J. Phys.: Condens. Matter* **23** 184104
[3] Zheng L, Wu X, Lou Z et al. 2004 *Chin. Sci. Bull* **49** 1779
[4] Bico J, Thiele U, Quere D 2002 *Colloid Surf. A: Physicochem. Eng. Asp.* **206(1-3)** 41
[5] Callies M, Quere D 2005 *Soft Matter* **1(1)**, 55
[6] Bhushan B, Jung Y 2011 *Progress in Materials Science* **56** 1
[7] Shirtcliffe N, McHale G, Atherton Sh et al. 2010 *Advances in Colloid and Interface Science* **161(1-2)** 124
[8] Zhang X, Shi F, Niu J et al. 2008 *J. Mater. Chem.* **18** 621
[9] Lisichkin G V, Fadeev A Yu 2003 *Chemistry of the grafted surface compounds* (Moscow: FIZMATLIT)
[10] Rigoberto C A et al. 2004 *Polymer Brushes: Synthesis, Characterization, Applications* (Weinheim: WILEY-VCH Verlag GmbH & Co. KGaA)
[11] Ageev A A, Aksenova I V, Volkov V A, Eleev A F 2012 *Fluorine notes* **4(83)**
[12] Gotlib Yu Ya, Maximov A V 1992 *Polymer Science A* **34(10)** 902
[13] Maksimov A V, Pavlov G M 2007 *Polymer Science A* **49(7)** 828
[14] Maksimov A V, Gerasimov R A 2009 *Physics of the Solid State* **51(7)** 1365
[15] Gerasimov R A, Maksimov A V, Petrova T O and Maksimova O G 2012 *Physics of the Solid State* **54(5)** 1002
[16] Petrova T O, Maksimova O G, Gerasimov R A and Maksimov A V 2012 *Physics of the Solid State* **54(5)** 937
[17] Maksimov A V, Gerasimov R A, Maksimova O G 2012 *Ferroelectrics* **432(1)** 32
[18] Maksimova O G, Maksimov A V 2003 *Polymer Science A* **45(9)** 859
[19] Askadskii A A 1973 *Deformation of polymers* (Moscow: Khimiya)
5