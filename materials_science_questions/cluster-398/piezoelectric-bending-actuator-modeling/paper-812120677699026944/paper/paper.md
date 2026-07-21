**RESEARCH PAPER**

Xianghua Guo · Daining Fang · Ai Kah Soh
Hyun Chul KIM · Jung Ju Lee

# Analysis of piezoelectric ceramic multilayer actuators based on an electro-mechanical coupled meshless method

Received: 15 April 2005 / Accepted: 6 September 2005 / Revised: 14 November 2005 / Published online: 13 January 2006
© Springer-Verlag 2006

## Abstract
This paper presents an efficient meshless method for analyzing cracked piezoelectric structures subjected to mechanical and electrical loading. In this method, an element free Galerkin (EFG) formulation, an enriched basic function and some special shape functions that contain discontinuous derivatives are employed. Based on the moving least squares (MLS) interpolation approach, the EFG method is one of the promising methods for dealing with problems involving progressive crack growth. Since the method is meshless and no element connectivity data are needed, the burdensome remeshing procedure required in the conventional finite element method (FEM) is avoided. The numerical results show that the proposed method can yield an accurate near-tip stress field in an infinite piezoelectric plate containing an interior hole. In another example studying a ceramic multilayer actuator, the proposed model was found to be accurate in the simulation of stress and electric field concentrations arround the abrupt end of an internal electrode.

**Keywords** Meshfree method · Ceramic multilayer actuator · Electro-mechanical coupling

---

The project supported by the National Natural Science Foundation of China (10025209, 10132010, and 90208002), and the Research Grants Council of the Hong Kong Special Administrative Region, China (HKU 7203/03E). The English text was polished by Yunming Chen.

X.H. Guo · D.N. Fang (☑)
Department of Engineering Mechanics,
Tsinghua University,
Beijing 100084, China
E-mail: fangdn@tsinghua.edu.cn

A.K. Soh
Department of Mechanical Engineering,
The University of Hong Kong,
Hong Kong, China

H.C. KIM · J.J. Lee
Department of Mechanical Engineering,
KAIST,
Taejon 305-701, Korea

---

## 1 Introduction
Piezoelectric materials are, due to their intrinsic electro-mechanical coupling, used in various applications, such as automotive actuators, sensors and transducers. However, because crack propagation is the main failure mechanism of piezoelectric when they are subjected to high electric fields, which often lead to the presence of high stress and high electric displacement, these applications require the materials have high reliability and the ability to withstand large strain. Therefore, many studies have been performed to understand the response of piezoelectric ceramics under electric field and mechanical loading. Kumar et al. [1] studied the stress distributions at the crack tip of a piezoelectric ceramic subjected to a combined mechanical and electrical loading. Based on the maximum stress criterion, the numerical results of Fang et al. [2] showed that crack propagation along the crack plane direction would be impeded if a negative electric field was applied, and it would tend to deviate at an angle of $84^\circ$ to the crack plane. Chen et al. [3] studied the effect of ferroelectric and ferroelastic switching on the magnitude of the field concentrations.

For many structures, crack propagation is a commonly encountered failure mechanism. So, an accurate and reliable numerical model is needed to predict its failure. An extensively used numerical method for fracture analysis is FEM. Based on a nonlinear, quasi-static eletro-mechanical coupled finite element method, Hom and Shankar [4] conducted some numerical analysis for multilayered, electrostrictive, ceramic actuators, including a single mutilayered actuator and an array of actuators embedded in a 2-2 composite. Using a linear and nonlinear model, Lucato and Lupascu et al. [5] investigated the initiation and propagation of cracks due to strain incompatibility between electrodes and piezoelectric materials in barium titanate and lead zirconate titanate (PZT) specimens. Moreover, the edge effect and specimen thickness effect were studied in their FEM model. Through Fourier transforms, Shindo and Narita et al. [6] obtained analytical resolutions of the displacement and electric potential in the vicinity of a surface electrode. By experimental

and numerical investigations of multilayer piezoelectric actuators, Shindo and Yoshida et al. [7] discussed electro-elastic field concentrations due to surface and internal elec-trodes. Gaudenzi and Bathe [8] made a summary of the FEM analysis for piezoelectric materials. Nevertheless, the FEM has its limitations in solving some mechanics problems in which the geometry of the domain changes are discontin-uous. In order to simulate the arbitrary and complex crack trajectories, a lot of remeshings of the finite element model have to be performed. Therefore, a considerable computa-tional effort is required for both remeshing the model and updating the nodal coordinates and crack trajectories. This pre- and post-processing of the finite element model often leads to degradation of numerical accuracy and complexity in computer programming.

