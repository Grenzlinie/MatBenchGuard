PHYSICAL REVIEW B 93, 134115 (2016)

# Thermal vacancies in random alloys in the single-site mean-field approximation

A. V. Ruban
Department of Materials Science and Engineering, KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden
and Materials Center Leoben Forschung GmbH, A-8700 Leoben, Austria

(Received 24 December 2015; revised manuscript received 16 February 2016; published 25 April 2016)

A formalism for the vacancy formation energies in random alloys within the single-site mean-filed approximation, where vacancy-vacancy interaction is neglected, is outlined. It is shown that the alloy configurational entropy can substantially reduce the concentration of vacancies at high temperatures. The energetics of vacancies in random $Cu_{0.5}Ni_{0.5}$ alloy is considered as a numerical example illustrating the developed formalism. It is shown that the effective formation energy increases with temperature, however, in this particular system it is still below the mean value of the vacancy formation energy, which would correspond to the vacancy formation energy in a homogeneous model of a random alloy, such as given by the coherent potential approximation.

DOI: 10.1103/PhysRevB.93.134115

Concentration of vacancies is one of the key parameters that determines the kinetics of phase transformation and diffusion in solids. In spite of the structural simplicity of vacancies, their energetics has proven to be one of the least reliable physical properties determined in the first-principles calculations (see, for instance, Refs. [1–6]). The situation becomes even more complicated at high temperatures, where anharmonic effects play an important role [6].

In this paper, we will not, however, deal with those problems related to different approximations in first-principles calculations and subsequent modeling of the vacancy thermodynamics, but rather consider another important aspect, namely, the statistical description of vacancies in concentrated alloys at finite temperature connected with their first-principles modeling. This topic has recently been recently attracted attention of several groups doing first-principles simulations [7–11]. In contrast to those investigations, in this work a simplified model for the energetics of vacancies will be presented for completely random alloys with the purpose to get a qualitative picture of the configurational effects.

It is based on the single-site mean-field approximation, and thus all the effects related to the vacancy-vacancy interactions will be ignored, while vacancy-alloy-component interactions will be indirectly taken into consideration through the account of the local environment effects next to the vacancy. Although this is a simplified model, it anyway yields a quite accurate description of the phenomenon in real systems. To demonstrate the formalism, we will consider the energetics of vacancies in $Cu_{0.5}Ni_{0.5}$ random alloy.

The vacancy formation energy at 0 K in a binary random $A_cB_{1-c}$ alloy can be formally defined as
$$
E_{f}^{0} = \min \left. \frac{dE_{0}(A_{c(1-c_v)}B_{(1-c)(1-c_v)}Va_{c_v})}{dc_v} \right|_{c_v=0}, \tag{1}
$$
where $E_0$ is the total energy per atom of a random $A_{c(1-c_v)}B_{(1-c)(1-c_v)}Va_{c_v}$ alloy consisting $c_v$ concentration of vacancies ($Va$). This definition takes into consideration the fact that the derivative in (1) is not well defined since in real random alloys there exist substantial fluctuations of local compositions, which affect this derivative leading to a wide spectrum of the local vacancy formation energies connected to the specific space arrangements of the alloy components around the vacancy. At 0 K, the vacancy formation energy, $E_{f}^{0}$ is apparently determined by the lowest value of the derivative in (1). Definition (1) also formally implies that the ratio of the concentrations of $A$ and $B$ alloy components is not changed during vacancy formation.

The dependence of the vacancy formation energy on the local environment can be also viewed as interaction energy between vacancy and alloy components. Nowadays, it can be obtained in first-principles calculations using, for instance, the so-called local cluster expansion [7,10]. If a supercell approach is used to determine local vacancy formation energies in random alloys, these effects can be naturally reproduced since the fluctuations of the local environment around each site are inevitable.

The existence of the local environment effects becomes important at finite temperatures, where vacancies with higher formation energies can be also created. For a given alloy configuration one can introduce the local vacancy formation energy distribution function, $g(E)$, which determines the number of sites, $Ng(E)$ in the alloy sample of size $N$, where the local vacancy formation energy is $E$, which satisfies the following normalization:
$$
\int dE g(E) = 1. \tag{2}
$$

