![](./images/811985670590431234_1.jpg)

Available online at www.sciencedirect.com

![](./images/811985670590431234_2.jpg)

International Journal of Engineering Science 45 (2007) 242–257

International
Journal of
Engineering
Science

www.elsevier.com/locate/ijengsci

# Investigation of the behavior of a mode-I crack
in functionally graded materials by non-local theory

Zhen-Gong Zhou *, Pei-Wei Zhang, Lin-Zhi Wu

Center for Composite Materials and Structures, Harbin Institute of Technology, P.O. Box 3010, Harbin 150080, PR China

Received 18 September 2006; received in revised form 8 December 2006; accepted 8 December 2006
Available online 7 June 2007

## Abstract

In this paper, the behavior of a mode-I crack in functionally graded materials is investigated by means of the non-local theory. The traditional concepts of the non-local theory are firstly extended to solve the mode-I crack fracture problem in functionally graded materials, in which the shear modulus varies exponentially with coordinate parallel to the crack. Through the Fourier transform, the problem can be solved with the help of two pairs of dual integral equations, in which the unknown variables are jumps of displacements across crack surfaces, not the dislocation density functions or the analysis functions. To solve the dual integral equations, the jumps of displacements across crack surfaces are directly expanded in a series of Jacobi polynomials. Unlike the classical elasticity solutions, it is found that no stress singularity is present near crack tips. The non-local elastic solutions yield a finite stress at crack tips, thus allowing us to use the maximum stress as a fracture criterion. Numerical examples are provided to show the effects of the crack length, the parameter describing functionally graded materials, the lattice parameter of materials and the material constants upon the stress fields near crack tips.

© 2007 Elsevier Ltd. All rights reserved.

Keywords: Crack; Functionally graded materials; Non-local theory; Mechanics of solids

## 1. Introduction

From the fracture mechanics viewpoint, the presence of a graded interlayer would play an important role in determining the crack driving forces and fracture resistance parameters. In an attempt to address the issues pertaining to the fracture analysis of bonded media with such transitional interfacial properties, a series of solutions to certain crack problems was obtained by Erdogan and his associates [1–3]. Similar problems of delamination or an interface crack between the functionally graded coating and the substrate were considered in Refs. [4–6]. The dynamic crack problem for the non-homogeneous composite materials was considered in Ref. [7] but they considered the FGM layer as multi-layered homogeneous media. Relatively few experimental and numerical investigations of the fracture behavior of FGMs (functionally graded materials) have been

* Corresponding author.
E-mail address: zhouzhg@hit.edu.cn (Z.-G. Zhou).

0020-7225/$ - see front matter © 2007 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijengsci.2007.03.018

conducted. Experimental investigations on the fracture of FGMs are limited due to the high cost and elaborate facilities required for processing FGMs [8-10]. The finite element method has also been used to simulate the fracture behavior of cracked FGMs [11,12]. The crack problem in FGM layers under thermal stresses was studied by Erdogan and Wu [13]. They considered an unconstrained elastic layer under statically self-equili- brating thermal or residual stresses. The interface crack problem for a non-homogeneous coating bonded to a homogeneous substrate was investigated in Ref. [14]. However, it is found that all the solutions in Refs. [1-14] contain the stress singularities at crack tips, which is not reasonable according to the physical nature. As a result of this, beginning with Griffith, all fracture criteria in practice today based on other considerations, e.g. energy, the $J$-integral [15] and the strain gradient theory [16].

To overcome the stress singularities at crack tips in the classical elastic fracture theory, Eringen [17-19] used the non-local theory to study the stress near the tip of a sharp line crack in an isotropic elastic plate subject to uniform tension, shear and anti-plane shear, and the resulting solutions did not contain any stress singularities at the crack tips. This allows us to use the maximum stress as a fracture criterion. In contrast to these local approaches, of zero-range internal interactions, the modern non-local continuum mechanics originated and developed in the last five decades. Edelen [20] contributed some mathematical formalism while Green [21] sim- ply enunciated some postulates for the non-local theory. On the other hand, Eringen [22] contributed not just the complete physics and mathematics of the non-local theory but also, in addition, shaped the theory into a concrete form making it viable for practical applications to boundary value problems. According to the non- local theory, the stress at a point $X$ in a body depends not only on the strain at point $X$ but also on that at all other points of the body. This is contrary to the classical theory that the stress at a point $X$ in a body depends only on the strain at point $X$. The basic idea of the non-local elasticity is to build a relationship between mac- roscopic mechanical quantities and microscopic physical quantities within the framework of continuum mechanics. The constitutive theory of the non-local elasticity has been developed in Ref. [20], in which the elastic modulus is influenced by the microstructure of the material. Other results have been given by the appli- cation of the non-local elasticity to the fields such as a dislocation near a crack [23,24], and fracture mechanics problems [25,26]. The literature on the fundamental aspects of non-local continuum mechanics is relatively extensive. The results of those concrete problems that were solved display a rather remarkable agreement with experimental evidence. This can be used to predict the cohesive stress for various materials and the results close to those obtained in atomic lattice dynamics [27,28]. Recently, some fracture problems [29-32] in an iso- tropic elastic material and the piezoelectric material have been studied by use of the non-local theory with a somewhat different method. More recently, the traditional concepts of the non-local theory are also extended to solve the anti-plane shear fracture problem of functionally graded materials [33,34], and the resulting solu- tions [33,34] did not contain any stress singularities at the crack tips. However, only the anti-plane shear frac- ture problems were considered in Refs. [33,34]. To our knowledge, the effect of the lattice parameter of functionally graded materials on the stress field near the mode-I crack tips has not been studied by use of the non-local theory due to the mathematical complexities. The present work is an attempt to offer the related information. Here, we give a theoretical solution for this problem.

In the present paper, the traditional concepts of the non-local theory are also extended to solve the mode-I crack problem of functionally graded materials, i.e., the stress fields near the mode-I crack tips in functionally graded materials are investigated by use of the non-local theory with Schmidt method [35,36]. To make the analysis tractable, it is assumed that the shear modulus varies exponentially with coordinate parallel to the crack. Fourier transform is applied and a mixed boundary value problem is reduced to two pairs of dual inte- gral equations, in which the unknown variables are jumps of displacements across crack surfaces, not the dis- location density functions or the analysis functions. To solve the dual integral equations, the jumps of displacements across crack surfaces are directly expanded in a series of Jacobi polynomials. Numerical solu- tions are obtained for the stress fields near crack tips. Contrary to the previous results, it is found that the solution does not contain any stress singularities at crack tips.

## 2. Formulation of the problem

It is assumed that there is a finite crack of length $2 l$ in the functionally graded materials as shown in Fig. 1. The lower half plane of functionally graded materials is denoted as material 1. The upper half plane of

![](./images/811985670590431234_3.jpg)

Fig. 1. Geometry of a finite crack in the functionally graded materials.

functionally graded materials is denoted as material 2. It is assumed that a tension stress loading $\tau_{yy}(x,0)=-\tau_0(x)$ ($\tau_0(x)$ is a magnitude of the stress loading) are applied over the upper and lower crack surfaces. Here, the standard superposition technique is used. As discussed in Ref. [19], the boundary conditions can be written as follows:

$$
\tau_{yy}^{(1)}(x,0)=\tau_{yy}^{(2)}(x,0)=-\tau_0(x),\quad \tau_{xy}^{(1)}(x,0)=\tau_{xy}^{(2)}(x,0)=0,\quad |x|\leqslant l \tag{1}
$$

$$
\tau_{yy}^{(1)}(x,0)=\tau_{yy}^{(2)}(x,0),\quad \tau_{xy}^{(1)}(x,0)=\tau_{xy}^{(2)}(x,0),\quad |x|> l \tag{2}
$$

