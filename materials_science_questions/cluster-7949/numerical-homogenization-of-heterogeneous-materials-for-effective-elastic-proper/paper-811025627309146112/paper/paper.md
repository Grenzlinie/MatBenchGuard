![](./images/811025627309146112_1.jpg)

Composites: Part B 32 (2001) 185-197

![](./images/811025627309146112_2.jpg)

www.elsevier.com/locate/compositesb

# An energetic homogenisation procedure for the elastic properties of general cellular sandwich cores

J. Hohe*, W. Becker

Universität Siegen, Institut für Mechanik und Regelungstechnik, Paul-Bonatz-Str. 9-11, D-57068 Siegen, Germany

## Abstract
The present study provides a general procedure for the determination of the effective elastic properties of two-dimensional cellular sandwich cores with arbitrary cell topology and geometry. The scheme uses a strain energy-based representative volume element procedure assuming that macroscopically equivalent strain states have to cause the same strain energy in a representative volume element whether the real microstructure or the "effective" homogenised medium is considered. The strain energy can be evaluated either by analytical or pure numerical methods. Both approaches agree well in a number of examples considering different sandwich core geometries. © 2001 Elsevier Science Ltd. All rights reserved.

Keywords: C: Finite element analysis (FEA); Cellular material

---

## 1. Introduction
Structural sandwich panels are a widespread means of lightweight construction, especially in the aerospace industry, since the principle of sandwich construction enables the design of plates and shells with high bending stiffness at very low weight. A classical sandwich shell consists of three layers: two face sheets made of a homogeneous material bonded to a low-density core which is typically made from a two-dimensional cellular material (see Fig. 1). Within the concept of sandwich construction, the core is used to stabilise the face sheets and has to carry the transverse shear loads.

For reasons of numerical efficiency, the analysis of structural sandwich panels is usually performed in terms of effective properties rather than by analysis of the real microstructure. Therefore, the cellular material forming the core has to be homogenised. Since the pioneering work by Kelsey et al. [1] and Chang and Ebcioglu [2] appeared, numerous studies on the effective properties of cellular sandwich cores have been published (e.g. Gibson and Ashby [3], Noor et al. [4]). Nevertheless, most of these studies are specialised to few specific cell geometries. Only few analyses are concerned with the non-orthotropic case (e.g. Overaker et al. [5]) or cellular media with more general topologies. To the authors' knowledge, no comprehensive analysis is available, which considers the case of general two-dimensional cellular media.

For the homogenisation of cellular materials, several methods have been proposed. Most of the early studies simply redistribute stress and strain along the boundaries of a representative volume element [1,2]. Other studies employ energetic considerations as the classical approach by Bishop and Hill [6]. In addition, some rigorous mathematical theories as the variational approaches by Hashin and Shtrikman [7] or the two-scale expansion approach by, e.g. Sanchez-Palencia [8] are also available.

The present study uses a strain energy-based concept for homogenisation of the microstructure, assuming that macroscopically equivalent strain states have to cause the same strain energy in a representative volume element consisting of the real microstructure or the effective medium. The method has successfully been applied in earlier studies by the present authors concerning special core geometries [9]. In the present study, this method is generalised to cellular media with arbitrary cell topologies and geometries consisting of straight and curved cell walls.

## 2. Energetic homogenisation
Consider a body $\Omega$ consisting of any kind of cellular material (see Fig. 2). The body $\Omega$ is bounded by the external boundary $\Gamma$ on which either prescribed displacements $u_i^0$ (on $\Gamma_u$) or prescribed surface tractions $T_i^0$ ($\Gamma_t$) are applied. For reasons of an efficient analysis, the body $\Omega$ has to be

---
* Corresponding author. Tel.: +49-271-740-4642; fax: +49-271-740-2461.
E-mail address: hohe@imr-sun8.fb5.uni-siegen.de (J. Hohe).

1359-8368/01/$ - see front matter © 2001 Elsevier Science Ltd. All rights reserved.
PII: S1359-8368(00)00055-X

![](./images/811025627309146112_3.jpg)

Fig. 1. Structural sandwich panel.

replaced by a body $\Omega^{*}$ with the same external boundaries $\Gamma_{u}$ and $\Gamma_{t}$ subject to the same prescribed displacements $u_{i}^{0}$ and prescribed surface tractions $T_{i}^{0}$. In contrast to $\Omega$, the body $\Omega^{*}$ is assumed to consist of a homogeneous "effective" medium with yet unknown properties.

The determination of the material properties of $\Omega^{*}$ can be performed considering a representative volume element of $\Omega$ and a corresponding volume element of $\Omega^{*}$. The effective properties have to be chosen in such a way that the mechanical behaviour of both volume elements is equivalent on the mesoscopic level. Within the energetic concept of the present study, equivalence of the mechan- ical behaviour on the mesoscopic level is assumed if equivalent strain states cause the same strain energy in both volume elements.

According to Bishop and Hill [6], strain states of both volume elements are defined to be equivalent on the meso- scopic level, if the condition

$$
\frac{1}{V} \int_{V_{\mathrm{RVE}}} \epsilon_{i j} \mathrm{~d} V=\frac{1}{V} \int_{V_{\mathrm{RVE}}} \epsilon_{i j}^{*} \mathrm{~d} V^{*}
\tag{1}
$$

holds, where $\epsilon_{i j}$ and $\epsilon_{i j}^{*}$ denote the infinitesimal strain tensor of the volume elements of $\Omega$ and $\Omega^{*}$, respectively, while $V_{\mathrm{RVE}}$ is the volume of the representative volume elements.

If Eq. (1) holds, the strain energy stored in both volume elements has to be equal. Therefore,

$$
\frac{1}{V} \int_{V_{\mathrm{RVE}}} w(\epsilon_{i j}) \mathrm{d} V=\frac{1}{V} \int_{V_{\mathrm{RVE}}} w^{*}(\epsilon_{i j}^{*}) \mathrm{d} V^{*}
\tag{2}
$$

