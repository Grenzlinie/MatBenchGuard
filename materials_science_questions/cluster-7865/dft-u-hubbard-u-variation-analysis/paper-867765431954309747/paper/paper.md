# Thermodynamics of spin crossover in ferropericlase: an improved LDA+$U_{sc}$ calculation

Yang Sun, $^{1}$ Jingyi Zhuang, $^{2,3}$ and Renata M. Wentzcovitch$^{1,2,3,*}$

$^{1}$ Department of Applied Physics and Applied Mathematics,
Columbia University, New York, NY 10027, U.S.A.
$^{2}$ Department of Earth and Environmental Sciences,
Columbia University, New York, NY 10027, U.S.A.
$^{3}$ Lamont–Doherty Earth Observatory, Columbia University, Palisades, NY 10964, U.S.A.

(Dated: Feb. 20, 2022)

We present LDA+$U_{sc}$ calculations of high-spin (HS) and low-spin (LS) states in ferropericlase (fp) with an iron concentration of 18.75%. The Hubbard parameter $U$ is determined self-consistently with structures optimized at arbitrary pressures. We confirm a strong dependence of $U$ on the pressure and spin state. Static calculations confirm that the antiferromagnetic configuration is more stable than the ferromagnetic one in the HS state, consistent with low-temperature measurements. Phonon calculations guarantee the dynamical stability of HS and LS states throughout the pressure range of the Earth mantle. Compression curves for HS and LS states agree well with experiments. Using a non-ideal mixing model for the HS to LS states solid solution, we obtain a crossover starting at $\sim$45 GPa at room temperature and considerably broader than previous results. The spin-crossover phase diagram is calculated, including vibrational, magnetic, electronic, and non-ideal HS-LS entropic contributions. Our results suggest the mixed-spin state predominates in fp in most of the lower mantle.

## I. INTRODUCTION

Ferropericlase (fp) is the second most abundant mineral in the Earth's lower mantle. It may be responsible for up to $\sim$20 vol% of this region [1]. It is a solid solution $(Mg_{1-x}Fe_{x})$O of MgO and FeO in the rocksalt-type (B1) crystal structure, with $x_{Fe}$=0.15-0.20 in the lower mantle. Its high-pressure electronic properties, spin state, and phase stability are critical to understanding the properties of and processes taking place in the mantle. In particular, iron in fp undergoes a pressure-induced spin-crossover from a high spin (HS) state with S=2 to a low spin (LS) state with S=0. This spin-crossover has attracted extensive research interest because it can have critical geophysical consequences, e.g., a density increase [2], a bulk modulus softening [3], thermoelastic anomalies [4, 5], etc.

Experiments have reported an HS-LS crossover pressure in the range of 40-70 GPa at room or lower temperatures [6-10], with $x_{Fe}$ around 0.20. High temperature leads to an increase in the spin-crossover pressure range and in the crossover onset pressure. This is caused by a mixed HS-LS state (MS) [2, 7, 11] caused entropic contributions. Because of the strongly correlated nature of the $3d$ electrons in Fe and the large supercells used to study the fp solid-solution by first-principles, the HS-LS crossover diagram has been challenging. Tsuchiya *et al.* [2] first performed LDA+$U$ calculations to study the HS and LS crossover with HS/LS configuration entropy and magnetic entropy. Later Ref.[4] extended LDA+$U$ calculations to include vibrational effects based on a virtual-crystal model. The model was also used to calculate thermodynamic anomalies in fp [3]. While LDA+$U$ can reasonably address the electronic structure of the correlated $3d$ electrons of iron, its performance on the crossover pressure highly depends on the $U$ value [12-17]. It has been argued that the complete dependence of $U$ on pressure/volume, structure, spin state, or even pseudopotential should be taken into account if one is to make predictions of phase transitions at extreme conditions. In this work, we employ a recent implementation of the self-consistent calculation of the Hubbard parameter based on density-functional perturbation theory (DFPT) [18]. Using LDA+$U_{sc}$ calculations, we compute the spin crossover diagram for fp with $x_{Fe}$=0.1875. This calculation differs from previous ones from our group by computing the HS and LS states' vibrational spectra vs. volume and going beyond the ideal solid-solution model by computing the excess free energy due to HS-LS interaction in the MS state.

