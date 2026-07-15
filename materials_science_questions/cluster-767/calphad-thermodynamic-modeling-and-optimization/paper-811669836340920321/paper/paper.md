# PREDICTION OF SOLID-AQUEOUS EQUILIBRIA IN CEMENTITIOUS SYSTEMS
USING GIBBS ENERGY MINIMIZATION:
## I. MULTIPHASE AQUEOUS - IDEAL SOLID SOLUTION MODELS

V.A.SINITSYN$^{1,2}$, D.A.KULIK$^{2,3}$, M.S. KHODORIVSKY$^{2}$, and I.K.KARPOV$^{4}$

$^{1}$Institute of Geochemistry, Mineralogy & Ore Formation, NAS Ukraine, 252180 Kyiv, Ukraine;
$^{2}$R&D Centre "META", 46 Nauka Prrosp., 252650 Kyiv, Ukraine;
$^{3}$State Scientific Center for Environmental Radiogeochemistry, 252180 Kyiv, Ukraine;
$^{4}$Institute of Geochemistry SB RAS, 664033 Irkutsk, Russia

---

## 1. INTRODUCTION

Concrete and other cement-based materials are increasingly utilized as major structural components of the disposal facilities for low-level and intermediate-level radioactive waste (LLW/ILW). At the same time, cementitious materials function as engineered barriers against migration of radionuclides and other hazardous compounds [1]. Taking into account the expected operation times of such constructions, the long-term prediction of environmental interactions and stability of concretes is important for the development of reliable facilities for LLW/ILW disposal. Thermodynamic approach has been widely used to promote understanding of chemical phenomena in cementitious systems. Recently, several authors attempted to demonstrate usefulness of computer codes for description of the available experimental data and prediction of cement/water equilibria [1-5]. These calculations were based on the Law-of-Mass Action - Reaction Stoichiometry Algorithm (LMA-RSA), widely applied so far in speciation modeling [6]. Apart from many evident achievements, the previous studies have revealed several unresolved or controversial problems which still exist in cement chemistry. In particular:

1. Calculation of equilibrium speciation in solid solution - aqueous solution (SSAS) systems [4];
2. Thermodynamic representation of the amorphous calcium silicate hydrogel (CSH) phase [5], which comprise up to 60% of Portland and blended cements;
3. Account of influence of alkali metals on cement/aqueous chemical interactions [3];
4. Estimation of the effective thermodynamic constants for some important components in cements of different aging times [4];
5. Extension of thermodynamic models of «doped» cements by incorporating species of radionuclides, heavy metals and other components of practical interest [5].

This contribution is aimed to demonstrate some important advantages which innovative Gibbs energy minimization (GEM) algorithms can introduce into development of the predictive thermodynamic models of chemical interactions in cementitious waste-isolating systems, in particular:
- Possibility of direct calculation of SSAS equilibria which adequately describe solubility data;
- Easy and direct extension of the suggested "core" thermodynamic dataset on the basis of solubility, mineralogical and petrographical studies of fresh, aged and doped cements.

---

## 2. MODELING APPROACH

Since early seventies, geochemical modeling based on GEM algorithms is under development as an efficient research technique, implemented, for instance, in *Selektor* codes [8]. Mainly in geosciences, numerous GEM applications have been done using this and other tools [9] on the background of continuous theoretical and algorithmic development [10,11]. In this work, calculations

were performed using Selektor-A code (ver. 3.0.243 for PC [12]) based on an Interior Points Method (IPM) convex programming algorithm [8,10]. The code finds explicit (meta)stable phase-component speciation $x$ (including aqueous, gas and solid-solution components); values of chemical potentials of stoichiometric units $u$; $pH$, $Eh$ and $pP$(gases). Input parameters are temperature $T$, pressure $P$, bulk chemical composition of the whole system $b$, apparent standard-state Gibbs energies for all species $g^o_{TP}$, and set of equations for non-ideality models $\theta$ (if appropriate). One aqueous electrolyte, one gas mixture, and any number of crystalline and dispersed (single- or multi-component) solid phases can be included in the system. This actually means that solubility, gas-aqueous and redox equilibria in complex solid solution - aqueous solution (SSAS) systems can be calculated by GEM immediately in one run, provided that the stoichiometry of end-members is rational, their standard-state chemical potentials are known in $TP$ region of interest, and the non-ideality equations with interaction parameters are available.

