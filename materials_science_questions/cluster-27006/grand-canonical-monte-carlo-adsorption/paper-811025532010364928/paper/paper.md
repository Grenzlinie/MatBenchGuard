# The rotational dynamics of $\text{H}_2$ adsorbed in covalent organic frameworks$\dagger$

Tony Pham,$\ddagger^{a}$ Katherine A. Forrest,$\ddagger^{a}$ Matthew Mostrom,$^{a}$ Joseph R. Hunt,$\S^{b}$ Hiroyasu Furukawa,$^{c}$ Juergen Eckert$^{*\text{ad}}$ and Brian Space$^{*a}$

A combined inelastic neutron scattering (INS) and theoretical study was carried out on $\text{H}_2$ adsorbed in two covalent organic framework (COF) materials: COF-1 and COF-102. These COFs are synthesized from self-condensation reactions of 1,4-benzenediboronic acid (BDBA) and tetra(4-(dihydroxy)borylphenyl)methane (TBPM) molecules, respectively. Molecular simulations of $\text{H}_2$ adsorption in COF-1 revealed that the $\text{H}_2$ molecules occupy the region between two eclipsed layers of the COF. The most favorable $\text{H}_2$ binding site in COF-1 is located between two $\text{B}_3\text{O}_3$ clusters of the eclipsed layers. Two distinct $\text{H}_2$ binding sites were identified in COF-102 from the simulations: the $\text{B}_3\text{O}_3$ clusters and the phenyl rings of the tetraphenylmethyl units. Two-dimensional quantum rotation calculations for $\text{H}_2$ adsorbed at the considered sites in both COFs resulted in rotational transitions that are in good agreement with those that appear in the corresponding INS spectra. Such calculations were important for interpreting the INS spectra in these materials. Calculation of the rotational potential energy surface for $\text{H}_2$ bound at the most favorable adsorption site in COF-1 and COF-102 revealed unusually high rotational barriers that are attributed to the nature of the $\text{B}_3\text{O}_3$ rings. The values for these barriers to rotation are greater than or comparable to those observed in some metal-organic frameworks (MOFs) that possess open-metal sites. This study demonstrates the power of using INS experiments in conjunction with theoretical calculations to gain valuable insights into the nature of the binding sites and, for the first time, the rotational dynamics of $\text{H}_2$ adsorbed in COFs.

## I. Introduction

Molecular $\text{H}_2$ has long been considered as an energy carrier and a promising alternative to petroleum and diesel fuels to help mitigate the effects of global warming in the future. Indeed, the use of $\text{H}_2$ in a fuel cell releases no greenhouse gases into the atmosphere and generates about $120.7$ kJ $\text{g}^{-1}$ of energy, the highest of any known fuel.$^{1}$ While $\text{H}_2$ is not naturally abundant, it can be obtained readily through chemical processes such as the electrolysis of $\text{H}_2\text{O}$.$^{2}$ Despite this significant promise for energy-related applications, a number of complications exist that currently prevent the extensive use of $\text{H}_2$ as a fuel carrier. For example, $\text{H}_2$ interacts weakly with its surroundings under near-ambient conditions, which makes the storage of neat $\text{H}_2$ difficult. In addition, because $\text{H}_2$ exhibits very low energy density by volume, a massive tank is required for storage of the gas.

A possible solution for storing $\text{H}_2$ effectively is to use a chemical medium to interact more strongly with the gas. Metal hydrides have been shown to store a significant amount of $\text{H}_2$, but there are difficulties involved with releasing the gas and with regeneration of the medium.$^{3}$ As a result, such systems are unsuitable for on-board $\text{H}_2$ storage at this time. Porous materials that bind to molecular $\text{H}_2$ by physisorption appear to offer tremendous advantage as potential $\text{H}_2$ storage systems since they can adsorb a considerable amount of $\text{H}_2$ within the pores (albeit at rather low temperatures) and have the ability to release the gas straightforwardly through changes in the thermodynamic conditions.$^{4}$ Metal-organic frameworks (MOFs) are examples of such materials that could be promising for $\text{H}_2$ storage if binding energies were to improve.$^{5}$ MOFs represent a class of crystalline

---

$^{a}$ Department of Chemistry, University of South Florida, 4202 East Fowler Avenue, CHE205, Tampa, FL 33620-5250, USA. E-mail: brian.b.space@gmail.com, juergen@usf.edu  
$^{b}$ Center for Reticular Chemistry at the California NanoSystems Institute, Department of Chemistry and Biochemistry, University of California-Los Angeles, 607 Charles E. Young Drive East, Los Angeles, CA 90095, USA  
$^{c}$ Department of Chemistry, University of California-Berkeley, Materials Sciences Division, Lawrence Berkeley National Laboratory, Berkeley, CA, 94720, USA  
$^{d}$ Department of Chemistry and Biochemistry, Texas Tech University, 2500 Broadway, Box 41061, Lubbock, TX 79409-1061, USA  
$\dagger$ Electronic supplementary information (ESI) available: Details of electronic structure calculations, grand canonical Monte Carlo methods, and quantum rotation calculations, pictures of COF fragments, tables of properties, and simulated $\text{H}_2$ adsorption results. See DOI: 10.1039/c7cp00924k  
$\ddagger$ Authors contributed equally.  
$\S$ Current address: Naval Surface Warfare Center Dahlgen Division, 4045 Higley Road, Dahlgren, Virginia 22448, USA.

