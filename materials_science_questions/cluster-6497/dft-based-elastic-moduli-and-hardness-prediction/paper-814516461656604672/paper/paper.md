Ab initio calculations of mechanical properties of bcc W-Re-Os random alloys: effects of transmutation of W

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 J. Phys.: Condens. Matter 28 295501

(http://iopscience.iop.org/0953-8984/28/29/295501)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 139.80.135.89
This content was downloaded on 05/06/2016 at 14:56

Please note that terms and conditions apply.

# Ab initio calculations of mechanical properties of bcc W-Re-Os random alloys: effects of transmutation of W

Xiaojie Li$^{1,2}$, Stephan Schönecker$^{2}$, Ruihuan Li$^{2}$, Xiaoqing Li$^{2}$,Yuanyuan Wang$^{1}$, Jijun Zhao$^{1}$, Börje Johansson$^{2,3}$ and Levente Vitos$^{2,3,4}$

$^{1}$ Key Laboratory of Materials Modification by Laser, Electron, and Ion Beams, Dalian University of Technology, Ministry of Education, Dalian 116024, People's Republic of China
$^{2}$ Applied Materials Physics, Department of Materials Science and Engineering, Royal Institute of Technology, Stockholm SE-10044, Sweden
$^{3}$ Department of Physics and Astronomy, Division of Materials Theory, Box 516, SE-75120 Uppsala, Sweden
$^{4}$ Research Institute for Solid State Physics and Optics, Wigner Research Center for Physics, PO Box 49, H-1525 Budapest, Hungary

E-mail: stesch@kth.se, xiaoqli@kth.se and zhaojj@dlut.edu.cn

Received 26 February 2016, revised 25 April 2016
Accepted for publication 16 May 2016
Published 3 June 2016

![](./images/814516461656604672_1.jpg)

## Abstract
To examine the effect of neutron transmutation on tungsten as the first wall material of fusion reactors, the elastic properties of $\mathrm{W}_{1-x-y}\mathrm{Re}_{x}\mathrm{Os}_{y}$ ($0 \leqslant x, y \leqslant 6\%$) random alloys in body centered cubic (bcc) structure are investigated systematically using the all-electron exact muffin-tin orbitals (EMTO) method in combination with the coherent-potential approximation (CPA). The calculated lattice constant and elastic properties of pure W are consistent with available experiments. Both Os and Re additions reduce the lattice constant and increase the bulk modulus of W, with Os having the stronger effect. The polycrystalline shear modulus, Young's modulus and the Debye temperature increase (decrease) with the addition of Re (Os). Except for $C_{11}$, the other elastic parameters including $C_{12}$, $C_{44}$, Cauchy pressure, Poisson ratio, $B/G$, increase as a function of Re and Os concentration. The variations of the latter three parameters and the trend in the ratio of cleavage energy to shear modulus for the most dominant slip system indicate that the ductility of the alloy enhances with increasing Re and Os content. The calculated elastic anisotropy of bcc W slightly increases with the concentration of both alloying elements. The estimated melting temperatures of the W-Re-Os alloy suggest that Re or Os addition will reduce the melting temperature of pure W solid. The classical Labusch-Nabarro model for solid-solution hardening predicts larger strengthening effects in $\mathrm{W}_{1-y}\mathrm{Os}_{y}$ than in $\mathrm{W}_{1-x}\mathrm{Re}_{x}$. A strong correlation between $C'$ and the fcc-bcc structural energy difference for $\mathrm{W}_{1-x-y}\mathrm{Re}_{x}\mathrm{Os}_{y}$ is revealed demonstrating that canonical band structure dictates the alloying effect on $C'$. The structural energy difference is exploited to estimate the alloying effect on the ideal tensile strength in the [00 1] direction.

Keywords: disordered W-Re-Os alloys, elastic properties, ductility, solid-solution hardening

(Some figures may appear in colour only in the online journal)

### 1. Introduction

Because of the high melting temperature, high thermal conductivity, low sputtering yield and good resistance against erosion, tungsten has been chosen as the primary candidate material for plasma-facing components of fusion reactors including ITER and possibly DEMO, especially in high-heat-flux regions such as the divertor [1]. In realistic fusion reactor environments, the plasma-facing material experiences high fluxes of both neutral and charged particles that escape from the plasma as well as strong irradiation of 14 MeV fusion neutrons.

Exposed to neutron irradiation, W undergoes transmutation to its neighboring elements (i.e. Re, Os, Hf, Ta) in the periodic table [2, 3]. Assuming a spectrum typical for fusion reactors, the bulk of the transmutation products arises from $(n,\gamma)$ and $(n,2n)$ reactions and leads mainly to Re and Os. For a commercial fusion reactor in the future, the first-wall components must be typically able to withstand a fusion environment for at least five years [4, 5]. After 5 year power-plant irradiation, it was estimated that the originally pure W will transmute into 3.8% Re, 1.38% Os, plus the remaining W [2]. Another independent estimation yielded the composition of first-wall tungsten materials as $\text{W}_{90.8}\text{Re}_{6.1}\text{Os}_{3.2}$ (model A), $\text{W}_{91.0}\text{Re}_{5.6}\text{Os}_{3.3}$ (model B), $\text{W}_{97.1}\text{Re}_{2.7}\text{Os}_{0.3}$ (model AB) after the assumed service lifetime of 5 years in the Power Plant Conceptual Study (PPCS) models [3].

Despite the importance of the transmutation effect on the mechanical properties of W and the large number of existing experiments on body centered cubic (bcc) W–Re and W–Re–Os alloys, no theoretical study reported on the ternary W–Re–Os alloys. Among the few first-principles calculations on the W–Re binary, Wei's study [6] employing special quasirandom structures (SQSs) predicted that bulk modulus and the ductility of $\text{W}_{1-x}\text{Re}_x$ ($x=0.25,0.50,0.75$) increase with Re concentration. Samolyuk *et al* [7] performed density functional theory (DFT) calculations based on the virtual crystal approximation (VCA) to treat the alloy problem and predicted lattice parameter, elastic constants and phonon dispersions. Their results also indicated that the ductility of $\text{W}_{1-x}\text{Re}_x$ alloys improves with the increase of the Re content. However, modeling a random ternary solid solution with continuous variation of its chemical composition by means of SQSs is quite cumbersome, while the use of the VCA in all-electron approaches is limited to binaries composed of neighboring elements. In this paper, we report on a systematical DFT investigation of $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ alloys with composition range of $x,y=0$–$0.06$ using the exact muffin-tin orbitals (EMTO) method [8–10] in conjunction with the coherent-potential approximation (CPA) [11–13] to describe the chemical disorder in random alloys. The CPA provides a consistent alloy theory for the average of the alloy components since it is formulated in terms of a self-averaging one-electron Green's function. We demonstrate that the volume of the alloy shrinks and the bulk modulus increases with the addition of Re and Os. The variations of Poisson's ratio ($v$), elastic modulus ratio ($B/G$) and Cauchy pressure, and the ratio of cleavage energy to shear modulus indicate consistently that the ductility of tungsten improves as a function of Re and Os concentrations but the alloying effect is more pronounced for Os. Structural energy differences and electronic structure arguments are used to explain the trends obtained for the elastic parameters and to predict the trend of the ideal tensile strength of W–Re–Os. We consider the classical Labusch–Nabarro model for solid-solution hardening, which predicts superior hardening by Os than by Re. The present *ab initio* results serve as input for coarse scale modeling of the mechanical properties.

The structure of the paper is as follows: in section 2, we describe the computational tools and the most important numerical details. The results are presented in section 3. Firstly, we calculate the properties of pure W to assess the accuracy of our method and then we study the effects of the alloying elements on bulk mechanical properties.

### 2. Computational method

The *ab initio* calculations were performed with the EMTO method [8–10], which is an improved screened Korringa–Kohn–Rostoker (KKR) method. In EMTO, the full potential is represented by overlapping muffin-tin potential spheres. Overlapping potential spheres describe the exact potential more accurately than conventional muffin-tin or non-overlapping approaches [8, 14]. The Perdew–Burke–Ernzerhof (PBE) [15] generalized gradient approximation (GGA) was chosen for the exchange-correlation functional. The CPA [11–13] was used to describe the problem of chemical disorder, and the total energy was calculated via the full charge-density technique. Since the CPA is a single-site approximation, short range order and local relaxation effects were not accounted for in the present study. Thus, all results are valid for completely disordered alloys with ideal bcc crystal structure. For the present W-Re-Os alloys, Takeuchi and Inoue [16] showed that the heat of mixing is $-4\ \text{kJ}\ \text{mol}^{-1}$ for W and Re, and $-10\ \text{kJ}\ \text{mol}^{-1}$ for W and Os, respectively. Such small negative heats of mixing would lead to the weak short range order in the alloys, which might slightly affect the description of mechanical properties of the alloys by CPA calculations. In all calculations, the Brillouin zones were sampled by a $33\times33\times33$ $\boldsymbol{k}$-point mesh to obtain the accuracy needed for elastic constants. The accuracy of the EMTO method in the *ab initio* study of physical properties of metals and alloys has been demonstrated in several previous works [8, 12, 17–23].

There are three independent single-crystal elastic constants for cubic crystals, namely $C_{11}$, $C_{12}$, and $C_{44}$. The $C_{11}$ and $C_{12}$ were obtained from the tetragonal shear modulus $C'=(C_{11}-C_{12})/2$ and the bulk modulus $B=(C_{11}+2C_{12})/3$. The bulk modulus was determined from an exponential Morse-type equation of state [24]. The two cubic shear modulus $C'$ and $C_{44}$ were calculated under orthorhombic and monoclinic lattice distortions with volume-conserving strains, respectively [22]. The following orthorhombic deformation was employed to obtain $C'$,

Table 1. Theoretical and experimental equilibrium lattice parameters ($a$ in Å) and single-crystal elastic constants ($C_{ij}$ in GPa) for bcc W.

<table>
<thead>
<tr>
<th></th>
<th>Method</th>
<th>$A$</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C'$</th>
<th>$C_{44}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Theory</td>
<td>EMTO</td>
<td>3.195</td>
<td>536.7</td>
<td>179.9</td>
<td>178.4</td>
<td>168.6</td>
</tr>
<tr>
<td></td>
<td>WIEN2K-GGA [6]</td>
<td>3.183</td>
<td>521.1</td>
<td>186.3</td>
<td>167.4</td>
<td>150.5</td>
</tr>
<tr>
<td></td>
<td>DFLRM-LDA [7]</td>
<td>3.190</td>
<td>520.9</td>
<td>200.2</td>
<td>160.4</td>
<td>141.1</td>
</tr>
<tr>
<td></td>
<td>QEP-GGA [31]</td>
<td>3.190</td>
<td>518.0</td>
<td>197.0</td>
<td>160.0</td>
<td>141.0</td>
</tr>
<tr>
<td></td>
<td>FP-LMTO-LDA [32]</td>
<td></td>
<td>553.0</td>
<td>207.0</td>
<td>173.0</td>
<td>178.0</td>
</tr>
<tr>
<td>Experiment</td>
<td>0 K</td>
<td></td>
<td>532.6 [28]</td>
<td>205.0 [28]</td>
<td>163.8 [28]</td>
<td>163.1 [28]</td>
</tr>
<tr>
<td></td>
<td>300 K</td>
<td>3.160 [29]</td>
<td>523.3 [28]</td>
<td>204.5 [28]</td>
<td>159.4 [28]</td>
<td>160.7 [28]</td>
</tr>
</tbody>
</table>

Note: The present results (EMTO) are compared to former theoretical [6, 7, 30, 31] and experimental data [28].

Table 2. Theoretical and experimental polycrystalline elastic moduli (in GPa), $B/G$ ratio, Poisson’s ratio ($\nu$) and Debye temperature ($\Theta$ in K) for bcc W.

<table>
<thead>
<tr>
<th></th>
<th>Method</th>
<th>$B$</th>
<th>$G$</th>
<th>$B/G$</th>
<th>$E$</th>
<th>$N$</th>
<th>$\Theta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Theory</td>
<td>EMTO</td>
<td>298.8</td>
<td>172.5</td>
<td>1.73</td>
<td>434.0</td>
<td>0.26</td>
<td>396.4</td>
</tr>
<tr>
<td></td>
<td>WIEN2K-GGA [6]</td>
<td>299.86</td>
<td>165.90</td>
<td>1.82</td>
<td>420.21</td>
<td>0.27</td>
<td>378.4</td>
</tr>
<tr>
<td></td>
<td>DFLRM-LDA [7]</td>
<td>307.1</td>
<td>148.51</td>
<td>2.07</td>
<td>383.68</td>
<td>0.29</td>
<td></td>
</tr>
<tr>
<td></td>
<td>QEP-GGA [31]</td>
<td>304</td>
<td>148.50</td>
<td>2.05</td>
<td>383.12</td>
<td>0.29</td>
<td></td>
</tr>
<tr>
<td>Experiment</td>
<td>0 K</td>
<td>314.15 [28]</td>
<td>163.40 [28]</td>
<td>1.92 [28]</td>
<td>417.76 [28]</td>
<td>0.28 [28]</td>
<td>384.3 [33]</td>
</tr>
<tr>
<td></td>
<td>300 K</td>
<td>310.78 [28]</td>
<td>160.18 [28]</td>
<td>1.94 [28]</td>
<td>410.08 [28]</td>
<td>0.28 [28]</td>
<td></td>
</tr>
</tbody>
</table>

Note: The present results (EMTO) are compared to former theoretical and experimental data.

$$
\begin{bmatrix}
1+\delta_0 & 0 & 0 \\
0 & 1-\delta_0 & 0 \\
0 & 0 & 1/(1-\delta_0^2)
\end{bmatrix},
$$

which leads to the energy change ($V$ abbreviates the bcc equilibrium volume)

$$
\Delta E(\delta_0)=2VC'\delta_0^2+O(\delta_0^4). \tag{1}
$$

The monoclinic distortion to compute $C_{44}$ reads

$$
\begin{bmatrix}
1 & \delta_{\text{m}} & 0 \\
\delta_{\text{m}} & 1 & 0 \\
0 & 0 & 1/(1-\delta_{\text{m}}^2)
\end{bmatrix}
$$

with corresponding energy change

$$
\Delta E(\delta_{\text{m}})=2VC_{44}\delta_{\text{m}}^2+O(\delta_{\text{m}}^4). \tag{2}
$$

Here, $\delta$ denotes the strain parameter, and for both distortions six strains (0.00, 0.01, …, 0.05) were considered.

The polycrystalline shear modulus ($G$) was obtained using the Hill average method [25, 26], $G=1/2(G_{\text{R}}+G_{\text{V}})$, where $G_{\text{R}}$ and $G_{\text{V}}$ are the Reuss and Voigt bounds, respectively. The employed computational methods for Young’s modulus ($E$), $\nu$, and the elastic Debye temperature ($\Theta_{\text{D}}$) can be found in [26]. The Zener ratio [27] is defined as $A_Z=C_{44}/C'$, (for an isotropic cubic crystal, the $A_Z$ ratio is one), which is commonly used to describe the elastic anisotropy.

## 3. Results and discussion

### 3.1. Lattice parameter and elastic constants of pure tungsten

First we assess the EMTO-PBE approach for pure bcc W. In tables 1 and 2, we list the equilibrium lattice constant, the single-crystal elastic constants, the polycrystalline elastic moduli, and the Debye temperature of W as predicted by the present method as well as the available experimental data [28, 29] and previous theoretical results [6, 7, 30–32]. From table 1, we can see that our lattice constant agrees well with the experiment data (1% deviation) and the other theoretical values. The elastic constants $C_{11}$ and $C_{44}$ are reasonably close to the experimental data, while $C_{12}$ and $C'$ are slightly underestimated and overestimated with respect to the experiment values, respectively. Compared to the experimental $B$, $G$ and $E$ listed in table 2, the present theoretical values deviate by less than 5%. The computed Poisson ratio $\nu$ is 7% smaller than the experimental data and the Debye temperature (396.4 K) accords with the experimental result (384.3 K) [33]. Overall speaking, the present theoretical method can reasonably describe the fundamental structural and elastic properties of tungsten and thus it is expected to be applicable to the present W-rich alloys as well.

### 3.2. Lattice constant and elastic parameters of W–Re binary alloy

The calculated and available experimental elastic parameters [33] for bcc W–Re binary alloys are compared to assess the accuracy of the present modeling approach. To the best of our knowledge, experimental data for the W–Os binary alloys have not reported hitherto. The theoretical single-crystal elastic constants for W–Re with up to 26 at.% Re content were calculated at the corresponding equilibrium lattice constant and the results are listed in table 3. We find that the theoretical lattice constant of $\text{W}_{1-x}\text{Re}_x$ decreases nearly linearly with increasing Re content. The variation of the theoretical lattice constant is in line with the experimental one (shown in figure 1) [34].

$C_{11}$ and $C'$ show small negative changes with increasing Re concentration, while $C_{12}$ and $C_{44}$ increase with increasing

<table>
<caption>Table 3. Theoretical equilibrium lattice parameter ($a$ in Å) and theoretical and experimental [33] single-crystal elastic constants ($C_{ij}$ in GPa) for $\text{W}_{1-x}\text{Re}_x$ alloy.</caption>
<thead>
<tr>
<th>
</th>
<th>Method</th>
<th>$a$</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C'$</th>
<th>$C_{44}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{W}_{0.97}\text{Re}_{0.03}$</td>
<td>EMTO</td>
<td>3.192</td>
<td>535.3</td>
<td>184.4</td>
<td>175.5</td>
<td>168.4</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (80 K)</td>
<td>
</td>
<td>541.4</td>
<td>213.2</td>
<td>164.1</td>
<td>162.9</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (300 K)</td>
<td>
</td>
<td>534.7</td>
<td>216.4</td>
<td>159.1</td>
<td>160.9</td>
</tr>
<tr>
<td>$\text{W}_{0.95}\text{Re}_{0.05}$</td>
<td>EMTO</td>
<td>3.191</td>
<td>533.8</td>
<td>186.4</td>
<td>173.7</td>
<td>169.6</td>
</tr>
<tr>
<td>$\text{W}_{0.90}\text{Re}_{0.10}$</td>
<td>EMTO</td>
<td>3.187</td>
<td>530.3</td>
<td>190.5</td>
<td>169.9</td>
<td>172.9</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (80 K)</td>
<td>
</td>
<td>531.0</td>
<td>218.2</td>
<td>156.4</td>
<td>170.6</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (300 K)</td>
<td>
</td>
<td>524.1</td>
<td>219.1</td>
<td>152.5</td>
<td>168.5</td>
</tr>
<tr>
<td>$\text{W}_{0.85}\text{Re}_{0.15}$</td>
<td>EMTO</td>
<td>3.184</td>
<td>529.3</td>
<td>195.8</td>
<td>166.7</td>
<td>176.7</td>
</tr>
<tr>
<td>$\text{W}_{0.80}\text{Re}_{0.20}$</td>
<td>EMTO</td>
<td>3.180</td>
<td>527.0</td>
<td>199.0</td>
<td>164.0</td>
<td>180.2</td>
</tr>
<tr>
<td>$\text{W}_{0.77}\text{Re}_{0.23}$</td>
<td>EMTO</td>
<td>3.177</td>
<td>526.4</td>
<td>202.3</td>
<td>162.0</td>
<td>181.9</td>
</tr>
<tr>
<td>$\text{W}_{0.74}\text{Re}_{0.26}$</td>
<td>EMTO</td>
<td>3.175</td>
<td>525.4</td>
<td>205.7</td>
<td>159.8</td>
<td>183.4</td>
</tr>
</tbody>
</table>

*Note:* The present theoretical values for pure W are listed for reference.

![](./images/814516461656604672_2.jpg)

Figure 1. Theoretical and experimental [34] lattice constants change of W-Re alloys as a function of Re content.

Re amount. The calculated elastic constant $C_{11}$ of $\text{W}_{0.97}\text{Re}_{0.03}$ and $\text{W}_{0.90}\text{Re}_{0.10}$ are 535.3 GPa and 530.3 GPa, respectively, which shows a compositional dependence consistent with the experimental results (541.4 GPa and 531.0 GPa, respectively). For 10 at.% Re, the calculated (experimental) $C_{12}$ and $C_{44}$ enhance by about 5.2% (6.4%) and 2.6% (4.6%), respectively, compared to their values for pure W. An experimental investigation at room temperature [33] reported that $C'$ decreases monotonically with increasing Re content, whereas $C_{44}$ slightly decreases at first ($0 \leqslant x \leqslant 0.03$) and then increases with further increasing the Re concentration. The non-monotonic experimental trend for $C_{44}$ might, however, be caused by a too large value reported for pure W as evident from the other values provided in [33]. Additional experimental investigations for dilute W-Re alloy are needed in order to resolve this issue.

In table 4, the bulk modulus, the shear modulus and Young’s modulus of the binary W-Re alloy are compared to the available experimental values [33]. The bulk and shear moduli increase with increasing Re content, whereas the compositional effect on $G$ is weaker. Young’s modulus exhibits a small increasing trend with Re addition to W. Specifically, the calculated bulk modulus of $\text{W}_{0.90}\text{Re}_{0.10}$ alloy increases by approximately 1.3% relative to that of pure W, in accordance with the experimental trend (about 3.1% increase) [33]. From table 4, we can see that the present theoretical results agree well with experimental data. Thus, we conclude that our method properly captures the elastic properties of the W–Re binary.

<table>
<caption>Table 4. Theoretical and experimental [33] polycrystalline elastic constants (in GPa), $B/G$ ratio and Poisson’ ratio ($\nu$) for $\text{W}_{1-x}\text{Re}_x$ alloy.</caption>
<thead>
<tr>
<th>
</th>
<th>Method</th>
<th>$B$</th>
<th>$G$</th>
<th>$E$</th>
<th>$\nu$</th>
<th>$B/G$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{W}_{0.97}\text{Re}_{0.03}$</td>
<td>EMTO</td>
<td>301.3</td>
<td>171.2</td>
<td>431.8</td>
<td>0.261</td>
<td>1.760</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (80 K)</td>
<td>322.6</td>
<td>163.4</td>
<td>419.3</td>
<td>0.283</td>
<td>1.975</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (300 K)</td>
<td>322.5</td>
<td>160.2</td>
<td>412.3</td>
<td>0.287</td>
<td>2.013</td>
</tr>
<tr>
<td>$\text{W}_{0.95}\text{Re}_{0.05}$</td>
<td>EMTO</td>
<td>302.2</td>
<td>171.2</td>
<td>432.0</td>
<td>0.262</td>
<td>1.765</td>
</tr>
<tr>
<td>$\text{W}_{0.90}\text{Re}_{0.10}$</td>
<td>EMTO</td>
<td>303.8</td>
<td>171.7</td>
<td>433.4</td>
<td>0.262</td>
<td>1.769</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (80 K)</td>
<td>322.5</td>
<td>164.8</td>
<td>422.4</td>
<td>0.282</td>
<td>1.957</td>
</tr>
<tr>
<td>
</td>
<td>Expt. (300 K)</td>
<td>320.8</td>
<td>161.9</td>
<td>415.8</td>
<td>0.284</td>
<td>1.981</td>
</tr>
<tr>
<td>$\text{W}_{0.85}\text{Re}_{0.15}$</td>
<td>EMTO</td>
<td>306.9</td>
<td>172.7</td>
<td>436.2</td>
<td>0.263</td>
<td>1.778</td>
</tr>
<tr>
<td>$\text{W}_{0.80}\text{Re}_{0.20}$</td>
<td>EMTO</td>
<td>308.3</td>
<td>173.5</td>
<td>438.3</td>
<td>0.263</td>
<td>1.777</td>
</tr>
<tr>
<td>$\text{W}_{0.77}\text{Re}_{0.23}$</td>
<td>EMTO</td>
<td>310.3</td>
<td>173.7</td>
<td>439.1</td>
<td>0.264</td>
<td>1.787</td>
</tr>
<tr>
<td>$\text{W}_{0.74}\text{Re}_{0.26}$</td>
<td>EMTO</td>
<td>312.3</td>
<td>173.6</td>
<td>439.3</td>
<td>0.266</td>
<td>1.799</td>
</tr>
</tbody>
</table>

*Note:* The experimental values are computed from the experimental single-crystal elastic constants using the Hill average method as explained in section 2.

### 3.3. Lattice constant and elastic parameters of W–Re–Os alloys

We now explore the mechanical properties of the W–Re–Os alloys. Figure 2 shows the lattice parameters for $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x$, $y \leqslant 0.06$) as a function of Re and Os solute concentrations. We can see that both Os and Re addition shrink the lattice constant of W, and Os has the stronger effect. These theoretical predictions are in general agreement with the trends observed in experiments [34, 35]. The smaller atomic radius of the hexagonal close packed Re (1.37 Å) and Os (1.35 Å) compared to the radius of bcc W (1.41 Å) [36] explains the above trends.

