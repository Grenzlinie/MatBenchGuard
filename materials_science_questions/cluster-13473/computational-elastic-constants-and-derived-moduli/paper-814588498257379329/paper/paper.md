Ferrogels cross-linked by magnetic particles: Field-driven deformation and elasticity studied using computer simulations

Rudolf Weeber', Sofia Kantorovich', and Christian Holm'

Citation: *The Journal of Chemical Physics* **143**, 154901 (2015); doi: 10.1063/1.4932371
View online: http://dx.doi.org/10.1063/1.4932371
View Table of Contents: http://aip.scitation.org/toc/jcp/143/15
Published by the American Institute of Physics

![](./images/814588498257379329_1.jpg)

THE JOURNAL OF CHEMICAL PHYSICS 143, 154901 (2015)
![](./images/814588498257379329_2.jpg)

# Ferrogels cross-linked by magnetic particles: Field-driven deformation and elasticity studied using computer simulations

Rudolf Weeber, $^{1,a)}$ Sofia Kantorovich, $^{2,3,b)}$ and Christian Holm $^{1,c)}$

$^{1}$Institut für Computerphysik, Universität Stuttgart, Allmandring 3, 70569 Stuttgart, Germany
$^{2}$Ural Federal University, Lenin Ave. 51, 620083 Ekaterinburg, Russia
$^{3}$Universität Wien, Sensengasse 8, 1090 Wien, Austria

(Received 9 June 2015; accepted 23 September 2015; published online 19 October 2015)

Ferrogels, i.e., swollen polymer networks into which magnetic particles are immersed, can be considered as “smart materials” since their shape and elasticity can be controlled by an external magnetic field. Using molecular dynamics simulations on the coarse-grained level, we study a ferrogel in which the magnetic particles act as the cross-linkers of the polymer network. In a homogeneous external magnetic field, the direct coupling between the orientation of the magnetic moments and the polymers by means of covalent bonds gives rise to a deformation of the gel, independent of the interparticle dipole-dipole interaction. In this paper, we quantify this deformation, and, in particular, we investigate the gel’s elastic moduli and its magnetic response for two different connectivities of the network nodes. Our results demonstrate that these properties depend significantly on the topology of the polymer network. © 2015 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4932371]

## I. INTRODUCTION

Polymer gels combined with magnetic nanoparticles are composite soft materials whose elastic properties can be controlled by external magnetic fields. $^{1}$ In the last decade, an active research in this area put forward several terms to characterise these materials: magnetoelastomers, ferrogels magnetic gels, etc. These materials gained attention both in fundamental research and applications, as they combine the intrinsic properties of a hydrogel with a relatively high sensitivity to magnetic fields inherent to magnetic fluids. $^{2}$ Of particular importance is the potential to change the shape and mechanical characteristics of a ferrogel by applying a relatively weak magnetic field. $^{3-8}$

The ability to control the shape of a magnetic gel gave rise to a number of new applications. Among them are drug delivery, $^{9,10}$ actuation, $^{11,12}$ and transport. $^{13,14}$

On a microscopical level, three ingredients need to be considered: the magnetic fluid, the polymer network, and the coupling between them. First, magnetic fluids (ferrofluids) have been available for decades. They have been studied extensively experimentally and theoretically and are used in technical and medical applications. $^{15-17}$ The magnetic nanoparticles typically have a size on the order of 10 nm and hence consist of a single ferromagnetic domain. This implies that they carry a permanent magnetic moment. Due to Brownian motion, the magnetic particles in a ferrofluid are randomly oriented and the fluid as a whole does not exhibit a net magnetic moment. This changes, once an external field is applied, and the magnetic moments in the fluid can align to it. There are two mechanisms by which this can occur: $^{18}$ the magnetic moments of the particles can re-align internally, without a rotation of the particle as a whole (Néel mechanism), or the particles as a whole can rotate to align their moments (Brownian mechanism). In the case of magnetic gels, it is of particular importance to know which mechanism is present, because only for the Brownian mechanism a direct coupling between the orientation of the magnetic moments and the polymers is possible. Moreover, one can also study ferrogels, where the magnetic nanoparticles have a uniaxial magnetic anisotropy. $^{19,20}$

Looking at the second ingredient, hydrogels, i.e., water-filled polymer networks, are common in everyday applications such as contact-lenses, food, and medical items. $^{21-24}$ They can be synthesized from a wide range of polymers and their chemical and physical properties can be tailored to suite the applications. For instance, by varying the degree of cross-linking between the polymers, their stiffness can be controlled. Also, hydrogels can be made sensitive to environmental factors such as temperature and pH-value. In the context of magnetic gels, it is particularly important to distinguish between the type of cross-linking between the polymers. This can be either due to comparatively weak interactions such as van der Wals forces and hydrogen bonds, or it can be due to covalent bonds. While the links between the polymers are dynamically changing in the first case, in the latter case, the bonds are stable and the network topology does not change over time. Simulations of hydrogels have been performed, but the literature is by far not as extensive as for polymer solutions. $^{25}$

The third thing to be considered when studying a ferrogel is the coupling between the polymers and the magnetic particles. One possibility is a loose coupling by means of hydrogen bonding or van der Waals interactions. In this case, the magnetic particles can exert a stress on the polymer matrix as they move, but the rotational degree of freedom of the nanoparticles is not directly coupled to the polymers. A rotational coupling between the nanoparticles

a)weeber@icp.uni-stuttgart.de
b)sofia.kantorovich@univie.ac.at
c)holm@icp.uni-stuttgart.de

0021-9606/2015/143(15)/154901/11/$30.00
143, 154901-1
© 2015 AIP Publishing LLC

and the polymers can be achieved by binding the polymers covalently to specific spots on the surface of the magnetic nanoparticles. $^{26-28}$ When the particles rotate due to an external field, the polymers wrap around the particles. This, in turn creates a stress on the polymer chain which leads to a shrinking of the gel. A sketch illustrating this mechanism can be found in Fig. 1. In this case, the magnetic particles act as actual cross-linkers of the network. $^{29}$

In this paper, we consider such a magnetic nanoparticle cross-linked gel, which due to the covalent bonds has a network topology which is constant over time. The magnetic moments are assumed to relax via the Brownian mechanism, i.e., by a rotation of the particle as a whole.