In the next section, we describe the computational details of the first-principle calculations. In Sec. III, we first analyze the electronic structure of ferropericlase with $x_{Fe}$=0.03125. In Sec. IV, we present static calculations of the spin-crossover of fp with $x_{Fe}$=0.1875 at T=0K. In Sec. V, we compute the phonon spectra and consider the finite temperature effect on the spin crossover by including various entropic contributions and non-ideal mixing effects. We summarize all findings in Sec. VI.

## II. METHODS

LDA+$U$ calculations were performed using the simplified formulation of Dudarev *et al.* [19] as implemented in the Quantum ESPRESSO code [20, 21]. The local density approximation (LDA) was used for the exchange-correlation functional with spin polarization. The projector-augmented wave (PAW) data

* Email: rmw2150@columbia.edu

sets from the high-accuracy version of PSlibrary [22] were employed with valence electronic configurations $3s^23p^63d^64s^2$, $2s^22p^63s^2$, and $2s^22p^4$ for Fe, Mg, and O, respectively. A kinetic-energy cutoff of 100 Ry for wave functions and 600 Ry for spin-charge density and potentials were used. In all cases, atomic orbitals were used to construct occupation matrices and projectors in the LDA+$U$ scheme. A cubic supercell of B1 structure with 64 atoms was constructed for the current study, i.e., $(\text{Fe}_x\text{Mg}_{1-x})_{32}\text{O}_{32}$. The $2\times2\times2$ $k$-point mesh was used for Brillouin zone integration. Structure optimization was performed by relaxing atom positions with a force convergence threshold of $0.01\ \text{eV}/\mathring{\text{A}}$. The convergence threshold of all self-consistent field (SCF) calculations was $1\times10^{-9}$ Ry.

The Hubbard correction [23] was applied to Fe-$3d$ states. The Hubbard parameter $U$ was computed using density-functional perturbation theory [18] implemented in the Quantum ESPRESSO code. The convergence threshold for the response function is $1\times10^{-6}$ Ry. An automated iterative scheme was employed to obtain the self-consistent $U_{sc}$ parameter while simultaneously optimizing the structure and desired spin state: starting from an empirical $U$ of 4.3 eV, the energies of all possible occupation matrices for a spin state were computed. There are five possible occupation matrices corresponding to the HS state of ferrous iron with $3d^6$ configuration (S=2), while there are ten possibilities for the LS state (S=0). The electronic configuration, i.e., occupation matrix, with the lowest energy, was selected for further structural optimization of lattice parameters and atomic positions. Then a new $U$ parameter is recalculated for further structural optimization. The process continued until mutual convergence of structure and $U$ is achieved for a convergence threshold of 0.01 eV for the $U$ parameter and the convergence criteria mentioned above for structural optimizations. Only the lowest energy configuration was adopted in subsequent calculations. Finite temperature effects on the static DFT energy were included using the Mermin functional with the Fermi-Dirac smearing [24,25]. The temperature-dependent electronic entropy was obtained from 0 K to 4500 K every 500 K and then interpolated. The scheme used here was described in Ref.[26]. We also computed the excess free energy from non-ideal mixing of HS and LS states which is described together with the ideal solution model in Sec. V.

With large unit cells containing 64 atoms, phonon calculations were performed using the finite-displacement method, using Phonopy code [27] with force constants computed by Quantum ESPRESSO. Vibrational density of states (VDOSs) were obtained using a $q$-point $20\times20\times20$ mesh. The vibrational contribution to the free energy was calculated using the quasiharmonic approximation [28] with the $qha$ code [29].

![](./images/867765431954309747_1.jpg)

FIG. 1. (a) The HS state of fp3 at P=0GPa. Gray is Fe, green is Mg and red is O. The charge density (yellow) is shown for the Fe minority electron occupying the $\text{d}_{xy}$ orbital. T Fe-O bond lengths in angstrom $(\mathring{\text{A}})$ are shown inside the octahedron. Mg and O without Fe-O bonds are drawn smaller for clarity. (b) The LS state of fp3 at P=0GPa. The charge density (yellow) is shown for the occupied t2g orbitals. (c) and (d) Projected density of state (DOS) for Fe 3d orbitals in HS and LS fp3 at P=0GPa. The schematic shows the energy splitting of $\text{e}_g$ doublet and $\text{t}_{2g}$ triplet.

### III. ELECTRONIC STRUCTURE FP WITH $x_{Fe}$=0.03125% (FP3)

