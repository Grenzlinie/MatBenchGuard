Accepted Manuscript

Mixed Mode cracks in annular planes of cylindrical orthotropy subjected to inplane loading

H. Goleij, R.T. Faal, A.R. Fotuhi

<table>
  <tr>
    <td>PII:</td>
    <td>S0167-8442(17)30211-2</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.tafmec.2017.06.011</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>TAFMEC 1893</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Theoretical and Applied Fracture Mechanics</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>25 April 2017</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>7 June 2017</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>12 June 2017</td>
  </tr>
</table>

![](./images/813128915533955072_1.jpg)

Please cite this article as: H. Goleij, R.T. Faal, A.R. Fotuhi, Mixed Mode cracks in annular planes of cylindrical orthotropy subjected to inplane loading, *Theoretical and Applied Fracture Mechanics* (2017), doi: http://dx.doi.org/10.1016/j.tafmec.2017.06.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Mixed Mode cracks in annular planes of cylindrical orthotropy subjected to inplane loading

H. Goleij, R. T. Faal¹

Faculty of Engineering, University of Zanjan, P. O. Box 45195-313, Zanjan, Iran

A. R. Fotuhi

Department of Mechanical Engineering, Yazd University, Yazd, Iran

**Abstract:** This paper is concerned with the mixed mode crack problem in an orthotropic annular plane. First, the Michell solution is generalized for material of cylindrical anisotropy. Next by using this solution, fundamental solutions of climb and glide edge dislocations are provided for an annular orthotropic plane of cylindrical orthotropy. Then, an analytical solution to stress field of the intact annular plane under normal and shear tractions on its outer boundaries is presented in this article. The distributed dislocation technique is employed to analyze multiple arbitrary oriented interacting cracks in an annular orthotropic plane. The ensuing integral equations are solved numerically to obtain the dislocation density on the surfaces of the cracks. The stress intensity factors are evaluated by using these dislocation densities. The approach of this study is applied to example problems and shown to be accurate for cases where given in the literature. Finally, the effects of crack geometry and location, material anisotropy, and interaction of cracks on the resulting stress intensity factors at the crack tips are studied.

**Keywords:** Annular plane, Volterra dislocation, Dislocation density, Generalized Michell solution.

## 1. Introduction

---
¹Corresponding author. Tel.: +98 241 515 2600; Fax: +98 241 515 2762.
E-mail address: faal92@yahoo.com (R.T. Faal)

### Nomenclature:

$E_{1}, E_{2}, E_{3}, v_{12}, v_{21}, v_{23}, v_{32}, v_{13}, v_{31}, G_{12}, G_{13}, G_{23}$
material constants

$\epsilon_{rr}, \epsilon_{\theta \theta}, \epsilon_{r \theta}, \epsilon_{zz}, \gamma_{\theta z}, \gamma_{rz}$
strain components in polar coordinates

$\sigma_{rr}, \sigma_{\theta \theta}, \sigma_{r \theta}, \sigma_{zz}, \sigma_{rz}, \sigma_{\theta z}$
stress components in polar coordinates

$\varphi$
Airy stress function

$\alpha, \beta$
pre-defined material property ratios

$(r, \theta)$
polar coordinates

$\rho, \delta$
constants defined in terms of $\alpha$ and $\beta$

$a_{0}, a_{1}, a_{2}, a_{3}, b_{0}, b_{1}, b_{2}, b_{3}, A_{1}, A_{2}, A_{3}, A_{4}$,
$B_{1}, B_{2}, B_{3}, B_{4}, a_{1n}, a_{2n}, a_{3n}, a_{4n}, b_{1n}, b_{2n}, b_{3n}, b_{4n}$
coefficients of Michell solution

$R_{1}, R_{2}$
inner and outer radii of annular plane

$b_{\theta}$
Volterra-type climb dislocation Burgers vector

$b_{r}$
Volterra-type glide dislocation Burgers vector

$H(.)$
Heaviside step-function

$u_{r}, u_{\theta}$
displacement components

$(r', \theta')$
local coordinates specifying dislocation singularity

$G$
shear modulus of an isotropic plane

$v$
Poison's ratio of an isotropic plane

$A_{n}(a), B_{n}(a), C_{n}(a), D_{n}(a)$,
$\bar{A}_{n}(a), \bar{B}_{n}(a), \bar{C}_{n}(a), \bar{D}_{n}(a)$
coefficients of Fourier series of dislocation stress field on the inner and outer radii of annular plane

$a$
radius specifying dislocation location

$A_{en}, B_{en}, C_{en}, D_{en}$,
$\bar{A}_{en}, \bar{B}_{en}, \bar{C}_{en}, \bar{D}_{en}$
coefficients of Fourier series of the intact annular plane stress field

$N$
total number of cracks

$N_{1}$
number of embedded cracks

$N_{2}$
number of edge cracks

$(r_{j}(t), \theta_{j}(t))$
parametric equations specifying the crack geometry

$\sigma_{nn}, \sigma_{ns}$
traction on the surface of the $i$-th crack

$\phi_{i}$
an angle between the tangent to the surface of the $i$-th crack and the radial direction $r_{i}$

$k_{1npij}(s, t), k_{2npij}(s, t)$
kernels of the integrals

$u_{sj}^{+}(s)-u_{sj}^{-}(s), u_{nj}^{+}(s)-u_{nj}^{-}(s)$
crack opening displacements

$t_{k}, s_{l}$
collocation points

$a_{11}', a_{12}', a_{16}', a_{26}', a_{22}', a_{66}'$
transformed elastic constants in the local coordinates tangent to the crack line on the crack tip

$\sigma_{01}(\theta), \tau_{01}(\theta)$
external loadings on the inner edge of the annular plane

$\sigma_{02}(\theta), \tau_{02}(\theta)$
external loadings on the outer edge of the annular plane

$k_{Ij}, k_{IIj}$
Mode I and II stress intensity factors

A cylindrically anisotropic material possesses different elastic properties in radial, tangential, and axial directions of the cylindrical coordinates. This kind of anisotropy can be seen in the cylindrical body, such as bamboo, tree trunk and carbon fiber. The metallic forming process, such as extrusion or drawing may produce material with cylindrical anisotropy. Also the filamentary wound composite is a cylindrically orthotropic material on the macroscopic scale. Existence of such a variety of natural or industrial manufactured cylindrical bodies necessitates fracture analysis of them. Especially, for example, the extruded cylinders as a subgroup of the cylindrically anisotropic material are generally vulnerable to cracking. These

cracks may initiate during the manufacturing process or in the course of service life of a cylinder.

Defects in extruded products occur mostly due to friction and non-homogeneous material flow. Three types of defects including extrusion defect, surface cracks and internal cracks are noticeable in extrusion. According to the above-mentioned explanation, the transverse section of such cylindrical bodies can be considered as a cracked orthotropic circular or annular plane. Therefor it is practically important to analysis the mixed Mode cracks including edge and embedded cracks and it can be the best motivation for this work.

Stress analysis of isotropic cracked circular planes and solid or hollow cylinders can be accomplished using a variety of methods including *dislocation distributed technique* [1-8, 10], *complex variable technique* [9, 11-22], *weight function technique* [24-31], *boundary element and finite element techniques* [32-39]. Also stress intensity factor evaluation can also be accomplished using *coefficient load relief factor* [41-42] and Mellin transform technique [43-45], experimental methods [46-48] and other special techniques [49-51]. For the sake of brevity, the review is allocated to the papers dealing with the dislocation distributed technique. In this regard, the stress intensity factor evaluation for a radial crack embedded in a hollow cylinder or ring was done by Delale and Erdogan [1]. The main problem of interest was the Mode I crack problem in which the self-equilibrating arbitrary normal crack surface tractions were the only external loads. In that problem the basic solution was expressed as the sum of a dislocation solution for an infinite plane and the general solution namely Michell solution in polar coordinates.

Using the method of the problem solution explained in the above, the problem of coated thick-walled cylinders with radial cracks has also been studied by Tangs and Erdogan [2] and Xiao-chun and Ren-ji [3]. In the first study, the cylinder was reinforced by an elastic membrane on its inner surface and in the later it was coated on its outer surface.

Problem of cracked disk can also be solved by superposing of the main problem into two sub-problems namely intact and cracked disk as it can be seen in the references [4-7]. For example, stress intensity factors for an internal or edge crack in a circular elastic disk subjected to concentrated or distributed loads were acquired by Xu and Delale [4]. In line with this superposition method, dissimilar disks were studied by Yong [5] and Yong Li [6]. The dissimilar disk consists an inner cracked disk and an outer coating which were bonded perfectly to each other. Yong obtained the stress intensity factors for a radial crack in a dissimilar disk subjected to a uniform crack surface pressure. Similarly, Mode I stress intensity factors of an embedded radial crack in a rotating dissimilar disk (disk-annulus) was obtained by Yong Li [6]. Parallel to the above-mentioned papers, after the superposition of the problem into two sub-problems, the problem of intact disk can be solved using the complex variable technique [6, 7]. This was generally obtained using the Muskhelishvili's complex variable technique [9]. Yong Li [7] analyzed a compound disk or compound cylinder with a radial crack in order to determine the stress intensity factors of the crack tips. The cylinder was subjected to the point loads. Li [8] also evaluated stress intensity factors of a central radial crack in a compound disk subjected to concentrated forces.

In the framework of the fracture mechanics, the Mode II crack problem in a circular ring or a hollow cylinder has also been paid attention. For instance, the problem of a circular ring or a

hollow cylinder with a radial crack under uniform self-equilibrating shear stresses was considered by Leung and Hu [10]. The approach for Mode II crack in this paper was similar to that of Delale and Erdogan [1] for Mode I crack.

The aims of this paper are to extend the literature to multiple arbitrary oriented interacting cracks, instead of being restricted to a single radial crack and single mode, and to solve the mixed mode crack problem in an annular orthotropic plane. It is assumed that the annular plane of cylindrical orthotropy has some embedded and inner and outer edge cracks. To the best of authors' knowledge, the mixed-mode problem of annular orthotropic planes with multiple arbitrary oriented interacting cracks was not investigated before. This task can be accomplished by generalizing the Michell solution for material of cylindrical anisotropy (orthotropic) which can be considered as another novel part of the paper. The generalized Michell solution can play a key role in solving other elasticity problems in orthotropic materials.

First, we generalize the Michell solution for material of cylindrical anisotropy (Section 2.1). Next, we present the analysis of the fundamental climb and glide edge dislocation solution for an annular orthotropic plane of cylindrical orthotropy (Section 2.2). Then, the analytical solution to stress field of the intact annular plane under normal and shear tractions on its outer boundaries are given (Section 3). We employ the dislocation solution to analyze related crack problems in an annular orthotropic plane using distributed dislocation technique (Section 4). Finally, Section 5 presents numerical examples to study the effect of loading, material anisotropy, and interaction of cracks on the resulting stress intensity factors at the crack tips. Section 6 offers concluding remarks.

## 2. Formulation

### 2.1. Generalized Michell solution for material of cylindrical anisotropy (orthotropic)

As it has been mentioned before, the elastic properties of a cylindrical body can be different in radial, tangential, and axial directions. According to the class of elastic symmetry, the cylindrical body may exhibit special type of material anisotropy such as monoclinic anisotropy, cylindrical orthotropy, and transverse isotropy. For cylindrically orthotropic material there are 9 independent material constants. Any transverse section of these cylindrical bodies can be assumed as a circular or annular orthotropic plane.

The geometry of many two-dimensional problems requires the use of polar coordinates. Some of these problems for isotropic materials are solved employing the Airy stress function approach and the governing biharmonic equation which was given in polar coordinates. The general solution to such problems was given by Michell (For example see the reference [52]). We now wish to generalize the Michell solution to a material having cylindrical anisotropy using the field equations developed in polar coordinates. To this end, we consider an orthotropic plane with cylindrical anisotropy. The plane is made of a material having cylindrical anisotropy where the Hooke's laws are

$$
\epsilon_{r r}=\frac{1}{E_{1}} \sigma_{r r}-\frac{\nu_{21}}{E_{2}} \sigma_{\theta \theta}-\frac{\nu_{31}}{E_{3}} \sigma_{z z} \tag{1}
$$

$$
\epsilon_{\theta \theta}=-\frac{\nu_{12}}{E_{1}} \sigma_{r r}+\frac{1}{E_{2}} \sigma_{\theta \theta}-\frac{\nu_{32}}{E_{3}} \sigma_{z z}
$$

$$
\epsilon_{z z}=-\frac{\nu_{13}}{E_{1}} \sigma_{r r}-\frac{\nu_{23}}{E_{2}} \sigma_{\theta \theta}+\frac{1}{E_{3}} \sigma_{z z}
$$

$$\gamma_{\theta z}=\frac{1}{G_{23}} \sigma_{\theta z}, \gamma_{r z}=\frac{1}{G_{13}} \sigma_{r z}, \gamma_{r \theta}=2 \epsilon_{r \theta}=\frac{1}{G_{12}} \sigma_{r \theta}$$

where
$$\frac{v_{23}}{E_{2}}=\frac{v_{32}}{E_{3}}, \frac{v_{21}}{E_{2}}=\frac{v_{12}}{E_{1}}, \frac{v_{31}}{E_{3}}=\frac{v_{13}}{E_{1}}\tag{2}$$

where $E_{1}, E_{2}, E_{3}, v_{12}, v_{21}, v_{23}, v_{32}, v_{13}, v_{31}, G_{12}, G_{13}, G_{23}$ are material constants. The strain-
compatibility relation in plane elasticity is as follows
$$\frac{\partial}{\partial r}\left(2 r \frac{\partial \epsilon_{r \theta}}{\partial \theta}-r^{2} \frac{\partial \epsilon_{\theta \theta}}{\partial r}\right)+r \frac{\partial \epsilon_{r r}}{\partial r}-\frac{\partial^{2} \epsilon_{r r}}{\partial \theta^{2}}=0\tag{3}$$

Substituting relations (1) into the above equation leads to
$$
\begin{aligned}
& \frac{1}{E_{1}}\left(r \frac{\partial \sigma_{r r}}{\partial r}-\frac{\partial^{2} \sigma_{r r}}{\partial \theta^{2}}\right)-\frac{1}{E_{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \sigma_{\theta \theta}}{\partial r}\right)+\frac{v_{12}}{E_{1}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \sigma_{r r}}{\partial r}\right)+\frac{v_{21}}{E_{2}}\left(-r \frac{\partial \sigma_{\theta \theta}}{\partial r}\right. \\
& \left.+\frac{\partial^{2} \sigma_{\theta \theta}}{\partial \theta^{2}}\right)+\frac{v_{32}}{E_{3}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial \sigma_{z z}}{\partial r}\right)-\frac{v_{31}}{E_{3}}\left(r \frac{\partial \sigma_{z z}}{\partial r}-\frac{\partial^{2} \sigma_{z z}}{\partial \theta^{2}}\right)+\frac{1}{G_{12}} \frac{\partial}{\partial r}\left(r \frac{\partial \sigma_{r \theta}}{\partial \theta}\right)=0
\end{aligned}\tag{4}
$$

The stress components in terms of the Airy stress function $\varphi(r, \theta)$ are given by the following relations
$$\sigma_{r r}=\frac{\partial \varphi}{r \partial r}+\frac{\partial^{2} \varphi}{r^{2} \partial \theta^{2}}, \quad \sigma_{\theta \theta}=\frac{\partial^{2} \varphi}{\partial r^{2}}, \quad \sigma_{r \theta}=-\frac{\partial}{\partial r}\left(\frac{\partial \varphi}{r \partial \theta}\right)\tag{5}$$

By considering the state of plane stress $(\sigma_{z z}=0)$ and substituting Eqs. (5) into (4) we arrive at
$$
\begin{aligned}
& r^{2} \frac{\partial^{4} \varphi}{\partial r^{4}}+2 r \frac{\partial^{3} \varphi}{\partial r^{3}}+\alpha\left(\frac{1}{r^{2}} \frac{\partial^{2} \varphi}{\partial \theta^{2}}-\frac{1}{r} \frac{\partial^{3} \varphi}{\partial r \partial \theta^{2}}+\frac{\partial^{4} \varphi}{\partial r^{2} \partial \theta^{2}}\right) \\
& -\beta\left(\frac{\partial^{2} \varphi}{\partial r^{2}}-\frac{1}{r} \frac{\partial \varphi}{\partial r}-\frac{2}{r^{2}} \frac{\partial^{2} \varphi}{\partial \theta^{2}}-\frac{\partial^{4} \varphi}{r^{2} \partial \theta^{4}}\right)=0
\end{aligned}\tag{6}
$$

where $\beta=\frac{E_{2}}{E_{1}}$ and $\alpha=\frac{E_{2}}{G_{12}}-2 \beta v_{12}$. It is worth mentioning that for the state of plane strain $(\varepsilon_{z z}=0)$ we may arrive at $\beta=\frac{E_{2}}{E_{1}}(\frac{1-v_{13} v_{31}}{1-v_{23} v_{32}})$ and $\alpha=\frac{E_{2}}{G_{12}(1-v_{23} v_{32})}-2 \beta(\frac{v_{12}+v_{13} v_{32}}{1-v_{13} v_{31}})$. A separable solution form to the above equation is given as $\varphi(r, \theta)=f(r) e^{b \theta}$. Therefore $f(r)$ is governed by the following equation
$$f^{\prime \prime \prime \prime}+\frac{2}{r} f^{\prime \prime \prime}-\frac{A}{r^{2}} f^{\prime \prime}+\frac{A}{r^{3}} f^{\prime}-\frac{B}{r^{4}} f=0\tag{7}$$

where the coefficients $A$ and $B$ are
$$A=-\alpha b^{2}+\beta, \quad B=-b^{2}\left(\alpha+2 \beta+\beta b^{2}\right)\tag{8}$$

By change of variable as $\xi=lnr$ the above equation is transformed as
$$\frac{\partial^{4} f}{\partial \xi^{4}}-4 \frac{\partial^{3} f}{\partial \xi^{3}}+(5-A) \frac{\partial^{2} f}{\partial \xi^{2}}-2(1-A) \frac{\partial f}{\partial \xi}-B f=0\tag{9}$$

By virtue of Eq. (8), the characteristic equation of the above differential equation can be written in one of the following forms
$$a^{4}-4 a^{3}+\left(5+\alpha b^{2}-\beta\right) a^{2}-2\left(1+\alpha b^{2}-\beta\right) a+b^{2}\left(\alpha+2 \beta+\beta b^{2}\right)=0,\tag{10}$$
$$\beta b^{4}+b^{2}\left(2 \beta+\alpha(1-a)^{2}\right)+a^{4}-4 a^{3}+(5-\beta) a^{2}-2(1-\beta) a=0$$

The above second equation is the same as the first one but it has been sorted as a quadratic equation in terms of $b^{2}$. We present these two types of equations to specify multiple roots for

$a$ and $b$. We should care about multiple roots for $a$ and $b$ because they specify the fundamental solutions. The solution to the second equation of (10) is as follows

$$
b^{2}=\frac{-\left(2 \beta+\alpha(1-a)^{2}\right) \pm|(a-1)| \sqrt{\left(\alpha^{2}-4 \beta\right)(a-1)^{2}+4 \beta(1+\alpha+\beta)}}{2 \beta} \tag{11}
$$

The term $\alpha^{2}-4 \beta=\left(\frac{E_{2}}{E_{1}}\right)^{2}\left[\left(\frac{E_{1}}{G_{12}}-2 v_{12}\right)^{2}-4 \frac{E_{1}}{E_{2}}\right]$ is positive because according to the reference [53] the term $\left(\frac{E_{1}}{G_{12}}-2 v_{12}\right)^{2}-4 \frac{E_{1}}{E_{2}}$ is also positive for most of material with cylindrical orthotropy. One of the repeated values for $b$ is $b=0$ and consequently $a$ should be one of the values $\{0,2,1+\sqrt{\beta}, 1-\sqrt{\beta}\}$. These fundamental solutions lead to the solution containing $1+a_{1} r^{2}+a_{2} r^{\sqrt{\beta}+1}+a_{3} r^{\sqrt{\beta}-1}$ and $\theta(a_{0}+a_{1} r^{2}+a_{2} r^{\sqrt{\beta}+1}+a_{3} r^{\sqrt{\beta}-1})$. Also by setting $\left(\alpha^{2}-4 \beta\right)(a-1)^{2}+4 \beta(1+\alpha+\beta)=0$ we will have $b=\pm \sqrt{\frac{(\alpha+2)(\alpha+2 \beta)}{\alpha^{2}-4 \beta}}$ or $a=1 \pm 2 \sqrt{\frac{\beta(1+\alpha+\beta)}{\alpha^{2}-4 \beta}} i$. This is valid only for $\alpha^{2}-4 \beta>0$ and corresponds to the following solution

$$
\begin{aligned}
& r\left[A_{1} \cos (2 \rho \ln r)+A_{2} \sin (2 \rho \ln r)\right] e^{\delta \theta}+r\left[A_{3} \cos (2 \rho \ln r)+A_{4} \sin (2 \rho \ln r)\right] e^{-\delta \theta} \\
& +r\left[B_{1} \cos (2 \rho \ln r)+B_{2} \sin (2 \rho \ln r)\right] \theta e^{\delta \theta} \\
& +r\left[B_{3} \cos (2 \rho \ln r)+B_{4} \sin (2 \rho \ln r)\right] \theta e^{-\delta \theta}
\end{aligned} \tag{12}
$$

where $\rho=\sqrt{\frac{\beta(1+\alpha+\beta)}{\alpha^{2}-4 \beta}}$ and $\delta=\sqrt{\frac{(\alpha+2)(\alpha+2 \beta)}{\alpha^{2}-4 \beta}}$. For repeated value $a=1$, the repeated values for $b$ are $\pm i$ and the solution forms are

$$
\begin{aligned}
& a_{31} r \cos \theta+b_{31} r \sin \theta+a_{51} r \theta \cos \theta+b_{51} r \theta \sin \theta \\
& +a_{61} r \ln r \theta \cos \theta+b_{61} r \ln r \theta \sin \theta
\end{aligned} \tag{13}
$$

We can have the periodic solution by choosing $b=in$. The solutions to the above equation are easily given in the form of $f=e^{(1+d_{j n}) \xi}=r^{1+d_{j n}}, j=1,2,3,4$ in which

$$
d_{1 n}=-d_{2 n}=\sqrt{\mu_{n}+\sqrt{\lambda_{n}}}, \quad d_{3 n}=-d_{4 n}=\sqrt{\mu_{n}-\sqrt{\lambda_{n}}} \tag{14}
$$

wherein $1+d_{j n}$ are the roots of the first equation of (10) and $\mu_{n}=\frac{1+A_{n}}{2}$ and $\lambda_{n}=\left(\frac{1-A_{n}}{2}\right)^{2}+B_{n}$ in which $A_{n}=\alpha n^{2}+\beta$ and $B_{n}=n^{2}(\alpha+2 \beta-\beta n^{2})$. It is worth mentioning that for $n=1$, we have $A_{n}=B_{n}$ and then $d_{3 n}=d_{4 n}=0$. Therefore, because of the existence of the repeated roots, the corresponding fundamental solutions to Eq. (9) should be 1 and $\ln r$. It is possible to show that $\mu_{n}, \lambda_{n} \geq 0$ and $(\mu_{n})^{2}-\lambda_{n}=A_{n}-B_{n}=\beta(1-n^{2})^{2} \geq 0$. Hence, $d_{j n}$ are the real constants. The generalized Michell solution as a solution to the Eq. (6) is given by

