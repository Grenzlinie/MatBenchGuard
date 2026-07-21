# Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials

Mengqi Zhang $^{a,*}$, Qian Wang $^{b,a}$, Zhanjiang Wang $^{a}$, Ning Zhao $^{c}$, Yanjun Peng $^{c}$

$^{a}$ Institute of Tribology Research, Southwest Jiaotong University, Chengdu, 610031, China
$^{b}$ Center for Surface Engineering and Tribology, Northwestern University, Evanston, IL 60201, USA
$^{c}$ School of Mechanical Engineering, Northwestern Polytechnical University, Xi'an 710072, China

---

## ARTICLE INFO

**Article history:**
Received 31 August 2018
Revised 12 March 2019
Available online xxx

**Keywords:**
Numerical equivalent inclusion method
Inhomogeneity
Particle clusters
Point contact

---

## ABSTRACT

Semi-analytical models (SAMs) have been developed to analyze contact problems efficiently, including those of inhomogeneous materials, based on the equivalent inclusion method. However, understanding the behavior of microscopic inhomogeneities requires SAMs of even higher efficiency. This study builds a new semi-analytical model for high-speed simulations of contacts of materials containing distributed particles of sizes orders of magnitude smaller than that of the contact radius. The domain decomposition method is applied to construct a two-level mesh set to implement multiscale computation. The macroscopic mesh uses homogenized elements that ensure a high computing efficiency in obtaining the contact pressure distribution as a boundary condition, whereas the material microstructures are modeled using the microscopic mesh, and thus the microscopic stress and strain are obtained. New influence coefficients are derived for eigenstress and eigenstrain calculations in both mesh levels and are used to calculate the eigenstress and equivalent eigenstrains. The new model is implemented to investigate the effects of particle clustering on the contact performances of composites.

© 2019 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Particles or fibers in a composite have material properties different from those of the matrix constituent and are generally referred to as inhomogeneities (Mura, 1987). In the last several decades, a number of modeling and numerical methods have been proposed to analyze the stress disturbances caused by inhomogeneities. Semi-analytical models have been proven efficient for solving the contact problems involving inhomogeneous materials. However, computational efficiency still remains as an issue when processing many distributed particles. This paper explores a more efficient numerical approach to reinforce semi-analytical modeling.

Many methods can model the contact of inhomogeneous materials. The finite element model (FEM) receives a wide application in analyzing material heterogeneities due to its advantages in versatility (Guan et al., 2017; Moghaddam et al., 2015, 2016; Paulson et al., 2015; Zhang et al., 2013; Harish et al., 2016); however, a computation domain much larger than the physical contact region is usually needed, which in turn incurs a long computation time. Analytical methods (Hori and Nemat-Nasser, 1993; Lu et al., 2013; Shodja and Sarvestani, 2001) require a much shorter computing time than does the FEM, but their applications are limited to certain special situations. These limitations stimulated the development of semi-analytical models for efficient and accurate solutions for mechanical problems (Chen et al., 2010; Liu and Wang, 2002; Harursampath et al., 2017a,b). In a semi-analytical model, arbitrarily shaped inhomogeneities and matrix materials are discretized into cuboidal elements of uniform stresses and strains. Based on the equivalent inclusion method (EIM) (Eshelby, 1957), discretized inhomogeneities can be replaced by inclusion elements with properly assigned eigenstrains that generate identical eigenstress fields. Then, the eigenstresses due to the inclusion elements are calculated, and their resultant contributions to elasticity at any point within the calculation zone can be resolved. The total stress fields are the superposition of eigenstresses and the stress field of the otherwise homogeneous material. Typical semi-analytical models are found in the work by Jacq et al. (2002), Chen et al. (2008b) and Zhou et al. (2015, 2012), and the last two focus on elastic contact-inhomogeneity problems. In recent years, several groups have reported semi-analytical models capable of handling problems involving coupled stress fields in inhomogeneous materials and beyond. For example, Amuzuga et al. (2016) and Zhang et al. (2017) used an elastoplastic contact model to investigate the effect of inhomo-

* Corresponding author.
E-mail address: mengqi.zhang@mail.nwpu.edu.cn (M. Zhang).

https://doi.org/10.1016/j.ijsolstr.2019.03.019
0020-7683/© 2019 Elsevier Ltd. All rights reserved.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

<table><tbody><tr><td colspan="2">Nomenclature</td></tr>
<tr><td>$a_0$</td><td>Hertz contact radius (mm)</td></tr>
<tr><td>$C_{ijkl}, C_{ijkl}^\ast$</td><td>elastic moduli of matrix and inhomogeneities (MPa)</td></tr>
<tr><td>$dx, dy, dz$</td><td>element sizes of microscopic level elements along $x$, $y$ and $z$ direction, respectively</td></tr>
<tr><td>$err$</td><td>relative errors between two results</td></tr>
<tr><td>$I_{ijkl}$</td><td>identity matrix</td></tr>
<tr><td>$n$</td><td>number of inhomogeneity elements in a microscopic level mesh</td></tr>
<tr><td>$nx, ny, nz$</td><td>total element number of microscopic mesh level along $x$, $y$ and $z$ direction, respectively</td></tr>
<tr><td>$Nx, Ny, Nz$</td><td>total element number of macroscopic mesh level along $x$, $y$ and $z$ direction, respectively</td></tr>
<tr><td>$P_0$</td><td>Hertz contact pressure (MPa)</td></tr>
<tr><td>$p$</td><td>contact pressure (MPa)</td></tr>
<tr><td>$S_{ijkl}$</td><td>influence coefficients, for calculating disturbance strain caused by eigenstrain</td></tr>
<tr><td>$T_{ijkl}$</td><td>influence coefficients, for calculating eigenstress caused by eigenstrain</td></tr>
<tr><td>$\alpha, \beta, \gamma, \xi, \eta, \vartheta$</td><td>element indices</td></tr>
<tr><td>$\Delta x, \Delta y, \Delta z$</td><td>element sizes of macroscopic level elements along $x$, $y$ and $z$ direction, respectively</td></tr>
<tr><td>$\varepsilon_{ij}$</td><td>strain disturbance caused by inhomogeneities</td></tr>
<tr><td>$\varepsilon_{ij}^0$</td><td>strain corresponding to the summation of homogeneous stresses</td></tr>
<tr><td>$\varepsilon_{ij}^\ast$</td><td>eigenstrain</td></tr>
<tr><td>$\nu$</td><td>Poisson's ratio</td></tr>
<tr><td>$\mu$</td><td>shear modules (MPa)</td></tr>
<tr><td>$\sigma_{ij}^0$</td><td>summation of homogeneous elastic and residual stresses (MPa)</td></tr>
<tr><td>$\sigma_{ij}^\ast$</td><td>eigenstress (MPa)</td></tr>
<tr><td colspan="2">Superscript</td></tr>
<tr><td>$L$</td><td>microscopic mesh level</td></tr>
<tr><td>$U$</td><td>macroscopic mesh level</td></tr>
<tr><td>$AVG$</td><td>average value</td></tr>
<tr><td colspan="2">Subscript</td></tr>
<tr><td>$I$</td><td>inhomogeneity</td></tr>
<tr><td>$M$</td><td>matrix</td></tr>
</tbody></table>

geneities on the distributions of plastic strain and residual stress; Wang et al. (2013a) and Dong et al. (2016) modeled inhomogeneities in partial slip contacts; and Wang et al. (2013c) studied the elastohydrodynamic lubrication of inhomogeneous materials.

The present semi-analytical model assumes that each computation element is homogeneous with uniform stress and strain distributions, implying that the size of an element must be reasonably smaller than an inhomogeneity. Because the distributed inhomogeneities in real materials can be very small, the computation mesh size should be even smaller. Thus, the computational burden, including the CPU time and memory usage, increases rapidly with the inhomogeneity number. Several potential solutions for handling the multiscale problem of inhomogeneous material contact analysis have been proposed.

(1) Improving the SAM efficiency by improving computation methods. For example, Zhou et al. (2016) proposed a mesh differential refinement scheme in which only the eigenstress field of a specific region is calculated, thus reducing the execution time. Apparently, this method loses its advantage for problems that require the stress field of the entire calculation zone, such as the determination of potential matrix yield points where the von Mises stress reaches the maximum. Wang et al. (2013b) tracked this issue via a parallel computation strategy, by dividing a large problem into smaller independent components and assigning them to multiple processors without sacrificing any computational accuracy. However, either method did not actually reduce the scale of a semi-analytical model, especially when considering materials containing distributed or clustered particles of very small size.

(2) Solving a contact problem locally. References Mura (1987) and Zhou et al. (2014b) indicate that the eigenstress caused by an inhomogeneity in matrix materials decreases rapidly with increasing distance from a point of interest to the particle. It appears that only a small portion of the material adjacent to an inhomogeneity must be modeled because the remainder is largely free from the inhomogeneity effects. In this approach, the calculation zone may not be sufficiently large to simulate the real contact between materials, and thus, the contact pressure is usually pre-assumed to follow Hertzian equations (Kabo, 2002; Moghaddam et al., 2014). Note that near-surface inhomogeneities may have a strong influence on contact pressure distributions (Leroux et al., 2010), and such an effect is related to the geometric and material properties of inhomogeneities. The Hertzian pressure assumption could be acceptable when the inhomogeneity disturbance to the contact is weak. However, when the inhomogeneities are close to the surface or the particle volume fraction is high, ignoring the contact pressure disturbance would lead to a notable error in the subsurface stress field. The root problem of this issue is that the effects of material microstructures on macroscopic properties are not well considered.

(3) Applying computational homogenization. The effective properties of an inhomogeneous material could be calculated based on its constituent geometries and microstructures, using analytical (Hashin and Shtrikman, 1962; Mori and Tanaka, 1973) or numerical methods (Zhou, 2012). The actual material could be homogenized and the microscopic heterogeneities could be ignored, thus reducing the scale of the model. However, the absence of microscopic stress fields, which should play an important role in the investigations of failure initiation, is the most significant defect of such approaches because the particles may act as the sites of fatigue-crack nucleation due to the highly localized stress concentrations there.

Generally speaking, the first two solutions provide microscopic results but may have a relatively low computational efficiency or low precision. The last solution offers good macroscopic results, but the localized stress information is missing. These deficiencies stimulate the present work on a multiscale computational scheme for strengthening the semi-analytical modeling approach using the equivalent inclusion method for analyzing the contact of materials containing distributed microscopic particles. Multiscale computing is implemented via a set of two-level meshes, which is enlightened by the multiscale methods in finite element modeling (Liu et al., 2016, 2018; Moore et al., 2014). The contact pressure is solved on the coarse mesh where the equivalent eigenstrains are determined using not only the contact-induced initial conditions but also the homogenized material microstructures, ensuring a high computational efficiency without losing the accuracy of the macroscopic results. The microscopic stress and strain fields are calculated in the fine mesh after the boundary conditions are obtained in the coarse mesh. The new model considers macroscopic properties and the microstructures of inhomogeneous materials and is thus more

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

advantageous than the existing semi-analytical models in material contact analyses.

## 2. Multiscale semi-analytical model for inhomogeneous materials

### 2.1. Model description

The semi-analytical method has been proved efficient in tackling contact problems of inhomogeneous materials. In the existing SAMs, arbitrarily shaped inhomogeneities and matrix are discretized into cuboidal elements. By applying the equivalent inclusion method, inhomogeneity elements are transformed to inclusions that contain properly assigned eigenstrains, followed by the eigenstress calculation. The interior of an element is assumed to be homogeneous; therefore, the size of the elements must be smaller than that of the smallest inhomogeneity in a material. In addition, the entire contact area should be modeled so that the coupling between the inhomogeneity-induced field and the contact pressure distribution can be considered. If the inhomogeneity is two or more orders of magnitude smaller than the radius of the contact area, a large number of elements are expected to model such a material in contact, leading to long computing time. In this work, a domain decomposition method (Yagawa et al., 1991; Hsiao and Wendland, 1991) is combined with a SAM via constructing a set of two-level meshes (macroscopic and microscopic mesh) to overcome this problem and facilitate multiscale computations, which should lead to reduce the CPU time without losing accuracy. This section discusses the general idea of the new method, including the theoretical background of SAMs for clarity and the construction of the two-meshes. This paper focuses on the contact between a rigid ellipsoidal indenter and an inhomogeneous half-space for simplicity in method description.

### 2.1.1. Theory background

#### 2.1.1.1. Contact pressure and elastic stress.
In conventional SAMs, the total stress at a point is the superposition of the contact-induced elastic stress and the eigenstress caused by inhomogeneities, i.e. $\sigma_{ij}=\sigma_{ij}^{E}+\sigma_{ij}^{*}$. The contact between surfaces is defined by the following compatibility conditions (the Greek letter subscripts in brackets are the indices for an individual element):

