
# Orientational ordering of lamellar structures on closed surfaces.

J. Pękalski \( ^{1} \)  and A. Ciach \( ^{1} \) 

 \( ^{1} \) Institute of Physical Chemistry, Polish Academy of Sciences, Kasprzaka 44/52, 01-224 Warszawa, Poland

Self-assembly of particles with short-range attraction and long-range repulsion (SALR) interactions on a flat and on a spherical surface is compared. Molecular dynamics (MD) simulations are performed for the two systems having the same area and the density optimal for formation of stripes of particles. Structural characteristics, e.g. a cluster size distribution, a number of defects and an orientational order parameter (OP), as well as the specific heat, are obtained for a range of temperature. In both cases, the cluster size distribution becomes bimodal and elongated clusters appear at the temperature corresponding to the maximum of the specific heat. When the temperature decreases, orientational ordering of the stripes takes place, and the number of particles per cluster or stripe increases in both cases. However, only on the flat surface the specific heat has another maximum at the temperature corresponding to a rapid change of the OP. On the sphere, the crossover between the isotropic and anisotropic structures occurs in a much broader temperature interval, the orientational order is weaker, and occurs at significantly lower temperature. At low temperature the stripes on the sphere form spirals, and the defects resemble defects in the nematic phase of rods adsorbed at a sphere.

## I. INTRODUCTION

Competing interactions of various origin can lead to pattern formation at different length scales  \( [1-11] \) . In particular, particles adsorbed at flat interfaces can form stripes or spherical clusters or bubbles, when the hard-core repulsion is followed by attraction at larger distances, and a repulsion is again present at still larger particle separations (SALR potential)  \( [12-18] \) . For increasing density of the particles, transitions between disordered fluid, hexagonal cluster crystal, stripes, hexagonal crystal of bubbles and dense disordered phase occur at sufficiently low temperature  \( T [17, 18] \) .

For the density optimal for the stripe formation, an isotropic labyrinth of stripes occurs at relatively high T. This isotropic inhomogeneous phase is transformed to an anisotropic phase of stripes with preferred orientation (molten lamella, ML) when T is decreased [17]. In a SALR system on a triangular lattice, further decrease of temperature leads to the transition to the lamellar phase (L) with a translational order, as found (for a finite system) by Monte Carlo simulations in Ref.[17].

A transition between the isotropic and anisotropic phases of stripes was observed also in thin magnetic films  \( [19] \) , and found in Ref. \( [20] \)  within the Landau-Brazovskii (LB) theory  \( [21] \) . The phenomenological LB theory is applicable to any system with competing interactions leading to the order parameter (OP) that oscillates in space. The SALR model is a particular member of the LB universality class  \( [22] \) . One may expect that some of the results concerning the structure of stripes obtained for the SALR model can be valid in other stripe-forming systems as well.

The L and ML phases are analogous to the smectic and nematic liquid crystals respectively, because in the L and smectic phases both the translational and the orientational order are present, and the ML and nematic phases are ordered only orientationally. The translational order in those phases is destroyed by topological defects like dislocations and disclinations.

The defects were intensively studied for stripe forming systems mainly in the case of block-copolymers thin films  \( [23–25] \) . In the case of the SALR system, the defects can be suppressed when the two-dimensional system is confined between two parallel boundaries (lines), i.e. decreasing the wall separation has an effect analogous to decreasing the temperature  \( [26] \) . The geometry, permeability and elasticity of the confinement, however, play an important role for the ordering of inhomogenous SALR structures  \( [15, 27–29] \) .

In this work we focus on the SALR particles adsorbed at a surface of a vesicle or at a spherical droplet. Particles adsorbed at the surface of a droplet, i.e. colloidosomes, have been studied mainly in the case of close packing  \( [30–33] \) . Recently, such systems attract attention also in the case of the sphere only partially covered by the particles, because of the possibility of spontaneous pattern formation. In the case of DNA-coated colloids on functionalized oil droplets  \( [34] \) , it was shown that various patterns can be formed when one tunes the strength of the attraction between the colloids. The studies in Ref. \( [34] \) , however, were limited to densities corresponding to formation of the bubbles, therefore the Authors did not find any lamellar or cluster morphology.

There are no true thermodynamic phase transitions in finite systems, therefore we do not expect any ordered phase on a surface of a sphere. However, the structure of the disordered phase may be significantly different for different densities and at different temperatures, due to a presence of a short-range order. We call the finite system "ordered", when the correlation length is larger than the size of the system, and a suitably defined OP is of order of unity. In this context, 'the ordered structure' should not be mistaken with 'the ordered phase'.

The global ordering on curved and closed surfaces is suppressed by defects that are inevitably associated with the curvature. The interesting question of defect formation at curved surfaces attracted a lot of attention re-
 

cently  \( [35–43] \) , but the studies focused mainly on closely-packed particles  \( [44, 45] \) . Studies of the pattern formation by the SALR particles on closed curved surfaces are rare  \( [34, 46–49] \) . In the current study, we focus on colloidal particles with a diameter of a few hundreds of nanometers that are adsorbed on a spherical droplet with a diameter  \( \sim 10\mu m \) , as in Ref.  \( [34] \) , i.e. the radius of the droplet is one order of magnitude larger than the particle diameter.