has to be satisfied where $w$ denotes the strain energy density. Since Eq. (2) is formulated in terms of the strain energy, a homogenisation scheme based on this equation yields lower bounds on the effective moduli. Alternatively, the comple- mentary energy might be used to obtain upper bounds. Nevertheless, in a finite element study on the effective trans- verse shear moduli of hexagonal honeycomb cores by Grediac [10] it is evident that for a core thickness within the typical range for technological application, the lower bound is a better approximation for the effective properties. The upper bound is approached in the thin core limit (see also Section 5.2).

With regard to Eqs. (1) and (2), the following homogeni-sation procedure can be introduced:

1. Deform both volume elements by a number of indepen- dent reference strain states which satisfy Eq. (1).
2. Compute the total strain energy density for both volume elements.
3. Choose the effective properties in such a way that Eq. (2) is satisfied for all reference strain states.

This procedure can also be formulated in incremental

![](./images/811025627309146112_4.jpg)

Fig. 2. Concept of the representative volume element.

![](./images/811025627309146112_5.jpg)

Fig. 3. Representative volume element for general sandwich cores.

form and is so far not restricted to any specific kind of effective constitutive behaviour.

If linear elastic behaviour is assumed on the effective level, the stress and strain components $\sigma_{ij}$ and $\epsilon_{ij}$ are interrelated by

$$
\sigma_{ij}=C_{ijkl}\epsilon_{kl} \tag{3}
$$

where the components $C_{ijkl}$ of the effective elasticity tensor can be obtained by partial differentiation of the strain energy density with respect to $\epsilon_{ij}$:

$$
C_{ijkl}=\frac{\partial^{2}w}{\partial \epsilon_{ij}\partial \epsilon_{kl}} \tag{4}
$$

If no analytical expression $w(\epsilon_{ij})$ is available, the differentiation in Eq. (4) can be performed numerically. Note that in the case of linear elasticity the result of analytical and numerical differentiation is identical. Numerical differentiation yields

$$
C_{ijkl}=
\begin{cases}
2w^{*}(\epsilon_{(ij)})\frac{1}{\epsilon_{(ij)}^{2}} & \text{if : } i=j \text{ and } k=l \text{ and } i=k \\
\frac{1}{2}w^{*}(\epsilon_{(ij)})\frac{1}{\epsilon_{(ij)}^{2}} & \text{if : } i\neq j \text{ and } k\neq l \text{ and } i=k \text{ and } j=l \\
(w^{*}(\epsilon_{(ij)},\epsilon_{(kl)})-w^{*}(\epsilon_{(ij)})-w^{*}(\epsilon_{(kl)}))\frac{1}{\epsilon_{(ij)}\epsilon_{(kl)}} & \text{if : } i=j \text{ and } k=l \text{ and } i\neq k \\
\frac{1}{4}(w^{*}(\epsilon_{(ij)},\epsilon_{(kl)})-w^{*}(\epsilon_{(ij)})-w^{*}(\epsilon_{(kl)}))\frac{1}{\epsilon_{(ij)}\epsilon_{(kl)}} & \text{if : } i\neq j \text{ and } k\neq l \text{ and } (i\neq k \text{ or } j\neq l) \\
\frac{1}{2}(w^{*}(\epsilon_{(ij)},\epsilon_{(kl)})-w^{*}(\epsilon_{(ij)})-w^{*}(\epsilon_{(kl)}))\frac{1}{\epsilon_{(ij)}\epsilon_{(kl)}} & \text{if : } i=j \text{ and } k\neq l
\end{cases} \tag{5}
$$

where $w^{*}(\epsilon_{(ij)},\epsilon_{(kl)})$ denotes the strain energy density for a reference strain state, where only $\epsilon_{ij}$ and $\epsilon_{kl}$ have non-zero values. Indices in parantheses mean that no summation has to be performed.

In this context, homogeneous macroscopic reference strain states $\epsilon_{ij}=\bar{\epsilon}_{ij}$ can be used with no loss in generality, since in linear elasticity the effective properties do not depend on the strain state. The strain energy density for the representative volume element consisting of the real microstructure can be computed either analytically (see Section 3) or numerically (see Section 4).

## 3. Analytical approach

### 3.1. General concept

The first approach for the determination of the strain energy density is an analytical one. An appropriate representative volume element for a general two-dimensional cellular medium is given in Fig. 3. For all types of the topology of the cellular solid, a parallelogram-shaped representative volume element as presented in Fig. 3 can be used. The external shape of the volume element is set up by the parameters $a$, $b$ and $c$. For description of the mechanical behaviour, a local coordinate system $x_{i}$ is introduced.

The cellular structure of the representative volume element is split up into individual cell wall elements connected at the nodal points 1 to $n$ (see Fig. 4). The total strain energy of the entire representative volume element is given as the sum of the total strain energies of all cell wall elements. Therefore, the strain energy for each individual cell wall element has to be computed in terms of the deflections of the nodal points. Four degrees of freedom (displacements in three directions and the rotation with respect to the $x_{3}$-axis) per nodal point are considered.

### 3.2. Straight cell walls

For determination of the strain energy of the straight cell wall element, a local coordinate system $\tilde{x}_{i}$ is introduced (see Fig. 5). Within the local system, the displacement of nodal point $i$ with respect to the $\tilde{x}_{j}$-direction is denoted by $\tilde{v}_{(i)j}$, while the rotation with respect to the $\tilde{x}_{3}$-axis is denoted by $\Delta \tilde{\varphi}_{(i)}$.

The total displacement field is assumed to consist of three parts:

- homogeneously distributed normal deformation in the $\tilde{x}_{1}-\tilde{x}_{3}$-plane

$$
\begin{aligned}
\tilde{u}_{1}^{\mathrm{I}}(\tilde{x}_{i}) &=\tilde{v}_{(1) 1}+\frac{\tilde{v}_{(2) 1}-\tilde{v}_{(1) 1}}{l} \tilde{x}_{1} \\
\tilde{u}_{2}^{\mathrm{I}}(\tilde{x}_{i}) &=-\frac{\nu}{1-\nu}\left(\frac{\tilde{v}_{(2) 1}-\tilde{v}_{(1) 1}}{l}+\bar{\epsilon}_{33}\right) \tilde{x}_{2} \\
\tilde{u}_{3}^{\mathrm{I}}(\tilde{x}_{i}) &=\bar{\epsilon}_{33} \tilde{x}_{3}
\end{aligned} \tag{6}
$$

