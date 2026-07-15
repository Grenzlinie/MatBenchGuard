# The origin of glass-like phonon dynamics in binary Si and Ge clathrates-I

Amrita Bhattacharya

Intermetallic guest filled host clathrate cages have been identified as promising materials for thermoelectric applications owing to their phonon glass electron crystal (PGEC) behavior. The vibrational dynamics of empty and guest filled stable host (Si and Ge) clathrates is explored using density functional theory based calculations. The role of the guests as well as the host in the vibrational dynamics of these clathrates is analysed. The empty clathrate cages are found to be harmonic crystals. However, filling of their cages with guest results in deviation from harmonicity, which is either due to imbalance of electronic charge (in Si clathrates) or due to softening of the framework bonds (in Ge clathrates). The increase in anharmonicity plays a crucial role in changing their scattering lifetimes and hence the lattice thermal conductivity. The lattice thermal conductivity of these compounds is calculated by modeling their phonon scattering lifetimes from the Grüneisen parameter, zone-boundary frequency, and group velocity of the acoustic phonon modes using the Debye Callaway formalism, which is found to be in good agreement with experiments.

## 1 Introduction

Thermoelectrics are promising alternatives for addressing the issue of the energy crisis.¹ The thermoelectric efficiency is directed by the dimensionless figure of merit: $ZT = S\sigma^{2}T/\kappa$, which depends on the intrinsic properties of the compound viz. the Seebeck coefficient $S$, the electrical conductivity $\sigma$, and the thermal conductivity $\kappa$. Optimizing $ZT$ is a non trivial task, which can be achieved either by increasing $S/\sigma$ or by reducing $\kappa$. Enhancing $S$ can be popularly achieved *via* quantum confinement,² electron energy filtering³ *etc.*, while a low lattice thermal conductivity can be obtained by increasing the grain boundaries *via* nanostructuring⁴⁻⁶ *etc*. However, such an approach can obviously only be successful if the core material itself has high electrical conductivity as well as low thermal conductivity.⁷

Desirable high electronic conductivity (crystal like) as well as low lattice thermal conductivity (glass-like) are the intrinsic properties of Phonon Glass Electron Crystal (PGEC),⁸,⁹ which make them ideal for thermoelectric applications.¹⁰,¹¹ Clathrates are cage-like structures of hosts, which have large voids in the crystal framework that encapsulate guest atoms.¹² More than two decades ago, Nolas *et al.* showed that the lattice thermal conductivity ($\kappa_{\text{l}}$) of the guest filled clathrates resembles glass-like behavior and suggested that the rattling motion of the guests is responsible for the lowering of the $\kappa_{\text{l}}$.⁹,¹³,¹⁴ Subsequent theoretical studies supported this hypothesis.¹⁵⁻¹⁷ Several other reports concluded that the mutual coupling of the motion of the guest and the host lowers the $\kappa_{\text{l}}$.¹⁸,¹⁹ Nevertheless, the phonon dynamics of the guest filled clathrates have remained puzzling.²⁰⁻²⁴ Many intricate studies are still being performed to understand the underlying scattering mechanism in more complex systems.²⁵,²⁶

In the context of thermoelectrics, typically investigated ones have a host framework comprising group-IV elements (Si, Ge, . . .) encapsulating alkali (Na, K, Rb, . . .) or alkaline earth metal (Sr, Ba, . . .) atoms as guests.¹⁰ The empty semiconducting clathrate framework, which is metastable with respect to the corresponding diamond phase, comprises 46 tetrahedrally bonded host atoms [$Si_{46}$ and $Ge_{46}$ (spacegroup $Pm\overline{3}n$)]. Out of these 46 host positions three are symmetrically unique; six $6c$-, sixteen $16i$-, and twenty-four $24k$-sites in Wyckoff notation.¹⁰ The large voids in the host framework encapsulate up to eight guest atoms in two symmetry-unique sites; two in the centers of the dodecahedral cages ($2a$ site) and six in the centers of the tetrakaidecahedral cages ($6d$ site). Filling of the cages with electropositive metal guests leads to stabilization of the metastable framework *via* electron transfer from the guests. In addition, these guests serve as scattering centres to the host phonons, thereby providing a tool to tune their $\kappa_{\text{l}}$. However, the addition of guests may also induce drastic structural changes, such as the spontaneous creation of vacancies in the host framework, which further complicates the case. For instance, in K and Ba filled Ge clathrates, the most favorable phases, $\text{K}_{8}\text{Ge}_{44}\square_{2}$²⁷,²⁸ and $\text{Ba}_{8}\text{Ge}_{43}\square_{3}$,²⁹ have two and three vacancies in their framework respectively. Curiously, the framework of

