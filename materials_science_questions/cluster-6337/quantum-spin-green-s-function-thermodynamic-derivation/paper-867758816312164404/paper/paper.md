
# Quantum and classical correlations in the solid-state NMR free induction decay.

V. E. Zobov \( ^{1} \)  and A. A. Lundin \( ^{2} \) 

 \( ^{1} \) L. V. Kirensky Institute of Physics, Siberian Branch, RAS, 660036, Krasnoyarsk, Russia,

 \( ^{2} \) N. N. Semenov Institute of Chemical Physics, RAS, 117977, Moscow, Russia,

e-mail: rsa@iph.krasn.ru

The free-induction decay (FID) of the transverse magnetization in a dipolar-coupled rigid lattice is a fundamental problem in magnetic resonance and in the theory of many-body systems. As it was shown earlier the FID shapes for the systems of classical magnetic moments and for quantum nuclear spins ones coincide if there are many quite equivalent nearest neighbors V in a solid lattice. In this paper, we reduce a multispin density matrix of above system to a two-spin matrix. Then we obtain analytic expressions for the mutual information and the quantum and classical parts of correlations at the arbitrary spin quantum number S, in the high-temperature approximation. The time dependence of these functions is expressed via the derivative of the FID shape. To extract classical correlations for  \( S>1/2 \)  we provide generalized POVM measurement using the basis of spin coherent states. We show that in every pair of spins the portion of quantum correlations changes from 1/2 to  \( 1/(S+1) \)  when S is growing up, and quantum properties disappear completely only if  \( S\to\infty \)  and not in the case when  \( V\to\infty \) .

PACS numbers: 03.67.Mn, 67.57.Lm, 76.60.-k

## I. INTRODUCTION

Nuclear spin systems observed by nuclear magnetic resonance (NMR) really for a long time and yet now perform a suitable laboratory for studying of physics of nonequilibrium processes in quantum many-body systems. Some of the most of fundamental lines of that type activities are the emergence and growth of correlations, spin dynamics and so on [1]. Quite recently applications of the NMR spin dynamics to investigate quantum information processing were initiated [2]. It is usually assumed that the quantum correlation existing both at low and at high temperatures influence the performance speed of quantum computer [3]. In this regard, the interest of researchers has shifted from the calculation of the correlation function as a whole to their partitioning into quantum and classical parts (e.g. see the review [3]). On the other hand different time correlation functions determine observed NMR signals in conventional NMR [1]. However their decomposition in quantum and classical components has not been done yet. In the present article it will be done for one of the most significant NMR time correlation functions, namely, for the free induction decay (FID) function.

The FID shape links to the shape of NMR absorption line via Fourier transform [1]. In the
 

many-body spin systems of solids, the calculation of the time correlation functions is a very challenging problem and different approaches to it solution has been widely discussed. In light of the above, point the works  \( [4, 5] \) . In the article  \( [4] \) , the numerical simulation has been used to derive FID curves for a simple cubic lattice with 216 classical magnetic moments (classical spins) coupled by dipole-dipole interaction. It was found that the calculated FID shape is close to the FID shape of fluorine nuclei (nuclear spin S = 1/2) which was experimentally measured in  \( CaF_{2} \)   \( [6] \) . In Ref.  \( [5] \)  we explained this result. We showed that the time dependence of FID for the system consisting of quantum spins and one formed by classical magnetic moments  \( \mu = \gamma \hbar \sqrt{S(S + 1)} \)  coincides in a limit of a large number of the equivalent nearest neighbors surrounding a probe spin (anyone spin) in a lattice. The deduction has been made on the basis of the analysis of various contributions to the spectral moments of all orders of NMR spectrum. Actually in Ref. \( [5] \)  we demonstrated that if the numbers of the rather equivalent nearest neighbors for any spin is large enough then the principal contributions to the arbitrary NMR spectral moment carrying in by the terms of the moment with maximum number of the summing indexes on the lattice. Referred above contributions coincide exactly for classical and quantum spin systems. So it works for ordinary regular three-dimensional lattices (e.g. simple cubic one). Comparison of the values of the exact spectral moments from  \( M_{4} \)  to  \( M_{8} \) , performed in Ref.  \( [5] \)  also revealed insignificant discrepancies between results for the systems of quantum and classical spins.

