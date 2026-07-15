
# From electrons to phase diagrams with classical and machine learning potentials: automated workflows for materials science with pyiron

Sarath Menon ☐,¹, * Yury Lysogorskiy,² Alexander L. M. Knoll,³,⁴ Niklas Leimeroth

☐,⁵ Marvin Poul ☐,¹ Minaam Qamar ☐,² Jan Janssen ☐,¹ Matous Mrovec ☐,² Jochen

Rohrer ☐,⁵ Karsten Albe ☐,⁵ Jörg Behler ☐,³,⁴ Ralf Drautz ☐,² and Jörg Neugebauer ☐¹,†

 \( ^{1} \)  Max-Planck-Institut für Eisenforschung GmbH, 40237 Düsseldorf, Germany

 \( ^{2} \) ICAMS, Ruhr-Universität Bochum, 44801 Bochum, Germany

 \( ^{3} \) Lehrstuhl für Theoretische Chemie II, Ruhr-Universität Bochum, 44780 Bochum, Germany

 \( ^{4} \) Research Center Chemical Sciences and Sustainability,

Research Alliance Ruhr, 44780 Bochum, Germany

 \( ^{5} \) Technische Universität Darmstadt, Fachbereich Material und Geowissenschaften, Fachgebiet Materialmodellierung, 64287 Darmstadt, Germany (Dated: March 12, 2024)

We present a comprehensive and user-friendly framework built upon the pyiron integrated development environment (IDE), enabling researchers to perform the entire Machine Learning Potential (MLP) development cycle consisting of (i) creating systematic DFT databases, (ii) fitting the Density Functional Theory (DFT) data to empirical potentials or MLPs, and (iii) validating the potentials in a largely automatic approach. The power and performance of this framework are demonstrated for three conceptually very different classes of interatomic potentials: an empirical potential (embedded atom method - EAM), neural networks (high-dimensional neural network potentials - HDNNP) and expansions in basis sets (atomic cluster expansion - ACE). As an advanced example for validation and application, we show the computation of a binary composition-temperature phase diagram for Al-Li, a technologically important lightweight alloy system with applications in the aerospace industry.

## I. INTRODUCTION

The advent of machine learning interatomic potentials (MLPs) is revolutionising the field of computational materials science, enabling simulations of large systems and complex material properties with ab initio accuracy  \( [1–5] \) . However, the development of these data-driven interatomic potentials is a computationally intensive task that needs automated and reliable workflows.

The life cycle of MLP development can be broadly divided into the following tasks: (i) generating a database containing reference data, (ii) fitting the model parameters to the reference data, and (iii) validating the resulting parametrization for a specified range of properties. Furthermore, it is often necessary to provide a feedback loop between the tasks via an active learning approach to ascertain transferability  \( [6, 7] \) .

The initial task of setting up the reference database usually requires to perform many thousands of density functional theory (DFT) calculations for a broad range of atomic environments that span the configuration space of interest as completely as possible. Such computations can nowadays be facilitated using either general workflow frameworks  \( [8–11] \)  or tools designed specifically for a particular MLP class  \( [12–17] \) . Nevertheless, there is still lack of standardized workflow setups, computational metaparameters and structural databases. Therefore, each research group relies mostly on their own expertise and experience. This may not only lead to inconsistencies in the generated data (for instance, due to variations in DFT settings, such as the exchange-correlation functional, Brillouin zone sampling or plane wave cutoff)  \( [18, 19] \) , but it can also strongly limit exchange of data from different sources and their collection into greater databases.

The situation remains similar when it comes to the second stage of MLP development, namely, fitting the model parameters. Many optimization algorithms and software tools are tailored to a particular class of potentials and are not easily transferable. Thus, a researcher must not only identify an appropriate type of potential that is suited for the system of interest, but often needs to learn a variety of specific software tools each of which uses its own terminology.

The final task in the development cycle is a thorough validation of the fitted parametrization. It should be stressed that simple correlations between the predictions of the potential and the reference DFT data, e.g. for energies and forces, are in most cases not sufficient and may be even misleading. It is crucial to evaluate not only fundamental physical properties, such as energy-volume curves, elastic moduli or phonon spectra, but to perform also dynamical simulations at finite temperatures that scrutinize spurious behavior of the model outside of the training domain. Existing initiatives  \( [20–22] \)  have mostly focused on classical interatomic potentials while automated validations of MLPs are still rare  \( [23] \) . This makes it difficult for users to determine a safe application range of a particular MLP parametrization for their applica-
 
![](./images/976997418136502272_1.jpg)

FIG. 1: A schematic illustration of the MLP development cycle. Here, pyiron is employed as a workflow manager to combine different software tools and packages.

tion. A thorough validation is also indispensable before applying the model in simulations of complex material properties, such as studies of extended defects, phase transformations, or predictions of phase diagrams.

Our aim is to demonstrate the whole MLP development cycle for three representative model potentials to elucidate the complete process to interested researchers, not on a benchmark comparison of different types of potentials. We introduce a set of standardised workflows that cover all aspects from generation of DFT data to MLP fitting and validation, as schematically illustrated in Fig. 1. As an example of an advanced application, we evaluate the phase diagrams for a prototypical binary system. The workflows presented here are reusable, reproducible, and most importantly, largely automated. While exposing all intricacies of the methods involved, we show that they significantly reduce the technical complexity. By providing the computer codes and software tools, we encourage to use this manuscript as a practitioner's guide into the field of modern MLP development as well as advanced thermodynamic applications.

As a model case, we chose the binary Al-Li system  \( [24, 25] \) . Al-Li alloys are well suited for aerospace applications since they exhibit low density and high mechanical strength  \( [26, 27] \) . Apart from a recent work  \( [28] \) , there is a lack of interatomic potential for this system, making it both desirable and a challenging option from the perspective of MLP development. We selected three prototypical examples of interatomic potentials: a classical central-force potential based on the embedded atom method (EAM)  \( [29, 30] \) , a high-dimensional neural network potential (HDNNP)  \( [31, 32] \) , and the atomic cluster expansion (ACE)  \( [6, 33] \) . We use calphy  \( [34] \)  for the calculation of phase diagram, and employ pyiron  \( [11] \)  as a workflow creation and management environment to bring together various software tools. Our goal is to enable seamless creation and validation of interatomic potentials while taking a step towards the FAIR (Findable, Accessible, Interoperable, and Reusable) data and software principles  \( [35, 36] \)  in the field of MLP development.

## II. RESULTS

## A. pyiron as a platform for automated workflows

We employ pyiron \( ^{[11]} \)  as a workflow environment for all stages of the MLP development and validation, as illustrated in Fig. 1. The development cycle is facilitated with pyiron by connecting the fundamental building blocks:

1. Generic and easy-to-use structure generation tools that combine standard software libraries in the field of computational materials science such as ASE [37], pymatgen [38], PyXtal [39], and others in a convenient and interoperable package;
 

2. An interoperable interface to a variety of electronic structure and atomistic simulation software packages such as VASP  \( [40–42] \)  and LAMMPS  \( [43] \) ;

3. A common storage format for energies, forces and stresses that can be used efficiently for hundreds of thousands of training configurations implemented in pyiron as the class TrainingContainer (see Sec. III E 4);

4. A common interface to the fitting tools used in this work, namely, pacemaker  \( [22, 44] \) , RuNNer  \( [45–47] \) , and atomicrex  \( [48] \) , implemented in pyiron as the PotentialFit class;

5. A common interface to validation workflows and tools for thermodynamic properties such as phonopy [49] and calphy [34].

Block (1) enables users with different backgrounds to generate easily new configurations or to import them from existing databases. The common interface in Block (2) provides a seamless switching between different quantum engines or simulation protocols to create training data with minimal changes in an existing workflow. It can also be employed to design and test a workflow using a lower-level method, which is computationally cheap, before switching to a production run using a higher-level theory. Blocks (3) and (4) provide flexibility to experiment with different MLP formalisms on the same data or selected subsets. In addition, Block (3) provides analysis and plotting routines for all types of training data generated in Block (2). Finally, Block (5) provides access to validation routines, helping a user to assess the quality of the fitted MLPs.

## B. Construction of a reference DFT dataset for the Al-Li system

Selection of the reference data needed to parametrize an interatomic potential is one of the most important steps in the life cycle of MLP development. For creation of the reference DFT data we employed VASP 5.4  \( [40–42] \) , using workflows as described in Sec. III E3. We employed the projector augmented wave (PAW) method  \( [50] \)  and the GGA-PBE exchange correlation functional  \( [51] \) . Several convergence tests were conducted to ensure the obtained energies and forces are highly accurate and consistent. These tests were carried out for three representative structures, namely, face-centered cubic (fcc) Al, body-centered cubic (bcc) Li, and the B32-type  \( \beta \) -LiAl, in a range of 30% volumetric strain around their respective equilibrium volumes. Based on these tests, the following DFT settings were used: a plane wave cutoff of 750 eV, a k-mesh spacing of  \( 0.1\ \AA^{-1} \) , and the Fermi smearing method with a width of 0.1 eV. With these settings we observed less than 0.5 meV/atom difference in the energies as compared to calculations performed at 800 eV plane wave cutoff and 0.05  \( \AA^{-1} \)  k-mesh spacing.
There exist multiple strategies for generation of relevant atomic configurations. We find that a combination of domain knowledge, active learning, and random search can be employed effectively for the construction of a balanced training dataset. In this three-step strategy, domain knowledge is employed first to select structures based on common structural prototypes available in standard crystallographic databases  \( [52] \) . Thereafter, we use active learning algorithms during validation and simulations, and random configurations obtained using a random-structure-search procedure  \( [53] \)  to augment the dataset.

The domain-knowledge step is focused on structures that are known to be important for the system of interest and to ensure that they are represented with high accuracy. In this work, we queried both elemental and binary structures with formation energies less than or equal to zero from the Materials Project database  \( [52] \) . Subsequently, a series of transformations was applied to these structures and their supercells, including uniform and non-uniform deformations of the cells and random displacements of atoms (see Supplementary information for details). These steps ensure that not only perfect bulk structures but also their distortions, which are crucial to reproduce elastic and vibrational properties, are included in the training data.

We then used active learning to ensure that even during extended simulations, which are needed to compute thermodynamic properties (See Sec. III E 8), potentials remain stable and accurate. Within the active learning loop, we iteratively selected structures based on high uncertainty indicators  \( [54] \)  derived from running molecular dynamics simulations for several Al-Li phases of interest.

Finally, we added random structures that are far from equilibrium. This step ensures a broader coverage of the configurational space. Relying on domain knowledge and active learning only may result in a short sighted training set that hampers the extrapolation capabilities of the fitted MLPs, whereas a random sampling-based approach alone might lead to the risk of missing or underrepresenting important phases in a material. The random structures were generated following a recent workflow  \( [53] \)  that utilizes the PyXtal  \( [55] \)  software as described in Sec. III E 2. We generated an initial set of structures of each space group for varying numbers of atoms (Not all space groups can be generated for every composition of the cells due to Wyckoff multiplicity constraints.), which are then relaxed using DFT first allowing only the volume to vary, followed by a full relaxation of the cell shape and internal degrees of freedom. It is not necessary that these relaxations lead to highly accurate minima in the potential energy landscape, so low accuracy DFT calculations can be employed to speed up this step. These relaxed structures are then recomputed using the required precision to ensure consistency of the training dataset. This procedure, very similar to ab initio structure search methods  \( [56] \) , and originally developed for this purpose, has recently been applied for machine learning potentials  \( [57] \) .
 
![](./images/976997418136502272_2.jpg)

FIG. 2: Energy distribution of the DFT reference data set as a function of the atomic volume. The fraction of lithium atoms in each structure is represented by the color of the points.

primary advantage of this approach is that it can help to find basins of the potential energy surface without domain knowledge, while also exposing the potential to a greater variety of structural and chemical environments [53].

Finally, random displacements and variations of the cell shape and size were applied to the relaxed structures to obtain additional samples around the minima of the potential energy surface. Detailed parameters for the random perturbations are described in the supplementary information. The initial set of random crystals as well as structures resulting from both the minimization steps and the random perturbations are then combined and added to the training set. The complete workflow is implemented in pyiron and the primitives introduced in the previous section II.A.

