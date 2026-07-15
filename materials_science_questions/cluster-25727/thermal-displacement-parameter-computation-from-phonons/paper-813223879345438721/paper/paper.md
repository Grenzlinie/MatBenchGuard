# Multiphonon absorption in alkali halides: Quantum treatment of Morse potential
Herbert B. Rosenstock
Naval Research Laboratory, Washington, D.C. 20375
(Received 19 September 1973)

With a view towards calculating the lattice absorption of solids, as a function of frequency and temperature, at frequencies much higher than that of the maximum lattice frequency, a quantum mechanical calculation is given of the absorption involving vibrational levels of a Morse potential that are not adjacent. The thermal average is then taken, and the nature of the solid simulated by a summation over a Debye spectrum. Results are evaluated numerically in the high-temperature approximation, and compared with experimental results on the temperature dependence of absorption by alkali halides at 10.6 $\mu$m.

## I. INTRODUCTION
Several workers have recently tried to calculate the absorption of insulating solids in regions of the infrared that would require the combined action of several phonons, $^{1-5}$ i.e., absorption of photons of energy 5 to 7 times that of the most energetic lattice phonon. Several of these papers$^{3,4}$ have either explicitly or by implication used the "Einstein" model of a solid: the solid is treated as an assembly of identical oscillators ("diatomic molecules"), independent but intrinsically anharmonic. In this model, the phonons that act together to provide the absorption all come from the same oscillator (or diatomic molecule). While it is realized that in the more usual model of a solid the phonons would come from different oscillators (where "oscillators" would mean the normal modes of the lattice in the harmonic approximation, coupled to each other by the anharmonicity of the potentials), this diatomic-molecule model is nonetheless used as an approximation. Each treatment obtained, either explicitly or by implication, a $T^{n-1}$ dependence of the absorption at a given frequency on the temperature, with $n$ the number of phonons required to achieve the process energetically. Most simply, this is shown to be just a consequence of the boson occupation numbers obeyed by phonons. $^{1,5}$ Experimental results$^{6}$ have revealed a much weaker temperature dependence ($T^{0}$ to $T^{2}$ for absorption at 10.6 $\mu$m, where $n$ for alkali halides would have to be at least 5 to 7). This has resulted in additional theoretical work to modify and elaborate earlier results. $^{7,8}$

One of the earlier approaches$^{4,8}$ provided a classical treatment of absorption by diatomic molecules for several choices of anharmonic interatomic potentials. Perhaps the most realistic of these potentials, the so-called Morse potential$^{9}$ is, however, exactly solvable in quantum mechanics, and we therefore attempt here a quantum mechanical calculation of "multiphonon" absorption by a Morse potential.

There are several reasons for doing this. One, of course, is the fact that the replacement of quantum mechanics by classical physics is valid only in the limit $\hbar \to 0$, i.e., at best at high temperatures; less obviously, the quantum calculation is also simpler—as is frequently the case where it can be carried out at all—and more transparent—in avoiding the complex statistical arguments and several approximations that the classical approach entails. Specifically, we use what is sometimes called semiclassical-radiation theory, in which the absorber is treated according to quantum mechanics, but the light as a Maxwellian electromagnetic wave. $^{10}$ No use is made of second-quantization techniques. The same approach has also been used with the Morse potential in Ref. 3.

We have put the word multiphonon in quotation marks above because the phonon concept does not really appear in our calculation. "Phonons" imply energy levels that are equally spaced, as arise in a structure that is treated as harmonic in the lowest approximation. In that lowest approximation, outside radiation can produce transitions between adjacent energy levels only (one-phonon transitions). Anharmonicity in that approach is treated by perturbation methods and allows transitions between energy levels that are not adjacent (coupling between the phonons or multiphonon transitions). By contrast, our potential is anharmonic from the beginning, and equally spaced energy levels, or phonons appear at no point. Radiation of the appropriate energy can then induce transitions between any pair of levels, and all are in general allowed; the main problem in essence is the calculation of the first-order matrix elements for transitions induced by radiation between energy levels—not necessarily adjacent ones—that are separated by a specified energy gap. This was done long ago, and is set down in Sec. II. The temperature dependence of the absorption is included by assigning Boltzmann population factors

to each level (Sec. III), and integration over the lattice frequencies is done in Sec. IV. Numerical results and figures, giving the absorption as a function of both light frequency and temperatures are obtained in Sec. V.

## II. MORSE OSCILLATOR FORMULAS-TRANSITIONS TO NONADJACENT LEVELS

