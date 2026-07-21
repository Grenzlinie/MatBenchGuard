# Zero-phonon line: Effect of quadratic electron-phonon coupling

V. Hizhnyakov *

Institute of Physics, University of Tartu, Riia 142, 51014 Tartu, Estonia

---

## ARTICLE INFO

**Article history:**
Received 19 March 2010
In final form 7 May 2010
Available online 12 May 2010

## ABSTRACT

The recently proposed theory of vibronic transitions in impurity centres of solids [10] is applied to zero-phonon lines in optical spectra. New equations for the relative intensity, position and width of the line are derived, which take into account both the linear and the quadratic electron-phonon couplings. The joint effect of these couplings on the line intensity is found to be different for absorption and luminescence.

© 2010 Published by Elsevier B.V.

---

## 1. Introduction

An important feature of the phonon-assisted processes in impurity centres of solids at low temperatures is the existence of well-distinguishing zero-phonon transitions. These transitions determine quantum diffusion, coherent hopping of polarons and excitons, and they lead to the appearance of the zero-phonon lines (ZPLs) in optical spectra. These lines have a small width and a large peak intensity, allowing for a number of applications of solid state spectroscopy (see, e.g. [1-4]).

Despite the quite long history of the problem, some important questions of the theory of ZPL have remained unanswered. In the so-called basic model [1], which takes into account only the linear vibronic coupling in harmonic approximation, ZPL has the natural line-width, temperature independent position and the temperature-dependent intensity. In reality, however, the natural line-width is observed only at very low temperatures. The increasing of temperature results in a fast broadening and a shift of the line. To remove the discrepancy one needs to include into consideration the nonlinear, above all, the quadratic vibronic coupling. However, this coupling leads to the mixing of phonons at the transition, which strongly complicates the problem.

In the case of a weak quadratic coupling the cumulant expansion of the Fourier transform of the spectrum can be used [5,6]. If this is not the case, then the method is inefficient due to a fast growth of the number of contributing terms with the amplification of the coupling [7,8]. An exception is the large time limit of the Fourier transform, when for purely quadratic coupling all cumulants can be summed up [9]. This allows to describe the temperature shift and the broadening of ZPL caused by this coupling. However, the joint effect of the linear and quadratic coupling remains obscure.

In [10], we proposed a new method of calculating vibronic transitions based on the Stratonovich identity which works for arbitrary linear and quadratic coupling. Some results of calculations of the model spectra using this model are given in [11-13]. Below we apply this method for the analytical description of ZPL.

## 2. General

We consider the vibronic transitions between the non-degenerate electronic states of an impurity centre in solids. We start the consideration with the Lax equation [13] for the Fourier transform of the spectral function

$$
F(t)=\left\langle e^{i t(H+V)} e^{-i t H}\right\rangle, \tag{1}
$$

where $\langle\cdots\rangle$ denotes the statistical averaging, $H=\sum_{j} \omega_{j}\left(\hat{a}_{j}^{+} \hat{a}_{j}+1 / 2\right)$ is the phonon Hamiltonian in the initial state, $\hbar=1$, $\hat{a}_{j}^{+}$and $\hat{a}_{j}$ are the creation and the destruction operators of the phonon of the frequency $\omega_{j}$, $V=(a q)+(q b q) / 2$ stands for the linear and quadratic vibronic coupling, $q=\sum_{j} e_{j} x_{j}$ is the vector of configurational coordinates, $e_{j}$ is the polarization vector of the phonon $j$, $x_{j}=\left(\hat{a}_{j}^{+}+\hat{a}_{j}\right) /\left(2 \omega_{j}\right)^{1 / 2}$ is the normal coordinate in the initial state, $a$ and $b$ are the parameters of the linear and quadratic coupling, respectively. The values of these parameters are determined by the strength of the electron-phonon interaction and by the change of the electronic wave function at the electronic transition. The method of calculation of these parameters has been developed in Ref. [14]. The results of the numerical calculation of these parameters in concrete systems, see, e.g. in [15,16] (linear coupling) and [17] (quadratic coupling).

A remarkable quadratic coupling is usually associated with the transitions between well-localized s- p-, and (sometimes) d-electronic states. For all these transitions, as a rule, several configurational coordinates give a contribution. The coordinates, which belong to different representations of the point group or to the different rows of the same representation, may be considered independently. Therefore, only few configurational coordinates belonging to the same representation and the same row of it have to be considered simultaneously. In the centres of a small size and high symmetry all these belong to different representations

