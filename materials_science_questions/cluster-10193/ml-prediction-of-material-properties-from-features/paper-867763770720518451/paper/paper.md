# A transferable prediction model of molecular adsorption on metals based on adsorbate and substrate properties

Paolo Restuccia, $^{1, *}$ Ehsan A. Ahmad, $^{2}$ and Nicholas M. Harrison $^{1}$

$^{1}$ Department of Chemistry, Imperial College London, 82 Wood Lane, W12 0BZ London, UK
$^{2}$ Faculty of Engineering and the Environment, University of Southampton, University Road, Southampton SO17 1BJ, UK

Surface adsorption is one of the fundamental processes in numerous fields, including catalysis, environment, energy and medicine. The development of an adsorption model which provides an effective prediction of binding energy in minutes has been a long term goal in surface and interface science. The solution has been elusive as identifying the intrinsic determinants of the adsorption energy for various compositions, structures and environments is non-trivial. We introduce a new and flexible model for predicting adsorption energies to metal substrates. The model is based on easily computed, intrinsic properties of the substrate and adsorbate. It is parameterised using machine learning based on first-principles calculations of probe molecules (e.g., $\ce{H2O}$, $\ce{CO2}$, $\ce{O2}$, $\ce{N2}$) adsorbed to a range of pure metal substrates. The model predicts the computed dissociative adsorption energy to metal surfaces with a correlation coefficient of 0.93 and a mean absolute error of 0.77 eV for the large database of molecular adsorption energies provided by *Catalysis-Hub.org* which have a range of 15 eV. As the model is based on pre-computed quantities it provides near-instantaneous estimates of adsorption energies and it is sufficiently accurate to eliminate around 90% of candidates in screening study of new adsorbates. The model, therefore, significantly enhances current efforts to identify new molecular coatings in many applied research fields.

## INTRODUCTION

Control of the chemical and physical properties of surfaces and interfaces is both of fundamental interest and vital in a very wide range of technologies including catalysis, environment, energy and medicine. Given the current pressing need for innovation in areas such as energy supply, energy distribution and transport there is a pressing need to develop technologies that can both extend the working lifetime of existing infrastructure and facilitate the development of new sustainable approaches to production and consumption. This has lead to the wide acknowledgment of the importance of controlling material surfaces and coatings [1, 2]. Common phenomena, such as corrosion and friction, cause substantial economic losses every year and severely impact the environment. For example, in extending the lifetime of current infrastructure, the worldwide costs of prevention, detection and mitigation of metal corrosion alone are estimated to be 2.5 trillion US dollars per year [3]. In addition, when considering the innovation of new devices, the development of micro- and nano-electromechanical systems requires new approaches for friction reduction in limited dimensions which leads to reduced efficiency and failure [4]. The ability to deposit molecular and nanostructured coatings with advanced functional properties is primed to have a profound effect on such diverse technologies as wearable electronics, corrosion inhibitors and lubricant additives. One of the challenges in molecular science is therefore the need to find novel, earth-abundant, inexpensive and environmentally friendly materials that adsorb in a controlled manner to surfaces and interfaces. Historically, innovation of new materials has been a time-consuming and challenging task; it typically takes 20 to 70 years to progress from laboratory conception to widespread commercial use [5]. Developments have also been mainly based on the incremental evolution of existing systems with the oft reported outcome that newly discovered solutions are based on exactly the same underlying mechanisms as their predecessors; to find something radical and innovative has usually been a matter of luck.

Extensive use is made of molecular additives for friction and corrosion reduction. A fundamental step in discovering new classes of these surfaces modifiers is a predictive understanding of the thermodynamics for both molecular and dissociative adsorption on different substrates [6–12]. For this purpose, it is essential to be able to compute the binding energy (BE) of different adsorption modes with sufficient accuracy to be able to predict the molecular level adhesion of the self assembling coating. In principle this is achievable using modern atomistic simulations but in practice is problematic as the parameter space of factors that affect the BE is very large [13]. There has therefore been a significant and sustained effort aimed at identifying a small number of easily computed descriptors that can accurately capture the nature of the molecule-surface interaction, and thus facilitating a simple and efficient predictive model of adsorption. In recent years the combination of high-throughput density functional theory (DFT) calculations and machine learning techniques has opened a new era of informatics-based approach to materials design, from which a number of simple models for predicting adsorption energies have emerged [14–32]. Similar approaches have also been used for predicting other figures of merit, like the inhibition efficiency of molecules [33]. These models are usually based on linear relationships using

* p.restuccia@imperial.ac.uk

simple descriptors for both the substrate and the ad- sorbed molecule (e.g., the number of valence electrons, the electronegativity of the substrate [15] and the ioniza- tion potential of the molecule [16]). Despite their simplic- ity, these models have been demonstrated to be quite ef- fective in predicting adsorption energies, especially when machine learning techniques are employed [14, 16]. How- ever, in the past such models have been limited in their transferability. For instance, any given model may be limited to the adsorption of molecules in one specific ad- sorption site (i.e., on-top or hollow). For a more extensive employment of these predictive calculations, one would like to extend the possible range of adsorption sites to model a broader array of realistic configurations, such as stepped edges or grain boundaries at the surface, and include a wide range of molecular adsorbates.

In the current work we present a new predictive lin- ear model that uses appropriate physical descriptors to predict in minutes the adsorption of a wide range of molecules to multiple substrates in a variety of surface adsorption sites. The model is based on a combination of systematic DFT calculations and machine learning. The model reported here accurately predicts the differ- ent dissociative adsorption energies of a range of probe molecules over simple homogeneous metallic substrates. Despite its simplicity, the model provides a good estimate of molecular BE in different configuration sites with lim- ited computational effort, and it is devised in a form that facilitates its extension to more complicated structures (e.g., oxides, carbonates or defective surfaces). More- over, the margin of error in the BE prediction is suf- ficiently small that provides a sufficiently accurate esti- mate of fully optimised ab initio calculations, saving time and facilitating the rapid screening of a broader range of systems. Therefore, the model is accurate enough to guide the discovery and optimisation of molecular ad- sorbates in order to improve the functionality of corro- sion inhibitors and lubricant additives and is likely to find application in fields such as catalysis, molecular elec- tronics and biomedicine [34-36], where the adsorption of molecules and molecular films underpins many important processes.

