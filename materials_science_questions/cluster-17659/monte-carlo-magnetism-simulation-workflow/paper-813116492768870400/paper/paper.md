# Anomalous zero-field muon spin relaxation in highly disordered magnets

D. R. Noakes
Physics Department, Virginia State University, Petersburg, Virginia 23806

G. M. Kalvius
Physik Department, Technische Universität München, D-85747 Garching, Germany

(Received 17 January 1997)

Low-temperature zero-field muon spin relaxation spectra from several disordered magnetic materials show static-field relaxation behavior that cannot be properly represented by the Gaussian or Lorentzian distributions commonly used in the analysis of such data (Kubo-Toyabe relaxation). In the case of ${\mathrm{CeCu}}_{0.2}{\mathrm{Ni}}_{0.8}\mathrm{Sn}$, a Gaussian distribution of second moments, convoluted with a Gaussian form of field distribution, produces a closed-form modified Kubo-Toyabe relaxation function that fits the data well. Its characteristic feature is a shallow polarization minimum before recovery to the 1/3 asymptote. Any microscopic model that reproduces such shallow static Kubo-Toyabe relaxation must do so by generating an excess of low-field sites.
[S0163-1829(97)00630-9]

Zero-field (ZF) positive muon spin relaxation ($\mu$SR) (Ref. 1) is a useful probe of disordered magnetism. $^{2}$ The interaction of the muon magnetic moment with the magnetic moments in the material is usually discussed in an effective-field model, where the atomic moments create a magnetic field at the muon site, about which the muon spin precesses. If there is any kind of magnetic ordering or spin-freezing "transition" temperature $T_{M}$ in a material, then well below this temperature all magnetic moments usually $^{1,3}$ become completely static on the $\mu$SR time scale ($\sim$10 ns). They generate a distribution of probability $P(\mathbf{B})$ of static magnetic field at the muon site. In magnetically well-ordered materials, there may be a nearly unique magnetic field magnitude at the muon, which generates "coherent" oscillation of muon polarization. In strongly disordered materials, such as spin glasses and their relatives, the field distribution at the muon site also becomes strongly disordered and requires a statistical (Kubo-Toyabe$^{4}$) analysis. In systems dense with uncorrelated magnetic moments, the probability distribution of each vector component of the local magnetic field, $P(B_{i})$, should be to a good approximation Gaussian, whereas in the dilute limit of sparse moments the field-component distribution is expected to become Lorentzian. $^{5}$ The majority of $\mu$SR experiments are performed on polycrystalline or powder samples, and, for them, the static ZF Kubo-Toyabe (KT) relaxation function that describes the time evolution of the muon polarization is

$$
G_{z}(t)=\frac{1}{3}+\frac{2}{3} \int P(|\mathbf{B}|) \cos \left(\gamma_{\mu}|\mathbf{B}| t\right) d|\mathbf{B}|, \tag{1}
$$

where

$$
P(|\mathbf{B}|) \equiv \int P(\mathbf{B})|\mathbf{B}|^{2} d \Omega_{B} \tag{2}
$$

(an integral over the sphere of all possible field directions, $d\Omega$ being the element of solid angle) and $\gamma_{\mu}=2\pi(13.55$ kHz/G) is the gyromagnetic ratio of the muon. In the Gaussian and Lorentzian cases, the component distributions are assumed to be statistically independent,

$$
P(\mathbf{B})=P(B_{x}) P(B_{y}) P(B_{z}), \tag{3}
$$

and then

$$
G_{z}^{G}(t)=\frac{1}{3}+\frac{2}{3}\left(1-\Delta^{2} t^{2}\right) \exp \left(-\frac{\Delta^{2} t^{2}}{2}\right), \tag{4}
$$

$$
G_{z}^{L}(t)=\frac{1}{3}+\frac{2}{3}(1-a t) \exp (-a t), \tag{5}
$$

where, for the Gaussian, $\Delta/\gamma_{\mu}$ is the rms field component, and for the Lorentzian, $a/\gamma_{\mu}$ is the component distribution half-width at half-maximum. In both of these functions, the polarization drops, as time increases, from its initial value to a single minimum before recovering to 1/3 (of initial) at late times. The "1/3 asymptote" is characteristic of ZF $\mu$SR in static fields. In this situation, each muon sees a unique local field for its entire life in the material, and in a polycrystal, on average, 1/3 of each muon's spin will be along that field, and will not evolve in time: 1/3 of the initial polarization cannot change. When dynamics are fast enough to change the local field a muon sees within the time window of the experiment, and then no part of the muon's spin remains along the local field for its lifetime: The total polarization evolves with time, and eventually will be lost. This feature allows the observer to discriminate between a static (frozen) and a dynamic (fluctuating) spin system and is one of the strengths of ZF-$\mu$SR spectroscopy. In particular, at the onset of dynamic behavior, relaxation from the 1/3 asymptote is seen first,

