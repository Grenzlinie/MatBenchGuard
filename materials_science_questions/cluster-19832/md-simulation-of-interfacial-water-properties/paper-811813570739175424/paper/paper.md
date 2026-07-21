![](./images/811813570739175424_1.jpg)

Analysis of anisotropic local field in sum frequency generation spectroscopy with the charge response kernel water model

Tatsuya Ishiyama and Akihiro Morita

Citation: *The Journal of Chemical Physics* **131**, 244714 (2009); doi: 10.1063/1.3279126
View online: http://dx.doi.org/10.1063/1.3279126
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/131/24?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Reorientation of the "free OH" group in the top-most layer of air/water interface of sodium fluoride aqueous solution probed with sum-frequency generation vibrational spectroscopy
J. Chem. Phys. **141**, 18C507 (2014); 10.1063/1.4895561

Molecular dynamics simulation of liquid methanol. II. Unified assignment of infrared, raman, and sum frequency generation vibrational spectra in methyl C–H stretching region
J. Chem. Phys. **134**, 024510 (2011); 10.1063/1.3514146

Sum frequency generation surface spectra of ice, water, and acid solution investigated by an exciton model
J. Chem. Phys. **127**, 204710 (2007); 10.1063/1.2790437

Microwave heating of water, ice, and saline solution: Molecular dynamics study
J. Chem. Phys. **126**, 034509 (2007); 10.1063/1.2403870

Three-dimensional picture of dynamical structure in liquid water
J. Chem. Phys. **112**, 1367 (2000); 10.1063/1.480689

![](./images/811813570739175424_2.jpg)

# Analysis of anisotropic local field in sum frequency generation spectroscopy with the charge response kernel water model

Tatsuya Ishiyama and Akihiro Morita $^{a)}$

Department of Chemistry, Graduate School of Science, Tohoku University, Sendai 980-8578, Japan

(Received 16 September 2009; accepted 7 December 2009; published online 30 December 2009)

A new flexible and polarizable water model based on the charge response kernel (CRK) theory is developed for the analysis of sum frequency generation (SFG) spectroscopy. The CRK model well describes several bulk water properties and SFG spectrum by molecular dynamics (MD) calculations. While the flexible and polarizable MD simulation generally adopts the short-range damping of intermolecular interaction, it is found that the same procedure is not adequate for the calculation of transition dipole in strongly hydrogen bonding environment. Accordingly, the improved calculation of the nonlinear susceptibility of water surface results in the positive imaginary part in the $3000-3200 \mathrm{~cm}^{-1}$ region, which is consistent with recent phase-sensitive experiments. The mechanism of the positive region is attributed to the anisotropic local field effect induced by the orientational correlation of surface water. (C) 2009 American Institute of Physics.

[doi:10.1063/1.3279126]

## I. INTRODUCTION

Water is a fundamental substance on the earth, and its hydrogen bonding (H-bonding) network plays crucial roles in a variety of physical, chemical, and life sciences. $^{1,2}$ Interfacial water is of particular significance in a number of phenomena, including heterogeneous atmospheric chemistry, bubble formation, biological membrane, and corrosion, and detailed nature of interfacial water have been unveiled by recent progress of experimental and theoretical methods. In the experimental side, $^{3-9}$ the nonlinear optical spectroscopies such as sum frequency generation (SFG) significantly contributed to investigation of interfacial properties, including H-bond structure, orientation, and dynamics of interfacial water molecules. $^{10-12}$ In the theoretical side, molecular dynamics (MD) simulations with a variety of force fields, such as classical, $^{13-26}$ empirical valence bond type, $^{27}$ and density functional theory, $^{28,29}$ are powerful tools to investigate structure, dynamic properties, electrostatic properties, and spectroscopic properties of interfacial water. Recently, the direct calculation of SFG spectra by MD simulation opened a promising avenue for the investigation of interfacial properties. $^{18,30,31}$ In the present paper, we develop a new water model to calculate SFG spectra of aqueous surfaces, whereas the present modeling methodology can be easily extended to more complicated molecules. The present model allows improvement for the previous calculations of the SFG spectra, as discussed below in detail.

The theoretical SFG calculation requires modeling of the frequency-dependent nonlinear susceptibility, $\chi(\omega_{\mathrm{SFG}}, \omega_{\mathrm{vis}}, \omega_{\mathrm{ir}})$. One possible method is based on the energy representation of $\chi^{30}$ To implement this method, molecular orientation at the interface is sampled by MD simulation while the transition dipole moment and transition polarizability are given on the basis of quantum chemical calculations. $^{14,17,19,20,30}$ The MD simulation in this method is relatively less demanding because a conventional force field can be used to sample the orientational structure of interface. On the other hand, accurate modeling of the transition dipole and polarizability in the interface environment poses quite challenging problems, and it is often difficult to make the modeling a general method applicable to other systems. Treatment of the transition dipole and polarizability is a major bottleneck in the energy representation method. Another possible method to compute $\chi$ is based on the timedependent representation, $^{31}$ where the transition dipole and polarizability are implicitly incorporated in the time correlation formula. This method reduces the burden to model transition dipole and polarizability and allows for straightforward calculation of the nonlinear susceptibility $\chi$ by MD simulation. $^{31,32}$ On the other hand, the MD calculation for this approach requires a sophisticated molecular model beyond the usual flexible and polarizable force field. $^{33-41}$ Calculation of instantaneous dipole and polarizability of the interface is a key ingredient of the MD simulation of this approach, as discussed below. For the time-dependent calculation of SFG spectra, we propose to use the charge response kernel (CRK) theory $^{42-46}$ as a general and promising modeling method. The present flexible and polarizable CRK water model is an extension to the previously developed CRK water model, $^{38}$ by explicitly incorporating conformational dependent terms in the Coulomb potential. Consequently the present model has the geometry dependence of dipole and polarizability, which is a requisite to describe IR or Raman spectra of intramolecular vibrations. The present CRK water model well reproduces the bulk liquid properties such as density, enthalpy of vaporization, diffusion coefficient, IR and Raman spectra, etc. We also note in passing that the present water model correctly reproduces the modified

$^{a)}$Electronic mail: amorita@m.tains.tohoku.ac.jp.

H-O-H angle in the liquid phase, $^{37}$ though most flexible and polarizable models fail to reproduce because of the lack of the geometric polarizability.

Regarding a technical problem of polarizable models, it is widely known that the polarizable MD simulation often suffers from numerical divergence of polarization, called "polarization catastrophe." Employing molecular flexibility makes the polarizable MD more fragile. To avoid such unphysical events, most flexible and polarizable models adopt damping treatments of short-range interactions. There are several types of damping functions such as a simple shield type, $^{33}$ Thole-type, $^{40,47,48}$ Gaussian-type, $^{34,39}$ or Slater-type. $^{36}$ The present paper demonstrates that such damping functions actually improve the accuracy of the force field at short internuclear distances. However, the damping treatment is not suitable for the calculation of instantaneous dipole and polarizability for the SFG spectra. The reason for this difference will be elucidated later. Consequently, calculation of the SFG spectra has been significantly improved, especially in the frequency region of strongly redshifted O-H stretching vibration.

The improvement in the SFG calculation is relevant to the recent phase-sensitive SFG experiment, $^{49,50}$ where the complex susceptibility itself, $\chi$, consisting of the real and imaginary parts, $\text{Re}[\chi]$ and $\text{Im}[\chi]$, was reported for water surface. $^{51-54}$ In the experiment, the imaginary part $\text{Im}[\chi]$ turned out to be composed of the following three bands: the first is the positive band at about $3700\ \text{cm}^{-1}$, the second is the negative band from $3200$ to $3600\ \text{cm}^{-1}$, and the third is the positive band from $3000$ to $3200\ \text{cm}^{-1}$. The reversed sign between the former two bands was predicted by our first SFG calculation and elucidated in terms of the molecular orientation, $^{30}$ though the third band has been puzzling to assign. Though this third band is assigned to some O-H components in a few surface layers by some groups, $^{51,55}$ no direct support by MD calculation of SFG spectra has been provided. The present study succeeded in reproducing the third band by improving the description of the short-range interactions in the MD simulation. To verify that the result is not due to an artifact of the molecular model, we also employed the point dipole (PD) model, which was developed in our previous study, $^{56}$ with the equivalent improvement in the short-range damping for the SFG calculation. It is found that both the CRK and PD models consistently reproduce the above mentioned third peak with the appropriate damping treatments. Based on the successful calculation of $\chi$, the assignment of the third band is given: that this positive feature is induced by the orientational correlation of interfacial water molecules.

The remainder of this paper is organized as follows. In Sec. II, the molecular model based on the CRK theory is described, where the geometry dependence of molecular electrostatic properties is properly considered. Then the formulae to construct nonlinear susceptibility are presented in Sec. III on the basis of both the CRK and PD models. In Sec. IV, the reliability of the present CRK model is thoroughly examined by MD simulation of bulk water and surface water. Section V is devoted to the calculation and analysis of the second-order nonlinear susceptibility. Here the short-range damping in the polarizable MD simulation is refined for the calculation of electrostatic properties, and thereby the phase of the nonlinear susceptibility is properly elucidated. Concluding remarks follow in Sec. VI.

![](./images/811813570739175424_3.jpg)

FIG. 1. Schematic of five interaction sites and internal coordinates for the CRK water molecule.

## II. MOLECULAR MODEL

A water molecule in the present CRK model consists of five interaction sites located on oxygen, two hydrogens, and two fictitious sites (X), as schematically illustrated in Fig. 1, where two X sites are set along the line passing through the oxygen O perpendicular to the molecular plane with O-X distance $d_{\text{OX}}$=0.55 Å. The two X sites allow for the out-of-plane polarization. $^{38}$ The equilibrium geometry for the CRK water molecule is determined by the experimental gas-phase monomer configuration, $^{57}$ where the equilibrium O-H bond length and the equilibrium H-O-H angle are $0.9572$ Å and $104.52^\circ$, respectively. While the molecular conformation varies with intramolecular vibration, the location of the sites X is uniquely determined.

The total potential energy of the present CRK model system $U_{\text{total}}$ consists of the intramolecular part $U_{\text{intra}}$, van der Waals part described by the Lennard-Jones potential $U_{\text{LJ}}$, and the Coulombic potential $U_{\text{C}}$,

$$
U_{\text{total}} = U_{\text{intra}} + U_{\text{LJ}} + U_{\text{C}}. \tag{1}
$$

In Eq. (1), $U_{\text{intra}}$ for the intramolecular vibration is the sum of those of constituent molecules. Each molecular term has the following functional form: $^{56}$