It is interesting to calculate share of quantum correlations under these conditions. One of the approaches to solution the problem of clearing quantum effects (quantum correlations) consists of the reduction of the multispin density matrix to the two-spin matrix with the subsequent analysis of pair correlations [3]. Thus, such approach is applied to the description of one-dimensional XY-chain in Refs. [7, 8], and also, in Ref. [9], to investigation of spins in nanopore with equal dipolar interaction between any two spins. In both cases, only nuclei with a spin quantum number S=1/2 only were studied. In the present work we consider lattices formed by nuclei with an arbitrary spin S. Any disturbing quadrupole effects are neglected. We will provide a reduction of the multispin density matrix to a two-spin matrix. Then, following the program put forward in Ref. [10], we are going to calculate shares of quantum and classical correlations: for S=1/2 we shall use the von Neumann orthogonal measurement, whereas for S>1/2 we shall provide generalized POVM measurement (positive-operator-valued-measure) [3, 11] using the basis of spin coherent states (SCS) [12]. In spite of our basic goal for the present paper consisting of studying spin systems coupled by a dipole-dipole interaction we are going also to consider model lattices with spin-spin interaction only between spin components, parallel to the external magnetic field (Ising like interaction) because the last one allows to get some exact results.
 

## II. HAMILTONIAN AND SOME BASIC EQUATIONS OF THE PROB-LEM.

In traditional experiments employing NMR, the spin temperature considerably exceeds the energy of the Zeeman and other interactions in the spin system. As a consequence, polarization is very small for nuclear spin in the strong static magnetic field at room temperature T,  \( \beta = \hbar\omega_{0}/kT \approx 10^{-5} \ll 1 \)  ( \( \omega_{0} \)  is the Larmor frequency), and the equilibrium density matrix has the form [1]:

 \[ \hat{\rho}_{e q}=(1+\beta\hat{S}_{z})/Z, \quad (1) \] 

where Z is the partition function,  \( \hat{S}_{\alpha}=\sum_{j}\hat{S}_{j\alpha} \) ,  \( \hat{S}_{j\alpha}\hat{S}_{j\alpha} \)  is the  \( \alpha \) -component ( \( \alpha=x,y,z \) ) of the spin j, and the external magnetic field  \( H_{0} \)  is directed along the z axis. As well known [1] for observation of a FID signal it is necessary preliminary to prepare the spin system using the pulse of the radio-frequency magnetic field causing rotation of spins at  \( \pi/2 \) -angle around the y axis of the rotating with the Larmor frequency reference frame. So we get

 \[ \hat{\rho}(0)=\hat{Y}\hat{\rho}_{e q}\hat{Y}^{-1}=(1+\beta\hat{S}_{x})/Z. \] 

This initial density matrix evolves in time as

 \[ \hat{\rho}(t)=\hat{U}(t)\hat{\rho}(0)\hat{U}^{-1}(t)=[1+\beta\hat{U}(t)\hat{S}_{x}\hat{U}^{-1}(t)]/Z=[1+\beta\Delta\hat{\rho}(t)]/Z, \quad (2) \] 

where  \( \hat{U}(t)=\exp(-i\hat{H}t/\hbar) \)  is the operator of evolution with the Hamiltonian  \( \hat{H} \) . An observable signal of FID is proportional to time-correlation function:

 \[ F(t)=\frac{T r\{\hat{S}_{x}\hat{\rho}(t)\}}{T r\{\hat{S}_{y}\hat{\rho}(0)\}} \quad (3) \] 

and it links to the shape of NMR absorption line via the Fourier transform.

As it is known [1], in nonmetallic diamagnetic solids (at least consisting of light nuclei (e.g., protons or  \( {}^{19} \) F nuclei)), a principal cause of the absorption NMR line broadening is a secular part of dipole-dipole interaction between nuclear spins. So this interaction completely specifies the dynamics of the nuclear spin system:

 \[ \hat{H}_{d}=\sum_{i\neq j}b_{i j}\hat{S}_{z i}\hat{S}_{z j}+\sum_{i\neq j}a_{i j}(\hat{S}_{x i}\hat{S}_{x j}+\hat{S}_{y i}\hat{S}_{y j})=\sum_{i\neq j}b_{i j}\hat{S}_{z i}\hat{S}_{z j}+\sum_{i\neq j}a_{i j}\hat{S}_{+i}\hat{S}_{-j}=\hat{H}_{z z}+\hat{H}_{f f}, \quad (4) \] 

where  \( \hat{S}_{i\pm}=\hat{S}_{ix}\pm i\hat{S}_{iy} \) ,  \( b_{ij}=\gamma^{2}\hbar(1-3\cos^{2}\theta_{ij})/2r_{ij}^{3} \) ,  \( a_{ij}=-b_{ij}/2 \) ,  \( \vec{r}_{ij} \)  is the vector connecting spins i and j,  \( \theta_{ij} \)  is the angle, formed by vector  \( \vec{r}_{ij} \)  with the static external magnetic field. From here on, energy is expressed in frequency units.

Let's suppose that the system is in equilibrium in the strong external magnetic field for which Zeeman splitting substantially exceeds spin-spin interaction (4). Therefore the initial state
 

