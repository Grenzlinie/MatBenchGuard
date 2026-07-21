![](./images/812402201283526656_1.jpg)

Physica D 107 (1997) 326-329

![](./images/812402201283526656_2.jpg)

# Zero temperature landscape of the random sine-Gordon model

Angel Sánchez $^{a,b,c,*}$, A.R. Bishop $^{a}$, David Cai $^{a}$, Niels Grønbech-Jensen $^{a}$,
Francisco Domínguez-Adame $^{a,c,d}$

$^{a}$ CNLS & T-11, MS B258, Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, USA
$^{b}$ Departamento de Matemáticas, Universidad Carlos III de Madrid, 28911 Leganés, Madrid, Spain
$^{c}$ Grupo Interdisciplinar de Sistemas Complicados, Universidad Carlos III de Madrid, 28911 Leganés, Madrid, Spain
$^{d}$ Departamento de Física de Materiales, Facultad de Físicas, Universidad Complutense 28040 Madrid, Spain

## Abstract
We present a preliminary summary of the zero temperature properties of the two-dimensional random sine-Gordon model of surface growth on disordered substrates. We found that the properties of this model can be accurately computed by using lattices of moderate size as the behavior of the model turns out to be independent of the size above certain length $(\approx 128 \times 128$ lattices). Subsequently, we show that the behavior of the height difference correlation function is of $(\log r)^2$ type up to a certain correlation length $(\xi \approx 20)$, which rules out predictions of $\log r$ behavior for all temperatures obtained by replica-variational techniques. Our results open the way to a better understanding of the complex landscape presented by this system, which has been the subject of very many (contradictory) analyses.

Keywords: Disordered sine-Gordon; Langevin dynamics; Growth models

---

## 1. Introduction
The two-dimensional (2D) random-phase sine-
Gordon model (RsGM) has attracted a lot of attention
after Toner and di Vicenzo [1] introduced the concept
of *super-roughening*. This system has been mainly
studied in connection to surface growth on disor-
dered substrates [2-16], but it is also very relevant
in many other contexts such as vortex-line systems
with random pinning [17], random-field vortex-free
XY models [14], phase degrees of freedom of pinned
charge-density waves [18,19], or Frenkel-Kontorova
models [20]. In addition to its ability to describe many
physical problems of interest, the importance of this
model stems from the fact that the advances made in
its investigation will certainly have far-reaching con-
sequences in understanding the statical and dynamical
landscape of glassy systems in general.

The RsGM is defined by the following hamiltonian:

$$
H = \frac{1}{2} \sum_{\langle i,j \rangle} (\phi_i - \phi_j)^2 - V_0 \sum_i \cos(\phi_i - \phi_i^0), \tag{1}
$$

where $\phi_i$ is a continuous variable on a square lattice,
$\langle i, j \rangle$ stands for nearest neighbors, $V_0$ stands explicitly
for the strength of the pinning potential compared to
that of the stiffness/surface tension term, and $\phi_i^0$ are
*quenched* (i.e., time-independent) uncorrelated ran-
dom variables uniformly distributed in $(0, 2\pi]$. This is
nothing but a generalization of the sine-Gordon model
(sGM), first introduced by Chui and Weeks [21] as

---

*Corresponding author. Address: Departamento de Mate-
máticas, Universidad Carlos III de Madrid, 28911 Leganés,
Madrid, Spain.

0167-2789/97/$17.00 Copyright © 1997 Elsevier Science B.V. All rights reserved
PII S0167-2789(97)00101-2

a continuous version of the solid-on-solid gaussian model (see, e.g., [22]). In this context, the random variable $\phi_i^0$ represents simply deviation from flatness of the substrate on top of which the surface is growing. The equilibrium of the sGM is well known [21,22] and consists of two phases separated by a roughening temperature, $T_R$, above which the periodic term becomes irrelevant in the sense of the renormalization group (RG). Therefore, for $T > T_R$, the surface is rough because the cost of creating steps is strictly zero, whereas for $T < T_R$ the surface is macroscopically flat. In fact, even the nonequilibrium problem has been addressed and it is presently well understood (see [23] and references therein).

As regards the RsGM, the situation is considerably less clear. There is agreement between the different groups in that there must be a roughening temperature $T_R^*$ (which in principle might not coincide with $T_R$) as well, above which the surface ceases to feel the periodic potential, thus behaving exactly like the sGM. The arguments supporting this idea are again related to RG results, and can be briefly stated by saying that temperature renormalization of the sine term should wipe out the disorder. At present, $T_R^*$ is not well determined. The problems arise when $T < T_R^*$, as different techniques yield very different and contradictory results. A good summary of these is contained in [14], but the main point is that RG calculations predict a super-rough low temperature phase (super-rough meaning that the height-difference correlation function $C(r) \sim (\log r)^2$, diverging faster than in the high temperature phase, $C(r) \sim \log r$ if $T > T_R^*$), whereas replica-symmetry breaking calculations yield a quenching of $C(r)$, i.e., it becomes independent of temperature for $T < T_R^*$ and equal to that at $T_R^*$ (of logarithmic type as stated). The available works on this subject [2-14] have not solved this dilemma, and hence our present research is intended to shed some light on these questions.

