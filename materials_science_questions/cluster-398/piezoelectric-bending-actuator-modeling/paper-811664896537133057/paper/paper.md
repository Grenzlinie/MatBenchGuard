# DETERMINATION OF MECHANICAL AND ELECTRICAL DAMAGES OF PIEZOELECTRIC MATERIAL WITH PERIODICALLY DISTRIBUTED MICROVOIDS

X. H. Yang $^*$ G. W. Zeng $^{**}$ C. Y. Chen $^{*}$

Department of Mechanics
Huazhong University of Science and Technology
Wuhan, 430074, China

## ABSTRACT

This paper emphasizes on determining the mechanical and electrical damages of piezoelectric ceramics with periodically distributed ellipsoidal or spherical microvoids. Based on the unit cell method, detailed three-dimensional finite element analyses are carried out to acquire the effective electromechanical properties of voided PZT-7A materials, and then the mechanical and electrical damages are determined through the relations between the damage variables and the effective properties in the continuum piezoelectric damage constitutive theory. The quantitative connections between the damages and microstructure parameters, including the microvoid volume fraction and the microvoid aspect ratio, are analyzed in detail. Some interesting conclusions are obtained.

Keywords : Piezoelectric ceramics, Mechanical and electrical damages, Microvoid, Unit cell method.

## 1. INTRODUCTION

Piezoelectric materials are increasingly becoming important both in the microelectronics industry and the emerging field of microelectromechanical systems (MEMS). Just like most of engineering materials, they are generally treated as linear and homogeneous in design, although they are actually nonlinear and inhomogeneous because of large numbers of microstructures, such as microvoids and microcracks, existing inside them. This is not appropriate for predicting lifetime of piezoelectric devices. In order to evaluate microstructure effects, all kinds of homogenization micromechanics methods, including the dilute, self-consistent, Mori-Tanaka, differential approximation and representative volume element, were extended to piezoelectric materials with defects. They are capable of determination of effective properties such as the conductivity, electroelastic moduli, thermal expansion and pyroelectric coefficients affected by the microstructures. Qin et al [1] pointed out that the dilute and Mori-Tanaka techniques can explicitly estimate the effective thermoelectroelastic moduli while the self-consistent and differential scheme can give only implicit estimates, and the behavior of each of the four micromechanics models was examined for a particular cracked material. Li et al [2] investigated the inherent relations between the effective properties and the non-uniform distributions of microscopic electromechanical coupling fields resulting from microvoids by carrying out three-dimensional (3-D) finite element analyses based on the unit cell method. Accounting for the interaction between inclusions and matrix, Wu [3] adopted a unified micromechanics approach to examine the electroelastic properties of piezoelectric materials containing voids. Influences of the volume fraction and aspect ratio of voids on the material properties were studied based on PZT-5H and $BaTiO_3$.

Microstructures in piezoelectric ceramics inevitably grow under combined mechanical and electrical loads, so that the nonlinearities occur. In order to analyze electromechanical behaviors of piezoelectric materials reasonably, it is necessary to set up a constitutive model which can reflect the dependence of material properties on both mechanical and electrical loads. Regarding piezoelectric ceramics as a class of mechanically brittle and electrically ductile solids, Gao et al [4] put forward a strip saturation model analogous with the classical Dugdale model for plastic yielding, in which electrical displacement is assumed to yield when electric field is up to its linear limit. Yang and Zhu [5] thought that piezoelectric nonlinearity comes from domain switching, so they proposed a small-scale domain-switching model to explain the toughening mechanism. Fulton and Gao [6] introduced a electrical nonlinearity model based on piezoelectric microstructure. They simulated the polarization switching and saturation in ferroelectrics by using a collection of discrete electric dipoles superimposed on a medium satisfying the linear piezoelectric constitutive law, and then derived a local crack driving force which generates a qualitative match to experimental observations. Based on the field limiting space charge model, Zhang et al [7] proposed a charge-free

* Professor ** Graduate student

---

Journal of Mechanics, Vol. 23, No. 3, September 2007

