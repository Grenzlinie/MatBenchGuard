# Physical Chemistry Chemical Physics

## Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: Y. Chan, I. Huang and M. Tsai, *Phys. Chem. Chem. Phys.*, 2019, DOI: 10.1039/C9CP02977J.

![](./images/812742337917616128_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the [Information for Authors].

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions] and the [Ethical guidelines] still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812742337917616128_2.jpg)

rsc.cc/pccp

# Enhancing C-C Bond Formation by Surface Strain: A Computational Investigation for the C2 and C3 Intermediate Formation on the Strained Cu Surfaces

Yu-Te Chan, I-Shou Huang, Ming-Kang Tsai*

Department of Chemistry, National Taiwan Normal University, Taipei, 11677, Taiwan.

## Abstract

In this study, 121 copper (100) models with surface strain are used for simulating the C-C bond formation by CO₂ electrochemical reduction. Its catalytic properties have been characterized by considering the formation energies of various C1 and C2 intermediates, and critical reaction steps along CO₂/CO reduction reactions. It turns out that the surface strain with one compressed axis and one elongated axis is geometrically beneficial for C2 products formation. The surface strain stabilizes the CO binding on the bridge sites (*CO_(bridge)) and the C2 intermediates – *OCCOH and *OCCO; remains at low activation energy of CO–CO coupling around 0.57 to 0.69 eV. The surface strain also suppresses *H formation which would allow more *CO formation leading to higher CO₂/CO reduction efficiency. Furthermore, the displaced copper models only exist under high compressing strain were found to having great potential to activate CO₂/CO into C3 products in a mild condition during the electrochemical reduction process. The activation energies for the third carbon atom coupling with C2 intermediates are 0.45 – 0.63 eV subject to the condition on the surface strain. The atomic arrangement with adjacent rectangle and parallelogram is found to play an important role in producing C3 products. The selectivity of C-C bond formation induced by surface strain is demonstrated by this computational study.

## Introduction

Due to the climbing CO₂ concentration in the atmosphere, human beings are facing several challenging issues like global warming, extreme climate, rising sea level, ecological crisis and ocean acidification.¹⁻⁴ Converting the waste gas – CO₂ back to a useful chemical is considered one of the critical but challenging tasks to fix the increasing CO₂. Nature has shown a great example where CO₂ molecules are integrated by RuBisCO to form new C-C bonds in the Calvin cycle.⁵ On the other hand, scientists have been actively developing various CO₂ conversion approaches using man-made catalysts.⁶⁻⁹ Back to 1994, Hori et al. reported the electrocatalytic CO₂ reduction in aqueous solution using pure metals electrodes where Au, Ag, Zn, Pd and Ga electrodes were found to mainly generate CO; Pb, Hg, In, Sn, Cd and Tl

electrodes were found to generate formic acid; Ni, Fe, Pt and Ti electrodes could produce H2; only Cu electrode could produce hydrocarbons.¹⁰

With using the Cu electrode in the electrocatalytic CO₂ reduction in the aqueous solution, a C2 species - ethylene was observed at the applied voltage of -0.72V vs. RHE by Hori et al. Contradictorily, CH₄ was generated at less than -0.82V vs. RHE. Thus, C-C bond formation of ethylene generation could exclude the involvement with the precursors of methane.¹¹ Schouten et al. compared the pH-dependent ethylene formation on Cu(100) and Cu(111) surfaces.¹² Ethylene was generated at -0.4V vs. RHE if pH < 12 on Cu(100) surface, but the same measurement using Cu(111) surface was pH-independent and required a more negative potential at -0.7V vs. RHE. Consequently, a key CO-CO coupling intermediate was proposed to be responsible for the C-C bond formation of ethylene generation.¹³ Recently, the OCCOH intermediate was determined by the real-time Fourier transformation infrared spectroscopy at the low potential of the region at -0.2V, being complemented with DFT calculations.¹⁴ The observed phenomena of applying a low potential at -0.2V to drive the C-C bond formation on Cu(100) surface was in line with the prediction by Montoya et al. whereas the activation energies of CO-CO coupling were calculated as 0.33 and 0.66 eV for Cu(100) and Cu(111) surfaces, respectively, under the solvation of mono-layer water approximation.¹³