Using the present theoretical equilibrium lattice parameters, we computed the single-crystal elastic constants and the polycrystalline elastic moduli of the $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x$, $y \leqslant 0.06$) alloy. The alloying effect on the bulk modulus is displayed in figure 2. It is found that $B(x, y)$ increases with Re or Os addition, which is in line with the opposite trends seen for the lattice parameter. $B(x, y)$ varies between a minimum value of 300.0 GPa for pure W and a maximum value of 306.2 GPa belonging to $\text{W}_{0.88}\text{Re}_{0.06}\text{Os}_{0.06}$.

The theoretical single-crystal elastic constants $C_{ij}(x, y)$ of bcc $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x$, $y \leqslant 0.06$) alloys are shown in figure 3. One can see that $C_{11}(x, y)$ reduces with Os addition, and remains almost constant with doping Re. $C_{12}(x, y)$ shows

![](./images/814516461656604672_3.jpg)
![](./images/814516461656604672_4.jpg)

Figure 2. Theoretical lattice constant (in Å) and bulk modulus (in GPa) of bcc $W_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x, y \leqslant 0.06$) alloys as functions of Re and Os concentrations.

small (large) positive change with Re (Os) addition to W. The maximum changes of $C_{11}(x, y)$ and $C_{12}(x, y)$ are 16.5 GPa and 17.6 GPa, respectively. Fine *et al* [37] proposed an empirical formula to approximately calculate the melting point ($T_{\text{m}}$) for metals, which is given by

