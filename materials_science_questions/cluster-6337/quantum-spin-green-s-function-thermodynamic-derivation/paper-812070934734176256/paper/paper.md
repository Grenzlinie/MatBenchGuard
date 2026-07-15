# Absence of long-range order in an antiferromagnetic chain with long-range interactions: Green's function approach

Ren-Gui Zhu and An-Min Wang*
Department of Modern Physics, University of Science and Technology of China, Hefei, 230026, People's Republic of China

(Received 22 March 2006; revised manuscript received 22 May 2006; published 19 July 2006)

The antiferromagnetic spin-1/2 chain with power-law decaying interactions $|J_n| \propto 1/n^p$ is studied by a Green's function method. The dispersion relation $\omega_k$ and an expression for the critical temperature $T_N$ as a function of $p$ are presented. By analyzing the small-$k$ behavior of $\omega_k$, it is shown that there will be no long-range order at finite temperature when $p \geq 2$, which is in good agreement with Bruno's rigorous proof. Our work refurbishes a previous work also by Green's function method, and validates the Tyablikov decoupling approximation to long-range interactions with $1 < p < 2$.

DOI: 10.1103/PhysRevB.74.012406
PACS number(s): 75.10.Jm, 68.35.Rh

Heisenberg ferro- and antiferromagnetic spin chains with long-range interactions have attracted much attention since an extension of the Mermin-Wagner theorem¹ was given by Bruno.² Through a rigorous proof, Bruno stated in his paper that $D$-dimensional ($D=1$ or 2) Heisenberg and $XY$ systems with long-range interactions monotonically decreasing as $|J_{\mathbf{R}}| \propto R^{-p}$ cannot be ferro- or antiferromagnetic at any finite temperature when $p \geq 2D$, while the original Mermin-Wagner theorem requires $p > 2+D$.

Rigorous results are very important, because they allow us to test the validity of approximate theories. Quantum and classical ferromagnetic chains with power-law decaying interactions have been studied by the Green's function method,³⁴ where the decoupling approximation is inevitably necessary. All these calculations gave results consistent with Bruno's. Subsequently, the spin-wave approximation (SWA) to the antiferromagnetic (AFM) chain⁵ and the coherent-state path integral approach to the $D$-dimensional ferromagnetic $XY$ model⁶ were both validated, namely, gave results in agreement with Bruno's. But in contrast to the SWA,⁵ the Green's function method with Tyablikov decoupling predicted⁷ $p > 1$, inconsistent with Bruno's result,² and the dispersion relation was found⁷ to be quite different from the SWA one.⁵

In this paper, we reconsider the AFM spin-1/2 chain with power-law decaying interactions, also using the Green's function method with Tyablikov decoupling as in Ref. 7, but more accurately, and obtain very different result. However, our result is consistent with Bruno's statement and the SWA prediction. The basic mistake made in Ref. 7 is pointed out before we give a conclusion.

We investigate the following Hamiltonian of the one-dimensional Heisenberg antiferromagnetic model:⁵⁷
$$
H = \sum_{m,n} J_{mn} \boldsymbol{S}_m \cdot \boldsymbol{S}_n \tag{1}
$$
with
$$
J_{mn} = J \frac{(-1)^{m+n-1}}{|m-n|^p} \tag{2}
$$
without double counting of bonds, where $J>0$ for an antiferromagnet. In the following, we will set $J$ to unity, using it as the energy scale. $p$ is the power-law exponent that controls the decay of the interaction. The summation with respect to $m$ and $n$ is taken over the whole lattice.

We study the model using the double-time-temperature Green's function method.⁸⁹ For this purpose, we first divide the Hamiltonian into three terms
$$
H = H_{oe} + H_{oo} + H_{ee} \tag{3}
$$
where the three terms are respectively defined as
$$
H_{oe} = \sum_{i,j} J_{2i-1,2j} \boldsymbol{S}_{2i-1} \cdot \boldsymbol{S}_{2j}, \tag{4}
$$
$$
H_{oo} = \sum_{i,j} J_{2i-1,2j-1} \boldsymbol{S}_{2i-1} \cdot \boldsymbol{S}_{2j-1}, \tag{5}
$$
$$
H_{ee} = \sum_{2i,2j} J_{2i,2j} \boldsymbol{S}_{2i} \cdot \boldsymbol{S}_{2j}. \tag{6}
$$

