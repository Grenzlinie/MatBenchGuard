# Frustration and Phase Transitions in Ising Model on Decorated Square Lattice

A. I. Proshkin$^{a, b, *}$ and F. A. Kassan-Ogly$^{a}$

$^{a}$ Mikheev Institute of Metal Physics, Ural Branch, Russian Academy of Sciences, Ekaterinburg, 620108 Russia
$^{b}$ Ural Federal University Named after the first President of Russia B.N. Yeltsin, Ekaterinburg, 620002 Russia
*e-mail: proshkin_ai@imp.uran.ru

Received July 24, 2019

Abstract—The Ising model on a square lattice with arbitrary number of decorating spins, considering both the interactions between nodal and decorating spins is examined. A plethora of peculiarities such as heat capacity splitting, generation and suppression of multiple phase transitions and several kinds of partial ordering are thoroughly scrutinized. A rigorous analytical expression for the partition function closely resembling the one obtained by Onsager is presented.

Keywords: Ising model, frustrations, decorated square lattice

DOI: 10.1134/S0031918X19130234

## INTRODUCTION

After a brilliant work of Lars Onsager [1], a considerable progress in understanding the physical processes, taking place in different real systems has been achieved. Exact analytical solutions of the Ising model on triangular [2, 3], hexagonal and kagome [4] lattice, to say nothing of the vast expanse of investigations that use different approximate approaches (see, for example [5, 6]), gave the humanity a solid ground for comprehending peculiar thermodynamic phenomena, such as phase transitions, frustrations [7], etc.

Despite the significant amount of effort made up to this time there is always something left to study. The Ising model may be generalized in different ways. One way is to allow the spins to orient in more than two directions. Such a model is called the Potts model and is being investigated too but with a considerably less interest from the scientific community [8]. Another way is to include interactions between next-nearest neighbors or a magnetic field. Unfortunately, such a model even in the simplest case of the square lattice has not been exactly solved yet. Thanks to Syozi [9] and his transformation technique, the Ising model on different decorated lattices may be solved exactly. This approach may even be used to investigate the model in a magnetic field of special kind [10].

It is necessary to mention that the Ising systems consisting of spins of various magnitudes, also called mixed-spin systems, recently got a great interest due to rich variety of unusual physical properties. A series of real compounds that may be described by such systems makes mixed-spin nets definitely worth to study (see [11, 12] and the references therein).

In the present work, we discuss the Ising model on a decorated square lattice, the model that in the absence of magnetic field can be exactly solved and includes the famous Onsager solution as a particular case. We present a rigorous analytical expression for the partition function and examine outstanding phenomena taking place in the model.

The outline of the article is as follows. In Section 1, we discuss the model and introduce an expression for the partition function including interactions between decorating and nodal sites. In Section 2, a particular case of the general model is thoroughly investigated: the case when only isotropic interactions between decorating spins are present. In Sections 3–5, the unusual properties of decorated lattices such as frustrations, multiple phase transitions and partial orderings are mentioned. The unusual thermodynamic properties of decorated Ising nets correlate with the experimental results obtained in different highly anisotropic lanthanum and actinium monopnictides and monochalcogenides such as UP and UAs so in the final Section 6 an attempt to describe some experimental results is performed.

## 1. GENERAL FORMULAE

The model under consideration is depicted in Fig. 1. The word “decorated” implies that there are spins (which will subsequently be referred to as decorating ones) located between spins occupying the nodal sites of a square lattice (undecorating spins). These

decorating spins interact with two neighboring spins by an exchange interaction $J_{xd}$ or $J_{yd}$; $J_x$ and $J_y$ stand for the direct interaction between undecorating spins.

The idea used here is to rewrite the Hamiltonian of the system in such a way that “replaces” all interactions between decorating spins with a new modified interaction between nodal spins only. Similar technique was previously used to derive the partition function of the hexagonal lattice and is known as a “startriangle transformation” [13]. It seems that this method for decorated lattices was firstly described by Syozi (see for example, [9]) and now is known as “decoration-iteration transformation”.

