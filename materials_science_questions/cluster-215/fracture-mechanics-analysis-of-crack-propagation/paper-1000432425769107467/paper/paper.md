![](./images/1000432425769107467_1.jpg)

# Structure and Infrastructure Engineering
Maintenance, Management, Life-Cycle Design and Performance

ISSN: (Print) (Online) Journal homepage: www.tandfonline.com/journals/nsie20

## Linear and nonlinear axial behaviour of internal replacement pipe systems for pipeline rehabilitation

Hamid Ahmadi, Ahmad Salah, Allan Manalo, Patrick G. Dixon, Warna Karunasena, Cam Minh Tri Tien, Shanika Kiriella, Thomas D. O'Rourke & Brad P. Wham

To cite this article: Hamid Ahmadi, Ahmad Salah, Allan Manalo, Patrick G. Dixon, Warna Karunasena, Cam Minh Tri Tien, Shanika Kiriella, Thomas D. O'Rourke & Brad P. Wham (21 May 2024): Linear and nonlinear axial behaviour of internal replacement pipe systems for pipeline rehabilitation, Structure and Infrastructure Engineering, DOI: 10.1080/15732479.2024.2356673

To link to this article: https://doi.org/10.1080/15732479.2024.2356673

![](./images/1000432425769107467_2.jpg)
© 2024 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group

![](./images/1000432425769107467_3.jpg)
Published online: 21 May 2024.

![](./images/1000432425769107467_4.jpg)
Submit your article to this journal ↗

![](./images/1000432425769107467_5.jpg)
View related articles ↗

![](./images/1000432425769107467_6.jpg)
View Crossmark data ↗

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=nsie20

STRUCTURE AND INFRASTRUCTURE ENGINEERING
https://doi.org/10.1080/15732479.2024.2356673

![](./images/1000432425769107467_7.jpg)

& OPEN ACCESS
![](./images/1000432425769107467_8.jpg)

# Linear and nonlinear axial behaviour of internal replacement pipe systems for pipeline rehabilitation

Hamid Ahmadi⁸, Ahmad Salah⁸, Allan Manalo⁸, Patrick G. Dixonᵇ, Warna Karunasena⁸, Cam Minh Tri Tien⁸,
Shanika Kiriella⁸, Thomas D. O'Rourkeᶜ and Brad P. Whamᵇ

⁸Centre for Future Materials, University of Southern Queensland, Toowoomba, QLD, Australia; ᵇCenter for Infrastructure, Energy, and Space Testing, University of Colorado Boulder, Boulder, CO, USA; ᶜSchool of Civil and Environmental Engineering, Cornell University, Ithaca, NY, USA

## ABSTRACT
Internal replacement pipe (IRP) is an innovative trenchless technology for the rehabilitation of legacy steel and cast-iron pipelines. This advanced IRP system must be properly designed so that it can safely and effectively restore the service of damaged pipelines. This paper studies the axial behaviour of IRP systems for repairing pipelines with circumferential host-pipe discontinuities under seasonal and extreme levels of temperature change. Analytical solutions along with a total of 270 linear and nonlinear finite element (FE) simulations, validated against experimental results and available closed-form solutions, were used for a parametric study on the effects of geometrical and material properties on axial stresses and deformations of IRP systems subjected to temperature change. Effects of the internal pressure, material and geometric nonlinearities, and different modes of IRP-host pipe unbonding were also investigated. An analytical model was developed for the prediction of temperature change induced loading and response of the IRP system. Using the results obtained from a comprehensive FE-based parametric study, three modification factors were extracted for the application to the developed analytical model in order to accurately predict the maximum axial stress of IRP and the opening of a circumferential host-pipe discontinuity subjected to various levels of temperature change.

## ARTICLE HISTORY
Received 19 June 2023
Revised 12 February 2024
Accepted 13 February 2024

## KEYWORDS
Gas pipeline; internal replacement pipe system; trenchless repair; finite element modelling; thermal load; axial response

## 1. Introduction
Pipelines play a vital role in satisfying the increasing global need for natural gas, recognized for its cleaner combustion compared to coal and oil. Therefore, maintaining the operational safety and reliability of this infrastructure is essential to ensure that natural gas remains a significant component of the global energy blend. Although gas pipelines provide a safe and reliable means of transporting natural gas from production sites to distribution networks and end users, they may experience damage over time because of a variety of actions, such as wear and tear (Shou & Chen, 2018), corrosion (Wang, Teh, & Li, 2022; Xiang & Zhou, 2020), and external forces such as earthquakes or landslides (Garmabaki, Marklund, Thaduri, Hedström, & Kumar, 2020). To address these issues, pipeline operators often engage in rehabilitation efforts that are designed to identify and address potential problems before they become more serious (Iqbal, Tesfamariam, Haider, & Sadiq, 2017).

Trenchless methods for the rehabilitation of pipelines are techniques that allow for the repair or replacement of pipelines without the need for extensive excavation (Lu et al., 2020a; Xin, 2014). These methods offer several advantages over traditional excavation-based methods including reduced disruption to the surrounding environment especially in densely inhabited regions (Lueke & Ariaratnam, 2001), quicker completion durations, and reduced overall expenses (Francom, El Asmar, & Ariaratnam, 2014; Jeyapalan, 2000; Li et al., 2023). Additionally, they can often be used to rehabilitate pipelines in difficult-to-reach areas or locations with limited access (Chin & Lee, 2005), making them a valuable tool for pipeline operators and municipalities seeking to maintain their infrastructure in a cost-effective and environmentally sustainable way (Fuselli, Huber, & Mambretti, 2022; Jung & Sinha, 2007).

Over the past few years, there have been significant advancements in trenchless repair technologies, especially with the implementation of internal replacement pipe (IRP) systems made of metallic components, polymers, and composite materials (Fu et al., 2022; Yu, Kim, Hwang, & Lee, 2008). The utilization of IRP has great potential as a trenchless approach for the rehabilitation of legacy bare-steel and cast-iron pipelines. Yet, the absence of established design procedures and standards for these technologies restricts their application in gas pipelines. Hence, it is imperative to investigate the structural performance of emerging IRP systems under applied loads and devise efficient designs to

---

CONTACT Hamid Ahmadi
hamid.ahmadi@unisq.edu.au

© 2024 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives License (http://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited, and is not altered, transformed, or built upon in any way.
The terms on which this article has been published allow the posting of the Accepted Manuscript in a repository by the author(s) or with their consent.

utilize them as internal repair systems for gas pipeline rehabilitation.

Nine major performance objectives have been identified by Dixon et al. (2023b) for the effective design of legacy gas pipelines with pipe-in-pipe (PIP) repair technology: cyclic surface load during service (Ha, Lee, & Kang, 2016; Wang, Wang, Xu, Zhong, & Li, 2019), lateral deformation (Kiriella et al., 2023), puncture/impact (Tafsirojaman et al., 2022), ovalisation (Vasilikis & Karamanos, 2012), axial deformation (Argyrou, Bouziou, O'Rourke, & Stewart, 2018), hoop stress (Tien et al., 2023), suitability for both present and forthcoming fluid compositions (Nuruddin et al., 2020), debonding at the interface between PIP and host pipe (O'Rourke et al., 2021), and service connections (Adebola, Moore, & Hoult, 2021). As outlined in this state-of-the-art review, a potential failure mode in pipelines and IRP systems is attributed to excessive thermal strains and the resultant stresses. In 2006, BP had to close sections of its Prudhoe Bay Pipeline in Alaska due to severe damage from excessive thermal strains, resulting in cracks and leaks (PHMSA, 2019). Subsequently, in 2021, the Colonial Pipeline faced closure following a cyber-attack. Upon restarting, the pipeline encountered a mechanical breakdown due to thermal expansion and contraction, triggering another shutdown that caused fuel shortages and price surges across multiple states (Bing & Kelly, 2021). Despite the critical need for safe design against thermal load-induced failures, research in this area is severely limited, and a comprehensive study addressing the structural challenges and design requisites of IRP systems against thermal actions is currently lacking in the literature.

Jeon, O'Rourke, and Neravali (2004) and Stewart, Weinberg, Berger, and Strait (2019) have devised a series of closed-form solutions for estimating crack opening in a cast-iron pipe undergoing rehabilitation with an internal pipe repair system under negative temperature variations. While these analytical formulations are beneficial for straightforward conservative assessments, they come with several constraints if a more accurate depiction of the system is desired. These formulations do not account for factors such as the stiffness of internal pipe, material nonlinearities, pipeline internal pressure, and thermal contraction/expansion of the repair pipe, all of which can influence crack opening and the axial behaviour of the repair system.

Dixon et al. (2023a) have employed an analytical method to predict potential levels of axial deformation. Their analysis centres on movement at a discontinuity, resembling a weak joint or circumferential crack in the host pipe, bridged by a rehabilitative internal pipe. They have derived closed-form equations for induced force and crack opening displacement. These formulations incorporate the effects of soil friction, as well as the stiffness and thermal contraction/expansion of the internal pipe. However, they do not account for the influence of material nonlinearities, stress concentrations, pipeline internal pressure, or variations in displacement along the thickness of both the internal repair pipe and the host pipe.

Bokaian (2004) formulated a comprehensive mathematical model to predict the thermal expansion of pipe-in-pipe and bundle systems commonly utilized in the offshore oil and gas industry. The objective was to determine displacements and forces on bulkheads, as well as axial loads within the inner pipe. However, this study assumed no discontinuities along the pipeline, limiting its applicability to gas distribution pipelines. Lu et al. (2020b) conducted a series of finite element (FE) stress analyses on urban gas pipelines repaired using the inserted hose lining method. However, their study did not address the effects of temperature fluctuations and discontinuities in the host pipe on the axial behaviour of the system. Tafsirojaman et al. (2022) investigated the failure modes of pipe-in-pipe repair systems for water and gas pipelines. Their research primarily focused on the behaviour of the repair system alone, without considering the influence of host pipe properties, material nonlinearities, or potential circumferential discontinuities in the thermal analysis.

When temperature falls below freezing, moisture in the soil can freeze and expand, resulting in frost load. This frost load can exert significant bending forces on the pipe. Kiriella et al. (2023) investigated the lateral deformation behaviour of IRP systems subjected to flexural loading. Their study yielded valuable insights into the response of IRP systems to bending loads such as frost-induced forces. They observed that the lateral deformation behaviour of an IRP system with a narrow circumferential discontinuity in the host pipe is primarily influenced by the host pipe, whereas for a wide discontinuity, the behaviour is governed by the IRP itself. They found that both the strength and stiffness of the system decrease with increasing discontinuity width. Regardless of the discontinuity width, the failure mode consistently involved local outward buckling at the crown position of IRP between the edges of the discontinuity. Additionally, they noted that increasing the thickness of IRP enhances the flexural capacity of the system, with a nonlinear increase for systems with wide discontinuities and a linear increase for systems with narrow discontinuities. Moreover, they found that the thickness and elastic modulus of the IRP have a greater impact on the lateral deformation of systems with wider discontinuity widths.

Ahmadi et al. (2024) developed a set of semi-analytical expressions for the calculation of thermal stresses and displacements of IRP systems. The effects of soil friction were incorporated in their models. However, the effects of the pipeline's internal pressure and various modes of debonding at the interface between the host pipe and IRP were not covered in their study. In addition, their research work did not include the statistical analysis of stress concentration factors (SCFs) in IRP systems.

The above discussion indicates that the axial behaviour of IRP system subjected to various levels of temperature change have not been thoroughly investigated; especially for cases in which there is a discontinuity along the pipeline (Figure 1). Three main categories of circumferential discontinuity may be identified in a host pipe (Figure 2): a circumferential fracture because of impact, fatigue crack propagation, and weld failure (Type I), a circumferential

![](./images/1000432425769107467_9.jpg)

Figure 1. Geometrical notation for an IRP system with a circumferential host pipe discontinuity.

![](./images/1000432425769107467_10.jpg)

Figure 2. Three major types of circumferential discontinuity in legacy gas pipelines.

discontinuity at bell and spigot joints (Type II), and a cir- cumferential discontinuity because of the removal of a sig- nificant portion of host pipe due to aging (Type III). For all these categories, IRP must be properly designed so that it performs satisfactorily in service.

This paper studies analytically and numerically the axial behaviour of IRP systems used for repairing pipelines with circumferential host-pipe discontinuities under seasonal and extreme levels of temperature change. Five major phases were implemented to achieve this objective. In Phase I, an analytical solution was developed for the prediction of load- ing and axial response of a mechanical model for an IRP system used in a host pipe with circumferential discontinu- ity subjected to a seasonal level of temperature change. Afterwards, in Phase II, parametric stress analyses were con- ducted on 134 FE models of IRP systems with a circumfer- ential discontinuity subjected to axial load. FE models were verified against experimental results and closed-form solu- tions. Numerical results were then utilized to investigate the effects of geometrical parameters and material properties on the axial displacements and stresses of the system subjected to seasonal temperature changes. In Phase III, based on the results of FE analysis, three modification factors were extracted for the application to the developed analytical model to accurately predict the maximum axial stress of IRP and the opening of a circumferential host-pipe discon- tinuity subjected to various levels of temperature change.

These modification factors are capable of taking three important aspects of the system's axial response into account: stress concentrations at the edge of circumferential discontinu- ity, nonuniform stress distribution along the thickness of IRP, and variations in displacement along the thickness of host pipe and IRP. Then, in Phase IV, 87 linear and nonlinear FE simu- lations were conducted and the results were utilized to investi- gate the effects of material nonlinearities and pipeline internal pressure on the axial displacements and stresses of the system due to seasonal and extreme temperature variations. Finally in Phase V, 49 linear/nonlinear FE stress analyses were carried out to study the effects of the presence of an unbonded seg- ment at the interface between IRP and host pipe on the axial response of the system due to seasonal and extreme tempera- ture changes. Results extracted from the analytical and

numerical models developed in this research will assist designers and developers in providing efficient and safe IRP systems urgently needed in pipeline industry.

It should be noted that depending on the material of the pipe, conditions of the surrounding soil, and stresses applied to the pipeline, both longitudinal and circumferential cracks may occur. Since in many cases, circumferential cracks tend to be more common than longitudinal cracks in buried pipelines, the present research is only focused on the circumferential cracks. It is also worth mentioning here that the effects of radial stresses due to temperature change are not included in this study, because subjected to temperature change, radial displacements in the pipeline and IRP system are relatively small compared to axial displacements (Jeon et al., 2004). Hence, generated radial stresses due to possible restriction of radial contraction/expansion would be small compared to axial thermal stresses (Stewart et al., 2019). This implies that the contributions of radial stresses and displacements into the maximum stress of IRP and opening of host-pipe discontinuity should be minimal.

## 2. Methodology

### 2.1. Formulating the maximum axial stress of IRP due to temperature variations

#### 2.1.1. Analytical formulation of an equivalent mechanical load for the simulation of thermal action
A compound section comprising both the host pipe and IRP is examined, featuring a circumferential discontinuity in the host pipe at the midspan. The pipe's length comprises three segments: a 'discontinuity' segment (Segment 2) containing only the IRP section, and two 'compound' segments (Segments 1 and 3) flanking the discontinuity segment. These compound segments include both the IRP and host pipe sections (refer to Figure 3). In such a compound section, even when axial deformation is unrestricted, a uniform temperature variation can still induce axial stresses in the pipe. This arises from differences in the coefficients of thermal expansion (CTE), which are material properties distinct for IRP and host pipe. The focal point of interest in this section is the tensile force per unit area of the compound section ($f_T$). This force is to be applied at the free end of the pipe in the mechanical model depicted in Figure 3, to replicate the axial response of the system to temperature changes.

Assuming that the material behaviour is linear and host pipe and IRP are fully bonded, the total axial deformation of the system ($\delta_T$) subjected to temperature change ($\Delta T$) is calculated as follows:

$$
\delta_{T}=\sum_{i=1}^{3} \delta_{i}=\alpha_{C}\left(\frac{L-c}{2}\right) \Delta T+\alpha_{I} c \Delta T+\alpha_{C}\left(\frac{L-c}{2}\right) \Delta T
\tag{1}
$$

![](./images/1000432425769107467_11.jpg)

Figure 3. Schematic representation of an IRP system with a host-pipe discontinuity subjected to the axial force.

where $L$ is the pipe's total length; $c$ is the discontinuity width; $\alpha_I$ is the CTE of IRP; and $\alpha_C$ is the equivalent CTE of the compound section which can be obtained from Equation (2). For the derivation of $\alpha_C$, refer to Ahmadi et al. (2024):

$$
\alpha_{C}=\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}
\tag{2}
$$

