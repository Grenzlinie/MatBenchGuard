![](./images/812480462436958208_1.jpg)

Chemical Physics Letters 774 (2021) 138619

Contents lists available at ScienceDirect

# Chemical Physics Letters

journal homepage: www.elsevier.com/locate/cplett

![](./images/812480462436958208_2.jpg)

Research paper

![](./images/812480462436958208_3.jpg)

# Cisplatin release from inclusion complex formed by oxidized carbon nanotube: A DFT study

Leonardo A. De Souza $^{a, *}$, Eduardo R. Almeida $^{b}$, Jadson C. Belchior $^{a}$, Hélio F. Dos Santos $^{b}$, Wagner B. De Almeida $^{c}$

$^{a}$ Departamento de Química, ICEx, Universidade Federal de Minas Gerais (UFMG), Campus Universitário, Pampulha, Belo Horizonte, MG 31270-901, Brazil
$^{b}$ Núcleo de Estudos em Química Computacional (NEQC), Departamento de Química, ICE, Universidade Federal de Juiz de Fora (UFJF), Campus Universitário, Martelos, Juiz de Fora, MG 36036-330, Brazil
$^{c}$ Laboratório de Química Computacional e Modelagem Molecular (LQC-MM), Departamento de Química Inorgânica, Instituto de Química, Universidade Federal Fluminense (UFF), Outeiro de São João Batista s/n, Campus do Valonguinho, 24020-141, Centro, Niterói, RJ, Brazil

---

## ARTICLE INFO

**Keywords:**
Cisplatin release
Oxidized carbon nanotube
DFT calculations
Thermodynamic analysis
Raman and $^{1}$H NMR spectra

## ABSTRACT

Computational methods were used to study the release of cisplatin (cDDP) from inclusion complex formed by cDDP and oxidized carbon nanotube (CNTox). The gas phase Gibbs free energy profile showed that the releasing process is exergonic by $\sim-25$ kcal mol$^{-1}$, nonetheless it was found to be kinetically unfavorable with a barrier of 58.4 kcal mol$^{-1}$. The Raman and $^{1}$H NMR spectra also were monitored and showed to be sensitive along the releasing path. These results may assist experimentalists in monitoring the controlled release of cisplatin in the biological environment.

---

## 1. Introduction

Cisplatin derivatives are widely used in the therapy of various types of solid tumors such as lung, liver, testis, breast, neck and head cancer [1]. However, the low selectivity associated with the high toxicity of these drugs limit their administration in chemotherapy of cancer [2]. In order to minimize these side effects, drug delivery systems (DDS) formed by host-molecules with 10-200 nm in length have been intensively investigated experimentally [3-7] and computationally [8-17]. In general, these systems offer some advantages as increasing the bioavailability of the drugs in the biological environment. DDS provide protection, physical and chemical stability of the drug against reactive biomolecules, increase the solubility and dispersion of poorly soluble drugs in the bloodstream and release them progressively and in a controlled manner. The latter advantages certainly minimize high dose administration [3,18]. In recent years, new achievements in synthesis and surface functionalization methods have made the carbon nanotubes (CNTs) [6] and other nanostructures [7] as potential DDS.

Guven et al. [19] studied *in vivo* biodistribution and therapeutic efficacy of ultra-short CNTs as DDS of cisplatin (cDDP) drug against breast cancer of mouse, and found that nanotubes assist in the delivery of encapsulated cDDP, increasing drug accumulation in cancer resistant cells. Yu et al. [6] constructed a targeted DDS formed by loboplatin drug into polyethylene glycol-modified carbon nanotubes and performed *in vitro* tests against human liver cancer cells. The authors show that the inclusion compounds have good cell penetrability and stability, a controlled release property at pH = 5 with 80% of loboplatin released, and high cell inhibition rate. Lucío et al. [7] studied the synthesis and characterization of a series of hybrid materials composed of functionalized carbon nanohorns (CNH) with monoclonal antibody (Ab) D2B, named f3-CNH, as delivery systems of cDDP and a targeting moiety, the anti-PSMA D2B Ab, with specific cytotoxicity against prostate cancer cells. They demonstrated in *in vitro* tests that there was a selective binding and uptake of the conjugates with D2B antibody on PSMA+ prostate cancer cells. This selectivity was enhanced when the nanostructures were protected with bovine serum albumin (BSA) biological environment [7].

From the theoretical point of view there are also several approaches looking for better DDS applications. Mehrjouei et al. [8] simulated the release of cisplatin from nanotubes cavity (CNT, boron nitride and silicon carbide nanotubes) using the classical molecular dynamics (MD) method. The authors observed that nanotube composition and diameter are more important than its chirality and temperature for the release process. In addition, they showed that the adsorption of the drug on the

---

* Corresponding author.
E-mail address: desouza.leonardo.chem@gmail.com (L.A. De Souza).

https://doi.org/10.1016/j.cplett.2021.138619
Received 4 November 2020; Received in revised form 31 March 2021; Accepted 5 April 2021
Available online 8 April 2021
0009-2614/© 2021 Elsevier B.V. All rights reserved.

