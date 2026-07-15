# Understanding and Controlling the Work Function of Perovskite Oxides Using Density Functional Theory

Ryan Jacobs, John Booske, and Dane Morgan*

Perovskite oxides containing transition metals are promising materials in a wide range of electronic and electrochemical applications. However, neither their work function values nor an understanding of their work function physics have been established. Here, the work function trends of a series of perovskite ($ABO_3$ formula) materials using density functional theory are predicted, and show that the work functions of (001)-terminated AO- and $BO_2$-oriented surfaces can be described using concepts of electronic band filling, bond hybridization, and surface dipoles. The calculated range of AO ($BO_2$) work functions are 1.60–3.57 eV (2.99–6.87 eV). An approximately linear correlation ($R^2$ between 0.77 and 0.86 is found, depending on surface termination) between work function and position of the oxygen 2p band center, which correlation enables both understanding and rapid prediction of work function trends. Furthermore, $SrVO_3$ is identified as a stable, low work function, highly conductive material. Undoped (Ba-doped) $SrVO_3$ has an intrinsically low AO-terminated work function of 1.86 eV (1.07 eV). These properties make $SrVO_3$ a promising candidate material for a new electron emission cathode for application in high power microwave devices, and as a potential electron emissive material for thermionic energy conversion technologies.

## 1. Introduction
Research into the basic science and applications of perovskite oxides is extremely active and very relevant for a number of technological applications. These applications include at least oxide electronics, $^{[1–3]}$ catalysis and solid oxide fuel cells, $^{[4–7]}$ transistor dielectrics, $^{[8,9]}$ field emission coatings, $^{[10–13]}$ magnetic tunnel junctions, $^{[14,15]}$ and solid state memory. $^{[16,17]}$ Perovskite materials are relevant to a wide variety of applications in part due to their stable incorporation of $\approx$90% of the elements in the periodic table. This high degree of compositional flexibility allows for tunable properties to fit the needs of many possible applications, including the tuning of the work function. The perovskite bulk and surface structures used in this work are shown in Figure 1, as well as described in the Computational Methods (Section 6) and Section 1 of the Supporting Information. We note that we use ideal (001) surfaces without defects or atomic position reconstructions, and we discuss the impacts of this approximation in our discussion of errors between experiment and simulation in Section 3.1 of the main paper and also in Section 3 of the Supporting Information.

Knowledge of a material's work function provides an absolute electron energy-level reference relative to the vacuum energy, which is important for device applications where the discontinuities of energy levels between different materials have a large effect on the device properties and performance. Absolute electron levels often play a critical role for devices with heterostructured interfaces or active surfaces, such as solar cells, oxide electronics, electrocatalysts, and applications utilizing thermionic electron or field emission physics such as Schottky junctions, thermionic energy converters, and vacuum cathodes for high power microwave sources. Accurate work function values and an understanding of their origins and trends are critical for materials development and optimization for these classes of technologies.

In this work, we provide a database and trends in work function with respect to composition changes of the A- and B-site cations of a representative set of $ABO_3$ perovskite materials, many of which may have practical value for the above applications in either pure or doped forms. Furthermore, we provide fundamental understanding of these work function trends by relating them to an electronic structure descriptor and known trends in transition metal chemistry. We use the HSE functional of Heyd, Scuseria, and Ernzerhof $^{[18]}$ within density functional theory (DFT) with Hartree–Fock exchange fractions obtained from refs. [19,20], which fit the exchange fractions specifically to yield correct bulk electronic properties for these materials. Use of these fitted Hartree–Fock exchange fractions ensures that the band levels and work functions are the most quantitative calculated values reported to date.

We also apply the methods and understanding gained in this work to discover a low work function perovskite material, $SrVO_3$, for efficient electron emission into vacuum (thermionic, field, or photoemission). The main electron emission applications considered here are high power electron beam applications (such as high power microwave or millimeter-wave source technologies) and thermionic energy conversion devices. A low

Dr. R. Jacobs, Prof. D. Morgan
Department of Materials Science and Engineering
University of Wisconsin-Madison
Madison, WI 53706, USA
E-mail: ddmorgan@wisc.edu
Prof. J. Booske
Department of Electrical and Computer Engineering
University of Wisconsin-Madison
Madison, WI 53706, USA

![](./images/811270270688952321_1.jpg)

DOI: 10.1002/adfm.201600243

---

Adv. Funct. Mater. 2016,
DOI: 10.1002/adfm.201600243

© 2016 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
wileyonlinelibrary.com 1

![](./images/811270270688952321_2.jpg)

![](./images/811270270688952321_3.jpg)

![](./images/811270270688952321_4.jpg)

![](./images/811270270688952321_5.jpg)

![](./images/811270270688952321_6.jpg)

Figure 1. Crystal structures for A) ideal cubic perovskite and B) pseudocubic perovskite phases. In both A) and B) the green (largest, corner atoms) are the A site cations, the blue/purple atoms at the center of the octahedra are the B site cations, and the red (octahedral corner) atoms are O. These structures depict high temperature pseudocubic phases that were derived from experimental A) Pm$\overline{3}$m (cubic) and B) Pbnm (orthorhombic) and R$\overline{3}$c (rhombohedral) symmetries. Structure models of $ABO_3$ surface slabs are C): asymmetric, stoichiometric, D): symmetric and AO terminated, nonstoichiometric, and E) symmetric and $BO_2$ terminated, nonstoichiometric.

work function is important for electron emitters as the most facile electron removal will result in high emitted electron current densities at lower temperatures, electric fields, or light intensity in the context of thermionic, field, or photoemission, respectively. In the rest of this paper, we specifically discuss and compare perovskite emission property predictions with conventional thermionic emitters, but the advantages are understood to apply more generally to all forms of electron emission.

Historically, thermionic electron emitters have been composed of a refractory metal such as W coated with an oxide or diffusing oxide species that lowers the work function via electrostatic surface dipoles. The coating is necessary because the refractory metals tend to have high work functions (on the order of 4.5 eV), and are therefore poor electron emitters unless a coating is included to lower their work function. Examples of thermionic emitters include impregnated W cathodes that have a low work function due to the formation of Ba-O dipoles$^{[21]}$ and scandate cathodes where the complex interplay between dipole formation and electron doping of Ba-O on $Sc_2O_3$ also creates a low work function.$^{[21-23]}$ These types of thermionic emitters are currently employed in many high power electron beam applications.$^{[24,25]}$ Even thermionic energy conversion emitting layers rely on the same type of volatile surface dipole layers, such as Cs-O adsorbed on GaAs or InGaAs.$^{[26,27]}$ Replacing these current emission materials which contain volatile surface species with a new material with an intrinsically low work function would simplify the architecture and increase the lifetime of electronic devices which use thermionic electron emission processes. In this work we propose that $SrVO_3$, due to its intrinsic stability, high conductivity, and low work function, is a very promising material for next generation thermionic electron emitters.

There has been some experimental and computational work related to measuring the work functions of some perovskite materials. These studies include Kelvin probe microscopy of $LaAlO_3^{[2]}$ and $A_{1-x}B_xMnO_3$ (A = La, Pr, Nd, B = Sr, Ca, Pb),$^{[28]}$ UPS measurements of Nb-doped $SrTiO_3$,$^{[29]}$ a combination of photoemission and redox potential measurements of $LaMnO_3$,$^{[30,31]}$ and X-ray absorption and emission measurements on a series of transition metal-containing $LaBO_3$ (B = Cr, Mn, Fe, Co, Ni) perovskites.$^{[32]}$ DFT work function calculations of $BaTiO_3$,$^{[33]}$ $SrTiO_3$,$^{[16]}$ and $La_{2/3}Sr_{1/3}MnO_3^{[34]}$ have been performed by other research groups. However, none of these studies provide enough data to establish the physics and trends governing true surface work functions. Summary tables of these experimental and calculated work functions from other research groups are provided in Section 3 of the Supporting Information along with a discussion of their comparison to our values. Generally, our calculated results agree with previous experimental and calculated values to the extent that comparison is possible.

## 2. Results: $ABO_3$ Work Function Data and Trends

### 2.1. $ABO_3$-Calculated Work Functions