of the system is well described by the density matrix (1). In this initial state all correlations are absent. In the course of evolution to the state described by Eq. (2) dynamic correlations are forming in the system. One of approaches to their examination consists in a reduction of the multispin density matrix (2) to the two-spin matrix with the subsequent analysis of pair correlations and to their partitioning into quantum and classical parts [3, 7 - 9]. For such a reduction we will choose two spins in the lattice points i and j and then calculate a trace in Eq. (2) over all other spin variables. The density matrix  \( \hat{\rho}_{ij}(t) \)  obtained will depend only on spin states of two nuclei i and j and in the present section we will use appropriate numbers accordingly 1 and 2.

The information-theoretic measure of correlations between two spins is the mutual information [3, 11],

 \[ I(\hat{\rho}_{12})=S_{N}(\hat{\rho}_{1})+S_{N}(\hat{p}_{2})-S_{N}(\hat{\rho}_{12}), \quad (5) \] 

where  \(  S_{N}(\hat{\rho}) = -Tr\{\hat{\rho}\log_{2}\hat{\rho}\}  \)  is the von Neumann entropy,  \( \hat{\rho}_{1} = Tr_{2}\hat{\rho}_{12} \) ,  \( \hat{\rho}_{2} = Tr_{1}\hat{\rho}_{12} \)  are the density matrices reduced to one spin. We assume to calculate the von Neumann entropy in the lowest order on  \( \beta \)  [1, 10],

 \[ S_{N}(\hat{\rho})=-T r\{\hat{\rho}\log_{2}\hat{\rho}\}\approx\log_{2}Z-\frac{\beta^{2}}{2Z\ln2}T r(\Delta\hat{\rho})^{2}. \] 

In the high-temperature approach accepted the mutual information (5) is as follows:

 \[ I(\hat{\rho}_{12})=\frac{\beta^{2}}{2\ln2}\left\{\frac{1}{d^{2}}T r(\Delta\hat{\rho}_{12})^{2}-\frac{1}{d}T r_{1}(\Delta\hat{\rho}_{1})^{2}-\frac{1}{d}T r_{2}(\Delta\hat{\rho}_{2})^{2}\right\}, \quad (6) \] 

where  \( d = 2S + 1 \) .

The mutual information (5) is used to measure the total correlations, which are sums of the classical and quantum correlations. The classical correlations can be calculated by the measurement, described in [3]. To perform a von Neumann measurement we must project the state  \( \hat{\rho}_{12}(t) \)  on the complete basis of orthogonal wave functions  \( \left|\Psi_{m}\right\rangle \)  by means of a complete set of projectors,

 \[ \hat{\Pi}_{m}=\left|\Psi_{m}\right\rangle\left\langle\Psi_{m}\right|,\qquad\sum_{m}\hat{\Pi}_{m}=1. \quad (7) \] 

In the case of system with S=1/2 the complete set of orthogonal projectors of the first spin consists of two projectors of a general form,

 \[ \hat{\Pi}_{1\pm}=\frac{1}{2}[1\pm(n_{x}\hat{\sigma}_{1x}+n_{y}\hat{\sigma}_{11y}+n_{z}\hat{\sigma}_{1z})], \quad (8) \] 

where  \( n_{\alpha} \)  are the direction cosines,  \( \hat{\sigma}_{\alpha} \)  are the Pauli matrices, and  \( \alpha = x, y, z \) .

The density matrix  \( \hat{\rho}_{12}(t) \)  is transformed after projecting on the states of the first spin to
 

 \[ \hat{\Pi}_{1}(\hat{\rho}_{12})=\frac{1}{Z}[1+\beta\hat{\Pi}_{1}(\Delta\hat{\rho}_{12}(t))], \quad (9) \] 

where we have

 \[ \hat{\Pi}_{1}(\Delta\hat{\rho}_{12}(t))=\sum_{m}(\hat{\Pi}_{1m}\otimes\hat{\mathrm{E}}_{2})\Delta\hat{\rho}_{12}(t)(\hat{\Pi}_{1m}\otimes\hat{\mathrm{E}}_{2}), \] 

and where  \( \hat{E}_{2} \)  is the unit matrix.

If one wants to use the generalized POVM measurement, he must recognize that the functions  \( \left|\Psi_{m}\right\rangle \)  in operators (7) can now be no orthogonal, and these operators strictly speaking are then already not projectors [11]. It is assumed that the spin coherent states (SCS) (Bloch states) [12]

 \[ \left|\theta,\varphi\right\rangle=\hat{R}(\theta,\varphi)\left|S\right\rangle=\sum_{m=-S}^{m=S}\left(\begin{array}{c}2S\\ S+m\end{array}\right)^{1/2}\left(\cos\theta/2\right)^{S+m}\left(e^{i\varphi}\sin\theta/2\right)^{3-m}\left|m\right\rangle, \quad (10) \] 