outer surface of the nanotube interfered on the release efficiency. Almeida et al. recently reported MD studies in aqueous solution of CNHs [9] and their oxidized/reduced forms [10] with cisplatin hosted in the nanostructures to form cDDP@CNH, cDDP@CNHox and cDDP@CNHh inclusion complexes, respectively. The authors showed in Ref. [9] that the opening angle of the cone is an important factor for the drug mobility, the inner solvation structure, and the binding free energies of cDDP@CNH complexes. In addition, all cDDP@CNH models were thermodynamically favorable with the main contributions for the complex stability from the van der Waals (vdW) and electrostatic in- teractions. In Ref. [10], Almeida and collaborators highlighted a slightly lower stability of the cDDP@CNHox complexes in comparison with the cDDP@CNHh and cDDP@CNH. The authors suggested that the inclusion complex stability depends on the nanowindow size present in the CNHox and CNHh molecules, an important feature that can be studied by ex- perimentalists in order to tune the drug releasing time. We have also recently reported [11] the use the relativistic NMR-DKH basis sets with density functional theory (DFT) calculations to study the $^{1} H$ and $^{195} Pt$ NMR spectra of inclusion complexes formed between cDDP and oxidized carbon nanotube (CNTox) and CNHox molecules. Our results showed that the $^{195} Pt$ NMR shifted upon inclusion, found at -2314 and -2192 ppm for inclusion complexes with CNTox and CNHox nanostructures, respectively compared to free cDDP $(-2110 ppm)$ . We also showed that the formation energy for cDDP@CNTox is lower (more negative) than for cDDP@CNHox complex.

The toxicity of carbon nanostructures, as well as the biological as- pects related to their function as a drug nanovector are dependent on their surface topology [20]. In vitro and in vivo studies [20] showed that multi-walled carbon nanotubes (MWCNT) functionalized with oxygen- ated groups such as carboxyls, carbonyls and hydroxyls contribute to the increase in the lipophilicity of these nanovectors and, therefore, assist in translocation through cell membranes. In this sense, our group per- formed a DFT study of structural, energetic and spectroscopic properties of oxidized carbon nanotubes and nanocones [16] according to theoretical-experimental reaction schemes in the presence of $O_{2}$ and H2O. Mlaouah et al. [21] performed DFT calculations of the DDS for- mation based on small models of pristine graphene encapsulating and releasing the gemcitabine antitumor drug. The authors demonstrated that the distance of $6 \AA$ between the two layers of graphene was enough to produce a stable inclusion complex $(-1.52 eV$ or $-35.05 kcal mol^{-1})$ , and during the release of the drug this distance reaches a little more than8.5 A. In another study, Duverger and Picaud [22] showed through MD simulations that the antibacterial agent ciprofiaxicin has its diffusive translocation improved through a lipid bilayer membrane model after the drug adsorption in nanoflakes formed by graphene oxide or boron nitride oxide. Epoxy and hydroxyls groups bounded to the surface of these nanostructures, increases their hydrophilicity and lipophilicity contributing to the process of translocation of the drug into the cell.

The present work is dealing with simulations of cDDP release from cDDP@CNTox inclusion complex through the CNTox vacancy. The stepwise pathway was monitored by $^{1} H$ NMR and Raman spectra. It is proposed relevant and quantitative spectroscopic data that can assist experimentalists interested in mapping the controlled release of the drug from these nanosystems.

## 2. Computational details

The calculations were carried out using the GAUSSIAN 09 package[23] employing the DFT methodology [24] and the B3LYP [25] func- tional with the LANL2DZ [26] effective core potential (ECP) for plat- inum atom and 6-31G [27] basis set for C, H, N and Cl atoms, named, B3LYP/LANL2DZ/6-31G. The geometry of the cDDP@CNTox inclusion complex $(C_{168} H_{24} O_{15} Cl_{2} N_{2} Pt)$ was reported in our previous study and more details on the molecular modeling of this structure can be found in Refs. [16,17]. From the optimized geometry of cDDP@CNTox inclusion complex, the semi-rigid scan (gas phase) simulating the drug release was performed. In this calculation, 72C atoms and 12H atoms were kept frozen and the rest of the structure was optimized at each scan step (see scheme of Fig. 1). The cDDP molecule was moved out $14.0 \AA$ ( $0.5 \AA$ step size) from equilibrium point. Twenty-eight geometries were generated, labeled as CNTox $\Rightarrow$ cDDP(X) where X is the geometry equivalent to scan coordinate. The release energies were calculated using the equilibrium complex geometry as starting point. Some snapshots taken from scan path (Fig. 1) were re-optimized and used for calculating the Raman spectra and thermodynamic properties. The solvent effect was accoun- ted in energy by means of Polarizable Continuum Model (PCM) using the Integral Equation Formalism variant (IEFPCM) [28] with dielectric constant adjusted for water solvent $(\varepsilon=78.3553)$ . The Gauge Independent Atomic Orbital (GIAO) method [29] was used for the calculation of $^{1} H$ magnetic shielding constants $(\sigma)$ , with chemical shifts(δ) obtained on a δ-scale relative to TMS.

