Microscopic calculation of the lattice dynamics of germanium using pseudo-atoms

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1987 J. Phys. C: Solid State Phys. 20 3795

(http://iopscience.iop.org/0022-3719/20/25/009)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 128.6.218.72
This content was downloaded on 21/08/2015 at 22:49

Please note that terms and conditions apply.

**Microscopic calculation of the lattice dynamics of germanium using pseudo-atoms**

M A Ball
Department of Applied Mathematics and Theoretical Physics, The University of Liverpool, PO Box 147, Liverpool L69 3BX, UK

Received 12 August 1986, in final form 18 December 1986

Abstract. The phonon frequencies of germanium are calculated using a quantum-mechanical dynamical matrix and the pseudo-atom expression for the change in charge density. A model pseudo-atom is constructed from Phillips' bond charge model with the dimensions of the bond charge taken from the static crystal: each pseudo-atom moves rigidly with its ion and is taken to consist of a central part and half of each adjacent bond charge. Without exchange-correlation (xc) effects, the calculated phonon spectrum is unsatisfactory with several acoustic modes being unstable. Several modifications of the model are tried but do not rectify this. An expression for the energy contribution caused by the xc effects is derived using perturbation theory. It is shown that it introduces a strong force attracting the two halves of the bond charge together. This force stabilises the acoustic modes and gives results in reasonable agreement with experiment and which are comparable with some of the results of more complicated methods. The flat behaviour of the TA modes is not reproduced. The amount of computation required is small and the method is compared with the usual methods of calculation. The implications of the treatment of the xc effects is discussed and so are some possible improvements to the model pseudo-atom.

### 1. Introduction
At the present time there are two main methods of calculating the lattice dynamics of semiconductors like germanium from a microscopic point of view. These are: (i) *the total energy method* (Wendel and Martin 1979, Kunc and Martin 1982); and (ii) *the dielectric function method* (Van Camp *et al* 1979). Although these methods have achieved some success, they both suffer from drawbacks; for example, they involve enormous amounts of computation and these sometimes obscure the physics of what is occurring during lattice vibrations. At present the former is capable of calculating both phonon frequencies at high-symmetry wave-vectors and planar force constants to a reasonable degree of accuracy. Calculations involving frequencies of non-planar vibrations (e.g. in the [110] direction of Ge (Srivastava and Kunc 1985)) or specific heats, are more difficult. The most recent results of the latter method (Van Camp *et al* 1985) are within 14% of the experimental results, but do involve an extrapolation procedure.

Model calculations have the dual advantages of providing an easier understanding of the underlying physics and usually an easier calculation. Is it however possible to construct a simple model from which the lattice dynamics of these semiconductors can be accurately calculated? In this paper we present a first attempt at such a model

calculation. The approach is based on the concept of generalised pseudo-atoms (Ball 1975), which describes the change in charge density caused by a phonon travelling through the crystal (Ball 1982a). This gives a simple physical picture of what is happening.

Consider a crystal with ions at $l + R_s^0$ where $l$ is a lattice point and $R_s^0$ is the position of the ion within the unit cell. Suppose a phonon changes this position by an amount $\delta R_s \exp(\text{i}q \cdot l)$. Then if the effective charges are zero, the charge density, $n(r)$, in the crystal can be uniquely written, to first order in $\delta R$,

$$
n(\boldsymbol{r})=\sum_{\boldsymbol{l}, s}\left[\rho_{s}\left(\boldsymbol{r}-\boldsymbol{l}-\boldsymbol{R}_{s}^{0}\right)+\delta \boldsymbol{R}_{s} \cdot\left(-\nabla \rho_{s}\left(\boldsymbol{r}-\boldsymbol{l}-\boldsymbol{R}_{s}^{0}\right)+\nabla \times \boldsymbol{B}_{s}\left(\boldsymbol{r}, \boldsymbol{l}+\boldsymbol{R}_{s}^{0}\right)\right)\right] \tag{1}
$$

where $\rho(r-l-R_s)$ is the charge that moves rigidly with the ion and $\delta R_s \cdot \nabla \times B_s(r, l + R_s)$ is the deformation charge density.

The electronic contribution to the dynamical matrix can be expressed in terms of the change in electronic charge density (see § 2) and the unscreened ionic pseudopotential, $W_s$. Thus a knowledge of the pseudo-atoms allows us to calculate the frequencies of the phonons.

To calculate the lattice dynamics of germanium, we construct models for the pseudo-atom based on the bond-charge model of Phillips (1973). In this paper we present calculations using a simple rigid-ion approximation in which half of each bond charge is fixed rigidly to its accompanying ion, as in the calculations of Martin (1969). Our work, however, is different from Martin's as it uses a quantum-mechanical dynamical matrix and a proper charge distribution for the bond-charges, not point charges. In addition we also incorporate exchange-correlation (XC) effects, so that our calculation is completely quantum-mechanical, whereas Martin's calculation often involves classical Coulomb interactions, point charges and does not incorporate XC effects.

The way we calculate the XC effects is new, and uses perturbation theory to derive a separate expression for the energy contribution of the XC effects. It has some interesting consequences, a particular one being that it introduces a strong attractive force between the two halves of the bond charge.

It should be stressed that this is the first stage in the construction of a suitable model. Further effects, for example non-rigid movement of the bond charges, as in Weber's model (Weber 1977), may be important. The aim of this paper is to lay the foundations for a model and to see whether such an approach is feasible; i.e. can reasonable results be obtained without resorting to much more complicated calculations?

## 2. The quantum-mechanical dynamical matrix

A crystal has translational symmetry so that we are interested in the Fourier components of the change in charge density due to a phonon of wave-vector $q$. We define a vector function $f_s^e(q + g)$ in terms of the static electron density response function, $\chi$ (Sham 1974)

$$
-\mathrm{i} f_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})=\sum_{\boldsymbol{g}^{\prime}} \chi\left(\boldsymbol{q}+\boldsymbol{g}, \boldsymbol{q}+\boldsymbol{g}^{\prime}\right)\left(\boldsymbol{q}+\boldsymbol{g}^{\prime}\right) W_{s}\left(\boldsymbol{q}+\boldsymbol{g}^{\prime}\right) \exp \left[\mathrm{i}\left(\boldsymbol{g}-\boldsymbol{g}^{\prime}\right) \cdot \boldsymbol{R}_{s}^{0}\right] \tag{2}
$$

