# Interaction of multiple straight cracks and elliptical inclusions in a finite plate due to mismatched thermal expansion

Jiong Zhang$^{a,*}$, Yunhai Huang$^{a}$, Weidong Liu$^{b}$, Liankun Wang$^{a}$

$^{a}$ School of Civil Engineering and Architecture, Wuyi University, 22 Dongcheng Village, Jiangmen 529020, PR China
$^{b}$ College of Energy and Electrical Engineering, Hohai University, No. 8 Fochengxi Road, Nanjing 211100, PR China

---

## ARTICLE INFO

**Keywords:**
Eshelby's equivalent inclusion
Inclusion
Crack
Distributed dislocations

## ABSTRACT

The purpose of this paper is to study the interaction between multiple elliptical inclusions and straight cracks in a finite plate due to a uniform temperature change. In this solution, Eshelby's equivalent inclusion method involving both interior Eshelby's tensor and exterior Eshelby's tensor is applied to calculate the thermal stress fields of an infinite plate containing multiple elliptical inclusions under a uniform temperature change first. Then the multiple cracks and the boundary are modeled by continuous distributions of dislocation densities in an infinite plate. Based on the stress boundary conditions of the cracks and boundary, a system of singular integral equations with Cauchy kernels are obtained. After solving the singular integral equations with Gauss–Chebyshev numerical quadrature, the stress intensity factor of each crack can be calculated. Besides, the finite element method is employed to examine the accuracy and efficiency of the presented method. Finally, the effects of the material and geometric parameters on the normalized stress intensity factors of the cracks are studied.

---

## 1. Introduction

Reinforced composite materials have been widely applied in many engineering areas such as aerospace, automotive and other fields for their excellent mechanical properties. However, due to mismatched thermal expansion coefficients, cracks unavoidably arise between the reinforcements and the matrix under thermal loading or temperature changes. Behaviors of the cracks in composites are much more complicated than in homogeneous materials due to the effects of the reinforcements. To prevent the catastrophic failure of the reinforced composite materials, it is very import to study the interaction of the cracks and inclusions when subjected to a temperature changes.

Various numerical methods have been conducted to study the thermal interaction of the crack and inclusion such as distributed dislocations method [1–6], equivalent inclusion method [7–9], interaction energy integral method [10]. However, most of the previous work is limited to one single inclusion or one crack in an infinite plate. Very few studies focus on the crack problem of a finite plate containing multiple cracks and inclusions due to mismatched thermal expansion.

As we all know, the Eshelby's equivalent inclusion method [11,12] is very efficient to study the inclusion problems. In the Eshelby's equivalent inclusion, it was more difficult to solve the exterior elastic field comparing with the interior elastic fields. However, Jin [13] presented a closed-form for exterior Eshelby's tensor to solve the exterior elastic fields and this can make it more convenient to solve the multiple inclusion problems.

Additionally, the distributed dislocation method has been widely used to solve various kinds of crack problems in infinite plates,

---

* Corresponding author.
E-mail address: jiongzhang@wyu.edu.cn (J. Zhang).

https://doi.org/10.1016/j.engfracmech.2020.107267
Received 20 February 2020; Received in revised form 6 August 2020; Accepted 10 August 2020
Available online 15 August 2020
0013-7944/ © 2020 Elsevier Ltd. All rights reserved.

![](./images/812578055485652992_1.jpg)

Fig. 1. A finite plate containing multiple elliptical inclusions and multiple cracks subjected to $\Delta T$.

finite plates and half plates [16-25]. Previous research [19] shows this method has considerable computational efficiency for solving a problem with large numbers of cracks and a problem of 100 cracks are solved with high efficiency. The main idea of this method is to model the cracks and boundary by a serial of continuous dislocations in an infinite medium. A system of singular integral equations with Cauchy-type kernel can be formulated based on the boundary condition of the cracks and boundary. By solving the singular integral equations, the stress intensity factor of each crack can be readily obtained.

So this paper, we present a numerical method combining the equivalent inclusion method and distributed dislocation method to solve the interaction of multiple inclusions and cracks in a finite plate subjected to a uniform temperature change. The mathematical process of the presented method is introduced first. Then some numerical examples are presented to show the practical application of the presented method. Also the accuracy and efficiency of the presented method is verified by the FEA.

## 2. Basic theory

### 2.1. Problem formation

A finite plate containing $N_{inc}$ elliptical inclusions and $N_{c}$ cracks is shown in Fig. 1. The $I$-th crack has an arbitrary lengths $2a_{I}$ and inclination angle $\theta_{I}$. The $I$-th elliptical inclusion has an arbitrary shear moduli $\mu_{I}$, coefficient of thermal expansion $\alpha_{I}$, Poisson's ratio $\nu_{I}$, the orientation angle $\varphi_{I}$ and two semi-axes $a_{I}$, $c_{I}$ respectively. The boundary of the plate contains $N_{b}$ segments and the $I$-th segment has a length of $2\Gamma_{I}$. When a temperature change $\Delta T$ occurs (heating up or cooling down), due to the mismatched thermal expansion coefficients of the matrix and the inclusions, thermal stresses develop and then an interaction occurs between the cracks and inclusions.

We can decompose this problem shown in Fig. 1 into the following two sub-problems based on the superposition principle as shown in Fig. 2: (a) an infinite plate containing multiple inclusions subjected to a uniform temperature change (as shown in Fig. 2(a)); (b) an infinite plate containing multiple straight cracks and a kinked crack, since the boundary can also be simulated by a special kinked crack by imagining the finite plate as a cut-out from an infinite plane[23] (as shown in Fig. 2(b)). Thus, the sub-problem shown in Fig. 2(a) can be solved by the equivalent inclusion method and the sub-problem shown in Fig. 2(b) can be solved by the distributed dislocation method.