In recent years, a large number of meshless or meshfree methods, such as diffuse elements [9], element-free Galerkin [10] and HP clouds EFMs [11], have been developed. These methods have demonstrated their effectiveness in solving extremely large deformation problems, high speed impact, phase switch and crack propagation. The element-free Galerkin method, a new numerical technique based on mov-ing least square interpolation, is one of the promising meth-ods for dealing with progressive crack growth. Although the integration elements do not connect strictly with interpo-lated nodes, it is prudent to mention that the EFG is not a truely "mesh-free" method since a set of background cells are needed to establish the solution equations. Atluri et al.[12] and De et al. [13] developed a truly meshless tech-nique, the meshless local Petrov-Galerkin (MLPG) method. This method has been successfully applied to a wide range of problems. Actually, by limiting quadrature to the nearby nodal points, the EFG can also be designed to be a truly meshless method, but this will lead to degradation in accu-racy, especially for non-convex domains. Therefore, unlike the conventional finite element method, the EFG does not require strict element connectivity data and does not subject to much degradation in accuracy when nodal arrangements are very irregular. This feature presents significant implica-tions for modeling fracture propagation due to the fact that the field is completely discretized by a set of nodes. Hence, the burdensome remeshing in FEM is avoided.

In this paper, the EFG method based on moving least square interpolation is employed to discretize the full field variables. By the penalty function method, the general dis-placement boundary conditions are imposed on the discrete equations. As a result, the stiffness matrix is sparse, sym-metric and positive-definite, hence the computational effort is reduced. For nonconvex bodies, such as holes and cracks, the discontinuous diffraction functions [14] are introduced as weight functions to satisfy the discontinuity of both the mechanical and electric displacements. Concurrently, some basis functions with singular terms are applied [15]. In addi-tion, nodal refinement is carried out around the crack tip. As a numerical example, an infinite plate with a central circular defect is simulated to verify the validity of our MLS approx-imation method. A good agreement between the numerical results and the existing theoretical solutions is achieved. In another example, only an external electric field is applied to a ceramic multilayer actuator. The concentrations of stress and electric fields can be determined for studying crack propaga-tions in the ceramic.

## 2 The principle of the moving least-squares approximation

In a general mesh-free approximation method, a discrete sys-tem is expressed completely in terms of the nodal values. Therefore, no predefined connectivity among nodes is estab-lished. In the entire domain, the displacement $\boldsymbol{u}^{h}(\boldsymbol{x})$ at any point $\boldsymbol{x}$ can be expressed as follows

$$
\boldsymbol{u}^{h}(\boldsymbol{x})=\boldsymbol{p}(\boldsymbol{x}) \boldsymbol{a}(\boldsymbol{x}),\qquad(1)
$$

where $\boldsymbol{p}(\boldsymbol{x})$ and $\boldsymbol{a}(\boldsymbol{x})$ are the vectors consisting of a complete basic function and the unknown coefficients which depend on $\boldsymbol{x}$, respectively. In this paper, $\boldsymbol{p}(\boldsymbol{x})$ is a linear basic function defined as follows

$$
\boldsymbol{p}(\boldsymbol{x})=[1, x, y].\qquad(2)
$$

In order to solve crack problems, and to ensure $1/\sqrt{r}$ singularity in linear elastic fracture mechanics, a partially or fully enriched basic function is employed, respectively, as follows

$$
\boldsymbol{p}(\boldsymbol{x})=[1, x, y, \sqrt{r}],\qquad(3)
$$

$$
\begin{gathered}
\boldsymbol{p}(\boldsymbol{x})=\left[1, x, y, \sqrt{r} \cos \frac{\theta}{2}, \sqrt{r} \sin \frac{\theta}{2}, \sqrt{r} \sin \frac{\theta}{2} \sin \theta,\right. \\
\left.\sqrt{r} \cos \frac{\theta}{2} \sin \theta\right],\qquad(4)
\end{gathered}
$$

where $r$ is the distance from the crack tip and $\theta$ is the angle from the tangent to the crack path at the crack tip.

