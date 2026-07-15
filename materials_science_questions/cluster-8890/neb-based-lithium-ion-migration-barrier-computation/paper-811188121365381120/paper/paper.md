# Trapping of $Li^{+}$ Ions by $[ThF_{n}]^{4-n}$ Clusters Leading to Oscillating Maxwell-Stefan Diffusivity in the Molten Salt LiF-ThF₄

Brahmananda Chakraborty, $^{*, \dagger}$ Sharif Kidwai, $^{\ddagger}$ and Lavanya M. Ramaniah $^{\dagger}$

$^{\dagger}$High Pressure and Synchrotron Radiation Physics Division, Bhabha Atomic Research Centre, Trombay, Mumbai 400085, India
$^{\ddagger}$Department of Electrical Engineering, Aligarh Muslim University, Aligarh 202002, India

Supporting Information

ABSTRACT: A molten salt mixture of lithium fluoride and thorium fluoride (LiF-ThF₄) serves as a fuel as well as a coolant in the most sophisticated molten salt reactor (MSR). Here, we report for the first time dynamic correlations, Onsager coefficients, Maxwell-Stefan (MS) diffusivities, and the concentration dependence of density and enthalpy of the molten salt mixture LiF-ThF₄ at 1200 K in the composition range of 2-45% ThF₄ and also at eutectic composition in the temperature range of 1123-1600 K using Green-Kubo formalism and equilibrium molecular dynamics simulations. We have observed an interesting oscillating pattern for the MS diffusivity for the cation-cation pair, in which $\mathcal{D}_{Li-Th}$ oscillates between positive and negative values with the amplitude of the oscillation reducing as the system becomes rich in ThF₄. Through the velocity autocorrelation function, vibrational density of states, radial distribution function analysis, and structural snapshots, we establish an interplay between the local structure and multicomponent dynamics and predict that formation of negatively charged $[ThF_{n}]^{4-n}$ clusters at a higher ThF₄ mole % makes positively charged $Li^{+}$ ions oscillate between different clusters, with their range of motion reducing as the number of $[ThF_{n}]^{4-n}$ clusters increases, and finally $Li^{+}$ ions almost get trapped at a higher ThF₄% when the electrostatic force on $Li^{+}$ exerted by various surrounding clusters gets balanced. Although reports on variations of density and enthalpy with temperature exist in the literature, for the first time we report variations of the density and enthalpy of LiF-ThF₄ with the concentration of ThF₄ (mole %) and fit them with the square root function of ThF₄ concentration, which will be very useful for experimentalists to obtain data over a range of concentrations from fitting the formula for design purposes. The formation of $[ThF_{n}]^{4-n}$ clusters and the reduction in the diffusivity of the ions at a higher ThF₄% may limit the percentage of ThF₄ that can be used in the MSR to optimize the neutron economy.

![](./images/811188121365381120_1.jpg)

## 1. INTRODUCTION

Molten salts¹ play an important role in nuclear technology and find multiple applications, for example, as a coolant for an advanced high-temperature reactor,²³ as nuclear fuel for advanced molten salt reactors (MSRs),⁴⁵ and as a solvent for the pyrometallurgical recycling process.⁶⁸ The structural arrangement and dynamics of the ions of the molten salt and the dissolved actinides have significant impact on the performance of the reactor and the efficiency of the recycling process. Among the alkali halides, molten fluoride salts are of particular importance in reactors because they are chemically stable and resistant to radiation and have low neutron capture cross sections, higher thermal conductivities, lower melting points, and higher boiling temperatures, as desired for reactor applications.⁹¹⁰ A molten salt mixture of lithium fluoride and thorium fluoride (LiF-ThF₄) serves as a fuel as well as a coolant in the MSR,⁴⁵ which is considered to be the most sophisticated fission reactor concept.

Theoretical data on the thermophysical properties¹¹ of the salt mixture for various compositions and temperatures, which control the performance of the coolant and fuel, is considered to be an essential input to the experimentalist as experimental investigations on varying compositions and temperatures are prohibitively time consuming and expensive. Molecular dynamics (MD)¹²¹³ is a powerful tool to provide structural and dynamic parameters for different compositions and temperatures using suitable interatomic potentials. Using MD simulations, Dewan et al.¹⁴ computed the density, self-diffusion coefficients, electrical conductivity, viscosity, and heat capacity for eutectic mixtures of LiF-ThF₄ (78 mol % LiF, 22 mol % ThF₄) over a wide range of temperatures. Although the computed data for eutectic mixtures matches reasonably well with the available experimental data, composition variation was not studied. Gheribi et al.,¹¹ using polarizable force fields, studied the composition and temperature variation of various thermophysical properties of LiF-ThF₄. They determined several figures of merit that are essential for designing MSRs by fitting the calculated data with analytic functions. Recently, Liu et al.,¹⁵ using MD simulations, investigated the local structure around $Th^{4+}$ in LiF-ThF₄ melts. They studied the character of Th-F bonding, coordination number, and transport properties for various temperatures and compositions. Although there

Received: May 23, 2016
Revised: July 22, 2016

exist a few studies on the structure, viscosity, and self-diffusion of ${\rm LiF-ThF_4}$ as mentioned above, there is no study on the multicomponent diffusion$^{16,17}$ of this important salt mixture. Multicomponent diffusion can provide insight into how the relative dynamics of various ions, leading to local arrangement and structure, controls the heat transfer and neutronics of the reactor. Multicomponent diffusion is difficult to study especially in an ionic system involving electric field as Fick's law can be misleading because it neglects the effect of electric fields. It was observed that sodium chloride diffuses against its gradient in a mixture of NaCl and HCl due to the electric field generated by ${\rm H^+}$ ions, whereas Fick's law$^{18}$ predicts the opposite. Another difficulty in Fick's approach is that for an $n$-component system there are $(n-1)^2$ Fick diffusion coefficients with non-symmetric matrix elements, which are difficult to manage. The Maxwell-Stefan (MS)$^{19,20}$ approach is more suitable for the multicomponent dynamics of the ionic system, as it accounts for the electric field, decouples the thermodynamic factor, and has diffusion coefficients that are symmetric with only $n(n - 1)/2$ MS diffusivities to deal with for an $n$-component system. In this approach, the driving force (which also includes the electrostatic force in an ionic system) of component $i$ is counterbalanced by the force arising due to friction between component $i$ and other components as expressed by$^{20}$

$$
-\frac{\nabla \mu_{i}}{R T}=\sum_{\substack{k=1 \\ k \neq i}}^{n} \frac{x_{k}}{\mathcal{D}_{i k}}\left(\hat{\mathbf{U}}_{i}-\hat{\mathbf{U}}_{k}\right)
\tag{1}
$$