Figure 2 is a plot of the calculated work functions for the AO- and $BO_2$-surface terminations versus composition of the B-site for all 20 materials considered in this work. These materials were chosen because their pure or slightly defected (doped

![](./images/811270270688952321_7.jpg)

Figure 2. Trend of (001) AO- and BO₂-terminated surface work func- tions for the 20 perovskite materials studied in this work as a function of B-site element across the periodic table. The solid (open) symbols connected with a solid (dashed) line are the BO₂ (AO) work functions, respectively. Red, blue, purple, black, green, orange and pink symbols signify the LaBO₃ series, SrBO₃ series, La₁₋ₓSrₓMnO₃, x = 0.0625, 0.125, 0.25, 0.375 (LSM), LaAlO₃, Ba₀.₅Sr₀.₅Co₀.₇₅Fe₀.₂₅O₃ (BSCF), LaRuO₃, and SrRuO₃ materials, respectively. Note that the data points of BO₂ LaFeO₃ and SrRuO₃ work functions lie on top of each other.

and/or off-stoichiometric variants have already been the sub- ject of intense research in the areas of oxide electronics, $^{[1-3]}$ catalysis and solid oxide fuel cells, $^{[4-7]}$ transistor dielectrics, $^{[8,9]}$ field emission coatings, $^{[10-13]}$ magnetic tunnel junctions, $^{[14,15]}$ and solid state memory. $^{[16,17]}$ Furthermore, these materials can exhibit the stable incorporation of many transition metals, resulting in a range of physical properties (e.g., from heavily insulating to metallic electronic conductivity), making them an ideal set of materials in which to study compositional trends in the work function. Looking from left to right, Figure 2 shows how the AO and BO₂ work functions for perovskite materials change as B-site cations move across the $3d$ series of the peri- odic table from Sc through Ni. Table 1 contains the calculated work functions for the AO- and BO₂-terminated (001) surfaces for all $ABO_{3}$ materials considered in this study. The O-bond ionicities are also provided, where the ionicity is defined by the ratio of the computed atomic charge on oxygen to the value of -2 expected for a perfectly ionic system (for example, an O atomic charge of -1.5 yields a bond ionicity of $-1.5/-2 = 0.75$, and a perfectly ionic system would yields a bond ionicity of $-2/-2 = 1$). The atomic charges were calculated using Bader charge analysis of atomic charges of bulk $ABO_{3}$ mate rials. $^{[35,36]}$ Finally, we have also included in Table 1 ranges of experimentally measured work functions for select materials. Generally, chemical bonding has mixed covalent and ionic character, therefore the calculated atomic charges on oxygen from the Bader analysis will be less than (i.e., more positive than) -2. The O-bond ionicities in Table 1 will be referenced in upcoming qualitative discussions of work function trends for these materials in Section 3.1. For the $LaBO_{3}$ series, the LaO work functions range from 1.60 eV (LaRuO₃) to 3.57 eV (LaScO₃) while the BO₂ work functions range from 2.99 eV (LaTiO₃) to 6.87 eV (LaAlO₃), and tend to increase in magni- tude for Ti through Ni. For the $SrBO_{3}$ series, the SrO work functions range from roughly 1.86 eV (SrVO₃) to 3.42 eV (SrCoO₃) while the BO₂ work functions range from 5.09 eV (SrVO₃) to 6.68 eV (SrFeO₃).

Table 1. Summary of HSE calculated work functions for all (001) sur- faces of $ABO_{3}$ materials considered in this study. Also listed are the ionicities (see text for definition) of the O-bonds for each material, which were calculated from Bader charge analysis of the bulk materials. A decrease in bonding ionicity is indicative of greater hybridization of the B $3d$ bands and O $2p$ bands. The range of reported experimental work functions for select materials is also provided. Additional discussion comparing calculated and experimental work functions is available in the Supporting Information.

| Material                  | AO WF [eV] | BO₂ WF [eV] | O bond ionicity | Experimental WF range [eV]ª |
|---------------------------|------------|-------------|-----------------|------------------------------|
| LaScO₃                    | 3.57       | 6.32        | 0.716           | –                            |
| LaTiO₃                    | 2.59       | 2.99        | 0.684           | –                            |
| LaVO₃                     | 2.97       | 3.60        | 0.664           | –                            |
| LaCrO₃                    | 2.77       | 5.27        | 0.665           | $4.3^{[32]}$                  |
| LaMnO₃                    | 1.76       | 5.21        | 0.653           | $4.5-5.1^{[30-32]}$           |
| LaFeO₃                    | 1.98       | 5.14        | 0.637           | $4.6^{[32]}$                  |
| LaCoO₃                    | 2.42       | 5.73        | 0.599           | $5.0^{[32]}$                  |
| LaNiO₃                    | 2.47       | 6.06        | 0.559           | $5.5^{[32]}$                  |
| LaAlO₃                    | 3.25       | 6.87        | 0.879           | $2.2-4.2^{[2]}$               |
| LaRuO₃                    | 1.60       | 4.78        | 0.597           | –                            |
| SrTiO₃                    | 3.18       | 6.33        | 0.655           | $2.6-4.9^{[37,38]}$           |
| SrVO₃                     | 1.86       | 5.09        | 0.601           | –                            |
| SrFeO₃                    | 3.24       | 6.68        | 0.556           | –                            |
| SrCoO₃                    | 3.42       | 6.51        | 0.537           | –                            |
| SrRuO₃                    | 2.55       | 5.16        | 0.614           | –                            |
| Ba₀.₅Sr₀.₅Co₀.₇₅Fe₀.₂₅O₃   | 2.94       | 6.35        | 0.540           | –                            |
| La₀.₉₃₇₅Sr₀.₀₆₂₅MnO₃       | 2.11       | 5.28        | 0.650           | –                            |
| La₀.₈₇₅Sr₀.₁₂₅MnO₃         | 2.23       | 5.49        | 0.647           | –                            |
| La₀.₇₅Sr₀.₂₅MnO₃           | 1.87       | 6.02        | 0.643           | $5.7^{[39]}$                  |
| La₀.₆₂₅Sr₀.₃₇₅MnO₃         | 2.39       | 5.85        | 0.637           | $4.7-4.9^{[38,39]}$           |

a)The experimental work function values reported here were measured using a variety of techniques on different sample types (e.g., thin film, polycrystalline com- pacts), which can render one-to-one comparisons between calculated and experi- mental work functions difficult. A detailed discussion comparing experimental and calculated work functions and possible reasons for discrepancy is presented in the Supporting Information.

Doping Sr into LaMnO₃ to produce LSM resulted in an increase of the AO and BO₂ work functions for all Sr concen- trations relative to undoped LaMnO₃. When replacing $La^{3+}$ with $Sr^{2+}$, the system becomes more oxidized, i.e., it becomes hole doped. This is evident from the work function data for the LSM series, where increasing the A-site Sr content tends to increase the work function of both surfaces and decrease the ionicity of the O-bonding. The fact that all BO₂ and most AO SrBO₃ material work functions are higher than their cor- responding LaBO₃ work functions (with the exception of AO- terminated SrVO₃) is consistent with the intuition that doping Sr in place of La should raise the work function of the perovs- kite. We note that the increase in the work function of (La,Sr) MnO₃ is not monotonic with increasing Sr content. This lack of monotonic behavior is most likely a result of the specific Sr ordering chosen, and more work is needed to better understand work function variations in the disordered solid solution struc- ture of La and Sr in LSM. Interestingly, BSCF has a lower work

function than both $SrFeO_{3}$ and $SrCoO_{3}$, suggesting that doping Ba in place of Sr results in a lowering of the work function for Sr-based perovskites. The effect of Ba doping on the $SrVO_{3}$ work functions will be examined further in Section 4. The AO terminations of $SrVO_{3}, LaMnO_{3}$ , and $LaRuO_{3}$ have the lowest calculated work functions of 1.86 and 1.76, and 1.60 eV, respec tively. By virtue of these low work functions, $SrVO_{3}, LaMnO_{3}$ , and $LaRuO_{3}$ may be suitable candidates for low-work function, electron-emission cathode materials. Of these candidate mate- rials, $SrVO_{3}$ is a particularly promising material to explore for the emission applications discussed in the introduction section by virtue of its low work function, metallic conductivity, ability to be synthesized as both a bulk powder $^{[40,41]}$ and (001)-oriented thin film, $^{[42]}$ and structural stability at high temperatures. $^{[40,41,43]}$  We therefore study $SrVO_{3}$ in more detail in Section 4.

### 2.2. 2p-Band Center As an Electronic Structure Descriptor
Having demonstrated qualitative work function trends with changing A- and B-site composition for the $ABO_{3}$ materials investigated here, we turned our focus to developing a greater understanding of the physics governing the value of the work function in these perovskite materials. To accomplish this, we used the O 2p-band center (see Section 2 of the Supporting Information for details) as an electronic structure descriptor, as this variable has proved useful for correlating with a number of perovskite properties. $^{[6,44-46]}$ The B-site cation 3 d-band center and the La/Sr A-site band centers (both calculated with respect to $E_{Fermi}$ ) were also investigated as possible descriptors. How ever, no useful physical trends emerged from their analysis. Therefore, we focused on the bulk O 2p-band center.

![](./images/811270270688952321_8.jpg)