materials that are constructed from metal ions and organic ligands.⁶ The building block approach allows for the possibility to synthesize or envision a vast number of MOF structures with desired properties.⁷

Covalent organic frameworks (COFs) represent another class of porous crystalline materials that have been proposed to be excellent candidates for applications in H₂ storage.⁸,⁹ Like MOFs, COFs have rigid structures with permanent porosity and can be synthesized in forms with high surface areas.¹⁰,¹¹ Different COFs can be created by tuning the geometry and dimensions of the building blocks. In contrast to MOFs, however, COFs are composed of entirely light elements (H, B, C, N, and O) in which the structures are held together through strong covalent bonds (C-C, C-O, C-B, B-O). Because of this, COFs typically possess low densities and have high thermal stability. The majority of extant COFs are synthesized through condensation reactions of an organic molecule containing boronic acid functional groups.

COFs can be synthesized to have two- or three-dimensional structures depending on the building blocks used. In 2005, it was shown that the self-condensation reaction between 1,4-benzenediboronic acid (BDBA) molecules (Fig. 1(a)) resulted in a porous material known as COF-1.¹⁰ Here, the boronic acid groups of the BDBA molecules combine together to form planar six-membered boroxine (B₃O₃) rings, with H₂O being eliminated through dehydration. In essence, the structure of COF-1 consists of two-dimensional hexagonal sheets of phenylene groups connected to B₃O₃ rings in which adjacent layers are staggered with respect to each other (Fig. 2(a)). The structure of COF-1 is similar to that of graphite, with comparable distances for the interlayer spacing.¹² In addition, the structure of the COF is held together through van der Waals interactions between the phenyl groups and the B₃O₃ rings of adjacent layers.¹⁰

While COF-1 is an example of a two-dimensional COF, COF-102 represents one of the first reported three-dimensional COFs.¹³ In 2007, this COF was synthesized through a self-condensation

$$
\mathrm{(a)}\quad
\begin{matrix}
\mathrm{HO}-\mathrm{B}-\mathrm{OH} \\
\mid \\
\mathrm{C_6H_4} \\
\mid \\
\mathrm{HO}-\mathrm{B}-\mathrm{OH}
\end{matrix}
\quad\quad
\mathrm{(b)}\quad
\begin{matrix}
\mathrm{HO}-\mathrm{B}-\mathrm{OH} & & \mathrm{HO}-\mathrm{B}-\mathrm{OH} \\
\mid & & \mid \\
\mathrm{C_6H_4} & \mathrm{C(CH_4)} & \mathrm{C_6H_4} \\
\mid & & \mid \\
\mathrm{HO}-\mathrm{B}-\mathrm{OH} & & \mathrm{HO}-\mathrm{B}-\mathrm{OH}
\end{matrix}
$$

Fig. 1 (a) 1,4-benzenediboronic acid (BDBA) and (b) tetra(4-(dihydroxy)-borylphenyl)methane (TBPM) molecule used to synthesize COF-1 and COF-102, respectively.

![](./images/811025532010364928_1.jpg)

Fig. 2 Orthographic c-axis view of (a) the 2 × 2 × 4 system cell of COF-1 and (b) the unit cell of COF-102. In (a), the two layers are distinguished by light and dark shading. Atom colors: C = gray, H = white, O = red, B = pink.

reaction of tetra(4-(dihydroxy)borylphenyl)methane (TBPM) molecules (Fig. 1(b)). As with COF-1, the boronic acid groups of the TBPM molecules converge to form the B₃O₃ units. In the case of COF-102, however, the use of a tetrahedral building block facilitates the construction of a three-dimensional framework with C₃N₄ (ctn) topology.¹⁴ The unit cell of this COF is shown in Fig. 2(b).

The experimental H₂ adsorption isotherms and isosteric heat of adsorption ($Q_{\text{st}}$) values for COF-1 and COF-102 were reported for the first time in 2009.⁹ Prior to this experimental work, a number of theoretical studies were carried out on H₂ adsorption in COFs in order to evaluate the H₂ uptake capacity in these materials.⁸,¹⁵⁻¹⁷ The experimental studies reported in ref. 9 revealed that the H₂ uptake for COF-1 and COF-102 at 77 K/1 atm is approximately 10.9 and 11.1 mg g⁻¹, respectively.⁹ Because of the larger specific surface area and pore size of COF-102 compared to COF-1, the former exhibits much higher H₂ uptake capacity at saturation (72.4 vs. 14.8 mg g⁻¹). However, the H₂ $Q_{\text{st}}$ value at zero-coverage is greater for COF-1 (6.2 vs. 3.9 kJ mol⁻¹), presumably because of the smaller pore size for

this COF, which allows for greater concurrent interactions between the host and guest. The relative trends for the $H_2$ uptake and $Q_{st}$ for COF-1 and COF-102 have been supported through earlier executed modeling studies. $^{8}$

In this work, we report inelastic neutron scattering (INS) spectroscopic studies on $H_2$ adsorbed in COF-1 and COF-102 in order to obtain molecular level information on the binding sites in these materials. This has been previously accomplished for $H_2$ adsorbed in many porous materials, such as zeolites and MOFs. $^{18,19}$ To the best of our knowledge, this is the first report of INS spectra for $H_2$ adsorbed in COFs. Molecular simulations of $H_2$ adsorption in COF-1 and COF-102 were also carried out to identify the $H_2$ binding sites in both COFs and relate these to the observed INS spectra by means of two-dimensional quantum rotation calculations and the associated transitions. A rather high barrier to rotation is encountered by $H_2$ molecules located at the primary adsorption site in both COFs, which is greater than or comparable to those for $H_2$ adsorbed in some MOFs which contain open-metal sites. $^{20}$

