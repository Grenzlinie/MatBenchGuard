# DISCRETE MODELS FOR PARTICLE PACKINGS
A. Jagota, E.I. DuPont de Nemours & Co., E356/347 Experimental Station, Wilming- ton, Delaware 19880-0356.

## Abstract
Discrete computational models for the viscosities, sintering rates, and transport properties of sintering particle packings are presented. The packing is represented by a set of nodes (the particle centroids) connected by links (inter-particle contacts). The models for the mechanical behavior enforce equilibrium for each particle which leads to a set of simultaneous equations for the particle motion. Electrical or thermal transport through inter-particle contacts is modelled by imposing zero net flux at a node which also leads to a set of simultaneous equations for the value of potential at each particle center. The model is used to simulate the compaction of spheres to generate a three- dimensional random packing. Statistical properties of the computed packing such as packing fraction, percolation threshold, and coordination number are compared with those of an experimental random packing. Results are also presented for the effective conductivity of mixtures of particles with very different conductivities.

## Introduction
The study of properties of granular materials has applications in diverse areas such as processing of metal and ceramic powders and soil mechanics [1,2]. Models for these phenomena are closely related to those used in the study of liquids [3] and percolation theory [4,5]. Our particular interest is in sintering particle packings and this paper is part of a larger study of their effective properties [6,7,8]. A discrete model for the deformation of granular materials is used to study the compaction of spheres in three dimensions. This generates a random packing of spheres which is compared with an ex- perimental packing. The sintering of such packings has been studied in [7]. A discrete model for conduction through particle contacts is used to study the effective transport properties of the packing.

## Computational methods
The model for deformation of the packing is based on a consideration of equilibrium of each particle. It is an extension of a previously developed model [9] and is discussed in greater detail in [8]. The model for effective transport properties satisfies the condition of zero net flux at each particle. Consider a packing of particles (Figure 1). Each particle transmits forces and moments through contacts with other particles. Force equilibrium of each particle requires that:
$$
\sum_{j=1}^{n^{c}} \mathbf{F}^{i j}+\mathbf{b}^{i}=0, \quad \forall i=1, n^{p}, \tag{1}
$$
where $\mathbf{F}^{i j}$ is the force transmitted between particles $i$ and $j$, $n^{c}$ is the number of contacts, $n^{p}$ is the total number of particles, and $\mathbf{b}^{i}$ is the body force. In the simulations presented here, the force between contacting spheres is dominantly central and moment equilibrium is satisfied identically.

