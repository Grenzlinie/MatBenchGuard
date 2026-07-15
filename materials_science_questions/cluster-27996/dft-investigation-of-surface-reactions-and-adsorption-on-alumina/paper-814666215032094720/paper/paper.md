# Dynamic Locking of Interfacial Side Reaction Sites Promotes Aluminum-Air Batteries Close to Theoretical Capacity

Yuanlin Huang, Lei Fang, Yu Gu, Pingshi Wang, Hao Yan, Yanjie Wang, Zexing Cao,* Zhaowu Tian, Bingwei Mao, and Li Zhang*

Aluminum metal has been regarded as a promising anode material for aqueous metal-air batteries. However, the stable cycling of Al anodes is challenging due to the severe parasitic corrosion of Al metal in alkaline electrolytes. Here, a novel additive, *n*-octylphosphonic acid (OPA), is introduced into the typical NaOH electrolyte system to improve the interfacial stability of Al anodes and thus promote high-performance Al-air batteries (AABs). Combining several experimental characterizations and theoretical calculation, it is proved that OPA molecules in an NaOH aqueous environment can modify the Al anode/electrolyte interface and alter the stacking of the discharge product. The electrolyte engineering is capable of anchoring dynamically to restrain side reactions through hydrogen bonds (H···O), homogenizing the dissolution of Al metal and avoiding precipitation agglomeration. As a proof of concept, AABs full cells with an electrolyte containing OPA achieve higher potential plateau and discharge capacity than those with a pure NaOH electrolyte. It paves a way to develop highly efficient and eco-friendly electrolyte additive strategies for high-performance AABs devices and advance the current understanding of organic additive mechanisms in AABs.

## 1. Introduction

As global energy demand grows, novel energy storage and conversion systems are desired to develop to reduce the use of fossil fuels that exacerbate the greenhouse effect. As an alternative, metal-air batteries (MABs, M = Al, Li, Zn, Mg, etc.) are highlighted owing to their sufficient specific gravimetric capacities of metal anodes and inexhaustible oxygen cathode materials taken directly from atmosphere.[1–3] Among these MABs, Al-air batteries (AABs) have attracted much attention due to the high safety,[4] and abundance,[5] and recyclability of Al.[6,7] More encouragingly, AABs approach a remarkable theoretical volumetric energy density of 21870 Wh L⁻¹,[8] far exceeding the counterpart of gasoline (9700 Wh L⁻¹).[9]

AABs prefer working in alkaline electrolyte because of higher working potential plateau and discharge capacity.[10–12] Ideally, the Al anode reacts with hydroxyl ions to form aluminate while releasing electrons into the external circuit during discharge (Equation (1)).[13,14] But in fact, Al undergoes severe self-corrosion reaction with H₂O (Equation (5)),[13–15] where different areas of Al anode act as both cathodic (hydrogen evolution) and anodic sites (Al oxidation) but without generating electrons to the external circuit. Apparently, the parasitic side reaction with H₂O significantly reduces the utilization, working potential plateau and discharge duration of Al anodes.[16,17]

$$
egin{align}
	\text{Anode}:\mathrm{Al}+4\mathrm{OH}^{-}&\to\left[\mathrm{Al}(\mathrm{OH})_{4}\right]^{-}+3\mathrm{e}^{-}\label{eq1}\
	E^{0}&=-2.35\ \mathrm{V\ versus\ SHE}\
	\left[\mathrm{Al}(\mathrm{OH})_{4}\right]^{-}&\to\mathrm{Al}(\mathrm{OH})_{3}(\mathrm{s})+\mathrm{OH}^{-}\label{eq2}\
	\text{Cathode}:\mathrm{O}_{2}+2\mathrm{H}_{2}\mathrm{O}+4\mathrm{e}^{-}&\to4\mathrm{OH}^{-}\ E^{0}=0.40\ \mathrm{V\ versus\ SHE}\label{eq3}\
	\text{Overall}:4\mathrm{Al}+3\mathrm{O}_{2}+6\mathrm{H}_{2}\mathrm{O}&\to4\mathrm{Al}(\mathrm{OH})_{3}\label{eq4}\
	E^{0}&=2.75\ \mathrm{V\ versus\ SHE}\
	\text{Side reaction}:6\mathrm{Al}+6\mathrm{H}_{2}\mathrm{O}&=2\mathrm{Al}(\mathrm{OH})_{3}+3\mathrm{H}_{2}\uparrow\label{eq5}
\end{align}
$$

Reasonable suppression of the self-corrosion reaction with H₂O, while ensuring adequate reactive sites with OH⁻ is the basic strategy to promote Al anodes to deliver the highest possible discharge capacity. Various inhibition methods, such as, alloying Al with metals with higher hydrogen evolution overpotentials,[18–23] adopting high concentration electrolytes, non-aqueous electrolytes, or gel electrolytes,[5,24–32] and adding corrosion inhibitors,[33] have been proposed to suppress the hydrogen generation and minimize the direct contact between Al and H₂O. Among them, the introduction of inhibitors is recognized as the most simple, convenient, and economical solution to engineer the Al/electrolyte interface. The common

Y. Huang, L. Fang, Y. Gu, P. Wang, H. Yan, Y. Wang, Z. Cao, Z. Tian, B. Mao, L. Zhang
State Key Laboratory of Physical Chemistry of Solid Surfaces
Department of Chemistry
College of Chemistry and Chemical Engineering
Collaborative Innovation Centre of Chemistry for Energy Materials (iChEM)
Tan Kah Kee Innovation Laboratory
Xiamen University
Xiamen, Fujian 361005, China
E-mail: zxcao@xmu.edu.cn; zhangli81@suda.edu.cn

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adsu.202100420.

DOI: 10.1002/adsu.202100420

inhibitors can be divided into three categories: Inorganic inhibitors ($\mathrm{Na_2SnO_3}$, $\mathrm{ZnO}$, $\mathrm{In(OH)_3}$, Silica ($\mathrm{SiO_2}$), etc.),$^{[34-38]}$ organic inhibitors (e.g., polypyrrole, thiourea, amino acids, nonoxynol-9), and hybrid inhibitors (e.g., alkyl polyglucoside/ $\mathrm{K_2SnO_3}$, butantetraol/dithiothreitol).$^{[33,39-41]}$ Generally, inor- ganic additives help achieve in situ deposition of metallic passi- vation layers (e.g., Zn, Sn) that increase the hydrogen evolution overpotential.$^{[42-44]}$ By contrast, organic inhibitors comprising electro-negative groups (O, S, N, and P) can adsorb and form a highly-ordered hydrophobic layer on the Al surface, thus greatly reducing the direct contact between $\mathrm{Al}$ and $\mathrm{H_2O}$ molecules.$^{[39]}$

Unlike conventional electrodes, the reaction interface of Al anodes is dynamically altered during discharge. In other words, the passivation or adsorption layer, whether inorganic or organic, would gradually detach and fall off with the consump- tion of Al. More importantly, the Al anode interface will soon convert to form the intermediate product interface before dis- integrating. In this sense, the interaction between the interme- diate products and inhibitors is even more critical to discharge performance of AABs than that between $\mathrm{Al}$ and inhibitors. However, there is still lack if research yet on interface chemistry between inhibitors and dynamically changing Al anode, and on this basis to explore novel inhibitors to significantly boost the discharge capacity of AABs.

