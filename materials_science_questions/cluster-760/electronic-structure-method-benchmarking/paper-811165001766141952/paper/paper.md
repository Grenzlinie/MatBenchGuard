# A theoretical study of the structures and electronic transitions of small silicon nitride clusters (SiₙNₘ, n + m ≤ 4)

E. Owusu-Ansah, Y.M. Wang¹, Y.J. Shi *

Department of Chemistry, University of Calgary, Calgary, Alberta T2N 1N4, Canada

---

## ARTICLE INFO

**Article history:**
Received 12 May 2016
In revised form 16 July 2016
Accepted 5 August 2016
Available online xxxx

**Keywords:**
Silicon nitride clusters
Global minimum
Electronic transitions
Ab initio calculations
Density functional theory

---

## ABSTRACT

A quantum mechanical study of small silicon nitride clusters (SiₙNₘ, n + m ≤ 4) was performed for both the ground and excited electronic states. The diatomic SiN as well as the tri-atomic SiN₂ and Si₂N clusters were chosen as our benchmark systems for an extensive investigation of the various methods, functionals and basis sets. Among the methods investigated for the ground-state geometry optimization and vibrational frequency calculations, density functional theory (DFT) with the B3LYP functional was found to be the best performed method overall. For the basis set, 6-311G(d) is chosen for its nice balance between accuracy and efficiency in time. At the B3LYP/6-311G(d) level of theory, the most stable isomers of SiN₂, Si₂N, SiN₃, Si₃N and Si₂N₂, were determined to be the triplet ($^3\Sigma^-$) asymmetric linear isomer (Si-N=N), the doublet ($^2\Pi_g$) symmetric linear isomer (Si=N=Si), the doublet ($^2A'$) nonlinear isomer (Si=N-N=N), the doublet ($^2B_1$) Y-type isomer, and the singlet ($^1\Sigma_g^+$) symmetric linear isomer (Si=N=N=Si), respectively. Analysis of the relative energies of various stable isomers shows that N-N bonding is the most favored one and Si-Si bonding is least favored. Due to its good performance in predicting the electronic transitions from the $X^2\Sigma^+$ ground state of SiN to three low-lying excited states $A^2\Pi, B^2\Sigma^+$, and $D^2\Pi$, TDDFT/B3LYP/6-311G(d) was chosen over EOMCCSD/6-311G(d) for the excited state calculations. The first ten electronic transitions for the most stable isomers of all SiₙNₘ (n + m ≤ 4) clusters were calculated.

© 2016 Elsevier Inc. All rights reserved.

---

## 1. Introduction

Silicon nitrides have unique properties such as chemical inertness, good resistance to wear and corrosion, strength, hardness, good dielectric properties, and thermal stability. This makes them highly sought after for applications in harsh environments, for example, abrasive and cutting tools, components of heat engines and furnaces, braking bands in automobiles, as well as diffusion barriers in microchips [1-3]. The increasing applications of silicon nitrides have created a lot of interest in the structure and bonding of their building blocks, i.e., the small heteroatomic clusters [4,5]. The bonding, structures, and relative stability of isomers vary greatly with the cluster size and stoichiometry [6,7]. The structural, mechanical and electronic properties of the bulk silicon nitride depend on the local atomic-level bonding in the bulk materials [8,9]. For example, Valentin and co-workers have found that the charge trapping behavior of bulk Si₃N₄ originates from the Si-Si bonds or tiny Si clusters formed inside the material [8]. An atomic-level study of the structure of small silicon nitride clusters could ultimately lead to a better understanding of the properties of the bulk materials which could help realize other latent applications. It also helps understand the initial stage in the growth of silicon nitride materials by chemical vapor deposition (CVD) and pulsed laser deposition (PLD) [10-13].

Small clusters of gaseous silicon nitride, SiₙNₘ (n + m ≤ 4), have been investigated by several experimental [4,14-16] and theoretical [5,17-19] research groups in order to understand their structure and bonding in both the ground and excited electronic states. A detailed spectroscopic information is important for the characterization and diagnostic of these species which helps the optimization of experimental conditions in the process of CVD [10,13] and PLD [11,12] of silicon nitride thin films. It may also have a direct impact on astrophysical studies since some silicon nitride clusters, for example, SiN and Si₃N₄, have been observed as components of interstellar medium [20-23].

There are a lot of theoretical studies on the diatomic SiN species. The first ab initio study was performed by Bruna et al. [24] who used the multi-reference single and double-excitation configuration interaction (MRDCI) to determine the equilibrium

---

* Corresponding author.
E-mail address: shiy@ucalgary.ca (Y.J. Shi).
¹ Current address: Department of Chemistry, University of Michigan, Ann Arbor, MI, USA.

http://dx.doi.org/10.1016/j.jms.2016.08.005
0022-2852/© 2016 Elsevier Inc. All rights reserved.

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005

geometries and transition energy $(T_e)$ values for three low-lying excited states. Cai et al. [25] used the coupled cluster method with single, double and triple excitations (CCSD(T)) together with Dun- ning's correlation-consistent basis sets (cc-pVDZ) to obtain the val- ues of $1.5733 \AA, 1150 ~cm^{-1}, 6.49 ~cm^{-1}$ and $0.72927 ~cm^{-1}$ , respectively, for the equilibrium internuclear distance $(r_{e})$ , har monic frequency $(\omega_{e})$ , anharmonic constant $(\omega_{e} x_{e})$ , and the equi librium rotational constant $(B_{e})$ , in the $X^{2} \Sigma^{+}$ ground state of SiN. These values agreed well with the experimental values of $1.5719 \AA, 1151.36 ~cm^{-1}, 6.47 ~cm^{-1}$ and $0.7311 ~cm^{-1}$ , respectively, reported by Saito et al. [26].

Similarly, the tri-atomic clusters, $SiN_{2}$ and $Si_{2} ~N$ , have beenexplored by both experimental and theoretical methods. $SiN_{2}$  trapped in various matrices at $4 ~K$ was first identified by Lembke et al. [27] through electron spin resonance (ESR). In that study, the ESR spectra recorded in neon, argon, and nitrogen matrices showed quite distinct features which were indicative of a linearelectronic structure, SiNN, in the argon matrix, and a bent $C_{2 v}$  structure in the nitrogen matrix. A computational study by Ornel- las et al. [28] at the CCSD(T)/cc-pVTZ level showed that the asym- metric linear (SiNN) triplet $(^{3} \Sigma^{-})$ structure was the global minimum. The other four local minima, i.e., the symmetric bent singlet $(^{1} A_{1})$ , symmetric linear triplet $(^{3} \Sigma_{g}^{-})$ , asymmetric linear sin glet $(^{1} \Sigma^{-})$ , and cyclic singlet $(^{1} A_{1})$ structures were found to lie higher in energy by $102.23,84.60,15.81$ , and $6.09 kcal / mol$ , respec tively, relative to the global minimum.

The $Si_{2} ~N$ cluster was first observed by Zmbov and Margrave [29] through mass spectrometry by vaporizing pure $Si$ inside a boron nitride Knudsen cell. It was not until 1993 when there was any fur-ther mention of $Si_{2} ~N$ in the literature. In 1993 Iraqi et al. [30] reported the identification of $Si_{2} ~N$ in a neutralization-reionization mass spectrometric study. Ornellas and Iwata [5] did a thorough computational study on three isomeric forms of $Si_{2} ~N$ , and all three were found to be stable at the CCSD(T)/cc-pVTZ level of theory. Theorder of stability was determined to be: symmetric linear (SiNSi)> symmetric cyclic > asymmetric linear SiSiN. The symmetric lin- ear and cyclic were found to be separated by only $1700 ~cm^{-1}$ , and therefore the isomers could possibly coexist in the gas phase. Their study helped explain the experimental work by Brugh and Morse [4] where the vibrational spectra could not be assigned because the observed transitions could be originating from the two low-lying isomers of $Si_{2} ~N$ .

In 1994, neutral, anionic, and cationic $Si_{3} ~N$ clusters were identi fied experimentally for the first time by Goldberg et al. [31] using collisional-activation and neutralization-reionization mass spec- trometry. The group also calculated the geometries and harmonic vibrational frequencies of the $Si_{n} ~N(n=1-3)$ for the neutral, anio nic, and cationic species with polarized split-valence basis sets(6-311+G(d)) and the Hartree-Fock (HF) and second order Møller-Plesset (MP2) methods. They found that $Si_{3} ~N$ formed two isomeric structures, Y-type and T-type structures with the $Si$ atom occupying the junctions, which are separated by $2.2 kcal / mol$ at the MP2 level, and therefore, may coexist in the gas phase. Also, similar two isomeric structures capable of coexisting in the gas phase were found for $Si_{2} ~N$ , in agreement with a previous study by Iraqi et al. [30] For $Si_{2} ~N_{2}$ , the detailed HF and post-HF calcula tions by Ornellas and Iwata are worth mentioning [18]. Their CCSD(T) calculations showed a global-minimum structure associ- ated with a linear SiNNSi geometry.

In this work we used the diatomic, and triatomic clusters of Si, Nm as benchmark systems to test the most readily available ab initio and density functional theory (DFT) methods with several basis sets and functionals. The best performing ground-state method from the comparison with the available experimental data was then used to optimize the ground-state geometries of allclusters studied in this work, including $SiN, SiN_{2}, Si_{2} ~N, SiN_{3}, Si_{3} ~N$  and $Si_{2} ~N_{2}$ . The energy of the stable ground-state isomers were re-examined using CCSD(T)/6-311G(d) to identify the global-minimum structures. The multireference character of all the stableground-state isomers were explored by analyzing the largest T2 amplitudes. This is followed by excited-state calculations on the electronic transitions mainly in the UV-visible region to help guide future spectroscopic investigations.

## 2. Computational methods
All calculations in this work were performed using the Gaussian09 program [32]. To test the performance of different methods with different basis sets, we calculated the ground-state geometry, harmonic vibrational frequency, and low-lying electronic transi- tions for the three diatomic and triatomic clusters $SiN, SiN_{2}$ , and Si2N. The results were compared with the available experimental values in the ground states and also of the electronic transitions.From this benchmark study, B3LYP/6-311G(d) was selected to opti-mize the ground-state geometry of all small $Si_{n} ~N_{m}(n+m \leqslant 4)$  clusters. The energy of different ground-state isomers were re- calculated by the CCSD(T) method with the 6-311G(d) basis set to determine the global-minimum structures. Finally, the first ten electronic transitions of these small silicon nitride clusters were calculated at the TDDFT/B3LYP/6-311G(d) level based on the opti- mized ground-state geometries. The obtained vertical electronic transition energies were compared with the first ionization energy(IE) of each molecule to know where they lay relative to the IE. For the silicon nitride clusters with no literature IE values, their verti- cal IEs were calculated at the B3LYP/6-311G(d) level.

## 3. Results and discussion
### 3.1. A benchmark study of $SiN, SiN_{2}$ and $Si_{2} ~N$ 
SiN, $SiN_{2}$ and $Si_{2} ~N$ are the three most extensively studied silicon nitride clusters [5,27-29,33-35]. There are lots of data available both experimentally and theoretically, which makes them the best choice for a benchmark study.
#### 3.1.1. The ground state of SiN
SiN is the simplest silicon nitride cluster, therefore, a compre- hensive study of different computational methods, basis sets, and functionals plays a very important role in setting the methods for our theoretical study. For the ground-state calculations, MP2, DFT, Brueckner Doubles (BD), and CCSD were used with different basis sets to perform geometry optimization and calculations of harmonic vibrational frequencies. The results are given in Table 1, where a comparison with the well-recognized experimental results by Bredohl et al. [36] is also provided.
From Table 1, we can see that all methods can give good results of $Si-N$ bond length $(r_{e})$ when a large basis set is chosen. DFT/ B3LYP, BD, CCSD, and MP2 showed good agreements with the experimental results in predicting both bond length and vibra- tional frequency. Among these methods, DFT has a unique advan- tage in both accuracy and efficiency. Usually, BD and CCSD methods are far more time consuming than the DFT method. For the simplest system, SiN, when using large basis sets, aug- ccPVQZ, the DFT method is $\sim 50$ times faster than BD and CCSDmethods. For 6-31G and 6-311G basis sets, we can see from Table 1 that adding diffuse function is not helpful for the improvement of accuracy and adding one $d$ polarization function is already suffi cient. Under the DFT/B3LYP method, the $\omega_{e}$ results for 6-31G, 6 $31 G+$ and $6-31 G++$ are $1051.33,1045.25$ and $1045.25 ~cm^{-1}$ , respectively, relative to the reference value of $1151.36 ~cm^{-1}$ . The

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005

<table><caption>Table 1
The bond distance ($r_e$) and vibrational frequency ($\omega_e$) in the ground electronic state of SiN calculated by different methods and basis sets.</caption>
<thead>
<tr>
<th>Method</th>
<th colspan="2">DFT/B3LYP</th>
<th colspan="2">CCSD</th>
<th colspan="2">BD</th>
<th colspan="2">MP2</th>
</tr>
<tr>
<th>Basis set</th>
<th>$r_e$ (Å)</th>
<th>$\omega_e$ (cm⁻¹)</th>
<th>$r_e$ (Å)</th>
<th>$\omega_e$ (cm⁻¹)</th>
<th>$r_e$ (Å)</th>
<th>$\omega_e$ (cm⁻¹)</th>
<th>$r_e$ (Å)</th>
<th>$\omega_e$ (cm⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [36]</td>
<td>1.5719</td>
<td>1151.36</td>
<td>1.5719</td>
<td>1151.36</td>
<td>1.5719</td>
<td>1151.36</td>
<td>1.5719</td>
<td>1151.36</td>
</tr>
<tr>
<td>6-31G</td>
<td>1.6324</td>
<td>1051.33</td>
<td>1.6583</td>
<td>965.85</td>
<td>1.6492</td>
<td>1023.87</td>
<td>1.5880</td>
<td>1167.66</td>
</tr>
<tr>
<td>6-31G+</td>
<td>1.6324</td>
<td>1045.25</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-31G++</td>
<td>1.6324</td>
<td>1045.25</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-31G(d)</td>
<td>1.5776</td>
<td>1171.59</td>
<td>1.5827</td>
<td>1160.43</td>
<td></td>
<td></td>
<td>1.5370</td>
<td>1476.61</td>
</tr>
<tr>
<td>6-31G(d,p)</td>
<td>1.5776</td>
<td>1171.59</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G</td>
<td>1.6172</td>
<td>1075.22</td>
<td>1.6367</td>
<td>1003.55</td>
<td>1.6297</td>
<td>1054.74</td>
<td>1.5739</td>
<td>1209.41</td>
</tr>
<tr>
<td>6-311G(d)</td>
<td>1.5736</td>
<td>1181.19</td>
<td>1.5760</td>
<td>1176.25</td>
<td>1.5760</td>
<td>1195.63</td>
<td>1.5315</td>
<td>1491.08</td>
</tr>
<tr>
<td>6-311G+(d)</td>
<td>1.5749</td>
<td>1176.14</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G++(d)</td>
<td>1.5749</td>
<td>1176.14</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G(d,p)</td>
<td>1.5736</td>
<td>1181.19</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G(2d)</td>
<td>1.5683</td>
<td>1180.81</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G(3d)</td>
<td>1.5667</td>
<td>1185.46</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6-311G++(3df,3pd)</td>
<td>1.5661</td>
<td>1184.11</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>cc-PVDZ</td>
<td>1.5890</td>
<td>1140.80</td>
<td>1.5997</td>
<td>1111.98</td>
<td>1.5974</td>
<td>1136.16</td>
<td>1.5475</td>
<td>1398.62</td>
</tr>
<tr>
<td>cc-PVTZ</td>
<td>1.5734</td>
<td>1177.81</td>
<td>1.5767</td>
<td>1176.46</td>
<td>1.5721</td>
<td>1192.54</td>
<td>1.5317</td>
<td>1509.22</td>
</tr>
<tr>
<td>cc-PVQZ</td>
<td>1.5675</td>
<td>1185.02</td>
<td>1.5681</td>
<td>1193.75</td>
<td>1.5609</td>
<td>1214.30</td>
<td></td>
<td></td>
</tr>
<tr>
<td>aug-cc-PVDZ</td>
<td>1.5920</td>
<td>1131.06</td>
<td>1.6057</td>
<td>1097.41</td>
<td>1.6027</td>
<td>1119.65</td>
<td></td>
<td></td>
</tr>
<tr>
<td>aug-cc-PVTZ</td>
<td>1.5740</td>
<td>1175.10</td>
<td>1.5784</td>
<td>1171.82</td>
<td>1.5711</td>
<td>1192.65</td>
<td></td>
<td></td>
</tr>
<tr>
<td>aug-ccPVQZ</td>
<td>1.5676</td>
<td>1183.45</td>
<td>1.5687</td>
<td>1191.62</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>DGDZVP</td>
<td>1.5793</td>
<td>1168.61</td>
<td>1.5687</td>
<td>1171.82</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>DGDZVP2</td>
<td>1.5807</td>
<td>1164.92</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Note: The best $r_e$ and $\omega_e$ values obtained at various basis sets under each method are bolded.

addition of one d polarization function to 6-31G increases the $r_e$ accuracy from 96.2 to 99.6%, while the introduction of an additional p function (i.e., 6-31G(d,p)) gives the same accuracy of 99.6%. Similar observation is made for the 6-311G(d) basis set under the DFT/B3LYP method where the addition of one (+) and two (++) diffuse functions reduced the accuracy of the $r_e$ value from 1.5736 to 1.5749 Å relative to 1.5719 Å as shown in Table 1. The obtained $r_e$ values for 6-311G was 1.6172 Å while a more accurate value of 1.5736 Å was obtained for both 6-311G(d) and 6-311G(d,p) basis sets under the DFT/B3LYP method.

Under the DFT/B3LYP method the difference between the calculated and the experimental Si—N bond length, $\Delta r_e$, for the following basis sets, 6-311G(d), cc-PVTZ, and aug-cc-PVTZ are 0.0017, 0.0015, and 0.0021 Å, respectively, and their corresponding difference in vibrational frequencies, $\Delta\omega_e$, relative to the experimental value of 1151.35 cm⁻¹ are 29.83, 26.45, and 23.74 cm⁻¹, respectively. The $\Delta\omega_e$ results of other basis sets, e.g., DGDZVP2 and cc-PVDZ are 13.56 and −10.56 cm⁻¹, respectively. These are better than 6-311G(d), cc-PVTZ, and aug-cc-PVTZ, however, these three basis sets have better balance of accuracy for both $r_e$ and $\omega_e$ under the DFT/B3LYP method than all other basis sets.

Under the CCSD method the best basis sets for computing the $r_e$ values are aug-cc-PVQZ, DGDZVP, cc-PVQZ, and 6-311G(d), while those for $\omega_e$ are 6-31G(d), 6-311G(d), aug-cc-PVTZ, and DGDZVP. This shows that the 6-311G(d) basis set is quite a good choice since it is among the best performing basis sets for two of the best post-HF methods, i.e., DFT/B3LYP and CCSD, that we have tested. Also, under the BD method, 6-311G(d) performed fairly well. It gave the $\Delta r_e$ and $\Delta\omega_e$ values of 0.0041 Å and 44.27 cm⁻¹ when compared to the best basis sets, cc-PVTZ, aug-cc-PVTZ, and cc-PVQZ which gave $\Delta r_e$ values of 0.0002, −0.0008, and −0.010 Å, with the corresponding $\Delta\omega_e$ values of 41.18, 41.29, and 62.94 cm⁻¹, respectively. The 6-311G(d) basis set performed fairly well with the $\Delta r_e$ and $\Delta\omega_e$ values of 0.0057 Å and 20.23 cm⁻¹, respectively, under the DFT/B3LYP method. It also gave the best $\Delta\omega_e$ value of 9.07 cm⁻¹ but a poor $\Delta r_e$ value of 0.0108 Å when compared to the results of 6-311G(d) basis set which had $\Delta\omega_e$ and $\Delta r_e$ values of 9.07 cm⁻¹ and 0.0041 Å, respectively, under the CCSD method.

For the Dunning's correlation consistent (CC) basis sets: cc-PVDZ, cc-PVTZ, and cc-PVQZ, the differences in their performances is not that significant. The more expensive cc-PVQZ is not significantly more accurate than cc-PVTZ. Therefore, cc-PVTZ and aug-cc-PVTZ were chosen as a supplement to the 6-311G(d) and 6-31G(d) basis sets. One note is that the 6-311G(d) and 6-31G(d) basis sets are more cost efficient in time than the Dunning's correlation consistent basis sets, cc-PVTZ and aug-cc-PVTZ.

To test the performance of different functionals with the DFT method, a comparison of several functionals was made using the same basis set, 6-311G(d). The results for $r_e$ and $\omega_e$ of SiN are given in Table 2. From Table 2, we can see that the best performing functionals in terms of $r_e$ are: B3LYP, LSDA/AUTO, B3PW91, and HSEH1PBE with the $\Delta r_e$ values of 0.0017, −0.0022, −0.0006, and −0.0024 Å, and the corresponding $\Delta\omega_e$ values of 29.83, 42.25, 39.44, and 44.77 cm⁻¹, respectively. Though other functionals such as BPV86/AUTO, PBEPBE, HCTH, and TPSSPSS have better $\Delta\omega_e$ values of −3.86, −1.02, −8.32, and 4.59 cm⁻¹, respectively, than the previously mentioned functionals, the B3LYP and B3PW9 functionals could be said to have better balance of accuracy than the rest of the functionals tested.

From the above discussions, the DFT/B3LYP, DFT/B3PW91, and CCSD methods were chosen along with the 6-31G(d), 6-311G(d), cc-PVTZ and aug-cc-PVTZ basis sets for the ground-state calculations of SiN₂ and Si₂N species.

<table><caption>Table 2
Calculated bond distance ($r_e$) and vibrational frequency ($\omega_e$) of SiN with different functionals using the DFT method and 6-311G(d) basis set.</caption>
<thead>
<tr>
<th>Method</th>
<th>$r_e$ (Å)</th>
<th>$\Delta r_e$ (Å)</th>
<th>$\omega_e$ (cm⁻¹)</th>
<th>$\Delta\omega_e$ (cm⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [36]</td>
<td>1.5719</td>
<td>0</td>
<td>1151.36</td>
<td>0</td>
</tr>
<tr>
<td>B3LYP</td>
<td>1.5736</td>
<td>0.0017</td>
<td>1181.19</td>
<td>29.83</td>
</tr>
<tr>
<td>LSDA/AUTO</td>
<td>1.5697</td>
<td>−0.0022</td>
<td>1193.61</td>
<td>42.25</td>
</tr>
<tr>
<td>BPV86/AUTO</td>
<td>1.5860</td>
<td>0.0141</td>
<td>1147.50</td>
<td>−3.86</td>
</tr>
<tr>
<td>CAM-B3LYP/AUTO</td>
<td>1.5628</td>
<td>−0.0091</td>
<td>1218.30</td>
<td>66.94</td>
</tr>
<tr>
<td>MPW1PW91</td>
<td>1.5683</td>
<td>−0.0036</td>
<td>1199.98</td>
<td>48.62</td>
</tr>
<tr>
<td>B3PW91</td>
<td>1.5713</td>
<td>−0.0006</td>
<td>1190.80</td>
<td>39.44</td>
</tr>
<tr>
<td>PBEPBE</td>
<td>1.5858</td>
<td>0.0139</td>
<td>1150.34</td>
<td>−1.02</td>
</tr>
<tr>
<td>HSEH1PBE</td>
<td>1.5695</td>
<td>−0.0024</td>
<td>1196.13</td>
<td>44.77</td>
</tr>
<tr>
<td>HCTH</td>
<td>1.5800</td>
<td>0.0081</td>
<td>1143.04</td>
<td>−8.32</td>
</tr>
<tr>
<td>TPSSPSS</td>
<td>1.5829</td>
<td>0.0110</td>
<td>1155.95</td>
<td>4.59</td>
</tr>
<tr>
<td>WB97XD</td>
<td>1.5640</td>
<td>−0.0079</td>
<td>1225.44</td>
<td>74.08</td>
</tr>
</tbody>
</table>

### 3.1.2. Excited states of SiN

Compared to the ground state, excited states are much less studied due to the difficulties in experimental techniques. Time-dependent DFT (TDDFT) and equation of motion CCSD (EOMCCSD) with different basis sets were used to study the excited states. The results are shown in Table 3. It should be pointed out that the calculated results in Table 3 are the vertical excitation energies. From the literature, three low-lying electronic transitions of $A^{2}\Pi \leftarrow X^{2}\Sigma^{+}$, $B^{2}\Sigma^{+} \leftarrow X^{2}\Sigma^{+}$, and $D^{2}\Pi \leftarrow X^{2}\Sigma^{+}$ have experimental values. The corresponding widely cited $T_{e}$ values (the difference in the potential energy minimum between the ground and excited electronic states) [14] for these three transitions were chosen as our references. Unfortunately, there are no vertical electronic transition energies reported in the literature. For the $A^{2}\Pi \leftarrow X^{2}\Sigma^{+}$ transition, the difference in transition energy between the best method, TDDFT/B3LYP/6-311G(d), and the experimental value ($\Delta T$) is $52.79\ \text{cm}^{-1}$, while the best EOMCCSD/aug-cc-PVTZ method gave a large difference of $1018.24\ \text{cm}^{-1}$. Similarly, for the $B^{2}\Sigma^{+} \leftarrow X^{2}\Sigma^{+}$ transition, the best $\Delta T$ values obtained for TDDFT/ B3LYP/6-31G(d) and EOMCCSD/6-31G were 822.55 and $2722.79\ \text{cm}^{-1}$, respectively. The best $\Delta T$ values for the $D^{2}\Pi \leftarrow X^{2}\Sigma^{+}$ transition obtained at TDDFT/B3LYP/aug-cc-PVTZ and EOMCCSD/6-31G(d) were 281.25 and $288.51\ \text{cm}^{-1}$, respectively. This shows that TDDFT out-performs EOMCCSD method for excited state calculations of the SiN cluster.

### 3.1.3. Ground state of $SiN_{2}$

Previous studies [27,28,37] showed that the triplet asymmetric linear $SiN_{2}$ ($X^{3}\Sigma^{-}$) is the most stable isomer in the ground state. This is the only isomer which has experimental data up to date. Therefore, this isomer was chosen to test our selected methods of DFT/B3LYP, DFT/B3PW91, and CCSD methods with the 6-31G (d), 6-311G(d), cc-PVTZ and aug-cc-PVTZ basis sets based on our benchmark study of SiN in Section 3.1.1. The results of the N-N and Si-N bond lengths, and the vibrational frequencies of symmetric N-N stretching ($\omega_{1}$), bending ($\omega_{2}$), and asymmetric Si-N stretching ($\omega_{3}$) modes are shown in Table 4. Both B3LYP and B3PW91 methods slightly overestimate $\omega_{1}$ and $\omega_{3}$, but their predictions are very close to the experimental values reported by Ornellas et al. [28] CCSD overestimates $\omega_{1}$ but underestimates $\omega_{3}$. In general, B3LYP and B3PW91 provide better agreements with experiments than CCSD.

### 3.1.4. Excited states of $SiN_{2}$

To our knowledge, only the $A^{3}\Pi \leftarrow X^{3}\Sigma^{-}$ transition of asymmetric linear $SiN_{2}$ has been observed experimentally with a transition origin at $27,200\ \text{cm}^{-1}$ [27], and therefore it is used for comparison with our theoretical results using TDDFT/B3LYP and EOMCCSD with different basis sets. Table 5 lists the calculation results for the vertical transition energy of $A^{3}\Pi \leftarrow X^{3}\Sigma^{-}$. Neither the TDDFT/B3LYP and EOMCCSD performs well in predicting this specific electronic transition energy. The lowest deviation of $4402.40\ \text{cm}^{-1}$ from the experimental value was obtained from the EOMCCSD/6-31G. Unfortunately, there were no experimental data to other excited states available for comparison.

### 3.1.5. Ground state of $Si_{2}N$

The ground state of $Si_{2}N$ has three stable isomers: symmetric linear, asymmetric linear, and symmetric bent. Of these isomers, symmetric linear $^{2}\Pi_{g}$ state has been reported as the electronic ground state [4,5,38]. The experimental value for this state is used to compare with our calculations, and the results for the Si-N bond

---

Table 3
Calculated electronic transition energies ($T$ in $\text{cm}^{-1}$) for $A^{2}\Pi \leftarrow X^{2}\Sigma^{+}$, $B^{2}\Sigma^{+} \leftarrow X^{2}\Sigma^{+}$, and $D^{2}\Pi \leftarrow X^{2}\Sigma^{+}$ of SiN using TDDFT/B3LYP and EOMCCSD with different basis sets.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">TDDFT/B3LYP</th>
<th colspan="2"></th>
<th colspan="2"></th>
<th colspan="2">EOMCCSD</th>
<th colspan="2"></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2">$A^{2}\Pi \leftarrow X^{2}\Sigma^{+}$</th>
<th colspan="2">$B^{2}\Sigma^{+} \leftarrow X^{2}\Sigma^{+}$</th>
<th colspan="2">$D^{2}\Pi \leftarrow X^{2}\Sigma^{+}$</th>
<th colspan="2">$A^{2}\Pi \leftarrow X^{2}\Sigma^{+}$</th>
<th colspan="2">$B^{2}\Sigma^{+} \leftarrow X^{2}\Sigma^{+}$</th>
<th colspan="2">$D^{2}\Pi \leftarrow X^{2}\Sigma^{+}$</th>
</tr>
<tr>
<th></th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [14]</td>
<td>2032.15</td>
<td>0</td>
<td>24299.19</td>
<td>0</td>
<td>28859.55</td>
<td>0</td>
<td>2032.15</td>
<td>0</td>
<td>24299.19</td>
<td>0</td>
<td>28859.55</td>
<td>0</td>
</tr>
<tr>
<td>6-31G</td>
<td>2188.18</td>
<td>156.03</td>
<td>22308.48</td>
<td>1990.71</td>
<td>27689.81</td>
<td>1169.74</td>
<td>5690.24</td>
<td>3658.09</td>
<td>27021.98</td>
<td>2722.79</td>
<td>29577.15</td>
<td>717.60</td>
</tr>
<tr>
<td>6-31G(d)</td>
<td>1738.93</td>
<td>−293.22</td>
<td>25121.74</td>
<td>822.55</td>
<td>29613.44</td>
<td>753.89</td>
<td>5258.73</td>
<td>3226.58</td>
<td>27142.16</td>
<td>2842.97</td>
<td>29148.06</td>
<td>288.51</td>
</tr>
<tr>
<td>6-311G</td>
<td>2660.02</td>
<td>627.87</td>
<td>23343.29</td>
<td>−955.90</td>
<td>28554.43</td>
<td>−305.12</td>
<td>5920.91</td>
<td>3888.76</td>
<td>27394.61</td>
<td>3095.42</td>
<td>29944.13</td>
<td>1084.58</td>
</tr>
<tr>
<td>6-311G(d)</td>
<td>2084.94</td>
<td>52.79</td>
<td>25554.05</td>
<td>1254.86</td>
<td>29918.32</td>
<td>1058.77</td>
<td>3656.11</td>
<td>1623.96</td>
<td>28731.88</td>
<td>4432.69</td>
<td>31227.36</td>
<td>2367.81</td>
</tr>
<tr>
<td>6-311G++(d)</td>
<td>1595.36</td>
<td>−436.79</td>
<td>25478.24</td>
<td>1179.05</td>
<td>30813.59</td>
<td>1954.04</td>
<td>3209.28</td>
<td>1177.13</td>
<td>28416.51</td>
<td>4117.32</td>
<td>30808.75</td>
<td>1949.20</td>
</tr>
<tr>
<td>6-311G++(3df)</td>
<td>1704.25</td>
<td>−327.90</td>
<td>25974.27</td>
<td>1675.08</td>
<td>30857.95</td>
<td>1998.40</td>
<td>3593.20</td>
<td>1561.05</td>
<td>29051.27</td>
<td>4752.08</td>
<td>31613.69</td>
<td>2754.14</td>
</tr>
<tr>
<td>cc-PVTZ</td>
<td>1646.18</td>
<td>−385.97</td>
<td>25554.86</td>
<td>1255.67</td>
<td>29338.41</td>
<td>478.86</td>
<td>3181.05</td>
<td>1148.90</td>
<td>29006.11</td>
<td>4706.92</td>
<td>31291.07</td>
<td>2431.52</td>
</tr>
<tr>
<td>aug-cc-PVTZ</td>
<td>1455.83</td>
<td>−576.32</td>
<td>25492.76</td>
<td>1193.57</td>
<td>29140.80</td>
<td>281.25</td>
<td>3050.39</td>
<td>1018.24</td>
<td>28902.87</td>
<td>4603.68</td>
<td>31154.77</td>
<td>2295.22</td>
</tr>
</tbody>
</table>

---

Table 4
Calculated bond lengths and vibrational frequencies of the most stable asymmetric linear SiNN isomer in its ground state, $X^{3}\Sigma^{-}$, using different methods and basis sets.

<table>
<thead>
<tr>
<th>Method</th>
<th>N-N</th>
<th>Si-N</th>
<th>$\omega_{1}$</th>
<th>$\omega_{2}$</th>
<th>$\omega_{3}$</th>
</tr>
<tr>
<th></th>
<th>(Å)</th>
<th>(Å)</th>
<th>($\text{cm}^{-1}$)</th>
<th>($\text{cm}^{-1}$)</th>
<th>($\text{cm}^{-1}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [27]</td>
<td></td>
<td></td>
<td>1731</td>
<td></td>
<td>485</td>
</tr>
<tr>
<td>Expt. [28]</td>
<td></td>
<td></td>
<td>1830</td>
<td></td>
<td>500</td>
</tr>
<tr>
<td>Expt. [28]</td>
<td></td>
<td></td>
<td>1785</td>
<td></td>
<td>476</td>
</tr>
<tr>
<td>Expt. (Ar, 12 K) [37]</td>
<td></td>
<td></td>
<td>1731.6</td>
<td></td>
<td>484.3</td>
</tr>
<tr>
<td>Exp. ($N_{2}$, 12 K) [37]</td>
<td></td>
<td></td>
<td>1754.7</td>
<td></td>
<td>461.6</td>
</tr>
<tr>
<td>B3LYP/6-31G(d)</td>
<td>1.1535</td>
<td>1.7572</td>
<td>1839.70</td>
<td>331.80</td>
<td>517.35</td>
</tr>
<tr>
<td>B3LYP/6-311G(d)</td>
<td>1.1459</td>
<td>1.7559</td>
<td>1825.85</td>
<td>328.63</td>
<td>515.30</td>
</tr>
<tr>
<td>B3LYP/cc-PVTZ</td>
<td>1.1408</td>
<td>1.7531</td>
<td>1833.09</td>
<td>340.47</td>
<td>526.01</td>
</tr>
<tr>
<td>B3LYP/aug-cc-PVTZ</td>
<td>1.1412</td>
<td>1.7519</td>
<td>1824.20</td>
<td>337.12</td>
<td>525.89</td>
</tr>
<tr>
<td>B3PW91/6-31G(d)</td>
<td>1.1508</td>
<td>1.7537</td>
<td>1868.51</td>
<td>331.12</td>
<td>527.96</td>
</tr>
<tr>
<td>B3PW91/6-311G(d)</td>
<td>1.1433</td>
<td>1.7531</td>
<td>1859.43</td>
<td>330.76</td>
<td>526.14</td>
</tr>
<tr>
<td>B3PW91/cc-PVTZ</td>
<td>1.1382</td>
<td>1.7511</td>
<td>1866.72</td>
<td>343.10</td>
<td>535.88</td>
</tr>
<tr>
<td>B3PW91/aug-cc-PVTZ</td>
<td>1.1385</td>
<td>1.7500</td>
<td>1859.80</td>
<td>340.16</td>
<td>536.25</td>
</tr>
<tr>
<td>CCSD/6-31G(d)</td>
<td>1.1426</td>
<td>1.8277</td>
<td>1920.03</td>
<td>302.97</td>
<td>304.40</td>
</tr>
<tr>
<td>CCSD/6-311G(d)</td>
<td>1.1344</td>
<td>1.8159</td>
<td>1906.01</td>
<td>300.90</td>
<td>316.48</td>
</tr>
<tr>
<td>CCSD/cc-PVTZ</td>
<td>1.1252</td>
<td>1.8196</td>
<td>1947.11</td>
<td>329.85</td>
<td>347.67</td>
</tr>
<tr>
<td>CCSD/aug-cc-PVTZ</td>
<td>1.1268</td>
<td>1.8141</td>
<td>1923.16</td>
<td>329.91</td>
<td>357.90</td>
</tr>
</tbody>
</table>

---

Table 5
Calculated electronic transition energy ($T$ in $\text{cm}^{-1}$) of $A^{3}\Pi \leftarrow X^{3}\Sigma^{-}$ for the asymmetric linear $SiN_{2}$ using TDDFT/B3LYP and EOM CCSD with different basis sets.

<table>
<thead>
<tr>
<th>Methods</th>
<th colspan="2">TDDFT/B3LYP</th>
<th colspan="2">EOMCCSD</th>
</tr>
<tr>
<th></th>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Exp. [27]</td>
<td>27,200</td>
<td>0</td>
<td>27,200</td>
<td>0</td>
</tr>
<tr>
<td>6-31G</td>
<td>34109.17</td>
<td>6909.17</td>
<td>31602.40</td>
<td>4402.40</td>
</tr>
<tr>
<td>6-31G(d)</td>
<td>34870.56</td>
<td>7670.56</td>
<td>34105.95</td>
<td>6905.95</td>
</tr>
<tr>
<td>6-311G</td>
<td>34372.11</td>
<td>7172.11</td>
<td>31939.54</td>
<td>4739.54</td>
</tr>
<tr>
<td>6-311G(d)</td>
<td>34768.93</td>
<td>7568.93</td>
<td>33938.18</td>
<td>6738.18</td>
</tr>
<tr>
<td>6-311++G(d)</td>
<td>34124.50</td>
<td>6924.50</td>
<td>32945.32</td>
<td>5745.32</td>
</tr>
<tr>
<td>6-311++G(3df)</td>
<td>34051.10</td>
<td>6851.10</td>
<td>33002.58</td>
<td>5802.58</td>
</tr>
<tr>
<td>cc-PVTZ</td>
<td>34493.90</td>
<td>7293.90</td>
<td>33426.83</td>
<td>6226.83</td>
</tr>
<tr>
<td>aug-cc-PVTZ</td>
<td>33913.99</td>
<td>6713.99</td>
<td>32944.51</td>
<td>5744.51</td>
</tr>
</tbody>
</table>

---

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005

<table><caption>Table 6
Calculated Si—N bond length and vibrational frequencies of the symmetric linear $^{2}\Pi_{g}$ electronic ground state of $Si_{2}N$.</caption>
<thead>
<tr>
<th>Method</th>
<th>Si—N (Å)</th>
<th>$\omega_{1}$ ($\sigma_{g}$) (cm⁻¹)</th>
<th>$\omega_{2}$ ($\pi_{u}$) (cm⁻¹)</th>
<th>$\omega_{3}$ ($\sigma_{u}$) (cm⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [4]</td>
<td>1.6395</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Expt. (matrix Ar) [38]</td>
<td></td>
<td></td>
<td></td>
<td>904.0</td>
</tr>
<tr>
<td>Expt. (matrix N₂) [38]</td>
<td></td>
<td></td>
<td></td>
<td>910.0</td>
</tr>
<tr>
<td>B3LYP/6-31G(d)</td>
<td>1.6429</td>
<td>613.81</td>
<td>192.95</td>
<td>1061.83</td>
</tr>
<tr>
<td>B3LYP/6-311G(d)</td>
<td>1.6400</td>
<td>615.76</td>
<td>172.45</td>
<td>1065.53</td>
</tr>
<tr>
<td>B3LYP/cc-PVTZ</td>
<td>1.6386</td>
<td>614.26</td>
<td>152.49</td>
<td>1064.18</td>
</tr>
<tr>
<td>B3LYP/aug-cc-PVTZ</td>
<td>1.6386</td>
<td>612.72</td>
<td>151.53</td>
<td>1062.67</td>
</tr>
<tr>
<td>B3PW91/6-31G(d)</td>
<td>1.6404</td>
<td>619.26</td>
<td>188.25</td>
<td>1072.38</td>
</tr>
<tr>
<td>B3PW91/6-311G(d)</td>
<td>1.6377</td>
<td>620.98</td>
<td>167.51</td>
<td>1075.79</td>
</tr>
<tr>
<td>B3PW91/cc-PVTZ</td>
<td>1.6360</td>
<td>619.87</td>
<td>142.36</td>
<td>1076.57</td>
</tr>
<tr>
<td>B3PW91/aug-cc-PVTZ</td>
<td>1.6359</td>
<td>618.83</td>
<td>140.89</td>
<td>1075.83</td>
</tr>
<tr>
<td>CCSD/6-31G(d)</td>
<td>1.6433</td>
<td>618.51</td>
<td>180.85</td>
<td>918.68</td>
</tr>
<tr>
<td>CCSD/6-311G(d)</td>
<td>1.6378</td>
<td>625.77</td>
<td>164.13</td>
<td>926.05</td>
</tr>
<tr>
<td>CCSD/cc-PVTZ</td>
<td>1.6382</td>
<td>622.61</td>
<td>142.18</td>
<td>882.31</td>
</tr>
<tr>
<td>CCSD/aug-cc-PVTZ</td>
<td>1.6397</td>
<td>618.80</td>
<td>134.79</td>
<td>868.94</td>
</tr>
</tbody>
</table>

length, vibrational frequencies of symmetric stretching $[\omega_{1}(\sigma_{g})]$, bending $[\omega_{2}(\pi_{u})]$ and asymmetric stretching $[\omega_{3}(\sigma_{u})]$ modes are listed in Table 6. Here, the Si—N bond lengths calculated by both DFT and CCSD methods are in good agreements with the experimental value of 1.6395 Å. Of the three vibrational modes, only $\omega_{3}(\sigma_{u})$ has experimental data. In contrast to the $SiN_{2}$ calculations, the CCSD method with the basis sets of 6-31G(d) and 6-311G(d) gave very close $\omega_{3}(\sigma_{u})$ values of 918.68 and $926.05\ \text{cm}^{-1}$, respectively, relative to the experimental values (904.0 cm⁻¹ in Ar matrix, and $910.0\ \text{cm}^{-1}$ in Ne matrix) than the DFT methods, as shown in Table 6. B3LYP and B3PW91 slightly overestimate the $\omega_{3}(\sigma_{u})$ which is similar to what was observed for the $SiN_{2}$ cluster. As for basis sets, there are no significant differences among them.

### 3.1.6. Excited states of $Si_{2}N$
The $^{2}\Sigma_{u}^{+}$ state is the only experimentally observed excited electronic state of $Si_{2}N$ reported in literature, where a vertical excitation energy of $34314.29\ \text{cm}^{-1}$ was found using resonant two-photon ionization spectroscopy [4]. The results we obtained with our theoretical calculations together with the experimental reference value are given in Table 7. The results show that both TDDFT and EOMCCSD methods give very close values to the experimental value of $34314.29\ \text{cm}^{-1}$.

In summary, DFT/B3LYP achieves the best balance between accuracy and efficiency for geometry optimization and the calculations of the vibrational frequencies in the ground states of $SiN$, $SiN_{2}$ and $Si_{2}N$. TDDFT performs better than EOMCCSD in predicting the electronic transition energies to the three low-lying excited states ($A^{2}\Pi$, $B^{2}\Sigma^{+}$ and $C^{2}\Pi$) of SiN. For $SiN_{2}$ and $Si_{2}N$ clusters, it is hard to claim which one is better due to the limited experimental data for comparison. However, TDDFT is more efficient in terms of the computational cost. We therefore choose TDDFT as the method to calculate the electronic transitions of all small silicon nitride clusters reported in this work. As for the basis set, 6-311G(d) is the choice for its nice balance between accuracy and efficiency.

### 3.2. Ground-state geometry optimization and electronic transitions of small silicon nitride clusters, $Si_{n}N_{m}\ (n + m \leqslant 4)$

#### 3.2.1. SiN
The geometry optimization of SiN using the B3LYP/6-311G(d) method gives a Si-N bond length of 1.574 Å. This is typical of doubly bonded Si=N [35], and it agrees well with the experimentally reported value of 1.5719 Å [36]. Fig. 1(a) is a spectrum of the calculated first 10 excited state transitions from the ground state $X^{2}\Sigma^{+}$ using TDDFT/B3LYP/6-311G(d). The data for the calculated electronic transition energies and their corresponding oscillator strengths are listed in Table S1 (See Support Information). The transition energy to the 10th excited state at 7.09 eV lies below the ionization energy (IE) of SiN at 10.1 eV [39].

#### 3.2.2. $SiN_{2}$
The optimized geometries of the various isomers of $SiN_{2}$ are shown in Fig. 2. The bond length and bond order information for all stable ground-state $SiN_{2}$ isomers can be found in Fig. 2. This

![](./images/811165001766141952_1.jpg)

Fig. 1. Calculated electronic transition spectra from the ground state to the first ten excited states for (a) SiN, (b) $SiN_{2}$, and (c) $Si_{2}N$ using TDDFT/B3LYP/6-311G(d).

<table><caption>Table 7
Calculated electronic transition energy ($T$ in cm⁻¹) of $^{2}\Sigma_{u}^{+} \leftarrow \tilde{X}^{2}\Pi_{g}$ for symmetric linear $Si_{2}N$ using TDDFT/B3LYP and EOM-CCSD with different basis sets.</caption>
<thead>
<tr>
<th rowspan="2">Methods</th>
<th colspan="2">TDDFT/B3LYP</th>
<th colspan="2">EOM-CCSD</th>
</tr>
<tr>
<th>$T$</th>
<th>$\Delta T$</th>
<th>$T$</th>
<th>$\Delta T$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expt. [4]</td>
<td>34314.29</td>
<td>0</td>
<td>34314.29</td>
<td>0</td>
</tr>
<tr>
<td>6-31G</td>
<td>32891.28</td>
<td>−1423.01</td>
<td>34821.36</td>
<td>507.07</td>
</tr>
<tr>
<td>6-31G(d)</td>
<td>33616.37</td>
<td>−697.92</td>
<td>35477.90</td>
<td>1163.61</td>
</tr>
<tr>
<td>6-311G</td>
<td>33623.63</td>
<td>−690.66</td>
<td>35778.74</td>
<td>1464.45</td>
</tr>
<tr>
<td>6-311G(d)</td>
<td>34076.10</td>
<td>−238.19</td>
<td>35435.95</td>
<td>1121.66</td>
</tr>
<tr>
<td>6-311++G(d)</td>
<td>35028.64</td>
<td>714.35</td>
<td>35848.10</td>
<td>1533.81</td>
</tr>
<tr>
<td>6-311++G(3df)</td>
<td>34145.47</td>
<td>−168.82</td>
<td>34114.82</td>
<td>−199.47</td>
</tr>
<tr>
<td>cc-PVTZ</td>
<td>34131.76</td>
<td>−182.53</td>
<td>34429.37</td>
<td>115.08</td>
</tr>
<tr>
<td>aug-cc-PVTZ</td>
<td>34169.66</td>
<td>−144.63</td>
<td>35227.86</td>
<td>913.57</td>
</tr>
</tbody>
</table>

![](./images/811165001766141952_2.jpg)

Fig. 2. Optimized ground-state structures of SiN₂ at the B3LYP/6-311G(d) level of theory. S1 denotes singlet isomer 1, T1 denotes triplet isomer 1, and so on. The value below each isomer is their relative energy (kcal/mol) calculated with CCSD(T)/6-311G(d) while those within the bracket are calculated with B3LYP/6-311G(d).

practice was performed for all other clusters studied in this work.
The triplet asymmetric linear isomer $X^3\Sigma^-$ (SiNN) is the most stable one as shown in Fig. 2, and this agrees with previous studies[20,21,26]. We performed a natural bond orbital (NBO) analysis at the B3LYP/6-311G(d) level of theory for all the ground-state structures shown in Fig. 2. For the triplet global minimum structure (T1), the natural population analysis (NPA) showed atomic charges of 0.45, −0.50, and 0.05 on Si, N (central atom), and N, with corresponding valence electron populations of 3.52, 5.45 and 4.90, respectively. This suggests a bond order (BO) of ~1.5 between the Si and central N, and 2 between the two N atoms. However, the obtained SiN bond length, $r$(SiN), of 1.756 Å is typical of a singly bonded Si and N [28] instead of the predicted BO of 1.5 from the NBO analysis. The $r$(NN) of 1.146 Å is in good agreement with a previously reported theoretical value of 1.135 Å [28] for a N=N double bond. In addition, our calculated $r$(NN) in T1 agrees well with the doubly bonded N₂ in CH₂N₂ [40]. This supports our calculation that the NN bond in SiNN is a double bond as shown in Fig. 2. Similar arguments can be applied to the SiN and NN bond lengths and orders for the lowest singlet SiNN structure (S1). The atomic charges for N, Si, and N in the triplet centro-symmetric bent NSiN structure (T2) are −0.57, 1.14 and −0.57 with corresponding valence electron populations of 5.55, 2.79 and 5.55, respectively. This suggests a BO of ~1.5 for SiN as shown in the structure T2. A previous theoretical study [41] reports a Si=N double length of 1.596 Å in small-ring bridgehead silanimines. Our $r$(SiN) value of 1.695 Å lies between those of a Si—N single bond and a Si=N double bond, which supports our calculated BO of ~1.5. Following this argument, the $r$(SiN) and $r$(NN) values of 1.843 Å and 1.235 Å obtained for the singlet S2 structure indicate a single and double bond, respectively, as shown in Fig. 2. The atomic charges for N, Si, and N in the symmetric linear NSiN structure (T3) are −0.96, 0.93 and −0.96 with corresponding valence electron populations of 3.46, 1.0 and 3.46, respectively. This indicates a BO ~1.5 for both Si—N bonds. A comparison of the $r$(SiN) value of 1.645 Å in our T3 structure to the literature values of $r$(Si=N) and $r$(Si—N) agrees with a BO of ~1.5 obtained from the NBO analysis. Similar to the T3 structure, both Si—N bonds in S3 have a bond order of 1.5.

The most stable isomer, T1, has a N=N bond connection. So do the other two low-energy isomers, S1 and S2. The other three isomers that have only the Si—N bonds are significantly higher in energy as compared to T1, S1 and S2. This suggests that the N—N bonding is more favorable than N—Si bonding, which makes T1, S1, and S2 the more stable isomers.

![](./images/811165001766141952_3.jpg)

Fig. 3. Optimized ground-state structures of Si₂N using B3LYP/6-311G(d). D1 denotes doublet isomer 1, Q1 denotes quartet isomer 1, and so on. The value below each isomer is their relative energy (kcal/mol) calculated with CCSD(T)/6-311G(d) while those within the bracket are calculated with B3LYP/6-311G(d).

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005

The IE of $SiN_2$ was calculated at the CCSD(T)/6-311G(d) level to be 7.67 eV, which is quite low. The calculated first 10 excited state transitions of $SiN_2$ are shown in Fig. 1(b), and the data are listed in Table S1 (See Support Information). Here, the 10th excited state at 7.54 eV is very close to the calculated first IE of $SiN_2$. TDDFT/B3LYP may not be able describe this and other high-lying excited states quite accurately. However, the first 10 excited state transitions were still included for $SiN_2$ for consistency with other molecules.

### 3.2.3. $Si_2N$
The stable isomers of $Si_2N$ after geometry optimization at the B3LYP/6-311G(d) level of theory are shown in Fig. 3. The doublet symmetric linear SiNSi isomer is found to be the most stable one, and this agrees with a previous study by Ornellas et al. [5]. The highest-energy isomer, in both doublet and quartet states, is the asymmetric linear structure with relative energies of 82.3 and 107.1 kcal/mol, respectively, above the global-minimum structure. This indicates that the Si-Si interaction is not favorable. By comparing the bonding connections between Si and N for both $Si_2N$ and $SiN_2$, a bonding tendency of N-N > N-Si > Si-Si can be observed. For the doublet symmetric linear SiNSi structure (D1), the NBO calculation gave Si, Ni and Si atomic charges of 0.86, $-1.71$ and 0.86, with corresponding valence electron populations of 3.1, 6.7 and 3.1, respectively. This indicates a high inclination towards a whole number SiN bond order of 1 or 2. Since the obtained $r$(SiN) value of 1.640 Å is closer to that of a $Si=N$ double bond than a Si-N single bond as discussed in the previous section on $SiN_2$, it is safe to say that the SiN bonds in both the D1 and Q1 structures have a very high double bond character as shown in Fig. 3. The $r$(SiN) value of 1.776 Å in Q2 is typical of Si-N single bonds [28]. However, the $r$(SiSi) value of 2.226 Å is approximately mid-way between singly and doubly bonded SiSi atoms in comparison to Si-Si and $Si=Si$ values of 2.320 [40] and 2.150 Å [41], respectively. This is supported by the NBO calculation which gives valence electron population of 3.40 for both Si atoms. The $r$(SiN) value of 1.683 Å for the D2 structure indicates some partial $Si=N$ bond as shown in the D2 structure. For the D3 structure, the $r$(SiSi) and $r$(SiN) values of 2.317 and 1.602 Å are typical of single Si-Si and double $Si=N$ bonds, respectively, as shown in the structure. However, in the Q3 structure which has the same atom-to-atom connectivity as the D3 structure, the quartet electron spin arrangement causes significant changes in the bond distances. The obtained $r$(SiN) and $r$(SiSi) values of 1.676 and 2.274 Å suggest partial $Si=N$ and $Si=Si$ doubly bonded atoms. This is supported by NBO calculations were the natural population of valence electrons around N, Si and Si atoms are 5.71, 3.20 and 4.00, respectively.

The calculated first 10 electronic transitions from the ground state, $^2\Pi_g$, of the most stable isomer, symmetric linear SiNSi, are shown in Fig. 1(c). The electronic transition energies and their corresponding oscillator strengths are listed in Table S1 (See Support Information). It can be seen that these electronic transition are well below the IE of SiNSi (9.3 eV) [29], therefore the spectra shown in Fig. 1(c) should be predicted reasonably well.

### 3.2.4. $SiN_3$
The stable isomers of $SiN_3$ in the ground state are shown in Fig. 4. The most stable isomer is the doublet $(^2A')$ nonlinear structure ($Si=N-N=N$) which agrees with previous studies [37,42]. The N-N bond is more favored than N-Si bond, and this makes the quartet isomer Q2 the highest-energy structure. From the NBO calculations the natural population of valence electrons around the Si,

![](./images/811165001766141952_4.jpg)

Fig. 5. Calculated electronic transition spectra from the ground state to the first ten excited states for (a) $SiN_3$, (b) $Si_3N$, and (c) $Si_2N_2$ using TDDFT/B3LYP/6-311G(d).

![](./images/811165001766141952_5.jpg)

Fig. 4. Optimized ground-state structures of $SiN_3$ using B3LYP/6-311G(d). D1 denotes doublet isomer 1, Q1 denotes quartet isomer 1, and Q2 represents quartet isomer 2. The value below each isomer is their relative energy (kcal/mol) calculated with CCSD(T)/6-311G(d) while those within the bracket are calculated with B3LYP/6-311G(d).

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005

N, N and N atoms in the most stable structure (D1) are 3.00, 5.94,
4.93 and 5.00, respectively. This electron population strongly indi-
cates whole-number bond orders as shown in the structure. Using
the typical $r(N\equiv N)$, $r(N=N)$ and $r(N-N)$ values of 1.098, 1.133 and
$1.351\ \text{\AA}$ as found in $\text{N}_2$, $\text{HN}_3$ and $\text{C}_3\text{H}_4\text{N}_2$ molecules [40], the NN
bond length values of 1.342 and $1.179\ \text{\AA}$ shown in the D1 structure
are in good agreement with singly and doubly bonded N-N atoms,
respectively. Both D1 and Q1 have similar structure as hydrogen
azide [40] ($\text{H-N=N=N}$) whose middle and terminal $r(N=N)$ values
are 1.237 and $1.133\ \text{\AA}$, respectively. In the Q1 structure, the $r(\text{SiN})$
value of $1.725\ \text{\AA}$ agrees well with the typical Si-N single bond,
whilst the $r(\text{NN})$ values of 1.231 and $1.270\ \text{\AA}$ indicates a double
$N=N$ and a partial $N=N$ bond in comparison to hydrogen azide. A
natural population analysis of the valence electrons for the Q2
structure shows 2.57 for the Si atom, and $\sim$5.44 for each of the
three N atoms. This strongly supports the formation of a partial
bond with a bond order of $\sim$1.5 as shown in the structure. The pre-
dicted electronic transition spectra including the first 10 excited
states from the doublet $^2A'$ electronic ground state structure
($\text{Si=N-N=N}$) is shown in Fig. 5(a). The transition energy to the
10th excited state at 4.70 eV is below the calculated IE value for
$\text{Si=N-N=N}$ of 7.81 eV at the CCSD(T)/6-311G(d) level The data
for this plot is shown in Table S1 (See Support Information).

### 3.2.5. $\text{Si}_3\text{N}$
Four stable isomers, all of $C_{2v}$ symmetry, were found for the
ground state of $\text{Si}_3\text{N}$, as illustrated in Fig. 6. For the D1 structure,
the $r(\text{Si-N})$ values of 1.766 and $1.780\ \text{\AA}$ are typical of singly
bonded Si and N atoms as previously explained, and the $r(\text{Si-Si})$
value of $2.410\ \text{\AA}$ indicates a slightly extended singly bonded silicon
atoms. Similarly, the $r(\text{Si-Si})$ value of $2.427\ \text{\AA}$ for the D2 structure
is $4.6\%$ longer than typical Si-Si single bonds in $\text{Si}_2\text{H}_6$ molecule
[40], and we attribute this to the strong electronegativity of N that
pulls electrons onto itself, and therefore leads to the extension in
the Si-Si single bond. The $r(\text{Si-N})$ value of $1.718\ \text{\AA}$ indicates a
slightly enhanced Si-N single bond. For the quartet structures,
the $r(\text{Si=N})$ value of $1.681\ \text{\AA}$ for the Q1 geometry indicates a BO
of $\sim$1.5. This is supported by valence electron population of 6.50
around the N atom from our NBO calculation. The $r(\text{Si-Si})$ value
of $2.525\ \text{\AA}$ is $\sim$8.8% longer than typical Si-Si single bonds [40],
and this indicates a loose Si-Si bond connection. The Q2 structure
is similar to the D1 structure in terms of atom-to-atom connectiv-
ity and bond distances, and the $r(\text{Si-N})$ values of 1.769 and $1.782\ \text{\AA}$
all indicate they are singly bonded Si and N atoms. However, the $r$
(Si-Si) value of $2.397\ \text{\AA}$ shows an extended Si-Si single bond since
it is $\sim$3.3% longer than a typical single bond [40].

The most stable isomer of $\text{Si}_3\text{N}$ is the doublet D1 which has the
Si in the center of three N formed triangle. However, D1 isomer
doesn't have a $D_{3\text{h}}$ point group and it adopts a $C_{2\text{v}}$ point group with
$^2B_1$ as the electronic ground state. This special configuration is
believed to be caused by Jahn-Teller effect [31]. The difference
between D1 and D2 isomers is 5.0 kcal/mol by CCSD(T)/6-311G
(d), and only 1.4 kcal/mol by B3LYP/6-311G(d). It is worth men-
tioning that a previous theoretical study at the MP2/6-311+G* level
by Goldberg et al. [31] found our D1 structure (Y-type) to lie
2.2 kcal/mol higher in energy relative to their global minimum
structure (T-type - which is similar to our D2 structure but with
a larger $\angle\text{SiNSi}$ value of $155.4^\circ$). However, our calculations both
at the B3LYP/6-311G(d) and CCSD(T)/6-311G(d) levels of theory
indicates D1 as the global minimum structure. As stated earlier,
our geometries were optimized at the DFT/B3LYP/6-311G(d) level,
and their energies were determined with MP2/6-311G*. This may
be the reason for the different global minimum structure obtained
in this work relative to the work of Goldberg et al. [31]

The predicted first 10 electronic transitions from the ground
state, $^2B_1$, of the D1 geometry up to 2.53 eV, which is well below
our calculated IE of 6.43 eV at the CSSD(T)/6-311G(d), is shown
in Fig. 5(b). The data for all the transitions in Fig. 5(b) is given in
Table S1 (See Support Information).

### 3.2.6. $\text{Si}_2\text{N}_2$
The optimized ground state geometries for 15 stable isomers of
$\text{Si}_2\text{N}_2$ are shown in Fig. 7. For the S1 structure, the $r(\text{SiN})$ value of
$1.590\ \text{\AA}$ is typical of a $\text{Si=N}$ bond as discussed in previous sections.

![](./images/811165001766141952_6.jpg)

Fig. 6. Optimized structures of $\text{Si}_3\text{N}$ using B3LYP/6-311G(d). D1 denotes doublet isomer 1, Q1 denotes quartet isomer 1, and so on. The value below each isomer is their
relative energy (kcal/mol) calculated with CCSD(T)/6-311G(d) while those within the bracket are calculated with B3LYP/6-311G(d).

![](./images/811165001766141952_7.jpg)

Fig. 7. The optimized singlet and triplet isomers of $Si_2N_2$ calculated with the CCSD(T)/6-311G(d) method. The energy (kcal/mol) values are given under the structures. The energy values in brackets were calculated with B3LYP/6-311G(d).

Unlike the asymmetric $Si-N=N$ structure of $SiN_2$ where the $r$ ($N=N$) was compared to the asymmetric $CH_2N=N$ molecule [40], here, we compare the $r$(NN) value of $1.264$ Å of the symmetric S1 geometry ($Si=N=N=Si$) to $1.252$ Å of the symmetric structure of trans-diazine ($H-N=N-H$) [40]. This shows that our calculated $r$ ($N=N$) agrees with a bond order of 2. Our calculated $r$(Si-N) value of $1.761$ Å for S2, and $1.731$ Å for S4 structures are typical of Si-N singly bonded atoms [28] as shown. The terminal $Si=N$ bonds of S3 geometry agree with a bond order of 2 whilst the central $r$(N=Si) value of $1.669$ Å suggests a partial $N=Si$ bond. This is supported by natural population of 6.67 and 2.41 valence electrons around the middle N and Si atoms according to our NBO calculation. For the S5 structure, the $r$(Si=N) and $r$(N-N) values of 1.605 and $1.374$ Å are typical of double $Si=N$ and single $N-N$ bonds, respectively, whilst the other terminal $r$(N=Si) value of $1.681$ Å indicates a partial $N=Si$ bond. For the S6 structure, the $r$(Si-Si) and $r$(Si-N) values of $2.255$ and $1.845$ Å are all typical single bonds, but the terminal $r$(N$\equiv$N) value of $1.125$ Å indicates a partial bond between doubly and triply bonded nitrogen-nitrogen atoms. The $r$(Si-Si) and $r$(Si-N) values of $2.330$ and $1.885$ Å for the staggered cyclic symmetric S7 structure agree with typical Si-Si and Si-N single bonds, whilst the $r$(N=N) value of $1.253$ Å agrees with doubly bonded $N=N$ atoms in comparison to $r$(N=N) of $1.252$ Å of symmetric trans-diazine ($H-N=N-H$) [40]. The $r$(Si=N) and $r$(Si-Si) values of $1.573$ and $2.330$ Å for the S8 structure agrees well with BO of 2 and 1, respectively.

The triplet T1 and T2 structures have very similar geometries with a small deviation in their $r$(Si-N) values which agrees with typical Si-N single bond. The $r$(Si-Si) for T1 and T2 are $2.417$ and $2.816$ Å, respectively, and this accounts for a Si-Si single bond in T1 whilst there is no such bond connectivity for the T2 structure. These two structures are separated by only 2.6 kcal/mol. For the T3 structure the terminal $r$(Si=N) value of $1.586$ Å indicates a bond order of 2, whilst the rest of the bonds show partial bonding character between single and double bonds. Similarly, for the T4 structure the terminal $r$(Si-N) bonds suggest single bonds whilst the $r$ ($N=N$) value of $1.249$ Å agrees with a double bond as previously discussed for the S7 structure of $Si_2N_2$. For the symmetric T5 structure, the terminal $r$(SiN) values of $1.670$ Å indicates a partial bond order of $\sim$1.5, and the $r$(N=N) value of $1.203$ Å deviates slightly from a typical symmetric $r$(N=N) value of $1.252$ Å towards a $r$ ($N\equiv$N) value of $1.098$ Å. This is supported by our NBO calculation where the population of valence electrons for the Si and N atoms were 3.40 and 5.52, respectively. This confirms the partial BO between the terminal Si and N atoms, as well as the deviation observed in the $N=N$ bond length. The difference in energy between T4 and T5 structures is only 1.3 kcal/mol at the CCSD (T)/6-311G(d) level. Similarly, for the symmetric NSiSiN triplet structure (T7), the terminal $r$(N=Si) value of $1.640$ Å indicates a partial BO of $\sim$1.5, whilst the central $r$(SiSi) value of $2.129$ Å is in good agreement with doubly bonded Si atoms [41]. It is worth mentioning that both T5 and T7 structures are linear symmetric with the major difference being the central bond as $N=N$ and $Si=Si$, respectively. This difference accounts for the T7 isomer lying $\sim$3 times higher in energy than the T5 structure, and it underscores the fact that Si-Si bonding is very unfavorable. The $r$(Si-N) values of $1.775$ and $1.780$ Å, and $r$(N-N) value of $1.373$ Å shown in the T6 structure are all typical single bonds distances.

Aside from the geometry of all stable isomers, Fig. 7 also shows the relative energies of all singlet and triplet isomers of $Si_2N_2$ calculated at the CCSD(T)/6-311G(d) level. As observed in Fig. 7, the low-spin isomers are generally more stable than the high-spin isomers. Out of the 15 stable isomers, the most stable one is the singlet $^1\Sigma_g^+$ symmetric linear $Si=N=N=Si$ structure (S1). The

<table><caption>Table 8
The largest T2 amplitudes for the stable ground-state isomers of SinNm (n + m ≤ 4) clusters calculated at CCSD(T)/6-311G(d).</caption>
<tbody><tr><th colspan="2">SiN</th><th colspan="2">SiN2</th><th colspan="2">Si2N</th><th colspan="2">SiN3</th><th colspan="2">Si3N</th><th colspan="2">Si2N2</th></tr><tr><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td><td>Isomer</td><td>T2</td></tr><tr><td>D1ª</td><td>0.17</td><td>S1ª</td><td>0.14</td><td>D1ª</td><td>0.13</td><td>D1ª</td><td>0.12</td><td>D1ª</td><td>0.12</td><td>S1ª</td><td>0.05</td><td>T1ª</td><td>0.11</td></tr><tr><td></td><td></td><td>S2</td><td>0.11</td><td>D2</td><td>0.07</td><td>Q1</td><td>0.11</td><td>D2</td><td>0.11</td><td>S2</td><td>0.07</td><td>T2</td><td>0.12</td></tr><tr><td></td><td></td><td>S3</td><td>0.26</td><td>D3</td><td>0.25</td><td>Q2</td><td>0.14</td><td>Q1</td><td>0.07</td><td>S3</td><td>0.07</td><td>T3</td><td>0.11</td></tr><tr><td></td><td></td><td>T1</td><td>0.10</td><td>Q1</td><td>0.18</td><td></td><td></td><td>Q2</td><td>0.09</td><td>S4</td><td>0.15</td><td>T4</td><td>0.13</td></tr><tr><td></td><td></td><td>T2</td><td>0.27</td><td>Q2</td><td>0.14</td><td></td><td></td><td></td><td></td><td>S5</td><td>0.09</td><td>T5</td><td>0.13</td></tr><tr><td></td><td></td><td>T3</td><td>0.19</td><td>Q3</td><td>0.16</td><td></td><td></td><td></td><td></td><td>S6</td><td>0.14</td><td>T6</td><td>0.16</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>S7</td><td>0.15</td><td>T7</td><td>0.24</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>S8</td><td>0.11</td><td></td><td></td></tr><tr><td colspan="14">ª Refer to the text for all the labels of various isomers.</td></tr></tbody></table>

highest-energy isomer in the singlet state is S8 (N=Si−Si=N) which has two Si atoms in the center and two N on the opposite sides. This arrangement provides further support that the Si−Si bond is highly unfavorable. S7 and S8 are the only singlet structures that are less stable than the lowest-energy triplet structure (T1) which is largely due to the unfavorable Si-Si bonding interaction. Similarly, the least stable triplet isomer is the symmetric linear N=Si=Si=N structure (T7) at 148.3 kcal/mol higher than the global minimum geometry (S1).

The predicted excited state transition spectra from the $^1\Sigma_g^+$ electronic ground state of the S1 geometry (Si=N=N=Si) up to the 10th excited state at 4.83 eV, which is below our calculated IE value of 7.85 eV at the CCSD(T)/6-311G(d) level, is shown in Fig. 5(c). The corresponding data is listed in Table S1 (See Support Information).

The small silicon nitride clusters studied in this work could have substantial multireference character. To check this, we have analyzed the T2 amplitude for all stable ground-state isomers at the CCSD(T)/6-311G(d) level. The largest T2 amplitude for various isomers are reported in Table 8. From the table, it can be seen that with the exception of the S3 and T2 isomer of SiN2, the D3 isomer of Si2N, and the T7 isomer of Si2N2 which give the largest T2 amplitude of 0.26, 0.27, 0.25, and 0.24, respectively, the rest all had a value of less than 0.2. It should also be noted that the largest T2 amplitudes for the lowest-energy isomers for all six clusters studied in this work range from 0.05 to 0.17, but all below 0.2. Therefore, the application of the single reference CC and EOM CC methods to study the ground-state geometries and excitation spectra can give reasonably good results.

## 4. Conclusions

We have systematically explored several quantum mechanical calculation methods, functionals and basis sets to calculate the ground-state geometry and harmonic vibrational frequencies of the diatomic and triatomic silicon nitride clusters, i.e., SiN, SiN2 and Si2N, as our benchmark systems. The methods studied included MP2, BD, CCSD, and DFT. It was determined that all tested methods gives good Si−N bond length ($r_e$) and vibrational frequency ($\omega_e$) values in agreements with the experimental results for the SiN cluster when large basis sets are used. However, we found DFT method with the best performed functional, B3LYP, has a unique advantage of both accuracy and efficiency. Many basis sets were tested with the different methods mentioned above. For 6-31G and 6-311G, the addition of diffuse functions was found not to improve accuracy, and the addition of one d polarization function was sufficient to give optimal results. Overall, the 6-311G(d) basis set performed better under most of the methods studied. For the more expensive Dunning's correlation consistent (CC) basis sets investigated, the difference in the performances of cc-PVDZ, cc-PVTZ, and cc-PVQZ is not significant. From the 11 functionals tested with the DFT method, B3LYP and B3PW91 were chosen for its best balanced accuracy in calculating the $r_e$ and $\omega_e$ values in SiN. From the benchmark study on SiN, DFT/B3LYP, DFT/B3PW91 and CCSD methods were selected along with the basis sets of 6-31G(d), 6-311G(d), cc-PVTZ, and aug-cc-PVTZ to examine SiN2 and Si2N. It was determined that DFT methods with B3LYP and B3PW91 functionals performed better in predicting the vibrational frequencies of SiN2. For Si2N, both DFT/B3LYP and CCSD provided good agreements with the experimental values. In the end, DFT/B3LYP/6-311G(d) achieves the best balance between accuracy and efficiency for geometry optimization and the calculations of the vibrational frequencies in the ground states of SiN, SiN2 and Si2N, and it is the method of choice used for optimizing the ground-state geometry of all small SinNm (n + m ≤ 4) clusters. The energies of all stable ground-state isomers were then determined by CCSD(T)/6-311G(d). We also performed NBO analysis to support the obtained bond distances and bond orders in the ground-state structures.

TDDFT/B3LYP and EOM-CCSD were used to calculate the electronic transitions from the ground state to different excited states. Different basis sets were tested with these two methods. For SiN, TDDFT/B3LYP outperformed EOMCCSD in predicting all three electronic transitions: $A^2\Pi \leftarrow X^2\Sigma^+$, $B^2\Sigma^+ \leftarrow X^2\Sigma^+$, and $D^2\Pi \leftarrow X^2\Sigma^+$, that have experimental values for comparison. Due to the limited experimental data available, it is hard to claim which of TDDFT/B3LYP and EOMCCSD performed better for SiN2 and Si2N. Considering its good performance in SiN and its efficiency, TDDFT/B3LYP/6-311G(d) was selected to calculate the excited state calculations.

At the B3LYP/6-311G(d) level, the most stable isomer for SiN2, Si2N, and SiN3 was determined to be the triplet ($X^3\Sigma^-$) asymmetric linear structure (Si−N=N), the doublet ($^2\Pi_g$) symmetric linear structure (Si=N=Si), and the doublet ($^2A'$) nonlinear structure (Si=N−N=N), respectively. These are in agreements with previous studies. For Si3N, we determined a Y-type structure (C2v) as the global minimum, which is different from a previous study showing a T-type structure as the most stable one at the MP2/6-311+G* level. A total of 15 stable isomers were obtained for Si2N2 in its ground state, and the singlet ($^1\Sigma_g^+$) symmetric linear structure (Si=N=N=Si) was determined as the global minimum. An examination of the relative energies of various stable isomers suggests a bonding tendency of N−N > N−Si > Si−Si. The unfavorable Si−Si bonding always leads to an increased energy in the isomer. The first 10 electronic transitions for the most stable isomers of all small silicon nitride clusters (SinNm, n + m ≤ 4) were also calculated using TDDFT/B3LYP/6-311G(d). The results in this study will be useful to guide future experiments that seek to understand the chemistry, structure, and bonding of these small silicon nitride clusters, which have received special interest due to their importance to various fields of applications including deposition of silicon nitride thin films, and astrophysics.

The largest T2 amplitudes for the most stable isomers of all six clusters studied in this work fall below 0.2. However, due to the nature of these molecules, the use of completely renormalized

EOMCC methods and multireference configuration interaction (MRCI) will be considered in the future to compare with the results presented in this work.

## Acknowledgment
This work was funded by the Natural Sciences and Engineering Research Council of Canada. The authors thank Compute Canada for providing the access to computing facilities in WestGrid. YW would like to thank Mitacs Globalink Program for a Globalink Research Internship.

## Appendix A. Supplementary material
Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.jms.2016.08.005.

## References
[1] K. Sardar, R. Bounds, M. Carravetta, G. Cutts, J.S.J. Hargreaves, A.L. Hector, J.A. Hriljac, W. Levason, F. Wilson, Dalton Trans. 45 (2016) 5765-5774, http://dx.doi.org/10.1039/c5dt04961j.
[2] R.N. Katz, Science 208 (1980) 841-847, http://dx.doi.org/10.1126/science.208.4446.841.
[3] S. Jin, L. Xu, H. Zhang, Y. Li, IEEE Photon. Technol. Lett. 28 (2016) 736-739, http://dx.doi.org/10.1109/LPT.2015.2507136.
[4] D.J. Brugh, M.D. Morse, Chem. Phys. Lett. 267 (1997) 370-376, http://dx.doi.org/10.1016/S0009-2614(97)00108-5.
[5] F.R. Ornellas, S. Iwata, J. Phys. Chem. 100 (1996) 10919-10927, http://dx.doi.org/10.1021/jp960255s.
[6] Y. Zhu, B. Li, G. Ye, Comput. Theor. Chem. 1017 (2013) 162-167, http://dx.doi.org/10.1016/j.comptc.2013.05.012.
[7] K. Jackson, G. Jungnickel, T. Frauenheim, Chem. Phys. Lett. 292 (1998) 235-242, http://dx.doi.org/10.1016/S0009-2614(98)00640-X.
[8] C.D. Valentin, G. Palma, G. Pacchioni, J. Phys. C 115 (2011) 561-569, http://dx.doi.org/10.1021/jp106756f.
[9] R.P. Vedula, N.L. Anderson, A. Strachan, Phys. Rev. B 85 (2012) 205209, http://dx.doi.org/10.1103/PhysRevB.85.205209.
[10] D.S.L. Mui, H. Liaw, A.L. Demirel, S. Strite, H. Morkoç, Appl. Phys. Lett. 59 (1991) 2847-2849, http://dx.doi.org/10.1063/1.105853.
[11] I.N. Mihailescu, A. Lita, V.S. Teodorescu, A. Luches, M. Martino, A. Perrone, M. Gartner, J. Mater. Sci. 31 (1996) 2839-2847, http://dx.doi.org/10.1007/BF00355991.
[12] J.M. Lackner, W. Waldhauser, R. Ebner, M. Beutl, G. Jakopic, G. Leising, H. Hutter, M. Rosner, Appl. Phys. A 79 (2004) 1525-1527, http://dx.doi.org/10.1007/s00339-004-2838-0.
[13] P.R. Bunker, R. Guérout, Z.J. Jakubek, P. Jensen, S.N. Yurchenko, J. Mol. Struct. 795 (2006) 9-13, http://dx.doi.org/10.1016/j.molstruc.2006.02.014.
[14] S.C.J. Foster, Mol. Spectros. 137 (1989) 430-431, http://dx.doi.org/10.1016/0022-2852(89)90185-9.
[15] C. Naulin, M. Costes, Z. Moudden, N. Ghanem, G. Dorthe, Chem. Phys. Lett. 202 (1993) 452-458, http://dx.doi.org/10.1016/0009-2614(93)90069-D.
[16] M. Elhanine, B. Hanoune, G. Guelachvili, C.J. Amiot, Phys. II France 2 (1992) 931-938, http://dx.doi.org/10.1051/jp2:1992176.
[17] L.E. Hintzsche, C.M. Fang, T. Watts, M. Marsman, G. Jordan, M.W.P.E. Lamers, A. W. Weeber, G. Kresse, Phys. Rev. B 86 (2012) 235204, http://dx.doi.org/10.1103/PhysRevB.86.235204.

[18] F.R. Ornellas, S. Iwata, J. Phys. Chem. 100 (1996) 16155-16161, http://dx.doi.org/10.1021/jp961432s.
[19] A.C. Borin, Chem. Phys. Lett. 262 (1996) 80-86, http://dx.doi.org/10.1016/0009-2614(96)01061-5.
[20] D. Clement, H. Mutschke, R. Klein, C. Jäger, J. Dorschner, E. Sturm, T. Henning, Astrophys. J. 621 (2005) 985, http://dx.doi.org/10.1086/426184/meta.
[21] L.R. Nittler, P. Hoppe, C.M.O.d. Alexander, S. Amari, P. Eberhardt, X. Gao, R.S. Lewis, R. Strebel, R.M. Walker, E. Zinner, Astrophys. J. Lett. 453 (1995) L25, http://dx.doi.org/10.1086/309743.
[22] M. Guélin, J. Cernicharo, C. Kahane, J. Gomez-Gonzalez, Astron. Astrophys. 157 (1986) L17-L20.
[23] B.E. Turner, in: P.D. Singh (Ed.), IAU Symposium No. 150, Astrochemistry of Cosmic Phenomena, 1992, http://dx.doi.org/10.1007/978-94-011-2761-5.
[24] P.J. Bruna, H. Dohmann, S.D. Peyerimhoff, Can. J. Phys. 62 (1984) 1508-1523, http://dx.doi.org/10.1139/p84-197.
[25] Z.L. Cai, J.M.L. Martin, J.P. François, R. Gijbels, Chem. Phys. Lett. 252 (1996) 398-404, http://dx.doi.org/10.1016/0009-2614(96)00183-2.
[26] S. Saito, Y. Endo, E. Hirota, J. Chem. Phys. 78 (1983) 6447-6450, http://dx.doi.org/10.1063/1.444682.
[27] R.R. Lembke, R.F. Ferrante, W. Weltner, J. Am. Chem. Soc. 99 (1977) 416-423, http://dx.doi.org/10.1021/ja00444a018.
[28] F.R. Ornellas, L.T. Ueno, S. Iwata, J. Chem. Phys. 106 (1997) 151-157, http://dx.doi.org/10.1063/1.473040.
[29] K.F. Zmbov, J.L. Margrave, J. Am. Chem. Soc. 89 (1967) 2492-2493, http://dx.doi.org/10.1021/ja00986a050.
[30] M. Iraqi, N. Goldberg, H. Schwarz, J. Phys. Chem. 97 (1993) 11371-11372, http://dx.doi.org/10.1021/j100146a004.
[31] N. Goldberg, M. Iraqi, H. Schwarz, A. Boldyrev, J. Simons, J. Chem. Phys. 101 (1994) 2871-2879, http://dx.doi.org/10.1063/1.467601.
[32] M.J. Frisch, G.W. Trucks, H.B. Schlegel, G.E. Scuseria, M.A. Robb, J.R. Cheeseman, G. Scalmani, V. Barone, B. Mennucci, G.A. Petersson, H. Nakatsuji, M. Caricato, X. Li, H.P. Hratchian, A.F. Izmaylov, J. Bloino, G. Zheng, J.L. Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J.A. Montgomery Jr., J.E. Peralta, F. Ogliaro, M.J. Bearpark, J. Heyd, E.N. Brothers, K.N. Kudin, V.N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A.P. Rendell, J.C. Burant, S.S. Iyengar, J. Tomasi, M. Cossi, N. Rega, N.J. Millam, M. Klene, J.E. Knox, J.B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R.E. Stratmann, O. Yazyev, A.J. Austin, R. Cammi, C. Pomelli, J.W. Ochterski, R.L. Martin, K. Morokuma, V.G. Zakrzewski, G.A. Voth, P. Salvador, J.J. Dannenberg, S. Dapprich, A.D. Daniels, Ö. Farkas, J.B. Foresman, J.V. Ortiz, J. Cioslowski, D.J. Fox, Gaussian, Inc., Wallingford, CT, USA, 2009.
[33] C. Yamada, E. Hirota, S. Yamamoto, S. Saito, J. Chem. Phys. 88 (1988) 46-51, http://dx.doi.org/10.1063/1.454627.
[34] C. Yamada, E. Hirota, J. Chem. Phys. 82 (1985) 2547-2552, http://dx.doi.org/10.1063/1.448304.
[35] I.S. Ignatyev, H.F. Schaefer, J. Phys. Chem. 96 (1992) 7632-7634, http://dx.doi.org/10.1021/j100198a027.
[36] H. Bredohl, I. Dubois, Y. Houbrechts, M. Singh, Can. J. Phys. 54 (1976) 680-688, http://dx.doi.org/10.1139/p76-076.
[37] G. Maier, H.P. Reisenauer, J. Glatthaar, Organometallics 19 (2000) 4775-4783, http://dx.doi.org/10.1021/om000234r.
[38] G. Meloni, S. Nunziante Cesaro, N. Sanna, Chem. Phys. Lett. 343 (2001) 113-118, http://dx.doi.org/10.1016/S0009-2614(01)00663-7.
[39] J.G. Radziszewski, P. Kaszynski, D. Littmann, V. Balaji, B.A. Hess, J. Michl, J. Am. Chem. Soc. 115 (1993) 8401-8408, http://dx.doi.org/10.1021/ja00071a057.
[40] NIST Computational Chemistry Comparison and Benchmark Database, NIST Standard Reference Database 101, Release 17b, September 2015.
[41] R. West, Angew. Chem. Inter. Ed. 26 (1987) 1201-1211, http://dx.doi.org/10.1002/anie.198712013.
[42] G. Jungnickel, T. Frauenheim, K.A. Jackson, J. Chem. Phys. 112 (2000) 1295-1305, http://dx.doi.org/10.1063/1.480681.

Please cite this article in press as: E. Owusu-Ansah et al., J. Mol. Spectrosc. (2016), http://dx.doi.org/10.1016/j.jms.2016.08.005