# Basic solution of a mode-I limited-permeable crack in functionally graded piezoelectric materials

Zhen-Gong Zhou · Jun-Feng Hui · Lin-Zhi Wu

Received: 5 February 2007 / Accepted: 24 September 2007 / Published online: 28 November 2007
© Springer Science+Business Media B.V. 2007

## Abstract
In this paper, the basic solution of a mode-I crack in functionally graded piezoelectric materials was investigated by using the generalized Almansi’s theorem. In the analysis, the electric permittivity of air inside the crack were considered. To make the analysis tractable, it was assumed that the shear modulus, piezoelectric constants and dielectric constants vary exponentially with coordinate parallel to the crack. The problem was formulated through Fourier transform into two pairs of dual integral equations, in which the unknown variables are jumps of displacements across the crack surfaces. To solve the dual integral equations, the jumps of displacements across the crack surfaces were directly expanded as a series of Jacobi polynomials. The solution of the present paper shows that the effects of the electric boundary conditions on the electric displacement fields near the crack tips can not be ignored. Simultaneously, the solution of the present paper will revert to a closed form one when the functionally graded parameter equals to zero.

**Keywords** Crack · Functionally graded piezoelectric materials · Mechanics of solids

---

Z.-G. Zhou (⊗) · J.-F. Hui · L.-Z. Wu
Center for Composite Materials and Structures, Harbin Institute of Technology, P.O. Box 3010, No.2 Yikuang Street, Harbin 150080, China
e-mail: zhouzhg@hit.edu.cn

---

## 1 Introduction

Piezoelectric ceramic materials have advantages of quick response, low power consumption, high linearity and a relatively large induced strain for an applied electric field. Thus, they had been used in the design of different smart structures, e.g. actuators, sensors, large-scale space structures, aircraft structures, satellites, and so forth. The demand for piezoelectric materials with high strength, high toughness, low thermal expansion coefficient and low dielectric constant encourages the study of functionally graded piezoelectric materials [1, 2]. Therefore, it is important to study the fracture behavior of functionally graded piezoelectric materials.

Recently, the fracture problems of functionally graded piezoelectric materials have been considered in the literature [3–7]. Li and Weng [7] first considered the static anti-plane problem of a finite crack in a functionally graded piezoelectric material strip. Their results showed that the singular stress and the singular electric displacements in functionally graded piezoelectric materials carry the same forms as those in homogeneous piezoelectric materials but the magnitudes of the intensity factors depend significantly upon the gradient parameter of functionally graded piezoelectric material properties. More recently, Zhou and Wang [8, 9] first studied the static ant-plane problems of two parallel cracks and a crack in functionally graded piezoelectric/piezomagnetic materials by using

![](./images/811957058671738881_1.jpg)

Schmidt method [10], but they just concentrated on the anti-plane shear fracture problems in functionally graded piezoelectric/piezomagnetic materials.

For the fracture problem of homogeneous piezoelectric materials, although many experts such as Gao et al. [11]; Zhang and Tong [12]; Zhong and Meguid [13] have studied the fracture problem of piezoelectric materials, there are still arguments about the electric boundary conditions along the crack surfaces. Some authors such as Parton [14], Mikhailov and Parton [15] considered that the thickness of the crack is very small. So the electric potential and the electric displacement should be continuous across the crack surfaces. This is the so-called permeable crack model. This has been argued by Pak [16]. Others [16, 17] assumed that since air occupies the crack gap and the permittivity of air inside the crack is far less than those of piezoelectric materials, the electric potential and the electric displacement are not continuous across crack surface. This is the so-called impermeable crack model. According to this crack mode, the interaction of multiple parallel impermeable cracks in piezoelectric materials was studied by the ‘pseudo-traction-electric displacement’ method in reference [17]. It was worth noting that different electric boundary conditions on the crack surfaces led to very different results [18]. Strictly speaking, even if the permittivity of air inside the crack is quite small, the flux of an electric field through the crack gap should not be zero, so it is more reasonable to assume the electric boundary condition on crack surfaces take the following form [19, 20] (it is supposes that crack is located on the $x$-axis):

$$
D_{y}^{+}=D_{y}^{-}, \quad D_{y}^{+}\left(v^{+}-v^{-}\right)=\varepsilon_{0}\left(\phi^{+}-\phi^{-}\right) \quad (1)
$$

in which $D_{y}$, $\phi$, $\varepsilon_{0}$ and $(v^{+}-v^{-})$ are electric displacement component along the $y$-axis, electric potential, permittivity of air inside the crack and the opening displacement component of the crack surfaces, respectively. This kind of the electric boundary condition was firstly proposed in Hao’s paper [19] as the limited-permeable crack model, which will be reduced to permeable boundary condition when $v^{+}-v^{-}=0$ and to impermeable one when $\varepsilon_{0}=0$. The permittivity of air inside the crack was considered in this crack mode. Although many results have been obtained for fracture problems of piezoelectric materials [12–18] and even the electric permittivity of air inside the crack in piezoelectric materials also has been considered [19, 20]; however, to our knowledge, understanding of the fracture behaviors of functionally graded piezoelectric materials are very insufficient compared with homogeneous piezoelectric materials. Meanwhile, the electric permittivity of air inside the crack in functionally graded piezoelectric materials has not been considered in the literature. The electro-elastic behavior of a limited-permeable mode-I crack in functionally graded piezoelectric materials has not been studied by the Schmidt method [10] before. This paper aims at giving a theoretical solution to this problem.

In this paper, the basic solution of a Mode-I limited-permeable crack [19, 20] in functionally graded piezoelectric material was investigated by the Schmidt method [10]. The Mode-I limited-permeable crack mode [19, 20] in piezoelectric materials as shown in (1) was firstly extended to study the Mode-I crack fracture problem of functionally graded piezoelectric materials. The present problem is different from ones as shown in Refs. [3, 4] because the electric permittivity of air inside the crack was not considered in Refs. [3, 4]. To make the analysis tractable, we assume that the shear modulus, piezoelectric constants and dielectric constants vary exponentially with coordinate parallel to the crack. The Fourier transform was applied and a mixed boundary value problem was reduced to two pairs of dual integral equations, in which the unknown variables are the jumps of displacements across the crack surfaces, not the dislocation density functions. To solve the dual integral equations, the jumps of displacements across the crack surfaces were directly expanded as a series of Jacobi polynomials and the Schmidt method [10] was used for numerical calculations. The solution shows that the singular stresses and the singular electric displacements at the crack tips in functionally graded piezoelectric materials carry the same forms as those in homogeneous piezoelectric materials, except that the magnitudes of the intensity factors are dependent on the electric permittivity of air inside the crack and the gradient parameter of functionally graded piezoelectric materials properties. The solution of the present paper will revert to a closed form one when the functionally graded parameter equals to zero.

## 2 Formulation of the problem

It is assumed that there is a crack of length $2l$ in a functionally graded piezoelectric material plane as

![](./images/811957058671738881_2.jpg)

![](./images/811957058671738881_3.jpg)

Fig. 1 Geometry and coordinate system for a crack

shown in Fig. 1. A Cartesian coordinate system $(x, y)$ is positioned as shown in Fig. 1. As discussed in the literature [19, 20], the electric permittivity of air inside the crack will be considered in the present study. It is assumed that a distributed normal stress loading $\sigma_{y y}(x, 0)=-\tau_{0}(x)$ ($\tau_{0}(x)$ is the magnitude of the stress loading) is directly applied on the upper and lower crack surfaces, which is equivalent to investigating the perturbation fields for a remotely loaded cracked-body through the standard superposition technique in fracture mechanics. So the boundary conditions along the crack surfaces can be written as follows:

$$
\left\{
\begin{aligned}
& \sigma_{x y}^{(1)}\left(x, 0^{+}\right)=\sigma_{x y}^{(2)}\left(x, 0^{-}\right)=0, \\
& \sigma_{y y}^{(1)}\left(x, 0^{+}\right)=\sigma_{y y}^{(2)}\left(x, 0^{-}\right)=-\tau_{0}(x), \\
& D_{y}(x, 0)\left[v^{(1)}\left(x, 0^{+}\right)-v^{(2)}\left(x, 0^{-}\right)\right] \\
& \quad=\varepsilon_{0}\left[\phi^{(1)}\left(x, 0^{+}\right)-\phi^{(2)}\left(x, 0^{-}\right)\right], \\
& D_{y}^{(1)}\left(x, 0^{+}\right)=D_{y}^{(2)}\left(x, 0^{-}\right),
\end{aligned} \quad |x| \leq l,\right.
\tag{2}
$$

$$
\left\{
\begin{aligned}
& u^{(1)}\left(x, 0^{+}\right)=u^{(2)}\left(x, 0^{-}\right), \\
& v^{(1)}\left(x, 0^{+}\right)=v^{(2)}\left(x, 0^{-}\right), \\
& \sigma_{y y}^{(1)}\left(x, 0^{+}\right)=\sigma_{y y}^{(2)}\left(x, 0^{-}\right), \\
& \sigma_{x y}^{(1)}\left(x, 0^{+}\right)=\sigma_{x y}^{(2)}\left(x, 0^{-}\right), \\
& \phi^{(1)}\left(x, 0^{+}\right)=\phi^{(2)}\left(x, 0^{-}\right), \\
& D_{y}^{(1)}\left(x, 0^{+}\right)=D_{y}^{(2)}\left(x, 0^{-}\right)
\end{aligned} \quad |x|>l,\right.
\tag{3}
$$

where $\sigma_{i k}^{(j)}(x, y)$ and $D_{k}^{(j)}(x, y)$ ($i=x, y, k=x, y$, $j=1,2$) are the plane stresses and in-plane electric displacements, respectively. $u^{(j)}(x, y)$ and $v^{(j)}(x, y)$ represent the displacement components in the $x$- and $y$-directions, respectively. $\phi^{(j)}(x, y)$ is electric potential. It should be noted that all the quantities with superscript $j$ ($j=1,2$) correspond to the upper half plane 1 and the lower half plane 2 as shown in Fig. 1, respectively. $D_{y}(x, 0)$ is electric displacements inside the crack. $\varepsilon_{0}$ is electric permittivity of air inside the crack.

## 3 Basic equations of functionally graded piezoelectric materials

For the plane problem of linear elastic, transversely isotropic, functionally graded piezoelectric materials, with vanishing body force and free charges, the basic equations are as follows [3, 4]

$$
\begin{aligned}
& \frac{\partial \sigma_{x x}^{(j)}}{\partial x}+\frac{\partial \sigma_{x y}^{(j)}}{\partial y}=0, \quad \frac{\partial \sigma_{x y}^{(j)}}{\partial x}+\frac{\partial \sigma_{y y}^{(j)}}{\partial y}=0, \\
& \frac{\partial D_{x}^{(j)}}{\partial x}+\frac{\partial D_{y}^{(j)}}{\partial y}=0,
\end{aligned}
\tag{4}
$$

$$
\sigma_{x x}^{(j)}(x, y)=c_{11}^{*} \frac{\partial u^{(j)}}{\partial x}+c_{13}^{*} \frac{\partial v^{(j)}}{\partial y}+e_{31}^{*} \frac{\partial \phi^{(j)}}{\partial y},
\tag{5}
$$

$$
\sigma_{y y}^{(j)}(x, y)=c_{13}^{*} \frac{\partial u^{(j)}}{\partial x}+c_{33}^{*} \frac{\partial v^{(j)}}{\partial y}+e_{33}^{*} \frac{\partial \phi^{(j)}}{\partial y},
\tag{6}
$$

$$
\sigma_{x y}^{(j)}(x, y)=c_{44}^{*}\left(\frac{\partial u^{(j)}}{\partial y}+\frac{\partial v^{(j)}}{\partial x}\right)+e_{15}^{*} \frac{\partial \phi^{(j)}}{\partial x},
\tag{7}
$$

$$
D_{x}^{(j)}(x, y)=e_{15}^{*}\left(\frac{\partial u^{(j)}}{\partial y}+\frac{\partial v^{(j)}}{\partial x}\right)-\varepsilon_{11}^{*} \frac{\partial \phi^{(j)}}{\partial x},
\tag{8}
$$

$$
D_{y}^{(j)}(x, y)=e_{31}^{*} \frac{\partial u^{(j)}}{\partial x}+e_{33}^{*} \frac{\partial v^{(j)}}{\partial y}-\varepsilon_{33}^{*} \frac{\partial \phi^{(j)}}{\partial y},
\tag{9}
$$

where $c_{11}^{*}, c_{13}^{*}, c_{33}^{*}, c_{44}^{*}$ are the elastic stiffness constants, $\varepsilon_{11}^{*}, \varepsilon_{33}^{*}$ are the dielectric constants, $e_{15}^{*}, e_{31}^{*}$, $e_{33}^{*}$ are the piezoelectric constants.

Crack problems in functionally graded materials do not appear to be analytically tractable for arbitrary variations of material properties. Usually, one tries to generate the forms of functionally graded materials for which the problem becomes tractable. Similar to the treatment of the crack problem for the isotropic functionally graded materials in Refs. [3-7], we assume that the material properties are described by:

$$
\begin{aligned}
& \left(c_{11}^{*}, c_{13}^{*}, c_{33}^{*}, c_{44}^{*}, e_{15}^{*}, e_{31}^{*}, e_{33}^{*}, \varepsilon_{11}^{*}, \varepsilon_{33}^{*}\right) \\
& \quad=\left(c_{11}, c_{13}, c_{33}, c_{44}, e_{15}, e_{31}, e_{33}, \varepsilon_{11}, \varepsilon_{33}\right) e^{\gamma x} \quad(10)
\end{aligned}
$$

where $\gamma$ is a constant which describes the gradient of properties along $x$ directions for the functionally graded material. When $\gamma=0$, it will return to the homogeneous piezoelectric material case [19]. In this case, the closed form solution can be obtained [19].

![](./images/811957058671738881_4.jpg)

The expressions of (10) are assumed to make the problem tractable.

$$
\left\{
\begin{aligned}
& c_{11} \frac{\partial^{2} u^{(j)}}{\partial x^{2}}+c_{44} \frac{\partial^{2} u^{(j)}}{\partial y^{2}}+\left(c_{13}+c_{44}\right) \frac{\partial^{2} v^{(j)}}{\partial x \partial y}+\left(e_{31}+e_{15}\right) \frac{\partial^{2} \phi^{(j)}}{\partial x \partial y}+\gamma\left[c_{11} \frac{\partial u^{(j)}}{\partial x}+c_{13} \frac{\partial v^{(j)}}{\partial y}+e_{31} \frac{\partial \phi^{(j)}}{\partial y}\right]=0, \\
& c_{44} \frac{\partial^{2} v^{(j)}}{\partial x^{2}}+c_{33} \frac{\partial^{2} v^{(j)}}{\partial y^{2}}+\left(c_{13}+c_{44}\right) \frac{\partial^{2} u^{(j)}}{\partial x \partial y}+e_{15} \frac{\partial^{2} \phi^{(j)}}{\partial x^{2}}+e_{33} \frac{\partial^{2} \phi^{(j)}}{\partial y^{2}}+\gamma\left[c_{44}\left(\frac{\partial u^{(j)}}{\partial y}+\frac{\partial v^{(j)}}{\partial x}\right)+e_{15} \frac{\partial \phi^{(j)}}{\partial x}\right]=0, \\
& \left(e_{31}+e_{15}\right) \frac{\partial^{2} u^{(j)}}{\partial x \partial y}+e_{15} \frac{\partial^{2} v^{(j)}}{\partial x^{2}}+e_{33} \frac{\partial^{2} v^{(j)}}{\partial y^{2}}-\varepsilon_{11} \frac{\partial^{2} \phi^{(j)}}{\partial x^{2}}-\varepsilon_{33} \frac{\partial^{2} \phi^{(j)}}{\partial y^{2}}+\gamma\left[e_{15}\left(\frac{\partial u^{(j)}}{\partial y}+\frac{\partial v^{(j)}}{\partial x}\right)-\varepsilon_{11} \frac{\partial \phi^{(j)}}{\partial x}\right]=0.
\end{aligned}
\right. \quad (11)
$$

## 4 Solution procedures

Equation (11) can be solved by use of the method proposed in Yang's work [21]. As expression in Yang's work [21], (11) can be rewritten as follows:

Substitution of (5-9) into (4), the governing equations are obtained as follows:

$$
[M D]\left\{\begin{array}{l}
u^{(j)} \\
v^{(j)} \\
\phi^{(j)}
\end{array}\right\}=0 \tag{12}
$$

where the operator matrix $[M D]$ is

$$
[M D]=\left\{\begin{array}{lll}
c_{11} \frac{\partial^{2}}{\partial x^{2}}+c_{44} \frac{\partial^{2}}{\partial y^{2}}+\gamma c_{11} \frac{\partial}{\partial x} & \left(c_{13}+c_{44}\right) \frac{\partial^{2}}{\partial x \partial y}+\gamma c_{13} \frac{\partial}{\partial y} & \left(e_{31}+e_{15}\right) \frac{\partial^{2}}{\partial x \partial y}+\gamma e_{31} \frac{\partial}{\partial y} \\
\left(c_{13}+c_{44}\right) \frac{\partial^{2}}{\partial x \partial y}+\gamma c_{44} \frac{\partial}{\partial y} & c_{44} \frac{\partial^{2}}{\partial x^{2}}+c_{33} \frac{\partial^{2}}{\partial y^{2}}+\gamma c_{44} \frac{\partial}{\partial x} & e_{15} \frac{\partial^{2}}{\partial x^{2}}+e_{33} \frac{\partial^{2}}{\partial y^{2}}+\gamma e_{15} \frac{\partial}{\partial x} \\
\left(e_{31}+e_{15}\right) \frac{\partial^{2}}{\partial x \partial y}+\gamma e_{15} \frac{\partial}{\partial y} & e_{15} \frac{\partial^{2}}{\partial x^{2}}+e_{33} \frac{\partial^{2}}{\partial y^{2}}+\gamma e_{15} \frac{\partial}{\partial x} & -\left(\varepsilon_{11} \frac{\partial^{2}}{\partial x^{2}}+\varepsilon_{33} \frac{\partial^{2}}{\partial y^{2}}+\gamma \varepsilon_{11} \frac{\partial}{\partial x}\right)
\end{array}\right\}.
$$

The determinant of $[M D]$ is

$$
\begin{aligned}
\operatorname{det}[M D]= & a \frac{\partial^{6}}{\partial y^{6}}+b \frac{\partial^{6}}{\partial x^{2} \partial y^{4}}+c \frac{\partial^{5}}{\partial x \partial y^{4}}+d \frac{\partial^{4}}{\partial y^{4}} \\
& +e \frac{\partial^{6}}{\partial x^{4} \partial y^{2}}+f \frac{\partial^{5}}{\partial x^{3} \partial y^{2}}+g \frac{\partial^{4}}{\partial x^{2} \partial y^{2}} \\
& +h \frac{\partial^{3}}{\partial x \partial y^{2}}+w_{1} \frac{\partial^{6}}{\partial x^{6}}+w_{2} \frac{\partial^{5}}{\partial x^{5}} \\
& +w_{3} \frac{\partial^{4}}{\partial x^{4}}+w_{4} \frac{\partial^{3}}{\partial x^{3}}
\end{aligned} \tag{13}
$$

in which

$$
a=-c_{44}\left(e_{33}^{2}+c_{33} \varepsilon_{33}\right), \tag{14}
$$

$$
\begin{aligned}
b= & e_{33}\left(2 c_{44} e_{31}-c_{11} e_{33}\right)+c_{13}^{2} \varepsilon_{33} \\
& -c_{33}\left[\left(e_{15}+e_{31}\right)^{2}+c_{44} \varepsilon_{11}+c_{11} \varepsilon_{33}\right] \\
& +2 c_{13}\left(e_{15} e_{33}+e_{31} e_{33}+c_{44} \varepsilon_{33}\right), \tag{15}
\end{aligned}
$$

$$
\begin{aligned}
c= & -\gamma\left\{e_{33}\left(-2 c_{44} e_{31}+c_{11} e_{33}\right)-c_{13}^{2} \varepsilon_{33}\right. \\
& +c_{33}\left[\left(e_{15}+e_{31}\right)^{2}+c_{44} \varepsilon_{11}+c_{11} \varepsilon_{33}\right] \\
& \left.-2 c_{13}\left(e_{15} e_{33}+e_{31} e_{33}+c_{44} \varepsilon_{33}\right)\right\}, \tag{16}
\end{aligned}
$$

$$
\begin{aligned}
d= & \gamma^{2}\left(-c_{33} e_{15} e_{31}+c_{13} e_{15} e_{33}+c_{44} e_{31} e_{33}\right. \\
& \left.+c_{13} c_{44} \varepsilon_{33}\right), \tag{17}
\end{aligned}
$$

$$
\begin{aligned}
e= & -c_{44} e_{31}^{2}-2 c_{11} e_{15} e_{33}+c_{13}^{2} \varepsilon_{11}-c_{11} c_{33} \varepsilon_{11} \\
& +2 c_{13}\left[e_{15}\left(e_{15}+e_{31}\right)+c_{44} \varepsilon_{11}\right]-c_{11} c_{44} \varepsilon_{33}, \tag{18}
\end{aligned}
$$

$$
\begin{aligned}
f=2 \gamma\{ & -c_{44} e_{31}^{2}-2 c_{11} e_{15} e_{33}+c_{13}^{2} \varepsilon_{11}-c_{11} c_{33} \varepsilon_{11} \\
& \left.+2 c_{13}\left[e_{15}\left(e_{15}+e_{31}\right)+c_{44} \varepsilon_{11}\right]-c_{11} c_{44} \varepsilon_{33}\right\}, \tag{19}
\end{aligned}
$$

$$
\begin{aligned}
g=- & \gamma^{2}\left[c_{44} e_{31}^{2}+2 c_{11} e_{15} e_{33}-c_{13}^{2} \varepsilon_{11}+c_{11} c_{33} \varepsilon_{11}\right. \\
& \left.-c_{13}\left(3 e_{15}^{2}+2 e_{15} e_{31}+3 c_{44} \varepsilon_{11}\right)+c_{11} c_{44} \varepsilon_{33}\right], \tag{20}
\end{aligned}
$$

![](./images/811957058671738881_5.jpg)

$$h=\gamma^{3} c_{13}\left(e_{15}^{2}+c_{44} \varepsilon_{11}\right),$$

$$
\begin{aligned}
& w_{1}=-c_{11}\left(e_{15}^{2}+c_{44} \varepsilon_{11}\right), \\
& w_{2}=-3 \gamma c_{11}\left(e_{15}^{2}+c_{44} \varepsilon_{11}\right),
\end{aligned}\tag{21}
$$

$$
\begin{aligned}
& w_{3}=-3 \gamma^{2} c_{11}\left(e_{15}^{2}+c_{44} \varepsilon_{11}\right), \\
& w_{4}=-\gamma^{3} c_{11}\left(e_{15}^{2}+c_{44} \varepsilon_{11}\right).
\end{aligned}\tag{22}
$$

Based on the cofactors $\Delta_{i k}$ of $\operatorname{det}[M D](i, k=1,2,3)$, using the method developed in literature [21], the general solution of (12) is

$$
\left(u^{(j)}, v^{(j)}, \phi^{(j)}\right)^{T}=\left(\Delta_{i 1}, \Delta_{i 2}, \Delta_{i 3}\right)^{T} F \quad(i=1,2,3)
$$

with $F(x, y)$ satisfying the following equation

$$
\operatorname{det}[M D] F=0.\tag{24}
$$

In the following analysis, we use only $\left(\Delta_{21}, \Delta_{22}, \Delta_{23}\right)$ for the present problem, which can be expressed as follows:

$$
\begin{aligned}
\Delta_{21}= & \alpha_{1} \frac{\partial^{4}}{\partial x^{3} \partial y}+\alpha_{2} \frac{\partial^{3}}{\partial x^{2} \partial y}+\alpha_{3} \frac{\partial^{2}}{\partial x \partial y} \\
& +\alpha_{4} \frac{\partial^{4}}{\partial x \partial y^{3}}+\alpha_{5} \frac{\partial^{3}}{\partial y^{3}},
\end{aligned}\tag{25}
$$

$$
\begin{aligned}
\Delta_{22}= & \alpha_{6} \frac{\partial^{4}}{\partial x^{2} \partial y^{2}}+\alpha_{7} \frac{\partial^{3}}{\partial x \partial y^{2}}+\alpha_{8} \frac{\partial^{4}}{\partial y^{4}}+\alpha_{9} \frac{\partial^{2}}{\partial y^{2}} \\
& +\alpha_{10} \frac{\partial^{4}}{\partial x^{4}}+\alpha_{11} \frac{\partial^{3}}{\partial x^{3}}+\alpha_{12} \frac{\partial^{2}}{\partial x^{2}},
\end{aligned}\tag{26}
$$

$$
\begin{aligned}
\Delta_{23}= & \alpha_{13} \frac{\partial^{4}}{\partial x^{2} \partial y^{2}}+\alpha_{14} \frac{\partial^{3}}{\partial x \partial y^{2}}+\alpha_{15} \frac{\partial^{4}}{\partial y^{4}}+\alpha_{16} \frac{\partial^{2}}{\partial y^{2}} \\
& +\alpha_{17} \frac{\partial^{4}}{\partial x^{4}}+\alpha_{18} \frac{\partial^{3}}{\partial x^{3}}+\alpha_{19} \frac{\partial^{2}}{\partial x^{2}}
\end{aligned}\tag{27}
$$

where
$$
\begin{aligned}
& \alpha_{1}=\left(c_{13}+c_{44}\right) \varepsilon_{11}+\left(e_{15}+e_{31}\right) e_{15}, \\
& \alpha_{2}=\gamma\left[e_{15}^{2}+2 e_{15} e_{31}+\left(2 c_{13}+c_{44}\right) \varepsilon_{11}\right], \\
& \alpha_{3}=\gamma^{2}\left(e_{15} e_{31}+c_{13} \varepsilon_{11}\right), \\
& \alpha_{4}=e_{33}\left(e_{15}+e_{31}\right)+\varepsilon_{33}\left(c_{13}+c_{44}\right), \\
& \alpha_{5}=\gamma\left(e_{31} e_{33}+c_{13} \varepsilon_{33}\right), \\
& \alpha_{6}=-\left(e_{15}+e_{31}\right)^{2}-c_{44} \varepsilon_{11}-c_{11} \varepsilon_{33}, \\
& \alpha_{7}=-\gamma\left[\left(e_{15}+e_{31}\right)^{2}+c_{44} \varepsilon_{11}+c_{11} \varepsilon_{33}\right], \\
& \alpha_{8}=-c_{44} \varepsilon_{33}, \quad \alpha_{9}=-\gamma^{2} e_{15} e_{31}, \\
& \alpha_{10}=-c_{11} \varepsilon_{11}, \quad \alpha_{11}=-2 \gamma c_{11} \varepsilon_{11}, \\
& \alpha_{12}=-\gamma^{2} c_{11} \varepsilon_{11}, \\
& \alpha_{13}=c_{44} e_{31}+\left(e_{15}+e_{31}\right) c_{13}-c_{11} e_{33}, \\
& \alpha_{14}=-\gamma\left[-c_{13}\left(2 e_{15}+e_{31}\right)+c_{11} e_{33}\right], \\
& \alpha_{15}=-c_{44} e_{33}, \\
& \alpha_{16}=\gamma^{2} c_{13} e_{15}, \quad \alpha_{17}=-c_{11} e_{15}, \\
& \alpha_{18}=-2 \gamma c_{11} e_{15}, \quad \alpha_{19}=-\gamma^{2} c_{11} e_{15}.
\end{aligned}
$$

Performing Fourier transform with respect to $x$, $F(x, y)$ can be expressed as follows:

$$
F(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} F^{*}(s, y) e^{i s x} d s.\tag{28}
$$

Substitution of (28) into (24) yields

$$
\begin{aligned}
& a \frac{\partial^{6} F^{*}}{\partial y^{6}}+\left(-b s^{2}+i c s+d\right) \frac{\partial^{4} F^{*}}{\partial y^{4}} \\
& \quad+\left(e s^{4}-i f s^{3}-g s^{2}+i s h\right) \frac{\partial^{2} F^{*}}{\partial y^{2}} \\
& \quad-\left(w_{1} s^{6}-i w_{2} s^{5}-w_{3} s^{4}+i w_{4} s^{3}\right) F^{*}=0
\end{aligned}\tag{29}
$$

which is a homogeneous equation, and the solution of $F^{*}(s, y)$ is a function of $\exp (\lambda y)$ in which $\lambda$ is the root of the following algebraic equation

$$
b_{0} \lambda^{6}-c_{0} \lambda^{4}+d_{0} \lambda^{2}-e_{0}=0\tag{30}
$$

where $b_{0}=a, c_{0}=-\left(-b s^{2}+i c s+d\right), d_{0}=e s^{4}-$ $i f s^{3}-g s^{2}+i s h, e_{0}=w_{1} s^{6}-i w_{2} s^{5}-w_{3} s^{4}+i w_{4} s^{3}$.

Let $\bar{\lambda}^{2}=\lambda^{2}-c_{0} / 3 b_{0}$. Then (30) becomes

$$
\bar{\lambda}^{6}+p \bar{\lambda}^{2}+q=0\tag{31}
$$

with

$$
p=-\frac{c_{0}^{2}}{3 b_{0}^{2}}+\frac{d_{0}}{b_{0}} \quad \text { and } \quad q=\frac{c_{0} d_{0}}{3 b_{0}^{2}}-\frac{e_{0}}{b_{0}}-\frac{2 c_{0}^{3}}{27 b_{0}^{3}}
$$

whose roots $\left(\bar{\lambda}^{2}\right)$ are

![](./images/811957058671738881_6.jpg)

$$
\left\{
\begin{aligned}
\bar{\lambda}_{1}^{2} &= \left\{ -\frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}} - \left\{ \frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}}, \\
\bar{\lambda}_{2}^{2} &= \omega \left\{ -\frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}} - \omega^{2} \left\{ \frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}}, \\
\bar{\lambda}_{3}^{2} &= \omega^{2} \left\{ -\frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}} - \omega \left\{ \frac{q}{2} + \sqrt{\left( \frac{q}{2} \right)^{2} + \left( \frac{p}{3} \right)^{3}} \right\}^{\frac{1}{3}}
\end{aligned}
\right. \tag{32}
$$