We cannot expect that at any temperature the stripes on a sphere can have the translational order such that the average density is given by an oscillatory function  \( \rho(z) \)  of a single scalar variable z, as in the lamellar phase on a flat surface. For this reason we do not study the translational ordering. It is not clear, however, if the SALR particles on a surface of a sphere can self-assemble into stripes that have a preferred orientation, and how the orientational order can be quantified. As far as we know, this question has not been studied yet, and we address it in the present work. In addition, we study if the orientational ordering is associated with the other structural characteristics such as the number of defects, the cluster size distribution, the average size of the cluster and thermal properties (specific heat). Our studies are based on molecular dynamics simulation (MD).

In the case of liquid crystals, the orientational OP is usually based on the eigenvalues of the ordering matrix  \( [50] \) . This order parameter successfully describes nematic order in amphiphilic systems  \( [51, 52] \) . However, it is inconvenient in MD studies where structures, even when ordered, flow and can change their orientation globally. To overcome this problem, we propose a new orientational order parameter that is suitable for describing the order found by MD simulations, and is easily applicable to systems with different topologies. We verify if the new OP gives results consistent with the standard OP based on the eigenvalue of the ordering matrix  \( [50] \)  by calculating both parameters for a flat surface.

In order to distinguish the effects of the finite size of the system from the effects of the curvature, we consider a flat surface with periodic boundary conditions (torus topology, TBC) and a surface of a sphere (SBC) with the same area as that of the flat one. Likewise, to eliminate the effects of incompatibility between the number of particles on the surface and the density optimal for the stripe formation, we fix the number of particles such that the density is close to the density optimal for the periodic lamellar structure, both on the flat and on the curved surface. On the curved surface the density optimal for the stripes is a bit smaller than on the flat one. We choose the SALR potential leading to small clusters or stripes of thickness  \( \sim2\sigma \) , where  \( \sigma \)  is the particle diameter.

In Section II, we define the model, introduce the orientational order parameter and describe the methods used for calculating the size distribution of the aggregates and the average number of dislocation defects. In Section III A, we present the results for the flat surface. We show typical snapshots of the structure, and temperature dependence of the following quantities: the number of clusters or stripes, the maximal number of particles in the aggregate, the two OP, the average number of defects, the aggregate size distribution, and the specific heat. In Section III B, we present the results for the same quantities for the particles adsorbed at the sphere. In Section IV we discuss the results.

## II. THE MODEL AND THE METHODS

## A. Model

The SALR potential is modeled as a sum of the Lennard-Jones and the Yukawa potentials:

 \[ V(r)=4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{2\alpha}-\left(\frac{\sigma_{r}}{r}\right)^{\alpha}\right]+\frac{A}{r}e^{-r/\xi}, \quad (1) \] 

where  \( \alpha = 6 \) , A = 1.27,  \( \xi = 2 \) , and  \( \varepsilon = 1.0 \) ,  \( \sigma = 1.0 \times 10^{-3} \)  set the unit of energy and length, respectively. In this case, the temperature has the units of  \( k_{B}T/\varepsilon \) . With that model parameters the area of the attraction well is around 3 times smaller than the area of the potential repulsive tail, i. e.  \( \int_{1}^{r_{0}} V(r) dr \approx 3 \int_{r_{0}}^{r_{cut}} V(r) dr \) , where  \( r_{0} \)  is the distance at which  \( V(r) \)  crosses zero and  \( r_{cut} \)  is the distance at which the potential was cut and shifted to zero for computational reasons. The used ratio matches the ratio of the repulsion to attraction strengths studied in the lattice model in Refs. [17, 18, 28, 29, 53]. The same form of the SALR potential was previously studied in Refs. [54–58].

![](./images/867747980113871104_1.jpg)

FIG. 1: The potential has a local minimum for r = 1.141σ, then it crosses zero at  \( r_{0} = 1.412\sigma \)  and it has a local maximum for r = 1.886σ. The potential has been cut off at r = 8σ.

## B. Methods

In order to perform MD simulations, the HOOMD-blue [59, 60] package was used. We obtained the low
 

temperature structures by linearly decreasing the temperature of the system. Typically, the starting temperature was set to  \( k_{B}T = 0.2 \)  and the procedure finished at  \( k_{B}T = 0.03 \) , where  \( k_{B} \)  is the Boltzmann constant. In all the runs at least  \( 10^{9} \)  MD steps were performed and the values of interest were sampled every  \( 10^{4} \)  step. In order to obtain ordered structures, relatively small systems were considered, namely in the case of the toroidal periodic boundary conditions we used N = 975 particles, and a square simulation box with  \( L = 51.52\sigma \) , while in the case of the spherical boundary conditions, the number of particles was set to N = 900, and the sphere radius was  \( 13.78\sigma \) . In the latter case the particles were constrained to move on the surface of the sphere.