where $W_s(r)$ is the unscreeened pseudopotential of the ion at $R_s$. The dynamical matrix is then $\Phi_{\alpha \beta}(q ; s, s')$ (Sham 1974).

$$
\Phi_{\alpha \beta}\left(\boldsymbol{q} ; s, s^{\prime}\right)=\left(M_{s} M_{s^{\prime}}\right)^{-1 / 2} \sum_{\boldsymbol{g}}\left(V_{\alpha \beta}\left(\boldsymbol{q}+\boldsymbol{g} ; s, s^{\prime}\right)-\delta_{s s^{\prime}} \sum_{s^{\prime \prime}} V_{\alpha \beta}\left(\boldsymbol{g} ; s, s^{\prime \prime}\right)\right) \tag{3}
$$

where
$$
\begin{aligned}
V_{\alpha \beta}(\boldsymbol{q}+\boldsymbol{g} ; s, s^{\prime}) & =(\boldsymbol{q}+\boldsymbol{g})_{\alpha}\left\{(\boldsymbol{q}+\boldsymbol{g})_{\beta} Z_{s} Z_{s^{\prime}} v(\boldsymbol{q}+\boldsymbol{g}) \exp \left[\mathrm{i}(\boldsymbol{q}+\boldsymbol{g})\left(\boldsymbol{R}_{s}-\boldsymbol{R}_{s^{\prime}}\right)\right]\right. \\
& \left.-\mathrm{i} W_{s}^{*}(\boldsymbol{q}+\boldsymbol{g}) f_{s^{\prime} \beta}^{\mathrm{e}}\left(\boldsymbol{q}+\boldsymbol{g}^{\prime}\right) \exp \left[\mathrm{i} \boldsymbol{g} \cdot\left(\boldsymbol{R}_{s}-\boldsymbol{R}_{s^{\prime}}\right)\right]\right\}.
\end{aligned}
\tag{4}
$$

The first term in (4) is the direct ion-ion interaction, and the second is caused by the movement of the electrons. We call (3) the quantum-mechanical dynamical matrix as it is derived from first principles. This distinguishes it from the dynamical matrix in terms of force constants (Maradudin et al 1971).

If there are no effective charges, $f_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})$ is continuous as $\boldsymbol{q} \rightarrow \mathbf{0}$. We then write the vector field $\boldsymbol{f}_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})$ in the form
$$
\boldsymbol{f}_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})=-\mathrm{i}(\boldsymbol{q}+\boldsymbol{g}) \rho_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})+\mathrm{i}(\boldsymbol{q}+\boldsymbol{g}) \times \boldsymbol{B}_{s}(\boldsymbol{q}+\boldsymbol{g})
\tag{5}
$$
thereby defining $\rho_{s}^{\mathrm{e}}$ and $\boldsymbol{B}_{s}$. These both have Fourier transforms, which are the electronic part of the rigid ion and the deformation charge density respectively of the ion at $\boldsymbol{R}_{s}$. If there is a non-zero effective charge, $f_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})$ is not continuous for $\boldsymbol{g} \neq \mathbf{0}$, and the charge density cannot be expressed in direct space solely in terms of a sum of rigid ions and deformable charge densities (Ball 1977, 1982b).

