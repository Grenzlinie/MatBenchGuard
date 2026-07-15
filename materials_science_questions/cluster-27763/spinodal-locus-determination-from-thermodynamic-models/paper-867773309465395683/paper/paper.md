
# Effect of shape biaxiality on the phase behavior of colloidal liquid-crystal monolayers

Miguel González-Pinto \( ^{*} \) 

Departamento de Física Teórica de la Materia Condensada,

Facultad de Ciencias, Universidad Autónoma de Madrid, E-28049 Madrid, Spain

Yuri Martínez-Ratón \( ^{\dagger} \) 

Grupo Interdisciplinar de Sistemas Complejos (GISC), Departamento de Matemáticas,

Escuela Politécnica Superior, Universidad Carlos III de Madrid,

Avenida de la Universidad 30, E-28911, Leganés, Madrid, Spain

Enrique Velasco \( ^{\dagger} \) 

Departamento de Física Teórica de la Materia Condensada,

Instituto de Ciencia de Materiales Nicolás Cabrera and Condensed

Matter Physics Center (IFIMAC), Facultad de Ciencias,

Universidad Autónoma de Madrid, E-28049 Madrid, Spain

Szabolcs Varga \( ^{§} \) 

Institute of Physics and Mechatronics, University of Pannonia,

PO Box 158, Veszprém, H-8201 Hungary

(Dated: September 11, 2021)
 

## Abstract

We extend our previous work on monolayers of uniaxial particles [J. Chem. Phys. 140, 204906 (2014)] to study the effect of particle biaxiality on the phase behavior of liquid-crystal monolayers. Particles are modelled as board-like hard bodies with three different edge lengths  \( \sigma_{1} \geq \sigma_{2} \geq \sigma_{\mathrm{3}} \) , and use is made of the restricted-orientation approximation (Zwanzig model). A density-functional formalism based on the fundamental-measure theory is used to calculate phase diagrams for a wide range of values of the largest aspect ratio ( \( \kappa_{1} = \sigma_{1}/\sigma_{3} \in [1, 100] \) ). We find that particle biaxiality in general destabilizes the biaxial nematic phase already present in monolayers of uniaxial particles. While plate-like particles exhibit strong biaxial ordering, rod-like ones with  \( \kappa_{1} > 21.34 \)  exhibit reentrant uniaxial and biaxial phases. As particle geometry is changed from uniaxial- to increasingly biaxial-rod-like, the region of biaxiality is reduced, eventually ending in a critical-end point. For  \( \kappa_{1} > 60 \) , a density gap opens up in which the biaxial nematic phase is stable for any particle biaxiality. Regions of the phase diagram where packing-fraction inversion occurs (i.e. packing fraction is a decreasing function of density) are found. Our results are compared with the recent experimental studies on nematic phases of magnetic nanorods.

PACS numbers: 61.30.Pq,64.70.M-,47.57.J-
 

## I. INTRODUCTION

Biaxial hard-particle systems have received considerable theoretical and experimental attention since their first theoretical prediction by Freiser [1]. The characteristic feature of the biaxial phase is that two directions of orientational ordering occur associated with two molecular symmetry axes [2]. The importance of studying biaxial nematic phases is that they might be used in practical applications, such as fast electro-optical devices [3].

The theoretical exploration of stable biaxial nematic order has been based on biaxial hard-body and Gay-Berne-type soft potential models, using specific particle shapes such as spheroplatelets  \( [4, 5] \) , biaxial ellipsoids  \( [6, 7] \)  and bent-core particles  \( [8–11] \) . The biaxial nematic phase has also been found in binary mixtures of uniaxial plate-like and rod-like particles  \( [12–17] \) . However, the experimental realization of this exotic phase has proved to be rather complicated. The first observation dates back to the study of Yu and Saupe  \( [18] \) , who observed that a mixture of potassium laurate, 1-decanol, and water exhibited a region of biaxial order between two uniaxial phases. Later, biaxial nematic order was observed in low molecular weight thermotropic liquid crystals where the constituting particles had biaxial symmetry  \( [19, 20] \) . Regarding the shape of the constituting particles, banana-shaped mesogenic molecules are found to form thermotropic biaxial nematic phase  \( [21, 22] \) , while board-shaped colloidal particles have been used successfully in the stabilization of lyotropic biaxial nematic phases  \( [23–25] \) .

The recent experimental observation of biaxial nematic order in suspensions of board-like goethite nanorods  \( [23–25] \)  has prompted several theoretical studies in order to determine the global phase behavior of hard board-shaped particles  \( [5, 26] \)  and also to identify those processes which promote the formation of the biaxial nematic phase  \( [27, 28] \) . Interestingly, an increasing polydispersity in shape and size favors the biaxial nematic phase over other ordered phases  \( [27] \) . In addition to this, binary mixtures consisting of board-shaped particles with added polymers can stabilize biaxial order very efficiently  \( [28] \) . Even the biaxiality of the nematic phase can be tuned by applying an external magnetic field  \( [29] \) .

By inserting goethite nanorods into a soft lamellar matrix of non-ionic surfactant, it is also possible to examine the effect of dimensional reduction on the stability of mesophases  \( [30–32] \) . The confined nanorods between the bilayers of a lamellar phase have been shown to undergo a first-order in-plane (two-dimensional) isotropic-nematic phase transition, where
 

the isotropic and nematic phases correspond to planar and biaxial nematic phases, respectively. In the light of increasing amount of knowledge about the ordering properties of board-shaped goethite nanorods in confined geometries, it is worth studying the phase behaviour of hard board-shaped particles in quasi-two-dimensions using theoretical methods, and this is the motivation of our work.

In the present study we use density-functional theory in the fundamental-measure version to examine the orientational and positional ordering properties of confined hard-board colloidal particles with discrete orientations. The confinement is such that the centers of the board particles are always on a flat surface. We mainly focus on the effect of shape biaxiality on the stability of the biaxial nematic phase, but we also determine the stability regions of other mesophases such as the uniaxial nematic and positionally-ordered smectic, columnar and solid phases using bifurcation analysis. An important result is that an increasing biaxiality does not promote the formation of biaxial nematic phases due to the free-volume maximizing effect of the packing entropy.

The paper is organized as follows. The particle model and expressions for the relevant order parameters measuring biaxial ordering are presented in Sec. II. Sec. III presents the results, which include the evolution of the phase diagrams with particle biaxiality and the density dependence of the order parameters for different particle shapes. Some conclusions are drawn in Sec. IV. Details on the density-functional theory and bifurcation analysis are presented in the Appendices.

## II. MODEL AND THEORY

Colloidal particles are modelled as biaxial hard boards with edge-lengths  \( \sigma_{1} \geq \sigma_{2} \geq \sigma \)  and centres of mass located on a flat surface perpendicular to the z axis. Particles are allowed to rotate (within the restricted-orientation approximation) in the full 3D solid angle, but constrained to move on a plane. By restricting the possible orientations to be the three Cartesian axes, and considering the symmetries of the particles, six possible orientations, depicted in Fig. 1, are possible. The system can then be mapped onto a six-component mixture, with species labelled by  \( \mu\nu \)  (with  \( \mu, \nu = x, y, z \)  and  \( \mu \neq \nu \) ), where the indexes refer to the orientation of the longest and intermediate particle lengths, respectively. The density of ‘species’  \( \mu\nu \)  is written as  \( \rho_{\mu\nu} = \rho\gamma_{\mu\nu} \) , with  \( \rho \)  the 2D total density.  \( \{\gamma_{\mu\nu}\} \)  is a set of molar
 
![](./images/867773309465395683_1.jpg)

FIG. 1: Six Zwanzig species  \( \mu\nu \)  (with  \( \mu,\nu=x,y,z \)  and  \( \mu\neq\nu \) ) of hard board-like particles of dimensions  \( \sigma_{1}\geq\sigma_{2}\geq\sigma_{3} \) .

fractions that fulfills the constraint  \( \sum_{\mu,\nu}\gamma_{\mu\nu}=1 \) . The particular cases of prolate ( \( \sigma_{1}=L \)  and  \( \sigma_{2}=\sigma_{3}=\sigma \) ) and oblate ( \( \sigma_{1}=\sigma_{2}=\sigma \)  and  \( \sigma_{3}=L \) ) particles are sketched in Figs. 2(a) and (b), respectively.

To characterise particle shape, two aspect ratios are defined,  \( \kappa_{1} = \sigma_{1}/\sigma_{3} \)  and  \( \kappa_{2} = \sigma_{2}/\sigma_{3} \) , which fulfill the inequalities  \( 1 \leq \kappa_{2} \leq \kappa_{1} \) . Further, the degree of particle biaxiality will be characterised by the parameter

 \[ \theta\equiv(\kappa_{1}-1)^{-1}\left(\frac{\kappa_{1}}{\kappa_{2}}-\kappa_{2}\right). \quad (1) \] 

