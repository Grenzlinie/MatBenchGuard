# Theoretical Study on Structure Prediction and Molecular Formula Determination of Polymeric Complexes Comprising Fe(II) and 1,2,4-*H*-Triazole Ligand

A. W. Nugraha¹, D. Onggo², and M. A. Martoprawiro²,*

¹Physical Chemistry Division Faculty of Mathematics and Natural Sciences, Universitas Negeri Medan, Medan, 20221 Indonesia
²Inorganic and Physical Chemistry Research Group, Faculty of Mathematics and Natural Sciences, Institut Teknologi Bandung, Bandung, 40132 Indonesia
*e-mail: muhamad.aw@kimiawan.org

Received March 14, 2018; revised August 6, 2018; accepted November 27, 2018

Abstract—The structure and the molecular formula of Fe(II) 1,2,4-*H*-triazole complex has been predicted by using Hartree–Fock (HF) and Density Functional Theory (DFT) methods. The distance between the Fe(II) ions and Fe–N bond length show good agreement with experimental measurements at the low-spin state. It has been conducted by using hybrid/basis set functions of B3LYP/6-31G(d), TPSSh/TZVP, and MO6-2x/6-31G(d). The distance between the Fe(II) ions complexes with deprotonated ligands are 3.30–3.75, 3.44–3.74, and 3.46–3.79 Å, respectively, and undeprotonated ligands are 3.41–4.04, 3.49–3.90, and 3.52–4.09 Å. Meanwhile, the Fe–N bond lengths in the complex with the deprotonated ligand are 1.84–2.07, 1.85–2.04, and 1.89–2.11 Å, respectively, while in the complex with undeprotonated ligands they are 1.89–2.20, 1.84–2.12, and 1.96–2.21 Å. The molecular formula of Fe(II)-Htrz complex is $([\text{Fe(Htrz)}_2(\text{trz})]^+)_n$ which has been obtained by comparing the energy difference between the complex formation with deprotonated ligands being lower than that with undeprotonated complex. The computational results on the hybrid/basis set function of B3LYP/6-31G(d) induces the difference of energy formation of $[\text{Fe}_2(\text{Htrz})_4(\text{trz})_2]^{2+}$, $[\text{Fe}_2(\text{Htrz})_6]^{4+}$, $[\text{Fe}_4(\text{Htrz})_8(\text{trz})_4]^{4+}$, $[\text{Fe}_4(\text{Htrz})_{12}]^{8+}$, $[\text{Fe}_6(\text{Htrz})_{12}(\text{trz})_6]^{6+}$, and $[\text{Fe}_6(\text{Htrz})_{18}]^{12+}$ complexes to be $-$5613.38, $-$3082.67, $-$11013.19, $-$147.40, $-$16101.36, and $-$6825.09 kJ/mol, respectively.

Keywords: computational chemistry, iron(II) 1,2,4-triazole complex, energy, stability, structure, deprotonated, and undeprotonated

DOI: 10.1134/S0036023619060123

## INTRODUCTION

The complex of iron(II) with 1,2,4-*H*-triazole (Htrz) ligand is a compound having spin transition (ST) characteristics. The experimental observations at room temperature of iron(II) with Htrz (Fe(II)-Htrz) complex induce a light purple (lilac) and diamagnetic, and by increasing the temperatures, the complex becomes colorless and paramagnetic. This characteristic change which reversible in around room temperature was affected by the anion type and the number of water. The ST phenomenon is the transfer of electrons between the $t_{2\text{g}}$ and $e_{\text{g}}$ orbitals in the octahedral complex compounds. The octahedral complex containing a central iron(II) ion with the d⁶ configuration consist in two different electronic states as low-spin (LS) and high-spin (HS). In the intermediate ligand field, the energy difference between the two spin states is small due to their external influences such as temperature change, pressure, and light induction induces a change the state of LS state into HS state or vice versa [1].