where $\mathcal{D}_{ik}$ is the MS diffusivity between $i$ and $k$, which can be labeled as an inverse friction coefficient, and $\hat{\mathbf{U}}_{i}$ is the velocity of the $i$th species. For a mixture of an ionic system with a common anion, the MS diffusivity, $\mathcal{D}_{ij}$, for the cation-cation pair can also become negative. $^{21}$ In our earlier study with the ${\rm LiCl-KCl}$ mixture,$^{22}$ we have observed divergent and negative MS diffusivity, $\mathcal{D}_{KLi}$, for eutectic mixtures at a temperature of 1095 K and at a KCl mole fraction of 0.48 at 1043 K. The diverging MS diffusivity may put a constraint on the use of a eutectic ${\rm LiCl-KCl}$ mixture above 1095 K and for the composition beyond 0.48 mole fraction of KCl. Negative MS diffusivity, equivalent to negative friction coefficient, has also been reported experimentally with an atomic force microscope tip on a graphite surface,$^{23}$ where the friction decreases with increasing load. Recently, we have shown a sign crossover in all MS diffusivities in ${\rm LiF-BeF_2}^{24}$ due to the formation of a flouride polyanion network between Be and F ions, which establishes that even the MS diffusivity between a cation-anion pair may also become negative in certain compositions. The only constraint is that it should satisfy the non-negative entropy production constraint$^{21}$ necessitated by the second law of thermodynamics. So it is worthwhile to study the multi-component diffusion of the ${\rm LiF-ThF_4}$ mixture to get insight into the relative dynamics of the ions at different compositions and temperatures, resulting from various configurations, and to correlate the structure with the multicomponent dynamics to assess its impact on the performance of the fuel and coolant. This may also help the experimentalist to choose the composition that can optimize the neutron economy as well as transfer heat more effectively.

In this article, applying Green-Kubo$^{25}$ formalism and equilibrium MD simulations, we report for the first time MS diffusivities, dynamic correlations, and Onsager coefficients$^{26}$ for a molten salt mixture ${\rm LiF-ThF_4}$ at a eutectic composition in the temperature range 1123-1600 K and at 1200 K in the composition range $2-45\%$ ${\rm ThF_4}$. Although reports on variations of density with temperature exist in the literature, we report for the first time variations of the density and enthalpy of ${\rm LiF-ThF_4}$ with the concentration of ${\rm ThF_4}$ and fit them with the square root function of ${\rm ThF_4}$ concentration. This fitting formula will be useful for the experimentalist to obtain the density and enthalpy data over the entire concentration range for designing the reactor. We have observed an interesting oscillating pattern for the MS diffusivity for the cation pair, in which $\mathcal{D}_{{\rm Li-Th}}$ oscillates between positive and negative values with the amplitude of the oscillation reducing as the system becomes rich in ${\rm ThF_4}$. The amplitude of the oscillation is the highest around 0.06 mole fraction of ${\rm ThF_4}$ and finally settles close to 0 around $48\%$ of ${\rm ThF_4}$. Through the velocity autocorrelation function, vibrational density of states (VDOS), radial distribution function (RDF) analysis, and structural snapshots, we predict that formation of negatively charged $[\rm ThF_n]^{4-n}$ clusters makes positively charged ${\rm Li^+}$ ions oscillate between different clusters with the range of its motion reducing (except initial rise) as the number of clusters increases and finally ${\rm Li^+}$ ions get trapped when the electrostatic force on ${\rm Li^+}$ exerted by various clusters surrounding it is almost getting balanced. This prediction may put a limitation on the percentage of ${\rm ThF_4}$ to be used in MSR to optimize the neutron economy. Oscillation of flux correlations and preservation of the VDOS peak for Th-F and F-F correlations at a higher ThF% indicate the cage dynamics due to the formation of the $[\rm ThF_n]^{4-n}$ network, supported by a reduction in the F-F separation through RDF and a structural snapshot, which control the multicomponent dynamics establishing a correlation between the structure and dynamics.

The article is organized as follows: in the next section, the theoretical formulation is outlined (detailed description is given in the *Supporting Information* (SI)) followed by computational details. The results of our calculations are presented and discussed in *Section 4*. The conclusions are summarized in *Section 5*.

### 2. THEORETICAL OUTLINE
In the present work, multicomponent diffusion is computed according to the Maxwell-Stefan (MS) approach, first proposed by Maxwell and extended by Stefan,$^{19}$ in which the driving force ($\hat{\mathbf{X}}$) is proportional to the relative velocity between the species in the system.$^{20}$ Through MD simulations, we have computed the Onsager dynamical matrix using Green-Kubo formalism$^{26}$ as well as using Einstein form,$^{28}$ and the three independent MS diffusivities for a ternary mixture have been evaluated outside the MD simulations using an in-house code from the elements of $\mathbf{B}$ matrix.$^{27}$ The detailed theoretical formalism has been described in our earlier work$^{22,24}$ and also given in the SI.

### 3. COMPUTATIONAL DETAILS
MD simulations are performed with 5000-6000 ions (changing with compositions) in a cubic cell under periodic boundary conditions using MD package DL_POLY_4$^{29}$ to compute MS diffusivity through Onsager phenomenological coefficients. As no MD package can directly provide the elements of the Onsager dynamical matrix, we have developed various modules in Fortran 90 using Green-Kubo and Einstein forms and incorporated these modules in DL_POLY_4. During the course of simulation, these modules take velocities and

positions at each time step as input from DL_POLY_4 and keep computing the Onsager phenomenological coefficients, giving the advantage of not keeping huge files containing the positions and velocities of all ions for a longer simulation period. The MS diffusivities are computed from Onsager phenomenological coefficients using an in-house code outside the MD simulations.

For the molten salt LiF−ThF₄, we have used Born−Mayer−Huggins (BHM) short-ranged potential, originally developed by Fumi and Tosi³⁰ with the parameters described in Dewan's work¹⁴ along with the long-range Coulomb interaction. The functional form of the short-range potential is expressed as

$$
\Phi_{i j}^{\text {short }}=B_{i j} e^{-\alpha r_{i j}}-\frac{C_{i j}}{r_{i j}^{6}}-\frac{D_{i j}}{r_{i j}^{8}}
\tag{2}
$$

