
# Sedimentation profiles and phase stacking diagrams in polydisperse hard rounded rectangle fluids

Tobias Eckert

German Aerospace Center (DLR), Earth Observation Center, Remote Sensing Technology Institute, Oberpfaffenhofen, 82234 Wessling, Germany and Physikalisches Institut, Universität Bayreuth, D-95440 Bayreuth, Germany

Daniel de las Heras \( ^{*} \) 

Institut für Theoretische Physik, Universität Tübingen, D-72076 Tübingen, Germany and Physikalisches Institut, Universität Bayreuth, D-95440 Bayreuth, Germany

Enrique Velasco
Departamento de Física Teórica de la Materia Condensada,
Instituto de Física de la Materia Condensada (IFIMAC) and Instituto de Ciencia de Materiales Nicolás Cabrera,
Universidad Autónoma de Madrid E-28049 Madrid, Spain

Yuri Martínez-Ratón
Universidad Carlos III de Madrid, Departamento de Matemáticas,
Grupo Interdisciplinar de Sistemas Complejos (GISC), 28911 Leganés, Spain
(Dated: November 11, 2025)

We analyze the sedimentation behavior of a polydisperse two-dimensional liquid-crystal fluid using a local density functional theory based on scaled particle theory. Polydispersity is incorporated through variations in the roundness of hard rectangular particles interacting solely via excluded area effects. Despite its simplicity, the model displays a rich phenomenology. In bulk, the fluid exhibits isotropic, nematic, and tetratic phases. In sedimentation, we obtain complex phase stacking diagrams featuring multiphasic stacking sequences with up to four stacks of different bulk phases, inverted stacking sequences such as top isotropic and bottom nematic together with top nematic and bottom isotopic, as well as stacking sequences with reentrant stacks such as tetratic and nematic stacks floating between two isotropic stacks. This phenomenology arises as a result of an intricate coupling between particle polydispersity and the effect of gravity. Our approach can be easily adapted to investigate the sedimentation behavior of other polydisperse colloidal systems.

## I. INTRODUCTION

Colloidal systems are inherently polydisperse and exhibit variations in particle size and shape. Polydispersity is more pronounced in some natural colloids, such as clays  \( [1] \) . Recent improvements in synthetic methods have made it possible the synthesis of micronsize particles with sharp size distributions  \( [2–5] \) . However, a certain degree of polydispersity is unavoidable, even for microspheres  \( [6, 7] \) , and small variations in particle sizes and shapes can affect the macroscopic properties of colloidal systems  \( [8, 9] \) .

Polydispersity significantly alters the entropy, and consequently the bulk phase behavior of colloidal systems, which is often the result of a delicate balance between different entropic contributions to the free energy. In particular, the ideal mixing entropy increases with polydispersity, while the interaction (e.g. excluded-volume) contribution is modified in non-trivial ways by the presence of different species. Polydispersity changes the relative stability of bulk phases  \( [10–15] \) , induces fractionation  \( [16] \) , and also preempts the formation of certain bulk phases that emerge in the corresponding monodisperse systems. Above a terminal polydispersity, the crystallization of hard-spheres  \( [17–19] \)  and the formation of smectic phases in suspensions of colloidal rods  \( [20] \)  are absent. In suspensions of silica rods, polydispersity can suppress the formation of crystalline phases, favoring instead a smectic B phase  \( [21] \) . Conversely, polydispersity can also stabilize phases that are not stable in the corresponding monodisperse system  \( [22–24] \) . A detailed understanding of how polydispersity modifies the bulk behavior remains an ongoing challenge.

Valuable information about the bulk phase equilibria of colloidal suspensions can be obtained from sedimentation experiments, where a colloidal sample is left to equilibrate in a cuvette under the influence of gravity. However, the gravitational length (i.e., the ratio between thermal energy and gravitational energy per unit of height) if often comparable to or even smaller than the sample height in colloidal systems. Hence, there is frequently a strong coupling between the gravitational field and bulk phenomena due to the gravity-induced particle density gradient along the vertical direction. In monodisperse colloidal systems, the height dependent density distribution provides a direct and rather intuitive way to understand the bulk phase behavior  \( [25–29] \) . In bi-
 

nary mixtures, there exist in general two distinct gravitational lengths and hence gravity affects each species differently. The gravitational field stabilizes the formation of stacking sequences with several stacks of different bulk phases  \( [30–35] \) . Moreover, the same bulk phase can appear twice within the cuvette. An example is the isotropic-nematic-isotropic stacking sequence experimentally observed in sphere-plate mixtures  \( [36] \) . Hence, drawing conclusions about bulk phenomena in binary mixtures from sedimentation experiments is a delicate issue.

An even more intricate interplay between gravity and bulk phenomena is expected in polydisperse colloidal systems since particle sizes and buoyant masses are not limited to a discrete set but are instead described by a density distribution function. The gravitational field creates a height-dependent density distribution function that differs from its bulk (parent) counterpart. Hence, phases that are not stable in bulk for a given parent distribution might appear in a sedimentation sample due to e.g. gravity-induced strong fractionation. Sedimented samples of highly polydisperse goethite nanorods revealed the formation of a smectic phase  \( [37, 38] \)  even though the polydispersity of the parent distribution was well above the theoretical terminal polydispersity for smectic phases  \( [20] \) . A polydisperse suspension of natural clay rods developed nematic-nematic demixing due to a pronounced, gravity-induced, fractionation in the rod length  \( [39] \) . In a suspension of highly polydisperse gibbsite platelets, the sedimented samples exhibited either an isotropic stack on top of a nematic one, or the inverse sequence (top nematic and bottom isotropic) depending on the sample height and average packing fraction  \( [40] \) .

To infer bulk phase equilibria from sedimentation experiments in polydisperse systems, we must first understand the role played by the gravitational field. From a theoretical point of view, sedimentation path theory  \( [35, 41, 42] \)  incorporates the gravitational field on top of the bulk description of the system. The theory relies on a local equilibrium approximation that at each height maps the sedimented sample to a bulk system using local (height-dependent) chemical potentials. So far, sedimentation path theory was used to study sedimentation in binary colloidal mixtures  \( [35, 36, 41–48] \) , polymer-colloid mixtures  \( [49] \) , and mass-polydisperse colloidal systems  \( [29, 50] \) . In a mass-polydisperse system, the colloidal particles have identical shapes and sizes but there is a continuous distribution of buoyant masses. Since mass-polydispersity does not alter the interparticle interactions with respect to a monodisperse system, it is possible to derive an effective chemical potential that describes how the state of the mass-polydisperse sample changes along the cuvette. Mass-polydispersity does not affect bulk equilibria but it can have a profound impact on sedimented samples with mass-distributions close to the experimentally relevant density-matching regime  \( [29, 50] \) .

Studying mass-polydisperse models is useful to isolate the effect of the gravitational field but it does not allow us to understand the interplay between bulk equilibria and gravity. As a first step in this direction, we theoretically investigate here the sedimentation of a two-dimensional model colloidal system with shape polydispersity by minimizing a local density functional in the presence of gravity. Bellier-Castella and Xu used a conceptually similar approach to study sedimentation of polydisperse isotropic particles (Van der Waals fluids) [51]. We model the particles as polydisperse hard rounded rectangles (HRR). Martínez-Ratón and Velasco recently investigated the bulk system [52] with scaled particle theory (SPT) [53]. The model exhibits isotropic, tetratic, and nematic phases. Several effects were attributed to polydispersity [52]: (i) a decrease of the stability of the tetratic phase, (ii) the occurrence of strong fractionation between coexisting phases, (iii) a change in the nature of the isotropic-nematic bulk transition from continuous to first order, and (iv) a packing fraction inversion in which the disordered isotropic phase has higher packing fraction than the orientationally ordered nematic phase.

In this work, we focus on the effect of the gravitational field on a polydisperse fluid of HRR. We first extend the scaled particle theory presented in Ref. [52] to spatially inhomogeneous systems via a simple local density approximation. Gravity is then incorporated to the polydisperse system as an external potential contribution to the free energy density functional. The height-dependent particle distribution function along the sedimented sample is obtained via a free minimization of the functional with respect to the full particle distribution resolved in both space and orientations. We found several stacking sequences that we group in a stacking diagram in the plane of average packing fraction and sample height. Unlike monodisperse and mass-polydisperse systems, shape polydisperse systems exhibit pairs of inverted stacking sequences, e.g. tetratic-nematic and its inverse nematic-tetratic. These inverted sequences are stable in different regions of the stacking diagram. Moreover, the degree of polydispersity has a strong effect on the topology of the stacking diagram, emphasizing its essential role on sedimentation.

## II. MODEL

