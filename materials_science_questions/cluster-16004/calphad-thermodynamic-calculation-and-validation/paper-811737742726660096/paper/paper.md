# First-principles calculations and thermodynamic modeling of the Re-Y system with extension to the Ni-Re-Y system

C. Zacherl*, J. Saal, Y. Wang, Z.K. Liu

Department of Materials Science and Engineering, The Pennsylvania State University, University Park, PA 16802, USA

---

## ARTICLE INFO

**Article history:**
Received 4 June 2010
Received in revised form
3 August 2010
Accepted 16 August 2010
Available online 15 September 2010

**Keywords:**
B. Thermodynamic and thermochemical properties
B. Phase diagrams
E. Ab-initio-calculations
E. Phase diagram, prediction (including CALPHAD)

---

## ABSTRACT

The thermodynamic properties of the Re-Y binary system were modeled by complimenting the CALculation of PHAse Diagram (CALPHAD) method with first-principles calculations. Hcp and bcc solid solution phases were predicted from first-principles calculations to have positive enthalpies of mixing, indicating the existence of a miscibility gap. Heat capacity, entropy of formation, and enthalpy of formation as a function of temperature were predicted by first-principles calculations for $Re_2Y$ using the supercell method with the quasi-harmonic approximation. Together with the experimental data in the literature, a complete thermodynamic description for this binary system was developed. To predict the properties of the Ni-Re-Y system, the Ni-Re system was remodeled to be consistent with the current thermodynamic database and combined with the Ni-Y system from the literature and the Re-Y system from the current work. An isothermal section and the liquidus projection are presented.

© 2010 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Improving the ability of Ni-base superalloys to withstand higher temperatures with increasing longevity is desirable to the aerospace industry. More advanced alloys will require complex, multi-component alloys with carefully engineered compositions. To develop such alloys, it is necessary to understand how different alloying elements, such as rhenium and yttrium, affect phase stability in multi-component Ni-base systems. The CALculation of PHAse Diagram (CALPHAD) [1, and references therein] modeling technique meets this challenge by predicting the thermodynamic descriptions of a multi-component system from extrapolation of the constituent binary and ternary systems, where data is more plentiful. With this method, the properties of complex alloys can be efficiently and accurately predicted reducing costly and time-consuming experimental investigations. The Re-Y system is a constituent binary of the Ni-base superalloy database. The Re-Y system was first investigated experimentally by Lundin and Klodt [2] using metallographic and X-ray diffraction techniques. It was found to have one intermetallic compound, $Re_2Y$, with a hexagonal laves structure (C14), prototype ($MgZn_2$), and spacegroup $P6_3/mmc$. Two invariant reactions were observed: a peritectic reaction involving Re and $Re_2Y$ at 2793 K with an unreported composition for the liquid. A eutectic at 1723 K with a composition $x_Y=95$ at. % was also reported. No solubility in either pure Re or Y was found. A galvanic cell experiment done by Rezukhina and Pokarev [3] reported the enthalpy of formation of $Re_2Y$ to be –45 kJ/mole-atom.

To overcome the lack of experimental data, first-principles calculations based on density functional theory (DFT) [4] are used to predict structural and physical properties in the present work [1]. Special quasirandom structures (SQS) are used to calculate the enthalpy of mixing for the bcc [5] and hcp [6] solid solutions. Enthalpy, heat capacity, and entropy of $Re_2Y$ are predicted as a function of temperature from phonon calculations using the supercell method [7–9] under the quasi-harmonic approximation. Both types of results from these first-principles calculations are combined with the available phase equilibrium data for evaluation of the thermodynamic model parameters of the Re-Y system using the CALPHAD technique.

## 2. Methodology

### 2.1. First-principles calculations

First-principles calculations based on DFT are carried out using the Vienna *ab-initio* Simulation Package (VASP) [10]. Calculations

---

* Corresponding author. Tel.: +1 814 863 9957.
E-mail address: clz125@psu.edu (C. Zacherl).

0966-9795/$ – see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.intermet.2010.08.032

employ the projector augmented wave (PAW) method [11,12] and the generalized gradient approximation (GGA) as implemented by Perdew, Burke, and Erzhenfest [13]. A plane wave energy cutoff of 350 eV is used for all calculations. For total energy calculations of the pure elements and $Re_2Y$, all degrees of freedom for the structures are allowed to relax. The pure Re and pure Y calculations are performed with a gamma k-point mesh $16 \times 16 \times 10$. $Re_2Y$ calculations are done with a $10 \times 10 \times 6$ k-point mesh.

