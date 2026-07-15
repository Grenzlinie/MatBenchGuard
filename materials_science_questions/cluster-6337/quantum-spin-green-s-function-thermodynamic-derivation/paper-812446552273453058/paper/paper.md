# ISING CORRELATIONS AT THE CRITICAL TEMPERATURE

Helen AU-YANG and Jacques H.H. PERK
Institute for Theoretical Physics, State University of New York, Stony Brook, NY 11794-3840, USA

Received 22 May 1984
Revised manuscript received 25 June 1984

We demonstrate how the quadratic difference equations of Hirota's Toda lattice form, recently derived for the planar Ising model, provide a particularly easy way to obtain pair correlation functions at the critical temperature. The new results are also relevant for the dimer problem.

The early work on critical correlations in the two-dimensional Ising model [1-3] requires calculating determinants whose sizes increase with the distances between spins. Then, it was discovered that the two-point correlation function, in the scaling limit towards $T_{\mathrm{c}}$, satisfies the Painlevé III ordinary second-order differential equation [4]. This was generalized to nonlinear partial differential equations for $n$-point functions in the scaling limit [5] and partial difference equations for the general case [6-8], see also ref. [9] for more details.

In this letter, we shall present a few new results for the two-point function at $T_{\mathrm{c}}, C(M, N) \equiv\left\langle\sigma_{00} \sigma_{M N}\right\rangle$. We shall start from the known results for the diagonal correlation $C(M, M)$ [1] and from the recently derived quadratic difference equation [7], relating $C(M, N)$ with $C(M \pm 1, N)$ and $C(M, N \pm 1)$. We shall give a new result for the next-to-the-diagonal correlation function $C(M, M \pm 1)$. This enables us to determine all other spin correlations iteratively, thus simplifying the cumbersome task of calculating increasingly larger determinants. In fact, this simplification is immediately understood, viewing the difference equation as a compound pfaffian theorem [7-9]. Finally, this equation, which is the discrete (imaginary) time Toda equation of Hirota [10] with a source term in the origin, enables us to obtain a hitherto unknown asymptotic expansion of $C(M, N)$ for large $M$ and $N$. This expansion gives astonishingly accurate results already for small values of $M$ and $N$, so it is relatively straightforward to compute the wave-vector dependent susceptibility at criticality. This, together with further details, will be presented elsewhere.

We start from the result [1]
$$C(0,0)=1,$$
$$\frac{C(M, M)}{C(M-1, M-1)}=\frac{\Gamma(M)^{2}}{\Gamma\left(M-\frac{1}{2}\right) \Gamma\left(M+\frac{1}{2}\right)}, \quad M \geqslant 1, \quad(1)$$
and the difference equation [7]
$$\begin{aligned}
& \sinh \left(2 H_{\mathrm{c}}\right)\left[C(M, N-1) C(M, N+1)-C(M, N)^{2}\right] \\
& \quad+\sinh \left(2 V_{\mathrm{c}}\right)\left[C(M-1, N) C(M+1, N)-C(M, N)^{2}\right] \\
& \quad=0, \quad \text { for }(M, N) \neq(0,0), \quad(2)
\end{aligned}$$
$$C(1,0)=\cosh \left(2 H_{\mathrm{c}}\right)-\sinh \left(2 H_{\mathrm{c}}\right) C(0,1). \quad(3)$$

Here $\sinh (2 H_{\mathrm{c}}) \sinh (2 V_{\mathrm{c}})=1$ and $H_{\mathrm{c}} k_{\mathrm{B}} T_{\mathrm{c}}\left(V_{\mathrm{c}} k_{\mathrm{B}} T_{\mathrm{c}}\right)$ is the coupling between the horizontal (vertical) nearest-neighbour pairs. Note that the result (1) holds independently of the anisotropy $\left(H_{\mathrm{c}} \neq V_{\mathrm{c}}\right)$.