zone model, and estimated the electric field at the tip of an electrically conductive crack according to the electric field intensity factor. Assuming that the electric field in a strip ahead of the crack tip is equal to the dielectric breakdown strength, Zhang et al [8] developed a strip dielectric breakdown model, which is similar to the strip saturation model proposed by Gao et al [4]. In the above models, only electrical nonlinearity is considered. However, the experimental results [9] demonstrated that in addition to the nonlinearities in the relationships of polarization versus electric field and strain versus electric field, the stress-strain curves are nonlinear. Accordingly, by introducing the mechanical damage variable tensor to depict the anisotropic degeneration of elastic property of piezoelectric materials and the electrical damage variable tensor to represent the degeneration of dielectric property from the continuum damage mechanics, we proposed a piezoelectric damage constitutive model involving both mechanical and electrical nonlinearities in our previous work [10,11].

It is well known that damage degree depends on microstructure geometry, microstructure density, microstructure interactions, etc. The phenomenological damage tensors in continuum damage theory can be connected with microstructure parameters by the aforementioned micromechanics methods. This paper places the emphasis on the quantitative connections between damages and microstructure parameters. Based on the unit cell method, detailed three-dimensional finite element analyses of piezoelectric ceramics PZT-7A with periodically distributed ellipsoidal and spherical microvoids are carried out to evaluate the mechanical and electrical damages. The influences of the void volume fraction and the void aspect ratio on the damages are discussed in detail.

## 2. PIEZOELECTRIC DAMAGE CONSTITUTIVE MODEL

Defining the effective electroelastic moduli and conductivity, Qin et al [1] gave a constitutive model for thermopiezoelectric cracked solids. Analogous to their work, we assumed that damaged thermopiezoelectric solids have the following constitutive equations [11].

$$
\begin{aligned}
\sigma_{i j} & =\tilde{c}_{i j k l} \varepsilon_{k l}-\tilde{e}_{k i j} E_{k}-\tilde{\gamma}_{i j} \theta, \\
D_{i} & =\tilde{e}_{i k l} \varepsilon_{k l}+\tilde{\lambda}_{i k} E_{k}+\tilde{\chi}_{i} \theta
\end{aligned}
\tag{1}
$$

where $\boldsymbol{\sigma}$, $\boldsymbol{\varepsilon}$, $\mathbf{D}$, $\mathbf{E}$ and $\theta$ are spatial average values of stress tensor, strain tensor, electric displacement vector, electric field vector, and temperature increment in a material element, and $\tilde{\mathbf{c}}$, $\tilde{\mathbf{e}}$, $\tilde{\lambda}$, $\tilde{\gamma}$, and $\tilde{\chi}$ are its effective elastic, piezoelectric, dielectric, thermal stress coefficient tensors, and pyroelectric coefficient vector, respectively, which are dependent on the mechanical and electrical damages. For a constant temperature [10], Eq. (1) can be simplified into

$$
\begin{aligned}
\sigma_{i j} & =\tilde{c}_{i j k l} \varepsilon_{k l}-\tilde{e}_{k i j} E_{k}, \\
D_{i} & =\tilde{e}_{i k l} \varepsilon_{k l}+\tilde{\lambda}_{i k} E_{k}.
\end{aligned}
\tag{2}
$$

Applying the theorem of energy equivalence, the effective properties were connected with the undamaged ones through the mechanical and electrical continuum tensors $\boldsymbol{\omega}$ and $\mathbf{G}$ as follows.

$$
\begin{aligned}
\tilde{c}_{i j m n} & =\frac{1}{4}\left(\omega_{k i} \delta_{l j}+\delta_{k i} \omega_{l j}\right)\left(\omega_{o m} \delta_{p n}+\delta_{o m} \omega_{p n}\right) c_{k l o p}, \\
\tilde{e}_{i m n} & =\frac{1}{2}\left(\omega_{k m} \delta_{l n}+\delta_{k m} \omega_{l n}\right) G_{j i} e_{j k l}, \\
\tilde{\lambda}_{i l} & =G_{j i} G_{k l} \lambda_{j k}.
\end{aligned}
\tag{3}
$$

in which $\mathbf{c}$, $\mathbf{e}$, and $\boldsymbol{\lambda}$ are the undamaged elastic, piezoelectric, dielectric, thermal stress constant tensors. The mechanical and electrical damage variables $\mathbf{D}^{\mathrm{M}}$ and $\mathbf{D}^{\mathrm{E}}$, which characterize damage degree of the material element, can be expressed in terms of the continuum tensors as

