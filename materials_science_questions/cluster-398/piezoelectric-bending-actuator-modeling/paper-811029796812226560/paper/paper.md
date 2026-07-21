![](./images/811029796812226560_1.jpg)

# The numerical analysis of piezoelectric ceramics based on the Hermite-type RPIM

Jichao Ma $^{a}$, Gaofeng Wei $^{a,*}$, Dandan Liu $^{b}$, Gongtian Liu $^{a}$

$^{a}$ School of Mechanical and Automotive Engineering, Qilu University of Technology, Jinan 250353, Shandong, People's Republic of China
$^{b}$ College of Foreign Languages, Shandong Normal University, Jinan 250358, Shandong, People's Republic of China

---

## ARTICLE INFO

**Keywords:**
Meshless methods
Piezoelectric ceramics
Radial point interpolation method
Numerical simulation

---

## ABSTRACT

In this paper, the Hermite-type radial point interpolation method (RPIM) is applied to analyze the property of piezoelectric ceramics in order to overcome the defects of finite element method. In this method, the inside and boundary of the problem domain are discreted by a distribution of nodes, and then the interpolation function of nodes are constructed to solve the displacement of the evaluation nodes. Compared with the finite element method, it is easier and faster for the Hermite-type RPIM to accurately achieve solution of the local regions. In contrast with the existing meshless methods, this method would not cause singularity in the process of evaluating the shape function. Furthermore, the shape function of the Hermite-type RPIM has a better stability and it can adapt to any distribution of nodes. In addition, the accuracy and stability of the method are proved by the numerical simulation.

© 2017 Elsevier Inc. All rights reserved.

---

## 1. Introduction

Piezoelectric ceramics have been used widely in sensors and actuators owing to its excellent performance, and it has played an important role in micro electro-mechanical systems and non-destructive testing.

In the piezoelectric ceramics, a voltage will be induced in the material when subjected to a mechanical deformation, which is known as the direct piezoelectric effect. Similarly, a strain will be generated if a voltage is applied across the material, which is known as the indirect piezoelectric effect. A lots of instruments have been designed based on the direct and indirect piezoelectric effect, such as pressure sensors [1], strain gauges, microphones, ultrasonic motors, accelerometers [2]; piezoelectric bender elements, linear extension elements, ultrasonic rotary motors [3].

In over half a century, the finite element method (FEM) has become a useful method to solve the engineering problems including complex structures and non-linear problems [4,5]. Besides, the FEM has been successfully used in the electromechanical coupling partial differential equations of the piezoelectric ceramics. Many studies have shown that the FEM can meet the requirements of accuracy and stability of solving the piezoelectric ceramics problems in engineering disciplines. However, the FEM needs much time and work to achieve the refinement of meshes for the situation, in which the local regions should be solved accurately for the complex structures.

Thus, the meshless methods have been put forward to overcome the problems mentioned above in the FEM [6–9]. The distinction between the meshless methods and the FEM is that the meshless methods use a series of appropriate scattered

* Corresponding author.
E-mail address: wgf@spu.edu.cn (G. Wei).

http://dx.doi.org/10.1016/j.amc.2017.03.045
0096-3003/© 2017 Elsevier Inc. All rights reserved.

nodes to express the problem domain and boundary, and construct the interpolation function to approximate the problem domain. The relation of connection among nodes is not necessary for the meshless methods. If we need to solve the local regions of problem domain accurately, only the number of the nodes should be increased. Clearly, it is easier to achieve, compared with the FEM.

In recent 20 years, the meshless methods have developed quickly. They mainly consist of the reproducing kernel particle method [10-12], the radial basis function method [13,14], the element-free Galerkin method [15-18], the finite point method [19,20], the partition of unity method [21,22], the polynomial point interpolation method [23,24], the moving least-squares method [25-27], the local Petrov-Galerkin method [28-31], the smooth particle hydrodynamics [32,33], the boundary inte- gral equation method [34,35], Hermite radial point interpolation method [36-38], and meshless manifold method [39-40].

Compared with the existing meshless methods, the Hermite-type RPIM has its own specific features: fast speed and high precision, so the piezoelectric ceramics can be analyzed by applying the Hermite-type RPIM. In this paper, the inside and boundary of the problem domain is discreted by a series of nodes, and the approximate displacement function of evaluation nodes are constructed by using the Hermite-type RPIM. The two corrected coefficients are introduced to make approximate displacement function close to exact displacement function, and the displacement of evaluation nodes are solved by the approximate displacement function. Additional nodes can be simply added to regions, if more accuracy is required. Finally, the examples are presented to demonstrate the accuracy and stability of the Hermite-type RPIM.

## 2. The governing equations of piezoelectric ceramics

In the $x-z$ plane, the two-dimensional piezoelectric ceramics constitutive equations can be expressed in two aspects of the stress and the electric field.

$$
\sigma_{p}=c_{p q}^{E} \varepsilon_{q}-e_{k q} E_{k} \tag{1}
$$

$$
D_{i}=e_{i q} \varepsilon_{q}+\xi_{i k}^{\varepsilon} E_{k} \tag{2}
$$

where $\varepsilon, \sigma, E_{k}$ and $D_{i}$ are the strain tensor, the stress tensor, the electric field vector and the electric displacement vector, respectively. $e, c^{E}$ and $\xi^{\varepsilon}$ are the piezoelectric constant, elastic stiffness, and dielectric constant, respectively. Superscript $\varepsilon$ and $E$ represent coefficients measured at constant electric field and stress, respectively.

The relationship between strains and displacements can be expressed as

$$
\varepsilon_{i j}=\frac{1}{2}\left(u_{i, j}+u_{j, i}\right) \tag{3}
$$

The condensed matrix between strain and displacement can be expressed as

$$
\varepsilon_{x}=\varepsilon_{x x}=u_{, x} \tag{4}
$$

$$
\varepsilon_{z}=\varepsilon_{z z}=w_{, z} \tag{5}
$$

$$
\gamma_{x z}=2 \varepsilon_{x z}=u_{, z}+w_{, x} \tag{6}
$$

where $u$ and $w$ are the displacements in the $x$ and $z$ directions, respectively. Commas followed by variables represent partial differentiation with the respect to variables.

The relationship between electric field and electric potential can be expressed as

$$
E_{i}=-\varphi_{, i} \tag{7}
$$

The governing equation of mechanical equilibrium equations is

$$
\sigma_{i j, j}=0 \tag{8}
$$

The governing equation of electrical equilibrium equations is

$$
D_{i, i}=0 \tag{9}
$$

The mechanical constitutive equations of the two-dimensional matrix form of piezoelectric ceramics is

