# Finite-size behavior of the simple-cubic Ising lattice*
D. P. Landau
Department of Physics and Astronomy, University of Georgia, Athens, Georgia 30602 $^{\dagger}$
and Institut für Festkörperforschung, Kernforschungsanlage Jülich, 517 Jülich, West Germany
(Received 22 January 1976)

A Monte Carlo method is used to study $N ×N ×N$ simple-cubic Ising lattices with periodic boundary conditions and free edges. For both types of boundary conditions the position of the specific-heat maximum varies for large $N$ as $a N^{-\lambda}$, where $\lambda$ has the scaling value $\lambda=\nu^{-1}$. Both the thermal and magnetic properties are shown to obey finite-size scaling. The free-edge data are shown to be consistent with a surface contribution described by the scaling exponents $\alpha_{s}=\alpha+\nu, \beta_{s}=\beta-\nu, \gamma_{s}=\gamma+\nu$. Using the free-edge data we also consider corrections to scaling in the infinite lattice and discuss "rounding" in real systems in terms of surface contributions from grains.

## I. INTRODUCTION

The expected thermodynamic behavior of finite systems of interacting particles has been discussed by Fisher $^{1}$ in terms of a scaling theory involving the critical exponents of the corresponding infinite system. According to this finite-size scaling theory, the free energy of an $N ×N ×N$ lattice is given by the scaling ansatz $^{2}$:
$$F(N, T)=N^{-\psi} \mathcal{F}^{0}\left(N^{\theta} t\right), \quad(1)$$
where $\psi=(2-\alpha) / \nu, t=|1-T / T_{c}(\infty)|, T_{c}(\infty)$ is the infinite-lattice transition temperature, and $\mathcal{F}^{0}$ is a scaling function involving the scaled variable $x=N^{\theta} t .^{3}$ The scaling of the correlation length $\xi=\xi_{0} t^{-\nu}$ suggests $\theta=\nu^{-1}$ and the appropriate scaling variable should be $x=t N^{1 / \nu}$. The shift in the "pseudo-ordering" temperature $T_{c}(N)$ (usually defined by the maximum in the specific heat) is given by
$$\delta T_{c}=\left[1-T_{c}(N) / T_{c}(\infty)\right] \approx a N^{-\lambda}, \quad N \to \infty \quad(2)$$
where, according to scaling theory, $\lambda=\nu^{-1}$. The possibility that $\lambda$ generally has the nonscaling value $\lambda=1$, however, could not be excluded. $^{1}$

The finite-size scaling of the free energy leads to similar relations for the spontaneous magnetization $M$, the susceptibility $\chi$, and the specific heat $C$ of systems with periodic boundary conditions (pbc):
$$M=N^{-\beta / \nu} X^{0}(x), \quad(3a)$$

$$\chi T=N^{\gamma / \nu} Y^{0}(x), \quad(3b)$$

$$C=N^{\alpha / \nu} Z^{0}(x), \quad(3c)$$
where again $x=t N^{1 / \nu}$. For large $x$ (i.e., $t \ll 1$ but $N \to \infty$ ) it is necessary that Eqs. (3a)-(3c) asymptotically reproduce the infinite-lattice critical behavior. With this constraint in mind it is straightforward to show that for large $x$
$$X^{0}(x) \approx B x^{\beta}, \quad(4a)$$

$$Y^{0}(x) \approx C^{ \pm} x^{-\gamma}, \quad(4b)$$

$$Z^{0}(x) \approx A^{ \pm} x^{-\alpha}, \quad(4c)$$
where $B, C^{ \pm}$, and $A^{ \pm}$are the critical amplitudes $(C^{+}, A^{+}$for $T>T_{c}$ and $C^{-}, A^{-}$for $T<T_{c})$ for an infinite system. Conversely, as $x \to 0, X^{0}, Y^{0}$, and $Z^{0}$ must approach constant values. For systems with free edges Eqs. (3a)-(3c) remain valid but the large-$x$ behavior must include correction terms due to the surfaces. In this case the scaling functions as $x \to \infty$ become
$$X^{0}(x) \approx B x^{\beta}+B_{s} x^{\beta_{s}}, \quad(5a)$$

$$Y^{0}(x) \approx C^{ \pm} x^{-\gamma}+C_{s}^{ \pm} x^{-\gamma_{s}}, \quad(5b)$$