Figure 3. Plots of calculated work functions for the A) $BO_{2}$ and B) AO terminated surfaces of $ABO_{3}$ materials as a function of the O 2 p-band center of bulk $ABO_{3}$ materials. In both plots, the blue symbols represent insulating perovskites while the red symbols represent metallic perovs- kites. In A) and B) there is a semiquantitative linear relationship between the work function and the O 2p-band center.

Figure 3 demonstrates the relationship between the calcu- lated (001) work functions and the value of the bulk O 2p-band center. Figure 3A,B is a plot of $BO_{2}$ work function (AO work function) as a function of the O 2p-band center energy. In both plots, the blue symbols refer to insulating perovskites while red symbols refer to metallic perovskites. In the present case, "insu- lating" refers to any material we calculated to have a finite bulk and surface band gap, whether due to band-insulating or Mott- Hubbard insulating behavior. The materials which compose the set of insulating perovskites are: $LaScO_{3}, LaTiO_{3}, LaVO_{3}$ , $LaCrO_{3}, SrTiO_{3}$ , and $LaAlO_{3}$ . The remaining perovskite mate rials are referred to as "metallic" perovskites. Although the bulk ground states of some of these materials, for example, $LaMnO_{3}$ and $LaFeO_{3}$ , are also insulating, the ferromagnetic near-surface electronic structure is metallic. $^{[47]}$ Our inclusion of these mate rials in the category of "metallic" perovskites is appropriate as these materials demonstrate fundamentally different electronic structure behavior from prototypical Mott-Hubbard insulators such as $LaTiO_{3}$ and $LaVO_{3}$ near their surfaces. The influence of band positions and the O 2p-band center relationship of Figure 3 are discussed in Section 3.1.

## 3. Discussion: $ABO_{3}$ Work Function Data and Trends
### 3.1. $ABO_{3}$ Work Function Trends
Perhaps the most striking feature of the calculated work func- tions in Figure 2 is that the AO surfaces generally have dra- matically lower work function values than $BO_{2}$ surfaces in all cases. Qualitatively, this can be understood in terms of the sur- face dipoles. The alternating layers of the (001) orientation are $AO / BO_{2} / AO / BO_{2}$ , which, when considering formal charges for $A^{3+} B^{3+} O_{3}^{6-}$ compounds, alternates +/-/+/-. A positive surface dipole is a dipole with an outwardly pointing positive charge, while a negative surface dipole has an outwardly pointing nega- tive charge. Thus we see that the AO termination forms a posi- tive surface dipole that decreases the work function, and the BO, surface forms a negative surface dipole that increases the work function. It is evident that the same trend of high $BO_{2}$ work functions and low AO work functions also occurs for the $SrBO_{3}$ (and BSCF) materials. Considering formal charges for these $A^{2+} B^{4+} O_{3}^{6-}$ compounds, one should expect no difference in surface dipole as the $A^{2+} O^{2-}$ and $B^{4+} O_{2}^{2-}$ surfaces both sum to zero charge. However, a number of previous studies have shown that surfaces of $A^{2+} B^{4+} O_{3}^{6-}$ compounds are in fact polar due to enrichment or deficiency of electrons relative to theirformal valence. $^{[47,48]}$ 

The trend of increasing $BO_{2}$ work function when proceeding from left to right on the periodic table along the 3d row as

shown in Figure 2 can be understood in terms of the transition metal electronegativities. When proceeding from Ti to Ni, the electronegativity of the transition metal ion is increasing as the $3d$ band fills. As a result, when proceeding from Ti to Ni, the $3d$ bands fill with more electrons, the $3d$ bands shift lower in energy, and the work function increases. For the materials $LaScO_3$, $LaAlO_3$, and $SrTiO_3$, the $3d$ bands are nearly empty and these materials behave as band insulators. Interestingly, these band insulator materials have nearly the same $BO_2$ and AO work function values within a few tenths of an eV. For the case of these band insulators, the absence of $3d$ electrons means the Fermi level resides at the top of the O $2p$ band. Thus, for materials with no $3d$ electrons, it is the O $2p$ band which sets the value of the work function.

From Table 1, it is evident that as the $3d$ bands fill, the bonding ionicity decreases, which implies that the B $3d$ and O $2p$ bands are becoming more hybridized. In addition, for the $SrBO_3$ materials where the B element is in the 4+ oxidation state, the bond ionicities are lower and thus the B $3d$ and O $2p$ bands are more hybridized than the corresponding $LaBO_3$ systems where the B element is in the 3+ oxidation state. These trends of B $3d$-O $2p$ band hybridization are consistent with a joint experimental and computational work by Santivich and co-workers that showed how B $3d$-O $2p$ band hybridization changes as a function of $3d$ band filling using O K-edge X-ray absorption and DFT calculations on a series of perovskite and Ruddlesden-Popper materials. $^{[49]}$ The increased B $3d$-O $2p$ band hybridization means that there is greater overlap of the B $3d$ and O $2p$ bands, and the O $2p$ band center becomes closer to $E_{Fermi}$. The above trends in hybridization with $3d$ band filling illustrate that materials with higher $3d$ band filling will have increased band hybridization. This increased band hybridization will result in O $2p$ bands that are closer to $E_{Fermi}$, which will result in higher $BO_2$ work functions. Based on this discussion, if one were interested in creating a perovskite with a higher work function, one strategy would be to increase the band hybridization by doping the A-site with alkaline earths to further oxidize the B-site, for example Sr doping in $LaMnO_3$ to create LSM or Sr and Ba doping in $La(Co, Fe)O_3$ to create BSCF.

Both plots in Figure 3 show a linear trend of the calculated work function versus the bulk O $2p$-band center, although the trend is more consistently linear (e.g., it has a higher $R^2$ value) in the case of $BO_2$ work functions. In general, these results demonstrate that the bulk O $2p$-band center provides an approximate predictor of the work function. Interestingly, in Figure 3A, the slopes of the $BO_2$ work function versus O $2p$-band center are ≈0.7 and 1, which is generally close to one, while in Figure 3B the slopes of the AO work functions are ≈0.2 and 0.6. Since the work function is controlled by a combination of the energy band positions and the magnitude of the surface dipole, the slope of $BO_2$ work function versus O $2p$-band center being nearly equal to one implies that the $BO_2$ work function changes are dominated by the band positions and are thus relatively insensitive to the magnitude of the surface dipole. In the case of the AO work functions, where the work function does not change as rapidly in proportion to the movement of the O $2p$-band center, we conclude that the AO work functions are dominated by surface dipoles and are relatively insensitive to the band positions.

Unfortunately, direct comparison with experimental values is difficult as there are no experiments that measure the work function of a specific perovskite surface termination, as we are calculating here. However, because DFT has been shown to accurately reproduce work functions of metal surfaces $^{[21]}$ and the ability of HSE to accurately reproduce the electronic structure of these materials, $^{[19,20]}$ it is reasonable to expect that the calculated work functions are within a few tenths of an eV of the true work function for the surface being modeled. Some additional errors are introduced due to the use of idealized surfaces without defects or reconstructions, but we expect those effects to also be within a couple of tenths of an eV for most surfaces, as discussed in Section 3 of the Supporting Information. Encouragingly, our calculated work function values follow the same compositional trend as the surface averaged work function values for $La(Cr, Mn, Fe, Co, Ni)O_3$ materials obtained with X-ray absorption and emission spectroscopy. $^{[32]}$ Additional discussion regarding causes of quantitative differences between experimental and calculated work functions is provided in Section 3 of the Supporting Information.

### 3.2. Density of States Pictures of Work Function Trends

As discussed in Section 3.1, the band positions are the dominant contribution setting the value of the $BO_2$ work functions. Here, we illustrate the connection between the band structure and work function using schematic density of states diagrams. Figure 4 is a density of states schematic that illustrates the trend of $BO_2$ work functions from Figure 2 by comparing the density of states of an insulating material with an empty $3d$ band and high ionicity (small amount of B $3d$-O $2p$ hybridization) such as $LaScO_3$ (Figure 4A), a less ionic material (large amount of B $3d$-O $2p$ hybridization) with half or mostly filled $3d$ band such as $LaNiO_3$ (Figure 4B) and a metallic, medium ionicity material (medium amount of B $3d$-O $2p$ hybridization) with a minimally occupied $3d$ band such as $SrVO_3$ (Figure 4C). The vacuum level, Fermi level and O $2p$-band center are denoted as $E_{vac}$, $E_{Fermi}$, and $\bar{O}_{2p}(E)$, respectively. Following the convention of DFT calculations, the position of $E_{Fermi}$ is at the energy of the highest filled electronic state. The O $2p$ states are shown in red and the B $3d$ states are shown in blue. The states that are shaded are filled states. In Figure 4, we made the simplifying approximation that for a fixed surface dipole the O $2p$ bands remain at a fixed energy level relative to vacuum. Maintaining a constant level of the O $2p$ band provides us with a straightforward and intuitive way to demonstrate how the work function varies with the band positions and associated properties such as bond ionicity/hybridization and also how the value of the O $2p$-band center ($x$-axis in Figure 3) physically relates to our calculated work function values. While our calculated results are most consistent with a fixed position for the O $2p$-band center relative to vacuum under a fixed surface dipole, it is difficult to prove that this rigorously occurs, and some movement of O $2p$-band center relative to vacuum is certainly possible between materials. We note that results of X-ray absorption and emission measurements of $La(Cr, Mn, Fe, Co, Ni)O_3$ polycrystalline samples show that the occupied O $2p$ states may move relative to the vacuum level by approximately $\pm 1$ eV for varying B-site composition. $^{[32]}$ When