Herein, a novel organic inhibitor, $n$-octylphosphonic acid (Figure 1a, denoted as OPA), is used to greatly suppress the self-corrosion of Al electrodes for the first time and to promote AABs to reach capacity close to their theoretical value. Unlike conventional organic inhibitors, OPA not only quickly adsorbs on the Al anode surface (Scheme 1a) and results in a uniform and compact hydrophobic layer (Scheme 1b), but also binds steadily with subsequent $\mathrm{Al(OH)_3}$ intermediate products via strong hydrogen bonds (Scheme 1c). More importantly, once the intermediate product falls off and fresh Al metal re-exposes, the discrete OPA molecules can immediately absorb on the Al surface and again form a new passivation layer (Scheme 1d,e). Apparently, OPA is capable of maintaining a stable yet dynam- ical bond to the changing Al anodes, thus greatly suppressing the self-corrosion reaction between $\mathrm{Al}$ and $\mathrm{H_2O}$. As such, the assembled AAB full cell with trace amount of OPA (4 м NaOH-1 мм OPA electrolyte) shows an exceptionally high dis- charge capacity of $2353\ \mathrm{mAh\ g^{-1}}$ at $20\ \mathrm{mA\ cm^{-2}}$, while demon- strating a high Al utilization up to 79%. Moreover, AABs using OPA and $\mathrm{Na_2SnO_3}$ hybrid inhibitors can further deliver an ultrahigh discharge capacity of $2694\ \mathrm{mAh\ g^{-1}}$, 91% of their theo- retical capacity ($2980\ \mathrm{mAh\ g^{-1}}$). A practically useful 5.2 V AAB pile is specially designed to drive a commercial digital camera. This work opens up a new avenue to boost the discharge per- formance of AABs via enhancing the interaction between inhib- itors and dynamically changing Al interfaces.

## 2. Results and Discussion
### 2.1. Theoretical Simulations of $n$-Octylphosphonic Acid Anchoring Mechanism on Al Anode Surface
Figure S1, Supporting Information, shows the highest occu- pied molecular orbital (HOMO) and the lowest unoccupied molecular orbital (LUMO), as well as, the electrostatic poten- tials (ESP) of deprotonated OPA. Obviously, both HOMO and LUMO are mainly contributed by the $\mathrm{PO_3}$ moiety, indicating that the phosphate group may not only easily donate electrons, but also form the back-donation bond with the metal surface. The ESP distribution in Figure S1c, Supporting Information, suggests that the highly negatively charged $\mathrm{PO_3}$ moiety may have relatively strong bonding with the electron-deficient $\mathrm{Al}$ through donation and back-donation interactions. As expected,

![](./images/814666215032094720_1.jpg)

Figure 1. a) Molecular structure of $n$-octylphosphonic acid (OPA). The optimal adsorption configurations of OPA on b) Al (022) surface calculated by DFT calculations and c) $\mathrm{Al(OH)_3}$ (001) surface calculated by QM/MM calculations. d) Concentration profiles for $\mathrm{H_2O}$ and $\mathrm{OH^-}$ distributions on the $\mathrm{Al(OH)_3}$ surface as a function of surface height for the systems with different numbers of OPA molecules.

![](./images/814666215032094720_2.jpg)

Scheme 1. Schematic illustration of protective mechanism of OPA on Al anodes.

OPA is predicted to be chemically adsorbed on the Al (022) surface, where two O atoms of $PO_3$ form chemical bonds with two Al atoms, respectively, shown in Figure 1b. Besides, we further performed 5 ps Ab initio molecular dynamics simulations and got the same result, as shown in Figure S1d, Supporting Information. Similar chemisorption configurations have also been reported in previous studies.[45-47]

To have an insight into OPA adsorption on the $Al(OH)_3$ surface, a 5 ns MD simulation has been carried out first. Figure S2, Supporting Information, depicts the final adsorption configurations with one, four and eight OPA molecules on the $Al(OH)_3$ (001) surface after MD simulations for 5 ns. Different from the Al surface, OPAs form hydrogen bonds with the $Al(OH)_3$ surface. In addition, the alkyl chains of OPAs tend to aggregate to form a protective layer.

Quantum-mechanics/molecular-mechanics (QM/MM) calculations further verify the hydrogen bond interactions between OPA and $Al(OH)_3$. The QM/MM-optimized configuration of OPA on the $Al(OH)_3$ surface is depicted in Figure 1c, in which there are hydrogen bonding interactions among an O atom of OPA and three OH groups of $Al(OH)_3$ with the O···HO distance of $2.07$ Å.

Figure 1d shows the concentration profile of NaOH aqueous solution on the $Al(OH)_3$ surface as a function of surface height for the systems with different numbers of OPA molecules. Note that the highest peaks of the concentration distribution almost appear at the same surface distance of about $11$ Å, and at this interface region, $H_2O$ or $OH^-$ can form hydrogen bond with $Al(OH)_3$. Therefore, OPA molecules compete with $H_2O$ or $OH^-$ in adsorption on $Al(OH)_3$. With the increase of OPA molecules at the interface, the number of adsorbed $H_2O$ and $OH^-$ on the surface of $Al(OH)_3$ decrease, as shown in Figure 1d. Presumably, in high concentrations, the surface $Al(OH)_3$ layer may cover by OPA molecules, which prevents $H_2O$ or $OH^-$ from interacting with $Al(OH)_3$ and the further self-corrosion of Al can be inhibited.

### 2.2. The Inhibitory Effect of n-Octylphosphonic Acid on the Side Reaction between Al and $H_2O$

As Figure 2a demonstrates, the contact angle of electrolyte droplet on the Al foil surface significantly increases from $33.3^\circ$to $80.2^\circ$after adding 1 mm OPA into 4 M NaOH electrolyte. This change in the interface from hydrophilic to hydrophobic can be ascribed to the adsorption and arrangement of $R-PO_3^{2-}$ in OPA molecules on the Al surface, whereas the hydrophobic end (alkyl chain tail) points to the electrolyte. Apparently, this greatly weakens the wettability of Al electrode and is beneficial to prevent water from contacting with Al substrate. Moreover, OPA molecules play a leading role in the competitive adsorption between corrosive media ($H_2O$) and OPA molecules with the existence of OPA in NaOH electrolyte, which benefits from the strong interaction between OPA molecules and hydroxyl group on the surface of Al mentioned in detail in the later part, as proved in Figure 2d. In order to quantitatively evaluate the inhibitory effect of OPA on the side reaction between Al and $H_2O$, a drainage-weighing setup was specially designed to measure the volume of hydrogen by-products of Al foils in the NaOH solutions with various amounts of OPA (the inset in Figure 2b). As displayed in Figure 2c and Table S1, Supporting Information, the amount of generated $H_2$ decreased drastically when the lower concentration of OPA (0.5 mm) is introduced, and does not change markedly as the OPA concentration increases further (1-4 mm). This clearly manifests that OPA is the way to inhibit the self-corrosion reaction by

![](./images/814666215032094720_3.jpg)

Figure 2. Hydrogen evolution inhibition effect of OPA: a) Contact angle images of solutions on Al surface. b) Photographs describing the phenomenon of Al immersed in the solutions for 5 min and Al surface after immersed in solutions for 2 h (the bottom part). c) Hydrogen volume of Al immersed in solutions for 1 h. d,e) Tafel plots of Al anodes in different electrolytes. f) Polarization parameters of Al anodes in different electrolytes.

forming a self-limited ultra-thin film on the Al surface. Digital photographs of Al foils soaked in the electrolytes with different OPA dosages again indicate that OPA can greatly suppress the self-corrosion of Al after the concentration reaches 0.5 mM (Figure 2c). However, once the concentration is higher than 2 mm, a large amount of hydrogen is bound on the surface of the Al foil, which reduces the density of Al foil and is very easy to float on the liquid surface. Therefore, choosing an appropriate additive concentration is very important.