We adopt the MLS method to determine the coefficient $\boldsymbol{a}(\boldsymbol{x})$. If the coordinates $\boldsymbol{x}_{I}$ and displacements $\boldsymbol{u}_{I}$ of $n$ nodes in the domain are known, the weighted residue can be expressed as

$$
J=\sum_{I=1}^{n} w\left(\boldsymbol{x}-\boldsymbol{x}_{I}\right)\left[\boldsymbol{p}(\boldsymbol{x}) \boldsymbol{a}(\boldsymbol{x})-\boldsymbol{u}_{I}\right]^{2},\qquad(5)
$$

where $w\left(\boldsymbol{x}-\boldsymbol{x}_{I}\right)$ is the weight function of node $I$ at point $\boldsymbol{x}$, $n$ is the number of nodes whose support domains include point $\boldsymbol{x}$, i.e., $w\left(\boldsymbol{x}-\boldsymbol{x}_{I}\right)>0$. $J$ reaches its minimum value when the derivative of $J$ with respect to $\boldsymbol{a}(\boldsymbol{x})$ equals zero. Therefore,

$$
\boldsymbol{A}(\boldsymbol{x}) \boldsymbol{a}(\boldsymbol{x})=\boldsymbol{B}(\boldsymbol{x}) \boldsymbol{u},\qquad(6)
$$

where

$$
\boldsymbol{A}(\boldsymbol{x})=\sum_{I=1}^{n} w\left(\boldsymbol{x}-\boldsymbol{x}_{I}\right) \boldsymbol{p}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{p}(\boldsymbol{x}),
$$

$$
\begin{gathered}
\boldsymbol{B}(\boldsymbol{x})=\left[w\left(\boldsymbol{x}-\boldsymbol{x}_{1}\right) \boldsymbol{p}\left(\boldsymbol{x}_{1}\right), w\left(\boldsymbol{x}-\boldsymbol{x}_{2}\right) \boldsymbol{p}\left(\boldsymbol{x}_{2}\right), \ldots,\right. \\
\left.w\left(\boldsymbol{x}-\boldsymbol{x}_{n}\right) \boldsymbol{p}\left(\boldsymbol{x}_{n}\right)\right],
\end{gathered}
$$

$$
\boldsymbol{u}=\left[\boldsymbol{u}_{1}, \boldsymbol{u}_{2}, \ldots, \boldsymbol{u}_{n}\right]. \tag{7}
$$

The matrix $\boldsymbol{A}(\boldsymbol{x})$ is often called the moment matrix. Solving Eq.(6), we can obtain
$$
\boldsymbol{a}(\boldsymbol{x})=\boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{B}(\boldsymbol{x}) \boldsymbol{u}. \tag{8}
$$

Substituting Eq.(8) into Eq.(1) yields the following equation:
$$
\begin{aligned}
\boldsymbol{u}^{h}(\boldsymbol{x}) &=\sum_{I=1}^{n} \boldsymbol{p}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{B}_{I}(\boldsymbol{x}) \boldsymbol{u}_{I} \\
&=\sum_{I=1}^{n} \phi_{I}(\boldsymbol{x}) \boldsymbol{u}_{I},
\end{aligned} \tag{9}
$$
where $\boldsymbol{B}_{I}(\boldsymbol{x})$ is the $I$th column of $\boldsymbol{B}(\boldsymbol{x})$, and
$$
\phi_{I}(\boldsymbol{x})=\boldsymbol{p}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{B}_{I}(\boldsymbol{x}), \tag{10}
$$
which is called the shape function. Its spatial derivatives can be expressed as
$$
\begin{aligned}
\phi_{I, i}(\boldsymbol{x})= & \boldsymbol{p}_{, i}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{B}_{I}(\boldsymbol{x}) \\
& +\boldsymbol{p}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{A}_{, i}^{-1}(\boldsymbol{x}) \boldsymbol{B}_{I}(\boldsymbol{x}) \\
& +\boldsymbol{p}^{\mathrm{T}}(\boldsymbol{x}) \boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{B}_{I, i}(\boldsymbol{x}),
\end{aligned} \tag{11}
$$
where $\boldsymbol{A}_{, i}^{-1}(\boldsymbol{x})=-\boldsymbol{A}^{-1}(\boldsymbol{x}) \boldsymbol{A}_{, i}(\boldsymbol{x}) \boldsymbol{A}^{-1}(\boldsymbol{x})$.

## 3 Formulation of electro-mechanical coupled EFG