# METHOD

## BE calculation in slab configuration

For the adsorption energies of the training set (i.e., the slab systems) and the calculation of the later defined Molecule-Bulk Energy (MBE) terms, Spin-polarized DFT calculations were performed using the projector- augmented wave method (PAW) as implemented in the plane-wave code QUANTUM ESPRESSO (QE) [37]. We used the PAW pseudpopotentials [38] from the PSLibrary1.0.0 [39] within the generalised gradient approximation (GGA) of Perdew, Burke and Enzerhoff (PBE) [40] for the exchange-correlation energy. The electronic wave functions are expanded as a linear combination of plane waves up to a kinetic energy of 95 Ry, which we find issufficient to converge the total energies (1 meV/atom) and equilibrium lattice constant (0.1 mÅ) for the consid- ered substrates.

For the cell structure, we considered different configu- rations for the slab and the MBE calculations: for the for- mer, we employed supercells with a $2 \times 2$ in-plane size in order to reduce the interaction between adsorbate repli- cas and 5 of 6 layers, depending on the substrate of the different materials. For the latter, all the clusters were computed in a $20\ \mathring{A} \times 20\ \mathring{A} \times 20\ \mathring{A}$ cubic cell, so the self interaction between the cluster replicas is negligible. All the input and output geometries for both the slab and the MBE calculations are provided as Supplementary In- formation.

The Monkhorst-Pack grid [41] is used for sampling the Brillouin Zone, but different k-mesh for each structure under study were considered. In particular, we selected the optimal k-point grid for each slab geometry, whereas all the calculations involving clusters had a sampling at Gamma point due to the large cell dimensions. To improve the convergence, the Marzari-Vanderbilt cold smearing [42] method is used for the sampling of the Fermi surface, with a width of 0.27 eV in order to ob- tain accurate forces. The convergence criteria of forces and energy are $0.003\ \text{eV}\ \mathring{A}^{-1}$ and $10^{-2}\ \text{eV}$.

## HOMO, LUMO and HOMO-LUMO gap calculation for molecule in gas phase

For the calculation of the HOMO, LUMO and HOMO- LUMO gap, we performed DFT calculations using the CRYSTAL17 computational suite [43, 44], in which the crystalline orbitals are expanded as a linear combination of a local basis set composed by atom-centered Gaussian orbitals with s, p, or d symmetry. For all the elements employed in the molecular calculations (namely, H, C, N, O, F, S, Cl), we used the 6-31G** basis sets [45-51].

The approximation of the exchange and correlation functional is based on the Becke, 3-parameter, Lee-Yang-Parr (B3LYP) hybrid functional incorporating $20\%$ Hartree-Fock exchange [52-54]. The Coulomb and ex- change series are summed directly and truncated using overlap criteria with thresholds of $10^{-10}$, $10^{-10}$, $10^{-10}$, $10^{-20}$, $10^{-30}$ as described elsewhere [44, 55].

# RESULTS AND DISCUSSION

The general definition for the computed BE to a sur-face may be written as:

$$
\mathrm{BE}=\mathrm{E}_{\mathrm{tot}}-\left(\mathrm{E}_{\mathrm{sub}}+\mathrm{E}_{\mathrm{mol}}\right) \tag{1}
$$

where $\mathrm{E}_{\text {tot }}$ is the computed total energy for a system

composed of a molecule adsorbed on a substrate and $E_{\text{sub}}$ ($E_{\text{mol}}$) is the energy for the isolated substrate (molecule). With this definition, a negative (positive) BE indicates that the dissociation process is favourable (unfavourable).

The total BE can be analysed in terms of many contributions that may be related to properties of the molecule and the surface [56-58]. Defining a comprehensive model for the BE is challenging. A recent approach proposed by Dean *et al.* [16] succeeded in predicting the BE of probe molecules to metal nano-particles. This model is based on the idea that BE can be adequately represented by stability descriptors for the adsorbate, the adsorption site, the substrate and a simply computed estimate of the interaction between the molecule and the surface. These assumptions led to the following linear equation for the BE:

$$
\mathrm{BE}=a+b × \mathrm{CE}_{\text{local}}+c × \mathrm{IPEA}+d × \mathrm{MADs} \quad (2)
$$

where $\mathrm{CE}_{\text{local}}$ is the term to describe the local cohesive energy of the adsorption site, IPEA is the negative average between the ionization potential and the electronic affinity of the molecule, and the MADs is the gas phase BE between the adsorbate and one atom of the metal substrate, which is obtained through *ab initio* calculations, and represents the descriptor for the adsorbate-metal interaction. Although this model proved to be effective in the prediction of BE, with correlation coefficient $R^{2}$ of around 0.94 and a mean absolute error (MAE) of around 0.1 eV, there are some limitations in the employed approach: i) the adsorbates were always in an on-top site configuration, limiting the possibility to predict the BE in other adsorption sites such as hollow or bridge, and ii) the model has been trained only on noble metals nanoparticles and slab surfaces, such as Ag, Au and Cu, narrowing the range of possible substrates over which the prediction is effective.

In order to overcome these limitations, we present here a model using suitable descriptors for the adsorption of molecules over flat substrates. In particular, we propose the following equation for the prediction of BE:

$$
\mathrm{BE}=a+b × \mathrm{CE}_{\mathrm{B}}+c ×\left(\mathrm{W}_{\mathrm{F}}-\frac{\mathrm{E}_{\mathrm{gap}}}{2}\right)+d × \mathrm{MBE} \ (3)
$$

where $\mathrm{CE}_{\mathrm{B}}$ is the cohesive bulk energy for the substrate atomic species, $\mathrm{E}_{\text{gap}}$ is the gap between the Highest Occupied (HOMO) and Lowest Unoccupied (LUMO) Molecular Orbital of the adsorbed molecule (from now on, HOMO-LUMO gap), $\mathrm{W}_{\mathrm{F}}$ is the work function of the substrate, MBE is the Molecule-Bulk Energy, which resembles the MADs of Eq. 2 and it is computed using *ab initio* theory; $a$, $b$, $c$ and $d$ are the linear coefficients for the regression. $\mathrm{CE}_{\mathrm{B}}$ provides a general estimate of the strength of the interaction between the substrate atoms and the MBE provides a simply computed estimate of the substrate-molecule interaction. The third term contains the difference between the surface work function and the middle of the HOMO-LUMO gap of the adsorbed molecule which in frontier molecular orbital theory controls the charge transfer and hybridisation contributions to the surface binding [59-61]. The MBE term is computed as:

$$
\mathrm{MBE}=\sum_{i=1}^{n_{f r a g}} E_{c o m p l e x, i}-E_{B, M, i}-\mu_{G, m o l, i} \quad (4)
$$

where $n_{frag}$ is the number of molecular fragments considered in the dissociative adsorption process, $E_{complex}$ is the total energy of a molecular functional group adsorbed on a single atom of the metal substrate, $E_{B,M}$ is the bulk energy of a single atom of the substrate atomic species and $\mu_{G,mol}$ is the chemical potential of the molecular fragment generalised from the fragment energy to allow for the adsorption environment. This quantity provides an easily computed and flexible estimate of the strength of adhesion between the adsorbate and the substrate. In contrast to the MADs term proposed by Dean *et al.*, where all the functional groups are computed as isolated components, in the proposed MBE term we refer all energies to a consistent reference enabling the use of precomputed data in a transferable predictive model. Another advantage of this approach is choosing the proper reference for the chemical potential in the calculation of MBE. In the current work, we chose to refer $\mu_{G,mol}$ to the isolated gas phase molecule for the sake of simplicity. However, it is possible to reference the chemical potential to different environments including solvated species, as shown in recent electrochemical studies [62-64].

![](./images/867763770720518451_1.jpg)

FIG. 1: Ball and stick representation of the models used for the different approaches in the calculation of MBE in the case of Cl adsorption on Cu: a) the substrate is modelled by just one atom, b) the substrate is represented by a cluster of 4 atoms and c) the cluster modelling the substrate is composed by 10 atoms. Green and brown balls represent chlorine and copper atoms, respectively.

In the current work, ordinary least squares (OLS) linear regressions were used to determine the coefficients in Eq. 3 from a training set of *ab initio* energies using the *statsmodels* library [65] provided in Python 3 [66]. For the OLS regression, we adopted a training set of eight different probe molecules, namely $\mathrm{Cl}_{2}$, $\mathrm{CO}_{2}$, $\mathrm{F}_{2}$, $\mathrm{H}_{2}$,

TABLE I: Regression coefficients, i.e., Coefficient Estimate, Standard Error (SE) and P-value, for the different approaches employed for MBE calculation in the case of a) single metal atom, b) a small metal cluster and c) a large metal cluster. Cases are trained using the dataset provided in the Supplementary Information. $R^2$ is the correlation coefficient, MAE is the mean absolute error.

(a) First approach for MBE, as shown in Fig. 1a. $R^2 = 0.21$, MAE = 1.97 eV, RMSE = 2.52 eV.

|   | Coefficient Estimate | SE    | P-value |
|---|----------------------|-------|---------|
| $a$ | 2.2460               | 1.6048| 0.167   |
| $b$ | -0.7268              | 0.3114| 0.023   |
| $c$ | 0.8900               | 0.2721| 0.002   |
| $d$ | -0.0886              | 0.0970| 0.365   |

(b) Second approach for MBE, as shown in Fig. 1b. $R^2 = 0.83$, MAE = 0.89 eV, RMSE = 1.17 eV.

|   | Coefficient Estimate | SE    | P-value |
|---|----------------------|-------|---------|
| $a$ | 1.5812               | 0.7064| 0.029   |
| $b$ | -0.2925              | 0.1461| 0.050   |
| $c$ | 0.1793               | 0.1122| 0.116   |
| $d$ | 1.0163               | 0.0691| $3 \cdot 10^{-21}$ |

(c) Third approach for MBE, as shown in Fig. 1c. $R^2 = 0.94$, MAE = 0.52 eV, RMSE = 0.69 eV.

|   | Coefficient Estimate | SE    | P-value |
|---|----------------------|-------|---------|
| $a$ | 0.7426               | 0.4208| 0.083   |
| $b$ | -0.1735              | 0.0874| 0.052   |
| $c$ | 0.1844               | 0.0659| 0.007   |
| $d$ | 0.9927               | 0.0370| $3 \cdot 10^{-34}$ |

$\text{H}_2\text{O}$, $\text{H}_2\text{S}$, $\text{N}_2$ and $\text{O}_2$, adsorbed over ten different metal substrates, namely Ag(111), Al(111), Au(111), Cu(111), Fe(100), Fe(110), Ir(111), Pt(111), V(100) and V(110). In each case the energy of the most stable adsorption configuration was used. Where possible standard reference data was used for each of the terms of Eq. 3: for $\text{CE}_\text{B}$, we used the observed formation energies of the transition metals provided by Ref. [67], for the work function, we employed the DFT computed values provided by the Materials Project database [68]. The HOMO-LUMO gap of the molecules was estimated from *ab initio* calculations, with the computational details provided in the Methods section. The MBE was also computed *ab initio* using a small cluster which will be discussed below.

## Analysing Contributions to the MBE

An appropriate calculation of the MBE is essential for the efficiency and accuracy of the proposed model. The simplest level of approximation used here is that proposed by Dean *et al.* in which the MBE is computed as Eq. 4, i.e., the binding energy is the energy difference in the gas phase of a specific fragment obtained during the dissociative process and one metal atom of the substrate [16]. An example of this possible configuration to calculate MBE is shown in Fig. 1a for the case of Cl adsorbed to a Cu atom. The regression statistics are shown in Table Ia, while Figure 2 shows the parity plot of the model training against the DFT computed adsorption energies for the predicted BE.

![](./images/867763770720518451_2.jpg)

FIG. 2: Parity plot for the training of the model against the DFT BE calculations with the MBE approach proposed in Eq. 4 and the system shown in Fig. 1a. The black solid line represents the parity between the computed DFT BE and the predicted value.

This approximation provides a rather poor prediction of the BE: the correlation coefficient $R^2$ is around 0.21 (an $R^2$ of 0 corresponds to no correlation and of 1.0 to a perfect set of predictions) and the mean absolute error (MAE) is almost 2 eV. The parity plot in Figure 2 confirms that the linear regression does not provide a good description of the BE. Although Dean *et al.* have shown convincingly that this approach reproduces the energy of adsorption to metallic nanoparticles in an on-top configuration of several radical groups (namely, $\text{CH}_3$, CO and OH), it evidently fails to do so when the molecules are adsorbed on a wide range of substrates.

