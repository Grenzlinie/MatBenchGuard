Author's Accepted Manuscript

Analysis of cracked bars with rectangular cross-section and isotropic coating layer under torsion

A.R. Hassani, M.M. Monfared

![](./images/811035415069851649_1.jpg)
www.elsevier.com/locate/ijmecsci

PII:
S0020-7403(17)30150-9
DOI:
http://dx.doi.org/10.1016/j.ijmecsci.2017.04.005
Reference:
MS3652

To appear in: International Journal of Mechanical Sciences

Received date: 17 January 2017
Revised date: 13 March 2017
Accepted date: 7 April 2017

Cite this article as: A.R. Hassani and M.M. Monfared, Analysis of cracked bars with rectangular cross-section and isotropic coating layer under torsion, International Journal of Mechanical Sciences
http://dx.doi.org/10.1016/j.ijmecsci.2017.04.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting galley proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Analysis of cracked bars with rectangular cross-section and isotropic coating layer under torsion

A. R. Hassani $^{1,*}$, M. M. Monfared$^{2}$

$^{1}$Young Researchers and Elite Club, Hashtgerd Branch, Islamic Azad University, Alborz, Iran.

$^{2}$Department of Mechanical Engineering, Hashtgerd Branch, Islamic Azad University, P.O. Box 33615-178, Alborz, Iran.

*Corresponding author. Tel.: +98 26 442 0163. ahassani1111@gmail.com

## Abstract
The solution to problem of a Volterra-type screw dislocation in a rectangular cross section bar with an isotropic coating is first achieved by means of a finite Fourier cosine transform. The bar is under axial torque which is governed by Saint-Venant torsion theory. The series solution is then derived for warping function and stress fields in the rectangular cross section with an isotropic coating. The dislocation solution is employed to derive a set of Cauchy singular integral equations for the analysis of smooth cracks. The solution of these equations is used to determine the torsional rigidity of bar and the stress intensity factors for the crack tips. Finally, several examples are presented to show the accuracy and efficiency of the dislocation technique in Saint-Venant torsion problems.

## Graphical abstract
![](./images/811035415069851649_2.jpg)

**Keywords:** Rectangular cross section; Coating; Saint-Venant torsion; Stress intensity factors; Torsional rigidity; Dislocation density

### 1. Introduction

Shafts or bars in torsion are often subjected to cracking during their service life. Though the torsion problem of a bar with a rectangular cross section is a rather old one in the theory of elasticity, the effect of coating structure on the stress intensity factors in a bar with a rectangular cross section weakened by multiple cracks has not yet been adequately investigated. The problems of elastic bars under torsional loading have been considered by numerous researchers. These investigations may be grouped into two major categories: those primarily dealing with bars without any crack, and those studying bars containing single or multiple cracks. Within the first category, there are numerous investigations in the literature [1-6]. The bars weakened by cracks have been the subject of other earlier investigations.

Some researchers attempted to calculate the stress intensity factors at the crack tips and torsional rigidity in the bars with a rectangular cross section. Chen [7] analyzed a bar with a rectangular cross section weakened by two edge cracks normal to the sides of the cross section under torsional loading. The succeeding Dirichlet problem of the Laplace equation was analyzed by dividing the cross section into several sub-regions and using the Durham theorem. A solution of the torsion problem of an orthotropic rectangular bar weakened by an edge crack, bisecting and perpendicular to one boundary of the cross section was treated by Chen et al. [8]. The solution of governing equation was presented by mapping a rectangular plane with cut to another one. Chen [9] gave a solution of the torsion problem of a rectangular cross section bar with inner crack as two Dirichlet problems with the definite boundary values. The corresponding Dirichlet problems were analyzed by using the finite difference method. Hassani and Faal [10] focused on an orthotropic rectangular cross section bar with the aid of the distribution dislocation technique. The solution of a Volterra-type screw dislocation was employed for the analysis of the bar with multiple cracks.

This part of the review is related to the torsion problems of bars with a circular cross section. We begin with a study done by Chen and Wu [11], who analyzed a circular bar containing several cracks. The solution of the problem was derived with the aid of the duality between the problem of the circular plane with multiple cracks in the out of plane deformation and the problem of several cracks of the round bar under torsional loading. The complete analysis of the torsional rigidity of a solid cylinder with radial cracks was carried out by Lebedev et al. [12]. The authors investigated the problem of the twisting of an elliptical cross section containing two edge cracks extended to its foci. Wang and Tang [13] attempted to represent an analytical solution for a circular bar containing a screw dislocation. The problem was reduced to solve a singular integral equation for the unknown dislocation density. Tweed and Rooke [14] analyzed the Saint-Venant torsion problem of a circular cross section bar containing a symmetric array of edge cracks. By symmetry, the problem reduced to an integral equation to that of finding the warping functions in some sectors. Wang [15] studied problem of a thick-walled cylinder with a radial edge crack under torsional loading. An expansion for the stress function was employed so that the ensuring stresses would have the square root singularity at the crack tip. The unknown coefficients of the expansion were calculated by the boundary collocation method. The analysis of the hollow cylinder with four edge cracks normal to the inner boundary of the cylinder under torsion was the subject of a study done by Chen [16]. Sih [17] formulated the flexural and torsional problem of bars with circular, elliptical and semi-elliptical cross sections weakened by some edge and embedded cracks based on three complex flexure functions including the classical torsion function and the non-trivial stresses. Tao and Tang

[18] analyzed a bar with a circular cross section weakened by an internal crack reinforced by an eccentric rod with different material of the cylinder with the aid of the Muskhelishvili single-layer potential function solution and the single crack solution for the torsion problem of a cylinder. Hassani and Faal [19] studied problem of an orthotropic bar with a circular cross section under Saint-Venant torsion. The solution of a Volterra-type screw dislocation was first obtained with the aid of a finite Fourier cosine transform. Next, the dislocation solution was employed to derive a set of Cauchy singular integral equations for the analysis of the bar with multiple smooth cracks. The effect of the piezoelectric layer on the reduction of the mechanical stress intensity factor with the aid of the dislocation technique was treated by Hassani and Faal [20].

There is a subgroup of torsion problems dealing with bars weakened by axisymmetric cracks which are reviewed in the following. The torsion problems of a finite cylinders containing a concentric penny-shaped crack with the aid of the Hankel transform and Fourier series were developed and extended many times [21-25]. Kudriavtsev and Parton [26] focused on the problem of torsion and extension of an infinite cylinder weakened by a circumferential edge crack. Lazzarin et al. [27] achieved the closed form solution of stress fields of a semi-elliptic circumferential notch and peripheral crack in a rounded bar under torsion. Zappalorto et al. [28] presented relations for the mode III notch stress intensity factors for the circumferentially-sharply-notched rounded bars under torsional loading. Hassani et al. [29] analyzed a finite cylinder containing multiple circumferential cracks. The problem of a cracked finite bar was treated by the cutting method. That is, a cracked infinite circular bar was sliced by extending two penny shape cracks.

According to the above review, the fracture problem of the bars under torsion is an interesting problem. It is worth noting that in all the above works were limited to the bars with a particular orientation and geometry of cracks. Also, no work has been published concerning the effect of the coating on the stress intensity factor of the crack tips in the bar with rectangular cross section subjected to torsional loading. Also, to authors' knowledge, no analytical solution has been presented on the Saint-Venant torsion of a rectangular cross section bar with multiple cracks by considering the effect of the coating. In this paper, the closed form solution of the stress fields and warping functions are presented for a rectangular cross section with an isotropic coating containing a Volterra-type screw dislocation (Section 2.1). The torsional rigidity of the cracked bar with an isotropic coating is evaluated in terms of the dislocation density function (Section 2.2). The problem is reduced to a set of Cauchy singular integral equation by the distribution dislocation technique (Section 3). The numerical examples are presented in Section 4 and results are validated by employing the available results from the literature. Finally, Section 5 offers the concluding remarks.

## 2. General formulation

### 2.1 Dislocation solution

The distributed dislocation technique is an efficient means of treating multiple curved cracks with smooth geometries. However, determining stress fields due to a single dislocation in the region has been a major obstacle to the utilization of this method. Consider a rectangular cross section bar with an isotropic coating (see Fig. 1). $h_1$ refers to the width of the bar and the thickness of the coating is assumed to be $h_2$. The $x$-axis is situated at the distance $\eta$ from the lower edge of the domain under consideration. Similarly, the $y$-axis is located at the distance $\xi$ from the left side

of the cross section. As such, the cross section consists of three sub-regions with finite widths $h_1 - \eta$, $\eta$ and $h_2$ which have been attached together along the $x$-axis. The interface of rectangular cross section and its coating is considered to be perfectly bonded. The rectangular cross section bar is made of a material with shear modulus $\mu_1$ which is coated by an isotropic coating with shear modulus $\mu_2$.

![](./images/811035415069851649_3.jpg)

Fig. 1. Rectangular cross-section of a bar with an isotropic coating containing a screw dislocation

As said by Saint-Venant torsion theory, the displacement components read as [30]

$$
\begin{aligned}
u & =-\theta z y \\
v & =\theta z x \\
w & =\theta \varphi(x, y)
\end{aligned} \tag{1}
$$

in which $\theta$ is the twist angle of unit length, and $\varphi(x, y)$ represents the warping function. The out of plane displacement component $w(x, y)$ under Saint-Venant torsion is of interest. Eqs. (1) are valid in whole domain (both of bar and its coating) with same value of $\theta$. Consequently, the two nonzero stress components in the $z$ direction are

$$
\begin{aligned}
& \tau_{z x}(x, y)=\mu_1 \theta\left(\frac{\partial \varphi(x, y)}{\partial x}-y\right),-\eta<y<h_1-\eta \\
& \tau_{z y}(x, y)=\mu_1 \theta\left(\frac{\partial \varphi(x, y)}{\partial y}+x\right),-\eta<y<h_1-\eta \\
& \tau_{z x}(x, y)=\mu_2 \theta\left(\frac{\partial \varphi(x, y)}{\partial x}-y\right), h_1-\eta<y<h_1+h_2-\eta \\
& \tau_{z y}(x, y)=\mu_2 \theta\left(\frac{\partial \varphi(x, y)}{\partial y}+x\right), h_1-\eta<y<h_1+h_2-\eta
\end{aligned} \tag{2}
$$

The equilibrium equations in the absence of body forces $\frac{\partial \tau_{z x}}{\partial x}+\frac{\partial \tau_{z y}}{\partial y}=0$, in view of Eq.(2) reduce to

$$
\frac{\partial^2 \varphi(x, y)}{\partial x^2}+\frac{\partial^2 \varphi(x, y)}{\partial y^2}=0 \tag{3}
$$

Appling the finite Fourier cosine transform, $\Phi(n, y)=\int_0^a \varphi(X, y) \cos (n \pi X / a) d X$ to the above equation, in which $X=x+\xi$, (see Fig. 1) leads to

$$
\frac{d^{2} \Phi_{l}(n, y)}{d y^{2}}-(n \kappa)^{2} \Phi_{l}(n, y)+(-1)^{n} \frac{\partial \varphi_{l}(a, y)}{\partial X}-\frac{\partial \varphi_{l}(0, y)}{\partial X}=0, l=1,2,3
\tag{4}
$$

where $\kappa = \pi/a$ and the subscripts $l = 1,2,3$ are used to refer to the sub-rectangular regions of the problem. The continuity of shear stress along the $y = h_1 - \eta$ and the stress free condition on the lateral surface of the domain under consideration require that

$$
\frac{\partial \varphi_{l}(X, y)}{\partial X}-y=0 \text { at } X=0, a, l=1,2,3
\tag{5}
$$

$$
\frac{\partial \varphi_{1}(X, y)}{\partial y}=\frac{\partial \varphi_{2}(X, y)}{\partial y} \text { at } y=h_{1}-\eta
$$

$$
\frac{\partial \varphi_{2}(X, y)}{\partial y}+X-\xi=0 \text { at } y=-\eta
$$

$$
\frac{\partial \varphi_{3}(X, y)}{\partial y}+X-\xi=0 \text { at } y=h_{1}+h_{2}-\eta
$$