Particle model. The fluid is composed of two-dimensional hard particles, each one with a fixed rectangular core of length L and width  \( D\ (L \geq D) \)  and a hard envelope obtained by sliding the center of mass of a disk of diameter l along the perimeter of the core, resulting in a rectangular shape with rounded corners. A sketch of the particle is shown in Fig. 1(a). The roundness length l is treated as a polydisperse variable and therefore distributed according to a given probability distribution function. For a given l, the particle area is

 \[ a(l)=L D+(L+D)l+\frac{\pi}{4}l^{2}. \quad (1) \]
 
![](2511.07034v1-images/2_0.jpg)

FIG. 1. Particle model and distributions. (a) Sketch of a HRR (blue) obtained from a fixed rectangular core (green) of dimensions  \( L \times D \)  by sliding a disk of diameter l (dashed-orange) around the perimeter of the core. (b) Parent distributions,  \( f(l) \) , as a function of the scaled roundness length  \( l/l_{0} \) . The values of the parameters  \( \nu \)  and s characterizing the distributions are indicated in the figure. (c) Representative examples of the particles considered in this study: polydisperse distribution functions with mean aspect ratios  \( \kappa_{0} = 2.22 \)  and  \( \kappa_{0} = 1.75 \) , see Eq. (33).

Particle distribution. We consider a column of height H of an equilibrium fluid of polydisperse HRR sedimented according to the law of gravity. The main magnitude characterizing the fluid behavior is the density profile,  \( \rho(l,z,\phi) \) , of particles with roundness length l, located at (vertical) position z (measured from the bottom of the sample), and with principal axes (parallel to the core side of length L) forming an angle  \( \phi \)  with respect to the z-axis (the direction of the nematic or one of the 4-atic directors) of a fixed reference frame.

Let  \( \rho_{0} \)  denote the mean density of the whole sample. Then, the following constraint on the density profile holds:

 \[ \frac{1}{H}\int_{0}^{H}d z\int_{0}^{\pi}d\phi\rho(l,z,\phi)=\rho_{0}f(l). \quad (2) \] 

Due to the head-tail symmetry of the particles, the angular integration can be restricted to the interval  \( [0, \pi] \) . The function  \( f(l) \)  is the fixed parent roundness length-distribution function, which we take as the truncated Schulz distribution

 \[ f(l)=\mathcal{C}\left(\frac{l}{l_{0}}\right)^{\nu}e^{-\alpha l/l_{0}}\Theta\left(l_{\mathrm{m a x}}-l\right), \quad (3) \] 

where  \( l_{max} \)  is the cut-off for the maximum roundness length and  \( \Theta(x) \)  is the Heaviside function. The normalization constant C and the parameter  \( \alpha \) , which depend on the exponent  \( \nu \)  and  \( l_{max} \) , are calculated by imposing the normalization

 \[ \int_{0}^{l_{\max}}d l f(l)=1, \quad (4) \] 

and fixing the value of the mean roundness length

 \[ \int_{0}^{l_{\max}}d l l f(l)=l_{0}. \quad (5) \] 

We use the mean roundness length,  \( l_{0} \) , as our unit of length. The exponent  \( \nu \)  together with the parameter  \( \alpha \)  in Eq. (3) control the degree of polydispersity which we quantify through the relative standard deviation

 \[ s\equiv\sqrt{\frac{\langle l^{2}\rangle_{f}}{l_{0}^{2}}-1}, \quad (6) \] 

with

 \[ \langle l^{2}\rangle_{f}\equiv\int_{0}^{l_{\max}}d l l^{2}f(l). \quad (7) \] 

In our numerical calculations, all the integrals in l were performed using a Gauss-Legendre quadrature with 101 points for  \( \nu=0 \)  and  \( l_{max}=5l_{0} \)  resulting in the polydisperse coefficient s=0.936, and 81 points for  \( \nu=2.82 \)  and  \( l_{max}=3l_{0} \)  resulting in s=0.5. These are the two cases selected for analysis, corresponding to large and moderate polydispersities. The parent distribution functions and illustrative particle shapes corresponding to them are shown in Fig. 1(b) and Fig. 1(c), respectively.

## III. THEORY

We use the SPT to approximate the interaction or excess part of the Helmholtz free energy per unit of area, which is supplemented by a local density approximation (the implications of this approximation are discussed later). The excess-free energy density (i.e., the excess part of the Helmholtz free-energy,  \( F_{exc} \) , divided by the system area, A, and scaled with the Boltzmann factor,  \( \beta^{-1} = K_{B}T \) ) depends locally on  \( \rho(l, z, \phi) \)  and has the
 

form [52]:

 \[ \begin{align*}\Phi_{\mathrm{exc}}(z)&\equiv\frac{\beta\mathcal{F}_{\mathrm{exc}}[\rho]}{A}\\&=-m_{0}^{(0)}(z)\ln\left[1-\eta(z)\right]+\frac{\langle\langle A_{\mathrm{spt}}\rangle\rangle(z)}{1-\eta(z)},\end{align*} \quad (8) \] 

where  \( m_{0}^{(0)}(z) \)  is the integrated density profile (see below), and the local packing fraction is defined as

 \[ \eta(z)=\int_{0}^{l_{\max}}d l\int_{0}^{\pi}d\phi\rho(l,z,\phi)a(l). \quad (9) \] 

Inserting Eq. (1) into (9) we obtain

 \[ \eta(z)=L D m_{0}^{(0)}(z)+(L+D)m_{1}^{(0)}(z)+\frac{\pi}{4}m_{2}^{(0)}(z), \quad (10) \] 

where we have introduced the generalized Fourier moment profiles

 \[ m_{i}^{(k)}(z)=\frac{2}{1+\delta_{k0}}\int_{0}^{l_{\max}}d l l^{i}\int_{0}^{\pi}d\phi\cos(2k\phi)\rho(l,z,\phi) \quad (11) \] 