which allows the measurement of very low fluctuation rates.
The static Gaussian Kubo-Toyabe function has zero slope at
$t=0$ and a well-developed minimum, while the Lorentzian
KT function has negative initial slope and a shallower mini-
mum. Somewhat surprisingly, these two simple relaxation
functions have sufficed to describe the vast majority of ob-
served static ZF muon spin relaxation in spin-frozen disor-
dered magnetic systems.

Recently, however, several seemingly unrelated disor-
dered magnetic materials have exhibited static ZF-$\mu$SR re-
laxation functions that cannot be fit by either of the two
standard functions above. In the geometrically frustrated py-
rochlore $\text{Y}_2\text{Mo}_2\text{O}_7$, very nearly static ZF relaxation with a
minimum too shallow for the Gaussian KT function (the mo-
ments are dense) has been observed below a spin freezing. $ ^6$
In spin-glassy icosahedral Al-Mn-Si quasicrystal, while the
ZF-$\mu$SR spectra are complicated by inhomogeneous freez-
ing, the frozen-region signal appears to execute *monotonic*
relaxation (it does not go through a minimum) to the 1/3
asymptote. $ ^7$

It is generally known that the depth of the minimum in
static KT relaxation can be reduced if there are two or more
muon sites whose $\Delta$ values differ so that they ‘‘interfere’’
appropriately in the resulting sum of relaxation functions. As
was discussed in Ref. 7, $N$ Gaussian sites of equal population
and equally spaced field widths, $\Delta_n=n\Delta_1$ for $n=1$ to $N$,
generate a set of static relaxation functions with successively
shallower minima as $N$ increases. In the limit $N\rightarrow\infty$, they
become a monotonic Gaussian relaxation function to the 1/3
asymptote. No member of that set fits the data we will de-
scribe below well, as the minimum produced by that proce-
dure is too broad as soon as $N>1$, but this example suggests
the use of a set of sites to create a variety of $\Delta$ values that
combine to reduce the depth of the minimum. Instead of an
equally spaced set of discrete $\Delta$ values, in some cases there
might be a cluster of $\Delta$ values in a limited range around a
central value $\Delta_0$. One way to model such a case is with a
Gaussian probability distribution of $\Delta$ values around $\Delta_0$,
with rms width $w$, $\rho_G(\Delta_0,w,\Delta)$, which is convoluted with
the Gaussian field distribution $P_G(0,\Delta,B_i)$ (representing a
single site with a particular value of $\Delta$), to create a
‘‘Gaussian-broadened Gaussian’’ (GBG) field distribution

$$
P_{\text{GBG}}(\Delta_0,w,B_i)=\int \rho_G(\Delta_0,w,\Delta)P_G(0,\Delta,B_i)d\Delta. \quad (6)
$$

The normalization of $\rho$, however, is not trivial, because
$P_G(0,\Delta,B_i)$ is nominally defined only for $\Delta>0$. The nor-
malization integral for $\rho$ may be cut off at zero (resulting in
terms involving error functions), but simpler mathematical
forms involving only small qualitative differences in behav-
ior result from defining $P_G(0,-\Delta,B_i)\equiv P_G(0,\Delta,B_i)$. While
we do not know a closed-form expression for $P_{\text{GBG}}$, the
order of integrations in Fourier transformation [Eq. (1)] and
convolution [Eq. (6)] can be exchanged, and the overall
Kubo-Toyabe relaxation function then expressed as the con-
volution of the single-site KT function with the distribution
of widths, with solution

![](./images/813116492768870400_1.jpg)

FIG. 1. The static ‘‘Gaussian-broadened Gaussian’’ Kubo-
Toyabe relaxation function for the $R$ values shown.

$$
\begin{aligned}
G_z^{\mathrm{GBG}}(t)= & \int \rho_G\left(\Delta_0, w, \Delta\right) G_z^G(t) d \Delta \\
= & \frac{1}{3}+\frac{2}{3}\left(\frac{1+R^2}{1+R^2+R^2 \Delta_{\mathrm{eff}}^2 t^2}\right)^{3 / 2} \\
& \times\left(1-\frac{\Delta_{\mathrm{eff}}^2 t^2}{1+R^2+R^2 \Delta_{\mathrm{eff}}^2 t^2}\right) \\
& \times \exp \left(\frac{-\Delta_{\mathrm{eff}}^2 t^2}{2\left(1+R^2+R^2 \Delta_{\mathrm{eff}}^2 t^2\right)}\right),
\end{aligned} \quad (7)
$$