## II. Methods
### A. Experimental section
COF-1 and COF-102 were synthesized and activated according to the procedure reported in ref. 10 and 13, respectively. The INS spectra for $H_2$ adsorbed in COF-1 and COF-102 were collected on the Quasi-Elastic Neutron Scattering (QENS) spectrometer at the Intense Pulsed Neutron Source (IPNS) of Argonne National Laboratory (ANL) using approximately 0.5 g each of both samples. For both COFs, adsorption of predetermined amounts of $H_2$ was carried out *in situ* at 77 K after first obtaining a spectrum of the "blank" sample. The samples were equilibrated after loading before cooling to the data collection temperature of 15 K.

### B. Theoretical section
Simulations of $H_2$ adsorption were performed in COF-1 and COF-102 using grand canonical Monte Carlo (GCMC) methods. $^{21}$ Additional details for executing the GCMC simulations are given in the ESI.$\dagger$ The $2 \times 2 \times 4$ system cell and unit cell was used for COF-1 and COF-102, respectively (Fig. 2). All COF atoms were treated with Lennard-Jones 12-6 parameters and point partial charges to model repulsion/dispersion and permanent electrostatic interactions, respectively. Thus, the total potential energy of the COF-$H_2$ system was computed through the sum of the Lennard-Jones potential and the Coulombic energy as calculated by Ewald summation$^{22,23}$ of the partial charges. More details of obtaining the simulation parameters for the COFs are provided in the ESI.$\dagger$ The $H_2$ molecule was modeled as a rigid five-site stationary electrostatic potential that was developed previously by Belof *et al.*$^{24}$

We normally include explicit many-body polarization interactions for classical simulations of gas adsorption in heterogeneous media. Such interactions have been shown to be important for the accurate modeling of $H_2$ adsorption in MOFs with open-metal sites. $^{25-29}$ However, COF-1 and COF-102 are materials that consist of only light atoms and do not possess open-metal sites. As a result, the contribution from polarization interactions was negligible for $H_2$ adsorption in these COFs. Simulations of $H_2$ adsorption in COF-1 and COF-102 with polarization included resulted in calculated $H_2$ adsorption isotherms that are very similar to those for the nonpolarizable potential within the respective COFs (Fig. S7 and S14, ESI$\dagger$). Furthermore, control simulations of $H_2$ adsorption were performed in both COFs using a single-site potential that includes only Lennard-Jones parameters. $^{30}$ The resulting isotherms are also similar to those obtained using the aforementioned electrostatic model (Fig. S7 and S14, ESI$\dagger$). This suggests that $H_2$ adsorption in these COFs is dominated by van der Waals interactions. Nevertheless, the five-site electrostatic potential was used here for the purposes of quantum rotation calculations for the linear adsorbate.

Two-dimensional quantum rotation calculations were carried out on $H_2$ bound at the considered sites in COF-1 and COF-102. More details of executing these calculations are provided in the ESI.$\dagger$ We have successfully utilized this method to accurately calculate the rotational transitions for $H_2$ adsorbed at specific sites in various porous materials. $^{19}$ We also calculated the rotational potential energy surface (PES) for $H_2$ adsorbed at the primary binding site in both COFs to estimate the rotational barrier that is imposed on the adsorbate molecules. The rotational PES was generated by calculating the total potential energy of the COF-$H_2$ system as the $H_2$ molecule was rotated at various angles of $\theta$ (0-180$^\circ$) and $\phi$ (0-360$^\circ$), with its center-of-mass kept fixed. The barrier to rotation corresponds to the maximum on the rotational PES, which is projected onto a sphere consisting of 4096 single point energies based on $64 \times 64$ Gaussian quadrature integration$^{31}$ in this work.

## III. Results and discussion
The INS spectra for $H_2$ adsorbed in COF-1 at two different loadings (0.3 and 0.7 mmol $H_2$) are shown in Fig. 3. We expect that the peak at about 8.5 meV in the INS spectra for COF-1 should represent the lowest energy transition observed and be associated with the most favorable $H_2$ binding site in the material. This transition energy is less than that for some MOFs that possess open-metal sites, such as HKUST-1 (9.1 meV). $^{32}$ It is also comparable to that for Zn-MOF-74, which contains exposed $Zn^{2+}$ ions, $^{33}$ as INS measurements of $H_2$ adsorbed in this MOF found the rotational tunnelling transition at 8.3 meV for the $Zn^{2+}$-$H_2$ interaction. $^{34}$ The INS spectra for both loadings also have a number of peaks above 10 meV (*e.g.*, *ca.* 12.2 and 13.4 meV). These peaks most likely correspond to $H_2$ binding at weaker adsorption sites in the COF. The aforementioned assumptions of the nature of the peaks in the INS spectra for COF-1 will be supported later through two-dimensional quantum rotation calculations.

In the INS spectra for COF-1, small peaks can be observed for both loadings at approximately 3.2 and 6.6 meV, which could suggest for the presence of very strong $H_2$ binding sites in

![](./images/811025532010364928_2.jpg)

