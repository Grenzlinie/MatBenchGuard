Accepted Manuscript

Mobility of hydrogen-helium clusters in tungsten studied by molecular dynamics

Petr Grigorev, Dmitry Terentyev, Giovanni Bonny, Evgeny E. Zhurkin, Guido van
Oost, Jean-Marie Noterdaeme

![](./images/814542439346864128_1.jpg)

| PII: | S0022-3115(16)30095-2 |
|-----|------------------------|
| DOI: | 10.1016/j.jnucmat.2016.03.022 |
| Reference: | NUMA 49639 |
| To appear in: | *Journal of Nuclear Materials* |

Received Date: 6 November 2015

Revised Date: 21 March 2016

Accepted Date: 23 March 2016

Please cite this article as: P. Grigorev, D. Terentyev, G. Bonny, E.E. Zhurkin, G. van Oost, J.-M.
Noterdaeme, Mobility of hydrogen-helium clusters in tungsten studied by molecular dynamics, *Journal of
Nuclear Materials* (2016), doi: 10.1016/j.jnucmat.2016.03.022.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to
our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and all
legal disclaimers that apply to the journal pertain.

# Mobility of hydrogen-helium clusters in tungsten studied by molecular dynamics

Petr Grigorev$^{a,b,c}$, Dmitry Terentyev$^{a}$, Giovanni Bonny$^{a}$, Evgeny E. Zhurkin$^{c}$, Guido Van Oost$^{b}$, Jean-Marie Noterdaeme$^{b,d}$

$^{a}$SCK•CEN, Nuclear Materials Science Institute, Boeretang 200, Mol, 2400, Belgium
$^{b}$Ghent University, Applied Physics EA17 FUSION-DC, St.Pietersnieuwstraat, 41 B4 B-9000, Gent, Belgium
$^{c}$Department of Experimental Nuclear Physics K-89, Institute of Physics, Nanotechnologies and Telecommunications, Peter the Great St.Petersburg Polytechnic University, St. Petersburg, Russia
$^{d}$Max-Planck-Institut für Plasmaphysik, Garching, Germany

## Abstract

Tungsten is a primary candidate material for plasma facing components in fusion reactors. Interaction of plasma components with the material is unavoidable and will lead to degradation of the performance and the lifetime of the in-vessel components. In order to gain better understanding the mechanisms driving the material degradation at atomic level, atomistic simulations are employed. In this work we study migration, stability and self-trapping properties of pure helium and mixed helium-hydrogen clusters in tungsten by means of molecular dynamics simulations. We test two versions of an embedded atom model interatomic potential by comparing it with *ab initio* data regarding the binding properties of He clusters. By analysing the trajectories of the clusters during molecular dynamics simulations at finite temperatures we obtain the diffusion parameters. The results show that the diffusivity of mixed clusters is significantly lower, than that of pure helium clusters. The latter suggest that the formation of mixed clusters during mixed hydrogen helium plasma exposure will affect the helium diffusivity in the material.

## 1. Introduction

Tungsten (W) is chosen as a divertor armor material for the International Thermonuclear Experimental Reactor (ITER) and is a candidate for the first wall material for DEMO reactor [1]. During the operation of a fusion reactor, the plasma facing material will be exposed to hydrogen (H) isotopes (deuterium and tritium) and helium (He) particle fluxes as well as high energy neutron irradiation. Thus, both H and He will be present in the material either coming directly from plasma or from the transmutation reactions induced by the neutrons. Understanding the effect of the presence of these elements on the modification of the material's properties and the

physical mechanisms guiding the undergoing processes is of great practical and theoretical interest.

