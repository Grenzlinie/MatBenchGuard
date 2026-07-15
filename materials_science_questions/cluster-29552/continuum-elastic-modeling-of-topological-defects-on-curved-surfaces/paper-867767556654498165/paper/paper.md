
# Crystalline Order on a Sphere and the Generalized Thomson Problem

M. Bowick, \( ^{1} \)  A. Cacciuto, \( ^{1}D. \)  R. Nelson, \( ^{2} \)  and A. Travesset \( ^{3} \) 

 \( ^{1} \)  Physics Department, Syracuse University, Syracuse NY 13244-1130, USA

 \( ^{2} \)  Lyman Laboratory of Physics, Harvard University, Cambridge MA 02138, USA and

 \( ^{3} \)  Loomis Laboratory, University of Illinois at Urbana, Urbana IL 61801, USA

We attack generalized Thomson problems with a continuum formalism which exploits a universal long range interaction between defects depending on the Young modulus of the underlying lattice. Our predictions for the ground state energy agree with simulations of long range power law interactions of the form  \( 1/r^{\gamma} \)  ( \( 0 < \gamma < 2 \) ) to four significant digits. The regime of grain boundaries is studied in the context of tilted crystalline order and the generality of our approach is illustrated with new results for square tilings on the sphere.

PACS numbers: PACS numbers: 68.35.Gy, 62.60.Dc, 61.72.Lk. 61.30.Jf

The Thomson problem of constructing the ground state of (classical) electrons interacting with a repulsive Coulomb potential on a 2-sphere [1] is almost one hundred years old [2] and has many important physical realizations. These include multi-electron bubbles [3], which may be studied by capillary wave excitations, or the surface of liquid metal drops confined in Paul traps [4]. Although the original Thomson problem refers to the ground state of spherical shells of electrons, one can also ask for crystalline ground states of particles interacting with other potentials. Such a generalized Thomson problem arises, for example, in determining the arrangements of the protein subunits which comprise the shells of spherical viruses [5, 6]. Here, the “particles” are clusters of protein subunits arranged on a shell. Other realizations include regular arrangements of colloidal particles in colloidosomes [7] proposed for encapsulation of active ingredients such as drugs, nutrients or living cells [8] and fullerene patterns of carbon atoms on spheres [9] and other geometries [10]. An example with long range (logarithmic) interactions is provided by the Abrikosov lattice of vortices which would form at low temperatures in a superconducting metal shell with a large monopole at the center [11]. In practice, the “monopole” could be approximated by the tip of a long thin solenoid.