$$
\begin{aligned}
u_{\text{intra}}^{\text{H}_2\text{O}} =& \sum_{n=2}^{6} \left[ k_{n}(\Delta r_1)^n + k_{n}(\Delta r_2)^n \right] + k_{rr'} \Delta r_1 \Delta r_2 \\
&+ (k_\theta/2)(\Delta r_3)^2 + k_{r\theta} \Delta r_3(\Delta r_1 + \Delta r_2),
\end{aligned} \tag{2}
$$

where $\Delta r_1$ and $\Delta r_2$ are the displacements of the two O-H bond lengths from the equilibrium O-H distance and $\Delta r_3$ is that from the equilibrium H-H distance. We reparametrized the ingredient parameters for the present CRK model so as to reproduce the O-H stretching frequencies of free OH region ($\sim3700\ \text{cm}^{-1}$) as well as the redshifted region ($\sim3400\ \text{cm}^{-1}$) of liquid water by MD simulation. The optimized parameters are tabulated in Table I, where the parameters for anharmonic terms $k_3 \sim k_6$ are different with respect to the sign of $\Delta r$. These parameters effectively incorporate the anharmonic frequency shift of OH stretching.

The second term, $U_{\text{LJ}}$, consists of site-site Lennard-Jones potentials,

<table><caption>TABLE I. Intramolecular potential parameters of CRK water model (in a.u.).</caption>
<thead>
  <tr>
    <th>
    </th>
    <th>
      $\Delta r &gt; 0$
    </th>
    <th>
      $\Delta r &lt; 0$
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      $k_2$
    </td>
    <td>
      0.269
    </td>
    <td>
      0.269
    </td>
  </tr>
  <tr>
    <td>
      $k_3$
    </td>
    <td>
      $-$0.45
    </td>
    <td>
      $-$0.50
    </td>
  </tr>
  <tr>
    <td>
      $k_4$
    </td>
    <td>
      0.55
    </td>
    <td>
      3.00
    </td>
  </tr>
  <tr>
    <td>
      $k_5$
    </td>
    <td>
      $-$3.0
    </td>
    <td>
      $-$3.9
    </td>
  </tr>
  <tr>
    <td>
      $k_6$
    </td>
    <td>
      7.0
    </td>
    <td>
      20.0
    </td>
  </tr>
  <tr>
    <td>
      $k_\theta$
    </td>
    <td>
      0.109
    </td>
    <td>
      0.109
    </td>
  </tr>
  <tr>
    <td>
      $k_{r\theta}$
    </td>
    <td>
      $-$0.0822
    </td>
    <td>
      $-$0.0822
    </td>
  </tr>
  <tr>
    <td>
      $k_{r^{\prime}r^{\prime}}$
    </td>
    <td>
      0.0678
    </td>
    <td>
      0.0678
    </td>
  </tr>
</tbody>
</table>

$$
U_{\mathrm{LJ}} = \sum_{i>j} \sum_{a,b}^{\mathrm{site}} 4\epsilon_{ab} \left\{ \left( \frac{\sigma_{ab}}{r_{ai,bj}} \right)^{12} - \left( \frac{\sigma_{ab}}{r_{ai,bj}} \right)^6 \right\}, \tag{3}
$$

where $r_{ai,bj}$ is the distance between site $a$ of the $i$th molecule and site $b$ of the $j$th molecule. Hereafter we use the notation that suffixes $i,j,k,\cdots$ refer to molecules and $a,b,c,\cdots$ to sites. $\epsilon_{ab}$ and $\sigma_{ab}$ are the Lennard-Jones parameters between sites $a$ and $b$, which are determined by the Lorentz–Berthelot mixing rules, i.e., $\sigma_{ab} = {(\sigma_{a} + \sigma_{b})}/2$ and $\epsilon_{ab} = \sqrt{\epsilon_{a}\epsilon_{b}}$. The Lennard-Jones parameters are assigned only to the oxygen site, and the values are $\sigma_{\mathrm{O}} = 3.205$ Å and $\epsilon_{\mathrm{O}} = 0.6496$ kJ mol$^{-1}$, respectively.

The third term of Eq. (1), $U_{\mathrm{C}}$, has the following form,
$$
U_{\mathrm{C}} = \frac{1}{2} \sum_{i} \sum_{a}^{\mathrm{site}} Q_{ai} V_{ai} - \frac{1}{2} \sum_{i} \sum_{a}^{\mathrm{site}} \sum_{b}^{\mathrm{site}} K_{abi} V_{ai} V_{bi}, \tag{4}
$$

where $Q_{ai}$ and $V_{ai}$ are the partial charge and electrostatic potential at the site $a$ of the $i$th molecule. In the present polarizable model, the partial charge $Q_{ai}$ varies in response to the electrostatic potential. The response is represented using the CRK, a property defined as $K_{abi} = {\partial Q_{ai}}/{\partial V_{bi}}$. The first term of Eq. (4) is the Coulomb interaction energy of the site charges $Q_{ai}$, and the second term in Eq. (4) is the so-called reorganization energy of polarization.

In Eq. (4), $Q_{ai}$ and $V_{ai}$ are determined self-consistently as follows. $V_{ai}$ is given by the partial charges of surrounding molecules $j(\neq i)$,
$$
V_{ai} = \sum_{j(\neq i)} \sum_{b}^{\mathrm{site}} \frac{Q_{bj}}{r_{ai,bj}} f_{ai,bj}, \tag{5}
$$

where $f_{ai,bj}$ is the damping function as described in Sec. II A. On the other hand, $Q_{ai}$ is determined as
$$
Q_{ai} = Q_{ai}^{0} + \sum_{b}^{\mathrm{site}} \frac{\partial Q_{ai}}{\partial V_{bi}} V_{bi} = Q_{ai}^{0} + \sum_{b}^{\mathrm{site}} K_{abi} V_{bi}, \tag{6}
$$

where $Q_{ai}^{0}$ is the site charge for an isolated molecule. In the present flexible model, $Q_{ai}^{0}$ and $K_{abi}$ are a function of the molecular conformation, as discussed in Sec. II B. Note that the conformational dependence of $Q_{ai}^{0}$ and $K_{abi}$ is essential to treat the IR, Raman, or SFG spectroscopy for intramolecular vibrations.

## A. Short-range damping function

The damping function $f_{ai,bj}$ in Eq. (5) is invoked in polarizable MD simulation to moderate the Coulomb interaction at a short distance, as mentioned in Sec. I. It effectively remedies the shortcomings of the point charge model at a short range. Here we introduce the damping function of Gaussian type $f^{\mathrm{Gauss}}$ by assuming a Gaussian charge distribution of site charge. $^{34,39,58}$ The Gaussian density of charge $Q_{ai}$ at the center of $\boldsymbol{r}_{ai}$ with the width of $\xi_{ai}$ is described by
$$
\rho_{ai}(\boldsymbol{r}) = \frac{Q_{ai}}{(2\pi \xi_{ai}^{2})^{3/2}} \exp\left[ - \frac{|\boldsymbol{r} - \boldsymbol{r}_{ai}|^{2}}{2\xi_{ai}^{2}} \right]. \tag{7}
$$

The Coulombic interaction energy between two charge densities can then be written by
$$
\iint \frac{\rho_{ai}(\boldsymbol{r}_{1}) \rho_{bj}(\boldsymbol{r}_{2})}{|\boldsymbol{r}_{1} - \boldsymbol{r}_{2}|} d\boldsymbol{r}_{1} \boldsymbol{r}_{2} = \frac{Q_{ai} Q_{bj}}{r_{ai,bj}} \mathrm{erf}(\gamma_{ai,bj} r_{ai,bj}), \tag{8}
$$

where
$$
\gamma_{ai,bj} = \frac{1}{\sqrt{2(\xi_{ai}^{2} + \xi_{bj}^{2})}}, \tag{9}
$$

and
$$
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp(-t^{2})dt. \tag{10}
$$

Equation (8) gives the modified Coulomb interaction between two charges. The damping factor $\mathrm{erf}(\gamma_{ai,bj} r_{ai,bj})$ is almost unity at $r_{ai,bj} \gg 1/\gamma_{ai,bj}$, while it becomes less than unity at $r_{ai,bj} \lessapprox 1/\gamma_{ai,bj}$. The width of the Gaussian charge distribution is set to $\xi = 0.593$ Å for the partial charges of water sites. In the practical calculations, the damping function takes the following form:
$$
f_{ai,bj}^{\mathrm{Gauss}} = \mathrm{erf}(\gamma_{ai,bj} r_{ai,bj}) S_{1}(r_{ai,bj}) + S_{2}(r_{ai,bj}), \tag{11}
$$

where $S_{1}$ and $S_{2}$ are the smooth functions between 0 and 1 as
$$
S_{1}(r) =
\begin{cases}
1 & (r \leq R_{1}) \\
\frac{(R_{2}^{2} - r^{2})^{2}(R_{2}^{2} + 2r^{2} - 3R_{1}^{2})}{(R_{2}^{2} - R_{1}^{2})^{3}} & (R_{1} < r < R_{2}), \\
0 & (R_{2} < r)
\end{cases}
\tag{12a}
$$

$$
S_{2}(r) =
\begin{cases}
0 & (r \leq R_{1}) \\
\frac{(R_{1}^{2} - r^{2})^{2}(R_{1}^{2} + 2r^{2} - 3R_{2}^{2})}{(R_{1}^{2} - R_{2}^{2})^{3}} & (R_{1} < r < R_{2}). \\
1 & (R_{2} < r)
\end{cases}
\tag{12b}
$$

The functions $S_{1}(r)$ and $S_{2}(r)$ interpolate the error function and unity in Eq. (11) in the range $R_{1} < r < R_{2}$. $R_{1}$ and $R_{2}$ were set with the following criteria: $\mathrm{erf}(\gamma_{ai,bj} R_{1}) = 1 - 10^{-7}$ and $R_{2} = R_{1} + 1.0$ bohr($\sim$0.53 Å). For the interaction between water molecules ($\xi = 0.593$ Å), accordingly $R_{1} = 4.465$ Å and $R_{2} = 4.995$ Å. The interpolation of Eq. (12) allows to omit the calculation of the damping function from the Coulomb interactions beyond $r > R_{2}$.

### B. Conformation-dependent partial charge and charge response kernel

Next we remark the conformational dependence of the partial charge $Q^0$ and CRK $K$ in Eq. (6). Our previous CRK water model did not incorporate those conformational dependence, and accordingly it allowed to treat only the spectra of intermolecular vibrations. $^{38}$ In the CRK model, the conformational dependence of $Q^0$ and $K$ is straightforwardly obtained by *ab initio* or DFT calculations for varying molecular conformation, and no empirical assumption is necessary.

Here the conformational dependence is expressed to the first-order displacements of internal coordinates $S_t$ as follows:

$$
Q_{a i}^{0}=Q_{a i}^{\mathrm{eq}}+\sum_{t}^{\text {mode }} \frac{\partial Q_{a i}}{\partial S_{t, i}} S_{t, i},
\tag{13a}
$$

$$
K_{a b i}=K_{a b i}^{\mathrm{eq}}+\sum_{t}^{\text {mode }} \frac{\partial K_{a b i}}{\partial S_{t, i}} S_{t, i},
\tag{13b}
$$

where $Q^{\text{eq}}$ and $K^{\text{eq}}$ are the values of equilibrium molecular conformation in the gas phase. The internal coordinates $S_t$ of $\mathrm{H_2O}$ are defined as

$$
S_{1}=\frac{1}{\sqrt{2}}\left(\Delta r_{1}+\Delta r_{2}\right),
\tag{14a}
$$

$$
S_{2}=\Delta \theta,
\tag{14b}
$$

$$
S_{3}=\frac{1}{\sqrt{2}}\left(\Delta r_{1}-\Delta r_{2}\right),
\tag{14c}
$$

where the definition of $r_1$, $r_2$, and $\theta$ are given in Fig. 1. The derivative quantities, $\partial Q/\partial S$ and $\partial K/\partial S$, in Eq. (13) are related to the Cartesian derivatives as follows:

$$
\frac{\partial Q_{a i}}{\partial S_{t, i}}=\sum_{p}^{x, y, z} \sum_{b}^{\text {site }} \frac{\partial Q_{a i}}{\partial x_{p, b i}} \frac{\partial x_{p, b i}}{\partial S_{t, i}},
\tag{15a}
$$

$$
\frac{\partial K_{a b i}}{\partial S_{t, i}}=\sum_{p}^{x, y, z} \sum_{b}^{\text {site }} \frac{\partial K_{a b i}}{\partial x_{p, b i}} \frac{\partial x_{p, b i}}{\partial S_{t, i}},
\tag{15b}
$$

where $x_{p,bi}$ is the Cartesian coordinate for $p$th $(x,y,z)$ direction of the site $b$ of the $i$th molecule. $\partial x_{p,bi}/\partial S_{t,i}$ is called the $B^{-1}$ matrix, which has $(3N_s)\times(3N_s-6)$ ($N_s$ is the number of sites in a molecule) dimension for each molecule. Note that the $B^{-1}$ is usually obtained from the $B$ matrix, $B_{t,pb}$ $=\partial S_t/\partial x_{p,pb}$, by $\boldsymbol{B}^{\dagger}(\boldsymbol{B}\boldsymbol{B}^{\dagger})^{-1}$, where $\boldsymbol{B}^{\dagger}$ is a transpose of $\boldsymbol{B}$. The $B^{-1}$ matrix thus obtained is not the true inverse of $B$, but satisfies the one-sided relation, $B\cdot B^{-1}=I$, where $I$ is the unit matrix of $(3N_s-6)\times(3N_s-6)$ dimension. The transformation relation of Eq. (15) is valid as $Q$ and $K$ are functions of internal coordinates, but not of translational or rotational coordinates.

$Q^{\text{eq}}$, $K^{\text{eq}}$, $\partial Q/\partial S$, and $\partial K/\partial S$ in Eqs. (13) and (15) are determined by the quantum chemical calculations of B3LYP/d-aug-cc-PVDZ$^{59,60}$ with the GAMESS-U.K. package$^{61}$ modified by our group. $^{45}$ The Cartesian derivatives $\partial X/\partial x$ ($X=Q$ and $K$) were calculated by five-point numerical differentiation. The results are summarized in Table II.

### III. LOCAL FIELD AND DIELECTRIC INTERACTION

The second-order nonlinear susceptibility of the interface system $\chi$ is a third rank tensor, composed of the vibrationally resonant part $\chi^{\text{R}}$ and the nonresonant part $\chi^{\text{NR}}$,

$$
\chi_{p q r}=\chi_{p q r}^{\mathrm{R}}+\chi_{p q r}^{\mathrm{NR}}.
\tag{16}
$$

In the time-dependent representation, $\chi_{pqr}^{\text{R}}$ is calculated by the following time correlation function of the polarizability tensor $A_{pq}$ and the dipole vector $M_r$:$^{18}$

$$
\chi_{p q r}^{\mathrm{R}}=\frac{i \omega_{I R}}{k_{B} T} \int_{0}^{\infty} d t \exp \left(i \omega_{I R} t\right)\left\langle A_{p q}(t) M_{r}(0)\right\rangle,
\tag{17}
$$

where $k_B$ and $T$ are the Boltzmann constant and temperature, and $\langle\cdots\rangle$ is the statistical average in the classical MD simulation. The nonresonant part $\chi^{\text{NR}}$ is assumed to be a constant in the IR frequency range in question, so as to be consistent with the experimental SFG spectrum.

In the following, we derive the formulation of $A$ and $M$ in the CRK model with appropriate local field correction factor. We also give the corresponding expressions of $A$ and $M$ in the PD model for comparison, which has been employed in our previous studies.$^{18,31,62}$

### A. Calculation of $A$ and $M$ by the CRK model

At a given instantaneous configuration of the interface system $\{\boldsymbol{r}_{ai}\}$, the partial charge $Q_{ai}$ and the electrostatic potential $V_{ai}$ are given by Eqs. (5) and (6). These self-consistent conditions are modified under an external field $\boldsymbol{E}_0$ as

$$
Q_{a i}=Q_{a i}^{0}+\sum_{b}^{\text {site }} K_{a b i} V_{b i},
\tag{18a}
$$

$$
V_{a i}=-\boldsymbol{r}_{a i} \cdot \boldsymbol{E}_{0}+\sum_{j(\neq i)} \sum_{b}^{\text {site }} \frac{f_{a i, b j} Q_{b j}}{r_{a i, b j}},
\tag{18b}
$$

where $Q_{ai}^0$ and $K_{abi}$ are functions of the internal coordinates $S_i$.

From the set of equations, Eq. (18), we have

$$
\begin{aligned}
& \sum_{j} \sum_{c}^{\text {site }}\left(\delta_{a c} \delta_{i j}-\sum_{b}^{\text {site }} \frac{f_{a i, b j} K_{b c j}}{r_{a i, b j}}\right) V_{c j} \\
& \quad=-\boldsymbol{r}_{a i} \cdot \boldsymbol{E}_{0}+\sum_{j(\neq i)} \sum_{b}^{\text {site }} \frac{f_{a i, b j} Q_{b j}^{0}}{r_{a i, b j}},
\end{aligned}
\tag{19a}
$$

$$
\begin{aligned}
& \sum_{j} \sum_{c}^{\text {site }}\left(\delta_{a c} \delta_{i j}-\sum_{b}^{\text {site }} \frac{f_{b i, c j} K_{a b i}}{r_{b i, c j}}\right) Q_{c j} \\
& \quad=Q_{a i}^{0}-\sum_{b}^{\text {site }} K_{a b i}\left(\boldsymbol{r}_{b i} \cdot \boldsymbol{E}_{0}\right).
\end{aligned}
\tag{19b}
$$

Then we define $G$, $G^T$ as

<table>
<caption>TABLE II. Partial charge $Q_a$, CRK $K_{ab}$, and their derivatives with respect to the internal coordinates $S_t$ of H₂O (in a.u.).</caption>
<tbody>
<tr>
<td colspan="2">$Q_a^{\text{eq}}$</td>
<td colspan="5">$K_{ab}^{\text{eq}}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$b=1$</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
</tr>
<tr>
<td>$a=1$ O</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>2 H</td>
<td>0.329</td>
<td>0.000</td>
<td>−3.271</td>
<td>−0.779</td>
<td>2.025</td>
<td>2.025</td>
</tr>
<tr>
<td>3 H</td>
<td>0.329</td>
<td>0.000</td>
<td>−0.779</td>
<td>−3.271</td>
<td>2.025</td>
<td>2.025</td>
</tr>
<tr>
<td>4 X</td>
<td>−0.329</td>
<td>0.000</td>
<td>2.025</td>
<td>2.025</td>
<td>−4.298</td>
<td>0.248</td>
</tr>
<tr>
<td>5 X</td>
<td>−0.329</td>
<td>0.000</td>
<td>2.025</td>
<td>2.025</td>
<td>0.248</td>
<td>−4.298</td>
</tr>
<tr>
<td colspan="2">$\partial Q_a/\partial S_t$</td>
<td colspan="5">$\partial K_{ab}/\partial S_t$</td>
</tr>
<tr>
<td colspan="7">$t=1$</td>
</tr>
<tr>
<td>1 O</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>2 H</td>
<td>−0.097</td>
<td>0.000</td>
<td>0.621</td>
<td>0.537</td>
<td>−0.579</td>
<td>−0.579</td>
</tr>
<tr>
<td>3 H</td>
<td>−0.097</td>
<td>0.000</td>
<td>0.537</td>
<td>0.621</td>
<td>−0.579</td>
<td>−0.579</td>
</tr>
<tr>
<td>4 X</td>
<td>0.097</td>
<td>0.000</td>
<td>−0.579</td>
<td>−0.579</td>
<td>0.038</td>
<td>1.120</td>
</tr>
<tr>
<td>5 X</td>
<td>0.097</td>
<td>0.000</td>
<td>−0.579</td>
<td>−0.579</td>
<td>1.120</td>
<td>0.038</td>
</tr>
<tr>
<td colspan="7">$t=2$</td>
</tr>
<tr>
<td>1 O</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>2 H</td>
<td>0.060</td>
<td>0.000</td>
<td>−1.784</td>
<td>−3.362</td>
<td>2.573</td>
<td>2.573</td>
</tr>
<tr>
<td>3 H</td>
<td>0.060</td>
<td>0.000</td>
<td>−3.362</td>
<td>−1.784</td>
<td>2.573</td>
<td>2.573</td>
</tr>
<tr>
<td>4 X</td>
<td>−0.060</td>
<td>0.000</td>
<td>2.573</td>
<td>2.573</td>
<td>−2.706</td>
<td>−2.440</td>
</tr>
<tr>
<td>5 X</td>
<td>−0.060</td>
<td>0.000</td>
<td>2.573</td>
<td>2.573</td>
<td>−2.440</td>
<td>−2.706</td>
</tr>
<tr>
<td colspan="7">$t=3$</td>
</tr>
<tr>
<td>1 O</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>2 H</td>
<td>−0.049</td>
<td>0.000</td>
<td>1.342</td>
<td>0.000</td>
<td>−0.671</td>
<td>−0.671</td>
</tr>
<tr>
<td>3 H</td>
<td>0.049</td>
<td>0.000</td>
<td>0.000</td>
<td>−1.342</td>
<td>0.671</td>
<td>0.671</td>
</tr>
<tr>
<td>4 X</td>
<td>0.000</td>
<td>0.000</td>
<td>−0.671</td>
<td>0.671</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>5 X</td>
<td>0.000</td>
<td>0.000</td>
<td>−0.671</td>
<td>0.671</td>
<td>0.000</td>
<td>0.000</td>
</tr>
</tbody>
</table>

$$
[G]_{a i, c j}=\delta_{a c} \delta_{i j}-\sum_{b}^{\text {site }} \frac{f_{a i, b j} K_{b c j}}{r_{a i, b j}}, \quad(20 \mathrm{a})
$$

$$
\left[G^{T}\right]_{a i, c j}=\delta_{a c} \delta_{i j}-\sum_{b}^{\text {site }} \frac{f_{b i, c j} K_{a b i}}{r_{b i, c j}}, \quad(20 \mathrm{~b})
$$

$$
V_{a i}^{0}=\sum_{j(\neq i)}^{\text {site }} \sum_{b} \frac{f_{a i, b j} Q_{b j}^{0}}{r_{a i, b j}}, \quad(21)
$$

and Eq. (19) is solved for $V_{a i}$ and $Q_{a i}$ using the definitions,

$$
V_{a i}=\sum_{j}^{\text {site }} \sum_{c}\left[G^{-1}\right]_{a i, c j}\left[V_{c j}^{0}-\boldsymbol{r}_{c j} \cdot \boldsymbol{E}_{0}\right], \quad(22)
$$

$$
\begin{aligned}
Q_{a i} & =\sum_{j}^{\text {site }} \sum_{c}\left[G^{T-1}\right]_{a i, c j}\left[Q_{c j}^{0}-\sum_{b}^{\text {site }} K_{c b j}\left(\boldsymbol{r}_{b j} \cdot \boldsymbol{E}_{0}\right)\right] \\
& =\sum_{j}^{\text {site }} \sum_{c}\left[G^{-1}\right]_{c j, a i}\left[Q_{c j}^{0}-\sum_{b}^{\text {site }} K_{c b j}\left(\boldsymbol{r}_{b j} \cdot \boldsymbol{E}_{0}\right)\right],
\end{aligned}
$$

where we used the relation $\left[G^{T}\right]_{a i, c j}=[G]_{c j, a i}$. Consequently, the dipole moment of the whole interface system is defined as

$$
\begin{aligned}
\boldsymbol{M}= & \sum_{i}^{\text {site }} \sum_{a} Q_{a i} \boldsymbol{r}_{a i}=\sum_{i}^{\text {site }} \sum_{j}^{\text {site }} \sum_{a}^{\text {site }} \sum_{c}\left[G^{-1}\right]_{c j, a i} Q_{c j}^{0} \boldsymbol{r}_{a i} \\
& \left(\boldsymbol{E}_{0}=0\right).
\end{aligned}
$$

The last expression of Eq. (24) is valid under the condition with no external field. The polarizability tensor can be defined by differentiating the system dipole moment $\boldsymbol{M}$ with respect to external field $\boldsymbol{E}_{0}$:

$$
\begin{aligned}
\boldsymbol{A}= & \frac{\partial \boldsymbol{M}}{\partial \boldsymbol{E}_{0}}=\sum_{i}^{\text {site }} \sum_{a} \frac{\partial Q_{a i}}{\partial \boldsymbol{E}_{0}} \boldsymbol{r}_{a i}=-\sum_{i}^{\text {site }} \sum_{a}^{\text {site }} \sum_{b}^{\text {site }} K_{a b, i} \boldsymbol{r}_{a i} \\
& \otimes\left[\sum_{j}^{\text {site }} \sum_{c}\left[G^{-1}\right]_{b i, c j} \boldsymbol{r}_{c j}\right] \quad\left(\boldsymbol{E}_{0}=0\right),
\end{aligned}
$$

where $\otimes$ denotes the tensor product. Inserting Eqs. (24) and (25) into Eq. (17) gives an expression of $\chi^{\mathrm{R}}$. However, this expression of $\chi^{\mathrm{R}}$ corresponds to the bare polarization of sum frequency generated by the visible and infrared lights. The generated polarization of sum frequency induces dielectric coupling with surrounding molecules and thereby additional polarization. $^{63,64}$ To take account of the dielectric coupling of the output frequency, $\boldsymbol{A}$ in Eq. (25) should be modified as

$$
\begin{aligned}
\boldsymbol{A}^{\mathrm{eff}}= & -\sum_{i}^{\text {site }} \sum_{a}^{\text {site }} \sum_{b} K_{a b i}\left[\sum_{c^{\prime} j^{\prime}}\left[G^{-1}\right]_{a i, c^{\prime} j^{\prime}} \boldsymbol{r}_{c^{\prime} j^{\prime}}\right] \\
& \otimes\left[\sum_{c j}\left[G^{-1}\right]_{b i, c j} \boldsymbol{r}_{c j}\right].
\end{aligned}
\tag{26}
$$

The phenomenological second-order resonant susceptibility $\chi^{\mathrm{R}}$ is obtained by substituting Eqs. (24) and (26) into Eq. (17). Hereafter we omit the suffix eff in Eq. (26) in the calculation of $\chi^{\mathrm{R}}$.

### B. Calculation of $\boldsymbol{A}$ and $\boldsymbol{M}$ by PD model

In the PD model, electronic polarization is represented with a molecular (or site) polarizability which generates the induced dipole moment under an electric field. The intermolecular electrostatic interaction is thus carried by the partial charges and the dipole moments. In the following formulation, the point polarizability and the dipole are located on the center of mass of each molecule $\boldsymbol{r}_{i}$, while the partial charges are on the sites $\boldsymbol{r}_{a i}$. In the PD model, the essentially equivalent discussion with that of the CRK model can be given for the dielectric coupling. In this subsection, the suffixes $p, q, r, \cdots$ refer to the Cartesian components $x \sim z$.

Suppose that each molecule $i$ has a polarizability $\alpha_{p q, i}$ and the permanent dipole $\mu_{p, i}^{0}$ at $\boldsymbol{r}_{i}$. In the condensed phase, the $i$ th molecule has the (permanent+induced) dipole $\mu_{p, i}$ under the electric field acting on the molecule, $E_{p, i}$. Then the self-consistent conditions between $\mu_{p, i}$ and $E_{p, i}$ are expressed as
$$
\mu_{p, i}=\mu_{p, i}^{0}+\sum_{q}^{x, y, z} \alpha_{p q, i} E_{q, i},
\tag{27a}
$$

$$
E_{p, i}=E_{p}^{0}+E_{p, i}^{0}-\sum_{j(\neq i)} \sum_{q}^{x, y, z} T_{p, i ; q, j} \mu_{q, j},
\tag{27b}
$$
where $E_{p}^{0}$ is the homogeneous external field, $E_{p, i}^{0}$ is the electric field at the $i$ th molecule that is generated by the point charges of surrounding molecules $j(\neq i)$, and $T_{p, i ; q, j}$ is the so-called dipole-dipole interaction tensor. $^{65}$ Here we write explicitly $E_{p, i}^{0}$ and $T_{p, i ; q, j}$:
$$
E_{p, i}^{0}=\sum_{j(\neq i)}^{\text {site }} \sum_{b} \frac{f_{i, b j} Q_{b j}}{r_{i, b j}^{3}} r_{p ; i, b j},
\tag{28}
$$

$$
T_{p, i ; q, j}=\frac{4 w_{i j}^{3}-3 w_{i j}^{4}}{r_{i j}^{3}} \delta_{p q}-\frac{3 w_{i j}^{4}}{r_{i j}^{5}} r_{p ; i, j} r_{q ; i, j},
\tag{29}
$$
where $r_{p ; i, b j}=\left[\boldsymbol{r}_{i}-\boldsymbol{r}_{b j}\right]_{p}, r_{p ; i, j}=\left[\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right]_{p}, r_{i, b j}=\left|\boldsymbol{r}_{i}-\boldsymbol{r}_{b j}\right|$, and $r_{i j}=\left|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right|$. $\delta_{p q}$ denotes Kronecker's delta. $f$ and $w$ are the damping functions for the electric field and the dipole tensor, respectively, in the PD model, $^{56}$ where their functional forms are of modified Thole-type by Bernardo $e t a l .^{48}$

From the set of equations, Eq. (27), we have
$$
\begin{aligned}
& \sum_{j} \sum_{r}^{x, y, z}\left(\delta_{p r} \delta_{i j}+\sum_{q}^{x, y, z} T_{p, i ; q, j} \alpha_{q r, j}\right) E_{r, j} \\
& \quad=E_{p}^{0}+E_{p, i}^{0}-\sum_{j(\neq i)} \sum_{q}^{x, y, z} T_{p, i ; q, j} \mu_{q, j}^{0},
\end{aligned}
\tag{30a}
$$

$$
\begin{aligned}
& \sum_{j} \sum_{r}^{x, y, z}\left(\delta_{p r} \delta_{i j}+\sum_{q}^{x, y, z} \alpha_{p q, i} T_{q, i ; r, j}\right) \mu_{r, j} \\
& \quad=\mu_{p, i}^{0}+\sum_{q}^{x, y, z} \alpha_{p q, i}\left(E_{q}^{0}+E_{q, i}^{0}\right).
\end{aligned}
\tag{30b}
$$

Then the following matrixes $\mathcal{G}$ and $\mathcal{G}^{T}$ are introduced:
$$
[\mathcal{G}]_{p i, r j}=\delta_{p r} \delta_{i j}+\sum_{q}^{x, y, z} T_{p, i ; q, j} \alpha_{q r, j},
\tag{31a}
$$

$$
\left[\mathcal{G}^{T}\right]_{p i, r j}=\delta_{p r} \delta_{i j}+\sum_{q}^{x, y, z} \alpha_{p q, i} T_{q, i ; r, j},
\tag{31b}
$$
and Eq. (30) is solved for $E_{p, i}$ and $\mu_{p, i}$,
$$
E_{p, i}=\sum_{j} \sum_{r}^{x, y, z}\left[\mathcal{G}^{-1}\right]_{p i, r j}\left[E_{r}^{0}+E_{r, j}^{0}-\sum_{j(\neq i)} \sum_{q}^{x, y, z} T_{r, j ; q, i} \mu_{q, i}^{0}\right],
\tag{32}
$$

$$
\begin{aligned}
\mu_{p, i} & =\sum_{j} \sum_{r}^{x, y, z}\left[\mathcal{G}^{T-1}\right]_{p i, r j}\left[\mu_{r, j}^{0}+\sum_{q}^{x, y, z} \alpha_{r q, j}\left(E_{q}^{0}+E_{q, j}^{0}\right)\right] \\
& =\sum_{j} \sum_{r}^{x, y, z}\left[\mathcal{G}^{-1}\right]_{r j, p i}\left[\mu_{r, j}^{0}+\sum_{q}^{x, y, z} \alpha_{r q, j}\left(E_{q}^{0}+E_{q, j}^{0}\right)\right], \quad(33)
\end{aligned}
$$
where we used the relation $\left[\mathcal{G}^{T}\right]_{p i, r j}=[\mathcal{G}]_{r j, p i}$. Here we define the local field factor for the molecule $i$,
$$
\mathfrak{F}_{p, r}^{i}=\sum_{j}\left[\mathcal{G}^{-1}\right]_{p i, r j}.
\tag{34}
$$

Using Eqs. (33) and (34), we have the expression for the dipole moment of the interface system $\boldsymbol{M}$,
$$
\begin{aligned}
M_{p}=\sum_{i} \mu_{p, i}= & \sum_{i} \sum_{j} \sum_{r}^{x, y, z}\left[\mathcal{G}^{-1}\right]_{r j, p i} \\
& \times\left[\mu_{r, j}^{0}+\sum_{q}^{x, y, z} \alpha_{r q, j}\left(E_{q}^{0}+E_{q, j}^{0}\right)\right] \\
= & \sum_{j} \sum_{r}^{x, y, z} \mathfrak{F}_{r, p}^{j}\left[\mu_{r, j}^{0}+\sum_{q}^{x, y, z} \alpha_{r q, j} E_{q, j}^{0}\right] \quad\left(\boldsymbol{E}^{0}=0\right),
\end{aligned}
\tag{35}
$$
where the last expression is valid under no external field ($E_{q}^{0}=0$). The system polarizability $\boldsymbol{A}$ is also given as

$$
A_{p,q}=\frac{\partial M_{p}}{\partial E_{q}^{0}}=\sum_{j}^{x,y,z} \sum_{r} \mathfrak{F}_{r,p}^{j} \alpha_{r q, j}.
$$

As in the case of the CRK model, we take account of the dielectric coupling of the output frequency. Thus the effective polarizability to describe $\chi^{\mathrm{R}}$ becomes

$$
A_{p, q}=\sum_{j}^{x, y, z} \sum_{r}^{x, y, z} \sum_{s}^{x, y, z} \mathfrak{F}_{r, p}^{j} \mathfrak{F}_{s, q}^{j} \alpha_{r s, j}. \tag{36}
$$

We note that the expressions of $M$ and $A$ in Eqs. (35) and (36) in the PD model are equivalent to the expressions in Eqs. (24) and (26) in the CRK model. The second-order resonant susceptibility $\chi^{\mathrm{R}}$ in the PD model is calculated by substituting Eqs. (35) and (36) into Eq. (17).

## IV. MD CALCULATION OF WATER PROPERTIES

### A. MD procedure

The MD simulations of pure water system with the CRK model are executed using a slab geometry of liquid in the rectangular simulation cell with dimensions of $L_x \times L_y \times L_z$ $=30 \times 30 \times 150 \ \mathring{\mathrm{A}}^3$, where the gas-liquid interfaces are normal to the $z$ axis. The number of molecules per each cell is 500, which is a half number of the previous study $^{56}$ but is enough to simulate pure water surfaces that form a thin interface thickness $\sim 3$ Å. For the correction of the long-range electrostatic forces, the Ewald summation method is employed, $^{66}$ where the Ewald separation parameter is set to $0.242 \ \mathring{\mathrm{A}}^{-1}$, and the real and reciprocal-space cutoffs are 13 $\mathring{\mathrm{A}}$ and $1.47 \ \mathring{\mathrm{A}}^{-1}$ respectively, the values of which are the optimized parameters to maximize computational performance. $^{67}$ The van der Waals and the real part of the electrostatic interactions were calculated with the cutoff length of $13$ Å, and the Verlet neighbor list $^{66}$ is employed for these calculations with a shell thickness of $2$ Å. The damping function $f$ in Eq. (5) acts only on the real space part. $^{40,56}$ For comparison, we also performed the MD simulation using the PD model $^{56}$ with the same conditions, except for the different short-range damping functions as mentioned in Sec. III B.

Newton's equations of motion are integrated numerically using the velocity Verlet algorithm $^{66}$ with a time step of 0.61 fs. At each time step, Eqs. (5) and (6) for the self-consistent induced charges in the CRK model is solved iteratively until the convergence is obtained, where the average root mean square differences of the induced charges for successive iterations, $\sqrt{\sum_{a i}\left|Q_{a i}(\text { new })-Q_{a i}(\text { old })\right|^{2} / N}$, is below a threshold of $1.0 \times 10^{-7}$ (a.u.). For the threshold condition of the PD model, refer to Ref. 56. In the calculation of local field correction factor $[G]$ for the CRK model and $\mathfrak{F}$ for the PD model, we employ not the Ewald summation scheme but the cutoff scheme with the cutoff length of $13$ Å to save computational time. We notice that the force fields calculation in MD simulation employs the Ewald summation method.

The molecules are initially placed with random displacements and orientations from cubic lattice points to form the slab geometry, and the initial velocities are randomized according to the Maxwell-Boltzmann distribution at a temperature of 298 K. The systems of 128 replicas are first equilibrated in parallel for 30 ps each, at the constant temperature using the Berendsen thermostat $^{68}$ with a coupling constant of 0.4 ps. Then, the statistical samplings are taken in parallel for a total of 60 ns under the $NVE$ ensemble, with the average kinetic temperature of 298 K.

The program code for the MD calculations was written by us. The MD calculations were performed on the Fujitsu Primequest at the Research Center for Computational Science, Okazaki, Japan.

### B. Bulk properties of CRK water model

In this section, we assess the reliability of the CRK water model for bulk properties of liquid water. We calculated and analyzed the bulk properties in the similar way as in our previous study using the PD water model. $^{56}$ Computational details are therefore described in Ref. 56.

In Table III, calculated results including density, enthalpy of vaporization, diffusion coefficient, and dipole moment in liquid phase are compared with the experimental values. The density and enthalpy of vaporization exhibit good agreement with the experiments. In fact, the Lennard-Jones parameters, $\sigma$ and $\epsilon$, and the width of the Gaussian charge distribution, $\xi$, in the molecular model were optimized to reproduce the density and enthalpy of vaporization. On the other hand, the diffusion coefficient of the CRK model tends to be underestimated. The average dipole moment of the CRK water in liquid is 3.22 D, which is consistent with the experimental value within the experimental error range. This value is close to the result of Car-Parrinello (CP) $ab$ initio MD study, 3.0 D. $^{69}$ The equilibrium configuration of water molecule will be discussed in Sec. IV C.

In Fig. 2, site-site radial distribution functions (RDFs) of the CRK water are shown with the experimental results of the neutron diffraction study. $^{70}$ One can see that the model RDFs are overstructured compared to the experiment, in particular for the first solvation peaks. This trend is similar to the CPMD result for the recommended fictitious electronic mass. $^{71}$ This agreement with the CPMD result may not be fortuitous because the charge distribution and its response to the electrostatic field in our CRK model are fitted to the DFT calculations. The discrepancy in the RDFs between our

<table>
<caption>TABLE III. Properties for bulk liquid water.</caption>
<thead>
  <tr>
    <th>Property</th>
    <th>CRK model</th>
    <th>Experiment</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Density (g/cm³)</td>
    <td>0.980</td>
    <td>0.997ᵃ</td>
  </tr>
  <tr>
    <td>Enthalpy of vaporization (kcal/mol)</td>
    <td>10.92</td>
    <td>10.51ᵇ</td>
  </tr>
  <tr>
    <td>Diffusion coefficient (10⁻⁹ m²/s)</td>
    <td>1.50</td>
    <td>2.30ᶜ</td>
  </tr>
  <tr>
    <td>Dipole moment (D)</td>
    <td>3.22ᵈ</td>
    <td>2.9±0.6ᵉ</td>
  </tr>
  <tr>
    <td>Equilibrium O–H bond length (Å)</td>
    <td>0.972</td>
    <td>0.970ᶠ</td>
  </tr>
  <tr>
    <td>Equilibrium H–O–H angle (deg)</td>
    <td>106.65</td>
    <td>106.06ᶠ</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="3">ᵃReference 85.</td>
  </tr>
  <tr>
    <td colspan="3">ᵇReference 86.</td>
  </tr>
  <tr>
    <td colspan="3">ᶜReference 87.</td>
  </tr>
  <tr>
    <td colspan="3">ᵈThis value is calculated with $f=f^{\text{Gauss}}$, while calculation with $f=1$ leads to 3.30 D (see Sec. V A).</td>
  </tr>
  <tr>
    <td colspan="3">ᵉReference 88.</td>
  </tr>
  <tr>
    <td colspan="3">ᶠReference 79.</td>
  </tr>
</tfoot>
</table>

![](./images/811813570739175424_4.jpg)

FIG. 2. (a) O–O, (b) O–H, and (c) H–H RDFs for the liquid water calculated with the CRK model. The dashed lines indicate experimental results (Ref. 70).

model (or CPMD water) and the experiment stems from neglect of the nuclear (proton) quantum motion, $^{71}$ and it is expected that the inclusion of quantum effects will cause an overall softening of the RDFs.

The O–H stretching vibrations in bulk liquid are manifested in the infrared (IR) and Raman spectra. Figure 3 shows the calculated result of the IR intensity ($\alpha^{\text{abs}}n(\omega)$) with the CRK model according to the formulae in Refs. 56 and 72 including a quantum correction of the harmonic approximation, $^{73–75}$

![](./images/811813570739175424_5.jpg)

FIG. 3. IR intensity of liquid water, $\alpha^{\text{abs}}(\omega)n(\omega)$, by experiment (Ref. 89) (black), and by the CRK model (blue and red) calculated with Eq. (37). The blue line refers to $C(t)=\boldsymbol{M}(0)\cdot\boldsymbol{M}(t)$, in which $\boldsymbol{M}$ is total (permanent +induced) dipole calculated by Eq. (24) with $f$=1 (See Sec. V A). The red line to $C(t)=\boldsymbol{M}^{\text{perm}}(0)\cdot\boldsymbol{M}^{\text{perm}}(t)$, where $\boldsymbol{M}^{\text{perm}}$ contains the permanent component only.

![](./images/811813570739175424_6.jpg)

FIG. 4. Calculated polarized (red line) and depolarized (blue line) Raman spectra, $(d^{2}\sigma_{\text{pol}}/d\omega d\Omega)$ and $(d^{2}\sigma/d\omega d\Omega)_{\perp}$, for the CRK water model. The inset shows the experimental Raman spectra (Ref. 90).

$$
\alpha^{\mathrm{abs}}(\omega) n(\omega)=\frac{2 \pi \omega^{2}}{3 V c k_{B} T} \int_{-\infty}^{\infty} d t e^{-i \omega t}\langle C(t)\rangle_{\mathrm{cl}},\qquad(37)
$$

where $\alpha^{\text{abs}}(\omega)$ is the absorption coefficient, $n(\omega)$ is the real part of refractive index, $V$ is the volume, $c$ is the speed of light, and $\langle C(t)\rangle_{\text{cl}}$ denotes the classical time correlation function of the dipole moment. The blue line in Fig. 3 represents the spectrum with the time correlation function $C(t)$ $=\boldsymbol{M}(0)\cdot\boldsymbol{M}(t)$ in which $\boldsymbol{M}$ is the total (permanent+induced) dipole calculated by Eq. (24), while the red line is the spectrum with $C(t)=\boldsymbol{M}^{\text{perm}}(0)\cdot\boldsymbol{M}^{\text{perm}}(t)$ where $\boldsymbol{M}^{\text{perm}}$ is the permanent dipole component ($\boldsymbol{M}^{\text{perm}}=\sum_{i}\sum_{a}^{\text{site}}Q_{ai}^{0}\boldsymbol{r}_{ai}$). One can see that the peak frequency of the calculated IR spectrum at about $3400\ \text{cm}^{-1}$ is in good agreement with the experimental spectrum, whereas the IR intensity in the model with the peak height ($\sim12\ 000\ \text{cm}^{-1}$) is somewhat weaker than the experimental intensity ($\sim17\ 500\ \text{cm}^{-1}$). The recent result with flexible and polarizable POLIR model by Mankoo and Keyes $^{72}$ elucidated that the IR intensity and the peak position is strongly dependent on the value of site charge. Burnham et al. $^{76}$ examined several water model dependence of IR intensity and reported that IR peak height in their new flexible and polarizable TTM4-F model (or TTM2-F) is about $12\ 000\ \text{cm}^{-1}$, whereas that in the flexible and nonpolarizable model (e.g., TIP3P-F) is about $4000\ \text{cm}^{-1}$. Thus we can say that the present model shows comparable performance to the recent other flexible and polarizable models. Comparing the blue line with the red line in Fig. 3, one can see that the IR intensity only from the permanent component significantly decreases its intensity and is somewhat blueshifted. This is qualitatively consistent with the result by Ahlborn et al., $^{77}$ showing that the IR intensity is governed by the polarization. Auer and Skinner $^{78}$ also obtained similar results by their recent MD and elucidated that the IR spectrum is significantly redshifted from the distribution of local-mode frequencies with the maximum at about $3490\ \text{cm}^{-1}$ due to the non-Condon effects.

Figure 4 shows the calculated results of the polarized Raman and depolarized Raman [panel(b)] spectra with the CRK model according to the formulae in Ref. 56, where the inset in each panel is the experimental result for comparison. The calculated polarized Raman spectrum captures the double-peak nature but is somewhat blueshifted in comparison with the experimental spectrum. On the other hand, the calculated depolarized Raman spectrum well reproduces the experimental peak position and the asymmetric shape. Al-

![](./images/811813570739175424_7.jpg)

FIG. 5. Panel (a): Partial charge on a hydrogen site $Q_{\mathrm{H}}^{0}$. Panel (b): $\mathrm{O}-\mathrm{H}$ bond polarizability $\alpha_{\mathrm{O}-\mathrm{H}}^{\text {bond }}$ of water monomer as a function of $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle.

though the assignments of the polarized and depolarized spectra are somewhat controversial, it is elucidated by the earlier studies (see Ref. 78 and references therein) that the lower frequency band of the polarized Raman spectrum should be attributed to the collective mode while the depolarized spectrum well reflects the local mode frequency distribution due to the different angular factors.

### C. Equilibrium water geometry
Next we focus on the equilibrium geometry of water molecule in liquid phase. Table III shows that the equilibrium $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle by the CRK model is $106.65^{\circ}$, which is larger than that in the gas phase, $104.52^{\circ}$. This trend is consistent with the recent neutron diffraction experiment $^{79}$ and the $a b$ initio calculations, $^{80,81}$ while most flexible water models including our previous PD model $^{56}$ predict a smaller $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle in liquid phase than in gas phase. This is known as a common shortcoming of the previous flexible models. Burnham and Xantheas $^{37}$ addressed this problem by introducing geometric charge and polarizability and reported the increase in the equilibrium $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle from the gas phase value to the liquid phase value. Other recent models also reported increasing angles: $105.45^{\circ}$ by TTM3-F, $^{41}$ $107.7^{\circ}$ by TTM4-F, $^{76}$ and $106.4^{\circ}$ by POLIR. $^{72}$ The present CRK water model, which properly takes account of the geometry dependence of charge and polarizability through Eqs. (13) and (15), provides further insight into the mechanism of this conformational difference in liquid.

We examined the dependence of partial charges and CRK of an isolated water molecule with varying $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle $\theta$ by the DFT calculation. Figure 5(a) shows the partial charge of a hydrogen site $Q_{\mathrm{H}}^{0}$ in the range of $90^{\circ}<\theta$ $<130^{\circ}$, with the $\mathrm{O}-\mathrm{H}$ bond length fixed at $r_{0}=0.9572 \AA$. This panel shows that the absolute partial charge of hydrogen monotonically increases with the $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle, indicating that the $\mathrm{O}-\mathrm{H}$ bond becomes increasingly polar. This is qualitatively understood from the valence bond picture that the increasing $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle augments the $s$ character in the hybrid orbitals of the oxygen. $^{1}$ The change in $\mathrm{O}-\mathrm{H}$ bond polarity implies that a water molecule with a larger $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle can form stronger H-bonds.

We also found that the geometry dependence of the CRK plays an important role in stabilization. To discuss the role of polarization in the H-bonding environment, the $\mathrm{O}-\mathrm{H}$ bond polarizability is defined as a function of the $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle $\theta$ in the followings. Suppose the $\mathrm{O}-\mathrm{H}_{1}$ moiety in Fig. 1 lies under a local electric field $\Delta E$ along the $\mathrm{O}-\mathrm{H}_{1}$ bond. This situation is represented by the CRK model that $\mathrm{H}_{1}$ site is exposed to the electrostatic potential of $-\Delta E \cdot r_{0}$, and two $\mathrm{X}$ sites (and $\mathrm{O}$ site) to $\Delta E \cdot r_{0}$. Consequently, the induced partial charge at the $\mathrm{H}_{1}$ site is
$$
\begin{aligned}
\Delta Q_{\mathrm{H}_{1}} & =K_{\mathrm{H}_{1}, \mathrm{X}_{1}}\left(\Delta E r_{0}\right)+K_{\mathrm{H}_{1}, \mathrm{X}_{2}}\left(\Delta E r_{0}\right)+K_{\mathrm{H}_{1}, \mathrm{H}_{1}}\left(-\Delta E r_{0}\right) \\
& =\left(K_{\mathrm{H}_{1}, \mathrm{X}_{1}}+K_{\mathrm{H}_{1}, \mathrm{X}_{2}}-K_{\mathrm{H}_{1}, \mathrm{H}_{1}}\right) \Delta E r_{0}.
\end{aligned}
$$

Thus the induced $\mathrm{O}-\mathrm{H}_{1}$ bond dipole along the bond direction is
$$
\Delta \mu_{\mathrm{O}-\mathrm{H}_{1}}=\Delta Q_{\mathrm{H}_{1}} \cdot r_{0}=\left(K_{\mathrm{H}_{1}, \mathrm{X}_{1}}+K_{\mathrm{H}_{1}, \mathrm{X}_{2}}-K_{\mathrm{H}_{1}, \mathrm{H}_{1}}\right) \Delta E r_{0}^{2},
$$
where the origin of the dipole is set at the $\mathrm{O}$ site. Accordingly, the $\mathrm{O}-\mathrm{H}_{1}$ bond polarizability $\alpha_{\mathrm{O}-\mathrm{H}_{1}}^{\text {bond }}$ is defined as
$$
\alpha_{\mathrm{O}-\mathrm{H}_{1}}^{\text {bond }}=\frac{\Delta \mu_{\mathrm{O}-\mathrm{H}_{1}}}{\Delta E}=\left(K_{\mathrm{H}_{1}, \mathrm{X}_{1}}+K_{\mathrm{H}_{1}, \mathrm{X}_{2}}-K_{\mathrm{H}_{1}, \mathrm{H}_{1}}\right) r_{0}^{2}. \quad \text { (38) }
$$

The bond polarizability for the other $\mathrm{O}-\mathrm{H}_{2}$ moiety is defined in the same way. In Fig. 5(b), $\alpha_{\mathrm{O}-\mathrm{H}_{1}}^{\text {bond }}$ is plotted as a function of $\theta$, indicating that the bond polarizability also monotonically increases with the $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle. The larger bond polarizability of $\mathrm{O}-\mathrm{H}$ moieties should result in enhanced polarity of $\mathrm{O}-\mathrm{H}$ bonds in liquid water and thus contribute to the H-bonding stabilization.

In the above discussion, the geometry dependence of both the partial charge $Q_{a}^{0}$ and the CRK $K_{a b}$ arguably prefers a larger $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle in the H-bonding environment in liquid. To assess the relative importance of $Q_{a}^{0}$ and $K_{a b}$ in the geometric perturbation, we decompose the solvation energy for a single molecule into two components, i.e.,
$$
\begin{aligned}
& \sum_{a}^{\text {site }} Q_{a} V_{a}-\sum_{a}^{\text {site }} \sum_{b}^{\text {site }} K_{a b} V_{a} V_{b} / 2 \\
& \quad=\sum_{a}^{\text {site }} Q_{a}^{0} V_{a}+\sum_{a}^{\text {site }} \sum_{b}^{\text {site }} K_{a b} V_{a} V_{b} / 2,
\end{aligned}
$$
and compare the sensitivity of the two terms with respect to $\theta(=S_{2})$. The derivatives of two terms are estimated to be $\Sigma_{a}(\partial Q_{a}^{0} / \partial S_{2}) V_{a}=-4.173 kcal / mol$ and $\Sigma_{a} \Sigma_{b}(\partial K_{a b} / \partial S_{2}) V_{a} V_{b} / 2=-9.975 kcal / mol$ , where the average solvation potential $V_{a}$ was provided by our MD simulation, $V_{\mathrm{H}}=-1.714 ×10^{-2}$ a.u. and $V_{\mathrm{X}}=3.845 ×10^{-2}$ a.u. This estimatation implies that the latter term has a dominant effect on the stabilization by increasing $\theta$. To confirm this argument, we carried out two test MD simulations of bulk liquid water, (i) and (ii). Case (i) assumes $\partial Q / \partial S=0$ in Eq. (13a) while the $\partial K / \partial S$ terms are left intact in Eq. (13b). Case (ii) assumes $\partial K / \partial S=0$ while $\partial Q / \partial S$ is left intact. These MD simulations showed that the equilibrium $\mathrm{H}-\mathrm{O}-\mathrm{H}$ angle

changed from $106.65^\circ$ in the original liquid to $104.46^\circ$ in case (i), and to $99.09^\circ$ in case (ii). These results show that case (ii) gives larger perturbation than case (i), implying that the geometry dependence of $K$ is more important in the perturbation on the equilibrium angle.

In summary, a water molecule has enhanced polarity of O–H bonds with increasing H–O–H angle, both permanent and induced components. The enhanced polarity therefore allows stronger H-bonds and further stabilization in liquid. In particular, the enhancement of the O–H bond polarizability by increasing H–O–H angle is the main source for the stabilization in the H-bonding environment. We also note in passing in Table III that the equilibrium O–H length of the CRK model slightly increases from $0.957$ Å in gas phase to $0.972$ Å in liquid, which is shown to be in good agreement with the experiment.

### D. Orientational structure of pure water surface

The orientation of surface water is analyzed using the CRK model. The purposes of the present analysis are twofold. One is to compare the orientational structure obtained by the CRK model to the previous study with the PD water.⁵⁶ The other is to clarify the orientational correlation between a pair of water molecules at the surface. This information on orientational correlation will assist our understanding of the SFG spectroscopy in Sec. V D.

The orientation of surface water is determined with two angles, $\theta_{\text{dip}}$ and $\varphi$, as illustrated in the inset of Fig. 6. $\theta_{\text{dip}}$ is the angle between the water permanent dipole vector and the surface normal vector, and $\varphi$ is a dihedral angle between the molecular plane and the plane containing the surface normal and the permanent dipole. We also define the depth coordinate from the Gibbs dividing surface, $\hat{z}=z-z_{\text{Gibbs}}$, where $z$ is the normal coordinate to the surface. This definition means that $\hat{z}=0$ is the location of the Gibbs dividing surface, and that positive (negative) region $\hat{z}>0(\hat{z}<0)$ refers to the gas (liquid) side, respectively.

Figure 6 shows the present MD results of two-dimensional $(\cos\,\theta,\varphi)$ orientational distribution with varying depth $\hat{z}$, where the displacement from isotropic distribution is displayed for each layer of $\hat{z}$, $P'(\cos\,\theta_{\text{dip}},\varphi;\hat{z})$$=P(\cos\,\theta_{\text{dip}},\varphi;\hat{z})-\langle P\rangle(\hat{z})$, where $\langle P\rangle$ is the orientational average of probability. The orientational structure of the CRK water quite resembles that of the PD water in our previous study,⁵⁶ indicating that the orientational structure of water surface is rather robust irrespective of the details of water model. To summarize the noteworthy features, a major orientation in the vapor side of the Gibbs dividing surface is illustrated as configuration (a) in Fig. 6, which is characterized with the “dangling (free)” OH moieties. This conformation (a) becomes less frequent in the liquid side, where the dominant conformations are (b)–(e) in Fig. 6. Note that the conformations (b)–(d) are analogous in the sense that the molecular plane is roughly parallel to the surface.

![](./images/811813570739175424_8.jpg)

FIG. 6. Orientational probability distributions of water molecules, $P'(\cos\,\theta_{\text{dip}},\varphi;\hat{z})$, for the present CRK model. The definitions of $\theta_{\text{dip}}$ and $\varphi$ are illustrated in the lower right inset. The blue regions refer to higher probabilities than the isotropic average $(P'>0)$, while the red region to lower probabilities $(P'<0)$. The major orientations labeled (a)–(e) are illustrated in the right side.

In what follows, we analyze the orientational correlation of a H-bonding pair of water at the interface. To take statistics of various conformations, we classify the molecular orientation $(\cos\,\theta_{\text{dip}},\varphi)$ into three classes, (a), (b–d), and (e), as defined in Fig. 7. Though this classification is somewhat arbitrary, the three classes should have equal population for the isotropic orientational distribution. During the MD trajectories, we sampled the orientation of surface water molecules, whose centers of mass are located in the range of $-1.5$ Å$<\hat{z}<1.5$ Å, and obtained the population ratio 1.00:1.37:1.34 for (a):(b,c,d):(e).

Next we investigate the H-bonding pair of surface water. Of the several H-bond definitions,⁸² we adopt a geometric definition consisting of the following two criteria: $\text{H}\cdots\text{O}$ distance being $<2.5$ Å and $\angle\text{O-H}\cdots\text{O}$ being $>140^\circ$. By applying this definition to the MD trajectories, we obtained the conformational statistics of H-bonding donor-acceptor pairs of the surface water in $-1.5$ Å$<\hat{z}<1.5$ Å. The results are summarized in Table IV. One can generally see that the orientation (b,c,d) tends to become a H-bond donor. In particular, the most probable H-bonding pair of surface water is

![](./images/811813570739175424_9.jpg)

FIG. 7. Present definition of molecular orientations (a), (b,c,d), and (e) in Fig. 6 on the $( \cos \theta_{\text{dip}}-\varphi )$ plane.

donor (b,c,d)-acceptor (e), which is schematically illustrated in Fig. 14. A plausible reason why the orientation (b,c,d) likely becomes a H-bonding donor to another surface water may be explained by the fact that a water with the orientation (b,c,d) can readily provide two donor bonds to other surface water molecules.

## V. ANALYSIS OF NONLINEAR SUSCEPTIBILITY

In this section, the CRK model is used to calculate and analyze the nonlinear susceptibility of water surface. An emphasis is put on the accurate treatment of the short-range damping function, which has significant influence on the spectral shape.

### A. Appropriate damping treatment

As stated in Secs. II and III, the short-range damping function for the electrostatic interactions is necessary for polarizable MD simulations to be stably performed. While this fact demonstrates that electrostatic interactions between point charges (or dipoles) are not realistic enough in a short range, accurate modeling of short-range interactions is a challenging issue. The empirical prescriptions to remedy the shortcoming of point charge models require definite justification. In the present work, we need to calculate the electrostatic properties, such as dipole moment and polarizability tensor, as well as the force field using the same polarizable model. It is not apparent that the same treatment of the short-range damping works with equal accuracy for the calculations of the force field and the electrostatic properties.

To examine the damping function for the present model, we investigated the water-water interaction for water dimer with varying configurations. DFT calculations of B3LYP/d-aug-cc-pVDZ level were performed for the total energy and dipole moment as reference values, and the results are compared with the calculations by the CRK model. Here we assume the damping function for the CRK model to be the Gaussian type in Sec. II A, $f=f^{\text{Gauss}}(\xi)$, and examine the parameter $\xi$. We note that the point charge model without damping $(f=1)$ corresponds to $\xi$=0.

Shown in Fig. 8(a) is the equilibrium water dimer configuration by the DFT, where the direction of the $x$ axis is defined along the centers of mass of water molecules in the equilibrium configuration. $r_{\text{OH}}$ is the distance between the donor hydrogen and the accepter oxygen, and the equilibrium value of $r_{\text{OH}}$ is calculated to be $1.946$ $\text{\AA}$.

Then we discuss the conformational dependence of dimer properties with varying $r_{\text{OH}}$. Here we focus on the range of $r_{\text{OH}}$ smaller than the equilibrium distance $1.946$ $\text{\AA}$ to investigate the short-range interaction, and also larger than $1.5$ $\text{\AA}$, where the intermolecular O–H radial distribution function has a significant finite probability in liquid water [see Fig. 2(b)]. Regarding the other coordinates than $r_{\text{OH}}$, we treated them in two ways, case 1 and case 2. In case 1, the donor molecule moves as a whole along with $r_{\text{OH}}$ while the molecular conformation is fixed. In case 2, only the hydrogen atom under the H-bond moves along the $x$ direction while the other five nuclei are fixed.

In Fig. 8(b), the total energy of the dimer is plotted against $r_{\text{OH}}$ in case 1, where the origin of energy is set at the equilibrium separation. Comparing the DFT to the CRK results with varying $\xi$, the appropriate value to reproduce the intermolecular potential surface is near $\xi$=0.593 $\text{\AA}$, which is actually employed to the force field in the MD simulation. One can also see in panel (b) that the potential curve with $\xi$=0.0 $\text{\AA}$ (point charge approximation) does not reproduce the repulsive behavior, which is inconsistent to the DFT results. In panel (d), we investigated the total dipole moment along the $x$ direction in case 1. The result also supports the appropriateness of the damping treatment ($\xi$=0.593 $\text{\AA}$), and the point charge ($\xi$=0.0 $\text{\AA}$) is a somewhat crude approximation.

On the other hand, Fig. 8(c) shows the total dipole moment along the $x$ direction in case 2. In this case, one can see that the most appropriate value of $\xi$ to reproduce the dipole moment is near $\xi$=0.0 $\text{\AA}$ (point charge model), while $\xi$=0.593 $\text{\AA}$ describes poor $M_{x}$. Considering that the dipole derivative in case 2 is pertinent to the transition dipole for the O–H stretching vibration, we notice that the IR or vibrational SFG spectra of the O–H stretching under small $r_{\text{OH}}$ distance or strong H-bond should be more appropriately described with the point charge model ($\xi$=0.0 $\text{\AA}$). We note in passing that the behavior of total energy in case 2 (not shown) is dominated by the intramolecular potential and thus insensitive to $\xi$.

The above argument for the different short-range damping has been confirmed in our previous study using the PD

TABLE IV. Population ratios of H-bonding donor-acceptor pairs of surface water molecules. The ratios are normalized by the population of donor(a)-acceptor(a).

<table>
<thead>
<tr>
<th>Donor</th>
<th>Acceptor</th>
<th>Ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td>(a)</td>
<td>(a)</td>
<td>1.00</td>
</tr>
<tr>
<td>(a)</td>
<td>(b,c,d)</td>
<td>1.36</td>
</tr>
<tr>
<td>(a)</td>
<td>(e)</td>
<td>2.11</td>
</tr>
<tr>
<td>(b,c,d)</td>
<td>(a)</td>
<td>2.20</td>
</tr>
<tr>
<td>(b,c,d)</td>
<td>(b,c,d)</td>
<td>2.48</td>
</tr>
<tr>
<td>(b,c,d)</td>
<td>(e)</td>
<td>4.61</td>
</tr>
<tr>
<td>(e)</td>
<td>(a)</td>
<td>1.15</td>
</tr>
<tr>
<td>(e)</td>
<td>(b,c,d)</td>
<td>1.30</td>
</tr>
<tr>
<td>(e)</td>
<td>(e)</td>
<td>2.39</td>
</tr>
</tbody>
</table>

![](./images/811813570739175424_10.jpg)

FIG. 8. Properties of water dimer with varying configurations in cases 1 and 2 (see the text). (a) Equilibrium configuration by the DFT calculation. (b) Potential energy surfaces by the DFT and the CRK model calculations in case 1. The DFT calculations and the CRK calculations with different values of $\xi$ are denoted by different symbols as shown in the inset of panel (c). These notations are common in panels (b)-(d). (c) Dipole moments in the $x$ direction in case 2. (d) Dipole moments in the $x$ direction in case 1. (e) Partial charges of donor (blue) and acceptor (red) molecules in case 2. (f) Partial charges in case 1. The notations are same as in panel (e).

water model. $^{62}$ Figure 1 of Ref. 62 showed that the intermolecular force field prefers the appropriate damping function $f=f^{Thole}$ while the variation in the dipole moment is well described with $f=1$ (point charge/PD approximation).

The different behaviors of short-range damping in cases 1 and 2 is explained as follows. In the hydrogen-bonding system $[O\cdots H-O]$ in case 2, the $H-O$ chemical bond length increases with decreasing H-bond distance $r_{OH}$. In such situation, significant electron transfer takes place from the acceptor $H_{2}O$ to the donor $H_{2}O$. To examine the amount of charge transfer (CT), we performed the DFT calculations of partial site charges for the water dimer in the same way as we performed the CRK calculation for a monomer in Sec. II B, and then lamped the site charges of donor molecule and those of acceptor molecule separately. The results are displayed in Fig. 8(e), demonstrating the substantial CT is emphasized with decreasing $r_{OH}$ in case 2. On the other hand, the hydrogen-bonding system $[O\cdots H-O]$ in case 1, the $H-O$ chemical bond length is invariant with decreasing $r_{OH}$. Thus the CT is rather modest as shown in panel (f), in comparison with panel (e).

In the process of $O-H$ vibration under the strong hydrogen-bonding environment in case 2, the significant CT is accompanied by the stretching motion, which consequently augments the induced polarization. In the classical simulation, however, polarizable models do not allow CT between molecules in general. This mechanism elucidates the difference in cases 1 and 2 that the CRK model with the appropriate damping function $\xi=0.593$ Å works well in case 1 while it is insufficient to describe the strong perturbation in case 2. In order to take account of the augmented induced dipole in the strong H-bonding system, the point charge model provides an effective method in the polarizable MD simulation. Even when the point charge model is employed to describe the electrostatic properties, the force field in the polarizable MD should be presented with the appropriate damping function. The above discussion will be of significance for accurate description of the nonlinear susceptibility in Sec. V B.

### B. Results of nonlinear susceptibility

Figure 9 displays the real (blue) and the imaginary (red) parts of the nonlinear susceptibility, $\chi$, in the $ssp$ polarization combination for the water surface. Panel (a) is the experimental result by Ji et al., $^{51}$ while panels (b) and (c) are the calculated results with the present CRK model. Though the force field for the MD simulation is common in both panels, panel (b) adopted the damping function of $f=f^{Gauss}(\xi=0.593$ Å) in the calculations of $\chi$ in Sec. III, while panel (c) adopted no damping function, $f=1$. Comparing panels (b) and (c), one can see that the spectral shape is quite analogous except for the region from 3000 to $3200\ \text{cm}^{-1}$. Regarding the imaginary part $\text{Im}[\chi]$ (red lines), both (b) and (c) reproduce the positive peak at about $3700\ \text{cm}^{-1}$ and the negative band from 3200 to $3600\ \text{cm}^{-1}$, whereas only (c) can slightly reproduce the positive band from 3000 to $3200\ \text{cm}^{-1}$. The different feature emerges in the $O-H$ frequency region of large redshift, where that strong H-bonds play dominant influence on the O-H stretching vibration.

It has long been believed that the sign of $\text{Im}[\chi]$ reflects the direction of molecular dipole moment. $^{30}$ In fact, the positive $\text{Im}[\chi]$ at the $3700\ \text{cm}^{-1}$ band is assigned to the dangling $O-H$ bonds at the topmost surface layer with the H atoms protruding toward the vapor phase, and the negative $\text{Im}[\chi]$ in $3200-3600\ \text{cm}^{-1}$ band to the H-bonded water molecules directing their dipoles toward the liquid phase. However, previous MD studies of the water SFG spectra did not reproduce the positive $\text{Im}[\chi]$ in the $3000-3200\ \text{cm}^{-1}$ region. A remain-

![](./images/811813570739175424_11.jpg)

FIG. 9. Second-order nonlinear susceptibility $\chi$ for the $s s p$ polarized SFG spectrum of water surface. Blue and red symbols denote real and imaginary parts of $\chi$, respectively. (a) Experimental results (Ref. 51) (Copyright 2008, American Physical Society). (b) Calculated results by the CRK model with the local field damping of $f=f^{\text {Gauss }}(\xi=0.593 \AA)$. (c) Calculated results by the CRK model with $f=1$.

ing problem to be addressed is to clarify the mechanism for this positive $\operatorname{Im}[\chi]$, which is discussed in the following subsections in detail.

To check the molecular model dependence of the above results, we also carried out the MD calculation of $\chi$ using the PD model as described in Sec. III B, with different treatments of the short-range damping. Figures 10(a) and 10(b) show the calculated results of $\chi$ with the damping functions of $f=f^{\text {Thole }}$ and $f=1$, respectively. One immediately notices that Figs. 10(a) and 10(b) using the PD model show essentially the same features as Figs. 9(b) and 9(c), respectively, using the CRK model discussed above. Comparing the calculated spectra by PD and CRK without damping, Figs. 10(b) and 9(c), the positive region of $\operatorname{Im}[\chi]$ in $3000-3200 \mathrm{~cm}^{-1}$ is more noticeable in the PD model calculation. This difference is probably attributed to the functional form of the short-range damping.

### C. Decomposition analysis of the second order susceptibility

In this and subsequent subsections, we elucidate the mechanism of the positive $\operatorname{Im}[\chi]$ in the low frequency region. First we decompose the polarization into isotropic and anisotropic parts in the following. For this purpose, we employ the formulation based on the PD model in Sec. III B, though essentially equivalent discussion is possible with the CRK model. This is because the induced dipole of molecules can be readily decomposed with the PD model, as discussed below.

![](./images/811813570739175424_12.jpg)

FIG. 10. Second-order nonlinear susceptibility $\chi$ in the $s s p$ polarized SFG spectrum of water surface. Blue and red lines denote $\operatorname{Re}[\chi]$ and $\operatorname{Im}[\chi]$, respectively. (a) Calculated results by the PD model with the local field damping of $f=f^{\text {Thole }}$. (b) Calculated results by the PD model with $f=1$.

In Eq. (35), the dipole moment of the interface system can be calculated by
$$
M_{p}=\sum_{i} \sum_{r}^{x, y, z} \mathfrak{F}_{r, p}^{i} \mu_{r, i}^{\prime},\qquad(39)
$$
where $\mu_{r, i}^{\prime}$ is defined as $\mu_{r, i}^{0}+\sum_{q} \alpha_{r q, i}(E_{q}^{0}+E_{q, i}^{0}). \mu_{r, i}^{\prime}$ means the dipole moment of the $i$ th molecule on condition that the intermolecular dielectric coupling among induced dipoles were missing. In fact, the effects of intermolecular dielectric coupling are represented by the local field correction factor, $\mathfrak{F}$. Then the dipole moment in the $z$ direction, $M_{z}$, which is relevant to the $s s p$ polarized SFG spectrum, is divided into the isotropic part $M_{z}^{\text {iso }}$ and the anisotropic part $M_{z}^{\text {aniso }}$,
$$
M_{z}=M_{z}^{\text {iso }}+M_{z}^{\text {aniso }},\qquad(40)
$$
where
$$
M_{z}^{\text {iso }}=\sum_{i} \mathfrak{F}_{z, z}^{i} \mu_{z, i}^{\prime},\qquad(41a)
$$

$$
M_{z}^{\text {aniso }}=\sum_{i}\left(\mathfrak{F}_{x, z}^{i} \mu_{x, i}^{\prime}+\mathfrak{F}_{y, z}^{i} \mu_{y, i}^{\prime}\right).\qquad(41b)
$$

$M_{z}^{\text {iso }}$ and $M_{z}^{\text {aniso }}$ are schematically illustrated in Fig. 11(a). In the isotropic part $M_{z}^{\text {iso }}$, the $z$ component of $\mu_{z, i}^{\prime}$ generates the induced dipole in the same direction, whereas in the anisotropic part $M_{z}^{\text {aniso }}$, the $x, y$ (tangential) component of $\mu_{x, i}^{\prime}, \mu_{y, i}^{\prime}$

![](./images/811813570739175424_13.jpg)

FIG. 11. (a) Illustration of isotropic and anisotropic parts of the dipole moment. (b) Decomposition of ${\rm Im}[\chi_{qqz}^{\rm R}]$ by the PD model with $f$=1. Blue is the isotropic component ${\rm Im}[\chi_{qqz}^{\rm R,isot}]$ and red is the anisotropic component ${\rm Im}[\chi_{qqz}^{\rm R,aniso}]$.

generates the induced dipole in the $z$ (normal) direction. Note that the anisotropic part $M_{z}^{\rm aniso}$ should necessarily vanish on average if the system was isotropic. This is not the case with the water surface.

According to the decomposition of Eq. (40), the vibra- tionally resonant susceptibility $\chi^{\rm R}$ in Eq. (17) is also decomposed as
$$
\chi_{qqz}^{\rm R}=\chi_{qqz}^{\rm R,isot}+\chi_{qqz}^{\rm R,aniso}\quad(q=x,y),\tag{42}
$$
where
$$
\chi_{qqz}^{\rm R,isot}=\frac{i\omega_{IR}}{k_{B}T}\int_{0}^{\infty}dt\exp(i\omega_{IR}t)\langle A_{qq}(t)M_{z}^{\rm iso}(0)\rangle,\tag{43a}
$$

$$
\chi_{qqz}^{\rm R,aniso}=\frac{i\omega_{IR}}{k_{B}T}\int_{0}^{\infty}dt\exp(i\omega_{IR}t)\langle A_{qq}(t)M_{z}^{\rm aniso}(0)\rangle.\tag{43b}
$$

The decomposed result of ${\rm Im}[\chi_{qqz}^{\rm R}]$ is shown in Fig. 11(b). The isotropic part (blue line) is rather consistent with the common interpretation of the dipole orientation at the interface, i.e., the dangling O–H bonds pointing to the vapor side gives the positive band at about $3700\ \mathrm{cm}^{-1}$, while the H-bonded OH moieties which slightly point their average dipoles to the liquid side brings the negative band at about $3400\ \mathrm{cm}^{-1}$. This result may be intuitive, as the isotropic part of $M_{z}^{\rm iso}$ reflects directly the orientation of the molecular dipole $\mu_{z,i}'$. However, an interesting result is observed in the anisotropic part, ${\rm Im}[\chi_{qqz}^{\rm R,aniso}]$ [red line in Fig. 11(b)], exhibiting a positive band from 3000 to $3400\ \mathrm{cm}^{-1}$. This anisotropic part obviously makes the total ${\rm Im}[\chi_{qqz}^{\rm R}]$ positive in the $3000$–$3200\ \mathrm{cm}^{-1}$ region. The positive anisotropic polarization along the surface normal is not directly assigned to the orientation of individual molecules pointing to the vapor side.

![](./images/811813570739175424_14.jpg)

FIG. 12. The average molecular dipoles of isotropic and anisotropic parts, $\langle\mathfrak{F}_{z,z}^{i}\mu_{z,i}'\rangle$ and $\langle\mathfrak{F}_{x,z}^{i}\mu_{x,i}'+\mathfrak{F}_{y,z}^{i}\mu_{y,i}'\rangle$ in Eq. (41), as a function of the depth $\hat{z}$. (a) Isotropic part. (b) Anisotropic part.

To further investigate the spatial origin of these polarization components, the average molecular dipoles of isotropic and anisotropic parts, $\langle\mathfrak{F}_{z,z}^{i}\mu_{z,i}'\rangle$ and $\langle\mathfrak{F}_{x,z}^{i}\mu_{x,i}'+\mathfrak{F}_{y,z}^{i}\mu_{y,i}'\rangle$ in Eq. (41), are plotted as a function of the depth $\hat{z}$ in Fig. 12. Panel (a) shows that the isotropic part has a negative region near the Gibbs dividing surface, $-3\ \mathring{\mathrm{A}}<\hat{z}<2\ \mathring{\mathrm{A}}$, which is in accord with the molecular orientation. $^{56}$ On the other hand, the anisotropic part in panel (b) shows a positive region in the spatial region close to the surface, $-3\ \mathring{\mathrm{A}}<\hat{z}$. This result confirms that the positive component of the anisotropic part is originated mostly from the top monolayer of the surface.

## D. Anisotropic local field effect and interfacial structure

Next question to be addressed here is how the anisotropic polarization is explained from the molecular orientation at the interface. Suppose a molecule $i$ at the interface has $\mu_{x,i}'>0$. (This assumption does not lose generality since the surface is azimuthally isotropic.) Then the positive anisotropic polarization $\mathfrak{F}_{x,z}^{i}\mu_{x,i}'>0$ means that the anisotropic local field factor $\mathfrak{F}_{x,z}^{i}$ tends to be also positive. Therefore, we first clarify the physical meaning of $\mathfrak{F}_{x,z}^{i}>0$. The local field factor $\mathfrak{F}^{i}$ is, by definition of Eqs. (34) and (31), determined by the configuration and polarizability of neighboring molecules around $i$.

In the discussion on the dielectric interaction in Sec. III B, let us consider a small external (Maxwell) field $\delta E_{z}^{0}$ imposed uniformly along the $z$ axis on the interface system. Then the variation in the local field $\delta E_{x,i}$ is derived from Eq. (32) as
$$
\delta E_{x,i}=\sum_{j}\left[G^{-1}\right]_{xi,zj}[\delta E_{z}^{0}]=\mathfrak{F}_{x,z}^{i}\delta E_{z}^{0}.\tag{44}
$$

Equation (44) allows $\mathfrak{F}_{x,z}^{i}>0$ to be interpreted that the local electric field on the $i$th molecule in the $x$ direction, $\delta E_{x,i}$ $>0$, would be induced by $\delta E_{z}^{0}>0$. This situation should be realized when the surrounding molecules around $i$ have the anisotropic polarizability $\alpha_{xz,j}>0$, where $j$ denotes a neighboring molecule which influences the induced field on the molecule $i$. We confirmed the above situation by MD simulation by calculating the correlation between $\mu_{x,i}^{0}$ and $\alpha_{xz,j}$ defined as

![](./images/811813570739175424_15.jpg)

FIG. 13. Molecular orientational correlation $H(\hat{z},r)$ defined with $\mu_{x,i}^{0}$ and $\alpha_{xz,j}$ in Eq. (45). $r$ is the molecular distance and $\hat{z}$ is the depth (see Sec. V D).

$$
H(\hat{z}, r)=\frac{\left\langle\sum_{i} \sum_{j(\neq i)}\left(\mu_{x, i}^{0} \cdot \alpha_{x z, j}\right) \delta\left(\hat{z}-z_{i}\right) \delta\left(r-\left|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right|\right)\right\rangle}{\left\langle\sum_{i} \sum_{j(\neq i)} \delta\left(\hat{z}-z_{i}\right) \delta\left(r-\left|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right|\right)\right\rangle},
\tag{45}
$$

where $r=|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}|$ is the intermolecular center-of-mass distance. The quantity $H(\hat{z}, r)$ reflects the orientational correlation of surface molecules, as shown in Fig. 13. One can see that there exists a clear positive region in $H(\hat{z}, r)$ at about the adjacent distance $r\sim3.0$ $\text{\AA}$ in the vicinity of the surface, $\hat{z}>-4.0$ $\text{\AA}$. This result supports the above picture that $\mu_{x,i}^{0}$ and $\alpha_{xz,j}$ tend to have the same sign for the adjacent molecules at the water surface. (Note that a case of $\mu_{x,i}^{0}<0$ and $\alpha_{xz,j}<0$ is equivalent if the $x$ axis is reversed.)