In order to improve the selectivity of CO₂ electrochemical reduction in producing C2 product, Kanan et al. synthesized the Cu nanoparticles containing grain boundaries and observed a substantial enhancement in Faraday efficiency of generating multi-carbon hydrocarbons.¹⁵ Such enhancement was proportionally correlated with the density of the grain boundary areas.¹⁶ Cheng et al. conducted the atomistic modeling for the chemical vapor deposition process of Cu nanoparticles whereas the strong CO bind sites with under-coordinated surface square sites could promote C–C coupling.¹⁷ Despite these catalytic active sites on the Cu nanoparticles may have been realistically simulated, the driving force of forming such surface structures has not been fully elaborated as well as the electronic structure of the adsorbed intermediates.

Having the recent progress in mind, we therefore propose a series of strain-imposed Cu(100) surface models and investigate the adsorption of the key intermediates, e.g. *H, *COOH, *CO, *CHO and *OCCOH under the application of different levels of strain. The activation energies of CO–CO coupling, the key step for C–C bond formation, in different surface strain condition are also calculated. Additionally, a displaced copper (100) surface morphology which only exists under the high compressive strain is observed. Its unique atomic arrangement provides a feasible way to catalyze CO₂/CO into C3 products.

Two C2 intermediates *CCH and *CCOH coupling with *CO are investigated by searching the transition states and calculating the free energies along the reaction pathway. The C3 intermediates formation step should be attainable on such a displaced copper with reasonably low activation energy.

### Computational details
All DFT calculations are performed using the Vienna ab initio simulation package (VASP) code.¹⁸⁻²⁰ Projector augmented waves(PAW) are used to describe the ion cores,²¹ and the exchange-correlation interactions are expressed with a generalized gradient approximation (GGA) in the form of the revised-PBE (Perdew, Burke, and Ernzerhof) functional.²²⁻²³ The spin polarization is considered in our calculation. The plane-wave basis set is expanded to the cutoff energy level of 400eV. A $4 \times 3 \times 1$ k-point mesh generated by the Monkhorst-Pack are used. All models are fully relaxed until the maximum of Hellmann-Feynman forces converged to $0.05\ \text{eV}\mathring{\text{A}}^{-1}$. The Nudged Elastic Band (NEB) method was used for searching transition states.²⁴ A set of $4 \times 3$ Cu(100) models (4 layers) are used. In order to study the phenomenon of surface strain, 121 models are created from a combination of different cell constant $\vec{a}$ and $\vec{b}$, each axis contains 11 grids. More model details, structural and electronic properties can be found in the Figures S1-S2 of electronic supplementary information (ESI). The solvation effect is not included in all formation energies calculations for reducing the computational expense. For better accuracy, an explicit water layer including $32\ \text{H}_2\text{O}$ molecules and one extra Na atom is used for searching transition states along C2/C3 intermediates formation pathway. Further details can be found in ESI. The applied potential on cathode in our models is about -0.62V. All activation energies and reaction energies are calculated by averaging five independent calculations and be corrected into free energies by considering the zero-point energy and entropy term. The vibrational frequencies are obtained by finite difference method. The details of explicit solvation modeling in provided in ESI.

We used a model with explicit water layer containing 32 water molecules and 1 extra sodium atom. The inclusion of a sodium atom introduces the applied potential effect, being resulted from the $\text{Na}^+$ ion solvation and the valence electron of Na atom transfer to electrode surface. The applied potential effect on the cathode is estimated to be -0.62 V at $pH=7$ condition using the following equation (Figure S3):

$$U_{RHE} = (\Phi - E_f) - 4.4 + 0.059 \times pH = 3.36 - 4.4 + 0.059 \times 7 = -0.62V$$

where $\Phi$ denotes the calculation electrostatic potential, $\text{E}_\text{f}$ denoted the Fermi energy, and the free energy of hydrogen electrode is 4.4 eV. This applied potential derived from 2CO* qualitatively represents the electrode potential effect in all reaction pathway toward 2C products as shown by Cheng et al, being deviated by only 0.08 eV from the averaged value.²⁵