$$
\left[\begin{array}{l}
\sigma_{x} \\
\sigma_{z} \\
\tau_{x z}
\end{array}\right]=\left[\begin{array}{ccc}
c_{11} & c_{13} & 0 \\
c_{13} & c_{33} & 0 \\
0 & 0 & c_{55}
\end{array}\right]\left[\begin{array}{l}
\varepsilon_{x} \\
\varepsilon_{z} \\
\gamma_{x z}
\end{array}\right]-\left[\begin{array}{cc}
0 & e_{31} \\
0 & e_{33} \\
e_{15} & 0
\end{array}\right]\left[\begin{array}{l}
E_{x} \\
E_{z}
\end{array}\right] \tag{10}
$$

The electrical constitutive equations of the two-dimensional matrix form of piezoelectric ceramics is

$$
\left[\begin{array}{l}
D_{x} \\
D_{z}
\end{array}\right]=\left[\begin{array}{ccc}
0 & 0 & e_{15} \\
e_{31} & e_{33} & 0
\end{array}\right]\left[\begin{array}{l}
\varepsilon_{x} \\
\varepsilon_{z} \\
\gamma_{x z}
\end{array}\right]+\left[\begin{array}{cc}
\xi_{11}^{\varepsilon} & 0 \\
0 & \xi_{33}^{\varepsilon}
\end{array}\right]\left[\begin{array}{l}
E_{x} \\
E_{z}
\end{array}\right] \tag{11}
$$

![](./images/811029796812226560_2.jpg)

Fig. 1. The supporting domain and distribution of nodes by applying the Hermite-type RPIM.

By substituting Eqs. (1), (2), (4)-(6) and (7) into equilibrium Eqs. (8) and (9), the equilibrium equations can be rewritten in terms of mechanical displacements and electric potential.

For two-dimensional piezoelectric ceramics, in the $x-z$ plane, the governing mechanical equilibrium equations are

$$
c_{11} u_{, x x}+c_{55} u_{, z z}+\left(c_{13}+c_{55}\right) w_{, x z}+\left(e_{31}+e_{15}\right) \varphi_{, x z}=0 \tag{12}
$$

$$
\left(c_{13}+c_{55}\right) u_{, x z}+c_{33} w_{, z z}+c_{55} w_{, x x}+e_{33} \varphi_{, z z}+e_{15} \varphi_{, x x}=0 \tag{13}
$$

The governing electrical equilibrium equations is

$$
\left(e_{31}+e_{15}\right) u_{, x z}+e_{15} w_{, x x}+e_{33} w_{, z z}-\xi_{11}^{\varepsilon} \varphi_{, x x}-\xi_{33}^{\varepsilon} \varphi_{, z z}=0 \tag{14}
$$

## 3. The approximate displacement function of piezoelectric ceramics constructed by the Hermite-type RPIM

In the $z$-direction, the approximate displacement function $w^{h}(x, z)$ can be expressed as the linear combination of RBFs (Racial Basis Function, constructed by $n$ nodes), normal derivative constructed by nodes of DBs (nodes on the interpolation function derivative condition) and $m$ polynomial functions in local supporting domain, as Fig. 1

$$
w^{h}(x, z)=\sum_{i=1}^{n} R_{i}(x, z) a_{i}+\sum_{j=1}^{n_{D B}} \frac{\partial R_{j}^{D B}(x, z)}{\partial \boldsymbol{n}} b_{j}+\sum_{k=1}^{m} p_{k}(x, z) c_{k} \tag{15}
$$

where $a_{i}, b_{j}$ and $c_{k}$ are undetermined coefficients; $n$ is the number of nodes in the local supporting domain (containing DB nodes); $n_{D B}$ are the number of DB nodes in the local supporting domain; $m$ are polynomial items; $p_{k}$ is monomial.

In Eq. (15) $R_{i}(x, z)$ expresses a class of functions whose values depend only on the distance between evaluation nodes $(x, z)$ and the nodes $\left(x_{i}, z_{i}\right), r_{i}=\sqrt{\left(x-x_{i}\right)^{2}+\left(z-z_{i}\right)^{2}}$

$$
R_{i}(x, z)=\left(r_{i}^{2}+\left(\alpha_{c} \cdot d_{c}\right)\right) \tag{16}
$$

In Eq. (15) $R_{j}(x, z)$ express a class of functions whose values depend only on the distance between evaluation nodes$(x, z)$ and the nodes $\left(x_{j}, z_{j}\right), r_{j}=\sqrt{\left(x-x_{j}\right)^{2}+\left(z-z_{j}\right)^{2}}$

$$
R_{j}^{D B}(x, z)=\exp \left[-\alpha_{c}\left(\frac{r_{j}}{d_{c}}\right)^{2}\right] \tag{17}
$$

$$
\frac{\partial R_{j}^{D B}(x, z)}{\partial \boldsymbol{n}}=l_{x j} \frac{\partial R_{j}^{D B}(x, z)}{\partial x}+l_{z j} \frac{\partial R_{j}^{D B}(x, z)}{\partial z} \tag{18}
$$

where $\boldsymbol{n}$ is boundary DB nodes the unit outward normal vector, $l_{x j}=\cos \left(n, x_{j}\right)$ and $l_{z j}=\cos \left(n, z_{j}\right)$ is direction cosine

$$
\mathbf{p}_{k}^{T}(x, z)=\left[\begin{array}{lllll}
1 & x & z & \ldots & p_{k}(x, z)
\end{array}\right] \tag{19}
$$

Eq. (15) can be rewritten into the matrix form

$$
w^{h}(x, z)=\mathbf{B}^{T} \mathbf{a}_{0} \tag{20}
$$

where the basis function vector $\mathbf{B}$ is

$$
\mathbf{B}^{T}=\left[\begin{array}{llllllllll}
R_{1} & \ldots & R_{n} & \frac{\partial R_{1}^{D B}}{\partial n} & \ldots & \frac{\partial R_{n_{D B}}^{D B}}{\partial n} & 1 & x & z & \ldots & p_{m}(x, z)
\end{array}\right] \tag{21}
$$

The coefficient vector $\mathbf{a}_{0}$ is

$$
\mathbf{a}_{0}^{T}=\left\{\begin{array}{lllllllllllll}
a_{1} & a_{2} & \ldots & a_{n} & b_{1} & b_{2} & \ldots & b_{D B} & c_{1} & c_{2} & \ldots & c_{m}
\end{array}\right\} \tag{22}
$$

In Eq. (15), coefficients $a_{i}$, $b_{j}$ and $c_{k}$can be obtained by all the function values of $n$ nodes and function derivative values of DB nodes in the supporting domain.

$w(x_{l},z_{l})$ can be got from all the $n$ nodes (containing DB nodes) in the supporting domain

$$
w\left(x_{l}, z_{l}\right)=\sum_{i=1}^{n} R_{i}\left(x_{l}, z_{l}\right) a_{i}+\sum_{j=1}^{n_{D B}} \frac{\partial R_{j}^{D B}\left(x_{l}, z_{l}\right)}{\partial n} b_{j}+\sum_{k=1}^{m} p_{k}\left(x_{l}, z_{l}\right) c_{k} \tag{23}
$$