$$
T_{\text{m}}(\text{K}) = 553(\text{K}) + 5.91C_{11}(\text{K GPa}^{-1}). \tag{3}
$$

According to this equation, the melting point of pure W was estimated to be 3731.6 K using the present theoretical value of $C_{11}$. This prediction agrees surprisingly well with the experimental value (3695 K) [29]. Based on the alloying effects on $C_{11}$ (figure 3), one expects that the melting point of W should decrease with increasing Re and Os content. The largest variation in $T_{\text{m}}(x, y)$ within the present concentration range ($0 \leqslant x, y \leqslant 0.06$) is about 100 K.

Under tetragonal deformation, the structural stability of a cubic solid is characterized by the tetragonal shear constant $C'$. Figure 3 shows that both Re and Os decrease $C'$, but the alloying effect for Os exceeds the one for Re by more than a factor of two. If we consider the maximum solute concentrations of Re and Os, $C'(x, y)$ softens from $\sim$178 GPa (pure W) to $\sim$161 GPa ($\text{W}_{0.88}\text{Re}_{0.06}\text{Os}_{0.06}$ alloy). The alloying trend of $C_{44}$ is opposite to that of $C'(x, y)$. Namely, the addition of Re or Os to W slightly increases $C_{44}(x, y)$, and as a result, alloys with the highest Re and Os concentrations possess the stiffest $C_{44}(x, y)$ as shown in figure 3. The above trends can be understood if one investigates, at first, the two shear elastic constants for the three constituent elements in the same crystal structure, i.e. for bcc W and the (hypothetical) bcc phases of Re and Os. The sign and relative magnitude of $C'$ for bcc W, Re, and Os can be qualitatively estimated from the curvature of the total energy curve along the bcc–fcc Bain path [38], while precise values have been reported as well⁵ [39]. Accordingly, the trend is $C'(\text{bcc W}) > C'(\text{bcc Re}) > C'(\text{bcc Os})$, which suggests that substituting Re or Os for W is expected to diminish $C'$ by the simple rule of mixing.

