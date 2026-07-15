This article was downloaded by: [Tufts University]
On: 27 October 2014, At: 07:40
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954
Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812088170614095874_1.jpg)

# Molecular Physics: An International Journal at the Interface Between Chemistry and Physics

Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/tmph20

# Further investigations into the low-density behaviour of the hypernetted chain equation for ionic fluids

Johan S. Høye $^{a}$ , Enrique Lomba $^{b c}$ & George Stell $^{d e}$

$^{a}$ Institutt for Fysikk, Universitetet i Trondheim, N-7034, Trondheim-NTH, Norway
$^{b}$ Instituto de Química Física Rocasolano, CSIC, Serrano 119, E-28006, Madrid, Spain
$^{c}$ Departamento Química Física I, U. Complutense, E-28040, Madrid, Spain
$^{d}$ Department of Chemistry, State University of New York at Stony Brook, Stony Brook, NY, 11794, USA
$^{e}$ Department Mechanical Engineering, State University of New York at Stony Brook, Stony Brook, NY, 11794, USA

Published online: 23 Aug 2006.

To cite this article: Johan S. Høye, Enrique Lomba & George Stell (1992) Further investigations into the low-density behaviour of the hypernetted chain equation for ionic fluids, Molecular Physics: An International Journal at the Interface Between Chemistry and Physics, 75:5, 1217-1232, DOI: 10.1080/00268979200100931

To link to this article: http://dx.doi.org/10.1080/00268979200100931

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable

for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden.

Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

MOLECULAR PHYSICS, 1992, VOL. 75, No. 5, 1217-1232

# Further investigations into the low-density behaviour of the hypernetted chain equation for ionic fluids

By JOHAN S. HØYE

Institutt for Fysikk, Universitetet i Trondheim, N-7034 Trondheim-NTH, Norway

ENRIQUE LOMBA

Instituto de Química Física Rocasolano, CSIC, Serrano 119, E-28006 Madrid, Spain and Departamento Química Física I, U. Complutense, E-28040 Madrid, Spain

and GEORGE STELL

Departments of Chemistry and Mechanical Engineering, State University of New York at Stony Brook, Stony Brook, NY 11794, USA

(Received 9 September 1991; accepted 31 October 1991)

We describe the low-density behaviour of the hypernetted chain equation (HNC) for the restricted primitive model (RPM) of ionic fluids. An efficient computational procedure is developed and applied to the study of the thermo-dynamics and convergency behaviour in the low density and low temperature (or high ionic strength) region in which there is evidence of liquid-gas coexistence. After a careful study, we attribute the divergence found on the liquid side of the coexistence curve to the presence of a spinodal line. In contrast, divergences on the gas side (low density) are unphysical and appear to result from intrinsic inconsistencies in the HNC approximation. We remark upon the effect that the presence of a 'cavity term' added to the RPM pair potential can be expected to have upon the phase-separation behaviour in the HNC approximation as well in a more exact analysis.

## 1. Introduction

Since the original work of Stell, Wu and Larsen [1] the determination of the low density coexistence curve for the restricted primitive model of electrolytes (and related models) has attracted a great deal of research in fluid-state physics$\dagger$. Later work by Gillan [2] showed clear evidence of the poor ability of the existing theories to cope quantitatively with the problem, especially on the gas (low-density) side of the coexistence. In the case of the mean spherical approximation (MSA) and its variants

$\dagger$ The restricted primitive model—symmetrically charged hard-sphere anions and cations —is used as a model of both electrolyte solutions and molten salts. In the latter role, the fluid-fluid branch of the RPM coexistence curve is to be identified with liquid-gas coexistence. In the former role, the presence of a solvent modelled as an inert structureless continuum suggests that the coexistence should instead be interpreted as the liquid-liquid phase separation or demixing that is found in some electrolytes. (For many real electrolytes, one anticipates that solvent-induced freezing, an effect not incorporated into the RPM, will occur to mask the incipient demixing of ionic solute.) For clarity and convenience throughout this paper we shall use the simpler terminology of solvent-free coexistence in discussing our results. Thus we talk about the 'gas-side' of the coexistence curve and 'low-density', rather than the 'less-dense fluid side' of the coexistence curve and 'low ionic concentration'.

0026-8976/92 $3.00 © 1992 Taylor & Francis Ltd

These limitations are connected to the inherent linearity in the closure relation, which prevents ionic association from being properly taken into account. The non-linear hypernetted chain approximation might well be an alternative approach to the problem. In this context Abernethy and Gillan [3] solved the HNC equation for a simple model of Coulombic fluid in which the hard sphere potential was replaced by a 'soft' repulsive term. Their work, however, concentrated on the molten salt regime, for which at very high ionic strengths they found divergences, which they thought were connected to the presence of a spinoidal line. A similar situation was later found by Belloni [4] for a highly asymmetric coulombic fluid.

In a recent work, Kinoshita and Harada [5] reconsidered the original calculations of Abernethy and Gillan using an extension of their numerical algorithm, and found strikingly that the isothermal compressibility reaches large but finite values at the so-called spinodal line for low densities. It then became clear that the boundary of the no-solution region could not be the spinodal line.

We will here attempt to throw some light onto this rather confusing situation. Therefore, in this paper we study not only the behaviour of the correlation functions but the thermodynamics of the system, with special emphasis on the thermodynamic potentials: the Helmholtz free energy and chemical potential.

The solution of the HNC equation in the low-density region is by itself a consider- able task. One has to consider not only the long range of the coulombic potential (and the direct correlation functions) but also the long range in the pair distribution function at low densities (given by the inverse of the Debye screening parameter, $\kappa_{D}$). We have developed an algorithm capable of handling these long range functions, minimizing errors during the iteration procedure (especially forward and backward Fourier transforms) and in the integration of thermodynamic quantities, but at the same time stable and fast enough to map out the entire locus of no solution.

It was Gillan [6] who first proposed an efficient procedure to solve the Orstein- Zernike (OZ) equation inspired by the Newton-Raphson method. The correlation functions are split into 'coarse' and 'fine' parts, and the 'coarse' part is expanded into a set of basis functions. The Newton-Raphson iterations are applied only to the coefficients of the 'coarse' components of the correlation functions.

In a subsequent paper Abernethy and Gillan [3] extended the original Gillan's method to mixtures. Their procedure was considerably improved by Kinoshita and Harada [5] who realized that the Jacobian matrix of the Newton-Raphson iteration remains approximately constant for a given system, i.e. independent of temperature and density. Gillan's method was further enhanced by Labik, Malijevsky and Vonka [7] who introduced a different and more natural basis set for the expansion of the coarse part (trigonometric functions). This method, hereafter referred to as LMV, has been generalized to mixtures (in particular, coulombic systems) by Ichiye and Haymet [8]. Also, one of us [9] has successfully applied the Kinoshita-Harada iteration strategy in the context of the LMV method to obtain the phase equilibrium for a simple Lennard-Jones fluid in the reference hypernetted chain (RHNC) approximation [9].