where $l=1,2,...,n$, and $\frac{\partial w_{l}^{D B}}{\partial n}$ can be got as

$$
\frac{\partial w\left(x_{l}^{D B}, z_{l}^{D B}\right)}{\partial n}=\sum_{i=1}^{n} \frac{\partial R_{i}\left(x_{l}^{D B}, z_{l}^{D B}\right)}{\partial n} a_{i}+\sum_{j=1}^{n_{D B}} \frac{\partial^{2} R_{j}^{D B}\left(x_{l}^{D B}, z_{l}^{D B}\right)}{\partial n^{2}} b_{j}+\sum_{k=1}^{m} \frac{\partial p_{k}\left(x_{l}^{D B}, z_{l}^{D B}\right)}{\partial n} c_{k} \tag{24}
$$

where $l=1,2,...,n_{DB}$.

The only solution can be given by applying constraint to the polynomial

$$
\sum_{i=1}^{n} p_{k}\left(x_{i}, z_{i}\right) a_{i}+\sum_{j=1}^{n_{D B}} p_{k}\left(x_{j}, z_{j}\right)=0 \tag{25}
$$

where $k=1,2,...,m$, simultaneous Eqs. (23)-(25), the matrix equation can be got as

$$
\mathbf{W}_{s}=\left\{\begin{array}{c}
w\left(x_{l}, z_{l}\right) \\
\frac{\partial w\left(x_{l}^{D B}, z_{l}^{D B}\right)}{\partial n} \\
0
\end{array}\right\}=\left[\begin{array}{ccc}
\mathbf{R}_{0} & \mathbf{R}_{D B 1} & \mathbf{P}_{m 1} \\
\mathbf{R}_{D B 2} & \mathbf{R}_{c} & \mathbf{P}_{D B} \\
\mathbf{P}_{m 1}^{T} & \mathbf{P}_{m 2}^{T} & 0
\end{array}\right]\left\{\begin{array}{l}
a \\
b \\
c
\end{array}\right\}=\mathbf{G a}_{0} \tag{26}
$$

where $\mathbf{G}$ is generalized torque matrix which is constituted by polynomial torque matrix of $n$ nodes

$$
\mathbf{P}_{m 1}^{T}=\left[\begin{array}{cccc}
p_{1}\left(x_{1}, z_{1}\right) & p_{1}\left(x_{2}, z_{2}\right) & \cdots & p_{1}\left(x_{n}, z_{n}\right) \\
p_{2}\left(x_{1}, z_{1}\right) & p_{2}\left(x_{2}, z_{2}\right) & \cdots & p_{2}\left(x_{n}, z_{n}\right) \\
\vdots & \vdots & \ddots & \vdots \\
p_{m}\left(x_{1}, z_{1}\right) & p_{m}\left(x_{2}, z_{2}\right) & \cdots & p_{m}\left(x_{n}, z_{n}\right)
\end{array}\right]_{(m \times n)} \tag{27}
$$

$$
\mathbf{P}_{m 2}^{T}=\left[\begin{array}{cccc}
p_{1}\left(x_{1}, z_{1}\right) & p_{1}\left(x_{2}, z_{2}\right) & \cdots & p_{1}\left(x_{n_{D B}}, z_{n_{D B}}\right) \\
p_{2}\left(x_{1}, z_{1}\right) & p_{2}\left(x_{2}, z_{2}\right) & \cdots & p_{2}\left(x_{n_{D B}}, z_{n_{D B}}\right) \\
\vdots & \vdots & \ddots & \vdots \\
p_{m}\left(x_{1}, z_{1}\right) & p_{m}\left(x_{2}, z_{2}\right) & \cdots & p_{m}\left(x_{n_{D B}}, z_{n_{D B}}\right)
\end{array}\right]_{\left(m \times n_{D B}\right)} \tag{28}
$$

The first-order polynomial derivative value of the torque matrix in $n_{D B}$ nodes is

$$
\mathbf{P}_{D B}=\left[\begin{array}{cccc}
\frac{\partial p_{1}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} & \frac{\partial p_{2}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} & \ldots & \frac{\partial p_{m}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} \\
\frac{\partial p_{1}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} & \frac{\partial p_{2}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} & \ldots & \frac{\partial p_{m}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial p_{1}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n} & \frac{\partial p_{2}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n} & \ldots & \frac{\partial p_{m}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n}
\end{array}\right]_{\left(n_{D B} \times m\right)} \tag{29}
$$

The RBFs torque matrix of $n$ nodes is

$$
\mathbf{R}_{0}=\left[\begin{array}{cccc}
R_{1}\left(x_{1}, z_{1}\right) & R_{2}\left(x_{1}, z_{1}\right) & \cdots & R_{n}\left(x_{1}, z_{1}\right) \\
R_{1}\left(x_{2}, z_{2}\right) & R_{2}\left(x_{2}, z_{2}\right) & \cdots & R_{n}\left(x_{2}, z_{2}\right) \\
\vdots & \vdots & \ddots & \vdots \\
R_{1}\left(x_{n}, z_{n}\right) & R_{2}\left(x_{n}, z_{n}\right) & \cdots & R_{n}\left(x_{n}, z_{n}\right)
\end{array}\right]_{(n \times n)}
$$

(30)

The first-order RBFs derivative values of torque matrix in DB nodes is

$$
\mathbf{R}_{D B 1}=\left[\begin{array}{cccc}
\frac{\partial R_{1}^{D B}\left(x_{1}, z_{1}\right)}{\partial n} & \frac{\partial R_{2}^{D B}\left(x_{1}, z_{1}\right)}{\partial n} & \cdots & \frac{\partial R_{n_{D B}}^{D B}\left(x_{1}, z_{1}\right)}{\partial n} \\
\frac{\partial R_{1}^{D B}\left(x_{2}, z_{2}\right)}{\partial n} & \frac{\partial R_{2}^{D B}\left(x_{2}, z_{2}\right)}{\partial n} & \cdots & \frac{\partial R_{n_{D B}}^{D B}\left(x_{2}, z_{2}\right)}{\partial n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial R_{1}^{D B}\left(x_{n}, z_{n}\right)}{\partial n} & \frac{\partial R_{2}^{D B}\left(x_{n}, z_{n}\right)}{\partial n} & \cdots & \frac{\partial R_{n_{D B}}^{D B}\left(x_{n}, z_{n}\right)}{\partial n}
\end{array}\right]_{\left(n \times n_{D B}\right)}
$$

(31)