By virtue of Eq. (4) and the first equation of (5), we easily arrive at $\frac{d^{2} \Phi_{l}(n, y)}{d y^{2}}-(n \kappa)^{2} \Phi_{l}(n, y)=\left[1-(-1)^{n}\right] y$. Using the inverse finite Fourier cosine transform, $\varphi_{l}(X, y)=\frac{\Phi_{l}(0, y)}{a}+\frac{2}{a} \sum_{n=1}^{\infty} \Phi_{l}(n, y) \cos (n \kappa X)$, the warping function takes the following form

$$
\begin{aligned}
& \varphi_{l}(X, y)=\frac{\Phi_{l}(0, y)}{a} \\
& +\frac{2}{a} \sum_{n=1}^{\infty}\left[A_{l n} \sinh (n \kappa y)+B_{l n} \cosh (n \kappa y)-\frac{\left[1-(-1)^{n}\right] y}{(n \kappa)^{2}}\right] \cos (n \kappa X), l=1,2,3
\end{aligned}
\tag{6}
$$

where $A_{l n}$ and $B_{l n}$ are unknown coefficients which must be determined using the boundary and continuity conditions. In light of Eqs. (4) and (5) we have $\Phi_{l}(0, y)=A_{l 0}+B_{l 0} y, l=1,2,3$. A Volterra dislocation of screw type with Burgers vector $b_z$ is located in the rectangular cross section with straight cut $y=0, x>0$. First, we suppose that bar and its coating are under net torsion $(\theta \neq 0)$ and then we make a screw dislocation in the domain under consideration. On the other hand, the Eqs. (1) and (2) hold. The boundary condition representing this dislocation under out of plane deformation is

$$
w\left(x, 0^{+}\right)-w\left(x, 0^{-}\right)=b_{z} H(x)
\tag{7}
$$

where $H(.)$ denotes the Heaviside step function. The continuity condition (self-equilibrium of stress) in the rectangular plane along the dislocation cut is as

$$
\tau_{z y}\left(X, 0^{+}\right)=\tau_{z y}\left(X, 0^{-}\right)
\tag{8}
$$

In view of Eqs. (1) and (2), The boundary and continuity conditions (7) and (8) can be rewritten in the following form

$$
\varphi_{1}\left(X, 0^{+}\right)-\varphi_{2}\left(X, 0^{-}\right)=\frac{b_{z}}{\theta} H(X-\xi)
\tag{9}
$$

$$
\frac{\partial \varphi_{1}(X, 0)}{\partial y}=\frac{\partial \varphi_{2}(X, 0)}{\partial y}
$$

With the aid of the expansion $X-\xi=\frac{2 a}{\pi^{2}} \sum_{n=1}^{\infty} \frac{(-1)^{n}-1}{n^{2}}[\cos (n \kappa X)-\cos (n \kappa \xi)]$, the second and third conditions (5) are applied to Eq. (6), leading to

$$B_{20}=\xi a-\frac{a^{2}}{2} \tag{10}$$

$$A_{10}=A_{20}+\frac{b_{z}}{\theta}(a-\xi)$$

$$A_{30}=A_{20}+\frac{b_{z}}{\theta}(a-\xi)$$

$$A_{2 n} \cosh (n \kappa \eta)-B_{2 n} \sinh (n \kappa \eta)=2 \Lambda_{n}$$

$$A_{3 n} \cosh \left(n \kappa\left(h_{1}+h_{2}-\eta\right)\right)+B_{3 n} \sinh \left(n \kappa\left(h_{1}+h_{2}-\eta\right)\right)=2 \Lambda_{n}$$

$$\begin{aligned}
& \mu\left(A_{3 n} \cosh \left(n \kappa\left(h_{1}-\eta\right)\right)+B_{3 n} \sinh \left(n \kappa\left(h_{1}-\eta\right)\right)-2 \Lambda_{n}\right) \\
& =A_{1 n} \cosh \left(n \kappa\left(h_{1}-\eta\right)\right)+B_{1 n} \sinh \left(n \kappa\left(h_{1}-\eta\right)\right)-2 \Lambda_{n}
\end{aligned}$$

$$\begin{aligned}
& A_{1 n} \sinh \left(n \kappa\left(h_{1}-\eta\right)\right)+B_{1 n} \cosh \left(n \kappa\left(h_{1}-\eta\right)\right) \\
& =A_{3 n} \sinh \left(n \kappa\left(h_{1}-\eta\right)\right)+B_{3 n} \cosh \left(n \kappa\left(h_{1}-\eta\right)\right)
\end{aligned}$$

$$B_{1 n}-B_{2 n}=-\frac{b_{z}}{n \kappa \theta} \sin (n \kappa \xi)$$

$$A_{1 n}=A_{2 n}$$

where $\Lambda_{n}=2(1-(-1)^{n}) /(\kappa^{3} n^{3})$ and $\mu_{2} / \mu_{1}=\mu$. Using the Mathematica 10, the unknown coefficients can be obtained as

$$B_{10}=B_{20}=B_{30}=\xi a-\frac{a^{2}}{2} \tag{11}$$

$$A_{10}=A_{30}=A_{20}+\frac{b_{z}}{\theta}(a-\xi)$$

$$\begin{aligned}
A_{1 n} & =A_{2 n}=\frac{b_{z}}{\theta n \kappa} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\left[\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)\right. \\
& \left.-\cosh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)\right]-\Omega_{n}\left(\cosh \left(h_{2} \kappa n\right)\left(\sinh \left(\kappa n\left(\eta-h_{1}\right)\right)+\right.\right. \\
& (\mu-1) \sinh (\eta \kappa n))-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)-\mu \sinh (\eta \kappa n)]
\end{aligned}$$

$$\begin{aligned}
B_{1 n} & =\frac{b_{z}}{\theta n \kappa} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\left[\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)\right. \\
& \left.-\cosh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)\right]-\Omega_{n}\left(\cosh \left(h_{2} \kappa n\right)\left(\cosh \left(\kappa n\left(\eta-h_{1}\right)\right)+\right.\right. \\
& (\mu-1) \cosh (\eta \kappa n))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)-\mu \cosh (\eta \kappa n)]
\end{aligned}$$

$$\begin{aligned}
B_{2 n} & =\frac{b_{z}}{n \kappa \theta}\left\{\sin (n \kappa \xi)+\Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\left[\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)\right.\right. \\
& \left.-\cosh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)\right]-\Omega_{n}\left(\cosh \left(h_{2} \kappa n\right)\left(\cosh \left(\kappa n\left(\eta-h_{1}\right)\right)+\right.\right.
\end{aligned}$$

$$\begin{aligned}
A_{3 n} & =\frac{b_{z}}{\theta \kappa n} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi) \sinh \left(\kappa n\left(-\eta+h_{1}+h_{2}\right)\right)+ \\
& \frac{1}{2} \Omega_{n}\left[(\mu-1)\left(\sinh \left(\kappa n\left(\eta-2 h_{1}\right)\right)+\sinh \left(\kappa n\left(-\eta+2 h_{1}+h_{2}\right)\right)\right)-\mu \sinh \left(\kappa n\left(\eta-h_{2}\right)\right)\right. \\
& \left.+\sinh \left(\kappa n\left(\eta-h_{2}\right)\right)+2 \sinh \left(\kappa n\left(-\eta+h_{1}+h_{2}\right)\right)+(\mu+1) \sinh (\eta \kappa n)\right]
\end{aligned}$$

$$\begin{aligned}
B_{3 n} & =-\frac{b_{z}}{\theta \kappa n} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi) \cosh \left(\kappa n\left(-\eta+h_{1}+h_{2}\right)\right)+ \\
& \frac{1}{2} \Omega_{n}\left[(\mu-1) \cosh \left(\kappa n\left(\eta-2 h_{1}\right)\right)+(\mu+1) \cosh (\eta \kappa n)\right. \\
& \left.-2 \cosh \left(\kappa n\left(-\eta+h_{1}+h_{2}\right)\right)\left((\mu-1) \cosh \left(h_{1} \kappa n\right)+1\right)\right]
\end{aligned}$$

where


$$
\Gamma_{n}=\frac{1}{\left(\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(h_{1} \kappa n\right)+\sinh \left(h_{1} \kappa n\right) \cosh \left(h_{2} \kappa n\right)\right)} \tag{12}
$$

$$
\Omega_{n}=\frac{2\left(1-(-1)^{n}\right)}{\kappa^{3} n^{3}} \Gamma_{n}
$$

Next, with substituting the coefficients $A_{l n}, B_{l n}, l=1,2,3$ into Eqs. (6), we may state the warping functions as

$$
\begin{aligned}
& \varphi(X, y)=\frac{A_{20}}{a}+\frac{b_{z}}{\theta}\left(1-\frac{\xi}{a}\right)+(X+\xi-a) y+\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta n \kappa} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\right. \\
& \left(\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(n \kappa\left(y+\eta-h_{1}\right)\right)-\cosh \left(h_{2} \kappa n\right) \cosh \left(n \kappa\left(y+\eta-h_{1}\right)\right)\right) \\
& -\Omega_{n}\left(\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)+(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))\right. \\
& \left.\left.-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right)-\mu \cosh (n \kappa(y+\eta))\right)\right] \cos (n \kappa X), 0 \leq y \leq h_{1}-\eta
\end{aligned} \tag{13}
$$

$$
\begin{aligned}
& \varphi(X, y)=\frac{A_{20}}{a}+(X+\xi-a) y+\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta n \kappa} \Gamma_{n} \cosh (n \kappa(y+\eta)) \sin (\kappa n \xi)\right. \\
& \left(\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)-\cosh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)\right) \\
& -\Omega_{n}\left(\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)+(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))\right. \\
& \left.\left.-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right)-\mu \cosh (n \kappa(y+\eta))\right)\right] \cos (n \kappa X),-\eta \leq y \leq 0
\end{aligned}
$$

$$
\begin{aligned}
& \varphi(X, y)=\frac{A_{20}}{a}+\frac{b_{z}}{\theta}\left(1-\frac{\xi}{a}\right)+(X+\xi-a) y \\
& +\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta n \kappa} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi) \cosh \left(\kappa n\left(y+\eta-h_{1}-h_{2}\right)\right)\right. \\
& \left(\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)-\cosh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)\right)+\frac{1}{2} \Omega_{n}((\mu-1) \\
& \left(-2 \cosh \left(\kappa n\left(-\eta+h_{1}+h_{2}\right)\right) \cosh \left(h_{1} \kappa n\right) \cosh (n \kappa y)+\cosh \left(\kappa n\left(y+\eta-2 h_{1}\right)\right)\right) \\
& \left.\left.-2 \cosh \left(\kappa n\left(y+\eta-h_{1}-h_{2}\right)\right)+(\mu+1) \cosh (n \kappa(y+\eta))\right)\right] \cos (n \kappa X) \\
& , h_{1}-\eta \leq y \leq h_{2}-\eta
\end{aligned}
$$

According to the Eqs. (2), the stress field takes the form

$$
\begin{aligned}
& \tau_{X z}(X, y)=-\mu_{1} \theta\left\{\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\left(\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(n \kappa\left(y+\eta-h_{1}\right)\right)\right.\right.\right. \\
& \left.-\cosh \left(h_{2} \kappa n\right) \cosh \left(n \kappa\left(y+\eta-h_{1}\right)\right)-\Omega_{n} n \kappa\left(\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.\left.\left.-\mu \cosh (n \kappa(y+\eta))\right)\right] \sin (n \kappa X)\right\}, 0 \leq y \leq h_{1}-\eta
\end{aligned} \tag{14}
$$

$$
\begin{aligned}
& \tau_{y z}(X, y)=\mu_{1} \theta\left\{2 X-a+\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta} \Gamma_{n} \sinh (\eta \kappa n) \sin (\kappa n \xi)\left(\mu \sinh \left(h_{2} \kappa n\right)\right.\right.\right. \\
& \left.\cosh \left(n \kappa\left(y+\eta-h_{1}\right)\right)-\cosh \left(h_{2} \kappa n\right) \sinh \left(n \kappa\left(y+\eta-h_{1}\right)\right)\right) \\
& -\Omega_{n} n \kappa\left(\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)+(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (n \kappa(y+\eta))\right. \\
& \left.\left.\left.-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right)-\mu \sinh (n \kappa(y+\eta))\right)\right] \cos (n \kappa X)\right\}, 0 \leq y \leq h_{1}-\eta
\end{aligned}
$$