$$
\begin{aligned}
& D_{i j}^{\mathrm{M}}=\delta_{i j}-\omega_{i k} \omega_{k j}, \\
& D_{i j}^{\mathrm{E}}=\delta_{i j}-G_{i k} G_{k j}.
\end{aligned}
\tag{4}
$$

Since polarized piezoelectric ceramics are transversely isotropic, their material constant matrices $[c]$, $[e]^{\mathrm{T}}$, and $[\lambda]$ with $x_{3}$ as the poling direction and $x_{1}-x_{2}$ as the isotropic plane can be expressed as

$$
\left[\begin{array}{cccccc}
c_{11} & c_{12} & c_{13} & 0 & 0 & 0 \\
c_{12} & c_{11} & c_{13} & 0 & 0 & 0 \\
c_{13} & c_{13} & c_{33} & 0 & 0 & 0 \\
0 & 0 & 0 & c_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & c_{44} & 0 \\
0 & 0 & 0 & 0 & 0 & c_{66}
\end{array}\right],
\quad\left[\begin{array}{ccc}
0 & 0 & e_{31} \\
0 & 0 & e_{31} \\
0 & 0 & e_{33} \\
0 & e_{15} & 0 \\
e_{15} & 0 & 0 \\
0 & 0 & 0
\end{array}\right], \quad\left[\begin{array}{ccc}
\lambda_{11} & 0 & 0 \\
0 & \lambda_{11} & 0 \\
0 & 0 & \lambda_{33}
\end{array}\right].
\tag{5}
$$

in which, $c_{66}=\frac{1}{2}\left(c_{11}-c_{12}\right)$. If it is assumed that the transversely isotropic piezoelectric damages with the same principal axis system as the material properties occur inside the element, its effective constant matrices $[\tilde{c}]$, $[\tilde{e}]^{\mathrm{T}}$, and $[\tilde{\lambda}]$ can be written as


$$
\left[\begin{array}{cccccc}
\tilde{c}_{11} & \tilde{c}_{12} & \tilde{c}_{13} & 0 & 0 & 0 \\
\tilde{c}_{12} & \tilde{c}_{11} & \tilde{c}_{13} & 0 & 0 & 0 \\
\tilde{c}_{13} & \tilde{c}_{13} & \tilde{c}_{33} & 0 & 0 & 0 \\
0 & 0 & 0 & \tilde{c}_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & \tilde{c}_{44} & 0 \\
0 & 0 & 0 & 0 & 0 & \tilde{c}_{66}
\end{array}\right],
$$

$$
\left[\begin{array}{ccc}
0 & 0 & \tilde{e}_{31} \\
0 & 0 & \tilde{e}_{31} \\
0 & 0 & \tilde{e}_{33} \\
0 & \tilde{e}_{15} & 0 \\
\tilde{e}_{15} & 0 & 0 \\
0 & 0 & 0
\end{array}\right], \quad\left[\begin{array}{ccc}
\tilde{\lambda}_{11} & 0 & 0 \\
0 & \tilde{\lambda}_{11} & 0 \\
0 & 0 & \tilde{\lambda}_{33}
\end{array}\right].
\tag{6}
$$

Incorporating two equations in Eq. (2) leads to

$$
\left\{\begin{array}{l}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{33} \\
\sigma_{32} \\
\sigma_{31} \\
\sigma_{12} \\
D_{1} \\
D_{2} \\
D_{3}
\end{array}\right\}=\left[\begin{array}{ccccccccc}
\tilde{c}_{11} & \tilde{c}_{12} & \tilde{c}_{13} & 0 & 0 & 0 & 0 & 0 & -\tilde{e}_{31} \\
\tilde{c}_{12} & \tilde{c}_{11} & \tilde{c}_{13} & 0 & 0 & 0 & 0 & 0 & -\tilde{e}_{31} \\
\tilde{c}_{13} & \tilde{c}_{13} & \tilde{c}_{33} & 0 & 0 & 0 & 0 & 0 & -\tilde{e}_{33} \\
0 & 0 & 0 & \tilde{c}_{44} & 0 & 0 & 0 & -\tilde{e}_{15} & 0 \\
0 & 0 & 0 & 0 & \tilde{c}_{44} & 0 & -\tilde{e}_{15} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & \tilde{c}_{66} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & \tilde{e}_{15} & 0 & \tilde{\lambda}_{11} & 0 & 0 \\
0 & 0 & 0 & \tilde{e}_{15} & 0 & 0 & 0 & \tilde{\lambda}_{11} & 0 \\
\tilde{e}_{31} & \tilde{e}_{31} & \tilde{e}_{33} & 0 & 0 & 0 & 0 & 0 & \tilde{\lambda}_{33}
\end{array}\right]\left\{\begin{array}{c}
\varepsilon_{11} \\
\varepsilon_{22} \\
\varepsilon_{33} \\
\varepsilon_{32} \\
\varepsilon_{31} \\
\varepsilon_{12} \\
E_{1} \\
E_{2} \\
E_{3}
\end{array}\right\}
\tag{7}
$$