As suggested in [5] and [9] the most useful application of the Kinoshita-Harada iteration strategy is to fluid mixtures. In this work therefore, we have developed a procedure for solving the OZ equation in ionic fluids (the so called 'renormalized' OZ, according to [8]) which includes both the extension of the LMV method to mixtures (in a slightly different formulation from [8]) together with the Kinoshita-Harada iteration strategy. As mentioned before, we have paid special attention to the treat-

ment of long range interactions, particularly in the computation of thermodynamic potentials.

The details of the computational procedure are described in section 2. In section 3 we have made extensive use of the procedure and carefully mapped out the no-solution region, focusing on the evolution of thermodynamic qualities in the vicinity of the divergence locus. The nature of the observed divergences becomes apparent when considering the behaviour of the isothermal compressibility and those components of the OZ relation which may cause instabilities in the numerical algorithm (see (41) in section 3).

## 2. Computational procedure

Three main aspects will be considered in this section. First, we will rederive in section 2.1 the renormalized OZ for Coulombic potential [8, 10] for which we have introduced some minor modifications that improve its numerical efficiency. Second, in section 2.2 we summarize the relevant aspects of the method of solution, and finally, the explicit expressions for the evaluation of thermodynamic properties are given in section 2.3. Explicit programming details as well as program source code can be found in [11].

### 2.1. Renormalized OZ equation

The interaction potential for the primitive model of electrolytes is
$$
u_{\alpha \beta}(r)=u_{\alpha \beta}^{\mathrm{HS}}(r)+\frac{Z_{\alpha} Z_{\beta} e^{2}}{\varepsilon r}. \tag{1}$$

Here $Z_{\alpha}$ and $Z_{\beta}$ are the electric charges of particles $\alpha$ and $\beta$, $\varepsilon$ is the dielectric constant of the solvent and $u_{\alpha \beta}^{\mathrm{HS}}$ is the hard sphere potential between these two particles, i.e.,
$$
u_{\alpha \beta}^{\mathrm{HS}}(r)= \begin{cases}\infty, & \text { if } r<\sigma_{\alpha \beta}, \\ 0, & \text { if } r \geqslant \sigma_{\alpha \beta},\end{cases} \tag{2}$$
and $\sigma_{\alpha \beta}=(\sigma_{\alpha \alpha}+\sigma_{\beta \beta}) / 2$, with $\sigma_{\alpha \alpha}$ the diameter of the $\alpha$ ion (and similarly for the $\beta$ ion). In what follows we will define the unit length as the largest ionic diameter (notice that for the RPM $\sigma_{\alpha \alpha}=\sigma_{\beta \beta}$).

Following previous work [8, 10] we split the interaction potential into short- and long-range components
$$
u_{\alpha \beta}(r)=u_{\alpha \beta}^{\mathrm{sr}}(r)+u_{\alpha \beta}^{\mathrm{lr}}(r), \tag{3}$$
where we have
$$-\beta u_{\alpha \beta}^{\mathrm{lr}}(r)=-\Gamma \frac{Z_{\alpha} Z_{\beta}}{r}\left(1-\mathrm{e}^{-\xi r}\right) \tag{4}$$
and $\Gamma=e^{2} / \varepsilon k T$ ($e$ is the electron charge) is the reduced inverse temperature (also denoted in the literature by $\beta^{*}$). In contrast to [8] we have, however, included a Yukawa term in (4) in order to minimize errors in the evaluation of Fourier transforms of short-range functions [2, 12] by suppressing the divergence that would otherwise show up at $r=0$. The inverse length Yukawa parameter $\xi$ is determined empirically.

Next we define the matrix
$$\boldsymbol{c}^{\mathrm{sr}}(r)=\boldsymbol{c}(r)-\boldsymbol{\psi}, \tag{5}$$

with coefficients $c_{\alpha \beta}^{\mathrm{sr}}(r)=c_{\alpha \beta}(r)-\psi_{\alpha \beta}$, where $c_{\alpha \beta}(r)$ is the direct correlation function and we have introduced $\psi_{\alpha \beta}(r)=-\beta u_{\alpha \beta}^{\mathrm{lr}}(r)$. The corresponding Fourier transforms are

$$\tilde{c}_{\alpha \beta}^{\mathrm{sr}}(k)=\tilde{c}_{\alpha \beta}(k)-\tilde{\psi}_{\alpha \beta}(k),
\tag{6}$$

with

$$\tilde{\psi}_{\alpha \beta}(k)=-\frac{4 \pi \Gamma Z_{\alpha} Z_{\beta} \xi^{2}}{k^{4}+k^{2} \xi^{2}}.
\tag{7}$$

One can then define the matrix function $\tilde{\boldsymbol{v}}(k)$ by

$$\tilde{\boldsymbol{v}}^{-1}(k)=\boldsymbol{\rho}^{-1}-\tilde{\boldsymbol{\psi}}(k) \quad \rho_{\alpha \beta}=\rho_{\alpha} \delta_{\alpha \beta},
\tag{8}$$

with $\rho_{\alpha}$ being the number density of ions $\alpha$. In the primitive model of electrolytes, where the solvent is assumed to be a structureless continuum, this is equivalent to the concentration of ions $\alpha$ measured in numbers of ions per unit volume. Equation (8) leads to the following expression for its components in $k$-space

$$\tilde{v}_{\alpha \beta}(k)=\rho_{\alpha} \delta_{\alpha \beta}-\frac{4 \pi \rho_{\alpha} \rho_{\beta} \Gamma Z_{\alpha} Z_{\beta} \xi^{2}}{k^{4}+k^{2} \xi^{2}+\kappa_{\mathrm{D}}^{2} \xi^{2}}.
\tag{9}$$

This function is connected to a modified Debye-Hückel chain bond $\tilde{\boldsymbol{q}}(k)$ as follows

$$\rho \tilde{\boldsymbol{q}}(k) \boldsymbol{\rho}=\tilde{\boldsymbol{v}}(k)-\boldsymbol{\rho},
\tag{10}$$

(i.e. $\tilde{\boldsymbol{q}}(k)=\tilde{\boldsymbol{\psi}}(k)+\tilde{\boldsymbol{\psi}}(k)+\ldots$ ). This modified chain bond $\boldsymbol{q}(r)$ contains the long-range behaviour of the total correlation function $h_{\alpha \beta}(r)$ at low densities, thus the function

$$\boldsymbol{h}^{\mathrm{sr}}(r)=\boldsymbol{h}(r)-\boldsymbol{q}(r),
\tag{11}$$

