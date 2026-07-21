![](./images/812037237192523776_1.jpg)

Available online at www.sciencedirect.com

![](./images/812037237192523776_2.jpg)

Acta Materialia 55 (2007) 1093-1108

![](./images/812037237192523776_3.jpg)

# Electromechanical response of 1-3 piezoelectric composites:
## An analytical model

Ronit Kar-Gupta, T.A. Venkatesh *

Department of Mechanical Engineering, Tulane University, 400 Lindy Boggs Center, New Orleans, LA 70118, USA

Received 13 August 2006; received in revised form 21 September 2006; accepted 24 September 2006
Available online 5 December 2006

## Abstract
An analytical model that captures the complete electromechanical response of a 1-3 piezoelectric composite system where both the matrix and fiber phases are, in general, elastically anisotropic and piezoelectrically active is developed. Upon identifying 36 classes of 1-3 composites based on the nature of the isotropy and the piezoelectric properties of the constituents, a detailed methodology for determin- ing all the 45 independent material constants of a general 1-3 composite is presented. By comparing the predictions of the analytical model with that of a finite element model for a range of composite materials, it is demonstrated that the composite material properties in the longitudinal direction (i.e., $C_{33}$, $\kappa_{33}$ and $\varepsilon_{33}$) are well predicted by the analytical model. However, as a consequence of the approx imation introduced in the model formulation (where the fiber composite is modeled as a layered composite) the analytical model could significantly underpredict the composite material properties in the transverse direction (especially the dielectric properties, $\kappa_{11}$ and $\kappa_{22}$) for some ("matrix-dominant") composite material systems.
 2006 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Piezoelectricity; Composites; Dielectrics; Analytical methods; Constitutive equations

---

## 1. Introduction
Piezoelectric materials have historically evoked consid- erable interest because of their unique electromechanical coupling characteristics which produce mechanical defor- mations under the application of electrical loads (i.e., the direct effect) and electrical fields under the application of mechanical loads (i.e., the converse effect). Recognizing the potential utility of piezoelectric materials as sensors and actuators in a large number of practical applications, several research efforts have focused on developing (monolithic) materials (e.g., lead zirconate titanate (PZT) and barium titanate) with enhanced coupled prop- erties. However, the monolithic materials that exhibit improved coupled properties also tend to be predomi- nantly ceramic (and inherently brittle) in nature. Conse- quently, the composites approach towards mitigating the limitation of brittleness in several piezoelectric materials has been investigated. For example, it has been demon- strated that the dispersion of an active phase (in a fibrous or a particulate form) in a (passive or active) polymer matrix results in a flexible structure that functions as a piezoelectrically active device as well.

In conjunction with experimental efforts [1,2], several studies have focused on developing analytical and numer- ical models to predict the effective electromechanical behavior of piezoelectric composites. Newnham et al. pro- posed a framework for a classification of piezoelectric composites based on the connectivity of the constituent phases and formulated a simple series-parallel model to derive some of the fundamental constants of piezoelectric composites [3]. Banno investigated the effects of porosity - distribution, size and geometry, in piezoelectric materials using a modified cubes approach [4]. Dunn and Taya coupled micromechanics theories with the electroelastic solution of an ellipsoidal inclusion in an infinite piezoelec- tric medium to predict the electromechanical properties of

* Corresponding author.
E-mail address: tav@tulane.edu (T.A. Venkatesh).

1359-6454/$30.00  2006 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actamat.2006.09.023

a piezocomposite [5]. Bisegna and Luciano generalized the Hashin–Shtrikman principles to generate eight variational principles based on auxiliary electro-elastic principles to determine the bounds for the overall properties of piezoelectric materials [6,7]. Poizat and Sester developed unit-cell-based finite-element models to predict the effective longitudinal and transverse electromechanical constants for 1–3 and 0–3 types of composites [8]. Nan and Weng adopted the effective medium theory to study the effect of polarization in a two phase (0–3 or 1–3 type) composite where both the phases are active [9].

Of the several classes of piezoelectric composites that have been developed, the 1–3 type of (long-fiber) composites have received increased attention in recent times because of their extensive use in naval and bio-medical applications [10,11]. Smith and Auld proposed a simple approach to characterize the thickness mode oscillation of 1–3 piezocomposites [10], while Smith formulated another model to predict the hydrostatic response of 1–3 composites [11]. Guinovart-Diaz et al. invoked the asymptotic homogenization method to identify analytical expressions for a binary piezoelectric composite where both the constituent phases exhibit hexagonal symmetry [12]. Petterman and Suresh and Kar-Gupta and Venkatesh developed finite-element-based numerical models for characterizing the constitutive behavior of 1–3 composites [13,14].

Overall, the 1–3 piezoelectric composite system where the matrix phase is passive and the fiber phase is active has been widely researched. However, only a few analytical models are available for the case where both the matrix and the fiber phases could be piezoelectrically active [5,9,12]. Furthermore, the analytical solutions that are currently available are limited to materials which conform to certain symmetry classes and/or specific combinations of poling characteristics of the matrix and the fiber phases. Hence, the overall objectives of the present study are:

(i) to develop an analytical model to capture the complete electromechanical response of a 1–3 piezoelectric composite system where both the matrix and fiber phases could, in general, be anisotropic and piezoelectrically active;
(ii) to assess the accuracy of the new model by recourse to detailed finite-element simulations of the electromechanical response of 1–3 piezoelectric composite systems;
(iii) to compare the fundamental elastic, dielectric and piezoelectric material constants of 1–3 piezoelectric composites predicted by the new model with the results of models developed earlier for specific cases of material anisotropy and poling characteristics; and
(iv) to discuss the application of the new model in determining the crystal symmetry and the figures of merit for the 1–3 piezoelectric composite materials.

The present work is organized as follows. A classification of 1–3 piezoelectric composite systems based on the crystal symmetry and the piezoelectric activity of the constituent phases is identified in Section 2. A brief review of the constitutive response of piezoelectric materials is presented in Section 3. The analytical model developed in the present study is detailed in Section 4. In Section 5 the results of the present model are compared to and assessed with the results of the analytical and numerical models developed prior to this study. The applications of the present model in determining the composite material symmetry and figures of merit are presented in Section 6 and the principal conclusions are summarized in Section 7.

## 2. Classification of 1–3 composite materials

Depending on the nature of the elastic anisotropy (e.g., fully anisotropic, transversely isotropic, or isotropic) and piezoelectric activity (i.e., active or passive) of the matrix and the fiber phases, 36 classes of 1–3 composite materials may be identified (Table 1). Furthermore, for each of the 1–3 piezoelectric composite material classes, several subclasses of composites can be recognized based on the relative orientation of the poling directions of the fiber and the matrix phases. While Kar-Gupta and Venkatesh highlighted five such sub-classes based on the poling characteristics of the matrix and fiber phases in a prior study [14], the 1–3 composite materials can broadly be grouped as: (a) "longitudinal" composites where the matrix and the fiber phases are poled along the longitudinal direction (Fig. 1a) and (b) "transverse" composites where the matrix phase is poled in the transverse direction (Fig. 1b).

As illustrated in Table 1, the analytical models that are currently available predict the electromechanical characteristics of a few classes of 1–3 composite materials. However, the model developed in the present study captures the electromechanical responses of all 36 classes of 1–3 (longitudinal and transverse) composite systems.

## 3. Constitutive behavior of piezoelectric materials

The constitutive response of piezoelectric materials in the linear elastic region is represented as:

$$
\begin{aligned}
\sigma_{i j} & =C_{i j k l}^{E} \varepsilon_{k l}-e_{i j k} E_{k} \\
D_{i} & =e_{i k l} \varepsilon_{k l}+\kappa_{i j}^{\varepsilon} E_{j}
\end{aligned} \tag{1}
$$

where $\sigma$ and $\varepsilon$ are the second rank stress and strain tensors, respectively, $E$ and $D$ are, respectively, the electric field and the electric displacement vectors, $\kappa$ is the second rank dielectric tensor, $e$ is the third rank coupling tensor and $C$ is the fourth rank elasticity tensor. The superscripts $E$ and $\varepsilon$ indicate that the elasticity and permittivity constants are determined under conditions of zero or constant electric field and strain, respectively. Following the matrix representation of Nye [15], Eq. (1) can also be represented as:

$$
\begin{aligned}
\sigma_{a} & =C_{a b}^{E} \varepsilon_{b}-e_{a b} E_{b} \\
D_{a} & =e_{a b} \varepsilon_{b}+\kappa_{a b}^{\varepsilon} E_{b}
\end{aligned} \tag{2}
$$


<table>
<caption>Table 1 (a) A classification of 1–3 piezoelectric composites based on the elastic anisotropy and the piezoelectric activity of the matrix and fiber phases; (b) list of commonly available piezoelectric materials and their crystal symmetries</caption>
<tbody>
<tr>
<th colspan="3">1–3 Composites</th>
<td colspan="2">Fiber</td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr>
<th colspan="3"></th>
<td colspan="2">Anisotropic</td>
<td colspan="2">Transversely isotropic</td>
<td colspan="2">Isotropic</td>
</tr>
<tr>
<th colspan="3"></th>
<td>Active</td>
<td>Passive</td>
<td>Active</td>
<td>Passive</td>
<td>Active</td>
<td>Passive</td>
</tr>
<tr>
<th>(a)</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>Matrix</th>
<td>Anisotropic</td>
<td>Active<br>Passive</td>
<td colspan="2">Present study</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th></th>
<td>Transversely isotropic</td>
<td>Active<br>Passive</td>
<td colspan="2">Dunn and Taya [5]</td>
<td colspan="2">Guinovart-Diaz et al. [12]</td>
<td></td>
<td></td>
</tr>
<tr>
<th></th>
<td>Isotropic</td>
<td>Active<br>Passive</td>
<td></td>
<td></td>
<td colspan="2">Smith and Auld [10],<br>Smith [11],<br>Chan and Unsworth [16]</td>
<td colspan="2">Whitney and Riley [17]</td>
</tr>
<tr>
<th>Material</th>
<td colspan="2"></td>
<td colspan="3">Point group</td>
<td colspan="3">Crystal system</td>
</tr>
<tr>
<th>(b)</th>
<td colspan="2"></td>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Cadmium sulfide</th>
<td colspan="3">6mm</td>
<td colspan="3">Hexagonal</td>
</tr>
<tr>
<th colspan="3">Lead zirconate titanate (PZT-7A)</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Poly vinilidine di fluoride (PVDF)</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Zinc oxide</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Zinc sulfide</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Ammonium dihyrdogen phosphate</th>
<td colspan="3">$\bar{4}$2m</td>
<td colspan="3">Tetragonal</td>
</tr>
<tr>
<th colspan="3">Potassium dihyrdogen phosphate</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Barium sodium niobate</th>
<td colspan="3">mm2</td>
<td colspan="3">Orthorhombic</td>
</tr>
<tr>
<th colspan="3">Barium titanate</th>
<td colspan="3">4mm</td>
<td colspan="3">Tetragonal</td>
</tr>
<tr>
<th colspan="3">Lithium niobate</th>
<td colspan="3">3m</td>
<td colspan="3">Trigonal</td>
</tr>
<tr>
<th colspan="3">Lithium tantalate</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Rochelle salt</th>
<td colspan="3">222</td>
<td colspan="3">Rhombic</td>
</tr>
<tr>
<th colspan="3">Bismuth germanate</th>
<td colspan="3">$\bar{4}$3m</td>
<td colspan="3">Cubic</td>
</tr>
<tr>
<th colspan="3">Gallium arsenide</th>
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr>
<th colspan="3">Tellurium dioxide</th>
<td colspan="3">422</td>
<td colspan="3">Tetragonal</td>
</tr>
</tbody>
</table>