Each water layer is pre-equilibrated for 2 ns with frozen adsorbate and electrode using classical molecular dynamics (MD) simulations of LAMMPS.²⁶ Subsequently, each classical MD is followed by 5 ps first-principle MD before optimization. All energies along C2 and C3 intermediates forming pathway were calculated by averaging 5 independent set (initial, TS, and final). All of the MD simulation employs 1 fs timestep. The classical MD adapts a tunable-polarizability water model, being specifically suitable for interfacial simulation.²⁷

## Results and Discussion
### I. Relative formation energies

Six intermediates along the CO₂RR and HER pathway on Cu(100) surface are calculated without water layers as schematically shown in Figure S3. The formation energies ($\Delta E_{form}^X$) of the intermediates, X = H, CO₍ₐₜₒₚ₎, CO₍ᵦᵣᵢdgₑ₎, CHO, COOH and OCCOH are calculated as the following:

$$
\mathrm{E_{form}^X = E^{X\cdot Cu} - (E^{Cu} + N_cE_c + N_HE_H + N_OE_O)}
$$
Eq. (1)

where $\mathrm{E^{Cu}}$ denotes the energy of Cu(100) surface, $E_c$, $E_H$, and $E_O$ denote the energies of elements in their standard states ($C_{(graphene)}$, $H_2$, and $O_2$) , $N_c$, $N_H$, and $N_O$ represent number of elements in the intermediate, and $\mathrm{E^{X\cdot Cu}}$ denotes the energy for the adsorbed intermediate. Thus, the more negative value of $\mathrm{E_{form}^X}$ indicates the stronger interaction upon the adsorption on the Cu surface. In Figures S4, the relative energy of Cu(100) surface and the relative $\mathrm{E_{form}^X}$, X = H, CO and OCCOH are summarized in respect to the non-strained counterpart. The relative $\mathrm{E_{form}^X}$ can be defined as the following:

$$
\Delta \mathrm{E_{form}^X = E_{strain}^X - E_{non-strain}^X}
$$
Eq. (2)

The energy of the bare and non-strained Cu(100) surface, denoted as (0, 0), is slightly higher than the energy of (1, 1) strained surface by 0.04 eV since we use the cell constant from experimental data rather than computational data for our pristine model, as shown in Figures S4a. The notation (0, 0) denotes the percentage of strain applied along the lattice vectors $\vec{a}$ and $\vec{b}$ of Cu surface, respectively. A positive or negative value represents the extent of elongation or compression, respectively. For instance, (1, -1) denotes elongating $\vec{a}$ by +1% and compressing $\vec{b}$ by 1%. Particularly, for the adsorption of the intermediates like *CO, *CHO and *OCCOH are found to be enhanced under the application of Cu surface strain as shown in the heat maps of Figures S4b – S4f. For C2 intermediate *OCCOH and its precursor *CO₍ᵦᵣᵢdgₑ₎, both cases appear to have stronger binding on the upper left region, representing the combinations of compressed $\vec{a}$ and elongated $\vec{b}$. To identify the most favorable surface strain for producing

C2 and C3 products, the adsorption of *H, *CO<sub>atop</sub>, *CO<sub>bridge</sub>, *CHO, *COOH and *OCCOH on the strained surfaces are comprehensively investigated along the direction of compressing $\vec{a}$ and elongating $\vec{b}$ as shown in Figure 1 where those heat map patterns can be categorized into 3 groups. Group 1 includes *CO<sub>atop</sub>, *CHO and *COOH (Figures 1a-1c), and these heat map patterns generally align well with the prediction of d-band theory – the higher d-band center position correlates to stronger binding. In Figure S5, the favorable binding regions with high d-band center, being enhanced by the strain, are predicted in the upper right region. In Figures 1b-1c, the most elongated $\vec{b}$ cases appear to disfavor *CHO and *COOH adsorption. The closest distance from the oxygen atom of the *CHO to *COOH to the surface Cu atoms are around at 2.82Å without the presence of surface strain. The bulking Cu atoms of the elongated $\vec{b}$ models enhance the repulsive interaction between oxygen and surface Cu atoms. Group 2 only contains *H, being absorbed on the 4-fold hollow site. The heat map pattern of *H does not correlate well the d-band center distribution. The favorable adsorption region is identified in the cases of non-elongated $\vec{b}$ but compressed $\vec{a}$ as shown by the dotted triangle in Figure 1d. The small radius of *H appears to prefer the shorter Cu-Cu distance environment in the lower-left region of Figure 1d. Group 3 contains *CO<sub>bridge</sub> and *OCCOH on bridge sites with the strong bindings region as shown by the dotted inverted V-shape region in Figures 1e-1f, which also does not correlate well with the pattern of d-band center.