Since many applications of ferrogels are connected to actuation in an external magnetic field, it is crucial to understand the microscopic mechanisms by which the gels are deformed. First, in a field gradient, the magnetic particles tend to accumulate in regions with a stronger field. $^{3}$ Second, in a homogeneous field, a deformation can occur due to a change of the interactions between the magnetic particles as they are aligning in an external field. The dipole moments in the gel system are randomly oriented in the field-free case, and there is on average only a weak interaction between them, which is not strong enough to overcome the elasticity of the polymer matrix. The interaction between magnetic particles can become significant, however, as their moments are aligned in a field. Due to this change in interaction, the particles rearrange and thereby deform the matrix. This is the microscopic equivalent of the fact that a homogeneously magnetized elastic medium elongates in field direction in order to reduce its demagnetization field. $^{30-32}$ This mechanism was observed, e.g., in Ref. 4. It is noteworthy that the type of local particle configuration influences the response to a field. $^{33,34}$ Finally, a third deformation mechanism arises from a direct coupling of the orientation of the magnetic moments to the polymers as described above. A detailed study on the interaction between two magnetic particles connected by a polymer chain in this way can be found in Ref. 35.

In our earlier work, $^{7}$ we presented two gel models in two dimensions, which deform by the second and third mechanisms, respectively. For the case of a gel cross-linked by magnetic particles (model II in Ref. 7), an isotropic shrinking can be observed. This is, because in 2D, there is only one rotation axis, namely, the one perpendicular to the model plane. Once the magnetic particle is rotated by the field, all chains attached to it receive the same amount of stress. In Ref. 36, however, we have shown that the shrinking is no longer isotropic in three dimensions. This can be explained by the effect that the rotation always takes place around an axis which is perpendicular to both the magnetic moment prior to alignment and the direction of the external magnetic field. Polymer chains that are attached within a plane spanned by these two vectors and that are going through the particle's center follow the full rotation of the magnetic particle. Chains attached parallel to the rotation axis, on the other hand, are not affected by the particle's rotation. Prior to the alignment by a

![](./images/814588498257379329_3.jpg)

FIG. 1. Sketch of magnetic nanoparticles in a gel. Upper row ((a) and (b)): 2D model, left without an applied external field, right with an applied external field, as marked with the red arrow. One can see four polymer chains rigidly bound to specific spots (light blue, virtual sites) on the surface of a magnetic nanoparticle. When a field is applied and the magnetic particle aligns its dipole to it, the polymer chains wrap around the particle. This exerts a stress on the chain, which leads to a shrinking of the ferrogel (isotropic in 2D). Lower row ((c) and (d)) 3D model, left without an external field, right with an external field applied. In sketch (c), a 4-fold (diamond) and 6-fold (cubic) cross-linker is shown. In sketch (d), an external magnetic field $H$ is applied within the plane, as shown with the red arrow. Notice that only chains within the plane are subjected to the deformation, the polymer chains perpendicular to the plane are not affected. This leads to an anisotropic shrinking of the gel in 3D.

field, the magnetic moments of different particles are random, but the rotation axis around which the alignment takes place is always perpendicular to the external field. Hence, there is less deformation in the directions perpendicular to the field. A sketch explaining this mechanism can be found in Fig. 1.

In contrast to our previous works, we present here a detailed quantitative study of the deformation, elasticity, and magnetic response of a three-dimensional gel cross-linked by magnetic particles, which has been investigated in depth in the Ph.D. work of the first author. $^{37}$ We consider two topologies of networks, a simple cubic (SC) network with sixfold connectivity and a diamond cubic (DC) topology with fourfold connectivity. The paper is structured as follows: In Sec. II, we describe the simulation technique used, and then introduce the model. Thereafter, the equilibrium degree of swelling of the gel is obtained (Sec. III). In Sec. IV, the gel's deformation in a field is determined. Sec. V deals with the system's elastic constants and in Sec. VI, the magnetic response is examined. We conclude the paper with a summary.

## II. SIMULATION TECHNIQUE

In this paper, we study the deformation of three-dimensional magnetic gels cross-linked by magnetic nanoparticles in a magnetic field. This is done by means of molecular dynamics simulations on a coarse-grained level, using the ESPResSo software: $^{38,39}$ rather than considering individual atoms as degrees of freedom, the smallest units considered in the simulations are the units of polymer that roughly match one Kuhn length, and the magnetic nanoparticles. In this way, the number of degrees of freedom in the system is reduced to a point, at which it is possible to simulate several meshes of the gel in each Cartesian direction. The simulations are performed in the canonical NVT ensemble using a Langevin thermostat. For each translational degree of freedom, the equation of motion is
$$
m \ddot{x}=-\gamma \dot{x}+F+F_{\text {random }}, \quad(1)
$$
where $m$ denotes the mass, $\gamma$ the friction coefficient, $F$ the force due to other particles, and $F_{\text {random }}$ a random force mimicking collisions with the surrounding solvent. According to the fluctuation-dissipation theorem, in order to maintain a thermal energy of $k_{B} T$, each random force component has to have a mean of zero and a variance of
$$
\left\langle F_{\text {random }}^{2}\right\rangle=2 k_{B} T \gamma. \quad(2)
$$

Rotational degrees of freedom are treated in a similar way. In Eq. (1), position, mass, and force are replaced by orientation, inertial tensor, and torque, respectively. $^{40}$

The polymer chains are represented as bead-spring models, in which the beads are bound by harmonic potentials
$$
U_{\text {harmonic }}(r)=\frac{1}{2} k\left(r-r_{0}\right)^{2}, \quad(3)
$$
where $k$ is the spring constant and $r_{0}$ the equilibrium distance.

Both the beads forming the polymer chains and the magnetic particles are represented as soft spheres interacting via a purely repulsive Lennard-Jones interaction, the so-called Weeks-Chandler-Andersen (WCA)-potential. $^{41}$ Its functional form is given by
$$
U_{W C A}= \begin{cases}4 \epsilon\left[\left(\frac{\sigma}{r_{i j}}\right)^{12}-\left(\frac{\sigma}{r_{i j}}\right)^{6}\right]+\epsilon & r<r_{c}, \\ 0 & r \geq r_{c}\end{cases}\quad(4)
$$
where $\epsilon$ controls the energy scale of the potential, $\sigma$ is the sum of the radii of the interacting beads, and $r_{c}=2^{1 / 6} \sigma$ denotes the cut-off distance after which the potential is zero.

The anchoring point of the covalent bonds between the magnetic nanoparticle and the polymer chains attached to it is modelled using the virtual site feature of ESPResSo. $^{39}$ Virtual sites are particles whose positions are not determined by integrating an equation of motion, rather they are calculated from the position and orientation of other particles. In this particular case, a virtual site is placed immediately under the surface of the magnetic nanoparticle to form a binding site for the attached polymer. The latter is rigidly connected to the magnetic particle and will follow both its translational and rotational motion. The technical details can be found in the Appendix of Ref. 7 as well as in Ref. 39. A sketch of a magnetic particle with the attached polymer chain can be found in Fig. 1.