$$Z^{0}(x) \approx A^{ \pm} x^{-\alpha}+A_{s}^{ \pm} x^{-\alpha_{s}}, \quad(5c)$$
where the new "surface" exponents are related to the usual ones by $\beta_{s}=\beta-\nu, \gamma_{s}=\gamma+\nu$, and $\alpha_{s}$ $=\alpha+\nu$. Results on $N ×N$ Ising square lattices $^{4,5}$ have borne out the scaling predictions in two dimensions. However, since $\nu=1$ in two dimensions, it was not possible to decide whether $\lambda=\nu^{-1}$ or $\lambda=1$ was in general correct. For the simple-cubic lattice, however, $\nu \simeq 0.64$ and the distinction should be clear. Previous Monte Carlo studies on simple-cubic Ising lattices with free edges $^{6}$ yielded a rather contradictory result, although it was later argued $^{7}$ rather convincingly that this was because the lattices investigated $(N \lesssim 12)$ were too small to show the asymptotic large-$N$ variation described by Eq. (2).

In this paper we show results of a Monte Carlo study of $S=\frac{1}{2}$ Ising spins arrayed on an $N ×N ×N$ simple-cubic lattice with
$$\mathcal{K}=\sum_{\langle i j\rangle} K_{\mathrm{nn}} \sigma_{i} \sigma_{j}, \quad(6)$$
where $K_{\mathrm{nn}}$ is the interaction constant for nearest-neighbor pairs $\langle i j\rangle$ and $\sigma_{i}, \sigma_{j}= \pm 1$. Lattices with

pbc and free edges were considered for $N \lesssim 20$.
The Monte Carlo method used was identical to the one developed for our square-lattice studies (complete details can be found in Ref. 5) and shall not be discussed here. Each data point was taken at least twice using different starting configurations. After "equilibrium" was reached typically 2000-5000 Monte Carlo steps per spin were used for calculating the averages. Our data will be presented in Sec. II and the scaling analysis and discussion will be given in Sec. III.

## II. RESULTS

The temperature variation of the internal energy is shown for the entire range of lattices studied in Fig. 1. The data normalized by $U_{0}=6 N^{3} K_{\mathrm{nn}}$ for both types of boundary conditions. The effect of finite size on lattices with pbc is quite small except near to $T_{c}(\infty)$. On the other hand, the data obtained for lattices with free edges showed pro- nounced size dependence over almost the entire temperature range. The difference in the finite-size behavior for the two sets of boundary conditions shows up similarly in the specific-heat data. These results, see Fig. 2, reveal distinct differences in both position and height of the maxima. In particular, $C_{\max }$ occurs near $T_{c}(\infty)$ for pbc but is shifted dramatically to lower temperatures for free edges.

Spontaneous magnetization data are shown in Fig. 3 along with the infinite-lattice curve $^{8}$ as determined from series expansions. As expected, $^{5,6}$ finite-size "tails" are found at high temperatures for both sets of boundary conditions, but only the free-edge data show significant finite size effects below $T_{c}(\infty)$. In Fig. 4 we show the susceptibility data, $^{9}$ plotted on a semilogarithmic scale. The effects of finite size are qualitatively similar to those for the specific heat (see Fig. 2) in that both the height and position of the maxima are affected differently by the two types of boundary conditions.

![](./images/813350827686100992_1.jpg)

FIG. 1. Temperature dependence of the internal energy for a range of lattice sizes: $U_{0}=6 N^{3} K_{\mathrm{nn}}$.

![](./images/813350827686100992_2.jpg)

FIG. 2. Temperature dependence of the specific heat for several different lattice sizes.

![](./images/813350827686100992_3.jpg)

## III. DISCUSSION

### A. Size variation of the "ordering temperature"