---
Department of Metallurgical Engineering and Materials Science, Indian Institute of Technology Bombay, Maharashtra, 400076, India. E-mail: b_amrita@iitb.ac.in

the isoelectronic $Si_{46}$ clathrate remains intact upon filling with the same K and Ba guests resulting in compositions $K_8Si_{46}^{30-32}$ and $Ba_8Si_{46}.^{33}$ Our recent studies confirm this experimental scenario and shed light on the underlying mechanisms. $^{34,35}$

Binary clathrates are ideal cases for analysing the effect of guest rattlers as well as host lattice changes in their phonon dynamics. In this work, first principles density functional theory based calculations are performed to explore the vibrational dynamics of filled stable Si and Ge clathrates. The guest filled Si clathrates are devoid of vacancies, but filling results in spontaneous creation of vacancies in the framework of Ge clathrates. The Grüneisen parameter, Debye temperature, and phonon group velocity of the transverse and longitudinal acoustic phonon modes of empty and filled stable Si and Ge clathrate compositions are calculated. Our calculations show that the empty clathrates are harmonic crystals, which become anharmonic with filling of guests. The anharmonicity in Si clathrates can be explained from the increase in surplus unbalanced electron count due to the charge transfer from the electropositive guest. While increase in anharmonicity in filled Ge clathrate is due to the formation of framework vacancies that softens the framework albeit balancing the electron count (either completely or partially). The lattice thermal conductivity $\kappa_1$ of these binary clathrates is calculated by modeling the phonon lifetimes using the Debye Callaway formalism $^{36}$ with Asen-Palmer modification for solid, $^{37}$ which is found to be in good agreement with experiments.

## 2 Computational details and methodology

Density functional theory (DFT) $^{38,39}$ calculations are performed using FHI-aims, $^{40}$ which is an all electron, full potential electronic structure code that uses numeric atom-centered basis sets. The exchange and correlation parts are treated using the generalized gradient approximation (GGA) based functional of Perdew Bruke Ernzerhof parametrized for solids (PBEsol) $^{41}$ (see ref. 34 for validation of the exchange correlation functional). All numerical settings are chosen so as to ensure a convergence in energy differences to better than $10^{-4}$ eV. For all the investigated compositions and geometries, both the atomic positions and lattice vectors are fully relaxed using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm $^{42}$ until all forces (including the ones stemming from the stress) are less than $10^{-3}$ eV $\mathring{A}^{-1}$. Converged reciprocal space grid $8 \times 8 \times 8$ per unit cell and "tight" basis sets are used.

The phonon band structure is calculated using the harmonic approximation implemented in the phonopy code. $^{43}$ The phonon group velocity $v$ ($v = d\omega/dK$) and mode resolved phonon group velocity $v_i$ ($v_i = d\omega_i/dK$) are obtained by differentiating the phonon modes using a forward difference method. Grüneisen parameter $\gamma$ ($\gamma = -\frac{1}{\omega}\frac{d\omega}{dV}$) and mode resolved Grüneisen parameter $\gamma_i$ ($\gamma_i = -\frac{1}{\omega_i}\frac{d\omega_i}{dV}$) are extracted from the quasi harmonic phonon band dispersions (using volume strain of $\pm 5\%$).

The Grüneisen parameter $(\bar{\gamma})$ at a given temperature is calculated from the number average of $\gamma$ within the corresponding frequency ($\omega = \frac{K_B T}{\hbar}$) range of $\pm 2\%$.

The normal phonon scattering lifetime $\tau_N$ corresponding to the transverse acoustic (TA) and longitudinal acoustic (LA) modes is written as a function of $x = \frac{\hbar\omega}{K_B T}$ as

$$
\frac{1}{\tau_{\mathrm{N}}^{\mathrm{TA} / \mathrm{TA}^{\prime}}(x)}=\frac{\gamma_{\mathrm{TA} / \mathrm{TA}^{\prime}}{ }^{2} V}{M v_{\mathrm{TA} / \mathrm{TA}^{\prime}}{ }^{5}}\left(\frac{K_{\mathrm{B}}{ }^{5}}{\hbar^{4}}\right) x T^{5} \tag{1}
$$

$$
\frac{1}{\tau_{\mathrm{N}}^{\mathrm{LA}}(x)}=\frac{\gamma_{\mathrm{LA}}{ }^{2} V}{M v_{\mathrm{LA}}{ }^{5}}\left(\frac{K_{\mathrm{B}}{ }^{5}}{\hbar^{4}}\right) x^{2} T^{5} \tag{2}
$$

where, $M$ and $V$ are the average mass of an atom in the crystal and crystal volume respectively.

