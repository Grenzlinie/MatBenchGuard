# New method for calculating series expansions of correlation functions in the $d=2$ Ising model

Ranjan K. Ghosh and Robert E. Shrock
Institute for Theoretical Physics, State University of New York at Stony Brook, Stony Brook, New York 11794-3840
(Received 8 February 1984)

We exhibit a new method for calculating high-and low-temperature series expansions for diagonal spin-spin correlation functions in the $d=2$ Ising model. The method makes use of a differential equation obeyed by these functions.

The two-dimensional Ising model remains of great importance as one of the very few many-body interacting systems which are exactly soluble. Among the interesting objects of study in this model are the (static) spin-spin correlation functions $\langle\sigma_{00} \sigma_{m n}\rangle$. Exact results, involving formal Toeplitz determinants, are known for these. $^{1,2}$ A rather different and potentially far-reaching approach to Ising-model correlation functions has been developed recently; it is based on analyzing these functions as solutions to certain difference $^{3}$ or differential $^{4}$ equations. In this paper we shall exploit the differential-equation approach to present a new method for calculating high- and low-temperature series expansions of diagonal Ising-model correlation functions. We suspect, moreover, that this method may well be generalized to arbitrary (static) correlation functions.

The method consists of calculating power-series solutions to a (nonlinear) ordinary differential equation (ODE) which the function $S_{n} \equiv\langle\sigma_{00} \sigma_{n n}\rangle$ obeys. The value of this stems from the fact that the exact formal solution in terms of $n \times n$ Toeplitz determinants becomes more and more difficult to evaluate as $n$ increases. For $n=1,^{1,2}$

$$
S_{1,+}=\frac{2}{\pi k_{>}}\left[E\left(k_{>}\right)+\left(k_{>}^{2}-1\right) K\left(k_{>}\right)\right], \quad \text { (1a) }
$$

$$
S_{1,-}=\frac{2}{\pi} E\left(k_{<}\right), \quad \text { (1b) }
$$

while $^{5}$ for $n=2$,

$$
\begin{aligned}
S_{2,+}=\frac{4}{3 \pi^{2} k_{>}^{2}} & {\left[\left(5-k_{>}^{2}\right) E\left(k_{>}\right)^{2}\right.} \\
& +8\left(k_{>}^{2}-1\right) E\left(k_{>}\right) K\left(k_{>}\right) \\
& \left.+3\left(k_{>}^{2}-1\right)^{2} K\left(k_{>}\right)^{2}\right] \quad \text { (2a) }
\end{aligned}
$$

$$
\begin{aligned}
S_{2,-}=\frac{4}{3 \pi^{2} k_{<}^{2}} & {\left[\left(5 k_{>}^{2}-1\right) E\left(k_{<}\right)^{2}\right.} \\
& +2\left(k_{<}^{2}-1\right)^{2} E\left(k_{<}\right) K\left(k_{<}\right) \\
& \left.-\left(k_{<}^{2}-1\right)^{2} K\left(k_{<}\right)^{2}\right], \quad \text { (2b) }
\end{aligned}
$$

where $S_{n,+}\left(S_{n,-}\right)$ denotes $S_{n}$ for $T>T_{c}\left(T<T_{c}\right), K(k)$ and $E(k)$ are complete elliptic integrals, $\beta=\left(k_{B} T\right)^{-1}$,

$$
\begin{aligned}
& k_{>}=\sinh \left(2 \beta J_{1}\right) \sinh \left(2 \beta J_{2}\right) \text { for } T>T_{c}, \\
& k_{<}=k_{>}^{-1} \text { for } T<T_{c}
\end{aligned}
$$

[recall that $k_{>}\left(\beta_{c}\right)=k_{<}\left(\beta_{c}\right)=1$ ], and $J_{i}, i=1,2$, are the exchange constants of the model, defined by the Hamiltonian

