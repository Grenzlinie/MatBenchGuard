
# Short-distance thermal correlations in the massive XXZ chain

Christian Trippe \( ^{*} \) , Frank Göhmann \( ^{\dagger} \) , Andreas Klümper \( ^{\ddagger} \) 

Fachbereich C – Physik, Bergische Universität Wuppertal, 42097 Wuppertal, Germany

December 4, 2018

## Abstract

We explore short-distance static correlation functions in the infinite XXZ chain using previously derived formulae which represent the correlation functions in factorized form. We compute two-point functions ranging over 2, 3 and 4 lattice sites as functions of the temperature and the magnetic field in the massive regime  \( \Delta > 1 \) , extending our previous results to the full parameter plane of the antiferromagnetic chain  \( (\Delta > -1 \)  and arbitrary field h). The factorized formulae are numerically efficient and allow for taking the isotropic limit  \( (\Delta = 1) \)  and the Ising limit  \( (\Delta=\infty) \) . At the critical field separating the fully polarized phase from the Néel phase, the Ising chain possesses exponentially many ground states. The residual entropy is lifted by quantum fluctuations for large but finite  \( \Delta \)  inducing unexpected crossover phenomena in the correlations.

## 1 Introduction

All observable information about a many-body quantum system is encoded in its correlation functions. For interacting systems in the thermodynamic limit this information is, in general, only accessible through various approximations. \( ^{1} \)  Until rather recently very few examples were known, where correlation functions could be calculated exactly. Among the known examples there was none with short-range interactions of finite and tunable strength. In particular, for the large and prototypical class of integrable models that are solvable by Bethe ansatz, the solution was limited to the spectral properties, but except for what can be concluded from the finite size corrections to the spectrum rather little was known about their correlation functions.
 

This situation is about to change. Extensive studies by several groups, mainly focusing on the XXZ quantum spin chain, have eventually uncovered a structure which we believe to be typical for the Bethe ansatz solvable models: the one-point and the neighbour correlation functions determine everything. We call this phenomenon factorization. Based on the factorization we can calculate for the first time short-range correlation functions with arbitrary accuracy, both, for finite temperatures in the thermodynamic limit  \( [3] \) , and for arbitrary finite length in the ground state  \( [11] \) . This has applications e.g. in the determination of ESR-line shifts  \( [28] \)  and is useful for estimating the errors associated with standard numerical techniques like the quantum Monte Carlo algorithm  \( [27] \) .

Factorization appeared first  \( [9] \)  as the explicit factorization of certain multiple integrals  \( [19,20,24] \)  describing the density matrix elements of the isotropic Heisenberg chain in the ground state with no magnetic field applied. A similar factorization for the ground state correlation functions of the XXZ chain in the massive regime, i.e. for the model considered in this article, was carried out in  \( [30,22] \) . After a multiple integral representation for finite temperature correlation functions had become available  \( [14,15] \) , the factorization of the integrals for short distances was extended to this case  \( [5] \) . Following the success with the direct factorization of the integrals a deep exploration into the algebraic structure of the static correlation functions of the XXZ chain was conducted by Boos, Jimbo, Miwa, Smirnov and Takeyama, culminating in the works  \( [8,7,21,4] \) , where the factorization of all static correlation functions of the XXZ chain was proved in a very general setting, including the finite temperature and finite magnetic field cases.

In all the recent works cited above it was crucial not to deal directly with the spin chain Hamiltonian, but with the associated six-vertex model  \( [2] \) . The six vertex model naturally carries inhomogeneity parameters in horizontal and vertical directions and can be distorted by a disorder field without losing its distinctive feature, the integrability. In this setting the density matrix of a finite segment of the XXZ chain is naturally generalized to include the inhomogeneity parameters and the strength  \( \alpha \)  of the disorder field. The vertical inhomogeneity parameters  \( \nu_{j} \)  and the disorder field regularize the expression for the density matrix. The horizontal spectral parameters allow one to introduce the temperature into the model  \( [14, 25, 26] \)  and to adjust the Hamiltonian  \( [31] \) . The density matrix of the inhomogeneous six-vertex model with disorder field depends polynomially on only two complex functions  \( \varphi(\nu|\alpha) \)  and  \( \omega(\nu_{1},\nu_{2}|\alpha) \)  which are efficiently described in terms of the solutions of integral equations  \( [4] \) . The calculation of the coefficients of the polynomials is a purely algebraic problem. It is related to the construction of a special fermionic basis  \( [8, 7] \)  on the space of local operators acting on the space of states of the spin chain. We call this the algebraic part of the problem and the calculation of the functions  \( \varphi \)  and  \( \omega \)  the physical part of the problem, since all dependence on the physical parameters, like temperature magnetic field or boundary conditions, is in these two functions.

For the time being no efficient algorithm for the algebraic part of the problem is known. This limits the range of the correlation functions we are actually able to calculate to a few lattice sites. In  \( [3] \)  we calculated the coefficients for the two-point functions for up to
 

four lattice site by brute force computer algebra. Then we solved the physical part of the problem in the massless regime. At a late stage of the calculation the homogeneous limit and the limit of vanishing disorder field had to be taken in order to obtain the correlation functions of the spin chain. Due to the singular nature of this limit the first derivative of  \( \omega \)  with respect to  \( \alpha \)  and various derivatives with respect to the inhomogeneity parameters appear. The final expressions are polynomials in three functions  \( \omega \) ,  \( \omega' \)  (basically the  \( \alpha \)  derivative of  \( \omega \) ) and  \( \varphi \)  and their derivatives. The coefficients in these polynomials are rational functions in the deformation parameter q, which determines the anisotropy of the XXZ chain, and are algebraic and universal. Therefore the expressions derived in [3] for the two-point functions in the massless regime also apply in the massive regime, if one replaces the physical part,  \( \omega \) ,  \( \omega' \)  and  \( \varphi \)  appropriately.