This situation of orientational correlation is schematically explained in Fig. 14, which illustrates the most probable pair of H-bonding water at the surface as shown in Table IV, where the molecule $i$ is a donor with the orientation (b,c,d) and $j$ is an acceptor with the orientation (e) in

![](./images/811813570739175424_16.jpg)

FIG. 14. Illustration of the most probable H-bonding pair of surface molecules, assigned as donor(b,c,d)-acceptor(e) in Table IV. This is a typical example to produce the anisotropic dipole along the $z$ axis (see the text).

Sec. IV D. It is readily shown by the DFT calculation that the orientation of each molecule gives $\mu_{x,i}^{0}>0$ and $\alpha_{xz,j}>0$ in the coordinates in Fig. 14.

To summarize the above discussion, the anisotropic local field is attributed to orientational correlation at the water surface. In the case that a surface water molecule with tangential dipole forms a H-bond with adjacent molecule like Fig. 14, the normal dipole moment is induced at the H-bonding acceptor molecule through its anisotropic polarizability. This correlation becomes significant for a strong H-bonding pair of surface water. This anisotropic local field effect results in the positively enhanced imaginary susceptibility $\text{Im}[\chi_{qqz}^{\text{R,aniso}}]$ at the low frequency region.

### VI. CONCLUSIONS