Extensive numerical studies of the Thomson problem show that the ground state for a small number of particles, typically  \( M \leq 150 \) , consists of twelve positive disclinations (the minimum number compatible with Euler's theorem) located at the vertices of an icosahedron [12, 13]. Recent results have shown that for systems as small as 500 particles, however, configurations with additional topological defects [14, 15] have lower energies than icosahedral ones.

These remarkable results for the Thomson problem raise a number of important questions, such as the mechanism behind the proliferation of defects, the nature of these unusual low-energy states, the universality with respect to the underlying particle potential and the generalization to more complex situations.

A formalism suitable to address all these questions has been proposed recently \( ^{[16]} \) . Disclinations are considered the fundamental degrees of freedom, interacting according to the energy  \( [16] \) 

 \[ \begin{align*}H=E_{0}+\frac{Y}{2}\int\int d\sigma(x)d\sigma(y)\\\left[\left(s(x)-K(x)\right)\frac{1}{\Delta^{2}}\Big(s(y)-K(y)\Big)\right],\end{align*} \quad (1) \] 

where the integration is over a fixed surface with area element  \( d\sigma(x) \)  and metric  \( g_{ij} \) , K is the Gaussian curvature, Y is the Young modulus in flat space and  \( s(x)=\sum_{i=1}^{N}\frac{\pi}{3}q_{i}\delta(x,x_{i}) \)  is the disclination density  \( \left(\delta(x,x_{i})=\delta(x-x_{i})/\sqrt{det(g_{ij})}\right) \) . Defects like dislocations or grain boundaries are built from these elementary disclinations.  \( E_{0} \)  is the energy corresponding to a perfect defect-free crystal with no Gaussian curvature;  \( E_{0} \)  would be the ground state energy for a 2D Wigner crystal of electrons in the plane. Eq.(1) restricted to a 2-sphere gives

 \[ \begin{align*}H=E_{0}+\frac{\pi Y}{36}R^{2}\sum_{i=1}^{N}\sum_{j=1}^{N}q_{i}q_{j}\chi(\theta^{i},\psi^{i};\theta^{j},\psi^{j})\\+\ N E_{core},\end{align*} \quad (2) \] 

where R is the radius of the sphere and  \( \chi \)  is a function of the geodesic distance  \( \beta_{ij} \)  between defects with polar coordinates  \( (\theta^{i},\psi^{i};\theta^{j},\psi^{j})[16] \) ;  \( \chi(\beta)=1+\int_{0}^{\frac{1-\cos\beta}{2}}dz\frac{\ln z}{1-z} \) . Here 5- and 7-fold defects correspond to  \( q_{i}=+1 \)  and -1 respectively. In this letter we show that the continuum formalism embodied in Eq.(2) implies: (a) flat space results for elastic constants can be bootstrapped into very accurate quantitative calculations for generalized Thomson problems, thus providing a stringent test of the validity of this approach; (b) new results for finite length grain boundaries, consisting of dislocations with variable spacing, in the context of the  \( 2\pi \)  disclinations appearing in tilted liquid crystal phases[17]; and (c) sufficient power and generality to determine the ground state for the 8 minimal disclinations arising in square tilings of a sphere.
 

<table><tr><td>\( \gamma \)</td><td>\( a_{1}(\gamma) \)</td><td>\( (n,n) \)</td><td>\( n,0 \)</td></tr><tr><td>1.5</td><td>1.51473</td><td>1.51454(2)</td><td>1.51445(2)</td></tr><tr><td>1.25</td><td>1.22617</td><td>1.22599(7)</td><td>1.22589(7)</td></tr><tr><td>1.0</td><td>1.10494</td><td>1.10482(3)</td><td>1.10464(3)</td></tr><tr><td>0.75</td><td>1.04940</td><td>1.04921(6)</td><td>1.04910(6)</td></tr><tr><td>0.5</td><td>1.02392</td><td>1.02390(4)</td><td>1.02372(4)</td></tr></table>

TABLE I: Analytical predictions (first column) for a large number of particles and values extrapolated from numerical simulations (second and third columns) of the coefficient  \( a_{1}(\gamma) \) , as defined in Eq.(4) for  \( (n,n) \)  and  \( (n,0) \)  icosadeltahedral lattices. Similar accuracy holds for other values of  \( \gamma \) .

The Young modulus appearing in Eq.(2) and the energy  \( E_{0} \)  may be computed in flat space via the Ewald method [18, 19]. The result for M particles with long range pairwise interactions given by  \( e^{2}/r^{\gamma} \)  ( \( 0 < \gamma < 2 \) ) is [20]

 \[ \begin{aligned}Y\quad&=\quad4\eta(\gamma)\frac{e^{2}}{A_{C}^{1+\gamma/2}},\\\frac{E_{0}}{Me^{2}}\quad&=\quad\theta(\gamma)\left(\frac{4\pi}{A_{C}}\right)^{\gamma/2}+\frac{\pi}{A_{C}R^{\gamma-2}}\rho(\gamma),\end{aligned} \quad (3) \] 

where  \( \eta \) ,  \( \theta \)  and  \( \rho \)  are potential-dependent coefficients whose numerical values will be reported elsewhere [20] and  \( A_{C} \)  is the area per particle. For M particles crystallizing on the sphere,  \( A_{C} = 4\pi R^{2}/M \) , and combining Eqs.(2) and (3) gives a large M expansion for the ground state energy,

 \[ E_{G}=\frac{e^{2}}{2R^{\gamma}}\left[a_{0}(\gamma)M^{2}-a_{1}(\gamma)M^{1+\frac{\gamma}{2}}+a_{2}(\gamma)M^{\frac{\gamma}{2}}+\cdots\right], \quad (4) \] 

where  \( a_{0}(\gamma) = 2^{1-\gamma}/(2-\gamma) \)  and the subleading coefficients  \( a_{i}(\gamma) \)  depend explicitly on the potential and on the positions and number of disclinations. The first (non-extensive) term is proportional to  \( M^{2} \)  and is usually canceled by a uniform background charge for Wigner crystals of electrons. The coefficient  \( a_{1} \)  is a universal function of the positions of the defects, up to a potential-dependent constant. Using the results in [16], theoretical predictions for large M for icosadeltahedral lattices [5] of type  \( (n,0) \)  and  \( (n,n) \)  are given in Table I for five values of  \( \gamma \) .

These predictions may now be compared with direct minimizations of particles on the sphere in icosadeltahedral configurations by fitting the results to Eq.(4). In Fig.1 we plot  \( \varepsilon(M) \)  versus 1/M for  \( (n,0) \)  and  \( (n,n) \)  icosadeltahedral configurations for  \( \gamma = 1.5 \)  and  \( \gamma = \overline{0.5} \) , where

 \[ \varepsilon(M)=\frac{[2R^{\gamma}E_{G}/e^{2}-a_{0}(\gamma)M^{2}]}{M^{1+\gamma/2}}. \quad (5) \] 

The coefficient  \( a_{1}(\gamma) \)  is determined by the intercept in the  \( M \rightarrow \infty \)  limit ( \( M = 10n^{2} + 2 \)  for  \( (n,0) \)  lattices and  \( M = 30n^{2} + 2 \)  for  \( (n,n) \)  lattices [5]).

![](./images/867767556654498165_1.jpg)

FIG. 1: Numerical estimate of  \( \varepsilon(M) \)  as a function of 1/M for  \( (n,0) \)  and  \( (n,n) \)  icosadeltahedral lattices with  \( \gamma = (1.5, 0.5) \) .

![](./images/867767556654498165_2.jpg)

![](./images/867767556654498165_3.jpg)

FIG. 2: Strain energy distribution (red/high, blue/low) for a  \( (10,0) \)  and a  \( (6,6) \)  configuration.
 
![](./images/867767556654498165_4.jpg)

FIG. 3: A 10-arm grain boundary array emerging from a +6 defect (purple square) at the north pole. Charge +1 disclinations are red and charge -1 disclinations are yellow.

The continuum elastic interaction between disclinations in Eq.(2) is essential to obtain the correct limiting behavior since it reflects contributions both from the energy per particle in flat space as well as the energies of 12 isolated disclinations. The defect core energy term in Eq.(2) contributes to the leading correction  \( a_{2}(\gamma) \) . We find agreement to four significant figures for  \( (n,0) \)  icosadeltahedral lattices and to five significant figures for  \( (n,n) \)  lattices. The small residual difference in energy for  \( (n,0) \)  and  \( (n,n) \)  configurations may be understood from the differing strain energies shown in Fig.2. This small discrepancy may be attributable to a line tension associated with ridges of minimum or maximum strain connecting disclinations [20].

We now turn to the study of grain boundaries on a sphere using the model described by Eq.(2). We illustrate the method [16] by considering just two  \( 2\pi \)  defects (appropriate to crystals of tilted molecules) with suitable boundary conditions [17]. To approximate the  \( 2\pi \)  disclination of tilted molecules in a hemispherical crystal [17] we replace the icosahedral configuration of twelve disclinations with two clusters of six  \( 2\pi/6 \)  defects at the north and south poles. For simplicity, we use isotropic elastic theory and neglect nonuniversal details near the core of the  \( +2\pi \)  disclination. Upon adding just one dislocation of Burgers vector b (i.e.  \( a^{+/-}2\pi/6 \)  disclination pair separated by distance b), the minimum energy in Eq.(2) is achieved by a polar angle  \( \theta_{0}(b) \)  with  \( \vec{b} \)  perpendicular to the geodesic joining the north and south poles. For small numbers of dislocations, the minimum energy configuration consists of two polar rings of dislocations located at angles  \( \theta_{0}(b) \)  and  \( \pi - \theta_{0}(c) \)  relative to the north pole. The dislocations eventually organize into grain boundaries centered on  \( \theta_{0}(b) \) , as shown in Fig.3. Remarkably, no other minima were found.

Because the global minimization just described becomes computationally demanding for more than thirty defects, further minimizations focused on a reduced parameter space specified by the orientations and distances

![](./images/867767556654498165_5.jpg)

FIG. 4: Defect positions obtained from minimization (up triangle) and from Eq. \( (7) \)  (diamonds).

of the grain boundaries from the two +6 defects. Following [16], the system dynamically chooses the average lattice spacing  \( a \equiv b \)  that best accommodates the array structure by extremizing the energy of Eq.(2).

For reasonable parameter values in our continuum description, both two antipodal +6 disclinations and the icosadeltahedral configurations are indeed unstable to the formation of grain boundaries for sufficiently large sphere radius \( ^{[14, 15, 16, 23]} \) . In a flat monolayer, the spacing between dislocations in m-grain boundary arms radiating from a disclination of charge s is given by  \( [21] \) 

 \[ l=\frac{b}{2\sin\left(\frac{s}{2m}\right)}, \quad (6) \] 

where b is the Burgers vector charge. The disclination charge is  \( s = \frac{2\pi}{6}p \)  (p = 1 or 6, corresponding to the Thomson problem or tilted molecules, respectively). To generalize this result for symmetrical grain boundaries on a sphere, consider the Burgers circuit formed by an isosceles spherical triangle with apex angle  \( \phi_{gb} = s/m \)  at a disclination at the north pole and centered on one of the m-grain boundary arms [22]. If the altitude of this triangle is h, the net Burgers vector B defined by this circuit is given by the geodesic distance spanning the base of this triangle. A straightforward exercise in spherical trigonometry leads to

 \[ \cos\left(\frac{B}{R}\right)=\frac{\cot^{2}(h/R)\cos^{2}(\phi_{gb}/2)+\cos(\phi_{gb})}{1+\cot^{2}(h/R)\cos^{2}(\phi_{gb}/2)}. \quad (7) \] 

Writing  \( B \approx b \int_{0}^{h} dh' / l(h') \) , where  \( l(h) \)  is a (variable) dislocation spacing [16], we can invert this formula and thus generalize Eq.(6) to the sphere.