The empirical potential function
$$
V(r)=D\left[1-e^{-a\left(r-r_{0}\right)}\right]^{2} \quad(1)
$$
was introduced into molecular physics by Morse $^{9}$ for three reasons: because it reasonably represents the potential between two atoms an equilibrium distance $r_{0}$ apart (it is very large at $r=0$, it has one minimum-zero-at $r=r_{0}$, and it approaches a finite value-the dissociation energy $D$-at $r=\infty$ ); because its Schrödinger equation can be solved exactly; and because it leads to eigenvalues in agreement with experiments that measure the spacing of adjacent energy levels in molecules (i.e., one-phonon-absorption experiments), at different temperatures. The eigenfunctions are $^{9}$
$$
\Psi(r, \theta, \phi)=\Phi(\phi) \Theta(\theta)[R(r) / r], \quad(2)
$$
with
$$
\Phi(\phi)=e^{i g \phi}, \quad \Theta(\theta)=\sin ^{g} \theta P_{j}^{g}(\cos \theta)
$$
the usual surface zonal harmonics that arise in problems with radial symmetry. When the rotational quantum number $j$ is nonzero, the radial function $R(r)$ is known only in the form of a complex integral $^{11}$ but is of similar form to the $j=0$ case, which is known in closed form. In that case it is
$$
R_{n}(r)=e^{-z / 2} z^{(k-2 n-1) / 2} L_{n}^{k-2 n-1}(z) e^{\sharp i(k-1)} C(n) \quad(4)
$$
where
$$
\begin{aligned}
k & =(8 \mu D)^{1 / 2} / a \hbar, \\
z & =k e^{a\left(r-r_{0}\right)}, \\
C(n) & =\frac{a^{1 / 2}}{\Gamma(k-n)}\left(\sum_{j=0}^{n} \frac{\Gamma(k-2 n-1+j)}{\Gamma(j+1)}\right)^{-1 / 2} ;
\end{aligned}
$$
the integer $n$ runs from 0 to $(k-1) / 2,2 \pi \hbar=h$ is Planck's constant, $\mu$ is the reduced mass, $m_{1} m_{2} /$ $\left(m_{1}+m_{2}\right)$ of the two atoms, and $\Gamma$ is the usual gamma function. Note that $k$ is not necessarily an integer. The associated Laguerre polynomials $L_{n}^{m}(z)$ are defined as $^{12}$
$$
L_{n}^{m}(z)=(-1)^{m} \frac{d^{m}}{d z^{m}}\left(e^{z} \frac{d^{n+m}}{d z^{n+m}}\left(z^{n+m} e^{-z}\right)\right).
$$

These functions are known polynomials even when $m$ is not an integer, $^{9}$ as is the case here. We confine ourselves to the case $j=0$, ignoring rotation, which has a small effect on the vibrational eigenvalues. $^{11}$ The latter are found to be finite in number
$$
\begin{gathered}
E_{n}=\hbar \omega\left(n+\frac{1}{2}\right)-\left(\hbar^{2} \omega^{2} / 4 D\right)\left(n+\frac{1}{2}\right)^{2} \\
\text { for } n=0,1, \ldots, \frac{1}{2}(k-1),
\end{gathered}
$$
with
$$
\begin{aligned}
\omega & =a(2 D / \mu)^{1 / 2} \\
\text { and } & \\
k & =4 D / \hbar \omega.
\end{aligned}
$$

The levels are thus seen to be approximately $\hbar \omega$ apart for small $n$, but very close together as the dissociation limit is approached.

[Readers of Ref. 9 should observe that the quantity there denoted by $\omega_{0}$ is what is above, and in today's conventional notation, called $\nu=\omega / 2 \pi$. They should also note a typographical error in the bottom line of Eq. (12), which appears as our Eq. (4), and in which $\Gamma(s-1)$ is written for the correct $\Gamma(s+1)$; and an apparent ambiguity in the top line of Eq. (12) which arises when $m \neq n$, in which case $b$ on the left has two meanings, viz., $k-2 n-1$ and $k-2 m-1$. The result is correct when $b$ is interpreted as the sum of half of these two quantities. Also, in his original paper, $^{9}$ Morse uses a somewhat different definition for the Laguerre polynomials, which we shall call $\bar{L}$, related to the $L$ above by
$$
\bar{L}_{n-b}^{b}(z)=(-1)^{b} L_{n}^{b}(z).
$$

Also, $V$ and the energy levels differ by a trivial constant term.]

From this, one can compute the probability for a transition from level $m$ to level $n$ caused by dipole radiation. By first-order perturbation theory this is proportional to the matrix element
$$
r_{m n}=\int \Psi_{m}^{*}\left(r-r_{0}\right) \Psi_{n} d V.
$$

With Eq. (2), this becomes, since the angular functions (3) are separately normalized,
$$
r_{m n}=\int r^{2} d r\left(R_{m}^{*} / r\right)\left(r-r_{0}\right)\left(R_{n} / r\right).
$$