where $\omega = (-1 + i\sqrt{3})/2$. The properties of the roots $\bar{\lambda}^{2}$ depends on the sign of a parameter, $\Delta = q^{2}/4 + p^{3}/27$, as follows:

(1) $\Delta > 0$, one real root and a pair of conjugate complex roots.
(2) $\Delta = 0$, three real roots,
    (a) $p = q = 0$, $\bar{\lambda}_{1}^{2} = \bar{\lambda}_{2}^{2} = \bar{\lambda}_{3}^{2} = 0$,
    (b) $q^{2}/4 = -p^{3}/27 \neq 0$, $\bar{\lambda}_{1}^{2} \neq \bar{\lambda}_{2}^{2} = \bar{\lambda}_{3}^{2}$.
(3) $\Delta < 0$, three real roots, $\bar{\lambda}_{1}^{2} \neq \bar{\lambda}_{2}^{2} \neq \bar{\lambda}_{3}^{2}$.

Based on (30), we obtain

$$
\lambda_{1}^{2}\lambda_{2}^{2}\lambda_{3}^{2} = -q > 0, \tag{33}
$$

which indicates that at least one of the roots $\lambda_{i}^{2}$ ($i = 1, 2, 3$) is positive.

Depending on the properties of $\lambda^{2}$, function $F^{*}(s, y)$ has four different general solutions (for $y \geq 0$, $j = 1, 2$):