![](./images/811270270688952321_9.jpg)

$$\Phi_1 \text{ (e.g. } \mathrm{LaScO_3}) > \Phi_2 \text{ (e.g. } \mathrm{LaNiO_3}) > \Phi_3 \text{ (e.g. } \mathrm{SrVO_3})$$

$$\Delta_1 \text{ (e.g. } \mathrm{LaScO_3}) < \Delta_2 \text{ (e.g. } \mathrm{LaNiO_3}) < \Delta_3 \text{ (e.g. } \mathrm{SrVO_3})$$

Figure 4. Schematic density of states plots for A) insulating perovskite with empty 3d band such as $\mathrm{LaScO_3}$, B) perovskite with partially or mostly filled 3d band such as $\mathrm{LaNiO_3}$, and C) metallic perovskite with minimally filled 3d band such as $\mathrm{SrVO_3}$. The red regions denote O 2p states while the blue regions denote B 3d states. Shaded regions indicate filled states while unshaded regions denote empty states. The labels and symbols are defined in the main text. The case in plot C) of a material with minimally filled 3d band results in an O 2p-band center furthest below $E_{\text{Fermi}}$ and a low work function. The $\Delta$ values are defined as the difference between the O 2p-band center and $E_{\text{Fermi}}$, equivalent to the x-axis of Figure 3.

we averaged our calculated bulk O 2p-band centers relative to the vacuum level for the $\mathrm{BO_2}$- and AO-terminated surfaces we found the standard deviation of O 2p-band center was 0.4 and 1 eV, respectively, which is qualitatively consistent with the spectroscopy results of ref. [32]. However, these measured and calculated changes mix both movement of the O 2p-band center and changes in the surface dipoles, and we believe that for fixed dipoles the O 2p-band center position relative to vacuum may be quite stable. The $\Delta$ values indicate the energy difference between the O 2p-band center and $E_{\text{Fermi}}$, equivalent to the x-axis of Figure 3. In Figure 4A, the insulating perovskite with empty 3d band has very deep O 2p bands, which results in a deep $E_{\text{Fermi}}$ (relative to the vacuum level), an O 2p-band center close to $E_{\text{Fermi}}$ and high work function. Because we use the DFT convention with $E_{\text{Fermi}}$ located at the valence band maximum, the diagram in Figure 4A shows the p-type limit of the work function (i.e., ionization potential) for an insulating perovskite. In Figure 4B, the perovskite with partially filled 3d band has a large amount of band hybridization (i.e., lower ionicity), which results in higher occupied electron energy states, an O 2p-band center further from $E_{\text{Fermi}}$ compared to Figure 4A, and a slightly lower work function. In Figure 4C, the metallic perovskite with minimally filled 3d band has less band hybridization than the case in Figure 4B, which results in an occupied portion of the B 3d band that is more empty, less hybridized and is higher in energy. Since the occupied portion of the B 3d band is higher in energy, $E_{\text{Fermi}}$ is also higher. Overall, this leads to an O 2p-band center that is further from $E_{\text{Fermi}}$ and a lower work function.

The insensitivity of the $\mathrm{BO_2}$ work functions to surface dipoles can be understood qualitatively by considering the origin and path of emitted electrons. These densities of states in Figure 4 show that for materials containing 3d electrons the states at $E_{\text{Fermi}}$ are dominated by hybridized B 3d and O 2p states. Therefore, we can think of the emitted electrons as emerging from the $\mathrm{BO_2}$ layers. Thus, the electrons being emitted from the $\mathrm{BO_2}$ surface are already at the surface and can be directly emitted into vacuum. Recall that, in contrast to the $\mathrm{BO_2}$ work function, the AO work functions are dominated by large surface dipoles. Emission from the AO surface involves electrons moving from the subsurface $\mathrm{BO_2}$ layer through the AO layer and being emitted. This difference in pathway makes the $\mathrm{BO_2}$ surface work function largely insensitive to the surface dipole but the AO surface work function very sensitive to the surface dipole. This explanation of a surface-emitting electron experiencing a large, work function-lowering surface dipole via the AO surface is shown in Figure 5.

From the above discussions, we can summarize our understanding of the trend in O 2p band with the work function as follows: The location of the O 2p band relative to $E_{\text{Fermi}}$ is highly dependent on the number of 3d electrons in the system and the hybridization between the B 3d levels and O 2p levels.

When proceeding from Ti through Ni, more 3d electrons are added to the system, the bond hybridization increases, the 3d bands fill and move lower in energy, and thus $E_{\text{Fermi}}$ is lower in energy and closer to the O 2p-band center. Because $E_{\text{Fermi}}$ is lower in energy, the work function of $\mathrm{BO_2}$ surfaces increases as more 3d electrons are added. Furthermore, for the same B-site transition metal element, if the B-site is more oxidized (e.g., comparing $\mathrm{Co^{3+}}$ in $\mathrm{LaCoO_3}$ with $\mathrm{Co^{4+}}$ in $\mathrm{SrCoO_3}$), the material containing the more oxidized transition metal will exhibit greater hybridization between the B 3d and O 2p bands, thus resulting in higher work functions. From Table 1 and Figure 2, one can see that all $\mathrm{SrBO_3}$ materials have higher work functions than their analogous $\mathrm{LaBO_3}$ materials, except for AO-terminated $\mathrm{SrVO_3}$. These hybridization trends with 3d electron filling are consistent with experimental and computational findings of Suntivich and co-workers.[49] Broadly, the band structure progression shown in Figure 4 is a close representation of how the $\mathrm{BO_2}$ work function changes with composition and 3d band filling. In the case of the AO work function, the portion of the work function due to surface dipoles is strong enough such that it overwhelms the band physics contributions of Figure 4. This yields a weaker relationship between work function and O 2p-band center (slope significantly less than one, see Figure 3B).

## 4. Results and Discussion: $\mathrm{SrVO_3}$ As a Low Work Function, Metallic Perovskite

Our earlier analysis in Section 2.1 has demonstrated that of the 18 perovskite materials considered here, $\mathrm{SrVO_3}$ is one of the

![](./images/811270270688952321_10.jpg)

Figure 5. Schematic demonstrating why the $BO_2$ work functions are insensitive to surface dipoles, and the AO work functions are dominated by surface dipoles. A) Density of states representative of a transition metal perovskite with partially occupied $3d$ band. The colors and labels are the same as Figure 4. The Fermi level is dominated by B $3d$ states for both the AO- and $BO_2$-terminated surfaces. Electrons emitting from the surfaces of these materials will originate at the Fermi level, which are predominantly from the $BO_2$ layers. In B), the emission of surface electrons from the $BO_2$ surface originates from the terminating surface layer. The $BO_2$ work function is dominated by the band positions relative to vacuum, and relatively insensitive to the surface dipoles. In C), the emis- sion of a surface electron again originates from the $BO_2$ layer, which is now present in the subsurface layer. The terminating surface layer is now an AO-plane, which does not appreciably contribute to the density of states near the Fermi level. Here, the AO surface acts as a large dipole layer, lowering the AO work function. In this way, the work function of the AO surface is dominated by surface dipoles, and is relatively insensitive to the band positions.

most promising materials for electron emitting applications, in particular for high power electron beam devices used in defense, scientific research and communications, and as an electron-emitting layer in the renewable energy technology of photon-enhanced thermionic energy conversion devices. The metallic perovskite $SrVO_3$ has been successfully synthesized both as a bulk polycrystalline powder$^{[40,41]}$ and as a controlled (001)-oriented thin film grown with MBE.$^{[42]}$ $SrVO_3$ possesses a very high conductivity of about $10^5\ \Omega^{-1}\ \text{cm}^{-1}$ at room temperature, higher than $SrRuO_3$ (a prototypical metallic perovskite) and on par with elemental metals such as Pt.$^{[42]}$ $SrVO_3$ main- tains its structural stability even up to high temperatures of $1300\ ^\circ\text{C}$ and under reducing conditions during annealing with an $H_2/N_2$ or $H_2/Ar$ gas atmosphere.$^{[40,41,43]}$ Because perovskites are receptive to compositional modification, there are opportu- nities with doping $SrVO_3$ to lower its work function further. In this section, we consider alkaline earth metal doping in $SrVO_3$. We also consider the pristine (011) and (111) surface termina- tions to ascertain the full work function range of $SrVO_3$ and also obtain a more quantitative understanding of which surface terminations should be stable (and thus present in the highest quantity) in a real device. In addition, we consider the effect of surface segregation in $SrVO_3$ as a number of studies have suggested that A-site alloyed perovskites can show significant cation segregation.$^{[47,50-58]}$