$$
\left\{
\begin{aligned}
\Delta x \cdot \Delta y \sum_{[\alpha, \beta] \in I_{g}} p_{[\alpha, \beta]} & =W \\
h_{[\alpha, \beta]} & =h_{[\alpha, \beta]}^{0}+u_{3[\alpha, \beta]}+u_{3[\alpha, \beta]}^{*}-\omega \\
p_{[\alpha, \beta]} \geq 0, \quad h_{[\alpha, \beta]} & =0 |[\alpha, \beta] \in I_{c} \\
p_{[\alpha, \beta]}=0, \quad h_{[\alpha, \beta]} & \geq 0 |[\alpha, \beta] \notin I_{c}
\end{aligned}
\right. \tag{1}
$$

where $\Delta x$ and $\Delta y$ are the sizes of element in the $x$- and $y$-direction, $\alpha, \beta$, the element indices, the total node number of the calculation zone along the $x$- and $y$-directions. Eq. (1) involves $W$, the total normal load, $p$, the contact pressure, $h$, the gap between the two surfaces, $\omega$, the 'rigid-body' motion between the two solids, $h^{0}$, the initial gap before loading, and $u_{3}$, the normal elastic surface displacement, as well as $u_{3}^{*}$, the normal surface displacement caused by eigenstrains. In addition, $I_{c}$ is the set of all nodes that are in contact while $I_{g}$ is the set of all nodes in the grid. Eq. (1) is solved using a single-loop iteration scheme based on the conjugate gradient method (CGM) (Polonsky and Keer, 1999; Jin et al., 2013).

The subsurface elastic stress field is expressed by the following form of discrete convolution:

$$
\sigma_{ij[\alpha, \beta, \gamma]}^{0}=\sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} D_{ij[\alpha-\xi, \beta-\eta, \gamma]} p_{[\xi, \eta]} \tag{2}
$$

where $D_{ij[\alpha-\xi, \beta-\eta, \gamma]}$ are the influence coefficients, referring to the value of elastic stress at element $[\alpha, \beta, \gamma]$ caused by a unit contact pressure at surface element $[\xi, \eta]$. Detailed expressions of $D_{ij}$ are given in the work of Liu and Wang (2002).

#### 2.1.1.2. Equivalent eigenstrain.
Using the equivalent inclusion method (EIM) (Mura, 1987), inhomogeneities are transformed to inclusions having proper eigenstrains, ensuring that the eigenstress caused by the inclusions are identical to those by the inhomogeneities. The consistency condition of the EIM, shown in Eq. (3), is enforced in all inhomogeneity elements (with the Greek letter subscripts in brackets as the indices for an individual element).

$$
C_{ijkl[\alpha, \beta, \gamma]}^{*}\left(\varepsilon_{kl}^{0}+\varepsilon_{kl[\alpha, \beta, \gamma]}\right)=C_{ijkl}\left(\varepsilon_{kl}^{0}+\varepsilon_{kl[\alpha, \beta, \gamma]}-\varepsilon_{kl[\alpha, \beta, \gamma]}^{*}\right) \tag{3}
$$

where $C_{ijkl}^{*}$ and $C_{ijkl}$ are the elastic module of the inhomogeneity and matrix material, respectively; $\varepsilon_{ij}^{0}$ is the elastic strain corresponding to the homogeneous stress field; $\varepsilon_{ij}^{*}$ is the equivalent eigenstrain; and $\varepsilon_{ij}$ is the disturbance strain. In Eq. (3), $C_{ijkl}^{*}$ and $C_{ijkl}$ are material constants, and $\varepsilon_{ij}$ is related to $\varepsilon_{ij}^{*}$ as $\varepsilon_{ij}=S_{ijkl}\varepsilon_{kl}^{*}$ (Mura, 1987); thus, the $\varepsilon_{ij}^{*}$ of an inhomogeneity element is depended on its $\varepsilon_{ij}^{0}$ value. Considering the linearity of Eq. (3), such correlation can be expressed as $\varepsilon_{ij}^{*}=A_{ijkl}\varepsilon_{kl}^{0}$, where $A_{ijkl}$ is a constant that related to material properties. For example, for the case of single inhomogeneity element (no interaction), $\varepsilon_{ij}^{*}=((\Delta C_{ijmn}S_{mnpq}+C_{ijpq})^{-1}\Delta C_{pqkl})\varepsilon_{kl}^{0}$ by refactoring Eq. (3) (where $\Delta C_{ijkl}=C_{ijkl}^{*}-C_{ijkl}$), then $A_{ijkl}=(\Delta C_{ijmn}S_{mnpq}+C_{ijpq})^{-1}\Delta C_{pqkl}$. However, the eigenstrain leads to surface eigen-displacement $u_{3}^{*}$, which is a component of the total surface gap $h$ (Eq. (1)), indicating that the eigenstrain $\varepsilon_{ij}^{*}$ affects the contact pressure, elastic stresses, and of course, $\varepsilon_{ij}^{0}$. An iterative method, shown below in Algorithm 1, should be applied to solve Eq. (3) by taking into account the coupling between the inhomogeneity effect and contact (Zhang et al., 2018) (superscripts $(i)$ or $(i-1)$ are indices of iteration steps):

#### 2.1.1.3. Eigenstress.
The eigenstress due to inhomogeneities is calculated with the following equation (Liu et al., 2012) after the equivalent eigenstrain, $\varepsilon_{ij}^{*}$, is determined:

$$
\begin{aligned}
\sigma_{ij[\alpha, \beta, \gamma]}^{*}= & \frac{-\mu}{4 \pi(1-\nu)}\left(\sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} \sum_{\vartheta=1}^{N z} T_{ijkl[\alpha-\xi, \beta-\eta, \gamma-\vartheta]}^{(0)} \varepsilon_{kl[\xi, \eta, \vartheta]}^{*}\right. \\
& +\sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} \sum_{\vartheta=1}^{N z} T_{ijkl[\alpha-\xi, \beta-\eta, \gamma+\vartheta]}^{(1)} \varepsilon_{kl[\xi, \eta, \vartheta]}^{*} \\
& +z \sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} \sum_{\vartheta=1}^{N z} T_{ijkl[\alpha-\xi, \beta-\eta, \gamma+\vartheta]}^{(2)} \varepsilon_{kl[\xi, \eta, \vartheta]}^{*} \\
& \left.+z^{2} \sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} \sum_{\vartheta=1}^{N z} T_{ijkl[\alpha-\xi, \beta-\eta, \gamma+\vartheta]}^{(3)} \varepsilon_{kl[\xi, \eta, \vartheta]}^{*}\right)
\end{aligned} \tag{4}
$$

where $\mu$ and $\nu$ are the shear modulus and Poisson's ratio of the matrix material, respectively; $z$ is the depth of an element $[\xi, \eta, \vartheta]$. $T_{ijkl}^{(0)}, T_{ijkl}^{(1)}, T_{ijkl}^{(2)}, T_{ijkl}^{(3)}$ are the influence coefficients, relating the eigenstress in a target element $[\alpha, \beta, \gamma]$ to a source element $[\xi, \eta, \vartheta]$ that contains a unit eigenstrain. The influence coefficients depend on element sizes and the properties of the matrix material; they maintain constant in a simulation and only need to be calculated once. Eq. (4) indicates that the eigenstress in an element is the collection of contributions from all elements that have non-zero eigenstrains. It contains one three-dimensional (3D) convolution (the first term) and three convolution-correlation combination terms. As described by references Liu et al. (2012) and

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

```
Algorithm 1 Elastic inhomogeneity-contact coupling algorithm (Zhang et al., 2018).
Initialization:
    $W, h^{0}, p=0, u_{3}=0, u_{3}^{*}=0$
Repeat:
    $h^{(i)} \leftarrow h^{(i-1)}, u_{3}^{*(i-1)}$
    $p^{(i)} \leftarrow W, h^{(i)}$
    $\varepsilon^{0(i)} \leftarrow p^{(i)}$
    $\varepsilon^{*(i)} \leftarrow \varepsilon^{0(i)}$
    $u_{3}^{*(i)} \leftarrow \varepsilon^{*(i)}$
Until:
    $|\varepsilon^{*(i)} - \varepsilon^{*(i-1)}| < tol$
Then:
    $\sigma^{*}=T * \varepsilon^{*(i)}, \sigma^{0}=D * p^{(i)}$
    $\sigma=\sigma^{0}+\sigma^{*}$
```
(1) Updating surface geometry by $u_{3}^{*}$ from the previous iteration step
(2) Calculating contact pressure distribution (Polonsky and Keer, 1999)
(3) Determining homogeneous elastic strain (Liu and Wang, 2002)
(4) Estimating equivalent eigenstrain under current $\varepsilon^{0}$
(5) Calculating surface eigen-displacement caused by current $\varepsilon^{*}$ (Liu et al., 2012)
(6) Calculating eigenstress (Liu et al., 2012) and elastic stress (Liu and Wang, 2002)
(7) Obtaining the total stress result

Liu and Wang (2005), the computation of 3D convolution can be accelerated by DC-FFT, while the convolution-correlation terms are evaluated by DC-FFT in the x- and y- directions and the discrete correlation and fast Fourier transform (DCR-FFT) algorithm in the z- direction (Liu et al., 2007; Chen et al., 2008a). Similarly, the surface eigen-displacement is determined by the following equation, by using the influence coefficients $G$:

$$
u_{3[\alpha, \beta, 0]}^{*}=-\frac{1}{2 \pi}\left(\sum_{\xi=1}^{N x} \sum_{\eta=1}^{N y} \sum_{\vartheta=1}^{N z} G_{3 k l[\alpha-\xi, \beta-\eta, \vartheta]} \varepsilon_{k l[\xi, \eta, \vartheta]}^{*}\right)
\tag{5}
$$

### 2.1.2. Construction of macro- and microscopic meshes
A two-level mesh set is needed in the new method. The construction of the meshes is stated in this section, while their relevance is discussed in Section 2.1.3. In the following, "element" refers to the basic unit of the discretization model. The stress and strain fields inside an element (for both micro- and macroscopic elements) are assumed to be uniform and equal to the values at the element center. The term "mesh" means the discrete calculation zone that is composed by a number of elements.

The contact between a rigid ellipsoidal indenter and an inhomogeneous half-space is shown in the left of Fig. 1. The surfaces are smooth. Two assumptions are made about the inhomogeneous material: (1) the particles are randomly distributed, i.e. the probability that a particle appears in any location is identical; (2) the size of particles is much smaller than that of the contact area.

A material of size $L x \times L y \times L z$ is selected as the calculation zone. The surface area of the calculation zone should be at least two times the contact area where non-zero contact pressure is present to allow the DC-FFT implementation. The calculation zone is discretized into $N x \times N y \times N z$ homogenized macroscopic elements, as shown in the middle of Fig. 1. The origin of the coordinate system coincides with the center of contact, and the z-axis points to the depth. The size of a macroscopic element is larger than that of inhomogeneities, thus there should be a plurality of particles in the region where a macroscopic element is located. However, the particles are not modeled in the macroscopic mesh; the existence of particles is reflected by the equivalent properties of macroscopic elements (Section 2.3). All the macroscopic elements share identical size and properties in one specific simulation. The macroscopic mesh is utilized to calculate contact pressure distributions and elastic stress fields; because the macroscopic mesh is homogeneous, a high-precision result can be obtained even by using a coarse mesh, implying a short time consumption over the macroscopic mesh. However, the macroscopic element should not be too small, otherwise fewer particles in one macroscopic element would cause strong randomness of the equivalent element properties in macroscopic elements obtained by homogenization. For all the cases involving randomly distributed particles, the edge length of the macroscopic elements is set to be at least ten times the radius of particles.

Each macroscopic element is decomposed into a microscopic mesh to model tiny particles, as shown in the right of Fig. 1. The edge length, $dx$, of a microscopic mesh is related to that of the macroscopic element with $n x \times d x=\Delta x$. A discretized particle is composed of several inhomogeneity microscopic elements, as indicated by the sketch in the top right of Fig. 1. Particles are assumed to be randomly distributed in a microscopic mesh; the volume fraction of particles in a microscopic mesh should be the same as that in the original inhomogeneous material. The microscopic meshes are independent of each other and have the same particle distribution and material properties, ensuring the consistency of macroscopic elements. The microscopic meshes are used to obtain the detailed stress and strain fields in the inhomogeneities and adjacent matrix materials.

