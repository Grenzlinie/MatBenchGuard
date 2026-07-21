Journal Pre-proof

![](./images/812715688320827392_1.jpg)

Analytical local stress model for UMo/Al dispersion fuel

Gwan Yoon Jeong, Yeon Soo Kim, Jaeyeong Park

| PII: | S0022-3115(19)30978-X |
|---|---|
| DOI: | https://doi.org/10.1016/j.jnucmat.2019.151881 |
| Reference: | NUMA 151881 |
| To appear in: | *Journal of Nuclear Materials* |

Received Date: 25 July 2019

Revised Date: 2 October 2019

Accepted Date: 1 November 2019

Please cite this article as: G.Y. Jeong, Y.S. Kim, J. Park, Analytical local stress model for UMo/Al dispersion fuel, *Journal of Nuclear Materials* (2019), doi: https://doi.org/10.1016/j.jnucmat.2019.151881.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier B.V.

# Analytical local stress model for UMo/Al dispersion fuel

Gwan Yoon Jeong$^{\text{a}}$, Yeon Soo Kim$^{\text{b}}$, Jaeyeong Park$^{\text{a}*}$

*Corresponding author: jypark@unist.ac.kr

a: Department of Nuclear Engineering, Ulsan National Institute of Science and Technology, 50 UNIST-gil, Eonyang-eup, Ulju-gun, Ulsan 44919 Republic of Korea

b: Argonne National Laboratory, 9700 South Cass Avenue, Argonne, IL 60439 USA

![](./images/812715688320827392_2.jpg)

### Abstract

The stress evolution occurring in UMo/Al dispersion fuel is important since it affects the fuel performance during irradiation. In this study, a new analytical model was developed to predict the local stresses in UMo/Al dispersion fuel. In the model, a hypothetical unit sphere composed of a UMo fuel particle, interaction layer (IL), and Al matrix was considered, and the governing equations for the stress-strain relationship, strain-displacement, and mechanical equilibrium were established using a spherical coordinate system. The mathematical derivations were obtained for local stresses in the radial and circumferential direction using a thick-walled sphere model. This analytical model employed the stress distribution as the boundary condition, which is calculated using a finite element model with homogenized fuel meat. The developed model's solution scheme was verified against Abaqus solutions obtained for two irradiated plates with heterogeneous meat. The model calculated consistent results for interfacial stresses in the IL and Al matrix, indicating that the newly developed model was reliable when simultaneously calculating fission gas pressurization on the UMo/IL/Al composite, and the use of the stress distribution in the homogenized fuel meat as the boundary condition for the analytical model was acceptable.

### 1. Introduction

UMo/Al dispersion fuel, UMo alloy fuel particles dispersed in an Al matrix, has been under development for the conversion of highly-enriched uranium (HEU) fuel into the low-enriched uranium (LEU) fuel that is utilized in research reactors [1]-[3]. In UMo/Al dispersion fuel, the fueled zone, also referred to as the fuel meat, is metallurgically bonded with the Al alloy cladding.

If this fuel is to warrant qualification for use, the main obstacle to overcome is the excessive fuel meat swelling known as breakaway swelling, which is caused by the growth of pores within the interaction layer between the UMo fuel and the Al matrix under high-power and/or high-burnup conditions [4][5]. The mechanism of this breakaway swelling is known by the interconnection of pores that weaken the overall strength of the fuel meat, even further facilitating pore growth.

It is believed that the formation of the pores in fuel meat is highly influenced by the microstructural changes that occur during irradiation, of which the characteristic phenomenon is interaction layer (IL) growth between the UMo particles and the Al matrix. The IL is known to become amorphous through irradiation [6][7]. The amorphous IL has a higher diffusivity than crystalline UMo and Al, which allows fission gases to migrate more readily through the IL. The released fission gases accumulate at the interface between the IL and Al matrix to form large pores [8][9]. To model the growth of this type of pore requires the prediction of local stress distribution around the pores.

The state of stress, largely affected by fuel mass relocation [10][11], also has a significant effect on pore growth. From post-irradiation examinations (PIE), large pores are typically formed in the regions apart from the lateral edges of the fuel meat where the fission density and fission rate are slightly higher but compressive stresses prevail. It indicates that burnup and fission rate are not the most deciding factors for pore growth, but other factors like stress are also important.

Mechanical analysis of the dispersion fuel is extremely complex. Fuel particles with different sizes are randomly distributed in the fuel meat, and fission-induced microstructural evolutions escalate its complexity even further. In order to predict local stresses, a heterogeneous domain needs to be modeled. A finite element method (FEM) using a commercially available program such as Abaqus is employed for this purpose. Several attempts have shown successful results (see [12]-[16] and references therein). However, these studies used models with representative elementary volume, which is the periodic unit cell for the fuel meat, so it was hard to fully analyze the effect of local stress in the fuel meat. These models also cannot be implemented directly in another performance modeling code such as DART [17] or PRIME [18] because the calculation is made via Abaqus. A more convenient method is having a simpler model that can be more readily implemented in a performance modeling code.

Researchers have also employed other approaches which deal with a homogeneous-meat model, in which the fuel meat constituents were homogenized into an effective medium, and they applied a much simpler FEM. Using this model, thermo-mechanical deformation of fuel meat was simulated and the corresponding stress distribution as a byproduct was obtained, albeit simplified [18]. However, this simple model lacks the necessary details for local stress distribution that are needed for pore growth modeling.

In order to improve the homogenized-meat model without using the complex Abaqus scheme, while also producing reasonable details in stress predictions, we have developed a 'hybrid model' that supplements the simple homogenized-meat FEM model with an additional analytical model in this study. The solution scheme is derived based on the thick-wall sphere theory, in which a hypothetical

sphere composed of UMo, IL, and Al is taken into account. The analytical model uses the stress states calculated by the homogeneous-meat FEM model as the boundary condition. The hybrid model is then verified by comparing it with the heterogeneous model using the Abaqus commercial FEM package discussed above.

## 2. Theory and derivation
### 2.1. Hypothetical sphere model
As mentioned earlier, the domain of calculation is a composite with UMo fuel particles randomly dispersed in the Al matrix, as shown in Fig. 1(a). IL growth takes place during irradiation with the consumption of the UMo and Al matrix. The Al has a higher consumption rate because the diffusion flux of Al in the UMo is much larger than that of UMo in the Al matrix. When IL growth progresses and the ILs of neighboring UMo particles come into contact, the IL phase starts to become a continuous phase in the fuel meat (see Fig. 1(b)).

A system of equations was derived to calculate stresses for the UMo fuel, IL and Al matrix, represented by the hypothetical composite sphere illustrated in Fig. 1(c). From this theoretical approach, it is possible to find the radial stress component at the IL/Al matrix (or UMo/IL) interface where the large-sized pores formed. This radial stress component, which is equivalent to the hydrostatic stress exerted on pores formed at the interface, can be coupled with the pore growth prediction model.

![](./images/812715688320827392_3.jpg)

Fig. 1 Illustration of the hypothetical composite model. (a) a schematic of the cross-section for a plate and an image of fuel meat cross-section, (b) image showing microstructure after irradiation (V1R010 from RERTR-6 [10]), and (c) a schematic showing a hypothetical

composite cell for the model derivation.

The stresses around the hypothetical sphere are determined by fission-induced creep and swelling of the UMo particle, thermal expansion, chemical volume expansion of the IL formation, internal pressure of fission gas bubbles within the UMo particle, and external pressure exerted by the reactor coolant. The corresponding volumetric strain for all components in the hypothetical composite sphere is expressed by treating a UMo particle as an internally-pressurized thick-walled sphere containing a hypothetical fission gas bubble. The thickness of the matrix layer is determined by the uranium loading of the fuel meat. For example, a uranium loading of $8\ \text{gU/cm}^3$ with a UMo particle size of 70 $\mu\text{m}$ gives an Al matrix layer of $9.5\ \mu\text{m}$.

### 2.2. General equations

Three governing equations are given for the system to access mechanical states: the constitutive equation, the kinematic equation for geometrical compatibility between the displacement and strain in a given coordinate system, and the equation for a mechanical equilibrium between the internal and external force. For the spherical shell under the stress condition, these equations are given as follows:

The constitutive equations for the total deformation are
$$
\varepsilon_{\mathrm{r}}=\varepsilon_{\mathrm{r}}^{\mathrm{E}}+\varepsilon_{\mathrm{r}}^{\mathrm{c}}+\varepsilon_{\mathrm{r}}^{\mathrm{sw}}+\varepsilon_{\mathrm{r}}^{\mathrm{th}}=\frac{1}{\mathrm{E}}\left[\sigma_{\mathrm{r}}-2 v \sigma_{\theta}\right]+\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[\sigma_{\mathrm{r}}-2 \mu \sigma_{\theta}\right] \mathrm{d} \tau+\mathrm{S}_{\mathrm{r}}+\eta_{\mathrm{r}}+\beta_{\mathrm{r}} \tag{1}
$$

$$
\varepsilon_{\theta}=\varepsilon_{\theta}^{\mathrm{E}}+\varepsilon_{\theta}^{\mathrm{c}}+\varepsilon_{\theta}^{\mathrm{sw}}+\varepsilon_{\theta}^{\mathrm{th}}=\frac{1}{\mathrm{E}}\left[(1-v) \sigma_{\theta}-v \sigma_{\mathrm{r}}\right]+\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \sigma_{\theta}-\mu \sigma_{\mathrm{r}}\right] \mathrm{d} \tau+\mathrm{S}_{\theta}+\eta_{\theta}+\beta_{\theta} \tag{2}
$$

The kinematic equations for geometrical compatibility in spherical coordinates are
$$
\varepsilon_{\mathrm{r}}=\frac{\partial \mathrm{u}}{\partial \mathrm{r}} \tag{3}
$$

$$
\varepsilon_{\theta}=\frac{\mathrm{u}}{\mathrm{r}} \tag{4}
$$

The equation of the mechanical equilibrium is
$$
\frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}-\frac{2}{\mathrm{r}}\left(\sigma_{\theta}-\sigma_{\mathrm{r}}\right)=0 \tag{5}
$$

where $\varepsilon$ is the strain, $\sigma$ is the stress in MPa, E is the Young modulus in MPa, $v$ is the Poisson ratio, t is the irradiation time in sec, $\mathrm{A}_{\mathrm{c}}$ is the creep rate constant in $\text{cm}^3/\text{MPa}$, $\dot{\mathrm{f}}$ is the fission rate in $\text{fission/cm}^3\text{-sec}$, $\mu$ is the Poisson ratio affected by creep deformation, $\tau$ is the arbitrary time during increment in sec, $\mathrm{S}$ is the strain by fission-induced swelling, $\eta$ is the strain by thermal expansion, and $\beta$ is the strain induced by the formation of the interaction layer by chemical interaction between UMo and Al. The subscripts r and $\theta$ stand for the radial and circumferential direction, respectively.

By rearranging Eq. (2) together with Eq. (4), we obtain the relation


$$
\frac{\mathrm{u}}{\mathrm{r}}=\frac{1}{\mathrm{E}}\left[(1-v) \sigma_{\theta}-v \sigma_{\mathrm{r}}\right]+\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \sigma_{\theta}-\mu \sigma_{\mathrm{r}}\right] \mathrm{d} \tau+\mathrm{S}_{\theta}+\eta_{\theta}+\beta_{\theta}
\tag{6}
$$