Based on Equation (2), Equation (1) is rewritten as follows:

$$
\delta_{T}=\Delta T\left[\alpha_{I} c+\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}(L-c)\right]
\tag{3}
$$

In a mechanical model designed to be "equivalent", the tensile force required at the free end of a compound section pipe to achieve an equivalent amount of axial deformation as when directly exposed to temperature change can be determined as follows:

$$
\begin{aligned}
F_{T} & =\delta_{T} k_{T}=\frac{\delta_{T}}{\frac{1}{k_{T}}} ; \frac{1}{k_{T}}=\sum_{i=1}^{3} \frac{1}{k_{i}}=\frac{\left(\frac{L-c}{2}\right)}{E_{C} A_{C}}+\frac{c}{E_{I} A_{I}}+\frac{\left(\frac{L-c}{2}\right)}{E_{C} A_{C}} \\
& =\frac{L-c}{E_{C} A_{C}}+\frac{c}{E_{I} A_{I}}
\end{aligned}
\tag{4}
$$

where $E_C$ and $A_C$ are equivalent elastic modulus and area of cross section for the compound section, respectively. The term $E_C A_C$ is calculated as a function of geometrical and material properties of host pipe and IRP as $E_I A_I + E_H A_H$ (see Ahmadi et al. (2024) for the derivation). Hence, the term $1/k_T$ in Equation (4) is rewritten as follows:

$$
\frac{1}{k_{T}}=\frac{L-c}{E_{I} A_{I}+E_{H} A_{H}}+\frac{c}{E_{I} A_{I}}
\tag{5}
$$

Substitution of Equations (3) and (5) into Equation (4) results in the following equation for the tensile load:

$$
F_{T}=\frac{\Delta T\left[\alpha_{I} c+\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}(L-c)\right]}{\frac{L-c}{E_{I} A_{I}+E_{H} A_{H}}+\frac{c}{E_{I} A_{I}}}
\tag{6}
$$

According to Equation (6), the tensile load per unit area of the cross-section ($f_T$) required at the free end of a pipe with a circumferential host-pipe discontinuity in an "equivalent" mechanical model, to induce the same amount of axial deformation caused by temperature change, is obtained as follows:

$$
f_{T}=\frac{F_{T}}{A_{C}}=\frac{\Delta T\left[\alpha_{I} c+\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}(L-c)\right]}{\left[\frac{L-c}{E_{I} A_{I}+E_{H} A_{H}}+\frac{c}{E_{I} A_{I}}\right]\left(A_{I}+A_{H}\right)}
\tag{7}
$$

#### 2.1.2. Transfer function for the IRP's nominal axial stress
Nominal axial stress of IRP at the discontinuity segment, $(\sigma_n)_I$, is formulated in terms of the tensile force per unit area of the compound section ($f_T$ in Equation (7)) as follows:

$$
\left(\sigma_{n}\right)_{I}=\lambda\left(D_{o H}, t_{H}, t_{I}\right) \cdot f_{T}
\tag{8}
$$

where $\lambda$ is a transfer function that is a function of host pipe's outer diameter ($D_{oH}$), host pipe's wall thickness ($t_H$),

and IRP's wall thickness $(t_{I})$ as follows (for derivation, refer to Appendix):

$$
\lambda=\frac{D_{o H}^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}}{\left(D_{o H}-2 t_{H}\right)^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}} \tag{9}
$$

### 2.1.3. Average value of axial stress along the wall thickness of IRP
Average values of axial stress along the wall thickness of IRP, $(\sigma_{a})_{I}$, were extracted from linear FE stress analyses carried out on 134 models with different material and geometrical properties. Values of axial stress were obtained from the midsection of the discontinuity segment. Afterwards, a parameter driven based on FE results was defined $(\eta)$ to transform the nominal values of axial stress in IRP at the discontinuity segment, $(\sigma_{n})_{I}$, to the $(\sigma_{a})_{I}$ values as follows:

$$
\left(\sigma_{a}\right)_{I}=\eta\left(\sigma_{n}\right)_{I} \tag{10}
$$

### 2.1.4. Hot-spot stress (HSS) in IRP
After obtaining the average value of axial stress along the thickness of IRP, IRP's HSS in the discontinuity segment is calculated as follows:

$$
\left(\sigma_{h s}\right)_{I}=\mathrm{SCF} \cdot\left(\sigma_{a}\right)_{I} \tag{11}
$$

in which, SCF denotes the stress concentration factor which needs to be determined from linear elastic FE analyses. The procedure for extracting SCFs from the FE models is elaborated in Section 2.3.3. The HSS is regarded as the indicative value for the peak axial stress within the discontinuity segment, serving as a basis for fatigue analysis of IRP systems. This HSS-based approach aligns with methodologies employed by well-known design codes like the American Petroleum Institute (API) (2007) and Det Norske Veritas (2005) for the fatigue assessment of tubular joints.

### 2.1.5. Final expression for the description of IRP's maximum axial stress
Combining Equations (7) through (11) results in the subsequent expression for IRP's hot-spot stress within the discontinuity segment:

$$
\begin{aligned}
\left(\sigma_{h s}\right)_{I}= & \mathrm{SCF} \cdot \eta \cdot \frac{D_{o H}^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}}{\left(D_{o H}-2 t_{H}\right)^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}} \\
& \cdot \frac{\alpha_{I} c+\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}(L-c)}{\left[\frac{L-c}{E_{I} A_{I}+E_{H} A_{H}}+\frac{c}{E_{I} A_{I}}\right]\left(A_{I}+A_{H}\right)} \cdot \Delta T
\end{aligned} \tag{12}
$$

where the values of SCF and $\eta$ are specified based on the results of linear elastic FE analyses carried out on 134 models having different material and geometrical characteristics.

## 2.2. Formulating the opening of discontinuity due to temperature variations

### 2.2.1. Analytical formulation of applicable axial displacement for the simulation of thermal actions
Utilizing the analytical formulation outlined in Section 2.1.1, the axial displacement required at the free end of the pipe in a mechanical model to replicate the axial deformation induced by temperature change can be computed using Equation (3).

### 2.2.2. Transfer function for the nominal discontinuity opening
Nominal discontinuity opening, $(\delta_{c})_{n}$, is obtained in terms of the applicable axial displacement ($\delta_{T}$ in Equation (3)) as follows:

$$
\left(\delta_{c}\right)_{n}=\mu\left(c, L, E_{I}, A_{I}, E_{H}, A_{H}\right) \cdot \delta_{T} \tag{13}
$$

where $\mu$ is a transfer function that depends on the system's material and geometrical properties as shown in Equation (14) (for derivation, the reader is referred to Ahmadi et al. (2024)):

$$
\mu=\frac{c}{E_{I} A_{I}\left(\frac{c}{E_{I} A_{I}}+\frac{L-c}{E_{H} A_{H}+E_{I} A_{I}}\right)} \tag{14}
$$

### 2.2.3. The ratio of actual to nominal discontinuity openings
Actual discontinuity openings, $\delta_{c}$, were extracted from linear FE stress analyses carried out on 134 models with different material and geometrical properties. The value of $\delta_{c}$ was obtained using the displacements of the discontinuity's upper edges. An FE-driven parameter was then defined $(\psi)$ to relate the nominal discontinuity openings, $(\delta_{c})_{n}$, to the $\delta_{c}$ values as:

$$
\delta_{c}=\psi\left(\delta_{c}\right)_{n} \tag{15}
$$

### 2.2.4. Final expression for the description of the discontinuity opening
Combining Equations (3) and (13)-(15) results in the subsequent expression for the circumferential discontinuity opening because of temperature variation in a host pipe rehabilitated by an IRP system:

$$
\begin{aligned}
\delta_{c}= & \psi \cdot \frac{c}{E_{I} A_{I}\left(\frac{c}{E_{I} A_{I}}+\frac{L-c}{E_{H} A_{H}+E_{I} A_{I}}\right)} \\
& \cdot\left[\alpha_{I} c+\frac{E_{I} A_{I} \alpha_{I}+E_{H} A_{H} \alpha_{H}}{E_{I} A_{I}+E_{H} A_{H}}(L-c)\right] \cdot \Delta T
\end{aligned} \tag{16}
$$

where the values of the parameter $\psi$ are obtained through linearly elastic FE analyses carried out on 134 models having different material and geometrical characteristics.

### 2.3. Numerical simulation

#### 2.3.1. Mesh generation, boundary conditions, and the simulation of interface between host pipe and IRP
The numerical modelling and analysis utilized the FE software ANSYS (2016). In this setup, one end of the pipe was completely fixed, while the other end was left free to replicate the conditions described in Section 2.1 and depicted in Figure 3. To streamline computational efficiency and account for symmetry in both geometry and loading, only one quarter of the entire tubular section was modelled. Symmetric boundary conditions were established on the symmetry planes as appropriate.

SOLID185 elements were employed to model both the host pipe and IRP. This element type, known for its compatible displacements and suitability for curved boundaries, is defined by eight nodes with three degrees of freedom per node and can be oriented spatially in any direction. During the FE modelling process, a sub-zone mesh generation approach was implemented. This involved dividing the entire pipe into multiple zones based on computational needs. The mesh for each zone was generated independently, and subsequently, the meshes of all sub-zones were merged to create the mesh for the entire system. This method can effectively manage mesh quantity and quality while preventing the occurrence of badly distorted elements (Ahmadi & Ziaei Nejad, 2017). Before conducting the 270 FE analyses for the parametric study, a mesh convergence check was performed. Various mesh densities were tested to ensure that the results remained unaffected by mesh size.

In scenarios where there is no debonding at the interface between the host pipe and IRP, host pipe and IRP are effectively bonded along the entire interface, resulting in no ability to slide or separate from each other, with no gap between them. To replicate this fully bonded condition within the model, a "Glue" condition is applied between host pipe and IRP. In areas where bonding is not present, no "Glue" condition is defined. This allows for relative displacements between the surfaces of IRP and host pipe over the unbonded segments.

---

### 2.3.2. Loading and analysis

#### 2.3.2.1. Loading and analysis to obtain the values of the $\eta$ and $\psi$
A value of $27.8\,^\circ\text{C}$ was selected for the temperature change. This value represents the maximum seasonal temperature changes experienced by pipelines in New York State and other regions of the Northeastern United States, typically ranging from 22 to $27.8\,^\circ\text{C}$ equivalent to $40$–$50\,^\circ\text{F}$ (Stewart et al., 2015, 2019). A tensile force per unit area of the cross section, calculated based on Equation (7) for $\Delta T = 27.8\,^\circ\text{C}$, was applied on host pipe and IRP cross sections at the pipe's free end. As the focus of this study for the extraction of the parameters $\eta$ and $\psi$ is seasonal temperature variations, the maximum $\Delta T$ is not large enough to result in considerable effects of material nonlinearities (Stewart et al., 2015, 2019). Hence, all the conducted mechanical FE analyses were linear and elastic. A steel host pipe was assumed having elastic modulus, CTE, and Poisson's ratio of $210.7\,\text{GPa}$ (Lee, Pouraria, Seo, & Paik, 2015), $12 \times 10^{-6}\,1/^\circ\text{C}$ (Valves Instruments Plus (VIP) Ltd, 2002), and 0.3, respectively. The Poisson's ratio of IRP was set to a constant value of 0.23.

#### 2.3.2.2. Loading and analysis to extract the SCFs
Under any specific type of loading, the SCF value does not depend on the applied load's magnitude. Hence, in order to calculate SCFs subjected to axial loading, a tensile force per unit area of the cross section equal to $1\,\text{MPa}$ was applied on host pipe and IRP cross sections at the pipe's free end. N'Diaye, Hariri, Pluvinage, and Azari (2007) suggested that linear elastic analysis of static type is appropriate for the computation of SCFs. Since the SCF is mainly a function of geometrical characteristics and it is independent from material properties (API, 2007), materials of host pipe and IRP were arbitrarily selected as steel of API 5L X42/L290 class and ALTRA10$^\circledR$ (Bureau, Davison, & O'Rourke, 2021), respectively. The modulus of elasticity (MoE) and Poisson's ratio were assumed as $210.7\,\text{GPa}$ and 0.3 for host pipe (Lee et al., 2015); and $3.77\,\text{GPa}$ and 0.23 for IRP (CDCQ, 2021), respectively.

#### 2.3.2.3. Loading and analysis to monitor the effects of material nonlinearities and internal pressure
The axial displacement value required for the application on the pipe's free end in the mechanical model to replicate the system's axial deformation due to the temperature variation was obtained utilizing Equation (3). Two different materials were considered for host pipe: steel and cast iron. Elastic modulus and CTE for steel were presented in Section 2.3.2.1. For cast iron, these material properties were $69.6\,\text{GPa}$ (Stewart et al., 2019) and $10.8 \times 10^{-6}\,1/^\circ\text{C}$ (TET., 2003), respectively. Values of the Poisson's ratio for IRP and host pipe were presented in Section 2.3.2.2. Stress-strain curves of IRP and host pipe in the axial direction are depicted in Figure 4. These curves were derived from true stress and true strain values. The transformation from engineering stress-strain data to the corresponding true values was achieved using the following equations:

$$
\sigma_{\text{true}} = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}}) \tag{17}
$$

$$
\varepsilon_{\text{true}} = \ln\left(1 + \varepsilon_{\text{eng}}\right) \tag{18}
$$

Engineering stress-strain curves for steel and cast-iron host pipes and ALTRA10$^\circledR$ IRP were referred from Lee et al. (2015), Mustafa and Moy (2011), and CDCQ (2021), respectively. To investigate the internal pressure's effect subjected to seasonal temperature variations, all the conducted FE analyses were linear and elastic. However, for the FE analysis of IRP system under extreme temperature variations, which may occur for example due to a fire incident or the exposure to high temperature steam, material nonlinearities were incorporated in the model. The effect of geometric nonlinearity was also examined in case of an extreme temperature change.

#### 2.3.2.4. Loading and analysis to study the effects of IRP-host pipe interface unbonding
An axial displacement,

![](./images/1000432425769107467_12.jpg)

Figure 4. True stress-strain curves used for the FE analysis: (a) API 5 L X42 steel, (b) cast iron, (c) ALTRA10®.

![](./images/1000432425769107467_13.jpg)