are closest to the states of the classical momenta. Here  \( \theta \)  and  \( \varphi \)  are the polar and azimuthal angles on the unit sphere (Bloch sphere),  \( \left|m\right\rangle \)  is an eigenstate of the operator  \( S_{z} \)  with eigenvalues m assuming  \( 2S+1 \)  values,

 \[ -S,-S+1,\cdots,S-1,S. \] 

These states (10) are obtained from the ground state  \( \left|S\right\rangle \)  by the rotation operator  \( \hat{R}(\theta,\varphi) \)  and are a superposition of states with different m. The average values of spin projections in the state (10) are as follows

 \[ \left\langle\theta,\varphi|\hat{S}_{z}\right|\theta,\varphi\rangle=S\cos\theta,\quad\left\langle\theta,\varphi|\hat{S}_{x}\right|\theta,\varphi\rangle=S\sin\theta\cos\varphi,\quad\left\langle\theta,\varphi|\hat{S}_{y}\right|\theta,\varphi\rangle=S\sin\theta\sin\varphi \] 

and are the same as for classical momentum. The completeness property

 \[ \frac{2S+1}{4\pi}\int\left|\theta,\varphi\right\rangle\left\langle\theta,\varphi\right|\sin\varTheta d\varTheta d\varphi=1 \] 

is satisfied for the SCS basis, but this basis is not orthogonal.

We take the SCS system as the measurement basis in Eq. (7), to perform the POVM measurement of the first spin, which reduces to multiplying by the SCS and calculating the trace, and obtain the classical density function for the probability distribution of the angle values

 \[ \hat{\rho}_{2}(\theta_{1}\varphi_{1};t)=\frac{(2S+1)}{4\pi}T r_{1}\{\hat{\rho}_{12}(t)|\theta_{1},\varphi_{1}\rangle\langle\theta_{1},\varphi_{|}\otimes\hat{E}_{2}\}=\frac{(2S+1)}{4\pi}\langle\theta_{1},\varphi_{|}|\hat{\rho}_{12}(t)|\theta_{1},\varphi_{1}\rangle. \quad (11) \] 

Now to calculate the Shannon entropy we must calculate the integral over the Bloch sphere

 \[ S_{S h N}(\hat{\rho}_{2}(\theta_{1}\varphi_{1};t))=-\int T r_{2}\{\hat{\rho}_{2}(\theta_{1}\varphi_{1};t)\log_{2}\hat{\rho}_{2}(\theta_{1}\varphi_{1};t)\}\sin\theta_{1}d\theta_{1}d\varphi_{1}. \] 

As usual let us choose the mutual information  \(  I(\hat{\Pi}_{1}(\hat{\rho}_{12}))  \)  calculated using formulas (5), (9) and (11) for this matrix, as a measure of classical correlations. Unfortunately the gained value
 

will depend on the chosen basis (7). It was proposed [3] to search all bases and to take the maximum value of correlation  \( I(\hat{\Pi}_{1}(\hat{\rho}_{12})) \)  as the universal measure. However, such a program can be realized only for some simple cases, e.g. for two-level system. If we subtract the classical part from all correlations (5), then we obtain the quantum part of the correlations

 \[ Q_{12}=I(\hat{\rho}_{12})-I(\hat{\Pi}_{1}(\hat{\rho}_{12})). \quad (12) \] 

After carrying out of minimization of this quantity on measurement bases one gains an entropy measure of quantum correlations named by quantum discord  \( D_{12} \)  [3]. Measure (12) without optimization was called a measurement dependent discord [3].

## III. THE MODEL CALCULATIONS WITH ISING LIKE-INTERACTION ONLY.

We are going to study the general case of Hamiltonian (4) in the following section, while now, at the first stage, let's put  \( a_{ij} = 0 \) . In this case, the time evolution of the matrix (2) can be written out in the explicit form

 \[ \hat{\rho}(t)=\frac{1}{Z}\Biggl\{1+\frac{\beta}{2}\Biggl[\sum_{i}\hat{S}_{i+}\prod_{j(\neq i)}\exp(-i t2b_{i j}\hat{S}_{j z})+\sum_{i}\hat{S}_{i-}\prod_{j(\neq i)}\exp(i t2b_{i j}\hat{S}_{j z})\Biggr]\Biggr\}. \quad (13) \] 

So the observable FID signal (3) is

 \[ F_{z z}(t)=\prod_{j(\neq i)}\frac{\sin(d b_{i j}t)}{d\sin(b_{i j}t)}. \quad (14) \] 

If a number of equivalent nearest neighbors V in formula (14) is large enough it can be adequate approximated by the Gaussian function

 \[ F_{G}(t)=\exp\left\{-M_{2}^{z z}t^{2}/2\right\} \quad (15) \] 

where

 \[ M_{2}^{z z}=\frac{4}{3}S(S+1)\sum_{j}b_{i j}^{2}. \] 