Rearranging Eq. (6) yields a 2nd-order differential equation of $\sigma_{\mathrm{r}}$ as follows:

$$
2 \mathrm{r} \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}+\frac{\mathrm{r}^{2}}{2} \frac{\partial^{2} \sigma_{\mathrm{r}}}{\partial \mathrm{r}^{2}}+\frac{\mathrm{E}}{1-v} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}(1-\mu) \Phi_{\mathrm{r}} \mathrm{d} \tau=\frac{\mathrm{E}}{1-v}(\Delta \mathrm{S}+\Delta \eta+\Delta \beta)
\tag{7}
$$

where

$$
\Phi_{\mathrm{r}}=2 \mathrm{r} \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}+\frac{\mathrm{r}^{2}}{2} \frac{\partial^{2} \sigma_{\mathrm{r}}}{\partial \mathrm{r}^{2}}
\tag{8}
$$

and $\Delta$ denotes the difference in quantities for the r-direction and $\theta$-direction (e.g., $\Delta \mathrm{S}=\mathrm{S}_{\mathrm{r}}-\mathrm{S}_{\theta}$).

The solution with respect to $\sigma_{\mathrm{r}}$ can be obtained solving Eq. (7) and that with respect to $\sigma_{\theta}$ can be obtained using Eq. (5) as follows:

$$
\sigma_{\mathrm{r}}=\mathrm{C}_{1}+\frac{\mathrm{C}_{2}}{\mathrm{r}^{3}}+\frac{2}{3} \mathrm{f}(\mathrm{t}) \cdot \ln (\mathrm{r})
\tag{9}
$$

$$
\sigma_{\theta}=\mathrm{C}_{1}-\frac{1}{2} \frac{\mathrm{C}_{2}}{\mathrm{r}^{3}}+\frac{1}{3} \mathrm{f}(\mathrm{t})[2 \ln (\mathrm{r})+1]
\tag{10}
$$

where $\mathrm{C}_{1}$ and $\mathrm{C}_{2}$ are integral coefficients. It should be noted that Eqs. (9) and (10) are employed to calculate the radial or circumferential stress in each region of fuel meat constituents as a function of radial coordinate and irradiation time. The detailed derivation procedure to obtain the solutions is given in Appendix A.

The coefficients $\mathrm{C}_{1}$ and $\mathrm{C}_{2}$ are determined using the boundary condition and interfacial condition, as shown in Fig. 2. It should be noted that the fission gas bubble pressure $(\mathrm{P}_{\mathrm{i}})$ and hydrostatic stress exerted outside the composite $(\sigma_{\mathrm{h}})$ are negative when they are compressive. Details for boundary and interfacial conditions and explicit forms of the integral coefficients in Eqs. (9) and (10) are summarized in Appendix B.

![](./images/812715688320827392_4.jpg)

Fig. 2 Schematic illustration showing boundary and interfacial conditions for UMo/IL/Al spherical model.

In the coefficients, only two interfacial stresses $(\Pi_{1}$ and $\Pi_{2})$ are unknown. In order to obtain them, two interfacial conditions are required; radial displacement at UMo/IL and the IL/Al matrix must be identical. Hence, the following can be written:

$$
\begin{aligned}
& \mathrm{u}_{\mathrm{f}}\left(\mathrm{r}_{\mathrm{f}}\right)=\mathrm{u}_{\mathrm{IL}}\left(\mathrm{r}_{\mathrm{f}}\right) \\
& \mathrm{u}_{\mathrm{IL}}\left(\mathrm{r}_{\mathrm{IL}}\right)=\mathrm{u}_{\mathrm{Al}}\left(\mathrm{r}_{\mathrm{IL}}\right)
\end{aligned}
\tag{11}
$$

For instance, the condition in Eq. (11) combining with Eq. (6) at UMo/IL to obtain $\Pi_{1}$ is fully expressed by the following equation:

$$
\begin{aligned}
& \frac{\mathrm{r}_{\mathrm{f}}}{\mathrm{E}_{\mathrm{f}}}\left[\left(1-\mathrm{v}_{\mathrm{f}}\right) \sigma_{0}^{\mathrm{f}}\left(\mathrm{r}_{\mathrm{f}}\right)-\mathrm{v}_{\mathrm{f}} \Pi_{1}\right]+\mathrm{r}_{\mathrm{f}} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}}^{\mathrm{f}} \dot{\mathrm{f}}_{\mathrm{f}}\left[\left(1-\mu_{\mathrm{f}}\right) \sigma_{0}^{\mathrm{f}}\left(\mathrm{r}_{\mathrm{f}}\right)-\mu_{\mathrm{f}} \Pi_{1}\right] \mathrm{d} \tau+\mathrm{r}_{\mathrm{f}}\left(\mathrm{S}_{0}^{\mathrm{f}}+\eta_{0}^{\mathrm{f}}+\beta_{0}^{\mathrm{f}}\right) \\
& =\frac{\mathrm{r}_{\mathrm{f}}}{\mathrm{E}_{\mathrm{IL}}}\left[\left(1-\mathrm{v}_{\mathrm{IL}}\right) \sigma_{0}^{\mathrm{IL}}\left(\mathrm{r}_{\mathrm{f}}\right)-\mathrm{v}_{\mathrm{IL}} \Pi_{1}\right]+\mathrm{r}_{\mathrm{f}} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}}^{\mathrm{IL}} \dot{\mathrm{f}}_{\mathrm{IL}}\left[\left(1-\mu_{\mathrm{IL}}\right) \sigma_{0}^{\mathrm{IL}}\left(\mathrm{r}_{\mathrm{f}}\right)-\mu_{\mathrm{IL}} \Pi_{1}\right] \mathrm{d} \tau+\mathrm{r}_{\mathrm{f}}\left(\mathrm{S}_{0}^{\mathrm{IL}}+\eta_{0}^{\mathrm{IL}}+\beta_{0}^{\mathrm{IL}}\right)
\end{aligned}
\tag{12}
$$

The same calculation was performed to obtain $\Pi_{2}$ for the interfacial condition at IL/Al. Consequently, $\Pi_{1}$ and $\Pi_{2}$ are given as a function of the known quantities including radial coordinates, material properties, and boundary conditions as $P_{i}(t)$ and $\sigma_{h}(t)$. By using the obtained $\Pi_{1}$ and $\Pi_{2}$, and the updated radial coordinates, radial and circumferential stresses and strains can be newly updated. A repetition of the above calculation in order to simultaneously update the radial coordinate and stress component is required.

### 2.3. Pressurization by internal fission gas bubble

Fission gases are generated by U-235 atom fission during irradiation. The fission gases, Xe and Kr, are insoluble in the UMo, and form gas bubbles inside the UMo fuel particle as shown in Fig. 3(a). It is known that fission gas bubbles are preferably nucleated in the UMo grain boundaries due to their low surface energy [19][20] (see Fig. 3(b)). Beyond the range of the grain size of around 7 μm,

therefore, fission gas bubbles are uniformly distributed in the UMo particle, by which it is possible to assume that the UMo is divided into polyhedral cells, each containing a gas bubble at the center. Each cell is then approximated by an equivalent spherical cell of equal volume. Using these approximations, a unit cell can be assumed, which is composed of two hypothetical spheres, as shown in Fig. 3(c); the inner sphere is for the fission gas bubble, and the outer one is equivalent to UMo fuel particle. Under these circumstances, the bubble pressure inside the equivalent UMo fuel grain is equal to that inside a UMo particle for the hypothetical fission gas bubble with the radius of $r_{i}$ , as illustrated in Fig. 3(d). The same method to approximate the pressure due to fission gas bubbles can be found elsewhere [21].

Fission gas pressure inside the fission gas bubble (or the innermost sphere in the model) is under mechanical equilibrium with the elasticity and creep resistance of the outer UMo sphere. This allows us to establish the mathematical equations to access the thermoelastic deformation and creep of the system composed of an internally pressurized thick-walled sphere (see Fig. 3(d)).

![](./images/812715688320827392_5.jpg)

Fig. 3 Schematics of the hypothetical composite sphere containing a fission gas bubble in the UMo.

The fraction of fission gas volume ( $x_{g}$ ) is defined as:
$$
\mathrm{x}_{\mathrm{g}}=\frac{\frac{4}{3} \pi \mathrm{r}_{\mathrm{i}}^{3}}{\mathrm{~V}_{\mathrm{f}}} \tag{13}
$$
where $r_{i}$ is the fission gas bubble radius. The solid UMo volume ( $V_{f}$ ), increasing as burnup increases, is expressed by
$$
\mathrm{V}_{\mathrm{f}}=\frac{4}{3} \pi\left(\mathrm{r}_{\mathrm{f}}^{3}-\mathrm{r}_{\mathrm{i}}^{3}\right) \tag{14}
$$

Combining Eqs. (13) and (14) yields the following equation, which obtains the radius of the fission gas bubble while satisfying the volume fraction of the fission gas bubble in solid UMo as

$$
\mathrm{r}_{\mathrm{i}}^{3}=\mathrm{r}_{\mathrm{f}}^{3} \frac{\mathrm{x}_{\mathrm{g}}}{\mathrm{x}_{\mathrm{g}}+1}
\tag{15}
$$

By using the ideal gas law, the fission gas pressure can be expressed by

$$
\mathrm{P}_{\mathrm{i}}=\frac{\mathrm{kY}_{\mathrm{fg}} \mathrm{F}_{\mathrm{d}} \mathrm{T}_{\mathrm{f}}}{\mathrm{x}_{\mathrm{g}}}
\tag{16}
$$

where k is the Boltzmann constant, $Y_{fg}$ is the sum of fission gas yields, $F_d$ is the fission density, and $T_f$ is the fuel temperature. It should be noted that $P_i$ is the effective bubble pressure, equivalent to the bubble pressure in the UMo grain.

Combining the volume fraction of the fission gas bubble and the size of UMo particle gives the size of the hypothetical bubble ( $r_i$ ). The calculated bubble size satisfies the volume ratio between solid UMo and gaseous fission products, which is given by the correlation for the swelling resulting from gaseous fission products. In addition, the UMo volume increases by solid fission product swelling which affects the solid UMo volume. Both types of swelling, i.e., UMo swelling caused by solid fission products and the fission gas bubbles, are defined respectively as follows:

$$
\mathrm{x}_{\mathrm{s}}=\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{\mathrm{f}}}\right)_{\mathrm{s}}
\tag{17}
$$

$$
\mathrm{x}_{\mathrm{g}}=\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{\mathrm{f}}}\right)_{\mathrm{g}}
\tag{18}
$$

The correlations used for the model were developed by Kim et al. [22] and are given in the Appendix C.

### 2.4. Pressure outside the composite sphere
In the conventional modeling method to calculate the stresses in nuclear fuel by solving the equation of mechanical equilibrium, the boundary condition at the outermost surface of the domain is given by a prescribed displacement or the coolant pressure. For simplicity, this prescribed pressure is assumed to be equal to the coolant pressure or even zero because its effect on the mechanical state of the single solid medium is negligible compared to other factors including the surface energy or thermal expansion at high temperatures (e.g., the intergranular fission gas bubble in $UO_2$ [23][24], the intragranular fission gas bubble in UMo [25] or pores in the Al matrix [26]). However, in the case of the UMo/Al dispersion fuel in which the size of the UMo particle is larger than the average distance between two neighboring particles, it is believed that the hydrostatic stress exerted on the outside of the UMo/IL/Al composite sphere, shown in Fig. 3(d), is affected by the microstructural changes of the medium surrounding the composite cell. More specifically, the local mechanical state of each cell is largely affected by the temperature gradient and the interaction between the neighboring particles due to the mass relocation caused by fission-induced creep. In order to take account of this particle-particle interaction, the calculation scheme implemented in PRIME (PRedIction code for thermo-MEchanical performance of research reactor fuel) computational program was used to compute the hydrostatic stress outside the composite sphere in order to obtain the local boundary condition [18].