$$
\mathbf{R}_{D B 2}=\left[\begin{array}{cccc}
\frac{\partial R_{1}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} & \frac{\partial R_{2}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} & \cdots & \frac{\partial R_{n}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n} \\
\frac{\partial R_{1}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} & \frac{\partial R_{2}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} & \cdots & \frac{\partial R_{n}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial R_{1}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n} & \frac{\partial R_{2}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n} & \cdots & \frac{\partial R_{n}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n}
\end{array}\right]_{\left(n_{D B} \times n\right)}
$$

(32)

The second-order RBFs derivative values of torque matrix in DB nodes is

$$
\mathbf{R}_{c}=\left[\begin{array}{cccc}
\frac{\partial}{\partial n}\left(\frac{\partial R_{1}^{D B}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n}\right) & \frac{\partial}{\partial n}\left(\frac{\partial R_{2}^{D B}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n}\right) & \cdots & \frac{\partial}{\partial n}\left(\frac{\partial R_{n_{D B}}^{D B}\left(x_{1}^{D B}, z_{1}^{D B}\right)}{\partial n}\right) \\
\frac{\partial}{\partial n}\left(\frac{\partial R_{1}^{D B}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n}\right) & \frac{\partial}{\partial n}\left(\frac{\partial R_{2}^{D B}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n}\right) & \cdots & \frac{\partial}{\partial n}\left(\frac{\partial R_{n_{D B}}^{D B}\left(x_{2}^{D B}, z_{2}^{D B}\right)}{\partial n}\right) \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial}{\partial n}\left(\frac{\partial R_{1}^{D B}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n}\right) & \frac{\partial}{\partial n}\left(\frac{\partial R_{2}^{D B}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n}\right) & \cdots & \frac{\partial}{\partial n}\left(\frac{\partial R_{n_{D B}}^{D B}\left(x_{n_{D B}}^{D B}, z_{n_{D B}}^{D B}\right)}{\partial n}\right)
\end{array}\right]_{\left(n_{D B} \times n_{D B}\right)}
$$

(33)

In Eq. (26), $\mathbf{G}$ is inverse matrix, so $\mathbf{a}_{0}$ can be got

$$
\mathbf{a}_{0}=\mathbf{G}^{-1} \mathbf{W}_{s}
$$

(34)

Substituting Eq. (34) into Eq. (20), we can get

$$
w^{h}(x, z)=\mathbf{B}^{T} \mathbf{a}_{0}=\mathbf{B}^{T} \mathbf{G}^{-1} \mathbf{W}_{s}=\boldsymbol{\Phi}^{T} \mathbf{W}_{s}
$$

(35)

where $\boldsymbol{\Phi}$ is a matrix of the approximate function defined by the following formula

$$
\boldsymbol{\Phi}^{T}=\mathbf{B}^{T} \mathbf{G}^{-1}=\left[\begin{array}{llllllllll}
\phi_{1} & \phi_{2} & \cdots & \phi_{n} & \phi_{1}^{H} & \cdots & \phi_{n_{D B}}^{H} & \phi_{1}^{p} & \cdots & \phi_{m}^{p}
\end{array}\right]_{\left(n+n_{D B}+m\right) \times 1}
$$

(36)

## 4. Correction of approximate function

Substituting Eq.(36) into Eq.(35), the detailed expression of the approximate function can be written as

$$
w^{h}(x, z)=\sum_{i=1}^{n} \phi_{i} w_{i}+\sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial w_{n_{D B}}^{D B}}{\partial n}
$$

(37)

In order to improve the accuracy of Eq.(37), the two corrected coefficients of $\mu$, $\eta$ are introduced to make approximate displacement function close to exact displacement function. Eq.(37) can be rewritten as the form of the interpolation

function and its derivative

$$
\begin{aligned}
\tilde{w}^{h}(x, z) & =\mu \sum_{i=1}^{n} \phi_{i} w_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial w_{j}^{D B}}{\partial n} \\
& =\left[\begin{array}{lllllll}
\mu \phi_{1} & \mu \phi_{2} & \cdots & \mu \phi_{n} & \eta \phi_{1}^{H} & \eta \phi_{2}^{H} & \cdots & \eta \phi_{n_{D B}}^{H}
\end{array}\right]\left[\begin{array}{c}
w_{1} \\
w_{2} \\
\vdots \\
w_{n} \\
\frac{\partial w_{1}^{D B}}{\partial n} \\
\frac{\partial w_{2}^{D B}}{\partial n} \\
\vdots \\
\frac{\partial w_{n_{D B}}^{D B}}{\partial n}
\end{array}\right]=\mathbf{N} \hat{\mathbf{w}}
\end{aligned}
$$

### 4.1. Boundary conditions applying to the piezoelectric ceramics

Approximate functions should satisfy boundary condition equations, and nodes on the boundary should satisfy the Neumann boundary condition.

The nodes located on the boundary should satisfy approximations of the mechanical boundary conditions

$$
\begin{aligned}
\sigma_{x}=0 \Rightarrow & c_{11}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{13}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{31}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)=0
\end{aligned}
$$

$$
\begin{aligned}
\sigma_{z}=0 \Rightarrow & c_{13}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{33}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{33}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)=0
\end{aligned}
$$

$$
\begin{aligned}
\tau_{x z}=0 \Rightarrow & c_{55}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{55}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{15}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)=0
\end{aligned}
$$

$$
u=0 \Rightarrow \mu \sum_{i=1}^{n} \phi_{i} u_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial u_{j}^{D B}}{\partial n}=0
$$

$$
w=0 \Rightarrow \mu \sum_{i=1}^{n} \phi_{i} w_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial w_{j}^{D B}}{\partial n}=0
$$

The nodes located on the boundary satisfy approximations of the electrical boundary conditions

$$
\varphi_{, x}=0 \Rightarrow \mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial \varphi_{j}^{D B}}{\partial n}=0
$$

$$
\varphi=V \Rightarrow \mu \sum_{i=1}^{n} \phi_{i} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial \varphi_{j}^{D B}}{\partial n}=V
$$

### 4.2. The weighted least-squares formulation for piezoelectric ceramics

The weighted residual method is an effective method to solve ordinary differential equations or partial differential equation interpolation function. Many numerical methods are based on the weighted residual method. In this paper, the weighted least square method is used to solve governing equations.

Residual functions in the problem domain are

$$
R_{S 1}=c_{11} u_{, x x}+c_{55} u_{, z z}+\left(c_{13}+c_{55}\right) w_{, x z}+\left(e_{31}+e_{15}\right) \varphi_{, x z} \tag{46}
$$

$$
R_{S 2}=\left(c_{13}+c_{55}\right) u_{, x z}+c_{33} w_{, z z}+c_{55} w_{, x x}+e_{33} \varphi_{, z z}+e_{15} \varphi_{, x x} \tag{47}
$$

