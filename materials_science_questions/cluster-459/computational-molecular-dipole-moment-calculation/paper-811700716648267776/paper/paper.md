$Ab$ initio study on vibrational dipole moments of $XH^{+}$ molecular ions: $X = ^{24}\text{Mg}$, $^{40}\text{Ca}$, $^{64}\text{Zn}$,
$^{88}\text{Sr}$, $^{114}\text{Cd}$, $^{138}\text{Ba}$, $^{174}\text{Yb}$ and $^{202}\text{Hg}$

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2010 J. Phys. B: At. Mol. Opt. Phys. 43 245102

(http://iopscience.iop.org/0953-4075/43/24/245102)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 138.26.31.3
This content was downloaded on 14/07/2015 at 06:28

Please note that terms and conditions apply.

# Ab initio study on vibrational dipole moments of XH⁺ molecular ions: X = ²⁴Mg, ⁴⁰Ca, ⁶⁴Zn, ⁸⁸Sr, ¹¹⁴Cd, ¹³⁸Ba, ¹⁷⁴Yb and ²⁰²Hg

Minori Abe¹, Masatoshi Kajita², Masahiko Hada¹ and Yoshiki Moriwaki³

¹ Department of Chemistry, Tokyo Metropolitan University, 1-1, Minami-Osawa, Hachioji, Tokyo 192-0397, Japan
² National Institute of Information and Communications Technology, Nukui-Kitamachi, Koganei, Tokyo 184-8795, Japan
³ Department of Physics, University of Toyama, Gofuku, Toyama, 930-8555, Japan

E-mail: minoria@tmu.ac.jp

Received 16 July 2010, in final form 9 October 2010
Published 1 December 2010
Online at stacks.iop.org/JPhysB/43/245102

## Abstract
The vibrational matrix elements of electric dipole moments were theoretically estimated for the electronic ground state of XH⁺ molecular ions (X = ²⁴Mg, ⁴⁰Ca, ⁶⁴Zn, ⁸⁸Sr, ¹¹⁴Cd, ¹³⁸Ba, ¹⁷⁴Yb and ²⁰²Hg) using the complete active space second-order perturbation theory method.
Because of the large rotational constant and zero X-nuclear spin, these molecules are advantageous to be localized to a single $(v, J, F)$ state, where $v$, $J$, $F$ are quantum numbers of the vibrational, rotational and hyperfine states, respectively. The information of the dipole moments is very useful to localize the period to localize the molecular ion to the $(v, J, F) = (0, 0, 1/2)$ state and also the period to remain in this state, which is limited by the interaction with the black body radiation. The agreement of experimental and our theoretical spectroscopic constants ensures the accuracy of our results. Vibrational permanent and transition dipole moments were obtained with special care of accuracy in numerical integration. Spontaneous emission rates were calculated from the vibrational dipole moments and transition energies.

(Some figures in this article are in colour only in the electronic version)

---

## 1. Introduction
The control and manipulation of the internal and external degrees of freedom of molecules are valuable for the development of new quantum information processing [1]. State-prepared molecular targets can also lead to refined reaction studies, which include uni-molecular reactions with coherent light fields [2, 3] or bimolecular reactions between two reaction partners in a well-characterized quantum state [4]. State-prepared molecules are also useful for precise measurement of molecular vibrational–rotational transition frequencies, which is useful for the detection of the variances of natural constants (particularly for the proton-to-electron mass ratio, whose variance is difficult to detect on the basis of atomic transitions alone) [5–11].

The following methods have been developed to obtain cold neutral molecules: magnetic trapping of molecules via the buffer-gas cooling [12], electrostatic trapping of decelerated [13, 14] or filtered molecules [15] and formation of cold molecules from laser-cooled atoms via photoassociation [16] or Feshbach resonance [17]. Molecules formed via photoassociation or Feshbach resonance are initially in the vibrationally excited states. However, they are transformed to the vibrational ground state by the additional use of the stimulated Raman adiabatic passage scheme [17] or through shaped fs-laser pulses [16].

Cooling techniques for molecular ions have been developed in parallel. Sympathetic cooling with laser-cooled atomic ions has now become a standard method to cool

molecular ions [18–21]. With this method, the external degrees of the molecular ions are controlled well. However, couplings between the internal and external degrees are very small, and the equilibrium distributions in the vibrational rotational states are given by the balance between the transition induced by the black body radiation and the spontaneous emission (temperature of the surrounding circumstance $T$). The molecular ions are localized in the vibrational–rotational ground state, when $k_{\mathrm{B}} T$ is smaller than the energy separation between different energy states. However, it takes a certain period until the thermal equilibrium state is attained. The distribution in the ground state can be increased with a shorter period by irradiating additional light sources (pumping light source) [22]. To estimate the period for the pumping to the rotational ground state and the period that the molecular ions remain in the rotational ground state after turning off the pumping light source, the values of the permanent dipole moments (PDMs) and the vibrational transition dipole moments (TDMs) are necessary.

In this paper, vibrational PDMs and TDMs are theoretically estimated for $\mathrm{XH}^{+}$molecular ions ($\mathrm{X}={ }^{24} \mathrm{Mg}$, ${ }^{40} \mathrm{Ca},{ }^{64} \mathrm{Zn},{ }^{88} \mathrm{Sr},{ }^{114} \mathrm{Cd},{ }^{138} \mathrm{Ba},{ }^{174} \mathrm{Yb}$ and ${ }^{202} \mathrm{Hg}$). $\mathrm{XH}^{+}$ molecular ions are advantageous to be localized to a single $(v, J, F)$ state in the ${ }^{1} \Sigma$ state, because of the large rotational constants (when $T<4 \mathrm{~K}$, population in the $J=0$ state is larger than 0.9) and zero X-nuclear spin (when $J=0, F$ can only be $1 / 2$ ). Here, $v, J$ and $F$ are the quantum numbers of the vibrational, rotational and hyperfine states, respectively. The theoretical TDMs are also useful to estimate the attainable accuracy of measured molecular transition frequencies. The measured frequency uncertainty is dominated by the Stark effect, which can be estimated using the vibrational PDMs and TDMs.

For electronic ground states, we adopted complete active space second-order perturbation (CASPT2) theory [23, 24] with high-quality basis sets and draw the potential energy curve (PEC) of eight molecules. To verify the accuracy of our calculations, we compare calculated and experimental spectroscopic constants. We also mention relativistic effects on spectroscopic constants. We obtained PDM functions $\mu(R)$ and discuss the trend of $\mu(R)$ functions of the eight molecules. Numerical vibrational wavefunctions were solved from the PECs using the Numerov method. Matrix elements of the vibrational PDMs and TDMs were calculated from numerical integration. Spontaneous emission rates (SERs) of vibrational levels are briefly discussed.

## 2. Computational details

MOLCAS 7.2 software was used throughout this study [25]. We calculated the electronic ground state of $\mathrm{XH}^{+}$, using the complete active space self-consistent field (CASSCF) theory followed by the CASPT2 theory. The CASPT2 method is a good alternative to the multi-reference configuration–interaction (MRCI) method, accurate enough but computationally faster than the MRCI method. (For example of the $\mathrm{HgH}^{+}$system, the CASPT2 calculation requires 13 s whereas MRCI calculation requires 178 s in our computer.) We have demonstrated MRCI calculations for the $\mathrm{MgH}^{+}$molecule to confirm that the difference of MRCI and CASPT2 is acceptably small. We also performed the coupled cluster single, double, and perturbatively triple (CCSD(T)) calculations. In general, the CCSD(T) method includes a higher level of electron correlation than the CASPT2 or MRCI method, when the system can be described by single configuration such as closed-shell systems. In the present $\mathrm{XH}^{+}$case, CCSD(T) can locally describe the PEC near the equilibrium bond distance, but cannot describe the correct dissociation limit with two doublet systems (i.e. $\mathrm{X}^{+}$and $\mathrm{H}$ atoms). Hence the CCSD(T) method cannot describe the full region of PEC and it is not the proper method to obtain vibrational wavefunctions. To obtain the full region of potential curves, the MRCI or CASPT2 method is adequate. However, spectroscopic constants, which can be calculated from the local part of PECs by the CCSD(T) method, are more accurate and a good reference to check the CASPT2 reliability.

We used $C_{2 v}$ point group symmetry. The third-order Douglas–Kroll–Hess (DKH3) Hamiltonian was used to consider the spin-free relativistic (Rel) effects [26]. Spin–orbit effects were neglected because the electronic ground states are ${ }^{1} \Sigma_{0}$. To compute the expectation values of electric dipole moments, the picture change effect at the second-order DKH level was considered [27]. ‘DENSITY’ keywords of MOLCAS were used in the CASPT2 routine for the calculation of expectation values. We also calculated PDM functions using finite field perturbation theory (FFPT) with a finite field strength of 0.001 in atomic unit, and confirmed that ‘DENSITY’ and FFPT calculations in CASTP2 are consistent with each other.

We calculated PDM functions, $\mu(R)$,
$$
\begin{aligned}
\mu(R) \equiv & \int \Psi_{e}^{*}\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N_{\mathrm{elec}}}, R\right)\left(-\sum_{i}^{N_{\mathrm{elec}}} \mathbf{r}_{i}+\sum_{I}^{N_{\mathrm{nuc}}} Q_{I} \mathbf{R}_{I}\right) \\
& \times \Psi_{e}\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N_{\mathrm{elec}}}, R\right) \mathrm{d} \mathbf{r}_{1}, \ldots, \mathrm{d} \mathbf{r}_{N_{\mathrm{elec}}},
\end{aligned}
$$
where $\mathbf{r}_{i}$ is the position vector of the $i$ th electron, $\mathbf{R}_{I}$ is the position vector of the $I$ th nucleus, $\Psi_{e}^{*}\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{N_{\text {elec }}}, R\right)$ is the ground-state total electronic wavefunction, where $R$ is the nuclear separation distance, $N_{\text {elec }}$ is the number of electrons, $N_{\text {nuc }}$ is the number of nuclei and $Q_{I}$ is the nuclear charge of the $I$ th nucleus. We took the origin of the coordinates for the calculation of the PDM function as the centre of nuclear mass.