where $\alpha$, $B$, $C$, and $D$ are the parameters and $r_{ij}$ is the interionic distance between the ions $i$ and $j$. The first term is the exponential repulsion term, whereas the second and third terms describe the dipole−dipole and dipole−quadrupole interactions, respectively. For the molten salt, the BHM potential has been successfully employed in predicting several thermodynamic, structural, and transport properties³¹,³² and is as good as polarizable models that are derived from ab initio simulations.³³
Figure 1 displays the short-range interactions between various pairs. We can see that the interaction is the strongest for the Th−F pair and weakest for the Li−Li pair, whereas the range of the interaction is longer for the Th−Li pair. The initial configurations for various compositions were generated using PACKMOL³⁴ software by randomly placing LiF and ThF₄ molecules in a cubic box. The system is equilibrated first in the NPT ensemble for 1 ns and then in the NVT ensemble for 1 ns, and then dynamical correlations data were collected for another 400 ps after verifying that the system is in the diffusion regime, making the total simulation length up to 2.4 ns. A time step of 1 fs was used to integrate Newton's equations of motion, employing the Velocity Verlet algorithm. We have employed the overlapped data structure¹² to improve the statistics without extending the simulation length where the data are stored in different blocks called a buffer (here, we have used 50 buffers) with different time origins. The Onsager coefficients as well as diffusion coefficients are computed by averaging over 5000 independent data sets with each set containing data for 4000 time steps (4 ps) in each run, and further they were averaged from six independent runs for each thermodynamic state point. Because of powerful features of the overlapped data structure¹² method, the effective time length for data collection for each thermodynamic state point becomes $4\ \text{ps} \times 5000 \times 6 = 120\ \text{ns}$. As the overlapping data structure feature is not there in DL_POLY_4, we have developed these modules and incorporated them in DL_POLY_4. The long-range electrostatic interactions in this periodic cubic system are modeled by smoothed particle mesh Ewald summation. The largest $K$-vector in the reciprocal space is given by $K_{\text{max}} = (2\pi/L)K_{\text{maxa}}$, where $L$ is the width of the cell in each direction and $K_{\text{maxa}}$ is an integer in each direction (for a cubic system, three integers are the same). We have considered $K_{\text{maxa}} = 14$ and checked the accuracy of the Ewald sum by comparing the Coulomb energy and the virial.²⁹

![](./images/811188121365381120_2.jpg)

Figure 1. Short-ranged BHM interactions for the LiF−ThF₄ mixture.

## 4. RESULTS AND DISCUSSION

### 4.1. Density, Enthalpy, Specific Heat Capacity, and Self-Diffusivity.
First, we have carried out NPT simulations to optimize the cell length and compute the density of the salt mixture at different compositions and temperatures. For a eutectic mixture at 1273 K, the computed density is $4.15\ \text{g/cm}^3$, as compared to the experimental value of $3.95\ \text{g/cm}^3$ and the simulated value of $3.83\ \text{g/cm}^3$ by Dewan et al.¹⁴ Thus, the computed density matches reasonably well with the experimental data within 5% error. Although the temperature dependence of density has been fit with a linear relation by many groups, a concentration (ThF₄ mole fraction) dependence of density may not exist, although it is important for the experimentalist to have access to the density over the entire concentration range from the fitting formula. In Figure 2, we plot the density of the mixture at 1273 K with the mole fraction of ThF₄ in the mixture. We try to fit the simulated data and find that the density, $\rho$, can be best described as $\rho = a + b\sqrt{C}$, with an excellent agreement between simulated and fitted data as shown in Figure 2 with $C$ as the mole fraction of ThF₄. The computed specific enthalpy for the eutectic mixture at 1273 K is $-27.85\ \text{kJ g}^{-1}$, in excellent agreement with the value of $-27.8\ \text{kJ g}^{-1}$ computed by Dewan et al.¹⁴ The specific enthalpy at various mole fractions of ThF₄ at 1273 K has been computed for the first time and plotted in Figure 3a. The enthalpy of the system increases as the mixture becomes rich in ThF₄. The specific enthalpy of the mixture varies with the square root of mole fraction of ThF₄, as shown in Figure 3a. So the density

![](./images/811188121365381120_3.jpg)

Figure 2. Variation of density with the concentration of ThF₄ at 1273 K.


![](./images/811188121365381120_4.jpg)

Figure 3. Variation of (a) specific enthalpy with the concentration of ThF₄ at 1273 K and (b) specific heat capacity with the concentration of ThF₄ at 1273 K.

![](./images/811188121365381120_5.jpg)

Figure 4. (a) Variation of MSD with time in an NVT simulation (after a 1 ns NPT run) at 1273 K for LiF−ThF₄ with 10% ThF₄; the linear variation of MSD indicates that the system is in the diffusion regime. (b) Plot of MSD with time on a log−log scale; the slope of MSD for all of the ions is almost 1.0, which confirms that the system has reached the diffusion zone.

and specific enthalpy at a particular temperature have similar dependence on the mole fraction of ThF₄. The specific heat capacity of the system is defined as

$$
C_{\mathrm{m}}^{p}=\left(\frac{\partial H_{\mathrm{m}}}{\partial T}\right)_{p} \tag{3}
$$

where $H_{\mathrm{m}}$ is the specific enthalpy and $C_{\mathrm{m}}^{p}$ is the specific heat capacity. The computed heat capacity for the eutectic mixture at 1273 K is 1.08 J g⁻¹ K⁻¹, which matches nicely with the experimental value of 1.0 J g⁻¹ K⁻¹ and simulated value of 1.049 J g⁻¹ K⁻¹ by Dewan et al.¹⁴ The variation of specific heat capacity at 1273 K with the mole fraction of ThF₄ is depicted in Figure 3b. We can see that specific heat capacity decreases for a higher ThF₄ mole fraction, which is expected as the specific heat capacity of LiF is higher than that of ThF₄.

Now, we will discuss the computation of self-diffusion coefficients through MD simulations. Here, we need to consider two issues very seriously: (1) reaching diffusion regime: the system should reach the diffusion regime before collection of dynamical data. (2) Improving statistics: to improve the statistics, sufficient amount of data and reasonable number of averaging from various data set of different time origins should be taken in each run. Then, final diffusivity should be computed by taking average from a set of independent runs. Figure 4a presents the temporal variation of the mean-square displacement (MSD) during the NVT simulation after NPT run (1 ns) at 1273 K for the LiF−ThF₄ mixture with 10% ThF₄. We can see from Figure 4a that the system exhibits a normal linear diffusive behavior (MSD ∝ $t$) after escaping the initial quadratic (MSD ∝ $t^{2}$) region¹³ even before 1 ns. In Figure 4b, we have plotted MSD versus time on a log−log scale and computed the slope. The slope of MSD is almost 1 on the log−log scale for all three ions, which again confirms that the system is in a regime for diffusive motion. We can see that MSD for Li is higher than that for F and Th, consistent with the fact that Li, being the lightest ion, diffuses faster than Th and F. To improve the statistics, we have employed the overlapped data structure³⁵ feature as described in Section 3. Self-diffusion coefficients obtained from MD simulations at 1273 K for the eutectic mixture (22% ThF₄) and for 50% ThF₄ mole % are presented in Table 1. The self-diffusion coefficients computed for $D_{\mathrm{Li}}$, $D_{\mathrm{F}}$, and $D_{\mathrm{Th}}$ are 8.3, 4.1, and 1.6 ($10^{-9}$ m² s⁻¹) and match reasonably well with the values of 8.83, 4.22, and 1.62 ($10^{-9}$ m² s⁻¹), respectively, reported by Dewan et al.¹⁴ The error bar presents one sigma standard error from six independent runs, which is less than 10% due to improved statistics. We can see that Li⁺ ions, being the lightest, diffuse faster and Th⁴⁺ ions move slowly as