In this study, model calculations were performed for ambient conditions $(25^o C, 1$ bar) in the system Na-Ca-Mg-Fe-Al-Si-S-H-O to achieve consistency of evaluated thermodynamic properties of components with available experimental data for cementitious aquatic systems. Activity coefficients of individual aqueous species were calculated using the extended Debye-Hueckel equation, with common third parameter set to 0.064. Solid solutions and gas phases were taken as ideal mixtures as first approximation. Total chemical composition of the modeled experimental systems was specified using quantities of solids and aqueous solution referred to in the literature as initial phases, taking into account stoichiometry of solids and composition of solutes. The calculated equilibrium states were described by equilibrium quantities of phases (solids including solid solutions, aqueous electrolyte and gas) and speciation within each phase. In addition, pH, Eh values, activities of species and total concentrations of dissolved chemical elements were computed for aqueous phase. For each modeled experimental system, a number of runs have been made adjusting the free energy of formation $\Delta G^0_{298.15}$ for some end-members of studied cement phases to achieve the best agreement between experimental and calculated data. Reference thermodynamic data used in calculations is presented in Table 1.

## 3. THERMODYNAMIC MODELS OF CEMENT HYDRATE PHASES

Amorphous calcium silicate hydrogel (CSH) phase is a generic name for colloidal products of reactions between calcium oxide, silica and water, and hydration of the tricalcium and dicalcium silicates found in Portland cements [13]. CSH, being principal binding agent in ordinary Portland cement (OPC) and other cement-based materials, has been the subject of multitude of investigations for many years. Numerous experimental solubility data [3, 13-18] recently have been used to develop some predictive thermodynamic models of CSH [1-3, 5]. Excluding the simplest approach (one phase of constant stoichiometry) [1], these models proceed from the assumption that CSH is one Ca-Si-phase of variable composition. However, the complexity of dissolution curves of CSH (Fig. 1A) is not consistent with that assumption.

Greenberg and Chang [13] have concluded from their experimental data on CSH solubility that several solid phases exist in the system Ca-Si-H-O, depending on Ca/Si ratio. Four Ca/Si ranges of CSH system with different phase composition have been identified [13]: (1) $Ca/Si < 0.14$, $SiO_2$ + silica partially enriched with $Ca(OH)_2$ ; (2) $0.14 < Ca/Si < 1.0$, partially reacted silica + $CaH_2SiO_4$ ; (3) $1.0 < Ca/Si < 1.75$, $CaH_2SiO_4\cdot nCa(OH)_2$ phase; (4) $Ca/Si < 1.75$, $CaH_2SiO_4\cdot nCa(OH)_2$ phase + $Ca(OH)_2$ .

Table 1. Reference set of $\Delta G^{0}_{298.15}$ for aqueous species and solids used in calculations.