(a) If $\lambda_{1}^{2} \neq \lambda_{2}^{2} \neq \lambda_{3}^{2} > 0$, then

$$
\begin{aligned}
F^{*}(s, y) &= A_{1}(s)e^{-\lambda_{1}y} + A_{2}(s)e^{-\lambda_{2}y} \\
&\quad + A_{3}(s)e^{-\lambda_{3}y}
\end{aligned} \tag{34}
$$

(b) If $\lambda_{1}^{2} \neq \lambda_{2}^{2} = \lambda_{3}^{2} > 0$, then

$$
\begin{aligned}
F^{*}(s, y) &= A_{1}(s)e^{-\lambda_{1}y} + A_{2}(s)e^{-\lambda_{2}y} \\
&\quad + A_{3}(s)sye^{-\lambda_{2}y}
\end{aligned} \tag{35}
$$

(c) If $\lambda_{1}^{2} = \lambda_{2}^{2} = \lambda_{3}^{2} > 0$, then

$$
\begin{aligned}
F^{*}(s, y) &= A_{1}(s)e^{-\lambda_{1}y} + A_{2}(s)sye^{-\lambda_{2}y} \\
&\quad + A_{3}(s)s^{2}y^{2}e^{-\lambda_{2}y}
\end{aligned} \tag{36}
$$

(d) If $\lambda_{1}^{2} > 0$ and $\lambda_{2}^{2}$, $\lambda_{3}^{2} < 0$ or $\lambda_{2}^{2}$ and $\lambda_{3}^{2}$ being a pair of conjugate complex roots, then, in this case, and therefore $\lambda_{2}$ and $\lambda_{3}$ are a pair of conjugate complexes $-\delta \pm i\omega$, the solution of function $F^{*}(s, y)$ is

$$
\begin{aligned}
F^{*}(s, y) &= A_{1}(s)e^{-\lambda_{1}y} + A_{2}(s)e^{-\delta y}\cos(s\omega y) \\
&\quad + A_{3}(s)e^{-\delta y}\sin(s\omega y)
\end{aligned} \tag{37}
$$

where $\delta$ and $\omega > 0$ and $A_{i}(s)$ ($i = 1, 2, 3$) is a function of $s$ to be determined by the boundary conditions.

Substituting the solution of auxiliary function $F^{*}(s, y)$ into (5-9) and (23), displacements, stresses, electric displacements and electric potential fields are calculated using Mathematica. For $\lambda_{1}^{2} \neq \lambda_{2}^{2} \neq \lambda_{3}^{2} > 0$, the general expressions for displacements, stresses, electric displacements and electric potential fields are given as follows (other cases can be obtained using a similar method, but they were omitted in the present paper for brevity):

$$
\left\{
\begin{aligned}
u^{(1)}(x, y) &= \frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(1)}(s)A_{i}(s)e^{-\lambda_{i}y}e^{isx}ds, \\
v^{(1)}(x, y) &= \frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(2)}(s)A_{i}(s)e^{-\lambda_{i}y}e^{isx}ds, \\
\phi^{(1)}(x, y) &= \frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(3)}(s)A_{i}(s)e^{-\lambda_{i}y}e^{isx}ds,
\end{aligned}
\right. \tag{38}
$$

$$
\left\{
\begin{aligned}
u^{(2)}(x, y) &= -\frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(1)}(s)B_{i}(s)e^{\lambda_{i}y}e^{isx}ds, \\
v^{(2)}(x, y) &= \frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(2)}(s)B_{i}(s)e^{\lambda_{i}y}e^{isx}ds, \\
\phi^{(2)}(x, y) &= \frac{1}{2\pi} \sum_{i=1}^{3} \int_{-\infty}^{\infty} \chi_{i}^{(3)}(s)B_{i}(s)e^{\lambda_{i}y}e^{isx}ds,
\end{aligned}
\right. \tag{39}
$$

![](./images/811957058671738881_7.jpg)

$$
\left\{
\begin{aligned}
\sigma_{yy}^{(1)}(x, y) &= \frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(1)}(s) A_{i}(s) e^{-\lambda_{i} y} e^{i s x} d s, \\
\sigma_{xy}^{(1)}(x, y) &= \frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(2)}(s) A_{i}(s) e^{-\lambda_{i} y} e^{i s x} d s, \\
D_{y}^{(1)}(x, y) &= \frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(3)}(s) A_{i}(s) e^{-\lambda_{i} y} e^{i s x} d s,
\end{aligned}
\right.
\tag{40}
$$

$$
\left\{
\begin{aligned}
\sigma_{yy}^{(2)}(x, y) &= -\frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(1)}(s) B_{i}(s) e^{\lambda_{i} y} e^{i s x} d s, \\
\sigma_{xy}^{(2)}(x, y) &= \frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(2)}(s) B_{i}(s) e^{\lambda_{i} y} e^{i s x} d s, \\
D_{y}^{(2)}(x, y) &= -\frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{3} \beta_{i}^{(3)}(s) B_{i}(s) e^{\lambda_{i} y} e^{i s x} d s
\end{aligned}
\right.
\tag{41}
$$

where
$$
\begin{aligned}
\chi_{i}^{(1)}(s) &= -\lambda_{i}(-i \alpha_{1} s^{3} - \alpha_{2} s^{2} + i s \alpha_{3} \\
&\quad + i s \alpha_{4} \lambda_{i}^{2} + \alpha_{5} \lambda_{i}^{2}),
\end{aligned}
$$

$$
\begin{aligned}
\chi_{i}^{(2)}(s) &= -\alpha_{6} s^{2} \lambda_{i}^{2} + i \alpha_{7} s \lambda_{i}^{2} + \alpha_{8} \lambda_{i}^{4} + \alpha_{9} \lambda_{i}^{2} \\
&\quad + \alpha_{10} s^{4} - \alpha_{11} i s^{3} - \alpha_{12} s^{2},
\end{aligned}
$$

$$
\begin{aligned}
\chi_{i}^{(3)}(s) &= -\alpha_{13} s^{2} \lambda_{i}^{2} + i \alpha_{14} s \lambda_{i}^{2} + \alpha_{15} \lambda_{i}^{4} + \alpha_{16} \lambda_{i}^{2} \\
&\quad + \alpha_{17} s^{4} - \alpha_{18} i s^{3} - \alpha_{19} s^{2},
\end{aligned}
$$

$$
\beta_{i}^{(1)}(s) = i s c_{13} \chi_{i}^{(1)}(s) - c_{33} \lambda_{i} \chi_{i}^{(2)}(s) - e_{33} \lambda_{i} \chi_{i}^{(3)}(s),
$$

$$
\begin{aligned}
\beta_{i}^{(2)}(s) &= -\lambda_{i} c_{44} \chi_{i}^{(1)}(s) + i s c_{44} \chi_{i}^{(2)}(s) \\
&\quad + i s e_{15} \chi_{i}^{(3)}(s),
\end{aligned}
$$