At finite temperatures, $g(E)$ determines the distribution of vacancies with respect to their local environment. To obtain it, we first define effective vacancy formation energy or free energy, which connects the free energy of the system with concentration of vacancies in a phenomenological way. For a binary random $A_cB_{1-c}$ alloy, it is defined as
$$
G_{\text{vac}} = c_v \bar{G}_f - T S_{\text{conf}}, \tag{3}
$$
where $c_v$ is the equilibrium concentration of vacancies; $\bar{G}_f$ is the effective vacancy formation free energy and $S_{\text{conf}}$ the configurational entropy of an alloy with vacancies:
$$
S_{\text{conf}} = -\left[ c_v \ln c_v + c_A \ln c_A + c_B \ln c_B \right], \tag{4}
$$
where $c_A = c(1 - c_v)$ and $c_B = (1 - c)(1 - c_v)$ are the concentration of alloy components, which implies that the ratio of concentrations of both components remains constant and the same as in the alloy without vacancies.

2469-9950/2016/93(13)/134115(5)
134115-1
©2016 American Physical Society

A. V. RUBAN

PHYSICAL REVIEW B 93, 134115 (2016)

In the single-site approximation, the minimization of (3) with respect to $c_v$ under the condition that the concentration of vacancies is substantially smaller than that of alloy components yields:
$$
c_{v}=\exp \left[-\frac{\bar{G}_{f}+T S_{\text {all }}}{T}\right] \equiv \exp \left[-\frac{\widetilde{G}_{f}}{T}\right],\qquad(5)
$$
where $S_{\text {all }}=-[c \ln c+(1-c) \ln (1-c)]$ is the alloy configurational entropy without vacancies, and here, we also define the renormalized vacancy formation energy, $\widetilde{G}_{f}=\bar{G}_{f}+T S_{\text {all }}$, which is different from the effective formation energy due to an additional configurational entropy contribution.

This result shows that the alloy configurational entropy can substantially reduce the concentration of vacancies in alloys. For instance, in the equiatomic binary random alloy ($c=0.5$), the equilibrium concentration is reduced by a factor of 2 compared to that in pure metal. At 1500 K, it corresponds to an approximate increase of the effective vacancy formation energy of about 0.09 eV. Let us note that the above derivation holds for multicomponent alloys, where this effect can be much more pronounced. For instance, in a four-component equimolar (frequently called high entropy) random alloy the concentration of vacancies will be four times lower than that in pure metal having the same vacancy formation energy, which corresponds to the additional increase of the effective vacancy formation energy of about 0.18 eV at 1500 K.

Considering vacancies at different sites as independent, i.e., neglecting vacancy-vacancy interaction and assuming that the vacancy formation entropy, $S_f$, associated with vibrational, magnetic and electronic degrees of freedom, does not depend on the local environment, it is easy to show that
$$
c_{v}=\exp \left(S_{f}-S_{\text {all }}\right) \int d E g(E) \exp \left(-\frac{E}{T}\right).\qquad(6)
$$

Otherwise one should consider the distribution function for the local vacancy formation free energies, $g_G(G)$. The expression under the integral in (6) is just the concentration of vacancies for specific energy formation $E$: $c_v(E)=g(E)\exp\left(-\frac{E}{T}\right)$. Comparing (5) and (6), one finds that
$$
\bar{G}_{f}=-T \ln \left[\int d E g(E) \exp \left(-\frac{E}{T}\right)\right]-T S_{f},\qquad(7)
$$
or the effective vacancy formation energy, $\bar{E}_f$ is
$$
\bar{E}_{f}=-T \ln \left[\int d E g(E) \exp \left(-\frac{E}{T}\right)\right],\qquad(8)
$$
while the renormalized vacancy formation energies will have an additional contribution $T S_{\text {all }}$: $\widetilde{G}_{f}=\bar{G}_{f}+T S_{\text {all }}$ and $\widetilde{E}_{f}=\bar{E}_{f}+T S_{\text {all }}$.

Let us now consider vacancy energetics in $\mathrm{Cu}_{0.5} \mathrm{Ni}_{0.5}$ random alloy. It should be stressed again that only a configurational part of the problem will be considered here, without any complications related to other thermal effects, such as electronic, vibrational, or magnetic excitations. We therefore also disregard thermal lattice expansion and perform calculations for a fixed lattice parameter of $3.56 \mathring{A}$.

