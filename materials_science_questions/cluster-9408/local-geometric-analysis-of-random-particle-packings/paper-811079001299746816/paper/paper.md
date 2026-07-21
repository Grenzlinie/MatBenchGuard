# Soft Matter

PAPER
View Article Online
View Journal

![](./images/811079001299746816_1.jpg)

Cite this: DOI: 10.1039/c6sm01567k

Received 8th July 2016,
Accepted 6th January 2017

DOI: 10.1039/c6sm01567k

rsc.li/soft-matter-journal

## Many-body interactions in soft jammed materials

Reinhard Höhler*$^{a,b}$ and Sylvie Cohen-Addad$^{a,b}$

In jammed packings of soft frictionless particles such as foams or emulsions, stress is transmitted via a network of mechanical contacts between neighbors. In generic simplified models of such materials, particle interaction energies are assumed to be pairwise additive. We report *ab initio* simulations of foam microstructures, showing that in general, this fundamental assumption is not justified: the conservation of bubble volumes introduces a many-body coupling between all the contacts of a given particle. It strongly modifies the relation between forces and displacements at individual contacts, in a way that cannot be captured by an effective two-body interaction. We report the impact of this effect on the linear and nonlinear elastic response of ordered bubble packings with coordination numbers ranging from 6 to 12, used as simple model systems, and we present an analytical model without free parameters which is valid as long as bubbles have an approximately spherical shape. It predicts the many-body coupling of particle contact forces, as well as the macroscopic mechanical response. For packing fractions approaching the jamming transition where contact forces go to zero, we derive an asymptotic two-body interaction law. It contains a logarithmic term, yielding a critical scaling that cannot be approximated by a power law.

## 1 Introduction

The interaction energies of dispersed atoms, molecules or colloidal particles are not always pairwise additive. Due to electric or magnetic forces, the presence of additional neighbors can modify the interaction of two particles. Such many-body effects govern the structure and properties of many solutions and colloidal dispersions. $^{1,2}$ In suspensions of bubbles, droplets or other soft frictionless particles in a fluid, the interactions often have a mechanical origin: if the particle volume fraction $\phi$ is increased up to a critical value $\phi_{\text{c}}$, neighboring particles are pressed against each other and their deformation induces an elastic repulsive interaction force. This jamming transition gives rise to soft glassy materials (foams, emulsions, pastes) that respond to a small applied macroscopic stress like an elastic solid. $^{3-5}$ For $\phi > \phi_{\text{c}}$ they yield and flow if the applied stress is large enough to induce local rearrangements in the random packing. $^{6-8}$ The dissipation that accompanies particle interactions gives rise to the non-linear macroscopic viscous friction observed in flowing foams, emulsions and pastes. $^{9,10}$ Modelling these mechanical behaviors over a wide range of packing fractions requires a quantitative understanding of forces and deformations at the particle scale.

To clarify the mechanisms of yielding and flow in soft glassy materials many simulation studies of the stress induced particle dynamics have been carried out. $^{4,11-14}$ The simulations suggest that both the critical packing fraction where jamming sets in as well as the mechanical properties strongly depend on system size. $^{3,4,12}$ However, resolving the deformation of each individual particle in detail in very large packings is beyond the capabilities of existing computers. These studies therefore rely on effective two-body interaction laws, where the particles are modeled as spheres that can interpenetrate. The interaction energy is calculated from the overlap distance of these spheres, as if pairs of neighbors in contact were connected by independent repulsive harmonic or anharmonic springs. $^{4,11}$ Droplets and bubbles packed in foams and emulsions are often considered as examples of this paradigm.

However, real bubbles or droplets in 3D packings cannot overlap. They adjust their shape rather than their volume when they are brought in contact with a neighbor, because the Laplace pressure is typically orders of magnitude smaller than the internal fluid's bulk compression modulus. $^{15,16}$ When two such particles are squeezed against each other, they therefore expand laterally, as if the internal fluid were incompressible. If neighbors hinder this expansion, the force necessary to reduce the distance between the two particle centers is enhanced. This suggests that simulations and models of soft glassy materials based on an effective two-body potential may not fully capture the structure and dynamics of these materials and that a quantitative theory of many-body soft particle interactions is needed. Such a theory should answer the question whether in the limit $\phi \to \phi_{\text{c}}$ where the bubbles become more and more spherical, a two-body model of the interactions can be derived from first principles.

$^{a}$ Sorbonne Universités, UPMC Univ Paris 06, CNRS-UMR 7588,
Institut des NanoSciences de Paris, 4 place Jussieu, 75005 Paris, France
$^{b}$ Université Paris-Est Marne-la-Vallée, 5 Bd Descartes, Champs-sur-Marne,
F-77454 Marne-la-Vallée cedex 2, France

This journal is © The Royal Society of Chemistry 2017
Soft Matter

Observations of quasi-two-dimensional emulsions held between glass plates have brought experimental insight about the droplet interactions.¹⁷ The interaction forces between neighboring droplets in such a confined geometry were deduced from the observed deformations of the droplets, and an empirical two-body interaction law has been established. The reported relation between the force exerted between nearest neighbors and the center to center distance is strongly scattered, suggesting that the stiffness of a contact may depend on the way the droplets are confined by their neighbors, as expected in the presence of many-body interactions. The confinement pressure and the shear modulus in foams or emulsions also depend on the average local interaction law.⁵,⁶,¹⁶,¹⁸⁻²¹ However, the effects of disorder, coordination number changes with packing fraction, non-affine deformation and, in the case of colloidal droplets, entropic effects⁵ make it difficult to infer the bubble or droplet interaction law from such data without ambiguity. In most mechanical experiments with foams and emulsions¹⁶ the excess packing fraction $\delta\phi = \phi - \phi_{\rm c}$ is controlled with an uncertainty larger than 0.01, and a much more extended range of $\phi - \phi_{\rm c}$ is investigated. In contrast, most simulation studies⁴ focus on the asymptotic case $|\delta\phi| \ll 0.01$. Thus, both ranges of $\phi - \phi_{\rm c}$ are of interest and will be discussed in the present paper.

We report *ab initio* simulations of disordered foams or emulsions in static mechanical equilibrium, at bubble or droplet packing fractions above the jamming transition. In particular in the presence of anisotropic stress and high coordination numbers, we find significant deviations between the simulated contact forces and the predictions derived from the effective two-body interaction hypothesis.¹⁸,²² We present an analytical interaction law without free parameters that accurately predicts this many-body effect, and we demonstrate its impact on the macroscopic mechanical response of bubble or droplet packings depending on the coordination number.

## 2 Simulations

In our simulations, we focus on packings of bubbles or droplets without static friction whose radius is so large that their thermal motion is insignificant. Depending on packing fraction $\phi$ or the corresponding confinement pressure $\Pi(\phi)$, neighboring particles are pushed against each other and deformed. Their interfacial area and energy thus increase, leading to a repulsive interaction between neighbors in contact. We focus on packings where $\Pi$ is so small that the particles remain approximately spherical. For a given particle, the radial distance $R(\vec{\Omega})$ between its center of mass and its surface depends on the direction of the radius, described by a unit vector $\vec{\Omega}$ (*cf.* Fig. 1d). The local bubble deformation is described by the radial surface displacement $\delta R(\vec{\Omega}) = R(\vec{\Omega}) - R_{\rm o}$, with $\left|\delta R(\vec{\Omega})\right| \ll R_{\rm o}$, where $R_{\rm o}$ is the radius of a sphere having the same volume as the particle. Contacts are numbered by an index $i$ and identified by a vector $\Omega_i$ pointing at their centers. The radial displacement at a contact $i$ is denoted $\delta R_i$. The modulus of the force exerted at this contact, $f_i$, is determined by multiplying the contact facet area by the excess pressure in the particles with respect to the continuous phase. In the following, we use dimensionless units by scaling all forces, energies, pressures and lengths respectively by $\gamma R_{\rm o}$, $\gamma R_{\rm o}^2$, $\gamma/R_{\rm o}$ and $R_{\rm o}$ where $\gamma$ is the interfacial tension. In polydisperse packings, $R_{\rm o}$ is replaced in these scalings by its average value.