With $R(r)$ given by (4) substitution gives
$$
\begin{aligned}
r_{m n}= & C(m) C(n) \int_{-\infty}^{\infty}\left(r-r_{0}\right) d r e^{-z} z^{k-m-n-1} \\
& \times L_{n}^{k-2 n-1}(z) L_{m}^{k-2 m-1}(z).
\end{aligned}
$$

The integration must be formally taken from $-\infty$ to $+\infty$ (rather than the usual 0 to $\infty$, as $V(r)$ was not symmetrical about the origin). This has been evaluated by Scholz $^{13}$ using generating functions methods. The result is
$$
r_{m n}^{2}=a^{-2}(n-m)^{-2} \frac{(k-1-2 m)(k-1-2 n)}{(k-1-m-n)^{2}}\left(\begin{array}{c}
n \\
m \\
\frac{k-m-1}{n-m}
\end{array}\right)
$$
for $n>m$, and $r_{m n}^{2}=r_{m n}$ otherwise. $\left(\begin{array}{l}n \\ m\end{array}\right)$ denotes the

usual binomial coefficient. Perhaps it is more appealing to write
$$
n-m=\Delta \quad, \quad(13)
$$
since for most applications $\Delta$ will be a small integer, while $m, n$ themselves could be large integers at elevated temperatures. Then
$$
r_{m, m+\Delta}^{2}=(a \Delta)^{-2} \frac{(k-1-2 m)(k-1-2 m-2 \Delta)}{(k-1-2 m-\Delta)^{2}} \frac{\left(\begin{array}{c}
m+\Delta \\
\Delta
\end{array}\right)}{\left(\begin{array}{c}
k-m-1 \\
\Delta
\end{array}\right)}
$$
for $\Delta>0$, and $r_{n m}=r_{m n}$ otherwise. We will use $r_{m, n}^{2}$ in this form, but also want to write down simplified expressions valid when $m \ll k$ (i.e., for levels well below the dissociation limit). Then we have approximately
$$
\begin{array}{r}
r_{m, m+\Delta}^{2} \cong(a \Delta)^{-2}(m+1)(m+2) \cdots(m+\Delta) / k^{\Delta}, \\
(m \ll k) \quad(15)
\end{array}
$$
specifically
$$
\begin{aligned}
& r_{m, m+1}^{2} \cong(m+1) / k a^{2}, \\
& r_{m, m+2}^{2} \cong(m+1)(m+2) / 4 k^{2} a^{2}, \\
& r_{m, m+3}^{2} \cong(m+1)(m+2)(m+3) / 9 k^{3} a^{2}, \text { etc. }
\end{aligned}
$$

Thus transitions for any two levels $\Delta$ apart are possible, but with decreasing probability proportional to $(m / k)^{\Delta}$.

### III. TEMPERATURE DEPENDENCE
Absorption of a photon of specified energy is possible if and only if the system is initially in a state that differs from a higher lying state by just that energy. The probability of being in such a state depends on the temperature, and consequently the probability of absorption does also. The absorption coefficient (except perhaps for constants) is given by
$$
\alpha\left(\omega, E_{l}, T\right)=\left(e^{-\beta E_{m}}-e^{-\beta E_{m+\Delta}}\right) r_{m, m+\Delta}^{2} / Z \quad(17)
$$
in the dipole approximation. So-called forbidden transitions, less probable by a factor $r_{0} / d$, with $d$ the wavelength of light, are not considered here. Here $E_{l}$ is the photon energy which must satisfy
$$
E_{l}=E_{m+\Delta}-E_{m} \quad. \quad(18)
$$
$\omega$, given by Eq. (7), is the basic frequency of the oscillator [roughly, as seen from Eq. (6), the separation between adjacent low-lying levels]. The normalizing constant
$$
Z=\sum_{m} e^{-\beta E_{m}} \quad(19)
$$
is usually called the partition function. As usual, we have written $\beta=\left(k_{B} T\right)^{-1}$, with $k_{B}$ Boltzmann's constant. Two terms appear in the numerator because the probability of the inverse process (emission of a photon as the system goes from state $m+\Delta$ to state $m$ ) has to be subtracted from the absorption probability (as the system goes from $m$ to $m+\Delta$ ) to give the net absorption probability; the matrix element $r^{2}$ is, as we have seen in Eq. (12) or (14), the same for the two processes. For high temperature, or, specifically $\beta E_{m+\Delta} \ll 1$, the numerator of Eq. (17) becomes, with (18),
$$
r_{m, m+\Delta}^{2} \beta E_{l} e^{-\beta E_{m}} \quad. \quad(20)
$$