## 2. Simulation results

We have carried out simulations of the RsGM using Langevin molecular dynamics (see [23] for details), which, at zero temperature, is a fully deterministic procedure that integrates the (overdamped) equations of motion, that read

$$
\dot{\phi}_{i}=\sum_{\langle i, j\rangle}\left(\phi_{i}-\phi_{j}\right)+V_{0} \sum_{i} \sin \left(\phi_{i}-\phi_{i}^{0}\right). \tag{2}
$$

We have simulated systems of different sizes $L \times L$, ranging from $L=32$ to $L=512$ lattice sites. In all cases, we have verified that the final configuration obtained was (statistically) the same independently of the initial conditions. This is a nontrivial question, as the presence of disorder in this system could give rise to glassy behavior, in particular, to the appearance of many different ground states, as well as different basins of attraction for each one of them.

After this satisfactory check, we proceeded to establish which was the dependence on the lattice size. This we show in Fig. 1, where we plot the time evolution of the interface width, defined as $\left\langle\left\langle\left(\phi_{i}-\left\langle\phi_{i}\right\rangle\right)^{2}\right\rangle\right\rangle_{d}$ ($\langle\cdots\rangle$ meaning average over the lattice, and $\langle\cdots\rangle_{d}$ average over substrates). We pick this quantity as a relevant global indicator of convergence to an asymptotic state but of course we monitored other quantities, such as the mean height or the mean velocity as independent checks of our conclusions (see also the discussion of correlation functions below). Snapshots of the final state (see Fig. 2) of the surface confirm this picture

![](./images/812402201283526656_3.jpg)

Fig. 1. Log-log plot of the squared interface width (roughness) as a function of time for typical realizations and different lattice sizes. Inset: same plot with normal axes.

![](./images/812402201283526656_4.jpg)

Fig. 2. Snapshot of the asymptotic state of a $L=256$ simulation.
In the bottom left corner, superimposed for comparison, same
for $L=32$, $L=64$, and $L=128$. Notice the similarity of the
results when $L\geq64$.

as well. From all these magnitudes, in particular from
the plots in Fig. 1, we conclude that systems with $L\geq$
128 yield basically the same results, and therefore we
can discuss our measurements on those simulations as
representative of large lattices behavior. We note in
passing that the values we have obtained so far for the
saturated roughness at zero temperature do not clarify
whether it exhibits scaling [22] or not, although from
Fig. 1 one can conjecture the existence of a dynamic
exponent $\beta$. We will pursue further this issue in the
near future.

We now come to the main point of the work we are
summarizing in this paper. Fig. 3 collects the simula-
tion program outcome about the correlation function
for all the studied lattices averaged over 10 realiza-
tions. From this plot, we can conclude with a high
degree of confidence that, first, our results are inde-
pendent of the system size, and second, that the corre-
lation function is of $(\log r)^{2}$ type (cf. the inset where
we plot $C(r)$ versus $(\log r)^{2}$, yielding a clear straight
line, for $L=256$). Nevertheless, this is not the only
information we extract from this function: Indeed, we
also see that there is a well-defined correlation length
$\xi\simeq20$ lattice units, beyond which the surface is un-
correlated. This characteristic value can also be seen
in Fig. 2 as the typical length scale of the surface
features.

![](./images/812402201283526656_5.jpg)

Fig. 3. Height difference correlation function Inset: $C(r)$ vs.
$(\log r)^{2}$ for $L=256$. Averages comprise 10 realizations of
the substrate disorder. Error bars correspond to the rms of the
average.

### 3. Discussion and conclusions

Among the results summarized in the previous para-
graph, we first discuss the finding of a particularly
noted length scale. This is coherent with the fact that
lattices of sizes above $64\times64$ yield basically the same
results: This is to be expected if the surface characteris-
tics do no extend beyond a range of about 20 sites. Pre-
liminary analytical and numerical calculations show
that this length arises at sites where the disorder takes
values around $\pi$, which turn out to be the ones respon-
sible for the most noticeable distortions of the surface.
These distortions adopt a more or less conical form,
their radius being very close to the correlation length
$\xi$. Therefore, we provisorily conclude that at the phys-
ical roots for the appearance of a correlation length
lies the effect of "more disordered" sites.

However, probably our most relevant achievement
in this work is the fact that we have shown that the
height-difference correlation function behaves very
approximately like $(\log r)^{2}$. We do not claim that
$C(r)$ is exactly a squared logarithm, as the contribu-
tion of corrections to this behavior cannot be excluded
from the present state of our simulation program.
Although this is something that remains to be settled,