$$
\begin{aligned}
\varphi & =a_{0}+a_{1} r^{2}+a_{2} r^{\sqrt{\beta}+1}+a_{3} r^{\sqrt{\beta}-1}+\left(b_{0}+b_{1} r^{2}+b_{2} r^{\sqrt{\beta}+1}+b_{3} r^{\sqrt{\beta}-1}\right) \theta \\
+ & r(a_{11} r^{\sqrt{1+\alpha+\beta}}+a_{21} r^{-\sqrt{1+\alpha+\beta}}+a_{31}+a_{41} \ln r+a_{51} \theta+a_{61} \theta \ln r) \cos \theta \\
+ & r(b_{11} r^{\sqrt{1+\alpha+\beta}}+b_{21} r^{-\sqrt{1+\alpha+\beta}}+b_{31}+b_{41} \ln r+b_{51} \theta+b_{61} \theta \ln r) \sin \theta \\
+ & r\{[A_{1} \cos (2 \rho \ln r)+A_{2} \sin (2 \rho \ln r)] e^{\delta \theta} \\
+ & {\left[A_{3} \cos (2 \rho \ln r)+A_{4} \sin (2 \rho \ln r)\right] e^{-\delta \theta\} } \\
+ & r\{[B_{1} \cos (2 \rho \ln r)+B_{2} \sin (2 \rho \ln r)] e^{\delta \theta} \\
+ & {[B_{3} \cos (2 \rho \ln r)+B_{4} \sin (2 \rho \ln r)] e^{-\delta \theta\} \theta} }
\end{aligned} \tag{15}
$$


$$
+r \sum_{n=2}^{\infty}\left(a_{1 n} r^{d_{1 n}}+a_{2 n} r^{d_{2 n}}+a_{3 n} r^{d_{3 n}}+a_{4 n} r^{d_{4 n}}\right) cosn \theta
$$

$$
+r \sum_{n=2}^{\infty}\left(b_{1 n} r^{d_{1 n}}+b_{2 n} r^{d_{2 n}}+b_{3 n} r^{d_{3 n}}+b_{4 n} r^{d_{4 n}}\right) sinn \theta
$$

We also mention that for $\beta=1$ the sum of the first four terms should be replaced by the terms $a_{0}+a_{1} r^{2}+a_{2} r^{2} lnr+a_{3} lnr$ because of the existence of the repeated roots. Furthermore, the next four terms should be replaced by $(b_{0}+b_{1} r^{2}+b_{2} r^{2} lnr+b_{3} lnr) \theta$. Moreover for $\alpha^{2}=4 \beta$ we should remove the terms of the solution (12) from Eq. (15). For isotropic materials i. e. $\beta=1$ and $\alpha=2$, the generalized Michell solution can be validated with that given in reference [52].

### 2.2. Dislocation solution
#### 2.1.1 Climb and glide edge dislocation

Let us consider an annular plane with inner and outer radii $R_{1}$ and $R_{2}$, respectively (Fig. 1). In the cylindrical coordinate a Volterra-type edge dislocation (climb and glide) located at $r=a, \theta=0$, is considered wherein the cut of dislocation is an outward radial ray emanating from $r=a$.

Fig.1. Schematic view of an annular plane with a climb/glide edge dislocation

The boundary conditions along the curved surfaces read as
$$
\begin{aligned}
& \sigma_{r r}\left(R_{i}, \theta\right)=0, i=1,2 \\
& \sigma_{r \theta}\left(R_{i}, \theta\right)=0, i=1,2
\end{aligned}\tag{16}
$$

The condition representing a Volterra-type climb dislocation located at $r=a, \theta=0$ in an annular region with the cut of dislocation in radial direction is
$$
u_{\theta}(r, 0)-u_{\theta}(r, 2 \pi)=b_{\theta} H(r-a)\tag{17}
$$
where, $b_{\theta}$ designates the dislocation Burgers vector and $H($.$) is the Heaviside step-function.$

The condition corresponding to a Volterra-type glide dislocation located at $r=a, \theta=0$ in a ring with the cut of dislocation in radial direction can be written as
$$
u_{r}(r, 0)-u_{r}(r, 2 \pi)=b_{r} H(r-a)\tag{18}
$$
where, $b_{r}$ refers to the dislocation Burgers vector. Moreover, the continuity of traction vector on the cut of the dislocation requires that
$$
\sigma_{\theta \theta}(r, 0)=\sigma_{\theta \theta}(r, 2 \pi), \sigma_{r \theta}(r, 0)=\sigma_{r \theta}(r, 2 \pi)\tag{19}
$$

To solve the relevant dislocation problem, first the problem of an infinite plane of cylindrical orthotropy with the Volterra-type climb and glide edge dislocations is solved. To this end, the Airy stress function approach is used. Solution to the Airy stress function governing biharmonic equation was given in a separable form and was originally credited to Michell in 1899. This solution was used for isotropic materials and a generalization of that, has been given in the previous section for material of cylindrical anisotropy (orthotropic).

The problem of an infinite plane of cylindrical orthotropy with the Volterra-type climb and glide edge dislocations is solved by considering only two terms of the generalized Michell solution $\varphi=a_{41} r lnr cos \theta+b_{41} r lnr sin \theta$. The corresponding stress components can be simply written using the Eq. (5) as follows
$$
\sigma_{r r}=\sigma_{\theta \theta}=a_{41} \frac{cos \theta}{r}+b_{41} \frac{sin \theta}{r}\tag{20}
$$

$$\sigma_{r \theta}=a_{41} \frac{\sin \theta}{r}-b_{41} \frac{\cos \theta}{r}$$

The strain-displacement relations in polar coordinates are as follows

$$\epsilon_{r r}=\frac{\partial u_{r}}{\partial r}, \quad r \epsilon_{\theta \theta}=u_{r}+\frac{\partial u_{\theta}}{\partial \theta}, \quad r \epsilon_{r \theta}=\frac{1}{2}\left(\frac{\partial u_{r}}{\partial \theta}+r \frac{\partial u_{\theta}}{\partial r}-u_{\theta}\right)\tag{21}$$

Solution of displacement in terms of strain components can be found by integrating of the above relations as below

$$u_{r}=\int \epsilon_{r r} d r+f(\theta)\tag{22}$$

$$u_{\theta}=\int r \epsilon_{\theta \theta} d \theta-\iint \epsilon_{r r} d r d \theta-\int f(\theta) d \theta+g(r)$$

wherein the functions $f(\theta)$ and $g(r)$ should satisfy the following relation

$$\begin{aligned}
&2 r \epsilon_{r \theta}=\int \frac{\partial}{\partial \theta} \epsilon_{r r} d r-r \int \epsilon_{r r} d \theta+\iint \epsilon_{r r} d r d \theta+r^{2} \int \frac{\partial}{\partial r} \epsilon_{\theta \theta} d \theta \\
&+\int f(\theta) d \theta+f^{\prime}(\theta)+r g^{\prime}(r)-g(r)
\end{aligned}\tag{23}$$

By considering the state of plane stress $(\sigma_{z z}=0)$, and using Eqs. (1) and (20), as well as the relations $\beta=\frac{E_{2}}{E_{1}}, \frac{v_{21}}{E_{2}}=\frac{v_{12}}{E_{1}}$ and $\alpha=\frac{E_{2}}{G_{12}}-2 \beta v_{12}$, the strain components are obtained as

$$\epsilon_{r r}=\frac{\beta}{E_{2}}\left(1-v_{12}\right) \frac{1}{r}\left(a_{41} \cos \theta+b_{41} \sin \theta\right)\tag{24}$$

$$\epsilon_{\theta \theta}=\frac{1}{E_{2}}\left(1-v_{12} \beta\right) \frac{1}{r}\left(a_{41} \cos \theta+b_{41} \sin \theta\right)$$

$$\epsilon_{r \theta}=\frac{1}{2 E_{2}}\left(\alpha+2 \beta v_{12}\right) \frac{1}{r}\left(a_{41} \sin \theta-b_{41} \cos \theta\right)$$

Substituting the above relations into Eqs. (22) and (23) results in

$$u_{r}=\frac{\beta}{E_{2}}\left(1-v_{12}\right)\left(a_{41} \cos \theta+b_{41} \sin \theta\right) \ln r+f(\theta)\tag{25}$$

$$u_{\theta}=\frac{1}{E_{2}}\left[\left(1-v_{12} \beta\right)-\beta\left(1-v_{12}\right) \ln r\right]\left(a_{41} \sin \theta-b_{41} \cos \theta\right)-\int f(\theta) d \theta+g(r)$$

wherein the functions $f(\theta)$ and $g(r)$ should satisfy the following relation

$$\begin{aligned}
&\frac{1}{E_{2}}(\alpha+\beta+1)\left(a_{41} \sin \theta-b_{41} \cos \theta\right)-\int f(\theta) d \theta-f^{\prime}(\theta)=r g^{\prime}(r)-g(r) \\
&=\text { constant }
\end{aligned}\tag{26}$$

The above equations are solved as follows

$$g(r)=E r+F, \quad f(\theta)=\frac{(\alpha+\beta+1)}{2 E_{2}} \theta\left(a_{41} \sin \theta-b_{41} \cos \theta\right)\tag{27}$$

Viewing Eqs. (20), we conclude that the boundary condition (19) is satisfied. Applying the condition (17) and (18) for the case of $a=0$, to Eq. (25) led to

$$a_{41}=E b_{\theta}, \quad b_{41}=E b_{r}\tag{28}$$

where $E=\frac{E_{2}}{\pi(\alpha+\beta+1)}$. To find solution to the problem of an infinite plane of cylindrical orthotropy with a Volterra-type climb edge dislocation wherein the dislocation cut is starting from $r=a>0$, we consider the local coordinates $(r', \theta')$ (see Fig. 1) and then $r' \cos \theta'=$

$rcos\theta - a$ and $r'sin\theta' = rsin\theta$. The corresponding stress components can be simply written using the Eq. (20) as follows

$$
\sigma_{r'r'}=\sigma_{\theta'\theta'}=E\frac{1}{r'}(b_{\theta}cos\theta'+b_{r}sin\theta') \tag{29}
$$

$$
\sigma_{r'\theta'}=E\frac{1}{r'}(b_{\theta}sin\theta'-b_{r}cos\theta')
$$

The above stress components are transformed to the global coordinates $(r,\theta)$ using the following transformations

$$
\sigma_{rr}=\frac{\sigma_{r'r'}+\sigma_{\theta'\theta'}}{2}+\frac{\sigma_{r'r'}-\sigma_{\theta'\theta'}}{2}cos(2(\theta-\theta'))+\sigma_{r'\theta'}sin(2(\theta-\theta')) \tag{30}
$$

$$
\sigma_{\theta\theta}=\frac{\sigma_{r'r'}+\sigma_{\theta'\theta'}}{2}-\frac{\sigma_{r'r'}-\sigma_{\theta'\theta'}}{2}cos(2(\theta-\theta'))-\sigma_{r'\theta'}sin(2(\theta-\theta'))
$$

$$
\sigma_{r\theta}=-\frac{\sigma_{r'r'}-\sigma_{\theta'\theta'}}{2}sin(2(\theta-\theta'))+\sigma_{r'\theta'}cos(2(\theta-\theta'))
$$

Substituting Eqs. (29) into (30) by virtue of the relations $r'cos\theta'=rcos\theta - a$ and $r'sin\theta' = rsin\theta$ led to

$$
\begin{aligned}
\sigma_{rr} &= Eb_{\theta}\left[\frac{a-rcos\theta}{r^{2}+a^{2}-2arcos\theta}+\frac{2arsin^{2}\theta(r-acos\theta)}{(r^{2}+a^{2}-2arcos\theta)^{2}}\right] \\
&+Eb_{r}\left[\frac{rsin\theta}{r^{2}+a^{2}-2arcos\theta}-\frac{2asin\theta(rcos\theta - a)(acos\theta - r)}{(r^{2}+a^{2}-2arcos\theta)^{2}}\right]
\tag{31}
\end{aligned}
$$

$$
\begin{aligned}
\sigma_{\theta\theta} &= Eb_{\theta}\left[\frac{2arsin^{2}\theta(acos\theta - r)}{(r^{2}+a^{2}-2arcos\theta)^{2}}-\frac{rcos\theta - a}{r^{2}+a^{2}-2arcos\theta}\right] \\
&+Eb_{r}\left[\frac{rsin\theta}{r^{2}+a^{2}-2arcos\theta}+\frac{2asin\theta(rcos\theta - a)(acos\theta - r)}{(r^{2}+a^{2}-2arcos\theta)^{2}}\right]
\end{aligned}
$$

$$
\begin{aligned}
\sigma_{r\theta} &= Eb_{\theta}\left[\frac{2a^{2}rsin^{3}\theta}{(r^{2}+a^{2}-2arcos\theta)^{2}}-\frac{rsin\theta}{r^{2}+a^{2}-2arcos\theta}\right] \\
&-Eb_{r}\left[\frac{(rcos\theta - a)}{r^{2}+a^{2}-2arcos\theta}-\frac{2a^{2}sin^{2}\theta(rcos\theta - a)}{(r^{2}+a^{2}-2arcos\theta)^{2}}\right]
\end{aligned}
$$

For the isotropic material with shear modulus $G$ and Poison's ratio $v$ we have $\beta=1$ and $\alpha=2$ and also $E_{2}=2(1+v)G$. In this case, the above solution for $b_{r}=0,b_{\theta}\neq0$ leads to that given in reference [1] which validates the work. Furthermore for $b_{\theta}=0,b_{r}\neq0$ the above solution yields to that presented in reference [10]. After deriving the solution for an infinite plane of cylindrical orthotropy with the Volterra-type climb and glide edge dislocations, the problem of a ring with a Volterra-type climb edge dislocation is considered. We first combine the infinite plane solution with the ring solution. Accordingly, we first express the normal and shear components of the stress state (31) along the circles $r=R_{1}$ and $r=R_{2}$ in terms of the following Fourier series:

$$
\sigma_{r\theta}(R_{1},\theta)=\frac{E}{a}\left(b_{\theta}\sum_{n=1}^{\infty}A_{n}(a)sin n\theta + b_{r}\sum_{n=1}^{\infty}\bar{A}_{n}(a)cos n\theta\right) \tag{32}
$$

$$
\sigma_{rr}(R_{1},\theta)=\frac{E}{a}\left(b_{\theta}\sum_{n=0}^{\infty}B_{n}(a)cos n\theta + b_{r}\sum_{n=1}^{\infty}\bar{B}_{n}(a)sin n\theta\right)
$$

$$
\sigma_{r\theta}(R_{2},\theta)=\frac{E}{a}\left(b_{\theta}\sum_{n=1}^{\infty}C_{n}(a)sin n\theta + b_{r}\sum_{n=1}^{\infty}\bar{C}_{n}(a)cos n\theta\right)
$$

$$
\sigma_{r r}\left(R_{2}, \theta\right)=\frac{E}{a}\left(b_{\theta} \sum_{n=0}^{\infty} D_{n}(a) \cos n \theta+b_{r} \sum_{n=1}^{\infty} \bar{D}_{n}(a) \sin n \theta\right)
$$

where the coefficients are given here

$$
A_{n}(a)=\frac{1}{2}\left(\frac{R_{1}}{a}\right)^{n}\left(n+(2-n)\left(\frac{a}{R_{1}}\right)^{2}\right) \text { for } n \geq 1, A_{1}(a)=\frac{R_{1}}{2 a} \tag{33}
$$

$$
B_{n}(a)=\frac{1}{2}\left(\frac{R_{1}}{a}\right)^{n}(2-n)\left(1-\left(\frac{a}{R_{1}}\right)^{2}\right) \text { for } n \geq 1, B_{0}(a)=1, B_{1}(a)=\frac{R_{1}}{2 a}
$$

$$
C_{n}(a)=\frac{1}{2}\left(\frac{a}{R_{2}}\right)^{n}\left(\left(\frac{a}{R_{2}}\right)^{2}(n+2)-n\right) \text { for } n \geq 1, C_{1}(a)=\frac{1}{2} \frac{a}{R_{2}}\left(3\left(\frac{a}{R_{2}}\right)^{2}-2\right)
$$

$$
D_{n}(a)=\frac{1}{2}\left(\frac{a}{R_{2}}\right)^{n}\left(\left(\left(\frac{a}{R_{2}}\right)^{2}-1\right)(n+2) \text { for } n \geq 1,\right.
$$

$$
D_{0}(a)=\left(\frac{a}{R_{2}}\right)^{2}, D_{1}(a)=\frac{1}{2} \frac{a}{R_{2}}\left(3\left(\frac{a}{R_{2}}\right)^{2}-2\right)
$$

$$
\bar{A}_{n}(a)=\frac{1}{2}\left(\frac{R_{1}}{a}\right)^{n}\left(\left(\frac{a}{R_{1}}\right)^{2}-1\right) n \text { for } n \geq 1, \bar{A}_{1}(a)=-\frac{R_{1}}{2 a}
$$

$$
\bar{B}_{n}(a)=\frac{1}{2}\left(\frac{R_{1}}{a}\right)^{n}\left(\left(\frac{a}{R_{1}}\right)^{2} n+(2-n)\right) \text { for } n \geq 1, \bar{B}_{1}(a)=\frac{1}{2} \frac{R_{1}}{a}
$$

$$
\bar{C}_{n}(a)=\frac{1}{2}\left(\frac{a}{R_{2}}\right)^{n}\left(\left(\frac{a}{R_{2}}\right)^{2}-1\right) n \text { for } n \geq 1, \bar{C}_{1}(a)=\frac{1}{2} \frac{a}{R_{2}}\left(\left(\frac{a}{R_{2}}\right)^{2}-2\right)
$$

$$
\bar{D}_{n}(a)=\frac{1}{2}\left(\frac{a}{R_{2}}\right)^{n}\left(\left(\frac{a}{R_{2}}\right)^{2} n-(n+2)\right) \text { for } n \geq 1, \bar{D}_{1}(a)=\frac{1}{2} \frac{a}{R_{2}}\left(2-\left(\frac{a}{R_{2}}\right)^{2}\right)
$$

We choose the following Michell's solution such that the condition (19) to be satisfied by the relevant stress components.

$$
\begin{aligned}
\varphi= & a_{2} r^{\sqrt{\beta}+1}+a_{3} r^{\sqrt{\beta}-1}+r\left(a_{11} r^{\sqrt{1+\alpha+\beta}}+a_{21} r^{-\sqrt{1+\alpha+\beta}}+a_{31}+a_{41} l n r\right) \cos \theta \\
+ & r \sum_{n=2}^{\infty}\left(a_{1 n} r^{d_{1 n}}+a_{2 n} r^{d_{2 n}}+a_{3 n} r^{d_{3 n}}+a_{4 n} r^{d_{4 n}}\right) \cos n \theta \\
+ & r\left(b_{11} r^{\sqrt{1+\alpha+\beta}}+b_{21} r^{-\sqrt{1+\alpha+\beta}}+b_{31}+b_{41} l n r\right) \sin \theta \\
+ & r \sum_{n=2}^{\infty}\left(b_{1 n} r^{d_{1 n}}+b_{2 n} r^{d_{2 n}}+b_{3 n} r^{d_{3 n}}+b_{4 n} r^{d_{4 n}}\right) \sin n \theta
\end{aligned} \tag{34}
$$

The relevant stress components are attained by use of Eqs. (5) as below

$$
\begin{aligned}
\sigma_{r r}(r, \theta) & =e_{2} r^{\sqrt{\beta}-1}+e_{3} r^{\sqrt{\beta}-3}+\frac{1}{r}\left(e_{11} r^{\sqrt{1+\alpha+\beta}}-e_{21} r^{-\sqrt{1+\alpha+\beta}}\right) \cos \theta \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{a_{1 n}\left(1+d_{1 n}-n^{2}\right) r^{d_{1 n}}+a_{2 n}\left(1+d_{2 n}-n^{2}\right) r^{d_{2 n}}\right. \\
& \left.+a_{3 n}\left(1+d_{3 n}-n^{2}\right) r^{d_{3 n}}+a_{4 n}\left(1+d_{4 n}-n^{2}\right) r^{d_{4 n}}\right\} \cos n \theta \\
& +\frac{1}{r}\left(f_{11} r^{\sqrt{1+\alpha+\beta}}-f_{21} r^{-\sqrt{1+\alpha+\beta}}\right) \sin \theta \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{b_{1 n}\left(1+d_{1 n}-n^{2}\right) r^{d_{1 n}}+b_{2 n}\left(1+d_{2 n}-n^{2}\right) r^{d_{2 n}}\right. \\
& \left.+b_{3 n}\left(1+d_{3 n}-n^{2}\right) r^{d_{3 n}}+b_{4 n}\left(1+d_{4 n}-n^{2}\right) r^{d_{4 n}}\right\} \sin n \theta
\end{aligned} \tag{35}
$$

$$
\begin{aligned}
\sigma_{\theta \theta}(r, \theta) & =e_{2} \sqrt{\beta} r^{\sqrt{\beta}-1}+e_{3}(\sqrt{\beta}-2) r^{\sqrt{\beta}-3}+\frac{1}{r}\left[e_{11}(\sqrt{1+\alpha+\beta}+1) r^{\sqrt{1+\alpha+\beta}}\right. \\
& \left.-e_{21}(1-\sqrt{1+\alpha+\beta}) r^{-\sqrt{1+\alpha+\beta}}\right] \cos \theta \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{a_{1 n} d_{1 n}\left(d_{n 1}+1\right) r^{d_{1 n}}+a_{2 n} d_{2 n}\left(d_{2 n}+1\right) r^{d_{2 n}}\right.
\end{aligned}
$$


$$\begin{aligned}
& \left.+a_{3 n} d_{3 n}\left(d_{3 n}+1\right) r^{d_{3 n}}+a_{4 n} d_{4 n}\left(d_{4 n}+1\right) r^{d_{4 n}}\right\} \cos n \theta \\
& +\frac{1}{r}\left[\left(\sqrt{1+\alpha+\beta}+1\right) f_{11} r^{\sqrt{1+\alpha+\beta}}+\left(\sqrt{1+\alpha+\beta}-1\right) f_{21} r^{-\sqrt{1+\alpha+\beta}}\right] \sin \theta \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{b_{1 n} d_{1 n}\left(d_{1 n}+1\right) r^{d_{1 n}}+b_{2 n} d_{2 n}\left(d_{2 n}+1\right) r^{d_{2 n}}\right. \\
& \left.+b_{3 n} d_{3 n}\left(d_{3 n}+1\right) r^{d_{3 n}}+b_{4 n} d_{4 n}\left(d_{4 n}+1\right) r^{d_{4 n}}\right\} \sin n \theta
\end{aligned}$$

$$\begin{aligned}
\sigma_{r \theta}(r, \theta) & =\frac{1}{r}\left(-f_{11} r^{\sqrt{1+\alpha+\beta}}+f_{21} r^{-\sqrt{1+\alpha+\beta}}\right) \cos \theta \\
& -\frac{1}{r} \sum_{n=2}^{\infty} n\left(b_{1 n} d_{1 n} r^{d_{1 n}}+b_{2 n} d_{2 n} r^{d_{2 n}}+b_{3 n} d_{3 n} r^{d_{3 n}}+b_{4 n} d_{4 n} r^{d_{4 n}}\right) \cos n \theta \\
& +\frac{1}{r}\left(e_{11} r^{\sqrt{1+\alpha+\beta}}-e_{21} r^{-\sqrt{1+\alpha+\beta}}\right) \sin \theta \\
& +\frac{1}{r} \sum_{n=2}^{\infty} n\left(a_{1 n} d_{1 n} r^{d_{1 n}}+a_{2 n} d_{2 n} r^{d_{2 n}}+a_{3 n} d_{3 n} r^{d_{3 n}}+a_{4 n} d_{4 n} r^{d_{4 n}}\right) \sin n \theta
\end{aligned}$$

where $e_{2}=a_{2}(\sqrt{\beta}+1), e_{3}=a_{3}(\sqrt{\beta}-1)$ and $\{e_{11}, e_{21}\}=\{a_{11}, a_{21}\} \sqrt{1+\alpha+\beta}$ and also $\{f_{11}, f_{21}\}=\{b_{11}, b_{21}\} \sqrt{1+\alpha+\beta}$. Equations (32) and (35) are combined to find the solution of a ring or annular plane of cylindrical orthotropy with the Volterra-type climb and glide edge dislocations. The combined solution certainly satisfies the continuity conditions of (19). Equation (32) fulfills the jump conditions (17) and (18). Now we want to know whether this combined solution still satisfies the jump conditions (17) and (18). Thereby, we analyze the multiple valued terms of Eqs. (35) or those giving two different values for $\theta=0$ and $\theta=2 \pi$. As it can be seen, there is no term in Eqs. (35) being multiple valued for $\theta=0$ and $\theta=2 \pi$, therefore viewing Eqs. (1), we conclude that the strain components behave similarly for $\theta=0$ and $\theta=2 \pi$. According to this point and Eq. (23) we draw a conclusion involving the point that only the terms $\sin \theta$ and $\cos \theta$ inside the strain components are able to produce the multiple-valued functions $\theta \sin \theta$ and $\theta \cos \theta$ for $f(\theta)$. Existence of such terms for $f(\theta)$ causes appearance of multiple-valued terms for displacements $u_{r}$ and $u_{\theta}$. In the case of plane stress, the terms of (35) including the trigonometric functions $\sin \theta$ and $\cos \theta$ are substituted into Eqs. (1) and the relevant strain components are found. As a matter of interest the terms of Eq. (23) which are included these strain components are vanished. Therefore, we arrive at $\int f(\theta) d \theta+f^{\prime}(\theta)+r g^{\prime}(r)-g(r)=0$. It means that the solution for $f(\theta)$ cannot be multiple-valued function and consequently the displacements $u_{r}$ and $u_{\theta}$ are not multiple-valued functions and then the jump conditions (17) and (18) are satisfied. Accordingly, the combined solution resulting from Eqs. (32) and (35) will be a solution for the ring or annular plane of cylindrical orthotropy weakened by the Volterra-type climb and glide edge dislocations provided that the inner and outer edge boundary conditions i.e. Eqs. (16) to be satisfied. Applying these boundary conditions to the combined solution yields

$$
e_{2} R_{2}{ }^{\sqrt{\beta}-1}+e_{3} R_{2}{ }^{\sqrt{\beta}-3}=-E b_{\theta} D_{0}(a) / a,
$$

$$
e_{11} R_{2}{ }^{\sqrt{1+\alpha+\beta}}-e_{21} R_{2}{ }^{-\sqrt{1+\alpha+\beta}}=-E b_{\theta} R_{2} D_{1}(a) / a,
$$

$$
\begin{aligned}
& a_{1 n}\left(1+d_{1 n}-n^{2}\right) R_{2}{ }^{d_{1 n}}+a_{2 n}\left(1+d_{2 n}-n^{2}\right) R_{2}{ }^{d_{2 n}} \\
& +a_{3 n}\left(1+d_{3 n}-n^{2}\right) R_{2}{ }^{d_{3 n}}+a_{4 n}\left(1+d_{4 n}-n^{2}\right) R_{2}{ }^{d_{4 n}}=-E b_{\theta} R_{2} D_{n}(a) / a, n \geq 2
\end{aligned}
$$

$$
e_{11} R_{2}{ }^{\sqrt{1+\alpha+\beta}}-e_{21} R_{2}{ }^{-\sqrt{1+\alpha+\beta}}=-E b_{\theta} R_{2} C_{1}(a) / a,
$$

$$
a_{1 n} d_{1 n} R_{2}{ }^{d_{1 n}}+a_{2 n} d_{2 n} R_{2}{ }^{d_{2 n}}+a_{3 n} d_{3 n} R_{2}{ }^{d_{3 n}}+a_{4 n} d_{4 n} R_{2}{ }^{d_{4 n}}=-E b_{\theta} R_{2} C_{n}(a) / n a,
$$

$$e_{2} R_{1}{ }^{\sqrt{\beta}-1}+e_{3} R_{1}{ }^{\sqrt{\beta}-3}=-E b_{\theta} B_{0}(a) / a,$$

$$e_{11} R_{1}^{\sqrt{1+\alpha+\beta}}-e_{21} R_{1}^{-\sqrt{1+\alpha+\beta}}=-E b_{\theta} R_{1} B_{1}(a) / a,$$

$$a_{1 n}\left(1+d_{1 n}-n^{2}\right) R_{1}{ }^{d_{1 n}}+a_{2 n}\left(1+d_{2 n}-n^{2}\right) R_{1}{ }^{d_{2 n}}$$

$$+a_{3 n}\left(1+d_{3 n}-n^{2}\right) R_{1}{ }^{d_{3 n}}+a_{4 n}\left(1+d_{4 n}-n^{2}\right) R_{1}{ }^{d_{4 n}}=-E b_{\theta} R_{1} B_{n}(a) / a,$$

$$e_{11} R_{1}^{\sqrt{1+\alpha+\beta}}-e_{21} R_{1}^{-\sqrt{1+\alpha+\beta}}=-E b_{\theta} R_{1} A_{1}(a) / a,$$

$$a_{1 n} d_{1 n} R_{1}{ }^{d_{1 n}}+a_{2 n} d_{2 n} R_{1}{ }^{d_{2 n}}+a_{3 n} d_{3 n} R_{1}{ }^{d_{3 n}}+a_{4 n} d_{4 n} R_{1}{ }^{d_{4 n}}=-E b_{\theta} R_{1} A_{n}(a) / n a,$$

$$f_{11} R_{2}^{\sqrt{1+\alpha+\beta}}-f_{21} R_{2}^{-\sqrt{1+\alpha+\beta}}=-E b_{r} R_{2} \overline{D}_{1}(a) / a,$$

$$b_{1 n}\left(1+d_{1 n}-n^{2}\right) R_{2}{ }^{d_{1 n}}+b_{2 n}\left(1+d_{2 n}-n^{2}\right) R_{2}{ }^{d_{2 n}}$$

$$+b_{3 n}\left(1+d_{3 n}-n^{2}\right) R_{2}{ }^{d_{3 n}}+b_{4 n}\left(1+d_{4 n}-n^{2}\right) R_{2}{ }^{d_{4 n}}=-E b_{r} R_{2} \overline{D}_{n}(a) / a,$$

$$f_{11} R_{1}^{\sqrt{1+\alpha+\beta}}-f_{21} R_{1}^{-\sqrt{1+\alpha+\beta}}=-E b_{r} R_{1} \overline{B}_{1}(a) / a,$$

$$b_{1 n}\left(1+d_{1 n}-n^{2}\right) R_{1}{ }^{d_{1 n}}+b_{2 n}\left(1+d_{2 n}-n^{2}\right) R_{1}{ }^{d_{2 n}}$$

$$+b_{3 n}\left(1+d_{3 n}-n^{2}\right) R_{1}{ }^{d_{3 n}}+b_{4 n}\left(1+d_{4 n}-n^{2}\right) R_{1}{ }^{d_{4 n}}=-E b_{r} R_{1} \overline{B}_{n}(a) / a,$$

$$b_{1 n} d_{1 n} R_{2}{ }^{d_{1 n}}+b_{2 n} d_{2 n} R_{2}{ }^{d_{2 n}}+b_{3 n} d_{3 n} R_{2}{ }^{d_{3 n}}+b_{4 n} d_{4 n} R_{2}{ }^{d_{4 n}}=E b_{r} R_{2} \bar{C}_{n}(a) / n a,$$

$$b_{1 n} d_{1 n} R_{1}{ }^{d_{1 n}}+b_{2 n} d_{2 n} R_{1}{ }^{d_{2 n}}+b_{3 n} d_{3 n} R_{1}{ }^{d_{3 n}}+b_{4 n} d_{4 n} R_{1}{ }^{d_{4 n}}=E b_{r} R_{1} \bar{A}_{n}(a) / n a,$$

$$-f_{11} R_{2}^{\sqrt{1+\alpha+\beta}}+f_{21} R_{2}^{-\sqrt{1+\alpha+\beta}}=-E b_{r} R_{2} \bar{C}_{1}(a) / a,$$

$$-f_{11} R_{1}^{\sqrt{1+\alpha+\beta}}+f_{21} R_{1}^{-\sqrt{1+\alpha+\beta}}=-E b_{r} R_{1} \bar{A}_{1}(a) / a$$

Knowing $A_{1}(a)=B_{1}(a), \bar{A}_{1}(a)=-\bar{B}_{1}(a)$ and $C_{1}(a)=D_{1}(a), \bar{C}_{1}(a)=-\bar{D}_{1}(a)$ solutions to the above equation are given in appendix. Problem of the climb edge dislocation $(b_{r}=0, b_{\theta} \neq 0)$ is symmetric with respect to the plane $\theta=0$ , [1]. It is easy to show that the half annular $0 \leq \theta \leq \pi$ is under the following boundary conditions [1]

$$\sigma_{r r}(r, \theta)=\sigma_{r r}(r,-\theta), \quad \sigma_{r \theta}(r, \theta)=-\sigma_{r \theta}(r,-\theta), \quad \sigma_{\theta \theta}(r, \theta)=\sigma_{\theta \theta}(r,-\theta),\qquad(37)$$

Also, the problem of the glide edge dislocation $(b_{\theta}=0, b_{r} \neq 0)$ is anti-symmetric with respect to the plane $\theta=0$ ,[10]. We observe that the half-annular $0 \leq \theta \leq \pi$ satisfies the following boundary conditions [10]

$$\sigma_{r r}(r, \theta)=-\sigma_{r r}(r,-\theta), \sigma_{r \theta}(r, \theta)=\sigma_{r \theta}(r,-\theta), \sigma_{\theta \theta}(r, \theta)=-\sigma_{\theta \theta}(r,-\theta)\qquad(38)$$

### 3. The intact annular plane under normal and shear tractions

In this section, we can now predict the stress field of an annular plane under normal and shear tractions on its boundaries. The boundary conditions along the curved surfaces read as

$$\sigma_{r r}\left(R_{1}, \theta\right)=\sigma_{01}(\theta)=\sum_{n=0}^{\infty} B_{e n} \cos n \theta+\sum_{n=1}^{\infty} \bar{B}_{e n} \sin n \theta\qquad(39)$$

$$\sigma_{r \theta}\left(R_{1}, \theta\right)=\tau_{01}(\theta)=\sum_{n=1}^{\infty} A_{e n} \sin n \theta+\sum_{n=0}^{\infty} \bar{A}_{e n} \cos n \theta$$

$$\sigma_{r r}\left(R_{2}, \theta\right)=\sigma_{02}(\theta)=\sum_{n=0}^{\infty} D_{e n} \cos n \theta+\sum_{n=1}^{\infty} \bar{D}_{e n} \sin n \theta$$

$$\sigma_{r \theta}\left(R_{2}, \theta\right)=\tau_{02}(\theta)=\sum_{n=1}^{\infty} C_{e n} \sin n \theta+\sum_{n=0}^{\infty} \bar{C}_{e n} \cos n \theta$$

For self-equilibrating loading we have $A_{e 1}=B_{e 1}, \bar{A}_{e 1}=-\bar{B}_{e 1}$ and $C_{e 1}=D_{e 1}, \bar{C}_{e 1}=-\bar{D}_{e 1}$ .

To prevent the unbalance moment, the constant terms in the shear stress expansions should satisfy the condition $R_{1}^{2} \bar{A}_{e 0}+R_{2}^{2} \bar{C}_{e 0}=0$. In fact the values of $R_{1}^{2} \int_{0}^{2 \pi} \tau_{01}(\theta) d \theta+$ $R_{2}^{2} \int_{0}^{2 \pi} \tau_{02}(\theta) d \theta$ must be zero for the problem to be one of elastostatics. To find the stress field we use the generalized Michell solution (35) and by applying the boundary conditions (39) to the aforementioned solution we arrive at

$$
\begin{aligned}
& e_{2}^{\prime} R_{1}^{\sqrt{\beta}-1}+e_{3}^{\prime} R_{1}^{\sqrt{\beta}-3}=B_{e 0} \\
& e_{2}^{\prime} R_{2}^{\sqrt{\beta}-1}+e_{3}^{\prime} R_{2}^{\sqrt{\beta}-3}=D_{e 0} \\
& e_{11}^{\prime} R_{1}^{\sqrt{1+\alpha+\beta}}-e_{21}^{\prime} R_{1}^{-\sqrt{1+\alpha+\beta}}=R_{1} B_{e 1} \\
& e_{11}^{\prime} R_{2}^{\sqrt{1+\alpha+\beta}}-e_{21}^{\prime} R_{2}^{-\sqrt{1+\alpha+\beta}}=R_{2} D_{e 1} \\
& e_{11}^{\prime} R_{1}^{\sqrt{1+\alpha+\beta}}-e_{21}^{\prime} R_{1}^{-\sqrt{1+\alpha+\beta}}=R_{1} A_{e 1} \\
& e_{11}^{\prime} R_{2}^{\sqrt{1+\alpha+\beta}}-e_{21}^{\prime} R_{2}^{-\sqrt{1+\alpha+\beta}}=R_{2} C_{e 1} \\
& a_{1 n}^{\prime}\left(1+d_{1 n}-n^{2}\right) R_{1}^{d_{1 n}}+a_{2 n}^{\prime}\left(1+d_{2 n}-n^{2}\right) R_{1}^{d_{2 n}} \\
& +a_{3 n}^{\prime}\left(1+d_{3 n}-n^{2}\right) R_{1}^{d_{3 n}}+a_{4 n}^{\prime}\left(1+d_{4 n}-n^{2}\right) R_{1}^{d_{4 n}}=R_{1} B_{e n} \\
& a_{1 n}^{\prime}\left(1+d_{1 n}-n^{2}\right) R_{2}^{d_{1 n}}+a_{2 n}^{\prime}\left(1+d_{2 n}-n^{2}\right) R_{2}^{d_{2 n}} \\
& +a_{3 n}^{\prime}\left(1+d_{3 n}-n^{2}\right) R_{2}^{d_{3 n}}+a_{4 n}^{\prime}\left(1+d_{4 n}-n^{2}\right) R_{2}^{d_{4 n}}=R_{2} D_{e n} \\
& a_{1 n}^{\prime} d_{1 n} R_{1}^{d_{1 n}}+a_{2 n}^{\prime} d_{2 n} R_{1}^{d_{2 n}}+a_{3 n}^{\prime} d_{3 n} R_{1}^{d_{3 n}}+a_{4 n}^{\prime} d_{4 n} R_{1}^{d_{4 n}}=R_{1} A_{e n} / n \\
& a_{1 n}^{\prime} d_{n 1} R_{2}^{d_{1 n}}+a_{2 n}^{\prime} d_{2 n} R_{2}^{d_{2 n}}+a_{3 n}^{\prime} d_{3 n} R_{2}^{d_{3 n}}+a_{4 n}^{\prime} d_{4 n} R_{2}^{d_{4 n}}=R_{2} C_{e n} / n \\
& f_{11}^{\prime} R_{1}^{\sqrt{1+\alpha+\beta}}-f_{21}^{\prime} R_{1}^{-\sqrt{1+\alpha+\beta}}=R_{1} \bar{B}_{e 1} \\
& f_{11}^{\prime} R_{2}^{\sqrt{1+\alpha+\beta}}-f_{21}^{\prime} R_{2}^{-\sqrt{1+\alpha+\beta}}=R_{2} \bar{D}_{e 1} \\
& -f_{11}^{\prime} R_{1}^{\sqrt{1+\alpha+\beta}}+f_{21}^{\prime} R_{1}^{-\sqrt{1+\alpha+\beta}}=R_{1} \bar{A}_{e 1} \\
& -f_{11}^{\prime} R_{2}^{\sqrt{1+\alpha+\beta}}+f_{21}^{\prime} R_{2}^{-\sqrt{1+\alpha+\beta}}=R_{2} \bar{C}_{e 1} \\
& b_{1 n}^{\prime}\left(1+d_{1 n}-n^{2}\right) R_{1}^{d_{1 n}}+b_{2 n}^{\prime}\left(1+d_{2 n}-n^{2}\right) R_{1}^{d_{2 n}} \\
& +b_{3 n}^{\prime}\left(1+d_{3 n}-n^{2}\right) R_{1}^{d_{3 n}}+b_{4 n}^{\prime}\left(1+d_{4 n}-n^{2}\right) R_{1}^{d_{4 n}}=R_{1} \bar{B}_{e n} \\
& b_{1 n}^{\prime}\left(1+d_{1 n}-n^{2}\right) R_{2}^{d_{1 n}}+b_{2 n}^{\prime}\left(1+d_{2 n}-n^{2}\right) R_{2}^{d_{2 n}} \\
& +b_{3 n}^{\prime}\left(1+d_{3 n}-n^{2}\right) R_{2}^{d_{3 n}}+b_{4 n}^{\prime}\left(1+d_{4 n}-n^{2}\right) R_{2}^{d_{4 n}}=R_{2} \bar{D}_{e n} \\
& b_{1 n}^{\prime} d_{1 n} R_{1}^{d_{1 n}}+b_{2 n}^{\prime} d_{2 n} R_{1}^{d_{2 n}}+b_{3 n}^{\prime} d_{3 n} R_{1}^{d_{3 n}}+b_{4 n}^{\prime} d_{4 n} R_{1}^{d_{4 n}}=-R_{1} \bar{A}_{e n} / n \\
& b_{1 n}^{\prime} d_{1 n} R_{2}^{d_{1 n}}+b_{2 n}^{\prime} d_{2 n} R_{2}^{d_{2 n}}+b_{3 n}^{\prime} d_{3 n} R_{2}^{d_{3 n}}+b_{4 n}^{\prime} d_{4 n} R_{2}^{d_{4 n}}=-R_{2} \bar{C}_{e n} / n
\end{aligned}
\tag{40}
$$

To distinguish the coefficients of the Michell solution used here from those given for the dislocation solution we use prime symbol for all coefficients. To find the stress field of an intact annular plane the above algebraic equations are solved and the unknown coefficients $e_{2}^{\prime}, e_{3}^{\prime}, e_{11}^{\prime}, e_{21}^{\prime}, f_{11}^{\prime}, f_{21}^{\prime}, a_{1 n}^{\prime}, a_{2 n}^{\prime}, a_{3 n}^{\prime}, a_{4 n}^{\prime}, b_{1 n}^{\prime}, b_{2 n}^{\prime}, b_{3 n}^{\prime}$ and $b_{4 n}^{\prime}$ are attained. For an isotropic annular we have $\beta=1$. Therefore the above solution for $\tau_{01}=\tau_{02}=0$ is simplified to that of given in the reference [52] which validates the above solution.

## 4. The annular plane with multiple cracks

Here, we are interested in examining how the dislocation solutions accomplished in Section 2 may be used to analyze the annular plane with multiple cracks. In order to achieve this aim, it is necessary to distribute a set of dislocations with unknown densities in the infinitesimal segments at the border of cracks. Let us consider an annular plane weakened by $N$ cracks including $N_1$ embedded cracks and $N_2$ edge cracks. Let the climb and glide edge dislocations with densities $b_{\theta j}$ and $b_{r j}$, respectively, be distributed on a curve in the ring or annular plane performing a j-th curved crack. Employing Eqs. (31), (35), the stress components caused at a point $(r, \theta)$ by the above-mentioned distribution of dislocations are

$$
\begin{aligned}
& \frac{1}{E} \sigma_{r r}(r, \theta)=\sum_{j=1}^{N}\left\{\int_{-1}^{1} b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}}[\frac{r_{j}-r c o s\left(\theta-\theta_{j}\right)}{r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)}\right. \\
& \left.+\frac{2 r_{j} r s i n^{2}\left(\theta-\theta_{j}\right)\left(r-r_{j} c o s\left(\theta-\theta_{j}\right)\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)\right)^{2}}\right] d t+\int_{-1}^{1}[\frac{r s i n\left(\theta-\theta_{j}\right)}{r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)} \\
& \left.-\frac{2 r_{j} s i n\left(\theta-\theta_{j}\right)\left(r_{j} c o s\left(\theta-\theta_{j}\right)-r\right)\left(r c o s\left(\theta-\theta_{j}\right)-r_{j}\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)\right)^{2}}\right] b_{r j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t \\
& +\int_{-1}^{1}\left\{e_{2 j} r^{\sqrt{\beta}-1}+e_{3 j} r^{\sqrt{\beta}-3}+\frac{1}{r}\left[e_{11 j} r^{\sqrt{1+\alpha+\beta}}-e_{21 j} r^{-\sqrt{1+\alpha+\beta}}\right] c o s\left(\theta-\theta_{j}\right)\right. \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{a_{1 n j}\left(1+d_{1 n}-n^{2}\right) r^{d_{1 n}}+a_{2 n j}\left(1+d_{2 n}-n^{2}\right) r^{d_{2 n}}\right. \\
& \left.+a_{3 n j}\left(1+d_{3 n}-n^{2}\right) r^{d_{3 n}}+a_{4 n j}\left(1+d_{4 n}-n^{2}\right) r^{d_{4 n}}\right\} c o s n\left(\theta-\theta_{j}\right) \\
& b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t+\int_{-1}^{1}\left\{\frac{1}{r}\left(f_{11 j} r^{\sqrt{1+\alpha+\beta}}-f_{21 j} r^{-\sqrt{1+\alpha+\beta}}\right) s i n\left(\theta-\theta_{j}\right)\right. \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} b_{1 n j}\left(1+d_{1 n}-n^{2}\right) r^{d_{1 n}}+b_{2 n j}\left(1+d_{2 n}-n^{2}\right) r^{d_{2 n}}\right. \\
& \left.\left.+b_{3 n j}\left(1+d_{3 n}-n^{2}\right) r^{d_{3 n}}+b_{4 n j}\left(1+d_{4 n}-n^{2}\right) r^{d_{4 n}}\right\} s i n n\left(\theta-\theta_{j}\right)\right\} d t
\end{aligned}
$$