must be short ranged for any density. The components of $\boldsymbol{q}(r)$ can be obtained from (8) and (10) in Fourier space as

$$\tilde{q}_{\alpha \beta}(k)=\frac{4 \pi \Gamma Z_{\alpha} Z_{\beta} \xi^{2}}{k_{+}^{2}-k_{-}^{2}}\left(\frac{1}{k^{2}+k_{+}^{2}}-\frac{1}{k^{2}+k^{2}}\right),
\tag{12}$$

with

$$k_{ \pm}^{2}=\left\{\xi^{2} \mp\left[\xi^{4}-4\left(\kappa_{\mathrm{D}} \xi\right)^{2}\right]^{1 / 2}\right\}^{2},
\tag{13}$$

and $\kappa_{\mathrm{D}}^{2}=4 \pi \Gamma\left(\rho_{\alpha} Z_{\alpha}^{2}+\rho_{\beta} Z_{\beta}^{2}\right)$. This latter quantity is the square of the inverse Debye screening length. The parameter $\xi$ must be chosen so as to produce real and non-negative values of $k_{ \pm}^{2}$. From (12) the chain bond in $r$-space is simply

$$q_{\alpha \beta}(r)=\frac{\Gamma \xi^{2} Z_{\alpha} Z_{\beta}}{k_{+}^{2}-k_{-}^{2}}\left(\frac{\mathrm{e}^{-k_{+} r}}{r}-\frac{\mathrm{e}^{-k_{-} r}}{r}\right).
\tag{14}$$

We can now rewrite the OZ equation for Coulombic mixtures using only short ranged functions. The OZ mixture equation in its usual form reads

$$h_{\alpha \beta}\left(r_{12}\right)-c_{\alpha \beta}\left(r_{12}\right)=\sum_{\lambda} \rho_{\lambda} \int c_{\alpha \lambda}\left(r_{13}\right) h_{\lambda \beta}\left(r_{32}\right) \mathrm{d} \boldsymbol{r}_{3}.
\tag{15}$$

This can be considerably simplified in Fourier space by introducing the functions

$$\begin{aligned}
\Gamma_{\alpha \beta}^{\mathrm{sr}}(r) & =r\left(h_{\alpha \beta}^{\mathrm{sr}}(r)-c_{\alpha \beta}^{\mathrm{sr}}(r)\right), \\
C_{\alpha \beta}^{\mathrm{sr}}(r) & =r c_{\alpha \beta}^{\mathrm{sr}}(r),
\end{aligned}
\tag{16}$$

and their density-scaled Fourier transforms
$$\tilde{\boldsymbol{\Gamma}}_{\alpha \beta}^{\mathrm{sr}}(k)=k\left(\rho_{\alpha} \rho_{\beta}\right)^{1 / 2}\left(h_{\alpha \beta}^{\mathrm{sr}}(k)-\tilde{c}_{\alpha \beta}^{\mathrm{sr}}(k)\right),\qquad(17)$$
and similarly for $\tilde{C}_{\alpha \beta}^{\mathrm{sr}}(k)$. One also introduces density factors in $\tilde{v}(k)$ by defining $\tilde{V}_{\alpha \beta}(k)=\left(\rho_{\alpha} \rho_{\beta}\right)^{-1 / 2} \tilde{v}_{\alpha \beta}(k)$. Notice that no additional $k$ factor enters this function and the exponent in the density factor is negative. With these modifications the renormalized Orstein-Zernike equation in matrix notation now has the form
$$\tilde{\boldsymbol{\Gamma}}^{\mathrm{sr}}=k^{2}\left[k \tilde{\boldsymbol{V}}^{-1}-\tilde{\boldsymbol{C}}^{\mathrm{sr}}\right]^{-1}-k \tilde{\boldsymbol{V}}-\tilde{\boldsymbol{C}}^{\mathrm{sr}}.\qquad(18)$$

The closure relation must be subsequently changed according to the new functions. For the HNC relation one gets
$$C_{\alpha \beta}^{\mathrm{sr}}(r)=r \exp \left(-\beta u_{\alpha \beta}^{\mathrm{sr}}(r)+\Gamma_{\alpha \beta}^{\mathrm{sr}}(r) / r+q_{\alpha \beta}(r)\right)-\Gamma_{\alpha \beta}^{\mathrm{sr}}(r)-r q_{\alpha \beta}(r)-r. \quad(19)$$

### 2.2. Extension of the LMV method to Coulombic fluids

The problem now reduces to solving the following set of highly non-linear equations
$$\tilde{\Phi}_{\alpha \beta}\left(k_{j}\right)=\tilde{\Gamma}_{\alpha \beta}^{\mathrm{sr}}\left(k_{j}\right)-k^{2}\left[k \tilde{\boldsymbol{V}}^{-1}-\tilde{\boldsymbol{C}}^{\mathrm{sr}}\right]_{\alpha \beta}^{-1}\left(k_{j}\right)+\tilde{C}_{\alpha \beta}^{\mathrm{sr}}\left(k_{j}\right)+k \tilde{V}_{\alpha \beta}\left(k_{j}\right)=0, \quad(20)$$
coupled with the closure
$$C_{\alpha \beta}^{\mathrm{sr}}\left(r_{i}\right)=F\left[\Gamma_{\alpha \beta}\left(r_{i}\right)\right],\qquad(21)$$
where the explicit form of the functional $F[f(r)]$ depends on the closure, and for the HNC is given by (19). In the expressions above both $k$ and $r$ are discretized with $k_{j}=j \Delta k$ and $r_{i}=i \Delta r,(i, j=1,..., N)$ and, as usual, the integration grid fulfils Lado's condition [13], i.e. $\Delta r \Delta k=\pi / N$.