Figure 5. Extraction of the parameters η, SCF, and ψ from the FE model.

calculated using Equation (3), was applied to the pipe's free end to replicate the system's axial deformation due to the temperature variation. A steel host pipe was assumed. Elastic modulus and CTE for steel were as assumed in Section 2.3.2.1. Values of the Poisson's ratio for IRP and host pipe were same as Section 2.3.2.2, and stress-strain curves for IRP (ALTRA10®) and host pipe (steel) were as described in Section 2.3.2.3.

### 2.3.3. Calculation of the η, SCF, and ψ
At the first step, values of axial stress along the thickness of IRP were obtained from the FE model at the discontinuity segment's midsection (Figure 5) for the purpose of calculating the value of the parameter η. Afterwards, the average axial stress, $(\sigma_a)_I$, was calculated based on Equation (19a); and then the obtained value was divided by the IRP's nominal value of axial stress, known from Equation (8), for calculating the η (Equation (19b)):

$$
(\sigma_a)_I = \frac{1}{k} \sum_{i=1}^{k} \sigma_{mi} \text{ (a)} \rightarrow \eta = \frac{1}{k \lambda f_T} \sum_{i=1}^{k} \sigma_{mi} \text{(b)} \tag{19}
$$

In Equation (19), $k$ is the number of nodes along the thickness of IRP and $\sigma_{mi}$ is the axial stress in the $i^{th}$ node along the thickness of IRP at the discontinuity segment's midsection (Figure 5). According to Equation (11), the SCF can be defined as follows:

$$
\mathrm{SCF} = \frac{(\sigma_{hs})_I}{(\sigma_a)_I} \tag{20}
$$

where $(\sigma_{hs})_I$ and $(\sigma_a)_I$ are IRP's HSS and average value of axial stress, respectively.

For the determination of the HSS, the axial stress at the edge of the discontinuity must be obtained from the stress field beyond the zone which is affected by the local geometry of the edge (Ahmadi, Lotfollahi-Yaghin, & Aminfar, 2012a, 2012b). The HSS calculated using this method depends on the overall geometry of the system instead on the specific geometry of the notch itself. The determination of the location from which stresses are extrapolated, known as the extrapolation region, is contingent upon the system's dimensions (Ahmadi, Chamani, & Kouhi, 2020). According to the guidelines outlined by the UK Health and Safety

Executive (1997) for acrylic tubular joints lacking welds, and the extrapolation method proposed by the International Institute of Welding, the initial extrapolation point is set at a distance of $0.4t_I$ from the edge. Subsequently, the second point is positioned $0.6t_I$ beyond the first, where $t_I$ represents the IRP thickness (Hobbacher, 2016). The HSS is derived by linearly extrapolating geometric stresses from these two points to the edge position, using Equation (21), as depicted in Figure 5:

$$
\sigma_{h s}=\frac{1}{0.6} \sigma_{a 1}-\frac{0.4}{0.6} \sigma_{a 2} \tag{21}
$$

where $\sigma_{a 1}$ and $\sigma_{a 2}$ are the values of axial stress at the first and second extrapolation points, respectively.

Substituting $(\sigma_a)_I$ from Equation (19) and $\sigma_{h s}$ from Equation (21) into Equation (20) leads to the following formula for the SCF calculation in an IRP system:

$$
\mathrm{SCF}=\frac{k\left(\sigma_{a 1}-0.4 \sigma_{a 2}\right)}{0.6 \sum_{i=1}^{k} \sigma_{m i}} \tag{22}
$$

To ensure uniform mesh densities across models with varying geometric characteristics, the parameter $k$ in Equation (22) should be contingent upon the thickness of IRP. It was set to 4, 7, 10, 13, 16, and 21 for $\tau$ values of 0.4, 0.65, 0.9, 1.15, 1.4, and 1.65, respectively. Here, $\tau$ represents the ratio of IRP thickness to host pipe thickness $(t_I/t_H)$.

The axial displacements at the upper edges of the discontinuity segment were obtained from the FE analysis (Figure 5) for calculating the value of the parameter $\psi$. Afterwards, the actual value of the discontinuity opening was obtained using Equation (23a); and then this value was divided by the nominal value of the discontinuity opening, known from Equation (13), to determine $\psi$ (Equation (23b)):

$$
\delta_{c}=\delta_{a 1}-\delta_{a 2} \text{ (a)} \rightarrow \psi=\frac{\delta_{a 1}-\delta_{a 2}}{\mu \delta_{T}} \text{ (b)} \tag{23}
$$

### 2.3.4. Validation of numerical models
#### 2.3.4.1. Examining nominal values of discontinuity opening and axial stress under temperature variation
Some of the parameters of interest in the present research could be predicted by both FE analysis and purely analytical solution (e.g. nominal value of IRP's axial stress, $(\sigma_n)_I$, and nominal value of discontinuity opening, $(\delta_c)_n$). These parameters were calculated using purely analytical expressions and then used to verify the accuracy of developed FE models. Some other parameters could only be predicted by the FE model, not the purely analytical solution (e.g. hot-spot stress, $(\sigma_{h s})_I$, and actual discontinuity opening, $\delta_c$). Values of these parameters were obtained by conducting extensive stress analyses on validated FE models and then used to propose modification factors (i.e. $\eta$, SCF, and $\psi$) for adjusting the purely analytical solution.

Nominal values of IRP's axial stress and discontinuity opening were obtained from three sample numerical models under the tensile load equivalent of a $27.8\,^\circ\text{C}$ temperature variation. Table 1 lists the material and geometrical characteristics of the developed FE models. Values of the axial stress at the central node along the IRP thickness at the discontinuity segment's midspan was obtained from the FE model as the representative value for the IRP's nominal axial stress. Nominal value of the discontinuity opening was obtained from the FE model through the calculation of the difference between the IRP's nodal displacements at the two ends of the discontinuity segment and subsequently averaging these differences along the thickness of IRP. Analytical values for the nominal value of IRP's axial stress and nominal discontinuity opening were calculated from Equations (8) and (13), respectively. Results of validation process summarised in Table 2 demonstrate a very close agreement between the numerical results and analytical values for both discontinuity opening and IRP's axial stress.

<table>
<caption>Table 1. Geometrical and material properties of FE models used for the verification of numerical results.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Unit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus of IRP</td>
<td>$E_I$</td>
<td>GPa</td>
<td>3.77, 10, and 24.5</td>
</tr>
<tr>
<td>Poisson's ratio of IRP</td>
<td>$v_I$</td>
<td>–</td>
<td>0.23</td>
</tr>
<tr>
<td>CTE of IRP</td>
<td>$\alpha_I$</td>
<td>$1/^\circ\text{C}$</td>
<td>$45\times10^{-6}$</td>
</tr>
<tr>
<td>Wall thickness of IRP</td>
<td>$t_I$</td>
<td>mm</td>
<td>4.115, 7.3025, and 10.4775</td>
</tr>
<tr>
<td>Young's modulus of the host pipe</td>
<td>$E_H$</td>
<td>GPa</td>
<td>210.7</td>
</tr>
<tr>
<td>Poisson's ratio of the host pipe</td>
<td>$v_H$</td>
<td>–</td>
<td>0.3</td>
</tr>
<tr>
<td>CTE of the host pipe</td>
<td>$\alpha_H$</td>
<td>$1/^\circ\text{C}$</td>
<td>$12\times10^{-6}$</td>
</tr>
<tr>
<td>Wall thickness of the host pipe</td>
<td>$t_H$</td>
<td>mm</td>
<td>6.35</td>
</tr>
<tr>
<td>Outer diameter of the host pipe</td>
<td>$D_{oH}$</td>
<td>mm</td>
<td>323.85</td>
</tr>
<tr>
<td>Discontinuity width</td>
<td>$c$</td>
<td>mm</td>
<td>12.7, 82.55, and 152.4</td>
</tr>
<tr>
<td>Pipe length</td>
<td>$L$</td>
<td>mm</td>
<td>3048</td>
</tr>
</tbody>
</table>

#### 2.3.4.2. Examining the axial deformation and induced stresses subjected to pipeline's internal pressure
In order to verify the validity of numerical models established for investigating the effects of pipeline's internal pressure on the system's axial behaviour, analytical values calculated via closed-form expressions were compared with the results obtained from the FE model of a host-pipe-only case with the pipeline's internal pressures of 1, 1.25, and 1.5 MPa at the temperature change of zero. Tables 1 and 3 list the values of material and geometrical characteristics of host pipe, respectively. Hoop/circumferential stress $(\sigma_\theta)$, longitudinal/axial stress $(\sigma_l)$, and radial stress $(\sigma_r)$ of host pipe subjected to pipeline's internal pressure are obtained using Equations (24)–(26), respectively:

$$
\sigma_{\theta}=\frac{p_{i} D_{i H}}{2 t_{H}} \tag{24}
$$

$$
\sigma_{l}=v_{H} \sigma_{\theta} \tag{25}
$$

$$
\sigma_{r}=-p_{i} \tag{26}
$$

where $p_i$ is pipeline's internal pressure; $D_{iH}$ is host pipe's inner diameter; $t_H$ is host pipe's wall thickness; and $v_H$ is host pipe's Poisson's ratio (API 5 L X42 class steel).

If the material behaviour is linear, system's axial deformation subjected to internal pressure is obtained as follows:

$$
\begin{aligned}
\delta_{T} & =\left.\delta(x)\right|_{x=L}=\int_{0}^{L} \varepsilon_{l}(x) d x=\int_{0}^{L} \frac{\sigma_{l}}{E_{H}} d x=\int_{0}^{L} \frac{v_{H} \sigma_{\theta}}{E_{H}} d x \\
& \left.=\frac{v_{H} p_{i} D_{i H} x}{2 E_{H} t_{H}}\right]_{x=0}^{x=L}=\frac{v_{H} p_{i} D_{i H} L}{2 E_{H} t_{H}}
\end{aligned} \tag{27}
$$

<table>
<caption>Table 2. Results of the FE verification process based on analytical predictions.</caption>
<thead>
<tr>
<th>Model properties</th>
<th>Parameter</th>
<th>FE result</th>
<th>Analytical prediction</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Case 1 ($E_I = 3.77$ GPa, $t_I = 4.115$ mm, $c = 12.7$ mm)</td>
<td>Nominal axial stress of IRP, $(\sigma_n)_I$</td>
<td>86.117 MPa</td>
<td>86.145 MPa</td>
<td>0.03%</td>
</tr>
<tr>
<td></td>
<td>Nominal value of discontinuity opening, $(\delta_c)_n$</td>
<td>0.2755 mm</td>
<td>0.2903 mm</td>
<td>5.1%</td>
</tr>
<tr>
<td>Case 2 ($E_I = 10$ GPa, $t_I = 7.3025$ mm, $c = 82.55$ mm)</td>
<td>Nominal axial stress of IRP, $(\sigma_n)_I$</td>
<td>53.409 MPa</td>
<td>53.430 MPa</td>
<td>0.04%</td>
</tr>
<tr>
<td></td>
<td>Nominal value of discontinuity opening, $(\delta_c)_n$</td>
<td>0.4203 mm</td>
<td>0.4411 mm</td>
<td>4.7%</td>
</tr>
<tr>
<td>Case 3 ($E_I = 24.5$ GPa, $t_I = 10.4775$ mm, $c = 152.4$ mm)</td>
<td>Nominal axial stress of IRP, $(\sigma_n)_I$</td>
<td>64.150 MPa</td>
<td>64.162 MPa</td>
<td>0.02%</td>
</tr>
<tr>
<td></td>
<td>Nominal value of discontinuity opening, $(\delta_c)_n$</td>
<td>0.3816 mm</td>
<td>0.3991 mm</td>
<td>4.4%</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3. Results of the FE model verification against closed-form solutions.</caption>
<thead>
<tr>
<th>Model properties</th>
<th>Parameter</th>
<th>Closed-form solution</th>
<th>FE result</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Case I ($D_{iH} = 311.15$ mm,
$t_H = 6.35$ mm, $L = 3048$ mm, $p_i = 1$ MPa)</td>
<td>Hoop stress, $\sigma_\theta$</td>
<td>24.5 MPa</td>
<td>24.528 MPa</td>
<td>0.1%</td>
</tr>
<tr>
<td></td>
<td>Longitudinal stress, $\sigma_l$</td>
<td>7.35 MPa</td>
<td>7.083 MPa</td>
<td>3.7%</td>
</tr>
<tr>
<td></td>
<td>Radial stress, $\sigma_r$</td>
<td>$-1$ MPa</td>
<td>$-0.918$ MPa</td>
<td>8.2%</td>
</tr>
<tr>
<td></td>
<td>Total axial deformation, $\delta_T$</td>
<td>0.106 mm</td>
<td>0.103 mm</td>
<td>2.8%</td>
</tr>
<tr>
<td>Case II ($D_{iH} = 593.60$ mm,
$t_H = 8.00$ mm, $L = 10000$ mm, $p_i = 1.25$ MPa)</td>
<td>Hoop stress, $\sigma_\theta$</td>
<td>46.38 MPa</td>
<td>46.32 MPa</td>
<td>0.1%</td>
</tr>
<tr>
<td></td>
<td>Longitudinal stress, $\sigma_l$</td>
<td>13.91 MPa</td>
<td>13.45 MPa</td>
<td>3.3%</td>
</tr>
<tr>
<td></td>
<td>Radial stress, $\sigma_r$</td>
<td>$-1.25$ MPa</td>
<td>$-1.16$ MPa</td>
<td>7.2%</td>
</tr>
<tr>
<td></td>
<td>Total axial deformation, $\delta_T$</td>
<td>0.832 mm</td>
<td>0.812 mm</td>
<td>2.4%</td>
</tr>
<tr>
<td>Case III ($D_{iH} = 890.60$ mm,
$t_H = 11.90$ mm,
$L = 30000$ mm, $p_i = 1.5$ MPa)</td>
<td>Hoop stress, $\sigma_\theta$</td>
<td>56.13 MPa</td>
<td>56.05 MPa</td>
<td>0.1%</td>
</tr>
<tr>
<td></td>
<td>Longitudinal stress, $\sigma_l$</td>
<td>16.84 MPa</td>
<td>16.33 MPa</td>
<td>3.0%</td>
</tr>
<tr>
<td></td>
<td>Radial stress, $\sigma_r$</td>
<td>$-1.5$ MPa</td>
<td>$-1.40$ MPa</td>
<td>6.7%</td>
</tr>
<tr>
<td></td>
<td>Total axial deformation, $\delta_T$</td>
<td>2.40 mm</td>
<td>2.35 mm</td>
<td>2.1%</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4. Geometrical and material properties of S01 and S02 specimens prepared for the experimental tests.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus of the ALTRA10® IRP</td>
<td>3769.2 MPa</td>
</tr>
<tr>
<td>Poisson's ratio of the ALTRA10® IRP</td>
<td>0.23</td>
</tr>
<tr>
<td>Wall thickness of the ALTRA10® IRP</td>
<td>4.115 mm</td>
</tr>
<tr>
<td>Young's modulus of the steel host pipe</td>
<td>210700 MPa</td>
</tr>
<tr>
<td>Poisson's ratio of the steel host pipe</td>
<td>0.3</td>
</tr>
<tr>
<td>Wall thickness of the steel host pipe</td>
<td>6.35 mm</td>
</tr>
<tr>
<td>Outer diameter of the steel host pipe</td>
<td>323.85 mm</td>
</tr>
<tr>
<td>Discontinuity width</td>
<td>12.7 mm (S01), 152.4 mm (S02)</td>
</tr>
<tr>
<td>Pipe length</td>
<td>3048 mm</td>
</tr>
</tbody>
</table>