For a more quantitative analysis, we notice that $C'$ for the transition metal elements correlates, in fact, with the structural energy difference (SED) between the face centered cubic (fcc) and bcc structure, $\Delta E^{\text{SED}} = E_{\text{fcc}} - E_{\text{bcc}}$ [32, 38, 40]. $\Delta E^{\text{SED}}$ follows a canonical pattern as the transition metal series is crossed from left to right corresponding to a gradual filling of the $d$-band. The characteristic pattern of the SED in transition metals is, in turn, determined by the electronic structure as revealed by canonical band theory [41]. Thus, the key to understand the trend of $C'(x, y)$ is to analyze $\Delta E^{\text{SED}}$ for the present transition metal alloy in light of the increasing $5d$-band filling due to alloying W with Re and Os. In what follows, we evaluated $\Delta E^{\text{SED}}(x, y)$ assuming constant volume fixed to the respective bcc equilibrium volume. Figure 5 shows $\Delta E^{\text{SED}}$ and $C'$ for $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ plotted as a function of the valence $d$-occupation (concentration weighted average over the alloy species). Similar to $C'$, $\Delta E^{\text{SED}}$ decreases monotonically with increasing the fraction of Re or Os and the alloying effect of Os is more pronounced than that of Re. As a matter of fact, $C'$ and $\Delta E^{\text{SED}}$ correlate strongly for the present alloy system. Due to their positions in the periodic table, Os contributes about twice as many $d$-electrons to the band filling as Re (for the same $x$ and $y$ values). This is clearly reflected in the overall downshifts of the valence band densities of states (DOSs) shown in figure 5 for the undistorted cubic structure and for a $C'$-type monoclinic distorted lattice. For $\text{W}_{0.95}\text{Re}_{0.05}$, this shift is nearly rigid with respect to W (rigid band filling), while disorder effects on the single-particle spectrum become more obvious for $\text{W}_{0.95}\text{Os}_{0.05}$.