Following Labik *et al.* [7] the solution for this set of equations is obtained using a Newton-Raphson method for $j=1,..., M$ (with $M$ typically between 20 and 30) instead of using the whole set of discrete points, since this would imply solving a system of $N$ equations (with $N$ between 256 and 2048 depending on the system). One has thus to solve the linearized set of equations given by
$$\sum_{\gamma, \delta, l} J_{\alpha \beta, j ; \gamma \delta, l} \Delta \tilde{\Gamma}_{\delta \gamma}^{\mathrm{sr}}\left(k_{l}\right)=-\tilde{\Phi}_{\alpha \beta}\left(k_{j}\right),\qquad(22)$$
where
$$\tilde{\Gamma}_{\delta \gamma}^{\mathrm{sr}}\left(k_{l}\right)^{n+1}=\tilde{\Gamma}_{\delta \gamma}^{\mathrm{sr}}\left(k_{l}\right)^{n}+\Delta \tilde{\Gamma}_{\delta \gamma}^{\mathrm{sr}}\left(k_{l}\right),\qquad(23)$$
denotes the $n+1$ Newton-Raphson estimate. The problem reduces to the inversion the Jacobian matrix; that is
$$\Delta \tilde{\boldsymbol{\Gamma}}=-\boldsymbol{J}^{-1} \tilde{\boldsymbol{\Phi}}\qquad(24)$$
represents the central part of the computation. Up to this point the procedure is identical to the one proposed by Ichiye and Haymet [8]. We, however, use a different expression for the Jacobian matrix which we think is simpler than (2.31) of [8], namely
$$J_{\alpha \beta, j ; \gamma \delta, l}=\frac{\mathrm{d} \tilde{\Phi}_{\alpha \beta}\left(k_{j}\right)}{\mathrm{d} \tilde{\Gamma}_{\gamma \delta}\left(k_{l}\right)}=\delta_{\alpha \gamma} \delta_{\beta \delta} \delta j l+\left(\delta_{\alpha \gamma} \delta_{\beta \delta}-k^{2}\left[\boldsymbol{\chi}^{-1}\right]_{\alpha \gamma}\left[\boldsymbol{\chi}^{-1}\right]_{\delta \beta}\right) \tilde{C}_{\gamma \delta, j l},\quad(25)$$
with
$$\boldsymbol{\chi}=k \tilde{\boldsymbol{V}}^{-1}-\tilde{\boldsymbol{C}}^{\mathrm{sr}},\qquad(26)$$

and

$$\tilde{C}_{\gamma \delta, j l}=\frac{1}{N}\left[D_{\gamma \delta}(|l-j|)-D_{\gamma \delta}(l+j)\right],$$

$$D_{\gamma \delta}(l)=\sum_{j}\left(\frac{\mathrm{d} C_{\gamma \delta}^{\mathrm{sr}}}{\mathrm{d} \Gamma_{\gamma \delta}^{\mathrm{sr}}}\right)_{r=r_{j}} \cos \left(\frac{\pi}{N} j l\right),
\tag{27}$$

where according to (19)

$$\left(\frac{\mathrm{d} C_{\gamma \delta}^{\mathrm{sr}}}{\mathrm{d} \Gamma_{\gamma \delta}^{\mathrm{sr}}}\right)_{r=r_{j}}=h_{\gamma \delta}^{\mathrm{sr}}\left(r_{j}\right)+q_{\gamma \delta}\left(r_{j}\right)=h_{\gamma \delta}\left(r_{j}\right).
\tag{28}$$

Equation (25) is consistent with the expression found by Wu et al. [14] in their extension of the LMV method to molecular fluids in the site-site approximation.

Once we have an initial estimate for $\boldsymbol{\Gamma}$ (the MSA yields sufficiently good initial guesses) one iterates (24) in $k$-space until convergence is achieved for $j=1, \ldots, M$. Then a direct iteration is performed on (18) for $j=M+1, \ldots, N$ inserting the initial $\tilde{\boldsymbol{C}}\left(k_{j}\right)$ computed via (19), as explained in [7] and [8], thus one gets a new estimate for $\tilde{\boldsymbol{\Gamma}}\left(k_{j}\right)$ for $j=1, \ldots, N$, which once inverted can re-enter the Newton-Raphson iterations scheme outlined above, and proceed until

$$\left(\sum_{i=1}^{N}\left(\Gamma_{\alpha \beta}^{n}\left(r_{i}\right)-\Gamma_{\alpha \beta}^{n-1}\left(r_{i}\right)\right)^{2}\right)^{1 / 2} \leqslant \eta,$$

where $\eta$ is a measure of the total accuracy of the solution. Convergence can be considerably improved by using a modification of Broyle's mixing iterates method instead of simple direct iterations (see (10), (11) in [9]).

The chore of the computation outlined above is the calculation and inversion of the Jacobian matrix $\boldsymbol{J}$ (whose dimension in $\left(n_{i} M\right) \times\left(n_{i} M\right)$ with $n_{i}$ being the number of different interactions, i.e. $n_{i}=3$ for a simple one-component electrolyte). Now, as suggested in a previous work by one of us [9], the Kinoshita-Harada strategy comes into play. Once the Jacobian matrix (or more properly its inverse, the system matrix [5,9]) is known for a given system, the Newton-Raphson iterations are performed keeping its value constant (to guarantee numerical stability it can be recomputed when convergence is achieved for the new system).

The proposed iteration strategy is considerably more stable and two or three times faster than those methods that involve recomputation of the Jacobian matrix for every Newton-Raphson loop.

### 2.3. Thermodynamics for Coulombic systems in the HNC approximation

In this section we will pay special attention to the treatment of long-range correlations when computing integrated thermodynamic quantities.

It is well known that the excess internal energy for a mixture (with respect to the uncharged system) is given by

$$\frac{\beta u^{\mathrm{ex}}}{N}=\frac{1}{2 \rho} \sum_{i, j} \rho_{i} \rho_{j} \int \beta u_{i j}^{\mathrm{coul}}(r) h_{i j}(r) \mathrm{d} \boldsymbol{r},
\tag{29}$$

where $u_{i j}^{\text {coul }}(r)=Z_{i} Z_{j} e^{2} / r \varepsilon$ and the electroneutrality condition $\left(\Sigma \rho_{i} u_{i j}^{\text {coul }}(r)=0\right)$ is

understood. For the primitive model this expression reduces to

$$\frac{\beta u^{\mathrm{ex}}}{N}=\frac{2 \pi \Gamma}{\rho}\left(\sum_{i, j} \rho_{i} \rho_{j} Z_{i} Z_{j} \int_{\sigma_{i j}}^{R_{n}} r h_{i j}(r) \mathrm{d} r-\frac{1}{2} \sum_{i, j} \rho_{i} \rho_{j} Z_{i} Z_{j} \sigma_{i j}^{2}\right)-\frac{\kappa_{\mathrm{D}}^{3}}{8 \pi} \frac{\mathrm{e}^{-\kappa_{\mathrm{D}} R_{n}}}{\rho},$$

where the use of a finite number of points in $r$-space determines the upper integration limit, $R_{n}=N \Delta r$. In the former expression we have included terms to estimate the long-range contribution at low densities.

The compressibility factor can be obtained from the virial equation, which in this case reads [16]

$$\frac{\beta P}{\rho}=1+\frac{2 \pi}{3 \rho} \sum_{i, j} \rho_{i} \rho_{j} \sigma_{i j}^{3}\left[h_{i j}\left(\sigma_{i j}\right)+1\right]+\frac{1}{3} \frac{\beta u^{\mathrm{ex}}}{N}.$$