Table 3 which summarises the results of validation process demonstrates that the established numerical models can produce valid and accurate results in case a combination of parameters are changed simultaneously.

#### 2.3.4.3. Comparing the numerical and experimental values of discontinuity opening.
In order to study the axial behaviour of IRP systems, experimental tests were carried out at Center for Infrastructure, Energy, and Space Testing (CIEST), University of Colorado Boulder. Two specimens, namely S01 and S02, were prepared for the tests. In both specimens, host pipe was steel, and IRP was ALTRA10®. Table 4 presents the material and geometrical properties of tested specimens. S01 and S02 specimens were tested under axial loading in a horizontal setup using 500 kN and 1000 kN actuators, respectively (Figure 6). Before conducting the axial test, loadings from traffic on the surface and parallel excavations were simulated in the lab, and specimens underwent 600,000 fatigue cycles. These prior bending tests could lead to some debonding even before the initiation of axial test.

Axial test was conducted by applying a tensile load which opens the discontinuity followed by a compressive load closing the discontinuity. The intention was to simulate the opening and closing of a circumferential discontinuity due to the temperature change from summer to winter and vice versa, respectively, during the design life of the IRP system. In the numerical model of S02 specimen, a greater debonded length was necessary to match the experimental results. Simulation of unbonded segments in the numerical model in depicted in Figure 7. This finding agrees well with specimens' conditions, because the parallel excavation was representative of a significantly larger displacement of soil for the S02 specimen in comparison with S01. Consequently, more severe debonding was expected in S02 specimen before the initiation of pull-push tests. Table 5 compares the discontinuity openings from the numerical analysis and experimental test lending support to reliability and accuracy of established numerical model.

### 2.4. Extraction of the expected peak SCF for design purposes

Based on FE stress analyses carried out on 44 models, a statistical sample was generated for the SCF values in IRP systems, and a statistical analysis was performed to characterise the maximum expected SCF for design purposes. The first step was to apply the Kolmogorov-Smirnov (K-S) goodness-of-fit test to examine the hypothesis that the SCF, as a random variable, follows a normal probability distribution. If the outcome of the test would support the hypothesis, then the second step would be using the properties of a normally distributed random variable to estimate the maximum expected value for the SCF.

The K-S goodness-of-fit test is a nonparametric test relating to the cumulative distribution function (CDF) of a continuous variable. In a two-sided test, the test statistic is the maximum absolute difference (which is usually the vertical distance) between the empirical and hypothetical CDFs (Kottegoda & Rosso, 2008). The maximum likelihood (ML) method was used to fit a hypothetical normal CDF to the empirical distribution function of SCF sample. After fitting the hypothetical CDF, a K-S test was carried out via MATLAB (MathWorks,

![](./images/1000432425769107467_14.jpg)

Figure 6. Experimental tests conducted at the university of Colorado boulder: (a) setup for axial pull-push tests, (b) S01 specimen, (c) digital image correlation (DIC) system setup for the S02 specimen.

![](./images/1000432425769107467_15.jpg)

Figure 7. Considered unbonding modes: (a) one-sided unbonded segment, (b) two-sided unbonded.

<table>
<caption>Table 5. Results of the FE model verification using experimental data.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Specimen</th>
<th>Debonded length</th>
<th>Experimental value</th>
<th>FE result</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Discontinuity opening</td>
<td>S01</td>
<td>95 mm</td>
<td>0.73 mm</td>
<td>0.77 mm</td>
<td>5.5%</td>
</tr>
<tr>
<td></td>
<td>S02</td>
<td>150 mm</td>
<td>2.95 mm</td>
<td>3.04 mm</td>
<td>3.1%</td>
</tr>
</tbody>
</table>

2007). For more details about the ML method and K-S test, the reader is referred to Ahmadi et al. (2019). If the generated SCF sample follows a normal probability distribution, then the maximum expected value of the SCF can be estimated as follows (Kottegoda & Rosso, 2008):

$$
\mathrm{SCF}_{\max}=\mu_{\mathrm{SCF}}+3 \sigma_{\mathrm{SCF}} \tag{28}
$$

where $\mu_{SCF}$ and $\sigma_{SCF}$ are the mean and standard deviation values for the SCF, respectively.

### 2.5. Details of parametric study

#### 2.5.1. Parametric study to characterize the $\eta$, SCF, and $\psi$
Altogether, 134 FE models were run to study the effects of material and geometrical properties of the system on values of parameters $\eta$, SCF, and $\psi$ to complete the formulation of axial deformations and stresses in an IRP system subjected to seasonal temperature variations. Table 6 lists the various values designated to the system's material and geometrical properties. Nondimensional geometrical parameters were defined (Equation (29)) to feasibly relate the behaviour of the IRP system to its geometrical properties:

$$
\tau=\frac{t_{I}}{t_{H}} ; \zeta=\frac{c}{t_{H}} ; \gamma=\frac{D_{o H}}{2 t_{H}} ; \alpha=\frac{2 L}{D_{o H}} \tag{29}
$$

Values of geometrical and material properties presented in Table 6 cover the practical ranges which are typically expected in IRP systems. Selected range for the parameter $\gamma$ is based on the actual sizes of both steel and cast-iron pipes used in the

<table>
<caption>Table 6. Geometrical and material properties used for the parametric study to characterise $\eta$, SCF, and $\psi$.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Unit</th>
<th>Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young’s modulus of IRP</td>
<td>$E_I$</td>
<td>GPa</td>
<td>1, 3.77, 10, 15, 24.5, 69</td>
</tr>
<tr>
<td>Wall thickness of IRP</td>
<td>$t_I$</td>
<td>mm</td>
<td>2.54, 4.115, 5.715, 7.3025, 8.89, 10.4775</td>
</tr>
<tr>
<td>CTE of IRP</td>
<td>$\alpha_I$</td>
<td>$(1/^\circ\text{C}){\times}10^{-6}$</td>
<td>10, 30, 45, 70, 90, 110, 130, 150</td>
</tr>
<tr>
<td>Outer diameter of the host pipe</td>
<td>$D_{oH}$</td>
<td>mm</td>
<td>323.85, 609.6, 914.4, 1219.2, 1524</td>
</tr>
<tr>
<td>Wall thickness of the host pipe</td>
<td>$t_H$</td>
<td>mm</td>
<td>6.35, 8, 11.9, 14.3</td>
</tr>
<tr>
<td>Discontinuity width</td>
<td>$c$</td>
<td>mm</td>
<td>6.35, 12.7, 47.625, 82.55, 117.475, 152.4</td>
</tr>
<tr>
<td>Pipe length</td>
<td>$L$</td>
<td>mm</td>
<td>3048, 12144.4, 24288.8, 48577.5</td>
</tr>
<tr>
<td>$t_I/t_H$ ratio</td>
<td>$\tau$</td>
<td>–</td>
<td>0.4, 0.65, 0.9, 1.15, 1.4, 1.65</td>
</tr>
<tr>
<td>$c/t_H$ ratio</td>
<td>$\zeta$</td>
<td>–</td>
<td>1, 2, 7.5, 13, 18.5, 24</td>
</tr>
<tr>
<td>$D_{oH}/2t_H$ ratio</td>
<td>$\gamma$</td>
<td>–</td>
<td>11.1, 18.5, 25.5, 34, 38.5, 45</td>
</tr>
<tr>
<td>$2L/D_{oH}$ ratio</td>
<td>$\alpha$</td>
<td>–</td>
<td>18.8, 75, 150, 300</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 7. Geometrical and material properties of 49 FE models to study the effects of the internal pressure and material nonlinearities.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Unit</th>
<th>Value(s)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young’s modulus of IRP</td>
<td>$E_I$</td>
<td>GPa</td>
<td>1, 3.77, 10</td>
</tr>
<tr>
<td>Wall thickness of IRP</td>
<td>$t_I$</td>
<td>mm</td>
<td>2.54, 4.115, 5.715</td>
</tr>
<tr>
<td>Outer diameter of the host pipe</td>
<td>$D_{oH}$</td>
<td>mm</td>
<td>323.85, 431.80, 571.50</td>
</tr>
<tr>
<td>Discontinuity width</td>
<td>$c$</td>
<td>mm</td>
<td>6.35, 12.7, 152.4</td>
</tr>
<tr>
<td>CTE of the host pipe</td>
<td>$\alpha_H$</td>
<td>$1/^\circ\text{C}$</td>
<td>$10.8{\times}10^{-6}$, $12{\times}10^{-6}$</td>
</tr>
<tr>
<td>Young’s modulus of the host pipe</td>
<td>$E_H$</td>
<td>GPa</td>
<td>69.6, 210.7</td>
</tr>
<tr>
<td>Poisson’s ratio of the host pipe</td>
<td>$v_H$</td>
<td>–</td>
<td>0.3</td>
</tr>
<tr>
<td>Wall thickness of the host pipe</td>
<td>$t_H$</td>
<td>mm</td>
<td>6.35</td>
</tr>
<tr>
<td>Poisson’s ratio of IRP</td>
<td>$v_I$</td>
<td>–</td>
<td>0.23</td>
</tr>
<tr>
<td>CTE of IRP</td>
<td>$\alpha_I$</td>
<td>$1/^\circ\text{C}$</td>
<td>$45{\times}10^{-6}$</td>
</tr>
<tr>
<td>Pipe length</td>
<td>$L$</td>
<td>mm</td>
<td>3048</td>
</tr>
</tbody>
</table>

gas industry. Steel pipe sizes were extracted from Gas Industry Standard GIS/L2 (2018) and cast-iron pipe dimensions were selected based on the information provided by Cast Iron Pipe Research Association (1952).

### 2.5.2. Parametric study on the effects of the internal pressure of the pipe and material nonlinearities
Collectively, 87 linear and nonlinear stress analyses were conducted to examine the effects of pipeline’s internal pressure and material nonlinearities on the axial stress and displacement of the IRP system with a circumferential discontinuity under seasonal and extreme temperature changes. Different values assigned to the geometrical and material characteristics of the system are listed in Table 7. In order to study the effect of internal pressure, a value of $27.8^\circ\text{C}$ was selected for the temperature change. The reason for the selection of this specific value has been discussed in Section 2.3.2.a. Five values were assigned for the internal pressure: 0, 0.25, 0.5, 0.75, and 1 MPa.

To investigate the effects of material and geometric nonlinearities, ALTRA10® was chosen as IRP; since it was previously used for water pipeline repair (Bureau et al., 2021) and its nonlinear stress-strain curve is available. MoE, Poisson’s ratio, and CTE for ALTRA10® were assumed to be 3.77 GPa (CDCQ, 2021), 0.23 (CDCQ, 2021), and $45{\times}10^{-6}\ 1/^\circ\text{C}$ (CDCQ., 2022), respectively. Seven $\Delta T$ values ranging from $13.9^\circ\text{C}$ to $97.3^\circ\text{C}$ were considered to cover both seasonal and extreme temperature changes ($\Delta T = 13.9$, 27.8, 41.7, 55.6, 69.5, 83.4, and $97.3^\circ\text{C}$).

### 2.5.3. Parametric study on the effects of unbonded IRP-host pipe interface
A total of 49 linear and nonlinear stress analyses were conducted to study the effects of the presence of an unbonded segment on the axial displacements and stresses of IRP systems with a circumferential discontinuity under temperature changes. Various values selected for geometrical and material characteristics of the system are given in Table 8. Two $\Delta T$ values equal to $27.8$ and $97.3^\circ\text{C}$ were considered to cover both seasonal and extreme temperature changes. The $\Delta T$ value of $97.3^\circ\text{C}$, which is 3.5 times the maximum seasonal variations, was selected as the representative extreme temperature change which may occur due to exposure of the pipeline to adjacent high-temperature steam pipes. For the linear analyses, three different values were assigned to the MoE of IRP (1, 3.77, and 10 GPa). For nonlinear analyses, ALTRA10® was chosen as IRP. Two modes of unbonding were considered as shown in Figure 7.

## 3. Results and discussion
### 3.1. Peak axial stress in IRP
#### 3.1.1. Variations of applied load ($f_T$) with geometrical and material properties
The value of tensile force per unit area of the cross section ($f_T$) which must be applied on the pipe’s free end with a circumferential host-pipe discontinuity in an “equivalent” mechanical model to achieve equal level of axial deformation due to the temperature change can be calculated using Equation (7). Effects of MoE and CTE of IRP on $f_T$ are depicted in Figure 8. The increase of both CTE and MoE of IRP results in increasing $f_T$. As the MoE increases, the effect of the CTE on $f_T$ becomes more significant implying that the stiffer the IRP material, the more effective is the CTE on the value of the $f_T$. The reason is that, for a linear material behaviour, thermal stress is linearly proportional to both MoE and CTE. Consequently, the change of thermal stress due to the change of CTE is more highlighted when the MoE is higher. Figure 9(a) indicates that the host pipe’s outer diameter does not have a significant effect on $f_T$. However, according to Figure 9(b), the wall thicknesses of host pipe and IRP both can have a considerable effect on $f_T$. If the host pipe’s wall thickness is small ($t_H = 6.35$ mm), the increase of IRP’s wall thickness leads to decreasing $f_T$. On the contrary, for a large value of the host pipe thickness ($t_H = 18.80$ mm), the increase in IRP thickness results in the increase of $f_T$.

<table>
<caption>Table 8. Geometrical and material properties of 87 FE models to study the effects of unbonded interface.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Unit</th>
<th>Value(s)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus of IRP</td>
<td>$E_I$</td>
<td>GPa</td>
<td>1, 3.77, 10</td>
</tr>
<tr>
<td>Unbonding mode (Figure 7)</td>
<td>–</td>
<td>–</td>
<td>One-sided, Two-sided</td>
</tr>
<tr>
<td>Unbonded length (Figure 7)</td>
<td>$l_u$</td>
<td>mm</td>
<td>0, 12.7, 25.4, 50.8, 76.2, 101.6, 127.0</td>
</tr>
<tr>
<td>Unbonded length to discontinuity width ratio</td>
<td>$l_u/c$</td>
<td>–</td>
<td>0, 1, 2, 4, 6, 8, 10</td>
</tr>
<tr>
<td>Material behaviour</td>
<td>–</td>
<td>–</td>
<td>Linear, Nonlinear</td>
</tr>
<tr>
<td>Poisson's ratio of IRP</td>
<td>$ν_I$</td>
<td>–</td>
<td>0.23</td>
</tr>
<tr>
<td>CTE of IRP</td>
<td>$α_I$</td>
<td>1/°C</td>
<td>$45 × 10^{-6}$</td>
</tr>
<tr>
<td>Wall thickness of IRP</td>
<td>$t_I$</td>
<td>mm</td>
<td>4.115</td>
</tr>
<tr>
<td>Young's modulus of the host pipe</td>
<td>$E_H$</td>
<td>GPa</td>
<td>210.7</td>
</tr>
<tr>
<td>Poisson's ratio of the host pipe</td>
<td>$ν_H$</td>
<td>–</td>
<td>0.3</td>
</tr>
<tr>
<td>CTE of the host pipe</td>
<td>$α_H$</td>
<td>1/°C</td>
<td>$12 × 10^{-6}$</td>
</tr>
<tr>
<td>Outer diameter of the host pipe</td>
<td>$D_{oH}$</td>
<td>mm</td>
<td>323.85</td>
</tr>
<tr>
<td>Wall thickness of the host pipe</td>
<td>$t_H$</td>
<td>mm</td>
<td>6.35</td>
</tr>
<tr>
<td>Discontinuity width</td>
<td>$c$</td>
<td>mm</td>
<td>12.7</td>
</tr>
<tr>
<td>Pipe length</td>
<td>$L$</td>
<td>mm</td>
<td>3048</td>
</tr>
</tbody>
</table>

