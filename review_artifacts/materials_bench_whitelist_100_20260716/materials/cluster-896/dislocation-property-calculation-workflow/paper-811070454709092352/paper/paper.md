# Heteroepitaxial anisotropic film growth of various orientations

Muhammad Ajmal Choudhary*, Julia Kundin

Department of Engineering Science, University Bayreuth, D-95440, Bayreuth, Germany

---

## ARTICLE INFO

**Article history:**
Received 11 September 2016
Revised 16 December 2016
Accepted 11 January 2017
Available online 31 January 2017

**Keywords:**
Nucleation
Dislocations
Misfit orientations
Material modeling

## ABSTRACT

Investigation of the heteroepitaxial film growth for anisotropic systems has been carried out by means of the anisotropic phase-field crystal model. Numerical simulations have been performed by varying the anisotropic parameters, orientations, and lattice misfit between isotropic substrate and anisotropic film layers. The simulation results demonstrate the formation of dislocations during the growth of layers with non-cubic anisotropic lattice in the presence of the elastic strain caused by the lattice misfits. It is shown that for any particular choice of misfit, both the lattice anisotropy of the film and the orientation of the substrate influence the parameters of dislocation formation such as the number of dislocations, the characteristic distance at which dislocations begin to nucleate, and the excess elastic energy.

© 2017 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The heteroepitaxial growth phenomena is one of the most commonly used techniques to fabricate various electronic as well as optical devices since most of these devices need sophisticated structures which are based on thin layers with various compositions. In the past, in most of the investigated epitaxial growth processes, both the epitaxial layer and the substrate had similar crystal structure and the same orientation. However, there are many important cases where the epitaxial layer and the substrate have either a different orientation such as CdTe [1,1,1] on GaAs [1,0,0] or a completely different crystal structure such as silicon on sapphire. The quality and performance of these devices depend on the structural composition and the arrangement of epitaxial layers, which are based on the growth method as well as several other factors such as the substrate and layer misfit, the thermodynamic driving force, and the substrate misorientation.

The properties of thin films can be totally different from the corresponding bulk material since the reduction in size can play an important role in the kinetics of the system. This drives several complex phenomena in heteroepitaxial growth (Thayer et al., 2001). The growth of a good quality heteroepitaxial film certainly depends on various factors including lattice mismatch between the substrate and the film, properties of the interface, and processes under which the interface is formed. The growth of a thin film with a certain lattice parameter on top of a substrate with a different lattice parameter naturally results in a strained structure due to the lattice mismatch. The misfit elastic strains strongly influence the kinetic features of the film growth and the resulting structural properties. They lead to an increasing surface roughening or buckling at a certain film thickness. Such strained films become energetically unstable as the film thickness keeps on increasing. Once the thickness of the film exceeds a certain critical value $H_c$ (commonly known as a critical layer thickness), the lattice of the thin film tries to relax to its initial structure with a specific lattice parameter and this situation often results in the formation of lattice defects being accompanied by 3D island growth (Politi et al., 2000). The misfit strains can be controlled during the

* Corresponding author.
E-mail address: ajmal.choudhary@gmail.com (M.A. Choudhary).

http://dx.doi.org/10.1016/j.jmps.2017.01.006
0022-5096/© 2017 Elsevier Ltd. All rights reserved.

![](./images/811070454709092352_1.jpg)
![](./images/811070454709092352_2.jpg)
![](./images/811070454709092352_3.jpg)

forming process and even artificial stress can be applied to the thin film material by choosing a certain substrate in order to achieve the desired physical properties. Moreover, there are several experimental evidences which demonstrate that the lattice mismatch between the substrate and the layer plays an important role in the formation of grain boundaries (Asano and Ishiwara, 1983; Farrow et al., 1981). This phenomenon is commonly known as morphological instability (Yu et al., 2011).

The key questions arising in film growth phenomena include the important features of the microstructures, factors that determine and control the microstructures, and the impact of these microstructures on the properties of resulting thin films. Considerable efforts have been made to understand and control the surface roughening in semiconductors and oxide thin film growth (Manasevit, 1974). For instance, oxide layers with perovskite structure, which have specific piezo- and ferroelectric properties, are of great interest for a large number of applications. Therefore, it is possible to achieve a desired set of properties for such oxide layers by controlling misfit strains in a layer (Biegalski et al., 2009; Haeni et al., 2004).

A recently developed continuum approach known as phase-field crystal method (PFC) has emerged as a widely used alternative to investigate heteroepitaxial growth phenomena because of its capability to simulate the evolution of atomic layers on time scales much longer than possible for molecular dynamic simulations (MD), while keeping much more detail than standard phase-field models. Since its introduction, the PFC approach has emerged as a computationally efficient alter- native to the other existing simulation approaches for problems where the atomic and continuum scales are tightly coupled (Berry et al., 2006; Elder and Grant, 2004; Elder et al., 2002; Stefanovic et al., 2006). An interesting feature of the PFC approach is the natural incorporation of elastic effects into the free energy functional. Thus in the PFC method (unlike tra- ditional phase-field models) one does not explicitly need to integrate elasticity into the functional (Choudhary et al., 2011). The first investigation of the effect of the misfit in liquid-phase epitaxial growth by means of the PFC model was carried out by Elder and Grant (2004). It was found that the simulated dependency of the critical layer thickness at which dislocations nucleate on the misfit in the region $-0.11 < \varepsilon < 0.11$ is almost consistent with the dependency proposed by Matthews and Blakeslee (1974). Recent developments in PFC modeling of the heteroepitaxy were summarized in the work of Podmaniczky et al. (2015) for non-vicinal substrate surfaces. The influence of the reduced temperature and the noise strength on the mis- fit dislocation formation was shown. It was found that the critical thickness decreases with increasing noise (Podmaniczky et al., 2015). The numerical investigations of the effect of the lattice misfit on the morphological instability in complex het- eroepitaxial systems on the vicinal substrates were carried out by Yu et al. (2011). The results show the influence of vicinal angles on the formation of islands and mismatch dislocation during the 2D and 3D heteroepitaxial growth.

In recent years, we extended the standard PFC method by developing a generalized model which has the capability to simulate anisotropic lattice systems (Choudhary et al., 2012; 2011; Kundin et al., 2014). This newly developed anisotropic phase-field crystal (APFC) model allows us to investigate the effect of misfit on the critical layer thickness for the lattices with non-cubic and sheared crystallographic symmetry (Choudhary et al., 2014). Moreover, it can be applied to the growth of the films with monoclinic or triclinic crystal lattice. For a two-dimensional case such lattices make up parallelogram (or oblique) lattices with base angles $\neq 90^{\circ}$. The typical examples of the epitaxial growth of the monoclinic or triclinic films are BiFeO3 films (Chen et al., 2011) and pentacene thin films (Drummy and Martin, 2005). H. Wang et al. also discussed the phenomenon of triclinic deformation and anisotropic strain relaxation of InAs films (Wang et al., 1998).