$$
H=\sum_{i, j \in Z^{2}}\left(J_{1} \sigma_{i, j} \sigma_{i+1, j}+J_{2} \sigma_{i, j} \sigma_{i, j+1}\right).
$$

Although it is not too difficult to calculate the $S_{n}$'s for a few higher values of $n$, the Toeplitz determinant method becomes progressively more difficult to use in order to calculate exact analytic expressions for $S_{n}$, as $n$ increases further. For such values of $n$, approximate methods are thus worthwhile as primary sources of information about $S_{n}$. These methods include numerical calculations of the determinant (for a given temperature) $^{6}$ and high- and low-temperature series expansions. $^{7}$ Here we shall focus on the latter. We recall that these series are absolutely convergent in their respective domains of applicability, $T>T_{c}$ and $T<T_{c}$. In practice, these have relied on the analysis of appropriate sets of graphs. One of the major points of this paper is that the differential-equation method presented here has clear computational advantages over conventional graphical techniques for obtaining series expansions of the $S_{n}$ correlation functions. For very large $n$, McCoy and Wu have computed asymptotic expansions, $^{1}$ in the variable $1 / n$, of the $S_{n, \pm}$; we shall show later how these match onto our Taylor-series expansions. Perhaps most importantly, our method of calculating high- and low-temperature series expansions for $S_{n, \pm}$ by means of power-series solutions to a differential equation obeyed by these functions is suggestive of a way to obtain approximations of correlation functions in other lattice models for which there are no exact results.

The analysis proceeds as follows. Define

$$
t= \begin{cases}k_{>}^{-2} & \text { for } T>T_{c} \\ k_{<}^{-2} & \text { for } T<T_{c},\end{cases}
$$

$$
\sigma_{n,-}=t(t-1) \frac{d}{d t} \ln S_{n,-}-\frac{1}{4},
$$

$$
\sigma_{n,+}=t(t-1) \frac{d}{d t} \ln S_{n,+}-\frac{1}{4} t.
$$


Then, as was shown by Jimbo and Miwa, $^{4} \sigma_{n}=\sigma_{n, \pm}(t)$ are solutions to the ODE
$$
\begin{aligned}
{\left[t(t-1) \sigma_{n}^{\prime \prime}\right]^{2} } & -n^{2}\left[(t-1) \sigma_{n}^{\prime}-\sigma_{n}\right]^{2} \\
& +4 \sigma_{n}^{\prime}\left[(t-1) \sigma_{n}^{\prime}-\sigma_{n}-\frac{1}{4}\right]\left(t \sigma_{n}^{\prime}-\sigma_{n}\right)=0, \quad(7)
\end{aligned}
$$

Consider first the high-temperature phase of the theory. For the moment, for simplicity, we shall take the interactions to be isotropic, i.e., $J_{1}=J_{2} \equiv J$; we shall later reconstruct expansions for the general anisotropic case. The variable $t$ is related to the standard high-temperature expansion variable $\tanh \beta J$ according to
$$
t=\frac{(1-x)^{4}}{16 x^{2}}, \quad(8)
$$
where
$$
x=\tanh ^{2}(\beta J). \quad(9)
$$

Using this relation, one can reexpress Eq. (7) in the form of an ODE in the variable $x$, which is convenient for analyzing the high-temperature behavior of the solutions. The correlation function $S_{n,+}$ has a high-temperature series expansion of the general form
$$
S_{n,+}=\sum_{k=n}^{\infty} c_{n, k} x^{k}. \quad(10)
$$

By well-known means, $^{7}$ it is possible to associate with each term in this expansion a set of graphs consisting of bonds linking the sites (0,0) and (n, n) on the lattice (with possible disconnected contributions). From this correspondence, it follows that the coefficients $c_{n, k}$ are positive integers. An elementary combinatorics argument yields the result
$$
c_{n, n}=\frac{(2 n)!}{(n!)^{2}}. \quad(11)
$$

Using graphical techniques, we have also found that
$$
c_{n, n+1}=2 n c_{n, n}. \quad(12)
$$