In the scheme, the fuel meat is treated as a homogenized medium by using an effective-medium approximation, as shown in Fig. 4, and mechanical responses are calculated by FEM with an incremental solution combined with an effective-stress function (ESF) algorithm to solve the thermo-elastic-plastic and creep problem (see [27] and references therein for details).

![](./images/812715688320827392_6.jpg)

Fig. 4 A schematic showing finite element for the homogenized fuel meat used.

The stress distribution is obtained from the stress tensor calculated in the homogenized fuel meat. The hydrostatic stress on the outermost surface of the UMo/IL/Al composite ($\sigma_{\mathrm{h}}$), which is calculated using normal stress components in the stress tensor, at the integration point is given as follows:

$$
\sigma_{\mathrm{h}}=\frac{1}{3} \sum \sigma_{\mathrm{ii}} \quad(\mathrm{i}=1,2,3) \tag{19}
$$

where $\sigma_{\mathrm{ii}}$ is the diagonal stress component in the stress tensor matrix. Among the nine integration points used in the full integration, the hydrostatic stress obtained from the integration point located at the center of the element is used as a nominal value for the boundary condition in the analytical model.

### 2.5. Calculation procedure
In the previous section, the components required to calculate displacements (u) were obtained. The coefficients used in the equations for stresses and displacement contain known radial coordinates and unknown interfacial stresses. The next step is to calculate the unknown interfacial stresses. Once they are obtained, the radial coordinates can be updated, and sequentially all stresses in Eqs. (9) and (10) can be updated also. Numerical iteration follows to obtain converged radial coordinates and stress components. The calculation steps to obtain the displacements are as follows:

1) Set the time interval $\Delta \mathrm{t}$.

2) Calculate fission density using the given fission rate and time interval.

3) Calculate $\mathrm{S}, \eta$ and $\beta$ using the fission-induced swelling model, interaction layer growth model and coefficient of thermal expansion of fuel meat constituents.

4) Calculate fission gas bubble pressure $(\mathrm{P}_{\mathrm{i}})$ by Eq. (16) and the size of the effective fission

gas bubble $(r_{i})$ in the UMo particle by Eq. (15).

5) Repeat the iteration until the calculated displacement is converged.

- Arrange the expressions of $\sigma_{r}$ and $\sigma_{\theta}$ for each region (i.e., UMo fuel, IL, and Al) using Eqs. (9) and (10) using the pressure at the boundary and interface.
- Calculate the interfacial stresses, $\Pi_{1}$ and $\Pi_{2}$ using the continuity of displacement at the UMo/IL and IL/Al interfaces.
- Update the coefficients of the stress functions in each region.
- Calculate $\varepsilon_{r}$ and $\varepsilon_{\theta}$ using $\sigma_{r}$ and $\sigma_{\theta}$ which are defined by Eqs. (1) and (2).
- Calculate displacement u(r) using Eq. (4).
- Update the radial coordinates for all interfaces and the surface, i.e., UMo/IL, IL/Al, and Al matrix.
- Check for a convergence of the radial coordinates with calculated displacements at the interfaces. For the iteration index (k), the convergence criterion for the interfacial displacement is given as follows:

$$
\frac{\Delta \mathrm{u}_{\mathrm{j}}^{(\mathrm{k})}}{\mathrm{u}_{\mathrm{j}}^{(\mathrm{k})}} \leq 10^{-4} \tag{20}
$$

where $\mathrm{u}_{\mathrm{j}}^{(\mathrm{k})}$ is the displacement at (k)-th iteration, $\Delta \mathrm{u}_{\mathrm{j}}^{(\mathrm{k})}$ is the displacement increment at the j-interface (e.g., j = UMo/IL, IL/Al).

6) Proceed to the next time step with the updated radial coordinates.

## 3. Irradiation models and material properties

### 3.1. Fission-induced swelling and creep

- **Swelling strain of UMo fuel and IL**

The fuel swelling of UMo alloy was correlated as a function of fission density using a model by Kim et al. [28]. The fuel swelling correlation predicts the total fuel swelling induced by the accumulation of both solid and gaseous fission products inside UMo.

Fission-induced swelling in the IL is assumed to be the same as that of $UAl_{4}$, which can be justified because of the low concentration of Mo in the UMo that does not significantly alter the fission induced swelling of $UAl_{4}$ [29]. The details of all correlations are summarized in Appendix C.

Because the swelling is isotropic, the swelling strain of fissile materials is calculated and expressed by

$$
\mathrm{S}_{\mathrm{j}, \mathrm{i}}=\frac{1}{3} \ln \left[1+\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{i}}^{\mathrm{s}}\right](\mathrm{j}=\mathrm{r}, \theta) \tag{21}
$$

where $\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{i}}^{\mathrm{s}}$ is the total fission-induced swelling, the subscript i stands for the fissile containing material index (i.e., UMo or IL) and the subscript j denotes the radial or circumferential direction. In the Al matrix region, the swelling strain is zero.

- Fission induced creep strain

An equation for fission-induced creep strain, independent on temperature, is given as follows [10]:

$$
\overline{\varepsilon}^{\mathrm{c}}=\mathrm{A}_{\mathrm{c}} \int \overline{\boldsymbol{\sigma}} \cdot \dot{\mathrm{f}} \mathrm{dt} \tag{22}
$$

where $\overline{\varepsilon}^{\mathrm{c}}$ and $\overline{\boldsymbol{\sigma}}$ are the effective strain and stress, respectively. In the isotropic spherical shell, the effective stress is calculated by the following equation:

$$
\overline{\boldsymbol{\sigma}}=\sigma_{\mathrm{r}}-\sigma_{\theta} \tag{23}
$$

To obtain time integration of effective creep strain in Eq. (22), the explicit Euler method was used with respect to the time increment of $\Delta \mathrm{t}$ and stress components available at time t.

### 3.2. Interaction layer growth and strain by chemical expansion

The calculation of IL growth and the conversion of IL thickness to IL volume is performed using the correlations available in [30]. The correlations are given by Eqs (C8) – (C11) in Appendix C. It should be noted that IL volume is calculated as a function of IL thickness under the condition where uniform-sized UMo fuel particles are regularly distributed in the Al matrix. The consumed volumes of the UMo and Al matrix were calculated based on the mass balance; the consumed UMo fuel mass is equal to the UMo fuel mass in the newly formed IL. For the Al matrix, the same principle is employed.

Similar to the definition of the swelling strain, the strains due to the volume change associated with the IL formation is given by

$$
\beta_{\mathrm{j}, \mathrm{i}}=\frac{1}{3} \ln \left[1+\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{i}}^{\mathrm{c}}\right](\mathrm{j}=\mathrm{r}, \theta) \tag{24}
$$

where $\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{i}}^{\mathrm{c}}$ is the volume expansion associated with the IL formation. For the UMo and Al matrix, $\beta$ becomes negative due to the consumption by IL growth, while that for IL is always positive. $\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{i}}^{\mathrm{c}}$ for each region is summarized in Appendix C.

### 3.3. Thermal expansion

The thermal strain for each region is calculated using the coefficient of thermal expansion, which is expressed as the following equation:

$$\eta_{\mathrm{i}}=\alpha_{\mathrm{m}, \mathrm{i}}\left(\mathrm{T}-\mathrm{T}_{\text {ref }}\right) \tag{25}$$

where $\alpha_{\mathrm{m}, \mathrm{i}}$ is the coefficient of the linear thermal expansion, $\mathrm{T}$ is the temperature in $\mathrm{K}$, and $\mathrm{T}_{\text {ref }}$ is the reference temperature, which is typically $298 \mathrm{~K}$.

### 3.4. Material properties

The physical and mechanical properties for each material used in the calculation are summarized in Table 1. Because the properties of IL are not available, the $\mathrm{UAl}_{4}$ properties are used [31][32]. The theoretical IL density is derived considering the Mo atom substitution on the $\mathrm{U}$ lattice in the $\mathrm{UAl}_{4}$ crystal structure.

Material properties for UMo and IL, such as Young's modulus and Poisson's ratios, are assumed to be constant throughout irradiation. For the Al matrix, temperature-dependent mechanical properties are used. The Poisson ratio of the Al matrix under creep deformation is assumed to be 0.5 because the creep strain was expected to be predominant, which enhanced the incompressibility of Al [33]. The value was also used in order to take account of irradiation-induced stiffening of Al [34]. Those mechanical properties are currently presumed to be constant during analysis, but they could be treated as time-varying ones if necessary.

Table 1 Summary of material properties for each material.

<table>
<thead>
<tr>
<th></th>
<th>UMo</th>
<th>IL</th>
<th>Al matrix</th>
</tr>
<tr>
<th>Physical property</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Density (g/cm³)</td>
<td>17.1 (U-10Mo)<br>17.3 (U-7Mo)</td>
<td>6.10</td>
<td>$2.7(1+\overline{\boldsymbol{\alpha}} \cdot \Delta \mathrm{T})^{-3}$</td>
</tr>
<tr>
<td>Instantaneous<br>coefficient of linear<br>thermal expansion<br>$(10^{-6})^{*}$</td>
<td>$7.91+1.21 \cdot 10^{-2} \mathrm{~T}$</td>
<td>16.5</td>
<td>$18.1+2.38 \cdot 10^{-2} \mathrm{~T}$<br>$-2.94 \cdot 10^{-5} \mathrm{~T}^{2}+3.03 \cdot 10^{-8} \mathrm{~T}^{3}$</td>
</tr>
<tr>
<td>Mechanical<br>property</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Young's modulus<br>(GPa)</td>
<td>67.7 (U-10Mo)<br>50.6 (U-7Mo)</td>
<td>134</td>
<td>$70.3 \cdot\left[1.0-4.8 \cdot 10^{-4}(\mathrm{~T}-293)\right]$</td>
</tr>
<tr>
<td>Poisson's ratio (ν)</td>
<td>0.34</td>
<td>0.241</td>
<td>0.33</td>
</tr>
<tr>
<td>Poisson's ratio under<br>creep (μ)</td>
<td>0.34</td>
<td>0.241</td>
<td>0.5</td>
</tr>
<tr>
<td>Creep rate constant<br>$(10^{-25}\ \mathrm{cm}^{3}/\mathrm{MPa})$</td>
<td>500</td>
<td>400</td>
<td>50</td>
</tr>
<tr>
<td>Ref.</td>
<td colspan="3">[18]</td>
</tr>
</tbody>
</table>

* Temperature (T) is in K, and $\overline{\boldsymbol{\alpha}}$ is the mean coefficient of linear thermal expansion.

## 4. Verification of the model against Abaqus simulation

### 4.1. Sample plate data