Using the data presented in Sec. II, we can now test the finite-size scaling relations presented in Sec. I. Identifying $T_c(N)$ with the positions of the specific-heat maxima we examine the size dependence of $T_c$ in Fig. 5. The asymptotic behavior for both sets of boundary conditions seems described by Eq. (2) with $\lambda=\nu^{-1}$. For pbc the data for $N \leqslant 6$ are all in the asymptotic region with $a=0.98 \pm 0.04$. The free-edge data, however, appear to be just entering the asymptotic region for $N=14$. Data on smaller lattices $^{6}$ could not probe the asymptotic region at all; large deviations from $T_c(\infty)$ quickly bring $T_c(N)$ outside the infinite-lattice critical region and corrections to scaling become important. Since the scaling prediction $\delta T_c \propto N^{-1 / \nu}$ comes about due to the correlation length $\xi=\xi_0 t^{-\nu}$ reaching system dimensions, the correction to scaling for $\xi$ should allow us to estimate the correction to the size dependence of $\delta T_c$. The expected relation for the correlation length including lowest-order corrections is
$$
\xi=\xi_0 \epsilon^{-\nu}\left(1+a_0 t^{\Delta}\right), \tag{7}
$$
and using the estimate of $\Delta=0.5$ we find that
$$
\delta T_c=a N^{-1 / \nu}+a^{\prime} N^{-3 / 2 \nu}+\cdots. \tag{8}
$$
The actual value of $\Delta$ may deviate appreciably from 0.5; however, our present analysis is too imprecise to be sensitive to small changes in $\Delta$. Saul et al. $^{10}$ provide a good discussion of the present evidence supporting this estimate. It should also be noted that outside the asymptotic scaling region, the shift in $T_c$ may not simply follow the $N / \xi$ criterion. In fact, various definitions of $\xi$ may begin to differ significantly. Recent series-expansion studies $^{10}$ on the fcc Ising lattice have

![](./images/813350827686100992_4.jpg)

![](./images/813350827686100992_5.jpg)

shown that the lowest-order correction to scaling for the high-temperature susceptibility vanishes for $S=\frac{1}{2}$. While there is no compelling reason why it should also vanish for the correlation length, the susceptibility result suggests that the possibility should be considered. In this case

$$\xi=\xi_{0} \epsilon^{-\nu}\left(1+a_{0} t^{1.0}\right)\qquad(9)$$

which leads to

$$\delta T_{c}=a N^{-1 / \nu}+a^{\prime} N^{-2 / \nu}+\cdots.\qquad(10)$$

The data are considered in view of these two possibilities [Eqs. (8) and Eq. (10)] in Fig. 6. The plots of $(\delta T_{c}) N^{1 / \nu}$ vs either $N^{-1 / \nu}$ [see Eq. (10)] or $N^{-1 / 2 \nu}$ [see Eq. (8)] should yield asymptotically linear behavior with intercept $a$ and slope $a'$. Included in this figure are the Monte Carlo results and exact values ( for $N=2$ and 3) of Binder. $^{6}$ From Fig. 6 we see that it is not possible to make a definitive decision, although the plot made assuming an $t^{0.5}$ correction term appears to be slightly superior over a wider range of $N$. It would also be desirable to determine whether or not the next-order correction terms in Eqs. (8) and (10) are negligible; however, this would require knowledge of the next-highest-order correction to $\xi$. It is clear from Fig. 6 that no matter which form is actually realized, that corrections to scaling will be important for $N \lesssim 10$ and may not be negligible even for $N=20$. Including both the experimental errors as well as the uncertainty in the correction we estimate the amplitude of the dominant term in the temperature shift $a=6.2 \pm 0.8$.

![](./images/813350827686100992_6.jpg)

FIG. 6. Size dependence of the "ordering temperature" with corrections to scaling included: present Monte Carlo data, $\bigcirc$; Monte Carlo values from Ref. 6, $+$; exact results from Ref. 6, $\bullet$.

### B. Bulk finite-size scaling
The finite-size scaling of the bulk properties for lattices with pbc are shown in Figs. 7-9. The scaling plot for the magnetization was made with $\beta=0.312$ and $\nu=0.64$. The solid line gives the predicted asymptotic behavior [Eq. (4a)] with slope $B=1.57$ (as determined from series expansions $^{8}$ ); the agreement with the data is clearly quite good. As $x \to 0, X^{0}(x) \approx 1.11 \pm 0.03$. The scaling of the susceptibility is also quite good as shown in Fig. 8. The solid line for $T>T_{c}$ corresponds to the asymptotic form given by Eq. (4b) with amplitude $C^{+}=1.058$ as determined from analysis of series expansions. $^{11}$ The uncertainties in both the critical amplitude and critical exponent are much greater below $T_{c}$ because of difficulties in the analysis of the low-temperature series. The best estimate $^{8,12,13}$ yields $C^{-} \approx 0.195$ with exponents ranging from $\gamma=1.25$ to 1.31 . In our finite-size scaling plot we have assumed exponent symmetry and taken $\gamma^{-}=\gamma^{+}=1.25$. The low-temperature-data scale will but yield a best fit of $C^{-}=0.155 \pm 0.015$, which is clearly below the series value. We feel that the series result is unlikely to be in error by anywhere near the amount of the discrepancy; it is more likely that the Monte Carlo susceptibility data are systematically too low by a small amount (as occurred with the square-lattice data $^{5}$ ).