The constitutive equations for piezoelectric materials are
$$
\boldsymbol{\sigma}=\boldsymbol{C}: \boldsymbol{\varepsilon}-\boldsymbol{e}^{\mathrm{T}} \cdot \boldsymbol{E}, \tag{12a}
$$
$$
\boldsymbol{D}=\boldsymbol{e}: \boldsymbol{\varepsilon}+\boldsymbol{d} \cdot \boldsymbol{E}, \tag{12b}
$$
where, $\boldsymbol{\sigma}, \boldsymbol{\varepsilon}, \boldsymbol{E}$ and $\boldsymbol{D}$ are the stress, strain, electric field and electric displacement tensors, respectively; and $\boldsymbol{C}, \boldsymbol{d}$ and $\boldsymbol{e}$ are the elastic, dielectric and piezoelectric constant tensors, respectively. For simplicity, all the numerical examples provided in this paper are treated as electro-mechanical coupled plane strain problems. Moreover, the materials, i.e., PZT ceramics, are assumed to be transversely isotropic. Thus, the constitutive equations (12) can be simplified (assume that $x_{3}$ is the poling direction and $x_{1}$-$x_{2}$ plane is the isotropic plane) as follows
$$
\boldsymbol{\sigma}^{\prime}=\boldsymbol{G} \cdot \boldsymbol{\varepsilon}^{\prime}, \tag{13}
$$
where
$$
\begin{gathered}
\boldsymbol{\sigma}^{\prime}=\left\{\begin{array}{c}
\sigma_{11} \\
\sigma_{33} \\
\sigma_{13} \\
D_{1} \\
D_{3}
\end{array}\right\}, \\
\boldsymbol{G}=\left[\begin{array}{ccccc}
C_{11} & C_{13} & 0 & 0 & e_{31} \\
C_{13} & C_{33} & 0 & 0 & e_{33} \\
0 & 0 & C_{44} & e_{15} & 0 \\
0 & 0 & e_{15} & -d_{11} & 0 \\
e_{31} & e_{33} & 0 & 0 & -d_{33}
\end{array}\right], \\
\boldsymbol{\varepsilon}^{\prime}=\left\{\begin{array}{c}
\varepsilon_{11} \\
\varepsilon_{33} \\
2 \varepsilon_{13} \\
-E_{1} \\
-E_{2}
\end{array}\right\}
\end{gathered} \tag{14}
$$
are the stress vector, stiffness matrix and strain vector, respectively. The total system potential in a domain $V$ with its boundary can be expressed as
$$
\begin{aligned}
\Pi= & \int_{V} \frac{1}{2} \boldsymbol{\varepsilon}^{\prime \mathrm{T}} \cdot \boldsymbol{G} \cdot \boldsymbol{\varepsilon}^{\prime} \mathrm{d} V-\int_{V} \boldsymbol{f}^{\prime} \cdot \boldsymbol{u}^{\prime} \mathrm{d} V \\
& -\int_{S^{\sigma}} \boldsymbol{T}^{\prime} \cdot \boldsymbol{u}^{\prime} \mathrm{d} S+\int_{S^{u}} \frac{1}{2} \alpha\left(\boldsymbol{u}^{\prime}-\overline{\boldsymbol{u}}^{\prime}\right) \mathrm{d} S,
\end{aligned} \tag{15}
$$
where $\boldsymbol{f}^{\prime}=\left[\boldsymbol{f} p^{e}\right]^{\mathrm{T}}, \boldsymbol{T}^{\prime}=\left[\boldsymbol{T} \bar{p}^{e}\right]^{\mathrm{T}}$ and $\boldsymbol{u}^{\prime}=[\boldsymbol{u} \phi]^{\mathrm{T}}$ are the body force, boundary force and displacement, respectively; and $\alpha$ is the penalty coefficient.

By applying the variational principle, the element-free Galekin formulation is obtained as follows
$$
\boldsymbol{K} \boldsymbol{u}^{\prime *}=\boldsymbol{f}^{\prime}, \tag{16}
$$
where $\boldsymbol{K}$ is made up of $3 \times 3$ matrix $\boldsymbol{k}_{I J}$, and $\boldsymbol{f}^{\prime}$ is made up of $3 \times 1$ matrix, $f_{I}$, respectively.

## 4 Numerical results