To first have a clear picture of the electronic structure of fp, we consider only one Mg substitution by Fe in the 64-atom supercell, i.e., $\text{FeMg}_{31}\text{O}_{32}$, $x_{Fe}$=0.03125 (fp3 hereafter), as shown in Fig. 1(a). In this case, there is no Fe-Fe interaction so that the energy levels of the $3d$ orbitals in the ferrous Fe can be well-identified. Ferrous $\text{Fe(Fe}^{2+})$ with $3d^6$ electronic configurations has six O neighbors in octahedral coordination. The octahedral crystal field splits the fivefold d-orbital degeneracy, producing a doublet with $\text{e}_g$ symmetry and a triplet with $\text{t}_{2g}$ symmetry. Because the $\text{t}_{2g}$ orbitals are pointing away from the oxygen neighbors, the $\text{t}_{2g}$ orbitals have lower energy than the $\text{e}_g$ orbitals, shown in Fig 1(c). In the HS state at low pressures, following Hund's rule, five of six electrons occupy five spin-up orbitals, and the remaining minority electron fills one of the $\text{t}_{2g}$ orbitals, as shown in Fig.1(a). The Fe-O octahedron is Jahn-Teller (JT) distorted in this electronic configuration, i.e., it has two short and four long bonds. At P=0 GPa, the difference between the short and long bonds is 2.4% in Fig. 1(a). The JT distortion, in turn, causes further energy splitting within the $\text{e}_g$ and $\text{t}_{2g}$ levels so that one can see a slight energy difference between $\text{d}_{z^2}$ and $\text{d}_{x^2-y^2}$, as well as $\text{d}_{xy}$ and $\text{d}_{zx}$ $(\text{d}_{zy})$. Ferrous Fe can also exhibit the low-

![](./images/867765431954309747_2.jpg)

FIG. 2. (a) Supercell structure of fp18 with (a) ferromagnetic and (b) antiferromagnetic configurations. The [111] planes are indicated in (b). However, in our collinear spin calculations, the direction of the spin magnetic moment is not relevant.

spin (LS) state with all six electrons in the $t_{2g}$ orbitals,
as shown in Fig. 1(d). Because the occupied $t_{2g}$ orbitals
have cubic symmetry, as shown in Fig. 1(b), there is no
JT distortion in the equilibrated LS state. The volume
of the FeO octahedron in the LS state is smaller than
that in the HS state. Comparing the lattices at 0 GPa
in Fig. 1(a) and (b), the octahedron volume of the LS
is 7.4% smaller than the one with $Fe^{2+}$ in the HS state.
Both HS and LS of fp3 are insulators.

## IV. SPIN CROSSOVER OF FP18 AT T=0K

We now perform static calculations to study the spin
crossover in fp at T=0K. For a pyrolitic mantle composition, the fp volume fraction should be around 0.15-
0.20 [1] . Here we focus on the spin crossover in the
$Fe_6Mg_{26}O_{32}$ lattice, i.e., $x_{Fe}$=0.1875 (fp18 hereafter),
while some results on fp3 are also included for comparison. To construct the supercell structure, we distribute
6 Fe uniformly by occupying the face centers and edge
centers, as shown in Fig. 2. Because fp is a solid solution
of FeO and MgO, a uniform distribution is more relevant
to the real situation. Moreover, it has been shown that
different types of Fe configurations have only a small effect on the spin crossover [30]. With $x_{Fe}$=0.1875, one
would expect the exchange interaction between Fe ions
in the HS state to be sizable because of the small Fe-Fe
distance. Here we consider both the ferromagnetic (FM)
and antiferromagnetic (AFM) configurations with spins
aligned as in Figs. 2(a,b). Considering the AFM spin
configuration in FeO-B1 [17], we assign opposite magnetic moments in the AFM configuration alternating in
neighboring [111] planes.

Figure 3 (a) shows the volume-dependent energy for
fp18 HS states with FM and AFM configurations and LS
state. The HS states have lower energy at large volumes
(low or negative pressures) than the LS state. The AFM
configuration has the lowest energy of all. Therefore, at
ambient conditions, the ground state is the HS with AFM
magnetic order. This is consistent with the experimental
measurement that AFM is the ground state below the

![](./images/867765431954309747_3.jpg)

FIG. 3. (a) Upper panel shows the E vs. V curves for the three
states of fp18. The lower panel shows the energy difference
between the HS-AFM and HS-FM. (b) The self-consistent
Hubbard parameters U for different spin states. (c) The enthalpy difference between HS and LS ($\Delta H = H_{HS} - H_{LS}$).