Through the combination of these three strategies — domain-knowledge, active learning, and random search — we were able to construct a robust and extensive atomic structure data set that captures a wide range of configurations. The distributions of DFT reference data over energy, volume and composition are shown in Fig. 2 and further information is provided in the supplementary information.

## C. Training of data-driven interatomic potentials

The training of MLPs is usually carried out using dedicated computer codes that are tailored to a particular model architecture. In our case, we used atomicrex  \( [48] \) , RuNNer  \( [45-47] \)  and pacemaker  \( [44] \)  to fit the EAM, HDNNP and ACE parametrizations, respectively. Due to differences in the fitting procedures, the training data sets needed to be adjusted to the respective codes and models.

## 1. EAM

For the EAM potential, we started by fitting potentials for the single elements, following an approach outlined by Mishin et al. [58]. This approach guarantees an exact fit of the lattice constant, cohesive energy and bulk modulus by constraining the fitting parameters accordingly. Parameters of functions describing Al-Li were fitted while keeping the single element parameters constant. The training data was limited to the domain knowledge subgroup of the whole set, containing 2081 structures. Because the potential has less than 100 adjustable parameters, this amount of training data is sufficient, and leads to faster parametrization routines. Furthermore, the functional form of EAMs have limited flexibility, so training to randomly sampled structures far from equilibrium could impact the accuracy of the more important low-energy structures. In the fitting process, energies were weighted based on the distance of the formation energy to the convex hull  \( E_{D} \)  (in eV/atom) as

 \[ W_{E}=\frac{100}{(E_{D}+0.2)^{4}}, \quad (1) \] 

while a uniform weight of one was applied for forces. Further details about the fitting procedure are provided in the Methods section and in Ref. [58].

## 2. HDNNP

Before starting the HDNNP training process, the training data set was refined by eliminating structures which were not relevant for the material properties of interest. These included structures containing isolated atoms without any bonding partners within a radius of 12 Å, structures with large positive formation energies or highly repulsive force components, and all structures with atomic volume outside the interval of  \( 10\ \mathring{A}^{3}/atom - 50\ \mathring{A^{3}}/atom \) . In total, 4915 data points were removed.

Using RUNNERASE [47], we then carried out a grid search to optimize the hyperparameters required for the HDNNP training performed with the RuNNer code [45, 46]. In particular, this includes the number, short-range cutoff radius and parameters of the atom-centered symmetry functions (ACSFs) [59] describing the atomic
 

environments, the hyperparameters of the optimisation algorithm (Kalman filter [60]), and the neural network architecture. For each trial, HDNNPs were trained on five randomly selected mini-batches of 200 data points and three random initialization seeds each. 1 ps NVT MD rapid heating runs between 300 K and 1000 K were performed to test the capabilities of each potential in a basic application. Finally, the best hyperparameters were selected based on the training accuracy and simulation stability (length of the stable trajectories, number of extrapolations) which were achieved across the 15 members of the group. The selected hyperparameters are presented in supplementary material, Tab. III. Then, a HDNNP was trained with the selected settings on the entire training dataset, randomly separated into a training (90%) and testing set (10%). All data points have been equally weighted in the training process. The same applies to the relative weight of total energies and force components.

## 3. ACE

The ACE parameterization was carried out using the Pacemaker package  \( [44] \) . A cutoff for all interactions was set to  \( 7\AA \) , based on the range of DFT interactions. The total number of basis functions per element was set to 1000. The resulting maximum radial and angular indices, dependent on the correlation order, as well as other ACE parameters are presented in Table II in supplementary material.

The total dataset was randomly divided into training and testing sets with a ratio of 95% to 5%. Weights for the training structures were assigned based on their energy distance to the convex hull, following the energy-based weighting method [44].

The fitting was performed in two stages. In the first stage, a higher emphasis was placed on forces  \( (\kappa = 0.99) \) , while in the second stage a more balanced distribution of energy-forces weights  \( (\kappa = 0.3) \)  was used.

A strong core repulsion pair potential was added at distances below 2 Å.

## 4. Comparison of training outcomes

An overview of all training datasets as well as the achieved training accuracy for all three potentials is given in Table I and the correlations between predicted and reference values for energies and force components are provided in Fig. 3.

It is seen that all three fitting methods yield favorable training results despite the different train set sizes and compositions. In line with our expectations, the physically-inspired EAM requires the least amount of training data spanning over large energy, force and volume ranges, albeit at the cost of higher training errors. In contrast, the HDNNP and ACE utilize most of the available training data and reach smaller errors with respect to the DFT reference values than EAM. Due to the higher weighting of low-energy structures employed in the training of the ACE potential, there are less outliers around forces close to zero in Fig. 3 (c), while such a weighting has not been applied in the HDNNP training.

To facilitate the validation and to compare objectively the accuracy of all potentials, we created a single test dataset containing only structures that were not part of any training dataset. The test structures were restricted to lie within  \( 1 \, eV/atom \)  or less above the convex hull, as these represent the physically most relevant subset for the phase diagram simulations. In Table I and Fig. 3, we depict test set metrics for this common test dataset only. For all potentials, the test error metrics are smaller than those for the training datasets. In the case of ACE, the overall metrics are additionally biased due to the non-uniform distribution of energy-based weights.

## D. Validation approach and strategy

Once the potentials have been parameterized with the desired accuracy, they must be extensively validated. Energy and force RMSEs of the final fit provide a first quantitative assessment of the potentials with respect to the reference data. However, it is mandatory to evaluate a broader range of fundamental material properties and to compare them to DFT reference data, and when applicable, experimental observations.

An elementary assessment of transferability is to compare energies of important bulk phases as a function of atomic volume. This data is fitted to the Murnaghan equation of state to obtain Murnaghan curves, that contain not only valuable information about the mutual stability of various phases, but also can be used for an estimation of their bulk moduli. Fig. 4 shows the Murnaghan curves as predicted by all three potentials for the fcc phase of Al, bcc and fcc phases of Li, and four binary phases (AlLi, Al \( _{3} \) Li, Al \( _{4} \) Li \( _{9} \) , and Al \( _{2} \) Li \( _{3} \) ) that appear in the phase diagram [25].

All potentials agree well with DFT for the ground states of Al and Li, with some minor variations observed for both Li phases of the order of a few meV (Note that the ground state according to reference PBE-DFT calculations is fcc, albeit with a small energy difference compared to bcc, as seen in Fig. 4 (b)). When considering the binary phases in Fig. 4(c), a clear distinction is observed between the EAM potential and the MLPs. While the MLPs predict both the atomic volumes as well as the formation energies in excellent agreement with DFT, the EAM potential shows a considerable overestimation of the atomic volumes.

The phonons predicted by the potentials are related to vibrational properties of materials and reflect the model's behaviour for small perturbations near the equilibrium ground state structure that are relevant for an accurate reproduction of phase diagrams. Figure 5 shows the
 
![](./images/976997418136502272_3.jpg)

![](./images/976997418136502272_4.jpg)

![](./images/976997418136502272_5.jpg)

![](./images/976997418136502272_6.jpg)

![](./images/976997418136502272_7.jpg)

![](./images/976997418136502272_8.jpg)

FIG. 3: Energy and forces predicted by the potentials  \( (E_{\mathrm{pot}} \)  and  \( F_{\mathrm{pot}}) \)  compared to DFT data for (a) EAM, (b) HDNNP, and (c) ACE. The corresponding values of the RMSE and MAE are given in Table I. Note that training data (purple) is a different subset of the reference DFT dataset for each potential, while test data (orange) is based on a common test set including only structures within 1 eV/atom above the convex hull of the system.

TABLE I: Energy and force RMSE (MAE) of EAM, HDNNP, and ACE with respect to DFT. Test set metrics are given for a common test set including only structures within 1 eV/atom above the convex hull of the system. The size of the dataset and the energy, force and volume ranges of training and testing data are also summarized.

<table><tr><td rowspan="2">Potential</td><td rowspan="2" colspan="2">Dataset Size</td><td rowspan="3">Energy Range [eV Atom \( ^{-1} \) ]</td><td rowspan="3">Force Range [eV Å \( ^{-1} \) ]</td><td rowspan="3">Volume Range [Å \( ^{3} \)  atom \( ^{-1} \) ]</td><td colspan="2">E RMSE (MAE) [meV atom \( ^{-1} \) ]</td><td colspan="2">F RMSE (MAE) [meV Å \( ^{-1} \) ]</td></tr><tr><td rowspan="2">Train</td><td rowspan="2" colspan="2">Test</td></tr><tr><td>EAM</td><td>2081</td><td>58</td><td>52</td><td>235</td><td>554 (82.2)</td><td>118 (89.9)</td><td>192 (116)</td></tr><tr><td>HDNNP</td><td>50834</td><td>3.5</td><td>20</td><td>40</td><td>10.6 (7.1)</td><td>10.2 (6.9)</td><td>64.2 (30.6)</td><td>49.2 (21.0)</td></tr><tr><td>ACE</td><td>51082</td><td>50</td><td>40</td><td>600</td><td>12.2 (7.5)</td><td>9.6 (6.6)</td><td>41.4 (16.9)</td><td>26.5 (11.7)</td></tr></table>

phonon densities of states for fcc Al, bcc Li, AlLi and  \( Al_{3}Li \) . Note that we restrict ourselves to the two binary phases with  \( x_{Li} \leq 0.5 \) , as this is the region considered in the phase diagram calculations (see Sec. II E). Similar to the Murnaghan curves, it is observed that HDNNP and ACE both predict the phonon DOS with good accuracy, while the EAM potential shows significant deviations for the binary phases.

As an initial step before evaluating the binary phase diagram, we evaluate and plot the formation energies of the binary phases as a function of Li content in Fig. 6. The so-called convex hull can in fact be thought of as a binary phase diagram at zero Kelvin. The convex hull plot allows the formation energies to be directly compared to DFT and our calculations show that both HDNNP and ACE predict the formation energies well with DFT accuracy while EAM predictions deviate from the reference.

The elastic matrix elements  \( C_{11} \) ,  \( C_{12} \)  and  \( C_{44} \)  for the fcc Al and bcc Li ground states are computed with the fitted potentials and reported in Table II. For fcc Al, the machine learning potentials match the DFT reference data very well while the EAM potential overestimates  \( C_{11} \)  and underestimates the other two elastic constants. For bcc Li, all potentials provide a good description of the elastic matrix.
 
![](./images/976997418136502272_9.jpg)

![](./images/976997418136502272_10.jpg)

![](./images/976997418136502272_11.jpg)

FIG. 4: Equation of state curves for (a) pure fcc Al, (b) pure bcc and fcc Li, and (c) different AlLi compounds as predicted by the EAM, HDNNP, and ACE potentials. The DFT reference is shown in black. In (b), as the bulk modulus of Li (11 GPa for bcc and 13 GPa for fcc) is lower than the respective value of Al (76 GPa), the range of energies is small, approximately 0.02 eV/atom, resulting in rather large visual discrepancies. For the binary compounds in (c), the predictions of the HDNNP, ACE, and DFT essentially coincide, and are thus hardly distinguishable.

![](./images/976997418136502272_12.jpg)

![](./images/976997418136502272_13.jpg)

![](./images/976997418136502272_14.jpg)

![](./images/976997418136502272_15.jpg)

FIG. 5: Phonon density of states for (a) fcc Al, (b) bcc Li, (c) AlLi, and (d)  \( Al_{3}Li \) , as predicted by EAM, HDNNP, and ACE in comparison with the DFT reference.

TABLE II: Elastic constants of elemental aluminium and lithium, given in GPa, as predicted by the three potentials and the DFT reference method.

<table><tr><td></td><td colspan="4">Al-fcc</td></tr><tr><td></td><td>DFT</td><td>EAM</td><td>HDNNP</td><td>ACE</td></tr><tr><td>C11</td><td>129</td><td>98</td><td>131</td><td>130</td></tr><tr><td>C12</td><td>52</td><td>67</td><td>67</td><td>57</td></tr><tr><td>C44</td><td>32</td><td>46</td><td>49</td><td>39</td></tr><tr><td></td><td colspan="4">Li-bcc</td></tr><tr><td>C11</td><td>15</td><td>15</td><td>12</td><td>13</td></tr><tr><td>C12</td><td>13</td><td>14</td><td>13</td><td>12</td></tr><tr><td>C44</td><td>11</td><td>12</td><td>12</td><td>11</td></tr></table>