In order to examine the accuracy of the proposed electro-mechanical coupled EFG, an infinite poled piezoelectric plate with a circular hole subjected to both remotely applied positive electric field and tensile stress is studied. The corresponding analytical solution was obtained by Sosa [16] and Zhang [17]. The side length of the rectangle plate is ten times of the radius of the hole. In our analysis, the specimen is made of PZT-5H ceramic, and its material parameters are listed in Table 1. The material is initially poled in the Y-direction, and the plate is assumed to be in plane strain conditions. The bottom surface is grounded and an electric potential is applied on the top surface. The electric field, which is perturbed by the circular hole, is obtained between the top and bottom surfaces. The normalized stress and electric displacement distributions at the rim of the circular hole are illustrated in Figs. 1 and 2. A good agreement is obtained between the present numerical results and Sosa's analytical solution [16], i.e., the accuracy of the coupled electro-mechanical EFG is acceptable.

Piezoelectric ceramic multilayer actuators often consist of hundreds of ceramic layers, alternating with thin metal films, as shown in Fig. 3. A wide range of applications have been found in view of their small volumes, quick response, and large generated forces.

Owing to their symmetry, only half of an individual layer needs to be analyzed. The numerical model is illustrated in

Table 1 Material parameters of PZT-5H

<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Value</th>
    <th>Parameter</th>
    <th>Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$C_{11}$</td>
    <td>$12.6×10^{10}\mathrm{N/m^2}$</td>
    <td>$e_{31}$</td>
    <td>$-6.5\mathrm{C/m^2}$</td>
  </tr>
  <tr>
    <td>$C_{12}$</td>
    <td>$5.5×10^{10}\mathrm{N/m^2}$</td>
    <td>$e_{31}$</td>
    <td>$23.2\mathrm{C/m^2}$</td>
  </tr>
  <tr>
    <td>$C_{13}$</td>
    <td>$12.3×10^{10}\mathrm{N/m^2}$</td>
    <td>$e_{31}$</td>
    <td>$17.0\mathrm{C/m^2}$</td>
  </tr>
  <tr>
    <td>$C_{33}$</td>
    <td>$11.7×10^{10}\mathrm{N/m^2}$</td>
    <td>$\varepsilon_{11}$</td>
    <td>$151×10^{-10}\mathrm{C/Vm}$</td>
  </tr>
  <tr>
    <td>$C_{44}$</td>
    <td>$3.53×10^{10}\mathrm{N/m^2}$</td>
    <td>$\varepsilon_{33}$</td>
    <td>$130×10^{-10}\mathrm{C/Vm}$</td>
  </tr>
</tbody>
</table>

![](./images/812120677699026944_1.jpg)

Fig. 1 The distributions of the normalized stress on the rim of the hole

![](./images/812120677699026944_2.jpg)

Fig. 2 The distributions of the normalized hoop electric displacement on the rim of the hole

![](./images/812120677699026944_3.jpg)

Fig. 3 A schematic picture of a ceramic multilayer actuator

Fig. 4. An electric potential is applied to the lower electrode such that

$$
\phi(x, 0)=V_{\text {appl }}, \quad-L_{2} \leq x \leq 0, \tag{17}
$$

the vertical displacement and the shear stress vanish on both the electrode and on its front plane due to symmetry.

![](./images/812120677699026944_4.jpg)

Fig. 4 Configuration of the numerical model for a multilayer actuator

Therefore,

$$
v(x, 0)=0, \quad \sigma_{x y}=0, \quad-L_{2} \leq x \leq L_{1} \tag{18}
$$

and the vertical electric displacement in front of the plane of the lower electrode vanishes, i.e.,

$$
D_{y}(x, 0)=0, \quad 0<x<L_{1}. \tag{19}
$$

The upper electrode is grounded, therefore,

$$
\phi(x, H)=0, \tag{20}
$$

where $H$ is the thickness of the layer of piezoelectric ceramic, and the vertical displacement is constant, i.e.,

$$
v(x, H)=\text { constant. } \tag{21}
$$

The value of the constant is to be determined by iteration. When no external stresses are applied on the actuator, the shear stress and the vertical resultant force vanish, i.e.,

$$
\sigma_{x y}=0, \quad \int_{-L_{2}}^{L_{1}} \sigma_{y y}(x, H) \mathrm{d} x=0. \tag{22}
$$

On the vertical symmetric plane of the actuator, the tractions and horizontal electric displacement vanish, i.e.,

