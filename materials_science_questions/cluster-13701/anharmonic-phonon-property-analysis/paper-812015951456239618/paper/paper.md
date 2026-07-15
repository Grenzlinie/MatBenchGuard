# Fluctuating Cu-O-Cu bond model of high-temperature superconductivity

D. M. NEWNS*† AND C. C. TSUEI*
IBM T.J. Watson Research Center, Yorktown Heights, New York 10598, USA
*These authors contributed equally to this work
†e-mail: dennisn@us.ibm.com

Published online: 18 February 2007; doi:10.1038/nphys542

Twenty years of research have yet to produce a consensus on the origin of high-temperature superconductivity (HTS). However, several generic characteristics of the copper oxide superconductors have emerged as the essential ingredients of and/or constraints on any viable microscopic model of HTS. Besides a critical temperature $T_c$ of the order of 100 K, they include a $d$-wave superconducting gap with Fermi liquid nodal excitations, a pseudogap with $d$-symmetry and the characteristic temperature scale $T^*$, an anomalous doping-dependent oxygen isotope shift, nanometre-scale gap inhomogeneity and so on. The isotope shift implies a key role for oxygen vibrations, but conventional Bardeen–Cooper–Schrieffer single-phonon coupling is essentially forbidden by symmetry and by the on-site Coulomb interaction $U$. Here we invoke the nonlinear modulation of the Cu–Cu bond by planar oxygen vibrations. The Fermi liquid nature of the $d$-wave superconducting ground state supports a weak-coupling treatment of this modulation. The dominant fluctuations are manifested in a pattern of oxygen vibrational square amplitudes with quadrupolar symmetry around a given Cu site. On the basis of such bond fluctuations, both dynamic and static, we can understand the salient features of HTS.

Great strides towards understanding HTS have been made during the past 20 years of intense experimental and theoretical research on cuprate superconductors¹⁻². However, no general consensus on a specific microscopic pairing mechanism, capable of consistently explaining the complex phenomenology of the superconducting and normal states, has emerged.

Among the highly unconventional properties of the cuprate superconductors are the $d$-wave symmetry of the superconducting gap³ and the presence of a pseudogap also with $d$-wave symmetry⁴. Theoretical insight is provided by study of the low-energy excitations around the node in the $d$-wave gap, where disparate low-temperature experiments including specific heat⁵, transport⁶⁻⁸, and penetration depth⁹, together with angle-resolved photoemission spectroscopy (ARPES)¹⁰, can all be interpreted in terms of a Fermi liquid description. This suggests the plausibility of a broadly Bardeen–Cooper–Schrieffer (BCS) framework², of which an important consequence is that the large on-site Coulomb repulsion $U$ (ref. 11)—renormalized to an interaction of the order of the electronic bandwidth—does not enter into $d$-wave pairing to first order.

In conventional superconductivity the isotope exponent $\alpha$ has been key in signalling the role of phonons in the pairing mechanism. HTS shows a universal, anomalous doping-dependent isotope shift¹², which suggests that phonons may again be playing a key role. Further evidence for the role of the electron–phonon interaction in HTS comes from spectroscopy. Recent ARPES experiments have demonstrated a kink in the energy band dispersion¹³, which is interpreted as of electron–phonon origin. Strong electron–phonon coupling is also implied by the anomalous universal doping-dependent softening of the planar oxygen-stretch half-breathing mode¹⁴⁻¹⁶. An anomalous, universal temperature dependence of the out-of-plane O-bend modes, which, in Raman¹⁷,¹⁸ and neutron scattering¹⁴,¹⁹,²⁰, are found to soften below $T_c$, strongly signals their involvement in pairing. A similar effect on line intensity is found in YBCO for the O-stretch mode²¹. Extensive theoretical studies¹³,²²⁻³² have been prompted by this evidence for electron–phonon coupling, but have still not led to a satisfactory comprehensive theory of HTS.

Here, in re-examining phonon coupling, we find a novel microscopic pairing mechanism, which can indeed explain the essence of HTS phenomena: high $T_c$ values, $d$-wave pairing, $d$-symmetry pseudogap, anomalous isotope shift and nanoscale gap inhomogeneity³³. Although the effects of $U$ are manifested¹¹, here we shall focus on interactions directly responsible for pairing, allowing for $U$ indirectly by decoupling from on-site charge fluctuations. We start by considering how electron motion in the CuO₂ plane—the universal active component of HTS materials—is modified by vibrations of the planar oxygen, which is known from site-selective isotope substitution to be the oxygen active in pairing³⁴. The CuO₂ plane is a square lattice of divalent Cu ions with oxygen ions located at the centres of the Cu–Cu bond (Fig. 1a). Only the highest-lying $3d_{x^2-y^2}$ orbital (Fig. 1b) plays an active role, crystal-field effects relegating the other Cu $3d^9$ orbitals to corelike status.

Let us look at a single Cu–Cu bond between $3d_{x^2-y^2}$ orbitals located on atoms labelled 1 and 2 (Fig. 1a,b). In a one-band model the kinetic energy (band width) comes predominantly from the nearest-neighbour hopping-matrix elements $t$ in the bonds. For the bond 1–2 this term in the hamiltonian is

$$
h_{12}^e=-t\sum_{\sigma}\left(c_{1,\sigma}^+c_{2,\sigma}+c_{2,\sigma}^+c_{1,\sigma}\right), \tag{1}
$$

where the $c_{i,\sigma}^+$ ($c_{i,\sigma}$) are fermion creation (destruction) operators for Cu site $i$ and spin $\sigma$. The intersite hopping actually occurs via superexchange, that is wavefunction overlap between the

![](./images/812015951456239618_1.jpg)

**Figure 1** Oxygen degrees of freedom and electron–phonon coupling. a, The unit cell in the $CuO_2$ plane, with Cu atoms (yellow) and O atoms (red), showing $x$, $y$ and $z$ vibrational modes (arrows). b, The Cu $3d_{x^2-y^2}$ and O $2p_x$ orbitals, illustrating the effect of an O $z$ displacement (green arrows), positive sense (top panel) and negative sense (bottom panel). c, Bare oxygen anharmonic potential (3): full (dashed) curves with positive (negative) harmonic coefficient $\chi$ in equation (3).

$3d_{x^2-y^2}$ orbital of Cu1, the intrabond oxygen $2p_x$ longitudinal with the bond, and the $3d_{x^2-y^2}$ orbital of Cu2 (Fig. 1b), sensitizing it to the local oxygen vibrational degrees of freedom (Fig. 1a). Consider the effect, sketched in Fig. 1b, of, for example, the out-of-plane oxygen displacement $z$, which is to reduce the overlap between both $3d_{x^2-y^2}$ orbitals and the oxygen $2p_x$ orbital, thus reducing the effective coupling $t$. In most cuprate systems the $CuO_2$ plane is atomically flat (the buckling of the planar oxygens in YBCO is ignored here, leaving its treatment to a future publication). The $t$-reduction effect is then the same irrespective of the sign of the displacement $z$, so that its lowest-order expression is as $z^2$. Hence the electron-vibrator term in the hamiltonian must have the unusual second-order form of coupling

$$
h_{12}^{\mathrm{ev}}=\frac{v}{2} z^{2} \sum_{\sigma}\left(c_{1, \sigma}^{+} c_{2, \sigma}+c_{2, \sigma}^{+} c_{1, \sigma}\right),\tag{2}
$$

where $v$ is the coupling strength. This electron-vibrator coupling causes the Cu–Cu bond strength $t$ to fluctuate with the oxygen-vibrator square amplitude $z^2$ — hence the description fluctuating-bond model (FBM). The two other oxygen vibrational modes, $x$ and $y$, can also couple to the bond strength in a similar manner. In addition, there is a coupling linear in the stretch mode $x$, via charge displacement onto the Cu1 and Cu2 sites; however, because charge accumulation on the Cu sites is resisted, owing to the projection out of double hole occupation of the Cu site by the large on-site Coulomb interaction $U$ (ref. 11), we do not believe that on-site charge fluctuation can be important, and ignore it in our model at the present maximally simplified stage.

