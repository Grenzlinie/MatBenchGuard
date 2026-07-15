Journal Pre-proof

Probing Nano-QSAR to Assess the Interactions between Carbon Nanoparticles and a SARS-CoV-2 RNA Fragment

Fan Zhang, Zhuang Wang, Martina G. Vijver, Willie J.G.M. Peijnenburg

![](./images/812406166301704194_1.jpg)

<table>
  <tr>
    <td>PII:</td>
    <td>S0147-6513(21)00468-1</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.ecoenv.2021.112357</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>YEESA112357</td>
  </tr>
</table>

To appear in: *Ecotoxicology and Environmental Safety*

Received date: 7 March 2021
Revised date: 16 May 2021
Accepted date: 17 May 2021

Please cite this article as: Fan Zhang, Zhuang Wang, Martina G. Vijver and Willie J.G.M. Peijnenburg, Probing Nano-QSAR to Assess the Interactions between Carbon Nanoparticles and a SARS-CoV-2 RNA Fragment, *Ecotoxicology and Environmental Safety*, (2021)
doi:https://doi.org/10.1016/j.ecoenv.2021.112357

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2021 Published by Elsevier.

# Probing Nano-QSAR to Assess the Interactions between Carbon Nanoparticles and a SARS-CoV-2 RNA Fragment

Fan Zhang$^\text{a}$, Zhuang Wang$^\text{b}$, Martina G. Vijver$^\text{a,*}$, Willie J.G.M. Peijnenburg$^\text{a,c,*}$

$^\text{a}$ Institute of Environmental Sciences (CML), Leiden University, Leiden 2300 RA, The Netherlands

$^\text{b}$ School of Environmental Science and Engineering, Collaborative Innovation Center of Atmospheric Environment and Equipment Technology, Jiangsu Key Laboratory of Atmospheric Environment Monitoring and Pollution Control, Nanjing University of Information Science and Technology, Nanjing 210044, P.R. China

$^\text{c}$ Centre for Safety of Substances and Products, National Institute of Public Health and the Environment (RIVM), Bilthoven 3720 BA, The Netherlands

* Corresponding authors:

E-mail addresses: Vijver@cml.leidenuniv.nl (M. G. Vijver), peijnenburg@cml.leidenuniv.nl (W. J. G. M. Peijnenburg)

ORCID:

0000-0003-1709-7788 (F. Zhang)

0000-0001-7032-4500 (Z. Wang)

0000-0003-2999-1605 (M. G. Vijver)

0000-0003-2958-9149 (W. J. G. M. Peijnenburg)

### Abstract

The coronavirus disease-19 (COVID-19) pandemic caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is rampant in the world and is a serious threat to global health. The SARS-CoV-2 RNA has been detected in various environmental media, which speeds up the pace of the virus becoming a global biological pollutant. Because many engineered nanomaterials (ENMs) are capable of inducing anti-microbial activity, ENMs provide excellent solutions to overcome the virus pandemic, for instance by application as protective coatings, biosensors, or nano-agents. To tackle some mechanistic issues related to the impact of ENMs on SARS-CoV-2, we investigated the molecular interactions between carbon nanoparticles (CNPs) and a SARS-CoV-2 RNA fragment (i.e., a model molecule of frameshift stimulation element from the SARS-CoV-2 RNA genome) using molecular mechanics simulations. The interaction affinity between the CNPs and the SARS-CoV-2 RNA fragment increased in the order of fullerenes < graphenes < carbon nanotubes. Furthermore, we developed quantitative structure-activity relationship (QSAR) models to describe the interactions of 17 different types of CNPs from three dimensions with the SARS-CoV-2 RNA fragment. The QSAR models on the interaction energies of CNPs with the SARS-CoV-2 RNA fragment show high goodness-of-fit and robustness. Molecular weight, surface area, and the sum of degrees of every carbon atom were found to be the primary structural descriptors of CNPs determining the interactions. Our research not only offers a theoretical insight into the adsorption/separation and inactivation of SARS-CoV-2, but also allows to design novel ENMs which act efficiently on the genetic material RNA of SARS-CoV-2. This contributes to minimizing the challenge of time-consuming

and labor-intensive virus experiments under high risk of infection, whilst meeting our precautionary demand for options to handle any new versions of the coronavirus that might emerge in the future.

**Keywords:** COVID-19; Coronavirus; Genetic material; Nanomaterials; Interaction

### 1. Introduction

The outbreak of a new coronavirus which by now has lasted for more than a year, has brought great disaster to human beings (Diffenbaugh et al., 2020; Slot et al., 2020; Snape et al., 2020). To deal with the most serious global public health emergency in recent decades, the governments of various countries have employed a number of measures to control the epidemic situation (Cheng et al., 2020). Scientists from various fields are stimulated to either improve existing or to develop new "weapons" against the coronavirus (Allawadhi et al, 2020; Florindo et al., 2020; Talebian et al., 2020). In response to the virus pandemic, nanoscience and nanotechnology are offering opportunities and challenges (Fig. 1).

Viruses such as the avian influenza virus (H5N1), the severe acute respiratory syndrome coronavirus (SARS), the swine influenza virus (H1N1), and the Middle East respiratory syndrome coronavirus (MERS) are nature's nanostructures (Kostarelo, 2020) which easily enter biological entities because of their special nanostructure-related advantages. Similarly, engineered nanomaterials (ENMs) also have such special properties due to the small size and hence relative large surface to volume ratio, which is in part why ENMs have been widely used for a variety of biomedical applications. In this respect there is a growing need for design of ENMs that are highly specific and efficiently taken up into target cells. The controllable