where $a$ and $b$ are derived from $ij$ and $kl$ as follows: for $ij$ or $kl = 11, 22, 33, 23, 13,$ or $12$; and $a$ and $b$ are, respectively, given by $1, 2, 3, 4, 5,$ or $6$ (e.g., $\varepsilon_{11} = \varepsilon_1$ and $C_{1122} = C_{12}$). The shear strains are accounted for appropriately as well (e.g., $2\varepsilon_{13} = \varepsilon_5$). Eq. (2) is the most general representation of the constitutive equation and has 21 elasticity, 18 piezoelectric and six permittivity (or dielectric) constants that are independent material properties. Thus, a complete characterization of a (monolithic or composite) piezoelectric material in the linear elastic domain requires an identification of all the 45 material constants.

![](./images/812037237192523776_4.jpg)

Fig. 1. Based on the relative orientation of the poling directions in the matrix and the fiber phases, two classes of 1–3 composites are identified: (a) “longitudinal” composites and (b) “transverse” composites.

## 4. Analytical model for 1–3 composites

### 4.1. Model formulation

An analytical model that captures the complete electro-mechanical response of a 1–3 binary piezoelectric composite where both the constituent phases could, in general, be elastically anisotropic and piezoelectrically active (in the longitudinal and/or the transverse sense) has been devel-

![](./images/812037237192523776_5.jpg)

Fig. 2. The stress-strain (and electric-field-electric displacement) relationships in the transverse direction (1 or 2) of a 1-3 fiber composite (a) may be recognized by invoking an equivalent layered composite [19] where the second phase layer thickness is proportional to the fiber volume fraction in the 1-direction (b) and the 2-direction (c).

oped in the present study. In developing the model, the following assumptions are invoked.

(i) The fiber and the matrix phases are assumed to be perfectly bonded such that there is no slip across the fiber-matrix interface. Hence, the normal strains in the fiber, matrix and the composite, along direction 3 (Fig. 2), are modeled as being equal to each other, as
$$
\varepsilon_{3}^{\mathrm{c}}=\varepsilon_{3}^{\mathrm{f}}=\varepsilon_{3}^{\mathrm{m}}. \tag{3}
$$

(ii) The composite normal stress along direction 3 (Fig. 2) is expressed as a weighted sum of the normal stresses of the individual constituents, with the weights being determined by the volume fractions of each of the phases, as
$$
\sigma_{3}^{\mathrm{c}}=v_{\mathrm{f}} \sigma_{3}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \sigma_{3}^{\mathrm{m}}. \tag{4}
$$

(iii) The relationships between the normal stresses and strains in the fiber, matrix and the composite in the transverse direction (i.e., directions 1 and 2), are recognized by representing the fiber composite (Fig. 2a) as an equivalent layered composite (Fig. 2b and c). Thus, the stresses and strains in the transverse directions are given as
$$
\sigma_{1}^{\mathrm{c}}=\sigma_{1}^{\mathrm{f}}=\sigma_{1}^{\mathrm{m}} \text { (Fig. 2b), } \quad \sigma_{2}^{\mathrm{c}}=\sigma_{2}^{\mathrm{f}}=\sigma_{2}^{\mathrm{m}} \text { (Fig. 2c) } \tag{5}
$$
$$
\varepsilon_{1}^{\mathrm{c}}=v_{\mathrm{f}} \varepsilon_{1}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \varepsilon_{1}^{\mathrm{m}}, \quad \varepsilon_{2}^{\mathrm{c}}=v_{\mathrm{f}} \varepsilon_{2}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \varepsilon_{2}^{\mathrm{m}}. \tag{6}
$$

(iv) Also, following the layered composite representation, the shear stresses and strains in the matrix, fiber and the composite are represented as
$$
\sigma_{5}^{\mathrm{c}}=\sigma_{5}^{\mathrm{f}}=\sigma_{5}^{\mathrm{m}} \tag{7}
$$
$$
\varepsilon_{5}^{\mathrm{c}}=v_{\mathrm{f}} \varepsilon_{5}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \varepsilon_{5}^{\mathrm{m}} \tag{8}
$$
$$
\sigma_{4}^{\mathrm{c}}=\sigma_{4}^{\mathrm{f}}=\sigma_{4}^{\mathrm{m}} \tag{9}
$$
$$
\varepsilon_{4}^{\mathrm{c}}=v_{\mathrm{f}} \varepsilon_{4}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \varepsilon_{4}^{\mathrm{m}} \tag{10}
$$
$$
\varepsilon_{6}^{\mathrm{c}}=\varepsilon_{6}^{\mathrm{f}}=\varepsilon_{6}^{\mathrm{m}} \tag{11}
$$
$$
\sigma_{6}^{\mathrm{c}}=v_{\mathrm{f}} \sigma_{6}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) \sigma_{6}^{\mathrm{m}}. \tag{12}
$$

(v) Furthermore, based on a simple theory of the series-parallel combination of dielectrics, the electric displacement of the composite is related to that of the individual phases by the following relations
$$
D_{3}^{\mathrm{c}}=v_{\mathrm{f}} D_{3}^{\mathrm{f}}+\left(1-v_{\mathrm{f}}\right) D_{3}^{\mathrm{m}} \tag{13}
$$
$$
D_{1}^{\mathrm{c}}=D_{1}^{\mathrm{f}}=D_{1}^{\mathrm{m}} \text { (Fig. 2b) } \tag{14}
$$
$$
D_{2}^{\mathrm{c}}=D_{2}^{\mathrm{f}}=D_{2}^{\mathrm{m}} \text { (Fig. 2c). } \tag{15}
$$

As a consequence of Eq. (13), $E_{3}^{\mathrm{c}}=E_{3}^{\mathrm{f}}=E_{3}^{\mathrm{m}}$, where $E$ is the electric field. In Eqs. (3)-(15), the superscripts c, f and m, respectively, refer to the composite, fiber and the matrix. The implications of the idealization (of a fiber composite as a layered composite, Fig. 2) that is invoked in the analytical model formulation on the accuracy of the model predictions are examined in detail in Section 5.3.

### 4.2. Electromechanical response of a 1-3 composite with anisotropic and active constituents

The electromechanical response of a 1-3 composite is determined through a two-step methodology as follows. First, using the stress-strain and the electric-field-electric displacement relationships identified in Eqs. (3)-(15) and the constitutive properties of the fiber, matrix and the composite, represented as

$$
\begin{pmatrix}
\sigma_{1}^{x} \\
\sigma_{2}^{x} \\
\sigma_{3}^{x} \\
\sigma_{4}^{x} \\
\sigma_{5}^{x} \\
\sigma_{6}^{x} \\
D_{1}^{x} \\
D_{2}^{x} \\
D_{3}^{x}
\end{pmatrix}
=
\begin{pmatrix}
C_{11}^{x} & C_{12}^{x} & C_{13}^{x} & C_{14}^{x} & C_{15}^{x} & C_{16}^{x} & -e_{11}^{x} & -e_{21}^{x} & -e_{31}^{x} \\
\cdot & C_{22}^{x} & C_{23}^{x} & C_{24}^{x} & C_{25}^{x} & C_{26}^{x} & -e_{12}^{x} & -e_{22}^{x} & -e_{32}^{x} \\
\cdot & \cdot & C_{33}^{x} & C_{34}^{x} & C_{35}^{x} & C_{36}^{x} & -e_{13}^{x} & -e_{23}^{x} & -e_{33}^{x} \\
\cdot & \cdot & \cdot & C_{44}^{x} & C_{45}^{x} & C_{46}^{x} & -e_{14}^{x} & -e_{24}^{x} & -e_{34}^{x} \\
\cdot & \cdot & \cdot & \cdot & C_{55}^{x} & C_{56}^{x} & -e_{15}^{x} & -e_{25}^{x} & -e_{35}^{x} \\
\cdot & \cdot & \cdot & \cdot & \cdot & C_{66}^{x} & -e_{16}^{x} & -e_{26}^{x} & -e_{36}^{x} \\
e_{11}^{x} & e_{12}^{x} & e_{13}^{x} & e_{14}^{x} & e_{15}^{x} & e_{16}^{x} & \kappa_{11}^{x} & \kappa_{12}^{x} & \kappa_{13}^{x} \\
e_{21}^{x} & e_{22}^{x} & e_{23}^{x} & e_{24}^{x} & e_{25}^{x} & e_{26}^{x} & \cdot & \kappa_{22}^{x} & \kappa_{23}^{x} \\
e_{31}^{x} & e_{32}^{x} & e_{33}^{x} & e_{34}^{x} & e_{35}^{x} & e_{36}^{x} & \cdot & \cdot & \kappa_{33}^{x}
\end{pmatrix}
\begin{pmatrix}
\varepsilon_{1}^{x} \\
\varepsilon_{2}^{x} \\
\varepsilon_{3}^{x} \\
\varepsilon_{4}^{x} \\
\varepsilon_{5}^{x} \\
\varepsilon_{6}^{x} \\
E_{1}^{x} \\
E_{2}^{x} \\
E_{3}^{x}
\end{pmatrix}
\tag{16}
$$