SQS calculations are performed to predict enthalpies of mixing for the hcp and bcc solid solution phases. While there is no reported solubility in these phases in the Re–Y system, the enthalpies of mixing for such solutions become important when they are extrapolated to ternary and higher-order systems. This ensures that for the Ni-base superalloy database in the CALPHAD community, the interaction parameters of the Re–Y system have physical meaning. SQSs used in this work are 16-atom supercells designed previously [5,6] to have the correlation functions of the supercells mimic the correlation functions of a random solution as much as possible for the first several nearest neighbor shells. The goal of fully relaxing the structures with DFT is to obtain the 0 K ground state energy. However, local atomic relaxations are known to cause a significant distortion of the SQS, which may result in the symmetry of the parent structure being lost. In this work, the structural symmetry of the SQS supercell is kept during DFT calculations to ensure the bcc and hcp symmetries are preserved. The SQS calculations are performed with a gamma k-point mesh of $8 \times 8 \times 5$ for hcp structures and a $8 \times 8 \times 6$ mesh for bcc structures. The enthalpy of mixing for both the bcc and hcp 16-atom SQS supercells is calculated by means of the following equation:

$$
\Delta_{f} H_{\mathrm{Re}_{x} Y_{y}}=E_{\mathrm{Re}_{x} Y_{y}}-\frac{x}{x+y} E_{\mathrm{Re}}-\frac{y}{x+y} E_{Y} \tag{1}
$$

where the $E$ terms are the total energies from SQS calculations and the pure elements in bcc or hcp structures.

For the bcc SQS calculations, the cell shape and cell volume are allowed to relax in order to maintain symmetry. Unlike the bcc structures, the hcp structures have to consider an additional factor during relaxation, the $c/a$ lattice parameter ratio. Previously, Shin et al. [6] allowed both the cell shape and the cell volume to relax simultaneously in VASP for the hcp SQS structures. However, this direct relaxation approach could cause a loss of symmetry by changing the angles between the primitive lattice vectors of the hcp structure. In the present work, a method is proposed that manually minimizes the energy of the SQS by changing the $a$ lattice parameter or the $c/a$ ratio. The cell shape is fixed during a volume relaxation to ensure that the angles between the lattice vectors cannot change. With this method, the equivalent of a cell shape and cell volume relaxation that guarantees the preservation of the hcp symmetry is achieved. The energy landscape becomes a function of the hexagonal lattice vector and is calculated from a matrix of lattice parameter $a$ and the $c/a$ ratio. The minimum energy is determined by interpolation and a final static calculation is performed to confirm the interpolated minimum energy.

A radial distribution analysis is performed on both the method from this work and the method proposed by Shin et al. [6] to compare resulting symmetry of the SQS structures. A radial distribution analysis examines the packing of atoms around each specific atom in the structure as a function of nearest neighbor distance. The radial distribution analysis shows that when compared to a pure hcp structure, both the method from this work and Shin et al. produce a structure that on average has a similar frequency of nearest neighbors occurrence from any given atom.

Finite temperature properties such as heat capacity, entropy, and enthalpy as a function of temperature for hcp Re, hcp Y, and $Re_2Y$ are determined by phonon calculations based on the supercell method.

The calculations employ the *fitfc* program of the Alloy Theoretical Automated Toolkit (ATAT) software package [14] as an interface to the VASP code. The quasi-harmonic approximation (QHA) is used. The Helmholtz energy of a solid phase, $F(V,T)$, has contributions from the 0 K static, vibrational, and thermoelectronic energies [9,15],

$$
F(V, T)=E_{0 \mathrm{~K}}(V)+F_{\mathrm{vib}}(V, T)+F_{\mathrm{el}}(V, T) \tag{2}
$$

where $E_{0 \mathrm{~K}}(V)$ is the volume-dependent 0 K static energy, $F_{\mathrm{vib}}(V,T)$ the vibrational contribution, and $F_{\mathrm{el}}(V,T)$ the thermoelectronic contribution.

Phonon calculations are performed with a gamma k-point mesh of $6 \times 6 \times 6$ and $5 \times 5 \times 6$ for the pure elements and $Re_2Y$, respectively. The steps for first-principles phonon calculations in ATAT using the QHA approximation are as follows: (1) fully relax the primitive cell using first-principles code, VASP, (2) increase the volume of the primitive cell several times by straining the lattice parameters by 2% and allow to fully relax using VASP, (3) select the size of the supercells for each increased volume according to the nearest neighbor interaction distance and recalculate the forces acting on the atoms using VASP, and (4) use ATAT and the calculated forces to evaluate the force constants, the phonon frequencies, and the electronic contribution to the free energy for each of the volumes calculated. Supercell sizes were with 114, 48, and 48 atoms for Re, Y, and $Re_2Y$, respectively.

### 2.2. CALPHAD modeling

The CALPHAD technique parameterizes the Gibbs energy of all the individual phases in a system with temperature and composition dependent expressions. Thermochemical data of individual phases and phase equilibria data between phases are used to fit the model parameters. The Gibbs energy of $Re_2Y$ used in the present work is of the form:

$$
G^{\mathrm{Re}_{2} Y}-H^{S E R}=a+b T+c T \ln (T)+d T^{2}+e T^{-1} \tag{3}
$$

where $a$, $b$, $c$, $d$, and $e$ are model parameters determined from enthalpy of formation, heat capacity, and entropy of the system. $H^{SER}$ is the stable element reference (SER) state that refers to the enthalpies of hcp Re and hcp Y at 298.15 K. Differentiating the Gibbs energy function from Eq. (3). twice with respect to temperature yields the heat capacity:

$$
C_{\mathrm{p}}^{\mathrm{Re}_{2} Y}=-T \frac{\mathrm{d}^{2} G}{\mathrm{~d} T^{2}}=-c-2 \mathrm{~d} T-2 e T^{-2} \tag{4}
$$

The heat capacity predicted from the phonon calculations is used to determine the model parameters in Eq. (4). The first derivative of Eq. (3) with respect to temperature yields entropy as a function of temperature

$$
S^{\mathrm{Re}_{2} Y}=-\frac{\mathrm{d} G}{\mathrm{~d} T}=-b-c(1+\ln (T))-2 \mathrm{~d} T+e T^{-2} \tag{5}
$$

$S_{298}$ from the phonon calculations is used to determine the model parameter $b$ in Eq. (5). Finally, the enthalpy is derived by adding $TS^{\mathrm{Re}_{2} Y}$, from Eq. (5), to the Gibbs energy,

$$
H_{\mathrm{Re}_{2} Y}=G^{\mathrm{Re}_{2} Y}+T S^{\mathrm{Re}_{2} Y}=a-c T-\mathrm{d} T^{2}+2 e T^{-1} \tag{6}
$$

$a$ is evaluated from the SER values of hcp Re and hcp Y.

The Gibbs energy, $G_{m}^{\varphi}$, of the liquid, bcc, and hcp solution phases are given as

$$
G_{m}^{\varphi}=x_{\mathrm{Re}} \cdot G_{\mathrm{Re}}^{\varphi}+x_{\mathrm{Y}} \cdot G_{\mathrm{Y}}^{\varphi}+R T\left(x_{\mathrm{Re}} \ln x_{\mathrm{Re}}+x_{\mathrm{Y}} \ln x_{\mathrm{Y}}\right)+{ }^{x S} G^{\varphi} \tag{7}
$$

where $x_{\mathrm{Re}}$ and $x_{\mathrm{Y}}$ are the mole fractions of Re and Y, respectively, $G_{\mathrm{Re}}^{\varphi}$ and $G_{\mathrm{Y}}^{\varphi}$ are the Gibbs energies of pure Re and Y in the

<table><thead><tr><th></th><th></th><th>a, Å</th><th>% Error</th><th>c, Å</th><th>% Error</th></tr></thead><tbody><tr><td rowspan="3">Re</td><td>Exp. [22]</td><td>2.76</td><td>–</td><td>4.46</td><td>–</td></tr><tr><td>Calc. [23]</td><td>2.785</td><td>0.906</td><td>4.498</td><td>0.852</td></tr><tr><td>This work</td><td>2.769</td><td>0.326</td><td>4.472</td><td>0.278</td></tr><tr><td rowspan="3">Y</td><td>Exp. [22]</td><td>3.65</td><td>–</td><td>5.73</td><td>–</td></tr><tr><td>Calc. [23]</td><td>3.654</td><td>0.110</td><td>5.649</td><td>1.414</td></tr><tr><td>This work</td><td>3.656</td><td>0.16</td><td>5.679</td><td>0.886</td></tr><tr><td rowspan="2">Re₂Y</td><td>Exp. [21]</td><td>5.397</td><td>–</td><td>8.824</td><td>–</td></tr><tr><td>This work</td><td>5.406</td><td>0.176</td><td>8.845</td><td>0.242</td></tr></tbody></table>

structure $\varphi$, respectively, and $^{xs}G^{\varphi}$ is the excess Gibbs energy. The first two terms represent the mechanical mixing of the alloying elements, and the third term represents the ideal mixing between the two elements. The excess Gibbs energy is modeled with the Redlich–Kister polynomial [16]

$$
{ }^{x s} G^{\varphi}=x_{\mathrm{Re}} x_{\mathrm{Y}} \sum_{k=0}{ }^{k} L_{\mathrm{Re}, \mathrm{Y}}^{\varphi}\left(x_{\mathrm{Re}}-x_{\mathrm{Y}}\right)^{k}
\tag{8}
$$

where $L_{\mathrm{Re}, \mathrm{Y}}^{\varphi}$ represents the non-ideal interactions between Re and Y and is usually defined as