A possible explanation for this discrepancy is that the variations of the interactions in the hollow and bridge adsorption sites considered here are not captured by binding to a single metal atom. This suggests that a somewhat larger cluster is required to take into account the different adsorption site configurations in the calculation of MBE such as that represented in Figure 1b. Here the Cl is adsorbed to a four atom cluster based on the hollow site presented by the Cu(111). This is the smallest cluster, for this specific substrate, which retains the symmetry of the surface adsorption site. We conveniently create

these clusters that resemble the surface adsorption sites for all the considered substrates in our training set and the geometries employed for these calculations are pro- vided as Supplementary Information. Another essential advantage of this approach is the possibility to explore sites with lower coordination numbers that resemble sub- strates containing defects or stepped edges. The only possibility to simulate these configurations with a peri- odic slab structure is by using large supercells with hun- dreds of atoms, thus increasing the computation time significantly compared to the few atoms used within a cluster.

With the use of this approach, we change the definition of MBE as follows:

$$
\operatorname{MBE}=\sum_{i=1}^{n_{f r a g}} E_{c o m p l e x, i}-E_{c l u s t e r, i}-\mu_{G, m o l, i} \quad(5)
$$

where all the terms of Eq. 5 are the same as Eq. 4, apart from $E_{cluster,i }$ which is the energy of the cluster mod elling the substrate. This approach leads to a significant improvement in the BE prediction, as shown in both Ta- ble Ib and Figure 3. There is a significant improvement in both the correlation coefficient (around 0.83) and the MAE (around 0.9 eV).

![](./images/867763770720518451_3.jpg)

FIG. 3: Parity plot for the training of the model against the DFT BE calculations with the MBE cluster approach proposed in Eq. 5 and the system shown in Fig. 1b. The black solid line represents the parity between the computed DFT BE and the predicted value.

Extending this approach, one can compute the MBE from adsorption to the 10 atom cluster displayed in Fig- ure 1c for the case Cl adsorbed to a hollow site on Cu. This cluster also maintains the adsorption site symmetry.

From Figure 4 it is evident that the model based on this MBE provides a satisfactory description of the adsorption energetics with a correlation coefficient of 0.94, and a more significant reduction of the MAE to 0.5 eV.

![](./images/867763770720518451_4.jpg)

FIG. 4: Parity plot for the training of the model against the DFT BE calculations with the MBE cluster approach proposed in Eq. 5 and the system shown in Fig. 1c. The black solid line represents the parity between the computed DFT BE and the predicted value.

In addition, all of the fitted parameters have a P-value equal or smaller than 0.05, which is the threshold to ob- tain a confidence level of 95% in the predictions of the model. Even if this threshold should not be seen as a sharp edge for statistical significance [69], the obtained values for both the P-value and the standard errors pro- vide a rigorous test for the effectiveness of our model.

It is possible to perform a more qualitative analysis of the accuracy of the proposed models by considering the residuals distribution as shown in Fig. 5: each panel presents this distribution as a histogram counter of the errors for the MBE calculation approaches proposed in this work. As expected, the errors follow a normal dis- tribution, and every time the description of the MBE is improved, the residuals range is almost halved, further validating our approach. It is also interesting to notice that moving from the smaller to larger cluster leads to a notable reduction in the MAE of around 40%, but the correlation coefficients are similar (0.83 for the smaller clusters, 0.94 for the larger ones). Therefore, one can adjust the model for convenience: it is possible to either lose a bit of predictive accuracy with the advantage of realising a database with smaller clusters (which usually requires around half the time for the actual calculation) or retain a better precision with the cost of longer com- putational time to build the database of the MBE co- efficients. From now on, our analysis will focus on the

predictive model employing the larger clusters since they provide the most accurate results.

The model proposed here is therefore able to predict BE with a fidelity comparable to the current state of the art but for a variety of adsorption geometries and adsor- bates. The MAE for the training set is somewhat higher that of the model reported by Dean et al. of around 0.1 eV but it is computed for a training dataset with a much larger range of BE (from -10 to +3 eV), so the associated relative error is comparable.

TABLE II: Correlation coefficient $R^2$, mean absolute error (MAE) and root mean square error (RMSE) of the OLS regression for the proposed Model and the MBE against the computed DFT values for the BE as shown in Figure 6.

|              | Model | MBE  |
|--------------|-------|------|
| $R^2$        | 0.94  | 0.93 |
| MAE (eV)     | 0.52  | 0.56 |
| RMSE (eV)    | 0.69  | 0.79 |

Before proceeding with the model validation analysis, it is interesting to note the importance of MBE in cal- culating the BE since its OLS regression coefficient $d$ is the one with the smallest relative error and P-value. To understand how relevant this term is in calculating the predicted BE, we compare two different types of dataset training. The first is the one we discussed in the previous paragraph and is shown in Figure 4. The second is based on a simple OLS regression of the MBE values of the con- sidered reaction paths against the computed DFT BE. The results are shown in Figure 6 and Table II. It is ap- parent that qualitatively the first training approach (blue dots) provides similar results to the one based solely on MBE (red squares), highlighting the greater importance of the MBE term in the definition of the model. A deeper analysis involving the regression coefficients, such as $R^2$, MAE and the root mean square error (RMSE), shows us a clearer picture. Although $R^2$ is similar in both scenar- ios (0.94 vs 0.93), we notice an increase in both MAE and RMSE when considering in training only MBE by 8% and 14%, respectively. Therefore, even if the MBE is an essential part of the definition of this new model, it is important to consider all the physical terms we have identified in the definition of Eq. 3, in order to minimize the average error in the BE.

After the training, the following step is to validate the model for use in predicting new dissociation paths for larger molecules. To do so, we compared its predictions to reaction energies computed and tabulated in previous work.

## Validation of the Model