The analysis of the formed aggregates was made based on the distance criterion with a cut-off distance set to  \( r = 1.41\sigma \) , that is the distance where the pair potential crosses zero and becomes repulsive. Using the width of the basin of attraction as a cut-off distance for identification of the aggregates is a typical choice in SALR systems studies [58, 61–65]. The aggregate size distribution (ASD) is presented in the manner commonly used in micellization studies, where the probability of cluster occurrence is weighted by the cluster size, so that

 \[ p(M)=\frac{P(M)M}{\sum_{M}P(M)M}, \quad (2) \] 

where  \( P(M) \)  is the probability of finding an aggregate of size M. Since at high temperatures the particles form structureless aggregates, and then upon cooling larger elongated structures stabilize, we will refer to the former as clusters and to the latter as stripes. At some temperature range, however, the clusters and the stripes coexist and the ASD is bimodal. Thus, we can identify the maximal size of what we call cluster,  \( M_{b} \) , with the minimum in the ASD that separates the two local maxima. In the case of our model  \( M_{b}=22 \) .

We determine if the stripes are orientationally ordered by considering local orientations of short segments within each of the lamellar stripes. Namely, we find vectors that connect two particles within the same stripe, normalize them, drag all initial points of such vectors to one point, O, and compute the moment of inertia of the object built by the vectors terminal points. Because the considered particles are isotropic, the result should be independent of the vectors' directions. Thus, we consider both directions of the vectors and as a result the built object is symmetric with respect to the point O (see Fig. 2). To make sure that each of the vectors describes the local orientation of the hosting stripe, we take into account only pairs of particles belonging to the same row of the stripe. This is obtained by considering only the pairs of particles with the distance between their centers larger than  \( \sqrt{7}\sigma \)  and smaller than  \( 3.5\sigma \)  (see Fig. 3).

For a perfectly isotropic lamellar structure in 3D, the terminal points of the vectors should lay on a surface of a sphere, while for the a structure with a perfect orientational order (parallel stripes) the terminal points would

(a)

(b)

![](./images/867747980113871104_2.jpg)

FIG. 2: Illustration of the way the order parameter,  \( O_{p} \) , is constructed. In panels (a-b) we show possible particle configurations at a flat surface and the vectors used for construction of  \( O_{p} \) . After all the vectors are found, they are normalized and moved to one point (panels (c-d) respectively). The points indicated by the terminal points of the vectors (red circles) form an object which principal moments of inertia,  \( I_{1} \)  and  \( I_{2} \)  determine the value of the order parameter in the following way:  \( O_{p} = 1 - I_{1}/I_{2} \) .

form a circle. Hence, we define the order parameter  \( O_{p} \)  as one minus the ratio between the largest and the smallest ones of the principal moments of inertia of this object, i.e.  \( O_{p} = 1 - I_{1}/I_{2} \) .

For the case of TBC we compare  \( O_{p} \)  with another orientational order parameter, i.e. the eigenvalue,  \( \lambda \) , of the ordering matrix \( ^{[50]} \) :

 \[ Q_{\alpha\beta}=\frac{1}{N_{\mathrm{p a i r}}}\sum_{i}2e_{i\alpha}e_{i\beta}-\delta_{\alpha\beta}, \quad (3) \] 

where  \( \alpha \)  and  \( \beta \)  are the Cartesian coordinates in the two-dimensional space (2D), the index i labels all  \( N_{pair} \)  considered normalized pairs of vectors and  \( \delta_{\alpha,\beta} \)  is the Kronecker delta function. It's important to note that, unlike in the 3d space, in 2d the ordering matrix has two eigenvalues  \( \pm\lambda \)  which do not vanish when the fluid is isotropic and  \( N_{pair}<\infty \) . [66]

We identify a dislocation defect in the stripe-forming system with breaking of the stripe, i.e. with formation of two extra ends of the stripes. The stripes ends are found by analyzing the number of first and second neighbors of all the particles that form stripes. We take into account only particles with 2 or 3 nearest neighbors (nm) and accept them as defect-pointers if the following conditions are fulfilled: a particle has 3 nm and two of those nm have 3 nm whereas one of them has 6 nm (Fig. 4a), or a particle has 2 nm and both of them have 4 nm (Fig. 4b), or one of them has 3 nm and the other one has 4 nm (Fig. 4c), or one has 3 nm and the other one 5 nm (Fig. 4d). The total number of dislocation defects, d, is defined as the total
 
![](./images/867747980113871104_3.jpg)

FIG. 3: Schematic illustration of the construction of the orientational OP  \( O_{p} \) . The black vector representing the local orientation of the stripe, connects the centers of the particles located in the same row. The distance between the centers is assumed to be  \( \sqrt{7}\sigma < r < 3.5\sigma \) . All such vectors are used in construction of the object, whose principal moments of inertia allow to distinguish isotropic and anisotropic structures. See the Section II B for more details.

(a)

(b)

(c)

(d)

![](./images/867747980113871104_4.jpg)

FIG. 4: Representative configurations of particles considered as the dislocation defects. The particles marked by red color are the defects pointers located as described in the text.

number of stripes ends divided by two, since breaking of one stripe results in two extra ends.

The visualization of the snapshots was made using The Open Visualization Tool (OVITO) [67].

## III. RESULTS