The most of ST properties was observed through temperature changes to magnetic susceptibility changes. The relationship curves between the magnetic susceptibility change and the temperature change is called the ST pattern. This ST pattern illustrates the change in the LS state to a HS state due to the influence of temperature changes. There are several types of ST patterns, which are gradual, incomplete, two-step, abrupt, and abrupt with hysteresis [1]. Materials with LS states changes to HS states in a very narrow range could be used as switches, whereas spin state changes in heating and cooling modes which occur at different temperatures can be used as data storage [2, 3].

Since the single crystal of Fe(II)-Htrz complex not established yet, so the study of complex structures was observed using various methods. The complex structure of $[\text{Fe(Htrz)}_2(\text{trz})](\text{BF}_4)$ and $[\text{Fe(Htrz)}_3](\text{BF}_4)_2 \cdot \text{H}_2\text{O}$ were determined by using EXAFS and X-ray Powder Diffraction (XRPD) at transition state. This EXAFS data

![](./images/812758086602194944_1.jpg)

Fig. 1. Schematic structure of polymeric complex Fe(II)-Htrz.

corresponds to the linear chain structure of both of compounds, in Fe(Htrz)₃ chromophores which are linked to each nitrogen at 1–2 position of the three triazole ligands. The stoichiometric of [Fe(Htrz)₂(trz)](BF₄) has a regular deprotonated ligand on each of the Fe(Htrz)₂(trz)Fe [4]. [Fe(Htrz)₂(trz)](BF₄) and [Fe(NH₂trz)₃](NO₃)₂ complexes in LS and HS was measured with Wide-Angle X-ray Scattering (WAXS). The results shows both of the compounds as a polymeric chain structure which each Fe(II) ion bound to three bridges with Fe(II) ions through Nitrogen atom of the Htrz or trz⁻¹ group. In the LS state, the complex has a linear polymer chain, whereas in HS state indicate elongation and deformation of the chain in lead to the chain loses linear characters [5]. The other studies used SEM and XRPD to determine the structure variables of the [Fe(NH₂trz)₃](NO₃)₂ and [Cu(NH₂trz)₃](NO₃)₂ H₂O complexes. Based on XRD analysis of single crystals of [Cu(NH₂trz)₃](NO₃)₂ H₂O complex, induce the complex has a polymeric structure associated with three Htrz ligands as bridges. The XRPD analysis in both of complexes show similar diffraction patterns, that lead to the two complexes have the same structure [6]. Determination of structure crystal of [Fe(Htrz)₂(trz)]BF₄ complex use the XRPD and Raman Spectroscopy on the LS and HS state. It observes the complex has a 1D linear polymeric structure. The Fe(II) ions are in an octahedral environment bound to six Htrz ligands, between Fe(II) ions linked by three N(1)–N(2) bridges [7, 8]. The scheme structure of Fe(II)-Htrz complex is presented in Fig. 1.

The computational studies on the Fe(II)-Htrz complex using molecular formula is [Fe(Htrz)₃]²⁺ [9, 10]. Sugiyarto and Goodwin [11] have performed elemental analysis of Fe(II)-Htrz complex which indicate that the complex molecular formula is [Fe(Htrz)₂trz]⁺¹. Another study observed on the ratio of the Raman spectra of Fe(II)-Htrz complex experimentally with the computational Raman spectra for Htrz and trz⁻¹ ligands. The comparison results show the spectra for the complex in LS and HS state corresponds to the Raman spectra peak for Htrz and trz⁻¹ computationally simulated results. It indicates the complex have Htrz and trz⁻¹ ligands with a ratio 2 : 1 [7]. Other studies use the molecular formula of [Fe(Htrz)₃]²⁺ and [Fe(Htrz)₂trz]⁺¹ to defining the ST characteristics complex [4, 12].