![](./images/811079001299746816_2.jpg)

Fig. 1 Packing structure. (a) Typical equilibrium structure of a disordered sample (radius polydispersity: 2.5%, packing fraction $\phi$ = 0.79). Contacts are highlighted in red. (b) Cut through a sample (radius polydispersity: 2%, packing fraction $\phi$ = 0.85) which is deformed by a 10% uniaxial isochoric strain. (c) Distribution of dimensionless contact forces in the sample shown in (a). (d) Cut through a particle confined by its neighbors. It illustrates the vector $\vec{\Omega}$ indicating a direction starting from the particle center, the radius $R(\vec{\Omega})$ in this direction and the undeformed particle radius $R_{\rm o}$.

The equilibrium structure of droplet or bubble packings is determined by minimizing the interfacial free energy density for fixed particle volumes, using the Surface Evolver software.²³ In a seminal pioneering study, it has been used to investigate how the interfacial energy of ordered packings varies with packing fraction. This variation was interpreted in terms of an effective empirical two-body particle interaction potential which depends on the packing coordination number $z$.¹⁸,²² This potential yields the following relation between the force and the displacement at a contact:¹⁸,²²

$$
f(\delta R)=
\begin{cases}
\kappa(z)\alpha(z)\dfrac{\left((1+\delta R)^{-3}-1\right)^{\alpha(z)-1}}{(1+\delta R)^4} & \text{for } \delta R < 0 \\
0 & \text{for } \delta R > 0
\end{cases} \tag{1}
$$

$\kappa(z)$ and $\alpha(z)$ are fitted functions¹⁸,²² depending only on the coordination number.† The interaction is predicted to be approximately harmonic for $z = 6$ and increasingly anharmonic for larger coordination numbers. Eqn (1) yields a relationship between $f$ and $\delta R$ which is unique in the sense that for a given

† We note that Table 1 of a pioneering publication in this field²² uses a different notation where $\kappa$ is expressed in terms of a constant $C = \kappa/(12\pi)$.

particle coordination number $z$ it depends neither on packing fraction (or $\Pi$) nor on sample deformation. Whether an effective two-body interaction law such as eqn (1) holds in disordered or strained packings has not been checked so far. Since the empirical functions $\kappa(z)$ and $\alpha(z)$ provide much flexibility, a stringent test requires disordered packings with a fixed coordination number $z$ over a range of packing fractions $\phi$. Random close packings do not have this property,⁴ since in this case, $z$ increases with $\phi$. We have constructed disordered polydisperse packings of 64 particles in mechanical equilibrium, where the coordination number of each particle is the same ($z = 12$) while the packing fraction is varied between 0.85 and 0.79, close to their jamming point, at $\phi_{\rm c} \approx 0.74$. For each packing fraction, three different realizations of the disorder are generated. The boundary conditions are periodic. As a reference, we also consider unit cells of monodisperse face centered cubic (fcc) packings with $z = 12$, for the same packing fractions. Details about the simulations and the packings are provided in the appendix. While the disorder is weak in the sense that the coordination number is fixed and independent of packing fraction, the small polydispersity (typically 2%) yields a wide distribution of contact areas and contact forces, shown on Fig. 1c. This feature provides a significant test of the particle interaction law in the absence of crystalline packing symmetry.

Fig. 2a shows the inward contact displacement $-\delta R_i$ versus the contact force $f_i$, simulated for the ordered and disordered structures with different packing fractions. The data are analyzed for the 384 contacts of each sample and they are binned. For the ordered monodisperse fcc packings with different packing fractions, the increase of $f_i$ with $-\delta R_i$ is well described by eqn (1). For disordered packings at given packing fractions, the simulated inward contact displacements $-\delta R_i$ also increase with $f_i$, as expected qualitatively. However, the relationship between $\delta R_i$ and $f_i$ is no longer unique, it depends on packing fraction. This result is not only incompatible with eqn (1), it demonstrates that a two-body interaction law cannot describe bubble or droplet contact forces in disordered foams or emulsions. Fig. 2b shows data for disordered packings elongated by an isochoric uniaxial strain of 0.1, as described in detail in Section 7.1. For a given $f_i$, $-\delta R_i$ tends to be much larger than predicted by eqn (1) for contact facets whose normal directions are perpendicular to the direction of elongation. In contrast, $-\delta R_i$ tends to be much smaller than predicted by eqn (1) for facets which are aligned with it (*cf.* Fig. 1b). In the latter case, almost half of the contact displacements $\delta R_i$ are positive. This is a consequence of particle volume conservation: since the isochoric uniaxial strain squeezes particles against each other in the planes perpendicular to the direction of elongation, they must bulge outwards along this axis. Therefore, particles can remain in contact with their neighbors along the direction of elongation at a center to center distance larger than the sum of their undeformed radii $R_{\rm o}$. The displacement at these contacts is indeed positive, in view of its definition. Two-body interaction laws like eqn (1) do not capture this effect, they imply that the interaction force must be zero and that contacts are lost whenever the contact displacement is positive.

![](./images/811079001299746816_3.jpg)

Fig. 2 Displacement versus force at individual contacts for different packing fractions. The thin line in (a) and (b) represents the prediction of the two-body interaction model eqn (1) with $\alpha = 2.5$ and $\kappa = 2.07$. For each sample, the data are binned (force interval per bin: 0.03). A typical standard deviation of $\delta R_i$, divided by the square root of the number of data per bin, is shown at the top of (a) and (b). (a) Monodisperse face centered cubic packings (big symbols) or polydisperse disordered packings (small symbols), in the absence of anisotropic stress. The thick dashed line represents the prediction of the many-body interaction model eqn (6), applied to a face centered cubic monodisperse packing. (b) Weakly polydisperse packings subjected to an isochoric uniaxial strain of 10%.

## 3 Analytical many-body interaction model

To model the impact of particle volume conservation on local interaction forces, we rely upon the seminal theory of capillary droplet interactions by Morse and Witten.¹⁵ Its starting point is Laplace's law, relating the mean curvature of a droplet surface to the difference between the internal and external pressures acting on it. Expressing the curvature of a weakly deformed particle interface in terms of angular derivatives of $R(\vec{\Omega})$ yields a differential equation which is linearized and solved using a Green's function. It predicts $\delta R\left(\vec{\Omega}_i\right)$, the radial surface displacement at a position $\vec{\Omega}_i$, induced by a central unit point force of modulus $f_j$, pushing the particle surface at a position identified by the vector $\vec{\Omega}_j$. Neighboring drops in real emulsions at packing fractions close to $\phi_{\rm c}$ do not actually exert point forces on each other, the forces are transmitted *via* thin liquid