The aim of our study is the comparison of the particle self-assembly into lamellar structures in systems with toroidal and spherical periodic boundary conditions. In both systems boundary conditions are periodic, however, the toroidal boundary conditions (TBC) are used to mimic flat and infinite systems, whereas in the case of the spherical boundary conditions (SBC) the surface is curved and closed. In what follows we present how the lamellar structures self-assemble in the two systems when the temperature is decreased.

## A. Toroidal boundary conditions

Presence of TBC can lead to different structures in the SALR model depending on the system size. If the size is large enough, then the SALR particles form disordered isotropic stripe patterns at  \( k_{B}T > 0 \) , [46] whereas in the case of smaller systems the use of TBC can induce order [17, 68]. Typical configurations obtained in our simulations are presented in Fig. 5. The high temperature

(a)

![](./images/867747980113871104_5.jpg)

(b)

(c)

![](./images/867747980113871104_6.jpg)

![](./images/867747980113871104_7.jpg)

(d)

![](./images/867747980113871104_8.jpg)

(e)

![](./images/867747980113871104_9.jpg)

(f)

![](./images/867747980113871104_10.jpg)

(g)

![](./images/867747980113871104_11.jpg)

FIG. 5: Representative configurations of the system with TBC and N = 975 at different temperatures. (a)  \( k_{B}T = 0.25 \) , (b)  \( k_{B}T = 0.18 \) , (c)  \( k_{B}T = 0.14 \) , (d)  \( k_{B}T = 0.12 \) , (e)  \( k_{B}T = 0.11 \) , (f)  \( k_{B}T = 0.10 \) , (g)  \( k_{B}T = 0.05 \) . The number of clusters in the consecutive panels are: 80, 45, 38, 24, 30, 7, 7.

structures show networks of particles that are structureless and disordered. The decrease of temperature results in formation of clusters with a preferred size, indicated by a local maximum in the ASD. Upon further cooling the preferred size increases slightly, the clusters merge into longer structures and the ASD becomes bimodal (Fig. 6) due to formation of elongated aggregates, which we call stripes. Cluster merging is associated with a local maximum in the heat capacity (Fig. 7) and a monotonic decrease of the number of the aggregates M (Fig. 8a). Interestingly, at temperatures  \( k_{B}T > 0.14 \) , although the
 
![](./images/867747980113871104_12.jpg)

FIG. 6: Mass weighted aggregate size distribution (Eq.(2)) for the system with TBC, N = 975, shifted vertically for better visibility.  \( k_{B}T = 0.20 \)  (red dotted line),  \( k_{B}T = 0.165 \)  (black solid line),  \( k_{B}T = 0.12 \)  (blue dashed line). Note the log scale on the horizontal axis.

![](./images/867747980113871104_13.jpg)

FIG. 7: The Canonical heat capacity  \( c_{V} \)  per particle as a function of temperature for the system with TBC. The location of the high-T maximum corresponds to the temperature at which the aggregate size distribution becomes bimodal (Fig. 6), while the low-T maximum indicates the temperature of the structural transition from the isotropic to the orientationally ordered (anisotropic) system.

number of aggregates decreases, the size of the largest observed aggregate  \( n_{max} \)  (Fig. 8b) and the orientation order parameters (Fig. 9) do not show any significant changes. Thus, we conclude that at the high temperatures the cluster formation and their merging into lamellar stripes leads to formation of isotropic structures made of easily distinguishable aggregates with a preferred and limited size. The size distribution of the aggregates (Fig. 6), however, is fairly broad, and thus the size fluctuations are large.

Further decrease of temperature triggers more intensive structural changes, which result in aligning of the lamellar stripes into orientationally ordered structure (Fig. 5e-g). As the temperature decreases, the number of aggregates decreases and exhibits a significant drop at  \( k_{B}T \approx 0.11 \) . The rapid merging of clusters into stripes induces high energy fluctuations and as a result, another peak in the heat capacity occurs. In order to show that the structural transition that takes place at  \( k_{B}T \approx 0.11 \)  resembles an order-disorder phase transition, we calculated two orientational order parameters described in Sec.

![](./images/867747980113871104_14.jpg)

![](./images/867747980113871104_15.jpg)

FIG. 8: Properties of the aggregates as a function of temperature for the case of TBC. Left panel: the number of clusters, M, divided by the number of particles N. Right panel: the size of the largest cluster,  \( n_{max} \)  divided by N.

![](./images/867747980113871104_16.jpg)

FIG. 9: Orientational order parameters for the system with TBC.  \( \lambda \)  is the eigenvalue of the ordering matrix defined in Eq. (3), while  \( O_{p} \)  is the order parameter based on the moments of inertia ratio introduced in sec.II.2.

II.B. The first order parameter,  \( \lambda \) , is the eigenvalue of the ordering matrix defined in Eq. (3) (Fig. 9a) and the second one is the order parameter  \( O_{p} \)  (Fig. 9b). In fact, the two OP for the case of a flat two-dimensional systems are strictly related:  \( O_{p} = 1 - \frac{1 - |\lambda|}{1 + |\lambda|} \) . However, only  \( O_{p} \)  can be conveniently used for non-flat systems, as will be shown in Sec. III.B. Both order parameters exhibit a rapid change at  \( k_{B}T \approx 0.11 \) . We verified that the transition occurred for different system sizes too, and that the temperature at the transition was the higher the smaller was the system. We did not try to verify if this orientational ordering was associated with a thermodynamic phase transition in the thermodynamic limit, since in this work we are interested in comparing systems of finite area that are either flat, or curved and closed.
 
