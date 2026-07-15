# Computation of the size-dependent elastic moduli of nano-fibrous and nano-porous composites by FFT

A.T. Tran $^{a}$, H. Le Quang $^{a, *}$, Q.-C. He $^{a, b, **}$

$^{a}$ Université Paris-Est, Laboratoire de Modélisation et Simulation Multi Echelle, UMR 8208 CNRS, 5 Bd Descartes, F-77454 Marne-la-Vallée Cedex 2, France
$^{b}$ Southwest Jiaotong University, School of Mechanical Engineering, Chengdu 610031, PR China

---

## ARTICLE INFO

**Article history:**
Received 22 July 2015
Received in revised form
13 September 2016
Accepted 15 September 2016
Available online 26 September 2016

**Keywords:**
Fibres
Nano composites
Interface
Mechanical properties
Multiscale modeling

---

## ABSTRACT

The present work is concerned with nanocomposites consisting of a matrix containing unidirectional nanofibers or nanopores. In such a nanocomposite, due to the exceptionally high surface-to-volume ratio of a nanofiber or nanopore, the fiber-matrix interface or pore surface stresses, which are usually neglected in determining the effective properties of classical fibrous and porous composites, have a non-negligible effect on the effective properties at the macroscopic scale. The purpose of this work is first to compute the effective elastic moduli of unidirectional nano-fibrous and nano-porous composites accounting for interface/surface stresses and second to study the dependencies of these effective moduli on the size, shape and distribution of nanofibers and nanopores in the matrix. To achieve this twofold objective, a coherent interface/surface model is adopted for the nanofiber-matrix interface and pore surface, and a numerical method based on the fast Fourier transform (FFT) is elaborated. The numerical results obtained for the effective elastic moduli of fibrous and porous nanocomposites are compared with the analytical estimates obtained from the generalized self-consistent model (GSCM), with some relevant bounds and with the corresponding numerical results provided by the extended finite element method (XFEM)/level-set approach.

© 2016 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Since the discovery of carbon nanotubes more than two decades ago by Ijima [1], the scientific community has observed a steady progress of the science and technology of nanocomposites. In general, a nanocomposite is a multiphase material in which a bulk matrix phase is reinforced by nano-dimensional phases. The reinforcing phases can be particles, sheets or fibres. Compared with the traditional composites, due to the exceptionally high surface-to-volume ratio of a reinforcing phase and/or its exceptionally high aspect ratio, nanocomposites may exhibit improved properties compared to classical composites, such as electrical conductivity, mechanical stiffness and strength, and various optical properties. This fact has been highlighted in recent theoretical and numerical studies on nanomaterials and nanosized structural elements (see, e.g., [2–12]).

In addition to the theoretical analyses and numerical computations of the properties of nanocomposites, there are some experimental studies. For example, by using the contact atomic force microscopy and applying the surface stress theory, Cuenot et al. [13] and Jing et al. [14] measured the elastic properties of silver nanowires whose outer diameter varies from 20 to 140 nm. At the same time, they observed that the Young's modulus measured of the silver nanowires increases when its diameter decreases. In the similar works, Chen et al. [15] investigated ZnO nanowires with diameters ranging from 17 to 550 nm. Priota et al. [16] used magnetic characterization to study metallic Ni and Co nanowires with lengths being set to vary from 530 to 2250 nm while the diameter is kept constant with 35 nm. Tan et al. [17] employed the atomic force microscopy to make three-point bending tests of CuO nanowires. In all these experimental measurements, the authors found clearly that the Young's modulus measured increases when decreasing the diameter of the nanowires due to the surface effect.

Among nanocomposites, unidirectional nanofibrous and nano-porous composites consisting of a matrix containing aligned

---
* Corresponding author.
** Corresponding author. Université Paris-Est, Laboratoire de Modélisation et Simulation Multi Echelle, UMR 8208 CNRS, 5 Bd Descartes, F-77454 Marne-la-Vallée Cedex 2, France.
E-mail addresses: hung.lequang@univ-paris-est.fr (H. Le Quang), qi-chang.he@univ-paris-est.fr (Q.-C. He).

http://dx.doi.org/10.1016/j.compscitech.2016.09.012
0266-3538/© 2016 Elsevier Ltd. All rights reserved.

![](./images/811139233631698946_1.jpg)
![](./images/811139233631698946_2.jpg)
![](./images/811139233631698946_3.jpg)

<table><caption>Table of notations</caption>
<tbody><tr>
<td>$\boldsymbol{\sigma}^{(p)}$</td>
<td>Cauchy stress tensor of phase $p$</td>
</tr>
<tr>
<td>$\boldsymbol{\varepsilon}^{(p)}$</td>
<td>Infinitesimal strain tensor of phase $p$</td>
</tr>
<tr>
<td>$\boldsymbol{\Sigma}$</td>
<td>Macroscopic stress tensor</td>
</tr>
<tr>
<td>$\mathbf{E}$</td>
<td>Macroscopic strain tensor</td>
</tr>
<tr>
<td>$\mathbb{C}^{(p)}$</td>
<td>Elastic stiffness tensor of phase $p$</td>
</tr>
<tr>
<td>$\mathbb{S}^{(p)}$</td>
<td>Elastic compliance tensor of phase $p$</td>
</tr>
<tr>
<td>$\mathbb{C}^{(si)}$</td>
<td>Elastic stiffness tensor of interface $\Gamma^{(i)}$</td>
</tr>
<tr>
<td>$\mathbb{S}^{(si)}$</td>
<td>Elastic compliance tensor of interface $\Gamma^{(i)}$</td>
</tr>
<tr>
<td>$\mathbb{C}^{*}$</td>
<td>Effective elastic stiffness tensor</td>
</tr>
<tr>
<td>$\mathbb{S}^{*}$</td>
<td>Effective elastic compliance tensor</td>
</tr>
<tr>
<td>$E_{p}$</td>
<td>Young's modulus of phase $p$</td>
</tr>
<tr>
<td>$\nu_{p}$</td>
<td>Poisson's ratio of phase $p$</td>
</tr>
<tr>
<td>$E_{si}$</td>
<td>Young's modulus of interface $\Gamma^{(i)}$</td>
</tr>
<tr>
<td>$V_{si}$</td>
<td>Poisson's ratio of interface $\Gamma^{(i)}$</td>
</tr>
<tr>
<td>$k^{*}$</td>
<td>Effective transverse bulk modulus</td>
</tr>
<tr>
<td>$m^{*}$</td>
<td>Effective shear modulus</td>
</tr>
<tr>
<td>$G^{*}$</td>
<td>Effective anti-plan longitudinal shear modulus</td>
</tr>
<tr>
<td>$\bar{G}^{*}$</td>
<td>Effective in-plan longitudinal shear modulus</td>
</tr>
<tr>
<td>$n^{*}$</td>
<td>Effective longitudinal modulus</td>
</tr>
<tr>
<td>$l^{*}$</td>
<td>Effective transverse modulus</td>
</tr>
</tbody>
</table>

parallel nanofibers or nanopores have the characteristic that their properties are homogeneous along the direction of nanofibers or nanopores but heterogeneous in its transverse plane. Recent advances in nanotechnology have made it possible to fabricate continuous nanofibers, nanofibrous networks or short nanowires from various materials such as polymers, carbon and semiconductors [18]. At the same time, suitable techniques have been also developed to measure and characterize the mechanical properties of nanofibers [19,20], which turn out to be largely superior to those of micron-sized fibers. Nanofibers are used for a wide range of applications and in particular as reinforcement in composites [18,21]. Due to the practical importance and technological interest of unidirectional nanofibrous and nanoporous composites, the present work aims to propose a numerical method based on the fast Fourier transform to compute the effective elastic moduli of unidirectional nanofibrous and nanoporous composites.

Recently, different works devoted to study the size-dependent mechanical behavior of unidirectional nanofibrous and nanoporous composites. Indeed, given a volume fraction of nanofibers or nanopores, when the size of a fiber or pore is diminished to the nano-scale, due to the large surface-to-volume ratio, the interface-to-volume ratio is so high that the fiber-matrix interface or pore surface energy or stress has a non-negligible effect on its overall properties. Thus, in order to determine the size-dependent overall elastic properties of unidirectional nanofibrous and nanoporous composites accounting for the surface/interface energies, use has been widely made of the coherent interface model in which the displacement vector field is continuous across an interface while the stress vector field is discontinuous across the same interface [22-24]. The coherent interface model has been shown to be a particular case of the general linear imperfect interface model whose development goes back to the works [25-31].

In fact, apart from the coherent interface model used in the present work, there exist also another model in which the stress vector filed is continuous across the interface but the displacement vector field is discontinuous. This interface model, called also spring-layer model, can be viewed as the complementary or dual of the one employed in this work. However, of these two most widely used interface models, according to the theoretical analyses and numerical computations presented in Refs. [2-12,22-24], only the coherent interface model is able to capture the size-dependency of the effective properties of nanocomposites. Moreover, the effective elastic properties obtained from the theoretical analyses and numerical computations are shown to agree with the ones provided by experimental measurements. For this reason, only the coherent interface model has been chosen to describe the interfaces between the nano-fiber (or nano-pore) and matrix phases of composites.

The present work has two objectives. First, it aims to extend the computational method based on the fast Fourier transform initially proposed by Moulinec and Suquet [32], Michel et al.. [33] to incorporating interface/surface energies so as to solve the localization problem for the nanofibrous or nanoporous composites in question. Second, it has the purpose of employing the solution of the localization problem to determine and study the effects of the interface, size and distribution of nanofibers or nanopores on the effective elastic moduli of unidirectional nanofibrous or nanoporous composites. Numerical results obtained for all the effective elastic moduli of unidirectional nanofibrous and nanoporous composites are shown to agree well with the analytical estimates obtained from the generalized self-consistent model [34], the relevant bounds [12] and the corresponding numerical results provided by the XFEM/level-set approach [35].

It is important to notice that all results obtained for nanofibrous composites can be directly applicable to nano-porous composites by considering the pores as fibres with a zero modulus. For this reason, in the rest of this paper, only the computational method relative to fibrous nanocomposites will be established and presented.

The paper is organized as follows. Section 2 is dedicated to describing the phase and interface properties of unidirectional nanofibers composites. In section 3, a computational method based on FFT is elaborated so as to include interfacial energy. In section 4, we apply the numerical method to several examples. In particular, the numerical results obtained illustrate the effects of the size, distribution and shape of nanofibers on the effective elastic moduli of unidirectional nanofibrous composites. In addition, the numerical results are compared with the estimates provided by GCSM, the corresponding bounds and the numerical ones obtained by the XFEM/level-set approach. Finally, a few concluding remarks are given in Section 5.

### 2. Setting of the problem

The fibrous nanocomposite considered in the present work consists of a matrix periodically containing $N$ ($\geq 1$) aligned parallel nanofibers (Fig. 1). The matrix, referred to as phase 0, and $i$th-fiber, denoted as phase $i$ with $i=1,2,....,N$, are assumed to be individually homogeneous and linearly elastic. In the Cartesian coordinate system $(x_{1},x_{2},x_{3})$ associated with an orthonormal basis $\{\mathbf{e}_{1},\mathbf{e}_{2},\mathbf{e}_{3}\}$ with the unit vector $\mathbf{e}_{3}$ defining the fiber direction, the matrix and fibers are characterized by the Hooke law:
$$
\boldsymbol{\sigma}^{(p)}(\mathbf{x})=\mathbb{C}^{(p)} \boldsymbol{\varepsilon}^{(p)}(\mathbf{x}) \text { or } \boldsymbol{\varepsilon}^{(p)}(\mathbf{x})=\mathbb{S}^{(p)} \boldsymbol{\sigma}^{(p)}(\mathbf{x}),\qquad(1)
$$
where $\boldsymbol{\sigma}^{(p)}$ and $\boldsymbol{\varepsilon}^{(p)}$ are, respectively, the Cauchy stress tensor and the infinitesimal strain tensor of phase $p$ $(=0,1,2,...,N)$; $\mathbb{C}^{(p)}$ and $\mathbb{S}^{(p)}$ stand for the fourth-order elastic stiffness and compliance tensors of phase $p$. These tensors have the usual minor and major symmetries and are positive definite.

Let $\Omega$ be a representative volume element (RVE) of the fibrous nanocomposite under consideration and let $\partial\Omega$ be the boundary of $\Omega$. The subdomains of $\Omega$ occupied by the matrix and the $i$th-fiber are designated by $\omega^{(0)}$ and $\omega^{(i)}$, respectively. In our investigation, the