The combination of the analytical stress analysis model with the homogenized-meat FEM model discussed earlier (denoted as the "hybrid model" hereafter) was verified against the Abaqus simulation that uses a heterogeneous meat model ("Abaqus model" hereafter) using the PIE data of two plates that showed distinctively different irradiation behavior. The plate V6022M has a pure Al matrix, while the plate R3R108 has a Si-modified Al matrix. V6022M exhibited high IL growth that made the IL the continuous phase, whereas R3R108 showed drastically lower IL growth, leaving the Al matrix as the continuous phase at EOL. Fig. 5 compares the cross-section images of the two plates. The most remarkable microstructural difference between these two plates may be the presence of large pores in V6022M, whereas R3R108 shows only localized cracks in the Al matrix between locations A and B in Fig. 5(b). These cracks in R3R108 are due to the lack of creep in the continuous-phase of Al matrix. Hence, the Al matrix was fractured by the stress due to UMo particle swelling.

![](./images/812715688320827392_7.jpg)

Fig. 5 Optical microscopic images of (a) V6022M and (b) R3R108. The arrows mark three locations where stress calculations were made for benchmarking.

### 4.2. Model calculation

In order to verify our model, a different set of solutions from the hybrid model was compared to the

results that were obtained using the Abaqus model, as represented in Fig. 6. The solutions include UMo fuel particle deformation, radial and circumferential stress distribution at different irradiation time, and IL/Al interfacial stress as a function of fission density. It should be noted that two different finite element models were used: One is a three-dimensional single UMo/IL/Al composite sphere, and the other is two-dimensional heterogeneous fuel meat. They were employed to compare numerical solutions from Abaqus with those obtained using the hybrid model, as shown in Fig. 7 and Fig. 8. The former was used to verify the analytical results for the radial displacement of the UMo particle and stress distributions, while the latter was used to validate whether it can be alternatively employed to assess the local stress distribution in the hybrid model instead of using the Abaqus heterogeneous meat model. Particularly, special attention was given to the state of stress at the IL/Al interface where the large pores are formed.

![](./images/812715688320827392_8.jpg)

Fig. 6 Summary of model calculation schemes for solution comparison between the hybrid model and Abaqus model.

The radial displacement of the UMo particle and stress distributions in both radial and circumferential directions were calculated using the hybrid and Abaqus model where the finite mesh of the single spherical composite was used (see Fig. 7).

For the Abaqus model to calculate the stress at the IL/Al interface, finite element analysis was performed using a generalized plane strain condition in the length direction. The mesh configurations for the Abaqus model are represented in Fig. 8. In the Abaqus model, IL growth was modeled by providing additional meshes around the UMo. Implementation of IL growth was dealt with using the prescribed field variable. The details of how to deal with IL growth in FEA have been documented elsewhere [12][13]. In the hybrid model, the IL growth was implemented through correlation to compute the time-dependent IL thickness as well as its volume fraction.

![](./images/812715688320827392_9.jpg)

Fig. 7 Finite meshes for Abaqus model to calculate the deformation of UMo fuel particle and stress distribution in the composite.

![](./images/812715688320827392_10.jpg)

Fig. 8 Finite meshes for Abaqus models implementing microstructural evolution by IL growth for (a) V6022M and (b) R3R108.

The life-averaged fission rate and temperature are used for simple verification. The fabrication and irradiation data are summarized in Table 2. The transversal power peaking distribution is considered in both calculations to consider the effect of burnup and microstructural evolution.

Table 2 Summary of input parameters of fabrication and irradiation data for two dispersion fuel plates.

<table>
  <tbody>
    <tr>
      <td>Plate ID</td>
      <td colspan="2">V6022M</td>
      <td colspan="2">R3R108</td>
    </tr>
    <tr>
      <td>Fuel meat composition</td>
      <td colspan="2">U-10Mo/Al</td>
      <td colspan="2">U-7Mo/Al-5Si</td>
    </tr>
    <tr>
      <td>U-loading (gU/cm³)</td>
      <td colspan="2">6</td>
      <td colspan="2">8</td>
    </tr>
    <tr>
      <td>Irradiation time (EFPD)</td>
      <td colspan="2">257</td>
      <td colspan="2">98</td>
    </tr>
    <tr>
      <td>UMo fuel particle size (µm)</td>
      <td colspan="2">50</td>
      <td colspan="2">50</td>
    </tr>
    <tr>
      <td>Initial IL thickness (µm)</td>
      <td colspan="4">0.5</td>
    </tr>
    <tr>
      <td>Location index</td>
      <td colspan="4">Fission density at EOL† (10²¹ fission /cm³-UMo)
and temperature* (□)</td>
    </tr>
    <tr>
      <td>A</td>
      <td>5.91</td>
      <td>134</td>
      <td>5.30</td>
      <td>274</td>
    </tr>
    <tr>
      <td>B</td>
      <td>5.68</td>
      <td>139</td>
      <td>4.78</td>
      <td>264</td>
    </tr>
    <tr>
      <td>C</td>
      <td>5.43</td>
      <td>139</td>
      <td>4.16</td>
      <td>244</td>
    </tr>
    <tr>
      <td>Ref.</td>
      <td colspan="4">†Fission density from [8].
*Temperature calculated in the present study.</td>
    </tr>
  </tbody>
</table>

The hydrostatic stress ($\sigma_{\mathrm{h}}$) used for the boundary condition in the hybrid model was obtained using the homogeneous meat FEA, as shown in Fig. 9. It is noticeable that $\sigma_{\mathrm{h}}$ turned out to be tensile at locations B and C in V6022M where the large pores were observed. Those stress calculation results using the EMA for the fuel meat were verified in the previous study reported in [18]. It is believed that the tensile stress in the thickness direction is formed by the combination of fission-induced fuel swelling and meat mass relocation due to fission-induced creep.

In contrast to V6022M, no tensile stresses were predicted for R3R108 at any locations during irradiation, implying that the stress state was unfavorable for pore growth. The major cause for this difference is due to the low IL growth in R3R108. Since the Al matrix has a much lower creep rate than the IL, the long-distance propagation of stress generated by fission-induced swelling was restricted. Instead, the local stress was relaxed by tearing the Al matrix, as discussed earlier.

![](./images/812715688320827392_11.jpg)

(a) V6022M

![](./images/812715688320827392_12.jpg)

(b) R3R108

Fig. 9 Pressure exerted on the outermost sphere of the hypothetical composite sphere (shown in Fig. 3). A, B, and C are the location marked in Fig. 5.

### 4.3. Comparison with Abaqus model

#### 4.3.1. UMo fuel particle deformation

The deformation of a UMo fuel particle was estimated and compared between the two models. The finite element of the single sphere composite was used in the Abaqus model to compare the mechanical response of the simple single composite. This comparison was also examined the calculated strain components related to volumetric expansion, consumption by chemical reaction of IL growth, and creep deformation. The deformation of the UMo fuel particle was estimated in terms of the change of radius of the particles, which was calculated using radial displacement as shown in Fig. 10.

![](./images/812715688320827392_13.jpg)

Fig. 10 Evolution of strain components calculated for each sample during finite element analysis and comparison of estimation for deformation of UMo fuel particle by Abaqus and hybrid model.

The radial displacement that is determined by the radial coordinate and total circumferential strain described in Eq. (4) was evaluated to be negative in both plate samples. It was found that the UMo fuel particle underwent shrinkage due to IL growth in the earlier stages of life but expanded later

when fission gas bubble swelling accelerated, although strain by fuel swelling did also exist in earlier stages. The transition of changes in the UMo fuel particle size from shrinkage to expansion found in the case of V6022M, since the swelling strain outweighed the strain causing volume shrinkage due to IL growth.

Changes in stresses in the radial and circumferential direction were plotted as a function of the fission density, as shown in Fig. 11, to analyze the mechanical behavior of the composite during irradiation. The radial stresses on the UMo fuel particle surface in both plates showed a transition from the compressive to tensile, which indicated that the UMo fuel particle underwent radial thinning (negative strain) by internal pressurization due to fission gas and compressive pressure from the composite outside at BOL. However, radial thickening (positive strain) occurred as the fission density increased due to fission-induced swelling. Those transitions were found in both the UMo and IL regions. It implies that changes in the radial coordinate at the UMo/IL interface were determined by the compatibly established mechanical states of two regions. It should be noted that circumferential strains and stresses were not equal, in contrast to the radial components.

With regards to the V6022M sample, the radial displacement of the UMo/IL interface was affected by the greater negative stress and strain in the IL region with higher volumetric expansion strains caused by extensive IL growth, compared to those in the UMo; the more negative circumferential strain (circumferential shortening) in the IL indicates that IL growth occurred in the inner radial direction due to the consumption of the UMo.

On the other hand, for the R3R108 sample, circumferential shortening of the UMo region at the UMo/IL interface was also found, but the underlying mechanical behavior was different. The circumferential shortening of the UMo fuel particle was smaller due to the suppression of IL growth. However, due to the difference in thermal strain between the UMo and IL (i.e., $\beta_{\mathrm{IL}}>\beta_{\mathrm{UMo}}$), compressive stress occurred in the IL region, while the UMo underwent tensile stress. UMo's higher creep rate constant, compared to that of IL, led to stress relief in the UMo region, causing the radial displacement at the UMo/IL interface to be governed by the change in the circumferential strain of the IL region.

![](./images/812715688320827392_14.jpg)

![](./images/812715688320827392_15.jpg)

Fig. 11 Changes of stresses and corresponding tangential creep strain as a function of fission density.

Hence, it was confirmed that the hybrid model gives reliable calculation results by comparing the estimation for the UMo fuel kernel size as a function of fission density. These estimations showed that the hybrid model has the capability to predict volume changes in UMo fuel particles.

### 4.3.2. Radial and circumferential stresses

The radial and circumferential stresses were calculated using the hybrid model and compared to the Abaqus results. The changes of stress components during irradiation were calculated at three different irradiation times (see Table 3 and Table 4). The radial stress was of interest because it can be used as the state of stress at the interface between composite constituents. Also, the circumferential stress is one of the determinants when computing the radial displacement of the interfaces, which is derived using Eq. (6). Because the value of Poisson's ratio used in both hybrid and Abaqus models is smaller than 0.5, it is expected that the circumferential stress is more influential than the radial stress in determining the radial displacement.

In the Abaqus model, the calculated stresses were obtained at the integration point that was not exactly on the element surface. It should be noted that the radial stress derived in the hybrid model was affected by the radial coordinate, meaning a discrepancy in the calculated radial stress between the models is unavoidable. Contrarily, the good agreement was found in the comparison for the circumferential stresses which did not change significantly through the thickness of a given layer. These acceptable differences in the circumferential stresses indicate that the radial stresses were also calculated quite precisely by the models.

Table 3 Comparison of calculated stresses for V6022M with Abaqus at different irradiation time.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">UMo/IL interface</th>
<th colspan="2">IL/Al interface</th>
<th colspan="2">Outermost surface</th>
</tr>
<tr>
<th>Hybrid</th>
<th>Abaqus</th>
<th>Hybrid</th>
<th>Abaqus</th>
<th>Hybrid</th>
<th>Abaqus</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="7">At BOL (10 EFPD)</th>
</tr>
<tr>
<th>Radial stress (MPa)</th>
<td>-7.78</td>
<td>-7.58</td>
<td>-7.57</td>
<td>-7.47</td>
<td>-2.53</td>
<td>-2.72</td>
</tr>
<tr>
<th>Circumferential stress (MPa)</th>
<td>-8.20</td>
<td>-8.24</td>
<td>-34.8</td>
<td>-33.1</td>
<td>-2.21</td>
<td>-2.22</td>
</tr>
<tr>
<th colspan="7">At MOL (127 EFPD)</th>
</tr>
<tr>
<th>Radial stress (MPa)</th>
<td>9.72</td>
<td>9.53</td>
<td>9.63</td>
<td>9.71</td>
<td>-2.77</td>
<td>-2.85</td>
</tr>
<tr>
<th>Circumferential stress (MPa)</th>
<td>4.55</td>
<td>4.54</td>
<td>2.37</td>
<td>2.33</td>
<td>-3.54</td>
<td>-3.64</td>
</tr>
<tr>
<th colspan="7">At EOL (257 EFPD)</th>
</tr>
<tr>
<th>Radial stress (MPa)</th>
<td>15.0</td>
<td>13.2</td>
<td>14.9</td>
<td>14.7</td>
<td>67.9</td>
<td>65.6</td>
</tr>
<tr>
<th>Circumferential stress (MPa)</th>
<td>7.73</td>
<td>7.66</td>
<td>6.60</td>
<td>6.53</td>
<td>71.2</td>
<td>71.8</td>
</tr>
</tbody>
</table>