Note that the charge density is necessarily a real quantity but that the vector field $\boldsymbol{f}_{s}^{\mathrm{e}}(\boldsymbol{q}+\boldsymbol{g})$ is not always real.

Our aim is to bypass the explicit calculation of $f_{s}^{\mathrm{e}}$, and use our knowledge of the physical situation to develop a model for $f_{s}^{\mathrm{e}}$. By using our knowledge of the non-perturbed crystal, we can determine the parameters of the model; these can then be used in the dynamical matrix to calculate the phonon frequencies.

In (3) and (4) translational invariance is automatically satisfied. The acoustic sum rule is also satisfied if the pseudo-atoms are neutral. The electronic parts of the two terms in (3) come from two different terms in a perturbation calculation (Sinha 1973): the first, as can be seen from (4), is the product of the first-order change in an operator, the unscreened pseudopotential, and the first-order change in the charge density. The second comes from the product of a term which is zeroth order in the charge density and a term which is second order in the pseudopotential.

In our model calculation we make the pseudo-atoms neutral thereby ensuring that the acoustic sum rule is satisfied. We also ensure that translational invariance is satisfied, by calculating the expression (4) and then deriving the second term in (3) from it. Thus we only consider electronic contributions which are the product of first-order changes in an operator and first-order changes in the charge density.

There are no explicit Hartree or exchange-correlation (XC) terms in (3) and (4); all the Hartree and XC effects on the phonon frequencies come about through their effects on the change in charge density, i.e. on $f_{s}^{\mathrm{e}}$. Formulae (3) and (4) can be derived from either Hartree or Kohn-Sham equations. If the latter are used to calculate $f_{s}^{\mathrm{e}}$, then $f_{s}^{\mathrm{e}}$, and hence (3) and (4), contain XC effects. If however Hartree equations are used to calculate $f_{s}^{\mathrm{e}}$, (3) and (4) do not include XC effects and these will have to be added in later. Our model of $f_{s}^{\mathrm{e}}$ is an approximation to its Hartree value, so that we should calculate the XC effects separately and then add them to the results of (4).

As XC effects are, in general, small relative to electron-ion interactions and Hartree effects, they are not easily visible in $f_{s}^{\mathrm{e}}$. Great care in the calculation of $f_{s}^{\mathrm{e}}$ is required if XC effects are to be taken into account when formula (4) is used to calculate the phonon frequencies. This is probably one of the reasons why the accurate calculation of phonon frequencies by the dielectric function method has been difficult. The total energy method

however does not have this drawback as it calculates the energy due to the xc effects directly. In our model calculation we shall also calculate the xc energies directly.

## 3. The model
Physical considerations suggest a bond charge model (Phillips 1973) for the charge density of tetrahedrally bonded germanium. In this model there is a 'central' part around each ion and bond charges between adjacent ions. How these change when a phonon is present determines the change in charge density $f$. In this paper we make the following assumptions.

(i) The 'central' part is non-polarisable and moves rigidly with the ion. Its Fourier components are given by
$$
W_{s}(\boldsymbol{q}+\boldsymbol{g}) /(\varepsilon(\boldsymbol{q}+\boldsymbol{g}, \boldsymbol{q}+\boldsymbol{g}) v(\boldsymbol{q}+\boldsymbol{g}))
\tag{6}
$$
where $\varepsilon$ is the calculated dielectric constant (Walter and Cohen 1970), and $v$ is the Coulomb interaction.

(ii) Each bond charge consists of two identical parts, each part rigidly attached to the accompanying ion and having total charge
$$
1 / \varepsilon(0,0).
\tag{7}
$$

In most calculations the bond charges are taken as point charges. In our model this assumption is not necessary and the dimensions of the bond charges can be obtained from calculations of the unperturbed crystal. For simplicity we assumed a spherically- symmetric bond charge with a charge density of the form
$$
C(1+\gamma r) \exp (-\gamma r).
\tag{8}
$$
$C$ is related to $\gamma$ by the requirement that the total bond charge be given by (7):
$$
C=\gamma^{3} / 16 \pi \varepsilon(0,0).
\tag{9}
$$
By fitting (8) to the calculated charge densities of the static crystal (Walter and Cohen 1971) the parameter $\gamma$ can be estimated; we found $\gamma$ to be $4.65 \mathrm{au}$.