![](./images/811025627309146112_6.jpg)

Fig. 4. Decomposition of the representative volume element.

![](./images/811025627309146112_7.jpg)

Fig. 5. Straight cell wall element.

- bending and shear deformation in the $\tilde{x}_{1}-\tilde{x}_{2}$-plane

$$
\begin{aligned}
\tilde{u}_{1}^{\mathrm{II}}(\tilde{x}_{i}) & =-\left(\frac{12}{E h t^{3}}\left(\frac{1}{2} C_{1} \tilde{x}_{1}^{2}+C_{2} \tilde{x}_{1}+C_{3}\right)+\frac{l^{2} \alpha}{E h t^{3}} C_{1}\right) \tilde{x}_{2} \\
\tilde{u}_{2}^{\mathrm{II}}(\tilde{x}_{i}) & =\frac{12}{E h t^{3}}\left(\frac{1}{6} C_{1} \tilde{x}_{1}^{3}+\frac{1}{2} C_{2} \tilde{x}_{1}^{2}+C_{3} \tilde{x}_{1}+C_{4}\right) \\
\tilde{u}_{3}^{\mathrm{II}}(\tilde{x}_{i}) & =0
\end{aligned}
$$

where

$$
\begin{aligned}
C_{1}= & \frac{1}{2} E h \frac{t^{3}}{l^{2}} \frac{1}{1+\alpha}\left(-2 \frac{\tilde{v}_{(2) 2}-\tilde{v}_{(1) 2}}{l}+\Delta \tilde{\varphi}_{(1)}+\Delta \tilde{\varphi}_{(2)}\right) \\
C_{2}= & \frac{1}{12} E h \frac{t^{3}}{l} \frac{1}{1+\alpha} \\
& \times\left(6 \frac{\tilde{v}_{(2) 2}-\tilde{v}_{(1) 2}}{l}-(4+\alpha) \Delta \tilde{\varphi}_{(1)}-(2-\alpha) \Delta \tilde{\varphi}_{(2)}\right)
\end{aligned}
$$

$$
\begin{aligned}
C_{3}= & \frac{1}{12} E h t^{3} \frac{1}{1+\alpha} \\
& \times\left(\alpha \frac{\tilde{v}_{(2) 2}-\tilde{v}_{(1) 2}}{l}+\frac{2+\alpha}{2} \Delta \tilde{\varphi}_{(1)}-\frac{\alpha}{2} \Delta \tilde{\varphi}_{(2)}\right) \\
C_{4}= & \frac{1}{12} E h t^{3} \tilde{v}_{(1) 2}
\end{aligned}
$$

$$
\alpha=
\begin{cases}
\frac{12}{5}(1-\nu) \frac{t^{2}}{l^{2}} & \text { Timoshenko theory } \\
0 & \text { Euler-Bernoulli theory }
\end{cases}
$$

- homogeneously distributed transverse shear deformation
($\tilde{x}_{1}-\tilde{x}_{3}$-plane)

$$
\begin{aligned}
\tilde{u}_{1}^{\mathrm{III}}(\tilde{x}_{i}) & =0 & \tilde{u}_{2}^{\mathrm{III}}(\tilde{x}_{i}) & =0 \\
\tilde{u}_{3}^{\mathrm{III}}(\tilde{x}_{i}) & =\tilde{v}_{(1) 3}+\frac{\tilde{v}_{(2) 3}-\tilde{v}_{(1) 3}}{l} \tilde{x}_{1} & &
\end{aligned}
$$

In Eqs. (6)-(8) $E$ and $\nu$ are the elastic constants of the

cell wall material while $l$, $h$ and $t$ denote length, height and thickness of the cell wall element, respectively.

The total displacement field is given by the sum $\tilde{u}_{i}=\tilde{u}_{i}^{\mathrm{I}}+\tilde{u}_{i}^{\mathrm{II}}+\tilde{u}_{i}^{\mathrm{III}}$. From the displacement field, the strain field of the cell wall element can be derived by partial differentiation. The stress field is obtained from the strain field using Hooke's law in conjunction with the plane stress condition $\tilde{\sigma}_{22}=0$. Once stress and strain have been evaluated, the total strain energy of the cell wall element can be determined by integrating the sum of the products of the components of stress and strain with respect to the volume of the cell wall element. This lengthy but straightforward calculation finally results in:

$$
W=\frac{E}{2\left(1-\nu^{2}\right)} h t l\left(\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 1}}{l} \\
\frac{\tilde{v}_{(2) 1}}{l} \\
\bar{\epsilon}_{33}
\end{array}\right)^{\mathrm{T}}\left(\begin{array}{ccc}
1 & -1 & -\nu \\
-1 & 1 & \nu \\
-\nu & \nu & 1
\end{array}\right)\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 1}}{l} \\
\frac{\tilde{v}_{(2) 1}}{l} \\
\bar{\epsilon}_{33}
\end{array}\right)\right)
$$

$$
+\beta\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 2}}{l} \\
\Delta \tilde{\varphi}_{(1)} \\
\frac{\tilde{v}_{(2) 2}}{l} \\
\Delta \tilde{\varphi}_{(2)}
\end{array}\right)^{\mathrm{T}}\left(\begin{array}{cccc}
1 & \frac{1}{2} & -1 & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{4} & -\frac{1}{2} & \frac{1}{4} \\
-1 & -\frac{1}{2} & 1 & -\frac{1}{2} \\
\frac{1}{2} & \frac{1}{4} & -\frac{1}{2} & \frac{1}{4}
\end{array}\right)\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 2}}{l} \\
\Delta \tilde{\varphi}_{(1)} \\
\frac{\tilde{v}_{(2) 2}}{l} \\
\Delta \tilde{\varphi}_{(2)}
\end{array}\right)
$$

