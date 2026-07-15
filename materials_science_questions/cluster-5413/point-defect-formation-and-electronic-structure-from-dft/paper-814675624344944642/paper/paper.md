# Theoretical evaluation of the surface electrochemistry of perovskites with promising photon absorption properties for solar water splitting†

Joseph H. Montoya, $^{a}$ Monica Garcia-Mota, $^{a}$ Jens K. Nørskov $^{ab}$ and Aleksandra Vojvodic $^{*ab}$

In this work, we present first-principles calculations describing the catalytic activity for of a set of photoelectrocatalysts identified as candidates for total water splitting in a previous screening study for bulk stability and bandgap. Our Density Functional Theory (DFT) calculations of the intermediate energetics for hydrogen evolution and oxygen evolution suggest that none of the proposed materials has the ideal combination of bandgap and surface chemical properties that should allow for total water splitting in a single material. This result suggests that co-catalysts are necessary to overcome the kinetic limitations of the both reactions, although some materials may catalyze one half-reaction, as has been observed in experiment.

## Introduction

Concern over the environmental impacts of conventional fossil fuel production and consumption has increased considerably over the past decade, making technologies that store the energy of sunlight in chemical bonds particularly attractive for research and development. One proposed device design is that of a photoelectrocatalytic cell, in which a semiconducting photo- anode and cathode generate electron-hole pairs that oxidize water and reduce protons, respectively. In addition, recent reports from Castelli *et al.* and Wu *et al.*$^{1,2}$ have shown that calculations from electronic structure theory can guide the search for bulk light-harvesting materials by efficiently identifying promising candidates among a large sample size of untested semiconductor materials.

Theory has also provided key insights into the fundamental limitations of various catalytic and electrocatalytic processes, particularly in electrochemical oxygen (OER)$^{3}$ and hydrogen (HER)$^{4}$ evolution reactions. Density functional theory (DFT) calculations demonstrate that the intermediate hydrogen binding energy correlates with catalytic activity, and these calculations even inspired the discovery of new active materials for HER.$^{5}$

For the anodic half-reaction, DFT studies have shown that the four-step OER mechanism is limited fundamentally to a minimum overpotential of 0.3–0.4 V due to scaling of OH* and OOH* intermediates.$^{3,6}$

A device constructed a single photoelectrocatalyst material should need not only to exceed the HER and OER equilibrium potentials with its conduction and valence band edges, respectively, but also the overpotentials in order to catalyze each half-reaction at a reasonable rate. This need to exceed the required overpotential with the bandgap is further complicated by shunts and free energy losses that contribute to inefficiencies in photovoltaic devices. A recent analysis from Seitz *et al.*$^{7}$ sets the best-case net free energy losses from entropic, mobility, light-trapping, and recombination effects at 0.49 eV. Hence, bandedges of individual materials should clear the kinetic overpotential barriers by a total additional margin of at least 0.5 eV in order to actually split water *in situ*, and may need even wider bandgaps if shunting resistances are significant.$^{8,9}$

In this work, we set out to determine whether the promising candidates identified by Castelli *et al.* for their bulk stability and optical properties well-suited to total water splitting also possessed the surface chemical properties necessary to catalyze that reaction with a high turnover rate.$^{1}$ To achieve this goal, we report calculations for the theoretical electrocatalytic HER and OER overpotentials using DFT. Using our results, we demonstrate that electron-hole pairs generated from these bulk materials may not be sufficient to overcome the inherent OER and HER overpotentials on any of the surfaces considered. Ultimately, our conclusion from theory can be applied towards strategies for

$^{a}$ SUNCAT Center for Interface Science and Catalysis, Department of Chemical Engineering, Stanford University, Stanford, USA. E-mail: alevoj@stanford.edu, norskov@stanford.edu
$^{b}$ SUNCAT Center for Interface Science and Catalysis, SLAC National Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, USA
† Electronic supplementary information (ESI) available. See DOI: 10.1039/c4cp05259e