<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Ref</th>
      <th>$\Delta G^{0}_{298.15}$ (J/mol)</th>
      <th>Species</th>
      <th>Ref</th>
      <th>$\Delta G^{0}_{298.15}$ (J/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6">AQUEOUS SPECIES</td>
    </tr>
    <tr>
      <td>$Al(OH)^{+2}$</td>
      <td>S92</td>
      <td>-696272</td>
      <td>$Fe^{+3}$</td>
      <td>S92</td>
      <td>-17238</td>
    </tr>
    <tr>
      <td>$Al(OH)_{2}^{+}$</td>
      <td>S92</td>
      <td>-904079</td>
      <td>$Fe(OH)_{3}^{\circ}$</td>
      <td>IR</td>
      <td>-659570</td>
    </tr>
    <tr>
      <td>$Al(SO_{4})^{+}$</td>
      <td>IR</td>
      <td>-1252053</td>
      <td>$Fe(OH)_{4}^{-}$</td>
      <td>IR</td>
      <td>-843353</td>
    </tr>
    <tr>
      <td>$Al(SO_{4})_{2}^{-}$</td>
      <td>IR</td>
      <td>-1845301</td>
      <td>$Fe(SO_{4})^{+}$</td>
      <td>IR</td>
      <td>-784756</td>
    </tr>
    <tr>
      <td>$Al^{+3}$</td>
      <td>S92</td>
      <td>-487616</td>
      <td>$Fe(SO_{4})_{2}^{-}$</td>
      <td>IR</td>
      <td>-1536865</td>
    </tr>
    <tr>
      <td>$AlO_{2}^{-}$</td>
      <td>S92</td>
      <td>-831361</td>
      <td>$H_{2}^{\circ}$</td>
      <td>S92</td>
      <td>17723</td>
    </tr>
    <tr>
      <td>$HAlO_{2}^{\circ}$</td>
      <td>S92</td>
      <td>-869854</td>
      <td>$O_{2}^{\circ}$</td>
      <td>S92</td>
      <td>16544</td>
    </tr>
    <tr>
      <td>$NaAlO_{2}^{\circ}$</td>
      <td>S92</td>
      <td>-1088961</td>
      <td>$Mg^{+2}$</td>
      <td>S92</td>
      <td>-453984.9</td>
    </tr>
    <tr>
      <td>$Ca(HSO_{4})^{+}$</td>
      <td>IR</td>
      <td>-1314716</td>
      <td>$MgOH^{+}$</td>
      <td>IR</td>
      <td>-623960</td>
    </tr>
    <tr>
      <td>$Ca(OH)^{+}$</td>
      <td>IR</td>
      <td>-717026</td>
      <td>$MgSO_{4}^{\circ}$</td>
      <td>IR</td>
      <td>-1211272</td>
    </tr>
    <tr>
      <td>$CaSO_{4}^{\circ}$</td>
      <td>IR</td>
      <td>-1309990</td>
      <td>$NaHSiO_{3}^{\circ}$</td>
      <td>S92</td>
      <td>-1285074</td>
    </tr>
    <tr>
      <td>$Ca^{+2}$</td>
      <td>S92</td>
      <td>-552790</td>
      <td>$NaOH^{\circ}$</td>
      <td>S92</td>
      <td>-414613</td>
    </tr>
    <tr>
      <td>$Fe^{+2}$</td>
      <td>S92</td>
      <td>-91504</td>
      <td>$NaSO_{4}^{-}$</td>
      <td>IR</td>
      <td>-1009771</td>
    </tr>
    <tr>
      <td>$Fe(HSO_{4})^{+}$</td>
      <td>IR</td>
      <td>-853425</td>
      <td>$Na^{+}$</td>
      <td>S92</td>
      <td>-261881</td>
    </tr>
    <tr>
      <td>$Fe(OH)^{+}$</td>
      <td>IR</td>
      <td>-281331</td>
      <td>$HSO_{4}^{-}$</td>
      <td>S92</td>
      <td>-755756</td>
    </tr>
    <tr>
      <td>$Fe(OH)_{2}^{\circ}$</td>
      <td>IR</td>
      <td>-458480</td>
      <td>$SO_{4}^{-2}$</td>
      <td>S92</td>
      <td>-744459</td>
    </tr>
    <tr>
      <td>$Fe(OH)_{3}^{-}$</td>
      <td>IR</td>
      <td>-620589</td>
      <td>$HSiO_{3}^{-}$</td>
      <td>S92</td>
      <td>-1013783</td>
    </tr>
    <tr>
      <td>$Fe(SO_{4})^{\circ}$</td>
      <td>IR</td>
      <td>-848521</td>
      <td>$SiO_{2}^{\circ}$</td>
      <td>S92</td>
      <td>-833411</td>
    </tr>
    <tr>
      <td>$Fe(HSO_{4})^{+2}$</td>
      <td>IR</td>
      <td>-787143</td>
      <td>$OH^{-}$</td>
      <td>S92</td>
      <td>-157298</td>
    </tr>
    <tr>
      <td>$Fe(OH)^{+2}$</td>
      <td>IR</td>
      <td>-241947</td>
      <td>$H^{+}$</td>
      <td>S92</td>
      <td>0</td>
    </tr>
    <tr>
      <td>$Fe(OH)_{2}^{+}$</td>
      <td>IR</td>
      <td>-458721</td>
      <td>$H_{2}O^{\circ}$</td>
      <td>S92</td>
      <td>-237181</td>
    </tr>
    <tr>
      <td colspan="6">SOLIDS</td>
    </tr>
    <tr>
      <td>$Al(OH)_{3}$</td>
      <td>RH</td>
      <td>-1154900</td>
      <td>$CaSO_{4}(H_{2}O)_{2}$</td>
      <td>RH</td>
      <td>-1797361</td>
    </tr>
    <tr>
      <td>$Al_{2}Si_{2}O_{5}(OH)_{4}$</td>
      <td>RH</td>
      <td>-3797500</td>
      <td>$Mg(OH)_{2}$</td>
      <td>RH</td>
      <td>-833500</td>
    </tr>
    <tr>
      <td>$Ca(OH)_{2}$</td>
      <td>RH</td>
      <td>-898426</td>
      <td>$Mg_{3}Si_{2}O_{5}(OH)_{4}$</td>
      <td>RH</td>
      <td>-4032400</td>
    </tr>
    <tr>
      <td>$Fe_{3}O_{4}$</td>
      <td>M</td>
      <td>-1011110</td>
      <td>$NaSi_{7}O_{13}(OH)_{3}(H_{2}O)_{3}$</td>
      <td>M</td>
      <td>-7373040</td>
    </tr>
    <tr>
      <td>$HFeO_{2}$</td>
      <td>M</td>
      <td>-487857</td>
      <td>$SiO_{2}$</td>
      <td>RH</td>
      <td>-850559</td>
    </tr>
  </tbody>
</table>

References: S92 - SPRONS92 database [22] and its extensions; IR - calculated using isocoulombic reactions and REACDC procedure [12] from selected LogK [19] of association / dissociation reactions; RH - Robie and Hemingway, 1995 [23]; M - Melnik, 1986 [24].

Similar model has been suggested by Sinitsyn et al. [19] for thermodynamic description of interactions between concrete construction materials and aqueous solutions inside Chernobyl Unit-4 Shelter. In [19], phase associations (1) and (2) [13] has been regarded as one solid solution (CSH1 phase) with $SiO_{2}$ and $CaH_{2}SiO_{4}$ end-members. $1.0 < Ca/Si < 1.7$ range was covered by another solid solution (CSH2) of $CaH_{2}SiO_{4}$ and $Ca_{1.7}H_{3.4}SiO_{5}\cdot 4H_{2}O$ end-members; and at Ca/Si $< 1.7$, association of two phases has been assumed, CSH2 and $Ca(OH)_{2.cr}$. Ideal models were used for both CSH1 and CSH2 solid solutions. Good agreement between experimental solubility data [3, 13-18] and Ca molalities calculated using *Selector-A* code has been considered as a criterion of model applicability.

In this study, our previous CSH model was improved by replacing $CaH_{2}SiO_{4}$ end-members (Ca/Si = 1) in CSH1 and CSH2 phases with end-members with $Ca/Si = 0.9$ ($Ca_{0.9}SiO_{3.8}H_{1.8}$). This pro-

![](./images/811669836340920321_1.jpg)

Fig. 1. Predicted (lines) and experimental (points) solubility of CSH in the $CaO-SiO_2-H_2O$ system.
A and B: Total concentrations of Ca and Si in aqueous solution; C: Calculated speciation in aqueous solution;
D: Calculated speciation of solid components in CSH.

Table 2. Comparison of experimental and modeled CSH solubilities in NaOH solution (mmol/L)

<table>
  <thead>
    <tr>
      <th>Initial
NaOH
conc.</th>
      <th>Ca/Si
Ratio</th>
      <th colspan="2">Experimental</th>
      <th colspan="4">Modeling</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Ca
Bennett et al. [3]</th>
      <th>Si
Bennett et al. [3]</th>
      <th>Ca
Bennett et al. [3]</th>
      <th>Si
Bennett et al. [3]</th>
      <th>Ca
This work</th>
      <th>Si
This work</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>400</td>
      <td>1.0</td>
      <td>0.15</td>
      <td>0.44</td>
      <td>0.035</td>
      <td>45.0</td>
      <td>0.23</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>400</td>
      <td>1.4</td>
      <td>1.2</td>
      <td>0.71</td>
      <td>0.47</td>
      <td>6.30</td>
      <td>6.90</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>400</td>
      <td>1.9</td>
      <td>1.30</td>
      <td>0.024</td>
      <td>1.20</td>
      <td>2.40</td>
      <td>5.88</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>600</td>
      <td>1.0</td>
      <td>0.10</td>
      <td>0.70</td>
      <td>0.015</td>
      <td>140.00</td>
      <td>0.63</td>
      <td>0.104</td>
    </tr>
    <tr>
      <td>600</td>
      <td>1.4</td>
      <td>0.80</td>
      <td>0.035</td>
      <td>0.32</td>
      <td>12.00</td>
      <td>4.79</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>600</td>
      <td>1.9</td>
      <td>0.90</td>
      <td>0.04</td>
      <td>0.82</td>
      <td>4.80</td>
      <td>4.55</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>800</td>
      <td>1.0</td>
      <td>0.14</td>
      <td>0.64</td>
      <td>0.011</td>
      <td>200.00</td>
      <td>0.30</td>
      <td>0.161</td>
    </tr>
    <tr>
      <td>800</td>
      <td>1.4</td>
      <td>0.64</td>
      <td>0.12</td>
      <td>0.24</td>
      <td>18.00</td>
      <td>4.23</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>800</td>
      <td>1.9</td>
      <td>0.70</td>
      <td>0.10</td>
      <td>0.61</td>
      <td>7.40</td>
      <td>4.13</td>
      <td>0.010</td>
    </tr>
  </tbody>
</table>

duced even better agreement between calculated and experimental solubility, especially in 0.9 < Ca/Si < 1.3 range. This update is also substantiated by the existence of stable tobermorite-like hydrated calcium silicates with Ca/Si mole ratio less than 1.0 [18, 20]. Fig.1 shows the predicted solubility of CSH in pure water as function of Ca/Si mole ratio in solid, compared with the available experimental data [3, 13-18]. Calculations were conducted at 1 mole of solid (CaO+ SiO₂) per 1 kg H₂O, that is, close to solid/water ratios used in many of referred experimental studies. Total concentrations of dissolved Ca and Si, aqueous speciation, amounts of solid phases and their composition (moles of end-members) have been calculated using reference thermodynamic properties of compounds (Table 1), with $\Delta G^{\mathrm{o}}_{\mathrm{f}, 298}$ of $\mathrm{Ca}_{1.7} \mathrm{H}_{3.4} \mathrm{SiO}_{5.4}\left(\mathrm{H}_{2} \mathrm{O}\right)_{4}\left(\mathrm{C}_{1.7} \mathrm{SH}_{4}\right)$, $\mathrm{Ca}_{0.9} \mathrm{SiO}_{3.8} \mathrm{H}_{1.8}\left(\mathrm{C}_{0.9} \mathrm{SH}_{0.9}\right)$ and $\mathrm{Ca}(\mathrm{OH})_{2}{ }^{\mathrm{o}}$ evaluated in this work (see below).

Quantitative account of influence of alkali metals on cement/aqueous chemical interactions is regarded as another unresolved problem in cement chemistry, discussed in [3,4,21]. We tried to model the experimental data on CSH solubilities in NaOH solutions [3]. Our approach included extension of two CSH ideal solid solution phases by adding some Na-containing end-members. Because there are no experimental clarifying the stoichiometry of sodium end-members in CSH, different Na-Si and Na-Ca-Si compounds were tested as end-members for improving thermodynamic description of solubility data as function of Ca/Si in solid and initial NaOH concentration.

Introduction of Na silicate end-members into CSH1 and CSH2 ideal solid solutions did not permit reasonable prediction of dissolved Ca and Si concentrations. Evidently, calcium-sodium exchange can not explain Na partitioning between solid and aqueous phases. The same conclusion has been done in [3]. Much more reasonable solubilities were calculated using Ca-Na hydrate silicate end-members. An example calculation based on the simplest model of sodium-bearing CSH with $\mathrm{CaNaH}_{2} \mathrm{SiO}_{4}(\mathrm{OH})$ end-members added to CSH1 and CSH2 solid solutions is presented in Table 2. Deviations of calculated solubilities from experimental data [3] do not exceed one order of magnitude of Ca and Si molalities, which is better than that obtained in [3], but still not quite satisfactory. Further improvement of the ideal alkali-CSH model is possible by introducing more Na-containing end members, or by developing a non-ideal model, fitting interaction parameters for end-member activity coefficients [7]. In any case, as concluded in [4], without more experimental and phase-identification data, the present prospects for accurate modeling of alkali concentration in cement pore waters, based on fundamental knowledge of the processes, are not promising.

**Table 3. Comparison of experimentally determined solubilities of some cement hydrate phases with modeled results (mmol/L).**

<table>
  <thead>
    <tr>
      <th>Phase</th>
      <th>Ca</th>
      <th>Si</th>
      <th>Al</th>
      <th>SO₄⁻²</th>
      <th>Mg</th>
      <th>pH</th>
      <th>Model phases</th>
      <th>Ref</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aft</td>
      <td>1.47<br>1.21-2.67<br>1.822</td>
      <td></td>
      <td>0.45<br>0.29-0.65<br>0.608</td>
      <td>1.00<br>0.97-1.68<br>0.916</td>
      <td></td>
      <td>10.9-11.4<br>11.0</td>
      <td>Aft</td>
      <td>[17]<br>[3]<br>*</td>
    </tr>
    <tr>
      <td>Afm</td>
      <td>6.84-5.05<br>5.81</td>
      <td></td>
      <td>3.52-2.70<br>3.87</td>
      <td>0.01-0.02<br>0.005</td>
      <td></td>
      <td></td>
      <td>Hgr,<br>Aft</td>
      <td>[17]<br>*</td>
    </tr>
    <tr>
      <td>Hgr</td>
      <td>6.14<br>5.11-7.43<br>5.81</td>
      <td></td>
      <td>4.57<br>3.80-5.20<br>3.88</td>
      <td></td>
      <td></td>
      <td>11.3-11.9<br>11.8</td>
      <td>Hgr</td>
      <td>[17]<br>[3]<br>*</td>
    </tr>
    <tr>
      <td>Gh</td>
      <td>2.0 - 0.91<br>0.36-2.00<br>0.84</td>
      <td>0.01-0.027<br>0.014-0.05<br>0.012</td>
      <td>0.97-0.61<br>0.29-0.97<br>1.09</td>
      <td></td>
      <td></td>
      <td>10.4-11.2<br>10.7</td>
      <td>Gh,Gs</td>
      <td>[17]<br>[3]<br>*</td>
    </tr>
    <tr>
      <td>Htc</td>
      <td></td>
      <td></td>
      <td>0.014-0.008<br><br>0.014-0.010<br><br>0.011</td>
      <td></td>
      <td>0.033-0.060<br>0.033-0.035<br>0.020</td>
      <td>9.3<br><br>9.46</td>
      <td>Htc</td>
      <td>[17]<br>[3]<br>*</td>
    </tr>
  </tbody>
</table>

Gs - grossular end-member; * - this work, model

Ettringite (Aft), monosulfate (Afm), gehlenite (Gh), hydrotalcite (Htc) and hydrogarnet (Hgr) solubility data [3,17] were processed for evaluation of $\Delta \text{G}^{0}_{298.15}$ values of these cement hydrate phases. Predicted solubilities (Table 3) have been obtained using $\Delta \text{G}^{0}_{298.15}$ (Table 4) calculated from ion activity products for the above phases [3] and reference $\Delta \text{G}^{0}_{298.15}$ values for aqueous species (Table 1). Experimental data [3,17] and calculated values (Table 3) are in reasonable agreement, therefore no further corrections of thermodynamic data for Aft, Afm, Gh, Htc, and Hgr have been made. Moreover, the experimental congruent dissolution of Aft, Hgr and Htc was reproduced in the model, as well as incongruent dissolution of Afm and Gh.

The proposed multiphase aqueous - ideal solid solution model for Portland cement SSAS is based on the above modeling results for separate cement phases. The multiphase model includes: non-ideal Na-Ca-Mg-Fe-Al-Si-S-O₂-H₂O aqueous electrolyte; CH (portlandite), Aft and Htc single-component phases; three ideal solid solution phases: CSH1 with SiO₂, $\text{Ca}_{0.9}\text{H}_{1.8}\text{SiO}_{3.8}$ and $\text{CaH}_{2}\text{SiO}_{4}\cdot\text{NaOH}$ end-members; CSH2 with $\text{Ca}_{0.9}\text{H}_{1.8}\text{SiO}_{3.8}$, $\text{Ca}_{1.7}\text{H}_{3.4}\text{SiO}_{5.4}\cdot4\text{H}_{2}\text{O}$ and $\text{CaH}_{2}\text{SiO}_{4}$ ·NaOH end-members; and hydrogarnet. The latter, besides Hgr and Gs (grossular) end- members proposed in [3], includes ferrihydrogarnet ($\text{Ca}_{3}\text{Fe}_{2}\text{O}_{6}\cdot\text{H}_{2}\text{O}$, FHgr) end member. $\Delta \text{G}^{0}_{298.15}$ for FHgr was calculated from $\log \text{K}_{sp}$ [1]. We did not attempt to model an immiscibility gap for hydrogarnet solid solution [3] because description of exsolution phenomena requires introduction of strong non-ideality into the model. Table 4 contains $\Delta \text{G}^{0}_{298.15}$ of species estimated in this work.

## 4. MODEL COMPOSITION OF CEMENT PORE SOLUTIONS

Experimental compositions of cements and pore solutions of different aging times (84 days [25] and 300 days [26]) have been used for testing the above multiphase thermodynamic model by

Table 4. Estimated values of $\Delta \mathrm{G}_{\text {298.15 }}^{\mathrm{o}}$ for $\mathrm{Ca}(\mathrm{OH})_{2}{ }^{\mathrm{o}}$ and cement hydrate solid components.

<table>
  <thead>
    <tr>
      <th colspan="2">Components</th>
      <th>$\Delta \mathrm{G}_{298.15}^{\mathrm{o}}$ (J/mol)</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\mathrm{Ca}(\mathrm{OH})_{2}{ }^{\mathrm{o}}(\mathrm{aq})$</td>
      <td></td>
      <td>-884819.0</td>
      <td>From portlandite solubility</td>
    </tr>
    <tr>
      <td>$\mathrm{CaH}_{2} \mathrm{SiO}_{4} \cdot \mathrm{NaOH}$</td>
      <td>$\left(\mathrm{CN}_{0.5} \mathrm{SH}_{1.5}\right)$</td>
      <td>-2211863.7</td>
      <td>Solubility of CSH + NaOH [3]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{0.9} \mathrm{SiH}_{1.8} \mathrm{O}_{3.8}$</td>
      <td>$\left(\mathrm{C}_{0.9} \mathrm{SH}_{0.9}\right)$</td>
      <td>-1681324.6</td>
      <td>CSH solubility (see text)</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{1.7} \mathrm{H}_{3.4} \mathrm{SiO}_{5.4} \cdot 4 \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{C}_{1.7} \mathrm{SH}_{5.4}\right)$</td>
      <td>-3351539.4</td>
      <td>CSH solubility (see text)</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{3} \mathrm{Al}_{2} \mathrm{O}_{6} \cdot 6 \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{C}_{3} \mathrm{AH}_{6}\right)$</td>
      <td>-5020021.4</td>
      <td>From solubility data [3, 17]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{3} \mathrm{Fe}_{2} \mathrm{O}_{6} \cdot 6 \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{C}_{3} \mathrm{FH}_{6}\right)$</td>
      <td>-4147548.6</td>
      <td>From $\mathrm{LogK}_{\mathrm{sp}}$ [1]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{3} \mathrm{Al}_{2} \mathrm{Si}_{3} \mathrm{O}_{12}$</td>
      <td>$\left(\mathrm{C}_{3} \mathrm{AS}_{3}, \mathrm{Gs}\right)$</td>
      <td>-6237668.0</td>
      <td>From Gh dissolution [3,17]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{2} \mathrm{Al}_{2} \mathrm{SiO}_{7} \cdot 8 \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{C}_{2} \mathrm{ASH}_{8}\right)$</td>
      <td>-5716998.3</td>
      <td>From solubility data [3, 17]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{4} \mathrm{Al}_{2} \mathrm{SO}_{10} \cdot \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{C}_{4} \mathrm{ASH}_{12}, \mathrm{Afm}\right)$</td>
      <td>-7779300.5</td>
      <td>From solubility data [17]</td>
    </tr>
    <tr>
      <td>$\mathrm{Ca}_{6} \mathrm{Al}_{2} \mathrm{~S}_{3} \mathrm{O}_{12}(\mathrm{OH})_{12}$</td>
      <td>$\left(\mathrm{C}_{6} \mathrm{AS}_{3} \mathrm{H}_{12}, \mathrm{Aft}\right)$</td>
      <td>-9050700.9</td>
      <td>From solubility data [3, 17]</td>
    </tr>
    <tr>
      <td>$\mathrm{Mg}_{4} \mathrm{Al}_{2} \mathrm{O}_{7} \cdot 10 \mathrm{H}_{2} \mathrm{O}$</td>
      <td>$\left(\mathrm{M}_{4} \mathrm{AH}_{10}\right)$</td>
      <td>-6402148.6</td>
      <td>From solubility data [3, 17]</td>
    </tr>
  </tbody>