To determine the local vacancy formation energies, we use the exact-muffin-tin orbital locally self-consistent Green's function (ELSGF) method [12], which allows relatively accurate first-principles calculations of the vacancy formation energies, at least on a rigid lattice without a consideration of the local lattice relaxations. The latter may decrease the vacancy formation energy by 0.1-0.2 eV, which is comparable with the usual error due to the use of different exchange-correlation approximations. The supercell size has been chosen to be 108 atoms (a $3\times3\times3$ cell built upon the four-atom cubic fcc cell [13]).

Every atom in this supercell was exchanged by a vacancy, and then the local vacancy formation energy at site $i$, $E_f^i$, has been determined as
$$
E_{f}^{i}=E_{\mathrm{vac}}^{i}-\frac{N-1}{N} E_{\mathrm{all}}-(N-1) \Delta c \mu_{\mathrm{eff}},\qquad(9)
$$
where $E_{\mathrm{vac}}^i$ is the total energy of the supercell with vacancy at site $i$; $E_{\text {all }}$ the total energy of the defect free supercell; $N$ is the number of atoms in the supercell; $\Delta c$ is the change of the supercell composition due to vacancy formation (for instance, in our case $\Delta c=\pm(53 / 107-54 / 108)$, and $\mu_{\text {eff }}$ is the effective chemical potential of the alloy determined as
$$
\mu_{\mathrm{eff}}=\frac{\partial E_{0}\left(A_{c} B_{1-c}\right)}{\partial c}.\qquad(10)
$$

Here, the $E_0$ is the total energy per atom of random $A_c B_{1-c}$ alloy. The latter can be quite accurately (and, what is important, consistently with the LSGF calculations) obtained by the EMTO-CPA method [14,15] using the Lyngby version of the code [16] with the appropriate choice of the electrostatic screening constants (determined again from the corresponding ELSGF supercell calculations [17]).

Other details of the calculations are the following. The partial waves up to $l_{\max}=3$ were used in the self-consistent calculations. The total energies have been obtained using the full charge density technique [15]. The ELSGF calculations have been performed using the local interaction zone (LIZ) which included the first two coordination shells around the central site. This means that chemical configurational effects were effectively cut off beyond the second coordination shell (which is not the case of electrostatic interactions, although they are relatively weak in this system, and some multisite interactions for the clusters within the LIZ). The PBE-sol exchange-correlation potential [3] has been used, which is partly the reason for the difference of the present results and those of Ref. [10].

In Fig. 1, the local vacancy formation energies are shown as a function of the number of Cu atoms next to the vacancy [18]. Although there is a dispersion of the local vacancy formation energies for every number of Cu nearest neighbors, they almost linearly decrease with the number of Cu nearest neighbors. The slope of the average descent of the local energies is in fact the vacancy-Cu (or vacancy-Ni if taken with the opposite sign) interaction energy, which is approximately $-0.082$ eV for the first and 0.018 eV for the second coordination shells. The dispersion is due to other type of interactions.

It should be mentioned that there is no apparent dependence of the local vacancy formation energies on the type of the atom occupying this site in the defect free supercell. This contrasts with the results obtained in Ref. [10] where much smaller

134115-2

![](./images/814532381389094914_1.jpg)

FIG. 1. Local vacancy formation energies in 108-atom supercell representing a random ${\rm Cu_{0.5}Ni_{0.5}}$ alloy. The distribution of the local vacancy formation energies with respect to the number of the Cu nearest neighbors is shown in the top panel of the figure, while the distribution with respect to the number of the next-nearest neighbors is shown in lower panel. In the latter case only sites having six Cu nearest neighbors are included in the figure. Straight lines show the average slopes, which corresponds to the vacancy-Cu interaction at the first and second coordination shell, respectively.

supercells have been used. From a general point of view, such a dependence should not exist in the macroscopic limit, unless a ghost of the removed atom is still in the site. Although in reality nobody is certain about ghosts, they cannot exist in the well-determined first-principles calculations.

The spurious dependence can originate from some technical details of the modeling. For instance, it is clear that small supercells, of an order of tens of atoms, provide quite a bad model for investigation of the local environment effects due to the fact that no good statistics can be obtained just from several sites. Besides, every exchange of an atom by vacancy leads to the different (from the initial) on average atomic distribution correlations functions.

The difference in statistics of the local environment for different alloy components of course also exists in the case of the 108-atom supercell used here, where the representation of the possible local environment effects is also quite restricted. It can be clearly seen in Fig. 1 that there are no sites in the supercell completely surrounded by Cu or Ni atoms, and there is only one site with 11 Cu nearest neighbors, while there are no sites with 11 Ni nearest neighbors.

In spite of this fact, one can still establish a qualitatively clear picture of the local environment effects in alloy. In Fig. 2, the local vacancy formation energy distribution function, $g(E)$, obtained from the present $ab$ initio calculations is shown. It was calculated using 0.08 eV energy interval window, which corresponds to the average change of the local vacancy formation energy when the number of the Cu nearest neighbors changes by one. As one can see, it can be very well approximated by the discreet binomial distribution, which for a binary equiatomic alloy is
$$
g_{b}[E(n)]=\frac{12!}{2^{12} n!(12-n)!},\qquad(11)
$$
for $n$ going from 0–12 and $E_{f}(n)=E_{f}^{0}+n V_{1}$ where $E_{f}^{0}$ is the lowest local vacancy formation energy [as it is determined in Eq. (1)], which corresponds to the case $n=0$ and $V_{1}$ is the positive interaction energy between the vacancy and the counted by $n$ alloy component. It is clear that such a choice of interaction, which is positive in this case, can be always made. In our case, it corresponds to the vacancy-Ni interaction and thus $n$ is the number of Ni atoms next to the vacancy.

![](./images/814532381389094914_2.jpg)

FIG. 2. Local vacancy formation energy distribution functions: squares are the results of the 108-atom supercell calculations; circles are binomial distribution (see text) and crosses are normal distribution.

Equally, the local vacancy formation energy distribution function, $g(E)$, can be approximated by the continues normal distribution (for the equiatomic composition only) as
$$
g_{n}(E)=\frac{1}{\sigma \sqrt{2 \pi}} \exp \left[-\frac{\left(E-\left\langle E_{f}\right\rangle\right)^{2}}{2 \sigma^{2}}\right],\qquad(12)
$$
where $\langle E_{f}\rangle$ is the mean local vacancy formation energy, which is about 1.9 eV in this particular case, and $\sigma=2|V_{1}|$.

Using $g_{n}(E)$ and (8), one can calculate the effective, $\bar{E}_{f}$, and renormalized, $\widetilde{E}_{f}$, vacancy formation energies as functions of temperature (no thermal lattice expansion and other effects are included). They are shown in Fig. 3. As one can see, both vacancy formation energies, effective and renormalized, exhibit quite strong dependence on the temperature at low temperatures, while at higher temperatures, $\bar{E}_{f}$ changes quite little and $\widetilde{E}_{f}$ grows linearly with temperature. It is interesting that at least in this particular case $\bar{E}_{f}$ does not reach the mean value, $\langle E_{f}\rangle$ even at relatively high temperatures.

![](./images/814532381389094914_3.jpg)

FIG. 3. Effective $(\widetilde{E}_{f})$ and renormalized $(\widetilde{E}_{f})$ vacancy formation energies in random $Cu_{0.5}Ni_{0.5}$ alloy obtained as a function of temperature neglecting all the possible type of thermal excitations except configurational in the single-site mean-field approximation. The dashed line shows the mean value of the vacancy formation energy, $\langle E_{f}\rangle$, which one, for instance, would obtain in the homogeneous CPA calculations.

In fact, $\langle E_{f}\rangle$ corresponds to the vacancy formation energy obtained in the homogeneous CPA calculations like those in Ref. [19,20], where all the sites of the supercell are treated as effective CPA medium of the given alloy composition [21]. This means that such energies do not make much sense in systems where the local vacancy formation energies strongly depend on their local environment, such as Cu-Ni calculated here.

Another energy of interest, which we call here $E_{d}$, is the local vacancy formation energy, which yields dominating contribution to the vacancy concentration at a given temperature. It is related to the dominating type of the local environment of vacancies at given $T$ and can be found by maximizing $c_{v}(E)$. In the case of a binary equiatomic alloy, it can be approximately obtained using the normal distribution $g_{n}(E)$ of the local vacancy formation energies:

$$
E_{d}=\left\langle E_{f}\right\rangle-\frac{\sigma^{2}}{T}=\left\langle E_{f}\right\rangle-\frac{4 V_{1}^{2}}{T}. \tag{13}
$$

This is shown in Fig. 3. As one can see, it is less than the effective formation energy, although at low temperatures, its definition (13) breaks down since $g_{n}(E)$ is always nonzero for all positive energies, while $g(E)$ of a real system is nonzero only within some specific energy interval above $E_{f}^{0}$.

Now, we can estimate the preferential local environment of vacancies at a given temperature. Since $\langle E_{f}\rangle \approx E_{f}^{0}+$ $(z_{1}/2)V_{1}$, where $z_{1}$ is the number of the nearest-neighbor sites, the number of Ni atoms next to the vacancy with the local formation energy $E_{d}$ at temperature $T$ is

$$
n_{\mathrm{Ni}}(E_{d})=\frac{z_{1}}{2}-\frac{4 V_{1}}{T}. \tag{14}
$$

This is a quite interesting result showing, first of all, that this number is inverse proportional to the temperature and, second, it is always less than $z_{1}/2$, which is just the average number of Ni atoms of the equiatomic random alloy considered here, reaching its maximum, $z_{1}/2=c_{\mathrm{Ni}}$, only at infinite temperature. This again shows that a homogeneous CPA-like model of vacancies in random alloys corresponds this infinite temperature limit and thus should always overestimate the vacancy formation energy if there is non-negligible vacancy-alloy-component interaction.

It is obvious that the number of Cu atoms next to the vacancy with the local formation energy $E_{d}$ at temperature $T$ is $n_{\mathrm{Cu}}(E_{d})=z_{1}/2+4V_{1}/T$ or in general in high temperature limit $n_{\mathrm{Cu}}(E_{d})=z_{1}c_{\mathrm{Cu}}+4V_{1}/T$ [22]. This kind of asymptotic behavior is observed for the average number of Cu nearest neighbors next to the vacancy as a function of temperature in Ref. [10] presented in Fig. 12, where one can clearly see inverse temperature dependence of this number on the temperature and the fact that the minimal average number of Cu atoms next to the vacancy in the limit $T \to \infty$ is 3 and which is the average number of Cu atoms in random $Cu_{0.25}Ni_{0.75}$ alloy at the first coordination shell $(z_{1}c_{\mathrm{Cu}})$.

In summary, a single-site mean-field theory for thermal vacancies in random alloys is presented. It shows that the alloy configurational entropy renormalizes the effective vacancy formation energy, and this contribution linearly increases with temperature. As a numerical example, we have calculated the vacancy formation energies in $Cu_{0.5}Ni_{0.5}$ random alloy and demonstrated that configurational effects play important role. In particular, the effective formation energy is lower than the mean value of the local vacancy formation energy, and this effect is proportional to the vacancy-solute/solvent interactions.

## ACKNOWLEDGMENTS

This work has been initiated after some discussion of the vacancy formation energies in random alloys with Hu-Bin Luo from the Key Laboratory of Magnetic Materials and Devices, Ningbo Institute of Material Technology and Engineering, Chinese Academy of Sciences. Financial support by the Austrian Federal Government (in particular from Bundesministerium für Verkehr, Innovation und Technologie and Bundesministerium für Wirtschaft, Familie und Jugend) represented by österreichische Forschungsförderungsgesellschaft mbH and the Styrian and the Tyrolean Provincial Government, represented by Steirische Wirtschaftsförderungsgesellschaft mbH and Standortagentur Tirol, within the framework of the COMET Funding Programme is gratefully acknowledged. The author also acknowledges the support of the Swedish Research Council (VR Project 2015-05538), the European Research Council grant, the VINNEX center Hero-m, financed by the Swedish Governmental Agency for Innovation Systems (VINNOVA), Swedish industry, and the Royal Institute of Technology (KTH). Calculations have been done using NSC (Linköping) and PDC (Stockholm) resources provided by the Swedish National Infrastructure for Computing (SNIC).


[1] R. Armiento and A. E. Mattsson, *Phys. Rev. B* **72**, 085108 (2005).

[2] A. E. Mattsson, R. R. Wixom, and R. Armiento, *Phys. Rev. B* **77**, 155211 (2008).

[3] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, *Phys. Rev. Lett.* **100**, 136406 (2008).

[4] A. E. Mattsson, R. Armiento, J. Paier, G. Kresse, J. M. Wills, and T. R. Mattsson, *J. Chem. Phys.* **128**, 084714 (2008).

[5] R. Nazarov, T. Hickel, and J. Neugebauer, *Phys. Rev. B* **85**, 144118 (2012).

[6] A. Glensk, B. Grabowski, T. Hickel, and J. Neugebauer, *Phys. Rev. X* **4**, 011018 (2014).

[7] A. Van der Ven and G. Ceder, *Phys. Rev. B* **71**, 054102 (2005).

[8] M. Muzyk, D. Nguyen-Manh, K. J. Kurzydlowski, N. L. Baluc, and S. L. Dudarev, *Phys. Rev. B* **84**, 104115 (2011).

[9] J. B. Piochaud, T. P. C. Klaver, G. Adjanor, P. Olsson, C. Domain, and C. S. Becquart, *Phys. Rev. B* **89**, 024101 (2014).

[10] X. Zhang and M. H. F. Sluiter, *Phys. Rev. B* **91**, 174107 (2015).

[11] A. A. Belak and A. Van der Ven, *Phys. Rev. B* **91**, 224109 (2015).

[12] O. E. Peil, A. V. Ruban, and B. Johansson, *Phys. Rev. B* **85**, 165140 (2012).

[13] The distribution of alloy components in the supercell was chosen in order to have the first eight pair atomic distribution correlation functions as in a completely random alloy. The quality of the atomic distribution is confirmed by good agreement of the statistical distribution of the local vacancy formation energies and the corresponding model binominal distribution.

[14] L. Vitos, I. A. Abrikosov, and B. Johansson, *Phys. Rev. Lett.* **87**, 156401 (2001).

[15] L. Vitos, *Computational Quantum Mechanics for Materials Engineers* (Springer-Verlag, London, 2007).

[16] The Lyngby version of the EMTO code properly takes into consideration electrostatics in random alloys in contrast to other existing versions. It is distributed by the author of the paper.

[17] A. V. Ruban and H. L. Skriver, *Phys. Rev. B* **66**, 024201 (2002); A. V. Ruban, S. I. Simak, P. A. Korzhavyi, and H. L. Skriver, *ibid.* **66** 024202 (2002).

[18] The local energies are approximately about 0.3–0.4 eV below the results of Ref. [10] due to different exchange correlation potential used in the calculations (see, for instance Table III in Ref. [10]) and neglect of local lattice relaxation effects in this work.

[19] L. Delczeg, B. Johansson, and L. Vitos, *Phys. Rev. B* **85**, 174101 (2012).

[20] E. K. Delczeg-Czirjak, L. Delczeg, and L. Vitos, and O. Eriksson, *Phys. Rev. B* **92**, 224107 (2015).

[21] The EMTO-CPA calculations of the vacancy formation energy using a 32-atom supercell $[2 \times 2 \times 2(\times 4)]$ where all the atomic positions are occupied by the inhomogeneous CPA effective medium of ${\rm Cu}_{50}{\rm Ni}_{50}$ random alloy yields the vacancy formation energy 1.87 eV, which is in good agreement with the ESLGF mean value of 1.9 eV taking into consideration that these are two completely different techniques, with different details of calculations such as the size of the supercell, $k$-point mesh, and CPA small inaccuracies.

[22] Let us note that this simple analysis is valid only at sufficiently high temperatures due to the use of the normal distribution, $g_n(E)$, in the derivation. The point is that $g_n(E)$ is not restricted by a system specific energy interval, like $g(E)$. Since $n(E_d) \geqslant 0$, the above consideration makes sense only for $T \geqslant (8/z_1)V_1$. In our case it is about 600 K.