In the present study, we construct a new flexible and polarizable CRK water model to calculate the SFG spectra and interfacial properties of aqueous systems. The CRK model based on the $ab$ initio or DFT calculations can readily incorporate conformational dependence of partial charges and polarization in a general manner, which is an important requisite to describe the vibrational SFG spectra. Extension to other molecules is thus quite straightforward, and the progress is underway in our group. The CRK model thus developed is confirmed to well describe bulk properties and spectroscopic properties of liquid water. The perturbation of equilibrium molecular geometry in liquid is also properly reproduced, and its mechanism is analyzed in terms of bond polarization.

An improvement in the present study is made to the description of electrostatic properties under the strong H-bonding environment. We found that the usual short-range damping treatments for Coulomb interactions are adequate to intermolecular force fields, while they are insufficient to describe the transition dipole of O-H vibration with the strong H-bond. This is attributed to the significant CT, and this effect is better represented with the point charge model in an effective way. With this improved treatment of the transition dipole, calculated nonlinear susceptibility $\chi_{qqz}$ for water surface exhibits good agreement with the recent phase-sensitive experiment, including the positive imaginary part in the $3000-3200$ $\text{cm}^{-1}$ region.

The mechanism of the positive $\text{Im}[\chi_{qqz}]$ in the low frequency region is elucidated from the MD analysis. We found