photoelectrochemical device design since it suggests that active co-catalysts, in addition to optimal light absorbers, may be crucial to allow for total water splitting at reasonable electrochemical turnover rates.

## Methods
In this study, self-consistent plane wave DFT calculations implemented in the Quantum Espresso¹⁰ software package are used to calculate adsorption energies of *O, *OH, and *OOH on the B site of a BO₂-terminated [100] perovskite surface, since this surface is the most stable for perovskite compounds.¹¹ Surfaces were constructed by geometrically optimizing a $2 \times 2 \times 2$ bulk cubic unit cell after rattling the crystal symmetry and allowing the atoms to form distorted octahedral structures that occur in natural $p3m3$ perovskites.¹²,¹³ This bulk structure was used to construct a supercell consisting of a $2 \times 2 \times 4$ slab with $10$ Å of vacuum in the z-direction. The adsorbates as well as the two top layers of the slab were allowed to relax, while the bottom two layers are kept fixed in the bulk positions. Periodic boundary conditions were used for all calculations, and a standard dipole correction was applied to correct both for the polarity of the surface and the induced dipole from the adsorbate. Brillouin-zone sampling was conducted using a $4 \times 4 \times 1$ Monkhorst–Pack mesh,¹⁴ and parameters of 400 and 4000 eV were used for energy and density cutoffs, respectively (see details in ESI†). An example of the geometry for the bare surface, adsorbates, and vacancy configurations are shown in Fig. 2 for LaTiO₂N.

All simulation results presented in this work use the revised Perdew–Burke–Ernzerhof (RPBE) exchange-correlation functional.¹⁵ Errors in calculations of energies related to water splitting for metal oxides using generalized-gradient approximation (GGA) functionals like RPBE are well-known. Oxygen bonding is a key element of our study, and for strongly-correlated systems (including late 3d elements) substantial errors in GGA oxygen bonding have been reported.¹⁶,¹⁷ A simple way to gauge errors in O bonding in metal oxides is to consider oxide heats of formation. In Fig. 1 we show that for the types of perovskites of interest for the present analysis, errors in O bonding are relatively small (mean absolute error of 0.24 eV per oxygen atom) and trends are very well reproduced by the present analysis. Details of this analysis can be found in the ESI.† Errors of this magnitude are not unlike those inherent to DFT, and since that the results reported here depend on energy differences between oxygen-derived adsorbates, this analysis provides some confidence that the reported overpotentials are sufficiently accurate to describe the materials considered. Furthermore, previous comparisons to both higher-level theory and experimental results demonstrate that GGA functionals are sufficient to describe trends in adsorption.³,¹⁸

![](./images/814675624344944642_1.jpg)

Fig. 1 Theoretical vs. experimental heats of formation $(\Delta H_f)$ for eleven common perovskite structures considered in this study vs. experimental values. Experimental values are adapted from ref. 19.

![](./images/814675624344944642_2.jpg)

Fig. 2 Schematics of LaTiO₂N slab. Leftmost column shows a perspective view of the $2 \times 2 \times 4$ computational cell with the B-site and O-site indicated using black arrows. The topmost layer represents the 100 surface. Subplots in center and right columns display top-down view of the LaTiO₂N (100) surface and configurations for OH*, O*, OOH*, H*–B, and H*–O adsorbates and a surface O vacancy at a 0.25 ML coverage. H*–B and H*–O refer to hydrogen adsorbates bound to the surface B metal and surface oxygen, respectively. The B and O adsorption sites were also considered for O*. These geometries were relaxed for each surface and used to determine the theoretical overpotentials and vacancy formation energies in Fig. 3 and 4.