Néel temperature [9]. With decreasing volume, the LS
state energy decreases w.r.t. that of the HS states. This
is mainly because the energy splitting between $t_{2g}$ and
$e_g$ increases with increasing pressure, leading to the spin
crossover. Figure 3(b) shows the self-consistent Hubbard
parameters for the different spin states. The $U_{sc}$ values of
the LS state are systematically higher than the HS states
regardless of volume. This trend is similar to fp3 and previous studies of Hubbard parameters of HS and LS states
in the FeO system [16]. The self-consistent $U$ value of
HS-FM and HS-AFM also shows a slight difference. The
energy-volume data are fitted by the third-order Birch-
Murnaghan (BM) equation of state (EoS) using the least
squares method. The enthalpies are obtained from the
fitted BM-EoS and are shown in Fig. 3(c). Based on
the enthalpy difference, the transition pressure from HS
to LS can be identified. In fp18, the transition pressures are 60 GPa for the FM state and 66 GPa for the
AFM state. By performing similar calculations with fp3,
we find the HS-LS transition pressure in fp3 is 53 GPa.
Therefore the spin crossover pressure increases with an
increasing iron concentration in ferropericlase. This transition pressure in fp18 is in good agreement with the experimental measurement of ferropericlase with $x_{Fe}$=0.17
at room temperature [7], which is $\sim$60GPa. A change in
the distribution of iron in the supercell of fp18 changes
the transition pressure by a few GPa only [29], but it
gives rise to a distribution of transition pressures.

The fp18 compression curves obtained from the zero-
kelvin EoS are shown in Fig. 4. The curves of HS-FM
and HS-AFM states are almost overlapped here. The
experimental measurement at room temperature with
$x_{Fe}$=0.17 ferropericlase [8] is also included for comparison. The calculated zero-kelvin compression curves are

![](./images/867765431954309747_4.jpg)

FIG. 4. Compression curve of fp18. The experimental data is at 300K with $x_{Fe}$=17% ferropericlase [8].

close but systematically smaller than the experimental data. This result is reasonable because no temperature effect is included yet. As discussed later, vibrational effects at finite temperature further improve the agreement with experiments.

Figure 5 shows the projected density of states (DOS) of Fe-$3d$ for fp18. Both HS and LS DOS are qualitatively similar to that of fp3 in Figure 1. However, a larger Fe concentration caused stronger crystal field splitting, leading to complicated energy levels of different orbitals. Nevertheless, both HS and LS states remain to be the insulating states. The gaps are around 2 eV and almost independent of the pressure increasing.

![](./images/867765431954309747_5.jpg)

FIG. 5. Projected density of state (DOS) of the Fe 3d orbitals in fp18 with (a) HS at 0 GPa; (b) HS at 60 GPa; (c) LS at 0 GPa; (d) LS at 60 GPa.

![](./images/867765431954309747_6.jpg)

FIG. 6. Vibrational DOS for (a) HS and (b) LS fp18 with three volumes. The upper and lower panels correspond to the same volume. Their static pressures at zero kelvin are indicated in the figure.

## V. FINITE TEMPERATURE EFFECT ON THE SPIN CROSSOVER

Phonon calculations are performed with LDA+$U_{sc}$ for all calculated volumes of both HS- and LS-fp18. Figure 6 shows examples of three vibrational densities of state (VDOS) from low to high pressures. All other VDOS are shown in Supplementary Fig. S1. With increasing pressure, the phonon frequencies are shifted towards higher energies. No imaginary frequency is found in either HS or LS state up to 100 GPa. This is consistent with the recent phonon calculations in $x_{Fe}$=0.0625 fp with density functional perturbation theory [30]. Therefore, both HS and LS states of fp with iron concentrations lower than 0.1875 are dynamically stable.

With the inclusion of vibrational entropy and electronic entropy described by the Mermin functional in static free energy calculations [24, 25], quasiharmonic calculations are performed to compute the free energy and

![](./images/867765431954309747_7.jpg)

FIG. 7. Static energy as a function n at constant volume V=7.2Å³/atom for ideal mixing and non-ideal mixing models.

EoS at finite temperatures. With the inclusion of ther-
mal electronic excitation effects on the static free energy,
the compression curve of both HS and LS at 300K agrees
very well with room-temperature experimental measure-
ments [8], as shown in Fig. 4. To obtain the HS-LS phase
boundary at finite temperature, we further consider the
non-ideal mixing of HS and LS states and its contribution
to the free energy. Using $n$ to represent the fraction of
LS states, the total free energy of an ideal solid solution
of HS and LS can be written as