The computational studies of ST characteristics of iron(II) complex was reported previously. Kitchen et al. [13] examined the ST characteristic of the Htrz-derived complex which is an one-core complex binding three ligands [Fe(Rdpt)₃]-(BF₄) to form FeN₆, where Rdpt is (N-4-3,5-di(2-pyridyl)-1,2,4-triazole). The signal of computational calculation with B3LYP/6-311G(d,p)//B3LYP/6-311+G (2d,p) was compared with ¹⁵N NMR spectral signal experimentally. The comparison of ¹⁵N measurement data gives similar results of N^pir and N⁴ but for N¹ is more distorted. Wolny et al. [14] also measured the complex vibrational properties of [Fe₃(4-(2'-hydroxy-ethyl)-1,2,4-triazole)₆] (CF₃SO₃)₆ which is a three-core complex using nuclear inelastic scattering spectroscopy of synchrotron radiation (NIS). The results explain the complex formed had ST properties on Fe(II) ion with FeN₆ framework while on the terminal side had FeN₃O₃ framework which did not show ST characteristic. The characteristic of the experimental Fe–N vibration modes observed experimentally similar to theoretical calculations using the B3LYP/CEP-31G hybrid/ basis set function. The computational study of ST characteristics has been performed on the intermediate core Fe(II) complexes and the three-core complexes, in which we study the ST characteristic for complexes about polymeric structures.

The study of a structure using WAXS and molecular modeling using CERIUS2 software was determined on [Fe(Htrz)₂(trz)](BF₄) and [Fe(NH₂trz)₃](NO₃)₂ complexes for the LS and HS state. In the LS state, the complex of [Fe (Htrz)₂(trz)](BF₄) have distance of Fe–Fe amounted to 3.63 Å and bond length of Fe–N at a 1.99 Å, whereas the compound [Fe(NH₂trz)₃](NO₃)₂ shows distance of Fe–Fe amounted to 3.65 Å and bond length of Fe–N at 2.01 Å [5]. The computational studies were used to predict the structure and determine the stability

![](./images/812758086602194944_2.jpg)

Fig. 2. Model of the polymeric structure of Fe(II)-Htrz.

of the complex $[Fe_{4}(Htrz)_{8}(trz)_{4}]^{4+}$ and $[Fe_{4}(Htrz)_{12}]^{8+}$.
The computational studies using HF, B3LYP, and
TPSSh with the 3-21G, 6-31G(d), and TZVP hybrid/
basis set functions. It showed the structure data of
Fe(II)-Htrz complex similar to Cu(II)-Htrz complex
and the $[Fe_{4}(Htrz)_{8}(trz)_{4}]^{4+}$ complexes were more sta-
ble than the $[Fe_{4}(Htrz)_{12}]^{8+}$ complex [15].

The computational approach is an alternative to
predicting the structure and determining the complex
molecular formula for Fe(II)-Htrz complex. Based on
the structure of the simulation results can be deter-
mined the data onto complex structures. The complex
molecular formula was determined by comparison of
differences in energy formation of iron(II) complexes
about undeprotonated ligand (Htrz) and deprotonated
ligand $(trz^{-1})$.

The computational studies using the B3LYP
method was used to determine the structure, energy of
formation, structural stability, energy splitting
LS/HS, and spin transition to some compounds that
give results that are in accordance with the experimen-
tal data [16-21]. Determination of structure, vibration
frequency, energy in some compounds using basis sets
3-21G, 3-21G(d), and 6-31G(d) good agreement with
experimental data [22-26]. Theoretical study of the
geometric parameters, energies, thermodynamics
parameters, and stability was examined for some com-
plexes using DFT method with B3LYP, OPBE and
6-31G(d), 6-31G, 6-311+G*, dan TZVP hybrid/ basis
set function [27-31].

Geometry optimization with B3LYP, HF, and
MP2 hybrid functions on a 6-311G basis set is compat-
ible with the bond length data and bond angles of
XRD study results on compound of 4-amino-1,2,4-
triazole molecule (4-at) and 4-amino-1,2,4-triazol-1-
ium cation (4-at(1+)) [32]. A comparison results of the
experimental measurements with X-ray on the 3-phe-
nylamino-4-phenyl-1,2,4-triazole-5-thione com-
pound using B3LYP/6-311G** showed the largest dif-
ference in the bond length C(9)-C(10) is $0.0431\ \mathring{A}$
and the bond angles C(14)-N(1)-C(6) is $2.0576^{\circ}$,
while the results in PBE1PBE/ 6-31G** indicates the
difference of bond length is $0.0394\ \mathring{A}$ and the bond
angles is $1.8431^{\circ}$. The computational determination by
using the PBE1PBE and B3LYP methods approached
the experimental measurement results [33].