![](./images/811139233631698946_4.jpg)

Fig. 1. Periodic fibrous nanocomposite with (a) squarely distributed nanofibers and (b) hexagonally distributed nanofibers.

interface between the matrix and the ith-fiber, denoted by $\Gamma^{(i)}$, is assumed to be suitably described by the coherent interface model. In the context of elasticity, this interface model was first proposed by Shuttleworth [22] and then improved by Gurtin and Murdoch [23] and Cahn [24]. According to it, the matrix-fiber interface is considered as an elastic deformable surface $\Gamma^{(i)}$ with a vanishing thickness, across which the displacement vector is continuous but the traction vector is discontinuous. Letting $\boldsymbol{n}(\mathbf{x})$ be the unit vector normal to the interface $\Gamma^{(i)}$ at $\mathbf{x} \in \Gamma^{(i)}$ and directed from the $i$ th inclusion $\omega^{(i)}$ into the matrix $\omega^{(0)}$, we define the normal projection operator $\mathbf{N}(\mathbf{x})$ and tangential projection operator $\mathbf{P}(\mathbf{x})$ by

$$
\mathbf{N}(\mathbf{x})=\mathbf{n}(\mathbf{x}) \otimes \mathbf{n}(\mathbf{x}), \quad \mathbf{P}(\mathbf{x})=\mathbf{I}-\mathbf{N}(\mathbf{x})
\tag{2}
$$

where $\mathbf{I}$ stands for the second-order identity tensor. By using Hadamard's relation (see e.g., [36]), it can be shown that, across the interface $\Gamma^{(i)}$, the tangential projection of the strain tensor field on this interface, denoted by $\boldsymbol{e}^{(s i)}(\mathbf{x})$, is in general continuous, even though the strain tensor field as a whole is discontinuous. Therefore, the strain state of an interface $\Gamma^{(i)}$ is characterized by the surface infinitesimal strain tensor $\boldsymbol{e}^{(s i)}(\mathbf{x})$, and its value is equal to the tangential part of $\boldsymbol{e}^{(i)}(\mathbf{x})$ or $\boldsymbol{e}^{(0)}(\mathbf{x})$:

$$
\boldsymbol{e}^{(s i)}(\mathbf{x})=\mathbb{T}(\mathbf{x}) \boldsymbol{e}^{(i)}(\mathbf{x})=\mathbb{T}(\mathbf{x}) \boldsymbol{e}^{(0)}(\mathbf{x}) \quad \forall \mathbf{x} \in \Gamma^{(i)}.
\tag{3}
$$

In this expression, $\mathbb{T}$ stands for the fourth-order tangential projection tensor defined by

$$
\mathbb{T}(\mathbf{x})=\mathbf{P}(\mathbf{x}) \overline{\otimes} \mathbf{P}(\mathbf{x}),
\tag{4}
$$

where the tensor product product $\overline{\otimes}$ is defined by $(\mathbf{A} \overline{\otimes} \mathbf{B})_{m n k l}=\left(A_{m k} B_{n l}+A_{m l} B_{n k}\right) / 2$ for any two second-order tensors $\mathbf{A}$ and $\mathbf{B}$ (see, e.g. Ref. [37]).

Unlike the classical perfect interface, the traction vector field is discontinuous across the coherent interface $\Gamma^{(i)}$, and its jump is related to the surface Cauchy stress tensor $\boldsymbol{\sigma}^{(s i)}(\mathbf{x})$ through the following generalized Young-Laplace equation (see e.g., [38,39]):

$$
[\![\boldsymbol{\sigma}(\mathbf{x})]\!] \mathbf{n}(\mathbf{x})=-\nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)}(\mathbf{x}) \quad \text { with } \mathbf{x} \in \Gamma^{(i)}
\tag{5}
$$

where $[\![\boldsymbol{\sigma}(\mathbf{x})]\!]=\boldsymbol{\sigma}^{(0)}(\mathbf{x})-\boldsymbol{\sigma}^{(i)}(\mathbf{x})$ represents the jump of the stress tensor across the coherent interface $\Gamma^{(i)}$ and $\nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)}(\mathbf{x})$ denoting the surface divergence of $\boldsymbol{\sigma}^{(s i)}(\mathbf{x})$ is defined by

$$
\nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)}(\mathbf{x})=\nabla \boldsymbol{\sigma}^{(s i)}(\mathbf{x}): \mathbf{P}(\mathbf{x}),
\tag{6}
$$

with $\mathbf{P}(\mathbf{x})$ defined as Eq. (2) and $\nabla$ being the usual 3D gradient operator. In particular, in the cylindrical coordinate system $(r, \theta, z)$ associated with a cylindrical basis $\left\{\mathbf{e}_{r}, \mathbf{e}_{\theta}, \mathbf{e}_{z}\right\}$, the surface divergence $\nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)}$ takes the following form

$$
\nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)}=-\frac{\sigma_{\theta \theta}^{(s i)}}{r} \mathbf{e}_{r}+\left[\frac{\partial \sigma_{\theta \theta}^{(s i)}}{r \partial \theta}+\frac{\partial \sigma_{\theta z}^{(s i)}}{\partial z}\right] \mathbf{e}_{\theta}+\left[\frac{\partial \sigma_{\theta z}^{(s i)}}{r \partial \theta}+\frac{\partial \sigma_{z z}^{(s i)}}{\partial z}\right] \mathbf{e}_{z}.
\tag{7}
$$

The behavior of the interface $\Gamma^{(i)}$ between the matrix and ith-fiber is assumed to be linearly elastic and characterized by the two-dimensional (2D) Hooke law:

$$
\boldsymbol{\sigma}^{(s i)}(\mathbf{x})=\mathbb{C}^{(s i)}(\mathbf{x}) \boldsymbol{e}^{(s i)}(\mathbf{x})
$$

or

$$
\boldsymbol{e}^{(s i)}(\mathbf{x})=\mathbb{S}^{(s i)}(\mathbf{x}) \boldsymbol{\sigma}^{(s i)}(\mathbf{x})
\tag{8}
$$

with $\mathbf{x} \in \Gamma^{(i)}$. Here $\mathbb{C}^{(s i)}(\mathbf{x})$ and $\mathbb{S}^{(s i)}(\mathbf{x})$ are the 2D fourth-order elastic stiffness and compliance tensors of $\Gamma^{(i)}$, respectively.

In this work, the constituent phases of the fibrous nanocomposite are assumed to be all isotropic and the interface $\Gamma^{(i)}$ between the matrix and the ith-fiber is taken to be also isotropic in the tangential plane. Correspondingly, the elastic tensors $\mathbb{C}^{(i)}(\mathbf{x})$, $\mathbb{C}^{(s i)}(\mathbf{x}), \mathbb{S}^{(i)}(\mathbf{x})$ and $\mathbb{S}^{(s i)}(\mathbf{x})$ of the phases and interfaces have the forms (see e.g., [12])

$$
\mathbb{C}^{(p)}=\frac{E_{p}}{1-2 \nu_{p}} \mathbb{J}+\frac{E_{p}}{1+\nu_{p}} \mathbb{K}, \quad \mathbb{S}^{(p)}=\frac{1-2 \nu_{p}}{E_{p}} \mathbb{J}+\frac{1+\nu_{p}}{E_{p}} \mathbb{K}, \tag{9}
$$

$$
\mathbb{C}^{(s i)}=\frac{E_{s i}}{2\left(1-\nu_{s i}\right)} \mathbf{P} \otimes \mathbf{P}+\frac{E_{s i}}{1+\nu_{s i}}\left\{\mathbb{T}-\frac{1}{2} \mathbf{P} \otimes \mathbf{P}\right\}, \tag{10}
$$

$$
\mathbb{S}^{(s i)}=\frac{1-\nu_{s i}}{2 E_{s i}} \mathbf{P} \otimes \mathbf{P}+\frac{1+\nu_{s i}}{E_{s i}}\left\{\mathbb{T}-\frac{1}{2} \mathbf{P} \otimes \mathbf{P}\right\}. \tag{11}
$$

In the above expressions, $E_{p}$ and $\nu_{p}$ designate the Young's modulus and Poisson's ratio of phase $p$; $E_{s i}$ and $\nu_{s i}$ denote the Young's modulus and Poisson's ratio of the interface $\Gamma^{(i)}$; $\mathbb{J}=\frac{1}{3} \mathbf{I} \otimes \mathbf{I}$ and $\mathbb{K}=\mathbb{I}-\mathbb{J}$ with $\mathbb{I}=\mathbf{I} \overline{\otimes} \mathbf{I}$ being the fourth-order identity tensor.

At the macroscopic scale, the fibrous nanocomposite under investigation is assumed to be statistically homogeneous. Moreover, due to the linearity of the local constitutive laws of each phase and to that of the imperfect interface $\Gamma^{(i)}$, the corresponding effective elastic behavior remains linearly elastic and takes the form

$$
\boldsymbol{\Sigma}=\mathbb{C}^{*} \mathbf{E} \quad \text { or } \quad \mathbf{E}=\mathbb{S}^{*} \boldsymbol{\Sigma}.
\tag{12}
$$

Here, $\mathbb{C}^{*}$ and $\mathbb{S}^{*}$ are the effective stiffness and compliance tensors of the fibrous nanocomposite, respectively; $\boldsymbol{\Sigma}$ and $\mathbf{E}$ denoting the macroscopic stress and strain tensors are defined as

$$
\boldsymbol{\Sigma}=\frac{1}{2|\Omega|} \int_{\partial \Omega}(\boldsymbol{\sigma} \mathbf{n}) \otimes^{s} \mathbf{x} \mathrm{d} \mathbf{x},
\tag{13}
$$

$$
\mathbf{E}=\frac{1}{2|\Omega|} \int_{\partial \Omega} \mathbf{u} \otimes^{s} \nu \mathrm{d} \mathbf{x}
\tag{14}
$$

where $\mathbf{n}$ is the outward unit normal vector to $\partial \Omega$; $|\Omega|$ represents the volume of $\Omega$ and the symbol $\otimes^{s}$ denotes the symmetric tensorial product such that $\mathbf{a} \otimes^{s} \mathbf{b}=\frac{1}{2}(\mathbf{a} \otimes \mathbf{b}+\mathbf{b} \otimes \mathbf{a})$ for any two vectors $\mathbf{a}$ and $\mathbf{b}$. It can be shown that the macroscopic strain tensor $\mathbf{E}$ can be defined as the volume average of the local strain field over the representative volume element $\Omega$ while the macroscopic stress tensor $\boldsymbol{\Sigma}$ is not simply the volume average of the stress field over $\Omega$

because of the discontinuity of the traction vector across the interface $\Gamma^{(i)}$.

## 3. Computation of the effective elastic moduli by FFT

Now, let $\Omega$ be subjected to the following prescribed uniform displacements on its external surface $\partial\Omega$:
$$
\mathbf{u}(\mathbf{x})=\mathbf{E}^{0} \mathbf{x}, \quad \mathbf{x} \in \partial \Omega,\qquad(15)
$$
where $\mathbf{E}^{0}$ is a constant strain tensor. Under the boundary conditions (15), it can be shown from (13) that the macroscopic strain tensor $\mathbf{E}$ is equal to $\mathbf{E}^{0}$. Next, owing to the fact that the fibrous nanocomposite under consideration is periodic in the plan transverse to the fibers, it suffices to consider now a unit cell $\mathcal{U}$ defined, for example, by
$$
\mathcal{U}=\left\{\mathbf{x} \in \Omega \mid-\lambda_{\alpha} \leq x_{\alpha} \leq \lambda_{\alpha},-\frac{h}{2} \leq x_{3} \leq \frac{h}{2}\right\}\qquad(16)
$$
where $\alpha=1,2 ; 2 \lambda_{1}$ and $2 \lambda_{2}$ are the dimensions of the unit cell in the plane perpendicular to the fiber direction and $h$ denotes the fiber length which should be taken to be sufficiently larger than both $\lambda_{1}$ and $\lambda_{2}$.

