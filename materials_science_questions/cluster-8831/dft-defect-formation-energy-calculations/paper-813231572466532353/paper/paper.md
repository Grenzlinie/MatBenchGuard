# Simulation Studies of the Phase Stability of the $\boldsymbol{Sr_{n+1}Ti_nO_{3n+1}}$ Ruddlesden-Popper Phases

Amr H. H. Ramadan, $^{\ddagger}$ Neil L. Allan, $^{\S}$ and Roger A. De Souza $^{\ddagger,\dagger}$

$^{\ddagger}$Institute of Physical Chemistry and JARA-FIT, RWTH Aachen University, Aachen 52056, Germany
$^{\S}$University of Bristol, Centre for Computational Chemistry, Bristol, BS8 1TS, United Kingdom

Atomistic simulation techniques are used to examine the stability of Ruddlesden-Popper (R-P) phases $Sr_{n+1}Ti_nO_{3n+1}$ ($n = 1$, 2, 3, 4 and $\infty$). Various sets of empirical pair potentials are employed to determine the formation energies of the R-P phases. Formation energies are also calculated with Density Functional Theory (DFT). The tendency of a given R-P phase to dissociate into a lower order R-P phase plus $SrTiO_3$ perovskite is found to increase with increasing $n$. The results obtained are compared with experiment and previous computational studies. The stability of intergrowth phases with respect to the pure R-P compounds is examined. In all cases the intergrowths are calculated to be thermodynamically less stable than the pure R-P phase, but the differences are in some cases negligible. Finally, the energy for SrO partial Schottky disorder in strontium titanate is computed taking the formation of R-P phases into account.

## I. Introduction

T HE perovskite oxide $SrTiO_3$ can accommodate small deviations from nominal cation stoichiometry, $0.995 \leq SrO/TiO_2 \leq 1.002$, and remain a single-phase, cubic perovskite. $^1$ For $SrO/TiO_2 < 0.995$, $TiO_2$ is exsolved as a second phase. In contrast, for $SrO/TiO_2 > 1.002$ the excess SrO is accommodated by the formation of Ruddlesden-Popper (R-P) phases of general composition $Sr_{n+1}Ti_nO_{3n+1}$. $^{2,3}$ Understanding the relative stability of R-P phases is of considerable importance in optimizing the different R-P phases for dielectric applications $^4$ or for use as resistive switches. $^5$

Experimentally there has been no success in preparing phase-pure R-P compounds with $n > 3$ by conventional solid-state methods; such samples consist of several R-P phases of different $n$ in the form of intergrowths. $^{6,7,8,9}$ Theoretical studies, devoted to the calculation of the formation energies of the R-P phases, have been of little help as they provide no consensus as to the relative stability of the various R-P phases. $^{10,11,12,13,14}$ In this study, we use static lattice calculations, based on various sets of empirical Pair Potentials (EPP) or Density Functional Theory (DFT), to study the energetics of R-P phases.

$SrTiO_3$ can itself become nonstoichiometric. The most favorable disorder type, according to both experiment $^{15,16}$ and theory, $^{17,18}$ is partial SrO-Schottky disorder

$$\text{Sr}_{\text{Sr}}^{\times} + \text{O}_{\text{O}}^{\times} \rightleftharpoons \text{V}_{\text{Sr}}'' + \text{V}_{\text{O}}^{\cdot\cdot} + \text{SrO}, \tag{1}$$

with disorder energy $U_{\text{Sch}}$. There is, however, a discrepancy between theoretical values for $U_{\text{Sch}}$, which are in the range 3.06-4.85 eV, $^{17,18,19,20}$ and the experimental value determined by Moos and Härdtl of 2.5 eV. $^{15}$ Below we reexamine this problem, taking into account that a more favorable reaction than (1) may be the formation of an R-P phase according to

$$\text{Sr}_{\text{Sr}}^{\times} + \text{O}_{\text{O}}^{\times} + n\ \text{SrTiO}_3 \rightleftharpoons \text{V}_{\text{Sr}}'' + \text{V}_{\text{O}}^{\cdot\cdot} + \text{Sr}_{n+1}\text{Ti}_n\text{O}_{3n+1}. \tag{2}$$

### Structure of Sr-Ti-O Ruddlesden-Popper phases

R-P phases have the general formula $SrO \cdot n\ SrTiO_3$ and are structures comprising of alternating $TiO_2$ and SrO layers with an additional rock-salt layer every $n$th SrO layer. The additional rock-salt layer causes a displacement of the following layers by $\begin{bmatrix} \frac{1}{2} \frac{1}{2} 0 \end{bmatrix}$ in comparison with the expected perovskite structure (see Fig. 1).

In this study we use the following naming convention. The pure R-P phase of the formula $Sr_{n+1}Ti_nO_{3n+1}$ is denoted by $\mathbf{n}_\text{p}$ (the subscript $p$ referring to the pure phase). For an intergrowth phase consisting of $n'$ and $n''$ of overall composition $n$, we use $\mathbf{n}_{\text{i}(n',n'')}$. For example $\mathbf{2}_{\text{i}(1,3)}$ refers to an intergrowth of $Sr_2TiO_4(\mathbf{1}_\text{p})$ and $Sr_4Ti_3O_{10}(\mathbf{3}_\text{p})$ with the overall stoichiometric composition of $2Sr_3Ti_2O_7$ (2). It is noted that $\mathbf{2}_{\text{i}(0,4)}$ corresponds nominally to phase separation, that is, alternating blocks of $4SrTiO_3$ and 2 SrO (examples are shown in Fig. 1).

## II. Atomistic simulation methodology

R-P compounds in the $SrO-TiO_2$ system were modeled with classical and quantum mechanical methods. In the former the lattice is described by the Born model in which ions have charges $Z$ corresponding to their formal valences. The ions interact with each other through long-range Coulombic forces and short-range forces, which account for the Pauli repulsion and van-der-Waals interactions. The short-range forces are approximated by EPP with the form of Buckingham potentials:

$$E_{ij}(r) = A_{ij} \exp\left(-\frac{r}{\rho_{ij}}\right) - \frac{C_{ij}}{r^6}. \tag{3}$$

$A_{ij}$, $\rho_{ij}$ and $C_{ij}$ are empirically determined parameters and $r$ is the interionic separation. Ionic polarizability is accounted for with the shell model, $^{21}$ in which an ion is described as a core of charge $(Z - Y)$ and a massless shell with charge $Y$. The core and shell are connected by a harmonic spring with the spring constant $k$. The EPPs and shell parameters used in this study can be found in Table 1.

The lattice energies for the compounds $SrO$, $TiO_2$, $\infty_\text{p}$, $\mathbf{1}_\text{p}$, $\mathbf{2}_\text{p}$, $\mathbf{3}_\text{p}$ and $\mathbf{4}_\text{p}$ were obtained for each potential set by minimizing the lattice parameters to zero strain at a constant pressure. The energies of individual point defects were calculated with the Mott-Littleton method $^{22}$ which is a two region strategy. The two spherical regions (regions 1 and 2) are defined by their radius. In this study region 1 has a radius of 10 Å, wherein the ions are relaxed explicitly, with the radius

---

D. J. Green—contributing editor

---

Manuscript No. 32492. Received December 17, 2012; approved February 26, 2013.
$^{\dagger}$Author to whom correspondence should be addressed. e-mail: desouza@pc.rwth-aachen.de

![](./images/813231572466532353_1.jpg)

Fig. 1. Unit cells of selected pure and intergrowth Ruddlesden-Popper phases.

of region 2 set at 20 Å. All classical atomistic simulations were performed using the GULP code.²³

In addition to the EPP simulations, we performed DFT calculations with the Vienna ab initio simulation package (VASP).²⁴,²⁵ We used the projector-augmented wave (PAW) method²⁶,²⁷ and the GGA functional in the formulation of Perdew, Burke, and Ernzerhof (PBE).²⁸ The energy cutoff was set to 500 eV, while an equally spaced Monkhorst-Pack k-point-mesh²⁹ was chosen for each calculation such that the k-point spacing in the reciprocal cell was approximately 0.2 Å⁻¹. Gaussian smearing with a width of 0.1 eV was applied. The number of atoms in the calculated structures is 6, 8, 5, 14, 24, 34, and 54 for TiO₂, SrO, ∞ₚ, 1ₚ, 2ₚ, 3ₚ, and 4ₚ, respectively. The potentials used for Sr and Ti accounted for 10 valence electrons for each atom, whereas the potential used for O accounted for 6 valence electrons.

### III. Results and Discussion

#### (1) Stability of the Ruddlesden-Popper phases
We discuss three possible reaction schemes that can be used to compare the stability of the R-P phases with respect to one another. The first possibility is the formation reaction from the binary oxides, SrO and TiO₂:

$$
\mathrm{SrO}+\mathrm{TiO}_{2} \longrightarrow \mathrm{SrTiO}_{3} \tag{4}
$$

$$
(n+1) \mathrm{SrO}+n \mathrm{TiO}_{2} \longrightarrow \mathrm{Sr}_{n+1} \mathrm{Ti}_{n} \mathrm{O}_{3 n+1}, \tag{5}
$$

for which the formation energies are given by:

$$
\Delta_{f} U_{\mathrm{bo}}\left(\infty_{\mathrm{p}}\right)=U\left(\infty_{\mathrm{p}}\right)-U(\mathrm{SrO})-U\left(\mathrm{TiO}_{2}\right) \tag{6}
$$

$$
\Delta_{f} U_{\mathrm{bo}}\left(\mathbf{n}_{\mathrm{p}}\right)=U\left(\mathbf{n}_{\mathrm{p}}\right)-(n+1) U(\mathrm{SrO})-n U\left(\mathrm{TiO}_{2}\right). \tag{7}
$$

$\Delta_f U_{\text{bo}}$ is the formation energy from the binary oxides and $U(\text{A})$ is the calculated lattice energy of phase A.

The second reaction involves the addition of SrTiO₃ to a given R-P phase to produce a higher order R-P phase:

$$
\mathrm{Sr}_{n} \mathrm{Ti}_{n-1} \mathrm{O}_{3 n-2}+\mathrm{SrTiO}_{3} \longrightarrow \mathrm{Sr}_{n+1} \mathrm{Ti}_{n} \mathrm{O}_{3 n+1}, \tag{8}
$$

with the energy for this perovskite addition reaction

$$
\Delta_{f} U_{\mathrm{pa}}\left(\mathbf{n}_{\mathrm{p}}\right)=U\left(\mathbf{n}_{\mathrm{p}}\right)-U\left((\mathbf{n}-\mathbf{1})_{\mathrm{p}}\right)-U\left(\infty_{\mathrm{p}}\right). \tag{9}
$$

The third possibility is the reaction of rock-salt SrO with perovskite SrTiO₃:

$$
\mathrm{SrO}+n \mathrm{SrTiO}_{3} \longrightarrow \mathrm{Sr}_{n+1} \mathrm{Ti}_{n} \mathrm{O}_{3 n+1}, \tag{10}
$$

with the energy for the perovskite plus rock-salt oxide reaction given by

$$
\Delta_{f} U_{\mathrm{p}+\mathrm{r}}\left(\mathbf{n}_{\mathrm{p}}\right)=U\left(\mathbf{n}_{\mathrm{p}}\right)-n U\left(\infty_{\mathrm{p}}\right)-U(\mathrm{SrO}). \tag{11}
$$

It is important to note that the three reactions are not independent of one another. For example, the formation energy from the binary oxides [Eq. (7)] can be expressed as the sum of Eqs. (6) and (11)