where the superscript " $x$ " refers to "c-composite", "f- fiber" and "m-matrix", the fiber phase properties are expressed in terms of the composite properties in a matrix format as

$$
\underbrace{
\begin{pmatrix}
\varepsilon_{1}^{\mathrm{f}} \\
\varepsilon_{2}^{\mathrm{f}} \\
\varepsilon_{4}^{\mathrm{f}} \\
\varepsilon_{5}^{\mathrm{f}} \\
E_{1}^{\mathrm{f}} \\
E_{2}^{\mathrm{f}}
\end{pmatrix}
=
\begin{pmatrix}
A_{1} & A_{2} & A_{3} & A_{4} & A_{5} & A_{6} & A_{7} & A_{8} & A_{9} \\
B_{1} & B_{2} & B_{3} & B_{4} & B_{5} & B_{6} & B_{7} & B_{8} & B_{9} \\
C_{1} & C_{2} & C_{3} & C_{4} & C_{5} & C_{6} & C_{7} & C_{8} & C_{9} \\
D_{1} & D_{2} & D_{3} & D_{4} & D_{5} & D_{6} & D_{7} & D_{8} & D_{9} \\
X_{1} & X_{2} & X_{3} & X_{4} & X_{5} & X_{6} & X_{7} & X_{8} & X_{9} \\
Y_{1} & Y_{2} & Y_{3} & Y_{4} & Y_{5} & Y_{6} & Y_{7} & Y_{8} & Y_{9}
\end{pmatrix}}_{Z}
\begin{bmatrix}
\varepsilon_{1}^{\mathrm{c}} \\
\varepsilon_{2}^{\mathrm{c}} \\
\varepsilon_{3}^{\mathrm{c}} \\
\varepsilon_{4}^{\mathrm{c}} \\
\varepsilon_{5}^{\mathrm{c}} \\
\varepsilon_{6}^{\mathrm{c}} \\
E_{1}^{\mathrm{c}} \\
E_{2}^{\mathrm{c}} \\
E_{3}^{\mathrm{c}}
\end{bmatrix}
\tag{17}
$$

The $Z$ matrix identified in Eq. (17) is given by
$$Z=[A]^{-1}[B] \tag{18}$$
where

$$
[A] =
\begin{pmatrix}
v_{\mathrm{m}} C_{11}^{\mathrm{f}}+v_{\mathrm{f}} C_{11}^{\mathrm{m}} & v_{\mathrm{m}} C_{12}^{\mathrm{f}}+v_{\mathrm{f}} C_{12}^{\mathrm{m}} & v_{\mathrm{m}} C_{14}^{\mathrm{f}}+v_{\mathrm{f}} C_{14}^{\mathrm{m}} & v_{\mathrm{m}} C_{15}^{\mathrm{f}}+v_{\mathrm{f}} C_{15}^{\mathrm{m}} & -\left(v_{\mathrm{m}} e_{11}^{\mathrm{f}}+v_{\mathrm{f}} e_{11}^{\mathrm{m}}\right) & -\left(v_{\mathrm{m}} e_{21}^{\mathrm{f}}+v_{\mathrm{f}} e_{21}^{\mathrm{m}}\right) \\
v_{\mathrm{m}} C_{12}^{\mathrm{f}}+v_{\mathrm{f}} C_{12}^{\mathrm{m}} & v_{\mathrm{m}} C_{22}^{\mathrm{f}}+v_{\mathrm{f}} C_{22}^{\mathrm{m}} & v_{\mathrm{m}} C_{24}^{\mathrm{f}}+v_{\mathrm{f}} C_{24}^{\mathrm{m}} & v_{\mathrm{m}} C_{25}^{\mathrm{f}}+v_{\mathrm{f}} C_{25}^{\mathrm{m}} & -\left(v_{\mathrm{m}} e_{12}^{\mathrm{f}}+v_{\mathrm{f}} e_{12}^{\mathrm{m}}\right) & -\left(v_{\mathrm{m}} e_{22}^{\mathrm{f}}+v_{\mathrm{f}} e_{22}^{\mathrm{m}}\right) \\
v_{\mathrm{m}} C_{14}^{\mathrm{f}}+v_{\mathrm{f}} C_{14}^{\mathrm{m}} & v_{\mathrm{m}} C_{24}^{\mathrm{f}}+v_{\mathrm{f}} C_{24}^{\mathrm{m}} & v_{\mathrm{m}} C_{44}^{\mathrm{f}}+v_{\mathrm{f}} C_{44}^{\mathrm{m}} & v_{\mathrm{m}} C_{45}^{\mathrm{f}}+v_{\mathrm{f}} C_{45}^{\mathrm{m}} & -\left(v_{\mathrm{m}} e_{14}^{\mathrm{f}}+v_{\mathrm{f}} e_{14}^{\mathrm{m}}\right) & -\left(v_{\mathrm{m}} e_{24}^{\mathrm{f}}+v_{\mathrm{f}} e_{24}^{\mathrm{m}}\right) \\
v_{\mathrm{m}} C_{15}^{\mathrm{f}}+v_{\mathrm{f}} C_{15}^{\mathrm{m}} & v_{\mathrm{m}} C_{25}^{\mathrm{f}}+v_{\mathrm{f}} C_{25}^{\mathrm{m}} & v_{\mathrm{m}} C_{45}^{\mathrm{f}}+v_{\mathrm{f}} C_{45}^{\mathrm{m}} & v_{\mathrm{m}} C_{55}^{\mathrm{f}}+v_{\mathrm{f}} C_{55}^{\mathrm{m}} & -\left(v_{\mathrm{m}} e_{15}^{\mathrm{f}}+v_{\mathrm{f}} e_{15}^{\mathrm{m}}\right) & -\left(v_{\mathrm{m}} e_{25}^{\mathrm{f}}+v_{\mathrm{f}} e_{25}^{\mathrm{m}}\right) \\
v_{\mathrm{m}} e_{11}^{\mathrm{f}}+v_{\mathrm{f}} e_{11}^{\mathrm{m}} & v_{\mathrm{m}} e_{12}^{\mathrm{f}}+v_{\mathrm{f}} e_{12}^{\mathrm{m}} & v_{\mathrm{m}} e_{14}^{\mathrm{f}}+v_{\mathrm{f}} e_{14}^{\mathrm{m}} & v_{\mathrm{m}} e_{15}^{\mathrm{f}}+v_{\mathrm{f}} e_{15}^{\mathrm{m}} & \left(v_{\mathrm{m}} \kappa_{11}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right) & \left(v_{\mathrm{m}} \kappa_{12}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{12}^{\mathrm{m}}\right) \\
v_{\mathrm{m}} e_{21}^{\mathrm{f}}+v_{\mathrm{f}} e_{21}^{\mathrm{m}} & v_{\mathrm{m}} e_{22}^{\mathrm{f}}+v_{\mathrm{f}} e_{22}^{\mathrm{m}} & v_{\mathrm{m}} e_{24}^{\mathrm{f}}+v_{\mathrm{f}} e_{24}^{\mathrm{m}} & v_{\mathrm{m}} e_{25}^{\mathrm{f}}+v_{\mathrm{f}} e_{25}^{\mathrm{m}} & \left(v_{\mathrm{m}} \kappa_{12}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{12}^{\mathrm{m}}\right) & \left(v_{\mathrm{m}} \kappa_{22}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{22}^{\mathrm{m}}\right)
\end{pmatrix}
\tag{19}
$$

and

$$
[B] =
\begin{pmatrix}
C_{11}^{\mathrm{m}} & C_{12}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{13}^{\mathrm{m}}-C_{13}^{\mathrm{f}}\right) & C_{14}^{\mathrm{m}} & C_{15}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{16}^{\mathrm{m}}-C_{16}^{\mathrm{f}}\right) & -e_{11}^{\mathrm{m}} & -e_{21}^{\mathrm{m}} & -v_{\mathrm{m}}\left(e_{31}^{\mathrm{m}}-e_{31}^{\mathrm{f}}\right) \\
C_{12}^{\mathrm{m}} & C_{22}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{23}^{\mathrm{m}}-C_{23}^{\mathrm{f}}\right) & C_{24}^{\mathrm{m}} & C_{25}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{26}^{\mathrm{m}}-C_{26}^{\mathrm{f}}\right) & -e_{12}^{\mathrm{m}} & -e_{22}^{\mathrm{m}} & -v_{\mathrm{m}}\left(e_{32}^{\mathrm{m}}-e_{32}^{\mathrm{f}}\right) \\
C_{14}^{\mathrm{m}} & C_{24}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{34}^{\mathrm{m}}-C_{34}^{\mathrm{f}}\right) & C_{44}^{\mathrm{m}} & C_{45}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{46}^{\mathrm{m}}-C_{46}^{\mathrm{f}}\right) & -e_{14}^{\mathrm{m}} & -e_{24}^{\mathrm{m}} & -v_{\mathrm{m}}\left(e_{34}^{\mathrm{m}}-e_{34}^{\mathrm{f}}\right) \\
C_{15}^{\mathrm{m}} & C_{25}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{35}^{\mathrm{m}}-C_{35}^{\mathrm{f}}\right) & C_{45}^{\mathrm{m}} & C_{55}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{56}^{\mathrm{m}}-C_{56}^{\mathrm{f}}\right) & -e_{15}^{\mathrm{m}} & -e_{25}^{\mathrm{m}} & -v_{\mathrm{m}}\left(e_{35}^{\mathrm{m}}-e_{35}^{\mathrm{f}}\right) \\
e_{11}^{\mathrm{m}} & e_{12}^{\mathrm{m}} & v_{\mathrm{m}}\left(e_{13}^{\mathrm{m}}-e_{13}^{\mathrm{f}}\right) & e_{14}^{\mathrm{m}} & e_{15}^{\mathrm{m}} & v_{\mathrm{m}}\left(e_{16}^{\mathrm{m}}-e_{16}^{\mathrm{f}}\right) & \kappa_{11}^{\mathrm{m}} & \kappa_{12}^{\mathrm{m}} & v_{\mathrm{m}}\left(\kappa_{13}^{\mathrm{m}}-\kappa_{13}^{\mathrm{f}}\right) \\
e_{21}^{\mathrm{m}} & e_{22}^{\mathrm{m}} & v_{\mathrm{m}}\left(e_{23}^{\mathrm{m}}-e_{23}^{\mathrm{f}}\right) & e_{24}^{\mathrm{m}} & e_{25}^{\mathrm{m}} & v_{\mathrm{m}}\left(e_{26}^{\mathrm{m}}-e_{26}^{\mathrm{f}}\right) & \kappa_{12}^{\mathrm{m}} & \kappa_{22}^{\mathrm{m}} & v_{\mathrm{m}}\left(\kappa_{23}^{\mathrm{m}}-\kappa_{23}^{\mathrm{f}}\right)
\end{pmatrix}.
\tag{20}
$$