The partition function (19) is to be evaluated with the use of Eq. (6) for the energy levels. We use the Euler-MacLaurin series; three terms suffice:
$$
\sum_{n=a}^{b} f(n)=\int_{a}^{b} f(x) d x+\frac{1}{2}[f(b)+f(a)]+\frac{1}{12}\left[f^{\prime}(b)-f^{\prime}(a)\right],
$$
where, from Eqs. (19) and (6) with (7) we take
$$
\begin{aligned}
f(n) & =\exp \left\{-\gamma\left[\left(n+\frac{1}{2}\right)-k^{-1}\left(n+\frac{1}{2}\right)^{2}\right]\right\}, \\
\text { with } \quad \gamma & =\beta \hbar \omega \quad.
\end{aligned}
$$

We obtain
$$
\begin{aligned}
Z= & Z_{\text {cont }}+(k / \gamma)^{1 / 2} e^{-\gamma k / 4} \Phi\left[\left(\frac{1}{4} \gamma k\right)^{1 / 2}\left(1-k^{-1}\right)\right] \\
& +\frac{1}{2}\left[1+\frac{1}{6} \gamma\left(1-k^{-1}\right)\right] e^{-(\gamma / 2)\left[1-(2 k)^{-1}\right]}+\frac{1}{2} e^{-\gamma k / 4}. \quad(22)
\end{aligned}
$$

Here
$$
\Phi(x) \equiv \int_{0}^{x} e^{+t^{2}} d t \quad(23)
$$
is a known, tabulated $^{14}$ function (not identical with the better-known error function on account of the $+$ sign in the exponent) for which two series expansion can be developed:
$$
\Phi(x)=x \sum_{j=0}^{\infty} \frac{x^{2 j}}{(2 j+1) j!} \quad(24)
$$
convergent for all $x$ but useful only for small $x$; and
$$
\Phi(x) \cong e^{x^{2}}(2 x)^{-1} \sum_{j=0} \frac{(2 j)!}{(2 x)^{2 j} j!} \quad(25)
$$
asymptotically valid for large $x$. $Z_{\text {cont }}$ in Eq. (22) is the sum over the continuum of states of energy greater than 0 ; these have been ignored when writing Eqs. (4) and (6), and describe the molecule after dissociation. Fortunately, we shall have no need to know them explicitly; they would be important only for energies above or near the dissociation energy (which as we shall see, implies temperature above $40000^{\circ} \mathrm{K}$).

We have a particular interest in the range in which $\gamma=\beta \hbar \omega$ is small, but $k \gamma$ large; i.e., in a temperature large enough to put the system well above the ground state, but not into the dissociation continuum. Then $Z_{\text {cont }}$ can be neglected and the other terms in Eq. (22) become, with Eq. (25),
$$
Z=(\beta \hbar \omega)^{-1}\left[1+4(k \beta \hbar \omega)^{-1}+\cdots\right]
$$

$$+\frac{1}{2}\left[1-\frac{2}{3} \beta \hbar \omega+\cdots\right]. \qquad (26)$$

Combining this with the high-temperature result (20) for the numerator of Eq. (17) then yields the absorption coefficient for the specific photons whose energy equals $E_{m+\Delta}-E_{m}$ for some $m$ and $\Delta$. In this section, we have evaluated the temperature-dependent part of the absorption coefficients (17) for "high" temperatures-temperatures high enough for anharmonicity to be essential rather than a mere perturbation, though, of course, low compared to the dissociation energy. In that regime, the expressions (20) and (22) allowed us to proceed a few steps further algebraically rather than numerically. On the other hand, it can be validly argued that it would be precisely at low temperatures than a quantum mechanical calculation such as this one is substantially superior to a valid classical one. $^{4,8}$ It should therefore be realized that the restriction, in this section, to high temperatures was made for convenience rather than by necessity, primarily because it is in this region that experimental data are now available. $^{6,15}$ A computation valid at low as well as high temperatures would begin numerical work after Eq. (17) rather than after Eq. (40) as is done here. This is quite feasible, involving, however, somewhat more computer time. Such a calculation is now in progress and will be reported later.

## IV. SUM OVER LATTICE FREQUENCIES

If our interest were indeed in an ideal gas of one species of diatomic molecules, then the evaluation of Eq. (17) in Sec. III, for photon energies $E_{l}$ $=E_{m+l}-E_{m}$ would be our final result. But, in fact, we are discussing the diatomic gas only as a model for an anharmonic solid. Restricting ourselves to one species of "molecule" therefore seems artificial; to be somewhat more realistic, we want to take account of the fact that the lattice frequencies span a continuous band from 0 to a fixed $\omega_{max}$. A simple way of simulating this is to integrate the result of Sec. III, which contains a frequency $\omega$ defined in terms of the parameter of the Morse potential by Eq. (7), over the known frequency spectrum of the lattice; the reader may think of this process as approximating the anharmonic lattice by a gas of independent diatomic anharmonic molecules not of one species but of many species, the basic frequencies of the molecules being chosen so as to match the known frequency distribution of the lattice.