</table>

Table 5. Comparison of experimental and predicted cement pore water compositions (total ion concentrations in mmol/L).

<table>
  <thead>
    <tr>
      <th>Ca</th>
      <th>Si</th>
      <th>Al</th>
      <th>$\mathbf{SO_4^{-2}}$</th>
      <th>Mg</th>
      <th>K</th>
      <th>Na</th>
      <th>pH</th>
      <th>Ref</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>27</td>
      <td>-</td>
      <td>639</td>
      <td>323</td>
      <td>-</td>
      <td>[25]</td>
    </tr>
    <tr>
      <td>0.69</td>
      <td>5.7</td>
      <td>0.22</td>
      <td>228</td>
      <td>$10^{-6}$</td>
      <td>947</td>
      <td>483</td>
      <td>13.83</td>
      <td>[4]</td>
    </tr>
    <tr>
      <td>18.2</td>
      <td>0.01</td>
      <td>0.008</td>
      <td>0.023</td>
      <td>$7 \cdot 10^{-6}$</td>
      <td>-</td>
      <td>4.87</td>
      <td>12.39</td>
      <td>[U]</td>
    </tr>
    <tr>
      <td>4.23</td>
      <td>1.16</td>
      <td>0.14</td>
      <td>5.44</td>
      <td>$5 \cdot 10^{-7}$</td>
      <td>-</td>
      <td>455</td>
      <td>13.42</td>
      <td>[C]</td>
    </tr>
    <tr>
      <td>2.3</td>
      <td>0.2</td>
      <td>0.19</td>
      <td>-</td>
      <td>0.008</td>
      <td>161</td>
      <td>65</td>
      <td>13.4</td>
      <td>[26]</td>
    </tr>
    <tr>
      <td>0.70</td>
      <td>5.2</td>
      <td>0.22</td>
      <td>196</td>
      <td>$10^{-6}$</td>
      <td>1035</td>
      <td>281</td>
      <td>13.81</td>
      <td>[4]</td>
    </tr>
    <tr>
      <td>18.8</td>
      <td>0.01</td>
      <td>0.006</td>
      <td>0.026</td>
      <td>$8 \cdot 10^{-6}$</td>
      <td>-</td>
      <td>3.4</td>
      <td>12.38</td>
      <td>[U]</td>
    </tr>
    <tr>
      <td>4.39</td>
      <td>0.88</td>
      <td>0.09</td>
      <td>4.16</td>
      <td>$5 \cdot 10^{-7}$</td>
      <td>-</td>
      <td>375</td>
      <td>13.35</td>
      <td>[C]</td>
    </tr>
  </tbody>