$$
\begin{aligned}
& +\frac{1}{12} \frac{t^{2}}{l^{2}}\left(\begin{array}{c}
\Delta \tilde{\varphi}_{(1)} \\
\Delta \tilde{\varphi}_{(2)}
\end{array}\right)^{\mathrm{T}}\left(\begin{array}{cc}
1 & -1 \\
-1 & 1
\end{array}\right)\left(\begin{array}{c}
\Delta \tilde{\varphi}_{(1)} \\
\Delta \tilde{\varphi}_{(2)}
\end{array}\right) \\
& +\frac{1-\nu}{2}\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 3}}{l} \\
\frac{\tilde{v}_{(2) 3}}{l}
\end{array}\right)^{\mathrm{T}}\left(\begin{array}{cc}
1 & -1 \\
-1 & 1
\end{array}\right)\left(\begin{array}{c}
\frac{\tilde{v}_{(1) 3}}{l} \\
\frac{\tilde{v}_{(2) 3}}{l}
\end{array}\right)
\end{aligned}
$$

where
$$
\beta=\frac{1}{(1+\alpha)^{2}}\left(\frac{t^{2}}{l^{2}}+\frac{1}{2} \alpha^{2}(1-\nu)\right)
$$

For determination of the nodal deflections (see Section 3.4), a relation between stress resultants $F_{(i) j}$ and $M_{(i)}$ at the nodal points of the cell wall element and the nodal deflections is required. The stress resultants are obtained by differentiation of Eq. (9) with respect to the corresponding nodal deflections. The result can be expressed in matrix form

$$
\left(\begin{array}{c}
\tilde{\mathbf{F}}_{(1)} \\
\tilde{\mathbf{F}}_{(2)}
\end{array}\right)=\left(\begin{array}{ll}
\tilde{\mathbf{K}}_{(11)} & \tilde{\mathbf{K}}_{(12)} \\
\tilde{\mathbf{K}}_{(21)} & \tilde{\mathbf{K}}_{(22)}
\end{array}\right)\left(\begin{array}{c}
\tilde{v}_{(1)} \\
\tilde{v}_{(2)}
\end{array}\right)+\left(\begin{array}{c}
\tilde{\mathbf{K}}_{(13)} \\
\tilde{\mathbf{K}}_{(23)}
\end{array}\right) \bar{\epsilon}_{33}
$$

where $\tilde{\mathbf{F}}_{(i)}=\left(\tilde{F}_{(i) 1}, \tilde{F}_{(i) 2}, \tilde{F}_{(i) 3}, \tilde{M}_{(i)}\right)^{\mathrm{T}}$ and $\tilde{v}_{(i)}=\left(\tilde{v}_{(i) 1}, \tilde{v}_{(i) 2}\right.$, $\left.\tilde{v}_{(i) 3}, \Delta \tilde{\varphi}_{(i)}\right)^{\mathrm{T}}$ denote the generalised vectors of nodal forces and nodal deflections, respectively. The stiffness matrices

![](./images/811025627309146112_8.jpg)

Fig. 6. Curved cell wall element.

are given by:

$$
\begin{pmatrix}
\tilde{\mathbf{K}}_{(11)} & \tilde{\mathbf{K}}_{(12)} \\
\tilde{\mathbf{K}}_{(21)} & \tilde{\mathbf{K}}_{(22)}
\end{pmatrix} = \frac{E}{1-\nu^{2}} \frac{h t}{l}
\begin{pmatrix}
1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\
0 & \beta & 0 & \frac{l}{2} \beta & 0 & -\beta & 0 & \frac{l}{2} \beta \\
0 & 0 & \frac{1-\nu}{2} & 0 & 0 & 0 & -\frac{1-\nu}{2} & 0 \\
0 & \frac{l}{2} \beta & 0 & \left( \frac{l^{2}}{4} \beta + \frac{t^{2}}{12} \right) & 0 & -\frac{l}{2} \beta & 0 & \left( \frac{l^{2}}{4} \beta - \frac{t^{2}}{12} \right) \\
-1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & -\beta & 0 & -\frac{l}{2} \beta & 0 & \beta & 0 & -\frac{l}{2} \beta \\
0 & 0 & -\frac{1-\nu}{2} & 0 & 0 & 0 & \frac{1-\nu}{2} & 0 \\
0 & \frac{l}{2} \beta & 0 & \left( \frac{l^{2}}{4} \beta - \frac{t^{2}}{12} \right) & 0 & -\frac{l}{2} \beta & 0 & \left( \frac{l^{2}}{4} \beta + \frac{t^{2}}{12} \right)
\end{pmatrix}
\tag{11}
$$

$$
\begin{pmatrix}
\tilde{\mathbf{K}}_{(13)} \\
\tilde{\mathbf{K}}_{(23)}
\end{pmatrix} = \frac{E}{1-\nu^{2}} \frac{h t}{l} \left( -l\nu \quad 0 \quad 0 \quad 0 \quad l\nu \quad 0 \quad 0 \quad 0 \right)^{\mathrm{T}}
\tag{12}
$$

### 3.3. Curved cell walls

Curved cell walls are approximated by a polygonal geometry (see Fig. 6). The polygonal cell wall element is set up by the end nodes 1 and 2 as well as the internal nodes 3 to $n$ which are situated on a circular arc defined by the coordinates of the end node and the radius $r$. The nodal points are connected by straight cell wall elements of constant length $\Delta l$. Thus, the strain energy for the curved cell wall element is determined by multiple evaluation of Eq. (9) for all straight subelements.

The nodal forces at all nodal points of the curved cell wall element are related to the nodal deflections by:

$$
\begin{pmatrix}
\tilde{\mathbf{F}}_{(1)} \\
\tilde{\mathbf{F}}_{(3)} \\
\vdots \\
\tilde{\mathbf{F}}_{(n)} \\
\tilde{\mathbf{F}}_{(2)}
\end{pmatrix} =
\begin{pmatrix}
\tilde{\mathbf{K}}_{(13)}^{(1)} \\
\left( \tilde{\mathbf{K}}_{(23)}^{(1)} + \tilde{\mathbf{K}}_{(13)}^{(3)} \right) \\
\vdots \\
\left( \tilde{\mathbf{K}}_{(23)}^{(n-1)} + \tilde{\mathbf{K}}_{(13)}^{(2)} \right) \\
\tilde{\mathbf{K}}_{(23)}^{(2)}
\end{pmatrix}
\bar{\epsilon}_{33} +
\begin{pmatrix}
\tilde{\mathbf{K}}_{(11)}^{(1)} & \tilde{\mathbf{K}}_{(12)}^{(1)} \\
\tilde{\mathbf{K}}_{(21)}^{(1)} & \left( \tilde{\mathbf{K}}_{(22)}^{(1)} + \tilde{\mathbf{K}}_{(11)}^{(3)} \right) & \tilde{\mathbf{K}}_{(12)}^{(3)} \\
& \tilde{\mathbf{K}}_{(21)}^{(3)} & \ddots & \ddots \\
& & \ddots & \left( \tilde{\mathbf{K}}_{(22)}^{(n-1)} + \tilde{\mathbf{K}}_{(11)}^{(2)} \right) & \tilde{\mathbf{K}}_{(12)}^{(2)} \\
& & & \tilde{\mathbf{K}}_{(21)}^{(2)} & \tilde{\mathbf{K}}_{(22)}^{(2)}
\end{pmatrix}
\begin{pmatrix}
\tilde{v}_{(1)} \\
\tilde{v}_{(3)} \\
\vdots \\
\tilde{v}_{(n)} \\
\tilde{v}_{(2)}
\end{pmatrix}
\tag{13}
$$

Since neither external forces are acting on the internal nodes nor are connections of any internal node to other cell wall elements present, all the generalised forces with respect to the internal nodes vanish: $\left( \tilde{\mathbf{F}}_{(3)}, \dots, \tilde{\mathbf{F}}_{(n)} = 0 \right)$. Therefore, the internal nodes can be eliminated. Omission of the first and the last equation in system (13) yields

$$
\begin{pmatrix}
\left( \tilde{\mathbf{K}}_{(22)}^{(1)} + \tilde{\mathbf{K}}_{(11)}^{(3)} \right) & \tilde{\mathbf{K}}_{(12)}^{(3)} \\
\tilde{\mathbf{K}}_{(21)}^{(3)} & \ddots & \ddots \\
& \ddots & \left( \tilde{\mathbf{K}}_{(22)}^{(n-1)} + \tilde{\mathbf{K}}_{(11)}^{(2)} \right)
\end{pmatrix}
\begin{pmatrix}
\tilde{v}_{(3)} \\
\vdots \\
\tilde{v}_{(n)}
\end{pmatrix}
=
\begin{pmatrix}
-\tilde{\mathbf{K}}_{(21)}^{(1)} \tilde{v}_{(1)} \\
\mathbf{0} \\
-\tilde{\mathbf{K}}_{(12)}^{(2)} \tilde{v}_{(2)}
\end{pmatrix}
-
\begin{pmatrix}
\left( \tilde{\mathbf{K}}_{(23)}^{(1)} + \tilde{\mathbf{K}}_{(13)}^{(3)} \right) \\
\vdots \\
\left( \tilde{\mathbf{K}}_{(23)}^{(n-1)} + \tilde{\mathbf{K}}_{(13)}^{(2)} \right)
\end{pmatrix}
\bar{\epsilon}_{33}
\tag{14}
$$

from which analytical expressions for $\tilde{v}_{(3)}$ to $\tilde{v}_{(n)}$ in dependence of $\tilde{v}_{(1)}$ and $\tilde{v}_{(2)}$ can be derived. Using these expressions, Eq. (13) can be reduced to a form similar to the corresponding expression (10) for the stiffness matrices of the straight cell wall element.

An analytical expression for the strain energy of the curved cell wall element similar to the corresponding expression (9) of the straight cell wall element can be stated. Nevertheless, both expressions are rather lengthy since the matrix coefficients depend on the number of subelements and therefore are not presented as closed-form expressions.

### 3.4. Determination of the nodal deflections

A complete linear system of equations for the determination of the nodal deflections of the entire representative volume element can be derived from the following considerations:

- The effective strain field is assumed to be homogeneous. Therefore, periodic boundary conditions have to be applied to the representative volume element to ensure that neighbouring volume elements in the entire cellular structure fit at their joint boundaries.

$$
\begin{aligned}
\Delta \varphi_{(i)} & =\Delta \varphi_{(i+1)}, & & i=1,3, \ldots, p \\
v_{(p) l}-v_{(i) l} & =v_{(p+1) l}-v_{(i+1) l}, & & i=1,3, \ldots,(p-2), \\
& & & l=1,2,3 \\
\Delta \varphi_{(j)} & =\Delta \varphi_{(j+1)}, & & j=(p+2),(p+4), \ldots, q \\
v_{(2) l}-v_{(j) l} & =v_{(p+1) l}-v_{(j+1) l}, & & j=(p+2),(p+4), \ldots, q, \\
& & & l=1,2,3 \\
\Delta \varphi_{(1)} & =\Delta \varphi_{(p)} & &
\end{aligned}
\tag{15}
$$

- Since homogeneous reference strain states $\bar{\epsilon}_{i j}$ are considered, the integral with respect to the volume element made of the effective medium in Eq. (1) is easily evaluated. The integral with respect to the representative volume element consisting of the real cellular material is transformed into a surface integral by means of Green's theorem. Therefore

$$
\frac{1}{V} \frac{1}{2} \int_{\Gamma_{\mathrm{RVE}}}\left(u_{i} n_{j}+u_{j} n_{i}\right) \mathrm{d} \Gamma=\bar{\epsilon}_{i j}
\tag{16}
$$

where $\Gamma_{\mathrm{RVE}}$ denotes the surface of the representative volume element and $n_{i}$ are the components of the outward normal unit vector on $\Gamma_{\mathrm{RVE}}$. The displacement field along $\Gamma_{\mathrm{RVE}}$ is interpolated using the mid-plane deformation of a straight cell wall element according to Eqs. (6)-(8) as an interpolation function. Subsequently, the integration in Eq. (16) can be performed. Considering the periodicity conditions (15), the following relations are obtained:

$$
\begin{aligned}
\bar{\epsilon}_{11} & =\frac{v_{(p) 1}-v_{(1) 1}}{a} \\
\bar{\epsilon}_{22} & =\frac{v_{(2) 2}-v_{(1) 2}}{b}+\frac{c}{a} \frac{v_{(p) 2}-v_{(1) 2}}{b} \\
\bar{\epsilon}_{23} & =\frac{1}{2}\left(\frac{v_{(2) 3}-v_{(1) 3}}{b}+\frac{c}{a} \frac{v_{(p) 3}-v_{(1) 3}}{b}\right) \\
\bar{\epsilon}_{13} & =\frac{1}{2} \frac{v_{(p) 3}-v_{(1) 3}}{a} \\
\bar{\epsilon}_{12} & =\frac{1}{2}\left(\frac{v_{(p) 2}-v_{(1) 2}}{a}+\frac{v_{(2) 1}-v_{(1) 1}}{b}+\frac{c}{a} \frac{v_{(p) 1}-v_{(1) 1}}{b}\right)
\end{aligned}
\tag{17}
$$

- No rigid body motions of the representative volume element are permitted:

$$
v_{(1) 1}=0 \quad v_{(1) 2}=0 \quad v_{(1) 3}=0 \quad v_{(p) 2}=0 \quad (18)
$$

- The stress resultants at all internal nodes as well as at all pairs of corresponding nodes $i$ and $i+1$ on the surfaces of the representative volume element (see Fig. 4) have to be in an equilibrium state since no external forces are acting.

$$
\begin{aligned}
& F_{(1) l}+F_{(2) l}+F_{(p) l}+F_{(p+1) l}=0 \\
& M_{(1)}+M_{(2)}+M_{(p)}+M_{(p+1)}=0 \\
& \begin{array}{l}
F_{(i) l}+F_{(i+1) l}=0 \\
M_{(i)}+M_{(i+1)}=0
\end{array} i=3,5, \ldots,(p-2)
\end{aligned}
\tag{19}
$$

and $i=(p+2),(p+4), \ldots, q$

$$
\begin{aligned}
& F_{(k) l}=0 \\
& M_{(k)}=0
\end{aligned} k=(q+2),(q+3), \ldots n
$$

where $l=1,2,3$

Note that the global equilibrium with respect to the nodal forces is satisfied identically since the assumptions (6)-(8) satisfy the local equilibrium conditions. Therefore, three independent equations of Eq. (19) are redundant.

Eqs. (15)-(19) form a complete linear system of equations which governs the $4 n$ nodal deflections in dependence of the macroscopic reference strain state $\bar{\epsilon}_{i j}$. The system is solved by Gaussian elimination. A summary of the algorithm is presented in Fig. 7.

### 4. Numerical approach

Alternative to the analytical approach described in Section 3, the strain energy for the reference strain states to be used with Eq. (5) can be computed in a pure numerical analysis using the finite element method. Therefore, the cell walls are meshed with four-node shell elements based on a shear flexible shell theory. In order to prevent spurious modes of deformation as well as locking effects, an enhanced strain formulation in conjunction with full integration is employed. Six degrees of freedom per node have to be considered to avoid instabilities in conjunction with plane cell walls. The finite element model is loaded by prescribed displacements at the top and bottom plane $(x_{3}=\pm h / 2)$ according to

$$
u_{i}^{0}=\left(\begin{array}{rrr}
x_{1} \bar{\epsilon}_{11} & +2 x_{2} \bar{\epsilon}_{12} & +2 x_{3} \bar{\epsilon}_{13} \\
& x_{2} \bar{\epsilon}_{22} & +2 x_{3} \bar{\epsilon}_{23} \\
& & x_{3} \bar{\epsilon}_{33}
\end{array}\right)
\tag{20}
$$

![](./images/811025627309146112_9.jpg)

Fig. 7. Algorithm for determination of the effective properties.

where $x_{i}$ is the spatial position of the node. Note that Eq. (20) describes the displacement field that would occur, if the face sheets were separated by a homogeneous medium. Thus, no interaction of cellular core and face sheets is considered. Along the remaining surfaces of the representative volume element, periodic boundary conditions according to

$$
\begin{gathered}
v_{(i) l}\left(x_{3}\right)-v_{(i) l}\left(\frac{h}{2}\right)=v_{(i+1) l}\left(x_{3}\right)-v_{(i+1) l}\left(\frac{h}{2}\right) \\
\Delta \varphi_{(i) l}\left(x_{3}\right)=\Delta \varphi_{(i+1) l}\left(x_{3}\right)
\end{gathered}
$$

$i=1,3, \ldots, q \quad l=1,2,3$

are applied, where $v_{(i) l}\left(x_{3}\right)$ denotes the displacement of a finite element node on line $i$ at $x_{3}$ with respect to direction $x_{l}$ while $\Delta \varphi_{(i) l}\left(x_{3}\right)$ denotes the rotation of a finite element node on line $i$ at $x_{3}$ with respect to the $x_{l}$-axis. Again, a total number of 21 independent reference strain states has to be applied. For each of the reference strain states, the total strain energy in the model is evaluated.

Dense meshes are used near the cell wall boundaries. In the cell wall interior, coarser meshes are sufficient and should be used for reasons of numerical efficiency.

## 5. Examples

In this section, the analytical and numerical methods presented in Sections 3 and 4 are applied to different sandwich core geometries (see Fig. 8). In all cases, aluminium with $E=72200 \mathrm{MPa}$ and $v=0.34$ is assumed as cell wall material. A constant relative core density of $\bar{\rho}=0.02$ is used by choosing an appropriate cell wall thickness.

### 5.1. Hexagonal core

The first example to be analysed is the hexagonal sandwich core. The representative volume element used for the analysis is presented in Fig. 9. The coordinates of the nodal points are given in Table 1. Equal length of all cell walls is assumed, while the thickness of the horizontal cell wall is twice the thickness of the inclined cell walls. The cell wall angle $\Phi$ (see Fig. 9) is varied from 60 to $150^{\circ}$. A constant core height of $h=10 l$ is used.

The components $C_{i j k l}$ of the effective elasticity tensor are presented in Fig. 10. In this figure, and in all subsequent figures, analytical results are denoted by lines while finite element results are marked by symbols. Comparison of the

![](./images/811025627309146112_10.jpg)

Fig. 8. Considered sandwich core geometries.

![](./images/811025627309146112_11.jpg)

Fig. 9. Hexagonal core — representative volume element.