$$
\Delta_{f} U_{\mathrm{bo}}\left(\mathbf{n}_{\mathrm{p}}\right)=n \Delta_{f} U_{\mathrm{bo}}\left(\infty_{\mathrm{p}}\right)+\Delta_{f} U_{\mathrm{p}+\mathrm{r}}\left(\mathbf{n}_{\mathrm{p}}\right), \tag{12}
$$

whereas $\Delta_f U_{\text{pa}}(\mathbf{n}_\text{p})$ can be expressed as a function of $\Delta_f U_{\text{bo}}$:

$$
\Delta_{f} U_{\mathrm{pa}}\left(\mathbf{n}_{\mathrm{p}}\right)=\Delta_{f} U_{\mathrm{bo}}\left(\mathbf{n}_{\mathrm{p}}\right)-\Delta_{f} U_{\mathrm{bo}}\left((\mathbf{n}-\mathbf{1})_{\mathrm{p}}\right)-\Delta_{f} U_{\mathrm{bo}}\left(\infty_{\mathrm{p}}\right). \tag{13}
$$

As a consequence, $\Delta_f U_{\text{pa}}(\mathbf{n}_\text{p})$ is related to both $\Delta_f U_{\text{bo}}$ and $\Delta_f U_{\text{p+r}}$:

**Table 1. Overview of the Potentials and Shell Parameters Used in this Study**

Udayakumar & Cormack¹⁰

<table>
  <tr>
    <td colspan="3">Buckingham potentials</td>
    <td>Cutoff = 10 Å</td>
    <td colspan="3">Shell parameters</td>
  </tr>
  <tr>
    <td>Interaction $ij$</td>
    <td>$A_{ij}$ /eV</td>
    <td>$\rho_{ij}$ /Å</td>
    <td>$C_{ij}$ /eVÅ⁶</td>
    <td>Ion</td>
    <td>$Y$ /$e$</td>
    <td>$k$ /eVÅ⁻²</td>
  </tr>
  <tr>
    <td>$\text{Sr}^{2+}\cdots\text{O}^{2-}$</td>
    <td>1400.0</td>
    <td>0.3500</td>
    <td>0.00</td>
    <td>$\text{Sr}^{2+}$</td>
    <td>1.33</td>
    <td>21.53</td>
  </tr>
  <tr>
    <td>$\text{Ti}^{4+}\cdots\text{O}^{2-}$</td>
    <td>754.2</td>
    <td>0.3879</td>
    <td>0.00</td>
    <td>$\text{Ti}^{4+}$</td>
    <td>2.89</td>
    <td>70.87</td>
  </tr>
  <tr>
    <td>$\text{O}^{2-}\cdots\text{O}^{2-}$</td>
    <td>22764.0</td>
    <td>0.1490</td>
    <td>43.0</td>
    <td>$\text{O}^{2-}$</td>
    <td>$-2.53$</td>
    <td>86.40</td>
  </tr>
</table>

McCoy et al.¹¹

<table>
  <tr>
    <td colspan="3">Buckingham potentials</td>
    <td>Cutoff = 20 Å</td>
    <td colspan="3">Shell parameters</td>
  </tr>
  <tr>
    <td>Interaction $ij$</td>
    <td>$A_{ij}$ /eV</td>
    <td>$\rho_{ij}$ /Å</td>
    <td>$C_{ij}$ /eVÅ⁶</td>
    <td>Ion</td>
    <td>$Y$ /$e$</td>
    <td>$k$ /eVÅ⁻²</td>
  </tr>
  <tr>
    <td>$\text{Sr}^{2+}\cdots\text{O}^{2-}$</td>
    <td>682.172</td>
    <td>0.39450</td>
    <td>0.00</td>
    <td>$\text{Sr}^{2+}$</td>
    <td>—</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$\text{Ti}^{4+}\cdots\text{O}^{2-}$</td>
    <td>2179.122</td>
    <td>0.30384</td>
    <td>8.986</td>
    <td>$\text{Ti}^{4+}$</td>
    <td>$-0.1$</td>
    <td>200.00</td>
  </tr>
  <tr>
    <td>$\text{O}^{2-}\cdots\text{O}^{2-}$</td>
    <td>9547.960</td>
    <td>0.21916</td>
    <td>32.0</td>
    <td>$\text{O}^{2-}$</td>
    <td>$-2.04$</td>
    <td>6.30</td>
  </tr>
</table>

Catlow et al.,²⁰ Set 1

<table>
  <tr>
    <td colspan="3">Buckingham potentials</td>
    <td>Cutoff = 15 Å</td>
    <td colspan="3">Shell parameters†</td>
  </tr>
  <tr>
    <td>Interaction $ij$</td>
    <td>$A_{ij}$ /eV</td>
    <td>$\rho_{ij}$ /Å</td>
    <td>$C_{ij}$ /eVÅ⁶</td>
    <td>Ion</td>
    <td>$Y$ /$e$</td>
    <td>$k$ /eVÅ⁻²</td>
  </tr>
  <tr>
    <td>$\text{Sr}^{2+}\cdots\text{O}^{2-}$</td>
    <td>843.0</td>
    <td>0.36335</td>
    <td>1.00</td>
    <td>$\text{Sr}^{2+}$</td>
    <td>1.33</td>
    <td>21.53</td>
  </tr>
  <tr>
    <td>$\text{Ti}^{4+}\cdots\text{O}^{2-}$</td>
    <td>835.051554</td>
    <td>0.382760</td>
    <td>9.6</td>
    <td>$\text{Ti}^{4+}$</td>
    <td>2.89</td>
    <td>70.87</td>
  </tr>
  <tr>
    <td>$\text{O}^{2-}\cdots\text{O}^{2-}$</td>
    <td>22764.3</td>
    <td>0.1490</td>
    <td>43.0</td>
    <td>$\text{O}^{2-}$</td>
    <td>$-2.53$</td>
    <td>86.40</td>
  </tr>
</table>