where

$$
\Delta_{\text{eff}}^2=\Delta_0^2+w^2, \quad (8)
$$

$$
R=w/\Delta_0. \quad (9)
$$

We have written this in terms of new parameters $\Delta_{\text{eff}}$ and
$R$ because the geometric sum of the two width parameters
governs the initial rate of relaxation, while the ratio of the
two governs the depth of the minimum. Starting from the
standard Gaussian KT end point at $R=0$, the depth of mini-
mum decreases as $R$ increases, until the relaxation becomes
monotonic (to 1/3) when $R=1$. This is illustrated in Fig. 1,
for a selection of $R$ values. As $R$ increases beyond unity, the
shape of the monotonic relaxation changes in a subtle man-
ner that may prove difficult to resolve experimentally: The
range $0\leqslant R\leqslant 1$ is of interest for this work.

Within the effective-field approximation, shallow KT re-
laxation requires an excess of low-field sites, as follows. For
a polycrystalline sample, the KT relaxation function, Eq. (1),
is a cosine Fourier transform of the distribution of field mag-
nitude, $P(|\mathbf{B}|)$ (plus constant 1/3). If there is a local maxi-
mum in $P(|\mathbf{B}|)$ at any nonzero $|\mathbf{B}|$, the Fourier transform
will execute oscillation with at least one minimum. Mono-
tonic relaxation to 1/3 can only be achieved if there are no
local maxima in $P(|\mathbf{B}|)$. Meanwhile, $P(|\mathbf{B}|)$ is $|\mathbf{B}|^2$ times a
surface integral [Eq. (2)] of the product of three orthogonal
copies [Eq. (3)] of the field-component distribution $P(B_i)$. If
$P(B_i)$ is finite at $B_i=0$, then the $|\mathbf{B}|^2$ factor forces $P(|\mathbf{B}|)$ to
zero as $|\mathbf{B}|\rightarrow 0$, and since the distributions must have a finite
norm, this forces $P(|\mathbf{B}|)$ to have at least one maximum at

![](./images/813116492768870400_2.jpg)

FIG. 2. ZF-$\mu$SR asymmetry spectrum in polycrystalline
CeCu$_{0.2}$Ni$_{0.8}$Sn at 0.08 K. The dashed line is a fit of the static
Gaussian Kubo-Toyabe relaxation function to the data. The solid
line is a fit of the static ‘‘Gaussian-broadened Gaussian’’ KT func-
tion described in the text.

finite $|\mathbf{B}|$. To generate monotonic static $KT$ relaxation, there-
fore, $P(B_{i})$ must diverge as $B_{i}\rightarrow0$ (while retaining the finite
norm). Physically, this means that as the KT minimum gets
shallower, for a constant initial relaxation rate (that is, fixed
rms field), the probability of low fields increases relative to
the probability of higher fields. To reduce the minimum to
zero, the probability of the lowest field (components) must
increase without limit, but narrowly, so as to leave the nor-
malization integral finite.

The authors of this paper have been involved in ZF-
$\mu$SR studies of copper-doped Kondo lattice CeNiSn. In pure
CeNiSn, there is no evidence of magnetic ordering, but weak
dynamic magnetic correlations are seen in $\mu$SR, and they
continue to be dynamic to $\sim$10 mK.$^{8}$ In CeCu$_{0.1}$Ni$_{0.9}$Sn, the
magnetic correlations are stronger, a spin-freezing transition
of some sort occurs at $\approx$0.9 K, and well below that ZF-
$\mu$SR spectra again show static monotonic relaxation.$^{9}$ In
CeCu$_{0.2}$Ni$_{0.8}$Sn, the freezing transition is near 4 K. Figure 2
shows the ZF-$\mu$SR asymmetry spectrum from a polycrystal-
line sample of CeCu$_{0.2}$Ni$_{0.8}$Sn at 0.08 K,$^{10}$ which executes
static relaxation with a shallow minimum similar to that of
Y$_{2}$Mo$_{2}$O$_{7}$. The dashed line shows that a static Gaussian KT
function [Eq. (4)] can be made to fit the early and late parts
of the spectrum, but then cannot reproduce the minimum. A
static Lorentzian KT function also does not fit this spectrum
well: While it has a shallower minimum than the Gaussain
KT function, the observed initial rate of relaxation is too
slow relative to the time at which the minimum occurs to
match the time dependence of a Lorentzian KT function. The
solid line in Fig. 2 shows the excellent fit of $G_{z}^{\text{GBG}}$ to the
low-temperature CeCu$_{0.2}$Ni$_{0.8}$Sn data, with a deduced value
of $R$ near 0.5.