Fig. 3 Inelastic neutron scattering (INS) spectra for $H_2$ in COF-1 at different loadings: 0.3 mmol $H_2$ (red) and 0.7 mmol $H_2$ (black). The spectra were collected on the QENS spectrometer at IPNS/ANL at a temperature of 15 K.

the COF. We note that rotational tunneling transitions that occur at lower neutron transfer energies correspond to a higher barrier to rotation for the adsorbate, and therefore a stronger interaction with the host. $^{18,19}$ These two peaks, however, appear to be invariant to loading, and hence may originate from $H_2$ riding on framework vibrational modes. The molecular simulations described below indeed show that there are only limited $H_2$ adsorption sites available in COF-1.

Fig. 4 shows the INS spectrum for 2 mmol $H_2$ adsorbed in COF-102. This spectrum has two relatively pronounced features: a distinct peak at about 11.5 meV; and a peak near 14.7 meV, which corresponds to the rigid rotor limit for free (or unhindered) $H_2$ as well as the $j = 0$ to $j = 1$ para-to-ortho transition. Otherwise, the spectrum contains a number of very weak peaks at lower energies. Our molecular simulations have identified two well-defined $H_2$ binding sites in COF-102, which may account for some of the features in the INS spectrum for this COF.

Molecular simulations were performed in COF-1 and COF-102 to identify the $H_2$ binding sites in the respective COFs.

![](./images/811025532010364928_3.jpg)

Fig. 4 Inelastic neutron scattering (INS) spectrum for $H_2$ in COF-102 at a loading of 2 mmol $H_2$. The spectrum was collected on the QENS spectrometer at IPNS/ANL at a temperature of 15 K.

GCMC simulations of $H_2$ adsorption in both COFs at 77 and 87 K and low pressures (up to 1.1 atm) resulted in isotherms that notably overestimate the corresponding experimental results$^9$ using the classical force field that was established in this work (Fig. S4 and S11, ESI$\dagger$). This oversorption relative to experiment is consistent with what was observed in past computational studies of $H_2$ adsorption in these COFs.$^{8,35}$

The simulations executed herein produced an excess adsorption isotherm that overestimates experiment at 77 K and high pressures (up to 90 atm) in COF-1 (Fig. S6, ESI$\dagger$). The simulated high pressure $H_2$ adsorption isotherm at 77 K in COF-1 as reported by Han et al. is also much higher than experiment for all pressures considered (Fig. S6, ESI$\dagger$).$^8$ In the case of COF-102, our simulations generated an excess adsorption isotherm that is in acceptable agreement with experiment under high pressures conditions at 77 K (Fig. S13, ESI$\dagger$). On the other hand, the simulated isotherm obtained by Han et al. for this COF within the same thermodynamic region notably deviate from experiment starting at around 30 atm (Fig. S13, ESI$\dagger$).$^8$ We note that this work and the theoretical study reported in ref. 8 utilized different force fields for the $H_2$ adsorption simulations in these COFs, which could explain the variations in the simulated results between the two studies. Specifically, the latter utilized an ab initio force field, whereas the potential energy function for the former is completely classical.

Our GCMC simulations demonstrate that $H_2$ adsorption in COF-1 and COF-102 is dominated by repulsion/dispersion interactions. The observed oversorption compared with experiment at 77 and 87 K and low pressures for both COFs (Fig. S4 and S11, ESI$\dagger$) can be attributed to the type of repulsion/dispersion parameters that were assigned to the COF atoms. Particularly, all atoms of the adsorbent were assigned Lennard-Jones parameters from known general purpose force fields (see ESI$\dagger$ for details)$^{36,37}$ as commonly done for simulations of gas adsorption in porous materials.$^{38}$ This is demonstrated by the fact that simulations using a single-site model which includes only Lennard-Jones parameters$^{30}$ generated isotherms that oversorb relative to experiment for both COFs (Fig. S7 and S14, ESI$\dagger$).

We note that previously reported COF-$H_2$ simulation studies also produced isotherms that overestimated the experimental results.$^{8,35}$ It is expected that the choice of van der Waals parameters that were used to treat the COF atoms contributed to the observed oversorption in these studies. Future work should focus on obtaining better repulsion/dispersion parameters for COFs in order to generate simulated isotherms in better agreement with experimental measurements. Such efforts are in fact ongoing in our group. Despite simulated $H_2$ adsorption isotherms that overestimate experiment within the low-pressure region for COF-1 and COF-102, we nonetheless calculated rotational transitions that are in very good experiment with the transitions observed in the corresponding INS spectra for $H_2$ adsorbed at the considered sites as described later. Thus, we believe that our prediction of the favorable $H_2$ binding sites in both COFs is still accurate.

$H_2$ adsorption in both COFs were also measured at 298 K and high pressures. While the data for COF-1 was affected by some experimental errors, the experimental absolute and excess

$\ce{H_{2}}$ adsorption isotherm for COF-102 at room temperature are shown in the ESI† (Fig. S15). The absolute and excess $\ce{H_{2}}$ uptakes at 298 K/85 bar were measured to be 17.1 and 7.0 mg g⁻¹, respectively. Simulations of $\ce{H_{2}}$ adsorption were also performed in both COFs at 298 K and pressures up to 100 atm and the resulting isotherms are displayed in the ESI† (Fig. S8 and S15). Our GCMC simulations predict an absolute/excess $\ce{H_{2}}$ adsorption capacity of 6.3/3.7 and 20.7/7.0 mg g⁻¹ for COF-1 and COF-102, respectively. Interestingly, the simulations generated $\ce{H_{2}}$ adsorption isotherms that are in very good agreement with experiment under these conditions for COF-102 (Fig. S15, ESI†).

