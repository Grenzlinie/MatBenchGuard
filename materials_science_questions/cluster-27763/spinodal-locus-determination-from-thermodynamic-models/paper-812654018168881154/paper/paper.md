![](./images/812654018168881154_1.jpg)

Critical properties of the self-consistent Ornstein-Zernike approximation for three-dimensional lattice gases with varying range of interaction

A. Borge and J. S. Høye

Citation: *J. Chem. Phys.* **108**, 4516 (1998); doi: 10.1063/1.475863
View online: http://dx.doi.org/10.1063/1.475863
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v108/i11
Published by the American Institute of Physics.

---

Additional information on *J. Chem. Phys.*
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/812654018168881154_2.jpg)

# Critical properties of the self-consistent Ornstein–Zernike approximation for three-dimensional lattice gases with varying range of interaction

A. Borge and J. S. Høye
Institutt for fysikk, NTNU, N-7034 Trondheim, Norway

(Received 9 July 1997; accepted 9 December 1997)

The self-consistent Ornstein–Zernike approach (SCOZA) is solved numerically, and its properties in the critical region are investigated for the lattice gas or Ising model in three dimensions. We especially investigate how critical properties depend upon the inverse range of interaction. We find effective critical indices that depend upon this range. However, the SCOZA does not fulfill scaling. Nevertheless, comparing with experimental results for fluids and magnets we find good agreement. Away from the critical point we find that SCOZA yields deviations from scaling that seem similar to experiments. © 1998 American Institute of Physics. [S0021-9606(98)50211-5]

## I. INTRODUCTION

Recently Dickman and Stell succeeded in numerically solving the self-consistent Ornstein–Zernike approach (SCOZA) partial differential equation such that a well-defined solution was also obtained below the critical temperature $T_c$ where one has phase coexistence.¹ They considered the Ising model or the equivalent lattice gas in three dimensions with nearest-neighbor interactions. A striking feature of their results was the accuracy with which the best estimates for Ising model thermodynamics were approximated for the three possible types of cubic lattices. This accuracy is present both in the values of $T_c$, which were within 0.2% of such estimates, as well as the general behavior in the critical region with effective critical exponents close to the best analytic estimates.

The critical region has been an especially complicated region to treat more accurately by statistical mechanics. Usually theories have been restricted to various types of mean-field or Van der Waals-like theories. In this way density fluctuations that are important and crucial in the critical region have been neglected. Thus mean-field theories are most inaccurate in this region, and they are in no way able to capture the singular behavior experienced by thermodynamic quantities as the critical point is approached. This singular behavior is again connected to the correlation length that grows to infinity.

New insight and major progress towards understanding the mechanism of critical behavior was obtained by Widom² and Kadanoff³ by introduction of homogeneity from which the well-known scaling relations followed. Further on, renormalization group methods were introduced by Wilson,⁴ after which Wilson and Fisher⁵ showed how quantitative predictions of critical exponents could be obtained as expansions in $4-d$ where $d$ is dimension.

However, globally more accurate treatments of systems at thermal equilibrium have been less developed. But some work has been performed as was done by one of the authors in his thesis.⁶ This work was based on the $\gamma$ ordering for long-range forces that was used by Hemmer⁷ and by Lebowitz *et al.*⁸ to obtain corrections to the well-known Van der Waals equation of state for fluids. From this study it became clear that corrections to mean-field theory (or here a three-dimensional version of Van der Waals equation) beyond the usual high-temperature contribution were relatively small except in a region around the critical point where corrections due to the finite range of interaction would be crucial. A notable problem with the critical point is its singular nature such that corrections to mean field tend to diverge. To some extent this was rectified by a resummation or renormalization of the leading contribution beyond mean field. In this way results that quantitatively compared well with experimental results for Ar were obtained using the Lennard–Jones potential. However, close to the critical point remaining thermodynamic inconsistencies were crucial in the sense that isotherms became ‘‘irregular’’ by which, for instance, the gas–liquid phase equilibrium no longer remained well defined. But nevertheless, extrapolation of results towards the critical point indicated a critical index $\beta \approx 1/3$ for the phase equilibrium while the one for the critical isotherm was $\delta \approx 5$.

For the lattice gas it later became clear⁶ that the resummed $\gamma$ ordering above was essentially the MSA (mean spherical approximation). Thus the critical properties were those of the MSA. However, the MSA result is less satisfactory in the latter case with nearest-neighbor interaction. In the view of the above analysis this can be understood from the correction to mean field. For the Lennard–Jones fluid the lowering of $T_c$ was less than 10% compared to the $T_c$ from the high-temperature result while the lattice gas case yields a lowering of 34% for the simple cubic lattice. That is corrections and thus inconsistencies will be considerably larger in the latter case.

The MSA for fluids and modified versions of it were studied extensively by Chandler *et al.*,⁹⁻¹² and accurate results were obtained outside the critical region. However, critical properties remained mean-field-like. This is the case with MSA for continuum fluids which is thermodynamicly inconsistent in such a way that the divergence of the correlation function will take place inside the two-phase region from the energy route and not at the critical point itself. Further various integral equations methods have been devel-

oped and refined to describe fluids. $^{13}$ Høye and Stell then proposed to apply thermodynamic self-consistency in con- nection with the MSA solution for fluids. $^{14}$ Further they fully developed equations necessary for solving the self- consistency problem. Preliminary numerical results sug- gested that the SCOZA approach might yield rather accurate thermodynamic results, $^{15}$ which recently was verified. $^{1}$ The high accuracy actually found may be surprising. But as ar- gued by Høye and Stell $^{16}$ there is reason to believe that this accuracy partly can be connected to the fact that in three dimensions the critical index $\eta$ for the correlation function is close to zero. Thus the spatial dependence of the assumed MSA form of the correlation function is close to the exact correlation function too. So the main defect of the MSA itself is apparently its thermodynamic inconsistency which is remedied by the SCOZA.

Recently another theory of global accuracy has also ap- peared. This is the hierarchical reference theory (HRT) of Parola and Reatto. $^{17,18}$ This theory is based on renormaliza tion group ideas that build in scaling, but is not self- consistent in our sense. However, it results in a similar nu- merical problem of solving a nonlinear partial differential equation of diffusion type.

