# Comparison of different fluid-thermal-electric multiphysics modeling approaches for thermoelectric generator systems

Ding Luo$^{a,b}$, Ruochen Wang$^{a,*}$,Yuying Yan$^{b,**}$, Zeyu Sun$^{a}$, Weiqi Zhou$^{a}$, Renkai Ding$^{a}$

$^{a}$ School of Automobile and Traffic Engineering, Jiangsu University, Zhenjiang, 212013, China

$^{b}$ Faculty of Engineering, University of Nottingham, University Park, Nottingham, UK

Corresponding author: * wrc@ujs.edu.cn; ** yuying.yan@nottingham.ac.uk

**Abstract:** This work proposes a novel fluid-thermal-electric multiphysics numerical model to predict the performance of thermoelectric generator systems applied to fluid waste heat recovery, with the consideration of multiphysics coupling effects of fluid, thermal, and electric fields. The comprehensive numerical simulations of the thermoelectric generator system are performed via COMSOL coupled solver. Besides, the effect of the neglect of parasitic heat on the output performance is investigated through the comparison with numerical results predicted by ANSYS and COMSOL separate solver, wherein the fluid-thermal field is computed first, then the thermal-electric field. The results show that the output power predicted by COMSOL separate solver is 8.52% lower than that predicted by COMSOL coupled solver at the inlet air temperature of 550 K and inlet air velocity of 30 m/s due to the neglect of parasitic heat. The output performance of the TEG system predicted by ANSYS is less affected by inlet air boundary conditions than that predicted by COMSOL. Finally, the experimental results show that the fluid-thermal-electric multiphysics model solved by the COMSOL coupled solver shows the lowest output power deviation of 2.81%. The proposed model can guide the numerical modeling of the thermoelectric generator system applied to fluid waste heat recovery.

**Keywords:** Thermoelectric generator; Numerical simulation; Multiphysics; Experimental validation; Numerical modeling

<h2>Nomenclature</h2>

<h3>Symbols</h3>
<table>
  <tr>
    <td>$A$</td>
    <td>area, $\text{mm}^2$</td>
    <td>$\lambda$</td>
    <td>thermal conductivity, $\text{W·m}^{-1}·\text{K}^{-1}$</td>
  </tr>
  <tr>
    <td>$c$</td>
    <td>specific heat capacity, $\text{J·kg}^{-1}·\text{K}^{-1}$</td>
    <td>$\alpha$</td>
    <td>Seebeck coefficient, $\mu\text{V·K}^{-1}$</td>
  </tr>
  <tr>
    <td>$\vec{E}$</td>
    <td>electric field intensity vector, $\text{mV·mm}^{-2}$</td>
    <td>$\sigma^{-1}$</td>
    <td>electrical resistivity, $10^{-5}\Omega\text{·m}$</td>
  </tr>
  <tr>
    <td>$h$</td>
    <td>height (mm) or convective coefficient ($\text{W·m}^{-2}·\text{K}^{-1}$)</td>
    <td>$\phi$</td>
    <td>electric potential, $\text{mV}$</td>
  </tr>
  <tr>
    <td>$I$</td>
    <td>current, $\text{A}$</td>
    <td>$\rho$</td>
    <td>density, $\text{kg·m}^{-3}$</td>
  </tr>
  <tr>
    <td>$\vec{J}$</td>
    <td>current density vector, $\text{mA·mm}^{-2}$</td>
    <td>$\mu$</td>
    <td>dynamic viscosity, $\text{Pa·s}$</td>
  </tr>
  <tr>
    <td>$k$</td>
    <td>turbulent kinetic energy, $\text{J}$</td>
    <td>$\varepsilon$</td>
    <td>turbulent dissipation rate</td>
  </tr>
  <tr>
    <td>$N$</td>
    <td>number of p-type or n-type thermoelectric legs</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$P$</td>
    <td>output power, $\text{W}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$p$</td>
    <td>pressure, $\text{Pa}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$Q$</td>
    <td>heat, $\text{W}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$R$</td>
    <td>resistance, $\Omega$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$T$</td>
    <td>temperature, $\text{K}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$U$</td>
    <td>output voltage, $\text{V}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$v$</td>
    <td>velocity, $\text{m·s}^{-1}$</td>
    <td></td>
    <td></td>
  </tr>
</table>

<h3>Greek symbols</h3>

<h3>Subscripts</h3>
<table>
  <tr>
    <td>air</td>
    <td>air</td>
  </tr>
  <tr>
    <td>am</td>
    <td>ambient</td>
  </tr>
  <tr>
    <td>c</td>
    <td>cold side</td>
  </tr>
  <tr>
    <td>h</td>
    <td>hot side</td>
  </tr>
  <tr>
    <td>in</td>
    <td>internal resistance</td>
  </tr>
  <tr>
    <td>L</td>
    <td>load resistance</td>
  </tr>
  <tr>
    <td>leg</td>
    <td>thermoelectric legs</td>
  </tr>
  <tr>
    <td>n</td>
    <td>n-type thermoelectric legs</td>
  </tr>
  <tr>
    <td>p</td>
    <td>p-type thermoelectric legs</td>
  </tr>
  <tr>
    <td>peltier</td>
    <td>Peltier effect</td>
  </tr>
</table>

<h1>1. Introduction</h1>

In recent decades, energy shortage has become an increasingly serious global problem due to the overuse of fossil fuels [1]. In particular, the fuel consumption of driving vehicles accounts for 38% of the annual global use of oil [2]. Considering that a considerable part of thermal energy, accounting for about 30% of the chemical energy contained in the fuel [3], is wasted in the form of exhaust gases, a potential manner to improve the fuel economy is to recover the waste heat contained in exhaust gases.

There are two kinds of engine waste heat recovery techniques, one is the Organic Rankine Cycle (ORC) system [4, 5] that converts thermal energy into mechanical energy, another one is the Thermoelectric Generator (TEG) system [6, 7] that directly converts thermal energy into electrical energy. Due to the limitation of space and weight of the automobile exhaust system, the application of ORC systems in passenger cars is limited, and ORC systems are mainly used in heavy-duty vehicles or ships. On the contrary, the TEG system enables wide applications from light-duty cars [8] to heavy trucks [9], owing

to its unparalleled merits, such as long service life, no moving components, small size, etc [10].

Nevertheless, the low conversion efficiency of the TEG system is still one of the main limitations of its wide commercial application in the automotive field. To improve the performance of the TEG system, it is essential to optimize its structure regarding thermoelectric modules (TEMs) [11] and heat exchangers [12, 13].

It is recommended to use theoretical modeling approaches to perform the structure optimization regarding the TEG system, rather than to fabricate several prototypes with different parameters and then compare their behavior via experimental tests. A great number of theoretical models have been developed to predict the performance of TEG systems in recent years. Based on a thermal resistance network, Hsiao et al. [14] established a one-dimensional analytical model to assess the output performance of the TEG system with one TEM, and the model results showed great consistency with experimental data. By extending the model of the TEG system from one TEM to a TEM array and from one dimension to three dimensions, Huang et al. [15] proposed a three-dimensional thermal resistance model to evaluate the performance of a TEG system with 8 TEMs; Compared with Computational Fluid Dynamics (CFD) simulations, the developed model can save much time, especially when several variables were considered to be optimized, and the model results matched CFD results within 6%. However, the output performance of the TEG system predicted by the thermal resistance model was more unrealistic than that predicted by the numerical model [16]. Kempf and Zhang [17] utilized the commercial numerical analysis software of ANSYS to carry out CFD simulations of an automotive TEG system, and detailed temperature distributions of the TEG system were obtained; According to the CFD results, output power and fuel efficiency of the automotive TEG system were modeled, and further, the parametric optimization for the heat exchanger was completed. He et al. [18] introduced an innovative power deviation analysis method which is significant to guide TEG design with high-efficiency for fluctuated exhaust heat recovery. Fernández-Yáñez et al. [19]

