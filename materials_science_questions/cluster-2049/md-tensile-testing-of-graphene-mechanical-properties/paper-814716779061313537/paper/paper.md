# Large-displacement strain theory and its application to graphene

J. A. Crosse*

Department of Electrical and Computer Engineering, National University of Singapore, 4 Engineering Drive 3, Singapore 117583

(Received 1 April 2014; revised manuscript received 28 May 2014; published 2 July 2014)

Under the application of a force a material will deform and, hence, the crystal lattice will experience strain. This induced strain will alter the electronic properties of the material. In particular, strain in graphene generates an artificial vector potential that, if spatially varying, admits a pseudomagnetic field. Current theories for spatially varying strain use linear or finite strain theory, whose derivation is based on small displacements of infinitesimal length vectors. Here we apply a differential geometry method to derive a strain theory for large displacements of finite length vectors. This method gives a finite displacement term whose contribution is comparable to that of the linear strain term. Furthermore, we show that a "domain-wall"-like pseudomagnetic-field profile can be generated when a wide graphene ribbon is subjected to a pair of opposing point forces (point stretch). The resulting field is a function of the new finite displacement term only and displays a maximum strength of over three times that which is predicted by the linear strain theory. These results extend the current theories of strain, which are based on the transformation of infinitesimal length vectors, to finite length vectors, thus providing an accurate description of pseudomagnetic-field structures in strained materials.

DOI: 10.1103/PhysRevB.90.045201

PACS number(s): 73.22.Pr, 77.80.bn, 81.05.ue, 75.90.+w

## I. INTRODUCTION

Extensive studies of graphene have shown that it displays a wide range of remarkable electronic properties [1-3], and there has been much speculation on its role in future electro- and electro-optical devices. However, although unique, the properties of graphene are not ideal. For example, the gapless band structure and resulting minimum conductivity leads to low on-off ratios, a major obstacle in the development of usable graphene transistors [4]. Thus, in order to create efficient devices, one needs to alter graphene's intrinsic electronic properties. A number of approaches to this "band-structure engineering" have been investigated, including geometric confinement [5,6], doping [7,8], and substrate interaction effects [9,10], to name but a few.

Another intriguing possibility is the use of strain. The band structure of a material is directly related to its crystal lattice. By applying a force, one can deform a material's crystal lattice and, hence, change its electronic properties. A number of studies have already proposed gap generation [11], modification of graphene's optical properties [12,13], and even the appearance of superconductivity [14] under strain. Another feature of strained graphene is the appearance of artificial vector potentials and pseudomagnetic fields [15-22] with predicted field strengths ranging from tens [18] to thousands of Tesla [19-22] for both in-plane and out-of-plane strains. The ability to generate such pseudomagnetic fields would remove the need for cumbersome external field generation and could pave the way for a generation of highly compact magnetoelectronic and spintronic devices. In light of this, there have been a number of previous studies using a variety of methods; rotation-free linear strain theory [11,15], rotational finite strain theory [16], or, more recently, rotational finite strain theory up to second order in the strain tensor [19] as well as first-principles atomistic simulations [20,21]. However, both the infinitesimal (linear) and finite strain tensors are based on the small displacements of infinitesimal length vectors [23]. It would be advantageous to generalize this to large displacements of finite length vectors.

Here, we present a theory that uses a differential geometry method from which one is able calculate the exact, strain-induced displacements for finite length vectors, thus going beyond the finite strain theory, which is based on small displacements of infinitesimal length vectors. This method gives a new finite displacement term that is found to be of comparable magnitude to the rotation and linear strain contributions. As an example, we compute the pseudomagnetic field generated in graphene by a "point stretch," where a pair of opposing point forces act laterally across the center of a wide graphene ribbon. The resulting field is found to be a function of the finite displacement term only, and it displays a "domain-wall"-like profile with a maximum field strength that is over three times that predicted by the linear strain theory alone.

## II. GENERAL THEORY OF DEFORMATIONS

In a strained material, the locations of the constituent atoms change from their equilibrium position, $R_i$, to $R_i' = R_i + u_i(\mathbf{R})$, where $u_i(\mathbf{R})$ is the displacement vector, which is, itself, a function of the equilibrium position of the atom (in the following, we will use index notation with implied summation over repeated indices). In general, for a given applied force, the displacements, $u_i(\mathbf{R})$, are not (a priori) known and, hence, one characterizes the deformation in terms of the strain tensor, $\varepsilon_{ij}$, which can be found from the stress tensor, $\sigma_{ij}$, using the generalized Hooke's law, $\varepsilon_{ij} = S_{ijkl}\sigma_{kl}$. (In principle, the displacements can be found from the elastic Green function, however formulating the equations of equilibrium for a material body usually involves some assumptions about the form of the strain tensor [23].) The rank-4 tensor $S_{ijkl}$ is the compliance tensor whose components are related to the mechanical properties of the material. Previous studies [11,15], which have considered rotation-free, linear displacements (symmetric, spatially constant strain

*alexcrosse@gmail.com

tensors), have found that the locations of the displaced atoms are given by $R_{i}'=(\delta_{ij}+\varepsilon_{ij})R_{j}$, where $\delta_{ij}$ is the Kronecker delta. Rotations are easily accounted for by the inclusion of the rotation tensor [16,19], $\omega_{ij}$, via $R_{i}'=(\delta_{ij}+\varepsilon_{ij}+\omega_{ij})R_{j}$. The rotation tensor is antisymmetric, trace-free, and related to the strain tensor by $\nabla \times \boldsymbol{\omega}=-\nabla \times \boldsymbol{\varepsilon}$.