In view of the accuracy of the results obtained $^{1}$ we found reason to believe that SCOZA will yield accurate informa- tion about properties in the critical region too as there is not much room for corrections due to higher-order perturbing terms. As is already clear, the SCOZA will not yield exact critical indices very close to the critical point. However, away from this very small region there seems to be an effec- tive critical behavior near the exact one as reported. $^{1}$ One purpose of this work is to investigate this more closely by performing more accurate and detailed evaluations especially in the critical region. Another purpose is to investigate the effect upon critical properties when varying the range of in- teraction. According to $\gamma$ ordering, results should be more accurate and reliable the smaller the inverse range of inter- action is.

In view of standard scaling theory we understand that critical properties are expected to be independent of the range of interaction, i.e., they are universal. However, the preliminary SCOZA results indicated that effective critical exponents were sensitive to interaction range. For example, by comparing the results of Refs. 1 and 15 one got an indi- cation that the effective supercritical index $\gamma$ for the inverse susceptibility had such a behavior as results obtained dif- fered. Also some previous unpublished numerical work by one of the authors in connection with a student project indi- cated the same. $^{19}$ In this latter case the continuum fluid with Yukawa interaction whose range could be varied was con- sidered. By the more precise and accurate evaluations per- formed here we actually find such a dependence upon the range of interaction. This sensitivity to interaction range for effective exponents may be related to the expected crossover behavior as one approaches the critical point, with the cross- over occurring at a ‘‘Ginzburg temperature’’ that dependsupon the sixth power of the inverse potential range $\gamma_{r} \cdot^{20-22}$  That is, inside this crossover temperature which turns out to be very small, our results indicate universal behavior while outside effective critical exponents vary.

In Ref. 15 the presence of scaling solutions of the SCOZA were shown. However, the results of Ref. 1 were not in accordance with these as the index $\gamma$ approached the MSA value 2 and not the scaling value 1 close to $T_{c}$ . Thus the boundary conditions of the SCOZA are in conflict with the family of possible scaling solutions. Later analytic work byHøye et al. $^{33}$ shows the presence of a solution with index $\gamma$ =2 where scaling is not present. What seems to happen is that the true solution approaches the trivial scaling solution that does not contain temperature and is thus nothing but the critical isotherm near the critical density.

In Sec. II we sketch the SCOZA theory, and in Sec. III we discuss the numerical method. In Sec. IV we discuss numerical results for critical indices while in Sec. V results for the equation of state and its deviations from scaling are discussed. We have evaluated the various critical indices for thermodynamic quantities and our results are presented in the figures. The indices, defined as slopes of curves in log- log plots, are evaluated for various ranges of interaction. Also the equation of state with scaled variables is evaluated and then compared with experimental results for fluids and magnets. Although SCOZA does not scale it turns out to be close to scaling in the part of the critical region usually cov- ered by experimental results. This is also the region best described by effective exponents. In fact a closer examina- tion of the experimental results indicate a similar deviation from scaling. That is the nonscaling properties of SCOZA seem to describe the exact behavior in a way that goes be- yond previous descriptions. However, deviations from and corrections to scaling are nothing new as considerable effort has been devoted to this to describe properties close to the critical point. $^{23,24}$ Furthermore, crossover has been studied by Fisher $^{25}$ and by Bagnuls and Bervillier $^{26}$ using renormaliza tion group methods while Anisimov et al. $^{27}$ have used a phe nomenological approach, Mon and Binder $^{28}$ have performed Monte Carlo simulations, and Parola and Reatto $^{17}$ have used a liquid-state theory.

## II. THEORY
As mentioned in the Introduction SCOZA builds upon the MSA by combining it with thermodynamic self- consistency where one can utilize the thermodynamic rela- tion

$$\frac{\partial\left(\beta \chi^{-1}\right)}{\partial \beta}=\frac{\partial^{2}(\rho u)}{\partial \rho^{2}},\qquad(1)$$

where $\rho \chi^{-1}$ is the inverse compressibility $\partial p / \partial \rho$ . Here $\beta$  $=1 / k_{B} T, p$ is the pressure, $\rho$ is the density, and u is the average energy per particle which has a contribution of mean-field form $u_{0}=-(q / 2) \rho$ and a contribution from cor relations $u_{1}$ .

$$u=u_{0}+u_{1}.\qquad(2)$$

Here we incorporate the coordination number $q$ as used in Ref. 1. For the Ising model $\rho$, $\chi^{-1}$, $\rho u$, and $\rho u_{0}$ are replaced by $\frac{1}{2}(1+m)$, $\partial H/\partial m$, $U$, and $U_{0}=-(1/2)m^{2}$ as done in Ref. 15.

For an interaction $-\psi(\mathbf{r})$ the SCOZA pair correlation function $h(\mathbf{r})$ has Fourier transform
$$
1+\rho \widetilde{h}(\mathbf{k})=\frac{1}{1-\rho \widetilde{c}(\mathbf{k})}, \tag{3}
$$
where the direct correlation function $\widetilde{c}(\mathbf{k})$ is assumed to be of MSA form
$$
\widetilde{c}(\mathbf{k})=c_{0}+c_{1} \widetilde{\psi}(\mathbf{k}). \tag{4}
$$

Equation (3) is nothing but the Fourier transform of the usual Ornstein-Zernike equation. Approximation (4) for $c(\mathbf{r})$ or its Fourier transform $\widetilde{c}(\mathbf{k})$ is of Ornstein-Zernike form assuming $c(\mathbf{r})$ to be of a range corresponding to the range of the potential. (This relation to Ornstein-Zernike$^{29}$ theory explains the name SCOZA of our approach.) At the same time we utilize the MSA form to define $\widetilde{c}(\mathbf{k})$ explicitly except for $c_{1}$ which is determined by thermodynamic self-consistency via Eq. (1) that yields Eq. (12) below. As in Ref. 1 we normalize $\psi(\mathbf{r})$ such that $\widetilde{\psi}(0)=q$. The core condition $h(0)=-1$ then implies
$$
1-\rho=\frac{1}{(2 \pi)^{3}} \int(1+\rho \widetilde{h}(\mathbf{k})) d \mathbf{k}=\frac{1}{1-\rho c_{0}} P(z), \tag{5}
$$
where
$$
P(z)=\frac{1}{(2 \pi)^{3}} \int \frac{d \mathbf{k}}{1-z \widetilde{\psi}(\mathbf{k}) / q} \tag{6}
$$
with
$$
z=\frac{\rho c_{1} q}{1-\rho c_{0}}=\frac{q \rho(1-\rho) c_{1}}{P(z)}. \tag{7}
$$