We used atomic-natural-orbital relativistic correlation-consistent (ANO-RCC) basis sets [28–30]. For $\mathrm{MgH}^{+}$and $\mathrm{CaH}^{+}$, we also adopted the non-relativistic (NRel) Hamiltonian using cc-PCV5Z basis sets for Mg [31, 32] and Ca [33], and cc-PC5Z basis sets for H [34]. For $\mathrm{ZnH}^{+}$, both NRel cc-pV5Z and Rel type of cc-pV5Z basis sets (cc-pV5Z-DK) [35] were also available and used to check relativistic effects with the NRel or Rel Hamiltonian. The contraction size of the used basis sets is listed in table 1. The active space of CAS is two electrons in two orbitals, composed of the valence $s$ of $\mathrm{X}$ and $1 s$ of $\mathrm{H}$ atomic orbitals. The orbitals correlated in the calculation of CASPT2, MRCI and CCSD(T) are taken differently between the cc-PCV5Z and ANO-RCC basis sets, which is described in table 1.

<table><thead><tr><th>Elements</th><th>Basis set</th><th>Contraction style</th><th>Correlated orbitals</th></tr></thead><tbody><tr><td>H</td><td>ANO-RCC</td><td>(8s4p3d1f)/[6s4p3d1f]</td><td>1s</td></tr><tr><td>H</td><td>cc-pV5Z</td><td>(8s,4p,3d,2f,1g)/[5s,4p,3d,2f,1g]</td><td>1s</td></tr><tr><td>Mg</td><td>ANO-RCC</td><td>(17s12p6d2f)/[9s8p6d2f]</td><td>2p,3s</td></tr><tr><td>Mg</td><td>cc-pCV5Z</td><td>(24s,18p,8d,6f,4g,2h)/[11s,10p,8d,6f,4g,2h]</td><td>2s,2p,3s</td></tr><tr><td>Ca</td><td>ANO-RCC</td><td>(20s16p6d4f)/[10s9p6d4f]</td><td>3p,4s</td></tr><tr><td>Ca</td><td>cc-pCV5Z</td><td>(26s,18p,8d,3f,2g,1h)/[12s,10p,5d,3f,2g,1h]</td><td>3s,3p,4s</td></tr><tr><td>Zn</td><td>ANO-RCC</td><td>(21s15p10d6f4g2h)/[10s9p8d6f4g2h]</td><td>3p,3d,4s</td></tr><tr><td>Zn</td><td>cc-pV5Z</td><td>(28s,20p,12d,4f,3g,2h,1i)/[9s,8p,6d,4f,3g,2h,1i]</td><td>3d,4s</td></tr><tr><td>Zn</td><td>cc-pV5Z-DK</td><td>(28s,20p,12d,4f,3g,2h,1i)/[9s,8p,6d,4f,3g,2h,1i]</td><td>3d,4s</td></tr><tr><td>Sr</td><td>ANO-RCC</td><td>(23s19p12d4f)/[11s10p7d4f]</td><td>4p,5s</td></tr><tr><td>Cd</td><td>ANO-RCC</td><td>(21s19p13d6f4g2h)/[10s8p8d5f4g2h]</td><td>4d,5s</td></tr><tr><td>Ba</td><td>ANO-RCC</td><td>(26s22p15d4f)/[12s10p8d4f]</td><td>5s,5p,6s</td></tr><tr><td>Yb</td><td>ANO-RCC</td><td>(25s22p15d11f4g2h)/[12s11p8d7f4g2h]</td><td>5s,5p,4f,6s</td></tr><tr><td>Hg</td><td>ANO-RCC</td><td>(25s22p16d12f4g2h)/[10s10p9d6f4g2h]</td><td>5d,6s</td></tr></tbody></table>

Table 1. Basis set size and correlated orbitals of each basis set.