physicochemical properties (e.g., size, shape, and surface) of ENMs facilitate their direct interactions with viral particles (e.g., interacting with viral envelope proteins and nucleic acids) or with host cell surface receptors to inhibit virus-cell interactions (Chen et al., 2020). Hence, there is an urgent need to realize whether ENMs as anti-viral nano-agents can offer effective therapeutic strategies to combat the emergence of the coronavirus disease-19 (COVID-19). Although there has been criticism about the negative impact of nanotechnology, the time for the SARS-CoV-2 pandemic has now come to highlight the knowledge and previous experience of nanotechnologists in vaccine and drug development, delivery, and distribution (Anonymous et al., 2020). At the same time, the presence of the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) RNA in the environment such as in air (Mohan et al., 2021; Morawska and Cao, 2020) and water (Kitajima et al., 2020; Mohan et al., 2021) requires us to confirm whether ENMs because of their strong tendency to adsorb to any biotic or abiotic moiety, can efficiently remove the novel coronavirus. Understanding the interaction mechanisms between ENMs and macromolecules that are part of SARS-CoV-2 is an important foundation for the application of ENMs versus COVID-19.

Molecular simulation methods could be effective tools in exploring the interactions between ENMs and biomacromolecules with key biological functions (Ge et al., 2011), which would facilitate the design of novel nano-agents and improve the development and application of new therapeutic techniques. Quantitative structure–activity relationships for nanomaterials (nano-QSARs) are guided by the classical QSAR model and combine impacts of (non-tested) ENMs with their specific physicochemical properties (Chen et al., 2017; Puzyn et al., 2011). This provides a new way for rapid screening and priority testing of those ENMs that are predicted to

be the most effective anti-viral agents. Combined with molecular simulation, nano-QSAR will play an increasingly important role in the fight against COVID-19 and future virus pandemics.

Many ENMs are known to exhibit high anti-microbial activity; either via induction of oxidative stress by for instance metal-based ENMs from which ions dissolve having the ability to generate oxidative stress (Sánchez-López et al., 2020), or via photothermal/photocatalytic effects, lipid extraction, inhibition of bacterial metabolism, isolation by wrapping the microbes (Maleki Dizaj et al., 2015) with a nano-layer due to the high adsorption and high mechanical strength of ENMs. Also carbon nanoparticles (CNPs) are recognized as a promising nanomaterial for the detection, filtering, and inactivation of viruses. According to recent studies the physical interaction of carbon-based nanomaterials with bacteria, rather than oxidative stress, is the primary antimicrobial activity of these nanostructures (Maleki Dizaj et al., 2015). An additional benefit of carbon-based nanoparticles is that their high bio-safety and high biological compatibility, which are the characteristics used to comply with various medical drugs (Aasi et al., 2020; Łoczechin et al., 2019; Palmieri et al., 2020; Vermisoglou et al., 2020). Therefore, this work is devoted to assessing and quantifying the interactions of the key fragment of the SARS-CoV-2 RNA (Zhang, Zheludev et al., 2020) with CNPs of different type and dimension. The fragment is a model molecule of frameshift stimulation element (FSE) from the SARS-CoV-2 RNA genome (Zhang, Zheludev et al., 2020). What is more, the FSE plays an important role in the virus replication cycle and has emerged as a major drug target (Lan et al., 2020). Subsequently, a predictive model is developed which quantifies the relationship between the structural properties of CNPs and these interactions.

## 2. Computational Methods

### 2.1. Annealing Simulations

The three-dimensional structure of the SARS-CoV-2 fragment determined by Zhang, Zheludev et al. (2020) was used for the simulations. Seventeen CNPs from three families of fullerenes, carbon nanotubes (CNTs), and graphene were selected as model molecules (Fig. 2). The constructed fullerene molecular models include $\text{C}_{20}$, $\text{C}_{36}$, $\text{C}_{70}$, $\text{C}_{240}$, carbon nanoballs $\text{C}_{60}$ and $\text{C}_{20}@\text{C}_{60}$, as well as the carbon nano-onion $\text{C}_{20}@\text{C}_{60}@\text{C}_{240}$. The constructed carbon nanotube molecular models include single-walled carbon nanotube (SCNT) (10,0), SCNT (6,6), SCNT (28,0), double-walled carbon nanotube (DCNT) (10,0), DCNT (6,6), triple-walled carbon nanotube (TCNT) (10,0), nanorope (NR) (6,6), and the complexes SCNT (16,0) with $\text{C}_{60}$ named $\text{SCNT (16,0)}@\text{C}_{60}$. The constructed graphene molecular models include mono-layer graphene (MG) and bilayer graphene (BG). To search for the best geometry with various forms of energy for each complex of the CNPs with the SARS-CoV-2 RNA fragment, a classical annealing simulation was performing with the Materials Studio software package (Ver. 8.0). The universal force field was adopted to perform this simulation. The cutoff radius was chosen to be $18.5\ \mathring{\text{A}}$. The annealing simulation was performed as follows: a total of 200 annealing cycles which represented an optimal balance of total energy (Fig. S1, Supplementary material) were simulated with an initial temperature of 200 K, a midcycle temperature of 300 K, and 50 heating ramps per cycle, with 100 dynamic steps per ramp. The canonical ensemble (NVT ensemble, in which the number of molecules [$N$], volume [$V$], and temperature [$T$] of the system are kept constant) was used and the molecular dynamic simulations were performed with a time step of 1.0 fs and a Nosé thermostat. After each cycle, the lowest energy configuration was optimized. The ‘van der