### 2.2. Equivalent inclusion method to solve sub-problem (a)

Both the interior Eshelby's tensor and the exterior Eshelby's tensor [13] are adopted in this research. When a temperature change $\Delta T$ takes place, a uniform strain expressed in the local coordinate system of the $I$-th inclusion will arise as follows [14],

$$
\varepsilon_{\hat{x} \hat{x}}^{P(I)}=\varepsilon_{\hat{y} \hat{y}}^{P(I)}=\left(\alpha_{I}^{*}-\alpha\right), \quad \varepsilon_{\hat{x} \hat{y}}^{P(I)}=0
\tag{1}
$$

where $\alpha_{I}^{*}$ and $\alpha$ are the coefficients of thermal expansion of the $I$-th inclusion and the matrix respectively.

Based on the equivalent inclusion method, problem shown in Fig. 2(a) can be transformed to the problem shown in Fig. 3. For a point located at $(x, y)$, the disturbance strain $\varepsilon_{i j^{\prime}}^{\prime(I)}$ aroused by the $I$-th inclusion can be obtained as [13],

$$
\varepsilon_{\hat{i} \hat{j}}^{\prime(I)}=K_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)} \varepsilon_{\hat{k} \hat{l}}^{*(I)}
\tag{2}
$$

where $\varepsilon_{\hat{k} \hat{l}}^{*(I)}$ is the eigenstrain strain of the $I$-th inclusion. And$K_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)}=\begin{cases}
S_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)} & \text{if} \quad \frac{x^{2}}{a_{I}^{2}}+\frac{y^{2}}{c_{I}^{2}} \leqslant 1 \\
G_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)} & \text{if} \quad \frac{x^{2}}{a_{I}^{2}}+\frac{y^{2}}{c_{I}^{2}}>1
\end{cases}, S_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)}$ is the interior Eshelby's tensor

![](./images/812578055485652992_2.jpg)

![](./images/812578055485652992_3.jpg)

Fig. 2. Decomposition of the original problem.

and $G_{\hat{i} \hat{j} \hat{k} \hat{l}}^{(I)}$ is the exterior Eshelby's tensor related to the $I$-th inclusion, $a_{I}$ and $c_{I}$ are the two semi-axis of the $I$-th inclusion respectively.

Based on the Hooke's law, by applying the equivalency condition at the center of $I$-th inclusion, the following equation can be given [11],

$$
C_{\hat{i} \hat{j} \hat{k} \hat{l}}^{*(I)} \varepsilon_{\hat{k} \hat{l}}^{\prime}=C_{\hat{i} \hat{j} \hat{k} \hat{l}}\left(\varepsilon_{\hat{k} \hat{l}}^{\prime}-\varepsilon_{\hat{k} \hat{l}}^{P(I)}\right)
$$

Where $C_{\hat{i} \hat{j} \hat{k} \hat{l}}^{*(I)}$ and $C_{\hat{i} \hat{j} \hat{k} \hat{l}}$ are the elastic modules of the $I$-th inclusion and the matrix respectively, $\varepsilon_{\hat{i} \hat{j}}^{\prime}$ is the summation of the disturbance strain caused by all the inclusions which can be calculated by the following equation by extending the research [13,15] to multiple inclusions,

$$
\varepsilon_{i j}^{\prime}=\sum_{M=1}^{N_{i n c}} K_{i j k l}^{(M)} \varepsilon_{k l}^{*(M)}
$$

where $K_{i j k l}^{(M)}=
\begin{cases}
S_{i j k l}^{(M)} & \text { if } \quad M=I \\
G_{i j k l}^{(M)} & \text { if } \quad M \neq I
\end{cases}, S_{i j k l}^{(M)}$ and $G_{i j k l}^{(M)}$ are the Eshelby's tensor for the $M$-th inclusion.

A linear algebraic system containing $3 \times N_{i n c}$ equations and $3 \times N_{i n c}$ unknown eigenstrain strains can be readily obtained and

![](./images/812578055485652992_4.jpg)

Fig. 3. Equivalent inclusion method.

expressed in the matrix form by applying the equivalency condition at the center of each inclusion. Extending the research [13,15] to multiple inclusions, thus the stress $\sigma_{ij}^{\Delta T}(x, y)$ of a point located at $(x, y)$ due to the temperature change expressed in global coordinate system can be calculated by solving the equations,

For a point in the matrix:

$$
\sigma_{i j}^{\Delta T}=\sum_{M=1}^{N_{i n c}} C_{i j m n} G_{m n k l}^{(M)} \varepsilon_{k l}^{*(M)}
\tag{5}
$$

For a point in $I$-th inclusion:

$$
\sigma_{i j}^{\Delta T}=C_{i j m n}^{*(I)} S_{m n k l}^{(I)} \varepsilon_{k l}^{*(I)}+\sum_{M=1}^{I-1} C_{i j m n} G_{m n k l}^{(M)} \varepsilon_{k l}^{*(M)}+\sum_{M=I+1}^{N_{i n c}} C_{i j m n} G_{m n k l}^{(M)} \varepsilon_{k l}^{*(M)}
\tag{6}
$$

### 2.3. Distributed dislocation method to solve sub-problem (b)

The cracks and the boundary can be modelled as distributed dislocation densities along the line of the crack as shown in Fig. 4.