$$
u^{(1)}(x,0)=u^{(2)}(x,0),\quad v^{(1)}(x,0)=v^{(2)}(x,0),\quad |x|> l \tag{3}
$$

$$
u^{(j)}(x,y)=v^{(j)}(x,y)=0,\quad \sqrt{x^2+y^2}\to\infty \tag{4}
$$

The superscript $j=1,2$ correspond to the half-planes $y\leqslant0$ and $y\geqslant0$ through in this paper as shown in Fig. 1.

### 3. Basic equations of non-local functionally graded materials

With vanishing body force, the basic equations of linear, isotropic, non-local functionally graded materials plane with the variable shear modulus are

$$
\frac{\partial\tau_{xx}^{(j)}}{\partial x}+\frac{\partial\tau_{xy}^{(j)}}{\partial y}=0\quad (j=1,2) \tag{5}
$$

$$
\frac{\partial\tau_{xy}^{(j)}}{\partial x}+\frac{\partial\tau_{yy}^{(j)}}{\partial y}=0\quad (j=1,2) \tag{6}
$$

$$
\tau_{xx}^{(j)}(x,y)=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\mu(|x'-x|,|y'-y|)\left[\frac{1+k}{k-1}\frac{\partial u^{(j)}(x',y')}{\partial x'}+\frac{3-k}{k-1}\frac{\partial v^{(j)}(x',y')}{\partial y'}\right]\mathrm{d}x'\mathrm{d}y'\quad (j=1,2) \tag{7}
$$

$$
\tau_{yy}^{(j)}(x,y)=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\mu(|x'-x|,|y'-y|)\left[\frac{1+k}{k-1}\frac{\partial v^{(j)}(x',y')}{\partial y'}+\frac{3-k}{k-1}\frac{\partial u^{(j)}(x',y')}{\partial x'}\right]\mathrm{d}x'\mathrm{d}y'\quad (j=1,2) \tag{8}
$$

$$
\tau_{xy}^{(j)}(x,y)=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\mu(|x'-x|,|y'-y|)\left[\frac{\partial v^{(j)}(x',y')}{\partial x'}+\frac{\partial u^{(j)}(x',y')}{\partial y'}\right]\mathrm{d}x'\mathrm{d}y'\quad (j=1,2) \tag{9}
$$

where $k=3-4v$ for the plane strain state, $k=(3-v)/(1+v)$ for the generalized plane stress state. In this paper, we just consider the plane strain problem. $v$ is the Poisson's ratio. The Poisson's ratio $v$ is taken to be a constant; owing to the fact its variation within a practical range has the rather insignificant influence on the value of the near-tip driving for fracture [1-3].

In the constitutive Eqs. (7)-(9), the only difference from classical elastic theory is in which the stress $\tau_{ik}^{(j)}(x,y)$ $(i,k=x,y)$ at a point $(x,y)$ depends on $u_k^{(j)}(x,y)$, $v_k^{(j)}(x,y)$, at all points of the body. $u^{(j)}(x,y)$ and $v^{(j)}(x,y)$ are the components of the displacement. For a isotropic, non-local functionally graded materials, the shear mod-

ulus $\mu(|x'-x|, |y'-y|)$ is a function of the distance $d = \sqrt{(x'-x)^2 + (y'-y)^2}$. As discussed in Refs. [27,28], it can be assumed in the form of $\mu(|x'-x|, |y'-y|)$ for which the dispersion curves of plane elastic waves coincide with those known in lattice dynamics. Among several possible curves the following has been found to be very useful

$$
\mu(|x'-x|, |y'-y|) = \mu_0^{*}(x)\alpha(|x'-x|, |y'-y|) \tag{10}
$$

$$
\alpha(|x'-x|, |y'-y|) = \alpha_0 \exp\left\{-(\beta/a)^2[(x'-x)^2 + (y'-y)^2]\right\} \tag{11}
$$

where $\alpha(|x'-x|, |y'-y|)$ is called as influence function. $\beta$ is also a constant and can be determined by experiment, as stated in Refs. [17-19], and $a$ is the characteristic length. The characteristic length may be selected according to the range and sensitivity of the physical phenomena. For instance, for a perfect crystal, $a$ may be taken as the lattice parameter. For a granular material, $a$ may be considered to be the average granular distance and for a fiber composite, the fiber distance, etc. In the present paper, $a$ is taken as the lattice parameter of the materials. $\alpha_0$ is determined by the normalization

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \alpha(|x'-x|, |y'-y|) \mathrm{d}x' \mathrm{d}y' = 1 \tag{12}
$$

However, the influence function $\alpha(|x'-x|, |y'-y|)$ should be assumed that the averaging is performed only on the part of the domain of influence that lies within the vicinity of the boundary of a finite body. This problem should be studied further. In the present work, the influence function $\alpha(|x'-x|, |y'-y|)$ in Eq. (12) has an infinite support. The non-local material parameters were given by Eqs. (10) and (11). Substituting Eq. (11) into Eq. (12), it can be obtained, in two-dimensional space,

$$
\alpha_0 = \frac{1}{\pi} (\beta/a)^2 \tag{13}
$$

Crack problems in functionally graded materials do not appear to be analytically tractable for arbitrary variations of material properties. Usually, one tries to generate the forms of functionally graded materials for which the problem becomes tractable. Similar to the treatment of the crack problem for the isotropic functionally graded materials in Refs. [13,14], we assume the material properties are described by

$$
\mu_0^{*}(x) = \mu_0 \mathrm{e}^{\gamma x} \tag{14}
$$

where $\mu_0$ is the shear modulus along the crack line. Only along the crack line $\mu_0$ is a constant value of the shear modulus of the material, which is exponentially graded. $\gamma$ is a constant which describes the functionally graded materials. $\gamma \neq 0$ is the case for the functionally graded materials. When $\gamma = 0$, it will return to the homogenous material case.

Substitution of Eqs. (10), (11) and (14) into Eqs. (7)-(9) yields

$$
\tau_{ik}^{(j)}(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \alpha(|x'-x|, |y'-y|)\sigma_{ik}^{(j)}(x',y') \mathrm{d}x' \mathrm{d}y' \quad (i,k=x,y) \tag{15}
$$

where

$$
\sigma_{xx}^{(j)}(x,y) = \mu_0 \mathrm{e}^{\gamma x} \left[ \frac{1+k}{k-1} \frac{\partial u^{(j)}(x,y)}{\partial x} + \frac{3-k}{k-1} \frac{\partial v^{(j)}(x,y)}{\partial y} \right] \tag{16}
$$

$$
\sigma_{yy}^{(j)}(x,y) = \mu_0 \mathrm{e}^{\gamma x} \left[ \frac{1+k}{k-1} \frac{\partial v^{(j)}(x,y)}{\partial y} + \frac{3-k}{k-1} \frac{\partial u^{(j)}(x,y)}{\partial x} \right] \tag{17}
$$

$$
\sigma_{xy}^{(j)}(x,y) = \mu_0 \mathrm{e}^{\gamma x} \left[ \frac{\partial v^{(j)}(x,y)}{\partial x} + \frac{\partial u^{(j)}(x,y)}{\partial y} \right] \tag{18}
$$

The expressions (16)-(18) are the classical constitutive equations.

Substituting Eq. (15) into Eqs. (5), (6), respectively, and using the Green–Gauss theorem, we have

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right)\left(\frac{\partial \sigma_{x x}^{(j)}\left(x^{\prime}, y^{\prime}\right)}{\partial x^{\prime}}+\frac{\partial \sigma_{x y}^{(j)}\left(x^{\prime}, y^{\prime}\right)}{\partial y^{\prime}}\right) \mathrm{d} x^{\prime} \mathrm{d} y^{\prime} \\
& \quad-\int_{-l}^{l} \alpha\left(\left|x^{\prime}-x\right|,|0|\right)\left[\left[\sigma_{x y}^{(j)}\left(x^{\prime}, 0\right)\right]\right] \mathrm{d} x^{\prime}=0
\end{aligned}
$$

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right)\left(\frac{\partial \sigma_{x y}^{(j)}\left(x^{\prime}, y^{\prime}\right)}{\partial x^{\prime}}+\frac{\partial \sigma_{y y}^{(j)}\left(x^{\prime}, y^{\prime}\right)}{\partial y^{\prime}}\right) \mathrm{d} x^{\prime} \mathrm{d} y^{\prime} \\
& \quad-\int_{-l}^{l} \alpha\left(\left|x^{\prime}-x\right|,|0|\right)\left[\left[\sigma_{y y}^{(j)}\left(x^{\prime}, 0\right)\right]\right] \mathrm{d} x^{\prime}=0
\end{aligned}
$$