Waals' energies, electrostatic and total potential energies of the studied systems were calculated using the annealing simulation.

For the interaction systems, interaction energy ($E_{\text{int}}$) is used to evaluate the stability of the complexes of the CNPs with the SARS-CoV-2 RNA fragment. The magnitude of $E_{\text{int}}$ is an indication of the magnitude of the driving force towards complexation. A negative value reflects a stable adsorption on the CNPs. $E_{\text{int}}$ was calculated by

$$
E_{\text{int}} = E_{\text{CNP-covRNA}} - E_{\text{CNP}} - E_{\text{covRNA}} \tag{1}
$$

where $E_{\text{CNP-covRNA}}$, $E_{\text{CNP}}$, and $E_{\text{covRNA}}$ represent the energies (van der Waals, electrostatic, or total potential energies) of the complex, the isolated CNPs, and the individual SARS-CoV-2 RNA fragment, respectively.

### 2.2. Development of a nano-QSAR predictive model for $E_{\text{int}}$

Based on the interactions between the CNPs and the SARS-CoV-2 RNA fragment implied by the annealing simulations, several constitutional geometric and topological descriptors (Table 1) such as molecular weight ($M_{\text{W}}$), overall surface area ($OSA$), volume ($Vol$), specific surface area ($SSA$), and sum of degrees ($SDeg$), were selected to correlate with $E_{\text{int}}$ so as to construct predictive models. $OSA$ and $Vol$ were calculated using Multiwfn 3.8 software (Lu and Chen, 2012a,b). The $SSA$ values were obtained directly from the derivation of $OSA$ and $Vol$. $SDeg$ was calculated using Chem3D Ultra (Ver. 19.0). Orthogonal partial least squares (OPLS) regression was performed with Simca (Ver. 14.1 Umetri AB & Erisoft AB) to select variables and to develop models. Randomization tests proposed for testing the rationality of the models were

performed using the RAND () function to generate the pseudo-random numbers of the $E_{\text{int}}$ derived from the total potential energy.

## 3. Results and Discussion

### 3.1. Modeling the interaction of CNPs with the SARS-CoV-2 RNA fragment

In order to reveal the mechanisms of the interactions of CNPs with the SARS-CoV-2 RNA fragment, the $E_{\text{int}}$ derived from the total potential energies, the 'van der Waals' energies, and electrostatic energies are summarized in Fig. 3. The optimized conformations obtained after the annealing simulations are shown in Fig. 3A. The computed values are negative, indicating that the CNPs can form stable complexes with the SARS-CoV-2 RNA fragment. Fig. 3B shows that CNTs have the highest absolute energy of interaction with the SARS-CoV-2 RNA fragment among the studied CNPs, as derived from the total potential energies. This suggests a strong interaction between the CNTs and the SARS-CoV-2 RNA fragment.

Generally, the interaction affinity between the CNPs and the SARS-CoV-2 RNA fragment increased in the order of fullerenes < graphenes < CNTs. In addition, the computed electrostatic interaction energies between the CNPs and the SARS-CoV-2 RNA fragment are similar to the $E_{\text{int}}$ values (Fig. 3B). This implies that the electrostatic interaction contributes mainly to the mechanism of interaction. Wang et al. (2017) also concluded that electrostatic interactions contribute to the gaseous adsorption energies of organic molecules onto carbon-based nanomaterials by means of polyparameter linear free energy relationships. As the SARS-CoV-2 has a positive charge (Zhang, Zheludev, 2020), whereas the studied CNPs are neutral, the electrostatic interactions are mainly ion-induced dipole interactions.

### 3.2. Nano-QSAR prediction of the interaction of CNPs with the SARS-CoV-2 RNA fragment

The OPLS regression technique was used to find the most suited descriptors (Table 1) for developing models to quantify the $E_{\text{int}}$ derived from the total potential energies (Eqs. (2)-(4)). $SSA$ is the parameter that most significantly correlates with the $E_{\text{int}}$ values of fullerenes, and there is a positive correlation between $SSA$ and the absolute value of $E_{\text{int}}$. For CNTs and graphenes, $OSA$ and $SDeg$ are the parameters that correlate most significantly with the $E_{\text{int}}$ values. At the same time, $OSA$ showed a positive correlation with the absolute $E_{\text{int}}$, whereas $SDeg$ displayed a negative correlation with the absolute $E_{\text{int}}$. For the whole set of fullerenes, CNTs, and graphenes, $M_W$ and $SDeg$ are the parameters correlating most significantly with the $E_{\text{int}}$ values. Moreover, $M_W$ presented a positive correlation with the absolute value of $E_{\text{int}}$, while $SDeg$ had a negative correlation with the absolute value of $E_{\text{int}}$.

Among the selected descriptors, $M_W$ usually describes the size of a molecule. $SDeg$ as a molecular descriptor of topology is the sum of degrees of every atom, and an atom's degree is the number of non-hydrogen atoms to which it is bonded. Moreover, $SSA$ and $OSA$ are known to be associated with the steric structures of NPs. Note that surface properties such as surface area generally dominate the behavior (Yang et al., 2010) and effects (Mottier et al., 2016) of CNPs. Taken together, the selected nano-specific descriptors not only are easy to obtain, but also can explain the interaction mechanism.

Fullerenes:

$$E_{\text{int}} = -32.241 - 0.021 \cdot SSA \tag{2}$$

$$n=7, R^2=0.804, \text{RMSE}=0.485, \text{Q}^2_{\text{CUM}}=0.737$$