analytical and numerical results shows a rather good agreement of both approaches. Although not visible in Fig. 10 due to the small absolute values, the agreement becomes worse in the case of $C_{1111}$ if $\Phi$ approaches $90^{\circ}$. In this case, the inclined cell walls are in a vertical position. Thus, the mode of deformation on which $C_{1111}$ is based consists exclusively in bending of the inclined cell walls. This mode of deforma-

<table>
<caption>Table 1<br>Hexagonal core — nodal points</caption>
<thead>
<tr>
<th>$i$</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\bar{x}_{(i)1}$</td>
<td>0</td>
<td>0</td>
<td>$l(1-\cos\Phi)$</td>
<td>$l(1-\cos\Phi)$</td>
<td>1</td>
</tr>
<tr>
<td>$\bar{x}_{(i)2}$</td>
<td>0</td>
<td>$2l\sin\Phi$</td>
<td>$-l\sin\Phi$</td>
<td>$l\sin\Phi$</td>
<td>0</td>
</tr>
</tbody>
</table>

tion is incompatible with the deformation of the face sheets. Therefore, an additional constraint to the deformation of the cell walls occurs near the face sheets, which is incorporated into the numerical approach but is not incorporated into the analytical one. This constraint causes additional strain energy to be stored near the face sheets. Since this effect causes a dependence of the elastic properties on the core thickness, it is often termed “thickness effect” in literature (see, e.g. Grediac [10] for the case of the transverse shear properties). Due to the large core thickness of $h=10l$, the effect is rather weak in the present case.

Regarding the influence of cell geometry on the effective properties it can be observed that in general an increase in stiffness occurs, if an increasing amount of material is oriented in the corresponding direction. Therefore, $C_{2222}$ and $C_{2323}$ increase if the inclined cell walls approach their vertical position ($\Phi\rightarrow90^{\circ}$). In contrast, $C_{1111}$ and $C_{1313}$ increase for larger values of $\Phi$. The transverse normal component $C_{3333}$ is strongly related to the relative density $\bar{\rho}$ and therefore varies only slightly with the cell wall angle. The variation is caused by changes in the associated coupling components $C_{2233}$ and $C_{1133}$. The in-plane shear component $C_{1212}$ achieves only low values throughout the considered range of $\Phi$.

In the case of $\Phi=120^{\circ}$, the regular hexagonal cell

![](./images/811025627309146112_12.jpg)

Fig. 10. Hexagonal core — effective elasticity tensor.

![](./images/811025627309146112_13.jpg)

Fig. 11. Tubular core — representative volume element.

geometry is obtained. This cell geometry is isotropic with respect to the in-plane properties. Therefore, $C_{1111}$ and $C_{2222}$ are equal as well as the associated coupling components $C_{1133}$ and $C_{2233}$. As it has been mentioned in literature (see, e.g. Gibson and Ashby [3]), a strong coupling of the in-plane normal deformation occurs in the case of the regular hexagonal core. The in-plane coupling component $C_{1122}$ is equal to the in-plane normal components $C_{1111}$ and $C_{2222}$. It decreases for $\Phi \neq 120^{\circ}$ and vanishes for $\Phi=90^{\circ}$. In case of the re-entrant hexagonal cell geometry $(\Phi<90^{\circ})$, the in-plane coupling component $C_{1122}$ becomes negative. Note that in this case the component $C_{1133}$ becomes negative too. Since the cell geometry is orthotropic on the effective level, neither coupling of normal and shear deformation nor coupling of shear and shear occurs. Thus, $C_{1112}, C_{2212}, C_{3312}$ as well as $C_{1323}$ are vanishing.

### 5.2. Tubular core
The second geometry under consideration in the present study is the tubular core geometry. An appropriate representative volume element and the coordinates of the nodal points are presented in Fig. 11 and Table 2, respectively. A constant tube diameter is assumed while the core thickness $h$ is varied from $h=r$ to $h=10 r$ in order to examine the influence of the core-face sheet constraints in more detail. The results are presented in Fig. 12.

The tubular core is found to be isotropic with respect to

![](./images/811025627309146112_14.jpg)

Fig. 12. Tubular core — effective elasticity tensor.

![](./images/811025627309146112_15.jpg)

Fig. 13. Flex-Core — representative volume element.

the in-plane directions $\bar{x}_{1}$ and $\bar{x}_{2}$. Therefore, the in-plane normal components $C_{1111}$ and $C_{2222}$ are equal as well as the associated coupling components $C_{1133}$ and $C_{2233}$ and the transverse shear components $C_{2323}$ and $C_{1313}$. No coupling of normal and shear deformation is observed.

Since bending of the cell walls is the dominant effect for the in-plane normal deformation of the unconstrained tubu- lar core, only very low values of the normal components $C_{1111}$ and $C_{2222}$ are obtained due to the low cell wall thick ness. A similar effect occurs in the case of the associated coupling components $C_{1133}$ and $C_{2233}$ and the in-plane shear stiffness $C_{1212}$. If the core thickness $h$ decreases, a transition of the mode of deformation of the cell walls from pure bending to bending and stretching occurs. The strain energy associated to cell wall stretching is significantly larger than in the case of pure bending. Therefore, a significant increase of the mentioned in-plane properties obtained from the finite element analysis is observed, since the relative contribution of the transition area in the vicinity of the face sheets to the total strain energy in the representative volume element increases with decreasing core thickness $h$. Thus, all the mentioned properties increase from nearly vanishing values in the case of thick cores to significant values for thin cores.

Minor effects of the core thickness are observed in the case of the transverse properties. In the case of the normal stiffness $C_{3333}$, the effect is caused by an increase in the coupling components $C_{2233}$ and $C_{1133}$. A slight effect on the transverse shear properties $C_{2323}$ and $C_{1313}$ is caused by the inhomogeneous distribution of the shear defor-