It can be derived from Eq. (3) that

$$
\begin{aligned}
& \tilde{c}_{11}=\omega_{11}^{2} c_{11}, \quad \tilde{c}_{12}=\omega_{11}^{2} c_{12}, \quad \tilde{c}_{13}=\omega_{11} \omega_{33} c_{13}, \\
& \tilde{c}_{33}=\omega_{33}^{2} c_{33}, \quad \tilde{c}_{44}=\frac{1}{4}\left(\omega_{11}+\omega_{33}\right)^{2} c_{44}, \quad \tilde{c}_{66}=\omega_{11}^{2} c_{66}, \\
& \tilde{e}_{31}=\omega_{11} G_{33} e_{31}, \quad \tilde{e}_{33}=\omega_{33} G_{33} e_{33}, \quad \tilde{e}_{15}=\frac{1}{2}\left(\omega_{11}+\omega_{33}\right) G_{11} e_{15}, \\
& \tilde{\lambda}_{11}=G_{11}^{2} \lambda_{11}, \quad \tilde{\lambda}_{33}=G_{33}^{2} \lambda_{33}.
\end{aligned}
\tag{8}
$$

Equation (4) can be simplified into

$$
\begin{aligned}
& D_{11}^{\mathrm{M}}=D_{22}^{\mathrm{M}}=1-\omega_{11}^{2}, \quad D_{33}^{\mathrm{M}}=1-\omega_{33}^{2}, \quad D_{12}^{\mathrm{M}}=D_{13}^{\mathrm{M}}=D_{23}^{\mathrm{M}}=0, \\
& D_{11}^{\mathrm{E}}=D_{22}^{\mathrm{E}}=1-G_{11}^{2}, \quad D_{33}^{\mathrm{E}}=1-G_{33}^{2}, \quad D_{12}^{\mathrm{E}}=D_{13}^{\mathrm{E}}=D_{23}^{\mathrm{E}}=0,
\end{aligned}
\tag{9}
$$

and Eq. (8) leads to

$$
\omega_{11}=\sqrt{\frac{\tilde{c}_{11}}{c_{11}}}=\sqrt{\frac{\tilde{c}_{12}}{c_{12}}}, \quad \omega_{33}=\sqrt{\frac{\tilde{c}_{33}}{c_{33}}}, \quad G_{11}=\sqrt{\frac{\tilde{\lambda}_{11}}{\lambda_{11}}}, \quad G_{33}=\sqrt{\frac{\tilde{\lambda}_{33}}{\lambda_{33}}}.
\tag{10}
$$

Combining Eqs. (9) and (10) yields

$$
\begin{aligned}
& D_{11}^{\mathrm{M}}=D_{22}^{\mathrm{M}}=1-\frac{\tilde{c}_{11}}{c_{11}}=1-\frac{\tilde{c}_{12}}{c_{12}}, \quad D_{33}^{\mathrm{M}}=1-\frac{\tilde{c}_{11}}{c_{11}}, \\
& D_{11}^{\mathrm{E}}=D_{22}^{\mathrm{E}}=1-\frac{\tilde{\lambda}_{11}}{\lambda_{11}}, \quad D_{33}^{\mathrm{E}}=1-\frac{\tilde{\lambda}_{33}}{\lambda_{33}}.
\end{aligned}
\tag{11}
$$

Equation (11) reveals a way to determine quantitative connections between the mechanical and electrical damages and microstructure parameters, because the effective properties of the damaged material element can be calculated by means of the aforementioned micromechanical mechanics methods.