CNTs and graphenes:

$$E_{\text{int}} = -309.469 - 0.742 \cdot OSA + 0.039 \cdot SDeg \tag{3}$$

$$n = 10, R^2 = 0.849, \text{RMSE} = 0.440, \text{Q}^2_{\text{CUM}} = 0.681$$

Fullerenes, CNTs, and graphenes:

$$E_{\text{int}} = -110.679 - 0.007 \cdot Mw + 0.020 \cdot SDeg \tag{4}$$

$$n = 17, R^2 = 0.804, \text{RMSE} = 0.473, \text{Q}^2_{\text{CUM}} = 0.710$$

where $n$ stands for the number of CNPs, $R^2$ is squared regression coefficient, *RMSE* is root mean squared error, and $\text{Q}^2_{\text{CUM}}$ is the cumulative percentage of variance explained for extracted components. The values of $\text{Q}^2_{\text{CUM}}$ of the models are higher than 0.5, suggesting the good robustness and internal predictability of the models and the models thus have high goodness-of-fit.

To further ensure the reliability of the obtained models, randomization tests was carried out by generating a fake pool of data for the $E_{\text{int}}$ values derived from the total potential energies (Table S2, Supplementary material). The $E_{\text{int}}$ values were scrambled in two ways, namely a single sample one and a full one, to generate the pseudo-random numbers. As shown in Table S2 (Supplementary material), all the OPLS models obtained with the scrambled data exhibited non-competitive $R^2$ and $\text{Q}^2_{\text{CUM}}$ values, as comparison to the three models provided in Eqs. (2)-(4). Thus, it is clear that the developed models are reliable and grasp the most significant

information used to interpret the interactions of CNPs with the SARS-CoV-2 RNA fragment. The outcome of the randomization testing also shows that the nano-specific descriptors are relevant.

### 3.3. Implications of nano-QSAR based approaches in battling coronaviruses

A virus can be regarded as a nanoscale particle consisting of outer-capsid proteins and inner-core nucleic acids (RNA or DNA). ENMs can not only directly interact with viral particles including the envelope protein and the nucleic acids, but they can also competitively bind with the cell receptors. As aforementioned, CNPs can interact with the SARS-CoV-2 RNA fragment and stabilize it. Knowing the interaction affinity between ENMs and virus particles is important for accurately inferring the efficacy of antiviral nano-agents, which can be applied to disrupt the viral replication cycle (Chen et al., 2020) and even directly to destroy its structure.

The SARS-CoV-2 RNA has been detected in environmental media (Al Huraimel et al., 2020; Kitajima et al., 2020; Mohan et al., 2021; Morawska and Cao, 2020), which causes the novel coronavirus to become an environmental pollutant especially in air, in sewage (e.g. via the stool of contaminated patients) and in watersheds. It is known that ENMs, especially carbon-based nanomaterials, are widely utilized in the adsorption and separation of environmental pollutants because of their strong adsorption capacity and high adsorption efficiency (Ji et al., 2013; Pan et al., 2008; Wang et al., 2017; Yang et al., 2010). It is reported that the SARS-CoV-2 RNA is likely to persist for a long time in untreated wastewater (Ahmed et al., 2020). Hence, it is important to elucidate the interactions of the CNPs with the SARS-CoV-2 RNA fragment. Besides, the knowledge of these interactions can deepen and expand related research in other nanotechnology-based applications, e.g., disinfectants for personal protective equipment and sensors for SARS-CoV-2 detection.

All human beta-coronaviruses share a certain degree of genetic and structural homology (Shin et al., 2020). As reported, the SARS-CoV-2 genome sequence homology with SARS-CoV and MERS-CoV is 77 % and 50 %, respectively (Kim et al., 2020). Hence, the nano-QSAR models developed for SARS-CoV-2 in the present study are likely to be suitable for forecasting the interactions between the CNPs and other beta-coronaviruses. Furthermore, we advocate to keep the modelling as simple as it can be, and to filter those molecular descriptors which are easy to obtain and are related to antimicrobial (physical) properties. In the face of the urgency of the COVID-19 pandemic, nano-QSAR is a useful tool to investigate the impacts of nanotechnology on the novel coronavirus, and it has the advantages of preliminary screening of effective ENMs that will save valuable research time - the step towards validating the models by means of experimental research can be started and done faster in a justified way. Eventually this may lead to saving efforts and preventing infection during experimental testing.

Nanomaterials entered the consumer market around 2000, meaning that by now nanoparticles are used in many products. For instance, within toothpaste titanium dioxide nanoparticles can be found as well as in creams to whiten products (Braakhuis et al., 2021; Rompelberg et al., 2016), and silver nanoparticles are used within many cosmetics like anti-aging creams (Kaul et al., 2018). The use of carbon-based nanomaterials for antiviral purposes is not so far off (Patel et al., 2019), and the virus killing activity of differently shaped carbon-based nanomaterials is intensively discussed (Innocenzi and Stagi, 2020; Serrano-Aroca et al., 2021). Serrano-Aroca et al. (2021) concluded that carbon-based nanomaterials had antiviral activity against 13 enveloped positive-sense single stranded RNA viruses, including SARS-CoV-2. It has been shown that the toxicity of nanomaterials is difficult to unravel, the antimicrobial activity of the nanoparticles

depends on their composition, surface modification, intrinsic properties (Innocenzi and Stagi, 2020). Especially for unwanted toxicity, rigid high aspect ratio carbon fibers might be an issue in this respect that need to be dived furth into. Nonetheless, the use of carbon-based biocompatible nanomaterials as antivirals is still an almost unexplored field, while the published results show promising prospects.