To further evaluate the inhibitory effect of OPA on the side reaction of Al anodes from a thermodynamic perspective, the potential dynamic polarization curves of Al foils in the bare NaOH and NaOH solutions with different OPA amounts were studied in detail through a three-electrode cells (Figure 2d-f). Note that all polarization curves consist of cathodic and anodic branches, representing hydrogen evolution and Al oxidation, $^{[48]}$ respectively. The junction of two branches is designated as the self-corrosion potential $(E_{corr})$ and is generally considered to be closely related to the synergy of two half reactions (Figure S3, Supporting Information). As Figure 2d,e manifest, $E_{corr}$ experiences a trend of rapid negative shift followed by slight positive shift with the increase of OPA concentration, and a minimal value (-1.634 V) appears at the 1 mm OPA addition (Figure 2f and Table S2, Supporting Information). As discussed above, OPA is capable of forming a self-limited thin film on the Al surface, thus largely increasing the $H_{2}$ evolution overpotential and promoting the negative shift of $E_{corr}$ (Figure S4, Supporting Information). But in turn, when the OPA dosage exceeds a certain value (e.g., 1 mM in this work), the formed OPA passivation layer may restrict the Al oxidation to some extent and drive the slight positive shift of $E_{corr}$ (Figure S5, Supporting Information). Meanwhile, the corrosion current density $(j_{corr})$ calculated from Butler-Volmer model exhibits a similar trend of variation, with a minimum value of $18.96 mA cm^{-2}$ at 1 mM OPA. Under the synergy of $E_{corr}$ and $j_{corr}$, the corrosion inhibition efficiency $(\eta)$ of the Al anode also presents a maximum value of $63.5\%$ at 1 mM OPA (Table S2, Supporting Information). The effect of addition of OPA on inhibiting hydrogen evolution can be further demonstrated by the linear sweep voltammetry (LSV) analysis. As Figure S6, Supporting Information, manifests, the hydrogen evolution current density decreases significantly from -0.145 A $cm^{-2}$ (blank) to -0.0811 A $cm^{-2}$ (1 mM OPA) at -1.6 V versus Hg/HgO. Given the above, OPA molecules can effectively suppress the side reactions between Al metal and $H_{2}O$ (i.e., $H_{2}$ evolution) through forming a self-limited thin passivation layer on the Al anode surface, and the optimum concentration of OPA determined experimentally is $\approx 1$ mM.

### 2.3. Experimental Validation of the Strong Al-Al(OH)₃-n-Octylphosphonic Acid Interface

#### 2.3.1. n-Octylphosphonic Acid Promotes Interface Stability of Al Anodes

Figure S7, Supporting Information, and Figure 3 show the scanning electron microscopy (SEM) images of the surface morphology of pure Al foils and Al foils immersed in 4 M NaOH solution with and without 1 mM OPA for 2 h, respectively. As displayed in Figure 3a,b, the Al foil presents a very rough and porous surface after immersion in the bare alkaline solution, with a large number of irregular cracks. This may cause active Al to fall off, resulting in loss of discharge capacity. $^{[24]}$ In contrast, the Al foil immersed in 4 M NaOH-1 mM OPA shows

![](./images/814666215032094720_4.jpg)

Figure 3. SEM and EDS images of Al surface after 2 h exposure in solutions: a,b) 4 м NaOH, c,d) 4 м NaOH -1 мм OPA. e,f) EDS images of Al anode surface immersed in 4 м NaOH -1 мм OPA.

a significantly smoother morphology (Figure 3c,d), which can undoubtedly be attributed to the uniform coverage of OPA passivation layer and the resulting suppressed self-corrosion reaction of Al. Energy dispersive spectrometer (EDS) is used to characterize the composition of OPA-modified Al surface (Figure 3e,f). The visible and uniform phosphorus signal in Figure 3f clearly confirms the uniform coverage of OPA thin film on the Al surface.

### 2.3.2. In-Depth Spectroscopic Characterization of the Al-Al(OH)₃-n-Octylphosphonic Acid Interface

To gain insight into the structural and chemical composition of the OPA protective film, the depth-dependent X-ray photoelectron spectroscopy (XPS) analysis of Al foil surface after immersion in NaOH-OPA solution is conducted (Figure 4a,b and Figure S7a,b, Supporting Information). As presented in Figure 4a, the peak of $P_{3/2}$ located at 131.6 eV and $P_{1/2}$ peak located at 132.6 eV confirm the presence of phosphorous in outer regions of protective film, whereas these peaks do not show up in Al sample soaked with bare NaOH solution (Figure S8b, Supporting Information). This is consistent with the EDS analysis shown in Figure 2e,f. Besides, other XPS spectra (Figure 4b) confirm OPA presents in the outer region for the protective film, and discharge product $Al(OH)_3$ is encapsulated in inner region. Therefore, the distribution of OPA in the outer layer greatly increases the stability of dynamic interface of Al by the interaction between intermediate and OPA in the AAB system. Consequently, there is a strong hydrogen bond between OPA and Al-OH, forming an $Al-Al(OH)_3$-OPA protective film, which hinders the formation of the product $Al(OH)_3$, and then achieves a protective effect. Furthermore, this XPS spectra also imply the formation of a OPA layer structured film with a thickness of $\approx$30 nm based on the sputtering depth of 6 nm each time. More importantly, in comparison with the P 2p spectrum of pure OPA powder (133.7 eV) (Figure S8a, Supporting Information), the binding energy of OPA (132.5 eV) (Figure 4a) on the Al foil immersed in NaOH-OPA solution is much lower, indicating that the electron cloud density around OPA molecules is higher than pure powder,$^{[49,50]}$ which is due to the association of OPA and $Al(OH)_3$. In addition, the XPS spectra of Al 2p also prove that OPA is extremely sensitive to the production of $Al(OH)_3$ (as shown in Figure S8c,d,

![](./images/814666215032094720_5.jpg)

![](./images/814666215032094720_6.jpg)

![](./images/814666215032094720_7.jpg)

![](./images/814666215032094720_8.jpg)

![](./images/814666215032094720_9.jpg)

![](./images/814666215032094720_10.jpg)

![](./images/814666215032094720_11.jpg)

![](./images/814666215032094720_12.jpg)

![](./images/814666215032094720_13.jpg)

Figure 4. Various characterizations for Al surface after immersed in different electrolyte system: a,b) P 2p XPS spectra of the sample in 4 m NaOH−1 mM OPA solution. c) XRD spectra. d,e) IR spectra. f) O 1s XPS spectra of the sample in pure NaOH solution. g) O 1s XPS spectra of the sample in solution with OPA. h) Nyquist plots of Al anode in different solutions. i) $R_{ct}$ of different solution.

Supporting Information). Clearly, such a structure is proved to play important roles in enhancing interfacial hydrophobicity and stability, thus improving Al anode against the side reaction.