conducted a thermal analysis of a TEG system using the CFD model, and the effects of sizes and internal structures of the heat exchanger were studied; The research findings provided a new insight for maximizing the output power and reducing the influence on the engine. However, when the heat is transferred from the hot side to the cold side of TEMs, thermoelectric effects will occur, including Seebeck effect, Peltier effect, Thomson effect, and Joule effect, and those can not be ignored during the modeling process of the TEG system.

In consideration of the inevitable error of current theoretical models, researchers manufactured a great number of TEG system prototypes and studied their performance via experimental tests, because experiment measurement is the most accurate method to evaluate the performance of the TEG system. Kim et al. [20] fabricated a hexagonal-shaped TEG system prototype with 18 TEMs and installed it in the engine exhaust system of a hybrid electric vehicle; The experimental results showed that the maximum output power of the TEG system is 98.8 W and the maximum conversion efficiency is 2.6%. Zhang [21] developed a 1-kW TEG system with 400 TEMs to recover the waste heat from the automotive exhaust gas, and a diesel engine test bench was adopted to examine the behavior of the manufactured TEG system. Chen et al. [22] investigated the effects of the hot-side temperature, flow pattern, number of modules, and water flow rate on the performance of the TEG system via experiments; The results indicated that the influence of flow pattern and water flow rate on the performance was insignificant, and more attention should be paid into improving the hot-side temperature. Aranguren et al. [23] fabricated a TEG system prototype with 48 TEMs to recover thermal energy from a combustion chamber, and the system was cooled by finned heat sinks; Through the experimental test, a net power of 21.56 W was reached. However, the experimental method is inadvisable when optimizing the structural parameters of the TEG system because of the huge cost of time and money. The most reasonable process is to use the theoretical model to optimize the TEG system, obtain the optimal structure, manufacture the corresponding prototype, and finally carry out

the verification test. Therefore, a more comprehensive and accurate theoretical model to predict the performance of the TEG system needs to be developed.

In essence, the complex multiphysics field coupling effects complicate the modeling of the TEG system, which includes not merely the fluid-thermal coupling effect between the exhaust gas (cooling water) and the heat exchanger (heat sinks), but also the thermal-electric coupling effect of TEMs. And further, the heat produced by the electric field will react on the flow field and thermal field. CFD model [24] has been developed as a powerful tool to compute the fluid flow, and it has been widely used in TEG systems. As for the modeling of TEMs, the thermal-electric multiphysics numerical model [25, 26] has been verified as an effective method to calculate the outputs of the thermoelectric generator or cooler. However, when recovering waste heat from hot fluids, the modeling of the whole TEG system suffers from the interaction of the flow, thermal, and electric fields. Luo et al. [27] considered the fluid-thermal-electric multiphysics coupling field as the combination of fluid-thermal field and thermal-electric field and proposed a fluid-thermal-electric multiphysics numerical model to predict the performance of the TEG system; The acceptable error between numerical results and experimental data exhibited a good validity of the proposed model. Nevertheless, the effect of Peltier heat and Joule heat on the fluid-thermal field was not taken into consideration in their research, which may induce the extra error. Accordingly, the fluid, thermal, and electric fields should be computed at the same time to ensure the high accuracy of the fluid-thermal-electric multiphysics model of the TEG system.

As mentioned above, analytical models [28, 29] can work out the output power and conversion efficiency of the TEG system in a short time, but the error is large. CFD model [30] can figure out the temperature distribution of the whole TEG system, and then the electric outputs can be calculated according to the surface temperature on both sides of TEMs [31]. In Ref. [27], the CFD model was combined with the thermal-electric numerical model, and the predicted results were more accurate than those from CFD simulations, but the fluid-thermal-electric multiphysics field coupling effects were

ignored in the model.

In this study, a novel fluid-thermal-electric multiphysics numerical model was proposed to assess the performance of an air-to-water TEG system, wherein the fluid, thermal, and electric fields were computed at the same time, which can predict more reasonable results than all aforementioned models. In addition, a comparison study among different multiphysics models was conducted, and the effect of inlet boundary conditions was investigated. Finally, the experimental demonstration was performed to validate the model. The findings of this work can provide a new idea to predict the performance of the TEG system applied to fluid waste heat recovery.

## 2. Fluid-thermal-electric multiphysics models of the thermoelectric generator system

### 2.1 Three-dimensional geometry of the air-to-water thermoelectric generator system

When the thermoelectric device is used to recover waste heat from engine exhaust or other forms of waste heat contained in thermal fluids, the thermoelectric generator (TEG) system usually consists of three parts: a heat exchanger, thermoelectric modules (TEMs), and heat sinks. Besides, the TEG system involves the intricate coupling effects of multiphysics fields, including fluid, thermal, and electric fields. This work is dedicated to investigate the multiphysics field coupling effect and establish a fluid-thermal-electric multiphysics numerical model to estimate the output performance of the TEG system. To achieve this goal, an air-to-water TEG system is chosen as the research object, as shown in Fig. 1(a). An aluminum heat exchanger with fins inside is designed to absorb the heat of hot air. The dimension of the cross section of the heat exchanger is $60\ \text{mm} \times 60\ \text{mm}$, and the length of the heat exchanger is $45\ \text{mm}$. The 12 fins are evenly distributed on the two inner hot-side walls of the heat exchanger, and the cross-sectional area of each fin is $37.5\ \text{mm}^2$, as shown in Fig. 1(b). Two steel connectors are connected to the heat exchanger as the air inlet and outlet with a diameter of $40\ \text{mm}$. An aluminum heat sink with cooling pipelines is designed to provide a stable cold-side temperature.

In this study, the coolant is water, and the diameter of the pipeline is 5.5 mm. The schematic of the TEM (TEG-127020, P&N technology, China) is shown in Fig. 1(d). There are 128 pairs of p-type and n-type thermoelectric legs connected in series by copper electrode slices, and the thermoelectric material is Bi₂Te₃-based. Thermoelectric legs and copper electrode slices are sandwiched between two ceramic plates. The size of thermoelectric legs is 1.4×1.4×1.0 (L×W×H) mm³, the size of copper electrode slices is 3.8×1.4×0.35 (L×W×H) mm³, and the size of ceramic plates is 44 (or 40)×40×0.8 (L×W×H) mm³. To form a complete electric circuit, a load resistance with a size of 0.5×0.5×35.5 mm³ is connected to the TEM, and the value of load resistance can be altered by changing its material resistivity. The datasheet regarding the material properties of the air-to-water TEG system can be found in Table 1. The temperature dependence of thermoelectric material and dry air is taken into consideration, and the corresponding material parameters as a function of temperature are obtained through a polynomial fitting method.

![](./images/811829752959598593_1.jpg)

Fig. 1. Schematic of the air-to-water thermoelectric generator system. (a) The whole structure of thermoelectric generator system; (b) The section view of the heat exchanger; (c) The grid system of thermoelectric generator system; (d) Schematic of the thermoelectric module. 1, inlet connector of the heat exchanger; 2, heat sink; 3, thermoelectric module; 4, outlet connector of the heat exchanger; 5, heat exchanger; 6, fin structure of heat exchanger; 7, p-type thermoelectric legs; 8, n-type thermoelectric legs; 9, copper electrode slices; 10, ceramic plate; 11, load resistance.