From the pair correlation function one can now obtain the equation of state in two different ways. First the internal energy due to correlations becomes
$$
\begin{aligned}
\rho u_{1} & =-\frac{1}{2} \frac{1}{(2 \pi)^{3}} \int\left(\rho+\rho^{2} \widetilde{h}(\mathbf{k})\right) \widetilde{\psi}(\mathbf{k}) d \mathbf{k} \\
& =-q \rho(1-\rho) F(z), \tag{8}
\end{aligned}
$$
where by use of Eqs. (5) and (7)
$$
F(z)=\frac{P(z)-1}{2 z P(z)}. \tag{9}
$$

Second, from the compressibility relation we further get
$$
\beta \chi^{-1}=\frac{1}{\rho}(1-\rho \widetilde{c}(0))=\frac{\epsilon^{2}}{\rho(1-\rho)}, \tag{10}
$$
where with (5) and (7) $[\widetilde{c}(0)=c_{0}+q c_{1}]$
$$
\epsilon^{2}=(1-z) P(z). \tag{11}
$$

The SCOZA partial differential equation now follows by inserting (8), (2), and (10) into (1) to obtain
$$
\frac{\partial \epsilon^{2}}{\partial \beta}=-q \rho(1-\rho)\left\{1+\frac{\partial^{2}}{\partial \rho^{2}}[\rho(1-\rho) F(z)]\right\}. \tag{12}
$$

The solution of this equation along with relations (6), (9), and (11) will determine the parameter $c_{1}$ in Eq. (4) and all other quantities of interest in Eqs. (2)-(11) above. This also includes the pair correlation function $h(\mathbf{r})$ [or $\widetilde{h}(\mathbf{k})$] in Eq. (3). Note that the whole influence of the pair interaction, besides the mean-field piece $u_{0}$, goes via the function $P(z)$ as given by Eq. (6) which is not restricted to dimensionality three as studied here.

## III. NUMERICAL SOLUTION

The preliminary SCOZA results reported by Høye and Stell in Ref. 15 were limited to supercritical temperatures as the problem of going below the critical temperature $T_{c}$ turned out to be nontrivial. The SCOZA equation is mathematically equivalent to a highly nonlinear diffusion process which becomes seriously instable by numerical solution when one tries to go below $T_{c}$. The reason is that the $\epsilon$ in Eqs. (10) and (12) goes towards zero at the critical point and continues to stay at this value along the on beforehand unknown spinodal curve below $T_{c}$. Close to $\epsilon=0$ the $F(z)$ is linear in $\epsilon$ (not $\epsilon^{2}$) due to the singular nature of integral (6) when $z \to 1$. From Eq. (12) this means that one will have a diffusion constant $D \sim 1 / \epsilon \to \infty$ which creates numerical problems along an unknown curve, inside which the equation will be invalid.

Originally we started our numerical work by using the form of the SCOZA equation established in Ref. 15. There a quantity $S$, that is essentially Helmholtz free energy, was used as the quantity to solve for. In terms of $S$ the $\epsilon^{2}$ used here is essentially its second derivative $\partial^{2} S / \partial \rho^{2}$. By numerical differentiation errors in $S$ amplify seriously when one also takes the square root to obtain $\epsilon$ near the spinodal $\epsilon=0$. Although we otherwise developed a stable numerical procedure the determination of the spinodal did not stabilize as far as we went. In the meantime the numerical results of Ref. 1 were obtained. The crucial step taken in this work was to use Eq. (1) as basis for the SCOZA equation instead of relating $u$ and $\chi$ via Helmholtz free energy and its derivatives. In this way the $\epsilon$ comes out directly from solution, not via a second derivative, and the determination of the spinodal $\epsilon=0$ becomes a stable procedure, although care has to be shown.

The numerical procedure used in Ref. 1 was not stable unless very small steps in $\beta$ direction were used. To rectify this Pini developed an unconditionally stable, accurate, and efficient numerical procedure based on previous experience in related work using a predictor-corrector method. $^{18,30}$ Our continued work is thus based directly upon programs developed by Pini. Then we solved Eq. (12) with respect to $\rho u_{1}$ as given by (8) expressing other quantities in Sec. II including the derivatives of Eq. (12) in terms of it by numerical tabulation in the general case. [However, $\rho u_{1}$ and $\epsilon$ are essentially the same and no separate tabulation is required when using expression (13) below.] To obtain accurate results close to the critical point we had to show special care in order to keep accuracy high.

![](./images/812654018168881154_3.jpg)

FIG. 1. Effective critical index $\gamma$ for the susceptibility along the critical isochor versus $\log_{10}t$ where $t=1-T_{c}/T$. The different curves correspond to $\gamma_{r}^{3}$ values $10^{-3}$, $10^{-2}$, 0.1, 0.2, 0.3, 0.34, 0.4, 0.5, 0.6, 0.7, and 0.8, respectively, starting with the lower dashed curve for $10^{-3}$. The solid line $\gamma=1$ is the mean-field result $\gamma_{r}\to0$ (i.e., we used $\gamma_{r}^{3}=10^{-6}$ to run the program). In Figs. 2–6 below the same set of $\gamma_{r}^{3}$ values (including $\gamma_{r}\to0$) and corresponding dashed curves are used. (The $\gamma_{r}$ is the inverse range parameter.)

The properties of the function $F(z)$ follow from the interaction and depend crucially on its range and dimensionality. With inverse range $\gamma_{r}$ the latter can be written as $\psi(r)=\gamma_{r}^{3}f(\gamma_{r}r)$. Its Fourier transform is $\widetilde{\psi}(k)=\widetilde{f}(k/\gamma_{r})=a - b(k/\gamma_{r})^{2}+\cdots$ in the continuum case. In the lattice case this will be modified slightly as integration is replaced by summation. Inserted in (6) this $\widetilde{\psi}(k)$ ($\widetilde{\psi}(0)/q=1$) by integration yields $F(z)\sim P(z)-1=\gamma_{r}^{3}(A-B\epsilon+\cdots)$ for small $\epsilon\to0$ or $z\to1$ in three dimensions. (The quantities $a$, $b$, $A$, and $B$ are constants.) Thus to simplify during the greater part of our work we approximated the internal energy function (8) by