![](./images/1000432425769107467_16.jpg)

Figure 8. The change of $f_T$ with material properties ($D_{oH}=323.5$mm, $t_H=6.35$mm).

### 3.1.2. Geometrical effects on the value of parameter $\lambda$
According to Equation (8), parameter $\lambda$ is the ratio of nominal axial stress of IRP in the discontinuity segment to the value of $f_T$ :

$$
\lambda = \frac{(\sigma_n)_I}{f_T} \tag{30}
$$

Using Equation (9), values of the parameter $\lambda$ can be calculated as a function of the host pipe's outer diameter ($D_{oH}$), host pipe's wall thickness ($t_H$), and IRP's wall thickness ($t_I$). Figure 10 clearly shows that the increase of IRP's wall thickness leads to the decrease of $\lambda$, and the host pipe's diameter does not have a significant effect on $\lambda$ (Figure 10(a)); while the increase of host pipe's wall thickness results in the increase of $\lambda$ (Figure 10(b)).

### 3.1.3. Geometrical effects on parameter $\eta$ and design values
According to Equation (10), the parameter $\eta$ can be defined as the ratio of the average value of axial stress along the wall thickness of IRP to the nominal value of axial stress at the discontinuity segment:

$$
\eta = \frac{(\sigma_a)_I}{(\sigma_n)_I} \tag{31}
$$

Values of the parameter $\eta$ were extracted from linear elastic FE stress analyses carried out on 134 models with various material and geometrical properties. With the increase of the discontinuity width, parameter $\eta$ is less affected by the geometrical characteristics of host pipe and IRP (Figure 11(a)). The reason is that, as explained in Section 3.1.5, the increase of discontinuity width generally leads to the decrease of stress concentration at the regions adjacent to the discontinuity edge which eventually leads to a more uniform stress distribution along the wall thickness of IRP. Consequently, the average axial stress along the IRP thickness becomes closer to the nominal stress at the discontinuity segment, and due to this, the value of the $\eta$ approaches unity. For example, for $c=6.35$ mm ($\zeta=1$), the value of the $\eta$ ranges between 0.865 and 1.073 for different IRP thicknesses. However, for $c=152.4$mm ($\zeta=24$), the range of the $\eta$ is between 1.000 and 1.011. MoE of IRP and host pipe do not have a significant effect on parameter $\eta$. Based on FE results (Figure 11(b)), a maximum $\eta$ value of 1.08 is recommended for design purposes.

### 3.1.4. Variations of hot-spot and nominal stresses with geometrical characteristics
Figure 12 shows the change of nominal and hot-spot stresses with the parameters $\tau$ and $\zeta$. As the value of $\tau$ increases, both nominal and hot-spot stresses decrease. This is an expected result; since the increase of the $\tau$, if the host pipe thickness is fixed, results in the increase of IRP's wall thickness that obviously results in the decrease of the axial stresses of IRP at the discontinuity segment. This result does not depend on the value of $\zeta$, and hence the discontinuity width. Designers can use Equation (12) to calculate the HSS of IRP, and then utilise the obtained HSS along with the S-N curve of the IRP material to estimate the design fatigue life of the system.

### 3.1.5. Effects of discontinuity width on the stress distribution along the IRP thickness
Figure 13 compares the distributions of axial stress along the IRP's wall thickness for various values of discontinuity width. The most uniform pattern is observed for $\zeta=24$, while the

![](./images/1000432425769107467_17.jpg)

![](./images/1000432425769107467_18.jpg)

Figure 9. Effects of geometrical properties on the $f_T$ for different values of the IRP thickness: (a) effect of the outer diameter of the host pipe, (b) effect of the wall thickness of the host pipe.

![](./images/1000432425769107467_19.jpg)

![](./images/1000432425769107467_20.jpg)

Figure 10. Variations of the parameter $\lambda$ with geometrical characteristics: (a) effects of the IRP thickness and its interactions with the host pipe diameter ($t_H =$ 6.35 mm), (b) effects of the IRP thickness and its interactions with the host pipe thickness ($D_{oH} = 323.85$ mm).

harshest variations are detected for $\zeta = 1$ which means that as the discontinuity width increases, the stress distribution along the IRP's wall thickness becomes closer to a uniform pattern. The reason is that, on an average basis, as the discontinuity width increases, the stress concentration at the regions adjacent to the discontinuity edge decreases. This leads to the decrease of the axial stress on the outer surface of IRP which consequently results in the decrease of difference between stresses on the outer and inner surfaces of IRP leading to a more uniform stress distribution along the IRP thickness. It can be observed that for $\zeta = 24$, axial stress is perfectly uniform (constant) along the thickness of IRP.

### 3.1.6. Effects of nondimensional geometrical parameters on the SCF values

Nondimensional geometrical parameters are defined in Equation (29), and the SCF is defined in Equation (20). For a constant wall thickness of host pipe, the increase of the $\tau$ leads to the increase of IRP's wall thickness. Figure 14 depicts the change of SCF values due to the change of the $\tau$. The increase of the $\tau$ results in the increase of the SCF at the discontinuity edge in an IRP system. With the increase of the $\tau$ and consequently the IRP thickness, the axial stiffness of the discontinuity segment increases. It is well-documented that with the increase of stiffness, the stress

![](./images/1000432425769107467_21.jpg)

Figure 11. (a) Effects of the IRP thickness and discontinuity width on the values of the parameter η, (b) change of the parameter η in 44 FE models with the same material properties and different geometrical characteristics.

![](./images/1000432425769107467_22.jpg)

Figure 12. The change of: (a) nominal stress and (b) hot-spot stress with the parameters τ and ζ.

![](./images/1000432425769107467_23.jpg)

Figure 13. Effects of discontinuity width on the stress distribution along the IRP thickness ($\tau = 0.65$, $f_T = 1$ MPa).

![](./images/1000432425769107467_24.jpg)

*(a) $\zeta = 1$*

![](./images/1000432425769107467_25.jpg)

*(b) $\zeta = 2$*

![](./images/1000432425769107467_26.jpg)

*(c) $\zeta = 24$*

Figure 14. Effect of the parameter $\tau$ on the SCFs and the interaction of this parameter with the $\zeta$.

concentration decreases at a sharp notch. For example, Ahmadi et al. (2012b) observed such behaviour during their research on reinforcing tubular joints with internal ring stiffeners. The magnitude of such increase is greatly affected by parameter $\zeta$. If the host pipe's wall thickness is fixed, the increase of the $\zeta$ leads to the increase of the discontinuity width. Figure 14 shows that as the value of $\zeta$ increases, parameter $\tau$ has less effect on the SCF. For $\zeta = 24$, the SCF remains almost unchanged as the IRP's wall thickness increases, while for $\zeta = 1$, the SCF for $\tau = 1.65$ is over twice the corresponding value for $\tau = 0.4$.

For a constant host pipe diameter, the thickness of the host pipe decreases with the increase of $\gamma$. FE results indicated that the SCF at the discontinuity edge generally increases with the increase of the $\gamma$. The reason is that with the increase of the $\gamma$ resulting in the decrease of the host pipe's wall thickness, the axial stiffness of the discontinuity segment decreases leading to the increase of the stress concentration at the edge as explained before. However, the amount of the increase is so small that it can be safely considered to be negligible. The reason behind such small changes of SCF due to the change of the $\gamma$ is that the stiffness of the discontinuity segment is primarily controlled by the axial stiffness of IRP rather than the host pipe. If the host pipe's diameter is fixed, the increase of the $\alpha$ results in the increase of the pipe length. Analysis results indicated that the parameter $\alpha$ has no effect on the SCF at the discontinuity edge. The main reason is that the change of pipe length cannot affect the stiffness of discontinuity segment and hence does not considerably influence the stress concentration at the discontinuity edge.

### 3.1.7. Design SCFs
With a hypothesis test outcome of 0 (accept), results of the Kolmogorov-Smirnov (K-S) goodness-of-fit test conducted on the generated SCF sample showed that the SCFs at the discontinuity edge in an IRP system follow a normal probability distribution. The $p$ value was equal to 0.0253; and the test statistic and critical value were 0.2409 and 0.2212, respectively. Details of the testing approach are given in Section 2.4. Hence, an estimation for the maximum expected value of the SCF can be obtained using Equation (28). Values of the mean, standard deviation, and coefficient of variations for the generated SCF sample were equal to 1.85, 0.23, and 12.3%, respectively; and the maximum expected value of the SCF was obtained as 2.53. The range of validity for geometrical parameters of these statistical measures is given in Equation (32). The probability of observing an SCF value that exceeds the estimated maximum expected value (2.53) is only 0.15%:

$$
\begin{aligned}
0.4 &\leq \tau\left(=\frac{t_{I}}{t_{H}}\right) \leq 1.65 \\
1 &\leq \zeta\left(=\frac{c}{t_{H}}\right) \leq 24 \\
11.1 &\leq \gamma\left(=\frac{D_{o H}}{2 t_{H}}\right) \leq 45 \\
18.8 &\leq \alpha\left(=\frac{2 L}{D_{o H}}\right) \leq 300
\end{aligned} \tag{32}
$$

### 3.2. Discontinuity opening

#### 3.2.1. The change of applied displacement $(\delta_{T})$ with geometrical and material properties
According to Equation (3), the axial displacement $(\delta_{T})$ which must be applied on the pipe's free end in a mechanical model to replicate the system's axial deformation under the temperature variation depends on the discontinuity width $(c)$, pipe length $(L)$, and temperature change $(\Delta T)$ as well as the cross-sectional area, MoE, and CTE of IRP and host pipe. Figure 15 shows that the increase of the IRP thickness, discontinuity width, and MoE of IRP all result in the increase of the $\delta_{T}$.

#### 3.2.2. Effects of material and geometrical properties on parameter $\mu$
The parameter $\mu$ is defined as the ratio of the nominal value of discontinuity opening to the $\delta_{T}$ value (Equation (13)):

$$
\mu = \frac{(\delta_{c})_{n}}{\delta_{T}} \tag{33}
$$

![](./images/1000432425769107467_27.jpg)

Figure 15. (a) Effects of the IRP thickness and discontinuity width on the values of the $\delta_T$, (b) effects of the thickness and MoE of IRP on the values of the. $\delta_T$

![](./images/1000432425769107467_28.jpg)

Figure 16. The change of nominal discontinuity opening with the IRP thickness and: (a) discontinuity width, (b) MoE of IRP; variations of the parameter $\mu$ with the IRP thickness and (c) discontinuity width, (d) MoE of IRP.

The parameter $\mu$ is a function of the discontinuity width (c) and pipe length ($L$) as well as the cross-sectional area and MoE host pipe and IRP. Figure 16 indicates that the increase of IRP's MoE and thickness both results in the decrease of the nominal value of discontinuity opening and the parameter $\mu$; while the increase of the discontinuity width increases both the nominal value of discontinuity opening and the parameter $\mu$.

### 3.2.3. The parameter $\boldsymbol{\psi}$ : material and geometrical effects and design formulation
According to Equation (15), the parameter $\psi$ can be defined as the ratio of actual to nominal values of the discontinuity opening:

$$
\psi=\frac{\delta_{c}}{\left(\delta_{c}\right)_{n}} \tag{34}
$$

Figure 17(a) indicates that the increase of the IRP thickness results in the decrease of the FE-driven values of the actual discontinuity opening; while, the increase of the discontinuity width leads to the increase of the actual discontinuity opening. Conversely, as shown in Figure 17(b), the value of the $\psi$ increases with the increase of the IRP thickness, while the increase of the discontinuity width reduces the value of the parameter $\psi$. This is because the increase of the IRP thickness results in the increase of the stress concentrations in the discontinuity segment due to the increase of the $\tau$, while the increase of the discontinuity width generally reduces the stress concentration. Figure 18 shows that, as expected, the increase of the MoE of IRP leads to the decrease of the actual discontinuity opening. However, the value of the parameter $\psi$ increases with the increase of the MoE of IRP.

#### 3.2.3.1. Type I circumferential discontinuity: fracture.
For the representation of a circumferential fracture as a result of impact, buckling, or fatigue crack propagation, the discontinuity width was selected to be equal to 6.35 mm (1/4 in.). Based on Figure 19, the following equation is suggested for calculating the parameter $\psi$ for a Type I circumferential discontinuity:

$$
\psi=c_{1} \tau^{3}+c_{2} \tau^{2}+c_{3} \tau+c_{4} ; \quad \tau=\frac{t_{I}}{t_{H}} \tag{35}
$$

where the coefficients $c_{1}$ to $c_{4}$ can be calculated using the following equation (Figure 20):

$$
\begin{aligned}
& c_{i}=\varphi_{i} e^{3}+\vartheta_{i} e^{2}+\xi_{i} e+\omega_{i} ; \quad e=\frac{E_{I}}{E_{I[\mathrm{ref}]}} ; \\
& E_{I[\mathrm{ref}]}=10 \mathrm{GPa} ; \quad i=1,2,3,4
\end{aligned} \tag{36}
$$

in which, coefficients $\varphi_{i}, \vartheta_{i}, \xi_{i}$, and $\omega_{i}$ are obtained by:

$$
\begin{aligned}
{[\boldsymbol{\varphi}]_{\text {Type I }} } & =\left[\begin{array}{l}
\varphi_{1} \\
\varphi_{2} \\
\varphi_{3} \\
\varphi_{4}
\end{array}\right]=\left[\begin{array}{r}
0.2062 \\
-0.5818 \\
0.5300 \\
-0.1238
\end{array}\right] ; \\
{[\boldsymbol{\vartheta}]_{\text {Type I }} } & =\left[\begin{array}{l}
\vartheta_{1} \\
\vartheta_{2} \\
\vartheta_{3} \\
\vartheta_{4}
\end{array}\right]=\left[\begin{array}{r}
-2.1067 \\
5.9948 \\
-5.5679 \\
1.2649
\end{array}\right] \\
{[\boldsymbol{\xi}]_{\text {Type I }} } & =\left[\begin{array}{l}
\xi_{1} \\
\xi_{2} \\
\xi_{3} \\
\xi_{4}
\end{array}\right]=\left[\begin{array}{r}
5.5974 \\
-16.403 \\
15.770 \\
-3.0065
\end{array}\right] ; \\
{[\boldsymbol{\omega}]_{\text {Type I }} } & =\left[\begin{array}{l}
\omega_{1} \\
\omega_{2} \\
\omega_{3} \\
\omega_{4}
\end{array}\right]=\left[\begin{array}{r}
-2.6464 \\
6.5157 \\
-3.8813 \\
3.8265
\end{array}\right]
\end{aligned} \tag{37}
$$