## 4. Conclusions

To sum up, through molecular mechanics simulations, we have mainly addressed the molecular interactions between CNPs and the SARS-CoV-2 RNA fragment. The estimated $E_{\text{int}}$ suggests that the electrostatic interaction could be the predominant driving force for the interactions. The models on $E_{\text{int}}$ developed by OPLS show high goodness-of-fit and robustness. Four nanostructural descriptors ($M_{\text{W}}$, $SSA$, $OSA$, and $SDeg$) were found to be the decisive factors controlling $E_{\text{int}}$.

## Acknowledgements

This article pays tribute to those who are fighting against COVID-19. This work was supported by the National Natural Science Foundation of China (31971522) to Z.W. and the European Union's Horizon 2020 research and innovation program "NanoinformaTIX" (814426) that supported W.J.G.M.P. and M.G.V. F.Z. greatly acknowledges the support from the China Scholarship Council (202008320308). We also thank the reviewers for their valuable comments on the manuscript.

### Competing interests

The authors declare no competing financial interest.

### Supplementary material

Variation of total energy of the complexes of the carbon nanoparticles with SARS-CoV-2 RNA fragment during Forcite Anneal optimization; Calculated total potential energy interaction energies ($E_{\text{int}}$), 'van der Waals' interaction energies, and electrostatic interaction energies between the CNPs and the SARS-CoV-2 RNA fragment (covRNA); Runs test for the calculated interaction energies derived from the total potential energies.

### References

Aasi, A.; Aghaei, S. M.; Moore, M. D.; Panchapakesan, B. Pt-, Rh-, Ru-, and Cu-Single-Wall Carbon Nanotubes are Exceptional Candidates for Design of Anti-Viral Surfaces: A Theoretical Study. *In. J. Mol. Sci.* **2020**, *21*, 5211.

Ahmed, W.; Bertsch, P. M.; Bibby, K.; Haramoto, E.; Hewitt, J.; Huygens, F.; Gyawali, P.; Korajkic, A.; Riddell, S.; Sherchan, S. P.; Simpson, S. L.; Sirikanchana, K.; Symonds, E. M.; Verhagen, R.; Vasan, M. Kitajima, S. S.; Bivins, A. Decay of SARS-CoV-2 and Surrogate Murine Hepatitis Virus RNA in Untreated Wastewater to Inform Application in Wastewater-Based Epidemiology. *Environ. Res.* **2020**, *191*, 110092.

Al Huraimel, K.; Alhosani, M.; Kunhabdulla, S.; Stietiya, M. H. SARS-CoV-2 in the Environment: Modes of Transmission, Early Detection and Potential Role of Pollutions. *Sci. Total Environ.* **2020**, *744*, 140946.

Allawadhi, P.; Khurana, A.; Allwadhi, S.; Joshi, K.; Packirisamy, G.; Bharani, K. K. Nanoceria as a Possible Agent for the Management of COVID-19. *Nano Today* **2020**, *35*, 100982.

Anonymous. Nanotechnology Versus Coronavirus. *Nat. Nanotechnol.* **2020**, *15*, 617.

Braakhuis, H. M.; Gosens, I.; Heringa, M. B.; Oomen, A. G.; Vandebriel, R. J.; Groenewold, M.; Cassee, F. R. Mechanism of Action of TiO₂: Recommendations to Reduce Uncertainties Related to Carcinogenic Potential. *Annu. Rev. Pharmacol. Toxicol.* **2021**, *61*, 203–223.

Chen, G.; Peijnenburg, W. J. G. M.; Xiao, Y.; Vijver, M. G. Current Knowledge on the Use of Computational Toxicology in Hazard Assessment of Metallic Engineered Nanomaterials. *Int. J. Mol. Sci.* **2017**, *18*, 1504.

Chen Y.; Ma J.; Xu M.; Liu S. Antiviral Nanoagents: More Attention and Effort Needed? *Nano Today* **2020**, *35*, 100976.

Cheng, C.; Barceló, J.; Hartnett, A. S.; Kubinec, R.; Messerschmidt, L. COVID-19 Government Response Event Dataset (CoronaNet v.1.0). *Nat. Hum. Behav.* **2020**, *4*, 756–768.

Diffenbaugh, N. S.; Field, C. B.; Appel, E. A.; Azevedo, I. L.; Baldocchi, D. D.; Burke, M.; Burney, J. A.; Ciais, P.; Davis, S. J.; Fiore, A. M.; Fletcher, S. M.; Hertel, T. W.; Horton, D. E.; Hsiang, S. M.; Jackson, R. B.; Jin, X.; Levi, M.; Lobell, D. B.; McKinley, G. A.; Moore, F. C.; Montgomery, A.; Nadeau, K. C.; Pataki, D. E.; Randerson, J. T.; Reichstein, M.; Schnell, J. L.; Seneviratne, S. I.; Singh, D.; Steiner, A. L.; Wong-Parodi, G. The COVID-19 Lockdowns: A Window into the Earth System. *Nat. Rev. Earth Environ.* **2020**, *1*, 470–481.

Florindo, H. F.; Kleiner, R.; Vaskovich-Koubi, D.; Acúrcio, R. C.; Carreira, B.; Yeini, E.; Tiram, G.; Liubomirski, Y.; Satchi-Fainaro, R. Immune-Mediated Approaches Against COVID-19. *Nat. Nanotechnol.* **2020**, *15*, 630–645.