For fixed  \( \kappa_{1} \) , the  \( \theta \)  parameter varies from -1 (when  \( \kappa_{2} = \kappa_{1} \) , corresponding to uniaxial plate-like geometry) to  \( \theta = 1 \)  (when  \( \kappa_{2} = 1 \) , pertaining to uniaxial rod-like geometry). The value  \( \theta = 0 \)  corresponds to perfect biaxiality, i.e.  \( \kappa_{2} = \sqrt{\kappa_{1}} \) ; when  \( \kappa_{2} \gtrsim \sqrt{\kappa_{1}} \)  particles are considered to be oblate or prolate, respectively.

The statistical mechanics of the monolayer is dealt with using a version of density-functional theory. This version is based on the fundamental-measure theory for hard cubes [33]. The resulting free-energy functional is expressed as a function of the set of molar fractions  \( \{\gamma_{\mu\nu}\} \) , and the equilibrium state of the monolayer is obtained by minimising the free energy with respect to this set with the constraint  \( \sum_{\mu,\nu}\gamma_{\mu\nu}=1 \)  and for fixed scaled
 
![](./images/867773309465395683_2.jpg)

FIG. 2: Projection of orientation-restricted uniaxial hard boards on the monolayer. (a) Uniaxial prolate particles  \( (\sigma_{1}=L \)  and  \( \sigma_{2}=\sigma_{3}=\sigma) \) . (b) Uniaxial oblate particles  \( (\sigma_{1}=\sigma_{2}=\sigma,\sigma_{3}=L) \) . The projected areas are conveniently shaded.

density  \( \rho^{*} = \rho\sigma_{3}^{2} \) , where  \( \rho = N/A \)  is the two-dimensional density (N is number of particles and A the area of monolayer). The chemical potentials  \( \mu_{\tau\nu} \)  of all species and the lateral pressure p of the monolayer can then be calculated, and phase equilibria can be obtained. Details on the density functional used are given in Appendix A. The stability analysis and bifurcation theory derived to obtain the biaxial nematic spinodal and the nematic stability against non-uniform fluctuations can be found in Appendices B and C.

A useful measure of the ordering properties of the equilibrium phases are the order parameters, which help identify the two possible nematic phases in our system: the uniaxial nematic phase,  \( N_{u} \) , and the biaxial nematic phase,  \( N_{b} \) . In the case of biaxial particles two order parameter tensors can be defined,

 \[ \hat{Q}_{\alpha\beta}=\frac{1}{2}\left(3\langle u_{\alpha}u_{\beta}\rangle-\delta_{\alpha\beta}\right),\quad\hat{B}_{\alpha\beta}=\frac{1}{2}\left(\langle n_{\alpha}n_{\beta}\rangle-\langle m_{\alpha}m_{\beta}\rangle\right), \quad (2) \] 

where  \( u_{\alpha} \) ,  \( n_{\alpha} \)  and  \( m_{\alpha} \)  are the  \( \alpha \) -components of the unit vectors u, n and m along the longest, intermediate and smallest particle lengths. Averages are taken over the orientational distribution function, given by the set  \( \{\gamma_{\mu\nu}\} \) . For our restricted-orientation approximation,
 

it can easily be shown that the tensors are diagonal:

 \[ \hat{Q}=\left(\begin{array}{c c c}{-\frac{Q-\Delta_{Q}}{2}}&{0}&{0}\\ {0}&{-\frac{Q+\Delta_{Q}}{2}}&{0}\\ {0}&{0}&{Q}\\ \end{array}\right),\quad\hat{B}=\left(\begin{array}{c c c}{-\frac{B-\Delta_{B}}{2}}&{0}&{0}\\ {0}&{-\frac{B+\Delta_{B}}{2}}&{0}\\ {0}&{0}&{B}\\ \end{array}\right) \quad (3) \] 

where Q and B are uniaxial nematic order parameters,

 \[ Q\equiv Q_{z z}=\frac{1}{2}\left(3\sum_{\nu\neq z}\gamma_{z\nu}-1\right),\quad B\equiv B_{z z}=\frac{1}{2}\left(\sum_{\mu\neq z}\gamma_{\mu z}-\sum_{\mu,\nu\neq z}\gamma_{\nu\mu}\right), \quad (4) \] 

with Q the usual uniaxial order parameter (note that  \( B \neq 0 \)  for both  \( N_{u} \)  and  \( N_{b} \)  phases), while

 \[ \Delta_{Q}\equiv Q_{x x}-Q_{y y}=\frac{3}{2}\left(\sum_{\nu\neq x}\gamma_{x\nu}-\sum_{\nu\neq y}\gamma_{y\nu}\right), \quad (5) \] 

 \[ \Delta_{B}\equiv B_{x x}-B_{y y}=\frac{1}{2}\left[\sum_{\mu\neq x}\gamma_{\mu x}-\sum_{\mu\neq y}\gamma_{\mu y}+\sum_{\mu,\nu\neq y}\gamma_{\nu\mu}-\sum_{\mu,\nu\not=x}\gamma_{\mu\nu}\right], \quad (6) \] 

are biaxial nematic order parameters, both different from zero only for the  \( N_{b} \)  phase.

A comment on the definition of the above order parameters in relation with the particle geometry is in order. For uniaxial rods  \( (\theta = 1) \) , the vector u points along the main symmetry axis (longest particle length), the other two being equivalent. Thus, the above definitions for  \( \{Q, B, \Delta_{Q}, \Delta_{B}\} \)  are correct in the limit  \( \theta \to 1 \) , and they will be used for any  \( \theta > 0 \) . However, for uniaxial oblate particles  \( (\theta = -1) \) , the main particle axis should be taken to lie along the shortest particle length m, the other two being equivalent: u and m should be interchanged for  \( \theta < 0 \) , and all four order parameter can be obtained from the same formulas as before but replacing  \( \gamma_{\mu\nu} \)  by  \( \gamma_{\tau\nu} \)  (with  \( \tau \neq \mu \) ). In this way we obtain, for example, that  \( Q \to -\frac{1}{2} \)  for perfect planar nematic ordering, as it should be.

In the following, the parameter  \( \Delta_{Q}^{*}\equiv2\Delta_{Q}/3 \)  will be used to measure the degree of biaxiality for uniaxial plate-like and rod-like particles  \( (\theta=\pm1) \) , while in the case of biaxial particles  \( (-1<\theta<1) \)  the parameter  \( \Delta_{B} \)  will be used. It can be shown that, for perfect biaxial order,  \( |\Delta_{B}|\to1 \)  and 0.5 for rods and plates, respectively, while  \( |\Delta_{Q}^{*}|\to1 \)  for both particles. In any case, we always plot absolute values of biaxial order parameters in the figures.

Finally, a useful measure of packing in the monolayer is  \( \eta \) , the area fraction covered by particles on the monolayer (packing fraction). It can be shown that  \( \eta \)  is related to  \( \rho^{*} \) , Q
 

and B by

 \[ \eta=\frac{\rho^{*}}{3}\left\{\kappa_{1}(\kappa_{2}+1)+\kappa_{2}-[\kappa_{1}(\kappa{}_{2}+1)-2\kappa_{2}]Q-3\kappa_{1}(\kappa_{2}-1)B\right\}. \quad (7) \] 

This equation is used later to explain packing-fraction inversion effects that take place for some particle symmetries.

## III. RESULTS

## A. Effect of particle biaxiality on biaxial phase

First we chose a pair of values for the largest aspect ratio,  \( \kappa_{1}=5 \)  and 10, and varied particle biaxiality  \( \theta \)  from -1 (plate-like uniaxial symmetry) to 1 (rod-like uniaxial symmetry). For each value of  \( \kappa_{1} \)  and  \( \theta \) , bifurcation analysis provides the values of scaled density  \( \rho^{*} \)  and molar fractions  \( \{\gamma_{zx}=\gamma_{zy}\neq\gamma_{xz}=\gamma_{yz}\neq\gamma_{xy}\} \)  corresponding to the  \( N_{u}\rightarrow N_{b} \)  bifurcation point. The nature (continuous vs. first order) of the transition was always checked via direct minimization of the free-energy density with respect to all the molar fractions  \( \{\gamma_{\mu\nu}\} \) , which confirmed the continuous character of the transition from  \( |\gamma_{zx}-\gamma_{zy}|\sim(\rho^{*}-\rho_{0}^{*})^{1/2} \)  (with  \( \rho_{0}^{*} \)  the scaled density at bifurcation) near and above the bifurcation point.