$$
\begin{aligned}
& \tau_{X z}(X, y)=-\mu_{1} \theta\left\{\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta} \Gamma_{n} \cosh (n \kappa(y+\eta))\left(\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)\right.\right.\right. \\
& \sin (\kappa n \xi)\left.-\cosh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right)-\Omega_{n} n \kappa\left(\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.\left.\left.-\mu \cosh (n \kappa(y+\eta))\right)\right] \sin (n \kappa X)\right\},-\eta \leq y \leq 0
\end{aligned}
$$

$$
\begin{aligned}
& \tau_{y z}(X, y)=\mu_{1} \theta\{2 X-a+\frac{2}{a} \sum_{n=1}^{\infty}\left[\frac{b_{z}}{\theta} \Gamma_{n} \sinh (n \kappa(y+\eta)) \sin (k n \xi)\left(\mu \sinh \left(h_{2} \kappa n\right)\right.\right. \\
& \cosh \left(\kappa n\left(\eta-h_{1}\right)\right)-\cosh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(\eta-h_{1}\right)\right) \\
& \left.-\Omega_{n} n \kappa\left(\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)+(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (\kappa n(y+\eta))\right. \\
& \left.\left.\left.-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right)-\mu \sinh (\kappa n(y+\eta))\right)\right] \cos (n \kappa X)\right\},-\eta \leq y \leq 0
\end{aligned}
$$

It is noteworthy that we do not need the stress filed in region 3 because the cracks are located in the bar, not in the coating. Using the expansion of the $\Gamma_{n}$ (see Appendix A Ref. [31])