The relation between the model under consideration and the classical Ising square lattice with “modified interactions” has the following form:
$$
Z_{N N_{0}}^{\mathrm{dec}}\left(K_{x d}, K_{x} ; K_{y d}, K_{y}\right)=A_{x}^{N} A_{y}^{N} Z_{N}^{\mathrm{sq}}\left(L_{x} ; L_{y}\right), \quad(1)
$$
where $N_0$ is the number of spins in the decorated lattice unit cell which is equal to $1+d_x+d_y$, $K_i=J_{i l}/T$, $Z_{N N_{0}}^{\mathrm{dec}}$ stands for the partition function of decorated square lattice with $N N_0$ spins and $Z_{N}^{\mathrm{sq}}$ stands for the partition function of $N$ spins on classical square lattice with interactions between nearest neighbors $L_x$ and $L_y$ along $x$ and $y$ axes correspondingly:
$$
L_{i}=\frac{1}{2} \ln \frac{G_{i}}{F_{i}}+K_{i}, \quad(2)
$$
$$
A_{i}=\sqrt{F_{i} G_{i}}, \quad(3)
$$
$$
G_{i}=2^{d_{i}}\left(\cosh K_{i d}^{d_{i}+1}+\sinh K_{i d}^{d_{i}+1}\right), \quad(4)
$$
$$
F_{i}=2^{d_{i}}\left(\cosh K_{i d}^{d_{i}+1}-\sinh K_{i d}^{d_{i}+1}\right), \quad(5)
$$
where $i=1,2$ and for the sake of brevity we denote $d_x$ and $d_y$ as $d_1$ and $d_2$, $J_x/T$ and $J_y/T$ as $K_1$ and $K_2$, $J_{xd}/T$ and $J_{yd}/T$ as $K_{1d}$ and $K_{2d}$ correspondingly.

An exact analytical expression for the partition function $\lambda$ (strictly speaking, the maximal eigenvalue of Kramers–Wannier transfer matrix, refer to [14] for the details) with arbitrary amount of decorating spins along $x$ and $y$ axes (these values do not necessarily coincide):
$$
\begin{gathered}
N_{0} \ln (\lambda / 2)=\frac{1}{8 \pi^{2}} \\
\times \int_{0}^{2 \pi} \int_{0}^{2 \pi} \ln \left(C_{1} C_{2}-S_{1} D_{2} \cos \phi-S_{2} D_{1} \cos \theta\right) d \phi d \theta,
\end{gathered}
\qquad(6)
$$
where
$$
D_{i}=\cosh ^{2 d_{i}+2} K_{i d}-\sinh ^{2 d_{i}+2} K_{i d}, \quad(7)
$$
$$
\begin{aligned}
C_{i} &=\frac{1}{2} e^{2 K_{i}}\left(\cosh ^{d_{i}+1} K_{i d}+\sinh ^{d_{i}+1} K_{i d}\right)^{2} \\
&+\frac{1}{2} e^{-2 K_{i}}\left(\cosh ^{d_{i}+1} K_{i d}-\sinh ^{d_{i}+1} K_{i d}\right)^{2},
\end{aligned}
\qquad(8)
$$

![](./images/812681513450602497_1.jpg)

Fig. 1. Ising model on decorated square lattice.

$$
\begin{aligned}
S_{i} &=\frac{1}{2} e^{2 K_{i}}\left(\cosh ^{d_{i}+1} K_{i d}+\sinh ^{d_{i}+1} K_{i d}\right)^{2} \\
&-\frac{1}{2} e^{-2 K_{i}}\left(\cosh ^{d_{i}+1} K_{i d}-\sinh ^{d_{i}+1} K_{i d}\right)^{2}.
\end{aligned}
\qquad(9)
$$

Equation (6) is deliberately written in such a form that closely resembles the famous Onsager’s expression for the partition function of original (undecorated) square lattice. One can easily obtain the Onsager’s equation as a particular case supposing $d_x=d_y=0$, $K_{1d}=K_{2d}=0$.

## 2. SINGLY DECORATED ISOTROPIC MODEL WITHOUT DIRECT INTERACTIONS

