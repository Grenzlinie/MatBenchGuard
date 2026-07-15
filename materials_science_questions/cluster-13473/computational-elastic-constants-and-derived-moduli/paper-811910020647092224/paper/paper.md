# Young's modulus of silicon nanoplates at finite temperature

Jing Wang, Qing-An Huang*, Hong Yu

Key Laboratory of MEMS of Ministry of Education, Southeast University, Nanjing 210096, China

---

## ARTICLE INFO
Article history:
Received 27 April 2008
Received in revised form 17 July 2008
Accepted 18 July 2008
Available online 6 August 2008

PACS:
62.25.+g

Keywords:
Silicon
Nanoplate
Young's modulus
Surface reconstruction
Temperature

## ABSTRACT
Based on the Keating model, a semi-continuum approach is developed in which the strain energy of silicon nanoplates is presented. Using the quasiharmonic approximation, the temperature dependence of the lattice parameter of silicon has been coupled into the semi-continuum approach. By considering $(2\times 1)$ surface reconstruction of the silicon nanoplate, Young's moduli at finite temperature are modeled and the surface effects on the mechanical properties of the silicon nanoplate are predicted. As the nanoplate thickness is scaled down to 100 nm, Young's moduli begin to deviate from that of the bulk silicon. It is interesting to note that Young's moduli exhibits opposite behavior with and without surface reconstruction. Without surface reconstruction, Young's modulus of the nanoplate decreases dramatically as the nanoplate is scaled down to several tens of nanometer, which means that the nanoplate is elastically softer than bulk. The surface reconstruction leads to stronger bonds and hence an increase in the Young's modulus of the material as it is scaled down, which makes the nanoplate stiffer along the $[1\ 0\ 0]$ direction. Young's modulus of the nanoplate exhibits a negative temperature coefficient.

© 2008 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Microelectromechanical systems (MEMS) and nanoelectrome-chanical systems (NEMS) are the important branch of the micro/nano technology. MEMS have been widely applied in many areas including communications, mechanical, informational, biological technologies. Due to the small mass and size, NEMS offer immense potential for new applications and fundamental measurements [1–4]. The classical physical models or continuum theories have been used to analyze MEMS, which are mainstays in the micromecha-nical realm. They may not be directly applicable in the nanoworld because of the small scales encountered in NEMS. The mechanical properties of nanostructures deviate from their microscopic and macroscopic counterparts. Fundamental frequencies in the micro-wave range, mechanical quality factors in the tens of thousands, and force sensitivities at the attonewton level, of NEMS necessitate a proper understanding and the development of accurate physical theories for NEMS.

A great deal of experiments has been done on the mechanical properties of nanoscale materials. The nanostructures can be stiffer [5] or softer [6,7] than their bulk counterparts. For silicon nano-beam, some experiments have proved that Young's modulus decreases monotonously as its thickness is scaled down [7], while others show that there is no significant dependent and is a little larger than the bulk in width [8].

As structures become nanoscale, macroscopic mechanics will break down and atomistic behavior will emerge. Atomistic simulation methods such as ab initio calculations, molecular dynamics (MD), and Monte Carlo (MC) simulations, have been employed for an accurate analysis of systems comprising several hundreds of atoms [9–11]. MD simulations have shown that Young's moduli of the nanostructures are size dependent and can be impacted by the surface reconstruction [12–14]. The coarse-grained molecular dynamics, which combined MD with finite element method, has been used for NEMS [15,16]. Although the characteristic length of NEMS is often a few nanometers, a large number of atoms are involved. Therefore, computational cost is an inherent drawback within them.

In addition, theoretical investigations have been developed to evaluate the elastic properties of structures ranging from nano to micrometer scales. A semi-continuum approach has been devel-oped to provide a simpler and yet a reasonably accurate description of the nanostructures, which also predict softer or stiffer nanoplate [17,18].

The physics encountered in NEMS, are different from MEMS. As the characteristic length of NEMS scales down to several tens of nanometers, the surface-to-volume ratio greatly increases, and physical property becomes increasingly dominated by the

* Corresponding author. Tel.: +86 25 83792632; fax: +86 25 83792939.
E-mail address: hqa@seu.edu.cn (Q.-A. Huang).

0169-4332/$ – see front matter © 2008 Elsevier B.V. All rights reserved.
doi:10.1016/j.apsusc.2008.07.172

surfaces. Surface reconstruction impacts nanostructure elasticity [12-14,19] and is prominent at nanoscale, which may be insignificant at the macroscale. Besides surface reconstruction, the effects of surface tension, surface relaxation, and surface native oxide play important roles in the mechanical properties of the nanostructures [18,20].

To achieve the goal of accurately capturing the atomistic physics and retaining the efficiency of continuum models, a semi-continuum approach is developed here to compute Young's modulus of a silicon nanoplate. The effect of surface reconstruction on the silicon nanoplate is predicted. The temperature dependence of the elasticity of the nanostructures is important for the NEMS design. Based on quasiharmonic approximation, the temperature dependence of the silicon lattice parameter has been coupled into the semi-continuum approach. The temperature dependence of Young's modulus of the nanoplate is also predicted.

### 2. 3D model of a silicon nanoplate

#### 2.1. Atomistic level description
A three-dimensional silicon (0 0 1) nanoplate, which is the prototype of study, is uniform in thickness and infinite in length and width. One layer thickness is assumed to be a silicon crystal cell with lattice parameter $4a$, and the model for the silicon plate has $N(N=1,2,3,...)$ crystal cells along the thickness. A rectangular coordinate system is taken with $x$ and $y$ axes along the length and the width directions of the plate, and $z$ axis along the thickness direction perpendicular to the nanoplate surface, as shown in Fig. 1.

An arbitrary atom is chosen to be the origin of the silicon lattice, which occupies the $i$th, $j$th rows, and $k$th column and can be identified by a unique expression $(x_{i}, y_{j}, z_{l})$. For simplicity, the expression can be rewritten by $(i,j,l)$. Denote unit vectors along the $x$, $y$ and $z$ axes by $\vec{k_{1}}$, $\vec{k_{2}}$ and $\vec{k_{3}}$, respectively. Thus the position of any other atom in the lattice can be identified by a unique set of integers $l_{1}$, $l_{2}$ and $l_{3}$ with a displacement vector, $\vec{r}=l_{1}a\vec{k_{1}}+l_{2}a\vec{k_{2}}+l_{3}a\vec{k_{3}}$. Thus, the position of the atom can be denoted by $(x_{i}+l_{1}a, y_{j}+l_{2}a, z_{l}+l_{3}a)$, simplified by $(i+l_{1},j+l_{2},l+l_{3})$.