The inclusion of large, spatially varying displacements is slightly more involved. The infinitesimal strain tensor gives the local change of an infinitesimal length over small displacements. For the change of finite lengths over a large displacement, one needs to "integrate" the infinitesimal strain tensor over the deformation. This can be done using methods from differential geometry to account for the change in the strain tensor as the deformation progresses. The change in the element of length of an infinitesimal vector, $dR_{i}$, under strain is given by [23]

$$
dl^{2}=g_{ij}dR_{i}dR_{j}=(\delta_{ij}+2\varepsilon_{ij})dR_{i}dR_{j}. \tag{1}
$$

Thus, the strain tensor acts as a metric with the large, spatially varying displacements accounted for by the "non-Euclidean" nature of the strain tensor. Note that, since the metric is, by definition, an infinitesimal object, one only needs to consider the unique infinitesimal strain tensor and not one of the many finite strain tensors (e.g., Green-Lagrange, Almansi, etc.). For vanishing strain, the metric is Euclidean, $g_{ij}=\delta_{ij}$, and hence the tangent spaces at different points on the manifold are identical. Thus, a vector, $\mathbf{R}_{u}$, defined in the tangent space at the origin and a vector, $\mathbf{R}_{u}'$, defined in the tangent space at a point $(x,y)$ are comparable, and the parallel transport of $\mathbf{R}_{u}$ from the origin to $(x,y)$ leaves it unchanged $(\mathbf{R}_{u}=\mathbf{R}_{u}')$. For nonvanishing strain, the "non-Euclidean" nature of the metric means tangent spaces at each point are different. Thus, a vector, $\mathbf{R}_{d}$, defined in the tangent space at the origin and a vector, $\mathbf{R}_{d}'$, in the tangent space at a point $(x,y)$ are not comparable. The parallel transport of $\mathbf{R}_{d}$ from the origin to the $(x,y)$ causes it to change by an amount proportional to the metric connections. Thus, in general, $\mathbf{R}_{d}\neq \mathbf{R}_{d}'$, with the difference between the two dependent on the form of the metric (which in this case is a function of the strain tensor). As the tangent space at the origin in the deformed material is isomorphic to Euclidean space and, hence, the undeformed material, we have $\mathbf{R}_{u}=\mathbf{R}_{d}$. Thus, the parallel transport of $\mathbf{R}_{u}$ from the origin to the point $(x,y)=(R_{u,x},R_{u,y})$ will give $\mathbf{R}_{d}'$ and hence the displacement due to the spatial variation of the strain tensor (see Fig. 1). To compute this, we employ the parallel transport equation, familiar from differential geometry,