Catlow et al.,²⁰ Set 2

<table>
  <tr>
    <td colspan="3">Buckingham potentials</td>
    <td>Cutoff = 15 Å</td>
    <td colspan="3">Shell parameters</td>
  </tr>
  <tr>
    <td>Interaction $ij$</td>
    <td>$A_{ij}$ /eV</td>
    <td>$\rho_{ij}$ /Å</td>
    <td>$C_{ij}$ /eVÅ⁶</td>
    <td>Ion</td>
    <td>$Y$ /$e$</td>
    <td>$k$ /eVÅ⁻²</td>
  </tr>
  <tr>
    <td>$\text{Sr}^{2+}\cdots\text{O}^{2-}$</td>
    <td>835.0</td>
    <td>0.36375</td>
    <td>0.00</td>
    <td>$\text{Sr}^{2+}$</td>
    <td>1.33</td>
    <td>21.53</td>
  </tr>
  <tr>
    <td>$\text{Ti}^{4+}\cdots\text{O}^{2-}$</td>
    <td>838.051554</td>
    <td>0.38202</td>
    <td>9.8</td>
    <td>$\text{Ti}^{4+}$</td>
    <td>2.89</td>
    <td>70.87</td>
  </tr>
  <tr>
    <td>$\text{O}^{2-}\cdots\text{O}^{2-}$</td>
    <td>22764.3</td>
    <td>0.1490</td>
    <td>43.0</td>
    <td>$\text{O}^{2-}$</td>
    <td>$-2.53$</td>
    <td>86.40</td>
  </tr>
</table>

Akhtar et al.¹⁷

<table>
  <tr>
    <td colspan="3">Buckingham potentials</td>
    <td>Cutoff = 10 Å</td>
    <td colspan="3">Shell parameters</td>
  </tr>
  <tr>
    <td>Interaction $ij$</td>
    <td>$A_{ij}$ /eV</td>
    <td>$\rho_{ij}$ /Å</td>
    <td>$C_{ij}$ /eVÅ⁶</td>
    <td>Ion</td>
    <td>$Y$ /$e$</td>
    <td>$k$ /eVÅ⁻²</td>
  </tr>
  <tr>
    <td>$\text{Sr}^{2+}\cdots\text{O}^{2-}$</td>
    <td>776.84</td>
    <td>0.35867</td>
    <td>0.00</td>
    <td>$\text{Sr}^{2+}$</td>
    <td>1.526</td>
    <td>11.406</td>
  </tr>
  <tr>
    <td>$\text{Ti}^{4+}\cdots\text{O}^{2-}$</td>
    <td>877.2</td>
    <td>0.38096</td>
    <td>9.0</td>
    <td>$\text{Ti}^{4+}$</td>
    <td>$-35.863$</td>
    <td>65974.0</td>
  </tr>
  <tr>
    <td>$\text{O}^{2-}\cdots\text{O}^{2-}$</td>
    <td>22764.3</td>
    <td>0.1490</td>
    <td>43.0</td>
    <td>$\text{O}^{2-}$</td>
    <td>$-2.389$</td>
    <td>18.41</td>
  </tr>
</table>

†We have found the Potentials of Catlow et al. to be more reliable when using the shell parameters of Udayakumar & Cormack.

$$
\begin{aligned}
\Delta_{f} U_{\mathrm{pa}}\left(\mathbf{n}_{\mathrm{p}}\right) &=(n-1) \Delta_{f} U_{\mathrm{bo}}\left(\infty_{\mathrm{p}}\right)-\Delta_{f} U_{\mathrm{bo}}\left((\mathbf{n}-\mathbf{1})_{\mathrm{p}}\right) \\
&+\Delta_{f} U_{\mathrm{p}+\mathrm{r}}\left(\mathbf{n}_{\mathrm{p}}\right).
\end{aligned} \tag{14}
$$

To a good approximation the results obtained using the EPP sets can be compared directly with the experimental results because both refer to room temperature: experimental enthalpies are listed for $T=298$ K,³⁰ and EPP results refer to the temperature of the lattice to which the potential parameters were fitted—in all cases examined here, room temperature. The DFT calculations, however, refer to the static limit, $T=0$ K in the absence of lattice vibrations. To correct the DFT results to $T=298$ K, and so effect a comparison with experiment, we assume that the difference in zero-point energies between reactants and products, $\Delta_{f} U_{z \mathrm{p}}$, is zero³¹ and that the difference in heat capacities, $\Delta_{f} c_{p}$, is also zero. In any case, inaccuracies and approximations in DFT itself are probably greater than any temperature effects.³²,³³

(A) Binary oxides reaction: The formation energies $\Delta_{f} U_{\mathrm{bo}}$ of the R–P compounds $\mathbf{1}_{\mathrm{p}}-\mathbf{4}_{\mathrm{p}}$ calculated with the different EPPs as well as with DFT are shown in Fig. 2. In

![](./images/813231572466532353_2.jpg)

Fig. 2. Formation energies (eV) from the binary oxides, $\Delta_{f} U_{\mathrm{bo}}$, of $\mathbf{1}_{\mathrm{p}}, \mathbf{2}_{\mathrm{p}}, \mathbf{3}_{\mathrm{p}}$, and $\mathbf{4}_{\mathrm{p}}$ (per formula unit).

addition, two experimental data points³⁰ are plotted. All formation energies are negative and increase with $n$. The closest agreement with the experimental values can be seen for the Cormack potentials and the DFT results. Results from the other potentials show a smaller decrease in $\Delta_f U_{\text{bo}}$ with increasing $n$. We note that the good agreement between experiment and DFT does not necessarily confirm $\Delta_f c_p \approx 0$ ($\Delta_f U_{\text{zp}}$ is probably negligible³¹). It may be that DFT, for example, underestimates experiment and is compensated by $\Delta_f c_p \neq 0$.