Since the specific heat diverges so weakly the divergent portion does not completely dominate the "background" except very close to $T_{c}$. In the $t$ region covered by the Monte Carlo data the

![](./images/813350827686100992_7.jpg)

FIG. 7. Finite-size scaling plot of the order parameter for lattices with pbc. The solid line describes the predicted asymptotic large-$x$ behavior given by Eq. (4a) with $B=1.57$ and $\beta=0.312$.

![](./images/813350827686100992_8.jpg)

FIG. 8. Finite-size scaling plots for the low- and high-temperature susceptibilities for lattices with pbc. The solid lines describe the predicted large-$x$ behavior given by Eq. (4b) with $C^{+}=1.058$ and $C^{-}=0.195$ and $\gamma=\gamma^{+}=\gamma^{-}$$=1.25$. The dashed line is a best fit to the data with $C^{-}=0.155$.

specific heat of an infinite lattice is well described by$^{14}$
$$
C / R=A^{ \pm} t^{-\alpha_{+}} b^{ \pm}, \quad(11)
$$
where the nonsingular part approximated by the constants $b^{ \pm}$cannot be neglected. Using the series-expansion estimates$^{14}$ $b^{+}=-1.242, A^{+}=1.136$, we find that the singular portion of the high-temperature specific heat $(C / R-b^{+})$ scales quite well and, as shown in Fig. 9, agrees with the predicted large-$x$ scaling form. For $T<T_{c}$, however, there are again uncertainties in the asymptotic critical form. Baker and Gaunt$^{12}$ estimated $A^{-}=8.16 \pm 0.2$ but this was based upon a value of $\alpha^{-}=\frac{1}{16}$. In addition, the background term $b^{-}$was not given. In Fig. 9 we see that if $b^{-}$is set to zero and the value $\alpha^{-}=\frac{1}{8}$ is chosen that the data do not scale. The large-$N$ data lie instead systematically above the small-$N$ data. As $b^{-}$becomes more negative the data for all $N$ values begin to approach a single curve. For $-4.0 \leqslant b$ $\leqslant-2.0$ the data scale equally well. For $b^{-} \leqslant-4.0$ the tendency for the large-$N$ data to fall below the small-$N$ data begins to appear. With the "central" value $b^{-}=-3$, however, $(C / R-b^{-})$ scales quite well yielding an asymptotic slope $=\alpha^{-}=\frac{1}{8}$ and an amplitude $A^{-}=3.2 \pm 0.9$. This value of $A^{-}$yields a ratio $A^{-} / A^{+}=2.8 \pm 0.8$ which is significantly greater than other estimates. The renormalization-group estimate $^{15}$ obtained to lowest order by $n$ and $\epsilon$ expansions yields $A^{-} / A^{+}$ $\approx 1.83$; and using series expansions Fisher and Tarko $^{16}$ found that the ratio of the correlation function amplitudes (which one expects to be the same as the specific-heat amplitude ratio) is $1.61 \pm 0.06$. In addition, Barmatz et al. $^{17}$ have recently emphasized that Eq. (11) is correct only to lowest order and that from a thoroughgoing scaling viewpoint one should use the corrected expression
$$
C / R=A^{ \pm} t^{-\alpha}\left(1+D^{ \pm} t^{\star}\right)+b^{ \pm}, \quad(12)
$$
where $b^{+}=b^{-}$! If we adopt the constraint $b^{-}=b^{+}$ $=1.242$, we find that $A^{-}=1.93 \pm 0.08$. The ratio $A^{-} / A^{+}=1.70 \pm 0.07$ now agrees well with other estimates.