### 2.1.3. Correlation between macro- and microscopic meshes
A microscopic mesh containing $n$ inhomogeneities is shown in the left of Fig. 2. Applying the EIM, the inhomogeneities are transformed to inclusions with eigenstrains which cause surface displacements and eigenstresses, while the macroscopic mesh uses homogenized elements (the stress and strain fields inside a macroscopic element are assumed to be uniform and equal to the values at the element center). In the new method, the macroscopic mesh is dedicated for contact modeling. Therefore, **the key issue of the proposed method is**: under a remote strain $\varepsilon_{i j}^{0}$, a macroscopic element should yield an equivalent eigenstrain $\varepsilon_{i j}^{*(m a)}$ and cause the same surface displacement and eigenstress as those induced by the inclusions in the corresponding microscopic mesh under the same $\varepsilon_{i j}^{0}$. Then, the coupling between inhomogeneities and contact can be taken into account even by implementing a coarse macroscopic mesh. This should notably shorten the execution time for determining the resultant contact pressure distribution.

Two modifications of the conventional SAMs are required to achieve the above expectations:
(1) Building a new coefficient connecting the current initial strain and equivalent eigenstrain as $\varepsilon_{i j}^{*(m a)}=A_{i j k l}^{\prime} \varepsilon_{k l}^{0}$ ($A_{i j k l}^{\prime}$ is constant for all macroscopic elements in a simulation). Such coefficient is commonly obtained by refactoring the EIM consistency equation, and it depends on the elastic moduli of inhomogeneity and matrix material; however, in the new $A_{i j k l}^{\prime}$, the distribution of particles must be involved. The derivation of $A_{i j k l}^{\prime}$ are shown in Section 2.3.1.
(2) Building new influence coefficients for eigen-displacement and eigenstress calculations on the macroscopic mesh. The new influence coefficients should consider the material microstructures but follow the expressions in Eqs. (4) and (5), and each macroscopic element should be the same (i.e. all the microscopic meshes should have identical properties) to ensure the identity of influence coefficients. This also facilitate the use of the DC-FFT algorithm for rapid eigen-displacement and eigen-

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

![](./images/812791689356771330_1.jpg)

Fig. 1. Contact involving an inhomogeneous material and schematics of the macro- and microscopic meshes for inhomogeneity treatments.

![](./images/812791689356771330_2.jpg)

Fig. 2. Schematics of a microscopic mesh and the corresponding equivalent macroscopic element.

stress processing. The influence coefficient derivations are given in Section 2.3.2.

After obtaining $A'_{ijkl}$ and the new influence coefficients, the iterative algorithm in Section 2.1.1 can be applied to solve the contact on the macroscopic mesh.

The detailed stress and strain fields in the inhomogeneities and their surrounding matrix material are calculated in the microscopic meshes after the contact problem is solved in the macroscopic mesh. The results from the macroscopic mesh are transferred to the microscopic meshes as the initial conditions. The calculations in the microscopic meshes have no effect on contact because the contact-inhomogeneity coupling has been taken into account in the macroscopic mesh.

### 2.2. Microscopic mesh

In this section, the calculations on microscopic meshes are discussed. The total stress at each microscopic element is the summation of initial stress $\sigma_{ij}^{0(mi)}$ and eigenstress $\sigma_{ij}^{*(mi)}$ caused by equivalent eigenstrains (the superscript "(mi)" refers to "microscopic").

#### 2.2.1. Calculation of equivalent eigenstrains

The methods for calculating the equivalent eigenstrains in a microscopic mesh includes: (1) setting up the initial values, (2) constructing the consistency equations of the equivalent inclusion method, and (3) numerical implementation of EIM. Superscripts 'mi' and 'ma' are used to distinguish the items (such as eigenstress, equivalent eigenstrain, etc.) in the micro- and macroscopic meshes,

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

respectively. The numbers or letters in the subscript are element indices. For example, $\varepsilon_{ij[l]}^{(0)(mi)}$ means equivalent eigenstrain in the $l^{\text{th}}$ element in the current microscopic mesh.

Consider a microscopic mesh space, as shown in the right of Fig. 1, that contains $n$ cuboidal inhomogeneity elements numbered as $\Omega_1...\Omega_l...\Omega_J...\Omega_n$. Only inhomogeneity elements are indexed here because the equivalent eigenstrains of the matrix elements are zero and are ignored in the equation set. Using the equivalent inclusion method, inhomogeneities are transformed to inclusions that have properly assigned eigenstrains. The consistency condition shown in Eq. (6) is enforced in each inhomogeneity element to ensure that the eigenstresses induced by the equivalent inclusions is identical to those by the inhomogeneities.

$$
\begin{aligned}
C_{ijkl[I]}^{*}\left(\varepsilon_{kl[I]}^{0(mi)}+\varepsilon_{kl[I]}^{(mi)}\right) &= C_{ijkl}\left(\varepsilon_{kl[I]}^{0(mi)}+\varepsilon_{kl[I]}^{(mi)}-\varepsilon_{kl[I]}^{*(mi)}\right) \text{ in } \Omega_I, \\
I &= 1,2,\dots,n
\end{aligned} \tag{6}
$$

The total stress or strain of a macroscopic element is transferred to the corresponding microscopic mesh as the initial values for the determination of equivalent eigenstrains, and the distributions of the initial stress and strain in a microscopic mesh are set to be uniform and are constants while solving for equivalent eigenstrains, as shown in Eq. (7).

$$
\left\{
\begin{aligned}
\sigma_{ij[I]}^{0(mi)} &= \sigma_{ij}^{(ma)} \\
\varepsilon_{ij[I]}^{0(mi)} &= \varepsilon_{ij}^{(ma)}
\end{aligned}
\right. I=1,2,\dots,n \tag{7}
$$

Note that both Eqs. (3) and (6) are consistency conditions of the equivalent inclusion method, and their differences are stated here. In Eq. (3), the elastic strain $\varepsilon_{ij}^{0}$ and equivalent eigenstrain $\varepsilon_{ij}^{*}$ (the unknown) have an implicit and nonlinear correlation because of the coupling between inhomogeneities and the contact pressure distribution (Zhang et al., 2018), so that only the numerical approaches that do not require derivatives of the equation set are useable for solving Eq. (3). Calculating the derivatives of Eq. (3) numerically might be an option, but it consumes considerable computing time. However, in Eq. (6), initial value $\varepsilon_{ij}^{0(mi)}$ remains constant and independent of equivalent eigenstrains. Therefore, Eq. (6) is explicit and linear, as shown in the following paragraphs. This section demonstrates how to construct this linear equation and, especially, only nonzero terms are involved.

All the inhomogeneity elements in the microscopic mesh contribute to the disturbance strain in element $\Omega_I$ as $\varepsilon_{ij[I]}^{(mi)}=\sum_{J=1}^{n}S_{ijkl[I,J]}^{(mi)}\varepsilon_{kl[J]}^{*(mi)}$ (Zhou et al., 2014a), where tensors $S_{ijkl[I,J]}^{(mi)}$ are constants and relate the eigenstrain in element $\Omega_J$ to the disturbance strain of element $\Omega_I$. Eq. (6) becomes the following:

$$
\begin{aligned}
& C_{ijkl[I]}^{*}\left(\varepsilon_{kl[I]}^{0(mi)}+\sum_{J=1}^{n}S_{klmn[I,J]}^{(mi)}\varepsilon_{mn[J]}^{*(mi)}\right) \\
& = C_{ijkl}\left(\varepsilon_{kl[I]}^{0(mi)}+\sum_{J=1}^{n}S_{klmn[I,J]}^{(mi)}\varepsilon_{mn[J]}^{*(mi)}-\varepsilon_{kl[I]}^{*(mi)}\right) \text{ in } \Omega_I, \\
& I=1,2,\dots,n
\end{aligned} \tag{8}
$$

Mathematically, $S_{ijkl[I,J]}^{(mi)}$ is obtained from influence coefficient $T_{ijkl[I,J]}^{(mi)}$ of the half-space eigenstress from Eq. (12) as:

$$
\left\{
\begin{aligned}
S_{ijkl[I,J]}^{(mi)} &= C_{ijmn}^{-1}T_{mnkl[I,J]}^{(mi)} + I_{ijkl} (I=J) \\
S_{ijkl[I,J]}^{L} &= C_{ijmn}^{-1}T_{mnkl[I,J]}^{(mi)} (I \neq J)
\end{aligned}
\right. \tag{9}
$$

where, $I_{ijkl}$ is the identity matrix, and,

$$
\begin{aligned}
T_{ijkl[I,J]}^{(mi)} &= \frac{-\mu}{4\pi(1-\nu)}\bigg( T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}-\vartheta^{(mi)}}]}^{(0)(mi)} \\
&\quad + T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}+\vartheta^{(mi)}}]}^{(1)(mi)} \\
&\quad + zT_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}+\vartheta^{(mi)}}]}^{(2)(mi)} \\
&\quad + z^2T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}+\vartheta^{(mi)}}]}^{(3)(mi)} \bigg)
\end{aligned} \tag{10}
$$

Detailed closed-form expressions for influence coefficients $T_{ijkl}^{(0)(mi)}, T_{ijkl}^{(1)(mi)}, T_{ijkl}^{(2)(mi)}, T_{ijkl}^{(3)(mi)}$ can be found in Liu et al. (2012), which only depend on the distance between the source and target element, matrix material properties, and element sizes, and they remain constant once the discretization of a microscopic mesh is completed. Therefore, the equivalent eigenstrain, $\varepsilon^{*(mi)} = [\varepsilon_{ij[1]}^{*(mi)}, \dots, \varepsilon_{ij[n]}^{*(mi)}]^T$, is the only unknown in Eq. (8), and it can be obtained by solving the linear equation set in Eq. (11) in the form $\mathbf{A}\boldsymbol{\varepsilon}^{*} = \mathbf{B}$ either analytically or numerically, including but not limited to the $LU$ decomposition scheme, the conjugate gradient method (CGM)[27], or the fixed-point iteration method (Zhang et al., 2018).

$$
\begin{aligned}
\mathbf{A}\boldsymbol{\varepsilon}^{*} &= \mathbf{B} \\
\mathbf{A} &= \begin{bmatrix}
\mathbf{a}_{[1,1]} & \dots & \mathbf{a}_{[1,J]} & \dots & \mathbf{a}_{[1,n]} \\
\vdots & \ddots & & & \vdots \\
\mathbf{a}_{[I,1]} & & \mathbf{a}_{[I,J]} & & \vdots \\
\vdots & & & \ddots & \vdots \\
\mathbf{a}_{[n,1]} & & & & \mathbf{a}_{[n,n]}
\end{bmatrix} \\
\mathbf{B} &= \begin{bmatrix}
\mathbf{b}_{[1]} & \dots & \mathbf{b}_{[I]} & \dots & \mathbf{b}_{[n]}
\end{bmatrix}^T
\end{aligned} \tag{11}
$$

where
$$
\begin{aligned}
\mathbf{a}_{[I,J]} &= \left(C_{ijkl[I]}^{*}-C_{ijkl}\right)S_{klmn[I,J]}^{(mi)} + C_{ijmn} (I=J) \\
\mathbf{a}_{[I,J]} &= \left(C_{ijkl[I]}^{*}-C_{ijkl}\right)S_{klmn[I,J]}^{(mi)} (I \neq J) \\
\mathbf{b}_{[I]} &= \left(C_{ijkl}-C_{ijkl[I]}^{*}\right)\varepsilon_{kl}^{0(mi)}
\end{aligned}
$$

### 2.2.2. Calculations of eigenstresses

This section addresses the eigenstresses in a microscopic mesh, which are induced by the eigenstrains within the same calculation zone. The influence coefficient refers to the eigenstress in a target element caused by the source element containing a unit eigenstrain, as a function of the distance between the source and target element, matrix material properties, and element size. It remains constant for one discretization of the microscopic mesh. The influence coefficients used for the eigenstress calculation in microscopic meshes are identical to those in the conventional models. The eigenstress of a microscopic element, indexed by $\alpha^{(mi)},\beta^{(mi)},\gamma^{(mi)}$, can be expressed as the sum of contributions from all elements in this microscopic mesh:

$$
\begin{aligned}
\sigma_{ij[{\alpha^{(mi)},\beta^{(mi)},\gamma^{(mi)}}]}^{*(mi)} &= \frac{-\mu}{4\pi(1-\nu)}\bigg( \sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} \\
&T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}-\vartheta^{(mi)}}]}^{(0)(mi)} \varepsilon_{kl[{\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}}]}^{*(mi)} \\
&+ \sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} \\
&T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}+\vartheta^{(mi)}}]}^{(1)(mi)} \varepsilon_{kl[{\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}}]}^{*(mi)} \\
&+ z \sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} \\
&T_{ijkl[{\alpha^{(mi)}-\xi^{(mi)},\beta^{(mi)}-\eta^{(mi)},\gamma^{(mi)}+\vartheta^{(mi)}}]}^{(2)(mi)} \varepsilon_{kl[{\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}}]}^{*(mi)}
\end{aligned}
$$

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

$$
\begin{aligned}
& +z^{2} \sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} \\
& \left.T_{i j k l\left[\alpha^{(m i)}-\xi^{(m i)}, \beta^{(m i)}-\eta^{(m i)}, \gamma^{(m i)}+\vartheta^{(m i)}\right]}^{(3)(m i)} \varepsilon_{k l\left[\xi^{(m i)}, \eta^{(m i)}, \vartheta^{(m i)}\right]}^{*(m i)}\right)
\end{aligned}
$$