![](./images/812480462436958208_4.jpg)

Fig. 1. Definition of the semi-rigid scan coordinate $(R_{scan})$ of the cisplatin molecule release from inside of cDDP@CNTox inclusion complex. The optimized atoms are represented in ball and bond type and those kept frozen in wireframe.

![](./images/812480462436958208_5.jpg)

## 3. Results and discussions

The model of cDDP@CNTox inclusion complex used as a starting point for the scan calculation of the cisplatin release corresponds to the structure studied in our previous work [17]. In order to evaluate the effect of the density functional in the geometry calculation, in the pre- sent work the system was also optimized with the functionals B3LYP-D3 [30] and M06-2X [31]. B3LYP-D3 includes terms of Grimme's empirical electronic dispersion, while the functional M06-2X has dispersion terms and better describes the short or long-range weak interactions, such as van der Waals interactions. 6-31G basis set was maintained to minimize the computational cost in calculations of geometry and vibrational harmonic frequencies. The optimized geometry in the three levels of theory for the cDDP@CNTox are shown in Fig. S1 (Supplementary Material). Total energy and thermodynamic parameters of formation of inclusion complex can be seen in Table S1 (Supplementary Material). It was not observed significant changes in the geometry of cDDP@CNTox. The cisplatin molecule had the same structural data obtained in Ref. 17 (average Pt-Cl and Pt-N bond lengths of 2.40 Å and 2.12 Å, respectively) and an intermolecular distance of approximately 4.47 Å from the inner walls of the CNTox. However, the data in Table S1 demonstrated that the energies associated with the formation of the inclusion complex are greatly affected by the three density functionals. B3LYP-D3 and M06-2X energies are 70.5 and 45.5 kcal mol⁻¹ more stabilized in relation to the $\triangle E_{\text{F}}$ value calculated with B3LYP, respectability. A similar trend was observed for the enthalpy $(\triangle H_{\text{F}})$ and free energy of Gibbs $(\triangle G_{\text{F}})$ formation calculated in the same levels of theory. According to our results, the formation of the cDDP@CNTox system with the functional B3LYP-D3 is more exothermic and thermodynamically favorable.

Knowing that the geometries obtained for the inclusion complex are very similar among the theoretical levels employed and keeping in mind the computational cost, the semi-rigid scan simulating the release of cisplatin was calculated at B3LYP/LANL2DZ/6-31G level. The cDDP release can be seen from the short movie (gif file) available to the reader as supplementary material. The movie shows the topological variation of the oxidized region of CNTox model in the initial stages until the cDDP release completely. The structural aspects of the CNTox⇒cDDP(X) systems will be discussed along with the energetic and thermodynamic parameters for drug release.

Fig. 2 shows the total energy variation $(\Delta E_{Release})$ for cDDP release. The $\Delta E_{Release}$ increases to 14.3 kcal mol⁻¹ (gas phase) at point 2 where the cDDP is only 1 Å distant from the equilibrium point. This energy change was slightly smaller in solution, of about 11.0 kcal mol⁻¹. From this point, the intramolecular (between —OH of —COOH group and vicinal —C═O group of CNTox) and intermolecular (between NH₃ group of cDDP and —OH of —COOH group of CNTox) hydrogen bonds are weakened and broken explaining the increase in relative energy. This result is curious because one could expect that the hydrogen bonds between the cDDP and the oxidized region of the nanotube would be more frequent with the approximation them. Perhaps, this was not observed during the drug release simulation due to the size of each step of the scan calculation. The energy barrier for cDDP release is reached when CNTox⇒cDDP(7) is formed; $\Delta E_{Release}=56.8$ kcal mol⁻¹ (gas phase value - Table 1) and 61.2 kcal mol⁻¹ (aqueous solution - Table 1). A higher energy barrier (83.1 kcal mol⁻¹ - Table 1) was observed when we corrected the $\Delta E_{Release}$ value through single-point (SP) calculations performed at B3LYP-D3/LANL2DZ/6-31G(d,p) level starting from the B3LYP geometry for CNTox⇒cDDP(7) system. $\Delta E_{Release}$ values calculated with the M06-2X functional and 6-31G and 6-31G(d,p) basis set, suggest that weak repulsive forces between the cDDP molecule and the oxidized region of the CNTox may contribute to expel the drug. An average increase of 8.5 kcal mol⁻¹ (Table 1) was observed for the drug release barrier in gas phase. The presence of repulsive forces can be observed by comparing the electrostatic potential surface calculated at B3LYP-D3/LANL2DZ/6-31G(d,p) level for the inclusion complex (Fig. S2a - Supplementary Material) and for each release system (Fig. S2b and f) highlighted in Fig. 2. Fig. S2a and c show that the approximation of the cDDP molecule to the oxidized opening of the CNTox, gradually disturbs the negative charge concentration in this region. After the passage of cisplatin chloride ligands (CNTox⇒cDDP(15) system) through the opening of the CNTox (Fig. S2d), the higher concentration of positive charges on the carbon atoms in this region seems to repel the metal and