## COMPUTATIONAL DETAILS

Computational calculations used Gaussian 09
Revision D.01 [34], visualization of the results of cal-
culations used Jmol [35] and Avogadro [36]. This
computational study used exchange-correlation func-
tional of UHF, B3LYP [37, 38], MO6-2x, and TPSSh
with basis set of 3-21G, 6-31G(d), 6-31G(d,p), and
TZVP to find the optimized structure and stability of
the complex.

The preparation of input in computational for
complex calculations by using a polymeric structure of
modeling in the form of the model fragments. The
shortest fragment model consists two ions of Fe(II)
and six ligands Htrz called the fragment model of A1.
Addition of fragment length performs by adding two
Fe(II) ion and six ligand fragment Htrz forming A2
and A3 models are presented in Fig. 2.

The computationally prediction of Fe(II)-Htrz
complex structure was examined by geometric optimi-
zation on hybrid/ basis set function B3LYP/6-31G(d)
to obtain the most stable structure. Bond angle and
bond length measurements were performed on the
complex structure of the visualization results. The data
structure parameters of the computational results was
compared with the experimental data of Fe(II)-Htrz
complex. The Fe(II)-Htrz complexes were modeled as
fragments of A1, A2, and A3 with the deprotonated
and undeprotonated ligand, i.e. $[Fe_{2}(Htrz)_{4}(trz)_{2}]^{2+}$,
$[Fe_{2}(Htrz)_{6}]^{4+}$, $[Fe_{4}(Htrz)_{8}(trz)_{4}]^{4+}$, $[Fe_{4}(Htrz)_{12}]^{8+}$,
$[Fe_{6}(Htrz)_{12}(trz)_{6}]^{6+}$, and $[Fe_{6}(Htrz)_{18}]^{12+}$ complexes.

Table 1. The optimized geometry structures of $([Fe(Htrz)_2(trz)]^+)_n$ and $([Fe(Htrz)_3]^{2+})_n$

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>$([Fe(Htrz)_2(trz)]^+)_n$</th>
      <th>$([Fe(Htrz)_3]^{2+})_n$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A1</td>
      <td>![](./images/812758086602194944_3.jpg)</td>
      <td>![](./images/812758086602194944_4.jpg)</td>
    </tr>
    <tr>
      <td>A2</td>
      <td>![](./images/812758086602194944_5.jpg)</td>
      <td>![](./images/812758086602194944_6.jpg)</td>
    </tr>
    <tr>
      <td>A3</td>
      <td>![](./images/812758086602194944_7.jpg)</td>
      <td>![](./images/812758086602194944_8.jpg)</td>
    </tr>
  </tbody>
</table>

The chemical formula of complex corresponding was determined through the comparison of complex stability based on both of the molecular formula prediction. Stability of the complex was determined by the magnitude of the difference of energy in forming iron(II) with Htrz ligand in the oligomers form. $E_{\text{stability}} = E_{\text{oligomer}} - (E_{\text{Fe ion}} + E_{\text{ligan}})$. The molecular formula of complex examine on complex with a deprotonated ligand with the general formula of $([Fe(Htrz)_2(trz)]^+)_n$, such as: $[Fe_2(Htrz)_4(trz)_2]^{2+}$, $[Fe_4(Htrz)_8(trz)_4]^{4+}$, and $[Fe_6(Htrz)_{12}(trz)_6]^{6+}$ complexes. Otherwise, other complexes which are undeprotonated ligand with the general formula of $([Fe(Htrz)_3]^{2+})_n$, such as $[Fe_2(Htrz)_6]^{4+}$, $[Fe_4(Htrz)_{12}]^{8+}$, and $[Fe_6(Htrz)_{18}]^{12+}$ complexes. The comparison of the complex stability was used with hybrid and basis set functions of UHF/3-21G, UHF/6-31G(d), B3LYP/3-21G, B3LYP/6-31G(d), B3LYP/6-31G(d,p), M06-2x/6-31G(d), and TPSSh/TZVP. The sequence of hybrid/basis set function is described the sequence of computational chemistry calculation accuracy.