Experimentally, electron–phonon coupling involving the O-stretch mode ($x$ in Fig. 1a) is manifested in the anomalous doping-dependent softening of the half-breathing mode ($\sim$70 meV) in many materials$^{14–16}$, and, in YBCO, by the anomalous change in the inelastic X-ray cross-section of this mode below $T_\text{c}$ (ref. 21). Electron–phonon coupling of the out-of-plane O-bend mode ($z$ in Fig. 1a), and its relevance for pairing, is shown by the widely observed softening of vibrations ($\sim$40 meV) involving this mode below $T_\text{c}$ (refs 14,17–20; see below), and by the existence of a critical planar oxygen buckling/tilting angle beyond which $T_\text{c}$ is suppressed$^{35}$. Modelling of the kink in the ARPES-determined energy band dispersion within a linearly coupled phonon model$^{13}$ shows that the $B_{1\mathrm{g}}$ ($\sim$40 meV) phonon mode (that is, out-of-plane O-bend mode ($z$) vibrations) couples to the high-density-of-states (DOS) antinodal part of the Fermi surface (FS), but the half-breathing stretch mode is sidelined by coupling only to the low-DOS nodal part of the FS. Here, however, we argue that, in the environment of the flat $CuO_2$ plane, linear coupling is forbidden. We shall show that the FBM nonlinear coupling (2) allows both O-bend and O-stretch modes to couple to the antinodal part of the FS and fully participate in pairing, consistent with the foregoing evidence. There is an absence of significant evidence regarding the in-plane O-bend mode.

The oxygen vibrational degree of freedom needs to include an anharmonic potential term in a theory with nonlinear electron-vibrator coupling$^{22,24,30,36}$. Hence, for example for the $z$ mode, the anharmonic vibrator hamiltonian should have the form

$$
h_{12}^{\mathrm{v}}=\frac{p_{z}^{2}}{2 m}+\frac{\chi}{2} z^{2}+\frac{w}{8} z^{4},\tag{3}
$$

where, in addition to the conventional harmonic terms, in which $p_z$ is oxygen momentum, $m$ oxygen mass and $\chi$ the force constant, a fourth-order potential with positive coefficient $w$ (symmetry is used to eliminate a cubic term) has been added. The shape of the potential well (3) depends on the sign of $\chi$. If $\chi > 0$ the potential is distorted harmonic (full curve in Fig. 1c), whereas if $\chi < 0$ the potential has double-well shape (dashed curve in Fig. 1c).

Experimentally, there is support for oxygen lattice dynamic anharmonicity$^{14}$ being strong. For example, in the 214 insulator, soft-mode behaviour of the planar oxygen-tilt mode$^{37}$ has no other explanation. In the Eu-123 material, combined Mossbauer and extended X-ray absorption fine structure data show a correlated $c$-axis motion of the Eu and planar oxygen ions in a double-well potential$^{38}$. In an extensive Raman study of several high-temperature superconducting materials$^{39}$, two-phonon peaks could not be assigned as harmonics of single-phonon peaks — especially in the YBCO and Bi 2212 materials — suggesting anharmonicity as one explanation. In equation (3) we shall assume that the parameters $\chi$ and $w$ are doping — and system — independent, in line with the fact that vibration frequencies do not vary much$^{14,17–20}$.

The FBM pairing interaction in standard second-order perturbation theory, $V^{(2)}$, takes the bond-local form (see Fig. 2, left panel)

$$
V^{(2)}=-\frac{c}{2} K X_{12}^{2} ; \quad X_{12}=\sum_{\sigma}\left(c_{1, \sigma}^{+} c_{2, \sigma}+c_{2, \sigma}^{+} c_{1, \sigma}\right),\tag{4}
$$

where we introduce the compact notation $X_{12}$ for the bond order operator describing the strength of the Cu1–Cu2 bond,

ARTICLES

the coupling energy scale $K = v^2/w$ and for example for a purely quartic oscillator $(\chi=0)$ $c=0.14$. The Fourier transform of $X_{12}$ eventually leads to the $d$-wave factor $\cos q_x - \cos q_y$ in $k$-space, resulting in pairing and pseudogap phenomena of $d$-wave symmetry.

We are now ready to write down the complete FBM hamiltonian, as a sum of electronic, vibrator and coupling terms:

$$
H^{\mathrm{FBM}}=H^{\mathrm{e}}+H^{\mathrm{v}}+H^{\mathrm{ev}} . \tag{5}
$$

Here the electronic term includes hopping over longer ranges than the nearest-neighbour hopping considered in equation (1):

$$
H^{\mathrm{e}}=-\frac{1}{2} \sum_{\mathbf{i}, \mathbf{j}, \sigma} t(\mathbf{i}-\mathbf{j}) c_{\mathbf{i}, \sigma}^{+} c_{\mathbf{j}, \sigma}, \tag{6}
$$

where $\mathbf{i}$ denotes the $3d_{x^2-y^2}$ orbital on lattice site $\mathbf{i}=(i_x, i_y)$ in the two-dimensional square lattice of $\mathrm{Cu}$ ions. The strongest interaction is the nearest-neighbour hopping integral $t(\pm 1,0)=t(0, \pm 1)=t$, followed by the next-nearest-neighbour interaction $t(\pm 1, \pm 1)=t^{\prime}$, and then the third-nearest-neighbour interaction $t(\pm 2,0)=t(0, \pm 2)=t^{\prime \prime}$. The band eigenvalues $\epsilon_{\mathbf{k}}$ of (6) are $\epsilon_{\mathbf{k}}=-2 t\left(\cos k_x+\cos k_y\right)-4 t^{\prime} \cos k_x \cos k_y$ $-2 t^{\prime \prime}\left(\cos 2 k_x+\cos 2 k_y\right)$ in units where the lattice constant $=1$.

In the vibrational term we introduce the bare oxygen-vibrator frequency $\omega_0$ by $\omega_0^2=\chi / m$, where $m$ is oxygen mass, and then

$$
H^{\mathrm{v}}=\sum_{\mathbf{i}, \widehat{\boldsymbol{\alpha}}=\widehat{\mathbf{x}}}^{\mathbf{y}}\left[\frac{1}{2 m} p_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}^{2}+\frac{m \omega_{0}^{2}}{2} x_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}^{2}+\frac{w}{8 n}\left(x_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}^{2}\right)^{2}\right], \tag{7}
$$

and the planar oxygen positions/momenta are relabelled as $x_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2} / p_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}$, in terms of a $\mathrm{Cu}$ site $\mathbf{i}$ and a unit vector $\widehat{\boldsymbol{\alpha}}=\widehat{\mathbf{x}}$ or $\widehat{\mathbf{y}}$ away from $\mathbf{i}$ in the positive axis direction. The vibrational modes are approximated as local (Einstein) and isotropic. The notation $p^{2}$, $x^{2}$ implies $\sum_{s=1}^{n} p_{s}^{2}, \sum_{s=1}^{n} x_{s}^{2}$, where $s$ is polarization ( $s=$ transverse to plane, longitudinal to bond or in plane transverse to bond; see Fig. 1a). The mode degeneracy is $n$.

The bond-order operators are defined using the same notation for bonds

$$
X_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}=\sum_{\sigma}\left[c_{\mathbf{i}, \sigma}^{+} c_{\mathbf{i}+\widehat{\boldsymbol{\alpha}}, \sigma}+c_{\mathbf{i}+\widehat{\boldsymbol{\alpha}}, \sigma}^{+} c_{\mathbf{i}, \sigma}\right]. \tag{8}
$$

In terms of these, the coupling hamiltonian is

$$
H^{\mathrm{ev}}=\frac{v}{2 \sqrt{n n_{\mathrm{s}}}} \sum_{\mathbf{i}, \boldsymbol{\alpha}} x_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}^{2} X_{\mathbf{i}+\widehat{\boldsymbol{\alpha}} / 2}. \tag{9}
$$

The prefactor includes a spin degeneracy $n_{\mathrm{s}}$.

As long as the system is in the Fermi liquid state (not a Mott insulator), it derives perturbationally from a non-interacting electron gas, and we can use the standard weak-coupling approach, which takes the electron gas as the unperturbed system. To develop a perturbation expansion when the Migdal theorem is not obeyed in $\mathrm{HTS}^{3}$, we adopt the $1 / N$ expansion technique, where $N$ is degeneracy, for example orbital or spin degeneracy. The $1 / N$ expansion works well for example for the Kondo problem $^{40}$, the results remaining physical down to spin degeneracy $N=2$. Here we systematically coexpand in the inverse of the mode degeneracy $n$ and the spin degeneracy $n_{\mathrm{s}}$, using a path-integral approach $^{41}$ (see the Supplementary Information), meaning by expressions such as ' $1 / N$ ' the joint orders $1 / n$ and $1 / n_{\mathrm{s}}$.