(This result is not necessary for our method, which needs only the fact that the lowest-order term is proportional to $x^{n}$ in order to begin.) The procedure is then to generate the higher terms recursively. An interesting feature is that one does not have to specify the actual value of $c_{n, n}$, given by Eq. (11), in order to solve for the higher $c_{n, k}$, which have the important property
$$
c_{n, k}=r_{n, k} c_{n, n}, \quad(13)
$$
where $r_{n, k}$ is a rational function of $n$ for each $k$. The problem of calculating the $c_{n, k}$ is thus reduced to the problem of calculating the ratios $r_{n, k}$. The equations for the $r_{n, k}$ are quadratics with coincident roots for $k=n+2$ and $n+3$, and a quadratic with distinct roots for $k=n+4$. The spurious root for $r_{n, n+4}$ is identified and eliminated by the requirement that the $c_{n, k}$ be integers. Next, for $k=n+5$ to $k=3(n+1)$ the equations for the $r_{n, k}$ are linear. Solving these equations yields the $r_{n, k}$ for $k \leq 3(n+1)$, except for the boundary case $n=1$, for which $k \leq 5$. We find that for $j \geq 2$ the $r_{n, n+j}$, at least as far as we have computed them, have the general form
$$
r_{n, n+j}=\frac{\sum_{l=1-\theta(j-3)}^{j+[j / 2]} \alpha_{n, j, l} n^{l}}{\prod_{m=1}^{[j / 2]}(n+m)}
$$
with rational $\alpha_{n, j, l}$ which satisfy
$$
\alpha_{n, j, 0}<0, \quad(15 a)
$$
$$
\alpha_{n, j, l}>0, \quad 1 \leq l \leq j+[j / 2], \quad(15 b)
$$
where $[v]$ denotes the integral part of $v$, and $\theta(x)$ is defined as 0 for $x \leq 0$, and 1 for $x>0$.

We thus obtain, for arbitrary $n$,
$$
r_{n, n+2}=n\left(2 n^{2}+3 n+5\right)(n+1)^{-1}, \quad(16)
$$

$$
r_{n, n+3}=2 n\left(2 n^{3}+5 n^{2}+16 n+25\right)[3(n+1)]^{-1}, \quad(17)
$$

$$
r_{n, n+4}=\left(4 n^{6}+24 n^{5}+103 n^{4}+372 n^{3}+943 n^{2}+726 n-48\right)[6(n+1)(n+2)]^{-1}, \quad(18)
$$

$$
r_{n, n+5}=\left(4 n^{7}+32 n^{6}+183 n^{5}+930 n^{4}+4031 n^{3}+10228 n^{2}+6972 n-960\right)[15(n+1)(n+2)]^{-1}. \quad(19)
$$

Further, for $n \geq 2$,
$$
\begin{aligned}
r_{n, n+6}= & \left(8 n^{9}+108 n^{8}+858 n^{7}+5793 n^{6}+36297 n^{5}+183027 n^{4}+613537 n^{3}+994032 n^{2}+462420 n-112320\right) \\
& \times[90(n+1)(n+2)(n+3)]^{-1}
\end{aligned}
$$

$$
\begin{aligned}
r_{n, n+7}= & \left(8 n^{10}+132 n^{9}+1278 n^{8}+10527 n^{7}+83412 n^{6}+575778 n^{5}+3027562 n^{4}+10150743 n^{3}\right. \\
& \left.+15729780 n^{2}+6345900 n-2358720\right)[315(n+1)(n+2)(n+3)]^{-1}
\end{aligned}
$$
and, for $n \geq 3$,
$$
\begin{aligned}
r_{n, n+8}= & \left(16 n^{12}+384 n^{11}+4984 n^{10}+50976 n^{9}+490377 n^{8}+4421088 n^{7}+34227506 n^{6}\right. \\
& +206199624 n^{5}+864880457 n^{4}+2149564968 n^{3}+2523141300 n^{2} \\
& +686019600 n-437633280)[2520(n+1)(n+2)(n+3)(n+4)]^{-1},
\end{aligned}
$$