The chemical potential is evaluated from the Kirkwood relation [15] that in the HNC approximation yields the following closed expression [16,17]

$$\beta\left(\mu_{i}-\mu_{i}^{\mathrm{id}}\right)=-\sum_{j} \rho_{j} \tilde{c}_{i j}(0)+\frac{1}{2} \sum_{j} \rho_{j} \int h_{i j}(r) \gamma_{i j}(r) \mathrm{d} r,$$

with $\mu_{i}^{\text {id }}$ the ideal gas chemical potential and $\gamma_{i j}=h_{i j}-c_{i j}$ as usual. Following Sloth and Sørensen [16] one can define $c_{i j}^{*}=c_{i j}+\beta Z_{i} Z_{j} e^{2} / r \varepsilon$ and $\gamma_{i j}^{*}=h_{i j}-c_{i j}^{*}$, and then from (32) one gets

$$\begin{aligned}
\beta\left(\mu_{i}-\mu_{i}^{\mathrm{id}}\right)= & -2 \pi \sum_{j} \rho_{j} \int_{0}^{\sigma_{i j}} c_{i j}^{*}(r) r^{2} \mathrm{~d} r+2 \pi \sum_{j} \rho_{j} \int_{\sigma_{i j}}^{R_{n}}\left[h_{i j}(r) \gamma_{i j}^{*}-2 c_{i j}^{*}\right] r^{2} \mathrm{~d} r \\
& +2 \pi \Gamma Z_{i} \sum_{j} \rho_{j} Z_{j} \int_{\sigma_{i j}}^{R_{n}} r h_{i j}(r) \mathrm{d} r+\frac{2 \pi}{3} \sum_{j} \rho_{j} \sigma_{j k}^{3}-2 \pi \Gamma Z_{i} \sum_{j} \rho_{j} \sigma_{i j}^{2} \\
& +Z_{i}^{2} \Gamma \frac{\kappa_{\mathrm{D}}}{2}\left(\frac{1}{2} \mathrm{e}^{-\kappa_{\mathrm{D}} R_{n}}-2\right) \mathrm{e}^{-\kappa_{\mathrm{D}} R_{n}} .
\end{aligned}$$

In a similar way one can determine the excess Helmholtz free energy per particle using [15]

$$\begin{aligned}
\beta\left(A-A^{\mathrm{id}}\right) / N= & \sum_{i, j} \rho_{i} \rho_{j} \int_{0}^{\infty}\left[\frac{1}{2} h_{i j}(r)^{2}-g_{i j}(r) c_{i j}(r)\right] r^{2} \mathrm{~d} r \\
& -\frac{1}{4 \pi^{2} \rho} \int\left\{\log \operatorname{det}\left[\boldsymbol{I}+\tilde{\boldsymbol{H}}(k) k^{-1}\right]-\operatorname{Tr}\left[\tilde{\boldsymbol{H}}(k) k^{-1}\right]\right\} k^{2} \mathrm{~d} k, \quad \text { (34) }
\end{aligned}$$

where $\tilde{\boldsymbol{H}}(k)$ is defined according to (17). In this equation det and $\operatorname{Tr}$ denote the determinant and trace of a matrix. From the numerical standpoint an accurate computation of the integral in $k$ space is particularly cumbersome. We have dealt with the long-range part of the function (the hard-core discontinuity implies a $k^{-2}$ decay) by approximating the log term with its second-order Taylor expansion for large $k$, namely

$$\tilde{f}_{\mathrm{lr}}(k)=-\sum_{i>j} \rho_{i} \rho_{j} \tilde{h}_{i j}(k)^{2}-\frac{1}{2} \sum_{i} \rho_{i}^{2} \tilde{h}_{i i}(k)^{2} \approx \log \operatorname{det}\left[\boldsymbol{I}+\tilde{\boldsymbol{H}}(k) k^{-1}\right]-\operatorname{Tr}\left[\tilde{\boldsymbol{H}}(k) k^{-1}\right] .$$

By using the Parsival identity
$$\frac{1}{(2 \pi)^{3}} \int \tilde{f}_{1}(k) \tilde{f}_{2}(k) \mathrm{d} k=\int f_{1}(r) f_{2}(r) \mathrm{d} r
\tag{36}$$
one can subtract the long range of the integral in $k$-space simultaneously adding the corresponding term in $r$ space, and this latter $r$ space integral can be easily handled. After some manipulation one gets
$$\begin{aligned}
\frac{\beta\left(A-A^{\mathrm{id}}\right)}{N}= & \frac{\beta u^{\mathrm{ex}}}{N}+\frac{4 \pi}{\rho} \sum_{i>j} \rho_{i} \rho_{j} \int_{\sigma_{i j}}^{R_{n}} h_{i j}(r)^{2} r^{2} \mathrm{~d} r \\
& +\frac{2 \pi}{\rho} \sum_{i} \rho_{i}^{2} \int_{\sigma_{i i}}^{R_{n}} h_{i i}(r)^{2} r^{2} \mathrm{~d} r-\frac{2 \pi}{\rho} \sum_{i, j} \rho_{i} \rho_{j} \int_{\sigma_{i j}}^{R_{n}} g_{i j}(r) c_{i j}^{*}(r) r^{2} \mathrm{~d} r \\
& +\frac{2 \pi}{3 \rho}\left(2 \sum_{i>j} \rho_{i} \rho_{j} \sigma_{i j}^{3}+\sum_{i} \rho_{i} \sigma_{i i}^{3}\right)+\left(\frac{\kappa_{\mathrm{D}}^{3}}{4 \pi \rho}+\frac{\pi \Gamma^{2}}{\kappa_{\mathrm{D}} \rho} \sum_{i} \rho_{i} Z_{i}^{4}\right) \mathrm{e}^{-2 \kappa_{\mathrm{D}} R_{n}} \\
& -\frac{1}{4 \pi^{2} \rho} \int_{0}^{k_{n}}\left\{\log \det \left[\boldsymbol{I}+\tilde{\boldsymbol{H}}(k) k^{-1}\right]-\operatorname{Tr}\left[\tilde{\boldsymbol{H}}(k) k^{-1}-\tilde{f}_{\mathrm{lr}}(k)\right]\right\} k^{2} \mathrm{~d} k.
\end{aligned}
\tag{37}$$

Notice that the pressure can now be computed from the excess Helmholtz free energy per particle and the chemical potential as
$$\frac{\beta P}{\rho}=1+\frac{1}{\rho} \sum_{i} \rho_{i} \beta\left(\mu_{i}-\mu_{i}^{\mathrm{id}}\right)-\frac{\beta\left(A-A^{\mathrm{id}}\right)}{N}.
\tag{38}$$