The interaction which scatters a pair $(\mathbf{k},-\mathbf{k})$ to $(\mathbf{k}+\mathbf{q},-\mathbf{k}-\mathbf{q})$ (Fig. 2) differs from the usual single-phonon propagator structure in BCS, because there is no single electron-phonon interaction term in the FBM equations (5)-(9). The structure is instead a two-boson propagator with leading-$N$ self-energy insertions in the denominator, consisting of a positive term in the boson-boson interaction $w$ and a negative term $v^2$ multiplied by a fermion response function, which can lead to a divergence in the overall expression. It is also a $2 \times 2$ matrix because the two interacting electronic states can each be in either bond $x$ or bond $y$. The key to simplifying this rather complicated object is that, in the most important small-$q$ regime, the divergence comes from a combination of the $x$ and $y$ components with $d$ symmetry, the complementary $s$ channel being non-singular and uninteresting. Therefore, our simplifying procedure is to reduce the $2 \times 2$ propagator matrix to a scalar by projecting out $s$-symmetry charge fluctuations and retaining only the $d$-symmetry ones, the projection procedure being implemented in path integral formalism (see the Supplementary Information). The vibrator amplitude/$X$-operator fluctuations around each $\mathrm{Cu}$ site now form a $d_{x^2-y^2}$-like, or quadrupolar, pattern (see Fig. 3). This selection of the $d$-channel has the additional physical merit that charge flow into and out of each $\mathrm{Cu}$ site is balanced (Fig. 3), so that there is zero net site charge accumulation, compatible with the accepted large Coulomb repulsion $U$ on each site, which inhibits such charge fluctuations.

![](./images/812015951456239618_2.jpg)

Figure 2 The pairing interaction. a, Binding of two quasiparticles of opposite spin in a $\mathrm{Cu}-\mathrm{Cu}$ bond, as given by equation (4). b, The interaction between two pairing quasiparticles $\mathbf{k}$ and $-\mathbf{k}$, exchanging momentum $\mathbf{q}$ and frequency $\omega_{n}$, is a product of $d$-wave form factors $\xi_{\mathbf{k}, \mathbf{k}+\mathbf{q}}^{2}$ (yellow circles) and pairing propagator $V(\mathbf{q}, \omega_{n})$ (double dashed line). c, Zeroth approximation to $V$ on the basis of $v^2 \times$ two-boson propagator. Dashed lines represent the single-vibrator (boson) propagator, red circles electron-boson interaction $v$. d, The leading-$N$ self-energy corrections to $V$ (see analogous corrections in the heavy-fermion problem $^{42}$ ) come from boson-boson interaction $w$ and $v^2 \times$ response function $R_{d d}$. Full lines represent the fermion quasiparticle propagator. The green square represents boson-boson interaction $w$; the fermion lens is response function $R_{d d}$.

The FBM pairing propagator $\Gamma(\mathbf{k}, \mathbf{q}, n)$ (Fig. 2b) for scattering a pair from $(\mathbf{k},-\mathbf{k})$ to $(\mathbf{k}+\mathbf{q},-\mathbf{k}-\mathbf{q})$ is now given (for a full derivation see the Supplementary Information) by the Fig. 2 graphs as a product of $d$-wave form factors and a scalar two-phonon pairing propagator $V(\mathbf{q}, n)$

$$
\Gamma(\mathbf{k}, \mathbf{q}, n)=\left|\xi_{\mathbf{k}, \mathbf{k}+\mathbf{q}}\right|^{2} V(\mathbf{q}, n), \tag{10}
$$

where the $d$-wave form factor (the cosines originate in the form factor of the bond operator $X$) is

$$
\xi_{\mathbf{k}, \mathbf{k}^{\prime}}=\frac{1}{2}\left[\cos \left(k_{x}\right)+\cos \left(k_{x}^{\prime}\right)-\cos \left(k_{y}\right)-\cos \left(k_{y}^{\prime}\right)\right],
$$


![](./images/812015951456239618_3.jpg)

Figure 3 The fluctuating bond field. The z component of the fluctuating bond field (after projecting out s fluctuations), at long wavelength, has d symmetry (quadrupolar pattern), with (left panel) 0 amplitude (dumbbells) large in y bonds, small in x bonds (notation as Fig. 1), phase-reversed field in right panel. Panels also illustrate opposite phases of the static d-wave CDW (15). The CDW r.m.s. amplitude (15) is given by equation (17). Note that at finite wavelength the quadrupole pattern is locally distorted by curvature of the envelope of the field.

and the pairing propagator (dropping a zero-frequency term, significant only at temperatures above those of interest) is

$$
V(\mathbf{q}, n)=\frac{-4 n_{\mathrm{s}}^{-1} K \omega_{\mathrm{a}}^{2} \eta_{\mathbf{q}}}{\omega_{n}^{2}+4 \overline{\omega}^{2}+4 \omega_{\mathrm{a}}^{2} \eta_{\mathbf{q}}\left[\frac{1}{2}-K R_{d d}(\mathbf{q}, n)\right]}. \quad (11)
$$

Here $\omega_{n}=2 \pi n k_{\mathrm{B}} T$ is the Matsubara frequency (Fourier component with respect to imaginary time), $T$ is the temperature, $k_{\mathrm{B}}$ is Boltzmann's constant and we introduce definitions of the mean-field harmonic vibrator frequency $\omega_{\mathrm{h}}$, the anharmonic component of the vibrator frequency $\omega_{\mathrm{a}}$ and the total vibrator frequency $\overline{\omega}\left(\overline{\omega}^{2}=\omega_{\mathrm{h}}^{2}+\omega_{\mathrm{a}}^{2}\right)$

$$
\begin{aligned}
\omega_{\mathrm{h}}^{2} & =\omega_{0}^{2}+\frac{v}{m \sqrt{n n_{\mathrm{s}}}}\left\langle X_{i, \alpha}\right\rangle ; \\
\omega_{\mathrm{a}}^{2} & =\frac{w}{2 m n}\left\langle x_{i, \alpha}^{2}\right\rangle=\frac{w}{4 m^{2} \overline{\omega}} \operatorname{coth}\left(\frac{\overline{\omega}}{2 k_{\mathrm{B}} T}\right).
\end{aligned}\quad (12)
$$

In the denominator of (11) we can identify (in square brackets) the two terms in the self-energy (Fig. 2d), the positive one coming from $w$, and the negative one (leading to the divergence) coming from $v^{2} R_{d d}$. The other two terms are the inverse of the two-boson propagator (Fig. 2c) with characteristic frequency $2 \overline{\omega}$ (a frequency (12) up-shifted by the single-boson self-energy). The form factor $\eta_{\mathbf{q}}$ is defined by $\eta_{\mathbf{q}}=(1 / 2)\left[\cos ^{2}\left(q_{x} / 2\right)+\cos ^{2}\left(q_{y} / 2\right)\right]$, and the $d d$ response function $R_{d d}$ is defined in the normal state as

$$
R_{d d}(\mathbf{q}, n)=-\sum_{\mathbf{k}} \frac{f\left(\epsilon_{\mathbf{k}}\right)-f\left(\epsilon_{\mathbf{k}+\mathbf{q}}\right)}{i \omega_{n}+\epsilon_{\mathbf{k}}-\epsilon_{\mathbf{k}+\mathbf{q}}} \xi_{\mathbf{k}. \mathbf{k}+\mathbf{q}} \xi_{\mathbf{k}+\mathbf{q}. \mathbf{k}}, \quad (13)
$$

where $f\left(\epsilon_{\mathbf{k}}\right)$ is the Fermi function. The $d d$ response function is a generalization of the density-density response function. The presence of the $\xi$ factors, showing that the response function can be interpreted as the $d$-symmetry density response to a $d$-symmetry perturbation, gives $R_{d d}$ a value several times the DOS at small $q$ and $\omega_{n}$. At long wavelengths, the response function is decoupled from the on-site fluctuations of $s$ symmetry, hence it is decoupled from the strong on-site Coulomb repulsion $U$.

The modified two-phonon propagator $V(\mathbf{q}, n)$ can diverge at low frequency and small $q$, at significant values of the interaction $K$, owing to the largeness of $R_{d d}$ when the Fermi level lies at the energy $\epsilon_{\text {sp }}$ of the saddle points (or 'antinodal points') at $\mathbf{k}=(\pi, 0)$ and $(0, \pi)$ in the band structure, signalling the emergence of a two-phonon bound state. The same saddle-point effect causes a peak, the van Hove singularity, in the DOS at energy $\epsilon_{\text {sp }}$. In this situation the superconducting gap acts, through controlling the magnitude of $R_{d d}$, to regularize the divergence.