$$
G_{i d e a l}(P, T, n)=(1-n) G_{H S}(P, T)+n G_{L S}(P, T)+G_{m i x}^{i d e a l}(n), \quad(1)
$$

where $G_{H S / L S}$ is the molar Gibbs free energy of the
pure HS/LS states, i.e.,

$$
G_{H S / L S}(P, T)=G_{H S / L S}^{s t a t+v i b}(P, T)+G_{H S / L S}^{m a g}, \quad(2)
$$

where $G_{H S / L S}^{s t a t+v i b}(P, T)$ is the Gibbs free energy contain-
ing static and vibrational contribution and $G_{H S / L S}^{m a g}$ is the
magnetic contribution. $G_{H S / L S}^{m a g}$ is a purely entropic con-
tribution that one can estimate approximately as

$$
G^{m a g}=-k_{B} T x_{F e} \ln [m(2 S+1)], \quad(3)
$$

where $S$ and $m$ are the spin and electronic configura-
tion (orbital) degeneracies of iron. In HS, S=2 and m=3.
In LS, S=0 and m=1. The ideal free energy of mixing is
given by the mixing entropy as

$$
G_{m i x}^{i d e a l}(n)=-T S_{m i x}=-k_{B} T x_{F e}[n \ln n+(1-n) \ln (1-n)]. \quad(4)
$$

Eq. (4) gives the free energy of mixing of the ideal
solution of HS and LS states, where $n$ is the LS fraction.
By minimizing the free energy in Eq. (1) with respect to
$n$, one obtains

$$
n_{i d e a l}=\frac{1}{1+m(2 S+1) \exp \left[\frac{\Delta G_{L S-H S}(P, T)}{k_{B} T x_{F e}}\right]}, \quad(5)
$$

where $\Delta G_{L S-H S}(P, T)=G_{L S}(P, T)-G_{H S}(P, T)$.

We now examine the effect of non-ideal mixing of HS
and LS states. In this case, different HS/LS configura-
tions are considered for a single Mg/Fe atomic arrange-
ment in fp18 and several $n$ values. The single Mg/Fe
configuration in the $(Mg_{26} Fe_{6}) O_{32}$ supercell is sampled
for $n=\frac{1}{6}, \frac{2}{6}, \frac{3}{6}, \frac{4}{6}$ and $\frac{5}{6}$. These configurations are listed
in Supplementary Table S1 and Supplementary Figure
S2. The static energy $\varepsilon_{i}$ of the $i^{th }$ non-equivalent atomic
configuration is computed in a large pressure range, us-
ing the consistent Hubbard parameters of fp18 shown in
Fig. 3(b). The non-ideal mixing energy can be obtained
by making a Boltzmann ensemble average for all non-
equivalent arrangements. Then

$$
E_{n o n-i d e a l}=\sum_{i} g_{i} p_{i} \varepsilon_{i}, \quad(6)
$$

where $g_{i}$ is the multiplicity of the $i^{th }$ non-equivalent
atomic configuration and $p_{i}$ is the Boltzmann factor as
$p_{i}=\frac{e^{\varepsilon_{i} / k_{B} T}}{\sum_{i} g_{i} e^{\varepsilon_{i} / k_{B} T}}$. Figure 7 shows that the results from
non-ideal mixing deviate from the one in the ideal mix-
ing model, indicating that the non-ideal mixing effect is
relatively significant when the HS and LS states have
similar static energies at the same volume. . The
excess energy can be obtained by calculating the en-
ergy difference between ideal and non-ideal models as
$E_{e x}(n)=E_{n o n-i d e a l}(n)-E_{i d e a l}(n)$. As can be seen
in Fig. 7, the temperature dependence of $E_{e x}(n)$ is in-
significant. We then include an excess free energy term,
$G_{e x}(P, T, n)$, of non-ideal mixing in Eqn. (1),

$$
G_{n o n-i d e a l}(P, T, n)=G_{i d e a l}(P, T, n)+G_{e x}(P, T, n). \quad(7)
$$

Here we assume the excess free energy is mainly con-
tributed by the static part so that we keep the vibra-
tional contributions the same as the one in the ideal
mixing model, i.e. $G_{e x}(P, T, n) \approx H_{e x}^{s t a t}(P, T, n)$, where
the T-dependence is negligible as in $E_{e x}(n)$. The ex-
cess enthalpy can be obtained by fitting $E_{n o n-i d e a l}$