(iii) The electronic part of a pseudo-atom is taken to consist of a 'central' part and four halves of the nearest bond charges. Note that the pseudo-atom's total charge is zero. In figure 1 the pseudo-atom for the ion at the origin is drawn symbolically. The bond-charge halves are numbered $1,2,3,4$ with, for example, 3 at $a(-1,1,-1) / 8$.

(iv) The pseudo-atom is rigid, i.e. the electronic part moves rigidly with the ion.

The unscreened pseudopotential used was the one used by Kunc and Gomes Dacosta (1985), i.e. the average of the pseudopotentials for Ga and As described by Chelikowsky and Cohen (1976). The advantages of this pseudo-potential are that it is diagonal in reciprocal space and that it reproduces the static lattice constant within $5 \%$.

We now have a complete description of our model pseudo-atom and this can be used in the dynamical matrix (3) to calculate the phonon frequencies. The ion-ion contributions are calculated by the Ewald method. In the calculations of the electronic contributions, sufficient reciprocal lattice vectors $(17^{3})$ were used to ensure that any neglected terms were of the order of $10^{-6}$ times the main terms.

The results were interesting but disappointing. For example in the [100] direction the longitudinal frequencies had the correct shape (see figure 2) but were too small,

whereas the transverse acoustic (TA) modes were unstable. Even more disappointing were the results in the [111] direction where all acoustic modes were unstable.

These results were surprising in the light of the results of Martin (1969), Cochran (1959) and Weber (1977), who all had stable TA modes. All these calculations involve 'classical' forces and incorporate electron-electron interactions; Weber's bond charge

![](./images/812465311893684224_1.jpg)

Figure 1. Symbolic representation of the pseudo-atom for the ion at the origin. The 'central' part of the ion at (a/4) (1, 1, 1) is shown broken.

model also incorporates valence forces of the type used by Keating (1966). The dynamical matrix (3), however, does not explicitly incorporate such interactions because, as we have already pointed out, such interactions only influence the nature of $f_{s}^{e}(q+g)$, the change in charge density.

We needed to find out what was wrong with our model pseudo-atom. We examined the effects on the results in the [100] direction of five possible changes in the pseudo-atom; these were as follows.

(a) The 'central' charge density was not accurately given by (6).
(b) The charge on the bond charges was too small.
(c) The rigid-ion approximation needed to be relaxed.
(d) There was significant movement of charge within the pseudo-atom.
(e) The exchange-correlation effects were very important (we defer consideration of this until $\S 4$).

To test possibility (a) we performed a Fourier transform on the 'central' part of the pseudo-atom as given by (6) to see what it looked like in direct space. Outside the ion cores it was very similar in shape to the charge density expected, i.e. to the charge density of one electron in an atomic s state and three electrons in the atomic p state. There was some overlap with the bond charges. Reducing this overlap by changing the range of the 'central' part increased the TA instability. Increasing the overlap had little effect; it would be more sensible to increase the bond charge, as in (b).

![](./images/812465311893684224_2.jpg)

Figure 2. The initial results (full curve) for the calculated frequencies for the longitudinal modes in the [100] direction. These results do not contain the XC effects. The experimental measurements of Nilsson and Nelin (1971) are the broken curves. $\zeta$ is $q/q_{\max}$.

This has a small effect on the TA modes but increases the L frequencies dramatically. For example the L frequencies could be brought into reasonable agreement with experiment by a 25% increase in the bond charge but the TA modes were still unstable. For these to be made stable a much larger increase in the bond charge would be necessary and then the L frequencies would be much too large.

To test hypothesis (c) we used a slightly modified version of Weber's (1977) bond charge model to determine the positions of the bond charges: the details will be given in a later paper. For reasonable values of the parameters, the effect on the phonon frequencies is not sufficient to stabilise the TA modes. It is possible to stabilise these modes if unlikely values are used but these distort the shape of the whole phonon spectrum, including the longitudinal modes.

The possible movement of charge (i.e. hypothesis (d)) when phonons are present is interesting. We assume that charge can only move within each rigid pseudoatom, i.e. charge can move from bond charge to bond charge or to 'central' part or vice versa. Thus for (100) phonons charge (+ or -) may move from bond charges 3 and 4 to bond charges 1 and 2. Such movement, if independent of $q$, would give rise to a dipole, which would

contribute to the effective charge. This may occur in some crystals, but in germanium the symmetry requires the effective charge to be zero. To ensure this the movement of the charges must sum to zero. This could be achieved within our model by assuming that the 'central' part is polarisable, as in the shell model (Sinha 1973). Thus when charge moves from bond charges 3 and 4 to 1 and 2, thereby creating a dipole $d$, the shell moves in such a way that it creates a dipole $-d$. Altogether a quadrupole is formed. The magnitude of this quadrupole is limited however by the magnitude of the bond charges as only a charge $1 / \varepsilon(0,0)$ can move from a bond charge. Even with this maximum amount the TA modes were not stabilised.