The calculated theoretical overpotentials ($\eta_{\text{OER}}$ and $\eta_{\text{HER}}$), defined in ref. 20 as the minimum applied potential required such that each electrochemical step in a mechanism is downhill in free energy, are based on simulations with adsorbate coverage of $\theta = 0.25$ monolayers (ML), i.e. one adsorbate per four surface B-metal atoms as shown in Fig. 2. In this study, the theoretical OER overpotential assumes a mechanism proceeding *via* OH*, O*, and OOH*, and HER proceeds *via* a single intermediate, adsorbed H*, which is protonated directly to form H₂ gas. The computational hydrogen electrode (CHE) model

assigns the proton-electron pair in a proton-coupled electron transfer (PCET) reaction a free energy defined by the reversible hydrogen electrode (RHE). By setting the free energy of the proton-electron pair equal to that of hydrogen gas at standard conditions, the CHE allows for a rigorous theoretical treatment of PCET energetics on an RHE scale. Thus, individual PCET steps in the mechanism of a given electrochemical reaction can be calculated with a given applied voltage vs. RHE or vs. SHE (standard hydrogen electrode) with the appropriate pH correction to the equilibrium potential from the Nernst equation.

In practice the theoretical OER overpotential is dictated by the maximum free energy of reaction for the four oxidative steps from $H_2O$ to $O_2$ through these intermediates, typically the oxidation of $OH^*$ to $O^*$ or $O^*$ to $OOH^*$. Since these two steps likely determine the potential, and $OH^*$ and $OOH^*$ scale with a slope of unity, a descriptor of the free energy of $O^*$ binding minus that of $OH^*$ ($\Delta G_O - \Delta G_{OH}$) can be used to formulate a Sabatier volcano for $\eta_{OER}$ against a single variable, as formulated previously by Man et al.³

For HER via the Volmer-Heyrovsky mechanism assumed here, an applied potential ($U$) vs. RHE shifts the free energy of adsorption of proton-electron pairs to form $H^*$ by $-eU$, and the free energy of hydrogen formation by an adsorbed hydrogen and a proton-electron pair similarly. Since the precursor proton-electron pairs and the hydrogen gas have equal free energies at 0 V vs. RHE, the theoretical overpotential is dictated by the absolute value of the $H^*$ binding free energy ($\Delta G_H$) at 0 V vs. RHE, since an applied potential either must drive the adsorption of a proton from the solvent or the subsequent protonation of that $H^*$ adsorbate to form $H_2$ gas. Theoretical overpotentials based on the CHE for HER,⁴ OER,³ and other reactions involving PCET transfer steps²¹ have been shown previously to correlate well with experimentally measured current densities for both oxides and transition metal surfaces.

Corrections from the harmonic approximation to both the enthalpy and entropy were added to determine free energies of adsorption for each OER and HER intermediate. Note that this analysis excludes the effects of kinetic barriers associated with proton-coupled electron transfer (PCET). Tripković et al. have previously shown that PCET reactions on Pt(111) have very small barriers on the order of 0.2 eV,²² and we assume that this holds for the oxide materials presented in our analysis.

In addition, little data on the explicit water structure or its effects on adsorption energy of OER and HER intermediates on oxide surfaces is available, and therefore solvation effects are not included in these calculations. On the Pt(111) surface, previous studies have shown that $OH^*$ and $OOH^*$ may be stabilized by 0.5 and 0.25 eV in the presence of an explicit water layer, respectively.²² The net effect of the water layer on the overpotential is a 0.5 V increase for less reactive catalysts limited by the $OH^*$ to $O^*$ step, and a 0.25 V decrease for materials limited by the $O^*$ to $OOH^*$ step. If this solvation effect is applied, the qualitative interpretation of the results, i.e. whether or not the valence bandedge of a particular material is sufficiently low to overcome the OER overpotential, does not change.