The spinodal instabilities of uniform nematic phases  \( N_{u} \) ,  \( N_{b} \)  with respect to density modulations of crystal (K), columnar (C) or smectic (S) symmetries were also obtained from the appropriate bifurcation theory (appendix C). The results are plotted in Fig. 3(a) for  \( \kappa_{1}=5 \)  and (b) for  \( \κ_{1}=10 \) . In the first case there exists a small region (shaded in the figure), close to  \( \theta=-1 \) , in which  \( N_{b} \)  is stable. The  \( N_{u}-N_{b} \)  bifurcation line crosses the curve associated with the spinodal instability to the non-uniform phases at  \( \theta\simeq-0.5 \) . The figure also shows the lack of biaxial ordering in rod-like ( \( \theta>0 \) ) particles, since the  \( N_{b} \)  bifurcation point occurs at densities higher than that of the C-S-K spinodal. For  \( \kappa_{1}=10 \)  the region of stability of  \( N_{b} \)  is considerably enlarged (spanning the interval  \( \theta\lesssim0 \) ); this is because the aspect ratio of the projected rectangles with the smallest area is larger. Again rod-like particles ( \( \theta>0 \) ) do not exhibit biaxial ordering.

To show the ordering properties of the system in more detail, Figs. 3(c) and (d) contain the behavior of the uniaxial and biaxial order parameters Q,  \( \Delta_{Q}^{*} \)  and  \( \Delta_{B} \) , as a function of  \( \rho^{*} \)  for uniaxial ( \( \theta = \pm1 \) ) and biaxial ( \( \theta \approx \pm0.5 \) ) symmetries, respectively, and for  \( \kappa_{1} = 10 \) . As already reported in a previous publication [34], uniaxial plates continuously become ordered
 
![](./images/867773309465395683_3.jpg)

![](./images/867773309465395683_4.jpg)

![](./images/867773309465395683_5.jpg)

![](./images/867773309465395683_6.jpg)

FIG. 3: (a) Phase diagrams in the plane scaled density  \( \rho^{*} \)  vs. particle biaxiality parameter  \( \theta \)  for  \( \kappa_{1}=5 \) . Density axis is in logarithmic scale. Solid curve: continuous  \( N_{u}-N_{b} \)  transition. Dashed curve: spinodal instability from the uniform to the non-uniform phases (either K, C or S). Region of  \( N_{b} \)  stability is shaded. (b) Same as (a), but for  \( \kappa_{1}=10 \) . (c) Uniaxial Q (solid curve) and biaxial  \( \Delta_{Q}^{*} \)  (dashed curve) order parameters as a function of scaled density  \( \rho^{*} \)  for uniaxial plate-like ( \( \theta=-1 \) ) and rod-like ( \( \theta=1 \) ) particles with  \( \kappa_{1}=10 \) . Density axis is in logarithmic scale. Filled circles on the curves indicate the instabilities to non-uniform phases. (d) Same as (c), but for plate-like ( \( \theta=-0.5 \) , dashed curve) and rod-like ( \( \theta=0.5 \) , dotted curve) biaxial particles.

with density, their main axes lying preferentially on the surface of the monolayer [see case  \( \theta = -1 \)  in Fig. 3(c)]. As density increases from zero, the uniaxial order parameter Q decreases continuously from zero and saturates at -0.5 for high densities, which means that the shortest particle axes lie on the monolayer. In this configuration the total particle area projected on the surface is minimized (with a vanishingly small fraction of plates with main axes perpendicular to the monolayer). When Q is almost saturated ( \( \rho^{*} \simeq 0.02 \) ), the in-plane
 

rotational symmetry of particle axes is broken and the system exhibits a  \( N_{u} \rightarrow N_{b} \)  transition.

For rod-like particles, case  \( \theta = 1 \)  in Fig. 3(c), the following behavior is observed: the uniaxial order parameter Q continuously increases from zero at vanishingly small densities, saturating to 1 as density increases. There are two clear differences with respect to the plate-like geometry: (i) axes of uniaxial particles are now preferentially oriented perpendicular to the monolayer (thus decreasing the total occupied area), and (ii) there is no orientational symmetry breaking: we can discard the presence of a  \( N_{b} \)  phase for rods with  \( \kappa_{1} = 10 \) .

The uniaxial and biaxial order parameters are also shown as a function of  \( \rho^{*} \)  for  \( \kappa = 10 \)  in the case of biaxial particles with  \( \theta = \pm0.5 \)  [see Fig. 3 (d)]. Here the situation is similar to the uniaxial case: (i) plate-like particles ( \( \theta = -0.5 \) ) exhibit  \( N_{u} \)  planar ordering and a  \( N_{u}-N_{b} \)  transition when Q is almost saturated. However, the  \( N_{b} \)  phase loses its stability against non-uniform phases at higher densities. (ii) Rod-like particles ( \( \theta = 0.5 \) ) possess uniaxial out-of-plane ordering and a direct transition from the  \( N_{u} \)  phase to the non-uniform phases (K, C or S). Note that  \( N_{b} \)  is metastable with respect to these phases.

From these results we can conclude that, contrary to intuition, the main effect of particle biaxiality in plate or rod monolayers is the destabilization of the  \( N_{b} \)  phase: note in Figs. 3(a) and (b) how the shaded region of  \( N_{b} \)  stability, bounded by the two spinodal curves, shrinks as  \( \theta \)  increases from the uniaxial case  \( \theta = -1 \) . There is a clear physical interpretation of this behavior. For uniaxial plates, with dimensions  \( \sigma \times \sigma \times L \)  ( \( L < \sigma \) ), there are two identical rectangular and mutually perpendicular projections of dimensions  \( L \times \sigma \) , which have different molar fractions for a given density, and consequently a  \( N_{b} \)  appears. The other (large) projection, of dimensions  \( \sigma \times \sigma \) , has a vanishingly small molar fraction. When particle biaxiality increases keeping fixed the largest aspect ratio ( \( \kappa_{1} = \sigma_{1}/\sigma_{3} = 10 \) ; without loss of generality we suppose  \( \sigma_{3} \)  to be constant), decreasing  \( \sigma_{2} \)  from  \( \sigma_{1} \) , the original projected rectangular species of equal areas becomes now different, with dimensions  \( \sigma_{1} \times \sigma_{3} \)  (intermediate species) and  \( \sigma_{2} \times \sigma_{3} \)  (smallest species). Note that biggest species, that with dimensions  \( \sigma_{1} \times \sigma_{2} \) , will continue to have a vanishingly small molar fraction. To minimize the excluded volume interactions between particles, the fraction of  \( \sigma_{2} \times \sigma_{3} \)  species should increase with respect to the other, and the total density has to increase to stabilize the  \( N_{b} \)  phase (we remind that a larger aspect ratio favours the  \( N_{u}-N_{b} \)  symmetry breaking).

It is fruitful to compare (at least qualitatively) our results with those of the recent experiment of goethite nanorods confined between the bilayers of a lamellar phase made from
 
![](./images/867773309465395683_7.jpg)

![](./images/867773309465395683_8.jpg)

![](./images/867773309465395683_9.jpg)

![](./images/867773309465395683_10.jpg)

![](./images/867773309465395683_11.jpg)

![](./images/867773309465395683_12.jpg)

FIG. 4: Phase diagrams in the  \( \rho^{*}-\theta\left[(a),(b),(c)\right] \)  and  \( \eta-\theta\left[(d),(e),(f)\right] \)  planes for  \( \kappa_{1}=20\left[(a)\right. \)  and  \( (d)] \) , 55  \( [(b) \)  and  \( (e)] \)  and 70  \( [(c) \)  and  \( (f)] \) . The regions of stability of different phases are correspondingly labelled. Regions of stability of the  \( N_{b} \)  phase are shaded. Curves have the same meanings as in Fig. 3 (a) and (b). Open circles over the curves represent the positions of critical end-points.

nonionic surfactant [30–32]. These particles orient perpendicular to an applied magnetic field along the lamellae axis so that negative uniaxial order parameters can be obtained, resulting in stacked sheets of liquid-like quasi-two-dimensional rods. Particle sizes were estimated by optical and X-ray diffraction methods to be  \( 315 \times 38 \times 18 \, nm^3 \)  resulting, in our notation, in aspect ratios  \( \kappa_1 = 17.5 \)  and  \( \kappa_2 = 2.1 \) , and  \( \theta = 0.37 \)  (i.e. relatively biaxial particle sizes). Rod interactions are approximately hard, but interact with the lamellae in complex ways, probably resulting in effective attractions between the rods in a sheet; intersheet interactions also exist, although they are probably weak. The authors find an ‘isotropic’ phase (corresponding to the uniaxial nematic phase  \( N_u \)  in our monolayer) and a ‘nematic’ phase (our biaxial  \( N_b \)  phase) and suggest a possible continuous phase transition between the two at a packing fraction which was not possible to estimate in the experiment. This particle geometry would correspond closely to the phase diagram of Figs. 4(a) and (d). In our diagram, the experimental value of  \( \theta \)  is slightly larger than the predicted limiting point for the biaxial phase. A number of factors could explain the difference: modified attractive interactions and size polydispersity in the experimental nanorod system, both of which could enhance
 