<table><thead><tr><th>Hamiltonian/Basis set/Correlation</th><th>$R_{\text{e}}$($\mathring{\text{A}}$)</th><th>$\omega_{\text{e}}$ (cm$^{-1}$)</th><th>$B_{\text{e}}$ (cm$^{-1}$)</th><th>$\alpha_{\text{e}}$ (cm$^{-1}$)</th><th>$D_{\text{e}}$ (eV)</th></tr></thead><tbody><tr><td>Rel/ANO-RCC/CASPT2</td><td>1.658</td><td>1678.0</td><td>6.389</td><td>0.18</td><td>$1.9909^{\text{d}}$</td></tr><tr><td>Rel/ANO-RCC/MRCI</td><td>1.653</td><td>1701.4</td><td>6.428</td><td>0.19</td><td>2.0743</td></tr><tr><td>Rel/ANO-RCC/CCSD(T)</td><td>1.652</td><td>1702.4</td><td>6.435</td><td>0.19</td><td>$2.0751^{\text{e}}$</td></tr><tr><td>NRel/cc-pCV5Z/CASPT2</td><td>1.659</td><td>1680.1</td><td>6.379</td><td>0.18</td><td>$2.0119^{\text{d}}$</td></tr><tr><td>NRel/cc-pCV5Z/CCSD(T)</td><td>1.653</td><td>1705.8</td><td>6.423</td><td>0.17</td><td>$2.0939^{\text{e}}$</td></tr><tr><td>Previous theoretical work$^{\text{a}}$</td><td>1.657</td><td>1682.0</td><td>6.400</td><td>0.16</td><td>1.8529</td></tr><tr><td>Previous theoretical work$^{\text{b}}$</td><td>1.659</td><td>1599.0</td><td>–</td><td>–</td><td>1.9591</td></tr><tr><td>Experiment$^{\text{c}}$</td><td>1.652</td><td>1699.1</td><td>6.387</td><td>0.18</td><td>2.0805</td></tr></tbody></table>

Table 2. Spectroscopic constants of $^{24}\text{MgH}^{+}$.

$^{\text{a}}$ Reference [36].
$^{\text{b}}$ Reference [37].
$^{\text{c}}$ Reference [35].
$^{\text{d}}$ Estimated by the super molecular calculation of $R = 100$ au.
$^{\text{e}}$ Estimated by the atomic limit calculation.

At the CASPT2 level, the obtained range of the PECs was $R = 1.5$–50 au. From the calculated PECs, we solved the radial Schrödinger equation by the Numerov method and obtained vibrational wavefunctions with the $J = 0$ rotational state, using the VIBROT program in MOLCAS. Matrix elements of vibrational levels, i.e. $\text{TDM}_{v-v'}$ and $\text{PDM}v$, were calculated as

$$
\text{TDM}_{v-v'}=\frac{\left|\int \mu(R)\Psi_{v'}^{*}(R)\Psi_{v}(R)R^{2}\mathrm{d}R\right|}{\sqrt{\int \Psi_{v'}^{*}(R)\Psi_{v'}(R)R^{2}\mathrm{d}R}\sqrt{\int \Psi_{v}^{*}(R)\Psi_{v}(R)R^{2}\mathrm{d}R}}
\tag{2}
$$

and

$$
\text{PDM}_{v}=\frac{\left|\int \mu(R)\Psi_{v}^{*}(R)\Psi_{v}(R)R^{2}\mathrm{d}R\right|}{\int \Psi_{v}^{*}(R)\Psi_{v}(R)R^{2}\mathrm{d}R},
\tag{3}
$$