Table 4 Comparison of calculated stresses for R3R108 with Abaqus at different irradiation time.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">UMo/IL interface</th>
<th colspan="2">IL/Al interface</th>
<th colspan="2">Outermost surface</th>
</tr>
<tr>
<th>Hybrid</th>
<th>Abaqus</th>
<th>Hybrid</th>
<th>Abaqus</th>
<th>Hybrid</th>
<th>Abaqus</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="7">At BOL (10 EFPD)</th>
</tr>
<tr>
<th>Radial stress (MPa)</th>
<td>-0.72</td>
<td>-0.73</td>
<td>-1.07</td>
<td>-1.08</td>
<td>-2.77</td>
<td>-2.76</td>
</tr>
<tr>
<th>Circumferential stress (MPa)</th>
<td>-1.77</td>
<td>-1.76</td>
<td>-6.91</td>
<td>-6.93</td>
<td>-2.93</td>
<td>-2.99</td>
</tr>
<tr>
<th colspan="7">At MOL (49 EFPD)</th>
</tr>
<tr>
<th>Radial stress (MPa)</th>
<td>7.28</td>
<td>7.19</td>
<td>7.20</td>
<td>7.21</td>
<td>-2.37</td>
<td>-2.47</td>
</tr>
<tr>
<th>Circumferential stress (MPa)</th>
<td>2.64</td>
<td>2.69</td>
<td>-1.17</td>
<td>-1.20</td>
<td>-3.14</td>
<td>-3.35</td>
</tr>
<tr>
<th colspan="7">At EOL (98 EFPD)</th>
</tr>
</tbody>
</table>

<table>
<tr><td>Radial stress (MPa)</td><td>10.6</td><td>10.7</td><td>10.6</td><td>10.62</td><td>-7.14</td><td>-7.24</td></tr>
<tr><td>Circumferential stress (MPa)</td><td>4.34</td><td>4.37</td><td>0.44</td><td>0.48</td><td>-8.57</td><td>-8.66</td></tr>
</table>

### 4.3.3. IL/Al interfacial stress as a function of FD

As described in Eq. (11), the radial stresses in both the IL and Al region should be the same at the radial coordinate which corresponds to the IL/Al interface. The radial stresses at three locations for V6022M and R3R108 were calculated using the hybrid model and compared to the Abaqus model in Fig. 12 and Fig. 13. The results obtained by the hybrid model are in good agreement with the Abaqus model results.

It is believed that the radial stress at the IL/Al interface was affected by $\sigma_{\mathrm{h}}$ which is used to impose the boundary condition at the outer surface of the Al region, particularly at the beginning of life. Also, the radial stress is influenced by the difference in the coefficient of thermal expansion between IL and Al. When the IL/Al interfacial stresses were compressive, they appeared to be more affected by the Al matrix than the IL because of the greater thermal expansion of the Al matrix. This expansion of the Al matrix compressed the inner sphere of the UMo fuel particle and IL shell.

The transition of the interfacial stresses from compressive stress to tensile stress is noticeable. The IL- Al interfacial stress changed consistently with the $\sigma_{\mathrm{h}}$ used in the stress calculation (see Fig. 9), particularly when the positive stress (or tensile in the radial direction) was applied. The establishment of the tensile stress at the IL/Al interface was the result of the combination of the tensile hydrostatic stress outside the composite and the stress from the UMo fuel particle, caused by the accelerated fuel swelling, which was transmitted through the IL that had a higher creep rate than the Al matrix.

It was found that no compressive-to-tensile transition of the radial stress at the IL/Al interface occurred at any location in R3R108. This is attributed to the fact that 1) the extent of thermal expansion of the Al matrix, compared to other constituents, was much larger due to the higher operation temperature in this plate, and 2) $\sigma_{\mathrm{h}}$ at all locations was compressive. The effect of $\sigma_{\mathrm{h}}$ on the magnitude of the radial stress in R3R108 was more significant than that in V6022M since the IL was much thinner for R3R108.

The common observation in all samples was that the absolute magnitude of the stresses was lowest at the plate center (i.e., location C shown in Fig.5). This may be due to the fact that the peak stress generated at the meat end region where the peak burnup occurred was propagated toward the transversal center of the plate where the constraint for the mechanical deformation was the lowest. During the stress propagation, the transition of the radial stress at the IL/Al interface occurred at the neighboring region of a bulge location where the thickness of the plate increased most, as observed at the location B in V6022M.

![](./images/812715688320827392_16.jpg)

(a) location A

![](./images/812715688320827392_17.jpg)

(b) location B

![](./images/812715688320827392_18.jpg)

Fig. 12 Comparison of local stress at IL/Al interface calculated using the hybrid model and Abaqus simulation for V6022M.

![](./images/812715688320827392_19.jpg)

(a) location A

![](./images/812715688320827392_20.jpg)

(b) location B

![](./images/812715688320827392_21.jpg)

Fig. 13 Comparison of local stress at IL/Al interface calculated using the hybrid model and Abaqus simulation for R3R108.

## 5. Discussion
### 5.1. Combination of the analytical model with a FEM using homogenized fuel meat

The hydrostatic stress ($\sigma_{\mathrm{h}}$) exerted on the outermost sphere composed of the Al matrix was calculated using the hybrid model. It should be noted that the stresses were computed using the homogenized-meat FEM model. Deriving a system of multiple materials of infinitesimal size, it is possible to homogenize the microscopically heterogeneous medium to a macroscopically homogeneous medium [35].

The effective-medium approximation (EMA) method was used by homogenizing the UMo/IL/Al dispersion fuel system [35]. In this method, it was presumed that a uniform hydrostatic strain field was imposed on the unit sphere, and the field outside the composite sphere remained unchanged [36].

All stresses in the homogenized fuel meat were calculated by the finite element method, which is currently used in performance analysis codes such as PRIME [18] and MAIA [37]. Among the stresses, normal stress components, which were calculated at the integration points through the Gaussian quadrature [27] in order to obtain $\sigma_{\mathrm{h}}$, were slightly different from those of the Abaqus heterogeneous meat model, as illustrated in Fig. 14. However, it is important to note that the calculated displacements in x- and y-direction, which were computed at the nodal points of the finite elements, were the same for both fuel meat models, as shown in Fig. 15(a) and Fig. 15(b).

![](./images/812715688320827392_22.jpg)

Fig. 14 Configuration of node and integration points in the finite element analysis.

![](./images/812715688320827392_23.jpg)

(a) Displacement along the transversal direction ($u_{xx}$)

![](./images/812715688320827392_24.jpg)

(b) Displacement along the thickness direction ($u_{yy}$)

Fig. 15 Comparison of computation results for the displacement by using the homogenized and heterogeneous medium of fuel meat.

Those results showing the agreement in the calculated displacements of the fuel plate imply that the stress which is computed at the integration point using the nodal displacement can represent the local mechanical states in the heterogeneous fuel meat. This inference can be justifiable in cases when the size of the finite element (i.e., macroscopic characteristic length; L) is considerably larger than the size of the unit cells composing the heterogeneous fuel meat (i.e., microscopic characteristic length; $\ell$). The typical mesh size of homogenized fuel meat is in the range of 300 - 640 $\mu$m, which is larger than the size of a single UMo/IL/Al sphere composite (<60 $\mu$m). Therefore, the stress computed using the homogenized fuel meat model can be used as a boundary condition if the stress state outside of the composite sphere is not affected by the deformation of the composite sphere. However, in the case that the size of UMo fuel particle is comparable to the that of homogenized meat mesh (i.e., $\ell/L$ ~ 1), any governing equations for the homogenized meat cannot be employed and the stress calculation should be performed in the microscopic domain where all meat constituents are independently dealt with.

In the hybrid model, the realistic morphologies found in UMo/Al fuel meat, including fission gas bubble distribution inside UMo, the particle-particle contact and agglomeration or transversal elongation of UMo fuel particles are not considered since they are beyond of the scope in the simplification. Only isotropic quantities were dealt with in the hybrid model, meaning that the phenomena of stress distribution inside the fuel particle or stress concentration at the Al matrix located at in-between particles could not be assessed. However, it has been shown that the hybrid model is still applicable to predict the stress at IL/Al interface, as a function of fission density, that is the essential determinant for pore growth kinetics. The calculation capability could be extended to address the heterogeneous distribution of fission gas bubbles inside the UMo and anisotropic deformation locally occurring in the fuel meat in the future.

### 5.2. Pressurization by fission gas bubble inside UMo
Fission gas bubble pressure is the primary source of the stresses generated in the UMo/Al dispersion fuel together with thermal expansion. Thermal expansion is solely dependent upon temperature and causes only volumetric change, not plastic deformation or creep. However, the pressurization caused by fission gas bubbles inside the UMo fuel, exerted on IL or Al matrix, produces stresses that drive the fuel to experience fission-induced creep.

The gas bubble pressure was calculated, as shown in Fig. 16, using the ideal gas law with the empirical correlation to obtain the volume fraction of gaseous fission products in UMo. Until the burnup reaches the threshold fission density where the fission gas bubble swelling increases parabolically, the bubble pressure is set unchanged since the amount of nano-sized bubbles is linearly proportional to the fission density, as the empirical correlation implies [28]. Beyond the threshold fission density, however, the pressure decreases as the volume of the fission gas bubble increases parabolically. By comparing the pressure between R3R108 and V6022M, higher pressurization is found in R3R108 due to the higher fuel temperature. This pressure-temperature relationship has been commonly demonstrated for other fuel types [38][39].

![](./images/812715688320827392_25.jpg)

Fig. 16 Pressurization of fission gas bubbles inside UMo for each plate as a function of fission density.

It should be noted that the calculated fission gas bubble pressure is the effective quantity required as the boundary condition in the governing equations for the mechanical state. In this study, the bubble pressure likely to be underestimated by the equation for thermo-mechanical equilibrium between the bubble pressure and surface energy of the solid UMo, particularly at the low burnup regime. However, this approach is applicable when estimating the pressure inside mostly submicron-sized fission gas bubbles because the magnitude of the pressure is in agreement with the results calculated by the Ronchi equation of state (EOS) [40]. The estimation of pressurization for the nanometer-sized bubble is not in the scope of this study, but it might affect the deformation of the UMo particle at the initial stage of irradiation.

### 5.3. Future applications of the hybrid model

