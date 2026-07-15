Mater. Res. Soc. Symp. Proc. Vol. 1541 © 2013 Materials Research Society
DOI: 10.1557/opl.2013.731

# Mechanics of Diffusion-Induced Fractures in Lithium-ion Battery Materials

Cheng-Kai ChiuHuang, Michael A. Stamps, and Hsiao-Ying Shadow Huang*

Department of Mechanical and Aerospace Engineering
North Carolina State University
R3002, EB3, 911 Oval Drive, Raleigh, NC 27695

## ABSTRACT

Our study is motivated by the need for development and deployment of reliable and efficient energy storage devices, such as lithium-ion batteries. However, the rate-capacity loss is the key obstacle faced by current lithium-ion battery technology, hindering many potential large-scale engineering applications, such as future transportation modalities, grid stabilization and storage systems for renewable energy. During electrochemical processes, diffusion-induced stress is an important factor causing electrode material capacity loss and failure. In this study, we present models that are capable for describing diffusion mechanisms and stress formation in $\mathrm{LiFePO}_{4}$ nanoparticles, a lithium-ion battery cathode material which promises an alternative, with the potential for reduced cost and improved safety. To evaluate mechanics of diffusion-induced fractures, a plate-like model is adopted with anisotropic materials properties and volume misfits during the phase transformation are considered. Stress distribution at phase boundaries and fracture mechanics information (energy release rates and stress intensity factors) are provided to further understand the stress development due to lithium-ion diffusion during discharging. This study contributes to the fundamental understanding of kinetics of materials in lithium-ion batteries, and results from our stress analysis provides better electrode materials design rules for future lithium-ion batteries.

## INTRODUCTION

Lithium ion batteries have become a widely known commodity for satisfying the world's mobile energy storage needs. Applications for these high power batteries include anything from laptop computers and mp3 players to orbiting satellites and electric tools. The advantages of Li-ion over other types or rechargeable batteries such as Nickel-Cadmium and Metal Hydride types lie in their superior energy-to-weight ratio, quicker recharge times, and increased cycle life. In addition, as the world becomes more concerned about rising oil prices and $\mathrm{CO}_{2}$ emissions, the need to increase hybrid or electric vehicle production and performance (along with other high power applications) has fueled research to improve Li-ion battery performance and even discover new battery materials.

Since the conception of Lithium-Iron-Phosphate $(\mathrm{LiFePO}_{4})$ as a possible cathode for today's Li-ion batteries [1], this material with olivine structure has been a focal point for such experimentation and discussion in the Li-ion battery realm. $\mathrm{LiFePO}_{4}$ boast several attractive qualities including a relatively high theoretical capacity of 170 mAh/g, great structure stability, long cycle life, impressive safety attributes and environmentally benign qualities. It's also widely available across the world at a relatively inexpensive price. But with the pros, cons also exist such as extremely low electrochemical conductivity for raw $\mathrm{LiFePO}_{4}$ and a tendency for

*Corresponding author, email: hshuang@ncsu.edu

capacitance loss over its cycle life. Nevertheless, the favorable characteristics of $LiFePO_4$ [2-4], especially in safety, provide a strong base that research advancements can build on to make $LiFePO_4$ one of the most competitive cathode material's in today's growing markets for battery powered electronics, power tools and hybrid electric vehicles to name a few.

![](./images/812765721514737665_1.jpg)
Figure 1. A two-phase $LiFePO_4$ model, in which lithium-ion diffuse along the b-axis and the phase boundary moves along the a-axis [5].

![](./images/812765721514737665_2.jpg)
Figure 2. Normalized $\sigma_{xx}$ evolution of a single $LiFePO_4$ (LFP) particle. Compression exists between phases due to different molar volumes of $LiFePO_4$ and $FePO_4$ phases.

Computational and experimental observations have found that lithium-ion diffusion in $LiFePO_4$ is one-dimensional confined along the b-axis [6-10]. Delmas et al. [11] have proposed a "domino-cascade" model to describe the phase boundary movement along the $a$-axis for $LiFePO_4$, when lithium-ion diffuse along the $b$-axis during charging/discharging. In the "domino-cascade" model, the interface is limited to one block, therefore, either a fully lithiated or an unlithiated phase exists in a partially discharged $LiFePO_4$ particle. That is, a diffused and transit interfacial zone was not considered in the domino-cascade model. Moreover, other experiment results reveal the coexistence of $FePO_4$ and $LiFePO_4$ phases in a single particle, where stripe-like juxtaposed phase boundaries are observed [12-15]. A co-existing two-phase system under fast discharging was also computationally predicted by Cogswell and Bazant, Bai et al. [16], and Van der Ven et al. [17].