Both routes for the computation of $\beta P / \rho$ ((31) and (38)) are identical in the HNC approximation [18]. We have used this identity as a powerful check of the numerical consistency of our results. It is also to be mentioned that (38) (free energy route) is numerically more reliable at high density, whereas at low density the virial equation (31) turns out to be more appropriate.

Finally let us recall that the reduced inverse isothermal compressibility $\chi_{0} / \chi$, for Coulombic fluids [20] is given by
$$\chi_{0} / \chi=\left(\frac{\partial \beta P}{\partial \rho}\right)_{T}=\frac{1}{\rho} \sum_{i, j} \rho_{i} \rho_{j} \tilde{c}_{i j}^{\mathrm{sr}}(0).
\tag{39}$$

In this expression $\chi_{0}$ denotes the ideal gas isothermal compressibility (i.e., $\chi_{0}=\beta / \rho$).

We have seen that thermodynamic quantities can be obtained from the correlation functions in a closed form. This is an interesting feature of the HNC approximation which is shared by approximations like the MSA or LHA (linearized hypervertex approximation) [19] but absent in the Percus-Yevick or reference hypernetted chain relations [15].

### 3. Quantitative results

In order to make things easier we have only considered the 1:1 restricted primitive model which consists of a mixture of equal sized charged hard spheres. The fact that the HNC equation appears not to converge at low densities and high ionic strength has been known for a long time [21], but as mentioned in the Introduction the nature of this divergence has remained somewhat obscure, especially in terms of its precise

![](./images/812088170614095874_2.jpg)

Figure 1. No-solution region for the HNC equation (delimited by the dashed line) together with estimates of the high and low density coexistence curves [2]. The filled circle represents the 'best estimate' of the critical point, according to [1]. Very recent simula- tions by Valleau [28] and Panagiotopoulos [29] place the RPM critical point quite close to the point $(\rho_{c} \approx 0.04, \Gamma \approx 14)$ at which the high and low density coexistence branches meet when smoothly extrapolated.

connection with low-density phase coexistence. We have performed an extensive series of computations along isochores and isotherms and thus obtained a clearly defined locus of no solution for the equation. This can be seen in figure 1 where we have plotted the estimates of low-density and high-density coexistence curves taken from [2] together with the no-solution locus obtained by us. As a matter of fact, our results are fully consistent with those presented by Hafskjold and Stell in figure 5.11 of [21]. For each system integration parameters were adjusted in order to give optimal numerical performance, thus we have used 1024 grid points (up to 2048 at the lowest densities) and the integration grid was set to $\Delta r=0.02$ (in ionic diameter units). At higher densities a smaller grid size is advisable. Our method, nonetheless, has proven to be able to yield results within a $5 \%$ accuracy (with the largest deviations at very low and rather high densities) utilizing only 256 points and $\Delta r=0.025$, for densities ranging from dilute electrolytes to molten salts. Obviously using this set of parameters computer time reduces considerably.

In addition to the convergency properties of the solution, we can get first-hand information from the thermodynamics of the HNC just by examining the behaviourof the thermodynamic potentials. Adding the ideal gas contributions to (33) and (37) we have
$$\begin{aligned}
\beta \mu_{i}(\rho, T) & =\log \rho_{i}+\beta\left(\mu-\mu^{\mathrm{id}}\right), \\
\frac{\beta A}{N} & =\frac{\beta\left(A-A^{\mathrm{id}}\right)}{N}+\frac{1}{\rho} \sum_{i} \rho_{i} \log \rho_{i}-1,
\end{aligned}\tag{40}$$

![](./images/812088170614095874_3.jpg)

Figure 2. Chemical potential along several isotherms. Labels denote different values of $\Gamma$, as follows: (A, 2·0; B, 5·0; C, 7·0; D, 8·0; E, 10·0; F, 12·0; G, 14·0).

plus terms of no importance in an isothermal construction. We have plotted these two thermodynamic potentials in figures 2 and 3, respectively. A rapid overview rules out the possibility of any coexistence curve outside the region of no solution (in contrast with the situation for other fluid systems like the monoatomic Lennard-Jones fluid in the RHNC approximation [9]).

Following Kinoshita and Harada [5] we can try to analyse the cause of divergence by taking a look at the OZ relation we are actually solving (18). We then observe that the quantity

$$\Delta(k)=\operatorname{det}\left[k \tilde{V}^{-1}(k)-\tilde{C}^{\mathrm{sr}}(k)\right] \tag{41}$$

which explicitly appears in (20) is essentially the inverse isothermal compressibility at $k=0$ and must be non-zero to avoid divergence. Only if this quantity vanishes at $k=0$ does it imply a divergence in the compressibility whereas we can only monitor it with precision at $k=k_{i} \neq 0$, e.g. at $k_{1}$. (This is the major source of uncertainty in our approach.) In figure 4 we have plotted the quantity $\Delta_{1}\left(=\Delta\left(k_{1}\right)\right)$ and the absolute value of its first and second derivatives (solid and dashed lines respectively) with respect to the inverse temperature $\Gamma$ at constant density $(\rho=0.05)$. We see that when approaching the limiting value of $\Gamma$ the quantity $\Delta_{1}$ falls down rapidly, but it remains finite. Numerical instabilities show up since $\Delta_{1}$ decreases approaching a vertical slope. The behaviour of the first and second derivatives whose absolute values are plotted in the upper part of the figure confirm the previous conclusion. All this might well mean that we are close to a point where two solutions meet; so for larger values of $\Gamma$ complex values of $\Delta_{1}$ might be expected. As in the case reported by Kinoshita and Harada [5] this we conclude cannot be attributed to a failure in the numerical procedure; the problem stems from the HNC equation itself.

![](./images/812088170614095874_4.jpg)

Figure 3. Helmholtz free energy along several isotherms. Curves are labelled as in figure 2.

On the other hand Abernethy and Gillan [3] reported a divergence in the iso- thermal compressibility (computed via the compressibility theorem) at higher den- sities at what appeared to be a true spinodal line. In order to analyse this in more detail we have plotted in figure 5 the evolution of the inverse isothermal compressibil- ity (evaluated using (39)) along several isotherms. One readily appreciates that at low density the inverse isothermal compressibility remains finite and non-zero at the boundary of the no-solution region. As the density increases there is a pronounced decay in its value (and the slope of the curves approaches $90^{\circ}$ ) close to the boundary. So far, it remains unclear whether at high density one has a true spinodal line at the boundary or the inverse compressibility remains small but finite, as was suggested by Kinoshita and Harada [5]. Therefore, in figure 6 we have plotted $\chi_{0} / \chi$ along two isochores against the difference $\Gamma_{1}(\rho)-\Gamma$ (where $\Gamma_{1}$ represents the limiting $\Gamma$ value one can reach by numerical solution along a constant density curve). We have also represented the first derivative with respect to $\Gamma$ to examine more closely the behaviour when the system approaches the divergence. The use of logarithmic scale magnifies the differences observed between the two isochores. This figure confirms the conclusions drawn from figure 5, in the sense that on the high-density side of the coexistence there is a clear evidence of a spinodal line (the inverse compressibility falls down rapidly to zero values) whereas, at low densities on the contrary it reaches a low but finite value at the boundary. The overall trend is clear, as density increases the limiting HNC solution approaches the spinodal line.