The simplest case to begin with is the singly decorated isotropic model in the absence of interactions between nodal sites. Let us suppose $d_x=d_y=1$, $K_x=K_y=0$ and $K_{xd}=K_{yd}=K_d$ in the general Eq. (1). Equation (6) in this case may be substantially simplified and written in the following compact form:
$$
\begin{gathered}
\ln \lambda=\frac{1}{3}\left[4\left(\cosh ^{2} 2 K_{d}+1\right)\right] \\
+\frac{1}{6 \pi} \int_{0}^{\pi} \ln \left[\frac{1}{2}\left(1+\sqrt{1-m^{2} \sin ^{2} \phi}\right)\right] d \phi,
\end{gathered}
\qquad(10)
$$
where
$$
m=\frac{2 \sinh 2 K_{d} \sinh 4 K_{d}}{\left(\cosh ^{2} 2 K_{d}+1\right)^{2}}. \quad(11)
$$

![](./images/812681513450602497_2.jpg)

Fig. 2. Heat capacity splitting in singly decorated square
lattice without direct interaction at $R_d = 0.08$.

We can derive an exact analytical expression for the
heat capacity function:
$$
\begin{aligned}
C =& \frac{4K_d^2}{3\pi}\bigl[\pi(3 + \cosh 4K_d)\csch^2 4K_d \\
&+ \frac{1}{4m^2}\Bigl(2\Bigl(\frac{dm}{dK_d}\Bigr)^2 - m\frac{d^2m}{dK_d^2}\Bigr)K(m) \\
&- (\coth 4K_d + 3\csch 4K_d)^2 E(m)\bigr],
\end{aligned}
\tag{12}
$$
where $K(m)$ and $E(m)$ are the complete elliptic integrals of the first and second kind:
$$
K(m) = \int_{0}^{\pi/2} \left(1 - m^2 \sin^2 \phi\right)^{-1/2} d\phi, \tag{13}
$$

$$
E(m) = \int_{0}^{\pi/2} \left(1 - m^2 \sin^2 \phi\right)^{1/2} d\phi. \tag{14}
$$

The elliptic integral of the first king diverges at $m = 1$
giving the phase transition temperature of the isotropic decorated square lattice as $T_c = 2/\cosh^{-1}(1+\sqrt{2})$
which may be obtained from the phase-transition-temperature expression for the nondecorated square
lattice by substituting natural logarithm with the
inverse hyperbolic cosine function.

The model possesses a plethora of peculiarities
such that undecorated lattices do not demonstrate. Let
us denote $R_d = J_{yd}/J_{xd}$. In the case of $R_d = 0$ the lattice consists of non-interacting linear chains with
"free" spins between them (spins that do not take part
in the interaction). Since there are $N/3$ such spins
($N$ is the total number of spins) zero-temperature
entropy in this case tends to nonzero value of $1/3 \ln 2$.
As a consequence, the ground state is highly degenerate, or frustrated ($R_d = 0$ is the frustration point).
Heat capacity in that case is a continuous curve with a
broad cupola-shaped maximum.

![](./images/812681513450602497_3.jpg)

Fig. 3. Phase diagram of singly decorated isotropic Ising
model on square lattice without direct interaction. Circles
represent phase transition temperatures, squares and triangles—broad heat capacity maxima locations.

At any nonzero $R_d$ the system possesses a phase transition, i.e. the temperature at which a long-range order
vanishes. Though it seems obvious that frustrated systems
cannot undergo phase transitions because they do not
have a long-range order even at zero temperature, it is not
always the case. This depends upon the different kinds of
partial orderings that may be present in the frustrated systems at different temperatures and is discussed in more
detail in Section 5.

At small values of $R_d$ the heat capacity splits. Figure 2
is the illustration of such a behavior in close vicinity of
frustration point. It is seen that the heat capacity possesses three distinct peaks of different kind. The right
one (in the high temperature region) is an echo of frustrations and is explained by new phase inclusions. The
middle one sharp lambda-shaped maximum corresponds to the phase transition and such a behavior is
not peculiar. Previously the effect of specific heat
splitting into two maxima has been observed in different lattices of various dimensions and described in
[15]. The most exciting maximum is the left one
because it is caused by decorating spins and signifies
partial orderings present in the system at low temperatures. The positions of all heat capacity peaks are summarized in Fig. 3.