films forming facets whose diameter is much smaller than the droplet size. However, at distances from the contacts, measured along the surface, which are much larger than the facet diameter, the point force model provides a good approximation for the real droplet shape. $^{15}$ The Green's function only depends on the angle between $\vec{\Omega}_{i}$ and $\vec{\Omega}_{j}$, denoted $\theta_{i j}:^{15}$

$$
G\left(\theta_{i j}\right)=-\frac{1}{4 \pi}\left\{\frac{1}{2}+\frac{4}{3} \cos \theta_{i j}+\cos \theta_{i j} \ln \left[\sin ^{2}\left(\theta_{i j} / 2\right)\right]\right\} \tag{2}
$$

This result has been used by Buzza and Cates $^{24}$ to derive a linear response function, relating infinitesimal changes of contact force $\mathrm{d} f_{i}$ to corresponding changes $\mathrm{d} R_{i}=\mathrm{d}\left(\delta R_{i}\right)$ of contact displacement $\delta R_{i}$:

$$
\mathrm{d} R_{i}=\sum_{j} \Gamma_{i j} \mathrm{~d} f_{j} \tag{3}
$$

The sum is performed over all the contacts of the considered bubble. $\Gamma_{i j}$ is defined as: $^{24}$

$$
\Gamma_{i j}=
\begin{cases}
\frac{1}{24 \pi}\left(11+6 \ln \left[\frac{f_{i}}{8 \pi}\right]\right) & \text { for } i=j \\
-G\left(\theta_{i j}\right) & \text { for } i \neq j
\end{cases} \tag{4}
$$

The sign of $\Gamma_{i j}$ in eqn (4) is opposite to the one in ref. 24, to make it consistent with our notation.

From these previous results, we deduce the contact displacements $\delta R_{i}$ at a given particle confined in a packing, subjected to a set of contact forces $f_{j}$. Let us imagine that by removing quasi-statically its neighbors, we simultaneously relax to zero all the forces acting on this particle, without modifying the directions $\Omega_{j}$ in which they are applied. We replace each force $f_{j}$ by $\varepsilon f_{j}$ where the dimensionless variable $\varepsilon$ is relaxed from 1 to 0. By integrating over the displacement changes $\mathrm{d} R_{i}$, given by eqn (3), that accompany this relaxation we deduce the initial displacement $\delta R_{i}$ of each contact:

$$
\delta R_{i}=-\sum_{j} \int_{\varepsilon=1}^{0} \Gamma_{i j}\left(\varepsilon f_{i}, \theta_{i j}\right) f_{j} \mathrm{~d} \varepsilon \tag{5}
$$

Since by construction the sum of the contact forces remains equal to zero during the relaxation, the particle center cannot move and the angles $\theta_{i j}$ remain fixed. Using eqn (4) we predict:

$$
\delta R_{i}=\frac{1}{24 \pi}\left[5+6 \ln \left(\frac{f_{i}}{8 \pi}\right)\right] f_{i}-\sum_{i \neq j} G\left(\theta_{i j}\right) f_{j} \tag{6}
$$

$\delta R_{i}$ is the sum of two terms which we will denote $\delta R_{i}^{\text {loc }}$ and $\delta R_{i}^{\text {nl }}$. $\delta R_{i}^{\text {loc }}$ is a local contribution, depending only on $f_{i}$, while $\delta R_{i}^{\text {nl }}$, is non-local because it depends on forces at the contacts $j \neq i$.

Since this model relies on a linearized expression describing the interfacial curvature, we check its range of validity numerically. We first consider fcc packings where all contact forces are of equal magnitude. Fig. 2a shows that in this case, eqn (6) fully agrees with the simulation data up to forces close to 0.4. We now consider the disordered as well as the strained structures studied on Fig. 2. The quantities $\delta R_{i}, f_{i}$ and $\theta_{i j}$ are determined for all simulated contacts and we calculate from these data $\delta R_{i}^{\text {nl }}$. Eqn (6) predicts that plotting $\delta R_{i}^{\text {loc }}=\delta R_{i}-\delta R_{i}^{\text {nl }}$ versus $f_{i}$ must yield a mastercurve, given without free parameters by the first term of eqn (6). Fig. 3 shows excellent agreement with this prediction, for monodisperse and polydisperse structures at different packing fractions, with or without applied strain. These tests show that eqn (6) accurately describes the many-body interactions in foams and emulsions at packing fractions in the neighborhood of the jamming transition. This is consistent with a previous prediction $^{15}$ that Morse and Witten's model of droplet interactions should be valid only if all the dimensionless contact forces are much smaller than 1. As the contact forces go to zero at the jamming point, the ratio of the second and the first term in eqn (6) goes to zero as $1 / \ln f$, suggesting that the many-body interaction effects decrease on the average logarithmically at the jamming point. This feature will be discussed in detail in Section 5.

![](./images/811079001299746816_4.jpg)

Fig. 3 Test of the proposed many-body interaction law. The local part $\delta R_{i}^{\text {loc }}$ of the contact displacement, defined as the first term in eqn (6), is plotted versus the force $f_{i}$ acting at the same contact, for all of the simulations shown on Fig. 2a and b. The colors and symbols indicate different packing fractions and strains, as in Fig. 2. The line represents the theoretical prediction of the many-body interaction model without free parameters, given by the first term in eqn (6).

## 4 Impact of many-body interactions on the macroscopic mechanical response of deeply jammed foams and emulsions

The simulations and calculations reported in the previous sections demonstrate that models of bubble or droplets interaction forces generally need to take into account the coupling between all contacts of a given particle due to the conservation of its internal volume. The data show that in the presence of anisotropic stress, the effective two-body interaction law eqn (1) cannot capture this effect. These results raise the question to what extent many-body effects have an impact on the macroscopic mechanical properties of foams or emulsions. As a simple model system, we consider in this section the unit cell of a cubic face centered packing of bubbles in the absence of gravity, subjected to isotropic compression, shear or uniaxial strain. We first present the calculation used to determine the

stress for a given interaction law, depending on the applied strain. This method can be used for studying any centrosymmetric ordered packing.

### 4.1 Analytical calculation of the stress in strained ordered packings
Due to symmetry, the particle centers in centrosymmetric packings must follow affine displacements,³⁰ given by a vector $\mathbf{U}$ depending on the initial particle position $\mathbf{x}$. In contrast, the deformation of the bubble or droplet shapes that minimizes interfacial energy is non-affine. We use the displacement gradient tensor to describe the particle center displacement:²⁵

$$
F_{kl} = \frac{\partial U_k}{\partial x_l}. \tag{7}
$$

In the presence of a deformation described by $F_{kl}$, the vector $\mathbf{r}_{ij}^o$ initially linking the centers of two neighboring particles $i$ and $j$, becomes $\mathbf{r}_{ij}$ with

$$
r_{ij,k} = \sum_l F_{kl} r_{ij,l}^o. \tag{8}
$$

The symbol $r_{ij,l}$ denotes the component $l$ of the vector $\mathbf{r}_{ij}$. Contacts are by symmetry located at the midpoints of lines connecting neighboring bubble centers. For given bubble radii and center positions the contact displacements $\delta R_i$ can therefore directly be calculated.

The contribution of the particle interaction forces to the macroscopic stress $\sigma_{\alpha\beta}$ in a packing of volume $V$ is given by the Irwin Kirkwood tensor.⁴

$$
\sigma_{\alpha\beta} = \frac{1}{2V} \sum_{i\neq j} f_{ij,\alpha} r_{ij,\beta} \tag{9}
$$

