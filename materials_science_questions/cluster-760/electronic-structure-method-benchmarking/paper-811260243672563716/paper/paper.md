![](./images/811260243672563716_1.jpg)

![](./images/811260243672563716_2.jpg)

Subscriber access provided by University of Sussex Library

Article

# Ion Association in Aprotic Solvents for Lithium Ion Batteries Requires Discrete-Continuum Approach: Lithium Bis(Oxalato)Borate in Ethylene Carbonate Based Mixtures

Oleksandr M. Korsun, Oleg N. Kalugin, Igor O. Fritsky, and Oleg V. Prezhdo

*J. Phys. Chem. C*, **Just Accepted Manuscript** • DOI: 10.1021/acs.jpcc.6b05963 • Publication Date (Web): 28 Jun 2016

Downloaded from http://pubs.acs.org on June 30, 2016

Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a free service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are accessible to all readers and citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

![](./images/811260243672563716_3.jpg)

The Journal of Physical Chemistry C is published by the American Chemical Society.
1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works
produced by employees of any Commonwealth realm Crown government in the course
of their duties.

# Ion Association in Aprotic Solvents for Lithium Ion Batteries Requires Discrete-Continuum Approach: Lithium Bis(Oxalato)Borate in Ethylene Carbonate Based Mixtures

Aleksandr M. Korsun, $^\dagger$ Oleg N. Kalugin, $^{*, \dagger}$ Igor O. Fritsky, $^\ddagger$ and Oleg V. Prezhdo $^{*, \S}$

$^\dagger$Department of Inorganic Chemistry, V. N. Karazin Kharkiv National University, Kharkiv 61022, Ukraine

$^\ddagger$Department of Physical Chemistry, Taras Shevchenko National University of Kyiv, Kyiv 01601, Ukraine

$^\S$Department of Chemistry, University of Southern California, Los Angeles, California 90089, United States

*Corresponding authors

E-mail: onkalugin@gmail.com
Tel.: +380 50 3032813

prezhdo@usc.edu
+1 213 8213116

ACS Paragon Plus Environment

**ABSTRACT**

Ion association in solutions of lithium salts in mixtures of alkyl carbonates carries significant impact on the performance of lithium-ion batteries. Focusing on lithium bis(oxalato)borate, LiBOB, in binary solvents based on ethylene carbonate, EC, we show that neither continuum nor discrete solvation approaches are capable of predicting physically meaningful results. So-called mixed or the discrete-continuum solvation approach, based on explicit consideration of an ion solvatocomplex combined with estimation of the medium polarization effect, is required in order to characterize the ion association at the quantitative level. The calculated changes of the Gibbs free energy are overestimated by nearly an order of magnitude by the purely continuum and purely discrete approaches, with the values having the opposite signs. The physically balanced discrete-continuum description predicts weak ion association. The numerical data obtained with density functional theory are validated using coupled cluster calculations and experimental X-ray data. The study contributes to resolution of the challenge in solvation modeling in general, and develops a reliable, practical method that can be used to screen ion association in a broad range of ion-molecular mixtures for lithium ion batteries, especially for the solutions of LiBOB in EC based mixtures.

![](./images/811260243672563716_4.jpg)

### 1. INTRODUCTION

Lithium-ion batteries (LIBs) constitute a key component of most modern portable electronic devices and vehicles. Electrolyte solutions used in the batteries consist of a particular lithium salt dissolved in a mixture of aprotic organic solvents, such as cyclic and linear carbonates or esters.¹ One of the most important physicochemical properties of the salts is high solubility with minimal ion association in a given solvent mixture. These operating conditions are necessary for ensuring maximal electrical conductivity and, as a consequence, high specific power of LIBs.²

From the thermodynamic point of view, minimal ion association corresponds to maximal change in the standard Gibbs free energy of ion association, $\Delta_{\text{ass}} G_{T}^{\circ} = -RT \ln K_{\text{ass}}$. An experimental determination of the ion association constant, $K_{\text{ass}}$, is quite a labor- and time-consuming procedure. Therefore, a reliable prediction of the sign and magnitude of $\Delta_{\text{ass}} G_{T}^{\circ}$ by molecular modelling constitutes an important task. A theoretical method capable of this task will have a significant impact on selection and development of novel lithium salts and polar aprotic co-solvents for design of advanced LIBs.

Several quantum-chemical approaches have been considered, most of which focus on aqueous media.³⁻⁴ Application of the discrete-continuum approach to non-aqueous solutions of lithium salts are quite rare. Recently the mixed approach has been used to investigate the solvation free energies of the $\text{Li}^{+}$ ion in acetonitrile,⁵ to characterize ion clustering for the $\text{Li[PF}_{6}]$ electrolyte in acetonitrile,⁶ and to demonstrate that the structure of the $\text{Li}^{+}$ first solvation shell can be predicted well in an organic carbonate mixture.⁷

In this paper, we show that neither continuum, nor discrete solvation models can provide a satisfactory description of ion solvation and association in a typical LIB system. A mixed discrete-continuum description is required in order to obtain a physically reasonable representation. We demonstrate with a popular lithium salt, dissolved in the EC based mixture of polar aprotic solvents, that the pure models err by nearly an order of magnitude, and that the mentioned errors have opposite signs. The errors are corrected in the mixed approach, which considers explicitly the first solvation shell of the

ion and treats the rest of the solvent as a polarizable medium. The method predicts a small degree of ion association. The described approach can be used to screen a large number of systems suitable for LIB applications, assisting in design of novel and more efficient electrolyte solutions. The computationally efficient level is validated using both higher level computations and experimental data.

Lithium bis(oxalato)borate ($\text{Li[B(C}_2\text{O}_4\text{)}_2\text{]}$, LiBOB) has been extensively studied as a highly promising electrolyte for use in LIBs. For example, LiBOB solutions in alkyl carbonates have been found much more thermally stable than the widely used $\text{Li[PF}_6\text{]}$ solutions. Also, the performance of lithiated graphite electrodes appears to be much better with LiBOB solutions than with any other known lithium salt solutions.$^{8}$

It is known that there exists no suitable single solvent, exhibiting both high dielectric constant and low viscosity. These solvent properties are needed to ensure good lithium salt solubility and high ion mobility, correspondingly. Currently, ethylene carbonate (EC) is a commonly used component in many LIB electrolyte solutions.$^{1}$ The dimethyl carbonate (DMC), diethyl carbonate (DEC) or ethylmethyl carbonate (EMC) are usually added to EC as non-viscous co-solvents.

The current study elucidates the utility of continuum, discrete, and mixed discrete-continuum solvation approaches in application to association of the $\text{Li}^{+}$ cation with the $\text{[B(C}_2\text{O}_4\text{)}_2\text{]}^{-}$ anion ($\text{BOB}^{-}$). The previously unstudied EC:DMC binary mixture with the 7:3 weight or $\approx$70:30% mole ratio is chosen as the solvent. The EC:DMC binary mixtures with the component molar ratio ranging from 50:50% to 75:25% exhibit sufficiently high dielectric constants and relatively low viscosities, making them appropriate for applications in the LIB technology.$^{9}$ The main goal of the present study is to develop and validate an approach that allows one to describe the ion association at the quantitative level without a need to refer to any experimental data. This task is important for advancing LIBs using the novel electrolytes and solvent mixtures.

## 2. THEORETICAL METHODOLOGY

ACS Paragon Plus Environment

For the target ion association process, $\text{Li}^{+}_{(\text{solv})} + \text{BOB}^{-}_{(\text{solv})} = [\text{Li}^{+}\text{BOB}^{-}]_{(\text{solv})}$, the change in the corresponding standard thermodynamic potential ($\Delta_{\text{ass}} \Phi_{T}^{\text{o}}$) at the arbitrary temperature ($T$) can be calculated using the eq. 1.

$$
\Delta_{\text{ass}} \Phi_{T}^{\text{o}} = \Delta_{\text{ass(g)}} \Phi_{T}^{\text{o}} - \Delta_{\text{solv}} \Phi_{T}^{\text{o}} \left(\text{Li}^{+}\right) - \Delta_{\text{solv}} \Phi_{T}^{\text{o}} \left(\text{BOB}^{-}\right) + \Delta_{\text{solv}} \Phi_{T}^{\text{o}} \left(\left[\text{Li}^{+}\text{BOB}^{-}\right]\right). \tag{1}
$$

