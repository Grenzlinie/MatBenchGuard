![](./images/811264329662857218_1.jpg)

Computational Materials Science 122 (2016) 288-294

Contents lists available at ScienceDirect

# Computational Materials Science

journal homepage: www.elsevier.com/locate/commatsci

![](./images/811264329662857218_2.jpg)

# Numerical investigation of microstructure effect on mechanical properties of bi-continuous and particulate reinforced composite materials

![](./images/811264329662857218_3.jpg)

Hailong Chen $^{a,1}$, Lingyi Meng $^{b}$, Shaohua Chen $^{a}$, Yang Jiao $^{a}$, Yongming Liu $^{a,*}$

$^{a}$ School for Engineering of Matter, Transport and Energy, Arizona State University, Tempe, AZ 85287, USA
$^{b}$ School of Civil Engineering and Transportation, South China University of Technology, Guangzhou 510641, China

---

## ARTICLE INFO

**Article history:**
Received 20 April 2016
Received in revised form 26 May 2016
Accepted 28 May 2016

**Keywords:**
Voxel-based analysis
Microstructure
Homogenization
Fracture
Composites

## ABSTRACT

In this paper, numerical simulations are proposed to investigate mechanical properties of bi-continuous and particulate reinforced composite materials using a non-local voxel-based discrete computational model. Special focus of this article is the effect of 3D microstructure and its heterogeneity on elastic deformation and fracture behaviors. First, a review on model formulation is presented. Model parameters are derived in terms of material constants using the concept of energy equivalency. Interface representation and numerical homogenization scheme are discussed. Following this, numerical investigations on the effects of interface properties and inclusion characteristics, i.e. the volume fraction and material constants, on homogenized elastic constants and fracture behaviors of statistically isotropic bi-phase composites are performed. The effective elastic constants predicted by the proposed model agree well with analytical results. Fracture simulation demonstrates good capability of the proposed model for the microstructure-sensitive failure analysis. Conclusions and future work are drawn based on the posed study.

© 2016 Published by Elsevier B.V.

---

## 1. Introduction

Significant progresses in advanced imaging techniques, such as Electron Backscatter Diffraction (EBSD) [1] and X-ray tomographic Microscopy [2], have enabled the incorporation of material microstructural information into mechanical modeling of materials, as reported in Refs. [3-8]. On one hand, when micrographic information is limited (e.g., only two-dimensional images are available) and plane strain/stress assumptions are valid under particular loading conditions, two-dimensional microstructure-based analyses can be used and essential mechanical behaviors of such materials can be obtained from corresponding simulations [9-11]. On the other hand, since most materials possess intrinsic three-dimensional heterogeneous microstructure in nature [12], such as polycrystalline materials and composite materials, a three-dimensional analysis is usually required in order to fully characterize and understand the physical properties of such materials [11].

Three-dimensional microstructures can be obtained by direct imaging techniques and numerical reconstructions. Advanced imaging techniques, such as X-ray tomographic microscopy [2] and multi-scale imaging [13], have been widely used to obtain three-dimensional microstructure with high-resolution for a wide range of heterogeneous materials, such as metal matrix composites [14]. In the meantime, a variety of three-dimensional microstructure reconstruction methods from limited two-dimensional information have been developed, such as the stochastic reconstruction procedure [15-20] and the multi-point reconstruction method [21-24]. The reconstruction techniques greatly reduce the experimental cost for full 3D imaging and enhance the computational materials investigation.

In this paper, we investigate the microstructure effect on mechanical properties of stochastically reconstructed three-dimensional bi-continuous and particulate reinforced composite materials. A three-dimensional voxel-based computational tool is proposed for the microstructure sensitive mechanical analysis. The paper is organized as follows: First, a brief review of the model formulation is given. The model parameters are derived based on the energy equivalency and the theory of hyper-elasticity. The interface representation and homogenization scheme for three-dimensional simulation are discussed. Following this, numerical

---

* Corresponding author.
E-mail address: Yongming.Liu@asu.edu (Y. Liu).
1 Current Address: Fuels Modeling and Simulation, Idaho National Laboratory, Idaho Falls, ID 83402, USA.

http://dx.doi.org/10.1016/j.commatsci.2016.05.037
0927-0256/© 2016 Published by Elsevier B.V.