The homogeneous-meat FEM model is mutually used in the hybrid model in order to obtain the hydrostatic stress distribution for the boundary condition of the analytical model. No feedback of local stress calculated by the analytical model to the stress distribution in the homogenized-meat FEM model is required. However, as shown in Fig. 17, the feedback of calculating stress at IL/Al interface with the stress-dependent pore formation is necessary since the pore degrades the thermo-mechanical properties of fuel meat. The implementation of coupling between the hybrid model and fuel performance prediction is beyond the scope in this study, but this coupling scheme is to be verified and validated systematically by comparing with commercial FEM programs such as Abaqus and PIE observations like particle deformation, and size of pores that are stress-dependent.

![](./images/812715688320827392_26.jpg)

Fig. 17 A schematic showing a flowchart to couple stresses from the hybrid model with stress-dependent performance prediction models.

### 6. Conclusion

An analytical model was developed in this study to calculate the stresses in UMo/Al dispersion fuel by solving the governing equations for a pressurized-sphere exhibiting thermoelastic and creep deformations during irradiation. The FEM method using a homogenized-meat model involving an effective-medium approximation method was used to obtain the temperature and mechanical boundary condition for the UMo/IL/Al composite. This analytical – FEM hybrid model calculated mechanical deformation and local stresses in UMo/Al dispersion fuel. The results are consistent with those found by Abaqus simulation, accounting for a much more complex heterogeneous dispersion fuel meat.

The hybrid model was able to systematically compute the stresses at the IL/Al interface of UMo/Al dispersion fuel meat that affects pore growth outside UMo particles. Previously this capability was only possible with Abaqus simulation.

The hybrid model was verified by comparing its results to the Abaqus solutions for two plates with drastically different fuel meat composition and irradiation conditions. The results from the hybrid model were in good agreement with the Abaqus solutions.

It was found that the effect of microstructural evolution and thermal expansion of meat constituents (i.e., UMo, IL, and the Al matrix) on the hydrostatic stress distribution, which occurred in the fuel meat during irradiation, also had a considerable effect on the stress distribution of UMo/IL/Al system. Therefore, for more accurate estimation of local stresses, microstructural evolution and thermo-mechanical behavior should be considered.

### Acknowledgments

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (NRF-2019M2A7A1001758), and in part by the U.S. Department of Energy, National Nuclear Safety Administration (NNSA), Office of Material Management and Minimization (NA-23) Reactor Conversion Program under Contract No. DE-AC-02-06CH11357 between UChicago Argonne, LLC and the US Department of Energy.

### References

[1] A. Leenaers, S. Van den Berghe, E. Koonen, C. Jarousse, F. Huet, M. Trotabas, M. Boyard, S. Guillot, L. Sannen, M. Verwerft, J. Nucl. Mater. 335 (2004) 39.

[2] G.L. Hofman, M.K. Meyer, Proc. Int. Mtg. on Reduced Enrichment for Research and Test Reactors (RERTR), Bariloche, Argentina, Oct. 3-8, 2002.

[3] O.A. Golosov, S.A. Averin, V.L. Panchenko, M.S. Lyutikova, Trans. Internat. Topical Meeting Research Reactor Fuel Management (RRFM), Vienna, Austria, March 22–25, 2009

[4] G.L. Hofman, Yeon Soo Kim, M.R. Finlay, J.L. Snelgrove et al., Proc. Internat. Mtg. Reduced Enrichment for Research and Test Reactors (RERTR), Chicago, IL, USA, Oct. 5-10, 2003.
Available on the web http://www.rertr.anl.gov

[5] P. Lemoine, J.L. Snelgrove, N. Arkhangelsky, L. Alvarez, Trans. Internat. Topical Meeting Research Reactor Fuel Management (RRFM), Munich, Germany, Mar. 21-24, 2004. Available on the web http://www.euronuclear.org/meetings/rrfm2004/index.htm

[6] H.J. Ryu, Yeon Soo Kim, G.L. Hofman, J. Nucl. Mater. 385 (2009) 623.

[7] Yeon Soo Kim, Uranium Intermetallic Fuels (U-Al, U-Si, U-Mo), In: Comprehensive Nuclear Materials, R.J.M. Konings, (ed.), volume 3, p 391-422, Amsterdam, Elsevier (2012).

[8] Yeon Soo Kim, G.Y. Jeong, D.-S. Sohn, L.M Jamison, J. Nucl. Mater. 478.(2016) 275-286.

[9] A. Leenaers, S. Van den Berghe, E. Koonen, V. Kuzminov, C. Detaverneir, J. Nucl. Mater. 458 (2015) 380.

[10] Yeon Soo Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, J. Nucl. Mater. 437 (2013) 37.

[11] Yeon Soo Kim, G.L. Hofman, J.M. Park, H.J. Ryu, A.B. Robinson, D. Wachs, Proc. Int. Mtg. Reduced Enrichment for Research and Test Reactor (RERTR), Santiago, Chile, October 23–27, 2011.

[12] G.Y. Jeong, Yeon Soo Kim, L.M. Jamison, A.B. Robinson, K.H. Lee, D.-S. Sohn, J. Nucl. Mater. 487 (2017) 265.

[13] G.Y. Jeong, Yeon Soo Kim, D. Sohn, J. Nucl. Mater. 466 (2015) 509.

[14] S. Ding, Q. Wang, Y. Huo, J. Nucl. Mater. 397 (2010) 80.

[15] Y. Zhao. X. Gong, S. Ding, Y. Huo, Int. J. Mech. Sci. 81 (2014) 174.

[16] Gregory K. Miller, D. E. Burkes, D. M. Wachs, Mater. Des. 31(7) (2010) 3234.

[17] B.Yei, J. Rest, Yeon Soo Kim, G.L. Hofman, B. Dionne, Nucl. Technol. 191 (1) (2015) 27-40.

[18] G.Y. Jeong, Yeon Soo Kim, Y.J. Jeong, J.M. Park, D.-S. Sohn, J. Nucl. Mater. 502 (2018) 331.

[19] J. Rest, G.L. Hofman, Yeon Soo Kim, J. Nucl. Mater. 385 (2009) 563.

[20] Yeon Soo Kim, G.L. Hofman, J. Nucl. Maters. 425 (2012) 181

[21] A.F. Lietzke, Lewis Research Center, NASA Technical report, NASA-TN-D-5609, 1970.

[22] Yeon Soo Kim, G.Y. Jeong, J.M. Park, A.B. Robinson, J. Nucl. Mater. 465 (2015) 142.

[23] D.M. Dowling, R.J. White, M.O. Tucker, J. Nucl. Mater. 110 (1981) 37.

[24] K.J. Gellhood, W.G. Luscher, C.E. Beyer, FRAPCON-3.5: A Computer Code for the Calculation of Steady-State, Thermal-Mechanical Behavior of Oxide Fuel Rods for High Burnup. Richland, WA: US Nuclear Regulatory Commission, Office of Nuclear Regulatory Research; 2011. (NUREG/CR-7022, Vol.1 Rev.1).

[25] A. Leenaers, S. Van den Berghe, E. Koonen, V. Kuzminov, C. Detavernier, J. Nucl. Mater. 458 (2015) 380

[26] Douglas E. Burkes, David J. Senor, Andrew M. Casella, Nucl. Eng. Des. 310 (2016) 48.

[27] K.J. Bathe, Finite Element Procedures, Prentice-Hall, Englewood Cliffs, NJ, 2016.

[28] Yeon Soo Kim, G.L. Hofman, J. Nucl. Maters., 419 (2011) 291

[29] H.J. Ryu, J.M. Park, Y.J. Jeong, K.H. Lee, Y.S. Lee, C.K. Kim, Yeon Soo Kim, Nucl. Eng. Technol. 45 (2013) 847.

[30] Yeon Soo Kim, G.L. Hofman, A.B. Robinson, D.M. Wachs, *Nucl. Eng. Technol.* 45 (2013) 827.

[31] W. Dienst, S. Nazare, F. Thummler, J. Nucl. Mater. 64 (1977) 1.

[32] H.J. Ryu, Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 385 (2009) 623.

[33] J. Shewchuk, S.Y. Zamrik, J. Marin, *Experimental Mechanics* 8(11) (1968) 504.

[34] K. Farrell, Performance of Aluminum in Research Reactors. In: Konings R.J.M., (ed.) Comprehensive Nuclear Materials, Volume 5, pp. 143-175 Amsterdam: Elsevier (2012).

[35] S. Torquato, Random Heterogeneous Materials, Springer, Princeton, NJ, 2001.

[36] Z. Hashin, S. Shtrikman, J. Mech. Phys. Solids. 11(2) (1963) 127-140.

[37] V. Marelle, F. Huet, P. Lemoine, Proc. Int. Topical Meeting Research Reactor Fuel Management (RRFM), Munich, Germany, Mar. 21-24, 2004.

[38] L. Gao, B. Chen, Z. Xiao, S. Jiang, J. Yu, Pore pressure calculation of the $\mathrm{UO}_{2}$ high burnup structure, Nucl. Eng. Des. 260 (2013) 11.

[39] Y.-H. Koo, B.-H. Lee, J.S. Cheon, D.-S. Sohn, Pore pressure and swelling in the rim region of LWR high burnup $\mathrm{UO}_{2}$ fuel, J. Nucl. Mater. 295 (2001) 213.

[40] D. Salvato, A. Leenaers, S. Van den Berghe, C. Detavernier, J. Nucl. Mater. 510 (2018) 472.

[41] H.J. Ryu, J.M. Park, Y.J. Jeong, K.H. Lee, Y.S. Lee, C.K. Kim, Yeon Soo Kim, *Nucl. Eng. Technol.* 45 (2013) 847.

### Nomenclature

$\mathrm{R}$ = universal gas constant

$\mathrm{T}$ = temperature

$\mathrm{Y}_{0}$ = IL thickness at in-pile condition with pure Al matrix

$\dot{\mathrm{f}}$ = fission rate

$\mathrm{f}_{\mathrm{Si}}$ = Si addition factor on IL growth

$\mathrm{W}_{\mathrm{si}}$ = Si content in Al matrix

$\mathrm{f}_{\mathrm{Mo}}$ = Mo content factor on IL growth

$\mathrm{W}_{\mathrm{Mo}}$ = Mo content in UMo fuel

$\mathrm{V}_{\mathrm{f}}$ = UMo particle volume

$\mathrm{r}_{\mathrm{f}}$ = UMo particle radius

$\mathrm{r}_{\mathrm{IL}}$ = UMo-IL composite particle radius

$\mathrm{r}_{\mathrm{m}}$ = UMo-IL-Al matrix composite particle radius (outermost sphere radius)

$\mathrm{V}_{\mathrm{IL}}$ = IL volume

$\mathrm{V}_{\mathrm{f}}^{\mathrm{c}}$ = consumed UMo volume

$\mathrm{V}_{\mathrm{Al}}^{\mathrm{c}}$ = consumed Al volume

$\rho_{\mathrm{f}}, \rho_{\mathrm{L}}, \rho_{\mathrm{A}}$ = density of UMo, IL, and Al matrix

$\mathrm{M}_{\mathrm{f}}, \mathrm{M}_{\mathrm{IL}}, \mathrm{M}_{\mathrm{Al}}$ = molecular weight of UMo, IL, and Al matrix

$$\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)$$
= fission-induced swelling

$\mathrm{F}_{\mathrm{d}}$ = fission density in UMo fuel

$\mathrm{F}_{\mathrm{d}}^{\mathrm{IL}}$ = fission density for unit IL volume

$\psi$ = the atomic ratio of fissile U atom number density in the IL to that in the UMo fuel