$$
\Gamma_{n}=4 \sum_{j=0}^{\infty} \frac{(1-\mu)^{j}}{(1+\mu)^{j+1}} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\left(e^{-2 h_{2} j} e^{-2 h^{\prime}(j-i)} e^{-2 h k} e^{-(2 m+1) h} n \kappa\right.
$$

(15)

In which $h=h_{1}-h_{2}$ and $h^{\prime}=h_{1}-h_{2}$. Also we have

$$
\sum_{n=1}^{\infty} \Gamma_{n} \sinh (n \kappa y)\left\{\begin{array}{l}
\cos (n \kappa x) \\
\sin (n \kappa x)
\end{array}\right\}=\frac{-1}{\mu+1} \sum_{j=0}^{\infty} \frac{(1-\mu)^{j}}{(1+\mu)^{j}} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\left\{\begin{array}{l}
F_{i j}^{k m}(x, y)-F_{i j}^{k m}(x,-y) \\
-E_{i j}^{k m}(x, y)+E_{i j}^{k m}(x,-y)
\end{array}\right\}
$$

(16)

The above-mentioned new functions are introduced as

$$
E_{i j}^{k m}(x, y)=\frac{\sin (\kappa x)}{\cosh \left(y \kappa+\ln \left(e^{-2 \kappa h_{2} j} e^{-2 \kappa h^{\prime}(j-i)} e^{-2 \kappa h k} e^{-(2 m+1) \kappa h}\right)\right)-\cos (\kappa x)}
$$

(17)

$$
F_{i j}^{k m}(x, y)=\frac{\sinh \left(y \kappa+\ln \left(\left(e^{-2 \kappa h_{2}}\right)^{j}\left(e^{-2 \kappa h^{\prime}}\right)^{j-i}\left(e^{-2 \kappa h}\right)^{k} e^{-(2 m+1) \kappa h}\right)\right)}{\cosh \left(y \kappa+\ln \left(e^{-2 \kappa h_{2} j} e^{-2 \kappa h^{\prime}(j-i)} e^{-2 \kappa h k} e^{-(2 m+1) \kappa h}\right)\right)-\cos (\kappa x)}
$$

The proof of Eq. (15) and (16) have been given in Appendix A and B, respectively.

Next, with the aid of product and sum formulas of the hyperbolic functions and Eq.(16), the stress components (14) can be summed over the entire domain, leading to

$$
\begin{aligned}
& \tau_{x z}(X, y)=-\frac{2 \mu_{1} b_{z}}{a} \varphi_{1}(X, \xi, y+\eta, \eta)+\frac{2 \kappa \mu_{1} \theta}{a} \sum_{n=1}^{\infty} \Omega_{n} n\left[\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (\kappa n(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.-\mu \cosh (\kappa n(y+\eta))] \sin (n \kappa X), 0 \leq y \leq h_{1}-\eta\right.
\end{aligned}
$$

(18)

$$
\begin{aligned}
& \tau_{y z}(X, y)=\mu_{1} \theta(2 X-a)+\frac{2 \mu_{1} b_{z}}{a} \psi_{1}(X, \xi, y+\eta, \eta) \\
& -\frac{2 \kappa \mu_{1} \theta}{a} \sum_{n=1}^{\infty} \Omega_{n} n\left[\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (\kappa n(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.-\mu \sinh (\kappa n(y+\eta))] \cos (n \kappa X), 0 \leq y \leq h_{1}-\eta\right.
\end{aligned}
$$

$$
\begin{aligned}
& \tau_{x z}(X, y)=-\frac{2 \mu_{1} b_{z}}{a} \varphi_{2}(X, \xi, y+\eta, \eta)+\frac{2 \kappa \mu_{1} \theta}{a} \sum_{n=1}^{\infty} \Omega_{n} n\left[\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (\kappa n(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.-\mu \cosh (\kappa n(y+\eta))] \sin (n \kappa X),-\eta \leq y \leq 0\right.
\end{aligned}
$$

$$
\begin{aligned}
& \tau_{y z}(X, y)=\mu_{1} \theta(2 X-a)+\frac{2 \mu_{1} b_{z}}{a} \psi_{2}(X, \xi, y+\eta, \eta) \\
& -\frac{2 \kappa \mu_{1} \theta}{a} \sum_{n=1}^{\infty} \Omega_{n} n\left[\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.
\end{aligned}
$$

$$+(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (\kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa\left(y+\eta-h_{1}\right)\right)$$

$$-\mu \sinh (\kappa(y+\eta))] \cos (\kappa X),-\eta \leq y \leq 0$$

where the functions $\psi_{r}(X, \xi, Y, \eta), \varphi_{r}(X, \xi, Y, \eta), r=1,2$ have been given in Appendix C.

There may be some reasons to rewrite stress component (14) in the form of Eq. (18). First, the functions $E_{i j}^{k m}(x, y)$ and $F_{i j}^{k m}(x, y)$ are converged very rapidly for larger values of $i, j, k$ and $m$. Also for a homogenous rectangular cross section $(\mu=1)$ the functions $E_{i j}^{k m}(x, y)$ and $F_{i j}^{k m}(x, y)$ are vanished for all $i, j, k \neq 0$. Therefore, in the latter case the stress field (18) can be simplified such that only the functions $E_{00}^{0 m}(x, y)$ and $F_{00}^{0 m}(x, y)$ remain nonzero. The comparison of resultant stress field for $\mu=1$ and $h_{1}+h_{2}=h$ the one obtained by Hassani and Faal [10] shows an exact agreement.

It is easy to show that $F_{00}^{01}(x, \eta)=\cot \left(\frac{\kappa x}{2}\right) \sim \frac{2}{\kappa x}$ as $x \to 0$. In other words, one can conclude that the stress component $\tau_{z y}(x, 0)$ has Cauchy singularity which was also previously reported, e.g., by Faal et al. [32] for a rectangular plane under out of plane deformation.

![](./images/811035415069851649_4.jpg)

Fig. 2. Rectangular cross section of bar with a smooth curved crack.

### 2.2 Calculation of torsional rigidity

We consider a system of coordinate $(X, Y)$ attached to lower and left edges of the domain, as shown in Fig. 2, which is compatible with the former change of variable i.e. $X=x+\xi$. Consequently, we also have $Y=y+\eta$. Substituting the stress components (2) into $M=\int_{0}^{a} \int_{0}^{h_{1}+h_{2}}(X \tau_{z Y}(X, Y)-Y \tau_{z X}(X, Y)) d X d Y=D \theta$, torsional rigidity of whole of the domain can be easily evaluated by using the following formula

$$
D=\sum_{l=1}^{3} G_{l} \int_{0}^{a} \int_{y s_{l}}^{y f_{l}}\left(X \theta\left(\frac{\partial \varphi_{3}(X, Y)}{\partial Y}+X-\xi\right)-Y \theta\left(\frac{\partial \varphi_{3}(X, Y)}{\partial x}-Y+\eta\right)\right) d X d Y
\tag{19}
$$

in which

$$
\begin{array}{ll}
y s_{1}=0, & y f_{1}=\eta \\
y s_{2}=\eta, & y f_{2}=h_{1} \\
y s_{3}=h_{1}, & y f_{3}=h_{1}+h_{2}
\end{array}
\tag{20}
$$


$G_{1}=G_{2}=\mu_{1}, \quad G_{3}=\mu_{2}$

where $M$ is the applied torque. Considering $w(X, Y)=\theta \varphi(X, Y)$ and also substituting Eqs. (13) into Eq. (19) we arrive at

$$
D=D_{0}-\frac{16 a^{2} b_{z} \mu_{1}}{\pi^{3} n^{3}} \sum_{n=1,3,5}^{\infty} \frac{\Gamma_{n}}{n^{3}} \sinh (n \kappa \eta / 2) \sin (n \kappa \xi)[\cosh (n \kappa \eta / 2)
$$

$(\mu(\sinh (n \kappa h_{1}) \sinh (n \kappa h_{2})-1)+\cosh (n \kappa h_{2})(\cosh (n \kappa h_{1})+\mu-1))$
$-\sinh (n \kappa \eta / 2)(\mu \sinh (n \kappa h_{2}) \cosh (n \kappa h_{1})+\sinh (n \kappa h_{1}) \cosh (n \kappa h_{2}))]$

in which

$$
D_{0}=\frac{1}{6} \mu_{1} a^{3}\left(h_{2} \mu+h_{1}\right)+\frac{4 \mu_{1}}{\pi^{2}} \sum_{n=1,3,5}^{\infty} \frac{\Omega_{n}}{n^{2}}\left[4 a \mu\left((\mu-1) \cosh \left(n \kappa h_{1}\right)+1\right)+\mu \sinh \left(n \kappa h_{2}\right)\right.
$$

$(\pi n(h_{2} \mu+h_{1}) \cosh (n \kappa h_{1})-4 a \sinh (n \kappa h_{1}))+\cosh (n \kappa h_{2})(\pi n(h_{2} \mu+h_{1}) \sinh (n \kappa h_{1})$
$-4 a((\mu-1) \mu+1) \cosh (n \kappa h_{1})-4 a(\mu-1))]$

$D_{0}$ denotes torsional rigidity in the rectangular cross section bar with the isotropic coating. Comparing $D_{0}$ for a homogenous rectangular cross section bar to that provided by Barber [30] shows identical result.

### 3. Analyses with multiple cracks

In this section, we implement the dislocation solutions accomplished in the prior section to analyze bars of rectangular cross section with an isotropic coating weakened by multiple arbitrary oriented curved cracks. The anti-plane stress components on the local coordinate $(X_{i}, Y_{i})$, as shown in Fig. 2, located on the surface of the i-th crack become

$$
\begin{aligned}
& \tau_{Y_{i} z}(X, Y)=\tau_{z y}(X, Y) \cos \varphi_{i}-\tau_{z x}(X, Y) \sin \varphi_{i} \\
& \tau_{X_{i} z}(X, Y)=\tau_{z y}(X, Y) \sin \varphi_{i}+\tau_{z x}(X, Y) \cos \varphi_{i}
\end{aligned}
$$

where $\varphi_{i}$ denotes angle between $X_{i}$ (local) and $X$ (global) axes.

The dislocation solution or solution to Eq. (4) leads to the warping function, which is also a solution to the governing equation of the problem, that is, Eq. (3). Also this solution with associated stress field (18) satisfies the equilibrium equation of the plane and the boundary condition of a rectangular cross section bar with an isotropic coating (Eq. (5)). The governing equation and the boundary condition of the rectangular cross section bar with an isotropic coating weakened by several cracks are still Equations (3) and (5), respectively. Therefore, the dislocation solution is a solution for the crack problem satisfying the governing equation and the boundary conditions of a domain. There is an additional controlling parameter $b_{z}$ to satisfy the last boundary condition of the problem, that is, the crack surfaces being traction free. Korsunsky and Hills [33] provide additional information on the distribution dislocation technique.

To solve the problem, suppose dislocations with unknown density $B_{z j}$ are distributed on the infinitesimal segment $d \lambda_{j}$ located at a point with the coordinate $(X_{j}, Y_{j})$ on the $j$-th crack surface. First, we find the traction on the surface of the $i$-th crack due to the presence of the above distribution of dislocations. Utilizing Eqs. (18) and (22), the anti-plane stress components become

$$
\tau_{Y_{i} z}\left(X_{i}, Y_{i}\right)=\frac{2 \mu_{1} b_{z}}{a}\left[\psi_{1}\left(X_{i}, X_{j}, Y_{i}, Y_{j}\right) \cos \varphi_{i}+\varphi_{1}\left(X_{i}, X_{j}, Y_{i}, Y_{j}\right) \sin \varphi_{i}\right]
\tag{24}
$$

$$
\begin{aligned}
& \mu_{1} \theta\left(2 X_{i}-a\right) \cos \varphi_{i}-\frac{2 \kappa \mu_{1} \theta}{a}\left\{\cos \varphi_{i} \sum_{n=1}^{\infty} \Omega_{n} n\left[\sinh \left(\kappa n\left(Y_{i}-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh \left(n \kappa Y_{i}\right)-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(Y_{i}-h_{1}\right)\right) \\
& \left.-\mu \sinh \left(n \kappa Y_{i}\right)\right] \cos \left(n \kappa X_{i}\right)+\sin \varphi_{i} \sum_{n=1}^{\infty} \Omega_{n} n\left[\cosh \left(\kappa n\left(Y_{i}-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh \left(n \kappa Y_{i}\right)-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(Y_{i}-h_{1}\right)\right) \\
& \left.\left.-\mu \cosh \left(n \kappa Y_{i}\right)\right] \sin \left(n \kappa X_{i}\right)\right\}, Y_{j} \leq Y_{i} \leq h_{1}
\end{aligned}
$$

$$
\begin{aligned}
& \tau_{Y_{i} z}\left(X_{i}, Y_{i}\right)=\frac{2 \mu_{1} b_{z}}{a}\left[\psi_{2}\left(X_{i}, X_{j}, Y_{i}, Y_{j}\right) \cos \varphi_{i}+\varphi_{2}\left(X_{i}, X_{j}, Y_{i}, Y_{j}\right) \sin \varphi_{i}\right]+ \\
& \mu_{1} \theta(2 X-a) \cos \varphi_{i}-\frac{2 \kappa \mu_{1} \theta}{a}\left[\cos \varphi_{i} \sum_{n=1}^{\infty} \Omega_{n} n\left[\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.-\mu \sinh (n \kappa(y+\eta))] \cos (n \kappa X)+\sin \varphi_{i} \sum_{n=1}^{\infty} \Omega_{n} n\left[\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right.\right. \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.\left.-\mu \cosh (n \kappa(y+\eta))] \sin (n \kappa X)], 0 \leq Y_{i} \leq Y_{j}\right.
\end{aligned}
$$

We have to emphasize that for evaluating $D$, the term $b_{z}$ in the Eq. (21) is replaced by $B_{z j} d \lambda_{j}$ and also $\xi$ and $\eta$ is replaced by $X_{j}$ and $Y_{j}$, respectively. Covering crack surfaces by dislocations, the principle of superposition can be invoked to obtain traction on a crack surface. Then, Eq. (21) is integrated on the non-dimensional crack length. The integration of Eq. (21) can be assisted by describing crack configurations in a parametric form $X_{j}=X_{j}(t), Y_{j}=Y_{j}(t), i=1,2, \ldots, N$, where $-1 \leq t \leq 1$. We recall that $\theta=M / D$ is a constant which depends on geometry of the domain under consideration and cracks. Finally, the torsional rigidity is achieved by

$$
D=\frac{D_{0}}{1+\int_{-1}^{1} U_{j}\left(X_{j}(t), Y_{j}(t)\right) b_{z j}(t) \sqrt{\left[X_{j}^{\prime}(t)\right]^{2}+\left[Y_{j}^{\prime}(t)\right]^{2}} d t}
\tag{25}
$$

where, $b_{z j}(t)$ is the dislocation density function along the dimensionless length $-1 \leq t \leq 1$. Analogously, the integration of Eq. (22), leads to the resultant tractions on the crack surfaces. Also $U_{j}(\xi, \eta)$ is given in Appendix C.

Substituting $\theta=\frac{M}{D}$ into Eqs. (22) gives the final form of the traction on the surface of the i-th crack. The crack surfaces are stress free, therefore the left side of the equation made by integration of Eq. (22) must be vanished. Consequently, the terms of Eqs. (24) which are not multiplied by $b_{z j}(t)$ are moved to the left side of these equations. Finally, we have

$$
Q_{i}\left(X_{i}(s), Y_{i}(s)\right)=\sum_{j=1}^{N} \int_{-1}^{1} k_{i j}(s, t) b_{z j}(t) d t,-1 \leq s \leq 1, \quad i=1,2,..., N
\tag{26}
$$

The kernels $k_{i j}(s, t)$ and the left side of Eqs. (26), i.e. $Q_{i}\left(X_{i}(s), Y_{i}(s)\right)$ can be expressed in the following form

$$
\begin{aligned}
k_{i j}(s, t)= & \left\{\frac{2 \mu_{1}}{a}\left[\psi_{r}\left(X_{i}(s), X_{j}(t), Y_{i}(s), Y_{j}(t)\right) \cos \phi_{i}+\varphi_{r}\left(X_{i}(s), X_{j}(t), Y_{i}(s), Y_{j}(t)\right) \sin \phi_{i}\right]\right. \\
& \left.+U_{j}\left(X_{j}(t), Y_{j}(t)\right) P_{i}\left(X_{i}(s), Y_{i}(s)\right)\right\} \sqrt{\left[X_{j}^{\prime}(t)\right]^{2}+\left[Y_{j}^{\prime}(t)\right]^{2}}
\end{aligned}
$$
(27)

$$
Q_{i}\left(X_{i}(s), Y_{i}(s)\right)=-\frac{M}{D_{0}} P_{i}\left(X_{i}(s), Y_{i}(s)\right)
$$

where the subscripts $r=1,2$ refer to the regions $Y_{j}(t) \leq Y_{i}(s) \leq h_{1}$ and $0 \leq Y_{i}(s) \leq Y_{j}(t)$ respectively and the functions $U_{j}(\xi, \eta)$ and $P_{i}(X, Y)$ have been given in Appendix C. By virtue of Bueckner's principle (see Ref. [34]), the left-hand side of Eq. (26) after changing the sign is the traction caused by the external moment on the intact domain at the presumed surfaces of cracks. In fact, we implicitly used the Bueckner's principle, to derive Eqs. (26).

As a result of single-valuedness of displacement field away from the surfaces of embedded cracks, the dislocation density functions are subjected to the following closure requirement [35]

$$
\int_{-1}^{1} \sqrt{\left[X_{j}^{\prime}(t)\right]^{2}+\left[Y_{j}^{\prime}(t)\right]^{2}} b_{z j}(t) d t=0
$$

(28)

The Cauchy singular integral Eqs. (26) and (28) must be solved simultaneously to determine the unknown dislocation density functions. To this end, the original numerical procedure proposed by Erdogan et al. [36] may not be directly applicable, since it is not able to simultaneously consider all types of cracks; i.e., embedded and edge cracks. In the study by Faal et al. [35], a minor generalization of this numerical procedure was introduced to overcome this issue. For want of space, we did not repeat it here but we use this generalized method to determine the unknown dislocation density functions.

Stress fields for embedded cracks are singular at the crack tips with square root singularity, thus for embedded cracks the dislocation density functions are represented by [35]

$$
b_{z j}(t)=\frac{g_{z j}(t)}{\sqrt{1-t^{2}}},-1 \leq t \leq 1
$$

(29)

For edge cracks, taking the embedded crack tip at $t=-1$, we let [35]

$$
b_{z j}(t)=g_{z j}(t) \sqrt{\frac{1-t}{1+t}},-1 \leq t \leq 1
$$

(30)

The stress intensity factors for the embedded and edge cracks are [35]

$$
\left\{\begin{aligned}
k_{I I I L i} & =\mu_{1} \frac{\sqrt{\pi}}{2}\left(\left[X_{j}^{\prime}(-1)\right]^{2}+\left[Y_{j}^{\prime}(-1)\right]^{2}\right)^{\frac{1}{4}} g_{z j}(-1) \\
k_{I I I R i} & =-\mu_{1} \frac{\sqrt{\pi}}{2}\left(\left[X_{j}^{\prime}(1)\right]^{2}+\left[Y_{j}^{\prime}(1)\right]^{2}\right)^{\frac{1}{4}} g_{z j}(1)
\end{aligned}\right.
$$

for embedded crack
(31)

$$
k_{I I L i}=\mu_{1} \sqrt{\pi}\left(\left[X_{j}^{\prime}(-1)\right]^{2}+\left[Y_{j}^{\prime}(-1)\right]^{2}\right)^{\frac{1}{4}} g_{z j}(-1) \text { for edge crack }
$$

In order to determine the torsional rigidity of cracked bar the integral appeared in Eq. (25) can be evaluated by use of discretization of domain of integration at the specific points $t_{k}=\cos \left(\frac{\pi(2 k-1)}{2 m_{0}}\right), k=1,2, \ldots, m_{0}$ where $m_{0}$ denotes the number of discrete points. This method was explained completely in Ref. [35]. Consequently, the torsional rigidity obtains as

$$
D = \frac{D_0}{1 + \frac{\pi}{m_0} \sum_{k=1}^{m_0} U_j(Y_j(t_k), X_j(t_k))g_{zj}(t_k) \sqrt{[X_j'(t_k)]^2 + [Y_j'(t_k)]^2}} \tag{32}
$$

where
$$
\Delta(t_k)=
\begin{cases}
1 & \quad for\ embedded\ cracks \\
1 - t_k & \quad for\ edge\ cracks
\end{cases} \tag{33}
$$

### 4. Numerical examples and discussions

The analysis framework, developed in the preceding section, allowed the consideration of a rectangular cross section bar with an isotropic coating weakened by multiple cracks. These cracks may include smooth embedded and edge cracks with different orientations.

In this section several examples have been evaluated to verify the accuracy and correctness of the current approach and second to illustrate the capability of the dislocation method in handling handle problems involving multiple arbitrary oriented curved cracks. The solution can be verified with the published results for the homogenous rectangular cross section by setting $\mu=1$ and $h_1+h_2=h$ (Tables 1–6).

**Example 1. An edge crack, bisecting and perpendicular to one side of the cross section in the homogenous rectangular cross section**

In order to demonstrate and verify the solution of the dislocation method, we consider the torsion problem of a homogenous cross section with an edge crack. In this example, the crack configuration can be seen in Fig. 3. Results for normalized torsional rigidities $10^4 D/\mu_1 a^4$ are listed in Table 1. Values of normalized stress intensity factors, $k_{III}a^{2.5}/M$, at the crack tip for aforementioned bar with an edge crack, bisecting and perpendicular to one side of cross section can be found in Table 2.

![](./images/811035415069851649_5.jpg)

Fig. 3. A homogenous cross section with an edge crack bisecting and normal to its side

Table 1. Values of $10^{4}D/\mu_{1}a^{4}$ for a homogenous cross section with an edge crack, bisecting and normal to one side of the cross section

<table>
<thead>
<tr>
<th colspan="2">Study source</th>
<th>$\frac{l}{a}=0.05$</th>
<th>$\frac{l}{a}=0.1$</th>
<th>$\frac{l}{a}=0.3$</th>
<th>$\frac{l}{a}=0.5$</th>
<th>$\frac{l}{a}=0.7$</th>
<th>$\frac{l}{a}=0.9$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.1$</td>
<td>Present work</td>
<td>22.782</td>
<td>21.871</td>
<td>17.893</td>
<td>13.895</td>
<td>9.930</td>
<td>6.640</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>22.968</td>
<td>21.773</td>
<td>17.820</td>
<td>13.841</td>
<td>9.891</td>
<td>6.626</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.2$</td>
<td>Present work</td>
<td>156.952</td>
<td>151.239</td>
<td>121.157</td>
<td>90.241</td>
<td>62.823</td>
<td>47.565</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>156.540</td>
<td>150.660</td>
<td>120.600</td>
<td>89.849</td>
<td>62.620</td>
<td>47.535</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.25$</td>
<td>Present work</td>
<td>281.540</td>
<td>271.690</td>
<td>216.103</td>
<td>158.812</td>
<td>111.661</td>
<td>88.956</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>280.790</td>
<td>270.630</td>
<td>214.950</td>
<td>158.040</td>
<td>111.660</td>
<td>88.892</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.5$</td>
<td>Present work</td>
<td>1389.948</td>
<td>1349.644</td>
<td>1082.410</td>
<td>811.037</td>
<td>633.847</td>
<td>573.873</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>1387.100</td>
<td>1344.900</td>
<td>1076.400</td>
<td>807.110</td>
<td>632.260</td>
<td>573.720</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=1$</td>
<td>Present work</td>
<td>4542.637</td>
<td>4460.576</td>
<td>3877.044</td>
<td>3278.181</td>
<td>2919.251</td>
<td>2814.675</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>4534.600</td>
<td>4446.900</td>
<td>38.57.4</td>
<td>3266.100</td>
<td>2914.200</td>
<td>2814.300</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=2.5$</td>
<td>Present work</td>
<td>14529.832</td>
<td>14433.787</td>
<td>13739.364</td>
<td>13019.619</td>
<td>12592.568</td>
<td>12471.722</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>14509.000</td>
<td>14400.000</td>
<td>13691.000</td>
<td>12986.000</td>
<td>12580.000</td>
<td>12471.000</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=5$</td>
<td>Present work</td>
<td>31196.451</td>
<td>31100.273</td>
<td>30404.791</td>
<td>29683.875</td>
<td>29256.160</td>
<td>29135.163</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>31161.000</td>
<td>31037.000</td>
<td>30326.000</td>
<td>29626.000</td>
<td>29239.000</td>
<td>29139.000</td>
</tr>
</tbody>
</table>

Table 2. Values of $k_{III}a^{2.5}/M$ for a homogenous cross section with an edge crack, bisecting and normal to one side of the cross section

<table>
<thead>
<tr>
<th colspan="2">Study source</th>
<th>$\frac{l}{a}=0.05$</th>
<th>$\frac{l}{a}=0.1$</th>
<th>$\frac{l}{a}=0.3$</th>
<th>$\frac{l}{a}=0.5$</th>
<th>$\frac{l}{a}=0.7$</th>
<th>$\frac{l}{a}=0.9$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.1$</td>
<td>Present work</td>
<td>17.765</td>
<td>20.082</td>
<td>24.999</td>
<td>32.179</td>
<td>44.411</td>
<td>47.274</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>17.355</td>
<td>20.044</td>
<td>25.070</td>
<td>32.303</td>
<td>44.573</td>
<td>45.199</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.2$</td>
<td>Present work</td>
<td>6.123</td>
<td>7.558</td>
<td>10.335</td>
<td>13.576</td>
<td>17.218</td>
<td>11.115</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>6.094</td>
<td>7.578</td>
<td>10.371</td>
<td>13.614</td>
<td>17.710</td>
<td>11.017</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.25$</td>
<td>Present work</td>
<td>4.415</td>
<td>5.588</td>
<td>7.942</td>
<td>10.366</td>
<td>12.269</td>
<td>6.783</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>4.435</td>
<td>5.617</td>
<td>7.979</td>
<td>10.387</td>
<td>12.165</td>
<td>6.758</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=0.5$</td>
<td>Present work</td>
<td>1.754</td>
<td>2.331</td>
<td>3.544</td>
<td>4.216</td>
<td>3.808</td>
<td>1.466</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>1.795</td>
<td>2.360</td>
<td>3.554</td>
<td>4.202</td>
<td>3.765</td>
<td>1.487</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=1$</td>
<td>Present work</td>
<td>0.757</td>
<td>1.015</td>
<td>1.480</td>
<td>1.524</td>
<td>1.130</td>
<td>0.366</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>0.789</td>
<td>1.034</td>
<td>1.486</td>
<td>1.515</td>
<td>1.112</td>
<td>0.368</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=2.5$</td>
<td>Present work</td>
<td>0.256</td>
<td>0.340</td>
<td>0.457</td>
<td>0.420</td>
<td>0.283</td>
<td>0.087</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>0.283</td>
<td>0.352</td>
<td>0.457</td>
<td>0.403</td>
<td>0.274</td>
<td>0.084</td>
</tr>
<tr>
<td rowspan="2">$\frac{h}{2a}=5$</td>
<td>Present work</td>
<td>0.1191</td>
<td>0.158</td>
<td>0.207</td>
<td>0.185</td>
<td>0.123</td>
<td>0.039</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>0.1462</td>
<td>0.171</td>
<td>0.205</td>
<td>0.178</td>
<td>0.114</td>
<td>0.034</td>
</tr>
</tbody>
</table>

### Example 2. An edge crack, non-bisecting and normal to one side of the cross section in the homogenous bar

In the second validation, we consider a homogenous rectangular cross section with an edge crack, non-bisecting and normal to one side of the cross section, as shown in Fig. 4. Values of normalized torsional rigidities $10^4D/\mu_1a^4$ and normalized stress intensity factors at the crack tip $k_{III}a^{2.5}/M$ can be found in Table 3 and 4 respectively. As can be observed, our results are in an excellent agreement with the previous investigation.

![](./images/811035415069851649_6.jpg)

Fig. 4. A homogenous rectangular cross section with an edge crack non-bisecting and normal to its side

Table 3. Values of $10^4D/\mu_1a^4$ for a homogenous cross section with an edge crack, non-bisecting and perpendicular to one side of the cross section

<table>
  <thead>
    <tr>
      <th>$\frac{h}{a}=1$</th>
      <th>Study source</th>
      <th>$\frac{l}{a}=0.1$</th>
      <th>$\frac{l}{a}=0.2$</th>
      <th>$\frac{l}{a}=0.3$</th>
      <th>$\frac{l}{a}=0.5$</th>
      <th>$\frac{l}{a}=0.7$</th>
      <th>$\frac{l}{a}=0.9$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\frac{d}{a}=0.1$</td>
      <td>Present work</td>
      <td>1392.874</td>
      <td>1363.562</td>
      <td>1324.686</td>
      <td>1238.010</td>
      <td>1167.481</td>
      <td>1137.330</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1391.700</td>
      <td>1361.800</td>
      <td>1322.700</td>
      <td>1236.300</td>
      <td>1166.600</td>
      <td>1137.200</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{d}{a}=0.2$</td>
      <td>Present work</td>
      <td>1375.728</td>
      <td>1310.734</td>
      <td>1230.746</td>
      <td>1067.898</td>
      <td>949.029</td>
      <td>904.360</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1370.000</td>
      <td>1301.200</td>
      <td>1227.000</td>
      <td>1065.100</td>
      <td>941.780</td>
      <td>904.230</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{d}{a}=0.3$</td>
      <td>Present work</td>
      <td>1361.581</td>
      <td>1265.932</td>
      <td>1151.428</td>
      <td>929.901</td>
      <td>778.482</td>
      <td>725.083</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1357.700</td>
      <td>1260.700</td>
      <td>1146.200</td>
      <td>926.440</td>
      <td>116.960</td>
      <td>724.930</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{d}{a}=0.4$</td>
      <td>Present work</td>
      <td>1352.664</td>
      <td>1237.116</td>
      <td>1100.056</td>
      <td>841.402</td>
      <td>670.674</td>
      <td>612.326</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1348.000</td>
      <td>1231.100</td>
      <td>1094.200</td>
      <td>837.470</td>
      <td>669.000</td>
      <td>612.160</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{d}{a}=0.5$</td>
      <td>Present work</td>
      <td>1349.644</td>
      <td>1227.265</td>
      <td>1082.410</td>
      <td>811.037</td>
      <td>633.847</td>
      <td>573.874</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1344.900</td>
      <td>1221.100</td>
      <td>1076.400</td>
      <td>807.110</td>
      <td>632.260</td>
      <td>573.720</td>
    </tr>
  </tbody>
</table>

Table 4. Values of $k_{III}a^{2.5}/M$ for homogenous cross section with an edge crack, bisecting and perpendicular to one side of cross section

<table>
<thead>
<tr>
<th>$\dfrac{h}{a}=1$</th>
<th>Study source</th>
<th>$\dfrac{l}{a}=0.1$</th>
<th>$\dfrac{l}{a}=0.2$</th>
<th>$\dfrac{l}{a}=0.3$</th>
<th>$\dfrac{l}{a}=0.5$</th>
<th>$\dfrac{l}{a}=0.7$</th>
<th>$\dfrac{l}{a}=0.9$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">$\dfrac{d}{a}=0.1$</td>
<td>Present work</td>
<td>1.080</td>
<td>1.372</td>
<td>1.546</td>
<td>1.655</td>
<td>1.395</td>
<td>0.846</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>1.093</td>
<td>1.378</td>
<td>1.546</td>
<td>1.645</td>
<td>1.378</td>
<td>0.833</td>
</tr>
<tr>
<td rowspan="2">$\dfrac{d}{a}=0.2$</td>
<td>Present work</td>
<td>1.662</td>
<td>2.086</td>
<td>2.347</td>
<td>2.557</td>
<td>2.152</td>
<td>1.250</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>1.678</td>
<td>2.094</td>
<td>2.349</td>
<td>2.543</td>
<td>2.125</td>
<td>1.235</td>
</tr>
<tr>
<td rowspan="2">$\dfrac{d}{a}=0.3$</td>
<td>Present work</td>
<td>2.044</td>
<td>2.606</td>
<td>2.977</td>
<td>3.365</td>
<td>2.905</td>
<td>1.677</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>2.067</td>
<td>2.619</td>
<td>2.978</td>
<td>3.349</td>
<td>2.868</td>
<td>1.660</td>
</tr>
<tr>
<td rowspan="2">$\dfrac{d}{a}=0.4$</td>
<td>Present work</td>
<td>2.261</td>
<td>2.927</td>
<td>3.396</td>
<td>3.980</td>
<td>3.546</td>
<td>2.058</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>2.291</td>
<td>2.942</td>
<td>3.404</td>
<td>3.965</td>
<td>3.499</td>
<td>2.037</td>
</tr>
<tr>
<td rowspan="2">$\dfrac{d}{a}=0.5$</td>
<td>Present work</td>
<td>2.331</td>
<td>3.036</td>
<td>3.544</td>
<td>4.217</td>
<td>3.811</td>
<td>2.219</td>
</tr>
<tr>
<td>Chen [7]</td>
<td>2.360</td>
<td>3.053</td>
<td>3.554</td>
<td>4.202</td>
<td>3.765</td>
<td>2.198</td>
</tr>
</tbody>
</table>

**Example 3. Two edge cracks bisecting two opposite sides of the homogenous cross section**

In the last validation, we consider two edge cracks bisecting two opposite sides of the homogenous cross section, as shown in Fig. 5. Values of normalized torsional rigidities $10^4D/\mu_1a^4$ and dimensionless stress intensity factors at the crack tips $k_{III}a^{2.5}/M$ are listed in Table 5 and 6 respectively.

![](./images/811035415069851649_7.jpg)

Fig. 5. Bar cross section with two edge cracks bisecting and normal to opposite sides

**Table 5.** Values of $10^4D/\mu_1a^4$ for a homogenous bar with two edge cracks bisecting and perpendicular to opposite sides

<table>
  <thead>
    <tr>
      <th></th>
      <th>Study source</th>
      <th>$\frac{l}{a}=0.1$</th>
      <th>$\frac{l}{a}=0.2$</th>
      <th>$\frac{l}{a}=0.3$</th>
      <th>$\frac{l}{a}=0.5$</th>
      <th>$\frac{l}{a}=0.7$</th>
      <th>$\frac{l}{a}=0.9$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.1$</td>
      <td>Present work</td>
      <td>22.258</td>
      <td>20.436</td>
      <td>18.472</td>
      <td>14.482</td>
      <td>10.504</td>
      <td>6.962</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>22.115</td>
      <td>20.283</td>
      <td>18.334</td>
      <td>14.382</td>
      <td>10.441</td>
      <td>6.943</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.25$</td>
      <td>Present work</td>
      <td>277.231</td>
      <td>257.575</td>
      <td>232.640</td>
      <td>177.659</td>
      <td>126.260</td>
      <td>92.553</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>275.950</td>
      <td>255.790</td>
      <td>230.790</td>
      <td>176.210</td>
      <td>125.420</td>
      <td>92.299</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.5$</td>
      <td>Present work</td>
      <td>1374.193</td>
      <td>1294.504</td>
      <td>1185.520</td>
      <td>936.306</td>
      <td>716.384</td>
      <td>588.585</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1368.800</td>
      <td>1286.100</td>
      <td>1176.100</td>
      <td>928.160</td>
      <td>711.440</td>
      <td>587.060</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=1$</td>
      <td>Present work</td>
      <td>4511.829</td>
      <td>4350.277</td>
      <td>4122.884</td>
      <td>3590.644</td>
      <td>3118.749</td>
      <td>2847.171</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>4496.500</td>
      <td>4325.900</td>
      <td>4094.100</td>
      <td>3563.100</td>
      <td>3100.500</td>
      <td>2841.700</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=2.5$</td>
      <td>Present work</td>
      <td>14494.048</td>
      <td>14305.003</td>
      <td>14036.990</td>
      <td>13404.098</td>
      <td>12838.344</td>
      <td>12511.240</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>14452.00</td>
      <td>14240.00</td>
      <td>13961.00</td>
      <td>13329.000</td>
      <td>12789.00</td>
      <td>12500.00</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=5$</td>
      <td>Present work</td>
      <td>31160.62</td>
      <td>30971.31</td>
      <td>30702.91</td>
      <td>30069.05</td>
      <td>29502.38</td>
      <td>29174.73</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>31086.00</td>
      <td>30845.00</td>
      <td>30554.00</td>
      <td>29928.00</td>
      <td>29419.00</td>
      <td>29164.0</td>
    </tr>
  </tbody>
</table>

Table 6. Values of $k_{III}a^{2.5}/M$ for a homogenous bar with two edge cracks bisecting and perpendicular to opposite sides

<table>
  <thead>
    <tr>
      <th></th>
      <th>Study source</th>
      <th>$\frac{l}{a}=0.1$</th>
      <th>$\frac{l}{a}=0.2$</th>
      <th>$\frac{l}{a}=0.3$</th>
      <th>$\frac{l}{a}=0.5$</th>
      <th>$\frac{l}{a}=0.7$</th>
      <th>$\frac{l}{a}=0.9$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.1$</td>
      <td>Present work</td>
      <td>18.185</td>
      <td>21.496</td>
      <td>24.131</td>
      <td>30.883</td>
      <td>42.229</td>
      <td>52.112</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>18.404</td>
      <td>21.599</td>
      <td>24.221</td>
      <td>31.002</td>
      <td>42.369</td>
      <td>50.420</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.25$</td>
      <td>Present work</td>
      <td>4.482</td>
      <td>5.883</td>
      <td>6.991</td>
      <td>9.346</td>
      <td>11.941</td>
      <td>10.518</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>4.606</td>
      <td>5.954</td>
      <td>7.046</td>
      <td>9.386</td>
      <td>11.903</td>
      <td>10.226</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=0.5$</td>
      <td>Present work</td>
      <td>1.770</td>
      <td>2.407</td>
      <td>2.903</td>
      <td>3.754</td>
      <td>4.217</td>
      <td>3.118</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>1.833</td>
      <td>2.441</td>
      <td>2.932</td>
      <td>3.764</td>
      <td>4.190</td>
      <td>3.016</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=1$</td>
      <td>Present work</td>
      <td>0.760</td>
      <td>1.028</td>
      <td>1.212</td>
      <td>1.435</td>
      <td>1.416</td>
      <td>0.937</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>0.797</td>
      <td>1.049</td>
      <td>1.225</td>
      <td>1.435</td>
      <td>1.398</td>
      <td>0.887</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=2.5$</td>
      <td>Present work</td>
      <td>0.255</td>
      <td>0.339</td>
      <td>0.387</td>
      <td>0.420</td>
      <td>0.377</td>
      <td>0.234</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>0.283</td>
      <td>0.351</td>
      <td>0.393</td>
      <td>0.417</td>
      <td>0.364</td>
      <td>0.207</td>
    </tr>
    <tr>
      <td rowspan="2">$\frac{h}{2a}=5$</td>
      <td>Present work</td>
      <td>0.1186</td>
      <td>0.157</td>
      <td>0.177</td>
      <td>0.187</td>
      <td>0.164</td>
      <td>0.100</td>
    </tr>
    <tr>
      <td>Chen [7]</td>
      <td>0.1458</td>
      <td>0.157</td>
      <td>0.181</td>
      <td>0.182</td>
      <td>0.151</td>
      <td>0.083</td>
    </tr>
  </tbody>
</table>

The efficiencies of the dislocation method were demonstrated by solving several numerical examples, in handling problems involving several arbitrary oriented curved cracks. In all following examples, we consider $h_1=0.5a$ and also an aluminum bar with shear modulus $\mu_1=26$ Gpa which is coated by steel with shear modulus $\mu_2=80$ Gpa.

Example 4. An inclined edge crack emanating from midpoint of one side of cross section

In the first non-comparative example we consider an inclined edge crack emanating from the midpoint of one side of the cross section of the bar. The extension of the crack line passes from the midpoint of the other side of the cross section, as shown in Fig. 6. The thickness of the coating is assumed to be $h_2 = 0.1a$. Variation of normalized stress intensity factor, $k_{III}a^{2.5}/M$, of the crack tip versus non-dimensional crack length $l/a$ is depicted in Fig. 6. First, the normalized stress intensity factor of the crack tip is increased with growing the crack length as we expected, but by approaching crack tip to the stress free surface the normalized stress intensity factor is reduced because of approaching the crack tip to the boundary of the cross section. In the following discussion, Variation of $10^4D/\mu_1a^4$ with respect to the normalized crack length can be found in Fig. 7. As seen from the figure, It could be observed that the torsional rigidity of the cracked bar is reduced by growing the crack length which makes a weaker domain.

![](./images/811035415069851649_8.jpg)

Fig. 6. Variation of $k_{III}a^{2.5}/M$ versus normalized crack length $l/a$ for an inclined edge crack

![](./images/811035415069851649_9.jpg)

Fig. 7. Variation of normalized torsional rigidity $10^{4} D / \mu_{1} a^{4}$ versus normalized crack length $l / a$ for an inclined edge crack

In the continuation of this example, the variation of normalized stress intensity factor with relative coating thickness, $h_{2} / a$, can be observed in Fig. 8. The crack length is considered $l=0.2 a$. As can be seen, enhancing thickness reduces the normalized stress intensity factors.

![](./images/811035415069851649_10.jpg)

Fig. 8. Variation of normalized stress intensity factor $k_{III}a^{2.5}/M$ versus normalized thickness of the coating
for an edge crack

Example 5. An embedded circular arc crack

As an alternative example, we consider an embedded circular arc crack with radius $R=0.05a$,
as shown in Fig. 9. We suppose that the crack length increases equally from its two tips. The
thickness of the coating is considered $h_{2}=0.1a$. The variation of normalized stress intensity factor
of crack tips $k_{III}a^{2.5}/M$ versus normalized crack length $l/a$ where $l=R(\pi-2\alpha)$ is displayed in
Fig. 9. As can be seen, increasing the crack length give rise to the normalized stress intensity
factors of the singular crack tips. This trend is continued until crack reaches $l/a\approx0.11$ but after
that we see a decreasing of the normalized stress intensity factors while the crack length is
increased because of approaching crack tip to the stress free surface of the cross section. Values of
$10^{4}D/\mu_{1}a^{4}$ versus the normalized half length of the circular crack, $l/a$, are illustrated in Fig. 10.
As expected, the normalized torsional rigidities tend to be less as the crack length grows up.

![](./images/811035415069851649_11.jpg)

Fig. 9. Values of $k_{III}a^{2.5}/M$ versus normalized half length of the circular crack $l/a$ for an embedded circular crack

![](./images/811035415069851649_12.jpg)

Fig. 10. Variation of $10^{4}D/\mu_{1}a^{4}$ versus normalized half length of the circular crack $l/a$ for an embedded circular crack

The variation of normalized stress intensity factors for semicircular crack with the normalized thickness can be observed in Fig. 11. The similar trend of the previous example for variations of the normalized stress intensity factors versus normalized thickness ratio can be observed.

![](./images/811035415069851649_13.jpg)

Fig. 11. Variation of normalized stress intensity factor $k_{III}a^{2.5}/M$ versus relative thickness of the coating for an embedded circular crack

### Example 6. An embedded crack and an edge crack

In the following examples, let us consider a rectangular cross section bar with an isotropic coating weakened by an embedded crack and an edge crack bisecting the left side of cross section as shown in Fig. 12. The center of embedded crack is situated in the distance $d=2a/3$ from the left side of the cross section. The thickness of the coating is assumed to be $h_2=0.1a$. The variations of normalized stress intensity factors of the singular crack tips $k_{III}a^{2.5}/M$ versus the normalized parameter $l/a$ are presented in Fig. 12. As can be seen from this graph, stress intensity factors, increase rapidly while the distance between the singular crack tips $(R_1,L_2)$ decreases. The formation of regions with high stress levels is because of the interaction of geometric singularities. The graph of normalized torsional rigidity $10^4D/\mu_1a^4$ versus the normalized parameter $l/a$ is depicted in Fig. 13. As expected, the existence of cracks makes the normalized torsional rigidities to be less when the crack length grows.

![](./images/811035415069851649_14.jpg)

Fig. 12. Variation of $k_{III}a^{2.5}/M$ versus normalized crack length $l/a$ for an embedded crack and an edge crack

![](./images/811035415069851649_15.jpg)

Fig. 13. Values of $10^{4}D/\mu_{1}a^{4}$ versus normalized crack length $l/a$ for an embedded crack and an edge crack

The variation of dimensionless stress intensity factors with the dimensionless thickness is depicted in Fig. 14 by considering $l = 0.15a$. As we expected, normalized torsional rigidities begin to go up as the crack length grows up

![](./images/811035415069851649_16.jpg)

Fig. 14. Variation of dimensionless stress intensity factor $k_{III}a^{2.5}/M$ versus dimensionless thickness of the coating for an embedded crack and an edge crack

### Example 7. Two embedded circular arc cracks

In the last example, we consider a rectangular cross section bar with an isotropic coating weakened by two embedded circular arc cracks with identical radii $R = 0.1h_1$. Centers of embedded cracks with lengths $2l$ are situated on the horizontal center-line of the cross section of the bar in the distances $0.2h_1$ and $0.4h_1$ from the right side of the cross section, respectively. The thickness of the coating is considered $h_2 = 0.1a$. Variations of $k_{III}a^{2.5}/M$ for all singular crack tips versus the normalized half length of the crack $l/a$ are illustrated in Fig. 15. The normalized stress intensity factors for all of the crack tips begin to go up by growing the crack length because of interaction between the crack tips. Generally speaking, one would expect an increasing for normalized stress intensity factor $R_1$ by growing the crack length and approaching to the crack tip $L_2$, but we notice that for the crack tip $R_1$, a reduction in stress intensity factor occurs because of receding from the crack tips $L_1$ and $L_2$. It is because of a compromise between some contrary effects. The plot of normalized torsional rigidity $10^4D/\mu_1a^4$ against normalized half crack length $l/a$ can be observed in Fig. 16. Similar to the former examples, with growing the crack length, the cross-section being weaker and then the torsional rigidity decreases.

![](./images/811035415069851649_17.jpg)

Fig. 15. Variation of $k_{III}a^{2.5}/M$ versus dimensionless crack length $l/a$ for two embedded cracks

![](./images/811035415069851649_18.jpg)

Fig. 16. Values of $10^4 D/\mu_1 a^4$ versus non-dimensional crack length $l/a$ for two embedded cracks

The variation of stress intensity factors for two semicircular cracks with the dimensionless thickness can be observed in Fig. 17. The similar trend of the previous example for variations of the normalized stress intensity factors against normalized thickness ratio can be realized.

![](./images/811035415069851649_19.jpg)

Fig. 17. Variation of dimensionless stress intensity factor $k_{III}a^{2.5}/M$ versus dimensionless thickness of the coating for two embedded cracks

## 5. Conclusion
This work presented an efficient dislocation approach for the evaluation of the stress intensity factors for multiple arbitrarily shaped cracks in a rectangular cross section bar with an isotropic coating. A solution of the torsion problem of a rectangular cross section bar with an isotropic coating weakened by Volterra-type dislocation was first presented in terms of dislocation density. The problem was reduced to a set of singular integral equations of Cauchy singular type in the rectangular cross section, by using the distribution dislocation technique to analyze the problem with multiple smooth cracks. The integral equations were solved numerically by reducing them to a system of algebraic equations. Finally, the stress intensity factor for the crack tips and the torsional rigidity of the domain under consideration were evaluated. To summarize, the stress intensity factors of crack tips and torsional rigidity in the rectangular cross section with the isotropic coating were found to depend on critical factors such as the distance of the crack tip from the free boundary of the domain, thickness of the coating, crack length and the interaction between the cracks.

## Appendix. A : Proof of Eq. (15)
We have

$$
\Gamma_{n}=\frac{1}{\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(h_{1} \kappa n\right)+\sinh \left(h_{1} \kappa n\right) \cosh \left(h_{2} \kappa n\right)} \tag{A-1}
$$

The $\Gamma_{n}$ can be simplified as

$$
\begin{aligned}
\Gamma_{n} & =\frac{1}{(\mu+1) \sinh \left(n \kappa\left(h_{1}+h_{2}\right)\right)+(1-\mu) \sinh \left(n \kappa\left(h_{1}-h_{2}\right)\right)} \\
& =\frac{2}{\mu+1} \frac{1}{\sinh \left(n \kappa\left(h_{1}+h_{2}\right)\right)} \frac{1}{1+\frac{1-\mu}{1+\mu} \frac{\sinh \left(n \kappa\left(h_{1}-h_{2}\right)\right)}{\sinh \left(n \kappa\left(h_{1}+h_{2}\right)\right)}}
\end{aligned}
$$

Using the expansions $\frac{1}{\sinh (H)}=2 \sum_{m=1}^{\infty} e^{-(2 m-1) H}$ and $\frac{1}{1+X}=\sum_{j=0}^{\infty} X^{m}$ results in

$$
\begin{aligned}
\Gamma_{n} & =\frac{4}{\mu+1} \sum_{m=1}^{\infty} e^{-(2 m-1) n \kappa(h 1+h 2)} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu} e^{-2 n \kappa h_{2}} \frac{1-e^{-2 n \kappa\left(h_{1}-h_{2}\right)}}{1-e^{-2 n \kappa\left(h_{1}+h_{2}\right)}}\right)^{j} \\
& =\frac{4}{\mu+1} \sum_{m=1}^{\infty} e^{-(2 m-1) n \kappa(h 1+h 2)} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu} e^{-2 n \kappa h_{2}}\right)^{j}\left(1-e^{-2 n \kappa\left(h_{1}-h_{2}\right)}\right)^{j}\left(1-e^{-2 n \kappa\left(h_{1}+h_{2}\right)}\right)^{-j}
\end{aligned}
$$

A-3

With the aid of the expansions $\left(1-e^{z}\right)^{j}=\sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}j \\ i\end{array}\right)\left(e^{z}\right)^{j-i}$ and $\left(1-e^{z}\right)^{-j}=\sum_{k=0}^{\infty}\left(\begin{array}{c}k+j-1 \\ k\end{array}\right)\left(e^{z}\right)^{k}$ (see Reference [37]), Eq.( A-3) can be written in following form

$$
\Gamma_{n}=4 \sum_{j=0}^{\infty} \frac{(1-\mu)^{j}}{(1+\mu)^{j+1}} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\left(e^{-2 h_{2} j} e^{-2 h^{\prime}(j-i)} e^{-2 h k} e^{-(2 m+1) h) n \kappa}\right.
$$

A-3

### Appendix. B: Proof of Eq.(16)

By means of exponential definition of sine and cosine, we have

$$
\begin{aligned}
& \sum_{n=1}^{\infty} K^{n} e^{\kappa n y} \sin (n \kappa x)=\frac{1}{2 i}\left(\frac{e^{(i X+y) \kappa} K}{1-e^{(i X+y) \kappa} K}-\frac{e^{(-i X+y) \kappa} K}{1-e^{(-i X+y) \kappa} K}\right) \\
& =\frac{1}{2} \frac{\sin (\kappa x)}{\cosh (y k+\ln (K))-\cos (\kappa X)}
\end{aligned}
$$

B-1

and

$$
\begin{aligned}
& \sum_{n=1}^{\infty} K^{n} e^{\kappa n y} \cos (n \kappa x)=\frac{1}{2}\left(\frac{e^{(i X+y) \kappa} K}{1-e^{(i X+y) \kappa} K}+\frac{e^{(-i X+y) \kappa} K}{1-e^{(-i X+y) \kappa} K}\right) \\
& =-\frac{1}{2}\left(1+\frac{\sinh (y k+\ln (K))}{\cosh (y k+\ln (K))-\cos (\kappa X)}\right)
\end{aligned}
$$

B-2

With aid of the definition of Hyperbolic functions and expansion $\Gamma_{n}$, Eq. (16) can be written as below

$$
\begin{aligned}
& \sum_{n=1}^{\infty} \Gamma_{n} \sinh (n \kappa y)\left\{\begin{array}{l}
\cos (n \kappa x) \\
\sin (n \kappa x)
\end{array}\right\}=\frac{2}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right) \\
& \sum_{n=1}^{\infty}\left(\left(e^{-2 \kappa h_{2}}\right)^{j}\left(e^{-2 \kappa\left(h_{1}-h_{2}\right)}\right)^{j-i}\left(e^{-2 \kappa(h 1+h 2)}\right)^{k} e^{-(2 m+1) \kappa(h 1+h 2)) n}\left(e^{n \kappa y}-e^{-n \kappa y}\right)\left\{\begin{array}{l}
\cos (n \kappa x) \\
\sin (n \kappa x)
\end{array}\right\}\right.
\end{aligned}
$$

B-3

With aid of Eq. (B-1) and (B-2) we have

$$
\sum_{n=1}^{\infty} \Gamma_{n} \sinh (n k y)\left\{\begin{array}{l}
\cos (n \kappa x) \\
\sin (n \kappa x)
\end{array}\right\}=\frac{-1}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right)
$$

$$
\sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\left\{\begin{array}{l}
F_{i j}^{k m}(x, y)-F_{i j}^{k m}(x,-y) \\
-E_{i j}^{k m}(x, y)+E_{i j}^{k m}(x,-y)
\end{array}\right\}
$$

### Appendix. C:

$$
\varphi_{1}(X, \xi, Y, \eta)=-\frac{1}{8} \frac{1}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\{(\mu+1)
$$

$$
\begin{aligned}
& \left(F_{i j}^{k m}(X-\xi, Y-\eta-h_{1}-h_{2})-F_{i j}^{k m}(X-\xi,-(Y-\eta-h_{1}-h_{2}))-F_{i j}^{k m}(X+\xi, Y-\eta-h_{1}-h_{2})\right. \\
& \left.+F_{i j}^{k m}(X+\xi,-(Y-\eta-h_{1}-h_{2}))\right)-(\mu+1)\left(F_{i j}^{k m}(X-\xi, Y+\eta-h_{1}-h_{2})\right. \\
& -F_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}-h_{2}))-F_{i j}^{k m}(X+\xi, Y+\eta-h_{1}-h_{2})+F_{i j}^{k m}(X+\xi,-(Y+\eta-h_{1}-h_{2}))) \\
& -(\mu-1)\left(F_{i j}^{k m}(X-\xi, Y-\eta-h_{1}+h_{2})-F_{i j}^{k m}(X-\xi,-(Y-\eta-h_{1}+h_{2}))\right. \\
& \left.-F_{i j}^{k m}(X+\xi, Y-\eta-h_{1}+h_{2})+F_{i j}^{k m}(X+\xi,-(Y-\eta-h_{1}+h_{2}))\right)+(\mu-1) \\
& \left(F_{i j}^{k m}(X-\xi, Y+\eta-h_{1}+h_{2})-F_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}+h_{2}))-F_{i j}^{k m}(X-\xi, Y+\eta-h_{1}+h_{2})\right. \\
& \left.\left.+F_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}+h_{2}))\right)\right\}, \quad Y_{j} \leq Y_{i} \leq h_{1}
\end{aligned}
$$