As shown in Fig. 5, a point located at $(x, y)$ has an induced stress field by an edge dislocation located at $(\eta, \xi)$ with the unknown Burgers vector $(b_{x}(\xi, \eta), b_{y}(\xi, \eta))$ which can be expressed as follows [14],

![](./images/812578055485652992_5.jpg)

Fig. 4. Modeling the cracks and boundary by continuous distributed dislocations.

![](./images/812578055485652992_6.jpg)

Fig. 5. Stresses induced due to the dislocation in an infinite plate.

$$
\begin{bmatrix}
\sigma_{xx}^{Dislocation}(x,y) \\
\sigma_{yy}^{Dislocation}(x,y) \\
\sigma_{xy}^{Dislocation}(x,y)
\end{bmatrix} = \frac{2\mu}{\pi(\varkappa + 1)}
\begin{bmatrix}
G_{xxx}(x, y; \xi, \eta) & G_{yxx}(x, y; \xi, \eta) \\
G_{xyy}(x, y; \xi, \eta) & G_{yyy}(x, y; \xi, \eta) \\
G_{xxy}(x, y; \xi, \eta) & G_{yxy}(x, y; \xi, \eta)
\end{bmatrix}
\begin{bmatrix}
b_x(\xi, \eta) \\
b_y(\xi, \eta)
\end{bmatrix} \tag{7}
$$

where $\mu$ is the shear modulus of the plate, $\nu$ is Poisson's ratio, $\varkappa=(3-\nu)/(1+\nu)$ for plane stress and $\varkappa=3-4\nu$for plane strain. The stress influence function $G_{ijkl}$ can be calculated as follows [16],

$$
\begin{cases}
G_{xxx}=\left(-\frac{1}{r_1^2}\right)\left(1+\frac{2x_1^2}{r_1^2}\right); & G_{yxx}=\left(-\frac{x_1}{r_1^2}\right)\left(1-\frac{2x_1^2}{r_1^2}\right) \\
G_{xyy}=\left(-\frac{x_1}{r_1^2}\right)\left(1-\frac{2x_1^2}{r_1^2}\right); & G_{yyy}=\left(-\frac{1}{r_1^2}\right)\left(3-\frac{2x_1^2}{r_1^2}\right) \\
G_{xxy}=\left(-\frac{x_1}{r_1^2}\right)\left(1-\frac{2x_1^2}{r_1^2}\right); & G_{yxy}=\left(-\frac{1}{r_1^2}\right)\left(1-\frac{2x_1^2}{r_1^2}\right)
\end{cases} \tag{8}
$$

where $r^2=x_1^2+y_1^2$, $x_1=x-\xi$, $y_1=y-\eta$.

Now the local coordinates of every crack branch are created as Fig. 6. The $I$-th local coordinate system is fixed at the center of the $I$-th boundary branch. The $\hat{X}$ and $\hat{Y}$ axes are along the crack line and vertical to the crack line respectively.

If we consider a dislocation is located at $(\hat{\xi}_J,0)$ on the $J$-th crack branch, then the induced stresses of the point $(\hat{x}_I,0)$ on the $I$-th crack branch can be calculated as [17],

![](./images/812578055485652992_7.jpg)

Fig. 6. Local coordinates for each crack.

$$
\begin{bmatrix}
\sigma_{\hat{x} \hat{x}}^{\text{Dislocation}}(\hat{x}_{I}, 0) \\
\sigma_{\hat{y} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0) \\
\sigma_{\hat{x} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0)
\end{bmatrix}
=
\frac{2\mu}{\pi(\varkappa + 1)}
\begin{bmatrix}
G_{\hat{x} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0)
\end{bmatrix}
\begin{bmatrix}
b_{\hat{x}}(\hat{\xi}_{J}, 0) \\
b_{\hat{y}}(\hat{\xi}_{J}, 0)
\end{bmatrix}
\tag{9}
$$

Note that corresponding transformation rules for $G_{ijk}$ and $b_i$ from global coordinates system to local coordinates can be summarized as Eqs. (10) and (11) [16,19],

$$
\begin{bmatrix}
b_{x}(\hat{\xi}_{J}, 0) \\
b_{x}(\hat{\xi}_{J}, 0)
\end{bmatrix}
=
\begin{bmatrix}
\cos \theta_{J} & -\sin \theta_{J} \\
\sin \theta_{J} & \cos \theta_{J}
\end{bmatrix}
\begin{bmatrix}
b_{\hat{x}}(\hat{\xi}_{J}, 0) \\
b_{\hat{y}}(\hat{\xi}_{J}, 0)
\end{bmatrix}
\tag{10}
$$

$$
\begin{bmatrix}
G_{\hat{x} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0)
\end{bmatrix}
=
\begin{bmatrix}
\cos^2 \theta_{I} & \sin^2 \theta_{I} & \sin 2\theta_{I} \\
\sin^2 \theta_{I} & \cos^2 \theta_{I} & -\sin 2\theta_{I} \\
\frac{-\sin 2\theta_{I}}{2} & \frac{\sin 2\theta_{I}}{2} & \cos 2\theta_{I}
\end{bmatrix}
\begin{bmatrix}
G_{xxx}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{yxx}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{xyy}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{yyy}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{xxy}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{yxy}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0)
\end{bmatrix}
\begin{bmatrix}
\cos \theta_{J} & -\sin \theta_{J} \\
\sin \theta_{JJ} & \cos \theta_{J}
\end{bmatrix}
\tag{11}
$$