The factor $\xi_{\mathbf{k}, \mathbf{k}^{\prime}}^{2}$ in the pairing interaction (10) is large when $\mathbf{k}$ and $\mathbf{k}^{\prime}$ are in the neighbourhood of the same saddle point, and small when they are at different saddle points. In addition to the fact that $V(\mathbf{q}, n)$ can diverge at low frequency and small $q$, this gives the pairing interaction the form of large and attractive at small $q$, and weak at large $q$, the classic form of interaction for generating a $d$-wave order parameter.

Let us now look at the leading- $N$ gap equation $^{42}$ at $T_{\mathrm{c}}$

$$
\Delta(\mathbf{k}, n)=-T \sum_{\mathbf{k}^{\prime}, n^{\prime}} \xi_{\mathbf{k}, \mathbf{k}^{\prime}}^{2} V\left(\mathbf{k}-\mathbf{k}^{\prime}, n-n^{\prime}\right) G_{2}\left(\mathbf{k}^{\prime}, n^{\prime}\right) \Delta\left(\mathbf{k}^{\prime}, n^{\prime}\right), \quad(14)
$$

where $\Delta(\mathbf{k}, n)$ is the gap and (taking $\mu$ as energy zero) $G_{2}(\mathbf{k}, n)=\left(v_{n}^{2}+\epsilon_{\mathbf{k}}^{2}\right)^{-1}$.

In standard BCS theory, $G_{2}$ gives rise to a log divergence in $T$, which results in a solution to the gap equation with the well-known standard BCS formula for $T_{\mathrm{c}}$ exponential in the inverse coupling constant. In contrast, in the FBM there is the stronger divergence in $V(\mathbf{q}, n)$, which tends to peg $T_{\mathrm{c}}$ at the temperature where the divergence disappears. Since this temperature is defined by the denominator in $V(\mathbf{q}, n)$, in which no degeneracy factor $n_{\mathrm{s}}$ appears, it is a leading- $N$ formula. Hence we are justified in ignoring the second Eliashberg equation involving electronic mass renormalization ( $Z$ factor) as a $1 / N$ correction.

Solving the gap equation, we always find a $d_{x^{2}-y^{2}}$-wave gap $\Delta(\mathbf{k}, n)$, for the reasons just outlined. In Fig. 4 we present some results for $T_{\mathrm{c}}$ and oxygen isotope shift (the technique used was to solve at finite gap using fast Fourier transform techniques $^{43}$, and extrapolate to zero gap) as a function of doping. The results show the standard hump in $T_{\mathrm{c}}$ as a function of doping, and a very dramatic minimum in the isotope shift, going down to almost zero around the $T_{\mathrm{c}}$ maximum, and going up to values above the BCS $\alpha=0.5$ on the underdoped side. In Fig. 4 we also present experimental results for the 'universal' isotope shift behaviour found for several materials $^{12}$ along with the widely used 'universal' empirical formula for $T_{\mathrm{c}}$ (ref. 44). It is seen that there is a remarkable degree of agreement between theory and experiment, as regards the doping dependence of both the transition temperature and isotope shift.

The explanation for the hump in $T_{\mathrm{c}}$ as a function of doping in the FBM is that the DOS and the response function peak around the point where the Fermi energy coincides with the band-structure energy at the saddle point, $\epsilon_{\text {sp }}$. High DOS always favours pairing, and pairing is further promoted by the increased $R_{d d}$, which makes the denominator of $V(\mathbf{q}, n)$ more readily divergent.

As regards isotope shift, we recall that the BCS pairing propagator is mass independent at zero frequency, but it falls off at frequencies beyond the phonon frequency, imparting a mass-dependent cutoff to the pairing interaction, leading to the BCS isotope shift $\alpha=0.5$. In the present model, the phonon parameters are such that the phonon frequency is mainly of anharmonic origin, which is a mainly quartic potential (see Fig. 4 caption, Fig. 1c). Under these conditions, $\omega_{\mathrm{a}}$ factors out from the zero-frequency pairing propagator $V(\mathbf{q}, 0)$ (11), making it mass independent, as in the BCS case. In contrast with BCS, near optimal doping, the frequency dependence of the pairing propagator (11) primarily originates from the mass-independent function $R_{d d}(\mathbf{q}, n)$ (equation (13)) (not, as in BCS, the external term $\omega_{n}^{2}$ in the denominator) — hence the extremely low isotope shift. As the Fermi energy moves away from $\epsilon_{\text {sp }}$, the DOS drops, $R_{d d}$ decreases and the FBM divergence in the pairing interaction tends to disappear, with a resumption of more normal BCS isotope shift.

The universally seen softening of the out-of-plane O-bend mode ( $z$ in Fig. 1a) below $T_{\mathrm{c}}$ (refs 14,17,18) can be semiquantitatively reproduced in a simple mean-field description

![](./images/812015951456239618_4.jpg)

Figure 4 Transition-temperature and isotope-shift calculations compared with experimental data. Transition temperature $T_{\mathrm{c}}$ (red squares) and oxygen isotope shift $\alpha$ (green circles) versus doping $p$, relative to doping $p_{0}$ at maximum $T_{\mathrm{c}}$ ($T_{\mathrm{c}}^{\max}=193 \mathrm{~K}$), from gap equation (14). Parameters $t=0.25 \mathrm{eV}$, $t^{\prime}=-0.06 \mathrm{eV}, t^{\prime \prime}=0.0325 \mathrm{eV}, K=0.48 \mathrm{eV}$, energy cutoff $=1.6 \mathrm{eV}$, $\omega_{\mathrm{a}}=0.05 \mathrm{eV}, \omega_{\mathrm{h}}=0.015 \mathrm{eV}$ ($\omega_{\mathrm{a}}$ and $\omega_{\mathrm{h}}$ held constant throughout). Phonon frequencies in this range are reported for refs 14,17-20. Blue points, experimental oxygen isotope-shift measurements for YBCO-based and Bi-2212 cuprate superconductors $^{12}(p_{0}=0.162)$. Magenta curve, empirical $T_{\mathrm{c}}$-doping relation $T_{\mathrm{c}}=T_{\mathrm{c}}^{\max}(1-82.6(p-p_{0})^{2})$ (ref. 44).

![](./images/812015951456239618_5.jpg)

Figure 5 Superconductivity-induced Raman shift. Frequency shift versus temperature below $T_{\mathrm{c}}$ for mean-field equations (12) and (18) on the basis of the $d$-wave gap $\Delta(\mathbf{k})=\Delta_{0}(\cos k_{x}-\cos k_{y})/2$, with $\Delta_{0}(T)=3.5 T_{\mathrm{c}} \tanh(\sqrt{\gamma}\sqrt{1-T/T_{\mathrm{c}}})/\tanh(\sqrt{\gamma})$, $\gamma=3.5$ and $v>0$. Inset, data for the two highest- $T_{\mathrm{c}}$ samples in ref. 17; the line is a guide to the eye.

on the basis of equation (12), where calculation of the expectation value $\langle X_{\mathbf{i},\alpha}\rangle$ is done in the BCS approximation (see the Methods section). The mean-field result — quite different from earlier theories $^{31,32}$ — has the characteristic that the frequency shift is predicted in both $B_{1g}$ and $A_{1g}$ symmetries (see the Methods section), despite the fact that $A_{1g}$ by itself is weakly coupled to the antinodal part of the Fermi surface. This prediction is indeed as observed $^{17,18}$. Comparison of the predicted $T$ dependence (Fig. 5) with recent $B_{1g}$

Raman data on the YBCO material $^{17}$ is successful. The magnitude of the shift on the basis of the local vibrational-mode model equation (7) (0.4%) should however be compared with available symmetry- and zone-averaged YBCO data $^{14}$, giving an effect of about 0.7% between $T=0$ and $T_{\mathrm{c}}$, comparable with theory.

From the nearly quartic Einstein local vibrator potential model, an additional prediction for Raman scattering is that a satellite peak on the vibrator frequency $\omega=\overline{\omega}\simeq\omega_{\mathrm{a}}$ should occur at $\omega=1.34\overline{\omega}$, with an intensity that is very low at low temperature, but increasing as $\simeq\exp(-\overline{\omega}/k_{\mathrm{B}}T)$. However, the peak will be broadened by phonon dispersion.