We may conclude that the HNC has a no-solution region whose origin is double: At low densities there is a divergence intrinsic to the HNC equation but not related to divergence in the correlation functions (i.e. the values of $\chi_{0} / \chi$ remain non-zero at the boundary), and additionally there is the spinodal line at higher densities. There

![](./images/812088170614095874_5.jpg)

Figure 4. Evolution of $\Delta_1$ (see (41) in the text) when approaching the divergence limit along the isochore $\rho = 0.05$. The upper part of the figure shows the behaviour of the first and second derivatives (absolute values) in solid and dashed line respectively.

appears to be a 'crossover' region in which it is hard to determine numerically which of the two causes is responsible for the divergence.

Although this behaviour may appear to be rather singular, Baxter reported a similar situation in the Percus-Yevick (PY) solution for sticky hard spheres [22] more than twenty years ago. An illuminating discussion on this problem can be found in the work by Cummings and Stell [23] on the critical behaviour of the Yukawa fluid in the mean spherical approximation. Whereas in this latter case the no-solution region lies inside the boundary of the two phase region and the spinodal line (as in the case for the Lennard-Jones fluid in the RHNC [9]), for the PY sticky hard-sphere fluid one finds a crossing region between the spinodal line and the boundary where the solutions of the equation lie in the complex plane. As a consequence, on the liquid side of the coexistence curve one finds a spinodal line while at low density (gas side) there is no coexistence curve. This parallelism between the PY sticky hard-sphere fluid and the HNC electrolyte deserves a more detailed and careful theoretical investigation which will be the subject of a forthcoming paper [27].

If one identifies the point of maximum temperature (minimum $\Gamma$) in the no-solution locus in figure 1 as the HNC 'compressibility' critical point, one sees that it is at a higher temperature and very much lower concentration than the simulation estimates given in [28] and [29]. The maxima of the coexistence curves in figures 2 and 3 locate

![](./images/812088170614095874_6.jpg)

Figure 5. Inverse isothermal compressibility along several isotherms. Curves are labelled as in figure 2.

the HNC critical point obtained via the alternative 'energy/virial' route. One sees that its density $(\rho \sigma^{3} \approx 7 \times 10^{-3})$ is almost an order of magnitude lower than the simulation estimates. We did not monitor the corresponding critical temperature, but since it lies outside the no-solution region, it must correspond to a temperature greater than $kT/e^{2}\sigma \approx 0\cdot 12$ ($\Gamma \approx 8$) and hence is clearly too high. In summary, we see that the HNC equation does not provide a reliable guide to the location of the RPM critical point.

The unphysical behaviour of the hypernetted chain approximation at low densities might have its origin in the inability of this equation to adequately treat the ion clustering effects [5], which are of extreme importance at strong coupling (low temperatures or $Z_{a}:Z_{b}$ electrolytes with $Z_{a}$ and $Z_{b} \geqslant 2$). A device to overcome this difficulty might be the introduction of a bridge function in (19) (RHNC scheme [24]) which takes indirectly into account correlations mediated by two or more particles. This function must be approximated by that of a 'reference' system, which in the case of charged particles should contain information about the long range behaviour of the true bridge function, as proposed by Foiles et al. [25] for the one component plasma (OCP). Alternatively, one may follow a different approximation scheme in the direction of the linearized and exponential-hypervertex approximations [19,26] which appropriately formulated, can take into account association phenomenon [30].

### 4. Further observations

It was long ago observed by Green [31] that for simple non-ionic fluids the HNC approximation yields an inverse structure factor $S(k)^{-1}$ that must assume a somewhat

![](./images/812088170614095874_7.jpg)