Thus none of the effects (a)-(d) on their own can stabilise the TA modes satisfactorily. We have not tested to see whether any combination might do better. Note that none of the effects (a)-(d) causes any direct increase in energy when the two parts of each bond charge move apart, i.e. there is no attraction between the two parts of the bond charge. Any increase comes only from the attraction of one half to the other ion, i.e. from the ion-bond charge force. We now investigate the exchange-correlation (XC) effects, (e), and will see that they do give rise to an attractive force between the two halves of a bond charge.

### 4. Exchange-correlation effects

To calculate the effect of the XC interaction on the charge density is extremely difficult. It is easier to calculate its effect on the phonon energies directly. The XC interaction only affects the electrons. It is, however, small in comparison with both the electron-ion attraction and the Hartree interaction so that it should be possible to calculate the XC effects on the electrons by standard perturbation theory.

The fact that phonon energies may be very small does not invalidate the use of perturbation theory for the XC effects. This is because we are comparing the XC interaction with the electron-ion attraction and the Hartree terms, which are always large, whereas the phonon energies also include the effects of the ion-ion interaction which often cancel the other effects.

In the approximation of slowly varying electronic density $n(\boldsymbol{r})$, the XC operator in the Kohn-Sham (Kohn and Sham 1965) equations is

$$
\mu_{\mathrm{XC}}(\boldsymbol{r})=-(3 \alpha / 2 \pi)\left(3 \pi^{2} n(\boldsymbol{r})\right)^{1 / 3} \tag{10}
$$

where $\alpha$ is a number usually about $\frac{2}{3}$. It is sometimes used as a parameter as the XC effects may vary from material to material; in our calculations we have used $\alpha=0.8$, as used by Kunc and Gomes Dacosta (1985).

The XC energy in the above approximation is

$$
\frac{3}{4} \int n(\boldsymbol{r}) \mu_{\mathrm{XC}}(\boldsymbol{r}) \mathrm{d}^{3} r \tag{11}
$$

where the coefficient $(\frac{3}{4})$ comes about because of self-consistency (Kohn and Sham 1965). The Kohn-Sham equations are a set of one-electron equations and in (11) the $n(\boldsymbol{r})$ term plays the role of the probability amplitude, i.e. the square of the modulus of the wavefunction; $\mu_{\mathrm{XC}}(\boldsymbol{r})$ plays the role of the XC operator. Thus to first order in $\mu$, the exact charge density $n(\boldsymbol{r})$ may be replaced by the charge density which is independent of $\mu$. This is the approximation we shall make, i.e. replace the exact charge density in (11) by

the one that is independent of xc effects. Such an approximation is easy to make as our pseudo-atom supposedly gives that charge density.

This ends the perturbation treatment of the xc effects. As the phonons are also treated in perturbation theory, it is essential to distinguish between the two perturbation treatments. From now on, unless specifically stated, any discussion of perturbation theory refers to the effect of the phonons.

We now examine (11) to find the change in xc energy due to the phonon perturbation. Let us write $n(\boldsymbol{r})$ (see (1)) in a shorthand form:
$$
n(\boldsymbol{r})=n_{0}(\boldsymbol{r})+f_{1}(\boldsymbol{r})+f_{2}(\boldsymbol{r}) \tag{12}
$$
where $n_{0}(\boldsymbol{r})$ is the charge density of the unperturbed crystal and $f_{1}(\boldsymbol{r})$ and $f_{2}(\boldsymbol{r})$ are respectively the first- and second-order changes in charge density. Then
$$
\mu_{\mathrm{XC}}(\boldsymbol{r})=\mu_{0}(\boldsymbol{r})+\mu_{1}(\boldsymbol{r})+\mu_{2}(\boldsymbol{r}) \tag{13}
$$
with
$$
\mu_{1}(\boldsymbol{r})=-(3 \alpha / 2 \pi)\left(3 \pi^{2} n_{0}(\boldsymbol{r})\right)^{1 / 3}\left(f_{1}(\boldsymbol{r}) / 3 n_{0}(\boldsymbol{r})\right) \tag{13a}
$$
and
$$
\mu_{2}(\boldsymbol{r})=-(3 \alpha / 2 \pi)\left(3 \pi^{2} n_{0}(\boldsymbol{r})\right)^{1 / 3}\left[\left(f_{2}(\boldsymbol{r}) / 3 n_{0}(\boldsymbol{r})\right)-\frac{1}{9}\left(f_{1}(\boldsymbol{r}) / n_{0}(\boldsymbol{r})\right)^{2}\right] \tag{13b}
$$
provided $n_{0}(\boldsymbol{r})$ is not zero. If at some point $\boldsymbol{r}, n_{0}(\boldsymbol{r})$ is zero, we approximate $\mu_{\mathrm{XC}}(\boldsymbol{r})$ by taking it to be zero.