<table>
<caption>Table 1. Datasheet of the material properties of the air-to-water TEG system [11]</caption>
<thead>
<tr>
<th>Component</th>
<th>Material name</th>
<th>Material parameter</th>
<th>Value</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Heat exchanger and heat sink</td>
<td>Aluminum</td>
<td>Thermal conductivity</td>
<td>217.7</td>
<td>W·m⁻¹·K⁻¹</td>
</tr>
<tr>
<td>Inlet and outlet connectors</td>
<td>Steel</td>
<td>Thermal conductivity</td>
<td>17</td>
<td>W·m⁻¹·K⁻¹</td>
</tr>
<tr>
<td rowspan="4">p-type and n-type thermoelectric legs</td>
<td rowspan="4">Bi₂Te₃-based thermoelectric material</td>
<td>p-type Seebeck coefficient</td>
<td>$-1.80268×10^{-7}T^{4}+3.23632×10^{-4}T^{3}$<br>$-0.21537T^{2}+62.97444T-6616.56781$</td>
<td>μV·K⁻¹</td>
</tr>
<tr>
<td>n-type Seebeck coefficient</td>
<td>$1.80268×10^{-7}T^{4}-3.23632×10^{-4}T^{3}$<br>$+0.21537T^{2}-62.97444T+6616.56781$</td>
<td>μV·K⁻¹</td>
</tr>
<tr>
<td>Thermal conductivity</td>
<td>$-3.0595×10^{-9}T^{4}+4.5678×10^{-6}T^{3}$<br>$-2.5162×10^{-3}T^{2}+0.6107T-53.9863$</td>
<td>W·m⁻¹·K⁻¹</td>
</tr>
<tr>
<td>Electrical resistivity</td>
<td>$-3.088×10^{-9}T^{4}+4.5653×10^{-6}T^{3}$<br>$-2.5854×10^{-3}T^{2}+0.6558T-60.588$</td>
<td>$10^{-5}Ω·m$</td>
</tr>
<tr>
<td rowspan="2">Copper electrode slices</td>
<td rowspan="2">Copper</td>
<td>Thermal conductivity</td>
<td>165.64</td>
<td>W·m⁻¹·K⁻¹</td>
</tr>
<tr>
<td>Electrical resistivity</td>
<td>$1.75×10^{-3}$</td>
<td>$10^{-5}Ω·m$</td>
</tr>
<tr>
<td>Ceramic plates</td>
<td>Ceramic</td>
<td>Thermal conductivity</td>
<td>18</td>
<td>W·m⁻¹·K⁻¹</td>
</tr>
<tr>
<td>Load resistance</td>
<td>NA</td>
<td>Electrical resistivity</td>
<td>$284^{-1}×10^{-3}~142^{-1}×10^{-2}$</td>
<td>Ω·m</td>
</tr>
</tbody>
</table>

### 2.2 Governing equations of the fluid-thermal-electric multiphysics model

When the heat is transferred from the hot air to the heat exchanger or from the heat sink to the cooling water, the fluid-thermal multiphysics field coupling effect is induced. Meanwhile, the carriers inside thermoelectric materials will move from the high-temperature side to the low-temperature side driven by the temperature difference, and a Seebeck voltage is generated, which involves the thermal-electric multiphysics field coupling effect. In addition, the parasitic heat caused by the Peltier effect and Joule effect will affect the heat conduction in the heat exchanger and heat sink and finally affect the fluid flow. Therefore, fluid, thermal, and electric fields interact with each other, and the governing equations of these three fields should be solved at the same time.

The physical characteristics of the fluid-thermal-electric multiphysics field coupling effect follow the fundamental governing equations of fluid flow, energy conservation, heat transfer, thermoelectric effect, and electrical current flow. The fluid flow of the hot air and cooling water can be modeled by the computational fluid dynamics (CFD) theory. In general, the air and water can be regarded as incompressible due to the considerably low Mach number of fluid flow [32]. Also, the fluid pattern presents turbulent flow, and the $k-\varepsilon$ turbulent model is one of the most effective methods to compute

the turbulent flow. In this study, the renormalization group (RNG) $k-\varepsilon$ turbulent model is used because of its higher accuracy and adaptivity. Detailed governing equations about the fluid flow includes:

$$
\nabla \cdot v=0 \tag{1}
$$

$$
\nabla \cdot(v v)=-\frac{1}{\rho} \nabla p+\nabla \cdot(\mu \nabla v) \tag{2}
$$

$$
\nabla \cdot(\lambda \nabla T)=\rho c v \cdot \nabla T \tag{3}
$$

$$
\frac{\partial}{\partial x_{i}}\left(\rho k u_{i}\right)=\frac{\partial}{\partial x_{j}}\left(\alpha_{k} \mu_{e f f} \frac{\partial k}{\partial x_{j}}\right)+G_{k}+G_{b}-\rho \varepsilon-Y_{M} \tag{4}
$$

$$
\frac{\partial}{\partial x_{i}}\left(\rho \varepsilon u_{i}\right)=\frac{\partial}{\partial x_{j}}\left(\alpha_{\varepsilon} \mu_{e f f} \frac{\partial \varepsilon}{\partial x_{j}}\right)+C_{1 \varepsilon} \frac{\varepsilon}{k}\left(G_{k}+C_{3 \varepsilon} G_{b}\right)-C_{2 \varepsilon} \rho \frac{\varepsilon^{2}}{k}-R_{\varepsilon} \tag{5}
$$

where $v$ is the fluid velocity, $\rho$ is the material density, $p$ is the fluid pressure, $\mu$ is the dynamic viscosity, $\lambda$ is the material thermal conductivity, $c$ is the specific heat, $k$ is the turbulent kinetic energy, $G_{k}$ is the generation of turbulence kinetic energy caused by the mean velocity gradients, $G_{b}$ is the generation of turbulence kinetic energy caused by buoyancy, $\varepsilon$ is the turbulent dissipation rate, $Y_{M}$ is the contribution of the fluctuating dilatation, and $\alpha_{k}$ and $\alpha_{\varepsilon}$ represent the inverse effective Prandtl numbers for $k$ and $\varepsilon$, respectively. Besides, it should be noted that the material properties of air are temperature-dependent. Eq. (1) represents the mass conservation of fluid flow, Eq. (2) represents the momentum conservation of fluid flow, and Eq. (3) denotes the energy conservation. Eq. (4) and Eq. (5) are the transportation equations of the RNG $k-\varepsilon$ turbulent model.

Energy conservation is the primary governing equation when heat is transferred along the solid regions, including the heat exchanger and heat sink, steel connectors, and ceramic plates, which can be expressed as:

$$
\nabla \cdot(\lambda \nabla T)=0 \tag{6}
$$

In the p-type and n-type thermoelectric legs, the heat transfer includes not only the Fourier heat conduction, but also the Joule heat, Peltier heat, and Thomson heat. Therefore, the change of thermal energy caused by Fourier effect, Peltier effect, and Thomson effect should be included in the source term of the energy conservation differential equation [33], which is:

$$
\nabla \cdot\left(\lambda_{\mathrm{p}, \mathrm{n}}(T) \nabla T_{\mathrm{p}, \mathrm{n}}\right)+\sigma_{\mathrm{p}, \mathrm{n}}^{-1}(T) \vec{J}^{2}-\nabla \alpha_{\mathrm{p}, \mathrm{n}}(T) \vec{J} T_{\mathrm{p}, \mathrm{n}}=0 \tag{7}
$$

where $\lambda_{\mathrm{p}, \mathrm{n}}(T)$, $\sigma_{\mathrm{p}, \mathrm{n}}^{-1}(T)$, and $\alpha_{\mathrm{p}, \mathrm{n}}(T)$ are the thermal conductivity, electric resistivity, and Seebeck coefficient of thermoelectric materials, respectively. Subscripts p and n represent p-type and n-type legs, respectively. $\vec{J}$ represents the current density vector. In this study, the temperature dependence of thermoelectric materials is taken into consideration.

For copper electrode slices and load resistance, the term related to the Seebeck coefficient is absent, and the energy conservation can be defined as:

$$
\nabla \cdot(\lambda \nabla T)+\sigma^{-1} \vec{J}^{2}=0 \tag{8}
$$

As for the electric field, the governing equations [34] include:

$$
\vec{J}=\sigma \vec{E}=\sigma(-\nabla \phi+\alpha \nabla T) \tag{9}
$$

$$
\nabla \cdot \vec{J}=0 \tag{10}
$$

where $\vec{E}$ represents the electric field density vector, and $\phi$ represents the electric potential. Eq. (10) is used to define the continuity of the electric current.

### 2.3 Detailed solving methods and boundary conditions of different modeling approaches

The numerical model is one of the most effective methods to solve the above governing equations, and ANSYS [35, 36] and COMSOL Multiphysics [37, 38] are two widely used numerical analysis software programs to obtain the specific physical field distribution characteristics of TEG systems. In a previous study [11], the fluid-thermal-electric multiphysics model of the TEG system was regarded

as the combination of the fluid-thermal model and thermal-electric model, wherein the temperature distribution of TEMs solved by the fluid-thermal model was used as the temperature boundary condition of the thermal-electric model, and the output performance of the TEG system was obtained via the coupling simulation of ANSYS/Fluent and ANSYS/Thermal-Electric. However, the fluid, thermal, and electric fields are not computed at the same time in the study, which is not in line with the actual situation. For this reason, the purpose of the present study is to integrate the governing equations into the COMSOL Multiphysics and use the COMSOL coupled solver to conduct a more accurate and comprehensive fluid-thermal-electric multiphysics investigation on the TEG system. In the platform of COMSOL, the process of predicting the performance of the TEG system by ANSYS in Ref. [11] can also be realized by the COMSOL separate solver, where the fluid-thermal field of the TEG system is calculated first, then the thermal-electric field.

![](./images/811829752959598593_2.jpg)

Fig. 2. The differences of the fluid-thermal-electric multiphysics field coupling effect among different modeling approaches.

The differences of the fluid-thermal-electric multiphysics field coupling effect among different multiphysics modeling approaches are shown in Fig. 2. In the COMSOL coupled solver, all of the physical characteristics among different fields are taken into consideration, which is the most reasonable approach to solve the fluid-thermal-electric multiphysics model. In the ANSYS and

COMSOL separate solver, the influence of the parasitic heat induced by the Peltier effect, Joule effect, and Thomson effect on the fluid-thermal multiphysics is ignored. In essence, the parasitic heat first affects the temperature distributions in the heat exchanger and heat sink, then affects the fluid temperature, temperature-dependent material properties of air, and finally affects the turbulence and energy conservation of the fluid flow. In order to study the influence of parasitic heat on the fluid-thermal-electric multiphysics numerical model, numerical results predicted by the COMSOL coupled solver, ANSYS, and COMSOL separate solver are compared in the following sections.

On the surfaces of the TEG system exposed to the ambient air, the convective heat transfer boundary condition is defined as Eq. (11) with the natural convection heat transfer coefficient of $h_{\text{am}} = 15$ W/($\text{m}^2\text{·K}$) and the ambient temperature of 300 K. In addition, the hot air enters the flow channel of the heat exchanger at an inlet air velocity of $v_{\text{air}}$ and an inlet air temperature of $T_{\text{air}}$, and leaves at standard atmospheric pressure. The cooling water enters the flow channel of the heat sink at an inlet velocity of 7.04 m/s and an inlet temperature of 300 K and leaves at standard atmospheric pressure. Here, different values of $v_{\text{air}} = 20$ m/s, 30 m/s, 40 m/s, 50 m/s, and $T_{\text{air}} = 400$ K, 450 K, 500 K, 550 K are chosen for the numerical analysis to investigate the effect of different boundary conditions on these three modeling approaches. Both the convective heat transfer boundary condition and the fluid boundary condition in ANSYS are the same as those in COMSOL.

$$
-\lambda \frac{\partial T}{\partial n}=h_{\mathrm{am}}\left(T-T_{\mathrm{am}}\right) \tag{11}
$$

However, the TEM boundary conditions in the ANSYS simulation environment are different from those in the COMSOL simulation environment, as shown in Fig. 3. In ANSYS, all numerical simulations are performed via the coupling simulation of ANSYS/Fluent and ANSYS/Thermal-electric. The fluid-thermal multiphysics field of the TEG system is calculated by ANSYS/Fluent, and the primary temperature distribution of the TEG system is obtained. Then, the obtained temperature

distributions of the hot-side and cold-side surfaces of the TEM are taken as the temperature boundary condition of the TEM. By setting the grounded boundary and voltage coupling boundary, the output performance of the TEM can be predicted by solving the thermal-electric multiphysics field via ANSYS/Thermal-electric.

![](./images/811829752959598593_3.jpg)

Fig. 3. Boundary conditions of the thermoelectric module. (a) ANSYS simulation environment. (b) COMSOL simulation environment. A = grounded boundary (U=0V), B = voltage coupling boundary, C = cold side temperature distribution solved by the fluid-thermal multiphysics, D = hot side temperature distribution solved by the fluid-thermal multiphysics, E = ground boundary (U=0V).

In COMSOL, the boundary condition of the TEM only includes the grounded boundary, and the TEM is directly connected with load resistance through the surface contact. The only difference between COMSOL coupled solver and COMSOL separate solver is that the coupled solver calculates the fluid, thermal, and electric fields at the same time, while the separate solver first calculates the fluid-thermal coupling field, and then calculates the thermal-electric coupling field.

### 2.4 Grid independence examination

The output performance predicted by the fluid-thermal-electric multiphysics numerical model is

sensitive to the grid of the TEG system. Generally, the model accuracy increases with the increase of the number of grids, but the execution time also increases. The grid independence examination is required to select a reasonable grid system before numerical simulations. The grid system in the ANSYS simulation environment refers to the previous study [11], where the grid size of the TEM is 0.4 mm. The grid system of the TEG system in the COMSOL simulation environment is shown in Fig. 1(c). The grids in different computation regions are controlled by their specific physical fields. Four grid systems of grid i, grid ii, grid iii, and grid iv with the mesh number of 3368064, 1505411, 452940, and 194420, respectively are chosen to check the grid independence of the TEG system. Under the boundary conditions of $v_{air}=30$ m/s, $T_{air}=500$ K, and $R_{L}=4$ Ω, the output voltage and output power of the TEG system predicted by COMSOL coupled solver and separate solver are listed in Table 2. It can be seen that the errors of output voltage and output power decrease with the increase of grid number. For COMSOL coupled solver, grid i takes approximately 18 hours per calculation. To reduce the execution time and ensure reasonable accuracy, grid ii is used for numerical simulation.

<table>
<caption>Table 2. Output performance of the TEG system under different grid systems</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">Mesh number</th>
<th colspan="4">COMSOL coupled solver</th>
<th colspan="4">COMSOL separate solver</th>
</tr>
<tr>
<th>Output voltage (V)</th>
<th>Error of voltage</th>
<th>Output power (W)</th>
<th>Error of power</th>
<th>Output voltage (V)</th>
<th>Error of voltage</th>
<th>Output power (W)</th>
<th>Error of power</th>
</tr>
</thead>
<tbody>
<tr>
<td>Grid i</td>
<td>3368064</td>
<td>3.5049</td>
<td>-</td>
<td>3.0711</td>
<td>-</td>
<td>3.3609</td>
<td>-</td>
<td>2.8239</td>
<td>-</td>
</tr>
<tr>
<td>Grid ii</td>
<td>1505411</td>
<td>3.5057</td>
<td>0.02%</td>
<td>3.0725</td>
<td>0.05%</td>
<td>3.3617</td>
<td>0.02%</td>
<td>2.8252</td>
<td>0.05%</td>
</tr>
<tr>
<td>Grid iii</td>
<td>452940</td>
<td>3.5111</td>
<td>0.18%</td>
<td>3.0820</td>
<td>0.35%</td>
<td>3.3669</td>
<td>0.18%</td>
<td>2.8340</td>
<td>0.36%</td>
</tr>
<tr>
<td>Grid iv</td>
<td>194420</td>
<td>3.5154</td>
<td>0.30%</td>
<td>3.0895</td>
<td>0.60%</td>
<td>3.3721</td>
<td>0.33%</td>
<td>2.8428</td>
<td>0.67%</td>
</tr>
</tbody>
</table>