$N_{U}^{IL}$ = U number density in IL

$N_{U}^{f}$ = U number density in fuel

E = modulus of elasticity

ν = Poisson's ratio

μ = Poisson's ratio under the creep deformation

S = fission-induced swelling strain

η = thermal expansion strain

β = volumetric strain by IL growth

σ = stress

ε = strain

u = displacement

$A_{c}$ = creep rate constant

$\overline{\alpha}$ = mean coefficient of thermal expansion

Subscripts

r = radial direction

θ = circumferential direction

f = UMo

IL = interaction layer

Al = Al matrix

### Abbreviation

HEU = highly-enriched uranium

LEU = low-enriched uranium

BOL = beginning of life

EOL = end of life

ANL = Argonne national laboratory

### Appendix

#### A. Procedure to derive Eq. (9) and (10)

Taking the derivative of both sides of Eq. (6) with respect to r, we have

$$
\frac{\partial \mathrm{u}}{\partial \mathrm{r}}=\frac{\mathrm{u}}{\mathrm{r}}+\frac{\mathrm{r}}{\mathrm{E}}\left[(1-v) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-v \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right]+\mathrm{r} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-\mu \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right] \mathrm{d} \tau
\tag{A1}
$$

By inserting Eq. (A1) in Eq. (6), we obtain

$$
\begin{aligned}
\frac{\partial \mathrm{u}}{\partial \mathrm{r}} & =\frac{1}{\mathrm{E}}\left[(1-v) \sigma_{\theta}-v \sigma_{\mathrm{r}}\right]+\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \sigma_{\theta}-\mu \sigma_{\mathrm{r}}\right] \mathrm{d} \tau+\mathrm{S}_{\theta}+\eta_{\theta}+\beta_{\theta} \\
& +\frac{\mathrm{r}}{\mathrm{E}}\left[(1-v) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-v \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right]+\mathrm{r} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-\mu \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right] \mathrm{d} \tau
\end{aligned}
\tag{A2}
$$

From Eqs. (1) and (3), we obtain an independent expression for $\frac{\partial \mathrm{u}}{\partial \mathrm{r}}$ as follows:

$$
\frac{\partial \mathrm{u}}{\partial \mathrm{r}}=\frac{1}{\mathrm{E}}\left[\sigma_{\mathrm{r}}-2 v \sigma_{\theta}\right]+\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[\sigma_{\mathrm{r}}-2 \mu \sigma_{\theta}\right] \mathrm{d} \tau+\mathrm{S}_{\mathrm{r}}+\eta_{\mathrm{r}}+\beta_{\mathrm{r}}
\tag{A3}
$$

By equating Eqs. (A2) and (A3), we obtain

$$
\begin{aligned}
& \frac{1+v}{\mathrm{E}}\left[\sigma_{\theta}-\sigma_{\mathrm{r}}\right]+\frac{\mathrm{r}}{\mathrm{E}}\left[(1-v) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-v \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right] \\
& +\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}(1+\mu)\left[\sigma_{\theta}-\sigma_{\mathrm{r}}\right] \mathrm{d} \tau+\mathrm{r} \int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}\left[(1-\mu) \frac{\partial \sigma_{\theta}}{\partial \mathrm{r}}-\mu \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}\right] \mathrm{d} \tau \\
& +\left(\mathrm{S}_{\theta}-\mathrm{S}_{\mathrm{r}}\right)+\left(\eta_{\theta}-\eta_{\mathrm{r}}\right)+\left(\beta_{\theta}-\beta_{\mathrm{r}}\right)=0
\end{aligned}
\tag{A4}
$$

By using Eq. (5), the term '$\sigma_{\theta}-\sigma_{\mathrm{r}}$' can be substituted by $\frac{\mathrm{r}}{2} \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}$, and Eq. (A4) turns into the 2nd-order differential equation in terms of $\sigma_{\mathrm{r}}$ as expressed in Eq. (7).

When we define H as

$$
\mathrm{H}=\int_{0}^{\mathrm{t}} \mathrm{A}_{\mathrm{c}} \dot{\mathrm{f}}(1-\mu) \Phi_{\mathrm{r}} \mathrm{d} \tau
\tag{A5}
$$

and taking the time derivative of Eq. (A5) and rearranging, we obtain

$$
\Phi_{\mathrm{r}}=\frac{1}{\mathrm{~A}_{\mathrm{c}} \dot{\mathrm{f}}(1-\mu)} \frac{\partial \mathrm{H}}{\partial \mathrm{t}}
\tag{A6}
$$

where $\Phi_{\mathrm{r}}$ is given as Eq. (8).

Inserting Eqs. (8) and (A6) to Eq. (6) gives

$$
\frac{\partial \mathrm{H}}{\partial \mathrm{t}}+\lambda(\mathrm{t}) \mathrm{H}=\lambda(\mathrm{t})(\Delta \mathrm{S}+\Delta \eta+\Delta \beta)
\tag{A7}
$$

$$\lambda(t)=\frac{\mathrm{EA}_{\mathrm{c}} \dot{\mathrm{f}}(\mathrm{t})(1-\mu)}{1-v}$$

where

To solve Eq. (A7), an integration factor, G(r,t), is introduced as follows:

$$\mathrm{G}(\mathrm{r}, \mathrm{t})=\exp \left[\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right] \tag{A8}$$

Using G(r,t) in Eq. (A7) gives

$$\mathrm{H}(\mathrm{r}, \mathrm{t})=\exp \left[-\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right] \cdot \int_{0}^{\mathrm{t}}\left[\lambda(\tau)(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \cdot \exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right] \mathrm{d} \tau \tag{A9}$$

$\mathrm{H}(\mathrm{r}, \mathrm{t})$ can be differentiated with respect to time 't' to obtain $\frac{\partial \mathrm{H}}{\partial \mathrm{t}}$ as follows:

$$
\begin{aligned}
\frac{\partial \mathrm{H}}{\partial \mathrm{t}}= & \lambda(\mathrm{t}) \cdot(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \\
& -\lambda(\mathrm{t}) \exp \left[-\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right] \cdot \int_{0}^{\mathrm{t}}\left[\lambda(\tau)(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \cdot \exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right] \mathrm{d} \tau
\end{aligned} \tag{A10}
$$

Inserting Eq. (A10) into Eq. (A6) gives the following equation:

$$2 \mathrm{r} \frac{\partial \sigma_{\mathrm{r}}}{\partial \mathrm{r}}+\frac{\mathrm{r}^{2}}{2} \frac{\partial^{2} \sigma_{\mathrm{r}}}{\partial \mathrm{r}^{2}}=\mathrm{f}(\mathrm{t}) \tag{A11}$$

where

$$
\begin{aligned}
\mathrm{f}(\mathrm{t})= & \frac{\mathrm{E}}{1-v}(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \\
& -\frac{\mathrm{E}}{1-v} \exp \left[-\int_{0}^{\mathrm{t}} \lambda(\tau) d \tau\right] \cdot \int_{0}^{\mathrm{t}}\left[\lambda(\tau)(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \cdot \exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right] \mathrm{d} \tau
\end{aligned} \tag{A12}
$$

with

$$\frac{\mathrm{d}}{\mathrm{d} \tau}\left[\exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right]=\lambda(\tau) \cdot \exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right) \tag{A13}$$

By using Eq. (A13), Eq. (A12) can be rearranged with the fact that components for S are zero at t=0 as follows:

$$
\begin{aligned}
\mathrm{f}(\mathrm{t})= & \frac{\mathrm{E}}{1-v}(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \\
& -\frac{\mathrm{E}}{1-v} \exp \left[-\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right] \cdot \int_{0}^{\mathrm{t}}\left[(\Delta \mathrm{S}+\Delta \eta+\Delta \beta) \cdot \frac{\mathrm{d}}{\mathrm{d} \tau}\left[\exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right]\right] \mathrm{d} \tau
\end{aligned} \tag{A14}
$$

It is noted that f(t) is the stress component caused by irradiation-induced swelling, thermal expansion, and chemical volume expansion induced by IL formation. According to the initial condition, the components for S and $\beta$ are equal to zero at t=0, so Eq. (A14) is expressed as


follows:

$$
\mathrm{f}(\mathrm{t})=\frac{\mathrm{E}}{1-\mathrm{v}}\left(\exp \left[-\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right]\right) \cdot\left[\Delta \eta(0)+\int_{0}^{\mathrm{t}}\left[(\Delta \dot{\mathrm{S}}+\Delta \dot{\eta}+\Delta \dot{\beta}) \cdot \exp \left(\int_{0}^{\mathrm{t}} \lambda(\tau) \mathrm{d} \tau\right)\right] \mathrm{d} \tau\right] \tag{A15}
$$

It is to be noted that f(t) is dependent only upon time and material properties, not the radial coordinate.

### B. Boundary/interfacial conditions and coefficients in equations of stresses

The boundary and interfacial conditions to obtain unknown coefficients in the function of radial stress in each region are given as follows:

- UMo region:

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{\mathrm{i}} \text { (hypothetical fission gas bubble radius) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{f}}=\mathrm{P}_{\mathrm{i}} \text { (pressure by fission gas bubble) }
\end{aligned} \tag{B1}
$$

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{\mathrm{f}} \text { (fuel particle radius) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{f}}=\Pi_{1} \text { (interfacial stress at UMo/IL) }
\end{aligned} \tag{B2}
$$

- Interaction layer region:

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{\mathrm{f}} \text { (fuel particle radius) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{IL}}=\Pi_{1} \text { (interfacial stress at UMo/IL) }
\end{aligned} \tag{B3}
$$

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{\mathrm{IL}} \text { (IL/Al interface) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{IL}}=\Pi_{2} \text { (interfacial stress at IL/Al) }
\end{aligned} \tag{B4}
$$

- At the interaction layer/Al layer interface:

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{\mathrm{IL}} \text { (IL-Al interface) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{Al}}=\Pi_{2} \text { (interfacial stress at IL/Al) }
\end{aligned} \tag{B5}
$$

$$
\begin{aligned}
& \text { At } \mathrm{r}=\mathrm{r}_{m} \text { (outermost radius) : } \\
& \sigma_{\mathrm{r}}^{\mathrm{Al}}=\sigma_{\mathrm{h}} \text { (hydrostactic stress) }
\end{aligned} \tag{B6}
$$

When UMo swelling, thermal expansion, and IL chemical volume expansion are all isotropic, $\Delta$ quantities are zero, leading to simplified equations for radial and circumferential stress, since f(t) = 0 . Then, coefficients in each region are explicitly expressed as follows:

- UMo fuel

$$
C_{1}^{\mathrm{f}}=-\frac{\mathrm{P}_{\mathrm{i}} \mathrm{r}_{\mathrm{i}}^{3}-\Pi_{1} \mathrm{r}_{\mathrm{f}}^{3}}{\mathrm{r}_{\mathrm{f}}^{3}-\mathrm{r}_{\mathrm{i}}^{3}} \tag{B7}
$$

$$
\mathrm{C}_{2}^{\mathrm{f}}=\frac{\mathrm{r}_{\mathrm{i}}^{3} \mathrm{r}_{\mathrm{f}}^{3}\left(\mathrm{P}_{\mathrm{i}}-\Pi_{1}\right)}{\mathrm{r}_{\mathrm{f}}^{3}-\mathrm{r}_{\mathrm{i}}^{3}} \tag{B8}
$$

- IL

$$
\mathrm{C}_{1}^{\mathrm{IL}}=-\frac{-\Pi_{1} \mathrm{r}_{\mathrm{f}}^{3}+\Pi_{2} \mathrm{r}_{\mathrm{IL}}^{3}}{\mathrm{r}_{\mathrm{f}}^{3}-\mathrm{r}_{\mathrm{IL}}^{3}} \tag{B9}
$$

$$
\mathrm{C}_{2}^{\mathrm{IL}}=-\frac{\mathrm{r}_{\mathrm{f}}^{3} \mathrm{r}_{\mathrm{IL}}^{3}\left(\Pi_{1}-\Pi_{2}\right)}{\mathrm{r}_{\mathrm{f}}^{3}-\mathrm{r}_{\mathrm{IL}}^{3}} \tag{B10}
$$

- Al matrix

$$
\mathrm{C}_{1}^{\mathrm{Al}}=-\frac{\sigma_{\mathrm{h}} \mathrm{r}_{\mathrm{m}}^{3}-\Pi_{2} \mathrm{r}_{\mathrm{IL}}^{3}}{\mathrm{r}_{\mathrm{IL}}^{3}-\mathrm{r}_{\mathrm{m}}^{3}} \tag{B11}
$$

$$
\mathrm{C}_{2}^{\mathrm{IL}}=-\frac{\mathrm{r}_{\mathrm{IL}}^{3} \mathrm{r}_{\mathrm{m}}^{3}\left(\Pi_{2}-\sigma_{\mathrm{h}}\right)}{\mathrm{r}_{\mathrm{IL}}^{3}-\mathrm{r}_{\mathrm{m}}^{3}} \tag{B12}
$$

### C. Irradiation performance models

#### C.1. Fission-induced swelling

##### - UMo fuel
The total UMo swelling for U-10Mo fuel is given as the following empirical correlation [22]:

$$
\begin{cases}
\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{f}}^{\mathrm{s}}=5.0 \mathrm{F}_{\mathrm{d}} & \mathrm{F}_{\mathrm{d}} \leq 3 \times 10^{21} \text { fission/cm}^3 \\
=15+6.3(\mathrm{F}_{\mathrm{d}}-3)+0.33(\mathrm{F}_{\mathrm{d}}-3)^{2} & \mathrm{F}_{\mathrm{d}}>3 \times 10^{21} \text { fission/cm}^3
\end{cases} \tag{C1}
$$

and for U-7Mo:

$$
\begin{cases}
\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{f}}^{\mathrm{s}}=5.0 \mathrm{F}_{\mathrm{d}} & \mathrm{F}_{\mathrm{d}} \leq 2 \times 10^{21} \text { fission/cm}^3 \\
=10+6.7(\mathrm{F}_{\mathrm{d}}-2)+0.58(\mathrm{F}_{\mathrm{d}}-2)^{2} & \mathrm{F}_{\mathrm{d}}>2 \times 10^{21} \text { fission/cm}^3
\end{cases} \tag{C2}
$$

where $\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{f}}^{\mathrm{s}}$ is the UMo swelling in percent, and $\mathrm{F}_{\mathrm{d}}$ is the fission density of UMo fuel in $10^{21}$ fission/cm³-UMo.

The transition in the UMo swelling correlation at a fission density of $2 \times 10^{21}$ for U-7Mo and $3 \times 10^{21}$ fission/cm³ for U-10Mo is reflecting the acceleration of swelling rate due to grain subdivision.

For the swelling by gaseous fission product, the correlation is given as follows:

For U-10Mo:

$$
\begin{cases}
\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{g}}=1.0 \mathrm{F}_{\mathrm{d}} & \mathrm{F}_{\mathrm{d}} \leq 3 \times 10^{21} \text { fission/cm}^3 \\
=3.0+6.3(\mathrm{F}_{\mathrm{d}}-3)+0.33(\mathrm{F}_{\mathrm{d}}-3)^{2} & \mathrm{F}_{\mathrm{d}}>3 \times 10^{21} \text { fission/cm}^3
\end{cases} \tag{C3}
$$

and for U-7Mo:

$$
\begin{cases}
\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{g}}=1.0 \mathrm{F}_{\mathrm{d}} & \mathrm{F}_{\mathrm{d}} \leq 2 \times 10^{21} \text { fission/cm}^3 \\
=2.0+6.7(\mathrm{F}_{\mathrm{d}}-2)+0.58(\mathrm{F}_{\mathrm{d}}-2)^{2} & \mathrm{F}_{\mathrm{d}}>2 \times 10^{21} \text { fission/cm}^3
\end{cases} \tag{C4}
$$