$f_{ij,\alpha}$ is the component $\alpha$ of the force at the contact between particles $i$ and $j$, and the sum is performed over all particles in the packing. Eqn (8) and (9) combined with an interaction law then determine the stress in the packing for a macroscopic deformation given by $F_{kl}$ or a strain tensor derived from it.

In the case of the two-body law eqn (1) this calculation does not require any further preparation; we use the parameters $\alpha$ and $\kappa$ specified in the literature and recalled in Table 1.

In contrast, the many-body interaction law eqn (6) is non-linear, and we use the following iterative algorithm to determine the forces in this case. As a starting point, all contact forces can roughly be estimated using eqn (1). We insert this first estimate into the logarithmic term in eqn (6), so that it becomes a linear set of equations. The contact forces can now be deduced from the contact displacements using standard numerical methods. We then replace in the logarithmic term of eqn (6) our first estimate of each contact force by the new values and evaluate the forces once again from the set of linear equations. This process is pursued iteratively until the set of forces $f_i$ no longer evolves, indicating that a self consistent mechanical equilibrium of the packing is obtained.

<table>
<caption>Table 1 This table recalls the parameters $\alpha$ and $\kappa$ recommended in the literature to model droplet interaction using eqn (1), depending on the coordination number $z$ of the packing structure. In this previous work,²² a notation with a constant $C$ defined as $C = \kappa/(12\pi)$ was used</caption>
<thead>
<tr>
<th>Packing structure</th>
<th>$\phi_c$</th>
<th>$z$</th>
<th>$\kappa$</th>
<th>$\alpha$</th>
</tr>
</thead>
<tbody>
<tr>
<td>fcc</td>
<td>$\pi/(3\sqrt{2})$</td>
<td>12</td>
<td>2.07</td>
<td>2.5</td>
</tr>
<tr>
<td>bcc</td>
<td>$\pi\sqrt{3}/8$</td>
<td>8</td>
<td>1.01</td>
<td>2.3</td>
</tr>
<tr>
<td>sc</td>
<td>$\pi/6$</td>
<td>6</td>
<td>0.79</td>
<td>2.2</td>
</tr>
</tbody>
</table>

### 4.2 Strain response of ordered packings: comparison between analytical calculations and Surface Evolver simulations
We use the algorithm presented in the previous section to predict the stress in a particle packing, assuming either many-body interactions eqn (6) or two-body interactions eqn (1). These results are compared to *ab initio* Surface Evolver simulations. Fig. 4 shows results obtained for isotropic compression of the packing, expressed here in terms of the continuous phase volume fraction. The prediction derived from the two-body potential is in excellent agreement with the Surface Evolver simulation. This agreement was to be expected since the two-body potential is deduced from a fit to such simulations, for the same range of contact displacements. The data on Fig. 4 suggest that the many-body interaction law predicts to a good approximation the same confinement pressure, up to packing fractions close to 0.83, although its mathematical form without free parameters is different from the one of the two-body law eqn (1). A limit of validity for increasing confinement pressures is indeed expected for the many-body law, because when the bubbles become highly non-spherical, the linearization of the

![](./images/811079001299746816_5.jpg)

Fig. 4 Confinement pressure in an fcc bubble packing, normalized by the ratio of surface tension to bubble radius, plotted *versus* packing fraction. The filled circles show *ab initio* simulation results obtained using the surface evolver software, which we consider as a reference. The thick and thin lines respectively show the predictions derived from the two-body interaction model eqn (1) and the many-body interaction model eqn (6), as explained in the text.

curvature expression used by Morse and Witten is no longer a good approximation. We recall that for this approximation to hold, the dimensionless contact forces must be much smaller than one.¹⁵ Fig. 5 shows the stress response of the packing to isochoric uniaxial deformation: the $x_3$ coordinates of the particle centers are multiplied by an extension ratio $\lambda$ while the $x_1$ and $x_2$ coordinates are multiplied by $\lambda^{-1/2}$, to ensure volume conservation.²⁵ We recall that the $x_1$, $x_2$ and $x_3$ axes are chosen along the directions of fourfold symmetry of the packing. This deformation induces a difference between the diagonal components of the stress tensor called normal stress difference. The dimensionless contact forces $f$ predicted by the many-body model in this range of parameters remain smaller than 0.3, in agreement with the condition $f_i \ll 1$ required for the model to be valid. Fig. 5 shows indeed a good agreement between the Surface Evolver calculations and the many-body interaction model. The prediction of the two-body potential model eqn (1) strongly deviates from the Surface Evolver simulation results. Physically, this deviation arises because the free parameters of eqn (1) are tuned to reproduce the bubble response to isotropic compression: if the forces at all of the contacts push the bubble inward, its interfaces must bulge outwards around the contacts to conserve the bubble volume. This deformation costs much interfacial energy, making the contacts appear to be stiffer than in the case of uniaxial deformation. In this latter case, contact forces elongate the bubble in the $x_3$ direction and shorten it in the $x_1$ and $x_2$ directions; this mode of deformation naturally conserves the bubble volume. Therefore, for a given contact strain, the interfacial deformation and the contact stiffness are smaller than in the case of isotropic deformation and the two-body model over-predicts the uniaxial stress response. Similar remarks apply to the shear response, illustrated on Fig. 6. While the two-body calculation fails to predict the Surface Evolver data, the many-body calculation is in good agreement with them, up to a shear strain close to 0.2. At larger strains, up to 0.4, small deviations progressively set in. This can be explained by the magnitude of the largest contact forces which remain below 0.4 up to a strain of 0.2. At a strain of 0.4, the largest contact forces approach 1, indicating that the limit of validity of the many-body model is reached here. This means that packings subjected to an even higher shear strain can only be modeled using eqn (6) for smaller packing fractions where the confinement pressure is lower. The results reported in this section illustrate that many-body interactions in foams and emulsions not only have an large impact on interaction forces at the level of individual bubbles, but also on the macroscopic mechanical response.

![](./images/811079001299746816_6.jpg)

Fig. 5 Normal stress difference $\sigma_{33} - \sigma_{11}$ in an fcc packing subjected to an isochoric uniaxial deformation. The packing is elongated by a ratio of extension $\lambda$ along the $x_3$ axis and by a factor $\lambda^{-1/2}$ in the $x_1$ and $x_2$ directions. The coordinate system is aligned with the axes of fourfold symmetry of the packing. The packing fraction is 0.8. The plot compares the predictions derived from the two-body interaction model eqn (1) and the many-body interaction model eqn (6) to ab initio simulation results obtained using the Surface Evolver software.

![](./images/811079001299746816_7.jpg)

Fig. 6 Shear stress $\sigma_{13}$ in an fcc bubble packing in response to a shear deformation in the $x_3$ direction. The coordinate system is aligned with the directions of fourfold symmetry. The packing fraction is 0.8, the lines styles and symbols have the same significance as in Fig. 5. The plot compares the predictions derived from the two-body interaction model eqn (1) and the many-body interaction model eqn (6). Ab initio to simulation results obtained using the Surface Evolver software.

## 5 Confinement pressure and linear mechanical response of ordered packings close to the jamming transition

In experiments with foams and emulsions, the difference $\delta\phi = \phi - \phi_c$ is hard to control with an accuracy better than 1%. The pioneering work²² where the interaction law eqn (1) was first proposed was mainly focused on the regime where $\delta\phi$ is large enough to be resolved experimentally. However, these authors also investigated the asymptotic behavior in the limit $\delta\phi \to 0$.