Our previously reported study of anisotropic film growth in liquid phase epitaxy by means of the APFC model demon- strated the effect of the anisotropic parameter on the critical layer thickness (Choudhary et al., 2014). The systems with various anisotropic mis-orientations were compared to the isotropic system with the non-vicinal substrate surface. In the present work, we extend these investigations of liquid phase heteroepitaxial growth further by performing simulations for various substrate-film configurations and various orientations of the substrate with vicinal and non-vicinal surface.

The paper is organized as follows: First, we give the description of two variants of the APFC model with tilted lattices in x and y directions in Section 2. Then we discuss the methodology used in these investigations in Section 3. The corresponding simulation results are also demonstrated in Section 3. Finally, we conclude with a summary in Section 4.

## 2. The APFC model with different orientations

The evaluation of model parameters of the APFC model has recently been reported in Ref. (Choudhary et al., 2014). In this model variant, the lattice inclination was considered in y-direction. Here, we describe both possible variants with orientation of the lattice anisotropy in x and y directions, which will be used in our current study. We start with a standard dimensionless form of the free energy functional with the anisotropic Laplace operator:

$$
\mathcal{F}=\int_{V}\left(\frac{\phi}{2}\left[r+\left(1+\nabla_{s}^{2}\right)^{2}\right] \phi+\frac{\phi^{4}}{4}\right) d r,
\tag{1}
$$

where $\phi$ is the phase field, which is the reduced atomic (particle) density, $r$ represents the undercooling, and $\nabla_{s}$ is the anisotropic gradient. The evolution equation of the phase field is

$$
\frac{\partial \phi}{\partial t}=M \nabla^{2} \frac{\delta \mathcal{F}}{\delta \phi}
\tag{2}
$$

with a constant mobility ($M=1$).

![](./images/811070454709092352_4.jpg)

Fig. 1. The illustration scheme of the lattices shifted clockwise; (a) and (c) shift vectors and the shifted lattice in x direction; (b) and (d) shift vectors and the shifted lattice in y direction.

In the first orientation variant, the anisotropy is considered as a shear of a triangle lattice in the x direction and the initial lattice is defined by

$$
\phi=f_{0}+f_{1}\left[\cos \left(k_{1}(x \pm s y)\right) \cos \left(k_{2} y / \sqrt{3}\right)+1 / 2 \cos \left(2 k_{2} y / \sqrt{3}\right)\right]. \tag{3}
$$

In the second orientation variant, the lattice is sheared in the y direction and is defined by

$$
\phi=f_{0}+f_{1}\left[\cos \left(k_{1} x\right) \cos \left(k_{2}(y \mp s x) / \sqrt{3}\right)+1 / 2 \cos \left(2 k_{2}(y \mp s x) / \sqrt{3}\right)\right]. \tag{4}
$$

Here, $f_{0}$ and $f_{1}$ are the average value and the amplitude of the phase field, and $k_{1}$ and $k_{2}$ are the wave numbers.

Due to the shear (which is defined as the anisotropic parameter $s$ in the model), the unit vector of the crystal lattice $\vec{e}_{y}$ is shifted to the vector $\vec{e}_{y}^{s}=\vec{e}_{y} \pm s \vec{e}_{x}$, or the unit vector $\vec{e}_{x}$ is shifted to the vector $\vec{e}_{x}^{s}=\vec{e}_{x} \pm s \vec{e}_{y}$. The symbol + indicates shift in the clockwise direction and - indicates shift in the anti-clockwise direction. For better understanding consult the illustration in Fig. 1.

The corresponding anisotropic gradient in (1) is defined as

$$
\nabla_{s}=a_{1} \frac{\partial}{\partial x} \vec{e}_{x}+a_{2} \frac{\partial}{\partial y} \vec{e}_{y}^{s}. \tag{5}
$$

Furthermore, one can expand the above equation to obtain an expression for the gradient square term, i.e.,

$$
\nabla_{s}^{2}=a_{1}^{2} \frac{\partial^{2}}{(\partial x)^{2}}\left|\vec{e}_{x}^{s}\right|^{2}+2 a_{1} a_{2} \frac{\partial^{2}}{\partial x \partial y}\left(\vec{e}_{x} \cdot \vec{e}_{y}^{s}\right)+a_{2}^{2} \frac{\partial^{2}}{(\partial y)^{2}}\left|\vec{e}_{y}^{s}\right|^{2}. \tag{6}
$$

For the sake of simplicity we consider the lattice Eq. (4) with the shear in y direction. By using the vector product calculated as $(\vec{e}_{x} \cdot \vec{e}_{y}^{s})= \pm s \cdot 1+1 \cdot 0= \pm s$ and the vector module $|\vec{e}_{y}^{s}|=\sqrt{1+s^{2}}$ we can rewrite Eq. (6) as

$$
\nabla_{s}^{2}=a_{1}^{2} \frac{\partial^{2}}{(\partial x)^{2}} \pm 2 a_{1} a_{2} s \frac{\partial^{2}}{\partial x \partial y}+a_{2}^{2}\left(1+s^{2}\right) \frac{\partial^{2}}{(\partial y)^{2}} \tag{7}
$$

Similarly, one can further expand Eq. (7) to obtain an expression for $\nabla_s^4$, i.e.,

$$
\begin{aligned}
\nabla_{s}^{4}=\left(\nabla_{s}^{2}\right)^{2} &=a_{1}^{4} \frac{\partial^{4}}{(\partial x)^{4}} \pm 4 a_{1}^{3} a_{2} s \frac{\partial^{4}}{(\partial x)^{3} \partial y} \\
&+2 a_{1}^{2} a_{2}^{2}\left(1+s^{2}\right) \frac{\partial^{4}}{(\partial x)^{2}(\partial y)^{2}}+4 a_{1}^{2} a_{2}^{2} s^{2} \frac{\partial^{4}}{(\partial x \partial y)^{2}} \\
&\pm 4 a_{1} a_{2}^{3} s\left(1+s^{2}\right) \frac{\partial^{4}}{\partial x(\partial y)^{3}}+a_{2}^{4}\left(1+s^{2}\right)^{2} \frac{\partial^{4}}{(\partial y)^{4}}.
\end{aligned} \tag{8}
$$

The parameters can be represented as components of the matrix $a_{ij}$ and the tensor $b_{ijkl}$ of the APFC model. The full derivation of parameters $a_{ij}$ and $b_{ijkl}$ is given in our previous paper (Choudhary et al., 2014). Then the corresponding anisotropic Laplace operator (7) is defined as

$$
\nabla_{s}^{2}=a_{11} \frac{\partial^{2}}{(\partial x)^{2}} \pm 2 a_{12} \frac{\partial^{2}}{\partial x \partial y}+a_{22} \frac{\partial^{2}}{(\partial y)^{2}}. \tag{9}
$$

Similarly, the expression for $\nabla_s^4$ is given by