$$
\varphi_{2}(X, \xi, Y, \eta)=-\frac{1}{8} \frac{1}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\{-(\mu+1)
$$

$$
\begin{aligned}
& \left(F_{i j}^{k m}(X-\xi, Y+\eta-h_{1}-h_{2})-F_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}-h_{2}))-F_{i j}^{k m}(X+\xi, Y+\eta-h_{1}-h_{2})\right. \\
& \left.+F_{i j}^{k m}(X+\xi,-(Y+\eta-h_{1}-h_{2}))\right)-(\mu-1)\left(F_{i j}^{k m}(X-\xi, Y-\eta+h_{1}-h_{2})\right. \\
& -F_{i j}^{k m}(X-\xi,-(Y-\eta+h_{1}-h_{2}))-F_{i j}^{k m}(X+\xi, Y-\eta+h_{1}-h_{2})+F_{i j}^{k m}(X+\xi,-(Y-\eta+h_{1}-h_{2}))) \\
& +(\mu-1)\left(F_{i j}^{k m}(X-\xi, Y+\eta-h_{1}+h_{2})-F_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}+h_{2}))\right. \\
& \left.-F_{i j}^{k m}(X+\xi, Y+\eta-h_{1}+h_{2})+F_{i j}^{k m}(X+\xi,-(Y+\eta-h_{1}+h_{2}))\right)+(\mu+1) \\
& \left(F_{i j}^{k m}(X-\xi, Y-\eta+h_{1}+h_{2})-F_{i j}^{k m}(X-\xi,-(Y-\eta+h_{1}+h_{2}))-F_{i j}^{k m}(X-\xi, Y-\eta+h_{1}+h_{2})\right. \\
& \left.\left.+F_{i j}^{k m}(X-\xi,-(Y-\eta+h_{1}+h_{2}))\right)\right\}, \quad 0 \leq Y_{i} \leq Y_{j}
\end{aligned}
$$