Interestingly, several strong binding are identified with 6% compression along $\vec{a}$ where *CO<sub>bridge</sub> and *OCCOH can be further stabilized up to 0.11 and 0.16 eV, respectively. Such stabilization can attribute to the suitable distances of copper atoms $r_{(Cu-Cu)_a}$ and $r_{(Cu-Cu)_b}$. Five structural descriptors, i.e. $A_1$, $A_2$, $r_{C-C}$, $r_{(Cu-Cu)_a}$ and $r_{(Cu-Cu)_b}$ as defined in Figure S6, are chosen to represent the surface strain induced stabilization. The right wing of the inverted V-shape seems to correlate with the enhanced region of the d-band center distribution (half of the off-diagonal cases at the upper-right region), meaning the electronic effect resulted from the surface strain dominates the adsorption of *CO<sub>bridge</sub> and *OCCOH. The left wing of the inverted-V shape can be rationalized by the bonding nature of C-C and C(OH)-Cu bond in OCCOH. The C-C bond lengths of *OCCOH are predicted to be single bond character at 1.493Å on the (-6, 10) surface strain model, being reduced to 1.477Å without the presence of surface strain. With the assignment of C-C single bond in *OCCOH, the C(OH) fragment can be subsequently assigned as a singlet carbene moiety, in which no spin density is accumulated on the carbon atom of C(OH) as shown in the PDOS (Figure S7). This $\sigma$ donor of C(OH) fragment overlap better with the surface copper atoms the (-6,10) model in comparison with the (0,0) case as shown in Figure S7, where the $p$ band of C of C(OH) is shifted noticeably to the lower energy region. The $p$ band shifting also exists for the negative-charged

fragment C(=O) of *OCCOH interacting with the surface copper atoms. A suitable $r_{(Cu-Cu)_b}$ distance at 2.93Å observed in the (-6,10) model appears to facilitate such stronger interaction in respect to the (0,0) case as shown in Figure S6. The details of these five structural properties of (0,0) and (-6,10) models are also tabulated in Figure S6b. The heat map of the structural property change is shown in Figure S6c where rC-C of *OCCOH is sensitive to the change of both lattice vector $\vec{a}$ and $\vec{b}$. Additionally, the electron localization functions (ELF) of *OCCOH on (0,0) and (-6,10) models are compared Figure 2. The localized electron density can be straightforwardly identified to represent the C-C and C-Cu chemical bonds, being highlighted in pink dotted spheres. The red and orange area of C-C bond in the (-6,10) model is substantially greater than the (0,0) case, implying a suitable condition with compressed $\vec{a}$ and elongated $\vec{b}$ further stabilize the C-C bond formation.

![](./images/812742337917616128_3.jpg)

Figure 1. Relative binding energy $\Delta \mathrm{E}_{\text {bind }}^{\mathrm{X}}, \mathrm{X}=$ (a) $* \mathrm{CO}_{\text {atop }}$, (b) $* \mathrm{CHO}$, (c) $* \mathrm{COOH}$, (d) $* \mathrm{H}$, (e) $* \mathrm{CO}_{\text {bridge }}$ and (f) $* \mathrm{OCCOH}$, being represented in color scale (in eV), on the various strained $\mathrm{Cu}$ surfaces. The numerical notation $-(\mathrm{x}, \mathrm{y})$ of $\mathrm{x}$-axis and $\mathrm{y}$-axis denotes the strained percentage along the lattice vector direction $\vec{a}$ and $\vec{b}$ of $\mathrm{Cu}(100)$ surface. For example, $(-2,4)$ denotes the compression of $\vec{a}$ and elongation of $\vec{b}$ by 2 and $4 \%$, respectively. The white circle, square, star markers on the grids represent top-side, 4-fold hollow-side, and bridge-side adsorption on the non-displaced surfaces, respectively. Otherwise, black bold markers on the grids are used to denote that the copper surface becomes displaced, in which its relative binding energy also takes into