By introducing the characteristic function $\chi^{(i)}$ for the $i$th-fiber $(i=1,2, \ldots, N)$, such that $\chi^{(i)}(\mathbf{x})=1$ for $\mathbf{x} \in \omega^{(i)}$ and $\chi^{(i)}(\mathbf{x})=0$ for $\mathbf{x} \notin \omega^{(i)}$, the local elastic stiffness tensor field can be now expressed as
$$
\mathbb{C}(\mathbf{x})=\sum_{i=1}^{N} \chi^{(i)}(\mathbf{x}) \mathbb{C}^{(i)}+\left\{1-\sum_{i=1}^{N} \chi^{(i)}(\mathbf{x})\right\} \mathbb{C}^{(0)},\qquad(17)
$$
where the fourth-order elastic stiffness tensors $\mathbb{C}^{(i)}$ and $\mathbb{C}^{(0)}$ are given by (9). Accounting for the presence of the coherent imperfect interface, the equilibrium equation is then rewritten in the following form:
$$
\nabla \cdot[\mathbb{C} \boldsymbol{\varepsilon}]-\sum_{i=1}^{N}\left[\boldsymbol{\sigma}^{(i)}-\boldsymbol{\sigma}^{(0)}\right] \mathbf{n}delta_{\Gamma^{(i)}}=0\qquad(18)
$$
where $\delta_{\Gamma^{(i)}}(\mathbf{x})$ stands for the Dirac delta function on the interface $\Gamma^{(i)}$ between the matrix and the $i$th-fiber.

By introducing a "reference medium" whose elastic stiffness tensor is denoted by $\overline{\mathbb{C}}$ and by setting $\Delta \mathbb{C}(\mathbf{x})=\mathbb{C}(\mathbf{x})-\overline{\mathbb{C}}$, Eq. (18) can be recast into
$$
\nabla \cdot\left\{[\overline{\mathbb{C}}+\Delta \mathbb{C}] \boldsymbol{\varepsilon}\right\}-\sum_{i=1}^{N}\left[\boldsymbol{\sigma}^{(i)}-\boldsymbol{\sigma}^{(0)}\right] \mathbf{n}delta_{\Gamma^{(i)}}=0.\qquad(19)
$$

The strain tensor field $\boldsymbol{\varepsilon}(\mathbf{x})$ can be decomposed into two parts:
$$
\boldsymbol{\varepsilon}(\mathbf{x})=\mathbf{E}^{0}+\boldsymbol{\varepsilon}^{*}(\mathbf{x})\qquad(20)
$$
where $\mathbf{E}^{0}$ is the macroscopic strain field and $\boldsymbol{\varepsilon}^{*}(\mathbf{x})$ represents the periodic perturbation strain field. By accounting for Eqs. (5) and (20), Eq. (19) becomes
$$
\nabla \cdot\left\{[\overline{\mathbb{C}}\left[\mathbf{E}^{0}+\boldsymbol{\varepsilon}^{*}\right]+\boldsymbol{\tau}\right\}+\sum_{i=1}^{N} \nabla_{s} \cdot \boldsymbol{\sigma}^{(s i)} \delta_{\Gamma^{(i)}}=0,\qquad(21)
$$
where the polarization tensor field $\boldsymbol{\tau}(\mathbf{x})$ is defined through
$$
\boldsymbol{\tau}=\Delta \mathbb{C}\left[\mathbf{E}^{0}+\boldsymbol{\varepsilon}^{*}\right]=[\mathbb{C}-\overline{\mathbb{C}}] \boldsymbol{\varepsilon}.\qquad(22)
$$

By substituting Eq. (17) into the above equation, we obtain
$$
\boldsymbol{\tau}=\left(\mathbb{C}^{(0)}-\overline{\mathbb{C}}\right) \boldsymbol{\varepsilon}+\sum_{i=1}^{N}\left[\left(\mathbb{C}^{(i)}-\mathbb{C}^{(0)}\right) \chi^{(i)} \boldsymbol{\varepsilon}\right].\qquad(23)
$$

The periodic perturbation strain field $\boldsymbol{\varepsilon}^{*}(\mathbf{x})$ can be derived from a perturbation displacement field $\mathbf{u}^{*}(\mathbf{x})$:
$$
\boldsymbol{\varepsilon}^{*}=\frac{1}{2}\left[\nabla \mathbf{u}^{*}+\nabla^{T} \mathbf{u}^{*}\right].\qquad(24)
$$

Substitution of Eqs (6) and (24) into Eq. (21) gives
$$
\boldsymbol{\Phi}^{(1)}+\boldsymbol{\Phi}^{(2)}+\boldsymbol{\Phi}^{(3)}=\mathbf{0},\qquad(25)
$$
where $\boldsymbol{\Phi}^{(1)}(\mathbf{x}), \boldsymbol{\Phi}^{(2)}(\mathbf{x})$ and $\boldsymbol{\Phi}^{(3)}(\mathbf{x})$ are defined by
$$
\boldsymbol{\Phi}^{(1)}=\nabla \cdot\left[\overline{\mathbb{C}} \nabla \mathbf{u}^{*}\right], \quad \boldsymbol{\Phi}^{(2)}=\nabla \cdot \boldsymbol{\tau},\qquad(26)
$$

$$
\boldsymbol{\Phi}^{(3)}=\sum_{i=1}^{N} \nabla \boldsymbol{\sigma}^{(s i)}: \mathbf{P} \delta_{\Gamma^{(i)}}.\qquad(27)
$$

By substituting Eqs. (8) and (3) into Eq. (27), it follows that
$$
\boldsymbol{\Phi}^{(3)}=\sum_{i=1}^{N} \mathcal{A}^{(i)}: \boldsymbol{\varepsilon}+\sum_{i=1}^{N} \mathbb{B}^{(i)} \vdots \nabla \boldsymbol{\varepsilon}\qquad(28)
$$
where $A^{(i)}(\mathbf{x})$ and $\mathbb{B}^{(i)}(\mathbf{x})$ are the third- and fourth-order tensors whose components are determined by
$$
A_{p k l}^{(i)}=a_{p k l}^{(i)} \delta_{\Gamma^{(i)}}, \quad B_{p k l r}^{(i)}=b_{p k l r}^{(i)} \delta_{\Gamma^{(i)}}\qquad(29)
$$
with
$$
a_{p k l}^{(i)}=\left[\mathbb{C}_{p q m n, r}^{(s i)} T_{m n k l}+\mathbb{C}_{p q m n}^{(s i)} T_{m n k l, r}\right] P_{q r},\qquad(30)
$$

$$
b_{p k l r}^{(i)}=\mathbb{C}_{p q m n}^{(s i)} T_{m n k l} P_{q r}.\qquad(31)
$$

The explicit expressions of $a_{p k l}^{(i)}(\mathbf{x})$ and $b_{p k l r}^{(i)}(\mathbf{x})$ are provided in Appendix A for the case where the interface $\Gamma^{(i)}$ is isotropic.

Next, the local stress field $\boldsymbol{\sigma}(\mathbf{x})$ can be compactly expressed by
$$
\boldsymbol{\Sigma}=\mathbb{C}^{(0)} \boldsymbol{\varepsilon}+\sum_{i=1}^{N}\left(\mathbb{C}^{(i)}-\mathbb{C}^{(0)}\right) \chi^{(i)} \boldsymbol{\varepsilon}+\sum_{i=1}^{N} \boldsymbol{\sigma}^{(s i)} \delta_{\Gamma^{(i)}}.\qquad(32)
$$

The corresponding macroscopic stress tensor $\mathbf{S}$ defined by (13) takes the following form
$$
\begin{aligned}
\boldsymbol{\Sigma}= & \frac{1}{|\mathcal{U}|} \int_{\mathcal{U}}\left[\mathbb{C}^{(0)}+\sum_{i=1}^{N}\left(\mathbb{C}^{(i)}-\mathbb{C}^{(0)}\right) \chi^{(i)}\right] \boldsymbol{\varepsilon} \mathrm{d} \mathbf{x} \\
& -\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \int_{\Gamma^{(i)}} \mathbf{x} \otimes^{s}\left[\nabla \boldsymbol{\sigma}^{(s i)}: \mathbf{P}\right] \mathrm{d} \mathbf{x} \\
& +\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \int_{\partial \Gamma^{(i)}}\left[\boldsymbol{\sigma}^{(s i)} \overline{\mathbf{m}} \otimes^{s} \mathbf{x}+\boldsymbol{\sigma}^{(s i)} \underline{\mathbf{m}} \otimes^{s} \mathbf{x}\right] \mathrm{d} \mathbf{x}.
\end{aligned}\qquad(33)
$$

Here, $|\mathcal{U}|$ denotes the volume of $\mathcal{U}$; the first term of the right-hand side of (33) is the volume average stress over $\mathcal{U}$; the second one comes from the discontinuity of the stress field across the interface $\Gamma^{(i)}$; the third term is due to the fact that the interface $\Gamma^{(i)}$ is open; $\partial \Gamma^{(i)}$ is the boundary of $\Gamma^{(i)}$ with $\overline{\mathbf{m}}(\mathbf{x})$ and $\underline{\mathbf{m}}(\mathbf{x})$ being unit outward vectors, normal to the respective top and bottom surfaces of $\mathcal{U}$ (see Fig. 2).

For later use, it is convenient to introduce the following three second-order tensors:
$$
\boldsymbol{\Psi}^{(1)}=\left[\mathbb{C}^{(0)}+\sum_{i=1}^{N}\left(\mathbb{C}^{(i)}-\mathbb{C}^{(0)}\right) \chi^{(i)}\right] \boldsymbol{e},
\tag{34}
$$

$$
\boldsymbol{\Psi}^{(2)}=-\sum_{i=1}^{N} \mathbf{x} \otimes^{s}\left[\nabla \boldsymbol{\sigma}^{(s i)}: \mathbf{P}\right] \delta_{\Gamma^{(i)}},
\tag{35}
$$

$$
\boldsymbol{\Psi}^{(3)}=\sum_{i=1}^{N} \frac{1}{h}\left[\boldsymbol{\sigma}^{(s i)} \overline{\mathbf{m}} \otimes^{s} \mathbf{x}+\boldsymbol{\sigma}^{(s i)} \underline{\mathbf{m}} \otimes^{s} \mathbf{x}\right] \delta_{\Gamma^{(i)}}.
\tag{36}
$$

The combination of (27)–(31) with (35) results in
$$
\boldsymbol{\Psi}^{(2)}=-\sum_{i=1}^{N} \mathbb{Q}^{(i)} \boldsymbol{e}-\sum_{i=1}^{N} \mathfrak{M}^{(i)} \therefore \nabla \boldsymbol{e}
\tag{37}
$$
where $\mathbb{Q}^{(i)}(\mathbf{x})$ and $\mathfrak{M}^{(i)}(\mathbf{x})$ are the fourth- and fifth-tensors whose components are defined by
$$
Q_{p s k l}^{(i)}=q_{p s k l}^{(i)} \delta_{\Gamma^{(i)}}, \quad M_{p s k l r}^{(i)}=m_{p s k l r}^{(i)} \delta_{\Gamma^{(i)}}
\tag{38}
$$
with
$$
q_{p s k l}^{(i)}=\frac{1}{2}\left[a_{p k l}^{(i)} x_{s}+a_{s k l}^{(i)} x_{p}\right], m_{p s k l r}^{(i)}=\frac{1}{2}\left[b_{p k l r}^{(i)} x_{s}+b_{s k l r}^{(i)} x_{p}\right].
\tag{39}
$$

Substituting (3) and (8) into (36) yields
$$
\boldsymbol{\Psi}^{(3)}=\sum_{i=1}^{N} \mathbb{Y}^{(i)} \boldsymbol{e}
\tag{40}
$$
where $\mathbb{Y}^{(i)}(\mathbf{x})$ is specified by
$$
Y_{p s k l}^{(i)}=y_{p s k l}^{(i)} \delta_{\Gamma^{(i)}}
\tag{41}
$$
with
$$
\begin{aligned}
y_{p s k l}^{(i)}= & \frac{1}{2 h}\left[C_{p q m n}^{(s i)} T_{m n k l} \overline{\boldsymbol{m}}_{q} x_{s}+C_{s q m n}^{(s i)} T_{m n k l} \overline{\boldsymbol{m}}_{q} x_{p}\right] \\
& +\frac{1}{2 h}\left[C_{p q m n}^{(s i)} T_{m n k l} \underline{\boldsymbol{m}}_{q} x_{s}+C_{s q m n}^{(s i)} T_{m n k l} \underline{\boldsymbol{m}}_{q} x_{p}\right].
\end{aligned}
\tag{42}
$$

![](./images/811139233631698946_5.jpg)

Fig. 2. Open interface $\Gamma^{(i)}$ in a typical unit celle $U$.

In Appendix A, the expressions of $y_{p s k l}^{(i)}(\mathbf{x})$ are detailed for the case where $\Gamma^{(i)}$ is isotropic.

Now, let $\mathbf{F}(\mathbf{x})$ denote a generic field, which may be the displacement, polarization, strain or stress field. Applying the fast Fourier transform (FFT), $\mathbf{F}(\mathbf{x})$ admits the following representation in the Fourier space:
$$
\mathbf{F}(\mathbf{x})=\sum_{\boldsymbol{\xi}} \widehat{\mathbf{F}}(\boldsymbol{\xi}) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}.
\tag{43}
$$