It is tempting to analyze $C_{44}(x, y)$ by a similar electronic structure argument. However, no successful correlation between $C_{44}$ and an SED has been reported in the literature to the best of our knowledge. The most obvious correlation might be established on the basis of the simple cubic (sc)—bcc

⁵ $C'(\text{bcc W}) = 178$ GPa, $C'(\text{bcc Re}) = -12$ GPa, $C'(\text{bcc Os}) = -266$ GPa, $C_{44}(\text{bcc W}) = 172$ GPa, $C_{44}(\text{bcc Re}) = 205$ GPa, $C_{44}(\text{bcc Os}) = 283$ GPa [39].

![](./images/814516461656604672_5.jpg)

Figure 3. Theoretical single-crystal elastic constants and polycrystalline elastic moduli (in GPa) for $W_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x, y \leqslant 0.06$) alloys as functions of Re and Os concentrations.

SED on the trigonal deformation path [42, 43], since $C_{44}$ also describes the structural stability of the bcc structure under trigonal deformation (in contrast to the monoclinic distortion in equation (2)), a trigonal distortion is a stretch of the bcc structure along the body diagonal that makes equal angles; the corresponding elastic strain energy has a larger prefactor, i.e. $\Delta E(\delta_t)=6VC_{44}\delta_t^2$. We computed the sc—bcc SED for the present W–Re–Os alloys but did not find a robust correlation with $C_{44}$. On the other hand, looking again at $C_{44}$ for the three constituent elements in the bcc structure, we found that

<table><caption>Table 5. Based on the fcc–bcc structure energy difference (SED) shown in figure 5, the approximate ideal tensile strengths ($\sigma_{\text{m}}^{\text{SED}}$) in [001] direction were estimated according to equation (4).</caption>
<tbody>
<tr>
<th>Composition</th>
<td>$\sigma_{\text{m}}^{\text{SED}}$ (GPa)</td>
</tr>
<tr>
<th>W</th>
<td>26.3</td>
</tr>
<tr>
<th>$\text{W}_{0.97}\text{Os}_{0.03}$</th>
<td>24.1</td>
</tr>
<tr>
<th>$\text{W}_{0.94}\text{Os}_{0.06}$</th>
<td>21.9</td>
</tr>
<tr>
<th>$\text{W}_{0.97}\text{Re}_{0.03}$</th>
<td>25.4</td>
</tr>
<tr>
<th>$\text{W}_{0.94}\text{Re}_{0.06}$</th>
<td>24.4</td>
</tr>
<tr>
<th>$\text{W}_{0.94}\text{Re}_{0.03}\text{Os}_{0.03}$</th>
<td>23.2</td>
</tr>
<tr>
<th>$\text{W}_{0.94}\text{Re}_{0.02}\text{Os}_{0.04}$</th>
<td>22.7</td>
</tr>
</tbody>
</table>

$C_{44}(\text{bcc W}) < C_{44}(\text{bcc Re}) < C_{44}(\text{bcc Os})$ [39]. This finding indicates that the alloying effect of Re and Os on $C_{44}$ of W follows the trends set by the solute elements possessing larger $d$-band occupation numbers than W. In fact, the canonical pattern of $C_{44}$ versus band filling correlates reasonably well with the one for the bulk modulus assuming the bcc structure for all transition metal elements [39]. Both the bulk modulus and $C_{44}$ reach their peak values in the bcc structure somewhat above half $d$-band filling, i.e. when the Fermi level is located above the characteristic bcc pseudo gap in the DOS (see the position of the Fermi level for the present alloy system in figure 5). Since the bulk modulus indicates metallic cohesion, and the shear constant $C_{44}$ follows the bulk modulus closely, $C_{44}$ may equally well be used to characterize cohesion in metals.

On the basis of the fcc–bcc SED, we are also able to predict the chemical effect on the ideal tensile strength (ITS). The ITS describes the mechanical properties of ideal defect-free crystals for large elongations [44]. For bcc crystals, the [001] direction is the weakest direction. Li et al have shown that alloying effects on the ITS and to some extent also the magnitude of the ITS (in the [001] direction) can be captured by a simple auxiliary stress, $\sigma_{\text{m}}^{\text{SED}}$, defined as [23, 45]

$$
\sigma_{\text{m}}^{\text{SED}}=\frac{1+\epsilon}{V} \frac{\Delta E^{\text{SED}}}{\Delta \epsilon}. \tag{4}
$$

Here, $\nabla \epsilon \approx 0.260$ is the strain needed to go from bcc to fcc lattice. Thus, $\sigma_{\text{m}}^{\text{SED}}$ depends only on $\Delta E^{\text{SED}}$ and the theoretical bcc equilibrium volume ($V$). With help of equation (4), we obtained $\sigma_{\text{m}}^{\text{SED}} = 26.3$ GPa for pure W, which is surprisingly close to the explicitly computed value of 28.9 GPa [46]. The approximate ITS $\sigma_{\text{m}}^{\text{SED}}$ for W-based alloys were also estimated and the results are listed in table 5. Compared to pure W, we can see that $\sigma_{\text{m}}^{\text{SED}}$ decreases with increasing Re or Os, and Os shows stronger effect. From the computed stresses, we conclude that both Re and Os additions decrease the ITS of W.

The shear modulus $G(x, y)$ and Young's modulus $E(x, y)$ are shown in figure 3. The addition of Re enlarges the shear modulus, and Os reduces it. However, the alloying effect on $G(x, y)$ is very small, and the largest variation is only 3 GPa. The reason for the above behavior is attributed to the opposite trends of Re and Os on $C_{44}(x, y)$ and $C'(x, y)$. $E(x, y)$ has a trend similar to the one of $G(x, y)$, and alloys containing high-Re ($x > 0.04$) and low-Os ($y < 0.02$) contents possess the maximum values.