---

* Fax: +372 7 383033.
E-mail addresses: hizh@fi.tartu.ee, hizh@eeter.fi.tartu.ee

0009-2614/$ - see front matter © 2010 Published by Elsevier B.V.
doi:10.1016/j.cplett.2010.05.017

or to different rows of the same representation and, consequently, can be considered independently. Therefore, in theses centers the model with a single parameter $a$ for the linear coupling and another one $b$ for the quadratic coupling can be used.

First we consider the latter case. We apply the Dyson formula (see [18])
$$
\exp (i t(H+V))=\widehat{T} \exp \left(i \int_{0}^{t} d t^{\prime} V\left(t^{\prime}\right)\right) \quad \exp (i t H),
$$
where $\widehat{T}$ is the time-ordering operator. Presenting the integral as the sum and the exponent of the sum as the product of the exponents, we get
$$
F(t) \simeq\left\langle\widehat{T} \prod_{n=1}^{N} e^{i t a q\left(t_{n}\right) / N} e^{i t b q^{2}\left(t_{n}\right) / 2 N}\right\rangle, \quad N \rightarrow \infty,\qquad(2)
$$
where $t_{n}=t n / N$. We apply now the Stratonovich identity [19]
$$
e^{x^{2} / 2}=(2 \pi)^{-1 / 2} \int_{-\infty}^{\infty} e^{-u^{2} / 2} e^{x u} d u,
$$
and take $x=(i t b / N)^{1 / 2} q(t_{n})$. We get
$$
F(t)=\left(\prod_{n}(2 \pi)^{-1 / 2} \int_{-\infty}^{\infty} e^{-u_{n}^{2} / 2} d u_{n}\right)\left\langle\widehat{T} \exp \left[\sum_{n} \sqrt{i t b / N} u_{n}^{\prime} q\left(t_{n}\right)\right]\right\rangle,\qquad(3)
$$
where $u_{n}^{\prime}=u_{n}+a \sqrt{i t / b N}$. An application of the Bloch-DeDominicis theorem to the last factor gives $\exp [(t b / 2 N) \sum_{n n^{\prime}} D_{n n^{\prime}} u_{n}^{\prime} u_{n^{\prime}}]$ , where $D_{n n^{\prime}} \equiv D(t_{n}-t_{n^{\prime}})=i\langle\widehat{T} q(t_{n}) q(t_{n^{\prime}})\rangle$ is the causal pair-correlation function (note that $D(t)=D(|t|)$ ). Consequently, $F(t)$ is reduced to the multidimensional Gaussian integral. Taking this integral we get [10]
$$
F(t)=\exp \left[g_{Q}(t)+g_{L}(t)\right],\qquad(4)
$$
where
$$
g_{L}(t)=\frac{i a^{2} t^{2}}{2 N^{2}} \sum_{n n^{\prime}}(D /(1-t b D / N))_{n n^{\prime}},\qquad(5)
$$
and
$$
g_{Q}(t)=-(1 / 2) \ln |I-t b D(t) / N|\qquad(6)
$$
describe the contributions of the renormalized linear and purely quadratic vibronic couplings to $\ln F(t)$, respectively, $|\cdots|$ denotes the determinant of the matrix.

## 3. Large time limit; diagonalization of matrix $D$

We take now into account that ZPL is the narrowest line in the spectrum. Therefore, to determine its characteristics it is sufficient to find the large time $t$ limits of $g_{L}(t)$ and $g_{Q}(t)$ [4,5]. To this end one can make a use of the fundamental physical property – the decay of correlations in time. In our case this means that the matrix elements $D_{n n^{\prime}}$ became very small for large $t|n-n^{\prime}| / N$ and they can be neglected. Therefore, in this limit $D_{n n^{\prime}}$ became analogous to the dynamical matrix of a long monatomic chain. Consequently, as in case of the chain the eigenvectors of $D$ become the plain waves
$$
S_{k n}=\left(2 N_{0}\right)^{-1 / 2} e^{i \pi(k+1 / 2) n / N_{0}},\qquad(7)
$$
where $k=-N_{0},-N_{0}+1, \ldots N_{0}-1$ (we take $N=2 N_{0}$ ); the eigenvalues of $D$ equal
$$
\mathfrak{D}_{k}=\sum_{m=-2 N_{0}+1}^{2 N_{0}-1} e^{i \pi(k+1 / 2) m / N_{0}} D\left(|m| / 2 N_{0}\right).\qquad(8)
$$