The $\ce{H_{2}}$ $Q_{\text{st}}$ values obtained from our GCMC simulations for COF-1 and COF-102 were approximately 7.9 and 3.9 kJ mol⁻¹, respectively, for all loadings considered (Fig. S5 and S12, ESI†). Although the theoretical $\ce{H_{2}}$ $Q_{\text{st}}$ values in COF-102 are in good agreement with experiment for the considered loading range (Fig. S12, ESI†), they are nonetheless higher than experiment for COF-1 (Fig. S5, ESI†). The experimental zero-loading $\ce{H_{2}}$ $Q_{\text{st}}$ values for COF-1 and COF-102 are 6.2 and 3.9 kJ mol⁻¹, respectively.⁹ While the experimental $Q_{\text{st}}$ values for both COFs were obtained by applying the virial method³⁹,⁴⁰ to the measured low pressure isotherms at 77 and 87 K, the theoretical values were obtained through fluctuations of the particle number and total potential energy of the COF–$\ce{H_{2}}$ system in GCMC simulation.⁴¹ *Han et al.* obtained simulated initial $\ce{H_{2}}$ $Q_{\text{st}}$ values of 8.8 and 5.7 kJ mol⁻¹, for COF-1 and COF-102, respectively, using the fluctuation formula.⁸

According to our molecular simulations, the $\ce{H_{2}}$ molecules were found to adsorb at one principal location in COF-1 and that is the area between two eclipsed layers of the material (see ESI,† Fig. S9). We note that the region between two directly adjacent layers, which are staggered with respect to each other, is inaccessible for adsorbate binding. Next, we performed simulated annealing calculations⁴² on a single $\ce{H_{2}}$ molecule in the COF-1 system cell within the canonical ensemble (*NVT*) to identify the most favorable $\ce{H_{2}}$ adsorption site in the COF. It was discovered that the global minimum for $\ce{H_{2}}$ in COF-1 corresponds to binding between two $\ce{B_{3}O_{3}}$ clusters of the eclipsed layers (Fig. 5). Here, each positively charged H atom of the $\ce{H_{2}}$ molecule can interact favorably with the negatively charged O atom of the $\ce{B_{3}O_{3}}$ rings. This binding site for $\ce{H_{2}}$ in COF-1 is consistent with what was observed in an earlier *ab initio* study of $\ce{H_{2}}$ adsorbed in the COF.¹⁷

![](./images/811025532010364928_4.jpg)

Fig. 5 Molecular illustration of an adsorbed $\ce{H_{2}}$ molecule between two $\ce{B_{3}O_{3}}$ clusters of eclipsed layers in COF-1 as determined from simulated annealing calculations. The adsorbate molecule is shown in orange. The middle layer, which is staggered with respect to the top and bottom layers, is darkened for clarity. The $\ce{O-H(H_{2})}$ distances are also displayed. Atom colors: C = gray, H = white, O = red, B = pink.

The rotational energy levels determined from two-dimensional quantum rotation calculations for $\ce{H_{2}}$ adsorbed at the most favorable binding site in COF-1 are given in Table 1. We note that, while sections of the COF structure are depicted in Fig. 5 to illustrate the binding site, the calculations were performed within the complete $2\times2\times4$ system cell of the material. The lowest $j = 0$ to $j = 1$ transition for $\ce{H_{2}}$ adsorbed at this site in COF-1 was calculated to be 8.61 meV. This value is in excellent agreement with the peak occurring at approximately 8.5 meV in the INS spectra for the COF (Fig. 3). We can thereby assign this peak to $\ce{H_{2}}$ adsorbing at the most favorable binding site in COF-1 on the basis of our quantum rotation calculations. This in turn suggests that the peaks occurring at lower energies do not correlate to rotational excitations from $\ce{H_{2}}$ molecules adsorbed in the framework.

Table 1 Calculated two-dimensional quantum rotational levels for a $\ce{H_{2}}$ molecule adsorbed at the most favorable adsorption site in COF-1 as depicted in Fig. 5. The energies are given relative to $E_{1}$, which is $-70.66$ meV