$$
\begin{aligned}
& \frac{1}{E} \sigma_{\theta \theta}(r, \theta)=\sum_{j=1}^{N}\left\{\int_{-1}^{1} b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}}[\frac{2 r_{j} r s i n^{2}\left(\theta-\theta_{j}\right)\left(r_{j} c o s\left(\theta-\theta_{j}\right)-r\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)\right)^{2}}\right. \\
& \left.-\frac{r c o s\left(\theta-\theta_{j}\right)-r_{j}}{r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)}\right] d t+\int_{-1}^{1}[\frac{r s i n\left(\theta-\theta_{j}\right)}{r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)} \\
& \left.+\frac{2 r_{j} s i n\left(\theta-\theta_{j}\right)\left(r_{j} c o s\left(\theta-\theta_{j}\right)-r\right)\left(r c o s\left(\theta-\theta_{j}\right)-r_{j}\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r c o s\left(\theta-\theta_{j}\right)\right)^{2}}\right] b_{r j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t \\
& +\int_{-1}^{1}\left\{e_{2 j} \sqrt{\beta} r^{\sqrt{\beta}-1}+e_{3 j}(\sqrt{\beta}-2) r^{\sqrt{\beta}-3}\right. \\
& +\frac{1}{r}\left[e_{11 j}\left(\sqrt{1+\alpha+\beta}+1\right) r^{\sqrt{1+\alpha+\beta}}-e_{21 j}\left(1-\sqrt{1+\alpha+\beta}\right) r^{-\sqrt{1+\alpha+\beta}}\right] c o s\left(\theta-\theta_{j}\right) \\
& +\frac{1}{r} \sum_{n=2}^{\infty}\left\{a_{1 n j} d_{1 n}\left(d_{1 n}+1\right) r^{d_{1 n}}+a_{2 n j} d_{2 n}\left(d_{2 n}+1\right) r^{d_{2 n}}\right. \\
& \left.a_{3 n j} d_{3 n}\left(d_{3 n}+1\right) r^{d_{3 n}}+a_{4 n j} d_{4 n}\left(d_{4 n}+1\right) r^{d_{4 n}}\right\} c o s n\left(\theta-\theta_{j}\right) \\
& b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t+\int_{-1}^{1}\left\{\frac{1}{r}[f_{11 j}\left(\sqrt{1+\alpha+\beta}+1\right) r^{\sqrt{1+\alpha+\beta}}\right. \\
& \left.-f_{21 j}\left(1-\sqrt{1+\alpha+\beta}\right) r^{-\sqrt{1+\alpha+\beta}}\right] s i n\left(\theta-\theta_{j}\right)
\end{aligned}
$$

(41)

$$
\begin{aligned}
& +\frac{1}{r} \sum_{n=2}^{\infty} b_{r j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}}\left\{b_{1 n j} d_{1 n}\left(d_{1 n}+1\right) r^{d_{1 n}}+b_{2 n j} d_{2 n}\left(d_{2 n}+1\right) r^{d_{2 n}}\right. \\
& \left.+b_{3 n j} d_{3 n}\left(d_{3 n}+1\right) r^{d_{3 n}}+b_{4 n j} d_{4 n}\left(d_{4 n}+1\right) r^{d_{4 n}}\right\} \operatorname{sinn}\left(\theta-\theta_{j}\right)\} d t \\
& \frac{1}{E} \sigma_{r \theta}(r, \theta)=\sum_{j=1}^{N}\left\{\int_{-1}^{1} b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}}\left[\frac{2 r_{j}^{2} r \sin ^{3}\left(\theta-\theta_{j}\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r \cos \left(\theta-\theta_{j}\right)\right)^{2}}\right.\right. \\
& -\frac{r \sin \left(\theta-\theta_{j}\right)}{r^{2}+r_{j}^{2}-2 r_{j} r \cos \left(\theta-\theta_{j}\right)}] d t \\
& -\int_{-1}^{1}\left(r \cos \left(\theta-\theta_{j}\right)-r_{j}\right)\left[\frac{1}{r^{2}+r_{j}^{2}-2 r_{j} r \cos \left(\theta-\theta_{j}\right)}\right. \\
& \left.-\frac{2 r_{j}^{2} \sin ^{2}\left(\theta-\theta_{j}\right)\left(r-r_{j} \cos \left(\theta-\theta_{j}\right)\right)}{\left(r^{2}+r_{j}^{2}-2 r_{j} r \cos \left(\theta-\theta_{j}\right)\right)^{2}}\right] b_{r j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t \\
& +\int_{-1}^{1}\left\{\frac{1}{r}\left[e_{11 j} r^{\sqrt{1+\alpha+\beta}}-e_{21 j} r^{-\sqrt{1+\alpha+\beta}}\right] \sin \left(\theta-\theta_{j}\right)\right. \\
& \left.+\frac{1}{r} \sum_{n=2}^{\infty} n\left(a_{1 n j} d_{1 n} r^{d_{1 n}}+a_{2 n j} d_{2 n} r^{d_{2 n}}+a_{3 n j} d_{3 n} r^{d_{3 n}}+a_{4 n j} d_{4 n} r^{d_{4 n}}\right) \operatorname{sinn}\left(\theta-\theta_{j}\right)\right\} \\
& b_{\theta j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t+\int_{-1}^{1}\left\{\frac{1}{r}\left[-f_{11 j} r^{\sqrt{1+\alpha+\beta}}+f_{21 j} r^{-\sqrt{1+\alpha+\beta}}\right] \cos \left(\theta-\theta_{j}\right)\right. \\
& \left.-\frac{1}{r} \sum_{n=2}^{\infty} n\left(b_{1 n j} d_{1 n} r^{d_{1 n}}+b_{2 n j} d_{2 n} r^{d_{2 n}}+b_{3 n j} d_{3 n} r^{d_{3 n}}+b_{4 n j} d_{4 n} r^{d_{4 n}}\right) \operatorname{cosn}\left(\theta-\theta_{j}\right)\right\} \\
& \left.b_{r j} \sqrt{\left(r_{j}^{\prime}\right)^{2}+\left(r_{j} \theta_{j}^{\prime}\right)^{2}} d t\right\}
\end{aligned}
$$

In Eq.(41), $r_{j}=r_{j}(t), \theta_{j}=\theta_{j}(t)$ where $(r_{j}(t), \theta_{j}(t))$ specify the geometry of the crack with respect to coordinate system located at the center of the annular plane and the prime symbol denotes differentiation with respect to the relevant argument.

Fig.2. An annular plane with a typical embedded curved crack

The traction on the surface of the $i$-th crack caused by the presence of the foregoing distribution of dislocations, via employing Eqs. (30), leads to

$$
\begin{aligned}
& \sigma_{n n}\left(r_{i}(s), \theta_{i}(s)\right)=\frac{\sigma_{r r}\left(r_{i}(s), \theta_{i}(s)\right)+\sigma_{\theta \theta}\left(r_{i}(s), \theta_{i}(s)\right)}{2} \\
& -\frac{\sigma_{r r}\left(r_{i}(s), \theta_{i}(s)\right)-\sigma_{\theta \theta}\left(r_{i}(s), \theta_{i}(s)\right)}{2} \cos \left(2 \phi_{i}(s)\right)-\sigma_{r \theta}\left(r_{i}(s), \theta_{i}(s)\right) \sin \left(2 \phi_{i}(s)\right) \\
& \sigma_{n s}\left(r_{i}(s), \theta_{i}(s)\right)=-\frac{\sigma_{r r}\left(r_{i}(s), \theta_{i}(s)\right)-\sigma_{\theta \theta}\left(r_{i}(s), \theta_{i}(s)\right)}{2} \sin \left(2 \phi_{i}(s)\right) \\
& +\sigma_{r \theta}\left(r_{i}(s), \theta_{i}(s)\right) \cos \left(2 \phi_{i}(s)\right)
\end{aligned}
$$

where $\phi_{i}$ is the angle between the tangent to the surface of the $i$-th crack and the radial direction $r_{i}$. In fact, the movable orthogonal coordinates $n-s$ are chosen on the i-th crack such that the origin locates on the crack while the $s$-axis remains tangent to the crack surface. The stress components (19) and the components of Burgers vector $b_{r j}(t)$ and $b_{\theta j}(t)$ are transformed to the new coordinates. To transform the components of the Burgers vector we use the transformation relations $b_{s j}(t)=b_{r j}(t) \cos \left(\phi_{j}(t)\right)+b_{\theta j}(t) \sin \left(\phi_{j}(t)\right)$ and $b_{n j}(t)=-b_{r j}(t) \sin \left(\phi_{j}(t)\right)+b_{\theta j}(t) \cos \left(\phi_{j}(t)\right)$. Using the Eqs. (41) and (42), the traction

component $\sigma_{n p}(r_{i}(s), z_{i}), i=1,2,..., N, p=n, s$ on the surface of i-th crack caused by distribution of dislocations on all cracks surfaces yields

$$
\sigma_{n p}\left(r_{i}(s), \theta_{i}(s)\right)=\sum_{j=1}^{N} \int_{-1}^{1}\left[k_{1 n p i j}(s, t) b_{s j}(t)+k_{2 n p i j}(s, t) b_{n j}(t)\right] d t,
$$

i = 1,2, ..., N, p = n, s
where the kernels of the integrals $k_{1npij}(s,t)$ and $k_{2npij}(s,t)$ can be written using Eqs. (41) and (42). For the sake of brevity we did not bring them here.

By virtue of the Bueckner's principle (see reference [54]) the left-hand side of Eq. (43), after changing the sign, is the traction caused by applying the loading on inner or outer boundary of the intact annular plane at the presumed surfaces of cracks. The applied traction on the intact cylinder is taken to be as the equation (42) wherein the stress components $\sigma_{r r}(r_{i}(s), \theta_{i}(s)), \sigma_{\theta \theta}(r_{i}(s), \theta_{i}(s))$ and $\sigma_{r \theta}(r_{i}(s), \theta_{i}(s))$ are attained using the Eqs. (35) by replacing the coefficients $e_{2}, e_{3}, e_{11}, e_{21}, f_{11}, f_{21}, a_{1 n}, a_{2 n}, a_{3 n}, a_{4 n}, b_{1 n}, b_{2 n}, b_{3 n}, b_{4 n}$ with $e_{2}', e_{3}', e_{11}', e_{21}', f_{11}', f_{21}', a_{1 n}', a_{2 n}', a_{3 n}', a_{4 n}', b_{1 n}', b_{2 n}', b_{3 n}', b_{4 n}'$. Also, we change the sign of the relevant stress components.

The crack opening displacements for $j=1,2,..., N$ by considering the definition of the dislocation density function are given by [56]

$$
\begin{aligned}
& u_{s j}^{+}(s)-u_{s j}^{-}(s)=\int_{-1}^{s}\left[b_{s j}(t) \cos (\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t))\right. \\
& \left.+b_{n j}(t) \sin (\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t))\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t,
\end{aligned}
$$