X-ray diffraction (XRD) and Fourier transform infrared spectroscopy (FT-IR) analysis was further performed to investigate the interaction between OPA and $Al(OH)_3$ (Figure 4c−e). XRD patterns of Al foils after immersed in NaOH electrolytes with various amounts of OPA are given in Figure 4c. Except for characteristic diffraction peaks from Al (PDF no.89-4037) substrates, obvious peaks of $Al_2O_3$ (PDF no.47-1770) and $Al(OH)_3$ (PDF no.20-0011) are observed in all samples, indicating that OPA might not change the product structure. In the comparison of diffraction patterns, it is evident that the intense of the diffraction peak at $2\theta = 18.9^\circ$ of $Al(OH)_3$ (001) surface gradually decreases as the additive concentration increases, implying the decrease in the thickness of each independently crystallized $Al(OH)_3$ grain, and the peak at around $2\theta = 20.5^\circ$ refers to $Al(OH)_3$ (110) crystal plane relative increases, revealing that the width of each independently crystallized $Al(OH)_3$ grain increases.$^{[51-53]}$ Both differences can be attributed to OPA adsorbing on $Al(OH)_3$ (001) surface, thus the product in OPA electrolyte is thinner and wider than prepared in the normal electrolyte. As demonstrated in Figure 3, SEM images confirm the differences of morphology between two kinds of product. FT-IR studies further illustrate that there is a strong interacting behavior between OPA with $Al(OH)_3$ (Figure 4d,e). The peak at 3660, 3552, and $3468\ cm^{-1}$ corresponds to the O−H stretching$^{[54]}$ in $Al(OH)_3$ and the some weak peaks at $500-1000\ cm^{-1}$ corresponds to the Al−O banding$^{[55]}$ (such as, $Al_2O_3$). After the introduction of the OPA molecule into electrolytes, the stretching vibration of $-O-H$ in $Al(OH)_3$ shifts from $3468\ cm^{-1}$ (blank) to $3458\ cm^{-1}$ (4 mM OPA), $-P=O$ changes

from $1686\ \text{cm}^{-1}$ (0.5 mM OPA) to $1638\ \text{cm}^{-1}$ (4 mM OPA), and $-\text{P}-\text{O}$ shifts from $2652\ \text{cm}^{-1}$ (1 mM OPA) to $2638\ \text{cm}^{-1}$ (4 mM OPA) as the concentration of the corrosion inhibitor increases (Figure 4d,e), which indicates a strong hydrogen bond between $\text{Al(OH)}_3$ on the surface with OPA through the phosphonic acid group, equalizing the electron cloud density and shifting the stretching vibration frequency to a lower wave number. Additionally, the sample in the electrolyte containing 0.5 mM OPA additives has weaker absorption intensity of some characteristic peaks due to the incomplete coverage. Consequently, it can be inferred that OPA is likely to absorb on $\text{Al(OH)}_3$ (001) facet, which becomes the anchoring point for OPA by hydrogen bonding to inhibit the self-corrosion. This is a kind of "a special protective film," combing with the product.

To obtain more information regarding the interaction mode of OPA with $\text{Al(OH)}_3$, XPS is used again to further investigate their interaction. Indeed, there have been some reports correlating XPS data with OPA's surface binding mode (mono- and bidentate binding mechanisms),$^{[56]}$ which can be distinguished by the O 1s spectra. Nevertheless, as presented in Figure 4f,g, it is clear to find that Al foil in bare NaOH electrolyte displays obvious peaks (531.8 eV, 531.6 eV) corresponding to the $\text{OH}^-$ and the oxidized Al species, which confirms the composition of deposited coating is $\text{Al(OH)}_3$ and $\text{Al}_2\text{O}_3$, consistent with XRD. In comparison, the protective filmed in electrolyte with OPA shows two more O 1s XPS signals at 532.0 and 531.3 eV, corresponding to $\text{P}-\text{O}$ and $\text{P}=\text{O}$, respectively, which points at a strong indication for a bidentate binding mode, consistent with the theoretical results. In addition, the chemisorption behavior of Al and OPA can also be confirmed by Langmuir isotherm fitting (as shown in Figure S17 and Table S11, Supporting Information).

To further explore the suppressing mechanism of additive during the discharge process, electrochemical impedance spectroscopy (EIS) and Raman spectra are executed to study the corrosion behavior of the sample and adsorption process of OPA, respectively. As demonstrated in Figure 4h, the Nyquist plot of Al anodes in different electrolytes are fitted with the equivalent circuit (the inset in Figure 4h), which illustrate an inductive loop from parasitic corrosion in the high frequency, and a capacitive loop from the relaxation process of electric double layer and charge transfer resistance of Al anode in the middle and low frequency. $L$ stands for the inductive reactance produced by HER and $C$ stands for the capacitance.$^{[57]}$ Besides, the solution resistance and the charge transfer resistance are represented by $R_{\text{s}}$ and $R_{\text{ct}}$,$^{[58]}$ respectively. Clearly, the diameter of semi-circle (Figure 4h) and the value of $R_{\text{ct}}$ (Figure 4i) increase to the maximal in 1 mM OPA, which could be ascribed to this double-layer structure protective film. Comparing with pure NaOH electrolyte, the value of impedance in the cell with introducing a small amount of OPA increases, demonstrating much enhanced stability for Al anode. While once introduced to excess OPA, the cell exhibits an obvious reduction of $R_{\text{ct}}$ in comparison to the one with 1 mM OPA, which can be attribute to that the protective film obstructs the contact of $\text{OH}^-$ with Al metal, weakening the interaction between the discharge species and OPA, even though it has a good repulsive effect on $\text{H}_2\text{O}$. All these results support that in the optimum concentration (1 mM), the most stable protective film has formed so that $\text{H}_2\text{O}$ is difficult to reach Al metal.

Thus, the dynamic adsorption of OPA is further monitored by ex situ Raman spectroscopy and Al anodes discharging different time. As present in Figure S9, Supporting Information, the relative intensity between the peaks near the located at $2850-2980\ \text{cm}^{-1}$ ascribed to $\text{C}-\text{H}$ stretching from OPA molecules and $3450-3700\ \text{cm}^{-1}$ ascribed to $-\text{O}-\text{H}$ stretching from $\text{Al(OH)}_3$ reverses as the discharge time increasing, implying that OPA can quickly adsorb on the surface of Al anode and then the outer region of "the special protective layer" is formed.

### 2.4. Effect of n-Octylphosphonic Acid on the Discharge Process and Products in Al-Air Batteries

In order to evaluate the impact of OPA on the composition and morphology of the product during discharge, AABs with a small amount (0.5 mL) of 4 M NaOH (with or without OPA) electrolyte are assembled. The schematics and physical photo of configuration of AAB are presented in Figure 5a and Figure S10, Supporting Information, respectively. The discharge products of AABs are investigated by a combination of XRD, SEM, and Raman. As Figure 5b demonstrates, after discharging for 3.5 h at $10\ \text{mA}\ \text{cm}^{-2}$, the Al anode in the bare NaOH electrolyte is consumed completely and the electrolyte has dried up, leaving behind a large number of white aggregations. By contrast, the addition of OPA results in a very smooth product interface, while the electrolyte remains fluid (Figure 5c). The exact composition and morphology are further characterized via XRD, SEM, and Raman analysis, as presented in Figure 5d-i. Distinct diffraction peaks at around $2\theta=18.9^\circ$ and $20.5^\circ$ for the product $\text{Al(OH)}_3$ (PDF no.89-4037) are observed in the discharge products obtained in the NaOH electrolyte with and without OPA, indicating that OPA does not affect the main component of the discharge product (Figure 5d).

Similarly, the discharge product in the bare NaOH solution demonstrates nearly the same Raman peaks as that of products obtained in the electrolyte containing OPA (Figure 5e). SEM images of them are further presented to analysis the morphology. As shown in Figure 5f,g, the microspheres-like products, in pure NaOH, one exhibits a significant agglomeration phenomenon. While, under the NaOH-OPA electrolyte, the discharge product precipitates in the form of plates (Figure 5h,i), which could be related to the adsorption of OPA on $\text{Al(OH)}_3$ (001) surface. This is consistent with the previous conclusion.