where $\mu$ and $\nu$ are the shear modulus and Poisson's ratio of the matrix material, respectively; $z$ is the depth of source element $\xi^{(m i)}, \eta^{(m i)}, \vartheta^{(m i)}$; and $n x, n y$, and $n z$ are the number of elements in the microscopic mesh along the $x$-, $y$ - and $z$-directions, respectively. Detailed expressions for the influence coefficients $T_{i j k l}^{(0)(m i)}, T_{i j k l}^{(1)(m i)}, T_{i j k l}^{(2)(m i)}, T_{i j k l}^{(3)(m i)}$ can be found in Liu et al. (2012). The discrete convolution and correlations in Eq. (12) are executed efficiently using the FFT (DC-FFT) algorithm in Liu and Wang (2002) and Liu et al. (2000) and the parallel computation method in Wang et al. (2013b).

### 2.3. Macroscopic mesh

The macroscopic elements are used to replace the original material that contains distributed particles. Therefore, a macroscopic element and the corresponding inhomogeneous material should provide a same amount of equivalent eigenstrain under an external loading, and they should cause identical eigenstress and surface eigen-displacement in the half-space subjected to the same equivalent eigenstrain. Therefore, the influence of inhomogeneities on the contact can be considered in the macroscopic elements, ensuring the accuracy of contact pressure results. The coefficients for eigenstress and equivalent eigenstrain calculations in the macroscopic elements are derived in this section.

#### 2.3.1. Calculation of equivalent eigenstrains

The equivalent eigenstrain in a macroscopic element equals the
$$
\boldsymbol{\varepsilon}_{x x}^{*(m i)}=\left[\begin{array}{c}
\varepsilon_{x x[1]}^{*(m i)} \\
\varepsilon_{x x[2]}^{*(m i)} \\
\vdots \\
\varepsilon_{x x[n]}^{*(m i)}
\end{array}\right]=\left[\begin{array}{cccccc}
A_{(1,1)}^{-1} & \cdots & A_{(1,6)}^{-1} & A_{(1,7)}^{-1} & \cdots & A_{(1,12)}^{-1} \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
A_{(7,1)}^{-1} & \cdots & A_{(7,6)}^{-1} & A_{(7,7)}^{-1} & \cdots & A_{(7,12)}^{-1} \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
A_{(6 n-5,1)}^{-1} & \cdots & A_{(6 n-5,6)}^{-1} & A_{(6 n-5,7)}^{-1} & \cdots & A_{(6 n-5,12)}^{-1}
\end{array} \vdots \cdots \vdots \begin{array}{cccc}
A_{(1,6 n-5)}^{-1} & \cdots & A_{(1,6 n)}^{-1} \\
\cdots & \cdots & \cdots \\
A_{(7,6 n-5)}^{-1} & \cdots & A_{(7,6 n)}^{-1} \\
\vdots & & \vdots \\
A_{(6 n-5,6 n-5)}^{-1} & \cdots & A_{(6 n-5,6 n)}^{-1}
\end{array}\right] \times\left[\begin{array}{c}
\Delta C_{i j k l[1]} \\
\Delta C_{i j k l[I]} \\
\vdots \\
\Delta C_{i j k l[n]}
\end{array}\right] \times\left[\begin{array}{c}
\varepsilon_{x x}^{0(m i)} \\
\varepsilon_{y y}^{0(m i)} \\
\vdots \\
\varepsilon_{z z}^{0(m i)} \\
\varepsilon_{y z}^{0(m i)} \\
\varepsilon_{x z}^{0(m i)} \\
\varepsilon_{x y}^{0(m i)}
\end{array}\right]
$$

average value of the equivalent eigenstrains $\left(\varepsilon_{i j}^{* A V G}\right.$ in Eq. (21)) of the corresponding microscopic mesh, which is required by the eigenstress calculation, to be stated later in Section 2.3.2. Therefore, the derivations in this section begin with the calculation of the equivalent eigenstrains using the microscopic mesh, where the equivalent eigenstrains, $\varepsilon^{*(m i)}=\left[\varepsilon_{i j[1]}^{*(m i)}, \ldots, \varepsilon_{i j[n]}^{*(m i)}\right]^{T}$, are obtained by solving Eq. (11), with matrix $\boldsymbol{A}$ determined by the material properties and distributions of inhomogeneities, as indicated in Section 2.2.1. In the following, the numbers in the square brackets indicate the indices of inhomogeneity elements in a microscopic mesh, e.g. $\varepsilon_{x x[7]}^{*(m i)}$ is component $x x$ of equivalent eigenstrain in the 7th inhomogeneity element of a microscopic mesh; and the numbers in the round parenthesis are the indices of elements in a vector or matrix, e.g. $A_{(5,7)}$ is the element in the 5 th row and 7 th column of matrix $\boldsymbol{A}$ in Eq. (11).

Mathematically, the vector of the equivalent eigenstrains in Eq. (11) is
$$
\begin{aligned}
\boldsymbol{\varepsilon}^{*(m i)}= & {\left[\varepsilon_{i j[1]}^{*(m i)}, \varepsilon_{i j[2]}^{*(m i)}, \ldots, \varepsilon_{i j[n]}^{*(m i)}\right]^{T} } \\
= & {\left[\varepsilon_{x x[1]}^{*(m i)}, \varepsilon_{y y[1]}^{*(m i)}, \varepsilon_{z z[1]}^{*(m i)}, \varepsilon_{y z[1]}^{*(m i)}, \varepsilon_{x z[1]}^{*(m i)}, \varepsilon_{x y[1]}^{*(m i)}, \varepsilon_{x x[2]}^{*(m i)}, \varepsilon_{y y[2]}^{*(m i)},\right.} \\
& \varepsilon_{z z[2]}^{*(m i)}, \varepsilon_{y z[2]}^{*(m i)}, \varepsilon_{x z[2]}^{*(m i)}, \varepsilon_{x y[2]}^{*(m i)}, \ldots \\
& \left.\ldots \varepsilon_{x x[n]}^{*(m i)}, \varepsilon_{y y[n]}^{*(m i)}, \varepsilon_{z z[n]}^{*(m i)}, \varepsilon_{y z[n]}^{*(m i)}, \varepsilon_{x z[n]}^{*(m i)}, \varepsilon_{x y[n]}^{*(m i)}\right]^{T}
\end{aligned}
$$

Let $\Delta C_{i j k l[I]}=C_{i j k l}-C_{i j k l[I]}^{*}$; then, column vector $\boldsymbol{B}$ in Eq. (11) is refactored as:
$$
\begin{aligned}
\boldsymbol{B} & =\left[\begin{array}{c}
\Delta C_{i j k l[1]} \\
\vdots \\
\Delta C_{i j k l[I]} \\
\vdots \\
\Delta C_{i j k l[n]}
\end{array}\right] \times\left[\begin{array}{c}
\varepsilon_{x x}^{0(m i)} \\
\varepsilon_{y y}^{0(m i)} \\
\varepsilon_{z z}^{0(m i)} \\
\varepsilon_{y z}^{0(m i)} \\
\varepsilon_{x z}^{0(m i)} \\
\varepsilon_{x y}^{0(m i)}
\end{array}\right] \text { and, } \Delta C_{i j k l[I]} \\
& =\left[\begin{array}{cccccc}
\Delta C_{x x x x[I]} & \Delta C_{x x y y[I]} & \Delta C_{x x z z[I]} & \Delta C_{x x y z[I]} & \Delta C_{x x z x[I]} & \Delta C_{x x y[I]} \\
\Delta C_{y y x x[I]} & \Delta C_{y y y y[I]} & \Delta C_{y y z z[I]} & \Delta C_{y y z y[I]} & \Delta C_{y y z x[I]} & \Delta C_{y y x y[I]} \\
\Delta C_{z z x x[I]} & \Delta C_{z z y y[I]} & \Delta C_{z z z z[I]} & \Delta C_{z z y z[I]} & \Delta C_{z z z x[I]} & \Delta C_{z z x y[I]} \\
\Delta C_{y z x x[I]} & \Delta C_{y z y y[I]} & \Delta C_{y z z z[I]} & \Delta C_{y z y z[I]} & \Delta C_{y z z x[I]} & \Delta C_{y z x y[I]} \\
\Delta C_{z x x x[I]} & \Delta C_{z x y y[I]} & \Delta C_{z x z z[I]} & \Delta C_{z x y z[I]} & \Delta C_{z x z x[I]} & \Delta C_{z x x y[I]} \\
\Delta C_{x y x x[I]} & \Delta C_{x y y y[I]} & \Delta C_{x y z z[I]} & \Delta C_{x y y z[I]} & \Delta C_{x y z x[I]} & \Delta C_{x y x y[I]}
\end{array}\right]
\end{aligned}
$$

According to Eq. (11), the equivalent eigenstrains in a microscopic mesh can be expressed as $\boldsymbol{\varepsilon}^{*(m i)}=\boldsymbol{A}^{-1} \boldsymbol{B}$, where $\boldsymbol{A}^{-1}$ is the inverse of $\boldsymbol{A}$, and the dimension of $\boldsymbol{A}^{-1}$ is $6 n \times 6 n$. When calculating the average value of equivalent eigenstrain, taking $\varepsilon_{x x}^{* A V G}$ as an example, only the $x x$ component of the equivalent eigenstrain in this microscopic mesh is needed, which can be expressed as:

(15)

Let,
$$
\mathbf{C}=\left[\begin{array}{c}
\Delta C_{i j k l[1]} \\
\vdots \\
\Delta C_{i j k l[I]} \\
\vdots \\
\Delta C_{i j k l[n]}
\end{array}\right] \text { and, } \varepsilon^{0(m i)}=\left[\begin{array}{c}
\varepsilon_{x x}^{0(m i)} \\
\varepsilon_{y y}^{0(m i)} \\
\varepsilon_{z z}^{0(m i)} \\
\varepsilon_{y z}^{0(m i)} \\
\varepsilon_{x z}^{0(m i)} \\
\varepsilon_{x y}^{0(m i)}
\end{array}\right]
$$

where the dimension of matrix $\mathbf{C}$ is $6 n \times 6$. Then, the average value of $\varepsilon_{x x}^{*(m i)}$ is written as:
$$
\varepsilon_{x x}^{* A V G}=\frac{1}{n} \sum_{I=1}^{n} \varepsilon_{x x[I]}^{*(m i)}=\frac{1}{n} \sum_{\alpha=1}^{n} \sum_{\beta=1}^{6 n} \sum_{\gamma=1}^{6} \mathbf{A}_{(6 \alpha-5, \beta)}^{-1} \mathbf{C}_{(\beta, \gamma)} \varepsilon_{(\gamma)}^{0(m i)}
$$

which can be directly related to the initial strain $\varepsilon_{i j}^{0(m i)}$ by matrix $\boldsymbol{A}^{\prime}$. Note that in Eq. (17), the subscript $(\gamma)$ is element index of ma-

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

trix $\varepsilon^{0(mi)}$ but not a tensor notation.

$$
\begin{aligned}
{\left[\begin{array}{c}
\varepsilon_{x x}^{* A V G} \\
\varepsilon_{y y}^{* A V G} \\
\varepsilon_{z z}^{* A V G} \\
\varepsilon_{y z}^{* A V G} \\
\varepsilon_{x z}^{* A V G} \\
\varepsilon_{x y}^{* A V G}
\end{array}\right] } & =\frac{1}{n} ×\left[\begin{array}{llllll}
A_{(1,1)}^{\prime} & A_{(1,2)}^{\prime} & A_{(1,3)}^{\prime} & A_{(1,4)}^{\prime} & A_{(1,5)}^{\prime} & A_{(1,6)}^{\prime} \\
A_{(2,1)}^{\prime} & A_{(2,2)}^{\prime} & A_{(2,3)}^{\prime} & A_{(2,4)}^{\prime} & A_{(2,5)}^{\prime} & A_{(2,6)}^{\prime} \\
A_{(3,1)}^{\prime} & A_{(3,2)}^{\prime} & A_{(3,3)}^{\prime} & A_{(3,4)}^{\prime} & A_{(3,5)}^{\prime} & A_{(3,6)}^{\prime} \\
A_{(4,1)}^{\prime} & A_{(4,2)}^{\prime} & A_{(4,3)}^{\prime} & A_{(4,4)}^{\prime} & A_{(4,5)}^{\prime} & A_{(4,6)}^{\prime} \\
A_{(5,1)}^{\prime} & A_{(5,2)}^{\prime} & A_{(5,3)}^{\prime} & A_{(5,4)}^{\prime} & A_{(5,5)}^{\prime} & A_{(5,6)}^{\prime} \\
A_{(6,1)}^{\prime} & A_{(6,2)}^{\prime} & A_{(6,3)}^{\prime} & A_{(6,4)}^{\prime} & A_{(6,5)}^{\prime} & A_{(6,6)}^{\prime}
\end{array}\right] \\
& ×\left[\begin{array}{c}
\varepsilon_{x x}^{0(m i)} \\
\varepsilon_{y y}^{0(m i)} \\
\varepsilon_{z z}^{0(m i)} \\
\varepsilon_{y z}^{0(m i)} \\
\varepsilon_{x z}^{0(m i)} \\
\varepsilon_{x y}^{0(m i)}
\end{array}\right]
\end{aligned}
\qquad(18)
$$