The Umklapp phonon scattering lifetime $\tau_U^i$ corresponding to the acoustic mode i is written as

$$
\frac{1}{\tau_{\mathrm{U}}^{\mathrm{i}}(x)}=\frac{\hbar \gamma^{2}}{M v_{\mathrm{i}}^{2} \theta_{\mathrm{i}}}\left(\frac{K_{\mathrm{B}}}{\hbar}\right)^{2} x^{2} T^{3} \mathrm{e}^{-\theta_{\mathrm{i}} / 3 T}. \tag{3}
$$

where, $\gamma$ is the number average of the acoustic modes $\gamma = \frac{\sum \gamma_i}{\sum n_i}$ for i = TA, TA', and LA. $\theta_i$ is the Debye temperature corresponding to the acoustic phonon mode i.

The Asen-Palmer modified version $^{37}$ of Debye Callaway theory $^{36}$ is used to calculate the lattice thermal conductivity $\kappa_1^i$ of the empty and filled clathrate phases from the scattering lifetimes of the acoustic phonon modes i = TA, TA', LA, obtained using eqn (1)-(3). The $\kappa_1^i$ is calculated using

$$
\kappa_{\mathrm{l}}^{\mathrm{i}}=\frac{1}{3} C_{\mathrm{i}} T^{3}\left\{\int_{0}^{\theta_{\mathrm{i}} / T} \frac{\tau_{\mathrm{c}}^{\mathrm{i}} x^{4} e^{x}}{\left(e^{x}-1\right)^{2}} \mathrm{~d} x+\frac{\left[\int_{0}^{\theta_{\mathrm{i}} / T} \frac{\tau_{\mathrm{c}}^{\mathrm{i}} x^{4} e^{x}}{\tau_{\mathrm{N}}^{\mathrm{i}}\left(e^{x}-1\right)^{2}}\right]^{2}}{\int_{0}^{\theta_{\mathrm{i}} / T} \frac{\tau_{\mathrm{c}}^{\mathrm{i}} x^{4} e^{x}}{\tau_{\mathrm{U}}^{\mathrm{i}} \tau_{\mathrm{N}}^{\mathrm{i}}\left(e^{x}-1\right)^{2}}}\right\} \tag{4}
$$

$C_{\mathrm{i}}=\frac{K_{\mathrm{B}}^{4}}{2 \pi^{2} \hbar^{3} v_{\mathrm{i}}}$ depends on the group velocity $v_i$ of the concerned mode and $\tau_{\mathrm{c}}^{\mathrm{i}}=\frac{\tau_{\mathrm{U}}^{\mathrm{i}} \tau_{\mathrm{N}}^{\mathrm{i}}}{\tau_{\mathrm{U}}^{\mathrm{i}}+\tau_{\mathrm{N}}^{\mathrm{i}}}$ is the relaxation time.