The sum over $m$ can be replaced by the integral over $\tau=m t / 2 N_{0}$. This gives $\mathfrak{D}_{k}=2 N_{0} D_{k} / t$ with
$$
D_{k}=2 \int_{0}^{t} \cos \left(\omega_{k} \tau\right) D(\tau) d \tau,\qquad(9)
$$
where $\omega_{k}=\pi(2 k+1) / t$. In the $t \rightarrow \infty$ limit $D_{k}=\mathfrak{D}(\omega_{k})$, where
$$
\mathfrak{D}(\omega)=\int_{-\infty}^{\infty} e^{i \omega t} D(t) d t=G(\omega)+i 2 n(|\omega|) \operatorname{Im} G(\omega),\qquad(10)
$$
$$
G(\omega)=\sum_{j} \frac{e_{j}^{2}}{\omega^{2}-\omega_{j}^{2}-i 0_{+}}\qquad(11)
$$
is the Green's function of phonons, $n(\omega)=1 /(\exp (\omega / k_{B} T)-1)$ is the Bose population factor; $\mathfrak{D}(\omega)=\mathfrak{D}(-\omega)$. The Green's function $G(\omega)$ can be calculated by the lattice dynamics methods (see, e.g. [20]).

## 4. Probability, position and width of ZPL

### 4.1. Renormalized linear coupling

To find the position, width and probability of ZPL one needs to find the linear and the constant terms of the large-time asymptotic of $g_{L}(t)$ and $g_{Q}(t)$ [4–6]. Let us consider first $g_{L}(t)$. We take into account that in the large $t$ limit the elements $\widetilde{D}_{n n^{\prime}}$ of the matrix $\widetilde{D}=D /(1-t b D)$ depend on $|n-n^{\prime}|$ :
$$
\widetilde{D}_{n n^{\prime}}=\sum_{k=-N_{0}}^{N_{0}-1} e^{i \pi(k+1 / 2)\left(n-n^{\prime}\right) / N_{0}} \widetilde{\mathfrak{D}}_{k},\qquad(12)
$$
where $\widetilde{\mathfrak{D}}_{k}=\mathfrak{D}_{k} /(1-b \mathfrak{D}_{k})$. Here the sum over $k$ may be replaced by the integral over $\omega=\pi(2 k+1) / t$. Inserting the equation, obtained in this way for $\widetilde{D}_{n n^{\prime}}$, into Eq. (5) and replacing the sums over $n$ and $n^{\prime}$ by the integrals over $t_{1}=t n / 2 N_{0}$ and $t_{1}^{\prime}=t n^{\prime} / 2 N_{0}$, we get after the integration
$$
g_{L}(t)=\frac{i a^{2}}{4 \pi} \int_{-\infty}^{\infty} d \omega \widetilde{\mathfrak{D}}(\omega) \omega^{-2}\left(2-e^{i \omega t}-e^{-i \omega t}\right),\qquad(13)
$$
where $\widetilde{\mathfrak{D}}(\omega)=\mathfrak{D}(\omega) /(1-b \mathfrak{D}(\omega))$. This is the even function of $\omega$. Therefore, the second-order pole at $\omega=0$ works only for $\propto \exp ( \pm i \omega t)$ terms; thereat it should be infinitesimally shifted in the complex plane up (for the term $\propto \exp (i \omega t)$ ) or down (for the term $\propto \exp (-i \omega t))$ to avoid the divergence in the $t \rightarrow \infty$ limit. We get in this limit $g_{L}(t)=-i \delta_{L} t-S_{L}$, where $\delta_{L}$ and $S_{L}$ are real:
$$
\delta_{L}=\left(a^{2} / 2 \pi\right) \operatorname{Re} \widetilde{\mathfrak{D}}(0)\qquad(14)
$$
describes the Stokes losses in the absorption and
$$
S_{L}=\left(a^{2} / \pi\right) \int_{0}^{\infty} \omega^{-2} \operatorname{Im} \widetilde{\mathfrak{D}}(\omega) d \omega,\qquad(15)
$$
is the Hung-Rhys factor renormalized due to the quadratic coupling.