![](./images/811910020647092224_1.jpg)
Fig. 1. 3D model of a (0 0 1) silicon nanoplate.

In a silicon crystal cell, atoms are connected by covalent bonds and each of them is tetrahedrally bonded to four nearest-neighboring atoms, as shown in Fig. 1. The discrete solid spheres denote atoms, and the short solid lines connecting these spheres denote atomic bonds. There are four tetrahedrons in the silicon crystal cell. The representative atom of the crystal cell is identified by the number of 1, which occupies the position $(i,j,l)$. In the tetrahedron containing atom 1, atoms occupy the following positions: $0, (i+1, j+1, l+1)$; $1, (i,j,l)$; $2, (i,j+2,l+2)$; $3, (i+2,j,l+2)$; $4, (i+2,j+2,l)$, and the atomic labeling is shown in Fig. 1.

The displacement components of the atom $(i,j,l)$ along the $x$, $y$ and $z$ directions can be denote by $u^{l}(i,j)$, $v^{l}(i,j)$ and $w^{l}(i,j)$, simplified to $u_{i,j}^{l}$, $v_{i,j}^{l}$, $w_{i,j}^{l}$. The classical continuum treatment is based on the assumption that displacements vary sufficiently slowly from atom to atom in each layer. Therefore, the discrete displacement components $u_{i,j}^{l}$, $v_{i,j}^{l}$ and $w_{i,j}^{l}$ of the atom $(i,j,l)$ can be expressed with continuous function of $x$ and $y$, i.e., $u_{i,j}^{l}=u^{l}(x_{i},y_{j})$, $v_{i,j}^{l}=v^{l}(x_{i},y_{j})$ and $w_{i,j}^{l}=w^{l}(x_{i},y_{j})$. The displacement keeps the continuum along the length and width directions and has the discrete nature along the thickness direction.

With the assumption that displacements in each layer vary slowly from atom to atom, the displacement component of the atom $(i+1,j,l)$ along the $x$ direction $u_{i+1,j}^{l}$ can be expanded in a two-term Taylor series expansion [17]
$$
u_{i+1,j}^{l}=u_{i,j}^{l}+\left.\frac{\partial u^{l}(x,y)}{\partial x}\right|_{(x_{i},y_{j})}(x_{i+1}-x_{i}). \tag{1}
$$

The displacement components along others direction can be expanded in the same way. If there are more than one atom present in the primitive unit cell, internal strains would occur within the cell. Hence the internal strain exists between the atom at the diagonal of the silicon crystal cell and the atom at non-diagonal. The expression of the displacement component expansion should add a term of internal strain for silicon,
$$
u_{i+1,j}^{l}=u_{i,j}^{l}+\left.\frac{\partial u^{l}(x,y)}{\partial x}\right|_{(x_{i},y_{j})}(x_{i+1}-x_{i})+u', \tag{2}
$$
where $u'$ is the component of internal strain along the $x$ direction. The components of internal strain along $y$ and $z$ directions are denoted by $v'$ and $w'$, respectively.

#### 2.2. Keating model
For a microscopic description of silicon, the Keating model is employed in this work, which has been used extensively to investigate the elastic properties of silicon [21]. In the Keating model, the elastic strain energy of a given system is calculated through the bond topology description. The strain energy of a crystal is subjected to various physical requirements, such as rotational and displacement invariance, which ensure that the strain energy $U$ depends only on the differences between atom positions, i.e., $U=U(r_{i}-r_{j})$, where $r_{i}$ and $r_{j}$ are the position vectors of the $i$th and $j$th atoms after deformation, respectively.

In the Keating model, the strain energy is expressed as the sum of the nearest-neighbor and the next nearest-neighbor interac-

tions. The strain energy $U$ of the system is given by

$$
U=\frac{1}{2} k_{b} \sum_{i}\left(R_{i}^{2}-r_{i}^{2}\right)^{2}+\frac{1}{2} k_{\theta} \sum_{i, j>i}\left(R_{i} R_{j}-r_{i} r_{j}\right)^{2},
\tag{3}
$$

where $r_{i}$ and $r_{j}$ are the equilibrium position vectors of the $i$ th and the $j$ th bonds, $R_{i}$ and $R_{j}$ are the position vectors of the $i$ th and $j$ th bonds after deformation, respectively. The force constants $k_{b}$ and $k_{\theta}$ essentially describe the bond-stretching and bond-bending restoring forces. While several different force constants sets have been presented for the Keating model, the constants values of silicon from Ref. [22] are used in this work, where $k_{b}=6.187 \times 10^{20} \mathrm{~N} / \mathrm{m}^{3}$ and $k_{\theta}=1.813 \times 10^{20} \mathrm{~N} / \mathrm{m}^{3}$.

### 2.3. Semi-continuum approach

For the semi-continuum approach, the key idea is to adopt the framework of continuum mechanics while it describes the material properties and the constitutive relations by the atomistic description of the underlying local environment.

For a nanoplate, the in-plane dimensions are assumed to be very large compared to the thickness dimension, which allows us to employ the classical continuum description in the $x$ and $y$ directions and investigate the thickness direction with a discrete treatment. In other words, the physical quantities are viewed as continuous in the $x$ and $y$ directions but discrete along the thickness direction.

If the strain energy of the representative element is denoted by $U_{\text {cell }}$, where the subscript (cell) denotes the cell from the origin atom $(i, j, l)$, the total strain energy of the nanoplate $U_{\text {tot }}$, can be obtained by the sum of all cells

$$
U_{\text {tot }}=\sum_{i} \sum_{j} \sum_{l} U_{\text {cell }}.
\tag{4}
$$

Due to the translation invariance of the tetrahedron in silicon crystal cell, their strain energies are equal. The strain energy of a tetrahedron in silicon crystal cell $U_{\text {tet }}$ can be written as [21]