$$
R_{S 3}=\left(e_{31}+e_{15}\right) u_{, x z}+e_{15} w_{, x x}+e_{33} w_{, z z}-\xi_{11}^{\varepsilon} \varphi_{, x x}-\xi_{33}^{\varepsilon} \varphi_{, z z}=0 \tag{48}
$$

Residual functions in the boundary condition are

$$
\begin{aligned}
R_{b 1}= & c_{11}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{13}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{31}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)
\end{aligned} \tag{49}
$$

$$
\begin{aligned}
R_{b 2}= & c_{13}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{33}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{33}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)
\end{aligned} \tag{50}
$$

$$
\begin{aligned}
R_{b 3}= & c_{55}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial z} u_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial z} \frac{\partial u_{j}^{D B}}{\partial n}\right)+c_{55}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} w_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial w_{j}^{D B}}{\partial n}\right) \\
& +e_{15}\left(\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial \varphi_{j}^{D B}}{\partial n}\right)
\end{aligned} \tag{51}
$$

$$
R_{b 4}=\mu \sum_{i=1}^{n} \phi_{i} u_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial u_{j}^{D B}}{\partial n} \tag{52}
$$

$$
R_{b 5}=\mu \sum_{i=1}^{n} \phi_{i} w_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial w_{j}^{D B}}{\partial n} \tag{53}
$$

$$
R_{b 6}=\mu \sum_{i=1}^{n} \frac{\partial \phi_{i}}{\partial x} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \frac{\partial \phi_{j}^{H}}{\partial x} \frac{\partial \varphi_{j}^{D B}}{\partial n} \tag{54}
$$

$$
R_{b 7}=\mu \sum_{i=1}^{n} \phi_{i} \varphi_{i}+\eta \sum_{j=1}^{n_{D B}} \phi_{j}^{H} \frac{\partial \varphi_{j}^{D B}}{\partial n}-V \tag{55}
$$

Then the following weighted integral of all residuals $R_{S}$ and $R_{b}$ for all nodes can be obtained in the weighted least square method

$$
J_{1}=\int_{\Omega} R_{S 1}^{T} R_{S 1} d \Omega+\int_{\Omega} R_{S 2}^{T} R_{S 2} d \Omega+\int_{\Omega} R_{S 3}^{T} R_{S 3} d \Omega \tag{56}
$$

$$
\begin{aligned}
J_{2}= & \int_{\Gamma_{1}} R_{b 1}^{T} R_{b 1} d \Gamma_{1}+\int_{\Gamma_{2}} R_{b 2}^{T} R_{b 2} d \Gamma_{2}+\int_{\Gamma_{3}} R_{b 3}^{T} R_{b 3} d \Gamma_{3}+\int_{\Gamma_{4}} R_{b 4}^{T} R_{b 4} d \Gamma_{4}+\int_{\Gamma_{5}} R_{b 5}^{T} R_{b 5} d \Gamma_{5} \\
& +\int_{\Gamma_{6}} R_{b 6}^{T} R_{b 6} d \Gamma_{6}+\int_{\Gamma_{7}} R_{b 7}^{T} R_{b 7} d \Gamma_{7}
\end{aligned} \tag{57}
$$

where $J_1$ is minimizing the function in problem domain, $J_2$ is minimizing the function in the boundary.

By minimizing the function $J_1$ in Eq. (56), substituting Eq. (56) into Eqs. (58) and (59)

$$
W_{1}=\frac{\partial J_{1}}{\partial \mu} \tag{58}
$$

$$
W_{2}=\frac{\partial J_{1}}{\partial \eta} \tag{59}
$$

By minimizing the functional $J_2$ in Eq. (57), substituting Eq. (57) into Eqs. (60) and (61)

$$
V_{1}=\frac{\partial J_{2}}{\partial \mu} \tag{60}
$$

$$
V_{2}=\frac{\partial J_{2}}{\partial \eta} \tag{61}
$$

Then substituting weight functions $W_i$ and $V_i$ into Eq. (62), we can get

$$
\int_{\Omega} W_{i} R_{s} d \Omega+\int_{\Gamma} V_{i} R_{b} d \Gamma=0 \tag{62}
$$

where $i=1,2$

Then coefficient $\mu$ and $\eta$ can be got. Finally, the governing equations matrix form of the piezoelectric ceramics can be deduced by the Hermite-type RPIM.

$$
\left[\begin{array}{lll}
\mathbf{K}_{u u} & \mathbf{K}_{u w} & \mathbf{K}_{u \varphi} \\
\mathbf{K}_{w u} & \mathbf{K}_{w w} & \mathbf{K}_{w \varphi} \\
\mathbf{K}_{\varphi u} & \mathbf{K}_{\varphi w} & \mathbf{K}_{\varphi \varphi}
\end{array}\right]\left[\begin{array}{c}
\hat{\mathbf{u}} \\
\hat{\mathbf{w}} \\
\hat{\varphi}
\end{array}\right]=\left[\begin{array}{c}
\mathbf{F}_{u} \\
\mathbf{F}_{w} \\
\mathbf{F}_{\varphi}
\end{array}\right] \tag{63}
$$

In the $x$-direction, the mechanical equilibrium equations are

$$
\mathbf{K}_{u u}=c_{11} \mathbf{N}_{, x x}+c_{55} \mathbf{N}_{, z z} \tag{64}
$$

$$
\mathbf{K}_{u w}=\left(c_{13}+c_{55}\right) \mathbf{N}_{, x z} \tag{65}
$$

$$
\mathbf{K}_{u \varphi}=\left(e_{31}+e_{15}\right) \mathbf{N}_{, x z} \tag{66}
$$

$$
\mathbf{F}_{u}=0 \tag{67}
$$

In the $z$-direction, the mechanical equilibrium equations are

$$
\mathbf{K}_{w u}=\left(c_{13}+c_{55}\right) \mathbf{N}_{, x z} \tag{68}
$$

$$
\mathbf{K}_{w w}=c_{33} \mathbf{N}_{, z z}+c_{55} \mathbf{N}_{, x x} \tag{69}
$$

$$
\mathbf{K}_{w \varphi}=e_{33} \mathbf{N}_{, z z}+e_{15} \mathbf{N}_{, x x} \tag{70}
$$

$$
\mathbf{F}_{w}=0 \tag{71}
$$

Electrical equilibrium equations are

$$
\mathbf{K}_{\varphi u}=\left(e_{33}+e_{15}\right) \mathbf{N}_{, x z} \tag{72}
$$

$$
\mathbf{K}_{\varphi w}=e_{15} \mathbf{N}_{, x x}+e_{33} \mathbf{N}_{, z z} \tag{73}
$$

$$
\mathbf{K}_{\varphi \varphi}=-\xi_{11}^{\varepsilon} \mathbf{N}_{, x x}-\xi_{33}^{\varepsilon} \mathbf{N}_{, z z} \tag{74}
$$