We take now into account that $G(\omega)[1-b G(\omega)]^{-1}=G_{1}(\omega)$ is the causal Green's function of phonons in the final electronic state [9,20] (it is given by Eq. (11), but with $\omega_{1 i}$ and $e_{1 i}$ instead of $\omega_{j}$ and $e_{j}$, respectively, where the subscript $i$ stands for the phonons in the excited state, $e_{1 i}$ is the polarization vector of the phonon $i$ ). Consequently $\widetilde{\mathfrak{D}}(0)=G_{1}(0)$ and $\delta_{L}$ gets the form
$$
\delta_{L}=\frac{1}{2 \pi} a^{2} G_{1}(0)=\sum_{i} \frac{e_{1 i}^{2}}{\omega_{1 i}^{2}}.\qquad(16)
$$

As it should be, only the phonons in the final state contribute to $\delta_{L}$. Analogously in the $T=0$ limit
$$
S_{L}=\frac{1}{2} a^{2} \sum_{i} e_{1 i}^{2} \omega_{1 i}^{-3},\qquad(17)
$$
i.e. in the $T=0$ limit only phonons in the final state contribute to $S_{L}$. However, if $T>0$ then both the phonons of the initial and final states give a contribution to $S_{L}$ as it is reflected in Eq. (15).

### 4.2. Purely quadratic coupling

In the diagonal representation of the $D$-matrix the term$g_Q(t)$ gets the form

$$
g_{Q}(t)=-\sum_{k=0}^{N_{0}-1} \ln \left(1-b D_{k}\right), \quad N_{0} \rightarrow \infty,
\tag{18}
$$

were $D_k$ is given by Eq. (9). To calculate this sum we apply the Abel and Plane formula

$$
\sum_{k=0}^{\infty} f(k)=\frac{1}{2} f(0)+\int_{0}^{\infty} f(k) d k+i \int_{0}^{\infty} \frac{f(i k)-f(-i k)}{e^{2 \pi k}-1} d k.
\tag{19}
$$

In our case $f(k)=\ln \left(1-2 b \int_{0}^{t} \cos (\pi(2 k+1) \tau / t) D(\tau) d \tau\right)$. We replace $k$ in the first integral by $\omega=\pi(2 k+1) / t$. The substitution of the lowest integration limit $\pi / t$ by $0$ is compensated by the constant term $f(0)/2$. The contribution of both these terms then equals $(i\delta_Q-\gamma)t+O(D(t))$, where $O(D(t))$ is the $\propto D(t)$ term which tends to zero if $t\rightarrow\infty$,

$$
\gamma-i \delta_{Q}=(1 / 2 \pi) \int_{0}^{\infty} \ln (1-b \mathfrak{D}(\omega)) d \omega.
\tag{20}
$$

This is the Levenson equation [9] for the temperature broadening and the shift of ZPL.

The second integral in Eq. (19) in the $t\rightarrow\infty$ limit tends to zero. Consequently, Eq. (18) describes only the largest term in the $t\rightarrow\infty$ limit. To find the next large (constant) term describing the contribution $(S_Q)$ of the purely quadratic coupling to the Huang-Rhys factor one needs to apply Eq. (6). This will be done elsewhere. Note that usually $S_Q$ is small. E.g. in the case of a single mode and $T=0$ it equals $\ln ((\omega_0+\omega_1)/2\sqrt{\omega_0\omega_1})$, where $\omega_0$ and $\omega_1=(\omega_0^2-b)^{1/2}$ are the frequencies of the mode in the initial and final states, respectively. If the elastic constant is changed twice ($b=\omega_0^2$ or $b=-\omega_0^2/2$) then $S_Q=0.059$.

### 5. Multiple configurational coordinates

Let us take now into account the contribution of several configurational coordinates to the vibronic coupling. In this case the linear coupling parameter $a$ becomes a vector with a finite (usually small) number $m$ of the components $a_v$, while the quadratic vibronic coupling parameter $b$ becomes the matrix of the rank $m$ with the elements $b_{vv'}$. Correspondingly, the function $D(t)$ becomes also the matrix with the elements $D_{vv'}(t)$. These elements can be found by means of the Green's function (11) where instead of $e_j^2$ stands $e_{jv}e_{jv'}$. This matrix-function can be calculated by the standard methods of the lattice dynamics [20].

To find the characteristics of ZPL in this case one can take into account that in the large $t$ limit the new $D$-matrix becomes analogous to the dynamical matrix of a long multiatiomic chain. Then the plane wave basis (7) can be used for the partial diagonalization of this matrix. As a result, instead of the eigenvalues $D_k$, we will get the matrixes with the elements $D_{k,vv'}$. Repeating the above-presented consideration, one finds that the above-derived equations hold for the characteristics of ZPL also in this case, but with the matrix-function $\mathfrak{D}_{vv'}(\omega)$ instead of the function $\mathfrak{D}(\omega)$. The answers read