Insight into the approximate linear relationship between $\Delta_f U_{\text{bo}}$ and $n$ can be obtained by examining Eq. (12). $\Delta_f U_{\text{p+r}}$ is only very weakly dependent on $n$ (discussed in more detail later on) so the slopes of the lines in Fig. 2 are determined by $\Delta_f U_{\text{bo}}(\infty_{\text{p}})$, i.e., by the calculated formation energy of $\text{SrTiO}_3$, which varies from one potential set to another.

(B) Perovskite addition reaction: The energies $\Delta_f U_{\text{pa}}$ of the addition reaction (reaction 8) are shown in Fig. 3. They range between $-0.3$ eV and $0.2$ eV for $n=1$ and converge to zero with increasing $n$. The closest agreement with the experimental value for $\mathbf{1_p}$ is seen for the DFT result; all the EPP results show larger deviations from the experimental value. The convergence of the formation energies to zero implies that with increasing $n$ it becomes harder to obtain phase pure R–P compounds as their formation energies are very similar: this is in agreement with experimental studies.⁶⁷⁸⁹ Unexpectedly, results obtained using periodic Hartree-Fock theory by Noguera¹² do not share any of the trends observed in the EPP or the DFT results.

![](./images/813231572466532353_3.jpg)

(C) Perovskite+rock-salt reaction: Figure 4 is a plot of $\Delta_f U_{\text{p+r}}$ for the R–P compounds. Once again the magnitude of the formation energies is of the order of $10^{-1}$eV. As in the perovskite addition reaction, the formation energies converge for greater $n$ to a certain value; however, in contrast to the perovskite addition reaction the results do not converge to zero, but to a different value for each potential used.

Due to the minimal change in formation energy within each potential set for increasing $n$, $\Delta_f U_{\text{p+r}}$ can be viewed as a constant which further helps in understanding the observed linear behavior for the formation energy of the binary oxides reaction $[\Delta_f U_{\text{bo}}(\mathbf{n_p})]$. All the results are in agreement with one another, whereas the DFT results show the best agreement with the experimental data. However, this is not the case for the results of Noguera,¹² which differ from all the observed trends and appear not to show signs of convergence.

Having examined three different reaction schemes we can conclude that the observed trends are mostly in agreement irrespective of the potential set used. However, the determined formation energies differ with the potentials used. The observed differences are mostly very small and could be a result of the known poor transferability of the $\text{Ti}^{4+}\dots \text{O}^{2-}$ potential between different crystal structures³⁴ or the accuracy limits of the computational methods used (for which a margin of error in the range of $0.5$ eV can be assumed).

(2) Stability of intergrowth R–P phases
The small formation energies of the Ruddlesden–Popper phases and the similarity in formation energy between phases is in agreement with the observed macroscopic phase separation in previous studies.⁶⁷⁸⁹ In this study, a variant of the phase separation is modeled in the form of intergrowths. The different intergrowths are produced by consecutive swapping of a $\text{SrO}$ layer with a $\text{TiO}_2$ layer. Due to the simulation method, translational symmetry is artificially imposed on the intergrowth cells, as can be seen on the right-hand side of Fig. 1 for the R–P phase of stoichiometric composition $n=2$. Although the preservation of the translational symmetry prohibits the simulation of a random distribution of the intergrowths, this method offers the possibility of a direct qualitative comparison of the intergrowth phases with their respective pure phase. The R–P phases with $n=1\text{--}4$ were investigated as described above. The results for R–P phases $\mathbf{3}$ and $\mathbf{4}$ are summarized in Table 2.

![](./images/813231572466532353_4.jpg)

The difference in lattice energies is positive in all cases, which indicates that the pure R–P phase is the most favorable. For both phases $\mathbf{3}$ and $\mathbf{4}$ an increase of an order of magnitude in $\Delta U_i$ is seen with each consecutive swap of $\text{SrO}$ and $\text{TiO}_2$ layers. This effect is also seen for R–P phases with $n=1$ and $2$. These results show a correlation between the separation of the inserted rock-salt layers and the change in lattice energy. In the pure compound $\mathbf{2_p}$ (see Figure 1) the inserted rock-salt layers are always located after every two $\text{SrTiO}_3$ units. The swapping of a $\text{TiO}_2$ and a $\text{SrO}$ layer (e.g., $\mathbf{2_{i(1,3)}}$ in Fig. 1) leads to unequal spacing of the inserted $\text{SrO}$ layers, i.e., there will be a shorter (one $\text{SrTiO}_3$ unit) and a longer (three $\text{SrTiO}_3$ units) distance between the rock-salt layers in comparison with the pure structure. We ascribe the increase in $\Delta U_i$ to the shorter distance between the inserted rock-salt layers, as the magnitude of the lattice energy difference for the intergrowth phases is of the same order for all R–P phase stoichiometries as long as the shorter distance between the $\text{SrO}$ layers in the intergrowth phase is the same (see Fig. 5).