Here, $\Delta_{\text{ass(g)}} \Phi_{T}^{\text{o}}$ is the change in the standard thermodynamic potential for the gas phase (g) association process, $\text{Li}^{+}_{(\text{g})} + \text{BOB}^{-}_{(\text{g})} = [\text{Li}^{+}\text{BOB}^{-}]_{(\text{g})}$, and $\Delta_{\text{solv}} \Phi_{T}^{\text{o}}$ are the standard thermodynamic potential changes for solvation (solv) of the $\text{Li}^{+}$, $\text{BOB}^{-}$ ions and the $[\text{Li}^{+}\text{BOB}^{-}]$ ion pair (IP). Note that in addition to eq. 1, the $\Delta_{\text{solv}} \Phi_{T}^{\text{o}}$ value for a particle $P$ in an arbitrary solvent can be computed rigorously according to eq. 2.

$$
\Delta_{\text{solv}} \Phi_{T}^{\text{o}} (P) = \Phi_{T}^{\text{o}} (\text{solution}) - \Phi_{T}^{\text{o}} (\text{solvent}) - \Phi_{T}^{\text{o}} \left(P_{(\text{g})}\right). \tag{2}
$$

Taking into account that a statistical mechanical treatment of the condensed phases is expensive, instead, eq. 3 is widely used in the framework of quantum-chemical calculations of the $\Delta_{\text{solv}} \Phi_{T}^{\text{o}}$ potentials.

$$
\Delta_{\text{solv}} \Phi_{T}^{\text{o}} (P) \equiv \Phi_{T}^{\text{o}} \left(P_{(\text{solv})}\right) - \Phi_{T}^{\text{o}} \left(P_{(\text{g})}\right). \tag{3}
$$

The changes in the standard Gibbs free energy during ion association ($\Delta_{\text{ass}} G_{T}^{\text{o}}$) and solvation ($\Delta_{\text{solv}} G_{T}^{\text{o}}$) can be obtained using the corresponding enthalpy and entropy data at $T=298.15\text{K}$. The enthalpy and entropy changes show weak variation over a broad temperature range. The changes in ion association enthalpy ($\Delta_{\text{ass}} H_{298}^{\text{o}}$) and entropy ($\Delta_{\text{ass}} S_{298}^{\text{o}}$) as well as solvation Gibbs free energy ($\Delta_{\text{solv}} G_{T}^{\text{o}}$) depend on the accuracy of the enthalpy ($\Delta_{\text{solv}} H_{298}^{\text{o}}$) and entropy ($\Delta_{\text{solv}} S_{298}^{\text{o}}$) of solvation of the ions and IP. The thermodynamic potentials can be predicted using quantum-chemical calculations for the gas and condensed phases. The latter data can be obtained with the self-consistent reaction field (SCRF) methods.$^{10-11}$

### 2.1. Approaches.
In order to calculate the Gibbs free energy and equilibrium constant of ion association (Figure 1), we consider three solvation approaches (A). According to the first one,

continuum model (AI), the bare ions and IP are placed in a structureless polarized continuum (c) with the dielectric constant of the solvent. The second, discrete solvation approach (AII), involves an explicit consideration of the solvatocomplexes of the ions and IP in the gas phase, including solvent molecules most strongly interacting with the solutes. A combination of the approaches mentioned above constitutes the mixed or discrete-continuum framework (AIII).

Application of AI is straightforward. It involves computation of the properties of the ions and IP in the gas phase and in the structureless polarized continuum of the solvent mixture. AII requires gas phase calculations on a series of ion-molecular and IP-molecular solvatocomplexes. According to AIII, the most exergonic cation, anion and IP solvatocomplexes from AII should be considered in the solvent continuum, as in AI.

In principle a fully atomistic description of the solvent is preferable to a continuum or discrete-continuum model. At the same time, an explicit solvent model has its own limitations, for instance due to approximations of a particular density functional, a basis set, or the size of the solvent shell that can be included in an explicit calculation given available computational resources. Working within the limits of the current theoretical approximations for the explicit and continuum descriptions of the solvent, we demonstrate that the mixed discrete-continuum provides the best results, while at the same time, remaining computationally efficient.

The separation between the explicit and continuum components of the mixed model is defined by solid physical arguments. The explicit part includes the first solvation shell of the ions surrounded by the most strongly interacting and abundant solvent molecules. Including the first solvation shell of the solvent without account for polarization of the remainder of the solvent leads to significant errors in solvation thermodynamics. Similarly, representing the entire complex by a continuum model ignores specific interactions between the solute and the first solvation shell, providing another source of error. The combination of the two descriptions gives a sound approach, in which the two errors cancel.

Chart 1 represents the set of solvation processes involving $Li^+$, $BOB^-$ ions and the $[Li^+BOB^-]$ IP,

and needed for the thermodynamic calculations of $\Delta_{\text{solv}} \Phi_{298}^{\text{o}}$ within the three approaches. The chart also shows the ion association processes, for which the $\Delta_{\text{ass}} \Phi_{298}^{\text{o}}$ values ($\Phi = H, S, G$) were computed in the EC:DMC (7:3) binary solvent mixture. Due to high dipole moment and favorable geometry (see Figure 2c), the EC molecule has a higher affinity to the bare ions and IP than the DMC molecule, as observed experimentally for the $\text{Li}^{+}$ ion.$^{12\text{-}13}$ In combination with a considerably larger EC mole fraction in a mixture with DMC, one expects preferential solvation of the ion species by EC molecules. This expectation is enhanced further by the higher, $\approx$70 % molar content of EC relative to $\approx$30% of DMC.

![](./images/811260243672563716_5.jpg)

