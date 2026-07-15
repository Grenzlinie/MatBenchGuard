# Thermodynamic modeling of the LiCl-KCl-LaCl₃ system with Bayesian model selection and uncertainty quantification

Rushi Gong¹,*, Shun-Li Shang¹,*, Vitaliy G. Goncharov²,³, Cillian Cockrell⁴,⁵, Kostya Trachenko⁵, Paul A. Bingham⁶, Xiaofeng Guo²,³, and Zi-Kui Liu¹

¹Department of Materials Science and Engineering, The Pennsylvania State University, University Park, PA 16802, United States

²Department of Chemistry, Washington State University, Pullman, Washington, 99164, United States

³Materials Science and Engineering Program, Washington State University, Pullman, Washington 99164, United States

⁴Nuclear Futures Institute, Bangor University, Bangor, LL57 1UT, United Kingdom

⁵School of Physical and Chemical Sciences, Queen Mary University of London, Mile End Road, London, E1 4NS, United Kingdom

⁶Materials and Engineering Research Institute, Sheffield Hallam University, Sheffield, S1 1WB, United Kingdom

*Corresponding authors

Corresponding emails: rfg5281@psu.edu (R. S. Gong), sus26@psu.edu (S. L. Shang)

### Abstract

Chloride molten salts are increasingly used in pyroprocessing techniques for the separation of lanthanides. Understanding thermodynamic properties of these salts is essential to predict their critical characteristics and optimize the separation process. Several thermodynamic models, including the associate model, the two-sublattice ionic model, and the modified quasichemical model with quadruplet approximation (MQMQA), have been utilized in the literature to capture the complexity of molten salts. In the present work, the Bayes factor is used to guide the model selection process for thermodynamic modeling of the KCl-LaCl₃ system and provide statistical comparison of various models. The results indicate that the MQMQA model is the most favorable one based on available data. The LiCl-KCl-LaCl₃ system has been further modelled with uncertainty quantification (UQ) using MQMQA with the thermodynamic properties of compounds in KCl-LaCl₃ predicted by the quasiharmonic approach in terms of first-principles phonon calculations as a function of temperature. The calculated phase stability shows excellent agreement with experimental data, indicating that an appropriate thermodynamic model is important for accurately predicting critical characteristics of complex molten salts.

Keywords: Molten salts, Lanthanides, CALPHAD modeling, Phonon, DFT, Bayesian model selection

Highlights:

- Temperature-dependent thermodynamic properties for compounds in KCl-LaCl₃ by DFT-based phonon calculations.

- Bayes factor to select thermodynamic model for the KCl-LaCl₃ liquid.

- Thermodynamic modeling with UQ of LiCl-KCl-LaCl₃ with MQMQA used for liquid.

## 1 Introduction

Chloride molten salts have gained significant attention for their potential applications in advanced nuclear reactors and pyroprocessing techniques [1–3]. Effective separation of fission products, such as lanthanides using pyroprocessing techniques, requires a comprehensive understanding of their thermodynamic properties of molten salts. The CALPHAD (CALculation of PHAse Diagram) modeling approach [4–6] is an effective method for investigating phase stability and thermodynamic properties in multicomponent systems. For modeling of complex molten salts, various thermodynamic models within the CALPHAD framework have been developed to describe intricate behaviors such as short-range ordering. These models include the associate model [7], the two-sublattice ionic model [8], and the modified quasichemical model with quadruplet approximation (MQMQA) [9,10]. All of them have been applied in CALPHAD modeling of molten salts [11–16]. However, systematical comparison of these models and selection of the most appropriate model for molten salts remain challenges, due to different physical interpretations and the complexities involved in quantifying model performance.

Several model selection criteria have been employed in the CALPHAD modeling approach. For instance, the corrected Akaike information criterion (AICc) [17] has been implemented in the open-source software ESPEI [18], facilitating the comparison and selection of Gibbs energy models. Shang et al. [19] utilized the AICc to select models aiming at fitting phonon and thermal electron contributions to free energy. Paulson et al. [20] used Bayes factor [21] to select heat capacity models for the alpha, beta and liquid phases of hafnium, while Honarmandi et al. [22]

used Bayes factor and Bayesian model average to compare models in the Hf-Si system. These studies highlight the utility of statistical comparison in guiding model selection in CALPHAD modeling.

In the present work, thermodynamic modeling of the LiCl-KCl-LaCl₃ system was performed using experimental data in the literature, supplemented with thermochemical data of compounds predicted by first-principles calculations based on density functional theory (DFT). The open-source software tools of ESPEI [18] and PyCalphad [23] were employed for the modeling process. The recent implementation of MQMQA [24] facilitates Bayesian parameter estimation, uncertainty quantification (UQ), and Bayesian model selection in modeling molten salts [16]. Four candidate thermodynamic models for the KCl-LaCl₃ liquid were compared in the present work. The optimal model for this system is identified using Bayes factor, leading to a further model of the ternary LiCl-KCl-LaCl₃ system, which demonstrates an excellent agreement with experimental data reported in the literature. The present work compares thermodynamic models commonly used in CALPHAD modeling for liquid, providing insights into an effective model selection strategy.

## 2 Literature review of the KCl-LaCl₃ and LiCl-KCl-LaCl₃ systems

The LiCl-KCl-LaCl₃ system contains the liquid phase, three binary compounds of LiCl, KCl, and LaCl₃, and two ternary compounds of K₂LaCl₅ and K₃La₅Cl₁₈ as summarized by Hao et al. [14]. K₂LaCl₅ is with a Pnma structure measured by Meyer et al. [25]. Seifert et al. [26] determined the

structure of $K_3La_5Cl_{18}$ with a space group of $P6_3/m$ through X-ray diffraction. The values of formation enthalpy of $K_2LaCl_5$ and $K_3La_5Cl_{18}$ were measured by Seifert et al. [26] using solution calorimetry. Reuter and Seifert [27] reported the values of heat capacity of $K_2LaCl_5$ and $K_3La_5Cl_{18}$ using differential scanning calorimetry (DSC). Gaune-Escard and Rycerz [28] also measured the heat capacity of $K_3La_5Cl_{18}$ using DSC. Papatheodorou and Ostvold [29] reported mixing enthalpy in liquid in $KCl-LaCl_3$ through calorimetric experiments. Qiao et al. [30] utilized the differential thermal analysis (DTA) techniques to determine melting and phase transition temperatures. In the $KCl-LaCl_3$ system, Song and Zheng [31] measured liquidus by DTA. Seifert et al. [26] measured phase boundaries in the $LaCl_3$-rich range by DTA.

In the ternary $LiCl-KCl-LaCl_3$ system, Bagri and Simpson [32] and Samin et al. [33] reported activity coefficient values for $LaCl_3$ in molten $LiCl-KCl$ eutectic salt using electromotive force measurements and cyclic voltammetry, respectively. Regarding the phase diagram, Song and Zheng [31] reported the liquidus projection and six isopleths. Two research works, by Nakamura el al. [34] and Krishnan et al. [35], constructed the pseudo-binary phase diagram from the LiCl-KCl eutectic to 25 mol% of $LaCl_3$ in the $LiCl-KCl$ eutectic through DSC. Mixing enthalpies of $LaCl_3$ in $LiCl-KCl$ eutectic with the $LaCl_3$ concentration from 0 to ~80 mol% have also been studied by Goncharov et al. [36], using both high-temperature drop calorimetry and *ab initio* molecular dynamics. Previously, high-temperature drop calorimetry was also used for examining other similar molten chloride systems [36–38], with recent revisions in the experimental method

[39,40]. These newly obtained mixing enthalpy values of LaCl₃-(LiCl-KCl) were used in this work for benchmarking our modeling results.

## 3 Methodology

### 3.1 DFT-based first-principles calculations

#### 3.1.1 Helmholtz energy at finite temperatures

The Helmholtz energy $F(V,T)$ as a function of volume ($V$) and temperature ($T$) in terms of the DFT-based quasiharmonic approximation (QHA) can be determined by [41],

$$
F(V,T) = E(V) + F_{el}(V,T) + F_{vib}(V,T)
$$
**Eq. 1**