account the energy of bare-but-displaced surface. The magenta dot lines indicate the regions of adsorbate stabilization.

![](./images/812742337917616128_4.jpg)

Figure 2. Electron Localization Function (ELF) of *OCCOH on (0, 0) and (-6, 10) models. Cu, C, O and H atoms are depicted as orange, black, red and white spheres. The pink dotted-sphere denotes the interaction between the carbonyl fragment with the surface Cu atom.

## II. Strain effect to the selectivity

To explore the influence of surface strain to the selectivity, we have calculated the differences of the relative formation energies of four catalytic-competing intermediate in Figure 3. The negative value shown on the heat map represents the surface strain stabilizing the first intermediate (minuend) over the

second one (subtrahend). Contrarily, the positive value suggests the surface strain strengthens the bonding of the second intermediate.

In this section, we mainly compare four relevant couples of intermediate couples: (1) the CO₂/CO reduction reaction (CO2RR/CORR) competing with hydrogen evolution reaction (HER), (2) *CO occupancy on atop vs. bridge sites, (3) C1-species from *CO, and (4) C2 vs. C1 species formation. In Figure 3a, *CO₍bridge₎ is selectively enhanced from *H as shown by applying elongation strain along $\vec{b}$, such preference could promote *CO occupation on Cu surface and consequently hinder the HER channel. Experimental evidence has been revealed that *CO would lower the binding strength of *H and suppress the HER.²⁸ In Figure 3b, *CO₍bridge₎ is more stabilized than *CO₍atop₎ with the compression of $\vec{a}$, and the increase of *CO₍bridge₎ occupancy could leads to subsequent C2 species formation as being discussed later. In Figure 3c, the application of surface strain does not apparently promote the hydrogenation step of *CO to form *CHO where only pale and deep blue colors are observed. Since the heat map of *CO₍bridge₎ vs. *CO₍atop₎ is already orange, the map of *CHO vs. *CO₍bridge₎ would be even more blue. Thus, the potential-determined step of CO₂/CO reduction to C1-species formation²⁹ would be suppressed by the application of surface strain. In Figure 3d, *OCCOH and *CHO are compared, the 1ˢᵗ-hydrigenated C2-intermediate is substantially preferred by up to 0.15 eV within (Nₐ < -5, Nᵦ > 5) region, being highlighted by black rectangle. The C2-species formation channel could be selectively activated under a suitable surface strain over the C1-species formation channel.

![](./images/812742337917616128_5.jpg)

Figure 3. Relative $\Delta E_{form.}$ between (a) $CO_{bridge}$ and H ($\Delta E_{form.}^{*CO_b} - \Delta E_{form.}^{*H}$), (b) CHO and $CO_{atop}$ ($\Delta E_{form.}^{*CHO} - \Delta E_{form.}^{*CO}$), (c) $CO_{bridge}$ and $CO_{atop}$ ($\Delta E_{form.}^{*CO_b} - \Delta E_{form.}^{*CO_t}$), (d) OCCOH and CHO ($\Delta E_{form.}^{*OCCOH} - \Delta E_{form.}^{*CHO}$) on the strained surface models. The circle, square, star symbols represent top, 4-fold hollow, and bridge site adsorption, respectively. The $\Delta E_{form.}$ terms containing the use of displaced surfaces are denoted by black circle markers.

## II-(a) C2 reaction pathway

Two *CO coupling with each other into *OCCO is the rate-determining step in producing C2 products on copper; the corresponding activation energy is around 0.69 eV predicted from the constrain MD calculation published by Cheng et al.²⁵ As shown in Figures 3a-3d, a surface strain including compressed $\vec{a}$ and elongated $\vec{b}$ can stabilize the initial and final states in CO-CO coupling, i.e. *CO and *OCCOH. Therefore, we carry out a 3x4 4-layer Cu(100) model with explicit water solvation (32H₂O and 1 Na atom) for calculating the corresponding transition state under the surface strain as sown in Figure S8. The one extra Na solvated in the solution turns the work function of Cu(100) model into 3.36 eV,