where $\left(\dfrac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{g}}$ is the fission gas bubble swelling.

##### - IL
The fission-induced swelling for $\mathrm{UAl}_{\mathrm{x}}$ is available in the literature [41] as follows:


$$
\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{IL}}=6.4 \mathrm{~F}_{\mathrm{d}}^{\mathrm{IL}}
\tag{C5}
$$

where $\mathrm{F}_{\mathrm{d}}^{\mathrm{IL}}$ is the fission density in $10^{21}$ fission/cm$^3$-IL. It is to be noted that $\mathrm{F}_{\mathrm{d}}^{\mathrm{IL}}$ is the fission density of IL, which is the amount of fissioned U atoms in a unit volume of IL. $\mathrm{F}_{\mathrm{d}}^{\mathrm{IL}}$ is calculated from the fission density of the UMo at the same time, which is shown as:

$$
\mathrm{F}_{\mathrm{d}}^{\mathrm{IL}}=\psi \mathrm{F}_{\mathrm{d}}
\tag{C6}
$$

where $\psi$ is the atomic ratio of fissile uranium atom number density in the IL to that in the UMo, calculated from:

$$
\psi=\frac{\mathrm{N}_{\mathrm{U}}^{\mathrm{IL}}}{\mathrm{N}_{\mathrm{U}}^{\mathrm{f}}}=\frac{\rho_{\mathrm{IL}} \mathrm{M}_{\mathrm{U}}}{\rho_{\mathrm{f}} \mathrm{M}_{\mathrm{IL}}} \frac{1}{\left(1-\mathrm{wt}_{\mathrm{Mo}}\right)}
\tag{C7}
$$

where $\mathrm{M}_{\mathrm{U}}$ is the atomic weight of uranium, and $\mathrm{wt}_{\mathrm{Mo}}$ is the Mo weight fraction in the UMo. The ratio $\psi$ is defined by the number density of U in the IL and UMo. For typical IL of U(Mo)Al₄, with 10 wt.% Mo, $\psi$ is 0.27.

### C.2. Interaction layer growth

The correlation for interaction layer growth with additional factors for the effect of Si addition and Mo content is expressed as follows [30]:

$$
\mathrm{Y}^{2}=\mathrm{Y}_{0}^{2} \cdot \mathrm{f}_{\mathrm{Si}} \cdot \mathrm{f}_{\mathrm{Mo}}
\tag{C8}
$$

where $\mathrm{Y}$ is the interaction layer thickness formed during irradiation in $\mathrm{\mu m}$, and $\mathrm{Y}_{0}$ is the interaction layer thickness in pure Al matrix in $\mathrm{\mu m}$, which is given as follows:

$$
\mathrm{Y}_{0}^{2}=2.6 \times 10^{-8} \dot{\mathrm{f}}^{1 / 2} \exp \left(-\frac{32009}{\mathrm{RT}}\right) \mathrm{t}
\tag{C9}
$$

where $\dot{\mathrm{f}}$ is the fission rate in fission/cm$^3$-sec, T is the temperature in K, t is the irradiation time in sec.

The factor for Si addition effect $(\mathrm{f}_{\mathrm{Si}})$ is given with the temperature dependency as follows:

$$
\begin{aligned}
\mathrm{f}_{\mathrm{Si}}= & (1.201-6.2 \times 10^{-4} \mathrm{~T}) \exp \left[-\left(10.333-2.1 \times 10^{-2} \mathrm{~T}\right) \mathrm{W}_{\mathrm{si}}\right] \\
& +(6.2 \times 10^{-4} \mathrm{~T}-0.201) \exp \left[-\left(8.1 \times 10^{-4} \mathrm{~T}-0.302\right) \mathrm{W}_{\mathrm{si}}\right]
\end{aligned}
\tag{C10}
$$

where T is the fuel meat temperature in K ($\leq$ 473K) and $\mathrm{W}_{\mathrm{Si}}$ is the Si content in the Al matrix in wt. %

($\leq 8$ wt. \%). $f_{s_{i}}$ has a range from 0.002 to 1.0.

The factor for Mo content ($f_{_{Mo}}$) effect in a range of 6 – 10 wt.% Mo is given as follows:

$$
f_{_{Mo}}=1.35-0.05W_{_{Mb}} \tag{C11}
$$

where $W_{_{Mb}}$ is the Mo content in UMo fuel in wt.\%. $f_{_{Mo}}$ has a maximum value of 1.05 with 6 wt.\% Mo, and a minimum value of 0.85 at 7 wt.\% Mo.

The IL volume ($V_{_{IL}}$) can be calculated using the model given in [30] with the assumption that UMo particles with the uniform size are dispersed in the Al matrix as a face-centered cubic (FCC) array. The consumed UMo and Al matrix volume can be calculated for the given IL volume formed during irradiation using densities for UMo fuel, Al matrix, and IL as follows:

$$
V_{f}^{c}=\frac{\rho_{_{IL}}}{\rho_{f}} \frac{M_{f}}{M_{_{IL}}} V_{_{IL}} \tag{C12}
$$

$$
V_{Al}^{c}=X_{_{IL}} \frac{\rho_{_{IL}}}{\rho_{Al}} \frac{M_{Al}}{M_{_{IL}}} V_{_{IL}} \tag{C13}
$$

where $\rho$ is the density, $V$ is the volume in $\mathrm{cm}^{3}$, $M$ is the molecular mass. The superscript c stands for the consumption, and subscripts represent the material; f for UMo and others for IL and Al.

Using the produced and consumed volume of UMo and Al matrix, the strain for each region due to the chemical volume expansion of IL can be given using Eqs. (C12) and (C13) as follows:

- **IL**

$$
eta_{r}=eta_{	heta}=\frac{1}{3} \ln [1+\left(\frac{\Delta V}{V_{0}}ight)_{_{IL}}^{c}] \tag{C14}
$$

where

$$
\left(\frac{\Delta V}{V_{0}}ight)_{_{IL}}^{c}=\frac{V_{_{IL}}}{V_{_{IL}}^{0}} \tag{C15}
$$

- **UMo**

$$
eta_{r}=eta_{	heta}=-\frac{1}{3} \ln [1+\left(\frac{\Delta V}{V_{0}}ight)_{f}^{c}] \tag{C16}
$$

where

$$
\left(\frac{\Delta V}{V_{0}}ight)_{f}^{c}=1-\frac{V_{f}^{c}}{V_{f}^{0}} \tag{C17}
$$

- **Al matrix**

$$
\beta_{\mathrm{r}}=\beta_{\theta}=-\frac{1}{3} \ln \left[1+\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{Al}}^{\mathrm{c}}\right] \tag{C18}
$$

where

$$
\left(\frac{\Delta \mathrm{V}}{\mathrm{V}_{0}}\right)_{\mathrm{Al}}^{\mathrm{c}}=1-\frac{\mathrm{V}_{\mathrm{Al}}^{\mathrm{c}}}{\mathrm{V}_{\mathrm{f}}^{0}} \tag{C19}
$$

The authors declare no conflict of interest.