To better understand the stress evolution with the phase boundary propagating along the a-axis [12-15], we have previously focused on studying the stress distribution on the phase boundary between $LiFePO_4$ and $FePO_4$ phases (Figure 1) [5]. We used a thermal stress analysis approach via a finite element method to obtain diffusion-induced stresses in a plate-like $LiFePO_4$ particle. The particle is divided into 10 layers along the $a$-axis and each layer contains one Li-ion diffusion channel. That is, each layer is corresponding with 10% nonstoichiometric lithium-ion composition (Figure 1b).

![](./images/812765721514737665_3.jpg)
Figure 3. Normalized $\sigma_{xz}$ evolution of a single $LiFePO_4$ (LFP) particle. Normalized $\sigma_{xz}$ exhibits a non-negligible value during the phase transformation and it might play an important role on fracture mechanics and crack propagation.

![](./images/812765721514737665_4.jpg)
Figure 4. A representative bi-materials $LiFePO_4$ particle. An initial flaw exists between two phases.

$LiFePO_4$ phase has a larger molar volume and $FePO_4$ phase has a smaller molar volume, where a coherent interface exists between these two phases during the phase transformation [18].

As a result, the $LiFePO_4$ phase would be under compression and the $FePO_4$ phase would be under tension due constrains of the coherent interface. The results from our finite element analysis indicate that the particle is under compression before 70% lithiation for normalized $\sigma_{xx}$ (Figure 2). Our finite element simulation also revealed that $\sigma_{xz}$ exhibits a non-negligible value during the phase transformation (Figure 3), and it is suggested that $\sigma_{xz}$ might play an important roles on fracture mechanics and crack propagation in electrode particles [19]. In the current study, we plan to unravel effects of diffusion-induced stresses on lithium-ion battery materials. In particular, to study fracture mechanics of nano-particles with pre-existing flaws.

## MATERIALS AND METHOD

To further study fracture mechanics and crack propagation in $LiFePO_4$ particles, virtual crack closure technique (VCCT) with the ANSYS finite element software (ANSYS, Inc. Canonsburg, Pennsylvania) is utilized to obtain energy release rates and the stress intensity factors [20]. Energy release rates are used to predict the fracture tendency and the stress intensity factors are used to relate stress fields around crack tips. The fracture mechanics information (energy release rates and stress intensity factors) are calculated from the command-coding interface of ANSYS [21], and they are currently not available on the graphical user interface of ANSYS.

Two-phase plate-like $LiFePO_4$ finite element models are generated and orthotropic material properties are adopted for both phases [22]. An interfacial crack is considered to run parallel to the $bc$-plane (along the $c$-axis) where phase boundaries are present (Figure 4) [23]. Three different sizes of finite element model are generated and the corresponding numbers of unit cells are as follows: (a) 500-nm × 300 nm × 225-nm with 125,000 unit cells, (b) 200-nm × 120 nm × 90-nm with 8,000 unit cells, and (c) 100-nm × 60 nm × 45-nm with 1,000 unit cells, respectively. The numbers of the unit cell are approximated based on the $LiFePO_4$ lattice constants: a = 10.3 Å, b = 6.0 Å, and c = 4.7 Å [24]. Assuming displacements along the $a$- and $c$-axes are independent of $b$-axis and there are no normal tractions on the $ac$-plane, the plane stress assumption is applied. A total of 21 finite element simulations are conducted, whereas the initial crack is considered from the top face with variable lengths of cracks sizes 0.05 – 0.8 L/d, in which L represents the crack length and d represents the particle size along the $c$-axis (Figure 4). The crack opening is set as 0.5 nm in the $a$-direction to stay proportional to experimentally observed cracks [23]. Displacements were applied to the $LiFePO_4$ phase according to the misfit strains previously measured and reported in the literature: expansion occurs along the a-direction ($\varepsilon_{a}=5.03\%$) and extraction occurs along the c-direction ($\varepsilon_{c}=-1.9\%$) [25] (Figure 4). Two-dimensional quadrilateral elements are used in the finite element analysis, and such eight-node parabolic elements allow for more flexibility and improved accuracy in contrast to four-node elements [26, 27].