where $\theta_{I}$ , $\theta_{J}$ are the crack incline angles in the global coordinates for the $I$-th crack branch and the $J$-th crack branch respectively.

Now the induced stresses for $(\hat{x}_{I}, 0)$ due to the distributed dislocations of the $J$-th crack can be given by [25],

$$
\begin{bmatrix}
\sigma_{\hat{x} \hat{x}}^{\text{Dislocation}(J)}(\hat{x}_{I}, 0) \\
\sigma_{\hat{y} \hat{y}}^{\text{Dislocation}(J)}(\hat{x}_{I}, 0) \\
\sigma_{\hat{x} \hat{y}}^{\text{Dislocation}(J)}(\hat{x}_{I}, 0)
\end{bmatrix}
=
\frac{2\mu}{\pi(\varkappa + 1)}
\int_{-a_J}^{a_J}
\begin{bmatrix}
G_{\hat{x} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0)
\end{bmatrix}
\begin{bmatrix}
B_{\hat{x}}(\hat{\xi}_{J}, 0) \\
B_{\hat{y}}(\hat{\xi}_{J}, 0)
\end{bmatrix}
d\hat{\xi}_{J}
\tag{12}
$$

where $B_{\hat{x}}(\hat{\xi}_{J}, 0)=db_{\hat{x}}(\hat{\xi}_{J}, 0)/d\xi$, $B_{\hat{y}}(\hat{\xi}_{J}, 0)=db_{\hat{y}}(\hat{\xi}_{J}, 0)/d\xi$ are the density functions for the distributed dislocations along the $J$-th crack, $a_J$ is the half crack length of the $J$-th crack.

The induced stresses for $(\hat{x}_{I}, 0)$ of all the dislocations by the cracks and boundary can be given by the principle of superposition,

$$
\begin{bmatrix}
\sigma_{\hat{x} \hat{x}}^{\text{Dislocation}}(\hat{x}_{I}, 0) \\
\sigma_{\hat{y} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0) \\
\sigma_{\hat{x} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0)
\end{bmatrix}
=
\frac{2\mu}{\pi(\varkappa + 1)}
\sum_{J=1}^{M}
\int_{-a_J}^{a_J}
\begin{bmatrix}
G_{\hat{x} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{x}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{y} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) \\
G_{\hat{x} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0) & G_{\hat{y} \hat{x} \hat{y}}^{II}(\hat{x}_{I}, 0; \hat{\xi}_{J}, 0)
\end{bmatrix}
\begin{bmatrix}
B_{\hat{x}}(\hat{\xi}_{J}) \\
B_{\hat{y}}(\hat{\xi}_{J})
\end{bmatrix}
d\hat{\xi}_{J}
\tag{13}
$$

where $M=N_c+N_b$. $N_c$ is the number of cracks and $N_b$ is the number of crack branches of the boundary.

### 2.4. Singular integral equations

Note that for a point $(\hat{x}_{I}, 0)$ located in the $I$-th crack or boundary, the stress is an addition of the above two solutions of stress distribution $\sigma^{\text{Dislocation}}(\hat{x}_{I}, 0)$ and $\sigma^{\Delta T}(\hat{x}_{I}, 0)$. It is noted that $\sigma^{\Delta T}(\hat{x}_{I}, 0)$ can be obtained by Eq. (5).

Since no displacements or mechanical boundary conditions are applied on the external boundary of the plate, the external boundary has to satisfy the traction free condition. Thus for both the cracks and boundary, the normal stress and shear stress of the crack line need to vanish, which gives the following equations,

$$
\begin{bmatrix}
\sigma_{\hat{y} \hat{y}}^{\Delta T}(\hat{x}_{I}, 0) \\
\sigma_{\hat{x} \hat{y}}^{\Delta T}(\hat{x}_{I}, 0)
\end{bmatrix}
+
\begin{bmatrix}
\sigma_{\hat{y} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0) \\
\sigma_{\hat{x} \hat{y}}^{\text{Dislocation}}(\hat{x}_{I}, 0)
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0
\end{bmatrix}
\tag{14}
$$

Inserting Eq. (13) into Eq. (14) and the governing integral equations with Cauchy kernels can be obtained,


$$
-\frac{\pi(\kappa+1)}{2 \mu}\left[\begin{array}{l}
\sigma_{\hat{x} \hat{y}}^{\Delta T}\left(\hat{x}_{I}, 0\right) \\
\sigma_{\hat{x} \hat{y}}^{\Delta T}\left(\hat{x}_{I}, 0\right)
\end{array}\right]=\frac{2 \mu}{\pi(\kappa+1)} \sum_{J=1}^{M} \int_{-a_{J}}^{a_{J}}\left[\begin{array}{ll}
G_{\hat{x} \hat{y} \hat{y}}^{I I}\left(\hat{x}_{I}, 0 ; \hat{\xi}_{J}, 0\right) & G_{\hat{y} \hat{y} \hat{y}}^{I I}\left(\hat{x}_{I}, 0 ; \hat{\xi}_{J}, 0\right) \\
G_{\hat{x} \hat{x} \hat{y}}^{I I}\left(\hat{x}_{I}, 0 ; \hat{\xi}_{J}, 0\right) & G_{\hat{y} \hat{x} \hat{y}}^{I I}\left(\hat{x}_{I}, 0 ; \hat{\xi}_{J}, 0\right)
\end{array}\right]\left[\begin{array}{l}
B_{\hat{x}}\left(\hat{\xi}_{J}\right) \\
B_{\hat{y}}\left(\hat{\xi}_{J}\right)
\end{array}\right] d \hat{\xi}_{J}
$$