Substituting this into (11), the xc energy becomes
$$
\frac{3}{4} \int \mathrm{d}^{3} r\left[\mu_{0} n_{0}+\left(\mu_{1} n_{0}+\mu_{0} f_{1}\right)+\left(\mu_{0} f_{2}+n_{0} \mu_{2}\right)+\left(\mu_{1} f_{1}\right)\right]. \tag{14}
$$

The zeroth-order terms are the static xc energy; the first-order terms should be included in the first-order contribution to the energy, which should be zero as the lattice is in equilibrium. The very last term, $\int \mu_{1} f_{1} \mathrm{~d}^{3} r$ is of the form expected from (4), i.e. a change in charge density times the change in an operator. We thus take the xc energy which contributes to the dynamical matrix as
$$
\frac{3}{4} \int f_{1}(\boldsymbol{r})(-\alpha / 2 \pi)\left(3 \pi^{2} n_{0}(\boldsymbol{r})\right)^{1 / 3}\left(f_{1}(\boldsymbol{r}) / n_{0}(\boldsymbol{r})\right) \mathrm{d}^{3} r. \tag{15}
$$

This is the result we shall use in our calculations. The other terms, $\int\left(\mu_{0} f_{2}+n_{0} \mu_{2}\right) \mathrm{d}^{3} r$, if our analysis following equations (3) and (4) is correct, contribute only to the second-order terms which make (3) translationally invariant. We note however that in (13b) the last term contributes an amount which is $(-\frac{1}{3})$ times the term (15), which would reduce (15) by a factor $(\frac{2}{3})$ if it were included.

The advantage of describing the charge density in terms of pseudo-atoms is that each pseudo-atom is associated with an ion. Thus the energy of interaction between two ions at $\boldsymbol{R}_{j}$ and $\boldsymbol{R}_{k}$ caused by the xc effects is calculated using the electronic part of the pseudo-atoms at $\boldsymbol{R}_{j}$ and $\boldsymbol{R}_{k}$. If these are fairly well localised, these interactions will be zero unless $\boldsymbol{R}_{j}$ and $\boldsymbol{R}_{k}$ are close.

We now calculate (15) in our model of the pseudo-atom for Ge. To simplify matters, we assume that the overlap of the 'central' part of a pseudo-atom with any other pseudo-atom is negligible. Thus only the bond charges contribute to the xc forces between two different ions. The bond charges are also well localised so that overlap only occurs

between two neighbouring ions and this occurs through the two halves of their common bond charge.

In our model each half moves rigidly with its ion so that it is easy to express this contribution to (15). The change in charge density is given by the gradient of (8). As the bond charges are spherically symmetric, the integrand in (15) is axially symmetric and integration over the angles can be done analytically. The remaining integration was done numerically using Simpson's rule.

The result is a strong attractive force between the two halves of the bond charge, thereby tending to bind them together. This is just what was required to make the acoustic modes stable. As far as the author is aware this is the first time that this force has been shown to exist and has been calculated from the Kohn-Sham XC operator (10). This force is important in molecular physics where it is usually assumed that valence electrons like to overlap. Indeed in Weber's model (Weber 1977), the bond charge is assumed to be indivisible; this could be taken to mean that the force binding the two parts of the bond charge together is infinite. We discuss the relevance of this new force to molecular physics further in § 5.

It is easy to incorporate this force into the dynamical matrix. It acts as a nearest-neighbour force, and stabilises all the modes.

The results are shown in figure 3, along with the experimental results of Nilsson and

![](./images/812465311893684224_3.jpg)

Figure 3. The calculated frequencies (full curves) which incorporate the XC effects using (15). The broken curves are the experimental measurements of Nilsson and Nelin (1971). $\zeta$ is $q/q_{max}$.

Nelin (1971). The results are very encouraging: the inclusion of the XC effects improves the agreement with experiment of all the modes. The longitudinal modes are all in reasonable agreement with experiment: the optical $\Gamma$O frequency is very close to the

experimental value: even the transverse frequencies approximate to the experimental ones.

There is room for improvement in the calculations. For example the TA modes have elastic constants that are slightly too small and the TA modes do not show the famous flat behaviour for large $q$. These discrepancies are probably due to our unsophisticated model of the pseudo-atom. If assumptions (iii) and (iv) (see § 3) are relaxed, and in particular if the bond charges are allowed some non-rigid movement, it is hoped that these discrepancies would disappear.