The magnetic particles, forming the nodes of the network, are initially placed on a regular three-dimensional lattice. Then, the chains are attached to a specific point on the nodes' surface. Therefore, when the node particles rotate, the chain ends have to follow. Before the chains are connected, the dipole moments of the node particles are randomized to make the system isotropic. The system is studied taking into account only the dipole-field interaction, but not the dipole-dipole interaction. We can neglect the latter for three reasons: first, the density of magnetic particles is relatively low, so that the influence of the dipole-dipole interaction is rather weak. This was checked in the 2D case discussed in Ref. 7. Second, the inclusion of the dipole-dipole interaction could result in two deformation mechanisms occurring at the same time, which would make it more difficult to attribute findings to a specific mechanism. Third, for particles placed on a regular lattice, the kind of deformation due to dipole-dipole interactions depends on the lattice structure. $^{42}$ In order to avoid artefacts, these interactions should therefore only be included in a more randomized system.

In this work, two simple choices for an initial lattice are considered. These are the DC and SC geometries. In the former case, four chain ends are connected to each node, while there are six in the latter case. By switching from the diamond cubic to the simple cubic structure, one can thus vary the degree of connectivity (and in consequence the elastic and magnetic response) of the network.

In contrast to the 2D case, which we studied in model II of Ref. 7, periodic boundary conditions are applied, in order to reduce surface effects, and to study a truly macroscopic gel. Snapshots of samples after equilibration are shown in Fig. 2 for the DC and SC lattice. The simulation parameters are as follows: the gel consists of $N_{n}=64$ node particles as well as $N_{c}^{\mathrm{dc}}=2 N_{n}$ chains in the diamond cubic structure, or $N_{c}^{\mathrm{sc}}=3 N_{n}$ chains in the simple cubic structure. The chains consist of 60 or 80 beads, with a diameter of $\sigma_{c}=1$, whereas

![](./images/814588498257379329_4.jpg)

FIG. 2. Snapshot of a gel sample at equilibrium swelling in the diamond cubic geometry with four chains attached to a node left and the simple cubic geometry with six chains attached to a node right. Consisting of 60 beads, the chains are connected to specific spots on the surface of the magnetic particles. In the field-free case, depicted here, the magnetic moments are randomly aligned.

the node particles have a diameter of $\sigma_n = 10$. The scale of the soft sphere interaction Eq. 4 is $\epsilon = 10$. The bonds between neighboring particles in a chain as well as between the ends of the chains and the virtual sites interact via a harmonic potential Eq. 3 with an equilibrium elongation of $2^\frac{1}{6}\sigma$, coinciding with the cutoff of the WCA-potential. The spring constant of the harmonic potential is $k = 10$.

As the shape of the gel for the given parameters is not known a priori, an iterative procedure is applied to adjust the box size. We begin with an estimated shape. Then, iteratively, the stress is calculated and the box is shrunk or expanded in each coordinate, according to the diagonal elements of the observed stress tensor. The orthogonal basis of the stress tensor coincides with the orientation of the simulation box. After the box shape is adjusted, a new simulation is performed. This is repeated, until the observed stress approaches zero with the desired tolerance. When the gel can be assumed to be isotropic, i.e., when no external field is applied, an optimized procedure can be used, which will be explained in Sec. III. Even in the field free case, there will be a small anisotropy in an individual sample of the gel, because the sum of the randomly drawn initial dipole moments is never exactly zero. The stress is computed and averaged for several instances of the system at any given set of parameters to compensate for this. In other words, the simulation is divided into the following steps:

1. The magnetic node particles are placed on the lattice with random dipole orientations. The distance between the surfaces of adjacent nodes is such that the chains can be inserted in an elongated configuration. Hence, the resulting initial lattice constant is
$$
a = \sigma_n + l_c \sigma_c, \tag{5}
$$
where $\sigma_n$ and $\sigma_c$ are the Lennard Jones diameters of the node and chain particles, and $l_c$ is the number of particles in a chain.

2. Chains are connected to the surface of two adjacent nodes. Four chain ends are connected to a node in the diamond cubic case and six in the simple cubic case.

3. After the network is cross-linked, it is scaled to the desired shape. This is done by adjusting the box size in 400 steps from the initial shape to the target shape. After each deformation step, the system is equilibrated with the Langevin thermostat for 100 iterations of time step $dt_{\text{reshape}} = 0.0006$ to disperse the energy introduced by the deformation.

4. When the final shape is reached, the system is equilibrated further for 200 000 steps of size $dt = 0.01$, again using the Langevin thermostat.

5. Finally, observables can be calculated. The time step is again $dt = 0.01$ and the stress is calculated every 20 time steps, whereas the magnetization is obtained every 100 000 steps. In a typical simulation, more than 50 000 stress observations are taken. This enormous amount of statistics is needed due to the large fluctuations of the measured stress due to the softness of the material.

### III. EQUILIBRIUM SWELLING

When a gel with specific topology, chain length, and interaction parameters is to be studied, the equilibrium swelling, and hence the box size, is not known a priori. Therefore, the first step in the analysis of the system is to determine this property in the field-free case. In principle, it is possible to do this by simulating in the $NPT$-ensemble using a barostat. However, this was found not to be efficient.⁴³ Instead, a set of simulations in the $NVT$-ensemble is performed at different volumes. By computing the stress tensor and averaging over its diagonal elements, the stress-strain relation for the gel is obtained,
$$
P(\epsilon) = \frac{1}{3} \sum_i S_{ii}, \tag{6}
$$
where $P(\epsilon)$ denotes the isotropic pressure at a certain strain $\epsilon$ and $S_{ij}$ denote the elements of the stress tensor. From this curve, the equilibrium strain, at which the stress is zero, can be estimated by linear interpolation. Taking the box length

![](./images/814588498257379329_5.jpg)

FIG. 3. Stress-strain relations for both the diamond cubic (filled symbols) and the simple cubic (open symbols) geometry. The x-axis is rescaled such that unity represents the equilibrium volume for the given geometry and chain length. From the respective slopes of the stress-strain relations at the point of equilibrium swelling, the elasticity of the samples can be determined. It can be seen that for both chain lengths shown, the samples in the diamond cubic geometry are softer than those in the simple cubic geometry. Additionally, longer chains make the gel more deformable.

of the initial system to be unity, with completely stretched polymers, the following equilibrium swelling was obtained: for the diamond cubic lattice, values of 0.2790 and 0.2546 are found for chains with 60 and 80 beads, respectively. The values for the simple cubic structure are 0.3153 and 0.2742. It is convenient to express the size of the gels in terms of this equilibrium swelling. This will be done throughout the rest of the paper.