As a first approximation, the calculated theoretical overpotentials are based on simulations with adsorbate coverage of $\theta = 0.25$ monolayers (ML), i.e. one adsorbate per four surface B-metal atoms as shown in Fig. 2. Later, the overpotential is recalculated in the high coverage regime corresponding to the most stable surface phase. The stability of surfaces with different adsorbate coverages was determined using the CHE model. Adsorbate coverages of $\theta = 0.5$, 0.75, and 1 ML for each adsorbate, including explicit simulated mixed coverages of $OH^*$ and $O^*$ were included in the study. The free energy of surface oxygen vacancy formation was also determined. Combining these, surface Pourbaix diagrams corresponding to the most stable surface coverage of $OH^*$, $O^*$, $H^*$ and vacancies as a function of pH and applied bias ($U$) using the CHE were constructed for each material.²³

The ESI† to this study contains a more detailed description of the analysis of heats of formation, more thorough summary of the overpotential calculation, and an explicit description of the mechanistic assumptions adapted from previous literature. In addition, thermodynamic data for each adsorption energy presented herein is provided, as well as a glossary of the symbols used.

## Results and discussion

In the following we first consider the OER and HER activity of each photocatalyst for a fixed surface structure and a low adsorbate coverage, see Fig. 3. We plot here the theoretical potential at which the OER and HER pathways become completely downhill in green and blue bars, respectively, alongside the indirect and direct bandgap of each material as previously calculated by Castelli et al.¹ Note that $CsNbO_3$ is omitted since it relaxes out of the perovskite phase upon geometric optimization of the surface.

Perhaps the most important aspect of the data shown in Fig. 3 is its suggestion that no single material seems to fit the requirements for both photoabsorber and electrocatalyst. Also notable is the lack of viable HER catalysts among the photoabsorbers at pH 7, which is consistent with a similar lack of HER photoelectrocatalysis in many of these materials without the presence of a co-catalyst. $CaSnO_3$ has an HER overpotential slightly below its conduction band edge that it might catalyze some hydrogen evolution at very low rates, but the margin between the direct band edge and the HER overpotential is likely too small to produce significant yields of $H_2$ at a reasonable turnover. $SnTiO_3$ also interestingly has an overpotential near the peak of the HER volcano, but should not catalyze HER at the conditions specified due to the correction applied for a pH of 7.0.

Note that the data shown in Fig. 3 include a Nernstian shift to the equilibrium potentials of OER and HER, and thus the positioning of the overpotential bars, upwards by 0.41 V in order to correct for a ambient pH of 7.0.²⁴ Since the bandedges are fixed relative to NHE (normal hydrogen electrode), according to the formulation in ref. 1, this suggests that some of these materials may not have the bandstructures required thermodynamically

![](./images/814675624344944642_3.jpg)

Fig. 3 Central plot shows theoretical overpotentials ($\eta$) for HER (blue) and OER (green), for $\theta$ = 0.25 ML, with direct and indirect bulk bandgaps positioned relative to RHE equilibrium potentials for fourteen candidate semiconductors for solar H₂O splitting at pH = 7.0. Indirect and direct bandgaps are adapted from Castelli et al.¹ Also shown are the OER (dashed green) and HER (dashed blue) equilibrium potentials (at pH = 7.0). The lower plot shows OER overpotentials (green points) with the OER volcano using $\Delta G_O - \Delta G_{OH}$ as a descriptor. Upper plot shows HER overpotentials (blue points) on the HER volcano.

for the splitting of H₂O in non-acidic electrolytes. Note also that the bandgaps presented in Fig. 3 could undergo shifts due to the presence of electronic states introduced by the termination of the surface or adsorbates. A more complete treatment would include these effects, but the data shown in Fig. 3 represent the best-case scenario for electrocatalysis using photogenerated electron-hole pairs, since these perturbations to the bandgap are likely to either reduce it or introduce trap states into the gap.¹⁶