</table>

[U]: this work, uncorrected $\Delta \mathrm{G}_{298.15}^{\mathrm{o}}(\mathrm{CN}_{0.5} \mathrm{SH}_{1.5})=-2211864 \mathrm{~J} / \mathrm{mole}$;
[C]: this work, corrected $\Delta \mathrm{G}_{298.15}^{\mathrm{o}}(\mathrm{CN}_{0.5} \mathrm{SH}_{1.5})=-2194864 \mathrm{~J} / \mathrm{mole}$.

calculating equilibria at water/solid ratio 0.5. Model calculations (Table 5) show that no satisfactory result can be obtained using thermodynamic data (Table 4) derived from experimental solubility of separate phases. The main source of this inconsistency can be traced to inadequate stability of $\mathrm{CN}_{0.5} \mathrm{SH}_{1.5}$ end member in CSH1 and CSH2 phases. As pointed out by E.Reardon [4], the partition of alkali between solid and aqueous phases appears to be different in studies on solubility of CSH in NaOH/KOH solutions and on composition of cement pore waters. Modeling data in Table 5 clearly reflect the same situation. For better agreement with porewater data, the

$\Delta G^{0}_{298.15}$ value of $CN_{0.5}SH_{1.5}$ was made 17 kJ/mole more positive, and calculations performed again ("corrected" model, Table 5). This permitted to obtain reasonable consistency between calculated and measured composition of cement porewaters, especially for more aged cement [26]. Comparing lines U and C in Table 5 with the corresponding experimental data, it is easy to see how important it is to achieve the correct thermodynamic description of the behavior of alkali in the Portland cement system. Next steps on this way could be done when more extensive and precise experimental data on alkali partitioning between solid and aqueous phases, as a basis for development of the non-ideal models of alkali-CSH phases.