$$
{ }^{k} L_{\mathrm{Re}, \mathrm{Y}}^{\varphi}={ }^{k} A+{ }^{k} B T
\tag{9}
$$

where $^{k}A$ and $^{k}B$ are model parameters to be evaluated. In the present work, the model parameters are evaluated using the PARROT module of ThermoCalc software [17]. The Gibbs energy description for pure Y was taken from the Scientific Group Thermodata Europe pure element (SGTE Unary) database [18]. The most recent Gibbs energy description for pure Re differs from the original SGTE Unary database and can be found in the most recent SGTE substance (SSUB) [19] database and on the SGTE Unary database webpage [20].

## 3. Results and discussion

The validity of the first-principles calculations is examined by comparing the lattice parameters of the fully relaxed structures to experimental and other first-principles results. In Table 1 the lattice parameters of Re, Y, and Re₂Y are compared to experimental [21,22] and calculated [23] data. Differences are on the order of 1%, which are typical for such DFT calculations. Excellent agreement is found with Wang et al. [23], where lattice parameters were calculated using the original GGA [24] pseudopotential, while the GGA-PBE method was used in the present work. Volume per atom of each structure as a function of mole fraction Y is shown in Fig. 1 for the solid solution phases, hcp and bcc, for the compositions $x_{\mathrm{Y}}=0.25$, 0.50, and 0.75. There is a good relationship between the mole fraction of Y and increasing volume per atom for the respective structures.

![](./images/811737742726660096_1.jpg)

Fig. 1. Volume per atom vs. mole fraction Y for hcp (●) and bcc (◆) solid solution structures.

![](./images/811737742726660096_2.jpg)

Fig. 2. Properties for Re from first-principles (a) Phonon dispersion curve with phonon density of states calculated frequencies (solid lines) compared to experimental data of Smith et al. [26] (transverse: ●, longitudinal: ○) and Shitikov et al. [25] (●), (b) calculated heat capacity (solid line) compared to experimental data by Taylor et al. [31] (●), Jaeger et al. [30] (■), Rudkin et al. [32] (▼), Arutyuno et al. [28] (▲), and Filippov et al. [29] (◆), (c) calculated enthalpy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line), and (d) calculated entropy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line).

The phonon dispersion curves and phone density of states (DOS) along with the heat capacity, enthalpy, and entropy as a function of temperature for hcp Re are compared to experiments and the SGTE SSUB [19] database and SGTE Unary database webpage [20] in Fig. 2. The phonon density of states was measured in Re through inelastic incoherent neutron scattering with polycrystalline plates

![](./images/811737742726660096_3.jpg)

Fig. 3. Properties for Y from first-principles (a) Phonon dispersion curve with phonon density of states calculated frequencies (solid lines) compared to experimental data of Shina et al. [33] (●), (b) calculated heat capacity (solid line) compared to experimental data by Jennings et al. [37] (▼), Berg, et al. [36] (▲), and Novikov et al. [35] (◆), (c) calculated enthalpy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line), and (d) calculated entropy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line).

![](./images/811737742726660096_4.jpg)

Fig. 4. Properties for Re₂Y from first-principles (a) Phonon dispersion curve with phonon density of states calculated frequencies (solid lines), (b) calculated heat capacity (solid line) compared to the SGTE SSUB database [19] (dashed line) and a Neumann-Kopp approximation from the pure element phonon calculations (dotted line), (c) calculated Gibbs energy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line) and experimental work done by Rezukhina et al. [3] (○), and (d) calculated entropy as a function of temperature (solid line) compared to the SGTE SSUB database [19] (dashed line) and a Neumann-Kopp approximation from the pure element phonon calculations (dotted line).

by Shitikov et al. [25] at 300 and 500 K with negligible temperature dependence. Compared with current calculations in Fig. 2(a), good agreement of the DOS shape is observed, particularly at lower frequencies. The phonon dispersion along the Γ-A direction is compared with experiments from Smith and Wakabayashi [26], and good agreement is found, including the representation of what Smith and Wakabayashi describe to be a Khon anomaly at the Fermi surface. Smith and Wakabayashi postulated that the anomaly is from strong electron–phonon interactions. Zolyomi et al. [27] show through *ab-initio* calculations that this anomaly exists due to a small hole pocket on the Fermi surface at the edge of the Brillouin zone. We see excellent agreement with available experimental data for heat capacity [28–32] and the SGTE data in ThermoCalc for all properties in Fig. 2(b–d).