<table>
<caption>Table 1. Self-Diffusion Coefficients of Ions for Different Compositions at 1273 K</caption>
<thead>
<tr>
<th rowspan="2">ions</th>
<th colspan="2">self-diffusion coefficients ($10^{-9}$ m² s⁻¹) for various compositions (ThF₄%)</th>
</tr>
<tr>
<th>22% (eutectic)</th>
<th>50%</th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>8.3 ± 0.62</td>
<td>6.9 ± 0.55</td>
</tr>
<tr>
<td>F</td>
<td>4.1 ± 0.36</td>
<td>3.4 ± 0.30</td>
</tr>
<tr>
<td>Th</td>
<td>1.6 ± 0.15</td>
<td>1.3 ± 0.12</td>
</tr>
</tbody>
</table>

expected. As seen from Table 1, self-diffusion coefficients for all three species decrease with increase in ThF₄ mole %. The close agreement of the computed thermodynamic parameters with the experimental data gives us the confidence regarding the validity of the force-field parameters and the accuracy of the simulation methods.

4.2. Diffusive Flux Correlations and Onsager Coefficients. Figure 5a presents the temporal variation of the diffusive flux correlations for the eutectic mixture (22% LiF) at a temperature of 1273 K. We notice prominent backscattering or a cage effect, which involves alternate negative and positive flux correlations after the initial decay for Th−F and F−F correlations. This may be due to stronger short-range interactions between Th−F and F−F pairs compared to those in others, as shown in Figure 1. The backscattering is almost negligible for Th−Th and Li−F pairs. The area constructed by the diffusive flux correlations with the X axis is a measure of the diffusivity of the species. The Li−Li ion pair diffuses much faster, which is expected as Li⁺ is the lightest ion in the system. The flux correlations for the Th−Th pair are almost flat. This is due to the fact that short-range interactions between Th−Th ions at an average separation (4.36 Å obtained from RDF) are almost zero, as seen in Figure 1. With increase in thermal energy although the diffusivity of the ions increases, there is almost no change in the cage dynamics patterns except slight decay in the oscillation for Th−F and F−F pairs, as indicated by the temporal variation of the diffusive flux correlations at 1500 K in Figure 5b. To see the effect of ThF₄ concentration on the temporal variation of diffusive flux correlations, in Figure 6 we present flux correlations for 4, 15, 30, and 45% ThF₄ at 1273 K. It is clear that as we increase the ThF₄ mole fraction the backscattering for the Th−F and F−F correlations becomes increasingly stronger, whereas for the Li−F pair, the cage dynamics diminishes beyond 4% of ThF₄ mole fraction. The oscillating nature of flux correlations for Th−F and F−F may indicate the formation of $[\text{Th}F_n]^{4-n}$ clusters for the ThF₄ rich mixture. As the ThF₄ mole fraction increases, Li−F flux correlation becomes almost flat, indicating a negligible interaction between the Li−F pair. The area under the curve reduces for almost all correlations with increasing ThF₄ mole fraction, which signifies that the species moves slowly making the mixture more sluggish.

Figure 7a displays the variation of Onsager coefficient with temperature for the eutectic mixture obtained from the time integral of diffusive flux correlation. With increasing thermal energy, ions become more dynamic and the magnitude of the Onsager coefficient increases. At any temperature, the Li−Li pair has the maximum Onsager coefficient, owing to its lightest mass. We can note that all of the Onsager coefficients are $O(10^{-9})$ m²/s, which is expected for typical ions in the liquid state. The Onsager coefficients for the pairs Li−F, Th−F, and Li−Th are negative, which is consistent with diffusive flux correlations, as shown in Figure 6, where Li−F and Th−F (Li−Th not shown) correlations start with a negative value and the effective area under X axis is also negative. Figure 7b depicts the concentration dependence of Onsager coefficient at 1200 K. The magnitudes of all Onsager coefficients reduce as the mixture becomes increasingly richer in ThF₄. The correlation Li−Li has the highest magnitude for all concentrations as its flux correlation function has largest area under the X axis for all concentrations, as depicted by Figure 6, and it reduces sharply with increasing ThF₄ mole fraction. After initial reduction, there is a negligible change of the Onsager coefficients of pairs F−F and Th−F due to the oscillating nature of flux correlations, which keeps the area almost the same. In general, all of the species move slowly with increasing ThF₄ mole fraction, making the ThF₄-rich mixture sluggish. The reduction in the Onsager coefficient with an increasing ThF₄ mole fraction is consistent with the reduction in the self-diffusivity of the ions with an increasing ThF₄ mole fraction, as presented in Table 1.

4.3. MS Diffusivity. Figure 8 depicts the variation of MS diffusivity with temperature for the eutectic mixture (22% ThF₄), where the error bar indicated by magenta color presents one sigma standard error from six independent runs. With increasing temperature, all three diffusivities, $D_{\text{LiF}}$, $D_{\text{ThF}}$, and $D_{\text{LiTh}}$, increase almost linearly, and we do not observe any diverging behavior reported in molten salt LiCl−KCl, where the diffusivity, $D_{\text{LiK}}$, becomes negative and divergent.²² For the

![](./images/811188121365381120_6.jpg)

Figure 5. Temporal variation of diffusive flux correlation, $\Psi(t)$, for the eutectic mixture (22% ThF₄) at (a) 1273 K and (b) 1500 K.

![](./images/811188121365381120_7.jpg)

Figure 6. Temporal variation of diffusive flux correlation, $\Psi(t)$, at 1200 K for the following compositions: (a) 4% ThF₄, (b) 15% ThF₄, (c) 30% ThF₄, and (d) 45% ThF₄.

![](./images/811188121365381120_8.jpg)

Figure 7. Variation of Onsager coefficients ($\Lambda$ matrix elements) with (a) temperature for the eutectic mixture (22% ThF₄) and (b) composition at 1200 K.

eutectic mixture, $D_{\text{LiF}}$ rises slowly with temperature compared to $D_{\text{ThF}}$ and $D_{\text{LiTh}}$, which have similar variation.

The concentration dependence of MS diffusivity at a temperature of 1200 K is delineated in Figure 9, where the error bar indicated by magenta color presents one sigma standard error from six independent runs. We observe an interesting composition dependence, although the MS diffusivities are expected to depend very lightly on the composition, owing to the decoupling of the thermodynamic factor arising because of nonideality of the mixture. The most exciting feature is the oscillating pattern for MS diffusivity $D_{\text{LiTh}}$ where it oscillates between positive and negative values for the LiF-rich mixture and finally settles close to zero for a higher mole fraction of ThF₄. The amplitude of the oscillation is highest around 0.06 mole fraction of ThF₄. In the whole concentration range, it changes sign five times and the sign crossover occurs around the 2.23, 4.36, 9.1, 14.3, and 43.9 mole % of ThF₄, as shown in Figure 9a. We can observe that the