with $3^{rd}$ BM-EOS, obtaining pressure and adding the $P_{non-ideal}V$ term. Similar to solving the ideal mixing model, $n_{non-ideal}$ can be obtained by minimizing Eqn. (7) with respect to $n$, which leads to

$$
f(P, T, n)=\Delta G_{L S-H S}(P, T)+\frac{\partial H_{e x}(P, T, n)}{\partial n}+k_{B} T x_{F e} \ln \left[\frac{n}{1-n}(m(2 S+1))\right]=0. \tag{8}
$$

![](./images/867765431954309747_8.jpg)

FIG. 8. Temperature-dependent spin-crossover ranges with fp18 based on the different models. (a) and (b) are ideal and non-ideal mixing models with $G^{mag}$; (c) and (d) are ideal and non-ideal mixing models without $G^{mag}$. The black line indicates the geotherm [31, 32].

We numerically solve Eqn. (8) for $n_{non-ideal}$ by first fitting $H_{ex}(n)$ with polynomial functions at each pressure and temperature, as shown in Fig. S2. The obtained $n_{non-ideal}(P, T)$ are plotted as a function of pressure and temperature in Fig. 8.

We now analyze how the magnetic entropy contribution and non-ideal mixing affect the temperature dependence of the HS-LS spin-crossover pressures in Fig. 8. Comparing the results from ideal and non-ideal mixing models (Fig. 8 (a) vs. (b), or (c) vs. (d)), the HS-LS mixing range is much broader in the non-ideal mixing models. At room temperature, the crossover pressure range is $\sim 5 \mathrm{GPa}$ in the ideal mixing model, while it is $\sim 30 \mathrm{GPa}$ in the non-ideal mixing model. This MS pressure range broadens further at higher temperatures. In principle, the non-ideal mixing model should be closer to the real situation than the ideal mixing model. The wide crossover range agrees better with the experimental data [7]. By comparing Fig. 8 (a) and (c) (or (b) and (d)), we find $G^{mag}$ significantly increases the Clapeyron slope of the spin crossover range. The slope of the phase boundary in Fig. 8(d) is more similar to the previous experimental data from Ref. [7] than others. This might occur because the current $G^{mag}$ is an approximate analytical estimate of the largest possible contribution of the magnetic entropy. In reality, the local spin magnetic moment at high temperatures should not be as large as $S=2$ for the HS state. Therefore, this magnetic entropic effect is likely overestimated. Taking these factors into account, Fig. 8(d) might represent the most realistic situation for the HS-LS spin cross in fp18. In Fig. 8(d), the spin crossover starts at $\sim 45$ GPa. High temperatures do not significantly affect the HS fraction at $\sim 45$ GPa, which agrees with the experimental data [7]. We include the mantle geotherm for a pyrolytic composition [31] in Figs. 8 (d). The spin-crossover starts at $\sim 45$ GPa, 2100 K and ends at $\sim 115$ GPa, 2400 K along the geotherm. These results indicate the MS state should predominate in fp in most of the lower mantle. fp near the core-mantle boundary (CMB) should be mainly in the LS state. We note that thermal electronic excitation effects described using the Mermin functional do not significantly affect the phase boundary, as shown in Supplementary Fig. S4. This is expected as both HS and LS are insulators.

## VI. SUMMARY

In summary, we revisited the HS-LS crossover in fp by performing LDA+$U_{sc}$ calculations. The Hubbard parameters $U$ are determined self-consistently ($U_{sc}$) using density functional perturbation theory (DFPT). The $U_{sc}$ parameter depends on pressure, spin state, electronic and atomic configuration, etc., and varies by 1-2 eV. The AFM configuration is found to be the ground state at low temperatures, consistent with experiments. The energy difference between FM and AFM configurations is less than $10 \mathrm{meV} /$ atom at $\mathrm{T}=0 \mathrm{~K}$, and magnetic ordering has a relatively minor impact on the spin crossover pressure in static calculations for $x_{F e}=0.1875$. Phonon spectra are computed for both HS and LS states. No imaginary frequencies are found in any case from 0 GPa to 120 GPa, confirming phonon stability in fp in the entire pressure range of the Earth's mantle. Quasiharmonic free energy calculations offer ab initio compression curves for HS and LS states in good agreement with experimental data at room temperature. The HS-LS phase diagram is obtained by including all finite-temperature effects, i.e., vibrational, magnetic, electronic, and non-ideal HS-LS mixing contributions. The non-ideal HS-