![](./images/867747980113871104_17.jpg)

FIG. 10: The number of defects as a function of temperature for the TBC case. The solid line is the fit of our results to the exponentially growing function of the form  \( c + a \exp(b/k_{B}T) \) . The number of dislocation defects is defined as a number of stripes ends divided by the factor of 2. The ends of the stripes were localized with the method described in Sec. II B.

In the case of TBC, ordering of winding lamellar stripes into a defect-less lamellar structure takes place in a narrow temperature range and is associated with merging of lamellar segments that are short. The emerging structure is composed of 7 stripes that thanks to periodicity of the simulation box do not have topological defects and form closed curves. The structure, however, is not translationally invariant probably due to incommensurability between the box size and the period of the structure or a mismatch between the box size and number of particles.

Large slopes of the order parameters are reflected in the birth rate of topological defects in the stripes. The number of the defects in the structure is an important factor from the point of view of possible industrial applications. In the case of the diblock copolymers which spontaneously form lamellar structures, the number of dislocation defects increases with temperature exponentially  \( [25] \)  via the following relation

 \[ n_{d}\sim\frac{1}{a_{c}^{2}}\exp^{-E_{d}/k_{B}T}, \quad (4) \] 

where  \( n_{d} \)  is the density of dislocations,  \( E_{d} \)  the energy of a single dislocation and  \( a_{c} \)  is a dislocation core radius. In the case of the SALR particles, heating up the orientationally ordered lamellar structure also results in an exponential growth of the number of the dislocation defects (Fig. 10).

## B. Spherical boundary conditions

In this section, we study the system with the SBC and the same area as in the system with the TBC presented in Sec. III A. The density, however, had to be lowered because while the TBC allows the SALR particles to form straight stripes, the SBC does not, and the packing of the stripes is less dense. For this reason in order to obtain ordered lamellar structures at low-T, a system with smaller density was used.

Representative configurations for different temperatures are shown in Fig. 11. High temperature structural behavior of the system with the SBC resembles that of the system with the TBC. The SALR fluid is disordered, but it is not homogeneous. When the temperature decreases, clusters with a preferred size start to form. Similarly as in the case of the TBC, further cooling results in merging of the clusters (Fig. 12a) into elongated structures, but in the case of the SBC the  \( n_{max} \)  is not constant and exhibits a local maximum at  \( k_{B}T \approx 0.14 \)  (Fig. 12b). The maximum of  \( n_{max} \)  occurs at the temperature at which also the slope of  \( M(T) \)  changes and becomes smaller for  \( k_{B}T < 0.14 \) . When  \( k_{B} T \)  is further decreased, the clusters merge into stripes, and  \( M(T) \)  exhibits an inflection point at  \( k_{B} T \approx 0.11 \) . At the same temperature the heat capacity has a maximum (Fig. 13) and the ASD becomes bimodal (Fig. 14).

The orientational order parameter  \( O_{p} \)  does not change as strongly as in the case of TBC (Fig. 15). The  \( O_{p} \)  changes smoothly in the temperature range  \( 0.06 < k_{B}T < 0.14 \)  between  \( O_{p} = 0.09 \)  and  \( O_{p}=0.42 \) . The low-T particle configurations are presented in Fig. 16. The obtained structures are composed of either 2 or 3 lamellar stripes, which wrap around each other. In particular, the 2-stripe structure resembles a double-helix, while the 3-stripe structure is a double-helix with an extra stripe that separates the other two. Importantly, in both structures only a local orientational order can be seen and both structures have similar total potential energy. Similar energies probably result from the same number of topological defects.

Our results show that for relatively small SALR systems with spherical topology, the number of dislocations increases with temperature via the exponential relation, as it was in the case of TBC (Fig. 17).

Merging of lamellar segments into longer stripes upon cooling takes place in a much broader temperature range then in the TBC case. Both M/N and  \( n_{max} \)  reach a plateau only for  \( k_{B}T \leq 0.06 \) .

The heat capacity dependence on temperature is significantly different than in the case of the flat surface too. In the case of the TBC there are two peaks: the high-T peak is associated with formation of the lamellar stripes, while the low-T peak reflects the energy fluctuations rise due to the stripe ordering into defect-less structure. In the case of the SBC, only the stripe formation leads to an increase of the heat capacity, probably because the orientational ordering upon cooling occurs in a broad temperature range, the order is weak and topological defects are allowed.

## IV. DISCUSSION AND CONCLUSIONS

The aim of our study was to determine how the curvature of the surface at which self-assembling particles are
 
![](./images/867747980113871104_18.jpg)

FIG. 11: Representative configurations of the system with SBC and N = 900 at different temperatures. From top to bottom row:  \( k_{B}T = 0.18, 0.14, 0.11, 0.09, 0.06 \) . The number of clusters in the consecutive rows are: 44, 24, 20, 17, 5. In each row different snapshots of the same configuration are presented. Different colors correspond to different clusters identified by the distance criterion.

