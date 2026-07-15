This article was downloaded by: [New York University]
On: 07 January 2015, At: 16:57
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office:
Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812082013841391617_1.jpg)

Molecular Physics: An International Journal
at the Interface Between Chemistry and
Physics

Publication details, including instructions for authors and subscription
information:
http://www.tandfonline.com/loi/tmph20

MCSCF calculation of the dipole moment
function of CO

Hans-Joachim Werner $^{a}$

$^{a}$ Institut für physikalische Chemie der Universität Frankfurt/M. , Robert-
Mayer Str. 11, D-6000, Frankfurt/M., West Germany
Published online: 23 Aug 2006.

To cite this article: Hans-Joachim Werner (1981) MCSCF calculation of the dipole moment function of
CO, Molecular Physics: An International Journal at the Interface Between Chemistry and Physics, 44:1,
111-123, DOI: 10.1080/00268978100102311

To link to this article: http://dx.doi.org/10.1080/00268978100102311

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the
"Content") contained in the publications on our platform. However, Taylor & Francis, our
agents, and our licensors make no representations or warranties whatsoever as to the
accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views
expressed in this publication are the opinions and views of the authors, and are not the views
of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon
and should be independently verified with primary sources of information. Taylor and Francis
shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses,
damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in
connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial
or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or
distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and
use can be found at http://www.tandfonline.com/page/terms-and-conditions

MOLECULAR PHYSICS, 1981, VOL. 44, No. 1, 111-123

# MCSCF calculation of the dipole moment function of CO

by HANS-JOACHIM WERNER

Institut für physikalische Chemie der Universität Frankfurt/M.,
Robert-Mayer Str. 11, D-6000 Frankfurt/M., West Germany

(Received 19 March 1981 ; accepted 13 May 1981)

Potential energy and dipole moment functions for the ground state of CO have been calculated using MCSCF wavefunctions. Some difficulties with the MCSCF method at large distances, which are due to the near degeneracy of the two asymptotic states, are discussed. From the theoretical dipole moment function and the RKR potential function vibrational dipole matrix elements have been evaluated. For the fundamental and first overtone sequences, the theoretical values are in excellent agreement with experimental data. For transitions involving large vibrational quantum numbers $(v^{\prime \prime}>25)$ the calculated matrix elements are expected to be the most reliable ones presently available.

## 1. INTRODUCTION

During the past decade much work has been devoted to the study of vibration-rotation transitions in the ground state of carbon monoxide. The accurate knowledge of the positions and intensities of these lines is of interest in astrophysics, since various vibration-rotation transitions involving quite large vibrational (up to 12) and rotational (~100) quantum numbers have been observed in the atmosphere of cooler stars [1] and in the photosphere of the sun [2]. Furthermore, the fundamental series $(\Delta v=1)$ of the CO vibration rotation transitions is of importance for the CO gas laser. More than 220 lasing lines with v' up to 36 have been observed [3,4]. The absolute wave numbers and molecular constants (Dunham coefficients) of CO have been determined more accurately than for any other molecule [3-15]. The CO laser lines serve therefore as very accurate frequency standards [12,16,17]. From the spectroscopic data RKR [18] potential energy functions valid over a relatively large range of internuclear distances, have been derived [19-21].

In order to interpret the stellar spectra quantitatively or to determine the relative population of vibrationally excited states in the products of chemical reactions the absolute intensities of the vibration-rotation transitions have to be known. For instance, the vibrational distribution of CO in the reaction $CS+O \to S+CO^{*}$ , which is used to pump the chemical CO laser [22], has been studied by various authors [23-28]. The intensities are proportional to the square of the matrix elements $M_{v^{\prime \prime} J^{\prime \prime} v' J'}=<\Psi_{v^{\prime \prime} J^{\prime \prime}}|M(r)| \Psi_{v' J'}>$ , where $M(r)$ is the electric dipole moment function (EDMF) of the molecule and $\Psi_{v, J}$ are vibrational wavefunctions which are solutions of the radial Schrödinger equation. For CO the sign of the elements $M_{v^{\prime \prime} J^{\prime \prime} v' J'}$ can be deduced unambiguously

0026-8976/81/4401 0111 $02.00 © 1981 Taylor & Francis Ltd

from the rotational dependence of the line intensities [29-34]. Usually, the
EDMF is approximated by a power series of $x=(r-r_{\mathrm{e}})/r_{\mathrm{e}}$:

$$
M(r) \cong \sum_{i=0}^{n} M_{i} x^{i}. \tag{1}
$$

In order to fit the $M_{i}$ such that the experimental line intensities are reproduced,
the matrix elements $\langle\Psi_{v^{\prime \prime} J^{\prime \prime}}|x^{i}|\Psi_{v^{\prime} J^{\prime}}\rangle$ must be evaluated. This can be done
either by solving the radial Schrödinger equation numerically [34, 35] using
the RKR potential energy function, or analytically [33, 36-38] by assuming a
Dunham potential

$$
V(x)=\gamma^{-2} x^{2}\left(1+\sum_{i} a_{i} x^{i}\right). \tag{2}
$$

In the latter case the rotationless matrix elements are obtained as a power
series of $\gamma=2 B_{\mathrm{e}} / \omega_{\mathrm{e}}$ (typically of order $10^{-2}$ to $10^{-3}$) with coefficients depending
on the $a_{i}, v$ and $\Delta v$. To first order in $\gamma$, the elements $M_{v}{ }^{v+n}(J=0)$ depend
only on the expansion coefficients $M_{i}, i \leqslant n$. Therefore, in order to find $M_{i}$ at
least the intensities of the fundamental and of the first $i-1$ overtone transitions
have to be known. This usually restricts the validity of the experimental
EDMF to quite a small region of internuclear distances around $r_{\mathrm{e}}$. For CO the
matrix elements $M_{v^{\prime \prime} J^{\prime \prime}}{ }^{v^{\prime} J^{\prime}}$ for various lines of the fundamental band [39,40]
and overtone transitions with $\Delta v \leqslant 4$ have been determined experimentally
[33, 40-45]. From these data cubic and quartic dipole moment function ex-
pansions have been derived [33-38]. Near the equilibrium distance these
functions are in very good agreement; at large distances $(x>0 \cdot 5)$, however, the
dipole moment functions diverge and do not show the correct long range
behaviour. Kirschner *et al.* [37] tried to remedy this drawback by approxi-
mating the EDMF by a Padé approximant

$$
M(x)=\frac{M_{0}\left(1+C_{1} x+C_{2} x^{2}\right)}{1+C_{3} x+C_{4} x^{2}+C_{5} x^{3}+C_{\infty} x^{6}}. \tag{3}
$$

The long range behaviour of this function depends on the coefficient $C_{\infty}$ which
had only been estimated.

The dipole moment functions derived from a small number of known
intensities can be used to calculate vibration-rotation dipole matrix elements
for other arbitrary transitions; however, due to the limited range of validity
of the EDMF the accuracy of matrix elements for transitions involving vibra-
tional quantum numbers larger than 20 is uncertain. On the other hand, the
dipole moment function can be obtained for large internuclear distances by *ab
initio* quantum mechanical calculations. In recent years, the accuracy of such
calculations [46-56] has been improved considerably and the theoretical results
are now of comparable accuracy with the most reliable experimental data. For
instance, using highly correlated SCEP/CEPA wavefunctions (self-consistent
electron pairs method [57] with coupled electron pair approximation [58-61])
or MCSCF wavefunctions (multi-configuration self consistent field) we
recently calculated the dipole moment functions for the hydrogen halides [51,
52] which yielded dipole matrix elements for the fundamental and first overtone
sequences with an accuracy of about 5 per cent. For CO many calculations
of the dipole moment at the equilibrium distances have been reported, but only