Furthermore, another possible reason for changing the accumulation mode of precipitation can be attributed to electrostatic interaction between $\text{Al(OH)}_3$ and free OPA molecules in solution. Owing to the adsorption of $\text{OH}^-$, the surface of $\text{Al(OH)}_3$ formed in the 4 M NaOH solution is negatively charged.$^{[59]}$ The free OPA in the electrolyte exists in the form of $\text{R-PO}_3^{2-}$, with a negative charge, which restricts the agglomeration behavior on flake $\text{Al(OH)}_3$. It is believed that the flake deposits is very helpful for prolonging the discharge time, not easy to block the transmission of $\text{OH}^-$, which is conducive to the continuous progress of the discharge process. Considering OPA's unique advantages in product morphology regulation and antiaggregation, it will certainly play a decisive role in improving the overall discharge performance.

---
Adv. Sustainable Syst. 2022, 6, 2100420
2100420 (7 of 12)
© 2021 Wiley-VCH GmbH

![](./images/814666215032094720_14.jpg)

Figure 5. Effect of OPA on the discharge product: a) Schematic diagram of AABs battery device. Photograph of battery after discharging with b) 4 M NaOH. c) 4 M NaOH-1 mM OPA. d) XRD of the discharge product. g) Raman spectrum of the product and pure Al(OH)₃. SEM micrographs at different resolution of products after 3.5 h discharge in different solutions of e,f) blank, h,i) 1 mM OPA.

In brief, on the basis of previously described analyses, a probable side-reaction inhibition mechanism of OPA as an electrolyte additive can be sketched out. As schematically shown in Scheme 1, during the discharging process, polar hydrophilic groups-phosphonic acid groups act as the adsorption center of OPA molecules on Al metal to create the protective hydrophobic layers with the nonpolar alkane chain, which can further restrict the formation and shedding of dissolved Al(OH)₃ at the interface by OPA additive strongly bonds to intermediate through the phosphonic acid functional group via hydrogen bonds (O···H), eventually leading to form a double-layered structure protective film (Al-Al(OH)₃-OPA). However, it is worth noting that the inner region is actually composed of Al(OH)₃ and the oxidized Al species, but it is mainly rich content of Al(OH)₃, thus represented as Al(OH)₃.The intermediates are used flexibly to stabilize the dynamic surface by the presence of the OPA additive, greatly improving the anti-corrosion ability of Al anodes. Once sufficient hydrogen is generated, the protective film on the surface will fall off which can be reshaped with the rapid adsorption of OPA molecules via electric drive. Furthermore, the electrostatic interaction between free OPA and the discharge products makes the deposits precipitate in the form of flakes, effectively advoiding precipitation reunions which alleviates the deposition blocking the pores and prolongs the discharge time.

### 2.5. Long-Endurance n-Octylphosphonic Acid-Based Al-Air Batteries and Actually Available Battery Pack

The excellent function of OPA additive in suppressing parasitic corrosion of Al has been verified by experimental evidence and

theoretical simulations. Next, various electrochemical analyses are further performed to study whether the addition of OPA can truly suppress the self-corrosion of Al anodes. First, the open circuit potential (OCP) measurements of Al anodes in 4 M NaOH electrolyte with different concentrations of OPA are conducted in a three-electrode configuration. It is evident that the polarization voltages exhibit a trend of rapid negative shift followed by slight positive shift with the additive concentration increase (as shown in Figure S11, Supporting Information). It should arise from the competitive adsorption between OPA and $H_2O$ on the electrode surface, which forms a screening layer against Al dissolution and self-corrosion. Galvanostatic discharge experiments with different electrolytes in a two-electrode configuration at a current density of $20~mA~cm^{-2}$ further prove that the surface adsorption of OPA improves and stabilizes voltage plateau, decreasing the anode polarization, as illustrated in Figure 6a.

Especially, for the electrolyte with 1 mm OPA, AAB shows ultra-high OCP (1.7 V, Figure S10, Supporting Information), the highest voltage plateau (1.45 V) and a specific capacity of $2353~mAh~g^{-1}$, which improves the utilization of Al (Equation (9)) from 53% (Pure NaOH) to 79%. It is clear that with a small amount of OPA in NaOH electrolyte, the overall performance of AABs exhibits effective enhancement in performance compared with pure NaOH electrolyte, indicating the introduction of electrolyte additive can effectively enhance the stability of the Al electrode and inhibit the side-reactions. While, for the electrolyte with over 1 mm OPA, although the shielding layer well constraining HER, it occupies adequate reactive sites with $OH^-$ at higher additive concentrations. Based on it, the formation of hydrogen bonding between OPA and the interface intermediate could be restricted, thus weakening the ability of the double-structured protective film to suppress the self-corrosion

![](./images/814666215032094720_15.jpg)

Figure 6. Electrochemical performance of AABs: a) Discharge curves of AABs with different electrolytes at $20~mA~cm^{-2}$. b) Galvanostatic discharge curves of AABs with 4 M NaOH-1 mM OPA electrolytes at different current density. c) Galvanostatic discharge curves of AABs with different electrolytes at $10~mA~cm^{-2}$. d) Specific capacity, current density, and open-circuit voltage of AAB with OPA compared with previously reported strategies. e,f) OCP and photographs of a commercial digital camera powered by AABs pies connected in series.

of Al. Furthermore, LSV is conducted to calculate power density of AABs (Figure S12, Supporting Information). Clearly, AABs using NaOH-OPA electrolyte present much higher power den- sity, up to $68.5~mW~cm^{-2}$. As a consequence, $1~mm$ is consid ered as the optimal condition for OPA to balance the two con- jugate reactions.

Then, the discharge behavior of AABs based on $1~mm$ OPA-4 M NaOH electrolyte under various current densities are tested to analyze the failure mechanism of AABs under working conditions (Figure 6b). The current density of $20~mA~cm^{-2}$ is assumed to be best, implying the continuous hydrogen accu- mulation is likely to block reaction site at low current density, and excessively fast discharge rate tends to affect the adsorp- tion effect of OPA on the interface, which results in AABs stop- ping working suddenly. OPA is an ideal additive in terms of both inhibition effect and cost (as discussed in Figures S18 and S19 and Table S12, Supporting Information). Based on it, a normal inorganic inhibitor, sodium stannate $(Na_{2}SnO_{3})$ is introduced to NaOH-OPA electrolyte, which pre- sent excellent synergistic inhibitory effect on self-corrosion of Al in alkaline AABs. When assembled AABs using a 4 M NaOH electrolyte with hydride additives (1 mM OPA-0.05 $M~Na_{2}SnO_{3}$), it could deliver an ultra-high specific capacity $2694~mAh~g^{-1}$, close to the theoretical capacity, remarkable the utilization rate of Al anode to $91\%$ at a current density of $10~mA~cm^{-2}$ (as shown in Figure 6c, Figures S13 and S14 and Table S7, Sup- porting Information). Importantly, all of these performances achieved in this work by virtue of the novel interface stability of strong hydrogen bonds between OPA with intermediate products, whether individual or collective inhibitors, are signifi- cantly higher than the control performances in the normal elec- trolyte and previously reported strategies (Figure 6d).