Ge, C.; Du, J.; Zhao, L.; Wang, L.; Liu, Y.; Li, D.; Yang, Y.; Zhou, R.; Zhao, Y.; Chai, Z.; Chen, C. Binding of Blood Proteins to Carbon Nanotubes Reduces Cytotoxicity. *PNAS* **2011**, *108*, 16968–16973.

Innocenzi, P.; Stagi, L. Carbon-based Antiviral Nanomaterials: Graphene, C-dots, and Fullerenes. A Perspective. *Chem. Sci.* **2020**, *11*, 6606–6622.

Ji, L.; Chen, W.; Xu, Z.; Zheng, S.; Zhu, D. Graphene Nanosheets and Graphite Oxide as Promising Adsorbents for Removal of Organic Contaminants from Aqueous Solution. *J. Environ. Qual.* **2013**, *42*, 191–198.

Kaul, S.; Gulati, N.; Verma, D.; Mukherjee, S.; Nagaich, U. Role of Nanotechnology in Cosmeceuticals: A Review of Recent Advances. *J. Pharm.* **2018**, 3420204.

Kim, J.-M.; Chung, Y.-S.; Jo, H. J.; Lee, N.-J.; Kim, M. S.; Woo, S. H.; Park, S.; Kim, J. W.; Kim, H. M.; Han, M.-G. Identification of Coronavirus Isolated from a Patient in Korea with COVID-19. *Osong Public Health Res. Perspect.* **2020**, *11*, 3–7.

Kitajima, M.; Ahmed, W.; Bibby, K.; Carducci, A.; Gerba, C. P.; Hamilton, K. A.; Haramoto, E.; Rose, J. B.; SARS-CoV-2 in Wastewater: State of the Knowledge and Research Needs. *Sci. Total Environ.* **2020**, *739*, 139076.

Kostarelos, K. Nanoscale Nights of COVID-19. *Nat. Nanotechnol.* **2020**, *15*, 343–344.

Lan, T. C. T.; Allan, M. F.; Malsick, L. E.; Khandwala, S.; Nyeo, S. S. Y.; Bathe, M.; Griffiths A.; Rouskin S. Structure of the full SARS-CoV-2 RNA genome in infected cells. *bioRxiv* **2020**, doi:10.1101/2020.06.29.178343.

Loczechin, A.; Séron, K.; Barras, A.; Giovanelli, E.; Belouzard, S.; Chen, Y.-T.; Metzler-Nolte, N.; Boukherroub, R.; Dubuisson, J.; Szunerits, S. Functional Carbon Quantum Dots as Medical Countermeasures to Human Coronavirus. *ACS Appl. Mater. Interfaces* **2019**, *11*, 42964–42974.

Lu, T.; Chen, F. Quantitative Analysis of Molecular Surface Based on Improved Marching Tetrahedra Algorithm. *J. Mol. Graph. Model.* **2012a**, *38*, 314–323.

Lu, T.; Chen, F. Multiwfn: A Multifunctional Wavefunction Analyzer. *J. Comput. Chem.* **2012b**, *33*, 580–592.

Maleki Dizaj, S.; Mennati, A.; Jafari, S.; Khezri, K.; Adibkia, K. Antimicrobial Activity of Carbon-Based Nanoparticles. *Adv. Pharm. Bull.* **2015**, *5*, 19–23.

Mohan, S. V.; Hemalatha, M.; Kopperi, H.; Ranjith, I.; Kumar, A. K. SARS-CoV-2 in Environmental Perspective: Occurrence, Persistence, Surveillance, Inactivation and Challenges. *Chem. Eng. J.* **2021**, *405*, 126893.

Morawska, L.; Cao, J. Airborne Transmission of SARS-CoV-2: the World Should Face the Reality. *Environ. Int.* **2020**, *139*, 105730.

Mottier, A.; Mouchet, F.; Laplanche, C.; Cadarsi, S.; Lagier, L.; Arnault, J.-C.; Girard, H. A.; León, V.; Vázquez, E.; Sarrieu, C.; Pinelli, É.; Gauthier, L.; Flahaut, E. Surface Area of

Carbon Nanoparticles: A Dose Metric for a More Realistic Ecotoxicological Assessment.
*Nano Lett.* **2016**, *16*, 3514–3518.

Palmieri, V.; Papi, M. Can Graphene Take Part in the Fight Against COVID-19? *Nano Today* **2020**, *33*, 100883.

Pan, B.; Xing, B. Adsorption Mechanisms of Organic Chemicals on Carbon Nanotubes. *Environ. Sci. Technol.* **2008**, *42*, 9005–9013.

Patel, K. D.; Singh, R. K.; Kim, H. W. Carbon-based Nanomaterials as All Emerging Platform for Theranostics. *Mater. Horiz.* **2019**, *6*, 434–469.

Puzyn, T.; Rasulev, B.; Gajewicz, A.; Hu, X.; Dasari, T. P.; Michalkova, A.; Hwang, H.-M.; Toropov, A.; Leszczynska, D.; Leszczynski, J. Using Nano-QSAR to Predict the Cytotoxicity of Metal Oxide Nanoparticles. *Nat. Nanotechnol.* **2011**, *6*, 175–178.

Rompelberg, C.; Heringa, M. B.; van Donkersgoed, G.; Drijvers, J.; Roos, A; Westenbrink, S.; Peters, R.; van Bemmel, G.; Brand, W.; Oomen, A. G. Oral Intake of Added Titanium Dioxide and Its Nanofraction from Food Products, Food Supplements and Toothpaste by the Dutch Population. *Nanotoxicology* **2016**, *10*, 1404–1414.