where $\Psi_{v}$ is the vibrational wavefunction with the state $v$. Because the $\Psi_{v}$ function is obtained as grid points by the Numerov method, integrations of equations (2) and (3) are calculated numerically by Simpson’s integration. We used an integration range from 1.5 to 50 au with 150 grid points to draw the vibrational wavefunction graphs and to obtain spectroscopic constants. We used an integration range from 1.5 to 15 au with 1000 grid points to obtain values of $\text{PDM}v$, the rotational constant ($B_{v}$) and the vibrational energy level ($E_{v}$). We used an integration range from 1.5 to 8.0 au with 1500 grid points to obtain values of $\text{TDM}_{v-v'}$, for $v$ and $v'$, which are less than 6. From the TDM values and vibrational energy differences, SERs $A v$ were calculated as follows:

$$
A_{v,J=0,J'=1}\approx\frac{16\pi^{3}}{3\varepsilon_{0}h^{4}c^{3}}\sum_{v'=0}^{v}(E_{v}-E_{v'})^{3}(\text{TDM}_{v-v'})^{2}, \quad (4)
$$

where $\varepsilon_{0}$ is the permittivity in vacuum, $h$ is the Planck constant and $c$ is the speed of light in vacuum.

## 3. Results and discussions

### 3.1. Spectroscopic constants

Tables 2–5 show spectroscopic constants of the $\text{MgH}^{+}$, $\text{CaH}^{+}$, $\text{ZnH}^{+}$ and $\text{CdH}^{+}$ molecules, respectively, with experimental [36] and/or previous theoretical data [37–41]. On table 6, we put all the results of $\text{SrH}^{+}$, $\text{BaH}^{+}$, $\text{YbH}^{+}$ and $\text{HgH}^{+}$ with the previous theoretical data [40, 42] since there are no experimental reports for these molecules.

In the result of $\text{MgH}^{+}$, the difference of basis sets and the Hamiltonians (Rel/ANO-RCC versus NRel/cc-PCV5Z) is very small in all the obtained spectroscopic constants. This is because relativity in Mg is very small and both ANO-RCC and cc-PCV5Z basis sets are large enough to describe the system. The results of MRCI are very close to the results of CCSD(T). The results of CASPT2 are slightly different from the ones of MRCI and CCSD(T), but the differences are acceptably

### Table 3. Spectroscopic constants of $^{40}\text{CaH}^+$.

| Hamiltonian/basis set/correlation | $R_\text{e}$(Å) | $\omega_\text{e}$ (cm$^{-1}$) | $B_\text{e}$ (cm$^{-1}$) | $\alpha_\text{e}$ (cm$^{-1}$) | $D_\text{e}$ (eV) |
|------------------------------------|-----------------|--------------------------------|---------------------------|--------------------------------|-------------------|
| Rel/ANO-RCC/CASPT2                 | 1.926           | 1457.7                         | 4.611                     | 0.09                           | 2.0169$^\text{c}$ |
| Rel/ANO-RCC/CCSD(T)                | 1.922           | 1480.8                         | 4.677                     | 0.09                           | 2.2665$^\text{d}$ |
| Rel/cc-pCV5Z/CASPT2                | 1.899           | 1486.9                         | 4.789                     | 0.09                           | 2.1381$^\text{c}$ |
| Rel/cc-pCV5Z/CCSD(T)               | 1.897           | 1501.5                         | 4.801                     | 0.09                           | 2.2199$^\text{d}$ |
| NRel/cc-pCV5Z/CASPT2               | 1.898           | 1478.4                         | 4.748                     | 0.08                           | 2.1634$^\text{c}$ |
| NRel/cc-pCV5Z/CCSD(T)              | 1.896           | 1502.7                         | 4.805                     | 0.09                           | 2.2455$^\text{d}$ |
| Previous theoretical work$^\text{a}$| 1.936           | 1511.0                         | 4.609                     | 0.13                           | 1.8355$^\text{e}$ |
| Previous theoretical work$^\text{b}$| 1.864           | 1468.0                         | –                         | –                              | 2.20              |

$^\text{a}$ Reference [36].
$^\text{b}$ Reference [38].
$^\text{c}$ Estimated by the super molecular calculation of $R=100$ au.
$^\text{d}$ Estimated by the atomic limit calculation.
$^\text{e}$ $D_0$ value.

---

### Table 4. Spectroscopic constants of $^{64}\text{ZnH}^+$.

| Hamiltonian/basis set/correlation | $R_\text{e}$(Å) | $\omega_\text{e}$ (cm$^{-1}$) | $B_\text{e}$ (cm$^{-1}$) | $\alpha_\text{e}$ (cm$^{-1}$) | $D_\text{e}$ (eV) |
|------------------------------------|-----------------|--------------------------------|---------------------------|--------------------------------|-------------------|
| Rel/ANO-RCC/CASPT2                 | 1.505           | 1945.3                         | 7.561                     | 0.23                           | 2.4821$^\text{c}$ |
| Rel/ANO-RCC/CCSD(T)                | 1.514           | 1931.9                         | 7.470                     | 0.24                           | 2.5076$^\text{d}$ |
| Rel/cc-pV5Z-DK/CASPT2              | 1.508           | 1939.9                         | 7.523                     | 0.24                           | 2.4639$^\text{c}$ |
| Rel/cc-pV5Z-DK/CCSD(T)             | 1.515           | 1933.5                         | 7.462                     | 0.24                           | 2.4971$^\text{d}$ |
| NRel/cc-pV5Z/CASPT2                | 1.527           | 1907.1                         | 7.345                     | 0.22                           | 2.3968$^\text{c}$ |
| NRel/cc-pV5Z/CCSD(T)               | 1.532           | 1904.9                         | 7.294                     | 0.22                           | 2.4330$^\text{d}$ |
| Previous theoretical work$^\text{a}$| 1.545           | 1868.0                         | –                         | –                              | 2.03              |
| Explt.$^\text{b}$                  | 1.515           | 1916                           | 7.407                     | 0.24                           | –                 |

$^\text{a}$ Reference [39].
$^\text{b}$ Reference [35].
$^\text{c}$ Estimated by the super molecular calculation of $R=100$ au.
$^\text{d}$ Estimated by the atomic limit calculations.

---

### Table 5. Spectroscopic constants of $^{112}\text{CdH}^+$.

| Hamiltonian/Basis set/Correlation | $R_\text{e}$(Å) | $\omega_\text{e}$ (cm$^{-1}$) | $B_\text{e}$ (cm$^{-1}$) | $\alpha_\text{e}$ (cm$^{-1}$) | $D_\text{e}$ (eV) |
|------------------------------------|-----------------|--------------------------------|---------------------------|--------------------------------|-------------------|
| Rel/ANO-RCC/CASPT2                 | 1.652           | 1819.6                         | 6.232                     | 0.20                           | 2.1767$^\text{d}$ |
| Rel/ANO-RCC/CCSD(T)                | 1.656           | 1824.7                         | 6.200                     | 0.17                           | 2.2212$^\text{e}$ |
| Previous theoretical work$^\text{a}$| 1.709           | 1696.0                         | –                         | –                              | 1.93              |
| Explt.$^\text{b}$                  | 1.667           | 1772.5                         | 6.071                     | 0.19                           | 2.1381$^\text{c}$ |

$^\text{a}$ Reference [40].
$^\text{b}$ Reference [35].
$^\text{c}$ $D_0$ value.
$^\text{d}$ Estimated by the super molecular calculation of $R=100$ au.
$^\text{e}$ Estimated by the atomic calculations.

---

small, such as $0.006$ Å in $R_e$, $6$ cm$^{-1}$ in $\omega_e$ and $0.08$ eV in $D_e$. Our calculated values are also in good agreement with the experimental data.

In the result of $\text{CaH}^+$, however, the obtained values of Rel/ANO-RCC and Rel/cc-pCV5Z (or NRel/cc-pCV5Z) are not so similar. The difference of Rel/ANO-RCC and NRel/cc-pCV5Z does not come from relativistic effects but probably comes from the structure of basis set functions, because the results of Rel/cc-pCV5Z and NRel/cc-pCV5Z are almost the same. There is a wealth of theoretical work, but no experimental data has been reported for $\text{CaH}^+$. However, previous theoretical data are not consistent with each other: for example, the value of $R_e$ is in the range of 1.86–2.09 Å [37]. The ANO-RCC basis set of Ca had a problem in the calculation of the 4s–3d transition energy of $\text{Ca}^+$ atomic spectra, while cc-PCV5Z reproduced it satisfactorily [43]. Hence, we adopted the PEC by NRel/cc-pCV5Z for further calculations to obtain the vibrational wavefunctions of the $\text{CaH}^+$ molecule.

In the calculations of $\text{ZnH}^+$, relativistic effects appear more significantly than in the calculations of $\text{MgH}^+$ or $\text{CaH}^+$. The results of relativistic calculation (Rel/ANO-RCC and Rel/cc-pV5Z-DK) are different from the results of NRel calculation (NRel/cc-pV5Z). In contrast, the difference of Rel/ANO-RCC and Rel/cc-pV5Z-DK is rather small and we could confirm the reliability of the ANO-RCC basis set for the $\text{ZnH}^+$ molecule. The relativistic results of the CCSD(T) method show good agreement with the experimental ones, although the relativistic CASPT2 results are slightly different from the experimental and CCSD(T) ones.

![](./images/811700716648267776_1.jpg)

Figure 1. Potential energy curve of the ground state of $^{24}\text{MgH}^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_{v}(R)$ (the various colourful lines) and permanent dipole moment functions $\mu(R)$ (CASPT2 level: the blue and dashed line, MRCI level: pink and solid line).

<table>
<thead>
<tr>
<th>Table 6. Spectroscopic constants of $^{88}\text{SrH}^+$,$^{138}\text{BaH}^+$, $^{174}\text{YbH}^+$ and $^{202}\text{HgH}^+$.</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>Molecule/Hamiltonian/basis set/correlation</th>
<th>$R_\text{e}$(Å)</th>
<th>$\omega_\text{e}$ (cm$^{-1}$)</th>
<th>$B_\text{e}$ (cm$^{-1}$)</th>
<th>$\alpha_\text{e}$ (cm$^{-1}$)</th>
<th>$D_\text{e}$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$^{88}\text{SrH}^+$/Rel/ANO-RCC/CASPT2</td>
<td>2.046</td>
<td>1397.3</td>
<td>4.072</td>
<td>0.079</td>
<td>2.0302$^\text{c}$</td>
</tr>
<tr>
<td>$^{88}\text{SrH}^+$/Rel/ANO-RCC/CCSD(T)</td>
<td>2.041</td>
<td>1408.8</td>
<td>4.094</td>
<td>0.078</td>
<td>2.1208$^\text{d}$</td>
</tr>
<tr>
<td>$^{88}\text{SrH}^+$/Previous theoretical work$^\text{a}$</td>
<td>2.079</td>
<td>1346</td>
<td>–</td>
<td>–</td>
<td>1.9948</td>
</tr>
<tr>
<td>$^{138}\text{BaH}^+$/Rel/ANO-RCC/CASPT2</td>
<td>2.145</td>
<td>1345.8</td>
<td>3.689</td>
<td>0.056</td>
<td>2.3613$^\text{c}$</td>
</tr>
<tr>
<td>$^{138}\text{BaH}^+$/Rel/ANO-RCC/CCSD(T)</td>
<td>2.139</td>
<td>1352.7</td>
<td>3.711</td>
<td>0.060</td>
<td>2.4504$^\text{d}$</td>
</tr>
<tr>
<td>$^{138}\text{BaH}^+$/Previous theoretical work$^\text{b}$</td>
<td>2.202</td>
<td>1408</td>
<td>–</td>
<td>–</td>
<td>2.2940</td>
</tr>
<tr>
<td>$^{174}\text{YbH}^+$/Rel/ANO-RCC/CASPT2</td>
<td>1.928</td>
<td>1492.6</td>
<td>4.560</td>
<td>0.098</td>
<td>1.9735$^\text{c}$</td>
</tr>
<tr>
<td>$^{174}\text{YbH}^+$/Rel/ANO-RCC/CCSD(T)</td>
<td>1.950</td>
<td>1477.4</td>
<td>4.460</td>
<td>0.094</td>
<td>1.9752$^\text{d}$</td>
</tr>
<tr>
<td>$^{202}\text{HgH}^+$/Rel/ANO-RCC/CASPT2</td>
<td>1.594</td>
<td>2021.5</td>
<td>6.669</td>
<td>0.224</td>
<td>2.6626$^\text{c}$</td>
</tr>
<tr>
<td>$^{202}\text{HgH}^+$/Rel/ANO-RCC/CCSD(T)</td>
<td>1.601</td>
<td>2031.2</td>
<td>6.609</td>
<td>0.179</td>
<td>2.6977$^\text{d}$</td>
</tr>
<tr>
<td>$^{202}\text{HgH}^+$/Previous theoretical work$^\text{b}$</td>
<td>1.627</td>
<td>1888</td>
<td>–</td>
<td>–</td>
<td>2.2246</td>
</tr>
<tr>
<td colspan="6">
$^\text{a}$ Reference [40].
<br>
$^\text{b}$ Reference [42].
<br>
$^\text{c}$ Estimated by the super molecular calculation of $R=100$ au.
<br>
$^\text{d}$ Estimated by the atomic calculations.
</td>
</tr>
</tbody>
</table>

For the $\text{CdH}^+$, $\text{SrH}^+$, $\text{BaH}^+$, $\text{YbH}^+$ and $\text{HgH}^+$ molecules, we calculated spectroscopic constants only by the relativistic approach because proper basis sets at the NRel level do not exist for these elements. In the calculation of $\text{CdH}^+$, our results show larger deviations from the experimental values than the deviations in $\text{ZnH}^+$ or $\text{MgH}^+$, but still provide better agreement than the previously reported values. The agreement between the CASPT2 and CCSD(T) results is also good. For $\text{SrH}^+$, $\text{BaH}^+$, $\text{YbH}^+$ and $\text{HgH}^+$ molecules, the previous theoretical works referred to here contain slightly old calculations. We were able to use better basis sets and the proper electron correlation and relativistic method than those used in previous works because of the high performance of recent computers and the development of methodologies. Hence we consider that our spectroscopic results are good theoretical references of these molecules.

### 3.2. PECs, PDMs and vibrational wavefunctions

Figures 1–8 show the PEC, PDM function $\mu(R)$ and vibrational wavefunctions $\Psi_{v}(R)$, with respect to the inter-nuclear distance $R$, for eight $\text{XH}^+$ molecules. In figure 1, we have included the PDM functions at both the CASPT2 (blue dashed line) and MRCI (pink solid line) levels, which are quite similar to each other. Table 7 summarizes vibrational energy, rotational constants and expectation values of PDM in each vibrational level. We obtained 16–21 vibrational levels for the $\text{XH}^+$ molecules. For the $\text{MgH}^+$ molecule, the MRCI results are also listed for comparison. The difference of MRCI and CASPT2 results is reasonably small in the lowest vibrational levels in table 7.

The present systems are ionic molecules and the value of PDM depends on the centre of coordinates. We took the origin of PDM as the centre of nuclear mass because we are

![](./images/811700716648267776_2.jpg)

Figure 2. Potential energy curve of the ground state of $^{40}\text{CaH}^+$ at the NRel/cc-pCV5Z/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

![](./images/811700716648267776_3.jpg)

Figure 3. Potential energy curve of the ground state of $^{64}\text{ZnH}^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

interested in (ro-)vibrational transitions of the molecules. The PDM values became positive when we took the $z$-axis as the direction from H to $\text{X}^+$. In the binding region, the PDM functions are conventionally approximated to the functions of $(R-R_e)/R_e$ at the second-order polynomials [44], such as

$$
\mu(R) \approx \mu_0 + \mu_1(R-R_e)/R_e + \mu_2((R-R_e)/R_e)^2. \tag{5}
$$

Our obtained PDM functions are possibly approximated to the second-order polynomials when the value of $R$ is less than 2–2.5 Å. Hence, this second-order approximation seems useful only for a few of the lowest vibrational levels (at least less than $v=4$). When $R$ becomes large, the PDM functions asymptotically go to the linear function, $m_{\text{H}}/(m_{\text{X}}+m_{\text{H}})R$, where $m_{\text{X}}$ and $m_{\text{H}}$ are the nuclear masses of X and H atoms, respectively. (The value of $m_{\text{H}}/(m_{\text{X}}+m_{\text{H}})R$ is obtained by 'the distance from the centre of nuclear mass to the $\text{X}^+$ atom' multiplied by '+1 charge' since the molecules dissociate to the mono-cationic atom $(\text{X}^+)$ and the neutral hydrogen atom $(\text{H}^0)$.)

The PDM functions are relatively similar in shape and magnitude among $\text{MgH}^+$, $\text{ZnH}^+$, $\text{CdH}^+$ and $\text{HgH}^+$. In contrast, the PDM functions of $\text{CaH}^+$, $\text{SrH}^+$, $\text{BaH}^+$ and $\text{YbH}^+$ show a different tendency; the PDM function takes the maximum at a larger value of $R$ than the equilibrium distance $R_e$ and the magnitude itself is larger than the rest of the molecules. To be the large magnitude of the PDM functions, the highest occupied molecular orbital should be located closely to the H atom in the present $\text{XH}^+$ systems. Actually, the atomic numerical Dirac–Coulomb Hartree–Fock calculations by GRASP2K [45] show that $\text{Ca}^+$, $\text{Sr}^+$ $\text{Ba}^+$ and $\text{Yb}^+$ have a larger averaged radius $\langle r \rangle$ value for the valence $s$ atomic orbital (3.71, 4.05, 4.53 and 3.76 au, respectively) while

![](./images/811700716648267776_4.jpg)

Figure 4. Potential energy curve of the ground state of $^{88}$SrH$^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

![](./images/811700716648267776_5.jpg)

Figure 5. Potential energy curve of the ground state of $^{112}$CdH$^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

Mg$^+$, Zn$^+$, Cd$^+$ and Hg$^+$ have relatively smaller $\langle r \rangle$ values for the valence $s$ orbital, such as 2.83, 2.53, 2.78 and 2.61 in au, respectively. The valence radial wavefunctions of Zn$^+$, Cd$^+$ and Hg$^+$ are contracted because of the incompleteness of nuclear charge shielding from the inner $d$-electrons and the $s$-orbital shrinkage by relativistic effects. Especially in Hg$^+$, 6$s$-orbital shrinkage by relativistic effects is significant and the PDM function in figure 8 is lower in value than those of the other molecules. Figure 9 summarizes the correlation between the $\langle r \rangle$ value of X$^+$ atoms and the $R_e$ value of molecules and the correlation between the $\langle r \rangle$ value of X$^+$ atoms and the $R$ value where the PDM function becomes maximum. We found that the high correlation between $\langle r \rangle$ and the $R$ value at the maximum PDM, and the eight molecules can be classified by two groups again.

### 3.3. TDMs and spontaneous emission rates of lower vibrational levels

TDMs, i.e. the off-diagonal matrix elements of the dipole moments at vibrational levels, are very sensitive to the numerical integration parameters, i.e. the number of grid points and integration range. This is because during the summation of a numerical integration with different vibrational wavefunctions, both negative and positive values exist and they are mostly cancelled by each other. In consequence, only a small value remains after the cancellation. In contrast, PDMs, i.e. diagonal values of matrix elements, have only the summation of positive or negative values without cancellation, and it is stable regardless to the integral grid number and range. Especially for higher vibrational states, it is difficult to ensure the precision of TDM. This is because

![](./images/811700716648267776_6.jpg)

Figure 6. Potential energy curve of the ground state of $^{138}\text{BaH}^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

![](./images/811700716648267776_7.jpg)

Figure 7. Potential energy curve of the ground state of $^{174}\text{YbH}^+$ at the Rel/ANO-RCC/CASPT2 level (the red and thick line) with vibrational wavefunctions $\Psi_v(R)$ (the various colourful lines) and the permanent dipole moment function $\mu(R)$ (the blue and dashed line).

the wavefunctions span over a wide range in $R$ and a greater number of grid points are required to keep the grid width adequately small. Besides, the wavefunctions have a lot of nodes for higher vibrational levels and a larger number of grid points are again required for the smooth description of the waves. Hence, in this work, we do not obtain the TDM values of higher vibrational levels. We only focus on TDMs of five lower vibrational levels by choosing 1500 grid points and an integration range of $R$ from 1.5 au to 8.0 au for $\text{MgH}^+$, $\text{CaH}^+$, $\text{ZnH}^+$, $\text{SrH}^+$, $\text{CdH}^+$ and $\text{HgH}^+$ systems. For the $\text{BaH}^+$ system, the integration range of $R$ is taken as 1.5–9.0 au and there are 1500 grid points. For the $\text{YbH}^+$ system, we used 1400 grid points with the integration range of $R$ from 1.5 to 8.0 au since there were some instability problems when we calculated vibrational levels with more than 1400 grid points.

Table 8 shows TDM values of the lowest five vibrational levels. The last digit may not converge against a gradual increase in the grid points. The values of TDM at the CASPT2 level in the $\text{MgH}^+$ molecule are close to the values of TDM at the MRCI level. Nonorthonormality of overlap matrices slightly exists: matrix elements of 3–2 of $\text{MgH}^+$, 4–3 of $\text{CaH}^+$, 4–3 of $\text{SrH}^+$, 1–0 of $\text{CdH}^+$, 1–0, 2–1, 3–2 of $\text{BaH}^+$ and 2–1 of $\text{YbH}^+$ are approximately $1.1$–$3.6\times10^{-3}$ and the rest of the non-diagonal parts are less than $1\times10^{-3}$. We obtained similar TDM values of 1–0 for all the molecules except $\text{BaH}^+$. The constant term $\mu_0$ in equation (5) does not contribute to the TDM integration owing to the orthogonality of vibrational wavefunctions and hence the decline of the PDM function is important for large values of TDM. The decline of the PDM function of the $\text{BaH}^+$ molecule around the

![](./images/811700716648267776_8.jpg)

Figure 8. Potential energy curve of the ground state of $^{202}\text{HgH}^+$ at the Rel/ANO-RCC/CASPT2 level (the thick red line) with vibrational wavefunctions $\Psi_v(R)$ (lines with various colours) and the permanent dipole moment function $\mu(R)$ (the dashed blue line).

Table 7. Vibrational energy levels (cm⁻¹), rotational constants (cm⁻¹) and permanent dipole moments (PDMs) of each vibrational level.

<table>
<thead>
<tr>
<th></th>
<th colspan="3">$^{24}\text{MgH}^+$(CASPT2)</th>
<th colspan="3">$^{24}\text{MgH}^+$(MRCI)</th>
<th colspan="3">$^{40}\text{CaH}^+$</th>
</tr>
<tr>
<th>$V$</th>
<th>Energy (cm⁻¹)</th>
<th>$\text{B}_v$ (cm⁻¹)</th>
<th>PDM (Debye)</th>
<th>Energy (cm⁻¹)</th>
<th>$\text{B}_v$ (cm⁻¹)</th>
<th>PDM (Debye)</th>
<th>Energy (cm⁻¹)</th>
<th>$\text{B}_v$ (cm⁻¹)</th>
<th>PDM (Debye)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>826</td>
<td>6.249</td>
<td>3.202</td>
<td>840</td>
<td>6.294</td>
<td>3.304</td>
<td>736</td>
<td>4.711</td>
<td>5.310</td>
</tr>
<tr>
<td>1</td>
<td>2429</td>
<td>6.060</td>
<td>3.113</td>
<td>2470</td>
<td>6.111</td>
<td>3.221</td>
<td>2177</td>
<td>4.615</td>
<td>5.344</td>
</tr>
<tr>
<td>2</td>
<td>3963</td>
<td>5.865</td>
<td>3.008</td>
<td>4034</td>
<td>5.922</td>
<td>3.124</td>
<td>3579</td>
<td>4.516</td>
<td>5.365</td>
</tr>
<tr>
<td>3</td>
<td>5426</td>
<td>5.663</td>
<td>2.886</td>
<td>5529</td>
<td>5.727</td>
<td>3.010</td>
<td>4938</td>
<td>4.414</td>
<td>5.369</td>
</tr>
<tr>
<td>4</td>
<td>6816</td>
<td>5.452</td>
<td>2.748</td>
<td>6952</td>
<td>5.523</td>
<td>2.879</td>
<td>6253</td>
<td>4.307</td>
<td>5.353</td>
</tr>
<tr>
<td>5</td>
<td>8129</td>
<td>5.231</td>
<td>2.594</td>
<td>8299</td>
<td>5.310</td>
<td>2.731</td>
<td>7520</td>
<td>4.194</td>
<td>5.310</td>
</tr>
<tr>
<td>6</td>
<td>9362</td>
<td>4.998</td>
<td>2.425</td>
<td>9567</td>
<td>5.085</td>
<td>2.566</td>
<td>8737</td>
<td>4.073</td>
<td>5.233</td>
</tr>
<tr>
<td>7</td>
<td>10 511</td>
<td>4.750</td>
<td>2.244</td>
<td>10 752</td>
<td>4.847</td>
<td>2.386</td>
<td>9901</td>
<td>3.944</td>
<td>5.117</td>
</tr>
<tr>
<td>8</td>
<td>11 571</td>
<td>4.485</td>
<td>2.052</td>
<td>11 850</td>
<td>4.591</td>
<td>2.193</td>
<td>11 006</td>
<td>3.805</td>
<td>4.954</td>
</tr>
<tr>
<td>9</td>
<td>12 536</td>
<td>4.198</td>
<td>1.852</td>
<td>12 854</td>
<td>4.315</td>
<td>1.989</td>
<td>12 049</td>
<td>3.652</td>
<td>4.739</td>
</tr>
<tr>
<td>10</td>
<td>13 401</td>
<td>3.885</td>
<td>1.649</td>
<td>13 761</td>
<td>4.014</td>
<td>1.779</td>
<td>13 024</td>
<td>3.483</td>
<td>4.466</td>
</tr>
<tr>
<td>11</td>
<td>14 158</td>
<td>3.537</td>
<td>1.446</td>
<td>14 561</td>
<td>3.681</td>
<td>1.566</td>
<td>13 923</td>
<td>3.295</td>
<td>4.134</td>
</tr>
<tr>
<td>12</td>
<td>14 800</td>
<td>3.145</td>
<td>1.249</td>
<td>15 248</td>
<td>3.307</td>
<td>1.356</td>
<td>14 740</td>
<td>3.083</td>
<td>3.745</td>
</tr>
<tr>
<td>13</td>
<td>15 315</td>
<td>2.690</td>
<td>1.068</td>
<td>15 812</td>
<td>2.877</td>
<td>1.158</td>
<td>15 466</td>
<td>2.843</td>
<td>3.303</td>
</tr>
<tr>
<td>14</td>
<td>15 693</td>
<td>2.150</td>
<td>0.922</td>
<td>16 243</td>
<td>2.369</td>
<td>0.987</td>
<td>16 093</td>
<td>2.567</td>
<td>2.817</td>
</tr>
<tr>
<td>15</td>
<td>15 925</td>
<td>1.498</td>
<td>0.870</td>
<td>16 529</td>
<td>1.757</td>
<td>0.885</td>
<td>16 609</td>
<td>2.248</td>
<td>2.297</td>
</tr>
<tr>
<td>16</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>17 006</td>
<td>1.870</td>
<td>1.759</td>
</tr>
<tr>
<td>17</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>17 274</td>
<td>1.414</td>
<td>1.242</td>
</tr>
<tr>
<td>18</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>17 410</td>
<td>0.847</td>
<td>0.875</td>
</tr>
</tbody>
</table>

Table 8. Transition dipole moments (Debye) between the lowest five vibrational states of each molecule.

<table>
<thead>
<tr>
<th></th>
<th colspan="8">TDM (Debye)</th>
</tr>
<tr>
<th>$v-v'$</th>
<th>$^{24}\text{MgH}^+$ (CASPT2)</th>
<th>$^{24}\text{MgH}^+$ (MRCI)</th>
<th>$^{40}\text{CaH}^+$</th>
<th>$^{64}\text{ZnH}^+$</th>
<th>$^{88}\text{SrH}^+$</th>
<th>$^{112}\text{CdH}^+$</th>
<th>$^{138}\text{BaH}^+$</th>
<th>$^{174}\text{YbH}^+$</th>
<th>$^{202}\text{HgH}^+$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1-0$</td>
<td>0.16</td>
<td>0.15</td>
<td>0.13</td>
<td>0.16</td>
<td>0.18</td>
<td>0.13</td>
<td>0.38</td>
<td>0.10</td>
<td>0.13</td>
</tr>
<tr>
<td>$2-0$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.05</td>
<td>0.01</td>
<td>0.05</td>
<td>0.00</td>
<td>0.07</td>
<td>0.04</td>
<td>0.00</td>
</tr>
<tr>
<td>$2-1$</td>
<td>0.25</td>
<td>0.23</td>
<td>0.15</td>
<td>0.24</td>
<td>0.24</td>
<td>0.21</td>
<td>0.50</td>
<td>0.11</td>
<td>0.20</td>
</tr>
<tr>
<td>$3-0$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.01</td>
<td>0.00</td>
<td>0.01</td>
<td>0.00</td>
<td>0.02</td>
<td>0.01</td>
<td>0.00</td>
</tr>
<tr>
<td>$3-1$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.08</td>
<td>0.02</td>
<td>0.09</td>
<td>0.00</td>
<td>0.12</td>
<td>0.08</td>
<td>0.01</td>
</tr>
<tr>
<td>$3-2$</td>
<td>0.32</td>
<td>0.31</td>
<td>0.15</td>
<td>0.31</td>
<td>0.25</td>
<td>0.28</td>
<td>0.63</td>
<td>0.10</td>
<td>0.26</td>
</tr>
<tr>
<td>$4-0$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>$4-1$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.02</td>
<td>0.00</td>
<td>0.02</td>
<td>0.00</td>
<td>0.03</td>
<td>0.02</td>
<td>0.00</td>
</tr>
<tr>
<td>$4-2$</td>
<td>0.00</td>
<td>0.00</td>
<td>0.12</td>
<td>0.03</td>
<td>0.13</td>
<td>0.01</td>
<td>0.17</td>
<td>0.11</td>
<td>0.02</td>
</tr>
<tr>
<td>$4-3$</td>
<td>0.42</td>
<td>0.40</td>
<td>0.11</td>
<td>0.38</td>
<td>0.23</td>
<td>0.35</td>
<td>0.67</td>
<td>0.07</td>
<td>0.31</td>
</tr>
</tbody>
</table>

<table><caption>Table 9. Spontaneous emission rates (s⁻¹) of the four lowest vibrational excited states of each molecule.</caption>
<thead>
<tr>
<th rowspan="2">$v$</th>
<th colspan="8">Spontaneous emission rate (s⁻¹)</th>
</tr>
<tr>
<td>²⁴MgH⁺</td>
<td>⁴⁰CaH⁺</td>
<td>⁶⁴ZnH⁺</td>
<td>⁸⁸SrH⁺</td>
<td>¹¹²CdH⁺</td>
<td>¹³⁸BaH⁺</td>
<td>¹⁷⁴YbH⁺</td>
<td>²⁰²HgH⁺</td>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>32.4</td>
<td>15.5</td>
<td>49.6</td>
<td>26.3</td>
<td>28.7</td>
<td>96.8</td>
<td>9.7</td>
<td>38.6</td>
</tr>
<tr>
<td>2</td>
<td>69.9</td>
<td>34.3</td>
<td>100.7</td>
<td>56.5</td>
<td>61.2</td>
<td>195.9</td>
<td>24.0</td>
<td>76.1</td>
</tr>
<tr>
<td>3</td>
<td>101.7</td>
<td>63.0</td>
<td>147.0</td>
<td>90.1</td>
<td>92.7</td>
<td>298.8</td>
<td>47.2</td>
<td>110.7</td>
</tr>
<tr>
<td>4</td>
<td>143.7</td>
<td>99.8</td>
<td>189.5</td>
<td>124.1</td>
<td>123.3</td>
<td>398.2</td>
<td>75.3</td>
<td>140.5</td>
</tr>
</tbody>
</table>

![](./images/811700716648267776_9.jpg)

Figure 9. Correlation between the $\langle r\rangle$ value of X⁺ atoms and equilibrium distance (red circle) and correlation between the $\langle r\rangle$ value of X⁺ atoms and the $R$ values where the PDM functions are maximum (blue square). $R^2$ values in the graph indicate coefficients of determination of the linear functions.

equilibrium distance shown in figure 6 is much larger than the ones of the other molecules.

We obtained large values of TDM matrix elements for the $\Delta v=1$ transition, which is consistent with the harmonic oscillator approximation. We also found that some TDM matrix elements for $\Delta v=2$ are non-zero due to anharmonicity. Especially in CaH⁺, the TDM value of 4–2 is quite large and comparable with the value of 4–3. We checked the validity of the obtained 4–2 TDM value of CaH⁺ by changing the integral range, but the values were always comparable with the 4–3 value. Hence, we consider that the reason for the large TDM value of 4–2 reflects the shape of the $\mu(R)$ function of CaH⁺. In YbH⁺, the similar tendency of a large TDM value of 4–2 exists because CaH⁺ and YbH⁺ have similar $R_{\rm e}$ and $R$ values at the maximum of the PDM function, confirmed in figure 9.

From the TDM values and vibrational energy difference of two levels, we computed SERs in s⁻¹ for four vibrational excited states (with $J=1\rightarrow0$) listed in table 9. In all the molecules, the values of SERs monotonically increase when the vibrational level becomes higher. We can calculate the lifetime of a vibrational level from the reciprocal value of the corresponding SER and the natural line width from the value of the corresponding SER divided by $2\pi$. The transition with the lower SERs to the ground state should have a narrower line width and be advantageous to the precise measurement for the detection of the proton-to-electron mass ratio. However, the instability of the measured transition energy is proportional to the value of the SER divided by the transition frequency. Thus, measurement instabilities will not be so different among the transition of 0–1 and 0–2 (and 0 to higher states) if we compare within the same molecule.

## 4. Conclusion

We demonstrated $ab$ $initio$ CASPT2 calculations for the electronic ground state of XH⁺ ionic molecules, where X is ²⁴Mg, ⁴⁰Ca, ⁶⁴Zn, ⁸⁸Sr, ¹¹⁴Cd, ¹³⁸Ba, ¹⁷⁴Yb and ²⁰²Hg. Our calculated spectroscopic constants from the potential curves at the CASPT2 level show reasonably good agreement with the values of previous experiments and the CCSD(T) results. After checking the reliability of potential curves from the discussion of spectroscopic constants, we obtained vibrational wavefunctions of the electronic ground state of each molecule by the Numerov method. We calculated the matrix elements of transition dipole moments and PDMs of vibrational levels by numerical integration of the PDM function $\mu(R)$. The SER was also obtained. These values are useful to estimate the period until the vibrational–rotational energy distributions of molecular ions converge to the equilibrium state, after turning the additional light sources on or off. These values are also important to discuss the possibility and attainability for the precise measurements with XH⁺ molecules, which is described in detail in another paper.

## Acknowledgment

MA thanks the Japan Society for the Promotion of Science. MH thanks the CREST project in Japan Science and Technology Agency.

## References

[1] DeMille D 2002 *Phys. Rev. Lett.* **88** 067901

[2] Rice S and Zaho Z 2000 *Optical Control of Molecular Dynamics* (New York: Wiley)

[3] Shapiro M and Brumer P 2003 *Principles of the Quantum Control of Molecular Process* (New York: Wiley)

[4] Krems R V 2008 *Phys. Chem. Chem. Phys.* **10** 4079

[5] Schiller S and Korobov V 2005 *Phys. Rev. A* **71** 032505

[6] Kajita M 2008 *Phys. Rev. A* **77** 012511

[7] Koelmeij J C J, Roth B, Wicht A, Ernsting I and Schiller S 2007 *Phys. Rev. Lett.* **98** 173002

[8] Hudson J J, Sauer B, Tarbutt M R and Hinds E A 2002 *Phys. Rev. Lett.* **89** 023003

[9] Hudson E, Lewandowski H J, Sawyer B C and Ye J 2006 *Phys. Rev. Lett.* **96** 143004

[10] Kajita M 2009 *New J. Phys.* **11** 055010

[11] Kajita M and Moriwaki Y 2009 *J. Phys. B: At. Mol. Opt. Phys.* **42** 154022

[12] Weinstein J D, de Carvalho R, Guillet T, Friedrich B and Doyle J M 1998 *Nature* **395** 148

[13] Bethem H L, Berden G, Crompvoets F M H, Jongma R T, van Roij A J A and Meijer G 2000 *Nature* **406** 491

[14] Crompvoets F M H, Bethlem H L, Jongma R T and Meijer G 2001 *Nature* **411** 174

[15] Rieger T, Junglen T, Rangwala S A, Pinkse P W and Rempe G 2005 *Phys. Rev. Lett.* **95** 173002

[16] Viteau M, Chotia A, Allegrini M, Bouloufa N, Dulieu O, Comparat D and Pillet P 2008 *Science* **321** 232

[17] Ni K-K, Ospelkaus S, de Miranda M H G, Peer A, Neyenhuis B, Zirbel J J, Kotochigova S, Julienne P S, Jin D S and Ye J 2008 *Science* **322** 2318

[18] Molhave K and Drewsen M 2000 *Phys. Rev.* A **62** 011401

[19] Drewsen M, Montensen A, Martinussen R, Staanum P and Sorensen J L 2004 *Phys. Rev. Lett.* **93** 243201

[20] Blythe P, Roth B, Froehlich U H and Schiller S 2005 *Phys. Rev. Lett.* **95** 183002

[21] Staanum P F, Hojbjerre K, Wester R and Drewsen M 2008 *Phys. Rev. Lett.* **100** 243003

[22] Vogelius I S, Madsen L B and Drewsen M 2002 *Phys. Rev. Lett.* **89** 173003

Vogelius I S, Madsen L B and Drewsen M 2004 *Phys. Rev. A* **70** 053412

[23] Andersson K, Malmqvist P-Å, Roos B O, Sadlej A J and Woliński K 1990 *J. Phys. Chem.* **94** 5483

[24] Andersson K, Malmqvist P-Å and Roos B O 1992 *J. Chem. Phys.* **96** 1218

[25] Karlstrom G *et al* 2003 *Comput. Mater. Sci.* **28** 222

[26] Wolf A, Reiher M and Hess B 2002 *J. Chem. Phys.* **117** 9215

[27] Wolf A and Reiher M 2006 *J. Chem. Phys.* **124** 06102

[28] Widmark P-O, Malmqvist P-Å and Roos B O 1990 *Theor. Chim. Acta* **77** 291

[29] Roos B O, Veryazov V and Widmark P-O 2004 *Theor. Chem. Acc.* **111** 345

[30] Roos B O, Lindh R, Malmqvist P-Å, Veryazov V and Widmark P-O 2005 *J. Phys. Chem. A* **109** 6575

[31] Feller D 1996 *J. Comput. Chem.* **17** 1571

[32] Schuchardt K L, Didier B T, Elsethagen T, Sun L, Gurumoorthi V, Chase J, Li J and Windus T L 2007 *J. Chem. Inf. Model.* **47** 1045

[33] Koput J and Peterson K A 2002 *J. Phys. Chem. A* **106** 9595

[34] Dunning T H Jr 1989 *J. Chem. Phys.* **90** 1007

[35] Balabanov N B and Peterson K A 2005 *J. Chem. Phys.* **123** 064107

[36] Huber K P and Herzberg G ‘Constants of diatomic molecules’ (data prepared by Gallagher J W and Johnson R D, III) *NIST Chemistry Web Book* ed P J Linstrom and W G Mallard (Gaithersburg, MD: National Institute of Standards and Technology) (*NIST Standard Reference Database Number 69*) http://webbook.nist.gov (retrieved 12 February 2010)

[37] Canuto S, Castro M A and Sinha K 1993 *Phys. Rev. A* **48** 2461

[38] Aymar M, Guérout R, Sahlaoui M and Dulieu O 2009 *J. Phys. B: At. Mol. Opt. Phys.* **42** 154025

[39] Boutalib A, Daudey J P and Mouhtadi M E 1992 *Chem. Phys.* **167** 111

[40] Schilling J B, Goddard W A III and Beauchamp J L 1986 *J. Am. Chem. Soc.* **108** 582

[41] Schilling J B, Goddard W A III and Beauchamp J L 1987 *J. Am. Chem. Soc.* **109** 5565

[42] Ohanessian G, Brusich M J and Goddard W A III 1990 *J. Am. Chem. Soc.* **112** 7179

[43] Abe M, Hada M, Kajita M and Moriwaki M 2010 in preparation

[44] Tipping R H 1976 *J. Mol. Spectrosc.* **61** 272

[45] Jönsson P, He X, Fischer C F and Grant I P 2007 *Comput. Phys. Commun.* **177** 597