$$
\psi_{1}(X, \xi, Y, \eta)=-\frac{1}{8} \frac{1}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\{(\mu-1)
$$

$$
\begin{aligned}
& \left(E_{i j}^{k m}(X-\xi, Y-\eta-h_{1}-h_{2})+E_{i j}^{k m}(X-\xi,-(Y-\eta-h_{1}-h_{2}))-E_{i j}^{k m}(X+\xi, Y-\eta-h_{1}-h_{2})\right. \\
& \left.-E_{i j}^{k m}(X+\xi,-(Y-\eta-h_{1}-h_{2}))\right)-(\mu-1)\left(E_{i j}^{k m}(X-\xi, Y+\eta-h_{1}-h_{2})\right. \\
& +E_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}-h_{2}))-E_{i j}^{k m}(X+\xi, Y+\eta-h_{1}-h_{2})-E_{i j}^{k m}(X+\xi,-(Y+\eta-h_{1}-h_{2}))) \\
& -(\mu+1)\left(E_{i j}^{k m}(X-\xi, Y-\eta-h_{1}+h_{2})+E_{i j}^{k m}(X-\xi,-(Y-\eta-h_{1}+h_{2}))\right. \\
& \left.-E_{i j}^{k m}(X+\xi, Y-\eta-h_{1}+h_{2})-E_{i j}^{k m}(X+\xi,-(Y-\eta-h_{1}+h_{2}))\right)+(\mu+1) \\
& \left(E_{i j}^{k m}(X-\xi, Y+\eta-h_{1}+h_{2})+E_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}+h_{2}))-E_{i j}^{k m}(X-\xi, Y+\eta-h_{1}+h_{2})\right. \\
& \left.\left.-E_{i j}^{k m}(X-\xi,-(Y+\eta-h_{1}+h_{2}))\right)\right\}, \quad Y_{j} \leq Y_{i} \leq h_{1}
\end{aligned}
$$