<table><thead><tr><th colspan="5">Table 1 Energetic and thermodynamic parameters (gas phase, p = 1 atm, T = 298.15 K) of the cisplatin molecule release in relation to the cDDP@CNTox inclusion complex. All values in units of kcal mol⁻¹.</th></tr><tr><th>CNTox ⇒ cDDP</th><th>$\Delta E_{Release}$</th><th>$\Delta H_{Release}$</th><th>$T\Delta S$</th><th>$\Delta G_{Release}$</th></tr></thead><tbody><tr><td>Scan 7</td><td>56.8 (61.2) a[65.8] b{64.9} c<br>[83.1] d{65.2} e</td><td>55.0</td><td>−3.4</td><td>58.4</td></tr><tr><td>Scan 11</td><td>36.9 (39.2) a[64.9] b{58.7} c<br>[67.7] d{59.9} e</td><td>32.8</td><td>−1.7</td><td>34.5</td></tr><tr><td>Scan 15</td><td>−45.6 (−57.2) a[7.5] b{2.0} c<br>[14.7] d{4.6} e</td><td>−33.4</td><td>0.1</td><td>−33.5</td></tr><tr><td>Scan 28</td><td>−15.2 (−40.6) a[46.2] b{32.3} c<br>[45.5] d{30.7} e</td><td>−21.2</td><td>−1.9</td><td>−19.3</td></tr></tbody><tfoot><tr><td colspan="5">aThe values were calculated at B3LYP/LANL2DZ/6-31G (IEFPCM-Water) level.<br>bThe values refer to single-point calculations at B3LYP-D3/LANL2DZ/6-31G (Gas Phase)// B3LYP/LANL2DZ/6-31G (Gas Phase) level.<br>cThe values refer to single-point calculations at M06-2X/LANL2DZ/6-31G (Gas Phase)// B3LYP/LANL2DZ/6-31G (Gas Phase) level.<br>dThe values refer to single-point calculations at B3LYP-D3/LANL2DZ/6-31G(d,p) (Gas Phase)// B3LYP/LANL2DZ/6-31G (Gas Phase) level.<br>eThe values refer to single-point calculations at M06-2X/LANL2DZ/6-31G(d,p) (Gas Phase)// B3LYP/LANL2DZ/6-31G (Gas Phase) level.</td></tr></tfoot></table>


its $NH_3$ ligands, decreasing the $\Delta E_{Release}$ values necessary for the convergence of the release scan. Table 1 shows that when CNTox$\Rightarrow$cDDP (15) is formed, the B3LYP $\Delta E_{Release}$ reaches its lowest value, $-45.6$ kcal mol$^{-1}$ (gas phase) and $-57.2$ kcal mol$^{-1}$ (solution), and the drug is outside the tube cavity. Table 1 also shows that the B3LYP-D3 and M06-2X $\Delta E_{Release}$ values (SP calculations) is almost twice increased in relation to the energy barrier for drug release calculated at B3LYP level. This suggests that the use of density functionals that include the terms of empirical dispersion and that contemplate van der Waals interactions may be considered important for a more realistic description of cisplatin release from the studied inclusion complex model.

Some factors may have a direct role on the thermodynamics of drug release. These factors include: (i) size and diameter of the tube [19,32,33] (ii) the vacancy topology generated as a function of the type and degree of surface oxidation [10,16] and, (iii) the presence of water molecules or other biomolecules in the nanotube cavity [33] that can expel the drug depending on the physicochemical conditions, such as temperature, pH and solvent polarity effects [34]. In the present work, the CNTox model [16] has nominal length and diameter around $18$ Å and $9.5$ Å, respectively. Our model represents precisely the region where in most cases the drug will be hosted, i.e., near to the closed end of the nanostructure [9,10,35]. We calculated the thermodynamic parameters for the cDDP release without the influence of solvent and inner solvation shells [9,10]. We focus on the structural and electronic variations of oxidized surface of CNTox and cDDP during the drug release in gas phase. Enthalpy ($\Delta H_{Release}$)and Gibbs free energy ($\Delta G_{Release}$) for cDDP release were obtained for structures CNTox$\Rightarrow$cDDP(X) (X = 7, 11, 15 and 28). Table 1 and Figs. 3 and 4 show that the cDDP release calculated with B3LYP functional is an exothermic and exergonic process with enthalpy and free energy change $\sim -33$ kcal mol$^{-1}$ (see Table 1). On the other hand, the activation barrier for releasing cDDP was 55-58 kcal mol$^{-1}$ with a small contribution of entropy change. Even though the cDDP molecule has shifted only $3.5$ Å from the equilibrium point up to maximum at the releasing path, the energy increases substantially due to mainly the small size of the oxidized nanowindows compared to the effective size of cDDP [10]. From an electronic point of view, this may be related to the predominance of repulsive forces that increase the energy barrier calculated with the B3LYP-D3 and M06-2X functionals, as previously discussed. The energy decreases when the point CNTox$\Rightarrow$cDDP (11) is reached where the oxidized window opens allowing the cDDP release. When the structure CNTox$\Rightarrow$cDDP(15) is formed, $\Delta H_{Release}$ and $\Delta G_{Release}$ values decrease, on an average, an average $-67$ kcal mol$^{-1}$ and the drug is released with a slight positive entropy ($T\Delta S \simeq 0.1$ kcal mol$^{-1}$). As the molecules move away, $\Delta H_{Release}$ and $\Delta G_{Release}$ values tend to increase and become constant when cisplatin is $10$ Å apart the equilibrium point in cDDP@CNTox.