#### 3.2.3.2. Type II circumferential discontinuity: joint.
For the representation of a circumferential discontinuity at bell and spigot joints, a 12.7-mm (1/2-in.) discontinuity width was assumed. According to Figures 21 and 22, Equations (35) and (36) can still be used to calculate the parameter $\psi$ for a Type II circumferential discontinuity. Values of the coefficients $\varphi_{i}, \vartheta_{i}, \xi_{i}$, and $\omega_{i}$ for a Type II circumferential discontinuity can be obtained from Equation (38). Note that according to Figure 21, the value of $c_{1}$ for the Type II circumferential discontinuity is equal to zero:

$$
\begin{aligned}
{[\boldsymbol{\varphi}]_{\text {Type II }} } & =\left[\begin{array}{l}
\varphi_{1} \\
\varphi_{2} \\
\varphi_{3} \\
\varphi_{4}
\end{array}\right]=\left[\begin{array}{l}
0.0000 \\
0.0000 \\
0.0000 \\
0.0000
\end{array}\right] ; \\
{[\boldsymbol{\vartheta}]_{\text {Type II }} } & =\left[\begin{array}{l}
\vartheta_{1} \\
\vartheta_{2} \\
\vartheta_{3} \\
\vartheta_{4}
\end{array}\right]=\left[\begin{array}{r}
0.0000 \\
0.0604 \\
-0.1875 \\
0.0404
\end{array}\right]
\end{aligned}
$$

![](./images/1000432425769107467_29.jpg)

Figure 17. Effects of the IRP thickness and discontinuity width on the value of: (a) actual discontinuity opening, (b) parameter $\psi$.

![](./images/1000432425769107467_30.jpg)

(a) $c = 6.35$ mm [1/4 in.]

![](./images/1000432425769107467_31.jpg)

(b) $c = 6.35$ mm [1/4 in.]

![](./images/1000432425769107467_32.jpg)

(c) $c = 12.7$ mm [1/2 in.]

![](./images/1000432425769107467_33.jpg)

(d) $c = 12.7$ mm [1/2 in.]

![](./images/1000432425769107467_34.jpg)

(e) $c = 152.4$ mm [6 in.]

![](./images/1000432425769107467_35.jpg)

(f) $c = 152.4$ mm [6 in.]

Figure 18. Effects of the IRP thickness and MoE on the values of the actual discontinuity opening and the parameter $\psi$ for different discontinuity widths.

![](./images/1000432425769107467_36.jpg)

(a) IRP MoE = 1 GPa

![](./images/1000432425769107467_37.jpg)

(b) IRP MoE = 3.77 GPa

![](./images/1000432425769107467_38.jpg)

(c) IRP MoE = 10 GPa

![](./images/1000432425769107467_39.jpg)

(d) IRP MoE = 15 GPa

![](./images/1000432425769107467_40.jpg)

(e) IRP MoE = 24.5 GPa

![](./images/1000432425769107467_41.jpg)

(f) IRP MoE = 69 GPa

Figure 19. Formulation of the $\psi$ as a function of the $\tau$ for different IRP MoE values in Type I discontinuity ($c = 6.35$ mm).

$$
\begin{aligned}
{[\boldsymbol{\xi}]_{\text {Type II }}} & =\left[\begin{array}{l}
\xi_{1} \\
\xi_{2} \\
\xi_{3} \\
\xi_{4}
\end{array}\right]=\left[\begin{array}{r}
0.0000 \\
-0.5911 \\
1.6506 \\
-0.0925
\end{array}\right] ; \\
{[\boldsymbol{\omega}]_{\text {Type II }}} & =\left[\begin{array}{l}
\omega_{1} \\
\omega_{2} \\
\omega_{3} \\
\omega_{4}
\end{array}\right]=\left[\begin{array}{l}
0.0000 \\
0.0336 \\
0.9205 \\
0.9237
\end{array}\right]
\end{aligned}\tag{38}
$$

$$
\begin{aligned}
{[\boldsymbol{\vartheta}]_{\text {Type III }}} & =\left[\begin{array}{l}
\vartheta_{1} \\
\vartheta_{2} \\
\vartheta_{3} \\
\vartheta_{4}
\end{array}\right]=\left[\begin{array}{r}
0.0000 \\
0.0037 \\
-0.0086 \\
0.0015
\end{array}\right] \\
{[\boldsymbol{\xi}]_{\text {Type III }}} & =\left[\begin{array}{l}
\xi_{1} \\
\xi_{2} \\
\xi_{3} \\
\xi_{4}
\end{array}\right]=\left[\begin{array}{r}
0.0000 \\
-0.0228 \\
0.0589 \\
0.0001
\end{array}\right] ; \\
{[\boldsymbol{\omega}]_{\text {Type III }}} & =\left[\begin{array}{l}
\omega_{1} \\
\omega_{2} \\
\omega_{3} \\
\omega_{4}
\end{array}\right]=\left[\begin{array}{l}
0.0000 \\
0.0050 \\
0.0049 \\
1.0998
\end{array}\right]
\end{aligned}\tag{39}
$$

3.2.3.3. Type III circumferential discontinuity: aging. A width of 152.4 mm (6 in.) was assumed for the representation of a circumferential discontinuity as a result of the elimination of a significant portion of host pipe due to aging. According to Figures 23 and 24, Equations (35) and (36) can still be used to calculate the parameter $\psi$ for a Type III circumferential discontinuity. Values of the coefficients $\varphi_{i}, \vartheta_{i}, \xi_{i}$, and $\omega_{i}$ for a Type III circumferential discontinuity can be obtained from Equation (39). Note that according to Figure 23, the value of $c_{1}$ for the Type III circumferential discontinuity is equal to zero:

$$
[\boldsymbol{\varphi}]_{\text {Type III }}=\left[\begin{array}{l}
\varphi_{1} \\
\varphi_{2} \\
\varphi_{3} \\
\varphi_{4}
\end{array}\right]=\left[\begin{array}{l}
0.0000 \\
0.0000 \\
0.0000 \\
0.0000
\end{array}\right] ;
$$

High values achieved for the determination coefficients $(R^{2}$ > 0.90) for Equations (35)-(39) can guaranty the accuracy of the fit (Figures 19-24). The validity ranges for the applicability of Equations (35)-(39) are $0.4 \leq \tau \leq 1.65$ and $1 \text{ GPa} \leq E_{I} \leq$ 69 GPa covering a wide range of practical applications.

After calculating the $\psi$, designers can use Equation (16) for the calculation of actual discontinuity opening $(\delta_{c})$ corresponding to the three different types of circumferential discontinuity expected to occur due to the fracture, joints, and aging. Afterwards, they can divide the $\delta_{c}$ by the appropriate discontinuity width (depending on the type of discontinuity) to obtain an estimation of critical axial strain, and then compare it with the failure strain of IRP material in

![](./images/1000432425769107467_42.jpg)

Figure 20. Formulation of the coefficients $c_1$ to $c_4$ in Equation (35) as a function of the MoE of IRP in Type I discontinuity ($c = 6.35$ mm).

order to approximate the margin of safety for their design and revise it if required.

### 3.3. Effects of the internal pressure of the pipe on the axial behaviour
Altogether, 45 linear elastic FE analyses were carried out to investigate the effects of the pipe's internal pressure on the axial stress of IRP and discontinuity opening. In this study, the influences of the IRP thickness, host pipe diameter, MoE of IRP, and the discontinuity width over the effect of the internal pressure were also investigated.

#### 3.3.1. Variations of the axial stress at the discontinuity segment with the internal pressure
Figure 25(a) demonstrates the effect of the pipe's internal pressure on the average axial stress along the wall thickness of IRP in the discontinuity segment's midspan, $(\sigma_a)_I$, as the thickness of IRP increases. The increase of internal pressure results in the increase of axial stress. However, the maximum difference between the axial stresses in the models with and without the inclusion of the pipe's internal pressure is only 8% (Figure 25(d)). It can also be observed in Figure 25(d) that as the IRP thickness increases, pipe's internal pressure has less effect on the axial stress. Figure 25(b) depicts the effect of the pipe's internal pressure on the value of $(\sigma_a)_I$ as the diameter of host pipe increases.
According to Figure 25(b), up to a certain level of internal pressure, the increase of the host pipe diameter leads to the decrease of the axial stress, while beyond this certain level, the increase of the diameter leads to the increase of the axial stress in the discontinuity segment.

Figure 25(e) indicates that with the increase of the host pipe's outer diameter from 323.85 to 571.50 mm, the maximum difference between the axial stresses in models with and without the inclusion of the pipe's internal pressure increases from 8% to 16%. Figure 25(c) shows that IRP's MoE does not have a significant influence over the effect of internal pressure on the axial stress. According to Figure 25(f), with the increase of MoE from 1 to 10 GPa, the maximum difference between the axial stresses in models with and without the inclusion of the pipe's internal pressure increases by only 1%. Analysis results also showed that as the discontinuity width increases, the effect of internal pressure on the axial stress becomes more significant. For example, with the increase of the discontinuity width from 6.35 to 152.4 mm (0.25 to 6 in.), the maximum difference between the axial stresses in models with and without the inclusion of the pipe's internal pressure increases from 8% to over 24%.

#### 3.3.2. Effects of the pipe's internal pressure on discontinuity opening
Figure 26(a) depicts the effect of the pipe's internal pressure on the discontinuity opening $(\delta_c)$ for different values of the

![](./images/1000432425769107467_43.jpg)

(a) IRP MoE = 1 GPa

![](./images/1000432425769107467_44.jpg)

(b) IRP MoE = 3.77 GPa

![](./images/1000432425769107467_45.jpg)

(c) IRP MoE = 10 GPa

![](./images/1000432425769107467_46.jpg)

(d) IRP MoE = 15 GPa

![](./images/1000432425769107467_47.jpg)

(e) IRP MoE = 24.5 GPa

![](./images/1000432425769107467_48.jpg)

(f) IRP MoE = 69 GPa

Figure 21. Formulation of the $\psi$ as a function of the $\tau$ for different IRP MoE values in Type II discontinuity ($c = 12.7$ mm).

![](./images/1000432425769107467_49.jpg)

(a) $c_2$

![](./images/1000432425769107467_50.jpg)

(b) $c_3$

![](./images/1000432425769107467_51.jpg)

(c) $c_4$

Figure 22. Formulation of the coefficients $c_2$ to $c_4$ in Equation (35) as a function of the MoE of IRP in Type II discontinuity ($c = 12.7$ mm); For a Type II discontinuity: $c_1 = 0$.

IRP thickness. The increase of the internal pressure leads to the increase of the discontinuity opening (Figure 26(a)), and the maximum difference between the discontinuity openings in the models with and without the inclusion of the pipe's internal pressure is around 10% (Figure 26(d)). Figure 26(d) also indicates that as the IRP thickness increases, the internal pressure of the pipeline becomes less effective on the amount of discontinuity opening. Figure 26(b) shows the effect of the pipe's internal pressure on the value of $\delta_c$ as the diameter of host pipe increases. Figure 26(e) indicates that with the increase of the host pipe's outer diameter from 323.85 to 571.50 mm, the maximum difference between the discontinuity opening values in models with and without the inclusion of the pipe's internal pressure increases from 11% to 19%. MoE of IRP does not have a significant influence over the effect of pipe's internal pressure on the discontinuity opening. As the width of discontinuity increases, the effect of internal pressure on the discontinuity opening becomes more significant. As an example, as can be observed in Figure 26(f), with the increase of the

![](./images/1000432425769107467_52.jpg)

(a) IRP MoE = 1 GPa

![](./images/1000432425769107467_53.jpg)

(b) IRP MoE = 3.77 GPa

![](./images/1000432425769107467_54.jpg)

(c) IRP MoE = 10 GPa

![](./images/1000432425769107467_55.jpg)

(d) IRP MoE = 15 GPa

![](./images/1000432425769107467_56.jpg)

(e) IRP MoE = 24.5 GPa

![](./images/1000432425769107467_57.jpg)

(f) IRP MoE = 69 GPa

Figure 23. Formulation of the $\psi$ as a function of the $\tau$ for different IRP MoE values in Type III discontinuity ($c = 152.4$ mm).

![](./images/1000432425769107467_58.jpg)

(a) $c_2$

![](./images/1000432425769107467_59.jpg)

(b) $c_3$

![](./images/1000432425769107467_60.jpg)

(c) $c_4$

Figure 24. Formulation of the coefficients $c_2$ to $c_4$ in Equation (35) as a function of the MoE of IRP in Type III discontinuity ($c = 152.4$ mm); for a Type III discontinuity: $c_1 = 0$.

discontinuity width from 6.35 to 152.4 mm (0.25 to 6 in.), the maximum difference between the discontinuity opening values in models with and without the inclusion of the pipe's internal pressure increases from 8% to over 18%.

circumferential discontinuity. In this study, two different materials were considered for host pipe: X42 steel and cast iron. ALTRA10$^\circledR$ was chosen as IRP because it has been previously proposed for the repair of water pipelines (Bureau et al., 2021) and its nonlinear stress-strain curve is available.

### 3.4. Effects of material and geometric nonlinearities on the axial behaviour

Altogether, 42 linear and nonlinear FE analyses were conducted to study the effects of material and geometric nonlinearities on the IRP's axial stress and opening of a

#### 3.4.1. Nonlinearity effects on the IRP's axial stress at the discontinuity segment

Figure 27 depicts the effects of material and geometric nonlinearities on the average axial stress along the wall thickness IRP in the midspan of discontinuity segment, $(\sigma_a)_I$, as

![](./images/1000432425769107467_61.jpg)

Figure 25. (a) The effect of internal pressure on the average axial stress along the IRP thickness in the Middle section of the discontinuity segment and its interaction with the (a) IRP thickness, (b) outer diameter of the host pipe, (c) IRP's elastic modulus; the ratio of the axial stress subjected to an arbitrary internal pressure to the axial stress subjected to zero internal pressure for different values of the (d) IRP thickness, (e) outer diameter of the host pipe, (f) IRP's elastic modulus.

the value of applied displacement increases. The value of applied displacement can be calculated based on Equation (3). It is the magnitude of axial displacement which must be applied to the pipe's free end in a mechanical model to rep- licate the system's axial deformation under the temperature variation $(\Delta T)$. Values of applied displacement in Figures 27 and 28 cover $\Delta T$ values ranging from 13.9 to $97.3^{\circ} C$.

According to Figure 27, the difference between nonlinear and linear solutions of the axial stress increases with the increase of the applied displacement. This means that as the value of $\Delta T$ increases, material nonlinearities affect IRP's axial stress more significantly. Hence, nonlinear material behaviour of host pipe and IRP should be included in analy- sing the pipeline repair systems under extreme temperature variations. The nonlinear solution of axial stress is always lower than the corresponding linear solution. The main rea- son is that when the material nonlinearity is considered, the structural system becomes more compliant resulting in greater deformations through which the energy exerted by applied loads is dissipated and consequently, the structural system is less reactive in terms of internal forces leading to the decrease of stresses.

For example, in a system with the steel host pipe, for a $\Delta T$ value of $97.3^{\circ} C$ which is corresponding to an applied displacement of 3.71 mm, nonlinear solution of the ALTRA10 $^{\circledR}$ IRP's axial stress is only $37\%$ of the corresponding linear solution. For a cast iron host pipe, this ratio is around $46\%$. Hence, it can be concluded that an IRP system with a steel host pipe is more affected by the nonlin- ear material behaviour compared to the corresponding sys- tem with a cast iron host pipe. It can also be observed in Figure 27 that if the maximum applied displacement is lim- ited to 3.71 mm, there is no considerable difference between the small- and large-displacement solutions, which implies that up to a $\Delta T$ value of $97.3^{\circ} C$, geometric nonlinearity has almost no effect on the axial stress of IRP in the discontinu- ity segment.