where

$$
A_{(i, j)}^{\prime}=\sum_{\alpha=1}^{n} \sum_{\beta=1}^{6 n} \mathbf{A}_{(6 \alpha-6+i, \beta)}^{-1} \mathbf{C}_{(\beta, j)}
\qquad(19)
$$

Note that the initial stress and strain in each microscopic element are uniform and equal to the present total stress and strain in the corresponding macroscopic element, given in Eq. (7). The initial stress and strain are related by $\varepsilon_{i j}^{0(m i)}=\Delta C_{i j k l[\Omega]}^{*-1} \sigma_{k l}^{0(m i)}$ to obtain $\varepsilon_{i j}^{0(m i)}$.

### 2.3.2. Calculations of influence coefficients and eigenstresses

In this newly proposed semi-analytical model, the influence coefficients of the macroscopic elements depend on the distributed inhomogeneities described by the microscopic mesh. In this section, the source and target macroscopic elements are not the same element. Influence coefficients for eigenstress calculations have four components, i.e., $T_{i j k l}^{(0)}, T_{i j k l}^{(1)}, T_{i j k l}^{(2)}, T_{i j k l}^{(3)}$. The first section is convolution whereas the remaining three are correlations. The method for calculating new influence coefficients is universal for all sections; therefore, symbol $T_{i j k l\left[\alpha-\xi, \beta-\eta, \gamma \pm \vartheta\right]}$ is used in the following as a representative, where the Greek letter subscripts $\alpha^{(m a)}, \beta^{(m a)}, \gamma^{(m a)}$ and $\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}$ are the locations of centers of the target and source elements, respectively. As mentioned above, an influence coefficient is referred to the eigenstress value at the target element center, which is caused by the source element with unit eigenstrain. Thus, the eigenstress is expressed as the product of the influence coefficient and eigenstrain in the source element. A macroscopic source element is discretized into $n$ microscopic elements having nonzero eigenstrains. All the source elements in this microscopic mesh should contribute to the eigenstress in the target macroscopic element, which is expressed as:

$$
\begin{aligned}
& \sigma_{i j\left[\alpha^{(m a)}, \beta^{(m a)}, \gamma^{(m a)}\right]}^{*(m a)} \\
& \quad=\sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m i)}, \beta^{(m a)}-\eta^{(m i)}, \gamma^{(m a)} \pm \vartheta^{(m i)}\right]}^{(m i)} \varepsilon_{k l\left[\xi^{(m i)}, \eta^{(m i)}, \vartheta^{(m i)}\right]}^{*(m i)}
\end{aligned}
\qquad(20)
$$

An assumption is made that all the source elements in the microscopic mesh have identical equivalent eigenstrains equal to the average defined as $\varepsilon_{i j\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G}$, given below:

$$
\varepsilon_{i j\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G}=\frac{1}{n} \sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} \varepsilon_{i j\left[\xi^{(m i)}, \eta^{(m i)}, \vartheta^{(m i)}\right]}^{*(m i)}
\qquad(21)
$$

where $n$ is the number of the microscopic elements with nonzero eigenstrains. The rationality of this assumption is discussed in Section 2.3.3 by analyzing the dispersion of $\varepsilon_{i j[\xi, \eta, \vartheta]}^{* A V G}$ in practical problems.

Then, Eq. (20) becomes the following:

$$
\begin{aligned}
& \sigma_{i j\left[\alpha^{(m a)}, \beta^{(m a)}, \gamma^{(m a)}\right]}^{*(m a)} \\
& \quad=\left(\sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m i)}, \beta^{(m a)}-\eta^{(m i)}, \gamma^{(m a)} \pm \vartheta^{(m i)}\right]}^{(m i)}\right) \varepsilon_{k l[\xi, \eta, \vartheta]}^{* A V G}
\end{aligned}
\qquad(22)
$$

Eq. (22) equalizes an inhomogeneous macroscopic element to a homogeneous element, and the corresponding influence coefficients for the macroscopic element are calculated using Eq. (23).

$$
\begin{aligned}
& T_{i j k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \gamma^{(m a)} \pm \vartheta^{(m a)}\right]}^{(m a)} \\
& =\sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m i)}, \beta^{(m a)}-\eta^{(m i)}, \gamma^{(m a)} \pm \vartheta^{(m i)}\right]}^{(m i)}
\end{aligned}
\qquad(23)
$$

Note the following: (1) $T_{i j k l\left[\alpha-\xi, \beta-\eta, \gamma \pm \vartheta\right]}^{(m a)}$ in Eq. (23) is the sum of the contributions from all the inhomogeneity elements within one microscopic mesh; therefore, the microstructure, such as the size, shape and distribution of inhomogeneities, are linked to $T_{i j k l\left[\alpha-\xi, \beta-\eta, \gamma \pm \vartheta\right]}^{(m a)}$ which further affects the stresses and strains; and (2) the definition of the influence coefficients remains the same as usual, and $T_{i j k l\left[\alpha-\xi, \beta-\eta, \gamma \pm \vartheta\right]}^{(m a)}$ is the eigenstress in a target element caused by the unit eigenstrain in a source element. This treatment ensures the use of FFT technologies for calculating the macroscopic eigenstress field with the new influence coefficients when multiple source elements should be processed, i.e.,

$$
\begin{aligned}
\sigma_{i j\left[\alpha^{(m a)}, \beta^{(m a)}, \gamma^{(m a)}\right]}^{*(m a)}= & \frac{-\mu}{4 \pi(1-v)}\left(\sum_{\xi^{(m a)}=1}^{N x} \sum_{\eta^{(m a)}=1}^{N y} \sum_{\vartheta^{(m a)}=1}^{N z}\right. \\
& T_{i j k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \gamma^{(m a)}-\vartheta^{(m a)}\right]}^{(0)(m a)} \varepsilon_{k l\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G} \\
& +\sum_{\xi^{(m a)}=1}^{N x} \sum_{\eta^{(m a)}=1}^{N y} \sum_{\vartheta^{(m a)}=1}^{N z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \gamma^{(m a)}+\vartheta^{(m a)}\right]}^{(1)(m a)} \\
& \varepsilon_{k l\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G} \\
& +z \sum_{\xi^{(m a)}=1}^{N x} \sum_{\eta^{(m a)}=1}^{N y} \sum_{\vartheta^{(m a)}=1}^{N z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \gamma^{(m a)}+\vartheta^{(m a)}\right]}^{(2)(m a)} \\
& \varepsilon_{k l\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G} \\
& \left.+z^{2} \sum_{\xi^{(m a)}=1}^{N x} \sum_{\eta^{(m a)}=1}^{N y} \sum_{\vartheta^{(m a)}=1}^{N z} T_{i j k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \gamma^{(m a)}+\vartheta^{(m a)}\right]}^{(3)(m a)} \varepsilon_{k l\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G}\right)
\end{aligned}
\qquad(24)
$$

Eigenstrains also cause surface eigen-deformation, which is also required for the contact analysis. The format of the eigendisplacement calculation (Eq. (25)), expressed as the convolution between influence coefficients and eigenstrains, is identical to that of eigenstress calculations (Eq. (24)). The influence coefficients for the macroscopic elements, $G_{i k l}^{(m a)}$, are determined by following the same principle introduced in this section.

$$
\begin{aligned}
u_{i\left[\alpha^{(m a)}, \beta^{(m a)}, 0\right]}^{*(m a)}= & -\frac{1}{2 \pi}\left(\sum_{\xi^{(m a)}=1}^{N x} \sum_{\eta^{(m a)}=1}^{N y} \sum_{\vartheta^{(m a)}=1}^{N z}\right. \\
& \left.G_{i k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \vartheta^{(m a)}\right]}^{(m a)} \varepsilon_{k l\left[\xi^{(m a)}, \eta^{(m a)}, \vartheta^{(m a)}\right]}^{* A V G}\right)
\end{aligned}
\qquad(25)
$$

$$
\begin{aligned}
& G_{i k l\left[\alpha^{(m a)}-\xi^{(m a)}, \beta^{(m a)}-\eta^{(m a)}, \vartheta^{(m a)}\right]}^{(m a)} \\
& \quad=\sum_{\xi^{(m i)}=1}^{n x} \sum_{\eta^{(m i)}=1}^{n y} \sum_{\vartheta^{(m i)}=1}^{n z} G_{i k l\left[\alpha^{(m a)}-\xi^{(m i)}, \beta^{(m a)}-\eta^{(m i)}, \vartheta^{(m i)}\right]}^{(m i)}
\end{aligned}
\qquad(26)
$$

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

<table>
<caption>Table 1<br>Modeling parameters and material properties used in examples (Figs. 3, 5 and 6).</caption>
<thead>
<tr>
<th>Item</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hertzian contact radius ($a_0$)</td>
<td>0.1 mm</td>
</tr>
<tr>
<td>Hertzian contact pressure ($P_0$)</td>
<td>2350 MPa</td>
</tr>
<tr>
<td>Sizes of the calculation zone ($x, y, z$)</td>
<td>[$-1.28a_0, 1.28a_0$] [$-$1.28$a_0$, 1.28$a_0$] [0, 2.56$a_0$]</td>
</tr>
<tr>
<td>Location of source element</td>
<td>$(0, 0, 0.24a_0)$</td>
</tr>
<tr>
<td>Element numbers in the macroscopic mesh ($Nx, Ny, Nz$)</td>
<td>32,32,32</td>
</tr>
<tr>
<td>Element numbers in the microscopic mesh ($nx, ny, nz$)</td>
<td>16,16,16</td>
</tr>
<tr>
<td>Edge length of the macroscopic elements ($\Delta x = \Delta y = \Delta z$)</td>
<td>$8 × 10^{-2}a_0$</td>
</tr>
<tr>
<td>Edge length of the microscopic elements ($dx = dy = dz$)</td>
<td>$5 × 10^{-3}a_0$</td>
</tr>
<tr>
<td>Edge length of the cuboidal inhomogeneities</td>
<td>$5 × 10^{-3}a_0$</td>
</tr>
<tr>
<td>Volume ratio of inhomogeneities in a microscopic mesh ($vol\%$)</td>
<td>5%</td>
</tr>
<tr>
<td>Young's modulus ratio ($E_I/E_M$)</td>
<td>4.0</td>
</tr>
<tr>
<td>Poisson's ratio of the inhomogeneities ($\nu_I$)</td>
<td>0.3</td>
</tr>
<tr>
<td>Poisson's ratio of the matrix material ($\nu_M$)</td>
<td>0.3</td>
</tr>
</tbody>
</table>

### 2.3.3. Derivation of eigenstress due to the average-eigenstrain assumption

An assumption is made in Section 2.3.2 that all the inhomogeneity elements in one microscopic mesh space equals the average, $\varepsilon_{ij[\xi,\eta,\vartheta]}^{*AVG}$, calculated in Eq. (21). The deviation of the eigenstress due to this assumption is discussed as follows. Consider a microscopic mesh containing $n$ inhomogeneity elements. The true and approximate eigenstresses in target macroscopic element $[\alpha, \beta, \gamma]$, which are induced by source macroscopic element $[\xi, \eta, \vartheta]$, can be expressed as:

$$
\begin{aligned}
\sigma_{ij[\alpha,\beta,\gamma]}^{*True} &= \sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} T_{ijkl[\alpha-\xi^{(mi)},\beta-\eta^{(mi)},\gamma\pm\vartheta^{(mi)}]}^{(mi)} \varepsilon_{kl[\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}]}^{*(mi)} \\
\sigma_{ij[\alpha,\beta,\gamma]}^{*Approx} &= \sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} T_{ijkl[\alpha-\xi^{(mi)},\beta-\eta^{(mi)},\gamma\pm\vartheta^{(mi)}]}^{(mi)} \varepsilon_{kl[\xi,\eta,\vartheta]}^{*AVG}
\end{aligned} \tag{27}
$$

and the relative error of the eigenstress is:

$$
\begin{aligned}
err_{[\alpha,\beta,\gamma]}
&= \left| \frac{\sigma_{ij[\alpha,\beta,\gamma]}^{*True} - \sigma_{ij[\alpha,\beta,\gamma]}^{*Approx}}{\sigma_{ij[\alpha,\beta,\gamma]}^{*True}} \right| × 100\% \\
&= \left| \frac{\sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} T_{ijkl[\alpha-\xi^{(mi)},\beta-\eta^{(mi)},\gamma\pm\vartheta^{(mi)}]}^{(mi)} \left( \varepsilon_{kl[\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}]}^{*(mi)} - \varepsilon_{kl[\xi,\eta,\vartheta]}^{*AVG} \right)}{\sum_{\xi^{(mi)}=1}^{nx} \sum_{\eta^{(mi)}=1}^{ny} \sum_{\vartheta^{(mi)}=1}^{nz} T_{ijkl[\alpha-\xi^{(mi)},\beta-\eta^{(mi)},\gamma\pm\vartheta^{(mi)}]}^{(mi)} \varepsilon_{kl[\xi^{(mi)},\eta^{(mi)},\vartheta^{(mi)}]}^{*(mi)}} \right| × 100\%
\end{aligned} \tag{28}
$$

Apparently, the eigenstress errors depend on the difference between the true eigenstrains of inhomogeneity elements and the average value $\varepsilon_{ij}^{*AVG}$. Parametric studies are performed to investigate the dispersion of $\varepsilon_{ij}^{*(mi)}$ data. The modeling parameters and material properties are listed in Table 1 and the parameters are normalized by the Hertzian contact radius $a_0$ or Hertzian pressure $P_0$, for the matrix material. The eigenstrains in a microscopic mesh are calculated using the approach introduced in Section 2.2.1. The eigenstrains in the microscopic mesh (which correspond to the macroscopic element centered at $(0, 0, 0.24a_0)$) are plotted in Fig. 3 as an example. Note that there is only one source element in this case. In this example, the volume ratio of inhomogeneities is 5%, and the total number of the microscopic mesh is $16 × 16 × 16 = 4096$. Thus, the number of inhomogeneity elements is $n=204$. Fig. 3 shows that the datum points of eigenstrains are distributed within a narrow range around the mean values, implying that the dispersion of $\varepsilon_{ij}^{*(mi)}$ is very limited.

![](./images/812791689356771330_3.jpg)

Fig. 3. Equivalent eigenstrains of all the inhomogeneous elements in one microscopic mesh. The corresponding macroscopic element of this mesh is located at $(0,0,0.24a_0)$.

Considering that eigenstresses decrease rapidly with the increasing distance between the source and the target elements, only the eigenstresses in the six adjacent macroscopic target elements along $x$- and $z$-direction are plotted. The layout of the selected source and target elements is shown in Fig. 4. For example, when the source element locates at $(0, 0, 0.24a_0)$ and the element edge is $0.08a_0$, the eigenstresses of the target elements at $(0.08a_0, 0, 0.24a_0)$, $(0.16a_0, 0, 0.24a_0)$, $(0.24a_0, 0, 0.24a_0)$, as well as $(0, 0, 0.32a_0)$, $(0, 0, 0.40a_0)$, $(0, 0, 0.48a_0)$ are collected for the comparison. The true and approximate eigenstresses in the six macroscopic elements are plotted in Fig. 5, when the source element is centered at $(0, 0, 0.24a_0)$. The shear stresses in this sample case are close to zero, due to the small magnitudes of shear eigenstrains, as shown in Fig. 3. The difference between the true and approximate eigenstresses is small.

The effects of major factors, including the source element location, particle elastic moduli and volume fraction, on the eigenstress deviation is shown in Fig. 6. In the following, the von Mises stress is used, instead of the stress components, for result demonstrations, i.e. $err=|\sigma_{VM}^{*Ture}-\sigma_{VM}^{*Approx}|/\sigma_{VM}^{*Ture}×100\%$. The default parameter values in Table 1 are applied, if not specified in the figures. Within the current parameter ranges, the depth of the source element and the particle volume fraction show stronger effects on the relative error than the other factors. The eigenstress deviation increases when the source element getting close to the surface, but for most of the calculation zone, the relative error is less than 2%. The relative error increases with the inhomogeneity volume fraction because a higher particle density leads to a stronger interaction among them, suggesting a larger dispersion of eigenstrains.

---
Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

![](./images/812791689356771330_4.jpg)

Fig. 4. Comparison of eigenstresses caused by the distributed particles in a microscopic meshand the corresponding macroscopic element.

![](./images/812791689356771330_5.jpg)

Fig. 5. Comparison of the true and approximate eigenstresses in the nearest three target macroscopic elements: (a) along the x-axis; (b) along the z-axis. In this example, the source element locates at $(0,0,0.24a_{0})$.

The results in Fig. 6 indicate that the assumption in Section 2.3.2 is proper.

### 2.4. Algorithm of the proposed model

The algorithm for the new model starts by solving for the contact pressure distribution (Polonsky and Keer, 1999), and then, subsurface elastic stresses are calculated (Liu and Wang, 2002). The total stress in the macroscopic mesh is composed of the updated elastic stress and the eigenstress from the last iteration step, and the total stress will be used for determining the equivalent eigenstrain in each macroscopic element in the next iteration by Eq. (18). The equivalent eigenstrains induce surface eigen-displacement, which is computed by Eq. (25); the contact pressure is updated again because the surface geometry has changed. The iterations stop when the difference between eigenstrains of consecutive steps is smaller than that of the preset tolerance. Such difference is calculated with Eq. (29), where $N$ is the number of macroscopic elements that have non-zero eigenstrains, and the superscript $(i)$ and $(i-1)$ are the iteration step indices. The tolerance is set to be 0.001.

$$
err = \frac{1}{N} \sum_{\xi=1}^{Nx} \sum_{\eta=1}^{Ny} \sum_{\vartheta=1}^{Nz} \left( \left( \varepsilon_{ij[\xi,\eta,\vartheta]}^{*(ma)(i)} - \varepsilon_{ij[\xi,\eta,\vartheta]}^{*(ma)(i-1)} \right) / \varepsilon_{ij[\xi,\eta,\vartheta]}^{*(ma)(i-1)} \right) \tag{29}
$$

All the computations mentioned above are in the macroscopic mesh. Once the solutions converge, the results of the macroscopic elements are applied as the initial values to evaluate the stress and strain fields in each microscopic mesh, solving for $\varepsilon_{ij}^{*(mi)}$ (Section 2.2.1) and $\sigma_{ij}^{*(mi)}$ (Section 2.3.1). The calculations on the microscopic mesh obtain the detailed stress and strain fields at the microscale level.

An example is used to explain the algorithm and to show typical results. The default modeling parameters and material properties are listed in Table 1, if not otherwise specified. The calculation zone is discretized into $32 \times 32 \times 32$ macroscopic elements. And only the elements inside a region of size $0.64a_{0} \times 0.64a_{0} \times 0.64a_{0}$ and centered at the depth of $0.48a_{0}$ are set as inhomogeneity elements, as indicated by Fig. 7(a). In this case, each microscopic mesh has $16^{3}$ elements.

The contact pressure distribution of the first iteration step is shown in Fig. 7(b). Presently, it follows the Hertizan contact equations because the initial value of equivalent eigenstrains is zero; thus, there is no eigen-displacement in the first step. The corresponding total stress field is plotted in Fig. 7(c). Similarly, the stress field appears to be homogeneous because the present eigenstress is zero. The equivalent eigenstrains of macroscopic inhomogene-

![](./images/812791689356771330_6.jpg)

Fig. 6. Relative errors of eigenstresses vs. (a) depth of the source element; (b) horizontal location of the source element; (c) particle elastic modulus; (d) particle volume fraction.

ity elements, which are calculated based on the stress field mentioned above, are shown in Fig. 7(d) (component $\varepsilon_{11}^{*}$). Then, the eigenstress and eigen-displacement induced by equivalent eigen-strains are determined (Fig. 7(e) and (f)). Note that the magnitude of eigenstress in Fig. 7(e) is much lower than that of the contact-induced elastic stress because the volume fraction of particles is only 5% in this case and they do not have a major effect on the average total stress in a macroscopic element. However, the detailed eigenstress field obtained in the microscopic meshes (Fig. 7(h)) indicates that the local eigenstress could be very strong. The calculations on the microscopic meshes are performed after the iteration on the macroscopic mesh has converged. The plot of the final von Mises stress in the XOZ section (Fig. 7(i)) is composed of $32^{2}$ microscopic meshes, and its total number of 'pixels' reaches $(32 \times 16)^{2}=262,144$. The stress and strain fields in the macrolevel and microlevel represent one of the advantages of the new model.

The calculation of the eigenstrains and eigenstress in each microscopic mesh requires considerable time for detailed stress results; the macroscopic mesh offers homogenized results and has a high computational efficiency due to the small number of elements.

### 2.5. Accuracy and efficiency of the new model

The new multiscale semi-analytical model is validated by comparing the results with those from a conventional SAM approach (Wang et al., 2013b). The contact between a spherical indenter and an inhomogeneous half-space is simulated. The dimensions of the calculation zone are $2.56a_{0}$, $2.56a_{0}$ and $1.28a_{0}$ in the x-, y- and z-directions, respectively. A total of $8 \times 8 \times 8=512$ cuboidal inhomogeneities are equally spaced in a $0.64a_{0} \times 0.64a_{0} \times 0.64a_{0}$ cubic cluster centered at $(0,0,0.48a_{0})$, as shown in Fig. 8. The edge length of the inhomogeneities is $0.02a_{0}$. In the conventional SAM model, an element must be smaller than an inhomogeneity; thus, the edge

![](./images/812791689356771330_7.jpg)

Fig. 7. Flow chart for the new model, shown with a sample case and its results: (a) model schematic; the elements in colored region are inhomogeneity macroscopic elements; (b) contact pressure distribution; (c) subsurface total stress of the first iteration step (the macroscopic mesh); (d) equivalent eigenstrain (component $\varepsilon_{11}^{*}$) in the macroscopic mesh; (e) eigenstress of the macroscopic mesh; (f) surface eigen-displacement; (g) equivalent eigenstrain in a microscopic mesh (component $\varepsilon_{11}^{*(mi)}$); (h) eigenstress in a microscopic mesh; (i) total stress field composed of all the microscopic meshes; (j) total stress field in the macroscopic mesh.

length of elements is set as $0.01a_{0}$, and $256 \times 256 \times 128$ elements are required. For the new model, the entire calculation zone is discretized into $32 \times 32 \times 16$ macroscopic elements, and there are $8 \times 8 \times 8$ elements in one microscopic mesh for a macroscopic element. The loading conditions and material properties follow those in Table 1, if not specified.

The results are plotted in Fig. 9. Only minor differences can be found between the contour plots of total von Mises stresses from the conventional SAM and the new model. The comparison of contact pressures is also plotted (Fig. 9(c)). Orthogonal tests were performed to verify the precision of the new model with varying parameters, as Table 2 shows. All the results indicate that the proposed new method is effective and reasonably accurate.

The efficiencies of the conventional and new models are compared by computing the cases listed in Table 2. The calculations are performed on a personal computer with an Intel i7-8700 CPU that has 12 parallel threads. The CPU times in Fig. 10 show that the present method has a higher efficiency than that of the conventional SAM model when addressing the same contact problems of inhomogeneous materials listed in Table 2.

### 3. Results and discussion

Particles in an actual composite may be non-uniformly distributed; the regions that have comparatively high local particle densities are termed clusters. Numerous studies have indicated that the mechanical properties and damage evolutions of particulate metal matrix composites are sensitive to the spatial distribution of the reinforcement phase (Conlon and Wilkinson, 2001; Hong et al., 2003; Segurado et al., 2003; Deng and Chawla, 2006; Segurado and LLorca, 2006). For example,

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

<table>
<thead>
<tr>
<th>No.</th>
<th>Young's modulus</th>
<th>Location of cluster center (x,y,z)</th>
<th>Inhomogeneity size</th>
<th>Maximum error of $\sigma_{VM}$ª</th>
<th>Average error of $\sigma_{VM}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Stiff ($E_i/E_M = 4.0$)</td>
<td>$(0, 0, 0.48a_0)$</td>
<td>$0.02a_0$</td>
<td>3.95%</td>
<td>0.98%</td>
</tr>
<tr>
<td>2</td>
<td>Stiff ($E_i/E_M = 4.0$)</td>
<td>$(0.48a_0, 0, 0.48a_0)$</td>
<td>$0.01a_0$</td>
<td>7.50%</td>
<td>0.94%</td>
</tr>
<tr>
<td>3</td>
<td>Compliant ($E_i/E_M = 0.25$)</td>
<td>$(0, 0, 0.48a_0)$</td>
<td>$0.01a_0$</td>
<td>4.04%</td>
<td>0.71%</td>
</tr>
<tr>
<td>4</td>
<td>Compliant ($E_i/E_M = 0.25$)</td>
<td>$(0.48a_0, 0, 0.48a_0)$</td>
<td>$0.02a_0$</td>
<td>10.52%</td>
<td>1.24%</td>
</tr>
</tbody>
</table>
$^a$ $error = |(\sigma_{VM}^{Classic} - \sigma_{VM}^{New})/\sigma_{VM}^{Classic}| \times 100\%$.