The fiber and matrix volume fractions are, respectively, $v_{\mathrm{f}}$ and $v_{\mathrm{m}}=\left(1-v_{\mathrm{f}}\right)$.

Second, the constitutive behavior of the composite material is captured by systematically combining Eq. (17) with the stress-strain and electric-field-electric displacement relationships (Eqs. (3)-(15)). For example, from Eq. (5), the composite normal stress is represented as

$$
\begin{aligned}
\sigma_{1}^{\mathrm{c}}=\sigma_{1}^{\mathrm{f}}= & C_{11}^{\mathrm{f}} \varepsilon_{1}^{\mathrm{f}}+C_{12}^{\mathrm{f}} \varepsilon_{2}^{\mathrm{f}}+C_{13}^{\mathrm{f}} \varepsilon_{3}^{\mathrm{f}}+C_{14}^{\mathrm{f}} \varepsilon_{4}^{\mathrm{f}}+C_{15}^{\mathrm{f}} \varepsilon_{5}^{\mathrm{f}} \\
& +C_{16}^{\mathrm{f}} \varepsilon_{6}^{\mathrm{f}}-e_{11}^{\mathrm{f}} E_{1}^{\mathrm{f}}-e_{21}^{\mathrm{f}} E_{2}^{\mathrm{f}}-e_{31}^{\mathrm{f}} E_{3}^{\mathrm{f}}.
\end{aligned}
\tag{21}
$$

The fiber phase strains and electric field components in Eq. (21) are then re-written in terms of the composite properties using Eq. (17). Subsequently, by comparing the corresponding coefficients of the composite strains and electric fields in Eqs. (16) and (21), nine of the 81 composite electroelastic moduli, where both the fiber and the matrix phases are completely anisotropic, are identified as follows.

$$
C_{11}^{\mathrm{c}}=A_{1} C_{11}^{\mathrm{f}}+B_{1} C_{12}^{\mathrm{f}}+C_{1} C_{14}^{\mathrm{f}}+D_{1} C_{15}^{\mathrm{f}}-X_{1} e_{11}^{\mathrm{f}}-Y_{1} e_{21}^{\mathrm{f}}
\tag{22}
$$

$$
C_{12}^{\mathrm{c}}=A_{2} C_{11}^{\mathrm{f}}+B_{2} C_{12}^{\mathrm{f}}+C_{2} C_{14}^{\mathrm{f}}+D_{2} C_{15}^{\mathrm{f}}-X_{2} e_{11}^{\mathrm{f}}-Y_{2} e_{21}^{\mathrm{f}}
\tag{23}
$$

$$
C_{13}^{\mathrm{c}}=A_{3} C_{11}^{\mathrm{f}}+B_{3} C_{12}^{\mathrm{f}}+C_{3} C_{14}^{\mathrm{f}}+D_{3} C_{15}^{\mathrm{f}}-X_{3} e_{11}^{\mathrm{f}}-Y_{3} e_{21}^{\mathrm{f}}+C_{13}^{\mathrm{f}}
\tag{24}
$$

$$
C_{14}^{\mathrm{c}}=A_{4} C_{11}^{\mathrm{f}}+B_{4} C_{12}^{\mathrm{f}}+C_{4} C_{14}^{\mathrm{f}}+D_{4} C_{15}^{\mathrm{f}}-X_{4} e_{11}^{\mathrm{f}}-Y_{4} e_{21}^{\mathrm{f}}
\tag{25}
$$

$$
C_{15}^{\mathrm{c}}=A_{5} C_{11}^{\mathrm{f}}+B_{5} C_{12}^{\mathrm{f}}+C_{5} C_{14}^{\mathrm{f}}+D_{5} C_{15}^{\mathrm{f}}-X_{5} e_{11}^{\mathrm{f}}-Y_{5} e_{21}^{\mathrm{f}}
\tag{26}
$$

$$
C_{16}^{\mathrm{c}}=A_{6} C_{11}^{\mathrm{f}}+B_{6} C_{12}^{\mathrm{f}}+C_{6} C_{14}^{\mathrm{f}}+D_{6} C_{15}^{\mathrm{f}}-X_{6} e_{11}^{\mathrm{f}}-Y_{6} e_{21}^{\mathrm{f}}+C_{16}^{\mathrm{f}}
\tag{27}
$$

$$
e_{11}^{\mathrm{c}}=-\left(A_{7} C_{11}^{\mathrm{f}}+B_{7} C_{12}^{\mathrm{f}}+C_{7} C_{14}^{\mathrm{f}}+D_{7} C_{15}^{\mathrm{f}}-X_{7} e_{11}^{\mathrm{f}}-Y_{7} e_{21}^{\mathrm{f}}\right)
\tag{28}
$$

$$
e_{21}^{\mathrm{c}}=-\left(A_{8} C_{11}^{\mathrm{f}}+B_{8} C_{12}^{\mathrm{f}}+C_{8} C_{14}^{\mathrm{f}}+D_{8} C_{15}^{\mathrm{f}}-X_{8} e_{11}^{\mathrm{f}}-Y_{8} e_{21}^{\mathrm{f}}\right)
\tag{29}
$$

$$
e_{31}^{\mathrm{c}}=-\left(A_{9} C_{11}^{\mathrm{f}}+B_{9} C_{12}^{\mathrm{f}}+C_{9} C_{14}^{\mathrm{f}}+D_{9} C_{15}^{\mathrm{f}}-X_{9} e_{11}^{\mathrm{f}}-Y_{9} e_{21}^{\mathrm{f}}\right)+e_{31}^{\mathrm{f}}.
\tag{30}
$$

Similarly, Eqs. (3)-(15) coupled with Eq. (17) are used to identify all the 81 electromechanical constants of the composite material represented in Eq. (16) (45 of which are independent due to symmetry). While the solutions for the electromechanical constants of the 1-3 composite are presented in an implicit format for the most general case, explicit solutions for select combinations of 1-3 composites are presented in the following Sections 4.3 and 4.4.

### 4.3. Electromechanical response of a 1-3 composite with transversely isotropic and active constituents

For the case where the fiber and the matrix phases are both transversely isotropic and are poled in the longitudinal direction (Fig. 1a), the electromechanical constants of the composite material (e.g., in the first row of Eq. (16)) can be identified following the procedure outlined in Section 4.2 as:

$$
C_{11}^{\mathrm{c}}=A_{1} C_{11}^{\mathrm{f}}+B_{1} C_{12}^{\mathrm{f}}
\tag{31}
$$

$$
C_{12}^{\mathrm{c}}=A_{2} C_{11}^{\mathrm{f}}+B_{2} C_{12}^{\mathrm{f}}
\tag{32}
$$

$$
C_{13}^{\mathrm{c}}=C_{23}^{\mathrm{c}}=A_{3} C_{11}^{\mathrm{f}}+B_{3} C_{12}^{\mathrm{f}}+C_{13}^{\mathrm{f}}
\tag{33}
$$

$$
e_{31}^{\mathrm{c}}=e_{32}^{\mathrm{c}}=-\left(A_{9} C_{11}^{\mathrm{f}}+B_{9} C_{12}^{\mathrm{f}}\right)+e_{31}^{\mathrm{f}}
\tag{34}
$$

$$
C_{14}^{\mathrm{c}}=C_{15}^{\mathrm{c}}=C_{16}^{\mathrm{c}}=e_{11}^{\mathrm{c}}=e_{21}^{\mathrm{c}}=0.
\tag{35}
$$

The complete solution set is presented in Table 2.

For the case where the matrix and the fiber phases are both transversely isotropic and the matrix phase is poled in the transverse direction (Fig. 1b), matrices $A$ and $B$ (Eqs. (19) and (20)) are given as

$$
[A]=\left(\begin{array}{cccccc}
v_{\mathrm{m}} C_{11}^{\mathrm{f}}+v_{\mathrm{f}} C_{11}^{\mathrm{m}} & v_{\mathrm{m}} C_{12}^{\mathrm{f}}+v_{\mathrm{f}} C_{12}^{\mathrm{m}} & 0 & 0 & -v_{\mathrm{f}} e_{11}^{\mathrm{m}} & 0 \\
v_{\mathrm{m}} C_{12}^{\mathrm{f}}+v_{\mathrm{f}} C_{12}^{\mathrm{m}} & v_{\mathrm{m}} C_{22}^{\mathrm{f}}+v_{\mathrm{f}} C_{22}^{\mathrm{m}} & 0 & 0 & -v_{\mathrm{f}} e_{12}^{\mathrm{m}} & 0 \\
0 & 0 & v_{\mathrm{m}} C_{44}^{\mathrm{f}}+v_{\mathrm{f}} C_{44}^{\mathrm{m}} & 0 & 0 & -v_{\mathrm{m}} e_{24}^{\mathrm{f}} \\
0 & 0 & 0 & v_{\mathrm{m}} C_{55}^{\mathrm{f}}+v_{\mathrm{f}} C_{55}^{\mathrm{m}} & -v_{\mathrm{m}} e_{15}^{\mathrm{f}} & 0 \\
v_{\mathrm{f}} e_{11}^{\mathrm{m}} & v_{\mathrm{f}} e_{12}^{\mathrm{m}} & 0 & v_{\mathrm{m}} e_{15}^{\mathrm{f}} & \left(v_{\mathrm{m}} \kappa_{11}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right) & 0 \\
0 & 0 & v_{\mathrm{m}} e_{24}^{\mathrm{f}} & 0 & 0 & \left(v_{\mathrm{m}} \kappa_{22}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{22}^{\mathrm{m}}\right)
\end{array}\right)
\tag{36}
$$