**Chart 1.** The investigated processes for the solution of the LiBOB salt in the EC:DMC (7:3) binary solvent mixture, obtained within the continuum (AI), discrete (AII) and mixed (AIII) solvation approaches (g – gas phase, c – continuum; $n = 1$–5 – coordination numbers of the $\text{Li}^{+}$ ion in the $[\text{Li(EC)}_{n}]^{+}$ solvatocomplexes, $\# = A$–$D$ – coordination types of the EC molecule in the $[\text{BOB(EC)}^{\#}]^{-}$ solvatocomplexes defined in Figure 2$i$–$l$, $m = 1, 2$ – coordination numbers of the $\text{Li}^{+}$ ion by EC in the $[\text{Li}^{+}\text{(EC)}_{m}\text{BOB}^{-}]$ solvatocomplexes).

### 2.2. Computations.
The quantum-chemical calculations were carried out with Gaussian 03.$^{14}$ The 6-31+G(2d) basis set and the B3LYP exchange-correlational functional were used.$^{15}$ The geometry optimization was done in two steps. First, the local minimum on the potential energy surface was founded using numerical second derivatives with respect to the nuclear coordinates. Then, the optimization was continued with the more robust analytical second derivatives. The latter also gave harmonic vibrational frequencies needed for thermodynamic analysis. The analytic second derivatives

were particularly important for the construction of the solvent-saturated solvation shells for the AII approach, since these derivatives were used to confirm that the found structures corresponded to local minima. The pressure $p^\circ$=101325 Pa (1 atm) and the most abundant isotopes were used for the thermodynamic data calculation within the ideal gas approximation (gas standard state). The basis set superposition error was taken into account using the counterpoise correction.

The isodensity polarizable continuum model (IPCM)$^{16}$ with the dielectric constant of 51.0 for the EC:DMC (7:3) binary solvent$^{17}$ was applied to represent the structureless solvent continuum in methods AI and AIII. Note that the SCRF computations employing the IPCM technique do not require a predefined or manually scaled atomic radii, in contrast to the more traditional PCM model. It is known in the case of the $Li^+$ ion that the van-der-Waals radius has to be scaled up significantly to obtain good results.$^{5}$ The solute energies were computed in a solvent cavity with the isodensity surface contour equal to $0.0002 e \cdot Bohr^{-3}$. The solution standard state was customarily defined to have the $1\ \text{mol·L}^{-1}$ concentration for all solute particles, while at the same time, neglecting solute-solute interactions.

2.3. Validation. The calculation results were validated by comparison of the B3LYP/6-31+G(2d) level of theory with the reference coupled-cluster calculations and X-ray experimental data. The aug-cc-pVDZ and 6-31+G(2d) basis sets were used in the CCSD(full) method. Geometric properties and dipole moment of the EC molecule (see Figure 2c), geometric properties of the $BOB^-$ ion (see Figure 2a), and the potential energy profile of the ion-molecular interaction for the $[Li(EC)]^+$ solvatocomplex were selected for validation. The experimental data for the EC molecule in the crystal and liquid states, as well as for the $BOB^-$ ion in the MeBOBs (Me = Li, Na, K) and $[Li(EC)_4]BOB$ crystals were used for the comparison. Some geometrical parameters and dipole moment of the EC molecule and $BOB^-$ ion obtained from the quantum-chemical calculations and experiments are presented in Tables 1 and 2, respectively.

Table 1. Selected bond distances $(d)$, valence angles $(a)$ and dipole moments $(\mu)$ of the EC $(C_2)$

![](./images/811260243672563716_6.jpg)

molecule obtained using the basic, B3LYP/6-31+G(2d), and reference, CCSD(full)/aug-cc-pVDZ and 6-31+G(2d), levels of quantum-chemical theory in gas phase, and those deduced from the X-ray experiments for the condensed phases. The subscript "(c)" designates the carbonyl group.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>CCSD(full)/ aug-cc-pVDZ</th>
      <th>B3LYP/ 6-31+G(2d)</th>
      <th>CCSD(full)/ 6-31+G(2d)</th>
      <th>X-ray crystal¹⁸ / liquid¹⁹</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$d(\text{C}_{(\text{c})}\text{O}_{(\text{c})})$, Å</td>
      <td>1.196</td>
      <td>1.191</td>
      <td>1.187</td>
      <td>1.15 / 1.20±0.09</td>
    </tr>
    <tr>
      <td>$d(\text{OC}_{(\text{c})})$, Å</td>
      <td>1.365</td>
      <td>1.359</td>
      <td>1.354</td>
      <td>1.33 / 1.34±0.12</td>
    </tr>
    <tr>
      <td>$d(\text{CO})$, Å</td>
      <td>1.442</td>
      <td>1.434</td>
      <td>1.432</td>
      <td>1.40 / 1.46±0.13</td>
    </tr>
    <tr>
      <td>$d(\text{CC})$, Å</td>
      <td>1.533</td>
      <td>1.534</td>
      <td>1.525</td>
      <td>1.52 / 1.52±0.11</td>
    </tr>
    <tr>
      <td>$d(\text{CH})$, Å</td>
      <td>1.097 / 1.101</td>
      <td>1.092 / 1.096</td>
      <td>1.094 / 1.099</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$a(\text{OC}_{(\text{c})}\text{O}_{(\text{c})})$, °</td>
      <td>124.76</td>
      <td>124.84</td>
      <td>124.80</td>
      <td>124.5 / –</td>
    </tr>
    <tr>
      <td>$a(\text{OC}_{(\text{c})}\text{O})$, °</td>
      <td>110.48</td>
      <td>110.32</td>
      <td>110.40</td>
      <td>111.0 / –</td>
    </tr>
    <tr>
      <td>$a(\text{COC}_{(\text{c})})$, °</td>
      <td>108.93</td>
      <td>109.83</td>
      <td>109.00</td>
      <td>109.0 / –</td>
    </tr>
    <tr>
      <td>$a(\text{CCO})$, °</td>
      <td>102.51</td>
      <td>103.03</td>
      <td>102.31</td>
      <td>102.0 / –</td>
    </tr>
    <tr>
      <td>$a(\text{HCO})$, °</td>
      <td>108.53 / 108.72</td>
      <td>108.53 / 108.51</td>
      <td>108.68 / 108.69</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$\mu$, D</td>
      <td>5.47</td>
      <td>5.54</td>
      <td>5.61</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

The data of Tables 1 and 2 show excellent agreement between the reference and basic levels of theory, and between the theories and the X-ray experiments. This fact indicates that the B3LYP/6-31+G(2d) method is able to reproduce the structure and charge distribution of the molecular and ionic species. Figure 1 show the basic and reference profiles of the potential energy surface for the gas phase $[\text{Li(EC)}]^+$ solvatocomplex as a function of the ion–molecule distance.

Table 2. Selected bond distances ($d$) and valence angles ($a$) of the $\text{BOB}^-$ ($D_{2d}$) ion obtained using the basic, B3LYP/6-31+G(2d), and reference, CCSD(full)/aug-cc-pVDZ and 6-31+G(2d), levels of quantum-chemical theory in gas phase, and those deduced from the X-ray experiments on crystals. The subscript "(c)" designates the carbonyl group.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>CCSD(full)/ aug-cc-pVDZ</th>
      <th>B3LYP/ 6-31+G(2d)</th>
      <th>X-ray $\text{Me}^\text{l}\text{BOBs}^{20}$</th>
      <th>X-ray $[\text{Li(EC)}_4]\text{BOB}^{21}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$d(\text{OB})$, Å</td>
      <td>1.483</td>
      <td>1.473</td>
      <td>1.474</td>
      <td>1.4707</td>
    </tr>
    <tr>
      <td>$d(\text{CO})$, Å</td>
      <td>1.334</td>
      <td>1.328</td>
      <td>1.326</td>
      <td>1.3320</td>
    </tr>
    <tr>
      <td>$d(\text{O}_{(\text{c})}\text{C})$, Å</td>
      <td>1.209</td>
      <td>1.203</td>
      <td>1.198</td>
      <td>1.1908</td>
    </tr>
    <tr>
      <td>$d(\text{CC})$, Å</td>
      <td>1.553</td>
      <td>1.554</td>
      <td>1.538</td>
      <td>1.536</td>
    </tr>
    <tr>
      <td>$a(\text{O}_{(\text{c})}\text{CO})$, °</td>
      <td>126.49</td>
      <td>126.46</td>
      <td>127.4</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$a(\text{O}_{(\text{c})}\text{CC})$, °</td>
      <td>125.93</td>
      <td>126.37</td>
      <td>124.5</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

<table>
  <tr>
    <td>$a(\text{OCC}),\ ^{\circ}$</td>
    <td>107.58</td>
    <td>107.17</td>
    <td>108.0</td>
    <td>–</td>
  </tr>
  <tr>
    <td>$a(\text{OBO}),\ ^{\circ}$</td>
    <td>105.43 / 111.53</td>
    <td>105.06 / 111.72</td>
    <td>109.5</td>
    <td>–</td>
  </tr>
</table>

![](./images/811260243672563716_7.jpg)

Figure 1. Potential energy profiles of the gas phase $[\text{Li(EC)}]^+$ ($C_2$) solvatocomplex along the lithium–oxygen coordinate, $d(\text{LiO}_{(c)})$, obtained using the basic, B3LYP/6-31+G(2d) (blue circles), and reference, CCSD(full)/aug-cc-pVDZ (dark red diamonds), levels of quantum-chemical theory. The subscript "(c)" designates the carbonyl group. The basic curve is shifted up by 0.86 Ha.

Figure 1 shows that the overall shape and location of the minimum on the potential energy curve relevant to the solvation process agree between the basic, B3LYP/6-31+G(2d), and highly rigorous, CCSD(full)/aug-cc-pVDZ, theory levels. It is known that in some cases B3LYP can overestimate the solvent binding energy⁷, however, it is not the case here, as evidenced by the data of Figure 1. Thus, the B3LYP/6-31+G(2d) description provides a good representation of the ion–molecule interaction involved in the solvation process.

## 3. RESULTS AND DISCUSSION

### 3.1.1. Solvatocomplexes Formation.
The gas phase structures of the $\text{BOB}^-$ ion, $[\text{Li}^+\text{BOB}^-]$ IP,

EC molecule, and the $[\text{Li(EC)}_n]^+$ ($n=1$–5), $[\text{BOB(EC)}^{\#}]^-$ ($\#=A$–$D$) and $[\text{Li}^+(\text{EC})_m\text{BOB}^-]$ ($m=1,2$) solvatocomplexes are shown in the Figure 2.

![](./images/811260243672563716_8.jpg)

Figure 2. Gas phase optimized structures of the $\text{BOB}^-$ ion (a), the $[\text{Li}^+\text{BOB}^-]$ ion pair (b), the EC molecule (c), and the $[\text{Li(EC)}_{1\text{–}5}]^+$ (d–h), $[\text{BOB(EC)}^{A\text{–}D}]^-$ (i–l) and $[\text{Li}^+(\text{EC})_{1,2}\text{BOB}^-]$ (m,n) solvatocomplexes. The symbols $A$–$D$ refer to coordination types of the EC molecule with respect to the $\text{BOB}^-$ ion in the $[\text{BOB(EC)}^{A\text{–}D}]^-$ structures shown in the figure.

Table 3 contains selected geometric data for the EC molecule, $\text{BOB}^-$ ion, $[\text{Li}^+\text{BOB}^-]$ IP and the $[\text{Li(EC)}_n]^+$ and $[\text{Li}^+(\text{EC})_m\text{BOB}^-]$ solvatocomplexes. The data were computed in the gas phase at the B3LYP/6-31+G(2d) level of theory. The $\text{Li}^+$ ion strongly polarizes the carbonyl groups of the coordinated EC molecules and $\text{BOB}^-$ ion in the $[\text{Li(EC)}_n]^+$, $[\text{Li}^+\text{BOB}^-]$ and $[\text{Li}^+(\text{EC})_m\text{BOB}^-]$ structures. This action results in the substantial lengthening of the double bonds of the coordinated species. As the first coordination sphere around the $\text{Li}^+$ ion gets saturated, the distances from $\text{Li}^+$ to the carbonyl oxygen atoms are increasing, and the corresponding valence angles are decreasing, as a result of ligand repulsion

and incrementing.

Table 3. Selected bond distances ($d$) and valence angles ($a$) of the EC molecule, $BOB^-$ ion, $[Li^+BOB^-]$ ion pair, and the $[Li(EC)_n]^+$ ($n = 1$-$5$) and $[Li^+(EC)_mBOB^-]$ ($m = 1, 2$) solvatocomplexes obtained using the basic, B3LYP/6-31+G(2d), level of theory in gas phase (see Figure $2a$-$h$, $m$-$n$). The subscript "(c)" designates the carbonyl group.

<table>
  <thead>
    <tr>
      <th>Particle</th>
      <th>$d(\text{O}_{(\text{c})}\text{C}_{(\text{c})})$, Å</th>
      <th>$d(\text{LiO}_{(\text{c})})$, Å</th>
      <th>$a(\text{LiO}_{(\text{c})}\text{C}_{(\text{c})})$, °</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC ($C_2$)</td>
      <td>1.191</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$[\text{Li(EC)}]^+$ ($C_2$)</td>
      <td>1.224</td>
      <td>1.734</td>
      <td>180.0</td>
    </tr>
    <tr>
      <td>$[\text{Li(EC)}_2]^+$</td>
      <td>1.216</td>
      <td>1.783</td>
      <td>180.0</td>
    </tr>
    <tr>
      <td>$[\text{Li(EC)}_3]^+$</td>
      <td>1.208</td>
      <td>1.849, 1.851, 1.850</td>
      <td>171.8, 166.4, 174.0</td>
    </tr>
    <tr>
      <td>$[\text{Li(EC)}_4]^+$</td>
      <td>1.204, 1.203, 1.204,<br>1.204</td>
      <td>1.943, 1.927, 1.940,<br>1.932</td>
      <td>144.6, 153.8, 142.3,<br>146.8</td>
    </tr>
    <tr>
      <td>$[\text{Li(EC)}_5]^+$</td>
      <td>1.202, 1.200, 1.202,<br>1.199, 1.198</td>
      <td>1.998, 2.148, 1.993,<br>2.266, 1.955</td>
      <td>134.9, 139.3, 136.5,<br>138.7, 174.5</td>
    </tr>
    <tr>
      <td>$BOB^-$ ($D_{2d}$)</td>
      <td>1.203</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>$[\text{Li}^+BOB^-]$ ($C_{2v}$)</td>
      <td>1.230 / 1.192</td>
      <td>1.893</td>
      <td>101.9</td>
    </tr>
    <tr>
      <td>$[\text{Li}^+(\text{EC})BOB^-]$</td>
      <td>1.225 / 1.194, 1.193 //<br>1.208</td>
      <td>1.957, 1.956 // 1.848</td>
      <td>103.1 // 151.7</td>
    </tr>
    <tr>
      <td>$[\text{Li}^+(\text{EC})_2BOB^-]$</td>
      <td>1.217 / 1.195, 1.196 //<br>1.205, 1.207</td>
      <td>2.053, 2.049 // 1.909,<br>1.957</td>
      <td>102.2, 102.3 // 134.9,<br>129.2</td>
    </tr>
  </tbody>
</table>

The standard changes in the calculated thermodynamic potentials of the $[\text{Li}^+BOB^-]$ IP, and the $[\text{Li(EC)}_n]^+$ ($n = 1$-$5$), $[\text{BOB(EC)}^\#]^-$ ($\# = A$-$D$) and $[\text{Li}^+(\text{EC})_mBOB^-]$ ($m = 1, 2$) solvatocomplexes formation in the gas phase are collected in the Table 4. This table contain $\Delta_{\text{ass(g)}}\Phi_{298}^\text{o}$ potentials ($\Delta\Phi_{298}^\text{o}$ values for the $[\text{Li}^+BOB^-]_{(\text{g})}$), that is significant for the eq. 1 application. The data of Table 4 show that the contact IP should be extremely stable, since $\Delta G_{298}^\text{o} = -486.7\text{kJ·mol}^{-1}$, i.e. considerably less than zero. The IP stability arises due to both Coulomb interaction, and chelate bonding of $\text{Li}^+$ by the $BOB^-$ ion (see Figure $2b$).

Table 4. Changes in potential energy ($\Delta E$), standard internal energy ($\Delta U_{298}^\text{o}$), enthalpy ($\Delta H_{298}^\text{o}$), entropy

$(\Delta S_{298}^{\mathrm{o}})$ and Gibbs free energy $(\Delta G_{298}^{\mathrm{o}})$ of gas phase (g) formation of the $[\mathrm{Li}^{+}\mathrm{BOB}^{-}]$ IP, and the $[\mathrm{Li}(\mathrm{EC})_{n}]^{+}$ ($n=1$-$5$), $[\mathrm{BOB}(\mathrm{EC})^{\#}]^{-}$ ($\#=A$-$D$) and $[\mathrm{Li}^{+}(\mathrm{EC})_{m}\mathrm{BOB}^{-}]$ ($m=1,2$) solvatocomplexes. The symbols $A$, $B$, $C$ and $D$ refer to coordination types of the EC molecule with respect to the $\mathrm{BOB}^{-}$ ion in the $[\mathrm{BOB}(\mathrm{EC})^{A-D}]^{-}$ structures (see Figure $2i$-$l$).

<table>
  <thead>
    <tr>
      <th>Complex formation process</th>
      <th>$\Delta E$,<br>$\mathrm{kJ{\cdot}mol^{-1}}$</th>
      <th>$\Delta U_{298}^{\mathrm{o}}$,<br>$\mathrm{kJ{\cdot}mol^{-1}}$</th>
      <th>$\Delta H_{298}^{\mathrm{o}}$,<br>$\mathrm{kJ{\cdot}mol^{-1}}$</th>
      <th>$\Delta S_{298}^{\mathrm{o}}$,<br>$\mathrm{J{\cdot}mol_{1}^{-1}{\cdot}K^{-}}$</th>
      <th>$\Delta G_{298}^{\mathrm{o}}$,<br>$\mathrm{kJ{\cdot}mol^{-1}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + BOB^{-}_{(g)} = [Li^{+}BOB^{-}]_{(g)}}$</td>
      <td>$-523.9$</td>
      <td>$-517.3$</td>
      <td>$-519.7$</td>
      <td>$-110.9$</td>
      <td>$\boldsymbol{-486.7}$</td>
    </tr>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + EC_{(g)} = [Li(EC)]^{+}_{(g)}}$</td>
      <td>$-212.4$</td>
      <td>$-205.3$</td>
      <td>$-207.8$</td>
      <td>$-86.3$</td>
      <td>$\boldsymbol{-182.0}$</td>
    </tr>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + 2EC_{(g)} = [Li(EC)_{2}]^{+}_{(g)}}$</td>
      <td>$-374.1$</td>
      <td>$-357.2$</td>
      <td>$-362.2$</td>
      <td>$-188.1$</td>
      <td>$\boldsymbol{-306.1}$</td>
    </tr>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + 3EC_{(g)} = [Li(EC)_{3}]^{+}_{(g)}}$</td>
      <td>$-469.0$</td>
      <td>$-446.1$</td>
      <td>$-453.5$</td>
      <td>$-310.3$</td>
      <td>$\boldsymbol{-361.0}$</td>
    </tr>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + 4EC_{(g)} = [Li(EC)_{4}]^{+}_{(g)}}$</td>
      <td>$-523.9$</td>
      <td>$-493.4$</td>
      <td>$-503.3$</td>
      <td>$-449.6$</td>
      <td>$\boldsymbol{-369.3}$</td>
    </tr>
    <tr>
      <td>$\mathrm{Li^{+}_{(g)} + 5EC_{(g)} = [Li(EC)_{5}]^{+}_{(g)}}$</td>
      <td>$-531.4$</td>
      <td>$-496.8$</td>
      <td>$-509.2$</td>
      <td>$-604.0$</td>
      <td>$\boldsymbol{-329.1}$</td>
    </tr>
    <tr>
      <td>$\mathrm{BOB^{-}_{(g)} + EC_{(g)} = [BOB(EC)^{A}]^{-}_{(g)}}$</td>
      <td>$-46.1$</td>
      <td>$-37.8$</td>
      <td>$-40.3$</td>
      <td>$-94.0$</td>
      <td>$\boldsymbol{-12.3}$</td>
    </tr>
    <tr>
      <td>$\mathrm{BOB^{-}_{(g)} + EC_{(g)} = [BOB(EC)^{B}]^{-}_{(g)}}$</td>
      <td>$-37.1$</td>
      <td>$-28.9$</td>
      <td>$-31.4$</td>
      <td>$-85.4$</td>
      <td>$\boldsymbol{-5.9}$</td>
    </tr>
    <tr>
      <td>$\mathrm{BOB^{-}_{(g)} + EC_{(g)} = [BOB(EC)^{C}]^{-}_{(g)}}$</td>
      <td>$-40.1$</td>
      <td>$-31.9$</td>
      <td>$-34.4$</td>
      <td>$-68.0$</td>
      <td>$\boldsymbol{-14.1}$</td>
    </tr>
    <tr>
      <td>$\mathrm{BOB^{-}_{(g)} + EC_{(g)} = [BOB(EC)^{D}]^{-}_{(g)}}$</td>
      <td>$-40.0$</td>
      <td>$-34.3$</td>
      <td>$-36.8$</td>
      <td>$-105.3$</td>
      <td>$\boldsymbol{-5.4}$</td>
    </tr>
    <tr>
      <td>$\mathrm{[Li^{+}BOB^{-}]_{(g)} + EC_{(g)} = [Li^{+}(EC)BOB^{-}]_{(g)}}$</td>
      <td>$-101.5$</td>
      <td>$-92.2$</td>
      <td>$-94.7$</td>
      <td>$-94.9$</td>
      <td>$\boldsymbol{-66.4}$</td>
    </tr>
    <tr>
      <td>$\mathrm{[Li^{+}BOB^{-}]_{(g)} + 2EC_{(g)} = [Li^{+}(EC)_{2}BOB^{-}]_{(g)}}$</td>
      <td>$-166.8$</td>
      <td>$-149.1$</td>
      <td>$-154.1$</td>
      <td>$-245.7$</td>
      <td>$\boldsymbol{-80.8}$</td>
    </tr>
  </tbody>
</table>

Changes in the Gibbs free energy for the $\mathrm{Li^{+}_{(g)} + nEC_{(g)} = [Li(EC)_{n}]^{+}_{(g)}}$ processes are negative and decrease down to $-369.3\ \mathrm{kJ{\cdot}mol^{-1}}$ for the four-coordinated solvatocomplex (see Figure $2d$-$g$). Taking into account the higher affinity of the EC molecules to the bare $\mathrm{Li^{+}}$ ion compared to DMC and the larger EC mole fraction, $\approx 70\ \%$ vs. $\approx 30\%$ for DMC, it is reasonable to expect that the most exergonic solvatocomplex, $[\mathrm{Li(EC)}_{4}]^{+}$, as determined in the gas phase cluster calculation, should dominate in solution, and fractions of other solvatocomplexes should be small.$^{12,22-23}$ The difference in the Gibbs free energy of formation of the $[\mathrm{Li(EC)}_{3}]^{+}$ and $[\mathrm{Li(EC)}_{4}]^{+}$ solvatocomplexes is less than $10\ \mathrm{kJ{\cdot}mol^{-1}}$, whereas the corresponding potential energy difference is much greater, approaching $50\ \mathrm{kJ{\cdot}mol^{-1}}$. The example described above demonstrates that it is very important to consider the Gibbs free energy rather than the

potential energy changes. The latter is used often for the thermodynamic characterization of various processes, since potential energy can be easily obtained from quantum-chemical calculations. $^{24-25}$ An even stronger case is formation of the $[Li(EC)_{5}]^{+}$ (see Figure $2 h$ ) from $[Li(EC)_{4}]^{+}$ . This process has a negative potential energy change and a positive Gibbs free energy change. Thus, this unfavorable process can be predicted erroneously as favorable based on the potential energy difference alone. The $[Li(EC)_{5}]^{+}$ solvatocomplex $(\Delta G_{298}^{o}=-329.1 kJ \cdot mol^{-1})$ has not been discussed previously as a possible form of the $[Li(EC)_{n}]^{+}$ in solution. $^{7,24,26-27}$ Due to translational dynamics and strong dipole-dipole repulsions of EC molecules in $[Li(EC)_{5}]^{+}$ , the latter is expected to be unstable in the bulk solution.

Ion-dipole interactions between the $BOB^{-}$ ion and EC molecules are extremely weak. The $\Delta G_{298}^{o}$ values for the $[BOB(EC)^{\#}]^{-}$ formation, where $\#=A-D$ is the EC coordination type (see Figure $2 i-l$ ) vary only from $-5.4 ~kJ \cdot mol^{-1}$ (type $D$ ) to $-14.1 ~kJ \cdot mol^{-1}$ (type $C$ ). Such low values can be explained by the large size of the $BOB^{-}$ ion, resulting in low specific density of the negative charge. Consequently, the BOB- anion cannot be strongly solvated in solution even by highly polar molecules such as EC.

The lithium site of the $[Li^{+} BOB^{-}]$ contact IP is not sterically saturated and can additionally attach one or two EC molecules (see Figure $2 m, n$ ). These processes are not as exergonic as formation of the $[Li(EC)_{n}]^{+}$ solvatocomplexes discussed above. The corresponding $\Delta G_{298}^{o}$ values for the $[Li^{+}(EC) BOB^{-}]$  and $[Li^{+}(EC)_{2} BOB^{-}]$ are -66.4 and $-80.8 ~kJ \cdot mol^{-1}$ . In other words, the first EC molecule binds to $[Li^{+} BOB^{-}]$ quite strongly, while the affinity of the second EC molecule to the IP monosolvate is small and comparable to the free Gibbs energy of the $[BOB(EC)^{\#}]^{-}$ formation. The two explicit EC molecules are sufficient for the complete saturation of the lithium solvation shell in the $[Li^{+} BOB^{-}]$ IP. Therefore, the coordination number of $Li^{+}$ in the solvated cation as well as in the solvated IP is defined by the carbonyl oxygen atoms and is equal to four.

According to the gas phase calculations (Table 4), the $[Li(EC)_{4}]^{+}$ cation, the $[BOB(EC)^{C}]^{-}$ anion, and the $[Li^{+}(EC)_{2} BOB^{-}]$ IP solvatocomplexes are the most stable species. Therefore, these species were chosen in the framework of the discrete (AIl) approach to characterize ion association of LiBOB in the

EC:DMC (7:3) binary mixture.

#### 3.1.2. SCRF Application.
The SCRF quantum-chemical calculations of the bare $Li^+$ and $BOB^-$ ions, the $[Li^+BOB^-]$ IP, the EC molecule, and the $[Li(EC)_4]^+$ and $[Li^+(EC)_2BOB^-]$ solvatocomplexes were carried out using the experimental value of dielectric constant (51.0) of the EC:DMC (7:3) binary mixture$^{17}$. The changes in the standard enthalpy of solvation within the simplest AI model, $\Delta_{solv(I)}H_{298}^{\circ}$, were estimated according to the eq. 4.

$$
\Delta_{solv(I)}H_{298}^{\circ} = \Delta_{solv(I)}E + p^{\circ}V^{\circ} - 298.15R \equiv \Delta_{solv(I)}E - 2.38\ \mathrm{kJ{\cdot}mol^{-1}}. \tag{4}
$$

Here, $\Delta_{solv(I)}E$ is the potential energy change during the solvation within AI, and $V^{\circ}=0.001\ \mathrm{m^3{\cdot}mol^{-1}}$ is the standard molar volume that is accessible by the solute particle in the solution standard state.

The isothermal compression stage of solvation decreases the translational entropy of transferring particles within the AI model. Those changes in the standard entropy of solvation, $\Delta_{solv(I)}S_{298}^{\circ}$, were taken into account with eq. 5.

$$
\Delta_{solv(I)}S_{298}^{\circ} = R\left(\ln V^{\circ} - \ln\frac{298.15R}{p^{\circ}}\right) = -26.58\ \mathrm{J{\cdot}mol^{-1}{\cdot}K^{-1}}. \tag{5}
$$

Since different standard states for the solvent and solute are usually used$^{28}$, the $V^{\circ}$ values for EC in eq. 4 and 5, molar volume that is accessible for the particular co-solvent molecules in target EC:DMC (7:3) binary solvent mixture, were preliminarily calculated from experimental data$^{29}$ and substituted on the $V_{EC}^{\circ}=1.024{\cdot}10^{-4}\ \mathrm{m^3{\cdot}mol^{-1}}$.

The changes in the standard thermodynamic potentials of solvation within AIII, $\Delta_{solv(III)}\Phi_{298}^{\circ}$, can be found as linear combinations of the corresponding data obtained within AI and AII (see Chart 1).

### 3.2. Solvation Data.
The changes in the standard enthalpy, entropy and Gibbs free energy of the solvation processes are summarized in Table 5 for the different solvation approaches ($\Delta_{solv(A)}\Phi_{298}^{\circ}$). In spite of a significant dipole moment value even in the gas phase, the EC molecules gives a very small magnitude of $\Delta_{solv(I)}G_{298}^{\circ}=-12.6\ \mathrm{kJ{\cdot}mol^{-1}}$. The bare $Li^+$ ion has a small radius, and consequently, a high

polarizing action. Hence, its transfer into the structureless continuum is characterized by an extremely negative change in the standard Gibbs free energy, which is equal to $-579.2\ \text{kJ·mol}^{-1}$. The same value for the saturated $[\text{Li(EC)}_4]^+$ solvatocomplex is almost four times smaller by module, because of the size increase upon binding of the four EC molecules. The $\Delta_{\text{solv(III)}}G_{298}^{\text{o}}$ value for the $\text{Li}^+$ ion is intermediate between those for the AI and AII models, and is equal to $-463.9\ \text{kJ·mol}^{-1}$.

**Table 5.** Changes in standard enthalpy ($\Delta_{\text{solv(A)}}H_{298}^{\text{o}}$), entropy ($\Delta_{\text{solv(A)}}S_{298}^{\text{o}}$) and Gibbs free energy ($\Delta_{\text{solv(A)}}G_{298}^{\text{o}}$) of solvation of the EC molecule, the $\text{Li}^+$ and $\text{BOB}^-$ ions, and the $[\text{Li}^+\text{BOB}^-]$ IP in the EC:DMC (7:3) binary solvent, obtained using the continuum (I), discrete (II) and mixed (III) solvation approaches (A) (g – gas, c – continuum).

<table>
  <thead>
    <tr>
      <th>Particle</th>
      <th>A</th>
      <th>Solvation process</th>
      <th>$\Delta_{\text{solv(A)}}H_{298}^{\text{o}},$<br>$\text{kJ·mol}^{-1}$</th>
      <th>$\Delta_{\text{solv(A)}}S_{298}^{\text{o}},$<br>$\text{J·mol}^{-1}·\text{K}^{-1}$</th>
      <th>$\Delta_{\text{solv(A)}}G_{298}^{\text{o}},$<br>$\text{kJ·mol}^{-1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EC</td>
      <td>I</td>
      <td>$\text{EC}_{(\text{g})}=\text{EC}_{(\text{c})}$</td>
      <td>$-26.1$</td>
      <td>$-45.5$</td>
      <td>$\textbf{-12.6}$</td>
    </tr>
    <tr>
      <td rowspan="4">$\text{Li}^+$</td>
      <td>I</td>
      <td>$\text{Li}^+_{(\text{g})}=\text{Li}^+_{(\text{c})}$</td>
      <td>$-587.1$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-579.2}$</td>
    </tr>
    <tr>
      <td>II</td>
      <td>$\text{Li}^+_{(\text{g})}+4\text{EC}_{(\text{g})}=[\text{Li(EC)}_4]^+_{(\text{g})}$</td>
      <td>$-503.3$</td>
      <td>$-449.6$</td>
      <td>$\textbf{-369.3}$</td>
    </tr>
    <tr>
      <td>I</td>
      <td>$[\text{Li(EC)}_4]^+_{(\text{g})}=[\text{Li(EC)}_4]^+_{(\text{c})}$</td>
      <td>$-152.8$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-144.9}$</td>
    </tr>
    <tr>
      <td>III</td>
      <td>$\text{Li}^+_{(\text{g})}+4\text{EC}_{(\text{c})}=[\text{Li(EC)}_4]^+_{(\text{c})}$</td>
      <td>$-551.5$</td>
      <td>$-294.0$</td>
      <td>$\textbf{-463.9}$</td>
    </tr>
    <tr>
      <td rowspan="3">$\text{BOB}^-$</td>
      <td>I</td>
      <td>$\text{BOB}^-_{(\text{g})}=\text{BOB}^-_{(\text{c})}$</td>
      <td>$-172.1$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-164.2}$</td>
    </tr>
    <tr>
      <td>II</td>
      <td>$\text{BOB}^-_{(\text{g})}+\text{EC}_{(\text{g})}=[\text{BOB(EC)}^C]^-_{(\text{g})}$</td>
      <td>$-34.4$</td>
      <td>$-68.0$</td>
      <td>$\textbf{-14.1}$</td>
    </tr>
    <tr>
      <td>III</td>
      <td>$\text{BOB}^-_{(\text{g})}+0\text{EC}_{(\text{c})}=\text{BOB}^-_{(\text{c})}$</td>
      <td>$-172.1$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-164.2}$</td>
    </tr>
    <tr>
      <td rowspan="4">$[\text{Li}^+\text{BOB}^-]$</td>
      <td>I</td>
      <td>$[\text{Li}^+\text{BOB}^-]_{(\text{g})}=[\text{Li}^+\text{BOB}^-]_{(\text{c})}$</td>
      <td>$-51.9$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-44.0}$</td>
    </tr>
    <tr>
      <td>II</td>
      <td>$[\text{Li}^+\text{BOB}^-]_{(\text{g})}+2\text{EC}_{(\text{g})}=[\text{Li}^+(\text{EC})_2\text{BOB}^-]_{(\text{g})}$</td>
      <td>$-154.1$</td>
      <td>$-245.7$</td>
      <td>$\textbf{-80.8}$</td>
    </tr>
    <tr>
      <td>I</td>
      <td>$[\text{Li}^+(\text{EC})_2\text{BOB}^-]_{(\text{g})}=[\text{Li}^+(\text{EC})_2\text{BOB}^-]_{(\text{c})}$</td>
      <td>$-65.0$</td>
      <td>$-26.6$</td>
      <td>$\textbf{-57.1}$</td>
    </tr>
    <tr>
      <td>III</td>
      <td>$[\text{Li}^+\text{BOB}^-]_{(\text{g})}+2\text{EC}_{(\text{c})}=[\text{Li}^+(\text{EC})_2\text{BOB}^-]_{(\text{c})}$</td>
      <td>$-166.8$</td>
      <td>$-181.2$</td>
      <td>$\textbf{-112.8}$</td>
    </tr>
  </tbody>
</table>

Taking into account that $\Delta_{\text{solv(I)}}G_{298}^{\text{o}}=-164.2\ \text{kJ·mol}^{-1}$ for the bare $\text{BOB}^-$ ion, its symmetric polarization by the structureless continuum is almost ten times more exergonic, as compared with the formation of $[\text{BOB(EC)}^C]^-$ anion in the gas phase. Therefore, consideration of any EC unsaturated

solvatocomplexes involving the $BOB^-$ ion is not reasonable and, as sequence, we taken
$\Delta_{\text{solv(III)}} \Phi_{298}^{\text{o}} \equiv \Delta_{\text{solv(I)}} \Phi_{298}^{\text{o}}$ (see Table 5).

As for the neutral $[Li^+BOB^-]$ IP as well as for the more spatial extended $[Li^+(EC)_2BOB^-]$ neutral
solvatocomplex the corresponding $\Delta_{\text{solv(I)}} G_{298}^{\text{o}}$ values are around $-50\ \text{kJ·mol}^{-1}$, that is almost a factor of
three smaller than for the bare $BOB^-$ ion. Simultaneously, the $\Delta_{\text{solv(II)}} G_{298}^{\text{o}}$ value for the $[Li^+BOB^-]$ IP is
only equal to $-80.8\ \text{kJ·mol}^{-1}$. Consequently, both discrete and continuum contributions to solvation of
the $[Li^+BOB^-]$ IP are significant and are accounted for within AIII model. The corresponding change in
the standard Gibbs free energy is equal to $-112.8\ \text{kJ·mol}^{-1}$.

### 3.3. Ion Association.
Table 6 presents the changes in the standard enthalpy, entropy and Gibbs
free energy for the $Li^+$ and $BOB^-$ ion association, obtained within the three different solvation
approaches ($\Delta_{\text{ass(A)}} \Phi_{298}^{\text{o}}$). The potentials were calculated according to the eq. 1 using the corresponding
$\Delta_{\text{ass(g)}} \Phi_{298}^{\text{o}}$ values from Table 4 for the IP formation in the gas phase (g), and the $\Delta_{\text{solv(A)}} \Phi_{298}^{\text{o}}$ data for the
solvation processes from Table 5. Solvation model AI predicts positive values of the $\Delta_{\text{ass(I)}} H_{298}^{\text{o}}$ and
$\Delta_{\text{ass(I)}} G_{298}^{\text{o}}$. The values are similar and are around $200\ \text{kJ·mol}^{-1}$, since the entropic factor is unessential.
Thus, the continuum solvation approach predicts an unphysical behavior: ion association is impossible
for the LiBOB solution in the EC:DMC (7:3) binary solvent at any temperature, because the entropic
contribution is not properly taken into account. Libration of the three EC molecules upon ion association
according to solvation model AII leads to a large positive change in $\Delta_{\text{ass(II)}} S_{298}^{\text{o}}=161.0\ \text{J·mol}^{-1}·\text{K}^{-1}$. The
corresponding $\Delta_{\text{ass(II)}} H_{298}^{\text{o}}$ value is strongly exothermic. As a consequence, the discrete approach predicts
a large negative value of $\Delta_{\text{ass(II)}} G_{298}^{\text{o}}=-184.1\ \text{kJ·mol}^{-1}$: ion dissociation impossible at any temperature.
The corresponding $K_{\text{ass}}$ is around $10^{32}$. That is, the discrete model sharply overestimates the hypothetical
ion association. Such value of $K_{\text{ass}}$ would make the lithium salt with a large anion, like $BOB^-$, totally

insoluble even in the highly polar aprotic solvents. $^{1,9}$ Solvation model AIII produces moderately positive values of all $\Delta_{\text{ass(III)}}\Phi_{298}^{\text{o}}$ potentials. Their absolute values are significantly smaller than the corresponding magnitudes obtained within AI and AII. Substitution of the two EC molecules in the $[\text{Li(EC)}_4]^+$ solvatocomplex by the *in abstracto* non-solvated and continuum polarized $\text{BOB}^-$ anion explains qualitatively the positive $\Delta_{\text{ass(III)}}S_{298}^{\text{o}}$ value. The entropic contribution does not exceed the $\Delta_{\text{ass(III)}}H_{298}^{\text{o}}$ contribution. As a result, the mixed or discrete-continuum approach gives $\Delta_{\text{ass(III)}}G_{298}^{\text{o}}=28.6\ \text{kJ·mol}^{-1}$, corresponding to $K_{\text{ass}}$ on the order of $10^{-5}$. This result allows one to conclude that LiBOB in the EC:DMC (7:3) binary mixture is associated weakly, which is favorable for the LIBs applications. The predictions made in the present work could be verified experimentally by conductometry method or IR/Raman and NMR spectroscopies, as has been achieved previously for $\text{Li}^+$ ion solvation in other solvents. $^{30}$

Table 6. Changes in standard enthalpy ($\Delta_{\text{ass(A)}}H_{298}^{\text{o}}$), entropy ($\Delta_{\text{ass(A)}}S_{298}^{\text{o}}$) and Gibbs free energy ($\Delta_{\text{ass(A)}}G_{298}^{\text{o}}$) during ion association for the LiBOB salt in the EC:DMC (7:3) binary solvent, obtained using the continuum (I), discrete (II) and mixed (III) solvation approaches (A) (g – gas, c – continuum).

<table>
<thead>
<tr>
<th>A</th>
<th>Association process</th>
<th>$\Delta_{\text{ass(A)}}H_{298}^{\text{o}}$,<br>$\text{kJ·mol}^{-1}$</th>
<th>$\Delta_{\text{ass(A)}}S_{298}^{\text{o}}$,<br>$\text{J·mol}^{-1}·\text{K}^{-1}$</th>
<th>$\Delta_{\text{ass(A)}}G_{298}^{\text{o}}$,<br>$\text{kJ·mol}^{-1}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>I</td>
<td>$\text{Li}^{+}_{(\text{c})} + \text{BOB}^{-}_{(\text{c})} = [\text{Li}^{+}\text{BOB}^{-}]_{(\text{c})}$</td>
<td>+187.6</td>
<td>−84.3</td>
<td><b>+212.7</b></td>
</tr>
<tr>
<td>II</td>
<td>$[\text{Li(EC)}_4]^{+}_{(\text{g})} + [\text{BOB(EC)}^C]^{+}_{(\text{g})} = [\text{Li}^{+}(\text{EC})_2\text{BOB}^{-}]_{(\text{g})} + 3\text{EC}_{(\text{g})}$</td>
<td>−136.1</td>
<td>+161.0</td>
<td><b>−184.1</b></td>
</tr>
<tr>
<td>III</td>
<td>$[\text{Li(EC)}_4]^{+}_{(\text{c})} + \text{BOB}^{-}_{(\text{c})} = [\text{Li}^{+}(\text{EC})_2\text{BOB}^{-}]_{(\text{c})} + 2\text{EC}_{(\text{c})}$</td>
<td>+37.1</td>
<td>+28.6</td>
<td><b>+28.6</b></td>
</tr>
</tbody>
</table>

### 4. CONCLUSIONS

In conclusion, we showed that neither continuum nor discrete solvation models are capable of describing ion association of lithium salt in high polar solvent mixtures, and that a combined discrete-continuum (mixed) treatment is required. Using these approaches, we performed quantum-chemical

calculations of the changes in the standard enthalpy, entropy and Gibbs free energy of the ion association process for solution of the LiBOB salt in the EC:DMC (7:3) binary solvent. This is the first theoretical prediction for the solvated $[Li^{+}BOB^{-}]$ IP formation from the solvated $Li^{+}$ and $BOB^{-}$ ions in an EC based solvent mixture. The results show that accurate description of the $Li^{+}$ ion solvation requires both continuum polarization of the solvent medium and binding of the four explicit EC molecules. On the contrary, in solvation of the $BOB^{-}$ anion is dominated polarization by the highly polar structureless solvent continuum. Explicit interaction of polar EC molecules with the $BOB^{-}$ ion is extremely weak. The discrete and continuum contributions to the Gibbs free energy of solvation of the $[Li^{+}BOB^{-}]$ IP are relatively small and are similar. Therefore, both components should be taken into account in order to describe the $[Li^{+}BOB^{-}]$ IP solvation and this can be achieved only with the mixed discrete-continuum model.

Most importantly, the discrete and continuum components to the Gibbs free energies of the ion association process are large and have opposite signs. The continuum approach predicts no association, while the discrete description produces complete association. Both results are unphysical and contradict between themselves. The mixed discrete-continuum model combines both contributions. The resulting Gibbs free energy of ion association is an order of magnitude smaller, predicting reasonably weak association. The conclusions drawn in the current work are particularly important for the selection of novel aprotic electrolyte salt solutions. The mixed discrete-continuum approach resolves the problems in determining the extent of ion association and can be used to screen the properties of a broad range of ion-molecular mixtures for LIBs.

## ACKNOWLEDGMENTS

This work was performed using computational facilities of joint computational cluster of SSI "Institute for Single Crystals" and Institute for Scintillation Materials of National Academy of Science of Ukraine incorporated into Ukrainian National Grid. O.M.K. and O.N.K. acknowledge the Fund of

![](./images/811260243672563716_9.jpg)

Ministry of Education and Science of Ukraine for the financial support (grants No. 0113U002426 and No. 0116U000834). O.V.P. acknowledges support of the US Department of Energy (grant No. DE-SC0014429), and is grateful to the Russian Science Foundation for financial support of the calculations, project No. 14-43-00052, base organization Photochemistry Center RAS.

REFERENCES

1.  Xu, K. Electrolytes and Interphases in Li-Ion Batteries and Beyond. *Chem. Rev.* 2014, 114, 11503–11618.

2.  Schweiger, H.-G.; Wachter, P.; Simbeck, T.; Wudy, F.; Zugmann, S.; Gores, H. J. Multichannel Conductivity Measurement Equipment for Efficient Thermal and Conductive Characterization of Nonaqueous Electrolytes and Ionic Liquids for Lithium Ion Batteries. *J. Chem. Eng. Data* 2010, 55, 1789–1793.

3.  Mennucci, B. Continuum Solvation Models: What Else Can We Learn from Them? *J. Phys. Chem. Lett.* 2010, 1, 1666–1674.

4.  Marenich, A. V.; Ding, W.; Cramer, C. J.; Truhlar, D. G. Resolution of a Challenge for Solvation Modeling: Calculation of Dicarboxylic Acid Dissociation Constants Using Mixed Discrete–Continuum Solvation Models. *J. Phys. Chem. Lett.* 2012, 3, 1437–1442.

5.  Bryantsev, V. S. Calculation of Solvation Free Energies of $Li^+$ and $O^{2-}$ Ions and Neutral Lithium–Oxygen Compounds in Acetonitrile Using Mixed Cluster/Continuum Models. *Theor. Chem. Acc.* 2012, 131, 1–11.

6.  Seo, D. M.; Boyle, P. D.; Borodin, O.; Henderson, W. A. $Li^+$ Cation Coordination by Acetonitrile-Insights from Crystallography. *RSC Advances* 2012, 2, 8014–8019.

7.  Borodin, O.; Olguin, M.; Ganesh, P.; Kent, P. R. C.; Allen, J. L.; Henderson, W. A. Competitive Lithium Solvation of Linear and Cyclic Carbonates from Quantum Chemistry. *Phys. Chem. Chem. Phys.* 2016, 18, 164–175.

8. Larush-Asraf, L.; Biton, M.; Teller, H.; Zinigrad, E.; Aurbach, D. On the Electrochemical and Thermal Behavior of Lithium Bis(Oxalato)Borate (LiBOB) Solutions. *J. Power Sources* **2007**, *174*, 400–407.

9. Xu, K. Nonaqueous Liquid Electrolytes for Lithium-Based Rechargeable Batteries. *Chem. Rev.* **2004**, *104*, 4303–4418.

10. Pliego, J. R.; Riveros, J. M. The Cluster–Continuum Model for the Calculation of the Solvation Free Energy of Ionic Species. *J. Phys. Chem. A* **2001**, *105*, 7241–7247.

11. Cramer, C. J.; Truhlar, D. G. A Universal Approach to Solvation Modeling. *Acc. Chem. Res.* **2008**, *41*, 760–768.

12. Bogle, X.; Vazquez, R.; Greenbaum, S.; Cresce, A. v. W.; Xu, K. Understanding $\text{Li}^{+}$–Solvent Interaction in Nonaqueous Carbonate Electrolytes with $^{17}\text{O}$ NMR. *J. Phys. Chem. Lett.* **2013**, *4*, 1664–1668.

13. Yang, L.; Xiao, A.; Lucht, B. L. Investigation of Solvation in Lithium Ion Battery Electrolytes by NMR Spectroscopy. *J. Mol. Liq.* **2010**, *154*, 131–133.

14. Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Montgomery, J. A.; Vreven, Jr., T.; Kudin, K. N.; Burant, J. C., *et al.* Gaussian 03, Revision E.01; Gaussian, Inc.: Wallingford CT, 2004.

15. Becke, A. D. Density-Functional Thermochemistry. III. The Role of Exact Exchange. *J. Chem. Phys.* **1993**, *98*, 5648–5652.

16. Foresman, J. B.; Keith, T. A.; Wiberg, K. B.; Snoonian, J.; Frisch, M. J. Solvent Effects. 5. Influence of Cavity Shape, Truncation of Electrostatics, and Electron Correlation on *Ab initio* Reaction Field Calculations. *J. Phys. Chem.* **1996**, *100*, 16098–16104.

17. Saito, Y.; Okano, M.; Kubota, K.; Sakai, T.; Fujioka, J.; Kawakami, T. Evaluation of Interactive Effects on the Ionic Conduction Properties of Polymer Gel Electrolytes. *J. Phys. Chem. B* **2012**, *116*, 10089–10097.

18. Brown, C. The Crystal Structure of Ethylene Carbonate. *Acta Cryst.* **1954**, 7, 92–96.

19. Soetens, J.-C.; Millot, C.; Maigret, B.; Bakó, I. Molecular Dynamics Simulation and X-Ray Diffraction Studies of Ethylene Carbonate, Propylene Carbonate and Dimethyl Carbonate in Liquid Phase. *J. Mol. Liq.* **2001**, 92, 201–216.

20. Zavalij, P. Y.; Yang, S.; Whittingham, M. S. Structures of Potassium, Sodium and Lithium Bis(Oxalato)Borate Salts from Powder Diffraction Data. *Acta Cryst. B* **2003**, 59, 753–759.

21. Zavalij, P. Y.; Yang, S.; Whittingham, M. S. Structural Chemistry of New Lithium Bis(Oxalato)Borate Solvates. *Acta Cryst. B* **2004**, 60, 716–724.

22. Xu, K.; Lam, Y.; Zhang, S. S.; Jow, T. R.; Curtis, T. B. Solvation Sheath of $\text{Li}^+$ in Nonaqueous Electrolytes and Its Implication of Graphite/Electrolyte Interface Chemistry. *J. Phys. Chem. C* **2007**, 111, 7411–7421.

23. von Wald Cresce, A.; Borodin, O.; Xu, K. Correlating $\text{Li}^+$ Solvation Sheath Structure with Interphasial Chemistry on Graphite. *J. Phys. Chem. C* **2012**, 116, 26111–26117.

24. Borodin, O.; Smith, G. D. Quantum Chemistry and Molecular Dynamics Simulation Study of Dimethyl Carbonate: Ethylene Carbonate Electrolytes Doped with $\text{LiPF}_6$. *J. Phys. Chem. B* **2009**, 113, 1763–1776.

25. Bhatt, M. D.; Cho, M.; Cho, K. Interaction of $\text{Li}^+$ Ions with Ethylene Carbonate (EC): Density Functional Theory Calculations. *Appl. Surf. Sci.* **2010**, 257, 1463–1468.

26. Li, T.; Balbuena, P. B. Theoretical Studies of Lithium Perchlorate in Ethylene Carbonate, Propylene Carbonate, and Their Mixtures. *J. Electrochem. Soc.* **1999**, 146, 3613–3622.

27. Masia, M.; Probst, M.; Rey, R. Ethylene Carbonate–$\text{Li}^+$: A Theoretical Study of Structural and Vibrational Properties in Gas and Liquid Phases. *J. Phys. Chem. B* **2004**, 108, 2016–2027.

28. Bryantsev, V. S.; Diallo, M. S.; Goddard Iii, W. A. Calculation of Solvation Free Energies of Charged Solutes Using Mixed Cluster/Continuum Models. *J. Phys. Chem. B* **2008**, 112, 9709–9719.


29. Naejus, R.; Lemordant, D.; Coudert, R.; Willmann, P. Excess Thermodynamic Properties of Binary Mixtures Containing Linear or Cyclic Carbonates as Solvents at the Temperatures 298.15 K and 315.15 K. *J. Chem. Thermodyn.* **1997**, *29*, 1503–1515.

30. Yu, Z. X.; Xu, T. T.; Xing, T. F.; Fan, L. Z.; Lian, F.; Qiu, W. H. A Raman Spectroscopy Investigation of the Interactions of LiBOB with $\gamma$-BL as Electrolyte for Advanced Lithium Batteries. *J. Power Sources* **2010**, *195*, 4285–4289.

TOC graphic

![](./images/811260243672563716_10.jpg)