Both experimental and modelling efforts were done to understand the interaction of H with W under ITER relevant exposure conditions [2-7]. It was demonstrated that exposure to H (deuterium) plasma in doses up to $\sim10^{26}$ D/m² leads to the formation of blisters on the surface of the material and accumulation of H (retention) accompanied by the bubble formation in the material's subsurface. Bubble formation occurred at a depth of several $\mu$m, which exceeds the implantation range by an order of magnitude (~ 10 nm). At the same time, experiments involving He implantation demonstrate the presence of He bubbles and ‘fuzz’ formation in a subsurface region at a length scale comparable to the implantation depth [8, 9]. Atomistic modelling [10-13] revealed a significant difference in the behaviour of H and He atoms in tungsten. The binding energy of two H atoms in tungsten is negative (~ -0.06 eV), meaning that H atoms do not cluster together in a W lattice unlike He atoms. This also means that accumulation of H in W will be governed by diffusion and trapping on lattice defects such as vacancies, dislocations and grain boundaries [14, 15]. In contrast, He atoms exhibit strong attraction (~1.0 eV) and do cluster together and can even push out a W atom from its equilibrium lattice site (to form self-interstitial) once the He cluster reaches a certain critical size. This mechanism is called self-trapping and it is believed to be responsible for the bubble and ‘fuzz’ formation under He implantation.

Ab initio studies of He-H interaction [16-18] showed that there is an attractive interaction between He clusters and H atoms suggesting synergetic effects under mixed He-H plasma implantation. Suppressing of blistering, confirmed by experimental studies [19, 20], is one of the effects seen under simultaneous H and He exposures. The suppression of blistering was attributed to a decrease of H permeability through the subsurface region due to He bubble formation. Another remarkable effect was a detection of nanometric He bubbles at a depth significantly larger than the He implantation range [20], not seen in pure He exposures. However, comprehensive physical mechanisms leading to these synergetic effects are so far not clear.

To contribute to the understanding of the He-H interaction in a W lattice, we perform atomistic simulations using molecular static (MS) and molecular dynamics (MD) computational techniques. In this work, we assess the interaction of He-H clusters of different sizes and chemical morphology. The obtained MS results are compared with available ab initio data to validate and substantiate the application of central-force interatomic potentials for the studied

problem. By means of MD simulations, we study the diffusion and thermal stability of mixed He-H clusters to gain an understanding of the mechanisms causing the above mentioned synergetic effects under mixed He-H implantation conditions.

## 2. Computational details.

In this work, we used the interatomic potential for the W-H-He system created in the framework of the Embedded Atom Model (EAM) and published in [21]. There are two versions referred to as "EAM1" and "EAM2" in [21]. Both potentials are based on the interatomic potential for bcc W named "EAM2" from work [22]. The choice of the base W potential was made on the basis of benchmark calculations involving 19 up to date available EAM potentials for W [23]. In the derivation of the EAM1 version, an emphasis was put on a quantitative reproduction of *ab initio* data for the binding between H-H, He-He and H-He pairs [21]. The off-center position of a H atom in a vacancy as predicted by DFT [24] was not considered, and therefore both H and He are described by pair potentials only. For the EAM2 potential, the focus was made on the stabilizing H in an off-center position in the vacancy and therefore an embedding function was added for the H-H and H-W interaction terms. Both types of the potentials predict the tetrahedral position for H and He atoms as the most favorable in bulk W.

MS and MD calculations were performed using the LAMMPS simulation package [25], where the above-mentioned interatomic potentials were implemented. Simulations were performed in bcc W. All MD simulations were performed using a classical MD algorithm in the NVE ensemble, where the number of particles N, volume V and total energy E in the system are kept constant. Prior to the NVE run, each sample was thermalized and set to zero pressure using the Berendsen algorithm [26]. A simulation timestep of 0.1-1 fs was taken depending on the simulation temperature and the total simulation time varied from 5 ns for high temperature simulations up to 25 ns for low temperature simulations. MS calculations were performed using a conjugate gradient algorithm embedded in the LAMMPS package with a relative energy change tolerance between iterations of $10^{-10}$.

The size of the crystallite used in simulations was $10x10x10$ $a_0^3$ ($a_0$ is the lattice constant predicted by the potential: 3.14 Å) and it contained 2000 atoms before any point defect or cluster was introduced. Periodic boundary conditions were applied in all three directions.

The incremental binding energy of a H or He atom to a cluster is defined as the energy difference between the state where the H or He atom is far away from the cluster and the state where it is part of the cluster. As such, the binding energy between an atom A and a cluster B in W is calculated as,

$$E_{b}(A B)=E(A)+E(B)-E(A B)-E_{ref} \tag{1}$$