Results comparing our minimization with Eq. \( (7) \)  are shown in Fig.4. Both approaches predict the same number of dislocations within a grain and dislocation spacings which increase with  \( \theta \)  [16]. The small discrepancies in the positions of the dislocations are presumably due to interactions between dislocations in different arms.

The physics associated with Eq. \( (2) \)  is remarkably general. We sketch here how the results above may be
 

adapted to a sphere tiled with a square lattice. A planar square lattice is described by three elastic constants (as opposed to the two Lamé coefficients in the triangular case), leading to an energy

 \[ H=\frac{\lambda_{\alpha\beta,\mu\nu}}{2}\int d^{2}\mathbf{x}u_{\alpha\beta}u_{\mu\nu}, \quad (8) \] 

where the independent elastic constants are  \( \lambda_{11,11} \) ,  \( \lambda_{1,1,22} \)  and  \( \lambda_{12,12} \) . The same derivation as that leading to Eq.(1) now leads to

 \[ H=\frac{1}{2}\int d\sigma(x)d\sigma(y)\Big(K(x)-s(x)\Big)G(x,y)\Big(K(y)-s(y)\Big), \quad (9) \] 

where  \( G(x,y)=(\frac{1}{T}\Delta^{2}+2\epsilon\nabla_{1}^{2}\nabla_{2}^{2})^{-1} \) , with  \( \nabla_{i} \)  the gradient in direction i=1 or 2, as defined by the local square lattice. The fundamental defects are now  \( \pm\frac{\pi}{2} \)  disclinations. The elastic constants are

 \[ \begin{aligned}Y&=\frac{\lambda_{11,11}^{2}-\lambda_{11,22}^{2}}{\lambda_{11,11}},\\ \epsilon&=-\frac{\lambda_{11,22}+\lambda_{11,11}}{\lambda_{11,11}^{2}-\lambda_{11,22}^{2}}+\frac{1}{2\lambda_{12,12}}.\end{aligned} \quad (10) \] 