Though plausible, it should be clear that this process is also somewhat artificial. The physical basis for integrating over a frequency distribution is the known theorem that the system of coupled harmonic oscillators can, by a canonical transformation, be decomposed into a system of uncoupled harmonic oscillators (each with its own frequency which is, in principle, known). This theorem does not apply to anharmonic oscillators; a system of coupled oscillators that are essentially anharmonic cannot be decomposed into a system of uncoupled oscillators. The conventional way to get around this and utilize the theorem after all is to begin with the harmonic approximation, make the decoupling transformation, and then consider the anharmonicity as a perturbation. That approach has been critized-cogently, we believe-as invalid for problems that are essentially, rather than just slightly, anharmonic. $^{4,8}$ This is therefore, not the approach of the present paper. We have instead chosen to start by approximating the system by an assembly of oscillators which are essentially anharmonic but, for simplicity, uncoupled. Consequently, our subsequent integration over lattice frequencies, which derives from the other approximation, may seem to be a mixture of two different models. Nonetheless, an integration over the known lattice frequencies will surely provide more realism than restriction to a single frequency alone would.

To perform this integration over frequencies we use the Debye approximation

$$g(\omega)= \begin{cases}\omega^{2}, & 0<\omega<\omega_{\max } \\ 0, & \text { otherwise, }\end{cases}\qquad(27)$$

with the fixed $\omega_{max}$ is chosen to fit the known reststrahl frequency. The dissociation energy $D$ but not the reduced mass $\mu$, are held constant in the integration. This is justified by the fact that every normal mode of the solid involves the same force constants, so that the dissociation energy-the energy needed to break a bond-is the same for each mode; whereas the effective mass, being proportional to the number of atoms that are more or less in phase, varies from mode to mode.

The absorption from such a lattice or assembly of oscillators is then (omitting multiplicative constants)

$$\alpha_{t o t}=\int_{0}^{\omega_{\max }} d \omega \omega^{2} \sum_{\Delta=1} \sum_{m=0} \alpha\left(\omega, E_{l}, T\right) \delta(u), \quad(28)$$

with $\alpha(\omega, E_{l}, T)$ given by (17),

$$u=u_{m, \Delta}(\omega)=\hbar^{-1}\left[E_{m+\Delta}(\omega)-E_{m}(\omega)-E_{l}\right] \quad(29)$$

and the Dirac delta function providing conservation of energy. Interchanging order of integration and summation then gives

$$\alpha_{t o t}=\sum_{\Delta=1} \sum_{m=0} \frac{\omega^{* 2} \alpha\left(\omega^{*}, E_{l}, T\right)}{u^{\prime}\left(\omega^{*}\right)},\qquad(30)$$

where

$$u_{m, \Delta}^{\prime}(\omega)=\frac{d u_{m, \Delta}(\omega)}{d \omega}\qquad(31)$$

and $\omega^{*}$ is the solution of
$$u_{m, \Delta}(\omega)=0\qquad(32)$$
for those values of $m$ and $\Delta$ for which the solution is physically acceptable (i. e., real and smaller than $\omega_{max}$), and zero otherwise. The use of Eq.(6) shows that Eq. (31) reads, explicitly,
$$u^{\prime}\left(\omega^{*}\right)=\Delta\left[1-2 k^{-1}(2 m+1+\Delta)\right].\qquad(33)$$

If we scale all energies to the reststrahl energy $\hbar \omega_{max}$, i. e., write
$$\begin{aligned}
& x=\hbar \omega / \hbar \omega_{\max }, \quad A=(2 m+1+\Delta) / k_{\min }, \\
& \bar{\beta}=\beta \hbar \omega_{\max }, \quad k_{\min }=4 D / \hbar \omega_{\max }=k x, \\
& \bar{E}_{l}=E_{l} / \hbar \omega_{\max }, \quad y=\bar{E}_{l} / \Delta, \\
& \bar{E}_{m}=E_{m} / \hbar \omega_{\max },
\end{aligned}\qquad(34)$$
then Eq. (33) becomes
$$u^{\prime}=\Delta\left(1-2 A x^{*}\right)\qquad(35)$$
and Eq. (32) becomes
$$A_{m,\Delta}x^{2}-x+y=0;$$
the solution that is of physical significance is
$$x^{*}=\left[1-(1-4Ay)^{1/2}\right]/2A.$$

The partition function (26) becomes
$$Z=(\bar{\beta} x)^{-1}\left[1+4(k \beta)^{-1}\right]\qquad(37)$$
and the matrix element (14) reads
$$\gamma^{2}=(x \Delta)^{-2} f(k, m),\qquad(38)$$
with
$$f(k,m)=\frac {(k-1-2m)(k-1-2m-2\Delta )}{(k-1-2m-\Delta )^{2}}\frac {\begin{pmatrix} m+\Delta \\ \Delta \end{pmatrix}}{\begin{pmatrix} k-m-1 \\ \Delta \end{pmatrix}}.$$