## RESULTS AND DISCUSSION
### Prediction of Complex Structures

Based on the proposed model, the computational calculations were performed on fragment models A1, A2, and A3. The most stable complex structure was determined by the geometry optimization by using B3LYP/6-31G(d) hybrid/basis set function. The geometric optimization results shows the Fe(II)-Htrz complex induce a polymeric structure and between Fe(II) ions was connected by three Htrz ligand rings. The Fe(II) ion was observed in octahedral environment by binding six N atoms of the Htrz ligand. The computational calculations were performed on complexes with deprotonated and undeprotonated ligands. The computational calculation result shows the model A1 contain two N atoms are deprotonated, the fragment model A2 have four deprotonated N atoms, whereas the fragment model A3 have six deprotonated N atom. Visualization of complex structures of $[Fe_2(Htrz)_4(trz)_2]^{2+}$, $[Fe_2(Htrz)_6]^{4+}$, $[Fe_4(Htrz)_8(trz)_4]^{4+}$, $[Fe_4(Htrz)_{12}]^{8+}$, $[Fe_6(Htrz)_{12}(trz)_6]^{6+}$, and $[Fe_6(Htrz)_{18}]^{12+}$ are presented in Table 1.

Parameters of the complex structure of Fe(II)-Htrz were examined to measure the distance between

Table 2. Distance between the Fe(II) ions the results of the geometry optimization

<table>
<thead>
<tr>
<th rowspan="2">Hybrid/basis set functions</th>
<th rowspan="2">Model</th>
<th colspan="2">Distance between ions Fe(II) in Å</th>
</tr>
<tr>
<th>$([Fe(Htrz)_2(trz)]^+)_n$</th>
<th>$([Fe(Htrz)_3]^{2+})_n$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">B3LYP/6-31G(d)</td>
<td>A1</td>
<td>3.30</td>
<td>3.41</td>
</tr>
<tr>
<td>A2</td>
<td>3.47–3.69</td>
<td>3.61–3.84</td>
</tr>
<tr>
<td>A3</td>
<td>3.49–3.75</td>
<td>3.67–4.04</td>
</tr>
<tr>
<td rowspan="3">TPSSh/TZVP</td>
<td>A1</td>
<td>3.44</td>
<td>3.49</td>
</tr>
<tr>
<td>A2</td>
<td>3.48–3.69</td>
<td>3.62–3.84</td>
</tr>
<tr>
<td>A3</td>
<td>3.51–3.74</td>
<td>3.59–3.90</td>
</tr>
<tr>
<td rowspan="3">MO6-2x/ 6-31G(d)</td>
<td>A1</td>
<td>3.46</td>
<td>3.52</td>
</tr>
<tr>
<td>A2</td>
<td>3.51–3.73</td>
<td>3.65–3.89</td>
</tr>
<tr>
<td>A3</td>
<td>3.54–3.79</td>
<td>3.70–4.09</td>
</tr>
</tbody>
</table>

Table 3. The bond length of Fe—N from geometry optimization results