![](./images/812681513450602497_4.jpg)

Fig. 4. Heat capacity peaks in Ising model on decorated square lattice $J_{xd}=J_{yd}=-1, J_x=-0.8, J_y=-3, d_x=d_y=1$.

![](./images/812681513450602497_5.jpg)

Fig. 5. Entropy jump in Ising model on decorated square lattice. $J_{xd}=J_{yd}=-1, J_x=-0.8, J_y=-3, d_x=d_y=1$.

### 3. FRUSTRATIONS

The system behavior becomes much more interesting when we take into consideration the direct interaction. At certain signs of exchange interaction parameters and decoration numbers the ground state of the system is frustrated (the difference here is that these parameters have nonzero values). The case 1: antiferromagnetic interaction between decorating and nodal sites when the decoration number is odd. The case 2: antiferromagnetic interaction between decorating sites with ferromagnetic direct interaction when the decoration number is even. The ground state degeneracy is of the order of $N$ so the residual entropy (entropy at $T \to 0$) does not tend to zero. This nonzero entropy at zero temperature does not conflict with the third law because the law demands an entropy derivative to be equal to zero and this rule is perfectly satisfied. It is possible to obtain a general formula for the residual entropy in both cases when modulo of all interaction energies are equal:

$$
\begin{aligned}
S_{n} &=\frac{1}{2 \pi(2 n+1)} \int_{0}^{\pi} \ln \left[\frac{1}{2}\left(n^{2}+2 n+2\right)^{2}\right. \\
& \times\left(1+\sqrt{1-\left(\frac{4 n(n+1)(n+2)}{\left(n^{2}+2 n+2\right)^{2}}\right)^{2} \sin ^{2} \phi}\right)] d \phi,
\end{aligned}
\tag{15}
$$

where $n=1,2 \ldots$. Here all odd values of $n$ give the residual entropy at the case 1, and all even values of $n$ refer to the case 2.

### 4. MULTIPLE PHASE TRANSITIONS

The most distinctive feature is the presence of multiple phase transitions in the system at certain values of interaction parameters and decoration numbers. In Fig. 4 an example of two phase transitions is shown. The entropy behavior in this case is drawn in Fig. 5. While temperature decreases entropy tends to a certain value and then drastically changes to another. Nevertheless, at zero temperature entropy is by no mean equal to zero when the frustration in the system is present. From the other side, heat capacity has two distinct sharp heat capacity maxima. Previously in the literature it was widely supposed that frustrated systems do not undergo phase transitions (not even a single one, to say nothing of two transitions or more).

This phenomenon, unusual for the Ising model, was pointed out by Syozi [16], who nevertheless did not pay much attention to it. We have thoroughly examined this behavior and found out that the system may possess none, one, two or even three phase transitions. Usually only one heat capacity maximum is clearly distinct. The others may look comparatively subtle. It must be stressed that it is possible to overlook these petty maxima using quantitative computer simulations especially using the traditional Monte Carlo approach.

### 5. PARTIAL ORDERINGS

Amusing heat capacity behavior drawn in Fig. 4 is due to the partial ordering present in the system. A function more suitable for representing these orderings was

![](./images/812681513450602497_6.jpg)

Fig. 6. Order parameter in Ising model on decorated square lattice. $J_{xd}=J_{yd}=-1, J_x=-0.8, J_y=-3, d_x=d_y=1$.

introduced in [17]. The authors called it the order parameter, which in the case has the following form:

$$
\eta(T)=1-\frac{S(T)}{\ln 2}, \tag{16}
$$

where $S$ is an entropy as function of temperature $T$.

Order parameter corresponding to the case plotted in Fig. 5 is shown in Fig. 6. It is clearly visible that at $T \to 0$ the system tends to a state with the order parameter equal to $1/3$ but then the ground state dras- tically changes so the order parameter becomes equal to $2/3$ resulting in the sharp heat capacity maximum seen in Fig. 4. It is worth noting that the order param- eter does not equal to unity even at zero temperature. This implies that the ground state does not have a long-range order. Only part of the system is ordered so the order parameter is the vivid example of the partial ordering present in the system.