<table>
<thead>
<tr>
<th>$n$</th>
<th>$j$</th>
<th>$\Delta E$ (meV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0.00</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>8.61</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>15.56</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>24.09</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>40.09</td>
</tr>
<tr>
<td>6</td>
<td>2</td>
<td>40.42</td>
</tr>
<tr>
<td>7</td>
<td>2</td>
<td>45.93</td>
</tr>
<tr>
<td>8</td>
<td>2</td>
<td>50.88</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>54.04</td>
</tr>
</tbody>
</table>

According to our simulations, some $\ce{H_{2}}$ molecules were also found to adsorb in the vicinity of the $\ce{H_{2}}$ that is localized at the most favorable binding site in COF-1. A view of the COF-1 system cell showing the sites of $\ce{H_{2}}$ occupancy in the material is displayed in Fig. S9 (ESI†). It can be observed that a number of $\ce{H_{2}}$ molecules populate the area between two eclipsed layers of the COF and do not necessarily interact with the $\ce{B_{3}O_{3}}$ rings. Such adsorbate molecules are likely the origin of the peaks appearing above 10 meV in the INS spectra for the COF at both loadings. In order to verify this, we performed two-dimensional quantum rotation calculations for selected $\ce{H_{2}}$ molecule positions that were obtained from equilibrated GCMC simulations of $\ce{H_{2}}$ adsorption in the system at 77 K/1.1 atm. The calculations produced $j = 0$ to $j = 1$ transitions ranging from 9 to 15 meV for these $\ce{H_{2}}$ molecules.

Two distinct $\ce{H_{2}}$ binding sites were identified in COF-102 from our simulations. The most favorable of these, denoted site 1 in this work, corresponds to adsorption onto a single $\ce{B_{3}O_{3}}$ cluster in the material; a close-up view of this site is given in Fig. 6(a). As in the case of COF-1, the $\ce{H_{2}}$ molecules prefer to adsorb in the vicinity of the $\ce{B_{3}O_{3}}$ units where the positively charged H atom of the adsorbate molecule can interact with a negatively charged O atom of the boroxine rings. Unlike what was observed in COF-1, however, the $\ce{H_{2}}$ molecules do

![](./images/811025532010364928_5.jpg)

Fig. 6 Molecular illustration of an adsorbed $H_2$ molecule about (a) site 1 and (b) site 2 in COF-102 as determined from GCMC simulations. The adsorbate molecule is shown in orange. Atom colors: C = gray, H = white, O = red, B = pink.

not interact with other components of the COF-102 framework in a concurrent fashion as they are adsorbed onto the $B_3O_3$ rings. This leads to a relatively less energetically favorable binding site and explains why the initial $H_2$ $Q_{st}$ is much lower for COF-102 compared to COF-1. The secondary $H_2$ adsorption site in COF-102, denoted site 2 herein, was identified as binding onto the phenyl rings of the tetraphenylmethyl units (Fig. 6(b)).

Two-dimensional quantum rotation calculations were performed for $H_2$ adsorbed at the two identified binding sites in COF-102 as shown in Fig. 6. These calculations were executed within the entire unit cell of the material. The resulting rotational transitions for $H_2$ adsorbed at both sites in COF-102 are presented in Table 2. The lowest $j = 0$ to $j = 1$ transition for $H_2$ adsorbed at site 1 was calculated to be 8.93 meV, which may correspond to one of the peaks with low intensities observed between 7.5 to 10 meV (Fig. 4). These peaks could possibly correspond to $H_2$ adsorbing onto the $B_3O_3$ clusters in this COF since we calculated a rotational transition that falls within this energy range for this site. Interestingly, this calculated transition is comparable to that for the lowest energy peak observed in the INS spectra for MOFs containing copper paddlewheel units, such as HKUST-1 (9.1 meV)$^{32}$ and rht-MOF-4a (9.0 meV).$^{43}$

For $H_2$ adsorbed at site 2, a value of 12.78 meV was calculated for the lowest $j = 0$ to $j = 1$ transition (Table 2). This calculated transition is reasonably close to the distinct peak occurring at approximately 11.5 meV in the INS spectrum for the COF (Fig. 4). We have therefore tentatively assigned the peak at ca. 11.5 meV as $H_2$ adsorbing onto the phenyl groups on the basis of our calculations and the fact that this is a populous site in COF-102. We expect that transitions occurring above 12.5 meV in the INS spectrum correspond to notably weaker $H_2$ adsorption sites in the COF that were not considered in this work (e.g., localization within the spacious pores of the material).

<table><caption>Table 2 Calculated two-dimensional quantum rotational levels for a $H_2$ molecule adsorbed at two sites in COF-102. Sites 1 and 2 are depicted in Fig. 6(a and b), respectively. The energies are given relative to $E_1$, which are $-34.38$ and $-44.32$ meV for the respective sites</caption>
<thead>
<tr>
<th>$n$</th>
<th>$j$</th>
<th>Site 1 $\Delta E$ (meV)</th>
<th>Site 2 $\Delta E$ (meV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>8.93</td>
<td>12.78</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>15.83</td>
<td>14.99</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>22.76</td>
<td>16.63</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>40.56</td>
<td>42.72</td>
</tr>
<tr>
<td>6</td>
<td>2</td>
<td>40.59</td>
<td>42.94</td>
</tr>
<tr>
<td>7</td>
<td>2</td>
<td>45.44</td>
<td>44.11</td>
</tr>
<tr>
<td>8</td>
<td>2</td>
<td>50.49</td>
<td>45.67</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>52.17</td>
<td>45.89</td>
</tr>
</tbody>
</table>

![](./images/811025532010364928_6.jpg)

Fig. 7 Two-dimensional rotational potential energy surface projected onto a sphere for a $H_2$ molecule adsorbed about the primary adsorption site in (a) COF-1 and (b) COF-102 as shown in Fig. 5 and 6(a), respectively. Relative energies are given in meV. The rotational barrier was calculated to be 41.25 and 35.18 meV for COF-1 and COF-102, respectively.

The rotational PES for $H_2$ located at the most favorable binding site in COF-1 as determined by simulated annealing calculations is shown in Fig. 7(a). The figure shows that the $H_2$ molecule reorients by $180^\circ$ rotations between the minima (shown in blue) over the barriers in between. The maximum on the PES corresponds to the rotational barrier for the adsorbed $H_2$ molecule and it was estimated to be 41.25 meV. This value for the barrier to rotation is actually greater than those for some MOFs that possess open-metal sites, such as members of the M-MOF-74 series. $^{20,44}$ The compact region between two $B_3O_3$ clusters of eclipsed layers in the COF therefore gives rise to a large degree of hindrance to reorientation for the bound $H_2$ molecule.

The rotational barrier for a $H_2$ molecule adsorbed at site 1 in COF-102 was calculated to be 35.18 meV from the rotational PES shown in Fig. 7(b). Although this value for the barrier to rotation is lower than that for $H_2$ adsorbed in COF-1, this quantity is still greater than those for some MOFs that contain open-metal sites based on a literature survey of previous INS and quantum dynamics studies of $H_2$ adsorbed in such materials. $^{20}$ This further suggests that the $B_3O_3$ clusters in COFs impose a significant barrier to rotation on the adsorbed $H_2$ molecule.

## IV. Conclusion

Insights into the nature of the binding sites and the associated rotational dynamics for $H_2$ adsorbed in COFs was presented for the first time by means of a combined INS and computational study, with the latter being essential for interpreting the rather complex INS spectra. $H_2$ molecules adsorbed in both COFs were found to have low rotational tunnelling frequencies, which were supported by our theoretical studies. Two-dimensional quantum rotation calculations for $H_2$ adsorbed at the most favorable binding site in both COFs produced rotational transitions that are good agreement with the lowest energy peaks that occur in the INS spectra. The preferred $H_2$ binding sites in both COFs were found to be within the vicinity of the $B_3O_3$ clusters. In the case of COF-1, a $H_2$ molecule can interact with two $B_3O_3$ rings of eclipsed layers simultaneously, which gives rise to a high $H_2$ adsorption enthalpy. These $B_3O_3$ clusters evidently impose a high rotational barrier on the bound $H_2$ according to our calculation of the rotational PES. The calculated barriers to rotation for $H_2$ adsorbed at the most favorable adsorption site in both COFs are greater than or comparable to those for some MOFs that possess open-metal sites. $^{20}$

The results from this study appear to confirm that COFs could represent promising alternatives to MOFs as candidates for $H_2$ storage applications. Like MOFs, COFs are highly tunable, as a number of different COFs with varying surface areas, pore sizes, topologies, and functionalities can be synthesized by incorporating different types of organic molecules. $^{10,11,13}$ In addition, COFs can exhibit higher thermal stability than most types of MOFs. The ability of COFs to adsorb considerable amounts of $H_2$ within the pores combined with their tunability and remarkable stability makes these materials one of the more promising candidates for $H_2$ storage. $^{8,9}$ In order to improve $H_2$ adsorption in COFs for their potential use as $H_2$ storage platforms at room temperature, future experimental work must focus on synthesizing such materials with highly constricted accessible regions that can interact strongly with the adsorbate through close-fitting van der Waals interactions. For instance, it is expected that a variant of COF-1 in which the eclipsed sheets are stacked closer together will give rise to a higher $Q_{st}$ and rotational barrier for the adsorbed $H_2$, as this will shorten the distances (and increase interactions) between the H atoms of the adsorbate and the O atoms of the $B_3O_3$ rings.

## Competing financial interest

The authors declare no competing financial interest.

## Acknowledgements

T. P., K. A. F., and B. S. acknowledges the National Science Foundation (Award No. DMR-1607989), including support from the Major Research Instrumentation Program (Award No. CHE-1531590). Computational resources were made available by a XSEDE Grant (No. TG-DMR090028) and by Research Computing at the University of South Florida. T. P. and B. S. also acknowledges support from a ACS Petroleum Research Fund grant (ACS PRF 56673-ND6). We thank Professor Omar M. Yaghi for his guidance with this work and for use of his adsorption instrument.

## References

1 A. Haryanto, S. Fernando, N. Murali and S. Adhikari, *Energy Fuels*, 2005, **19**, 2098-2106.

2 W. Doenitz, R. Schmidberger, E. Steinheil and R. Streicher, *Int. J. Hydrogen Energy*, 1980, **5**, 55-63.

3 B. Sakintuna, F. Lamari-Darkrim and M. Hirscher, *Int. J. Hydrogen Energy*, 2007, **32**, 1121-1140.

4 D. J. Collins, S. Ma and H.-C. Zhou, in *Metal-Organic Frameworks: Design and Application*, ed. L. R. MacGillivray, John Wiley & Sons, Inc., Hoboken, NJ, 2010, pp. 249-266.

5 M. P. Suh, H. J. Park, T. K. Prasad and D.-W. Lim, *Chem. Rev.*, 2012, **112**, 782-835.

6 H. Furukawa, K. E. Cordova, M. O'Keeffe and O. M. Yaghi, *Science*, 2013, **341**, 1230444.

7 M. Eddaoudi, D. B. Moler, H. Li, B. Chen, T. M. Reineke, M. O'Keeffe and O. M. Yaghi, *Acc. Chem. Res.*, 2001, **34**, 319-330.

8 S. S. Han, H. Furukawa, O. M. Yaghi and W. A. Goddard III, *J. Am. Chem. Soc.*, 2008, **130**, 11580-11581.

9 H. Furukawa and O. M. Yaghi, *J. Am. Chem. Soc.*, 2009, **131**, 8875-8883.

10 A. P. Côté, A. I. Benin, N. W. Ockwig, M. O'Keeffe, A. J. Matzger and O. M. Yaghi, *Science*, 2005, **310**, 1166-1170.

11 X. Feng, X. Ding and D. Jiang, *Chem. Soc. Rev.*, 2012, **41**, 6010-6022.

12 R. C. Tatar and S. Rabii, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1982, **25**, 4126-4141.

13 H. M. El-Kaderi, J. R. Hunt, J. L. Mendoza-Cortés, A. P. Côté, R. E. Taylor, M. O'Keeffe and O. M. Yaghi, *Science*, 2007, **316**, 268-272.

14 D. N. Dybtsev, H. Chun and K. Kim, *Chem. Commun.*, 2004, 1594-1595.

15 G. Garberoglio, *Langmuir*, 2007, **23**, 12154-12158.

16 E. Klontzas, E. Tylianakis and G. E. Froudakis, *J. Phys. Chem. C*, 2008, **112**, 9095-9098.

17 P. Srepusharawoot, R. H. Scheicher, C. M. Araújo, A. Blomqvist, U. Pinsook and R. Ahuja, *J. Phys. Chem. C*, 2009, **113**, 8498-8504.

18 J. Eckert and W. Lohstroh, in *Neutron Applications in Materials for Energy*, ed. G. J. Kearley and V. K. Peterson, Springer International Publishing, 2015, pp. 205-239.

19 T. Pham, K. A. Forrest, B. Space and J. Eckert, *Phys. Chem. Chem. Phys.*, 2016, **18**, 17141-17158.

20 T. Pham, K. A. Forrest, P. A. Georgiev, W. Lohstroh, D.-X. Xue, A. Hogan, M. Eddaoudi, B. Space and J. Eckert, *Chem. Commun.*, 2014, **50**, 14109-14112.

21 N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller, *J. Chem. Phys.*, 1953, **21**, 1087-1092.

22 P. P. Ewald, *Ann. Phys.*, 1921, **369**, 253-287.

23 B. A. Wells and A. L. Chaffee, *J. Chem. Theory Comput.*, 2015, **11**, 3684-3695.

24 J. L. Belof, A. C. Stern and B. Space, *J. Chem. Theory Comput.*, 2008, **4**, 1332-1337.

25 K. A. Forrest, T. Pham, K. McLaughlin, J. L. Belof, A. C. Stern, M. J. Zaworotko and B. Space, *J. Phys. Chem. C*, 2012, **116**, 15538-15549.

26 T. Pham, K. A. Forrest, P. Nugent, Y. Belmabkhout, R. Luebke, M. Eddaoudi, M. J. Zaworotko and B. Space, *J. Phys. Chem. C*, 2013, **117**, 9340-9354.

27 T. Pham, K. A. Forrest, A. Hogan, K. McLaughlin, J. L. Belof, J. Eckert and B. Space, *J. Mater. Chem. A*, 2014, **2**, 2088-2100.

28 T. Pham, K. A. Forrest, K. McLaughlin, J. Eckert and B. Space, *J. Phys. Chem. C*, 2014, **118**, 22683-22690.

29 T. Pham, K. A. Forrest, R. Banerjee, G. Orcajo, J. Eckert and B. Space, *J. Phys. Chem. C*, 2015, **119**, 1078-1090.

30 V. Buch, *J. Chem. Phys.*, 1994, **100**, 7610-7629.

31 M. Abramowitz, *Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables*, Dover Publications, Inc., Mineola, NY, 1965, p. 887.

32 C. M. Brown, Y. Liu, T. Yildirim, V. K. Peterson and C. J. Kepert, *Nanotechnology*, 2009, **20**, 204025.

33 N. L. Rosi, J. Kim, M. Eddaoudi, B. Chen, M. O'Keeffe and O. M. Yaghi, *J. Am. Chem. Soc.*, 2005, **127**, 1504-1518.

34 Y. Liu, H. Kabbour, C. M. Brown, D. A. Neumann and C. C. Ahn, *Langmuir*, 2008, **24**, 4772-4777.

35 B. Assfour and G. Seifert, *Microporous Mesoporous Mater.*, 2010, **133**, 59-65.

36 A. K. Rappé, C. J. Casewit, K. S. Colwell, W. A. Goddard and W. M. Skiff, *J. Am. Chem. Soc.*, 1992, **114**, 10024-10035.

37 W. L. Jorgensen, D. S. Maxwell and J. Tirado-Rives, *J. Am. Chem. Soc.*, 1996, **118**, 11225-11236.

38 Q. Yang, D. Liu, C. Zhong and J.-R. Li, *Chem. Rev.*, 2013, **113**, 8261-8323.

39 L. Czepirski and J. Jagiełło, *Chem. Eng. Sci.*, 1989, **44**, 797-801.

40 M. Dincă, A. Dailly, Y. Liu, C. M. Brown, D. A. Neumann and J. R. Long, *J. Am. Chem. Soc.*, 2006, **128**, 16876-16883.

41 D. Nicholson and N. G. Parsonage, *Computer Simulation and the Statistical Mechanics of Adsorption*, Academic Press, London, 1982, p. 97.

42 S. Kirkpatrick, C. D. Gelatt and M. P. Vecchi, *Science*, 1983, **220**, 671-680.

43 J. F. Eubank, F. Nouar, R. Luebke, A. J. Cairns, L. Wojtas, M. Alkordi, T. Bousquet, M. R. Hight, J. Eckert, J. P. Embs, P. A. Georgiev and M. Eddaoudi, *Angew. Chem., Int. Ed.*, 2012, **51**, 10099-10103.

44 L. Kong, G. Román-Pérez, J. M. Soler and D. C. Langreth, *Phys. Rev. Lett.*, 2009, **103**, 096103.