### 3. COMPUTATIONAL MODEL AND METHOD

In this investigation, the piezoelectric material is assumed to be PZT-7A ceramics. Many ellipsoidal or spherical insulating microvoids are periodically distributed in the simple cubic, shown in Fig. 1(a). Its polarized direction is parallel to the long axis of the void. The material constants are listed in Tab. 1. With the help of the unit cell method, the damages are quantitatively analyzed. A unit cell is a smallest periodical unit which contains sufficient information on the geometrical and material parameters at the microscopic level. The rectangular coordinate system $(x_1, x_2, x_3)$ with the origin at the cell center is adopted. Considering the symmetry, only quarter of the cell model, namely the region of $x_1 \geq 0, x_2 \geq 0$, and $x_3 \geq 0$ (see Fig. 1(b)), is analyzed, so that the displacement boundary conditions can be described as

$$
\begin{aligned}
& U_{1}=0, \quad \text { for } x_{1}=0, \\
& U_{2}=0, \quad \text { for } x_{2}=0, \\
& U_{3}=0, \quad \text { for } x_{3}=0.
\end{aligned}
\tag{12}
$$

The three-dimensional 8-node piezoelectric brick element Solid5 in ANSYS is used for discretizing the model into 6048 elements with displacement and electrical potential as degrees of freedom. Different loading and boundary conditions are imposed in order to evaluate the effective properties [2]. For example, we can apply the displacement degree of freedom $U_{x_{1}=1}$ on the boundary planes $x_1=1$ or $U_{x_{3}=1}$ on the planes $x_3=1$, in order to evaluate the elastic constant $\tilde{c}_{11}$ from Eq. (7) by

$$
\begin{aligned}
& E_{1}=E_{2}=E_{3}=0, \quad \varepsilon_{22}=\varepsilon_{33}=0, \quad \varepsilon_{11} \neq 0, \\
& \tilde{c}_{11}=\frac{\sigma_{11}}{\varepsilon_{11}} \approx \frac{Q_{x_{1}=1}}{U_{x_{1}=1}},
\end{aligned}
\tag{13}
$$

![](./images/811664896537133057_1.jpg)

(a) PZT-7A with periodically distributed microvoids

![](./images/811664896537133057_2.jpg)

(b) Quarter of the cell model

Fig. 1 Unit cell model and its coordinate system

or $\tilde{c}_{33}$ by

$$
\begin{aligned}
& E_{1}=E_{2}=E_{3}=0, \quad \varepsilon_{11}=\varepsilon_{22}=0, \\
& \varepsilon_{33} \neq 0, \quad \tilde{c}_{33}=\frac{\sigma_{33}}{\varepsilon_{33}} \approx \frac{Q_{x_{3}=1}}{U_{x_{3}=1}}.
\end{aligned}
\tag{14}
$$

In the above two expressions, $Q_{x_{1}=1}$ and $Q_{x_{3}=1}$ are the active forces on the planes $x_{1=1}$ and $x_{3=1}$ respectively. When we impose only the electric field $E_{2}$ along the $x_{2^{-}}$ direction through applying the voltage degree of freedom $V_{x_{2}=1}$ on the plane $x_{2=1}$ and $V_{x_{2}=0}$ on the plane $x_{2=0}$ of the cubic cell, we have $D_{2}=\tilde{e}_{15} \varepsilon_{32}+\tilde{\lambda}_{33} E_{2}$, so that the dielectric constant $\tilde{\lambda}_{11}$ can be evaluated as

$$
\begin{aligned}
& E_{1}=E_{3}=0, E_{2} \neq 0, \varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=\varepsilon_{32}=0, \\
& \tilde{\lambda}_{11}=\frac{D_{2}}{E_{2}} \approx \frac{D_{x_{2}=1}}{V_{x_{2}=1}-V_{x_{2}=0}}
\end{aligned}
\tag{15}
$$

Applying the voltage degree of freedom $V_{x_{3}=1}$ on the plane $x_{3}=1$ and $V_{x_{3}=0}$ on the plane $x_{3}=0$ of the cubic cell, we can get the dielectric constant $\tilde{\lambda}_{33}$ by