$$
\frac{DR_{i}'}{D\lambda}=-\Gamma_{ijk}[\mathbf{R}(\lambda)]R_{j}(\lambda)\frac{dR_{k}(\lambda)}{d\lambda}, \tag{2}
$$

where $\lambda$ parametrizes the path over which the vector is parallel transported. Here, $\Gamma_{ijk}$ are the metric connections that can be expressed uniquely in terms of the Christoffel symbols of the first kind, which are given, in terms of the metric, by

$$
\Gamma_{ijk}=\frac{1}{2}\left(\frac{\partial g_{ij}}{\partial x_{k}}+\frac{\partial g_{ik}}{\partial x_{j}}-\frac{\partial g_{jk}}{\partial x_{i}}\right). \tag{3}
$$

We wish to transport the vector $R_{i}$ from the origin at $(0,0,0)$ along its length to $(R_{x},R_{y},R_{z})$. Thus, we use the parametrization $R_{i}(\lambda)=\lambda R_{i}=(\lambda R_{x},\lambda R_{y},\lambda R_{z})$, where $\lambda \in [0,1]$ and $dR_{i}/d\lambda=R_{i}$. Thus the spatially varying displacement is given by

$$
R_{i}'=-R_{j}R_{k}\int_{0}^{1}d\lambda\ \lambda\Gamma_{ijk}[\mathbf{R}(\lambda)]. \tag{4}
$$

![](./images/814716779061313537_1.jpg)

FIG. 1. Schematic diagram of parallel transport. The vector $\mathbf{R}_{u}$ in the undeformed material is unchanged when parallel transported along the solid line to $(x,y)$. The vector $\mathbf{R}_{d}$ in the deformed material is changed when parallel transported along the dotted line to $(x,y)$. This change is a direct result of the spatially varying displacement of the material and, hence, from this change the displacements can be found.

Essentially, we have integrated the infinitesimal strain tensor over the deformation and hence have found the displacement of finite length vectors. This goes beyond the usual finite strain theory, which, although second-order, is still based on the displacement of infinitesimal vectors. Note that, in the case of linear deformations (constant strain tensor), the Christoffel symbols, $\Gamma_{ijk}$, vanish. Thus, the finite displacement term also vanishes and one recovers the results of previous studies [11,15].

Finally, one finds that the change in the vector locations of atoms displaced by a general spatially varying strain is given by

$$
R_{i}'=(\delta_{ik}+\varepsilon_{ik}+\omega_{ik})R_{k}-\Sigma_{ijk}R_{j}R_{k}, \tag{5}
$$

where $\Sigma_{ijk}=\int_{0}^{1}d\lambda\ \lambda\Gamma_{ijk}[\mathbf{R}(\lambda)]$ is the finite displacement term. Hence from Eq. (5) one is able to find the displacement vectors, $u_{i}(\mathbf{R})$, for any point in the deformed material. One should note that this expression is only valid for elastic deformation.

### III. BOND DEFORMATION

The electronic properties of a material are determined (to first approximation) by the relative locations of neighboring atoms. Under strain, the atoms are displaced and hence these interatomic distances are changed. Using the expression for a general displacement in Eq. (5), the change in the relative

distance between two atoms at $\mathbf{R}_n$ and $\mathbf{R}_m$ is given by
$$
\begin{aligned}
R_{n, i}^{\prime}-R_{m, i}^{\prime}= & {\left[R_{n, i}+\varepsilon_{i k}\left(\mathbf{R}_{n}\right) R_{n, k}+\omega_{i k}\left(\mathbf{R}_{n}\right) R_{n, k}\right.} \\
& \left.-\Sigma_{i j k}\left(\mathbf{R}_{n}\right) R_{n, j} R_{n, k}\right]-\left[R_{m, i}+\varepsilon_{i k}\left(\mathbf{R}_{m}\right) R_{m, k}\right. \\
& \left.+\omega_{i k}\left(\mathbf{R}_{n}\right) R_{n, k}-\Sigma_{i j k}\left(\mathbf{R}_{m}\right) R_{m, j} R_{m, k}\right]. \quad(6)
\end{aligned}
$$

Defining the interatomic distance as $\mathbf{R}_{\alpha}=\mathbf{R}_{n}-\mathbf{R}_{m}$ and employing the symmetries of the Christoffel symbols, $\Gamma_{i j k}=$ $\Gamma_{i k j}$ (and hence $\Sigma_{i j k}=\Sigma_{i k j}$ ), one finds
$$
\begin{aligned}
R_{\alpha, i}^{\prime}= & R_{\alpha, i}+\varepsilon_{i k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right) R_{\alpha, k}+\omega_{i k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right) R_{\alpha, k} \\
& +\left[\varepsilon_{i k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right)-\varepsilon_{i k}\left(\mathbf{R}_{m}\right)\right] R_{m, k} \\
& +\left[\omega_{i k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right)-\omega_{i k}\left(\mathbf{R}_{m}\right)\right] R_{m, k} \\
& -\left[\Sigma_{i j k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right)-\Sigma_{i j k}\left(\mathbf{R}_{m}\right)\right] R_{m, j} R_{m, k} \\
& -2 \Sigma_{i j k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right) R_{\alpha, j} R_{m, k} \\
& -\Sigma_{i j k}\left(\mathbf{R}_{m}+\mathbf{R}_{\alpha}\right) R_{\alpha, j} R_{\alpha, k}.
\end{aligned}
$$

If the various strain contributions do not vary significantly on the scale of the bond length (which is required for Bloch theorem to hold locally), then $f(\mathbf{R}_{m}+\mathbf{R}_{\alpha}) \approx f(\mathbf{R}_{m})$. Furthermore, we can drop the last term in Eq. (7) as it is second-order in the bond length and hence its contribution to the band structure will be small. Thus one finds
$$
R_{\alpha, i}^{\prime}=R_{\alpha, i}+\Omega_{i k}\left(\mathbf{R}_{m}\right) R_{\alpha, k}, \quad(8)
$$
with
$$
\Omega_{i k}\left(\mathbf{R}_{m}\right)=\left\{\varepsilon_{i k}\left(\mathbf{R}_{m}\right)+\omega_{i k}\left(\mathbf{R}_{m}\right)-2 \Sigma_{i j k}\left(\mathbf{R}_{m}\right) R_{m, j}\right\}. \quad(9)
$$

The transformation $\Omega_{i k}(\mathbf{R}_{m})$ gives the displacement of the lattice vectors in the neighborhood of $\mathbf{R}_{m}$ and is a function of the global coordinate, $\mathbf{R}_{m}$, only.

## IV. BAND STRUCTURE

So far the discussion of strain has been general and can be applied to any material. Now we will consider graphene as an example. Graphene consists of two independent triangular sublattices (labeled $A$ and $B$ ). The unit cell is rhombic and contains two atoms, one from each sublattice, with nearest-neighbor hopping connecting the two sublattices (see Fig. 2).

![](./images/814716779061313537_2.jpg)

FIG. 2. The graphene lattice.

The length of the lattice vector is $a=2.46$ Å and the nearest neighbor vectors read
$$
\mathbf{R}_{A, 1}=\left(\begin{array}{c}
\frac{a}{\sqrt{3}} \\
0
\end{array}\right), \quad \mathbf{R}_{A, 2}=\left(\begin{array}{c}
-\frac{a}{2 \sqrt{3}} \\
\frac{a}{2}
\end{array}\right), \quad \mathbf{R}_{A, 3}=\left(\begin{array}{c}
-\frac{a}{2 \sqrt{3}} \\
-\frac{a}{2}
\end{array}\right),
$$

$$
\mathbf{R}_{B, 1}=\left(\begin{array}{c}
-\frac{a}{\sqrt{3}} \\
0
\end{array}\right), \quad \mathbf{R}_{B, 2}=\left(\begin{array}{c}
\frac{a}{2 \sqrt{3}} \\
\frac{a}{2}
\end{array}\right), \quad \mathbf{R}_{B, 3}=\left(\begin{array}{c}
\frac{a}{2 \sqrt{3}} \\
-\frac{a}{2}
\end{array}\right),
$$
each with length $d=a / \sqrt{3}=1.42$ Å.

The nearest-neighbor tight-binding Hamiltonian for each sublattice can be written as
$$
\hat{H}=\left\{\sum_{\alpha} t_{\alpha} e^{-i \mathbf{k} \cdot\left[\mathbf{R}_{\alpha}+\boldsymbol{\Omega}\left(\mathbf{R}_{m}\right) \cdot \mathbf{R}_{\alpha}\right]}\right\} \hat{a}_{\mathbf{k}}^{\dagger} \hat{b}_{\mathbf{k}}+\text { H.c. }, \quad(11)
$$
where the operators $\hat{a}_{\mathbf{k}}^{\dagger}$ and $\hat{b}_{\mathbf{k}}^{(\dagger)}$ create or annihilate electrons of momentum $\mathbf{k}$ from the $A$ and $B$ sublattices, respectively. The sum over $\alpha$ is the sum over all nearest-neighbor vectors, and $t_{\alpha}$ is the renormalized hopping amplitude. Much discussion has gone into the form of the hopping amplitude under strain. Here we use the parametrization [11] $t_{\alpha}=t_{0} \exp [-\beta(l / d-1)]$, where $l=\left|\mathbf{R}_{\alpha}+\boldsymbol{\Omega}\left(\mathbf{R}_{m}\right) \cdot \mathbf{R}_{\alpha}\right|$ is the nearest-neighbor distance under strain, $t_{0} \approx 2.8 \mathrm{eV}$ [1] is the unstrained hopping amplitude, and $\beta \approx 3$ is the hopping decay parameter [11]. Since the displacement of the atoms is small, we can expand the Hamiltonian in Eq. (11) to linear order in strain. One finds that the tight-binding Hamiltonian becomes $\hat{H}=\hat{H}_{0}+\hat{H}_{\varepsilon}$, where $\hat{H}_{0}$ is the Hamiltonian for the unstrained graphene sheet, and
$$
\hat{H}_{\varepsilon}=t_{0} \sum_{\alpha} e^{-i \mathbf{k} \cdot \mathbf{R}_{\alpha}}\left[\beta-\frac{\beta l}{d}-\mathbf{k} \cdot \boldsymbol{\Omega}\left(\mathbf{R}_{m}\right) \cdot \mathbf{R}_{\alpha}\right] \hat{a}_{\mathbf{k}}^{\dagger} \hat{b}_{\mathbf{k}}+\text { H.c. }
$$
is a strain-induced perturbation.

The usual expansion of the unstrained and the strain-induced perturbation Hamiltonians about the Dirac points at $\left[\mathbf{K}_{1, \pm}=(0, \pm 4 \pi / 3 a), \quad \mathbf{K}_{2, \pm}=( \pm 2 \pi / \sqrt{3} a, \pm\right.$ $2 \pi / 3 a), \mathbf{K}_{3, \pm}=( \pm 2 \pi / \sqrt{3} a, \mp 2 \pi / 3 a)]$ leads to the usual linear band structure but with the replacement $\mathbf{k} \rightarrow \mathbf{k}-\mathbf{A}$, with the artificial vector potential, $\mathbf{A}$, at each Dirac point reading
$$
\mathbf{A}_{1, \pm}\left(\mathbf{R}_{m}\right)= \pm \frac{4 \pi}{3 a}\left(\begin{array}{c}
\Omega_{y x} \\
\Omega_{y y}
\end{array}\right) \pm \mathbf{A}_{\beta}\left(\mathbf{R}_{m}\right), \quad(13 \mathrm{a})
$$

$$
\mathbf{A}_{2, \pm}\left(\mathbf{R}_{m}\right)= \pm \frac{2 \pi}{3 a}\left(\begin{array}{c}
-\sqrt{3} \Omega_{x x}-\Omega_{y x} \\
-\sqrt{3} \Omega_{x y}-\Omega_{y y}
\end{array}\right) \pm \mathbf{A}_{\beta}\left(\mathbf{R}_{m}\right), \quad(13 \mathrm{~b})
$$

$$
\mathbf{A}_{3, \pm}\left(\mathbf{R}_{m}\right)= \pm \frac{2 \pi}{3 a}\left(\begin{array}{c}
\sqrt{3} \Omega_{x x}-\Omega_{y x} \\
\sqrt{3} \Omega_{x y}-\Omega_{y y}
\end{array}\right) \pm \mathbf{A}_{\beta}\left(\mathbf{R}_{m}\right), \quad(13 \mathrm{c})
$$
where
$$
\mathbf{A}_{\beta}\left(\mathbf{R}_{m}\right)=\frac{\sqrt{3} \beta}{2 a}\left(\begin{array}{c}
\Omega_{x y}+\Omega_{y x} \\
\Omega_{x x}-\Omega_{y y}
\end{array}\right). \quad(14)
$$

The first term in the potential originates from the distortion of the lattice and the second from the renormalization of the hopping amplitude. Note these are slightly different from the expressions found in previous work [15,18–20] since in those studies the displacement is described solely by the strain tensor, which is symmetric, or by the strain and rotation tensors, the latter of which is antisymmetric. Thus, some simplification occurs. Here we have included the effect of the finite displacement term, which is asymmetric, and therefore we have arrived at a more general expression. As the deformation, $\boldsymbol{\Omega}$, and hence the expressions for the artificial vector potentials are spatially varying, they admit a curl and, therefore, describe a pseudomagnetic field, which near the $i$th Dirac point is given by $\mathbf{B}_{i,\pm} = \nabla \times \mathbf{A}_{i,\pm}$.

## V. POINT STRETCH OF A GRAPHENE RIBBON
Here, we consider the point stretch of a wide graphene ribbon orientated such that the armchair edge is parallel to the $x$ axis and the zigzag edge is parallel to the $y$ axis. The ribbon is considered to be wide enough such that confinement effects are negligible and, hence, the band structure can be treated as that of bulk graphene. The ribbon is subject to a pair of equal and opposite point forces that act at opposing locations on the ribbon's edge. We define a coordinate system such that the origin is located at the center of the ribbon on the neutral axis and the forces act along the $y$ axis at $x = 0$ [see Fig. 3(a)].

One can show (see Appendix) that the strain tensor for such a geometry is given by
$$
\boldsymbol{\varepsilon}(x,y) = \frac{F_0}{E L_z} \begin{pmatrix}
-\frac{\nu}{(|x|+1)} & -\frac{\text{sgn}[x]|y|}{2(|x|+1)^2} \\
-\frac{\text{sgn}[x]|y|}{2(|x|+1)^2} & \frac{1}{(|x|+1)}
\end{pmatrix}, \tag{15}
$$
where $F_0$ is the applied force, $L_z = 3.5$ Å is the thickness (in the $z$ direction) of the graphene ribbon [24], and $E \approx 340$ N m$^{-1}$ ($\approx 1$ TPa acting over the graphene ribbon thickness, $L_z$), and $\nu = 0.165$ are the Young's modulus [24] and the Poisson ratio [25] of graphene, respectively. The coordinates $x \to x/L_z$ and $y \to x/L_z$ are dimensionless distances scaled by the thickness of the graphene ribbon. Note that the strain tensor for other orientation can easily be found via a rotational transformation. It is easy to show that the strain tensor satisfies the compatibility equation
$$
\frac{\partial^2 \varepsilon_{xx}}{\partial y^2} + \frac{\partial^2 \varepsilon_{yy}}{\partial x^2} - 2 \frac{\partial^2 \varepsilon_{xy}}{\partial x \partial y} = 0, \tag{16}
$$
and hence describes a unique, smoothly varying deformation. Furthermore, from $\nabla \times \boldsymbol{\omega} = -\nabla \times \boldsymbol{\varepsilon}$, one can show that the rotation tensor reads
$$
\boldsymbol{\omega}(x,y) = \frac{F_0}{E L_z} \begin{pmatrix}
0 & \frac{\text{sgn}[x]|y|}{2(|x|+1)^2} \\
-\frac{\text{sgn}[x]|y|}{2(|x|+1)^2} & 0
\end{pmatrix}. \tag{17}
$$

Using the form of the metric tensor given in Eq. (1), one finds that the Christoffel symbols are given by
$$
\Gamma_{xxx} = \frac{F_0}{E L_z} \frac{\nu}{(1 + |x|)^2}, \tag{18a}
$$
$$
\Gamma_{yxx} = \frac{F_0}{E L_z} \frac{2 \text{sgn}[x] |y|}{(1 + |x|)^3}, \tag{18b}
$$
$$
\Gamma_{yxy} = \Gamma_{yyx} = -\frac{F_0}{E L_z} \frac{1}{(1 + |x|)^2}, \tag{18c}
$$
$$
\Gamma_{xyy} = \Gamma_{xxy} = \Gamma_{xyx} = \Gamma_{yyy} = 0, \tag{18d}
$$
from which the components of $\boldsymbol{\Sigma} \cdot \mathbf{R}$ are calculated to be
$$
\begin{aligned}
& \boldsymbol{\Sigma} \cdot \mathbf{R}(x,y) \\
& = \frac{F_0}{E L_z} \begin{pmatrix}
\nu\left[\frac{\ln[1+|x|]}{|x|} - \frac{1}{1+|x|}\right] & 0 \\
\frac{|y|}{x}\left[\frac{\ln[1+|x|]}{|x|} - \frac{2|x|+1}{(1+|x|)^2}\right] & -\left[\frac{\ln[1+|x|]}{|x|} - \frac{1}{1+|x|}\right]
\end{pmatrix}.
\end{aligned}
\tag{19}
$$

Considering the band structure close to the $\mathbf{K}_{1,\pm} = (0, \pm 4\pi/3a)$ Dirac points and using the definition of the transformation $\Omega$ from Eq. (9), one finds that the artificial vector potential that results from the strain is given by
$$
\begin{aligned}
A_{1,\pm,x} = \mp & \frac{F_0}{E L_z} \frac{8\pi + 3\sqrt{3}\beta}{6a} \frac{|y|}{x} \\
& \times \left[ \frac{2 \ln [1 + |x|]}{|x|} - \frac{(2 + 3|x|)}{(1 + |x|)^2} \right], \tag{20a}
\end{aligned}
$$
$$
\begin{aligned}
A_{1,\pm,y} = \pm & \frac{F_0}{E L_z} \frac{8\pi - 3\sqrt{3}\beta(1 + \nu)}{6a} \\
& \times \left[ \frac{2 \ln [1 + |x|]}{|x|} - \frac{1}{(1 + |x|)} \right], \tag{20b}
\end{aligned}
$$
which leads to a pseudomagnetic field of
$$
\begin{aligned}
B_{\mathbf{K}_{1,\pm},z} = \mp & \frac{\hbar}{e} \frac{F_0}{E L_z^2} \frac{\sqrt{3}\beta}{2a} \frac{(2 + \nu)}{x} \\
& \times \left[ \frac{2 \ln [1 + |x|]}{|x|} - \frac{(2 + 3|x|)}{(1 + |x|)^2} \right]. \tag{21}
\end{aligned}
$$

A similar calculation shows that the expressions for the pseudomagnetic fields at $\mathbf{K}_{2,\pm}$ and $\mathbf{K}_{3,\pm}$ are identical. Note that the field is constant in the $y$ direction and hence does not change over the height of the ribbon. Considering the form of the pseudomagnetic field given in Eq. (21), one can see that it is proportional to $\beta$ and hence is a result of the renormalization of the hopping amplitude only. In this particular case, the distortion of the lattice does not contribute. This is consistent with previous studies [16,19]. Furthermore, comparing Eq. (21) with Eq. (19), one can see that the pseudomagnetic field is solely the result of the finite displacement term, $\boldsymbol{\Sigma} \cdot \mathbf{R}$.

Figure 3(b) shows the local band structure near the Dirac point for the $\mathbf{K}_{1,\pm}$ valleys at various points along the graphene ribbon. One can see that the Dirac cone is shifted compared to unstrained graphene, $\mathbf{k} \to \mathbf{k} - \mathbf{A}$, and hence an artificial vector potential has been induced by the strain. The shift (artificial vector potential) is largest close to the origin, where the point

![](./images/814716779061313537_3.jpg)

FIG. 3. (Color online) (a) Schematic diagram of the applied force. A pair of equal and opposing point forces, $F_0$, act in the $\pm y$ directions at $x=0$. (b) The local shift of the Dirac point for the positive (top) and negative (bottom) valleys for $y=0$ at (A) the origin, (B) $x=10$ Å, and (C) $x=40$ Å, respectively, for an applied force of $F_0=0.35$ nN. The red solid line shows the Dirac cone for the strained graphene lattice when the linear strain, rotation, and finite displacement contributions are taken into account. The blue dashed line shows the Dirac cone for the strained graphene lattice when only the linear strain term is taken into account [15]. The gray dotted line shows the Dirac cone for the unstrained graphene lattice. The arrows mark the artificial vector potential, $\mathbf{A}_{\mathbf{K}_{1,\pm}}$ as calculated by Eq. (13a) (for the red curve) or the expressions found in previous studies [15] (for the blue curve).

forces act, and it falls off as one moves away from the origin. At large distances, the location of the Dirac cone approaches that of unstrained graphene. This spatial variation of the artificial vector potential gives rise to the pseudomagnetic field. Note that, by taking the finite displacement terms into account, one sees that, at the origin, the artificial vector potential is almost double that which is predicted by the linear strain theory alone.

Figure 4 shows the pseudomagnetic field for various applied forces. One sees a "domain-wall" structure with a sudden change in the orientation of the field at the origin. Increasing the applied force increases the maximum field, increasing the height of the domain wall. By taking the rotation and finite displacement terms into account, one sees that the strength of the field is over three times that which is predicted by the linear strain theory (0.1 nN gives a field of $\approx 5$ T compared to the $\approx 1.5$ T field given by linear strain theory [15]). Similarly, we see up to a factor of 2 increase in the pseudomagnetic-field strength compared to studies that used finite strain theory and included the rotation tensor (strains of $\approx 12\%$ lead to fields of $\approx 1500$ T, whereas previous studies find fields of 800–1400 T depending on the strain profile [19]). Finally, pseudomagnetic-field profiles have been predicted for strain induced via nanostructured substrates [20–22], however this study shows that it is possible to create similar field profiles with in-plane strains only.

In addition to the appearance of a pseudomagnetic field, some studies have predicted the appearance of pseudoscalar fields that are linearly proportional to the average change in the bond length [26–28]. The finite displacement term contributes to the change in bond length and, hence, changes the pseudoscalar potential. The change in bond length depends greatly on the strength and direction of the applied forces and the location of the bond in the material, however in the current study the change in bond length can be as large as a factor of 2.

Finally, it is worthwhile to compare the above analytical results with those obtained via atomistic simulations. Such first-principles simulations should not suffer from the ap- proximations imposed by linear strain theory. The current study has considered low strains of $\approx 0.25\%$ comparable to previous studies of linear strain theory [15]. However, the theory is valid for large strains as well with strains of $\approx 12\%$ leading to pseudomagnetic fields of $\approx 1500$ T. Out-of-plane deformations with similar magnitude strain fields have been studied previously using atomistic simulations [20,21], and the calculated pseudomagnetic field is of similar magnitude to those predicted by the current study.

![](./images/814716779061313537_4.jpg)

FIG. 4. (Color online) The pseudomagnetic field for the positive (top) and negative (bottom) valleys for different applied forces.

## VI. SUMMARY

We have developed a theory of strain-induced band-structure engineering that goes beyond the small displacement, infinitesimal vector transformations of linear and finite strain theory. By integrating the infinitesimal strain tensor over the deformation, and thereby finding the strain transformation of finite vectors under large displacements, we obtain a finite displacement term that makes a significant contribution to the strained band structure. Furthermore, we found that a point stretch of a wide graphene ribbon by a force on the order of 0.1 nN generates a "domain-wall"-like pseudomagnetic-field profile with field strength on the order of 5 T, over three times as much as predicted by the linear strain theory. This ability to generate and tailor complex pseudomagnetic-field structures allows for unprecedented control of the electrons in graphene and could pave the way for many novel magnetoelectronic and spintronic devices.

## ACKNOWLEDGMENTS

The author would like to thank P. Del Linz for useful discussions and A. Danner and the members of the Optical Device Research Group at the National University of Singapore for their hospitality. The author would also like to thank F. M. Peeters for bringing the latest developments in the field to his attention.

## APPENDIX: STRAIN TENSOR OF A POINT STRETCH

Here we derive the strain tensor for a material ribbon under a point stretch. The ribbon is considered to be unbounded in the $x$ direction but bounded in the $y$ direction. The ribbon is subject to a pair of equal and opposite point forces that act at opposing locations on the ribbon's edge. We define a coordinate system such that the origin is located at the center of the ribbon, on the neutral axis, and the forces act along the $y$ axis at $x=0$. The stress tensor can be computed by performing a force balance on an infinitesimal area element at a location $(x,y)$ relative to the origin (see Fig. 5). For a static element, both the tensile stresses and moments must vanish. In the following, we will consider the upper right quadrant $(+x,+y)$ of the coordinate system. The other three quadrants follow identically with an appropriate change of sign.

The $\sigma_{xx}$ component vanishes trivially as there is no component of the force acting in the $x$ direction. The $\sigma_{yy}$ component can be found from a moment balance (the tensile stress balance in the $y$ direction gives a trivial constraint)
$$
\begin{aligned}
F(x,y)x =& F(x+dx,y)[x+dx] \\
&+ L_z[F_{sx}(x,y+dy)-F_{sx}(x,y)], \quad \text{(A1)}
\end{aligned}
$$
which to first order gives
$$
x\frac{dF(x,y)}{dx}dx + F(x,y)dx + L_z\frac{dF_{sx}(x,y)}{dy}dy = 0, \quad \text{(A2)}
$$
where $F_{sx}(x,y)$ is the shear stress along the length, $dx$, and across the thickness (z direction), $L_z$, of the ribbon. This term appears because shear stress is able to transfer the moment laterally. The shear stress in the $x$ direction must equal the difference in tensile stress at $x$ and $x+dx$,
$$
\begin{aligned}
\frac{dF_{sx}(x,y)}{dy}dy = F(x+dx,y)-F(x,y) = \frac{dF(x,y)}{dx}dx.
\tag{A3}
\end{aligned}
$$

Substituting the definition in Eq. (A3) into Eq. (A2) leads to
$$
(x+L_z)\frac{dF(x,y)}{dx} + F(x,y) = 0, \quad \text{(A4)}
$$
which has the solution
$$
F(x,y) = \frac{c}{(x+L_z)}. \quad \text{(A5)}
$$

![](./images/814716779061313537_5.jpg)

FIG. 5. (a) Schematic diagram of the applied force. (b) Force balance of an area element $(dx,dy)$ at point $(x,y)$.

At $x=0$, the stress must be equal to the applied force acting over the thickness. Thus, $c=F_0$, where $F_0$ is the applied force at the ribbon edge.

The shear stress can be found from Eq. (A3),
$$
\begin{aligned}
\frac{d F_{s x}(x, y)}{d y} d y & =\frac{d F(x, y)}{d x} d x, \\
\frac{d F_{s x}(x, y)}{d y} & =\frac{d F(x, y)}{d x} \frac{d x}{d y},
\end{aligned}
\qquad (A6)
$$
where, due to shear deformation, we have
$$
\frac{d x}{d y}=\frac{\Delta x}{\Delta y}=G, \qquad (A7)
$$
where $G$ is the shear modulus, which, for a planar orthotropic material, is given in terms of the Poisson ratio, $\nu$, by $G=1 / 2(1+\nu)$. Thus
$$
\begin{aligned}
\frac{d F_{s x}(x, y)}{d y} & =\frac{1}{2(1+\nu)} \frac{d F(x, y)}{d x}, \\
\frac{d F_{s x}(x, y)}{d y} & =-\frac{1}{2(1+\nu)} \frac{F_{0}}{\left(x+L_{z}\right)^{2}}, \\
F_{s x}(x, y) & =-\frac{1}{2(1+\nu)} \frac{F_{0} y}{\left(x+L_{z}\right)^{2}}+c.
\end{aligned}
\qquad (A8)
$$

On the neutral axis $(y=0)$ the shear stress vanishes, hence $c=0$. Finally, the stress tensor over all four quadrants is given by
$$
\boldsymbol{\sigma}(x, y)=\frac{F_{0}}{L_{z}}\left(\begin{array}{cc}
0 & -\frac{1}{2(1+\nu)} \frac{\operatorname{sgn}[x]|y|}{(|x|+1)^{2}} \\
-\frac{1}{2(1+\nu)} \frac{\operatorname{sgn}[x]|y|}{(|x|+1)^{2}} & \frac{1}{(|x|+1)}
\end{array}\right), \qquad (A9)
$$
where $x \to x / L_{z}$ and $y \to x / L_{z}$ have been scaled by the ribbon thickness.

The components of the strain tensor can be found from the compliance tensor. For a planar, isotropic material, the transformation reads
$$
\left(\begin{array}{l}
\varepsilon_{x x}(x, y) \\
\varepsilon_{y y}(x, y) \\
\varepsilon_{x y}(x, y)
\end{array}\right)=\frac{1}{E}\left(\begin{array}{ccc}
1 & -\nu & 0 \\
-\nu & 1 & 0 \\
0 & 0 & (1+\nu)
\end{array}\right)\left(\begin{array}{l}
\sigma_{x x}(x, y) \\
\sigma_{y y}(x, y) \\
\sigma_{x y}(x, y)
\end{array}\right), \qquad (A10)
$$
where $E$ is the Young's modulus, which here carries units of $\mathrm{N} \mathrm{m}^{-1}$. Thus, the strain tensor reads
$$
\boldsymbol{\varepsilon}(x, y)=\frac{F_{0}}{E L_{z}}\left(\begin{array}{cc}
-\frac{\nu}{(|x|+1)} & -\frac{\operatorname{sgn}[x]|y|}{2(|x|+1)^{2}} \\
-\frac{\operatorname{sgn}[x]|y|}{2(|x|+1)^{2}} & \frac{1}{(|x|+1)}
\end{array}\right). \qquad (A11)
$$

[1] A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, Rev. Mod. Phys. 81, 109 (2009).

[2] D. S. L. Abergel, V. Apalkov, J. Berashevich, K. Ziegler, and T. Chakraborty, Adv. Phys. 59, 261 (2010).

[3] S. Das Sarma, S. Adam, E. H. Hwang, and E. Rossi, Rev. Mod. Phys. 83, 407 (2011).

[4] F. Schwierz, Nat. Nano. 5, 487 (2010).

[5] K. Wakabayashi, M. Fujita, H. Ajiki, and M. Sigrist, Phys. Rev. B 59, 8271 (1999).

[6] A. V. Rozhkov, G. Giavaras, Y. P. Bliokh, V. Freilikher, and F. Nori, Phys. Rep. 503, 77 (2011).

[7] P. P. Shinde and V. Kumar, Phys. Rev. B 84, 125401 (2011).

[8] T. P. Kaloni, R. P. Joshi, N. P. Adhikari, and U. Schwingenschlögl, Appl. Phys. Lett. 104, 073116 (2014).

[9] F. Varchon, R. Feng, J. Hass, X. Li, B. N. Nguyen, C. Naud, P. Mallet, J.-Y. Veuillen, C. Berger, E. H. Conrad, and L. Magaud, Phys. Rev. Lett. 99, 126805 (2007).

[10] D. Marchenko, A. Varykhalov, M. R. Scholz, G. Bihlmayer, E. I. Rashba, A. Rybkin, A. M. Shikin, and O. Rader, Nat. Commun. 3, 1232 (2012).

[11] V. M. Pereira, A. H. Castro Neto, and N. M. R. Peres, Phys. Rev. B 80, 045401 (2009).

[12] V. M. Pereira, R. M. Ribeiro, N. M. R. Peres, and A. H. Castro Neto, Europhys. Lett. 92, 67001 (2010).

[13] F. Hipolito, A. J. Chaves, R. M. Ribeiro, M. I. Vasilevskiy, V. M. Pereira, and N. M. R. Peres, Phys. Rev. B 86, 115430 (2012).

[14] C. Si, Z. Liu, W. Duan, and F. Liu, Phys. Rev. Lett. 111, 196802 (2013).

[15] A. L. Kitt, V. M. Pereira, A. K. Swan, and B. B. Goldberg, Phys. Rev. B 85, 115432 (2012).

[16] A. L. Kitt, V. M. Pereira, A. K. Swan, and B. B. Goldberg, Phys. Rev. B 87, 159909(E) (2013).

[17] V. M. Pereira and A. H. Castro Neto, Phys. Rev. Lett. 103, 046801 (2009).

[18] F. Guinea, M. I. Katsnelson, and A. K. Geim, Nat. Phys. 6, 30 (2010).

[19] M. Ramezani Masir, D. Moldovan, and F. M. Peeters, Solid State Commun. 175-176, 76 (2013).

[20] M. Neek-Amal and F. M. Peeters, Phys. Rev. B 85, 195446 (2012).

[21] M. Neek-Amal, L. Covaci, and F. M. Peeters, Phys. Rev. B 86, 041405(R) (2012).

[22] D. Moldovan, M. Ramezani Masir, and F. M. Peeters, Phys. Rev. B 88, 035446 (2013).

[23] L. D. Landau and E. M. Lifshitz, Theory of Elasticity, 3rd ed. (Pergamon, New York, 1975).

[24] C. Lee, X. Wei, J. W. Kysar, and J. Hone, Science 321, 385 (2008).

[25] O. L. Blakslee, D. G. Proctor, E. J. Seldin, G. B. Spence, and T. Weng, J. Appl. Phys. 41, 3373 (1970).

[26] S.-M. Choi, S.-H. Jhi, and Y.-W. Son, Phys. Rev. B 81, 081407(R) (2010).

[27] J. V. Sloan, A. A. Pacheco Sanjuan, Z. Wang, C. Horvath, and S. Barraza-Lopez, Phys. Rev. B 87, 155436 (2013).

[28] S. Barraza-Lopez, A. A. Pacheco Sanjuan, Z. Wang, and M. Vanević, Solid State Commun. 166, 70 (2013).