Here E(X) is the total energy of the box containing the defect X and $E_{ref}$ is the total energy of the box containing no defects (bcc W in our case). In this notation, a positive value of the binding energy corresponds to attraction between the defects. Prior to the static relaxation of the considered atomic configuration a short MD run at 300 K for 1 ps was performed after which the system was quenched to 0 K. This procedure allows the possibility for the system to evolve out of local minima and arrange itself into most stable configuration.

In order to obtain the diffusion parameters of H and He clusters a number of MD simulations were performed at finite temperature, $T$, varied in the range of 200 – 1700 K. The main goal was to obtain the diffusion coefficient as a function of temperature, which allows one to extract the pre-exponential factor $D_0$ and activation energy $E_m$ using the Arrhenius type equation:

$$D=D_{0} \exp \left(-\frac{E_{m}}{k_{B} T}\right) \tag{2}$$

In each MD run that lasted over a timespan of $\tau$ (5 – 25 ns), the trajectory of the H atom was followed and visualized. Then, the mean square displacement $\overline{R^{2}}$ of the position of the H atom was calculated to obtain the diffusion coefficient using the well-known Einstein equation:

$$D_{n}(T)=\frac{\overline{R_{n}^{2}}}{2 n \tau}(T) \tag{3}$$

where $n$ is dimensionality of the motion (i.e., $n$=3 for three dimensional bulk diffusion) and $\tau$ is the simulation time.

To improve the accuracy of the diffusion coefficient estimation, we employed the so-called independent interval method (IIM) [27]. The idea of the method is to decompose the full time of the simulation ($\tau$) into a number of independent segments ($k$) with time length of $\tau/k$ and calculate the diffusion coefficient using equation (3) on each segment. After that, the mean value

of the diffusion coefficient is taken. This method also allows one to estimate the uncertainty of the calculation by calculating the standard deviation of the mean ($\sigma$) since the trajectory is divided into statistically independent intervals. Once the diffusion coefficient as a function of temperature is obtained, the Arrhenius equation (equation 2) is fitted to extract the activation energy and prefactor. Employing a weighted least squares method [28] for fitting and using $1/\sigma^{2}$ as the weights, the diffusion parameters together with corresponding errors were obtained.

In case of simulations with mixed H-He clusters, only the time and trajectories where the atoms were clustered together was taken into account. Some weakly bound clusters have limited stability at finite temperature and therefore they decay quickly and bind back. By applying a post-processing algorithm, we only consider a set of separate segments where the cluster was stable and moved as a whole object. If the number of such independent segments was higher than 10, we used an average value of the diffusion coefficient calculated over these segments. If the number of these segments was lower than 10, the IIM method was applied to the longest time segment. The average time length of the segments when the cluster remains stable, $\bar{t}$, allows one to calculate a decay frequency $\nu=\frac{1}{\bar{t}}$. Having a set of data for decay frequency as a function of temperature, an Arrhenius expression $\nu=\nu_{0} \exp \left(-\frac{E_{d}}{k_{B} T}\right)$ was fitted to this dataset to deduce the dissociation energy, $E_{d}$ and pre-exponential factor $\nu_{0}$. These values were compared with the predictions from static calculations as well as ab initio data.

## 3. Results and discussion

### 3.1 Molecular static calculations

As was said before, for our calculations we used both EAM1 and EAM2 potentials from [21]. In this work both versions of the potentials were tested to reproduce ab initio values of the interaction energy of H-He, He-He and H-H pairs, reported in [18]. It was demonstrated that both potentials give qualitative agreement with ab initio data and quantitative agreement is achieved by the EAM1 potential. In Fig. 1 we compare the results for incremental binding energy of a He atom to a cluster of He atoms in bulk tungsten, predicted by both versions of the potential and ab initio values from [11]. As was shown in [21], EAM1 gives better agreement for the He-He pair interaction and EAM2 underestimates the corresponding binding energy. However, as can be

seen from Fig. 1, EAM1 shows a rapid increase of the binding energy with increasing of the cluster size, which is not in agreement with the trend coming from ab initio data. At the same time EAM2 gives reasonable agreement regarding for the binding energy function. Since in this work we study the mobility of mixed He-H clusters, the adequate reproduction of the binding energy function is important to correctly describe the thermal stability of the clusters during MD simulations.