The interaction energy for disclinations in a square lattice becomes equivalent to Eq. \( (1) \)  only in the limit  \( \epsilon = 0 \) . Although details such as the critical value of  \( R/a \)  for the onset of grain boundaries will differ, we expect that the physics remains essentially the same. For small numbers of particles the ground state will consist of  \( 8 q = +1 \)  disclinations. In the isotropic case ( \( \epsilon = 0 \) ) the ground state is a distorted cube, with one face twisted by  \( 45^{\circ} \)  [20], similar to tetratic liquid crystal ground states on the sphere [24].

We expect similar results for geometries other than the sphere. For isotropic crystals on a torus with the right aspect ratio, for example, one might expect 12 5-fold disclinations on the outer wall (where the Gaussian curvature is positive) and twelve compensating 7-fold disclinations on the inner wall (where the Gaussian curvature is negative) to play the role of the icosahedral configurations on the sphere. As more particles are placed on the torus, we expect grain boundaries to emerge from these disclinations.

There are some important issues left for a future publication [20], such as a more detailed derivation of the asymptotic expansion Eq.(4) and a reliable determination of the optimal number of arms within a grain boundary. We hope the calculations presented here will convince the reader of the usefulness of our approach.

It is a pleasure to thank Alar Toomre for sharing with us his numerical work on the original Thomson problem. The work of M.B. and A.C. has been supported by the U.S. Department of Energy (DOE) under Contract No. DE FG02 85ER40237. The research of D.R.N was supported by the National Science Foundation through Grant No. DMR97-14725 and through the Harvard Material Research Science and Engineering Laboratory via Grant No. DMR98-09363. The work of A.T. has been supported by the Materials Computation Center and grants NSF-DMR 99-76550 and NSF-DMR 00-72783.