In Fig. 3, the stress-strain curves for both DC and SC geometries are shown. From the slope of the curves at the equilibrium strain, the stiffness of the gel can be deduced. The higher the slope, the stiffer the material is. It can be seen that the gel in the SC geometry is more stiff than in the DC geometry. Also, a decrease of the chain length results in a stiffer system. Both these observations can be understood by noting the higher particle density for shorter chain lengths and for a larger number of chains. A quantitative study of the elastic constants will follow in Sec. V.

## IV. ANISOTROPIC DEFORMATION

In this section, the deformation of the gel under the influence of an external field will be discussed. In particular, we will have a closer look at the anisotropic deformation described in Ref. 36. As the first step, we estimate the tendency of the gel to deform in the directions parallel and perpendicular to the field, due to the wrapping of the polymer chains around the magnetic particles (Fig. 1). In order to separate this wrapping effect from the elastic properties, we first obtain the direction-dependent stress due to an external field in the non-deformed gel. Hence, the gel is simulated in the NVT-ensemble at the equilibrium volume for the field free case as it was determined in Sec. III. Then, a field is applied and the stress in the directions parallel and perpendicular to the field is determined. The results for chain lengths of 60 and 80 beads, and for both, the DC and SC geometry, are shown in Fig. 4. Throughout this paper, magnetic fields are expressed in terms of the Langevin parameter

$$
\alpha=\frac{\mu_{0} m H}{k_{B} T}, \quad(7)
$$

where $m$ denotes the particles' moment, $\mu_{0}$ the vacuum permittivity, and $H$ the external field. This parameter measures the ratio between the Zeeman energy and the thermal energy $k_{B} T$. The stresses for all applied external magnetic fields larger than zero are negative, indicating that the gels would contract if the constraint of the constant volume would be removed. The absolute value of the stress in the direction parallel to the field is significantly larger than the one found in the perpendicular direction. It is also worth noting that the stress is significantly stronger in the SC geometry, where six chains are connected to a node as opposed to four in the DC geometry. This implies that two contradicting forces are at play. On the one hand, in the simple cubic structure, there are more chains attached to a node. This leads to a stronger wrapping effect and a stronger tendency of the system to deform in the field. On the other hand, from the slope at the equilibrium swelling in Fig. 4, it can be observed that the gel based on the simple cubic structure is stiffer than the one based on the diamond structure. From the deformation of the gel, it turns out that for this particular model, the elasticity dominates the deformation behaviour.

![](./images/814588498257379329_6.jpg)

FIG. 4. Stress parallel and perpendicular to the external field versus the strength of the external field. Data are shown for the diamond cubic (DC, full symbols) and simple cubic (SC, open symbols) geometry and for chain lengths (cl) of 60 and 80 beads per chain. It can be seen that in both geometries, the absolute value of the stress parallel to the field is larger than the value found in the perpendicular direction. A much larger negative stress is observed in the simple cubic geometry than in the diamond cubic one.

To find the equilibrium shape of the gel for a given external magnetic field, simulations in the NVT-ensemble are executed iteratively. In each simulation, the stress is calculated in the directions parallel and perpendicular to the external field. Then, the box size for the next simulation is altered according to the stress. This procedure is repeated until the remaining stress approaches zero within the chosen error tolerance. The details of the procedure are as follows:

- A shape of a simulation consists of the lengths of the simulation box parallel and perpendicular to the external field.

![](./images/814588498257379329_7.jpg)
![](./images/814588498257379329_8.jpg)

FIG. 5. (a) Length of the gel in the directions parallel and perpendicular to an externally applied magnetic field versus the strength of that field. (b) Relative loss of volume of a gel versus the strength of the external field. Full symbols denote the diamond cubic (DC) geometry, whereas open symbols are used for the simple cubic (SC) one. Black and red symbols are used for the directions parallel and perpendicular to the field, respectively. The chain length (cl) was 60 (squares) and 80 (circles), respectively. It can be seen that the overall shrinkage is comparable in magnitude for all systems considered within the simulation error, which, however, is large. While all samples shrink significantly more in the direction parallel to the field, it is noteworthy that the gels in the simple cubic geometry shrink less in the direction parallel to the field, but more in the perpendicular direction than those in the diamond cubic geometry. This results in a similar change of volume in all systems, although the "shape" of the deformation depends strongly on the network geometry.

- For each shape simulated, the stress is averaged over 24 simulations to reduce the statistical error.
- Initially, two sets of simulations are performed for a given external magnetic field. The gel samples in them have manually selected shapes, of which one is above and the other is below the expected equilibrium shape for the given field. For these shapes, the corresponding stresses in the direction parallel and perpendicular to the field are obtained.
- In all further iterations, a single new shape consisting of a box length parallel and perpendicular to the field is generated. For the respective directions parallel and perpendicular to the field, a new box length is generated from the two ones examined in the previous iterations which yielded the lowest corresponding absolute stress. From these box lengths and corresponding stresses, a linear stress-strain relation is constructed, which is used to extrapolate to the point where the stress would be zero according to this relation. Due to large statistical errors in the stress calculations, it is necessary to restrict the change in box length to approximately two percent per iteration to keep the procedure stable. For this new shape, again, the stress is measured in the directions parallel and perpendicular to the external magnetic field.
- The iteration is terminated, if the stress in both the direction parallel and perpendicular to the field is below $10^{-5}$.

The iterative procedure provides satisfactory results but requires a large amount of computational resources and occasional manual interventions. In a future study, more sophisticated procedures, like genetic optimizations, might be considered. As an alternative to the iterative procedure, it is also possible to simulate a set of shapes around the expected equilibrium shape, obtain the corresponding stresses, and fit a linear stress-strain model to the data. This is done in conjunction with the estimation of elastic constants in Sec. V.

To study the deformation of the gel in an external magnetic field, the equilibrium shapes were determined for fields up to $\alpha = 60$ in terms of the Langevin parameter. Results for chain lengths of 60 and 80 beads are shown in Fig. 5(a) for gels based on both the diamond cubic and simple cubic network structure. It can be seen that, as expected from the anisotropic stress at constant volume (Fig. 4) and as explained above, the gel deforms significantly more in the direction parallel to the external field than in the perpendicular direction. The deformation decreases when the chain length is increased. This can be explained by noting that, as the node particles align to the external field, the chains attached to the node are effectively shortened. The entropic effect of this shortening is more significant for a short chain than for a long one. While a long chain can slightly uncoil to accommodate for the motion of its ends, a short chain will be forced into a rather straight configuration, which is entropically very unfavorable.