![](./images/814542439346864128_2.jpg)

Figure 1. Comparison of the predictions of the incremental binding energy for He clusters obtained with the EAM1 and EAM2 interatomic potentials and ab initio method in [11].

An important process that affects the diffusivity of He clusters is the so called self-trapping mechanism. After a cluster of He atoms of a certain size is created, it becomes energetically more favorable to create a Frenkel pair in order to release the stress created by the interstitial He atoms. After the Frenkel pair is created, He atoms occupy the vacancy and become immobile. Thus it is important to test the ability of the potentials to reproduce this mechanism for reliable simulations of H-He clusters mobility. MS calculations were used to assess the energy balance of a system containing a He cluster in an ideal W matrix and a system where the same He cluster is placed in a vacancy close to a W self-interstitial atom (SIA). The same energy balance calculations were also performed by ab initio techniques in [12]. The results from this work are compared with our MS calculations in Fig. 2. It can be seen that both versions of the potential are in good agreement with the ab initio values. Regarding the threshold size of the He cluster at which the formation of a Frenkel pair becomes more favorable the potentials predict a value for

$N_{He}$ between 5 and 6 atoms. Despite the significant difference in description of binding of He clusters in bulk tungsten (see Fig. 1), both versions of the potentials give very similar values for the formation energy of Frenkel pairs. This observation is explained by the fact that the bias of EAM1 for the binding of He atoms in bulk is similar to its bias for He atoms in a vacancy. Since there is no difference between both EAM potentials with respect to the He self-trapping mechanism; but the EAM2 potential describes the energetics of He clusters in the bulk W better, we chose the EAM2 potential for the finite temperature simulations.

![](./images/814542439346864128_3.jpg)

Figure 2. Comparison of the predictions of the Frenkel pair formation energies in presence of He clusters obtained by EAM1 and EAM2 and ab initio method in [12]

As we study the mobility of He-H clusters, it is important to first assess the binding energy of He and H atoms in these clusters by MS calculations. In Fig. 3, the results for the incremental binding energy of a H atom to He-H clusters are presented. It is important to note that the He binding energy is higher than that for a H atom because of the strong He-He bonding (1.03 eV), while the He-H bond strength is only 0.2 eV. Thus, the stability of the mixed He-H clusters will be determined by the binding energy of a H atom as it has the lowest binding energy. It can be seen from Fig. 3 that there is a rapid decrease of the binding energy as the number of H atoms in the cluster increases. Starting from three H atoms in the cluster, the binding energy becomes negligible, indicating that the cluster becomes unstable. This result is in agreement with ab initio data from [17] where low stability of clusters containing more than three H atoms was demonstrated. The most stable atomic configurations for the considered clusters are shown in Fig. 4.

![](./images/814542439346864128_4.jpg)

Figure 3. Incremental binding energy of a H atom to He-H clusters as predicted by the EAM2 potential.

These static calculations defined the configurations that should be studied by MD simulations. The energy needed for He-induced Frenkel pair formation becomes quite low (~2 eV) if the cluster contains four He atoms. Adding the fifth He atom results in the spontaneous generation of a Frenkel pair. This means that the punching of a tungsten self-interstitial is also possible for He-H clusters containing four He atoms at sufficiently high temperature, as was actually demonstrated in [12]. Thus, we decided to study only clusters containing at most four He atoms to avoid the transformation caused by self-interstitial punching. Fig. 3 shows that starting from three H atoms in the cluster, the latter becomes unstable, meaning it will decay during MD runs at finite temperatures. Thus for further MD studies, the pure and mixed clusters containing from one to four He atoms and up to two H atoms were considered.

![](./images/814542439346864128_5.jpg)

Figure 4. The atomic configurations of mixed He-H clusters corresponding to binding energy values reported in fig 3. The visualization is done using OVITO tool [29].