adsorbed influences pattern formation. We have chosen the radius of the sphere one order of magnitude larger than the diameter of the adsorbed particles. The number of particles was chosen such that lamellar structures can be formed on both flat and curved surface. We have limited our study to a single value of the density because formation of lamellar structures at low T requires very precise choice of the density [17].

To determine the effects of curvature, we have computed the number of aggregates  \( M(T) \) , the maximal number of particles in the aggregate  \( n_{max}(T) \) , the aggregate size distribution, the number of defects (half of the terminal points of elongated aggregates)  \( d(T) \) , the orientational OP  \( O_{p}(T) \) , and the specific heat  \( c_{V}(T) \) , for a flat and a spherical surface, both of the same area.

For relatively high temperature the curvature does not play a significant role. The particles on both, the flat

![](./images/867747980113871104_19.jpg)

![](./images/867747980113871104_20.jpg)

FIG. 12: Cluster properties as a function of temperature for the case of SBC. The number of clusters (left panel) and the number of particles in the largest cluster (right panel) divided by the number of particles, N.

![](./images/867747980113871104_21.jpg)

FIG. 13: Heat capacity per particle for the system with SBC. The maximum is at  \( k_{B}T = 0.11 \) .

![](./images/867747980113871104_22.jpg)

FIG. 14: Mass weighted aggregate size distribution (Eq.(2)) for the spherical system with N = 900 particles at different temperatures.  \( k_{B}T = 0.08 \)  (dashed blue),  \( k_{B}T = 0.11 \)  (solid black),  \( k_{B}T = 0.14 \)  (dotted red).
 
![](./images/867747980113871104_23.jpg)

FIG. 15: Orientational order parameter  \( O_{p} \)  defined in sec.II B for the system with SBC.

![](./images/867747980113871104_24.jpg)

FIG. 16: Low-temperature equilibrium structures. Left column: two lamellar stripes with two topological defects, i.e., four ends of the stripes. Right column: three stripes; one of them forms a closed curve (marked by the blue color) and the other two (white and red) have four ends.

surface and the surface of the sphere self-assemble into clusters when temperature is decreased. At some T the clusters merge into elongated assemblies (stripes), and the aggregate size distribution becomes bimodal. The specific heat takes a maximum at this temperature. The value of this temperature, however, is lower at the spherical surface.

Further cooling of the system leads to merging of the short stripes into larger ones that tend to be parallel to each other. This process begins at similar temperatures in both cases. On the flat surface the number

![](./images/867747980113871104_25.jpg)

FIG. 17: The number of dislocations defects of the lamellar stripes for the system with SBC as a function of temperature.

of stripes decreases rapidly and the orientational OP increases rapidly between  \( O_{p} \approx 0.3 \)  and  \( O_{p'} \approx 0.85 \)  in the same very narrow temperature interval around  \( k_{B}T \approx 0.11 \) . The orientational ordering and the rapid decrease of the number of defects are accompanied by a pick in the specific heat. On the sphere, the increase of the  \( O_{p} \)  and the decrease of the  \( M(T) \)  occur much more gradually. Both parameters change in the temperature interval  \( 0.06 < k_{B}T < 0.12 \) . In fact the upper boundary of the crossover region between the oriented and the isotropic structures cannot be uniquely determined, since the slope of  \( O_{p}(T) \)  changes gradually for  \( 0.06 < k_{B}T < 0.14 \) . The  \( O_{p} \)  increases from  \( O_{p'} \approx 0.1 \)  at  \( k_{B}T \approx 0.12 \)  to  \( O_{p} \approx 0.4 \)  at  \( k_{B}T \approx 0.06 \)  that is much smaller than  \( k_{B}T \approx 0.11 \)  corresponding to the ordered structure on a flat surface of the same area. Moreover, the broad crossover between the isotropic and anisotropic structures is not accompanied by a pick in the specific heat. Still, a significant difference between the high-T isotropic structure with many defects and the low-T anisotropic structure with few defects can be seen. We conclude that the curvature does not play a crucial role as long as the self-assembled stripes are shorter than the radius of the sphere. When the length of the stripes becomes comparable with the radius of the sphere or larger, then the curvature starts to play a significant role, as one should expect.

In the anisotropic structure with few defects the number of defects on the flat surface increases according to eqn (4) for increasing T, and on the sphere the same relation, but shifted by the ground state value of 2, holds. This is because according to our simulations the minimal number of defects on the sphere surface is d = 2.

Let us discuss the low temperature structure on the sphere. One might naively expect that parallel rings consisting of bilayers of particles would be formed. However, the lengths of the two layers of particles in the ring are different, and this difference increases when the rings approach the poles of the sphere. For this reason the distance between the particles in the two layers forming the ring are different, and it is not possible that most of the particles are separated by the distance corresponding to the minimum of the interaction potential. Thus, the splay of the ring-forming stripe is associated with an en-
 

ergy cost which for our model is large. In our model, the spirals that are parallel near the equator and make turns between segments that lie at a portion of a big circle, and eventually near the pole of the sphere break (Fig.16), are energetically favourable.