![](./images/811188121365381120_9.jpg)

Figure 8. Variation of MS diffusivities with temperature at eutectic composition; the error bar indicated by magenta color presents one sigma standard error from six independent runs.

concentration difference, $\Delta c$, between successive sign crossover points increases with a reduction in amplitude (after an initial rise) as we move toward the higher mole % of $\mathrm{ThF}_{4}$. The scenario can be visualized as $\mathrm{Li}^{+}$ions oscillating back and forth with respect to $\mathrm{Th}^{4+}$ ions with both the speed and range of their motion restricted for the $\mathrm{ThF}_{4}$ mixture. Unlike in $\mathrm{LiCl}-\mathrm{KCl}^{22}$ where the MS diffusivity between the cation–cation ion pairs becomes divergent at some particular concentration, here the MS diffusivity between the cation pair Th–Li remains finite over the whole concentration range with oscillation between positive and negative values. Although negative MS diffusivity has been reported in few cases for electrolyte solutions especially between the cation–cation pair, where $D_{++}$ remains negative for most of the concentration range and becomes positive for higher concentration $^{21}$ range, here for the first time we observe an oscillating pattern for $D_{\text{LiTh}}$ with five sign crossover points over the concentration range. We try to fit the simulated data through an exponential function with a cosine term and find that $D_{\text{LiTh}}$ can be best described as $D_{\text{LiTh}} = A \exp(-bc) \cos(\omega c + \Phi)$, as shown in Figure 9c, where $c$ is the mole $\%$ of $\mathrm{ThF}_{4}$ and $A$, $b$, $\omega$, and $\Phi$ are the adjusting parameters.

The MS diffusivity between the cation–anion pair, $D_{\text{LiF}}$, decreases slightly with an increase in $\mathrm{ThF}_{4}$ mole fraction and then starts increasing at around 4–6% of $\mathrm{ThF}_{4}$, and finally falls close to zero for the $\mathrm{ThF}_{4}$-rich mixture, as shown in Figure 9b. The third independent MS diffusivity, $D_{\text{ThF}}$, starts with a negative value for 0.02 mole fraction of $\mathrm{ThF}_{4}$, as shown in Figure 9b. With increasing mole fraction, it then increases

![](./images/811188121365381120_10.jpg)

Figure 9. (a) Variation of MS diffusivity $D_{\text{LiTh}}$ with mole $\%$ of $\mathrm{ThF}_{4}$ at 1200 K, (b) variation of MS diffusivities $D_{\text{LiF}}$ and $D_{\text{ThF}}$ with mole $\%$ of $\mathrm{ThF}_{4}$ at 1200 K, (c) fitting of MS diffusivity $D_{\text{LiTh}}$ with concentration of $\mathrm{ThF}_{4}$ (mole $\%$), (d) variation of entropy constraint with mole $\%$ of $\mathrm{ThF}_{4}$ at 1200 K showing a non-negative entropy production rate at all thermodynamic states. The error bar for MS diffusivity indicated by magenta color presents one sigma standard error from six independent runs.

![](./images/811188121365381120_11.jpg)

Figure 10. Structural snapshot of the salt mixture at 1200 K for various compositions: (a) 4% ThF₄, (b) 22% ThF₄, (c) 45% ThF₄; green, blue, and silver colors represent Li, Th, and F ions, respectively.

![](./images/811188121365381120_12.jpg)

Figure 11. RDF for the salt mixture with 4, 15, 22, and 45% of ThF₄ molecules at 1200 K for the ion pairs (a) Th−F, (b) F−F, and (c) Li−F.

exponentially and becomes positive having a maximum value of 6.359 m²/s at around 4−6% of ThF₄ and then reduces toward zero. At a higher ThF₄ mole fraction, all three MS diffusivities tend to zero, making the mixture sluggish for the ThF₄-rich mixture, and the viscosity becomes high. In the whole concentration range, both the cation−anion MS diffusivities, $\mathcal{D}_{\text{ThF}}$ and $\mathcal{D}_{\text{LiF}}$, remain positive, whereas the cation−cation MS diffusivity fluctuates between positive and negative values.

In the MS framework, the negative diffusivity is considered acceptable, provided the total rate of entropy produced by all the diffusing species is positive definite, as demanded by the second law of thermodynamics.²⁰ In our earlier work, in LiF−BeF₂, a sign crossover by all three MS diffusivities has been reported, indicating that both cation−anion and anion−cation MS diffusivities can take negative values provided the total rate of entropy production remains positive. The entropy production rate per unit volume can be expressed as²⁰

$$
\dot{\sigma}=c R \sum_{\substack{i=1 \\ i>k}}^{n} \frac{x_{i} x_{k}}{\mathcal{D}_{i k}}\left(\hat{\mathbf{U}}_{i}-\hat{\mathbf{U}}_{k}\right)^{2}
\tag{4}
$$

where $R$ is the universal gas constant.

In an $n$-component ionic mixture, when various ions diffuse in an electrical and activity gradient to satisfy positive entropy production rate, as governed by the second law of thermodynamics, if one component consumes entropy due to its uphill diffusion, some other component produces entropy through downhill diffusion. So all of the independent MS diffusivites cannot be negative at the same thermodynamic state. The positive entropy production rate given by eq 4 leads to the following inequality, which holds for all thermodynamic states²¹

$$
\begin{gathered}
\beta_{a b}=\sum_{\substack{i=1 \\ i \neq a}}^{n}\left(\frac{x_{i} x_{a}}{\mathcal{D}_{i a}}\right) \sum_{\substack{j=1 \\ j \neq b}}^{n}\left(\frac{x_{j} x_{b}}{\mathcal{D}_{j b}}\right)-\left(\frac{x_{a} x_{b}}{\mathcal{D}_{a b}}\right)^{2} \geq 0, \\
a, b=(1,..., n), \quad a \neq b
\tag{5}
\end{gathered}
$$

We have computed all three entropy production constraints for the all compositions, which remain positive as shown in Figure 9d. So the entropy production rate remains non-negative at all thermodynamic states although MS diffusivity for the positive−positive ion pair is negative.

### 4.4. Correlation between Structure and Dynamics.
Now we will try to analyze the following: (1) What leads to such interesting concentration dependence of MS diffusivity? (2) What information regarding the local structure and relative dynamics of the ions can we extract from the behavior of the MS diffusivity? To find the answers to the above two questions, we perform a thorough analysis from MD snapshots, RDF, diffusive flux correlation, and VDOS.