A crack will propagate if the total energy release rate of Modes 1 and Mode 2, $G_T$, is larger than approximately twice the surface energy of the particle ($G_T$>2$\gamma$) [28]. A first-principle analysis by Wang et al. has reported a $\gamma$ value of 0.66 N/m for $LiFePO_4$ in the (100) crack face orientation [29]. In the current study, we collect finite element results satisfying $G_T$>2$\gamma$, and the difference between these two energies is used to predict crack growth patterns. That is, crack propagation is eminent and a crack will grow until the surface energy from the newly formed crack faces brings the particle back to equilibrium with the strain energy release rate. First, we calculate the additional energy release rate for a 0.01-nm crack extension for all models, $E_R$.

Second, we calculate the additional surface energy for a 0.01-nm crack extension for all models, $E_S$=0.01×b×γ, where b is the particle size in the $b$-axis. Last, we calculate the required crack extension da via the ratio of $E_R$ and $E_S$.

## RESULTS AND DISCUSSION

The results of the finite element method based-VCCT indicate that Mode I fracture is dominant for all models. **Figure 5** reveals that $G_I$ is highly dependent on the crack size for all three different particle sizes. Critical points occur at around L/d=0.5 and 0.6, where energy release rates increase with the increased crack lengths, and then energy release rates begin to level off. In particular, smaller particles (100 nm × 60 nm × 45 nm) are able to better accommodate initial flaws with the crack propagation when L/d ≤0.2. Although the crack propagation is possible in other planes, literature and experimentations have reported cracks are observed in the $bc$-plane between phases while propagating in the $c$-axis [13]. Less energy release rates are observed in the Mode II fracture, however, these values are considered to contribute to the total energy release rate $G_T$ for the crack propagation, and it is discussed in the following section.

![](./images/812765721514737665_5.jpg)
Figure 5. Energy release rates for two modes for three different particle sizes.

**Table 1** shows the fracture mechanics and crack propagation results from the finite element method-based VCCT simulation. It is observed that Mode I stress intensity factor increases with larger crack to particle size (L/d). Moreover, when $G_T$ is compared with $2\gamma$, the energy difference $\Delta E$=$G_T$-$2\gamma$ is shown in **Table 1**, and it is used to calculate the required additional strain energy release rate for a crack extension. It is observed that crack propagation is highly dependent on the initial crack size and particle sizes.

Table 1: Fracture mechanics and crack propagation results from the finite element method-based VCCT simulation.