what we do claim is that $C(r)$ is by no means simply logarithmic. This is very important, since variational replica-symmetry breaking calculations predicted that $C(r)=A(T_{\mathrm{R}}^{*})\log r$ for all $T<T_{\mathrm{R}}^{*}$ including $T=0$. We believe that our simulations rule out the possibiliy of this prediction being correct. Recent work from the Rome group analyzing higher moments of $C(r)$ supports this conclusion as well [24]; another group has subsequently found the same behavior [25]. $^{1}$
We note that this conclusion raises the possibility of multiscale homogenization issues and associated averaging and nonergodicity features. On the other hand, we do not think that our results should be taken as grounds to establish the validity of RG calculations, because these are only expected to be valid in a temperature interval around $T_{\mathrm{R}}^{*}$; RG predicts nothing about the very low temperature regime we are dealing with here. Therefore, till now we can only provide the negative result of the invalidation of variational predictions, whereas on the positive side we can only say that there are indications that RG results may be closer to the actual physical behavior. We hope that the extension of our results to nonzero temperatures, which we are currently addressing, will allow us to find out what is the actual landscape of this system and whether RG is still a good theory to understand it.

## Acknowledgements

We thank Juan Jesús Ruiz Lorenzo for helpful and friendly discusssions as well as communication of results prior to publication. Work at Los Alamos is performed under the auspices of the US DoE. Work at Leganés and Madrid is supported by CICyT (Spain) under grant no. MAT95-0325.

$^{1}$ Ref. [25] appeared after we submitted our manuscript and this note was added in the final version.

## References

[1] J. Toner and D.P. DiVincenzo, Phys. Rev. B 41 (1990) 632.
[2] G.G. Batrouni and T. Hwa, Phys. Rev. Lett. 72 (1994) 4133.
[3] P.B. Littlewood, Phys. Rev. B 36 (1986) 6694.
[4] P.B. Littlewood and R. Rammal, Phys. Rev. B 38 (1988) 2675.
[5] D. Cule and Y. Shapir, Phys. Rev. Lett. 74 (1995) 114.
[6] S.E. Korshunov, Phys. Rev. B 48 (1993) 3969.
[7] T. Giamarchi and P. Le Doussal, Phys. Rev. Lett. 71 (1994) 1530.
[8] D. Cule, Phys. Rev. E 52 (1995) R1.
[9] P. Nozières and F. Gallet, J. Physique 48 (1987) 353.
[10] Y.-C. Tsai and Y. Shapir, Phys. Rev. Lett. 69 (1992) 1773.
[11] Y.-C. Tsai and Y. Shapir, Phys. Rev. E 50 (1994) 3546, 4445.
[12] E. Marinari, R. Monasson and J.J. Ruiz-Lorenzo, J. Phys. A 28 (1995) 3975.
[13] D.J. Lancaster and J.J. Ruiz-Lorenzo, J. Phys. A 28 (1995) L577.
[14] D. Cule and Y. Shapir, Phys. Rev. E 53 (1996) 1553.
[15] D. Cule and Y. Shapir, J. Phys. A 29 (1996) 21.
[16] D. Cule and Y. Shapir, Phys. Rev. B 51 (1995) R3305.
[17] M.P.A. Fisher, Phys. Rev. Lett. 62 (1989) 1773.
[18] S.N. Coppersmith, Phys. Rev. Lett. 65 (1990) 1044.
[19] E. Frey and F. Schawbl, Adv. Phys. 43 (1994) 577.
[20] L.M. Floría and J.J. Mazo, Adv. Phys. (1996) in press.
[21] S.T. Chui and J.D. Weeks, Phys. Rev. Lett. 40 (1978) 733.
[22] A.-L. Barabási and H.E. Stanley, Fractal Concepts in Surface Growth (Cambridge University Press, Cambridge, UK, 1995).
[23] A. Sánchez, D. Cai, N. Grønbech-Jensen, A.R. Bishop and Z.J. Wang, Phys. Rev. B 51 (1995) 14664.
[24] J.J. Ruiz-Lorenzo, private communication (1996).
[25] C. Zeng, A.A. Middleton and Y. Shapir, Phys. Rev. Lett. 77 (1996) 3204.
[26] Y.Y. Goldschmidt and B. Schaub, Nucl. Phys. B 251 (1985) 77.
[27] L.F. Cugliandolo, J. Kurchan, and P. Le Doussal, Phys. Rev. Lett. 76 (1996) 2390.
[28] S.N. Coppersmith and A.J. Millis, Phys. Rev. B 44 (1991) 7799.
[29] C.C. Chow and T. Hwa, Physica D 84 (1995) 494.
[30] N. Grønbech-Jensen, A.R. Bishop, F. Falo and P.S. Lomdahl, Phys. Rev. B 45 (1992) 10139.