$$
\psi_{2}(X, \xi, Y, \eta)=-\frac{1}{8} \frac{1}{\mu+1} \sum_{j=0}^{\infty}\left(\frac{1-\mu}{1+\mu}\right)^{j} \sum_{i=0}^{j}(-1)^{i}\left(\begin{array}{l}
j \\
i
\end{array}\right) \sum_{m=0}^{\infty} \sum_{k=0}^{\infty}\left(\begin{array}{c}
k+j-1 \\
k
\end{array}\right)\{-(\mu+1)
$$

$$
\begin{aligned}
& \left(E_{i j}^{k m}\left(X-\xi, Y-\eta-h_{1}-h_{2}\right)+E_{i j}^{k m}\left(X-\xi,-\left(Y-\eta-h_{1}-h_{2}\right)\right)-E_{i j}^{k m}\left(X+\xi, Y-\eta-h_{1}-h_{2}\right)\right. \\
& \left.-E_{i j}^{k m}\left(X+\xi,-\left(Y-\eta-h_{1}-h_{2}\right)\right)\right)-(\mu-1)\left(E_{i j}^{k m}\left(X-\xi, Y+\eta-h_{1}-h_{2}\right)\right. \\
& \left.+E_{i j}^{k m}\left(X-\xi,-\left(Y+\eta-h_{1}-h_{2}\right)\right)-E_{i j}^{k m}\left(X+\xi, Y+\eta-h_{1}-h_{2}\right)-E_{i j}^{k m}\left(X+\xi,-\left(Y+\eta-h_{1}-h_{2}\right)\right)\right) \\
& +(\mu-1)\left(E_{i j}^{k m}\left(X-\xi, Y-\eta-h_{1}+h_{2}\right)+E_{i j}^{k m}\left(X-\xi,-\left(Y-\eta-h_{1}+h_{2}\right)\right)\right. \\
& \left.-E_{i j}^{k m}\left(X+\xi, Y-\eta-h_{1}+h_{2}\right)-E_{i j}^{k m}\left(X+\xi,-\left(Y-\eta-h_{1}+h_{2}\right)\right)\right)+(\mu+1) \\
& \left(E_{i j}^{k m}\left(X-\xi, Y+\eta-h_{1}+h_{2}\right)+E_{i j}^{k m}\left(X-\xi,-\left(Y+\eta-h_{1}+h_{2}\right)\right)-E_{i j}^{k m}\left(X+\xi, Y+\eta-h_{1}+h_{2}\right)\right. \\
& \left.\left.-E_{i j}^{k m}\left(X+\xi,-\left(Y+\eta-h_{1}+h_{2}\right)\right)\right)\right\}, \quad 0 \leq Y_{i} \leq Y_{j}
\end{aligned}
$$