Under these conditions the FID shape does not depend on S and, therefore, coincides with the FID shape of the system of classical magnetic moments with  \( \mu=\gamma\hbar\sqrt{S(S+1)} \)  which one gets in the limit  \( S\to\infty \) .

We can discriminate functions given by Eqs. (15) and (14) using discrepancy of their fourth moments:

 \[ M_{G4}=3(M_{2}^{zz})^{2}=3\Biggl[\frac{4}{3}S(S+1)\sum_{j}b_{ij}^{2}\Biggr]^{2}, \] 

 \[ M_{4}^{z z}=3(M_{2}^{z z})^{2}-\frac{3}{5}\Biggl[\frac{4}{3}S(S+1)\Biggr]^{2}\Biggl\{2+\frac{1}{S(S+1)}\Biggr\}\sum_{j}b_{i j}^{4}. \quad (16) \]
 

As it follows from Eq. (16) the above discrepancy  \( \Delta M_{4}=M_{G4}-M_{4}^{zz} \)  expressed through the lattice sum with only one summation via lattice sites whereas quantity of the moment (16) defines by the lattice sums with two such indexes of summation containing in  \( (M_{2}^{zz})^{2} \) , and therefore  \( \Delta M_{4}/M_{4}^{zz}\sim1/V \) .

What does it really mean? Whether coincidence of the FID shapes at  \( V \rightarrow \infty \)  means disappearance of quantum correlations? To answer this question, we will execute a reduction of a density matrix (13) [7-9]. Let us fix two spins in sites i and j and then calculate a trace in Eq. (13) over all other spin variables. So we get

 \[ \begin{aligned}&\hat{\rho}_{ij}(t)=\frac{1}{d^{2}}\Biggl\{1+\frac{\beta}{2}\Big[G_{i(j)}(t)\hat{S}_{i+}\exp(-it2b_{ij}\hat{S}_{jz})+\\ &+G_{i(j)}(t)\hat{S}_{i-}\exp(it2b_{ij}\hat{S}_{jz})+G_{j(i)}(t)\hat{S}_{j+}\exp(-it2b_{ij}\hat{S}_{iz})+G_{j(i)}(t)\hat{S}_{j-}\exp(it2b_{ij}\hat{S}_{iz})\Big]\Biggr\},\\ \end{aligned} \] 

 \[ G_{i(j)}(t)=\prod_{f(\neq i,j)}\frac{\sin(d b_{i f}t)}{d\sin(b_{i f}t)},\;G_{j(i)}(t)=\prod_{f(\neq i,j)}\frac{\sin(d b_{j f}t)}{d\sin(b_{j f}t)}. \quad (17) \] 

To simplify the analysis let us suppose that all the spins occupy equivalent positions in the lattice. As a result one can write

 \[ G_{i(j)}(t)=G_{j(i)}(t)\equiv G_{i j}(t), \] 

and the density matrix becomes

 \[ \hat{\rho}_{i j}(t)=\{1+\beta\Delta\hat{\rho}_{i j}\left(t\right)\}/d^{2} \quad (18) \] 

where

 \[ \begin{aligned}&\Delta\hat{\rho}_{ij}(t)=G_{ij}(t)[\hat{S}_{i+}\exp(-it2b_{ij}\hat{S}_{jz})+\hat{S}_{i-}\exp(it2b_{ij}\hat{S}_{jz})+\\ &+\hat{S}_{j+}\exp(-it2b_{ij}\hat{S}_{iz})+\hat{S}_{j-}\exp(it2b_{ij}\hat{S}_{iz})]/2.\\ \end{aligned} \] 

Expression (18) differs from the similar expression for isolated pair of spins, obtained in Ref. [10], owing to replacement of  \( \tau \)  by  \( t2b_{ij} \)  and  \( \beta \)  by  \( \beta G_{ij}(t) \) . Therefore, omitting intermediate evaluations, let's state the final results at once. At first, for the mutual information (6) with  \( \Delta\hat{\rho}_{12} = \Delta\hat{\rho}_{\dot{ij}}(t) \)  we get

 \[ I(\hat{\rho}_{i j})=\frac{(\beta G_{i j}(t))^{2}}{3\ln2}S(S+1)[1-g_{i j}^{2}(t)], \quad (19) \] 

where

 \[ g_{i j}(t)=\frac{\sin(d b_{i j}t)}{d\sin(b_{i j}t)}. \]
 

And secondly, if S = 1/2 we obtain for classical  \(  C_{ij} = I(\hat{\Pi}_{1}(\hat{\rho}_{ij}))  \)  and quantum (by using quantum discord (12)  \( D_{ij} \) ) parts of correlations

 \[ C_{ij}=D_{ij}=\frac{1}{2}I(\hat{\rho}_{ij})=\frac{(\beta G_{ij}(t))^{2}}{8\ln2}\sin^{2}(tb_{ij}). \quad (20) \] 