Here the surface integral may be dropped since the displacement field vanishes at infinity. $\llbracket \rrbracket$ indicates a jump on the crack line, i.e.

$$
\left[\left[\sigma_{x y}^{(j)}(x, 0)\right]\right]=\sigma_{x y}^{(j)}\left(x, 0^{+}\right)-\sigma_{x y}^{(j)}\left(x, 0^{-}\right)
$$

$$
\left[\left[\sigma_{y y}^{(j)}(x, 0)\right]\right]=\sigma_{y y}^{(j)}\left(x, 0^{+}\right)-\sigma_{y y}^{(j)}\left(x, 0^{-}\right)
$$

As discussed in Ref. [19], it can be obtained that

$$
\left[\left[\sigma_{x y}^{(j)}(x, 0)\right]\right]=0, \quad\left[\left[\sigma_{y y}^{(j)}(x, 0)\right]\right]=0
$$

Hence from Eqs. (19) and (20), it can be obtained that

$$
\frac{\partial \sigma_{x x}(x, y)}{\partial x}+\frac{\partial \sigma_{x y}(x, y)}{\partial y}=0
$$

$$
\frac{\partial \sigma_{x y}(x, y)}{\partial x}+\frac{\partial \sigma_{y y}(x, y)}{\partial y}=0
$$

almost everywhere. Substituting Eqs. (16)–(18) into Eqs. (24) and (25), the governing equations are obtained as

$$
(1+k) \frac{\partial^{2} u^{(j)}}{\partial x^{2}}+(k-1) \frac{\partial^{2} u^{(j)}}{\partial y^{2}}+2 \frac{\partial^{2} v^{(j)}}{\partial x \partial y}+\gamma\left[(1+k) \frac{\partial u^{(j)}}{\partial x}+(3-k) \frac{\partial v^{(j)}}{\partial y}\right]=0
$$

$$
(1+k) \frac{\partial^{2} v^{(j)}}{\partial y^{2}}+(k-1) \frac{\partial^{2} v^{(j)}}{\partial x^{2}}+2 \frac{\partial^{2} u^{(j)}}{\partial x \partial y}+\gamma(k-1)\left(\frac{\partial v^{(j)}}{\partial x}+\frac{\partial u^{(j)}}{\partial y}\right)=0
$$

## 4. Solution procedures

The system of above governing Eqs. (26) and (27) are solved, using the Fourier integral transform to obtain the general expressions for displacement components satisfying Eq. (4) as

$$
\left\{\begin{array}{l}
u^{(1)}(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} A_{i}(s) \mathrm{e}^{-\lambda_{i+2} y} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s \\
v^{(1)}(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} m_{i+2}(s) A_{i}(s) \mathrm{e}^{-\lambda_{i+2} y} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
\end{array}\right.
$$

$$
\left\{\begin{array}{l}
u^{(2)}(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} B_{i}(s) \mathrm{e}^{-\lambda_{i} y} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s \\
v^{(2)}(x, y)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} m_{i}(s) B_{i}(s) \mathrm{e}^{-\lambda_{i} y} \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
\end{array}\right.
$$

and from Eqs. (16)-(18), the stress components are obtained as

$$
\left\{
\begin{aligned}
\sigma_{yy}^{(1)}(x,y) &= \frac{\mu_0 \mathrm{e}^{\gamma x}}{2\pi(k-1)} \int_{-\infty}^{\infty} \sum_{i=1}^{2} [-(k+1)m_{i+2}(s)\lambda_{i+2} + \mathrm{i}s(3-k)] A_i(s) \mathrm{e}^{-\lambda_{i+2}y} \mathrm{e}^{\mathrm{i}sx} \mathrm{d}s \\
\sigma_{xy}^{(1)}(x,y) &= \frac{\mu_0 \mathrm{e}^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} [-\lambda_{i+2} + \mathrm{i}sm_{i+2}(s)] A_i(s) \mathrm{e}^{-\lambda_{i+2}y} \mathrm{e}^{\mathrm{i}sx} \mathrm{d}s
\end{aligned}
\right. \tag{30}
$$

$$
\left\{
\begin{aligned}
\sigma_{yy}^{(2)}(x,y) &= \frac{\mu_0 \mathrm{e}^{\gamma x}}{2\pi(k-1)} \int_{-\infty}^{\infty} \sum_{i=1}^{2} [-(k+1)m_i(s)\lambda_i + \mathrm{i}s(3-k)] B_i(s) \mathrm{e}^{-\lambda_i y} \mathrm{e}^{\mathrm{i}sx} \mathrm{d}s \\
\sigma_{xy}^{(2)}(x,y) &= \frac{\mu_0 \mathrm{e}^{\gamma x}}{2\pi} \int_{-\infty}^{\infty} \sum_{i=1}^{2} [-\lambda_i + \mathrm{i}sm_i(s)] B_i(s) \mathrm{e}^{-\lambda_i y} \mathrm{e}^{\mathrm{i}sx} \mathrm{d}s
\end{aligned}
\right. \tag{31}
$$

where $s$ is the transform variable. $A_1$, $A_2$, $B_1$ and $B_2$ are arbitrary unknowns, $\lambda_i(s)$ ($i=1,2,3,4$) are the roots of the characteristic equation

$$
\lambda^4 + \left(2\mathrm{i}s\gamma - 2s^2 - \gamma^2 \frac{3-k}{k+1}\right)\lambda^2 + s^4 - 2\mathrm{i}s^3\gamma - \gamma^2 s^2 = 0 \tag{32}
$$

and $m_{i(s)}$ ($i=1,2,3,4$) are expressed for each root $\lambda_{i(s)}$ as

$$
m_i(s) = \frac{-(k+1)s^2 + (k-1)\lambda_i^2 + \mathrm{i}s\gamma(k+1)}{\lambda_i[2\mathrm{i}s + \gamma(3-k)]} \tag{33}
$$

The roots may be obtained as

$$
\lambda_1 = \sqrt{\frac{(-b + \sqrt{b^2 - 4c})}{2}}, \quad \lambda_2 = \sqrt{\frac{(-b - \sqrt{b^2 - 4c})}{2}} \tag{34}
$$

$$
\lambda_3 = -\sqrt{\frac{(-b + \sqrt{b^2 - 4c})}{2}}, \quad \lambda_4 = -\sqrt{\frac{(-b - \sqrt{b^2 - 4c})}{2}} \tag{35}
$$

where $b=2\mathrm{i}s\gamma - 2s^2 - \gamma^2 \frac{3-k}{k+1}$, $c=s^4 - 2\mathrm{i}s^3\gamma - \gamma^2 s^2$.

From Eqs. (30) and (31), it can be seen that there are four unknown constants (in Fourier space they are functions of $s$), i.e, $A_1$, $A_2$, $B_1$ and $B_2$ which can be obtained from the boundary conditions.

To solve the present problem, the jumps of displacements across crack surfaces can be defined as follows:

$$
f_1(x) = u^{(2)}(x,0) - u^{(1)}(x,0) \tag{36}
$$

$$
f_2(x) = v^{(2)}(x,0) - v^{(1)}(x,0) \tag{37}
$$

Applying the Fourier transforms and the boundary conditions (1)-(3), it can be obtained

$$
[X_1] \begin{bmatrix} B_1(s) \\ B_2(s) \end{bmatrix} - [X_2] \begin{bmatrix} A_1(s) \\ A_2(s) \end{bmatrix} = \begin{bmatrix} \bar{f}_1(s) \\ \bar{f}_2(s) \end{bmatrix} \tag{38}
$$

$$
[X_3] \begin{bmatrix} B_1(s) \\ B_2(s) \end{bmatrix} = [X_4] \begin{bmatrix} A_1(s) \\ A_2(s) \end{bmatrix} \tag{39}
$$

where the matrices $[X_i]$ ($i=1,2,3,4$) can be seen in the Appendix attached to this paper. A superposed bar indicates the Fourier transform through the paper.

From Eq. (15), we have

$$
\tau_{y y}^{(1)}(x, y)=\int_{0}^{\infty}\left[\int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right) \sigma_{y y}^{(2)}\left(x^{\prime}, y^{\prime}\right) \mathrm{d} x^{\prime}\right] \mathrm{d} y^{\prime}+\int_{-\infty}^{0}\left[\int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right) \sigma_{y y}^{(1)}\left(x^{\prime}, y^{\prime}\right) \mathrm{d} x^{\prime}\right] \mathrm{d} y^{\prime}
\tag{40}
$$

$$
\tau_{x y}^{(1)}(x, y)=\int_{0}^{\infty}\left[\int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right) \sigma_{x y}^{(2)}\left(x^{\prime}, y^{\prime}\right) \mathrm{d} x^{\prime}\right] \mathrm{d} y^{\prime}+\int_{-\infty}^{0}\left[\int_{-\infty}^{\infty} \alpha\left(\left|x^{\prime}-x\right|,\left|y^{\prime}-y\right|\right) \sigma_{x y}^{(1)}\left(x^{\prime}, y^{\prime}\right) \mathrm{d} x^{\prime}\right] \mathrm{d} y^{\prime}
\tag{41}
$$