the stability of the biaxial phase, and/or defects in the theoretical approach.

## B. Topology of phase diagram

In this section the topology of the phase diagram as a function of  \( \kappa_{1} \)  is analysed. Figs. 4 show phase diagrams in the  \( \rho^{*}-\theta\left[\left(\mathrm{a}-\mathrm{c}\right)\right] \)  and  \( \eta-\theta\left[\left(\mathrm{d}-\mathrm{f}\right)\right] \)  planes for  \( \kappa_{1}=20 \) , 55 and 70. For  \( \kappa_{1}=20\left[\left(\mathrm{a}\right)\right. \)  and  \( \left.\left(\mathrm{d}\right)\right] \)  the phase diagrams retain the same topology as for the case  \( \kappa_{1}=10 \) , see Fig. 3(b).

As shown in our recent work [34], a monolayer of uniaxial rods in the restricted-orientation approximation exhibits a peculiar phase behaviour for  \( \kappa_{1}=21.34 \) , with a reentrant  \( N_{u} \)  phase and an intermediate  \( N_{b} \)  phase. This behaviour persists in the case of biaxial rods. For example, Figs. 4(b) and (e) pertain to the case  \( \kappa_{1}=55 \) , and the aforementioned system would be similar to the case  \( \theta=1 \)  (uniaxial rods). The  \( N_{b} \)  stability region shrinks for increasing particle biaxiality (decreasing  \( \theta \) ), totally disappearing at a critical-end point (shown with open circle). The presence of a biaxial phase in monolayers of uniaxial rods is easy to explain: For high aspect ratios and densities such that the total packing fraction of the projected rectangular species  \( L\times\sigma \)  is close to  \( \eta_{2D} \)  (that of the I-N transition of hard rectangles in 2D), an orientational symmetry breaking at the surface of the monolayer takes places. Of course the presence of the square,  \( \sigma\times\sigma \) , species should be taken into account. However, at low densities and high aspect ratios, the packing fraction of squares is small compared to that of rectangles. When the total density is increased, the packing fraction of squares increases (as uniaxial nematic ordering is promoted), while the packing fraction of rectangles decreases. Then the packing fraction of rectangles jumps below  \( \eta_{2D} \) , and consequently the  \( N_{b} \)  phase looses its stability with respect to the  \( N_{u} \)  phase.

Now we discuss the stability region of the biaxial nematic phase on the prolate side. When particle biaxiality is increased ( \( \theta \)  decreases from 1), rectangular species becomes inequivalent and the largest one, of dimensions  \( \sigma_{1} \times \sigma_{2} \) , rapidly decreases in molar fraction with respect to the intermediate one, of dimensions  \( \sigma_{1} \times \sigma_{3} \) . Therefore the total density should increase so that the total area fraction of the projected rectangular becomes on the order of  \( \eta_{2D} \) , and the  \( N_{u}-N_{b} \)  transition density increases. On the other hand, the alignment of particles along z is enhanced with the increased biaxiality such that the packing fraction of the smallest species grows at the expense of the other two, and consequently the  \( N_{b}-N_{u} \)  transition curve moves
 
![](./images/867773309465395683_13.jpg)

![](./images/867773309465395683_14.jpg)

FIG. 5: (a) Detail of Fig. 4(b) in which a region of first-order  \( N_{u}-N_{b} \)  transitions (hatched area) is observed. (b)  \( \eta \)  vs.  \( \rho^{*} \)  for  \( \kappa_{1}=70 \)  and  \( \theta=0.04 \)  [see Fig. 4(c)] showing the packing fraction inversion. Vertical lines show the values of  \( \rho^{*} \)  corresponding to phase transitions between different phases.

to lower densities. For a particular value of particle biaxiality the two transition curves, for the  \( N_{u}-N_{b} \)  and  \( N_{b}-N_{u} \)  transitions, coalesce into a single critical end-point [see Fig. 4(b)].

It is interesting to note from Figs. 4(a–c) that the  \( N_{u}-N_{b} \)  spinodal in the region  \( \theta < 0 \)  deforms as  \( \kappa_{1} \)  increases and eventually develops a loop at  \( \theta \simeq 0 \)  [see Fig. 4(b) for  \( \kappa_{1} = 55 \) ]. This means that there is a small  \( \theta \) -interval (between the two critical end-points shown with open circles) where both nematic phases are reentrant. Also, there is a particular value of aspect ratio,  \( \kappa_{1}^{*} \simeq 60 \) , for which the two critical end-points in the plate-like ( \( \theta < 0 \) ) and rod-like ( \( \theta > 0 \) ), on the corresponding  \( N_{b} \)  spinodals, coalesce into a single point. For  \( \kappa_{1} > \kappa_{1}^{*} \)  a density gap appears in the phase diagram where the  \( N_{b} \)  is stable for any  \( \theta \) , as shown in Fig. 4(c) for  \( \kappa_{1} = 70 \) . Now both nematic phases are reentrant in wide intervals of  \( \theta \) .

We should mention that the nature of the  \( N_{u}-N_{b} \)  transition is always continuous, except for  \( \kappa_{1}>40 \)  in a very small range of particle biaxiality corresponding to the density loop mentioned above. This is shown in Fig. 5(a) where a detail of the phase diagram for  \( \kappa_{1}=55 \)  is shown. The hatched area represents the  \( N_{u}-N_{b} \)  coexistence region.

For high enough  \( \kappa_{1} \)  and particles with  \( \theta\simeq0 \)  the phase diagrams present an interesting feature, namely a packing-fraction inversion. This is shown in Fig. 4(e) and (f) for  \( \kappa_{1}=55 \)  and 70. In this region the lower  \( N_{u}\rightarrow N_{b} \)  and upper  \( N_{b}\rightarrow N_{u} \)  transition curves in the  \( \rho^{*}-\theta \)  plane change their relative locations when plotted in the  \( \eta-\theta \)  plane. This peculiar
 
![](./images/867773309465395683_15.jpg)

![](./images/867773309465395683_16.jpg)

FIG. 6: (a) Location of critical end-points in the  \( \kappa_{1}-\theta \)  plane. The curve separates regions where one or three phase transitions between uniform phases take place. (b) Biaxial order parameter  \( \Delta_{B} \)  vs.  \( \rho^{*} \)  for  \( \theta = -0.5 \)  (solid), 0 (dotted) and 0.5 (dashed) for  \( \kappa_{1} = 70 \) . Filled circles on the curves indicate the instabilities to non-uniform phases.

phenomenon can be clearly visualized in Fig. 5(b), where the packing fraction  \( \eta \)  is plotted against  \( \rho^{*} \) . As we can see, once the  \( N_{u}-N_{b} \)  transition takes place, the transition packing fraction exhibits a maximum and then decreases down to the value at the  \( N_{b}-N_{u} \)  transition. For larger  \( \rho^{*} \)  the packing fraction exhibits the usual monotonic behaviour. This effect can be explained by resorting to Eqn. (7), which shows that  \( \eta \)  is a function of  \( \rho^{*} \)  and the two order parameters Q and B. It is then possible for the packing fraction to decrease with  \( \rho^{*} \)  when the order parameters are positive and increase sufficiently strongly with  \( \rho^{*} \)  (i.e., uniaxial ordering is strongly promoted so that the number of particles of the species with the smallest projected area increases rapidly enough), in such a way that the total increase in the number of particles is compensated.

One interesting feature of the phase diagrams shown in Fig. 4 is that, for particular values of the parameters  \( (\kappa_{1},\theta) \) , the total number of transitions between uniform phases  \( (\mathrm{N}_{\mathrm{u}} \)  and  \( \mathrm{N}_{\mathrm{b}}) \)  can be one or three (the latter case associated with reentrant phases). The curve in the  \( \kappa_{1}-\theta \)  plane separating both regions is just the continuous boundary of critical end-points (see appendix B for details on their calculation), and is plotted in Fig. 6(a), where the regions corresponding to one or three phase transitions are correspondingly labelled.

To finish this section, we compare in Fig. 6(b) the biaxial orientational order, as measured by the biaxial order parameter  \( \Delta_{B} \) , of plate-like ( \( \theta = -0.5 \) , solid curve), perfectly biaxial
 

 \( (\theta = 0 \) , dotted curves) and rod-like  \( (\theta = 05 \) , dashed curve) particles, all of them having  \( \kappa_{1} = 70 \) . There are important differences between the three cases: while the biaxial order of plate-like particles increases from the bifurcation point and finally saturates at its maximum value, rod-like particles exhibit a rather small biaxial order in the range of densities where the  \( N_{b} \)  phase is stable. Finally, for  \( \theta = 0 \)  a small region of biaxial order (with relatively small order parameter) is followed by a second transition to a second  \( N_{b} \)  phase possessing a high degree of biaxiality up to the transition to a non-uniform phase. This trend is general for any  \( \kappa_{1} > 21.34 \) : The  \( N_{b} \)  phase of rod-like particles exhibits only a small degree of global biaxial ordering, quantified through the order parameter  \( \Delta_{B} \) . Therefore, its stability is questionable for the freely-rotating case.