The influence of the network geometry (diamond cubic vs. simple cubic) on the amount of shrinkage is determined by three factors. First, more chains attached to a node lead to a higher stress, when a field is applied, as more chains get stretched by the node particles' rotation. Second, more chains lead to a higher density of particles in the system, and therefore also a higher stiffness. Finally, a contraction in one direction in most materials leads to an expansion in the perpendicular directions. The strength of this expansion in the direction perpendicular to the stress is characterized by the Poisson ratio (Eq. (14)), which also depends on the network geometry.

As can be seen from the plot of the gel's equilibrium shape versus the field (Fig. 5(a)), the amount of shrinkage in the direction parallel to the field is larger for the diamond cubic geometry than for the simple cubic one. In the direction perpendicular to the field, gels based on the diamond cubic geometry expand slightly, while they contract when based on the simple cubic geometry. The relative shrinkage, i.e., the loss of volume due to an applied field, divided by the volume in the field free case is given by

$$
\frac{\delta V(\alpha)}{V_{0}}=1-\frac{l_{\|}(\alpha) l_{\perp}(\alpha)^{2}}{l_{0}^{3}}, \tag{8}
$$

where $l_{\|}(\alpha)$ and $l_{\perp}(\alpha)$ denote the length of the gel parallel and perpendicular to an external magnetic field with a Langevin

parameter of $\alpha$, and $l_0$ denotes the length of the gel in the field free case, which is equal in all Cartesian directions. The shrinkage for gels based on the diamond cubic and simple cubic geometries and chain lengths of 60 and 80 beads is shown in Fig. 5(b). It can be seen that the shrinkage is of similar magnitude for all systems considered, even though the actual shape of the gel (Fig. 5(a)) depends strongly on the network geometry. The similarity of the shrinkage stems from the fact that, while the simple cubic gels shrink less in the direction parallel to the field than the diamond cubic ones, they shrink more in the perpendicular direction.

## V. ELASTIC CONSTANTS AND POISSON RATIO

To gain an understanding of the deformation of magnetic gels in external fields, it is not only necessary to study the underlying mechanism. Additionally, the elastic properties of the material need to be considered, as they determine, to what degree the material will deform under a given stress. Additionally, in an external magnetic field, not only the shape of a magnetic gel can change but also its elastic properties. Hence, in this section, the change in these elastic constants will be examined for our two gel models. The resulting stress can be assumed to be linear in the strains, if the strains are sufficiently small. In this case, the elastic constants describe what kind of stress is observed in a system, when a certain strain or shear is applied. When only the linear strain but no shear is considered, the elastic constants can be written down in matrix form as follows:

$$
C = \begin{pmatrix}
c_{xx} & c_{xy} & c_{xz} \\
c_{yx} & c_{yy} & c_{yz} \\
c_{zx} & c_{zy} & c_{zz}
\end{pmatrix},
\tag{9}
$$

where the first index denotes the direction of the stress response and the second index denotes the direction of a strain. Then, for a given strain in $x$, $y$, and $z$-directions

$$
\epsilon = \begin{pmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz}
\end{pmatrix},
\tag{10}
$$

the resulting stress is

$$
\sigma = C\epsilon.
\tag{11}
$$

Hence, to describe the elastic properties of the gel in the linear response regime, the elasticity matrix $C$ has to be determined.

Depending on the symmetry of the system, some of the entries of the elastic matrix $C$ are identical. For an isotropic material, there are only two free parameters, namely, the diagonal and the off-diagonal elements of $C$. The diagonal elements describe the stress in the direction parallel to the strain, whereas the off-diagonal elements describe the strain in the perpendicular direction. We have

$$
C = \begin{pmatrix}
a & b & b \\
b & a & b \\
b & b & a
\end{pmatrix}.
\tag{12}
$$

This situation applies to the gel, when no external field is applied.

When, on the other hand, a field is applied, a distinction needs to be made between the direction parallel to the field and the two Cartesian directions perpendicular to it. When the external magnetic field is parallel to the $x$-direction, the resulting elastic matrix has the from

$$
C_{\text{field}} = \begin{pmatrix}
a & b & b \\
c & d & e \\
c & e & d
\end{pmatrix}.
\tag{13}
$$

As it can be seen, there are five independent elastic constants. The constant $a$ describes the stress parallel to the field for a strain parallel to the field, $b$ describes the stress parallel to the field for a strain perpendicular to the field, and $c$ describes the stress perpendicular to the field for a strain parallel to the field. The symbol $d$ describes the stress parallel to a strain which is applied perpendicular to the field. Finally, $e$ describes the stress in a direction perpendicular to the field, when the strain is applied along the second Cartesian direction perpendicular to the field.

In this paper, the elastic constants are obtained by numerically calculating the derivatives of the stress tensor by running simulations at different strains close to the equilibrium strain, measuring the stress, and fitting a linear model to the resulting data. The technical details of this procedure can be found in the supplementary material. $^{44}$

The elastic constants are obtained for gels based on both the simple cubic and the diamond cubic network geometries with a chain length of 60 beads. Values are obtained for the field-free case as well as for an external field of $\alpha = 20$. Even when no field is applied, no additional constraints are applied to the elasticity matrix.

In Fig. 6, the elastic constants are compared for gels in the simple cubic and diamond cubic geometries. It can be seen that gels in the simple cubic geometry are significantly stiffer than those in the diamond cubic one. In particular, the elastic constants which describe a stress occurring parallel to a strain ($a$ and $d$ in Eq. (13)) are approximately four times larger. The off-diagonal elements of the elasticity matrix ($b$, $c$, and $e$) are only higher by $10\%$-$25\%$ in the simple cubic geometry.

In Fig. 7, the elasticity of a gel in an external field ($\alpha = 20$) is compared to that of a gel with no applied field. Data are presented for the DC and SC geometries, respectively. We observe that all ratios are larger than unity. Hence, the material is more stiff, when an external magnetic field is applied. This can be understood by noting that the gel shrinks in a field, and therefore the density of particles in the system is higher. It is notable that in the simple cubic geometry, the off-diagonal elements ($b$, $c$, and $e$) are increased more strongly than the diagonal elements ($a$ and $d$), when an external field is applied.

From the elasticity matrix, it is also possible to calculate the Poisson ratio for the investigated systems. For a prescribed strain in one direction, these ratios measure the resulting strain in the perpendicular directions. In the case of a system with one spacial direction, namely, the field direction, there are three different Poisson ratios: a prescribed strain in the field direction and a resulting strain in a non-field direction, a prescribed

![](./images/814588498257379329_9.jpg)

FIG. 6. Comparison of the elastic constants $a$-$e$ as defined by Eq. (13) for gels constructed in the diamond cubic and simple cubic geometries for the field-free case ($\alpha=0$). It can be seen that the absolute value of the constants for the simple cubic system is always larger than that for the diamond cubic one. This indicates a more rigid gel.