The ductility/brittleness of an engineering alloy is set by various microscopic mechanisms controlling the dislocation glide, whose description solely from ab initio is not feasible. Ductility correlates, however, with other mechanical parameters, which are in reach of ab initio approaches [47]. Two phenomenological indicators for ductility/brittleness are the Cauchy pressure ($C_{12}$–$C_{44}$) and the $B/G$ ratio as introduced by Pettifor [48] and Pugh [49], respectively. If the $B/G$ ratio is larger than 1.75 and the Cauchy pressure is positive, then the material is typically ductile; otherwise, it is in the brittle regime. Poisson's ratio can also be used to indicate the ductility of metallic materials: a material is more ductile if Poisson's ratio is higher [50, 51]. For isotropic polycrystalline materials, the $B/G$ criterion for ductility corresponds to $v > 0.26$. The alloying effects on the Cauchy pressure, $B/G$, and Poisson's ratio are shown in figure 4. One can see that the addition of both Os and Re enhances the $B/G$ ratio and Cauchy pressure, but Re shows a weaker effect. Alloys with low-Os ($<1.5\%$) concentration have the lowest $B/G$ values ($\sim$1.74), and alloys with the largest $B/G$ ratios ($\sim$1.78) correspond to high-Re ($>4\%$) and high-Os ($>5\%$) contents. The values of the Cauchy pressure are positive for all W-based alloys and follow the same trend as the $B/G$ ratio as a function of the solute concentrations. Poisson's ratio increases with doping of Re and Os and the effect is more obvious with the addition of Os.

More sophisticated physical measures of the ductile-brittle behavior of metallic materials involve a competition between crack propagation and local plastic deformation, e.g. the dissipation of energy by crack blunting [47, 52]. This competition is embodied in the ratio of brittle cleavage stress ($\sigma_{\text{cl}}$) in Griffith's theory [53] to the shear modulus for the most dominant slip system in bcc (slip in bcc systems occurs primarily in the $\{110\}$ plane along the $\langle 111 \rangle$ direction with Burgers vector (1/2, 1/2, 1/2)), viz [47].

$$
\{110\}=\sigma_{\text{cl}.}\{110\}/G\{110\}\langle 111 \rangle,
$$

where

$$
G\{110\}\langle 111 \rangle=\frac{3 C_{44} C^{\prime}}{C^{\prime}+2 C_{44}}
$$

and the cleavage stress of the $\{110\}$ plane is given by

$$
\sigma_{\text{cl}.}\{110\}=\left(\frac{E_{110} \gamma_{110}}{d_{110}}\right)^{1 / 2}.
$$

Here, $E_{110}$, $\gamma_{110}$, and $d_{110}$ are Young's modulus along $\langle 110 \rangle$ ($E_{110}=12 C^{\prime} B C_{44}/(C_{11} C_{44}+3 C^{\prime} B)$), the surface energy of the $\{110\}$ surface facet, and the interlayer distance between adjacent $\{110\}$ planes, respectively. We computed $\{110\}$ for bcc pure W, and W-based W–Re–Os alloys using the calculated lattice constants and elastic parameters, and obtained the surface energies from slab calculations following [54]. The reference bulk energy was deduced from a linear fit to slab total energies with 7, 9, and 11 atomic layers separated by seven vacuum layers.

The measure $\{110\}$ is also shown in figure 4. It increases with the addition of Re/Os and the alloying effect is more

![](./images/814516461656604672_6.jpg)

Figure 4. Theoretical Cauchy pressure (in GPa), $B/G$ ratio, elastic anisotropy ($A_Z$), Debye temperature ($\Theta$) (in K), Poisson's ratio ($\nu$) and $\{110\}$ for $\text{W}_{1-x-y}\text{Re}_x\text{Os}_y$ ($0 \leqslant x, y \leqslant 0.06$) alloys as a function of Re and Os concentration.

pronounced for Os than for Re. The increase in $\{110\}$ signals that cleavage (crack propagation) becomes more difficult relative to plastic deformation at the dominant slip plane. This result suggests that the ductility of the alloy increases with increasing solute concentration. The variation of $\{110\}$ is consistent to those of $B/G$, the Cauchy pressure and the Poisson ratio. In summary, the trends of all investigated ductility criteria support the fact that the W-based alloy is

more ductile than pure W due to incorporation of Re or Os. Experimentally, alloying Re into W was indeed reported to improve ductility [33].

The elastic Zener ($A_Z$) anisotropy [27] and the Debye temperature $(\Theta)$ for the $\mathrm{W}_{1-x-y}\mathrm{Re}_x\mathrm{Os}_y$ $(0 \leqslant x, y \leqslant 0.06)$ alloys as a function of Re and Os concentrations are plotted in figure 4. The elastic anisotropy plays a significant role in the gliding of dislocations and yield strength of materials. For pure W, the present $A_Z$ is 0.95, with a 5% error when compared to the experimental value of 0.996 reported by Featherston *et al* [28]. The deviation mainly follows from the overestimation of $C'$ (table 1). The above results show that pure W is almost isotropic at 0 K. One can see from figure 4 that the $A_Z$ ratio strongly (slightly) increases with increasing Os (Re) concentration. According to our theoretical results, some W–Re–Os alloys are still elastically isotropic, if $y < 0.04$, and $\mathrm{W}_{1-x-y}\mathrm{Re}_x\mathrm{Os}_y$ alloys with high Re- and/or Os- concentrations $(x + y > 0.1)$ become anisotropic with $A_Z > 1.0$. Besides, within the entire concentration ranges explored, the variation of the Debye temperature for the $\mathrm{W}_{1-x-y}\mathrm{Re}_x\mathrm{Os}_y$ alloys is only about 4.1 K with minimum and maximum at 393.2 K and 397.3 K, respectively. Due to the small Debye temperature change by alloying, one could conclude that lattice vibrations have no significant compositional effect on the phase stability of $\mathrm{W}_{1-x-y}\mathrm{Re}_x\mathrm{Os}_y$ $(0 \leqslant x, y \leqslant 0.06)$.

From the above discussions, the overall transmutation effect of Os on the mechanical properties of W is more pronounced than that of Re, which can be understood by the relative positions of these three elements in the periodic table. An increase of the amount of Re (Os) increases the bulk modulus of the alloys parallel to shrinking the volume. Meanwhile, the ductility of the alloy is enhanced as indicated by the computed Cauchy pressure, Poisson's ratio, $B/G$ and $\{110\}$ by the addition of Re (Os) content. In addition, the high melting temperature of bulk W is moderately reduced by alloying with Re and Os, as is the Debye temperature.

### 3.4. Solid solution hardening (SSH)
As an important mechanical property of materials, hardness measures the resistance of a solid matter to various kinds of permanent shape change when a force is applied. Low hardness of materials limits their applications. There are various methods to improve the hardness of materials, such as work hardening, solid-solution hardening (SSH) by interstitial atoms or by substitutional atoms, and refinement of grain size. Here we assume homogeneous solid solutions, and thus focus on the SSH effect only.

Essentially, SSH is due to dislocation pinning by solute atoms, which has been described by different models [55–58]. The Labusch–Nabarro (LN) semi-empirical model [56–58] is often used to describe the hardening mechanism in alloys. In the LN model, dislocation pinning is mostly determined by the size misfit and elastic misfit parameters. They are calculated from the concentration dependent Burgers vector and the shear modulus.