$$
\begin{aligned}
r_{n, n+9}= & \left(16 n^{13}+448 n^{12}+6776 n^{11}+80384 n^{10}+901641 n^{9}+9733956 n^{8}+94231394 n^{7}\right. \\
& +754112240 n^{6}+4601914009 n^{5}+19260277516 n^{4}+46906943700 n^{3} \\
& \left.+52537189536 n^{2}+10939731264 n-11226055680\right)[11340(n+1)(n+2)(n+3)(n+4)]^{-1}.
\end{aligned}
\tag{23}
$$

The coefficients with $n+6 \leq k \leq n+9, n=1,2$, which are not given by these general formulas are $c_{1,7}=2038$, $c_{1,8}=9104, c_{1,9}=41986, c_{1,10}=198516, c_{2,10}=341298$, and $c_{2,11}=1642536$. Nothing in principle prevents one from calculating the $r_{n, k}$ and hence $c_{n, k}$ for $k \geq n+10$ (with $k$-dependent lower bounds on $n$ analogous to those cited above). We have stopped at $k=n+9$ because of the increasing amount of time required for the computation and because the point of our analysis is not just to present specific results but, more generally, to exhibit a new method of calculation for series expansions of correlation functions.

The advantage of our present method for calculating the high-temperature series of $S_{n,+}$ over the method based on the enumeration of graphs should now be obvious; al- though it is relatively easy to use combinatoric and graph- ical techniques to calculate $c_{n, n}$ and $c_{n, n+1}$, to do the same for the higher coefficients would clearly be a need- lessly difficult way to try to calculate these coefficients.

It is interesting to see how our new exact coefficients for the $c_{n, k}$ up to $k=n+9$ extend known results. McCoy and $\mathrm{Wu}$ derived an asymptotic expansion for $S_{n,+}$ for fixed $T>T_{c}$ as $n \rightarrow \infty .{ }^{1}$ This is a different limit than the one for a high-temperature expansion of $S_{n,+}$, which is fixed $n$ with $T \rightarrow \infty$. Their result [Eq. (XI.2.46) of Ref. 1] is
$$
\begin{aligned}
S_{n,+} \sim \frac{1}{(\pi n)^{1 / 2}} \frac{k_{>}^{n}}{\left(1-k_{>}^{2}\right)^{1 / 4}} & \left\{1-\frac{\kappa}{2^{3} n}+\frac{9 \kappa^{2}-8}{2^{7} n^{2}}\right. \\
& +\frac{5 \kappa\left(-15 \kappa^{2}+16\right)}{2^{10} n^{3}} \\
& \left.+O\left(n^{-4}\right)\right\}
\end{aligned}
\tag{24}
$$
where
$$
\kappa=\frac{1+k_{>}^{2}}{1-k_{>}^{2}} . \tag{25}
$$

To compare these two expansions, we consider the region of their common validity, namely, $T \rightarrow \infty$ and $n \rightarrow \infty$. First, by the use of Stirling's asymptotic expansion, we have
$$
\begin{aligned}
\frac{(2 n) !}{(n !)^{2}} \sim \frac{2^{2 n}}{(\pi n)^{1 / 2}} & \left\{1-\frac{1}{2^{3} n}+\frac{1}{2^{7} n^{2}}+\frac{5}{2^{10} n^{3}}\right. \\
& \left.-\frac{21}{2^{15} n^{4}}-\frac{399}{2^{18} n^{5}}+O\left(n^{-6}\right)\right\} . \text { (26) }
\end{aligned}
$$