It should be noted that major difference observed between nonlinear and linear behaviours of ALTRA10 $^{\circledR}$ IRP in terms of axial stress does not invalidate the developed analytical solution and modification factors $\eta$ and SCF extracted from linear FE analyses. There are several IRP materials which do not exhibit significantly nonlinear behaviour up to the point of failure. Hence, the developed analytical solution is accurate for such IRP systems. For IRP materials with considerably nonlinear behaviour, Equation (12) results in a conservative estimation of peak axial stress which does not compromise a safe design.

### 3.4.2. Nonlinearity effects on the discontinuity opening

Figure 28 indicates that the difference between the linear and nonlinear solutions of discontinuity opening increases

![](./images/1000432425769107467_62.jpg)

![](./images/1000432425769107467_63.jpg)

![](./images/1000432425769107467_64.jpg)

![](./images/1000432425769107467_65.jpg)

![](./images/1000432425769107467_66.jpg)

![](./images/1000432425769107467_67.jpg)

Figure 26. (a) The effect of internal pressure on the discontinuity opening and its interaction with the (a) IRP thickness, (b) outer diameter of the host pipe, (c) discontinuity width; the ratio of the discontinuity opening subjected to an arbitrary internal pressure to the discontinuity opening subjected to zero internal pressure for different values of the (d) IRP thickness, (e) outer diameter of the host pipe, (f) discontinuity width.

with the increase of the applied displacement, implying that as the $\Delta T$ increases, material nonlinearities affect the discontinuity opening more significantly. The nonlinear solution of the discontinuity opening is always larger than the corresponding linear solution. For example, in a system with the cast iron host pipe, for a $\Delta T$ value of $97.3\ \mathrm{^\circ C}$ which is corresponding to an applied displacement of 3.40 mm, nonlinear solution of the discontinuity opening is 1.95 times the corresponding linear solution. For a steel host pipe, this ratio is around 1.91. It can also be observed that up to a $\Delta T$ value of $97.3\ \mathrm{^\circ C}$, geometric nonlinearity does not have a considerable effect on the amount of discontinuity opening.

Considerable difference between nonlinear and linear behaviours of an ALTRA10$^\circledR$ IRP system in terms of discontinuity opening does not mean that the developed analytical solution and modification factor $\psi$ extracted from linear FE analyses are invalid. Many IRP materials do not exhibit significantly nonlinear behaviour up to the point of failure, and hence, the developed analytical solution is accurate for such IRP systems. For IRP materials with significantly nonlinear behaviour, Equation (16) tends to underestimate the maximum discontinuity opening and users may have to apply a factor of safety for design purposes. It should also be noted that such nonlinear effects are more highlighted for extreme rather than seasonal temperature changes.

In linear FE models, the ratio of discontinuity opening to applied displacement is always fixed, and for the specific geometrical and material properties used in Figures 27 and 28, this ratio is equal to 0.419 and 0.379 for steel and cast iron host pipes, respectively. In nonlinear FE models, the ratio of discontinuity opening to applied displacement increases with the amount of applied displacement, and it's always higher than the corresponding ratio from a linear analysis. For the specific geometrical and material properties used in Figures 27 and 28, this nonlinear ratio for a system with the steel host pipe ranges between 0.493 and 0.802 with an average value of 0.702 which is 40% higher than the corresponding linear ratio. In a system with the cast iron host pipe, nonlinear ratio varies between 0.410 and 0.739 with an average value of 0.625 which is 39% higher than the corresponding linear ratio.

### 3.5. Effects of the unbonded interface on the axial behaviour

#### 3.5.1. Effects of unbonded length on linear and nonlinear axial responses

Figures 29 and 30 demonstrate the effects of the presence of an unbonded segment on linear and nonlinear axial behaviours of IRP systems under seasonal and extreme temperature variations. Figure 29 indicate that the increase of

![](./images/1000432425769107467_68.jpg)
![](./images/1000432425769107467_69.jpg)

![](./images/1000432425769107467_70.jpg)
![](./images/1000432425769107467_71.jpg)

Figure 27. (a) And (b) effects of material and geometric nonlinearities on the average axial stress along the IRP thickness in the Middle section of the discontinuity segment, (c) and (d) the ratio of axial stress obtained from a nonlinear FE analysis to the corresponding value extracted from a linear FE analysis.

unbonded length can result in significant decrease of the axial stress of IRP in the discontinuity segment. Comparison of Figure 29(b,d) shows that if the material behaviour is linear, the amount of stress decrement is the same for seasonal and extreme temperature changes, where the ratio of the axial stress in a system with an unbonded segment to the corresponding axial stress in a fully bonded system ranges between 0.83 (for $l_u/c=1$) and 0.31 (for $l_u/c=10$). However, if the nonlinear material behaviour is included, then the increase of the unbonded length subjected to an extreme temperature change has greater effect over the axial response compared to the seasonal temperature change, where the maximum difference between the axial stresses in unbonded and fully bonded systems is 55% and 60% for seasonal and extreme temperature changes, respectively.

Figure 30 illustrates that the increase of unbonded length results in the increase of discontinuity opening. For a linear material behaviour, the amount of such increase is the same for seasonal and extreme temperature changes, and the ratio of the discontinuity opening in a system with an unbonded segment to the corresponding discontinuity opening in a fully bonded system ranges between 1.23 (for $l_u/c=1$) and 1.96 (for $l_u/c=10$). If the nonlinear material behaviour is considered, then the increase of the unbonded length subjected to the seasonal temperature change has greater effect over the system's axial response compared to the extreme temperature variation, where the maximum difference between the discontinuity openings in unbonded and fully bonded systems is 14% and 32% for seasonal and extreme temperature changes, respectively.

![](./images/1000432425769107467_72.jpg)

Figure 28. (a) And (b) effects of material and geometric nonlinearities on the discontinuity opening, (c) and (d) the ratio of discontinuity opening obtained from a nonlinear FE analysis to the corresponding value extracted from a linear FE analysis.

### 3.5.2. Effects of unbonded length on the axial behaviour of the systems with different MoE
Figure 31(a,b) indicate that for IRP materials with lower MoE, the change of the unbonded length has a greater effect on the axial stress. For example, the ratio of the axial stress in a system with a relatively long unbonded segment ($l_u/c=10$) to the corresponding axial stress in a fully bonded system is 0.19, 0.31, and 0.42 for MoE values of 1, 3.77, and 10 GPa, respectively. This means that with the increase of the MoE of IRP from 1 to 10 GPa, the ratio of axial stress in a system with a relatively long unbonded segment to the corresponding axial stress in a fully bonded system increases by a factor of over two. Figure 31(c,d) indicate that with the increase of MoE, the effect of unbonded length on discontinuity opening gets more significant. It can be seen that for $l_u/c=10$, the ratio of discontinuity opening in the unbonded IRP system to the corresponding discontinuity opening in a fully bonded system increases from 1.3 to 2.5, if the MoE changes from 1 to 10 GPa.

### 3.5.3. Effects of the unbonding mode on the axial stresses and displacements
Figures 32 and 33 demonstrate the effects of the two modes of unbonding (one-sided and two-sided as shown in Figure 7) on the IRP's axial behaviour under seasonal temperature changes. As can be seen in Figure 32(a), in terms of the average axial stress along the wall thickness of IRP in the midspan of discontinuity segment, there is no considerable difference between one- and two-sided modes of unbonding. However, it should be noted that this does not necessarily mean that the HSS values for IRP in one- and two-sided modes of unbonding should be the same too. Figure 33

![](./images/1000432425769107467_73.jpg)
![](./images/1000432425769107467_74.jpg)

![](./images/1000432425769107467_75.jpg)
![](./images/1000432425769107467_76.jpg)

Figure 29. Effects of the presence of an unbonded segment on linear and nonlinear axial responses of IRP systems subjected to seasonal and extreme temperature changes: (a) and (c) the effect of unbonded length on the average axial stress along the IRP thickness at the Middle section of the discontinuity segment, (b) and (d) the ratio of the axial stress in an IRP system with an unbonded segment to the corresponding axial stress in a fully bonded system.

clearly shows that the peak stress of IRP in a system with a one-sided unbonded segment can be quite larger than the peak stress in the corresponding system with a two-sided unbonded segment. The reason is that the stress concentra- tions are more significant in the one-sided mode of unbonding compared to the two-sided mode. Figure 32(b) shows that there is no significant difference between the val- ues of discontinuity opening in one- and two-sided modes of unbonding.

## 4. Conclusions

Structural response of an IRP system under the seasonal and extreme levels of temperature variation was studied applying numerical and analytical approaches validated against experimental results and available closed-form expressions. A comprehensive FE analysis comprising 270 linear and nonlinear assessments was conducted to examine the axial behaviour of IRP systems and explore how geomet- rical parameters and material properties influence system stresses and displacements. Analytical expressions were for- mulated to depict the loading and resulting responses of a mechanical model for IRP systems experiencing seasonal temperature variations. Subsequently, leveraging the FE findings, three adjustment factors were formulated to refine the analytical expressions, facilitating the determination of the peak axial stress in IRP and the opening of circumferen- tial discontinuities due to seasonal temperature fluctuations.
The key findings can be outlined as follows:

- The increase of parameter $\tau$ (IRP to host pipe thickness ratio) results in the increase of the stress concentration

![](./images/1000432425769107467_77.jpg)

Figure 30. Effects of the presence of an unbonded segment on linear and nonlinear axial responses of IRP systems subjected to seasonal and extreme temperature changes: (a) and (c) the effect of unbonded length on the discontinuity opening, (b) and (d) the ratio of the discontinuity opening in an IRP system with an unbonded segment to the corresponding discontinuity opening in a fully bonded system.

factor (SCF) at the discontinuity edge in IRP systems. The magnitude of such increase is greatly affected by parameter $\zeta$ (discontinuity width to host pipe thickness ratio). As the value of $\zeta$ increases, the effect of parameter $\tau$ on the SCF becomes less highlighted.

- The increase in discontinuity width makes the stress distribution along the wall thickness of IRP uniform. The increase of $\gamma$ (host pipe radius to thickness ratio) generally increases the stress concentration at the discontinuity edge in an IRP system but can be safely considered to be negligible. The increase of parameter $\alpha$ (host pipe length-to-radius ratio) has no effect on the SCF. The SCFs at the discontinuity edge in an IRP system follow a normal probability distribution and the estimated maximum expected value for the SCF in IRP systems is 2.53.
- The increase of the pipeline's internal pressure results in the increase of the IRP's axial stress as well as the discontinuity opening. As the IRP thickness increases, pipeline's internal pressure gets less effective on the magnitude of IRP's axial stress and discontinuity opening. As the initial width of discontinuity increases, the effect of pipeline's internal pressure on IRP's axial stress and discontinuity opening becomes more significant.
- Material nonlinearities affect IRP's axial stress and discontinuity opening more significantly as the level of temperature fluctuation increases. Hence, nonlinear material

![](./images/1000432425769107467_78.jpg)

![](./images/1000432425769107467_79.jpg)

![](./images/1000432425769107467_80.jpg)

![](./images/1000432425769107467_81.jpg)

Figure 31. Effects of the presence of an unbonded segment on axial responses of IRP systems with different young's moduli subjected to seasonal temperature changes: (a) and (c) the effect of unbonded length on the axial stress of IRP and discontinuity opening, (b) and (d) the ratio of the axial response in an IRP system with an unbonded segment to the corresponding response in a fully bonded system.

behaviour of host pipe and IRP should be included in analysing the pipeline repair systems under the extreme temperature variations. An IRP system with a steel host pipe is more affected by the nonlinear material behaviour compared to the corresponding system with a cast-iron host pipe.

- The increase of the unbonded length can result in significant decrease of the axial stress of IRP in the discontinuity segment. This suggests that a degree of debonding could be advantageous for repair systems, as it assists the IRP system to more effectively accommodate thermal strains and the resulting stresses.

- For both linear and nonlinear IRP materials, the increase of unbonded length results in the decrease of stress and increase of discontinuity opening. Nonlinear behaviour of IRP material is affected more by the extreme than seasonal temperature change.
- The change of the unbonded length has a greater effect on the axial stress of IRP with low modulus of elasticity while the effect of the unbonded length on the discontinuity opening becomes more significant for stiff IRP.
- IRP's hot-spot stress in the one-sided mode of unbonding can be quite larger than the two-sided mode. However, there is no significant difference between

![](./images/1000432425769107467_82.jpg)

![](./images/1000432425769107467_83.jpg)

Figure 32. Effects of the two modes of unbonding on the: (a) average axial stress along the IRP thickness at the Middle section of the discontinuity segment, (b) discontinuity opening.

![](./images/1000432425769107467_84.jpg)

(a) IRP repair system with a one-sided unbonded segment

![](./images/1000432425769107467_85.jpg)

(b) IRP repair system with a two-sided unbonded segment

Figure 33. Deformed shapes of the system with different unbonding modes (contours: axial stress [MPa]).

discontinuity openings in one- and two-sided modes of unbonding.

The analytical and numerical models developed in this paper offer a dependable framework for describing the linear and nonlinear axial behaviour of internal replacement pipe (IRP) systems within host pipes afflicted by circumferential cracks. Depending on factors such as pipe material, soil conditions, and applied stresses, both circumferential and longitudinal cracks may occur. Future research endeavours could explore the behaviour of IRP systems retrofitted for longitudinal cracks under temperature variations. Additionally, investigating radial stresses and deformations resulting from temperature changes is suggested as another avenue for future research. When temperatures drop below freezing, moisture-laden soil can freeze and expand, exerting frost loads that impose significant bending forces on the pipe. Although not addressed in this study, examining the response of IRP systems to frost loads presents another promising avenue for future research endeavours.

### Acknowledgements
The opinions and viewpoints expressed by the authors in this paper do not necessarily represent those of the United States Government or any of its agencies. The authors would like to extend their gratitude to the anonymous reviewers for their invaluable feedback on earlier drafts of this paper.

### Disclosure statement
No potential conflict of interest was reported by the author(s).

### Funding
This research received partial funding from the Advanced Research Projects Agency-Energy (ARPA-E), US Department of Energy, under Award Number DE-AR0001327.

### References
Adebola, T., Moore, I., & Hoult, N. (2021). Use of optical fibers to investigate strength limit states for pressure pipe liners spanning across circular perforations. *Journal of Pipeline Systems Engineering and Practice, 12*(2), 04021006. doi:10.1061/(ASCE)PS.1949-1204.0000523

Ahmadi, H., Chamani, S., & Kouhi, A. (2020). Effects of geometrical parameters on the degree of bending (DoB) in multi-planar tubular XT-joints of offshore structures subjected to axial loading. *Applied Ocean Research, 104*, 102381. doi:10.1016/j.apor.2020.102381

Ahmadi, H., Lotfollahi-Yaghin, M. A., & Aminfar, M. H. (2012a). Stress concentration factors at saddle and crown positions on the central brace of two-planar welded CHS DKT-connections. *Journal of Marine Science and Application, 11*(1), 83-97. doi:10.1007/s11804-012-1109-2

Ahmadi, H., Lotfollahi-Yaghin, M. A., Shao, Y. B., & Aminfar, M. H. (2012b). Parametric study and formulation of outer-brace geometric stress concentration factors in internally ring-stiffened tubular KT-joints of offshore structures. *Applied Ocean Research, 38*, 74-91. doi:10.1016/j.apor.2012.07.004