Substituting all this into Eq. (30) with Eq. (17) gives
$$\alpha_{\text {tot }}=\bar{E}_{l} \bar{\beta}^{2} \sum_{\Delta=1} \Delta^{-3} \sum_{m=0} \frac{x^{*} e^{-\bar{\beta} \bar{E}_{m}} f(k, m)}{\left[1+4(k \bar{\beta})^{-1}\right]\left(1-2 A x^{*}\right)}. \quad(40)$$

As before, we have omitted multiplicative constants; we have set
$$(e^{-\overline {\beta}\overline {E}_{m+\Delta}}-e^{-\overline {\beta}\overline {E}_{m}})-(1-e^{-\overline {\beta}\overline {E}_{l}})e^{-\overline {\beta}\overline {E}_{m}}$$
using (32) and allowed the first factor to be written $\bar{\beta} \bar{E}_{l}$ as is appropriate in our temperature range; and from Eq. (6), $\bar{E}_{m}$ is given by
$$\bar{E}_{m}=\left(m+\frac{1}{2}\right) x^{*}-\left(m+\frac{1}{2}\right)^{2} x^{* 2} / k_{\min }.\qquad(41)$$

### V. NUMERICAL ESTIMATES

Our real interest is in alkali halide crystals, but the model is that of a gas of individual molecules. There is some question, therefore, wheth-

<table><thead><tr><td><b>TABLE I. Physical constants, and parameters needed derived from them, for KCl and NaCl.</b></td><td></td><td></td></tr></thead><tbody><tr><td></td><td><b>KCl</b></td><td><b>NaCl</b></td></tr><tr><td><b>$r_{0}(\hat {A})$</b></td><td><b>2.76</b></td><td><b>2.36</b></td></tr><tr><td><b>$\overline {h}ω_{max}(eV)$</b></td><td><b>0.0342</b></td><td><b>0.0466</b></td></tr><tr><td><b>$D(eV)$</b></td><td><b>4.35</b></td><td><b>4.25</b></td></tr><tr><td><b>μ(atomic masses)</b></td><td><b>18.4</b></td><td><b>13.8</b></td></tr><tr><td><b>$k_{min}$</b></td><td><b>505</b></td><td><b>377</b></td></tr><tr><td><b>$T/(hω_{max}/k_{B})(^{\circ }K)$</b></td><td><b>400</b></td><td><b>524</b></td></tr><tr><td><b>$a_{max}(A^{-1})$</b></td><td><b>0.783</b></td><td><b>0.895</b></td></tr></tbody></table>

er we should evaluate our formulas with numbers appropriate to solid alkali halides, or to gaseous ones. We chose the latter. They are collected in Table I. Its first four lines are constants for diatomic molecules taken from Ref. 16, the others are from Eqs. (7) and (34).

We also remember that at room temperature, $k_{B} T=\beta^{-1}$ is about $0.025 eV$ . Table I shows that the spacing $\hbar \omega_{max }$ of low-lying levels is about that energy, but that the dissociation energy $D$ is larger by a factor of 100. Excitation of lower-lying ex- cited states is therefore quite probable for room temperature to perhaps $1000^{\circ} K$ (the region for which data are available $^{6}$ ), but excitation beyond the bound states is quite improbable at such temperatures. Thus, the assumptions used in the preceding section, viz., that $\beta \hbar \omega<1$ but $k_{min }$  $\times \beta \hbar \omega_{ max } \gg 1$ are quite appropriate.

We can now proceed to evaluate Eq. (40) numerically. Results are presented in two kinds of figures: Fig. 1 gives absorption as a function of photon energy, for several fixed temperatures, and for $KCl$ and $NaCl$ ; Fig. 2, as a function of temperature, for several fixed energies for $KCl$ . Experimental results are also shown in Fig. 2, arbitrarily scaled. Both photon energies and temperatures are scaled to the maximum vibrational frequency according to Eq. (34).

At low temperatures, Fig. 1 shows sharp discontinuities at points close to integer values of the photon energy; this is a consequence of the need for a transition across $n$ levels $(\Delta=n, n$ -phonon transitions) when $\bar{E}_{l}=E_{l} / \hbar \omega$ is greater than $n$ , whereas transitions across only $n-1$ levels which, by (16), are much more probable, suffice for $\bar{E}_{l}<n$ . At higher temperatures, the higher probability of initial excited states, and the consequent availability of many more transitions that satisfy the energy conservation requirement, smooths out the discontinuities. It is interesting that similar structure appears in Ref. 8, though it is based on a wholly classical calculation.

The curves on the log-log scales of Fig. 2 are nearly straight lines, suggesting that the power law, $\alpha \sim T^{j}$ does hold approximately; but $j$ is