### Table 2
The fundamental material properties of the 1-3 piezoelectric composite system predicted by the new model for the following two cases: (a) the fiber and the matrix phases are both transversely isotropic and poled in the longitudinal direction (Fig. 1a); and (b) the fiber and the matrix phases are both isotropic and passive

#### (a)
$$
C_{33}^{\mathrm{c}}=v_{\mathrm{f}}\left(A_{3}+B_{3}\right)\left(C_{13}^{\mathrm{f}}-C_{13}^{\mathrm{m}}\right)+v_{\mathrm{f}} C_{33}^{\mathrm{f}}+v_{\mathrm{m}} C_{33}^{\mathrm{m}}
$$

$$
C_{44}^{\mathrm{c}}=C_{55}^{\mathrm{c}}=C_{4} C_{44}^{\mathrm{f}}-Y_{4} e_{24}^{\mathrm{f}}
$$

$$
C_{66}^{\mathrm{c}}=v_{\mathrm{f}} C_{66}^{\mathrm{f}}+v_{\mathrm{m}} C_{66}^{\mathrm{m}}
$$

$$
e_{15}^{\mathrm{c}}=e_{24}^{\mathrm{c}}=-D_{7} C_{44}^{\mathrm{f}}+X_{7} e_{15}^{\mathrm{f}}
$$

$$
e_{33}^{\mathrm{c}}=v_{\mathrm{f}}\left(A_{3}+B_{3}\right)\left(e_{31}^{\mathrm{f}}-e_{31}^{\mathrm{m}}\right)+v_{\mathrm{f}} e_{33}^{\mathrm{f}}+v_{\mathrm{m}} e_{33}^{\mathrm{m}}
$$

$$
\kappa_{11}^{\mathrm{c}}=\kappa_{22}^{\mathrm{c}}=D_{7} e_{15}^{\mathrm{f}}+X_{7} \kappa_{11}^{\mathrm{f}}
$$

$$
\kappa_{33}^{\mathrm{c}}=v_{\mathrm{f}}\left(A_{9}+B_{9}\right)\left(e_{31}^{\mathrm{f}}-e_{31}^{\mathrm{m}}\right)+v_{\mathrm{f}} \kappa_{33}^{\mathrm{f}}+v_{\mathrm{m}} \kappa_{33}^{\mathrm{m}}
$$

$$
\begin{aligned}
C_{1}(v)= & \left(v_{\mathrm{m}}\right)^{2}\left[\left(C_{11}^{\mathrm{f}}\right)^{2}-\left(C_{12}^{\mathrm{f}}\right)^{2}\right]+\left(v_{\mathrm{f}}\right)^{2}\left[\left(C_{11}^{\mathrm{m}}\right)^{2}-\left(C_{12}^{\mathrm{m}}\right)^{2}\right] \\
& +2 v_{\mathrm{m}} v_{\mathrm{f}}\left(C_{11}^{\mathrm{f}} C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{12}^{\mathrm{m}}\right)
\end{aligned}
$$

$$
C_{2}(v)=v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}}-C_{12}^{\mathrm{f}}\right)+v_{\mathrm{f}}\left(C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{m}}\right)
$$

$$
C_{3}(v)=\left(v_{\mathrm{m}} C_{44}^{\mathrm{f}}+v_{\mathrm{f}} C_{44}^{\mathrm{m}}\right)\left(v_{\mathrm{m}} \kappa_{11}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right)+\left(v_{\mathrm{m}} e_{15}^{\mathrm{f}}+v_{\mathrm{f}} e_{15}^{\mathrm{m}}\right)^{2}
$$

$$
A_{1}=B_{2}=\left[v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}} C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{12}^{\mathrm{m}}\right)+v_{\mathrm{f}}\left(C_{11}^{\mathrm{m}} C_{11}^{\mathrm{f}}-C_{12}^{\mathrm{m}} C_{12}^{\mathrm{f}}\right)\right] / C_{1}(v)
$$

$$
A_{2}=B_{1}=v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}} C_{12}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{11}^{\mathrm{m}}\right) / C_{1}(v)
$$

$$
A_{3}=B_{3}=v_{\mathrm{m}}\left(C_{13}^{\mathrm{m}}-C_{13}^{\mathrm{f}}\right) / C_{2}(v)
$$

$$
A_{9}=B_{9}=v_{\mathrm{m}}\left(e_{31}^{\mathrm{m}}-e_{31}^{\mathrm{f}}\right) / C_{2}(v)
$$

$$
D_{7}=v_{\mathrm{m}}\left(e_{15}^{\mathrm{f}} \kappa_{11}^{\mathrm{m}}-\kappa_{11}^{\mathrm{f}} e_{15}^{\mathrm{m}}\right) / C_{3}(v)
$$

$$
X_{7}=\left\{v_{\mathrm{m}}\left[e_{15}^{\mathrm{f}} e_{15}^{\mathrm{m}}+C_{44}^{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right]+v_{\mathrm{f}}\left[\left(e_{15}^{\mathrm{m}}\right)^{2}+C_{44}^{\mathrm{m}} \kappa_{11}^{\mathrm{m}}\right]\right\} / C_{3}(v)
$$

$$
C_{4}=\left\{v_{\mathrm{m}}\left[C_{44}^{\mathrm{m}} \kappa_{11}^{\mathrm{f}}-e_{15}^{\mathrm{f}} e_{15}^{\mathrm{m}}\right]+v_{\mathrm{f}}\left[C_{44}^{\mathrm{m}} \kappa_{11}^{\mathrm{m}}-\left(e_{15}^{\mathrm{m}}\right)^{2}\right]\right\} / C_{3}(v)
$$

$$
Y_{4}=v_{\mathrm{m}}\left(e_{15}^{\mathrm{m}} C_{44}^{\mathrm{f}}-e_{15}^{\mathrm{f}} C_{44}^{\mathrm{m}}\right) / C_{3}(v)
$$

#### (b)
$$
C_{33}^{\mathrm{c}}=v_{\mathrm{f}}\left(A_{3}+B_{3}\right)\left(C_{12}^{\mathrm{f}}-C_{12}^{\mathrm{m}}\right)+v_{\mathrm{f}} C_{33}^{\mathrm{f}}+v_{\mathrm{m}} C_{33}^{\mathrm{m}}
$$

$$
C_{44}^{\mathrm{c}}=C_{55}^{\mathrm{c}}=C_{4} C_{44}^{\mathrm{f}}
$$

$$
C_{66}^{\mathrm{c}}=v_{\mathrm{f}} C_{66}^{\mathrm{f}}+v_{\mathrm{m}} C_{66}^{\mathrm{m}}
$$

$$
\kappa_{11}^{\mathrm{c}}=\kappa_{22}^{\mathrm{c}}=X_{7} \kappa_{11}^{\mathrm{f}}
$$

$$
\kappa_{33}^{\mathrm{c}}=v_{\mathrm{f}} \kappa_{33}^{\mathrm{f}}+v_{\mathrm{m}} \kappa_{33}^{\mathrm{m}}
$$

$$
\begin{aligned}
C_{1}(v)= & \left(v_{\mathrm{m}}\right)^{2}\left[\left(C_{11}^{\mathrm{f}}\right)^{2}-\left(C_{12}^{\mathrm{f}}\right)^{2}\right]+\left(v_{\mathrm{f}}\right)^{2}\left[\left(C_{11}^{\mathrm{m}}\right)^{2}-\left(C_{12}^{\mathrm{m}}\right)^{2}\right] \\
& +2 v_{\mathrm{m}} v_{\mathrm{f}}\left(C_{11}^{\mathrm{f}} C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{12}^{\mathrm{m}}\right)
\end{aligned}
$$

$$
C_{2}(v)=v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}}-C_{12}^{\mathrm{f}}\right)+v_{\mathrm{f}}\left(C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{m}}\right)
$$

$$
C_{3}(v)=\left(v_{\mathrm{m}} C_{44}^{\mathrm{f}}+v_{\mathrm{f}} C_{44}^{\mathrm{m}}\right)\left(v_{\mathrm{m}} \kappa_{11}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right)
$$

$$
A_{1}=B_{2}=\left[v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}} C_{11}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{12}^{\mathrm{m}}\right)+v_{\mathrm{f}}\left(C_{11}^{\mathrm{m}} C_{11}^{\mathrm{f}}-C_{12}^{\mathrm{m}} C_{12}^{\mathrm{f}}\right)\right] / C_{1}(v)
$$

$$
A_{2}=B_{1}=v_{\mathrm{m}}\left(C_{11}^{\mathrm{f}} C_{12}^{\mathrm{m}}-C_{12}^{\mathrm{f}} C_{11}^{\mathrm{m}}\right) / C_{1}(v)
$$

$$
A_{3}=B_{3}=v_{\mathrm{m}}\left(C_{12}^{\mathrm{m}}-C_{12}^{\mathrm{f}}\right) / C_{2}(v)
$$

$$
X_{7}=-\left(v_{\mathrm{m}} C_{44}^{\mathrm{f}}+v_{\mathrm{f}} C_{44}^{\mathrm{m}}\right) \kappa_{11}^{\mathrm{m}} / C_{3}(v)
$$

$$
C_{4}=\left(v_{\mathrm{m}} \kappa_{11}^{\mathrm{f}}+v_{\mathrm{f}} \kappa_{11}^{\mathrm{m}}\right) C_{44}^{\mathrm{m}} / C_{3}(v)
$$


$$
[B]=\begin{pmatrix}
C_{11}^{\mathrm{m}} & C_{12}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{13}^{\mathrm{m}}-C_{13}^{\mathrm{f}}\right) & 0 & 0 & 0 & -e_{11}^{\mathrm{m}} & 0 & v_{\mathrm{m}} e_{31}^{\mathrm{f}} \\
C_{12}^{\mathrm{m}} & C_{22}^{\mathrm{m}} & v_{\mathrm{m}}\left(C_{23}^{\mathrm{m}}-C_{23}^{\mathrm{f}}\right) & 0 & 0 & 0 & -e_{12}^{\mathrm{m}} & 0 & v_{\mathrm{m}} e_{32}^{\mathrm{f}} \\
0 & 0 & 0 & C_{44}^{\mathrm{m}} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & C_{55}^{\mathrm{m}} & 0 & 0 & 0 & -v_{\mathrm{m}} e_{35}^{\mathrm{m}} \\
e_{11}^{\mathrm{m}} & e_{12}^{\mathrm{m}} & v_{\mathrm{m}} e_{13}^{\mathrm{m}} & 0 & 0 & 0 & \kappa_{11}^{\mathrm{m}} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & v_{\mathrm{m}} e_{26}^{\mathrm{m}} & 0 & \kappa_{22}^{\mathrm{m}} & 0
\end{pmatrix}.
\tag{37}
$$