In this expression, $\iota=\sqrt{-1}$ is the imaginary unit, $\boldsymbol{\xi}=\left(\xi_{1}, \xi_{2}, 0\right)=\left(n_{1} \pi / \lambda_{1}, n_{2} \pi / \lambda_{2}, 0\right)$ with $n_{1}$ and $n_{2}=-N_{k}+1,-N_{k}+2$, ..., 0,1,..., $N_{k}$ is a discrete 2D wave vector, and the summation has to be made for all the discrete wave vectors involved, whose number is equal to $2 N_{k} \times 2 N_{k}$.

Applying (43) with the appropriate field variable to $(26)_{1}$ and $(26)_{2}$, we obtain
$$
\Phi_{p}^{(1)}=-\sum_{\boldsymbol{\xi}} \overline{C}_{p q k l} \xi_{l} \xi_{q} \widehat{u}_{k}^{*}(\boldsymbol{\xi}) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}},
\tag{44}
$$

$$
\Phi_{p}^{(2)}=\sum_{\boldsymbol{\xi}} \widehat{\tau}_{p q}(\boldsymbol{\xi}) \iota \xi_{q} e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}.
\tag{45}
$$

In a similar way, using (43) for (22), we have
$$
\begin{aligned}
\tau_{p q}= & \sum_{\boldsymbol{\xi}}\left(C_{p q k l}^{(0)}-\overline{C}_{p q k l}\right) \widehat{\varepsilon}_{k l}(\boldsymbol{\xi}) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}+\sum_{i=1}^{N} \sum_{\boldsymbol{\xi}^{\prime}}\left(C_{p q k l}^{(i)}\right. \\
& \left.-C_{p q k l}^{(0)}\right) \chi^{(i)} e^{\iota \boldsymbol{\xi}^{\prime} \cdot \mathbf{x}} \widehat{\varepsilon}_{k l}\left(\boldsymbol{\xi}^{\prime}\right).
\end{aligned}
\tag{46}
$$

Here, the 2D discrete wave vector $\boldsymbol{\xi}^{\prime}$ is defined by $\boldsymbol{\xi}^{\prime}=\left(\xi_{1}^{\prime}, \xi_{2}^{\prime}, 0\right)=\left(n_{1}^{\prime} \pi / \lambda_{1}, n_{2}^{\prime} \pi / \lambda_{2}, 0\right)$ with $n_{1}^{\prime}$ and $n_{2}^{\prime}=-N_{k}+1,-N_{k}+2, \ldots, 0,1, \ldots, N_{k}$, and the Fourier transform of the characteristic function $\chi^{(i)} e^{\iota \boldsymbol{\xi}^{\prime} \cdot \mathbf{x}}$ is given by
$$
\chi^{(i)} e^{\iota \boldsymbol{\xi}^{\prime} \cdot \mathbf{x}}=\sum_{\boldsymbol{\xi}} \mathcal{F}\left[\chi^{(i)} e^{\iota \boldsymbol{\xi}^{\prime} \cdot \mathbf{x}}\right] e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}=\sum_{\boldsymbol{\xi}} \widehat{\chi}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}
\tag{47}
$$
where use has been made of the result
$$
\mathcal{F}\left[\chi^{(i)} e^{\iota \boldsymbol{\xi}^{\prime} \cdot \mathbf{x}}\right]=\frac{1}{|\mathcal{U}|} \int_{\omega^{(i)}} e^{-\iota\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x}=\widehat{\chi}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right).
\tag{48}
$$

By introducing Eq. (47) into Eq. (46), the polarization stress field can be rewritten as
$$
\begin{aligned}
\tau_{p q}= & \sum_{i=1}^{N} \sum_{\boldsymbol{\xi}, \boldsymbol{\xi}^{\prime}}\left(C_{p q k l}^{(i)}-C_{p q k l}^{(0)}\right) \widehat{\chi}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \widehat{\varepsilon}_{k l}\left(\boldsymbol{\xi}^{\prime}\right) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}+\sum_{\boldsymbol{\xi}}\left(C_{p q k l}^{(0)}\right. \\
& \left.-\overline{C}_{p q k l}\right) \widehat{\varepsilon}_{k l}(\boldsymbol{\xi}) e^{\iota \boldsymbol{\xi} \cdot \mathbf{x}}.
\end{aligned}
\tag{49}
$$

Noting that
$$
\sum_{\boldsymbol{\xi}^{\prime}} \widehat{\chi}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \widehat{\varepsilon}_{k l}\left(\boldsymbol{\xi}^{\prime}\right)=\left[\widehat{\chi}^{(i)} * \widehat{\varepsilon}_{k l}\right](\boldsymbol{\xi})
\tag{50}
$$
where the symbol $^{*}$ denotes the convolution product, Eq. (49) can be recast into

$$
\begin{aligned}
\tau_{p q}= & \sum_{i=1}^{N} \sum_{\xi}\left(C_{p q k l}^{(i)}-C_{p q k l}^{(0)}\right)\left[\widehat{\chi}^{(i)} * \widehat{\varepsilon}_{k l}\right](\xi) e^{\iota \xi \cdot \mathbf{x}}+\sum_{\xi}\left(C_{p q k l}^{(0)}\right. \\
& \left.-\bar{C}_{p q k l}\right) \widehat{\varepsilon}_{k l}(\xi) e^{\iota \xi \cdot \mathbf{x}}.
\end{aligned}
\tag{51}
$$

Consequently, the Fourier transform $\widehat{\boldsymbol{\tau}}(\boldsymbol{\xi})$ of the polarization field $\boldsymbol{\tau}(\mathbf{x})$ is given by
$$
\widehat{\tau}_{p q}=\left(C_{p q k l}^{(0)}-\bar{C}_{p q k l}\right) \widehat{\varepsilon}_{k l}+\sum_{i=1}^{N}\left(C_{p q k l}^{(i)}-C_{p q k l}^{(0)}\right)\left[\widehat{\chi}^{(i)} * \widehat{\varepsilon}_{k l}\right].
\tag{52}
$$

Applying Eq. (48) to Eq. (28) yields
$$
\Phi_{p}^{(3)}=\sum_{i=1}^{N} \sum_{\xi^{\prime}} A_{p k l}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}} \widehat{\varepsilon}_{k l}\left(\xi^{\prime}\right)+\sum_{i=1}^{N} \sum_{\xi^{\prime}} B_{p k l r}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}} \widehat{\varepsilon}_{k l r}\left(\xi^{\prime}\right)
\tag{53}
$$
with $\widehat{\varepsilon}_{k l r}\left(\xi^{\prime}\right)=\widehat{\varepsilon}_{k l}\left(\xi^{\prime}\right) \xi_{r}{ }^{\prime} \iota$.

In the Fourier space, we can write
$$
A_{p k l}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}}=\sum_{\xi} \mathcal{F}\left[A_{p k l}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}}\right](\xi) e^{\iota \xi \cdot \mathbf{x}}=\frac{1}{|\mathcal{U}|} \sum_{\xi} \widehat{A}_{p k l}^{(i)}\left(\xi-\xi^{\prime}\right) e^{\iota \xi \cdot \mathbf{x}},
\tag{54}
$$
$$
B_{p k l r}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}}=\sum_{\xi} \mathcal{F}\left[B_{p k l r}^{(i)} e^{\iota \xi^{\prime} \cdot \mathbf{x}}\right](\xi) e^{\iota \xi \cdot \mathbf{x}}=\frac{1}{|\mathcal{U}|} \sum_{\xi} \widehat{B}_{p k l}^{(i)}\left(\xi-\xi^{\prime}\right) e^{\iota \xi \cdot \mathbf{x}},
\tag{55}
$$
with
$$
\begin{aligned}
& \widehat{A}_{p k l}^{(i)}\left(\xi-\xi^{\prime}\right)=\int_{\Gamma^{(i)}} a_{p k l}^{(i)} e^{-\iota\left(\xi-\xi^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x}, \\
& \widehat{B}_{p k l r}^{(i)}\left(\xi-\xi^{\prime}\right)=\int_{\Gamma^{(i)}} b_{p k l r}^{(i)} e^{-\iota\left(\xi-\xi^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x}.
\end{aligned}
\tag{56}
$$

Using Eqs. (54) and (55) in Eq. (53) while accounting for
$$
\begin{aligned}
& \sum_{\xi^{\prime}} \widehat{A}_{p k l}^{(i)}\left(\xi-\xi^{\prime}\right) \widehat{\varepsilon}_{k l}\left(\xi^{\prime}\right)=\widehat{A}_{p k l}^{(i)} * \widehat{\varepsilon}_{k l}, \\
& \sum_{\xi^{\prime}} \widehat{B}_{p k l r}^{(i)}\left(\xi-\xi^{\prime}\right) \widehat{\varepsilon}_{k l r}\left(\xi^{\prime}\right)=\widehat{B}_{p k l r}^{(i)} * \widehat{\varepsilon}_{k l r},
\end{aligned}
\tag{57}
$$
we obtain
$$
\Phi_{p}^{(3)}=\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \sum_{\xi} \widehat{A}_{p k l}^{(i)} * \widehat{\varepsilon}_{k l} e^{\iota \xi \cdot \mathbf{x}}+\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \sum_{\xi} \widehat{B}_{p k l r}^{(i)} * \widehat{\varepsilon}_{k l r} e^{\iota \xi \cdot \mathbf{x}}.
\tag{58}
$$

Next, by introducing Eqs. (44), (45) and (58) into Eq. (25), the equilibrium equation in the Fourier space takes the form
$$
-\bar{C}_{p q k l} \xi_{l} \xi_{q} \widehat{u}_{k}^{*}+\widehat{\tau}_{p q}(\xi) \iota \xi_{q}+\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \widehat{A}_{p k l}^{(i)} * \widehat{\varepsilon}_{k l}+\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \widehat{B}_{p k l r}^{(i)} * \widehat{\varepsilon}_{k l r}=0.
\tag{59}
$$

By introducing the acoustic tensor $\overline{\mathbf{K}}$ with the components $\bar{K}_{p k}=\bar{C}_{p q k l} \xi_{l} \xi_{q}$, the perturbation part of the displacement field in the Fourier space can be derived from Eq. (59) as
$$
\widehat{u}_{k}^{*}=\bar{K}_{k p}^{-1} \widehat{\tau}_{p q} \iota \xi_{q}+\frac{\bar{K}_{k p}^{-1}}{|\mathcal{U}|} \sum_{i=1}^{N} \widehat{A}_{p v l}^{(i)} * \widehat{\varepsilon}_{v l}+\frac{\bar{K}_{k p}^{-1}}{|\mathcal{U}|} \sum_{i=1}^{N} \widehat{B}_{p v l r}^{(i)} * \widehat{\varepsilon}_{v l r}.
\tag{60}
$$

Applying (43) to Eq. (24), it follows that
$$
\widehat{\varepsilon}_{k t}^{*}=\frac{1}{2}\left[\widehat{u}_{k}^{*} \iota \xi_{t}+\widehat{u}_{t}^{*} \iota \xi_{k}\right].
\tag{61}
$$

Combining Eq. (60) with Eq. (61) leads to
$$
\begin{aligned}
\widehat{\varepsilon}_{k t}^{*}= & -\frac{1}{2}\left(\bar{K}_{k p}^{-1} \xi_{q} \xi_{t} \iota+K_{t p}^{-1} \xi_{q} \xi_{k}\right) \widehat{\tau}_{p q}+\frac{1}{2|\mathcal{U}|}\left(\bar{K}_{k p}^{-1} \iota \xi_{t}+\bar{K}_{t p}^{-1} \iota \xi_{k}\right) \\
& \times \sum_{i=1}^{N}\left(\widehat{A}_{p v l}^{(i)} * \widehat{\varepsilon}_{v l}+\widehat{B}_{p v l r}^{(i)} * \widehat{\varepsilon}_{v l r}\right).
\end{aligned}
\tag{62}
$$

By introducing (52) into (62) and by accounting for $\widehat{\boldsymbol{\varepsilon}}(\boldsymbol{\xi})=\widehat{\mathbf{E}}^{0}(\boldsymbol{\xi})+\widehat{\boldsymbol{\varepsilon}}^{*}(\boldsymbol{\xi})$ with
$$
\widehat{\mathbf{E}}^{0}(\xi)= \begin{cases}\mathbf{E}^{0} & \text { for } \boldsymbol{\xi}=\mathbf{0}, \\ \mathbf{0} & \text { for } \boldsymbol{\xi} \neq \mathbf{0},\end{cases}
\tag{63}
$$
we get
$$
\begin{aligned}
\widehat{E}_{k t}^{0}= & \widehat{\varepsilon}_{k t}+\widehat{\Gamma}_{k t p q}\left\{\left(C_{p q v l}^{(0)}-\bar{C}_{p q v l}\right) \widehat{\varepsilon}_{v l}+\sum_{i=1}^{N}\left(C_{p q v l}^{(i)}\right.\right. \\
& \left.\left.-C_{p q v l}^{(0)}\right) \widehat{\chi}^{(i)} * \widehat{\varepsilon}_{v l}\right\}-\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{k t p} \sum_{i=1}^{N}\left(\widehat{A}_{p v l}^{(i)} * \widehat{\varepsilon}_{v l}+\widehat{B}_{p v l r}^{(i)} * \widehat{\varepsilon}_{v l r}\right).
\end{aligned}
\tag{64}
$$

Here, the Fourier transforms of the Green operators $\widehat{\Gamma}_{k t p q}(\xi)$ and $\widehat{\Lambda}_{k t p}(\xi)$ are respectively given by
$$
\widehat{\Gamma}_{k t p q}=\frac{1}{4}\left(\bar{K}_{k p}^{-1} \xi_{q} \xi_{t}+\bar{K}_{t p}^{-1} \xi_{q} \xi_{k}+\bar{K}_{k q}^{-1} \xi_{p} \xi_{t}+\bar{K}_{t q}^{-1} \xi_{p} \xi_{k}\right),
\tag{65}
$$
$$
\widehat{\Lambda}_{k t p}=\frac{1}{2}\left(\bar{K}_{k p}^{-1} \iota \xi_{t}+\bar{K}_{t p}^{-1} \iota \xi_{k}\right).
$$

In particular, when the reference medium is assumed to be isotropic with Young modulus $\bar{E}$ and Poisson ratio $\bar{\nu}$, the expression of $\bar{K}_{i j}^{-1}$ is explicitly given by
$$
\bar{K}_{i j}^{-1}=\frac{2(1+\bar{\nu})}{\bar{E}|\xi|^{2}}\left[\delta_{i j}-\frac{1}{2(1-\bar{\nu})} \cdot \frac{\xi_{i} \xi_{j}}{|\xi|^{2}}\right],
\tag{66}
$$
where $|\boldsymbol{\xi}|$ denotes the norm of $\boldsymbol{\xi}$. The Fourier transform of $\boldsymbol{\Psi}^{(i)}(\mathbf{x})$ with $i=1,2,3$ is provided by
$$
\boldsymbol{\Psi}^{(i)}(\mathbf{x})=\sum_{\xi} \widehat{\boldsymbol{\Psi}}^{(i)}(\xi) e^{\iota \xi \cdot \mathbf{x}}
\tag{67}
$$
where
$$
\widehat{\Psi}_{p s}^{(1)}=C_{p s k l}^{(0)} \widehat{\varepsilon}_{k l}+\sum_{i=1}^{N}\left(C_{p s k l}^{(i)}-C_{p s k l}^{(0)}\right) \widehat{\chi}^{(i)} * \widehat{\varepsilon}_{k l},
\tag{68}
$$
$$
\widehat{\Psi}_{p s}^{(2)}=-\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N}\left(\widehat{Q}_{p s k l}^{(i)} * \widehat{\varepsilon}_{k l}+\widehat{M}_{p s k l r}^{(i)} * \widehat{\varepsilon}_{k l r}\right),
\tag{69}
$$

$$
\widehat{\Psi}_{p s}^{(3)}=\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N} \widehat{Y}_{p s k l}^{(i)} * \widehat{\varepsilon}_{k l},
\tag{70}
$$