$$
\begin{aligned}
& E_{1}=E_{2}=0, E_{3} \neq 0, \varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=0, \\
& \tilde{\lambda}_{33}=\frac{D_{3}}{E_{3}} \approx \frac{D_{x_{3}=1}}{V_{x_{3}=1}-V_{x_{3}=0}}
\end{aligned}
\tag{16}
$$

In the above two expressions, $D_{x_{2}=1}$ and $D_{x_{3}=1}$ are the average components of electric flux density on the planes $x_{2}=1$ and $x_{3}=1$ respectively. Further, the mechanical and electrical damages can be determined in accordance with Eq. (11).

Similarly, we can evaluate the piezoelectric coefficients by

$$
\begin{aligned}
& E_{3} \neq 0, \varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=0, \\
& \tilde{e}_{13}=-\frac{\sigma_{11}}{E_{3}} \approx-\frac{F_{x_{1}=1}}{V_{x_{3}=1}-V_{x_{3}=0}} ; \tilde{e}_{33}=-\frac{\sigma_{11}}{E_{3}} \approx-\frac{F_{x_{3}=1}}{V_{x_{3}=1}-V_{x_{3}=0}}
\end{aligned}
\tag{17}
$$

and

$$
\begin{aligned}
& E_{2} \neq 0, \varepsilon_{11}=\varepsilon_{22}=\varepsilon_{33}=\varepsilon_{32}=0, \\
& \tilde{e}_{15}=-\frac{\sigma_{32}}{E_{2}} \approx \frac{F_{x_{2}=1}}{V_{x_{2}=1}-V_{x_{2}=0}}
\end{aligned}
\tag{18}
$$

In the above two expressions, $F_{x_{1}=1}, F_{x_{2}=1}$ and $F_{x_{3}=1}$ are the reactive forces on the planes $x_{1}=1, x_{2}=1$ and $x_{3}$ $=1$, respectively. On the other hand, according to the obtained mechanical and electrical damage components, the piezoelectric coefficients can be also obtained from Eq. (8). By comparison of these results from the above two kinds of methods, rationality of the hypothesis of the transversely isotropic damage can be checked.

## 4. RESULT ANALYSIS

In the unit cell, the ellipsoidal void geometry is characterized by its shape and size. The void size is characterized by the volume fraction $f=V_{v} / V_{m}$, where $V_{v}$ and $V_{m}$ are respectively the void and matrix volumes, and its shape is characterized by the aspect ratio $S=b / a$, where $a$ and $b$ are respectively the minor and major semi-axes of the void. As important structural parameters of microvoids, the void volume fraction $f$ and the void aspect ratio $S$ play important roles in macroscopic electromechanical behavior of the voided piezoelectric solid. In the following, their influences on the mechanical and electrical damages are investigated carefully.

First, the influences of the void volume fraction $f$ on the damages are analyzed. Assuming that the insulating void is spherical, namely fixing the void aspect ratio

$S$ on 1.0 and varying the void volume fraction $f$ from 0 to $32.1\%$, we calculate the mechanical and electrical damages according to the presented method in section 3. Variation of the damages with the void volume fraction $f$ is drawn in Fig. 2(a). Both the mechanical and electrical damages increase with the increasing void volume fraction $f$. Moreover, the curves of $D_{11}^{M}$ and $D_{33}^{M}$ are in superposition, which reveals that the mechanical damage induced by spherical voids is isotropic. This is in good agreement with our knowledge.

Second, the influences of the void aspect ratio $S$ on the damages are observed. The void volume fraction $f$ is fixed on $6.54\%$ and the void aspect ratio $S$ varies from 0.3 to 2.0. The longitudinal void cross-section area fraction can be expressed by $A_{3}=(3 f \sqrt{\pi} / 4 S)^{\frac{2}{3}}$ and the transverse void cross-section area fraction by $A_{1}=A_{2}=(3 f \sqrt{\pi S} / 4)^{\frac{2}{3}}$. Fig. 2(b) plots the variation curves of the damages with the void aspect ratio $S$. While $D_{33}^{M}$ go down rapidly in forepart but slowly afterward with increasing the void aspect ratio $S$, $D_{11}^{M}$ always goes up slowly. This is understandable because $A_{3}$ decreases but $A_{1}$ or $A_{2}$ increases with the increasing void aspect ratio $S$ for a fixed void volume fraction $f$. Nevertheless, $D_{11}^{E}$ and $D_{33}^{E}$ hardly change. It is shown that the electrical damage components are nearly independent of the void aspect ratio $S$. In a word, the void aspect ratio $S$ has complex effect on damages.