The electromechanical constants of the composite material (e.g., in the first row of Eq. (16)) are then presented as follows (see Table 3):
$$
C_{11}^{\mathrm{c}}=A_{1} C_{11}^{\mathrm{f}}+B_{1} C_{12}^{\mathrm{f}} \tag{38}
$$
$$
C_{12}^{\mathrm{c}}=A_{2} C_{11}^{\mathrm{f}}+B_{2} C_{12}^{\mathrm{f}} \tag{39}
$$
$$
C_{13}^{\mathrm{c}}=A_{3} C_{11}^{\mathrm{f}}+B_{3} C_{12}^{\mathrm{f}}+C_{13}^{\mathrm{f}} \tag{40}
$$
$$
e_{11}^{\mathrm{c}}=-\left(A_{7} C_{11}^{\mathrm{f}}+B_{7} C_{12}^{\mathrm{f}}\right) \tag{41}
$$
$$
e_{31}^{\mathrm{c}}=-\left(A_{9} C_{11}^{\mathrm{f}}+B_{9} C_{12}^{\mathrm{f}}\right)+e_{31}^{\mathrm{f}} \tag{42}
$$
$$
C_{14}^{\mathrm{c}}=C_{15}^{\mathrm{c}}=C_{16}^{\mathrm{c}}=e_{21}^{\mathrm{c}}=0. \tag{43}
$$

### 4.4. Electromechanical response of a 1-3 composite with isotropic and passive constituents

For the case where the fiber and the matrix phases are both isotropic and passive, the electromechanical constants of the composite material (in the first row of Eq. (16)) are presented as follows:
$$
C_{11}^{\mathrm{c}}=A_{1} C_{11}^{\mathrm{f}}+B_{1} C_{12}^{\mathrm{f}} \tag{44}
$$
$$
C_{12}^{\mathrm{c}}=A_{2} C_{11}^{\mathrm{f}}+B_{2} C_{12}^{\mathrm{f}} \tag{45}
$$
$$
C_{13}^{\mathrm{c}}=C_{23}^{\mathrm{c}}=A_{3} C_{11}^{\mathrm{f}}+B_{3} C_{12}^{\mathrm{f}} \tag{46}
$$
$$
C_{14}^{\mathrm{c}}=C_{15}^{\mathrm{c}}=C_{16}^{\mathrm{c}}=e_{11}^{\mathrm{c}}=e_{21}^{\mathrm{c}}=e_{31}^{\mathrm{c}}=0. \tag{47}
$$

The complete solution set is presented in Table 2.

**Table 3**
The fundamental properties of the matrix and the fiber constituents utilized for assessing the predictions of the model developed in the present study for 1-3 composites

|  | PZT-7A ($\rho=7700\ \text{kg/m}^3$) | BaTiO₃ ($\rho=5700\ \text{kg/m}^3$) | PVDF ($\rho=1770\ \text{kg/m}^3$) |
| --- | --- | --- | --- |
| $C_{11}^{E}$ (Pa) | $1.480\mathrm{E}+11$ | $1.504\mathrm{E}+11$ | $4.840\mathrm{E}+09$ |
| $C_{12}^{E}$ (Pa) | $7.620\mathrm{E}+10$ | $6.563\mathrm{E}+10$ | $2.720\mathrm{E}+09$ |
| $C_{22}^{E}$ (Pa) | $1.480\mathrm{E}+11$ | $1.504\mathrm{E}+11$ | $4.840\mathrm{E}+09$ |
| $C_{13}^{E}$ (Pa) | $7.420\mathrm{E}+10$ | $6.594\mathrm{E}+10$ | $2.220\mathrm{E}+09$ |
| $C_{23}^{E}$ (Pa) | $7.420\mathrm{E}+10$ | $6.594\mathrm{E}+10$ | $2.220\mathrm{E}+09$ |
| $C_{33}^{E}$ (Pa) | $1.310\mathrm{E}+11$ | $1.455\mathrm{E}+11$ | $4.630\mathrm{E}+09$ |
| $C_{44}^{E}$ (Pa) | $2.530\mathrm{E}+10$ | $4.386\mathrm{E}+10$ | $5.260\mathrm{E}+07$ |
| $C_{55}^{E}$ (Pa) | $2.530\mathrm{E}+10$ | $4.386\mathrm{E}+10$ | $5.260\mathrm{E}+07$ |
| $C_{66}^{E}$ (Pa) | $3.590\mathrm{E}+10$ | $4.237\mathrm{E}+10$ | $1.060\mathrm{E}+09$ |
| $e_{15}$ ($\text{C/m}^2$) | $9.310\mathrm{E}+01$ | $1.140\mathrm{E}+01$ | $-1.999\mathrm{E}-03$ |
| $e_{31}$ ($\text{C/m}^2$) | $-2.324\mathrm{E}+00$ | $-4.322\mathrm{E}+00$ | $4.344\mathrm{E}-03$ |
| $e_{33}$ ($\text{C/m}^2$) | $1.099\mathrm{E}+01$ | $1.736\mathrm{E}+01$ | $-1.099\mathrm{E}-01$ |
| $\kappa_{11}^{E}$ (C/Vm) | $3.984\mathrm{E}-09$ | $1.280\mathrm{E}-08$ | $6.641\mathrm{E}-11$ |
| $\kappa_{33}^{E}$ (C/Vm) | $2.081\mathrm{E}-09$ | $1.510\mathrm{E}-08$ | $7.083\mathrm{E}-11$ |

All the constituents are transversely isotropic and are poled in the longitudinal (i.e., 3) direction.

---

## 5. Comparison of the analytical model with models developed earlier

The predictions of the analytical model developed in the present study for the effective electromechanical responses of 1-3 composites are compared to the results of models developed earlier for specific conditions of material anisotropy and piezoelectric activity.

### 5.1. Comparison of analytical and numerical models for "longitudinal" composites

For model composite systems comprising of a transversely isotropic matrix (e.g., barium titanate or PVDF) and fiber (e.g., PZT-7A) where both the matrix and the fiber phases are poled in the longitudinal direction, the electromechanical constants predicted by the new model agree well with the asymptotic homogenization based model developed by Guinovart-Diaz et al. [12], the micromechanics based model presented by Dunn and Taya [5] and the unit-cell-based finite-element model formulated by Kar-Gupta and Venkatesh [14] for a wide range of volume fractions of the fiber phase (Fig. 3). The variations of the electromechanical constants with volume fraction of the fiber phase are generally linear for the barium titanate system and nonlinear for the PVDF-based system. The composite properties converge to the expected constituent properties in the limits of very low and very high volume fractions of the fiber phase.

It has also been verified that the results of the present analytical model reduce to the formulation presented by Chan and Unsworth [16] for composites with transversely isotropic and active fiber and passive matrix and to that of the model presented by Whitney and Riley [17] for composites where both the matrix and the fiber are isotropic and passive as well.

### 5.2. Comparison of analytical and numerical models for "transverse" composites

As the analytical models developed earlier [5,12] provide explicit solutions for the electromechanical

![](./images/812037237192523776_6.jpg)

Fig. 3. The electromechanical constants of a 1-3 piezocomposite predicted by the model developed in the present study compare well with the asymptotic homogenization (AHM) based model developed by Guinovart-Diaz et al. [12], the micromechanics (MM) based model developed by Dunn and Taya [5] and a finite-element model (FEM) [14] for two model "longitudinal" composite systems consisting of: (i) $BaTiO_{3}$ (matrix) and PZT-7A (fiber) and (ii) PVDF (matrix) and PZT-7A (fiber) (Table 3).

constants of "longitudinal" 1-3 composites where the matrix and fiber constituents conform to specific crystal symmetries, the predictions of the present analytical model for "transverse" composites are compared to the results of a finite-element model [14] for the barium titanate and the PVDF-based systems. Overall,

![](./images/812037237192523776_7.jpg)

Fig. 4. The electromechanical constants of a 1-3 piezocomposite predicted by the model developed in the present study compare well with the solutions of the finite-element (FEM) model [14] for two model "transverse" composite systems consisting of: (i) $BaTiO_{3}$ (matrix) and PZT-7A (fiber) and (ii) PVDF (matrix) and PZT-7A (fiber) (Table 3).

there is good agreement between the predictions of the analytical model and the finite-element results (Fig. 4).

While, in general, there is reasonable agreement between the predictions of the analytical model and the finite-element model for the "longitudinal" and "trans-

Table 4
The electromechanical constants of a barium titanate (matrix)–50% volume fraction PZT7A (fiber) ‘longitudinal’ composite where both the constituents are transversely isotropic, predicted by the model developed in the present study

| (a)                |                   |                   |                   |                   |                   |
|--------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| $1.489\text{E} + 11$ | $7.115\text{E} + 10$ | $6.999\text{E} + 10$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ |
| $7.115\text{E} + 10$ | $1.489\text{E} + 11$ | $6.999\text{E} + 10$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ |
| $6.999\text{E} + 10$ | $6.999\text{E} + 10$ | $1.381\text{E} + 11$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ |
| $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $3.235\text{E} + 10$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ |
| $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $3.235\text{E} + 10$ | $0.000\text{E} + 00$ |
| $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $3.914\text{E} + 10$ |
| (b)                |                   |                   |                   |                   |                   |
| 0.00               | 0.00              | 0.00              | 0.00              | 10.79             | 0.00              |
| 0.00               | 0.00              | 0.00              | 10.79             | 0.00              | 0.00              |
| $-3.34$            | $-3.34$           | 14.14             | 0.00              | 0.00              | 0.00              |
| (c)                |                   |                   |
| $6.485\text{E} - 09$ | $0.000\text{E} + 00$ | $0.000\text{E} + 00$ |
| $0.000\text{E} + 00$ | $6.485\text{E} - 09$ | $0.000\text{E} + 00$ |
| $0.000\text{E} + 00$ | $0.000\text{E} + 00$ | $8.599\text{E} - 09$ |