with
$$
\widehat{Q}_{p s k l}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right)=\int_{\Gamma^{(i)}} q_{p s k l}^{(i)}(\mathbf{x}) e^{-\iota\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x},
\tag{71}
$$

$$
\widehat{M}_{p s k l r}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right)=\int_{\Gamma^{(i)}} m_{p s k l r}^{(i)}(\mathbf{x}) e^{-\iota\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x},
\tag{72}
$$

$$
\widehat{Y}_{p s k l}^{(i)}\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right)=\int_{\Gamma^{(i)}} y_{p s k l}^{(i)}(\mathbf{x}) e^{-\iota\left(\boldsymbol{\xi}-\boldsymbol{\xi}^{\prime}\right) \cdot \mathbf{x}} \mathrm{d} \mathbf{x}.
\tag{73}
$$

For simplicity, by using the two-to-one subscript identification $k t \equiv \tilde{t}, p q \equiv \tilde{q}, v l \equiv \tilde{l}, k l \equiv \bar{l}$ and $p s \equiv \bar{s}$ and by setting the values of $\tilde{t}, \tilde{q}, \tilde{l}$ and $\bar{s}$ be equal to $1,2, \ldots, 6$ when the values of $k t, p q, v l, k l$ and $p s$ are equal to $11,22,33,23$ or 32,13 or 31 and 12 or 21 , respectively, Eq. (64) can be rewritten as

$$
\begin{aligned}
\widehat{E}_{\tilde{t}}^{0}= & \widehat{e}_{\tilde{t}}+\widehat{\Gamma}_{\tilde{t} \tilde{q}}\left\{\left(C_{\tilde{q} \tilde{l}}^{(0)}-\overline{C}_{\tilde{q} \tilde{l}}\right) \widehat{e}_{\tilde{l}}+\sum_{i=1}^{N}\left(C_{\tilde{q} \tilde{l}}^{(i)}-C_{\tilde{q} \tilde{l}}^{(0)}\right) \hat{\chi}^{(i)} * \widehat{e}_{\tilde{l}}\right\} \\
& -\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{\tilde{t} p} \sum_{i=1}^{N} \widehat{A}_{p \tilde{l}}^{(i)} * \widehat{e}_{\tilde{l}}-\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{\tilde{t} p} \sum_{i=1}^{N} \widehat{B}_{p \tilde{l} r}^{(i)} * \widehat{e}_{\tilde{l} r}.
\end{aligned}
\tag{74}
$$

The above equation leads to the following system of linear equations

$$
\begin{aligned}
\widehat{E}_{\tilde{t}}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right)= & \widehat{e}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right) \delta_{\tilde{t} \tilde{l}} \delta^{(\alpha \beta)}+\widehat{\Gamma}_{\tilde{t} \tilde{q}}\left(\boldsymbol{\xi}^{(\beta)}\right)\left(C_{\tilde{q} \tilde{l}}^{(0)}-\overline{C}_{\tilde{q} \tilde{l}}\right) \widehat{e}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right) \delta^{(\alpha \beta)} \\
& +\widehat{\Gamma}_{\tilde{t} \tilde{q}}\left(\boldsymbol{\xi}^{(\alpha)}\right) \sum_{\beta=1}^{4 N_{k}^{2}} \sum_{i=1}^{N}\left(C_{\tilde{q} \tilde{l}}^{(i)}-C_{\tilde{q} \tilde{l}}^{(0)}\right) \hat{\chi}^{(i)}\left(\boldsymbol{\xi}^{(\alpha)}\right. \\
& \left.-\boldsymbol{\xi}^{(\beta)}\right) \widehat{e}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right)-\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{\tilde{t} p}\left(\boldsymbol{\xi}^{(\alpha)}\right) \sum_{\beta=1}^{4 N_{k}^{2}} \sum_{i=1}^{N} \widehat{B}_{p \tilde{l} r}^{(i)}\left(\boldsymbol{\xi}^{(\alpha)}\right. \\
& \left.-\boldsymbol{\xi}^{(\beta)}\right) \iota \xi_{r}^{(\beta)} \widehat{e}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right)-\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{\tilde{t} p}\left(\boldsymbol{\xi}^{(\alpha)}\right) \sum_{\beta=1}^{4 N_{k}^{2}} \sum_{i=1}^{N} \widehat{A}_{p \tilde{l}}^{(i)}\left(\boldsymbol{\xi}^{(\alpha)}\right. \\
& \left.-\boldsymbol{\xi}^{(\beta)}\right) \widehat{e}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right).
\end{aligned}
\tag{75}
$$

Above, $\alpha$ and $\beta=1,2, \ldots, 4 N_{k}^{2} ; \quad \boldsymbol{\xi}^{(\alpha)}=\left(\xi_{1}^{(\alpha)}, \xi_{2}^{(\alpha)}, 0\right) \quad$ and $\boldsymbol{\xi}^{(\beta)}=\left(\xi_{1}^{(\beta)}, \xi_{2}^{(\beta)}, 0\right)$ with $\xi_{m}^{(\alpha)}=n_{m}^{(\alpha)} \pi / \lambda_{m}$ and $\xi_{m}^{(\beta)}=n_{m}^{(\beta)} \pi / \lambda_{m}(m=1$ or $2, n_{m}^{(\alpha)}$ and $n_{m}^{(\beta)}=-N_{k}+1,-N_{k}+2, \ldots, 0,1, \ldots, N_{k}) ; \delta^{(\alpha \beta)}$ is the Kronecker symbol defined as $\delta^{(\alpha \beta)}=1$ for $\alpha=\beta$ and $\delta^{(\alpha \beta)}=0$ otherwise. The resolution of the system of linear equation (75) is detailed in Appendix B.

The macroscopic stress defined in (33) can be determined from the Fourier transform of the functions $\Psi_{\bar{s}}^{(1)}(\mathbf{x}), \Psi_{\bar{s}}^{(2)}(\mathbf{x})$ and $\Psi_{\bar{s}}^{(3)}(\mathbf{x})$ by setting the wave vector be equal to zero, $\boldsymbol{\xi}=0$, in Eqs. 68-70. Thus,

$$
\begin{aligned}
\Sigma_{\bar{s}}= & C_{\bar{s} \tilde{l}}^{(0)} \widehat{e}_{\tilde{l}}(\mathbf{0})+\sum_{i=1}^{N}\left(C_{\bar{s} \tilde{l}}^{(i)}-C_{\bar{s} \tilde{l}}^{(0)}\right)\left[\hat{\chi}^{(i)} * \widehat{e}_{\tilde{l}}\right](\mathbf{0}) \\
& -\frac{1}{|\mathcal{U}|} \sum_{i=1}^{N}\left\{\left[\widehat{Q}_{\bar{s} \tilde{l}}^{(i)} * \widehat{e}_{\tilde{l}}\right](\mathbf{0})+\left[\widehat{M}_{\bar{s} \tilde{l} r}^{(i)} * \widehat{e}_{\tilde{l} r}\right](\mathbf{0})-\left[\widehat{Y}_{\bar{s} \tilde{l}}^{(i)} * \widehat{e}_{\tilde{l}}\right](\mathbf{0})\right\}
\end{aligned}
\tag{76}
$$

At the macroscopic scale, as mentioned in Section 2, the fibrous nanocomposite is assumed to be statistically homogeneous and the corresponding effective elastic behavior is expressed by Eq. (12). In this work, we are interested in the particular important case where nanofibers are squarely or hexagonally distributed in the matrix phase. In this case, with the moduli of Hill [40] defined by

$$
\begin{aligned}
& k^{*}=\frac{1}{2}\left(L_{1111}+L_{1122}^{*}\right), m^{*}=\frac{1}{2}\left(L_{1111}^{*}-L_{1122}^{*}\right), \\
& l^{*}=L_{1133}^{*}=L_{2233}^{*}, \quad G^{*}=L_{2323}^{*}=L_{3131}^{*}, \\
& n^{*}=L_{3333}^{*}, G^{*^{\prime}}=L_{1212}^{*},
\end{aligned}
\tag{77}
$$

where $C_{i j k l}^{*}$ denotes the components of the effective stiffness tensor $\mathbb{C}^{*}$, the macroscopic constitutive relation takes the following matrix form:

$$
\begin{aligned}
{\left[\begin{array}{c}
\Sigma_{1} \\
\Sigma_{2} \\
\Sigma_{3} \\
\sqrt{2} \Sigma_{4} \\
\sqrt{2} \Sigma_{5} \\
\sqrt{2} \Sigma_{6}
\end{array}\right] } & =\left[\begin{array}{cccccc}
k^{*}+m^{*} & k^{*}-m^{*} & l^{*} & 0 & 0 & 0 \\
k^{*}-m^{*} & k^{*}+m^{*} & l^{*} & 0 & 0 & 0 \\
l^{*} & l^{*} & n^{*} & 0 & 0 & 0 \\
0 & 0 & 0 & 2 G^{*} & 0 & 0 \\
0 & 0 & 0 & 0 & 2 G^{*} & 0 \\
0 & 0 & 0 & 0 & 0 & 2 G^{*^{\prime}}
\end{array}\right] \\
& \times\left[\begin{array}{c}
E_{1} \\
E_{2} \\
E_{3} \\
\sqrt{2} E_{4} \\
\sqrt{2} E_{5} \\
\sqrt{2} E_{6}
\end{array}\right].
\end{aligned}
\tag{78}
$$

Physically, $k^{*}$ and $m^{*}$ designate the effective transverse bulk and shear moduli; $G^{*}$ denotes the effective anti-plane longitudinal shear modulus whereas $G^{*^{\prime}}$ symbolizes the effective in-plane plane shear modulus; $n^{*}$ and $l^{*}$ stand for the effective longitudinal and transverse moduli. In particular, when the fibrous nanocomposite under consideration is macroscopically transversely isotropic with respect to the fiber direction, it is immediate that $G^{*}=m^{*}$.

By successively setting the non-zero components of the imposed macroscopic strain tensor in (15) to be such that $\mathrm{E} \tilde{t}=\mathrm{Ef} 0=1$ with $\tilde{t}=1,2$ or 6 , we can calculate the effective moduli $k^{*}, m^{*}$ and $G^{*^{\prime}}$ in (78). Further, by imposing the boundary conditions (15) with the non-zero macroscopic component $E_{\tilde{t}}=E_{\tilde{t}}^{0}=1$ with $\tilde{t}=4$ or 5 , we can compute the effective module $G^{*}$.

In addition, by using the two exact connections established by Chen and Dvorak [8] (Eq. (13) in Ref. [8]) for the effective elastic moduli of a two-phase nanocomposite with circular cylindrical nanofibers, the effective longitudinal and transverse moduli $l^{*}$ and $n^{*}$ can be indirectly determined in terms of the effective transverse bulk modulus $k^{*}$.

## 4. Numerical examples, comparisons and discussions

### 4.1. Materials with cylindrical nanopores of circular cross-section

The FFT method presented in the precedent section is first applied to compute the effective elastic moduli of a porous medium consisting of a solid matrix weakened by unidirectional nanopores whose cross-sections are circular and of the same radius $R_{i}$. The nanopores are assumed to be either squarely or hexagonally distributed in the plane transverse to the nanopores. The Young's modulus and Poisson's ratio of the matrix are chosen to be $E_{0}=70 \mathrm{GPa}$ and $\nu_{0}=0.32$.

Three sets of numerical values are adopted for the surface elastic moduli of cylindrical nanopores (see Table 1). These surface elastic moduli correspond to those used by Miller and Shenoy [2] and Sharma and Dasgupta [3]. The numerical results obtained for the effective elastic moduli of the porous material corresponding to the surface $A$ or $B$ are indexed by $A$ or $B$ whereas the relevant numerical

results which do not account for the surface stress of nanopores are indicated by C. It can be seen from Table 1 that some surface moduli can be negative. However, this does not mean that the corresponding value of the energy function can be negative; otherwise, this would violate some thermodynamic principles. In fact, such a paradox can be explained by the fact that the surface or interface never exists with no bulk material. The total energy function must be defined as the energy function of the surface plus the one of the bulk material. For this reason, even the energy function of the surface can be negative, the total energy function can never be negative. Often, the surface moduli are determined by using the molecular dynamics computations.

In order to study the dependencies of the effective elastic moduli of the porous material under consideration on the size and distribution of the nanopores in the matrix phase, the radius $R_i$ of the cross-section of nanopores is set to vary from 1 to 50nm while the nanopores fraction, denoted by $f$, is kept constant with $f$=0.2.

The numerical results obtained for the effective elastic moduli of the porous material incorporating surface effects are first normalized with respect to the corresponding ones without accounting for the surface effects and then plotted in terms of the nanopore radius in Figs. 3-8. These values of the effective elastic moduli of the porous material are compared with both the relevant estimates obtained by Le Quang and He [34] using GSCM and the corresponding ones in the case where the nanopores are free from the surface stress (surface C). It can be seen from Figs. 3-8 that: (i) the difference between the effective elastic moduli obtained with surfaces $A$ and $B$ and the corresponding ones with surface $C$ decreases when the nanopore radius $R_i$ increases; (ii) the effective elastic moduli obtained with surfaces $A$ and $B$ depend on the nanopore radius $R_i$ whereas the corresponding ones with surface $C$ is independent of $R_i$; (iii) the effect of the surface stress becomes negligible when $R_i$ is larger than 50 nm; (iv) the effective elastic moduli obtained with surfaces $A$ and $B$ are in very good agreement with the estimates obtained by Le Quang and He [34] with the aid of GSCM.

In addition, by comparing in Fig. 9 the values of the normalized effective transverse bulk moduli $k^*/k_M$ with the numerical ones provided by applying the XFEM/level-set approach proposed by Yvonnet et al. [35], a good agreement is observed between them.

### 4.2. Materials with cylindrical nanopores of non-circular cross-section
The numerical method based on FFT is now applied to materials with cylindrical nanopores whose cross-sections are non-circular. In particular, we study the effects of different shapes of cross-sections on the effective elastic moduli of nanoporous materials (see Fig. 10). To describe a class of non-circular cross-sections, we use the system of polar coordinates $(R,\theta)$ and express the radius $R_i$ of a nanopore as a function of $\theta$ as follows:

$$
R_{i}(\theta)=R_{0}+A \sin (B \theta), \quad(79)
$$

where $R_0$ is a reference radius, $B$ denotes the number of oscillations and $A$ corresponds to the amplitude of oscillations. In this example, three cases cross-sections are considered: (i) circular shape with $A$=0; (ii) non-convex shape of 4 oscillations with $A$=$0.4R_0$ and $B$=4; (ii) non-convex shape of 8 oscillations with $A$=$0.4R_0$ and $B$=8.

<table>
<caption>Table 1
The elastic moduli of nanopore surfaces.</caption>
<thead>
<tr>
<th>Surface</th>
<th>$E_{si}(GPa\cdot m)$</th>
<th>$\nu_{si}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>$-7.58576×10^{-9}$</td>
<td>0.39</td>
</tr>
<tr>
<td>B</td>
<td>$-1.59233×10^{-9}$</td>
<td>1.123</td>
</tr>
<tr>
<td>C</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

![](./images/811139233631698946_6.jpg)

Fig. 3. The ratio $k^*/k_C^*$ versus the void radius $R_i$.

![](./images/811139233631698946_7.jpg)

Fig. 4. The ratio $m^*/m_C^*$ versus the void radius $R_i$.

![](./images/811139233631698946_8.jpg)

Fig. 5. The ratio $n^*/n_C^*$ versus the void radius $R_i$.

Correspondingly, the area of the cross-section of a cylindrical nanopore is given by

![](./images/811139233631698946_9.jpg)

Fig. 6. The ratio $I^{*} / I_{C}^{*}$ versus the void radius $R_{i}$.

![](./images/811139233631698946_10.jpg)

Fig. 7. The ratio $G^{*} / G_{C}^{*}$ versus the void radius $R_{i}$.

![](./images/811139233631698946_11.jpg)

Fig. 8. The ratio $G^{*} / G_{C}^{*}$ versus the void radius $R_{i}$.

$$
S=\frac{1}{8 B}\left[4 A^{2} B \pi+8 A R_{0}+8 B \pi R_{0}^{2}-8 A R_{0} \cos (2 B \pi)-A^{2} \sin (4 B \pi)\right).
\tag{80}
$$

With the void volume fraction $f=0.2$, the values of the ratio $k^{*} / \kappa_{0}$ are plotted in Fig. 11 in terms of $R_{0}$ for the two non-convex shapes of four and eight oscillations as well as for the circular shape. The numerical values obtained are then compared with the relevant numerical ones provided by Yvonnet et al. [35] by using XFEM/level set approach. It can be seen from Fig. 11 a good agreement exists between the results given by the two numerical methods.

### 4.3. Composites with cylindrical nanofibers

The third example concerns a unidirectional nanofibrous composite consisting of a host matrix phase in which identically cylindrical nanofibers are periodically embedded. In this example, the nanofibers are assumed to be softer than the matrix phase and have circular across-sections of same radius $R_{i}$. Three typical nanostructures of fibrous nanocomposites with squared, hexagonal and random distributions of the cylindrical nanofibers are considered. In particular, for a random distribution of cylindrical nanofibers, each unit cell contains 100 nanofibers and the results obtained for the effective elastic moduli correspond to the mean values from 5 realizations. For example, a typical realization of the random distribution of cylindrical nanofibers is shown in Fig. 12.

Moreover, in order to analyze the effects of the interface-to-volume ratio on the effective elastic moduli of the fibrous nanocomposite under consideration, the nanofiber radius $R_{i}$ is set to vary from 1 to $50 \mathrm{~nm}$ while the nanofiber volume fraction is fixed as $f=0.3$. The Young's modulus and Poison's ratio of the matrix and nanofibers are $E_{0}=2 E_{i}=70 \mathrm{GPa}$ and $\nu_{0}=\nu_{i}=0.25$. The Young's modulus and Poison's ratio of the coherent imperfect interface are chosen to be such that $E_{s i} / E_{0}=1.1636 \times 10^{-9} m$ and $\nu_{s i}=0.45$. These values of the material parameters correspond to those used by Le Quang and He [12].

The normalized effective elastic moduli provide by the present method based on FFT are plotted versus the parameter $\alpha=\log (2 f /$ $R_{i})=\log (S / V)$ in Figs. 13-18. In fact, the ratio $2 f / R_{i}$ correspond to the ratio of the fiber/matrix interface area $S$ to the volume $V$ of a unit cell. These results for the effective elastic moduli are also compared with the closed-form estimates obtained by Le Quang and He [34] using GSCM and with the corresponding first-order lower and upper bounds for the effective elastic moduli derived by Le Quang

![](./images/811139233631698946_12.jpg)

Fig. 9. The ratio $k^{*} / \kappa_{M}$ versus the void radius $R_{i}$.

![](./images/811139233631698946_13.jpg)

Fig. 10. Different cross-sections of cylindrical nanopores.

![](./images/811139233631698946_14.jpg)

Fig. 11. The ratio $k^*/k_0$ versus the void radius $R_i$ for different shapes of nanopores.

and He [12]. It is seen from Figs. 13-18 that:

(i) By applying the present numerical method, the values obtained for the effective elastic moduli of fibrous nanocomposites with the squared, hexagonal and random distributions of cylindrical nanofibers are well situated between the first-order upper and lower bounds.

(ii) The effective elastic moduli of fibrous nanocomposites with squared, hexagonal and random distributions of the cylindrical nanofibers are very close to the estimates of Le Quang and He [34]. The same observation has been mentioned in the work of Yvonnet et al. [35] with applying XFEM/level-set approach. Consequently, we can conclude that the estimation using GSCM is an excellent approximation for the effective elastic moduli of periodic composites with squared, hexagonal and random distributions of the circular cylindrical nanofibers.

(iii) Although the nanofibers phase is softer than the matrix phase, due to the effect of imperfect interfaces, the effective elastic moduli increases when the inhomogeneity volume fraction augments. This is quite different from the relevant results in the classical case with perfect interfaces. This important property of fibrous nanocomposites can be explained as follows. When the size of fibers decreases at nanoscale, the interface stress around the fibers becomes important and has the dominant effect on the effective rigidity of nano-fibrous composites. For this reason, the effective elastic moduli of composites with nanopores may achieve or even exceed the stiffness of the composites with nanofibres. This exceptional property of nano-fibrous composites can be obtained only when the fiber interface elastic moduli satisfy certain conditions. In general, we cannot derive explicitly and analytically these conditions. However, in particular case with nanoporous composites, Duan and his co-authors showed in Ref. [41] that the effective transverse bulk can exceed the corresponding one of the matrix phase if the following condition holds:

$$
R_{\mathrm{i}}<\frac{E_{\mathrm{si}}\left(1+\nu_{0}\right)\left(1-2 \nu_{0}\right)}{E_{0}\left(1-\nu_{\mathrm{si}}^{2}\right)}. \tag{81}
$$

![](./images/811139233631698946_15.jpg)

Fig. 12. A typical unit cell of a fibrous nanocomposite containing 100 randomly distributed nanofibers.

![](./images/811139233631698946_16.jpg)

Fig. 13. The ratio $k^*/k_0$ versus the surface-to-volume ratio $\alpha$=log(S/V).

(iv) It is interesting to observe from Fig. 13 that all curves converge to a point when $\alpha$=8.51. This can be explained by the fact that when alpha = 8.51, the strain field in the fibrous nanocomposite is uniform and equal exactly to the prescribed constant strain $\mathbf{E}^{0}$ at the external surface of the fibrous nanocomposite in Eq. (15). This is a particular case in which the strain field of the fibrous nanocomposite can be determined exactly. Consequently, the upper and lower bounds of the effective transverse bulk moduli $k^*$ take the same value. Furthermore, this explains clearly that, all other estimation values of the effective transverse bulk modulus $k^*$ which have to be, in general, situated between the upper and lower bounds must take the identical value of their upper and lower bounds

![](./images/811139233631698946_17.jpg)

Fig. 14. The ratio $m^{*}/\mu_{0}$ versus the surface-to-volume ratio $\alpha$=log(S/V).

![](./images/811139233631698946_18.jpg)

Fig. 15. The ratio $n^{*}/\mu_{0}$ versus the surface-to-volume ratio $\alpha$=log(S/V).

![](./images/811139233631698946_19.jpg)

Fig. 16. The ratio $l^{*}/\mu_{0}$ versus the surface-to-volume ratio $\alpha$=log(S/V).

bounds. This remark has been also mentioned in the work of Le Quang and He [12].

![](./images/811139233631698946_20.jpg)

Fig. 17. The ratio $G^{*}/\mu_{0}$ versus the surface-to-volume ratio $\alpha$=log(S/V).

![](./images/811139233631698946_21.jpg)

Fig. 18. The ratio $G'^{*}/\mu_{0}$ versus the surface-to-volume ratio $\alpha$=log(S/V).

## 5. Concluding remarks

In this work, the coherent imperfect interface model has been adopted for the nanofiber-matrix interfaces. A numerical method based on the fast Fourier transform has been elaborated to compute the effective elastic moduli of periodic fibrous nanocomposites. In contrast with the case of classical composites with imperfect fiber-matrix interfaces, the results obtained for the effective elastic moduli of fibrous nanocomposites show that they depend not only on the material properties of the matrix and nanofiber phases but also on the size of the cross-section of nanofibers as well as the material properties of the matrix-nanofiber interfaces. These effects increase significantly when the fiber size becomes small, displaying a significant size effect. Moreover, in the present work, the dependencies of the effective elastic moduli of periodic fibrous nanocomposites on the shapes and distributions of nanofibers embedded in the matrix phase have also been studied.

Compared with the mostly used numerical method based on the finite element method (FEM), the proposed numerical method does not need to mesh the microstructure of composites. For this reason, it has no difficulties related to meshing. In addition, avoiding the difficulties of FEM in modelling the interfaces between the different phases of composites with some discontinuities conditions, the

method presented in this work achieves the description of the interfaces by using the work characteristic function which is explicitly determined and depends only on the form of the cross-section of fibers.

Finally, the basic idea underlying the numerical method based on the fast Fourier transform incorporating coherent imperfect interfaces elaborated in the present work can be adapted for periodic fibrous nanocomposites with spring imperfect interfaces and for periodic elastic fibrous nanocomposites at finite strain. On the other hand, we note that all the results obtained in the present work hold under the condition that the nanofibers of composites are all cylindrical and aligned. It should be interesting to develop the present method for the case of composites with nanoparticles

## Appendix A. Appendices.

### A. Derivations of $a_{pkl}^{(i)}(\mathbf{x}),\ b_{pklr}^{(i)}(\mathbf{x})$ and. $y_{pskl}^{(i)}(\mathbf{x})$

First, Eq. (10) et (4) can be rewritten in the index form as follows:
$$
I_{p q m n}^{(s i)}=\kappa_{s i} P_{p q} P_{m n}+2 \mu_{s i}\left[T_{p q m n}-\frac{1}{2} P_{p q} P_{m n}\right], \tag{A-1}
$$

$$
T_{p q m n}=\frac{1}{2}\left[P_{p m} P_{q n}+P_{p n} P_{q m}\right], \tag{A-2}
$$

$$
T_{m n k l}=\frac{1}{2}\left[P_{m k} P_{n l}+P_{m l} P_{n k}\right]. \tag{A-3}
$$

Next, by introducing (A-1), (A-2) and (A-3) into (30), it follows that
$$
\begin{aligned}
a_{p k l}^{(i)}= & \frac{1}{2}\left(\kappa_{s i}-\mu_{s i}\right)\left(P_{p q, r} P_{m n} P_{m k} P_{n l} P_{q r}+P_{p q} P_{m n, r} P_{m k} P_{n l} P_{q r}\right. \\
& +P_{p q, r} P_{m n} P_{m l} P_{n k} P_{q r}+P_{p q} P_{m n, r} P_{m l} P_{n k} P_{q r} \\
& +\frac{1}{2} \mu_{s i}\left(P_{p m, r} P_{q n} P_{m k} P_{n l} P_{q r}+P_{p m} P_{q n, r} P_{m l} P_{n k} P_{q r}\right. \\
& \left.+P_{p n, r} P_{q m} P_{m k} P_{n l} P_{q r}+P_{p n} P_{q m, r} P_{m l} P_{n k} P_{q r}\right)
\end{aligned} \tag{A-4}
$$

In addition, by using the connections
$$
\mathbf{P}^{2}=\mathbf{P} \quad \text { and } \quad \mathbf{P n}=\mathbf{0}, \tag{A-5}
$$
and by accounting the expression (2), the expression (A-4) is now given by
$$
\begin{aligned}
a_{p k l}^{(i)}= & -\left(\kappa_{s i}-\mu_{s i}\right) P_{p q} P_{k l} n_{q, r} n_{r} \\
& -\left(\kappa_{s i}-\mu_{s i}\right)\left[\frac{1}{2} P_{p r} P_{m l} n_{m, r} n_{k}+\frac{1}{2} P_{p r} P_{n k} n_{n, r} n_{l}\right] \\
& -\left(\kappa_{s i}-\mu_{s i}\right)\left[\frac{1}{2} P_{m k} P_{p r} n_{m, r} n_{l}+\frac{1}{2} P_{p r} P_{n l} n_{n, r} n_{k}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{m k} P_{l r} n_{m, r} n_{p}+P_{n k} P_{l r} n_{n, r} n_{p}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{k r} P_{n l} n_{n, r} n_{p}+P_{k r} P_{m l} n_{m, r} n_{p}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{p m} P_{l r} n_{m, r} n_{k}+P_{p k} P_{n r} n_{n, r} n_{l}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{p m} P_{k r} n_{m, r} n_{l}+P_{p l} P_{n r} n_{n, r} n_{k}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{p l} P_{m r} n_{m, r} n_{k}+P_{p n} P_{k r} n_{n, r} n_{l}\right] \\
& -\frac{\mu_{s i}}{2}\left[P_{p k} P_{m r} n_{m, r} n_{l}+P_{p n} P_{l r} n_{n, r} n_{k}\right]
\end{aligned} \tag{A-6}
$$

Finally, by using (A-5), the expressions (31) and (41) can be rewritten as
$$
b_{p k l r}^{(i)}=\left(\kappa_{s i}-\mu_{s i}\right) P_{p r} P_{k l}+\mu_{s i}\left[P_{p k} P_{l r}+P_{p l} P_{k r}\right] \tag{A-7}
$$

$$
\begin{aligned}
y_{p s k l}^{(i)}= & \frac{\left(\kappa_{s i}-\mu_{s i}\right)}{2 h}\left(\overline{m}_{p} x_{s}+\underline{m}_{p} x_{s}+\overline{m}_{s} x_{p}+\underline{m}_{s} x_{p}\right) P_{k l}+\frac{\mu_{s i}}{2 h}\left[\left(\overline{m}_{l} x_{s}\right.\right. \\
& \left.+\underline{m}_{l} x_{s}\right) P_{p k}+\left(\overline{m}_{k} x_{s}+\underline{m}_{k} x_{s}\right) P_{p l}+\left(\overline{m}_{l} x_{p}+\underline{m}_{l} x_{p}\right) P_{s k} \\
& \left.+\left(\overline{m}_{k} x_{p}+\underline{m}_{k} x_{p}\right) P_{s l}\right].
\end{aligned} \tag{A-8}
$$

### B. Resolution of the system of linear equation (75)

The system of linear equation (75) can be decomposed into 2 independent sub-systems of linear equations corresponding to two cases of in-plane and anti-plane loading as follows
$$
\left(\begin{array}{lll}
H_{11}^{(\alpha \beta)} & H_{12}^{(\alpha \beta)} & H_{16}^{(\alpha \beta)} \\
H_{21}^{(\alpha \beta)} & H_{22}^{(\alpha \beta)} & H_{26}^{(\alpha \beta)} \\
H_{61}^{(\alpha \beta)} & H_{62}^{(\alpha \beta)} & H_{66}^{(\alpha \beta)}
\end{array}\right)\left(\begin{array}{l}
\widehat{\varepsilon}_{1}\left(\boldsymbol{\xi}^{(\beta)}\right) \\
\widehat{\varepsilon}_{2}\left(\boldsymbol{\xi}^{(\beta)}\right) \\
\widehat{\varepsilon}_{6}\left(\boldsymbol{\xi}^{(\beta)}\right)
\end{array}\right)=\left(\begin{array}{l}
\widehat{E}_{1}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right) \\
\widehat{E}_{2}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right) \\
\widehat{E}_{6}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right)
\end{array}\right),
$$

$$
\left(\begin{array}{ll}
T_{44}^{(\alpha \beta)} & T_{45}^{(\alpha \beta)} \\
T_{54}^{(\alpha \beta)} & T_{55}^{(\alpha \beta)}
\end{array}\right)\left(\begin{array}{l}
\widehat{\varepsilon}_{4}\left(\boldsymbol{\xi}^{(\beta)}\right) \\
\widehat{\varepsilon}_{5}\left(\boldsymbol{\xi}^{(\beta)}\right)
\end{array}\right)=\left(\begin{array}{l}
\widehat{E}_{4}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right) \\
\widehat{E}_{5}^{0}\left(\boldsymbol{\xi}^{(\alpha)}\right)
\end{array}\right)
$$
where
$$
\widehat{\varepsilon}_{\tilde{l}}\left(\boldsymbol{\xi}^{(\beta)}\right)=\left[\begin{array}{c}
\widehat{\varepsilon}_{\tilde{l}}\left(\boldsymbol{\xi}^{(1)}\right) \\
\widehat{\varepsilon}_{\tilde{l}}\left(\boldsymbol{\xi}^{(2)}\right) \\
\vdots \\
\widehat{\varepsilon}_{\tilde{l}}\left(\boldsymbol{\xi}^{\left(4 N_{k}^{2}\right)}\right)
\end{array}\right] ; \quad \widehat{E}_{\tilde{t}}^{0}\left(\boldsymbol{\xi}^{(\beta)}\right)=\left[\begin{array}{c}
\widehat{E}_{\tilde{t}}^{0}\left(\boldsymbol{\xi}^{(1)}\right) \\
\widehat{E}_{\tilde{t}}^{0}\left(\boldsymbol{\xi}^{(2)}\right) \\
\vdots \\
\widehat{E}_{\tilde{t}}^{0}\left(\boldsymbol{\xi}^{\left(4 N_{k}^{2}\right)}\right)
\end{array}\right]
$$
with $\tilde{l}, \tilde{t}=1,2,4,5,6$,