<table>
<thead>
  <tr>
    <th colspan="5">a x b x c = 500 nm x 300 nm x 225 nm</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>L/d</td>
    <td>K₁ (MPa-m¹ᐟ²)</td>
    <td>G_T (N/m)</td>
    <td>2γ (N/m)</td>
    <td>ΔE (N/m)</td>
  </tr>
  <tr>
    <td>0.05</td>
    <td>0.659</td>
    <td>5.462</td>
    <td>1.32</td>
    <td>4.142</td>
  </tr>
  <tr>
    <td>0.1</td>
    <td>0.833</td>
    <td>5.922</td>
    <td>1.32</td>
    <td>4.602</td>
  </tr>
  <tr>
    <td>0.2</td>
    <td>1.136</td>
    <td>8.744</td>
    <td>1.32</td>
    <td>7.424</td>
  </tr>
  <tr>
    <td>0.3</td>
    <td>1.310</td>
    <td>11.027</td>
    <td>1.32</td>
    <td>9.707</td>
  </tr>
  <tr>
    <td>0.4</td>
    <td>1.403</td>
    <td>12.373</td>
    <td>1.32</td>
    <td>11.053</td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>1.456</td>
    <td>13.053</td>
    <td>1.32</td>
    <td>11.733</td>
  </tr>
  <tr>
    <th colspan="5">a x b x c = 200 nm x 120 nm x 90 nm</th>
  </tr>
  <tr>
    <td>L/d</td>
    <td>K₁ (MPa-m¹ᐟ²)</td>
    <td>G_T (N/m)</td>
    <td>2γ (N/m)</td>
    <td>ΔE (N/m)</td>
  </tr>
  <tr>
    <td>0.05</td>
    <td>0.354</td>
    <td>0.068</td>
    <td>1.32</td>
    <td>-1.252</td>
  </tr>
  <tr>
    <td>0.1</td>
    <td>0.531</td>
    <td>0.079</td>
    <td>1.32</td>
    <td>-1.241</td>
  </tr>
  <tr>
    <td>0.2</td>
    <td>0.674</td>
    <td>3.481</td>
    <td>1.32</td>
    <td>2.161</td>
  </tr>
  <tr>
    <td>0.3</td>
    <td>0.779</td>
    <td>4.400</td>
    <td>1.32</td>
    <td>3.080</td>
  </tr>
  <tr>
    <td>0.4</td>
    <td>0.836</td>
    <td>4.850</td>
    <td>1.32</td>
    <td>3.530</td>
  </tr>
  <tr>
    <td>0.5</td>
    <td>0.861</td>
    <td>5.176</td>
    <td>1.32</td>
    <td>3.856</td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>0.902</td>
    <td>5.220</td>
    <td>1.32</td>
    <td>3.900</td>
  </tr>
  <tr>
    <td>0.7</td>
    <td>0.903</td>
    <td>5.211</td>
    <td>1.32</td>
    <td>3.891</td>
  </tr>
  <tr>
    <td>0.8</td>
    <td>0.926</td>
    <td>5.305</td>
    <td>1.32</td>
    <td>3.985</td>
  </tr>
  <tr>
    <th colspan="5">a x b x c = 100 nm x 60 nm x 45 nm</th>
  </tr>
  <tr>
    <td>L/d</td>
    <td>K₁ (MPa-m¹ᐟ²)</td>
    <td>G_T (N/m)</td>
    <td>2γ (N/m)</td>
    <td>ΔE (N/m)</td>
  </tr>
  <tr>
    <td>0.05</td>
    <td>0.297</td>
    <td>0.029</td>
    <td>1.32</td>
    <td>-1.291</td>
  </tr>
  <tr>
    <td>0.1</td>
    <td>0.375</td>
    <td>0.042</td>
    <td>1.32</td>
    <td>-1.278</td>
  </tr>
  <tr>
    <td>0.2</td>
    <td>0.510</td>
    <td>1.740</td>
    <td>1.32</td>
    <td>0.420</td>
  </tr>
  <tr>
    <td>0.3</td>
    <td>0.589</td>
    <td>2.200</td>
    <td>1.32</td>
    <td>0.880</td>
  </tr>
  <tr>
    <td>0.4</td>
    <td>0.629</td>
    <td>2.470</td>
    <td>1.32</td>
    <td>1.150</td>
  </tr>
  <tr>
    <td>0.6</td>
    <td>0.652</td>
    <td>2.607</td>
    <td>1.32</td>
    <td>1.287</td>
  </tr>
</tbody>
</table>

CONCLUSIONS

In summary, mechanics of diffusion-induced fractures of lithium-ion battery materials is presented. Our preliminary results showed that mechanical stresses on the phase boundary would likely promote crack propagation (Figure 3), if initial flaws exist inside electrode nano-particles. Finite element method based-VCCT is adopted in the current study to obtain strain energy release rates and stress intensity factors. Results show that energy release rates (Figure 5) and stress intensity factors are highly related to the initial flaw sizes and particle sizes (Table 1). In particular, smaller particles (100 nm × 60 nm × 45 nm) are better to accommodate initial cracks. This is a first approach towards utilizing stress fields on the phase boundary to better understand fracture mechanics of lithium-ion battery electrode materials. The results of the current study helps improve battery structural design by providing a better understanding of micromechanics and a base for future fatigue analyses, which may incorporate a variety of electrode materials and additional fatigue life parameters. Studies have shown that the application of nano-layer coatings to increase electronic conductivity along with reducing particle size to effectively reduce the diffusion path and decrease internal stress within the particle [30, 31]. This research will hopefully elucidate a relationship between micromechanics and battery usage to help in the design of a higher performance, longer lasting battery for the future.

## REFERENCES

[1] A.K. Padhi, K.S. Nanjundaswamy, J.B. Goodenough, Journal of the Electrochemical Society, 144 (1997) 1188-1194.

[2] Y. Wang, H.-Y.S. Huang, Materials Research Society Proceedings, 1363-RR05-30 (2011).

[3] Y. Wang, H.-Y.S. Huang, ASME International Mechanical Engineering Congress and Exposition Proceedings, IMECE2011-65663 (2011).