Figure 6 contains the surface structures of (011) and (111) terminated $SrVO_3$. From Figure 6A, the (011) termination can either be O-terminated or ABO-terminated. Figure 6B,C show symmetric (111) surfaces that are B-terminated (Figure 6B) and $AO_3$-terminated (Figure 6C). The work functions and surface energies for these surface terminations (as well as surface ener- gies for (001) surfaces) were calculated and are tabulated below in Table 2.

From Table 2, one can see that the pristine (001) sur- faces have a lower surface energy and thus more stable than (011) and (111) surfaces, consistent with previous DFT studies.$^{[47,51,59]}$ Recent experimental$^{[60-64]}$ and computational studies$^{[57,64,65]}$ show that numerous perovskite materials exhibit segregation of alkaline earth elements such as Sr and Ba. From our current calculations, the overall order of stability is: $\gamma(001) < \gamma(111) < \gamma(011)$. The ABO-terminated (011) surface has a reasonably low work function of 2.32 eV, but overall the (011) and (111) surfaces possess higher work functions than AO-ter- minated (001). The fact that the (001) terminations of $SrVO_3$ are predicted to be the stable terminations, together with the fact that AO-terminated (001) $SrVO_3$ exhibits the lowest work func- tion of the surfaces explored here, further reinforces the choice of $SrVO_3$ as a potentially new low work function material.

We now turn to examining the effect of doping the alkaline earth metals Mg, Ca and Ba in $SrVO_3$. From Figure 2, it was suggested from comparing the work function values of $SrFeO_3$, $SrCoO_3$, and BSCF that doping Ba onto the A-site of Sr-based perovskites may result in a lowering of the work function. Here, we focus solely on the AO-terminated (001) surface of $SrVO_3$ since this is the low work function surface termination of interest. The AO-terminated (001) surface was simulated with concentrations of 25%, 50%, and 100% (this is equiva- lent to replacing one SrO row with a (Mg, Ca, Ba)O row) site fraction Mg, Ca, and Ba on the surface of the AO (001) slab (see Figure 7C). As shown in Figure 7, it was found that sur- face doping of Mg and Ca raised the work function for all con- centrations, while doping Ba lowered the work function for all concentrations. In particular, a site fraction of 100% Ba on the surface resulted in a very low work function of just 1.07 eV.

To better understand the role of Ba doping in lowering the work function (i.e., bulk doping versus surface dipole forma- tion), we also simulated a full layer of BaO in place of SrO in the middle of the AO (001) slab. It was found that placement of Ba in the middle of the slab resulted in a barely increased work function of 1.90 eV, which is 0.04 eV higher than pure $SrVO_3$. However, placement of the Ba in the top surface layer resulted in a significant lowering of the work function down to 1.07 eV, which is 0.79 eV lower than pure $SrVO_3$. This indicates that the work function lowering from Ba doping is due entirely to altering the surface dipole, rather than altering the Fermi level.

![](./images/811270270688952321_11.jpg)

Figure 6. $SrVO_3$ surface slabs of (011) and (111) orientations. A) The (011) orientation, whereby the top surface is O-terminated and the bottom surface is $ABO$-terminated. B) The (111) orientation, with both surfaces terminated as $AO_3$. C) The (111) orientation, now with both surfaces B-terminated. The large green spheres are Sr, medium-sized red spheres are V (in the middle of the octahedra), and the small red spheres are O.

By comparing the atomic positions of a pristine $SrVO_3$ surface and $SrVO_3$ with Ba in the surface layer, it is clear that the bond lengths between Ba and sub-surface O (the O in the $BO_2$ layer beneath the surface) is about $0.2\ \mathring{A}$ longer than the bond length between Sr and the same sub-surface O. This longer bond length is most likely the result of the larger ionic radius of Ba $(1.75\ \mathring{A})$ over Sr $(1.58\ \mathring{A}).^{[66]}$ This bond lengthening is expected to increase the size of the dipole for Ba at the surface in a direction that will lower the work function compared to Sr, and this bond lengthening is likely a major reason for the work function change with Ba doping. The work function reduction of 0.79 eV amounts to a surface dipole change of $\approx 0.26\ eV\text{-\AA}$ with the addition of a full Ba surface layer, which can be obtained directly from VASP simulations and is also calculable using the Helmholtz equation. $^{[21,22]}$

Because $Ba^{2+}$ is a larger cation than $Sr^{2+}$, it was worth investigating whether cation segregation may occur in doped $SrVO_3$. As discussed previously, cation segregation has been observed in many perovskite materials. $^{[50-57,60-66]}$ To ascertain if Ba segregation may occur in $SrVO_3$, we calculated the formation energy of substituting Ba in place of Sr for the two cases illustrated in Figure 7, and also calculated the segregation energy of dilute Ba (25% Ba substitution in the middle of the surface slab) to the surface of $SrVO_3$. The energy to substitute Sr for Ba, $\Delta E_{sub}$, was calculated using the equation $\Delta E_{sub}=E_{defected}-E_{perfect}-x(E_{BaO}-E_{SrO})$, where $E_{defected}$ is the total energy of the $SrVO_3$ surface slab with Ba substituting for Sr, $E_{perfect}$ is the energy of the undefected $SrVO_3$ slab, $x$ is the number of Ba substitutions (in this case $x = 1$ Ba atom in our

Table 2. Tabulated values of calculated work functions and surface energies for different $SrVO_3$ surface terminations. The work functions of (001) surfaces are repeated from Table 1 for clarity.

<table>
<thead>
<tr>
<th>Termination</th>
<th>Work function [eV]</th>
<th>Surface energy $[eV$ per $\mathring{A}^2]$</th>
</tr>
</thead>
<tbody>
<tr>
<td>(001)</td>
<td>1.86 (AO), 5.09 (BO₂)</td>
<td>0.052 (AO/BO₂ average)</td>
</tr>
<tr>
<td>(011)</td>
<td>2.32 (ABO), 7.23 (O)</td>
<td>0.094 (O/ABO average)</td>
</tr>
<tr>
<td>(111)</td>
<td>2.78 (B), 4.68 (AO₃)</td>
<td>0.078 (B/AO₃ average)</td>
</tr>
</tbody>
</table>

![](./images/811270270688952321_12.jpg)

Figure 7. Simulated AO-terminated (001) $SrVO_3$ surfaces with a single SrO layer replaced by AO (A = Mg, Ca, Ba), with a focus on Ba. A) Ba doping in the middle of the surface slab, resulting in a work function of 1.90 eV. B) Ba doping at the surface of the slab, resulting in an extremely low work function of 1.07 eV. The Ba segregation energy is calculated to be -0.64 eV/Ba, and indicates that Ba will preferentially segregate to the surface. The large green spheres are Sr, the large blue spheres are Ba, medium-sized red spheres are V (in the middle of the octahedra), and the small red spheres are O. The plot in C) shows how the calculated AO-terminated $SrVO_3$ work function changes when the top surface layer is alloyed with Mg, Ca, and Ba for different concentrations. The only dopant expected to lower the work function is Ba.

dilute calculation), and $E_{\text{BaO}}$ and $E_{\text{SrO}}$ are the total energies of rocksalt BaO and rocksalt SrO, respectively, which are taken as the reference states for Ba and Sr atoms. We found that the energy to substitute Ba for Sr in the middle of the $\text{SrVO}_3$ slab (Figure 7A) was 0.26 eV/Ba, while to substitute Ba for Sr on the surface (Figure 7B) was -0.38 eV/Ba. The energetic driving force for Ba surface segregation is just the difference of these energies, and is equal to -0.64 eV/Ba. Note that while the value of $\Delta E_{\text{sub}}$ is, in principle, dependent on temperature, pressure, and choice of reference state, the energy difference reported by calculating the segregation energy is the more physically insightful quantity, and its value is independent of the chosen reference state. The magnitude of this segregation energy is consistent with DFT calculations of cation surface segregation in other systems. $^{[67]}$ Therefore, if Ba is doped into $\text{SrVO}_3$, one may expect that over time Ba will diffuse to the surface and can dramatically lower the value of the work function. Analogous calculations for Mg and Ca doping indicate there is essentially no driving force (-0.07 eV per atom for Mg, -0.05 eV per atom for Ca) to segregate these species to the $\text{SrVO}_3$ surface compared to the Ba case. A combined experimental and DFT study of Ca, Sr, and Ba doping in (La, Sm)$\text{MnO}_3$ has suggested that cation segregation is a combination of both elastic (via lattice strain of mismatched cation sizes) and electrostatic effects attributed to the differing valences of alkaline earth and lanthanide elements as well as interaction with charged defects in doped $\text{LaMnO}_3$ $^{[57]}$ In our case of alkaline earth doping in $\text{SrVO}_3$ the predicted Ba cation segregation is presumably due primarily to lattice strain, as Mg, Ca, Sr and Ba are all 2+ cations and no charged defects or vacancies have been considered.