#### 4.4.1. MD Snapshot.
To get some insight into the structure, we plot the MD snapshots of the mixture with 4, 22, and 45% ThF₄ molecules, as shown in Figure 10. We can see that as the number of ThF₄ molecules increases from 4 to 22%, there is a tendency for the formation of $[\text{ThF}_{n}]^{4-n}$ clusters. Cluster formation at a higher ThF₄ mole fraction is also mentioned by Liu et al.¹⁵ with coexistence of $[\text{ThF}_{7}]^{-3}$, $[\text{ThF}_{8}]^{-4}$, $[\text{ThF}_{9}]^{-5}$, and $[\text{ThF}_{10}]^{-6}$ complexes in the melt. As the dominant coordination number of the complexes in the melt is around 8,¹⁵ F⁻ ions move toward Th⁴⁺ ions for the initiation of the

![](./images/811188121365381120_13.jpg)

Figure 12. VDOS function for the salt mixture with 1, 4, 6, 22, and 45% ThF₄ at 1200 K for the correlations between the ion pairs (a) Th−F and (b) F−F; the peak frequency remains almost constant (5.3 THz) from 6% onward, indicating metastable cage formation.

clustering process. Because the cluster as a whole is negatively charged, Li⁺ ions get attracted and move around the clusters. As more ThF₄ molecules are introduced, more clusters are formed and the number of Li⁺ ions is reduced. One Li⁺ ion can now experience Coulomb attractive forces from few clusters around it, as shown in Figure 10c for 45% of ThF₄, where one Li⁺ ion is surrounded by five $[ThF_{n}]^{4-n}$ clusters. It may happen that at higher ThF₄ mole fractions, the forces on the Li⁺ ion by various $[ThF_{n}]^{4-n}$ clusters get balanced and the Li⁺ ion can be trapped by the clusters.

4.4.2. RDF. To verify the structural information obtained from MD snapshots, in Figure 11 we display the RDF for the Th−F, F−F, and Li−F pairs for 4, 15, 22, and 45% of ThF₄ molecules at 1200 K. For the Th−F pair, the RDF shows a very sharp first peak at 2.23 Å in comparison to 2.24 Å reported by Liu et al.¹⁵ and 2.26 Å obtained by Dewan et al.¹⁴ There is almost no change in the position of the first peak with increasing ThF₄ mole fraction although the second peak gets slightly shifted toward lower value. The sharp first peak with deep minima indicates a partially covalently bonded cluster. For F−F correlation, the position of the first peak is shifted from 2.83 Å at 0.04 mole fraction of ThF₄ to 2.63 Å at 0.45 mole fraction of ThF₄, as shown in Figure 11b. For the Li−F pair, the first peak is not sharp compared to that of Th−F. With increasing ThF₄ concentration, there is a reduction in the average F−F separation and a sharp peak for the Th−F signal toward $[ThF_{n}]^{4-n}$ cluster formation at a higher ThF₄ mole fraction, as predicted by the MD snapshots as well.

4.4.3. Diffusive Flux Correlations and VDOS. To correlate the structure with the dynamics, we try to relate the structural information obtained through MD snapshots and RDF analysis with the temporal variation of the diffusive flux correlation as depicted in Figure 6. For Th−F and Th−Th pairs, we can hardly see any oscillation for the LiF-rich mixture with ThF₄ mole fraction of 0.04 and 0.15 as displayed in Figure 6a,b respectively. As the ThF₄ mole fraction increases, the oscillation in diffusive flux correlation for Th−Th and Th−F becomes increasingly stronger, as shown in Figure 6c,d, indicating the formation of $[ThF_{n}]^{4-n}$ clusters where F ions oscillate back and forth around Th⁴⁺ ions and the relative configuration of the F ions does not change much and they also oscillate relative to each other in the cluster. So the formation of $[ThF_{n}]^{4-n}$ clusters at a higher ThF₄ mole fraction, as suggested by MD snapshot and RDF analysis obtained through structural data, has also been demonstrated by diffusive flux correlation obtained through the dynamics of the ions. In Figure 12, we display the VDOS which is calculated from the Fourier transformation of the diffusive flux correlations. Interestingly, for Th−F and F−F correlations, the peak frequency remains almost constant ($\nu^{m} \approx$ 5.3 THz) once the mixture contains ThF₄ beyond 6%, which seems to be the ThF₄ concentration where network formation initiates. Preservation of the VDOS peak can be interrelated with the prolonged and persistent backscattering in the diffusive flux correlations for Th−F and F−F pairs, as seen in Figure 6. For a low concentration of ThF₄, we observe smearing of the peak frequencies and broadening of the low frequencies. Please note that for both Th−F and F−F correlations, the peak frequency is almost the same. Preservation of VDOS peak, persistence of backscattering in the diffusive flux correlation (Th−F and F−F), and sharp Th−F peak along with reduced F−F separation with increasing ThF₄ concentration in RDF resemble a metastable phase due to the formation of $[ThF_{n}]^{4-n}$ clusters at a higher ThF₄ mole fraction. So there exists an interplay between the structure and dynamics of the ions in which the local structure controls the dynamics of the ions, which may have strong impact on the performance of the reactor.

4.5. Explanation for Unusual Variation of MS Diffusivity. In light of the structural information obtained through the RDF, MD snaps, and diffusive flux correlations, we will now try to explain the interesting concentration dependence of MS diffusivity as discussed in Section 4.3.

4.5.1. Explanation for $D_{LiTh}$. As more and more ThF₄ molecules are introduced in pure LiF, the F⁻ ions around Li⁺ ions rearrange themselves to be around Th4⁺ ions as Th has a coordination number around 8, which initiates the process of cluster formation, as shown in Figure 10b. As the cluster as a whole is an anion, Li⁺ ions are attracted toward it and move around it to avoid the repulsive force between Li⁺−Li⁺ ions. As more ThF₄ molecules are introduced, the Li⁺ ion can see more $[ThF_{n}]^{4-n}$ clusters and can move around one cluster to another cluster. So Li⁺ ions can have back and forth movement with respect to Th⁴⁺ ions, resulting in an oscillatory behavior of MS diffusivity between Th−Li ions, as displayed in Figure 9a. If one side movement corresponds to positive MS diffusivity, the reverse movement should have negative MS diffusivity. With an

increase in $ThF_4\%$, the $Li^+$ ion may be surrounded by many clusters. So the range of back−forth movement in $Li^+$ with respect to Th reduces, which is reflected by the reduction in the amplitude (except the initial rise) of the oscillation, as shown in Figure 9a. All of these clusters being anions attract $Li^+$ ions. Finally, at a very high $ThF_4\%$, the Coulomb force on $Li^+$ may be almost balanced by the attractive forces from different clusters, resulting in almost no net motion of $Li^+$ ions. We can say that $Li^+$, the most dynamic ion of the mixture, is getting trapped by the $[ThF_n]^{4-n}$ cluster. This is an interesting pattern observed in the multicomponent diffusion phenomenon in $LiF-ThF_4$.