We now turn to a more detailed treatment of the surface chemistry including considerations of surface phase and stability of the catalysts under reaction conditions. Surface vacancies, for example, may act as recombination centers for electron-hole pairs, perturb nearby active sites, act as active sites themselves, or simply initiate the bulk corrosion of the material. Thus, calculations of the surface oxygen-vacancy formation energies are shown in Fig. 4. Our analysis indicates roughly the conditions at which surface vacancies should begin to form, given that these energies are calculated relative to solvated protons in the CHE model and water. Positive values for vacancy formation energy suggest that the material remains stable even under reducing or acidic conditions, while negative ones suggest that vacancies should readily form under reducing conditions.

![](./images/814675624344944642_4.jpg)

Fig. 4 Oxygen vacancy formation energies ($\Delta E_{vac}$) for candidate materials calculated at 0 V vs. RHE. Positive values indicate stability at reducing potentials, i.e. less than 0.0 V vs. RHE. Values between 0.0 and -2.46 eV indicate vacancy formation at reducing potentials, but stable surfaces above the OER equilibrium potential, i.e. 1.23 V vs. RHE. Very negative values, less than -2.46 eV indicate spontaneous formation of surface vacancies even at very oxidizing conditions, i.e. greater than 1.23 V vs. RHE.

Highly exergonic oxygen vacancy formation, such as those found for CaGeO₃ and SrGeO₃, suggests that vacancies form even at oxidizing conditions. Therefore the BO₂-terminated surface of both SrGeO₃ and CaGeO₃ may be unstable under electrochemical conditions for OER. The remaining materials would not spontaneously form surface O vacancies under OER conditions. Under reducing conditions, however, only six of the considered surfaces would remain stable, which are SnTiO₃ and each of the oxynitrides. SnTiO₃ and MgTaO₂N also both have particularly low overpotentials for HER, suggesting that they might be both active and stable enough to produce hydrogen at low overpotentials in acid. The calculated OER overpotential for SnTiO₃ exceeds its valence bandedge, however, and MgTaO₂N could have problems retaining its nitrogen anions under oxidizing conditions similar to those observed for LaTiO₂N.

Considerations of adsorbate coverages of intermediates may also play a role in determining the overpotential for each material, and therefore determining the most stable surface coverage under a particular voltage and pH condition is necessary for a more physical description of the required overpotential. To determine this surface phase, Pourbaix diagrams were constructed and are shown in Fig. 5. The materials included in these diagrams were chosen due to their stability over a range of pH values and voltages encompassing both HER and OER. Nearly all of the oxides reconstruct, or form stable surface vacancies, upon the adsorption of high coverages of H*, further suggesting that they cannot remain stable under reducing conditions. In addition to

![](./images/814675624344944642_5.jpg)

Fig. 5 Surface Pourbaix diagrams for different adsorbate coverages ($\theta$) for six candidate materials. Pourbaix diagrams corresponding to the most stable surface configuration and coverage are shown for $LaTiO_{2}N$, $CaTaO_{2}N$, $SrTaO_{2}N$, $BaTaO_{2}N$, $MgTaO_{2}N$, and $SnTiO_{3}$. Lines corresponding to the OER low coverage theoretical overpotential, OER equilibrium potential, HER equilibrium potential, and HER low coverage theoretical overpotential are drawn on each Pourbaix diagram, demonstrating the surface coverage at that condition. Note also that oxygen vacancy defects were considered in this analysis, but were not found to be stable at any of the presented conditions for these materials, as per Fig. 4.

the oxynitrides, $SnTiO_{3}$ neither reconstructs with high $H^{*}$ coverages nor forms stable surface oxygen vacancies and therefore is included in Fig. 5. We find that surface coverages of either $OH^{*}$ or $OOH^{*}$ are higher for these materials under oxidizing conditions than $\theta = 0.25$ ML, suggesting that calculations at higher coverages may more accurately represent the state of the system.