$$
\begin{aligned}
\nabla_{s}^{4}=\left(\nabla_{s}^{2}\right)^{2} &=b_{1111} \frac{\partial^{4}}{(\partial x)^{4}} \pm 4 b_{1112} \frac{\partial^{4}}{(\partial x)^{3} \partial y} \\
&+2 b_{1122} \frac{\partial^{4}}{(\partial x)^{2}(\partial y)^{2}}+4 b_{1212} \frac{\partial^{4}}{(\partial x \partial y)^{2}} \\
&\pm 4 b_{1222} \frac{\partial^{4}}{\partial x(\partial y)^{3}}+b_{2222} \frac{\partial^{4}}{(\partial y)^{4}}.
\end{aligned} \tag{10}
$$

The resulting expressions for the matrix parameters for the shear in the $x$ direction are:

$$
\begin{aligned}
&a_{11}=a_{1}^{2}\left(1+s^{2}\right), \\
&a_{22}=a_{2}^{2}, \\
&a_{12}=a_{1} a_{2} s,
\end{aligned} \tag{11}
$$

and

$$
\begin{aligned}
&b_{1111}=a_{1}^{4}\left(1+s^{2}\right)^{2}, \\
&b_{1112}=a_{1}^{3} a_{2} s\left(1+s^{2}\right), \\
&b_{1122}=a_{1}^{2} a_{2}^{2}\left(1+s^{2}\right), \\
&b_{1212}=a_{1}^{2} a_{2}^{2} s^{2}, \\
&b_{1222}=a_{1} a_{2}^{3} s, \\
&b_{2222}=a_{2}^{4}.
\end{aligned} \tag{12}
$$

Similarly for the shear in the $y$ direction, the parameters can be defined as

$$
\begin{aligned}
&a_{11}=a_{1}^{2}, \\
&a_{22}=a_{2}^{2}\left(1+s^{2}\right), \\
&a_{12}=a_{1} a_{2} s,
\end{aligned} \tag{13}
$$

and

$$
\begin{aligned}
&b_{1111}=a_{1}^{4}, \\
&b_{1112}=a_{1}^{3} a_{2} s, \\
&b_{1122}=a_{1}^{2} a_{2}^{2}\left(1+s^{2}\right), \\
&b_{1212}=a_{1}^{2} a_{2}^{2} s^{2}, \\
&b_{1222}=a_{1} a_{2}^{3} s\left(1+s^{2}\right), \\
&b_{2222}=a_{2}^{4}\left(1+s^{2}\right)^{2}.
\end{aligned} \tag{14}
$$

The equilibrium properties of crystals that lie within the capacity of the model and elastic constants are derived and discussed in detail in a separate article (Kundin and Choudhary, 2016). Here, we briefly describe the resulting expression.

The equilibrium wave numbers in $x$ and $y$ directions, $k_1$ and $k_2$, and the equilibrium amplitude $A_{\text{min}}$ are derived by setting derivatives $\frac{\partial \tilde{F}}{\partial k_{1}}$, $\frac{\partial \tilde{F}}{\partial k_{2}}$, and $\frac{\partial \tilde{F}}{\partial I_{1}}$ to zero. Furthermore, a stretch parameter $\epsilon=(a_1 - a_2)/a_2$ and the value of $a_1=1$ is used in this expression. The resulting expressions are given as follows:

$$
k_{1}^{2}=\frac{3}{4} \frac{\left(1+\epsilon^{2} s^{2}\right)}{\left(1+(3 / 2) \epsilon^{2} s^{2}\right)}, \quad k_{2}^{2}=\frac{3}{4} \frac{(1+\epsilon)^{2}}{\left(1+(3 / 2) \epsilon^{2} s^{2}\right)}, \tag{15}
$$

and
$$
A_{\text{min}}=-\frac{4}{5}\psi_{0}-\frac{4}{15}\sqrt{-15(r+R)-36f_{0}^{2}}, \tag{16}
$$
where
$$
R=\frac{(1/2)\epsilon^{2}s^{2}}{\left(1+(3/2)\epsilon^{2}s^{2}\right)}. \tag{17}
$$

The wave numbers depend on $s$ and $\epsilon$ according to Eq. (15). It can be seen that in the case of $a_{1}=a_{2}$ and $\epsilon=0$, the wave numbers become equal to the equilibrium wave number, $k_{1}=k_{2}=q_{\text{eq}}=\sqrt{3}/2$, and do not depend on the anisotropic parameter $s$. In our current study we use $\epsilon=0$ to investigate the pure effect of the anisotropic parameter.

The definition of elastic properties for an anisotropic system is very useful for the present study of the stress induced morphological instability. The resulting expression for the Poisson's ratio is defined in Kundin and Choudhary (2016) as
$$
\nu=\frac{1}{3}\frac{\left(1+3\epsilon^{2}s^{2}\right)}{\left(1+\epsilon^{2}s^{2}\right)}. \tag{18}
$$

It is important to mention that the standard simplistic PFC model can only model systems with Poisson's ratio of 1/3. However, the anisotropic PFC model which is a more generalized form of the standard PFC model has the capability to model systems with arbitrary Poisson's ratio which can be expressed as functions of $s$ and $\epsilon$. Thus, according to Eq. (18), $\nu$ deviates from the ideal case 1/3 if both the stretch $\epsilon$ and the shear $s$ of a lattice are non-zero.

The other elastic modules can be evaluated as
$$
\begin{aligned}
C_{12} & =\frac{\left(A_{\text{min}}q_{\text{eq}}^{2}\right)^{2}}{3}\frac{\left(1+\epsilon^{2}s^{2}\right)\left(1+3\epsilon^{2}s^{2}\right)}{\left(1+(3/2)\epsilon^{2}s^{2}\right)^{2}}=A_{\text{min}}^{2}k_{1}^{4}\nu, \\
C_{44} & =\frac{\left(A_{\text{min}}q_{\text{eq}}^{2}\right)^{2}}{3}\frac{(1+\epsilon)^{2}\left(1+3\epsilon^{2}s^{2}\right)}{\left(1+(3/2)\epsilon^{2}s^{2}\right)^{2}}=A_{\text{min}}^{2}k_{1}^{2}k_{2}^{2}\nu, \\
C_{11} & =\left(A_{\text{min}}q_{\text{eq}}^{2}\right)^{2}\frac{\left(1+\epsilon^{2}s^{2}\right)^{2}}{\left(1+(3/2)\epsilon^{2}s^{2}\right)^{2}}=A_{\text{min}}^{2}k_{1}^{4}. \tag{19}
\end{aligned}
$$

The magnitude of elastic constants can be adjusted with the amplitude $A_{\text{min}}$ which depends on the temperature $r$ and the density $f_{0}$ according to Eq. (16). Since the elastic constants depend on $r$ and $f_{0}$, the latter can influence the results of numerical simulations. Therefore, we have used constant values of $r$ and $f_{0}$ in our study.