strain in a non-field direction and a resulting strain in the field direction, and a prescribed strain in a non-field direction and a resulting strain in the second non-field direction. The subscript $f$ and $n$ will be used to denote field and non-field directions, respectively. The first letter denotes the direction of the prescribed strain, whereas the second letter denotes the direction of the response. The Poisson ratio is positive, when a prescribed expansion leads to a contraction in the response direction. The field is assumed to be applied in $x$-direction. To obtain the Poisson ratio $p_{fn}$ for a prescribed strain in field direction and a resulting strain in a non-field direction, we apply the strain

$$
\vec{\epsilon}=\begin{pmatrix}
1 \\
-p_{fn} \\
-p_{fn}
\end{pmatrix}
\tag{14}
$$

to the system. Note that for a prescribed strain of unity, the resulting contraction in the perpendicular directions is the Poisson ratio. Now, to find the Poisson ratio, we require that for the given $\vec{\epsilon}$, the stress in the response directions has to be zero,

$$
C\vec{\epsilon}=\begin{pmatrix}
x \\
0 \\
0
\end{pmatrix},
\tag{15}
$$

where $C$ is the elasticity matrix. The stress occurring in the direction of the prescribed strain is irrelevant, so $x$ can take an arbitrary value. In other words, only the second and third rows of the equation have to be solved. Using Eq. (13) for the elasticity matrix $C$, we find

$$
p_{fn}=\frac{c}{d+e}.
\tag{16}
$$

The remaining two Poisson ratios, $p_{nf}$ and $p_{nn}$, can be obtained similarly. They are

$$
p_{nf}=\frac{b}{a+b}, p_{nn}=\frac{e}{d+e}.
\tag{17}
$$

![](./images/814588498257379329_10.jpg)

FIG. 7. Comparison of the elastic constants $a$-$e$ (Eq. (13)) of our model gel for the cases of no external field and an external field of $\alpha=20$. Results for the diamond cubic geometry are shown at the top (a), while results for the simple cubic geometry are shown at the bottom (b).

Based on these equations, the Poisson ratios for the gels can be calculated using the elastic constants shown in Fig. 7. The resulting ratios are shown in Fig. 8. Values are shown for networks based on the diamond cubic and simple cubic geometry, and for both, the field-free case and an external field of $\alpha=20$. In the field-free case, the system is isotropic, and thus the three Poisson ratios $p_{fn}$, $p_{nf}$, and $p_{nn}$ are expected to be equal. In the figure, however, a deviation of about 20% is visible due to statistical errors. It can be seen that the choice of directions for the prescribed strain and the observed response (field or non-field direction) does not have a strong influence on the Poisson ratio. The choice of network geometry — diamond cubic or simple cubic — on the other hand, has a strong influence on the Poisson ratio: a much higher value is observed for the diamond cubic geometry. The Poisson ratios also increase, when a strong magnetic field is applied.

In summary, a procedure has been described to obtain the elastic constants by fitting a linear elastic model to a set of stress-strain pairs. The elastic constants are found to be influenced mostly by the choice of network topology. In the diamond cubic case, the gel is much softer but has much larger Poisson ratios compared to the simple cubic case. The elastic

![](./images/814588498257379329_11.jpg)

FIG. 8. Poisson ratios $p_{fn}$, $p_{nf}$, and $p_{nn}$ for gel samples based on the diamond cubic (DC) and simple cubic (SC) geometries for external magnetic fields of $\alpha = 0$ and $\alpha = 20$. In the field-free case, all Poisson ratios for a given geometry are expected to be the same. The visible deviations are due to statistical noise. It can be seen that the direction of the prescribed strain as well as the direction of the observed response does not significantly influence the Poisson ratio. The Poisson ratio does, however, strongly depend on the network geometry. In the diamond cubic case, a much higher value is found.

constants turn out not to be strongly anisotropic, even when an external field is applied. The differences in Poisson ratio help to explain the differences in the deformation behaviour found for different network geometries (Fig. 5). In particular, the low shrinkage in the direction perpendicular to the field for the gel based on the diamond cubic geometry is related to the high Poisson ratio for this system: Due to the shrinkage in the direction parallel to the field, an expansion occurs in the perpendicular direction. Due to the high value of the Poisson ratio for this geometry, this compensates for the shrinkage which would otherwise occur due to the rolling-up of polymer chains around the magnetic particles.

## VI. MAGNETIC RESPONSE

In the model considered here, through the binding of the polymer chains to specific spots on the surface of the magnetic nanoparticles cross-linking the network, a coupling is created between the magnetic particles' orientation and the polymer matrix. This coupling is the basis of the deformation mechanism for this kind of magnetic gels. By means of the gel's magnetic response to an external magnetic field, further insights into the details of the deformation mechanism can be gained. In Fig. 9, the magnetization curve $M(\alpha)$ is shown for gels based on the diamond cubic and simple cubic geometries with chain lengths of 60 and 80 beads. The curve describes the component parallel to the magnetic field of the sum of all magnetic moments in the system for a given field expressed in terms of the Langevin parameter (Eq. (7)). Also shown is the Langevin law, which is the result expected for non-interacting dipoles, given by

$$
M_{\mathrm{l}}(\alpha)=\frac{\cosh \alpha}{\sinh \alpha}-\frac{1}{\alpha}. \tag{18}
$$

From the plot, it can be seen that the magnetization of the gels is always lower than the corresponding Langevin magnetization. This is due to the fact that the polymer chains get strained, when the magnetic particles rotate to align their dipole moments to the external field. The strain on the polymer chains causes a stress on them, which in turn creates a torque on the magnetic particles, which counteracts the magnetic field. This leads to a reduction in magnetization. The loss of entropy per chain, due to its stretching, increases for shorter chains. Thus, a larger stress occurs and the magnetization is lower for the sample with shorter chains. Also, the torque on the magnetic particles is larger, when more chains are attached to it. Hence, the magnetization is also lower for the gel based on the simple cubic geometry, in which six chains are connected to each node particle, compared to four chains attached in the diamond cubic geometry. It is noteworthy that, in a dense system, the reduction of magnetization caused by the presence of the polymer chains may be counteracted to a degree by magnetic interactions between the nanoparticles. The influence of these interactions on the magnetization curve can be estimated from mean field theory. $^{45}$ The magnetization is always enhanced, in particular, for high densities and large magnetic moments.

![](./images/814588498257379329_12.jpg)