with

 \[ k=\left\{\begin{array}{l l}{0}&{\mathrm{i f}i=\{1,2\}}\\ {\{0,1,\cdots,n_{\mathrm{m a x}}\}}&{\mathrm{i f}i=0.}\end{array}\right. \quad (12) \] 

Here,  \( \delta_{kj} \)  is the Kronecker delta. The value  \( n_{max} \)  is chosen to ensure an adequate approximation for the orientational distribution function  \( h(z,\phi) \)  (see below). Note that we only need the moments  \( \{m_{i}^{(0)}\} \)  to define  \( \eta(z) \) . However, at this point, we introduce all the moments required to find the equilibrium density profile,  \( \rho(l,z,\phi) \) , as will be shown later.

The magnitude  \( \langle\langle A_{\mathrm{spt}}\rangle\rangle \)  in Eq. (8) is the double angular average, with respect to the density profiles  \( \rho(l,z,\phi) \)  and  \( \rho(l',z,\phi') \) , of the so-called SPT-area integrated with respect to the polydisperse roundness lengths l and  \( l' \) :

 \[ \begin{align*}\langle\langle A_{\mathrm{spt}}\rangle\rangle(z)\equiv&\int_{0}^{l_{\max}}dl\int_{0}^{l_{\max}}dl^{\prime}\int_{0}^{\pi}d\phi\int_{0}^{\pi}d\phi^{\prime}\rho(l,z,\phi)\\&\times\rho(l^{\prime},z,\phi^{\prime})A_{\mathrm{spt}}(l,l^{\prime},\phi-\phi^{\prime}).\end{align*} \quad (13) \] 

In turn,  \( A_{\mathrm{spt}}(l,l',\phi) \)  can be calculated from the excluded area,  \( A_{\mathrm{exc}}(l,l',\phi) \) , as

 \[ \begin{align*}A_{\mathrm{spt}}(l,l^{\prime},\phi)&=\frac{1}{2}\left[A_{\mathrm{exc1}}(l,l^{\prime},\phi)-a(l)-a(l^{\prime})\right]\\&=\frac{\left(L^{2}+D^{2}\right)}{2}|\sin\phi|+LD|\cos\phi|\\&+\frac{(L+D)}{2}(l+l^{\prime})+\frac{\pi}{4}ll^{\prime}.\end{align*} \quad (14) \] 

The excluded area,  \( A_{\mathrm{exc1}}(l,l',\phi) \) , between two HRRs with roundness lengths l and  \( l' \)  and orientation  \( \phi \)  is the region of space inaccessible to the center of mass of one particle due to the presence of the other particle. Note that here  \( \phi \)  is the relative orientation between both particles.
The Fourier expansion of the SPT-area (14) using the cosine basis functions  \( \{\cos(2k\phi)\}_{k=0}^{n_{\max}} \)  is

 \[ \begin{align*}A_{\mathrm{spt}}(l,l^{\prime},\phi)&=\frac{(L+D)}{2}(l+l^{\prime})+\frac{\pi}{4}ll^{\prime}\\&\quad+\frac{1}{\pi}\left[g_{0}+2\sum_{k=1}^{n_{\max}}g_{k}\cos(2k\phi)\right],\end{align*} \quad (15) \] 

with Fourier coefficients,

 \[ g_{k}=-\frac{\left(L+(-1)^{k}D\right)^{2}}{4k^{2}-1},\quad k=0,\cdots,n_{\max}. \quad (16) \] 

Inserting Eq. (15) into (13) we arrive at

 \[ \begin{align*}\langle\langle A_{\mathrm{spt}}\rangle\rangle(z)&=\frac{1}{\pi}\left[g_{0}\left(m_{0}^{(0)}(z)\right)^{2}+\frac{1}{2}\sum_{k=1}^{n_{\max}}g_{k}\left(m_{0}^{(k)}(z)\right)^{2}\right]\\&+\left(L+D\right)m_{0}^{(0)}(z)m_{1}^{(0)}(z)+\frac{\pi}{4}\left(m_{1}^{(0)}(z)\right)^{2},\end{align*} \quad (17) \] 

where we have used the definitions of the generalized Fourier moment profiles (11).

Equations (8) and (13) constitute a local density functional approximation. For this approximation to accurately take into account short ranged particle correlations, the variation of the integrated density profile,  \( m_{0}^{(0)}(z) \) , along z should be much less than the inverse of the average characteristic length of the interparticle potential,  \( \Lambda \equiv 2(L + l_{0}) \) . Hence, in our case, the relative variation of the density profile along z should be of the order of the gravitational length  \( \langle \xi \rangle \equiv (\tau \langle a \rangle_{f})^{-1} \) . That is,

 \[ \frac{1}{m_{0}^{(0)}(z)}\left|\frac{d m_{0}^{(0)}(z)}{d z}\right|\lesssim\langle\xi\rangle^{-1}. \quad (18) \] 

As  \( \langle\xi\rangle\gg\Lambda \) , we obtain a condition to justify the local density approximation,

 \[ \frac{1}{m_{0}^{(0)}(z)}\left|\frac{d m_{0}^{(0)}(z)}{d z}\right|\ll\Lambda^{-1}. \quad (19) \] 

We have defined

 \[ \langle a\rangle_{f}=L D+(L+D)l_{0}+\frac{\pi}{4}l_{0}^{2}(1+s^{2}) \quad (20) \] 

as the averaged particle area with respect to the parent distribution function  \(  f(l)  \) , while  \(  \tau = \beta (\Delta d) g  \)  is a coefficient defined from the product of  \( \Delta d \equiv d_{m} - d_{s} > 0 \) , the difference between the mass density of the material from which solute particles are made ( \( d_{m} \) ) and that of the solvent ( \( d_{s} \) ), and the constant of gravity g, divided by  \( \beta^{-1} = k_{B} T \) .

The ideal part of the free-energy density in reduced thermal units for the polydisperse mixture is given ex-
 

actly by

 \[ \begin{align*}\Phi_{\mathrm{id}}(z)&\equiv\frac{\beta\mathcal{F}_{\mathrm{id}}[\rho]}{A}\\&=\int_{0}^{l_{\max}}dl\int_{0}^{\pi}d\phi\rho(l,z,\phi)\left[\ln\left(\rho(l,z,\phi)\right)-1\right],\end{align*} \quad (21) \] 

where we have dropped the (irrelevant) particle thermal areas.

Finally, the gravitational field is incorporated as an external potential contribution due to a conservative force field,

 \[ \begin{align*}\Phi_{\mathrm{ext}}(z)&\equiv\frac{\beta\mathcal{F}_{\mathrm{ext}}[\rho]}{A}\\&=\tau z\int_{0}^{l_{\max}}dl\int_{0}^{\pi}d\phi\rho(l,z,\phi)a(l)=\tau z\eta(z).\end{align*} \quad (22) \] 

The total Helmholtz free-energy functional per unit of area in reduced thermal units is

 \[ \Phi[\rho]\equiv\frac{\beta\mathcal{F}[\rho]}{A}=\frac{1}{H}\int_{0}^{H}dz\left[\Phi_{\mathrm{i d}}(z)+\Phi_{\mathrm{e x c}}(z)+\Phi_{\mathrm{e x t}}(z)\right]. \quad (23) \] 

The functional minimization of  \( \Phi[\rho] \)  with respect to  \( \rho(l,z,\phi) \) , taking into account the constraint (2), yields

 \[ \rho(l,z,\phi)=\frac{\rho_{0}f(l)e^{c(l,z,\phi)}}{T(l)}, \quad (24) \] 

 \[ c(l,z,\phi)\equiv c_{1}(l,z,\phi)-\tau a(l)z, \quad (25) \] 

 \[ T(l)\equiv H^{-1}\int_{0}^{H}d z^{\prime}\int_{0}^{\pi}d\phi^{\prime}e^{c(l,z^{\prime},\phi^{\prime})} \quad (26) \] 

where the one-body direct correlation function is

 \[ -c_{1}(l,z,\phi)=-\ln\left[1-\eta(z)\right]+\frac{S(l,z,\phi)}{1-\eta(z)}+p^{*}(z)a(l), \quad (27) \] 

with

 \[ S(l,z,\phi)\equiv2\int_{0}^{l_{\max}}d l^{\prime}\int_{0}^{\pi}d\phi^{\prime}\rho(l^{\prime},z,\phi^{\prime})A_{\mathrm{s p t}}(l,l^{\prime},\phi-\phi^{\prime}), \quad (28) \] 

and

 \[ p^{*}(z)\equiv\frac{m_{0}^{(0)}(z)}{1-\eta(z)}+\frac{\langle\langle A_{\mathrm{s p t}}\rangle\rangle(z)}{(1-\eta(z))^{2}}, \quad (29) \] 

being the local pressure profile in reduced thermal units, i.e.,  \(  p^{*}(z) = \beta p(z)  \) . The function  \(  S(l, z, \phi)  \)  in turn can be expressed as a function of the generalized Fourier moment profiles  \(  \{ m_{k}^{(i)}(z) \}  \)  taking into account the Fourier expansion of  \(  A_{\mathrm{spt}}(l, l', \phi)  \) , given in Eq. (15), resulting in

 \[ \begin{aligned}&S(l,z,\phi)=\frac{2}{\pi}\Biggl[g_{0}m_{0}^{(0)}(z)+\sum_{k=1}^{n_{\max}}g_{k}m_{0}^{(k)}(z)\cos(2k\phi)\Biggr]\\&+(L+D)m_{1}^{(0)}(z)+\left[(L+D)m_{0}^{(0)}(z)+\frac{\pi}{2}m_{1}^{(0)}(z)\right]l.\\ \end{aligned} \quad (30) \] 

Using the result (24) and the definitions (11), we obtain the following set of self-consistent nonlinear integral equations for the unknown functions  \( \{m_{i}^{(k)}(z)\} \) :

 \[ m_{i}^{(k)}(z)=\frac{2\rho_{0}}{1+\delta_{k0}}\int_{0}^{l_{\max}}d l l^{i}\frac{f(l)}{T(l)}\int_{0}^{\pi}d\phi\cos(2k\phi)e^{c(l,z,\phi)}. \quad (31) \] 

This system of nonlinear equations allows us to find the  \( n_{\max}+3 \)  unknown generalized moment profiles  \( \{m_{i}^{(k)}(z)\} \) ; three  \( m_{i}^{(0)}(z) \)  corresponding to i=0,1,2 and a total number of  \( n_{\max} \)  moment profiles  \( m_{0}^{(k)}(z) \)  for  \( 1 \leq k \leq n_{\max} \) . Here, we set  \( n_{\max}=20 \) .

The system of equations is solved iteratively, after uniform discretization of the spatial coordinate, using Anderson's acceleration method [54] with memory length M = 3, by gradually increasing the mixing parameter from  \( 10^{-8} \)  to  \( 1024 \times 10^{-7} \) . The iterations stop when the residual (quadratic mean) is less than  \( 10^{-6} \) . To perform the integrals over  \( \phi \)  we use the Gauss-Legendre quadrature with either 81 or 101 sample points in the interval  \( [0, \pi] \) . We perform the integration over z using the Simpson's rule with  \( n_{p} = \max([450\tau] + 1, 41) \)  uniformly distributed points, where  \( [\cdot] \)  denotes the ceiling function.

The procedure to obtain the equilibrium density profile of a given sample is as follows. First, we fix the average packing fraction, the sample height, and the parent distribution function. Next, we initialize the generalized moment functions  \( \{m_{i}^{(k)}(z)\} \)  with certain guesses depending on the bulk phases that we want to include along the column as possible candidates to the equilibrium profiles (see Sec. IV). Then, we iteratively solve the system (31) to find the final equilibrium profile  \( \rho_{\mathrm{eq}}(l,z,\phi) \) , which is a function of the set of equilibrium generalized moment functions. In some cases different initial guesses result in different converged profiles. To distinguish which of them is the equilibrium one, we compute the free energy for all converged profiles and choose the one with the lowest free energy. It is straightforward to show from Eqs. (23), (24), and (31) that the free energy at equilibrium is given by

 \[ \begin{align*}\Phi[\rho_{\mathrm{eq}}]&=\rho_{0}\left(\ln\rho_{0}+\int_{0}^{l_{\max}}dl f(l)\ln\left[\frac{f(l)}{T_{\mathrm{eq}}(l)}\right]\right)\\&\quad-\frac{1}{H}\int_{0}^{H}dz p_{\mathrm{eq}}^{*}(z).\end{align*} \quad (32) \] 

To end this section, we briefly remind the concepts of cloud and shadow coexisting phases at bulk. These concepts will be used later when we compare the equilibrium sedimented phases obtained from the present model with those obtained at bulk conditions. With cloud-A-shadow-B coexistence we mean that the whole sample filled by phase A (the cloud phase) coexists with an infinitesimally thin layer of phase B (the shadow phase).
 

## IV. SAMPLE CHARACTERIZATION

To describe the particle shape, we use both the mean aspect ratio,  \( \kappa_{0} \) , and the roundness parameter,  \( \theta \) , defined as

 \[ \kappa_{0}=\frac{L+l_{0}}{D+l_{0}}, \quad (33) \] 

 \[ \theta=\frac{l_{0}}{D+l_{0}}. \quad (34) \] 

The roundness parameter lies in the interval  \( [0,1] \)  with  \( \theta\to0 \)  being the limit of a rectangle  \( (l_{0}\ll D) \) , and  \( \theta\to1 \)  being the limit of a discreteangle  \( (l_{0}\gg D) \) .

Further, we define the scaled mean density  \( \bar{\eta} \equiv \rho_{0} \langle a \rangle_{f} \)  or mean packing fraction (with respect to the parent distribution function) and the dimensionless density profile  \( \rho^{*}(z) \equiv m_{0}^{(0)}(z) \langle a \rangle_{f} \) .

To measure the degree of fractionation in the polydisperse roundness as a function of the elevation z, we define the distribution function  \( x(l,z) \)  as the fraction of particles with roundness l located in an infinitesimally thin slab at position z:

 \[ \begin{align*}x(l,z)\equiv&\frac{\int_{0}^{\pi}d\phi\rho(l,z,\phi)}{\int_{0}^{l_{\max}}dl^{\prime}\int_{0}^{\pi}d\phi^{\prime}\rho(l^{\prime},z,\phi^{\prime})}\\=&\frac{1}{m_{0}^{(0)}(z)}\int_{0}^{\pi}d\phi\rho(l,z,\phi).\end{align*} \quad (35) \] 

The distribution function  \( x(l,z) \)  is normalized for all positions,

 \[ \int_{0}^{l_{\max}}d l x(l,z)=1,\forall z. \quad (36) \] 

Then, we can compute the scaled average roundness (in units of  \( l_{0} \) ),

 \[ \sigma_{1}(z)\equiv\langle l\rangle_{x}(z)/l_{0}, \quad (37) \] 

and its mean square value

 \[ \sigma_{2}(z)\equiv\langle l^{2}\rangle_{x}(z)/l_{0}^{2}, \quad (38) \] 

as a function of the vertical coordinate z. We define the moments of l with respect to the distribution function  \( x(l,z) \)  as

 \[ \langle l^{i}\rangle_{x}(z)\equiv\int_{0}^{l_{\max}}d l l^{i}x(l,z)=\frac{m_{i}^{(0)}(z)}{m_{0}^{(0)}(z)},\quad i=1,2, \quad (39) \] 

with the last equality obtained from (11). Both  \( \sigma_{1} \)  and  \( \sigma_{2} \)  help to characterize the mean roundness of particles populating the fluid slab at elevation z together with the degree of fluid polydispersity at this position.

We also use the maximum value of the distribution function  \( x(l,z) \)  as a function of l for a fixed z,  \( \mathcal{M}(z) \equiv \max_{l} [x(l,z)] \) , to quantify the shape of  \( x(l,z) \)  at each position z.
To find the stacking sequences [41] of the liquid crystal fluid column, it is necessary to describe the orientational symmetries of the different sedimented phases. First, we define the orientational distribution function of the polydisperse fluid at the position z as

 \[ h(z,\phi)\equiv\frac{\int_{0}^{l_{\max}}d l\rho(l,z,\phi)}{\int_{0}^{\pi}d\phi^{\prime}\int_{0}^{l_{\max}}d l^{\prime}\rho(l^{\prime},z,\phi^{\prime})}, \quad (40) \] 

which is normalized for all positions:

 \[ \int_{0}^{\pi}d\phi h(z,\phi)=1,\forall z. \quad (41) \] 

Next, we define the orientational order parameters, measuring the degree of nematic (\(n=2\)) or tetratic (\(n=4\)) order, as cosines-weighted angular moments of the orientational distribution function

 \[ Q_{2n}(z)=\int_{0}^{\pi}d\phi h(z,\phi)\cos(2n\phi)=\frac{m_{0}^{(n)}(z)}{2m_{0}^{(0)}(z)},\quad n=1,2. \quad (42) \] 

With the orientational order parameters, we classify the state of the sedimented sample at position z according to the following rule:

• Isotropic phase:  \( Q_{2}(z) = Q_{4}(z) = 0 \) ,

• Tetratic phase:  \( Q_{2}(z) = 0 \) ,  \( Q_{4}(z) > 0 \) .

• Nematic phase:  \( Q_{2}(z) > 0 \) ,  \( Q_{4}(z) > 0 \) .

## V. RESULTS

## A. Sedimentation profiles

We begin by analyzing three sedimentation profiles, each corresponding to a distinct set of model parameters selected to illustrate representative behaviours of the system. Across all three cases, the following parameters are held constant: mean aspect ratio (33)  \( \kappa_{0}=1.75 \) , polydispersity coefficient (6) s=0.936 (corresponding to  \( \nu=0 \)  with the parent distribution function shown in Fig. 1), and mean roundness (34)  \( \theta=0.3 \) . To generate the different profiles, we vary the capillary height H and the mean packing fraction  \( \bar{\eta} \) , allowing us to explore the influence of these parameters on the sedimentation behaviour.

Figure 2 displays the profiles along the sedimentation direction of the capillary for the three selected cases. The first case corresponds to a sample height  \( H/\langle\xi\rangle = 105 \)  and the highest scaled mean density,  \( \bar{\eta} = 0.913 \) . In this case, the profiles of the orientational order parameters, Fig. 2(b1), reveal that in the top region,  \( Q_{2} = 0 \)  and  \( Q_{4} \neq 0 \) , while in the bottom region both  \( Q_{2} \neq 0 \)  and  \( Q_{4} \neq 0 \) . Hence, the stacking sequence is TN (tetratic-nematic), where we denote the stacks of different bulk phases from top to bottom.
 
![](2511.07034v1-images/6_0.jpg)

![](2511.07034v1-images/6_1.jpg)

![](2511.07034v1-images/6_2.jpg)

![](2511.07034v1-images/6_3.jpg)

![](2511.07034v1-images/6_4.jpg)

![](2511.07034v1-images/6_5.jpg)

FIG. 2. Sedimentation profiles. (a1) Scaled density  \( \rho^{*} \)  and local packing fraction  \( \eta \)  as a function of elevation z for a sample with mean packing fraction  \( \overline{\eta}=0.913 \)  and sample height  \( H/\langle\xi\rangle=105 \) , corresponding to a TN stacking sequence. The mean aspect ratio is  \( \kappa_{0}=1.75 \) , the polydispersity coefficient is s=0.936, and the mean roundness is  \( \theta=0.3 \) . (b1) Order parameters  \( Q_{2} \)  and  \( Q_{4} \)  as a function of elevation for the same sample as in (a1). (c1) Profiles for the first and second dimensionless moments  \( \sigma_{1} \) ,  \( \sigma_{2} \) , and maximum value M of  \( x(l,z) \)  with respect to l as a function of z, for the same sample as in (a1). A sketch of the sample highlighting the stacking sequence is shown in panel (c1). (d1) Local roundness distribution functions  \( x(l,z) \)  as a function of l at three selected elevations z, marked in panels (c1) with arrows. Panels (a2) to (d2) display the same quantities as panels (a1) to (d1) for a sample with height  \( H/\langle\xi\rangle=105 \)  and mean packing fraction  \( \overline{\eta}=0.908 \) , which corresponds to an ITNT stacking sequence. Panels (a3) to (d3) display the same quantities as panels (a1) to (d1) for a sample with height  \( H/\langle\xi\rangle=30.8 \)  and mean packing fraction  \( \overline{\eta}=0.91 \) , which corresponds to a NT stacking sequence. Figure 3(d), shows the location of the three samples in the stacking diagram using pentagons labeled 1 to 3.
 

This sequence is consistent with the behaviour expected in bulk systems with low polydispersity. In the central region of the capillary, the stable phase is the uniaxial nematic (N), although the uniaxial order parameter  \( Q_{2} \)  decreases towards both the top and bottom boundaries. This trend can be understood by considering the density and packing fraction profiles shown in Fig. 2(a1), which indicates that the particle number density increases towards the top, opposite to the trend of the packing fraction. This apparent contradiction arises due to gravity-driven sedimentation: heavier particles tend to settle lower in the capillary. These heavier particles typically have higher roundness values l, and the aspect ratio  \( \kappa(l) \)  is a monotonically decreasing function of l:

 \[ \kappa(l)=\frac{L+l}{D+l}, \quad (43) \] 

which implies that particles with greater roundness possess lower aspect ratios and are in turn more massive as Eq. (1) for the particle area shows. Since lower aspect ratios are associated with reduced uniaxial nematic order  \( Q_{2} \) , the decrease in  \( Q_{2} \)  towards the bottom is consistent with the presence of rounder, less anisotropic particles. In contrast, the local packing fraction at the top is sufficiently reduced so as to stabilize the less ordered liquid-crystal T phase. Figure 2(c1) shows the first,  \( \sigma_{1} \) , and second,  \( \sigma_{2} \) , moments of the polydispersity distribution. Both quantities increase towards the bottom of the capillary as a result of gravity-induced fractionation. Near the bottom, this pronounced fractionation causes the peak of the roundness distribution to shift from l = 0 to significantly larger values, see Fig. 2(d1). That is, gravity induces a qualitative change in the shape of the local distribution of particles.

The stacking sequence shown in Fig. 2 panels (a2) to (d2) corresponds to the same value of sample height,  \( H/\langle\xi\rangle = 105 \) , but the scaled mean density is decreased to  \( \bar{\eta} = 0.908 \) . This small decrease is however sufficient to stabilise an isotropic stack at the top and a tetratic stack at the bottom, leading to a four stack ITNT sequence. The bottom tetratic stack appears again as a result of the accumulation of more rounded (heavier) particles toward the bottom of the sample.

Finally, in Fig. 2 panels (a3) to (d3) we show that by reducing the capillary height to  \( H/\langle\xi\rangle = 30.8 \)  and for an average packing fraction  \( \overline{\eta} = 0.91 \) , the nematic phase no longer has sufficient vertical space to establish an interface with either a tetratic or an isotropic phase at the top. Instead, a nematic-tetratic (NT) stacking sequence emerges. This is an inversion of the stacking sequence with respect to the TN sequence shown in Fig. 2 panels (a1) to (d1). Similarly, the cloud-N-shadow-T and shadow-N-cloud-T coexist in bulk at approximately the same polydispersity [52]. However, the inversion of the stacking sequence is much stronger under sedimentation conditions as compared to the bulk. Other phase inversion phenomena are present in the system, as discussed below. A conceptually similar inversion of the stacking sequence (between isotropic-nematic and nematic-isotropic) was experimentally observed by van der Kooij et al. in polydisperse platelets [40].

In contrast to the previous cases, the peak of the distribution function remains fixed at l = 0 throughout the whole vertical column, see Fig. 2(d3).

## B. Phase stacking diagrams

We next group all possible stacking sequences for a given parent distribution in a stacking diagram, see Fig. 3. We construct the stacking diagram by computing sedimentation profiles for each point on a rectangular grid in the plane defined by the average packing fraction  \( \overline{\eta} \)  and the sample height H. The phase of each horizontal stack is then identified using the orientational order parameters  \( Q_{2}(z) \)  and  \( Q_{4}(z) \) . The grid size is chosen according to the complexity of the diagram. A finer grid is used when the number and symmetries of the involved stacking sequences is rather sensitive to small changes in  \( \overline{\eta} \)  and/or  \( H/\langle\xi\rangle \) . Each point in the stacking diagram corresponds to a sedimented sample with a given stacking sequence. As mentioned above, we label the stacking sequences from top to bottom. Hence, the stacking sequence INT means that the stacks I, N and T are observed from the top towards the bottom along the vertical direction. Three schematic examples of biphasic (1 and 2) and triphasic (3) stacking sequences are represented next to panel (b) of Fig. 3. These particular samples are indicated in the corresponding stacking diagrams shown in Fig. 3(a) and Fig. 3(b).

Four stacking diagrams are shown in Fig. 3 in the  \( \overline{\eta} \) -H/ \( \langle\xi\rangle \)  plane, where again  \( \langle\xi\rangle = (\tau\langle a\rangle)^{-1} \)  is the average gravitational length. First, we study HRR systems with an average aspect ratio  \( \kappa_{0} = 2.22 \)  (for which the tetratic phase T is not stable in bulk [52]) under gravity, see Fig. 3(a) and Fig. 3(b). For a moderate degree of polydispersity, s = 0.50 (corresponding to the parent distribution function shown in Fig. 1), and  \( \theta = 0.556 \) , we only find the stacking sequence IN (sketched sequence 1) in addition to the pure I and N stacks, see Fig. 3(a). For this parent distribution, the I-N transition is of first order in bulk and there is no phase inversion with respect to packing fraction [52]. Therefore, the stacking sequences found correspond to those expected for a bulk first-order transition. For example, for  \( H/\langle\xi\rangle \approx 50 \)  and mean packing fractions between 0.85 and 0.9, we observe the expected cascade of stacking sequences  \( I \rightarrow IN \rightarrow N \) . The region occupied by the sequence IN in the stacking diagram will presumably keep growing as we increase the sample height. In the limit of very large samples, the IN should develop at essentially any value of the average packing fraction. The parent distribution contains only particles with positive buoyant masses and therefore in the limit  \( H/\langle\xi\rangle \rightarrow \infty \)  the top stack must always be a dilute isotropic phase. We expect that the stacking sequence IN
 

is still present in the bulk limit, i.e.,  \( H/\langle\xi\rangle \rightarrow 0 \) , with the corresponding density gap at coexistence. For this parent distribution the most ordered bulk phase (N) appears at the bottom. No inversion of the stacking sequence is present.

Using the same values for  \( \kappa_{0} \)  and  \( \theta \) , but increasing the polydispersity to  \( s \rightarrow 1 \) , we observe that no inversion in packing fraction occurs in bulk [52]. Specifically, at the cloud-I-shadow-N coexistence, the packing fraction of the isotropic phase (I) is lower than that of the nematic phase (N). For the cloud-N-shadow-I coexistence, both packing fractions are approximately equal. However, the situation changes in presence of the gravitational field, see Fig. 3(b). When the polydispersity increases to s = 0.936, a phase inversion in the local packing fraction emerges: the conventional IN stacking sequence disappears (within the resolution of our sampling grid and also for the range of samples heights and packing fractions considered), and new sequences, NI and INI, are stabilized, see the sketched sequences 2 and 3 in Fig. 3(b). The sequence INI, i.e., a nematic stack floating between two isotropic stacks, has been experimentally observed in plate-rod binary colloidal mixtures [36] and theoretically studied with sedimentation path theory [36, 48].

Although the NI sequence is present at all sample heights considered here, it will disappear above a certain height because in the limit  \( H/\langle\xi\rangle \rightarrow \infty \)  a dilute isotropic must develop on top (note that all buoyant masses are positive). The triphasic INI sequence occurs only for sample heights above  \( H/\langle\xi\rangle \gtrsim 35 \) . Hence, at a fixed sample height  \( H/\langle\xi\rangle = 60 \)  and increasing the mean packing fractions in the range  \( 0.86 \leq \overline{\eta} \leq 0.9 \) , we observe the cascade  \( I \rightarrow INI \rightarrow NI \rightarrow N \) .

In the triphasic INI configuration, the more disordered I phase resides at the bottom, followed by an intermediate N layer, and then another I layer at the top, similar to the INI sequence found in sphere-plates binary mixtures  \( [36, 48] \) . There, the bottom (top) isotropic stack is rich in the heavier spheres (lighter plates). Here, both isotropic stacks are occupied by HRRs that differ on their relative roundness size. The INI sequence found here provides another direct evidence of a genuine phase inversion induced by the coupling between polydispersity and gravity, an effect that is absent in the bulk phase diagram for the same parameters  \( [52] \) . Note also that no evidence of three-phase coexistence is present in bulk, highlighting the role of the gravitational field in the emergence of these complex stacking sequences. The stabilization of the INI sequence requires a finite sample height  \( (H/\langle\xi\rangle \neq 0) \)  which clearly distinguishes this phenomenon from bulk behavior.

In summary, even when only two stable bulk phases, I and N, do exist, we observe a clear inversion in the stacking sequence (from IN to NI) and the emergence of a reentrant I stack within the INI sequence as the degree of polydispersity s increases.

We next reduce the average aspect ratio to  \( \kappa_{0}=1.75 \) , with the goal of introducing a new stable phase in bulk: the tetratic phase (T). Under these conditions, we analyze a system with three stable bulk phases, namely the isotropic (I), tetratic (T), and nematic (N), using a roundness parameter  \( \theta=0.3 \)  and a moderate degree of polydispersity, s=0.50. In bulk, the I-T transition is of second order, while the T-N transition is of first order. No packing fraction inversion phenomena are observed in bulk [52].

In the sedimented system, see Fig. 3(c), alongside pure I, T, and N stacking sequences, a rich variety of biphasic stacking sequences, IT and TN, as well as a triphasic stacking, ITN, are stabilized. However, no inversion of the stacking sequence is present. The most ordered stack appears always at the bottom. The transitions between stacking sequences can be quite intricate: for example, at  \( H/\langle\xi\rangle \approx 80 \) , we observe the cascade  \( I \rightarrow IT \rightarrow ITN \rightarrow TN \rightarrow N \)  as  \( \eta \)  increases over a relatively narrow interval  \( (0.88 \lesssim \overline{\eta} \lesssim 0.93) \) . Notably, the ITN stacking sequence disappears if the sample height is smaller than  \( H/\langle\xi\rangle \approx 20 \) , indicating that the corresponding I-T-N three-phase coexistence does not occur in bulk. We anticipate that the region corresponding to the ITN sequence in the stacking diagram will continue to expand as the sample height increases.

For a higher degree of polydispersity, s = 0.936, an even wider variety of stacking sequences emerges, including IT, TI, ITI, TN, NT, TNT, and ITNT, see Fig. 3(d). It is interesting to note that inverted sequences such as IT and TI can appear at the same average packing fraction  \( (0.902 \leq \overline{\eta} \leq 0.904) \)  but for different sample heights. Similarly, an inversion from TN to NT is also observed at  \( \overline{\eta} \sim 0.912 \) : the TN sequence appears in taller samples  \( (H/\langle\xi\rangle \sim 100) \) , while the NT sequence is found in shorter samples  \( (H/\langle\xi\rangle \sim 60) \) . The samples shown in figure 2 panels (a1-c1) and (a3-c3) are illustrative examples of this inversion. Two inverted sequences do not share a common boundary in the stacking diagram. For example, transforming the sequence TN into NT (e.g., by increasing the sample height at constant packing fraction) requires passing through the intermediate region TNT in the stacking diagram.

The topology of the phase stacking diagram is rather complex. For example, if we fix  \( H/\langle\xi\rangle = 100 \)  and vary  \( \overline{\eta} \in [0.89, 0.92] \) , then up to 7 stacking sequences appear as  \( \overline{\eta} \)  increases:  \( I \rightarrow ITI \rightarrow IT \rightarrow ITNT \rightarrow TNT \rightarrow TN \rightarrow N \) , with one of them including up to four stacks of different bulk phases along the column. Also, if we fix the average packing fraction at  \( \overline{\eta} \approx 0.906 \)  and increase the sample height within the interval  \( H/\langle\xi\rangle \in [0, 160] \)  we find the stacking sequences  \( I \rightarrow T \rightarrow TI \rightarrow ITI \rightarrow IT \rightarrow ITNT \) . These examples illustrate the challenges in inferring bulk phase equilibria from a collection of sedimented samples.

To better visualize the stacking sequences that appear in a narrow range of  \( \overline{\eta} \) , we have included two insets in Fig. 3(d). The first inset focuses on relatively large values of the sample height (including the discussed case of  \( H/\langle\xi\rangle = 100 \) ), while the second inset considers short samples with H values up to  \( 40\langle\xi\rangle \) . In the latter case,
 

setting  \( H/\langle\xi\rangle\approx30 \) , we again observe a cascade of up to seven different stacking sequences: I  \( \rightarrow \)  ITI  \( \rightarrow \)  TI  \( \rightarrow \)  T  \( \rightarrow \)  TNT  \( \rightarrow \)  NT  \( \rightarrow \)  N (when  \( \overline{\eta} \)  varies between 0.9 and 0.915). An inversion in the local packing fraction is observed, with a T stack (having less orientational order than phase N) occupying to the bottom (in the case of the TNT or the NT sequence), and also an I stack (without orientational order) appearing at lower height than the T stack in the ITI sequence, where the phase I also reappears at the top of the column as a reentrant stack.

Two three-phase sequences (ITI and TNT) appear under sedimentation conditions but are absent in bulk  \( (H/\langle\xi\rangle\rightarrow0) \) . As we previously described, the local inversion in the packing fraction occurs because the more disordered phases are richer in particles with smaller aspect ratios and consequently more rounded, which in turn implies a greater area and hence more gravitational attraction, making them sink to the bottom. The reentrant top isotropic (tetratic) stack in the INI (TNT) sequence occurs due to reduced number of particles in the upper portion of the column. As density decreases, orientational order declines because interparticle interactions become less prominent.

In the large-sample limit, multiple scenarios are plausible. There, the stacking sequences must develop a top isotropic stack followed by tetratic and nematic stacks. However, due to the occurrence of local phase inversion, the sequences ITNT and even ITNTI (not observed in the range of heights considered here) could be present and possibly dominate the stacking diagram at large-sample heights.

## VI. CONCLUSIONS

We have investigated the sedimentation behavior of a polydisperse two-dimensional liquid-crystal model using a local density-functional theory. This is the first consistent treatment of the intricate interplay between polydispersity, phase equilibria, and gravity in liquid-crystal fluids. Given the inherent complexity of the problem, we have employed a simplified particle model, rounded hard rectangles, in our theoretical framework. Nevertheless, the same theoretical framework can be used to study other types of interaction potentials. We argue that this minimal model is sufficient to capture qualitatively correct features, particularly in high columns composed of phases that are uniform in bulk. Note, however, that our local density approximation assumes that the walls do not affect the properties of the fluid inside the capillary. Surface effects such as wetting, anchoring, and layering will modify the free-energy landscape and enrich the phenomena observed here. Also, situations where the local-density approximation may not be accurate include the occurrence of stacks with positionally ordered phases (see below), and stacking sequences where the thickness of the stacks is of the same order of magnitude as the thickness of the interfaces that separate the corresponding stacks. In these cases a nonlocal version of the theory would be necessary to quantitatively describe the sedimentation profiles. In the stacking diagram, such sequences with narrow stacks occur near the boundaries between two stacking sequences. However, we expect that the local approximation will qualitatively capture the stacking sequences and the topology of the stacking diagram.

Despite the simplicity of the model, our analysis reveals a remarkably rich variety of stacking sequences, far exceeding the structural diversity observed in bulk. These include inverted sequences, reentrant stacks, multiphasic stacking sequences with up to four stacks, and cascades of transitions between different stacking sequences occurring by either varying the packing fraction while keeping the sample height constant or varying the height at constant average packing fraction. All of these phenomena arise from the coupling between particle polydispersity and the gravitational field.

In the present study we have used exponentially decaying parent distribution functions. In principle other distributions with an exponential or more rapidly decaying functional forms will produce qualitatively similar results. The case is different when the distribution has a fat tail such as in log-normal or power-like distributions. For instance, in length-polydisperse rods, the more ordered nematic phase is enriched in particles of very large size, making the order of the phase transitions and fractionation effects much stronger  \( [64] \) . For our HRR model, we expect fat tails to enrich the I and T phases with particles of very large roundness.

Our two-dimensional model should also accurately represent the sedimentation behavior in tilted monolayers  \( [55] \)  of polydisperse colloidal particles. Also, new experiments on tilted vibrated monolayers of granular rods can be designed to study the effect of gravity on the sedimentation behavior of granular particles. Moreover, our approach, based on projecting the infinite-dimensional thermodynamic space of the polydisperse system onto a finite set of density moments, is computationally efficient, and readily extendable to three-dimensional colloidal systems. Hence, it is a promising tool for studying more realistic systems where the coupling between gravity and polydispersity is significant. Comparison with already available experimental data  \( [38–40] \)  should then be possible. Our theoretical framework has potential applications ranging from better understanding the sedimentation of natural suspensions such as clay, which is crucial for erosion prediction, to optimizing the fabrication of colloidal inks where controlled particle settling prevents clogging, and modeling the sedimentation of biofluids which could improve diagnostics accuracy.

An interesting line of research for future works is to study the effect of continuous particle length polydispersity on the stacking diagrams of colloidal suspensions with stable non-uniform bulk phases, such as smectic, columnar, and crystalline phases. Non-local density functionals, such as those based on the fundamental measure theory  \( [56–60] \) , are then required to accurately describe
 
![](2511.07034v1-images/10_0.jpg)

![](2511.07034v1-images/10_1.jpg)

![](2511.07034v1-images/10_2.jpg)

FIG. 3. Stacking diagrams of polydisperse hard rounded rectangles in the plane of average packing fraction  \( \overline{\eta} \)  and scaled sample height  \( H/\langle\xi\rangle \) . The aspect ratio and average roundness of the parent (bulk) distributions are: (a,b)  \( \kappa_{0}=2.22 \) ,  \( \theta=0.56 \)  and (c,d)  \( \kappa_{0}=1.75 \) ,  \( \theta=0.3 \) . Two degrees of polydispersity are considered in each case: s=0.5 (a,c) and s=0.936 (b,d), as indicated above panels (a,b). Each gray square corresponds to a sedimentation sample that we calculated to obtain the stacking diagrams. The black solid lines mark the approximate boundaries between two different stacking sequences in the stacking diagrams. Stacking sequences are labeled from top to bottom and colored differently (see color box). Close-up views of two highlighted regions in panel (d) are shown in the two side panels. The numbered black circles in (a,b) mark the position of the three sedimentation samples sketched to the right of panel (b). The labeled pentagons in (d) and white squares mark the position in the stacking diagram of the three sedimentation samples depicted in Fig. 2. Minimization of the functional was not possible in the white region of panel (d) due to numerical instabilities.

the bulk. A full minimization of the free energy of the inhomogeneous system, as we have done in this work, would fully incorporate the effect of the gravitational field. The frozen or discrete [11, 61] orientation approximations can alleviate the high computational cost required for the numerical implementation of non-local density functionals. Still, accurately describing non-homogeneous bulk phases requires a computational grid with sub-particle resolution. Hence, the minimization of a polydisperse non-local density functional in presence of gravity can only be done for relatively small systems [51, 62, 63], with a maximum height of a few hundred particle sizes. This limits the ability to compare with standard sedimentation experiments in which the sample height is often thousands and even millions of times larger than the particle size.

An extension of equilibrium [65] and non-equilibrium [66] neural functionals to polydisperse systems could help address this issue, and also open the door to accurately describe the dynamics of sedimentation in polydisperse fluids. Another promising possibility to overcome this limitation is to extend sedimentation path theory [35, 41, 42] from mass-polydisperse [50] to
 

fully polydisperse systems. A sedimented sample would then be discretised using a relatively small number of horizontal slabs. Each slab would be approximated by a bulk system with the same local particle distribution as that in the slab. An iterative procedure, conceptually similar to that done for mass-polydisperse systems  \( [50] \) , could be used to find the mapping between the bulk and the set of horizontal slabs via a height-dependent distribution of local chemical potentials. Sedimentation path theory assumes that each slab is equivalent to an equilibrium system (in contrast to the approach presented here) but it allows the study of arbitrarily large samples. In addition, this local equilibrium approximation is usually accurate in colloidal systems. A further advantage of sedimentation path theory is that it incorporates the effect of the gravitational field using only the bulk equation of state, regardless of its origin. Hence, it might be possible to accurately describe the bulk of the polydisperse system combining computer

[1] G. Lagaly, Handbook of Clay Science (Elsevier, 2006) p. 141.

[2] R. P. Murphy, K. Hong, and N. J. Wagner, Synthetic control of the size, shape, and polydispersity of anisotropic silica colloids, J. Colloid Interface Sci. 501, 45 (2017).

[3] J.-H. Kim, H. J. Hwang, J. S. Oh, S. Sacanna, and G.-R. Yi, Monodisperse magnetic silica hexapods, J. Am. Chem. Soc. 140, 9230 (2018).

[4] J. Roller, J. D. Geiger, M. Voggenreiter, J.-M. Meijer, and A. Zumbusch, Formation of nematic order in 3d systems of hard colloidal ellipsoids, Soft Matter 16, 1021 (2020).

[5] M. Voggenreiter, J. Roller, J. Geiger, L. Ebner, A. Zumbusch, and J.-M. Meijer, Preparation and tracking of oblate core-shell polymethyl-methacrylate ellipsoids, Langmuir 36, 13087 (2020).

[6] J. C. de la Vega, P. Elischer, T. Schneider, and U. O. Häfeli, Uniform polymer microspheres: Monodispersity criteria, methods of formation and applications, Nanomed. 8, 265 (2013).

[7] B. N. Klibetsov and A. M. Burov, Synthesis of monodisperse silica particles by controlled regrowth, Colloid J. 85, 456 (2023).

[8] H. N. W. Lekkerkerker and G. J. Vroege, Liquid crystal phase transitions in suspensions of mineral colloids: new life from old roots, Philos. Trans. R. Soc. A. 371, 20120263 (2013).

[9] H. Almohammadi, S. A. Khadem, P. Azzari, Y. Yuan, A. Guerra, A. D. Rey, and R. Mezzenga, Liquid-liquid crystalline phase separation of filamentous colloids and semiflexible polymers: experiments, theory and simulations, Rep. Prog. Phys. 88, 036601 (2025).

[10] P. Sollich, Predicting phase equilibria in polydisperse systems, J. Phys.: Condens. Matter 14, R79 (2001).

[11] Y. Martínez-Ratón and J. A. Cuesta, Enhancement by polydispersity of the biaxial nematic phase in a mixture of hard rods and plates, Phys. Rev. Lett. 89, 185701 (2002).

[12] C. A. De Filippo, S. Del Galdo, P. Corsi, C. De Michele,

simulation data and deep learning [67]. Moreover, sedimentation path theory would straightforwardly describe sedimentation in systems with stable non-uniform bulk phases, provided that the underlying theory used to describe the bulk of the polydisperse system correctly accounts for such phases.

## ACKNOWLEDGMENTS

EV and YMR acknowledge financial support from Grants PID2023-148633NB-I00/AEI and PID2021-126307NB-C21/MICIU/AEI/10.13039/501100011033/FEDER, UE respectively. DdlH acknowledges support through the Heisenberg program of the Deutsche Forschungsgemeinschaft (DFG) under project number 550390029.

and B. Capone, On the role of polydispersity on the phase diagram of colloidal rods, Soft Matter 19, 1732 (2023).

[13] Y. Martínez-Ratón and E. Velasco, Effect of polydispersity, bimodality, and aspect ratio on the phase behavior of colloidal platelet suspensions, J. Chem. Phys. 137, 134906 (2012).

[14] E. Velasco and Y. Martínez-Ratón, Interplay between columnar and smectic stability in suspensions of polydisperse colloidal platelets, Phys. Chem. Chem. Phys. 16, 765 (2014).

[15] A. Díaz-De Armas and Y. Martínez-Ratón, Role of length polydispersity in the phase behavior of freely rotating hard-rectangle fluids, Phys. Rev. E 95, 052702 (2017).

[16] D. V. Byelov, M. C. D. Mourad, I. Snigireva, A. Snigirev, A. V. Petukhov, and H. N. W. Lekkerkerker, Experimental observation of fractionated crystallization in polydisperse platelet colloids, Langmuir 26, 6898 (2010).

[17] P. Pusey, The effect of polydispersity on the crystallization of hard spherical colloids, J. Phys. 48, 709 (1987).

[18] D. A. Kofke and P. G. Bolhuis, Freezing of polydisperse hard spheres, Phys. Rev. E 59, 618 (1999).

[19] S. Auer and D. Frenkel, Suppression of crystal nucleation in polydisperse colloids due to increase of the surface free energy, Nature 413, 711 (2001).

[20] M. A. Bates and D. Frenkel, Influence of polydispersity on the phase behavior of colloidal liquid crystals: A monte carlo simulation study, J. Chem. Phys. 109, 6193 (1998).

[21] A. Kuijk, D. V. Byelov, A. V. Petukhov, A. van Blaaderen, and A. Imhof, Phase behavior of colloidal silica rods, Faraday Discuss. 159, 181 (2012).

[22] A. V. Petukhov, D. van der Beek, R. P. A. Dullens, I. P. Dolbnya, G. J. Vroege, and H. N. W. Lekkerkerker, Observation of a hexatic columnar liquid crystal of polydisperse colloidal disks, Phys. Rev. Lett. 95, 077801 (2005).

[23] D. Sun, H.-J. Sue, Z. Cheng, Y. Martínez-Ratón, and E. Velasco, Stable smectic phase in suspensions of polydisperse colloidal platelets with identical thickness, Phys. Rev. E 80, 041704 (2009).
 

[24] R. Kotni, A. Grau-Carbonell, M. Chiappini, M. Dijkstra, and A. van Blaaderen, Splay-bend nematic phases of bent colloidal silica rods induced by polydispersity, Nat. Commun. 13, 7264 (2022).

[25] T. Biben, J.-P. Hansen, and J.-L. Barrat, Density profiles of concentrated colloidal suspensions in sedimentation equilibrium, J. Chem. Phys. 98, 7330 (1993).

[26] R. Piazza, T. Bellini, and V. Degiorgio, Equilibrium sedimentation profiles of screened charged colloids: A test of the hard-sphere equation of state, Phys. Rev. Lett. 71, 4267 (1993).

[27] D. van der Beek, T. Schilling, and H. N. W. Lekkerkerker, Gravity-induced liquid crystal phase transitions of colloidal platelets, J. Chem. Phys. 121, 5423 (2004).

[28] S. V. Savenko and M. Dijkstra, Sedimentation and multiphase equilibria in suspensions of colloidal hard rods, Phys. Rev. E 70, 051401 (2004).

[29] T. Eckert, M. Schmidt, and D. de las Heras, Effect of sample height and particle elongation in the sedimentation of colloidal rods, Soft Matter 19, 2214 (2023).

[30] F. M. van der Kooij and H. N. W. Lekkerkerker, Liquid-crystalline phase behavior of a colloidal rod-plate mixture, Phys. Rev. Lett. 84, 781 (2000).

[31] F. M. van der Kooij and H. N. W. Lekkerkerker, Liquid-crystal phases formed in mixed suspensions of rod- and plateletlike colloids, Langmuir 16, 10144 (2000).

[32] L. Luan, W. Li, S. Liu, and D. Sun, Phase behavior of mixtures of positively charged colloidal platelets and nonadsorbing polymer, Langmuir 25, 6349 (2009).

[33] T. Nakato, Y. Yamashita, E. Mouri, and K. Kuroda, Multiphase coexistence and destabilization of liquid crystalline binary nanosheet colloids of titanate and clay, Soft Matter 10, 3161 (2014).

[34] M. Chen, H. Li, Y. Chen, A. F. Mejia, X. Wang, and Z. Cheng, Observation of isotropic-isotropic demixing in colloidal platelet-sphere mixtures, Soft Matter 11, 5775 (2015).

[35] T. Eckert, M. Schmidt, and D. de las Heras, Gravity-induced phase phenomena in plate-rod colloidal mixtures, Commun. Phys. 4, 202 (2021).

[36] D. de las Heras, N. Doshi, T. Cosgrove, J. Phipps, D. I. Gittins, J. S. V. Duijneveldt, and M. Schmidt, Floating nematic phase in colloidal platelet-sphere mixtures, Sci. Rep. 2, 789 (2012).

[37] G. Vroege, D. Thies-Weesie, A. Petukhov, B. Lemaire, and P. Davidson, Smectic liquid-crystalline order in suspensions of highly polydisperse goethite nanorods, Adv. Mater. 18, 2565 (2006).

[38] E. van den Pol, D. M. E. Thies-Weesie, A. V. Petukhov, G. J. Vroege, and K. Kvashnina, Influence of polydispersity on the phase behavior of colloidal goethite, J. Chem. Phys. 129, 164715 (2008).

[39] Z. X. Zhang and J. S. van Duijneveldt, Isotropic-nematic phase transition of nonaqueous suspensions of natural clay rods, J. Chem. Phys. 124, 154910 (2006).

[40] F. M. van der Kooij, D. van der Beek, and H. N. W. Lekkerkerker, Isotropic-nematic phase separation in suspensions of polydisperse colloidal platelets, J. Phys. Chem. B 105, 1696 (2001).

[41] D. de las Heras and M. Schmidt, The phase stacking diagram of colloidal mixtures under gravity, Soft Matter 9, 8636 (2013).

[42] T. Geigenfeind and D. de las Heras, The role of sample height in the stacking diagram of colloidal mixtures under

gravity, J. Phys. Condens. Matter 29, 064006 (2016).

[43] T. Drwenski, P. Hooijer, and R. van Roij, Sedimentation stacking diagrams of binary mixtures of thick and thin hard rods, Soft Matter 12, 5684 (2016).

[44] D. de las Heras, L. L. Treffenstädt, and M. Schmidt, Reentrant network formation in patchy colloidal mixtures under gravity, Phys. Rev. E 93, 030601 (2016).

[45] G. Avvisati, T. Dasgupta, and M. Dijkstra, Fabrication of colloidal laves phases via hard tetramers and hard spheres: Bulk phase diagram and sedimentation behavior, ACS Nano 11, 7702 (2017).

[46] T. Dasgupta and M. Dijkstra, Towards the colloidal laves phase from binary hard-sphere mixtures via sedimentation, Soft Matter 14, 2465 (2018).

[47] R. Braz Teixeira, D. de las Heras, J. M. Tavares, and M. M. Telo da Gama, Phase behavior of a binary mixture of patchy colloids: Effect of particle size and gravity, J. Chem. Phys. 155, 044903 (2021).

[48] T. Eckert, M. Schmidt, and D. de las Heras, Sedimentation of colloidal plate-sphere mixtures and inference of particle characteristics from stacking sequences, Phys. Rev. Research 4, 013189 (2022).

[49] D. de las Heras and M. Schmidt, Sedimentation stacking diagram of binary colloidal mixtures and bulk phases in the plane of chemical potentials, J. Phys.: Condens. Matter 27, 194115 (2015).

[50] T. Eckert, M. Schmidt, and D. de las Heras, Sedimentation path theory for mass-polydisperse colloidal systems, J. Chem. Phys 157, 234901 (2022).

[51] L. Bellier-Castella and H. Xu, Sedimentation profiles of polydisperse fluids, J. Phys.: Condens. Matter 15, 5417 (2003).

[52] Y. Martínez-Ratón and E. Velasco, Effect of combined roundness and polydispersity on the phase behavior of hard-rectangle fluids, Phys. Rev. E 106, 034602 (2022).

[53] E. Helfand, H. Reiss, H. L. Frisch, and J. L. Lebowitz, Scaled particle theory of fluids, J. Chem. Phys. 33, 1379 (1960).

[54] S. Pollock, L. G. Rebholz, and M. Xiao, Anderson-accelerated convergence of picard iterations for incompressible navier–stokes equations, Siam J. Numer. Anal. 57, 615 (2019).

[55] A. L. Thorneywork, J. L. Abbott, D. G. Aarts, and R. P. Dullens, Two-dimensional melting of colloidal hard spheres, Phys. Rev. Lett. 118, 158001 (2017).

[56] R. Roth, Fundamental measure theory for hard-sphere mixtures: a review, J. Phys.: Condens. Matter 22, 063102 (2010).

[57] Y. Martínez-Ratón, S. Varga, and E. Velasco, Biaxial nematic phases in fluids of hard board-like particles, Phys. Chem. Chem. Phys. 13, 13247 (2011).

[58] R. Wittmann, M. Marechal, and K. Mecke, Fundamental measure theory for non-spherical hard particles: predicting liquid crystal properties from the particle shape, J. Phys.: Condens. Matter 28, 244003 (2016).

[59] R. Wittmann, C. E. Sitta, F. Smallenburg, and H. Löwen, Phase diagram of two-dimensional hard rods from fundamental mixed measure density functional theory, J. Chem. Phys. 147, 134908 (2017).

[60] A. El Moumane, M. te Vrugt, H. Löwen, and R. Wittmann, Biaxial nematic order in fundamental measure theory, J. Chem. Phys. 160, 094903 (2024).

[61] R. Zwanzig, First-order phase transition in a gas of long thin rods, J. Chem. Phys. 39, 1714 (1963).
 

[62] M. Buzzacchi, I. Pagonabarraga, and N. B. Wilding, Polydisperse hard spheres at a hard wall, J. Chem. Phys. 121, 11362 (2004).

[63] Y.-X. Yu, J. Wu, Y.-X. Xin, and G.-H. Gao, Structures and correlation functions of multicomponent and polydisperse hard-sphere mixtures from a density functional theory, J. Chem. Phys. 121, 1535 (2004)

[64] Á. Speranza and P. Sollich, Isotropic-nematic phase equilibria of polydisperse hard rods: The effect of fat tails in the length distribution, J. Chem. Phys. 118, 5213 (2003)

[65] F. Sammüller, S. Hermann, D. de las Heras, and M. Schmidt, Neural functional theory for inhomogeneous fluids: Fundamentals and applications, Proc. Natl. Acad. Sci. 120, e2312484120 (2023).

[66] T. Zimmermann, F. Sammüller, S. Hermann, M. Schmidt, and D. de las Heras, Neural force functional for non-equilibrium many-body colloidal systems, Mach. Learn.: Sci. Technol. 5, 035062 (2024).

[67] L. Ding and C. Do, Deciphering the small-angle scattering of polydisperse hard spheres using deep learning, APL Mach. Learn. 3, 036112 (2025).
 