The elastic constants are consistent with the symmetry of a triangle system in isotropic case, i.e., the anisotropy ratio $(C_{11}-C_{12})/(2C_{44})$ is equal to 1. In the anisotropic case, the elastic constants and the anisotropy ratio change with $s$ and $\epsilon$. The examples of the elastic constants and the anisotropy ratio for anisotropic lattices can be found in the Refs. (Cogswell and Bazant, 2012; Goryaeva et al., 2015; Jiang et al., 2008; Mourachkine, 2006). Note that these examples of real lattices do not show the quantitative correspondence to the model parameters because the connection of the simple PFC model to the real systems is still a complicated problem for both isotropic and anisotropic crystal lattices.

It should also be noted that the lattice parameter, $a$, is defined as the distance between nearest-neighbor local maxima of $\phi$, and the equilibrium wave number is defined as $q_{\text{eq}}=2\pi/a$. Both parameters do not depend on $r, f_{0}, s$ and $\epsilon$.

The Gaussian random noise is used in the simulations in accordance to the definition given in Ref. (Elder and Grant, 2004). The noise amplitude is chosen as $D=A_{\text{noise}}^{2}\phi^{2}$.

## 3. Numerical investigation of the heteroepitaxial growth for anisotropic system

In this section, we present the investigation of the dislocation formation during the heteroepitaxial growth for the anisotropic systems by means of the APFC model. The simulations were carried out in two-dimensions (2D). The reason for choosing a 2D model for these investigations is to avoid demanding computational resources required for the 3D structures. The 3D simulations of the heteroepitaxial growth on a vicinal substrate were successfully carried out in Ref. (Yu et al., 2011). They revealed the step-brunching profile as well as the misfit dislocations within the film, which are elongated in the same direction as steps. The 2D sections normal to the steps show the steps and dislocations as point elements of the structure. It can be seen that due to this geometry, the third direction does not influence the growth modes and the defect nucleation significantly so that the simulations can be reduced to 2D case.

Eq. 1is transformed to describe the substrate and the growing film with the different lattice constants, i.e.,
$$
F=\int_{V}\left(\frac{\phi}{2}\left[r+\left(1+\lambda^{2}\nabla_{s}^{2}\right)^{2}\right]\phi+\frac{\phi^{4}}{4}\right)dr, \tag{20}
$$
where $\lambda$ is the parameter responsible for the lattice constant.

The investigated system consist of the substrate and the film which grows in the $y$ direction. In the substrate, the anisotropic parameter is equal to zero, i.e., $s_{0}=0$ and the lattice constant parameter is assumed to be 1, i.e., $\lambda_{0}=1$. In

![](./images/811070454709092352_5.jpg)

Fig. 2. A simulation box (having four unit cells) with $\Delta x=a/9$ and $\Delta y=aq_{\text{eq}}/8$.

the growing film, various values of the anisotropic parameter for the shear in the $x$ or $y$ direction are chosen in the interval $s\in[0,0.32]$, and the lattice constant is chosen in the interval $\lambda_{f}\in[0.86,1.14]$. The corresponding misfit $\varepsilon=(\lambda_{f}-\lambda_{0})/\lambda_{0}$ belongs to the interval $[-0.14,+0.14]$.

The influence of the anisotropy on the resulting microstructures and the dislocation nucleation at various misfits $\varepsilon$ is investigated. This study shall establish how the nucleation of defects depends on the anisotropic parameter of the film as well as on the orientation of the substrate surface.

In order to achieve this, we adopt different possible substrate/film configurations in heteroepitaxial anisotropic growth with vicinal and non-vicinal substrate surfaces and compare the resulting parameters of the dislocation nucleation and the propagation in detail. For vicinal surfaces, we consider the system configuration with the growth direction and the shear direction along the $y$-axis. This configuration is termed as "Test YY" in this study. For non-vicinal surfaces, we assume the growth direction along the $y$-axis and the shear direction along the $x$-axis. This configuration is termed as "Test YX".

The governing evolution Eq. (2) is solved numerically in two-dimensions on a system domain of size $L_{x}\times L_{y}$ with $\lambda=1$ in the substrate and $\lambda=\lambda_{f}$ in the rest of the domain. The Euler discretization scheme is used for the time derivative and the "spherical Laplacian" approximation is used to calculate Laplacians.

One unit cell has the size of $l_{x}\times l_{y}=a\times(\sqrt{3}/2)a$. The lattice constant is defined as $a=2\pi/q_{\text{eq}}=4\pi/\sqrt{3}$. The discretization size is chosen as $\Delta x=a/9=(4\pi/\sqrt{3})/9$ and $\Delta y=(\sqrt{3}/2)a/8=4\pi/16$, where 9 and 8 are the numbers of discretization points in the $x$ and $y$ direction, respectively. A section of the simulation box, which consist of 4 unit cells, is illustrated in Fig. 2. The values of the other model parameters used in the simulations are chosen as $r=-0.25$, $f_{0}=0.285$ and $\Delta t=0.0009$. The periodic boundary conditions are applied to the left and right side of the growing film. Following Ref. (Elder and Grant, 2004), we use the constant mass flux boundary condition at a distance $L_{b}=120\Delta x$ above the solidification front with setting $\phi(L_{b})=f_{0}$. On the bottom of the substrate, the atomic field is defined by the isotropic lattice with $s_{0}=0$.

By setting different parameters $s$ and $\lambda$ for the substrate area and the film growth area in the model equation, the diffuse interface forms. It can be seen from the simulation results that no phase transformation occurs between the film and the substrate. This is because of the reason that the two solid phases have similar thermodynamic properties. The phase transformation between the solid film and the liquid is provided by the model equation and by a constant flux boundary condition above the solidification front.

### 3.1. Vicinal substrate surface

In this section we consider the configuration "Test YY" with the shear of the film lattice and the film growth direction along the $y$-axis. The lattice of substrate is initialized at the bottom of the simulation box. The thickness of the substrate is chosen to be $60\Delta y$. The film lattice produced during the simulation has the form

$$
\phi=f_{0}+f_{1}\left[\cos(k_{1}x)\cos(k_{2}(y-sx)/\sqrt{3})+1/2\cos(2k_{2}(y-sx)/\sqrt{3})\right],\tag{21}
$$

The simulation results for this configuration show that for the case of non-tilted surface the difference of the anisotropic parameters between the substrate and the film $\Delta s=s_{0}-s_{f}$ produces an incoherent interface between the substrate surface and the film. Due to the incoherent interface, dislocations nucleate directly on the interface. In order to ensure coherent interface, which is appropriate for the real film growth, we adjust the substrate surface by the rotation of the substrate lattice on the corresponding vicinal angle $\theta$ with $\tan(\theta)=\Delta s$. In such a case, the vicinal substrate surface will be initialized with the corresponding number of steps.