### 3. Comparison of different multiphysics modeling approaches

#### 3.1 Numerical results predicted by ANSYS and COMSOL

Fig. 4 shows the numerical results of the TEG system predicted by ANSYS and COMSOL coupled solver at $v_{air}=30$ m/s, $T_{air}=500$ K, and $R_{L}=4$ Ω. Both the temperature distribution and voltage distribution predicted by ANSYS are almost similar to those predicted by COMSOL coupled solver.

According to Figs 4(a) and (c), the temperature drop from air to the hot side of the heat exchanger is obviously higher than the temperature rise from the water to heat sink, because the specific heat of air is lower than that of water. Moreover, there is a great temperature difference between the hot side and cold side of the TEM, which makes the carriers in thermoelectric materials migrate from the hot side to the cold side, thus generating a Seebeck voltage. The Seebeck voltage is proportional to the temperature difference on both sides of thermoelectric legs. Therefore, effective ways to enhance the output performance of the TEG system include increasing the hot-side temperature, reducing the cold-side temperature, and lowering the thermal conductivity of thermoelectric materials.

![](./images/811829752959598593_4.jpg)

Fig. 4. Numerical results predicted by ANSYS and COMSOL coupled solver at $v_{\mathrm{air}}$=30m/s, $T_{\mathrm{air}}$=500K, and $R_{\mathrm{L}}$=4Ω. (a) Temperature distribution of TEG system predicted by ANSYS; (b) Voltage distribution of TEM predicted by ANSYS; (c) Temperature distribution of TEG system predicted by COMSOL coupled solver; (d) Voltage distribution of TEM predicted by COMSOL coupled solver.

The voltage distributions of the TEM predicted by ANSYS and COMSOL coupled solver are shown in Figs 4(b) and (d), respectively. The electric potential increases from cathode to anode. In practical application, TEMs are usually connected with an energy recovery circuit to store the generated electricity, and the output voltage of the TEM can be obtained by measuring the end voltage of load

resistance. Here, the output voltage predicted by ANSYS and COMSOL coupled solver is 3.49 V and 3.51 V respectively. The reasons for this difference can be attributed to the neglect of the effect of parasitic heat caused by the Peltier effect, Joule effect and Thomson effect on the fluid-thermal field in ANSYS, as well as the difference of differential equation solver between ANSYS and COMSOL.

Theoretically, the COMSOL coupled solver calculates the fluid, thermal, and electric fields at the same time, which can predict more reasonable results. In the following chapters, we will further discuss the reasons for this difference and study the influence of boundary conditions on it.

![](./images/811829752959598593_5.jpg)

Fig. 5. Detailed numerical results of the TEM predicted by COMSOL coupled solver. (a) Temperature distribution of the whole TEM; (b) Hot-side temperature distribution of the TEM; (c) Cold-side temperature distribution of the TEM; (d) Voltage distribution of the TEM.

Fig. 5 shows the detailed temperature and voltage distributions of the TEM predicted by COMSOL coupled solver. According to Fig. 5(a), the temperature of load resistance is the highest due to the Joule effect, and the generated Joule heat is equal to the output power of the TEM. The temperature drop of the whole TEM mainly occurs in thermoelectric legs, and the temperature difference on both ends of legs is about 135 K. However, when the heat is transferred from the hot air to the heat exchanger, then

to the hot side of the TEM, or from the cold side of the TEM to the heat sink, then to the cooling water, the temperature distribution on both sides of legs is not uniform. And thus, the generated current among different legs will be different due to the uneven temperature difference, causing the current limitation of the whole TEM. The hot-side temperature distribution and the cold-side temperature distribution of the TEM are shown in Figs 5(b) and (c), respectively. The hot-side temperature of legs fluctuates from 438 K to 445 K, while the cold-side temperature of legs is almost fixed at 307.5 K, which is also caused by the different specific heat capacities of air and water. One of the most effective methods to address the current limitation problem is to adjust the cross-sectional area of each thermoelectric leg according to its specific temperature difference [11]. The detailed voltage distribution of TEM is shown in Fig. 5(d). The output power of TEM can be estimated by $P=U^{2}/R_{\text{L}}$. The output voltage is 3.51 V at the load resistance of 4$\Omega$, and thus the output power is 3.07 W. When the TEM is working at a temperature difference, the parasitic internal resistance exists in the thermoelectric legs [39], and it is necessary to study the load response characteristics of the TEM under different load resistances.

### 3.2 Output performance of the thermoelectric generator system at constant boundary conditions

To study the influence of different multiphysics modeling approaches, including ANSYS, COMSOL coupled solver, and COMSOL separate solver, on the output performance of the TEG system, the output voltage and output power as a function of current under the constant boundary conditions of $v_{\text{air}} = 30$ m/s and $T_{\text{air}} = 500$ K are obtained, as shown in Fig. 6(a). As can be seen, the output voltage decreases linearly with the increase of current. The output power is parabolic with the current. Both output voltage and output power predicted by COMSOL separate solver are lower than those predicted by ANSYS. In essence, the solution process of the fluid-thermal-electric multiphysics numerical model in ANSYS is the same as that in COMSOL separate solver, where the fluid-thermal multiphysics coupling field is computed first, then the thermal-electric multiphysics coupling field.

The reason why there is a greater output performance in ANSYS is that the solution of partial differential equations in ANSYS/Fluent is based on the finite volume method, while the solution in COMSOL is based on the finite element method. When solving the thermal-electric field in ANSYS, the surface temperature distribution on both sides of the TEM is used, while in COMSOL, the temperature distribution of the whole three-dimensional geometry is used.

![](./images/811829752959598593_6.jpg)

Fig. 6. Output performance of the TEG system at constant boundary conditions. (a) Output voltage and output power as a function of current at $v_{\text{air}}$=30m/s and $T_{\text{air}}$=500K. (b) Peltier heat under different load resistances predicted by different multiphysics modeling approaches.

Through the comparison of output performance between COMSOL coupled solver and separate solver, it can be noticed that the separate solver predicts a lower output performance than the coupled solver, which means the effect of parasitic heat on the fluid-thermal multiphysics coupling field can not be ignored. The neglect of the influence of parasitic heat caused by the Peltier effect, Thomson effect, and Joule effect on the fluid-thermal multiphysics coupling field will lead to a lower estimation of output performance when solving the fluid-thermal-electric multiphysics numerical model of the TEG system.

The output power predicted by COMSOL coupled solver is higher than that predicted by ANSYS when $I \leq$1A , and it is opposite for $I \geq$1A , which may be caused by the difference of internal resistance. The absolute value of the slope of the $U$-$I$ curve represents the internal resistance value of

the TEM. The internal resistance of the TEM predicted by COMSOL coupled solver is about 4.25 $\Omega$, which is higher than 4.03 $\Omega$ predicted by ANSYS and 3.91 $\Omega$ predicted by COMSOL separate solver.

The reason for this is caused by the neglect of the influence of parasitic heat on the fluid-thermal multiphysics coupling field in ANSYS and COMSOL separate solver. Combined with the electrical resistivity of thermoelectric material in Table 1 and the hot-side and cold-side temperature distributions of legs in Fig. 5, the real internal resistance can be defined as:

$$
R_{\text{in}}=N \times \frac{h_{\text{leg}}}{A_{\text{leg}}} \times\left( \frac{\int_{T_{\text{c\_p}}}^{T_{\text{h\_p}}} \sigma_{\text{p}}^{-1}(T) d T}{T_{\text{h\_p}}-T_{\text{c\_p}}}+\frac{\int_{T_{\text{c\_n}}}^{T_{\text{h\_n}}} \sigma_{\text{n}}^{-1}(T) d T}{T_{\text{h\_n}}-T_{\text{c\_n}}} \right) \tag{12}
$$

where $N$ is the number of p-type or n-type thermoelectric legs, $h_{\text{leg}}$ and $A_{\text{leg}}$ are respectively the height and cross-sectional area of legs, $T_{\text{h\_p}}$ ($T_{\text{h\_n}}$) and $T_{\text{c\_p}}$ ($T_{\text{c\_n}}$) are respectively the mean temperature of hot-side and cold-side surface temperature of p-type (n-type) legs.

After a simple calculation, the real internal resistance of $R_{\text{in}}=3.89 \Omega$ is obtained. It can be noticed that the internal resistance predicted by the fluid-thermal-electric multiphysics numerical model is higher than the real internal resistance of the TEM because the parasitic internal resistance exists in thermoelectric legs, especially for the situation of COMSOL coupled solver. According to Ref. [39], the parasitic internal resistance is directly related to the Peltier effect. However, the effect of parasitic heat caused by the Peltier effect, Thomson effect, and Joule effect on the fluid-thermal multiphysics coupling field is not considered in ANSYS and COMSOL separate solver.

To further study the effect of parasitic heat on the fluid-thermal-electric multiphysics numerical model, Peltier heat of thermoelectric units under different load resistances is obtained, as shown in Fig. 6(b). The hot-side Peltier heat is estimated by $\alpha IT_{\text{h}}$, and the cold-side Peltier heat is estimated by $\alpha IT_{\text{c}}$. Both the hot-side and cold-side Peltier heat predicted by COMSOL separate solver keep the same changing trend as those predicted by ANSYS due to the almost same solution process, however,

the situation for COMSOL coupled solver is quite different. More reasonably, the fluid, thermal, and electric fields should be computed at the same time, and the effect of parasitic heat on the fluid-thermal multiphysics coupling field should not be ignored. According to the above analysis, it can be concluded that the fluid-thermal-electric multiphysics numerical model using COMSOL coupled solver can predict more reasonable results, compared with that using ANSYS and COMSOL separate solver. In addition, the Peltier heat estimated by COMSOL coupled solver is quite different from that by ANSYS and COMSOL separate solver, causing the difference of parasitic internal resistance.

### 3.3 Effect of inlet air temperature on the output performance with different multiphysics modeling approaches

The output characteristics of the TEG system are highly sensitive to the boundary conditions of hot fluid, including inlet temperature and inlet velocity. Also, the boundary conditions may lead to the difference in numerical results among different multiphysics modeling approaches. For this reason, the effect of boundary conditions on the output performance of the TEG system with different multiphysics modeling approaches is studied. Fig. 7(a) shows the output voltage as a function of current at different inlet air temperatures. Here, the inlet air velocity is fixed at 30 m/s. It can be observed that the changing trend of voltage predicted by ANSYS is consistent with that predicted by COMSOL separate solver, and the inlet air temperature has little effect on the difference of parasitic internal resistances between ANSYS and COMSOL separate solver. When the temperature decreases from 550 K to 400 K, the absolute value of the curve slope obtained by ANSYS decreases from 4.07 to 3.79, and that by COMSOL coupled solver decreases from 4.29 to 4.03. The reason for this is that the Peltier heat decreases with the decrease in temperature, causing a decrease in parasitic internal resistance. Besides, the output voltage obtained by COMSOL coupled solver is larger than that by ANSYS when $T_{\text{air}} = 550$ K, whereas it is lower than that by ANSYS when $T_{\text{air}} = 400$ K. Compared with numerical results predicted by ANSYS and COMSOL separate solver, the inlet air temperature

has a greater influence on those predicted by COMSOL coupled solver. It seems that the influence of inlet air temperature on the output performance of the TEG system will be underestimated by ANSYS.

![](./images/811829752959598593_7.jpg)

Fig. 7. Effects of air temperature and velocity on the output performance of the TEG system with different multiphysics modeling approaches. (a) Output voltage as a function of current at different inlet air temperatures. (b) Output power as a function of load resistance at different inlet air temperatures. (c) Output power as a function of current at different inlet air velocities. (d) Output power as a function of load resistance at different inlet air velocities.

Fig. 7(b) shows the output power as a function of load resistance at different inlet air temperatures.

Obviously, the load resistance at the maximum output power predicted by COMSOL coupled solver is larger than those predicted by the other two modeling approaches, due to the underestimation of parasitic internal resistance in ANSYS and COMSOL separate solver. The output power of the TEG system predicted by COMSOL coupled solver is on average 2.18% higher than that by ANSYS, and 8.52% higher than that by COMSOL separate solver at the inlet air temperature of 550 K. Besides, the output power of the TEG system predicted by COMSOL coupled solver is on average 3.16% lower than that by ANSYS, and 9.59% higher than that by COMSOL separate solver at the inlet air

temperature of 400K. There are two main reasons for this contradiction between ANSYS and COMSOL coupled solver: i) The solution of partial differential equations in ANSYS/Fluent is based on the finite volume method, while the solution in COMSOL is based on the finite element method; ii) The neglect of parasitic heat in ANSYS causes the underestimation of parasitic internal resistance of the TEM. With the increase of inlet air temperature, the output power predicted by ANSYS is larger than that predicted by COMSOL coupled solver at first, and then becomes smaller than that predicted by COMSOL coupled solver. Through the comparison between COMSOL coupled solver and separate solver, it can be concluded that the neglect of the effect of parasitic heat on the fluid-thermal field will induce the underestimation of output performance of the TEG system. Through the comparison between ANSYS and COMSOL separate solver, it can be concluded that the performance of the TEG system predicted by the finite volume method is higher than that predicted by the finite element method. When $R_{\mathrm{L}}=4\ \Omega$ and $v_{\mathrm{air}}=30\ \mathrm{m/s}$, with the increase of air temperature from 400 K to 550 K, the output power of the TEG system predicted by ANSYS, COMSOL separate solver, and COMSOL coupled solver increases from 0.83 W to 4.52 W, 0.73 W to 4.23 W, and 0.80 W to 4.61 W, respectively, increasing by 445.33%, 476.17%, and 475.37% respectively. The results show that the output performance of the TEG system predicted by ANSYS is less affected by inlet air temperature than that predicted by COMSOL.

### 3.4 Effect of inlet air velocity on the output performance with different multiphysics modeling approaches

The fluid velocity has a great influence on the turbulent flow of hot air and affects the output performance of the TEG system. For this reason, the effect of inlet air velocity on the output performance of the TEG system with different multiphysics modeling approaches is investigated. The output voltage as a function of current at different inlet air velocities is shown in Fig. 7(c). Here, the inlet air temperature is fixed at 500 K. With the increase of velocity, the distance of the $U$-$I$ curve

between ANSYS and COMSOL separate solver becomes smaller under the same condition; The $U$-$I$ curve of COMSOL coupled solver is obviously below the $U$-$I$ curve of ANSYS at $v_{\text{air}} = 20$ m/s, whereas it is opposite for $v_{\text{air}} = 50$ m/s. The reason for this can be attributed to the different solving mechanisms between ANSYS and COMSOL, as well as the great influence of fluid velocity on the computation of fluid flow. On the other hand, the slope of these curves almost remains unchanged regardless of the change of inlet air velocity because the Peltier heat is directly related to the temperature but not the fluid velocity.