We make the origin site and all the even sites belong to the up sublattice. Then two retarded Green's function can be introduced:
$$
G_{11}(2i,t) := \langle\langle S_{2i}^+(t); S_0^-\rangle\rangle = -i \theta(t) \langle [S_{2i}^+, S_0^-] \rangle, \tag{7}
$$
$$
G_{12}(2i-1,t) := \langle\langle S_{2i-1}^+(t); S_0^-\rangle\rangle = -i \theta(t) \langle [S_{2i-1}^+, S_0^-] \rangle, \tag{8}
$$
where $S^\pm = S^x \pm i S^y$ are raising ($+$) and lowering ($-$) operators. The Fourier components of the Green's functions obey the equations of motion
$$
\omega G_{11}(2i,\omega) = \frac{1}{2\pi} \langle [S_{2i}^+, S_0^-] \rangle + \langle\langle [S_{2i}^+, H] ; S_0^- \rangle\rangle, \tag{9}
$$
$$
\omega G_{12}(2i-1,\omega) = \frac{1}{2\pi} \langle [S_{2i-1}^+, S_0^-] \rangle + \langle\langle [S_{2i-1}^+, H] ; S_0^- \rangle\rangle.
\tag{10}
$$

To calculate the commutators $[S_{2i}^+, H]$ and $[S_{2i-1}^+, H]$, it will be very convenient to write $\boldsymbol{S}_m \cdot \boldsymbol{S}_n$ as $S_m^z S_n^z + \frac{1}{2}(S_m^+ S_n^- + S_m^- S_n^+)$. Then using the commutation relations $[S_i^\pm, S_j^z] = \mp S_i^\pm \delta_{ij}$ and $[S_i^\pm, S_j^\mp] = 2 S_i^z \delta_{ij}$, and with the help of the Hamiltonian separation (3), we rewrite the equations of motion as

$$
\begin{aligned}
\omega G_{11}(2 i, \omega)= & \frac{\left\langle S_{0}^{z}\right\rangle}{\pi} \delta_{i 0}+\sum_{j} J_{2 j-1,2 i}\left(\left\langle\left\langle S_{2 j-1}^{+} S_{2 i}^{z} ; S_{0}^{-}\right\rangle\right\rangle\right. \\
& \left.-\left\langle\left\langle S_{2 j-1}^{z} S_{2 i}^{+} ; S_{0}^{-}\right\rangle\right\rangle\right)+2 \sum_{j} J_{2 j, 2 i}\left(\left\langle\left\langle S_{2 i}^{z} S_{2 j}^{+} ; S_{0}^{-}\right\rangle\right\rangle\right. \\
& \left.-\left\langle\left\langle S_{2 i}^{+} S_{2 j}^{z} ; S_{0}^{-}\right\rangle\right\rangle\right),
\end{aligned}
$$

$$
\begin{aligned}
\omega G_{12}(2 i-1, \omega)= & \sum_{j} J_{2 i-1,2 j}\left(\left\langle\left\langle S_{2 i-1}^{z} S_{2 j}^{+} ; S_{0}^{-}\right\rangle\right\rangle-\left\langle\left\langle S_{2 i-1}^{+} S_{2 j}^{z} ; S_{0}^{-}\right\rangle\right\rangle\right) \\
& +2 \sum_{j} J_{2 i-1,2 j-1}\left(\left\langle\left\langle S_{2 j-1}^{+} S_{2 i-1}^{z} ; S_{0}^{-}\right\rangle\right\rangle\right. \\
& \left.-\left\langle\left\langle S_{2 j-1}^{z} S_{2 i-1}^{+} ; S_{0}^{-}\right\rangle\right\rangle\right).
\end{aligned}
$$

In order to solve the two equations, we must break the chain of Green's functions. Here we consider the simplest decoupling scheme, Tyablikov decoupling: $^{9}\left\langle\left\langle S_{i}^{+} S_{m}^{z} ; S_{n}^{-}\right\rangle\right\rangle$ $\sim\left\langle S_{m}^{z}\right\rangle\left\langle\left\langle S_{i}^{+} ; S_{n}^{-}\right\rangle\right\rangle$. To project the equations into wave vector space, we introduce the Fourier transforms as follows:

$$
G_{11}(2 n, \omega)=\frac{1}{N} \sum_{k} G_{11}(k, \omega) \exp (i 2 n k), \quad(13)
$$

$$
G_{12}(2 n-1, \omega)=\frac{1}{N} \sum_{k} G_{12}(k, \omega) \exp [i(2 n-1) k], \quad(14)
$$

$$
J_{2 m, 2 n}=J_{2 m-1,2 n-1}=\frac{1}{N} \sum_{k} J_{11}(k) \exp [i 2(m-n) k], \quad(15)
$$

$$
J_{2 m, 2 n-1}=\frac{1}{N} \sum_{k} J_{12}(k) \exp \{i[2(m-n)+1] k\}, \quad(16)
$$

where, $N$ is half the total number of sites, and the summation with respect to $k$ is taken over the first Brillouin Zone of sublattice. In this way, we finally find the Green's function $G_{11}(k, \omega)$,

$$
G_{11}(k, \omega)=\frac{\sigma_{a}}{2 \pi \omega_{k}}\left(\frac{\omega_{k}-\sigma_{a}\left(\alpha-f_{k}\right)}{\omega+\omega_{k}}+\frac{\omega_{k}+\sigma_{a}\left(\alpha-f_{k}\right)}{\omega-\omega_{k}}\right)
$$

where $\sigma_{a}=\left\langle S_{0}^{z}\right\rangle=\left\langle S_{2 i}^{z}\right\rangle=-\left\langle S_{2 j-1}^{z}\right\rangle$, and for convenience, we have defined two functions:

$$
f_{k}:=2\left[J_{11}(0)-J_{11}(k)\right]=4 \sum_{n=1}^{\infty} \frac{1}{(2 n)^{p}}(\cos 2 n k-1), \quad(18)
$$

$$
g_{k}:=J_{12}(k)=2 \sum_{n=1}^{\infty} \frac{1}{(2 n-1)^{p}} \cos (2 n-1) k, \quad(19)
$$

and $\alpha:=J_{12}(0)=2 \sum_{n=1}^{\infty} 1 /(2 n-1)^{p}$. The dispersion relation is just the pole of the Green's functions:

$$
\omega_{k}=\sigma_{a} \sqrt{\left(\alpha-f_{k}\right)^{2}-g_{k}^{2}} .
$$

Thus we have got the same dispersion relation as Ref. 5. We will subsequently give an expression of the critical temperature $T_{N}$ as a function of the power-law parameter $p$. For this purpose, we express the spin correlation function on the same site as follows, with the help of the spectrum density theorem: $^{10}$

$$
\begin{aligned}
\left\langle S_{0}^{-} S_{0}^{+}\right\rangle & =-\frac{2}{N} \lim _{\epsilon \rightarrow 0} \sum_{k} \int_{-\infty}^{\infty} \frac{\operatorname{Im} G_{11}(k, \omega+i \epsilon)}{e^{\beta \omega}-1} d \omega \\
& =\frac{\sigma_{a}}{N} \sum_{k}\left(\frac{\sigma_{a}\left(\alpha-f_{k}\right)}{\omega_{k}} \operatorname{coth} \frac{\beta \omega_{k}}{2}-1\right) .
\end{aligned}
$$

For spin $1 / 2, \sigma_{a}=1 / 2-\left\langle S_{0}^{-} S_{0}^{+}\right\rangle$, so we get the equation for $\sigma_{a}$,

$$
\frac{1}{2}=\frac{\sigma_{a}}{N} \sum_{k} \frac{\alpha-f_{k}}{\sqrt{\left(\alpha-f_{k}\right)^{2}-g_{k}^{2}}} \operatorname{coth} \frac{\beta \omega_{k}}{2} .
$$

The inverse of the critical temperature is obtained from $\sigma_{a}$ $\rightarrow 0$,

$$
T_{N}^{-1}=\frac{4 k_{B}}{N} \sum_{k} \frac{\alpha-f_{k}}{\left(\alpha-f_{k}\right)^{2}-g_{k}^{2}}=\frac{2 k_{B}}{\pi} \int_{-\pi}^{\pi} \frac{\alpha-f_{k}}{\left(\alpha-f_{k}\right)^{2}-g_{k}^{2}} d k
$$