As a proof of concept, three AABs, where each Al foil area is $85~cm^{2}$ and each cell is coupled to double commercial air cathode using a 4 M NaOH electrolyte with the OPA additive, are connected in series to triple the output voltage and power. Accordingly, Figure 6e shows the open circuit voltage of the series AABs can be as high as 5.20 V, while the OCP of single AAB is 1.692 V (Figure S15a, Supporting Information). More impressively, they are designed to power a commercial digital camera, which can be effectively operated smoothly and stably for a long time (Figure 5f and Figure S15c, Supporting Infor- mation) with this AAB pile. The operation video is illustrated in supporting information (Video S1, Supporting Information). Therefore, it is a promising additive for high-power electronic equipment.

3. Conclusion

In summary, an effective and low-cost additive, OPA, is intro- duced into typical NaOH electrolyte to achieve the inhibition of parasitic corrosion of Al anode in AABs via the unique func- tion mechanism, which has been proved through theoretical calculation. This novel organic inhibitor can not only improve the interfacial stability by adsorbing on $Al(OH)_{3}$ (001) surface through hydrogen bonding to form a $Al-Al(OH)_{3}$-OPA protec- tive film, but also modify the deposited precipitate in the form of flakes, both of which help suppress self-corrosion and optimize discharge behavior. As a result, OPA endows AABs full cell higher capacity $(2353~mAh~g^{-1})$ at $20~mA~cm^{-2}$, which is signifi cant improvement over the cell using pure NaOH electrloyte $(1579~mAh~g^{-1})$. Moreover, AABs with $NaOH-OPA/Na_{2}SnO_{3}$ electrolyte are able to deliver higher capacity $(2694~mAh~g^{-1})$, $91\%$ of theoretical capacity at $10~mA~cm^{-2}$ owing to the excellent synergistic effects, which is much better than pure NaOH elec- trolyte (59% retention). Notably, the improvement of all of these performances proves once again the optimized electrochem- ical performance for AABs with such a novel OPA additive. Importantly, our proposed electrolyte additive exhibits obvious advantages than other types of reported additives in view of the voltage plateau, specific capacity and the eco-friendly. By applying OPA molecule to the normal electrolyte, a 5.2 V AAB pile is fabricated to drive a commercial digital camera, which demonstrates the potential for practical applications. This work has provided an effective and scalable electrolyte inhibitor strategy for parasitic corrosion of Al anodes and longer-life alka- line AABs, which is likely to open up a promising way for other aqueous MBAs.

4. Experimental Section

Materials and Chemicals: 4 M sodium hydroxide (NaOH) (98%, Alfa Aesar) solution without and with various amounts of inhibitors (n-octyl phosphonic acid, abbreviated as OPA, 95% purity, Macklin, and $Na_{2}SnO_{3}$, 98%, Alfa Aesar; n-proplyphonic acid, abbreviated as PPA, 98%, Heowns; n-hexylphosphonic acid, abbreviated as HPA, 98%, Aladdin; n-dodecylphosphonic acid, abbreviated as DDPA, 97%, Aladdin; n-octadecylphosphonic acid, abbreviated as ODPA, 97%, Macklin) were employed as the electrolyte. Before each test, commercial Al foils (99.99%, 0.25 mm in thickness, Alfa Aesar) were mechanically polished with emery papers of #1200-7000 to remove the natural oxide film on the surface, and then washed with acetone, absolute ethanol, and ultrapure water in turn for 15 min under ultrasonic bath, and finally dried in vacuum at $60^{\circ}C$ for 6 h.

Al Self-Corrosion Rate Measurements: To quantitatively characterize the self-corrosion rates of Al foils $(20×20×0.25~mm)$ in the pristine NaOH and NaOH solutions with various amounts of OPA, a drainage- weighing setup was specially designed to measure the volume of hydrogen by-products at room temperature. The pre-cut Al foils were immersed in a conical flask containing 100 mL of different solutions, and the weighing values of the electronic balance were recorded every5 min for 1 h. The corrosion rates $(R_{corr})$ and inhibition efficiency $(\varphi_{inh})$ of the samples were calculated from the volume of hydrogen, V, as:

$$
R_{\text{corr}}=\frac{V}{St}=\frac{m}{\rho St} \tag{6}
$$

$$
\varphi_{\text{inh}}=\frac{R_{\text{w/o}}-R_{\text{w}}}{R_{\text{w/o}}}×100\% \tag{7}
$$

where V represents the volume of hydrogen collected in mL, S stands for the area of Al foils in $cm^{2}$, t is the immersion time of samples in min, m refers to the mass of discharged water (unit: g), $\rho$ is the density of water under the same conditions, in $g~mL^{-1}$. $R_{w}$ and $R_{w/o}$ are the Al self- corrosion rates in electrolytes with or without inhibitors, respectively.

Characterizations: The surface morphology and corresponding elemental pattern analysis of Al foils after immersion in bare NaOH and NaOH-OPA solutions, discharged product of AABs and the catalytic layer of commercial air cathode were characterized by field- emission scanning electron microscopy (Zeiss Gemini SEM 500). Elemental scanning patterns were recorded using energy dispersive

X-ray spectrometer (Ultim extreme). The chemical composition and elementary valence information of these Al foils surfaces were gathered by XPS (Escalab 250 xi+), XRD (Rigaku Ultima IV, Cu K$\alpha$) and FT-IR (Bruker vertex v70v). Raman spectra were recorded using a XploRA confocal Raman microscope with an excitation wavelength of 638 nm (Jobin Yvon-Horiba, France). The contact angles of different electrolytes were collected through a contact angle meter (OCA 100, Germany).

Electrochemical Measurements: The corrosion behavior of Al anode was performed under an electrochemical workstation (CHI 631) with a three-electrode system, where Al foil, Pt and Hg/HgO were as work electrode, counter electrode and reference electrode, respectively. The open-circle potential (OCP) curves were recorded for 4500 s. The Tafel plots were recorded by linear voltammetry scanning (LSV) at a scan rate of 5 mV s$^{-1}$ in a potential range of ±300 mV versus OCP of the system. The inhibition efficiency ($\eta$) can be therefore calculated using the following formula.

$$
\eta=\frac{j_{\mathrm{w} / \mathrm{o}}-j_{\mathrm{w}}}{j_{\mathrm{w} / \mathrm{o}}} \times 100 \% \tag{8}
$$

$j_{\mathrm{w}}$ and $j_{\mathrm{w/o}}$ stand for the corrosion current density for Al anodes in 4 м NaOH solution with and without inhibitors, respectively. The EIS measurements were conducted under OCP in a frequency range from 100 kHz and 0.01 Hz with the amplitude set to 5 mV on an Autolab PGSTAT204 electrochemical workstation (Metrohm).

Al-Air Full Battery Performance: Galvanostatic discharging behavior of AABs was investigated on a LANHE CT2001A battery testing system (LAND Electronics). The commercial air cathode (Figure S16, Supporting Information) was composed of $\mathrm{MnO}_{2} / \mathrm{C}$ catalyst, $^{[60-62]}$ nickel mesh, and gas diffusion layer. AABs were assembled with Al foils as anodes, glass fibers as separators, 4 м NaOH with or without additives as electrolytes and the commercial air cathodes in the atmosphere. The specific discharge capacities values were calculated based on the mass of Al consumed. The utilization (UAl) of Al anode should been taken into consideration, which can be given by:

$$
U_{\mathrm{Al}}=\frac{9 I t}{\Delta m F} \times 100 \% \tag{9}
$$

where $I$ is the current, $t$ is the discharge time (in h), $F$ is the Faraday constant, and $\Delta m$ is the mass difference of Al foils before and after discharging.