$$
\mathbf{F}_{\varphi}=0 \tag{75}
$$

![](./images/811029796812226560_3.jpg)

Fig. 2. The state of parallel bimorphs.

<table>
<caption>Table 1<br>The properties of PVDP.</caption>
<thead>
<tr>
<th>$c_{11}$</th>
<th>$2.18\ e-3\frac{N}{\mu m^{2}}$</th>
<th>$e_{31}$</th>
<th>$4.6\ e-8\frac{N}{V\mu m}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$c_{13}$</td>
<td>$6.33\ e-4\frac{N}{\mu m^{2}}$</td>
<td>$e_{33}$</td>
<td>$4.6\ e-8\frac{N}{V\mu m}$</td>
</tr>
<tr>
<td>$c_{33}$</td>
<td>$2.18-3\frac{N}{\mu m^{2}}$</td>
<td>$\xi_{11}^{\varepsilon}$</td>
<td>$1.062\ e-10\frac{N}{V^{2}}$</td>
</tr>
<tr>
<td>$c_{55}$</td>
<td>$7.75\ e-4\frac{N}{\mu m^{2}}$</td>
<td>$\xi_{33}^{\varepsilon}$</td>
<td>$1.062\ e-10\frac{N}{V^{2}}$</td>
</tr>
</tbody>
</table>

![](./images/811029796812226560_4.jpg)

Fig. 3. The displacements of bimorph nodes under the voltage.

## 5. Numerical examples

### 5.1. Mechanical deformation of the bimorph with 1 V

A $10\times1\mathrm{\mu m}(L=10\mathrm{\mu m},2h=1\mathrm{\mu m})$ bimorph made of PVDF is taken as an example to analyze the displacements, as Fig 2. The bimorph is divided into the top and bottom layers, and each layer is represented by nodes. Nodes lying on the interface are placed to coincide with the adjoining nodes on the other side. After discreteting the problem domain by nodes, the approximate function are constructed by applying the Hermite-type RPIM.

The following boundary conditions apply to the top layer

$$
\begin{align*}
\varphi^{(1)}(x,z=0) &= V & \sigma_{z}^{(1)}(x,z=0) &= 0 & \tau_{xz}^{(1)}(x,z=0) &= 0 \\
\varphi(1)(x,z=h) &= 0 & \sigma_{z}^{(1)}(x,z=h) &= \sigma_{z}^{(2)}(x,z=h) \\
\tau_{xz}^{(1)}(x,z=h) &= \tau_{xz}^{(2)}(x,z=h) \\
\varphi_{,x}^{(1)}(x=0,z) &= 0 & u^{(1)}(x=0,z) &= 0 & w^{(1)}(x=0,z) &= 0 \\
\varphi_{,x}^{(1)}(x=L,z) &= 0 & \sigma_{x}^{(1)}(x=L,z) &= 0 & \tau_{xz}^{(1)}(x=L,z) &= 0
\end{align*}
$$