where $E(V)$ is static energy at 0 K without the zero-point vibrational energy, and $F_{el}(V,T)$ and $F_{vib}(V,T)$ represent the temperature-dependent thermal electron contribution and the vibrational contribution, respectively. In the present work, a four-parameter Birch-Murnaghan (BM4) equation of state (EOS) [41] as shown in **Eq. 2** was used to obtain equilibrium properties at zero external pressure ($P=0$ GPa), including the static energy $E_0$, volume ($V_0$), and bulk modulus ($B_0$) and its pressure derivate ($B'$).

$$
E(V) = a + bV^{-2/3} + cV^{-4/3} + dV^{-2}
$$
**Eq. 2**

where $a$, $b$, $c$, and $d$ are fitting parameters.

$F_{el}(V,T)$ is calculated by the following equation [42],

$$F_{el}(V,T) = E_{el}(V,T) - T \cdot S_{el}(V,T) \tag{Eq. 3}$$

where $E_{el}$ and $S_{el}$ are the internal energy and entropy due to thermal electron excitations, respectively, which can be obtained by the electronic density of states (DOS). Note that the thermal electronic contribution to Helmholtz energy is negligible for non-metals due to the Fermi level in the band gap. $F_{vib}(V,T)$ can be obtained by the following equation [42,43],

$$F_{vib}(V,T) = k_B T \sum_q \sum_j \ln\left\{2\sinh\left[\frac{\hbar\omega_j(q,V)}{2k_B T}\right]\right\} \tag{Eq. 4}$$

where $\omega_j(q,V)$ represents the frequency of the $j^{th}$ phonon mode at wave vector $q$ and volume $V$, and $\hbar$ the reduced Planck constant.

### 3.1.2 Details of first-principles calculations

All DFT-based first-principles and phonon calculations in the present work were performed by the Vienna *ab initio* Simulation Package (VASP) [44]. The projector augmented-wave method (PAW) was used to account for electron-ion interactions in order to increase computational efficiency compared with the full potential methods [45,46]. Electron exchange and correlation effects were described using the generalized gradient approximation (GGA) as implemented by Perdew, Burke,

and Ernzerhof (PBE) [47]. The plane-wave basis cutoff energy was 262 eV for structural relaxations and 520 eV for the final static calculations of total energy. The convergent criterion of electronic self-consistency was set as $5×10^{-6}$ eV/atom for relaxations and static calculations. Seifert et al. [26] reported that $K_3La_5Cl_{18}$ possesses the symmetry of P6₃/m with three Wyckoff sites of 2b, 2c, and 6h. However, the occupancy of the 2b site is less than 1, while the 2c site is occupied by both K and La atoms. Considering these, ATAT [48] was used to search for all possible configurations under these conditions and 9 symmetry inequivalent configurations were found in terms of a 26-atom unit cell. The configuration with the lowest energy was predicted using DFT calculations. Phonon calculations were performed using the supercell method. Table 1 provides detailed settings for DFT-based first-principles and phonon calculations, including reciprocal k-points meshes and supercell sizes for phonon calculations, which ensures the convergence and accuracy of the DFT calculations.

## 3.2 CALPHAD modeling

### 3.2.1 Compounds

In the present work, the ternary compounds in the $LiCl-KCl-LaCl_3$ system are considered as stoichiometric compounds, including $K_2LaCl_5$ and $K_3La_5Cl_{18}$ (as listed in Sec. 2). Thermodynamic functions of the binary endmembers $KCl$ and $LaCl_3$, are sourced from the JANAF tables [49] and the SSUB database [50]. The Gibbs energy for a given compound is expressed as:

$$
G_{m}=\Delta_{f} H_{m}^{0}(298.15)-T S_{m}^{0}(298.15)+\int_{298.15}^{T} C_{P, m} d T-T \int_{298.15}^{T} \frac{C_{P, m}}{T} d T
$$

where $\Delta_{f} H_{m}^{0}(298.15)$ represents the standard formation enthalpy, $S_{m}^{0}(298.15)$ the standard entropy at 298.15 K, and $C_{P, m}$ the heat capacity. For ternary compounds, their thermodynamic data including enthalpy, entropy, and heat capacity are obtained through DFT-based first-principles and phonon calculations, as presented in Sec.4.1.

### 3.2.2 Four thermodynamic models for liquid in KCl-LaCl₃

Regarding the liquid phase, we consider four frequently used models in the literature to describe complex molten salts, including the associate model [7], the two-sublattice ionic model [8], and the MQMQA [9,10] with two sets of coordination numbers.

The species KCl and LaCl₃ are assumed in the associate model [7], since no observation of other complex associates exists in the literature. The Gibbs energy of liquid can be expressed as:

$$
\begin{aligned}
G_{m}= & y_{K C l}{ }^{o} G_{K C l}^{\text {Liquid }}+y_{\text {LaCl}_{3}}{ }^{o} G_{\text {LaCl}_{3}}^{\text {Liquid }}+R T\left(y_{K C l} l n y_{K C l}+y_{\text {LaCl}_{3}} l n y_{\text {LaCl}_{3}}\right) \\
& +y_{K C l} y_{\text {LaCl}_{3}} \sum_{v=0} L_{K C l, L a C l_{3}}^{v}\left(y_{K C l}-y_{\text {LaCl}_{3}}\right)^{v}
\end{aligned}
$$

where $y_{i}$ is the mole fraction of specie $i$ (= KCl or LaCl₃), ${ }^{o} G_{i}^{\text {Liquid }}$ the Gibbs energy of species $i$, $R$ the gas constant, and $L_{K C l, L a C l_{3}}^{v}$ the $v^{\text {th }}$ interaction parameter between KCl and LaCl₃.

In the two-sublattice ionic model [8], the liquid phase in KCl-LaCl₃ can be described as:

$$(K^{+}, La^{3+})_P(Cl^-)_Q \tag{Eq. 7}$$

where the cations and anions are separated into two sublattices. The site ratios of P and Q follow the following relationships to maintain charge neutrality:

$$P = y_{Cl^-} = 1 \tag{Eq. 8}$$

$$Q = y_{K^+} + y_{La^{3+}} \tag{Eq. 9}$$

where $y_i$ represents site fraction of ion $i$, i.e., the mole fraction in each sublattice. The Gibbs energy function can be expressed as:

$$G_m = y_{K^+} {^oG_{KCl}^{Liquid}} + y_{La^{3+}} {^oG_{LaCl_3}^{Liquid}} + RT(y_{K^+}ln{y_{K^+}} + y_{La^{3+}}ln{y_{La^{3+}}}) + {^{xs}G_m} \tag{Eq. 10}$$

where $^{xs}G_m$ represents the excess Gibbs energy and can be described based on the Redlich-Kister polynomial [51], similarly as in **Eq. 6**:

$$^{xs}G_m = y_{K^+}y_{La^{3+}} \sum_{\nu=0} L_{K^+,La^{3+}:Cl^-}^{\nu}(y_{K^+} - y_{La^{3+}})^{\nu} \tag{Eq. 11}$$

where $L_{K^+,La^{3+}:Cl^-}^{\nu}$ is the $\nu^{th}$ interaction parameter between $K^+$ and $La^{3+}$.

The MQMQA [9,10] describes the KCl-LaCl₃ liquid phase by assuming interactions between the quadruplets of K₂/Cl₂, La₂/Cl₂, and KLa/Cl₂. Coordination numbers Z are defined to describe the second nearest neighbors (SNN) coordination number of the species i (= K, La, or Cl) in the quadruplets. Z of anions can be calculated from **Eq. 12** to maintain charge neutrality,

$$
\frac{q_{\mathrm{K}}}{Z_{\mathrm{KLa} / \mathrm{ClCl}}^{\mathrm{La}}}+\frac{q_{\mathrm{La}}}{Z_{\mathrm{KLa} / \mathrm{ClCl}}^{\mathrm{La}}}=2 \times \frac{q_{\mathrm{Cl}}}{Z_{\mathrm{AB} / \mathrm{ClCl}}^{\mathrm{Cl}}}
$$

**Eq. 12**

where $q_i$ represents the charges of ion i (= K, La, or Cl). Two sets of coordination numbers were applied to KLa/ClCl in the present work as summarized in Table 2. The selection of MQMQA-M3 is based on Sun et al.'s modeling for KCl-NdCl₃ [52], while the MQMQA-M4 is based on the MSTDB-TC for KCl-LaCl₃ [15].

In MQMQA, the excess Gibbs energy $G^{excess}$ is related to the formation Gibbs energy of the quadruplet, $\Delta g_{quadruplet}^{ex}$,

$$
\left(\mathrm{K}_{2} / \mathrm{Cl}_{2}\right)_{\text {quad }}+\left(\mathrm{La}_{2} / \mathrm{Cl}_{2}\right)_{\text {quad }}=2\left(\mathrm{KLa} / \mathrm{Cl}_{2}\right)_{\text {quad }} \quad \Delta g_{\mathrm{AB} / \mathrm{Cl}_{2}}^{ex}
$$

**Eq. 13**

where $\Delta g_{\mathrm{KLa} / \mathrm{Cl}_{2}}^{ex}$ represents the Gibbs energy change when forming the quadruplets and can be described by:

$$
\Delta g_{\mathrm{KLa} / \mathrm{Cl}_{2}}^{ex}=\Delta g_{\mathrm{KLa} / \mathrm{Cl}_{2}}^{o}+\sum_{(i+j) \geq 1} g_{\mathrm{KLa} / \mathrm{Cl}_{2}}^{i j} \chi_{\mathrm{KLa} / \mathrm{Cl}_{2}}^{i} \chi_{\mathrm{LaK} / \mathrm{Cl}_{2}}^{j}
$$

**Eq. 14**

where $g_{\mathrm{KLa/Cl_2}}^{ij}$ is a function which is dependent of temperature. $\chi_{\mathrm{KLa/Cl_2}}^i$ and $\chi_{\mathrm{LaK/Cl_2}}^j$ are composition-dependent terms, defined as:

$$
\chi_{\mathrm{KLa/Cl_2}}^i = \frac{X_{\mathrm{K_2/Cl_2}}}{X_{\mathrm{K_2/Cl_2}} + X_{\mathrm{KLa/Cl_2}} + X_{\mathrm{La_2/Cl_2}}}
$$
**Eq. 15**

where $X_{\mathrm{KLa/Cl_2}}$ is the mole fraction of the formula $(\mathrm{KLa/Cl_2})_{\mathrm{quad}}$.

All model parameters in the present work were simultaneously optimized through the Bayesian approach using the Markov Chain Monte Carlo (MCMC) method [18] as implemented in ESPEI [18]. The input data included primarily experimental phase equilibrium data for two or more co-existing phases, mixing enthalpy data, and activity coefficient data from the literature. For stochiometric compounds, their thermochemical data from DFT-based calculations were also used as input. In the present work, each model parameter employed two Markov chains with a standard derivation of 0.1 when initializing its Gaussian distribution. During the modeling process, the chain values can be tracked and the MCMC processes were performed until the model parameters converged.

### 3.3 Bayesian statistics and model selection

ESPEI [18] uses Bayesian parameter estimation to optimize model parameters [53],

$$
p(\theta|D,M) = \frac{p(D|\theta,M)p(\theta|M)}{p(D|M)} \qquad \text{Eq. 16}
$$

where $\theta$'s are the model parameters, $M$ the model, and $D$ the input experimental data. In *Eq. 16*, the posterior $p(\theta|D,M)$ is the probability of model parameters conditioned on data, the likelihood $p(D|\theta,M)$ is the probability that the data are described by parameters, the prior $p(\theta|M)$ contains the domain knowledge in the probability distribution of each parameter, and the marginal likelihood (or evidence) $p(D|M)$ is the probability of data being generated by the model. Here, in CALPHAD modeling, model parameters $\theta$ represent coefficients within Gibbs energy functions. These include terms like $L_{KCl,LaCl_3}^v$ from *Eq. 6*, $L_{K^+,La^{3+}:Cl^-}^v$ from *Eq. 11*, or $g_{\text{KLa}/\text{Cl}_2}^{ij}$ from *Eq. 14*. The model $M$ a consists of Gibbs energy expressions that vary depending on the thermodynamic model used, such as associate model (*Eq. 6*), ionic model (*Eq. 10*), or MQMQA (*Eq. 14*). The input data $D$ includes all properties and datasets provided for fitting the Gibbs energy functions.

Bayesian statistics employed in parameter optimization provide a strategy for model selection for CALPHAD modeling [20,22]. Bayes factor usually suggests which model is more favored by the data, which can be evaluated from the ratio of marginal likelihoods for two competing models:

$$
K = \frac{p(D|M_1)}{p(D|M_2)} \qquad \text{Eq. 17}
$$

The marginal likelihood has the desirable qualities of rewarding models that match the data well and penalizing models that are overly complex (i.e., too many degrees of freedom or parameters). The marginal likelihood is determined by:

$$
p(D|M) = \int_{\Omega_{\theta}} p(D|\theta, M)p(\theta|M)d\theta
$$

Eq. 18

where $\Omega_{\theta}$ represents the complete parameter space. The evaluation of marginal likelihood requires computation of an integral with dimension given by the number of parameters, which is typically high-dimensional. The evaluation of the marginal likelihood $p(D|M)$ is usually difficult and computationally expensive. The harmonic mean estimator was hence proposed by Newton and Raftery [54] to estimate the marginal likelihood:

$$
p(D|M) \approx \left[\frac{1}{N}\sum_{i=1}^{N} p(D|\theta_i, M)^{-1}\right]^{-1}
$$

Eq. 19

where $\theta_i$ are samples from the parameters' prior $p(\theta|M)$. Likelihood values can be obtained from the ESPEI MCMC output, which provides statistical comparison of liquid models through Bayes factor.

## 4 Results and discussion

### 4.1 Thermodynamic properties in LiCl-KCl-LaCl₃ by first-principles calculations

Thermodynamic properties of compounds in the KCl-LaCl₃ system were predicted using first-principles calculations. Table 3 summarizes the equilibrium properties of V₀, B₀, and B' at 0 K obtained by DFT-based calculations in comparison with experiments. The present work predicts the bulk modulus B₀ value to be 16.23 GPa for KCl, which is slightly lower than the experimental measurement of 19.7 GPa by Norwood et al. [55]. The equilibrium volume V₀ of LaCl₃ is predicted to be 27.37 Å³/atom in the present work, which is in good agreement with the measured 26.38 Å³/atom by Zachariasen [56]. It indicates that the present DFT calculations provide reliable predictions regarding the equilibrium properties of compounds in the KCl-LaCl₃ system. The present DFT calculations predicted the V₀ of K₂LaCl₅ to be 29.96 Å³/atom and B₀ to be15.89 GPa. For K₃La₅Cl₁₈, the V₀ is reported to be 27.49 Å³/atom and B₀ to be 26.46 GPa, respectively.

Thermodynamic properties at finite temperature are obtained through DFT-based QHA in terms of phonon. Figure 1 compares the predicted values of heat capacity (Cₚ), entropy (S), and enthalpy (H-H₃₀₀) of KCl and LaCl₃ to those from the SGTE database [50]. For KCl, the present QHA results are slightly higher than the SGTE data [50] with a minor difference of about 6% for S. For LaCl₃, the present QHA results slightly underpredict Cp and H-H₃₀₀ compared to SGTE [50], particularly at higher temperature. The differences in Cp for LaCl₃ remain less than 3.2 J/mol-atom-K at high temperature, while the entropy and enthalpy closely match the SGTE values [50]. Figure 2 shows the predicted Cₚ of K₂LaCl₅ and K₃La₅Cl₁₈ in comparison with experiments [27,28], demonstrating an excellent agreement. For example, at 500 K, Cₚ of K₂LaCl from QHA calculations is 26.99 J/mol-K, which is 0.8% and 0.5% higher than 26.77 J/mol-K reported by

Reuter et al. [27] and 0. 26.86 J/mol-K by Gaune-Escard et al. [28], respectively. For $K_3La_5Cl_{18}$, the predicted $C_p$ at 500 K is 25.99 J/mol-K, slightly lower than 26.34 J/mol-K by Reuter et al. [27]. These thermodynamic data of $K_2LaCl_5$ and $K_3La_5Cl_{18}$ obtained from the present DFT calculations are used in the present CALPHAD modeling.

### 4.2 Model selection for the liquid phase in the $KCl-LaCl_3$ system
The $KCl-LaC_3$ system is modeled using four models, i.e., the associate model (Associate-M1), the ionic model (Ionic-M2), and the MQMQA-M3 and the MQMQA-M4 with different coordination numbers. Table 4 summarizes the modeling parameters for these models. Each model has four adjustable parameters, which were optimized by at least 1000 MCMC iterations. This process continued until the posterior probability values from each Markov chain stabilized, i.e., the model parameters converged. Figure 3 compares the phase diagrams calculated from these four models with experimental data [26,31]. It shows that for the liquidus of the KCl-rich region, MQMQA- M3 and MQMQA-M4 provide better agreements with experimental data than Associate-M1 and Ionic-M2. Table 5 lists the invariant reactions predicted by different models in comparison with experimental data [26,31]. In general, all these four models show excellent agreements with the experimental data. Ionic-M2 and MQMQA-M4 slightly overpredict the invariant temperatures compared to those from Asscociate-M1 and MQMQA-M3. Specifically, Ionic-M2 and MQMQA- M4 predict a eutectic temperature of 854 K for the reaction of Liquid$\leftrightarrow$KCl+$K_2LaCl_5$, which is 9 K higher than 845 K reported by Song et al. [31] and 1 K above 853 K by Seifert et al. [26]. For the melting temperature of $K_2LaCl_5$, Ionic-M2 predicts a 917 K, while MQMQA-M4 predicts a

926 K, both are higher than the measured 913 K by Seifert et al.[26] and 916 K by Song et al. [31]. Associate-M1 slightly underpredicts the peritectic temperature of the reaction Liquid+LaCl₃↔K₃La₅Cl₁₈ at 882 K, which is 3 K lower than the 885 K by Seifert et al. [26]. The mean absolute error (MAE) for predicting these invariant temperatures using Associate-M1 is 2.5 K. MQMQA-M3 provides a good agreement with experimental data, with a slightly lower prediction of eutectic temperature for the reaction Liquid↔K₂LaCl₅+K₃La₅Cl₁₈ at 845 K, which is 6 K lower than 851 K reported by Seifert et al. [26]. Regarding the invariant compositions x(LaCl₃), MQMQA-M3 and MQMQA-M4 offer better predictions with an MAE of 0.017 for both, compared to 0.025 for Associate-M1 and 0.022 for Ionic-M2.

Figure 4 shows the values of mixing enthalpy of liquid at 1173 K calculated using these four models, which are compared with experimental data by Papatheodorou and Ostvold [29]. The comparison indicates that Associate-M1 and Ionic-M2 predict lower mixing enthalpy values than those by MQMQA-M3 and MQMQA-M4. For example, at x(LaCl₃) = 0.496, Associate-M1 predicts -15.469 kJ/mol and Ionic-M2 predicts -15.455 kJ/mol, slightly lower than the -15.097 kJ/mol predicted by MQMQA-M3 and -15.118 kJ/mol by MQMQA-M4. When compared to the mixing enthalpy value of -15.319 kJ/mol reported by Papatheodorou and Ostvold [29], Associate-M1 and Ionic-M2 show a closer alignment, with a difference of 0.9%, compared to a 1.4% difference for MQMQA-M3 and MQMQA-M4. Notably, Associate-M1 and Ionic-M2 align more closely with experimental data [29], particularly in the composition region with x(LaCl₃) > 0.4.

According to phase diagrams (Figure 3) and mixing enthalpy predictions (Figure 4), each model demonstrates a strength in predicting thermodynamic properties of the KCl-LaCl₃ system. Associate-M1 and Ionic-M2 perform well in predicting mixing enthalpy, showing a better match with experimental data as discussed above. However, these two models are less accurate in predicting phase boundaries compared to MQMQA-M3 and MQMQA-M4, especially at the LaCl₃-rich region. Choosing an appropriate model remains challenging, as it requires balancing agreement with all available experimental data. A quantitative method is hence needed to determine the overall favorability for the models of study.

Bayesian parameter estimation through MCMC offers a powerful tool to statistically compare models, as discussed in Sec.3.3. Table 6 lists the estimated marginal likelihood value for each model, indicating that MQMQA-M3 has the highest marginal likelihood value of $\ln(p(D|M_3)) = -370.628$. Consequently, the Bayes factors for the other models were calculated with respect to MQMQA-M3, using the marginal likelihood value of MQMQA-M3 as the numerator shown in *Eq. 17*. The interpretation of the Bayes factor is also included in Table 6 according to the guideline by Kass and Raftery [21]. That is, a $log_{10}$(Bayes factor) value between 0 and 1/2 suggests not worth more than a bare mention in comparing two models even if it points very slightly towards the model at the denominator, a range of 1/2 to 1 indicates substantial evidence in favor of the model at the denominator, 1 to 2 denotes a strong evidence, and a value greater than 2 represents a decisive evidence in favor of the model at the denominator.

It can be seen in included in Table 6 that the Bayes factor $log_{10}K_{M3/M1}$ is 28.016, suggesting decisive evidence of favoring MQMQA-M3 over Associate-M1. This is due to the larger discrepancy in phase boundary predictions from Associate-M1 compared to the experimental phase diagram data shown in Figure 3(a). Regarding the Ionic-M2, the Bayes factor $log_{10}K_{M3/M2}$ = 1.208 indicates strong evidence of favoring MQMQA-M3 over Ionic-M2. Additionally, the Bayes factor comparing the two MQMQA models, $log_{10}K_{M3/M4}$, is 0.344, suggesting that MQMQA-M3 is slightly favored over MQMQA-M4, but not worth a bare mention when comparing these two models. It implies that the choice of these two sets of coordination numbers did not significantly affect the performance of MQMQA models in predicting thermodynamic properties in the KCl-LaCl₃ system.

In summary, Bayesian parameter estimation through MCMC indicates that MQMQA-M3 is more favored, in terms of the input data of phase boundary and mixing enthalpy, over the other three models. This approach provides a robust technique for estimating the marginal likelihood values to assess the probability of data being generated by the model and calculating Bayes factors to statistically compare different models.

### 4.3 Thermodynamic modeling of the LiCl-KCl-LaC₃ system

The MQMQA-M3 is selected for the KCl-LaCl₃ system according to the Bayes factor. The ternary LiCl-KCl-LaCl₃ system is further improved by this model. The other two binary systems of LiCl-

KCl and LiCl-LaCl₃ are taken from the MSTDB-TC [15]. The available experimental data used for CALPHAD modeling include phase boundary data measured by Nakamura et al. [34] and Venkata Krishnan et al. [35], activity coefficient data measured by Bagri and Simpson [32] and Samin et al. [33], and mixing enthalpy data of LaCl₃ in LiCl-KCl eutectic [36]. Table 7 summarizes the modeled ternary interaction parameters after MCMC optimizations.

Thermodynamic properties predicted from the present CALPHAD modeling are compared with available experimental data. In addition, uncertainty quantification (UQ) is performed to propagate parameter uncertainties into property predictions. Figure 5(a) presents the values of activity coefficient of LaCl₃ in the eutectic LiCl-KCl at 773 K, compared with the measurements by Bagri et al. [32] and Samin et al. [33]. The present modeling aligns more closely with the results by Bagri et al. [32], since they provided a larger dataset over a broader composition range than those by Samin et al. [33]. The present CALPHAD model shows a good agreement in the low x(LaCl3) region (x(LaCl3) < 0.015) but slightly overestimates the activity coefficients when x(LaCl3) increases to 0.02. The MAE of the present modeling, compared with values reported by Bagri et al. [32], is 0.0016. The present modeling represents a significant improvement over the previous work by Hao et al. [14], which had a MAE of 0.0078 for the activity coefficients. While MSTDB-TC [15] shows a good agreement in the composition range of x(LaCl3) from 0.022 to 0.027, it has an overall MAE of 0.0024 compared to the values reported by Bagri et al. [32]. The present UQ values were performed using the last 10 MCMC iterations with 60 MCMC samples. The shadow region in Figure 5(b) illustrates the uncertainties in predicting activity coefficients, with a 95%

credible interval (Bayesian credible intervals containing 95% of the activity coefficients samples).

This indicates that the present model has an uncertainty range of -10% to +2% in predicting the activity coefficient values.

Figure 6 shows the mixing enthalpy at 873 K and 1133 K calculated from the present modeling, in comparison with experimental data [36] and modeling results by Hao et al. [14] and MSTDB-TC [15]. In Figure 6(a), at 873 K, all these three modeling works closely match experimental measurements [36] for x(LaCl₃) < 0.2. For example, at x(LaCl₃) = 0.1926, the present modeling predicts a mixing enthalpy of -4231 J/mol, which is 51 J/mol lower than the experimental value [36] of -4180 J/mol. In comparison, Hao et al. [14] predicts -4266 J/mol and MSTDB-TC [15] predicts -4659 J/mol, showing larger differences of 86 J/mol and 389 J/mol, respectively. The MAE of the present modeling in predicting mixing enthalpy at 873 K is 101 J/mol, compared to 120 J/mol for Hao et al. [14] and 312 J/mol for MSTDB-TC [15], highlighting the improved accuracy of the present modeling. Figure 6(a) also shows different shapes of the curves in the LaCl₃-rich region predicted by three modeling works. The present modeling predicts a minimum energy similar to that by MSTDB-TC [15] at around -5650 J/mol, whereas Hao et al. [14] predicts a value of -6186 J/mol, which is around 540 J/mol lower. Note that experiments investigations at 1133 K primarily focus on the LaCl₃-rich region [36].

Figure 6(b) indicates that both Hao et al. [14] and MSTDB-TC [15] predict lower values of mixing enthalpy compared to the present modeling and experiments [36]. The present work improves the accuracy of mixing enthalpy predictions, reducing the MAE to 45.84 J/mol, compared to 159.75 J/mol by Hao et al. [14] and 183.30 J/mol by MSTDB-TC [15]. Figure 6(c) presents the uncertainty quantification of the present modeling in predicting mixing enthalpy, represented by the 95% credible interval. At 873 K, the uncertainty range in predicting mixing enthalpy is around -5% to +5%. At 1133 K, the uncertainty range in predicting mixing enthalpy is around -6% to +6% with all existing experimental data [36] falling within the lower boundary of the uncertainty region. This implies that the present modeling might underestimate the mixing enthalpy, particularly around x(LaCl3) = 0.4. Further experiments or simulations in this composition range are recommended to enhance the accuracy of the present CALPHAD modeling. Figure 7 shows the predicted fraction of each quadruplet in the liquid phase. The peak fractions of the LiLa/ClCl and LaK/ClCl quadruplets appear around $\text{x(LaCl}_3\text{)} = 0.4$, indicating strong short-range ordering (SRO) and consistent with the lowest mixing enthalpy around $\text{x(LaCl}_3\text{)} = 0.4$.

Figure 8 shows the partial isopleth between the eutectic KCl-LiCl and $\text{LaCl}_3$ calculated from the present CALPHAD modeling compared with experimental measurements [34,35], depicting a close match of liquidus and solidus lines. For the eutectic reaction $\text{Liquid}\leftrightarrow\text{KCl+LiCl+K}_2\text{LaCl}_5$, the present modeling predicts a eutectic temperature of 630 K, which is 5 K higher than the 625 K reported by Nakamura et al. [34] and Venkata Krishnan et al. [35]. Similarly, for the reaction $\text{Liquid}\leftrightarrow\text{LiCl+K}_2\text{LaCl}_5\text{+ K}_3\text{La}_5\text{Cl}_{18}$, the present modeling predicts the eutectic temperature at 705

K, which is 3 K higher than the reported 702 K by Nakamura et al. [34] and Venkata Krishnan et al. [35]. Overall, the present modeling of LiCl-KCl-LaCl₃ demonstrates good agreement with experimental data [32–35] regarding phase boundary properties.

## 5 Conclusions

The present work demonstrates an application of Bayesian model selection to identify optimal model for molten salts, focusing on the KCl-LaCl₃ system. Four candidate models are considered, which are the associate model, the two-sublattice ionic model, and two MQMQA models with different coordination numbers. By estimating the marginal likelihoods of each model from MCMC optimization and calculating Bayes factors, one of the MQMQA models is suggested as the most favorable one to describe the KCl-LaCl₃ system based on available input data. Additionally, DFT-based calculations provide important thermodynamic properties for compounds in KCl-LaCl₃, including equilibrium volumes, bulk moduli, enthalpies, entropies, and heat capacities. Furthermore, the ternary LiCl-KCl-LaCl₃ system is modelled, demonstrating a better agreement with experimental data compared to the previous CALPHAD modeling works in the literature. The uncertainty quantification and propagation show that the present modeling provides reliable predictions of activity coefficients and mixing enthalpy when compared with experimental data. The present work indicates that the Bayesian model selection approach facilitates a more rational comparison among different liquid models, enhancing the accuracy of thermodynamic predictions in molten salts.

### Acknowledgments

The authors acknowledge financial supports by the U.S. Department of Energy, Office of Nuclear Energy's Nuclear Energy University Programs via Award No. DE-NE0009288. CC, KT and PAB acknowledge with thanks funding from EPSRC (EP/X011607/1). First-principles calculations were performed partially on the Roar supercomputer at the Pennsylvania State University's Institute for Computational and Data Sciences (ICDS), partially on the resources of the National Energy Research Scientific Computing Center (NERSC) supported by the U.S. Department of Energy, Office of Science User Facility operated under Contract No. DE-AC02-05CH11231, and partially on the resources of ACCESS (previously the Extreme Science and Engineering Discovery Environment, XSEDE) supported by National Science Foundation (NSF) with Grant No. ACI-1548562.

![](./images/1012241974285041669_1.jpg)

Figure 1. Comparison of the present values (blue lines) of heat capacity $C_p$, entropy S, and enthalpy with reference to the value at 300 K (H-H₃₀₀) for (a-c) KCl and (d-f) LaCl₃ from the DFT-based phonon calculations (blue lines) with the SGTE data [50] (red dash lines).

![](./images/1012241974285041669_2.jpg)

Figure 2. Comparison of heat capacity $C_p$ values for (a) $K_2LaCl_5$ and (b) $K_3La_5Cl_{18}$ from the present DFT-based QHA (blue lines) with experiments by Reuter et al. [27] (yellow dash lines) and Gaune-Escard et al. [28] (red circles).

![](./images/1012241974285041669_3.jpg)

Figure 3. Predicted phase diagrams of the $LaCl_3$-KCl system with the liquid phase modeled using (a) associate model (Associate-M1), (b) ionic model (Ionic-M2), (c) MQMQA (MQMQA-M3), and (d) MQMQA (MQMQA-M4) in comparison to experimental data [26,31].

![](./images/1012241974285041669_4.jpg)

Figure 4. Predicted values of mixing enthalpy of the LaCl₃-KCl liquid at 1173K from four models in comparison with experimental data by Papatheodorou and Ostvold [29]. The red dash line represents Associate-M1, the blue dotted line represents Ionic-M2, the black solid line represents MQMQA-M3, and the green dash dotted line represents MQMQA-M4.

![](./images/1012241974285041669_5.jpg)

Figure 5. (a) Activity coefficients of LaCl₃ in KCl-LiCl eutectic at 773 K calculated from the present modeling in comparison with the modeling works from Hao et al. [14] (blue dash line) and MSTDB-TC [15] (purple dash dotted line), experimental measurements by Bagri et al. (red circles) and Samin et al. (green squares). (b) The uncertainty of the present modeling in predicting activity coefficients shown in the grey region using a 95% credible interval in predicting the values.

![](./images/1012241974285041669_6.jpg)

Figure 6. Mixing enthalpy in LiCl-KCl-LaCl₃ at (a) 873 K and (b) 1133 K calculated from the present modeling compared with experimental measurements by Goncharov et al. [36] and the previous modeling works by Hao et al. [14] and MSTDB-TC [15]. (c) The uncertainty of the present modeling in predicting mixing enthalpy shown in the light red region (for 873 K) and the light blue region (for 1133 K) using a 95% credible interval.

![](./images/1012241974285041669_7.jpg)

Figure 7. Precited quadruplet fractions in the LiCl-KCl-LaCl₃ liquid at 1133 K according to the present CALPHAD modeling using MQMQA.

![](./images/1012241974285041669_8.jpg)

Figure 8. Partial isopleth between the eutectic KCl-LiCl and LaCl₃ calculated from the present modeling work in comparison with experimental measurements by Krishnan and Nagarajan (blue squares) [35] and Nakamura and Kurata (green circles) [34].

## 7 Tables and Table Captions

Table 1. Details of the present DFT-based first-principles and phonon calculations for each compound, including space group, total atoms in the supercells, k-point meshes for structure relaxations and the final static calculations (indicated by DFT), supercell sizes for phonon calculations, and k-point meshes for phonon calculations.

<table>
  <thead>
    <tr>
      <th>Phase</th>
      <th>Space Group</th>
      <th>Atoms in crystallographic cell</th>
      <th>k-points for DFT</th>
      <th>Atoms in supercell for phonon</th>
      <th>k-points for phonon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KCl</td>
      <td>Fm$\overline{3}$m</td>
      <td>8</td>
      <td>8×8×8</td>
      <td>64</td>
      <td>3×3×3</td>
    </tr>
    <tr>
      <td>LaCl₃</td>
      <td>P6₃/m</td>
      <td>8</td>
      <td>8×8×12</td>
      <td>64</td>
      <td>2×2×2</td>
    </tr>
    <tr>
      <td>K₂LaCl₅</td>
      <td>Pnma</td>
      <td>32</td>
      <td>7×7×4</td>
      <td>32</td>
      <td>4×4×2</td>
    </tr>
    <tr>
      <td>K₃La₅Cl₁₈</td>
      <td>P3</td>
      <td>26</td>
      <td>8×8×5</td>
      <td>26</td>
      <td>5×5×3</td>
    </tr>
  </tbody>
</table>

Table 2. Coordination numbers used in the present CALPHAD modeling with MQMQA for the liquid phase.

<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th>$Z_{\text{AB/ClCl}}^{\text{A}}$</th>
      <th>$Z_{\text{AB/ClCl}}^{\text{B}}$</th>
      <th>$Z_{\text{AB/ClCl}}^{\text{F}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>K⁺</td>
      <td>K⁺</td>
      <td></td>
      <td>6.0</td>
      <td>6.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>La³⁺</td>
      <td>La³⁺</td>
      <td></td>
      <td>6.0</td>
      <td>6.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>K⁺</td>
      <td>La³⁺</td>
      <td>MQMQA-M3</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>MQMQA-M4</td>
      <td>3.5</td>
      <td>6.0</td>
      <td>2.55</td>
    </tr>
  </tbody>
</table>

Table 3. Predicted equilibrium properties of volume V₀, bulk modulus B₀, and the first derivative of bulk modulus with respect to pressure B' for compounds in the KCl-LaCl₃ system based on the present EOS fitting at 0 K (Eq. 2). Experimental data are also listed for comparison.

<table>
  <thead>
    <tr>
      <th>Compounds</th>
      <th>V₀ (Å³/atom)</th>
      <th>B₀ (GPa)</th>
      <th>B'</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KCl</td>
      <td>32.62</td>
      <td>16.23</td>
      <td>4.67</td>
      <td>This work</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>19.7</td>
      <td></td>
      <td>Norwood et al. [55]</td>
    </tr>
    <tr>
      <td>LaCl₃</td>
      <td>27.37</td>
      <td>29.02</td>
      <td>6.40</td>
      <td>This work</td>
    </tr>
    <tr>
      <td></td>
      <td>26.38</td>
      <td></td>
      <td></td>
      <td>Zachariasen [56]</td>
    </tr>
    <tr>
      <td>K₂LaCl₅</td>
      <td>29.96</td>
      <td>15.89</td>
      <td>5.38</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>K₃La₅Cl₁₈</td>
      <td>27.49</td>
      <td>26.46</td>
      <td>6.35</td>
      <td>This work</td>
    </tr>
  </tbody>
</table>

Table 4. Details of four models and the resulting model parameters in the present work for KCl-LaCl₃.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Models</th>
      <th>Model parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Associate-M1</td>
      <td>$(KCl, LaCl_{3})$</td>
      <td>$L_{KCl,LaCl_{3}}^{0}=-61777.370 + 1.218 * \text{T}$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>$L_{KCl,LaCl_{3}}^{1}=-12634.241 - 1.383 * \text{T}$</td>
    </tr>
    <tr>
      <td>Ionic-M2</td>
      <td>$(K^{+}, La^{3+})_{P}(Cl^{-})_{Q}$</td>
      <td>$L_{K^{+},La^{3+}:Cl^{-}}^{0}=-61720.724 + 5.247 * \text{T}$</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>$L_{K^{+},La^{3+}:Cl^{-}}^{1}=-12786.004 + 3.360 * \text{T}$</td>
    </tr>
    <tr>
      <td>MQMQA-M3</td>
      <td>See Table 2</td>
      <td>$\Delta g_{\text{KLa/Cl}_{2}}^{ex}=-13295.794 - 1.236 * \text{T}$
<br>$+ (-9228.101)\chi_{\text{KLa/Cl}_{2}}$
<br>$+ (-2071.866)\chi_{\text{LaK/Cl}_{2}}$</td>
    </tr>
    <tr>
      <td>MQMQA-M4</td>
      <td>See Table 2</td>
      <td>$\Delta g_{\text{KLa/Cl}_{2}}^{ex}=-13313.121 - 1.333 * \text{T}$
<br>$+ (-9173.701)\chi_{\text{KLa/Cl}_{2}}$
<br>$+ (-1989.647)\chi_{\text{LaK/Cl}_{2}}$</td>
    </tr>
  </tbody>
</table>

Table 5. Predicted invariant equilibria in the KCl-LaCl₃ system by the four models, compared with experimental data.

<table>
  <thead>
    <tr>
      <th colspan="2">Reaction</th>
      <th>x(LaCl₃)</th>
      <th>Temperature (K)</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eutectic</td>
      <td>Liquid↔KCl+K₂LaCl₅</td>
      <td>0.22</td>
      <td>853</td>
      <td>Seifert et al.[26]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.22</td>
      <td>845</td>
      <td>Song et al. [31]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.197</td>
      <td>848</td>
      <td>Associate-M1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.202</td>
      <td>854</td>
      <td>Ionic-M2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.204</td>
      <td>847</td>
      <td>MQMQA-M3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.200</td>
      <td>854</td>
      <td>MQMQA-M4</td>
    </tr>
    <tr>
      <td>Melting</td>
      <td>Liquid↔K₂LaCl₅</td>
      <td>0.333</td>
      <td>913</td>
      <td>Seifert et al.[26]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.333</td>
      <td>916</td>
      <td>Song et al. [31]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.333</td>
      <td>913</td>
      <td>Associate-M1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.333</td>
      <td>917</td>
      <td>Ionic-M2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.333</td>
      <td>915</td>
      <td>MQMQA-M3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.333</td>
      <td>926</td>
      <td>MQMQA-M4</td>
    </tr>
    <tr>
      <td>Eutectic</td>
      <td>Liquid↔K₂LaCl₅+K₃La₅Cl₁₈</td>
      <td>0.51</td>
      <td>851</td>
      <td>Seifert et al.[26]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.485</td>
      <td>852</td>
      <td>Associate-M1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.481</td>
      <td>851</td>
      <td>Ionic-M2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.482</td>
      <td>845</td>
      <td>MQMQA-M3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.49</td>
      <td>851</td>
      <td>MQMQA-M4</td>
    </tr>
    <tr>
      <td>Peritectic</td>
      <td>Liquid+LaCl₃↔K₃La₅Cl₁₈</td>
      <td>0.595</td>
      <td>885</td>
      <td>Seifert et al.[26]</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.565</td>
      <td>882</td>
      <td>Associate-M1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.573</td>
      <td>885</td>
      <td>Ionic-M2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.586</td>
      <td>885</td>
      <td>MQMQA-M3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>0.586</td>
      <td>885</td>
      <td>MQMQA-M4</td>
    </tr>
  </tbody>
</table>

Table 6. Summary of the predicted marginal likelihood and Bayes factor for each model with respect to those of MQMQA-M3, and the suggested strength of evidence according to Kass and Raftery [21].

<table>
<thead>
<tr>
<th>Model name</th>
<th>Marginal<br>likelihood<br>(ln value)</th>
<th>Bayes factor log₁₀K</th>
<th>Strength of evidence</th>
</tr>
</thead>
<tbody>
<tr>
<td>Associate-M1</td>
<td>-435.136</td>
<td>28.016</td>
<td>Decisive</td>
</tr>
<tr>
<td>Ionic-M2</td>
<td>-373.410</td>
<td>1.208</td>
<td>Strong</td>
</tr>
<tr>
<td>MQMQA-M3</td>
<td>-370.628</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>MQMQA-M4</td>
<td>-371.420</td>
<td>0.344</td>
<td>Not worth more than a bare mention</td>
</tr>
</tbody>
</table>

Table 7. Modelled ternary interaction parameters in the LiCl-KCl-LaCl₃ liquid using MQMQA after MCMC optimization in the present work.

<table>
<thead>
<tr>
<th>System</th>
<th>Ternary parameters</th>
</tr>
</thead>
<tbody>
<tr>
<td>LiCl-KCl-LaCl₃</td>
<td>$\Delta g_{\text{LaLi(K)/Cl}_2}^{101} = 10153.591$</td>
</tr>
<tr>
<td></td>
<td>$\Delta g_{\text{KLi(La)/Cl}_2}^{001} = 18921.383 - 12.806 * \text{T}$</td>
</tr>
</tbody>
</table>

## References

[1] K. Sridharan, T. Allen, M. Anderson, M. Simpson, Thermal Properties of LiCl-KCl Molten Salt for Nuclear Waste Separation, (2012). https://doi.org/10.2172/1058922.

[2] A. Mourogov, P.M. Bokov, Potentialities of the fast spectrum molten salt reactor concept: REBUS-3700, Energy Convers. Manag. 47 (2006) 2761-2771. https://doi.org/10.1016/J.ENCONMAN.2006.02.013.

[3] M. Iizuka, T. Koyama, N. Kondo, R. Fujita, H. Tanaka, Actinides recovery from molten salt/liquid metal system by electrochemical methods, J. Nucl. Mater. 247 (1997) 183-190. https://doi.org/10.1016/S0022-3115(97)00096-2.

[4] Z.K. Liu, Computational thermodynamics and its applications, Acta Mater. 200 (2020) 745-792. https://doi.org/10.1016/J.ACTAMAT.2020.08.008.

[5] H.L. Lukas, S.G. Fries, B. Sundman, Computational Thermodynamics: the Calphad Method, Cambridge University Press, Cambridge UK, 2007. https://iopscience.iop.org/article/10.1088/0305-4470/27/7/011.

[6] Z.-K. Liu, Y. Wang, Computational thermodynamics of materials, Cambridge University Press, 2016.

[7] F. Sommer, Association Model for the Description of the Thermodynamic Functions of Liquid Alloys: I. Basic Concepts, Int. J. Mater. Res. 73 (1982) 72-76. https://doi.org/10.1515/IJMR-1982-730202.

[8] M. Hillert, B. Jansson, B. Sundman, J. ågren, A two-sublattice model for molten solutions with different tendency for ionization, Metall. Trans. A. 16 (1985) 261-266. https://doi.org/10.1007/BF02815307.

[9] A.D. Pelton, P. Chartrand, G. Eriksson, The modified quasi-chemical model: Part IV. Two-sublattice quadruplet approximation, Metall. Mater. Trans. A 2001 326. 32 (2001) 1409-1416. https://doi.org/10.1007/S11661-001-0230-7.

[10] A.D. Pelton, Phase diagrams and thermodynamic modeling of solutions, Elsevier, 2014.

[11] L. Rycerz, J. Kapała, B. Salamon, I. Szczygiel, M. Gaune-Escard, Phase diagram and thermodynamic properties of the LaI3-RbI binary system, Calphad. 70 (2020) 101809. https://doi.org/10.1016/J.CALPHAD.2020.101809.

[12] L. Rycerz, J. Kapala, M. Gaune-Escard, Experimental mixing enthalpy and thermodynamic modelling of UCl3-KCl system, J. Mol. Liq. 342 (2021) 116963. https://doi.org/10.1016/J.MOLLIQ.2021.116963.

[13] W. Zhou, Y. Wang, J. Zhang, M. Khafizov, Calculated thermodynamic properties of GdCl3 in LiCl-KCl eutectic molten salt, J. Nucl. Mater. 508 (2018) 40-50. https://doi.org/10.1016/J.JNUCMAT.2018.05.030.

[14] L. Hao, S. Sridar, W. Xiong, Thermodynamic optimization of KCl-LiCl-LaCl3 with ionic

two-sublattice model for liquid, J. Mol. Liq. 400 (2024) 124516.
https://doi.org/10.1016/J.MOLLIQ.2024.124516.

[15] J.C. Ard, J.A. Yingling, K.E. Johnson, J. Schorne-Pinto, M. Aziziha, C.M. Dixon, M.S. Christian, J.W. McMurray, T.M. Besmann, Development of the Molten Salt Thermal Properties Database - Thermochemical (MSTDB-TC), example applications, and LiCl-RbCl and UF3-UF4 system assessments, J. Nucl. Mater. 563 (2022) 153631.
https://doi.org/10.1016/j.jnucmat.2022.153631.

[16] R. Gong, S.L. Shang, Y. Wang, J. Paz Soldan Palma, H. Kim, Z.K. Liu, Revisiting thermodynamics in (LiF, NaF, KF, CrF2)-CrF3 by first-principles calculations and CALPHAD modeling, Calphad. 85 (2024) 102703.
https://doi.org/10.1016/J.CALPHAD.2024.102703.

[17] J.E. Cavanaugh, Unifying the derivations for the Akaike and corrected Akaike information criteria, Stat. Probab. Lett. 33 (1997) 201-208. https://doi.org/10.1016/S0167-7152(96)00128-9.

[18] B. Bocklund, R. Otis, A. Egorov, A. Obaied, I. Roslyakova, Z.K. Liu, ESPEI for efficient thermodynamic database development, modification, and uncertainty quantification: Application to Cu-Mg, MRS Commun. 9 (2019) 618-627.
https://doi.org/10.1557/mrc.2019.59.

[19] S.-L. Shang, R. Gong, M.C. Gao, D.C. Pagan, Z.-K. Liu, Revisiting first-principles thermodynamics by quasiharmonic approach: Application to study thermal expansion of additively-manufactured Inconel 625, Scr. Mater. 250 (2024) 116200.
https://doi.org/10.1016/J.SCRIPTAMAT.2024.116200.

[20] N.H. Paulson, E. Jennings, M. Stan, Bayesian strategies for uncertainty quantification of the thermodynamic properties of materials, Int. J. Eng. Sci. 142 (2019) 74-93.
https://doi.org/10.1016/j.ijengsci.2019.05.011.

[21] R.E. Kass, A.E. Raftery, Bayes Factors, J. Am. Stat. Assoc. 90 (1995) 773-795.
https://doi.org/10.1080/01621459.1995.10476572.

[22] P. Honarmandi, T.C. Duong, S.F. Ghoreishi, D. Allaire, R. Arroyave, Bayesian uncertainty quantification and information fusion in CALPHAD-based thermodynamic modeling, Acta Mater. 164 (2019) 636-647. https://doi.org/10.1016/j.actamat.2018.11.007.

[23] R. Otis, Z.-K. Liu, pycalphad: CALPHAD-based Computational Thermodynamics in Python, J. Open Res. Softw. 5 (2017) 1-11. https://doi.org/10.5334/jors.140.

[24] J. Paz Soldan Palma, R. Gong, B.J. Bocklund, R. Otis, M. Poschmann, M. Piro, S. Shahbazi, T.G. Levitskaia, S. Hu, N.D. Smith, Y. Wang, H. Kim, Z.-K. Liu, S.-L. Shang, Thermodynamic modeling with uncertainty quantification using the modified quasichemical model in quadruplet approximation: Implementation into PyCalphad and ESPEI, Calphad. 83 (2023) 102618. https://doi.org/10.1016/j.calphad.2023.102618.

[25] G. Meyer, E. Hüttl, K2MCl5(M=La-Dy) und Rb2MCl5 (M=La-Eu): Ino-Chloride mit siebenfach koordinierten Seltenen Erden, ZAAC - J. Inorg. Gen. Chem. 497 (1983) 191-

198. https://doi.org/10.1002/ZAAC.19834970218.

[26] H.J. Seifert, H. Fink, G. Thiel, Thermodynamic properties of double chlorides in the systems $ACl/LaCl3$ ($A \equiv Na$, K, Rb, Cs), J. Less-Common Met. 110 (1985) 139–147. https://doi.org/10.1016/0022-5088(85)90315-7.

[27] G. Reuter, H.J. Seifert, The heat capacities of ternary lanthanum chlorides An LaCl3+n from 200 to 770 K and the $\Delta$Cp values for their formation from $nACl + LaCl3$, Thermochim. Acta. 237 (1994) 219–228. https://doi.org/10.1016/0040-6031(94)80178-9.

[28] M. Gaune-Escard, L. Rycerz, Heat Capacity of K3LnCl6Compounds with Ln = La, Ce, Pr, Nd, Zeitschrift Fur Naturforsch. - Sect. A J. Phys. Sci. 54 (1999) 229–235. https://doi.org/10.1515/ZNA-1999-3-412/MACHINEREADABLECITATION/RIS.

[29] G.N. Papatheodorou, T. Ostvold, Thermodynamic studies of binary charge unsymmetrical fused salt systems. Calorimetric and electromotive force measurements of liquid lanthanum(III) chloride-alkali chloride mixtures, J. Phys. Chem. 78 (1974) 181–185. https://doi.org/10.1021/j100595a019.

[30] Z. Qiao, M. Wang, C. Zheng, S. Duan, Measurement and Calculation of ReCl3-LiCl (Re: La, Ce) Phase Diagrams, J. Univ. Sci. Technol. Beijing. 11 (1989) 598–603. https://doi.org/10.13374/J.ISSN1001-053X.1989.06.034.

[31] X. Song, C. Zheng, An Investigation on the Phase Diagram of Ternary System LaCl3-KCl-LiCl（in Chinese), Acta Chim. Sin. 53 (1995) 978–984.

[32] P. Bagri, M.F. Simpson, Determination of activity coefficient of lanthanum chloride in molten LiCl-KCl eutectic salt as a function of cesium chloride and lanthanum chloride concentrations using electromotive force measurements, J. Nucl. Mater. 482 (2016) 248–256. https://doi.org/10.1016/j.jnucmat.2016.10.006.

[33] A. Samin, Z. Wang, E. Lahti, M. Simpson, J. Zhang, Estimation of key physical properties for LaCl3 in molten eutectic LiCl–KCl by fitting cyclic voltammetry data to a BET-based electrode reaction kinetics model, J. Nucl. Mater. 475 (2016) 149–155. https://doi.org/10.1016/J.JNUCMAT.2016.04.002.

[34] K. Nakamura, M. Kurata, Materials Lanthanide Trichloride, 247 (1997) 309–314.

[35] R. Venkata Krishnan, K. Nagarajan, The pseudo-binary phase diagram of LiCl-KCl-LaCl₃ system, (2006). http://inis.iaea.org/Search/search.aspx?orig_q=RN:38095420 (accessed April 22, 2024).

[36] V.G. Goncharov, W. Smith, J. Li, J.A. Eakin, E.D. Reinhart, J. Boncella, L.D. Gibson, V.S. Bryantsev, R. Gong, S.-L. Shang, Z.-K. Liu, H. Xu, A. Clark, X. Guo, Molecular interaction volume model of mixing enthalpy for molten salt system: An integrated calorimetry-model case study of LaCl$_3$-LiCl-KCl, (2024). https://arxiv.org/abs/2408.16943v1 (accessed September 3, 2024).

[37] F. Dienstbach, R. Blachnik, Mischungsenthalpien von geschmolzenen Alkalihalogenid- Lanthanoidenhalogenidsystemen, Zeitschrift Für Anorg. Und Allg. Chemie. 412 (1975) 97–

109. https://doi.org/10.1002/zaac.19754120202.

[38] I. Chojnacka, L. Rycerz, J. Kapala, M. Gaune-Escard, Calorimetric investigation of TmCl3- MCl liquid mixtures (M=Li, Na, K, Rb), J. Mol. Liq. 319 (2020) 113935. https://doi.org/10.1016/J.MOLLIQ.2020.113935.

[39] J. Lonergan, V. Goncharov, M. Swinhart, K. Makovsky, M. Rollog, B. McNamara, R. Clark, D. Cutforth, C. Armstrong, X. Guo, P. Paviet, Thermodynamic investigation of the NaCl-KCl salt system from 25 to 950 °C, J. Mol. Liq. 391 (2023) 122591. https://doi.org/10.1016/J.MOLLIQ.2023.122591.

[40] A.C. Strzelecki, C.B. Cockreham, S.S. Parker, S.C. Mann, C. Lhermitte, D. Wu, X. Guo, M. Monreal, J.M. Jackson, J. Mitchell, H. Boukhalfa, H. Xu, A new methodology for measuring the enthalpies of mixing and heat capacities of molten chloride salts using high temperature drop calorimetry, Rev. Sci. Instrum. 95 (2024) 14103. https://doi.org/10.1063/5.0144910/3023026.

[41] S.L. Shang, Y. Wang, D.E. Kim, Z.K. Liu, First-principles thermodynamics from phonon and Debye model: Application to Ni and Ni3Al, Comput. Mater. Sci. 47 (2010) 1040-1048. https://doi.org/10.1016/j.commatsci.2009.12.006.

[42] Y. Wang, Z.K. Liu, L.Q. Chen, Thermodynamic properties of Al, Ni, NiAl, and Ni3Al from first-principles calculations, Acta Mater. 52 (2004) 2665-2671. https://doi.org/10.1016/j.actamat.2004.02.014.

[43] A. Van de Walle, G. Ceder, The effect of lattice vibrations on substitutional alloy thermodynamics, Rev. Mod. Phys. 74 (2002) 11-45. https://doi.org/10.1103/RevModPhys.74.11.

[44] G. Kresse, J. Furthmuller, J. Furthmüller, J. Furthmuller, J. Furthmüller, J. Furthmueller, J. Furthmuller, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B-Condensed Matter. 54 (1996) 11169-11186. https://doi.org/10.1103/PhysRevB.54.11169.

[45] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B. 50 (1994) 17953-17979. https://doi.org/10.1103/PhysRevB.50.17953.

[46] D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B - Condens. Matter Mater. Phys. 59 (1999) 1758-1775. https://doi.org/10.1103/PhysRevB.59.1758.

[47] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868. https://doi.org/10.1103/PhysRevLett.77.3865.

[48] A. van de Walle, Multicomponent multisublattice alloys, nonconfigurational entropy and other additions to the Alloy Theoretic Automated Toolkit, Calphad Comput. Coupling Phase Diagrams Thermochem. 33 (2009) 266-278. https://doi.org/10.1016/j.calphad.2008.12.005.

[49] M.W. Chase, J.L. Curnutt, J.R. Downey, R.A. Mcdonald, A.N. Syverud, E.A. Valenzuela,

JANAF Thermochemical Tables, 1982 Supplement, J. Phys. Chem. Ref. Data. 11 (2009) 695. https://doi.org/10.1063/1.555666.

[50] SGTE Substance Database - SGTE - Scientific Group Thermodata Europe, (n.d.). https://www.sgte.net/en/neu.

[51] O. Redlich, A.T. Kister, Algebraic Representation of Thermodynamic Properties and the Classification of Solutions, Ind. Eng. Chem. 40 (1948) 345-348. https://doi.org/10.1021/ie50458a036.

[52] Y. Sun, X. Ye, Y. Wang, J. Tan, Optimization and calculation of the NdCl3-MCl (M = Li, Na, K, Rb, Cs) phase diagrams, Calphad Comput. Coupling Phase Diagrams Thermochem. 28 (2004) 109-114. https://doi.org/10.1016/j.calphad.2004.07.004.

[53] A. Gelman, J.B. Carlin, H.S. Stern, D.B. Dunson, A. Vehtari, D.B. Rubin, Bayesian Data Analysis, Chapman and Hall/CRC, New York, 2013. https://doi.org/10.1201/b16018.

[54] M.A. Newton, A.E. Raftery, Approximate Bayesian Inference with the Weighted Likelihood Bootstrap, J. R. Stat. Soc. Ser. B. 56 (1994) 3-48. http://www.jstor.org/stable/2346025 (accessed September 24, 2023).

[55] M.H. Norwood, C. V. Briscoe, Elastic Constants of Potassium Iodide and Potassium Chloride, Phys. Rev. 112 (1958) 45. https://doi.org/10.1103/PhysRev.112.45.

[56] W. Zachariasen, The UC13-type of Crystal Structure, 1947. https://books.google.com/books?hl=en&lr=&id=JN5euEip198C&oi=fnd&pg=PP3&dq=W.+H.+Zachariasen,+J.+Chem.+Phys.+16,+254+1948&ots=5JUWOCYgO3&sig=viArw6bUB5kU9eJGgwhKGP9A8so (accessed May 1, 2024).