It is interesting to compare the low-T structures shown in Fig.16 with the defects that occur in a nematic phase of rods adsorbed at a sphere. There are two defects associated with the ends of the two open stripes. They lie on the opposite sides of the big circle (or at the poles of the sphere), in full analogy with the defects in the nematic phase. (see Fig.24 in Ref. \( [35] \) ). Thus, the analogy between the ML phase in the SALR system and the nematic phase in a system of rod-like particles, based on the orientational order in the two phases, persists on the

[1] M. Seul and D. Andelman, Science 267, 476 (1995).

[2] W. M. Gelbart, R. P. Sear, J. R. Heath, and S. Chaney, Faraday Discuss. 112, 299 (1999).

[3] A. Stradner, H. Sedgwick, F. Cardinaux, W. Poon, S. Egelhaaf, and P. Schurtenberger, Nature 432, 492 (2004).

[4] H. Sedgwick, S. Egelhaaf, and W. Poon, J. Phys. Condens. Matter 16, S4913 (2004).

[5] A. I. Campbell, V. J. Anderson, J. S. van Duijneveldt, and P. Bartlett, Phys. Rev. Lett. 94, 208301 (2005).

[6] A. Rauh, M. Rey, L. Barbera, M. Zanini, M. Karg, and L. Isa, Soft Matter pp. – (2017).

[7] Y. Zhuang, K. Zhang, and P. Charbonneau, Phys. Rev. Lett. 116, 098301 (2016).

[8] Y. Zhuang and P. Charbonneau, J. Phys. Chem. B 120, 6178 (2016).

[9] Y. Zhuang and P. Charbonneau, J. Phys. Chem. B 120, 7775 (2016).

[10] M. Edelmann and R. Roth, Phys. Rev. E 93, 062146 (2016).

[11] D. Pini and A. Parola, Soft Matter 13, 9259 (2017).

[12] A. Imperio and L. Reatto, J. Phys.: Condens. Matter 18, S2319 (2004).

[13] A. J. Archer, Phys. Rev. E 78, 031402 (2008).

[14] D. F. Schwanzer and G. Kahl, J. Phys.: Condens. Matter 22, 415103 (2010).

[15] R. Roth, Mol. Phys 109, 2897 (2011).

[16] B. Chacko, C. Chalmers, and A. J. Archer, J. Chem. Phys. 143, 244904 (2015).

[17] N. G. Almarza, J. Pékalski, and A. Ciach, J. Chem. Phys. 140, 164708 (2014).

[18] J. Pékalski, A. Ciach., and N. G. Almarza, J. Chem. Phys. 140, 114701 (2014).

[19] N. Saratz, A. Lichtenberger, O. Portmann, U. Ramsperger, A. Vindigni, and D. Pescia, Phys. Rev. Lett. 104, 077203 (2010).

[20] D. G. Barci, A. Mendoza-Coto, and D. A. Stariolo, Phys. Rev. E 88, 062140 (2013).

[21] S. A. Brazovskii, Sov. Phys. JETP 41, 85 (1975).

[22] A. Ciach, J. Pékalski, and W. T. Gózdź, Soft Matter 9, 6301 (2013).

[23] M. R. Hammond, E. Cochran, G. H. Fredrickson, and E. J. Kramer, Macromolecules 38, 6575 (2005).

curved surface of the sphere.

## V. ACKNOWLEDGEMENTS

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 734276 (CONIN). An additional support in the years 2017-2018 has been granted for the CONIN project by the Polish Ministry of Science and Higher Education. Financial support from the National Science Center under grant No. 2015/19/B/ST3/03122 is also acknowledged.

[24] A. Horvat, G. A. Sevink, A. V. Zvelindovsky, A. Krekhov, and L. Tsarkova, ACS nano 2, 1143 (2008).

[25] V. Mishra, G. H. Fredrickson, and J. Kramer, ACS Nano 6, 2629 (2012).

[26] N. G. Almarza, J. Pékalski, and A. Ciach, Soft Matter 12, 7551 (2016).

[27] A. Imperio and L. Reatto, Phys. Rev. E 76, 040402 (2007).

[28] J. Pékalski, A. Ciach, and N. G. Almarza, J. Chem. Phys. 142, 014903 (2015).

[29] J. Pékalski, N. Almarza, and A. Ciach, J. Chem. Phys. 142, 204904 (2015).

[30] N. Geerts and E. Eiser, Soft Matter 6, 4647 (2010).

[31] F. Rossier-Miranda, C. Schroën, and R. Boom, Colloids Surf. A Physicochem. Eng. Asp. 343, 43 (2009).

[32] Y. Yang, Y. Cai, N. Sun, R. Li, W. Li, S. C. Kundu, X. Kong, and J. Yao, Colloids Surf. B Biointerfaces 151, 102 (2017).

[33] B. Y. Guan, L. Yu, and X. W. D. Lou, Advanced Materials 28, 9596 (2016).

[34] D. Joshi, D. Bargteil, A. Caciagli, J. Burelbach, Z. Xing, A. S. Nunes, D. E. Pinto, N. A. Araújo, J. Brujic, and E. Eiser, Sci. Adv. 2, e1600881 (2016).