## 5. CONCLUSIONS
1. SSAS thermodynamic model based on GEM provides simple yet rigorous description of published solubility data in $Ca-Si-Al-Fe-Na-H_{2}O$ cement systems.
2. The model can be fine-tuned and extended by incorporating new end-members of radionuclides and other "doping" components, provided that relevant solubility and crystal-chemical data become available.
3. GEM approach opens a direct way towards thermodynamic predictions of long-time behavior of cements, reflecting growing knowledge about the nature and mechanisms of physical-chemical transformations in cementitious waste-isolating systems.

## REFERENCES
1. J.Lee, D.Roy, B.Mann and D.Stahl, Mat.Res.Soc.Symp.Proc., 353 (1995).
2. F.Glasser, D.Macphee and E.Lachovski, Mat.Res.Soc.Symp.Proc.112 (1988).
3. D.Bennett, D.Read, M.Atkins, and F.Glasser, Jour. Nucl. Materials, 190 (1992).
4. E.Reardon, Waste Management, 12 (1992).
5. M.Kersten, Environ.Sci.Technol., 30 (1996).
6. M.Reed, Geoch.Cosmoch.Acta 46 (1982).
7. D.Kulik, V.Sinitsyn, and I.Karpov (1997: this volume).
8. I.Karpov, Computer-aided physicochemical modeling in geochemistry. (Nauka publ., Novosibirsk. 1981), in Russian.
9. Yu.Shvarov, The algorithms to determine the equilibrum composition of multicomponent heterogeneous system. Ph.D. dissertation, Moscow State University (1982, in Russian).
10.I.Karpov, D.Kulik, K.Chudnenko, In: Water-Rock Interaction. 8. Eds: Y.Kharaka, O.Chudaev (Balkema, Rotterdam, 1995).
11.D.Kulik, Ibid.
12.D.Kulik, S.Dmitrieva, K.Chudnenko et al. (1997): Selektor-A test-version 3.1$\beta$ for DOS. User's Manual (draft). (Brooklyn, 1997).
13.S.Greenberg and T.Chang, J. Phys.Chem. 69 (1965).
14.E.Flint and L.Wells, J.Nat.Bur.Stand. 12 (1934).
15.P.Roller and G.Ervin Jr., J.Am.Chem.Soc. 62 (1940).
16.H.Taylor, J.Chem. Soc. London, 276 (1950).
17.M.Atkins, F.Glasser, and A.Kindness, Cem. Concr. Res. 22 (1992).
18.K.Fuji and W.Kondo, J.Amer.Ceram.Soc. 66 (1983).
19.V.Sinitsyn, D.Kulik, M.Khodorivski et.al., Mat.Res.Soc.Symp.Proc. 465 (1997).
20.H.Taylor, Z.Krist. 41 (1992).
21.H.Taylor, Adv. Cem. Res. 1 (1987).
22.J.Johnson, E.Oelkers, and H.Helgeson, Comput. Geosci. 18 (1992).
23.R.Robie and B.Hemingway, U.S.Geol.Surv.Bull. 2141 (1995).
24.Yu.Melnik, Genesis of Precambrian Iron Formations (Nauk.Dumka, Kyiv,1986) (in Russian).
25.C.Page and O.Vennesland, Rev. Mater. Constr. 16 (1983).
26.K.Andersson, B.Allaard, M.Bengtsson, and B.Magnusson, Cem.Concr.Res., 19 (1989).

960