studies on elastic homogenization and quasi-static fracture of bi-phase composite materials are performed. Effects of interface elastic properties, inclusion shape, volume fraction and spatial distribution on the effective elastic properties and fracture behaviors are investigated. Finally, conclusions are drawn based on this study.

### 2. Voxel-based computational tool: a review

In voxel-based models, a given volume of material is represented by a three-dimensional regular grid (array of voxels on periodic lattice). A voxel is a volume element, located at the lattice site following certain packing, such as the simple cubic packing shown in Fig. 1(a). The voxels are connected with their neighbors via axial springs. The interaction between a typical voxel pair is nonlocal in the sense that it not only depends on the voxel pair itself, but also has contribution from all neighboring voxels. Theoretically, a typical voxel can interact with all its neighboring voxels. In this study, only the first and the second nearest neighboring voxels are considered (see Fig. 1(b)).

#### 2.1. Model parameters derivation

The derivation of model parameters in terms of material constants is based on the equivalency of energy [25], i.e., the potential energy of a voxel should be identical in both the continuum and discrete descriptions. In the discrete description, the potential energy is described based on the concept of the unit cell. A unit cell is a repeating non-overlapping unit identified from the geometric relationship between a reference voxel and its neighbors. For the two-neighbor case in this study, the unit cell for the first nearest neighbors is a cube and the unit cell for the second nearest neighbors is a rhombic dodecahedron, as shown in Fig. 1(c). For a given packing, the corresponding unit normal vectors of a typical voxel can be calculated. For the case of simple cubic packing with first and second nearest neighbors, the normal vectors are given in Table 1. These unit normal vectors will be used to calculate the potential energy of a typical voxel.

The total potential energy of a reference voxel is the sum of the energies from these two unit cells, which can be written as

$$
U_{voxel\_i} = \sum_{k=1}^{2} U_{cell\_k}^{i}
\tag{1}
$$

And for each unit cell the energy has two parts

$$
U_{cell\_k}^{i} = U_{local\_k}^{i} + U_{nonlocal\_k}^{i}
\tag{2}
$$

where

$$
U_{local\_k}^{i} = \frac{1}{2} \left( \alpha_{k}^{i} \sum_{j=1}^{N_{k}^{i}} \left( \delta l_{kj}^{i} \cdot \delta l_{kj}^{i} \right) \right)
\tag{3}
$$

is the pair-wise local potential energy, and

$$
U_{nonlocal\_k}^{i} = \frac{1}{2} t_{k}^{i} \left( \sum_{j=1}^{N_{k}^{i}} \delta l_{kj}^{i} \right) \cdot \left( \sum_{j=1}^{N_{k}^{i}} \delta l_{kj}^{i} \right)
\tag{4}
$$

is the non-local multi-body potential energy of unit cell $k$ of voxel $i$.

In Eqs. (3) and (4), $\alpha_{k}^{i}$ and $t_{k}^{i}$ are the pairwise and multi-body parameters for springs associated with unit cell $k$ of voxel $i$; $N_{k}^{i}$ is the total number of neighbors for unit cell $k$ of voxel $i$, and $\delta l_{kj}^{i}$ is the half length of spring elongation of spring $j$ of unit cell $k$ of voxel $i$.

Given the potential of each voxel, i.e., Eqs. (1)–(4), the interaction between a reference voxel and its neighbor $j$ can be calculated by differentiating the potential energy with respect to its length change as

$$
f_{kj}^{i} = -\frac{\partial U_{voxel\_i}}{\partial \left( \delta l_{kj}^{i} \right)} = -\alpha_{k}^{i} \left( \delta l_{kj}^{i} \right) - t_{k}^{i} \left( \sum_{m=1}^{N_{k}^{i}} \delta l_{km}^{i} \right)
\tag{5}
$$

The effective spring stiffness can be obtained from Eq. (5) as

$$
\alpha_{kj}^{i} = \alpha_{k}^{i} + t_{k}^{i} \left( \sum_{m=1}^{N_{k}^{i}} \left( \frac{\delta l_{km}^{i}}{\delta l_{kj}^{i}} \right) \right)
\tag{6}
$$