This is the main subject of this work. We reformulate the expressions for the functions  \( \omega \) ,  \( \omega' \)  and  \( \varphi \)  originally obtained in [6] in a way that is convenient for numerical calculations in the massive regime  \( \Delta > 1 \)  of the XXZ chain. Combining this with the general formulae and the numerical results from [3] we obtain accurate data for the two-point functions in the full parameter plane of the infinite antiferromagnetic chain (anisotropy  \( \Delta > -1 \)  and magnetic field h arbitrary). They exhibit a surprisingly rich non-monotonic behaviour.

We should comment on the level of mathematical rigour of our results. In  \( [6,3] \)  we conjectured the physical part of the problem as well as the contribution to the algebraic part connected with the one-point functions in the limit, when  \( \alpha\to0 \) . Meanwhile we know  \( [21,4] \)  the exact physical part even for finite  \( \alpha \)  and we could show  \( [4] \)  that it reproduces our conjecture for  \( \alpha\to0 \) . The algebraic part for distances up to four lattice sites was checked in  \( [3] \)  by several independent means (comparison with the high temperature expansion of the multiple integrals  \( [15] \) , direct numerical computation, consideration of various limits). Now, as we may infer from  \( [8,21,4] \) , it is clear that the exponential formula of  \( [3] \)  is valid for arbitrary distances and zero magnetic field and at least for the distance of two lattice sites at finite magnetic field. On the other hand, the work  \( [21] \)  offers a future way for the rigorous calculation of the algebraic part which needs no exponential form of the density matrix and will hopefully lead to the calculation of static correlation functions for points at larger distances.

## 2 Hamiltonian and density matrix

We consider the Hamiltonian

 \[ \mathcal{H}_{N}=J\sum_{j=-N+1}^{N}\left(\sigma_{j-1}^{x}\sigma_{j}^{x}+\sigma_{j-1}^{\prime}\sigma_{j}^{y}+\Delta(\sigma_{j-1}^{z}\sigma_{j}^{z}-1)\right) \quad (1) \] 

of the XXZ chain in the massive antiferromagnetic regime  \( (J > 0 \)  and  \( \Delta > 1) \) . The  \( \sigma_{j}^{\alpha}, j = -N + 1, \ldots, N \) , act locally as Pauli matrices,  \( \Delta = \operatorname{ch}(\eta) \)  is the anisotropy parameter and J the exchange coupling.
 

The XXZ Hamiltonian preserves the z-component of the total spin

 \[ \mathcal{S}_{N}^{z}=\frac{1}{2}\sum_{j=-N+1}^{N}\sigma_{j}^{z}. \quad (2) \] 

Thus, the magnetization in z-direction is a thermodynamic quantity, and the thermal equilibrium of the finite system is characterized by the statistical operator

 \[ \rho_{N}(T,h)=\frac{e^{-(\mathcal{H}_{N}-h\mathcal{S}_{N})/T}}{\mathrm{t r}_{-N+1,\ldots,N}e^{-(\mathcal{H}_{N}-h\mathcal{S}_{N})/T}} \quad (3) \] 

depending on the temperature T and the external magnetic field h.

In the thermodynamic limit  \( L = 2N \rightarrow \infty \)  the system severely simplifies, since, from the six-vertex model point of view, a single eigenstate of the so-called quantum transfer matrix determines the state of thermodynamic equilibrium and hence all static correlation functions [14]. Clearly the naive limit  \( N \rightarrow \infty \)  makes no sense in (3). To perform this limit in a sensible way we fix integers m, n with m < n and introduce the density matrix

 \[ D_{[m,n]}(T,h)=\lim_{N\to\infty}\mathrm{tr}_{-N+1,\ldots,m-1,n+1,n+2,\ldots,N}\rho_{N}(T,h) \quad (4) \] 

of the segment  \( [m,n] \)  of the infinite chain which is well defined. It has the reduction properties

 \[ \mathrm{tr}_{m}D_{[m,n]}(T,h)=D_{[m+1,n]}(T,h),\quad\mathrm{tr}_{n}D_{[m,n]}(T,h)=D_{[m,n-1]}(T,h). \quad (5) \] 

We consider the vector space W of operators on the infinite chain which act non-trivially only on a finite number of lattice sites  \( (\sigma_{j}^{z}\sigma_{k}^{z} \)  for arbitrary fixed j and k is an example of such an operator). On this space we define a map  \( \mathbf{trf}_{[m,n]} : \mathcal{W} \to (\mathbb{C}^{2})^{\otimes(n-m+1)} \)  by

 \[ \mathbf{t r f}_{[m,n]}\mathcal{O}=\cdots\frac{1}{2}\mathrm{t r}_{m-2}\frac{1}{2}\mathbf{t r}_{m-1}\frac{1}{{2}}\mathbf{t r}_{n+1}\frac{1]{2}\mathbf{t r}_{n{+}2}\cdots\mathcal{O}. \quad (6) \] 

It restricts the action of O to the interval  \( [m, n] \) .

Because of (5) the definition  \( Z : W \to C \) ,

 \[ Z(\mathcal{O})=\lim_{\substack{m\rightarrow-\infty\\ n\rightarrow\infty}}\mathrm{tr}_{m,\ldots,n}D_{[m,n]}(T,h)\mathbf{trf}_{[m,n]}\mathcal{O} \quad (7) \] 

makes sense and determines the thermal expectation value of O. The functional Z has the natural interpretation of the statistical operator on the space W and may be thought of as the thermodynamic limit of  \( \rho_{N} \) , equation (3).

The functional Z allows for a generalization within the framework of the six-vertex model with disorder field. In the seminal paper  \( [21] \)  this generalization was denoted  \( Z^{\kappa} \)  (with  \( \kappa \)  referring to the magnetic field in certain units). It is this functional which depends
 

on only two functions  \( \varphi(\nu|\alpha) \)  and  \( \omega(\nu_{1},\nu_{2}|\alpha) \)  and which clearly separates the physical and the algebraic part of the problem. For details we refer the reader to [21,4].

In this work we are dealing with applications. We shall only need an understanding of the general idea of factorization and the concrete formula obtained in  \( [3] \) . For this reason we refrain in the following from any sophisticated mathematical notation and simply write  \( \langle\mathfrak{O}\rangle_{h,T}=Z(\mathfrak{O}) \)  for thermal expectation values on the infinite chain.

## 3 The physical part of the construction

As explained in  \( [3] \)  the limit  \( \alpha\to0 \)  leads to three functions  \( \omega(\mu_{1},\mu_{2}) \) ,  \( \omega'(\mu_{1},\mu_{2}) \)  and  \( \varphi(\mu) \)  that determine the correlation functions of the XXZ chain. A relatively simple description of these functions in terms of an auxiliary function a and a generalized magnetization density G was given in  \( [6] \) . We call it the a-formulation. The a-formulation is useful for deriving multiple integral formulae  \( [14] \)  and for studying the high-temperature expansion of the free energy and the correlation functions  \( [32] \) . It allows for a rather uniform description of the massless and the massive XXZ chain, the only difference between the two cases being a different choice for the so-called canonical integration contour in the complex plane  \( [14] \) .

For numerical calculations of thermodynamic properties  \( [25,26] \)  or short-distance correlators from the multiple integral  \( [10,3] \)  one has to change to a different formulation we refer to as the bô-formulation. It needs pairs of functions, but the defining integral equations involve only straight contours. It is here where one has to distinguish between the massless and the massive case, when it comes to numerical calculations. Two separate computer programs are needed. In  \( [3] \)  we studied the massless case. Here we proceed to the massive case. We start from the a-formulation of the physical part proposed in  \( [6] \)  and switch to the bô-formulation. This is a standard procedure which (in the massive case) basically requires the application of Fourier series and the convolution theorem. As far as the integral equations are concerned the reader may e.g. refer to  \( [10] \) . Then it is rather obvious how to proceed in a similar way with the expressions for the functions  \( \varphi \) ,  \( \omega \)  and  \( \omega' \)  (equations  \( (15) \) ,  \( (17) \)  and  \( (20) \)  for  \( \alpha = 0 \)  in  \( [6] \) ). For this reason we just state the results.

Let us define a pair of auxiliary functions b, b as the solution of the non-linear integral equations (NLIE)

 \[ \ln\mathfrak{b}(x)=-\frac{h}{2T}-\frac{2J\sinh(\eta)}{T}d(x)+\kappa*\ln\left(1+\mathfrak{b}\right)(x)-\kappa^{-}*\ln\left(1+\bar{\mathfrak{b}}\right)(x), \quad (8a) \] 

 \[ \ln\bar{\mathfrak{b}}(x)=\frac{h}{2T}-\frac{2J\sinh(\eta)}{T}d(x)+\kappa*\ln\left(1+\bar{\mathfrak{b}}\right)(x)-\kappa^{+}*\ln\left(1+\mathfrak{b}\right)(x) \quad (8b) \] 

with  \(  f * g(x) = \frac{1}{\pi} \int_{-\pi/2}^{\pi/2} \mathrm{d}y f(x - y) g(y)  \)  denoting a convolution.

The integral equations are specified by the integration kernels  \( \kappa \) ,  \( \kappa^{\pm} \)  and the driving terms, which contain a single transcendental function d. Note that the physical parameters
 

temperature T, coupling J and magnetic field h enter into the calculation of the correlation functions only through the driving terms of the NLIE (8).

The functions d and  \( \kappa \) ,  \( \kappa^{\pm} \) , as well as some other functions occurring in other integral equations below, have simple Fourier series representations which arise naturally in the derivation of the non-linear equations and which are also useful for solving them numerically.

 \[ d(x)=\sum_{k=-\infty}^{\infty}\frac{e^{i2k x}}{\mathrm{c h}(\eta k)}, \quad (9a) \] 

 \[ \kappa(x)=\sum_{k=-\infty}^{\infty}\frac{e^{-\eta|k|+2i k x}}{2\mathrm{c h}(\eta k)},\quad\kappa^{\pm}(x)=\kappa(x\pm i\eta^{\mp}). \quad (9b) \] 

Alternatively the kernel and the function d can be realized in terms of special functions. For the function d we find

 \[ d(x)=\frac{2K}{\pi}\mathrm{d n}\left(\frac{2K x}{\pi},i\frac{\eta}{\pi}\right), \quad (10) \] 

where  \( \mathrm{dn}(x,\tau) \)  is one of the Jacobi elliptic functions [1], and K is the complete elliptic integral of the first kind.

The integration kernel  \( \kappa \)  can be expressed in terms of the normalized trigonometric gamma function T introduced in [29]. In order to define it we first of all recall the definition of the q-gamma function [13],

 \[ \Gamma_{q}(z)=(1-q)^{1-z}\prod_{n=1}^{\infty}\frac{1-q^{n}}{1-q^{z+n+1}}. \quad (11) \] 

Then, for  \( q = \exp(-4\eta) \) ,

 \[ T(r;z)=\frac{\Gamma_{q}(1/2)}{\Gamma_{q}(iz+1/2)}\exp\left(-\frac{1}{2}\ln\pi+\frac{rz^{2}}{2}-iz\ln\left(\frac{1-e^{-2r}}{2r}\right)\right) \quad (12) \] 

and

 \[ \kappa(x)=\frac{1}{2i}\partial_{x}\ln\left[\frac{T\big(2\eta;\frac{x}{2\eta}\big)T\big(2\eta;-{\frac{x}{2\eta}}-{\frac{i}{2}}\big)}{T\big(2\eta;-{\frac{x}{2\eta}}\big)T\big(2\eta;{\frac{x}{2\gamma}}-{\frac{i}{2}}\big)}\right]. \quad (13) \] 

In addition to the auxiliary functions b and  \( \bar{b} \)  we need two more pairs of functions  \( g_{\mu}^{\pm} \)  and  \( g_{\mu^{\prime}}^{\prime\pm} \)  to express  \( \omega \) ,  \( \omega^{\prime} \)  and  \( \varphi \)  by means of auxiliary functions. Both are solutions of linear integral equations involving b and  \( \bar{b} \) ,

 \[ g_{\mu}^{+}(x)=-d(x-\mu)+\kappa*\frac{g_{\mu}^{+}}{1+\mathfrak{b}^{-1}}(x)-\kappa^{-}*\frac{g_{\mu}^{-}}{1+\mathfrak{b}^{-1}}(x), \quad (14a) \] 

 \[ g_{\mu}^{-}(x)=-d(x-\mu)+\kappa*\frac{g_{\mu}^{-}}{1+\mathfrak{b}^{-1}}(x)-\kappa^{+}*\frac{g_{\mu}^{+}}{1+\mathfrak{b}^{-1}}(x) \quad (14b) \]
 

and

 \[ \begin{align*}g_{\mu}^{\prime+}(x)=&-\eta c_{+}(x-\mu)+\eta l*\frac{g_{\mu}^{+}}{1+\mathfrak{b}^{-1}}(x)-\eta l^{-}*\frac{g_{\mu}^{-}}{1+\mathfrak{b}^{-1}}(x)\\&+\kappa*\frac{g_{\mu}^{\prime+}}{1+\mathfrak{b}^{-1}}(x)-\kappa^{-}*\frac{g_{\mu}^{\prime-}}{1+\mathfrak{b}^{-1}}(x),\end{align*} \quad (15a) \] 

 \[ \begin{align*}g_{\mu}^{\prime-}(x)=&-\eta c_{-}(x-\mu)+\eta l*\frac{g_{\mu}^{-}}{1+\mathfrak{b}^{-1}}(x)-\eta l^{+}*\frac{g_{\mu}^{+}}{1+\mathfrak{b}^{-1}}(x)\\&+\kappa*\frac{g_{\mu}^{\prime-}}{1+\mathfrak{b}^{-1}}(x)-\kappa^{+}*\frac{g_{\mu}^{\prime+}}{1+\mathfrak{b}^{-1}}(x).\end{align*} \quad (15b) \] 

The new integration kernel l and the new functions  \( c^{\pm} \)  occurring in (15) are conveniently described as Fourier series,

 \[ l(x)=\sum_{k=-\infty}^{\infty}\frac{\mathrm{s i g n}(k)e^{i2k x}}{4\mathrm{c h}^{2}(\eta k)},\quad l^{\pm}(x)=l(x\pm i\eta^{\mp}), \quad (16) \] 

where we used the standard convention  \( \mathrm{sign}(0)=0 \) , and

 \[ c_{\pm}(x)=\pm\sum_{k=-\infty}^{\infty}\frac{e^{\pm\eta k+2i k x}}{2\mathrm{c h}^{2}(\eta k)}. \quad (17) \] 

The functions  \( \omega(\mu_{1},\mu_{2}) \) ,  \( \omega'(\mu_{1},\mu_{2}) \)  and  \( \varphi(\mu) \)  which determine the inhomogeneous correlation functions can be expressed as integrals over the above functions. The function

 \[ \varphi(\mu)=\int\limits_{-\pi/2}^{\pi/2}\frac{\mathrm{d}x}{2\pi}\left(\frac{g_{\mu}^{-}(x)}{1+\mathfrak{b}(x)^{-1}}-\frac{g_{\mu}^{+}(x)}{1+\mathfrak{b}(x)^{-1}}\right) \quad (18) \] 

with \( ^{2} \)   \( \tilde{\mu} = -i\mu \)  is related to the magnetization

 \[ m(h,T)=\frac{1}{2}\left\langle\sigma_{j}^{z}\right\rangle_{T,h}=-\frac{1}{2}\varphi(0) \quad (19) \] 

which is the only independent one-point function of the XXZ chain. The function

 \[ \omega(\mu_{1},\mu_{2})=-4\kappa(\tilde{\mu}_{2}-\tilde{\mu}_{1})+\tilde{K}_{\eta}(\tilde{\mu}_{2}-\tilde{\mu}_{1})-d*\left(\frac{g_{\mu_{1}}^{+}}{1+\mathfrak{b}^{-1}}+\frac{g_{\mu_{1}}^{-}}{1+\mathfrak{b}^{-1}}\right)(\tilde{\mu}_{2}) \quad (20) \] 

with

 \[ \tilde{K}_{\eta}(x)=\frac{\mathrm{sh}(2\eta)}{2\sin(x+i\eta)\sin(x-i\eta)} \quad (21) \]
 

also determines the internal energy [3]. The last function which is necessary to determine the correlation functions is

 \[ \begin{align*}\omega^{\prime}(\mu_{1},\mu_{2})=-4\eta l(\tilde{\mu}_{2}-\tilde{\mu}_{1})-\eta\tilde{L}_{\eta}(\tilde{\mu}_{2}-\tilde{\mu}_{1})-d*\left(\frac{g_{\mu_{1}}^{+}}{1+\mathfrak{b}^{-1}}+\frac{g_{\mu_{1}}^{-}}{1+\mathfrak{b}^{-1}}\right)(\tilde{\mu}_{2})\\-n c_{-}*\frac{g_{\mu_{1}}^{+}}{1+\mathfrak{b}^{-1}}(\tilde{\mu}_{2})-\eta c_{+}*\frac{g_{\mu_{1}}^{-}}{1+\mathfrak{b}^{-1}}(\tilde{\mu}_{2}),\end{align*} \quad (22) \] 

where

 \[ \tilde{L}_{\eta}(x)=\frac{i\sin(2x)}{2\sin(x+i\eta)\sin(x-i\eta)}. \quad (23) \] 

The physical meaning of  \( \omega^{\prime} \)  is less intuitive. Its derivative appears in the two-point functions and is therefore related to certain neighbour correlators.

As shown in  \( [6,3] \)  it is necessary to perform the homogeneous limit for the calculation of correlation functions. This limit seems rather singular, because the coefficients coming from the algebraic part in general have poles, when two inhomogeneities coincide. Still, these poles are canceled by zeros coming from certain symmetric combinations of the functions  \( \omega(\mu_{1},\mu_{2}) \) ,  \( \omega^{\prime}(\mu_{1},\mu_{2}) \)  and  \( \varphi(\mu) \)  in the numerators. In order to perform the limit one has to apply l'Hôpital's rule. This finally leads to polynomials in the functions  \( \omega(0,0) \) ,  \( \omega^{\prime}(0,0) \) .  \( \varphi(0) \)  and in derivatives of these functions with respect to the inhomogeneity parameters evaluated at zero. We denote derivatives with respect to the first argument by subscripts x and derivatives with respect to the second argument by subscripts y and leave out zero arguments for simplicity. Then e.g.  \( \omega_{xyy}=\partial_{x}\partial_{y}^{2}\omega(x,y)|_{x,y=0} \)  etc.

For the examples in the next section the non-linear integral equations for b and  \( \bar{b} \)  as well as their linear counterparts for  \( g_{\mu}^{(\pm)} \)  and  \( g_{\mu}^{\prime(\pm)} \)  were solved iteratively in Fourier space, using the fast Fourier transformation algorithm. The derivatives of  \( g_{\mu}^{(\pm)} \)  and  \( g_{\mu}^{\prime(\pm)} \)  with respect to  \( \mu \) , needed in the computation of the respective derivatives of  \( \omega \)  and  \( \omega^{\prime} \) , satisfy linear integral equations as well, which were obtained as derivatives of the equations for  \( g_{\mu}^{(\pm)} \)  and  \( g_{\mu}^{\prime(\pm)} \) . The modifications due to the derivatives are particularly simple in Fourier space.

## 4 Examples of short distance correlators

In the sequel we shall restrict ourselves to the longitudinal and transversal two-point functions  \( \langle\sigma_{1}^{z}\sigma_{n}^{z}\rangle_{T,h},\langle\sigma_{1}^{x}\sigma_{n}^{x}\rangle_{T,h} \)  for  \( n=2,3,4.^{3} \)  The algebraic part for these correlation functions
 

was already calculated in our previous papers [6] and [3]. Here we merely cite those results. For the nearest neighbour correlation functions the following equations were obtained

 \[ \langle\sigma_{1}^{z}\sigma_{2}^{z}\rangle_{T,h}=\mathrm{c t h}(\eta)\omega+\frac{\omega_{x}^{\prime}}{\eta}, \quad (24a) \] 

 \[ \langle\sigma_{1}^{x}\sigma_{2}^{x}\rangle_{T,h}=-\frac{\omega}{2\mathrm{s h}(\eta)}-\frac{\mathrm{c h}(\eta)\omega_{x}^{\prime}}{2\eta}. \quad (24b) \] 

The expansions for next-nearest neighbours read

 \[ \langle\sigma_{1}^{z}\sigma_{3}^{z}\rangle_{T,h}=2\mathrm{c t h}(2\eta)\omega+\frac{\omega_{x}^{\prime}}{\eta}+\frac{\mathrm{t h}(\eta)(\omega_{x x}-2\omega_{x y})}{4}-\frac{\mathrm{s h}^{2}(\eta)\omega_{x x y}^{\prime}}{4\eta}, \quad (25a) \] 

 \[ \langle\sigma_{1}^{x}\sigma_{3}^{x}\rangle_{T,h}=-\frac{1}{\mathrm{s h}(2\eta)}\omega-\frac{\mathrm{c h}(2\eta)}{2\eta}\omega_{x}^{\prime}-\frac{\mathrm{c h}(2\eta)\mathrm{t h}(\eta)(\omega_{x x}-2\omega_{x y})}{8}+\frac{\mathrm{s h}^{2}(\eta)\omega_{x x y}^{\prime}}{8\eta}. \quad (25b) \] 

The length of the formulae grows rapidly with the number of lattice sites. For n = 4 it reads

 \[ \begin{aligned}\langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle_{T,h}&=\frac{1}{768q^{4}\left(-1+q^{6}\right)\left(1+q^{2}\right)\eta^{2}}\\&\left\{384q^{4}\left(1+q^{2}\right)^{2}\left(5-4q^{2}+5q^{4}\right)\eta^{2}\omega\right.\\&\left.-8\left(1+q^{4}\left(52+64q^{2}-234q^{4}+64q^{6}+52q^{8}+q^{12}\right)\right)\eta^{2}\omega_{xy}\right.\\&\left.\quad+192q^{4}\left(-1+q^{2}\right)^{2}\left(1+4q^{2}+q^{4}\right)\eta^{2}\omega_{yy}\right.\\&\left.+\left(-1+q^{2}\right)^{4}\left(1+q^{4}\right)\left(1+4q^{2}+q^{4}\right)\eta^{2}\Big[-4\omega_{xyyy}+6\omega_{xxyy}\Big]\right.\\&\left.\quad-768q^{4}\left(-1-q^{2}+q^{6}+q^{8}\right)\eta\omega_{y}^{\prime}\right.\\&\left.+16\left(-1+q^{2}\right)^{3}\left(1+6q^{2}+11q^{4}+11q^{6}+6q^{8}+q^{10}\right)\eta\omega_{xy}^{\prime}\right.\\&\left.\quad-2\left(-1+q^{2}\right)^{5}\left(1+2q^{2}+2q^{4}+q^{6}\right)\eta\omega_{xxyy}^{\prime}\right.\\&\left.+8\left(-1+q^{2}\right)^{3}\left(1+q^{2}\left(1+6q^{2}+34q^{4}+6q^{6}+q^{8}\right)\eta^{2}\Big[\omega_{y}^{2}-\omega_{xyy}\Big]\right.\right.\\&\left.+\left(-1-4q^{2}-22q^{4}-12q^{6}+12q^{10}+22q^{12}+4q^{14}+q^{16}\right)\eta^{2}\Big[-6\omega_{yy}^{2}\right.\\&\left.\left.+12\omega_{yy}\omega_{xy}+4\omega_{y}\omega_{yyy}-12\omega_{y}\omega{}_{xyy}-4\omega_{xyyy}+6\omega_{xxyy}\right]\right.\end{aligned} \]
 

 \[ \begin{aligned}&+16\left(-1+q^{2}\right)^{4}\left(1+q^{2}\ right)^{2}\left(1+q^2+q^{4}\right)\eta\left[\omega_{yyy}\omega^{^{\prime}}_{y}-\omega_{y}\omega^{^{\'}}_{yy}+\omega\omega^{^{\prime}}_{xyy}\right]\\+\left(-1+q^{4}\right)^{2}\left(1+5q^{2}+6q^{4}+5q^{6}+q^{8}\right)\eta\left[4\omega_{xyyy}\omega^{^{\prime}}_{y}-6\omega_{xxyy}\omega^{^{\'}}_{y}-2\omega_{yyy}\omega^{^{\'}}_{\ y y}\right.\\+\left.6\omega_{xyy}\omega^{^{\prime}}_{yy}+2\omega_{yy}\omega^{^{\prime}}_{\ y y y}-4\omega_{xy}\omega^{^{\prime}}_{yyy}-6\omega_{yy}\omega^{^{\prime}}_{\ xy y}+4\omega_{y}\omega^{^{\prime}}_{xyyy}-2\omega\omega^{^{\prime}}_{xxyyy}\right]\\+\left.3\left(-1+q^{4}\right)^{3}\left(1+q^{2}+q^{4}\right)\left[\omega^{^{\prime}}_{yyy}\omega^{^{\prime}}_{xyy}-\omega^{^{\prime}}_{yy}\omega^{^{\prime}}_{\ xy y}+\omega^{^{\prime}}_{y}\omega^{^{\prime}}_{xxyyy}\right]\right\}\end{aligned} \quad (26) \] 

and in the transversal case,

 \[ \begin{aligned}\langle\sigma_{1}^{x}\sigma_{4}^{x}\rangle_{T,h}=&\frac{1}{3072q^{5}\left(-1+q^{6}\right)\eta^{2}}\\&\left\{-768q^{6}\left(1+10q^{2}+q^{4}\right)\eta^{2}\omega\right.\\&\left.+16q^{2}\left(-1+q^{2}\right)^{2}\left(31+56q^{2}-30q^{4}+56q^{6}+31q^{8}\right)\eta^{2}\omega_{xy}\right.\\&\left.-96q^{2}\left(-1+q^{2}\right)^{2}\left(3+5q^{2}-4q^{4}+5q^{6}+3q^{8}\right)\eta^{2}\omega_{yy}\right.\\&\left.+q^{2}\left(-1+q^{2}\right)^{4}\left(1+4q^{2}+q^{4}\right)\eta^{2}\left[8\omega_{xyyy}-12\omega_{xxyy}\right]\right.\\&\left.+192q^{2}\left(-3-q^{2}-q^{4}+q^{8}+q^{10}+3q^{12}\right)\eta\omega^{^{\prime}}_{y}\right.\\&\left.+8\left(-1+q^{2}\right)^{3}\left(1-12q^{2}-25q^{4}-25q^{6}-12q^{8}+q^{10}\right)\eta\omega^{^{\prime}}_{xyy}\right.\\&\left.+2\left(-1+q^{2}\right)^{5}\left(1+2q^{2}+2q^{4}+q^{6}\right)\eta\omega^{^{\prime}}_{xxyyy}\right.\\&\left.+16q^{2}\left(-1+q^{2}\right)^{3}\left(17+7q^{2}+7q^{4}+17q^{6}\right)\eta^{2}\left[\omega\omega_{xy}-\omega_{y}^{2}\right]\right.\\&\left.+q^{2}\left(-5-4q^{2}-13q^{4}+13q^{8}+4q^{10}+5q^{12}\right)\eta^{2}\left[12\omega_{yy}^{2}-24\omega_{yy}\omega_{xy}\right.\right.\\&\left.\left.-8\omega_{y}\omega_{yyy}+24\omega_{y}\omega{}_{xyy}+8\omega\omega_{xyyy}-12\omega\omega_{xxyy}\right]\right.\\&\left.+8\left(-1+q^{2}\right)^{4}\left(1-9q^{2}-8q^{4}-9q^{6}+q^{8}\right)\eta\left[\omega_{yy}\omega^{^{\prime}}_{y}-\omega_{y}\omega^{^{\prime}}_{\ y y}+\omega\omega^{^{\prime}}_{xyy}\right]\right.\\&\left.+\left(-1+q^{4}\right)^{2}\left(1+5q^{2}+6q^{4}+5q^{6}+q^{8}\right)\eta\left[-4\omega_{xyyy}\omega^{^{\prime}}_{y}+6\omega_{xxyy}\omega^{^{\'}}_{y}\right.\right.\\&\left.\left.+2\omega_{yyy}\omega^{^{\prime}}_{y y}-6\omega_{xyy}\omega^{^{\'}}_{y y}-2\omega_{yy}\omega^{^{\prime}}_{yyy}+4\omega_{xy}\omega^{^{\prime}}_{\ y y y}+6\omega_{yy}\omega^{^{\prime}}_{xyy}-4\omega_{y}\omega^{^{\prime}}_{\ xy y}+2\omega\omega^{^{\prime}}_{xxyyy}\right]\right.\\&\left.+3\left(-1+q^{4}\right)^{3}\left(1+q^{2}+q^{4}\right)\left[-\omega^{^{\prime}}_{yyy}\omega^{^{\prime}}_{xyy}+\omega^{^{\prime}}_{yy}\omega^{^{\prime}}_{\ xyyy}-\omega^{^{\prime}}_{y}\omega^{^{\prime}}_{xxyyy}\right]\right\},\end{aligned} \quad (27) \] 

with  \( q = e^{\eta} \) .

Using the representations via linear and non-linear integral equations for the functions  \( \omega \)  and  \( \omega' \)  of the previous section we can determine high-precision numerical values for the various two-point correlators. Figures 1-4 show selected examples of connected two-point functions. The longitudinal correlation functions  \( \langle\sigma_{1}^{z}\sigma_{n}^{z}\rangle_{T,h}-\langle\sigma_{1}^{z}\rangle_{ T,h}\langle\sigma_{n}^{z}\rangle_{T,h} \)  (n=2,3,4)
 

are shown in the left panels, while the right panels show the transversal correlation functions  \( \langle\sigma_{1}^{x}\sigma_{n}^{x}\rangle_{T,h}-\langle\sigma_{1}^{x}\rangle_{ T,h}\langle\sigma_{n}^{x}\rangle_{T,h} \) . Note that the contributions from the one-point functions are somewhat trivial. Due to the translational invariance of the Hamiltonian the longitudinal one-point functions do not depend on the site index,  \( \langle\sigma_{1}^{z}\rangle_{T,h}=\langle\sigma_{n}^{z}\rangle_{ T,h} \) , and are given by (18) for all n. The conservation of the z-component of the total spin, on the other hand, implies that  \( \langle\sigma_{n}^{x}\rangle_{T,h}=0 \) . The above notation for the connected two-point functions is merely used for systematic reasons.

In figure 1 we show the dependence of the correlation functions on the magnetic field for  \( \Delta=2 \)  and for several values of the temperature. At low temperatures one can clearly see the two critical fields of the ground state phase diagram, figure 5. The saturation field is at h=12 and the critical field at which the excitation gap opens can be calculated [12,33] to be located at  \( h\approx1.55921 \) . This can be seen even better in figure 4, where the  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle_{T,h}-\langle\sigma_{1}^{z}\rangle_{ T,h}\langle\sigma_{4}^{z}\rangle_{T,h} \)  correlation is shown for different low temperatures and for magnetic fields in the vicinity of the two critical fields. Here the curves for T/J=0.01 and T/J=0.001 are clearly distinguishable, which is not the case on the larger scale of figure 1. For fields above the saturation field h=12 the correlators have a fixed value as saturation sets in. For h below the lower critical field we observe a constant behaviour as well, which in this case is due to the excitation gap. In between, however, for values of the magnetic field for which the system is critical, an interesting non-monotonic behaviour can be seen. It is most pronounced for the correlators  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle_{T,h}-\langle\sigma_{1}^{z}\rangle_{ T,h}\langle\sigma_{4}^{z}\rangle_{T,h} \)  for which two local extrema exist if the temperature is sufficiently small. If the temperature is too high, thermal fluctuations dominate and all correlations die out. In figure 1 this is illustrated with the curve for T/J=10 in the n=2 case. For n=3,4 the effect is similar.

In figure 2 we show the correlation functions for several values of the magnetic field as functions of the temperature. Here we observe a non-monotonic behaviour as well for intermediate magnetic fields. Regarding the low temperature behaviour we notice that the connected correlation functions depend in a non-trivial way on the distance and on the magnetic field. There exists a field for which the connected correlation functions have maximal modulus. For nearest neighbours the figures for the transversal correlation functions on the right side, show the largest values for h/J=6, but for next nearest and next-to-next nearest neighbours the correlations for h/J=10 are more pronounced at low temperature. For the field strength h/J=16, which is above the saturation field, the connected correlation functions deviate the lesser from zero at intermediate temperatures the larger the distance is.

The excitation gap can also clearly be seen in the left panel in figure 3, where we show  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle_{T,h}-\langle\sigma_{1}^{z}\rangle_{ T,h}\langle\sigma_{4}^{z}\rangle_{T,h} \)  for low temperatures and several magnetic fields in the vicinity of the lower critical field. With increasing magnetic field the correlations start deviating from the h=0 line at lower and lower temperatures, until finally the zero temperature limit is different from the zero field case. Close to the critical field the system is particularly sensitive to small changes in the field strength, which can be well observed by comparing e.g. the correlation functions for h=1.56, slightly above the critical field, and h=1.55.
 

slightly below the critical field.

The right panel again shows  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle_{T,h}-\langle\sigma_{1}^{z}\rangle_{Th}\langle\sigma_{4}^{z}\rangle_{T,h} \) , but this time as a function of  \( \Delta \)  for fixed small temperature  \( T/J=0.01 \)  and several magnetic fields. For large values of  \( \Delta \)  the connected correlation function is independent of the magnetic field due to the excitation gap. The effect of the phase transition from the massive fully polarized state to the critical antiferromagnet is also visible in this figure. For h/J=8, for instance, we observe an abrupt change at  \( \Delta=1 \) , which, at this field strength, is the critical anisotropy at which saturation sets in. Note that for producing the data for  \( 0<\Delta<1 \)  in the figure we used the formulation and computer implementation of our previous work [3]. The curves smoothly match at  \( \Delta=1 \) .
 
![](./images/867760846585987207_1.jpg)

![](./images/867760846585987207_2.jpg)

![](./images/867760846585987207_3.jpg)

![](./images/867760846585987207_4.jpg)

![](./images/867760846585987207_5.jpg)

![](./images/867760846585987207_6.jpg)

Figure 1: (Color online)  \( \langle\sigma_{1}^{z}\sigma_{n}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{n}^{z}\rangle \)  and  \( \langle\sigma_{1}^{x}\sigma_{n}^{x}\rangle-\langle\sigma_{1}^{z}\rangle\langle\sigma_{n}^{x}\rangle \)  for different values of temperature T/J and fixed anisotropy  \( \Delta=2 \) . The rows are for n=2,3,4.
 
![](./images/867760846585987207_7.jpg)

Figure 2: (Color online)  \( \langle\sigma_{1}^{z}\sigma_{n}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{n}^{z}\rangle \)  and  \( \langle\sigma_{1}^{x}\sigma_{n}^{x}\rangle-\langle\sigma_{1}^{z}\rangle\langle\sigma_{n}^{x}\rangle \)  for different values of the magnetic field h/J and fixed anisotropy  \( \Delta=2 \) . The rows are for n=2,3,4.
 
![](./images/867760846585987207_8.jpg)

![](./images/867760846585987207_9.jpg)

Figure 3: (Color online) The left panel shows  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{4}^{x}\rangle \)  for different magnetic fields h/J and fixed anisotropy  \( \Delta=2 \)  at low temperatures. The right panel shows  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{4}^{x}\rangle \)  for different magnetic fields h/J as a function of the anisotropy  \( \Delta \)  at T/J=0.01.

![](./images/867760846585987207_10.jpg)

![](./images/867760846585987207_11.jpg)

Figure 4: (Color online)  \( \langle\sigma_{1}^{z}\sigma_{4}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{4}^{x}\rangle \)  for different low temperatures T/J and fixed anisotropy  \( \Delta=2 \) . The values of the magnetic field are in the vicinity of the critical fields.
 
![](./images/867760846585987207_12.jpg)

Figure 5: (Color online) Ground state phase diagram of the XXZ chain.
 

## 5 Ising limit

The subject of this work is the study of correlation functions of the XXZ chain for  \( \Delta > 1 \) . This includes the two extreme cases  \( \Delta = 1 \)  and  \( \Delta = \infty \) . The physically interesting isotropic point  \( \Delta = 1 \)  is difficult to access analytically. In fact, the regularization of the density matrix by a disorder field mentioned in the introduction fails exactly at this point, and it seems that the picture of factorization described above needs a slight modification in the presence of a magnetic field, when additional independent functions, called 'moments' in [5], appear. On the other hand, the numerics discussed in the previous section remain remarkably stable, if one approaches the isotropic point from above, and smoothly matches the numerics for approaching it from below [3].

For  \( \Delta = \infty \)  or, more precisely, in the limit  \( \Delta \to \infty \)  for finite  \( J_{I} = J\Delta \)  the XXZ Hamiltonian (1) turns into the Hamiltonian of the Ising chain

 \[ \mathcal{H}_{I}=J_{I}\sum_{j=-N+1}^{N}\left(\sigma_{j-1}^{z}\sigma_{j}^{z}-1\right)-\frac{h}{2}\sum_{j=-N+1}^{N}\sigma_{j}^{z}. \quad (28) \] 

The Ising chain may be viewed as a classical one-dimensional model of statistical mechanics with  \( 2 \times 2 \) -transfer matrix (see (39) below). For this reason its correlation functions can be calculated explicitly [2],

 \[ \left\langle\sigma_{j}^{z}\right\rangle=\frac{\mathrm{sh}\left(\frac{h}{2T}\right)}{\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}}, \quad (29a) \] 

 \[ \left\langle\sigma_{j}^{z}\sigma_{k}^{z}\right\rangle=\frac{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)}{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}+\frac{e^{4J_{I}/{T}}}{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/{T}}}\left(\frac{\mathrm{ch}\left(\frac{h}{2T}\right)-\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/{T}}}}{\mathrm{ch}\left(\frac{h}{2T}\right)+\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/{T}}}}\right)^{k-j}. \quad (29b) \] 

An interesting and non-trivial test of the formulae of the previous section is to reproduce these results analytically and numerically in the limit  \( \Delta \to \infty \) . A similar exercise starting from the multiple integral formulae of [14] was carried out in [17]. In our case at hand we start with the auxiliary functions in the b \( \bar{b} \) -formulation which turn into

 \[ \mathfrak{b}(x)=e^{-(h/2+4J_{I})/T}\left(-\mathrm{s h}\left(\frac{h}{2T}\right)+\sqrt{\mathrm{s h}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}\right) \quad (30a) \] 

 \[ \bar{\mathfrak{b}}(x)=\frac{e^{h/2T}}{-\mathrm{s h}\left(\frac{h}{2T}\right)+\sqrt{\mathrm{s h}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}} \quad (30b) \]
 

in the Ising limit. Note that, in this special case, they do not depend on the spectral parameter. This is also true for the functions

 \[ g_{\mu}^{\pm}(x)=-1\pm\frac{\mathrm{sh}\left(\frac{h}{2T}\right)}{\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}} \quad (31) \] 

which moreover do not depend on  \( \mu \)  anymore. The same is therefore true for

 \[ \varphi(\mu)=-\frac{\mathrm{sh}\left(\frac{h}{2T}\right)}{\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}} \quad (32) \] 

and

 \[ \omega(\mu_{1},\mu_{2})=-\mathrm{c t h}\left(\frac{2J_{I}}{T}\right)+\frac{e^{2J_{I}/T}}{\mathrm{s h}\left(\frac{2J_{I}}{T}\right)}\frac{\mathrm{c h}\left(\frac{h}{2T}\right)}{\sqrt{\mathrm{s h}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}}. \quad (33) \] 

Similarly, for  \( g_{\mu}^{\prime\pm} \) , for which a rescaling is necessary to obtain a sensible limit, one obtains

 \[ \frac{g_{\mu}^{\prime\pm}(x)}{\eta}=\mp\frac{1}{2}\left(1+\frac{\mathrm{ch}\left(\frac{h}{2T}\right)}{\sqrt{\mathrm{sh}^{2}\left(\frac{h}{2T}\right)+e^{4J_{I}/T}}}\right). \quad (34) \] 

Note that this rescaling is unproblematic for  \( \eta\to\infty \)  due to (15). Thus, we obtain

 \[ \frac{\omega^{\prime}(\mu_{1},\mu_{2})}{\eta}=0. \quad (35) \] 

The above leads to the correct results for  \( \langle\sigma_{1}^{z}\rangle \)  and  \( \langle\sigma^{z}_{1}\sigma^{z}_{2}\rangle \) . For the next-to-nearest neighbour and all higher correlation functions, however, some of the coefficients in the factorized form of the correlation functions may diverge in the Ising limit, e.g. the term  \( \mathrm{sh}^{2}(\eta)/\eta \)  on the right-hand side of (25a). All the terms where such type of divergence occurs have to be handled separately.

Sticking with the example of equation (25a) we define

 \[ f^{\pm}(x)=\lim_{\eta\to\infty}\mathrm{sh}(\eta)\partial_{\mu}^{2}g_{\mu}^{\pm}(x)\Big|_{\mu=0} \quad (36a) \] 

 \[ h^{\pm}(x)=\lim_{\eta\to\infty}\mathrm{sh}(\eta)\partial_{\mu}^{2}\frac{g_{\mu}^{\prime\pm}(x)}{\eta}\Bigg|_{\mu=0} \quad (36b) \]
 

implying

 \[ f^{+}(x)=-\frac{4}{1+\mathfrak{b}}e^{i2x}-4e^{-i2x} \quad (37a) \] 

 \[ f^{-}(x)=-e^{i2x}-\frac{4}{1+\mathfrak{b}}e^{-i2x} \quad (37b) \] 

 \[ h^{+}(x)=-\frac{4}{1+\mathfrak{b}}e^{i2x} \quad (37c) \] 

 \[ h^{-}(x)=\frac{4}{1+\mathfrak{b}}e^{-i2x} \quad (37d) \] 

with  \( b,\bar{b} \)  according to (30). Using the latter expressions we conclude that

 \[ \lim_{\eta\rightarrow\infty}\frac{\sin^{2}(\eta)}{\eta}\omega_{x x y}^{\prime}=4-\frac{16}{(1+\mathfrak{b})(1+\bar{\mathfrak{b}})} \quad (38) \] 

which indeed reproduces (29b) when inserted into the equation (25a) for  \( \langle\sigma_{1}^{z}\sigma_{3}^{z}\rangle \) .

After having shown that the Ising limit is included in our representation of the correlation functions by means of solutions of NLLE, it appears natural to compare the analytic limit with numerical results for large  \( \Delta \) . In figure 6 we show the temperature dependence of the connected two-point function  \( \langle\sigma_{1}^{z}\sigma_{3}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{3}^{z}\rangle \)  for the Heisenberg chain near the Ising limit, for different values of the anisotropy parameter and the magnetic field. In general, these curves do not depend on  \( \Delta \)  for large anisotropies and match the curves for the Ising limit given by (29). E.g., the curves in the left panel for  \( \Delta=1000 \)  and  \( h/J_{I}=3.9 \)  or  \( h/J_{T}=4.1 \) , respectively, match the corresponding Ising curves to the precision of the line width in the figure. In the vicinity of  \( h=4J_{I} \) , however, we observe large deviations from the low-temperature Ising curves.

This behaviour is induced by a critical point at  \( 1/\Delta = 0 \) ,  \( h = 4J_{I} \)  in the zero temperature phase diagram of the XXZ chain (see figure 7) which separates regions of different asymptotics for the two-point correlation functions of the Ising chain. The latter fact is most easily understood by inspection of the  \( 2 \times 2 \)  transfer matrix of the Ising chain [2],

 \[ t=\left(\begin{array}{c c}{e^{h/2T}}&{e^{2J_{I}/T}}\\ {e^{2J_{l}/T}}&{e^{-h/2T}}\\ \end{array}\right). \quad (39) \] 

Its eigenvalues  \( \lambda_{\pm}\left(\lambda_{+}>\lambda_{-}\right) \)  and eigenvectors  \( v_{\pm} \)  determine the partition function of the Ising chain as well as its two-point functions. In fact, when we wrote (29b), we used the formula [2]

 \[ \left\langle\sigma_{1}^{z}\sigma_{n+1}^{z}\right\rangle=\left\langle\mathbf{v}_{+},\sigma^{z}\mathbf{v}_{+}\right\rangle^{2}+\left\langle\mathbf{v}_{+},\sigma^{z}\mathbf{v}_{-}\right\rangle^{2}\left(\frac{\lambda_{-}}{\lambda_{+}}\right)^{n} \quad (40) \] 

and the explicit expression for the eigenvalues and eigenvectors of t, which the reader may easily calculate from (39). In order to understand the different zero temperature behaviour
 

of the Ising correlation functions it suffices to consider the low temperature asymptotics of the transfer matrix. Using (39), (40) one easily distinguishes three different asymptotic regimes.

 \[ \bullet\quad h>4J_{I}:\qquad t\sim e^{h/2T}\left(\begin{array}{l l}{1}&{0}\\ {0}&{0}\end{array}\right), \quad   \left\langle\sigma_{1}^{z}\sigma_{n+1}^{z}\right\rangle\sim1,   \quad (41a) \] 

 \[ \bullet\quad h<4J_{I}:\qquad t\sim e^{2J_{I}/T}\left(\begin{array}{l l}{0}&{1}\\ {1}&{0}\end{array}\right), \quad   \left\langle\sigma_{1}^{z}\sigma_{n+1}^{z}\right\rangle\sim(-1)^{n},   \quad (41b) \] 

 \[ \bullet\quad h=4J_{I}:\qquad t\sim e^{2J_{I}/T}\left(\begin{array}{l l}{1}&{1}\\ {1}&{0}\end{array}\right),\qquad\left\langle\sigma_{1}^{z}\sigma_{n+1}^{z}\right\rangle\sim\frac{1}{5}+\frac{4}{5}\left(\frac{1-\sqrt{5}}{1+\sqrt{5}}\right)^{n}. \quad (41c) \] 

Thus, in the Ising limit the absolute value of the ground state correlation functions is generally independent of the spatial separation, except at the critical field  \( h_{c} = 4J_{I} \) , where we see exponential decay due to the residual entropy resulting from an exponential degeneracy of the ground state. For finite  \( \Delta \)  this degeneracy is lifted by residual quantum mechanical interactions causing algebraically decaying correlations. The critical point of the Ising chain corresponding to a first order phase transition appears as a critical point in the ground state phase diagram of the XXZ chain if we draw it in the  \( h-1/\Delta \)  plane for fixed  \( J_{I} \) , see figure 7.

Contrary to the Ising case, there are always two critical fields if  \( \Delta \)  is finite. They correspond to two second order phase transition lines at the boundary of the critical phase in the h-1/ \( \Delta \)  diagram. This means that, away from the Ising limit, even the ground state correlation functions depend continuously on the magnetic field. Hence, for sufficiently low temperatures, there must be deviations from the Ising curves for values of h and  \( \Delta \)  belonging to the critical phase. In general the zero temperature limit should depend on the anisotropy and the magnetic field. This can be seen in the left panel in figure 6 for  \( h/J_{I}=3.9965 \) ,  \( \Delta=1000 \)  and  \( \Delta=2000 \) . However, as the width of the critical phase gets smaller with increasing  \( \Delta \) , one can find for each magnetic field, except for the critical field, a sufficiently large  \( \Delta \)  such that for larger anisotropies the correlation functions behave as in the Ising model.

For  \( h/J_{I}=4 \) , there is always a deviation in the zero temperature behaviour between the Ising chain and the XXZ chain for finite  \( \Delta \) . See figure 6, where the connected correlation functions are shown for  \( \Delta=1000 \) , 2000, 5000 and in the Ising limit. Interestingly in this case the zero temperature limit does not depend on the (finite) value of  \( \Delta \) . This is a general behaviour as we observe that the correlation functions are asymptotically constant on straight lines ending in the Ising critical point. We can see this exemplarily in the right panel of figure 6, where the connected correlation functions show the same zero temperature asymptotics for three different pairs of values of the anisotropy and the magnetic field.

Comparing these curves with those for the Ising model with the same magnetic fields, we identify four different temperature regimes. For very high temperatures the curves are
 

independent of  \( \Delta \)  and h. Then, for intermediate temperatures, they are independent of the (large) anisotropy and only depend on the magnetic field. This is where the curves for finite  \( \Delta \)  and the curves of the Ising model match. Next comes an regime where the correlation functions depend on the anisotropy and the magnetic field, and finally, for very low temperatures, only the product  \( (h - h_{c})\Delta \)  determines the correlation functions. In fact, this is a rare example, where the full low temperature asymptotics of thermodynamic quantities and short-range correlation functions in the vicinity of a critical point can be worked out analytically [16].

![](./images/867760846585987207_13.jpg)

![](./images/867760846585987207_14.jpg)

Figure 6: (Color online)  \( \langle\sigma_{1}^{z}\sigma_{3}^{z}\rangle-\langle\sigma_{1}^{x}\rangle\langle\sigma_{3}^{z}\rangle \)  for large values of the anisotropy, fixed  \( J_{I} \)  and different values of  \( h/J_{I} \) . The labels in both panels are the tupels  \( \Delta \) ,  \( h/J_{I} \)  where ‘Ising’ denotes the analytic Ising curves.
 
![](./images/867760846585987207_15.jpg)

Figure 7: (Color online) Ground state phase diagram of the XXZ chain in the  \( h-1/\Delta \)  plane for fixed  \( J_{I}=J\Delta \)  and large  \( \Delta \) .
 

## 6 Paramagnet

Another limit, which is interesting from a technical point of view, is the paramagnet J = 0. At a first glance it might look rather trivial. Yet, as the coefficients in section 4 depend on  \( \eta \) , the functions  \( \omega \) ,  \( \omega' \)  and  \( \varphi \)  depend on  \( \eta \)  as well, but the final result must not. In this sense the paramagnetic limit is even more intricate than the Ising limit, as, in contrast to the latter, all the summands in the algebraic part contribute. This way we have an additional test for the coefficients in (24)-(27). We note that the physical part takes the form

 \[ \varphi(\mu)=-\operatorname{t h}\left(\frac{h}{2T}\right), \quad (42a) \] 

 \[ \omega(\mu_{1},\mu_{2})=\tilde{K}_{\eta}(\tilde{\mu}_{2}-\tilde{\mu}_{1})\operatorname{t h}^{2}\left(\frac{h}{2T}\right), \quad (42b) \] 

 \[ \omega^{\prime}(\mu_{1},\mu_{2})=\tilde{L}_{\eta}(\tilde{\mu}_{2}-\tilde{\mu}_{1})\operatorname{t h}^{2}\left(\frac{h}{2T}\right). \quad (42c) \] 

in the paramagnetic limit.

## 7 Conclusion

We have studied the short-range correlation functions of the XXZ chain in the massive phase by means of the equations (24)-(27) representing them in factorized form. For this purpose we derived in section 3 a representation of the physical part of the correlation functions which is well suited for the implementation on a computer. We obtained high-accuracy data for the correlation functions of the spin chain in the thermodynamic limit. Together with our previous results  \( [3] \)  we can now access the full parameter plane of the infinite antiferromagnetic chain (anisotropy  \( \Delta > -1 \)  and magnetic field h arbitrary) at arbitrary temperatures. The short-range correlation functions show a surprisingly rich non-monotonous behaviour at intermediate magnetic fields and temperatures. At low enough temperatures the critical lines of the ground state phase diagram can be read off from our data. The numerics is stable in the isotropic limit  \( \Delta \rightarrow 1+ \)  and in the Ising limit  \( \Delta \rightarrow \infty \) .

So far our method is still limited in the accessible range of the correlation functions. In order to extend this range, an efficient algorithm for the calculation of the algebraic part of the correlation functions is needed. Since this is a well defined, purely algebraic problem though, we have little doubt that it will be solved in the future. For the exact calculation of the large-distance asymptotics at finite temperatures, on the other hand, we believe that new insight will be needed (for recent progress on the corresponding ground state problem see  \( [23] \) ).
 

## Acknowledgment

The authors are grateful to M. Karbach for helpful discussions. CT likes to acknowledge support by the research program of the Gradiiertenkolleg 1052 funded by the Deutsche Forschungsgemeinschaft.

## References

[1] M. Abramowitz and I. Stegun (eds.), Handbook of mathematical functions, 8th ed., Dover Publications, Inc., New York, 1975.

[2] R. J. Baxter, Exactly solved models in statistical mechanics, Academic Press, London, 1982.

[3] H. Boos, J. Damerau, F. Göhmann, A. Klümper, J. Suzuki, and A. Weiße, Short-distance thermal correlations in the XXZ chain, J. Stat. Mech. (2008), P08010.

[4] H. Boos and F. Göhmann, On the physical part of the factorized correlation functions of the XXZ chain, J. Phys. A 41 (2009), 315001.

[5] H. Boos, F. Göhmann, A. Klümper, and J. Suzuki, Factorization of multiple integrals representing the density matrix of a finite segment of the Heisenberg spin chain, J. Stat. Mech. (2006), P04001.

[6] ___, Factorization of the finite temperature correlation functions of the XXZ chain in a magnetic field, J. Phys. A 40 (2007), 10699.

[7] H. Boos, M. Jimbo, T. Miwa, and F. Smirnov, Completeness of a fermionic basis in the homogeneous XXZ model, preprint, arXiv:0903.0115, 2009.

[8] H. Boos, M. Jimbo, T. Miwa, F. Smirnov, and Y. Takeyama, Hidden Grassmann structure in the XXZ model II: creation operators, Comm. Math. Phys. (2009), 875.

[9] H. E. Boos and V. E. Korepin, Quantum spin chains and Riemann zeta function with odd arguments, J. Phys. A 34 (2001), 5311.

[10] M. Bortz and F. Göhmann, Exact thermodynamic limit of short range correlation functions of the antiferromagnetic XXZ chain at finite temperatures, Eur. Phys. J. B 46 (2005), 399.

[11] J. Damerau, F. Göhmann, N. P. Hasenclever, and A. Klümper, Density matrices for finite segments of Heisenberg chains of arbitrary length, J. Phys. A 40 (2007), 4439.

[12] J. Des Cloizeaux and M. Gaudin, Anisotropic linear magnetic chain, J. Math. Phys. 7 (1966), 1384.
 

[13] G. Gasper and M. Rahman, Basic hypergeometric series, Cambridge University Press, 1990.

[14] F. Göhmann, A. Klümper, and A. Seel, Integral representations for correlation functions of the XXZ chain at finite temperature, J. Phys. A 37 (2004), 7625.

[15] ___, Integral representation of the density matrix of the XXZ chain at finite temperature, J. Phys. A 38 (2005), 1833.

[16] F. Göhmann, A. Klümper, and C. Trippe, in preparation, 2009.

[17] F. Göhmann and A. Seel, XX and Ising limits in integral formulae for finite temperature correlation functions of the XXZ chain, Theor. Math. Phys. 146 (2006), 119.

[18] A. J. A. James, W. D. Goetze, and F. H. L. Essler, Finite temperature dynamical structure factor of the Heisenberg-Ising chain, Phys. Rev. B 79 (2009), 214408.

[19] M. Jimbo, K. Miki, T. Miwa, and A. Nakayashiki, Correlation functions of the XXZ model for  \( \Delta < -1 \) , Phys. Lett. A 168 (1992), 256.

[20] M. Jimbo and T. Miwa, Quantum KZ equation with  \( |q|=1 \)  and correlation functions of the XXZ model in the gapless regime, J. Phys. A 29 (1996), 2923.

[21] M. Jimbo, T. Miwa, and F. Smirnov, Hidden Grassmann structure in the XXZ model III: introducing Matsubara direction, J. Phys. A 42 (2009), 304018.

[22] G. Kato, M. Shiroishi, M. Takahashi, and K. Sakai, Third-neighbour and other four-point correlation functions of spin-1/2 XXZ chain, J. Phys. A 37 (2004), 5097.

[23] N. Kitanine, K. K. Kozlowski, J. M. Maillet, N. A. Slavnov, and V. Terras, Algebraic Bethe ansatz approach to the asymptotic behavior of correlation functions, J. Stat. Mech. (2009), P04003.

[24] N. Kitanine, J. M. Maillet, and V. Terras, Correlation functions of the XXZ Heisenberg spin- \( \frac{1}{2} \)  chain in a magnetic field, Nucl. Phys. B 567 (2000), 554.

[25] A. Klümper, Free energy and correlation length of quantum chains related to restricted solid-on-solid lattice models, Ann. Physik 1 (1992), 540.

[26] ___, Thermodynamics of the anisotropic spin-1/2 Heisenberg chain and related quantum chains, Z. Phys. B 91 (1993), 507.

[27] U. Löw, Néel order in the two-dimensional S=1/2 Heisenberg model, Phys. Rev. B 76 (2007), 220409.

[28] Y. Maeda, K. Sakai, and M. Oshikawa, Exact analysis of ESR shift in the spin-1/2 Heisenberg antiferromagnetic chain, Phys. Rev. Lett. (2005), 037602.
 

[29] S. N. M. Ruijsenaars, First order analytic difference equations and integrable quantum systems, J. Math. Phys. 38 (1997), 1069.

[30] M. Takahashi, G. Kato, and M. Shiroishi, Next nearest-neighbor correlation functions of the spin-1/2 XXZ chain at massive region, J. Phys. Soc. Jpn. 73 (2004), 245.

[31] C. Trippe and A. Klümper, Quantum phase transitions and thermodynamics of quantum antifferromagnets with competing interactions, Low Temp. Phys. 33 (2007), 920.

[32] Z. Tsuboi and M. Shiroishi, High temperature expansion of the emptiness formation probability for the isotropic Heisenberg chain, J. Phys. A 38 (2005), L363.

[33] C. N. Yang and C. P. Yang, One-dimensional chain of anisotropic spin-spin interactions. III. Applications, Phys. Rep. 151 (1966), 258.
 