<table>
<caption>Table 2. Difference in Lattice Energies (eV) of Different Intergrowths of the R–P Phases 3 and 4</caption>
<thead>
<tr>
<th></th>
<th colspan="3">$\Delta U_{i}$ /eV</th>
</tr>
<tr>
<th></th>
<th>$\mathbf{3_{i(2,4)} - 3_{p}}$</th>
<th>$\mathbf{3_{i(1,5)} - 3_{i(2,4)}}$</th>
<th>$\mathbf{3_{i(0,6)} - 3_{i(1,5)}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cormack</td>
<td>0.0016</td>
<td>0.0227</td>
<td>0.3562</td>
</tr>
<tr>
<td>McCoy</td>
<td>0.0056</td>
<td>0.0420</td>
<td>0.2685</td>
</tr>
<tr>
<td>Catlow 1</td>
<td>0.0012</td>
<td>0.0147</td>
<td>0.2436</td>
</tr>
<tr>
<td>Catlow 2</td>
<td>0.0012</td>
<td>0.0148</td>
<td>0.2429</td>
</tr>
<tr>
<td>Akhtar</td>
<td>0.0037</td>
<td>0.0261</td>
<td>0.3469</td>
</tr>
<tr>
<td></td>
<th colspan="3">$\Delta U_{i}$ /eV</th>
</tr>
<tr>
<td></td>
<th>$\mathbf{4_{i(3,5)} - 4_{p}}$</th>
<th>$\mathbf{4_{i(2,6)} - 4_{i(3,5)}}$</th>
<th>$\mathbf{4_{i(1,7)} - 4_{i(2,6)}}$</th>
<th>$\mathbf{4_{i(0,8)} - 4_{i(1,7)}}$</th>
</tr>
<tr>
<td>Cormack</td>
<td>0.0001</td>
<td>0.0017</td>
<td>0.0226</td>
<td>0.3582</td>
</tr>
<tr>
<td>McCoy</td>
<td>0.0009</td>
<td>0.0066</td>
<td>0.0422</td>
<td>0.2689</td>
</tr>
<tr>
<td>Catlow 1</td>
<td>0.0002</td>
<td>0.0014</td>
<td>0.0161</td>
<td>0.2457</td>
</tr>
<tr>
<td>Catlow 2</td>
<td>0.0002</td>
<td>0.0014</td>
<td>0.0148</td>
<td>0.2450</td>
</tr>
<tr>
<td>Akhtar</td>
<td>0.0010</td>
<td>0.0077</td>
<td>0.0307</td>
<td>0.3401</td>
</tr>
</tbody>
</table>

![](./images/813231572466532353_5.jpg)

Fig. 5. Shorter distance (of two) between SrO layers in different pure and intergrowth R–P phases. The plotted distances for each phase are averaged over all EPP sets used. Phases with the same shorter distance between inserted rock-salt layers are listed at the same position on the abscissa. Each symbol corresponds to a specific stoichiometric composition $\mathbf{n}$ as indicated by the key.

It is noteworthy that the larger distance between the inserted rock-salt layers appears to have a negligible effect on the resulting $\Delta U_{i}$. Further consecutive swapping of the layers will eventually lead to a nominal phase separation (e.g., $\mathbf{2_{i(0,4)}}$ in Fig. 1), wherein the shorter distance between rock-salt layers is zero and the longer distance corresponds to the four unit cells of $SrTiO_{3}$. In all cases the phase $\mathbf{n_{i(0,2n)}}$ is the least favored phase, as the shorter distance between the rock-salt layers is the shortest possible and the corresponding $\Delta U_{i}$ is the largest between it and the $\mathbf{n_{i(n',n'')}}$ phases [e.g., $(\mathbf{3_{i(0,6)} - 3_{i(1,5)}})$ and $(\mathbf{4_{i(0,8)} - 4_{i(1,7)}})$ in Table 2].

We conclude, therefore, that the smaller the minimum distance between inserted rock-salt layers, the less favorable is the intergrowth phase. Thus the pure R–P phase is the most favored state thermodynamically as it achieves the maximum spacing between all the inserted rock-salt layers. Furthermore, this result implies that the larger $n$ is, the greater the likelihood intergrowth phases will be observed because $\Delta U_{i} \to 0$ for $n \to \infty$.

### (3) SrO Partial Schottky disorder in $SrTiO_{3}$
Having investigated the formation energies of R–P phases in the $SrO-TiO_{2}$ system, we take a renewed look at the SrO partial Schottky disorder energies as all previously calculated values $^{17,18,19,20}$ overestimate the experimental value determined by Moos & Härdtl. $^{15}$ To date all reported SrO partial Schottky disorder energies have been calculated according for reaction (1) with SrO as the second phase. However, the second phase is not confined to SrO, but could also be a Ruddlesden–Popper phase as reaction (2) suggests. The disorder energy can then be calculated according to

$$
U_{\mathrm{Sch}}\left(\mathbf{n}_{\mathrm{p}}\right)=U\left(\mathrm{~V}_{\mathrm{Sr}}^{\prime \prime}\right)+U\left(\mathrm{~V}_{\mathrm{O}}^{\ddot{ }}\right)+U\left(\mathbf{n}_{\mathrm{p}}\right)-n U\left(\infty_{\mathrm{p}}\right), \quad(15)
$$

which can then be transformed to Eq. (16) using Eq. (11) (where $\Delta_{f} U_{\mathrm{p}+\mathrm{r}}(\mathbf{0}_{\mathrm{p}})=0$).

$$
U_{\mathrm{Sch}}\left(\mathbf{n}_{\mathrm{p}}\right)=U\left(\mathrm{~V}_{\mathrm{Sr}}^{\prime \prime}\right)+U\left(\mathrm{~V}_{\mathrm{O}}^{\ddot{ }}\right)+U(\mathrm{SrO})+\Delta_{f} U_{\mathrm{p}+\mathrm{r}}\left(\mathbf{n}_{\mathrm{p}}\right) \quad(16)
$$

<table>
<caption>Table 3. Calculated SrO Partial Schottky Disorder Energies in eV for $SrTiO_{3}$ with Respect to the Formation of Different Second Phases $\mathbf{n_{p}}$ for the Different Potential Sets. The Given Energies are for the Full Disorder (and not disorder energy per defect)</caption>
<thead>
<tr>
<th></th>
<th>$U_{\mathrm{Sch}}(\mathbf{0}_{\mathrm{p}})$</th>
<th>$U_{\mathrm{Sch}}(\mathbf{1}_{\mathrm{p}})$</th>
<th>$U_{\mathrm{Sch}}(\mathbf{2}_{\mathrm{p}})$</th>
<th>$U_{\mathrm{Sch}}(\mathbf{3}_{\mathrm{p}})$</th>
<th>$U_{\mathrm{Sch}}(\mathbf{4}_{\mathrm{p}})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cormack</td>
<td>4.89</td>
<td>4.78</td>
<td>4.76</td>
<td>4.76</td>
<td>4.76</td>
</tr>
<tr>
<td>McCoy†</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>Catlow 1</td>
<td>3.84</td>
<td>3.95</td>
<td>3.93</td>
<td>3.93</td>
<td></td>
</tr>
<tr>
<td>Catlow 2</td>
<td>3.88</td>
<td>3.98</td>
<td>3.96</td>
<td>3.96</td>
<td>3.96</td>
</tr>
<tr>
<td>Akhtar</td>
<td>1.55</td>
<td>1.71</td>
<td>1.69</td>
<td>1.68</td>
<td>1.68</td>
</tr>
<tr>
<td>Moos (exp.)</td>
<td>2.5</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

†The defect energies for the McCoy potentials could not be obtained as the calculations did not converge.

The calculated results for the full partial Schottky disorder for the different second phases are summarized in Table 3. Energies are given for the full SrO partial Schottky disorder and not disorder energy per defect.

Some of the potentials used in this study have been used before to calculate the partial Schottky disorder energies $U_{\mathrm{Sch}}(\mathbf{0}_{\mathrm{p}})$, such as those of Catlow et al. and Akhtar et al. The results using the two Catlow potentials in this study differ from the results obtained by Catlow et al. $^{20}$ by 0.3 eV which is a result of using different shell parameters for the calculation; otherwise the results are in very good agreement. Akhtar et al. obtained a disorder energy of 3.06 eV using the CASCADE program, $^{17}$ whereas using their potential set with the GULP code yielded a disorder energy of 1.55 eV. This

discrepancy—although unexpected— could be a result of the difficulty seen in modeling the interactions of the Sr–Ti–O system with EPPs.³⁴ As for the partial Schottky disorder energies involving R–P phases as the second phase, it can be seen that the effect of their formation is minimal as their formation energies $\Delta U_{\text{p+r}}(\mathbf{n}_\text{P})$ are so small. However, depending on whether they are positive or negative an increase or decrease in the disorder energy can be achieved. Comparing the results with the experimental value of 2.5 eV from Moos \& Härdtl,¹⁵ it is obvious that most potentials irrespective of the second phase overestimate the actual value with the exception of the Akhtar potential set which underestimates the experimental value by approximately 1 eV.

In conclusion we have shown that the formation of R–P phases can have an influence on the disorder energy, but as their formation energies are relatively small, their effect would be minimal unless the formation entropy—which has not been taken into consideration—of the R–P compounds has a larger influence on the partial Schottky disorder energy at high temperatures (such as those of synthesis).

### IV. Summary

In this article, three different reaction schemes for the formation of R–P phases have been investigated using atomistic simulations as well as *ab initio* calculations, and it was possible to show that the formation energies for R–P compounds are small irrespective of the reaction scheme chosen. As the formation energies of higher order R–P phases were very similar, the energetics of intergrowths were also investigated and the results increases that the likelihood of the formation of intergrowths increases for $\text{Sr}_{n+1}\text{Ti}_n\text{O}_{3n+1}$ with large $n$. Both the results of the different reaction schemes as well as those of the simulated intergrowths are supported by the observations made in attempts to synthesize R–P phases with $n > 3$.⁶,⁷,⁸,⁹ Finally, the results of the investigation of the partial Schottky disorder energies of $\text{SrTiO}_3$ showed that the formation of R–P phases can have an influence on the formation energies of the disorder. Although the amount of influence appears to be minimal, further studies with respect to the free energy of the system are warranted to investigate the entropic contribution to the disorder energy.³⁵

### Acknowledgment

We acknowledge funding from the DFG (German Science Foundation) within the framework of the collaborative research centre SFB 917 "Nanoswitches".

### References

¹S. Witek and D. M. Smyth, "Variability of the Sr/Ti Ratio in $\text{SrTiO}_3$," *J. Am. Ceram. Soc.*, **67** [5] 372–5 (1984).

²S. N. Ruddlesden and P. Popper, "New Compounds of the $\text{K}_2\text{NiF}_4$ Type," *Acta Cryst.*, **10** 538–9 (1957).

³S. N. Ruddlesden and P. Popper, "The Compound $\text{Sr}_3\text{Ti}_2\text{O}_7$ and Its Structure," *Acta Cryst.*, **11** 54–5(1958).

⁴D. G. Schlom, L.-Q. Chen, X. Pan, A. Schmehl, and M. A. Zurbuchen, "A Thin Film Approach to Engineering Functionality Into Oxides," *J. Am. Ceram. Soc.*, **91** [8] 2429–54 (2008).

⁵K. Shibuya, R. Dittmann, S. Mi, and R. Waser, "Impact of Defect Distribution on Resistive Switching Characteristics of $\text{Sr}_2\text{TiO}_4$ Thin Films," *Adv. Mater.*, **22** [3] 411–4 (2010).

⁶R. J. D. Tilley, "An Electron Microscope Study of Perovskite-related Oxides in the Sr-Ti-O System," *J. Solid State Chem.*, **21** 293 (1977).

⁷G. J. McCarthy, W. B. White, and R. Roy, "Phase Equilibria in the 1375°C Isotherm of the System Sr-Ti-O," *J. Am. Ceram. Soc.*, **52**463 (1969).

⁸G. J. McCarthy, W. B. White, and R. Roy, "The System Eu-Ti-O: Phase Relations in a Portion of the 1400°C Isotherm," *J. Inorg. Nucl. Chem.*, **31** 329 (1969).

⁹W. Tian, X. Q. Pan, J. H. Haeni, and D. G. Schlom, "Transmission Electron Microscopy Study of $n$=1–5 $\text{Sr}_{n+1}\text{Ti}_n\text{O}_{3n+1}$ Epitaxial Thin Films," *J. Mater. Res.*, **16** [7] 2013–26 (2001).

¹⁰K. R. Udayakumar and A. N. Cormack, "Structural Aspects of Phase Equilibria in the Strontium-Titanium-Oxygen System," *J. Am. Ceram. Soc.*, **71** [11] C-469–71 (1988).

¹¹M. A. McCoy, R. W. Grimes, and W. E. Lee, "Phase Stabiliy and Interfacial Structures in the SrO–SrTiO₃ System," *Philos. Mag. A*, **75** [3] 83–46 (1997).

¹²C. Noguera, "Theoretical Investigation of the Ruddlesden-Popper Compounds $\text{Sr}_{n+1}\text{Ti}_n\text{O}_{3n+1}$ ($n$=1–3)," *Phil. Mag. Lett.*, **80**[3] 173–80 (2000).

¹³T. Suzuki and M. Fujimoto, "First-principles Structural Stability Study of Non-stoichiometry-related Planar Defects in $\text{SrTiO}_3$ and $\text{BaTiO}_3$," *J. Appl. Phys.*, **89** [10] 5622–9 (2001).

¹⁴O. Le Bacq, E. Salinas, A. Pisch, C. Bernard, and A. Pasturel, "First-principles Structural Stability in the Strontium-titanium-oxygen System," *Philos. Mag.*, **86** [15] 2283–92 (2006).

¹⁵R. Moos and K. H. Härdtl, "Defect Chemistry of Donor-Doped and Undoped Strontium Titanate Ceramics between 1000 and 1400C," *J. Am. Ceram. Soc.*, **80** [10] 2549–62 (1997).

¹⁶W. Menesklou, "Compensation of the Excess Charge in Lanthanum-Doped Barium Titanate and Strontium Titanate" (in German), Ph.D. thesis, Karlsruhe University, Karlsruhe, FRG, 1997.

¹⁷M. J. Akhtar, Z.-U.-N. Akhtar, R. A. Jackson, and C. R. A. Catlow, "Computer Simulation Studies of Strontium Titanate," *J. Am. Ceram. Soc.*, **78** [2] 421–8 (1995).

¹⁸J. Crawford and P. Jacobs, "Joint Defect Energies for Strontium Titanate: A Pair-Potentials Study," *J. Solid State Chem.*, **144** 423–9(1999).

¹⁹T. Tanaka, K. Matsunaga, Y. Ikuhara, and T. Yamamoto, "First-principles Study on Structures and Energetics of Intrinsic Vacancies in $\text{SrTiO}_3$," *Phys. Rev. B*, **68** 205213-1–8 (2003).

²⁰C. R. A. Catlow, Z. X. Guo, M. Miskufova, S. A. Shevlin, A. G. H. Smith, A. A. Sokoll, A. Walsh, D. J. Wilson, and S. M. Woodley, "Advances in Computational Studies of Energy Materials," *Phil. Trans. R. Soc. A*, **368** 3379–456 (2010).

²¹B. G. Dick and A. W. Overhauser, "Theory of the Dielectric Constants of Alkali Halide Crystals," *Phys. Rev.*, **112** [1] 90–103 (1958).

²²N. F. Mott and M. J. Littleton, "Conduction in Polar Crystals. I. Electro-lytic Conduction in Solid Salts," *Trans Faraday Soc.*, **34**, 485–99 (1938).

²³J. D. Gale, "GULP: A Computer Program for the Symmetry-adapted Simulation of Solids," *J. Chem. Soc.*, **93**, 629–37 (1997).

²⁴G. Kresse and J. Hafner, "Ab Initio Molecular Dynamics for Liquid Metals," *Phys. Rev. B*, **47** 558–61 (1993).

²⁵G. Kresse and J. Furthmüller, "Efficient Iterative Scheme for Ab Initio Total Energy Calculations using a Plane-Wave Basis Set," *Phys. Rev. B*, **54** 11169–86 (1996).

²⁶G. Kresse and D. Joubert, "From Ultrasoft Pseudopotentials to the Projector Augmented Wave Method," *Phys. Rev. B*, **59** 1758–75 (1999).

²⁷P. E. Blöchl, "Projector Augmented-wave Method," *Phys. Rev. B*, **50**[24] 17953–79 (1994).

²⁸J. P. Perdew, K. Burke, and M. Ernzerhof, "Generalized Gradient Approximation Made Simple," *Phys. Rev. Lett.*, **77** [18] 3865–8(1996).

²⁹H. J. Monkhorst and J. D. Pack, "Special Points for Brillouin-zone Integrations," *Phys. Rev. B*, **13** [12] 5188–92 (1976).

³⁰I. Barin, *Thermochemical Data of Pure Substances*, third edition edn. VCH Verlagsgesellschaft mbH, Weinheim (Federal Republic of Germany) and VCH Publishers, Inc., New York, NY (USA), 1995

³¹G. D. Barrera, M. B. Taylor, N. L. Allan, T. H. K. Barron, and L. N. Kantorovich, "Ionic Solids at Elevated Temperatures and High Pressures: $\text{MgF}_2$," *J. Chem. Phys.*, **11** 4337–44 (1997).

³²R. P. Stoffel, C. Wessel, M.-W. Lumey, and R. Dronskowski, "Ab Initio Thermochemistry of Solid-State Materials," *Angew. Chem. Int. Ed. Engl.*, **49** 5242–66 (2010).

³³K. Burke, "Perspective on Density Functional Theory," *J. Chem. Phys.*, **136**, 150901-1–9 (2012).

³⁴T. S. Bush, J. D. Gale, C. R. A. Catlow, and P. D. Battle, "Self-consistent Interatomic Potentials for the Simulation of Binary and Ternary Oxides," *J. Mater. Chem.*, **4** [6] 831–7 (1994).

³⁵M. B. Taylor, G. D. Barrera, N. L. Allan, T. H. K. Barron, and W. C. Mackrodt, "Free Energy of Formation of Defects in Polar Solids," *Faraday Discuss.*, **106** 377–87 (1997).
□