From Eq. (6), it is clear that the effective spring stiffness for each spring in the proposed lattice spring model is non-local. This nonlocality removes the well-known restriction on materials' Poisson's ratio of classical lattice spring models [26].

If the spring elongations are related to components of strain tensor $\boldsymbol{\varepsilon}$ at the continuum level, the potential of unit cell $k$ can be rewritten in terms of strain components and spring normal vectors given in Table 1 as

$$
U_{cell\_k}^{i} = \frac{1}{2} \left( l_{k} \right)^{2} \left( \alpha_{k}^{i} \sum_{b=1}^{N_{k}^{i}} \left( n_{I}^{b} \varepsilon_{IJ} n_{J}^{b} n_{K}^{b} \varepsilon_{KL} n_{L}^{b} \right) + t_{k}^{i} \left( \sum_{b=1}^{N_{k}^{i}} n_{I}^{b} \varepsilon_{IJ} n_{J}^{b} \right) \left( \sum_{b=1}^{N_{k}^{i}} n_{K}^{b} \varepsilon_{KL} n_{L}^{b} \right) \right)
\tag{7}
$$

where $l_{k}$ is the distance between the reference voxel $i$ with its $k$th neighbor at the un-deformed condition, i.e. the original spring length. $l_1$ equals to a voxel length and $l_2 = \sqrt{2l_1}$.

By conservation of the potential energy, the material stiffness tensor according to the theory of hyper-elasticity for a reference voxel can be obtained as

$$
\begin{aligned}
C_{IJKL}^{i} &= \frac{1}{V_{1}} \frac{\partial^{2} \left( U_{cell\_1}^{i} \right)}{\partial \varepsilon_{IJ} \partial \varepsilon_{KL}} + \frac{V_{2}}{V_{1}} \left( \frac{1}{V_{2}} \frac{\partial^{2} \left( U_{cell\_2}^{i} \right)}{\partial \varepsilon_{IJ} \partial \varepsilon_{KL}} \right) \\
&= \frac{1}{8} \alpha_{1}^{i} \sum_{b=1}^{6} n_{I}^{b} n_{J}^{b} n_{K}^{b} n_{L}^{b} + \frac{1}{8} t_{1}^{i} \left( \sum_{b=1}^{6} n_{I}^{b} n_{J}^{b} \right) \left( \sum_{b=1}^{6} n_{K}^{b} n_{L}^{b} \right) \\
&\quad + \frac{1}{4} \alpha_{2}^{i} \sum_{b=7}^{18} n_{I}^{b} n_{J}^{b} n_{K}^{b} n_{L}^{b} + \frac{1}{4} t_{2}^{i} \left( \sum_{b=7}^{18} n_{I}^{b} n_{J}^{b} \right) \left( \sum_{b=7}^{18} n_{K}^{b} n_{L}^{b} \right)
\end{aligned}
\tag{8}
$$

where $V_{1} = l_{1}^{3}$ is the volume of the unit cell 1. $V_{2} = 2l_{1}^{3}$ is the volume of the unit cell 2.

In the proposed study, it is assumed that the nonlocal parameters for the two unit cells are identical for Hookean isotropic materials. Thus, the model parameters in terms of material's Young's modulus and Poisson's ratio can be uniquely solved as

$$
\begin{aligned}
\alpha_{1}^{i} &= \frac{l_{1} E}{1+\nu}, \quad \alpha_{2}^{i} = \frac{l_{1} E}{1+\nu} \\
t^{i} &= \frac{l_{1} E(4\nu-1)}{18(1+\nu)(1-2\nu)}
\end{aligned}
\tag{9}
$$

where $E$ and $\nu$ are the Young's modulus and Poisson's ratio of a material.

The stress and strain tensors at each reference voxel center can also be calculated based on the potential energy as