An important consideration of Ba doping in $\text{SrVO}_3$ is whether or not the surface-segregated Ba atoms are stable on the surface. To investigate this stability, we compared the adsorption energy of the Ba-O species present on the surface relative to bulk rocksalt BaO using standard GGA-based DFT methods for three cases: 1/4 monolayer Ba-O coverage on W(001) following ref. [21], 7/8 monolayer Ba-O coverage on $\text{Sc}_2\text{O}_3$(011) following ref. [22], and the present case of 1 monolayer Ba-O coverage on $\text{SrVO}_3$ (001). We use GGA-DFT methods here so that direct comparison with previous work can be made. These materials were chosen for comparison with $\text{SrVO}_3$ because W(001) with BaO is the dominant emitting surface of typical commercial thermionic cathode devices and $\text{Sc}_2\text{O}_3$(011) with BaO was found to be the most likely candidate for low work function surfaces in scandate cathode devices. $^{[21,22]}$ We found that the adsorption energy (per Ba-O formula unit) for W(001), $\text{Sc}_2\text{O}_3$(011) and $\text{SrVO}_3$(001) are: 0.71 eV per Ba, -0.27 eV per Ba, and -1.19 eV per Ba, respectively. Because the time to desorb an atom from a material surface scales exponentially with the adsorption energy, it is evident from the above calculations that at $T = 1000$ K, which is an approximate temperature used in thermionic emission devices, Ba will reside on the $\text{SrVO}_3$(001) surface approximately five orders of magnitude longer than on $\text{Sc}_2\text{O}_3$(011), and approximately nine orders of magnitude longer than on W(001). Overall, the surface-segregated Ba atoms in $\text{SrVO}_3$ are much more strongly bonded to the $\text{SrVO}_3$ surface than the volatile Ba-O surface dipole layers present in W- and $\text{Sc}_2\text{O}_3$-based electron sources. This may provide a method of obtaining an electron emission source that simultaneously exhibits an ultra-low work function of 1.07 eV and operating lifetime orders of magnitude longer than current dispenser cathode technologies.

As we have only considered a small representative set of perovskite materials in this study, it is possible that other low work function perovskite materials besides $\text{SrVO}_3$ exist. The O 2p-band center provides an approximate way to predict the work function of either the AO- or $\text{BO}_2$-terminated surface from strictly a bulk materials property. In general, surface supercell calculations are quite computationally expensive (especially with HSE functionals), while bulk calculations are many times faster as a result of fewer atoms per supercell and higher supercell symmetry. Thus, the correlation between bulk O 2p-band center and surface work function may enable fast, bulk materials screening of the O 2p-band center to predict work function values of perovskite alloys. Calculation of the bulk O 2p-band center is roughly a factor of 25 times faster than calculating the work function (a factor of 50 considering both the AO- and $\text{BO}_2$-terminated surfaces), and thus provides a useful estimate of a perovskite work function with comparatively minimal computational time. By high-throughput calculation of perovskite band gaps and O 2p-band centers one could screen for low work function materials. $^{[68-70]}$ In particular, any material that meets the conditions of zero (or near-zero) band gap and low O 2p-band center may warrant further investigation by way of surface calculations for quantitative work function values. Some preliminary high-throughput DFT screening using GGA+U has indicated that perovskites within the family of (La, Pr, Y) (Ti, V)$\text{O}_3$ and $\text{SrVO}_3$ have deep O 2p band centers and a partially filled 3d band, and thus should have low work functions, consistent with the trends in Figure 2. While many of the (La, Pr, Y)(Ti, V)$\text{O}_3$ materials are Mott-Hubbard insulators and thus may not be sufficiently conducting for low work function cathode applications, further A-site alloying of alkaline earths and B-site alloying with other transition metals within this low O 2p-band composition space may potentially yield smaller (or zero) bandgap materials that are worth further investigation.

## 5. Conclusions

In this study, we have computationally explored 20 technologically relevant perovskite materials at idealized undefected compositions to understand how their chemistry influences the value of the work function, and then use this new understanding to search for a new, low work function material for electron emission applications. We have explained compositional trends in the work function using concepts of bonding ionicity, hybridization, band filling, and surface dipoles. We found that the bulk O 2p-band center can function as a semi-quantitative descriptor of the work function for both AO- and $\text{BO}_2$-terminated (001) perovskite surfaces. Our usage of the O 2p-band center descriptor has provided both further understanding of the work function physics for these materials and may enable fast computational screening of perovskite materials with a particular work function value. Broadly, the work function depends both on the bulk electronic band filling ($E_{\text{Fermi}}$ position) and the influence of surface dipoles. Based on our analysis, the value of the $\text{BO}_2$ surface work function

---

Adv. Funct. Mater. 2016,
DOI: 10.1002/adfm.201600243

© 2016 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
wileyonlinelibrary.com 9

is dominated by bulk band positions while the work function of the AO surfaces is dominated by surface dipoles. Understanding the work function trends in perovskites as well as the physics governing these trends (e.g., band filling versus surface dipoles) is pivotal for the rational design of perovskite-containing devices involving electron transport at interfaces or surfaces.

We have computationally predicted $SrVO_3$ to be a new, promising low work function material for electron emission applications such as high power microwave devices, satellite communications, and possibly as an emissive layer for photo-n-enhanced thermionic energy converters. $SrVO_3$ is not only predicted to have a low work function, but has been experimentally shown to be stable in reducing environments and exhibit a high electrical conductivity. When doped with Ba, we have shown that Ba will preferentially segregate to the surface and result in an ultralow work function down to nearly 1 eV. The Ba contained in the $SrVO_3$ surface-emitting layer is significantly more stable than the Ba-containing dipole layers used in conventional thermionic electron emission cathodes such as the B-type W dispenser and scandate cathodes, which should thus produce a stable, highly-emissive, long lifetime electron emitter.

## 6. Computational Methods

Perovskite structures generally form in the $Pm\overline{3}m$ (cubic, space group 221), $P4mm$ (tetragonal, space group 99), $Pbnm/Pnma$ (orthorhombic, space group 62), and $R\overline{3}c$ (rhombohedral, space group 167) symmetries.[71] In this study, we used idealized, undefected $2\times2\times2$ pseudocubic structure lattice constants adopted from full relaxation of the ideal cubic $ABO_3$ symmetry ($Pm\overline{3}m$, $SrTiO_3$, $SrVO_3$, $SrFeO_3$, $SrCoO_3$, $SrRuO_3$, $Ba_{0.5}Sr_{0.5}Co_{0.75}Fe_{0.25}O_3$), orthorhombic symmetry ($Pbnm$, $LaScO_3$, $LaTiO_3$, $LaVO_3$, $LaCrO_3$, $LaMnO_3$, $La_{1-x}Sr_xMnO_3$, $LaFeO_3$, $LaRuO_3$), and rhombohedral symmetry ($R\overline{3}c$, $LaCoO_3$, $LaNiO_3$), and the structures are shown in Figure 1. Our use of pseudocubic structures provides a good approximation to the average cubic symmetry exhibited by many of these materials at elevated temperatures of $T>500$ K,[5] and provides a structurally consistent set of materials to investigate compositional trends in the surface work function. We expect the compositional trends in work function and physics described in this work to also hold under room temperature conditions. However, some quantitative differences in work function should be expected. Figure 1 also provides examples of the asymmetric (Figure 1C, used for $La_{1-x}Sr_xMnO_3$) and symmetric (Figure 1D,E, used for all other materials besides $La_{1-x}Sr_xMnO_3$) surface slabs used for the work function calculations. Additional details on perovskite bulk and surface calculations are provided in Section 1 of the Supporting Information.