$$
\begin{aligned}
U_{\text {tet }} & =\frac{1}{2} k_{b} \sum_{i=1}^{4}\left(R_{0 i}^{2}-r_{0 i}^{2}\right)^{2}+\frac{1}{2} k_{\theta} \sum_{i=1, j>i}^{4}\left(R_{0 i} R_{0 j}-r_{0 i} r_{0 j}\right)^{2} \\
& =\sum_{i=1}^{4} U_{0 i}^{b}+\sum_{i=1, j>i}^{4} U_{01,0 j}^{\theta},
\end{aligned}
\tag{5}
$$

where $r_{0 j}$ is the position vector of the bond between atom 0 and $j$ (bond $0 j$ ), $R_{0 j}$ is the position vector of the bond $0 j$ after deformation, $U_{0 i}^{b}$ is the deformation energy of the bond $0 i$ stretching, $U_{0 i, 0 j}^{\theta}$ is the deformation energy of the bond bending between bonds $0 i$ and $0 j$.

Deformation energies of bond stretching and of bond bending are calculated as follows. The detail derivations of $U_{01}^{b}$ and $U_{01,02}^{\theta}$ are given by

$$
\begin{aligned}
U_{01}^{b}= & \frac{1}{2} k_{b}\left(R_{01}^{2}-r_{01}^{2}\right)^{2}=\frac{1}{2} k_{b}\left[\left(a+u_{i+1, j+1}^{l+1}-u_{i, j}^{l}\right)^{2}+\left(a+v_{i+1, j+1}^{l+1}-v_{i, j}^{l}\right)^{2}+\left(a+w_{i+1, j+1}^{l+1}-w_{i, j}^{l}\right)^{2}-\left(a^{2}+a^{2}+a^{2}\right)\right]^{2} \\
\approx & 2 k_{b} a^{2}\left(u_{i+1, j+1}^{l+1}-u_{i, j}^{l}+v_{i+1, j+1}^{l+1}-v_{i, j}^{l}+w_{i+1, j+1}^{l+1}-w_{i, j}^{l}\right)^{2}=2 k_{b} a^{2}\left[u^{l+1}\left(x_{i+1}, y_{j+1}\right)-u^{l}\left(x_{i}, y_{j}\right)+v^{l+1}\left(x_{i+1}, y_{j+1}\right)\right. \\
& \left.-v^{l}\left(x_{i}, y_{j}\right)+w^{l+1}\left(x_{i+1}, y_{j+1}\right)-w^{l}\left(x_{i}, y_{j}\right)\right]^{2} \approx 2 k_{b} a^{2}\left\{u^{l}\left(x_{i}, y_{j}\right)+a\left[\frac{\partial u^{l}(x, y)}{\partial x}+\frac{\partial u^{l}(x, y)}{\partial y}+\frac{u^{l+1}(x, y)-u^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)} \\
& +u^{l}-u^{l}\left(x_{i}, y_{j}\right)+v^{l}\left(x_{i}, y_{j}\right)+a\left[\frac{\partial v^{l}(x, y)}{\partial x}+\frac{\partial v^{l}(x, y)}{\partial y}+\frac{v^{l+1}(x, y)-v^{l}(x, y)}{a}\right]\left.\right|_{\left(x_{i}, y_{j}\right)}+v^{l}-v^{l}\left(x_{i}, y_{j}\right)+w^{l}\left(x_{i}, y_{j}\right) \\
& \left.+a\left[\frac{\partial w^{l}(x, y)}{\partial x}+\frac{\partial w^{l}(x, y)}{\partial y}+\frac{w^{l+1}(x, y)-w^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}+w^{l}-w^{l}\left(x_{i}, y_{j}\right)\}^{2} \\
= & 2 k_{b} a^{2}\left\{a\left[\frac{\partial u^{l}(x, y)}{\partial x}+\frac{\partial u^{l}(x, y)}{\partial y}+\frac{u^{l+1}(x, y)-u^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}+u^{l}+a\left[\frac{\partial v^{l}(x, y)}{\partial x}+\frac{\partial v^{l}(x, y)}{\partial y}+\frac{v^{l+1}(x, y)-v^{l}(x, y)}{a}\right]\left.\right|_{\left(x_{i}, y_{j}\right)} \\
& \left.+v^{l}+a\left[\frac{\partial w^{l}(x, y)}{\partial x}+\frac{\partial w^{l}(x, y)}{\partial y}+\frac{w^{l+1}(x, y)-w^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}+w^{l}\right\}^{2},
\end{aligned}
\tag{6}
$$

$$
\begin{aligned}
U_{01,02}^{\theta}= & \frac{1}{2} k_{\theta}\left(R_{01} R_{02}-r_{01} r_{02}\right)^{2}=\frac{1}{2} k_{\theta}\left[\left(a+u_{i+1, j+1}^{l+1}-u_{i, j}^{l}\right)\left(a+u_{i+1, j+1}^{l+1}-u_{i, j+2}^{l+2}\right)+\left(a+v_{i+1, j+1}^{l+1}-v_{i, j}^{l}\right)\left(a+v_{i+1, j+1}^{l+1}-v_{i, j+2}^{l+2}\right)\right. \\
& \left.+\left(a+w_{i+1, j+1}^{l+1}-w_{i, j}^{l}\right)\left(a+w_{i+1, j+1}^{l+1}-w_{i, j+2}^{l+2}\right)-\left(a^{2}-a^{2}-a^{2}\right)\right]^{2} \approx \frac{1}{2} k_{\theta} a^{2}\left(u_{i+1, j+1}^{l+1}-u_{i, j}^{l}+u_{i+1, j+1}^{l+1}-u_{i, j+2}^{l+2}+v_{i, j}^{l}-v_{i, j+2}^{l+2}+w_{i, j}^{l}\right. \\
& \left.-w_{i, j+2}^{l+2}\right)^{2}=\frac{1}{2} k_{\theta} a^{2}\left\{\left.a\left[\frac{\partial u^{l}(x, y)}{\partial x}+\frac{\partial u^{l}(x, y)}{\partial y}+\frac{u^{l+1}(x, y)-u^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}+u^{l}+\left.a\left[\frac{\partial u^{l}(x, y)}{\partial x}-\frac{\partial u^{l}(x, y)}{\partial y}-\frac{u^{l+1}(x, y)-u^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}\right. \\
& \left.+\left.u^{l}-2 a\left[\frac{\partial v^{l}(x, y)}{\partial y}+\frac{v^{l+1}(x, y)-v^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)}-2 a\left[\frac{\partial w^{l}(x, y)}{\partial y}+\frac{w^{l+1}(x, y)-w^{l}(x, y)}{a}\right]\right|_{\left(x_{i}, y_{j}\right)} ^{2}\right\}.
\end{aligned}
\tag{7}
$$

Since the deformation is small and the strain varies sufficiently slowly, the macroscopic elasticity is a useful concept. The elastic strains in the silicon nanoplate are defined as [17]

$$
\begin{aligned}
\varepsilon_{x x} & =\frac{\partial u}{\partial x}, \quad \varepsilon_{y y}=\frac{\partial v}{\partial y}, \quad \varepsilon_{z z}=\frac{w^{l+1}-w^{l}}{a}, \quad \gamma_{x y} \\
& =\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y}, \quad \gamma_{z x}=\frac{u^{l+1}-u^{l}}{a}+\frac{\partial w}{\partial x}, \quad \gamma_{y z}=\frac{\partial w}{\partial y}+\frac{v^{l+1}-v^{l}}{a}
\end{aligned}
\tag{8}
$$

Then $U_{01}^{b}$ and $U_{01,02}^{\theta}$ can be expressed as the functions of elastic strain.

$$
U_{01}^{b}=2 k_{b} a^{4}\left(\varepsilon_{x x}+\varepsilon_{y y}+\varepsilon_{z z}+\gamma_{x y}+\gamma_{y z}+\gamma_{z x}+\frac{u^{l}+v^{l}+w^{l}}{a}\right)^{2}, \quad(9)
$$

$$
U_{01,02}^{\theta}=2 k_{\theta} a^{4}\left(\varepsilon_{x x}-\varepsilon_{y y}-\varepsilon_{z z}-\gamma_{y z}+\frac{u^{l}}{a}\right)^{2}.
\tag{10}
$$

Other deformation energies of bond stretching and bond bending can be obtained in the same way. Therefore, the deformation energy of a silicon cell can be written as [21]

$$
\begin{aligned}
U_{\text {cell }}= & \sum_{i=1}^{4} U_{\text {tet }}=8 k_{b} a\left[\left(\varepsilon_{x x}+\varepsilon_{y y}+\varepsilon_{z z}+\gamma_{x y}+\gamma_{z x}+\gamma_{y z}+\frac{u^{\prime}+v^{\prime}+w^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}+\varepsilon_{y y}+\varepsilon_{z z}-\gamma_{x y}+\gamma_{z x}-\gamma_{y z}-\frac{u^{\prime}-v^{\prime}+w^{\prime}}{a}\right)^{2}\right. \\
& \left.+\left(\varepsilon_{x x}+\varepsilon_{y y}+\varepsilon_{z z}-\gamma_{x y}-\gamma_{z x}+\gamma_{y z}+\frac{u^{\prime}-v^{\prime}-w^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}+\varepsilon_{y y}+\varepsilon_{z z}+\gamma_{x y}-\gamma_{z x}-\gamma_{y z}-\frac{u^{\prime}+v^{\prime}-w^{\prime}}{a}\right)^{2}\right] \\
& +8 k_{\theta} a^{4}\left[\left(\varepsilon_{x x}-\varepsilon_{y y}-\varepsilon_{z z}-\gamma_{y z}+\frac{u^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}-\varepsilon_{y y}+\varepsilon_{z z}+\gamma_{z x}-\frac{v^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}+\varepsilon_{y y}-\varepsilon_{z z}+\gamma_{x y}-\frac{w^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}+\varepsilon_{y y}-\varepsilon_{z z}-\gamma_{x y}+\frac{w^{\prime}}{a}\right)^{2}\right. \\
& \left.+\left(\varepsilon_{x x}-\varepsilon_{y y}+\varepsilon_{z z}-\gamma_{z x}+\frac{v^{\prime}}{a}\right)^{2}+\left(\varepsilon_{x x}-\varepsilon_{y y}-\varepsilon_{z z}+\gamma_{y z}-\frac{u^{\prime}}{a}\right)^{2}\right]
\end{aligned}
$$

(11)

By imposing the condition $\partial U_{\text {cell }} / \partial u^{\prime}=\partial U_{\text {cell }} / \partial v^{\prime}=\partial U_{\text {cell }} / \partial w^{\prime}=0$, we obtain $u^{\prime}=\left(a\left(k_{\theta}-2 k_{b}\right) / k_{\theta}+2 k_{b}\right) \gamma_{y z}, v^{\prime}=\left(a\left(k_{\theta}-2 k_{b}\right) / k_{\theta}+\right.$ $\left.2 k_{b}\right) \gamma_{x z}$ and $w^{\prime}=\left(a\left(k_{\theta}-2 k_{b}\right) / k_{\theta}+2 k_{b}\right) \gamma_{x y}$. Substituting internal strain into Eq. (11) and then Eq. (4), the total strain energy of the nanoplate can be obtained.

The average strain energy density $f$ is defined as the ratio of the total strain energy $U_{\text {tot }}$ to the volume $v$ of the system, i.e., $f=U_{\text {tot }} / v$. Because the periodicity of the crystal lattice in the $x-y$ plane, the periodic calculation element is chosen to contain $N(=1 \times 1 \times N)$ crystal cell. Thus the calculation element volume is $v=4 a \times 4 a \times h$, where $h$ is the thickness of the nanoplate. It is reasonable to define the nanoplate thickness as the product of the thickness of one atom layer multiplied by the number of the atom layers [21], which gives $h=(4 N+1) a$.

Since $\sigma_{x x}=E \varepsilon_{x x}$ and $\sigma_{i j}=\partial f / \partial \varepsilon_{i j}(i, j=1,2, \ldots, 6)$ for simple tension, where $i$ and $j(=1,2, \ldots, 6)$ correspond to $x, y, z, x y, y z$, and $z x$, respectively. Young's modulus $E$ of the nanoplate along the $x$ direction is finally given by

$$
E=\frac{4 N a}{4 N+1}\left(k_{b}+\frac{3 k_{\theta}}{2}\right) .
$$

(12)

It is evident that Young's modulus of the Si (0 01$)$ nanoplate is dependent on the number of atomic layers $N$, which is size dependent.

### 2.4. D. Silicon surface model

In this work, we consider $(2 \times 1)$ surface reconstruction in the $\operatorname{Si}(001)$ surface. Both classical potentials and $a b$ initio calculations have been used to systematically examine the reconstruction of the $\operatorname{Si}(001)$ surfaces, and most calculations agree on the essentials of the $\operatorname{Si}(001)(2 \times 1)$ reconstruction with the dimer bond along the (1 10 ) direction, which is along the in-plane diagonal direction on the Si (0 01$)$ surfaces [23-26]. For $(2 \times 1)$ reconstruction, surface atom also retains a dangling bond in this work. Moreover, the dangling bond can be terminated by a hydrogen atom, and hence there would be one monolayer with hydrogen passivation in surface.

For the $\operatorname{Si}(001)(2 \times 1)$ reconstruction, the Tersoff potential has been used to approximate the Si-Si covalent bond interactions, which gives a Si-Si dimer bond length of $2.37 \AA$ [26]. Since the dimer bond length is known from the reference, the positions of the surface reconstruction atoms can be obtained, i.e., $0.735 \AA$, as shown in Fig. 2(a). The components of the distance along the $x$ and $y$ directions both are $\delta=0.5197 \AA$. Certainly, the dimer bond length increases with the distance between the positions of the surface reconstruction atoms, and the ideal position decreases [26]. For the atom bond chains, and there are $(2 \times 1)$ dimer bonds along different directions, therefore the top surface and the bottom surface of the nanoplate are nonequivalent, as shown in Fig. 2(b).

In this paper, the ideal $(2 \times 1)$ surface reconstruction is only considered while the absence of the defects is assumed. Therefore the effect of the defects on the elasticity of silicon nanoplate is neglected.

Due to $(2 \times 1)$ surface reconstruction, the positions of surface atoms are different from the bulk atoms and the dimer bonds exist on the surface along the in-plane diagonal, which are different from the ideal silicon crystal cell. Thus the strain energy of the upper part (or low part) of a top surface (or bottom surface) crystal cell must be expressed identically.

Because of the periodicity of the crystal lattice and $(2 \times 1)$ surface reconstruction in $x-y$ plane, the periodic calculation element is chosen to contain $2 N(=2 \times 1 \times N)$ crystal cell. Upon considering surface reconstruction, the total strain energy $U_{\text {tot }}$ of the nanoplate, should be the sum of all parts

$$
U_{\mathrm{tot}}=\sum_{i} \sum_{j} \sum_{l}^{N-2} U_{\mathrm{cell}}+\sum_{i / 2} \sum_{j} \sum_{l}^{1} U^{T}+\sum_{i / 2} \sum_{j} \sum_{l}^{1} U^{B},
$$

(13)

where $U_{\text {cell }}$ is still the strain energy for a silicon crystal cell from the origin atom $(i, j, l)$, superscript $T$ denote the top surface crystal

![](./images/811910020647092224_2.jpg)

Fig. 2. (a) Atomic configurations of surface unreconstruction (UR) and $(2 \times 1)$ surface reconstruction. (b) Top surface cell and bottom surface cell after reconstruction. Darker spheres represent atoms closer to the top or the bottom.

cell which contains the low part of two crystal cells and the $(2 \times 1)$ reconstructed top surface cell, superscript $B$ denotes the bottom surface crystal cell which contains the upper part of two crystal cells and the $(2 \times 1)$ reconstructed bottom surface cell, respectively.

In the same way of ideal crystal cell, we can write the strain energy of the $(2 \times 1)$ reconstructed top surface cell (shown in Fig. 2(b)) as

$$
\begin{aligned}
U & =2 k_{b}\left\{(2 a-2 \delta)^{4}\left(\varepsilon_{x}+\varepsilon_{y}+\gamma_{x y}\right)^{2}\right. \\
& +\left[(a+\delta)^{2} \varepsilon_{x}+(\delta-a)^{2} \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(\delta^{2}-a^{2}\right) \gamma_{x y}-a(a+\delta) \gamma_{x z}+a(a-\delta) \gamma_{y z}+(a+\delta) u^{\prime \prime}+(\delta-a) v^{\prime \prime}-a w^{\prime \prime}\right]^{2} \\
& +\left[(\delta-a)^{2} \varepsilon_{x}+(a+\delta)^{2} \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(\delta^{2}-a^{2}\right) \gamma_{x y}+a(a-\delta) \gamma_{x z}-a(a+\delta) \gamma_{y z}+(\delta-a) u^{\prime \prime}+(a+\delta) v^{\prime \prime}-a w^{\prime \prime}\right]^{2} \\
& +2 a^{2}\left[a \varepsilon_{x}+a \varepsilon_{y}+a \varepsilon_{z}+a \gamma_{x y}+a \gamma_{x z}+a \gamma_{y z}+u^{\prime \prime}+v^{\prime \prime}+w^{\prime \prime}\right]^{2}+2 a^{2}\left[a \varepsilon_{x}+a \varepsilon_{y}+a \varepsilon_{z}+a \gamma_{x y}-a \gamma_{x z}-a \gamma_{y z}-u^{\prime \prime}-v^{\prime \prime}+w^{\prime \prime}\right]^{2} \\
& +\left[(a-\delta)^{2} \varepsilon_{x}+(a+\delta)^{2} \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(\delta^{2}-a^{2}\right) \gamma_{x y}-a(a-\delta) \gamma_{x z}+a(a+\delta) \gamma_{y z}+(a-\delta) u^{\prime \prime}-(a+\delta) v^{\prime \prime}-a w^{\prime \prime}\right]^{2} \\
& +\left[(a+\delta)^{2} \varepsilon_{x}+(a-\delta)^{2} \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(\delta^{2}-a^{2}\right) \gamma_{x y}+a(a+\delta) \gamma_{x z}-a(a+\delta) \gamma_{y z}-(a+\delta) u^{\prime \prime}+(a-\delta) v^{\prime \prime}-a w^{\prime \prime}\right]^{2} \\
& +\frac{1}{2} k_{\theta}\left\{8 a^{2}\left(a \varepsilon_{x}+a \varepsilon_{y}-a \varepsilon_{z}+a \gamma_{x y}-w^{\prime \prime}\right)^{2}\right. \\
& +\left[2 a(a+\delta) \varepsilon_{x}+2 a(\delta-a) \varepsilon_{y}-2 a^{2} \varepsilon_{z}+2 a \delta \gamma_{x y}+a \delta \gamma_{x z}+a(\delta-2 a) \gamma_{y z}+(2 a+\delta) u^{\prime \prime}+\delta v^{\prime \prime}\right]^{2} \\
& +\left[2 a(\delta-a) \varepsilon_{x}+2 a(a+\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}+2 a \delta \gamma_{x y}+a(\delta-2 a) \gamma_{x z}+a \delta \gamma_{y z}+\delta u^{\prime \prime}+(2 a+\delta) v^{\prime \prime}\right]^{2} \\
& +\left[-2 a(a+\delta) \varepsilon_{x}+2 a(a-\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}-2 a \delta \gamma_{x y}+a(2 a+\delta) \gamma_{x z}+a \delta \gamma_{y z}+\delta u^{\prime \prime}+(\delta-2 a) v^{\prime \prime}\right]^{2} \\
& +\left[2 a(a-\delta) \varepsilon_{x}-2 a(a+\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}-2 a \delta \gamma_{x y}+a \delta \gamma_{x z}+a(2 a+\delta) \gamma_{y z}+(\delta-2 a) u^{\prime \prime}+\delta v^{\prime \prime}\right]^{2} \\
& +4\left[\left(\delta^{2}-a^{2}\right) \varepsilon_{x}+\left(\delta^{2}-a^{2}\right) \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(a^{2}+\delta^{2}\right) \gamma_{x y}-a \delta \gamma_{x z}-a \delta \gamma_{y z}+\delta u^{\prime \prime}+\delta v^{\prime \prime}-a v^{\prime \prime}\right]^{2} \\
& +\left[2 a(a-\delta) \varepsilon_{x}-2 a(a+\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}+2 a \delta \gamma_{x y}-a \delta \gamma_{x z}-a(2 a+\delta) \gamma_{y z}+(2 a-\delta) u^{\prime \prime}-\delta v^{\prime \prime}\right]^{2} \\
& +\left[-2 a(a+\delta) \varepsilon_{x}+2 a(a-\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}-2 a \delta \gamma_{x y}-a(2 a+\delta) \gamma_{x z}-a \delta \gamma_{y z}-\delta u^{\prime \prime}+(2 a-\delta) v^{\prime \prime}\right]^{2} \\
& +\left[2 a(\delta-a) \varepsilon_{x}+2 a(a+\delta) \varepsilon_{y}-2 a^{2} \varepsilon_{z}+2 a \delta \gamma_{x y}+a(2 a-\delta) \gamma_{x z}-a \delta \gamma_{y z}-\delta u^{\prime \prime}-(2 a+\delta) v^{\prime \prime}\right]^{2} \\
& +\left[2 a(a+\delta) \varepsilon_{x}+2 a(\delta-a) \varepsilon_{y}-2 a^{2} \varepsilon_{z}+2 a \delta \gamma_{x y}-a \delta \gamma_{x z}+a(2 a-\delta) \gamma_{y z}-(2 a+\delta) u^{\prime \prime}-\delta v^{\prime \prime}\right]^{2} \\
& \left.+4\left[\left(\delta^{2}-a^{2}\right) \varepsilon_{x}+\left(\delta^{2}-a^{2}\right) \varepsilon_{y}+a^{2} \varepsilon_{z}+\left(a^{2}+\delta^{2}\right) \gamma_{x y}+a \delta \gamma_{x z}+a \delta \gamma_{y z}-\delta u^{\prime \prime}-\delta v^{\prime \prime}-a w^{\prime \prime}\right]^{2}\right\}.
\end{aligned}
\tag{14}
$$

As the structure of the top surface cell has changed after reconstruction, the components of the internal strain $u^{\prime \prime}, v^{\prime \prime}$ and $w^{\prime \prime}$ are different from those of the body and can be obtained in the same way,

$$
\begin{aligned}
& u^{\prime \prime}=\frac{a^{3} \delta^{2}\left[2 k_{b}\left(k_{\theta}+2 k_{b}\right)-k_{\theta}^{2}\right] \gamma_{z x}+\left[a^{5}\left(k_{\theta}+2 k_{b}\right)\left(k_{\theta}-2 k_{b}\right)-a^{3} \delta^{2} k_{\theta}^{2}\right] \gamma_{y z}}{a^{2}\left[\left(a^{2}+\delta^{2}\right)\left(k_{\theta}+2 k_{b}\right)+\delta^{2} k_{\theta}\right]\left(k_{\theta}+2 k_{b}\right)}, \\
& v^{\prime \prime}=\frac{a^{3} \delta^{2}\left[2 k_{b}\left(k_{\theta}+2 k_{b}\right)-k_{\theta}^{2}\right] \gamma_{y z}-\left[a^{5}\left(k_{\theta}+2 k_{b}\right)\left(k_{\theta}-2 k_{b}\right)-a^{3} \delta^{2} k_{\theta}^{2}\right] \gamma_{z x}}{a^{2}\left[\left(a^{2}+\delta^{2}\right)\left(k_{\theta}+2 k_{b}\right)+\delta^{2} k_{\theta}\right]\left(k_{\theta}+2 k_{b}\right)}, \\
& w^{\prime \prime}=\frac{\delta^{2}}{2 a}\left(\varepsilon_{x}+\varepsilon_{y}\right)+\left[\frac{\delta^{2}}{2 a}+\frac{a\left(k_{\theta}-2 k_{b}\right)}{2\left(k_{\theta}+2 k_{b}\right)} \gamma_{x y}\right].
\end{aligned}
\tag{15}
$$

There are some differences between the top surface cell and the bottom surface cell after reconstruction (shown in Fig. 2(b)). The strain energy and the internal strain expressions of the bottom surface cell can be obtained in the same way. The calculation element volume is $v=8 a \times 4 a \times h$, where $h$ is the thickness of the nanoplate, and, $h=(4 N+1) a$. The strain energy of the calculation element can be obtained from Eqs. (13) and (14). Young's modulus $E$ of the nanoplate along the $x$ direction with $(2 \times 1)$ surface reconstruction also can be obtained by

$$
\begin{aligned}
E= & \frac{1}{(4 N+1) a^{3}}\left\{4(N-1) a^{4}\left(k_{b}+\frac{3 k_{\theta}}{2}\right)+k_{b}\left\{8(a-\delta)^{4}\right.\right. \\
& \left.+\left[(a+\delta)^{2}-\frac{\delta^{2}}{2}\right]^{2}+\left[(a-\delta)^{2}-\frac{\delta^{2}}{2}\right]^{2}+2\left(a^{2}+\frac{\delta^{2}}{2}\right)^{2}\right\} \\
& \left.+\frac{k_{\theta}}{2}\left[\left(2 a^{2}-\delta^{2}\right)^{2}+4 a^{2}(a+\delta)^{2}+4 a^{2}(a-\delta)^{2}\right]\right\}.
\end{aligned}
\tag{16}
$$

Form the above expression, it shows that Young's modulus of the $\operatorname{Si}(001)$ surface reconstruction nanoplate is dependent on the reconstruction and also dependent on the number of atomic layers $N$. If the contributions of $(2 \times 1)$ surface reconstruction (the dimer bonds and the displacements of the reconstructed surface atoms from the ideal position) are omitted, Eq. (16) reduces Eq. (12).

## 3. Elasticity at finite temperature

### 3.1. Lattice parameters

It is well known that the mean interatomic distances increase with temperature, which is the intrinsic property for the thermal expansion of materials. However, the classical harmonic approximation predicts no thermal expansion. Thermal expansion is indeed due to the anharmonic characteristic of the interatomic potential, which should be taken for investigating the thermal properties. The zero pressure lattice parameter $a(T)$ has been computed at various temperatures (100-1500 K) by using quasiharmonic model [27] or MD simulation [10]. The lattice parameter values from Ref. [27] are used in this work, which accounts for the dependence of the phonon frequencies on the

![](./images/811910020647092224_3.jpg)

Fig. 3. Lattice parameter at different temperatures [27].

temperature and is a simple extension of the classical harmonic approximation by making the force constant change with the volume of the crystal.

Fig. 3 shows the variation of the lattice parameter at various temperatures, obtained from quasiharmonic model [27]. It is noted that the lattice parameter increases with temperature and their variation is almost linear from 500 K to 1500 K.

### 3.2. Anharmonic model

Recently, a quasiharmonic approximation with a phonon Green's function approach is developed to compute thermodynamic and mechanical properties of silicon nanostructures at finite temperature [21]. However, the phonon spectrums of atoms have to be known, and the calculation is more complex than the semi-continuum approach. Thus the semi-continuum approach is extended here to take temperature effect into account.

Since the lattice parameter is the function of temperature, the strain energy and the volume of the nanoplate vary with temperature. The total strain energy is different from before and varies with temperature, causing Young's modulus to vary with temperature. Therefore the variation of Young's modulus would be dependent on the temperature besides the nanoplate thickness.

In the Keating model as introduced in Eq. (3), the lowest-order contribution to the strain energy was described correctly through quadratic terms in the distortion of the equilibrium geometry. Since the bonding curve of a crystal deviates considerably from the quadratic form for distortions of the crystal volume, it is obvious that the strain energy must be extended to include higher-order anharmonic terms for a reasonable description of deformations of the atomic structure. One way to include higher-order terms is to use force constants which depend explicitly on the local geometry. Within the local picture of a valence-force model, for homogeneous distortions, the force constants can be assumed as [22]

$$
k_{b}=k_{b}^{0}\left(\frac{r_{i j}^{0}}{r_{i j}}\right)^{4}, \quad k_{\theta}=k_{\theta}^{0}\left(\frac{r_{i j}^{0}}{r_{i j}}\right)^{7}. \tag{17}
$$

where $r_{i j}$ and $r_{i j}^{0}$ are the deformation and equilibrium bond lengths and can be obtained from the corresponding lattice parameters, $k_{b}^{0}$ and $k_{\theta}^{0}$ are the equilibrium force constants, respectively. Once the lattice parameter at the given temperature is known, the force constants can be obtained from above equations, as shown in Fig. 4. It is obvious that the force constants both decrease as the temperature increases. $k_{b}$ varies faster than $k_{\theta}$, even it is the function of the lower power of the bond length.

![](./images/811910020647092224_4.jpg)

Fig. 4. Force constants at different temperature.

### 3.3. Results and discussions

Based on the above expressions, Fig. 5 shows Young's moduli of the Si (0 0 1) nanoplate with and without $(2 \times 1)$ surface reconstruction as a function of the thickness, along the high-symmetry [1 0 0] direction. As the nanoplate thickness is above 100 nm, Young's moduli tend to become a constant value, which approaches the bulk value of 130 GPa [28]. As the thickness decreases, Young's moduli begin to deviate from that of the bulk silicon. This is due to the fact that the surface-to-volume ratio increases as the structures are miniaturized, and the surface effects become more important. It is interesting to note that Young's moduli exhibit opposite behavior with and without surface reconstruction as the thickness scaling down. Without surface reconstruction, surface atoms have two dangling bonds out of the $x$-$y$ plane and Young's modulus of the nanoplate decreases dramatically as the nanoplate is scaled down to several tens of nanometers, which means that the nanoplate is elastically softer than bulk. The difference of Young's moduli of nanoplates with and without surface reconstruction gradually increases as the plate thickness decreases from about 100 nm. On the $(2 \times 1)$ reconstruction surfaces, surface atoms miss bonds and their positions are different from ideal positions, and dimer bonds exist. The surface reconstruction leads to stronger bonds and hence an increase in Young's modulus of the material as it is scaled down, which makes the nanoplate stiffer along the [1 0 0] direction. It is

![](./images/811910020647092224_5.jpg)

Fig. 5. Young's modulus of the silicon nanoplate as a function of thickness.

![](./images/811910020647092224_6.jpg)

Fig. 6. Variation of Young's modulus with temperature at different thickness.

evident that the $(2 \times 1)$ surface reconstruction has a significant effect on the elasticity of the nanoplate, especially at several nanometers.

It is crucial to investigate various stiffening and softening mechanisms. The softening effects are principally attributed to bond loss [29], and the stiffening effect is primarily from electron density distribution [27] and bond contraction or volume contraction [30,31]. There is no doubt that electrons on the surface are distributed after surface reconstruction, and the electron density around the dimer atoms is higher, which gives rise to stronger bonding on the surface. In our model, the dimer bonds are along the in-plane diagonal and not along the $x$ and $y$ directions. The length of the dimer bond is shorter than that of the body and the interaction is strengthened after reconstruction. Therefore, the bond energy is higher after reconstruction.

The dimer bonds also exist in bulk of solids. Surface reconstruction is insignificant for solids of macroscopic dimen- sions. However, for nanostructures it is pivotally important since surface-to-volume ratio is large.

Fig. 5 also shows Young's modulus of a silicon nanoplate with and without surface reconstruction at 100 K. Young's modulus of the nanoplate with surface reconstruction decreases as tempera- ture varying from 0 K to 100 K, and Young's modulus of the nanoplate without surface reconstruction exhibits the same behavior. It is interesting to note that Young's moduli tend to become a constant value with and without surface reconstruction at 100 K, which is similar to the behavior at 0 K.

Once the lattice parameter at the given temperature is known, Young's modulus of the $Si(001)$ nanoplate with surface recon struction can be obtained. Fig. 6 shows the variation of Young's moduli of the silicon nanoplate at various temperatures. At the given thickness, Young's modulus decreases as temperature increases and the variation of Young's modulus is obvious from 100 K to 1500 K. It is evident that the impacts of temperature on Young's moduli are the same at various thicknesses. The conclusion can be drawn that Young's modulus of the nanoplate has a negative temperature coefficient, which agrees with the results by using quasiharmonic model [32].

### 4. Conclusion

A semi-continuum approach has been developed for a multiscale analysis of a silicon plate, which captures the atomistic physics and retains the efficiency of continuum models. The Keating model is used to describe the strain energy of the system. The result indicates that the elastic modulus of the nanoplate is size dependent. Young's moduli of the silicon nanoplate deviate from that of the bulk silicon and exhibit opposite behavior with and without surface reconstruction as the thickness is scaling down. It is concluded that the nanoplate may be softer or stiffer than the corresponding bulk. The softening or stiffening depends on the bond status (bond loss, bond saturation, or alignment of bond). The nanoplate elasticity is sensitive to surface reconstruction, which may impact the application of the nanoplate as sensors. The semi-continuum approach is an efficient way to determine the mechanical properties of the nanoplate.

The semi-continuum approach is extended to perform a mechanical analysis of the silicon nanoplate at finite temperature. Taking into account the variations of the lattice parameter with the temperature, the Keating anharmonic model is used to compute the strain energy of the system. At finite temperature, Young's modulus of the silicon nanoplate with surface reconstruction is computed. The dependence of Young's modulus of the nanoplate on temperature is predicted, and it exhibits a negative temperature coefficient.

### Acknowledgements

The project is supported by the National Basic Research Program of China (grant no. 2006CB300404), and the National High-Tech Research and Development Program of China (grant no. 2007AA04Z301).

### References

[1] G. Eres, F.Y.C. Hui, T.G. Thundat, D.C. Joy, Microelectron. Eng. 41/42 (1998) 519.
[2] J. Fritz, M.K. Baller, H.P. Lang, H. Rothuizen, P. Vettiger, E. Meyer, H.J. Guntherodt, C. Gerber, J.K. Gimzewski, Science 288 (2000) 316.
[3] B. Ilic, D. Czaplewski, M. Zalalutdinov, H.G. Craighead, P. Neuzil, C. Campagnolo, C. Batt, J. Vac. Sci. Technol. B 19 (2001) 2825.
[4] A. Vidic, D. Then, Ch. Ziegler, Ultramicroscopy 97 (2003) 407.
[5] P.O. Renault, E.L. Bourhis, P. Villain, P. Goudeau, K.F. Badawi, D. Faurie, Appl. Phys. Lett. 83 (2003) 473.
[6] P. Villain, P. Goudeau, P.O. Renault, K.F. Badawi, Appl. Phys. Lett. 81 (2002) 4365.
[7] X. Li, T. Ono, Y. Wang, M. Esashi, Appl. Phys. Lett. 83 (2003) 3081.
[8] S. Sundararajan, B. Bhushan, Sens. Actuators A 101 (2002) 338.
[9] S. Wei, C. Li, M.Y. Chou, Phys. Rev. B 50 (1994) 14587.
[10] L.J. Porter, S. Yip, M. Yamaguchi, H. Kaburaki, M.-J. Tang, J. Appl. Phys. 81 (1997) 96.
[11] M. Karimi, H. Yates, J.R. Ray, T. Kaplan, M. Mostoller, Phys. Rev. B 58 (1998) 6019.
[12] L.G. Zhou, H.C. Huang, Appl. Phys. Lett. 84 (2004) 1940.
[13] H.W. Shim, L.G. Zhou, H.C. Huang, T.S. Cale, Appl. Phys. Lett. 86 (2005) 151912.
[14] F.H. Streitz, R.C. Cammarata, K. Sieradzki, Phys. Rev. B 49 (1994) 10699.
[15] J.Q. Broughton, C.A. Meli, P. Vashishta, K. Kalia, Phys. Rev. B 56 (1997) 611.
[16] R.E. Rudd, J.Q. Broughton, Phys. Rev. B 72 (2005) 144104.
[17] C.T. Sun, H. Zhang, J. Appl. Phys. 93 (2003) 1212.
[18] J.-G. Guo, Y.-P. Zhao, J. Appl. Phys. 98 (2005) 074306.
[19] J. Wang, Q.A. Huang, H. Yu, Chin. Phys. Lett. 25 (2008) 1403.
[20] J. Wang, Q.A. Huang, H. Yu, Solid State Commun. 145 (2008) 35.
[21] P.N. Keating, Phys. Rev. 145 (1966) 637.
[22] H. Rücker, M. Methfessel, Phys. Rev. B 52 (1995) 11059.
[23] A.M. Krivtsov, N.F. Morozov, Phys. Solid State 44 (2002) 2158.
[24] R.M. Tromp, R.J. Hamers, J.E. Demuth, Phys. Rev. Lett. 55 (1985) 1303.
[25] S. Ihara, S.L. Ho, T. Uda, M. Hirao, Phys. Rev. Lett. 65 (1990) 1909.
[26] I.P. Batra, Phys. Rev. B 41 (1990) 5048.
[27] Z. Tang, N.R. Aluru, Phys. Rev. B 99 (2006) 064314.
[28] J.J. Wortman, R.A. Evans, J. Appl. Phys. 36 (1965) 153.
[29] L.G. Zhou, H. Huang, Appl. Phys. Lett. 84 (2004) 1940.
[30] D. Wolf, Appl. Phys. Lett. 58 (1991) 2081.
[31] C.Q. Sun, B.K. Tay, X.T. Zeng, S. Li, T.P. Chen, J. Zhou, H.L. Bai, E.Y. Jiang, J. Phys.: Condens. Matter 14 (2002) 7781.
[32] Z. Tang, H. Zhao, G. Li, N.R. Aluru, Phys. Rev. B 74 (2006) 064110.