[4] Y. Wang, H.-Y.S. Huang, TSEST Transaction on Control and Mechanical Systems, 1 (2012) 192-200.

[5] C.-K. ChiuHuang, H.-Y.S. Huang, ASME International Mechanical Engineering Congress and Exposition Proceeding, IMECE2012-89235 (2012).

[6] S.E. Boulfelfel, G. Seifert, S. Leoni, Journal of Materials Chemistry, 21 (2011) 16365-16372.

[7] S.-i. Nishimura, G. Kobayashi, K. Ohoyama, R. Kanno, M. Yashima, A. Yamada, Nature Materials, 7 (2008) 707-711.

[8] R. Malik, D. Burch, M. Bazant, G. Ceder, Nano Letters, 10 (2010) 4123-4127.

[9] G.K.P. Dathar, D. Sheppard, K.J. Stevenson, G. Henkelman, Chemistry of Materials, 23 (2011) 4032-4037.

[10] J.J. Yang, J.S. Tse, Journal of Physical Chemistry A, 115 (2011) 13045-13049.

[11] C. Delmas, M. Maccario, L. Croguennec, F. Le Cras, F. Weill, Nat Mater, 7 (2008) 665-671.

[12] L. Laffont, C. Delacourt, P. Gibot, M.Y. Wu, P. Kooyman, C. Masquelier, J.M. Tarascon, Chemistry of Materials, 18 (2006) 5520-5529.

[13] G. Chen, X. Song, T.J. Richardson, Electrochemical and Solid-State Letters, 9 (2006) A295-A298.

[14] C.V. Ramana, A. Mauger, F. Gendron, C.M. Julien, K. Zaghib, Journal of Power Sources, 187 (2009) 555-564.

[15] G. Brunetti, D. Robert, P. Bayle-Guillemaud, J.L. Rouviere, E.F. Rauch, J.F. Martin, J.F. Colin, F. Bertin, C. Cayron, Chemistry of Materials, 23 (2011) 4515-4524.

[16] P. Bai, D.A. Cogswell, M.Z. Bazant, Nano Letters, 11 (2011) 4890-4896.

[17] A. Van den Ven, K. Garikipati, S. Kim, M. Wagemaker, Journal of the Electrochemical Society, 156 (2009) A949-A957.

[18] N. Meethong, H.-Y.S. Huang, S.A. Speakman, W.C. Carter, Y.-M. Chiang, Advanced Functional Materials, 17 (2007) 1115-1123.

[19] H.Y.S. Huang, Y.X. Wang, Journal of the Electrochemical Society, 159 (2012) A815-A821.

[20] M.A. Stamps, H.-Y.S. Huang, ASME International Mechanical Engineering Congress and Exposition Proceeding IMECE2012-88037 (2012).

[21] I. Ansys, ANSYS commands reference, release 12.0, ANSYS, Inc, Canonsburg, PA, 2009.

[22] T. Maxisch, G. Ceder, Physical Review B, 73 (2006) 174112-174112.

[23] H. Gabrisch, J. Wilcox, M.M. Doeff, Electrochemical and Solid State Letters, 11 (2008) A25-A29.

[24] V.A. Streltsov, E.L. Belokoneva, V.G. Tsirelson, N.K. Hansen, Acta Crystallographica Section B-Structural Science, 49 (1993) 147-153.

[25] G. Rousse, J. Rodriguez-Carvajal, S. Patoux, C. Masquelier, Chemistry of Materials, 15 (2003) 4082-4090.

[26] R.D. Cook, Finite element modeling for stress analysis, John Wiley & Sons, Inc., New York, 1995.

[27] R.D. Cook, D.S. Malkus, M.E. Plesha, Concepts and Applications of Finite Element Analysis, John Willey and Sons, Inc., 1989.

[28] J.W. Hutchinson, Z. Suo, Advances in Applied Mechanics, Vol 29, 29 (1992) 63-191.

[29] L. Wang, F. Zhou, Y.S. Meng, G. Ceder, Physical Review B, 76 (2007).

[30] S.-Y. Chung, J.T. Bloking, Y.-M. Chiang, Nature Materials, 1 (2002) 128-128.

[31] N. Meethong, H.-Y.S. Huang, W.C. Carter, Y.-M. Chiang, Electrochemical and Solid State Letters, 10 (2007) A134-A138.