Figure 7a represents the heat capacity as function of temperature in the case when only equal interac- tions between nodal sites are present. From heat capacity we see that the phase transition temperature does not depend upon the decoration number. In that case, it is equal to the famous Onsager result $2/\ln(1+\sqrt{2})$. Heat capacity still logarithmically diverges and has only difference in magnitude. Figure 7b illus- trates the order parameter. Here the difference is evi- dent. The order parameter at zero temperature is not equal to unity but rather to value $1/N_0$, where $N_0$ is the number of spins in the unit cell. It is easy to under- stand because there are "free" spins not taking part in the interaction resulting in the fact that the system as a whole cannot have a long-range order. Only subset of the system is ordered and the order parameter clearly points this out. It should be noted that such a conclu- sion is not easy to deduce from the entropy.

![](./images/812681513450602497_7.jpg)

Fig. 7. Heat capacity (a) and order parameter (b) as functions of temperature in Ising model on square decorated lattice with equal direct interactions and zero interactions between decorating spins. The number of decoration is 3 (solid line), 5 (dashed line) and 10 (dot-dashed line).

![](./images/812681513450602497_8.jpg)

Fig. 8. (a) Heat capacity as function of temperature in UP. The first sharp maximum at 22.5 K was not explained by the authors in [18]; (b) magnetic entropy as function of temperature in UP [19].

## 6. COMPARISON WITH THE EXPERIMENTAL DATA

As was previously mentioned, the Ising model on square decorated lattice possesses many peculiarities that distinguish the model form the classical ones. The model can be inspiring in a preparation of new magnetic materials. As for now, the authors are unaware of any real two-dimensional system that can directly be described by the model under investigation. Nevertheless, it is worth mentioning that three-dimensional bcc and fcc lattices may be regarded as body-decorated and face-decorated cubic lattices respectively.

It seems that the most distinguishable property of the model is the presence of the sharp heat capacity maximum at certain values of interactions and decoration numbers. The sharp maximum closely resembling the one shown in Fig. 4 was previously found in UP [18, 19] and UAs [20, 21]. The peculiar behavior of heat capacity of UP is shown in Fig. 7a and entropy in Fig. 7b. It is clearly visible that the first heat capacity maximum in UP significantly overwhelms the second one at $T_{\mathrm{N}}=121$ K. Authors of [18] note that its "origin has not been established". Even though it is not correct to directly compare the results obtained in two-dimensional model with the experimental data on three-dimensional sample some close similarities between systems are evident. Lanthanum and actinium monopnictides and monochalcogenides are the complex three-dimensional systems with unique magnetic and thermodynamic properties that cannot be directly described by the simplified model investigated in the current paper. These compounds may demand usage of more complex models, for example, Potts models or Heisenberg model. Anyway similar heat capacity behavior may be found in many different systems.

## CONCLUSIONS

In this work, the Ising model on a square lattice with the presence of interactions between decorating and nodal spins with arbitrary number of decorations is examined. Outstanding properties such as multiple phase transitions, partial orderings, heat capacity splitting and frustrations are pointed out and discussed. So far, this model possesses every aspect of unusual phenomena of Ising model on different lattices reported previously in the scientific literature.

The most prominent feature of the model is the sharp heat capacity maximum that appears at certain interaction parameters and decoration numbers. The similar peculiarities in thermodynamic behavior have been obtained previously for the real three-dimensional magnetic systems such as UP and UAs suggesting that the results obtained in the present article may be utilized to explain such a behavior. Moreover, such a feature may be utilized in manufacturing magnetic refrigerator systems in the future.

The detailed analysis showed that the model might possess none, one, two or even three phase transitions. When multiple phase transitions are present some heat capacity maxima may be comparatively subtle or even not seen if the sharp peak like the one found in UP is present. All the same chosen parameters may produce quite different results that depend upon the topology of the system.

The method described in the article is completely general so similar calculation may be performed for all lattice geometries and all values of decoration numbers. It is of great interest to investigate thermodynamic properties of the Ising model on decorated triangular, hexagonal and kagome lattices. A lot of interesting phenomena in these systems have been obtained by the authors and the results are to be published.