<table>
<thead>
<tr>
<th rowspan="3">Hybrid/ basis set functions</th>
<th rowspan="3">Model</th>
<th colspan="3">The bond length of Fe—N in Å</th>
</tr>
<tr>
<th colspan="2">$([Fe(Htrz)_2(trz)]^+)_n$</th>
<th rowspan="2">$([Fe(Htrz)_3]^{2+})_n$</th>
</tr>
<tr>
<td>deprotonated ring</td>
<td>undeprotonated ring</td>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">B3LYP/6-31G(d)</td>
<td>A2</td>
<td>1.84–2.02</td>
<td>1.89–2.04</td>
<td>1.89–2.05</td>
</tr>
<tr>
<td>A3</td>
<td>1.85–2.01</td>
<td>1.90–2.07</td>
<td>1.89–2.20</td>
</tr>
<tr>
<td rowspan="2">TPSSh/ TZVP</td>
<td>A2</td>
<td>1.85–2.00</td>
<td>1.91–2.02</td>
<td>1.89–2.12</td>
</tr>
<tr>
<td>A3</td>
<td>1.86–2.00</td>
<td>1.91–2.04</td>
<td>1.84–2.09</td>
</tr>
<tr>
<td rowspan="2">MO6-2x 6-31G(d)</td>
<td>A2</td>
<td>1.89–2.04</td>
<td>1.96–2.09</td>
<td>1.96–2.16</td>
</tr>
<tr>
<td>A3</td>
<td>2.02–2.04</td>
<td>1.97–2.11</td>
<td>1.96–2.21</td>
</tr>
</tbody>
</table>

Fe(II) ions and bond length of Fe—N. A selection of these parameters based on a consideration that both of parameters have changed significantly in the event of electronic state changes in Fe(II) ion. Observation of the structures shows the distance between the Fe(II) ions on the deprotonated complex is shorter than the undeprotonated complex. The distance between the Fe(II) ions were generated from the geometry optimi- zation with hybrid/ basis set function of B3LYP/6-31G(d), TPSSh/TZVP, and MO6-2x/6-31G(d) for the complexes with a deprotonated ligand are 3.30–3.75, 3.44–3.74, and 3.46–3.79 Å respectively and complexes with undeprotonated ligands are 3.41–4.04 3.49–3.90 and 3.52–4.09 Å. XRPD measurements result shows the distance between the Fe(II) ions in the LS state at the $[Fe(Htrz)_2(trz)]BF_4$ is 3.671(1) Å and the HS states is 3.891(1) Å [7]. Data from computational calculations on fragments A1 is much smaller than the experimental data, but the data was obtained from the fragment model A2 and A3 has a correspond range to experimental data. These data indicate the model A1 is not accurate while model A2 and A3 correspond to the experimental data. Otherwise, the results of the computational calculations by using hybrid/basis set functions of TPSSh/TZVP and MO6-2x/6-31G(d) shows the similar distance between the Fe(II) ions. The distance between Fe(II) ions complex of deprotonated and undeprotonated complex on the model fragment A1, A2, and A3 are presented in Table 2.

The bond length of Fe—N in the deprotonated complex is shorter than the undeprotonated complex. In deprotonated complex, the bond length of Fe—N with ring deprotonated shorter than the bond length of Fe—N with undeprotonated ring. These results induces the deprotonated ligand ring with Fe(II) ion bound more strongly than the undeprotonated ring. These facts indicate the deprotonated ligand rings cause the formed complex to be more stable than the complex with undeprotonated ligands. The computational results on the hybrid/ basis set function of B3LYP/6-31G(d), TPSSh/TZVP, and MO6-2x/6-31G(d) induces the bond lengths of Fe—N on the complexes with deprotonated ligands are 1.84–2.07, 1.85–2.04, and 1.89–2.11 Å respectively and the complexes with undeprotonated ligand are 1.89–2.20, 1.84–2.12, and 1.96–2.21 Å. The experimentally measurement results of Fe—N bond length on the low-spin state is 1.827(5)—1.981(6) Å and the high-spin state is 2.04(2)—2.042(5) Å [7]. The bond length of Fe—N at deprotonated and undeprotonated complexes are presented in Table 3.

![](./images/812758086602194944_9.jpg)

Fig. 3. Determination of energy changes of (a) model A2 and (b) model A3 on the various hybrid and basis set functions: A = UHF/3-21G, B = UHF/6-31G(d), C = B3LYP/3-21 G, D = B3LYP/6-31G(d), E = B3LYP/6-31G(d,p), F = MO6-2x/6-31G(d), G = TPSSh/TZVP.

### Determination of Molecular Formula of Complex