## E. Construction of thermodynamic phase diagrams

Phase diagrams provide critical information about the material system, the phases that are predicted to be stable at the given thermodynamic conditions, and the conditions at which one phase transitions to another, or two phases coexist. Phase diagrams are, therefore, a crucial and challenging test for interatomic potentials. In general, the given interatomic potential should be able to reproduce the key aspects of the phase diagram, or at least parts of it, pertaining to the expected thermodynamic region where the interatomic potential is to be employed.

The CALPHAD method [61] is perhaps the most well-known method for the calculation of phase diagrams, aided by experimental observations of thermodynamic properties of a system. From an atomistic perspective, different methods exist for the determination of phase diagrams [62, 63]. Broadly, the methods either evaluate phase stability directly, through approaches such as coexisting phase simulations [64–66], or indirectly, by determining the Gibbs free energy or chemical potential
 
![](./images/976997418136502272_16.jpg)

FIG. 6: The convex hull for the Al-Li binary system as predicted by EAM, HDNNP, and ACE. The black dashed line connects the points along the DFT convex hull.

of the relevant phases [67]. We follow the approach of calculating free energies, using the thermodynamic integration method, in which the free energy difference between a given system and a reference system is calculated [68, 69]. We combine thermodynamic integration with non-equilibrium Hamiltonian interpolation and reversible scaling to obtain the free energies efficiently (see Methods for more details). The workflow for such a calculation boils down to the code as described in Sec. III E8. For this methodology, a priori information about the relevant phases is needed, which is motivated by the currently established phase diagram [25, 70]. In order to have a set of robust, automated, and efficient workflows for the phase diagram determination, we consider only substitutional defects in the off-stoichiometric compounds, and limit ourselves to the left side of the phase diagram, until  \( x_{Li} = 0.5 \) . Therefore, we consider the fcc Al, AlLi in the bcc-like B32 lattice, and the liquid. Furthermore, the  \( L1_{2} \)   \( Al_{3}Li \)  appears as a metastable phase in the experimentally determined phase diagram [70], and on the convex hull determined through DFT calculations (see Fig. 6), which makes it an interesting candidate to be considered in the calculation of the phase diagram.

For pure Al, we present the pressure-temperature P-T phase diagrams. In order to arrive at the P-T phase diagrams, the free energies of the relevant phases are calculated as a function of temperature and pressure. To this end, we perform reversible scaling calculations which provide the free energy over a given temperature range. A pressure range of 0-40 GPa is chosen, with free energy calculations carried out at intervals of 10 GPa. The fcc and liquid phases are considered, and at each pressure, the melting temperature is obtained from the intersection of the free energy curves. A system size of approximately 7000 atoms is chosen for both phases such that any finite size effects are avoided. The same set of calculations is performed with all three potentials, the results of which are shown in Fig. 7. In general, all three potentials closely follow the predictions from experiments. Although the zero pressure melting temperature is underestimated compared to the experimental value [71], it is comparable with the melting temperature from ab initio calculations [72].

![](./images/976997418136502272_17.jpg)

FIG. 7: Melting curve of fcc Al up to 40 GPa. The melting temperature,  \( T_{m} \) , at various pressures is calculated for EAM, HDNNP, and ACE. Melting temperatures determined from laser melting experiments [73] are marked in gray.

For the construction of the binary phase diagram, the fcc and liquid are considered in the composition range  \( 0 \leq x_{Li} \leq 0.5 \) , and B32 AlLi in  \( 0.4 \leq x_{Li} \leq 0.5 \) , and  \( Al_{3}Li \)  in  \( 0.2 \leq x_{Li} \leq 0.3 \) . We chose the composition ranges for AlLi and  \( Al_{3}Li \)  based on the relevant regions in the experimental phase diagram. We then ascertain that the free energies of these phases were significantly higher than the other phases outside of the selected composition range. In order to create an Al-rich fcc lattice with Li as impurity, Al atoms are randomly selected and replaced by Li, that is, we assume that Li impurities occupy substitutional lattice positions. Similarly, substitutional Al impurities are introduced in the B32 structure to create off-stoichiometric compositions. No other mechanisms, such as vacancies, or interstitials are considered.

Within the selected composition range, we perform free energy calculations at composition intervals of 0.01 for all the phases. At each composition, temperatures from 600-1000 K are considered, and the free energy over this range is obtained in a single calculation using the reversible scaling approach. Free energy calculations are then performed with timescales of 25 ps for equilibration, 50 ps for switching, and system size of roughly 7000 atoms for each phase.

Once the free energies are obtained, at each tempera-
 
![](./images/976997418136502272_18.jpg)

FIG. 8: Free energy of mixing,  \( \Delta F \) , for fcc, liquid, AlLi, and  \( Al_{3}Li \)  at 800 K as a function of the composition of Li, calculated with the ACE potential. Substitutional impurity atoms are added in each of the phases to obtain free energy variation with composition (up to 0.5 Li). The two-phase coexisting regions are identified through common tangent constructions, indicated by black dashed lines.