## IV. CONCLUSIONS

In this work we studied the effect of particle biaxiality on the phase behaviour of liquid-crystal colloidal monolayers, using a fundamental-measure density-functional theory for hard board-like biaxial particles with restricted orientations. Various phase diagrams were obtained for different values of the two parameters that describe the particle shape: the largest particle aspect ratio  \( \kappa_{1} \)  and the particle biaxiality  \( \theta \) . This study is an extension of our previous work in which monolayers of uniaxial rod-like and plate-like particles were analysed [34]. Contrary to expected, particle biaxiality destabilizes the biaxial phase in the cases where the latter is present, a phenomenon directly related with the competition between (i) the biaxiality promoted by the two-dimensional spatial constraint on particle centres of mass, and (ii) the biaxial ordering promoted by particle biaxiality for high enough densities. For biaxial particles the rectangular projected areas are inequivalent, and the mixing entropy stabilizes, mainly for plate-like geometry, the 2D isotropic phase.

For rod-like geometry the  \( N_{b} \)  phase has a small degree of biaxial orderer and occurs in a narrow interval of densities. Again an increase in particle biaxiality reduces the stability interval which eventually disappears at a critical end point. For high enough values of the largest aspect ratio,  \( \kappa_{1} \simeq 60 \) , the phase diagram exhibits a density gap in which the  \( N_{b} \)  is stable for any value of particle biaxiality  \( \theta \) . The transitions between nematic phases are continuous, except for a small range of values of  \( \theta \)  about zero and for large values of  \( \kappa_{1} \) , where a first-order  \( N_{u}-N_{b} \)  transition appears. A packing fraction inversion phenomenon also
 

exists. The rapid increase of particle alignment along z, resulting in a large fraction of the projected species with the smallest area, compensates the total increment in number of particles, resulting in a decrease of  \( \eta \)  with  \( \rho^{*} \) .

The presence of a  \( N_{b} \)  phase in the rod-like region of the phase diagram ( \( \theta > 0 \) ) should be taken with care, as it could be a direct consequence of the restriction on particle orientations. As shown by Monte Carlo simulations and Parsons-Lee density-functional theory, uniaxial freely-rotating plate-like ellipsoidal particles adsorbed on a monolayer without orientational restrictions do exhibit a  \( N_{b} \)  phase, while their rod-like counterparts do not [35]. However it would be necessary to explore a larger variety of particle geometries, without imposing orientational constraints, to finally discard the presence of a biaxial nematic phase.

We hope that our study will serve as a guide for future experimental studies of confined board-shaped colloidal systems, such as goethite nanorods  \( [30–32] \)  and the recently synthesized lead carbonate nanoplatelets  \( [36] \) .

## Acknowledgments

We gratefully acknowledge illuminating discussions with G. Odriozola. Financial support from MINECO (Spain) under grants FIS2010-22047-C01 and FIS2010- 22047-C04 is acknowledged. SV acknowledges the financial support of the Hungarian State and the European Union under the TAMOP-4.2.2.A-11/1/KONV-2012-0071.

## Appendix A: Density-functional Theory

We use a density functional (DF) based on fundamental-measure theory for the Zwanzig model (particle orientations along the three Cartesian axes) which fulfills the 3D→2D dimensional crossover [33]. In this formalism the excess part of free-energy density depends on a set of weighted densities calculated by convoluting the density profiles of the two-dimensional projections of the six species with certain weighting functions, the latter depending on the
 

geometry of a single particle:

 \[ \begin{aligned}&n_{\alpha}(\boldsymbol{r})=\sum_{\mu\nu}\int d\boldsymbol{r}^{\prime}\rho_{\mu\nu}(\boldsymbol{r}^{\prime})\omega_{\mu\nu}^{(\alpha)}(\boldsymbol{r}-\boldsymbol{r}^{\prime}),\\&\omega_{\mu\nu}^{(0)}(\boldsymbol{r})=\frac{1}{4}\delta\left(\frac{\sigma_{\mu\nu}^{x}}{2}-|x|\right)\delta\left(\frac{\sigma_{\mu\nu}^{y}}{2}-|y|\right),\\&\omega_{\mu\nu}^{(1x)}(\boldsymbol{r})=\frac{1}{2}\Theta\left(\frac{\sigma_{\mu\nu}^{x}}{2}-|x|\right)\delta\left(\frac{\sigma_{\mu\nu}^{y}}{2}-|y|\right),\\&\omega_{\mu\nu}^{(1y)}(\boldsymbol{r})=\frac{1}{2}\delta\left(\frac{\sigma_{\mu\nu}^{x}}{2}-|x|\right)\Theta\left(\frac{\sigma_{\mu\nu}^{y}}{2}-|y|\right),\\&\omega_{\mu\nu}^{(2)}(\boldsymbol{r})=\Theta\left(\frac{\sigma_{\mu\nu}^{x}}{2}-|x|\right)\Theta\left(\frac{\sigma_{\mu\nu}^{y}}{2}-|y|\right),\\ \end{aligned} \quad (A1) \] 

where  \( \delta(x) \)  and  \( \Theta(x) \)  are the Dirac delta and Heaviside functions, respectively, while we have introduced the tensor  \( \sigma_{\mu\nu}^{\tau} = \sigma_{3} + (\sigma_{1} - \sigma_{3})\delta_{\tau\mu} + (\sigma_{2} - \sigma_{3})\delta_{\tau\nu} \)  (with  \( \tau = x, y \)  and  \( \delta_{\tau\mu} \)  the Kronecker delta). In the uniform limit we obtain  \( n_{\alpha} = \sum_{\mu\nu} \rho_{\mu\nu} \mathcal{M}_{\mu\nu}^{(\alpha)} \) , with  \( \mathcal{M}_{\mu\mu}^{(\alpha)} = \int d\boldsymbol{r} \omega_{\mu\nu}^{(\alpha)}(\boldsymbol{r}) \)  the fundamental measures of the 2D particle projections:

 \[ \mathcal{M}_{\mu\nu}^{(0)}=1,\quad\mathcal{M}_{\mu\nu}^{(1\tau)}=\sigma_{\mu\nu}^{\tau},\quad\mathcal{M}_{\mu\nu}^{(2)}=\sigma_{\mu\nu}^{x}\sigma_{\mu\nu}^{y}. \quad (A2) \] 

The excess part of the scaled free-energy density for a 2D mixture of six particle projections,

 \[ \Phi_{\mathrm{e x c}}^{*}\equiv\beta\mathcal{F}_{\mathrm{e x c}}\sigma_{3}^{2}/A=\sigma_{3}^{2}\left(-n_{0}\ln(1-n_{2})+\frac{n_{1x}n_{1y}}{1-n_{2}}\right), \quad (A3) \] 

(with  \( F_{exc} \)  the uniform limit of the excess part of the DF and A the total area) can be written as

 \[ \Phi_{\mathrm{e x c}}^{*}=\rho^{*}\left[-\ln(1-\eta)+y\Psi_{1x}\Psi_{1y}\right], \quad (A4) \] 

where the scaled density is defined as  \( \rho^{*} = \rho\sigma_{3}^{2} \)  and the packing fraction,  \( \eta = \rho^{*}\Psi_{2} \) , is the uniform limit of the weighted density  \( n_{2}(\boldsymbol{r}) \) . Also we have defined  \( y = \rho^{*}/(1 - \eta) \) , and the following functions

 \[ \Psi_{1x}=\left(\gamma_{xy}+\gamma_{xz}\right)\kappa_{1}+\left(\gamma_{yx}+\gamma_{zx}\right)\kappa_{2}+\gamma_{zy}+\gamma_{yz}, \quad (A5) \] 

 \[ \Psi_{1y}=\left(\gamma_{yx}+\gamma_{yz}\right)\kappa_{1}+\left(\gamma_{xy}+\gamma_{zy}\right)\kappa_{2}+\gamma_{zx}+\gamma_{xz}, \quad (A6) \] 

 \[ \Psi_{2}=\left(\gamma_{xy}+\gamma_{yx}\right)\kappa_{1}\kappa_{2}+\left(\gamma_{xz}+\gamma_{yz}\right)\kappa_{1}+\left(\gamma_{zx}+\gamma_{zy}\right)\kappa_{2}. \quad (A7) \] 