The phonon dispersion curves and phonon DOS of Y as well as the heat capacity, enthalpy of formation, and entropy as a function of temperature are compared with experiments and the SGTE Unary database [18] in Fig. 3. The phonon dispersion curve in Fig. 3 (a) is compared to measurements obtained via inelastic neutron scattering by Sinha et al. [33]. The calculated Y phonon dispersion curves also show good agreement with experiments, especially along the Γ-A direction. The calculations slightly underestimate the frequencies along the Γ-K-M and M-Γ directions; a result similar to another first-principles calculation of Y lattice dynamics done by Souvatzis et al. [34]. Heat capacity shows good agreement with experiments [35–37] as well as with the SGTE Unary database [18] in Fig. 3(b–d).

From the agreement of the phonon dispersion and phonon DOS for Re and Y, it is concluded that the finite temperature properties of Re₂Y can be accurately predicted by phonon calculations employing the supercell method. The phonon dispersion curve and density of states plot, heat capacity, Gibbs energy, and entropy as a function of temperature for Re₂Y are shown in Fig. 4. In Figure (b) we see the heat capacity calculated from this work compared to the Neumann-Kopp approximation from the pure element phonon calculations and from the SGTE SSUB database [19]. Excellent agreement is found. Fig. 4(c) shows the Gibbs energy as a function of temperature for this work based on phonon calculations, the SSUB database and experimental points calculated from galvanic cell experiments with solid calcium fluoride done by Rezukhina and Pokarev [3] between 1010 K and 1180 K. It is clearly seen in Fig. 4(c) that the SSUB function was created based on the experimental data from [3], and that a discrepancy exists between the experimental and first-principles Gibbs energy. Several sources of error for measuring energies of solid state fluoride galvanic cells were given by Azad and Sreedharan [38]; factors which could have caused incorrect measurements of the energy of the cell involving the formation of Re₂Y. The work by Rezukhina and Pokarev [3] suggests a room temperature enthalpy of formation around –45 kJ/mol-atom which is higher than all of the values of C14 Laves compounds reported in both experimental and computational studies done on Hf–M₂ alloys by Levy et al. [39] and on M–Cr₂ alloys by Chen et al. [40].

SQS calculations are performed for hcp and bcc solid solution phases allowing volume and shape relaxation using the symmetry

![](./images/811737742726660096_5.jpg)

Fig. 5. Radial distribution analysis for 25 atomic % Re hcp solid solution structure.

![](./images/811737742726660096_6.jpg)

Fig. 6. Enthalpy of mixing for hcp (□) and bcc (◇) SQS from first-principles (points) and CALPHAD modeling in the current work (lines).

<table><thead><tr><th>Phase (model)</th><th>Parameters</th><th>Modeling from first-principles</th><th>Modeling from SSUB</th></tr></thead><tbody><tr><td>Liquid (Re,Y)</td><td>$^0L_{\text{Re,Y}}^\text{liq}$</td><td>$125,800 - 50.105T$</td><td>$508,660 - 238.87T$</td></tr><tr><td></td><td>$^1L_{\text{Re,Y}}^\text{liq}$</td><td>$32923$</td><td>$135,890$</td></tr><tr><td>hcp (Re,Y)</td><td>$^0L_{\text{Re,Y}}^\text{hcp}$</td><td>$320,000$</td><td>$300,000$</td></tr><tr><td>bcc (Re,Y)</td><td>$^0L_{\text{Re,Y}}^\text{bcc}$</td><td>$170,000$</td><td>$200,000$</td></tr><tr><td>Re₂Y</td><td></td><td>$-81382 + 365.48T - 70.982T\text{ln}(T) \\ -.00763T^2 - 3598.4T^{-1}$</td><td>$-157944 + 372.12^*T - 71.128T\text{ln}(T) \\ -.00929T^2 - 20920.4T^{-1}$</td></tr></tbody></table>

preservation method described above, volume and shape relaxation following the work of Shin et al. [6], and full relaxation to occur. The symmetry is analyzed by a radial distribution analysis for each structure that is compared to a pristine hcp or bcc structure. It is not expected that the SQS symmetry will have the intensity of the ideal structure, but Fig. 5 shows excellent agreement and only minor local relaxations for both volume and shape relaxed cases in the hcp structure. For this work, the process described in the methodology section is used to relax the shape and volume of the hcp structures because it achieves a slightly lower energy per atom for the structure. For the bcc structures, volume and shape are relaxed in VASP because it achieves the lowest energy per atom while still retaining local symmetry. The full relaxation results in the complete loss of symmetry for botb hcp and bcc SQS and is thus not used in the present work. The calculated enthalpies of mixing from first-principles and the CALPHAD modeling as a function of Y content are shown in Fig. 6 for both hcp and bcc solid solutions phases. The first-principles results predict a parabolic behavior for the enthalpy of mixing of both phases, indicating that a $^0L$ description is sufficient to describe their behavior. Since the enthalpies of mixing for both the bcc and hcp SQSs are positive, miscibility gaps are possible in the solution phases. The two solutions are modeled in Thermo-Calc as regular solutions, employing only $^0L$ interaction parameters determined from the enthalpy of mixing predictions.