DFT Calculations: In consideration of the experimental system in strongly alkaline environments, OPA should be deprotonated, and it's doubly negative charged state has been adopted in all theoretical calculations here. The geometry optimization of OPA was performed at the B3LYP/6-311+G(d,p) level by using the Gaussian09 program. $^{[63]}$ OPA adsorption on the Al(022) surface was investigated with the GGA-PBE functional, $^{[64]}$ implemented in the Vienna ab initio simulation package. $^{[65]}$ The lattice constants of the supercell for the target system are $a = 20.25$, $b = 8.59$, $c = 36.83$ Å, with a vacuum region of 20 Å. The energy cutoff was set to be 400 eV, and the Brillouin zone was sampled with a $2 \times 6 \times 1$ k-point grid. The convergence criteria for energy and force were set to be $10^{-7}$ eV and $0.02$ eV Å$^{-1}$, respectively.

Molecular Dynamics Simulations: The interactions between OPA and $\mathrm{Al(OH)_3(001)}$ surface were investigated by using molecular dynamics (MD) simulations with the Forcite module. $^{[66]}$ $500\ \mathrm{H_2O}$, $36\mathrm{Na^+}$, and $36\ \mathrm{OH^-}$ are put into the computational unit-cell model to simulate the alkaline solvent. The interactions between $\mathrm{Al(OH)_3}$ (001) facet and OPA in a periodic supercell $(25.31 \times 34.68 \times 38.00$ Å$^3)$ were investigated by using the Dreiding force field. $^{[67]}$ All MD simulations were performed in the NVT ensemble at 298 K with the total simulation time of 5 ns and the time step of 1 fs.

Quantum-Mechanics/Molecular-Mechanics Calculations: Since there are complicated noncovalent and bonding interactions at the surface/ interface of $\mathrm{Al}$ and $\mathrm{Al(OH)_3}$ with OPA, as well as, water molecules, etc. which play a vital role in preventing the self-corrosion of Al, here combined QM/MM methods implemented in QMERA$^{[68]}$ were used to calculate interactions between OPA and $\mathrm{Al(OH)_3}$ (001) surface. In QM/ MM calculations, the QM region consists of OPA molecules and other atoms are in the MM region. The QM region was optimized by using the PBE/DND approach in the DMol3 module, and the tolerances for energy and force were set to be $2 \times 10^{-4}$ Ha and $4 \times 10^{-3}$ Ha/Å, respectively. The optimization of MM region was performed by using the Dreiding force field in the GULP module.

## Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements
Y.H. and L.F. contributed equally to this work. The authors acknowledge financial support from the National Natural Science Foundation of China (NSFC, 21875155, 22032004, 21975211, 21901240). The authors are grateful to Dr. Yuhao Hong at Tan Kah Kee Innovation Laboratory (IKKEM), Center for Micro-nano Fabrication and Advanced Characterization, Xiamen University for help with the XPS measurement.

## Conflict of Interest
The authors declare no conflict of interest.

## Data Availability Statement
The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Keywords
aluminum anodes, aluminum-air batteries, corrosion inhibitors, self-corrosion

Received: November 11, 2021
Revised: December 8, 2021
Published online: December 29, 2021

[1] Q. F. Liu, Z. F. Pan, E. D. Wang, L. An, G. Q. Sun, *Energy Storage Mater.* **2020**, 27, 478.
[2] H. P. Wang, R. Tan, Z. X. Yang, Y. Z. Feng, X. C. Duan, J. M. Ma, *Adv. Energy Mater.* **2021**, 11, 18.
[3] Y. Sun, X. Liu, Y. Jiang, J. Li, J. Ding, W. Hu, C. Zhong, *J. Mater. Chem. A* **2019**, 7, 18183.
[4] E. Grishina, D. Gelman, S. Belopukhov, D. Starosvetsky, A. Groysman, Y. Ein-Eli, *ChemSusChem* **2016**, 9, 2103.
[5] S. Choi, D. Lee, G. Kim, Y. Y. Lee, B. Kim, J. Moon, W. Shim, *Adv. Funct. Mater.* **2017**, 27, 9.
[6] X. Zhang, R. Lv, W. Tang, G. Li, A. Wang, A. Dong, X. Liu, J. Luo, *Adv. Funct. Mater.* **2020**, 30, 2004187.
[7] G. A. Elia, K. Marquardt, K. Hoeppner, S. Fantini, R. Lin, E. Knipping, W. Peters, J. F. Drillet, S. Passerini, R. Hahn, *Adv. Mater.* **2016**, 28, 7564.
[8] E. Faegh, B. Ng, D. Hayman, W. E. Mustain, *Nat. Energy* **2021**, 6, 21.
[9] D. Gelman, B. Shvartsev, Y. Ein-Eli, *J. Mater. Chem. A* **2014**, 2, 20237.
[10] S. H. Yang, H. Knickle, *J. Power Sources* **2002**, 112, 162.

Adv. Sustainable Syst. 2022, 6, 2100420
2100420 (11 of 12)
© 2021 Wiley-VCH GmbH

[11] H. Yang, H. Li, J. Li, Z. Sun, K. He, H.-M. Cheng, F. Li, Angew. Chem., Int. Ed. 2019, 58, 11978.

[12] L. Wang, R. Cheng, C. Liu, M. C. Ma, W. Wang, G. Yang, M. K. H. Leung, F. Liu, S. P. Feng, Mater. Today Phys. 2020, 14, 100242.

[13] G. A. Elia, K. Marquardt, K. Hoeppner, S. Fantini, R. Y. Lin, E. Knipping, W. Peters, J. F. Drillet, S. Passerini, R. Hahn, Adv. Mater. 2016, 28, 7564.

[14] T. Hu, K. Li, Y. Fang, L. Su, Z. Song, H. Shen, L. Sheng, Int. J. Energy Res. 2019, 43, 1099.

[15] T. Hibino, K. Kobayashi, M. Nagao, J. Mater. Chem. A 2013, 1, 14844.

[16] R. Buckingham, T. Asset, P. Atanassov, J. Power Sources 2021, 498, 229762.

[17] S. Wu, Q. Zhang, J. Ma, D. Sun, Y. Tang, H. Wang, Mater. Today Energy 2020, 18, 100499.

[18] Y. S. Liu, Q. Sun, W. Z. Li, K. R. Adair, J. Li, X. L. Sun, Green Energy Environ. 2017, 2, 246.

[19] I. J. Park, S. R. Choi, J. G. Kim, J. Power Sources 2017, 357, 47.

[20] H. Lee, T. A. Listyawan, N. Park, G. Kim, I. Chang, Int. J. Precis. Eng. Manuf.-Green Technol. 2020, 7, 505.

[21] X. Liu, P. Zhang, J. Xue, C. Zhu, X. Li, Z. Wang, Chem. Eng. J. 2021, 417, 128006.

[22] J. Ren, C. Fu, Q. Dong, M. Jiang, A. Dong, G. Zhu, J. Zhang, B. Sun, ACS Sustainable Chem. Eng. 2021, 9, 2300.

[23] J. Ma, J. Wen, J. Gao, Q. Li, Electrochim. Acta 2014, 129, 69.

[24] S. G. Wu, S. Y. Hu, Q. Zhang, D. Sun, P. F. Wu, Y. G. Tang, H. Y. Wang, Energy Storage Mater. 2020, 31, 310.

[25] Z. Zhang, C. C. Zuo, Z. H. Liu, Y. Yu, Y. X. Zuo, Y. Song, J. Power Sources 2014, 251, 470.

[26] Y. Li, L. Liu, Y. Lu, R. Shi, Y. Ma, Z. Yan, K. Zhang, J. Chen, Adv. Funct. Mater. 2021, 31, 2102063.