$$
\begin{aligned}
& u_{n j}^{+}(s)-u_{n j}^{-}(s)=\int_{-1}^{s}\left[b_{n j}(t) \cos (\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t))\right. \\
& \left.-b_{s j}(t) \sin (\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t))\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t,
\end{aligned}
$$

As we know, the displacement field is single-valued away from the embedded crack surfaces. Therefore, the dislocation density for the j-th annular crack $(j=1,2,..., N_{1})$ should be subjected to the closure requirement as

$$
\begin{aligned}
& \int_{-1}^{1}\left[b_{s j}(t) \cos (\phi_{j}(1)+\theta_{j}(1)-\phi_{j}(t)-\theta_{j}(t))\right. \\
& \left.+b_{n j}(t) \sin (\phi_{j}(1)+\theta_{j}(1)-\phi_{j}(t)-\theta_{j}(t))\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t=0,
\end{aligned}
$$

$$
\begin{aligned}
& \int_{-1}^{1}\left[b_{n j}(t) \cos (\phi_{j}(1)+\theta_{j}(1)-\phi_{j}(t)-\theta_{j}(t))\right. \\
& \left.-b_{s j}(t) \sin (\phi_{j}(1)+\theta_{j}(1)-\phi_{j}(t)-\theta_{j}(t))\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t=0
\end{aligned}
$$

The Cauchy singular integral Eqs. (43) and the closure equations for embedded crack, that is, Eqs. (45) are solved simultaneously to determine dislocation density functions.

The stress field near the crack tips has a square-root singularity (Liebowitz [55]) therefore, by choosing that the tips of the embedded and edge cracks to be singular at $t=-1$, the dislocation densities for each kind of cracks are grouped as

$$
\begin{cases}
b_{p j}(t)=\frac{g_{p j}(t)}{\sqrt{1-t^{2}}} & \text { for embedded cracks } \\
b_{p j}(t)=g_{p j}(t) \sqrt{\frac{1-t}{1+t}} & \text { for edge cracks }
\end{cases}
\quad p=s, n \tag{46}
$$

Viewing Eqs.(46), as before, the integral equations (43) in conjunction with the closure equations for embedded i.e. Eqs. (45) are solved numerically. These integral equations are solved using a standard scheme namely Lobatto-Chebyshev (see for more details the reference [54]). They are discretized in the collocation points $t_{k}=\cos \left(\frac{k-1}{n-1} \pi\right), k=1,2, \ldots, n$ and $s_{l}=\cos \left(\frac{2 l-1}{2(n-1)} \pi\right), l=1,2, \ldots, n-1$. The number of discrete points, $s_{l}$ is one less than $t_{k}$. This eventually caused that the number of total discretized algebraic equations to be $2 N_{2}$ less than of the number of the unknowns $g_{j}\left(t_{k}\right)$. For embedded cracks because of the existing $2 N_{1}$ closure equations, the number of total equations and the unknowns $g_{j}\left(t_{k}\right)$ are identical. But for edge cracks, we have no closure equation and it seems that the number of discretized algebraic equations to be less than of the number of the unknowns $g_{j}\left(t_{k}\right)$. Fortunately the unknown variable $g_{j}(1)$ for edge crack will not be appeared in the discretized equations as we will explain it later and thus for this kind of cracks we don't need any additional equations. At last, the solution to the aforementioned equations leads to the dislocation density functions on the cracks.

The discretization of integral equations can be done using the following formula ([54], [57])

$$
\int_{-1}^{1} k_{i j}\left(s_{l}, t\right) \frac{g_{j}(t)}{\sqrt{1-t^{2}}} d t=\frac{\pi}{n-1} \sum_{k=1}^{n} e_{k} k_{i j}\left(s_{l}, t_{k}\right) g_{j}\left(t_{k}\right) \tag{47}
$$

$$
\int_{-1}^{1} k_{i j}\left(s_{l}, t\right) g_{j}(t) \sqrt{\frac{1-t}{1+t}} d t=\frac{\pi}{n-1} \sum_{k=1}^{n} e_{k}\left(1-t_{k}\right) k_{i j}\left(s_{l}, t_{k}\right) g_{j}\left(t_{k}\right)
$$

where $e_{k}=0.5$ for $k=1, n$ and $e_{k}=1$ for $1<k<n$. As it can be seen for $t_{n}=1$, the coefficient $1-t_{n}$ is vanished and then $g_{j}\left(t_{n}=1\right)$ will not be appeared in the discretized equations. To obtain a relation for stress intensity factor, firstly, we consider an infinite domain of the material with cylindrical orthotropy and an embedded crack. The local displacement field near the tip of an embedded crack located at the above-mentioned domain is given by ([55])

$$
\begin{aligned}
& u_{x}=k_{I}(2 r)^{1 / 2} R e\left\{\frac{1}{s_{1}-s_{2}}\left[s_{1} p_{2}(\cos \theta+s_{2} \sin \theta)^{1 / 2}-s_{2} p_{1}(\cos \theta+s_{1} \sin \theta)^{1 / 2}\right]\right\} \\
& +k_{I I}(2 r)^{1 / 2} R e\left\{\frac{1}{s_{1}-s_{2}}\left[p_{2}(\cos \theta+s_{2} \sin \theta)^{1 / 2}-p_{1}(\cos \theta+s_{1} \sin \theta)^{1 / 2}\right]\right\}
\end{aligned} \tag{48}
$$

$$
\begin{aligned}
& u_{y}=k_{I}(2 r)^{1 / 2} R e\left\{\frac{1}{s_{1}-s_{2}}\left[s_{1} q_{2}(\cos \theta+s_{2} \sin \theta)^{1 / 2}-s_{2} q_{1}(\cos \theta+s_{1} \sin \theta)^{1 / 2}\right]\right\} \\
& +k_{I I}(2 r)^{1 / 2} R e\left\{\frac{1}{s_{1}-s_{2}}\left[q_{2}(\cos \theta+s_{2} \sin \theta)^{1 / 2}-q_{1}(\cos \theta+s_{1} \sin \theta)^{1 / 2}\right]\right\}
\end{aligned}
$$

where $k_{I}$ and $k_{I I}$ are the Modes I and II stress intensity factors of the crack tip respectively. Also, $(r, \theta)$ is the local polar coordinates in which $r$ is the distance from the crack tip and $\theta$ is measured from the line tangent to the crack line on the crack tip. The angle between this line and x-axis is $\psi_{j}$ in which $\psi_{j}=\theta_{j}+\tan ^{-1}\left(\frac{r_{j} \theta_{j}^{\prime}}{r_{j}^{\prime}}\right)$. In the above relations the sign $R e\{$.$\} 

designates to real part of complex argument and $s_1$ and $s_2$ are the two zeros of the quartic equation of the material properties which is given by the relation $a_{11}'s^4 - 2a_{16}'s^3 + (2a_{12}' + a_{66}')s^2 - 2a_{26}'s + a_{22}' = 0$ where $a_{11}', a_{12}', a_{16}', a_{26}', a_{22}'$ and $a_{66}'$ are the transformed elastic constants in the local coordinates tangent to the crack line on the crack tip and are given by [53]

$$
\begin{align}
a_{11}' &= \frac{1}{E_2}\left[\beta cos^4\psi_j + \alpha sin^2\psi_j cos^2\psi_j + sin^4\psi_j\right] \\
a_{12}' &= \frac{1}{E_2}\left[(\beta - \alpha + 1)sin^2\psi_j cos^2\psi_j - \beta v_{12}\right] \\
a_{16}' &= \frac{1}{E_2}\left[(\alpha - 2\beta)cos^2\psi_j + (2 - \alpha)sin^2\psi_j\right]sin\psi_j cos\psi_j \\
a_{22}' &= \frac{1}{E_2}\left[\beta sin^4\psi_j + \alpha sin^2\psi_j cos^2\psi_j + cos^4\psi_j\right] \\
a_{26}' &= \frac{1}{E_2}\left[(2 - \alpha)cos^2\psi_j + (\alpha - 2\beta)sin^2\psi_j\right]sin\psi_j cos\psi_j \\
a_{66}' &= \frac{1}{E_2}\left[4(\beta - \alpha + 1)sin^2\psi_j cos^2\psi_j + \alpha + 2\beta v_{12}\right]
\end{align} \tag{49}
$$

Furthermore, we have [53, 55]

$$
\begin{align}
p_1 &= a_{11}'s_1^2 + a_{12}' - a_{16}'s_1, & p_2 &= a_{11}'s_2^2 + a_{12}' - a_{16}'s_2 \\
q_1 &= \frac{a_{12}'s_1^2 + a_{22}' - a_{26}'s_1}{s_1}, & q_2 &= \frac{a_{12}'s_2^2 + a_{22}' - a_{26}'s_2}{s_2}
\end{align} \tag{50}
$$

$$
s_1 = \frac{\frac{i}{\sqrt{2\beta}}\sqrt{\alpha - \sqrt{\alpha^2 - 4\beta}}cos\psi_j - sin\psi_j}{cos\psi_j + \frac{i}{\sqrt{2\beta}}\sqrt{\alpha - \sqrt{\alpha^2 - 4\beta}}sin\psi_j}
$$

$$
s_2 = \frac{\frac{i}{\sqrt{2\beta}}\sqrt{\alpha + \sqrt{\alpha^2 - 4\beta}}cos\psi_j - sin\psi_j}{cos\psi_j + \frac{i}{\sqrt{2\beta}}\sqrt{\alpha + \sqrt{\alpha^2 - 4\beta}}sin\psi_j}
$$

Substituting relations (50) into (48) yields

$$
u_n(\bar{r}_j, \pi) - u_n(\bar{r}_j, -\pi) = 2a_{22}'\sqrt{2\bar{r}_j}\sqrt{\frac{\alpha}{\beta} + \frac{2}{\sqrt{\beta}}}\left(\frac{k_{Ij}\chi_1 + k_{IIj}\chi_2}{\chi_3}\right) \tag{51}
$$

$$
u_s(\bar{r}_j, \pi) - u_s(\bar{r}_j, -\pi) = 2a_{11}'\sqrt{2\bar{r}_j}\sqrt{\frac{\alpha}{\beta} + \frac{2}{\sqrt{\beta}}}\left(\frac{k_{Ij}\chi_4 + k_{IIj}\chi_5}{\chi_6}\right), as \ \bar{r}_j \to 0
$$

where $\bar{r}_j$ is the radial distance from the j-th crack tip and the $n$ axis and the $s$ axis are normal and tangent to the j-th crack surfaces, respectively. Also

$$
\begin{align}
\chi_1 &= 2\left[\left(\frac{1}{\sqrt{\beta}} - 1\right)cos2\psi_j - \left(1 + \frac{1}{\sqrt{\beta}}\right)\right] \\
&+ \frac{1}{2\sqrt{\beta}}sin^22\psi_j\left[\frac{3\beta - \alpha - 1}{\sqrt{\beta}} + 3 - \alpha - \beta + (\beta - \alpha + 1)\left(\frac{1}{\sqrt{\beta}} - 1\right)cos2\psi_j\right] \\
\chi_2 &= \frac{1}{2}\left(1 - \frac{1}{\sqrt{\beta}}\right)sin2\psi_j\left[2(1 + \beta) + 2(\beta - 1)cos2\psi_j + (\alpha - \beta - 1)sin^22\psi_j\right]
\end{align} \tag{52}
$$

$$\chi_{3}=\frac{1}{4 \beta}(1+\beta-\alpha)^{2} \sin ^{4} 2 \psi_{j}+\left[\left(1+\frac{1}{\beta}\right) \alpha-4\right] \sin ^{2} 2 \psi_{j}+4$$

$$\chi_{4}=2\left(1-\frac{1}{\sqrt{\beta}}\right) \sin 2 \psi_{j}$$

$$\chi_{5}=2\left[\left(\frac{1}{\sqrt{\beta}}-1\right) \cos 2 \psi_{j}-\left(1+\frac{1}{\sqrt{\beta}}\right)\right]$$

$$\chi_{6}=2\left(1+\frac{1}{\beta}\right)+2\left(1-\frac{1}{\beta}\right) \cos 2 \psi_{j}+\left(\frac{\alpha-\beta-1}{\beta}\right) \sin ^{2} 2 \psi_{j}$$

Substituting these relations into Eqs. (44) and using Eq. (46) yields

$$
k_{I j} \chi_{1}+k_{I I j} \chi_{2}=\chi_{3} \lim _{s \rightarrow \pm 1} \frac{1}{2 a_{22}^{\prime} \sqrt{\frac{\alpha}{\beta}+\frac{2}{\sqrt{\beta}}} \sqrt{2 \bar{r}_{j}(s)}}
\tag{53}
$$

$$
\begin{aligned}
& \int_{-1}^{s}\left[-\frac{g_{s j}(t)}{\sqrt{1-t^{2}}} \sin \left(\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t)\right)\right. \\
& \left.+\frac{g_{n j}(t)}{\sqrt{1-t^{2}}} \cos \left(\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t)\right)\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t
\end{aligned}
$$

$$
k_{I j} \chi_{4}+k_{I I j} \chi_{5}=\chi_{6} \lim _{s \rightarrow \pm 1} \frac{1}{2 a_{11}^{\prime} \sqrt{\frac{\alpha}{\beta}+\frac{2}{\sqrt{\beta}}} \sqrt{2 \bar{r}_{j}(s)}}
$$

$$
\begin{aligned}
& \int_{-1}^{s}\left[\frac{g_{s j}(t)}{\sqrt{1-t^{2}}} \cos \left(\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t)\right)\right. \\
& \left.+\frac{g_{n j}(t)}{\sqrt{1-t^{2}}} \sin \left(\phi_{j}(s)+\theta_{j}(s)-\phi_{j}(t)-\theta_{j}(t)\right)\right] \sqrt{\left(r_{j}^{\prime}(t)\right)^{2}+\left(r_{j}(t) \theta_{j}^{\prime}(t)\right)^{2}} d t
\end{aligned}
$$