<table>
<caption>Table 2
The comparison of the w-displacements for the FEM and the Hermite-type RPIM.</caption>
<thead>
<tr>
<th>Coordinate (μm)</th>
<th>The displacements
of the FEM (μm)</th>
<th>The displacements of the
Hermite-type RPIM (μm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>(0.00,0.00)</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>(1.00,0.00)</td>
<td>0.049</td>
<td>0.046</td>
</tr>
<tr>
<td>(2.00,0.00)</td>
<td>0.213</td>
<td>0.201</td>
</tr>
<tr>
<td>(3.00,0.00)</td>
<td>0.398</td>
<td>0.374</td>
</tr>
<tr>
<td>(4.00,0.00)</td>
<td>0.725</td>
<td>0.688</td>
</tr>
<tr>
<td>(5.00,0.00)</td>
<td>1.255</td>
<td>1.167</td>
</tr>
<tr>
<td>(6.00,0.00)</td>
<td>1.753</td>
<td>1.647</td>
</tr>
<tr>
<td>(7.00,0.00)</td>
<td>2.398</td>
<td>2.254</td>
</tr>
<tr>
<td>(8.00,0.00)</td>
<td>3.222</td>
<td>2.996</td>
</tr>
<tr>
<td>(9.00,0.00)</td>
<td>3.921</td>
<td>3.685</td>
</tr>
<tr>
<td>(10.00,0.00)</td>
<td>4.859</td>
<td>4.616</td>
</tr>
<tr>
<td>(0.00,0.50)</td>
<td>0.500</td>
<td>0.500</td>
</tr>
<tr>
<td>(1.00,0.50)</td>
<td>0.539</td>
<td>0.501</td>
</tr>
<tr>
<td>(2.00,0.50)</td>
<td>0.723</td>
<td>0.679</td>
</tr>
<tr>
<td>(3.00,0.50)</td>
<td>0.898</td>
<td>0.835</td>
</tr>
<tr>
<td>(4.00,0.50)</td>
<td>1.235</td>
<td>1.173</td>
</tr>
<tr>
<td>(5.00,0.50)</td>
<td>1.775</td>
<td>1.739</td>
</tr>
<tr>
<td>(6.00,0.50)</td>
<td>2.273</td>
<td>2.273</td>
</tr>
<tr>
<td>(7.00,0.50)</td>
<td>2.928</td>
<td>3.015</td>
</tr>
<tr>
<td>(8.00,0.50)</td>
<td>3.742</td>
<td>3.854</td>
</tr>
<tr>
<td>(9.00,0.50)</td>
<td>4.471</td>
<td>4.649</td>
</tr>
<tr>
<td>(10.00,0.50)</td>
<td>5.449</td>
<td>5.666</td>
</tr>
<tr>
<td>(0.00,1.00)</td>
<td>1.000</td>
<td>1.000</td>
</tr>
<tr>
<td>(1.00,1.00)</td>
<td>1.149</td>
<td>1.217</td>
</tr>
<tr>
<td>(2.00,1.00)</td>
<td>1.333</td>
<td>1.399</td>
</tr>
<tr>
<td>(3.00,1.00)</td>
<td>1.548</td>
<td>1.625</td>
</tr>
<tr>
<td>(4.00,1.00)</td>
<td>1.875</td>
<td>1.987</td>
</tr>
<tr>
<td>(5.00,1.00)</td>
<td>2.425</td>
<td>2.546</td>
</tr>
<tr>
<td>(6.00,1.00)</td>
<td>2.903</td>
<td>3.048</td>
</tr>
<tr>
<td>(7.00,1.00)</td>
<td>3.588</td>
<td>3.803</td>
</tr>
<tr>
<td>(8.00,1.00)</td>
<td>4.412</td>
<td>4.633</td>
</tr>
<tr>
<td>(9.00,1.00)</td>
<td>5.143</td>
<td>5.348</td>
</tr>
<tr>
<td>(10.00,1.00)</td>
<td>6.081</td>
<td>6.385</td>
</tr>
</tbody>
</table>

Boundary conditions for the bottom layer are

$$
\begin{aligned}
& \varphi^{(2)}(x, z=h)=\varphi^{(1)}(x, z=h) & u^{(2)}(x, z=h)=u^{(1)}(x, z=h) \\
& w^{(2)}(x, z=h)=w^{(1)}(x, z=h) & \\
& \varphi^{(2)}(x, z=2 h)=V & \sigma_{z}^{(2)}(x, z=2 h)=0 \\
& \tau_{x z}^{(2)}(x, z=2 h)=0 & \\
& \varphi_{, x}^{(2)}(x=0, z)=0 & u^{(2)}(x=0, z)=0 \quad w^{(2)}(x=0, z)=0 \\
& \varphi_{, x}^{(2)}(x=L, z)=0 & \sigma_{x}^{(2)}(x=L, z)=0 \quad \tau_{x z}^{(2)}(x=L, z)=0
\end{aligned}
$$

The properties of PVDF are shown in Table 1. The displacements of the bimorph are shown when the 1 V voltage is applied, in Fig 3.

The displacements of the bimorph are exhibited in Table 2. The relative maximum error between this method and the FEM is 0.07, which shows that the calculations of the FEM and the Hermite-type RPIM are approximate.

### 5.2. The displacement of bimorph under different voltages

A device, which consists of two parallel bimorphs and a piece of mirror shown as Fig 4, is designed to prove the accuracy of the method in this paper. Both of the bimorphs are $10 \times 1$ μm respectively, the center of the two bimorphs is connected by a $1$ μm length mirror. When the voltages are applied, the two bimorphs will deflect in adverse direction, then produce a tilt angle-$θ$ and make the tip from $A$ to $A'$, as shown in Fig. 5. Through changing the applied voltages, the reflected light of the mirror can be changed. The displacements of the tip can be tested under different voltages. The tilt angle of the mirror determines the displacements of the tip. The displacements of the tip are shown in Fig. 6. The mirror is assumed to conform to linear elastic equation, and the tilt angle of the device for different applied voltages is summarized in Table 3. The relative maximum error between the measured displacement and the Hermite-type RPIM is 0.06. The relative maximum error between the measured displacement and the local Petrov–Galerkin method is 0.09. The results show that the Hermite-type RPIM is more correct and effective than local Petrov–Galerkin method.

![](./images/811029796812226560_5.jpg)

Fig. 4. The initial status of the bimorph.

![](./images/811029796812226560_6.jpg)

Fig. 5. The status change of the bimorph under different voltages.

![](./images/811029796812226560_7.jpg)

Fig. 6. Tip displacements of the bimorph under different voltages.

Table 3
Measured displacements, the displacements of local Petrov-Galerkin method [28] and the Hermite-type RPIM under different voltages.

<table>
<thead>
<tr>
<th>Applied voltage (V)</th>
<th>Tilt angles ($\theta$)</th>
<th>Measured displacements ($\mu$m)</th>
<th>Hermite-type RPIM displacements ($\mu$m)</th>
<th>Local Petrov-Galerkin method displacements ($\mu$m)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>1.00</td>
<td>0.566</td>
<td>2.398E$-$03</td>
<td>2.326E$-$03</td>
<td>2.182E$-$03</td>
</tr>
<tr>
<td>2.00</td>
<td>1.131</td>
<td>4.607E$-$03</td>
<td>4.438E$-$03</td>
<td>4.239E$-$03</td>
</tr>
<tr>
<td>5.00</td>
<td>2.826</td>
<td>1.239E$-$02</td>
<td>1.192E$-$02</td>
<td>1.164E$-$02</td>
</tr>
<tr>
<td>10.00</td>
<td>5.639</td>
<td>2.448E$-$02</td>
<td>2.328E$-$02</td>
<td>2.276E$-$02</td>
</tr>
<tr>
<td>15.00</td>
<td>8.424</td>
<td>3.762E$-$02</td>
<td>3.547E$-$02</td>
<td>3.424E$-$02</td>
</tr>
<tr>
<td>20.00</td>
<td>11.170</td>
<td>4.824E$-$02</td>
<td>4.824E$-$02</td>
<td>4.438E$-$02</td>
</tr>
<tr>
<td>25.00</td>
<td>13.847</td>
<td>6.176E$-$02</td>
<td>6.424E$-$02</td>
<td>5.621E$-$02</td>
</tr>
<tr>
<td>50.00</td>
<td>26.272</td>
<td>1.099E$-$01</td>
<td>1.165E$-$01</td>
<td>1.044E$-$01</td>
</tr>
</tbody>
</table>

## 6. Conclusions

In this paper, the characteristic of the piezoelectric ceramics is indicated by the electromechanical coupling partial differential equations, then the partial differential equations can be solved by the Hermite-type RPIM. This method uses nodes to discrete the inside and boundary of the problem domain instead of meshing, and constructs approximate displacement function. The two corrected coefficients are introduced to make approximate displacement function close to exact displacement function, and the displacement of the evaluation nodes are solved by approximate displacement function.

The nodes within the problem domain need to meet the governing equations, while the nodes on the boundary need to meet boundary condition equations. The accuracy and effectiveness of the Hermite-type RPIM are confirmed by solving the electromechanical coupling partial differential equations of piezoelectric ceramics.

In contrast with the FEM and the local Petro-Galerkin method it is easier for the Hermite-type RPIM to solve the local regions accurately. This paper illustrates a rapid and efficient meshless method, the Hermite-type RPIM, to solve the electromechanical coupling partial differential equations of the piezoelectric ceramics.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant number 11271234).

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:.

## References