In this work we did not directly test other types of the available interatomic potentials for W-He-H system regarding He cluster formation energy, He assisted Frenkel pair formation and H and He mobility. However in [21] a Bond Order Potential (BOP) from [30] was benchmarked and validated by comparison with *ab initio* data. The results of that comparison allow us to estimate the relevance of the potential for our study. Both types of the potential (BOP and EAM) predict the tetrahedral position as the most favourable for both H and He together with correct ordering of interstitial formation energies, although EAM potentials show the best quantitative agreement with *ab initio*. Both types of the potentials demonstrate good agreement in terms of H-H, H-He and He-He pair interaction. With respect to the binding energy of a H-vacancy or He-vacancy pair, EAM potentials reproduce the *ab initio* values, while BOP underestimates and overestimates the binding for H and He, respectively. BOP predicted binding energy of H atoms to vacancy-H-He clusters is overestimated by about a factor two, but for He, on the other hand, the values lay within the *ab initio* range. These discrepancies would affect the energetics of the

He-H clustering behavior together with He assisted Frenkel pair, as treated by the BOP potential. The migration energy for H interstitial is well reproduced by all potentials, The migration energy for He interstitial is well reproduced by EAM potentials, but underestimated by BOP by a factor three. Thus, we believe that qualitatively simulations using BOP potential would results similar picture regarding the mobility of He-H clusters. However, numerical discrepancies between BOP and *ab initio* data in He migration energy and H binding energy to vacancy-H-He clusters together with He assisted Frenkel pair formation energy would lead to essential quantitative differences in the results and EAM2 potential remains our choice for dynamic calculations.

### 3.2 Molecular dynamic simulations

A set of MD simulations was performed to obtain information on the diffusivity and thermal stability (i.e. lifetime) of the He-H clusters. As was described in Section 2, the Arrhenius expression was used to fit the set of diffusion coefficients and decay frequencies obtained at different temperatures from the MD simulations. In Fig. 5, the decay frequency together with Arrhenius fits for the He-H clusters is presented. The slope of the plot corresponds to the dissociation energy $E_{diss}$. The error bars correspond to 1.96 times the standard error around the average, which corresponds to the 95% confidence interval of the mean value. Following the standard assumption, the dissociation energy $E_{diss}$ is a sum of binding energy and migration barrier ($E_{diss}=E_b+E_m$). The average discrepancy between the values of the dissociation energy $E_{diss}$ obtained by fitting the MD data and the results of the static calculations for binding energies $E_b$ (see Fig. 3) is 0.21 ±0.03 eV. This is in excellent agreement with the H migration barrier (0.21 eV) in bulk W both predicted by the potential and obtained with *ab initio* calculations (0.2 eV) [18].

![](./images/814542439346864128_6.jpg)

Figure 5 Arrhenius plot of the decay frequency of He-H clusters with 1 to 4 He atoms in the cluster obtained from MD simulations. The error bars represent 95 % confidence interval around the mean..

As was said before, for obtaining diffusion parameters of He and He-H clusters we used independent interval method. However, another way to obtain diffusivity from particle trajectory is to calculate the slope of the mean square displacement (MSD) as a function of time. In IIM method the MSD dependence on time is not calculated directly, thus we can validate the results of the method by comparison with the theoretical dependence $MSD =6*t*D$. This comparison is made for He2-H1 and He3 clusters on the Fig. 6. (a) and (b) respectfully. It can be seen from the figure that MSD data lies in the area defined by the values of diffusivity the uncertainties obtained by IIM method, which confirms the validity of the method. The similar comparison was made for other clusters showing the same result.

![](./images/814542439346864128_7.jpg)

Figure 6 Mean square displacement as a function of time for 2He-1H (a) and 3He (b) clusters. The dashed lines represent diffusivities obtained with IIM method; the colored areas represent the error for diffusivity as 95 % confidence interval.

In Fig.7, the diffusion parameters for He-H clusters (a) and He clusters (b) are shown.

From Fig. 7(a) it follows that the slope of the fits for the clusters with 1 and 2 H atoms is almost the same, while the prefactor, $D_0$, decreases for the larger cluster. This means that the migration energy is the same for these clusters, but the effective attempt frequency is different. The latter indicates a difference in vibrational entropy between the two clusters. Fig 7(b) demonstrates that the migration energy of a He cluster increases with its size.

It is important to note that for the $He_4$ cluster an event of self-trapping was detected during the MD run at 1700 K, which is in agreement with the MS predictions as well as with the MD results from [12].