The validation of the proposed model is essential for its employment in actual technological applications. To do so, we compare the BE predicted by the model with the DFT reaction energies available on the Catalysis-Hub.org database [22, 23] for 80 different surface reactions. In par- ticular, we chose twelve different molecules, namely $\text{CH}_4$, $\text{C}_2\text{H}_6$, $\text{CO}_2$, $\text{H}_2$, $\text{H}_2\text{O}$, $\text{H}_2\text{S}$, $\text{N}_2$, $\text{NH}_3$, $\text{NO}$, $\text{N}_2\text{O}$, $\text{NO}_2$ and $\text{O}_2$, adsorbed over eleven different metal substrates, namely Ag(111), Al(111), Au(111), Co(111), Cu(111), Ir(111), Ni(111), Pd(111), Pt(111), Sc(111), Y(111). The specific reaction geometries employed for the validation are provided as Supplementary Information. All the DFT reaction energies retrieved from the Catalysis-Hub.org database had been computed within the BEEF-vdW ap- proximation to electronic exchange and correlation [70].

The parity plots resulting from this comparison are shown in Figure 7. The error bars present in the plots are computed using standard error propagation based on the errors obtained from the OLS regressions.

From Figure 7a, it is clear that the model captures to an exceptional level of accuracy the variation in BE in these systems: the correlation coefficient of the parity plot is 0.93, the MAE is 0.77 eV and the RMSE is 1.02 eV. When searching for a molecule with a specific adsorption energy with a typical range of 20 eV the MAE of 0.77eV is sufficient to reduce the number of candidate molecules by well over an order of magnitude. It is, nevertheless, interesting to note that there are outliers to this general trend. For example, the model predicts a favourable ad- sorption energy for several molecules ($\text{C}_2\text{H}_6$, $\text{H}_2\text{O}$, $\text{NH}_3$ and $\text{N}_2\text{O}$) on Pd(111) (data provided in the Supplemen- tary Information), whereas the DFT data predicts un- favourable adsorption energies. In all of these cases, the BE is in the region of $\pm 1$ eV, which is consistent with the MAE found in the training of the model. We can tentatively conclude from this that the current model is less reliable in describing the dissociative adsorption in this weak bonding region. Another possible explanation for this behaviour can also be found in the different ex- change and correlation functional employed in our study: as explained in the Method section, we used the general- ized gradient approximation (GGA) for the MBE calcula- tion, whereas the data retrieved from Catalysis-Hub.org were all computed within the BEEF-vdW approximation, which has specific corrections to take into account the dispersion interactions. The absence of the latter in our model can explain the differences arising from the weakly bonded systems.

Apart from these outliers, the prediction of tabulated values is remarkably accurate. As for the original fit to the training set, the intercept of the model has a signif- icant associated error and P-value. It is therefore inter- esting to test the performance of the model when this pa- rameter is neglected, this data is displayed in Figure 7b. It is notable that i) without $a$ there is only a slight off- set in the predicted BE which does not affect the general behaviour of the parity plot, with $R^2$, MAE and RMSE essentially unchanged, and ii) the estimated error bars for each energy are substantially reduced. This latter observation is explained by the fact that half of the er-

![](./images/867763770720518451_5.jpg)

FIG. 5: Residual distribution for the MBE calculation as proposed in Fig. 1a (left panel), Fig. 1b (center panel) and Fig. 1c (right panel). The blue curve represents a smoothing interpolation of the residual data.

![](./images/867763770720518451_6.jpg)

FIG. 6: Parity plot for the trained model BE (blue dots) with the coefficients reported in Table Ic and MBE values (red squares) against the DFT BE calculations.

ror in the predicted BE is due to the uncertainty of $a$, which is the coefficient with the highest relative error and P-value.

The discussion above demonstrates that the current model provides a low cost prediction of the BE to ho- mogeneous metal substrates. It is interesting to spec- ulate on the extension of the model to a more general framework for predicting adsorption to a wider range of substrates. A natural extension would be to design a simple MBE cluster calculation for the oxide and carbon- ate substrates, which are essential in many technological applications and for which there is currently a lack of predictive models regarding molecular adsorption.

### Comparison with SISSO approach

A possible concern in using the proposed approach is that our model only uses OLS regressions, which could appear simplistic compared to the current state- of-the-art approaches. In particular, one of the most advanced methods in extracting effective descriptors to predict materials properties is the so-called Sure Inde- pendence Screening and Sparsifying Operator (SISSO) algorithm [71]. SISSO can identify the best descriptors among a set of physical properties, determining the op- timal subset. Moreover, it can also identify the most accurate mathematical expressions to obtain the opti- mised relationship for the available data. It is, therefore, natural to benchmark the results shown in the previous

![](./images/867763770720518451_7.jpg)
![](./images/867763770720518451_8.jpg)

FIG. 7: Parity plots for the validation of the model against the DFT BE calculations available on the Catalysis-Hub.org database. The panel a) shows the predicted values considering the intercept $a$, whereas panel b) represents the predictive model dismissing the intercept $a$.

sections with the ones obtained by employing the SISSO algorithm.

The first step is to identify whether our approach provides an accurate set of descriptors and identifies the proper mathematical expression. Therefore, alongside the three descriptors employed in the previous sections, we added eight additional physical and chemical properties of the molecule and the metallic substrate to increase the set of descriptors, among which SISSO would determine the optimal ones. Namely, we choose the number of valance electrons of the atomic specie in the metallic substrate ($\mathrm{N_{ve}}$), the surface energy of the metal ($\gamma_{\text{met}}$), the first ionization potential of the metal ($\mathrm{I_1}$), the volume of a single atom in the metallic substrate ($\mathrm{V_{met}}$), the metal electronegativity ($\chi_{\text{met}}$), the HOMO ($\text{HOMO}_{\text{mol}}$), LUMO ($\text{LUMO}_{\text{mol}}$) and molar mass ($\mathrm{M_{mol}}$) of the molecule as additional physical/chemical descriptors to process in the SISSO algorithm. These data have been gathered as tabulated values (namely, $\mathrm{N_{ve}}$, $\mathrm{I_1}$, $\mathrm{V_{met}}$, $\chi_{\text{met}}$ and $\mathrm{M_{mol}}$), by DFT values provided by the Materials Project database ($\gamma_{\text{met}}$) [68] and by performing DFT calculations ($\text{HOMO}_{\text{mol}}$ and $\text{LUMO}_{\text{mol}}$) as detailed in the Method section.

Once we applied the SISSO algorithm to the training data shown in Fig. 4, we obtained the best fitting with three coefficients by using the following equation (the data obtained by the SISSO algorithm are provided as Supplementary Information):