[1] Y.T. He, J.H. Liu, L. Li, J.H. He, A novel capacitive pressure sensor and interface circuitry, Microsyst. Technol. 19 (2013) 25-30.
[2] T. Kawada, H. Suzuki, T. Shimizu, M. Katsumata, Agreement in regard to total sleep time during a nap obtained via a sleep polygraph and accelerometer: a comparison of different sensitivity thresholds of the accelerometer, Int. J. Behav. Med. 19 (2012) 398-401.
[3] Y.X. Liu, J.K. Liu, W.S. Chen, P.L. Feng, A square-type rotary ultrasonic motor using longitudinal modes, J. Electroceramics 33 (2014) 69-74.
[4] H.Y. Lee, M.R. Ohm, J.Y. Shin, Fully discrete mixed finite element method for a quasilinear stefan problem with a forcing term in non-divergence form, J. Appl. Math. Comput. 24 (2007) 191-207.
[5] H. Guo, A splitting positive definite mixed finite element method for two classes of integro-differential equations, J. Appl. Math. Comput. 39 (2012) 271-301.
[6] J.J. Monaghan, Particle method for hydrodynamics, Comput. Phys. Rep. 3 (1985) 71-124.
[7] R.A. Gingold, J.J. Monaghan, Smoothed particle hydrodynamics: theory and applications to non-spherical stars, Mon. Not. R. Astron. Soc. 18 (1977) 375-389.
[8] L. Chen, H.P. Ma, Y.M. Cheng, Combining the complex variable reproducing kernel particle method and the finite element method for solving transient heat conduction problems, Chin. Phys. B 22 (5) (2013) 050202.
[9] X. Zhang, M.W. Lu, J.L. Wegner, A 2-D meshless model for jointed rock structures, Int. J. Num. Meth. Eng. 47 (10) (2000) 1649-1661.
[10] C.T. Yang, Application of reproducing kernel particle method and element-free Galerkin method on the simulation of the membrane of capacitive micromachined microphone in viscothermal air, Comput. Mech. 51 (2013) 295-308.
[11] D.D. Wang, P.J. Chen, Quasi-convex reproducing kernel meshfree method, Comput. Mech. 54 (2014) 689-709.
[12] L. Chen, Y.M. Cheng, H.P. Ma, The complex variable reproducing kernel particle method for the analysis of Kirchhoff plates, Comput. Mech. 55 (3) (2013) 591-602.
[13] S.B. Lin, X. Liu, Y.H. Rong, Z.B. Xu, Almost optimal estimates for approximation and learning by radial basis function networks, Mach. Learn. 95 (2014) 147-164.
[14] A. Žilinskas, On similarities between two models of global optimization: statistical models and radial basis functions, J. Glob. Optim. 48 (2010) 173-182.
[15] Y.J. Deng, C. Liu, M.J. Peng, Y.M. Cheng, The interpolating complex variable element-free Galerkin method for temperature field problems, Int. J. Appl. Mech. 7 (2) (2015) 1550017.
[16] Y. Yin, L.Q. Yao, Y. Cao, A 3D shell-like approach using element-free Galerkin method for analysis of thin and thick plate structures, Acta Mech. Sin. 29 (1) (2013) 85-98.
[17] Y.M. Cheng, F.N. Bai, C. Liu, M.J. Peng, Analyzing nonlinear large deformation with an improved element-free Galerkin method via the interpolating moving least-squares method, Int. J. Comput. Mater. Sci. Eng. 5 (4) (2016) 1650023.
[18] Y.M. Cheng, C. Liu, F.N. Bai, M.J. Peng, Analysis of elastoplasticity problems using an improved complex variable element-free Galerkin method, Chin. Phys. B 24 (10) (2015) 100202.
[19] M. Tatari, M. Kamranian, M. Dehghan, The finite point method for the p-Laplace equation, Comput. Mech. 48 (2011) 689-697.
[20] Z.Y. Huang, X. Yang, Tailored finite point method for first order wave equation, J. Sci. Comput. 49 (2011) 351-366.
[21] J.P. Shi, W.T. Ma, N. Li, Extended meshless method based on partition of unity for solving multiple crack problems, Meccanica 48 (2013) 2263-2270.
[22] O. Christensen, P. Massopust, Exponential B-splines and the partition of unity property, Adv. Comput. Math. 37 (2012) 301-318.
[23] D.N. Varsamis, N.P. Karampetakis, On the Newton bivariate polynomial interpolation with applications, Multidimens. Syst. Sign. Process. 25 (2014) 179-209.
[24] Y. Strozecki, On enumerating monomials and other combinatorial structures by polynomial interpolation, Theory Comput. Syst. 53 (2013) 532-568.
[25] I. Svalina, K. Sabo, G. Šimunović, Machined surface quality prediction models based on moving least squares and moving least absolute deviations methods, Int. J. Adv. Manuf. Technol. 57 (2011) 1099-1106.
[26] C.Y. Song, H.Y. Choi, J.S. Lee, Approximate multi-objective optimization using conservative and feasible moving least squares method: application to automotive knuckle design, Struct. Multidisc. Optim. 49 (2014) 851-861.
[27] F.X. Sun, J.F. Wang, Y.M. Cheng, A.X. Huang, Error estimates for the interpolating moving least-squares method in n-dimensional space, Appl. Numer. Math. 98 (2015) 79-105.
[28] D. Mirzaei, R. Schaback, Solving heat conduction problems by the direct meshless local Petrov-Galerkin (DMLPG) method, Numer. Algor. 65 (2014) 275-291.
[29] G.Y. Sheu, Prediction of probabilistic settlements by the perturbation based spectral stochastic meshless Local Petrov-Galerkin Method, Geotech. Geol. Eng. 31 (2013) 1453-1464.
[30] B.D. Dai, B.J. Zheng, Numerical solution of transient heat conduction problems using improved meshless local Petrov-Galerkin method, Appl. Math. Comput. 219 (2013) 10044-10052.

[31] B.D. Dai, J. Cheng, B.J. Zheng, A moving Kriging interpolation-based meshless local Petrov-Galerkin method for elastodynamic analysis, Int. J. Appl. Mech. 5 (1) (2013) 1350011.

[32] M.B. Liu, G.R. Liu, Smoothed particle hydrodynamics (SPH): An overview and recent developments arch, Comput. Meth. Eng. 17 (2010) 25-76.

[33] Y.W. Han, H.F. Qiang, H. Liu, W.R. Gao, An enhanced treatment of boundary conditions in implicit smoothed particle hydrodynamics, Acta Mech. Sin. 30 (1) (2014) 37-49.

[34] I. Mantegh, M.R.M. Jenkin, A.A. Goldenberg, Path planning for autonomous mobile robots using the boundary integral equation method, J. Intell. Robot. Syst. 59 (2010) 191-220.

[35] G.Z. Xie, J.M. Zhang, C. Huang, C.J. Lu, G.Y. Li, A direct traction boundary integral equation method for three-dimension crack problems in infinite and finite domains, Comput. Mech. 53 (2014) 575-586.

[36] X.Y. Cui, G.R. Liu, G.Y. Li, A smoothed Hermite radial point interpolation method for thin plate analysis, Arch. Appl. Mech. 81 (2011) 1-18.

[37] Y. Liu, Y.C. Hon, K.M. Liew, A meshfree Hermite-type radial point interpolation method for Kirchhoff plate problems, Int. J. Numer. Methods Eng. 66 (2006) 1153-1178.

[38] A.L. Rocca, H. Power, A Hermite radial basis function collocation approach for the numerical simulation of crystallization processes in a channel, Commun. Numer. Meth. Eng. 22 (2006) 119-135.

[39] H.F. Gao, G.F. Wei, Stress intensity factor for interface cracks in bimaterials using complex variable meshless manifold method, Math. Probl. Eng. (2014) 353472.

[40] H.F. Gao, G.F. Wei, Complex variable meshless manifold method for elastic dynamic problems, Math. Probl. Eng. (2016) 5803457.