![](./images/813223879345438721_1.jpg)

FIG. 1. Absorption vs photon energy at various temperatures, for KCl (a) and NaCl (b). In each case the photon energy is scaled to the fundamental or reststrahl mode (see Table I). The absorption scale is arbitrary.

appreciably smaller than $n-1$ (viz., about 4 for $\bar{E}_{l}=7$, and about 2 for $\bar{E}_{l}=3.36$, the normalized energy of a photon of wavelength $10.6 \mu \mathrm{m}$).
Agreement with experiment is much better than should be expected from the crudity of our model.

### VI. SUMMARY

We have approximated the absorption of light by a solid in spectral regions well beyond that of the energy of lattice vibrations by a quantum mechan-
ical calculation of a solvable anharmonic (Morse) potential. The virtue of the calculation is the com- plete avoidance of the harmonic approximation in this highly anharmonic situation; its weakness- describing a solid initially by an assembly of di- atomic molecules-is somewhat ameliorated by performing a sum over the lattice frequencies (ap- proximated by a Debye spectrum) in the end. At any fixed temperature, the absorption versus fre- quency curves show discontinuities at the fre- quencies at which additional phonons are needed to make the process allowable energetically; the discontinuities become less sharp as temperature goes up, and the envelope of the curve is always roughly exponential. At fixed frequencies, on the other hand, the absorption vs temperature curves approximately follow a power law $\alpha \sim T^{j}$, with $j$ ap- preciably smaller than the number of phonons in- volved in the process. Agreement with experiment is reasonably good.

![](./images/813223879345438721_2.jpg)

FIG. 2. Absorption vs temperature for various pho- ton energies, for KCl. Absorption scale is arbitrary; photon energies as in Fig. 1. Data points from Ref. 15.

### ACKNOWLEDGMENTS

Part of this work was done at the Aspen Center for Physics, Aspen, Colo. I am indebted to Dr. M. Hass, Dr. J. A. Harrington, Dr. A. R. Ruffa, Dr. B. M. Klein, and Professor E. Merzbacher for many discussions.

### APPENDIX: ANALOGOUS EXPRESSIONS FOR THE HARMONIC OSCILLATOR

We should compare the matrix elements (12), (14), or (15) with the well known result for the harmonic oscillator
$$
\gamma_{m, m+\Delta}^{2}=\gamma_{m+\Delta, m}^{2}=\frac{\delta_{\Delta, 1}(m+1)}{2 \mu \omega / \hbar}. \tag{42}
$$

Since $ka^2$ turns out to be exactly $2\mu\omega/\hbar$ when the Morse potential (1) is expanded abouts its minimum to determine $\omega$, this is in exact agreement with the first, but only the first of Eqs. (16); i.e., in the harmonic-oscillator case, only transitions between adjacent states (one-phonon transitions) can be induced by electric dipole radiation, while with the Morse potential transitions between all levels are allowed (though with decreasing probability as the separation between levels increases). We also write down expressions for the matrix elements of powers of $x$ (which are powers of $r^2=x^2+y^2+z^2$):

$$
\begin{aligned}
\left\langle x^{2}\right\rangle_{m, m+\Delta}^{2}= & (2 \mu \omega / \hbar)^{-2} \\
& \times\left[(2 m+1) \delta_{\Delta, 0}+(m+1)(m+2) \delta_{\Delta, 2}\right], \\
\left\langle x^{3}\right\rangle_{m, m+\Delta}^{2}= & (2 \mu \omega / \hbar)^{-3} \\
& \times\left[9(m+1) \delta_{\Delta, 1}+(m+1)(m+2)(m+3) \delta_{\Delta, 3}\right], \\
\left\langle x^{4}\right\rangle_{m, m+\Delta}^{2}= & (2 \mu \omega / \hbar)^{-4}\left[9\left(2 m^{2}+2 m+1\right)^{2} \delta_{\Delta, 0}\right. \\
& +(3+2 m)^{2}(m+1)(m+2) \delta_{\Delta, 2} \\
& \left.+(m+1)(m+2)(m+3)(m+4) \delta_{\Delta, 4}\right].
\end{aligned}
\tag{43}
$$

In absorption calculations, these matrix elements may arise in two ways: when higher-order multipole radiation is considered, or when the harmonic-oscillator potential is perturbed by cubic or quartic terms. The expressions are clearly reminescent of Eq. (16) but still have the property of vanishing beyond a certain-small-level separation. It is now clear that the rigorous vanishing of most of the matrix elements is an artifact introduced by beginning with the harmonic oscillator potential, which is not a natural start if one intends to deal with high-lying levels, with anharmonicity that is large rather than a perturbation, or with high temperatures. The Morse potential, in which anharmonicity is appears *ab initio* rather than as a perturbation, is a potential which is not only more natural but also likely to provide a better basis as a starting point.