As well as driving pairing, the coupling $K$ can also produce static distortions. The phonon–phonon interaction $w$ can be renormalized to $\widetilde{w}$ by summing a somewhat more extended set of leading-$N$ Feynman diagrams than those in Fig. 2. $\widetilde{w}$ is found to contain the proportionality factor

$$
\widetilde{w}\sim\frac{1}{2}-K R_{dd}(\mathbf{q},n),
$$

leading to a zero in the long-wavelength $\widetilde{w}$ at a temperature $T_{mf}$. Below $T_{mf}$ there is symmetry breaking in the system, which can be likened to the presence of an Ising pseudospin in each unit cell. The symmetry breaking can be described in real space as a local splitting of the nearest-neighbour hopping integrals $t$, $t_{x}\neq t_{y}$, and in $\mathbf{k}$ space as a splitting of the saddle-point energies at the $k$ points X and Y, $\epsilon_{\mathrm{sp}}^{\mathrm{X}}\neq\epsilon_{\mathrm{sp}}^{\mathrm{Y}}$.

An ordered pseudospin structure has been sought in the form of a one-dimensional $d$-wave charge-density wave (dCDW) (ref. 45), with the Ansatz

$$
u_{\mathbf{i}}^{2}=\frac{2\sqrt{nn_{\mathrm{s}}}}{v}\chi_{\mathrm{Q}}\cos(\mathbf{Q}.\mathbf{i}),\tag{15}
$$

where $\chi_{\mathrm{Q}}$ is the dCDW amplitude, $u_{\mathbf{i}}^{2}$ is a quadrupolar modulation of vibrational amplitude

$$
u_{\mathbf{i}}^{2}=\frac{1}{2}\left(x_{\mathbf{i}+\widehat{\mathbf{x}}/2}^{2}+x_{\mathbf{i}-\widehat{\mathbf{x}}/2}^{2}-y_{\mathbf{i}+\widehat{\mathbf{y}}/2}^{2}-y_{\mathbf{i}-\widehat{\mathbf{y}}/2}^{2}\right),\tag{16}
$$

and $\mathbf{Q}=(Q_{x},Q_{y})$ is the dCDW wavevector. The $d$-wave nature of the dCDW is seen in that the expression (16) corresponds to a static distortion of the type represented in Fig. 3.

By calculating the free energy (see the Methods section), the wavevector $\mathbf{Q}$ was determined by energy minimization. The direction of $\mathbf{Q}$ is found to lie along the $x$ or $y$ axis, $\mathbf{Q}=(Q,0)$ or $(0,Q)$. The dCDW is found to be stable — relative to the uniformly polarized (but presumably disordered) $Q=0$ state — below a temperature $T_{\mathrm{dCDW}}$, which is plotted in Fig. 6, a stability mostly confined to the underdoped side. $Q$ in this region closely tracks the nesting wavevector between the two pieces of FS at X or Y in the band structure (inset Fig. 6).

In Fig. 6 we also plot the temperature $T_{\mathrm{dCF}}$ below which $R_{dd}(q_{x},0,0)$ has a maximum in $q_{x}$ at $q_{x}\neq0$, signalling the existence of dCDW fluctuations.

The dCDW-induced modification to the energy band structure can be seen by looking at the poles in the propagator (see the Methods section), lying approximately at

$$
i\nu_{n}=\epsilon_{\mathrm{F}}\pm\frac{1}{2}\chi_{\mathrm{Q}}\xi_{\mathbf{k},\mathbf{k}+\mathbf{Q}}\to\epsilon_{\mathrm{F}}\pm\chi_{\mathrm{Q}},
$$

where $\xi_{\mathbf{k},\mathbf{k}+\mathbf{Q}}\simeq\pm2$. We see that $\chi_{\mathrm{Q}}$ is the gap opened up by the breakdown in long-range order caused by the dCDW — it is a form of pseudogap. The factor $\xi_{\mathbf{k},\mathbf{k}+\mathbf{Q}}$, which is approximately

![](./images/812015951456239618_6.jpg)

Figure 6 HTS phase diagram in temperature-versus-doping plane. Blue area, region of $d$-wave (quadrupolar) CDW fluctuations. Magenta and red hatched areas, $T < T_{\text{CDW}}$, showing the presence of one-dimensional $d$-wave CDW. Red hatched area, coexistence of $d$-wave CDW and $d$-wave SC. Green curve, isotope shift $\alpha$ (convolution with one-dimensional CDW has smoothed out the $p$ dependence of $\alpha$—this effect would be reduced in a two-dimensional CDW). CDW wavevector $\mathbf{Q}$ tracks the nesting wavevector $\mathbf{q}$ (illustrated in inset at point $X=(\pi, 0)$ in the BZ). At maximum $T_{\text{c}}$ the CDW wavelength is $2\pi/Q=109$\AA. Parameters as in Fig. 5, except $K=0.23$ eV in $T_{\text{CDW}}$ calculation (see Methods B).

$\cos k_{x}-\cos k_{y}$ at the small $Q$ of interest, shows the presence of a $d$-wave symmetry factor in this gap.

The quadrupolar phonon mean square amplitudes $u_{\text{i}}^{2}$ induced by the dCDW (16) can be conveniently compared with the zero-point amplitude of the harmonic oscillator of frequency $\overline{\omega}$, $\langle x_{\text{i},\alpha}^{2}\rangle$ (see equation (12), $\sqrt{\langle x_{\text{i},\alpha}^{2}\rangle}\simeq0.05$\AA). The ratio is given by

$$
\sqrt{\left\langle\left(u_{\mathrm{i}}^{2}\right)\right\rangle /\left\langle x_{\mathrm{i}, \alpha}^{2}\right\rangle} \simeq \sqrt{2 n_{s} \chi_{\mathrm{Q}}^{2} / n K \omega_{\mathrm{a}}}=0.65 \quad \text { for } n=3, \tag{17}
$$

where we assume for simplicity again that $\omega_{\text{h}}$ is small. The dCDW modulates the zero-point amplitude substantially.

We tentatively identify the dCDW gap as the $d$-wave pseudogap seen in the HTS materials. Which of the theoretical energy scales, $\chi_{\text{Q}}$, $T_{\text{dCDW}}$ or $T_{\text{dCF}}$ (Fig. 6), is identifiable with the observed pseudogap energy/temperature scale, typically termed $T^{*}$ (ref. 2), will depend on the experimental probe. STM studies show a highly inhomogeneous spatial variation of the gap$^{33}$, apparently controlled by the oxygen dopant distribution, which we interpret as a strongly impurity-pinned dCDW. The regions where the gap is maximal (75 meV — our $\chi_{\text{Q}}\simeq60$ meV), but with little sign of superconducting coherence peaks, are interpreted as the peaks in the dCDW amplitude. The length scale $\simeq40$\AA observed is similar to that predicted from the dCDW half-wavelength $\pi/Q$.

We need to estimate the interaction between the two order parameters, superconducting and dCDW. This is done in a Landau–Ginzburg formalism (for details, see the Methods section). Superconductivity and dCDW are found to be antagonistic, and the superconducting gap is found to be confined in space near the nodes of the dCDW. This seems consistent with the STM results$^{33}$, where the regions with a pronounced superconducting coherence peak also have a smaller gap, identifiable with the superconducting gap. Calculations show that the mean-field $T_{\text{c}}$ is also markedly reduced by this confinement of the superconducting regions to the dCDW nodes, whereas the isotope shift shows less variation with doping (see Fig. 6) — because $\chi_{\text{Q}}$ provides an additional perturbation competing with the effect of chemical potential (the dominant control parameter in Fig. 4). In fact, the STM results$^{33}$ would be more compatible with a two-dimensional CDW than the one-dimensional CDW found to be the ground state in this paper, and indeed tentative results for a two-dimensional CDW show much less $T_{\text{c}}$ reduction, and enhanced isotope shift variation, which would be in better agreement with experiment, for example the isotope shift. The observed stability of the two-dimensional-like dCDW is attributable to the pinning mechanism or other factors.

The observation of greatly reduced superfluid density $n_{\text{s}}$, scaling with the product of $T_{\text{c}}$ and normal state conductivity $\sigma$ (ref. 46), can be interpreted in terms of Pippard's expression for $n_{\text{s}}$ in strongly scattering superconductors$^{46,47}$. The short quasiparticle lifetime involved can be derived within the FBM, which also captures the strong anisotropy of the lifetime over the Fermi surface seen experimentally$^{4}$. Calculation of $n_{\text{s}}$ for a granular superconductor$^{48}$ — appropriate in the presence of the nanometre-scale inhomogeneity arising from the dCDW — also shows $n_{\text{s}}\propto\sigma$.