With Gibbs energy descriptions for Re₂Y, the pure elements, and the hcp and bcc solution phases, only the Gibbs energy parameters of the liquid phase remain to be determined. The liquid phase is modeled as a sub-regular solution phase, employing $^0L$ and $^1L$ terms in the Redlich-Kister polynomial of Eq. (8). The sub-regular solution model is necessary to reproduce the eutectic and peritectic reactions. With a regular solution, Re₂Y melts congruently. The eutectic and peritectic data from Lundin and Klodt [2] are used for the evaluation of the liquid model parameters. The complete list of parameters for all of the phases in the Re-Y system can be found in Table 2. Also in Table 2 is a list of parameters for the Re-Y system if the modeling is completed using the function for Re₂Y found in the SGTE SSUB database based on the experimental data of Rezukbina and Pokarev [3] and the functions for the pure elements mentioned above. As the SSUB database predicts a significantly more stable description for Re₂Y, parameters larger by an order of magnitude are needed to compensate for this difference and to reproduce the phase equilibrium experiments. In addition to being an order of magnitude larger than the original modeling, the values are also physically unrealistic. In an article by Witusiewicz and Sommer [41] on the excess entropy of mixing in binary liquid alloys, we see that for more than 70 systems examined, the majority of the entropy of mixing terms for the liquid phases fell between −40 J/mol K and 20 J/mol K, with no system's term outside of a −60 J/mol K and 60 J/ mol K range. Therefore, at 238.9 J/mol K, the magnitude of the entropy of mixing term in the liquid phase for the SSUB modeling is physically unrealistic. The description of the Re-Y system based on the results of the first-principles calculations for the thermochemical properties of Re₂Y yields a more physical modeling.

The phase diagram based on the assessment from this work of the Re-Y system is plotted in Fig. 7 and compared to the experimental data described above. The experimental eutectic at a liquid composition of 94.97 at. % Y and 1723 K is well reproduced by the model parameters. The peritectic reaction is also well reproduced, with the liquid composition predicted to be around 37 at. % Y.

![](./images/811737742726660096_7.jpg)

Fig. 7. Calculated phase diagram of the Re-Y system with experimental data from Lundin [2] ($\Delta$).

![](./images/811737742726660096_8.jpg)

Fig. 8. Re-calculated phase diagram of the Ni-Re system with experimental data from Savitskii et al. [45] ($\bullet$) melting, ($\Delta$) one phase, ($\mathbf{\Delta}$) two phase.

<table><caption>Table 3<br>Parameters of the Ni–Re system, in J/mole-formula.</caption>
<thead>
<tr>
<th>Phase (model)</th>
<th>Parameters</th>
<th>This work</th>
</tr>
</thead>
<tbody>
<tr>
<td>Liquid (Ni,Re)</td>
<td>$^{0}L_{\text{Ni,Re}}^{\text{liq}}$</td>
<td>16,000</td>
</tr>
<tr>
<td>hcp (Ni,Re)</td>
<td>$^{0}L_{\text{Ni,Re}}^{\text{hcp}}$</td>
<td>$12,396 + 7.99^{*}T$</td>
</tr>
<tr>
<td>fcc (Ni,Re)</td>
<td>$^{0}L_{\text{Ni,Re}}^{\text{bcc}}$</td>
<td>$27,246 - 2.44^{*}T$</td>
</tr>
<tr>
<td/>
<td>$^{1}L_{\text{Ni,Re}}^{\text{bcc}}$</td>
<td>−16,906</td>
</tr>
<tr>
<td>bcc (Ni,Re)</td>
<td>$^{0}L_{\text{Ni,Re}}^{\text{bcc}}$</td>
<td>27,558</td>
</tr>
</tbody>
</table>

### 3.1. Extension to the Ni–Re–Y system

As a further contribution to the Ni-superalloy database being created, phase equilibria in the Ni–Re–Y system is predicted. The modeling uses the Ni–Y database from Du and Lu [42] and the Ni–Re system from Huang and Chang [43]. However, in the Ni–Re system, the description of the pure elements is from the second version of the SGTE SSUB pure element database [18], while the phase descriptions of the pure elements of the Ni–Y and Re–Y systems are from the most recent version, version four. This creates an incompatibility in the ternary description of hcp Re as the function had changed between version two and three. The Ni–Re system was remodeled using the phase description for pure Re from version four of the SGTE SSUB pure element database. As described by Huang and Chang [43], interaction parameters for magnetic properties were not included because this binary system has not been investigated at temperatures below 1000 K. The liquid interaction parameter was kept as similar as possible to the previous modeling and was based on an estimate of the enthalpy of mixing at 50% Re done by de Boer et al. [44]. The re-calculated phase diagram is presented in Fig. 8 along with its corresponding modeling parameters in Table 3. The present modeling agrees well with both the experimental data from Savitskii et al. [45] and the previous modeling done by Huang and Chang [43].