It is also instructive to compare the partition function (22) or (26) with the one for the harmonic oscillator. Since the $E_n$ are now equally spaced, viz., given by $\hbar\omega(n+\frac{1}{2})$, i. e., by Eq. (6) without the quadratic term, $Z$ sums exactly to $(1-e^{-\beta\hbar\omega})^{-1}$ and in the limit of small $\beta$ (high temperature) thus approaches $(\beta\hbar\omega)^{-1}$ just as Eq. (26) does. However, more importantly, the sum must also be taken in the numerator of Eq. (17), for (18) is, precisely because of the equal spacing of energy levels, satisfied for all levels if it is satisfied for any one $m$. Since, by (43), $r_{m,m+\Delta}^2$ goes as $m^\Delta$, the sum over $m$ will go as $(1-e^{-\beta\hbar\omega})^{-\Delta}$, or $(\beta\hbar\omega)^{-\Delta}$ in the small-$\beta$ limit. Dividing by $Z$ then shows that the absorption goes as $(\beta\hbar\omega)^{-\Delta-1}\sim T^{\Delta-1}$ in the high-temperature limit. This is the usual result obtained in many more complicated methods but basically analogous to this one, and is quite different from the present result which gives a weaker dependence (see Figs. 1 and 2).

This $T^{\Delta-1}$ dependence of the absorption coefficient in any approximation that begins with the harmonic oscillator can also be derived in a way that is, or at least appears to be, different, by using the language of second quantization; let us verbalize this briefly. What used to be called the $n$th excited state of the harmonic oscillator is now referred to as the presence of $n$ phonons; the quantity

$$
N^{(a)}=\sum_{n} \frac{E_{n} e^{-\beta E_{n}}}{Z}=\left(e^{-\beta E^{(a)}}-1\right)^{-1},
$$

previously the mean energy of the system at temperature $T$, is now viewed as the phonon occupation number of system $(a)$ (quantitatively correctly, if phonons obey Bose-Einstein statistics). If $i$ systems of harmonic oscillators are then caused to interact (by some perturbation, such as an incoming photon), the probability of that process is$^{17}$

$$
\begin{aligned}
\left(1+N^{(a)}\right)\left(1+N^{(b)}\right) \ldots & \left(1+N^{(i)}\right) \\
& -N^{(a)} N^{(b)} \ldots N^{(i)}.
\end{aligned}
$$

The leading term, which involves $i-1$ of the $N$'s, will again go as $T^{i-1}$ for high temperature, where $i$, analogous to $\Delta$ in the preceding paragraph, is the number of phonons.

---
$^{1}$J. R. Hardy and B. S. Agrawal, Appl. Phys. Lett. $\underline{22}$, 236 (1973).
$^{2}$M. Sparks and L. J. Sham, Solid State Commun. $\underline{11}$, 1451 (1973).
$^{3}$T. C. McGill, R. W. Hellwarth, M. Mangir, and H. V. Winston, J. Phys. Chem. Solids (to be published).
$^{4}$D. L. Mills and A. A. Maradudin, Phys. Rev. B $\underline{8}$, 1617 (1973).
$^{5}$H. B. Rosenstock, J. Appl. Phys. $\underline{44}$, 4473 (1973).
$^{6}$J. A. Harrington and M. Hass, Phys. Rev. Lett. $\underline{31}$, 710 (1973).
$^{7}$M. Sparks and L. J. Sham, Phys. Rev. Lett. $\underline{31}$, 714 (1973).
$^{8}$A. A. Maradudin and D. L. Mills, Phys. Rev. Lett. $\underline{31}$, 718 (1973).
$^{9}$P. M. Morse, Phys. Rev. $\underline{34}$, 57 (1929).
$^{10}$See, e.g., L. I. Schiff, *Quantum Mechanics* (McGraw-Hill, New York, 1955), Chap. X.
$^{11}$C. L. Pekeris, Phys. Rev. $\underline{45}$, 98 (1934).
$^{12}$P. M. Morse and H. Feshbach, *Methods of Theoretical Physics* (McGraw-Hill, New York, 1953), part I, p. 784.
$^{13}$K. Scholz, Z. Phys. $\underline{78}$, 751 (1932).
$^{14}$E. Jahnke and F. Emde, *Tables of Functions*, 4th ed. (Dover, New York, 1945), p. 32.
$^{15}$J. A. Harrington and M. Hass (private communication).

I am grateful to these authors for the use of unpublished data.

¹⁶*American Institute of Physics Handbook*, 3rd ed. (McGraw-Hill, New York, 1972), p. 7-176.

¹⁷P. A. M. Dirac, *Principles of Quantum Mechanics*, 3rd ed. (Oxford, U. P., Oxford, England, 1947), Sec. 61.