<table>
<caption>Table 6. Theoretical misfit parameters and solid solution hardening (SSH, $\Delta\tau$/Const. is tabulated) as a function of solute content.</caption>
<thead>
<tr>
<th></th>
<th>$\varepsilon_b$</th>
<th>$\varepsilon_G$</th>
<th>$\varepsilon_{G-\mathrm{LN}}'$</th>
<th>$\varepsilon_L$</th>
<th>SSH</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\mathrm{W}_{0.98}\mathrm{Os}_{0.02}$</td>
<td>−0.360</td>
<td>−2.071</td>
<td>−1.017</td>
<td>3.743</td>
<td>0.092</td>
</tr>
<tr>
<td>$\mathrm{W}_{0.96}\mathrm{Os}_{0.04}$</td>
<td>−0.367</td>
<td>−1.853</td>
<td>−0.962</td>
<td>3.793</td>
<td>0.149</td>
</tr>
<tr>
<td>$\mathrm{W}_{0.94}\mathrm{Os}_{0.06}$</td>
<td>−0.354</td>
<td>−2.240</td>
<td>−1.057</td>
<td>3.698</td>
<td>0.189</td>
</tr>
<tr>
<td>$\mathrm{W}_{0.98}\mathrm{Re}_{0.02}$</td>
<td>−0.281</td>
<td>0.682</td>
<td>0.509</td>
<td>2.855</td>
<td>0.064</td>
</tr>
<tr>
<td>$\mathrm{W}_{0.96}\mathrm{Re}_{0.04}$</td>
<td>−0.248</td>
<td>1.306</td>
<td>0.790</td>
<td>2.601</td>
<td>0.090</td>
</tr>
<tr>
<td>$\mathrm{W}_{0.94}\mathrm{Re}_{0.06}$</td>
<td>−0.250</td>
<td>1.116</td>
<td>0.716</td>
<td>2.605</td>
<td>0.118</td>
</tr>
</tbody>
</table>