$$
\beta_{i}^{(3)}(s) = i s e_{31} \chi_{i}^{(1)}(s) - e_{33} \lambda_{i} \chi_{i}^{(2)}(s) + \varepsilon_{33} \lambda_{i} \chi_{i}^{(3)}(s).
$$

Introduce the jumps of displacements and electric potential across the crack surfaces as follows:
$$
f_{1}(x) = u^{(1)}(x, 0^{+}) - u^{(2)}(x, 0^{-}), \tag{42}
$$

$$
f_{2}(x) = v^{(1)}(x, 0^{+}) - v^{(2)}(x, 0^{-}), \tag{43}
$$

$$
f_{3}(x) = \phi^{(1)}(x, 0^{+}) - \phi^{(2)}(x, 0^{-}). \tag{44}
$$

By substituting (38) and (39) into (42-44), and the resultant equations into (40) and (41), through Fourier transform and the boundary conditions (2) and (3), we have

$$
\begin{bmatrix}
\chi_{1}^{(1)}(s) & \chi_{2}^{(1)}(s) & \chi_{3}^{(1)}(s) \\
\beta_{1}^{(1)}(s) & \beta_{2}^{(1)}(s) & \beta_{3}^{(1)}(s) \\
\beta_{1}^{(3)}(s) & \beta_{2}^{(3)}(s) & \beta_{3}^{(3)}(s)
\end{bmatrix}
\begin{bmatrix}
A_{1}(s) \\
A_{2}(s) \\
A_{3}(s)
\end{bmatrix}
-
\begin{bmatrix}
\chi_{1}^{(1)}(s) & \chi_{2}^{(1)}(s) & \chi_{3}^{(1)}(s) \\
\beta_{1}^{(1)}(s) & \beta_{2}^{(1)}(s) & \beta_{3}^{(1)}(s) \\
\beta_{1}^{(3)}(s) & \beta_{2}^{(3)}(s) & \beta_{3}^{(3)}(s)
\end{bmatrix}
\begin{bmatrix}
B_{1}(s) \\
B_{2}(s) \\
B_{3}(s)
\end{bmatrix}
=
\begin{bmatrix}
\bar{f}_{1}(s) \\
0 \\
0
\end{bmatrix},
\tag{45}
$$

$$
\begin{bmatrix}
\chi_{1}^{(2)}(s) & \chi_{2}^{(2)}(s) & \chi_{3}^{(2)}(s) \\
\chi_{1}^{(3)}(s) & \chi_{2}^{(3)}(s) & \chi_{3}^{(3)}(s) \\
\beta_{1}^{(2)}(s) & \beta_{2}^{(2)}(s) & \beta_{3}^{(2)}(s)
\end{bmatrix}
\begin{bmatrix}
A_{1}(s) \\
A_{2}(s) \\
A_{3}(s)
\end{bmatrix}
+
\begin{bmatrix}
\chi_{1}^{(2)}(s) & \chi_{2}^{(2)}(s) & \chi_{3}^{(2)}(s) \\
\chi_{1}^{(3)}(s) & \chi_{2}^{(3)}(s) & \chi_{3}^{(3)}(s) \\
\beta_{1}^{(2)}(s) & \beta_{2}^{(2)}(s) & \beta_{3}^{(2)}(s)
\end{bmatrix}
\begin{bmatrix}
B_{1}(s) \\
B_{2}(s) \\
B_{3}(s)
\end{bmatrix}
=
\begin{bmatrix}
\bar{f}_{2}(s) \\
\frac{D_{0} \bar{f}_{2}(s)}{\varepsilon_{0}} \\
0
\end{bmatrix}
\tag{46}
$$

where $D_{0}=D_{y}(x, 0)(|x| \leq l)$. As discussed in the literature [19, 20], the thickness of the is very small. The change rate of $D_{y}(x, 0)$ along the thickness direction inside the crack is also very small. Therefore we assumed that $D_{0}=D_{y}(x, 0)(|x| \leq l)$ inside the crack can be used as a constant. Here an over bar indicates the Fourier transform.

By solving six equations of (45) and (46) with six unknown functions, substituting the solutions into (40) and applying the boundary conditions (2) and (3), we have

$$
\begin{aligned}
\sigma_{yy}^{(1)}(x, 0) &= \frac{e^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \left[ g_{1}(s) + \frac{D_{0}}{\varepsilon_{0}} g_{2}(s) \right] \\
&\quad \times \bar{f}_{2}(s) e^{i s x} d s = -\tau_{0}(x), \\
&|x| \leq l,
\end{aligned}
\tag{47}
$$

$$
\begin{aligned}
\sigma_{xy}^{(1)}(x, 0) &= \frac{e^{\gamma x}}{2\pi} \int_{0}^{\infty} g_{3}(s) \bar{f}_{1}(s) e^{i s x} d s = 0, \\
&|x| \leq l,
\end{aligned}
\tag{48}
$$

![](./images/811957058671738881_8.jpg)

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \bar{f}_{1}(s) e^{i s x} d s=0, \int_{-\infty}^{\infty} \bar{f}_{2}(s) e^{i s x} d s=0, \\
& \quad|x|>l
\end{aligned}
$$

where $g_{i}(s)(i=1,2,3)$ are known functions. Here they were omitted for brevity. Moreover,

$$
\operatorname{Lim}_{s \rightarrow+\infty} g_{1}(s) / s=-\operatorname{Lim}_{s \rightarrow-\infty} g_{1}(s) / s=\beta_{1},
$$

$$
\operatorname{Lim}_{s \rightarrow+\infty} g_{2}(s) / s=-\operatorname{Lim}_{s \rightarrow-\infty} g_{2}(s) / s=\beta_{2}
$$

and

$$
\operatorname{Lim}_{s \rightarrow+\infty} g_{3}(s) / s=-\operatorname{Lim}_{s \rightarrow-\infty} g_{3}(s) / s=\beta_{3}.
$$

$\beta_{j}(j=1,2,3)$ are non-zero constants which are dependent on the material properties. Here they were also omitted for brevity. These constants are the same as ones of the fracture problem in homogeneous piezoelectric materials as shown in Ref. [21]. When $\gamma=0, g_{j}(s) / s(j=1,2)$ will become two constants, i.e. it can be obtained $g_{j}(s) / s=\beta_{j}(s>0)$ and $g_{j}(s) / s=-\beta_{j}(s<0)(j=1,2)$ for $\gamma=0$ as shown in Ref. [21]. In this case, the closed form solution can be obtained as shown in Ref. [19]. For this case, it can be assumed that the loading $\tau_{0}(x)=\tau_{0}^{*}$ ( $\tau_{0}^{*}$ is a constant. In this case, the properties of materials are symmetric about $y$-axis for $\gamma=0.0$, so the stress loading on the crack surfaces should be also symmetric about $y$-axis for $\gamma=0.0$ ) because the present problem will become a symmetric one about $y$-axis. We can prove that $f_{1}(x)$ is an odd function and $f_{2}(x)$ is an even function for $\gamma=0$. The above two pairs of dual integral equations (47-49) must be solved to determine the unknown functions $\bar{f}_{1}(s)$ and $\bar{f}_{2}(s)$.

## 5 Solution of dual integral equations

The Schmidt method [10] is used to solve the dual integral equations (47-49). The jumps of displacement across the crack surfaces are directly expanded by the following series:

$$
\begin{aligned}
& f_{1}(x)=\sum_{n=0}^{\infty} a_{n} P_{n}^{\left(\frac{1}{2}, \frac{1}{2}\right)}\left(\frac{x}{l}\right)\left(1-\frac{x^{2}}{l^{2}}\right)^{\frac{1}{2}}, \\
& \quad \text { for }|x| \leq l,
\end{aligned}
$$

$$
f_{1}(x)=0, \quad \text { for }|x|>l,
$$

$$
\begin{aligned}
& f_{2}(x)=\sum_{n=0}^{\infty} b_{n} P_{n}^{\left(\frac{1}{2}, \frac{1}{2}\right)}\left(\frac{x}{l}\right)\left(1-\frac{x^{2}}{l^{2}}\right)^{\frac{1}{2}}, \\
& \quad \text { for }|x| \leq l,
\end{aligned}
$$

$$
f_{2}(x)=0, \quad \text { for }|x|>l,
$$

where $a_{n}$ and $b_{n}$ are unknown coefficients, $P_{n}^{(1 / 2,1 / 2)}(x)$ is a Jacobi polynomial [22]. The Fourier transforms of (50-53) are as follows [23]:

$$
\begin{aligned}
& \bar{f}_{1}(s)=\sum_{n=0}^{\infty} a_{n} G_{n} \frac{1}{s} J_{n+1}(s l), \\
& \bar{f}_{2}(s)=\sum_{n=0}^{\infty} b_{n} G_{n} \frac{1}{s} J_{n+1}(s l),
\end{aligned}
$$

$$
G_{n}=2 \sqrt{\pi}(-1)^{n} i^{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n !}
$$

where $\Gamma(x)$ and $J_{n}(x)$ are the Gamma and Bessel functions of order $n$, respectively.

Substituting (54) into (47-49), it can be shown that (49) is automatically satisfied. After integration with respect to $x$ in $[-l, x],(47)$ and (48) are reduced to the following forms:

$$
\begin{aligned}
& \frac{1}{2 \pi} \sum_{n=0}^{\infty} G_{n} b_{n} \int_{-\infty}^{\infty} \frac{1}{s(i s+\gamma)}\left[g_{1}(s)+\frac{D_{0}}{\varepsilon_{0}} g_{2}(s)\right] \\
& \quad \times J_{n+1}(s l)\left[e^{i s x+\gamma x}-e^{-i s l-\gamma l}\right] d s \\
& =-\int_{-l}^{x} \tau_{0}(t) d t, \quad|x| \leq l,
\end{aligned}
$$

$$
\begin{aligned}
& \sum_{n=0}^{\infty} G_{n} a_{n} \int_{-\infty}^{\infty} \frac{1}{s(i s+\gamma)} g_{3}(s) J_{n+1}(s l) \\
& \quad \times\left[e^{i s x+\gamma x}-e^{-i s l-\gamma l}\right] d s=0, \quad|x| \leq l .
\end{aligned}
$$

So it can be derived that $a_{n}=0(n=0,1,2,3, \ldots)$ from (56), i.e. $f_{1}(x)=0$.

The semi-infinite integral in (55) can be evaluated directly. Equation (55) can now be solved for coefficients $b_{n}$ by the Schmidt method [10]. For details, please see Ref. [24]. When $\gamma=0$, it can be assumed that the loading $\tau_{0}(x)=\tau_{0}^{*}$ ( $\tau_{0}^{*}$ is a constant) because the present problem will become a symmetric one. So it can be derived that $a_{n}=0(n=0,1,2,3, \ldots), b_{0}=-\tau_{0}^{*} l /\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right)$ and $b_{n}=0(n=1,2,3,4, \ldots)$ from (55) and (56).