Sánchez-López, E.; Gomes, D.; Esteruelas, G.; Bonilla, L.; Lopez-Machado, A. L.; Galindo, R.; Cano, A.; Espina, M.; Ettcheto, M.; Camins, A.; Silva, A. M.; Durazzo, A.; Santini, A.; Garcia, M. L.; Souto, E. B. Metal-Based Nanoparticles as Antimicrobial Agents: An Overview. *Nanomaterials* **2020**, *10*, 292.

Serrano-Aroca, Á.; Takayama, K.; Tuñón-Molina, A.; Seyran, M.; Hassan, S. S.; Pal Choudhury, P.; Uversky, V. N.; Lundstrom, K.; Adadi, P.; Palù, G.; Aljabali, A. A. A.; Chauhan, G.; Kandimalla, R.; Tambuwala, M. M.; Lal, A.; Abd El-Aziz, T. M.; Sherchan, S.; Barh, D.; Redwan, E. M.; Bazan, N. G.; Mishra, Y. K.; Uhal, B. D.; Brufsky, A. Carbon-Based Nanomaterials: Promising Antiviral Agents to Combat COVID-19 in the Microbial-Resistant Era. *ACS Nano.* 2021, doi: 10.1021/acsnano.1c00629.

Shin, M. D.; Shukla, S.; Chung, Y. H.; Beiss, V.; Chan, S. K.; Ortega-Rivera, O. A.; Wirth, D. M.; Chen, A.; Sack, M.; Pokorski, J. K.; Steinmetz, N. F. COVID-19 Vaccine Development and a Potential Nanomaterial Path Forward. *Nat. Nanotechnol.* 2020, 15, 646–655.

Slot, E.; Hogema, B. M.; Reusken, C. B. E. M.; Reimerink, J. H.; Molier, M.; Karregat, J. H. M.; IJlst, J.; Novotný, V. M. J.; van Lier, R. A. W.; Zaaijer, H. L. Low SARS-CoV-2 Seroprevalence in Blood Donors in the Early COVID-19 Epidemic in the Netherlands. *Nat. Commun.* 2020, 11, 5744.

Snape, M. D.; Viner, R. M. COVID-19 in Children and Young People. *Science* 2020, 370, 286-288.

Talebian, S.; Wallace, G. G.; Schroeder, A.; Stellacci, F.; Conde, J. Nanotechnology-Based Disinfectants and Sensors for SARS-CoV-2. *Nat. Nanotechnol.* 2020, 15, 618–621.

Vermisoglou, E.; Panáček, D.; Jayaramulu, K.; Pykal, M.; Frébort, I.; Kolář, M.; Hajdúch, M.; Zbořil, R.; Otyepka, M. Human Virus Detection with Graphene-Based Materials. *Biosens. Bioelectron.* 2020, 166, 112436.

Wang, Y.; Chen, J.; Wei, X.; Hernandez Maldonado, A. J.; Chen, Z. Unveiling Adsorption Mechanisms of Organic Pollutants onto Carbon Nanomaterials by Density Functional Theory Computations and Linear Free Energy Relationship Modeling. *Environ. Sci. Technol.* **2017** *51*, 11820–11828.

Yang, K.; Xing, B. Adsorption of Organic Compounds by Carbon Nanomaterials in Aqueous Phase: Polanyi Theory and its Application. *Chem. Rev.* **2010**, *110*, 5989–6008.

Zhang, K.; Zheludev, I. N.; Hagey, R. J.; Wu, M. T.-P.; Haslecker, R.; Hou, Y. J.; Kretsch, R.; Pintilie, G. D.; Rangan, R.; Kladwang, W.; Li, S.; Pham, E. A.; Bernardin-Souibgui, C.; Baric, R. S.; Sheahan, T. P.; D'Souza, V.; Glenn, J. S.; Chiu, W.; Das, R. Cryo-Electron Microscopy and Exploratory Antisense Targeting of the 28-kDa Frameshift Stimulation Element from the SARS-CoV-2 RNA Genome. *bioRxiv: the preprint server for biology* **2020**.

Figure Caption

Fig. 1. Use of compositional and combinatorial ENM libraries, including metals, metal oxides, carbon nanotubes, and silica-based nanomaterials, to perform mechanism-based toxicological screening that links material composition and systematic variation of specific properties to biological outcomes.

Fig. 2. Structure, morphology, and character of the studied models of carbon nanoparticles.

Fig. 3. Optimized structures of the complexes of the CNPs with the SARS-CoV-2 RNA fragment (abbreviated as covRNA) obtained after the annealing/geometry optimization procedure (A) and

the calculated total potential energy interaction energies ($E_{\text{int}}$), 'van der Waals' interaction energies, and electrostatic interaction energies between the CNPs and the SARS-CoV-2 RNA fragment using the simulated annealing method. The first 7 pictures (A) and the orange block (B) represent the fullerenes, the middle 8 pictures (A) and blue block (B) represent the nanotubes, the last 2 pictures (A) and the pink block (B) represent the graphenes.

Table 1. Molecular parameters of the carbon nanoparticles.