4.5.2. Explanation for $D_{LiF}$. When few $ThF_4$ molecules are introduced in the system, the movement of the $Li^+$ ions with respect to Th ions gets disturbed due to the presence of $Th^{4+}$ ion with a higher charge state. In this case, $Li^+$ ions have to avoid $Th^{4+}$ ions as well as $Li^+$ ions for their movement. This may be the reason for the initial decrease in MS diffusivity $D_{LiF}$, as shown in Figure 9b. When more $Th^{4+}$ ions are introduced, the nearby $F^-$ ions around $Li^+$ ions move toward $Th^{4+}$ ions as $Th^{4+}$ has an average coordination number around 8−9. So the $F^-$ ions move with respect to $Li^+$ ions to initiate the $[ThF_n]^{4-n}$ cluster formation procedure, resulting in an increase in MS diffusivity $D_{LiF}$. Once the cluster $[ThF_n]^{4-n}$ becomes increasingly stronger, Li ions move around the $[ThF_n]^{4-n}$ clusters as the cluster as a whole is negatively charged. So the $Li^+$ ions are always surrounded by $F^-$ ions, decreasing $D_{LiF}$ with an increase in $ThF_4\%$ as the clusters become higher in number.

4.5.3. Explanation for $D_{ThF}$. Once a few $ThF_4$ molecules are introduced into pure LiF, the $F^-$ ions are relatively more attracted by the heavier and higher-charge-state $Th^{4+}$ ions, resulting in an increase in the MS diffusivity, $D_{ThF}$, as shown in Figure 9b, where it increases exponentially and becomes positive from an initial negative value. This may be the concentration region where the formation of the $[ThF_n]^{4-n}$ cluster is initiated.$^{15}$ Once the cluster formation started, the $F^-$ ions cannot move much due to frictional (Coulomb) forces and go back and forth, resulting in a decrease in MS diffusivity between the pair $D_{ThF}$. The MS diffusivity goes on decreasing as bigger and more $[ThF_n]^{4-n}$ clusters are formed with an increase in $ThF_4\%$. Finally, all of the MS diffusivity tends to zero, making the mixture sluggish for the $ThF_4$-rich mixture, and the viscosity becomes high.

4.6. Significance for Reactor Applications. The salt $LiF-ThF_4$ is used as a coolant as well as a fuel in MSRs. The formation of $[ThF_n]^{4-n}$ clusters at higher $ThF_4\%$ may have strong impact on the neutronics of the reactor. When a $Th^{4+}$ ion is surrounded by many $F^-$ ions, the probability of the neutron to collide with $F^-$ ion is higher, especially for thermal neutrons. As the thermal neutron has the substantial scattering cross section with $F^-$, it may get scattered by $F^-$ ions before reaching the $Th^{4+}$ ion. So the probability of the thermal neutron reaching $Th^{4+}$ ions reduces as the cluster becomes increasingly bigger. This may have an impact on the neutron economy because, for the same amount of thorium inventory, the extracted power (or $K_{eff}$)$^{35}$ will be lower if the salt takes a clustering configuration. In reactor physics calculation in general, the molecular structure is not taken explicitly and $K_{eff}$ is computed on the basis of number density only. Because of the clustering effect, the composition of the fuel becomes very critical in designing the reactor. As $LiF-ThF_4$ also serves as a coolant, it needs to remove the heat more efficiently. For an efficient coolant, all of the components should diffuse faster and there should not be any network formation. As the concentration of $ThF_4$ increases, the mixture becomes less dynamic and the diffusivity of the ions reduces, as seen from Table 1, where self-diffusivity of the ions reduces with increasing $ThF_4$ mole fractions. Reduction in diffusivity along with cluster formation tendency puts an upper limit on $ThF_4\%$ to optimize power in MSRs.

## 5. CONCLUSIONS
Using equilibrium MD simulations, we report the local structure and multicomponent dynamics of the molten salt mixture $LiF-ThF_4$ at different compositions and temperatures, which is considered as a fuel as well as a coolant in MSRs. We observe an unusual composition variation of MS diffusivity, where MS diffusivity between the cation−cation pair, $D_{Li-Th}$, oscillates between positive and negative values with its amplitude reducing as the mixture becomes richer in $ThF_4$. The negative MS diffusivity satisfies the positive entropy constraint at all thermodynamic states as demanded by the second law of thermodynamics. After comparing the self-diffusivity, density, and enthalpy of the eutectic mixture with the literature values, we report for the first time the variation of the density and enthalpy of $LiF-ThF_4$ with the concentration of $ThF_4$ mol %, with the density and enthalpy being fitted with the square root function of $ThF_4$ concentration. The data of enthalpy and density over the entire concentration range from the fitting formula will be very useful for the experimentalist to design MSRs. The diffusivity of all of the species reduces with increasing $ThF_4$ concentration and the salt becomes sluggish at a higher $ThF_4$ mol %. Preservation of the VDOS peak, persistence of backscattering in the diffusive flux correlation (Th−F and F−F), and the sharp Th−F peak along with the reduced F−F separation with increasing $ThF_4$ concentration in the RDF resemble a metastable phase due to the formation of $[ThF_n]^{4-n}$ clusters at a higher $ThF_4$ mole fraction. Formation of negatively charged $[ThF_n]^{4-n}$ clusters makes positively charged $Li^+$ ions oscillate between different clusters with the range of their motion being reduced (except the initial rise) as the number of $[ThF_n]^{4-n}$ clusters increases, and finally $Li^+$ ions almost get trapped at a higher $ThF_4\%$ when the electrostatic force on $Li^+$ exerted by various clusters surrounding it gets almost balanced. Because an efficient coolant should remove heat more effectively through diffusion of all species, the formation of $[ThF_n]^{4-n}$ clusters and reduction in the diffusivity of the ions at a higher $ThF_4\%$ may put a limitation on the percentage of $ThF_4$ to be used in MSRs to optimize the neutron economy.

## ASSOCIATED CONTENT
### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jpcb.6b05173.

Theoretical formalism for computing MS diffusivity using Onsager dynamical matrix through MD simulations (PDF)

## AUTHOR INFORMATION
### Corresponding Author
*E-mail: brahma@barc.gov.in. Phone: +91-2225592057.

### Notes
The authors declare no competing financial interest.

### ACKNOWLEDGMENTS

The authors would like to thank Dr. N.K. Sahoo for his constant support and encouragement. This work was possible due to the facilities and help from the staff of the BARC Computer Centre. The authors would also like to thank Abhijeet Gangan for useful discussions in curve fitting.

### REFERENCES

(1) Hansen, J. P.; McDonald, I. R. *Theory of Simple Liquids: with Applications to Soft Matter*; Academic Press, 2006.

(2) Grimes, W. R. Molten-Salt Reactor Chemistry. *Nucl. Appl. Technol.* **1970**, *8*, 137.

(3) Forsberg, C. W. http://fhr.nuc.berkeley.edu/wp-content/uploads/2014/09/AHTR.Nuclear.Technology.Article.May20.2003.pdf (accessed April 11, 2016).