The system size is chosen as $L_{x}\times L_{y}=1440\times1440$. To achieve the periodic boundary conditions in the $x$-direction, the vicinal surface angle $\theta$ and the box size $L_{x}$ need to be selected so that the number of steps $N_{x}$ is an integer value. In order to achieve this, we choose $N_{x}=(10,20,40,60)$. Then using $N_{x}=L_{x}\Delta x/(an)=L_{x}/(9n)$, where $n$ is the step spacing

![](./images/811070454709092352_6.jpg)

Fig. 3. Resulting microsctructures from numerical simulations performed for the vicinal angle $6.178^{\circ}$ for (a) the isotropic and (b) anisotropic film lattice with $s_{f}=0.10825$. The simulation time $t=420$, $\varepsilon=0.09$. The color bar represents the value of $\phi$. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

in units of the lattice constant, we can calculate $n=(16,8,4,8/3)$ for $L_{x}=1440$. Finally, $\theta$ is defined from the condition $\tan(\theta)=(l_{y}/(nl_{x})=(\sqrt{3}/2)/n=(\sqrt{3}/32,\sqrt{3}/16,\sqrt{3}/8,3\sqrt{3}/16)$. The corresponding angles are $\theta=(3.098^{\circ},6.178^{\circ},12.216^{\circ},17.992^{\circ})$ and the anisotropic parameters in the film are $s_{f}=\tan\theta=(0.05413,0.10825,0.21651,0.32476)$.

To produce the vicinal surface at various vicinal angles, the atomic field in the substrate is initialized by the rotated lattice, i.e.

$$
\phi=f_{0}+f_{1}\left[\cos(k_{1}(x-\tan(\theta)y))\cos(k_{2}(y+\tan(\theta)x-s_{0}x)/\sqrt{3})+1/2\cos(2k_{2}(y+\tan(\theta)x-s_{0}x)/\sqrt{3})\right],\quad(22)
$$

Note that the Laplace operator is rotationally invariant and we do not need to change the code to incorporate the rotation in the dynamic Eq. (2).

Simulations are performed for various lattice misfits $\varepsilon$ and the anisotropic parameters of the film to study the effects of the anisotropy on the overall growth phenomena. We evaluate the critical thickness of the dislocation formation $H_{c}$ (in units of unit cells) and the change of the free energy of the system due to the dislocations.

### 3.1.1. The system with positive misfit $\varepsilon>0$

The numerical simulations are performed for positive misfit values (a film in compression) according to the procedure described in the previous section. In case of an isotropic system with singular surface, the simulations were carried out with the noise $A_{\text{noise}}=0.5$. In case of vicinal surfaces and anisotropic systems, the simulations were carried out without noise and with noise $A_{\text{noise}}=1.2$.

Fig. 3 illustrates the resulting microstructures obtained from numerical simulations, performed for the isotropic and anisotropic films with $\theta=6.178^{\circ}$, $s_{f}=0.108$, and $\varepsilon=0.09$.

In our simulations (see Fig. 3), the dislocations form at the tips of the grooves of the solid-liquid interface, which becomes non-flat due to the stress-driven morphological instability. This is a result of the stress concentration in grooves. The stress-driven morphological instability is called the Asaro-Tiller-Grinfeld instability and it is usually associated with step-bunching and dislocation-free Stranski-Krastanow growth. It is different from the Mathews-Blakeslee model which postulates the nucleation of misfit dislocation that accommodates the applied strain. In general, both mechanisms are present simultaneously. The stress-driven morphological instability can strongly influence the nucleation of misfit dislocations. This statement was verified through experimental investigations (Jonsdottir and Freund, 1995; Ozkan et al., 1997; Wu et al., 2007) as well as through modeling (Dong et al., 1998; Elder and Grant, 2004; Haataja et al., 2001; 2002; Ruffini et al., 2013). The previous results of the PFC modeling of isotropic film growth show the formation of dislocations due to the Asaro-Tiller-Grinfeld instability and a linear relationship between $\varepsilon$ and the inverse critical thickness, $P$, similar to the Mathews-Blakeslee model (Elder and Grant, 2004; Podmaniczky et al., 2015). At the same time, it was found that the deviation from the isotropy can influence this dependency, for example, it was shown in the work (Podmaniczky et al., 2015) that the $P$ versus $\varepsilon$ plot for a faceted system (a surface anisotropy) results in a considerable deviation from the original Mathews-Blakeslee plot.

The critical thickness of the dislocation formation $H_{c}$ and the inverse critical thickness $P=(1+\log(H_{c}))/H_{c}$ as a function of the misfit for the isotropic and anisotropic films with the corresponding vicinal surface angles is shown in Fig. 4. A comparison to the previously reported studies is illustrated in Fig. 5. Note that in all plots the angles and the anisotropic parameters are given in rounded form for the sake of simplicity.

The results in Fig. 4(b) demonstrate that for an isotropic system with $\theta=0$ (non-vicinal singular surface), the dependence of $P$ on $\varepsilon$ is linear. This dependence corresponds to Matthews-Blakeslee analytical expression similarly to the previously reported studies (Elder and Grant, 2004; Podmaniczky et al., 2015). It can be seen in Fig. 5(a) that the calculated inverse critical thickness $P$ is smaller in comparison to Elder and Grant (2004).

![](./images/811070454709092352_7.jpg)

Fig. 4. The resulting (a) critical film thickness $H_c$ and (b) inverse critical film thickness $P$ for isotropic and anisotropic system with various vicinal angles $\theta$ as functions of $\varepsilon > 0$.

Now we will discuss the results of the simulation of anisotropic and isotropic films on vicinal surfaces which were carried out without noise (see Fig. 4). The plot $P$ versus $\varepsilon$ for $\theta = 3^\circ$ is close to linear. For $\theta \geq 6^\circ$, the plot has a linear trend for small misfit values and becomes exponential at large misfits. A simple physical explanation of this behavior is that the morphological instability as well as the dislocation formation are essentially reduced without additional noise. Only when the stress reaches a critical level, dislocations begin to form near the substrate surface and the resulting plots transform from linear to exponential form. Fig. 4 also demonstrates that, in comparison to singular surface, the vicinal angles (for $\theta$ $> 6^\circ$) strongly increase the critical thickness. However, for $\theta \leq 6^\circ$, the critical thickness is smaller than that of the singular surface.

The next interesting observation is that at a small vicinal angle $(3^\circ)$, the slope of the dependency $P$ versus $\varepsilon$ $(dP/d\varepsilon)$ in Fig. 4(b) is very large in comparison to the singular surface. However, it decreases with increasing vicinal angle $\theta$. The minimal misfit at which the dislocation formation was observed also increases with the increasing $\theta$. This behavior shows the decrease of the morphological instability and the dislocation formation with increasing vicinal angle. From the physical point of view, it can be explained by the fact that the steps serve as nucleation sites or places for the dislocations. The higher the number of steps in the simulation box, the smaller is the strain energy per step and smaller is the probability of the dislocation formation in grooves.

The anisotropy of the film affects the critical thickness in such a way that $H_c$ increases ($P$ decreases) in comparison to the isotropic system with the same vicinal angle. It means that the anisotropy of the film reduces the morphological instability and the defect formation in the systems with positive misfits. Since the anisotropy changes the principal lattice directions, it can be assumed that the geometrical factor of the dislocation formation associated with dislocation slip systems and the

![](./images/811070454709092352_8.jpg)

Fig. 5. The comparison of the inverse critical film thickness with the previous studies at (a) $\varepsilon>0$ (b) $\varepsilon<0$.

applied stress direction plays an important role in this particular scenario. The understanding of this behavior requires a detailed theoretical analysis in the future work.

In order to investigate the effect of noise on the critical thickness, we have carried out additional simulations with the noise $A_{noise}=1.2$ for isotropic singular and vicinal surfaces (see Fig. 5 (a)). The simulations performed with increasing noise result in larger values of $P$. The morphological instability increases and the plots become more uniform and close to linear. For the isotropic singular surface, the values are close to Elder and Grant (2004). For vicinal surfaces, the results deviate from the plots reported in Yu et al. (2011) for the same vicinal angles. This deviation might exist due to the different numerical methods used in the simulations in Yu et al. (2011) and the current work. The main points that are used in the simulations in Yu et al. (2011) and are different from the current works are the following: (i) an external potential was used in order to define the substrate; (ii) the numerical discretization was implemented using semi-implicit Fourier spectral method; and (iii) the initial perturbation of the step spacing was added. All of these points can influence the overall numerical noise in the system and cause the deviation of the results.

It is important to mention that for a singular surface the plot $P$ versus $\varepsilon$ remains linear independent of the noise level. At the same time, the plots for vicinal surfaces and anisotropic systems are nonlinear in most tests. However, after adding the noise they become more linear. It should be mentioned here that the dislocation formation in the anisotropic films cannot be a result of the different elastic constants in the film and the substrate (in the investigated systems, the elastic constants do not depend on the anisotropic parameter) so that it cannot explain the nonlinear behavior.

In order to investigate the thermodynamics of the dislocation formation in a quantitative way, we also calculated the free energy density $F$ and the free energy derivative $\partial F/\partial\phi$ during the film growth. Furthermore, the free energy in sections, $F_{k}$, and the free energy derivative in sections, $(\frac{\partial F}{\partial\phi})_{k}$, were calculated according to Eqs. (23) and (24). Average values were

![](./images/811070454709092352_9.jpg)

Fig. 6. The comparison of the free energy derivative of the dislocation formation for isotropic and anisotropic films with various vicinal angles $\theta$, $\varepsilon>0$.

![](./images/811070454709092352_10.jpg)

Fig. 7. The comparison of the section free energy for isotropic and anisotropic films with various vicinal angles $\theta$, $\varepsilon>0$.

estimated in the sections normal to the growth direction for a section of width $8\Delta y$:

$$
F_{k}=\sum_{i=1}^{N x} \sum_{j=8 k}^{8(k+1)-1} F_{i j}, \tag{23}
$$

$$
\left(\frac{\partial F}{\partial \phi}\right)_{k}=\sum_{i=1}^{N x} \sum_{j=8 k}^{8(k+1)-1}\left(\frac{\partial F}{\partial \phi}\right)_{i j}. \tag{24}
$$

Here, $k$ is the section number and $i,j$ are the grid indices.

The change of the free energy derivative at the critical thickness due to dislocation formation $\Delta\left(\frac{\partial F}{\partial \phi}\right)_{k}$ was estimated and plotted as a function of $\varepsilon$ for various values of $\theta$ in Fig. 6 for isotropic and anisotropic films. The resulting values were all positive which indicate that the formation of the dislocation leads to a stepwise increase in the free energy derivative. Since the derivative represents the growth velocity, one can state that the formation of the dislocation leads to an increase in the growth velocity, even more so, this increment is larger for the larger misfit. The corresponding section free energy, $F_{k}$, at the critical thickness is plotted in Fig. 7. The dependencies follow the curves for the inverse critical thickness $P$ in Fig. 4 (b). The section free energy decreases with increasing vicinal angles. Moreover, all curves for the vicinal surfaces lie below the curve for the singular surface. The curves of free energy derivative also correspond to the dependencies in Fig. 4 (b). One

![](./images/811070454709092352_11.jpg)

Fig. 8. Resulting microsctructures from numerical simulations performed for the vicinal angle 6.178° for (a) the isotropic and (b) anisotropic film lattice with $s_f=0.10825$. The simulation time $t=140$, $\varepsilon=-0.06$. The color bar represents the value of $\phi$. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

can see that the anisotropy of the films decreases the system energy and correspondingly affects the growth velocity, which increases strongly after the defect formation in the systems without anisotropy.

To define the critical thickness, we used the data from the time step where the most dislocations form and the disloca- tion positions are overgrown by 4 to 5millilitre layers. It was observed that with time the dislocations move to the surface and the distance between the dislocations and the substrate decreases. The average free energy density is evaluated at the same time as the critical thickness.

### 3.1.2. The system with negative misfit $\varepsilon < 0$

In case of negative misfit (a film in tension), the formation of the dislocation was observed at smaller film thicknesses in comparison to the positive misfits. An example of the resulting microstructures obtained from numerical simulations is shown in Fig. 8. It corresponds to the isotropic and anisotropic films with $\theta=6.178^{\circ}$, $s_f=0.108$, and $\varepsilon=-0.06$.

The critical thickness of the dislocation formation $H_c$ and the inverse critical thickness $P$ as a function of the misfit for the isotropic and anisotropic films with the corresponding vicinal surface angles are shown in Fig. 9. The results for a singular surface,i.e., $\theta=0$ fully corresponds to Ref. (Elder and Grant, 2004). The dependence of $P$ versus $\varepsilon$ is nearly linear again which corresponds to Matthews-Blakeslee analytical expression. The slope $dP/d\varepsilon$ for the systems with vicinal angles $3^{\circ}$ and $6^{\circ}$ is larger than that of the singular surface. The critical misfit, where the dislocation formation is observed in the investigated system, increases with increasing $\theta$. The anisotropy of the films decreases the critical thickness $H_c$ and increases $P$ which is opposite to the trends seen for the systems with the positive misfit. It can also be observed in Fig. 9 (b) that for the vicinal surface angles $\theta<6^{\circ}$, the inverse critical thickness is larger and for the angles $\theta>6^{\circ}$ the inverse critical thickness is smaller than for the singular surface (black cycles). This is a common effect for both positive and negative misfits (see Section 3.1.1). It can be explained by the influence of the interstep distance on the stress-induced morphological instability through the formation of grooves at the step kinks and a redistribution of the strain energy between the steps.

A comparison with previous reported studies in Fig. 5(b) shows that the $P$ versus $\varepsilon$ plot for the singular surface is close to the results in Elder and Grant (2004). It is also an interesting observation that the plot for $\theta=6^{\circ}$ is close to the plot in Yu et al. (2011) for positive misfit.

The change of the free energy derivative at the critical thickness due to dislocation formation is plotted as a function of the misfit in Fig. 10. The free energy derivative is smaller for smaller $P$ that is in agreement with previous observations for the positive misfit. The section free energy at the critical thickness is plotted in Fig. 11. The free energy decreases with increasing angle and is larger for the anisotropic systems that in general corresponds to the behavior of the inverse critical thickness in Fig. 9 (b). We can summarize that in the systems with negative misfit, the anisotropy of the films enhances the elastic energy and increases the increment of the growth velocity after the dislocation formation (increases the free energy derivative $\frac{\partial F}{\partial \phi}$).

Note that the question why the anisotropy decreases the critical thickness for the negative misfit and increases it for the positive misfit is open and a detailed theoretical analysis of this phenomenon is of advantage.

![](./images/811070454709092352_12.jpg)

Fig. 9. The resulting (a) critical film thickness $H_c$ and (b) inverse critical film thickness $P$ (b) for isotropic and anisotropic system with various vicinal angles $\theta$ as functions of $\varepsilon < 0$.

![](./images/811070454709092352_13.jpg)

Fig. 10. The comparison of the free energy derivative of the dislocation formation for isotropic and anisotropic films with various vicinal angles $\theta$, $\varepsilon < 0$.

![](./images/811070454709092352_14.jpg)

Fig. 11. The comparison of the section free energy for isotropic and anisotropic films with various vicinal angles $\theta$, $\varepsilon < 0$.

![](./images/811070454709092352_15.jpg)

Fig. 12. Resulting microsctructures from numerical simulations performed for (a) the vicinal angle of $6.178^{\circ}$ and (b) $12.3^{\circ}$ for non-vicinal substrate surface.
The simulation time $t=560$, $\varepsilon=-0.10$. The color bar represents the value of $\phi$. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

### 3.2. Non-vicinal substrate surface (singular substrate)

In this section, we investigate the dislocation formation for the "Test YX" configuration, i.e., with the shear of the anisotropic film lattice in the $x$-direction and the film growth in the $y$-direction. The initial field has the form

$$
\phi=f_{0}+f_{1}\left[\cos \left(k_{1}(x+s y)\right) \cos \left(k_{2} y / \sqrt{3}\right)+1 / 2 \cos \left(2 k_{2} y / \sqrt{3}\right)\right]. \tag{25}
$$

The anisotropic film and the substrate have the parallel lattice planes and do not produce the incoherent substrate/film interface. Therefore, we do not need to rotate the lattice of the substrate and the non-vicinal growth for various lattice misfits and anisotropic parameters can be investigated without rotation (zero vicinal angle). The system domain size is chosen as $L_x\times L_y=720\times 1440$. The resulting microstructure is presented in Fig. 12.

The evaluated critical thickness $(H_c)$ and the inverse critical thickness $P$ as function of the misfit for isotropic and anisotropic films are shown in Fig. 13. Here, the strong increase of the critical thickness (decrease of $P$) is observed with the increasing anisotropic parameter. The larger the anisotropy, the larger is the critical misfit. This behavior demonstrates that the film anisotropy decreases the morphological instability and increases the ability to resist the dislocation formation.

At a critical misfit in the region [0.1;0.12], a strong increase of $P$ is observed which tends to the value of isotropic systems. The addition of the noise $A_{\text{noise}}=0.5$ increases the morphological instability and decreases the critical thickness. Therefore, the $P$ versus $\varepsilon$ curves become closer to the linear plot of the isotropic systems as shown in Fig. 13 by dashed lines.

The free energy density derivative as a function of $\varepsilon$ for various $s_f$ is plotted in Fig. 14 for the simulations performed without noise. The free energy derivative represents the accumulated strain energy before the dislocation formation. The resulting plots show that the accumulated strain energy of the system increases with increasing $\varepsilon$ for all values of $s_f>0$ and then reduces at a critical misfit to the isotropic plot (black solid line with cycles). This behavior demonstrates that for

![](./images/811070454709092352_16.jpg)

Fig. 13. The comparison of the inverse critical film thickness P for non-vicinal substrate surface.

![](./images/811070454709092352_17.jpg)

Fig. 14. Comparison of the free energy derivatives for non-vicinal substrate surface.

a flat substrate surface the stress-induced morphological instability and hence the dislocation formation are significantly reduced when noise is excluded from the system. Only for a large misfit when the accumulated strain energy exceeds a critical level, the instability appears and dislocations form close to the substrate surface so that for large misfits the free energy density derivative reduces abruptly to the isotropic level.

Therefore, we can summarize that for the anisotropic film growth on the non-vicinal substrate surfaces, the noise has a large influence on the dislocation formation. This can be physically explained by the small roughness of the growing interface and hence by reduced morphological instability.

## 4. Conclusion

The anisotropic PFC model has been applied to study the heteroepitaxial growth for various vicinal angles of the substrate surface and various anisotropic parameters of the film. The important conclusions of our numerical investigations can be summarized as follows:

- The critical thickness of the dislocation formation decreases with increasing misfit. Under the condition of adding noise, it mostly follows the Matthews-Blakeslee analytical expression (linear plot of $P$ versus $\varepsilon$) for isotropic and anisotropic films on both vicinal and non-vicinal substrate surfaces (Figs. 5 and 13). Without noise, the dependencies $P$ versus $\varepsilon$ for anisotropic systems are linear in the beginning and then break to the exponential form for larger values of misfits. This is due to the effects of noise on the morphological instability.

- The vicinal angles influence the critical thickness and the free energy in such a way that the critical thickness increases and the free energy decreases with increasing vicinal angle for angles $\theta > 6^\circ$ (Figs. 4 and 7). It can be explained by the redistribution of the strain energy between the steps.
- In case of systems with positive misfit, the anisotropy of films enhances the critical thickness and decreases the free energy, in comparison to the isotropic systems with the same vicinal angles (Figs. 4 and 7). However, on the contrary, in case of systems with positive misfit, the anisotropy reduces the critical thickness and increases the free energy (Figs. 9 and 7). The understanding of this effect requires further investigations and a detailed theoretical analysis of the influence of the anisotropy on the dislocation formation.
- In comparison to the singular surface, the systems with the vicinal surface and anisotropic films have smaller critical thickness for angles $\theta < 6^\circ$ and larger critical thickness for angles $\theta > 6^\circ$ for both positive and negative misfits (Figs. 4 and 9). This common effect shows the influence of the interstep distance on the stress-induced morphological instability.

## Acknowledgment

This work has been supported by the DFG through the DFG priority program SPP 1296.

## References

Asano, T., Ishiwara, H., 1983. Epitaxial relations in groupIIa fluoride/Si (111) heterostructures. Appl. Phys. Lett. 42, 517-519.

Berry, J., Grant, M., Elder, K.R., 2006. Diffusive atomistic dynamics of edge dislocations in two dimensions. Phys. Rev. E 73, 031609.

Biegalski, M.D., Vlahos, E., Sheng, G., Li, Y.L., Bernhagen, M., Reiche, P., Uecker, R., Streiffer, S.K., Chen, L.Q., Gopalan, V., Schlom, D.G., 2009. Influence of anisotropic strain on the dielectric and ferroelectric properties of SrTiO3 thin films on DyScO3 substrates. Phys. Rev. B 79 (22), 224117.

Chen, Z., Prosandeev, S., Luo, Z.L., Ren, W., Qi, Y., Huang, C.W., You, L., Gao, C., Kornev, I.A., Wu, T., Wang, J., 2011. Coexistence of ferroelectric triclinic phases in highly strained BiFeO 3 films. Phys. Rev. B 84, 094116.

Choudhary, M.A., Kundin, J., Emmerich, H., 2012. Phase-field crystal modeling of anisotropic material systems of arbitrary Poisson's ratio. Philos. Mag. Lett. 92 (9), 451-458.

Choudhary, M.A., Kundin, J., Emmerich, H., 2014. Misfit and dislocation nucleation during heteroepitaxial growth. Comp. Mater. Sci. 83, 451-458.

Choudhary, M.A., Li, D., Emmerich, H., Lwen, H., 2011. DDFT calibration and investigation of an anisotropic phase-field crystal model. J. Phys. 23, 265005.

Cogsweil, D.A., Bazant, M.Z., 2012. Orthorhombic crystal system coherency strain and the kinetics of phase separation in LiFePO. ACS Nano 6, 2215-2225.

Dong, L., Schnittker, J., Smith, R.W., Srolovitz, D.J., 1998. Stress relaxation and misfit dislocation nucleation in the growth of misfitting films: a molecular dynamics simulation study. J. Appl. Phys. 83 (1), 217-227.

Drummy, L.F., Martin, D.C., 2005. Thickness driven orthorhombic to triclinic phase transformation in pentacene thin films. Adv. Mater. 17, 903-907.

Elder, K.R., Grant, M., 2004. Modeling elastic and plastic deformations in nonequilibrium processing using phase field crystals. Phys. E 70, 051605.

Elder, K.R., Katakowski, M., Haataja, M., Grant, M., 2002. Modeling elasticity in crystal growth. Phys. Rev. Lett. 88, 245701.

Farrow, R.F.C., Sullivan, P.W., Williams, G.M., Jones, G.R., Cameron, D.C., 1981. MBEgrown fluoride films: a new class of epitaxial dielectrics. J. Vac. Sci. Technol. 19, 415-420.

Goryaeva, A.M., Carrez, P., Cordier, P., 2015. Modeling defects and plasticity in MgSiO3 post-perovskite: part 2-screw and edge [100] dislocations. Phys. Chem. Miner. 42 (10), 793-803.

Haataja, M., Müller, J., Rutenberg, A.D., Grant, M., 2001. Dynamics of dislocations and surface instabilities in misfitting heteroepitaxial films.. Phys. Rev. B 65 (3), 0354011-0354015.

Haataja, M., Müller, J., Rutenberg, A.D., Grant, M., 2002. Dislocations and morphological instabilities: continuum modeling of misfitting heteroepitaxial films. Phys. Rev. B 65 (16), 1654141-1654142.

Haeni, J.H., Irvin, P., Chang, W., Uecker, R., Reiche, P., Li, Y.L., Choudhury, S., Tian, W., Hawley, M.E., Craigo, B., Tagantsev, A.K., 2004. Room-temperature ferroelectricity in strained SrTiO3. Nature 430, 758-761.

Jiang, C., Srinivasan, S.G., Caro, A., Maloy, S.A., 2008. Structural, elastic, and electronic properties of Fe3C from first principles. J. Appl. Phys. 103, 043502.

Jonsdottir, F., Freund, L.B., 1995. Equilibrium surface roughness of a strained epitaxial film due to surface diffusion induced by interface misfit dislocations. Mech. Mater. 20, 337-349.

Kundin, J., Choudhary, M.A., 2016. Recent developments in anisotropic phase-field crystal modeling. Model. Sim. Mater. Sci. Eng. submitted.

Kundin, J., Choudhary, M.A., Emmerich, H., 2014. Bridging the phase-field and phase-field crystal approaches for anisotropic material systems. Eur. Phys. J.Special Topics 223, 363-372.

Manasevit, H.M., 1974. A survey of the heteroepitaxial growth of semiconductor films on insulating substrates. J. Cryst. Growth 22 (2), 125-148.

Matthews, J.W., Blakeslee, A.E., 1974. Defects in epitaxial multilayers: I. misfit dislocations. J. Cryst. Growth 27, 118.

Mourachkine, A., 2006. High-Temperature Superconductivity in Cuprates: The Nonlinear Mechanism and Tunneling Measurements. Springer Science & Busi- ness Media.

Ozkan, C.S., Nix, W.D., Gao, H., 1997. Strain relaxation and defect formation in heteroepitaxial Si1-xGex films via surface roughening induced by controlled annealing experiments. Appl. Phys. Lett. 70, 2247-2249.

Podmaniczky, F., Toth, G.I., Tegze, G., Granasy, L., 2015. Recent developments in modeling heteroepitaxy/heterogeneous nucleation by dynamical density functional theory. Mater. Trans. A 46A, 4908-4920.

Politi, P., Grenet, G., Marty, A., Ponchet, A., Villain, J., 2000. Instabilities in crystal growth by atomic or molecular beams. Phys. Rep. 324, 271-404.

Ruffini, A., Durinck, J., Colin, J., Coupeau, C., Grilhé, J., 2013. Buckling-induced dislocation emission in thin films on substrates. Int. J. Solids Struct. 50 (22-23), 3717-3722.

Stefanovic, P.M., Haataja, M., Provatas, N., 2006. Phase-field crystals with elastic interactions. Phys. Rev. Lett. 96, 225504.

Thayer, G.E., Ozolins, V., Schmidt, A.K., Bartelt, N.C., Asta, M., Hoyt, J.J., Chiang, S., Hwang, R.Q., 2001. Role of stress in thin film alloy thermodynamics: competition between alloying and dislocation formation. Phys. Rev. Lett. 86, 660-663.

Wang, H., Zeng, Y., Zhou, H., Kong, M., 1998. Triclinic deformation and anisotropic strain relaxation of an InAs film on a GaAs (001) substrate measured by a series of symmetric double crystal x-ray diffraction. J. Cryst. Growth 191 (4), 627-630.

Wu, C.C., Stach, E.A., Hull, R., 2007. Nanoscale mechanisms of misfit dislocation propagation in undulated $\text{Si}_{1-x}\text{Ge}_{x}$/Si(100) epitaxial thin films. Nanotech- nology 18, 165705-165711.

Yu, Y.-M., Backofen, R., Voigt, A., 2011. Morphological instability of heteroepitaxial growth on vicinal substrates: a phase-field crystal study. J. Cryst. Growth 318, 18-22.