The result (20) is gained by means of the von Neumann orthogonal measurement (9) with the projectors (8) on one of the spins. At last, if S > 1/2 for classical  \( (J_{ij}) \)  and quantum  \( (Q_{ij}) \)  parts of correlations one gets

 \[ J_{ij}=\frac{(\beta G_{ij}(t))^{2}}{6\ln2}\big\{S(S+1)\big[f_{ij}(t)-g_{ij}^{2}(t)\big]+S^{2}\big[1-g_{ij}^{2}(t)\big]\big\}, \quad (21) \] 

 \[ Q_{ij}=I(\hat{\rho}_{ij})-J_{ij}=\frac{(\beta G_{ij}(t))^{2}}{6\ln2}\big\{S(S+1)\big[1-f_{ij}(t)\big]+S\big[1-g_{ij}^{2}(t)\big]\big\}. \quad (22) \] 

In the above equations we use notation

 \[ f_{ij}\left(t\right)=\sum_{n=0}^{n=2S}\binom{2S}{n}\frac{\left(2n\right)!!}{\left(2n+1\right)!!}\left(-1\right)^{n}\left(\sin t b_{ij}\right)^{2n}. \] 

The formula (21) is gained by using the generalized POVM measurement (11) with the basis from SCS (10).

The expressions (21) and (22) describe evolution of required parts of correlations with time. To make a qualitative analysis of their behavior for the large number of neighbors V we need to pay attention the fact that in this case function  \(  G_{ij}(t)  \)  (17) rapidly dies out at time scale with the order of  \( 1/\sqrt{M_{2}^{zz}} \) . At such times we have

 \[ \left|b_{ij}t\right|\sim\sqrt{b_{ij}^{2}/M_{2}^{zz}}\sim1/\sqrt{V}<<1. \] 

Therefore in Eqs. (19), (21) and (22) it is possible to keep only first nonvanishing terms in expansion of the functions  \( f_{ij}(t) \) ,  \( g_{ij}(t) and also \sin tb_{ij} \)  in powers of t. So we get

 \[ I(\hat{\rho}_{ij})\approx\frac{(\beta G_{ij}(t))^{2}}{9\ln2}4[S(S+1)b_{ij}t]^{2}, \quad (23) \] 

 \[ Q_{ij}\approx\frac{(\beta G_{ij}(t))^{2}}{9\ln2}4[Sb_{ij}t]^{2}(S+1). \quad (24) \] 

From here for the relative share of quantum correlation we can extract

 \[ Q_{ij}/I(\hat{\rho}_{ij})\approx1/(S+1), \quad (25) \] 

i.e. we reveal that as S is growing up the share of quantum correlations decreases. We would note also that if S = 1/2 expression (25) is equal to 2/3 whereas from Eq. (20) one gets 1/2. The discrepancy is related to the distinctions in the methods of measurement.
 

## IV. Dipole-dipole interaction case

Now let us study system with the total Hamiltonian (4). Interaction between transversal spin components does not allow writing down just now an explicit time dependence of the density matrix in a so simple form as Eq. (13). In this situation for finding the appropriate form of the density matrix, we shall decompose it over the complete system of orthogonal operators  \( [k] \)  following the line outlined in ref. [13 - 15]. In this representation

 \[ \hat{S}_{x}(t)=\hat{U}(t)\hat{S}_{x}\hat{U}^{-1}(t)=\sum_{k=0}^{\infty}A_{k}(t)[k]. \quad (26) \] 

The initial operator  \( [0)=\hat{S}_{x} \) . Each subsequent operator of the basis is obtained from the previous one after the procedure of commutation with the Hamiltonian according to the recursion relations:

 \[ \begin{aligned}\left[1\right)=i\left[\hat{H}_{d},\left[0\right]\right]\quad\left[k+1\right)=i\left[\hat{H}_{d},\left[k\right]\right]+\nu_{k-1}^{2}\left[k-1\right)\quad\left(i f k\geq1\right),\\\nu_{k}^{2}=Sp\left(\left\{k+1|k+1\right\}\right)/Sp\left(\left\{k|k\right\}\right).\end{aligned} \quad (27) \] 

For amplitudes  \( A_{k}(t) \)  the system of the differential equations [13, 14] has been revealed

 \[ \dot{A}_{0}(t)=\nu_{0}^{2}A_{1}(t),\quad\dot{A}_{k}(t)=A_{k-1}(t)-\nu_{k}^{2}A_{k+1}(t)\quad(i f k\geq1). \quad (28) \] 