$$
F(z)=\frac{1}{2}\gamma_{r}^{3}(1-\epsilon). \tag{13}
$$

Here and below we write $\gamma_{r}$ for the inverse range of interaction to distinguish it from the critical index $\gamma$. Via (9) this function approximates integral (6) for $P(z)$ and yields the proper form of its singularity near the critical point at $\epsilon=0$. In addition it immediately incorporates the inverse range of interaction $\gamma_{r}$, the effect of which upon critical properties we want to study. It can be noted that $\gamma_{r}$ is the same as the range parameter $\gamma$ introduced by Uhlenbeck *et al.*$^{31}$ in their works on one-dimensional systems using the Kac potential $\gamma e^{-\gamma|x|}$ to obtain a model that is exactly solvable in the form of an integral equation that was analyzed obtaining Van der Waals equation in the limit $\gamma\to0$. This parameter $\gamma$ was then also introduced in the more general situation considered in Refs. 6–8.

One might think that the precise form of $F(z)$ would be important. But from previous analysis of $\gamma$ ordering$^{6}$ and preliminary numerical work by Pini$^{30}$ we had reason to believe that this was not the case. However, in the present work we also performed detailed SCOZA computations to evaluate effective critical indices using the correct $P(z)$ for nearest-neighbor interaction on the SC lattice as done in Ref. 1. And in accordance with the above assumption the results were near those with $\gamma_{r}^{3}=0.34$. By near we mean that with the choice $\gamma_{r}^{3}=0.3405...$, which gives the SC value $P(1)=1.516...$, the critical temperature was nearly the same (0.7% deviation) and corresponding curves for the various critical indices were essentially the same. (For example, in Fig. 1 the curve for $\gamma$ in the SC case was shifted about a distance 0.2 to the right of the $\gamma_{r}^{3}=0.34$ curve for $t\leq0.1$ and the minimum value for $\gamma$ was lowered about 0.03. On the other hand it nearly coincided the $\gamma_{r}^{3}=0.4$ curve in the same region.) Doing the same for the BCC and FCC lattices gave essentially the same results for the indices although a somewhat smaller $\gamma_{r}^{3}$ would be more appropriate to yield the correct $T_{c}$. That is, details of the pair interaction have minor influence compared with its range, and with respect to critical properties there will be no influence in the qualitative sense. Thus to investigate how effective critical indices depend upon $\gamma_{r}^{3}$ we kept form (13). Clearly it is possible to $\gamma_{r}$ parametrize the correct nearest-neighbor function too.$^{32}$ But we did not do so here as this will not change our conclusions as just argued.

![](./images/812654018168881154_4.jpg)

FIG. 2. Effective critical index $\delta$ for the critical isotherm versus $\log_{10}\Delta\rho$, where $\Delta\rho=|(\rho-\rho_{c})/\rho_{c}|(\rho_{c}=1/2)$ (notation as in Fig. 1).

## IV. NUMERICAL RESULTS

Above $T_{c}$ evaluations were relatively straightforward to perform with high accuracy. For the critical indices $\gamma$ and $\delta$ for the susceptibility at critical density and the critical isotherm, respectively, the asymptotic values 2 and 5 were easily verified.$^{1,33}$ However, away from the critical point one finds effective values and these vary with the $\gamma_{r}^{3}$ parameter, as can be clearly seen from Figs. 1 and 2. Here and below effective critical indices are defined by the logarithmic derivative of the quantity in question. That is, $\alpha=\partial(\log C_{v})/\partial(\log t)$, $\delta=\partial(\log(p_{2}-p_{1}))/\partial(\log\Delta\rho)$, etc. where $C_{v}$ is the configurational specific heat, and $p_{2}$ and $p_{1}$ are the pressures on the critical isotherm at densities $\rho_{2}=\rho_{c}(1+\Delta\rho)$ and $\rho_{1}=\rho_{c}(1-\Delta\rho)$, respectively. For example, the curves for $\gamma$ typically each have a minimum that defines an effective exponent that dominates the critical region except very close to $T_{c}$, i.e., the effective exponent dominates when $t\gtrsim10^{-2}$ for $\gamma_{r}^{3}=0.34$ that is near to the Ising model with nearest-neighbor interaction. Here $t=1-T_{c}/T$ for $T>T_{c}$ while for $T<T_{c}$ we use $t=1-T/T_{c}$. As in Ref. 1 we find $\gamma$ near 1.25 in good agreement with best estimates. Here we find it interesting to note that the best estimate $\gamma\approx1.25$ coincides well with the dominant effective SCOZA $\gamma$ for nearest-neighbor interaction (or $\gamma_{r}^{3}\approx0.34$). However, when $\gamma_{r}^{3}$ is changed the effective $\gamma$ changes too. Thus we find reason to ask ourselves whether this latter nonuniversal behavior is accidental or will estimates for more long-ranged

![](./images/812654018168881154_5.jpg)

FIG. 3. Effective critical index $\alpha$ for the specific heat along the critical isochor versus $\log_{10}t$ where $t=1-T_{c}/T$ (notation as in Fig. 1). (Note $\alpha$ $=1/2$ in the mean-field limit as long as $\gamma_{r}^{3}$ is kept finite by which configurational internal energy $\sim\gamma_{r}^{3}$ is finite.)

interactions also follow effective SCOZA values. As far as we can understand this feature has not been investigated, although the universality hypothesis will say that the true $\gamma$ is fixed. The situation is similar with the exponent $\delta$ as seen in Fig. 2.

In view of the accuracy of SCOZA as shown in Ref. 1 we find reason to expect that this nonuniversal behavior away from the critical point is part of the exact behavior as discussed in Sec. V. But as we do not know about independent investigations in this respect we cannot check to which extent the SCOZA results are correct. Although this behavior is a type of correction to scaling we do not find it directly comparable to previous work. $^{23,24}$