Nevertheless in view of the simple model of the pseudo-atom used these results can be considered as good. They stand comparison with the model calculations of Martin (1969) and Cochran (1959), with many of the calculations using the dielectric function matrix (Van Camp et al 1983) and in the [110] direction with total-energy calculations (Srivastava and Kunc 1985).

It came as a surprise to the author that the XC effects could give rise to such a large force. The reason it is so large is that the charge density at the bond charges is large. In retrospect it is clear from molecular physics that a force binding the bond charge together must exist and must be reasonably large. Our calculations (see § 3) showed that such a force does not come from ionic attraction so the XC effects are the only possible mech- anism for providing it. These calculations confirm this.

There are two calculations which confirm the importance of XC effects in the lattice dynamics of diamond-type semiconductors. The first, by Van Camp et al (1983) in silicon found that the $\Gamma$O and TA(X) frequencies increased considerably when XC effects were included. Fleszar et al (1985) found that XC effects were needed to stabilise the TA(X) mode. They found however that there was hardly any change in the $\Gamma$O frequency when XC effects were included. It should be remembered that theirs was a self-consistent calculation, and not a model calculation like ours. The changes caused by the inclusion of XC effects are therefore likely to be different.

### 5. Discussion

The two main advantages of our approach to the microscopic calculation of lattice dynamics are firstly that it does not require enormous computation and secondly that it uses simple physical models to describe what is happening.

The computations involved in the calculations in this paper were so short that they were done interactively on a mainframe computer. The programming was simple even in the [110] direction; most of the computing time was taken up with summing over the reciprocal lattice vectors for each value of $\boldsymbol{q}$. The amount of computation may increase if our approach becomes more sophisticated, for example if a more complicated model for the pseudo-atom or a non-local pseudopotential were to be used, but even then the computation will still be an order of magnitude less than is involved in the other microscopic methods mentioned in § 1.

The simplicity of our calculation, in contrast to the enormous quantity of data involved in the other methods, makes physical understanding easier. This is also facili- tated by the 'model' approach because what is happening in lattice dynamics can be understood in terms of the model (for example pseudo-atoms and bond charges). The 'model' approach also sometimes leads to new concepts and new ways of understanding. For example our calculations have introduced the picture of bond charge distortion (see below) and the consequent increase in energy due to XC effects.

Pseudo-atoms and the lattice dynamics of germanium

A minor advantage of using models is that some of the parameters of the model can be deduced from calculations already made, as in our derivation of the dimensions of the bond charge. This is where the total energy calculations may be very useful in the future: when the pseudo-atom model is made more sophisticated, some of the required parameters may be deducible from particular total energy calculations.

It is noteworthy that it was essential to include the XC effects in our calculations because without them several acoustic modes are unstable. There are two remarks we would like to make about the way we included the XC interaction. The first is that the use of perturbation theory in the direct calculation of the XC energy contribution allowed us to bypass the explicit calculation of the XC effect on the charge density, which is one of the most difficult parts of lattice dynamical calculations. It may be possible to use this approach in other calculations, for example in using the dielectric function method.

The second remark is that the XC effects give rise to a force which binds the two parts of the bond charge together. It is surprising that such a small interaction as the XC interaction can give rise to a strong force, but it should be remembered that the electronic charge density at the bond charges is four or five times the maximum electronic charge density elsewhere.

Both in our model and in actuality, all other XC effects on the phonon frequencies are negligible, because charge densities are small everywhere except at bond charges and in 'central' parts. The XC effects may tend to ensure that a 'central' part travel rigidly with its ion, but this has been assumed in our model already.

The method of calculation of the XC binding force developed in this paper may be useful in other situations. For example it should make the microscopic calculation of the vibration frequencies of molecules easier. This in turn may lead to a better understanding of the forces involved in molecular vibrations.

Let us then briefly discuss what happens when covalently bonding systems vibrate. The electronic charge density is large midway between two ions in a covalent bond in a molecule, and can be called a 'bond charge'. This bond charge needs to be described not only in terms of the position of its centre of charge but also in terms of its shape and density. The reason why there is a 'bond charge' is, according to the Huckel view, that the electrons want to be attracted to both ions. This is probably correct in the equilibrium situation; however when neighbouring ions move, each half of the intermediate bond charge wants to move with its accompanying ion and so the bond charge is likely to distort; how much will it distort and how far does its centre of charge move from the position midway between the ions? What are the forces on the two halves of a bond charge and what are their relative strengths?