## FUNDING

The research was carried out within the state assignment of Minobrnauki of Russia (theme "Quantum" no. AAAA-A18-118020190095-4), supported in part by Ural Branch of the Russian Academy of Sciences (project no. 18-2-2-11).

## REFERENCES

1.  L. Onsager, "Crystal statistics. I. A two-dimensional model with an order-disorder transformation," Phys. Rev. **65**, 117–149 (1944).

2.  R. M. F. Houtappel, "Order-disorder in hexagonal lattices," Physica **16**, 425–455 (1950).

3.  G. H. Wannier, "Antiferromagnetism. The triangular Ising net," Phys. Rev. **79**, 357–364 (1950).

4.  K. Kanô and S. Naya, "Antiferromagnetism. The kag-omé Ising net," Prog. Theor. Phys. **10**, 157–172 (1953).

5.  D. P. Landau and K. Binder, *A Guide to Monte-Carlo Simulations in Statistical Physics* (Cambridge University Press, Cambridge, 2009.

6.  A. K. Murtazaev, M. K. Ramazanov, and M. K. Badiev, "Critical properties of the two-dimensional Ising model on a square lattice with competing interactions," Phys. B: Condens. Matter **476**, 1–5 (2015).

7.  H. T. Diep, *Frustrated spin systems* (World Scientific, Singapore, 2013).

8.  F. Y. Wu, "The Potts model," Rev. Mod. Phys. **54**, 235–268 (1982).

9.  I. Syozi and S. Miyazima, "A statistical model for the dilute ferromagnet," Prog. Theor. Phys. **36**, 1083–1094 (1966).

10. M. Fisher, "Transformations of Ising models," Phys. Rev. **113**, 969–981 (1958).

11. M. Jaščur, V. Štubňa, K. Szalowski, and T. Balcerzak, "Frustration in an exactly solvable mixed-spin Ising model with bilinear and three-site four-spin interactions on a decorated square lattice," J. Magn. Magn. Mater. **417**, 92–99 (2016).

12. L. Čanova, J. Strečka, and M. Jaščur, "Exact results of the mixed-spin Ising model on a decorated square lattice with two different decorating spins of integer magnitudes," Int. J. Mod. Phys. B **22**, 2355–2372 (2008).

13. R. J. Baxter, *Exactly Solved Models in Statistical Mechanics* (Academic, New York, 1982).

14. H. A. Kramers and G. H. Wannier, "Statistics of the two-dimensional ferromagnet. Part I," Phys. Rev. **60**, 252–262 (1941).

15. F. A. Kassan-Ogly and A. I. Proshkin, "Frustrations and ordering in magnetic systems of various dimensions," Phys. Solid State **60**, 1090–1097 (2018).

16. I. Syozi, "A decorated Ising lattice with three transition temperatures," Prog. Theor. Phys. **39**, 1367–1368 (1968).

17. F. A. Kassan-Ogly, B. N. Filippov, A. K. Murtazaev, M. K. Ramazanov, and M. K. Badiev, "Influence of field on frustrations in low-dimensional magnets," J. Magn. Magn. Mater. **324**, 3418–3421 (2012).

18. J. F. Counsell, R. M. Dell, A. R. Junkison, and F. F. Martin, "Thermodynamic properties of uranium compounds," Trans. Faraday Soc. **63**, 72–79 (1966).

19. A. Blaise, R. Lagnier, J. E. Gordon, and R.Troc, "Heat capacity studies of ThP and $\text{UP}_{0.5}\text{As}_{0.5}$ solid solution. Reanalyzing UP data," J. Low-Temp. Phys. **61**, 323–335 (1985).

20. H. Yokokawa, Y. Takahashi, and T. Mukaibo, "The heat capacity of uranium monophosphide from 80 to 1080 K and the electronic contribution," in Thermodynamics of Nuclear Materials 1974, Vol. II (Int. Atomic Energy Agency, Vienna, 1975), pp. 419–430.

21. A. Blaise, R. Troc, R. Lagnier, and M. J. Mortime, "The heat capacity of uranium monoarsenide," J. Low. Temp. Phys. **38**, 79–92 (1980).