$$
\sigma_{x x}=0, \quad \sigma_{x y}=0, \quad D_{x}=0. \tag{23}
$$

At the right end of the actuator, the tractions vanish, and the end is grounded too, i.e.,

$$
\sigma_{x x}=0, \quad \sigma_{x y}=0, \quad \phi\left(L_{1}, y\right)=0. \tag{24}
$$

To avoid rigid body motion, the lower left corner is constrained in the $x$-direction, i.e.,

$$
u\left(-L_{2}, 0\right)=0. \tag{25}
$$

In the numerical calculations, we assume that $L_{1}=2 H$, $L_{2}=8 H$ and the applied electric field is $E_{\text {appl }}=0.72 E_{c}$, where $E_{c}=0.4 \mathrm{MV} / \mathrm{m}$ is the coercive electric field of PZT5H ceramic. In the mesh-free calculations, there are $80 \times 8$ integration cells which coincide with the uniform nodal arrangement, and $5 \times 5$ Gauss quadrature is used in each integration region. In order to properly describe the electric field and stress concentrations around the end of the lower electrode, five 4-node-rings are devised around the end of the electrode. Moreover, $9 \times 9$ Gauss quadrature is used in the refined region. Therefore, the total number of nodes employed in the model is 749.

With reference to Fig. 5, the electric field around the terminating electrode edge is non-uniform and much higher than the applied electric field. The electric field vector lies in the $x$-direction in front of the electrode edge, and lies in

![](./images/812120677699026944_5.jpg)

Fig. 5 The electric field distribution around the terminating internal electrode edge

![](./images/812120677699026944_6.jpg)

Fig. 6 The electric field distribution along the x-axis

the $y$-direction behind the electrode edge. In the region close to the end of the electrode, the electric field is very high, as shown in Fig. 6. However, the electric field in front of the electrode attenuates rapidly, even reduces to zero at some location; and it approaches the applied field behind the elec- trode edge. Therefore, the material around an electrode edge is subject to an incompatible deformation. This often induces a concentrated stress field that may lead to crack propagation, as shown in Fig. 7. Figure 8 illustrates the normalized stress, $\sigma_{y y} / \sigma_{c}$ ($\sigma_{c}=11$ MPa is the coercive stress), along the elec trode and in front of the electrode edge. The normal stress $\sigma_{y y}$ is negative in the electrode near the end, that is, the ce ramic near the end endures compressive stress. However, a considerable tensile stress is acting at the ceramic in front of the electrode edge. This implies that cracks may nucleate and propagate readily. In order to investigate what would happen when a crack nucleates in front of the electrode edge, a crack with the length of $2a=0.12H$ was introduced in front of the electrode tip. Figures 9 and 10 illustrate the distributions of $\sigma_{y y}$ around the crack. The result shown that the stress $\sigma_{y y}$ is compressive at the end of the crack and near the electrode tip, nevertheless, it is tensile at the other end of the crack. Moreover, the magnitude of compressive and tensile stress becomes larger when a crack nucleates in front of the elec- trode tip. This means that the crack will propagate along a straight line readily if only the stress $\sigma_{y y}$ is taken into account.

![](./images/812120677699026944_7.jpg)

Fig. 7 The distribution of stress $\sigma_{y y}$ (MPa) around the terminating elec trode edge

![](./images/812120677699026944_8.jpg)

Fig. 8 The normal stress distribution along the x-axis near the electrode edge

## 5 Conclusions

An efficient electro-mechanical coupled meshless method has been developed to analyze piezoelectric ceramic structures subjected to combined electrical and mechanical loadings. Our numerical examples show that by employing enriched basic functions, the element free Garlekin method is capa- ble of simulating the singularity of nonconvex regions, such as cavity and electrode edge. In the numerical example for the multilayer actuator, the trends of the electric field and stress distributions around the electrode edge are in over- all agreement with the analytical results of Gong et al. [18]. The discrepancy between the present results and those of Gong et al. is reasonable, in spite of the fact that they made the assumption that $L_{1}=L_{2} \gg H$. The proposed method is meshless, a structured mesh is not required. Instead, a scattered set of nodes is needed to discretize the domain of interest. In other words, no element connectivity data are needed. Therefore, element remeshing often required in the

![](./images/812120677699026944_9.jpg)

Fig. 9 The distribution of stress $\sigma_{yy}$ (MPa) around a crack in front of the terminating electrode edge