In the way Fig. 1 (and other figures) are presented one may ask why a value of $\gamma$ close to the minimum of the curve can define a dominant effective exponent. The reason is that it represents a stationary point of the slope of the susceptibility versus $t$ on a log-log plot. And restricting the latter to the region $10^{-4.4}\leqslant t\leqslant1$ as done in Ref. 1 one sees almost a straight line that curves somewhat on the end. (That is, $\gamma$ $\approx1.25$ is restricted to $10^{-2}<t<1.$) Our computations have been made accurate much closer to the critical point, however, to capture crossover phenomena for varying $\gamma_{r}^{3}$ and to obtain the SCOZA limiting values that we find independent of $\gamma_{r}^{3}$. Due to this the tiny region more or less unattainable by experiments covers a dominating part of our figures when using logarithmic variables while the easily attainable region where effective exponents vary with $\gamma_{r}^{3}$, is less dominating.

![](./images/812654018168881154_6.jpg)

FIG. 4. Effective critical index $\beta$ for the coexistence curve versus $\log_{10}t$ where $t=1-T/T_{c}$ (notation as in Fig. 1).

![](./images/812654018168881154_7.jpg)

FIG. 5. Effective subcritical index $\gamma'$ for the susceptibility along the coexistence curve versus $\log_{10}t$ where $t=1-T/T_{c}$ (notation as in Fig. 1).

Note that as one might expect, the effective exponents change smoothly into the mean-field behavior as $\gamma_{r}\to0$. How this ‘‘crossover’’ to mean-field behavior takes place more precisely can be seen from the figures. However, for small $\gamma_{r}^{3}$ one generally has MSA behavior for $t\gtrsim c(\gamma_{r}^{3})^{2}$ where $c$ is a constant $(T>T_{c})$. Typically the effective MSA exponents change with $t$ and they become the mean-field ones as $t$ increases. For $t>c(\gamma_{r}^{3})^{2}$ we expect this MSA behavior to be close to the exact result. But for $t\leqslant c(\gamma_{r}^{3})^{2}$ the MSA will be too inconsistent, and modifications from SCOZA become important. These latter, however, are not exact either, but we expect them to represent the exact behavior well as was demonstrated with nearest-neighbor forces. $^{1}$ The condition $t\leqslant c(\gamma_{r}^{3})^{2}$ is also in accordance with the Ginzburg criterion that tells that crossover from mean-field behavior takes place when entering this region. $^{20-22}$ Crossover from mean-field behavior to limiting SCOZA behavior in accordance with this criterion can be clearly seen in Figs. 1–6 for small $\gamma_{r}^{3}$. For larger $\gamma_{r}^{3}$ there is no clear meanfield region that separates out.

The MSA solution
$$\epsilon=-\gamma_{r}^{3}x+\sqrt{\left(\gamma_{r}^{3}x\right)^{2}-2\left(1-\gamma_{r}^{3}\right)x+1}\tag{14}$$
with $x=\frac{1}{2}q\rho(1-\rho)\beta$ follows from Eqs. (7), (9), (11), and (13) with $c_{1}=\beta$ inserted. From (14) follows the MSA critical temperature $(\epsilon=0)T_{c}^{M}=(q/4)(1-\gamma_{r}^{3})$. For the SCOZA critical temperature $T_{c}^{SC}$ we numerically found the shift $T_{c}^{SC}/T_{c}^{M}\approx1+0.9(\gamma_{r}^{3})^{2}$ for $\gamma_{r}^{3}\lesssim0.5$. Also it should be noted from Fig. 1 that in the SCOZA the critical exponent $\gamma$ approaches its asymptotic value 2 much more slowly than in the MSA where it follows from (14). For values of $\gamma\gtrsim1.5$ the ratio between corresponding values of $t$ is about a factor

![](./images/812654018168881154_8.jpg)

FIG. 6. Effective subcritical index $\alpha'$ for the specific heat along the coexistence curve versus $\log_{10}t$ where $t=1-T/T_{c}$ (notation as in Fig. 1).

100. That is in SCOZA $\gamma=2$ is located in a much smaller region by which this asymptotic value of $\gamma$ will have a small influence upon the general accuracy.

Concerning the critical index $\alpha$ for the specific heat it is clear from Fig. 3 and Ref. 1 that it does not follow best estimates so well as the other indices ($\gamma_{r}^{3}=0.34$). This accuracy of $\alpha$ is connected to the way SCOZA in its present form closely ties $\alpha$ to $\gamma$ since for susceptibility we here have $\epsilon^{2} \sim t^{\gamma}$ and for change in internal energy $\epsilon \sim t^{1-\alpha}$ as $t \to 0$. Thus $\alpha=1-\frac{1}{2} \gamma$ by which it varies along with $\gamma$ in a way not dictated by scaling. So this is a clear defect of the SCOZA.

For subcritical temperatures the numerical evaluations are more challenging with respect to accuracy to determine the phase transition once one has a numerically stable procedure. Due to symmetry around $\rho=1 / 2$ it is sufficient to use either equal pressures or chemical potentials for this purpose. We used the former as in Ref. 1 obtaining the pressure $p$ by integration of the susceptibility from both $\rho=0$ and $\rho=1$. (Alternatively one could go via Helmholtz free energy by integration of the internal energy.) To determine the constant of integration one notes that the mean-field result is exact for $\rho=0$ and $\rho=1$. (Due to division by zero one must start integration at neighboring values of $\rho=0$ and $\rho=1$ where analytic exact expansions are also used to maintain desired accuracy.) However, due to numerical inaccuracy (using the Simpson rule) the $p$ values will differ slightly at $\rho=1 / 2$ for $T>T_{c}$ when integrating from both sides. To eliminate this error to which determination of phase equilibrium is very sensitive close to $T_{c}$ we corrected for the difference obtained at $T_{c}$ and kept this correction as an added constant below $T_{c}$. The justification for this is that the error of integration will stay essentially constant as the integrand is almost the same by small changes in temperature near $T_{c}$ where this is important.

Near $T_{c}$ the determination of phase equilibrium turned out very sensitive to numerical accuracy. Thus some of our preliminary values for the critical exponent $\beta$ for the curve of coexistence was misleading. That is, for $t \to 0, \beta \to 1 / 5$ when $\gamma_{r}^{3}>0.5$. This we later found wrong by performing a sensitive check of consistency using the thermodynamic relation for magnetic systems