It is not possible to perform Surface Evolver simulations for $\delta \phi \ll 1\%$: in this regime, the size of the contacts is orders of magnitude smaller than the droplet size, and the number of finite elements required to represent the bubble interfaces accurately diverges. The regime $\delta \phi \to 0$ therefore requires an analytical investigation. As a model system, Lacasse *et al.* considered a single 3D droplet confined between two parallel plates in the absence of gravity,²² a case which they solved without approximations by calculating the droplet shape that minimizes interfacial energy. The environment of such a droplet appears to be quite different from the typical one in a 3D emulsion where droplets have on the average at least six contacts. However, as we will show below in the framework of Morse and Witten's theory, the responses of the contacts of a given droplet become independent of each other (and thus of the coordination number) in the limit of small applied forces. Therefore, studying the case of two contacts does provide insight about the asymptotic interaction behavior of bubbles or droplets in foams and emulsions for $\delta \phi \to 0$. Using the calculated droplet shape, Lacasse *et al.* determined the contact force, depending on the droplet deformation imposed by the gap between the plates. Expressed in our notation, the following logarithmic scaling was found in the limit $\delta \phi \to 0$:

$$
\delta R \propto f \ln(f), \tag{10}
$$

We now compare the prediction of the interaction law eqn (6) derived from Morse and Witten's theory to Lacasse *et al.*'s analytical result eqn (10). In the limit $\delta \phi \to 0$, the logarithm in the first term in eqn (6) diverges, and therefore this term dominates over the second one. This means that the coupling between contacts due to volume conservation, expressed by this second term, becomes insignificant. The many-body model is in this limit reduced to a two-body model where contacts of a given bubble or droplet respond independently from each other. This response is predicted by the remaining first term of eqn (6).

$$
\delta R_{i}=\frac{1}{24 \pi}\left[5+6 \ln \left(\frac{f_{i}}{8 \pi}\right)\right] f_{i} \tag{11}
$$

In the limit $f \to 0$ (i.e. at the jamming transition) its form is in full agreement with Lacasse *et al.*'s prediction eqn (10). The logarithmic dependency on the contact force in eqn (11) indicates that the critical scaling of the mechanical behavior of emulsions and foams at the jamming transition where contact forces go to zero cannot be modeled accurately using power-law interaction models such as eqn (1). Moreover, eqn (11) has no free parameters and does not depend on the coordination number, again in contrast with eqn (1).

### 5.1 Confinement pressure

To study how the two-body interaction behavior described by eqn (11) sets in at the jamming transition, we calculate the confinement pressures in fcc, bcc and sc bubble packings as a function of $\delta \phi$, using the Irwin Kirkwood relation, as explained in Section 4.1. We first do this by taking into account only the first term of eqn (6) (the two-body contribution eqn (11)).

Then we perform the same calculation taking also into account the many-body contribution (i.e. both terms in eqn (6)). The ratio between these two results must be equal to one if the many-body coupling is negligible, and it is plotted *versus* $\delta \phi$ on Fig. 7. We see that the ratio approaches the value one as $\delta \phi \to 0$ but the convergence is slow. Even for $\delta \phi$ as small as $10^{-6}$, the ratio only reaches the value 0.9 for all investigated packing structures. Moreover, the impact of many-body effects decreases with decreasing coordination number. We conclude that for practical purposes, a two-body approximation of the interaction law based on the first term of eqn (6) may be useful for $\delta \phi \ll 0.01$, depending on the required accuracy. The onset of two-body behavior could depend on disorder and the applied deformation, the investigation of all these features is beyond the scope of the present study.

To predict the confinement pressure at packing fractions down to the jamming transition, the analytical “cone model” has recently been proposed.²⁶ It applies to ordered bubble packings where all first neighbors are equivalent by symmetry, and the shapes of bubble contacts are approximated as conical surfaces. The confinement pressure is predicted as follows in this framework.

$$
\Pi=-\frac{z \phi^{2}}{3 \phi_{\mathrm{c}}^{2}} \frac{\phi-\phi_{\mathrm{c}}}{\ln \left(\phi-\phi_{\mathrm{c}}\right)} \tag{12}
$$

Fig. 8 and 9 provide an overview of the variations of confinement pressure with packing fraction close to the jamming transition for fcc, bcc and sc structures predicted by our model eqn (6). In Fig. 10 we compare them to the predictions of the cone model

![](./images/811079001299746816_8.jpg)

Fig. 7 This plot shows the ratio of two predictions for the confinement pressure in face centered cubic ($z$ = 12), body centered cubic ($z$ = 8) and simple cubic ($z$ = 6) bubble or droplet packings *versus* $\phi - \phi_{\mathrm{c}}$. The first is the logarithmic two-body approximation eqn (11), obtained by neglecting the second term in eqn (6). The second is the full many-body prediction eqn (6). The slow convergence of this ratio towards one with decreasing packing fraction indicates how many-body effects asymptotically disappear at the jamming transition.

![](./images/811079001299746816_9.jpg)

Fig. 8 Dimensionless confinement pressure for simple cubic (sc) and face centered cubic (fcc) droplet packings, versus the difference between the packing fraction $\phi$ and its critical value $\phi_c$ below which neighboring particles are no longer in touch. The color and decoration of the curves identify predictions derived either from the effective two-body approximation eqn (1) or from the many-body model eqn (6) as explained in Section 4.1.

![](./images/811079001299746816_10.jpg)

Fig. 9 Dimensionless confinement pressure for body centered cubic (bcc) droplet packings, versus the difference between the packing fraction $\phi$ and its critical value $\phi_c$ below which neighboring particles are no longer in touch. The color and decoration of the curves identify predictions derived either from the effective two-body approximation eqn (1) or from the many-body model eqn (6) as explained in Section 4.1.

eqn (12). The good agreement between these two models which use different analytical approaches is remarkable since neither of them have adjustable parameters. The validity of the many-body model at small excess packing fractions is indeed expected: we have shown that on the one hand, it agrees with Surface Evolver simulations for excess packing fractions down to $\delta \phi=0.05$ ( $c f$. Sections 2 and 3); on the other hand, the key perturbative assumption of Morse and Witten's model that the droplets are approximately spherical is increasingly well fulfilled when $\phi$ approaches $\phi_{\mathrm{c}}$.

The analytical investigations discussed so far in this section aim to represent accurately the interactions encountered in real foams or emulsions. Many numerical studies of soft particle packings near the jamming transition $^{4}$ have followed a more schematic approach based on harmonic or anharmonic power law two-body interaction laws, such as eqn (1). In the following, we investigate to what extent such generic numerical models describe the mechanical response of weakly compressed bubbles or droplets.

Fig. 8 and 9 compare the confinement pressures predicted either by the power law two-body model eqn (1) or by the many-body model eqn (6) close to the jamming point. Three ordered packings with different coordination numbers $z$ are investi gated: fcc $(z=12)$, bcc $(z=8)$ and sc $(z=6)$. For $\delta \phi \gg 0.01$, the two-body and the many-body results are very similar for all packing structures, in agreement with Fig. 4. The success of the two-body approximation eqn (1) in this regime is indeed expected since its parameters $\alpha$ and $\kappa$, recalled in Table 1, are tuned for each structure to achieve a good agreement with Surface Evolver Simulations of the confinement pressure in the same range of packing fractions. However, the predictions derived from the two interaction laws start to deviate for $\delta \phi$ below $\approx 0.01$. For fcc packings the discrepancy reaches almost two orders of magnitude at $\delta \phi=10^{-6}$. Fig. 10 illustrates that the deviation decreases with decreasing coordination number. It is smallest for simple cubic packings which have the same coordination number $z=6$ as random close packings on the average at the jamming transition. Bcc packings have a coordi nation number of 8, typically found in random close packings