$$
\begin{aligned}
\mathrm{BE_{SISSO}} &= 0.787 - 0.044 \times \mathrm{V_{met}}+ \\
& \quad + 0.178 \times \left(\mathrm{W_F} - \frac{\mathrm{E_{gap}}}{2}\right) + 1.010 \times \mathrm{MBE} \tag{6}
\end{aligned}
$$

with an associated RMSE of 0.65 eV. The best descriptors identified by the SISSO algorithm were the MBE and the difference between the substrate work function and half of the HOMO-LUMO gap, as already identify in with our approach, alongside $\mathrm{V_{met}}$. The former is the only different descriptor compared to our model, in which we used the cohesive bulk energy of the substrate. Most notably, Eq. 6 shows a linear relationship with similar coefficients to the OLS fitting shown in Table Ic, and we noticed a reduction of the RMSE of around 5%. Therefore, our proposed model shows similar results both in identifying the best descriptors and in the RMSE, thus the SISSO methodology validates our approach. The significant difference in one of the descriptors identified by the fitting should not be seen as a downside of our work, rather as a different way to interpret the problem of predicting BE: we have identified the descriptors in our methodology by finding physical and chemical properties adequate to the studied systems, whereas the SISSO algorithm is looking only to the primary features that best fit mathematically the BE data.

## CONCLUSION

In summary, we report a new model of molecule-surface binding based on the combination of *ab initio* calculations with machine learning algorithms, such as ordinary least squares regression. This model provides in minutes and with limited computational effort a reasonable estimate of the adsorption of small molecules to metal substrates given a set of easily computed descriptors. The model distinguishes different reaction sites and between molecular and dissociative adsorption accurately, especially for larger adsorption energies (values greater than $\pm 1$ eV). Compared with an independent and well established database of computed adsorption ener-

gies, the predicted values suggest that the model is trans- ferable in that it can provide equally accurate BE pre- dictions for a variety of functional groups and surfaces from outside the training set. We have benchmarked our model against the SISSO algorithm, finding that the best fitting of the BE data is with a linear equation, and our choice of the descriptors is very close to the best-case sce- nario identified by the algorithm, with a difference in the RMSE of around 5%.

The model is constructed so that its extension to dif- ferent substrates (e.g., oxides and carbonates) and tech- nically relevant functional groups is straightforward. We expect the model to find widespread use in a variety of applications. For example, the innovation of new coat- ings for friction and corrosion reduction and the devel- opment of novel anti-pathogen coatings to reduce disease transmission via surfaces.

## ACKNOWLEDGEMENTS

This work made use of the high performance comput- ing facilities of Imperial College London. The authors thankfully acknowledge the funding and technical sup- port from BP through the BP International Centre for Advanced Materials (BP-ICAM). The authors want also to thank Dr. Giuseppe Mallia for the fruitful discussions. The pictures present in this article are generated thanks to XCrySDen [72, 73] and Matplotlib [74].

[1] J. V. Barth, G. Costantini, and K. Kern, Engineering atomic and molecular nanostructures at surfaces, **Nature 437**, 671 (2005).

[2] K. Choy, Chemical vapour deposition of coatings, **Progress in Materials Science 48**, 57 (2003).

[3] G. Koch, J. Varney, N. Thompson, O. Moghissi, M. Gould, and J. Payer, International measures of pre- vention, application, and economics of corrosion tech- nologies study, **NACE Impact** (2016).

[4] K. Komvopoulos, Surface engineering and microtribol- ogy for microelectromechanical systems, **Wear 200**, 305 (1996).

[5] R. Gross, R. Hanna, A. Gambhir, P. Heptonstall, and J. Speirs, How long does innovation and commercialisa- tion in the energy sectors take? historical case studies of the timescale from invention to widespread commercial- isation in energy supply and end use technology, **Energy Policy 123**, 682 (2018).

[6] M. Finšgar and J. Jackson, Application of corrosion in- hibitors for steels in acidic media for the oil and gas in- dustry: A review, **Corrosion Science 86**, 17 (2014).

[7] Y. Zhu, M. L. Free, R. Woollam, and W. Durnie, A re- view of surfactants as corrosion inhibitors and associated modeling, **Progress in Materials Science 90**, 159 (2017).

[8] K. Kousar, M. Walczak, T. Ljungdahl, A. Wetzel, H. Oskarsson, P. Restuccia, E. Ahmad, N. Harrison, and R. Lindsay, Corrosion inhibition of carbon steel in hydrochloric acid: Elucidating the performance of an imidazoline-based surfactant, **Corrosion Science 180**, 109195 (2021).

[9] A. Neville, A. Morina, T. Haque, and M. Voong, Compat- ibility between tribological surfaces and lubricant addi- tives—how friction and wear reduction can be controlled by surface/lube synergies, **Tribology International 40**, 1680 (2007).

[10] I. Minami, Molecular science of lubricant additives, **Ap- plied Sciences 7**, 445 (2017).

[11] G. Fatti, P. Restuccia, C. Calandra, and M. C. Righi, Phosphorus adsorption on fe(110): An ab initio compar- ative study of iron passivation by different adsorbates, **The Journal of Physical Chemistry C 122**, 28105 (2018).

[12] S. Peeters, P. Restuccia, S. Loehlé, B. Thiebaut, and M. C. Righi, Characterization of molybdenum dithiocar- bamates by first-principles calculations, **The Journal of Physical Chemistry A 123**, 7007 (2019).

[13] J. K. Nørskov, T. Bligaard, B. Hvolbæk, F. Abild- Pedersen, I. Chorkendorff, and C. H. Christensen, The nature of the active site in heterogeneous metal cataly- sis, **Chem. Soc. Rev. 37**, 2163 (2008).

[14] E.-J. Ras, M. J. Louwerse, M. C. Mittelmeijer-Hazeleger, and G. Rothenberg, Predicting adsorption on metals: simple yet effective descriptors for surface catalysis, **Phys. Chem. Chem. Phys. 15**, 4436 (2013).

[15] W. Gao, Y. Chen, B. Li, S.-P. Liu, X. Liu, and Q. Jiang, Determining the adsorption energies of small molecules with the intrinsic properties of adsorbates and substrates, **Nature Communications 11**, 1196 (2020).