$$
C_{H}-C_{M}=T\left(\frac{\partial M}{\partial T}\right)_{H}^{2}\left(\frac{\partial H}{\partial M}\right)_{T}, \tag{15}
$$

where the derivatives are taken along the curve of coexistence. With this relation fulfilled the results became acceptable. Close to $T_{c}$ this relation would easily fail especially for larger values of $\gamma_{r}^{3}$. Increasing the number of grid points improved upon this situation. Thus we typically used $10^{3}$ (and in a few cases up to $10^{4}$) grid points for the density in the region from zero density to $\rho_{c}$.

For the effective critical exponents $\beta, \gamma^{\prime}$, and $\alpha^{\prime}$ one from Figs. 4–6 sees that they also vary with $\gamma_{r}^{3}$. Down to $\gamma_{r}^{3} \approx 0.1$ the variation is relatively slow, but from there on the change to mean-field effective exponents is more rapid. As far as the accuracy of our computations went using standard double precision, it seems clear that each of these exponents has a common asymptotic or universal value as $t \to 0$ independent of $\gamma_{r}^{3}$ as long as it is finite. Figs. 4–6 show that these asymptotic values are something like $\beta \approx 0.35, \gamma^{\prime} \approx 1.40$, and $\alpha^{\prime} \approx-0.10$. [These values are related via the usual scaling relation $\alpha^{\prime}+2 \beta+\gamma^{\prime}=2$ that follows from Eq. (15) whenever $C_{H}$ is dominant compared to $C_{M}$.] We find these values interesting especially the one for $\beta$ which is close to best estimates of its exact value. Somehow, for some reason SCOZA tries to aim for something near the exact $\beta$.

Concerning the asymptotic value $\alpha^{\prime} \approx-0.10$ one must expect this to be a defect of SCOZA as a negative $\alpha^{\prime}$ does not seem reasonable as an exact value. Thus the value $\gamma^{\prime}$ $\approx 1.40$, which is connected to $\alpha^{\prime}$ via the scaling relation above, is somewhat large too. However, away from $T_{c}$ the $\gamma^{\prime}$ lowers its value such that more reasonable values for the effective $\gamma^{\prime}$ are then obtained. (Corresponding values obtained by the HRT theory of Ref. 18 are $\beta \approx 0.345$ and $\gamma^{\prime}$ $\approx 1.378$.)

The asymptotic exponents can be given some additional comments. For example, the limiting value $\gamma=2$ itself is no improvement over the MSA value. However, instead the improvement is the major increase in general accuracy such that the asymptotic region with $\gamma=2$ has moved about two decades closer to the critical point as discussed below Eq. (14).

However, for the exponent $\beta$ (and to some extent $\gamma^{\prime}$) the situation is more spectacular as the asymptotic value $\beta$ $\approx 0.35$ is in fact close to best estimates that can vary somewhat depending on approach. $^{23,24}$ Thus the $\beta$ is clearly no longer tied to mean-field and spherical model value $\beta=0.5$. (As indicated in the Introduction the MSA defines no $\beta$, as meaningful phase coexistence is destroyed near $T_{c}$.)

The specific heat exponent $\alpha \to 0.5$ in the mean-field limit $\gamma_{r}^{3} \to 0$ needs a special comment (Fig. 3). The reason for this Gaussian model value is that kinetic energy is not included, and the mean-field configurational energy does not contribute to the specific heat above $T_{c}$. Thus only the correction to it contributes, and from Eqs. (8), (9), and (14) one has $u_{1} \sim \gamma_{r}^{3} \sqrt{t}(\gamma_{r} \to 0)$ or $C_{v} \sim \gamma_{r}^{3} / \sqrt{t}$. So $\alpha=0.5$, but on the other hand $C_{v}$ itself vanishes anyway along with $\gamma_{r}$.

From the viewpoint of scaling it is clearly unsatisfactory that $\gamma \neq \gamma^{\prime}$ and $\alpha \neq \alpha^{\prime}$. However, again this is of most concern in the small asymptotic region close to the critical point where it is clear that SCOZA fails anyway.

The nonuniversal behavior of effective exponents depending upon $\gamma_{r}^{3}$ may look strange and be unexpected in view of scaling. As discussed in Sec. V this may be part of the exact behavior too such that true scaling will be present only very close to the critical point, i.e., for something like $t \leq 10^{-3}$ for real systems.

## V. NONSCALING AND SCALED EQUATION OF STATE

As mentioned in the Introduction the SCOZA does not yield a scaled equation of state in the critical region due to its boundary conditions. Despite this SCOZA seems to yield very accurate results as verified by the results obtained for the three-dimensional Ising model in Ref. 1. Thus we were lead to speculate that somehow the SCOZA would yield something close to a scaling solution in a relatively large region that may fit into experimental results. To do this com-

![](./images/812654018168881154_9.jpg)

FIG. 7. Equation of state for SCOZA with $\gamma_{r}^{3}=0.34$ using scaled variables. Symbols designating the various supercritical isotherms are plotted on the various curves. For $T<T_{c}$ the symbols on the curves have been omitted since the curves are so close together.

parison we chose the $\gamma_{r}^{3}=0.34$ case that gave results close to the ones for the Ising model with nearest-neighbor interaction on the SC lattice. To plot SCOZA results we then introduced scaled variables in Figs. 7 and 8. (These variables were not used in the SCOZA equation itself as it does not scale.) They are
$$
\begin{aligned}
& x=\Delta \rho / t^{\beta}, \\
& y=\Delta p / t^{\delta \beta},
\end{aligned}\qquad(16)
$$
with
$$
\begin{aligned}
& \Delta \rho=\left|\frac{\rho_{c}-\rho}{\rho_{c}}\right|, \\
& \Delta p=\frac{p_{2}-p_{1}}{2 p_{c}},
\end{aligned}\qquad(17)
$$
where $\rho_{1}$ and $\rho_{2}$ are the coexisting densities and $p_{1}$ and $p_{2}$ are the corresponding pressures. (Alternatively we could have used the corresponding chemical potential, or in spin system language the magnetic field, which is fully symmetric around $\rho_{c}$.)