![](./images/811079001299746816_11.jpg)

Fig. 10 The confinement pressures predicted either by the cone model eqn (12) or by the power law two-body model (using eqn (1) cf. Section 4.1) are both divided by the one predicted by the many-body model, (using eqn (6) cf. Section 4.1). These ratios are plotted versus the excess packing fraction $\delta \phi=\phi-\phi_{c}$ for fcc, bcc and sc packings. The agreement between the cone model and the many-body model is good while the prediction of the power law two-body model deviates significantly from both of them.

![](./images/811079001299746816_12.jpg)

Fig. 11 The linear uniaxial modulus $E$ for simple cubic (sc) bubble or droplet packings is plotted versus the excess packing fraction $\delta\phi=\phi-\phi_{\rm c}$. The three curves are the predictions derived either from the power law two-body interaction model eqn (1), the many-body model eqn (6) or the non-standard two-body model eqn (11) derived from eqn (6) in the limit $\delta\phi\rightarrow0$.

at packing fractions a few percent above the jamming transition. In this case, Fig. 10 shows deviations reaching an order of magnitude for $\phi-\phi_{\rm c}=10^{-6}$. The increase of discrepancies between the predictions of the power law two-body model and the many-body model for $\delta\phi\rightarrow0$ reflects that the empirical interaction law eqn (1) does not have the theoretically expected asymptotic scaling property eqn (10).

### 5.2 Elastic response to uniaxial strain of shear

We have investigated the elastic response of fcc, bcc and sc packings to uniaxial deformation and shear, over a range of deformations sufficiently small for the stress to vary linearly with strain. The directions of displacement are chosen along the axes of fourfold symmetry of the packings that we will call $x_1$, $x_2$ and $x_3$. For the packing fractions and interactions considered here, bcc packings are unstable to uniaxial strain while sc packings are unstable to simple shear. These two cases are therefore not discussed in the following. In the uniaxial case, the response is described by the modulus $E=(\sigma_{33}(\lambda)-\sigma_{11}(\lambda))/(\lambda-1)$. As explained in Section 4, $\lambda$ describes the extension of the structure in the $z$ direction; here, its value is chosen sufficiently close to one for the strain induced normal stress difference to vary linearly with $\lambda-1$. All results plotted in Fig. 11-14 for structures with coordination numbers ranging from 6 to 12 show the same qualitative behavior: the elastic moduli predicted by the many-body model decrease slowly in the limit $\delta\phi\rightarrow0$, in agreement with previous results in the case of cubic packings$^{24}$ where an asymptotic scaling of the elastic modulus $\propto1/\ln(\delta\phi)$ was predicted. The non-standard two-body approximation eqn (11), containing a logarithmic dependency on $f$, that we derive from eqn (6) in the limit $\delta\phi\rightarrow0$ provides a good approximation. However, for $\delta\phi\gg0.01$, significant deviations occur, especially in the case of the coordination number 6. They can be seen more clearly in plots showing the ratio of the predictions deduced from eqn (11) or eqn (6), presented in the appendix, Section 7.5. The elastic moduli derived from the power-law two body model eqn (1) strongly deviate from those predicted by the full many-body model, especially in the limit $\delta\phi\rightarrow0$. These deviations increase with the coordination number of the packing.

![](./images/811079001299746816_13.jpg)

Fig. 12 The shear modulus $G$ for body centered cubic (bcc) bubble or droplet packings is plotted versus the excess packing fraction $\delta\phi=\phi-\phi_{\rm c}$. The three curves are the predictions derived either from the power law two-body interaction model eqn (1), the many-body model eqn (6) or the non-standard two-body model eqn (11) derived from eqn (6) in the limit $\delta\phi\rightarrow0$.

![](./images/811079001299746816_14.jpg)

Fig. 13 The linear uniaxial modulus $E$ for face centered cubic (fcc) bubble or droplet packings is plotted versus the excess packing fraction $\delta\phi=\phi-\phi_{\rm c}$. The three curves are the predictions derived either from the power law two-body interaction model eqn (1), the many-body model eqn (6) or the non-standard two-body model eqn (11) derived from eqn (6) in the limit $\delta\phi\rightarrow0$.

One may optimize the agreement between the many body model and the effective two-body model eqn (1) by tuning its fit

![](./images/811079001299746816_15.jpg)

Fig. 14 The shear modulus $G$ for face centered cubic (fcc) bubble or droplet packings is plotted versus the excess packing fraction $\delta \phi = \phi - \phi_{\rm c}$. The three curves are the predictions derived either from the power law two-body interaction model eqn (1), the many-body model eqn (6) or the non-standard two-body model eqn (11) derived from eqn (6) in the limit $\delta \phi \to 0$.

parameters $\alpha$ and $\kappa$. The values that we used in this section are those reported in the literature, but for investigations focused on a restricted range of excess packing fractions and a particular aspect of the mechanical response, better agreement may be possible with other fit parameter values. However, no such adjustment can provide the correct asymptotic scaling given by eqn (10).

## 6 Conclusion

Our simulations of foam or emulsion microstructures show that in general, the deformation at a given contact of a bubble or droplet depends on the entire set of forces exerted by its first neighbors. We show that this many-body effect cannot be captured by an effective two-body potential. In the framework of a theory based on first principles proposed by Morse and Witten, we derive a model without free parameters which predicts the interaction law quantitatively, provided that all dimensionless contact forces are much smaller than one. For monodisperse and weakly polydisperse packings with fixed coordination number $z=12$, the model correctly predicts the macroscopic stress response to shear, uniaxial deformation and isotropic strain found in *ab initio* simulations. Assuming an effective two-body interaction leads to predictions of these quantities that are correct for isotropic strain, but that strongly deviate from these reference data if the case of anisotropic strain.

Previous simulations and experiments with emulsions have shown that the average coordination number in a random packing varies rapidly with packing fraction. To study the impact of the coordination number, we have calculated the linear mechanical response of face centered cubic ($z=12$), body centered cubic ($z=8$) and simple cubic ($z=6$) ordered droplet packings, using our interaction model derived from Morse and Witten's theory. We find that the impact of many-body effects decreases with decreasing coordination number. Our calculations show significant differences between the predictions of the mechanical response of ordered packings derived either from the power law two-body interaction model eqn (1) or from Morse and Witten's theory, even in the limit $\phi \to \phi_{\rm c}$.

In this limit we derive a new two-body interaction law in the framework of the Morse and Witten theory. It contains a logarithmic term and can therefore not be represented as a power law. This interaction law without free parameters correctly predicts the confinement pressure and the linear elastic response of ordered packings in the limit $\phi \to \phi_{\rm c}$ in the range of investigated coordination numbers 6-12. In further work we intend to explore the usefulness of this non-standard two-body approximation for simulating the mechanical response of disordered foams and emulsions very close to the jamming transition.