ture the free energy for each phase with varying composition is extracted, as shown in Fig. 8. A current limitation of our workflow is that it does not include the contribution to the free energy due to configurational entropy in the solid phase, therefore the ideal mixing contributions are added to the fcc, B32, off-stoichiometric phases. In order to calculate the free energy of mixing, the endmembers are chosen to be the phases with the lowest free energy at  \( x_{Li} = 0 \)  and  \( x_{Li'} = 0.5 \)  at the given temperature. Finally, the convex hull is calculated at each temperature to extract the regions of stability for each phase. Following such a construction, the regions of phase stability and coexistence can be obtained. Once again, the calculations are performed for all three potentials and the results are shown in Fig. 9 (a-c). The reference phase diagram calculated using the CALPHAD approach as implemented in the pycalphad [74] tool, with an AlLi database from Ref. [75], is shown in Fig. 9 (d).

The HDNNP and ACE exhibit phase diagrams (Fig. 9 (b, c)) show excellent agreement with both the CALPHAD and the experimental phase diagrams. The main features of the phase diagram, such as the solubility of Li in the Al lattice, the eutectic point (liquid  \( \rightarrow \)  fcc + AlLi), general shape of the liquidus lines are all well reproduced. A comparison of the melting temperature of the end members, eutectic temperature, eutectic composition, and the solubility of Li in the fcc Al lattice are shown in Table III. Both MLPs underestimate the melting temperatures and the eutectic temperature by approximately 15 %, which is expected from the melting temperature of the underlying DFT reference ([76, 77] and [78] with references therein). The prediction of a lower melting temperature by the MLIPs are also evident at increasing pressure, as seen from Fig. 7. Both the eutectic composition and Li solubility, are close to the ranges in experimental observations.

A major difference is the solubility of Al in the AlLi ordered phase. Experimental and CALPHAD show solubility, while HDNNP and ACE predict predictions are on the contrary. This discrepancy could be due to a limitation in the phase diagram calculation workflows rather than the interatomic potentials. In B32 AlLi, experimental studies propose that at lower Li concentrations, the Li atoms exhibit a vacancy mediated diffusion mechanism  \( [79] \) . The exclusion of vacancies in favor of substitutional defects could lead to the low solubility of Al in the AlLi phase.

Although the  \( Al_{3}Li \)  phase is present on the DFT convex hull, it does not appear in the calculated phase diagram in the given temperature range. At lower temperatures, the ACE potential predicts regions of coexistence of the FCC and  \( Al_{3}Li \) , and  \( Al_{2}Li \)  and AlLi, which disappears around 580 K (See supplemental).

The phase diagram of the EAM potential, as represented in Fig. 9 (c), does not reproduce the characteristic features of the phase diagram, indicating the possible limitations of an empirical interatomic potential. Even though the EAM potential provides the closest estimate of the melting temperature of pure Al as compared to experiments, it predicts the stability of the competing phases incorrectly. Therefore, the applicability of the EAM potential in this study is limited to properties of the pure phases, such as the elastic constants.

Overall, to obtain the phase diagram presented in this work for a potential, we require about 120 molecular dynamics simulations of about 150 ps each, making this approach computationally feasible even with the more expensive MLPs. Apart from the selection of relevant phases and temperature ranges, the rest of the workflow can be fully automated, allowing for the calculation of phase diagrams to be a routine task in the lifecycle of interatomic potential development. We observe that a 1 meV difference in free energy of phases leads to about 20 K difference in the calculated transition temperature; this, in turn, combined with the limitations of DFT in predicting transition temperatures, indicates that a 15-20 % difference in transition temperatures as compared to the experimental phase diagrams is to be expected. Nevertheless, the calculated phase diagrams are highly beneficial to predict the thermodynamic conditions under which an interatomic potential is reliable, and for the interpretation of the observed phase transformation behavior.

## F. Conclusions and outlook

In conclusion, our presented framework, built upon the pyiron integrated development environment (IDE), es-
 
![](./images/976997418136502272_19.jpg)

![](./images/976997418136502272_20.jpg)

![](./images/976997418136502272_21.jpg)

![](./images/976997418136502272_22.jpg)

FIG. 9: Phase diagram of Al-Li up to  \( x_{Li}=0.5 \) , calculated using (a) EAM, (b) HDNNP, and (c) ACE. In (d), the phase diagram calculated using the CALPHAD method is shown.

TABLE III: Comparison of the salient features of the phase diagram: the melting temperature of the end members, eutectic temperature, eutectic composition and the Li solubility in fcc Al at the eutectic temperature as predicted by the different interatomic potentials. The melting temperature of fcc Al from DFT calculations is estimated to be 786 - 890 K [72], depending on the chosen exchange-correlation functional (see Sec. III B). Note that since the eutectic point does not appear in the phase diagram predicted by the EAM potential, the values are an estimation.

<table><tr><td colspan="2">Potential Melting temperature (K),  \( x_{\mathrm{Li}} = 0.0 \)</td><td colspan="2">Melting temperature (K),  \( x_{\mathrm{Li}} = 0.5 \)</td><td colspan="2">Eutectic temperature (K)</td><td colspan="2" rowspan="2">Liquid composition  \( x_{\mathrm{Li}} \)</td><td rowspan="2">Li solubility  \( x_{\mathrm{Li}} \)</td></tr><tr><td>EAM</td><td>961</td><td>782</td><td>&lt;500</td><td>0.25 - 0.35</td><td>0.1 - 0.2</td></tr><tr><td>HDNNP</td><td>871</td><td>846</td><td>786</td><td>0.33</td><td>0.20</td><td></td><td></td><td></td></tr><tr><td>ACE</td><td>886</td><td>837</td><td>771</td><td>0.32</td><td>0.21</td><td></td><td></td><td></td></tr><tr><td>Exp.</td><td>933 [71]</td><td>965-991 [25]</td><td>871-876 [25]</td><td>0.234 - 0.300 [25]</td><td></td><td>0.124 - 0.180 [25]</td><td></td><td></td></tr><tr><td>DFT</td><td>786 - 890 [72]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

tablishes a comprehensive, robust, and user-friendly platform for the development of empirical and machine learning potentials. We have successfully demonstrated its versatility by running all tasks necessary in the development cycle of modern interatomic potentials, covering the creation of systematic Density Functional Theory databases, the fitting of DFT data to various interatomic potentials (EAM, HDNNP, and ACE), and the subsequent validation through a largely automated approach. The power and performance of the framework were exemplified in the computation of a binary composition-temperature phase diagram for the Al-Li alloy system, showcasing its applicability to running highly complex simulation protocols over large datasets consisting of thousands of individual atomic structures and for technologically important and complex materials systems.

The potential applications of the framework presented here are vast. Its user-friendly nature and adaptability make it an accessible and open tool for researchers in diverse fields, offering a streamlined approach to MLP development. Future efforts may focus on expanding the range of potential classes that can be incorporated, further enhancing the flexibility and applicability of the framework to a wide range of materials science challenges requiring complex simulation protocols. Ongoing developments will seek to optimize and automate additional aspects of the MLP development cycle allow-
 

ing researchers to address even more advanced materials properties needed e.g. to compute defect phase diagrams, thermoelectric behavior, or superconductivity, thus paving the way for more efficient and reproducible research practices.

We envision our presented framework to act as a foundational platform, inviting researchers to explore and study the opportunities opened by machine learning potentials and their diverse applications. The ongoing commitment to openness, reproducibility, and automation positions our framework as a flexible and expandable basis for innovation and discovery in the quickly expanding landscape of using machine learning approaches in materials science. We therefore encourage the community to actively engage with the provided computer codes and software tools, which are openly provided via github and conda.

## III. METHODS

## A. Workflows in materials science

The last few years showed a tremendous change in how high-performance compute clusters are used: While historically large monolithic codes allowed an up-scaling on an increasing number of cores, with the advent of machine learning a new type of computations becomes more and more important where huge numbers of small and medium-sized jobs running various codes need to be combined to get the final result. A prominent example is the fitting and validation of machine learning potentials described in this paper. The number of DFT calculations needed to get high-quality potentials is in the range of a few ten thousands up to several hundreds of thousands individual DFT calculations. Data management for such a large number of jobs requires not only storing the input and output data but also of their status, i.e., whether they ran successfully, whether they converged, or whether they were aborted. If a jobs fail, they need to be resubmitted and it may be necessary to correct their input. For job sizes of a few 10,000 calculations, even small failure rates make a manual handling inefficient. For these types of advanced calculations automated workflow systems become almost mandatory.

In the present work, we have used pyiron  \( [11] \)  as a workflow platform to include all the necessary tools to create advanced machine learning potentials. pyiron provides features that are well-suited for these tasks: It provides an easy way to run large numbers of DFT calculations (to create the reference data set), to perform the training, and to analyze extensive sets of interatomic potential calculations (for validation). pyiron provides several features that make running such complex workflows efficient and intuitive for users. Its generic input and output provide an easy way to substitute one DFT code or potential/ML approach with another one. For example, to replace the DFT code the main change would be to change the job type. The generic input specifying the basis set, k-point sampling etc. remains unchanged and will be translated by pyiron into the code-specific format. The close integration within the Jupyter ecosystem provides interactive and easy access to all workflow components and data, and the availability of advanced job management tools provides an efficient route to upscale and run all calculations on modern supercomputer architectures.

## B. DFT Calculations

Density Functional Theory (DFT) is a quantum mechanical modeling approach that has become the de facto standard for ab initio computations of materials properties, especially for larger system sizes. This method allows for the calculation of materials properties without the need for fitting or empirical parameters, offering a rigorous and first-principles-based framework for providing the large data sets needed to fit empirical or machine learning potentials. In DFT, a pivotal approximation lies in the exchange-correlation (xc) functional. This approximation enables the reduction of the high-dimensional many-body interaction to a 3D mean field potential incorporated into the Kohn-Sham equations.

A restriction of all available xc-functionals is that they cannot be systematically improved, i.e., deviations to experiment are inherent. Common functionals, such as the PBE-GGA functional employed in this study, generally demonstrate good agreement with experimental results. However, it is important to note that deviations exist, with errors in bond lengths typically around 1%, discrepancies in elastic constants potentially reaching 10% and errors in the melting temperature in the order of 100 K. \( ^{[76, 77]} \) 

While the exchange-correlation functional represents the only non-controllable approximation in DFT, there exist other parameters that can be used to systematically improve accuracy, albeit at an increased computational cost. Among these, the plane wave energy cutoff, which defines the completeness of the basis set, and the k-point sampling are particularly crucial. Achieving convergence in material properties concerning the choice of these parameters is imperative, especially when employing DFT data for training interatomic potentials. Inadequate convergence does not only lead to often non-systematic deviations from converged results but also introduces noise-like discontinuities in the energy surface due to the discrete nature of the plane wave basis set and the k-point set. For the generation of DFT datasets for potential fitting, it is therefore crucial to carefully select these convergence parameters to ensure that the amplitude of discontinuous fluctuations remains small compared to the targeted error. To be used for development of MLIPs, this typically means an energy convergence to about 1 meV/atom and a force convergence to about 0.1 eV/Å.

When carefully choosing these convergence parame-
 

ters, DFT is known to smoothly interpolate between similar structures. This characteristic renders DFT particularly well-suited for applications demanding a smooth energy surface and derivatives (e.g. forces and stresses) such as developing interatomic potentials.

## C. Interatomic potentials

## 1. EAM

In EAM potentials the energy of the system is given by a pair potential V and a nonlinear function F, called embedding energy

 \[ E=\frac{1}{2}\sum_{i j}V(r_{i j})+\sum_{i}F(\rho_{i}). \quad (2) \] 

Here,  \( \rho_{i} \)  is given by  \( \rho_{j} = \sum_{j} \rho(r_{ij}) \)  and is called electron density. It is motivated by viewing each atom in a solid as impurity that is embedded in the host matrix and therefore subject to its electron density, leading to attractive chemical interactions. Then, V can be considered as repulsive core-core interaction. [29] In modern EAM potentials V,  \( \rho \)  and F are chosen to best reproduce certain properties and do not necessarily follow the constraints resulting from this motivation, e.g. V often includes attractive terms. When freely choosing these functions the EAM formalism is equivalent to the effective-medium [80] and Finnis-Sinclair [81] potentials. The potential we fitted closely follows a procedure applied by Mishin et al. [58]. Details on the employed functional forms and constraints can be found in the original reference and the supplemental information.

## 2. HDNNP

The general ansatz underlying the development of second-generation HDNNPs, introduced in 2007 by Behler and Parrinello [31, 32], is that the total energy  \( E_{tot} \)  of a system can be decomposed into M environmental-dependent atomic energy contributions  \( E_{i} \) , such that

 \[ E_{\mathrm{t o t}}=\sum_{i=1}^{M}E_{i}(\vec{G}_{i}(\vec{r})). \quad (3) \] 

This approach, which extended the applicability of MLPs to condensed systems containing large numbers of atoms, is based on the assumption that for many systems the atomic energy to a good approximation is a local property that depends only on the interaction of a central atom with its neighboring atoms inside a sphere of radius  \( r_{c} \) . The environment inside this cutoff sphere is captured by a vector  \( \vec{G}_{i} \)  of atom-centred symmetry functions, which in turn depend on the coordinates of all neighbours while maintaining the mandatory rotational, translational and permutational invariances. The functional form of these many-body descriptors is described in more detail elsewhere \( ^{[59]} \) . Each entry in  \( \vec{G}_{i} \)  is passed to an input node of an element-specific dense feed-forward neural network, which provides the atomic energy as its output.

During training, the weights of all atomic neural networks are iteratively updated based on the loss gradients of both the total energies and the atomic force components in the training data set to achieve the best match to the reference values in the training set. Further information on the construction and training of HDNNPs can be found in  \( [45] \)  and  \( [7] \) .

## 3. ACE

The atomic cluster expansion (ACE) [33] introduces basis functions that are complete in the space of atomic environments. In analogy to HDNNPs and other MLPs, the energy is represented by a sum of individual atomic energies within a cutoff sphere, for N atoms,

 \[ E_{t o t}=\sum_{i}^{N}E_{i}. \quad (4) \] 

The individual energies are calculated from general, abstract atomic properties  \( (\varphi_{i}) \) , which in ACE are expanded as

 \[ \varphi_{i}=\sum_{v}^{n_{v}}c_{v}B_{i v}, \quad (5) \] 

where  \( c_{v} \)  are the expansion coefficients for the  \( n_{v} \)  basis functions  \( B_{iv} \) . In linear ACE,  \( E_{i} \)  is written directly as

 \[ E_{i}=\varphi_{i}. \quad (6) \] 

However, a more efficient approach is to calculate atomic energies as

 \[ E_{i}=\mathcal{F}(\varphi_{i}^{(1)},\varphi_{i}^{(2)},...,\varphi_{i}^{(P)}), \quad (7) \] 

where F can be any general non-linear function. The ACE potential used in this work employs a mildly nonlinear form with two atomic properties and a square-root embedding as in the Finnis-Sinclair method

 \[ E_{i}=\varphi_{i}^{(1)}+\sqrt{\varphi_{i}^{(2)}}\quad. \quad (8) \]
 

## D. Thermodynamics

One of the most widely employed techniques to calculate free energies through atomistic simulations is thermodynamic integration  \( [68, 69] \) . In this computational technique, a system of interest and a reference system with known free energy are coupled with a parameter  \( \lambda \) . The Hamiltonian of the combined system is given by

 \[ H(\lambda)=\lambda H_{f}+(1-\lambda)H_{i} \quad (9) \] 

where  \( H_{i} \) , is the initial or reference system with the known free energy, and  \( H_{f} \)  is the final system, or the system of the interest. If the system of interest is in the solid state, we use a non-interacting Einstein crystal [82] as the reference state, while for liquids, an Uhlenbeck-Ford model [83] is employed. The free energy difference between the two systems can be calculated as

 \[ F_{f}=F_{i}=\int_{\lambda=0}^{\lambda=1}d\lambda\bigg\langle\frac{\partial H(\lambda)}{\partial\lambda}\bigg\rangle_{\lambda}. \quad (10) \] 

The integration has to be performed over a discretized  \( \lambda \)  array, and therefore is computationally quite expensive, which calls for methodological improvements. In the non-equilibrium approach to thermodynamic integration [84], the coupling parameter  \( \lambda \)  is time-dependent, and the switching between the initial and final system is carried out in both forward and reverse directions in a single time-dependent calculation. The work done in such a switching process is calculated as,

 \[ W^{s}=\int_{t_{i}}^{t_{f}}\frac{d\lambda(t)}{d t}\frac{\partial H(\lambda)}{\partial\lambda}d t \quad (11) \] 

which is related to the free energy difference  \( \Delta F \)  between the two systems,

 \[ \Delta F=W^{r e v}=W^{s}-E^{d}. \quad (12) \] 

 \( E^{d} \)  is the energy dissipation in the switching process, which can be obtained as the difference between the forward and reverse switching. The non-equilibrium approach can be used to efficiently calculate the free energy of the system of interest at a given thermodynamic condition  \( (P, T) \) . Once a free energy  \( F(P, T) \)  is known the free energy as a function of temperature over a given range from T to  \( T_{f} \)  can be obtained in a single calculation using the reversible scaling approach [85]. These approaches, and associated algorithms have been discussed in more detail in Ref. [34].

## E. Software

## 1. pyiron

pyiron is a workflow framework for atomistic simulation, focused on rapid prototyping and up-scaling simulation protocols. Based on an object-oriented approach, the individual components of a simulation protocol in pyiron are combined like building blocks. Each pyiron object is connected to the jupyter-based user-interface, the data storage interface which combines a structured database (SQL) and a hierarchical file format (HDF5) as well as the resource interface to connect to computing resources and parameter databases. By implementing the potential fitting codes (atomicrex, RuNer and pacemaker), the simulation codes (LAMMPS and VASP) and the thermodynamics code (calphy) based on the same job class, the technical complexity of executing the underlying codes is greatly reduced.

As a first step of the simulation protocol a new project is initialized: pr = Project("All"). The project object is represented as a folder on the file system and all calculations in this project are going to be executed in this folder. From the project object the individual job objects are created using the factoring pattern:

## job = pr.create.job.SimulationCode('job_name')

The factoring pattern, which refers to using one object to create objects of different types, has two advantages: On the one hand it allows the users to use autocompletion in selecting the new object to create and on the other hand the newly created object can be already initialized with information of the object it is created from. In this case the job object receives its storage location from the project object is was created from. The individual job classes for the VASP DFT code, the different fitting codes and calphy and LAMMPS for validation are introduced below.

## 2. PyXtal

For the generation of random crystal structures we have wrapped the python code PyXtal in the structuretoolkit module distributed with pyiron.

import structetoolkit.build.random as stark
al_li_structures = stark.pyxtal(
    group=[227, 194],
    species=["Al", "Li"],
    num_ions=[4, 4],
    repeat=10
)

would generate a list of ten structures each of the spacegroups 227 and 194 with stoichiometry  \( Al_{4}Li_{4} \) . More advanced options as document by the PyXtal library itself, can be passed to the function as well.

## 3. VASP

Starting with the Vienna Ab initio Simulation Package (VASP) [40–42], the job object is created from the
 

project object using the factoring pattern and an atomic structure in the Atoms format defined by the Atomic Simulation Environment (ASE) is assigned:

job = pr.create.job.Vasp("job_name")
job.structure = structure

In addition to the atomic structure also the input parameters which determine the precision of the DFT calculation can be specified directly through the pyiron python interface. For this pyiron provides two interfaces, first the generic interface which is independent of the specific simulation code and second the code-specific interface, which allows users already experienced with a specific simulation code to directly modify specific input parameters. Using the generic interface the plane wave energy cutoff is set to 750 eV, the k-point density is set to 0.1 Å \( ^{-1} \)  and the level of electronic convergence is defined as  \( 10^{-8} \)  eV:

job.set_encut(750.0)
job.set_kpoints(k_mesh_spacing=0.1)
job.set_convergence_precision(
    electronic_energy=1.0e-8,
)
job.set_occupancy_smearing(
    smearing="FermiDirac",
    width=0.2,
)

The advantage of using the generic interface is that the users can switch between different DFT simulation codes by only changing the create job function call pr.create.job.Vasp(), the rest of the commands remain the same. For expert users pyiron also provides the option to access the simulation code specific input directly. As an example, while the electronic smearing can be specified using the generic set_occupancy_smearing() function, it can also be modified based on the VASP specific input file named INCAR, which can be accessed in pyiron like a python dictionary:

job.input.incar["TSMFAR"] = -1
job.input.incarn["SIGMA"] = 0.1

Finally, in addition to the simulation code-specific parameters the pyiron job object also provides the option to specify the submission to the high performance computing (HPC) queuing system:

job.server.queue = "gpu_queue"
job.server.cores = 4
job.server.gpus = 4

After the specification of the input parameters and resource assignment is completed the pyiron job object can be executed using the run() function. This triggers the internal cycle of writing the input files, submitting the calculation to the HPC for execution and once the calculation is completed parse the output files to provide the output to the pyiron python interface.

## 4. TrainingContainer

Following the execution of the DFT calculations, the next step is the aggregation of the outputs of these calculation to provide them to the fitting codes for the interatomic potentials. In pyiron this is achieved by combining two objects, the pyiron table object and the TrainingContainer. The pyiron table object specifies a series of functions which are applied to each job object in a given pyiron project, following a map-reduce pattern:

table = pr.create.table()
table.add.get_job_name
table.add.get_structure
table.add.get_energy_tot
table.add.get_forces
table.run()

The aggregated data, which is returned as a pandas DataFrame object is then stored in the TrainingContainer for reference in the fitting codes:

tr = pr.create.job.TrainingContainer("tc_job")
tr.include_dataset(table.get_dataframe())

Additionally, the class defines common plotting that makes the creation of graphs such as Figs. 6 and 4 easier, for example,

tr.plot.energy_volume()

## 5. atomicrex

The atomicrex interface exposes the full functionality of the code  \( [48] \)  in a pyiron python interface, while storing relevant inputs and output necessary to reproduce fitting processes. An atomicrex job object can be created with

job = pr.create.job.Atomicrex("AtomicrexJob")

Currently atomicrex implements EAM, modified EAM  \( [30] \) , angular dependent  \( [86] \) , analytic bond order  \( [87] \)  and Tersoff  \( [88] \)  potentials. They can be set using

pot = job.factories.potentials.potential_type()

For potentials that allow for different functional forms like EAM potentials it is necessary to define these functions. Here the user can choose between predefined functions and own creations via a math parser.

morse = job.factories.functions.morse_B(
    identifier="V",
    D0=0.05,
    r0=2.5,
    beta=2.2,
    S=2.4,
    delta=0.0,
 

species=["Al", "Li"]
uf = ref.factories.functions.user_function(identifier="UserElement1Element2", input_variable="r")
uf.expression = "A*exp(r0-r)"
uf.derivative = "-A*exp(r0-1)"
uf.parameters.add_parameter("A", 3)
uf.parameters.add_parameters("r0", 5)
pot.pair_interactions[more.identifier] = more
pot.element_densities[uf.identifier] = uf
Structures and corresponding fit properties can be directly assigned using the general TrainingContainer interface. If fine grained control over weights is required they can also be added one by one:
s = pr.create.structure.ase.bulk("Al")
job.structures.add_structure(s, identifier="SomeStructure", relative_weight=10000)
job.structures.add_scalar_fit_property("atomic-energy", target_val=-4.0, relative_weight=100,
)
Nearly arbitrary parameter constraints can be added using math parser expressions:
job.input.parameter_constraint.add_constraint(identifier="SomeConstraint", dependent_dof="constrainedParameter", expression="MathparserExpression",
)
Finally, the user can choose between an internal LBFGS minimizer and a plethora of optimization algorithms provided via the NLopt library [89] to fit the potential.
algo = job.factories.algorithms.some_algo(max_iter=1000)
job.input.fit_algorithm = algo

## 6. RuNNer

Training with RuNNer usually passes through three stages: in mode 1, the values of the atom-centered symmetry functions for the whole training dataset are calculated and stored to disk, and the data is separated into a training and a test set. mode 2 optimizes the parameters of the HDNNP in order to represent best the reference energies and forces. Finally, mode 3 is used to predict the properties of unknown configurations.

The pyiron job RuNNerFit reflects these steps. Similar to the other training jobs, it is created by invoking the create routine of a pyiron Project object. Every RuNNerFit job also requires the specification of a training dataset.
mode1 = proj.create.job.RunnerFit('mode1')
mode1.add_training_data(dataset)

In the next step, a set of atom-centered symmetry functions must be parameterized for the training dataset. runnerase offers the procedure generate_symmetryfunctions to help with this task. Afterwards, the job can be started using the run command:

sfs = generate_symmetryfunctions(dataset, sftype=2, cutoff=12.0)
model1.parameters.symfunction_short += sfs
model1.run()

After the successful termination of mode 1, mode 2 is started by reloading the first job and altering the setting runner_mode. This tells the underlying RuNNer code how to operate:

mode2 = model1.restart('mode2')
mode2.parameters.runner_mode = 2
mode2.run()

The same procedure is followed to run mode 3. In a RuNNerFit, the execution of mode 3 is mandatory to complete training and obtain a full prediction of both the train and test datasets:

mode3 = mode2.restart('mode3')
mode3.parameters.runner_mode = 3
mode3.run()

In order to use the trained potential in an application with LAMMPS, one can call the get_lammps_potential routine which returns the required pair_style and pair_coeff commands. The HDNNP pair style is part of the LAMMPS interface provided by the n2p2 package  \( [90] \) :

mode3.get_lammps_potential()

## 7. pacemaker

In order to setup the pacemaker job, one needs to create the corresponding pyiron job and add the training dataset.

job = pr.create.job.PacemakerJob("pacemaker_job")
job.add_training_data(dataset)

Parameters for ACE parameterization procedure will be initialized to their defaults. However, one always can configure all of them. For example, setting energy-force weights balance ( \( \kappa \)  from Ref. \( ^{[44]} \) ) as

job.input['fit'][loss'][kappa']=0.3

After that one can run the job and get the LAMMPS potential as well.
 

## 8. calphy

The computational approaches to obtain free energies as discussed in Section III D consists of multiple interdependent steps, and presents a complex computational workflow. In order to facilitate a user to easily calculate the free energies, and at the same time retain the ability to tune each step in the workflow as needed, we developed calphy  \( [34] \) , a python library for automated calculation of free energies. It uses LAMMPS as the molecular dynamics driver to perform free energy calculations in an automated manner. calphy when combined with pyiron, can leverage additional features such as interoperability with other common atomistic simulation tools, scaling to HPC systems, and job and data management.

Within pyiron, a non-equilibrium free calculation, for example an Al fcc lattice at 500 K and 0 pressure can be carried out by the following code:

pr = Project("free_energy")
job = pr.create.job.Calphy("Al_fcc_500")
job.structure = pr.create.structure.ase.bulk("Al", cubic=True).repeat(4)
job.potential = "Al-atomicrox"
job.calc_free_energy(
    temperature=500,
    pressure=0,
    reference_phase="solid",
    n_equilibration_steps=25000,
    n_switching_steps=50000,
)
job.run()

The main inputs needed are the input structure and the interatomic potential, apart from the thermodynamic conditions at which the calculation is to be performed. For calculating the free energy of a liquid system, the only change needed is reference_phase='liquid'. calphy automatically uses a different reference system based on this command. To obtain free energies over a given temperature range, one needs to change the temperature option: temperature=[500, 800]. In this case, a free energy calculation at 500 K is performed first, followed by a temperature integration up to 800 K in another calculation.

## 9. LAMMPS

Beyond the free energies calculated with calphy to construct the phase diagram, the LAMMPS molecular dynamics simulation code is used to validate material properties calculated with the individual machine learning potentials. In pyiron the workflows to calculate the material properties is defined independent of the specific simulation code, so in the first step a reference LAMMPS job is defined for the interatomic potential fitted with the atomicrex fitting code:
pr = Project('validation')
job = pr.create.job.Lammps('lmp')
job.structure = structure
job_lmp.potential = 'Al-atomicrox'

Following the definition of the reference job the next step is assigning this reference job to the workflow to calculate a material property, in this case the calculation of the elastic constants with the ElasticMatrix job:

elastic = pr.create.job.ElasticMatrix('elmat')
elastic.ref_job = job_lmp
elastic.run()

By defining the calculation of the material properties independent of the simulation code, the same validation calculation can be applied for the LAMMPS molecular dynamics simulation code to test the fitted interatomic potentials as well as the VASP DFT simulation code, to enable a direct comparison.

## F. Software and data availability

The software used in this paper, pyiron, pacemaker, RuNNer, atomicrex, calphy, LAMMPS, pycalphad, and PyXtal are freely available from their respective repositories. A list of the software tools, along with their repositories and documentation is provided in the supplementary material. Exemplary workflows to illustrate the calculations mentioned in this manuscript are available in an online repository \( ^{[91]} \) , along with the free energy values for the construction of the phase diagram. In addition, the dataset used for parametrization of the interatomic potentials, is also made available  \( [92] \) .

## G. Acknowledgements

The workflows, potentials, and results presented here were obtained in the framework of the POTENTIALS collaboration and scientific network “Assessment of atomistic simulations” with funding from the German Science Foundation (DFG) (grant number 405602047). Furthermore, a workshop on the subject of this manuscript at which participants could interactively execute and explore the initial versions of these workflows was held in June 2022 [93].

S. M. acknowledges funding by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under the National Research Data Infrastructure – NFDl 38/1 – project number 460247524. J. B. acknowledges funding by the DFG (project number 405479457 as part of PAK 965/1). A. K. acknowledges funding by the Studienstiftung des Deutschen Volkes (doctoral scholarship). N. L. and J. R. acknowledge funding by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under grant number 405621137. K. A. acknowledges funding from the the DFG under
 

grant number 405621160. M. M. and R. D. acknowledge funding by the German Science Foundation (DFG), projects 405621081 and 405621217. R.D. and Y. L. acknowledge computation time by Center for Interface-Dominated High Performance Materials (ZGH) at Ruhr-

[1] J. Behler, Perspective: Machine learning potentials for atomistic simulations, J. Chem. Phys. 145, 170901 (2016).

[2] V. L. Deringer, M. A. Caro, and G. Csányi, Machine learning interatomic potentials as emerging tools for materials science, Adv. Mater. 31, 1902765 (2019).

[3] O. T. Unke, S. Chmiela, H. E. Sauceda, M. Gastegger, I. Poltavsky, K. T. Schütt, A. Tkatchenko, and K.-R. Müller, Machine learning force fields, Chem. Rev. 121, 10142 (2021).

[4] P. Friederich, F. Hässe, J. Proppe, and A. Aspuru-Guzik, Machine-learned potentials for next-generation matter simulations, Nat. Mater 20, 750 (2021).

[5] J. Behler and G. Csányi, Machine learning potentials for extended systems - a perspective, Eur. Phys. J. B 94, 142 (2021).

[6] Y. Lysogorskiy, C. van der Oord, A. Bochkarev, S. Menon, M. Rinaldi, T. Hammerschmidt, M. Mrovec, A. Thompson, G. Csányi, C. Ortner, and R. Drautz, Performant implementation of the atomic cluster expansion (PACE) and application to copper and silicon, Npj Comput. Mater. 7, 1 (2021).

[7] A. M. Tokita and J. Behler, How to train a neural network potential, J. Chem. Phys. 159, 121501 (2023).

[8] S. P. Huber, S. Zoupanos, M. Uhrin, L. Talirz, L. Kahle, R. Häuselmann, D. Gresch, T. Müller, A. V. Yakutovich, C. W. Andersen, F. F. Ramirez, C. S. Adorf, F. Gargiulo, S. Kumbhar, E. Passaro, C. Johnston, A. Merkys, A. Cepellotti, N. Mounet, N. Marzari, B. Kozinsky, and G. Pizzi, Aiida 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance, Sci. Data 7, 300 (2020).

[9] K. Mathew, J. H. Montoya, A. Faghaninia, S. Dwarakanath, M. Aykol, H. Tang, I. heng Chu, T. Smidt, B. Bocklund, M. Horton, J. Dagdelen, B. Wood, Z.-K. Liu, J. Neaton, S. P. Ong, K. Persson, and A. Jain, Atomate: A high-level interface to generate, execute, and analyze computational materials science workflows, Comput. Mater. Sci 139, 140 (2017).

[10] M. Gjerding, T. Skovhus, A. Rasmussen, F. Bertoldo, A. H. Larsen, J. J. Mortensen, and K. S. Thygesen, Atomic simulation recipes: A python framework and library for automated workflows, Comput. Mater. Sci 199, 110731 (2021).

[11] J. Janssen, S. Surendralal, Y. Lysogorskiy, M. Todorova, T. Hickel, R. Drautz, and J. Neugebauer, pyiron: An integrated development environment for computational materials science, Comput. Mater. Sci 163, 24 (2019).

[12] A. I. Duff, R. Sakidja, H. C. Walker, R. A. Ewings, and D. Voneshen, Automated potential development workflow: Application to bazro3, Comput. Phys. Commun. 293, 108896 (2023).

[13] J. Zeng, D. Zhang, D. Lu, P. Mo, Z. Li, Y. Chen, M. Rynik, L. Huang, Z. Li, S. Shi, Y. Wang, H. Ye,

Universität Bochum, Germany. J.J. and J.N. acknowledge funding by the DFG under grant number 405621217. M.P. and J.N. acknowledge funding from the DFG under grant number 405621160.

P. Tuo, J. Yang, Y. Ding, Y. Li, D. Tisi, Q. Zeng, H. Bao, Y. Xia, J. Huang, K. Muraoka, Y. Wang, J. Chang, F. Yuan, S. L. Bore, C. Cai, Y. Lin, B. Wang, J. Xu, J.-X. Zhu, C. Luo, Y. Zhang, R. E. A. Goodall, W. Liang, A. K. Singh, S. Yao, J. Zhang, R. Wentzcovitch, J. Han, J. Liu, W. Jia, D. M. York, W. E, R. Car, L. Zhang, and H. Wang, DeepMD-kit v2: A software package for deep potential models, J. Chem. Phys. 159, 054801 (2023).

[14] A. Rohskopf, C. Sievers, N. Lubbers, M. Cusentino, J. Goff, J. Janssen, M. McCarthy, D. M. O. de Zapirain, S. Nikolov, K. Sargsyan, D. Sema, E. Sikorski, L. Williams, A. Thompson, and M. Wood, FitSNAP: Atomistic machine learning with LAMMPS, J. Open Source Soft. 8, 5118 (2023).

[15] S. Vandenhaute, M. Cools-Ceuppens, S. DeKeyser, T. Verstraelen, and V. Van Speybroeck, Machine learning potentials for metal-organic frameworks using an incremental learning approach, Npj Comput. Mater. 9, 19 (2023).

[16] E. Gelzinyte, S. Wengert, T. K. Stenczel, H. H. Heenen, K. Reuter, G. Csányi, and N. Bernstein, wfl Python toolkit for creating machine learning interatomic potentials and related atomistic simulation workflows, J. Chem. Phys. 159, 124801 (2023).

[17] M. Wen, Y. Afshar, R. S. Elliott, and E. B. Tadmor, KLIFF: A framework to develop physics-based and machine learning interatomic potentials, Comput. Phys. Commun. 272, 108218 (2022).

[18] P. Kratzer and J. Neugebauer, The basics of electronic structure theory for periodic systems, Front. Chem. 7, 106 (2019).

[19] E. Bosoni, L. Beal, M. Bercx, P. Blaha, S. Blügel, J. Bröder, M. Callsen, S. Cottenier, A. Degomme, V. Dikan, et al., How to verify the precision of density-functional-theory implementations via reproducible and universal workflows, Nat. Rev. Phys., 45 (2023).

[20] C. A. Becker, F. Tavazza, Z. T. Trautt, and R. A. Buarque de Macedo, Considerations for choosing and using force fields and interatomic potentials in materials science and engineering, Curr. Opin. Solid State Mater. Sci. 17, 277 (2013).

[21] L. M. Hale, Z. T. Trautt, and C. A. Becker, Evaluating variability with atomistic simulations: the effect of potential and calculation methodology on the modeling of lattice and elastic constants, Modelling Simul. Mater. Sci. Eng. 26, 055003 (2018).

[22] Y. Lysogorskiy, T. Hammerschmidt, J. Janssen, J. Neugebauer, and R. Drautz, Transferability of interatomic potentials for molybdenum and silicon, Modelling Simul. Mater. Sci. Eng. 27, 025007 (2019).

[23] Y. Zuo, C. Chen, X. Li, Z. Deng, Y. Chen, J. Behler, G. Csányi, A. V. Shapeev, A. P. Thompson, M. A. Wood, and S. P. Ong, A performance and cost assessment of machine learning interatomic potentials, J. Phys. Chem.
 

A 124, 731 (2020).

[24] A. Abd El-Aty, Y. Xu, X. Guo, S.-H. Zhang, Y. Ma, and D. Chen, Strengthening mechanisms, deformation behavior, and anisotropic mechanical properties of Al-Li alloys: A review, J. Adv. Res. 10, 49 (2018).

[25] B. Hallstedt and O. Kim, Thermodynamic assessment of the Al–Li system, Int. J. Mater. Res. 98, 961 (2007).

[26] R. Gupta, N. Nayan, G. Nagasireesha, and S. Sharma, Development and characterization of Al–Li alloys, Mater. Sci. Eng. A 420, 228 (2006).

[27] R. J. Rioja, Fabrication methods to manufacture isotropic Al-Li alloys and products for space and aerospace applications, Mater. Sci. Eng. A 257, 100 (1998).

[28] Y. Liu and Y. Mo, Assessing the accuracy of machine learning interatomic potentials in predicting the elemental orderings: A case study of li-al alloys, Acta Mater. 268, 119742 (2024).

[29] M. S. Daw and M. I. Baskes, Embedded-atom method: Derivation and application to impurities, surfaces, and other defects in metals, Phys. Rev. B 29, 6443 (1984).

[30] M. I. Baskes, Application of the Embedded-Atom Method to Covalent Materials: A Semiempirical Potential for Silicon, Phys. Rev. Lett. 59, 2666 (1987).

[31] J. Behler and M. Parrinello, Generalized neural-network representation of high-dimensional potential-energy surfaces, Phys. Rev. Lett. 98, 146401 (2007).

[32] J. Behler, Four generations of high-dimensional neural network potentials, Chem. Rev. 121, 10037 (2021).

[33] R. Drautz, Atomic cluster expansion for accurate and transferable interatomic potentials, Phys. Rev. B 99, 014104 (2019).

[34] S. Menon, Y. Lysogorskiy, J. Rogal, and R. Drautz, Automated free-energy calculation from atomistic simulations, Phys. Rev. Mater. 5, 103801 (2021).

[35] M. D. Wilkinson, M. Dumontier, I. J. Aalbersberg, G. Appleton, M. Axton, A. Baak, N. Blomberg, J.-W. Boiten, L. B. da Silva Santos, P. E. Bourne, J. Bouwman, A. J. Brookes, T. Clark, M. Crosas, I. Dillo, O. Dumon, S. Edmunds, C. T. Evelo, R. Finkers, A. Gonzalez-Beltran, A. J. Gray, P. Groth, C. Goble, J. S. Grethe, J. Heringa, P. A. 't Hoen, R. Hooft, T. Kuhn, R. Kok, J. Kok, S. J. Lusher, M. E. Martone, A. Mons, A. L. Packer, B. Persson, P. Rocca-Serra, M. Roos, R. van Schaik, S.-A. Sansone, E. Schultes, T. Sengstag, T. Slater, G. Strawn, M. A. Swertz, M. Thompson, J. van der Lei, E. van Mulligen, J. Velterop, A. Waagmeester, P. Wittenburg, K. Wolstencroft, J. Zhao, and B. Mons, The FAIR Guiding Principles for scientific data management and stewardship, Sci. Data 3, 160018 (2016).

[36] N. P. Chue Hong, D. S. Katz, M. Barker, A.-L. Lamprecht, C. Martinez, F. E. Psomopoulos, J. Harrow, L. J. Castro, M. Gruenpeter, P. A. Martinez, and T. Honeyman, FAIR Principles for Research Software (FAIR4RS Principles) (2021).

[37] A. Hjorth Larsen, J. Jørgen Mortensen, J. Blomqvist, I. E. Castelli, R. Christensen, M. Dulak, J. Friis, M. N. Groves, B. Hammer, C. Hargus, E. D. Hermes, P. C. Jennings, P. Bjerre Jensen, J. Kermode, J. R. Kitchin, E. Leonhard Kolsbjerg, J. Kubal, K. Kaasbjerg, S. Lysgaard, J. Bergmann Maronsson, T. Maxson, T. Olsen, L. Pastewka, A. Peterson, C. Rostgaard, J. Schiøtz, O. Schütt, M. Strange, K. S. Thyge

sen, T. Vegge, L. Vilhelmsen, M. Walter, Z. Zeng, and K. W. Jacobsen, The atomic simulation environment—a Python library for working with atoms, J. Phys. Condens. Matter 29, 273002 (2017).

[38] S. P. Ong, W. D. Richards, A. Jain, G. Hautier, M. Kocher, S. Cholia, D. Gunter, V. L. Chevrier, K. A. Persson, and G. Ceder, Python materials genomics (pymatgen): A robust, open-source python library for materials analysis, Comput. Mater. Sci 68, 314 (2013).

[39] S. Fredericks, K. Parrish, D. Sayre, and Q. Zhu, PyXtal: A Python library for crystal structure generation and symmetry analysis, Computer Physics Communications 261, 107810 (2021).

[40] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47, 558 (1993).

[41] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6, 15 (1996).

[42] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).

[43] S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J. Comput. Phys. 117, 1 (1995).

[44] A. Bochkarev, Y. Lysogorskiy, S. Menon, M. Qamar, M. Mrovec, and R. Drautz, Efficient parametrization of the atomic cluster expansion, Phys. Rev. Mater. 6, 013804 (2022).

[45] J. Behler, Constructing high-dimensional neural network potentials: A tutorial review, Int. J. Quantum Chem. 115, 1032 (2015).

[46] J. Behler, First principles neural network potentials for reactive simulations of large molecular and condensed systems, Angew. Chem. Int. Ed. 56, 12828 (2017).

[47] A. Knoll and J. Behler, runerase: An interface between the runner neural network energy representation (runner) and the atomic simulation environment (ase), https://runner-suite.gitlab.io/runnerase/1.0.2 (2021).

[48] A. Stukowski, E. Fransson, M. Mock, and P. Erhart, Atomicrex—a general purpose tool for the construction of atomic interaction models, Model. Simul. Mat. Sci. Eng. 25, 055003 (2017).

[49] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Implementation strategies in phonopy and phono3py, J. Phys. Condens. Matter 35, 353001 (2023).

[50] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59, 1758 (1999).

[51] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[52] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. a. Persson, The Materials Project: A materials genome approach to accelerating materials innovation, APL Mater. 1, 011002 (2013).

[53] M. Poul, L. Huber, E. Bitzek, and J. Neugebauer, Systematic atomic structure datasets for machine learning potentials: Application to defects in magnesium, Phys. Rev. B 107, 104103 (2023).

[54] Y. Lysogorskiy, A. Bochkarev, M. Mrovec, and R. Drautz, Active learning strategies for atomic cluster expansion models, Phys. Rev. Lett. 7, 043801 (2023).

[55] S. Fredericks, K. Parrish, D. Sayre, and Q. Zhu, Pyx-tal: A python library for crystal structure generation
 

and symmetry analysis, Comput. Phys. Commun. 261, 107810 (2021).

[56] C. J. Pickard and R. Needs, Ab initio random structure searching, J. Phys.: Condens. Matter 23, 053201 (2011).

[57] H. Yanxon, D. Zagaceta, B. C. Wood, and Q. Zhu, Neural network potential from bispectrum components: A case study on crystalline silicon, J. Chem. Phys. 153, 10.1063/5.0014677 (2020).

[58] Y. Mishin, M. J. Mehl, D. A. Papaconstantopoulos, A. F. Voter, and J. D. Kress, Structural stability and lattice defects in copper: Ab initio, tight-binding, and embedded-atom calculations, Phys. Rev. B 63, 224106 (2001).

[59] J. Behler, Atom-centered symmetry functions for constructing high-dimensional neural network potentials, J. Chem. Phys. 134, 074106 (2011).

[60] R. E. Kalman, A New Approach to Linear Filtering and Prediction Problems, J. Basic Eng. 82, 35 (1960).

[61] L. Kaufman and M. Cohen, The Martensitic Transformation in the Iron-Nickel System, JOM 8, 1393 (1956).

[62] C. Vega, E. Sanz, J. L. F. Abascal, and E. G. Noya, Determination of phase diagrams via computer simulation: methodology and applications to water, electrolytes and proteins, J. Phys.: Condens. Matter 20, 153101 (2008).

[63] P. Y. Chew and A. Reinhardt, Phase diagrams—Why they matter and how to predict them, J. Chem. Phys. 158, 030902 (2023).

[64] A. Opitz, Molecular dynamics investigation of a free surface of liquid argon, Phys. Lett., A 47, 439 (1974).

[65] A. Ladd and L. Woodcock, Triple-point coexistence properties of the Lennard-Jones system, Chem. Phys. Lett. 51, 155 (1977).

[66] W. Kranendonk and D. Frenkel, Computer simulation of solid-liquid coexistence in binary hard sphere mixtures, Mol. Phys. 72, 679 (1991).

[67] D. Frenkel and B. Smit, Chapter 7 - free energy calculations, in Understanding Molecular Simulation (Second Edition), edited by D. Frenkel and B. Smit (Academic Press, San Diego, 2002) second edition ed., pp. 167–200.

[68] J. G. Kirkwood, Statistical Mechanics of Fluid Mixtures, J. Chem. Phys. 3, 300 (1935).

[69] D. Frenkel and B. Smit, Understanding Molecular Simulation, 2nd ed. (Academic Press, Inc., USA, 2001).

[70] F. W. Gayle, J. B. Vander Sande, and A. J. McAlister, The Al-Li (Aluminum-Lithium) system, Bull. alloy phase diagr. 5, 19 (1984).

[71] D. R. Lide, CRC handbook of chemistry and physics, Vol. 85 (CRC press, 2004).

[72] L. Vočadlo and D. Alfe, Ab initio melting curve of the fcc phase of aluminum, Phys. Rev. B 65, 214105 (2002).

[73] A. Hänström and P. Lazor, High pressure melting and equation of state of aluminium, J. Alloys Compd. 305, 209 (2000).

[74] R. Otis and Z.-K. Liu, pycalphad: CALPHAD-based Computational Thermodynamics in Python, J. Open Res. Softw. 5, 1 (2017).

[75] P. Wang, Y. Du, and S. Liu, Thermodynamic optimization of the Li–Mg and Al–Li–Mg systems, Calphad 35, 523 (2011).

[76] L.-F. Zhu, B. Grabowski, and J. Neugebauer, Efficient approach to compute melting properties fully from ab initio with application to Cu, Phys. Rev. B 96, 224202 (2017).

[77] L.-F. Zhu, F. Körmann, A. V. Ruban, J. Neugebauer, and B. Grabowski, Performance of the standard exchange-correlation functionals in predicting melting properties fully from first principles: Application to al and magnetic ni, Phys. Rev. B 101, 144108 (2020).

[78] F. Dorner, Z. Sukurma, C. Dellago, and G. Kresse, Melting si: Beyond density functional theory, Phys. Rev. Lett. 121, 195701 (2018).

[79] K. Kishio and J. Brittain, Defect structure of  \( \beta \) -LiAl, J. Phys. Chem. Solids 40, 933 (1979).

[80] K. W. Jacobsen, J. K. Norskov, and M. J. Puska, Interatomic interactions in the effective-medium theory, Phys. Rev. B 35, 7423 (1987).

[81] M. W. Finnis and J. E. Sinclair, A simple empirical N-body potential for transition metals, Phil. Mag. A 50, 45 (1984).

[82] D. Frenkel and A. J. C. Ladd, New Monte Carlo method to compute the free energy of arbitrary solids. Application to the fcc and hcp phases of hard spheres, J. Chem. Phys. 81, 3188 (1984).

[83] R. Paula Leite, R. Freitas, R. Azevedo, and M. de Koning, The Uhlenbeck-Ford model: Exact virial coefficients and application as a reference system in fluid-phase free-energy calculations, J. Chem. Phys. 145, 194101 (2016).

[84] M. Watanabe and W. Reinhardt, Direct dynamical calculation of entropy and free energy by adiabatic switching, Phys. Rev. Lett. 65, 3301 (1990).

[85] M. de Koning, A. Antonelli, and S. Yip, Optimized Free-Energy Evaluation Using a Single Reversible-Scaling Simulation, Phys. Rev. Lett. 83, 3973 (1999).

[86] Y. Mishin, M. J. Mehl, and D. A. Papaconstantopoulos, Phase stability in the Fe–Ni system: Investigation by first-principles calculations and atomistic simulations, Acta Mater. 53, 4029 (2005).

[87] D. W. Brenner, Empirical potential for hydrocarbons for use in simulating the chemical vapor deposition of diamond films, Phys. Rev. B 42, 9458 (1990).

[88] J. Tersoff, Empirical interatomic potential for silicon with improved elastic properties, Phys. Rev. B 38, 9902 (1988).

[89] S. G. Johnson, The NLopt nonlinear-optimization package, https://github.com/stevengj/nlopt (2007).

[90] A. Singraber, J. Behler, and C. Dellago, Library-Based LAMMPS Implementation of High-Dimensional Neural Network Potentials, J. Chem. Theory and Comput. 15, 1827 (2019).

[91] Repository for workflows, https://github.com/pyiron/potential_publication.

[92] S. Menon, From electrons to thermodynamic phase diagrams with interatomic potentials: pyiron-based automated workflows for materials science applications (2023).

[93] From electrons to phase diagrams (2022), https://potentials.rub.de/2022/index.php.
 

# Supplemental material for ‘From electrons to phase diagrams with classical and machine learning potentials: automated workflows for materials science with pyiron’

Sarath Menon  \( \textcircled{0} \) , \( ^{1,*} \)  Yury Lysogorskiy, \( ^{2} \)  Alexander L. M. Knoll, \( ^{3,4} \)  Niklas Leimeroth

 \( ^{0} \) , \( ^{5} \)  Marvin Poul  \( ^{0} \)  \( ^{1} \)  Minaam Qamar  \( ^{0} \)  \( ^{2} \)  Jan Janssen  \( ^{0} \)  \( ^{1} \)  Matous Mrovec  \( ^{0} \)  \( ^{2} \)  Jochen

Rohrer  \( ^{0} \) , \( ^{5} \)  Karsten Albe  \( ^{0} \) , \( ^{5} \)  Jörg Behler  \( ^{0} \) , \( ^{3,4} \)  Ralf Drautz  \( ^{0} \) , \( ^{2} \)  and Jörg Neugebauer  \( ^{0} \) , \( ^{1} \) 

 \( ^{1} \)  Max-Planck-Institut für Eisenforschung GmbH, 40237 Düsseldorf, Germany

 \( ^{2} \) ICAMS, Ruhr-Universität Bochum, 44801 Bochum, Germany

 \( ^{3} \) Lehrstuhl für Theoretische Chemie II, Ruhr-Universität Bochum, 44780 Bochum, Germany

 \( ^{4} \) Research Center Chemical Sciences and Sustainability,

Research Alliance Ruhr, 44780 Bochum, Germany

 \( ^{5} \)  Technische Universität Darmstadt, Fachbereich Material und Geowissenschaften,

Fachgebiet Materialmodellierung, 64287 Darmstadt, Germany

(Dated: March 12, 2024)

## I. DATA SET GENERATION

## A. Domain-driven data set generation

First generation of training dataset contained following structures:

1. Perfect unary crystals (fcc/bcc/hcp) of Al and Li. For each structure, the following properties were computed: an energy-nearest neighbor distance curve (from 2 to 6.5 Å with a 0.5 Å step), full structural relaxation, an energy-volume curve around equilibrium volume ( \( \pm10\% \)  with a 2% step), elastic matrix calculations (with 5 points along each deformation mode in a  \( \pm0.5\% \)  strain range), phonons (as determined by Phonopy [1, 2]), and a supercell with a single vacancy.

2. Binary prototypes from the Materials Project, that contains Al and Li: Li2Al mp-1210753, LiAl mp-1067, LiAl3 mp-10890, Li9Al4 mp-568404, LiAl mp-1079240, LiAl mp-1191737, Li3Al2 mp-16506. For each structure, the same steps as in p.1 were performed.

3. Randomly deformed supercells. For each of the optimized structures from pp. 1 and 2, a new supercell was constructed in such a way that its minimal length of the cell vector was more than  \( 7\AA \) . For each supercell, five random deformations were generated. Each deformation consists of random normal atom displacements with  \( \sigma = 0.05\AA \)  and a random normal cell deformation with  \( \sigma = 0.05 \) . For each of the five random deformations, 11 uniformly isotropic deformations from -10% to +10% with a 2% step were generated.

This dataset was utilized to train the zeroth generation of the ACE potential. An active learning procedure was employed with this potential to sample more configurations. New configurations were generated through MD simulations in the NPT ensemble with zero pressure and increasing temperatures from 1 to 1500 K over 15,000 steps of supercells from p.3. Only structures with a maximum per-atom extrapolation grade exceeding 5 were selected. If the extrapolation grade exceeded 20, simulations were halted. Extrapolation grades were computed every 5th MD step. The number of captured configurations for different crystal structure types ranged from 6 to 261. In total, 491 structures were collected during the first round of active learning. These structures were computed with DFT, added to the training set, and the ACE potential was retrained. In the second round of active learning, the same procedure as before was applied, but MD ran for 50,000 steps with a steady temperature increase from 1 to 1500 K, followed by an additional 50,000 steps at T=1500 K. A total of 225 configurations were collected, ranging from 4 to 146 configurations per crystal structure.

## B. Random Crystal Structures

Table I show the parameters used to generate the training data. During all steps of this procedure we remove structures that have atomic distances below  \( 1.9\AA \)  to avoid overlapping PAW spheres, which would negatively impact the quality of the training data.

Figure 1 shows the distribution of Li concentration in the full training set, Fig. 2 the distribution of volume and Fig. 3 the convex hull.

## II. FUNCTIONS IN EAM POTENTIAL

The pair function V is defined as sum of 2 Morse functions  \( M(r, r_{0}, \alpha) = \exp(-2\alpha(r - r_{0})) - 2\exp(-\alpha(r - r_{0}) \) , additional short range repulsive terms  \( R(r_{s}, S) = S(r_{s} - r)^{4} \)  for  \( r < r_{s} \)  else 0 and a cutoff function  \( \Psi(x) = \)
 

TABLE I: Hyperparameters for systematic training set generation. Within each step of the random perturbations all listed modifications are applied together. The number of samples per structures refers to the number of displaced, strained or sheared structures per structure obtained from PyXtal after minimization.

<table><tr><td>Step</td><td>parameter</td><td>value</td></tr><tr><td rowspan="3">PyXtal</td><td>#Atoms, unary</td><td>total  \( \leq \)  10</td></tr><tr><td>#Atoms, binary</td><td>1,2,3,4,6 total  \( \leq \)  8</td></tr><tr><td>#Samples</td><td>3346</td></tr><tr><td rowspan="4">Vibrational</td><td>displacements</td><td>gaussian  \( \sigma \)  = 0.2  \( \AA \)</td></tr><tr><td>strain</td><td>uniform 0.05</td></tr><tr><td>shear</td><td>uniform 0</td></tr><tr><td>#Samples</td><td>4 per structure</td></tr><tr><td rowspan="3">Elastic, Tri-axial</td><td>train</td><td>uniform 0.05</td></tr><tr><td>shear</td><td>uniform 0</td></tr><tr><td>#Samples</td><td>4 per structure</td></tr><tr><td rowspan="3">Elastic, Shear</td><td>strain</td><td>uniform 0.05</td></tr><tr><td>shear</td><td>uniform 0</td></tr><tr><td>#Samples</td><td>4 per structure</td></tr></table>

![](./images/976997418136502272_23.jpg)

FIG. 1: Histogram of Li concentration in the training set. y-axis gives the number of structures on a log scale.

 \[ \begin{aligned}x^{4}/(1+x^{4})for x\geq0else0:\\V(r)=\left[E^{(1)}M(r,r_{0}^{(1)},\alpha^{(1)})+E^{(2)}M(r,r_{0}^{(2)},\alpha^{(2)})\right]\\\Psi\left(\frac{r-r_{c}}{h}\right)+\sum_{n=1}^{3}R(r,r_{n}^{(n)},S^{(n)}).\end{aligned} \quad (1) \] 

The electron density  \( \rho \)  is given by

 \[ \begin{align*}\rho(r)=\left[\alpha\exp(-\beta^{(1)}(r-r_{0}^{(3)})^{2})+\exp(-\beta^{(2)}(r-r_{0}^{(4)}))\right]\\\Psi\left(\frac{r-r_{c}}{h}\right),\end{align*} \quad (2) \] 

where  \( \alpha \)  is a prefactor used to normalize the total electron density on an atom in the equilibrium structure to 1 with  \( \overline{\rho} = \sum_{m} N_{m} \rho_{m} = 1 \) , where  \( N_{m} \)  is the number of atoms at distance  \( r_{m} \)  and  \( \rho_{m} \)  is  \( \rho(r_{m}) \) . The embedding term is defined separately for  \( \overline{\rho} < 1 \) 

 \[ F(\overline{\rho})=F^{(0)}+\frac{1}{2}F^{(2)}(\overline{\rho}-1)^{2}+\sum_{n=1}^{4}q^{(n)}(\overline{\rho}-1)^{n+2} \quad (3) \] 

TABLE II: ACE basis configurations: cutoff radius  \( (r_{c}) \) , type of radial basis functions,  \( \nu \) -order,  \( n_{max} \) ,  \( l_{max} \) , and the maximum number of functions per element (# func/elem) for each order  \( \nu \)  for this configuration.

<table><tr><td>rc</td><td>7  \( \textup{\AA} \)</td></tr><tr><td>Radial basis function</td><td>SBessel</td></tr><tr><td>\( \nu \) -order</td><td>1/2/3/4/5/6</td></tr><tr><td>\( n_{\text{max}} \)</td><td>15/6/4/3/2/2</td></tr><tr><td>\( l_{\text{max}} \)</td><td>0/3/3/2/2/1</td></tr><tr><td># func/elem</td><td>27/207/433/237/78/18</td></tr></table>

and  \( \overline{\rho} > 1 \) 

 \[ F(\overline{\rho})=\frac{F^{(0)}+\frac{F^{(2)}}{2}(\overline{\rho}-1)^{2}+q^{(1)}(\overline{\rho}-{1})^{3}+Q^{(1)}(\overline{p}-{1})^{4}}{1+Q^{(2)}(\overline{\rho}-{1})^{3}}. \quad (4) \] 

To satisfy an exact match of the lattice constant V was constrained by solving  \( \sum_{m} N_{m} R_{m} V_{m}^{\prime} = 0 \)  for  \( E^{(1)} \) . An exact match of the cohesive energy  \( E_{0} \)  is achieved by setting  \( F^{(0)} = E_{0} - 1/2 \sum_{m} N_{m} V_{m} \) . The expression for the bulk modulus B is obtained from

 \[ \frac{1}{2}\sum_{m}N_{m}V_{m}^{\prime\prime}R_{m}^{2}+F^{(2)}\left(\sum_{m}N_{m}\rho_{m}^{\prime}R_{m}\right)^{2}=9B\Omega_{0} \quad (5) \] 

with the equilibrium atomic volume  \( \Omega_{0} \) .

The mixed function  \( V_{AlLi} \)  was defined as a combination of a generalized Morse potential and the repulsive terms also applied for the pure elements

 \[ \begin{align*}V_{\mathrm{AlLi}}(r)=[\frac{D_{0}}{S-1}\exp\left(-\beta\sqrt{2S}(r-r_{0})\right)-\\ \frac{D_{0}S}{S-1}\exp\left(-\beta\sqrt{2/S}(r-r_{0})\right)+\delta]\Psi\left(\frac{r-r_{c}}{h}\right)\\ +\sum_{n=1}^{3}R(r,r_{s}^{(n)},S^{(n)}).\end{align*} \quad (6) \] 

In the case of  \( \rho_{AlLi} \)  and  \( \rho_{LiAl} \)  the same function as for the single elements was applied.

## III. SELECTION OF DATA

## IV. ACE POTENTIAL CONFIGURATION

ACE basis configuration is provided in Table II.

## V. SETTINGS OF THE RUNNER HDNPP FIT

All HDNNPs mentioned in this work were generated using RUNNER (version 1.3), compiled with IFORT (version 20230609) and linked against the MKL library (version 2023.2.0) as available through the INTEL ONEAPI. In addition to PYIRON, RUNNERASE (version 1.2.0) was
 
![](./images/976997418136502272_24.jpg)

![](./images/976997418136502272_25.jpg)

FIG. 2: Distribution of (per atom) volume and density in the training set.

![](./images/976997418136502272_26.jpg)

FIG. 3: Formation energies  \( (E_{\mathrm{f}}) \)  of atomic configurations included in the training dataset (only configurations with energies below 0.1 eV are shown for clarity).

used to facilitate calculation setup and evaluation. The hyperparameters and settings that were chosen for training the HDNNP are given in Supplementary Tab. III. The employed atom-centered symmetry functions (ACSFs) were generated automatically using RUNNERASE within a short-range cutoff radius of  \( R_{c} = 12.0 a_{0} \) . Nine radial ACSFs were generated for each of the four element combinations of the binary system with the hyperparameter  \( \eta = 0.9 a_{0}^{-2} \)  and  \( R_{s} \)  spaced equally between the minimum pairwise distance of the given element and the cutoff radius. Additionally, multiple groups of angular ACSFs were created, permuting  \( \lambda = [1.0, -1.0] \) ,  \( \zeta = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512] \)  and four  \( \eta \)  values per element triplet. In total, this yielded 258 ACSFs per element.

## VI. Al_{3}Li IN THE PHASE DIAGRAM

Although the  \( Al_{3}Li \)  appears on the DFT convex hull, it does not appear as a stable phase neither on the phase diagram [3], nor on the CALPHAD phase diagram. The ACE potential predicts a fcc  \( +Al_{3}Li \)  and  \( Al_{3}Li+AlLi \)  region which disappears at 580 K. For example, in the free energy curves at 500K, shown in Fig. 4, the ACE potential predicts a stable  \( Al_{3}Li \)  phase that appears in the phase diagram. The HDNNP potential does not predict a stable  \( Al_{3}Li \)  region in the investigated temperature range, although we note that this phase has been observed in a temperature range similar to ACE with an earlier HDNNP version exhibiting larger errors when employing different hyperparameters and data set filters. Overall, it should be stressed that the subtle energy differences resulting in the emergence of this phase are in the order of the convergence level of the DFT calculations and the accuracy of the employed exchange correlation functional.

## VII. SOFTWARE AVAILABILITY

The various software used in this work, along with their repository and documentation in shown in Table IV.
 
![](./images/976997418136502272_27.jpg)

![](./images/976997418136502272_28.jpg)

FIG. 4: Free energy curves as a function of composition at 500 K for the (a) HDNNP and (b) ACE potential.  \( Al_{3}Li \)  phase is above the common tangent that connects FCC Al and AlLi for the HDNNP potential, while it appears on the phase diagram for the ACE potential.

[2] A. Togo, First-principles phonon calculations with phonopy and phono3py, J. Phys. Soc. Jpn. 92, 012001 (2023).
[3] B. Hallstedt and O. Kim, Thermodynamic assessment of the Al–Li system, Int. J. Mater. Res. 98, 961 (2007).
 

TABLE III: Settings of the RuNNer HDNNP fit. Keywords and their values are listed as they are specified in the RuNNer input file format. ACSF settings are not included.

<table><tr><td>Keyword</td><td>Setting</td></tr><tr><td>bond_threshold</td><td>0.5</td></tr><tr><td>calculate_forces</td><td>true</td></tr><tr><td>center_symmetry_functions</td><td>true</td></tr><td>cutoff_type</td><td>1</td><tr><td>elements</td><td>Li Al</td></tr><tr><td>epochs</td><td>100</td></tr><tr><td>force_update_scaling</td><td>1.0</td></tr><tr><td>global_activation_short</td><td>t t t l</td></tr><tr><td>global_hidden_layers_short</td><td>3</td></tr><tr><td>global_nodes_short</td><td>25 20 15</td></tr><tr><td>kalman_lambda_short</td><td>0.988</td></tr><tr><td>kalma_nue_short</td><td>0 9987</td></tr><tr><td>mix_all_points</td><td>true</td></tr><tr><td>nguyen_widrow_weights_short</td><td>true</td></tr><tr><td>nn_type_short</td><td>1</td></tr><tr><td>number_of_elements</td><td>2</td></tr><tr><td>optmode_short_energy</td><td>1</td></tr><tr><td>optmodeshort_force</td><td>1</td></tr><td>precondition_weights</td><td>true</td><tr><td>random_seed</td><td>90</td></tr><tr><td>repeated_energy_update</td><td>true</td></tr><tr><td>scale_symmetry_functions</td><td>true</td></tr><td>short_energy_error_threshold</td><td>0.1</td><tr><td>short_energy_fraction</td><td>1.0</td></tr><tr><td>short_force_error_threshold</td><td>1.0</td><tr><td>short_force_fraction</td><td>0.1</td></tr><tr><td>test_fraction</td><td>0 1</td></tr><tr><td>use_short_forces</td><td>true</td></tr><tr><td>use short nn</td><td>true</td></tr><td>write_weights_epoch</td><td>1</td></table>

TABLE IV: Repository and documentation of the various software tools employed in this work.

<table><tr><td>Software</td><td>Repository</td><td>Documentation</td></tr><tr><td>pyiron</td><td>https://github.com/pyiron/pyiron</td><td>https://pyiron.org/</td></tr><tr><td>pacemaker</td><td>https://github.com/ICAMS/python-ace</td><td>https://pacemaker.readthedocs.io/</td></tr><tr><td>RuNNer</td><td>https://gitlab.com/runner-suite/runnerase</td><td>https://runner-suite.gitlab.io/</td></tr><tr><td>atomicrex</td><td>https://gitlab.com/atomicrex/atomicrex</td><td>https:/atomicrex.org/</td></tr><tr><td>CALPHY</td><td>https://github.com/ICAMS/calphy</td><td>https://calphy.org/</td></tr><tr><td>LAMMPS</td><td>https://github.com/lammps/lammps</td><td>https://www.lammps.org/</td></tr><tr><td>pycalphad</td><td>https://github.com/pycalphad/pycalphad</td><td>https://pycalphad.org/</td></tr><tr><td>pyXtal</td><td>https://github.com/qzhu2017/PyXtal</td><td>https:/pyxtal.readthedocs.io/</td></tr></table>
 