[1] J. J. Thomson, Philos. Mag. 7, 237 (1904).

[2] E.B. Saff and A.B.J. Kuijlaars, Math. Intelligencer 19, 5 (1997).

[3] P. Leiderer, Z. Phys. B98, 303 (1993).

[4] E.J. Davis, Aerosol Sci. Techn. 26, 212 (1997).

[5] D.L.D. Caspar and A. Klug, Cold Spring Harbor Symp. Quant. Biol. 27, 1 (1962).

[6] C.J. Marzec and L.A. Day, Biophys. Jour. 65, 2559 (1993).

[7] M. Nikolaides, Thesis, Physics Department, TU Munich, 2001.

[8] A.D. Dinsmore, M.F. Hsu, M. Nikolaides, M. Marquez, A.R. Bausch and D.A. Weitz, Colloidosomes: Selectively-Permeable Capsules Composed of Colloidal Particles (to be published).

[9] H.W. Kroto et al, Nature 318, 162 (1985).

[10] J.O.M. Sano, A. Kamino, and S. Shinkai, Science 293, 1299 (2001).

[11] M.J.W. Dodgson and M.A. Moore, Phys. Rev. B 55, 3816 (1997) (arXiv:cond-mat/9512123).

[12] E.L. Altschuler, T.J. Williams, E.R. Ratner, R. Tipton, R. Stong, F. Dowla and F. Wooten, Phys. Rev. Lett. 78, 2681 (1997).

[13] T. Erber and G.M. Hockney, Adv. Chem. Phys. 98, 495 (1997).

[14] A. Toomre, private communication.

[15] A. Perez-Garrido and M. A. Moore, Phys. Rev. B 60, 15628 (1999) (arXiv:cond-mat/9905217) and references therein.

[16] M. Bowick, D. R. Nelson, and A. Travesset, Phys. Rev. B 62, 8738 (2000) (arXiv:cond-mat/9911379).

[17] R. Pindak, S.B. Dierker, and R.B. Meyer, Phys. Rev. Lett. 56, 1819 (1986); by introducing a pressure difference across the free standing liquid crystal film, one could study the  \( 2\pi \)  disclinations and grain boundaries of this reference in a hemispherical environment (R. Pindak and C.C. Huang, private communication).

[18] L. Bonsall and A.A. Maradudin, Phys. Rev. B 15, 1959 (1977).

[19] D. Fisher, B. Halperin, and R. Morf, Phys. Rev. B 20, 4692 (1979).

[20] M. Bowick, A. Cacciuto, D.R. Nelson, and A. Travesset, in preparation.

[21] J. P. Hirth and J. Lothe, Theory of Dislocations (Wiley, New York, 1982).

[22] C. Carraro and D. R. Nelson, Phys. Rev. E 48, 3082 (1993) (arXiv:cond-mat/9307008).

[23] For the purposes of determining grain boundary stability it is useful to write the core energy term  \( E_{core} \)  in Eq.(2) as  \( NE_{core} = 12E_{5} + \frac{N-12}{2}E_{d} \)  and parametrize the physics in terms of a dislocation core energy  \( E_{d} \)  of order  \( 0.1Ya^{2} \) . For antipodal +6 defects,  \( NE_{core} = 2E_{6} + \frac{N-2}{2}E_{d} \) .

[24] T.C. Lubensky and J. Prost, J. Phys. II 2, 371 (1992).
 