We found experimental results with which to compare in the work by Green $e t a l.^{34}$ where the equation of state for various fluids were plotted using the scaled variables above. With some spreading these points fall along scaling curves, and they represent various isotherms with given deviations from their critical temperatures. Thus the range of $t$ values and $\Delta \rho$ values covered is easily estimated, and the corresponding region (extended somewhat) using the SCOZA results was plotted. From Fig. 7 one sees that isotherms with small separations are obtained, and these lines fall within the experimental points as shown in Fig. 8. The only change from the experimental results in this log-log plot is a minor translation in position which we have performed. Such a shift in position should not be unexpected since we are in fact comparing experimental data for continuum fluids with SCOZA results for lattice gases. Also for the lattice gas considered here we obtained the critical ratio $\beta_{c} p_{c} / \rho_{c}$ $=0.227 \ldots$ which is somewhat lower than usually found experimentally for fluids. The SCOZA results we have drawn with indices $\delta=5$ and $\beta=0.38$ gave the best fit while Ref. 34 used $\beta=0.35$. When the results in Fig. 7 are extended beyond the temperature region considered there, they start to spread markedly on the lower left side. Thus for the region plotted SCOZA yields an equation of state that is close to a scaled equation which would yield two single lines on such a plot.

![](./images/812654018168881154_10.jpg)

FIG. 8. Scaled equation of state for SCOZA with $\gamma_{r}^{3}=0.34$ (dashed curves) compared to experimental results for $\mathrm{CO}_{2}$ (solid curves) taken from Ref. 34. Start and end points of both sets of curves are indicated with symbols corresponding to the actual temperatures (see inset). (The solid curves are somewhat wiggly as they connect various experimental points.)

We have also compared our SCOZA results with experimental results for the magnetic system $\mathrm{Ni}$ that has a FCC structure. $^{35}$ (Thus the extreme anisotropy in the $z$ direction of the Ising model interactions is clearly not present.) In Ref. 35 scaled magnetization $m=M /|t|^{\beta}$ and scaled magnetic field $h=H /|t|^{\beta \delta}$ is used. In Figs. 2(a) and 2(b) of Ref. 35 subcritical and supercritical results, respectively, are plotted on log$\log$ plots. In the subcritical case $m^{2}-m_{0}^{2}$ is plotted as a function of $h / m$ while in the supercritical case $m^{2}$ is plotted as a function of $h / m-h_{0} / m_{0}$. The $m_{0}$ and $h_{0} / m_{0}$ are limiting $t \rightarrow 0$ values of $m$ and $h / m$ in the two cases, and are determined by Fig. 1 of Ref. 35. By suitable choice of parameters we find that the SCOZA results coincide fully with the experimental ones except for a small shift in position. Due to this coincidence we have not drawn here these figures that can be found in Ref. 35. There is quite a bit of flexibility with respect to choice of such parameters as within certain limits a choice of $\gamma_{r}^{3}$ can be compensated by a choice of effective $\beta$ and $\gamma$. For example, we found full agreement with these experimental results with the two sets of choices

$$
\begin{aligned}
& \gamma_{r}^{3}=0.34 \quad \beta=0.371 \quad \gamma=1.33, \\
& \gamma_{r}^{3}=0.25 \quad \beta=0.382 \quad \gamma=1.28,
\end{aligned}
\tag{18}
$$

for $T>T_{c}$, while for $T<T_{c}$ a small deviation beyond experimental uncertainty can be seen. On the other hand the experimental results for Ni for $T>T_{c}$ shown in Fig. 3(b) in Ref. 36, slightly different from those in Ref. 35, agrees fully with the choice of parameters $\gamma_{r}^{3}=0.2, \beta=0.388$, and $\gamma$ $=1.26$. Unlike the results for $\mathrm{CO}_{2}$ presented in Fig. 8 we do not see significant nonscaling in the result for $\mathrm{Ni}$ and similarly the corresponding SCOZA curves are very close together along a single line in the relatively narrow region of temperature and density covered in this case. (Outside this region the SCOZA curves start to diverge somewhat with respect to density.) However, a choice of parameters different from (18) will easily yield curves that spread quite a bit. Also it should be mentioned that the determination of the SCOZA values for $m_{0}$ and $h_{0}$ defined above yield values somewhat different from the dimensionless ones reported in Table I of Ref. 35. For the SCOZA $\left(\gamma_{r}^{3}=0.34\right)$ we find $m_{0} \approx 1.76$ and $h_{0} \approx 2.38$ while from Ref. $35 m_{0}=1.487$ and $h_{0}=1.524$ for the Ising model, and $m_{0}=1.422$ and $h_{0}$ $=1.037$ for Ni. Why especially the value for $h_{0}$ disagrees significantly is unclear (as we recover the mean-field values $m_{0}=h_{0}=\sqrt{3}$ when $\gamma_{r}^{3} \rightarrow 0$ ).

One can ask why SCOZA despite its nonscaling properties nevertheless almost scales in a region with available experimental values. If one follows the shift in isotherms by changing $t$ one notes that first the isotherms are shifted in one direction and then the shift is returned as can be seen from Fig. 7 where the end points of the curves are marked for $T>T_{c}$. Thus this shift goes through a stationary point (like passing through an extremum). Accordingly a whole range of isotherms locate themselves close to a single line. The range of these values for some reason coincides rather well with the one covered by the experimental data used. (For $T<T_{c}$ the situation is similar but cannot be directly seen in Fig. 7 since the curves are already so close together.)

In view of the accuracy demonstrated by $\mathrm{SCOZA}^{1}$ we found reason from the above to speculate whether the type of corrections to scaling present in SCOZA might be present in real fluids too. The plotting made in Ref. 34 assumed full scaling in the region considered such that all deviations from a single line could be regarded as experimental uncertainties. On the basis of our SCOZA results we found it possible that part of these deviations might be related to the nonscaling properties found in SCOZA. Thus we made a closer examination of the experimental data where several isotherms for $\mathrm{CO}_{2}$ were plotted using different symbols. These were not easy to identify in the figure in Ref. 34. However, by scrutinizing it we were able to identify points belonging to the same isotherm. Then for changing $t$ one, in Fig. 8 actually sees (by looking carefully), a clear tendency of the same systematic shift of lines as found above from SCOZA. (That is in Fig. 8 one sees that the various symbols for end points of curves mostly occur pairwise.) Thus it seems that this nonscaling behavior of the SCOZA represents properties of real fluids too away from the critical point. As mentioned in the Introduction corrections to scaling is nothing new and close to the critical point such corrections have been worked out and used to compare with experimental data and to make estimates of critical exponents. $^{23,24}$ However, the specific features exhibited by the SCOZA solution do not seem to have been noticed before.