We have derived the new result
$$\begin{aligned}
& C(M, M+1)=C(M+1, M+1) \cosh \left(2 H_{\mathrm{c}}\right) \\
& \quad × F\left(\frac{1}{2}, M+1 ; M+\frac{3}{2} ;-\sinh ^{2}\left(2 H_{\mathrm{c}}\right)\right),
\end{aligned}\qquad(4)$$
where $F(a, b ; c ; x)$ is the hypergeometric function, which here, for small values of $M$, can also be reexpressed in terms of $\sinh (2 H_{\mathrm{c}})$ and the gudermannian $\operatorname{gd}(2 H_{\mathrm{c}})$.

**Table 1**
$C(M,N)$ for the symmetric case.

<table>
  <thead>
    <tr>
      <th>$M$</th>
      <th>$N=0$</th>
      <th>$N=1$</th>
      <th>$N=2$</th>
      <th>$N=3$</th>
      <th>$N=4$</th>
      <th>$N=5$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>$1/\sqrt{2}$</td>
      <td>$1-4/\pi^{2}$</td>
      <td>$2\sqrt{2}(1-8/\pi^{2})$</td>
      <td>$16(1-112/9\pi^{2}+256/9\pi^{4})$</td>
      <td>$128\sqrt{2}(1-88/9\pi^{2})(1-64/9\pi^{2})$</td>
    </tr>
    <tr>
      <td>1</td>
      <td></td>
      <td>$2/\pi$</td>
      <td>$4\sqrt{2}/\pi^{2}$</td>
      <td>$(8/3\pi)(16/\pi^{2}-1)$</td>
      <td>$(128\sqrt{2}/9\pi^{2})(32/\pi^{2}-3)$</td>
      <td>$(512/5\pi)(1-272/9\pi^{2}+2^{14}/81\pi^{4})$</td>
    </tr>
    <tr>
      <td>2</td>
      <td></td>
      <td></td>
      <td>$16/3\pi^{2}$</td>
      <td>$32\sqrt{2}/9\pi^{2}$</td>
      <td>$(256/15\pi^{2})(1-64/9\pi^{2})$</td>
      <td>$(2048\sqrt{2}/25\pi^{2})(1-256/27\pi^{2})$</td>
    </tr>
    <tr>
      <td>3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>$2048/135\pi^{3}$</td>
      <td>$2^{16}\sqrt{2}/3^{4}\times5^{2}\pi^{4}$</td>
      <td>$(2^{17}/3\times5^{3}\times7\pi^{3})(1024/81\pi^{2}-1)$</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>$2^{20}/3^{3}\times5^{3}\times7\pi^{4}$</td>
      <td>$2^{23}\sqrt{2}/3^{2}\times5^{4}\times7^{2}\pi^{4}$</td>
    </tr>
    <tr>
      <td>5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>$2^{35}/3^{5}\times5^{5}\times7^{3}\pi^{5}$</td>
    </tr>
  </tbody>
</table>

All other correlations can now be obtained iteratively from (1) - (4), which is a Cauchy-type initial value problem. In the symmetric case $H_{\mathrm{c}}=V_{\mathrm{c}}$, with $\sinh(2H_{\mathrm{c}})=1$, $\cosh(2H_{\mathrm{c}})=\sqrt{2}$, we have the reflection symmetries $C(M,N)=C(N,M)=C(M,-N)=C(-M,N)$. Then all correlations can be obtained from (1) - (3) by iteration, eq. (4) being directly implied. We have given the results for $0\leqslant M\leqslant N\leqslant5$ in table 1, which can be extended easily; but the missing values can be computed very accurately also from the following.

One of the sums in ref. [11] can be carried out. Therefore, the asymptotic expansion for the diagonal correlation $C(M,M)$ for large $M$ is

$$
\begin{aligned}
& \ln C(M, M)=\ln A-\frac{1}{4} \ln M \\
& \quad+\sum_{k=2}^{\infty} \frac{\left(2^{2 k}-1\right) B_{2 k}}{k(k-1) 2^{2 k} M^{2(k-1)}},
\end{aligned}
\tag{5}
$$