The components of the force transmitted through a contact are related to the particle velocity $\mathbf{v}^{i}$ through the relationships:
$$
\dot{F}_{n}^{i j}=\mu^{n} \frac{\left(v_{n}^{j}-v_{n}^{i}\right)}{L}, \quad \dot{F}_{t}^{i j}=\mu^{t} \frac{\left(v_{t}^{j}-v_{t}^{i}\right)}{L}, \tag{2}
$$
$$
\mu^{t}=1.0, \quad \mu^{n}=\left\{\begin{array}{ll}
1.0 & (L>2 R) \\
1.0 \mathrm{x} 10^{15} \sqrt{1-L / 2 R} & (L \leq 2 R)
\end{array}.\right. \tag{3}
$$

Here, $L$ is the length between nodes $i$ and $j$, and subscripts $n$ and $t$ refer to components along the contact normal and tangent. The parameters $\mu^{n}$ and $\mu^{t}$ are contact moduli. When the distance between particle centers is less than the diameter, the incremental

Mat. Res. Soc. Symp. Proc. Vol. 278. ©1992 Materials Research Society

![](./images/811676871128252417_1.jpg)

Figure 1: Three-dimensional random packing of spheres (1220 particles).

![](./images/811676871128252417_2.jpg)

Figure 2: Change in bulk modulus, co- ordination number, and sphere-sphere interpenetration during compaction.

modulus $\mu^n$ is based on Hertzian contact [10]. When the distance is larger than the diameter, soft contacts with modulus of unity are established between each sphere and other spheres within a radius of 1.1 times the particle radius. This provides numeri- cal mechanical stability to the packing. Combining equation (2) with the equilibrium equation (1) then results in the matrix equation:

$$
[K]\{V\}=\{\dot{F}\}, \tag{4}
$$

where $\{V\}$ are the nodal velocities and $\{\dot{F}\}$ are the rates of change of nodal forces. These equations are solved incrementally. The time-step is chosen so that the maximum interpenetration between any two spheres is less than 0.001 times the radius. With different contact constitutive models, this technique is used to study sintering particle packings [7].

Conduction in the packing is modelled by requiring that net flux entering each par- ticle is zero. It is assumed that flux enters or leaves a particle only through contacts with other particles:

$$
\sum_{j=1}^{n^{c}} J^{i j}+q^{i}=0, \quad \forall i=1, n^{p}, \tag{5}
$$

where $J^{i j}$ is the flux entering particle $i$ through a contact with particle $j$, and $q^{i}$ is the flux generated in particle $i$. The flux is related to the potential $\phi$ at sphere centers by:

$$
J^{i j}=c^{i j}\left(\phi^{j}-\phi^{i}\right) / L, \tag{6}
$$

where $c^{i j}$ is the conductivity of the contact and is related to the conductivity of the particles and the area of contact [11]. Equations (5) and (6) combine to yield a set of simultaneous equations for the unknown potential $\phi$ at each particle center.

### Compaction of random packing

A collection of particles was original generated by randomly placing 2000 points in a cube. These were compressed into a packing of spheres upto a packing fraction of about 0.58 using the Bernal/Mason/Finney algorithm [3].

![](./images/811676871128252417_3.jpg)

Figure 3: Coordination number as a function of cut-off distance.

![](./images/811676871128252417_4.jpg)

Figure 4: Distribution of coordination numbers.

The algorithm consists of incrementally increasing the diameter of each particle fol- lowed by a step in which overlapping spheres are moved apart along the line of centers. Compared to serial deposition algorithms, this method yields isotropic structures. This packing was then compressed hydrostatically. Boundary conditions corresponding to a frictionless wall were imposed on three faces of the cube $(x=0, y=0, z=0)$. The remaining three walls had velocity boundary conditions corresponding to hydrostatic compression. The boundaries followed the contours of the discrete packing to minimize end effects. At each increment in the simulation the effective bulk modulus, maximum interpenetration between any two spheres, and the coordination number of the packing was computed.

These results are shown in Figure 2 as a function of relative density of the packing. The most striking feature is the sudden increase of several orders of magnitude in the effective bulk modulus of the packing at a relative density of about 0.603. This repre- sents a rigidity threshold for the packing. It is higher than that measured by allowing spheres to settle gently (0.555 [13]), but close to that measured by squeezing out fluid from a packing (0.61 [12]). This threshold corresponds to the formation and percola- tion of tetrahedral units through the packing [14]. The coordination number increases rapidly below the threshold by rearrangement of the spheres with little interpenetra- tion of spheres. Above the threshold, the coordination number increases only slowly above 6.0, and the maximum interpenetration increases rapidly as the deformation of contacts now dominates the mechanical response. The packing is shown in Figure 1.

### Characterization of random packings

The computer-generated random packing was compared to an experimentally mea- sured random packing [3,15]. In the experimental packing, whether or not two particles are in contact depends on the cut-off radius chosen to define contacts. In the generated packing, the procedure for computing the packing automatically specifies which parti- cles are in contact. Choosing a larger cut-off radius around a particle center increases the coordination number as shown in Figure 3. A cut-off radius of 1.01 was chosen for the experimental packing which corresponds to an average coordination number of 6.08 compared to 6.02 for the generated packing (see also [16,3]). The distribution about

![](./images/811676871128252417_5.jpg)

Figure 5: Distribution of packing fractions for voronoi cells.

![](./images/811676871128252417_6.jpg)

Figure 6: Effective conductivity of mixture of high and low conductivity spheres.

the mean value (Figure 4) and the radial distribution function (not shown) of the two packings are similar.

Relative densities were determined by computing the Voronoi tessellation of the two packings using the algorithm of [17]. The relative density for each particle is defined as the fraction of the Voronoi cell occupied by the particle. The distribution of relative densities for the two packings is shown in Figure 5. Note that there is no indication of crystallinity in either packing. The mean relative density for the generated and experimental packing were 0.610 and 0.636, the latter being the standard packing fraction for a random close packing [18]. This is the major difference between the two packings, the generated packing being considerably less dense. Other features computed using the Voronoi analysis were similar, e.g., the average number of faces of the Voronoi cell being 14.38 for the generated packing and 14.27 for the experimental packing. The lower density of the generated packing has probably to do with the procedure used to generate it; monotonic and isotropic loading (see also [12]).

The percolation threshold for mixtures of equal size spheres was computed by randomly assigning the spheres one of two different labels, say A and B. This procedure was repeated for increasing site fractions of A while checking for percolation of contact-sharing A particles. The probability of percolation as a function of site fraction of A and percolation probability distributions were computed using methods described in [4]. These were used to compute the site percolation threshold for the two packings. By extrapolating computed values for different sized packings using finite-size scaling [4] the thresholds are estimated to be $0.335 \pm 0.004$ for the generated and $0.315 \pm 0.001$ for the experimental packing. Both values are somewhat higher than those measured in [19] (0.27). These are in good agreement with the results of [20]: 0.326. It is also noteworthy that the threshold depends somewhat on the precise choice of cut-off radius that defines contacts in the experimental packing.

## Effective conductivity

The effective conductivity of random mixtures of spheres with very different conductivities was computed using the two packings. A fraction of the spheres $v_{f}$ were

randomly selected to have much greater conductivity than the rest. The conductiv- ity, $c^{ij}$, of contacts between these spheres was $10^{12}$ time greater than between two low-conductivity spheres. Contacts between the two types of spheres were assigned a conductivity based on a series arrangement of the two. The packing was subjected to a potential gradient across two faces and insulating boundary conditions across other faces. The effective conductivity was computed as a function of increasing site fraction. This process was repeated for several realizations. Typical results are shown in Figure 6. The effective conductivity experiences a transition from low to high conductivity at the percolation threshold $v_{c}$, which is different for the two packings. In other regards the two packings behaved very similarly. The numerical data for effective conductivity were fit with the forms:

$$
C / C_{o}=\left[v_{c} /\left(v_{c}-v_{f}\right)\right]^{n_{l}}, \quad\left(v_{f}<v_{c}\right), \quad C / C_{1}=\left[\left(v_{f}-v_{c}\right) /\left(1-v_{c}\right)\right]^{n_{u}}, \quad\left(v_{f}>v_{c}\right), \quad(7)
$$

where $C_{o}$ is the effective conductivity of the packing with only insulating particles and $C_{1}$ is the effective conductivity with only conducting particles. Mean values of the exponents for the generated packing are: $n_{l}=0.68, n_{u}=1.69$, while for the experimental packing they are: $n_{l}=0.66, n_{u}=1.72$. These are similar to each other and in the expected 'universal' range [4,21].

![](./images/811676871128252417_7.jpg)

Figure 7: Comparison of computed ef- fective conductivities with continuum models.

![](./images/811676871128252417_8.jpg)

Figure 8: Distribution of normalized gradient across an element.

The computed values are compared with two continuum models in Figure 7. Below the threshold, the Hashin-Shtrikman lower bound [21] is quite accurate for dilute con- centrations of the conducting phase. Above the threshold the Hashin-Shtrikman upper bound is accurate only very close to a packing fully occupied with conducting spheres. Also shown are the results of a modified mean-field model. In the original work [11], the effective conductivity of a packing of spheres was computed using a mean-field assumption which predicts that for an isotropic material, $C_{1}=c^{i j}(\rho n^{c} / 4 \pi R^{2})$. This was seen to be accurate within $2 \%$ for both random packings. Because the fraction of the three types of contacts is $v_{f}^{2},(1-v_{f})^{2}$, and $2 v_{f}(1-v_{f})$ respectively, this mean-field model can be applied to a composite:

$$
C=v_{f}^{2} C_{1}+\left(1-v_{f}\right)^{2} C_{o}+2 v_{f}\left(1-v_{f}\right) C_{01}, \quad(8)
$$

where $C_{01}$ is the effective conductivity of a packing consisting of interfacial links only.

This model is also an upper bound [11,16] and is shown as the mean-field model in Figure 7. Above the threshold it is more accurate than the Hashin-Shtrikman upper bound but is still very inaccurate near and below the threshold.

The mean field model is based on an assumption that the potential drop across a contact is given by the macroscopic average field. This assumption is examined in Figure 8. The gradient across each element $(\phi^j - \phi^i)/L$ is normalized by the mean-field gradient. The distribution of this normalized gradient is plotted in Figure 8. If the distribution is $f(x)$, then $\int_{-\infty}^{+\infty} f(x)dx = 1$. Moreover, if the mean-field assumption is satisfied exactly, $f(x) = \delta(1)$ and the mean of the distribution $\bar{f}(x) = \int_{-\infty}^{+\infty} f(x)xdx = 1$. If $\bar{f}(x) \approx 1$, the mean-field model is still valid. This is seen in the case of a packing where all the spheres have high conductivity $(v_f = 1.0)$. Note however, that even in this case there is a significant fraction of contacts that carry no gradient. Near the threshold, the distribution in gradients spreads out over a wide range. There is a dominant peak near zero gradient, and several contacts carry a negative normalized gradient: signifying that the local gradient is opposed to the macroscopic gradient as the flux has to adopt circuitous routes. The mean of the distribution is now far from unity and the mean-field model breaks down.

### Acknowledgements
The author is grateful to Professor H.J. Frost for providing him the coordinates of the experimentally measured random close packing and to G.W. Scherer for several helpful discussions.

### References
[1] A. Jagota, K. Mikeska, R.K. Bordia, *J. Amer. Ceram. Soc.* **73** [8] 2266-2273 (1990).
[2] P.A. Cundall, J.T. Jenkins, I. Ishibashi, *Proc. Int. Conf. on Micromechanics of Granular Media*, J. Biarez, R.Gourvès (ed.), 319-322, Balkema (1989).
[3] J.L. Finney, *J. de Phys.*, **C2** [4] C2-1 - C2-11 (1975).
[4] D. Stauffer,*Introduction to Percolation Theory*, Taylor and Francis (London) (1985).
[5] L. Limat, *Phys. Rev. B* **40** [13] 9253-9268 (1989).
[6] G.W. Scherer, A. Jagota, in Ceram. Trans., *Composites: Processing, Microstructure, and Properties*, edited by M. Sacks, American Ceramic Society, Westerville OH, 99-109 (1991).
[7] A. Jagota, E.D. Boyes, R.K. Bordia, Symposium on Synthesis and Processing of Ceramics: Scientific Issues, Fall MRS Meeting, Boston (1991).
[8] A. Jagota, to appear in *Proc. Symp. on sintering and granular materials*, ASME winter annual meeting (1992).
[9] A. Jagota, P.R. Dawson, *Acta Metall.* **36** [9] 2563-2573 (1988).
[10] R.D. Mindlin, *J. App. Mech.* **71** 259-268 (1949).
[11] A. Jagota, C-Y. Hui, *J. App. Mech.* **57** 789-791 (1990).
[12] D. Marion, A. Nur, *Physica A* **157** 575-579 (1989).
[13] G.Y. Onoda, E.G. Liniger, *Phys. Rev. Lett.* **64** [22] 2727-2730 (1990).
[14] N.N. Medvedev, A. Geiger, W. Brostow, *J. Chem. Phys.* **93** [11] 8337-8342 (1990).
[15] H.J. Frost, *Acta Metall.* **30** 889-904 (1982).
[16] M. Tassopoulos M., D.E. Rosner, *AICHE Journal*, in press (1992).
[17] W. Brostow, J-P. Dussault, B.L. Fox, *J. Comp. Phys.* **29** 81-92 (1978).
[18] G.D. Scott, *Nature* **188** 908-909 (1960).
[19] J.P. Fitzpatrick, R.B. Malt, F. Spaepen, *Phys. Lett.* **47A** [3] 207-208 (1974).
[20] W.J. Frith, R. Buscall, *J. Chem. Phys.* **95** [8] 5983-5989, (1991).
[21] D.S. McLachlan, M. Blaszkiewicz M., R.E. Newnham *J. Amer. Ceram. Soc.* **73** [8] 2187-2203 (1990).