LS solid-solution mixing model gives a crossover start-
ing at $\sim45$ GPa at room temperature and is consider-
ably broader than previous calculations. The magnetic
entropy is found to affect the Clapeyron slope of the
HS-LS crossover significantly. Considering these effects,
the mixed spin state is predicted to predominate the fp
throughout most of the lower mantle.

## ACKNOWLEDGMENTS

This work was supported primarily by National Science
Foundation awards EAR-1918126 and EAR-1918134. We
acknowledge partial support from the U.S. Department of
Energy Grant DE-SC0019759. We also acknowledge the
computer resources from the Extreme Science and Engi-
neering Discovery Environment (XSEDE), which is sup-
ported by the National Science Foundation grant number
ACI-1548562.

[1] Wentzcovitch R M, Yu Y G and Wu Z 2010 Thermody-
namic properties and phase relations in mantle minerals
investigated by first principles quasiharmonic theory Rev.
Mineral. Geochemistry 71 59–98

[2] Tsuchiya T, Wentzcovitch R M, da Silva C R S and de
Gironcoli S 2006 Spin Transition in Magnesiowüstite in
Earth’s Lower Mantle Phys. Rev. Lett. 96 198501

[3] Wu Z, Justo J F, da Silva C R S, de Gironcoli S
and Wentzcovitch R M 2009 Anomalous thermodynamic
properties in ferropericlase throughout its spin crossover
Phys. Rev. B 80 014409

[4] Wentzcovitch R M, Justo J F, Wu Z, da Silva C R S, Yuen
D A and Kohlstedt D 2009 Anomalous compressibility of
ferropericlase throughout the iron spin cross-over Proc.
Natl. Acad. Sci. 106 8447–52

[5] Wu Z and Wentzcovitch R M 2014 Spin crossover in fer-
ropericlase and velocity heterogeneities in the lower man-
tle Proc. Natl. Acad. Sci. 111 10468–72

[6] Badro J, Fiquet G, Guyot F, Rueff J P, Struzhkin V
V., Vankó G and Monaco G 2003 Iron partitioning in
Earth’s mantle: Toward a deep lower mantle discontinu-
ity Science 300 789–91

[7] Lin J-F, Vanko G, Jacobsen S D, Iota V, Struzhkin V
V., Prakapenka V B, Kuznetsov A and Yoo C-S 2007
Spin Transition Zone in Earth’s Lower Mantle Science
317 1740–3

[8] Lin J F, Struzhkin V V., Jacobsen S D, Hu M Y, Chow
P, Kung J, Liu H, Mao H K and Hemley R J 2005 Spin
transition of iron in magnesiowüstite in the Earth’s lower
mantle Nature 436 377–80

[9] Fei Y, Zhang L, Corgne A, Watson H, Ricolleau A, Meng
Y and Prakapenka V 2007 Spin transition and equations
of state of (Mg, Fe)O solid solutions Geophys. Res. Lett.
34 1–5

[10] Lyubutin I S, Struzhkin V V., Mironovich A A, Gavriliuk
A G, Naumov P G, Lin J F, Ovchinnikov S G, Sinogeikin
S, Chow P, Xiao Y and Hemley R J 2013 Quantum crit-
ical point and spin fluctuations in lower-mantle ferroper-
iclase Proc. Natl. Acad. Sci. U. S. A. 110 7142–7

[11] Mao Z, Lin J F, Liu J and Prakapenka V B 2011 Thermal
equation of state of lower-mantle ferropericlase across the
spin crossover Geophys. Res. Lett. 38 2–5

[12] Cococcioni M and de Gironcoli S 2005 Linear response
approach to the calculation of the effective interaction pa-
rameters in the LDA+U method Phys. Rev. B 71 035105

[13] Kulik H J, Cococcioni M, Scherlis D A and Marzari
N 2006 Density Functional Theory in Transition-Metal
Chemistry: A Self-Consistent Hubbard U Approach
Phys. Rev. Lett. 97 103001

[14] Hsu H, Umemoto K, Wu Z and Wentzcovitch R M 2010
Spin-state crossover of iron in lower-mantle minerals: Re-
sults of DFT+U investigations Rev. Mineral. Geochem-
istry 71 169–99

[15] Cococcioni M and Marzari N 2019 Energetics and cath-
ode voltages of LiMPO4 olivines (M=Fe , Mn) from ex-
tended Hubbard functionals Phys. Rev. Mater. 3 033801