![](./images/812480462436958208_6.jpg)

Fig. 3. Enthalpy variation ($\Delta H_{Release}$) calculated at B3LYP/LANL2DZ/6-31G (Gas phase) level for the release of the cisplatin molecule from the cDDP@CNTox inclusion complex.

![](./images/812480462436958208_7.jpg)

Fig. 4. Gibbs free energy variation ($\Delta G_{Release}$) calculated at B3LYP/LANL2DZ/6-31G (Gas phase) level for the release of the cisplatin molecule from the cDDP@CNTox inclusion complex.

In previous works, we calculated the energy barrier for the inclusion of the cisplatin molecule in CNH [12] and CNT [14] models. The rigid scan calculations at B3LYP/LANL2DZ/3-21G (gas phase) level showed average values around $27$ kcal mol$^{-1}$ [12] and $90$ kcal mol$^{-1}$ [14], respectively. However, in addition to the lowest theoretical level employed, for the inclusion complex formed with the CNT, the rigid approach used does not allow tube breathing upon inclusion and this may overestimate the energy barrier for the drug inclusion. In the present work, the B3LYP-D3 and M06-2X calculations revealed energy barriers for the release of the drug in the range of $65-83$ kcal mol$^{-1}$. Both calculations (inclusion and release), represent directed and forced simulations whose results are totally dependent on the studied system model and do not take into account specific physicochemical conditions of the biological environment that certainly contribute to minimize such energy barriers.

Raman spectra of the free CNTox, cDDP@CNTox and CNTox$\Rightarrow$cDDP (7,11,15,28) systems were calculated (Fig. 5) and the main vibrational modes are assigned in Table 2. For free CNTox the band frequencies and assignments are in fair agreement with the experimental results [36-38]. In this work, we discussed the changes in the Raman spectrum upon the cisplatin releasing process. The three analyzed regions of the Raman spectrum are: $100-300$ cm$^{-1}$ assigned to the RBM (radial breathing mode) bands, which is related to the tube diameter and represents carbon atoms movement in the radial direction; the bands around $1300-1500$ cm$^{-1}$ that represent disorder peaks, called D band, and those close to $1500-1600$ cm$^{-1}$ assigned to the graphitic G band. By comparing Fig. 5a and b it can be seen that the similar intensities of D and G bands, after the formation of the cDDP@CNTox inclusion complex, leads to increase of the G/D intensity ratio from 0.4 to 0.6. For CNTox$\Rightarrow$cDDP(7) (Fig. 5c), the cDDP molecule is closer to the oxidized region and consequently the G band intensity decreases considerably. In contrast, the intensity of D band increases and the G/D value decreased from 0.6 in cDDP@CNTox to 0.2 in CNTox$\Rightarrow$cDDP(7). When the cisplatin is released from CNTox, the G/D ratio increases to 0.6 in CNTox$\Rightarrow$cDDP(15) (Fig. 5e) and 1.9 in CNTox$\Rightarrow$cDDP (28) (Fig. 5f). Table 2 shows that the position of the RBM bands are not significantly shifted after cisplatin release. In CNTox$\Rightarrow$cDDP(7) and (11), the RBM band is shifted about $15$ cm$^{-1}$ to highest energy region, suggesting a decreasing in the average diameter of the tube. Table 2 also shows that when cDDP is released, the G and D bands frequencies are closer to the

![](./images/812480462436958208_8.jpg)

Fig. 5. Simulation of the Raman spectra calculated at B3LYP/LANL2DZ/6-31G (Gas phase) level to free CNTox (a), cDDP@CNTox inclusion complex (b) and its scan 7, 11, 15 and 28 geometries for the cisplatin released (c-g). The main bands are in Table 2.