![](./images/814542439346864128_8.jpg)

Figure 7. Arrhenius plot of the diffusion coefficients for He clusters containing 1 to 4 He atoms obtained from MD simulations. The error bars represent 95 % confidence interval of the mean..

The diffusion and lifetime parameters were obtained by fitting Arrhenius equation to the data. Having the uncertainty of the data available from IIM method, we can estimate the validity of the Arrhenius equation for the data. To do this one can use so called reduced Chi squared test, where the following value needs to be calculated: $$\tilde{\chi}^{2}=\frac{1}{\mathrm{~d}} \sum_{1}^{\mathrm{N}}\left(\frac{\mathrm{y}_{\mathrm{i}}-\mathrm{f}\left(\mathrm{x}_{\mathrm{i}}\right)}{\sigma_{\mathrm{i}}}\right)^{2}$$ [31], where N is number of data points, $y_{i}$ and $x_{i}$ is the data set, $\sigma_{i}$ - uncertainty of $y_{i}, f(x)$ is the expected function, in our case it is Arrhenius equation, d - is a number of degrees of freedom of the data distribution. In our case $\mathrm{d}=\mathrm{N}-\mathrm{c}$, where $\mathrm{N}$ is number of data points and $c$ - number of constrains. In our study $c$ equals 2 since we define 2 parameters for Arrhenius equation from the data. Values of $\tilde{\chi}^{2}$ close to 1, or lower indicate high validity of expected function for the data [31]. Using 95 % confidence interval for the uncertainty estimation of the data we calculated reduced Chi squared for diffusion and lifetime data. Obtained values are reported in table 1. As can be seen from the table, most of the values are significantly lower or very close to 1, which confirms the validity of Arrhenius equation for the data.

The migration energy of different He-H clusters as well as of pure He clusters obtained by applying the above described techniques are summarized in Fig. 8. It can be seen that indeed the migration energy of He clusters increases with the size of the cluster (black curve). If H atoms are added to a He cluster, the migration energy increases almost by a factor of two and gets close to the value of the migration energy of a single H atom, denoted by the green area in the graph. The increase of the migration energy of the mixed clusters compared to pure He clusters is consistent

with the fact that it is defined by the slowest constituent of the cluster, which is H atom. Hence, the formation of mixed clusters will have a strong impact on the diffusivity of pure He clusters, which migrate extremely fast in a H-free tungsten lattice. On the other hand, pure He and mixed He-H clusters would act as trapping sites for freely migrating H atoms, which do not feature self-clustering in bulk W. The obtained values for the migration barriers and dissolution energies are summarized in table 1.

![](./images/814542439346864128_9.jpg)

Figure 7. Migration energies for He-H clusters extracted from MD simulations. The error bars represent the 95 % confidence interval.

<table>
  <thead>
    <tr>
      <th>Cluster type</th>
      <th>Migration barrier (eV)</th>
      <th>$\tilde{\chi}^2$ for diffusion data</th>
      <th>Dissolution energy (eV)</th>
      <th>$\tilde{\chi}^2$ for lifetime data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1He</td>
      <td>0.071 $\pm$ 0.007</td>
      <td>0.61</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>2He</td>
      <td>0.09 $\pm$ 0.01</td>
      <td>1.23</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3He</td>
      <td>0.17 $\pm$ 0.01</td>
      <td>0.42</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>4He</td>
      <td>0.28 $\pm$ 0.02</td>
      <td>1.24</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>1He-1H</td>
      <td>0.21 $\pm$ 0.03</td>
      <td>0.08</td>
      <td>0.52 $\pm$ 0.02</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>1He-2H</td>
      <td>0.25 $\pm$ 0.03</td>
      <td>0.02</td>
      <td>0.51 $\pm$ 0.04</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>2He-1H</td>
      <td>0.23 $\pm$ 0.02</td>
      <td>0.12</td>
      <td>0.79 $\pm$ 0.01</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>2He-2H</td>
      <td>0.25 $\pm$ 0.04</td>
      <td>0.07</td>
      <td>0.77 $\pm$ 0.08</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>3He-1H</td>
      <td>0.40 $\pm$ 0.03</td>
      <td>0.67</td>
      <td>0.98 $\pm$ 0.09</td>
      <td>1.17</td>
    </tr>
  </tbody>