[16] Floris A, Timrov I, Himmetoglu B, Marzari N, De Giron-
coli S and Cococcioni M 2020 Hubbard-corrected density
functional perturbation theory with ultrasoft pseudopo-
tentials Phys. Rev. B 101 064305

[17] Sun Y, Cococcioni M and Wentzcovitch R M 2020
LDA+U calculations of phase relations in FeO Phys. Rev.
Mater. 4 063605

[18] Timrov I, Marzari N and Cococcioni M 2018 Hubbard
parameters from density-functional perturbation theory
Phys. Rev. B 98 085127

[19] Dudarev S L, Botton G A, Savrasov S Y, Humphreys
C J and Sutton A P 1998 Electron-energy-loss spectra
and the structural stability of nickel oxide: An LSDA+U
study Phys. Rev. B 57 1505–9

[20] Giannozzi P, Baroni S, Bonini N, Calandra M, Car R,
Cavazzoni C, Ceresoli D, Chiarotti G L, Cococcioni M,
Dabo I, Dal Corso A, De Gironcoli S, Fabris S, Fratesi
G, Gebauer R, Gerstmann U, Gougoussis C, Kokalj A,
Lazzeri M, Martin-Samos L, Marzari N, Mauri F, Maz-
zarello R, Paolini S, Pasquarello A, Paulatto L, Sbraccia
C, Scandolo S, Sclauzero G, Seitsonen A P, Smogunov
A, Umari P and Wentzcovitch R M 2009 QUANTUM
ESPRESSO: a modular and open-source software project
for quantum simulations of materials J. Phys. Condens.
Matter 21 395502

[21] Giannozzi P, Andreussi O, Brumme T, Bunau O, Buon-
giorno Nardelli M, Calandra M, Car R, Cavazzoni C,
Ceresoli D, Cococcioni M, Colonna N, Carnimeo I, Dal
Corso A, De Gironcoli S, Delugas P, Distasio R A, Fer-
retti A, Floris A, Fratesi G, Fugallo G, Gebauer R, Ger-
stmann U, Giustino F, Gorni T, Jia J, Kawamura M,
Ko H Y, Kokalj A, Kücükbenli E, Lazzeri M, Marsili M,
Marzari N, Mauri F, Nguyen N L, Nguyen H V., Otero-
De-La-Roza A, Paulatto L, Poncé S, Rocca D, Sabatini

R, Santra B, Schlipf M, Seitsonen A P, Smogunov A, Timrov I, Thonhauser T, Umari P, Vast N, Wu X and Ba-roni S 2017 Advanced capabilities for materials modelling with Quantum ESPRESSO J. Phys. Condens. Matter 29 465901

[22] Dal Corso A 2014 Pseudopotentials periodic table: From H to Pu Comput. Mater. Sci. 95 337-50

[23] Anisimov V I, Zaanen J and Andersen O K 1991 Band theory and Mott insulators: Hubbard U instead of Stoner I Phys. Rev. B 44 943-54

[24] Mermin N D 1965 Thermal properties of the inhomoge-neous electron gas Phys. Rev. 137 A1441

[25] Wentzcovitch R M, Martins J L and Allen P B 1992 Energy versus free-energy conservation in first-principles molecular dynamics Phys. Rev. B 45 11372-4

[26] Zhuang J, Wang H, Zhang Q and Wentzcovitch R M 2021 Thermodynamic properties of $\epsilon$-Fe with thermal electronic excitation effects on vibrational spectra Phys. Rev. B 103 144102

[27] Togo A and Tanaka I 2015 First principles phonon cal-culations in materials science Scr. Mater. 108 1-5

[28] Wallace D C 1972 Thermodynamics of Crystals (Mineola:Dover)

[29] Qin T, Zhang Q, Wentzcovitch R M and Umemoto K 2019 qha: A Python package for quasiharmonic free en-ergy calculation for multi-configuration systems Comput. Phys. Commun. 237 199-207

[30] Marcondes M L, Zheng F and Wentzcovitch R M 2020 Phonon dispersions throughout the iron spin crossover in ferropericlase Phys. Rev. B 102 104112

[31] Valencia-Cardona J J, Shukla G, Wu Z, Houser C, Yuen D A and Wentzcovitch R M 2017 Influence of the iron spin crossover in ferropericlase on the lower mantle geotherm Geophys. Res. Lett. 44 4863-71

[32] Stacey F D and Davis P M 2008 Physics of the Earth vol 193 (Cambridge: Cambridge University Press)