Fig. 7(d) shows the output power as a function of load resistance at different inlet air velocities. When the inlet air velocity is 20 m/s, the output power of the TEG system predicted by ANSYS is on average 3.28% and 12.13% higher than that by COMSOL coupled solver and separate solver respectively. However, when the inlet air velocity is 50 m/s, the output power of the TEG system predicted by ANSYS is on average 3.87% lower than that predicted by COMSOL coupled solver, and 3.28% higher than that predicted by COMSOL separate solver. The contradiction between ANSYS and COMSOL coupled solver can also be explained by the different numerical solution methods and the neglect of parasitic heat in ANSYS. When $R_{\text{L}} = 4\ \Omega$ and $T_{\text{air}} = 500$ K, with the increase of inlet air velocity from 20 m/s to 50 m/s, the output power of the TEG system predicted by ANSYS, COMSOL separate solver, and COMSOL coupled solver increases from 2.78 W to 3.35 W, 2.44 W to 3.22 W, and 2.68 W to 3.47 W, respectively, increasing by 20.58%, 31.80%, and 29.56% respectively. The results show that the output performance of the TEG system predicted by ANSYS is less affected by inlet air velocity than that predicted by COMSOL, and the error between ANSYS and COMSOL coupled solver is mainly affected by the different solving mechanisms of software, followed by the parasitic heat. Theoretically, when ignoring the effect of parasitic heat on the fluid-thermal field, the fluid-thermal-electric multiphysics numerical model of the TEG system will predict an unreasonably low output performance and a low parasitic internal resistance, but for the numerical simulation

through ANSYS, the obtained output power may be higher than the output power predicted by COMSOL coupled solver because of the different solving mechanisms between ANSYS and COMSOL.

### 3.5 Experimental validation

![](./images/811829752959598593_8.jpg)

Fig. 8. Comparison of output performance of TEG system between model results and experimental results.

Luo et al.'s experimental data [11] are used to examine the model accuracy of different fluid-thermal-electric multiphysics modeling approaches. Fig. 8 compares the measurement data regarding the output voltage and output power with numerical predictions by present models at the inlet air temperature of 500 K and inlet air mass flow rate of 40 g/s. In the present work, the inlet air velocity boundary is adopted, and the inlet air velocity of 45.67 m/s is determined according to the mass flow rate of 40 g/s. According to the comparison between numerical results and experimental data, the average error of output voltage for COMSOL coupled solver, ANSYS, and COMSOL separate solver is about 1.42%, 2.55%, and 5.24%, respectively, and that of output power is about 2.81%, 5.03%, and 10.21%, respectively. It is obvious that the fluid-thermal-electric multiphysics numerical model predicted by COMSOL coupled solver shows a greater accuracy than the other two modeling approaches. The experimental data are slightly higher than numerical results, which may be caused by the measurement error during the test.

In summary, the fluid-thermal-electric multiphysics numerical model using COMSOL coupled solver is the most reasonable approach to predict the performance of the TEG system, because the fluid, thermal, and electric fields are computed at the same time, and the effect of parasitic heat on the fluid-thermal multiphysics coupling field is taken into consideration, which is in line with the practical situation. In comparison with the model results of COMSOL separate solver, it can be concluded that the fluid-thermal-electric multiphysics numerical model may predict an unreasonably low output performance and a low parasitic internal resistance when the fluid-thermal field is computed first, and then the thermal-electric field. However, due to the different solving mechanisms of ANSYS, compared with COMSOL coupled solver, the multiphysics model established by ANSYS may predict higher output performance when the inlet air temperature and inlet air velocity remain at a relatively low level, and vice versa. Although the same solution process between ANSYS and COMSOL separate solver, ANSYS can predict a higher output performance of the TEG system. It seems that there is a specific range of air temperature and air velocity, which makes the numerical results of ANSYS and COMSOL coupled solver have a good agreement. Besides, air temperature and air velocity have a greater influence on the numerical results of COMSOL than those on the numerical results of ANSYS.

## 4. Conclusions

In this work, a fluid-thermal-electric multiphysics numerical model was disclosed to predict the output performance of the TEG system, wherein the fluid, thermal, and electric fields are computed at the same time through COMSOL coupled solver. The comparison between COMSOL coupled solver and ANSYS was performed in the present work to investigate the effect of the neglect of parasitic heat on the fluid-thermal-electric multiphysics numerical model. Nevertheless, the solution of partial differential equations in COMSOL is based on the finite element method, while ANSYS/Fluent is based on the finite volume method, which may affect the model accuracy between COMSOL coupled

solver and ANSYS. And thus, the numerical modeling approach using COMSOL separate solver, with the same solution process as ANSYS, was included in the comparison to investigate the effect of different solving mechanisms on the numerical results. Considering the sensitivity of the inlet air boundary conditions to numerical results, the effects of inlet temperature and inlet velocity on the model accuracy among different modeling approaches were also studied. The following conclusions can be drawn through the comparison of numerical results predicted by COMSOL coupled solver, ANSYS, and COMSOL separate solver at various boundary conditions:

(1) The fluid-thermal-electric multiphysics numerical model, predicted by COMSOL coupled solver, is the most effective method to predict the output performance of TEG system, and the proposed model can generate highly precise numerical results with the consideration of the effect of parasitic heat on the fluid-thermal multiphysics coupling field, wherein the fluid, thermal, and electric fields are computed at the same time.

(2) When ignoring the effect of parasitic heat, caused by the Peltier effect, Joule effect, and Thomson effect, on the fluid-thermal field, the fluid-thermal-electric multiphysics numerical model predicted by COMSOL separate solver will generate an unreasonably low output power, which is 8.52% lower than the output power predicted by COMSOL coupled solver at the inlet air temperature of 550 K and the inlet air velocity of 30 m/s. Besides, it will cause the low prediction of parasitic internal resistance of the thermoelectric module and cause the unreasonable prediction of the maximum power point.

(3) Although the same solution process with COMSOL separate solver, ANSYS may predict a higher or a lower output performance than COMSOL coupled solver, which is highly affected by the inlet air boundary conditions. The output power predicted by ANSYS will be higher than that by COMSOL coupled solver when the inlet air temperature and velocity remain at a relatively low level, and vice versa. It seems that there is a specific range of air temperature and air velocity, which makes the numerical results of ANSYS and COMSOL coupled solver have a good agreement.

(4) With the increase of air temperature from 400 K to 550 K ($R_{\mathrm{L}}=4\ \Omega$ and $v_{\mathrm{air}}=30\ \mathrm{m/s}$) and air velocity from 20 m/s to 50 m/s ($R_{\mathrm{L}}=4\ \Omega$ and $T_{\mathrm{air}}=500\ \mathrm{K}$), the output power of the TEG system predicted by ANSYS, COMSOL separate solver, and COMSOL coupled solver is increased by 445.33%, 476.17%, 475.37%, and 20.58%, 31.80%, 29.56%, respectively. The output performance of the TEG system predicted by ANSYS is less affected by inlet air temperature and air velocity than that predicted by COMSOL.

(5) Through the experimental validation, the minimum output voltage error of 1.42% and the minimum output power error of 2.81% are reached between the numerical results predicted by COMSOL coupled solver and experimental data. The proposed fluid-thermal-electric multiphysics numerical model can be extended from the TEG system containing one TEM to the TEG system containing multiple TEMs, providing a novel insight for modeling the whole TEG system.

### Acknowledgements
The authors are grateful for the financial support from the National Natural Science Foundation of China (51977100), EU ThermaSMART project under Grant No. H2020-MSCA-RISE (778104), as well as Ningbo Science and Technology Bureau's Technology under Grant No. 2019B10042. D. Luo acknowledges the financial support from China Scholarship Council (CSC).