![](./images/811957058671738881_9.jpg)

## 6 Intensity factors

Once we determine coefficients $a_n$ and $b_n$, we can obtain the whole stress field. However, from the viewpoint of fracture mechanics, it is important to determine the stresses $\sigma_{y}^{(1)}$, $\sigma_{x y}^{(1)}$ and the electric displacement $D_{y}^{(1)}$ in the vicinity of crack tips. In the present study, $\sigma_{y}^{(1)}$, $\sigma_{x y}^{(1)}$ and $D_{y}^{(1)}$ along the crack line can be expressed, respectively, as follows:

$$
\begin{aligned}
\sigma_{y y}^{(1)}(x, 0)= & \frac{e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} \\
& \times \int_{-\infty}^{\infty} \frac{1}{s}\left[g_{1}(s)+\frac{D_{0}}{\varepsilon_{0}} g_{2}(s)\right] \\
& \times J_{n+1}(s l) e^{i s x} d s,
\end{aligned}
$$

$$
\sigma_{x y}^{(1)}(x, 0)=0,
$$

$$
\begin{aligned}
D_{y}^{(1)}(x, 0)= & \frac{e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} \\
& \times \int_{-\infty}^{\infty} \frac{1}{s}\left[g_{4}(s)+\frac{D_{0}}{\varepsilon_{0}} g_{5}(s)\right] \\
& \times J_{n+1}(s l) e^{i s x} d s
\end{aligned}
$$

where $g_4(s)$ and $g_5(s)$ are two known functions. Here they were also omitted for brevity. Moreover,
$$
\lim _{s \rightarrow+\infty} g_{4}(s) / s=\beta_{4}=-\lim _{s \rightarrow-\infty} g_{4}(s) / s,
$$

$$
\lim _{s \rightarrow+\infty} g_{5}(s) / s=\beta_{5}=-\lim _{s \rightarrow-\infty} g_{5}(s) / s,
$$

$\beta_4$ and $\beta_5$ are two constants which depends on the properties of materials. They are the same as ones of the homogeneous piezoelectric material fracture problem [21]. When $\gamma=0, g_{4}(s) / s$ and $g_{5}(s) / s$ will become two constants, i.e. they can be obtained $g_{4}(s) / s=\beta_{4}, g_{5}(s) / s=\beta_{5} \quad(s>0), g_{4}(s) / s=-\beta_{4}$ and $g_{5}(s) / s=-\beta_{5} \quad(s<0)$ for $\gamma=0$ as shown in Ref. [21].

From (57) and (58), when $\gamma=0$, it can be obtained that $\sigma_{y}^{(1)}$, $\sigma_{x y}^{(1)}$ and $D_{y}^{(1)}$ along the crack line can be expressed as follows:

$$
\begin{aligned}
\sigma_{y y}^{(1)}(x, 0) & =\frac{\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}}{\pi} b_{0} G_{0} \int_{0}^{\infty} J_{1}(s l) \cos (s x) d s \\
& =-\tau_{0}^{*} l \int_{0}^{\infty} J_{1}(s l) \cos (s x) d s \\
& = \begin{cases}-\tau_{0}^{*}, & x<l, \\
\frac{\tau_{0}^{*} l^{2}}{\sqrt{x^{2}-l^{2}}\left[x+\sqrt{x^{2}-l^{2}}\right]}, & x>l,\end{cases}
\end{aligned}
$$

$$
\sigma_{x y}^{(1)}(x, 0)=0, \quad(60)
$$

$$
\begin{aligned}
D_{y}^{(1)}(x, 0) & =\frac{\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}}{\pi} b_{0} G_{0} \int_{0}^{\infty} J_{1}(s l) \cos (s x) d s \\
& = \begin{cases}-\frac{\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}}{\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}} \tau_{0}^{*}, & x<l, \\
\frac{\beta_{3}}{\beta_{1}} \frac{\tau_{0}^{*} l^{2}}{\sqrt{x^{2}-l^{2}}\left[x+\sqrt{x^{2}-l^{2}}\right]}, & x>l .\end{cases}
\end{aligned}
$$

For $x>l$, the singular parts of the stress and electric displacement fields near the right tip of the crack in (57) and (58) can be expressed, respectively, as follows:

$$
\begin{aligned}
\tau_{1 y y}= & \frac{\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{\gamma x}}{2 \pi} \\
& \times \sum_{n=0}^{\infty} b_{n} G_{n}\left[\int_{0}^{\infty} J_{n+1}(s l) e^{i s x} d s\right. \\
& \left.-\int_{-\infty}^{0} J_{n+1}(s l) e^{i s x} d s\right] \\
= & \frac{\left(\beta_{2}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} Q_{n}(x),
\end{aligned}
$$

$$
\tau_{1 x y}=0, \quad(63)
$$

$$
\begin{aligned}
D_{1 y}= & \frac{\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{\gamma x}}{2 \pi} \\
& \times \sum_{n=0}^{\infty} b_{n} G_{n}\left[\int_{0}^{\infty} J_{n+1}(s l) e^{i s x} d s\right. \\
& \left.-\int_{-\infty}^{0} J_{n+1}(s l) e^{i s x} d s\right] \\
= & \frac{\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} Q_{n}(x)
\end{aligned}
$$

where

$$
Q_{n}(x)=\left\{\begin{aligned}
\frac{-2(-1)^{\frac{n}{2}} l^{n+1}}{\sqrt{x^{2}-l^{2}}\left[x+\sqrt{x^{2}-l^{2}}\right]^{n+1}}, \\
n=0,2,4,6, \ldots, \\
\frac{2 i(-1)^{\frac{n+1}{2}} l^{n+1}}{\sqrt{x^{2}-l^{2}}\left[x+\sqrt{x^{2}-l^{2}}\right]^{n+1}}, \\
n=1,3,5,7, \ldots .
\end{aligned}\right.
$$

For $x<-l$, the singular parts of stress and electric displacement fields near the left tip of the crack in (57)

![](./images/811957058671738881_10.jpg)

and (58) can be expressed, respectively, as follows:

$$
\begin{aligned}
\tau_{2 y y}= & \frac{\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{\gamma x}}{2 \pi} \\
& \times \sum_{n=0}^{\infty} b_{n} G_{n}\left[\int_{0}^{\infty} J_{n+1}(s l) e^{i s x} d s\right. \\
& \left.-\int_{-\infty}^{0} J_{n+1}(s l) e^{i s x} d s\right] \\
= & \frac{\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} Q_{n}^{*}(x),
\end{aligned}
\tag{65}
$$

$$
\tau_{2 x y}=0, \tag{66}
$$

$$
\begin{aligned}
D_{2 y}= & \frac{\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{\gamma x}}{2 \pi} \\
& \times \sum_{n=0}^{\infty} b_{n} G_{n}\left[\int_{0}^{\infty} J_{n+1}(s l) e^{i s x} d s\right. \\
& \left.-\int_{-\infty}^{0} J_{n+1}(s l) e^{i s x} d s\right] \\
= & \frac{\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} b_{n} G_{n} Q_{n}^{*}(x)
\end{aligned}
\tag{67}
$$

where

$$
Q_{n}^{*}(x)=\left\{\begin{aligned}
& \frac{-2(-1)^{\frac{n}{2}} l^{n+1}}{\sqrt{x^{2}-l^{2}}\left[|x|+\sqrt{x^{2}-l^{2}}\right]^{n+1}}, \\
& \quad n=0,2,4,6, \ldots, \\
& \frac{-2 i(-1)^{\frac{n+1}{2}} l^{n+1}}{\sqrt{x^{2}-l^{2}}\left[|x|+\sqrt{x^{2}-l^{2}}\right]^{n+1}}, \\
& \quad n=1,3,5,7, \ldots.
\end{aligned}\right.
$$

The results of stress intensity factors $K_{\mathrm{I}}(l), K_{\mathrm{II}}(l)$ and electric displacement intensity factor $K^{D}(l)$ at the right tip of the crack can be given as follows:

$$
\begin{aligned}
K_{\mathrm{I}}(l)= & \lim _{x \rightarrow l^{+}} \sqrt{2(x-l)} \cdot \tau_{1 y y} \\
= & -\frac{2\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{\gamma l}}{\sqrt{\pi l}} \\
& \times \sum_{n=0}^{\infty} b_{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n!},
\end{aligned}
\tag{68}
$$

$$
K_{\mathrm{II}}(l)=0,
$$

$$
\begin{aligned}
& =-\frac{2\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{\gamma l}}{\sqrt{\pi l}} \sum_{n=0}^{\infty} b_{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n!} \\
& =\frac{\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}}{\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}} K_{\mathrm{I}}(l).
\end{aligned}
\tag{69}
$$

The results of stress intensity factors $K_{\mathrm{I}}(-l), K_{\mathrm{II}}(-l)$ and electric displacement intensity factor $K^{D}(-l)$ at the left tip of the crack can be given as follows:

$$
\begin{aligned}
K_{\mathrm{I}}(-l)= & \lim _{x \rightarrow-l^{-}} \sqrt{2(|x|-l)} \cdot \tau_{2 y y} \\
= & \frac{2\left(\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}\right) e^{-\gamma l}}{\sqrt{\pi l}} \\
& \times \sum_{n=0}^{\infty}(-1)^{n+1} b_{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n!},
\end{aligned}
\tag{70}
$$