The structure and rheology of foams, emulsions and similar soft packings without static particle friction in the "deeply jammed" regime has recently been investigated by several simulations and models on the particle scale, ${^{9,10,27}}$ and we hope that our results may help to develop them further. Fig. 2 illustrates that for large strains, many contacts can persist in a droplet packing even though they should be disconnected according to two-body interaction models. Such changes of the coordination in the packing can modify the yielding and non-affine local deformation behavior. Moreover, since the nonlinear viscous friction between particles ${^{9,10}}$ in flowing samples is governed by contact forces, their modification by many-body effects needs to be considered in models of energy dissipation in foams and emulsions.

Simulating the structure and mechanical response of random close packings is indeed an important perspective for extending the present work. Surface Evolver simulations of disordered bubble or droplet packings are extremely difficult to perform near the jamming transition where the size of the contacts is typically orders of magnitude smaller than the bubble or droplet diameter. The interaction model eqn (6) can be used to model such packings. It thus provides the opportunity to study the quasistatic local mechanical response of emulsions and foams, governed by the interplay of many-body interactions, of the singular change of coordination number with excess packing fraction and of the non affinity of the deformation. $^{4}$

In this context, an experimental validation of our model in the case of fully disordered packings would be very useful. Published data for disordered quasi-2D emulsions confined between glass plates are unfortunately outside its range of validity since in these experiments, the droplets were squeezed between the plates so strongly that the dimensionless forces at the contacts between the droplets and the plates were not much smaller than one. $^{17}$ Observations of quasi 2D emulsions with almost spherical droplets or highly resolved confocal microscopy images of 3D emulsions would provide a valuable reference.

We expect a large class of soft incompressible solid particles (with Poisson ratio close to 0.5) to present many-body interactions in disordered packings, similar to those that we have

evidenced for droplets and bubbles. The form of the interaction law may vary, but the physical constraint imposed by particle volume conservation is generic. Couplings between interactions at different contacts have indeed been evidenced by finite element simulations of soft solid disk packings. $^{28}$ We therefore expect that the work reported here will help to bridge the gap between generic models of soft glassy materials and the flow behavior of real foams, emulsions and soft pastes.

## 7 Appendix

### 7.1 Simulation methods
In our simulations, the interfaces between the particles and the surrounding continuous phase are represented as assemblies of triangular facets, each defined by three vertices. The boundary conditions of the particle packing are periodic. Multiplying the total facet area by the surface tension yields the facet's interfacial energy, and a conjugate gradient algorithm, implemented in the Surface Evolver software, $^{18}$ is used to determine for a given set of fixed particle volumes the particle shapes that minimize the total interfacial energy. This minimization takes into account the contacts with neighbors. Wherever two particles touch, the thin film at their contact is represented as an assembly of facets, whose surface tension is twice the one of a single gas liquid interface. Thus, we do not model the finite thickness of contact films in real foams or emulsions, instead, we focus on the case where this thickness is negligible because it is orders of magnitude smaller than the particle size.

To study disordered structures, we first simulate assemblies of 64 identical particles, forming a face centered cubic packing where the coordination number of each particle is 12. The structure will be described using a cartesian coordinate system whose axes are aligned with the axes of fourfold symmetry of the packing. To make these packings polydisperse, we transfer a small amount of volume among two randomly chosen bubbles, and we equilibrate the structure using the conjugate gradient algorithm. This procedure is applied iteratively, and as a con- sequence, the contact areas and contact forces that were initially identical follow a distribution that becomes wider and wider. Finally, some of the contact areas shrink to zero, indicating that a contact is lost so that the particle coordination number changes. We stop the iterations before this happens, and thus obtain polydisperse equilibrated structures with a wide distribu- tion of contact forces (see Fig. 1d), and the same coordination number $z=12$ for each particle.

To determine whether an equilibrium structure is reached, we monitor the evolution of the interfacial energy upon the conjugate gradient search. When the energy no longer decreases, the mesh is refined. This procedure is continued iteratively until further refinement does not reduce the total energy within numerical accuracy. Under these conditions, each bubble is typically represented by 5200 quadratic finite elements.

Uniaxial deformations are applied to the simulated samples by small steps, following a procedure used in many previous Surface Evolver studies of foam rheology. $^{29}$ We first apply an affine displacement to each of the vertices of the structure, as well as to the unit cell that defines the periodic boundary conditions. This can be done using the displacement gradient tensor $F$, already used in eqn (14). $v_{k}^{o}$ are the initial coordinates of vertex number $k, v_{k}$ are the vertex coordinates obtained after the deformation.

$$
v_{k}=\sum_{l} F_{k l} v_{k}^{o}. \tag{13}
$$

In our simulations, we apply an extension factor called $\lambda$ along the $x_{3}$ direction and factors $\lambda^{-1 / 2}$ in the $x_{1}$ and $x_{2}$ directions. A uniaxial deformation of $10 \%$ corresponds to $\lambda=1.1$. The expression of $F$ for this uniaxial strain is. $^{25}$

$$
F_{k l}=\left[\begin{array}{ccc}
\lambda^{-1 / 2} & 0 & 0 \\
0 & \lambda^{-1 / 2} & 0 \\
0 & 0 & \lambda
\end{array}\right] \tag{14}
$$

The deformation of the unit cell is affine and it sets the mechanical boundary conditions, but the minimum interfacial energy of the microstructure corresponds to non-affine local deformations. We use the Surface Evolver to relax the structure towards this state. Upon this relaxation we monitor all the components of the stress tensor as well as the energy of the packing and we stop the simulations when all of these quantities have converged to a constant upon the iterations.

### 7.2 Excess pressures in the particles and calculation of contact forces
Fig. 15 shows a typical distribution of internal pressure differences between neighboring particles $\Delta P_{\mathrm{i}}$, divided by the average of the capillary pressures $P_{\mathrm{i}}$. The standard deviation of this distribution is smaller than $2 \%$. In view of Laplace's law, this means that the curvature of contact films is two orders of magnitude smaller that the curvature of the interfaces between the internal phase of the particles and the continuous phase surrounding them. As a con- sequence, the contacts can be considered to a good approximation

![](./images/811079001299746816_16.jpg)

Fig. 15 Distribution of internal pressure differences between particles in contact. The data are normalized by the average excess pressure with respect to the continuous phase. The sample has a packing fraction of 0.85.

as flat, and the contact forces are simply expressed as the excess pressure multiplied by the contact area.

### 7.3 Central orientation of contact forces
We have performed Surface Evolver simulations to check that in the investigated range of structures and packing fractions, the particle interaction forces are to a good approximation central: lines linking the centers of mass of two particles that touch are perpendicular to the contact film where they meet within $2^\circ$ in unstrained samples specified in Fig. 2a and within $4^\circ$ in strained samples specified in Fig. 2b. The orientation of the contact film is determined numerically by calculating the average over normal vectors of each of its facets.

### 7.4 Calculation of the confinement pressure
The confinement pressure $\Pi$ is given by the trace of the particle stress tensor $\sigma$:

$$
\Pi = -\frac{1}{3}\sum_{k} \sigma_{kk} \tag{15}
$$

This tensor is deduced from the contact forces using the Irvin-Kirkwood relation eqn (9).

The dimensionless pressures obtained in our simulations are given in Table 2. The confinement pressure obtained for fcc structures is close to the results reported in the literature.¹⁷ Introducing a polydispersity of 2% and applying a uniaxial isochoric strain of 10% induces a slight increase of this pressure. A detailed study of this increase is beyond the scope of the present work.