<table>
<caption>Table 2<br>Tubular core — nodal points</caption>
<thead>
<tr>
<th>I</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\bar{x}_{(i)1}$</td>
<td>0</td>
<td>$-r$</td>
<td>$2r$</td>
<td>$r$</td>
<td>$-(1/2)r$</td>
<td>$(3/2)r$</td>
<td>$(1/2)r$</td>
</tr>
<tr>
<td>$\bar{x}_{(i)2}$</td>
<td>0</td>
<td>$\sqrt{3}r$</td>
<td>0</td>
<td>$\sqrt{3}r$</td>
<td>$(\sqrt{3}/2)r$</td>
<td>$(\sqrt{3}/2)r$</td>
<td>$(\sqrt{3}/2)r$</td>
</tr>
</tbody>
</table>

mation near the face sheets due to the curvature of the cell walls.

### 5.3. Flex-Core

As a more complex core geometry, a Flex-Core¹-type cellular structure is analysed. An appropriate representative volume element is presented in Fig. 13. The coordinates of the nodal points are given in Table 3. A constant core thick- ness of $h=25$ mm is assumed.

In Fig. 14 the components of the effective elasticity tensor $C_{ijkl}$ are presented in dependence of the angle $\bar{\Psi}$ of the global coordinate system $\bar{x}_{i}$. Again, a rather good agreement of analytical and numerical approach is observed. Slightly larger values are obtained by the finite element approach due to the core-face sheet constraint.

It can be observed from Fig. 14 that in comparison to the other properties, the Flex-Core possesses relatively large transverse normal and shear properties $C_{3333}$, $C_{2323}$ and $C_{1313}$. Anisotropic behaviour is obtained with respect to the transverse shear properties. For this reason, coupling of the transverse shear deformation occurs resulting in non-zero values of the coupling component $C_{1323}$. Never- theless, $C_{1323}$ vanishes for $\bar{\Psi}=0$, 90 and $180^{\circ}$ since the considered cellular structure is orthotropic on the effective level due to the symmetry to the $\bar{x}_{1}$ - and $\bar{x}_{2}$-axes (see Figs. 8 and 13).

In contrast to the transverse properties, rather low values are observed in the case of the in-plane normal components $C_{1111}$ and $C_{2222}$, and in case of the in-plane shear component $C_{1212}$ and all associated coupling components. The low values of the in-plane properties cause the outstanding flex- ibility of this type of sandwich core, which therefore is a very convenient choice for application in conjunction with strongly curved sandwich shells.

## 6. Conclusions

The aim of the present study is the derivation of a scheme for the determination of the complete set of effective elastic properties of cellular sandwich cores with general cell topol- ogy and geometry. The employed homogenisation method makes use of the assumption that the strain energy in a deformed representative volume element has to be equal, whether the real cellular structure or the quasi-homoge- neous effective medium is considered, if the strain state

---
¹ Flex-Core is a registered trademark of the Hexcel Co., Dublin, CA, USA.

![](./images/811025627309146112_16.jpg)

Fig. 14. Flex-Core — effective elasticity tensor.

<table>
<caption>Table 3 Flex-Core — nodal points</caption>
<thead>
<tr>
<th>$i$</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
<th>11</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\bar{x}_{(i)1}$ (mm)</td>
<td>0.00</td>
<td>0.00</td>
<td>5.50</td>
<td>5.50</td>
<td>6.47</td>
<td>6.47</td>
<td>2.70</td>
<td>3.66</td>
<td>4.54</td>
<td>0.87</td>
<td>1.84</td>
</tr>
<tr>
<td>$\bar{x}_{(i)2}$ (mm)</td>
<td>0.00</td>
<td>8.00</td>
<td>−3.26</td>
<td>4.74</td>
<td>−4.00</td>
<td>4.00</td>
<td>0.00</td>
<td>0.74</td>
<td>4.00</td>
<td>4.74</td>
<td>4.00</td>
</tr>
</tbody>
</table>

for both cases is equivalent on the macroscopic level. Within the homogenisation process, the strain energy is evaluated comparatively by means of the finite element method and an analytical scheme. The analytical scheme uses an element-based approach but is, in contrast to the finite element method, formulated by means of the strong form of the equilibrium conditions. The results of both the approaches are found to agree well in a number of analyses considering sandwich cores consisting of straight and curved cell walls. The only exceptions are cases where strong core-face sheet constraints are present which are incorporated into the finite element approach but not into the analytical one.

The advantage of the scheme presented in the present study is the fact that all the components of the effective elasticity tensor can be determined directly, independently of the topology and geometry of the cellular structure. Thus, although experimental work for determination of the effective properties cannot totally be replaced by analytic considerations, the great expense of extensive testing might be reduced. Due to the high computational efficiency of the analytical approach, a design of high-performance sandwich cores with optimised properties for any kind of requirement in technological application can be performed in a very efficient way.

### Acknowledgements

This work was financially supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Association) under grant no. Be 1090/4-1.

### References

[1] Kelsey S, Gellatley RA, Clark BW. The shear modulus of foil honeycomb cores. Aircraft Engng 1958;30:294–302.

[2] Chang CC, Ebcioglu IK. Effect of cell geometry on the shear modulus and on density of sandwich panel cores. J Basic Engng 1961;83:513–8.

[3] Gibson LJ, Ashby MF. Cellular solids — structure and properties. Cambridge: Cambridge University Press, 1997.

[4] Noor AK, Burton WS, Bert CW. Computational models for sandwich panels and shells. Appl Mech Rev 1996;49:155–99.

[5] Overaker DW, Cuitiño AM, Langrana NA. Elastoplastic micromechanical modeling of two-dimensional irregular convex and nonconvex (re-entrant) hexagonal foams. J Appl Mech 1998;65:748–57.

[6] Bishop JFW, Hill R. A theory of the plastic distortion of a

polycrystalline aggregate under combined stress. Philos Mag 1951;42: 414–27.

[7] Hashin Z, Shtrikman S. On some variational principles in anisotropic and nonhomogeneous elasticity. J Mech Phys Solids 1962;10:335–42.

[8] Sanchez-Palencia E. Non-homogeneous media and vibration theory. Berlin: Springer, 1980.

[9] Hohe J, Beschorner C, Becker W. Effective elastic properties of hexa- gonal and quadrilateral grid structures. Compos Struct 1999;46:73–89.

[10] Grediac M. A finite element study of the transverse shear in honey- comb cores. Int J Solids Struct 1993;30:1777–88.