Ahmadi, H., Manalo, A., Dixon, P. G., Salah, A., Karunasena, W., Tien, C. M. T., … Wham, B. P. (2024). Temperature change-induced linear and nonlinear axial responses of internal replacement pipe (IRP) systems for pipeline rehabilitation incorporating the effects of soil friction. *Structures, 62*, 106247. doi:10.1016/j.istruc.2024.106247

Ahmadi, H., Mayeli, V., & Zavvar, E, University of Tabriz. (2019). A probability distribution model for the degree of bending in tubular KT-joints of offshore structures subjected to IPB moment loadings. *International Journal of Coastal and Offshore Engineering, 3*(2), 11-29. doi:10.29252/ijcoe.3.2.11

Ahmadi, H., & Ziaei Nejad, A. (2017). Geometrical effects on the local joint flexibility of two-planar tubular DK-joints in jacket substructure of offshore wind turbines under OPB loading. *Thin-Walled Structures, 114*, 122-133. doi:10.1016/j.tws.2017.02.001

American Petroleum Institute (API). (2007). *Recommended practice for planning, designing and constructing fixed offshore platforms-Working stress design: RP 2A-WSD* (21st ed.). American Petroleum Institute, USA.

ANSYS. (2016). *ANSYS mechanical APDL theory reference* Release 17.1, Canonsburg, US.

Argyrou, C., Bouziou, D., O'Rourke, T. D., & Stewart, H. E. (2018). Retrofitting pipelines with cured-in-place linings for earthquake-induced ground deformations. *Soil Dynamics and Earthquake Engineering, 115*, 156-168. doi:10.1016/j.soildyn.2018.07.015

Bing, C., & Kelly, S. (2021). *Cyber attack shuts down top U.S. fuel pipeline network* Reuters. Archived from the original on May 8, 2021.

Bokaian, A. (2004). Thermal expansion of pipe-in-pipe systems. *Marine Structures, 17*(6), 475-500. doi:10.1016/j.marstruc.2004.12.002

Bureau, M., Davison, M., & O'Rourke, T. D. (2021). How bonded a bonded CIPP liner needs to be? A review of 3rd-party studies on CIPP KPI's. In *North American Society for Trenchless Technology (NASTT) 2021 No-Dig Show*. NASTT, Orlando, FL, US.

Cast Iron Pipe Research Association. (1952). *Handbook of cast iron pipe for water, gas, sewerage and industrial service* (2nd ed.). Cast Iron Pipe Research Association, Chicago, US.

CDCQ. (2021). *Characterization of 4 water main CIPP liner*. Centre de développement des composites du Québec: Canada.

CDCQ. (2022). *Characterization of coefficient of thermal expansion of water main CIPP material*. Centre de développement des composites du Québec: Canada.

Chin, W. S., & Lee, D. G. (2005). Development of the trenchless rehabilitation process for underground pipes based on RTM. *Composite Structures, 68*(3), 267-283. doi:10.1016/j.compstruct.2004.03.019

Det Norske Veritas. (2005). *Fatigue design of offshore steel structures, Recommended Practice: DNV-RP-C203*. Greater Oslo, Norway.

Dixon, P. G., Tafsirojaman, T., Klingaman, J., Hubler, M. H., Dashti, S., O'Rourke, T. D., … Wham, B. P. (2023b). State-of-the-art review of performance objectives for legacy gas pipelines with pipe-in-pipe rehabilitation technologies. *Journal of Pipeline Systems Engineering and Practice, 14*(2), 03122003. doi:10.1061/JPSEA2.PSENG-1371

Dixon, P. G., Salah, A., Ahmadi, H., Ulrich, M. E., Hubler, M. H., Dashti, S., … Wham, B. P. (2023a). *An analytical approach for thermally induced axial deformation in rehabilitated pipelines*. ASCE UESI Pipelines 2023 Conference, August 12-16, San Antonio, Texas, US. doi:10.1061/9780784485026.028

Francom, T., El Asmar, M., & Ariaratnam, S. T. (2014). *Using alternative project delivery methods to enhance the cost performance of trenchless construction projects*. Construction Research Congress, May 19-21, Atlanta, Georgia, US. doi:10.1061/9780784413517.125

Fu, G., Shannon, B., Azoor, R., Ji, J., Deo, R., & Kodikara, J. (2022). Reliability based failure assessment of deteriorated cast iron pipes lined with polymeric liners. *Structure and Infrastructure Engineering, 19*(11), 1516-1529. doi:10.1080/15732479.2022.2035404

Fuselli, F., Huber, S., & Mambretti, S. (2022). Environmental aspects of trenchless pipe rehabilitation methods. *Urban Water Journal, 19*(8), 879-887. doi:10.1080/1573062X.2022.2087531

Garmabaki, A. H. S., Marklund, S., Thaduri, A., Hedström, A., & Kumar, U. (2020). Underground pipelines and railway infrastructure-failure consequences and restrictions. *Structure and*

Infrastructure Engineering, 16(3), 412-430. doi:10.1080/15732479.2019.1666885

Gas Industry Standard GIS/L2. (2018). Specification for steel pipe 21.3mm to 1219mm outside diameter for operating pressures up to 7bar. Supplementary to BS EN ISO 3183 PSL 2, UK.

Ha, S. K., Lee, H. K., & Kang, I. S. (2016). Structural behavior and performance of water pipes rehabilitated with a fast-setting polyureaur- ethane lining. Tunnelling and Underground Space Technology, 52, 192-201. doi:10.1016/j.tust.2015.12.003

Hobbacher, A. F. (2016). Recommendations for fatigue design of welded joints and components. IIW Document IIW-2259-15 ex XIII-2460-13/XV-1440-13, International Institute of Welding.

Iqbal, H., Tesfamariam, S., Haider, H., & Sadiq, R. (2017). Inspection and maintenance of oil & gas pipelines: A review of policies. Structure and Infrastructure Engineering, 13(6), 794-815. doi:10.1080/15732479.2016.1187632

Jeon, S., O'Rourke, T. D., & Neravali, A. N. (2004). Repetitive loading effects on cast iron pipelines with cast-in-place pipe lining systems. Journal of Transportation Engineering, 130(6), 692-705. doi:10.1061/(ASCE)0733-947X(2004)130:6(692)

Jeyapalan, J. K. (2000). Future outlook for trenchless pipeline rehabilitation technologies. National Conference on Environmental and Pipeline Engineering, July 23-26, Kansas City, Missouri, US. doi:10.1061/40507(282)25

Jung, Y. J., & Sinha, S. K. (2007). Evaluation of trenchless technology methods for municipal infrastructure system. Journal of Infrastructure Systems, 13(2), 144-156. doi:10.1061/(ASCE)1076-0342(2007)13:2(144)

Kiriella, S., Manalo, A., Tien, C. M. T., Ahmadi, H., Wham, B. P., Salah, A., ... O'Rourke, T. D. (2023). Lateral deformation behaviour of structural internal replacement pipe repair systems. Composite Structures, 319, 117144. doi:10.1016/j.compstruct.2023.117144

Kottegoda, N. T., & Rosso, R. (2008). Applied statistics for civil and environmental engineers (2nd ed.). UK: Blackwell Publishing.

Lee, G. H., Pouraria, H., Seo, J. K., & Paik, J. K. (2015). Burst strength behaviour of an aging subsea gas pipeline elbow in different external and internal corrosion-damaged positions. International Journal of Naval Architecture and Ocean Engineering, 7(3), 435-451. doi:10.1515/ijnaoe-2015-0031

Li, B., Yu, W., Xie, Y., Fang, H., Du, X., Wang, N., ... Zhao, X. (2023). Trenchless rehabilitation of sewage pipelines from the perspective of the whole technology chain: A state-of-the-art review. Tunnelling and Underground Space Technology, 134, 105022. doi:10.1016/j.tust.2023.105022

Lu, H., Behbahani, S., Azimi, M., Matthews, J. C., Han, S., & Iseley, T. (2020a). Trenchless construction technologies for oil and gas pipelines: State-of-the-art review. Journal of Construction Engineering and Management, 146(6), 1-21. doi:10.1061/(ASCE)CO.1943-7862.0001819

Lueke, J. S., & Ariaratnam, S. T. (2001). Rehabilitation of underground infrastructure utilizing trenchless pipe replacement. Practice Periodical on Structural Design and Construction, 6(1), 25-34. doi:10.1061/(ASCE)1084-0680(2001)6:1(25)

Lu, H., Wu, X., Ni, H., Azimi, M., Yan, X., & Niu, Y. (2020b). Stress analysis of urban gas pipeline repaired by inserted hose lining method. Composites Part B: Engineering, 183, 107657. doi:10.1016/j.compositesb.2019.107657

MathWorks. (2007). MATLAB programming language. Version 7.5. MathWorks, Massachusetts, US.

Mustafa, S. A. A., & Moy, S. S. J. (2011). Strengthening cast iron struts using carbon fibre reinforced polymers - Finite element modelling. Composites Part B: Engineering, 42(5), 1048-1056. doi:10.1016/j.compositesb.2011.03.026

N'Diaye, A., Hariri, S., Pluvinage, G., & Azari, Z. (2007). Stress concentration factor analysis for notched welded tubular T-joints. International Journal of Fatigue, 29(8), 1554-1570. doi:10.1016/j.ijfatigue.2008.07.014

Nuruddin, M., DeCocker, K., Sendesi, S. M. T., Whelton, A. J., Youngblood, J. P., & Howarter, J. A. (2020). Influence of aggressive environmental aging on mechanical and thermo-mechanical properties of ultra violet (UV) cured in place pipe liners. Journal of Composite Materials, 54(23), 3365-3379. doi:10.1177/0021998320913988

O'Rourke, T. D., Strait, J. E., Mottl, N., Berger, B. A., Wham, B. P., Stewart, H. E., & Price, D. (2021). Performance evaluation of aqua-pipe under earthquake-induced ground deformation. Final Report, School of Civil and Environmental Engineering, Cornell University, Ithaca, NY, US.

PHMSA. (2019). CPF No. 5-2008-5016H: Notice of proposed corrective action order. Lakewood, CO, US: Pipeline and Hazardous Materials Safety Administration.

Shou, K. J., & Chen, B. C. (2018). Numerical analysis of the mechanical behaviors of pressurized underground pipelines rehabilitated by cured-in-place-pipe method. Tunnelling and Underground Space Technology, 71, 544-554. doi:10.1016/j.tust.2017.11.005

Stewart, H. E., O'Rourke, T. D., Wham, B. P., Netravali, A. N., Argyrou, C., Zeng, X., & Bond, T. K. (2015). Performance testing of field-aged cured-in-place liners (CIPL) for cast iron piping. Final Report (Submitted to: NYSEARCH/Northeast Gas Association), School of Civil and Environmental Engineering. Ithaca, NY, US: Cornell University.

Stewart, H. E., Weinberg, S. R., Berger, B. A., & Strait, J. E. (2019). Slow cooling of cured-in-place liners for cast iron and steel gas pipelines. Final Report (Submitted to: NYSEARCH/Northeast Gas Association), School of Civil and Environmental Engineering. Ithaca, NY, US: Cornell University.

Tafsirojjaman, T., Manalo, A., Tien, C. M. T., Wham, B. P., Salah, A., Kiriella, S., ... Dixon, P. (2022). Analysis of failure modes in pipe-in-pipe repair systems for water and gas pipelines. Engineering Failure Analysis, 140, 106510. doi:10.1016/j.engfailanal.2022.106510

TET. (2003). Thermal expansion - Linear expansion coefficients. The Engineering Toolbox, USA.

Tien, C. M. T., Manalo, A., Dixon, P., Tafsirojjaman, T., Karunasena, W., Flood, W. W., ... Wham, B. P. (2023). Effects of the legacy pipe ends on the behaviour of pipe-in-pipe repair systems under internal pressure. Engineering Failure Analysis, 144, 106957. doi:10.1016/j.engfailanal.2022.106957

UK Health and Safety Executive. (1997). OTH 354: Stress concentration factors for simple tubular joints-assessment of existing and development of new parametric formulae. Prepared by Lloyd's Register of Shipping, UK.

Valves Instruments Plus (VIP) Ltd. (2002). Thermal expansion. UK: Valves Instruments Plus.

Vasilikis, D., & Karamanos, S. A. (2012). Mechanical behavior and wrinkling of lined pipes. International Journal of Solids and Structures, 49(23-24), 3432-3446. doi:10.1016/j.ijsolstr.2012.07.023

Wang, C., Teh, L. H., & Li, Y. (2022). Time-dependent reliability assessment of steel pipelines subjected to localized corrosion. Structure and Infrastructure Engineering, 19(11), 1505-1515. In Press. doi:10.1080/15732479.2022.2033799

Wang, R., Wang, F., Xu, J., Zhong, Y., & Li, S. (2019). Full-scale experimental study of the dynamic performance of buried drainage pipes under polymer grouting trenchless rehabilitation. Ocean Engineering, 181, 121-133. doi:10.1016/j.oceaneng.2019.04.009

Xiang, W., & Zhou, W. (2020). Integrated pipeline corrosion growth modeling and reliability analysis using dynamic Bayesian network and parameter learning technique. Structure and Infrastructure Engineering, 16(8), 1161-1176. doi:10.1080/15732479.2019.1692363

Xin, J. (2014). Application of trenchless pipeline rehabilitation technology. International Conference on Pipelines and Trenchless Technology, Xiamen, China. doi:10.1061/9780784413821.051

Yu, H. N., Kim, S. S., Hwang, I. U., & Lee, D. G. (2008). Application of natural fiber reinforced composites to trenchless rehabilitation of underground pipes. Composite Structures, 86(1-3), 285-290. doi:10.1016/j.compstruct.2008.03.015

### Appendix. Deriving the analytical expression of the transfer function $\lambda$

Parameter $\lambda$ is defined as (Equation (8)):

$$
\lambda=\frac{\left(\sigma_{n}\right)_{I}}{f_{T}}=\frac{F_{T} / A_{I}}{F_{T} / A_{C}}=\frac{A_{C}}{A_{I}}=\frac{A_{I}+A_{H}}{A_{I}} \tag{A1}
$$

Cross-sectional areas for IRP and host pipe are calculated as follows:

$$
A_{H}=\frac{\pi}{4}\left[D_{o H}^{2}-\left(D_{o H}-2 t_{H}\right)^{2}\right] \tag{A2}
$$

$$
A_{I}=\frac{\pi}{4}\left[D_{o I}^{2}-\left(D_{o I}-2 t_{I}\right)^{2}\right] \tag{A3}
$$

Outer diameter of IRP $(D_{oI})$ can be rewritten in terms of the wall thickness and outer diameter of host pipe as follows:

$$
D_{o I}=D_{o H}-2 t_{H} \tag{A4}
$$

Substitution of Equation (A4) in Equation (A3) leads to the below expression for the IRP's cross-sectional area:

$$
A_{I}=\frac{\pi}{4}\left[\left(D_{o H}-2 t_{H}\right)^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}\right] \tag{A5}
$$

Substitution of Equations (A2) and (A5) in Equation (A1) results in the below analytical expression of the transfer function $\lambda$ as follows:

$$
\lambda=\frac{D_{o H}^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}}{\left(D_{o H}-2 t_{H}\right)^{2}-\left(D_{o H}-2 t_{H}-2 t_{I}\right)^{2}} \tag{A6}
$$