$$
K_{\mathrm{II}}(-l)=0,
$$

$$
\begin{aligned}
K^{D}(-l)= & \lim _{x \rightarrow-l^{-}} \sqrt{2(|x|-l)} \cdot D_{2 y} \\
= & \frac{2\left(\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}\right) e^{-\gamma l}}{\sqrt{\pi l}} \\
& \times \sum_{n=0}^{\infty}(-1)^{n+1} b_{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n!} \\
= & \frac{\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}}{\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}} K_{\mathrm{I}}(-l).
\end{aligned}
\tag{71}
$$

For the case $\gamma=0$, the closed form solutions of stress intensity factors $K_{\mathrm{I}}(l), K_{\mathrm{II}}(l)$, and electric displacement intensity factor $K^{D}(l)$ can be written as follows (in this case, stress intensity factors $K_{\mathrm{I}}(l), K_{\mathrm{II}}(l)$ and electric displacement intensity factor $K^{D}(l)$ at the right tip of the crack will equal to the stress intensity factors $K_{\mathrm{I}}(-l), K_{\mathrm{II}}(-l)$ and electric displacement intensity factor $K^{D}(-l)$ at the left tip of the crack, respectively):

$$
\begin{aligned}
K_{\mathrm{I}}(l) & =K_{\mathrm{I}}(-l)=\lim _{x \rightarrow l^{+}} \sqrt{2(x-l)} \cdot \sigma_{y y}^{(1)}(x, 0) \\
& =\tau_{0}^{*} \sqrt{l},
\end{aligned}
\tag{72}
$$

$$
K_{\mathrm{II}}(l)=K_{\mathrm{II}}(-l)=0,
$$

![](./images/811957058671738881_11.jpg)

$$
\begin{aligned}
K_{\mathrm{I}}^{D}(l) & =K_{\mathrm{I}}^{D}(-l)=\lim _{x \rightarrow l^{+}} \sqrt{2(x-l)} \cdot D_{y}^{(1)}(x, 0) \\
& =\frac{\beta_{4}+\frac{D_{0}}{\varepsilon_{0}} \beta_{5}}{\beta_{1}+\frac{D_{0}}{\varepsilon_{0}} \beta_{2}} K_{\mathrm{I}}.
\end{aligned}\tag{73}
$$

## 7 Discussion and conclusions

It can be seen from previous works [24-27] that the Schmidt method possesses sufficient accuracy if the first ten terms of the infinite series in (55) are retained. Although the values of $D_{0}$ depend on the external loading, we assume that $D_{0}$ is a constant in the calculation, which allows us to focus on the effect of the electric permittivity $\varepsilon_{0}$ of air inside the crack on the stress and electric displacement fields near the crack tips. Since $\varepsilon_{0}$ is a variable, $D_{0} / \varepsilon_{0}$ can be used as a variable in the calculation. The crack surface loading $-\tau_{0}(x)$ will simply be assumed to be a polynomial of the following form (the properties of the materials are non-symmetric about $y$-axis for $\gamma \neq 0.0$, so the stress loading on the crack surfaces should be also non-symmetric about $y$-axis for $\gamma \neq 0.0)$:

$$
\begin{aligned}
-\tau_{0}(x)= & -p_{0}-p_{1}\left(\frac{x}{l}\right)-p_{2}\left(\frac{x}{l}\right)^{2} \\
& -p_{3}\left(\frac{x}{l}\right)^{3}.
\end{aligned}\tag{74}
$$

Since the problem is linear, the results can be obtained through superposition in any suitable manner. Here the results are obtained by taking only one of the four input parameters $p_{0}, p_{1}, p_{2}$ and $p_{3}$ as nonzero each time in the calculation. In all computations, material properties are given $c_{11}=12.6 \times 10^{10} \mathrm{~N} / \mathrm{m}^{2}, c_{33}=11.7 \times$ $10^{10} \mathrm{~N} / \mathrm{m}^{2}, c_{44}=3.53 \times 10^{10} \mathrm{~N} / \mathrm{m}^{2}, c_{13}=5.3 \times$ $10^{10} \mathrm{~N} / \mathrm{m}^{2}, e_{31}=-6.5 \mathrm{C} / \mathrm{m}^{2}, e_{33}=23.3 \mathrm{C} / \mathrm{m}^{2}$, $e_{15}=17.0 \mathrm{C} / \mathrm{m}^{2}, \varepsilon_{11}=151.0 \times 10^{-10} \mathrm{C} / \mathrm{Vm}$ and $\varepsilon_{33}=130 \times 10^{-10} \mathrm{C} / \mathrm{V} \mathrm{m}$. The calculated stress and electric displacement intensity factors at the crack tips are plotted in Figs. 2 to 14, respectively.

We discuss the results and draw our conclusions as follows:

(i) In the present paper, the generalized Almansi's theorem is applied and the basic solution is then obtained for stress and electric displacement intensity factors of a Mode-I limited-permeable crack in functionally graded piezoelectric materials. This method in the present paper is feasible for general cases, as discussed in (34-37), and thus the obtained solution is valid to general cases. However, the Eshelby-Stroh's method is valid only for the cases of non-degenerate materials. At the same time, the closed form solutions of the stress intensity factors $K_{\mathrm{I}}(l), K_{\mathrm{II}}(l)$, and the electric displacement intensity factor $K^{D}(l)$ can be obtained when $\gamma=0$.

![](./images/811957058671738881_12.jpg)

Fig. 2 Stress intensity factor versus $D_{0} / \varepsilon_{0}$ for $l=1.0$ and $\gamma l=0.4\left(\tau_{0}(x)=p_{0}\right)$

![](./images/811957058671738881_13.jpg)

Fig. 3 Electric displacement intensity factor versus $D_{0} / \varepsilon_{0}$ for $l=1.0$ and $\gamma l=0.4\left(\tau_{0}(x)=p_{0}\right)$

(ii) The limited-permeable crack mode [19, 20] in piezoelectric materials was firstly extended to study the fracture problem of functionally graded piezoelectric materials. The electric permittivity $\varepsilon_{0}$ of air inside the crack are considered in the present paper to mimic the real electric boundary conditions along the crack surfaces. The present problem is different from ones as shown in Refs. [3,4] because the electric permittivity of air inside the crack was not considered in

![](./images/811957058671738881_14.jpg)

![](./images/811957058671738881_15.jpg)

Fig. 4 Stress intensity factor versus $D_0/\varepsilon_0$ for $l=1.0$ and $\gamma l=0.4$ ($\tau_0(x)=p_1(x/l)$)

![](./images/811957058671738881_16.jpg)

Fig. 5 Electric displacement intensity factor versus $D_0/\varepsilon_0$ for $l=1.0$ and $\gamma l=0.4$ ($\tau_0(x)=p_1(x/l)$)

![](./images/811957058671738881_17.jpg)

Fig. 6 Stress intensity factor versus $D_0/\varepsilon_0$ for $l=1.0$ and $\gamma l=0.4$ ($\tau_0(x)=p_2(x/l)^2$)

![](./images/811957058671738881_18.jpg)

Fig. 7 Electric displacement intensity factor versus $D_0/\varepsilon_0$ for $l=1.0$ and $\gamma l=0.4$ ($\tau_0(x)=p_2(x/l)^2$)

Refs. [3, 4]. The current paper introduces the jumps of displacements across the crack surfaces as unknown variables in constructing the dual integral equations, which is quite different from the previous work [3-7] and [19, 20]. To solve the dual integral equations, the jumps of displacements across the crack surfaces were directly expanded as a series of Jacobi polynomials. This is the major difference between the current work and the available work in the literature.

(iii) The solution shows that the singular stress and the singular electric displacement at the crack tips in functionally graded piezoelectric materials carry the same forms as those in the homogeneous piezoelectric materials, except that the magnitudes of the stress and the electric displacement intensity factors depend significantly upon the gradient of the functionally graded piezoelectric materials as reported in Ref. [7]. The stress and electric displacement intensity factors depend on the crack length, the electric permittivity $\varepsilon_0$ of air inside the crack and the properties of the material for the Mode-I limited-permeable crack in functionally graded piezoelectric materials as shown in (55) and (68-73). The electro-elastic coupling effects can be also obtained as shown in (68-73). The results of electric displacement intensity factors can be directly obtained form results of stress intensity factors through (68-73). In addition, they are very small in magnitude as shown in Figs. 3, 5 and 7. This means that the applied mechanical load can cause the electric displacement singularities.

(iv) For the symmetric stress loading, the stress intensity factors at crack tips decrease with the increase of $D_0/\varepsilon_0$ as shown in Figs. 2 and 6, i.e. the stress intensity factors at the crack tips decrease with the decrease of the electric permittivity $\varepsilon_0$ of air inside the crack. So we have that the crack extending force can

![](./images/811957058671738881_19.jpg)

![](./images/811957058671738881_20.jpg)

Fig. 8 The stress intensity factor versus $D_0/\varepsilon_0$ for $l=1.0$ and $\gamma l=0.4$ ($\tau_0(x)=p_3(x/l)^3$)

![](./images/811957058671738881_21.jpg)

Fig. 9 Stress intensity factor versus $\gamma l$ for $l=1.0$ and $D_0/\varepsilon_0=4.0\times10^8$ ($\tau_0(x)=p_0$)