The ideal part of the free-energy density in reduced units is

 \[ \Phi_{\mathrm{i d}}^{*}\equiv\beta\mathcal{F}_{\mathrm{i d}}\sigma_{3}^{2}/A=\rho^{*}\left[\ln\rho^{*}-1+\sum_{\mu,\nu}\gamma_{\mu\nu}\ln\gamma_{\mu\nu}\right]. \quad (A8) \]
 

The minimization of the total free-energy density,  \( \Phi^{*} = \Phi_{id}^{*} + \Phi_{exc}^{*} \) , with respect to the molar fractions  \( \gamma_{\mu\nu} \) , together with the constraint  \( \sum_{\mu,\nu} \gamma_{\mu\nu} = 1 \) , provide the following set of equations that have to be solved to obtain their equilibrium values:

 \[ \begin{aligned}\gamma_{\mu\nu}&=\frac{e^{-\chi_{\mu\nu}}}{\sum_{\alpha\beta}e^{-\chi_{\alpha\beta}}},\\ \chi_{\mu\nu}&=y\left[\Psi_{1x}\kappa_{\mu\nu}^{y}+\Psi_{1y}\kappa_{\mu\nu}^{\alpha x}+(1+y\Psi_{1x}\Psi_{1y})\kappa_{\mu\nu}^{\alpha x}\kappa_{\mu\nu}^{y}\right],\end{aligned} \quad (A9) \quad (A10) \] 

where we have denoted  \( \kappa_{\mu\nu}^{\tau}=1+(\kappa_{1}-1)\delta_{\tau\mu}+(\kappa_{2}-1)\delta_{\nu\tau} \) 

The chemical potentials of the species  \( \tau\nu \)  evaluated at the equilibrium  \( \{\gamma_{\mu\nu}^{(\mathrm{eq})}\} \)  are

 \[ \beta\mu_{\tau\nu}=\beta\mu_{0}=\ln\left(\frac{y}{\sum_{\alpha\beta}e^{-\chi_{\alpha\beta}}}\right),\quad\forall\tau,\nu \quad (A11) \] 

Finally, the pressure in reduced units can be computed as

 \[ p^{*}\equiv\beta p\sigma_{3}^{2}=y+y^{2}\Psi_{1x}\Psi_{1y}. \quad (A12) \] 

Both quantities are required to calculate the coexistence densities in case of first-order phase transitions.

## Appendix B: Bifurcation to the biaxial phase

Here we perform a bifurcation analysis from the uniaxial nematic  \( \left(\mathrm{N}_{\mathrm{u}}\right) \)  to the biaxial nematic  \( \left(\mathrm{N}_{\mathrm{b}}\right) \)  phase. The latter phase has two nematic directors, perpendicular and parallel to the monolayer, respectively. By solving Eqs. (B12) and (B17) below we find the values of the scaled density  \( \rho^{*} \)  and two independent molar fractions at the bifurcation (spinodal). Note that in case of continuous  \( N_{u}-N_{b} \)  phase transitions, this formalism provides the exact location of the transition point.

Let us define the new variables  \( u_{\pm} = (\gamma_{zx} \pm \gamma_{zy})/2 \) ,  \( v_{\pm} = (\gamma_{xz} \pm \gamma_{yz})/2 \) , and  \( r_{\pm} = (\gamma_{xy} \pm \gamma_{yx})/2 \)  which for  \( N_{u} \)  symmetry  \( (\gamma_{zx} = \gamma_{zy}, \gamma_{xz} = \gamma_{yz} \)  and  \( \gamma_{xy} = \gamma_{yx}) \)  are equal to  \( \gamma_{zx} \) ,  \( \gamma_{xz} \)  and  \( \gamma_{xy} \)  for the (+) sign, and strictly zero for the (−) sign. Also let us define the quantities

 \[ s_{\pm}=u_{\pm}(k_{2}\pm1)+v_{\pm}(k_{1}\pm1)+r_{\pm}(k_{2}\pm k_{2}). \quad (B1) \] 

Then we find that

 \[ \Psi_{1x}\Psi_{1y}=s_{+}^{2}-s_{-}^{2},\quad\Psi_{2}=2\left(u_{+}\kappa_{2}+v_{+}\kappa_{1}+r_{+}\kappa_{1}\kappa_{2}\right). \quad (B2) \]
 

The ideal part of the free-energy density, in these new variables, has the form

 \[ \begin{aligned}\Phi_{id}^{*}&=\rho^{*}\left\{\ln\rho^{*}-1+\sum_{\nu=\pm1}\left[(u_{+}+\nu u_{-})\ln\left(u_{+}+\nu u_{-}\right)+\left(v_{+}+\nu v_{-}\right)\ln\left(v_{+}+\nu v_{ -}\right)\right.\right.\\&\left.\left.+\left(r_{+}+\nu r_{-}\right)\ln\left(r_{+}+\nu r_{ -}\right)\right]\right\},\end{aligned} \quad (B3) \] 

while the excess part has the same expression (A4). Minimizing the total free energy density  \( \Phi_{id}^{*} + \Phi_{exc}^{*} \)  with respect to  \( u_{\pm} \) ,  \( v_{\pm} \)  and  \( r_{\pm} \) , we obtain

 \[ \ln(u_{+}^{2}-u_{-}^{2})+2y\left[1+y(s_{+}^{2}-s_{-}^{2})\right]\kappa_{2}+2y s_{+}(\kappa_{2}+1)+2\Lambda=0, \quad (B4) \] 

 \[ \ln(v_{+}^{2}-v_{-}^{2})+2y\left[1+y(s_{+}^{2}-s_{-}^{2})\right]\kappa_{1}+2y s_{+}(\kappa_{1}+1)+2\Lambda=0, \quad (B5) \] 

 \[ \ln(r_{+}^{2}-r_{-}^{2})+2y\left[1+y(s_{+}^{2}-s_{-}^{2})\right]\kappa_{1}\kappa_{2}+2y s_{+}(\kappa_{1}+\kappa_{2})+2\Lambda=0, \quad (B6) \] 

 \[ \ln\left(\frac{u_{+}+u_{-}}{u_{+}-u_{-}}\right)-2y s_{-}(\kappa_{2}-1)=0, \quad (B7) \] 

 \[ \ln\left(\frac{v_{+}+v_{-}}{v_{+}-v_{-}}\right)-2y s_{-}(\kappa_{1}-1)=0, \quad (B8) \] 

 \[ \ln\left(\frac{r_{+}+r_{-}}{r_{+}-r_{-}}\right)-2y s_{-}(\kappa_{1}-\kappa_{2})=0, \quad (B9) \] 

where  \( \Lambda \)  is a Lagrange multiplier which guarantees the constraint  \( 2\left(u_{+}+v_{+}+r_{+}\right)=1 \) . Considering the case of vanishingly small biaxial ordering, i.e.  \( u_{-}\sim0 \) ,  \( v_{-}\sim0 \)  and  \( r_{-}\sim0 \) (which is correct near and above the bifurcation point), we can expand Eqns. (B7), (B8) and (B9) up to first order in these variables to obtain in matrix form  \( A\cdoth=0 \) , where we have defined the vector  \( \boldsymbol{h}^{T}=(u_{-},v_{-},r_{-}) \)  and a matrix A with the form

 \[ A=\begin{pmatrix}1-y u_{+}(\kappa_{2}-1)^{2}&-y u_{+}(\kappa_{1}-1)(\kappa_{2}-1)&-y u_{+}(\kappa_{1}-\kappa_{2})(\kappa_{2}-1)\\ -y v_{+}(\kappa_{1}-1)(\kappa_{2}-1)&1-y v_{+}(\kappa_{1}-1)^{2}&-y v_{+}(\kappa_{2})(\kappa_{1}-1)\\ -y r_{+}(\kappa_{1}-\kappa_{2})(\kappa_{2}-1)&-y r_{+}(\kappa_{1}-\kappa_{2})(\kappa_{1}-1)&1-y r_{+}(\kappa_{1}-\kappa_{2})^{2},\end{pmatrix} \quad (B10) \] 

This matrix is to be evaluated at  \( u_{+} = \gamma_{zx} \) ,  \( v_{+} = \gamma_{\alpha z} \)  and  \( r_{+} = \gamma_{xy} \)  (the values for uniaxial symmetry). A nontrivial solution of  \( A \cdot h = 0 \)  is obtained when  \( \det(A) = 0 \) , which is equivalent to the condition

 \[ \begin{align*}y^{-1}&=u_{+}(\kappa_{2}-1)^{2}+v_{+}(\kappa_{1}-1)^{2}+r_{+}(\kappa_{1}-\kappa_{2})^{2}\\&=\frac{(\kappa_{1}-\kappa{2})^{2}}{2}-(\kappa_{1}-1)(\kappa_{1}+1-2\kappa_{2})u_{+}-(\kappa_{2}-1)(\kappa_{2}+1-2\kappa_{1})v_{+}.\end{align*} \quad (B11) \] 