In the CeCu$_{x}$Ni$_{1-x}$Sn alloy system, when the magnetism
is strong enough to cause a freezing transition (there is no
evidence of spin freezing for $x<0.05$, $^{9}$ the onset concentra-
tion being between that and 0.1), the static frozen state pro-
duces a muon-site field distribution consistent with the
Gaussian-broadened Gaussian described here, *and the broad-
ening ratio R is a function of x*, achieving monotonic static
relaxation ($R\geqslant1$) for $x=0.1$, and decreasing to $\cong0.5$ for
$x=0.2$. A complete physical explanation would include a
description of how the magnetic moments in the material
generate such a static local field distribution. For small val-
ues of $R$, a variety of models might apply, but as $R$ ap-
proaches unity, and in particular, when the minimum is shal-
lower than that of the static Lorentzian KT function, a
reasonable model becomes quite difficult to construct.
Among the ideas we considered, and were forced to reject,
was random variation of the moment magnitude. The vast
majority of (local-moment) magnetic materials have stable,
well-defined, individual moment magnitudes. Disorder in
magnetism is usually positional and/or orientational; the mo-
ments’ magnitudes rarely vary. Thinking that the additional
randomness of magnitude of moment over a continuous
range from zero up to a maximum might be what we needed,
we incorporated it into Monte Carlo software used previ-
ously to determine the static field distributions to be expected
from uncorrelated frozen states of nondilute alloy spin
glasses.$^{11}$ This has consistently generated static relaxation
functions with minima *not* significantly shallower than for
constant-moment-magnitude cases with the same initial re-
laxation rate, and so does not appear to be the correct micro-
scopic model.

To our knowledge, no theoretical work has yet attempted
to determine what physically reasonable magnetic configura-
tions might generate local field (component) distributions
that diverge as $B_{i}\rightarrow0$. The Lorentzian field distribution is
well known to be the vanishing-concentration limit of dilute-
alloy uncorrelated random-field distributions, and our at-
tempts to reduce the depth of the Lorentzian KT minimum
by the introduction of a new dimension of uncorrelated ran-
domness to random alloy Monte Carlo simulations were un-
successful. This suggests that some unexpected kind of mag-
netic correlation is active in the materials where reduced
static KT minima have been observed. On the basis of the
convolution procedure used in the construction of both phe-
nomenological models above, Ref. 7 discussed the outline of
a model involving range-correlated magnetic moment (mag-
nitude) variation. Other, more radical, approaches might
involve (1) violation of the statistically-independent-
component [Eq. (3)] assumption for the vector field distribu-
tion, or (2) invalidation of the effective-field approximation
for the interaction of the $\mu^{+}$ spin with the host. For ZF
$\mu$SR, the latter has been found in cases where the muon is in
close interaction with only a very small number of host
moments,$^{12}$ and for small corrections at very high statistics.$^{13}$
The former has played no notable role in $\mu$SR to date (a toy
model is discussed in Ref. 11). Or (3) unusual magnetic ion
dynamics that somehow manage to preserve the 1/3 tail with-
out being static may be involved. We know of no credible
scheme for such dynamics at this time. Note that longitudinal
field (LF) $\mu$SR data from $i$-Al-Mn-Si (Ref. 7) and
CeCu$_{x}$Ni$_{1-x}$Sn ($x\geqslant0.1$) (Refs. 9 and 10) at the lowest tem-
peratures show that the late tails shift upward and remain
flat, behavior consistent with completely static local fields.
The application of GBG LF relaxation functions to those
data is a subject of future work.

In summary, recent $\mu$SR studies have revealed a number
of magnetic materials that, at low temperatures, cause static
zero-field relaxation spectra with minima too shallow to be