In succession, the effective piezoelectric coefficients are calculated from Eq. (8) and from Eqs. (17) or (18), respectively, and the results are drawn in the same figures. Fig. 3(a) and (b) give variation curves of the effective piezoelectric coefficients with the void volume fraction and the void aspect ratio. Apparently, the results from the two methods nearly approximate each other. So it can be said that the hypothesis of the transversely isotropic damage is reasonable for the analyzed piezoelectric solid with voids.

### 5. CONCLUSIONS

By applying the unit cell model, detailed three-dimensional finite element investigations on mechanical and electrical damages of piezoelectric ceramics with periodically distributed ellipsoidal microvoids are implemented, and quantitative connections of the damages with the microvoid structural parameters are analyzed. The following conclusions have been given: (1) Both the mechanical and electrical damages increase with increasing the void volume fraction, and the mechanical damage caused by spherical voids is isotropic. (2) The void shape ratio has complex influences on the mechanical damage components but hardly changes the electrical damage. (3) The hypothesis of the transversely isotropic damage can be approximately satisfied

![](./images/811664896537133057_3.jpg)

Fig. 2 Variation curves of mechanical and electrical damages with (a) the void volume fraction and (b) the void aspect ratio

![](./images/811664896537133057_4.jpg)

Fig. 3 Variation curves of effective piezoelectric coefficients with (a) the void volume fraction and (b) the void aspect ratio

for the piezoelectric solid with periodically distributed ellipsoidal or spherical voids.

## ACKNOWLEDGEMENTS

This work is supported by the National Natural Science Foundation of China (No. 10172036).

## REFERENCES

1. Qin, Q. H., Mai Y. W. and Yu S. W., "Effective Moduli for Thermopiezoelectric Materials with Microcracks," *Int. J. Fracture*, 91, pp. 359-371 (1998).
2. Li Z. H., Wang C. and Chen C. Y., "Effective Electro- mechanical Properties of Transversely Isotropic Piezo- electric Ceramics with Microvoids," *Computational Materials Science*, 27, pp. 381-392 (2003).
3. Wu T. L., "Micromechanics Determination of Electroe- lastic Properties of Piezoelectric Materials Containing Voids," *Materials Science and Engineering A*, 280, pp. 320-327 (2000).
4. Gao H., Zhang T. Y. and Tong P., "Local and Global Energy Release Rates for an Electrically Yielded Crack in a Piezoelectric Ceramic," *J. Mechanics and Physics of Solids*, 45, pp. 491-510 (1997).

5. Yang W. and Zhu T., "Switch-Toughening of Ferroelec- trics Subjected to Electric Field," *J. Mechanics and Physics of Solids*, 46, pp. 291-311 (1998).
6. Fulton C. C. and Gao H., "Effect of Local Polarization Switching on Piezoelectric Fracture," *J. Mechanics and Physics of Solids*, 49, pp. 927-952 (2001).
7. Zhang T. Y., Wang T. H. and Zhao M. H., "Failure Be- havior and Failure Criterion of Conductive Cracks (Deep Notches) in Thermally Depoled PZT-4 Ceram- ics," *Acta Materialia*, 51, pp. 4881-4895 (2003).
8. Zhang T. Y., Zhao M. H. and Gao C. F., "The Strip Di- electric Breakdown Model," *Int. J. Fracture*, 132, pp. 311-327 (2005).
9. Zhang T. Y. and Gao C. F., "Fracture Behaviors of Piezoelectric Materials," *Theoretical and Applied Fracture Mechanics*, 41, pp. 339-379 (2004).
10. Yang X. H., Chen C. Y., Hu Y. T. and Wang C., "Dam- age Analysis and Fracture Criteria for Piezoelectric Ceramics," *Int. J. Non-Linear Mechanics*, 40, pp. 1204-1213 (2005).
11. Yang X. H., Zhang Y., Hu Y. T. and Chen C. Y., "Con- tinuum Damage Mechanics for Thermo-PiezoelectricMaterials," *Journal of Mechanics*, 22, pp. 93-98(2006).

(Manuscript received August 14, 2006,accepted for publication November 22, 2006.)