The molecular formula of polymeric complex of Fe(II)-Htrz was determined computationally using the hybrid functions UHF, B3LYP, MO6-2x, and TPSSh. The hybrid function used could be categorized into low level theory as UHF function while high level theories are B3LYP, MO6-2x, and TPSSh hybrid functions. The computational results shows the energy changes obtained from the calculations in the low level theory are inconsistent compared to the calculations in the high level theory, but there are deviations on the calculation results for complex $[Fe_6(Htrz)_{18}]^{12+}$ with hybrid/ basis set function B3LYP/6-31G (d). The order of the level of accuracy basis set functions are used 3-21G, 6-31G(d), 6-31G(d,p), and TZVP. The result of computational calculation shows the changes of energy complex formation $[Fe_4(Htrz)_8(trz)_4]^{4+}$ is smaller than the complex $[Fe_4(Htrz)_{12}]^{8+}$ in all hybrid and basis set functions. In model A3, the changes of energy complex formation $[Fe_6(Htrz)_{12}(trz)_6]^{6+}$ is smaller than the complex $[Fe_6(Htrz)_{18}]^{12+}$ in all hybrid and basis set functions. It shows the deprotonated complexes are more stable than the undeprotonated complexes. The energy differences of the $[Fe_4(Htrz)_8(trz)_4]^{4+}$ $[Fe_4(Htrz)_{12}]^{8+}$, $[Fe_6(Htrz)_{12}(trz)_6]^{6+}$, and $[Fe_6(Htrz)_{18}]^{12+}$ complexes from the calculation result of the various hybrid and the basis set functions are presented in Fig. 3.

The result of the determination of differences energy on the model A2 and A3 shows the deprotonated complex is more stable than the undeprotonated complex, which lead to the molecular formula of Fe(II)-Htrz complex is $([Fe(Htrz)_2trz]^+)_n$. Their consistency energy differences formation of complex for all the hybrid / basis set functions shows the molecular formula of Fe(II)-Htrz complex was quite determined by using the low-cost method and basis set function as UHF/3-21G. The consistency of the calculation result of computing the hybrid/ basis set functions are MO6-2x/6-31G(d) and TPSSh/TZVP shows the calculation was stable if determined using the high-cost hybrid/basis set function.

### CONCLUSION

Based on the results of geometry optimization on the hybrid /basis set function of B3LYP/6-31G(d) was obtained shows the Fe(II)-Htrz complex induce as a polymeric structure and between Fe(II) ions was connected by three Htrz ligand rings. Determination of the energy complex computationally shows the Fe(II)-Htrz with one deprotonated ligand complex is more stable compared than the undeprotonated ligand which lead to the appropriate molecular formula of $([Fe(Htrz)_2trz]^+)_n$. The computational calculations on the various hybrid/basis set functions and model A2 and A3 indicates the consistent results due to the comparative stability of the Fe(II)-Htrz complex on both of molecular formula.

### ACKNOWLEDGEMENTS

This work was supported by Directorate General of Higher Education, The Ministry of Research, Technology and Higher Education the Republic of Indonesia by the Doctoral Dissertation Research Grant (project no. 064/SP2H/PL/Dit.litabmas/II/2015).

### REFERENCES

1. P. Gütlich and H. A. Goodwin, Top. Curr. Chem. **233**, 1 (2004).
2. O. Kahn, J. Kröber, and C. Jay, Adv. Mater. **4**, 718 (1992).
3. O. Kahn and C. J. Martinez, Science, **279** (44), 44 (1998).


4. A. Michalalowicz, J. Moscovici, B. Ducourant, et al., Chem. Mater. 7, 1833 (1995).

5. M. Verelst, L. Sommier, P. Lecante, et al., Chem. Mater. 10, 980 (1998).

6. M. M. Dirtu, C. Neuhausen, A. D. Naik, et al., Inorg. Chem. 49, 5723 (2010).

7. A. Urakawa, W. V. Beek, M. M. Capilla, et al., J. Phys. Chem. C 115, 1323 (2011).