Finally, we should identify some key experimental tests. For the dCDW, it would be valuable to look for the spatially inhomogeneous quadrupolar ($d$-wave) amplitude modulation (Fig. 3, equations (15)–(17)) of the planar oxygens in different polarizations Fig. 1a, mapping onto an incipient striped phase. The modulation should disappear on the temperature scale of $T^{*}$.

The anharmonicity of the isolated oxygen vibrations should be seen in the appearance of a vibrational satellite at $\omega=1.34\overline{\omega}$ (subject to broadening by phonon dispersion), with an intensity that is very low at low temperature, but rapidly increasing as $\simeq\exp(-\overline{\omega}/k_{\text{B}}T)$ with increasing temperature.

# METHODS
## MODE DISPERSION AND MEAN-FIELD RAMAN SHIFT
For spectroscopic purposes, the dispersion of the oxygen modes needs to be included, when the harmonic part $V_{\text{h}}^{\text{v}}$ of the vibrator potential in (7) can be written

$$
V_{\mathrm{h}}^{\mathrm{v}}=\frac{m}{2} \sum_{\mathbf{k}}\left[\omega_{+}^{2}(\mathbf{k}) v_{\mathbf{k}}^{+} v_{-\mathbf{k}}^{+}+\omega_{-}^{2}(\mathbf{k}) v_{\mathbf{k}}^{-} v_{-\mathbf{k}}^{-}\right],
$$

where $\omega_{+}(\mathbf{k})$ ($\omega_{-}(\mathbf{k})$) are normal modes (with $A_{1\text{g}}$ ($B_{1\text{g}}$) polarization for the $z$ mode), and the corresponding modes are $v_{\mathbf{k}}^{\pm}=\left(x_{\mathbf{k}}\pm y_{\mathbf{k}}\right)/\sqrt{2}$, $x_{\mathbf{k}}$ ($y_{\mathbf{k}}$) being the Fourier transforms of $x_{\text{i}+\widehat{x}/2}$ ($y_{\text{i}+\widehat{y}/2}$). The coupling hamiltonian (9) in mean field, where $X_{\text{i}+\widehat{\alpha}/2}\to\langle X_{\text{i}+\widehat{\alpha}/2}\rangle$ is independent of $\text{i},\alpha$, becomes

$$
H^{\mathrm{ev}}=\frac{v}{2} \sum_{\mathbf{k}}\left[v_{\mathbf{k}}^{+} v_{-\mathbf{k}}^{+}+v_{\mathbf{k}}^{-} v_{-\mathbf{k}}^{-}\right]\left\langle X_{\mathrm{i}+\widehat{\alpha} / 2}\right\rangle.\tag{18}
$$

The shift in squared frequency, $\Delta\omega_{\pm}^{2}=v\langle X_{\text{i}+\widehat{\alpha}/2}\rangle/m$, is the same for both symmetries. Evaluating $\langle X_{\text{i}+\widehat{\alpha}/2}\rangle$ (using symmetry) as

$$
\left\langle X_{\mathrm{i}+\widehat{\alpha} / 2}\right\rangle=\sum_{\mathbf{k}, \sigma}\left\langle n_{\mathbf{k}, \sigma}\right\rangle\left(\cos k_{x}+\cos k_{y}\right),
$$

where $n_{\mathbf{k},\sigma}$ is the number operator for state $\mathbf{k}$ and spin $\sigma$, can be done below $T_{\text{c}}$ in BCS theory using

$$
\left\langle n_{\mathbf{k}, \sigma}\right\rangle=u_{\mathbf{k}}^{2} f\left(E_{\mathbf{k}}\right)+v_{\mathbf{k}}^{2} f\left(-E_{\mathbf{k}}\right),
$$

where $f(E)$ is the Fermi function and the BCS coherence factors are $v_{\mathbf{k}}^{2}=1-u_{\mathbf{k}}^{2}=\frac{1}{2}(1-\epsilon_{\mathbf{k}}/E_{\mathbf{k}})$ (taking $\mu$ as energy zero), and $E_{\mathbf{k}}=\sqrt{\epsilon_{\mathbf{k}}^{2}+\Delta_{\mathbf{k}}^{2}}$, where $\Delta_{\mathbf{k}}=\frac{1}{2}\Delta_{0}(\cos k_{x}-\cos k_{y})$ is the energy gap. With the Fig. 5 model for the $T$ dependence of the gap, $\langle X_{\text{i}+\widehat{\alpha}/2}\rangle$ and hence the frequency shift can be evaluated.

In addition to mean field, there are $1/N$ corrections to the vibration frequencies. To calculate these it will be necessary to generalize the coupling

ARTICLES

Lagrangian $\mathcal{L}_{z v}=-\sum_{i} z_{v, i} u_{i}^{2}$ (see the Supplementary Information) to include dispersion. In Fourier space the term becomes
$$
\mathcal{L}_{z v}=-\sum_{\mathbf{q}, \mathbf{k} n, m} z_{-\mathbf{q},-n}\left[v_{-\mathbf{k},-\mathbf{m}}^{+} v_{-\mathbf{k},-\mathbf{m}}^{-}\right]\left[\begin{array}{l}
f_{\mathbf{q}}^{-} f_{\mathbf{q}}^{+} \\
f_{\mathbf{q}}^{+} f_{\mathbf{q}}^{-}
\end{array}\right]\left[\begin{array}{l}
v_{\mathbf{k}+\mathbf{q}, \mathbf{m}+\mathbf{n}}^{+} \\
v_{\mathbf{k}+\mathbf{q}, \mathbf{m}+\mathbf{n}}^{-}
\end{array}\right],
$$
where $f_{\mathbf{q}}^{ \pm}=(1 / 2)(\cos \left(q_{x} / 2\right) \pm \cos \left(q_{y} / 2\right))$. It is seen that at small $q$, only the off-diagonal couplings $v_{-\mathbf{k},-\mathbf{m}}^{ \pm} v_{\mathbf{k}+\mathbf{q}, \mathbf{m}+\mathbf{n}}^{\mp}$ remain. The vibrational field $z_{\mathbf{q}, n}$ at wavevector $\mathbf{q}$ then couples to two phonons, at wavevector $\mathbf{k}+\mathbf{q}$ and $-\mathbf{k}$, which for small $\mathbf{q}$ have predominantly different symmetries, $\mathrm{A}_{1 \mathrm{~g}}$ and $\mathrm{B}_{1 \mathrm{~g}}$.

### d-WAVE CDW
In the presence of the $d$-wave (quadrupolar) CDW (Fig. 3)
$$
u_{\mathbf{i}}^{2}=\frac{2 \sqrt{\pi n_{s}}}{v} \chi_{\mathrm{Q}} \cos (\mathbf{Q}. \mathbf{i}),
$$
the propagator $G(\mathbf{k}, n)$, in a standard approximation where the self-energy is second order in $\chi_{\mathrm{Q}}$, is given by
$$
G(\mathbf{k}, n)=\frac{1}{i v_{n}-\epsilon_{\mathbf{k}}-\chi_{\mathrm{Q}}^{2} \Phi(\mathbf{k}, n)},
$$
with
$$
\Phi(\mathbf{k}, n)=\frac{1}{4}\left[\frac{\xi_{\mathbf{k}, \mathbf{k}+\mathbf{Q}}^{2}}{i v_{n}-\epsilon_{\mathbf{k}+\mathbf{Q}}}+\frac{\xi_{\mathbf{k}, \mathbf{k}-\mathbf{Q}}^{2}}{i v_{n}-\epsilon_{\mathbf{k}-\mathbf{Q}}}\right].
$$

The free energy $\Omega$ of the dCDW state can be calculated by the method of coupling-constant integration, for example. We find for the difference $\Delta \Omega$ between the free energy of the dCDW and that of the normal state
$$
\Delta \Omega=\frac{n_{s} \chi_{\mathrm{Q}}^{2}}{8 K}-\frac{T}{4} \sum_{\mathbf{k}, n, \sigma} \log \left\{\frac{\left(\epsilon_{\mathbf{k}}+\chi_{\mathrm{Q}}^{2} \Phi_{1}(\mathbf{k}, n)\right)^{2}+\left(v_{n}-\chi_{\mathrm{Q}}^{2} \Phi_{2}(\mathbf{k}, n)\right)^{2}}{\epsilon_{\mathbf{k}}^{2}+v_{n}^{2}}\right\},
$$
where $\Phi=\Phi_{1}+i \Phi_{2}$. The free energy for the $Q=0$ case is the same as for the $Q \rightarrow 0$ dCDW case. By calculating the free energy, the wavevector $\mathbf{Q}$ and $\chi_{\mathrm{Q}}$ were determined by energy minimization.