### 7.5 Onset of many-body effects near the jamming transition
As discussed in Section 5.2, the mechanical coupling between the different contacts of a given bubble becomes negligible in the limit $\delta\phi \to 0$, and in this range, we have derived the non-standard two-body interaction model eqn (11) from eqn (6). Eqn (11) is qualitatively different from eqn (1), since it contains a logarithmic dependency on $f$, and it does not involve any free parameters. We divide the predictions of the non-standard two-body approximation eqn (6) by the prediction of the many-body law eqn (11) and plot this ratio versus $\delta\phi$, on Fig. 17 for the shear modulus $G$ and on Fig. 16 for the uniaxial modulus $E$. For both shear and uniaxial strain, we observe for all packing structures a slow convergence of this ratio to one as $\phi \to \phi_c$. This means that many-body effects become negligible in this limit. The weakness of this convergence is indeed expected, since the first term in eqn (6) dominates over the second one only by a factor $\ln(f)$. We note that beyond excess packing fractions $\delta\phi$ of the order of 0.01, the many-body contribution rapidly increases.

Table 2 For the indicated packing fractions, the dimensionless confinement pressure is specified for all of the types of samples studied in Fig. 2 and 3: ordered fcc packings ($\Pi_{\text{fcc}}$), disordered packings with 2% polydispersity and a coordination number of 12 ($\Pi_{\text{dis}}$), as well as this latter kind of samples to which a uniaxial isochoric strain of 10% has been applied ($\Pi_{\text{str}}$)

| Packing fraction | $\Pi_{\text{fcc}}$ | $\Pi_{\text{dis}}$ | $\Pi_{\text{str}}$ |
|------------------|--------------------|--------------------|--------------------|
| 0.79             | 0.07               | 0.08               |                    |
| 0.81             | 0.13               | 0.14               | 0.15               |
| 0.83             | 0.20               | 0.20               |                    |
| 0.85             | 0.28               | 0.29               | 0.3                |

![](./images/811079001299746816_17.jpg)

Fig. 16 Ratio of the linear uniaxial moduli $E$ of simple cubic (sc) or face centered cubic (fcc) bubble or droplet packings, predicted either by the full many-body model eqn (6) or by eqn (11). This latter equation is derived from eqn (6) assuming that interactions between contacts of a given bubble are negligible, as expected in the limit $\delta\phi \to 0$. A ratio of 1 indicates that this is true. The ratio is plotted versus the excess packing fraction $\delta\phi = \phi - \phi_c$.

![](./images/811079001299746816_18.jpg)

Fig. 17 Ratio of the linear shear moduli $G$ of body centered cubic (bcc) or face centered cubic (fcc) bubble or droplet packings, predicted either by the full many-body model eqn (6) or by eqn (11). This latter equation is derived from eqn (6) assuming that interactions between contacts of a given bubble are negligible, as expected in the limit $\delta\phi \to 0$. A ratio of 1 indicates that this is true. The ratio is plotted versus the excess packing fraction $\delta\phi = \phi - \phi_c$.

## Acknowledgements
We thank Christiane Caroli, Douglas Durian, Eric Weeks and Denis Weaire for stimulating discussions. This work was

supported by the European Space Agency (contract MAP AO 99-108) and the French Space Agency (agreement CNES/CNRS no. 130615 and no. 140569).

## References

1 J. W. Merrill, S. K. Sainis and E. R. Dufresne, *Phys. Rev. Lett.*, 2009, **103**, 138301.

2 N. Osterman, I. Poberaj, J. Dobnikar, D. Frenkel, P. Ziherl and D. Babić, *Phys. Rev. Lett.*, 2009, **103**, 228301.

3 A. J. Liu and S. R. Nagel, in *Annual Review of Condensed Matter Physics*, ed. J. S. Langer, Annual Reviews, 2010, vol. 1, pp. 347–369.

4 M. Van Hecke, *J. Phys.: Condens. Matter*, 2010, **22**, 033101.

5 F. Scheffold, F. Cardinaux and T. G. Mason, *J. Phys.: Condens. Matter*, 2013, **25**, 502101.

6 T. Mason, J. Bibette and D. Weitz, *J. Colloid Interface Sci.*, 1996, **179**, 439–448.

7 S. Cohen-Adddad, R. Höhler and O. Pitois, *Annu. Rev. Fluid Mech.*, 2013, **45**, 241–267.

8 J. Lin, E. Lerner, A. Rosso and M. Wyart, *Proc. Natl. Acad. Sci. U. S. A.*, 2014, **111**, 14382–14387.

9 N. D. Denkov, S. Tcholakova, K. Golemanov, K. P. Ananthapadmanabhan and A. Lips, *Phys. Rev. Lett.*, 2008, **100**, 138301.

10 J. R. Seth, L. Mohan, C. Locatelli Champagne, M. Cloitre and R. T. Bonnecaze, *Nat. Mater.*, 2011, **10**, 838–843.

11 D. J. Durian, *Phys. Rev. Lett.*, 1995, **75**, 4780–4783.

12 P. Olsson and S. Teitel, *Phys. Rev. Lett.*, 2007, **99**, 178001.

13 B. P. Tighe, *Phys. Rev. Lett.*, 2011, **107**, 158303.

14 C. Goodrich, A. J. Liu and S. R. Nagel, *Nat. Phys.*, 2014, **10**, 578–581.

15 D. C. Morse and T. A. Witten, *Europhys. Lett.*, 1993, **22**, 549–555.

16 S. Cohen-Adddad and R. Höhler, *Curr. Opin. Colloid Interface Sci.*, 2014, **19**, 536–548.

17 K. W. Desmond, P. J. Young, D. Chen and E. R. Weeks, *Soft Matter*, 2013, **9**, 3424–3436.

18 T. G. Mason, M.-D. Lacasse, G. Grest, D. Levine, J. Bibette and D. A. Weitz, *Phys. Rev. E: Stat. Phys., Plasmas, Fluids, Relat. Interdiscip. Top.*, 1997, **56**, 3150–3166.

19 R. Höhler, Y. Y. C. Sang, E. Lorenceau and S. Cohen-Adddad, *Langmuir*, 2008, **24**, 418–425.

20 A. Maestro, W. Drenckhan, E. Rio and R. Höhler, *Soft Matter*, 2013, **9**, 2531–2540.

21 I. Jorjadze, L. Pontani and J. Brujic, *Phys. Rev. Lett.*, 2013, **110**, 048302.

22 M.-D. Lacasse, G. S. Grest and D. Levine, *Phys. Rev. E: Stat. Phys., Plasmas, Fluids, Relat. Interdiscip. Top.*, 1996, **54**, 5436–5446.

23 K. Brakke, *Exp. Math.*, 1992, **1**, 141.

24 D. M. A. Buzza and M. E. Cates, *Langmuir*, 1994, **10**, 4503–4508.

25 A. Mal and S. Singh, *Deformation of Elastic Solids*, Prentice Hall, 1991.

26 S. Hutzler, R. Murtagh, D. Whyte, S. Tobin and D. Weaire, *Soft Matter*, 2014, **10**, 7103–7108.

27 C. Zhao, K. Tian and N. Xu, *Phys. Rev. Lett.*, 2011, **106**, 125503.

28 A. Siber and P. Ziherl, *Phys. Rev. Lett.*, 2013, **110**, 214301.

29 M. E. Evans, A. M. Kraynik, D. A. Reinelt, K. Mecke and G. E. Schröder-Turk, *Phys. Rev. Lett.*, 2013, **111**, 138301.

30 S. Alexander, *Phys. Rep.*, 1998, **296**, 65–236.