According to our calculations, there are situations in which our model pseudo-atoms have a lower energy than the equilibrium energy if only the ion-ion, ion-electron and Hartree energies are taken into account; certainly the change in these energies is not sufficient to stabilise the lattice in germanium. Our model pseudo-atom would lead to a distorted bond charge, but with its centre of charge midway between the ions. Our calculations suggest that the XC effects tend to diminish such distortion, as it pulls the two halves of the bond charge together. Thus, within our model, the centre of charge lies midway between the ions but the bond charge is distorted with the distortion diminished by the XC effects.

Incorporation of Keating forces, as in Weber's (1977) model will alter the pseudo-atom by adding parts of non-adjacent bond charges. This is too complicated to discuss further here except to say that Weber's model takes the movement of the centre of charge of bond charges into account but does not consider bond charge distortion.

One of the pleasing aspects of our calculations is that reasonable results have been obtained without taking into account the fine detail of the charge density. Obviously the effects that determine the gross features of the phonon spectrum are contained within our model. Nevertheless our results do not completely agree with the experiment. For example the elastic constants and the flatness of the TA modes have not been reproduced, nor has the crossover of the optical frequencies in the [100] direction. Altogether there is room for improvement in the calculation of the TO frequencies. Whether these features can be reproduced by a model, or need the fine details which can only be calculated by a large computation using one of the two methods mentioned in $\S 1$ remains to be seen.

We remain hopeful however that some modifications to our model will reproduce these features. Two parts of our model probably merit scrutiny. The first is the way (see (8)) we have described the bond charge. The force between the two parts of the bond charge may depend critically on the accuracy of this description. A more accurate description might improve the transverse elastic constants.

The second and more important feature is the nature of our pseudo-atom. Assump- tions (iii) and (iv) need altering, i.e. the idea that half of each bond charge is rigidly attached to its adjacent ion needs changing. The movement of the halves of the bond charges needs calculating self-consistently, i.e. under the influence of the forces acting upon each half. This calculation would be similar to the Weber (1977) phenomenological model but would incorporate the finiteness of the force between the two halves of the bond charge, which we have shown arises from the XC effects. We hope to show how this is done in a later paper. Weber was able to reproduce the flatness of the TA modes so that this feature should be a function of the position of the centre of charge of the bond charge. It should carry over to a microscopic calculation.

## References

Ball M A 1975 *J. Phys. C: Solid State Phys.* **8** 3328-40
—— 1977 *J. Phys. C: Solid State Phys.* **10** 4921-30
—— 1982a *J. Phys. C: Solid State Phys.* **15** 229-39
—— 1982b *J. Phys. C: Solid State Phys.* **15** 5937-44
Chelikowsky J R and Cohen M L 1976 *Phys. Rev.* B **13** 826-30
Cochran W 1959 *Proc. Roy. Soc.* A **253** 260
Fleszar A, Kunc K, Resta R and Tosatti E 1985 *Phonon Physics* ed. J Kollar, N Kroo, N Menyhard and T Siklos (Singapore: World Scientific)
Keating P N 1966 *Phys. Rev.* **145** 637
Kohn W and Sham L J 1965 *Phys. Rev.* **140** 1133-7
Kunc K and Gomes Dacosta P 1985 *Phys. Rev.* B **32** 2010-21
Kunc K and Martin R M 1982 *Phys. Rev. Lett.* **48** 406-10
Maradudin A A, Montroll E W, Weiss G H and Ipatova I P 1971 *Theory of Lattice Dynamics in the Harmonic Approximation* (London: Academic)
Martin R M 1969 *Phys. Rev.* **186** 871-84
Nilsson G and Nelin G 1971 *Phys. Rev.* B **3** 364-70
Phillips J C 1973 *Bonds and Bands in Semiconductors* (London: Academic)
Sham L J 1974 *Dynamical Properties in Solids* I ed. G K Horton and A A Maradudin (Amsterdam: North-Holland)
Sinha S K 1973 *Crit. Rev. Solid State Sci.* **3** 273-336
Srivastava G P and Kunc K 1985 *Phonon Physics* ed. J Kollar, N Kroo, N Menyhard and T Siklos (Singapore: World Scientific)
Van Camp P E, Van Doren V E and Devreese J T 1979 *Phys. Rev. Lett.* **42** 1224
—— 1983 *Ab Initio Calculation of Phonon Spectra* ed. J T Devreese, P E Van Camp and V E Van Doren (New York: Plenum) pp 25-48

—— 1985 *Phonon Physics* ed. J Kollar *et al* (Singapore: World Scientific)

Walter J P and Cohen M L 1970 *Phys. Rev.* B **2** 1821–6

—— 1971 *Phys. Rev.* B **4** 1877

Weber W 1977 *Phys. Rev.* B **15** 4789–803

Wendel H and Martin R M 1979 *Phys. Rev.* B **19** 5251