A lower $K$ value is used in the dCDW results illustrated in Fig. 6 relative to that in Fig. 5 for the superconducting properties, a discrepancy interpreted as a pseudopotential effect. A large hidden negative contribution to the empirical $K$ can be assumed from the nearest-neighbour Coulomb repulsion $V$. In a superconducting context, Coulomb interactions are reduced to a lower value $V^{*}$ by off-shell scattering (pseudopotential effect), whereas there is no such effect for the static dCDW. Hence the dCDW effective $K$ should be less attractive, with the two $K$-values differing by roughly $V-V^{*}$.

The dCDW-induced modification to the energy band structure can be seen by looking at the poles in the propagator $G(\mathbf{k}, n)$ lying at low energy. Suppose that $\epsilon_{\mathbf{k}}$ and $\epsilon_{\mathbf{k}+\mathbf{Q}}$ lie near the Fermi level ( $\mathbf{k}$ and $\mathbf{k}+\mathbf{Q}$ are two points related by nesting - see Fig. 6 inset), when $\epsilon_{\mathbf{k}-\mathbf{Q}}$ will typically lie far away so only the term in $\epsilon_{\mathbf{k}+\mathbf{Q}}$ in $\Phi$ diverges. Then the poles are approximately at
$$
i v_{n}=\epsilon_{\mathrm{F}} \pm \frac{1}{2} \chi_{\mathrm{Q}} \xi_{\mathbf{k}, \mathbf{k}+\mathbf{Q}} \rightarrow \epsilon_{\mathrm{F}} \pm \chi_{\mathrm{Q}},
$$
where $\xi_{\mathbf{k}, \mathbf{k}+\mathbf{Q}} \simeq \pm 2$. An identical argument can be made for the case of scattering from $\mathbf{k}$ to $\mathbf{k}-\mathbf{Q}$. Hence we see that $\chi_{\mathrm{Q}}$ is the gap opened up by the breakdown in long-range order caused by the dCDW — it is a form of pseudogap. The factor $\xi_{\mathbf{k}, \mathbf{k}+\mathbf{Q}}$, which is approximately $\cos k_{x}-\cos k_{y}$ at the small $Q$ of interest, shows the presence of a $d$-wave symmetry factor in this gap. Because of nesting factors, the gap is not symmetric in $X$ versus $Y$, but full symmetry in $k$-space will reappear on averaging over spatial domains $\mathbf{Q}=(Q, 0)$ or $(0, Q)$.

We need to estimate the interaction between the two order parameters, superconducting and dCDW. We calculate the dCDW order parameter on the basis of the normal state, assuming that we always have $T_{\mathrm{dCDW}}>T_{\mathrm{c}}\left(T^{*}>T_{\mathrm{c}}\right)$, for which there is supporting evidence $^{49}$. The superconducting phase - owing to its small coherence length $\xi \sim 1.5 \mathrm{~nm}$ — can coexist with the competing dCDW phase $^{50}$. We shall here describe the inhomogeneous two-order-parameter coexistence phase in an approximate manner using a form of Landau-Ginzburg (LG) approach. The approach does not take into account local distortion of the superconducting order parameter by the dCDW (local distortions average out, leaving a perfect $d$ wave, over a dCDW wavelength).

The LG expression for the superconducting free energy takes the form
$$
F=\frac{a}{2}(\nabla \Delta)^{2}+\frac{b}{2}\left(T-T_{\mathrm{c}}^{0}\right) \Delta^{2}+\frac{1}{2} \Delta^{2} f\left(\chi^{2}(\mathbf{x})\right),
$$
where $\chi(\mathbf{x})$ is the dCDW order parameter
$$
\chi(\mathbf{x})=\chi_{\mathrm{Q}} \cos (\mathbf{Q}. \mathbf{x}) ; \quad Q \neq 0, \quad \chi=\chi_{0} / \sqrt{2} ; \quad Q=0,
$$
$\Delta(\mathbf{x})$ is the superconducting gap, $a$ and $b$ are LG parameters, $T_{\mathrm{c}}^{0}$ is the transition temperature in the absence of the dCDW order parameter and $f$ is a coupling function between the two order parameters.

In the absence of dCDW order the coherence length is given by the standard formula $\xi_{\mathrm{LG}}^{0}=\sqrt{a / b T_{\mathrm{c}}^{0}}=0.739 \xi_{\mathrm{BCS}}^{0}$; the BCS coherence length $\xi_{\mathrm{BCS}}^{0}$ is assumed to follow BCS scaling relative to the known coherence length of the HTS. The function $f$ is determined from solving the gap equation as a function of a spatially uniform dCDW amplitude $\chi_{0}$, the input being the splitting $t_{x}-t_{y}=\chi_{0}$ in the nearest-neighbour hopping integral. To limit order parameter distortion, a cutoff on the maximum $\chi$ is inserted, which however does not affect the conclusions.

Differentiating the free energy w.r.t. $\Delta$ we obtain the Schrödinger-like equation for the gap
$$
-a \nabla^{2} \Delta+V(\mathbf{x}) \Delta=\epsilon \Delta,
$$
where $V(\mathbf{x})=f\left(\chi^{2}(\mathbf{x})\right)-b T_{\mathrm{c}}^{0}, \epsilon=-b T$. The lowest-energy $\epsilon$ solution represents the highest global transition temperature $T_{\mathrm{c}}=T$. The procedure is then to (1) solve for the dCDW amplitude and wavevector, (2) calculate the effect on $T_{\mathrm{c}}$ of a given magnitude of uniform order parameter and then (3) solve the Schrödinger-like equation for the transition temperature.

Received 24 May 2006; accepted 10 January 2007; published 18 February 2007.