Substituting this into our series and transforming Eq. (24) into a power series in $x$, we find, first, that the common $x$-independent prefactor from Eq. (24) agrees to the extent of its accuracy, which is to terms of order $n^{-3}$ in the large brackets, with Eq. (26). Extracting this common factor (26) to the requisite accuracy, we may compare the exact ratios $r_{n, k}$ with the analogous ratios resulting from the expansion of Eq. (24). We find, again, that they agree, to the extent of the accuracy of the latter result. For ex- ample, for the coefficient of $x^{n+2}$, with the common fac- tor (26) removed, Eq. (24) yields the expansion
$$
2 n^{2}+n+4-\frac{4}{n}+\frac{4}{n^{2}}-\frac{4}{n^{3}}+O\left(n^{-4}\right),
$$
which agrees, to the extent of its accuracy, with the corre- sponding large- $n$ expansion of our exact ratio $r_{n, n+2}$ given in Eq. (16). In general, Eq. (24) yields coefficients of $x^{n+k}$, as defined above, which are accurate to $O\left(n^{k-5}\right)$. We note in passing that, as is evident from Eqs. (11)-(23), our exact coefficients for the $c_{n, k}$ have the large- $n$ behavior
$$
c_{n, k} \propto n^{k-n-1 / 2}\left[1+O\left(n^{-1}\right)\right] . \tag{27}
$$

We return to the high-temperature expansion of $S_{n,+}$. Beyond the level $k=5$ for $n=1$ and $k=3(n+1)$ for $n>1$, the equations for the $c_{n, k}$ take the form of an infinite set of coupled linear equations:
$$
\begin{aligned}
\left(\sum_{p=0}^{1+l} A_{2 n+5+l, 3 n+4+p} c_{n, 3 n+4+p}\right)+B_{2 n+5+l}=0, \\
l=0,1, \ldots, \infty \quad(28)
\end{aligned}
$$
where $A$ and $B$ are, respectively, a constant matrix and vector of infinite dimension. These equations arise, as be- fore, from equating to 0 the coefficient of $x$ to the ap propriate power, here $x^{2 n+5+l}$, in the power-series evalua tion of the ODE (7). However, they differ from the equa- tions for the lower-order $c_{n, k}$ 's because of the infinite cou pling of all levels in $k$ to each other. This property prevents one from using the present method to solve for the $c_{n, k}$ for $k>5$ for $n=1$ and $k>3(n+1)$ for $n>1$. Although our general formulas for the $c_{n, k}$, Eqs. (11)-(23), stop at $k=n+9$, we have gone beyond this level in numerical computations. In Appendix A we list the (exact) numerical values for $c_{n, k}, n \leq 8$, and $k \leq 3(n+1)$ which we have obtained. With our method it is equally easy to compute the $c_{n, k}$ for $n \geq 9$ as for the cases $n \leq 8$ that are given.

The variable $\tanh \beta J$ is a natural one for high temperature series expansions. However, as is evident from the expressions for $S_{1,+}$ and $S_{2,+}$ [Eqs. (1a) and (2a)], the exact results actually depend directly on the variable $k_{>}$. Hence, it is worthwhile to reexpress our ex- pansion of $S_{n,+}$ in $x$, Eq. (10), as an expansion in $k_{>}$. We have done this and find that this expansion has the general form

$$
S_{n,+}=\left(\frac{k_{>}}{4}\right)^{n} \sum_{l=0}^{\infty} h_{n, n+2 l}\left(\frac{k_{>}}{4}\right)^{2 l}.
\tag{29}
$$

It is convenient to choose the normalization for the expansion variable to be $k_{>} / 4$ because this renders the lowest-order coefficients in the series equal:
$$
h_{n, n}=c_{n, n}=\frac{(2 n) !}{(n !)^{2}}.
\tag{30}
$$