To this effect, Fig. 6 shows the recalculated self-consistent overpotential for each of the oxynitrides and $SnTiO_{3}$. It is calculated in the high coverage regimes corresponding to the most stable surface phase. Note that higher coverages of $O^{*}$ on the surface cause a significant shift in the $\Delta G_{O} - \Delta G_{OH}$ descriptor to the right on the volcano in Fig. 6 for most of the materials shown. The corresponding theoretical overpotential also shift considerably at high coverages of $O^{*}$ by up to 1.5 V. Also note that some materials are shifted from the left leg of the volcano, indicating higher reactivity and a limiting step of $O^{*}$ to $OOH^{*}$, to the right leg of the volcano, indicating lower reactivity and a limiting step of $OH^{*}$ to $O^{*}$. Despite the magnitude of the shift, however, most of the materials shown in Fig. 5 are still not predicted to catalyze OER with an overpotential lower than around 1 V at pH 7, suggesting that even at high coverage conditions, none of the materials will be an efficient electrocatalyst without irradiation. Furthermore, $\Delta G_{O} - \Delta G_{OH}$ is still a good predictor of the OER overpotential at high coverage, which suggests that the best case overpotential for any of the materials is still greater than the 0.4 V from intermediate scaling.

Note also that the point representing $MgTaO_{2}N$ in the upper section of Fig. 6 shifts to the left, rather than to the right. This is due to the reconstruction involving formation of interstitial nitrogen in the subsurface layers during the geometric optimization, further suggesting that an attempt that surface layers might be susceptible to $N_{2}$ evolution and degradation, despite having an OER overpotential below the requirement given by its valence band edge.

![](./images/814675624344944642_6.jpg)

Fig. 6 Overpotentials and bandgaps for coverages obtained from the Pourbaix diagrams in Fig. 5. Lower figure shows low coverage overpotential as a function of low coverage $\Delta G_{O} - \Delta G_{OH}$ descriptor and high coverage overpotential as a function of high coverage descriptor for comparison. High coverage calculations use a precursor coverage of $\theta_{O} = 0.75$ ML, as per Fig. 5, i.e. adsorption energies are the energy difference when binding an additional adsorbate at this coverage. Low coverage calculations are at $\theta_{OH} = \theta_{O} = \theta_{OOH} = 0.25$ ML. High coverage limiting potentials are shown on the upper figure for OER (green bar) and HER (blue bar) along with direct (black line) and indirect (red line) bandgap. Dashed lines are the equilibrium potentials of $H_{2}O/O_{2}$ and $H^{+}/H_{2}$. As before, calculations assume a pH of 7.0.

If one considers the low and high coverage cases as lower and upper bounds for the reactivity, the ranges generated suggest that the oxynitrides might have some coverage which allows for OER catalysis near the peak of limiting potentials shown in Fig. 6. However, simultaneous HER catalysis is not predicted to occur on those materials at any reasonable pH, as each of the required HER overpotentials shown in Fig. 6 far exceeds the conduction bandedge, even without considering free energy losses or shunting.

However, some of the materials in Fig. 6 have OER overpotentials near or below the requirement dictated by their valence band edge, suggesting that photogenerated holes might

catalyze OER in the presence of a sacrificial reagent at the cathode or in a tandem system. $LaTiO_2N$, $CaTaO_2N$, and $BaTaO_2N$, for example, each have an OER overpotential within 0.3 V of their direct and indirect band edge, suggesting that they might catalyze OER alone under illumination at observable rates, if kinetic barriers to the formation of intermediates are low.

This interpretation agrees with observation of transient OER in at least one of the materials, $LaTiO_2N$, that reduces sacrificial $Ag^+$ species at the cathode, but the steady-state activity of this photocatalyst is observed to decrease as the $N^{3-}$ anions in the surface become oxidized to form $N_2$ gas, which is observed evolving from the surface.²⁵ Activity without a co-catalyst of the remaining compounds has not yet been reported on in literature to our knowledge. $CaTaO_2N$ and $BaTaO_2N$, for example, are predicted to have similar relative overpotentials to their band edges as $LaTiO_2N$, and could exhibit similar behavior. If it can be synthesized in the perovskite phase, $SnTiO_3$ in particular could be very promising, considering it has both an OER overpotential well-below its valence band edge and a high resistance to vacancy formation, as shown in Fig. 4. $SnTiO_3$ might also be less susceptible to corrosion of its bulk constituents than the oxynitrides.