(4) Mathieu, L.; Heuer, D.; Brissot, R.; Garzenne, C.; Le Brun, C.; Lecarpentier, D.; Liatard, E.; Loiseaux, J. M.; Meplan, O.; Merle-Lucotte, E.; et al. The Thorium Molten Salt Reactor: Moving on from the MSBR. *Prog. Nucl. Energy* **2006**, *48*, 664−679.

(5) Delpech, S.; Merle-Lucotte, E.; Heuer, D.; Allibert, M.; Ghetta, V.; Le-Brun, C.; Doligez, X.; Picard, G. Reactor Physic and Reprocessing Scheme for Innovative Molten Salt Reactor System. *J. Fluorine Chem.* **2009**, *130*, 11−17.

(6) Kato, T.; Inoue, T.; Iwai, T.; Arai, Y. Separation behaviors of actinides from rare-earths in molten salt electrorefining using saturated liquid cadmium cathode. *J. Nucl. Mater.* **2006**, *357*, 105−114.

(7) Katz, J. J.; Seaborg, G. T.; Morss, L. R. *The Chemistry of the Actinide Elements*, 2nd ed.; Chapman and Hall: New York, 1986; Vol. 1.

(8) Salanne, M.; et al. Calculation of Activities of Ions in Molten Salts with Potential Application to the Pyroprocessing of Nuclear Waste. *J. Phys. Chem. B* **2008**, *112*, 1177−1183.

(9) Idaho National Laboratory. http://inldigitallibrary.inl.gov/sti/4502650.pdf (accessed April 11, 2016).

(10) Benes, O.; Konings, R. J. M. Thermodynamic properties and phase diagrams for fluoride salts for nuclear applications. *J. Fluorine Chem.* **2009**, *130*, 22−29.

(11) Gheribi, A. E.; Corradini, D.; Dewan, L.; Chartrand, P.; Simon, C.; Madden, P. A.; Salanne, M. Prediction of the thermophysical properties of molten salt fast reactor fuel from first-principles. *Mol. Phys.* **2014**, *112*, 1305−1312.

(12) Rapaport, D. C. *The Art of Molecular Dynamics Simulations*; Cambridge University Press: Cambridge, 1995.

(13) Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*; Clarendon Press: Oxford, 1987.

(14) Dewan, L. C.; Simon, C.; Madden, P. A.; Hobbs, L. W.; Salanne, M. Molecular Dynamics Simulation of the Thermodynamic and Transport Properties of the Molten Salt Fast Reactor Fuel LiF−ThF₄. *J. Nucl. Mater.* **2013**, *434*, 322−327.

(15) Liu, J. B.; Chen, X.; Qiu, Y. H.; Xu, C. F.; Schwarz, W. H. E.; Li, J. Theoretical Studies of Structure and Dynamics of Molten Salts: The LiF−ThF₄ System. *J. Phys. Chem. B* **2014**, *118*, 13954−13962.

(16) Groot, S. R. D.; Mazur, P. *Nonequilibrium Thermodynamics* ; Dover Publications Inc.: New York, 1984.

(17) Hanley, H. J. M. *Transport Phenomena in Fluids*; Marcel Dekker: New York, 1969.

(18) Krishna, R.; Wesselingh, J. A. *Elements of Mass Transfer*; Ellis Horwood: Chichester, 1990; p 88.

(19) Curtiss, C. F.; Bird, R. B. Multicomponent Diffusion. *Ind. Eng. Chem. Res.* **1999**, *38*, 2515.

(20) Krishna, R.; Wesselingh, J. A. The Maxwell-Stefan approach to mass transfer. *Chem. Eng. Sci.* **1997**, *52*, 861−911.

(21) Kraaijeveld, G.; Wesselingh, A. Negative Maxwell-Stefan diffusion coefficients. *Ind. Eng. Chem. Res.* **1993**, *32*, 738−742.

(22) Chakraborty, B.; Wang, J.; Eapen, J. Multicomponent diffusion in molten LiCl-KCl: Dynamical correlations and divergent Maxwell-Stefan diffusivities. *Phys. Rev. E* **2013**, *87*, No. 052312.

(23) Deng, Z.; Smolyanitsky, A.; Li, Q.; Feng, X. Q.; Cannara, R. J. A. Adhesion-dependent negative friction coefficient on chemically modified graphite at the nanoscale. *Nat. Mater.* **2012**, *11*, 1032−1037.

(24) Chakraborty, B. Sign Crossover in All Maxwell−Stefan Diffusivities for Molten Salt LiF-BeF₂: A Molecular Dynamics Study. *J. Phys. Chem. B* **2015**, *119*, 10652.

(25) Zhou, Y.; Miller, G. H. Green-Kubo formulas for mutual diffusion coefficients in multicomponent systems. *J. Phys. Chem* **1996**, *100*, 5516−5524.

(26) Wheeler, D. R.; Newman, A. Molecular dynamics simulations of multicomponent diffusion. *J. Phys. Chem. B* **2004**, *108*, 18353−18361.

(27) Krishna, R.; van Baten, J. M. The Darken Relation for Multicomponent Diffusion in Liquid Mixtures of Linear Alkanes: An Investigation using Molecular Dynamics(MD) Simulations. *Ind. Eng. Chem. Res.* **2005**, *44*, 6939−6947.

(28) Keffer, D. J.; Gao, C. Y.; Edwards, B. J. On the Relationship between Fickian Diffusivities at the Continuum and Molecular Levels. *J. Phys. Chem. B* **2005**, *109*, 5279−5288.

(29) Todorov, I. T.; Smith, A. DL_POLY_3: the CCP5 national UK code for molecular-dynamics simulations. *Philos. Trans. R. Soc. London, Ser. A* **2004**, *362*, 1835.

(30) Tosi, M. P.; Fumi, F. G. Ionic Sizes and the Born Repulsive Parameters in the NaCl-type alkali halides-II: The generalized Huggins-Mayer Form. *J. Phys. Chem. Solids* **1964**, *25*, 45−52.

(31) Ribeiro, M. C. C. Chemla effect in molten LiCl/KCl and LiF/ KF mixtures. *J. Phys. Chem. B* **2003**, *107*, 4392−4402.

(32) Lantelme, F.; Turq, P. Ionic dynamics in the LiCl-KCl system at liquid state. *J. Chem. Phys.* **1982**, *77*, 3177−3187.

(33) Salanne, M.; Simon, C.; Turq, P.; Madden, P. A. Intermediate range chemical ordering of cations in simple molten alkali halides. *J. Phys. Condens. Matter* **2008**, *20*, No. 332101.

(34) Martínez, L.; Andrade, R.; Birgin, E. G.; Martínez, J. M. Packmol: A package for building initial configurations for molecular dynamics simulations. *J. Comput. Chem.* **2009**, *30*, 2157−2164.

(35) Glasstone, S.; Sesonske, A. *Nuclear Reactor Engineering*; Springer, 1994.