$$
\begin{aligned}
\boldsymbol{\sigma}_{i} &= \frac{1}{V_{1}} \frac{\partial U_{voxel\_i}}{\partial \boldsymbol{\varepsilon}_{i}} = \frac{1}{V_{i}} \sum_{n=1}^{2} \sum_{j=1}^{N_{n}^{i}} l_{nj}^{i} \frac{\partial U_{cell\_n}^{i}}{\partial \delta l_{nj}^{i}} \frac{\partial e_{nj}^{i}}{\partial \boldsymbol{\varepsilon}_{i}} \\
&= \frac{1}{V_{1}} \sum_{n=1}^{2} \sum_{j=1}^{N_{n}^{i}} l_{nj}^{i} \left( \alpha_{n}^{i} \delta l_{nj}^{i} + T_{n}^{i} \sum_{k=1}^{N_{n}^{i}} \delta l_{nk}^{i} \right) \mathbf{n}_{nj}^{i} \left( \mathbf{n}_{nj}^{i} \right)^{T}
\end{aligned}
\tag{10}
$$

and

$$
\boldsymbol{\varepsilon}_{i} = \boldsymbol{\sigma}_{i} \cdot \mathbf{S}_{i}
\tag{11}
$$

where $\mathbf{S}_{i}$ is the compliance matrix of voxel $i$.

![](./images/811264329662857218_4.jpg)

Fig. 1. The voxel system in the proposed model.