where $\bar{r}_{j}(s)=\sqrt{\left(r_{j}(s)\right)^{2}+\left(r_{j}( \pm 1)\right)^{2}-2 r_{j}(s) r_{j}( \pm 1) \cos \left(\theta_{j}(s)-\theta_{j}( \pm 1)\right)}$ in which $(r_{j}(s), \theta_{j}(s))$ is the parametric form of the j-th crack in the polar coordinates. Using the Taylor's expansion we may conclude that $\bar{r}_{j}(s) \to \sqrt{[r_{j}'( \pm 1)]^{2}+[r_{j}( \pm 1) \theta_{j}'( \pm 1)]^{2}}|s \mp 1|$ as $s \to \pm 1$. Application of the L'Hopital's rule in view of this relation allows us to simplify Eqs. (52). By solving the simplified equations for $k_{I j}$ and $k_{I I j}$ we arrive at

$$
\begin{aligned}
& k_{I j}=\left(\frac{\chi_{3} \chi_{5}}{a_{22}^{\prime}} g_{n j}( \pm 1)-\frac{\chi_{2} \chi_{6}}{a_{11}^{\prime}} g_{s j}( \pm 1)\right) \chi /\left(\chi_{1} \chi_{5}-\chi_{4} \chi_{2}\right) \\
& k_{I I j}=\left(\frac{\chi_{1} \chi_{6}}{a_{11}^{\prime}} g_{s j}( \pm 1)-\frac{\chi_{4} \chi_{3}}{a_{22}^{\prime}} g_{n j}( \pm 1)\right) \chi /\left(\chi_{1} \chi_{5}-\chi_{4} \chi_{2}\right)
\end{aligned}
\tag{54}
$$

where $\chi=0.5\left(\left[r_{j}^{\prime}( \pm 1)\right]^{2}+\left[r_{j}( \pm 1) \theta_{j}^{\prime}( \pm 1)\right]^{2}\right)^{\frac{1}{4}} / \sqrt{\frac{\alpha}{\beta}+\frac{2}{\sqrt{\beta}}}$. Similar relations to that found in the case of embedded cracks, can also be found out for the inner or outer edge cracks. In this case we eliminate the coefficient 0.5 from $\chi$. In the case of straight crack with half crack length $l$ we have $\psi_{j}=0$ and then the above relation are simplified as

$$
\begin{aligned}
& k_{I j}=-0.5 E_{2} g_{n j}( \pm 1) \sqrt{l} / \sqrt{\frac{\alpha}{\beta}+\frac{2}{\sqrt{\beta}}} \\
& k_{I I j}=-0.5 E_{2} g_{s j}( \pm 1) \sqrt{l} / \sqrt{\frac{\alpha}{\beta}+\frac{2}{\sqrt{\beta}}}
\end{aligned}
\tag{55}
$$

## 5. Results and discussion

The validity of analysis is verified by considering a few examples, that is, examples 1-3.

### Example 1
For our first example we consider an isotropic hollow cylinder or a disk weakened by an embedded radial crack wherein the disk loaded by different types of loadings. Using Eqs. (55), stress intensity factors for a radial embedded crack ($c \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta\theta}(r,0)=-\sigma_0$ are determined. The results are compared with those obtained by Delale and Erdogan [1], shown in Table 1. The geometry of the crack is specified by the following relations $\frac{d-c}{R_2-R_1}=0.5$ and $\frac{c-R_1}{R_2-d}=1$.

Table 1. Normalized stress intensity factor for a radial embedded crack ($c \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta\theta}(r,0)=-\sigma_0$

$$
\left(\frac{d-c}{R_2-R_1}=0.5, \frac{c-R_1}{R_2-d}=1, k_0=\sigma_0\sqrt{\frac{d-c}{2}}\right)
$$

<table>
  <thead>
    <tr>
      <th>$\frac{R_1}{R_2-R_1}$</th>
      <th>Present study<br>$k_i/k_0$</th>
      <th>Present study<br>$k_o/k_0$</th>
      <th>[1]<br>$k_i/k_0$</th>
      <th>[1]<br>$k_o/k_0$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.05</td>
      <td>1.1477</td>
      <td>1.2046</td>
      <td>1.1477</td>
      <td>1.2046</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1.1498</td>
      <td>1.2030</td>
      <td>1.1498</td>
      <td>1.2030</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>1.1580</td>
      <td>1.2018</td>
      <td>1.1580</td>
      <td>1.2018</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>1.1664</td>
      <td>1.2007</td>
      <td>1.1664</td>
      <td>1.2007</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.1736</td>
      <td>1.1980</td>
      <td>1.1736</td>
      <td>1.1980</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.1788</td>
      <td>1.1943</td>
      <td>1.1788</td>
      <td>1.1943</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.1809</td>
      <td>1.1923</td>
      <td>1.1810</td>
      <td>1.1923</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.1822</td>
      <td>1.1911</td>
      <td>1.1822</td>
      <td>1.1911</td>
    </tr>
  </tbody>
</table>

The above problem is reconsidered for a similar crack subjected to the uniform shear traction $\sigma_{r\theta}(r,0)=-\tau_0$ on the crack surface. The stress intensity factors are determined and compared with those obtained by Leung and Hu [10], given in Table 2. As it may be observed, the agreement of the results in the above examples is reasonable.

Table 2. Normalized stress intensity factor for a radial embedded crack ($c \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{r\theta}(r,0)=-\tau_0$

$$
\left(\frac{d-c}{R_2-R_1}=0.5, \frac{c-R_1}{R_2-d}=1, k_0=\tau_0\sqrt{\frac{d-c}{2}}\right)
$$

<table>
  <thead>
    <tr>
      <th>$\frac{R_1}{R_2-R_1}$</th>
      <th>Present study<br>$k_i/k_0$</th>
      <th>Present study<br>$k_o/k_0$</th>
      <th>[10]<br>$k_i/k_0$</th>
      <th>[10]<br>$k_o/k_0$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.05</td>
      <td>1.1024</td>
      <td>1.1403</td>
      <td>1.102403</td>
      <td>1.140259</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1.1130</td>
      <td>1.1439</td>
      <td>1.112981</td>
      <td>1.143946</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>1.1437</td>
      <td>1.1581</td>
      <td>1.143672</td>
      <td>1.158068</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>1.1730</td>
      <td>1.1753</td>
      <td>1.172981</td>
      <td>1.175292</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.1931</td>
      <td>1.1903</td>
      <td>1.193131</td>
      <td>1.190321</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.2010</td>
      <td>1.1981</td>
      <td>1.200979</td>
      <td>1.198131</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.2024</td>
      <td>1.2002</td>
      <td>1.202374</td>
      <td>1.200159</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.2027</td>
      <td>1.2009</td>
      <td>1.202751</td>
      <td>1.200981</td>
    </tr>
  </tbody>
</table>

5
1.2029
1.2014
1.202869
1.201402

The results for an internal radial edge crack $(R_{1} \leq r \leq d)$ are given in tables 3 and 4. The obtained results are compared with those borrowed from references [1] and [10] for Modes I and II stress intensity factors, respectively. For certain kind of crack and certain radii of annular plane the convergence of the infinite series of Eqs. (41) was rather slow. To overcome this problem we use the curve-fitting procedure of the form $A+B N^{-\delta}$ in which $N$ is the number of the truncation terms of the above mentioned series and $\delta$ is generally greater than unity [1]. Using the least square method and by choosing the values $N=100,120,140$, the constants $A, B$ are evaluated for each value of $\delta$. Obviously for $\delta>1$ the series will converge to $A$ when $N \rightarrow \infty$. For the sake of simplicity such a curve-fitting procedure of the form $A+B N^{-\delta}$ can be easily done only for the stress intensity factor evaluation [1]. The results of tables 3 and 4 are given for $\delta=5$ although they have a less dependence to $\delta$.

Table 3. Normalized stress intensity factor $(k_{I} / k_{0})$ for a radial inner edge crack $(R_{1} \leq r \leq d)$ in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta \theta}(r, 0)=-\sigma_{0}$

$$k_{0}=\sigma_{0} \sqrt{d-R_{1}}$$

<table>
    <thead>
        <tr>
            <th rowspan="2" colspan="2"></th>
            <th rowspan="2"></th>
            <th colspan="4">$\frac{R_{1}}{R_{2}-R_{1}}$</th>
        </tr>
        <tr>
            <th>$\frac{1}{3}$</th>
            <th>$\frac{1}{2}$</th>
            <th>1</th>
            <th>2</th>
            <th>3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="16">$\frac{d-R_{1}}{R_{2}-R_{1}}$</td>
            <td>Present study</td>
            <td>0.1</td>
            <td>1.1694</td>
            <td>1.1605</td>
            <td>1.1543</td>
            <td>1.1572</td>
            <td>1.1583</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.1</td>
            <td>1.153</td>
            <td>1.155</td>
            <td>1.157</td>
            <td>1.159</td>
            <td>1.167</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.2</td>
            <td>1.2321</td>
            <td>1.2324</td>
            <td>1.2486</td>
            <td>1.2786</td>
            <td>1.2959</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.2</td>
            <td>1.218</td>
            <td>1.229</td>
            <td>1.247</td>
            <td>1.277</td>
            <td>1.299</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.3</td>
            <td>1.3010</td>
            <td>1.3151</td>
            <td>1.3690</td>
            <td>1.4476</td>
            <td>1.4927</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.3</td>
            <td>1.295</td>
            <td>1.310</td>
            <td>1.366</td>
            <td>1.449</td>
            <td>1.493</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.4</td>
            <td>1.3805</td>
            <td>1.4092</td>
            <td>1.5087</td>
            <td>1.6581</td>
            <td>1.7489</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.4</td>
            <td>1.373</td>
            <td>1.402</td>
            <td>1.503</td>
            <td>1.655</td>
            <td>1.747</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.5</td>
            <td>1.4753</td>
            <td>1.5182</td>
            <td>1.6667</td>
            <td>1.9072</td>
            <td>2.0671</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.5</td>
            <td>1.465</td>
            <td>1.508</td>
            <td>1.658</td>
            <td>1.901</td>
            <td>2.066</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.6</td>
            <td>1.5928</td>
            <td>1.6484</td>
            <td>1.8446</td>
            <td>2.1905</td>
            <td>2.4453</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.6</td>
            <td>1.578</td>
            <td>1.635</td>
            <td>1.830</td>
            <td>2.177</td>
            <td>2.441</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.7</td>
            <td>1.7486</td>
            <td>1.8145</td>
            <td>2.0505</td>
            <td>2.4998</td>
            <td>2.8671</td>
        </tr>
        <tr>
            <td>[1]</td>
            <td>0.7</td>
            <td>1.730</td>
            <td>1.796</td>
            <td>2.030</td>
            <td>2.475</td>
            <td>2.851</td>
        </tr>
    </tbody>
</table>

Table 4. Normalized stress intensity factor $(k_{I I} / k_{0})$ for a radial inner edge crack $(R_{1} \leq r \leq d)$ in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{r \theta}(r, 0)=-\tau_{0}$

$$k_{0}=\tau_{0} \sqrt{d-R_{1}}$$

<table>
    <thead>
        <tr>
            <th rowspan="2" colspan="2"></th>
            <th rowspan="2"></th>
            <th colspan="4">$\frac{R_{1}}{R_{2}-R_{1}}$</th>
        </tr>
        <tr>
            <th>$\frac{1}{3}$</th>
            <th>$\frac{1}{2}$</th>
            <th>1</th>
            <th>2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="10">$\frac{d-R_{1}}{R_{2}-R_{1}}$</td>
            <td>Present study</td>
            <td>0.1</td>
            <td>1.1192</td>
            <td>1.1207</td>
            <td>1.1363</td>
            <td>1.1675</td>
        </tr>
        <tr>
            <td>[10]</td>
            <td>0.1</td>
            <td>1.114205</td>
            <td>1.113084</td>
            <td>1.112207</td>
            <td>*</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.2</td>
            <td>1.1424</td>
            <td>1.1286</td>
            <td>1.1267</td>
            <td>1.1425</td>
        </tr>
        <tr>
            <td>[10]</td>
            <td>0.2</td>
            <td>1.137115</td>
            <td>1.123781</td>
            <td>1.119115</td>
            <td>1.117818</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.3</td>
            <td>1.1904</td>
            <td>1.1644</td>
            <td>1.1461</td>
            <td>1.1519</td>
        </tr>
        <tr>
            <td>[10]</td>
            <td>0.3</td>
            <td>1.184718</td>
            <td>1.159126</td>
            <td>1.141009</td>
            <td>1.136173</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.4</td>
            <td>1.2592</td>
            <td>1.2249</td>
            <td>1.1926</td>
            <td>1.1889</td>
        </tr>
        <tr>
            <td>[10]</td>
            <td>0.4</td>
            <td>1.253483</td>
            <td>1.219228</td>
            <td>1.187572</td>
            <td>1.180698</td>
        </tr>
        <tr>
            <td>Present study</td>
            <td>0.5</td>
            <td>1.3538</td>
            <td>1.3140</td>
            <td>1.2708</td>
            <td>1.2584</td>
        </tr>
    </tbody>
</table>

| [10]          | 0.5 | 1.347864 | 1.308061 | 1.265209 | 1.252182 |
|---------------|-----|----------|----------|----------|----------|
| Present study | 0.6 | 1.4872   | 1.4434   | 1.3920   | 1.3727   |
| [10]          | 0.6 | 1.480665 | 1.437068 | 1.385657 | 1.366051 |
| Present study | 0.7 | 1.6880   | 1.6407   | 1.5830   | 1.5585   |
| [10]          | 0.7 | 1.680663 | 1.633779 | 1.57550  | 1.551078 |
| Present study | 0.8 | 2.0326   | 1.9803   | 1.9157   | 1.8877   |
| [10]          | 0.8 | 2.023717 | 1.972012 | 1.906569 | 1.878181 |
| Present study | 0.9 | 2.8257   | 2.7608   | 2.6822   | 2.6513   |
| [10]          | 0.9 | 2.813413 | 2.749417 | 2.669403 | 2.635523 |

## Example 2
As a second example, consider a concentric arc crack in an isotropic $(E_1 = E_2)$ rotating disc $(R_1 = 0)$ with a radius $a$ as shown in figure 3. The crack central angle is $2\gamma$. The mass density of the rotating disc is $\rho$ and it rotates with constant angular velocity $\omega$. The stress components of intact rotational disc are given as $\sigma_{rr} = \frac{\rho\omega^2}{8}(3 + v)(R_2^2 - r^2)$ and $\sigma_{\theta\theta} = \frac{\rho\omega^2}{8}[(3 + v)R_2^2 - (1 + 3v)r^2]$ (See for example [52]). The values of normalized Mode I and II stress intensity factors $\frac{k}{k_0}$ are tabulated in Table 5 for different ratios of $a/R_2$ and $\gamma$ in which $k_0 = \frac{\rho\omega^2}{8}(3 + v)(R_2^2 - a^2)\sqrt{\pi a sin\gamma}$. Because of symmetry of the problem the stress intensity factors of both crack tips should be identical as it has obtained in this study. They are not exactly equal as can be seen from the results obtained by boundary element approach [32]. Comparison of results of this study and those extracted from reference [32] verifies this work logically. The results are given for $E_1 = E_2 = \rho = \omega = 1$ and the poison ratio $v = 0.3$.

Fig.3. A rotating disc with a concentric arc crack

Table 5. Normalized stress intensity factor for a concentric arc crack in a rotating disc

<table>
    <thead>
        <tr>
            <th></th>
            <td colspan="4">$\frac{a}{R_2}=0.25$</td>
            <td colspan="4">$\frac{a}{R_2}=0.5$</td>
        </tr>
        <tr>
            <th>$\gamma$</th>
            <td>Present study $k_I/k_0$</td>
            <td>Present study $k_{II}/k_0$</td>
            <td>[32] $k_I/k_0$</td>
            <td>[32] $k_{II}/k_0$</td>
            <td>Present study $k_I/k_0$</td>
            <td>Present study $k_{II}/k_0$</td>
            <td>[32] $k_I/k_0$</td>
            <td>[32] $k_{II}/k_0$</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>15</th>
            <td>0.9818</td>
            <td>0.1307</td>
            <td>0.963<br>0.958</td>
            <td>0.132<br>0.136</td>
            <td>1.0228</td>
            <td>0.1480</td>
            <td>1.01<br>1.01</td>
            <td>0.148<br>0.154</td>
        </tr>
        <tr>
            <th>30</th>
            <td>0.9241</td>
            <td>0.2571</td>
            <td>0.916<br>0.913</td>
            <td>0.259<br>0.267</td>
            <td>1.0104</td>
            <td>0.3406</td>
            <td>1.00<br>1.00</td>
            <td>0.341<br>0.350</td>
        </tr>
        <tr>
            <th>45</th>
            <td>0.8271</td>
            <td>0.3667</td>
            <td>0.825<br>0.822</td>
            <td>0.372<br>0.383</td>
            <td>0.8977</td>
            <td>0.5143</td>
            <td>0.899<br>0.897</td>
            <td>0.520<br>0.531</td>
        </tr>
        <tr>
            <th>60</th>
            <td>0.7042</td>
            <td>0.4470</td>
            <td>0.704<br>0.703</td>
            <td>0.457<br>0.470</td>
            <td>0.7205</td>
            <td>0.6207</td>
            <td>0.728<br>0.729</td>
            <td>0.633<br>0.647</td>
        </tr>
        <tr>
            <th>75</th>
            <td>0.5749</td>
            <td>0.4950</td>
            <td>0.578<br>0.575</td>
            <td>0.510<br>0.525</td>
            <td>0.5362</td>
            <td>0.6626</td>
            <td>0.548<br>0.545</td>
            <td>0.682<br>0.698</td>
        </tr>
    </tbody>
</table>

When the outer radius of the disc $R_2$ trends to infinite we deal with an infinite plane. The problem of an infinite plane with an arc crack similar to the first part of this example was studied by Sih et al. [58]. The plane was under the action of two remote biaxial loadings $\sigma_x = \sigma_y = \sigma_0$ or $\sigma_{rr} = \sigma_{\theta\theta} = \sigma_0$. In this reference the analytical Mode I and II stress intensity factors were given by $k_I = \frac{\sigma_0\sqrt{sin\gamma(1-cos\gamma)}}{1+sin^2\frac{\gamma}{2}}$ and $k_{II} = \frac{\sigma_0\sqrt{sin\gamma(1+cos\gamma)}}{1+sin^2\frac{\gamma}{2}}$ for $a = 1$. The comparison of dimensionless stress intensity factors of this study for $\frac{a}{R_2} = 0.02$ and those

obtained by the aforementioned formula are given in Table 6. The stress intensity factors are normalized by $k_{0}=\sqrt{a \gamma}$. The results show a negligible difference between the results of the present work and those obtained by [58].

Table 6. Dimensionless stress intensity factor for a concentric arc crack in an infinite plane under two remote biaxial loadings $\sigma_{x}=\sigma_{y}=\sigma_{0}$

$$\frac{a}{R_{2}}=0.02$$

<table>
<thead>
  <tr>
    <th>$\gamma$</th>
    <th>Present study<br>$k_{I}/k_{0}$</th>
    <th>Present study<br>$k_{II}/k_{0}$</th>
    <th>[58]<br>$k_{I}/k_{0}$</th>
    <th>[58]<br>$k_{II}/k_{0}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>15</td>
    <td>0.1157</td>
    <td>0.8791</td>
    <td>0.1157</td>
    <td>0.8790</td>
  </tr>
  <tr>
    <td>30</td>
    <td>0.3041</td>
    <td>1.1346</td>
    <td>0.3040</td>
    <td>1.1346</td>
  </tr>
  <tr>
    <td>45</td>
    <td>0.4978</td>
    <td>1.2013</td>
    <td>0.4975</td>
    <td>1.2011</td>
  </tr>
  <tr>
    <td>60</td>
    <td>0.6603</td>
    <td>1.1429</td>
    <td>0.6598</td>
    <td>1.1428</td>
  </tr>
  <tr>
    <td>75</td>
    <td>0.7743</td>
    <td>1.0083</td>
    <td>0.7737</td>
    <td>1.0083</td>
  </tr>
</tbody>
</table>

## Example 3
In the following example, we consider a circular cylinder weakened by a pair of symmetric radial cracks depicted in Fig. 4. The inner and outer radii of the cylinder are $R_{1}=0$ and $R_{2}=$ 1 respectively. The cracks are extended along $c \leq x \leq d,-d \leq x \leq-c$ and subjected to a uniform crack surface pressure $\sigma_{\theta \theta}(r, 0)=-\sigma_{0}=-1$. The values of stress intensity factors of tips of cracks are presented in Table 5 and compared with those obtained by [16] which validates the work in the case of multiple cracks. Because of the symmetry of the problem the stress intensity factors of inner tips $k_{i}$ are identical for both cracks. Similarly the stress intensity factors of outer tips $k_{o}$ are equal.

Fig.4. A circular cylinder weakened by a pair of symmetric radial cracks

Table 7. Stress intensity factor for a pair of symmetric radial cracks $(c \leq x \leq d,-d \leq x \leq-c)$ in a cylinder or a disk subjected to a uniform crack surface pressure $\sigma_{\theta \theta}(r, 0)=-\sigma_{0}=-1$ for $c=0.1$

<table>
<thead>
  <tr>
    <th>$d$</th>
    <th>Present study<br>$k_{i}$</th>
    <th>Present study<br>$k_{o}$</th>
    <th>[16]<br>$k_{i}$</th>
    <th>[16]<br>$k_{o}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.2</td>
    <td>0.2292</td>
    <td>0.2280</td>
    <td>0.2292</td>
    <td>0.2279</td>
  </tr>
  <tr>
    <td>0.3</td>
    <td>0.3407</td>
    <td>0.3336</td>
    <td>0.3412</td>
    <td>0.3333</td>
  </tr>
  <tr>
    <td>0.4</td>
    <td>0.4445</td>
    <td>0.4258</td>
    <td>0.4463</td>
    <td>0.4245</td>
  </tr>
  <tr>
    <td>0.5</td>
    <td>0.5516</td>
    <td>0.5152</td>
    <td>0.5548</td>
    <td>0.5127</td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>0.6668</td>
    <td>0.6076</td>
    <td>0.6694</td>
    <td>0.6054</td>
  </tr>
  <tr>
    <td>0.7</td>
    <td>0.7938</td>
    <td>0.7113</td>
    <td>0.7896</td>
    <td>0.7154</td>
  </tr>
  <tr>
    <td>0.8</td>
    <td>0.9380</td>
    <td>0.8459</td>
    <td>0.9155</td>
    <td>0.8720</td>
  </tr>
  <tr>
    <td>0.9</td>
    <td>1.1147</td>
    <td>1.0859</td>
    <td>1.058</td>
    <td>1.173</td>
  </tr>
</tbody>
</table>

In the remaining of this section, more examples are rendered to demonstrate the applicability of the procedure for orthotropic materials. Because of the lack of the results for the orthotropic circular or annular planes we will not verify the results by comparison with literature and we just content ourselves to compare them by isotropic ones. It is worth mentioning that even for isotropic cases, the literature was restricted to a single mode while we extended the literature to solve the mixed mode crack problems.

## Example 4

This example concerns the problem of an annular wooden orthotropic plane of thickness $t = R_2 - R_1 = R_1$ with an embedded crack normal to the radial direction. The crack center is located at the point $(0.5(R_1 + R_2),0.6(R_2 - R_1))$ which the system of coordinates is attached to the center of the plane. Also, the x-axis is the ray $\theta = 0$. The crack angle is $\gamma = 0.5211\pi$ with respect to x-axis. This angle is chosen to make sure that the crack is opened under the following loading. For the sake of simplicity we consider a special case of loading (39) in which the annular plane is only under normal and shear tractions on its inner edge as below
$$
\sigma_{r r}\left(R_{1}, \theta\right)=\sigma_{0} \theta(2 \pi-\theta)=\sigma_{0}\left[\frac{2}{3} \pi^{2}-4 \sum_{n=1}^{\infty} \frac{1}{n^{2}} \cos n \theta\right], 0 \leq \theta \leq 2 \pi \tag{56}
$$

$$
\sigma_{r \theta}\left(R_{1}, \theta\right)=\frac{1}{3} \sigma_{0} \theta(\theta-\pi)(2 \pi-\theta)=-4 \sigma_{0} \sum_{n=1}^{\infty} \frac{1}{n^{3}} \sin n \theta, 0 \leq \theta \leq 2 \pi
$$

Therefore, by comparison with Eqs. (39) we have $C_{e n}=D_{e n}=\bar{C}_{e n}=\bar{D}_{e n}=\bar{A}_{e n}=\bar{B}_{e n}=0, A_{e n}=-\frac{4 \sigma_{0}}{n^{3}}(n \geq 1), B_{e 0}=\frac{2}{3} \pi^{2} \sigma_{0}$ and $B_{e n}=-\frac{4 \sigma_{0}}{n^{2}}, n \geq 1$. Also, the condition $A_{e 1}=B_{e 1}$ is satisfied. Then, the solution of the Eqs. (40) leads to non-zeros coefficients $e_{3}', e_{11}', e_{21}', a_{1 n}', a_{2 n}', a_{3 n}'$ and $a_{4 n}'$.

Wood is generally considered an anisotropic material. As a natural fiber-composite material, wood, globally shows a cylindrical anisotropy of stiffness and strength properties. The three principal axes of the cylindrical material anisotropy are (1) the stem (rotation) axis, termed pith, being parallel to the fiber direction; (2) the radial; and (3) tangential directions in the cross section normal to pith. In the radial-tangential plane the constitutive law thus is polar anisotropic. Also, in terms of engineering elastic models, wood is usually treated as an orthotropic material. Material properties of the wood are well documented through the numerous experimental studies. Therefore, without loss of generality, we choose a wooden annular plane of cylindrical orthotropy as an example of the annular planes of cylindrical orthotropy. Material Properties of the wooden annular plane of cylindrical orthotropy are chosen via the Table 8.

Table 8. Elastic and Poisson's ratios for various species at approximately 12% moisture content (Extracted from [59])

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    $E_{2}/E_{3}$
   </th>
   <th>
    $E_{1}/E_{3}$
   </th>
   <th>
    $G_{31}/E_{3}$
   </th>
   <th>
    $G_{32}/E_{3}$
   </th>
   <th>
    $G_{12}/E_{3}$
   </th>
   <th>
    Anisotropy ratios of this study (plane stress)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    Balsa
   </th>
   <td>
    $0.015$
   </td>
   <td>
    $0.046$
   </td>
   <td>
    $0.054$
   </td>
   <td>
    $0.037$
   </td>
   <td>
    $0.005$
   </td>
   <td>
    $\beta = 0.3261$
   </td>
  </tr>
  <tr>
   <th>
    (Hardwoods)
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
    $\alpha = 2.5663$
   </td>
  </tr>
  <tr>
   <th>
    Douglas-fir
   </th>
   <td>
    $0.039$
   </td>
   <td>
    $0.068$
   </td>
   <td>
    $0.064$
   </td>
   <td>
    $0.078$
   </td>
   <td>
    $0.007$
   </td>
   <td>
    $\beta = 0.5735$
   </td>
  </tr>
  <tr>
   <th>
    (Softwoods)
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
    $\alpha = 5.1241$
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    $\nu_{31}$
   </th>
   <th>
    $\nu_{32}$
   </th>
   <th>
    $\nu_{12}$
   </th>
   <th>
    $\nu_{21}$
   </th>
   <th>
    $\nu_{13}$
   </th>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    Balsa
   </th>
   <td>
    $0.229$
   </td>
   <td>
    $0.488$
   </td>
   <td>
    $0.665$
   </td>
   <td>
    $0.231$
   </td>
   <td>
    $0.018$
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    (Hardwoods)
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    Douglas-fir
   </th>
   <td>
    $0.292$
   </td>
   <td>
    $0.449$
   </td>
   <td>
    $0.390$
   </td>
   <td>
    $0.374$
   </td>
   <td>
    $0.036$
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <th>
    (Softwoods)
   </th>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

Generally speaking, not only the selection of the softwood (Douglas-fir) and the hardwood (Balsa) as the examples of orthotropic materials but also the comparison of the results of them with an isotropic material are very important. Because from the fracture behavior point of view the isotropic material locates between these orthotropic materials. This can be shown in the following.

Fig 5 shows the variation of the dimensionless stress intensity factors, $k_I/k_0$ and $k_{II}/k_0$ at the crack tips against $\frac{l}{R_2-R_1}$ in which $k_0=\sigma_0\sqrt{l}$ and $l$ is the half crack length. As one would expect, the increases of $k_I/k_0$ as well as $k_{II}/k_0$ in both crack tips with the growth of the crack length are seen. The indexes $L$ and $U$ denote to lower and upper crack tips, respectively. The stress intensity factors $k_I/k_0$ and $k_{II}/k_0$ for hardwood have the smallest values for all crack lengths in contrast to the other materials. Also, for softwood they have the biggest values in comparison with other materials. Beside of the graphically presentation of the results we show the results in tabular form to give better comparison between them (See Table 9).

We reexamine this example with a crack of half crack length $l=0.3(R_2-R_1)$ and we plot variation of the dimensionless stress intensity factors with respect to dimensionless crack center horizontal distance $d/(R_2-R_1)$ in Fig. 6. In other word, the crack center is located at coordinates $(d,0.6(R_2-R_1))$. As we generally expect, approaching the crack to the outer portion of circular plane, reduces nondimensional stress intensity factors of the crack tips. Comparison of two annular planes made of hardwood and softwood with isotropic annular plane shows that for the hardwood, $k_I/k_0$ and $k_{II}/k_0$ have the smallest values. Table 10 provides the numerical values of the results shown in Fig. 6.

Fig 5. Variation of non-dimensional stress intensity factors at crack tips against $\frac{l}{R_2-R_1}$ for $R_2=2R_1$ and $\frac{d}{R_2+R_1}=0.5$.

Fig. 6. Variation of the non-dimensional stress intensity factors at crack tips against $d/(R_2-R_1)$ for $R_2=2R_1$ and $l=0.3(R_2-R_1)$.

Table 9. Values of non-dimensional stress intensity factors at crack tips in terms of $\frac{l}{R_2-R_1}$ for $R_2=2R_1$ and $\frac{d}{R_2+R_1}=0.5$.

<table>
<thead>
<tr>
<th>$\frac{l}{R_2-R_1}$</th>
<th>Balsa $k_I/k_0$</th>
<th>Isotopic $k_I/k_0$</th>
<th>Douglas-fir $k_I/k_0$</th>
<th>Balsa $k_{II}/k_0$</th>
<th>Isotopic $k_{II}/k_0$</th>
<th>Douglas-fir $k_{II}/k_0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.02</td>
<td>0.2216</td>
<td>0.2630</td>
<td>0.3112</td>
<td>0.2070</td>
<td>0.2419</td>
<td>0.2878</td>
</tr>
<tr>
<td>0.07</td>
<td>0.4408</td>
<td>0.5256</td>
<td>0.6189</td>
<td>0.4008</td>
<td>0.4607</td>
<td>0.5549</td>
</tr>
<tr>
<td>0.12</td>
<td>0.6112</td>
<td>0.7334</td>
<td>0.8591</td>
<td>0.5626</td>
<td>0.6320</td>
<td>0.7741</td>
</tr>
<tr>
<td>0.17</td>
<td>0.7627</td>
<td>0.9216</td>
<td>1.0747</td>
<td>0.7323</td>
<td>0.8055</td>
<td>1.0013</td>
</tr>
<tr>
<td>0.22</td>
<td>0.8999</td>
<td>1.0939</td>
<td>1.2725</td>
<td>0.9167</td>
<td>0.9923</td>
<td>1.2463</td>
</tr>
<tr>
<td>0.27</td>
<td>1.0248</td>
<td>1.2516</td>
<td>1.4548</td>
<td>1.1158</td>
<td>1.1937</td>
<td>1.5099</td>
</tr>
<tr>
<td>0.32</td>
<td>1.1398</td>
<td>1.3976</td>
<td>1.6243</td>
<td>1.3288</td>
<td>1.4089</td>
<td>1.7916</td>
</tr>
<tr>
<td>0.37</td>
<td>1.2481</td>
<td>1.5364</td>
<td>1.7847</td>
<td>1.5563</td>
<td>1.6377</td>
<td>2.0923</td>
</tr>
</tbody>
</table>

Table 10. Values of non-dimensional stress intensity factors at crack tips in terms of $d/(R_2-R_1)$ for $R_2=2R_1$ and $l=0.3(R_2-R_1)$.

<table>
<thead>
<tr>
<th>$\frac{d}{R_2-R_1}$</th>
<th>Balsa $k_I/k_0$</th>
<th>Isotopic $k_I/k_0$</th>
<th>Douglas-fir $k_I/k_0$</th>
<th>Balsa $k_{II}/k_0$</th>
<th>Isotopic $k_{II}/k_0$</th>
<th>Douglas-fir $k_{II}/k_0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.2</td>
<td>2.5299</td>
<td>2.4738</td>
<td>3.2776</td>
<td>3.0826</td>
<td>3.1653</td>
<td>4.0274</td>
</tr>
<tr>
<td>1.25</td>
<td>2.2276</td>
<td>2.2546</td>
<td>2.9319</td>
<td>2.6538</td>
<td>2.7454</td>
<td>3.4924</td>
</tr>
<tr>
<td>1.3</td>
<td>1.9635</td>
<td>2.0604</td>
<td>2.6266</td>
<td>2.3059</td>
<td>2.4022</td>
<td>3.0535</td>
</tr>
</tbody>
</table>

| 1.35 | 1.7336 | 1.8887 | 2.3573 | 2.016 | 2.1135 | 2.6844 |
|-----|-------|-------|-------|------|-------|-------|
| 1.4 | 1.5344 | 1.7373 | 2.1202 | 1.7702 | 1.8663 | 2.3690 |
| 1.45 | 1.3627 | 1.6044 | 1.912 | 1.5598 | 1.6526 | 2.0972 |
| 1.5 | 1.2158 | 1.4886 | 1.7301 | 1.3792 | 1.4672 | 1.8621 |
| 1.55 | 1.0917 | 1.3889 | 1.5727 | 1.2248 | 1.3075 | 1.6596 |
| 1.6 | 0.9894 | 1.3057 | 1.4394 | 1.095 | 1.1724 | 1.4882 |
| 1.65 | 0.9099 | 1.2416 | 1.3321 | 0.9906 | 1.0637 | 1.3494 |
| 1.7 | 0.8599 | 1.2068 | 1.2605 | 0.9173 | 0.9886 | 1.2518 |

### Example 5
In this example, we consider an annular orthotropic plane of thickness $t=R_1$ with a concentric arc crack of a radius $a=1.5R_1$. The crack central angle is $2\gamma$. The crack tip is located on the ray $\theta=0$ in the radial distance $d=0.5(R_1+R_2)$ from the center of the plane. The annular plane is only under normal and shear tractions on its inner edge as obeying from the loading (56). The domain of variation of the angle $\gamma$ is chosen such that to make sure the crack is opened under the loading (56). Material Properties of the wooden annular plane of cylindrical orthotropy are also chosen from the Table 8. Fig 7 shows the variation of the dimensionless stress intensity factors, $k_I/k_0$and $k_{II}/k_0$ at the crack tips against $\frac{a\gamma}{R_2-R_1}$ in which $k_0=\sigma_0\sqrt{a\gamma}$. Similarly the indexes $L$ and $U$ denote to lower and upper crack tips, respectively. Comparison between results of an annular plane of isotropic material and two kinds of softwood and hardwood can be seen in this Fig.7. Similar to example 4, the increases of $k_I/k_0$ as well as $k_{II}/k_0$ in both crack tips with the growth of the crack length are observed. Under the effect of curvature of the crack and material isotropy, $k_I/k_0$ and $k_{II}/k_0$ for hardwood have the smallest values for all crack lengths in comparison with the other materials. For all lengths of the circular crack $k_I/k_0$ for both the softwood and the isotropic material are almost identical but $k_{II}/k_0$ for softwood has the biggest value. Similar to previous example we give the results in Table 11.

Fig. 7. Variation of the non-dimensional stress intensity factors at crack tips against $l/(R_2-R_1)$ for $R_2=2R_1$ and $R=1.5R_1$.

Table 11. Values of non-dimensional stress intensity factors at crack tips in terms of $l/(R_2-R_1)$ for $R_2=2R_1$ and $R=1.5R_1$.

<table>
<thead>
  <tr>
    <th rowspan="2">$\frac{l}{R_2-R_1}$</th>
    <th>Balsa</th>
    <th>Isotropic</th>
    <th>Douglas-fir</th>
    <th>Balsa</th>
    <th>Isotropic</th>
    <th>Douglas-fir</th>
  </tr>
  <tr>
    <th>$k_I/k_0$</th>
    <th>$k_I/k_0$</th>
    <th>$k_I/k_0$</th>
    <th>$k_{II}/k_0$</th>
    <th>$k_{II}/k_0$</th>
    <th>$k_{II}/k_0$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.0052</td>
    <td>4.333e-5</td>
    <td>4.8001e-5</td>
    <td>5.8385e-5</td>
    <td>0.0216</td>
    <td>0.0324</td>
    <td>0.0323</td>
  </tr>
  <tr>
    <td>0.0528</td>
    <td>0.0433</td>
    <td>0.0487</td>
    <td>0.0587</td>
    <td>0.2261</td>
    <td>0.3331</td>
    <td>0.3373</td>
  </tr>
  <tr>
    <td>0.1052</td>
    <td>0.1173</td>
    <td>0.1369</td>
    <td>0.1609</td>
    <td>0.3528</td>
    <td>0.4993</td>
    <td>0.5229</td>
  </tr>
  <tr>
    <td>0.1576</td>
    <td>0.2034</td>
    <td>0.2511</td>
    <td>0.2848</td>
    <td>0.4935</td>
    <td>0.6671</td>
    <td>0.7241</td>
  </tr>
  <tr>
    <td>0.2099</td>
    <td>0.2925</td>
    <td>0.3863</td>
    <td>0.4209</td>
    <td>0.6574</td>
    <td>0.8532</td>
    <td>0.9519</td>
  </tr>
  <tr>
    <td>0.2623</td>
    <td>0.3792</td>
    <td>0.5388</td>
    <td>0.5638</td>
    <td>0.8476</td>
    <td>1.0618</td>
    <td>1.2075</td>
  </tr>
  <tr>
    <td>0.3146</td>
    <td>0.4598</td>
    <td>0.7058</td>
    <td>0.7096</td>
    <td>1.0673</td>
    <td>1.2925</td>
    <td>1.4915</td>
  </tr>
  <tr>
    <td>0.3670</td>
    <td>0.5320</td>
    <td>0.8846</td>
    <td>0.8553</td>
    <td>1.3192</td>
    <td>1.5425</td>
    <td>1.8039</td>
  </tr>
  <tr>
    <td>0.4194</td>
    <td>0.5949</td>
    <td>1.0725</td>
    <td>0.9989</td>
    <td>1.6036</td>
    <td>1.8069</td>
    <td>2.1412</td>
  </tr>
  <tr>
    <td>0.4717</td>
    <td>0.6496</td>
    <td>1.2667</td>
    <td>1.1396</td>
    <td>1.9178</td>
    <td>2.0796</td>
    <td>2.4972</td>
  </tr>
</tbody>
</table>

### Example 6
The problem of a pair of symmetric radial cracks, Fig. 4, solved by Chang [16] is re-examined and the results are depicted in Fig. 8. To ensure the opening of the cracks occurs, we let the disc be under uniform crack surface pressure $\sigma_{\theta\theta}(r,0)=-\sigma_0$. In fact the loading and cracks configurations are similar to the earlier example; namely example 3. Here, the

centers of the cracks are fixed and located at distance $d = 0.5(R_2 + R_1)$ from the center of the disc. The ensuing trends of Mode I dimensionless stress intensity factors, $k_I/k_0$, versus the dimensionless crack length $l/(R_2 - R_1)$ are shown in Fig. 8 in which $k_0 = \sigma_0\sqrt{l}$. Because of the symmetry of the problem, the stress intensity factors of inner tips i.e. $k_{Ii1}$ and $k_{Ii2}$ are identical for both cracks. Similarly the stress intensity factors of inner tips i.e. $k_{Io1}$ and $k_{Io2}$ are equal. The stress intensity factors for the crack tips increase rapidly as the crack lengths increase. The interaction between the two approaching inner crack tips is noticeable in the current example. Comparison of a disc made of hardwood with two discs, namely an isotropic disc and a disc made of softwood, shows that $k_{Io}/k_0$ for hardwood has the least value. Similarly $k_{Ii}/k_0$ for hardwood has the lowest values in comparison with that for isotropic and softwood annular planes. A good assessment of the results of Fig. 8 can also be attained using table 12.

Fig. 8. Variation of the non-dimensional stress intensity factors at crack tips against $l/(R_2 - R_1)$ for $R_2 = 2R_1$ and $R = 1.5R_1$.

Table 12. Values of non-dimensional stress intensity factors at crack tips in terms of $l/(R_2 - R_1)$ for $R_2 = 2R_1$ and $R = 1.5R_1$.

<table>
<thead>
<tr>
<th>$\frac{l}{R_2 - R_1}$</th>
<th>Balsa<br>$k_{Io1}/k_0$</th>
<th>Isotopic<br>$k_{Io1}/k_0$</th>
<th>Douglas-fir<br>$k_{Io1}/k_0$</th>
<th>Balsa<br>$k_{IIi1}/k_0$</th>
<th>Isotopic<br>$k_{IIi1}/k_0$</th>
<th>Douglas-fir<br>$k_{IIi1}/k_0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.01</td>
<td>0.5474</td>
<td>1.0046</td>
<td>0.9654</td>
<td>0.5377</td>
<td>0.9921</td>
<td>0.9508</td>
</tr>
<tr>
<td>0.06</td>
<td>1.4147</td>
<td>2.5622</td>
<td>2.4764</td>
<td>1.2713</td>
<td>2.3789</td>
<td>2.2606</td>
</tr>
<tr>
<td>0.11</td>
<td>2.0454</td>
<td>3.6612</td>
<td>3.5507</td>
<td>1.6866</td>
<td>3.2002</td>
<td>3.0096</td>
</tr>
<tr>
<td>0.16</td>
<td>2.6666</td>
<td>4.7260</td>
<td>4.5891</td>
<td>2.0292</td>
<td>3.8999</td>
<td>3.6243</td>
</tr>
<tr>
<td>0.21</td>
<td>3.3477</td>
<td>5.8868</td>
<td>5.7116</td>
<td>2.3718</td>
<td>4.6068</td>
<td>4.2267</td>
</tr>
<tr>
<td>0.26</td>
<td>4.1503</td>
<td>7.2583</td>
<td>7.0227</td>
<td>2.7721</td>
<td>5.4235</td>
<td>4.9117</td>
</tr>
<tr>
<td>0.31</td>
<td>5.1635</td>
<td>9.0059</td>
<td>8.6724</td>
<td>3.3087</td>
<td>6.4906</td>
<td>5.8073</td>
</tr>
<tr>
<td>0.36</td>
<td>6.5580</td>
<td>11.446</td>
<td>10.950</td>
<td>4.1333</td>
<td>8.0809</td>
<td>7.1619</td>
</tr>
</tbody>
</table>

## 6. Concluding remarks

We have developed the fundamental climb and glide edge dislocation solutions for an annular plane of cylindrical anisotropy which its boundaries are free of any surface traction. To this end, the Michell solution is generalized for material of cylindrical anisotropy. As the complementary results, stress field in an intact annular plane of cylindrical anisotropy under traction on its inner and outer edges were given. The fundamental dislocation solution has been successfully employed to analyze crack problems in an annular plane by a continuous distribution of dislocation densities over the crack faces. As demonstrated, the unknown dislocation density on cracks surfaces was computed using solving a set of integral equations of Cauchy singular type. Finally, some example problems with multiple cracks and with smooth geometries were solved.

Major assumptions of the problem have been considered as follows:

(1) The in-plane theory of elasticity was used to analyze the problem namely both states of plane stress and strain was analyzed.

(2) The annular plane is made of a material having cylindrical anisotropy with 9 independent anisotropy elastic constant.

(3) Cracks are at the transverse section of a cylindrically anisotropic material.

(4) The problem has been solved in the scope of linear elastic fracture mechanics.

It is worth mentioning that the results for wooden annular planes are not verified by the results of the literature. Also, the results in particular, suggested that:

(1) The normalized stress intensity factor (SIF) of the crack tip in the annular plane increases as its length increases. Conversely, SIF decreases at a crack tip as it approaches the outer edge of the annular plane.

(2) The stress intensity factors $k_I/k_0$ and $k_{II}/k_0$ for hardwood have the smallest values for all crack lengths in comparison with the other materials.

(3) Anisotropy and crack location have crucial effects on SIFs of different modes of fracture. Hence, the final SIF value is a compromise/trade-off between these two effects and which mode of fracture is intended. Whether the cracks extended radially or angularly, the SIF will be differently under affection of material anisotropy.

(4) The interaction between the cracks is a factor affecting the SIF.

(5) The curvature of curved cracks is also another factor affecting the SIF

Future work can include more complex crack problems, considering annular planes made of different material types (e.g., for functionally graded materials).

References:

[1] F. Delale, F. Erdogan, Stress intensity factors in a hollow cylinder containing a radial crack, Int. J. Fract., **20** (1982) 251-265.

[2] R. Tang, F. Erdogan, Stress intensity factors in a reinforced thick-walled cylinder, Int. J. Eng. Sci., **22** (1984) 867-879.

[3] W. Xiao-chun, T. Ren-ji, An analysis of a radial crack in a reinforced hollow cylinder, Appl. Math. Mech., **8** (1987) 697-703.

[4] Y.L. Xu, F. Delale, Stress intensity factors for an internal or edge crack in a circular elastic disk subjected to concentrated or distributed loads, Eng. Fract. Mech., **42** (1992) 757-787.

[5] X. Yong Li, Stress intensity factors of a radial crack in a compound disk, Int. J. Eng. Sci., **31** (1993) 1375-1389.

[6] X. Yong Li, Stress intensity factors of a radial crack in a rotating compound disk, Eng. Fract. Mech., **44** (1993) 409-423.

[7] X. Yong Li, Stress intensity factors of a radial crack in a compound disk subjected to point loads, Int. J. Solids Struct., **30** (1993) 499-511.

[8] X. Yong Li, Stress intensity factors of a radial crack in a compound disk subjected to concentrated forces, Eng. Fract. Mech., **47** (1994) 777-791.

[9] N.I. Muskhelishvili, Some basic problems of the mathematical theory of elasticity, Springer Science & Business Media 2013.

[10] A.Y.T. Leung, J.D. Hu, Mode II stress intensity factors for a circular ring or a hollow cylinder with a radial crack, Int. J. Press. Vessels Pip., **72** (1997) 149-156.

[11] O.L. Bowie, C.E. Freese, Elastic analysis for a radial crack in a circular ring, Eng. Fract. Mech., **4** (1972) 315-321.

[12] P.G. Tracy, Elastic analysis of radial cracks emanating from the outer and inner surfaces of a circular ring, Eng. Fract. Mech., **11** (1979) 291-300.

[13] P. Tracy, Stress intensity factors for multiple edge cracks in rotating hollow discs, Int. J. Fract., **16** (1980) 85-93.

[14] S. Chang, An equivalent procedure for the evaluation of the stress intensity factors of a radial crack in a disc, Int. J. Eng. Sci., **21** (1983) 1247-1252.

[15] Y.Z. Chen, H.Y. Liu, Multiple cracks in pressurized hollow cylinder, Theor. Appl. Fract. Mech., **10** (1988) 213-218.

[16] S. Chang, Stress intensity factors in a circular cylinder containing a pair of radial cracks, Eng. Fract. Mech., **30** (1988) 811-818.

[17] Y. Chang-yan, Z. Cheng-de, Plane problems of a finite disc containing an internal crack, Appl. Math. Mech., **11** (1990) 921-930.

[18] Y.H. Wang, R.C. Xu, Y.K. Cheung, SIF evaluation for a pressurized hollow cylinder with a single crack on the outside surface, Eng. Fract. Mech., **38** (1991) 13-21.

[19] D.-L. Ma, Stress distribution in a ring subjected internally to a pair of eccentrically applied point loads, Int. J. Press. Vessels Pip., **58** (1994) 59-64.

[20] S. Vigdergauz, An effective method for computing the elastic field in a finite cracked disk, Eng. Fract. Mech., **53** (1996) 545-556.

[21] X. Zhang, N. Hasebe, Stress intensity factors of a crack in a composedcircular cylinder, Int. J. Solids Struct., **36** (1999) 3779-3797.

[22] C.F. Markides, D.N. Pazis, S.K. Kourkoulis, Stress intensity factors for the Brazilian disc with a short central crack: Opening versus closing cracks, Appl. Math. Modell., **35** (2011) 5636-5651.

[23] H.F. Bueckner, Novel principle for the computation of stress intensity factors, Zeitschrift fuer Angewandte Mathematik & Mechanik, **50** (1970).

[24] C.P. Andrasic, A.P. Parker, Dimensionless stress intensity factors for cracked thick cylinders under polynomial crack face loadings, Eng. Fract. Mech., **19** (1984) 187-193.

[25] G.A. Schneider, R. Danzer, Calculation of the stress intensity factor of an edge crack in a finite elastic disc using the weight function method, Eng. Fract. Mech., **34** (1989) 547-552.

[26] X.R. Wu, The arbitrarily loaded single-edge cracked circular disc; accurate weight function solutions, Int. J. Fract., **49** (1991) 239-256.

[27] T. Fett, A semi-analytical study of the edge-cracked circular disc by use of the boundary collocation method, Eng. Fract. Mech., **56** (1997) 331-346.

[28] S. Dong, Y. Wang, Y. Xia, Stress intensity factors for central cracked circular disk subjected to compression, Eng. Fract. Mech., **71** (2004) 1135-1148.

[29] A.-j. Chen, W.-j. Zeng, Weight function for stress intensity factors in rotating thick-walled cylinder, Appl. Math. Mech., **27** (2006) 29-35.

[30] C. Aijun, Study on dynamic stress intensity factors of disk with a radial edge crack subjected to external impulsive pressure, Acta Mech. Solida Sin., **20** (2007) 41-49.

[31] A. Chen, L. Liao, D. Zhang, Analysis of dynamic stress intensity factors of thick-walled cylinder under internal impulsive pressure, Acta Mech. Sin., **25** (2009) 803-809.

[32] R.N.L. Smith, Stress intensity factors for an ARC crack in a rotating disc, Eng. Fract. Mech., **21** (1985) 579-587.

[33] M. Perl, R. Arone, Stress intensity factors for large arrays of radial cracks in thick-walled steel cylinders, Eng. Fract. Mech., **25** (1986) 341-348.

[34] H.M. Shu, J. Petit, G. Bezine, Stress intensity factors for radial cracks in thick walled cylinders—I. Symmetrical cracks, Eng. Fract. Mech., **49** (1994) 611-623.

[35] H.M. Shu, J. Petit, G. Bezine, Stress intensity factors for radial cracks in thick walled cylinders—II. Combination of autofrettage and internal pressure, Eng. Fract. Mech., **49** (1994) 625-629.

[36] H.M. Shu, J. Petit, G. Bezine, Stress intensity factors for radial cracks in thick walled cylinders—III. Asymmetrical cracks, Eng. Fract. Mech., **49** (1994) 839-847.

[37] K.J. Kirkhope, R. Bell, J. Kirkhope, Stress intensity factor equations for single and multiple cracked pressurized thick-walled cylinders, Int. J. Press. Vessels Pip., **41** (1990) 103-111.

[38] R.L. Wilson, S.A. Meguid, On the determination of mixed mode stress intensity factors of an angled crack in a disc using FEM, Finite Elem. Anal. Des., **18** (1995) 433-448.

[39] K. Ramesh, S. Shukla, P. Dixit, N. Karuppaiah, Numerical evaluation of sif for radial cracks in thick annular ring using cyclic symmetry, Eng. Fract. Mech., **56** (1997) 141-153.

[40] H. Neuber, Theory of notch stresses: Principles for exact stress calculation, JW Edwards1946.

[41] F.I. Baratta, Stress intensity factors for internal multiple cracks in thick-walled cylinders stressed by internal pressure using load relief factors, Eng. Fract. Mech., **10** (1978) 691-697.

[42] A. Parker, J. Farrow, Stress intensity factors for multiple radial cracks emanating from the bore of an autofrettaged or thermally stressed, thick cylinder, Eng. Fract. Mech., **14** (1981) 237-241.

[43] R. J. Tang and K. Wang, On the Griffith crack whose surfaces are loaded asymmetrically, Eng. Fract. Mech., **16** (1982) 47-54.

[44] J. Tweed, S.C. Das, D.P. Rooke, D.P. Rooke, The stress intensity factors of a radial crack in a finite elastic disc, Int. J. Eng. Sci., **10** (1972) 323-335.

[45] D.P. Rooke, J. Tweed, Stress intensity factors for periodic radial cracks in a rotating disc, Int. J. Eng. Sci., **26** (1988) 1059-1069.

[46] A.A. Sukere, The stress intensity factors of internal radial cracks in rotating disks by the method of caustics, Eng. Fract. Mech., **26** (1987) 65-74.

[47] A.D.A. Kazemi, N.S. Murthy, N.G. Raju, Stress intensity factor determination of radially cracked circular rings subjected to tension using photoelastic technique, Eng. Fract. Mech., **32** (1989) 403-408.

[48] K. Badarinarayana, K.S.S. Aradhya, On the investigation of singular stress field around radial cracks in annulii subjected to diametrical tension, Eng. Fract. Mech., **33** (1989) 437-443.

[49] D.P. Rooke, J. Tweed, The stress intensity factors of a radial crack in a point loaded disc, Int. J. Eng. Sci., **11** (1973) 285-290.

[50] R. Gregory, The spinning circular disc with a radial edge crack; an exact solution, Int. J. Fract., **41** (1989) 39-50.

[51] C. Weili, I. Finnie, Stress intensity factors for radial cracks in circular cylinders and other simply closed cylindrical bodies, Eng. Fract. Mech., **32** (1989) 767-774.

[52] M.H. Sadd, Elasticity: Theory, Applications, and Numerics, Elsevier Science, 2009.

[53] S.G. Lekhnitskii, Theory of Elasticity of an Anisotropic Elastic Body, Holden-Day, San Francisco, 1963.

[54] D.A. Hills, P.A. Kelly, D.N. Dai, A.M. Korsunsky, Solution of Crack Problems: The Distributed Dislocation Technique, Springer Netherlands, 2013.

[55] H. Liebowitz, Fracture Mechanics, Academic Press, New York, 1968.

[56] R.T. Faal, S.J. Fariborz, Stress analysis of orthotropic planes weakened by cracks, Appl. Math. Modell., **31** (2007) 1133-1148.

[57] R.T. Faal, S.J. Fariborz, H.R. Daghyani, Antiplane deformation of orthotropic strips with multiple defects, J. Mech. Mater. Struct., **1** (2006) 1097-1114.

[58] G.C. Sih, P.C. Paris, F. Erdogan, Crack-tip, stress-intensity factors for plane extension and plate bending problems, J. Appl. Mech., **29** (1962) 306-312.

[59] David E. Kretschmann, Mechanical Properties of Wood, General Technical Report FPL–GTR–190, 2010.

Appendix

$$
e_{2}=E \frac{b_{\theta}}{a}\left(\frac{R_{1}{ }^{3-\sqrt{\beta}}-a^{2} R_{2}{ }^{1-\sqrt{\beta}}}{{R_{2}}^{2}-{R_{1}}^{2}}\right) \tag{A.1}
$$

$$
e_{3}=E \frac{b_{\theta}}{a}\left(R_{1} R_{2}\right)^{2}\left(\frac{a^{2} R_{2}{ }^{-1-\sqrt{\beta}}-R_{1}{ }^{1-\sqrt{\beta}}}{{R_{2}}^{2}-{R_{1}}^{2}}\right)
$$

$$
e_{11}=E \frac{b_{\theta}}{2\left(a R_{2}\right)^{2}} \frac{R_{1}{ }^{\sqrt{1+\alpha+\beta}+2}{R_{2}}^{2}-R_{2}{ }^{\sqrt{1+\alpha+\beta}} a^{2}\left(3 a^{2}-2{R_{2}}^{2}\right)}{{R_{2}}^{2 \sqrt{1+\alpha+\beta}}-{R_{1}}^{2 \sqrt{1+\alpha+\beta}}}
$$

$$
e_{21}=E \frac{b_{\theta}}{2\left(a R_{2}\right)^{2}}\left(R_{1} R_{2}\right)^{\sqrt{1+\alpha+\beta}} \frac{R_{2}{ }^{2+\sqrt{1+\alpha+\beta}}{R_{1}}^{2}-R_{1}{ }^{\sqrt{1+\alpha+\beta}} a^{2}\left(3 a^{2}-2{R_{2}}^{2}\right)}{{R_{2}}^{2 \sqrt{1+\alpha+\beta}}-{R_{1}}^{2 \sqrt{1+\alpha+\beta}}}
$$

$$
f_{11}=E \frac{b_{r}}{2\left(a R_{2}\right)^{2}} \frac{R_{1}{ }^{2+\sqrt{1+\alpha+\beta}}{R_{2}}^{2}+R_{2}{ }^{\sqrt{1+\alpha+\beta}} a^{2}\left(a^{2}-2{R_{2}}^{2}\right)}{{R_{2}}^{2 \sqrt{1+\alpha+\beta}}-{R_{1}}^{2 \sqrt{1+\alpha+\beta}}}
$$

$$
f_{21}=E \frac{b_{r}}{2\left(a R_{2}\right)^{2}}\left(R_{1} R_{2}\right)^{\sqrt{1+\alpha+\beta}} \frac{R_{2}{ }^{2+\sqrt{1+\alpha+\beta}}{R_{1}}^{2}+R_{1}{ }^{\sqrt{1+\alpha+\beta}} a^{2}\left(a^{2}-2{R_{2}}^{2}\right)}{{R_{2}}^{2 \sqrt{1+\alpha+\beta}}-{R_{1}}^{2 \sqrt{1+\alpha+\beta}}}
$$

$$
\begin{aligned}
a_{1 n} & =-E \frac{b_{\theta}}{a \Delta}\left\{\Delta_{11} R_{2} C_{n}(a) / n+\Delta_{12} \frac{R_{2}}{\left(1-n^{2}\right)}\left[D_{n}(a)-C_{n}(a) / n\right]\right. \\
& \left.+\Delta_{13} R_{1} A_{n}(a) / n+\Delta_{14} \frac{R_{1}}{\left(1-n^{2}\right)}\left[B_{n}(a)-A_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
a_{2 n} & =-E \frac{b_{\theta}}{a \Delta}\left\{\Delta_{21} R_{2} C_{n}(a) / n+\Delta_{22} \frac{R_{2}}{\left(1-n^{2}\right)}\left[D_{n}(a)-C_{n}(a) / n\right]\right. \\
& \left.+\Delta_{23} R_{1} A_{n}(a) / n+\Delta_{24} \frac{R_{1}}{\left(1-n^{2}\right)}\left[B_{n}(a)-A_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
a_{3 n} & =-E \frac{b_{\theta}}{a \Delta}\left\{\Delta_{31} R_{2} C_{n}(a) / n+\Delta_{32} \frac{R_{2}}{\left(1-n^{2}\right)}\left[D_{n}(a)-C_{n}(a) / n\right]\right. \\
& \left.+\Delta_{33} R_{1} A_{n}(a) / n+\Delta_{34} \frac{R_{1}}{\left(1-n^{2}\right)}\left[B_{n}(a)-A_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
a_{4 n} & =-E \frac{b_{\theta}}{a \Delta}\left\{\Delta_{41} R_{2} C_{n}(a) / n+\Delta_{42} \frac{R_{2}}{\left(1-n^{2}\right)}\left[D_{n}(a)-C_{n}(a) / n\right]\right. \\
& \left.+\Delta_{43} R_{1} A_{n}(a) / n+\Delta_{44} \frac{R_{1}}{\left(1-n^{2}\right)}\left[B_{n}(a)-A_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
b_{1 n} & =-E \frac{b_{r}}{a \Delta}\left\{-\Delta_{11} R_{2} \bar{C}_{n}(a) / n+\Delta_{12} \frac{R_{2}}{\left(1-n^{2}\right)}\left[\bar{D}_{n}(a)+\bar{C}_{n}(a) / n\right]\right. \\
& \left.-\Delta_{13} R_{1} \bar{A}_{n}(a) / n+\Delta_{14} \frac{R_{1}}{\left(1-n^{2}\right)}\left[\bar{B}_{n}(a)+\bar{A}_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
b_{2 n} & =-E \frac{b_{r}}{a \Delta}\left\{-\Delta_{21} R_{2} \bar{C}_{n}(a) / n+\Delta_{22} \frac{R_{2}}{\left(1-n^{2}\right)}\left[\bar{D}_{n}(a)+\bar{C}_{n}(a) / n\right]\right. \\
& \left.-\Delta_{23} R_{1} \bar{A}_{n}(a) / n+\Delta_{24} \frac{R_{1}}{\left(1-n^{2}\right)}\left[\bar{B}_{n}(a)+\bar{A}_{n}(a) / n\right]\right\}
\end{aligned}
$$

$$
b_{3 n}=-E \frac{b_{r}}{a \Delta}\left\{-\Delta_{31} R_{2} \bar{C}_{n}(a) / n+\Delta_{32} \frac{R_{2}}{\left(1-n^{2}\right)}\left[\bar{D}_{n}(a)+\bar{C}_{n}(a) / n\right]\right.
$$

$$-\Delta_{33} R_{1} \bar{A}_{n}(a) / n+\Delta_{34} \frac{R_{1}}{\left(1-n^{2}\right)}\left[\bar{B}_{n}(a)+\bar{A}_{n}(a) / n\right]\}$$

$$b_{4 n}=-E \frac{b_{r}}{a \Delta}\left\{-\Delta_{41} R_{2} \bar{C}_{n} / n+\Delta_{42} \frac{R_{2}}{\left(1-n^{2}\right)}\left[\bar{D}_{n}(a)+\bar{C}_{n}(a) / n\right]\right.$$

$$-\Delta_{43} R_{1} \bar{A}_{n}(a) / n+\Delta_{44} \frac{R_{1}}{\left(1-n^{2}\right)}\left[\bar{B}_{n}(a)+\bar{A}_{n}(a) / n\right]\}$$

where $\Delta_{i j}, i, j=1,2,3,4$ and $\Delta$ are given as below

$$
\begin{aligned}
\Delta_{11}=&\left(d_{2 n}-d_{3 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{2 n}+d_{3 n}}+\left(d_{4 n}-d_{2 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{2 n}+d_{4 n}} \\
+&\left(d_{3 n}-d_{4 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{12}=& d_{4 n}\left(d_{3 n}-d_{2 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{2 n}+d_{3 n}}+d_{3 n}\left(d_{2 n}-d_{4 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{2 n}+d_{4 n}} \\
+& d_{2 n}\left(d_{4 n}-d_{3 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{13}=&\left(d_{2 n}-d_{3 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{2 n}+d_{3 n}}+\left(d_{4 n}-d_{2 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{2 n}+d_{4 n}} \\
+&\left(d_{3 n}-d_{4 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{14}=& d_{4 n}\left(d_{3 n}-d_{2 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{2 n}+d_{3 n}}+d_{3 n}\left(d_{2 n}-d_{4 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{2 n}+d_{4 n}} \\
+& d_{2 n}\left(d_{4 n}-d_{3 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{21}=&\left(d_{3 n}-d_{1 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{1 n}+d_{3 n}}+\left(d_{1 n}-d_{4 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{1 n}+d_{4 n}} \\
+&\left(d_{4 n}-d_{3 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{22}=& d_{4 n}\left(d_{1 n}-d_{3 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{1 n}+d_{3 n}}+d_{3 n}\left(d_{4 n}-d_{1 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{1 n}+d_{4 n}} \\
+& d_{1 n}\left(d_{3 n}-d_{4 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{23}=&\left(d_{3 n}-d_{1 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{1 n}+d_{3 n}}+\left(d_{1 n}-d_{4 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{1 n}+d_{4 n}} \\
+&\left(d_{4 n}-d_{3 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{24}=& d_{4 n}\left(d_{1 n}-d_{3 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{1 n}+d_{3 n}}+d_{3 n}\left(d_{4 n}-d_{1 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{1 n}+d_{4 n}} \\
+& d_{1 n}\left(d_{3 n}-d_{4 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{3 n}+d_{4 n}} \\
\Delta_{31}=&\left(d_{1 n}-d_{2 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{1 n}+d_{2 n}}+\left(d_{2 n}-d_{4 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{2 n}+d_{4 n}} \\
+&\left(d_{4 n}-d_{1 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{1 n}+d_{4 n}} \\
\Delta_{32}=& d_{4 n}\left(d_{2 n}-d_{1 n}\right) R_{2}{ }^{d_{4 n}} R_{1}{ }^{d_{2 n}+d_{1 n}}+d_{2 n}\left(d_{1 n}-d_{4 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{1 n}+d_{4 n}} \\
+& d_{1 n}\left(d_{4 n}-d_{2 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{2 n}+d_{4 n}} \\
\Delta_{33}=&\left(d_{1 n}-d_{2 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{1 n}+d_{2 n}}+\left(d_{4 n}-d_{1 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{1 n}+d_{4 n}} \\
+&\left(d_{2 n}-d_{4 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{2 n}+d_{4 n}} \\
\Delta_{34}=& d_{4 n}\left(d_{2 n}-d_{1 n}\right) R_{1}{ }^{d_{4 n}} R_{2}{ }^{d_{1 n}+d_{2 n}}+d_{2 n}\left(d_{1 n}-d_{4 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{1 n}+d_{4 n}} \\
+& d_{1 n}\left(d_{4 n}-d_{2 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{2 n}+d_{4 n}} \\
\Delta_{41}=&\left(d_{2 n}-d_{1 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{1 n}+d_{2 n}}+\left(d_{3 n}-d_{2 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{2 n}+d_{3 n}} \\
+&\left(d_{1 n}-d_{3 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{3 n}+d_{1 n}} \\
\Delta_{42}=& d_{3 n}\left(d_{1 n}-d_{2 n}\right) R_{2}{ }^{d_{3 n}} R_{1}{ }^{d_{2 n}+d_{1 n}}+d_{2 n}\left(d_{3 n}-d_{1 n}\right) R_{2}{ }^{d_{2 n}} R_{1}{ }^{d_{1 n}+d_{3 n}} \\
+& d_{1 n}\left(d_{2 n}-d_{3 n}\right) R_{2}{ }^{d_{1 n}} R_{1}{ }^{d_{2 n}+d_{3 n}} \\
\Delta_{43}=&\left(d_{2 n}-d_{1 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{1 n}+d_{2 n}}+\left(d_{1 n}-d_{3 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{1 n}+d_{3 n}} \\
+&\left(d_{3 n}-d_{2 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{2 n}+d_{3 n}} \\
\Delta_{44}=& d_{3 n}\left(d_{1 n}-d_{2 n}\right) R_{1}{ }^{d_{3 n}} R_{2}{ }^{d_{1 n}+d_{2 n}}+d_{2 n}\left(d_{3 n}-d_{1 n}\right) R_{1}{ }^{d_{2 n}} R_{2}{ }^{d_{1 n}+d_{3 n}} \\
+& d_{1 n}\left(d_{2 n}-d_{3 n}\right) R_{1}{ }^{d_{1 n}} R_{2}{ }^{d_{2 n}+d_{3 n}}
\end{aligned}
\tag{A.2}
$$

$$
\Delta=\left|\begin{array}{cccc}
d_{1 n} R_{2}{ }^{d_{1 n}} & d_{2 n} R_{2}{ }^{d_{2 n}} & d_{3 n} R_{2}{ }^{d_{3 n}} & d_{4 n} R_{2}{ }^{d_{4 n}} \\
R_{2}{ }^{d_{1 n}} & R_{2}{ }^{d_{2 n}} & R_{2}{ }^{d_{3 n}} & R_{2}{ }^{d_{4 n}} \\
d_{1 n} R_{1}{ }^{d_{1 n}} & d_{2 n} R_{1}{ }^{d_{2 n}} & d_{3 n} R_{1}{ }^{d_{3 n}} & d_{4 n} R_{1}{ }^{d_{4 n}} \\
R_{1}{ }^{d_{1 n}} & R_{1}{ }^{d_{2 n}} & R_{1}{ }^{d_{3 n}} & R_{1}{ }^{d_{4 n}}
\end{array}\right|
$$

![](./images/813128915533955072_2.jpg)

![](./images/813128915533955072_3.jpg)

![](./images/813128915533955072_4.jpg)

![](./images/813128915533955072_5.jpg)

![](./images/813128915533955072_6.jpg)

![](./images/813128915533955072_7.jpg)

![](./images/813128915533955072_8.jpg)

![](./images/813128915533955072_9.jpg)

Table 1. Normalized stress intensity factor for a radial embedded crack ($c \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta\theta}(r, 0) = -\sigma_0$

$$
\left(\frac{d-c}{R_2-R_1}=0.5, \frac{c-R_1}{R_2-d}=1, k_0=\sigma_0 \sqrt{\frac{d-c}{2}}\right)
$$

<table>
  <thead>
    <tr>
      <th>$\frac{R_1}{R_2-R_1}$</th>
      <th>Present study $k_i/k_0$</th>
      <th>Present study $k_o/k_0$</th>
      <th>[1] $k_i/k_0$</th>
      <th>[1] $k_o/k_0$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.05</td>
      <td>1.1477</td>
      <td>1.2046</td>
      <td>1.1477</td>
      <td>1.2046</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1.1498</td>
      <td>1.2030</td>
      <td>1.1498</td>
      <td>1.2030</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>1.1580</td>
      <td>1.2018</td>
      <td>1.1580</td>
      <td>1.2018</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>1.1664</td>
      <td>1.2007</td>
      <td>1.1664</td>
      <td>1.2007</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.1736</td>
      <td>1.1980</td>
      <td>1.1736</td>
      <td>1.1980</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.1788</td>
      <td>1.1943</td>
      <td>1.1788</td>
      <td>1.1943</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.1809</td>
      <td>1.1923</td>
      <td>1.1810</td>
      <td>1.1923</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.1822</td>
      <td>1.1911</td>
      <td>1.1822</td>
      <td>1.1911</td>
    </tr>
  </tbody>
</table>

Table 2. Normalized stress intensity factor for a radial embedded crack ($c \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{r\theta}(r, 0) = -\tau_0$

$$
\left(\frac{d-c}{R_2-R_1}=0.5, \frac{c-R_1}{R_2-d}=1, k_0=\tau_0 \sqrt{\frac{d-c}{2}}\right)
$$

<table>
  <thead>
    <tr>
      <th>$\frac{R_1}{R_2-R_1}$</th>
      <th>Present study $k_i/k_0$</th>
      <th>Present study $k_o/k_0$</th>
      <th>[10] $k_i/k_0$</th>
      <th>[10] $k_o/k_0$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.05</td>
      <td>1.1024</td>
      <td>1.1403</td>
      <td>1.102403</td>
      <td>1.140259</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1.1130</td>
      <td>1.1439</td>
      <td>1.112981</td>
      <td>1.143946</td>
    </tr>
    <tr>
      <td>0.25</td>
      <td>1.1437</td>
      <td>1.1581</td>
      <td>1.143672</td>
      <td>1.158068</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>1.1730</td>
      <td>1.1753</td>
      <td>1.172981</td>
      <td>1.175292</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.1931</td>
      <td>1.1903</td>
      <td>1.193131</td>
      <td>1.190321</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.2010</td>
      <td>1.1981</td>
      <td>1.200979</td>
      <td>1.198131</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1.2024</td>
      <td>1.2002</td>
      <td>1.202374</td>
      <td>1.200159</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1.2027</td>
      <td>1.2009</td>
      <td>1.202751</td>
      <td>1.200981</td>
    </tr>
    <tr>
      <td>5</td>
      <td>1.2029</td>
      <td>1.2014</td>
      <td>1.202869</td>
      <td>1.201402</td>
    </tr>
  </tbody>
</table>

Table 3. Normalized stress intensity factor ($k_I/k_0$) for a radial inner edge crack ($R_1 \leq r \leq d$) in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta\theta}(r, 0) = -\sigma_0$

$$k_0 = \sigma_0\sqrt{d-R_1}$$

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">$\frac{R_1}{R_2-R_1}$</th>
    </tr>
    <tr>
      <th></th>
      <th>0.1</th>
      <th>$\frac{1}{3}$</th>
      <th>$\frac{1}{2}$</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Present study</td>
      <td>0.1</td>
      <td>1.1694</td>
      <td>1.1605</td>
      <td>1.1543</td>
      <td>1.1572</td>
      <td>1.1583</td>
    </tr>
  </tbody>
</table>

<div>
<table>
<tbody>
<tr>
<td rowspan="12">
$\dfrac{d - R_1}{R_2 - R_1}$
</td>
<td>[1]</td>
<td>0.1</td>
<td>1.153</td>
<td>1.155</td>
<td>1.157</td>
<td>1.159</td>
<td>1.167</td>
</tr>
<tr>
<td>Present study</td>
<td>0.2</td>
<td>1.2321</td>
<td>1.2324</td>
<td>1.2486</td>
<td>1.2786</td>
<td>1.2959</td>
</tr>
<tr>
<td>[1]</td>
<td>0.2</td>
<td>1.218</td>
<td>1.229</td>
<td>1.247</td>
<td>1.277</td>
<td>1.299</td>
</tr>
<tr>
<td>Present study</td>
<td>0.3</td>
<td>1.3010</td>
<td>1.3151</td>
<td>1.3690</td>
<td>1.4476</td>
<td>1.4927</td>
</tr>
<tr>
<td>[1]</td>
<td>0.3</td>
<td>1.295</td>
<td>1.310</td>
<td>1.366</td>
<td>1.449</td>
<td>1.493</td>
</tr>
<tr>
<td>Present study</td>
<td>0.4</td>
<td>1.3805</td>
<td>1.4092</td>
<td>1.5087</td>
<td>1.6581</td>
<td>1.7489</td>
</tr>
<tr>
<td>[1]</td>
<td>0.4</td>
<td>1.373</td>
<td>1.402</td>
<td>1.503</td>
<td>1.655</td>
<td>1.747</td>
</tr>
<tr>
<td>Present study</td>
<td>0.5</td>
<td>1.4753</td>
<td>1.5182</td>
<td>1.6667</td>
<td>1.9072</td>
<td>2.0671</td>
</tr>
<tr>
<td>[1]</td>
<td>0.5</td>
<td>1.465</td>
<td>1.508</td>
<td>1.658</td>
<td>1.901</td>
<td>2.066</td>
</tr>
<tr>
<td>Present study</td>
<td>0.6</td>
<td>1.5928</td>
<td>1.6484</td>
<td>1.8446</td>
<td>2.1905</td>
<td>2.4453</td>
</tr>
<tr>
<td>[1]</td>
<td>0.6</td>
<td>1.578</td>
<td>1.635</td>
<td>1.830</td>
<td>2.177</td>
<td>2.441</td>
</tr>
<tr>
<td>Present study</td>
<td>0.7</td>
<td>1.7486</td>
<td>1.8145</td>
<td>2.0505</td>
<td>2.4998</td>
<td>2.8671</td>
</tr>
<tr>
<td>
</td>
<td>[1]</td>
<td>0.7</td>
<td>1.730</td>
<td>1.796</td>
<td>2.030</td>
<td>2.475</td>
<td>2.851</td>
</tr>
</tbody>
</table>
</div>

Table 4. Normalized stress intensity factor $(k_{II}/k_0)$ for a radial inner edge crack $(R_1 \leq r \leq d)$ in a hollow cylinder or a disk subjected to uniform crack surface pressure $\sigma_{r\theta}(r, 0) = -\tau_0$

$$
k_0 = \tau_0\sqrt{d - R_1}
$$

<div>
<table>
<thead>
<tr>
<th>
</th>
<th>
</th>
<th>
</th>
<th colspan="4">
$\dfrac{R_1}{R_2 - R_1}$
</th>
</tr>
<tr>
<th>
</th>
<th>
</th>
<th>
</th>
<th>$\dfrac{1}{3}$</th>
<th>$\dfrac{1}{2}$</th>
<th>1</th>
<th>2</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="20">
$\dfrac{d - R_1}{R_2 - R_1}$
</td>
<td>Present study</td>
<td>0.1</td>
<td>1.1192</td>
<td>1.1207</td>
<td>1.1363</td>
<td>1.1675</td>
</tr>
<tr>
<td>[10]</td>
<td>0.1</td>
<td>1.114205</td>
<td>1.113084</td>
<td>1.112207</td>
<td>*</td>
</tr>
<tr>
<td>Present study</td>
<td>0.2</td>
<td>1.1424</td>
<td>1.1286</td>
<td>1.1267</td>
<td>1.1425</td>
</tr>
<tr>
<td>[10]</td>
<td>0.2</td>
<td>1.137115</td>
<td>1.123781</td>
<td>1.119115</td>
<td>1.117818</td>
</tr>
<tr>
<td>Present study</td>
<td>0.3</td>
<td>1.1904</td>
<td>1.1644</td>
<td>1.1461</td>
<td>1.1519</td>
</tr>
<tr>
<td>[10]</td>
<td>0.3</td>
<td>1.184718</td>
<td>1.159126</td>
<td>1.141009</td>
<td>1.136173</td>
</tr>
<tr>
<td>Present study</td>
<td>0.4</td>
<td>1.2592</td>
<td>1.2249</td>
<td>1.1926</td>
<td>1.1889</td>
</tr>
<tr>
<td>[10]</td>
<td>0.4</td>
<td>1.253483</td>
<td>1.219228</td>
<td>1.187572</td>
<td>1.180698</td>
</tr>
<tr>
<td>Present study</td>
<td>0.5</td>
<td>1.3538</td>
<td>1.3140</td>
<td>1.2708</td>
<td>1.2584</td>
</tr>
<tr>
<td>[10]</td>
<td>0.5</td>
<td>1.347864</td>
<td>1.308061</td>
<td>1.265209</td>
<td>1.252182</td>
</tr>
<tr>
<td>Present study</td>
<td>0.6</td>
<td>1.4872</td>
<td>1.4434</td>
<td>1.3920</td>
<td>1.3727</td>
</tr>
<tr>
<td>[10]</td>
<td>0.6</td>
<td>1.480665</td>
<td>1.437068</td>
<td>1.385657</td>
<td>1.366051</td>
</tr>
<tr>
<td>Present study</td>
<td>0.7</td>
<td>1.6880</td>
<td>1.6407</td>
<td>1.5830</td>
<td>1.5585</td>
</tr>
<tr>
<td>[10]</td>
<td>0.7</td>
<td>1.680663</td>
<td>1.633779</td>
<td>1.57550</td>
<td>1.551078</td>
</tr>
<tr>
<td>Present study</td>
<td>0.8</td>
<td>2.0326</td>
<td>1.9803</td>
<td>1.9157</td>
<td>1.8877</td>
</tr>
<tr>
<td>[10]</td>
<td>0.8</td>
<td>2.023717</td>
<td>1.972012</td>
<td>1.906569</td>
<td>1.878181</td>
</tr>
<tr>
<td>Present study</td>
<td>0.9</td>
<td>2.8257</td>
<td>2.7608</td>
<td>2.6822</td>
<td>2.6513</td>
</tr>
<tr>
<td>[10]</td>
<td>0.9</td>
<td>2.813413</td>
<td>2.749417</td>
<td>2.669403</td>
<td>2.635523</td>
</tr>
</tbody>
</table>
</div>

Table 5. Normalized stress intensity factor for a concentric arc crack in a rotating disc

<div>
<table>
<tbody>
<tr>
<td>
</td>
<td colspan="4">
$\dfrac{a}{R_2} = 0.25$
</td>
<td colspan="4">
$\dfrac{a}{R_2} = 0.5$
</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>Present<br>study<br>$k_I/k_0$</td>
<td>Present<br>study<br>$k_{II}/k_0$</td>
<td>[32]<br>$k_I/k_0$</td>
<td>[32]<br>$k_{II}/k_0$</td>
<td>Present<br>study<br>$k_I/k_0$</td>
<td>Present<br>study<br>$k_{II}/k_0$</td>
<td>[32]<br>$k_I/k_0$</td>
<td>[32]<br>$k_{II}/k_0$</td>
</tr>
</tbody>
</table>
</div>

<table>
<tbody>
<tr>
<td>15</td>
<td>0.9818</td>
<td>0.1307</td>
<td>0.963</td>
<td>0.132</td>
<td>1.0228</td>
<td>0.1480</td>
<td>1.01</td>
<td>0.148</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>0.958</td>
<td>0.136</td>
<td>
</td>
<td>
</td>
<td>1.01</td>
<td>0.154</td>
</tr>
<tr>
<td>30</td>
<td>0.9241</td>
<td>0.2571</td>
<td>0.916</td>
<td>0.259</td>
<td>1.0104</td>
<td>0.3406</td>
<td>1.00</td>
<td>0.341</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>0.913</td>
<td>0.267</td>
<td>
</td>
<td>
</td>
<td>1.00</td>
<td>0.350</td>
</tr>
<tr>
<td>45</td>
<td>0.8271</td>
<td>0.3667</td>
<td>0.825</td>
<td>0.372</td>
<td>0.8977</td>
<td>0.5143</td>
<td>0.899</td>
<td>0.520</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>0.822</td>
<td>0.383</td>
<td>
</td>
<td>
</td>
<td>0.897</td>
<td>0.531</td>
</tr>
<tr>
<td>60</td>
<td>0.7042</td>
<td>0.4470</td>
<td>0.704</td>
<td>0.457</td>
<td>0.7205</td>
<td>0.6207</td>
<td>0.728</td>
<td>0.633</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>0.703</td>
<td>0.470</td>
<td>
</td>
<td>
</td>
<td>0.729</td>
<td>0.647</td>
</tr>
<tr>
<td>75</td>
<td>0.5749</td>
<td>0.4950</td>
<td>0.578</td>
<td>0.510</td>
<td>0.5362</td>
<td>0.6626</td>
<td>0.548</td>
<td>0.682</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>0.575</td>
<td>0.525</td>
<td>
</td>
<td>
</td>
<td>0.545</td>
<td>0.698</td>
</tr>
</tbody>
</table>

Table 6. Dimensionless stress intensity factor for a concentric arc crack in an infinite plane under two remote biaxial loadings $\sigma_x = \sigma_y = \sigma_0$

$$
\frac{a}{R_2}=0.02
$$

<table>
<thead>
<tr>
<th>$\gamma$</th>
<th>Present study</th>
<th>Present study</th>
<th>[58]</th>
<th>[58]</th>
</tr>
<tr>
<th>
</th>
<th>$k_I/k_0$</th>
<th>$k_{II}/k_0$</th>
<th>$k_I/k_0$</th>
<th>$k_{II}/k_0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>15</td>
<td>0.1157</td>
<td>0.8791</td>
<td>0.1157</td>
<td>0.8790</td>
</tr>
<tr>
<td>30</td>
<td>0.3041</td>
<td>1.1346</td>
<td>0.3040</td>
<td>1.1346</td>
</tr>
<tr>
<td>45</td>
<td>0.4978</td>
<td>1.2013</td>
<td>0.4975</td>
<td>1.2011</td>
</tr>
<tr>
<td>60</td>
<td>0.6603</td>
<td>1.1429</td>
<td>0.6598</td>
<td>1.1428</td>
</tr>
<tr>
<td>75</td>
<td>0.7743</td>
<td>1.0083</td>
<td>0.7737</td>
<td>1.0083</td>
</tr>
</tbody>
</table>

Table 7. Stress intensity factor for a pair of symmetric radial cracks ($c \leq x \leq d, -d \leq x \leq -c$) in a cylinder or a disk subjected to uniform crack surface pressure $\sigma_{\theta\theta}(r, 0)=-\sigma_0=-1$ for $c=0.1$

<table>
<thead>
<tr>
<th>$d$</th>
<th>Present study</th>
<th>Present study</th>
<th>[16]</th>
<th>[16]</th>
</tr>
<tr>
<th>
</th>
<th>$k_i$</th>
<th>$k_o$</th>
<th>$k_i$</th>
<th>$k_o$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.2</td>
<td>0.2292</td>
<td>0.2280</td>
<td>0.2292</td>
<td>0.2279</td>
</tr>
<tr>
<td>0.3</td>
<td>0.3407</td>
<td>0.3336</td>
<td>0.3412</td>
<td>0.3333</td>
</tr>
<tr>
<td>0.4</td>
<td>0.4445</td>
<td>0.4258</td>
<td>0.4463</td>
<td>0.4245</td>
</tr>
<tr>
<td>0.5</td>
<td>0.5516</td>
<td>0.5152</td>
<td>0.5548</td>
<td>0.5127</td>
</tr>
<tr>
<td>0.6</td>
<td>0.6668</td>
<td>0.6076</td>
<td>0.6694</td>
<td>0.6054</td>
</tr>
<tr>
<td>0.7</td>
<td>0.7938</td>
<td>0.7113</td>
<td>0.7896</td>
<td>0.7154</td>
</tr>
<tr>
<td>0.8</td>
<td>0.9380</td>
<td>0.8459</td>
<td>0.9155</td>
<td>0.8720</td>
</tr>
<tr>
<td>0.9</td>
<td>1.1147</td>
<td>1.0859</td>
<td>1.058</td>
<td>1.173</td>
</tr>
</tbody>
</table>

Table 8. Elastic and Poisson's ratios for various species at approximately 12% moisture content (Extracted from [59])

<table>
<thead>
<tr>
<th>
</th>
<th>$E_2/E_3$</th>
<th>$E_1/E_3$</th>
<th>$G_{31}/E_3$</th>
<th>$G_{32}/E_3$</th>
<th>$G_{12}/E_3$</th>
<th>Anisotropy ratios of this study (plane stress)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Balsa</td>
<td>0.015</td>
<td>0.046</td>
<td>0.054</td>
<td>0.037</td>
<td>0.005</td>
<td>$\beta=0.3261$</td>
</tr>
<tr>
<td>(Hardwoods)</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>$\alpha=2.5663$</td>
</tr>
</tbody>
</table>

<table>
<tbody><tr><td>Douglas-fir
(Softwoods)</td>
<td>0.039</td>
<td>0.068</td>
<td>0.064</td>
<td>0.078</td>
<td>0.007</td>
<td rowspan="3">$\beta=0.5735$
$\alpha=5.1241$</td></tr>
<tr>
<td></td>
<td>$v_{31}$</td>
<td>$v_{32}$</td>
<td>$v_{12}$</td>
<td>$v_{21}$</td>
<td>$v_{13}$</td></tr>
<tr>
<td>Balsa
(Hardwoods)</td>
<td>0.229</td>
<td>0.488</td>
<td>0.665</td>
<td>0.231</td>
<td>0.018</td></tr>
<tr>
<td>Douglas-fir
(Softwoods)</td>
<td>0.292</td>
<td>0.449</td>
<td>0.390</td>
<td>0.374</td>
<td>0.036</td>
<td></td></tr>
</tbody></table>

Table 9. Values of non-dimensional stress intensity factors at crack tips in terms of $\frac{l}{R_{2}-R_{1}}$ for $R_{2}=2R_{1}$ and $\frac{d}{R_{2}+R_{1}}=0.5$.

<table>
<tbody><tr><td>$\frac{l}{R_{2}-R_{1}}$</td>
<td>Balsa
$k_{I}/k_{0}$</td>
<td>Isotopic
$k_{I}/k_{0}$</td>
<td>Douglas-fir
$k_{I}/k_{0}$</td>
<td>Balsa
$k_{II}/k_{0}$</td>
<td>Isotopic
$k_{II}/k_{0}$</td>
<td>Douglas-fir
$k_{II}/k_{0}$</td></tr>
<tr>
<td>0.02</td>
<td>0.2216</td>
<td>0.2630</td>
<td>0.3112</td>
<td>0.2070</td>
<td>0.2419</td>
<td>0.2878</td></tr>
<tr>
<td>0.07</td>
<td>0.4408</td>
<td>0.5256</td>
<td>0.6189</td>
<td>0.4008</td>
<td>0.4607</td>
<td>0.5549</td></tr>
<tr>
<td>0.12</td>
<td>0.6112</td>
<td>0.7334</td>
<td>0.8591</td>
<td>0.5626</td>
<td>0.6320</td>
<td>0.7741</td></tr>
<tr>
<td>0.17</td>
<td>0.7627</td>
<td>0.9216</td>
<td>1.0747</td>
<td>0.7323</td>
<td>0.8055</td>
<td>1.0013</td></tr>
<tr>
<td>0.22</td>
<td>0.8999</td>
<td>1.0939</td>
<td>1.2725</td>
<td>0.9167</td>
<td>0.9923</td>
<td>1.2463</td></tr>
<tr>
<td>0.27</td>
<td>1.0248</td>
<td>1.2516</td>
<td>1.4548</td>
<td>1.1158</td>
<td>1.1937</td>
<td>1.5099</td></tr>
<tr>
<td>0.32</td>
<td>1.1398</td>
<td>1.3976</td>
<td>1.6243</td>
<td>1.3288</td>
<td>1.4089</td>
<td>1.7916</td></tr>
<tr>
<td>0.37</td>
<td>1.2481</td>
<td>1.5364</td>
<td>1.7847</td>
<td>1.5563</td>
<td>1.6377</td>
<td>2.0923</td></tr>
</tbody></table>

Table 10. Values of non-dimensional stress intensity factors at crack tips in terms of $d/(R_{2}-$
$R_{1})$ for $R_{2}=2R_{1}$ and $l=0.3(R_{2}-R_{1})$.

<table>
<tbody><tr><td>$\frac{d}{R_{2}-R_{1}}$</td>
<td>Balsa
$k_{I}/k_{0}$</td>
<td>Isotopic
$k_{I}/k_{0}$</td>
<td>Douglas-fir
$k_{I}/k_{0}$</td>
<td>Balsa
$k_{II}/k_{0}$</td>
<td>Isotopic
$k_{II}/k_{0}$</td>
<td>Douglas-fir
$k_{II}/k_{0}$</td></tr>
<tr>
<td>1.2</td>
<td>2.5299</td>
<td>2.4738</td>
<td>3.2776</td>
<td>3.0826</td>
<td>3.1653</td>
<td>4.0274</td></tr>
<tr>
<td>1.25</td>
<td>2.2276</td>
<td>2.2546</td>
<td>2.9319</td>
<td>2.6538</td>
<td>2.7454</td>
<td>3.4924</td></tr>
<tr>
<td>1.3</td>
<td>1.9635</td>
<td>2.0604</td>
<td>2.6266</td>
<td>2.3059</td>
<td>2.4022</td>
<td>3.0535</td></tr>
<tr>
<td>1.35</td>
<td>1.7336</td>
<td>1.8887</td>
<td>2.3573</td>
<td>2.016</td>
<td>2.1135</td>
<td>2.6844</td></tr>
<tr>
<td>1.4</td>
<td>1.5344</td>
<td>1.7373</td>
<td>2.1202</td>
<td>1.7702</td>
<td>1.8663</td>
<td>2.3690</td></tr>
<tr>
<td>1.45</td>
<td>1.3627</td>
<td>1.6044</td>
<td>1.912</td>
<td>1.5598</td>
<td>1.6526</td>
<td>2.0972</td></tr>
<tr>
<td>1.5</td>
<td>1.2158</td>
<td>1.4886</td>
<td>1.7301</td>
<td>1.3792</td>
<td>1.4672</td>
<td>1.8621</td></tr>
<tr>
<td>1.55</td>
<td>1.0917</td>
<td>1.3889</td>
<td>1.5727</td>
<td>1.2248</td>
<td>1.3075</td>
<td>1.6596</td></tr>
<tr>
<td>1.6</td>
<td>0.9894</td>
<td>1.3057</td>
<td>1.4394</td>
<td>1.095</td>
<td>1.1724</td>
<td>1.4882</td></tr>
<tr>
<td>1.65</td>
<td>0.9099</td>
<td>1.2416</td>
<td>1.3321</td>
<td>0.9906</td>
<td>1.0637</td>
<td>1.3494</td></tr>
<tr>
<td>1.7</td>
<td>0.8599</td>
<td>1.2068</td>
<td>1.2605</td>
<td>0.9173</td>
<td>0.9886</td>
<td>1.2518</td></tr>
</tbody></table>

Table 11. Values of non-dimensional stress intensity factors at crack tips in terms of
$l/(R_{2}-R_{1})$ for $R_{2}=2R_{1}$ and $R=1.5R_{1}$.

<table>
<tbody><tr><td>$\frac{l}{R_{2}-R_{1}}$</td>
<td>Balsa
$k_{I}/k_{0}$</td>
<td>Isotopic
$k_{I}/k_{0}$</td>
<td>Douglas-fir
$k_{I}/k_{0}$</td>
<td>Balsa
$k_{II}/k_{0}$</td>
<td>Isotopic
$k_{II}/k_{0}$</td>
<td>Douglas-fir
$k_{II}/k_{0}$</td></tr>
<tr>
<td>0.0052</td>
<td>4.333e-5</td>
<td>4.8001e-5</td>
<td>5.8385e-5</td>
<td>0.0216</td>
<td>0.0324</td>
<td>0.0323</td></tr>
</tbody></table>

0.0528
0.1052
0.1576
0.2099
0.2623
0.3146
0.3670
0.4194
0.4717
0.0433
0.1173
0.2034
0.2925
0.3792
0.4598
0.5320
0.5949
0.6496
0.0487
0.1369
0.2511
0.3863
0.5388
0.7058
0.8846
1.0725
1.2667
0.0587
0.1609
0.2848
0.4209
0.5638
0.7096
0.8553
0.9989
1.1396
0.2261
0.3528
0.4935
0.6574
0.8476
1.0673
1.3192
1.6036
1.9178
0.3331
0.4993
0.6671
0.8532
1.0618
1.2925
1.5425
1.8069
2.0796
0.3373
0.5229
0.7241
0.9519
1.2075
1.4915
1.8039
2.1412
2.4972

Table 12. Values of non-dimensional stress intensity factors at crack tips in terms of
$l/(R_2-R_1)$ for $R_2=2R_1$ and $R=1.5R_1$.

<table>
<thead>
<tr>
<th>$\frac{l}{R_2-R_1}$</th>
<th>Balsa<br>$k_{Io1}/k_0$</th>
<th>Isotopic<br>$k_{Io1}/k_0$</th>
<th>Douglas-fir<br>$k_{Io1}/k_0$</th>
<th>Balsa<br>$k_{IIi1}/k_0$</th>
<th>Isotopic<br>$k_{IIi1}/k_0$</th>
<th>Douglas-fir<br>$k_{IIIi1}/k_0$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.01</td>
<td>0.5474</td>
<td>1.0046</td>
<td>0.9654</td>
<td>0.5377</td>
<td>0.9921</td>
<td>0.9508</td>
</tr>
<tr>
<td>0.06</td>
<td>1.4147</td>
<td>2.5622</td>
<td>2.4764</td>
<td>1.2713</td>
<td>2.3789</td>
<td>2.2606</td>
</tr>
<tr>
<td>0.11</td>
<td>2.0454</td>
<td>3.6612</td>
<td>3.5507</td>
<td>1.6866</td>
<td>3.2002</td>
<td>3.0096</td>
</tr>
<tr>
<td>0.16</td>
<td>2.6666</td>
<td>4.7260</td>
<td>4.5891</td>
<td>2.0292</td>
<td>3.8999</td>
<td>3.6243</td>
</tr>
<tr>
<td>0.21</td>
<td>3.3477</td>
<td>5.8868</td>
<td>5.7116</td>
<td>2.3718</td>
<td>4.6068</td>
<td>4.2267</td>
</tr>
<tr>
<td>0.26</td>
<td>4.1503</td>
<td>7.2583</td>
<td>7.0227</td>
<td>2.7721</td>
<td>5.4235</td>
<td>4.9117</td>
</tr>
<tr>
<td>0.31</td>
<td>5.1635</td>
<td>9.0059</td>
<td>8.6724</td>
<td>3.3087</td>
<td>6.4906</td>
<td>5.8073</td>
</tr>
<tr>
<td>0.36</td>
<td>6.5580</td>
<td>11.446</td>
<td>10.950</td>
<td>4.1333</td>
<td>8.0809</td>
<td>7.1619</td>
</tr>
</tbody>
</table>

**Highlights**

Michell solution is generalized for material of cylindrical anisotropy.

New analytical dislocation solution in an annular orthotropic plane is developed.

Material anisotropy has an efficient effect on stress intensity factors.

The curvature of curved cracks implies that mixed-mode analysis is essential.