FIG. 9. Magnetization curve for gels of the diamond cubic and simple cubic geometries for chain lengths of 60 and 80 beads, respectively. The solid line shows the magnetization curve expected for non-interacting dipoles in three dimensions (Langevin curve). It can be seen that the magnetization for all gels considered is below that of non-interacting dipoles. As soon as the field aligns the magnetic node particles of the polymer network, a stress is created on the polymer chains. Due to this stress, the polymer chains exert a torque on the magnetic particle which acts against the alignment to the external field. The torque counteracting the magnetization is larger, if the chains are shorter, and if there are more chains. Thus, a lower magnetization is observed for the case of 60 beads as well as the case of the simple cubic network geometry.

## VII. SUMMARY

In this paper, we presented a detailed study of the deformation mechanism in a magnetic gel which is cross-linked by magnetic nanoparticles. The deformation mechanism described arises from a direct coupling of the orientational degree of freedom of the magnetic moments to the polymer chains. When an external field is applied, the magnetic nanoparticles rotate and exert a stress on the polymer chains attached to them. This, in turn leads to a contraction of the matrix. The model, which we study by means of coarse-grained molecular dynamics, is inspired by an experimental system discussed in Ref. 27. In the three dimensional case, which is the focus of this report, an anisotropic deformation is observed. While there is a strong shrinkage in the direction parallel to the field, the shrinkage in the perpendicular directions is either small or not present at all depending on the network topology.

A comparison was made between two network topologies, one with four chains and another one with six chains connected

to a node. In these topologies, the nodes are arranged in a diamond cubic and simple cubic geometry, respectively. An increase of the number of chains connected to a node has two effects. On the one hand, it increases the stress on the gel caused by an alignment of the magnetic particles to the external field. This, on its own, should lead to an increased shrinkage of the gel. However, at the same time, the higher number of chains results in a higher particle density in the model gel, which should lead to a lower shrinkage. For the systems studied here, there is a stronger shrinkage, when four chains are attached to a node. As this result is presumably highly dependent of the details of the model, it is conceivable that the trade-off between the two mentioned trends can lead to a different behaviour for a system with, for instance, significantly lower overall density. Elastic properties were studied by fitting a linear elasticity model to a set of strain pairs. We found a significantly higher stiffness for the more strongly cross-linked gels in the simple cubic structure, as well as an increase of the stiffness when a field is applied.

The magnetic response of the model gel which is cross-linked by magnetic particles is strongly influenced by the coupling between the orientation of the magnetic nanoparticles and the polymers. As the alignment of the magnetic particles to an external field exerts a stress on the polymers, there is an additional energy penalty for this alignment. In consequence, the magnetic response of the gel is below that of non-interacting magnetic particles.

In summary, a detailed study of the deformation, elasticity, and magnetic response of a particle-cross-linked ferrogel was performed using simulations. Based on the results, we have shown that the overall deformational response is determined by an interplay between the gel's degree of cross-linking and its elasticity. In the future, we plan to extend the model by introducing randomness into the chain lengths and the connectivities. Additionally, in experimental systems, different deformation mechanisms might occur at the same time. This would be the case for gels, which are cross-linked by magnetic particles with a very high magnetic moment and at a high density.

## ACKNOWLEDGMENTS

R.W. and C.H. are grateful for financial support from the DFG through the SPP 1681. In addition, we acknowledge funding through the cluster of excellence EXC 310, SimTech, and access to the computer facilities of the HLRS and BW-UniCluster. S.K. was supported by Austrian Science Fund (FWF): START-Project No. Y 627-N27 and RFBR Grant No. mol-a-ved 12-02-33106.

¹L. Barsi, A. Büki, D. Szabo, and M. Zrinyi, "Gels with magnetic properties," Prog. Colloid Polym. Sci. 102, 57 (1996).

²R. E. Rosensweig, Ferrohydrodynamics (Cambridge University Press, Cambridge, 1985).

³M. Zrinyi, L. Barsi, and A. Büki, "Deformation of ferrogels induced by nonuniform magnetic fields," J. Chem. Phys. 104, 8750 (1996).

⁴C. Gollwitzer, A. Turanov, M. Krekhova, G. Lattermann, I. Rehberg, and R. Richter, "Measuring the deformation of a ferrogel in a homogeneous magnetic field," J. Chem. Phys. 128, 164709 (2008).

⁵G. Filipcsei and M. Zrinyi, "Magnetodeformation effects and the swelling of ferrogels in a uniform magnetic field," J. Phys.: Condens. Matter 22, 276001 (2010).

⁶D. S. Wood and P. J. Camp, "Modeling the properties of ferrogels in uniform magnetic fields," Phys. Rev. E 83, 011402 (2011).

⁷R. Weeber, S. Kantorovich, and C. Holm, "Deformation mechanisms in 2D magnetic gels studied by computer simulations," Soft Matter 8, 9923–9932 (2012).

⁸M. Alberto Annunziata, A. M. Menzel, and H. Löwen, "Hardening transition in a one-dimensional model for ferrogels," J. Chem. Phys. 138(20), 204906 (2013).

⁹S.-H. Hu, T.-Y. Liu, D.-M. Liu, and S.-Y. Chen, "Controlled pulsatile drug release from a ferrogel by a high-frequency magnetic field," Macromolecules 40, 6786–6788 (2007).

¹⁰J. Qin, I. Asempah, S. Laurent, A. Fornara, R. N. Muller, and M. Muhammed, "Injectable superparamagnetic ferrogels for controlled release of hydrophobic drugs," Adv. Mater. 21(13), 1354–1357 (2009).

¹¹R. V. Ramanujan and L. L. Lao, "The mechanical behavior of smart magnet–hydrogel composites," Smart Mater. Struct. 15(4), 952 (2006).

¹²S. Monz, A. Tschöpe, and R. Birringer, "Magnetic properties of isotropic and anisotropic Co Fe₂ O₄-based ferrogels and their application as torsional and rotational actuators," Phys. Rev. E 78(2), 021404 (2008).

¹³A. Kondo, H. Kamura, and K. Higashitani, "Development and application of thermo-sensitive magnetic immunomicrospheres for antibody purification," Appl. Microbiol. Biotechnol. 41(1), 99–105 (1994).

¹⁴X. Wang, C. Zhao, P. Zhao, P. Dou, Y. Ding, and P. Xu, "Gellan gel beads containing magnetic nanoparticles: An effective biosorbent for the removal of heavy metals from aqueous system," Bioresour. Technol. 100(7), 2301–2304 (2009).

¹⁵Colloidal Magnetic Fluids: Basic, Development and Application of Ferrofluids, edited by S. Odenbach (Springer, 2009), Vol. 763.

¹⁶R. Jurgons, C. Seliger, A. Hilpert, L. Trahms, S. Odenbach, and C. Alexiou, "Drug loaded magnetic nanoparticles for cancer therapy," J. Phys.: Condens. Matter 18(38), S2893 (2006).