be resisted by reducing the electric permittivity $\varepsilon_0$ of air inside the crack in this case. However, the electric displacement intensity factors decrease until reaching a minimal peak value at $D_0/\varepsilon_0\approx1.6\times10^9$, and then they increase with the increase of $D_0/\varepsilon_0$ as shown in Figs. 3 and 7.

(v) For the anti-symmetric stress loading, the stress intensity factor at the right tip of crack decreases with the increase of $D_0/\varepsilon_0$ as shown in Figs. 4 and 8, i.e. the stress intensity factor at the right tip of crack decreases with the decrease of electric permittivity $\varepsilon_0$ of air inside the crack. However, the stress intensity factor at the left tip of crack increases with the increase of $D_0/\varepsilon_0$ as shown in Figs. 4 and 8. The stress intensity factors at the right and left tips of crack are almost symmetric about line $K=0$ as shown in Figs. 4 and 8. The stress intensity factor at the left tip of crack is negative because the stress loading is negative. However, electric displacement intensity factors at the right tip of crack decrease until reaching a minimal peak value at $D_0/\varepsilon_0\approx1.2\times10^9$, and then they increase with the increase of $D_0/\varepsilon_0$ as shown in Fig. 5. The electric displacement intensity factors at the right and left tips of crack are almost symmetric about line $K^D=0$ as shown in Fig. 5.

![](./images/811957058671738881_22.jpg)

Fig. 10 Electric displacement intensity factor versus $\gamma l$ for $l=1.0$ and $D_0/\varepsilon_0=4.0\times10^8$ ($\tau_0(x)=p_0$)

![](./images/811957058671738881_23.jpg)

Fig. 11 Stress intensity factor versus $\gamma l$ for $l=1.0$ and $D_0/\varepsilon_0=4.0\times10^8$ ($\tau_0(x)=p_1(x/l)$)

(vi) For the symmetric stress loading, stress intensity factors at crack tips are symmetric about the line $\gamma l=0$ as shown in Figs. 9 and 12 with variation of $\gamma l$. For electric displacement intensity factors as shown in Fig. 10, they have the same changing rule with variation of $\gamma l$ as stress intensity factors as shown in (68-73). Here, they were omitted for the other cases. As shown in Fig. 9, it can be obtained that the stress intensity factors $K(l)/(\tau_0\sqrt{l})=K(-l)/(\tau_0\sqrt{l})=1.0$ for $\gamma l=0$. It is the same as the closed solution as shown in (72) and (73). This is also proved that the

![](./images/811957058671738881_24.jpg)

![](./images/811957058671738881_25.jpg)

Fig. 12 Stress intensity factor versus $\gamma l$ for $l=1.0$ and $D_{0}/\varepsilon_{0}=4.0\times 10^{8}\ (\tau_{0}(x)=p_{2}(x/l)^{2})$

![](./images/811957058671738881_26.jpg)

Fig. 13 Stress intensity factor versus $\gamma l$ for $l=1.0$ and $D_{0}/\varepsilon_{0}=4.0\times 10^{8}\ (\tau_{0}(x)=p_{3}(x/l)^{3})$

Schmidt method is performed satisfactorily to solve this problem. However, for the anti-symmetric stress loading, the stress intensity factors at the crack tips are anti-symmetric about the point $K=0$ and $\gamma l=0$ as shown in Figs. 11 and 13 with variation of $\gamma l$. In this case, the symbols of the stress intensity factors are opposite as shown in Figs. 11 and 13. So we only discuss the properties of stress and electric displacement intensity factors at the right tip of crack with variation of $\gamma l$ as follows.

(vii) For the symmetric loading as shown in Figs. 9 and 12, stress and electric displacement intensity factors at the right tip of crack have a slight decrease with the increase of the gradient parameter $\gamma l$ for $\gamma l\leq -1.3$, then it increases until reaching a maximum peak value at $\gamma l\approx 0.65$, soon afterwards it decreases rapidly with the increase of $\gamma l$.

![](./images/811957058671738881_27.jpg)

Fig. 14 Stress intensity factor versus $l$ for $\gamma=0.4$ and $D_{0}/\varepsilon_{0}=4.0\times 10^{8}\ (\tau_{0}(x)=p_{0})$

(viii) For the anti-symmetric loading as shown in Figs. 11 and 13, the stress intensity factors at the right tip of crack have a slight increase with the increase of the gradient parameter $\gamma l$ for $\gamma l\leq 0.8$, and then it increases rapidly with the increase of $\gamma l$. Certainly, the magnitudes of the stress intensity factors are different for the different stress loading.

(viii) As shown in Fig. 14, it can be obtained that the value of stress intensity factor at the left tip of the crack decreases with the increase of the crack length. However, the value of stress intensity factor at the right tip of the decreases with the increase of the crack length for $l<1.7$, then it increases. This phenomenon may be cased by the effect of the functionally graded materials as discussed in Ref. [28]. It should be further studied.

Acknowledgements This work was supported by the National Natural Science Foundation of China (10572043), the Natural Science Foundation with Excellent Young Investigators of Heilongjiang Province (JC04-08), the National Science Foundation with Excellent Young Investigators of China (10325208) and the National Natural Science Key Item Foundation of China (10432030).

### References
1. Zhu X, Zhu J, Zhou S, Li Q, Liu Z (1999) Microstructures of the monomorph piezoelectric ceramic actuators with functionally gradient. Sens Actuators A 74:198-202
2. Takagi K, Li JF, Yokoyama S, Watanabe R (2003) Fabrication and evaluation of PZT/Pt piezoelectric composites and functionally graded actuators. J Eur Ceram Soc 10:1577-1583
3. Chen J, Liu ZX, Zou ZZ (2003) Electriomechanical impact of a crack in a functionally graded piezoelectric medium. Theor Appl Fract Mech 39:47-60

![](./images/811957058671738881_28.jpg)

4. Ueda S (2006) Transient response of a center crack in a functionally graded piezoelectric strip under electro- mechanical impact. Eng Fract Mech 73:1455–1471

5. Jin B, Zhong Z (2002) A moving mode-III crack in func- tionally graded piezoelectric material: permeable problem. Mech Res Commun 29:217–224

6. Wang BL (2003) A mode-III crack in functionally graded piezoelectric materials. Mech Res Commun 30:151–159

7. Li CY, Weng GJ (2002) Antiplane crack problem in functionally graded piezoelectric materials. J Appl Mech 69(4):481–488

8. Zhou ZG, Wang B (2004) Two parallel symme- try permeable cracks in functionally graded piezoelec- tric/piezomagnetic materials under anti-plane shear load- ing. Int J Solids Struct 41:4407–4422

9. Zhou ZG, Wu LZ, Wang B (2005) The behavior of a crack in functionally graded piezoelectric/piezomagnetic materials under anti-plane shear loading. Arch Appl Mech 74(8):526–535

10. Morse PM, Feshbach H (1958) Methods of theoretical physics, vol 1. McGraw-Hill, New York

11. Gao HJ, Zhang TY, Tong P (1997) Local and global energy release rates for an electrically yielded crack in a piezoelec- tric ceramics. J Mech Phys Solids 45(4):491–510

12. Zhang TY, Qian CF, Tong P (1998) Linear electro-elastic analysis of a cavity or a crack in a piezoelectric material. Int J Solids Struct 35:2121–2149

13. Zhong Z, Meguid SA (1997) Analysis of a circular arc- crack in piezoelectric materials. Int J Fract 84:143–158

14. Parton VS (1976) Fracture mechanics of piezoelectric ma- terials. ACTA Astronaut 3:671–683

15. Mikhailov GK, Parton VS (1990) Electromagnetoelasticity. Hemisphere, New York

16. Pak YE (1990) Crack extension force in a piezoelectric ma- terial. J Appl Mech 57:647–653

17. Han JJ, Chen YH (1999) Multiple parallel cracks interac- tion problem in piezoelectric ceramics. Int J Solids Struct 36:3375–3390

18. Soh AK, Fang DN, Lee KL (2000) Analysis of a bi- piezoelectric ceramic layer with an interfacial crack sub- jected to anti-plane shear and in-plane electric loading. Eur J Mech A/Solid 19:961–977

19. Hao TH, Shen ZY (1994) A new electric boundary condi- tion of electric fracture mechanics and its applications. Eng Fract Mech 47(6):793–802

20. Hao TH (2001) Multiple collinear cracks in a piezoelectric material. Int J Solids Struct 38(50–51):9201–9208

21. Yang FQ (2001) Fracture mechanics for a Mode I crack in piezoelectric materials. Int J Solids Struct 38:3813–3830

22. Gradshteyn IS, Ryzhik IM (1980) Table of integrals, series and products. Academic Press, New York

23. Erdelyi A (ed) (1954) Tables of integral transforms, vol 1. McGraw-Hill, New York

24. Zhou ZG, Wang B, Yang LJ (2004) Investigation of the behavior of an interface crack between two half-planes of orthotropic functionally graded materials by using a new method. JSME Int J 47(3):467–478

25. Itou S (1978) Three dimensional waves propagation in a cracked elastic solid. J Appl Mech 45(5):807–811

26. Zhou ZG, Wu LZ, Wang B (2006) The scattering of harmonic elastic anti-plane shear waves by two collinear cracks in anisotropic material plane by using the non-local theory. Meccanica 41(6):591–598

27. Zhou ZG, Wang B (2006) Investigation of the behavior of an interface crack for a functionally graded strip sand- wiched between two homogeneous layers of finite thick- ness by use of the Schmidt method for the opening mode. Meccanica 41(2):79–99

28. Shbeeb NI, Binienda WK (1999) Analysis of an inter- face crack for a functionally graded strip sandwiched be- tween two homogeneous layers of finite thickness. Eng Fract Mech 64:693–720

![](./images/811957058671738881_29.jpg)