that this positive band is assigned to the anisotropic part of the induced polarization at the surface. The anisotropic po- larization originates from orientational correlation of surface water, as typically illustrated in Fig. 14. This mechanism of anisotropic local field is similar to the intermolecular corre- lation effect previously reported by us $^{83,84}$ in the sense that the SFG spectroscopy is interpreted with molecular correla- tion rather than the individual molecular properties. Such collective effects are of particular significance in the SFG analysis of strongly hydrogen bonding systems.

## ACKNOWLEDGMENTS

This work was supported by the Next-Generation Super- computer Project and the Grants-in-Aid (Grant Nos. 20750003, 20038003, 20050003, and 21245002) by the Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan.

$^{1}$ D. Eisenberg and W. Kauzmann, *The Structure and Properties of Water*(Clarendon, Oxford, 1969).
$^{2}$ Y. Marechal, *The Hydrogen Bond and the Water Molecule*(Elsevier, Amsterdam, 2007).
$^{3}$ Q. Du, R. Superfine, E. Freysz, and Y. R. Shen, *Phys. Rev. Lett.* **70**, 2313(1993).
$^{4}$ Q. Du, E. Freysz, and Y. R. Shen, *Science* **264**, 826 (1994).
$^{5}$ M. J. Shultz, C. Schnitzer, D. Simonelli, and S. Baldelli, *Int. Rev. Phys. Chem.* **19**, 123 (2000).
$^{6}$ E. A. Raymond, T. L. Tarbuck, M. G. Brown, and G. L. Richmond, *J. Phys. Chem. B* **107**, 546 (2003).
$^{7}$ D. Liu, G. Ma, L. M. Levering, and H. C. Allen, *J. Phys. Chem. B* **108**,2252 (2004).
$^{8}$ W. Gan, D. Wu, Z. Zhang, R. Feng, and H. Wang, *J. Chem. Phys.* **124**,114705 (2006).
$^{9}$ M. Sovago, R. K. Campen, G. W. H. Wurpel, M. Müller, H. J. Bakker, and M. Bonn, *Phys. Rev. Lett.* **100**, 173901 (2008).
$^{10}$ G. L. Richmond, *Chem. Rev.* (Washington, D.C.) **102**, 2693 (2002).
$^{11}$ Y. R. Shen and V. Ostroverkhov, *Chem. Rev.* (Washington, D.C.) **106**,1140 (2006).
$^{12}$ H. C. Allen, N. N. Casillas-Ituarte, M. R. Sierra-Hernández, X. Chen, and C. Y. Tang, *Phys. Chem. Chem. Phys.* **11**, 5538 (2009).
$^{13}$ I. Benjamin, *Phys. Rev. Lett.* **73**, 2083 (1994).
$^{14}$ V. Buch, *J. Phys. Chem. B* **109**, 17771 (2005).
$^{15}$ E. C. Brown, M. Mucha, P. Jungwirth, and D. J. Tobias, *J. Phys. Chem. B* **109**, 7934 (2005).
$^{16}$ A. Perry, C. Neipert, B. Space, and P. B. Moore, *Chem. Rev.* (Washington, D.C.) **106**, 1234 (2006).
$^{17}$ D. S. Walker, D. K. Hore, and G. L. Richmond, *J. Phys. Chem. B* **110**,20451 (2006).
$^{18}$ A. Morita and T. Ishiyama, *Phys. Chem. Chem. Phys.* **10**, 5801 (2008).
$^{19}$ B. M. Auer and J. L. Skinner, *J. Phys. Chem. B* **113**, 4125 (2009).
$^{20}$ J. Noah-Vanhoucke, J. D. Smith, and P. L. Geissler, *J. Phys. Chem. B* **113**, 4065 (2009).
$^{21}$ A. Perry, H. Ahlborn, P. Moore, and B. Space, *J. Chem. Phys.* **118**, 8411(2003).
$^{22}$ A. Perry, C. Neipert, C. Ridley, and B. Space, *Phys. Rev. E* **71**, 050601(2005).
$^{23}$ A. Perry, C. Neipert, C. Ridley, T. Green, P. Moore, and B. Space, *J. Chem. Phys.* **123**, 144705 (2005).
$^{24}$ D. S. Walker and G. L. Richmond, *J. Phys. Chem. C* **111**, 8321 (2007).
$^{25}$ B. M. Auer and J. L. Skinner, *J. Chem. Phys.* **129**, 214705 (2008).
$^{26}$ B. M. Auer and J. L. Skinner, *Chem. Phys. Lett.* **470**, 13 (2009).
$^{27}$ S. Iuchi, H. Chen, F. Paesani, and G. A. Voth, *J. Phys. Chem. B* **113**,4017 (2009).
$^{28}$ H.-S. Lee and M. E. Tuckerman, *J. Phys. Chem. A* **113**, 2144 (2009).
$^{29}$ C. J. Mundy and I. W. Kuo, *Chem. Rev.* (Washington, D.C.) **106**, 1282(2006).
$^{30}$ A. Morita and J. T. Hynes, *Chem. Phys.* **258**, 371 (2000).
$^{31}$ A. Morita and J. T. Hynes, *J. Phys. Chem. B* **106**, 673 (2002).
$^{32}$ A. Morita, *J. Phys. Chem. B* **110**, 3158 (2006).
$^{33}$ A. Wallqvist, *Chem. Phys.* **148**, 439 (1990).
$^{34}$ S. B. Zhu, S. Singh, and G. W. Robinson, *J. Chem. Phys.* **95**, 2791(1991).
$^{35}$ G. Corongiu, *Int. J. Quantum Chem.* **42**, 1209 (1992).
$^{36}$ H. Saint-Martin, J. Hernandez-Cobos, M. I. Bernal-Uruchurtu, I. Ortega-Blake, and H. J. C. Berendsen, *J. Chem. Phys.* **113**, 10899 (2000).
$^{37}$ C. J. Burnham and S. S. Xantheas, *J. Chem. Phys.* **116**, 5115 (2002).
$^{38}$ S. Iuchi, A. Morita, and S. Kato, *J. Phys. Chem. B* **106**, 3466 (2002).
$^{39}$ J. Jeon, A. E. Lefohn, and G. A. Voth, *J. Chem. Phys.* **118**, 7504 (2003).
$^{40}$ P. Ren and J. W. Ponder, *J. Phys. Chem. B* **107**, 5933 (2003).
$^{41}$ G. S. Fanourgakis and S. S. Xantheas, *J. Chem. Phys.* **128**, 074506(2008).
$^{42}$ A. Morita and S. Kato, *J. Am. Chem. Soc.* **119**, 4032 (1997).
$^{43}$ A. Morita and S. Kato, *J. Chem. Phys.* **108**, 6809 (1998).
$^{44}$ A. Morita and S. Kato, *J. Phys. Chem. A* **106**, 3909 (2002).
$^{45}$ T. Ishida and A. Morita, *J. Chem. Phys.* **125**, 074112 (2006).
$^{46}$ T. Ishida, *J. Phys. Chem. A* **112**, 7035 (2008).
$^{47}$ B. T. Thole, *Chem. Phys.* **59**, 341 (1981).
$^{48}$ D. N. Bernardo, Y. Ding, K. Krogh-Jespersen, and R. M. Levy, *J. Phys. Chem.* **98**, 4187 (1994).
$^{49}$ V. Ostroverkhov, G. A. Waychunas, and Y. R. Shen, *Phys. Rev. Lett.* **94**,046102 (2005).
$^{50}$ S. Yamaguchi and T. Tahara, *J. Chem. Phys.* **129**, 101102 (2008).
$^{51}$ N. Ji, V. Ostroverkhov, C. S. Tian, and Y. R. Shen, *Phys. Rev. Lett.* **100**,096102 (2008).
$^{52}$ C. S. Tian and Y. R. Shen, *Chem. Phys. Lett.* **470**, 1 (2009).
$^{53}$ C. S. Tian and Y. R. Shen, *J. Am. Chem. Soc.* **131**, 2790 (2009).
$^{54}$ S. Nihonyanagi, S. Yamaguchi, and T. Tahara, *J. Chem. Phys.* **130**,204704 (2009).
$^{55}$ Y. Fan, X. Chen, L. Yang, P. Cremer, and Y. Q. Gao, *J. Phys. Chem. B* **113**, 11672 (2009).
$^{56}$ T. Ishiyama and A. Morita, *J. Phys. Chem. C* **111**, 721 (2007).
$^{57}$ W. S. Benedict, N. Gailar, and E. K. Plyler, *J. Chem. Phys.* **24**, 1139(1956).
$^{58}$ M. Sprik and M. L. Klein, *J. Chem. Phys.* **89**, 7556 (1988).
$^{59}$ T. H. Dunning, Jr., *J. Chem. Phys.* **90**, 1007 (1989).
$^{60}$ R. A. Kendall and T. H. Dunning, Jr., *J. Chem. Phys.* **96**, 6796 (1992).
$^{61}$ GAMESS-UK, is a package of ab initio programs written by M. F. Guest, J. H. van Lenthe, J. Kendrick, K. Schoeffel, and P. Sherwood, with contributions from R. D. Amos, R. J. Buenker, M. Dupuis, N. C. Handy, I. H. Hillier, P. J. Knowles, V. Bonacic-Koutecky, W. von Niessen, R. J. Harrison, A. P. Rendell, V. R. Saunders, and A. J. Stone. The package is derived from the original GAMESS code due to M. Dupuis, D. Spangler, and J. Wendoloski, NRCC Software Catalog, Vol. 1, Program No. QG01(GAMESS), 1980.
$^{62}$ T. Ishiyama and A. Morita, *J. Phys. Chem. C* **113**, 16299 (2009).
$^{63}$ S. Mukamel, *Principles of Nonlinear Optical Spectroscopy* (Oxford University Press, Oxford, 1995).
$^{64}$ M. Cho, C. Hess, and M. Bonn, *Phys. Rev. B* **65**, 205423 (2002).
$^{65}$ C. J. F. Böttcher, *Theory of Electric Polarization* (Elsevier, New York,1973).
$^{66}$ M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids* (Clarendon, Oxford, 1987).
$^{67}$ D. Fincham, *Mol. Simul.* **13**, 1 (1994).
$^{68}$ H. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. DiNola, and J. R. Haak, *J. Chem. Phys.* **81**, 3684 (1984).
$^{69}$ P. L. Silvestrelli and M. Parrinello, *Phys. Rev. Lett.* **82**, 3308 (1999).
$^{70}$ A. K. Soper and M. G. Phillips, *Chem. Phys.* **107**, 47 (1986).
$^{71}$ J. C. Grossman, E. Schwegler, E. W. Draeger, F. Gygi, and G. Galli, *J. Chem. Phys.* **120**, 300 (2004).
$^{72}$ P. K. Mankoo and T. Keyes, *J. Chem. Phys.* **129**, 034504 (2008).
$^{73}$ P. H. Berens, S. R. White, and K. R. Wilson, *J. Chem. Phys.* **75**, 515(1981).
$^{74}$ J. S. Bader and B. J. Berne, *J. Chem. Phys.* **100**, 8359 (1994).
$^{75}$ S. A. Egorov, K. F. Everitt, and J. L. Skinner, *J. Phys. Chem. A* **103**,9494 (1999).
$^{76}$ C. J. Burnham, D. J. Anick, P. K. Mankoo, and G. F. Reiter, *J. Chem. Phys.* **128**, 154519 (2008).
$^{77}$ H. Ahlborn, X. Ji, and B. Space, *J. Chem. Phys.* **111**, 10622 (1999).
$^{78}$ B. M. Auer and J. L. Skinner, *J. Chem. Phys.* **128**, 224511 (2008).
$^{79}$ K. Ichikawa, Y. Kameda, T. Yamaguchi, H. Wakita, and M. Misawa, *Mol. Phys.* **73**, 79 (1991).
$^{80}$ N. W. Moriarty and G. Karlström, *J. Chem. Phys.* **106**, 6470 (1997).
$^{81}$ P. L. Silvestrelli and M. Parrinello, *J. Chem. Phys.* **111**, 3572 (1999).

$^{82}$R. Kumar, J. R. Schmidt, and J. L. Skinner, J. Chem. Phys. 126, 204107 (2007).

$^{83}$T. Ishiyama and A. Morita, Chem. Phys. Lett. 431, 78 (2006).

$^{84}$T. Ishiyama and A. Morita, J. Phys. Chem. C 111, 738 (2007).

$^{85}$W. Wagner and A. Pruss, J. Phys. Chem. Ref. Data 31, 387 (2002).

$^{86}$W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, and M. L. Klein, J. Chem. Phys. 79, 926 (1983).

$^{87}$Kagaku Binran, 5th ed., edited by the Chemical Society of Japan (Maruzen, Tokyo, 2004).

$^{88}$Y. S. Badyal, M. L. Saboungi, D. L. Price, S. D. Shastri, D. R. Haeffner, and A. K. Soper, J. Chem. Phys. 112, 9206 (2000).

$^{89}$J. E. Bertie and Z. Lan, Appl. Spectrosc. 50, 1047 (1996).

$^{90}$M. H. Brooker, G. Hancock, B. C. Rice, and J. Shapter, J. Raman Spec- trosc. 20, 683 (1989).