![](./images/812791689356771330_8.jpg)

Fig. 8. Schematics of the conventional and new models. In the new model, the inhomogeneity is modeled in the microscopic mesh further discretized in an macroscopic elelent, as shown by the right-side schematic.

Borbély et al. (2001) found that composites with clustered particles have higher flow stresses because of the more severe strain-hardening of matrix materials, compared with composites with randomly distributed particles. In addition, the ductility and fracture toughness of a composite decrease with the increasing heterogeneity of the reinforcement distributions (Murphy et al., 1998). Mishnaevsky et al. (2004) indicated that the stresses in clustered particles are much higher than those of randomly arranged particles, leading to earlier particle fractures. Young's modulus of a particle reduces nearly to zero after failing, and then, cavities and microvoids nucleate in the matrix near the broken particle, grow and coalesce, and that leads to the failure of the matrix ligaments between particles, and finally to the formation of a macro-crack in a volume (Derrien et al., 1999). Uniaxial tensile loading was applied in the work mentioned above, but the studies of the stresses and deformation mechanism of clustered composites under a contact loading are largely missing. The behaviors of composites that contain particle clusters and undertake a contact loading are investigated using the new model proposed in this paper.

The schematic of such an inhomogeneous material and modeling processes are shown in the left of Fig. 11, the particles are inside the area of clusters which are marked by the dash circles. The calculation zone is discretized by the macroscopic mesh, as discussed in Section 2.1.2. The elements inside a cluster area are inhomogeneities and be decomposed into microscopic meshes, while the others are matrix elements whose eigenstrains maintain at zero.

The sizes of the particles and the spherical clusters, and the particle volume fraction in the entire calculation zone $(V_f)$, are assumed to be constant in the following cases. This section aims to reveal the effect of particle concentrations on the contact behaviors of a composite. Apparently, the total volume of all the clusters determines the local particle density, e.g. a smaller number of clusters implies larger particle-free regions and a higher particle density in clusters. Therefore, the parameter, $V_{f\_U}$, defined as the volume ratio of clusters and the calculation zone, is utilized to represent the magnitude of particle concentrations.

Note that in a specific case, clusters are randomly distributed in the half-space, and the particle density in each cluster are identical. For example, letting $V_f = 2\%$, $V_{f\_U}$=50%, and the size of calculation zone is $0.0168\ \text{mm}^3$, then the particle fraction in clusters should be the total volume of particles divided by the volume of clusters, i.e. $(2\% \times 0.0168)/(50\% \times 0.0168)=4\%$. In the microscopic mesh, particles are randomly distributed; the particle volume fraction in the microscopic meshes is equal to that in the clusters.

Three parameters are used to illustrate the stress status of inhomogeneous materials with particle clusters: the maximum von Mises stresses, $max(\sigma_{VM\_M})$ and $max(\sigma_{VM\_I})$, maximum principal stress in inhomogeneities, $max(\sigma_{1\_I})$ (where subscripts 'I' and 'M' are referred to 'inhomogeneity' and 'matrix', respectively) and the stress volumetric integral of the entire calculation zone, $Vol(\sigma_{VM})$, calculated as Eq. (30).

$$
Vol(\sigma_{VM}) = \Delta x \times \Delta y \times \Delta z \times \sum_{\alpha=1}^{Nx} \sum_{\beta=1}^{Ny} \sum_{\gamma=1}^{Nz} \left( \sigma_{VM|[\alpha,\beta,\gamma]}^{(ma)} \right) \tag{30}
$$

where Nx, Ny and Nz are number of elements in the macroscopic mesh along the x-, y- and z-directions, respectively, and $\Delta x$, $\Delta y$, $\Delta z$ are the edge lengths of the macroscopic elements.

The motivations for choosing these parameters are stated as follows. (1) Plastic deformation in a material is always undesired due to its natural connection to fatigue failure. Inhomogeneities cause stress concentrations (Koumi et al., 2014b), and the peak stress may exceed the yield limit of matrix materials (but usually, the particles in reinforced composites do not yield because they have very high hardness). Therefore, the investigation of the maximum von Mises stress is necessary for evaluating the possibility of plastic deformation in such composites. (2) Particles may fracture under high-localized stresses without yielding. Young's modulus of a particle decreases nearly to zero after failing, and then cavities and microvoids nucleate in the matrix near the broken particle, grow and coalesce, and that leads to the failure of the matrix ligaments between particles, and finally to the formation of a macrocrack in a volume (Mishnaevsky et al., 2004; Derrien et al., 1999). The maximum principal stress is one of the fracture criteria and was used in Lippmann and Schmauder (2003) and Mishnaevsky et al. (1999, 2004). (3) Zaretsky (1987) proposed a model to predict the contact fatigue life of rolling bearings. The probability of survival can be expressed through the volumetric integral of an equivalent stress over the stressed volume. The von Mises stress is selected as the equivalent stress in reference Zhou et al. (2014a), and good agreement is found between experimental and simulation results. Therefore, the value of the von Mises stress volumetric integral,

![](./images/812791689356771330_9.jpg)

Fig. 9. Total von Mises stresses from (a) the conventional SAM model and (b) the new model; (c) comparison of contact pressure results.

normalized by that in the case of a homogeneous distribution, is used in this section as an index for comparing the rolling contact fatigue lives.

The parameters used in the following cases are listed in Table 3, if not otherwise specified. The von Mises stress fields of the XOZ section when $V_{f\_U}$ equals 100%, 50% and 25% are plotted in Fig. 12. The clusters are bounded by the dashed circles. $V_{f\_U}=100\%$ corresponds to the random particle distribution whereas $V_{f\_U}<100\%$ is a clustered distribution. The randomness of the results is expected due to the location of clusters. This is because that the total stress is the sum of elastic stress and eigenstress, and the elastic stress field induced by a contact loading has large gradients in the near-surface material. There is a large variation in elastic stress in the regions that these clusters are located, which makes the major

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

<table><caption>Table 3 Modeling parameters and material properties used in Section 3.</caption>
<thead>
<tr>
<th>Item</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hertzian contact radius ($a_0$)</td>
<td>0.1 mm</td>
</tr>
<tr>
<td>Hertzian contact pressure ($P_0$)</td>
<td>2350 MPa</td>
</tr>
<tr>
<td>Sizes of the calculation zone ($x,y,z$)</td>
<td>$[-1.28a_0, 1.28a_0]$ $[0, 1.28a_0]$</td>
</tr>
<tr>
<td>Element numbers in the macroscopic mesh ($N_x,N_y,N_z$)</td>
<td>32,32,16</td>
</tr>
<tr>
<td>Element numbers in the microscopic mesh ($n_x,n_y,n_z$)</td>
<td>16,16,16</td>
</tr>
<tr>
<td>Edge length of the macroscopic elements ($\Delta x=\Delta y=\Delta z$)</td>
<td>$8×10^{-2}a_0$</td>
</tr>
<tr>
<td>Edge length of the microscopic elements ($dx=dy=dz$)</td>
<td>$5×10^{-3}a_0$</td>
</tr>
<tr>
<td>Edge length of the inhomogeneities</td>
<td>$1×10^{-2}a_0$</td>
</tr>
<tr>
<td>Radius of the clusters</td>
<td>$0.32a_0$</td>
</tr>
<tr>
<td>Inhomogeneity volume fraction of the entire calculation zone ($V_f$)</td>
<td>2%</td>
</tr>
<tr>
<td>Young's modulus ratio ($E_I/E_M$)</td>
<td>4.0 (stiff), 0.5 (compliant)</td>
</tr>
<tr>
<td>Poisson's ratio of the inhomogeneities ($\nu_I$)</td>
<td>0.3</td>
</tr>
<tr>
<td>Poisson's ratio of the matrix material ($\nu_M$)</td>
<td>0.3</td>
</tr>
</tbody>
</table>

![](./images/812791689356771330_10.jpg)

Fig. 10. Comparison of the CPU times of the two methods with different modeling and material parameters listed in Table 2.

contribution to the deviations in Fig. 13. Therefore, ten calculations were run for each data point in the following figures, and the average values are plotted as scatter, with the standard deviations as error bars.

Plots (a) and (b) in Fig. 13 present the maximum stresses against the volume fraction of inhomogeneity elements of the macroscopic mesh, $V_{f\_U}$. For both stiff and compliant inhomogeneities, $max(\sigma_{VM\_M})$ and $max(\sigma_{VM\_I})$ increase when $V_{f\_U}$ decreases. Note that stiff and compliant inhomogeneities induce stress concentrations in matrix materials because the matrix maximum von Mises stresses considered in Fig. 13(a) and (b) are much higher than that of the corresponding homogeneous case (approximately equals $0.62P_0$). In addition, as demonstrated in reference Koumi et al. (2014a), no stress concentration is found inside a compliant inhomogeneity, which is indicated by Fig. 13(b) in that the maximum stresses in inhomogeneities are lower than those in matrix materials. The clustered distributions result in a stronger compressive stress in inhomogeneities for $E_I/E_M=4.0$ and $E_I/E

![](./images/812791689356771330_11.jpg)

Fig. 11. An inhomogeneous material with particle clusters is modeled via the two-level mesh scheme.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

![](./images/812791689356771330_12.jpg)

Fig. 12. von Mises stress in the XOZ section when $V_{f,U}$ equals (a) 100%; (b) 50%; (c) 25%. Here, the Young's modulus ratio is $E_I/E_M=3.0$.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

![](./images/812791689356771330_13.jpg)

![](./images/812791689356771330_14.jpg)

![](./images/812791689356771330_15.jpg)

![](./images/812791689356771330_16.jpg)

![](./images/812791689356771330_17.jpg)

Fig. 13. Maximum von Mises stress in matrix and inhomogeneities vs. $V_{f\_U}$ for (a) stiff inhomogeneities and (b) compliant inhomogeneities; maximum principal stress in inhomogeneities for (c) stiff inhomogeneities and (d) compliant inhomogeneities; normalized stress volumetric integral vs. $V_{f\_U}$ for (e) stiff inhomogeneities and (f) compliant inhomogeneities.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

![](./images/812791689356771330_18.jpg)

Fig. 14. von Mises stress fields in a microscopic mesh, when the gap among inhomogeneities is (a) 10r; (b) 4r.

tween them are set to 10r or 4r, where r is the radius of an inhomogeneity. The corresponding macroscopic element is located at $(0,0,0.48a_{0})$. The von Mises stresses of the two examples are plotted in Fig. 14. When the inhomogeneities are far from each other (Fig. 14(a)), each inhomogeneity induces an identical stress disturbance in the adjacent matrix material, suggesting that there are almost no interactions among them, and the maximum stress of inhomogeneity is $1.01P_{0}$. However, the maximum value increases to $1.12P_{0}$ if the inhomogeneity gap is only 4r because the overlapping of the stress concentration regions amplifies the eigenstress in inhomogeneities and matrix materials. A smaller $V_{f_{-}U}$ implies larger particle-free regions, leading to a higher local particle density in the clusters and a smaller gap between inhomogeneities, explaining the variations in Fig. 13.

## 4. Conclusions

This paper introduces a new semi-analytical model for simulating the contact of materials containing distributed or clustered particles. A two-level mesh scheme is applied to implement multiscale computation: the macroscopic mesh uses homogenized elements that ensure a high computing efficiency, whereas the material microstructures are modeled by the elements of the microscopic mesh; and thus, the microscopic stress and strain can be obtained. The eigenstress and eigenstrain, as well as the corresponding influence coefficients, are derives for both mesh levels.

The new model is applied to investigate the effects of particle clustering on the contact performances of composites. The results show that the maximum von Mises stress and the maximum principal stress in inhomogeneities of a composite with particle clusters are higher than that of the composite with particles in a random distribution, suggesting that the clustered material is more likely to yield and that the particles in a cluster have more possibilities to be fractured. For stiff particles, the stress volumetric integral increases with the particle distribution heterogeneity, but for compliant ones, the random distribution has the highest stress volumetric integral value.

## Acknowledgments

Q. Wang would also like to acknowledge the support from US National Science Foundation (Grant number, CMMI-1434834).

Z. Wang would like to express gratitude to the support from China National Science Foundation (Grand number 51775457). Center for Surface Engineering and Tribology at Northwestern University, Evanston, USA, is also acknowledged. The authors would also like to thank the review suggestions for improving the quality and completeness of this publication.

## References

Amuzuga, K., Chaise, T., Duval, A., Nelias, D., 2016. Fully coupled resolution of heterogeneous elastic-plastic contact problem. J. Tribol. 138, 021403.