![](./images/812120677699026944_10.jpg)

Fig. 10 The normal stress distribution along the x-axis near a crack in front of the electrode edge

conventional finite element analysis is not necessary. How- ever, although the meshless method is convergent and accu- rate in dealing with crack problems, the inherent deficiency of meshless methods exists also in EFG. Because of the compli- cated non-polynomial functions, large efforts of matrix inver- sion and Gauss integration have to be made to compute the stiffness matrix and force vector. Although many researchers [19] have developed various techniques to alleviate the bur- den of excessive computations, considerable improvements of meshless method must be achieved before it has the same efficiency as the conventional finite element method.

### References

1. Kumar, S., Singh, R.N.: Effect of the mechanical boundary condi- tion at the crack surfaces on the stress distribution at the crack tip in piezoelectric materials. Mater. Sci. Eng. A252, 64-77 (1998)
2. Fang, D., Qi, H., Yao, Z.: Numerical analysis of crack propaga- tion in piezoelectric ceramics. Fat. Fract. Eng. Mater. Struct. 21,1371-1380 (1998)
3. Chen, W., Lynch, C.S.: Finite element analysis of cracks in ferro-electric ceramic materials. Eng. Fract. Mech. 64, 539-562 (1999)
4. Hom, C.L., Shankar, N.: A numerical analysis of relaxor ferroelec- tric multilayered actuators and 2-2 composite arrays. Smart Mater.Struct. 4, 305-317 (1995)
5. Dos Santos, E., Lucato, S.L., Lupascu, D.C., Kamlah, M., et al.: Constraint-induced crack initiation at electrode edges in piezoelec-tric ceramics. Acta Mater. 49, 2751-2759 (2001)
6. Shindo, Y., Narita, F., Sosa, H.: Electroelastic analysis of pie- zoelectric ceramics with surface electrodes. Int. J. Eng. Sci. 36,1001-1009 (1998)
7. Shindo, Y., Yoshida, M., Narita, F., Horiguchi, K.: Electroelastic field concentrations ahead of electrodes in multilayer piezoelectric actuators: experiment and finite element simulation. J. Mech. Phys.Solids 52, 1109-1124 (2004)
8. Gaudenzi, P., Bathe, K.J.: An Iterative finite element procedure for the analysis of piezoelectric continua. J. Intelligent MaterialSystems and Structures 2, 266-273 (1995)
9. Nayroles, B., Touzot, G., Villon, P.: Generalizing the finite ele- ment method: diffuse approximation and diffuse elements. Com-put. Mech. 10, 307-318 (1992)
10. Belytschko, T., Lu, Y.Y., Gu, L.: Element-free methods. Int. J. Num.Methods Eng. 37, 229-256 (1994)
11. Durate, C.A., Oden, J.T.: HP clouds-a meshless method to solve boundary-value problems. Technical Report 95-05, Texas Institute for Computational and Applied Mathematics, University of Texas at Austin
12. Atluri, S.N., Zhu, T.: A new meshless local Petrov-Galerkin(MLPG) approach in computational mechanics. Comput. Mech.22, 117-127 (1998)
13. De, S., Bathe, K.J.: The method of finite spheres. Comput. Mech.25, 329-345 (2000)
14. Belytschko, T., Flemming, M.: Smoothing, enrichment and contactin the element-free Galerkin method. Comput. Struct. 71, 173-195(1999)
15. Organ, D., Flemming, M., Terry, T., Belytschko, T.: Continuous meshless approximation for nonconvex bodies by diffraction andtransparency. Comput. Mech. 18, 1-11 (1996)
16. Sosa, H., Pak, Y.: Three dimensional eigenfunction analysis of acrack in a piezoelectric material. Int. J. Solids Struct. 26, 1-15(1990)
17. Zhang, T.Y., Qian, C.F., Tong, P.: Linear electro-elastic analysis of a cavity or acrack in a piezoelectric material. Int. J. Solids Struct.35, 2121-2149 (1998)
18. Gong, X., Suo, Z.: Reliability of ceramic multilayer actuators: a nonlinear finite element simulation. J. Mech. Phys. Solids 44,751-769 (1996)
19. Fleming, M., Chu, Y.A., Moran, B., Belytschko: Enriched element- free Galerkin methods for crack tip fields. Int. J. Num. MethodsEng. 40, 1483-1504 (1998)