From Eq. (29) it follows that $S_{n,+}$ is an even or odd function of $k_{>}$ if $n$ is even or odd, respectively. Recall that, in contrast, $S_{n,+}$ is neither an even nor an odd function of $x$. We find that, analogously to the case with the $c_{n, k}$, the $h_{n, k}$ have the factorization property
$$
h_{n, k}=\rho_{n, k} h_{n, n},
\tag{31}
$$
where $\rho_{n, k}$ is a rational function of $n$ for each $k$. The general form of $\rho_{n, n+2 j}$ for the nontrivial case $j \geq 1$ is
$$
\rho_{n, n+2 j}=\frac{\sum_{l=1-\theta(j-1)}^{j} \gamma_{n, j, l} n^{l}}{\prod_{m=1}^{j}(n+m)}
\tag{32}
$$
with integral $\gamma_{n, j, l}$ which satisfy
$$
\gamma_{n, j, 0}<0,
\tag{33a}
$$
$$
\gamma_{n, j, l}>0, \quad 1 \leq l \leq j.
\tag{33b}
$$

Our calculations yield the specific results
$$
\rho_{n, n+2}=\frac{4 n}{n+1},
\tag{34}
$$
$$
\rho_{n, n+4}=\frac{8\left(5 n^{2}+5 n-1\right)}{(n+1)(n+2)},
\tag{35}
$$
$$
\rho_{n, n+6}=\frac{96\left(5 n^{3}+15 n^{2}+7 n-4\right)}{(n+1)(n+2)(n+3)},
\tag{36}
$$
$$
\rho_{n, n+8}=\frac{96\left(65 n^{4}+390 n^{3}+637 n^{2}+104 n-231\right)}{(n+1)(n+2)(n+3)(n+4)}.
\tag{37}
$$

One advantage of this form of the expansion is that it manifestly applies both in the isotropic and the anisotropic case. As with the $c_{n, k}$, it is possible to calculate (exact) numerical values of the $h_{n, k}$ beyond the level $k=n+8$. In Appendix B we list the further values of $h_{n, k}$ which can be obtained from the $c_{n, k}$ 's that we have calculated, for $5 \leq n \leq 8$. This concludes our discussion of the high-temperature series expansions of $S_{n,+}$.

An interesting feature of the ODE (7) is that it applies, with appropriate redefinitions of $t$ and $\sigma_{n}(t)$, for both $T>T_{c}$ and $T<T_{c}$. It is natural to inquire what information it gives about low-temperature series expansions of $S_{n,-}$. Here we find a somewhat different structure than in the high-temperature region. As the spin separation goes to infinity, any (static) spin-spin correlation function approaches the square of the long-range order parameter, or magnetization, given by $^{8}$
$$
M^{2}=\lim _{m^{2}+n^{2} \rightarrow \infty}\left\langle\sigma_{00} \sigma_{m n}\right\rangle=\left(1-k_{<}^{2}\right)^{1 / 4}.
\tag{38}
$$

Hence, a fortiori, as $n \rightarrow \infty$
$$
S_{n,-} \rightarrow\left(1-k_{<}^{2}\right)^{1 / 4}=\sum_{l=0}^{\infty}(-1)^{l}\left(\begin{array}{l}
\frac{1}{4} \\
l
\end{array}\right) k_{<}^{2 l},
\tag{39}
$$
where $\left(\begin{array}{l}\mu \\ l\end{array}\right)$ is the binomial coefficient. Of course, this does not determine the expansion of $S_{n,-}$ for finite $n$. However, one would expect that (a) for a given $n$, the closer $T$ is to 0 , the closer the corresponding low-temperature expansion of $S_{n,-}$ will be to Eq. (39), and (b) for a given $T<T_{c}$, the larger $n$ is, the closer the expansion of $S_{n,-}$ will be to (39). Both of these expected properties are true of the expansions that we calculate. The expansion variable which we choose is $k_{<}^{2}$, which is natural both for the ODE and for the comparison with the large-$n$ limit given by Eq. (38). Our procedure is again a recursive one. We find that
$$
S_{n,-}=\sum_{l=0}^{n}(-1)^{l}\left(\begin{array}{l}
\frac{1}{4} \\
l
\end{array}\right) k_{<}^{2 l}+O\left(k_{<}^{2 l+2}\right),
\tag{40}
$$
where the terms of order $k_{<}^{2 l+2}$ and higher are specific to the given value of $n$. Thus the low-temperature expansion of $S_{n,-}$ consists first of a dominant part, extending from zeroth to $n$th order in $k_{<}^{2}$, which is universal and reflects the long-range order (spontaneous magnetization) present for $T<T_{c}$. The second part of the $S_{n,-}$ expansion is higher order and $n$ dependent, and reflects the detailed nature of the spin-spin correlations along the diagonal. As is clear from Eq. (40), for each unit increase in $n$, the universal part of the expansion grows, by one order in $k_{<}^{2}$. These results are in agreement with an asymptotic expansion of $S_{n,-}$, for fixed $T<T_{c}$ and $n \rightarrow \infty$ [Eqs. (XI.3.27) of Ref. 1].