<table>
<caption>Table 2<br>Vibrational frequencies (in cm⁻¹) and Raman assignments for the CNTox, CNTox in the cDDP@CNTox inclusion complex and CNTox in scan geometries for the cisplatin released.</caption>
<thead>
<tr>
<th>Structure</th>
<th>G band</th>
<th>D band</th>
<th>RBM</th>
</tr>
</thead>
<tbody>
<tr>
<td>CNTox</td>
<td>1580</td>
<td>1340</td>
<td>265</td>
</tr>
<tr>
<td>cDDP@CNTox</td>
<td>1568</td>
<td>1308</td>
<td>249</td>
</tr>
<tr>
<td>CNTox ⇒ cDDP (scan 7)</td>
<td>1572</td>
<td>1311</td>
<td>263</td>
</tr>
<tr>
<td>CNTox ⇒ cDDP (scan 11)</td>
<td>1574</td>
<td>1320</td>
<td>264</td>
</tr>
<tr>
<td>CNTox ⇒ cDDP (scan 15)</td>
<td>1573</td>
<td>1338</td>
<td>253</td>
</tr>
<tr>
<td>CNTox ⇒ cDDP (scan 28)</td>
<td>1600</td>
<td>1350</td>
<td>262</td>
</tr>
</tbody>
</table>

values calculated for the free CNTox.

NMR techniques are widely used to determine the molecular structure of drugs, and can also be employed in cells for ions transport, diffusion of drugs through the membrane and membrane permeability studies [39-41]. For example, Becker et al. [40] monitored the local disposition of the drug carboplatin by $^{195}$Pt NMR spectroscopy after subcutaneous injection of the drug in mouse tissue (back of the neck of the animal). To determine chemical shifts and the detection threshold, the authors performed in vitro $^{195}$Pt NMR experiments with potassium tetrachloroplatinate(II), carboplatin and cisplatin solutions in different solvents such as H₂O, DMSO, and DMF. It was observed a chemical shift change regardless the solvent used (except for cisplatin).

In recent years, we have successfully performing DFT calculations to predict the NMR spectrum of free cisplatin [42] and its inclusion compounds formed by carbon nanostructures [11,12,14,17] in solution, and

![](./images/812480462436958208_9.jpg)

Fig. 6. B3LYP/LANL2DZ/6-31G(d,p) (PCM-Water) $^1$H NMR spectra for free cDDP (a), cDDP in the cDDP@CNTox inclusion complex (b) and its scan 7, 11, 15 and 28 geometries for the cisplatin released (c-f) with all values in ppm.

other biomolecules in various solvents [43-48]. Here, we calculate the $^1$H NMR chemical shifts ($\delta$) for cisplatin protons (NH₃ group) in each geometry CNTox$\Rightarrow$cDDP(X) along the entire scan path represented in Fig. 2. The solvent effect was accounted for by IEFPCM. Table S2 (Supplementary Material) shows the calculated $\delta$ values for the two distinct hydrogen atoms of free cDDP, opposite (Hₐ, H'ₐ, Hᵦ, H'ᵦ) and near (H_c, H'_c) the chlorine atoms; 4.3 and 3.9 ppm, respectively. The experimental $\delta$ value [49] (5 mmol dm⁻³ solution containing cisplatin in 95% H₂O + 5% D₂O and pH 4.7) is about 4.1 ppm which is in good agreement with our predictions. By comparing Fig. 6a and b, it is noted that the symmetry of the two $^1$H signals of free cDDP is broken in the cDDP@CNTox inclusion complex with maximum $\Delta\delta$ about -12 ppm (upfield). In general, Table S1 shows that the proton signals of cDDP in CNTox$\Rightarrow$cDDP(X) shift to the low-field region ($\Delta\delta>0$) with the drug release. Fig. 6c and d show that when the drug is almost out of the CNTox cavity, cDDP protons are less shielded and $\Delta\delta$ is maximum, reaching 13 ppm and 15 ppm in CNTox$\Rightarrow$cDDP(7) and CNTox$\Rightarrow$cDDP(11), respectively. From the CNTox$\Rightarrow$cDDP(15) (Fig. 6e), $\Delta\delta$ becomes constant (see Table S1) and the $^1$H NMR chemical shifts are similar to the $\delta$ values for the free cDDP.

### 4. Conclusions

In the present work, DFT method was used to study the structure, thermodynamics and spectroscopic characterization (Raman and $^1$H NMR spectra) of cisplatin releasing from the cDDP@CNTox inclusion complex. The releasing energy barrier calculated in gas phase was 56.8 kcal mol$^{-1}$. The activation Gibbs free energy was 58.4 kcal mol$^{-1}$, with very small entropic contribution. Besides that, the drug release was exergonic with Gibbs free energy variation of -33 kcal mol$^{-1}$. The analyses of Raman spectra showed that the characteristic bands of CNTox molecule are strongly affected after cDDP release. G/D ratio increases from CNTox$\Rightarrow$cDDP(7) to CNTox$\Rightarrow$cDDP(15), which indicates the decrease of the D band intensity due to the release of the drug from CNTox cavity. Our reported results for $^1$H NMR spectra in aqueous solution showed that experimental detection of drug release can be promptly attained through analysis of chemical shifts calculated for cisplatin NH$_3$ protons. After the total release of the drug from the nanostructure cavity, the simulated $^1$H NMR spectrum is very similar to the one calculated for free cisplatin in solution. Overall, these theoretical predictions at an adequate level of *ab-initio* calculations can provide spectroscopic data, especially thermodynamics data, for suggesting new experiments for controlled release systems.

### Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgments

L. A. De Souza thanks the CAPES for a Post-Doctoral scholarship (Proc. No. 88882.306139/2018-01) during the period 2017-2018 at Universidade Federal Fluminense. L. A. De Souza also thanks the Capes for a new Post-Doctoral scholarship (Proc. No. 88887.363111/2019-00) at Universidade Federal de Minas Gerais. W. B. De Almeida would like to thank the Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) for a research fellowship (Proc. No. 310102/2016-2) and Fundação Carlos Chagas Filho de Amparo à Pesquisa do Estado do Rio de Janeiro (FAPERJ) for support (Proc. No. 233888.).