where
$$
A=2^{1 / 12} \mathrm{e}^{3 \zeta(-1)}=0.645002448 \ldots,
\tag{6}
$$
and $B_{2k}$ are the Bernoulli numbers. We note that the sum in (5) contains only even powers of the distance $M$. Expanding eq. (4) for the symmetric case $H_{\mathrm{c}}=V_{\mathrm{c}}$, we get

$$
\begin{aligned}
& \ln C(M, M+1)=\ln C(M, M) \\
& \quad-\sum_{k=1}^{\infty} \frac{\left(2^{2 k}-1\right)\left(2^{2 k-1}-1\right) B_{2 k}}{2 k(2 k-1)(2 M)^{2 k-1}}.
\end{aligned}
\tag{7}
$$

Notice that this asymptotic expansion also contains odd powers of $M$. However, if we expand $\ln C(M,M+1)$ in the scaled distance
$$
R=\left[\frac{1}{2} M^{2}+\frac{1}{2}(M+1)^{2}\right]^{1 / 2}
\tag{8}
$$
between the two spins, by substituting
$$
M=\left(R^{2}-\frac{1}{4}\right)^{1 / 2}-\frac{1}{2}
\tag{9}
$$
into (5) and (7), we find

$$
\begin{aligned}
& \ln C(M, M+1)=\ln A-\frac{1}{4} \ln R \\
& \quad+\sum_{m=1}^{\infty} \frac{K_{2 m}}{2^{2 m+2} m R^{2 m}},
\end{aligned}
\tag{10}
$$

with
$$
K_{2 m}=\sum_{k=0}^{m}\left(\begin{array}{c}
m \\
k
\end{array}\right)\left[E_{2 k}-B_{2 k+2}\left(2^{2 k+2}-1\right) /(k+1)\right],(11)
$$
where $E_{2k}$ are the Euler numbers. Now we find that odd powers again vanish.

For the general case with $V_{\mathrm{c}} \neq H_{\mathrm{c}}$, we can derive a similar asymptotic expansion. We note thet $C(M,N)$ is the restriction of a function analytic in two variables. We therefore expect that the correlation has a smooth asymptotic behaviour for $M,N\rightarrow\infty$ and that in the Taylor expansions of $C(M\pm z,N)$ and $C(M,N\pm z)$, for $z=1$, the higher terms are increasingly smaller. Keeping only first and second derivatives, the difference equation (2) becomes the Laplace partial differential equation

$$
\begin{aligned}
& \sinh \left(2 H_{\mathrm{c}}\right)\left(\partial^{2} / \partial N^{2}\right) \ln C(M, N) \\
& \quad+\sinh \left(2 V_{\mathrm{c}}\right)\left(\partial^{2} / \partial M^{2}\right) \ln C(M, N)=0.
\end{aligned}
\tag{12}
$$

At $T_{\mathrm{c}}$ the correlation lengths $\xi_{\mathrm{h}}$ and $\xi_{\mathrm{v}}$ in the horizontal and vertical directions are infinite, but their ratio is
$$
\xi_{\mathrm{v}} / \xi_{\mathrm{h}}=\left[\sinh \left(2 V_{\mathrm{c}}\right) / \sinh \left(2 H_{\mathrm{c}}\right)\right]^{1 / 2}=\tan \alpha.
\tag{13}
$$

We scale the coordinates accordingly
$$
\begin{aligned}
& N=x / \cos \alpha=R \cos \theta / \cos \alpha, \\
& M=y / \sin \alpha=R \sin \theta / \sin \alpha
\end{aligned}
\tag{14}
$$
and we arrive at
$$
\left(\partial^{2} / \partial x^{2}+\partial^{2} / \partial y^{2}\right) \ln C(x, y)=0.
\tag{15}
$$