<table><caption>Table 1 List of normal vectors of a typical voxel for the simple cubic packing.</caption>
<thead>
<tr>
<th>$n_1$</th>
<th>$(1,0,0)$</th>
<th>$n_{10}$</th>
<th>$(-\sqrt{2}/2,-\sqrt{2}/2,0)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$n_2$</td>
<td>$(0,1,0)$</td>
<td>$n_{11}$</td>
<td>$(\sqrt{2}/2,0,\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_3$</td>
<td>$(-1,0,0)$</td>
<td>$n_{12}$</td>
<td>$(0,\sqrt{2}/2,\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_4$</td>
<td>$(0,-1,0)$</td>
<td>$n_{13}$</td>
<td>$(-\sqrt{2}/2,0,\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_5$</td>
<td>$(0,0,1)$</td>
<td>$n_{14}$</td>
<td>$(0,-\sqrt{2}/2,\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_6$</td>
<td>$(0,0,-1)$</td>
<td>$n_{15}$</td>
<td>$(\sqrt{2}/2,0,-\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_7$</td>
<td>$(\sqrt{2}/2,-\sqrt{2}/2,0)$</td>
<td>$n_{16}$</td>
<td>$(0,\sqrt{2}/2,-\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_8$</td>
<td>$(\sqrt{2}/2,\sqrt{2}/2,0)$</td>
<td>$n_{17}$</td>
<td>$(-\sqrt{2}/2,0,-\sqrt{2}/2)$</td>
</tr>
<tr>
<td>$n_9$</td>
<td>$(-\sqrt{2}/2,\sqrt{2}/2,0)$</td>
<td>$n_{18}$</td>
<td>$(0,-\sqrt{2}/2,-\sqrt{2}/2)$</td>
</tr>
</tbody>
</table>

The above derivation of model parameters follows the same procedure as described in Ref. [9]. The only difference is that the final form of the potential energy and hence the material stiffness matrix is different. This is true for different packing systems as shown in Ref. [27].

### 2.2. Interface representation
Many studies have been devoted to analyze the interface effect on particulate composites using different interface models [28]. As discussed in Ref. [9], interface is intrinsic in discrete models and it is represented by springs straddling across different phases. By assigning different interface parameters for interface springs, interface effects can be effectively considered in these models. A schematic diagram illustrating the interface representation for 3D voxel-based modeling is shown in Fig. 2. Different color indicates different phases and springs.

### 2.3. Homogenization scheme
Many analytical and numerical homogenization schemes are available in the literature, such as Hashin-Shtrikman bounds [29], third-order approximation method [30], and energy based numerical approaches [31]. In this section, the homogenization procedure presented in Refs. [9,31] for two-dimensional analysis is extended to three-dimensional cases.

The calculation of the effective elastic moduli is conducted in the following three steps:

(i) Apply uniform tri-axial extension to the investigated microstructure domain, corresponding to a strain state $\varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=\varepsilon_{0}$, and calculate the total strain energy $U_{(1)}$ as a sum of energies of all voxels;

(ii) Apply uniform bi-axial extension on four faces and apply uniform uniaxial compression on the other two faces, which is corresponding to the strain state of $-\varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=\varepsilon_{0}$. Following this, the total strain energy $U_{(2)}^i$ is calculated. This step is repeated three times by rotating the bi-axial strain state to other faces and the average calculated strain energy $U_{(2)}=\frac{1}{3}\sum_{i=1}^{3}U_{(2)}^i$ is chosen as the strain energy for this step;

In terms of the bulk modulus $K$ and shear modulus $G$, the strain energy of a three-dimensional homogeneous isotropic linear elastic continuum of volume $V$ is

$$
U=V\left(\frac{K}{2}\varepsilon_{ii}\varepsilon_{jj}+G\left(\varepsilon_{ij}\varepsilon_{ij}-\frac{1}{3}\varepsilon_{ii}\varepsilon_{jj}\right)\right) \tag{12}
$$

Thus, the bulk modulus and shear modulus can be obtained using the strain energy data as

$$
K=\frac{2}{9}\frac{U_{(1)}}{V\varepsilon_{0}^{2}} \tag{13}
$$

$$
G=\frac{1}{24}\frac{9U_{(2)}-U_{(1)}}{V\varepsilon_{0}^{2}} \tag{13}
$$

The Poisson's ratio in terms of the bulk and shear moduli is

$$
\nu=\frac{3K-2G}{2(3K+G)} \tag{14}
$$

Thus, the model parameters can be derived in terms of the material constants using the concept of energy equivalency and the theory of hyper-elasticity. In next section, the proposed 3D voxel based model will be used in the microstructure-sensitive mechanical analysis of different composite systems.

### 3. Numerical results
The microstructure systems used in this study are generated using the stochastic reconstruction procedure (for bi-continuous composites) and the hard-particle Monte Carlo (MC) simulations [32] (for particulate composites). Typical systems generated using these methods are shown in Fig. 3, with the red color indicating the inclusion and the blue color representing the matrix. Simulations

![](./images/811264329662857218_5.jpg)

Fig. 2. Interface representation in the proposed model.

![](./images/811264329662857218_6.jpg)

Fig. 3. Microstructures for different bi-phase composite systems used in this study (v.f. 50%).

in this section will be based on these two digitized microstructures. The dimensions are assumed to be 0.01 m along each edges and the domain is discretized with a voxel density of 128 × 128 × 128.

The material properties for different phases are: Young's modulus $E_m = 110\ GPa$, $\nu_m = 0.34$ and $E_i = 450\ GPa$, $\nu_i = 0.17$, where $m$ indicates the matrix and $i$ for the inclusion. For the elastic homogenization problem, the implicit solution scheme developed in Ref. [33] is used, while the explicit solution scheme discussed in Refs. [26,34] is used for quasi-static fracture problems.

### 3.1. Elastic homogenization
In this subsection, the proposed voxel-based discrete model is applied to estimate the effective elastic properties of aforementioned two composite systems. The procedure described in Section 2.3 is carried out for this purpose. We consider both the inclusion volume fraction effect and the interface effect on the effective elastic properties of these two composite systems. Two types of interface properties are used, i.e., interface 1 assumes the interface has the same properties as the inclusion while interface 2 assigns matrix properties to the interface.

The obtained results are shown in Fig. 4 for bi-continuous composite system and Fig. 6 for particulate reinforced composite system. As can be seen, the predicted effective constants, bulk modulus and shear modulus, do not exactly fit with the Hashin-Shtrikman (H-S) bound [29] for all inclusion volume fractions, which is different from the observation from the two-dimensional analysis [9]. The interface effect is more important for the three-dimensional analysis than the two-dimensional analysis in determining the effective material constants of composite systems. This is due to the fact that for a fixed inclusion volume fraction, the interface volume fraction is larger for the three-dimensional case than that for the two-dimensional case.

The calculated von Mises strain and stress using the Eqs. (10) and (11) for the case of 50% inclusion volume fraction are shown in Figs. 5 and 7 for bi-continuous and particulate composite systems, respectively. As can be seen, the stress concentration occurs at the matrix-inclusion interface. This is due to the discontinuity of material properties at the interface.

### 3.2. Fracture modeling
The fracture modeling of general solid material is a nontrivial problem in the literature. The complexity of the microstructure of reinforced composites adds additional difficulties. In this example, the proposed voxel-based model is applied to study the fracture behaviors, e.g., interfacial debonding, of particulate composites. This problem has been shown to be critical for the strength of particulate composite and has been investigated extensively, such as [35].

Three different particulate composites are considered in this example. All these systems have the same inclusion volume fraction and inclusion size, but with different inclusion distribution. Two descriptors are used to characterize the particulate distribution, i.e., the two-point correlation function S2(r) and the lineal-

![](./images/811264329662857218_7.jpg)

Fig. 4. The effective elastic moduli for bi-continuous composite system.

![](./images/811264329662857218_8.jpg)

Fig. 5. The von Mises stress and strain distributions for bi-continuous composite system (vol% = 50).

![](./images/811264329662857218_9.jpg)

Fig. 6. The effective elastic moduli for particulate composite system.

![](./images/811264329662857218_10.jpg)

Fig. 7. The von Mises stress and strain distributions for particulate composite system (vol% = 50).

![](./images/811264329662857218_11.jpg)

Fig. 8. The S2 and L functions for three different particulate composite systems.

![](./images/811264329662857218_12.jpg)

Fig. 9. The crack surfaces for three different particulate composites.

![](./images/811264329662857218_13.jpg)

Fig. 10. The reaction force on the top face versus applied strain.

path function L(r). The two-point correlation function S2(r) gives the probability of finding two points in the phases of interest [12,36,37]. The lineal-path function L(r) gives the probability that a randomly chosen line segment of length r entirely falls into the phase of interest [12,38]. The corresponding S2(r) and L(r) for the particulate inclusion phase are calculated and shown in Fig. 8. As can be seen, among the three different composites, the probabilities of finding two points in the inclusion phases are slightly different while the probabilities that a randomly chosen line segment entirely falls into the inclusion phase are the same.

For all three composites, the interfaces are assumed to have the properties of the matrix. Constant loading rates are applied on the top and bottom surfaces to simulate the uniaxial tension loading case. The critical elongation failure criterion is used and the critical values being $0.1\%$ and $0.1\%/\sqrt{2}$ for springs connecting the first and the second neighbors, respectively. Periodic boundary condition is applied on the lateral surfaces in a way similar to the Molecular Dynamic simulations (MD).

The final crack surface for three different composites are shown in Fig. 9. The color indicates phases, i.e., the red one is the inclusion while the blue one is the matrix. The crack surfaces 1-3 correspond to the S2 and L curves in Fig. 8. As can be seen, the major failure mechanism of the particulate reinforced composites is the interfacial debonding, which is consistent with the experimental observation [39].

Statistical information obtained from the three crack surfaces are as follows: For the inclusion phase, the ratios of voxels on the crack surface to the total number of inclusion voxels are 1.2%, 1.3% and 1.6%, respectively. For the matrix phase, the ratios are 9.6%, 10.5% and 12.7%, respectively. The ratios of voxels on the crack surface to the total number of voxels are 5.4%, 5.9% and 7.2%, respectively.

The reaction forces on the top surfaces versus the applied strains are shown in Fig. 10. Microstructure 1 has the smallest peak reaction force and microstructure 3 has the largest peak reaction force. This is consistent with the statistical data from the crack surfaces show in Fig. 9. This is due to the larger energy required for larger crack surfaces.

## 4. Conclusions

In this paper, a three-dimensional voxel-based numerical investigation of microstructure effect on mechanical properties of bicontinuous and particulate reinforced composite materials was presented. In the proposed computational model, both the first and second nearest neighbors of a voxel were considered. The local and nonlocal model parameters were derived using the concept of energy equivalency and the theory of hyper-elasticity. The interface was represented by springs straddling different phases. The

fracture behaviors were modeled using a spring-based critical fail- ure criterion.

The proposed voxel-based computational tool can be effectively applied to the microstructure-sensitive mechanical analysis of composite materials. For elastic homogenization, the effective con- stants calculated using the proposed computational tool are con- sistent with other analytical predictions. The interfacial debonding failure mechanism of particulate reinforced composites is accurately captured.

In the current study, no material defects have been considered in any of the simulation. As has been reported in [40,41], evolution of defects, such as grain boundaries in crystalline martials, is very important in studying both the elastic and fracture behaviors of materials under extreme conditions. The proposed computational tool needs further investigation to model the defect effects on the mechanical behaviors of composite materials. The investiga- tion of the particulate spatial distribution effect, i.e. clustering effect, on the failure behaviors of particulate composite needs fur- ther work.

## Acknowledgement

This work is partially supported by DARPA under Grant No. N66001-14-1-4036.

## References

[1] V. Randle, Applications of electron backscatter diffraction to materials science: status in 2009, J. Mater. Sci. 44 (16) (2009) 4211-4218.
[2] J.H. Kinney, M.C. Nichols, X-ray tomographic microscopy (XTM) using synchrotron radiation, Annu. Rev. Mater. Sci. 22 (1) (1992) 121-152.
[3] L.L. Mishnaevsky Jr, Automatic voxel-based generation of 3D microstructural FE models and its application to the damage analysis of composites, Mater. Sci. Eng., A 407 (1-2) (2005) 11-23.
[4] J.H. Kim, M.-G. Lee, R.H. Wagoner, A boundary smoothing algorithm for image- based modeling and its application to micromechanical analysis of multi- phase materials, Comput. Mater. Sci. 47 (3) (2010) 785-795.
[5] E. Tarleton, M.N. Charalambides, C. Leppard, Image-based modelling of binary composites, Comput. Mater. Sci. 64 (2012) 183-186.
[6] A. Alghamdi, P. Mummery, M.A. Sheikh, Multi-scale 3D image-based modelling of a carbon/carbon composite, Modell. Simul. Mater. Sci. Eng. 21 (8) (2013) 085014.
[7] B. Sun, X. Wang, Z. Li, Meso-scale image-based modeling of reinforced concrete and adaptive multi-scale analyses on damage evolution in concrete structures, Comput. Mater. Sci. 110 (2015) 39-53.
[8] J. Zhang et al., Crack initiation and fatigue life prediction on aluminum lug joints using statistical volume element-based multiscale modeling, J. Intell. Mater. Syst. Struct. (2012).
[9] H. Chen et al., A novel discrete computational tool for microstructure-sensitive mechanical analysis of composite materials, Mater. Sci. Eng., A 659 (2016) 234-241.
[10] O. Amsellem et al., Two-dimensional (2D) and three-dimensional (3D) analyses of plasma-sprayed alumina microstructures for finite-element simulation of Young's modulus, J. Mater. Sci. 43 (12) (2008) 4091-4098.
[11] H.J. Böhm, W. Han, Comparisons between three-dimensional and two- dimensional multi-particle unit cell models for particle reinforced metal matrix composites, Modell. Simul. Mater. Sci. Eng. 9 (2) (2001) 47.
[12] S. Torquato, Random heterogeneous media: microstructure and improved bounds on effective properties, Appl. Mech. Rev. 44 (1991) 37-76.
[13] K.M. Gerke, M.V. Karsanina, D. Mallants, Universal Stochastic Multiscale Image Fusion: An Example Application for Shale Rock, Sci. Rep. 5 (2015) 15880.
[14] A. Borbély et al., Three-dimensional characterization of the microstructure of a metal-matrix composite by holotomography, Mater. Sci. Eng., A 367 (1-2) (2004) 40-50.
[15] C.L.Y. Yeong, S. Torquato, Reconstructing random media. II. Three-dimensional media from two-dimensional cuts, Phys. Rev. E 58 (1) (1998) 224-233.
[16] H. Xu et al., Descriptor-based methodology for statistical characterization and3D reconstruction of microstructural materials, Comput. Mater. Sci. 85 (2014)206-216.
[17] S. Chen, H. Li, Y. Jiao, Dynamic reconstruction of heterogeneous materials and microstructure evolution, Phys. Rev. E 92 (2) (2015) 023301.
[18] K.M. Gerke, M.V. Karsanina, Improving stochastic reconstructions by weighting correlation functions in an objective function, EPL 111 (5) (2015).
[19] A. Hasanabadi et al., 3D microstructural reconstruction of heterogeneous materials from 2D cross sections: a modified phase-recovery algorithm, Comput. Mater. Sci. 111 (2016) 107-115.
[20] S. Chen et al., Stochastic multi-scale reconstruction of 3D microstructure consisting of polycrystalline grains and second-phase particles from 2D micrographs, Metall. Mater. Trans. A 47 (3) (2016) 1440-1450.
[21] H. Okabe, M.J. Blunt, Pore space reconstruction using multiple-point statistics, J. Petrol. Sci. Eng. 46 (1-2) (2005) 121-137.
[22] P. Avery, C. Farhat, G. Reese, Fast frequency sweep computations using a multi- point Padé-based reconstruction method and an efficient iterative solver, Int. J. Num. Meth. Eng. 69 (13) (2007) 2848-2875.
[23] A. Hajizadeh, A. Safekordi, F.A. Farhadpour, A multiple-point statistics algorithm for 3D pore space reconstruction from 2D images, Adv. Water Resour. 34 (10) (2011) 1256-1267.
[24] Y. Staraselski et al., Reconstruction of the 3D representative volume element from the generalized two-point correlation function, Modell. Simul. Mater. Sci. Eng. 23 (1) (2015) 015007.
[25] H. Chen, Y. Jiao, Y. Liu, A nonlocal lattice particle model for fracture simulation of anisotropic materials, Compos. B Eng. 90 (2016) 141-151.
[26] H. Chen, E. Lin, Y. Liu, A novel volume-compensated particle method for 2D elasticity and plasticity analysis, Int. J. Solids Struct. 51 (9) (2014) 1819-1833.
[27] H. Chen, Y. Liu, A non-local 3D lattice particle framework for elastic solids, Int. J. Solids Struct. 81 (2016) 411-420.
[28] W.X. Xu, H.S. Chen, Analytical and modeling investigations of volume fraction of interfacial layers around ellipsoidal aggregate particles in multiphase materials, Modell. Simul. Mater. Sci. Eng. 21 (1) (2013) 015005.
[29] Z. Hashin, Z. Shtrikman, A variational approach to the theory of the elastic behaviour of multiphase materials, J. Mech. Phys. Solids 11 (2) (1963) 127-140.
[30] S. Torquato, Effective stiffness tensor of composite media: II. Application to isotropic dispersions, J. Mech. Phys. Solids 46 (1998) 1411-1440.
[31] H. Chen, Y. Jiao, Y. Liu, Investigating the microstructural effect on elastic and fracture behavior of polycrystals using a nonlocal lattice particle model, Mater. Sci. Eng., A 631 (2015) 173-180.
[32] S. Torquato, Y. Jiao, Dense packings of polyhedra: platonic and archimedean solids, Phys. Rev. E 80 (4) (2009) 041104.
[33] E. Lin, H. Chen, Y. Liu, Finite element implementation of a non-local particle method for elasticity and fracture analysis, Finite Elem. Anal. Des. 93 (2015) 1-11.
[34] H. Chen et al., A generalized 2D non-local lattice spring model for fracture simulation, Comput. Mech. 54 (6) (2014) 1541-1558.
[35] Y. Jiang, K. Tohgo, An incremental damage theory for micropolar composites taking account of progressive debonding and particle size effect, Comput. Mater. Sci. 50 (12) (2011) 3358-3364.
[36] Y. Jiao, F.H. Stillinger, S. Torquato, Modeling heterogeneous materials via two- point correlation functions: basic principles, Phys. Rev. E 76 (3)(2007) 031110.
[37] Y. Jiao, F.H. Stillinger, S. Torquato, Modeling heterogeneous materials via two- point correlation functions. Il. Algorithmic details and applications, Phys. Rev. E77(3)(2008) 031135.
[38] B. Lu, S. Torquato, Lineal-path function for random heterogeneous materials, Phys. Rev. A 45 (2) (1992) 922-929.
[39] P.N. Bindumadhavan, H.K. Wah, O. Prabhakar, Assessment of particle-matrix debonding in particulate metal matrix composites using ultrasonic velocity measurements, Mater. Sci. Eng., A 323 (1-2) (2002) 42-51.
[40] Z. Chen et al., Dislocation climb strengthening in systems with immobile obstacles: three-dimensional level-set simulation study, Phys. Rev. B 81 (5)(2010) 054104.
[41] A.T. Lim et al., Stress-driven migration of simple low-angle mixed grain boundaries, Acta Mater. 60 (3) (2012) 1395-1407.