Figure 6. Inverse isothermal compressibility (lower figure) when approaching the limiting value of $\Gamma$ for two isochorous lines (denoted by $\Gamma_{l}(\rho)$ corresponding to $\rho=0.01$ and $\rho=0.382$. The upper figure shows the behaviour of the first derivative.

peculiar form at the critical point in the neighbourhood of $k=0$. Namely

$$S(k)^{-1}=D_{1} k+\text { higher order terms in } k. \tag{42}$$

We have generalized Green's analysis to apply to the spinodal of the RPM. (We shall give the details in a subsequent publication [27].) We obtain, in particular

$$D_{1}=\left(1 / 2 \pi^{2 / 3}\right) \rho^{-1 / 3}, \quad \rho=\rho_{-}+\rho_{+}. \tag{43}$$

In comparing this slope to our numerical assessment of $S(k)^{-1}$ close to the spinodal at $\rho=0.5$ we find remarkable agreement (see figure 7). The $k_{j}=0$ value is obtained by integration of $c_{\alpha \beta}^{\mathrm{sr}}(r)$ and for $k_{j} \neq 0$ we have used

$$S\left(k_{j}\right)^{-1}=1-\frac{1}{\rho} \sum_{\alpha, \beta}\left(\rho_{\alpha} \rho_{\beta}\right)^{1 / 2} k_{j}^{-1} \tilde{C}_{\alpha \beta}^{\mathrm{sr}}\left(k_{j}\right).$$

As one of us has noted in an earlier publication with Hafskjold [32] we expect the exact RPM $S(k)^{-1}$ at the critical point to have the form

$$S(k)^{-1}=D_{2-\eta} k^{2-\eta}+\text { higher order terms in } k, \tag{44}$$

with $\eta$ having a very small Ising-model value $(\approx 1 / 20)$, rather than the HNC value of $\eta=1$.

It is worth noting that the above analysis must be modified if one extends it from

![](./images/812088170614095874_8.jpg)

Figure 7. Low $k$ behaviour of the inverse structure factor close to the spinodal line at $\rho=0.5$ ($\Gamma=41.957$). Filled circles represent the computed values, the solid line is the theoretical prediction and the dotted curve is a spline fitting in which the $k=0$ computed value has been replaced by the 'true' value at the spinodal line (i.e. $S(k)^{-1}=0$).

the RPM to a model with a solvent-averaged pair potential that includes a 'cavity term', $Ar^{-4}, A>0$. Such a term is to be expected in real electrolytes as a result of the presence of solvent particles bearing permanent dipole moments [33,34]. It also appears in the continuum-solvent model of charged hard spheres in a uniform structureless solvent of dielectric constant $\varepsilon$ if one assumes that the solvent does not permeate the interior of the spheres, which are assumed to be cavities with the dielectric constant of a vacuum [35,36]. In this model

$$A=\frac{(\varepsilon-1)\left(Z_{+}^{2} \sigma_{++}^{3}+Z_{-}^{2} \sigma_{--}^{3}\right) e^{2}}{16(2 \varepsilon+1)}. \tag{45}$$

The cavity term will contribute a competing term of magnitude $-\rho \beta \pi^{2} A k$ to the right-hand side of (42) and, more generally of (44). Its presence will also change the magnitude of $D_{1}$ (and, more generally of $D_{2-\eta}$). In the HNC case, further analysis reveals that this will make little difference for small $A$, but that as $A$ increases, one reaches a value of $\beta A$ for which no real solution to the HNC exists along the spinodal. (For a recent HNC study of a model with a cavity term we refer the readers to a paper by $Xu$ et al. [37]). In the more general case given by (44), when $\eta$ is smaller than 1, the cavity contribution will give rise to a 'dimple' in the profile of $S(k)^{-1}$ so that it has its minimum for some $k_{0} \neq 0$, and $S(k)^{-1}=0$ can only be satisfied for $k \neq 0$, thus the formation of a spinodal curve and critical point will be suppressed and density waves with non-zero wave number would appear when $S(k)^{-1}=0$ instead. We shall discuss these effects in more detail in [27].

E. L. wishes to thank the Royal Norwegian Council for Scientific and Industrial Research (NTNF) which supported his postdoctoral stay in Trondheim. This work has been partially financed by the Dirección General de Investigación Científica y Técnica under Project SEUI no. PB87-0246-C02-01. G. S. gratefully acknowledges

the support of the Division of Chemical Sciences, Office of Basic Energy Sciences, Office of Energy Research, US Department of Energy. He is also indebted to Dr Fernando Rainieri for many stimulating discussions concerning this work and to all three authors of [37] for sharing with him preliminary versions of that manuscript which concerns an HNC treatment of phase separation.

## References
[1] STELL, G., WU, K. C., and LARSEN, B., 1976, *Phys. Rev. Lett.*, **37**, 1369.
[2] GILLAN, M. J., 1983, *Molec. Phys.*, **49**, 421.
[3] ABERNETHY, G. M., and GILLAN, M. J., 1980, *Molec. Phys.*, **39**, 839.
[4] BELLONI, L., 1986, *Phys. Rev. Lett.*, **57**, 2026.
[5] KINOSHITA, M., and HARADA, M., 1988, *Molec. Phys.*, **65**, 599; 1990, *Molec. Phys.*, **70**, 1121.
[6] GILLAN, M. J., 1979, *Molec. Phys.*, **38**, 1781.
[7] LABIK, S., MALIJEVSKY, A., and VONKA, P., 1985, *Molec. Phys.*, **56**, 709.
[8] ICHIYE, T., and HAYMET, D. J., 1988, *J. chem. Phys.*, **89**, 4315.
[9] LOMBA, E., 1989, *Molec. Phys.*, **68**, 87.
[10] ROSSKY, P. J., and FRIEDMAN, H. L., 1980, *J. chem. Phys.*, **72**, 5694.
[11] LOMBA, E., and HØYE, J. S., *Comput. Phys. Commun.*, (in press).
[12] SPRINGER, J. F., POKRANT, M. A., and STEVENS, F. A., 1973, *J. chem. Phys.*, **58**, 4863.
[13] LADO, F., 1967, *J. chem. Phys.*, **47**, 4828.
[14] WU, R. S., LEE, L. L., and HARWELL, J. H., 1989, *J. chem. Phys.*, **91**, 4254.
[15] KYSELYOV, O. E., and MARTYNOV, G. A., 1990, *J. chem. Phys.*, **93**, 1942.
[16] SLOTH, P., and SØRENSEN, T. S., 1990, *J. phys. Chem.*, **94**, 2116.
[17] HANSEN, J. P., TORRIE, G. M., and VIEILLEFOSSE, P., 1977, *Phys. Rev. A*, **16**, 2153.
[18] GRAY, C. G., and GUBBINS, K. E., 1984, *Theory of molecular fluids*, (Clarendon).
[19] HØYE, J. S., and STELL, G., 1982, *J. chem. Phys.*, **78**, 1290.
[20] HANSEN, J. P., and MCDONALD, I. R., 1986, *Theory of simple Liquids*, 2nd edn (Academic).
[21] HAFSKJOLD, B., and STELL, G., 1982, *The Liquid State of Matter*, edited by E. W. Montroll and J. L. Lebowitz (North-Holland).
[22] BAXTER, R. J., 1968, *J. chem. Phys.*, **49**, 2770.
[23] CUMMINGS, P. T., and STELL, G., 1983, *J. chem. Phys.*, **78**, 1917 and references therein.
[24] LADO, F., FOILES, S. M., and ASHCROFT, N. W., 1983, *Phys. Rev. A*, **28**, 2374; CACCAMO, C., MALESCIO, G., and REATTO, L., 1984, *J. chem. Phys.*, **81**, 4093 (1984).
[25] FOILES, S. M., ASHCROFT, N. W., and REATTO, L., 1984, *J. chem. Phys.*, **80**, 4441.
[26] HØYE, J. S., and LOMBA, E., 1991, *J. chem. Phys.*, **95**, 4502.
[27] HØYE, J. S., LOMBA, E., and STELL, G., (to be published).
[28] VALLEAU, J. P., 1991, *J. chem. Phys.*, **95**, 584.
[29] PANAGIOTOPOULOS, A. Z., 1991, *Fluid Phase Equil.* (in press).
[30] HØYE, J. S., and STELL, G., (unpublished).
[31] GREEN, M. S., 1960, *J. chem. Phys.*, **33**, 1403.
[32] HAFSKJOLD, B., and STELL, G., 1982, *The Liquid State of Matter*, edited by E. W. Montroll and J. L. Lebowitz (North-Holland) p. 256.
[33] JEPSEN, D. W., and FRIEDMAN, H. L., 1963, *J. chem. Phys.*, **38**, 846.
[34] RAMANATHAN, P. S., and FRIEDMAN, H. L., 1971, *J. chem. Phys.*, **54**, 1086.
[35] LEVINE, S., and BELL, G., 1966, *International Symposium on Electrolytes*, edited by B. E. Conway and R. G. Barradas (Wiley).
[36] HØYE, J. S., and STELL, G., 1978, *Faraday Discuss. Chem. Soc.*, **64**, 16 and references therein.
[37] XU, H., FRIEDMAN, H. L., and RAINIERI, F. (to be published).