</table>

Table 1. Migration barriers and dissolution energies together with $\tilde{\chi}^2$ values for He and mixed He-H clusters.

## 4. Conclusive remarks

A set of molecular dynamics calculations at finite temperature was performed and diffusion parameters for He-H clusters were obtained. Prior to performing the MD calculations, two versions of EAM potential from [21] were validated by comparison of the results of static calculations on He-He, He-H and H-H interaction with *ab initio* data from [11, 12]. The most adequate potential was selected and applied in MD simulations. On the basis of the benchmark MS calculations and results of finite temperature MD simulations, the following conclusions can be drawn:

- The static calculations revealed a significant difference in the binding energy of He in the He clusters as predicted by the EAM1 and EAM2 potentials. The pair interactions of He-He atoms is better reproduced by the EAM1 potential, while EAM2 underestimates the interaction, as compared to the *ab initio* results. However, the EAM1 potential overestimates the increase of the binding energy with cluster size. The EAM2 potential, on the other hand, shows better agreement.
- Comparison of the energy balance for He assisted Frenkel pair formation showed that both versions of the potential demonstrate acceptable agreement with *ab initio* prediction. The inaccuracy of the EAM1 potential with respect to the prediction of the He binding energy in the He clusters should be considered as an important drawback for the modeling of the diffusion process of the small mixed clusters. The EAM2 potential reproduces the binding energy of He in He clusters in close agreement with *ab initio* calculations.
- The binding of a H atom in He-H clusters becomes negligible if the mixed clusters contains three H atoms or more. Thus, stable mixed clusters contain no more than two H atoms.
- On the basis of the diffusion coefficients of pure He and mixed He-H clusters deduced from the MD simulations, we conclude that the migration energy of pure He clusters increases with increasing cluster size; and for the $\text{He}_3$ cluster it is two times higher than the migration energy of a He interstitial (0.07 eV).
- Mixing of H atom(s) with a He cluster leads to the increase of the migration barrier, so that the migration energy of the mixed clusters are comparable to the

migration energy of an interstitial H atom (0.2 eV). This implies that the formation of mixed clusters primary leads to the suppression of the He diffusivity.

The conclusions listed above were made based on the analysis of the results of MD simulations using 3D periodic conditions relevant from the bulk material. In order to properly study synergetic effects during mixed He-H implantation one has to perform a full scale simulation of mixed beam exposure conditions taking account surface effects. Unfortunately, experimentally-relevant timescales are not reachable by MD techniques and an upper scale model such as rate theory is needed. Our work provides diffusion and lifetime parameters together with self-trapping energetics for He-H clusters being the necessary input for such simulations.

### Acknowledgements:

This work was supported by the European Commission and carried out within the framework of the Erasmus Mundus International Doctoral College in Fusion Science and Engineering (FUSION-DC).

This work has been carried out within the framework of the EUROfusion Consortium and has received funding from the Euratom research and training programme 2014-2018 under grant agreement No 633053. The views and opinions expressed herein do not necessarily reflect those of the European Commission.

### References:

[1] R.E. Clark and D. Reiter 2005 *Nuclear fusion research: understanding plasma-surface interactions* Springer)

[2] Y. Zayachuk, M.H.J.t. Hoen, P.A.Z.v. Emmichoven, I. Uytdenhouwen and G.v. Oost, Nucl. Fusion 52 (2012) 103021.

[3] O.V. Ogorodnikova, J. Roth and M. Mayer, J. Nucl. Mater. 313–316 (2003) 469-477.

[4] V.K. Alimov, B. Tyburska-Püschel, S. Lindig, Y. Hatano, M. Balden, J. Roth, K. Isobe, M. Matsuyama and T. Yamanishi, J. Nucl. Mater. 420 (2012) 519-524.

[5] T. Ahlgren, K. Heinola, K. Vörtler and J. Keinonen, J. Nucl. Mater. 427 (2012) 152-161.

[6] A.A. Haasz, J.W. Davis, M. Poon and R.G. Macaulay-Newcombe, J. Nucl. Mater. 258–263, Part 1 (1998) 889-895.