To avoid confusion, a certain difference in the definition of amplitudes  \( A_{k}(t) \)  in references [13] and [14] should be noticed. The difference is in the factor  \( (i)^{k} \) . We have chosen a variant used in ref. [14] at which functions  \( A_{k}(t) \)  contain no imaginary part, because the factor  \( (i)^{k} \)  is included into definition of operators  \( [k] \) . The parameters  \( \{v_{k}\} \)  which values determine the solution of the system (28), are expressed unequivocally through the moments of the NMR absorption line [13]. In particular

 \[ \nu_{0}^{2}=M_{2}=3S(S+1)\sum_{j}b_{j}^{2},\ \nu_{1}^{2}=(M_{4}-M_{2}^{2})/M_{2},\ \nu_{2}^{2}=(M_{2}M_{6}-M_{4}^{2})/(M_{4}-M_{2}^{2})M_{2}, \quad (29) \] 

where  \( M_{2}, M_{4}, M_{6} \)  are the second, fourth and sixth moments of the NMR absorption line.

Let us substitute decomposition (26) to Eq. (2) and then execute the reduction. As it means we have to choose two spins at sites i and j and then to calculate a trace in Eq. (2) over all other spin variables. Thus we have

 \[ \hat{\rho}_{i j}(t)=\frac{1}{d^{2}}\left\{1+\beta\sum_{k=0}^{\infty}A_{k}(t)\frac{d^{2}}{Z}T r\left[k\right]\right\}. \quad (30) \] 

So for the first two orthogonal operators of the complete set we get

 \[ \frac{1}{Z}T r\left[0\right)=\frac{1}{Z}Tr\sum_{f}\hat{S}_{x f}=\frac{1}{d^{2}}(\hat{S}_{x i}+\hat{S}_{x j}), \quad (31) \]
 

 \[ \frac{1}{Z}Tr[1]=\frac{i}{Z}\underset{\neq i,j}{Tr}[\hat{H}_{d},\hat{S}_{x}]=\frac{-2}{d^{2}}(b_{ij}-a_{ij})(\hat{S}_{yi}\hat{S}_{zj}+\hat{S}_{yj}\hat{S}_{zi}). \quad (32) \] 