Borbély, A., Biermann, H., Hartmann, O., 2001. FE investigation of the effect of particle distribution on the uniaxial stress - strain behaviour of particulate reinforced metal-matrix composites. Mater. Sci. Eng. A 313 (1-2), 34-45.

Chen, W., Liu, S., Wang, Q., 2008a. Fast Fourier transform based numerical methods for elasto-plastic contacts of nominally flat surfaces. J. Appl. Mech. 75, 011022.

Chen, W., Zhou, K., Keer, L., Wang, Q., 2010. Modeling elasto-plastic indentation on layered materials using the equivalent inclusion method. Int. J. Solids Struct. 47, 2841-2854.

Chen, W.W., Wang, Q.J., Wang, F., Keer, L.M., Cao, J., 2008b. Three-dimensional repeated elasto-plastic point contacts, rolling, and sliding. J. Appl. Mech. 75, 021021. doi:10.1115/1.2755171.

Conlon, K.T., Wilkinson, D.S., 2001. Effect of particle distribution on deformation and damage of two-phase alloys. Mater. Sci. Eng. A 317, 108-114.

Deng, X., Chawla, N., 2006. Modeling the effect of particle clustering on the mechanical behavior of SiC particle reinforced Al matrix composites. J. Mater. Sci. 41, 5731-5734.

Derrien, K., Baptiste, D., Guedra-Degeorges, D., Foulquier, J., 1999. Multiscale modeling of the damaged plastic behavior and failure of Al/SiCp composites. Int. J. Plast. 15, 667-685.

Dong, Q., Zhou, K., Chen, W., Fan, Q., 2016. Partial slip contact modeling of heterogeneous elasto-plastic materials. Int. J. Mech. Sci. 114, 98-110.

Eshelby, J., 1957. The determination of the elastic field of an ellipsoidal inclusion, and related problems. Proc. R. Soc. A Math. Phys. Eng. Sci. 241, 376-396.

Guan, J., Wang, L., Zhang, C., Ma, X., 2017. Effects of non-metallic inclusions on the crack propagation in bearing steel. Tribol. Int. 106, 123-131.

Harish, A.B., Wriggers, P., Jungk, J., Hojdis, N., Recker, C., 2016. Mesoscale constitutive modeling of non-crystallizing filled elastomers. Comput. Mech. 57, 653-677.

Harursampath, D., Harish, A.B., Hodges, D.H., 2017a. Model reduction in thin-walled open-section composite beams using variational asymptotic method. Part II: applications. Thin-Walled Struct. 117, 367-377.

Harursampath, D., Harish, A.B., Hodges, D.H., 2017b. Model reduction in thin-walled open-section composite beams using variational asymptotic method. Part I: theory. Thin-Walled Struct. 117, 356-366.

Hashin, Z., Shtrikman, S., 1962. A variational approach to the theory of the elastic behaviour of polycrystals. J. Mech. Phys. Solids 10, 343-352.

Hong, S.J., Kim, H.M., Huh, D., Suryanarayana, C., Chun, B.S., 2003. Effect of clustering on the mechanical properties of SiC particulate-reinforced aluminum alloy 2024 metal matrix composites. Mater. Sci. Eng. A 347, 198-204.

Hori, M., Nemat-Nasser, S., 1993. Double-inclusion model and overall moduli of multi-phase composites. Mech. Mater. 14, 189-206.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019

Hsiao, G.C., Wendland, W.L., 1991. Domain decomposition in boundary element methods. In: Proc. Fourth Int. Symp. Domain Decompos. Methods Partial Dif- fer. Equations, pp. 41-49.

Jacq, C., Nelias, D., Lormand, G., Girodin, D., 2002. Development of a three-dimen- sional semi-analytical elastic-plastic contact code. J. Tribol. 124, 653.

Jin, X., Keer, L.M., Wang, Q.J., Chez, E.L., 2013. Conjugate gradient method for contact analysis. In: Encycl. Tribol.. Springer, pp. 446-451.

Kabo, E., 2002. Material defects in rolling contact fatigue - influence of overloads and defect clusters. Int. J. Fatigue. 24, 887-894.

Koumi, K., Zhao, L., Leroux, J., Chaise, T., Nelias, D., 2014a. Contact analysis in the presence of an ellipsoidal inhomogeneity within a half space. Int. J. Solids Struct. 51, 1390-1402.

Koumi, K.E., Nelias, D., Chaise, T., Duval, A., 2014b. Modeling of the contact be- tween a rigid indenter and a heterogeneous viscoelastic material. Mech. Mater.77,28-42.

Leroux, J., Fulleringer, B., Nélias, D., 2010. Contact analysis in presence of spherical inhomogeneities within a half-space. Int. J. Solids Struct. 47, 3034-3049.

Lippmann, N., Schmauder, S., 2003. Computational modeling of crack propagation in real microstructures of steels and virtual testing of artificially designed materi- als. Int. J. Fatigue 581-600.

Liu, S., Hua, D., Chen, W., Wang, Q., 2007. Tribological modeling: application of fast Fourier transform. Tribol. Int. 40, 1284-1293.

Liu, S., Jin, X., Wang, Z., Keer, L., Wang, Q., 2012. Analytical solution for elastic fields caused by eigenstrains in a half-space and numerical implementation based on FFT. Int. J. Plast. 35, 135-154.

Liu, S., Wang, Q., 2002. Studying contact stress fields caused by surface tractions with a discrete convolution and fast fourier transform algorithm. J. Tribol. 124,36-45.

Liu, S., Wang, Q., 2005. Elastic fields due to eigenstrains in a half-space. J. Appl. Mech. 72, 871-878.

Liu, S., Wang, Q., Liu, G., 2000. A versatile method of discrete convolution and FFT(DC-FFT) for contact analyses. Wear 243, 101-111.

Liu, Z., Bessa, M.A., Liu, W.K., 2016. Self-consistent clustering analysis: an efficient multi-scale scheme for inelastic heterogeneous materials[J]. Comput. Methods Appl. Mech. Eng. 306, 319-341. doi:10.1016/j.cma.2016.04.004.

Liu, Z., Fleming, M., Liu, W.K., 2018. Microstructural material database for self-con- sistent clustering analysis of elastoplastic strain softening materials. Comput. Methods Appl. Mech. Eng. 330, 547-577.

Lu, P., Leong, Y., Pallathadka, P., He, C., 2013. Effective moduli of nanoparticle rein- forced composites considering interphase effect by extended double-inclusion model - Theory and explicit expressions. Int. J. Eng. Sci. 73, 33-55.

Mishnaevsky, L., Derrien, K., Baptiste, D., 2004. Effect of microstructure of parti- cle reinforced composites on the damage evolution: probabilistic and numerical analysis. Compos. Sci. Technol. 64, 1805-1818.

Mishnaevsky, L., Dong, M., Hönle, S., Schmauder, S., 1999. Computational mesome- chanics of particle-reinforced composites. Comput. Mater. Sci. 16, 133-143.

Moghaddam, S., Sadeghi, F., Paulson, K., Weinzapfel, N., Correns, M., Bakolas, V., Dinkel, M., 2015. Effect of non-metallic inclusions on butterfly wing initia- tion, crack formation, and spall geometry in bearing steels. Int. J. Fatigue 80,203-215.

Moghaddam, S., Sadeghi, F., Paulson, K., Weinzapfel, N., Correns, M., Dinkel, M., 2016. A 3D numerical and experimental investigation of microstructural alter- ations around non-metallic inclusions in bearing steel. Int. J. Fatigue 88, 29-41.

Moghaddam, S., Sadeghi, F., Weinzapfel, N., Liebel, A., 2014. A damage mechanics approach to simulate butterfly wing formation around nonmetallic inclusions. J. Tribol. 137, 011404.

Moore, J.A., Ma, R., Domel, A.G., Liu, W.K., 2014. An efficient multiscale model of damping properties for filled elastomers with complex microstructures. Com- pos. Part B Eng. 62, 262-270.

Mori, T., Tanaka, K., 1973. Average stress in matrix and average elastic energy of materials with misfitting inclusions. Acta Metall. 21, 571-574.

Mura, T., 1987. Micromechanics of Defects in Solids. Martinus Nijhoff, Dordrecht.

Murphy, A.M., Howard, S.J., Clyne, T.W., 1998. Characterisation of severity of particle clustering and its effect on fracture of particulate MMCs. Mater. Sci. Technol. 14,959-968.

Paulson, N., Evans, N., Bomidi, J., Sadeghi, F., Evans, R., Mistry, K., 2015. A finite el- ement model for rolling contact fatigue of refurbished bearings. Tribol. Int. 85,1-9.

Polonsky, I., Keer, L., 1999. A numerical method for solving rough contact problems based on the multi-level multi-summation and conjugate gradient techniques. Wear 231, 206-219.

Segurado, J., González, C., LLorca, J., 2003. A numerical investigation of the effect of particle clustering on the mechanical properties of composites. Acta Mater. 51,2355-2369.

Segurado, J., LLorca, J., 2006. Computational micromechanics of composites: the ef- fect of particle spatial distribution. Mech. Mater. 38, 873-883.

Shodja, H., Sarvestani, A., 2001. Elastic fields in double inhomogeneity by the equiv- alent inclusion method. J. Appl. Mech. 68, 3-10.

Wang, Z., Jin, X., Keer, L., Wang, Q., 2013a. Novel Model for Partial-Slip Contact In- volving a Material With Inhomogeneity. J. Tribol. 135, 041401.

Wang, Z., Jin, X., Zhou, Q., Ai, X., Keer, L., Wang, Q., 2013b. An efficient numerical method with a parallel computational strategy for solving arbitrarily shaped in- clusions in elastoplastic contact problems. J. Tribol. 135, 031401.

Wang, Z., Zhu, D., Wang, Q., 2013c. Elastohydrodynamic lubrication of inhomoge- neous materials using the equivalent inclusion method. J. Tribol. 136, 021501.

Yagawa, G., Soneda, N., Yoshimura, S., 1991. A large scale finite element analysis using domain decomposition method on a parallel computer. Comput. Struct.38,615-625.

Yang, W., Huang, Y., Zhou, Q., Wang, J., Jin, X., Keer, L., 2017. Parametric study on stressed volume and its application to the quantification of rolling contact fa- tigue performance of heterogeneous material. Tribol. Int. 107, 221-232.

Zaretsky, E.Y., 1987. Fatigue criterion to system design, life, and reliability. NASA Tech. Memo. 3, 76-83.

Zhang, J., Lu, L., Wu, P., Ma, J., Wang, G., Zhang, W., 2013. Inclusion size evaluation and fatigue strength analysis of 35CrMo alloy railway axle steel. Mater. Sci. Eng. A. 562, 211-217.

Zhang, M., Zhao, N., Glaws, P., Hegedus, P., Zhou, Q., Wang, Z., Jin, X., Keer, L.M.L.M., Wang, Q., 2017. Elasto-plastic contact of materials containing double-layered in- homogeneities. Int. J. Solids Struct. 126-127, 208-224.

Zhang, M., Zhao, N., Wang, Z., Wang, Q., 2018. Efficient numerical method with a dual-grid scheme for contact of inhomogeneous materials and its applications. Comput. Mech. 1-17.

Zhou, K., 2012. Elastic field and effective moduli of periodic composites with arbi- trary inhomogeneity distribution. Acta Mech. 223, 293-308.

Zhou, K., Keer, L., Wang, Q., Ai, X., Sawamiphakdi, K., Glaws, P., Paire, M., Che, F., 2012. Interaction of multiple inhomogeneous inclusions beneath a surface. Com- put. Methods Appl. Mech. Eng. 217-220, 25-33.

Zhou, Q., Jin, X., Wang, Z., Wang, J., Keer, L., Wang, Q., 2014a. An efficient approxi- mate numerical method for modeling contact of materials with distributed in- homogeneities. Int. J. Solids Struct. 51, 3410-3421.

Zhou, Q., Jin, X., Wang, Z., Wang, J., Keer, L., Wang, Q., 2015. Numerical implemen- tation of the equivalent inclusion method for 2D arbitrarily shaped inhomo- geneities. J. Elast. 118, 39-61.

Zhou, Q., Jin, X., Wang, Z., Yang, Y., Wang, J., Keer, L., Wang, Q., 2016. A mesh differ- ential refinement scheme for solving elastic fields of half-space inclusion prob- lems. Tribol. Int. 93, 124-136.

Zhou, Q., Xie, L., Jin, X., Wang, Z., Wang, J., Keer, L.M., Wang, Q., 2014b. Numeri- cal modeling of distributed inhomogeneities and their effect on rolling-contact fatigue life. J. Tribol. 137, 011402.

Please cite this article as: M. Zhang, Q. Wang and Z. Wang et al., Multiscale computational scheme for semi-analytical modeling of the point contact of inhomogeneous materials, International Journal of Solids and Structures, https://doi.org/10.1016/j.ijsolstr.2019.03.019