<table>
<thead>
<tr>
<th>CNPs *</th>
<th>Chemical formula</th>
<th>Mol Weight (g/mol)</th>
<th>Overall surface area ($\text{nm}^2$)</th>
<th>Volume ($\text{nm}^3$)</th>
<th>Specific surface area ($\text{m}^2$/g)</th>
<th>Sum of Degrees</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{20}$</td>
<td>C20</td>
<td>240.220</td>
<td>1.859</td>
<td>0.234</td>
<td>4659.147</td>
<td>60</td>
</tr>
<tr>
<td>$C_{36}$</td>
<td>C36</td>
<td>432.396</td>
<td>2.678</td>
<td>0.404</td>
<td>3729.094</td>
<td>108</td>
</tr>
<tr>
<td>$C_{60}$</td>
<td>C60</td>
<td>720.660</td>
<td>3.812</td>
<td>0.645</td>
<td>3185.747</td>
<td>180</td>
</tr>
<tr>
<td>$C_{70}$</td>
<td>C70</td>
<td>840.770</td>
<td>4.325</td>
<td>0.750</td>
<td>3098.086</td>
<td>210</td>
</tr>
<tr>
<td>$C_{240}$</td>
<td>C240</td>
<td>2882.640</td>
<td>13.127</td>
<td>2.538</td>
<td>2742.369</td>
<td>720</td>
</tr>
<tr>
<td>$C_{20}@C_{60}$</td>
<td>C80</td>
<td>960.880</td>
<td>4.340</td>
<td>0.824</td>
<td>2720.323</td>
<td>240</td>
</tr>
<tr>
<td>$C_{20}@C_{60}@C_{240}$</td>
<td>C320</td>
<td>3843.520</td>
<td>10.283</td>
<td>3.047</td>
<td>1611.094</td>
<td>960</td>
</tr>
<tr>
<td>SCNT (10,0)</td>
<td>C2010H22</td>
<td>24164.286</td>
<td>108.576</td>
<td>21.858</td>
<td>2705.906</td>
<td>6010</td>
</tr>
<tr>
<td>SCNT (6,6)</td>
<td>C2100</td>
<td>25223.100</td>
<td>113.148</td>
<td>22.822</td>
<td>2701.464</td>
<td>6288</td>
</tr>
</tbody>
</table>

<table>
<tr><td>SCNT (28,0)</td><td>C5846</td><td>70291.912</td><td>314.016</td><td>62.889</td><td>2690.280</td><td>1098</td></tr>
<tr><td>DCNT (10,0)</td><td>C2282H58</td><td>29767.822</td><td>65.384</td><td>22.949</td><td>1322.735</td><td>1495</td></tr>
<tr><td>DCNT (6,6)</td><td>C2080H68</td><td>27148.064</td><td>61.193</td><td>21.367</td><td>1357.418</td><td>1454</td></tr>
<tr><td>TCNT (10,0)</td><td>C2146H130</td><td>28069.814</td><td>50.583</td><td>21.944</td><td>1085.212</td><td>2173</td></tr>
<tr><td>NR (6,6)</td><td>C2160H144</td><td>28266.192</td><td>92.495</td><td>23.584</td><td>1970.605</td><td>3204</td></tr>
<tr><td>SCNT (16,0)@C₆₀</td><td>C2108H32</td><td>27415.828</td><td>109.455</td><td>22.416</td><td>2404.270</td><td>1091</td></tr>
<tr><td>MG</td><td>C2046H126</td><td>26763.882</td><td>124.221</td><td>23.031</td><td>2795.087</td><td>6012</td></tr>
<tr><td>BG</td><td>C2112H180</td><td>27677.568</td><td>77.180</td><td>22.648</td><td>1679.300</td><td>6156</td></tr>
</table>

*= more details in Fig. 2.

![](./images/812406166301704194_2.jpg)

Fig. 1. Use of compositional and combinatorial ENM libraries, including metals, metal oxides, carbon nanotubes, and silica-based nanomaterials, to perform mechanism-based toxicological screening that links material composition and systematic variation of specific properties to biological outcomes.

![](./images/812406166301704194_3.jpg)

Fig. 2. Structure, morphology, and character of the studied models of carbon nanoparticles.

![](./images/812406166301704194_4.jpg)

Fig. 3. Optimized structures of the complexes of the CNPs with the SARS-CoV-2 RNA fragment (abbreviated as covRNA) obtained after the annealing/geometry optimization procedure (A) and the calculated total potential energy interaction energies ($E_{\text{int}}$), 'van der Waals' interaction energies, and electrostatic interaction energies between the CNPs and the SARS-CoV-2 RNA fragment using the simulated annealing method. The first 7 pictures (A) and the orange block (B) represent the fullerenes, the middle 8 pictures (A) and blue block (B) represent the nanotubes, the last 2 pictures (A) and the pink block (B) represent the graphenes.

Graphical Abstract

![](./images/812406166301704194_5.jpg)

### Credit Author Statement

Fan Zhang: Conceptualization, Methodology, Investigation, Data curation, Formal analysis, Writing-Original draft preparation, Visualization, Funding acquisition. Zhuang Wang: Conceptualization, Formal analysis, Resources, Writing - Review & Editing, Funding acquisition, Project administration. Martina G. Vijver: Conceptualization, Formal analysis, Writing - Review & Editing, Supervision, Funding acquisition, Project administration. Willie J. G. M. Peijnenburg: Conceptualization, Writing - Review & Editing, Supervision, Funding acquisition, Project administration.

### Declaration of interests

☒ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

☐The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

![](./images/812406166301704194_6.jpg)

**Highlights:**

-   This is the first QSAR study to assess interaction of CNPs with a SARS-CoV-2 RNA fragment
-   The developed QSARs on Eint show high goodness-of-fit and robustness
-   Two nano-structural descriptors were found to be decisive factors controlling Eint
-   Electrostatic interaction could be the predominant driving force for the interactions
-   QSAR is a useful tool to investigate nanotechnology impacts on the novel coronavirus