### Appendix A. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.cplett.2021.138619.

### References

[1] L. Kelland, Nat. Rev. Cancer 7 (2007) 573-584.
[2] S. Dasari, P.B. Tchounwou, Eur. J. Pharmacol. 740 (2014) 364-378.
[3] S. Lata, G. Sharma, M. Joshi, P. Kanwar, T. Mishra, Int. J. Nanotechnol. Nanosci. 5 (2017) 1-29.
[4] S. Duggan, W. Cummins, O.O'. Donovan, H. Hughes, E. Owens, Euro. J. Pharm. Sci. 100 (2017) 64-78.
[5] T.C. Johnstone, K. Suntharalingam, S.J. Lippard, Chem. Rev. 116 (2016) 3436-3486.
[6] S. Yu, Q. Li, J. Wang, J. Du, Y. Gao, L. Zhang, L. Chen, Y. Yangb, X. Liu, J. Mater. Res. 33 (2018) 2565-2575.
[7] M.I. Lucío, R. Opri, M. Pinto, A. Scarsi, J.L.G. Fierro, M. Meneghetti, G. Fracasso, M. Prato, E. Vazquez, M.A. Herrero, J. Mater. Chem. B 5 (2017) 8821-8832.
[8] E. Mehrjouei, H. Akbarzadeh, A.N. Shamkhali, M. Abbaspour, S. Salemi, P. Abdi, Mol. Pharm. 14 (2017) 2273-2284.
[9] E.R. Almeida, L.A. De Souza, W.B. De Almeida, H.F. Dos Santos, J. Mol. Graphics Modell. 89 (2019) 167-177.
[10] E.R. Almeida, L.A. De Souza, W.B. De Almeida, H.F. Dos Santos, J. Chem. Inf. Model. 60 (2020) 500-512.
[11] L.A. De Souza, E.R. Almeida, J.H. Cunha e Silva, D. Paschoal, J.C. Belchior, H. F. Dos Santos, W.B. De Almeida, RSC Adv. 11 (2021) 5909-611.
[12] L.A. De Souza, C.A.S. Nogueira, J.F. Lopes, H.F. Dos Santos, W.B. De Almeida, J. Inorg. Biochem. 129 (2013) 71-83.
[13] H.F. Dos Santos, L.A. De Souza, W.B. De Almeida, T. Heine, J. Phys. Chem. C 118 (42) (2014) 24761-24768.
[14] L.A. De Souza, C.A.S. Nogueira, J.F. Lopes, H.F. Dos Santos, W.B. De Almeida, J. Phys. Chem. C 19 (2015) 8394-8401.
[15] L.A. De Souza, C.A.S. Nogueira, P.F.R. Ortega, J.F. Lopes, H.D.R. Calado, R. L. Lavall, G.G. Silva, H.F. Dos Santos, W.B. De Almeida, Inorg. Chim. Acta 447 (2016) 38-44.
[16] L.A. De Souza, A.M. Da Silva Jr., H.F. Dos Santos, W.B. De Almeida, RSC Adv. 7 (2017) 13212-13222.
[17] L.A. De Souza, H.F. Dos Santos, L.T. Costa, W.B. De Almeida, J. Inorg. Biochem. 178 (2018) 134-143.
[18] X. Cui, S. Xu, X. Wang, C. Chen, Carbon 138 (2018) 436-450.
[19] A. Guven, G.J. Villares, S.G. Hilsenbeck, A. Lewis, J.D. Landua, L.E. Dobrolecki, L. J. Wilson, M.T. Lewis, Acta Biomater. 58 (2017) 466-478.
[20] R. Alshehri, A.M. Ilyas, A. Hasan, A. Arnaout, F. Ahmed, A. Memic, J. Med. Chem. 59 (2016) 8149-8167.
[21] M. Mlaouah, B. Tangour, M. El Khalifi, T. Gharbi, F. Picaud, J. Mol. Model. 24 (102) (2018) 1-9.
[22] E. Duverger, F. Picaud, J. Mol. Model. 26 (135) (2020) 1-10.
[23] M.J. Frisch, G.W. Trucks, H.B. Schlegel, G.E. Scuseria, M.A. Robb, J.R. Cheeseman, G. Scalmani, V. Barone, B. Mennucci, G.A. Petersson, H. Nakatsuji, M.Li, X. Caricato, H.P. Hratchian, A.F. Izmaylov, J. Bloino, G. Zheng, J.L. Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J.A. Montgomery Jr., J.E. Peralta, F. Ogliaro, M. Bearpark, J.J. Heyd, E. Brothers, K.N. Kudin, V.N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J.C. Burant, S.S. Iyengar, J. Tomasi, M. Cossi, N. Rega, J.M. Millam, M. Klene, J.E. Knox, J.B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R.E. Stratmann, O. Yazyev, A.J. Austin, R. Cammi, C. Pomelli, J.W. Ochterski, R.L. Martin, K. Morokuma, V.G. Zakrzewski, G.A. Voth, P. Salvador, J.J. Dannenberg, S. Dapprich, A. D. Daniels, O. Farkas, J.B. Foresman, J. V. Ortiz, J. Cioslowski, D.J. Fox., Gaussian, Inc., Wallingford CT, 2009.
[24] R.G. Parr, W. Yang, Density-Functional Theory of Atoms and Molecules, Oxford University Press, Oxford, 1989.
[25] C. Lee, W. Yang, R.G. Parr, Phys. Rev. B: Condens. Matter Mater. Phys. 37 (1988) 785-789.
[26] P.J. Hay, W.R. Wadt, J. Chem. Phys. 82 (1985) 299-310.
[27] W.J. Hehre, L. Radom, P.V.R. Schleyer, J.A. Pople, Ab Initio Molecular Orbital Theory, Wiley, New York, 1986.
[28] E. Cances, B. Mennucci, J. Tomasi, J. Chem. Phys. 107 (1997) 3032-3041.
[29] K. Wolinski, J.F. Hilton, P. Pulay, J. Am. Chem. Soc. 112 (1990) 8251-8260.
[30] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, J. Chem. Phys 132 (2010), 154104.
[31] Y. Zhao, D.G. Truhlar, Theor. Chem. Account 120 (2008) 215-241.
[32] L. Muzi, C. Ménard-Moyon, J. Russier, J. Li, C.F. Chin, W.H. Ang, G. Pastorin, G. Risuleo, A. Bianco, Nanoscale 7 (2015) 5383-5394.
[33] V.V. Chaban, O.V. Prezhdo, ACS Nano 5 (2011) 5647-5655.
[34] J. Fan, F. Zeng, J. Xu, S. Wu, J. Nanopart. Res. 15 (2013) (1911) 1-15.
[35] K. Ajima, T. Murakami, Y. Mizoguchi, K. Tsuchida, T. Ichihashi, S. Iijima, M. Yudasaka, ACS Nano 2 (2008) 2057-2064.
[36] A. Jorio, L.G. Cançado, Phys. Chem. Chem. Phys. 14 (2012) 15246-15256.
[37] M.S. Dresselhaus, A. Jorio, M. Hofmann, G. Dresselhaus, R. Saito, Nano Lett. 10 (2010) 751-758.
[38] R. Giro, B.S. Archanjo, E.H.M. Ferreira, R.B. Capaz, A. Jorio, C.A. Achete, Nucl. Inst. Methods Phys. Res. B 319 (2014) 71-74.
[39] A. Timoszyk, Dynamics of Model Membranes by NMR, IntechOpen, 2017.
[40] M. Becker, R.E. Port, H.-J. Zabel, W.J. Zeller, P. Bachert, J. Magn. Reson. 133 (1998) 115-122.
[41] F. Arnesano, L. Banci, I. Bertini, I.C. Felli, M. Losacco, G. Natile, J. Am. Chem. Soc. 133 (2011) 18361-18369.
[42] H.C. Da Silva, W.B. De Almeida, Chem. Phys. 528 (2020), 110479.
[43] L.A. De Souza, M.M. Soeiro, W.B. De Almeida, Int. J. Quantum Chem. 118 (2018), e25773.
[44] L.A. De Souza, W.M.G. Tavares, A.P.M. Lopes, M.M. Soeiro, W.B. De Almeida, Chem. Phys. Lett. 676 (2017) 46-52.
[45] L.A. De Souza, H.C. Da Silva, W.B. De Almeida, ChemistryOpen 7 (2018) 902-913.
[46] H.F. Dos Santos, M.A. Chagas, L.A. De Souza, W.R. Rocha, M.V. De Almeida, C.P. An.coni, W.B. De Almeida, J. Phys. Chem. A 121 (2017) 2839-2846.
[47] H.C. Da Silva, L.A. De Souza, H.F. Dos Santos, W.B. De Almeida, ACS Omega 5 (2020) 3030-3042.
[48] M.C.R. Freitas, V.R. Campos, J.A.L.C. Resende, M.M.P. Da Silva, V.F. Ferreira, A. C. Cunha, J.W.M. Carneiro, M.R. Lage, L.A. De Souza, H.C. Silva, W.B. De Almeida, J. Braz. Chem. Soc. 31 (2020) 867-885.
[49] S.J. Berners-Price, T.A. Frenkiel, U. Frey, J.D. Ranford, P.J. Sadler, J. Chem. Soc. Chem. Commun. (1992) 789-791.