[16] J. Dean, M. G. Taylor, and G. Mpourmpakis, Unfolding adsorption on metal nanoparticles: Connecting stability with catalysis, **Science Advances 5**, eaax5101 (2019).

[17] L. T. Roling and F. Abild-Pedersen, Structure-sensitive scaling relations: Adsorption energies from surface site stability, **ChemCatChem 10**, 1643 (2018).

[18] L. T. Roling, L. Li, and F. Abild-Pedersen, Configura- tional energies of nanoparticles based on metal-metal co- ordination, **The Journal of Physical Chemistry C 121**, 23002 (2017).

[19] Z. Yan, M. G. Taylor, A. Mascareno, and G. Mpourm- pakis, Size-, shape-, and composition-dependent model for metal nanoparticle stability prediction, **Nano Letters 18**, 2696 (2018).

[20] C. Liu, Y. Li, M. Takao, T. Toyao, Z. Maeno, T. Ka- machi, Y. Hinuma, I. Takigawa, and K.-i. Shimizu, Fron- tier molecular orbital based analysis of solid–adsorbate interactions over group 13 metal oxide surfaces, **The Journal of Physical Chemistry C 124**, 15355 (2020).

[21] F. Calle-Vallejo, J. I. Martínez, J. M. García-Lastra, P. Sautet, and D. Loffreda, Fast prediction of adsorp- tion properties for platinum nanocatalysts with general- ized coordination numbers, **Angewandte Chemie Interna- tional Edition 53**, 8316 (2014).

[22] K. T. Winther, M. J. Hoffmann, J. R. Boes, O. Mamun, M. Bajdich, and T. Bligaard, Catalysis-hub.org, an open electronic structure database for surface reactions, **Scien- tific Data 6**, 75 (2019).

[23] O. Mamun, K. T. Winther, J. R. Boes, and T. Bligaard, High-throughput calculations of catalytic properties of bimetallic alloy surfaces, *Scientific Data* **6**, 76 (2019).

[24] O. Mamun, K. T. Winther, J. R. Boes, and T. Bligaard, A bayesian framework for adsorption energy prediction on bimetallic alloy catalysts, *npj Computational Materials* **6**, 177 (2020).

[25] M. Andersen, S. V. Levchenko, M. Scheffler, and K. Reuter, Beyond scaling relations for the description of catalytic materials, *ACS Catalysis* **9**, 2752 (2019).

[26] A. J. Chowdhury, W. Yang, E. Walker, O. Mamun, A. Heyden, and G. A. Terejanu, Prediction of adsorption energies for chemical species on metal catalyst surfaces using machine learning, *The Journal of Physical Chemistry C* **122**, 28142 (2018).

[27] C. S. Praveen and A. Comas-Vives, Design of an accurate machine learning algorithm to predict the binding energies of several adsorbates on multiple sites of metal surfaces, *ChemCatChem* **12**, 4611 (2020).

[28] Y. Zhang and X. Xu, Predictions of adsorption energies of methane-related species on cu-based alloys through machine learning, *Machine Learning with Applications* **3**, 100010 (2021).

[29] C. Chang and A. J. Medford, Application of density functional tight binding and machine learning to evaluate the stability of biomass intermediates on the rh(111) surface, *The Journal of Physical Chemistry C* **125**, 18210 (2021).

[30] V. Fung, G. Hu, P. Ganesh, and B. G. Sumpter, Machine learned features from density of states for accurate adsorption energy prediction, *Nature Communications* **12**, 88 (2021).

[31] Z. Li, B. J. Bucior, H. Chen, M. Haranczyk, J. I. Siepmann, and R. Q. Snurr, Machine learning using host/guest energy histograms to predict adsorption in metal-organic frameworks: Application to short alkanes and xe/kr mixtures, *The Journal of Chemical Physics* **155**, 014701 (2021).

[32] R. Anderson, A. Biong, and D. A. Gómez-Gualdrón, Adsorption isotherm predictions for multiple molecules in mofs using the same deep learning model, *Journal of Chemical Theory and Computation* **16**, 1271 (2020).

[33] C. T. Ser, P. Žuvela, and M. W. Wong, Prediction of corrosion inhibition efficiency of pyridines and quinolines on an iron surface using machine learning-powered quantitative structure-property relationships, *Applied Surface Science* **512**, 145612 (2020).

[34] T. Bligaard, J. Nørskov, S. Dahl, J. Matthiesen, C. Christensen, and J. Sehested, The brønsted-evans-polanyi relation and the volcano curve in heterogeneous catalysis, *Journal of Catalysis* **224**, 206 (2004).

[35] C. Joachim and M. A. Ratner, Molecular electronics: Some views on transport junctions and beyond, *Proceedings of the National Academy of Sciences* **102**, 8801 (2005).

[36] B. Kasemo, Biological surface science, *Surface Science* **500**, 656 (2002).

[37] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, Quantum espresso: a modular and open-source software project for quantum simulations of materials, *Journal of Physics: Condensed Matter* **21**, 395502 (2009).

[38] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, *Phys. Rev. B* **59**, 1758 (1999).

[39] A. Dal Corso, Pseudopotentials periodic table: From h to pu, *Computational Materials Science* **95**, 337 (2014).

[40] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, *Phys. Rev. Lett.* **77**, 3865 (1996).

[41] H. J. Monkhorst and J. D. Pack, Special points for brillouin-zone integrations, *Phys. Rev. B* **13**, 5188 (1976).

[42] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Thermal contraction and disordering of the al(110) surface, *Phys. Rev. Lett.* **82**, 3296 (1999).

[43] R. Dovesi, A. Erba, R. Orlando, C. M. Zicovich-Wilson, B. Civalleri, L. Maschio, M. Rérat, S. Casassa, J. Baima, S. Salustro, and B. Kirtman, Quantum-mechanical condensed matter simulations with CRYSTAL, *WIREs Computational Molecular Science* **8**, e1360 (2018).

[44] R. Dovesi, V. R. Saunders, C. Roetti, R. Orlando, C. M. Zicovich-Wilson, F. Pascale, B. Civalleri, K. Doll, N. M. Harrison, I. J. Bush, P. D'Arco, M. Llunell, M. Causà, Y. Noël, L. Maschio, A. Erba, M. Rérat, and S. Casassa, *CRYSTAL17 User's Manual*, University of Torino (2017).