The contribution to Eq. (30) from orthogonal operators of the higher order can be obtained in two cases. First case assumes zero direct interaction between the chosen spins i and j. It is a possible case for example, if the angle  \( \theta_{ij} \)  between the vector  \( \vec{r}_{ij} \)  and external magnetic field is equal to the "magic" value  \( 54^{0}44' \) . In this situation we have to take into account the contribution from vector [3] which depends on the constant  \( b_{ij}b_{jf}^{2} \)  through the intermediate spin f if this constant is distinct from zero. The second case appears if S > 1/2 because orthogonal operators of the high order are formed of products of spin operators not only from different sites, but also from the same site. For examples in vector [2] there is a contribution  \( \hat{S}_{xi}\{\hat{S}_{zj}^{2}-S(S+1)/3\} \) , and in vector [3] one gets a contribution  \( \hat{S}_{yi}\{\hat{S}_{zj}^{3}-\hat{S}_{zj}(3S^{2}+3S-1)/5\} \) . We shall neglect above mentioned contributions in Eq. (30) as far as these parts do not contain new qualitative properties, and are small corrections to contributions from Eqs. (31) and (32). The trifle of discussing corrections is a consequence of the different time dependence of the different order amplitudes:  \( A_{k}(t)\sim t^{k} \)  at small times. Because of the rapid decay of amplitudes at times  \( t\geq1/\sqrt{M_{2}} \) , each additional power of t adds only a small factor  \( \left|b_{ij}t\right|\sim\sqrt{b_{ij}^{2}/M_{2}}\sim1/\sqrt{V}<<1 \) .

Having retained two contributions (31) and (32) in Eq. (30) we get

 \[ \hat{\rho}_{i j}(t)\approx\frac{1}{d^{2}}\{1+\beta A_{0}(t)(\hat{S}_{x i}+\hat{S}_{x j})+\beta A_{1}(t)B_{i j}(\hat{S}_{y i}\hat{S}_{z j}+\hat{S}_{y j}\hat{S}_{z i})\}, \quad (33) \] 

where  \(  B_{ij} = -2(b_{ij} - a_{ij}) = -3b_{ij}  \)  for the Hamiltonian (4). At last, at the further reduction to one spin one gets

 \[ \hat{\rho}_{i j}(t)\approx\frac{1}{d}\{1+\beta A_{0}(t)\hat{S}_{x i(j)}\}. \quad (34) \] 

Having substituted Eq. (34) in Eq. (3), we get  \( F(t) = A_{0}(t) \) .

The density matrix (33) looks like similar expression for isolated pair of the spins, calculated in [10] at small times. Therefore, skipping on intermediate evaluations, we are giving the results at once. By such a way we calculated for the mutual information

 \[ I(\hat{\rho}_{i j})\approx\frac{\beta^{2}}{9\ln2}[S(S+1)B_{i j}A_{l}(t)]^{2}=\frac{\beta^{2}b_{i j}^{2}}{M_{2}^{2}\ln2}[S(S+1)\dot{F}(t)]^{2}. \quad (35) \] 

Under the transformations in process of obtaining the Eq. (35) formulas (28) and (29) were used. We obtain also that the quantum discord  \( D_{ij} \)  (if S=1/2) and the quantum part of correlations  \( Q_{ij} \)
 

(if S > 1/2) are related to the mutual information  \( I(\hat{\rho}_{ij}) \)  from Eq. (35) by the same relations (20) and (25), as in the previous example:

 \[ C_{ij}=D_{ij}=I(\hat{\rho}_{ij})/2,\quad Q_{ij}\approx I(\hat{\rho}_{ij})/(S+1). \] 

On the basis of the results derived above it can be concluded that the time dependence of the mutual information (35) and the quantum part of correlations is revealing through the derivative of FID shape. Thus rapid exhaustion of pair correlations and reduction of their peak values with the growing up of the number of neighbors V generally speaking do not mean impairment of correlated relations of spins, but mean redistribution of pair correlations to more complicated multispin ones. As a measure of total correlation the total information [3, 16] can serve:

 \[ T(\hat{\rho})=\sum_{i}S_{N}(\hat{\rho}_{i})-S_{N}(\hat{\varrho})\approx\frac{\beta^{2}}{3\ln2}S(S+1)[1-A_{0}^{2}(t)]. \quad (36) \] 

At the initial moment of time  \( A_{0}^{2}(0)=1 \)  and  \( T(\hat{\rho})=0 \) . For a long times  \( A_{0}^{2}(t) \)  is coming to zero and therefore  \( T(\hat{\rho}) \)  reaches own limiting value only defined by entry conditions: e.g. by polarization  \( \beta \)  at given temperature and at the fixed strength of the external magnetic field.

## V. Conclusion

Our results mean that in spite of coincidence [5] of the FID shapes both of classical and quantum spin systems for a large number V of nearest neighbors, the quantum properties of the system are not lost. For every pair of spins the portion of quantum correlations changes from 1/2 to  \( 1/(S+1) \)  with S growing up. In reality the quantum properties disappear completely only if  \( S \to \infty \)  but not in the case when  \( V \to \infty \) . The similarity of the FID shapes means that measurable classical correlations and "immeasurable" (lost at measurement) quantum correlations are bringing the equal influence at FID. So it implies that unobservable simultaneously spin components  \( \hat{S}_{x}, \hat{S}_{y}, \hat{S}_{z} \)  are capable to give the contribution to dynamics of spins simultaneously. Thereof the time scale dependence is determined by the quantity  \( S(S+1) \) , instead of  \( S^{2} \) , where S is the maximal value of an observable projection upon any axis.
 

## REFERENCES

[1] A. Abraham and M. Goldman, “Nuclear Magnetism: order and disorder”, Oxford, Univ. Press, (1982).

[2] J. A. Jones, Quantum Computing with NMR, Prog. NMR Specrosc. 59, 91 (2011).

[3] K. Modi, A. Brodutch, H. Cable, T. Paterek, and V. Vedral, Rev. Mod. Phys. 84, 1655 (2012).

[4] S. J. Knak Jensen and O. Platz, Phys. Rev. B 7, 31 (1973).

[5] A. A. Lundin and V. E. Zobov, J. Magnet. Reson. 26. 229 (1977).

[6] I. J. Lowe and R. E. Norberg, Phys. Rev. 107, 46 (1957).

[7] E. B. Fel'dman and A. I. Zenchuk, Phys. Rev. A 86, 012303 (2012).

[8] E. B. Fel'dman and A. I. Zenchuk, Quantum. Inf. Process. 13, 201 (2014).

[9] E. B. Fel'dman, E. I. Kuznetsova, and M. A. Yurishchev, J. Phys. A: Math. Theor. 45, 475304 (2012).

[10] V. E. Zobov, Teor. Math. Phys, 177, 1377 (2013).

[11] J. Preskill, Quantum Information and Computation. Lecture notes for physics 229, California Institute of Technology, (1998).

[12] F. T. Arrechi, E. Courtens, R. Gilmore, and H. Thomas, Phys. Rev. A 6, 2211 (1972).

[13] F. Lado and J. D. Memory, G. W. Parker, Phys. Rev. B, 4, 1406 (1971).

[14] M. H. Lee, Phys. Rev. Lett., 52, 1579 (1984).

[15] V. E. Zobov and A. A. Lundin, JETP, 103, 904 (2006).

[16] B. Groisman, S. Popescu, and A. Winter, Phys. Rev. A 72, 032317 (2005).
 