which is corresponding to -0.62V vs. RHE ($3.36 - 4.40 + 0.0592 \times 7 = -0.62$V). This is consistent with the experimental observed value in the previous study for generating the highest selectivity toward ethylene at pH $7.^{12}$ The activation energies of CO-CO coupling were compared using 2 different strain models, (-6, 10) and (-10, 10) in respect to the non-strained pristine surface. The energies along the reaction pathway on two strain surface and pristine surface are shown in Figure 4a. All the activation energies in these three models are quite close to each other; only differing by at most -0.11 eV. Interestingly, the final state – *OCCO on (-6,10) model is noticeably more stable than the case of (-10,10) and (0,0) cases where *OCCO of (-6,10) model is 0.07 eV lower than the (0,0) counterpart. Such additional strain-induced stability could facilitate the subsequent protonation step to form *OCCOH. According to the aforementioned relative formation energies and activation energies, one can conclude that surface strain can enhance the C2 intermediate, *OCCO, forming on Cu (100), i.e. binding *CO stronger, stabilizing the *OCCO, and not substantially hamper the activation energy of CO-CO coupling, resulting in a higher selectivity toward C2 product generation.

## II-(b) C3 reaction pathway

There have been many studies reporting selectivity enhancement of $CO_2$RR or CORR toward C2 and C3 products in the literature, $^{15-16, 30}$ where CO-CO coupling has been consensually considered as the critical step of C-C bond formation. The surface morphology, particularly the basal plane of Cu, has also been found to play an important role to C-C bond formation via the first-principle simulations. $^{13}$ Consequently, it is straightforward to anticipate the necessity of unique Cu morphology in facilitating the second C-C bond formation for C3 product generation.

It is known that the rectangle and parallelogram four-Cu moieties are most suitable for C-C bond formation on Cu(100) and Cu(111) surfaces, respectively, $^{13}$ being highlighted by pink and orange dashed lines in Figures S9a-S9b. In this study, displaced surface morphology is also identified on several highly compressive models, e.g. the (-6,10) model listed on Figure S9c. This unique arrangement of surface atoms containing adjacent rectangles and parallelograms, conceptually integrating Cu(100) and Cu(111) characteristic together, is identified and the corresponding C-C bond formation barrier for C3 intermediate formation is investigated. We select *CCH and *CCOH as the C2 precursors to react with *CO for understanding the initial C3 formation reaction channel. The *CCH and *CCOH intermediates have been reported as the precursors leading to energy-demanding electrochemical steps ($\Delta G^{\ddagger} >$0.90 eV) along the Langmuir-Hinchelwood mechanism for ethylene generation;$^{25}$ these two intermediates can be

consequently selected as the possible precursors to carry out C3 formation. We also select *CO as the feedstock for C3 formation due to its energy-demanding hydrogenation step in forming *CHO.