Using the relations as follows [37]:

$$
\int_{0}^{\infty} \mathrm{e}^{-p x^{2}-v x} \sin (b x) \mathrm{d} x=-\frac{\mathrm{i}}{4} \sqrt{\frac{\pi}{p}}\left\{\exp \left(\frac{(v-\mathrm{i} b)^{2}}{4 p}\right)\left[1-\Phi\left(\frac{v-\mathrm{i} b}{2 \sqrt{p}}\right)\right]-\exp \left(\frac{(v+\mathrm{i} b)^{2}}{4 p}\right)\left[1-\Phi\left(\frac{v-\mathrm{i} b}{2 \sqrt{p}}\right)\right]\right\}
\tag{42}
$$

$$
\int_{0}^{\infty} \mathrm{e}^{-p x^{2}-v x} \cos (b x) \mathrm{d} x=\frac{1}{4} \sqrt{\frac{\pi}{p}}\left\{\exp \left(\frac{(v-\mathrm{i} b)^{2}}{4 p}\right)\left[1-\Phi\left(\frac{v-\mathrm{i} b}{2 \sqrt{p}}\right)\right]+\exp \left(\frac{(v+\mathrm{i} b)^{2}}{4 p}\right)\left[1-\Phi\left(\frac{v-\mathrm{i} b}{2 \sqrt{p}}\right)\right]\right\}
\tag{43}
$$

$$
\int_{0}^{\infty} \exp \left(-p y^{2}-\gamma y\right) \mathrm{d} y=\frac{1}{2}(\pi / p)^{1 / 2} \exp \left(\gamma^{2} / 4 p\right)[1-\Phi(\gamma / 2 \sqrt{p})]
\tag{44}
$$

$$
\Phi(z)=\frac{2}{\sqrt{\pi}} \int_{0}^{z} \exp \left(-t^{2}\right) \mathrm{d} t
\tag{45}
$$

We have