### References
1. Leggett, A. J. What do we know about high $T_{c}$? Nature Phys. 2, 134-136 (2006).
2. Bonn, D. A. Are high-temperature superconductors exotic? Nature Phys. 2, 159-168 (2006).
3. Tsuei, C. C. \& Kirtley, J. R. Pairing symmetry in cuprate superconductors. Rev. Mod. Phys. 72, 969 (2000).
4. Norman, M. R. et al. Destruction of the Fermi surface in high- $T_{\mathrm{c}}$ superconductors. Nature 392, 157-160 (1998).
5. Moler, K. A. et al. Magnetic field dependence of the density of states of $\mathrm{YBa}_{2} \mathrm{Cu}_{3} \mathrm{O}_{6.95}$ as determined from the specific heat. Phys. Rev. Lett. 73, 2744-2747 (1994).
6. Lee, P. A. Localized states in a d-wave superconductor. Phys. Rev. Lett. 71, 1887-1890 (1993).
7. Chiao, M. et al. Low-energy quasiparticles in cuprate superconductors: A quantitative analysis. Phys. Rev. B 62, 3554-3558 (2000).
8. Proust, C. et al. Heat transport in a strongly overdoped cuprate: Fermi liquid and a pure d-wave BCS superconductor. Phys. Rev. Lett. 89, 147003 (2002).
9. Achkir, D, Poirier, M., Bonn, D. A., Liang, R. \& Hardy, W. N. Temperature dependence of the in-plane penetration depth of $\mathrm{YBa}_{2} \mathrm{Cu}_{3} \mathrm{O}_{6.95}$ and $\mathrm{YBa}_{2}\left(\mathrm{Cu}_{0.9985} \mathrm{Zn}_{0.0015}\right)_{3} \mathrm{O}_{6.95}$ crystals from $\mathrm{T}$ to $\mathrm{T}^{*}$. Phys. Rev. B 48, 13184-13187 (1993).
10. Zhou, X. J. et al. Dichotomy between normal and anomalous quasiparticles in underdoped $\mathrm{La}_{2-x} \mathrm{Sr}_{x} \mathrm{CuO}_{4}$. Phys. Rev. Lett. 92, 187001-187005 (2004).
11. Anderson, P. W. et al. The physics behind high-temperature superconducting cuprates: the 'plain vanilla' version of RVB. J. Phys. Condens. Matter 16, R755-R769 (2004).
12. Pringle, D. J., Williams, G. V. M. \& Tallon, J. L. Effect of doping and impurities on the oxygen isotope effect in high-temperature superconducting cuprates. Phys. Rev. B 62, 12527-12533 (2000).
13. Devereaux, T. P., Cuk, T., Shen, Z.-X. \& Nagaosa, N. Anisotropic electron-phonon interaction in the cuprates. Phys. Rev. Lett. 93, 117004 (2004).
14. Pintschovius, L. Electron-phonon coupling effects explored by inelastic neutron scattering. Phys. Status Solidi B 242, 30-50 (2005).
15. McQueeney, R. J. et al. Anomalous dispersion of LO phonons in $\mathrm{La}_{1.85} \mathrm{Sr}_{0.15} \mathrm{CuO}_{4}$ at low temperatures. Phys. Rev. Lett. 82, 628 (1999).
16. Uchiyama, H. et al. Softening of $\mathrm{Cu}-\mathrm{O}$ bond stretching phonons in tetragonal $\mathrm{HgBa}_{2} \mathrm{CuO}_{4+\delta}$. Phys. Rev. Lett. 92, 197005 (2004).
17. Hewitt, K. C. et al. Hole concentration and phonon renormalization of the $340 \mathrm{~cm}^{-1} \mathrm{~B}_{1 \mathrm{~g}}$ mode in $2 \%$ Ca-doped $\mathrm{YBa}_{2} \mathrm{CuO}_{7}(6.76 \leqslant y \leqslant 7.00)$. Phys. Rev. B 69, 065414 (2004).
18. Zhou, Z., Cardona, M., Colson, D. \& Viallet, V. Plane oxygen vibrations and their temperature dependence in $\mathrm{HgBa}_{2} \mathrm{Ca}_{2} \mathrm{Cu}_{3} \mathrm{O}_{8+\delta}$. Phys. Rev. B 55, 12770-12775 (1997).
19. Harashina, H. et al. Superconductivity-induced $B_{1 \mathrm{~g}}$ phonon anomalies of $\mathrm{YBa}_{2} \mathrm{Cu}_{3} \mathrm{O}_{6+x}$ and symmetry of the order parameter. Neutron inelastic scattering studies. Physica C 263, 257-259 (1996).
20. Reznik, D., Keimer, B., Dogan, F. \& Aksay, I. A. $q$ dependence of self-energy effects of the plane oxygen vibrations in $\mathrm{YBa}_{2} \mathrm{Cu}_{3} \mathrm{O}_{y}$. Phys. Rev. Lett. 75, 2396-2399 (1995).
21. Chung, J. H. et al. In-plane anisotropy and temperature dependence of oxygen phonon modes in $\mathrm{YBa}_{2} \mathrm{Cu}_{3} \mathrm{O}_{6.95}$. Phys. Rev. B 67, 014517 (2003).
22. Bussmann-Holder, A. \& Keller, H. Polaron formation as origin of unconventional isotope effects in cuprate superconductors. Eur. Phys. J. B 44, 487-490 (2005).
23. Müller, K. A. in Treatise on High Temperature Superconductivity (ed. Schrieffer, J. R.) (in the press).

ARTICLES

24. Crespi, V. H. & Cohen, M. L. Anharmonic phonons and high-temperature superconductivity. Phys. Rev. 48, 398–406 (1993).
25. Kulić, M. L. Interplay of electron–phonon interaction and strong correlations: the possible way to high-temperature superconductivity. Phys. Rep. 338, 1–264 (2000).
26. Cappelluti, E. & Pietronero, L. Nonadiabatic superconductivity: The role of van Hove singularities. Phys. Rev. B 53, 932–944 (1996).
27. Sakai, T., Poilblanc, D. & Scalapino, D. J. Hole pairing and phonon dynamics in generalized two-dimensional $t-J$ Holstein Models. Phys. Rev. B 55, 8445–8451 (1997).
28. Fu, H. C., Honerkamp, C. & Lee, D.-H. Renormalization group study of the electron–phonon interaction in high $T_c$ cuprates. Preprint at <http://www.arxiv.org/cond-mat/0509072 v2 > (2005).
29. Schuttler, H.-B. & Pao, C.-H. Isotope effect in d-wave superconductors. Phys. Rev. Lett. 75, 4504–4507 (1995).
30. Song, J. & Annett, J. F. Electron–phonon coupling and d-wave superconductivity in the cuprates. Phys. Rev. B 51, 3840–3849 (1995).
31. Zeyher, Z. & Zwicknagl, G. Superconductivity-induced phonon self-energy effects in high-$T_c$ superconductors. Z. Phys. B 78, 175–190 (1990).
32. Nicol, E. J., Jiang, C. & Carbotte, J. P. Effect of $d$-wave energy-gap symmetry on Raman shifts. Phys. Rev. B 47, 8131–8139 (1993).
33. McElroy, K. et al. Atomic-scale sources and mechanism of nanometer scale electronic disorder in $Bi_2Sr_2CaCu_2O_{8+\delta}$. Science 309, 1048–1052 (2005).
34. Khasanov, R. et al. Site-selective oxygen isotope effect on the magnetic penetration depth in underdoped $Y_{0.6}Pr_{0.4}Ba_2Cu_3O_{7-\delta}$. Phys. Rev. B 68, 220506 (2003).
35. Büchner, B., Breuer, M., Freimuth, A. & Kampf, A. P. Critical buckling for the disappearance of superconductivity in rare-earth-doped $La_{2-x}Sr_xCuO_4$. Phys. Rev. Lett. 73, 1841–1844 (1994).
36. Mahan, G. D. Reentrant superconductivity from the anharmonic electron–phonon interaction. Phys. Rev. B 56, 8322–8329 (1997).
37. Weber, W. H., Peters, C. R. & Logothetis, E. M. Raman studies of lanthanum cuprate superconductors. L. Opt. Soc. Am. B 6, 455–464 (1989).
38. Piazza, F. et al. Study of atomic motions in $EuBa_2Cu_3O_{7-\delta}$ using Mössbauer and EXAFS spectroscopies. J. Supercond. 14, 675–681 (2001).

39. Sugai, S. et al. Carrier-density-dependent momentum shift of the coherent peak and the LO phonon mode in $p$-type high- $T_c$ superconductors. Phys. Rev. B 68, 184504 (2003).
40. Read, N. & Newns, D. M. On the solution to the Coqblin–Schrieffer hamiltonian by the large-N expansion technique. J. Phys. C 16, 3273–3295 (1983).
41. Coleman, S. Aspects of Symmetry (Cambridge Univ. Press, New York, 1985).
42. Lavagna, M., Millis, A. J. & Lee, P. A. d-wave superconductivity in the large-degeneracy limit of the Anderson lattice. Phys. Rev. Lett. 58, 266–269 (1987).
43. Serene, J. W. & Hess, D. W. Quasiparticle properties of the two-dimensional Hubbard model in a propagator-renormalized fluctuation-exchange approximation. Phys. Rev. B 44, 3391–3394 (1991).
44. Presland, M. R., Tallon, J. L., Buckley, R. G., Liu, R. S. & Flower, N. E. General trends in oxygen stoichiometry effects on Tc in Bi and Tl superconductors. Physica C 176, 95–105 (1991).
45. Grüner, G. The dynamics of charge density waves. Rev. Mod. Phys. 60, 1129–1138 (1988).
46. Homes, C. C. et al. Scaling of the superfluid density in high-temperature superconductors. Nature 430, 539 (2004).
47. Tallon, J. L. et al. Scaling relation for the superfluid density of cuprate superconductors: Origins and limits. Phys. Rev. B 73, 180504(R) (2006).
48. Ebner, C. & Stroud, D. Superfluid density, penetration depth, and integrated fluctuation conductivity of a model granular superconductor. Phys. Rev. B 28, 5053 (1983).
49. Shibauchi, T., Krusin-Elbaum, L., Li, M., Maley, M. P. & Kes, P. H. Closing the pseudogap by Zeeman splitting in $Bi_2Sr_2CaCu_2O_{8+\delta}$ at high magnetic fields. Phys. Rev. Lett. 86, 5763–5767 (2001).
50. Machida, K., Koyama, T. & Matsubara, T. Theory of charge-density-wave superconductors. Phys. Rev. B 23, 99–105 (1981).

Correspondence and requests for materials should be addressed to D.M.N.
Supplementary Information accompanies this paper on www.nature.com/naturephysics.

## Competing financial interests
The authors declare that they have no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

---

nature physics | VOL 3 | MARCH 2007 | www.nature.com/naturephysics
©2007 Nature Publishing Group
191