[7] L. Buzi, G.D. Temmerman, B. Unterberg, M. Reinhart, A. Litnovsky, V. Philipps, G.V. Oost and S. Möller, J. Nucl. Mater. 455 (2014) 316-319.

[8] M.J. Baldwin and R.P. Doerner, J. Nucl. Mater. 404 (2010) 165-173.

[9] M. Yamagiwa, S. Kajita, N. Ohno, M. Takagi, N. Yoshida, R. Yoshihara, W. Sakaguchi and H. Kurishita, J. Nucl. Mater. 417 (2011) 499-503.

[10] D.F. Johnson and E.A. Carter, J. Mater. Res. 25 (2010) 315-327.

[11] C.S. Becquart and C. Domain, Phys. Rev. Lett. 97 (2006) 196402.

[12] J. Boisse, C. Domain and C.S. Becquart, J. Nucl. Mater. 455 (2014) 10-15.

[13] K.O. Henriksson, K. Nordlund, A. Krasheninnikov and J. Keinonen, Appl. Phys. Lett. 87 (2005) 163113-163113-163113.

[14] V.I. Dubinko, P. Grigorev, A. Bakaev, D. Terentyev, G. Van Oost, F. Gao, D. Van Neck and E.E. Zhurkin, JOURNAL OF PHYSICS-CONDENSED MATTER 26 (2014)

[15] P. Grigorev, D. Terentyev, G. Bonny, E.E. Zhurkin, G. Van Oost and J.-M. Noterdaeme, J. Nucl. Mater. 465 (2015) 364-372.

[16] H.-B. Zhou, Y.-L. Liu, S. Jin, Y. Zhang, G.-N. Luo and G.-H. Lu, Nucl. Fusion 50 (2010) 115010.

[17] A. Takayama, A.M. Ito, Y. Oda and H. Nakamura, J. Nucl. Mater. 463 (2015) 355-358.

[18] C.S. Becquart and C. Domain, J. Nucl. Mater. 386-388 (2009) 109-111.

[19] Y. Ueda, M. Fukumoto, J. Yoshida, Y. Ohtsuka, R. Akiyoshi, H. Iwakiri and N. Yoshida, J. Nucl. Mater. 386-388 (2009) 725-728.

[20] M. Miyamoto, D. Nishijima, M.J. Baldwin, R.P. Doerner, Y. Ueda, K. Yasunaga, N. Yoshida and K. Ono, J. Nucl. Mater. 415 (2011) S657-S660.

[21] G. Bonny, P. Grigorev and D. Terentyev, J. Phys.: Condens. Matter. 26 (2014) 485001.

[22] M.-C. Marinica, L. Ventelon, M.R. Gilbert, L. Proville, S.L. Dudarev, J. Marian, G. Bencteux and F. Willaime, J. Phys.: Condens. Matter. 25 (2013) 395502.

[23] G. Bonny, D. Terentyev, A. Bakaev, P. Grigorev and D.V. Neck, Modelling and Simulation in Materials Science and Engineering 22 (2014) 053001.

[24] K. Heinola, T. Ahlgren, K. Nordlund and J. Keinonen, Phys. Rev. B 82 (2010) 094102.

[25] S. Plimpton, J. Comput. Phys. 117 (1995) 1-19.

[26] H.J.C. Berendsen, J.P.M. Postma, W.F. van Gunsteren, A. DiNola and J.R. Haak, The Journal of Chemical Physics 81 (1984) 3684-3690.

[27] M.W. Guinan, R.N. Stuart and R.J. Borg, Physical Review B 15 (1977) 699-710.

[28] J.R. Taylor and E. Cohen, Measurement Science and Technology 9 (1998) 1015.

[29] A. Stukowski, Modelling and Simulation in Materials Science and Engineering 18 (2010) 015012.

[30] X.-C. Li, X. Shu, Y.-N. Liu, Y. Yu, F. Gao and G.-H. Lu, J. Nucl. Mater. 426 (2012) 31-37.

[31] J.R. Taylor 1997 An Introduction to Error Analysis: The Study of Uncertainties in Physical Measurements University Science Books)