$$
\tau_{y y}^{(1)}(x, y)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi(k-1)} \int_{-\infty}^{\infty}\left[\sum_{i=1}^{2} g_{i}(s) n_{i}(s, y) B_{i}(s)+\sum_{i=1}^{2} g_{i+2}(s) q_{i}(s, y) A_{i}(s)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
\tag{46}
$$

$$
\tau_{x y}^{(1)}(x, y)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi} \int_{-\infty}^{\infty}\left[\sum_{i=1}^{2} h_{i}(s) n_{i}(s, y) B_{i}(s)+\sum_{i=1}^{2} h_{i+2}(s) q_{i}(s, y) A_{i}(s)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
\tag{47}
$$

where $g_{i}(s)=-(k+1) m_{i}(s) \lambda_{i}+\mathrm{i} s(3-k), h_{i}(s)=-\lambda_{i}+\mathrm{i} s m_{i}(s)$ ($i=1,2,3,4$),

$$
\begin{aligned}
n_{i}(s, y) & =\frac{1}{4} \mathrm{e}^{-p y^{2}} \mathrm{e}^{\frac{\left(\lambda_{i}-2 p y\right)^{2}}{4 p}}\left[1-\Phi\left(\frac{\lambda_{i}-2 p y}{2 \sqrt{p}}\right)\right] \mathrm{e}^{\frac{(\gamma+\mathrm{i} s)^{2}}{4 p}}\left[2-\Phi\left(\frac{-\gamma-\mathrm{i} s}{2 \sqrt{p}}\right)-\Phi\left(\frac{\gamma+\mathrm{i} s}{2 \sqrt{p}}\right)\right] \\
& =\frac{1}{2} \mathrm{e}^{-p y^{2}} \mathrm{e}^{\frac{\left(\lambda_{i}-2 p y\right)^{2}}{4 p}}\left[1-\Phi\left(\frac{\lambda_{i}-2 p y}{2 \sqrt{p}}\right)\right] \mathrm{e}^{\frac{(\gamma+\mathrm{i} s)^{2}}{4 p}},
\end{aligned}
$$

$$
\begin{aligned}
q_{i}(s, y) & =\frac{1}{4} \mathrm{e}^{-p y^{2}} \mathrm{e}^{\frac{\left(-\lambda_{i+2}+2 p y\right)^{2}}{4 p}}\left[1-\Phi\left(\frac{-\lambda_{i+2}+2 p y}{2 \sqrt{p}}\right)\right] \mathrm{e}^{\frac{(\gamma+\mathrm{i} s)^{2}}{4 p}}\left[2-\Phi\left(\frac{-\gamma-\mathrm{i} s}{2 \sqrt{p}}\right)-\Phi\left(\frac{\gamma+\mathrm{i} s}{2 \sqrt{p}}\right)\right] \\
& =\frac{1}{2} \mathrm{e}^{-p y^{2}} \mathrm{e}^{\frac{\left(-\lambda_{i+2}+2 p y\right)^{2}}{4 p}}\left[1-\Phi\left(\frac{-\lambda_{i+2}+2 p y}{2 \sqrt{p}}\right)\right] \mathrm{e}^{\frac{(\gamma+\mathrm{i} s)^{2}}{4 p}}, \quad \Phi(z)=-\Phi(-z), \quad p=\left(\frac{\beta}{a}\right)^{2} \quad(i=1,2).
\end{aligned}
$$

By solving four Eqs. (38) and (39) with four unknown functions $A_{1}, A_{2}, B_{1}$ and $B_{2}$, substituting the solutions into Eqs. (28), (29), (46) and (47), and applying the boundary conditions (1)-(3) to the results, we have

$$
\tau_{y y}^{(1)}(x, 0)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi(k-1)} \int_{-\infty}^{\infty}\left[d_{1}(s) \bar{f}_{1}(s)+d_{2}(s) \bar{f}_{2}(s)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=-\tau_{0}(x), \quad-l \leqslant x \leqslant l
\tag{48}
$$

$$
\tau_{x y}^{(1)}(x, 0)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi} \int_{-\infty}^{\infty}\left[d_{3}(s) \bar{f}_{1}(s)+d_{4}(s) \bar{f}_{2}(s)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=0, \quad-l \leqslant x \leqslant l
\tag{49}
$$

$$
\int_{-\infty}^{\infty} \bar{f}_{1}(s) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=0, \quad|x|>l
\tag{50}
$$

$$
\int_{-\infty}^{\infty} \bar{f}_{2}(s) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=0, \quad|x|>l
\tag{51}
$$

where
$$
d_{1}(s)=g_{1}(s) n_{10}(s) e_{11}(s)+g_{2}(s) n_{20}(s) e_{21}(s)+g_{3}(s) q_{10}(s) c_{11}(s)+g_{4}(s) q_{20}(s) c_{21}(s)
$$

$$
d_{2}(s)=g_{1}(s) n_{10}(s) e_{12}(s)+g_{2}(s) n_{20}(s) e_{22}(s)+g_{3}(s) q_{10}(s) c_{12}(s)+g_{4}(s) q_{20}(s) c_{22}(s)
$$

$$
d_{3}(s)=h_{1}(s) n_{10}(s) e_{11}(s)+h_{2}(s) n_{20}(s) e_{21}(s)+h_{3}(s) q_{10}(s) c_{11}(s)+h_{4}(s) q_{20}(s) c_{21}(s)
$$

$$
d_{4}(s)=h_{1}(s) n_{10}(s) e_{12}(s)+h_{2}(s) n_{20}(s) e_{22}(s)+h_{3}(s) q_{10}(s) c_{12}(s)+h_{4}(s) q_{20}(s) c_{22}(s)
$$

$n_{i 0}(s)=n_{i}(s, 0), q_{i 0}(s)=q_{i}(s, 0), e_{i j}(s)$ and $c_{i j}(s)(i=1,2, j=1,2)$ are known functions. It can be seen in the Appendix attached to this paper. To determine the unknown functions $\bar{f}_{1}(s)$ and $\bar{f}_{2}(s)$, the above two pairs of dual integral equations (48)-(51) must be solved. For the lattice parameter $a \rightarrow 0$, then $d_{i}(s) / s$ equal to non-zero constants and Eqs. (48)-(51) reduce to two pairs of dual integral equations for the same problem in the classical functionally graded materials.

## 5. Solution of the dual integral equations

The only difference between the classical and non-local equations is in the influence function $d_{i}(s)(i=1,2,3,4)$, it is logical to utilize the classical solution to convert the system Eqs. (48)-(51) to two pairs of the integral equation of the second kind, which is generally better behaved. For the lattice parameter $a \rightarrow 0$, then $d_{i}(s) / s(i=1,2,3,4)$ equals to non-zero constants and Eqs. (48)-(51) reduce to two pairs of dual integral equations for the same problem in classical elasticity. As discussed in Ref. [19], the dual integral equations (48)-(51) cannot be transformed into a Fredholm integral equation of the second kind, because $d_{i}(s) / s(i=1,2,3,4)$ does not tend to constants $c_{i}\left(c_{i} \neq 0, i=1,2,3,4\right)$ for $s \rightarrow \infty$. Of course, the dual integral equations (48)-(51) can be considered to be a single integral equation of the first kind with discontinuous kernel. It is well-known in the literature that integral equations of the first kind are generally ill-posed in sense of Hadamard, i.e. small perturbations of the data can yield arbitrarily large changes in the solution. This makes the numerical solution of such equations quite difficult. To overcome the difficult, the Schmidt method [35,36] is used to solve the dual integral equations (48)-(51). The jumps of displacements across crack surface can be expanded by the following series:

$$
f_{1}(x)=\sum_{n=0}^{\infty} a_{n} P_{n}^{\left(\frac{1}{2}, \frac{1}{2}\right)}\left(\frac{x}{l}\right)\left(1-\frac{x^{2}}{l^{2}}\right)^{\frac{1}{2}} \quad \text { for }-l \leqslant x \leqslant l
\tag{52}
$$

$$
f_{1}(x)=0 \quad \text { for }|x|>l
\tag{53}
$$

$$
f_{2}(x)=\sum_{n=0}^{\infty} b_{n} P_{n}^{\left(\frac{1}{2}, \frac{1}{2}\right)}\left(\frac{x}{l}\right)\left(1-\frac{x^{2}}{l^{2}}\right)^{\frac{1}{2}} \quad \text { for }-l \leqslant x \leqslant l
\tag{54}
$$

$$
f_{2}(x)=0 \quad \text { for }|x|>l
\tag{55}
$$

where $a_{n}$ and $b_{n}$ are unknown coefficients, $P_{n}^{(1 / 2,1 / 2)}(x)$ is a Jacobi polynomial [37].

The Fourier transforms of Eqs. (52)-(55) are as follows: [38]

$$
\bar{f}_{1}(s)=\sum_{n=0}^{\infty} a_{n} G_{n} \frac{1}{s} J_{n+1}(s l), \quad G_{n}=2 \sqrt{\pi}(-1)^{n} \mathrm{i}^{n} \frac{\Gamma\left(n+1+\frac{1}{2}\right)}{n!}
\tag{56}
$$

$$
\bar{f}_{2}(s)=\sum_{n=0}^{\infty} b_{n} G_{n} \frac{1}{s} J_{n+1}(s l)
\tag{57}
$$

where $\Gamma(x)$ and $J_{n(x)}$ are the Gamma and Bessel functions, respectively.

Substituting Eqs. (56), (57) into Eqs. (48)-(51), it can be shown that Eqs. (50) and (51) are automatically satisfied. Eqs. (48) and (49) are reduced to

$$
\frac{\mu_{0} \mathrm{e}^{\mathrm{i} x}}{2 \pi(k-1)} \sum_{n=0}^{\infty} \int_{-\infty}^{\infty} \frac{1}{s}\left[d_{1}(s) a_{n} G_{n} J_{n+1}(s l)+d_{2}(s) b_{n} G_{n} J_{n+1}(s l)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=-\tau_{0}(x), \quad-l \leqslant x \leqslant l
\tag{58}
$$

$$
\sum_{n=0}^{\infty} \int_{-\infty}^{\infty} \frac{1}{s}\left[d_{3}(s) a_{n} G_{n} J_{n+1}(s l)+d_{4}(s) b_{n} G_{n} J_{n+1}(s l)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s=0, \quad-l \leqslant x \leqslant l
\tag{59}
$$

The multi-valued functions $\lambda_{1}, \lambda_{2}, \lambda_{3}$ and $\lambda_{4}$, have branch points. We choose the branches such that $\operatorname{Re}(\lambda_{1}) \geqslant 0, \operatorname{Re}(\lambda_{2}) \geqslant 0, \operatorname{Re}(\lambda_{3}) \leqslant 0$ and $\operatorname{Re}(\lambda_{4}) \leqslant 0$ on the path of integration. For a large $s$, the integrands of Eqs. (58) and (59) almost all decrease exponentially. So the semi-infinite integral in Eqs. (58) and (59) can be evaluated numerically. The semi-infinite integral in Eqs. (58) and (59) can be evaluated directly. Eqs. (58) and (59) can now be solved for the coefficients $a_{n}$ and $b_{n}$ by the Schmidt method [35,36]. For briefly, Eqs. (58) and (59) can be rewritten as

$$
\sum_{n=0}^{\infty} a_{n} E_{n}^{*}(x)+\sum_{n=0}^{\infty} b_{n} F_{n}^{*}(x)=U_{0}(x), \quad-l \leqslant x \leqslant l
\tag{60}
$$

$$
\sum_{n=0}^{\infty} a_{n} G_{n}^{*}(x)+\sum_{n=0}^{\infty} b_{n} H_{n}^{*}(x)=0, \quad-l \leqslant x \leqslant l
\tag{61}
$$

where $E_{n}^{*}(x), F_{n}^{*}(x), G_{n}^{*}(x)$ and $H_{n}^{*}(x)$ and $U_{0}(x)$ are known functions, i.e., $E_{n}^{*}(x)=\frac{\mu_{0} \mathrm{e}^{\mathrm{i} x}}{2 \pi(k-1)} \int_{-\infty}^{\infty} \frac{1}{s} d_{1}(s) G_{n} J_{n+1}(s l) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s$, $F_{n}^{*}(x)=\frac{\mu_{0} \mathrm{e}^{\mathrm{i} x}}{2 \pi(k-1)} \int_{-\infty}^{\infty} \frac{1}{s} d_{2}(s) G_{n} J_{n+1}(s l) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s$, $G_{n}^{*}(x)=\int_{-\infty}^{\infty} \frac{1}{s} d_{3}(s) G_{n} J_{n+1}(s l) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s$, $H_{n}^{*}(x)=\int_{-\infty}^{\infty} \frac{1}{s} d_{4}(s) G_{n} J_{n+1}(s l) \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s$, $U_{0}(x)=-\tau_{0}(x)$. $a_{n}$ and $b_{n}$ are unknown coefficients. From Eq. (61), it can be obtained:

$$
\sum_{n=0}^{\infty} b_{n} H_{n}^{*}(x)=-\sum_{n=0}^{\infty} a_{n} G_{n}^{*}(x)
\tag{62}
$$

It can now be solved for the coefficients $b_{n}$ using the Schmidt method. Here the form $-\sum_{n=0}^{\infty} a_{n} G_{n}^{*}(x)$ can be considered as a known function temporarily. A set of functions $P_{n}(x)$, which satisfy the orthogonality condition

$$
\int_{-l}^{l} P_{m}(x) P_{n}(x) \mathrm{d} x=N_{n} \delta_{m n}, \quad N_{n}=\int_{-l}^{l} P_{n}^{2}(x) \mathrm{d} x
\tag{63}
$$

can be constructed from the function, $H_{n}^{*}(x)$, such that

$$
P_{n}(x)=\sum_{i=0}^{n} \frac{M_{i n}}{M_{n n}} H_{i}^{*}(x)
\tag{64}
$$

where $M_{i j}$ is the cofactor of the element $d_{i j}$ of $D_{n}$, which is defined as

$$
D_{n}=\left[\begin{array}{c}
d_{00}, d_{01}, d_{02}, \ldots, d_{0 n} \\
d_{10}, d_{11}, d_{12}, \ldots, d_{1 n} \\
d_{20}, d_{21}, d_{22}, \ldots, d_{2 n} \\
\cdots \cdots \cdots \cdots \cdots \\
\cdots \cdots \cdots \cdots \cdots \\
\cdots \cdots \cdots \cdots \cdots \\
d_{n 0}, d_{n 1}, d_{n 2}, \ldots, d_{n n}
\end{array}\right], \quad d_{i j}=\int_{-l}^{l} H_{i}^{*}(x) H_{j}^{*}(x) \mathrm{d} x
$$

Using Eqs. (62)-(65), we obtain

$$
b_{n}=\sum_{j=n}^{\infty} q_{j} \frac{M_{n j}}{M_{j j}} \quad \text { with } q_{j}=-\sum_{i=0}^{\infty} a_{i} \frac{1}{N_{j}} \int_{-l}^{l} G_{i}^{*}(x) P_{j}(x) \mathrm{d} x
$$

Hence, it can be rewritten

$$
b_{n}=\sum_{i=0}^{\infty} a_{i} K_{i n}^{*}, \quad K_{i n}^{*}=-\sum_{j=n}^{\infty} \frac{M_{n j}}{N_{j} M_{j j}} \int_{-l}^{l} G_{i}^{*}(x) P_{j}(x) \mathrm{d} x
$$

Substituting Eq. (67) into Eq. (60), it can be obtained

$$
\sum_{n=0}^{\infty} a_{n} Y_{n}^{*}(x)=U_{0}(x), \quad Y_{n}^{*}(x)=E_{n}^{*}(x)+\sum_{i=0}^{\infty} K_{n i}^{*} F_{i}^{*}(x)
$$

Hence, it can now be solved for the coefficients $a_{n}$ by the Schmidt method again as mentioned above. With the aid of Eq. (66), the coefficients $b_{n}$ can be obtained.

## 6. Numerical calculations and discussion

The coefficients $a_{n}$ and $b_{n}$ are known, so that the whole stress field can be obtained. However, from the viewpoint of fracture, it is important to determine stresses $\tau_{y y}^{(1)}$ and $\tau_{x y}^{(1)}$ in the vicinity of crack tips. In the case of the present study, $\tau_{y y}^{(1)}$ and $\tau_{x y}^{(1)}$ along the crack line can be expressed as

$$
\tau_{y y}=\tau_{y y}^{(1)}(x, 0)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi(k-1)} \sum_{n=0}^{\infty} \int_{-\infty}^{\infty} \frac{1}{s}\left[d_{1}(s) a_{n} G_{n} J_{n+1}(s l)+d_{2}(s) b_{n} G_{n} J_{n+1}(s l)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
$$

$$
\tau_{x y}=\tau_{x y}^{(1)}(x, 0)=\frac{\mu_{0} \mathrm{e}^{\gamma x}}{2 \pi} \sum_{n=0}^{\infty} \int_{-\infty}^{\infty} \frac{1}{s}\left[d_{3}(s) a_{n} G_{n} J_{n+1}(s l)+d_{4}(s) b_{n} G_{n} J_{n+1}(s l)\right] \mathrm{e}^{\mathrm{i} s x} \mathrm{~d} s
$$

From Refs. [39,40], it can be seen that the Schmidt method is performed satisfactorily if the first ten terms of infinite series in Eqs. (69) and (70) are retained. At $-l \leqslant x \leqslant l, y=0$, it can be obtained that $\tau_{y y}^{(1)} / \tau_{0}$ is very close to negative unity. Hence, the solution of this paper can also be proved to satisfy the boundary conditions (1). The material constants of the functionally graded materials are assumed as $\mu_{0}=77.0\left(\times 10^{9} \mathrm{~N} / \mathrm{m}^{2}\right)$ and $v=0.28$, respectively.

The crack surface loading $-\tau_{0}(x)$ will simply be assumed to be a polynomial of the form as follows (The properties of the materials are non-symmetric about $y$-axis for $\gamma \neq 0.0$, so the stress loading on the crack surfaces should be also non-symmetric about $y$-axis for $\gamma \neq 0.0$.):

$$
-\tau_{0}(x)=-p_{0}-p_{1}\left(\frac{x}{l}\right)-p_{2}\left(\frac{x}{l}\right)^{2}-p_{3}\left(\frac{x}{l}\right)^{3}
$$

Since the problem is linear, the results can be superimposed in any suitable manner. The results are obtained by taking only one of the four input parameters $p_{0}, p_{1}, p_{2}$ and $p_{3}$ non-zero at a time. The normalized non-homogeneity constant $\gamma l$ is varied between -2.8 and 2.8 , which covers most of the practical cases. The results of this paper are shown in Figs. 2-12. From the results, the following observations are very significant:

![](./images/811985670590431234_4.jpg)

Fig. 2. The stress along the crack line versusxfor $\lambda l=1.0$ for $a/\beta l=0.001$ and $l=1.0$ under the loading $\tau_{0}(x)=p_{0}$.

![](./images/811985670590431234_5.jpg)

Fig. 3. The stress at the crack tips versus $a/\beta l$ for $l=1.0$ and $\gamma l=0.4$ under the loading $\tau_{0}(x)=p_{0}$.

![](./images/811985670590431234_6.jpg)

Fig. 4. The stress at the crack tips versus $\gamma l$ for $l=1.0$ and $a/\beta l=0.002$ under the loading $\tau_{0}(x)=p_{0}$.

![](./images/811985670590431234_7.jpg)

Fig. 5. The stress at the crack tips versus $l$ for $\gamma l=0.4$ and $a/\beta l=0.002$ under the loading $\tau_{0}(x)=p_{0}$.

(i) The problem of the present paper is different from one as shown in Refs. [33,34]. The mode-I crack fracture problem is studied in the present paper. However, the problems in Refs. [33,34] are for the anti-plane shear fracture problem. The solving processes of the problems in Refs. [33,34] are also quite simply compared to with one of the present paper. The aim of this paper is also just to use the non-local theory

![](./images/811985670590431234_8.jpg)

Fig. 6. The stress at the crack tips versus $\eta$ for $a/\beta l=0.002$, $l=1.0$ and $\gamma l=0.4$ under the loading $\tau_0(x)=p_0$.

![](./images/811985670590431234_9.jpg)

Fig. 7. The stress at the crack tips versus $a/\beta l$ for $l=1.0$ and $\gamma l=0.4$ under the loading $\tau_0(x)=p_1x/l$.

![](./images/811985670590431234_10.jpg)

Fig. 8. The stress at the crack tips versus $\gamma l$ for $l=1.0$ and $a/\beta l=0.002$ under the loading $\tau_0(x)=p_1x/l$.

![](./images/811985670590431234_11.jpg)

Fig. 9. The stress at the crack tips versus $a/\beta l$ for $l=1.0$ and $\gamma l=0.4$ under the loading $\tau_0(x)=p_2(x/l)^2$.

to solve the fracture problem in the functionally graded materials. The traditional concepts of the non-
local theory are extended to solve the mode-I crack fracture problem in the functionally graded
materials.

![](./images/811985670590431234_12.jpg)

Fig. 10. The stress at the crack tips versus $\gamma l$ for $l=1.0$ and $a/\beta l=0.002$ under the loading $\tau_{0}(x)=p_{2}(x/l)^{2}$.

![](./images/811985670590431234_13.jpg)

Fig. 11. The stress at the crack tips versus $a/\beta l$ for $l=1.0$ and $\gamma l=0.4$ under the loading $\tau_{0}(x)=p_{3}(x/l)^{3}$.

![](./images/811985670590431234_14.jpg)

Fig. 12. The stress at the crack tips versus $\gamma l$ for $l=1.0$ and $a/\beta l=0.002$ under the loading $\tau_{0}(x)=p_{3}(x/l)^{3}$.

(ii) For $a/\beta l\neq0$, it can be proved that the semi-infinite integration and the series in Eqs. (69) and (70) are convergent for any variable $x$ because the integrands of Eqs. (69) and (70) almost all decrease exponen- tially as shown in the forms of $d_{i}(s)$ $(i=1,2,3,4)$. So the stresses give finite values all along the crack line as shown in Fig. 2. Contrary to the classical theory solution, it is found that no stress singularities are present at crack tips, and also the present results converge to the classical ones when far away from crack tips. The non-local elastic solutions yield a finite stress at crack tips, thus allowing us to use the maximum stress as a fracture criterion. The maximum stress does not occur at crack tips, but slightly away from crack tips. This phenomenon has been thoroughly substantiated in Ref. [41]. The distance between the crack tip and the maximum stress point is very small, and it depends on the crack length, the lattice parameter and the parameter describing the functionally graded materials.

(iii) The stresses at the crack tips become infinite as the lattice parameter $a\rightarrow0$. This is the classical contin- uum limit of square root singularity. This can be shown from Eqs. (58) and (59). For $a\rightarrow0$, $d_{i}(s)/s=c_{i}$ $(c_{i}$ $(i=1,2,3,4)$ are constants), Eqs. (58) and (59) will reduce to a dual integral equation for the same problem in the classical functionally graded materials. The dual integral equation can be solved by using the singular integral equation for the same problem in the local functionally graded materials problem. However, the stress singularities are present at crack tips in the local functionally graded materials prob- lem as well known.

(iv) The stress of $\tau_{yy}$ does not depend on the shear modulus $\mu_{0}$ as shown in Eqs. (58), (59) and Eqs. (69), (70). However, the stress of $\tau_{yy}$ depends on the crack length, the parameter describing the functionally graded materials and the lattice parameter of the materials. This is the same as the fracture problem in the isotropic homogeneous materials. Other, the shear stress $\tau_{xy}$ is very small. It is omitted in the figure.

(v) For the symmetric loading, the effect of the lattice parameter of functionally graded materials on the stress fields at crack tips decreases with the increase of the lattice parameter as shown in as shown in Figs. 3 and 9. For the anti-symmetric loading, as shown in Figs. 7 and 11, the effect of the lattice parameter of functionally graded materials on the stress field at the crack right tip decreases with the increase of the lattice parameter. However, the absolute value of the stress field at the crack left tip decreases with the increase of the lattice parameter. Simultaneously, for the non-local solution, the more smaller the lattice parameter is, the more closer to the classical solution.

(vi) For the symmetric loading, as shown in Figs. 4 and 10, the value of the stress field at crack left tip decreases with the increase of $\gamma l$. However, the value of the stress field at crack right tip increases with the increase of $\gamma l$. The change tendencies of these stress fields are quite opposite. For the anti-symmetric loading, as shown in Figs. 8 and 12, the value of the stress field at crack left tip is a negative value because the loading is negative, and the value of the stress field at crack right tip is a positive value because the loading is negative in this case. The value of the stress field at crack right tip increases with the increase of $\gamma l$ for $\gamma l \leqslant 0$, then it decreases for $\gamma l > 0$. However, the value of the stress field at crack left tip decreases with the increase of $\gamma l$ for $\gamma l \leqslant 0$, then it increases for $\gamma l > 0$.

(vii) As shown in Fig. 6, the variation of the Poisson's ratio $v$ within a practical range has the rather insignificant influence on the stress value near crack tips as discussed in Refs. [1-3].

(viii) For the symmetric loading, the values of the stress fields at the crack tip almost linearly increase with the increase of the crack length as shown in Fig. 5. This is similar with results of the classical theory.

## 7. Conclusion

In the present paper, the traditional concepts of the non-local theory are firstly extended to solve the mode-I fracture problem of functionally graded materials, in which the shear modulus varies exponentially with coordinate parallel to the crack. As expected, the solution in this paper does not contain the stress singularities at crack tips. It can be obtained that the solution of the present paper yields a finite stress at crack tips, thus allows us to use the maximum stress as a fracture criterion.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (10572043), the Natural Science Foundation with Excellent Young Investigators of Hei Long Jiang Province (JC04-08), the National Science Foundation with Excellent Young Investigators of China (10325208) and the National Natural Science Key Item Foundation of China (10432030).

## Appendix

The known functions $e_{ij}(s)$ and $c_{ij}(s)$ ($i=1,2,j=1,2$) can be expressed as follows:

$$
[X_{1}] = \begin{bmatrix}
1 & 1 \\
m_{1}(s) & m_{2}(s)
\end{bmatrix}, \quad [X_{2}] = \begin{bmatrix}
1 & 1 \\
m_{3}(s) & m_{4}(s)
\end{bmatrix}, \quad [X_{3}] = \begin{bmatrix}
g_{1}(s) & g_{2}(s) \\
h_{1}(s) & h_{2}(s)
\end{bmatrix}
$$

$$
[X_{4}] = \begin{bmatrix}
g_{3}(s) & g_{4}(s) \\
h_{3}(s) & h_{4}(s)
\end{bmatrix}, \quad [X_{5}] = [X_{1}] - [X_{2}][X_{4}]^{-1}[X_{3}]\begin{bmatrix}
e_{11}(s) & e_{12}(s) \\
e_{21}(s) & e_{22}(s)
\end{bmatrix} = [X_{5}]^{-1},
$$

$$
[X_{6}] = [X_{4}]^{-1}[X_{3}][X_{5}]^{-1} = \begin{bmatrix}
c_{11}(s) & c_{12}(s) \\
c_{21}(s) & c_{22}(s)
\end{bmatrix}
$$

### References

[1] F. Delale, F. Erdogan, On the mechanical modeling of the interfacial region in bonded half-planes, ASME Journal of Applied Mechanics 55 (1988) 317-324.

[2] Y.F. Chen, Interface crack in nonhomogeneous bonded materials of finite thickness, Ph.D. Dissertation, Lehigh University, 1990.

[3] M. Ozturk, F. Erdogan, Axisymmetric crack problem in bonded materials with a graded interfacial region, International Journal of Solids and Structures 33 (1996) 193-219.

[4] Z.H. Jin, R.C. Batra, Interface cracking between functionally graded coating and a substrate under antiplane shear, International Journal of Engineering Science 34 (1996) 1705-1716.

[5] G. Bao, H. Cai, Delamination cracking in functionally graded coating/metal substrate systems, ACTA Materialia 45 (1997) 1055-1066.

[6] N.I. Shbeeb, W.K. Binienda, Analysis of an interface crack for a functionally graded strip sandwiched between two homogeneous layers of finite thickness, Engineering Fracture Mechanics 64 (1999) 693-720.

[7] B.L. Wang, J.C. Han, S.Y. Du, Crack problem for non-homogeneous composite materials subjected to dynamic loading, International Journal of Solids and Structures 37 (2000) 1251-1274.

[8] P.R. Marur, H.V. Tippur, Evaluation of mechanical properties of functionally graded materials, Journal of Testing and Evaluation 26 (1998) 539-545.

[9] R.J. Butcher, C.E. Rousseau, H.V. Tippur, A functionally graded particulate composite: preparation, measurements and failure analysis, ACTA Materialia 47 (1999) 259-268.

[10] C.E. Rousseau, H.V. Tippur, Compositionally graded materials with cracks normal to the elastic gradient, ACTA Materialia 48 (2000) 4021-4033.

[11] P. Gu, M. Dao, R.J. Asaro, A simplified method for calculating the crack tip field of functionally graded materials using the domain integral, Journal of Applied Mechanics 66 (1999) 101-108.

[12] G. Anlas, M.H. Santare, J. Lambros, Numerical calculation of stress intensity factors in functionally graded materials, International Journal of Fracture 104 (2000) 131-143.

[13] F. Erdogan, H.B. Wu, Crack problems in FGM layer under thermal stress, Journal of Thermal Stress 19 (1996) 237-265.

[14] Y.F. Chen, F. Erdogan, The interface crack problem for a nonhomogeneous coating bonded to a homogeneous substrate, Journal of Mechanics and Physics of Solids 44 (5) (1996) 771-787.

[15] J.R. Rice, A path independent integral and the approximate analysis of strain concentrations by notches and cracks, Journal of Applied Mechanics 35 (1968) 379-386.

[16] Z.C. Xia, J.W. Hutchinson, Crack tip fields in strain gradient plasticity, Journal of Mechanics and Physics of Solids 44 (1996) 1621-1648.

[17] A.C. Eringen, Linear crack subject to shear, International Journal of Fracture 14 (1978) 367-379.

[18] A.C. Eringen, Linear crack subject to anti-plane shear, Engineering Fracture Mechanics 12 (1979) 211-219.

[19] A.C. Eringen, C.G. Speziale, B.S. Kim, Crack tip problem in non-local elasticity, Journal of Mechanics and Physics of Solids 25 (1977) 339-346.

[20] D.G.B. Edelen, Non-local field theory, in: A.C. Eringen (Ed.), Continuum Physics, vol. 4, Academic Press, New York, 1976, pp. 75-204.

[21] A.E. Green, R.S. Rivilin, Multipolar continuum mechanics: functional theory I, Proceeding of The Royal Society of London A 284 (1965) 303-315.

[22] A.C. Eringen, Non-local polar field theory, in: A.C. Eringen (Ed.), Continuum Physics, vol. 4, Academic Press, New York, 1976, pp. 205-267.

[23] K.L. Pan, The image force on a dislocation near an elliptic hole in non-local elasticity, Archive of Applied Mechanics 62 (1992) 557-564.

[24] K.L. Pan, The image force theorem for a screw dislocation near a crack in non-local elasticity, Journal of Applied Physics 27 (1994) 344-346.

[25] K.L. Pan, J. Fang, Non-local interaction of dislocation with a crack, Archive of Applied Mechanics 64 (1993) 44-51.

[26] K.L. Pan, Interaction of a dislocation with a surface crack in non-local elasticity, International Journal of Fracture 69 (1995) 307-318.

[27] A.C. Eringen, B.S. Kim, On the problem of crack in non-local elasticity, in: P. Thoft-Christensen (Ed.), Continuum Mechanics Aspects of Geodynamics and Rock Fracture Mechanics, Reidel, Dordrecht, Holland, 1974, pp. 81-113.

[28] A.C. Eringen, B.S. Kim, Relation between non-local elasticity and lattice dynamics, Crystal Lattice Defects 7 (1977) 51-57.

[29] Z.G. Zhou, J.C. Han, S.Y. Du, Investigation of a Griffith crack subject to anti-plane shear by using the non-local theory, International Journal of Solids and Structures 36 (1999) 3891-3901.

[30] Z.G. Zhou, Y.P. Shen, Investigation of the scattering of harmonic shear waves by two collinear cracks using the non-local theory, Acta Mechanica 135 (1999) 169-179.

[31] Z.G. Zhou, B. Wang, S.Y. Du, Investigation of anti-plane shear behavior of two collinear permeable cracks in a piezoelectric material by using the non-local theory, Journal of Applied Mechanics 69 (2003) 388-390.

[32] Z.G. Zhou, B. Wang, Investigation of anti-plane shear behavior of two collinear impermeable cracks in the piezoelectric materials by using the non-local theory, International Journal of Solids and Structures 39 (2003) 1731-1742.

[33] Z.G. Zhou, B. Wang, Non-local theory solution of two collinear cracks in the functionally graded materials, International Journal of Solids and Structures 43 (5) (2006) 887-898.

[34] Z.G. Zhou, B. Wang, The nonlocal theory solution for two collinear cracks in functionally graded materials subjected to the harmonic elastic anti-plane shear wave, Structural Engineering and Mechanics 23 (1) (2006) 63–74.

[35] P.M. Morse, H. Feshbach, Methods of Theoretical Physics, McGraw-Hill, New York, 1958, pp. 926–1010.

[36] W.F. Yan, Axisymmetric slipless indentation of an infinite elastic cylinder, SIAM Journal of Applied Mathematics 15 (1967) 219–227.

[37] I.S. Gradshtyn, I.M. Ryzhik, Table of Integrals, Series and Products, Academic Press, New York, 1980, p. 480.

[38] A. Erdelyi, Tables of Integral Transforms, vol. 1, McGraw-Hill, New York, 1954.

[39] S. Itou, Three dimensional waves propagation in a cracked elastic solid, Journal of Applied Mechanics 45 (1978) 807–811.

[40] Z.G. Zhou, Y.Y. Bai, X.W. Zhang, Two collinear Griffith cracks subjected to uniform tension in infinitely long strip, International Journal of Solids and Structures 36 (1999) 5597–5609.

[41] A.C. Eringen, Interaction of a dislocation with a crack, Journal of Applied Physics 54 (1983) 6811–6817.