### 2.5. Numerical solution of the governing singular integral equations

In order to solve the governing singular integral equations, Eq. (15) needs to be normalized within the interval $[-1,1]$ firstly by the following transform [26],
$$
\left\{\begin{aligned}
\hat{\xi}_{J} & =\hat{\xi}_{J}\left(\hat{s}_{I}\right)=\frac{a_{I}}{2} \hat{s}_{I} \\
\hat{x}_{I} & =\hat{x}_{I}\left(\hat{t}_{I}\right)=\frac{a_{I}}{2} \hat{t}_{I}
\end{aligned}\right.
$$

Then the dislocation density functions for the $I$-th crack can be decomposed in the following form [26],
$$
\left[\begin{array}{l}
B_{\hat{x}}\left(\hat{\xi}_{I}\left(\hat{s}_{I}\right)\right) \\
B_{\hat{y}}\left(\hat{\xi}_{I}\left(\hat{s}_{I}\right)\right)
\end{array}\right]=\frac{1}{\sqrt{1-\hat{s}_{I}^{2}}}\left[\begin{array}{l}
\phi_{\hat{x}}^{I}\left(\hat{s}_{I}\right) \\
\phi_{\hat{y}}^{I}\left(\hat{s}_{I}\right)
\end{array}\right]
$$

where $\phi_{\hat{x}}^{i}\left(\hat{s}_{i}\right)$ and $\phi_{\hat{y}}^{i}\left(\hat{s}_{i}\right)$ are the new unknown functions to be determined and $-1 \leqslant \hat{s}_{i} \leqslant 1$ is a non-dimensional parameter along $I$-th crack.

Now imposing $\mathrm{N}$ integration points and $\mathrm{N}-1$ collocation points accordingly on the $I$-th crack, the following algebraic equations can be obtained,
$$
\begin{gathered}
-\frac{\pi(\kappa+1)}{2 \mu}\left[\begin{array}{l}
\sigma_{\hat{x} \hat{x}}^{\Delta T}\left(\hat{x}_{I}, 0\right) \\
\sigma_{\hat{x} \hat{y}}^{\Delta T}\left(\hat{x}_{I}, 0\right)
\end{array}\right]= \\
\sum_{J=1}^{M} \frac{a_{I}}{2} \sum_{i=1}^{N}\left[\begin{array}{ll}
G_{\hat{x} \hat{y} \hat{y}}^{I}\left(\hat{x}_{I}\left(\hat{t}_{k}^{I}\right), 0 ; \hat{\xi}_{J}\left(\hat{s}_{i}^{J}\right), 0\right) & G_{\hat{y} \hat{y} \hat{y}}^{I}\left(\hat{x}_{I}\left(\hat{t}_{k}^{I}\right), 0 ; \hat{\xi}_{J}\left(\hat{s}_{i}^{J}\right), 0\right) \\
G_{\hat{x} \hat{x} \hat{y}}^{I}\left(\hat{x}_{I}\left(\hat{t}_{k}^{I}\right), 0 ; \hat{\xi}_{J}\left(\hat{s}_{i}^{J}\right), 0\right) & G_{\hat{y} \hat{x} \hat{y}}^{I}\left(\hat{x}_{I}\left(\hat{t}_{k}^{I}\right), 0 ; \hat{\xi}_{J}\left(\hat{s}_{i}^{J}\right), 0\right)
\end{array}\right]\left[\begin{array}{l}
\phi_{\hat{x}}^{J}\left(\hat{s}_{i}^{J}\right) \\
\phi_{\hat{y}}^{J}\left(\hat{s}_{i}^{J}\right)
\end{array}\right]
\end{gathered}
$$

where $\hat{s}_{i}=\cos \left(\frac{2 i-1}{2 W} \pi\right), \mathrm{i}=1,2 \ldots \mathrm{N}$ and $\hat{t}_{k}=\cos \left(\frac{k}{W} \pi\right), \mathrm{k}=1,2 \ldots \mathrm{N}-1$.

However, extra equations are needed in order to solve Eq. (18). For the boundary, the dislocation densities along the $I$-th boundary and $I+1$-th boundary are equal. Thus, the following equations can be given [26],
$$
\begin{aligned}
& \cos \theta_{I} \phi_{\hat{x}}^{I}(+1)-\sin \theta_{I} \phi_{\hat{y}}^{I}(+1)=\cos \theta_{I+1}^{I} \phi_{\hat{x}}^{I+1}(+1)-\sin \theta_{I+1}^{I} \phi_{\hat{y}}^{I+1}(+1) \\
& \sin \theta_{I+1} \phi_{\hat{x}}^{I}(+1)+\cos \theta_{I} \phi_{\hat{y}}^{I}(+1)=\sin \theta_{I+1}^{I} \phi_{\hat{x}}^{I+1}(+1)+\cos \theta_{I+1}^{I} \phi_{\hat{y}}^{I+1}(+1)
\end{aligned}
$$

Here can be calculated by the following equations [26],
$$
\begin{aligned}
& \phi(+1)=\sum_{i=1}^{N} \frac{\sin ((2 i-1)(2 n-1) \pi /(4 N))}{\sin ((2 i-1) /(4 N))} \phi\left(s_{i}\right) \\
& \phi(-1)=\sum_{i=1}^{N} \frac{\sin ((2 i-1)(2 n-1) \pi /(4 n))}{\sin ((2 i-1) /(4 n))} \phi\left(s_{N+1-i}\right)
\end{aligned}
$$

Besides, the summation of the net dislocation from all the crack branches for a kinked crack (the boundary of the plate) must be zero when moving from one end of the crack to the other. Thus other two equations can be obtained [26],
$$
\begin{aligned}
& \sum_{I=1}^{N_{b}}\left[\frac{\Gamma_{I} \cos \theta_{I}}{N} \sum_{i=1}^{N} \phi_{\hat{x}}^{I(i)}\left(\hat{s}_{i}\right)-\frac{\Gamma_{I} \sin \theta_{I}}{N} \sum_{i=1}^{N} \phi_{\hat{y}}^{I(i)}\left(\hat{s}_{i}\right)\right]=0 \\
& \sum_{I=1}^{N_{b}}\left[\frac{\Gamma_{I} \sin \theta_{I}}{N} \sum_{i=1}^{W} \phi_{\hat{x}}^{I(i)}\left(\hat{s}_{i}\right)+\frac{\Gamma_{I} \sin \theta_{I}}{N} \sum_{i=1}^{N} \phi_{\hat{y}}^{I(i)}\left(\hat{s}_{i}\right)\right]=0
\end{aligned}
$$

As for the straight cracks, other two extra equations can be given base on the displacements of the crack tips need to be zero,
$$
\begin{aligned}
& \sum_{i=1}^{N} \phi_{\hat{x}}\left(\hat{s}_{i}\right)=0 \\
& \sum_{i=1}^{N} \phi_{\hat{y}}\left(\hat{s}_{i}\right)=0
\end{aligned}
$$

By solving the algebraic equations (18)-(22), $\phi_{\hat{x}}$ and $\phi_{\hat{y}}$ can be obtained. The stress intensity factor for each crack can be calculated by the following equation [26],
$$
\begin{aligned}
& K_{I}^{I}( \pm 1)= \pm \sqrt{\pi a_{I}} \frac{2 \mu}{\kappa+1} \phi_{\hat{y}}^{I}( \pm 1) \\
& K_{I I}^{I}( \pm 1)= \pm \sqrt{\pi a_{I}} \frac{2 \mu}{\kappa+1} \phi_{\hat{x}}^{I}( \pm 1)
\end{aligned}
$$

where $a_{I}$ is the half crack length of the $I$-th crack. $K_{I}^{I}( \pm 1)$ represents the mode I stress intensity factors of the left tip and right tip of $I$-th crack respectively. Similarly, $K_{I I}^{I}( \pm 1)$ represents the mode II stress intensity factors of the left tip and right tip of $I$-th crack respectively

![](./images/812578055485652992_8.jpg)

Fig. 7. A square plane containing 5 inclusions and 2 cracks subjected to $\Delta T$.

### 3. Verification

In order to validate the presented method, both the presented method and FE software ABAQUS are used to solve the problem shown in Fig. 7.

As shown in Fig. 7, a square plate containing 5 inclusions and 2 cracks is subjected to a uniform temperature change $\Delta T$. The shear modulus and thermal expansion coefficients of the matrix and inclusions are denoted by$\mu, \alpha, \mu_{i}$ and $\alpha_{i}$ respectively. The dimensions of this problem are in mm. The locations and incline angles of the cracks and inclusions are shown in Fig. 7. The 4 crack tips are denoted by A, B, C and D. The Poisson's ratio $v$ of the matrix and inclusions are assumed to be 0.3. 4-node bilinear quadratic elements (plane strain) are used in the finite element analysis. Singular elements are used around the crack tip to calculate the stress intensity factors. The meshes of this model are shown in Fig. 8.

The normalized stress intensity factor of the crack is defined as,

$$
F=K /\left(\mu \cdot\left(\alpha_{1}-\alpha\right) \cdot \Delta T \cdot \sqrt{\pi a}\right) \tag{24}
$$

where K is the calculated stress intensity factor for the crack. $\mu$ is the shear modulus of the matrix. $\alpha_{1}$ and $\alpha$ are the thermal expansion coefficients of the inclusions and matrix respectively. $a$ is the half crack length of the crack.

Firstly, $\mu_{1} / \mu$ is fixed at 0.2 and 100 respectively. And the variation of the normalized stress intensity factors with the increase of the number of integration points is studied as shown in Fig. 9.

As we can see from Fig. 9, when the integration number of each crack increases from 2 to 20, the results of the presented method converge with the FEA very quickly. Actually, when the integration number is 10, most of the maximum errors between the two methods are less than 5% except for $F_{\mathrm{II}(\mathrm{C})}$. That is because $F_{\mathrm{II}(\mathrm{C})}$ is very small in this example. In order to obtain a very good result of

![](./images/812578055485652992_9.jpg)

(a) The whole model
(b) crack tip

Fig. 9. Normalized stress intensity factor versus the number of integration points.

![](./images/812578055485652992_10.jpg)

Fig.8. Meshes of the model.

the FEA, the meshes must be very fine. Thus it takes a couple of minutes to finish this calculation. However, only less than 10 s are needed for the presented method.

Fig. 10 shows the effect of the $\mu_1/\mu$ on the normalized stress intensity factor when the integration number is selected to be 20. We can also find that the results agree with each other very well.

## 4. Applications

In this section, two numerical examples are presented to show the application of the presented method. The Poisson's ratios $\nu$ for all the inclusions and matrix are 0.3. Plane strain condition is assumed. The number of integration points for each crack is fixed at 20. We also need to mention that only circular inclusions are considered in the following examples since they are the most commonly used in the composites materials though the presented method is capable of solving elliptical inclusions problems.

### 4.1. One inclusion and one crack

One circular inclusion and one horizontal crack are embedded in a square plate as shown in Fig. 11. The crack with the length of $2a$ is fixed at the center of the plate. The distance between the center of the crack and the inclusion is $D$. The 2 crack tips are denoted by $A$ and $B$. Similarly, all the stress intensity factors are normalized by($\mu\cdot(\alpha_1 - \alpha)\cdot\Delta T\cdot\sqrt{\pi a}$).

(1) The effect of $\mu_1/\mu$ on the normalized stress intensity factors.

In this example, the following condition is fixed first: $H = W = 10R$, $R = a$, $D = 3R$ and $\varphi = 0$.
The variation of the normalized stress intensity factors for crack tips A and B with the increases of $\mu_1/\mu$ are shown in Fig. 12.

![](./images/812578055485652992_11.jpg)

Fig. 10. Normalized stress intensity factor for different $\mu_1/\mu$.

![](./images/812578055485652992_12.jpg)

Fig. 11. A square plate containing a inclusion and a crack subjected to $\Delta T$.

![](./images/812578055485652992_13.jpg)

Fig. 12. The normalized stress intensity factors vs $\mu_1/\mu$.

As we can see from Fig. 12, the normalized stress intensity factors increase with the increase of $\mu_1/\mu$. When $\mu_1/\mu$ is less than 1, the increase is very drastic. However when $\mu_1/\mu$ is larger than 20, the increase is not obvious anymore and almost remain unchanged. We can also see that the normalized stress intensity factor of A is larger than that of B since crack tip A is much closer to the inclusion than B.

(2) The effect of $D$ on the normalized stress intensity factors.

Now the distance between the crack of the inclusion $D$ is studied here. The following condition is fixed: $H = W = 10R$, $R = a$ and $\varphi = 0$.

The change of the normalized stress intensity factors for crack tips A and B with the increases of $D/R$ is shown in Fig. 13.

It is very obvious in Fig. 13 that both $F_{I(A)}$ and $F_{I(B)}$ decrease when the inclusion is getting further to the crack. When the inclusion is much far from the inclusion, they are very close to zero since the effect of the difference of the thermal expansion coefficients of the inclusion and matrix under temperature change vanishes.

(3) The effect of the angle $\varphi$ on the normalized stress intensity factors.

In this case, the change of the normalized stress intensity factors is studied when $\varphi$ increases from 0 to $\pi$ under the following condition: $H = W = 10R$, $R = a$ and $D = 3R$. The results are shown in Fig. 14.

As we can see from Fig. 14, both $F_{I(A)}$ and $F_{I(B)}$ decrease with the increase of $\varphi$ when $\varphi$ is less than $\pi/2$. Then $F_{I(A)}$ and $F_{I(B)}$ increase since the inclusion is about to be on the crack line. However, there are two inflexion points for the $F_{II}$ which are$\pi/4$ and $3\pi/4$.

(4) The effect of the boundary on the normalized stress intensity factors.

![](./images/812578055485652992_14.jpg)

Fig. 13. The normalized stress intensity factors vs $D/R$.

![](./images/812578055485652992_15.jpg)

Fig. 14. The normalized stress intensity factors vs $\varphi$.

The normalized stress intensity factors vary with the increase of $W/R$ is studied as shown in Fig. 15 under the condition: $H = W$,
$R = a$, $D = 3R$ and $\varphi = \pi/4$.

As can be seen in Fig. 15, the normalized stress intensity factors decrease with the increase of the length of the plate. However,
when $W/D$ is larger than 20, the boundary effect almost vanish and the result should agree very well with that of an infinite plate.

![](./images/812578055485652992_16.jpg)

Fig. 15. The effect of the boundary on the normalized stress intensity factors.

![](./images/812578055485652992_17.jpg)

Fig. 16. A circular plate containing eight inclusions and four crossed cracks subjected to $\Delta T$.

### 4.2. Multiple inclusions and cracks problem

A circular plate with the radius $R$ containing eight equally distributed circular inclusions and four crossed cracks under a uniform temperature change is presented in this example. As shown in Fig. 16, four crossed cracks with the length of $2a$ are equally located at center of the circular plate. The distances between the centers of the inclusions and cracks are denoted by $L$. The mode I normalized stress intensity factor of point A is studied here.

In this example, the boundary can be divided into a kinked crack containing $N_b$ segments end to end. When $N_b$ is big enough, it will approach a very good solution. Thus, the effect of $N_b$ is investigated first under the following condition:
$R = 10r$, $a = r$ $L = 4r$ and $\mu_1/\mu = 100$.

The number of segments is chosen to be 4–80. And the variation of the result is shown in Fig. 17.

As we can see from Fig. 17, the boundary actually doesn't need to be divided into a lot number of segments. When $N_b$ is larger than 20, the result is almost invariant which means the solution is accurate enough.

Now we study the change of the normalized stress intensity factor with the increase of $a/R$ shown in Fig. 18 when the following condition is fixed: $R = 10r$, $L = 8r$ and $\mu_1/\mu = 100$.

As can be seen in Fig. 18, the normalized stress intensity factor increases with the increase of $a/R$. From this example, we can see that the presented method is very convenient to study the interaction of multiple cracks and inclusions in a finite plate subjected to a temperature change.

Here we need to mention that the presented method has its advantage of solving problem of multiple cracks. However, if nu- merous or even countless cracks are involved, further study combined with other methods such as research [27] is still needed to

![](./images/812578055485652992_18.jpg)

Fig. 17. Effect of the number of the boundary divided on the solution.

![](./images/812578055485652992_19.jpg)

Fig. 18. The normalized stress intensity factors vs $a/R$.

develop in the future.

## 5. Conclusion

In this study, a numerical method to study the interaction of multiple cracks and inclusions in a finite plate subjected a uniform temperature change is provided. The presented method utilizes the advantage of both the equivalent inclusion method and dis- tributed dislocation method. It is efficient in solving multiple cracks problems. The high accuracy and efficiency of the presented method are verified by the FEA. A couple of numerical examples are presented to investigate the effects of some parameters of the boundary and inclusion on the normalized stress intensity factors of the cracks.

### Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgments

This work was financially supported by National Natural Science Foundation of China (No. 51802229) and Natural Science Foundation of Guangdong Province (No. 2018A030313430 and No. 2018A030313561) and innovation and strong school engineering Foundation of Guangdong Province (No. 2017KQNCX201, No. 2017KQNCX186 and No. 2018KZDXM072).

### References

[1] Frenchko YS. Effect of a stationary temperature field on the stressed state of a plane with a foreign inclusion and a crack. Mat Met Fiz-Mekh Polya 1975;1:160-4.
[2] Herrmann KP, Wang R. Interaction of a crack with a circular inclusion in a thermally stressed material. J Appl Math Mech 1995;75(4):295-300.
[3] Wang R, Hasebe N. The interacting stress field around a composite crack with a misfitting inclusion. Int J Fracture 1996;81:163-70.
[4] Herrmann KP, Wang R. The stress field around a tensile crack interacting with a circular inclusion in a thermally stressed material. Mech Res Commun 1995;22:387-93.
[5] Chernyak MS. Interaction of a crack with a cylindrical inclusion in heating and tension of a body. J Math Sci 2010;171(5):682-91.
[6] Saebom L, Seung TC, Youn YE, Dae YC. Stress intensity factors and kink angle of a crack interacting with a circular inclusion under remote mechanical and thermal loadings. J Mech Sci Technol 2003;17:1120-32.
[7] Peng B, Feng ML, Fan JQ. Study on the crack-inclusion interaction with coupled mechanical and thermal strains. Theor Appl Fract Mec 2015;75:39-43.
[8] Peng B, Feng ML. Study on the plane stress mode II crack-inclusion interaction with coupled mechanical and thermal strains. Arch Appl Mech 2015;85:725-33.
[9] Chen WF, Peng B, Wang FH, Feng ML. Crack-inclusion interaction due to mismatched thermal expansion under plane stress condition. Meccanica 2016;51:2225-33.
[10] Zhang YY, Guo LC, Huang K, Bai XM, Pang JC, Zhang ZF. A numerical method for the thermal-shock crack problems of nonhomogeneous materials with inclusions based on an interaction energy integral method. Eng Fract Mech 2018;190:159-74.
[11] Eshelby JD. The determination of the elastic field of an ellipsoidal inclusion and related problems. Proc. R. Soc. Lond. Ser 1957;A 241:376-96.
[12] Eshelby JD. Elastic inclusion and inhomogeneities. Amsterdam 1961.
[13] Jin XQ, Wang ZJ, Zhou QH, Keer LM, Wang Q. On the solution of an elliptical inhomogeneity in plane elasticity by the equivalent inclusion method. J Elastity 2014;114:1-18.
[14] Mura T. Micromechanics of defects in solids. Springer Science & Business Media; 2013.
[15] Moschovidis ZA, Mura T. Two-Ellipsoidal inhomogeneities by the equivalent inclusion method. J Appl Mech 1975;42:847-52.
[16] Hills DA, Kelly PA, Dai DN, Korsunsky AM. Solution of crack problems-the distributed dislocation. Kluwer Academic Publishers; 1996.
[17] Weertman JH. Dislocation based fracture mechanics. Singapore: World Scientific; 1996.
[18] Hills DA, Comninou M. A normally loaded half plane with an edge crack. Int J Solids Struct 1985;21:399-410.
[19] Jin XQ, Keer LM. Solution of multiple edge cracks in an elastic plane. Int J Fract 2006;137:121-37.
[20] Li XT, Yang HD, Zan XD, Li X, Jiang XY. Effect of a micro-crack on the kinked macro-crack. Theor Appl Fract Mec 2018;96:468-75.
[21] Li XT, Li X, Jiang XY. Influence of a micro-crack on the finite macro-crack. Eng Fract Mech 2017;177:95-103.

[22] Hallback N, Tofique MW. Development of a distributed dislocation dipole technique for the analysis of multiple straight, kinked and branched cracks in an elastic half-plane. Int J Solids Struct 2014;51:2878-92.

[23] Dai DN. Modeling cracks in finite bodies by distributed dislocation dipoles. Fatigue Fract Eng M 2002;25:27-39.

[24] Zhang J, Qu Z, Huang QQ. Solution of multiple cracks in a finite plane of an elastic isotropic material with the distributed dislocation method. Acta Mech Solida Sin 2014;27:276-83.

[25] Boukellif R, Ricoeur A. Identification of crack parameters and stress intensity factors in finite and semi-infinite planes solving inverse problems of linear elasticity. Acta Mech 2020;231:795-813.

[26] Erdogan F, GuptaGD, Cook TS. Numerical solution of singular integral equations. In: Sih GC, editor. Methods of analysis and solutions of crack problems. Noordhoff, Leyden; 1973.

[27] Feng XQ, Li JY, Yu SW. A simple method for calculating interaction of numerous microcracks and its applications. Int J Solids Struct 2003;40:447-64.