In conclusion, we believe that our high-temperature series expansion of the diagonal correlation functions $\left\langle\sigma_{00} \sigma_{n n}\right\rangle$ of the $d=2$ Ising model are valuable sources of information about these functions, especially for large $n$, where the evaluation of Toeplitz determinants is impracticable and the combinatorics necessary for graphical calculations are forbiddingly complicated. More generally, we hope to have convinced the reader of the power of the differential equation technique for obtaining analytic approximations to correlation functions. If the present case is a reliable guide, one should be able to discover new differential equations, or perhaps difference-differential equations, which govern the temperature and spatial behavior of arbitrary correlations functions in the $d=2$ Ising model and indeed other classical- or quantum-lattice models. We anticipate that these may play a very important role in the effort to obtain exact solutions and practical approximations to these functions.

We thank B. M. McCoy and J. H. H. Perk for valuable discussions. This research was supported in part by National Science Foundation Grant No. PHY-81-09110A-01.

## APPENDIX A

We list below the values of $c_{n, k}, 4 \leq n \leq 8$, which go beyond those which can be obtained from the general formulas (11)-(17), i.e., $n+10 \leq k \leq 3(n+1)$:

$c_{4,14}=348\ 874\ 048\ ,$
$c_{4,15}=1\ 758\ 430\ 208\ ,$

$c_{5,15}=2\ 161\ 862\ 608\ ,$
$c_{5,16}=10\ 890\ 254\ 880\ ,$
$c_{5,17}=55\ 652\ 958\ 384\ ,$
$c_{5,18}=287\ 484\ 027\ 520\ ,$

$c_{6,16}=13\ 298\ 019\ 920\ ,$
$c_{6,17}=66\ 643\ 280\ 992\ ,$
$c_{6,18}=339\ 942\ 433\ 564\ ,$
$c_{6,19}=1\ 756\ 267\ 070\ 032\ ,$
$c_{6,20}=9\ 161\ 355\ 037\ 832\ ,$
$c_{6,21}=48\ 155\ 077\ 839\ 504\ ,$

$c_{7,17}=81\ 913\ 174\ 980\ ,$
$c_{7,18}=406\ 728\ 277\ 384\ ,$
$c_{7,19}=2\ 064\ 091\ 639\ 508\ ,$
$c_{7,20}=10\ 638\ 795\ 387\ 712\ ,$
$c_{7,21}=55\ 460\ 032\ 171\ 484\ ,$
$c_{7,22}=291\ 625\ 929\ 973\ 016\ ,$
$c_{7,23}=1\ 544\ 074\ 562\ 707\ 204\ ,$
$c_{7,24}=8\ 222\ 147\ 869\ 275\ 600\ ,$

$c_{8,18}=507\ 527\ 808\ 304\ ,$
$c_{8,19}=2\ 488\ 641\ 985\ 696\ ,$
$c_{8,20}=12\ 525\ 796\ 852\ 160\ ,$
$c_{8,21}=64\ 250\ 389\ 221\ 024\ ,$
$c_{8,22}=334\ 100\ 874\ 771\ 632\ ,$
$c_{8,23}=1\ 754\ 976\ 215\ 268\ 832\ ,$
$c_{8,24}=9\ 290\ 773\ 334\ 546\ 134\ ,$