$$
H_{\tilde{t} \tilde{l}}^{(\alpha \beta)}=\left[\begin{array}{cccc}
H_{\tilde{t} \tilde{l}}^{(11)} & H_{\tilde{t} \tilde{l}}^{(12)} & \cdots & H_{\tilde{t} \tilde{l}}^{\left(14 N_{k}^{2}\right)} \\
H_{\tilde{t} \tilde{l}}^{(21)} & H_{\tilde{t} \tilde{l}}^{(22)} & \cdots & H_{\tilde{t} \tilde{l}}^{\left(24 N_{k}^{2}\right)} \\
\vdots & \vdots & \ddots & \vdots \\
H_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 1\right)} & H_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 2\right)} & \cdots & H_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 4 N_{k}^{2}\right)}
\end{array}\right]
$$
with $\tilde{l}, \tilde{t}=1,2,6$,

$$
T_{\tilde{t} \tilde{l}}^{(\alpha \beta)}=\left[\begin{array}{cccc}
T_{\tilde{t} \tilde{l}}^{(11)} & T_{\tilde{t} \tilde{l}}^{(12)} & \cdots & T_{\tilde{t} \tilde{l}}^{\left(14 N_{k}^{2}\right)} \\
T_{\tilde{t} \tilde{l}}^{(21)} & T_{\tilde{t} \tilde{l}}^{(22)} & \cdots & T_{\tilde{t} \tilde{l}}^{\left(24 N_{k}^{2}\right)} \\
\vdots & \vdots & \ddots & \vdots \\
T_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 1\right)} & T_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 2\right)} & \cdots & T_{\tilde{t} \tilde{l}}^{\left(4 N_{k}^{2} 4 N_{k}^{2}\right)}
\end{array}\right]
$$
with $\tilde{l}, \tilde{t}=4,5$.

Next, the expressions for the components $H_{\tilde{t} \tilde{l}}^{(\alpha \beta)}$ and $T_{\tilde{t} \tilde{l}}^{(\alpha \beta)}$ can be detailed in the following forms:

$$
\begin{aligned}
H_{\bar{l} \bar{t}}^{(\alpha \beta)}= & \delta^{(\alpha \beta)}+\sum_{\gamma=1,2,6}\left\{\widehat{\Gamma}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N}\left(L_{\gamma \bar{t}}^{(i)}-L_{\gamma \bar{t}}^{(0)}\right) \widehat{\chi}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right)\right\} \\
& +\sum_{\gamma=1,2,6}\left\{\widehat{\Gamma}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right)\left(L_{\gamma \bar{t}}^{(0)}-\bar{L}_{\gamma \bar{t}}\right) \delta^{(\alpha \beta)}\right\} \\
& -\frac{1}{|\mathcal{U}|} \sum_{\gamma=1,2}\left\{\widehat{\Lambda}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N} \widehat{A}_{\gamma \bar{t}}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right)\right\} \\
& -\frac{1}{|\mathcal{U}|} \sum_{\gamma=1,2 ; \eta=1,2}\left\{\widehat{\Lambda}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N} \widehat{B}_{\gamma \bar{t} \eta}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right) \iota \xi_{\eta}^{(\beta)}\right\}.
\end{aligned}
$$

$$
\begin{aligned}
T_{\bar{l} \bar{t}}^{(\alpha \beta)}= & \delta^{(\alpha \beta)}+\sum_{\gamma=4,5}\left\{\widehat{\Gamma}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N}\left(L_{\gamma \bar{t}}^{(i)}-L_{\gamma \bar{t}}^{(0)}\right) \widehat{\chi}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right)\right\} \\
& +\sum_{\gamma=4,5}\left\{\widehat{\Gamma}_{\bar{l} \gamma}\left(\xi^{(\alpha)}\right)\left(L_{\gamma \bar{t}}^{(0)}-\bar{L}_{\gamma \bar{t}}\right) \delta^{(\alpha \beta)}\right\} \\
& -\frac{1}{|\mathcal{U}|} \widehat{\Lambda}_{\bar{l} 3}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N} \widehat{A}_{3 \bar{t}}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right) \\
& -\frac{1}{|\mathcal{U}|} \sum_{\eta=1,2}\left\{\widehat{\Lambda}_{\bar{l} 3}\left(\xi^{(\alpha)}\right) \sum_{i=1}^{N} \widehat{B}_{3 \bar{t} \eta}^{(i)}\left(\xi^{(\alpha)}-\xi^{(\beta)}\right) \iota \xi_{\eta}^{(\beta)}\right\}.
\end{aligned}
$$

## References

[1] S. Iijima, Helical microtubules of graphitic carbon, Nature 354 (1991) 56-58.

[2] R.E. Miller, V.B. Shenoy, Size-dependent elastic properties of nanosized structural elements, Nanotechnology 11 (2000) 139-147.

[3] P. Sharma, A. Dasgupta, Average elastic fields and scale-dependent overall properties of heterogeneous micropolar materials containing spherical and cylindrical inhomogeneities, Phys. Rev. B 66 (2002), 224110-1-224110-10.

[4] R. Dingreville, J. Qu, M. Cherkaoui, Surface free energy and its effect on the elastic behavior of nano-sized particles, wires and films, J. Mech. Phys. Solids 8 (2005) 1827-1854.

[5] H.L. Duan, J. Wang, Z.P. Huang, B.L. Karihaloo, Eshelby formalism for nanocomposites, Proc. R. Soc. A 461 (2005) 3335-3353.

[6] H.L. Duan, J. Wang, Z.P. Huang, B.L. Karihaloo, Size-dependent effective elastic constants of solids containing nano-inhomogeneities with interface stress, J. Mech. Phys. Solids 53 (2005) 1574-1596.

[7] H.L. Duan, B.L. Karihaloo, Thermo-elastic properties of heterogeneous materials with imperfect interfaces: generalized Levin's formula and Hill's connections, J. Mech. Phys. Solids 55 (2007) 1036-1052.

[8] T. Chen, G.J. Dvorak, Fibrous nanocomposites with interface stress: Hill's and Levin's connections for effective moduli, Appl. Phys. Lett. 88 (2006) 211912.

[9] T. Chen, G.J. Dvorak, C.C. Yu, Size-dependent elastic properties of unidirectional nano-composites with interface stresses, Acta Mech. 118 (2007) 39-54.

[10] T. Chen, G.J. Dvorak, C.C. Yu, Solids containing spherical nano-inclusions with interface stresses: effective properties and thermal-mechanical connections, Int. J. Solids Struct. 44 (2007) 941-955.

[11] H. Le Quang, Q.C. He, Size-dependent effective thermoelastic properties of nanocomposites with spherically anisotropic phases, J. Mech. Phys. Solids 55 (2007) 1889-1921.

[12] H. Le Quang, Q.C. He, Variational principles and bounds for elastic inhomogeneous materials with coherent imperfect interfaces, Mech. Mater. 40 (2008) 865-884.

[13] S. Cuenot, C. Fretigny, S. Demoustier-Champagne, B. Nysten, Surface tension effect on the mechanical properties of nanomaterials measured by atomic force microscopy, Phys. Rev. B 69 (2004) 165410-165413.

[14] G.Y. Jing, H.L. Duan, X.M. Sun, Z.S. Zhang, J. Xu, Y.D. Li, J. Wang, D.P. Yu, Surface effects on elastic properties of silver nanowires: contact atomic-force microscopy, Phys. Rev. B 73 (2006) 235409.

[15] C.Q. Chen, Y. Shi, Y.S. Zhang, J. Zhu, Y.J. Yan, Size dependence of Youngs modulus in ZnO nanowires, Phys. Rev. Lett. 96 (2006) 075505.

[16] K.R. Pirota, E.L. Silva, D. Zanchet, D. Navas, M. Vazquez, M. Hernandez-Velez, M. Knobel, Size effect and surface tension measurements in Ni and Co nanowires, Phys. Rev. B 76 (2007) 233410.

[17] E.P.S. Tan, Y. Zhu, T. Yu, L. Dai, C.H. Sow, V.B.C. Tan, C.T. Lim, Crystallinity and surface effects on Young's modulus of CuO nanowires, Phys. Lett. 90 (2007) 163112.

[18] A. Chatterjee, B.L. Deopura, Carbon nanotubes and nanofibre: an overview, Fibers Polym. 3 (2002) 134-139.

[19] S. Sundararajan, B. Bhushan, T. Namazu, Y. Isono, Mechanical property measurements of nanoscale structures using an atomic force microscope, Ultramicroscopy 91 (2002) 111-118.

[20] E.P.S. Tan, C.T. Lim, Mechanical characterization of nanofibers-a review, Comp. Sci. Tech. 66 (2006) 1102-1111.

[21] J. Sandler, A.H. Windle, P. Werner, V. Altstadt, M. van Es, M.S.P. Shaffer, Carbon-nanofibre-reinforced poly(either ether ether ketone) fibres, J. Mater. Sci. 38 (2003) 2135-2141.

[22] R.Shuttleworth, The surface tension of solid, Proc. Phys. Soc. A63 (1950) 444-457.

[23] M.E. Gurtin, M. Murdoch, A continuum theory of elastic material surfaces, Arch. Ration. Mech. Anal. 57 (1975) 291-323 and 1975;59:389-390.

[24] J.W. Cahn, Surface stress and the chemical equilibrium of small crystals-I. The case of the isotropic surface, Acta Metall. 28 (1980) 1333-1338.

[25] E. Sanchez-Palencia, Comportement limite d'un problème de transmission à travers une plaque faiblement conductrice, C. R. Acad. Sci. Paris Ser. A270 (1970) 1026-1028.

[26] H. Pham Huy, E. Sanchez-Palencia, Phénomènes de transmission à travers des couches minces de conductivité élevée, J. Math. Anal. Appl. 47 (1974) 284-309.

[27] A. Klarbring, Derivation of a model of adhesively bonded joints by the asymptotic expansion method, Int. J. Eng. Sci. 29 (1991) 493-512.

[28] T. Miloh, Y. Benveniste, On the effective conductivity of composites with ellipsoidal inhomogeneities and highly conducting interfaces, Proc. R. Soc. Lond A 455 (1999) 2687-2706.

[29] Z. Hashin, Thin interphase/imperfect interface in conduction, J. Appl. Phys. 89 (2001) 2261-2267.

[30] Y. Benveniste, A general interface model for a three-dimensional curved thin anisotropic interphase between two anisotropic media, J. Mech. Phys. Solids 6 (2006) 4563-4570.

[31] S.T. Gu, Q.C. He, Interfacial discontinuity relations for coupled multifield phenomena and their application to the modeling of thin interphases as imperfect interfaces, J. Mech. Phys. Solids 59 (2011) 1413-1426.

[32] H. Moulinec, P. Suquet, A fast numerical method for computing the linear and nonlinear mechanical properties of composites, C. R. Acad. Sci. II 318 (1994) 1417-1423.

[33] J. Michel, H. Moulinec, P. Suquet, Effective properties of composite materials with periodic microstructure: a computational approach, Comput. Methods Appl. Mech. Eng. 172 (1999) 109-143.

[34] H. Le Quang, Q.C. He, Estimation of the effective thermoelastic moduli of fibrous nanocomposites with cylindrically anisotropic phases, Arch. Appl. Mech. 79 (2009) 225-248.

[35] J. Yvonnet, H. Le Quang, Q.C. He, An XFEM/level set approach to modelling surface/interface effects and to computing the size-dependent effective properties of nanocomposites, Comput. Mech. 42 (2008) 119-131.

[36] R. Hill, Discontinuity relations in mechanics of solids, in: I.N. Sneddon, R. Hill (Eds.), Progress in Solid Mechanics, vol. 2, North-Holland, Amsterdam, 1961, pp. 247-276.

[37] Q.C. He, A. Curnier, A more fundamental approach to damaged elastic stressstrain relations, Int. J. Solids Struct. 32 (1995) 1433-1457.

[38] Y.Z. Povstenko, Theoretical investigation of phenomena caused by heterogeneous surface tension in solids, J. Mech. Phys. Solids 41 (1993) 1499-1514.

[39] T. Chen, M.S. Chiu, C.N. Weng, Derivation of the generalized Young-Laplace equation of curved interfaces in nanoscaled solids, J. Appl. Phys. 100 (2006) 074308.

[40] R. Hill, Theory of mechanical properties of fibre-strengthened materials: I. Elastic behaviour, J. Mech. Phys. Solids 12 (1964) 199-212.

[41] H.L. Duan, J. Wang, B.L. Karihaloo, Z.P. Huang, Nanoporous materials can be made stiffer than non-porous counterparts by surface modification, Acta Mater. 54 (2006) 2983-2990.