Therefore, the leading order (scaling) solution is
$$C(M, N) \sim A R^{-\eta}, \tag{16}$$
which is rotationally invariant. Here $A$ and $\eta$ are determined by using (5) and (6) as boundary conditions. Correction can be obtained systematically, by successively keeping higher order derivatives in the Taylor expansions of $\ln C(x \pm 1, y)$ and $\ln C(x, y \pm 1)$. We find
$$\begin{aligned}
& \ln C(M, N)=\ln A-\frac{1}{4} \ln R+A_{1}(\theta) R^{-2} \\
& \quad+A_{2}(\theta) R^{-4}+A_{3}(\theta) R^{-6}+\mathrm{O}\left(R^{-8}\right), \tag{17}
\end{aligned}$$
with
$$A_{1}(\theta)=2^{-8}(-1+3 \cos 4 \theta-6 u \cos 2 \theta), \tag{18}$$
$$\begin{aligned}
A_{2}(\theta) & =2^{-13}(5+36 \cos 4 \theta+63 \cos 8 \theta \\
& \left.+18 u \cos 2 \theta-162 u \cos 6 \theta+72 u^{2} \cos 4 \theta\right), \quad(19)
\end{aligned}$$
$$\begin{aligned}
A_{3}(\theta) & =3^{-1} 2^{-19}\left(-524-324 \cos 4 \theta\right. \\
& +24732 \cos 8 \theta+28884 \cos 12 \theta \\
& -1566 u \cos 2 \theta-24003 u \cos 6 \theta \\
& -95679 u \cos 10 \theta-486 u^{2}-3672 u^{2} \cos 4 \theta \\
& \left.+83358 u^{2} \cos 8 \theta-15072 u^{3} \cos 6 \theta\right), \tag{20}
\end{aligned}$$
and
$$u \equiv \cos 2 \alpha. \tag{21}$$

For the correlation along the horizontal $\theta=0$, we find $A_{1}(0)=(1-3 \cos 2 \alpha) / 128$, which is identically the same as given by Wu [12]. For the symmetric case $\cos 2 \alpha=u=0, A_{i}(\theta)$ also agrees with (10). Finally, in the time-continuum limit $u=1$, after Wick rotation, our results match with those of the one-dimensional Ising chain in critical transverse field [13,14], in the space-like regime. There are some differences between this case and ours. We have a nonlinear elliptic boundary value problem for which Dirichlet boundary conditions are natural, but for which the Cauchy problem is extremely sensitive to the detailed initial conditions. Giving the leading decay at infinity and the source in the origin specifies the solution, and the dependence on the source is only exponentially small at infinity. In the hyperbolic case of ref. [13] there is a light-cone phenomenon and the Dirichlet problem is unnatural.

We conclude with a few remarks. Surprisingly, exactly the same hypergeometric function as in eq. (4) appears in Hartwig's solution for the monomer-monomer correlation along the diagonal in the otherwise closest-packed two-dimensional dimer problem on a regular square lattice [15,16]. In fact, we were able to show that the monomer correlation is a product of two Ising correlations at $T_{\mathrm{c}}$, i.e.
$$\begin{aligned}
& \omega(p, q)=\frac{1}{2}\left(x^{2}+y^{2}\right)^{-1 / 2} C\left(\left[\frac{1}{2} p\right],\left[\frac{1}{2} q\right]\right) \\
& \quad × C\left(\left[\frac{1}{2}(p+1)\right],\left[\frac{1}{2}(q+1)\right]\right), \tag{22}
\end{aligned}$$
for $p+q$ odd, [ ] denoting integer part, $y / x=\sinh$ $(2 H_{\mathrm{c}})$, and correcting a few minor mistakes in ref. [16]. Since the monomer-dimer problem is two-dimensional Ising model in a magnetic field [17], we were led to consider the special case of the magnetic field being $\mathrm{i} \pi k T / 2$, introduced by Yang and Lee in their study of the zeros of the partition function [18]. This case reduces to the dimer problem in the infinite-temperature limit. We have obtained factorizations like (22) for the partition function and all $n$-point correlations involving order- and dis-order variables, also for certain finite lattices with specified boundary conditions. In particular, all quantitites for this model, calculated in refs. [18,19], can be simply expressed in terms of two identical zero-field Ising models, not at $T_{\mathrm{c}}$; and scaling limit $(T \rightarrow \infty)$ results can be written down using ref. [4]. We should remark that the dual of this model is the fully-frustrated square Ising model, for which Forgács [20] factorized spin correlations, with all spins on the same sublattice, in terms of two dual Ising models using decimation. More generally, we have that all correlations become simple quadratic expressions in terms of correlations of the ordinary zero-field Ising model. Also, our results should be useful in a further study of the Yang-Lee edge singularity at high temperatures [21].