## Conclusions

In this work, we have calculated theoretical overpotentials for HER and OER, providing a quantitative estimate for the thermodynamic requirement for applied voltage for both reactions on candidates with bandgaps well suited to solar $H_2O$-splitting. Low calculated overpotentials for HER suggest that certain materials, notably $SnTiO_3$ and $MgTaO_2N$, may merit further study as candidates for stand-alone catalysts. Of the tested materials, none in particular stands out as a particularly active OER electrocatalyst, but $CaTaO_2N$ may be the most active, if it can be stabilized at oxidizing conditions.

We further illustrate that surface stability under both HER and OER conditions is rare among these candidates. Oxynitride surfaces and $SnTiO_3$ are shown to have high oxygen vacancy formation energies, suggesting that they may be resistant to corrosion *via* a vacancy-mediated mechanism at HER conditions. Some oxynitrides, without co-catalysts, however, have been shown to degrade due to the oxidation of $N^{3-}$ and formation of $N_2$, which remains a concern for those materials. Bulk stability and phase also may further exclude certain candidates, and is not considered in this work.

Ultimately, we have demonstrated that theoretical calculations for OER and HER overpotentials suggest that the photovoltage for candidates with suitable bandgaps may not be sufficient to catalyze both reactions on a single $H_2O$-splitting photoelectrocatalyst. This further emphasizes the necessity of co-catalysts, since the photoabsorbers themselves cannot bind the intermediates with energetics appropriate to facilitate OER or HER at a reasonable rate. Combining co-catalytic materials like $RuO_2$,²⁶,²⁷ Pt,²⁷,²⁸ and cobalt-phosphate²⁹ found in many experimental studies of photoelectrocatalytic $H_2O$ splitting should improve the energetics of OER and HER intermediate adsorption, allowing for higher turnover of oxygen. Furthermore, our results show that an inter-sectional approach that considers the bulk solid-state properties, the surface chemistry, and their interface is absolutely necessary to a theory-guided search for viable photoelectrocatalysts, if high-throughput screening is to yield a successful technology for solar fuel production in the future.

## Acknowledgements

The authors acknowledge support from the Center of Nanostructuring for Efficient Energy Conversion (CNEEC) at Stanford University, an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Basic Energy Sciences under award number DE-SC0001060. Support from the U.S. Department of Energy Office of Basic Energy Science to the SUNCAT Center for Interface Science and Catalysis is gratefully acknowledged. J.H.M. acknowledges support from the NSF GRFP, grant number DGE-114747.

## Notes and references

1 I. E. Castelli, T. Olsen, S. Datta, D. D. Landis, S. Dahl, K. S. Thygesen and K. W. Jacobsen, *Energy Environ. Sci.*, 2012, **5**, 5814-5819.

2 Y. Wu, P. Lazic, G. Hautier, K. Persson and G. Ceder, *Energy Environ. Sci.*, 2013, **6**, 157-168.

3 I. C. Man, H.-Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov and J. Rossmeisl, *ChemCatChem*, 2011, **3**, 1159-1165.

4 J. Greeley, T. F. Jaramillo, J. Bonde, I. Chorkendorff and J. K. Nørskov, *Nat. Mater.*, 2006, **5**, 909-913.

5 B. Hinnemann, P. G. Moses, J. Bonde, K. P. Jørgensen, J. H. Nielsen, S. Horch, I. Chorkendorff and J. K. Nørskov, *J. Am. Chem. Soc.*, 2005, **127**, 5308-5309.

6 M. Koper, *J. Electroanal. Chem.*, 2011, **660**, 254-260.

7 L. C. Seitz, Z. Chen, A. J. Forman, B. A. Pinaud, J. D. Benck and T. F. Jaramillo, *ChemSusChem*, 2014, **7**, 1372-1385.