¹⁷C. Holm and J.-J. Weis, "The structure of ferrofluids: A status report," Curr. Opin. Colloid Interface Sci. 10, 133–140 (2005).

¹⁸R. Koetitz, P. C. Fannin, and L. Trahms, "Time domain study of Brownian and neel relaxation in ferrofluids," J. Magn. Magn. Mater. 149, 42–46 (1995).

¹⁹A. V. Ryzhkov, P. V. Melenev, C. Holm, and Yu. L. Raikher, "Coarse-grained molecular dynamics simulation of small ferrogel objects," J. Magn. Magn. Mater. 383, 277–280 (2015).

²⁰D. Collin, G. K. Auernhammer, O. Gavat, P. Martinoty, and H. R. Brand, "Frozen-in magnetic order in uniaxial magnetic gels: Preparation and physical properties," Macromol. Rapid Commun. 24, 737 (2003).

²¹N. A. Peppas, P. Bures, W. Leobandung, and H. Ichikawa, "Hydrogels in pharmaceutical formulations," Eur. J. Pharm. Biopharm. 50, 27 (2000).

²²E. Chiessi, F. Cavalieri, and G. Paradossi, "Water and polymer dynamics in chemically cross-linked hydrogels of poly(vinyl alcohol): A molecular dynamics simulation study," J. Phys. Chem. B 111(11), 2820–2827 (2007).

²³A. S. Hoffman, "Hydrogels for biomedical applications," Adv. Drug Delivery Rev. 64, 18–23 (2012).

²⁴J. Höpfner, T. Richter, P. Košovan, C. Holm, and M. Wilhelm, "Seawater desalination via hydrogels: Coarse grained simulations and practical realisation," Prog. Colloid Polym. Sci. 140, 247 (2013).

²⁵P. Košovan, T. Richter, and C. Holm, "Molecular simulations of hydrogels," in Intelligent Hydrogels, Progress in Colloid and Polymer Science edited by G. Sadowski and W. Richtering (Springer International Publishing, 2013), Vol. 140, pp. 205–221.

²⁶M. R. Dudek, B. Grabiec, and K. W. Wojciechowski, "Molecular dynamics simulations of auxetic ferrogel," Rev. Adv. Mater. Sci. 14, 173 (2007).

²⁷R. Messing, N. Frickel, L. Belkoura, R. Strey, H. Rahn, S. Odenbach, and A. M. Schmidt, "Cobalt ferrite nanoparticles as multifunctional cross-linkers in PAAM ferrohydrogels," Macromolecules 44(8), 2990–2999 (2011).

²⁸L. Roeder, M. Reckenthaler, L. Belkoura, S. Roitsch, R. Strey, and A. M. Schmidt, "Covalent ferrohydrogels based on elongated particulate cross-linkers," Macromolecules 47(20), 7200–7207 (2014).

²⁹P. Ilg, "Stimuli-responsive hydrogels cross-linked by magnetic nanoparticles," Soft Matter 9(13), 3465–3468 (2013).

³⁰Yu. L. Raikher and O. V. Stolbov, "Magnetodeformational effect in ferrogel samples," J. Magn. Magn. Mater. 258-259, 477 (2003).

³¹A. Yu Zubarev, "On the theory of the magnetic deformation of ferrogels," Soft Matter 8(11), 3174–3179 (2012).

³²D. Ivaneyko, V. Toshchevikov, M. Saphiannikova, and G. Heinrich, "Mechanical properties of magneto-sensitive elastomers: Unification of the continuum-mechanics and microscopic theoretical approaches," Soft Matter 10, 2213 (2013).

$^{33}$D. Ivaneyko, V. P. Toshchevikov, M. Saphiannikova, and G. Heinrich, "Magneto-sensitive elastomers in a homogeneous magnetic field: A regu- lar rectangular lattice model," *Macromol. Theory Simul.* **20**(6), 411–424 (2011).

$^{34}$O. Stolbov, Y. L. Raikher, and M. Balasoiu, "Modelling of magnetodipolar striction in soft magnetic elastomers," *Soft Matter* **7**, 8484–8487 (2011).

$^{35}$G. Pessot, R. Weeber, C. Holm, H. Löwen, and A. M. Menzel, "Towards a scale-bridging description of ferrogels and magnetic elastomers," *J. Phys. Cond. Mat.* **27**, 325105 (2015).

$^{36}$R. Weeber, S. Kantorovich, and C. Holm, "Ferrogels cross-linked by mag- netic nanoparticles—Deformation mechanisms in two and three dimensions studied by means of computer simulations," *J. Magn. Magn. Mater.* **383**, 262–266 (2015).

$^{37}$R. Weeber, "Simulation of novel magnetic materials in the field of soft matter," Ph.D. thesis, University Stuttgart, 2014.

$^{38}$H. J. Limbach, A. Arnold, B. A. Mann, and C. Holm, "ESPResSo—An extensible simulation package for research on soft matter systems," *Comput. Phys. Commun.* **174**(9), 704–727 (2006).

$^{39}$A. Arnold, O. Lenz, S. Kesselheim, R. Weeber, F. Fahrenberger, D. Röhm, P. Košovan, and C. Holm, "ESPResSo 3.1—Molecular dynamics software for coarse-grained models," in *Meshfree Methods for Partial Differential Equa- tions VI*, Lecture Notes in Computational Science and Engineering edited by M. Griebel and M. A. Schweitzer (Springer, 2013), Vol. 89, pp. 1–23.

$^{40}$Z. Wang, C. Holm, and H. Walter Müller, "Molecular dynamics study on the equilibrium magnetization properties and structure of ferrofluids," *Phys. Rev. E* **66**, 021405 (2002).

$^{41}$J. D. Weeks, D. Chandler, and H. C. Andersen, "Role of repulsive forces in determining the equilibrium structure of simple liquids," *J. Chem. Phys.* **54**, 5237 (1971).

$^{42}$D. Ivaneyko, V. Toshchevikov, M. Saphiannikova, and G. Heinrich, "Effects of particle distribution on mechanical properties of magneto-sensitive elasto- mers in a homogeneous magnetic field," *Condens. Matter Phys.* **15**(3), 33601 (2012).

$^{43}$B. A. Mann, "The swelling behaviour of polyelectrolyte networks," Ph.D. thesis, Johannes Gutenberg-University, Mainz, Germany, 2005.

$^{44}$See supplementary material at http://dx.doi.org/10.1063/1.4932371 for details regarding the procedure to obtain the elasticity matrix of the gel.

$^{45}$A. O. Ivanov and O. B. Kuznetsova, "Magnetic properties of dense ferroflu- ids: An influence of interparticle correlations," *Phys. Rev. E* **64**, 041405 (2001).