In the Ni–Re–Y system there are no known ternary compounds so it was assumed that no ternary phases formed. Ternary interaction parameters in the hcp, fcc, and liquid solid solutions were not introduced. The Gibbs energy parameters for the Ni–Y systems can be found in the paper by Du and Lu [42]. After constructing the ternary description from the three binary systems, a stable bcc phase formed in the Ni–Re binary system. Instead of choosing an arbitrary positive interaction parameter for the Ni–Re bcc phase, an SQS calculation was done to predict the enthalpy of mixing at 50 at. %Re. This ensured the value would have a physical value. It is also a testament to the usefulness of SQS calculations which can predict values such as enthalpies of mixing for systems that are not attainable experimentally. Completion of the calculation led to a bcc interaction parameter of 27,558 J/mol-formula, which is reflected in Table 3. An isothermal section of the Ni–Re–Y system at 1000 K is shown in Fig. 9. The Ni-rich portion of the diagram agrees well with experimental data from Savitskii et al. [46], showing the boundary between the two phase fcc + Ni₁₇Y₂ and the three phase fcc + hcp + Ni₁₇Y₂ at 1273 K. There is no known experimental data regarding ternary solubilities in the binary intermetallics. Therefore, ternary solubilities were not modeled in this work. The liquidus projection for this system is shown in Fig. 10 with the phases forming from the liquid during primary solidification.

![](./images/811737742726660096_9.jpg)

Fig. 9. Isothermal section of the Ni–Re–Y system at 1000 K.

![](./images/811737742726660096_10.jpg)

Fig. 10. Liquidus projection of the Ni–Re–Y system.

There are two significant areas in which experiments could enhance the present work. In the case of the modeling of Re–Y, no experimental data exists on the shape of the liquidus curves. Therefore, the liquid was modeled with the fewest parameters possible. With experimental data regarding the liquidus curve, the inflection of the liquidus curves and the exact location of the eutectic could be reproduced more accurately. Another area that would benefit from experimental data is the presence of ternary solubility of the binary intermetallics. Currently, no experimental data exists on the Ni–Re–Y system beyond the work of Savitskii et al. [46] showing the boundary between the two phase fcc + Ni₁₇Y₂ and the three phase fcc + hcp + Ni₁₇Y₂ in the ternary system. Experiments on the solubility of pure Re and Re₂Y in the Ni–Y intermetallics could help to improve this modeling.

## 4. Conclusions

The coupling of first-principles calculations and thermodynamic modeling is a valuable approach when designing new Ni-base superalloys, particularly with elements such as rhenium that exist in limited quantities. First-principles calculations based on density functional theory have supplemented the limited experimental thermochemical data of the Re–Y system. The enthalpy of formation for the compound Re₂Y is calculated from first-principles,

showing that the experimental value may have a substantial error. The enthalpies of mixing for the hcp and bcc solution phases are calculated through the use of special quasirandom structures and are found to be positive for both phases. Phonon calculations provided heat capacity, entropy, and enthalpy of formation at finite temperatures. A complete self-consistent thermodynamic evalua- tion of the Re-Y system has been obtained with first-principles calculations of solid phases and experimental phase equilibrium data. Phase equilibria in the Ni-Re-Y system was predicted based on the databases of the constituent binary systems and included a re-modeling of the Ni-Re system.

## Acknowledgements
This work is funded by the Office of Naval Research (ONR) under contract number N0014-07-1-0638. We thank the program manager David Shifler for his support and encouragement. First- principles calculations were carried out in part on the LION clusters at the Pennsylvania State University supported by the Materials Simulation Center and the Research Computing and Cyberinfras- tructure unit at The Pennsylvania State University, and in part by the high performance computing resources at ARSC, ERDC, DSRC, and AFRL as part of the Department of Defense High Performance Computing Modernization Program. We would like to thank Dr. W. Huang and Dr. Z. Du for providing the Ni-Re and Ni-Y binary databases used in this modeling, respectively. The authors would also like to thank DongEung Kim and Arkapol Saengdeejing for stimulating discussion and Dr. Shunli Shang for the use of his scripts.

## Appendix. Supplementary data
Supplementary data that consists of the Thermo-Calc database file of the Ni-Re-Y system can be found in the online version, at doi:10.1016/j.intermet.2010.08.032.