[45] T. Clark, J. Chandrasekhar, G. W. Spitznagel, and P. V. R. Schleyer, Efficient diffuse function-augmented basis sets for anion calculations. III. the 3-21+g basis set for first-row elements, Li-F, *J. Comput. Chem.* **4**, 294 (1983).

[46] R. Ditchfield, W. J. Hehre, and J. A. Pople, Self-consistent molecular-orbital methods. IX. an extended gaussian-type basis for molecular-orbital studies of organic molecules, *J. Chem. Phys.* **54**, 724 (1971).

[47] M. M. Francl, W. J. Pietro, W. J. Hehre, J. S. Binkley, M. S. Gordon, D. J. DeFrees, and J. A. Pople, Self-consistent molecular orbital methods. XXIII. a polarization-type basis set for second-row elements, *J. Chem. Phys.* **77**, 3654 (1982).

[48] M. S. Gordon, J. S. Binkley, J. A. Pople, W. J. Pietro, and W. J. Hehre, Self-consistent molecular-orbital methods. 22. small split-valence basis sets for second-row elements, *J. Am. Chem. Soc.* **104**, 2797 (1982).

[49] P. C. Hariharan and J. A. Pople, The influence of polarization functions on molecular orbital hydrogenation energies, *Theor. Chim. Acta* **28**, 213 (1973).

[50] W. J. Hehre, R. Ditchfield, and J. A. Pople, Self-consistent molecular orbital methods. XII. further extensions of gaussian-type basis sets for use in molecular orbital studies of organic molecules, *J. Chem. Phys.* **56**, 2257 (1972).

[51] G. W. Spitznagel, T. Clark, P. v. R. Schleyer, and W. J. Hehre, An evaluation of the performance of diffuse function-augmented basis sets for second row elements, na-cl, *J. Comput. Chem.* **8**, 1109 (1987).

[52] A. D. Becke, A new mixing of hartree-fock and local density-functional theories, *The Journal of Chemical Physics* **98**, 1372 (1993).

[53] C. Lee, W. Yang, and R. G. Parr, Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density, *Physical Review B* **37**, 785 (1988).

[54] P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M. J. Frisch, Ab initio calculation of vibrational absorp- tion and circular dichroism spectra using density func- tional force fields, *The Journal of Physical Chemistry* **98**, 11623 (1994).

[55] C. Pisani, R. Dovesi, and C. Roett, *Hartree-Fock Ab Ini- tio Treatment of Crystalline Systems*, 1st ed., Lecture Notes in Chemistry, Vol. 48 (Springer Verlag, 1988).

[56] J. Scaranto, G. Mallia, and N. Harrison, An efficient method for computing the binding energy of an adsorbed molecule within a periodic approach. the application to vinyl fluoride at rutile TiO2(110) surface, *Computational Materials Science* **50**, 2080 (2011).

[57] C. Morin, D. Simon, and P. Sautet, Chemisorption of benzene on Pt(111), Pd(111), and Rh(111) metal sur- faces: A structural and vibrational comparison from first principles, *The Journal of Physical Chemistry B* **108**, 5653 (2004).

[58] B. Wang, S. Günther, J. Wintterlin, and M.-L. Bocquet, Periodicity, work function and reactivity of graphene on ru(0001) from first principles, *New Journal of Physics* **12**, 043041 (2010).

[59] K. Fukui, T. Yonezawa, and H. Shingu, A molecular or- bital theory of reactivity in aromatic hydrocarbons, *The Journal of Chemical Physics* **20**, 722 (1952).

[60] R. Hoffmann, A chemical and theoretical way to look at bonding on surfaces, *Rev. Mod. Phys.* **60**, 601 (1988).

[61] H. Ishii, K. Sugiyama, E. Ito, and K. Seki, Energy level alignment and interfacial electronic structures at organic/metal and organic/organic interfaces, *Advanced Materials* **11**, 605 (1999).

[62] N. G. Hörman, O. Andreussi, and N. Marzari, Grand canonical simulations of electrochemical interfaces in im- plicit solvation models, *The Journal of Chemical Physics* **150**, 041730 (2019).

[63] N. G. Hörmann, N. Marzari, and K. Reuter, Electrosorp- tion at metal surfaces from first principles, *npj Compu- tational Materials* **6**, 136 (2020).

[64] N. G. Hörmann and K. Reuter, Thermodynamic cyclic voltammograms based on ab initio calculations: Ag(111) in halide-containing solutions, *Journal of Chemical The- ory and Computation* **17**, 1782 (2021).

[65] S. Seabold and J. Perktold, statsmodels: Econometric and statistical modeling with python, in *9th Python in Science Conference* (2010) pp. 92–96.

[66] G. Van Rossum and F. L. Drake, *Python 3 Reference Manual* (CreateSpace, 2009).

[67] C. Kittel, *Introduction to Solid State Physics*, 8th ed. (John Wiley & Sons, 2004).

[68] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. a. Persson, The Materials Project: A materials genome approach to accelerating materials innovation, *APL Materials* **1**, 011002 (2013).

[69] Analytical Methods Committee AMCTB No. 93, To p or not to p: the use of p-values in analytical science, *Anal. Methods* **12**, 872 (2020).

[70] J. Wellendorff, K. T. Lundgaard, A. Møgelhøj, V. Pet- zold, D. D. Landis, J. K. Nørskov, T. Bligaard, and K. W. Jacobsen, Density functionals for surface science: Exchange-correlation model development with bayesian error estimation, *Phys. Rev. B* **85**, 235149 (2012).

[71] R. Ouyang, S. Curtarolo, E. Ahmetcik, M. Scheffler, and L. M. Ghiringhelli, Sisso: A compressed-sensing method for identifying the best low-dimensional descriptor in an immensity of offered candidates, *Phys. Rev. Materials* **2**, 083802 (2018).

[72] A. Kokalj, Xcrysden—a new program for displaying crystalline structures and electron densities, *Journal of Molecular Graphics and Modelling* **17**, 176 (1999).

[73] A. Kokalj, Computer graphics and graphical user inter- faces as tools in simulations of matter at the atomic scale, *Computational Materials Science* **28**, 155 (2003), pro- ceedings of the Symposium on Software Development for Process and Materials Design.

[74] J. D. Hunter, Matplotlib: A 2d graphics environment, *Computing in Science Engineering* **9**, 90 (2007).