[27] Y. Xu, Y. Zhao, J. Ren, Y. Zhang, H. Peng, Angew. Chem., Int. Ed. Engl. 2016, 55, 7979.

[28] L. Ye, Y. Hong, M. Liao, B. J. Wang, D. C. Wei, H. S. Peng, L. Ye, Y. Hong, M. Liao, B. Wang, D. Wei, H. Peng, Energy Storage Mater. 2020, 28, 364.

[29] C. C. Zhao, X. Gao, H. F. Lu, R. Yan, C. T. Wang, H. Y. Ma, RSC Adv. 2015, 5, 54420.

[30] R. Revel, T. Audichon, S. Gonzalez, J. Power Sources 2014, 272, 415.

[31] D. Gelman, B. Shvartsev, Y. Ein-Eli, Top. Curr. Chem. 2016, 374, 82.

[32] Y. Wang, H. Y. H. Kwok, W. Pan, H. Zhang, X. Lu, D. Y. C. Leung, Appl. Energy 2019, 251, 113342.

[33] S. G. Wu, Q. Zhang, D. Sun, J. Y. Luan, H. W. Shi, S. Y. Hu, Y. G. Tang, H. Y. Wang, Chem. Eng. J. 2020, 383, 123162.

[34] J. Ryu, M. Park, J. Cho, Adv. Mater. 2019, 31, 8.

[35] X. Li, J. Li, D. Zhang, L. Gao, J. Qu, T. Lin, J. Mol. Liq. 2021, 322, 114946.

[36] D. Gelman, I. Lasman, S. Elfimchev, D. Starosvetsky, Y. Ein-Eli, J. Power Sources 2015, 285, 100.

[37] C. Zhu, H. X. Yang, A. Q. Wu, D. Q. Zhang, L. X. Gao, T. Lin, J. Power Sources 2019, 432, 55.

[38] Y. Liu, Q. Sun, X. Yang, J. Liang, B. Wang, A. Koo, R. Li, J. Li, X. Sun, ACS Appl. Mater. Interfaces 2018, 10, 19730.

[39] M. A. Deyab, J. Power Sources 2019, 412, 520.

[40] P. F. Sun, J. T. Chen, Y. L. Huang, J. H. Tian, S. Li, G. L. Wang, Q. B. Zhang, Z. W. Tian, L. Zhang, Energy Storage Mater. 2021, 34, 427.

[41] H. Cheng, T. Wang, Z. Li, C. Guo, J. Lai, Z. Tian, ACS Appl. Mater. Interfaces 2021, 13, 51735.

[42] J. Liu, D. P. Wang, D. Q. Zhang, L. X. Gao, T. Lin, J. Power Sources 2016, 335, 1.

[43] J. X. Gao, Y. Li, Z. Yan, Q. F. Liu, Y. L. Gao, C. K. Chen, B. Ma, Y. J. Song, E. D. Wang, J. Power Sources 2019, 412, 63.

[44] Q. X. Kang, T. Y. Zhang, X. Wang, Y. Wang, X. Y. Zhang, J. Power Sources 2019, 443, 227251.

[45] H. Jiang, S. Yu, W. Z. Li, Y. H. Yang, L. S. Yang, Z. J. Zhang, J. Power Sources 2020, 448, 227460.

[46] N. Ammouchi, H. Allal, Y. Belhocine, S. Bettaz, E. Zouaoui, J. Mol. Liq. 2020, 300, 112309.

[47] C. C. Ye, F. Q. Zhao, S. Y. Xu, X. H. Ju, J. Mol. Model. 2013, 19, 2451.

[48] H. J. Flitt, D. P. Schweinsberg, Corros. Sci. 2005, 47, 2125.

[49] R. Brandiele, C. Durante, E. Gradzka, G. A. Rizzi, J. Zheng, D. Badocco, P. Centomo, P. Pastore, G. Granozzi, A. Gennaro, J. Mater. Chem. A 2016, 4, 12232.

[50] S. J. Yoo, K. S. Lee, S. J. Hwang, Y. H. Cho, S. K. Kim, J. W. Yun, Y. E. Sung, T. H. Lim, Int. J. Hydrogen Energy 2012, 37, 9758.

[51] G. B. Hix, V. J. Carter, D. S. Wragg, R. E. Morris, P. A. Wright, J. Mater. Chem. 1999, 9, 179.

[52] G. Chaplais, J. L. Bideau, De Leclercq, H. Mutin, A. Vioux, J. Mater. Chem. 2000, 10, 1593.

[53] K. M. Naik, E. Higuchi, H. Inoue, J. Power Sources 2020, 455, 227972.

[54] S. Choi, H. W. Do, D. Jin, S. Kim, J. Lee, A. Soon, J. Moon, W. Shim, Adv. Funct. Mater. 2021, 31, 2101720.

[55] S. Hosseini, Z. Y. Liu, C. T. Chuan, S. M. Soltani, V. K. Lanjapalli, Y. Y. Li, Electrochim. Acta 2021, 375, 137995.

[56] K. Niegelhell, S. Leimgruber, T. Griesser, C. Brandl, B. Chernev, R. Schennach, G. Trimmel, S. Spirk, Langmuir 2016, 32, 1550.

[57] Q. Zhao, M. J. Zachman, W. I. Al Sadat, J. Zheng, L. F. Kourkoutis, L. Archer, Sci. Adv. 2018, 4, 8131.

[58] X. D. Lin, Y. Gu, X. R. Shen, W. W. Wang, Y. H. Hong, Q. H. Wu, Z. Y. Zhou, D. Y. Wu, J. K. Chang, M. S. Zheng, B. W. Mao, Q. F. Dong, Energy Environ. Sci. 2021, 14, 1439.

[59] B. Yu, Z. H. Tian, J. Xiong, L. Xiang, J. Nanomater. 2013, 2013, 718979.

[60] N. N. Xu, Q. Nie, L. Y. Q. Luo, C. Z. Yao, Q. J. Gong, Y. Y. Liu, X. D. Zhou, J. L. Qiao, ACS Appl. Mater. Interfaces 2019, 11, 578.

[61] B. Xu, H. Lu, W. Cai, Y. Cao, Y. Deng, W. Yang, Electrochim. Acta 2019, 305, 360.

[62] N. R. Levy, P. Tereshchuk, A. Natan, R. Haas, D. Schroeder, J. Janek, P. Jakes, R. A. Eichel, Y. Ein-Eli, J. Power Sources 2021, 514, 230597.

[63] L. Ouksel, R. Bourzami, S. Chafaa, N. Chafai, J. Mol. Struct. 2020, 1222, 128813.

[64] J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1997, 78, 1396.

[65] J. Radilla, G. E. N. Silva, M. P. Pardave, M. R. Romo, M. Galvan, Electrochim. Acta 2013, 112, 577.

[66] S. Farahati, A. Ghaffarinejad, S. M. Mousavi-Khoshdel, J. Rezania, H. Behzadi, A. Shockravi, Prog. Org. Coat. 2019, 132, 417.

[67] S. L. Mayo, B. D. Olafson, W. A. Goddard, J. Phys. Chem. 1990, 94, 8897.

[68] L. J. Liu, Z. M. Wang, Y. J. Lyu, J. F. Zhang, Z. Huang, T. Qi, Z. B. Si, H. Q. Yang, C. W. Hu, Catal. Sci. Technol. 2020, 10, 278.

---

Adv. Sustainable Syst. 2022, 6, 2100420
2100420 (12 of 12)
© 2021 Wiley-VCH GmbH