a few papers are concerned with the calculation of the dipole moment as a function of the internuclear distance. The first calculations of the EDMF near the equilibrium distance were performed at the Hartree-Fock level by Nesbet [54] and Huo [55], but these results were far from quantitative. A more accurate EDMF was obtained by Billingsley and Krauss [56] using MCSCF wavefunctions. Although in the MCSCF functions the configurations needed for proper dissociation into the asymptotic states $C(^3P) \times O(^3P)$ were included, the calculations were restricted to quite a small range of internuclear distances around $r_e$. The slope of the EDMF at $r_e$ obtained was 16 per cent too large. As has been pointed out by Kirby-Docken and Liu [48], this large error is probably due to the neglect of certain configurations which are important at intermediate internuclear distances. So far the most accurate EDMF for CO has been obtained by the latter authors (referred to in the following as KDL). On the basis of MCSCF orbitals they performed valence configuration interaction (VCI, including all configurations which can be obtained by dis- tributing the 10 valence electrons in the orbitals $3\sigma$ to $6\sigma$ and $1\pi$ and $2\pi$) and first order CI calculations (FOCI, which in addition to the VCI accounts for relaxation and polarization effects of the valence orbitals and for the semi- internal correlation). These calculations included all configurations needed for proper dissociation and bond formation and yielded dipole matrix elements for the fundamental and first overtone sequences with an accuracy of about 5 per cent. KDL compared their VCI and FOCI results also to CI calculations which included all singly and doubly substituted configurations with respect to the Hartree-Fock determinant (SD-CI). The SD-CI results were found to be much worse than those for VCI and FOCI. The first derivative of the EDMF at $r_e$, which mainly determines the dipole matrix elements of the funda- mental series, was obtained about 14 per cent too large. This is in agreement with findings of this investigation (see $\S 3$ ). Using PNO-CEPA (pseudo natural orbital coupled electron pair approximation [58-61] Werner and Meyer[62] obtained a dipole moment at $r_e$ which was about 0.15 D too large. Similar results were reported by Jaquet, Kutzelnigg and Staemmler [63]. The failure of the SD-CI approximation is probably due to the importance of triple and quadruple substitutions, which are needed for proper dissociation. The CEPA approximation, which corrects for these terms and has been shown to yield very accurate dipole moment functions for molecules with single bonds [48,51-53], seems to overshoot in cases with multiple bonds. This has also been found by Meyer and Rosmus [64] for the molecules SiO, PN, CS, $H_2CO$ and $H_2CS$. Recently, Cooper and Langhoff [65] published CI calculations of the potential and dipole moment functions for several states of CO. Their wave- functions comprised about 10 000 single and double substitutions with respect to a set of reference configurations which were selected perturbationally at various internuclear distances. The first derivative of the EDMF at $r_e$ was obtained 16 per cent too large. This considerable error is probably due to the use of canonical Hartree-Fock orbitals instead of MCSCF orbitals as a one particle basis for the CI calculations.

Here we present MCSCF calculations of the EDMF and the potential function of CO for a large range of internuclear distances. For comparison, SCEP (SD-CI) and SCEP/CEPA calculations in the equilibrium region have also been performed with the same basis set. Only the MCSCF wavefunction

yields an EDMF which closely parallels the experimental function in the region of its validity. In $\S 2$ we describe the basis and configuration sets used and discuss some difficulties arising at large distances due to the near degeneracy of the two asymptotic states. In $\S 3$ we present the calculated dipole matrix elements and compare them with available experimental and empirical data. It will be shown, that the matrix elements obtained from the MCSCF dipole moment function and the RKR potential energy function are in excellent agreement with the most accurate experimental values. It is expected therefore that the matrix elements obtained for large vibrational quantum numbers, which are not known experimentally, are the most reliable presently available.

## 2. COMPUTATIONAL DETAILS

Computations were performed with two different GTO basis sets. For preliminary test calculations we used Huzinagas [66] $9 s / 5 p$ sets with the innermost $4 s$ and $2 p$ functions contracted. This basis set was augmented by two sets of $d$-functions ($d_\sigma$ and $d_\pi$ only) with exponents $2 \cdot 0,0 \cdot 5$ for $\mathrm{O}$ and $1 \cdot 0,0 \cdot 25$ for $\mathrm{C}$. It yields quite accurate results near $r_{\mathrm{e}}$ but due to the missing flexibility in the valence region the dipole moments obtained are too small at large distances. Final calculations were performed with a larger basis set comprising $11 s, 6 p$ and $3 d$ functions for each atom. The $11 s$ sets were derived from Huzinagas $10 s$ sets (innermost $4 s$ contracted) by replacing the function with smallest exponent by two functions with exponents $0 \cdot 3,0 \cdot 12$ for $\mathrm{O}$ and $0 \cdot 16,0 \cdot 06$ for $\mathrm{C}$. Similarly, the $6 p$ sets were obtained from Huzinagas $5 p$ sets (innermost $2 p$ contracted) by replacing the outermost function by two functions with exponents $0 \cdot 25,0 \cdot 09$ for $\mathrm{O}$ and $0 \cdot 14,0 \cdot 05$ for $\mathrm{C}$. The exponents of the $d$-functions are $3 \cdot 0,1 \cdot 0,0 \cdot 3$ for $\mathrm{O}$ and $1 \cdot 5,0 \cdot 5,0 \cdot 15$ for $\mathrm{C}$. This basis set is expected to yield dipole matrix elements within 2 per cent of the limits of the methods applied.

MCSCF calculations have been performed with varying numbers of configurations. In order to allow proper dissociation to the two possible $|\mathrm{C}({ }^{3} P, M_{L}) \times \mathrm{O}({ }^{3} P,-M_{L})|^{1} \Sigma^{+}$($M_{L}=0,1$) asymptotic states and to describe properly the bond formation at intermediate distances the following 19 configurations are needed :

$$
\left|5 \sigma^{2}, 6 \sigma^{2},(5 \sigma 6 \sigma)\right|^{1} \Sigma^{+} \times\left|1 \pi^{4}, 1 \pi_{x}{ }^{2} 2 \pi_{y}{ }^{2}+2 \pi_{x}{ }^{2} 1 \pi_{y}{ }^{2},{ }^{3}\left(1 \pi_{x} 2 \pi_{x}\right){ }^{3}\left(1 \pi_{y} 2 \pi_{y}\right), 2 \pi^{4}\right|^{1} \Sigma^{+},
$$

$$
\left|5 \sigma^{2}, 6 \sigma^{2}\right| \times\left|\left(1 \pi^{3} 2 \pi\right),\left(1 \pi 2 \pi^{3}\right)\right|^{1} \Sigma^{+},
$$

$$
\begin{aligned}
\left|(5 \sigma 6 \sigma\right|^{3} \Sigma^{+} \times\left|\left(1 \pi^{3} 2 \pi\right),\left(1 \pi 2 \pi^{3}\right),{ }^{3}\left(1 \pi_{x} 2 \pi_{x}\right){ }^{1}\left(1 \pi_{y} 2 \pi_{y}\right)\right. & \\
& \left.+{ }^{3}\left(1 \pi_{y} 2 \pi_{y}\right){ }^{1}\left(1 \pi_{x} 2 \pi_{x}\right)\right|^{3} \Sigma^{+}.
\end{aligned}
$$

With these configurations the asymptotic states as well as the molecule at shorter distances are described by delocalized orbitals, i.e. at $r=\infty, p_{\sigma}(\mathrm{O})=2^{-1 / 2}(5 \sigma+6 \sigma)$, $p_{\sigma}(\mathrm{C})=2^{-1 / 2}(5 \sigma-6 \sigma), \quad p_{\pi}(\mathrm{O})=2^{-1 / 2}(1 \pi+2 \pi)$ and $p_{\pi}(\mathrm{C})=2^{-1 / 2}(1 \pi-2 \pi)$. In order to allow for correlation and relaxation effects near $r_{\mathrm{e}}$ additional configurations have to be included. First, we added the remaining five configurations which can be obtained from this set by different spin couplings, e.g.

$$
\left|5 \sigma^{2}, 6 \sigma^{2}\right| \times\left|{ }^{1}\left(1 \pi_{x} 2 \pi_{x}\right){ }^{1}\left(1 \pi_{y} 2 \pi_{y}\right)\right|,
$$

$$
\left|(5 \sigma 6 \sigma)\right|^{1} \Sigma^{+} \times\left|\left(1 \pi^{3} 2 \pi\right),\left(1 \pi 2 \pi^{3}\right),{ }^{1}\left(1 \pi_{x} 2 \pi_{x}\right){ }^{1}\left(1 \pi_{y} 2 \pi_{y}\right)\right|^{1} \Sigma^{+}.
$$

The resulting 24 configuration wavefunction includes all important configura- tions which can be obtained by distributing six electrons in the orbitals $5 \sigma, 6 \sigma, 1 \pi$ and $2 \pi$ (configurations of type $5 \sigma^{2} \to 2 \pi^{2}, 1 \pi^{2} \to 6 \sigma^{2}, 1 \pi_{x}^{2} \to 2 \pi_{y}^{2}$ have a very small effect on the dipole moment and have not been included). It corresponds essentially to the set of reference configurations for the FOCI calculation of KDL. Finally, in order to obtain more reliable results the following 6 con- figurations have been added which represent the most important (double) excitations from the Hartree-Fock determinant into the $7 \sigma$ and $3 \pi$ orbitals :

$$7 \sigma^{2} 1 \pi^{4},$$

$$5 \sigma^{2} ×\left|\left(1 \pi_{x}^{2} 3 \pi_{x}^{2}+1 \pi_{y}^{2} 3 \pi_{y}^{2}\right),{ }^{1}\left(1 \pi_{x} 3 \pi_{x}\right){ }^{1}\left(1 \pi_{y} 3 \pi_{y}\right)\right|,$$

$$\left|(5 \sigma 6 \sigma)\right|^{1} \Sigma^{+} ×\left|\left(1 \pi^{3} 3 \pi\right)\right|^{1} \Sigma^{+},$$

$$\left|(5 \sigma 7 \sigma)\right|^{1} \Sigma^{+} ×\left|\left(1 \pi^{3} 2 \pi\right),\left(1 \pi^{3} 3 \pi\right)\right|^{1} \Sigma^{+}.$$

These 30 configurations yield a dipole moment function which parallels closely the experimental function in the region of its validity. However, the absolute value of the dipole moment at $r_{e}$ is $0 \cdot 11 D$ too large. Errors of this magnitude have been reported also by KDL and others [70, 62, 63, 67]. Only the SD-CI dipole moment at $r_{e}$ is nearly exact, but in view of the large error of $(d M / d r)_{r_{e}}$ this seems to be accidental. We have performed various MCSCF calculations with up to 50 configurations including $8 \sigma$ and $4 \pi$ orbitals. In some of these calculations the $2 s$ electrons $(3 \sigma$ and $4 \sigma)$ were also correlated. Although im proving the wavefunction lowered the dipole moment slightly, an error of0-10 D remained. This error is presumably due to dynamic correlation effects which cannot be fully accounted for with MCSCF wavefunctions.

Preliminary test calculations at large distances revealed some difficulties with the MCSCF method which are now discussed briefly. Using quadratically convergent MCSCF procedures [68, 69] it is most advantageous to use the orbitals of a neighbouring geometry as a starting approximation for the next calculation. When proceeding in this manner from shorter to longer distances convergence is usually obtained in 2-3 iterations and smooth potential and dipole moment functions are obtained up to a distance of about $6.0 a_{0}$. How ever, on going to $6.5 a_{0}$ large orbital changes suddenly occur and after con vergence the energy is about $0.35 eV$ lower than at $6.0 a_{0}$ . This incorrect behaviour is explained as follows: At intermediate distances $(4-6 a_{0})$ the wave function is essentially a mixture of the $M_{L}=0$ and $M_{L}=1$ asymptotic states. At about $6 a_{0}$ the asymptotic energy is practically achieved and the two statesbecome degenerate. At larger distances the $M_{L}=0$ state $|z_{0}^{2}^{3}(x_{0} y_{0})^{3}(x_{C} y_{C})|^{1} \Sigma^{+}$  yields a slightly lower energy $(\cong 0.04 eV)$ than the $M_{L}=1$ state

$$\left|x_{0}{ }^{2}{ }^{3}\left(y_{0} z_{0}\right){ }^{3}\left(y_{\mathrm{C}} z_{\mathrm{C}}\right)+y_{0}{ }^{2}{ }^{3}\left(x_{0} z_{0}\right){ }^{3}\left(x_{\mathrm{C}} z_{\mathrm{C}}\right)\right|^{1} \Sigma^{+}$$

which is due to the equivalence restriction imposed on the $\pi_{x}$ and $\pi_{y}$ orbitals. Hence, at distances $\geqslant 6.5 a_{0}$ the contributions of the $M_{L}=1$ state vanish. In order to describe the $M_{L}=0$ state alone the $6 \sigma$ orbital is no longer needed, provided the $5 \sigma$ orbital becomes a localized $2 p_{\sigma}(O)$ orbital. In fact, this change from a delocalized to a localized orbital description takes place at $6.5 a_{0}$ . Thereby the $6 \sigma$ orbital becomes essentially a $3 p_{\sigma}(O)$ orbital, which is used to correlate the $2 p_{\sigma}(O)$ electrons; this correlation yields the energy lowering.

Obviously, the energy obtained when coming in small steps from shorter distances corresponds at $6.0\ a_0$ to a local minimum with respect to the orbital rotations. On the other hand, if the asymptotic (lower) valley is followed to shorter distances, the original potential curve is crossed at $4.7\ a_0$. Proceeding in small steps we can again follow a local minimum up to $4.4\ a_0$. Going on to $4.2\ a_0$ the energy changes discontinuously and we finally obtain the same result as if we come from short distances.

There are two possible ways to prevent the orbital reorganization at $6.5\ a_0$ and to obtain a smooth potential function. The first, which has been applied by KDL, is to include only those configurations in the MCSCF wavefunction which are needed to represent the $M_L=1$ asymptotic state in a delocalized orbital description. The remaining configurations can then be included in a final CI calculation without reoptimization of the orbitals. This procedure is expected to yield reasonable results at large distances. At intermediate distances, however, some of the configurations which are omitted in the MCSCF function become quite important. This may lead to larger errors unless all singly substituted configurations with respect to the complete reference function are included (as is the case in the FOCI wavefunction). A second possibility, which is applied in this work, is to fully optimize all configurations as far as possible, i.e. up to $6\ a_0$. At larger distances we optimize an energy average of the two lowest $^1\Sigma^+$ states, i.e. $E_{\text{AV}}=W_1E_1+W_2E_2$. In this way the role of the $6\sigma$ orbital can be controlled since it is required for the second state. In order to keep the second state down only a very small weight, $W_2/W_1=0.001$, is needed. With these weight factors we obtain at $6.0\ a_0$ practically the same results as with $W_2=0$ (the energy changes by less than $10^{-6}\ E_{\text{h}}$ and the dipole moment by less than $10^{-4}\ ea_0$) and a smooth potential function is obtained. However, as already mentioned, the two asymptotic states are not exactly degenerate as they should be. Therefore, the mixing of the two states at $r>6\ a_0$ is not properly accounted for and no reliable dipole moments are obtained. In fact, since at large distances the MCSCF wavefunction represents the pure $M_L=0$ state, the polarity $\text{C}^{\delta-}\text{O}^{\delta+}$ is obtained for $r\geqslant6.5\ a_0$, which is due to electron donation from the doubly occupied $p_\sigma(\text{O})$ orbital to the empty $p_\sigma(\text{C})$ orbital.

## 3. RESULTS

The calculated molecular constants are compared with experimental and some previously published values in table 1. The MCSCF results obtained with both basis sets are nearly of the same quality. The calculated equilibrium distances deviate from the experimental value by only $0.001\ \text{Å}$; the harmonic frequencies obtained are about $36\ \text{cm}^{-1}$ too large. In accordance with the SD-CI results of KDL [49] and the PNO-CI values of Jaquet *et al.* [63] the SCEP/VAR (SD-CI) method yields an equilibrium distance which is too short and an $\omega_{\text{e}}$ which is considerably too large. In contrast, the SCEP/CEPA and PNO/CEPA methods as well as the VCI and FOCI calculations yield quite accurate $\omega_{\text{e}}$ values but the equilibrium distances are somewhat too large. This reflects the general trend that for too small $r_{\text{e}}$, $\omega_{\text{e}}$ is often calculated too large and *vice versa*. The MCSCF calculations yield a dissociation energy which is $0.3\ \text{eV}$ too large. This error is probably due to the neglect of the correlation of the $2s$ electrons. In particular, for the carbon atom the addition of

<table>
<thead>
  <tr>
    <th>Method</th>
    <th>Ref.</th>
    <th>$r_\text{e}/$\AA</th>
    <th>$B_\text{e}/\text{cm}^{-1}$</th>
    <th>$\alpha_\text{e}/\text{cm}^{-1}$</th>
    <th>$\omega_\text{e}/\text{cm}^{-1}$</th>
    <th>$\omega_\text{e}x_\text{e}/\text{cm}^{-1}$</th>
    <th>$D_\text{e}/\text{eV}$</th>
    <th>$M_\text{e}/\text{D}$</th>
    <th>$(\partial M/\partial r)_\text{e}$<br>/$\text{D}\text{\AA}^{-1}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>SCEP/VAR ($a$)</td>
    <td>This work</td>
    <td>1·123</td>
    <td>1·948</td>
    <td>−0·0158</td>
    <td>2260·8</td>
    <td>10·9</td>
    <td></td>
    <td>−0·0806</td>
    <td>3·47</td>
  </tr>
  <tr>
    <td>SCEP/CEPA ($a$)</td>
    <td>This work</td>
    <td>1·132</td>
    <td>1·918</td>
    <td>−0·0169</td>
    <td>2174·9</td>
    <td>12·3</td>
    <td></td>
    <td>−0·270</td>
    <td>2·45</td>
  </tr>
  <tr>
    <td>MCSCF(30) ($a$)</td>
    <td>This work</td>
    <td>1·129</td>
    <td>1·928</td>
    <td>−0·0166</td>
    <td>2206·8</td>
    <td>12·8</td>
    <td>11·50</td>
    <td>−0·230</td>
    <td>3·08</td>
  </tr>
  <tr>
    <td>MCSCF(30) ($b$)</td>
    <td>This work</td>
    <td>1·127</td>
    <td>1·935</td>
    <td>−0·0170</td>
    <td>2205·8</td>
    <td>12·8</td>
    <td>11·52</td>
    <td>−0·236</td>
    <td>3·17</td>
  </tr>
  <tr>
    <td>Exp.</td>
    <td>11, 35, 69</td>
    <td>1·128</td>
    <td>1·931</td>
    <td>−0·0175</td>
    <td>2169·8</td>
    <td>13·29</td>
    <td>11·23</td>
    <td>−0·1222</td>
    <td>3·14</td>
  </tr>
  <tr>
    <td>VCI ($c$)</td>
    <td>49</td>
    <td>1·133</td>
    <td>1·913</td>
    <td>−0·0171</td>
    <td>2154·2</td>
    <td>12·95</td>
    <td>11·32</td>
    <td>−0·260</td>
    <td>3·26</td>
  </tr>
  <tr>
    <td>FOCI ($d$)</td>
    <td>49</td>
    <td>1·133</td>
    <td>1·915</td>
    <td>−0·0168</td>
    <td>2166·3</td>
    <td>12·85</td>
    <td>11·72</td>
    <td>−0·319</td>
    <td>2·98</td>
  </tr>
  <tr>
    <td>SD-CI ($e$)</td>
    <td>49</td>
    <td>1·120</td>
    <td>1·958</td>
    <td>−0·0160</td>
    <td>2258·9</td>
    <td>11·50</td>
    <td></td>
    <td>−0·0821</td>
    <td>3·53</td>
  </tr>
  <tr>
    <td>PNO-CI ($f$)</td>
    <td>63</td>
    <td></td>
    <td></td>
    <td></td>
    <td>2264·0</td>
    <td>13·68</td>
    <td></td>
    <td>−0·117</td>
    <td></td>
  </tr>
  <tr>
    <td>PNO-CEPA ($f$)</td>
    <td>63</td>
    <td>1·137</td>
    <td>1·901</td>
    <td></td>
    <td>2167·3</td>
    <td>14·96</td>
    <td></td>
    <td>−0·275</td>
    <td></td>
  </tr>
  <tr>
    <td>DPT ($g$)</td>
    <td>70</td>
    <td>1·125</td>
    <td>1·943</td>
    <td>−0·0156</td>
    <td>2247</td>
    <td>12·16</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

(a) Basis 9/5/2, see text. (b) Basis 11/6/3, see text. (c) Valence CI. (d) First order CI. (e) Singles-doubles CI. (f) Pseudo natural orbital CI and coupled electron pair approximation. (g) Third order diagrammatic perturbation theory.

the configuration $2p^4 \, (^3P)$ to the Hartree-Fock configuration $2s^2 \, 2p^2 \, (^3P)$ would lower the energy by about 0·5 eV.

The calculated dipole ...oments are presented in table 2 and compared graphically with the empirical dipole moment functions in the figure. The calculated EDMF is shifted with respect to the experimental function by about

<table>
<thead>
  <tr>
    <th>$r/a_0$</th>
    <th>SCEP/VAR‡</th>
    <th>SCEP/CEPA‡</th>
    <th>MCSCF(30)‡</th>
    <th>MCSCF(30)§</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1·5</td>
    <td></td>
    <td></td>
    <td>−0·4682</td>
    <td>−0·4766</td>
  </tr>
  <tr>
    <td>1·6</td>
    <td></td>
    <td></td>
    <td>−0·4169</td>
    <td>−0·4249</td>
  </tr>
  <tr>
    <td>1·7</td>
    <td></td>
    <td></td>
    <td>−0·3610</td>
    <td>−0·3685</td>
  </tr>
  <tr>
    <td>1·8</td>
    <td>−0·2644</td>
    <td>−0·2865</td>
    <td>−0·3014</td>
    <td>−0·3083</td>
  </tr>
  <tr>
    <td>1·9</td>
    <td>−0·1967</td>
    <td>−0·2307</td>
    <td>−0·2393</td>
    <td>−0·2452</td>
  </tr>
  <tr>
    <td>2·0</td>
    <td>−0·1265</td>
    <td>−0·1756</td>
    <td>−0·1755</td>
    <td>−0·1802</td>
  </tr>
  <tr>
    <td>2·13183</td>
    <td>−0·03172</td>
    <td>−0·1064</td>
    <td>−0·09059</td>
    <td>−0·09306</td>
  </tr>
  <tr>
    <td>2·3</td>
    <td>0·09053</td>
    <td>−0·02816</td>
    <td>0·01589</td>
    <td>0·01720</td>
  </tr>
  <tr>
    <td>2·5</td>
    <td>0·2336</td>
    <td>0·04344</td>
    <td>0·1344</td>
    <td>0·1416</td>
  </tr>
  <tr>
    <td>2·8</td>
    <td></td>
    <td></td>
    <td>0·2822</td>
    <td>0·3005</td>
  </tr>
  <tr>
    <td>3·1</td>
    <td></td>
    <td></td>
    <td>0·3806</td>
    <td>0·4104</td>
  </tr>
  <tr>
    <td>3·4</td>
    <td></td>
    <td></td>
    <td>0·4373</td>
    <td>0·4758</td>
  </tr>
  <tr>
    <td>3·7</td>
    <td></td>
    <td></td>
    <td>0·4521</td>
    <td>0·4979</td>
  </tr>
  <tr>
    <td>4·0</td>
    <td></td>
    <td></td>
    <td>0·4163</td>
    <td>0·4688</td>
  </tr>
  <tr>
    <td>4·5</td>
    <td></td>
    <td></td>
    <td>0·2848</td>
    <td>0·3359</td>
  </tr>
  <tr>
    <td>5·0</td>
    <td></td>
    <td></td>
    <td>0·1553</td>
    <td>0·1958</td>
  </tr>
  <tr>
    <td>5·5</td>
    <td></td>
    <td></td>
    <td>0·0747</td>
    <td>0·1057</td>
  </tr>
  <tr>
    <td>6·0</td>
    <td></td>
    <td></td>
    <td>0·0251</td>
    <td>0·0526</td>
  </tr>
</tbody>
</table>

† In $ea_0$, $1 \, ea_0$=2·54158 D, positive sign corresponds to polarity C⁺O⁻.
‡ Basis 9/5/2, see text.
§ Basis 11/6/3, see text.

![](./images/812082013841391617_2.jpg)

Comparison of empirical (a, b) and computed (c, d) dipole moment functions of CO.
(a) [37], ---: Padé approximant with coefficients $C_{1}$ to $C_{5}$ as given in [37], $C_{\infty}=0 \cdot 1 ; \cdot-\cdot-$ : Padé approximant with same $C_{1}$ to $C_{5}$ but $C_{\infty}=1 \cdot 175$. This value was fitted to the computed dipole moment at $6.0 a_{0}$. (b) Five term power series expansion, [35]. (c) MCSCF (30), basis 11/6/3. (d) FOCI, [49]. The vertical bar indicates the equilibrium distance, the horizontal bars indicate the classical turning points for the specified vibrational states.

<table>
<caption>Table 3. Comparison of calculated and experimental rotationless dipole matrix elements for the ground state of CO (in D).</caption>
<thead>
<tr>
<th>$v'$</th>
<th>$v''$</th>
<th>MCSCF(30)(a)</th>
<th>MCSCF(30)(b)</th>
<th>MCSCF(30)(c)</th>
<th>Experimental</th>
<th>Empirical(d)</th>
<th>FOCI(e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0·1029</td>
<td>0·1061</td>
<td>0·1070</td>
<td>0·1055 (f)</td>
<td>0·1055</td>
<td>0·100</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>$-0\cdot 6233-2$</td>
<td>$-0\cdot 6167-2$</td>
<td>$-0\cdot 6415-2$</td>
<td>$-0\cdot 653-2$ (g)</td>
<td>$-0\cdot 657-2$</td>
<td>$-0\cdot 610-2$</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$-0\cdot 639-2$ (h)</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$-0\cdot 661-2$ (i)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>0·3705-3</td>
<td>0·3468-3</td>
<td>0·3735-3</td>
<td>0·424-3 (g)</td>
<td>0·424-3</td>
<td>0·36-3</td>
</tr>
<tr>
<td>4</td>
<td>0</td>
<td>$-0\cdot 2342-4$</td>
<td>$-0\cdot 2093-4$</td>
<td>$-0\cdot 1837-4$</td>
<td>$-0\cdot 201-4$ (h)</td>
<td>$-0\cdot 201-4$</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>0</td>
<td>0·7008-6</td>
<td>0·6960-6</td>
<td>0·7777-6</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>$-0\cdot 1099-1$</td>
<td>$-0\cdot 1089-1$</td>
<td>$-0\cdot 1129-1$</td>
<td>$-0\cdot 126-1$ (h)</td>
<td>$-0\cdot 1151-1$</td>
<td>$-0\cdot 107-1$</td>
</tr>
<tr>
<td>4</td>
<td>2</td>
<td>$-0\cdot 1575-1$</td>
<td>$-0\cdot 1561-1$</td>
<td>$-0\cdot 1618-1$</td>
<td>$-0\cdot 148-1$ (h)</td>
<td>$-0\cdot 1647-1$</td>
<td>$-0\cdot 153-1$</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>$-0\cdot 2057-1$</td>
<td>$-0\cdot 2039-1$</td>
<td>$-0\cdot 2118-1$</td>
<td>$-0\cdot 230-1$ (h)</td>
<td>$-0\cdot 2150-1$</td>
<td>$-0\cdot 201-1$</td>
</tr>
<tr>
<td>6</td>
<td>4</td>
<td>$-0\cdot 2553-1$</td>
<td>$-0\cdot 2529-1$</td>
<td>$-0\cdot 2628-1$</td>
<td>$-0\cdot 264-1$ (i)</td>
<td>$-0\cdot 2662-1$</td>
<td></td>
</tr>
</tbody>
</table>

(a) Basis 9/5/2, evaluated with computed potential function. (b) Basis 11/6/3, evaluated with computed potential function. (c) Basis 11/6/3, evaluated with RKR potential function. (d) [35] from empirical dipole moment function fitted to the listed values of $M_{0}{}^{n}$. (e) [49] dipole moments from FOCI wavefunctions, matrix elements evaluated with RKR potential function. (f) [39]. (g) [33]. (h) [46]. (i) [42].

0·1 D to more negative values. Due to the orthogonality of the vibrational wavefunctions this shift has no influence on the calculated off-diagonal dipole matrix elements (the effect on matrix elements of vibration-rotation transitions with $J=\pm 1$ is negligible). In contrast, the first derivative of the EDMF at $r_{e}$, which mainly determines the vibrational matrix elements of the funda- mental series, is in excellent agreement with the experimental value (see table1). As observed from the figure the calculated and empirical dipole moment functions closely parallel each other up to a distance of about $2.8 a_{0}$ . The calculated EDMF has a maximum at about $3.7 a_{0}$ and falls off smoothly to zero at larger distances. With the exception of the Padé approximant of Kirschner et al. [37], the experimental functions do not show the correct long range behaviour. Kirschner et al. fitted the coefficients $C_{1}$ to $C_{5}$ of (1) to a five term power series expansion, thereby ignoring the long range term $C_{\infty} x^{6}$ . They proposed to fit $C_{\infty}$ to ab initio results at large distances. Following this sug gestion we obtain $C_{\infty}=1 \cdot 175$ , a much larger value than that estimated by Kirschner et al. The corresponding dipole moment function is also shown in the figure. We do not believe, however, that this approximation yields very reliable results at intermediate distances, since due to the procedure adopted for the determination of the coefficients $C_{1}$ to $C_{5}$ the Padé approximant closely follows the power series up to too large a distance. Hence, in the region around $3.5 a_{0}$ the dipole moments are probably too large.

Using Cooley's method [72] from the computed potential energy and dipole moment functions vibrational dipole matrix elements have been evaluated, which provide the most direct comparison with experimental data. In table 3 the calculated matrix elements for the fundamental and various overtone transitions are compared with experimental and empirical values and with the FOCI results of KDL. In the first two columns the values obtained with the smaller and larger basis sets are compared. For the fundamental and first overtone bands the results are not very different. The matrix elements $M_{0}^{3}$ and $M_{0}^{4}$ , however, are more sensitive to small changes of the potential and dipole moment functions and differ for both basis sets by about 10 per cent. In order to eliminate the errors due to inaccuracies of the computed potential function the RKR potential function [20] can be used. (With this function we reproduced the experimental term values up to v=36 within $1 cm^{-1}$ .) The corresponding dipole matrix elements for the larger basis set are listed in the third column of table 3. Again the change of the matrix element $R_{0}^{1}$ is small, but the influence on the overtone transitions is appreciable. We found that the matrix elements $M_{0}^{n}, n>2$ , depend quite sensitively on small shifts of the dipole moment function to shorter or longer distances. This is attributed to the fact that the dipole moment function has a point of inflection near $r_{e}$ and, hence, a small shift can influence the second derivative $(d^{2} M / d r^{2})_{r_{e}}$ drastically. This is probably the main reason for the differences of the matrix elements in the second and third column of table 3. The calculated matrix elements for the fundamental and first overtone bands are in excellent agreement with the empirical matrix elements of Chackerian [35], Tipping [36] or others [37, 38]. The empirical values had been obtained from the experimental dipole moment functions, which are fitted such that the matrix elements $M_{0}^{n}, n ≤4$ , are repro duced (the agreement of the experimental and empirical $M_{0}^{n}$ values is therefore meaningless). The non-systematic deviations of the theoretical and empirical

matrix elements $M_n^{n+2}$ from the experimental data reveal an uncertainty of about 10 per cent for the latter values. Obviously, the ab initio values are of much higher accuracy. The FOCI results of KDL are somewhat less reliable than our values : they deviate by 5-7 per cent from the empirical values and the MCSCF(30) results.

Table 4. Comparison of calculated and experimental dipole matrix elements for the fundamental sequence of CO (in D).

<table>
  <thead>
    <tr>
      <th>$v'$</th>
      <th>$J'$</th>
      <th>$v''$</th>
      <th>$J''$</th>
      <th>MCSCF(30)†</th>
      <th>Exp.‡</th>
      <th>Empirical§</th>
      <th>Empirical∥</th>
      <th>FOCI¶</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0·1070</td>
      <td>0·1055</td>
      <td>0·1055</td>
      <td>0·1055</td>
      <td>0·100</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0·1512</td>
      <td></td>
      <td>0·1490</td>
      <td>0·149</td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0·1849</td>
      <td></td>
      <td>0·1822</td>
      <td>0·182</td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0·2132</td>
      <td></td>
      <td>0·2100</td>
      <td>0·211</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0·2379</td>
      <td></td>
      <td>0·2343</td>
      <td>0·235</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>11</td>
      <td>4</td>
      <td>12</td>
      <td>0·2377</td>
      <td>0·238 ± 0·003</td>
      <td>0·2345</td>
      <td>0·235</td>
      <td>0·223</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>5</td>
      <td>11</td>
      <td>0·2600</td>
      <td>0·259 ± 0·002</td>
      <td>0·2565</td>
      <td>0·258</td>
      <td>0·244</td>
    </tr>
    <tr>
      <td>7</td>
      <td>8</td>
      <td>6</td>
      <td>9</td>
      <td>0·2802</td>
      <td>0·277 ± 0·002</td>
      <td>0·2765</td>
      <td>0·278</td>
      <td>0·262</td>
    </tr>
    <tr>
      <td>8</td>
      <td>7</td>
      <td>7</td>
      <td>8</td>
      <td>0·2988</td>
      <td>0·295 ± 0·002</td>
      <td>0·2951</td>
      <td>0·297</td>
      <td>0·280</td>
    </tr>
    <tr>
      <td>9</td>
      <td>10</td>
      <td>8</td>
      <td>11</td>
      <td>0·3161</td>
      <td>0·313 ± 0·003</td>
      <td>0·3126</td>
      <td>0·314</td>
      <td>0·296</td>
    </tr>
    <tr>
      <td>10</td>
      <td>11</td>
      <td>9</td>
      <td>12</td>
      <td>0·3322</td>
      <td>0·326 ± 0·004</td>
      <td>0·3291</td>
      <td>0·331</td>
      <td>0·311</td>
    </tr>
    <tr>
      <td>11</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>0·3472</td>
      <td>0·344 ± 0·005</td>
      <td>0·3445</td>
      <td>0·347</td>
      <td></td>
    </tr>
    <tr>
      <td>16</td>
      <td>12</td>
      <td>15</td>
      <td>11</td>
      <td>0·4064</td>
      <td></td>
      <td>0·4011</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>21</td>
      <td>12</td>
      <td>20</td>
      <td>11</td>
      <td>0·4463</td>
      <td></td>
      <td>0·4446</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>21</td>
      <td>21</td>
      <td>20</td>
      <td>20</td>
      <td>0·4446</td>
      <td></td>
      <td>0·4426</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>26</td>
      <td>12</td>
      <td>25</td>
      <td>11</td>
      <td>0·4698</td>
      <td></td>
      <td>0·4742</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>31</td>
      <td>12</td>
      <td>30</td>
      <td>11</td>
      <td>0·4787</td>
      <td></td>
      <td>0·4908</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>31</td>
      <td>21</td>
      <td>30</td>
      <td>20</td>
      <td>0·4746</td>
      <td></td>
      <td>0·4862</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>36</td>
      <td>12</td>
      <td>35</td>
      <td>11</td>
      <td>0·4728</td>
      <td></td>
      <td>0·4951</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>36</td>
      <td>21</td>
      <td>35</td>
      <td>20</td>
      <td>0·4671</td>
      <td></td>
      <td>0·4889</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

† Basis 11/6/3, evaluated with RKR potential function.
‡ Weisbach, M. F., and Chackerian, C. [40].
§ Chackerian, C. [35].
∥ Tipping, R. H. [36].
¶ First order CI [49].

In table 4 a number of calculated matrix elements for the fundamental sequence, which are of interest for laser transitions, are compared with available experimental and empirical values. The empirical matrix elements obtained by various authors are virtually identical, which is not surprising since the corresponding dipole moment functions have been fitted to the same set of known intensities. For transitions involving vibrational quantum numbers up to about 25 our ab initio results are in excellent agreement with all experi- mental and empirical values. For larger quantum numbers, however, the deviations between the empirical values of Chackerian [35] and our results increase up to about 5 per cent for $v'=36$. For these transitions the theo- retical EDMF yields smaller matrix elements than the empirical EDMF. This is probably due to the fact that the empirical function diverges for $x>0.5$ from the correct function and shows no maximum (the empirical values for $v''>11$

have therefore been regarded by Chackerian as estimates only, but due to the fact that they are predominantly determined by the first derivative of the EDMF at $r_{\mathrm{e}}$ they are accurate for quantum numbers up to about 25). For transitions involving vibrational quantum numbers larger than 25 we believe that our theoretical matrix elements are more accurate than those derived from the empirical dipole moment functions and to be the most reliable presently available.

Table 5. Calculated Einstein coefficients of spontaneous emission (in $\mathrm{s}^{-1}$).

<table>
  <thead>
    <tr>
      <th rowspan="2">$v'$</th>
      <th colspan="3">$\Delta v$</th>
    </tr>
    <tr>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>35·3</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>68·0</td>
      <td>1·00</td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>97·9</td>
      <td>2·98</td>
      <td>0·011</td>
    </tr>
    <tr>
      <td>5</td>
      <td>150·2</td>
      <td>9·71</td>
      <td>0·121</td>
    </tr>
    <tr>
      <td>10</td>
      <td>240·0</td>
      <td>40·7</td>
      <td>1·67</td>
    </tr>
    <tr>
      <td>15</td>
      <td>278·4</td>
      <td>87·5</td>
      <td>6·53</td>
    </tr>
    <tr>
      <td>20</td>
      <td>276·1</td>
      <td>142·6</td>
      <td>16·7</td>
    </tr>
    <tr>
      <td>25</td>
      <td>247·0</td>
      <td>193·8</td>
      <td>35·5</td>
    </tr>
    <tr>
      <td>30</td>
      <td>203·4</td>
      <td>229·2</td>
      <td>63·5</td>
    </tr>
    <tr>
      <td>35</td>
      <td>154·7</td>
      <td>243·4</td>
      <td>96·2</td>
    </tr>
  </tbody>
</table>

In table 5 some calculated Einstein coefficients of spontaneous emission are compared for the fundamental and first two overtone sequences. For the fundamental band the transition probability increases with increasing $v'$ by a factor of about 8 up to $v'=17$ but due to the decreasing transition frequency, which enters cubically in the coefficients, it decreases for larger quantum numbers. The intensities of the overtone transitions also increase strongly with increasing $v'$. For transitions with $v'\geqslant 28$ the $\Delta v=2$ lines are predicted to be more intense than the $\Delta v=1$ ones. The strongest increase of the intensity with increasing vibrational quantum number is predicted for the $\Delta v=3$ transitions : in this case the Einstein coefficient for $v'=35$ is about $10^{4}$ times larger than that for $v'=3$. Due to the sensitivity of these values with respect to the curvature of the dipole moment function the coefficients for the $\Delta v=3$ transitions are expected to be somewhat less reliable than those of the fundamental and first overtone sequences and should be regarded as estimates only.

The author wishes to thank Professors E.-A. Reinsch and W. Meyer for many stimulating and helpful discussions. The computer facilities of the Hochschulrechenzentrum der Universität Frankfurt and the Hochschulrechenzentrum der Technischen Hochschule Darmstadt are acknowledged.

## REFERENCES

[1] MAILLARD, J. P., 1974, *Highlights of Astronomy*, edited by G. Contopoulos (D. Reidel, Dordrecht), pp. 313-320.

[2] MULLER, C., and SAUVAL, A. J., 1975, *Astron. Astrophys.*, **39**, 445. HALL, D. N. B., NOYES, R. W., and AYRES, T. R., 1972, *Astrophys. J.*, **171**, 615. HALL, D. N. B., 1973, *Astrophys. J.*, **182**, 977.

[3] GUELACHEVILI, G., 1973, *Optics Commun.*, **8**, 171.

[4] ENG, R. S., KIDAL, H., MIKKELSEN, J. C., and SPEARS, D. L., 1974, *Appl. Phys. Lett.*, **24**, 231.

[5] WHITFORD, B. G., SIEMSEN, K. J., and RICCUS, N. D., 1974, *Optics Commun.*, **10**, 288.

[6] ROH, W. B., and RAO, K. N., 1974, *J. molec. Spectrosc.*, **49**, 317.

[7] JOHNES, J. W. C., MCKELLAR, A. R. W., and WEITZ, D., 1974, *J. molec. Spectrosc.*, **51**, 539.

[8] MANTZ, A. W., and MAILLARD, J. P., 1974, *J. molec. Spectrosc.*, **53**, 446.

[9] KIDAL, H., ENG, R. S., and ROSS, A. H. M., 1974, *J. molec. Spectrosc.*, **53**, 479.

[10] ROSS, A. H. M., ENG, R. S., and KIDAL, H., 1974, *Optics Commun.*, **12**, 433.

[11] MANTZ, A. W., MAILLARD, J. P., ROH, W. B., and RAO, K. N., 1975, *J. molec. Spectrosc.*, **57**, 155.

[12] TODD, T. R., CLAYTON, C. M., TELFAIR, W. B., MCCUBBIN, T. K. JR., and PLIVA, J., 1976, *J. molec. Spectrosc.*, **62**, 201.

[13] CHEN, D. W., RAO, K. N., and MCDOWELL, R. S., 1976, *J. molec. Spectrosc.*, **61**, 71.

[14] OGILVIE, J. F., 1978, *J. molec. Spectrosc.*, **69**, 169.

[15] GUELACHIVI, G., 1979, *J. molec. Spectrosc.*, **75**, 251.

[16] KIDAL, H., and MIKKELSEN, J. C., 1973, *Optics Commun.*, **9**, 315.

[17] RAMSAY, D. (editor), 1976, *Physical Chemistry, Ser. 2, Vol. 3* (Butterworth), p. 352.

[18] RYDBERG, R., 1931, *Z. Phys.*, **73**, 376 ; 1933, **80**, 514. KLEIN, O., 1932, *Z. Phys.*, **76**, 226. REES, A. L. G., 1947, *Proc. phys. Soc.*, **59**, 998.

[19] KUPRENIE, P., and WEISSMAN, S., 1965, *J. chem. Phys.*, **43**, 1529.

[20] KIRSCHNER, S. M., and WATSON, J. K. G., 1974, *J. molec. Spectrosc.*, **51**, 321.

[21] HUFFAKER, J. N., 1977, *J. molec. Spectrosc.*, **65**, 1 ; 1978, **71**, 160.

[22] See, for instance : GROSS, R. W. F., and BOTT, J. F., (editors), 1976, *Handbook of Chemical Lasers* (Wiley).

[23] HANCOCK, G., and SMITH, I. W. M., 1971, *Trans. Faraday Soc.*, **67**, 2586. HANCOCK, G., MORLEY, C., and SMITH, I. W. M., 1971, *Chem. Phys. Lett.*, **12**, 193. HANCOCK, G., RIDLEY, B. A., and SMITH, I. W. M., 1972, *Trans. Faraday Soc.*, **68**, 2117, 2127.

[24] FOSTER, K. D., 1972, *J. chem. Phys.*, **57**, 2451.

[25] TSUCHIYA, S., NIELSEN, N., and BAUER, S. H., 1973, *J. phys. Chem.*, **77**, 2455.

[26] POWELL, H. T., and KELLEY, J. D., 1974, *J. chem. Phys.*, **60**, 2191.

[27] DJEU, N., 1974, *J. chem. Phys.*, **60**, 4109.

[28] HUDGENS, J. W., GLEAVES, and MCDONALD, J. D., 1976, *J. chem. Phys.*, **64**, 2528.

[29] TIPPING, R. H., and HERMAN, R. M., 1970, *J. molec. Spectrosc.*, **36**, 404.

[30] HERMAN, R. M., and WALLIS, R. J., 1955, *J. chem. Phys.*, **23**, 637.

[31] JACOBI, N., 1970, *J. chem. Phys.*, **52**, 2694.

[32] TIPPING, R. H., 1972, *J. molec. Spectrosc.*, **43**, 31.

[33] TOTH, R. A., HUNT, R. H., and PLYLER, E. K., 1969, *J. molec. Spectrosc.*, **32**, 74, 85 ; 1970, *Ibid.*, **35**, 110.

[34] YOUNG, L. A., and EACHUS, W. J., 1966, *J. chem. Phys.*, **44**, 4195.

[35] CHACKERIAN, C., 1976, *J. chem. Phys.*, **65**, 4228.

[36] TIPPING, R. H., 1976, *J. molec. Spectrosc.*, **61**, 272.

[37] KIRSCHNER, S. M., LEROY, R. J., OGILVIE, J. F., and TIPPING, R. H., 1977, *J. molec. Spectrosc.*, **65**, 306.

[38] BOUANICH, J. P., and BRODBECK, C., 1976, *J. quant. Spectrosc. radiat. Transfer*, **16**, 153.

[39] VARASANI, P., and SARANGI, S., 1975, *J. quant. Spectrosc. radiat. Transfer*, **15**, 473.

[40] WEISBACH, M. F., and CHACKERIAN, C. JR., 1973, *J. chem. Phys.*, **59**, 4272.

[41] ROUX, F., EFFANTIN, C., and D'INCAN, J., 1972, *J. quant. Spectrosc. radiat. Transfer*, **12**, 97.

[42] ROUX, F., CERNY, D., and D'INCAN, J., 1974, *J. quant. Spectrosc. radiat. Transfer*, **14**, 153.

[43] CRANCE, M., and VERGES, J., 1975, *J. Phys. B*, **8**, 3001.

[44] KORB, C. L., HUNT, R. H., and PLYLER, E. K., 1968, *J. chem. Phys.*, **48**, 4252.

[45] CHACKERIAN, C. JR., and VALERO, F. P. J., 1976, *J. molec. Spectrosc.*, **62**, 338.

[46] STEVENS, W. J., DAS, G., WAHL, A. C., NEUMANN, D., and KRAUSS, M., 1974, *J. chem. Phys.*, **61**, 3686.

[47] CHU, S. I., YOSHIMINE, M., and LIU, B., 1974, *J. chem. Phys.*, **61**, 5389.

[48] MEYER, W., and ROSMUS, P., 1975, *J. chem. Phys.*, **63**, 2356.

[49] KIRBY-DOCKEN, K., and LIU, B., 1977, *J. chem. Phys.*, **66**, 4309.

[50] KIRBY, K., and LIU, B., 1978, *J. chem. Phys.*, **69**, 200.

[51] WERNER, H.-J., and ROSMUS, P., 1980, *J. chem. Phys.*, **73**, 2319.

[52] WERNER, H.-J., REINSCH, E.-A., and ROSMUS, P., 1981, *Chem. Phys. Lett.*, **78**, 311.

[53] WERNER, H.-J., and MEYER, W., 1981, *J. chem. Phys.*, **74**, 5802.

[54] NESBET, R. K., 1964, *J. chem. Phys.*, **40**, 3619.

[55] HUO, W. M., 1965, *J. chem. Phys.*, **43**, 624.

[56] BILLINGSLEY II, F. P., and KRAUSS, M., 1974, *J. chem. Phys.*, **60**, 4130.

[57] MEYER, W., 1976, *J. chem. Phys.*, **64**, 2901.

[58] MEYER, W., 1971, *Int. J. quant. Chem.*, **55**, 341.

[59] MEYER, W., 1973, *J. chem. Phys.*, **58**, 1017.

[60] AHLRICHS, R., LISCHKA, H., STAEMMLER, V., and KUTZELNIGG, W., 1975, *J. chem. Phys.*, **62**, 1225.

[61] MEYER, W., 1977, *Modern Theoretical Chemistry* edited by H. F. Schaefer (Plenum) ; KUTZELNIGG, W., *Ibid.*

[62] WERNER, H.-J., and MEYER, W., 1976, *Molec. Phys.*, **31**, 855.

[63] JACQUET, R., KUTZELNIGG, W., and STAEMMLER, V., 1980, *Theor. chim. Acta*, **54**, 205.

[64] MEYER, W., and ROSMUS, P. (private communication).

[65] COOPER, D. M., and LANGHOFF, S. R., 1981, *J. chem. Phys.*, **74**, 1200.

[66] HUZINAGA, S., 1965, Technical Report, Department of Chemistry, University of Alberta, Alberta, U.S.A.

[67] SIU, A. K. Q., and DAVIDSON, E. R., 1970, *Int. J. quant. Chem.*, **4**, 223.

[68] WERNER, H.-J., and MEYER, W., 1980, *J. chem. Phys.*, **73**, 2342.

[69] WERNER, H.-J., and MEYER, W., 1981, *J. chem. Phys.*, **74**, 5794, and references cited therein.

[70] DOUGLAS, A. E., and MOLLER, C. K., 1955, *Can. J. Phys.*, **33**, 125.

[71] WILSON, S., 1977, *Int. J. quant. Chem.*, **12**, 609.

[72] COOLEY, J. W., 1961, *Math. Comput.*, **15**, 363.