### References
[1] He W, Tao L, Han L, Sun Y, Campana PE, Yan J. Optimal analysis of a hybrid renewable power system for a remote island. Renewable Energy 2021;179:96-104.

[2] Ziolkowski A. Automotive Thermoelectric Generator impact on the efficiency of a drive system with a combustion engine. MATEC Web Conf. 2017;118.

[3] Twaha S, Zhu J, Yan Y, Li B. A comprehensive review of thermoelectric technology: Materials,

applications, modelling and performance improvement. Renewable Sustainable Energy Rev 2016;65:698-726.

[4] Shu G, Shi L, Tian H, Deng S, Li X, Chang L. Configurations selection maps of CO2-based transcritical Rankine cycle (CTRC) for thermal energy management of engine waste heat. Appl Energy 2017;186:423-35.

[5] Tian H, Chang L, Gao Y, Shu G, Zhao M, Yan N. Thermo-economic analysis of zeotropic mixtures based on siloxanes for engine waste heat recovery using a dual-loop organic Rankine cycle (DORC). Energy Convers Manage 2017;136:11-26.

[6] Zhao Y, Wang S, Ge M, Liang Z, Liang Y, Li Y. Performance investigation of an intermediate fluid thermoelectric generator for automobile exhaust waste heat recovery. Appl Energy 2019;239:425-33.

[7] Ge M, Li Z, Wang Y, Zhao Y, Zhu Y, Wang S, et al. Experimental study on thermoelectric power generation based on cryogenic liquid cold energy. Energy. 2021;220:119746.

[8] Crane D, LaGrandeur J, Jovovic V, Ranalli M, Adldinger M, Poliquin E, et al. TEG On-Vehicle Performance and Model Validation and What It Means for Further TEG Development. J Electron Mater 2013;42:1582-91.

[9] Risseh AE, Nee H-P, Goupil C. Electrical Power Conditioning System for Thermoelectric Waste Heat Recovery in Commercial Vehicles. IEEE Transactions on Transportation Electrification. 2018;4:548-62.

[10] Champier D. Thermoelectric generators: A review of applications. Energy Convers Manage 2017;140:167-81.

[11] Luo D, Wang R, Yu W, Zhou W. A novel optimization method for thermoelectric module used in waste heat recovery. Energy Convers Manage 2020;209:112645.

[12] Li B, Huang K, Yan Y, Li Y, Twaha S, Zhu J. Heat transfer enhancement of a modularised

thermoelectric power generator for passenger vehicles. Appl Energy 2017;205:868-79.

[13] Liu C, Deng YD, Wang XY, Liu X, Wang YP, Su CQ. Multi-objective optimization of heat exchanger in an automotive exhaust thermoelectric generator. Appl Therm Eng 2016;108:916-26.

[14] Hsiao YY, Chang WC, Chen SL. A mathematic model of thermoelectric module with applications on waste heat recovery from automobile engine. Energy. 2010;35:1447-54.

[15] Huang G-Y, Hsu C-T, Fang C-J, Yao D-J. Optimization of a waste heat recovery system with thermoelectric generators by three-dimensional thermal resistance analysis. Energy Convers Manage 2016;126:581-94.

[16] Luo D, Wang R, Yu W. Comparison and parametric study of two theoretical modeling approaches based on an air-to-water thermoelectric generator system. J Power Sources 2019;439:227069.

[17] Kempf N, Zhang Y. Design and optimization of automotive thermoelectric generators for maximum fuel efficiency improvement. Energy Convers Manage 2016;121:224-31.

[18] He W, Wang S, Zhang X, Li Y, Lu C. Optimization design method of thermoelectric generator based on exhaust gas parameters for recovery of engine waste heat. Energy. 2015;91:1-9.

[19] Fernández-Yañez P, Armas O, Capetillo A, Martínez-Martínez S. Thermal analysis of a thermoelectric generator for light-duty diesel engines. Appl Energy 2018;226:690-702.

[20] Kim TY, Kwak J, Kim B-w. Energy harvesting performance of hexagonal shaped thermoelectric generator for passenger vehicle applications: An experimental approach. Energy Convers Manage 2018;160:14-21.

[21] Zhang Y. Thermoelectric Advances to Capture Waste Heat in Automobiles. ACS Energy Letters. 2018;3:1523-4.

[22] Chen W-H, Liao C-Y, Hung C-I, Huang W-L. Experimental study on thermoelectric modules for power generation at various operating conditions. Energy. 2012;45:874-81.

[23] Aranguren P, Astrain D, Rodríguez A, Martínez A. Experimental investigation of the applicability of a thermoelectric generator to recover waste heat from a combustion chamber. Appl Energy 2015;152:121-30.

[24] Chen W-H, Lin Y-X, Chiou Y-B, Lin Y-L, Wang X-D. A computational fluid dynamics (CFD) approach of thermoelectric generator (TEG) for power generation. Appl Therm Eng 2020;173:115203.

[25] Luo D, Wang R, Yu W, Zhou W. Parametric study of a thermoelectric module used for both power generation and cooling. Renewable Energy 2020;154:542-52.

[26] Chen W-H, Liao C-Y, Hung C-I. A numerical study on the performance of miniature thermoelectric cooler affected by Thomson effect. Appl Energy 2012;89:464-73.

[27] Luo D, Wang R, Yu W, Zhou W. A numerical study on the performance of a converging thermoelectric generator system used for waste heat recovery. Appl Energy 2020;270:115181.

[28] Wang Y, Dai C, Wang S. Theoretical analysis of a thermoelectric generator using exhaust gas of vehicles as heat source. Appl Energy 2013;112:1171-80.

[29] He W, Guo R, Liu S, Zhu K, Wang S. Temperature gradient characteristics and effect on optimal thermoelectric performance in exhaust power-generation systems. Appl Energy 2020;261:114366.

[30] Wang Y, Li S, Xie X, Deng Y, Liu X, Su C. Performance evaluation of an automotive thermoelectric generator with inserted fins or dimpled-surface hot heat exchanger. Appl Energy 2018;218:391-401.

[31] Massaguer A, Massaguer E, Comamala M, Pujol T, González JR, Cardenas MD, et al. A method to assess the fuel economy of automotive thermoelectric generators. Appl Energy 2018;222:42-58.

[32] Young DF, Munson BR, Okiishi TH, Huebsch WW. A brief introduction to fluid mechanics: John

Wiley & Sons; 2010.

[33] Chen W-H, Wu P-H, Lin Y-L. Performance optimization of thermoelectric generators designed by multi-objective genetic algorithm. Appl Energy 2018;209:211-23.

[34] Luo D, Yan Y, Wang R, Zhou W. Numerical investigation on the dynamic response characteristics of a thermoelectric generator module under transient temperature excitations. Renewable Energy 2021;170:811-23.

[35] Nithyanandam K, Mahajan RL. Evaluation of metal foam based thermoelectric generators for automobile waste heat recovery. Int J Heat Mass Transfer 2018;122:877-83.

[36] Bai W, Yuan X, Liu X. Numerical investigation on the performances of automotive thermoelectric generator employing metal foam. Appl Therm Eng 2017;124:178-84.

[37] Luo D, Wang R, Yan Y, Yu W, Zhou W. Transient numerical modelling of a thermoelectric generator system used for automotive exhaust waste heat recovery. Appl Energy 2021;297:117151.

[38] Yan S-R, Moria H, Asaadi S, Sadighi Dizaji H, Khalilarya S, Jermsittiparsert K. Performance and profit analysis of thermoelectric power generators mounted on channels with different cross-sectional shapes. Appl Therm Eng 2020:115455.

[39] Luo D, Wang R, Yu W, Zhou W. Parametric study of asymmetric thermoelectric devices for power generation. Int J Energy Res 2020:1-14.