Finally, we note that the solution (16), of the homogeneous Laplace equation (15), is also conformally invariant. Recently, local conformal invariance has been used successfully to explain critical exponents [22-24] and to derive new results for critical correlations in the continuum limit [22,23], for a class of two-dimensional systems. Here, however, we have obtained in an unexpectedly easy way three corrections (18)-(20) due to the lattice, solving inhomogeneous Laplace equations. Therefore, our results may provide insight, how to generalize the concept of local conformal invariance to lattice models.

We thank Professor B.M. McCoy for his interest.
Professor R.E. Shrock and Dr. R.K. Ghosh have kind-
ly informed us that their results confirm the first row
of table 1. This work has been supported by the
National Science Foundation under Grant No.
DMR-82-06390.

## References

[1] B. Kaufman and L. Onsager, Phys. Rev. 76 (1949) 1244.
[2] B.M. McCoy and T.T. Wu, The two-dimensional Ising
model (Harvard Univ. Press, Cambridge, 1973) pp.
261-284.
[3] M.E. Fisher and R.J. Burford, Phys. Rev. 156 (1967)
583.
[4] T.T. Wu, B.M. McCoy, C.A. Tracy and E. Barouch, Phys.
Rev. B13 (1976) 316.
[5] M. Sato, T. Miwa and M. Jimbo, Proc. Japan Acad. 53A
(1977) 6, 147, 153, 183.
[6] B.M. McCoy and T.T. Wu, Phys. Rev. Lett. 45 (1980)
675.
[7] J.H.H. Perk, Phys. Lett. 79A (1980) 3.
[8] B.M. McCoy, J.H.H. Perk and T.T. Wu, Phys. Rev. Lett.
46 (1981) 757.
[9] J.H.H. Perk, H.W. Capel, G.R.W. Quispel and F.W.
Nijhoff, Physica 123A (1984) 1.
[10] R. Hirota, J. Phys. Soc. Japan 43 (1977) 2074.

[11] B.M. McCoy and T.T. Wu, The two-dimensional Ising
model (Harvard Univ. Press, Cambridge, 1973) p.265,
eqs. (4.40), (4.41).
[12] T.T. Wu, Phys. Rev. 149 (1966) 380.
[13] B.M. McCoy, J.H.H. Perk and R.E. Shrock, Nucl. Phys.
B220 [FS8] (1983) 35, 269.
[14] G. Müller and R.E. Shrock, Phys. Rev. B29 (1984) 288.
[15] M.E. Fisher and J. Stephenson, Phys. Rev. 132 (1963)
1411.
[16] R.E. Hartwig, J. Math. Phys. 7 (1966) 286.
[17] O.J. Heilmann and E.H. Lieb, Phys. Rev. Lett. 24 (1970)
1412.
[18] C.N. Yang and T.D. Lee, Phys. Rev. 87 (1952) 404, 410.
[19] B.M. McCoy and T.T. Wu, Phys. Rev. 155 (1967) 438.
[20] G. Forgács, Phys. Rev. B22 (1980) 4473;
G. Forgács and E. Fradkin, Phys. Rev. B23 (1981) 3442.
[21] P.J. Kortman and R.B. Griffiths, Phys. Rev. Lett 27
(1971) 1439;
D.A. Kurtze and M.E. Fisher, Phys. Rev. B20 (1979)
2785.
[22] A.A. Belavin, A.B. Zamolodchikov and A.M. Polyakov,
J. Stat. Phys. 34 (1984) 763.
[23] Vl.S. Dotsenko, J. Stat. Phys. 34 (1984) 781; Nucl. Phys.
B235 [FS11] (1984) 54;
Vl.S. Dotsenko and V.A. Fateev, NORDITA preprint
84/8.
[24] D. Friedan, Z. Qiu and S. Shenker, Phys. Rev. Lett 52
(1984) 1575.