## VI. CONCLUSION

As demonstrated in Ref. 1 the SCOZA yields accurate results. Its critical properties are such that the equation of state does not scale. Except very close to the critical point this does not seem to be a defect or inaccuracy of the SCOZA but instead seems to represent properties that would be present by an exact treatment too as demonstrated in Figs. 7 and 8. Furthermore, except very close to the critical point this leads to nonuniversal behavior and thus effective critical exponents that vary with the inverse range of interaction as demonstrated by Figs. 1-6. However, very close to the critical point the SCOZA will fail somewhat as the expected full scaling cannot be obtained. But, nevertheless, the SCOZA critical exponents $\delta=5$ and $\beta \approx 0.35$ (as $t \rightarrow 0$ ) are near estimated exact values.

## ACKNOWLEDGMENTS

We are very grateful to Davide Pini for sending us his program for the SCOZA in the lattice gas case and to George Stell for helpful comments.

$^{1}$ R. Dickman and G. Stell, Phys. Rev. Lett. 77, 996 (1996).
$^{2}$ B. Widom, J. Chem. Phys. 43, 3898 (1965).
$^{3}$ L. Kadanoff, Physics (Long Island City, NY) 2, 263 (1966).
$^{4}$ K. G. Wilson, Phys. Rev. B 4, 3174 (1971); K. G. Wilson and J. B. Kogut, Phys. Rev. C 12, 2 (1974).
$^{5}$ K. G. Wilson and M. E. Fisher, Phys. Rev. Lett. 28, 240 (1972).
$^{6}$ J. S. Høye, thesis NTH, 1973.
$^{7}$ P. C. Hemmer, J. Math. Phys. 5, 75 (1964).
$^{8}$ J. L. Lebowitz, G. Stell, and S. Baer, J. Math. Phys. 6, 1282 (1965).
$^{9}$ H. C. Andersen and D. Chandler, J. Chem. Phys. 57, 1918 (1972).
$^{10}$ H. C. Andersen, D. Chandler, and J. D. Weeks, J. Chem. Phys. 57, 2626 (1972).
$^{11}$ H. C. Andersen, D. Chandler, and J. D. Weeks, J. Chem. Phys. 56, 3812 (1972).
$^{12}$ D. Chandler and J. D. Weeks, Phys. Rev. Lett. 25, 149 (1970).
$^{13}$ C. Caccamo, Phys. Rep. 274, 1 (1996).
$^{14}$ J. S. Høye and G. Stell, Mol. Phys. 52, 1071 (1984). See also Sec. IV of J. S. Høye and G. Stell, J. Chem. Phys. 67, 439 (1977).
$^{15}$ J. S. Høye and G. Stell, Int. J. Thermophys. 6, 561 (1985).
$^{16}$ J. S. Høye and G. Stell, Physica A 244, 176 (1997).
$^{17}$ A. Parola and L. Reatto, Phys. Rev. Lett. 53, 2417 (1984); Phys. Rev. A 31, 3309 (1985); A. Parola, A. Meroni, and L. Reatto, Phys. Rev. Lett. 62, 2981 (1989); A. Parola and L. Reatto, Phys. Rev. A 44, 6600 (1991).
$^{18}$ D. Pini, A. Parola, and L. Reatto, J. Stat. Phys. 72, 1179 (1993).
$^{19}$ C. B. Jensen, F. Rinnan, and J. S. Høye (unpublished).
$^{20}$ M. E. Fisher, Phys. Rev. Lett. 71, 3826 (1993).
$^{21}$ R. F. J. Leote de Carvalho and R. Evans, J. Phys.: Condens. Matter 7, L575 (1995).
$^{22}$ V. L. Ginzburg, Sov. Phys. Solid State 2, 1824 (1960).
$^{23}$ D. S. Gaunt and C. Domb, J. Phys. C 3, 1442 (1970).
$^{24}$ J. V. Sengers and J. M. H. Sengers, Annu. Rev. Phys. Chem. 37, 189 (1986).
$^{25}$ M. E. Fisher, Phys. Rev. Lett. 57, 1911 (1986).
$^{26}$ C. Bagnuls and C. Bervillier, Phys. Rev. Lett. 76, 4094 (1996).
$^{27}$ M. A. Anisimov, S. B. Kiselev, J. V. Sengers, and S. Tang, Physica A 188, 487 (1992).

$^{28}$K. K. Mon and K. Binder, Phys. Rev. E **48**, 2498 (1993).

$^{29}$L. S. Ornstein and F. Zernike, Proc. R. Acad. Sci. Amsterdam **7**, 793 (1914).

$^{30}$D. Pini (unpublished); see also W. F. Ames, Numerical Methods for Par- tial Differential Equations (Academic, New York, 1977) pp. 82–86.

$^{31}$M. Kac, G. E. Uhlenbeck, and P. C. Hemmer, J. Math. Phys. **4**, 216 (1963); G. E. Uhlenbeck, P. C. Hemmer, and M. Kac, ibid. **4**, 229 (1963);
P. C. Hemmer, M. Kac, and G. E. Uhlenbeck, ibid. **5**, 60 (1964).

$^{32}$J. S. Høye and G. Stell, J. Stat. Phys. **89**, 177 (1997).

$^{33}$J. S. Høye, G. Stell, and G. Tarjus (unpublished).

$^{34}$M. S. Green, M. Vicentini-Missoni, and J. M. H. Levelt Sengers, Phys. Rev. Lett. **18**, 1113 (1967).

$^{35}$J. S. Kouvel and J. B. Comly, Phys. Rev. Lett. **20**, 1237 (1968).

$^{36}$J. S. Kouvel and D. S. Rodbell, Phys. Rev. Lett. **18**, 215 (1967).