In Figure 4d, the CO-CO coupling barrier on the displaced-surface (-10,10) model is calculated to be 0.57 eV; this activation energy is subtly affected by the surface strain and comparable to the non-strained case at 0.58 eV. Therefore, the C2 intermediates *OCCO/*OCCOH could possibly form on these displaced regions, being available for further hydrogenation steps. The "long-lived" *CCH and *CCOH coupling with *CO could be in presence on the displaced regions. We have calculated the corresponding C-C bond formation barrier using (-10, 0) and (-10, 10) models, as shown in Figures 4h and 4l, under the condition of explicit water solvation and applied voltage at -0.62V. The activation energies of *CCH coupling with *CO on (-10,0) and (-10,10) models are 0.45 eV and 0.51 eV to form *CCH(CO), and the corresponding reaction energies are 0.13 eV and 0.18 eV, respectively. Notably, these predicted C-C bond formation barriers for C3 reaction channel are comparable, even smaller, to that of C2 reaction channel while the calculated reaction energies are negligibly endothermic. For *CCOH coupling with *CO on (-10,0) and (-10,10) models are 0.63 and 0.53 eV to form *(OC)CCOH, and the corresponding reaction energies are exothermic at -0.01 and -0.19 eV, respectively. For both *CCH and *CCOH coupling with *CO, *CO is found to initially reside on the displaced copper atoms, and subsequently moves quasi-perpendicularly to the C-C bond of *CCH and *CCOH through the transition state structures shown on Figures 4f and 4j, respectively. The displaced surface morphology consisted of adjacent rectangles and parallelograms provides low activation energy channels and stabilize the C3 intermediates. Such potential catalytic property could contribute to future design in advanced electrocatalyst of $CO_2$RR/CORR toward to selective C3 production.

![](./images/812742337917616128_6.jpg)

Figure 4. Schematic representations of reaction coordinates and calculated activation energies for CO-CO coupling (a-d), *CCH and *CO coupling (e-h), and *CCOH and *CO coupling (i-l) processes on the various surface models. Cu, C, O, Na and H atoms are depicted as orange, grey, red, purple and white spheres, respectively. The standard deviations are labeled as the error bars.

## Conclusion

In this study, we have built 121 copper models under various surface strain conditions to investigate the interplay between the surface strain and the catalytic properties of intermediates along CO₂RR/CORR pathway. According to the current computational results, Cu(100) model with compressed $\vec{a}$ (5-8%) and elongated $\vec{b}$ (6-10%) axis should be able to generate a higher C2 over C1 product ratio in electrochemical CO₂RR/CORR in comparison with the pristine case. There are three reasons can contribute this higher C2 over C1 ratio: (1) the C2 intermediates – *OCCOH and *OCCO are

preferentially stabilized by the introduction of surface strain due to the strong adsorption resulted from the enhanced C-Cu and C-C orbital overlapping as shown by the aforementioned ELF and PDOS analysis; (2) the activation energy of CO-CO coupling is negligibly affected by surface strain predicted by the NEB calculations; (3) hydrogenation of *CO and HER are noticeably suppressed due to strained-induced $^*$CO$_{\text{bridge}}$ stabilization, subsequently increasing the energy cost of forming *CHO and excluding *H formation site.

Furthermore, the displaced surface morphology can be found under high compressing strain (> 8% in this study). These unique atomic arrangements integrate rectangle and parrallegram four-Cu moieties together and provide suitable binding sites for C2 intermediate coupling with *CO, resulting in feasible activation energies. We present two important steps of forming C3 intermediates initiated from *CCH and *CCOH coupling with *CO with the activation energies around 0.45 to 0.63 eV, highly comparable to the rate-determined step of C2 product generation. This adjacent rectangle and parallelogram arrangement could provide new insights for designing the advanced electrocatalysts for selective C3 products from CO$_2$RR/CORR.

### Conflicts of interest
There are no conflicts to declare.

### Acknowledgements
This study is supported by the Ministry of Science and Technology of Taiwan (107-2113-M-003-007 and 107-2811-M-003-528). The authors also thank the innovation-oriented trilateral research fund for young investigators of NTU system. The authors are grateful to the computational resources provided by National Center for High-Performance Computing of Taiwan and Center for Cloud Computing in National Taiwan Normal University.

### Notes and references
Department of Chemistry, National Taiwan Normal University, Taipei 11677, Taiwan.
E-mail: mktsai@ntnu.edu.tw
†Electronic Supplementary Information (ESI) available: various schematic representation of strain model, heat map of calculated intermediates, calculated electrostatic potential, density of state analysis, and comparison of current computational model with TEM image. See DOI: 10.1039/x0xx00000x

(1). T. R. Anderson, E. Hawkins and P. D. Jones, *Endeavour* 2016, 40, 178-187.

(2). B. Ekwurzel, J. Boneham, M. W. Dalton, R. Heede, R. J. Mera, M. R. Allen and P. C. Frumhoff, *Climatic Change* 2017, 144, 579-590.

(3). J. P. Gattuso, A. Magnan, R. Billé, W. W. L. Cheung, E. L. Howes, F. Joos, D. Allemand, L. Bopp, S. R. Cooley, C. M. Eakin, O. Hoegh-Guldberg, R. P. Kelly, H. O. Pörtner, A. D. Rogers, J. M. Baxter, D. Laffoley, D. Osborn, A. Rankovic, J. Rochette, U. R. Sumaila, S. Treyer, C. and C. Turley, *Science* 2015, 349, 4722.

(4). P. M. Visser, J. M. H. Verspagen, G. Sandrini, L. J. Stal, H. C. P. Matthijs, T. W. Davis, H. W. Paerl and J. Huisman, *Harmful Algae* 2016, 54, 145-159.

(5). J. A. Bassham, S. A. Barker, M. Calvin and U. C. Quarck, *Biochim. Biophy. Acta* 1956, 21, 376-377.

(6). Y.-T. Chan and M.-K. Tsai, *Phys. Chem. Chem. Phys.* 2017, 19, 29068-29076.

(7). S. Lin, C. S. Diercks, Y.-B. Zhang, N. Kornienko, E. M. Nichols, Y. Zhao, A. R. Paris, D. Kim, P. Yang, O. M. Yaghi and C. J. Chang, *Science* 2015, 349, 1208.

(8). J. Low, B. Cheng and J. Yu, *Appl. Surf. Sci.* 2017, 392, 658-686.

(9). W.-H. Wang, Y. Himeda, J. T. Muckerman, G. F. Manbeck and E. Fujita, *Chem. Rev.* 2015, 115, 12936-12973.

(10). Y. Hori, H. Wakebe, T. Tsukamoto and O. Koga, *Electrochim. Acta* 1994, 39, 1833-1839.

(11). Y. Hori, A. Murata and R. Takahashi, *J. Chem. Soc., Faraday Trans. 1* 1989, 85, 2309-2326.

(12). K. J. P. Schouten, E. Pérez Gallent and M. T. M. Koper, *J. Electroanal. Chem.* 2014, 716, 53-57.

(13). J. H. Montoya, C. Shi, K. Chan and J. K. Nørskov, *J. Phys. Chem. Lett.* 2015, 6, 2032-2037.

(14). E. Pérez-Gallent, M. C. Figueiredo, F. Calle-Vallejo and M. T. M. Koper, *Angew. Chem. Int. Ed.* 2017, 56, 3621-3624.

(15). C. W. Li, J. Ciston and M. W. Kanan, *Nature* 2014, 508, 504.

(16). X. Feng, K. Jiang, S. Fan and M. W. Kanan, *ACS Cent. Sci.* 2016, 2, 169-174.

(17). T. Cheng, H. Xiao and W. A. Goddard, *J. Am. Chem. Soc.* 2017, 139, 11642-11645.

(18). G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* 1996, 6, 15-50.

(19). G. Kresse and J. Hafner, *Phys. Rev. B* 1993, 47, 558-561.

(20). G. Kresse and J. Hafner, *Phys. Rev. B* 1994, 49, 14251-14269.

(21). P. E. Blöchl, *Phys. Rev. B* 1994, 50, 17953-17979.

(22). G. Kresse and D. Joubert, *Phys. Rev. B* 1999, 59, 1758-1775.

(23). J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.* 1996, 77, 3865-3868.

(24). H. Jonsson, G. Mills and K. W. Jacobsen, *World Scientific*: 1998; pp 385-404.

(25). T. Cheng, H. Xiao and W. A. Goddard, *Proc. Nat. Acad. Sci.* 2017, 114, 1795-1800.

(26). S. Plimpton, *J. Comp. Phys.* 1995, 117, 1-19.

(27). I.-S. Huang, M.-K. Tsai, *J. Phys. Chem. A* 2018, 122, 4654-4622.

(28). H. Ooka, M. C. Figueiredo and M. T. M. Koper, *Langmuir* 2017, 33, 9307-9313.

(29). A. A. Peterson, F. Abild-Pedersen, F. Studt, J. Rossmeisl and J. K. Nørskov, *Energy Environ. Sci.* 2010, 3, 1311-1315.

(30). E. L. Clark, C. Hahn, T. F. Jaramillo and A. T. Bell, *J. Am. Chem. Soc.* 2017, 139, 15848-15857.