fit by either of the standard Kubo-Toyabe relaxation func- tions that until now have served to explain all static disor- dered cases. In at least two cases, the extreme case of mono- tonic static ZF relaxation has been observed, and in the $CeCu_{x} Ni_{1-x} Sn$ system, the shallowness of the minimum is a function of the dopant concentration. We have shown that a shallower minimum indicates an excess of low-field prob- ability in the local field distribution, and that in the case of static monotonic KT relaxation, the field-component prob- ability must diverge at zero. A static "Gaussian-broadened" Gaussian Kubo-Toyabe relaxation function was constructed, and fits the observed data in $CeCu_{0.2} Ni_{0.8} Sn$ , whereas a finite set of sites with equally spaced $\Delta$ values, suggested in a previous publication, does not fit those data. We do not yet have complete understanding of how the magnetism of the materials generates such a broadened field distribution with an excess of low fields: It may be that novel static magnetic correlations occur in the spin-frozen states of these solids.

This work was supported by U.S. DOE Grant No. DE- FG05-88ER45353 and by the BMBF (Germany) under Con- tract No. 03-KA-TU1-9.

\footnotetext{ $^{1}$ For recent reviews, see E. B. Karlsson, Solid State Phenomena as seen by Muons, Protons, and Excited Nuclei (Clarendon, Ox- ford, 1995); A. Schenck and F. N. Gygax, in Handbook of Mag- netic Materials, edited by K. H. J. Buschow (Elsevier, Amster- dam, 1995), Vol. 9, pp. 57-302.}
\footnotetext{ $^{2}$ T. Yamazaki, Nucl. Instrum. Methods Phys. Res. 199, 133(1982).}
\footnotetext{ $^{3}$ An exception occurs in some "perfectly" frustrated systems, where there is no more than partial ordering of the moments, and dynamics can persist to very low temperatures: See A. Keren, K. Kojima, L. P. Le, G. M. Luke, W. D. Wu, Y. J. Uemura, M. Takano, H. Dabkowska, and M. J. P. Gingras, Phys. Rev. B 53,6451 (1996), and references cited therein.}
\footnotetext{ $^{4}$ R. Kubo and T. Toyabe, in Magnetic Resonance and Relaxation, edited by R. Blinc (North-Holland, Amsterdam, 1967), pp. 810-823; R. Kubo, Hyperfine Interact. 8, 731 (1981).}
\footnotetext{ $^{5}$ L. R. Walker and R. E. Walstedt, Phys. Rev. B 22, 3816 (1980).}
\footnotetext{ $^{6}$ S. R. Dunsiger, R. F. Kiefl, K. H. Chow, B. D. Gaulin, M. J. P. Gingras, J. E. Greedan, A. Keren, K. Kojima, G. M. Luke, W. A. MacFarlane, N. P. Raju, J. E. Sonier, Y. J. Uemura, and W. D. Wu, J. Appl. Phys. 79, 6636 (1996).}
\footnotetext{ $^{7}$ D. R. Noakes, A. Ismail, E. J. Ansaldo, J. H. Brewer, G. M. Luke, P. Mendels, and S. J. Poon, Phys. Lett. A 199, 107 (1995).}
\footnotetext{ $^{8}$ A. Kratzer, G. M. Kalvius, T. Takabatake, G. Nakamoto, H. Fujii, and S. R. Kreitzman, Europhys. Lett. 19, 649 (1992); Y. Kagan and G. M. Kalvius, JETP Lett. 61, 758 (1995).}
\footnotetext{ $^{9}$ S. J. Flaschin, A. Kratzer, F. J. Burghart, G. M. Kalvius, R. Wäp pling, D. R. Noakes, R. Kadono, I. Watanabe, T. Takabatake, K. Kobayashi, G. Nakamoto, and H. Fujii, J. Phys. Condens. Matter8, 6967 (1996).}
\footnotetext{ $^{10}$ G. M. Kalvius, T. Takabatake, A. Kratzer, R. Wäppling, D. R. Noakes, S. J. Flaschin, F. J. Burghart, R. Kadono, I. Watanabe, A. Brückl, K. Neumaier, K. Andres, K. Kobayashi, G. Naka- moto, and H. Fujii, Hyperfine Interact. 104, 157 (1997).}
\footnotetext{ $^{11}$ D. R. Noakes, Phys. Rev. B 44, 5064 (1991). The notation $P(B)$ here is more correct than $P(H)$ used there.}
\footnotetext{ $^{12}$ Muonium, about which there is a large literature [see, e.g., B. D. Patterson, Rev. Mod. Phys. 60, 69 (1988); T. A. Claxton, Chem. Soc. Rev. 24, 437 (1995), and references cited therein]; and the $(F \mu F)^{-}$ molecular ion [see D. R. Noakes, E. J. Ansaldo, and G. M. Luke, J. Appl. Phys. 73, 5666 (1993), and references cited therein].}
\footnotetext{ $^{13}$ M. Celio, Phys. Rev. Lett. 56, 2720 (1986).}