$$
\begin{aligned}
& U_{j}(\eta, \xi)=\frac{16 a^{2} \mu_{1}}{\pi^{3} n^{3}} \sum_{n=1,3,5}^{\infty} \frac{\Gamma_{n}}{n^{3}} \sinh (n \kappa \eta / 2) \sin (n \kappa \xi)[\cosh (n \kappa \eta / 2) \\
& \left(\mu\left(\sinh \left(n \kappa h_{1}\right) \sinh \left(n \kappa h_{2}\right)-1\right)+\cosh \left(n \kappa h_{2}\right)\left(\cosh \left(n \kappa h_{1}\right)+\mu-1\right)\right) \\
& \left.-\sinh (n \kappa \eta / 2)\left(\mu \sinh \left(n \kappa h_{2}\right) \cosh \left(n \kappa h_{1}\right)+\sinh \left(n \kappa h_{1}\right) \cosh \left(n \kappa h_{2}\right)\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& P_{i}(X, Y)=\mu_{1}(2 X-a) \cos \phi_{i}-\frac{2 \kappa \mu_{1}}{a}\{\cos \phi_{i} \sum_{n=1}^{\infty} \Omega_{n} n[\sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right) \\
& +(\mu-1) \cosh \left(h_{2} \kappa n\right) \sinh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \\
& \left.-\mu \sinh (n \kappa(y+\eta))] \cos (n \kappa X)+\sin \phi_{i} \sum_{n=1}^{\infty} \Omega_{n} n[\cosh \left(\kappa n\left(y+\eta-h_{1}\right)\right) \cosh \left(h_{2} \kappa n\right)\right) \\
& \left.+(\mu-1) \cosh \left(h_{2} \kappa n\right) \cosh (n \kappa(y+\eta))-\mu \sinh \left(h_{2} \kappa n\right) \sinh \left(\kappa n\left(y+\eta-h_{1}\right)\right)\right) \\
& \left.-\mu \cosh (n \kappa(y+\eta))] \sin (n \kappa X)\right\}
\end{aligned}
$$

### References

[1] R.Q. Xu, J.S. He and W.Q. Chen, Saint-Venant torsion of orthotropic bars with inhomogeneous rectangular cross section, Composite Structures, 92 1449-1457 (2010).

[2] I. Ecsedi, Some analytical solutions for Saint-Venant torsion of non-homogeneous cylindrical bars, European Journal of Mechanics - A/Solids, 28 985-990 (2009).

[3] R. Santoro, The line element-less method analysis of orthotropic beam for the De Saint Venant torsion problem, International Journal of Mechanical Sciences, 52 43-55 (2010).

[4] A.W. Leissa and J.H. Brann, On the torsion of bars having symmetry axes, International Journal of Mechanical Sciences, 6 45-50 (1964).

[5] R. Pavazza, Torsion of thin-walled beams of open cross-section with influence of shear, International Journal of Mechanical Sciences, 47 1099-1122 (2005).

[6] H. Teimoori, R.T. Faal and R. Das, Saint-Venant torsion analysis of bars with rectangular cross-section and effective coating layers, Applied Mathematics and Mechanics, 37 237-252 (2016).

[7] Y.-Z. Chen, Solutions of torsion crack problems of a rectangular bar by harmonic function continuation technique, Engineering Fracture Mechanics, 13 193-212 (1980).

[8] Y.Z. Chen, X.Y. Lin and R.S. Chen, Solution of torsion crack problem of an orthotropic rectangular bar by using computing compliance method, Communications in Numerical Methods in Engineering, 13 655-663 (1997).

[9] Y.-Z. Chen, Torsion problem of rectangular cross section bar with inner crack, Computer Methods in Applied Mechanics and Engineering, 162 107-111 (1998).

[10] A.R. Hassani and R.T. Faal, Saint-Venant torsion of orthotropic bars with rectangular cross section weakened by cracks, International Journal of Solids and Structures, 52 165-179 (2015).

[11] Y.-Z. Chen and X.-F. Wu, Solutions of multiple crack problems of a circular region for antiplane elastic problem or torsion problem by using Fredholm integral equation approach, International Journal of Fracture, 25 R15-R19 (1984).

[12] N.I.N. Lebedev, I.P. Skalskaya, I.A.S. Ufland and R.A. Silverman, Worked Problems in Applied Mathematics,(Dover Publications 1979).

[13] X.C. Wang and R.J. Tang, On the torsion of a cylinder with several cracks, Applied Mathematics and Mechanics, 9 745-754 (1988).

[14] J. Tweed and D.P. Rooke, The torsion of a circular cylinder containing a symmetric array of edge cracks, International Journal of Engineering Science, 10 801-812 (1972).

[15] Y. Wang, Torsion of a thick-walled cylinder with an external crack: boundary collocation method, Theoretical and Applied Fracture Mechanics, 14 267-273 (1990).

[16] Y.-Z. Chen, Multiple crack problems for torsion thin-walled cylinder, International Journal of Pressure Vessels and Piping, 76 49-53 (1999).

[17] G.C. Sih, Strength of Stress Singularities at Crack Tips for Flexural and Torsional Problems, Journal of Applied Mechanics, 30 419-425 (1963).

[18] F.M. Tao and R.J. Tang, Saint-Venant's torsion problem for a composite circular cylinder with aninternal edge crack, Applied Mathematics and Mechanics, 14 507-516 (1993).

[19] A.R. Hassani and R.T. Faal, Saint-Venant torsion of orthotropic bars with a circular cross- section containing multiple cracks, Mathematics and Mechanics of Solids, 21 1198-1214 (2014).

[20] A.R. Hassani and R.T. Faal, Torsion analysis of cracked circular bars actuated by a piezoelectric coating, Smart Materials and Structures, 25 125030 (2016).

[21] B. Liang and X.S. Zhang, The problem of a concentric penny-shaped crack of mode III in a nonhomogeneous finite cylinder, Engineering Fracture Mechanics, 42 79-85 (1992).

[22] X.S. Zhang and Y.U. Zhang, A concentric penny-shaped crack off the middle plane of a finite orthotropic cylinder under torsional shear stress, Engineering Fracture Mechanics, 31 385-393 (1988).

[23] X.S. Zhang, Off-plane concentric penny-shaped crack in a finite cylinder under arbitrary torsion, Theoretical and Applied Fracture Mechanics, 9 263-270 (1988).

[24] X.S. Zhang, The general solution of a finite orthotropic cylinder with a concentric penny- shaped crack under torsion, Engineering Fracture Mechanics, 31 827-835 (1988).

[25] S.S. Chang, The general solution of a finite cylinder with a concentric penny-shaped crack under torsion, Engineering Fracture Mechanics, 22 571-578 (1985).

[26] B.A. Kudriavtsev and V.Z. Parton, Torsion and extension of a cylinder with an external annular slit, Journal of Applied Mathematics and Mechanics, 37 297-306 (1973).

[27] P. Lazzarin, M. Zappalorto and J.R. Yates, Analytical study of stress distributions due to semi- elliptic notches in shafts under torsion loading, International Journal of Engineering Science, 45 308-328 (2007).

[28] M. Zappalorto, P. Lazzarin and F. Berto, Elastic notch stress intensity factors for sharply V- notched rounded bars under torsion, Engineering Fracture Mechanics, 76 439-453 (2009).

[29] A.R. Hassani, R.T. Faal and N.A. Noda, Torsion analysis of finite solid circular cylinders with multiple concentric planar cracks, ZAMM-Journal of Applied Mathematics and Mechanics/Zeitschrift für Angewandte Mathematik und Mechanik, (2016).

[30] J.R. Barber, Elasticity,(Springer 2009).

[31] R.T. Faal, A.R. Fotuhi, S.J. Fariborz and H.R. Daghyani, Antiplane stress analysis of an isotropic wedge with multiple cracks, International Journal of Solids and Structures, 41 4535-4550 (2004).

[32] R.T. Faal, M. Daliri and A.S. Milani, Anti-Plane stress analysis of orthotropic rectangular planes weakened by multiple defects, International Journal of Solids and Structures, **48** 661-672 (2011).

[33] A.M. Korsunsky and D.A. Hills, The Solution of Crack Problems by Using Distributed Strain Nuclei, Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, **210** 23-31 (1996).

[34] D.A. Hills, P.A. Kelly, D.N. Dai and A.M. Korsunsky, Solution of Crack Problems: The Distributed Dislocation Technique,(Springer 1996).

[35] R.T. Faal, S.J. Fariborz and H.R. Daghyani, Antiplane deformation of orthotropic strips with multiple defects, Journal of Mechanics of Materials and Structures, **1** 1097-1114 (2006).

[36] F. Erdogan, G.D. Gupta and T.S. Cook, Numerical solution of integral equations. In: Sih, G.C. (Ed.), Methods of Analysis and Solution of Crack Problems,(Noordhoof, Leyden, Holland 1973).

[37] M.R. Spiegel, S. Lipschutz and J. Liu, Schaum's Outline of Mathematical Handbook of Formulas and Tables, 3ed,(McGraw-Hill Education 2008).

### Highlights
- We analyze the torsion problem of a rectangular bar with an effective coating containing a screw dislocation.
- The bar and its coating are governed by the Saint-Venant torsion theory.
- We use the dislocation distribution technique for analysis of multiple arbitrary oriented curved cracks.
- We rewrite the solution of problem in term of new functions which converge very rapidly.
- The stress components of the dislocation solution have Cauchy singularity.
- By enhancing crack length, the stress intensity factor of crack tip is increased.
- Approaching of the crack tips to the stress free surface decrease the normalized stress intensity factor.
- The stress intensity factor of the crack tip increases as it approaches the other singular crack tips.
- The normalized stress intensity factor is reduced by enlarging thickness of the coating