The values of  \( u_{+} \) ,  \( v_{+} \)  and  \( r_{+} \)  at the bifurcation are those obtained from (B4), (B5) and (B6) taking  \( u_{-} = v_{-} = r_{-} = 0 \) . Note that, as they are not independent variables, we can solve
 

only the equations for  \( u_{+} \)  and  \( v_{+} \) , and substitute  \( r_{+} = 1/2 - u_{+} - v_{+} \)  in all the parameters depending on  \( r_{+} \) . The result is:

 \[ f_{1}(u_{+},v_{+})\equiv u_{+}-C^{-1}(u_{+},_{v_{+}})e^{-\xi_{1}(u_{+},v_{+})}=0, \] 

 \[ f_{2}(u_{+},v_{+})\equiv v_{+}-C^{-1}(u_{+},v_{+})e^{-\xi_{2}(u_{+},v_{+})}=0, \] 

 \[ C(u_{+},v_{+})=2\left[e^{-\xi_{1}(u_{+},v_{+})}+e^{-\xi_{2}(u_{+},v_{+})}+e^{-\xi{}_{3}(u_{+},v_{+})}\right], \quad (B12) \] 

where we have defined

 \[ \xi_{1}(u_{+},v_{+})=y\left[\kappa_{2}(1+y s_{+}^{2})+(\kappa_{2}+1)s_{+}\right], \quad (B13) \] 

 \[ \xi_{2}(u_{+},v_{+})=y\left[\kappa_{1}(1+y s_{+}^{2})+(\kappa_{1}+1)s_{+}\right], \quad (B14) \] 

 \[ \xi_{3}(u_{+},v_{+})=y\left[\kappa_{1}\kappa_{2}(1+y s_{+}^{2})+(\kappa_{1}+\kappa_{2})s_{+}\right], \quad (B15) \] 

and it is convenient to rewrite  \( s_{+} \) , considering that  \( u_{+} + v_{+} + r_{+} = 1/2 \) , as

 \[ s_{+}=\frac{\kappa_{1}+\kappa_{2}}{2}-(\kappa_{1}-1)u_{+}-(\kappa_{2}-1)v_{+}. \quad (B16) \] 

Once the values of  \( u_{+} \)  and  \( v_{+} \)  are found by solving the set (B12), the packing fraction at which the bifurcation occurs can be calculated from

 \[ \eta=\frac{y\Psi_{2}}{1+y\Psi_{2}},\quad\Psi_{2}=\kappa_{1}\kappa_{2}-2\kappa_{2}(\kappa_{1}-1)u_{+}-2\kappa_{1}(\kappa_{2}-1)v_{+}. \quad (B17) \] 

The set of end-points separating the regions in the  \( \kappa_{1}-\kappa_{2} \)  plane where the system (B12) has a different number of solutions can be calculated by equating the Jacobian to zero:

 \[ J(u_{+},v_{+})\equiv\left|\frac{\frac{\partial f_{1}}{\partial u_{+}}\frac{\partial f_{l}}{\partial v_{+}}}{\frac{\partial f_{2}}{\partial u_{+}}\frac{\partial f_{l}}{\partial v_{+}}}\right|. \quad (B18) \] 

Using Eqs. (B12) we obtain:

 \[ \begin{align*}J(u_{+},v_{+})~&=~1+3u_{+}v_{+}(1-2u_{+}-2v_{+})y^{3}(\kappa_{1}-1)^{2}(\kappa_{2}-1)^{2}(\widetilde{\kappa_{2}}-\kappa_{1})^{2}\\&~+~u_{+}(1-2u_{+})\frac{\partial\xi_{13}}{\partial u_{+}}+v_{+}(1-2v_{+})\frac{\partial\xi_{23}}{\partial v_{+}}-2u_{+}v_{+}\left(\frac{\partial\xi_{23}}{\partial u_{+}}+\frac{\partial\xi_{13}}{\partial v_{+}}\right),\end{align*} \quad (B19) \] 

where the explicit expressions for the functions  \( \partial\xi_{i3}/\partial(u_{+},v_{+}) \)  ( \( \xi_{i3}=\xi_{i}-\xi_{3} \)  and i=1,2)
 

are:

 \[ \begin{aligned}&\frac{\partial\xi_{13}}{\partial u_{+}}=-y(\kappa_{1}-1)^{2}\left[y\left(\kappa_{2}+(1+2y\kappa_{2}s_{+})s_{+}\right)\left(\kappa_{1}+1-2\kappa_{2}\right)-1-2y\kappa_{2}s_{+}\right],\\&\frac{\partial\xi_{13}}{\partial v_{+}}=-y(\kappa_{1}-1)(\kappa_{2}-1)\left[y\left(\kappa_{2}+(1+2y\kappa_{2}s_{+})s_{+}\right)\left(\kappa_{2}+1-2\kappa_{1}\right)-1-2y\kappa_{2}s_{+}\right],\\&\frac{\partial\xi_{23}}{\partial u_{+}}=-y(\kappa_{1}-1)(\kappa_{2}-1)\left[y\left(\kappa_{1}+(1+2y\kappa_{1}s_{+})s_{+}\right)\left(\kappa_{1}+1-2\kappa_{2}\right)-1-2y\kappa_{1}s_{+}\right],\\&\frac{\partial\xi_{23}}{\partial v_{+}}=-y(\kappa_{2}-1)^{2}\left[y\left(\kappa_{1}+(1+2y\kappa_{1}s_{+})s_{+}\right)\left(\kappa_{2}+1-2\kappa_{1}\right)-1-2\kappa{}_{1}s_{+}\right].\\ \end{aligned} \quad (B20) \] 

To compute the values of  \( u_{+} \) ,  \( v_{+} \)  and  \( \kappa_{1} \)  (we fix the value of  \( \kappa_{2} \) ) for the location of the critical end-point of the  \( N_{u}-N_{b} \)  transition, we need to solve Eqs. (B12) and also the equation:

 \[ J(u_{+},v_{+})=0. \quad (B21) \] 

## Appendix C: Spinodal instability to nonuniform phases

The spinodal instability of a uniform phase with respect to density modulations of a given symmetry can be calculated by searching the singularities of the structure factor matrix, whose elements can be calculated as

 \[ T_{\mu\nu,\tau\iota}(\pmb{q},\rho)=\delta_{\mu\nu,\tau\tau}-\rho\sqrt{\gamma_{\mu\nu}\gamma_{\tau\iota}}\hat{c}_{\mu\nu,\tau\iota}(\pmb{q},\rho), \quad (C1) \] 

with  \( \hat{c}_{\mu\nu,\tau\iota}(\pmb{q},\rho) \)  the Fourier transforms of the direct correlation functions, calculated from the second functional derivatives of  \( \mathcal{F}_{\mathrm{exc}}[\{\rho_{\mu\nu}\}] \)  with respect to density profiles. The latter can be computed as

 \[ -\hat{c}_{\mu\nu,\tau\iota}(\pmb{q},\rho)=\sum_{\alpha,\beta}\frac{\partial^{2}\Phi_{\mathrm{e x c}}}{\partial n_{\alpha}\partial n_{\beta}}\hat{\omega}_{(\alpha)}^{(\alpha)}(\pmb{q})\hat{\omega}_{(\tau\iota)}^{(\beta)}(\pmb{q}), \quad (C2) \] 

where the Fourier transforms of the weighting functions are

 \[ \hat{\omega}_{\mu\nu}^{(0)}(\pmb{q})=\hat{w}_{\mu\nu}^{(0)}\left(\pmb{q}\right)=\prod_{\tau=x,y}\chi_{0}(q_{\tau}^{*}\kappa_{\mu\nu}^{\tau}/2), \quad (C3) \] 

 \[ \hat{\omega}_{\mu\nu}^{(2)}(\pmb{q})=\sigma_{3}^{2}\hat{w}_{\mu\nu}^{(2)}(\pmb{q})=\sigma_{3}^{2}\prod_{\tau=x,y}\kappa_{\mu\nu}^{\tau}\chi_{1}(q_{\tau}^{*}\kappa_{\mu\nu}^{\tau}/2), \quad (C4) \] 

 \[ \hat{\omega}_{\mu\nu}^{(1x)}(\pmb{q})=\sigma_{3}\hat{w}_{\mu\nu}^{(1x)}(\pmb{q})=\sigma_{3}\kappa_{\mu\nu}^{x}\chi_{1}(q_{x}^{*}\kappa_{\mu\nu}^{x}/2)\chi_{0}(q_{y}^{*}\kappa_{\mu\nu}^{y}/2), \quad (C5) \] 

 \[ \hat{\omega}_{\mu\nu}^{(1y)}(\pmb{q})=\sigma_{3}\hat{w}_{\mu\nu}^{(1y)}(\pmb{q})=\sigma_{3}\kappa_{\mu\nu}^{y}\chi_{0}(q_{x}^{*}\kappa_{\mu\nu}^{x}/2)\chi_{1}(q_{y}^{*}\kappa_{\mu\nu}^{y}/2), \quad (C6) \]
 