which is quite different from the expression in Ref. 7.

For a given $p$, if $T_{N}$ has a finite value, there will exist long-range order (LRO) for $T<T_{N}$ (namely, the system will be antiferromagnetic). If $T_{N}$ is zero, then there will not exist LRO at any finite temperature. We can judge the convergence or divergence of $T_{N}^{-1}$ by studying the small-$k$ behavior of the dispersion relation, which has been discussed in great detail by Yusuf et al. in Ref. 5 using the analytical properties of the Bose-Einstein integral function. Because we have got the same dispersion relation as theirs, it is certain that we can obtain the same small-$k$ behavior. So we just directly present the result here. For small $k$ and $1<p<3$, we have $\omega_{k}$ $\propto k^{(p-1) / 2}$. The inverse of the critical temperature is

$$
T_{N}^{-1} \propto \int_{-\pi}^{\pi} \frac{d k}{k^{p-1}}
$$

which will converge when $1<p<2$ and diverge when $2 \leqslant p<3$. Furthermore, we have $\omega_{k} \propto k$ for all values of $p>3$ and $\omega_{k} \propto k \sqrt{|\ln (k)|}$ for $p=3$, which all lead to divergence of $T_{N}^{-1}$. So we can conclude that the Green's function method predicts that $T_{N}^{-1}$ diverges for all values of $p \geqslant 2$.

Now, before we give a conclusion, we would like to point out the basic mistake made in Ref. 7. The distinct difference first emerges in the motion equations of the Green's functions. Comparing our results (11) and (12) with the results (8) and (9) in Ref. 7, we can see that the authors of Ref. 7 did not separate the Hamiltonian as we do. In fact, we think that they mistakenly only considered the part of the Hamiltonian $H_{o e}$, which is equivalent to confining the sites denoted by $i$ to the up sublattice and the ones denoted by $j$ to the down sublattice. So they left out the interactions in the same sublattice, and got formulas very like ones in the situation of first-nearest-neighbor interactions, except for the form of $J_{k}$. Their results can only be applied to the situation that the

power-law decaying interactions are confined between two different sublattices, and there is no interaction in the same sublattice.

In summary, we have studied the antiferromagnetic spin-1/2 chain with power-law decaying interactions, using the Green's function method with Tyablikov decoupling. Our work refurbishes a previous work⁷ dealing with the same model and using the same method. Our results show that the Green's function method also rules out LRO when $p \geqslant 2$, which is consistent with the SWA prediction⁵ and Bruno's extension² of the Mermin-Wagner theorem. So our results validate the Green's function method in dealing with antiferromagnetic chains with long-range interactions.

We are grateful to Feng Xu, Xiaosan Ma, Ningbo Zhao, Xiaoqiang Su, and Ya Cao for helpful discussions. This work was funded by the National Fundamental Research Program of China with Grant No. 2001CB309310 and partially supported by the National Natural Science Foundation of China under Grant No. 60573008.

*Electronic address: anmwang@ustc.edu.cn

¹N. D. Mermin and H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
²P. Bruno, Phys. Rev. Lett. 87, 137203 (2001).
³M. Hamedoun, Y. Cherriet, A. Hourmatallah, and N. Benzakour, Phys. Rev. B 63, 172402 (2001).
⁴A. Cavallo, F. Cosenza, and L. De Cesare, Phys. Rev. B 66, 174439 (2002).
⁵Eddy Yusuf, Anuvrat Joshi, and Kun Yang, Phys. Rev. B 69, 144412 (2004).

⁶J. R. De Sousa, Eur. Phys. J. B 43, 93 (2005).
⁷J. T. M. Pacobahyba, W. Nunes, and J. R. De Sousa, Phys. Rev. B 69, 092410 (2004).
⁸N. Majlis, *The Quantum Theory of Magnetism* (World Scientific, Singapore, 2000).
⁹N. N. Bogolyubov and S. V. Tyablikov, Sov. Phys. Dokl. 4, 604 (1959).
¹⁰S. V. Tyablikov, *Methods in the Quantum Theory of Magnetism* (Plenum, New York, 1967), Sec. 26.