An inspection of (a) the elasticity constants (Pa), (b) the coupling constants ($\text{C}/\text{m}^2$), and (c) the permittivity constants ($\text{C}/\text{Vm}$) illustrates that the composite is also transversely isotropic.

<table>
<caption>Table 5<br>The 20 combinations of ‘longitudinal’ composite material systems utilized to assess the accuracy of the analytical model</caption>
<thead>
<tr>
<th rowspan="3">Fiber<sup>a</sup></th>
<th colspan="7">Matrix (‘longitudinal’)</th>
</tr>
<tr>
<th colspan="6">Barium titanate</th>
<th colspan="7">PVDF</th>
</tr>
<tr>
<th>I</th>
<th>II</th>
<th>III</th>
<th>IV</th>
<th>V</th>
<th>VI</th>
<th>VII</th>
<th>I</th>
<th>II</th>
<th>III</th>
<th>IV</th>
<th>V</th>
<th>VI</th>
<th>VII</th>
</tr>
</thead>
<tbody>
<tr>
<td>PZT-7A</td>
<td>0.98</td>
<td>0.98</td>
<td>0.90</td>
<td>0.31</td>
<td>0.31</td>
<td>0.14</td>
<td>0.63</td>
<td>30.58</td>
<td>30.58</td>
<td>28.29</td>
<td><strong>59.99</strong></td>
<td><strong>59.99</strong></td>
<td><strong>29.38</strong></td>
<td>100.03</td>
</tr>
<tr>
<td>Ammonium dihydrogen Phosphate</td>
<td>0.45</td>
<td>0.45</td>
<td><strong>0.23</strong></td>
<td>0.04</td>
<td>0.04</td>
<td>0.01</td>
<td>–</td>
<td>13.97</td>
<td>13.97</td>
<td><strong>7.30</strong></td>
<td>7.47</td>
<td>7.47</td>
<td>1.93</td>
<td>–</td>
</tr>
<tr>
<td>Barium sodium niobate</td>
<td><strong>1.59</strong></td>
<td><strong>1.64</strong></td>
<td>0.93</td>
<td><strong>0.16</strong></td>
<td><strong>0.17</strong></td>
<td><strong>0.03</strong></td>
<td><strong>0.25</strong></td>
<td><strong>49.36</strong></td>
<td><strong>51.12</strong></td>
<td>29.18</td>
<td>31.34</td>
<td>32.93</td>
<td>6.38</td>
<td><strong>39.46</strong></td>
</tr>
<tr>
<td>Lithium niobate</td>
<td>1.35</td>
<td>1.35</td>
<td><strong>1.67</strong></td>
<td>0.06</td>
<td>0.06</td>
<td>0.02</td>
<td>0.08</td>
<td>41.92</td>
<td>41.92</td>
<td><strong>52.51</strong></td>
<td>11.20</td>
<td>11.20</td>
<td>3.75</td>
<td>11.91</td>
</tr>
<tr>
<td>Quartz</td>
<td>0.58</td>
<td>0.58</td>
<td>0.74</td>
<td><strong>0.003</strong></td>
<td><strong>0.003</strong></td>
<td><strong>0.003</strong></td>
<td>–</td>
<td>17.92</td>
<td>17.92</td>
<td>23.15</td>
<td><strong>0.60</strong></td>
<td><strong>0.60</strong></td>
<td><strong>0.59</strong></td>
<td>–</td>
</tr>
<tr>
<td>Rochelle salt</td>
<td><strong>0.19</strong></td>
<td><strong>0.28</strong></td>
<td>0.27</td>
<td>0.14</td>
<td>0.01</td>
<td>0.01</td>
<td>–</td>
<td><strong>5.79</strong></td>
<td><strong>8.55</strong></td>
<td>8.50</td>
<td>27.33</td>
<td>1.28</td>
<td>1.19</td>
<td>–</td>
</tr>
<tr>
<td>Bismuth germanate</td>
<td>0.75</td>
<td>0.75</td>
<td>0.78</td>
<td>0.01</td>
<td>0.01</td>
<td>0.01</td>
<td>–</td>
<td>23.43</td>
<td>23.43</td>
<td>24.49</td>
<td>2.13</td>
<td>2.13</td>
<td>2.00</td>
<td>–</td>
</tr>
<tr>
<td>Cadmium sulfide</td>
<td>0.60</td>
<td>0.60</td>
<td>0.64</td>
<td>0.01</td>
<td>0.01</td>
<td>0.01</td>
<td><strong>0.03</strong></td>
<td>18.74</td>
<td>18.74</td>
<td>20.26</td>
<td>1.25</td>
<td>1.25</td>
<td>1.29</td>
<td><strong>4.16</strong></td>
</tr>
<tr>
<td>Telllerium dioxide</td>
<td>0.38</td>
<td>0.38</td>
<td>0.73</td>
<td>0.02</td>
<td>0.02</td>
<td>0.01</td>
<td>–</td>
<td>11.78</td>
<td>11.78</td>
<td>22.96</td>
<td>3.05</td>
<td>3.05</td>
<td>3.09</td>
<td>–</td>
</tr>
<tr>
<td>Zinc oxide</td>
<td>1.39</td>
<td>1.39</td>
<td>1.45</td>
<td>0.01</td>
<td>0.01</td>
<td>0.01</td>
<td>0.08</td>
<td>43.33</td>
<td>43.33</td>
<td>45.62</td>
<td>1.22</td>
<td>1.22</td>
<td>1.58</td>
<td>12.01</td>
</tr>
</tbody>
</table>

The minimum and maximum values for the ratio of the fiber and matrix properties are highlighted in bold.
$\text{I} = C_{11}^{\text{fiber}}/C_{11}^{\text{matrix}}$, $\text{II} = C_{22}^{\text{fiber}}/C_{22}^{\text{matrix}}$, $\text{III} = C_{33}^{\text{fiber}}/C_{33}^{\text{matrix}}$, $\text{IV} = \kappa_{11}^{\text{fiber}}/\kappa_{11}^{\text{matrix}}$, $\text{V} = \kappa_{22}^{\text{fiber}}/\kappa_{22}^{\text{matrix}}$, $\text{VI} = \kappa_{33}^{\text{fiber}}/\kappa_{33}^{\text{matrix}}$, $\text{VII} = e_{33}^{\text{fiber}}/e_{33}^{\text{matrix}}$.
<sup>a</sup> 10%, 30%, 50%, 70%.

verse" composites for two model material systems, the following observations are made.

1. Amongst all the electromechanical constants, those which are associated with the longitudinal direction (i.e., $C_{33}$ and $\kappa_{33}$) show greater agreement between the predictions of the analytical model and the finite-element model.

2. Composite material constants associated with the transverse direction (i.e., $C_{11}$, $C_{22}$, $\kappa_{11}$ and $\kappa_{22}$) show greater differences between the predictions of the analytical model and finite-element model, especially for the barium titanate based system. The observed differences in the material properties associated with the transverse direction could in part be due to the idealization of the fiber composite as a layered composite in the transverse direction and the subsequent recognition of simplified relationships between the (normal and shear) stresses and (normal and shear) strains in the transverse direction (Eqs. (7)–(12)).

The impact of the idealization of the fiber composite as a layered composite on the predictions of material properties for 1–3 composites is examined in detail in the following section.

### 5.3. Assessment of the accuracy of the analytical model

The accuracy of the analytical model in determining the composite electromechanical constants is examined by comparing the analytical model predictions with the finite-element model results for 20 material combinations each for the "longitudinal" and "transverse" composites, where the matrix and fiber constituents exhibit a wide

![](./images/812037237192523776_8.jpg)

Fig. 5. The accuracy of the analytical model developed in the present study in predicting the electromechanical constants of a "longitudinal" 1-3 composite is estimated by comparison with the results of a finite-element model, for a wide range of composite material systems.

range of elastic, dielectric and piezoelectric properties (Table 5).

From Figs. 5 and 6 it is evident that:

1. The material properties in the longitudinal direction (i.e., $C_{33}$, $\kappa_{33}$ and $e_{33}$) are well predicted by the analytical model for a wide range of composite materials wherein the elastic, piezoelectric and dielectric properties of the fiber and matrix constituents vary over nearly three, four and five orders of magnitude, respectively (Figs. 5c,d,g and 6c,g).
2. However, for the material properties in the transverse direction (i.e., $C_{11}$, $C_{22}$, $\kappa_{11}$ and $\kappa_{22}$), the analytical model generally underpredicts the composite properties. The

![](./images/812037237192523776_9.jpg)

Fig. 6. The accuracy of the analytical model developed in the present study in predicting the electromechanical constants of a "transverse" 1-3 composite is estimated by comparison with the results of a finite-element model, for a wide range of composite material systems.

differences between the analytical model predictions and the finite-element results are greater for those composites which exhibit higher differences between the matrix and the fiber properties. The largest differences (of almost 100%) between the results of the analytical and the finite-element models are observed for the dielectric properties (i.e., $\kappa_{11}$ and $\kappa_{22}$) of composite materials that are "matrix-dominant" (i.e., $\kappa_{11}^{\mathrm{fiber}} / \kappa_{11}^{\mathrm{matrix}} \ll 1$) while comparatively lesser differences are observed for the composite materials which are "fiber-dominant" (e.g., $\kappa_{11}^{\mathrm{fiber}} / \kappa_{11}^{\mathrm{matrix}} \gg$

![](./images/812037237192523776_10.jpg)

Fig. 7. The asymmetry in the differences between the analytical and the finite-element model predictions for "matrix-dominant" and "fiber-dominant" composite systems is examined by considering two model composite systems with the same matrix phase but with fiber phases that (relative to the matrix) are "stronger" (System 1) or "weaker" (System 2) by similar proportions.

<table>
  <tr>
    <th>Fiber</th>
    <th>Matrix<br>(longitudinal poling)</th>
    <th>Matrix<br>(transverse poling)</th>
    <th>Composite</th>
  </tr>
  <tr>
    <td>Anisotropic</td>
    <td>Anisotropic</td>
    <td>Anisotropic</td>
    <td>Anisotropic</td>
  </tr>
  <tr>
    <td>Transversely<br>isotropic (b)</td>
    <td>Transversely<br>isotropic (b)</td>
    <td>Transversely<br>isotropic (b)</td>
    <td>Transversely<br>isotropic (b)</td>
  </tr>
  <tr>
    <td>Transversely<br>isotropic (b)</td>
    <td>Transversely<br>isotropic<br>(c)</td>
    <td></td>
    <td>'m'<br>Symmetry</td>
  </tr>
  <tr>
    <td>Transversely<br>isotropic (b)</td>
    <td>Isotropic<br>(passive)</td>
    <td>Transversely<br>isotropic (b)</td>
    <td></td>
  </tr>
  <tr>
    <td>Isotropic<br>(passive)</td>
    <td>Isotropic<br>(passive)</td>
    <td>Transversely<br>isotropic (b)<br>(passive)</td>
    <td></td>
  </tr>
</table>

![](./images/812037237192523776_11.jpg)

Fig. 8. Schematics illustrating the crystal symmetry of 1-3 composites created by combining matrix and fiber constituents with varying degrees of anisotropy.

1). The observed asymmetry with regards to the differences between the analytical and finite-element models predictions in the "matrix-dominant" and "fiber-dominant" systems is further investigated by considering two material systems that have the same matrix phase but with fiber phases that have properties that are (approximately) equally higher or lower than that of the matrix (e.g., $\kappa_{11}^{\text{fiber}} / \kappa_{11}^{\text{matrix}}=8.04$ and $\kappa_{11}^{\text{matrix}} / \kappa_{11}^{\text{fiber}}=7.69$). Fig. 7 indicates that the "matrix-dominant" system does show a larger difference between the results of the analytical and the finite- element models over that of the "fiber-dominant" system.