We performed all of our calculations using density functional theory (DFT) as implemented by the Vienna ab initio simulation package (VASP)[72] with a plane wave basis set. We used the hybrid HSE exchange and correlation functional of Heyd, Scuseria, and Ernzerhof[18] with Perdew-Burke-Ernzerhof (PBE)-type pseudopotentials[73] utilizing the projector augmented wave (PAW)[74] method for La, Ca, Mg, Ba, Sr, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Ru, and O atoms. The fraction of Hartree-Fock (HF) exchange in the HSE method for each material was obtained from refs. [19,20]. In refs. [20,19] the fraction of HF exchange was fitted to reproduce the experimentally measured bulk bandgap and densities of states from ultraviolet photoemission spectroscopy (UPS) measurements. Thus, the fractions of Hartree-Fock exchange used in our HSE calculations were 0.25 ($LaScO_3$), 0.15 ($LaTiO_3$, $LaCrO_3$, $LaMnO_3$, $LaFeO_3$), 0.125 ($LaVO_3$), 0.05 ($LaCoO_3$), and 0 ($LaNiO_3$). For the band insulators $SrTiO_3$ and $LaAlO_3$, a value of 0.25 is used for the HF exchange fraction.[75,76] For the remaining materials, the HF exchange values used were the same as the respective transition metal-containing lanthanide perovskite. Therefore, for $SrVO_3$, $SrFeO_3$, $SrCoO_3$, $Ba_{0.5}Sr_{0.5}Co_{0.75}Fe_{0.25}O_3$ (BSCF) and $La_{1-x}Sr_xMnO_3$ (LSM), the HF values used were 0.125, 0.15, 0.05, 0.05, and 0.15, respectively. This method of tuning the amount of HF exchange to reproduce experimental bulk electronic structure properties such as the bandgap has recently been shown to provide more accurate Li insertion voltages (a quantity that depends sensitively on the electronic structure near the Fermi level) than the default HF exchange of 0.25 for a wide range of transition metal oxide materials.[77] Last, the HF exchanges for $LaRuO_3$ and $SrRuO_3$ have, to our knowledge, not been thoroughly characterized in the same manner as the other perovskites studied here. Therefore, we use an HF value equal to that of $LaFeO_3$ (HF exchange of 0.15) because Fe and Ru are in the same column of the periodic table and thus can be expected to exhibit similar chemistry. Because $LaRuO_3$ and $SrRuO_3$ have not been as widely studied computationally with hybrid functionals, their calculated work functions may show larger errors than the other systems studied here.

The valence electron configurations of the atoms utilized in the calculations were La: $5s^25p^66s^25d^1$, Ca: $3s^23p^64s^2$, Mg: $2s^22p^63s^2$, Ba: $5s^25p^66s^2$, Sr: $3s^23p^64s^2$, Sc: $3s^23p^64s^23d^1$, Ti: $3s^23p^64s^23d^2$, V: $3p^64s^13d^4$, Cr: $3p^64s^13d^5$, Mn: $3p^64s^23d^5$, Fe: $3s^23p^64s^13d^7$, Co: $4s^13d^8$, Ni: $3p^64s^23d^8$, Al: $3s^23p^1$, Ru: $4p^65s^14d^7$, and O: $2s^22p^4$, respectively. The plane wave cutoff energies were, at a minimum, 30% larger than the maximum plane wave energy of the chosen pseudopotentials, and equal to a minimum of 405 eV for all systems. We performed all calculations with spin polarization. The Monkhorst-Pack scheme was used for reciprocal space integration in the Brillouin Zone for bulk perovskite materials.[78] For surface calculations we used a $\Gamma$-centered reciprocal space integration scheme instead of Monkhorst-Pack as we use only one k-point, and the electronic minimization was performed simultaneously for all energy bands. A $2\times2\times2$ k-point mesh was used for the $2\times2\times2$ bulk supercells of all $LaBO_3$ materials (40 atoms per cell), with total energy convergence (ionic and electronic degrees of freedom) of 3 meV per formula unit. For surface slab calculations, we reduced the k-point mesh to $1\times1\times1$ and maintained a minimum vacuum distance of $15$ Å. We verified that all calculated work functions were well-converged (error of $\pm$0.1 eV) with respect to both slab thickness and vacuum region thickness, with the exception of $LaAlO_3$ and $LaScO_3$, which are highly polar materials and with work functions which converge very slowly with slab thickness. Therefore, work function results for $LaScO_3$ and $LaAlO_3$ have a larger error of $\pm$0.4 eV, based on GGA calculations of symmetric (001) surface slabs of $LaAlO_3$ between

5 and 17 layers. Last, we implemented the dipole correction in VASP to ensure vacuum level convergence, and the dipole correction was calculated only in the axial direction normal to the terminating surface. Additional details regarding the bulk and surface calculations of the perovskite materials considered here can be found in Section 1 and Section 2 of the Supporting Information.

# Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

# Acknowledgements
This work was supported by the US Air Force Office of Scientific Research through grants No. FA9550-08-0052 and No. FA9550-11-0299. Computational support was provided by the Extreme Science and Engineering Discovery Environment (XSEDE), which is supported by National Science Foundation Grant No. OCI-1053575. This research was performed using the compute resources and assistance of the UW-Madison Center For High Throughput Computing (CHTC) in the Department of Computer Sciences.

Received: January 15, 2016
Revised: April 5, 2016
Published online:

[1] J. Luo, Z.-J. Qiu, J. Deng, C. Zhao, J. Li, W. Wang, D. Chen, D. Wu, M. Östling, T. Ye, S.-L. Zhang, Microelectron. Eng. 2014, 120, 174.
[2] T. Susaki, A. Makishima, H. Hosono, Phys. Rev. B 2011, 84, 115456.
[3] P. Zubko, S. Gariglio, M. Gabay, P. Ghosez, J.-M. Triscone, Annu. Rev. Condens. Matter Phys. 2011, 2, 141.
[4] J. Suntivich, H. A. Gasteiger, N. Yabuuchi, H. Nakanishi, J. B. Goodenough, Y. Shao-Horn, Nat. Chem. 2011, 3, 546.
[5] Y.-L. Lee, J. Kleis, J. Rossmeisl, D. Morgan, Phys. Rev. B 2009, 80, 224101.
[6] Y.-L. Lee, J. Kleis, J. Rossmeisl, Y. Shao-Horn, D. Morgan, Energy Environ. Sci. 2011, 4, 3966.
[7] J. Suntivich, J. K. May, H. A. Gasteiger, J. B. Goodenough, Y. Shao-Horn, Science 2011, 334, 1383.
[8] A. M. Kolpak, S. Ismail-Beigi, Phys. Rev. B 2012, 85, 195318.
[9] K. Garrity, A. Kolpak, S. Ismail-Beigi, J. Mater. Sci. 2012, 47, 7417.
[10] X. F. Chen, H. Lu, W. G. Zhu, O. K. Tan, Surf. Coat. Technol. 2005, 198, 266.
[11] X. Chen, H. Lu, H. Bian, W. Zhu, C. Sun, O. Tan, J. Electroceram. 2006, 16, 419.
[12] T.-H. Yang, Y.-W. Harn, K.-C. Chiu, C.-L. Fan, J.-M. Wu, J. Mater. Chem. 2012, 22, 17071.
[13] H. J. Bian, X. F. Chen, J. S. Pan, C. Q. Sun, W. Zhu, J. Vac. Sci. Technol. B 2007, 25, 817.
[14] X. W. Li, A. Gupta, G. Xiao, G. Q. Gong, Appl. Phys. Lett. 1997, 71, 1124.
[15] J. Teresa, A. Barthelemy, A. Fert, J. Contour, F. Montaigne, P. Seneor, Science 1999, 286, 507.
[16] M. Mrovec, J. M. Albina, B. Meyer, C. Elsässer, Phys. Rev. B 2009, 79, 245121.
[17] N. Horiuchi, T. Hoshina, H. Takeda, T. Tsurumi, J. Ceram. Soc. Jpn. 2010, 118, 664.
[18] J. Heyd, G. E. Scuseria, M. Ernzerhof, J. Chem. Phys. 2003, 118, 8207.
[19] F. Cesare, J. Phys.: Condens. Matter 2014, 26, 253202.
[20] J. He, C. Franchini, Phys. Rev. B 2012, 86, 235117.
[21] V. Vlahos, J. H. Booske, D. Morgan, Phys. Rev. B 2010, 81, 054207.
[22] R. M. Jacobs, J. H. Booske, D. Morgan, J. Phys. Chem. C 2014, 118, 19742.
[23] P. M. Zagwijn, J. W. M. Frenken, U. van Slooten, P. A. Duine, Appl. Surf. Sci. 1997, 111, 35.
[24] J. H. Booske, Phys. Plasmas 2008, 15, 055502.
[25] A. S. Gilmour, Principles of Traveling Wave Tubes, Artech House, Norwood, MA, USA 1994.
[26] J. W. Schwede, I. Bargatin, D. C. Riley, B. E. Hardin, S. J. Rosenthal, Y. Sun, F. Schmitt, P. Pianetta, R. T. Howe, Z.-X. Shen, N. A. Melosh, Nat. Mater. 2010, 9, 762.
[27] J. W. Schwede, T. Sarmiento, V. K. Narasimhan, S. J. Rosenthal, D. C. Riley, F. Schmitt, I. Bargatin, K. Sahasrabuddhe, R. T. Howe, J. S. Harris, N. A. Melosh, Z. X. Shen, Nat. Commun. 2013, 4, 1576.
[28] D. W. Reagor, S. Y. Lee, Y. Li, Q. X. Jia, J. Appl. Phys. 2004, 95, 7971.
[29] G. M. Vanacore, L. F. Zagonel, N. Barrett, Surf. Sci. 2010, 604, 1674.
[30] T. Kida, G. Guan, A. Yoshida, Chem. Phys. Lett. 2003, 371, 563.
[31] K. A. Stoerzinger, M. Risch, J. Suntivich, W. M. Lu, J. Zhou, M. D. Biegalski, H. M. Christen, Ariando, T. Venkatesan, Y. Shao-Horn, Energy Environ. Sci. 2013, 6, 1582.
[32] W. T. Hong, K. A. Stoerzinger, B. Moritz, T. P. Devereaux, W. Yang, Y. Shao-Horn, J. Phys. Chem. C 2015, 119, 2063.
[33] M. Krčmar, C. L. Fu, Phys. Rev. B 2003, 68, 115404.
[34] B. Zheng, N. Binggeli, Phys. Rev. B 2010, 82, 245311.
[35] W. Tang, E. Sanville, G. Henkelman, J. Phys.: Condens. Matter 2009, 21, 084204.
[36] G. Henkelman, A. Arnaldsson, H. Jónsson, Comput. Mater. Sci. 2006, 36, 354.
[37] W. Maus-Friedrichs, M. Frerichs, A. Gunhold, S. Krischok, V. Kempter, G. Bihlmayer, Surf. Sci. 2002, 515, 499.
[38] M. Minohara, R. Yasuhara, H. Kumigashira, M. Oshima, Phys. Rev. B 2010, 81, 235322.
[39] S. P. S. Badwal, T. Bak, S. P. Jiang, J. Love, J. Nowotny, M. Rekas, C. C. Sorrell, E. R. Vance, J. Phys. Chem. Solids 2001, 62, 723.
[40] T. Maekawa, K. Kurosaki, S. Yamanaka, J. Alloys Compd. 2006, 426, 46.
[41] M. Onoda, H. Ohta, H. Nagasawa, Solid State Commun. 1991, 79, 281.
[42] J. A. Moyer, C. Eaton, R. Engel-Herbert, Adv. Mater. 2013, 25, 3578.
[43] S. Hui, A. Petric, Solid State Ionics 2001, 143, 275.
[44] Y.-L. Lee, D. Lee, X. D. Wang, H. N. Lee, D. Morgan, Y. Shao-Horn, J. Phys. Chem. Lett. 2016, 7, 244.
[45] A. Grimaud, K. J. May, C. E. Carlton, Y.-L. Lee, M. Risch, W. T. Hong, J. Zhou, Y. Shao-Horn, Nat. Commun. 2013, 4, 2439.
[46] W. T. Hong, M. Risch, K. A. Stoerzinger, A. Grimaud, J. Suntivich, Y. Shao-Horn, Energy Environ. Sci. 2015, 8, 1604.
[47] Y.-L. Lee, D. Morgan, Phys. Rev. B 2015, 91, 195430.
[48] G. Jacek, F. Fabio, N. Claudine, Rep. Prog. Phys. 2008, 71, 016501.
[49] J. Suntivich, W. T. Hong, Y.-L. Lee, J. M. Rondinelli, W. Yang, J. B. Goodenough, B. Dabrowski, J. W. Freeland, Y. Shao-Horn, J. Phys. Chem. C 2014, 118, 1856.
[50] Z. Cai, M. Kubicek, J. Fleig, B. Yildiz, Chem. Mater. 2012, 24, 1116.
[51] H. Ding, A. V. Virkar, M. Liu, F. Liu, Phys. Chem. Chem. Phys. 2013, 15, 489.
[52] Y. Orikasa, E. J. Crumlin, S. Sako, K. Amezawa, T. Uruga, M. D. Biegalski, H. M. Christen, Y. Uchimoto, Y. Shao-Horn, ECS Electrochem. Lett. 2014, 3, F23.
[53] Z. Cai, Y. Kuru, J. W. Han, Y. Chen, B. Yildiz, J. Am. Chem. Soc. 2011, 133, 17696.
[54] Z. Feng, Y. Yacoby, W. T. Hong, H. Zhou, M. D. Biegalski, H. M. Christen, Y. Shao-Horn, Energy Environ. Sci. 2014, 7, 1166.
[55] J. Druce, T. Ishihara, J. Kilner, Solid State Ionics 2014, 262, 893.

Adv. Funct. Mater. 2016,
DOI: 10.1002/adfm.201600243

© 2016 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
wileyonlinelibrary.com 11

[56] M. Burriel, S. Wilkins, J. P. Hill, M. A. Munoz-Marquez, H. H. Brongersma, J. A. Kilner, M. P. Ryan, S. J. Skinner, Energy Environ. Sci. 2014, 7, 311.

[57] W. Lee, J. W. Han, Y. Chen, Z. Cai, B. Yildiz, J. Am. Chem. Soc. 2013, 135, 7909.

[58] T. T. Fister, D. D. Fong, J. A. Eastman, P. M. Baldo, M. J. Highland, P. H. Fuoss, K. R. Balasubramaniam, J. C. Meador, P. A. Salvador, Appl. Phys. Lett. 2008, 93, 151904.

[59] Y. Choi, D. S. Mebane, M. C. Lin, M. Liu, Chem. Mater. 2007, 19, 1690.

[60] J. Druce, H. Tellez, M. Burriel, M. D. Sharp, L. J. Fawcett, S. N. Cook, D. S. McPhail, T. Ishihara, H. H. Brongersma, J. A. Kilner, Energy Environ. Sci. 2014, 7, 3593.

[61] J. Kilner, S. Skinner, H. Brongersma, J. Solid State Electrochem. 2011, 15, 861.

[62] I. C. Fullarton, J. P. Jacobs, H. E. van Benthem, J. A. Kilner, H. H. Brongersma, P. J. Scanlon, B. C. H. Steele, Ionics 1995, 1, 51.

[63] Z. Feng, Y. Yacoby, W. T. Hong, H. Zhou, M. D. Biegalski, H. M. Christen, Y. Shao-Horn, Energy Environ. Sci. 2014, 7, 1166.

[64] D. Lee, Y.-L. Lee, W. T. Hong, M. D. Biegalski, D. Morgan, Y. Shao-Horn, J. Mater. Chem. A 2015, 3, 2144.

[65] Y.-L. Lee, M. J. Gadre, Y. Shao-Horn, D. Morgan, Phys. Chem. Chem. Phys. 2015, 17, 21643.

[66] R. Shannon, Acta Crystallogr., Sect. A 1976, 32, 751.

[67] M. J. Gadre, Y.-L. Lee, D. Morgan, Phys. Chem. Chem. Phys. 2012, 14, 2606.

[68] S. Curtarolo, G. L. W. Hart, M. B. Nardelli, N. Mingo, S. Sanvito, O. Levy, Nat. Mater. 2013, 12, 191.

[69] A. Jain, G. Hautier, C. J. Moore, S. Ping Ong, C. C. Fischer, T. Mueller, K. A. Persson, G. Ceder, Comput. Mater. Sci. 2011, 50, 2295.

[70] T. Angsten, T. Mayeshiba, H. Wu, D. Morgan, New J. Phys. 2014, 16, 015018.

[71] M. A. Pena, J. L. G. Fierro, Chem. Rev. 2001, 7, 1981.

[72] G. Kresse, J. Furthmuller, Phys. Rev. B 1996, 54, 11169.

[73] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1996, 77, 3865.

[74] G. Kresse, D. Joubert, Phys. Rev. B 1999, 59, 1758.

[75] R. Wahl, D. Vogtenhuber, G. Kresse, Phys. Rev. B 2008, 78, 104116.

[76] M. Choi, F. Oba, Y. Kumagai, I. Tanaka, Adv. Mater. 2013, 25, 86.

[77] D.-H. Seo, A. Urban, G. Ceder, Phys. Rev. B 2015, 92, 115118.

[78] H. J. Monkhorst, J. D. Pack, Phys. Rev. B 1976, 13, 5188.
---
12 wileyonlinelibrary.com
© 2016 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
Adv. Funct. Mater. 2016,
DOI: 10.1002/adfm.201600243