[35] M. J. Bowick and L. Giomi, Adv. Phys. 58, 449 (2009).

[36] F. C. Keber, E. Loiseau, T. Sanchez, S. J. DeCamp, L. Giomi, M. J. Bowick, M. C. Marchetti, Z. Dogic, and A. R. Bausch, Science 345, 1135 (2014).

[37] L. Perotti, S. Dharmavaram, W. Klug, J. Marian, J. Rudnick, and R. Bruinsma, Phys. Rev. E 94, 012404 (2016).

[38] E. Allahyarov, A. Voigt, and H. Löwen, Soft matter 13, 8120 (2017).

[39] A. Azadi and G. M. Grason, Phys. Rev. E 94, 013003 (2016).

[40] W. T. Irvine, V. Vitelli, and P. M. Chaikin, Nature 468, 947 (2010).

[41] L. R. Gómez, N. A. García, V. Vitelli, J. Lorenzana, and D. A. Vega, Nature Communications 6, 6856 (2015).

[42] T. Zhang, X. Li, and H. Gao, Extreme Mech Lett 1, 3 (2014).

[43] R. E. Guerra, C. P. Kelleher, A. D. Hollingsworth, and P. M. Chaikin, Nature 554, 346 (2018).

[44] B. De Nijs, S. Dussi, F. Smallenburg, J. D. Meeldijk, D. J. Groenendijk, L. Filion, A. Imhof, A. Van Blaaderen, and
 

M. Dijkstra, Nature materials 14, 56 (2015).

[45] S. Paquay, H. Kusumaatmaja, D. J. Wales, R. Zandi, and P. van der Schoot, Soft Matter 12, 5708 (2016).

[46] G. J. Zarragoicoechea, A. G. Meyra, and V. A. Kuz, Mol. Phys 107, 549 (2009).

[47] J. J. Amazon, S. L. Goh, and G. W. Feigenson, Phys. Rev. E 87, 022708 (2013).

[48] S. L. Goh, J. J. Amazon, and G. W. Feigenson, Biophysical journal 104, 853 (2013).

[49] J. J. Amazon and G. W. Feigenson, Phys. Rev. E 89, 022702 (2014).

[50] M. P. Allen and D. J. Tildesley, Computer Simulation of Liquids (Oxford University Press, 1987).

[51] J. R. McColl and C. Shih, Phys. Rev. Lett. 29, 85 (1972).

[52] P. A. Lebwohl and G. Lasher, Phys. Rev. A 6, 426 (1972), URL https://link.aps.org/doi/10.1103/PhysRevA.6.426.

[53] J. Pękalski, A. Ciach, and N. G. Almarza, J. Chem. Phys. 138, 144903 (2013).

[54] F. Sciortino, S. Mossa, E. Zaccarelli, and P. Tartaglia, Phys. Rev. Lett. 93, 055701 (2004).

[55] F. Sciortino, P. Tartaglia, and E. Zaccarelli, J. Phys. Chem. B 109, 21942 (2005).

[56] E. Mani, W. Lechner, W. K. Kegel, and P. G. Bolhuis, Soft Matter 10, 4479 (2014), URL http://dx.doi.org/10.1039/C3SM53058B.

[57] J. Toledano, F. Sciortino, and E. Zaccarelli, Soft Matter

5, 2390 (2009).

[58] A. P. Santos, J. Pękalski, and A. Z. Panagiotopoulos, Soft Matter 13, 8055 (2017).

[59] J. A. Anderson, C. D. Lorenz, and A. Travesset, J. Comput. Phys. 227, 5342 (2008).

[60] J. Glaser, T. D. Nguyen, J. A. Anderson, P. Lui, F. Spiga, J. A. Millan, D. C. Morse, and S. C. Glotzer, Comput. Phys. Commun. 192, 97 (2015).

[61] P. D. Godfrin, R. Castañeda-Priego, Y. Liu, and N. J. Wagner, J. Chem. Phys. 139, 154904 (2013).

[62] P. D. Godfrin, N. E. Valadez-Perez, R. Castaneda-Priego, N. J. Wagner, and Y. Liu, Soft Matter 10, 5061 (2014), URL http://dx.doi.org/10.1039/C3SM53220H.

[63] R. B. Jadrich, J. A. Bollinger, K. P. Johnston, and T. M. Truskett, Phys. Rev. E 91, 042312 (2015).

[64] J. A. Bollinger and T. M. Truskett, J. Chem. Phys. 145, 064902 (2016).

[65] J.-M. Bomont, D. Costa, and J.-L. Bretonnet, Phys. Chem. Chem. Phys. 19, 15247 (2017).

[66] D. Frenkel and R. Eppenga, Phys. Rev. A 31, 1776 (1985).

[67] A. Stukowski, Modell. Simul. Mater. Sci. Eng. 18, 015012 (2010), URL http://stacks.iop.org/0965-0393/18/i=1/a=015012.

[68] A. Imperio and L. Reatto, J. Chem. Phys. 124, 164712 (2006).
 

(a)

![](./images/867747980113871104_26.jpg)

(b)

![](./images/867747980113871104_27.jpg)

 