The total lattice thermal conductivity $\kappa_1$ is the sum of the lattice thermal conductivity due to the acoustic phonon branches $\kappa_1 = \kappa_1^{\mathrm{LA}} + \kappa_1^{\mathrm{TA}'} + \kappa_1^{\mathrm{TA}}$.

## 3 Results and discussions

The formation energy of filled type-I Si and Ge clathrates, as calculated by including the contributions stemming from geometric relaxation, electronic saturation as well as vibrational and configurational entropy, is discussed in our previous work. $^{35}$ The most favourable phase of Na, K and Ba filled Si clathrates has an intact framework, while K and Ba filled Ge clathrates have two and three vacancies in their framework respectively. So, the calculations are performed on the most stable phase of Na/K/Ba filled Si/Ge clathrates at 300 K, which are $Na_8Si_{46}$, $K_8Si_{46}$, $Ba_8Si_{46}$, $K_8Ge_{44}\square_2$, and $Ba_8Ge_{43}\square_3$. Fig. 1 and 2 show the harmonic

![](./images/812718215804223488_1.jpg)

Fig. 1 The phonon band structure of (a) empty, (b) Na, (c) K, and (d) Ba filled Si clathrates.

phonon band structure of the pristine and filled stable Si and Ge clathrate compositions respectively. The presence of flat band or localized mode in the phonon band structure signifies zero or low group velocity and therefore, implies the negligible contri- bution of that specific mode towards the lattice thermal con- ductivity $\kappa_{1}$ . Prior to the inclusion of the guests, the localized modes are observed in the frequency regions of $140-180 ~cm^{-1}$  and $450-480 ~cm^{-1}$ of the phonon spectrum of $Si_{46}$ [cf. Fig. 1(a)]. Filling with guests introduces localized rattling modes (shown in the box in Fig. 1(b)-(d)), which leads to avoided crossing of the acoustic modes and they reach the Brillouin zone boundary with a reduced frequency. Interestingly, it is unusual that the rattling mode of $Na$ is introduced at a lower frequency in comparison to those of $K$ , in spite of its lower atomic mass. This lowers the Debye temperature of the acoustic modes in the case of the former with respect to the latter. Filling also leads to the low- ering in the phonon spectrum width by up to $\sim 30 \%$ (if the presence of highly localized modes at $\sim 450 ~cm^{-1}$ is ignored)[cf. Fig. 1(b)-(d)].

Localized modes are observed in the regions of $70-100 ~cm^{-1}$  and $250-275 ~cm^{-1}$ in the phonon spectrum of $Ge_{46}$ [cf. Fig. 2(a)]. With the inclusion of guest rattlers [contribution shown in black in Fig. 2(b) and (c)] the number density of the localized modes increases through out the phonon dispersion. Due to the presence of the framework vacancies as well as the guest fillers, the entirephonon spectrum of $K_{8} Ge_{44} \square_{2}$ and $Ba_{8} Ge_{43} \square_{3}$ , beyond $50 ~cm^{-1}$  and $20 ~cm^{-1}$ respectively, is found to consist of only localized modes or flat bands [cf. Fig. 2(b) and (c)]. Therefore, it can be concluded that the highest contribution to the $\kappa_{1}$ comes from the acoustic modes in the filled Si/Ge clathrates. The phonon spectrum width is found to be reduced by up to $10 \%$ upon filling in the Ge clathrates. Thus, the three main differences observed upon filling of the empty clathrates are (a) occurrence of a large number of flat bands through out the spectrum, (b) lowering in the energy intensity of the acoustic phonon modes at which they reach the Brillouin zone boundary due to avoided crossings, and(c) lowering of the phonon spectral width.

![](./images/812718215804223488_2.jpg)

Fig. 2 The phonon band structure of (a) empty, (b) K filled $(K_{8} Ge_{44} \square_{2})$  and (c) Ba filled $(Ba_{8} Ge_{43} \square_{3})$ Ge clathrates.

The Debye temperature of the TA $(\theta_{TA})$ and LA $(\theta_{LA})$ modes is calculated from the average of the acoustic phonon frequencies $\omega_{ max }$ at which the $\Gamma$ originated phonon modes get terminated at the Brillouin zone boundaries in different directions $(\theta=\hbar \omega_{ max } / K_{B})$ . The average Debye temperature $\theta_{D}$ is calculatedfrom $v_{s} \cdot \dagger$ As expected from the higher mass of phonons, the $\theta_{s}$  of $Ge_{46}$ is found to be $\sim 40 \%$ lower than $Si_{46}$ . The presence of the localized flat bands in $K, Na$ and $Ba$ filled $Si_{46}$ [cf. Fig. 1(b)-(d)], leads to lowering of mode $\theta_{s}$ . Owing to the exceptionally low rattling modes of $Na$ in $Na_{8} Si_{46}$ , the mode $\theta_{s}$ are found to be even

$$\dagger \theta_{\mathrm{D}}=\frac{h}{K_{\mathrm{B}}} v_{\mathrm{s}}\left(\frac{3 N}{4 \pi V}\right)^{1 / 3},$$

where $N$ and $V$ are the number of atoms in the unit cell and the volume of the unit cell respectively.

<table>
<caption>Table 1 The average Grüneisen parameter $\bar{\gamma}|_{300}$ at 300 K, average Grüneisen parameter of the transverse acoustic (TA) and longitudinal acoustic (LA) branches $\gamma_{TA/LA}$, average phonon group velocity of the LA and TA branches $v_{TA/LA}$ (km s⁻¹), and the Debye temperature of the TA and LA branches $\theta_{TA/LA}$ (K). The average of the $\theta$ and $\gamma$ of the TA and TA$'$ modes is provided</caption>
<thead>
<tr>
<th>System</th>
<th>$\bar{\gamma}|_{300}$</th>
<th>$\gamma_{TA}$</th>
<th>$\gamma_{LA}$</th>
<th>$v_{TA}$</th>
<th>$v_{LA}$</th>
<th>$v_s$</th>
<th>$\theta_{TA}$</th>
<th>$\theta_{LA}$</th>
<th>$\theta_D$</th>
<th>$\kappa_1$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si₄₆</td>
<td>0.95</td>
<td>0.5</td>
<td>0.9</td>
<td>4.5</td>
<td>7.8</td>
<td>5.0</td>
<td>125</td>
<td>145</td>
<td>522</td>
<td>16.0</td>
</tr>
<tr>
<td>Na₈Si₄₆</td>
<td>1.10</td>
<td>0.4</td>
<td>1.2</td>
<td>4.4</td>
<td>7.3</td>
<td>4.8</td>
<td>92</td>
<td>94</td>
<td>535</td>
<td>2.7</td>
</tr>
<tr>
<td>K₈Si₄₆</td>
<td>1.10</td>
<td>0.5</td>
<td>1.3</td>
<td>4.0</td>
<td>6.4</td>
<td>4.4</td>
<td>100</td>
<td>102</td>
<td>481</td>
<td>5.2</td>
</tr>
<tr>
<td>Ba₈Si₄₆</td>
<td>1.50</td>
<td>1.1</td>
<td>1.6</td>
<td>3.0</td>
<td>5.2</td>
<td>3.3</td>
<td>65</td>
<td>65</td>
<td>360</td>
<td>1.0</td>
</tr>
<tr>
<td>Ge₄₆</td>
<td>1.00</td>
<td>0.2</td>
<td>1.1</td>
<td>2.7</td>
<td>4.6</td>
<td>3.0</td>
<td>75</td>
<td>87</td>
<td>300</td>
<td>14.5</td>
</tr>
<tr>
<td>K₈Ge₄₄□₂</td>
<td>1.20</td>
<td>0.6</td>
<td>1.6</td>
<td>2.3</td>
<td>3.7</td>
<td>2.5</td>
<td>51</td>
<td>57</td>
<td>264</td>
<td>1.1</td>
</tr>
<tr>
<td>Ba₈Ge₄₃□₃</td>
<td>1.60</td>
<td>—</td>
<td>—</td>
<td>1.5</td>
<td>3.0</td>
<td>1.6</td>
<td>20</td>
<td>25</td>
<td>185</td>
<td>—</td>
</tr>
</tbody>
</table>

lower than those in K₈Si₄₆ (in agreement with⁴⁴). Inclusion of the guests leads to reduction in $\theta$ by up to 40% in Si clathrates. In the filled Ge₄₆, the coupling of the flat bands with the vacancies results in a very wide spread broad region of flat bands throughout the phonon spectrum. In K₈Ge₄₄□₂ and Ba₈Ge₄₃□₃, the flat bands are found in the ~50–100 cm⁻¹ and ~20–100 cm⁻¹ regions of the phonon spectrum respectively [cf. Fig. 2(b) and (c)]. Thus, filling of Ge₄₆ results in up to 70% lowering of $\theta$. This lowering of $\theta$ is ~30% higher than the lowering due to filling in Si₄₆ and may be attributed to the presence of the framework vacancies in the Ge host, which leads to softening of the phonon modes.

The average phonon group velocity of the TA and LA branches $v_{TA/LA}$ is enlisted in Table 1. They are calculated by averaging the maximum group velocity attained by the phonon modes at the $\Gamma$ point. The average velocity $v_s$ of phonons in the empty and filled clathrate is calculated from their $v_{TA}$ and $v_{LA}$.$\ddagger$ The phonon group velocity as a function of frequency $\omega$ (Fig. 3) and the corresponding mode resolved dispersion throughout the high symmetry path in the Brillouin zone are presented in Fig. 4. The $v_{TA}$ and $v_{LA}$ are found to be dependent on the type of guest filler as well as the host. The average phonon group velocity in Ge₄₆ is found to be ~40% lower than the average phonon group velocity in Si₄₆. This is partially attributed to the higher mass of the host phonons, which reduces the vibrational frequencies in Ge₄₆. The filling of the cages in Si₄₆ reduces the phonon group velocity by up to 50% (cf. Table 1). This is attributed to the localized flat bands induced by the fillers (as shown in Fig. 1 and 2). The filling of guests as well as the structural changes in the host framework (i.e. due to formation of vacancies) reduce the phonon group velocity by up to 50% in Ge₄₆, similar to Si₄₆.

The scattering lifetime $\tau$ is inversely proportional to the square of the Grüneisen parameter $\gamma^2$ (see eqn (2)–(3)). The Grüneisen parameter $\gamma$ is calculated from the change in phonon dispersion by subjecting the lattice to compression and expansion, which is analogous to the effect of adiabatic cooling or heating of the lattice. Therefore, $\gamma$ provides the estimation of anharmonicity in the compound. For instance, in a compound with harmonic oscillator potential the $\gamma$ should be equal to unity. Thus, the higher the deviation of $\gamma$ from unity, the larger the deviation from the harmonic oscillator approximation. The average Grüneisen parameter at 300 K ($\bar{\gamma}|_{300}$) and the average Grüneisen parameter of the TA and LA branches ($\gamma_{TA/LA}$) are enlisted in Table 1. The $\gamma$ and their mode resolved dispersions $\gamma_i$ for all the acoustic modes are plotted in Fig. 3 and 4 respectively. The $\bar{\gamma}|_{300}$ is found to be close to unity for the empty Si and Ge clathrates. $\bar{\gamma}|_{300}$ is found to be mostly dependent on the type of guest filler and increase by up to 60% upon filling of the Si and Ge empty host cages. Interestingly, $\bar{\gamma}|_{300}$ is found to vary by only ~10% with the change of the host (including the drastic structural changes in the host lattice). The increase in anharmonicity in Si clathrates is due to increase in surplus unbalanced electronic charge in the framework due to transfer of electrons from the electropositive guests. Thus, the $\bar{\gamma}|_{300}$ is found to be close for monovalent Na and K guest filled clathrates, while it is found to be much higher for divalent Ba filled ones. On the other hand, in Ge clathrates the $\bar{\gamma}|_{300}$ also increases with filling due to the

![](./images/812718215804223488_3.jpg)

Fig. 3 Phonon group velocity $v_g$ and Grüneisen parameter $\gamma$ plotted as a function of frequency $\omega$ for the (a) Si and (b) Ge clathrates.

$\ddagger$ The average velocity $v_s$ of phonons is calculated using the expression
$$
v_s = \left[ \frac{1}{3} \left( \frac{1}{v_{LA}^3} + \frac{2}{v_{TA}^3} \right) \right]^{-\frac{1}{3}}.
$$

![](./images/812718215804223488_4.jpg)

Fig. 4 The mode resolved group velocity $v_{g}$ and Grüneisen parameter $\gamma_{i}$ plotted in the high symmetry path of the Brillouin zone for empty and filled Si (a)-(h) and Ge (i)-(k) clathrates.

spontaneous creation of vacancies in the framework which softens the framework although the electronic charge is balanced completely and partially in $K_{8}Ge_{44}\square_{2}$ and $Ba_{8}Ge_{43}\square_{3}$. In most cases, the $\gamma_{i}$ of the LA mode is found to be higher than that of the TA mode. The $\gamma_{LA}$ is found to be close to $\bar{\gamma}|_{300}$ suggesting that the LA mode has higher contribution towards the anharmonicity in all cases. However, in $Ba_{8}Ge_{43}\square_{3}$, the $\gamma$ corresponding to the LA, TA, and TA' modes diverge.

Using the parameters enlisted in Table 1 in eqn (4), the lattice thermal conductivity $\kappa_{1}$ of the empty and filled clathrate compositions is calculated. The corresponding value at 300 K $\kappa_{1}|_{300}$ is enlisted in Table 1. $\kappa_{1}$ is plotted as a function of temperature $T$ in Fig. 5. Pristine clathrates exhibit classical behavior, whereby the $\kappa_{1}$ is found to decrease as an inverse function of $T$. Filling of guests leads to lowering of $\kappa_{1}$ in both $Si_{46}$ and $Ge_{46}$ clathrates, which is expected from their phonon spectrum. Owing to the low mode Debye temperature in $Na_{8}Si_{46}$, its $\kappa_{1}$ is found to be as low as $2.7\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ at 300 K, which is

![](./images/812718215804223488_5.jpg)

Fig. 5 The lattice thermal conductivity $\kappa_{1}$ of empty and filled stable clathrates plotted as a function of temperature $T$ as calculated using the Debye Callaway formalism.

roughly in agreement with the experimental measurement performed by Nolas et al. $^{44,45}$ The $\kappa_{1}$ of $K_{8}Si_{46}$ is found to be $\sim 5.2\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ at 300 K. The $\kappa_{1}$ of $Na_{8}Si_{46}$ is found to be lower than $K_{8}Si_{46}$, which is primarily due to the low mode Debye temperatures of the acoustic modes caused from avoided crossing due to the presence of a rattling mode of the guests in adition to the increased anharmonicity of the compound due to filling. The $\kappa_{1}$ of $Ba_{8}Si_{46}$ is found to be $\sim 1\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ at 300 K, which is in agreement with the reported $\kappa_{1}$ of type-I silicon based clathrates at room temperature. $^{46}$ The presence of vacancies in the framework of $K_{8}Ge_{44}\square_{2}$ further lowers the $\kappa_{1}$ due to the increase in the scattering centers. The $\kappa_{1}$ of $K_{8}Ge_{44}\square_{2}$ is calculated to be $1.1\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$, which is in agreement with the experimentally reported $\kappa_{1}$ of Beekman et al. of $1.0\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$ at $300\ \text{K}^{27}$ The $\kappa_{1}$ of $Ba_{8}Ge_{43}\square_{3}$ is not calculated using this analytical model due to the diverging tendencies of the acoustic Grüneisen parameter in this specific case.

## 4 Conclusions

The results of first principles based density functional theory calculations are presented to unravel the phonon dynamics of guest filled Si/Ge clathrates. The most stable compositions of Na, K and Ba filled Si clathrates are devoid of vacancies, but filling with K and Ba results in spontaneous creation of two and three vacancies (per unit cell) respectively in the Ge clathrates. The effect of change of guest and host (including the spontaneous structural changes due to the formation of vacancies) is explored on the vibrational dynamics of the empty and filled stable clathrates. The Grüneisen parameter, Debye temperature, and phonon group velocity of the transverse and longitudinal acoustic phonon modes of empty and filled stable clathrate compositions are compared. The empty clathrates are calculated to have a harmonic crystal lattice. With filling of the host cages, the crystal becomes anharmonic. The anharmonicity is found to be strongly dependent on the type of guest fillers. In Si clathrates, the increase in surplus unbalanced electron count due to the charge transfer from electropositive guest leads to increase in anharmonicity. While in Ge clathrates, the formation of framework vacancies softens the bonds and

increases the anharmonicity of the crystal. The increase in anharmonicity plays a major role in the lattice dynamics of these compounds.

## Conflicts of interest
There are no conflicts to declare.

## Acknowledgements
Matthias Scheffler and Christian Carbogno of FHI, Berlin are acknowledged for initiating the project and for many helpful discussions. AB acknowledges the DST Inspire faculty project (DST/INSPIRE/04/2015/000089), IIT B seed grant project (RD/0517-IRCCSH0-043) and SERB ECRA project (ECR/2018/002356) for the financial assistance. The high performance computing facilities (space time and corona) of IIT Bombay are acknowledged for providing the computation hours.

## Notes and references
1 L. E. Bell, *Science*, 2008, **321**, 1457.
2 T. C. Harman, P. J. Taylor, M. P. Walsh and B. E. LaForge, *Science*, 2002, **297**, 2229-2232.
3 J. P. Heremans, C. M. Thrush and D. T. Morelli, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2004, **70**, 115334.
4 K. F. Hsu, S. Loo, F. Guo, W. Chen, J. S. Dyck, C. Uher, T. Hogan, E. K. Polychroniadis and M. G. Kanatzidis, *Science*, 2004, **303**, 818-821.
5 B. Poudel, Q. Hao, Y. Ma, Y. Lan, A. Minnich, B. Yu, X. Yan, D. Wang, A. Muto, D. Vashaee, X. Chen, J. Liu, M. S. Dresselhaus, G. Chen and Z. Ren, *Science*, 2008, **320**, 634-638.
6 N. S. Chauhan, B. Gahtori, B. Sivaiah, S. D. Mahanti, A. Dhar and A. Bhattacharya, *Appl. Phys. Lett.*, 2018, **113**, 013902.
7 M. W. Gaultois and T. D. Sparks, *Appl. Phys. Lett.*, 2014, **104**, 113906.
8 D. T. Morelli and G. P. Meisner, *J. Appl. Phys.*, 1995, **77**, 3777-3781.
9 G. S. Nolas, J. L. Cohn, G. A. Slack and S. B. Schujman, *Appl. Phys. Lett.*, 1998, **73**, 178-180.
10 M. Christensen, S. Johnsen and B. B. Iversen, *Dalton Trans.*, 2010, **39**, 978.
11 X. Yan, M. Ikeda, L. Zhang, E. Bauer, P. Rogl, G. Giester, A. Prokofiev and S. Paschen, *J. Mater. Chem. A*, 2018, **6**, 1727-1735.
12 A. D. McNaught and A. Wilkinson, *IUPAC. Compendium of Chemical Terminology*, Blackwell Scientific Publications, Oxford, 1997.
13 J. L. Cohn, G. S. Nolas, V. Fessatidis, T. H. Metcalf and G. A. Slack, *Phys. Rev. Lett.*, 1999, **82**, 779-782.
14 Y. Gao, X. Zhang, Y. Zhou and M. Hu, *J. Mater. Chem. C*, 2017, **5**, 10578-10588.
15 N. P. Blake, L. Mollnitz, G. Kresse and H. Metiu, *J. Chem. Phys.*, 1999, **111**, 3133-3144.

16 J. Dong, O. F. Sankey, G. K. Ramachandran and P. F. McMillan, *J. Appl. Phys.*, 2000, **87**, 7726-7734.
17 J. Dong, O. F. Sankey and C. W. Myles, *Phys. Rev. Lett.*, 2001, **86**, 2361-2364.
18 M. Christensen, A. B. Sabrahamsen, N. B. Christensen, F. Juranyi, N. H. Andersen, K. Lefmann, J. Andreasson, C. R. H. Bahl and B. B. Iversen, *Nat. Mater.*, 2008, **7**, 811-815.
19 A. Fujiwara, K. Sugimoto, C.-H. Shih, H. Tanaka, J. Tang, Y. Tanabe, J. Xu, S. Heguri, K. Tanigaki and M. Takata, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2012, **85**, 144305.
20 J. S. Tse, T. Iitaka, T. Kume, H. Shimizu, K. Parlinski, H. Fukuoka and S. Yamanaka, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2005, **72**, 155441.
21 K. Suekuni, M. A. Avila, K. Umeo and T. Takabatake, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2007, **75**, 195210.
22 E. N. Nenghabi and C. W. Myles, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **78**, 195202.
23 V. V. Novikov, K. S. Pilipenko, A. V. Matovnikov, N. V. Mitroshenkov, B. I. Kornev, M. S. Likhanov, A. S. Tyablikov and A. V. Shevelkov, *Phys. Chem. Chem. Phys.*, 2017, **19**, 27725-27730.
24 J.-Y. Yang, L. Cheng and M. Hu, *Appl. Phys. Lett.*, 2017, **111**, 242101.
25 T. Tadano and S. Tsuneyuki, *Phys. Rev. Lett.*, 2018, **120**, 105901.
26 M. S. Ikeda, H. Euchner, X. Yan, P. Tomes, A. Prokofiev, L. Prochaska, G. Lientschnig, R. R. Svagera, S. Hartmann, E. Gati, M. Lang and S. Paschen, *Nat. Commun.*, 2019, **10**, 887.
27 M. Beekman and G. S. Nolas, *Int. J. Appl. Ceram. Technol.*, 2007, **4**, 332-338.
28 H. G. von Schnering, J. Llanos, K. Peters, M. Baitinger, Y. Grin and R. Nesper, *Z. Kristallogr. - New Cryst. Struct.*, 2011, **226**, 9.
29 U. Aydemir, C. Candolfi, H. Borrmann, M. Baitinger, A. Ormeci, W. Carrillo-Cabrera, C. Chubilleau, B. Lenoir, A. Dauscher, N. Oeschler, F. Steglich and Y. Grin, *Dalton Trans.*, 2010, **39**, 1078-1088.
30 T. Kume, T. Koda, S. Sasaki, H. Shimizu and J. S. Tse, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2004, **70**, 052101.
31 G. K. Ramachandran and P. F. McMillan, *J. Solid State Chem.*, 2000, **154**, 626.
32 S. Stefanoski and G. S. Nolas, *Cryst. Growth Des.*, 2011, **11**, 4533-4537.
33 H. Fukuoka, J. Kiyoto and S. Yamanaka, *Inorg. Chem.*, 2003, **42**, 2933-2937.
34 A. Bhattacharya and S. Bhattacharya, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2016, **94**, 094305.
35 A. Bhattacharya, C. Carbogno, B. Böhme, M. Baitinger, Y. Grin and M. Scheffler, *Phys. Rev. Lett.*, 2017, **118**, 236401.
36 J. Callaway, *Phys. Rev.*, 1959, **113**, 1046-1051.
37 M. Asen-Palmer, K. Bartkowski, E. Gmelin, M. Cardona, A. P. Zhernov, A. V. Inyushkin, A. Taldenkov, V. I. Ozhogin, K. M. Itoh and E. E. Haller, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1997, **56**, 9431-9447.
38 P. Hohenberg and W. Kohn, *Phys. Rev.*, 1964, **136**, B864.

39 W. Kohn and L. J. Sham, *Phys. Rev.*, 1965, **140**, A1133.

40 V. Blum, R. Gehrke, F. Hanke, P. Havu, V. Havu, X. Ren, K. Reuter and M. Scheffler, *Comput. Phys. Commun.*, 2009, **180**, 2175.

41 J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou and K. Burke, *Phys. Rev. Lett.*, 2008, **100**, 136406.

42 D. Frenkel and B. Smit, *Understanding Molecular Simulation*, Academic Press, San Francisco, 2002.

43 A. Togo, F. Oba and I. Tanaka, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2008, **78**, 134106.

44 G. S. Nolas, J.-M. Ward, J. Gryko, L. Qiu and M. A. White, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2001, **64**, 153201.

45 S. Stefanoski, J. Martin and G. S. Nolas, *J. Phys.: Condens. Matter*, 2010, **22**, 485404.

46 *The Physics and Chemistry of Inorganic Clathrates*, ed. G. S. Nolas, Springer, Dordrecht, 2014.