3. The absolute magnitudes of differences in the properties predicted by the analytical and finite-element models (i.e., $|\kappa_{11}^{\text{analytical}} - \kappa_{11}^{\text{finite-element}}|$) are generally higher for composites with low-volume fractions of the fiber phase. However, the normalized differences (i.e., $|\kappa_{11}^{\text{analytical}} / \kappa_{11}^{\text{finite-element}}|$ or $|\kappa_{11}^{\text{analytical}} - \kappa_{11}^{\text{finite-element}}| / \kappa_{11}^{\text{finite-element}}|$) are lower for materials with lower volume fractions of the fiber phase. Thus, the results in Figs. 5 and 6 indicate that the composites with lower-volume fractions of the fiber phase demonstrate comparatively better agreement with the finite-element results than those with higher-fiber volume fractions.

Overall, in utilizing the analytical model developed in the present study (which approximates a 1-3 fiber composite as a layered composite (Fig. 2)) to predict composite material properties, particular attention must be paid to the differences in the properties of the matrix and the fiber constituents, as the analytical model could significantly underpredict the material properties in the transverse direction (especially, the dielectric properties - $\kappa_{11}$ and $\kappa_{22}$) for some ("matrix- dominant") composite material systems. In general, the results presented in Figs. 5 and 6 can be used to obtain a first-order (or approximate) estimate of the accuracy of the predictions of the analytical model for a given 1-3 composite.

## 6. Applications of the analytical model

### 6.1. Determination of crystal symmetry

As the new model developed in the present study can predict all the 45 independent electromechanical constants (Eq. (16)) that are required to formulate the complete constitutive behavior of the 1-3 piezocomposite system, the crystal symmetry group of the composite can be readily determined as well. For example, Table 4 presents the electromechanical constants for a barium titanate (matrix)-50% volume fraction PZT7A (fiber) "longitudinal" composite, where both the constituents are transversely isotropic. An inspection of the composite material properties indicates that the 1-3 system is also transversely isotropic. However, if a "transverse" composite is constructed from the same constituents (i.e., barium titanate (matrix)-50% volume fraction PZT7A (fiber)), but with the matrix phase poled in the transverse direction, a reduction in the resulting composite material symmetry to the "m" class is observed. Fig. 8 summarizes the symmetry classes observed for composites that correspond to several combinations of the matrix and the fiber phases.

### 6.2. Determination of figures of merit

Figures of merit help assess the utility of a given piezoelectric composite system for use in particular applications. Three figures of merit that are frequently invoked are described below.

The piezoelectric coupling constant $(k_{i})$ reflects the efficiency of electromechanical transduction [18], across the

![](./images/812037237192523776_12.jpg)

Fig. 9. The figures of merit such as the coupling constant (a), the acoustic impedance (b) and the hydrostatic charge coefficient (c) predicted by the model developed in the present study agree well with the results of finite- element computations for model barium titanate-PZT7A and PVDF- PZT7A "longitudinal" composites.

longitudinal (or thickness) direction (i.e., direction 3 (Fig. 1)) and is defined as

$$
k_{\mathrm{t}}=\sqrt{1-\frac{C_{33}^{E}}{C_{33}^{D}}}
\tag{48}
$$

where

$$
C_{33}^{D}=C_{33}^{E}+\frac{e_{33}^{2}}{\kappa_{33}^{c}}.
\tag{49}
$$

The acoustic impedance ($Z$) determines the fidelity of signal transfer across a substrate-transducer interface and is given by

$$
Z=\left(C_{33}^{D} \rho\right)^{1 / 2}
\tag{50}
$$

where $\rho$ is the density of the composite given by $\rho=v_{\mathrm{f}} \rho^{\mathrm{f}}+v_{\mathrm{m}} \rho^{\mathrm{m}}$.

The piezoelectric charge coefficient ($d_{\mathrm{h}}$) captures the effective strength of electromechanical coupling in a piezoelectric material, especially in the conversion of mechanical loads (under hydrostatic loading conditions) to electrical signals (in a given direction, e.g., 3) and is identified as $d_{\mathrm{h}}=d_{33}+d_{31}+d_{32}$.

In order to achieve optimal device performance in practical applications, the coupling constant and the piezoelectric charge coefficient need to be enhanced, while the acoustic impedance of the piezoelectric material has to be tailored to better match with that of the substrate material. As the present study enables the determination of all the fundamental electromechanical constants of 1-3 composites, the corresponding figures of merit can be predicted for several combinations of composite materials as well, as illustrated in Fig. 9.

### 7. Conclusions

With the recognition that 1-3 piezoelectric composites could provide enhanced mechanical flexibility and piezoelectric activity in a number of applications, there has been considerable interest in developing such novel composite materials. In conjunction with materials development efforts, several models that predict the electromechanical behavior of piezoelectric composites have been developed as well. However, the analytical models that predict the electromechanical response of piezoelectric composite materials are, in general, applicable to a limited set of piezoelectric materials. Hence, the current study focused on developing an analytical model to characterize the coupled behavior of a broad range of 1-3 piezoelectric composites with the following principal conclusions.

(i) Based on the elastic anisotropy and the piezoelectric activity of the constituent phases and the relative orientation of the poling directions of the fiber and the matrix phases, a large number of classes of 1-3 piezoelectric materials can be identified.

(ii) An analytical model that captures the complete electromechanical response of a 1-3 piezoelectric composite system where both the matrix and fiber phases could, in general, be elastically anisotropic and piezoelectrically active has been developed. A detailed methodology for determining all the 45 independent material constants of the 1-3 composite for several combinations of the fiber and matrix phases has been presented.

(iii) By comparing the predictions of the analytical model with those of a finite-element model for a range of composite materials, it is demonstrated that the composite material properties in the longitudinal direction (i.e., $C_{33}, \kappa_{33}$, and $\mathrm{e}_{33}$) are well predicted by the analytical model. However, as a consequence of the approximation introduced in the model formulation (where the fiber composite is modeled as a layered composite) the analytical model could significantly underpredict the composite material properties in the transverse direction (especially, the dielectric properties - $\kappa_{11}$ and $\kappa_{22}$) for some ("matrix-dominant") composite material systems. The composite systems where the fiber properties are dominant show greater agreement with finite-element results than those systems where the matrix properties are dominant.

(iv) Because all the 45 independent fundamental material constants are readily determined through the present model, the crystal symmetry of the composite materials can be unambiguously identified as well. In general, the "transverse" composites where the matrix is poled in the transverse direction (i.e., orthogonal to the long-axis of the fiber) exhibit lower-order symmetry compared to the "longitudinal" composites where the matrix is poled in the longitudinal direction (i.e., parallel to the long-axis of the fiber).

(v) The fundamental material constants predicted by the model can also be invoked to quantify the corresponding figures of merit that help assess the utility of piezoelectric materials for practical applications.

### Acknowledgement

The present study was supported in part by National Science Foundation Grant DMR-0547903.

### References

[1] Taunaumang H, Guy IL, Chan HLW. J Appl Phys 1994;76: 484-9.
[2] Chan HLW, Ng PKL, Choy CL. Appl Phys Lett 1999;74: 3029-31.
[3] Newnham RE, Skinner DP, Cross LE. Mater Res Bull 1978;13: 525-36.
[4] Banno H. Ceram Bull 1987;66:1332-7.
[5] Dunn ML, Taya M. Int J Solids Struct 1993;30:161-75.
[6] Bisegna P, Luciano R. J Mech Phys Solids 1996;44:583-602.

[7] Bisegna P, Luciano R. J Mech Phys Solids 1996;45:1329–56.

[8] Poizat C, Sester M. Comput Mater Sci 1997;16:89–97.

[9] Nan C, Weng GJ. J Appl Phys 2000;88:416–23.

[10] Smith WA, Auld BA. IEEE Trans Ultrason Ferroelectr Freq Control 1991;38:40–6.

[11] Smith WA. IEEE Trans Ultrason Ferroelectr Freq Control 1993;40:41–8.

[12] Guinovart-Diaz R, Bravo-Castillero J, Rodriguez-Ramos R, Sabina FJ, Martinez-Rosado R. Mater Lett 2001;48:93–8.

[13] Pettermann HE, Suresh S. Int J Solids Struct 2000;37:5447–64.

[14] Kar-Gupta R, Venkatesh TA. J Appl Phys 2005;98:054102-1–054102-14.

[15] Nye JF. Physical properties of crystals. Oxford: Clarendon Press; 1985.

[16] Chan HLW, Unsworth J. IEEE Trans Ultrason Ferroelectr Freq Control 1989;36:434–41.

[17] Whitney JM, Riley MB. AIAA J 1966;4:1537–42.

[18] Uchino K. Ferroelectric devices. New York: Marcel Dekker; 2000.

[19] Hull D, Clyne TW. An introduction to composite materials. New York: Cambridge University Press; 1996.