$$
\delta_{L}=\left(a^{2} / 2 \pi\right) \sum_{v v^{\prime}} \operatorname{Re} \widetilde{\mathfrak{D}}_{v v^{\prime}}(0),
\tag{21}
$$

$$
S_{L}=\left(a^{2} / \pi\right) \int_{0}^{\infty} \omega^{-2} \sum_{v v^{\prime}} \operatorname{Im} \widetilde{\mathfrak{D}}_{v v^{\prime}}(\omega) d \omega,
\tag{22}
$$

$$
\gamma-i \delta_{Q}=(1 / 2 \pi) \int_{0}^{\infty} \ln |I-(b \mathfrak{D}(\omega))| d \omega,
\tag{23}
$$

where $\widetilde{\mathfrak{D}}_{vv'}(\omega)=\sum_{v''v'''} \mathfrak{D}_{vv''}(\omega)(1-b\mathfrak{D}(\omega))_{v''v'''}^{-1}$ is the renormalized $\mathfrak{D}_{vv'}(\omega)$ matrix, $|\cdots|$ denotes the determinant of the matrix. Eqs. (21)-(23) give a solution of the problem. One can see that to find the characteristics of ZPL in the case of an arbitrary linear and quadratic coupling of optical electron(s) with several configurational coordinates one must calculate the determinant of the matrix $I-b\mathfrak{D}(\omega)$ and its reciprocal matrix. Entering here the matrix-function $\mathfrak{D}_{vv'}(\omega)$ can be calculated by the methods of lattice dynamics. As it was explained above, these matrixes have usually a small rank.

### 6. Absorption and emission: renormalized Huang-Rhys factors in the Debye-Van Hove model

The position and the width of ZPL in absorption and luminescence spectra are the same [4]. However, if $a\neq0$ and $b\neq0$, then its relative intensity in these spectra is different. Indeed, if the initial state corresponds to the ground state, then Eq. (16) holds for absorption. To get the value of this factor for luminescence one needs to replace $G(\omega)$ by $G_1(\omega)$. Then one gets the same equation but with $\operatorname{Im}\widetilde{\mathfrak{D}}(\omega)|1-bG(\omega)|^2$ instead of $\operatorname{Im}\widetilde{\mathfrak{D}}(\omega)$, which leads to a different value of the factor. Another effect of the quadratic coupling is the weakening of the temperature dependence which stems from the denominator of the function $\widetilde{\mathfrak{D}}(\omega)=\mathfrak{D}(\omega)/(1-b\mathfrak{D}(\omega))$.

To illustrate the effects mentioned we use the Debye-Van Hove model of phonons in the ground state. In this model the density of states (DOS) of contributing to $q$ phonons in the ground state equals $\rho(\omega)=(32/\pi)\omega^4\sqrt{1-\omega^2}$ (the top phonon frequency is taken as the unity). Here the addition factor $\omega^2$ takes into account that $q$ is the difference of the displacements of atoms. In this model the DOS of contributing phonons in the excited state equals $\rho_1(\omega)=\rho(\omega)/|1-bG(\omega)|^2$, where $\operatorname{Im}G(\omega)=(\pi/2\omega)\rho(\omega)$, $\operatorname{Re}G(\omega)=-2-8\omega^2+16\omega^4$ (see $\rho_1(\omega)$ for three $b$ values in Fig. 1). Note that if $b<b_0=-1/2$ then the final state is dynamically unstable. If $b$ is slightly larger than $b_0$, then a low-frequency peak of the pseudolocal mode appears in $\rho_1(\omega)$. If $b$ is close or even larger than $b_1=1/6$, then a narrow (if $b<b_1$) or discrete peak (if $b>b_1$) appears in $\rho_1(\omega)$ manifesting the existence of the high-frequency pseudolocal or local mode in the final state.

The results of the calculation of the temperature dependence of the Huang-Rhys factors for absorption and luminescence in this model for the same $b$ values as in Fig. 1 are given in Fig. 2. Comparing the $b=0$ and $b\neq0$ cases, one can conclude that the quadratic coupling indeed leads to the weakening of the temperature dependence at higher temperatures and to the distinction of the relative intensities and temperature dependence of ZPLs in absorption and luminescence. Especially strongly this coupling affects (increase) $S_L$

![](./images/811788284597370881_1.jpg)

Fig. 1. DOS of phonons in the excited state for the following values of the vibronic coupling parameter $b$: 0 (0), -0.2 (1); 0.16 (2); in the case $b=0$ it coincides with the DOS of phonons in the ground state. The top phonon frequency is taken as the unity.

![](./images/811788284597370881_2.jpg)

Fig. 2. Temperature dependence of the normalized Huang-Rhys factor $S_L/a^2$ for the same $b$ values as in Fig. 1; solid lines - absorption; dashed lines - luminescence (in case $b=0$ both lines coincide).

in the case when the local phonon dynamics softens at the transition ($b$ is negative). This conclusion is in agreement with the resent result of Ref. [16] where it was found that in the case of $b \approx b_0$ the spectrum has no ZPL; its shape is dominated by the low-frequency phonons and it resembles a triangle. The theory [21] explains the spectrum of the triplet-triplet transition in $\mathrm{Na}_2$ complexes trapped on the surface of a $^4$He droplet.

Finally we note that the presented theory may have a broader range of applicability than only ZPLs in the optical spectra of solids. E.g. it may be applied for the description of the quantum diffusion of vacancies and other defects [22]. The essential features of these processes are (a) a remarkable (in case of vacancies very strong [22]) change (rearrangement) of the atomic bonds at every jump of the defect and (b) an essential contribution of several configurational coordinates in the process. Both of these are taken into account in the presented theory.

Acknowledgment

The research was supported by ETF Grant No. 7741.

References

[1] K. Rebane, Impurity Spectra of Solids, Plenum Press, NewYork, 1970.
[2] O. Sild, K. Haller (Eds.), Zero-phonon Lines and Spectral Hole Burning in Spectroscopy and Photochemistry, Springer-Verlag, Berlin, 1988.
[3] Y. Toyozawa, Optical Processes in Solids, Cambridge University Press, 2003.
[4] I.S. Osad'ko, Selective Spectroscopy of Single Molecules, Springer, Berlin, 2003.
[5] D.E. McCumber, Math. Phys. 5 (1964) 508.
[6] M.A. Krivoglaz, Soc. Phys. Solid State 6 (1964) 1340.
[7] D. Hsu, J.L. Skinner, J. Chem. Phys. 81 (1984) 1604.
[8] D. Hsu, J.L. Skinner, J. Chem. Phys. 83 (1985) 2097.
[9] G.F. Levenson, Phys. Status Solidi B 43 (1971) 739.
[10] V. Hizhnyakov, I. Tehver, Chem. Phys. Lett. 422 (2006) 299.
[11] V. Hizhnyakov, G. Benedek, I. Tehver, V. Boltrushko, J. Non-Cryst. Solids 352 (2006) 2558.
[12] V. Boltrushko, S. Holmar, I. Tehver, V. Hizhnyakov, J. Mol. Struct. 838 (2007) 164.
[13] V. Hizhnyakov, S. Holmar, I. Tehver, J. Lumin. 127 (2007) 7.
[14] V. Dohm, P. Fulde, Zeit. Phys. B 21 (1975) 369.
[15] B.Z. Malkin, O.V. Solovyev, A.Yu. Malishev, S.K. Saikin, J. Lumin. 125 (2007) 175.
[16] M.G. Brik, N.M. Avram, J. Phys. C 21 (2009) 155502.
[17] B.Z. Malkin, S.K. Saikin, Proc. SPIE 2706 (1996) 193.
[18] M. Lax, J. Chem. Phys. 20 (1953) 1752.
[19] R.L. Stratonovich, Dokl. Akad. Nauk SSSR 115 (1957) 1097.
[20] A.A. Maradudin, E.W. Montroll, G.S. Weiss, I.P. Ipatova, in: H. Ehrenreich, F. Seitz, D. Turnbull (Eds.), Theory of Lattice Dynamics in the Harmonic Approximation, second edn., Solid State Physics, Academic Press, New York, 1971 (Suppl. 3).
[21] V. Hizhnyakov, I. Tehver, G. Benedek, Eur. Phys. J. B 70 (4) (2009) 507; V. Hizhnyakov, I. Tehver, G. Benedek, Europhys. News 40 (5) (2009) 9.
[22] V. Hizhnyakov, G. Benedek, Eur. Phys. J. B 43 (4) (2005) 431.