![](./images/813350827686100992_9.jpg)

FIG. 9. Finite-size scaling plot for the singular part of the specific heat $(C / R-b^{*}=-1.242$, the lower plot for $T<T_{c}$.

### C. Surface finite-size scaling
Similar plots of the free-edge data showed that the scaled data all lie on single smooth curves, but tests of the surface contribution can be obtained only by analyzing the difference between data points and the infinite lattice values as outlined in Eqs. (5a)-(5c). In Fig. 10 the surface contribution to the magnetization is analyzed in a finite-size scaling plot. The solid line has the theoretically predicted slope $\beta_{s}=\beta-\nu$. The data are consistent with the predicted asymptotic behavior with $B_{s}=2.3 \pm 0.2$ but only over a very narrow range of $x$. For $x \leqslant 2.8$ additional correction terms

![](./images/813350827686100992_10.jpg)

FIG. 10. Finite-size scaling plot for the correction to bulk behavior of the magnetization for lattices with free edges. The solid line shows a best fit to the data using the predicted surface contribution $B_{s} x^{-\beta_{s}}$ with $\beta_{s}=\beta-\nu$ and yielding $B_{s}=2.3 \pm 0.2$.

![](./images/813350827686100992_11.jpg)

FIG. 11. Finite-size scaling plot for the correction to bulk behavior of the susceptibility for lattices with free edges. The solid lines show best fits to the data using predicted surface contributions $C_{s}^{+} x^{-\gamma_{s}}$ where $\gamma_{s}=\gamma_{s}^{+}$ $=\gamma_{s}^{-}=\gamma+\nu$ yielding $C_{s}^{+}=1.4 \pm 0.2$ and $C_{s}^{-}=1.8 \pm 0.2$.

become important. By comparison, the deviation from asymptotic behavior due to finite-size cor- rections alone in the pbc data dis not occur until $x \lesssim 0.5$ (see Fig. 7). The corrections to the susceptibility both above and below $T_{c}(\infty)$ are analyzed in a finite-size scaling plot in Fig. 11. Above $T_{c}$ the data obey finite-size scaling quite well with an asymptotic slope equal to $\gamma_{s}=\gamma+\nu$ and amplitude [Eq. (5b)] $C_{s}^{+}=1.4 \pm 0.2$. Below $T_{c}$ the situation is complicated by the uncertainty in the asymptotic infinite-system amplitude $C^{-}$. Taking $C^{-}=0.155$ as determined from our pbc data in Fig. 8, we find reasonable agreement with the predicted asymptotic slope and an amplitude $C_{s}^{-}=1.8 \pm 0.2$. Use of the series-expansion value $C^{-} \approx 0.195$ would lower the large- $x$ points, thus tending to increase the asymptotic slope. In any case it is clear that the surface contribution to the susceptibility is much more symmetric than the bulk susceptibility itself, i.e., $C_{s}^{+} \approx C_{s}^{-}$ while $C^{+} \approx 6 C^{-}$.

Because of the uncertainty in both $A^{-}$ and $b^{-}$ we have not analyzed the low-temperature specific heat. Above $T_{c}$, however, since both $A^{+}$ and $b^{+}$ are well known from series expansions a good test of the finite-size scaling of the surface contribution can be made. The result, shown in Fig. 12, indicates that the correction to the bulk specific heat is well described by the surface contribution with $\alpha_{s}=\alpha+\nu$ and amplitude $A_{s}^{+}=0.85$ $\pm 0.10$.

### D. "Rounding" in critical phenomena

The results obtained in the previous sections can also be said to shed light on the "rounding" observed in the critical behavior of real magnetic systems. The data on lattices with pbc describe the effect of finite size alone. We have already seen that "rounding" or deviations from the asymptotic large-lattice behavior become evident when the scaling variable $x$ is less than a minimum value $x_{c}$ but in all cases $x_{c} \approx 1$. In order for rounding due to finite size to become visible for $t \lesssim 10^{-3}$, the system size must be smaller than $N=(x_{c} / t)^{\nu}=83$. In a real crystal with lattice spacing $a_{0}=5 \AA$ this would imply that grain sizes of $\sim 400 \AA$ or less would have to be typical in order to account for rounding. Such small grains are highly unlikely; moreover, pbc are certainly unphysical. Although grain boundaries will not be completely independent of neighboring grains, the assumption of free edges should be a more realistic approximation. For $x>x_{c}$ the bulk terms in Eqs. (5a)-(5c) reproduce the infinite-lattice critical behavior. The second, or surface, terms behave differently and must be small or the total result will differ from the asymptotic critical form. Using the amplitudes found in the previous section we find that the values of $x$ for which the surface terms are less than $1 \%$ of the bulk terms are much larger than $x_{c}$ and are on the order of $2.5 \times 10^{3}$. With $t=10^{-3}$ this now means that $N<12000$ rounding will appear due to the surface contribution. For $a_{0}=5 \AA$ this implies a grain size of $\sim 6 \mu \mathrm{m}$, which is quite reasonable. (A value of $N \sim 2800$ would now produce rounding at $t=10^{-2}$.) This effect would be qualitatively similar to that which can be simulated $^{18}$ by assuming a Gaussian distribution of $T_{c}$'s in microcrystals where each grain obeys

![](./images/813350827686100992_12.jpg)

FIG. 12. Finite-size scaling plot for the correction to bulk behavior of the high temperature specific heat for lattices with free edges. The solid line is a best fit to the data using the predicted surface contribution $A_{s}^{+} x^{-\alpha_{s}}$ where $\alpha_{s}=\alpha+\nu$ yielding $A_{s}^{+}=0.85 \pm 0.10$.

the infinite-lattice critical form but with a shifted $T_c$. Our data also show that each different grain size will have a different $T_c$ but that all $T_c$'s will be shifted below $T_c(\infty)$ rather than being symmetrically distributed. These shifts will still be quite small since the asymptotic size dependence of $T_c(N)$ yields $\delta T_c=1.3 \times 10^{-4}$ for $N=1000$. Note, however, that only the very large grains would effectively follow the infinite-lattice critical form. The others would be rounded by the surface contribution. Although this model is clearly oversimplified, the surface contribution will probably be larger in real systems. Since grains will not have perfectly smooth sides, the fraction of spins which are in the "surface" will be substantially greater than for $N \times N \times N$ cubes and the rounding will be magnified correspondingly. More distant than nearest-neighbor exchange and dipolar coupling will also increase the effect. Surface effects could therefore be at least in part responsible for experimentally observed rounding.

## IV. SUMMARY AND CONCLUSION
The data which have been presented here show that the finite-size scaling theory developed by Fisher describes the size behavior of the simplecubic Ising lattice. Since $\nu^{-1} \neq 1$ we have been able to decide between $\lambda=1$ and $\lambda=\nu^{-1}$; a decision which was not possible in two dimensions where $\nu=1$. For lattices with pbc simple corrections to bulk behavior are well described in the asymptotic large-$N$ limit using infinite-lattice exponents and amplitudes. The range of the scaling variable $x=t N^{1 / \nu}$ over which the asymptotic form is followed is considerably smaller than for the square lattice (e.g., for the order parameter $x \approx 0.2$ is the limiting square-lattice value, whereas here $x \approx 0.5$ is appropriate). For lattices with free edges, the corrections to the bulk critical behavior are well described by surface exponents predicted from finite-size scaling theory. Surface amplitudes have also been determined and, in the case of the susceptibility, the high- and lowtemperature surface amplitudes are found to be much more symmetric than the bulk amplitudes. The variation of $T_c$ with $N$ for lattices with free edges suggests that the lowest-order correction to scaling for $\xi$ in the infinite lattice is $\sim t^{0.5}$ rather than $\sim t^{1.0}$. We have also presented evidence that the rounding in real systems may be due to the surface contributions to grain behavior. Finite-size scaling makes equivalent predictions for both cubic-shaped systems as well as for thin films and the probability that $\lambda$ is different in these two cases is quite small. Our present results then also imply that the shift exponent for thin Ising films is $\lambda=\nu^{-1}$. This result has already been checked by direct study. $^{19,20}$ We conclude then that the finite-size behavior in all two- and threedimensional Ising systems is well understood.

## ACKNOWLEDGMENTS
We wish to thank Professor K. Binder, Professor M. E. Fisher, and Professor R. Bausch for helpful discussions and suggestions. We are also indebted to the Alexander von Humboldt Foundation for their support and the Universität des Saarlandes for their hospitality during a portion of the time this work was being carried out.

*Supported in part by the the National Science Foundation
$\dagger$Permanent address.
${ }^{1}$ M. E. Fisher, Proceedings of the International Summer School "Enrico Fermi," Course LI (Academic, New York, 1971); see also M. E. Fisher and M. N. Barber, Phys. Rev. Lett. $\underline{28}, 1516$ (1972).
${ }^{2}$ The scaling theory was originally expressed in terms of the variable $t=\left[T-T_c(N)\right] T_c(\infty)$, where $T_c(N)$ is the "pseudotransition" temperature of a finite lattice. Since an analysis of our data in terms of $t$ would introduce an additional error due to the uncertainty in $T_c(N)$, we have adopted the alternative formulation proposed by Fisher in Ref. 1.
${ }^{3}$ Because of the recent use of $\epsilon$ as $4-d$ in renormalization-group " $\epsilon$ expansions" we have adopted the newer convention which uses $t$ instead of $\epsilon$ to denote the reduced "distance" from $T_c$.
${ }^{4}$ M. E. Fisher and A. E. Ferdinand, Phys. Rev. Lett. 19, 169 (1967); A. E. Ferdinand and M. E. Fisher, Phys. Rev. $\underline{185}, 832$ (1969).
${ }^{5}$ D. P. Landau, Phys. Rev. B 13, 2997 (1976).
${ }^{6}$ K. Binder, Physica $\underline{62}, 508$ (1972).
${ }^{7}$ K. Binder and P. C. Hohenberg, Phys. Rev. B $\underline{9}, 2194$ (1974).
${ }^{8}$ J. W. Essam and M. E. Fisher, J. Chem. Phys. $\underline{38}, 802$ (1963).
${ }^{9}$ The susceptibility determined here from the fluctuations is the "reduced quantity,"
$$
\begin{aligned}
\chi & =\left(\left\langle\left(\sum_{i}^{N} \sigma_{i}\right)^{2}\right\rangle-\left\langle\sum_{i}^{N} \sigma_{i}\right\rangle^{2}\right) / N k T \\
& =N^{-1} \sum_{i}^{N} \sum_{j}^{N}\left(\left\langle\sigma_{i} \sigma_{j}\right\rangle-\left\langle\sigma_{i}\right\rangle^{2}\right).
\end{aligned}
$$

Since the observation time for our experiments is quite short compared to the time required for the entire lattice to overturn, $\left\langle\sum_{i} \sigma_{i}\right\rangle^{2}$ is nonzero and remains finite below $T_c$.
${ }^{10}$ D. M. Saul, M. Wortis, and D. Jasnow, Phys. Rev.

B 11, 2571 (1975).

¹¹M. F. Sykes, D. S. Gaunt, P. D. Roberts, and J. A. Wyles, J. Phys. A 5, 667 (1972).

¹²G. A. Baker, Jr. and D. S. Gaunt, Phys. Rev. 155, 545 (1967).

¹³J. W. Essam and D. L. Hunter, J. Phys. C 1, 392 (1968).

¹⁴M. F. Sykes, D. L. Hunter, D. S. McKenzie, and B. R. Heap, J. Phys. A5, 667 (1972).

¹⁵E. Brézin, J. C. LeGuillou, and J. Zinn-Justin, Phys. Lett. A 47, 285 (1974).

¹⁶M. E. Fisher and H. B. Tarko, Phys. Rev. B 11, 1131 (1975).

¹⁷M. Barmatz, P. C. Hohenberg, and A. Kornblit, Phys. Rev. B 12, 1947 (1975).

¹⁸See, for example, R. Wielinga, thesis [Kamerlingh Onnes (Paris) Laboratorium, 1968] (unpublished); D. P. Landau, J. Phys. Suppl. (Paris) 32, C1-1013 (1971); R. J. Birgeneau, H. J. Guggenheim, and G. Shirane, Phys. Rev. B 8, 304 (1973).

¹⁹K. Binder, Thin Solid Films 20, 367 (1974).

²⁰The form of the finite-size scaling function for the sus- ceptibility of Ising thin films has been studied by T. Weston Capehart, Masters thesis (Cornell Univ., 1975) (unpublished); T. W. Capehart and M. E. Fisher, Phys. Rev. B 13, 5021 (1976).