## References
[1] Liu ZK. Journal of Phase Equilibria and Diffusion 2009;30:517.
[2] Lundin CE. Rare earths. New York: John Wiley Sons; 1961.
[3] Rezukhin TN, Pokarev BS. Journal of Chemical Thermodynamics 1971;3:369.
[4] Kohn W, Sham LJ. Physical Review 1965;140:A1133.
[5] Jiang C, Wolverton C, Sofo J, Chen L-Q, Liu Z-K. Physical Review B 2004;69:214202.
[6] Shin D, Arroyave R, Liu ZK, Van de Walle A. Physical Review B 2006;74:13.
[7] Wei SQ, Chou MY. Physical Review Letters 1992;69:2799.
[8] van de Walle A, Ceder G. Reviews of Modern Physicas 2002;74:11.
[9] Arroyave R, Shin D, Liu ZK. Acta Materialia 2005;53:1809.
[10] Kresse G, Furthmuller J. Physical Review B 1996;54:11169.
[11] Blöchl PE. Physical Review B 1994;50:17953.
[12] Kresse G, Joubert D. Physical Review B 1999;59:1758.
[13] Perdew JP, Burke K, Ernzerhof M. Physical Review Letters 1996;77:3865.
[14] van de Walle A, Asta M, Ceder G. Calphad 2002;26:539.
[15] Wang Y, Liu ZK, Chen LQ. Acta Materialia 2004;52:2665.
[16] Redlich O, Kister AT. Industrial & Engineering Chemistry 2002;40:345.
[17] Andersson JO, Helander T, Hoglund LH, Shi PF, Sundman B. Calphad - Computer Coupling of Phase Diagrams and Thermochemistry 2002;26:273.
[18] Dinsdale AT. Calphad - Computer Coupling of Phase Diagrams and Thermo- chemistry 1991;15:317.
[19] Scientific Group Thermodata Europe (SGTE). Thermodynamic properties of inorganic materials, vol. 19. Berlin Heidelberg: Springer, Verlag; 1999.
[20] SGTE Pure Element Database (UNARY) v. 4. Scientific Group Thermodata Europe. online, http://www.sgte.org/; 2009.
[21] Compton VB, Matthias BT. Acta Crystallographica 1959;12:651.
[22] Kittel C. John Wiley & Sons: New York, NY, 2005, p. 20.
[23] Wang Y, Curtarolo S, Jiang C, Arroyave R, Wang T, Ceder G, et al. Calphad 2004;28:79.
[24] Perdew JP, Wang Y. Physical Review B 1992;45:13244.
[25] Shitikov YL, Tulina NA, Zemlyanov MG. Physica Status Solidi B-Basic Research 1986;133:469.
[26] Smith H, Wakabayashi N. Solid State Communications 1981;39:371.
[27] Zolyomi V, Kollar J, Vitos L. Physical Review. B, Condensed Matter and Materials Physics 2008;78:195414.
[28] Arutyuno AV, Filippov LP. High Temperature 1970;8:1025.
[29] Filippov LP, Él'darov FG. Journal of Engineering Physics and Thermophysics 1977;32:180.
[30] Jaeger F, Rosenbohm E. Proceedings of the Academy of Science Amsterdam 1933;36.
[31] Taylor RE, Finch RA. Journal of the Less-Common Metals 1964;6:283.
[32] Rudkin RL, Parker WJ, Jenkins RJ. Temp. Meas. Control Sci. Ind 1962;3:523.
[33] Sinha SK, Brun TO, Muhlestein LD, Sakurai J. Physical Review B 1970;1:2430.
[34] Souvatzis P, Eriksson O. Physical Review B (Condensed Matter and Materials Physics) 2008;77:024110.
[35] Novikov II, Mardykin IP. Atomic Energy 1974;37:1088.
[36] Berg JR, F.H. Spedding, A.H. Daane. US Department of Energy, 1963, p. 35.
[37] Jennings LD, Miller RE, Spedding FH. The Journal of Chemical Physics 1960;33:1849.
[38] Azad AM, Sreedharan M. Journal of Applied Electrochemistry 1989;19:475.
[39] Levy O, Hart GLW, Curtarolo S. Acta Materialia 2010;58:2887.
[40] Chen XQ, Wolf W, Podloucky R, Rogl R. Physical Review B 2005;71:11.
[41] Witusiewicz VT, Sommer F. Journal of Alloys and Compounds 2000;312:228.
[42] Du ZM, Lu DX. Intermetallics 2005;13:586.
[43] Huang W, Chang YA. Materials Science and Engineering a-Structural Materials Properties Microstructure and Processing 1999;259:110.
[44] de Boer FR. Cohesion in metals: transition metal alloys; 1988. North-Holland, Amsterdam.
[45] Savitskii EM, Tylkina MA, Arskaya EP. Izv. Vyssh. Ucheb. Zaved., Tsvet. Met 1970;13:113.
[46] Savitskii EM, Tylkina MA, Arskaya EP. Splavy tsvetnykh metallov. Moscow: Nauka; 1972.