$c_{8,25}=49\ 494\ 022\ 749\ 324\ 800\ ,$
$c_{8,26}=265\ 040\ 815\ 910\ 603\ 776\ ,$
$c_{8,27}=1\ 425\ 597\ 420\ 325\ 991\ 936\ .$

---

## APPENDIX B

We list below the values of $h_{n,l}$, $4\leq n\leq 8$, which go beyond those covered by the general formulas (34)-(37), i.e., $l\geq n+10$:

$h_{4,14}=2\ 447\ 808\ ,$

$h_{5,15}=10\ 150\ 096\ ,$
$h_{5,17}=126\ 484\ 512\ ,$

$h_{6,16}=41\ 168\ 576\ ,$
$h_{6,18}=520\ 068\ 304\ ,$
$h_{6,20}=6\ 738\ 609\ 024\ ,$

$h_{7,17}=164\ 997\ 456\ ,$
$h_{7,19}=2\ 106\ 274\ 016\ ,$
$h_{7,21}=27\ 559\ 374\ 016\ ,$
$h_{7,23}=367\ 401\ 459\ 936\ ,$

$h_{8,18}=656\ 728\ 576\ ,$
$h_{8,20}=8\ 453\ 815\ 776\ ,$
$h_{8,22}=111\ 477\ 519\ 872\ ,$
$h_{8,24}=1\ 497\ 089\ 756\ 452\ ,$
$h_{8,26}=20\ 395\ 689\ 781\ 632\ .$

---

$^{1}$For a comprehensive review of the $d=2$ Ising model and references to the literature, see B. M. McCoy and T. T. Wu, *The Two-Dimensional Ising Model* (Harvard University Press, Cambridge, 1973).

$^{2}$A partial list of early works on spin-spin correlation functions in the $d=2$ Ising model is as follows: L. Onsager, Phys. Rev. 65, 117 (1944); B. Kaufman and L. Onsager, *ibid.* 76, 1244 (1949); C. N. Yang, *ibid.* 85, 803 (1952); E. W. Montroll, R. B. Potts, and J. C. Ward, J. Math. Phys. 4, 308 (1963); T. T. Wu, Phys. Rev. 149, 380 (1966); R. B. Griffiths, J. Math. Phys. 8, 474 (1967); 8, 484 (1967); B. M. McCoy and T. T. Wu, Phys. Rev. 155, 438 (1967); 162, 719 (1967); 174, 546 (1968); H. Cheng and T. T. Wu, *ibid.* 164, 719 (1967); L. P. Kadanoff, Nuovo Cimento 44, 276 (1966); B. M. McCoy, T. T. Wu, C. A. Tracy, and E. Barouch, Phys. Rev. B 13, 316 (1976).

$^{3}$B. M. McCoy and T. T. Wu, Phys. Rev. Lett. 45, 675 (1980).
$^{4}$M. Jimbo and T. Miwa, Proc Jpn. Acad. 56A, 405 (1980); M. Kashiwara and T. Miwa, *ibid.* 57A, 342 (1981).
$^{5}$The $S_n$ functions for $2\leq n\leq 6$ are given in R. K. Ghosh and R. E. Shrock, Stony Brook preprint ITP-SB-84-15 (to be published). $S_2$ has also been calculated by J. H. H. Perk (private communication).
$^{6}$For an early calculation of this type, see M. E. Fisher and J. Stephenson, Phys. Rev. 132, 1411 (1963).
$^{7}$See, e.g. C. Domb, Adv. Phys. 9, 149 (1960); *Series Expansions of Lattice Models*, Vol. 3 of *Phase Transitions and Critical Phenomena*, edited by C. Domb and M. S. Green (Academic, New York, 1974), and references therein.
$^{8}$C. N. Yang, Phys. Rev. 85, 808 (1952).