8 B. A. Pinaud, J. D. Benck, L. C. Seitz, A. J. Forman, Z. Chen, T. G. Deutsch, B. D. James, K. N. Baum, G. N. Baum, S. Ardo, H. Wang, E. Miller and T. F. Jaramillo, *Energy Environ. Sci.*, 2013, **6**, 1983-2002.

9 M. G. Walter, E. L. Warren, J. R. McKone, S. W. Boettcher, Q. Mi, E. A. Santori and N. S. Lewis, *Chem. Rev.*, 2010, **110**, 6446-6473.

10 P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari and R. M. Wentzcovitch, *J. Phys.: Condens. Matter*, 2009, **21**, 395502.

11 M. A. Peña and J. L. G. Fierro, *Chem. Rev.*, 2001, **101**, 1981-2018.

12 M. Johnsson and P. Lemmens, in *Handbook of Magnetism and Advanced Magnetic Materials*, ed. H. Kronmüller and S. Parkin, John Wiley & Sons Ltd, Chichester, 2007, vol. 4, pp. 2098-2106.

13 M. Johnsson and P. Lemmens, *J. Phys.: Condens. Matter*, 2008, **20**, 264001.

14 H. J. Monkhorst and J. D. Pack, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1976, **13**, 5188.

15 B. Hammer, L. B. Hansen and J. K. Nørskov, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1999, **59**, 7413.

16 P. Liao, J. A. Keith and E. A. Carter, *J. Am. Chem. Soc.*, 2012, **134**, 13296-13309.

17 M. Bajdich, M. García-Mota, A. Vojvodic, J. K. Nørskov and A. T. Bell, *J. Am. Chem. Soc.*, 2013, **135**, 13521-13530.

18 M. García-Mota, A. Vojvodic, F. Abild-Pedersen and J. K. Nørskov, *J. Phys. Chem. C*, 2013, **117**, 460-465.

19 A. Navrotsky, *Perovskite: A structure of great interest to geophysics and materials science*, 1989, pp. 67-80.

20 J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard and H. Jónsson, *J. Phys. Chem. B*, 2004, **108**, 17886-17892.

21 A. A. Peterson, F. Abild-Pedersen, F. Studt, J. Rossmeisl and J. K. Norskov, *Energy Environ. Sci.*, 2010, **3**, 1311-1315.

22 V. Tripković, E. Skúlason, S. Siahrostami, J. K. Nørskov and J. Rossmeisl, *Electrochim. Acta*, 2010, **55**, 7975-7981.

23 H. A. Hansen, J. Rossmeisl and J. K. Nørskov, *Phys. Chem. Chem. Phys.*, 2008, **10**, 3722-3730.

24 M. Butler and D. Ginley, *J. Electrochem. Soc.*, 1978, **125**, 228-232.

25 A. Kasahara, K. Nukumizu, G. Hitoki, T. Takata, J. N. Kondo, M. Hara, H. Kobayashi and K. Domen, *J. Phys. Chem. A*, 2002, **106**, 6750-6753.

26 J. Sato, N. Saito, Y. Yamada, K. Maeda, T. Takata, J. N. Kondo, M. Hara, H. Kobayashi, K. Domen and Y. Inoue, *J. Am. Chem. Soc.*, 2005, **127**, 4150-4151.

27 K. Maeda, T. Takata, M. Hara, N. Saito, Y. Inoue, H. Kobayashi and K. Domen, *J. Am. Chem. Soc.*, 2005, **127**, 8286-8287.

28 M. Higashi, R. Abe, T. Takata and K. Domen, *Chem. Mater.*, 2009, **21**, 1543-1549.

29 S. Y. Reece, J. A. Hamel, K. Sung, T. D. Jarvi, A. J. Esswein, J. J. H. Pijpers and D. G. Nocera, *Science*, 2011, **334**, 645-648.