(with  \( \chi_{0}(x)=\cos x \) ,  \( \chi_{1}(x)=\sin(x)/x \)  for  \( x\neq0 \)  while  \( \chi_{1}(0)=1 \) , and  \( q_{\tau}^{*}=q_{\tau}\sigma_{3} \) ).

The elements (C1) can be written in the following explicit form:

 \[ T_{\mu\nu,\tau\iota}=\delta_{\mu\nu,\tau}\iota+y\sqrt{\gamma_{\mu\nu}\gamma_{\tau\iota}}\left\{\langle\hat{w}_{\mu\nu}^{(0)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(2)}(\boldsymbol{q}^{*}) \right\}+\langle\hat{w}_{\mu\nu}^{(1x)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(1y)}(\boldsymbol{q}^{*}) \quad (C7) \] 

 \[ +y\left[\Psi_{1y}\langle\hat{w}_{\mu\nu}^{(1x)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(2)}(\boldsymbol{q}^{*}) \right)+\Psi_{1x}\langle\hat{w}_{\mu\nu}^{(1y)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(2)}(\boldsymbol{q}^{*}) \right\}+(1+2y\Psi_{1x}\Psi_{1y})\hat{w}_{\mu\nu}^{(2)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(2)}(\boldsymbol{\boldsymbol{q}}^{*})]\Bigg\}, \quad (C8) \] 

where we have defined

 \[ \langle\hat{w}_{\mu\nu}^{(\alpha)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(\beta)}(\boldsymbol{q}^{*}) \rangle=\hat{w}_{\mu\nu}^{(\alpha)}(\boldsymbol{q}^{*})\hat{w}_{\tau\iota}^{(\beta)}(\boldsymbol{q}^{*})+\hat{w}_{\mu\nu}^{(\beta)}(\mathbf{q}^{*})\hat{w}_{\tau\iota}^{(\alpha)}(\boldsymbol{q}^{*}). \quad (C9) \] 

Therefore the spinodal instability of a uniform phase with respect to density modulations can be found from

 \[ |T(\boldsymbol{q}^{*},\rho^{*})|=0, \quad (C10) \] 

where  \( |T(\boldsymbol{q}^{*},\rho^{*})| \)  denotes the determinant of the  \( 6 \times 6 \)  symmetric matrix with elements given by (C8). In this way we find the values  \( \rho_{b}^{*} \)  and  \( q_{b}^{*} \) at the bifurcation for which the absolute minimum of  \( |T(\boldsymbol{q}^{*},\rho^{*})| \)  as a function of  \( q^{*} \)  is equal to zero for the first time. In practice we select  \( \boldsymbol{q}^{*} = (q_{x}^{*}, 0) \)  or  \( \boldsymbol{q}^{*} = (0, q_{y}^{*}) \)  with  \( q_{x,y}^{*} = 2\pi\sigma_{3}/d_{x,y} \)  where  \( d_{x} \)  and  \( d_{y} \)  are the periods of nonuniform phases along x and y respectively. The values  \( \{\gamma_{\mu\nu}\} \)  at each step of the numerical procedure used to solve Eqns. (C10) are found from the solution of Eqn. (A9). Bifurcated phases can have different symmetries: smectic (S) or columnar (C), where density modulations exist along only one spatial direction which could coincide (S) or not (C) with the alignment directions of the particle projections. Also a crystalline phase (K) with full 2D positional ordering could exist with (orientational ordered K) or without (plastic K) orientational ordering.

[1] M. J. Freiser, Phys. Rev. Lett. 24, 1041 (1970).

[2] R. Berardi, L. Muccioli, S. Orlandi, M. Ricci, and C. Zannoni, J. Phys.: Condens. Matter 20, 463101 (2008); G. R. Luckhurst, Nature 430, 413 (2004).

[3] S. Kumar, Biaxial liquid crystal electro-optic devices, US Patent No. 7, 604, 850 (2009).

[4] M. P. Taylor and J. Herzfeld, Phys. Rev. A. 44, 3742 (1991).
 

[5] S. D. Peroukidis and A. G. Vanakaras Soft Matter 9, 7419 (2013); S. D. Peroukidis, A. G. Vanakaras, and D. J. Photinos, Phys. Rev. E 88, 062508 (2013).

[6] P. J. Camp and M. P. Allen, J. Chem. Phys. 106, 6681 (1997).

[7] A. N. Zakhlevnykh and P. A. Sosnin, Mol. Cryst. Liq. Cryst. 293, 135 (1997).

[8] P. I. C. Teixeira, A. J. Masters, and B. Mulder, Mol. Cryst. Liq. Cryst. 323, 167 (1998).

[9] M. A. Bates and G. R. Luckhurst, Phys. Rev. E 72, 051702 (2005).

[10] S. Orlandi, R. Berardi, J. Stelzer, and C. Zannoni, J. Chem. Phys. 124, 124907 (2006).

[11] P. Grzybowski and L. Longa, Phys. Rev. Lett. 107, 027802 (2011).

[12] R. Alben, J. Chem. Phys. 59, 4299 (1973).

[13] R. van Roij and B. M. Mulder, J. Phys. II 4, 1763 (1994).

[14] P. J. Camp and M. P. Allen, Physica A 229, 410 (1996); P. J. Camp, M. P. Allen, P. G. Bolhuis, and D. Frenkel, J. Chem. Phys. 106, 9270 (1997).

[15] H. H. Wensink, G. J. Vroege, and H. N. W. Lekkerkerker, J. Chem. Phys. 115, 7319 (2001).

[16] S. Varga, A. Galindo, and G. Jackson, Phys. Rev. E 66, 011707 (2002).

[17] R. Berardi and C. Zannoni, Soft Matter 8, 2017 (2012).

[18] L. J. Yu and A. Saupe, Phys. Rev. Lett. 45, 1000 (1980).

[19] L. A. Madsen, T. J. Dingemans, M. Nakata, and E. T. Samulski, Phys. Rev. Lett. 92, 145505 (2004).

[20] B. R. Acharya, A. Primak, and S. Kumar, Phys. Rev. Lett. 92, 145506 (2004).

[21] V. Prasad, S.-W. Kang, K. A. Suresh, L. Joshi, Q. Wang, and S. Kumar, J. Am. Chem. Soc. 127, 1722 (2005).

[22] T. J. Dingemans, L. A. Madsen, O. Francescangeli, F. Vita, D. J. Photinos, C.-D. Poon, and E. T. Samulski, Liq. Cryst. 40, 1655 (2013).

[23] E. Van den Pol, A. V. Petukhov, D. M. E. Byelov, and G. J. Vroege, Phys. Rev. Lett. 103, 258301 (2009).

[24] E. Van den Pol, D. M. E. Thies-Weesie, A. V. Petukhov, D. V. Byelov, and G. J. Vroege, Liq. Cryst. 37, 651 (2010).

[25] G. J. Vroege, Liq. Cryst. 41, 342 (2014).

[26] Y. Martínez-Ratón, S. Varga, and E. Velasco, Phys. Chem. Chem. Phys. 13, 13247 (2011).

[27] S. Belli, A. Patti, M. Dijkstra, and R. Van Roij, Phys. Rev. Lett. 107, 148303 (2011).

[28] S. Belli, M. Dijkstra, and R. van Roij, J. Phys.: Condens. Matter 24, 284128 (2012).
 

[29] A. B. G. M. Leferink op Reinink, S. Belli, R. van Roij, M. Dijkstra, A. V. Petukhov, and G. J. Vroege, Soft Matter 10, 446 (2014).

[30] K. Bénéut, D. Constantin, P. Davidson, A. Dessombz, and C. Chénéac, Langmuir 24, 8205 (2008).

[31] D. Constantin, P. Davidson, and C. Chénéac, Langmuir 26, 4586 (2010).

[32] K. Slyusarenko, D. Constantin, and P. Davidson, J. Chem. Phys. 140, 104904 (2014).

[33] J. A. Cuesta and Y. Martínez-Ratón, Phys. Rev. Lett. 78, 3681 (1997); J. A. Cuesta and Y. Martínez-Ratón, J. Chem. Phys. 107, 6379 (1997).

[34] Y. Martínez-Ratón, S. Varga, and E. Velasco, J. Chem. Phys. 140, 204906 (2014).

[35] S. Varga, Y. Martínez-Ratón, E. Velasco, G. Bautista-Carbajal and G. Odriozola, unpublished.

[36] J. Zhang, T. Vad, M. Heidelmann, T. E. Weirich and W. F. C. Sager, Soft Matter (2014, accepted manuscript).
 