According to the LN model, the SSH can be described as
$$
\Delta\tau=\mathrm{Const.} \times c^{2/3} \times \varepsilon_L^4, \tag{7}
$$
where Const. is a host specific positive constant (which does neither depend on $c$ nor on the size of the misfit) [56], $c$ is the atomic fraction of the solute atom, $\varepsilon_L$ is the Fleischer parameter defined as
$$
\varepsilon_L=\left[\varepsilon_{G-\mathrm{LN}}'^2+\alpha\varepsilon_b^2\right]^{1/2}, \tag{8}
$$
and
$$
\varepsilon_{G-\mathrm{LN}}'=\varepsilon_G/(1+0.5|\varepsilon_G|), \tag{9}
$$

Here $\alpha$ is a parameter, we adopted $\alpha=10$ in this work (usually, the value of $\alpha$ is between 9 and 16), and $\varepsilon_L$ and $\varepsilon_G$ are the volume misfit parameter and modulus misfit parameter, respectively. $\varepsilon_b$ and $\varepsilon_G$ were obtained from the following equations:
$$
\varepsilon_b=[\delta(b)/\delta(c)]/b(0), \tag{10}
$$
and
$$
\varepsilon_G=[\delta(G)/\delta(c)]/G(0), \tag{11}
$$
where $b$ is the Burgers vector (lattice parameter) and $G$ is the shear modulus. In the following, the concentration $c$ stands for either $x$ or $y$.

Table 6 shows the theoretical misfit parameters and SSH for the binary alloys (W-$c$\%Os/W-$c$\%Re, $c=2,4,6$). These results indicate that the hardness of bcc W is enhanced with increasing Os or Re, and that Os shows a stronger effect due to the larger misfit parameters. An experimental measurement [35] showed that the hardness of W strongly increases with addition of Os, and slightly decreases first $(c<5\%)$ and then increases as a function of Re. Another experiment [59] showed that the hardness of the alloy increases as a function of Re (Os) content and the effect is more obvious for Os. Overall, our predicted alloying trends agree with the experimental observations. For the ternary alloys, the SSHs were estimated by simply summing the effects obtained from the W–Re and W–Os binary alloys, and the results are shown in figure 6. The hardness increases with the addition of the impurity contents (Re/Os), which is in line with the experimental results [35]. Alloys with higher Re ($>4\%$) and Os ($>4\%$) contents exhibit the highest SSHs.

![](./images/814516461656604672_7.jpg)

![](./images/814516461656604672_8.jpg)

Figure 5. Left panel: the fcc-bcc SED and $C'$ for $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ alloy (left), plotted as a function of the average valence $d$-band occupation as obtained in the bcc structure. The average $5d$-band filling in the fcc structure nearly equals the one in the bcc phase. Notice the difference in the Re and Os alloying effects embodied in the distinct slopes for the $\text{W}_{1-x}\text{Re}_{x}$, $\text{W}_{1-y}\text{Os}_{y}$, and $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ data sets. Right panel: density of states (DOS, normalized per atom) for pure W, W-5%Os and W-5%Re alloys (right) without distortion and for a $C'$-type monoclinic distorted lattice.

![](./images/814516461656604672_9.jpg)

Figure 6. Theoretical solid solution hardening of $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ alloy as functions of Re and Os concentrations. Plotted is $\Delta\tau/$ Const. (dimensionless).

### 4. Conclusion
Using the exact muffin-tin orbital method in conjunction with the coherent-potential approximation, the elastic properties of the W-based $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ ($0\leqslant x, y\leqslant0.06$) solid solution were systematically calculated. Both Re and Os solute atoms gradually shrink the lattice constants and lead to an increasing trend of the bulk modulus as the amount of Re or Os increases. The estimated melting temperatures of the alloy shows that the inclusion of both solute atoms decreases the melting point. The two cubic shear elastic constants show opposite alloying trends and the variation of $C'(x, y)$ is more pronounced. A strong correlation between $C'$ and the fcc-bcc structural energy difference for $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ was found, which demonstrates that canonical band structure captures the alloying effect on $C'$. The structural energy difference was used to estimate the alloying effect on the ideal tensile strength in the [001] direction. Meanwhile, the shear modulus and Young's modulus show a positive effect as a function of Re content and a negative effect as a function of Os content. The $B/G$ ratio and the Cauchy pressure increase as a function of Os content but remain almost constant with the addition of Re. This finding indicates that Os is expected to increase the ductility of the alloy. The variation of the recently suggested ductility measure {110} indicates that the ductility of the alloy increases as a function of Re/Os contents supporting the previous result. The variation of the elastic anisotropy shows that the $\text{W}_{1-x-y}\text{Re}_{x}\text{Os}_{y}$ alloy becomes elastically more isotropic as the total solute concentration approaches the threshold $x + y = 0.03$ from below, and gradually more anisotropic as the total concentration is above this threshold ($x + y > 0.1$ exhibit the largest anisotropy). The slight variation of the Debye temperature indicates that lattice vibrations are not expected to have a significant compositional influence on the phase stability of the investigated W-based alloy. We employed the classical Labusch-Nabarro model for solid-solution hardening and predict larger strengthening effects in $\text{W}_{1-y}\text{Os}_{y}$ than in $\text{W}_{1-x}\text{Re}_{x}$. We combined the effects obtained from the W-Re and W-Os binary alloys to estimate the solid-solution hardening for the ternary alloys. The present theoretical results may serve as starting point to establish the

mechanical properties of W-based ternary alloy and should lay the foundation for further studies of the transmutation effect of W as first-wall material in fusion reactors.

## Acknowledgments
This work was supported by National Magnetic Confinement Fusion Energy Research Project (2015GB118001), the Swed- ish Research Council, the Swedish Foundation for Strategic Research, and the China Scholarship Council. The Hungarian Scientific Research Fund (OTKA 84078 and 109570) are also acknowledged for financial support.

## References
[1] Pintsuk G 2012 *Tungsten as a Plasma-Facing Material* (Amsterdam: Elsevier) pp 551–81

[2] Gilbert M and Sublet J-C 2011 *Nucl. Fusion* **51** 043005

[3] Cottrell G, Pampin R and Taylor N 2006 *Fusion Sci. Technol.* **50** 89–98

[4] Maisonnier D, Cook I, Pierre S, Lorenzo B, Luciano G, Prachai N, Aldo V and Team P 2006 *Fusion Eng. Des.* **81** 1123–30

[5] Maisonnier D *et al* 2005 *Fusion Eng. Des.* **75** 1173–9

[6] Wei N, Jia T, Zhang X, Liu T, Zeng Z and Yang X 2014 *AIP Adv.* **4** 057103

[7] Samolyuk G D, Ossetskiy Y N and Stoller R E *First-Principles Investigation of the Influence of Alloying Elements on the Elastic and Mechanical Properties of Tungsten* (Oak Ridge: National Laboratory)

[8] Vitos L 2001 *Phys. Rev. B* **64** 014107

[9] Vitos L, Skriver H L, Johansson B and Kollár J 2000 *Comput. Mater. Sci.* **18** 24–38

[10] Andersen O K, Jepsen O and Krier G 1994 *Lectures on Methods of Electronic Structure Calculations* (Singapore: World Scientific) pp 63–124

[11] Gyorffy B L 1972 *Phys. Rev. B* **5** 2382–4

[12] Taga A, Vitos L, Johansson B and Grimvall G 2005 *Phys. Rev. B* **71** 014201

[13] Vitos L, Abrikosov I and Johansson B 2001 *Phys. Rev. Lett.* **87** 156401

[14] Andersen O K, Arcangeli C, Tank R W, Saha-Dasgupta T, Krier G, Jepsen O and Dasgupta I 1998 *Tight-Binding Approach to Computational Materials Science* (Pittsburgh, PA: Materials Research Society)

[15] Perdew J P, Burke K and Ernzerhof M 1996 *Phys. Rev. Lett.* **77** 3865

[16] Takeuchi Aand Inoue A 2005 *Mater. Trans.* **46** 2817–29

[17] Zander J, Sandström R and Vitos L 2007 *Comput. Mater. Sci.* **41** 86–95

[18] Vitos L, Korzhavyi P A and Johansson B 2003 *Nat. Mater.* **2** 25–8

[19] Huang L, Vitos L, Kwon S, Johansson B and Ahuja R 2006 *Phys. Rev. B* **73** 104203

[20] Magyari-Köpe B, Grimvall G and Vitos L 2002 *Phys. Rev. B* **66** 179902

[21] Magyari-Köpe B, Vitos L and Grimvall G 2004 *Phys. Rev. B* **70** 052102

[22] Li X, Zhang H, Lu S, Li W, Zhao J, Johansson B and Vitos L 2012 *Phys. Rev. B* **86** 014105

[23] Li X, Tian F, Schönecker S, Zhao J and Vitos L 2015 *Sci. Rep.* **5** 12334

[24] Moruzzi V, Janak J and Schwarz K 1988 *Phys. Rev. B* **37** 790–9

[25] Hill R 1952 *Proc. Phys. Soc. A* **65** 349

[26] Vitos L 2007 *Computational Quantum Mechanicals for Materials Engineers* (Berlin: Springer)

[27] Zener C 1948 *Elastisity and Anelasticity of Metals* (Chicago, IL: University of Chicago Press)

[28] Featherston F and Neighbours J 1963 *Phys. Rev.* **130** 1324–33

[29] Charles K, Paul M and Paul M 1976 *Introduction to Solid State Physics* vol 8 (New York: Wiley)

[30] Romaner L, Ambrosch-Draxl C and Pippan R 2010 *Phys. Rev. Lett.* **104** 195503

[31] Samolyuk G D, Osetsky Y and Stoller R 2013 *J. Phys.: Condens. Matter* **25** 025403

[32] Söderlind P, Eriksson O, Wills J and Boring A 1993 *Phys. Rev. B* **48** 5844

[33] Ayres R A, Shannette G W and Stein D F 1975 *J. Appl. Phys.* **46** 1526

[34] Fujitsuka M, Tsuchiya B, Mutoh I, Tanabe T and Shikama T 2000 *J. Nucl. Mater.* **283** 7 1148–51

[35] He J-C, Hasegawa A, Fujiwara M, Satou M, Shishido T and Abe K 2004 *Mater. Trans.* **45** 2657–60

[36] Smith D W 1990 *Inorganic Substances* (Cambridge: Cambridge University Press)

[37] Fine M E, Brown L D and Marcus H L 1984 *Script. Metall.* **18** 951–6

[38] Wills J M, Eriksson O, Söderlind P and Boring A M 1992 *Phys. Rev. Lett.* **68** 2802–5

[39] Schönecker S 2011 Theoretical studies of epitaxial bain paths of metals *PhD Thesis* TU Dresden

[40] Söderlind P, Ahuja R, Eriksson O, Wills J M and Johansson B 1994 *Phys. Rev. B* **50** 5918–27

[41] Skriver H L 1985 *Phys. Rev. B* **31** 1909–23

[42] Šob M, Wang L and Vitek V 1997 *Comput. Mater. Sci.* **8** 100–6

[43] Wang L G and Šob M 1999 *Phys. Rev. B* **60** 844–50

[44] Clatterbuck D M, Chrzan D C and Morris J W 2003 *Acta Mater.* **51** 2271–83

[45] Li X, Schönecker S, Zhao J, Johansson B and Vitos L 2014 *Phys. Rev. B* **90** 024201

[46] Černý M and Pokluda J 2007 *Phys. Rev. B* **76** 024115

[47] Wang G, Schönecker S, Hertzman S, Hu Q-M, Johansson B, Kwon S K and Vitos L 2015 *Phys. Rev. B* **91** 224203

[48] Pettifor D G 1992 *Mater. Sci. Technol.* **8** 345–9

[49] Pugh S F 1954 *London Edinburgh Dublin Phil. Mag. J. Sci.* **45** 823–43

[50] Yoo M, Takasugi T, Hanada S and Izumi O 1990 *Mater. Trans. JIM* **31** 435–42

[51] Gao M C, Doğan Ö N, King P, Rollett A D and Widom M 2008 *J. Miner. Met. Mater. Soc.* **60** 61–5

[52] Rice J R 1992 *J. Mech. Phys. Solids* **40** 239–71

[53] Griffith A A 1921 *Philos. Trans. R. Soc. A* **221** 163

[54] Boettger J C 1994 *Phys. Rev. B* **49** 16798

[55] Gypen L A and Deruyttere A 1981 *Script. Metall.* **15** 815–20

[56] Labusch R 1972 *Acta Metall.* **20** 917–27

[57] Fleischer R L 1963 *Acta Metall.* **11** 203–9

[58] Nabarro F R N 1977 *Phil. Mag.* **35** 613–22

[59] Tanno T, Hasegawa A, He J-C, Fujiwara M, Nogami S, Satou M, Shishido T and Abe K 2007 *Mater. Trans.* **48** 2399–402