8. M. C. Muñoz and J. A. Real, in Spin-Crossover Materi- als Properties and Applications, John Wiley & Sons, Ltd., Chichester, Ed. by M. A. Halcrow (2013), p. 121.

9. L. G. Lavrenova, O. G. Shakirova, V. N. Ikorskii, et al., Russ. J. Coord. Chem. 29, 22 (2003).

10. A. Nakamoto, N. Kojima, L. XiaoJun, et al., Polyhe- dron 24, 2909 (2005).

11. K. H. Sugiyarto and H. A. Goodwin, Aust J. Chem. 47, 263 (1994).

12. J. Kröber, J. Audière, R. Claude, et al., Chem. Mater. 6, 1404 (1994).

13. J. A. Kitchen, N. G. White, M. Boyd, et al., Inorg. Chem. 48, 6670 (2009).

14. J. A. Wolny, H. Paulsen, A. X. Trautwein, et al., Coord. Chem. Rev, 253, 2423 (2009).

15. A. W. Nugraha, D. Onggo, and M. A. Martoprawiro, Proc. Chem, 17, 9 (2015).

16. A. G. Baboul, L. A. Curtiss, P. C. Redfern, et al., J. Chem. Phys. 110, 7650 (1999).

17. Z. X. Chen, J. M. Xiao, H. M. Xiao, et al., J. Phys. Chem. A 103, 8062 (1999).

18. H. Furuta, H. Maeda, and A. Osuka, J. Org. Chem. 65, 4222 (2000).

19. M. Malagoli and J. L. Bredas, Chem. Phys. Lett. 327, 13 (2000).

20. S. Zein, G. S. Matouzenko, and S. A. Borshch, Chem. Phys. Lett. 397, 475 (2004).

21. A. Slimani, X. Yu, A. Muraoka, et al., J. Phys. Chem. A 118, 9005 (2014).

22. J. S. Binkley, J. A. Pople, and W. J. Hehre, J. Am. Chem. Soc. 102, 939 (1980).

23. W. J. Pietro, M. M. Francl, W. J. Hehre, et al., J. Am. Chem. Soc. 104, 5039 (1982).

24. M. S. Gordon, J. S. Binkley, J. A. Pople, et al., J. Am. Chem. Soc. 104, 2797 (1982).

25. P. v. R. Schleyer, T. Clark, A. J. Kos, et al., J. Am. Chem. Soc. 106, 6468 (1984).

26. B. Sosa, J. Andzelm, B. C. Elkin, et al., J. Phys. Chem. 96, 6630 (1992).

27. C. V. Chachkov and O. V. Mikhailov, Russ. J. Inorg. Chem. 54, 1952 (2009).

28. O. V. Mikhailov and D. V. Chachkov, Russ. J. Inorg. Chem. 60, 187 (2015).

29. D. V. Chachkov and O. V. Mikhailov, Russ. J. Inorg. Chem. 57, 205 (2012).

30. E. V. Chachkov and O. V. Mikhailov, Russ. J. Inorg. Chem. 59, 489 (2014).

31. O. P. Charkin, N. M. Klimenko, D. O. Charkin, et al., Russ. J. Inorg. Chem. 52, 1248 (2007)

32. I. Matulkova, I. Nemec, K. Teubner, et al., J. Mol. Struct. 873, 46 (2008).

33. H. Y. Wang, P. S. Zhao, R. Q. Li, et al., Molecules, 14, 608 (2009).

34. M. J. Frisch et al., GAUSSIAN 09 Revision D.01 (Gaussian, Wallingford CT, 2013).

35. Jmol: An Open-Source Java Viewer for Chemical Structures in 3D. http://www.jmol.org/

36. M. D. Hanwell, D. E. Curtis, D. C. Lonie, et al., Avo- gadro, J. Cheminformatics 4 (17) (2012).

37. P. J. Stephens, F. J. Devlin, C. S. Ashvar, et al., Faraday Discuss. 99, 103 (1994).

38. D. Becke, J. Chem. Phys. 98, 5648 (1993).

RUSSIAN JOURNAL OF INORGANIC CHEMISTRY Vol. 64 No. 6 2019