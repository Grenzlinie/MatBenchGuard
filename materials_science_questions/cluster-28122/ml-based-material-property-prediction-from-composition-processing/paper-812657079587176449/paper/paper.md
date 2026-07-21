Received December 26, 2015, accepted January 13, 2016, date of publication January 22, 2016, date of current version March 8, 2016.

Digital Object Identifier 10.1109/ACCESS.2016.2521162

# Modeling and Optimizing Tensile Strength and Yield Point on a Steel Bar Using an Artificial Neural Network With Taguchi Particle Swarm Optimizer

PING-YI CHOU¹, JINN-TSONG TSAI², AND JYH-HORNG CHOU³,⁴,⁵, (Fellow, IEEE)
¹Institute of Engineering Science and Technology, National Kaohsiung First University of Science and Technology, Kaohsiung 824, Taiwan
²Department of Computer Science, National Pingtung University, Pingtung City 900, Taiwan
³Department of Electrical Engineering, National Kaohsiung University of Applied Sciences, Kaohsiung 807, Taiwan
⁴Institute of Electrical Engineering, National Kaohsiung First University of Science and Technology, Kaohsiung 824, Taiwan
⁵Department of Healthcare Administration and Medical Informatics, Kaohsiung Medical University, Kaohsiung 807, Taiwan

Corresponding author: J.-H. Chou (choujh@kuas.edu.tw)

This work was supported by the Ministry of Science and Technology, Taiwan, under Grant NSC 102-2221-E-151-021-MY3,
Grant NSC 102-2221-E-153-002, and Grant MOST 103-2221-E-153-004-MY2.

**ABSTRACT** A Taguchi particle swarm optimization (TPSO) with a three-layer feedforward artificial neural network (ANN) is used to model and optimize the chemical composition of a steel bar. The novel contribution of a TPSO is the use of a Taguchi method mechanism to exploit better solutions in the search space through iterations, the use of the conventional non-linear PSO to increase convergence speed, and the use of random movement for particle diversity. The exploration and exploitation capability of the TPSO were confirmed by performance comparisons with other PSO-based algorithms in solving high-dimensional global numerical optimization problems. Experiments in this paper showed that the TPSO provides higher computational efficiency and higher robustness when solving problems involving seven non-linear benchmark functions, including three unimodal functions, one multimodal functions, two rotated functions, and one shifted functions. The results for the computational experiments show that the TPSO outperforms other PSO-based algorithms reported in the literature. Finally, the results obtained by a TPSO-based ANN model of the chemical composition of the steel bar were consistent with the actual data. That is, the proposed TPSO with three-layer feedforward ANN can be used in practical applications.

**INDEX TERMS** Taguchi method, particle swarm optimization, feedforward artificial neural network, chemical composition of steel bar, yield point, tensile strength.

## I. INTRODUCTION
In recent years, the use of steel reinforcing bars in buildings, bridges, and other concrete structure has increased in Asia. However, corrosion is a common problem when using reinforcing steel bars in concrete structures such as building and bridges. In Taiwan, earthquakes are a common natural disaster because Taiwan is located in the western portion of the Circum-Pacific seismic belt. Nearly 18,000 seismic events occur annually in the region surrounding Taiwan, and the most destructive earthquakes have caused substantial property losses and casualties. Examples include the $M_L = 7.1$ Meishan earthquake that caused 1258 deaths in 1906, the $M_L = 7.1$ Hsinchu-Taichung earthquake that caused 3276 deaths in 1935, and the $M_L = 7.3$ Chi-Chi earthquake that caused 2455 deaths in 1999.The damage caused by the Chi-Chi earthquake in Central Taiwan was particularly severe. Therefore, the earthquake resistance of steel bars has become an important issue. The quality of steel bars usually depends on the rolling process used during fabrication [1]–[5]. Recent developments in computational intelligence techniques have enabled the use of artificial neural networks (ANNs) to improve the steel rolling process. Peng et al. [6] noted several related ways to control the strip shape such as side depression adjustment, work roll bending, and middle roll axial shifting caused unpredictable results. Therefore, ANN was used to recognize the strip shape pattern.

VOLUME 4, 2016
2169-3536 © 2016 IEEE. Translations and content mining are permitted for academic research only.
Personal use is also permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

In Abdalla and Hawileh [7], an ANN model used to predict the low-cycle fatigue life of steel reinforcing bars revealed that the analysis and design of the bars should consider both the strain ratio and the maximum strain because they both significantly affect low-cycle fatigue life, especially when the maximum strain is low. To minimize the high costs of direct tensile tests, Ghaisari et al. [8] developed an intelligent ANN-based method of indirectly monitoring the mechanical properties of steel parts. Golafshani et al. [9] proposed a fuzzy logic ANN model for predicting the bonding strength of steel bars used to reinforce concrete. They concluded that their ANN model was more accurate than conventional fuzzy logic model. Bagheripoor and Bisadi [10] used a four-input two-output ANN to improve rolling force and rolling torque in a hot strip mill. Their experimental results showed that the ANN model is feasible for optimizing the rolling schedule. In Taghizadeh et al. [11], tempering temperature and time were used as parameters of an ANN model for predicting how water quenching affects hardness in specimens of tempered AISI 1045 steel. Although the above studies agree that ANN is an effective tool for optimizing the steel bar rolling process, improvements in the rolling process have been limited. The essential factor in the quality of the steel bar is the chemical composition [12]–[16]. Studies such as Cadoni et al. [17] and Sato et al. [18] indicate the composition (i.e., carbon, sulfur, phosphorus, silicon, manganese, carbon equivalent (CE), copper, etc.) of a steel specimen affects its yield point (YP) and tensile strength (TS). That is, optimization of the composition of steel is rarely reported and needs further study.

Recent applications of particle swarm optimization (PSO) algorithm have demonstrated its effectiveness for solving engineering problems such as optimization of designs for antennas [19], manipulator control systems [20], DC-DC converters [21], permanent-magnet synchronous machines [22], and graphic processing units [23]. The advantages of PSO for solving these problems are its simple structure, fast convergence speed, and easy modification.

In this study, a Taguchi PSO (TPSO) was combined with a three-layer feedforward ANN. The TPSO-based three-layer feedforward ANN is used to model ten chemical components of steel bar and their relationships to quality evaluation criteria. Finally, the TPSO is used to optimize the weight values for each layer of the proposed ANN model. To find the global best particle, the TPSO combines Taguchi method, random movement method, and conventional non-linear PSO. The novel mechanism of the TPSO is the use of Taguchi combination to increase the population diversity. The Taguchi combination uses three main tools: orthogonal array (OA), signal-to-noise ratio (SNR), and response table. The SNR is used as a quality measure for each experimental design [24], [25], and the OA provides a set of different combination rules for generating candidate particles. The response table obtains the best combination of design parameters based on the best factors or the best combination of factors. As the Taguchi combination creates new particles, it systematically enhances the robustness and convergence performance of the PSO. The structure of the TPSO is simplified by using a conventional non-linear PSO moving mechanism for population evolution. Meanwhile, to ensure that the global best particle is moved during iterations, the proposed method uses random movement method to perform random movement in a certain probability by the global best particle.

This paper is organized as follows. Section 2 defines the problem considered in this study. Section 3 presents the TPSO combined with three-layer feedforward ANN. Section 4 describes the experimental settings and then reports and discusses the experimental results. Section 5 concludes the study.

## II. PROBLEM DESCRIPTION
Although chemical composition is the key technology in steel bar manufacturing, the settings and procedures conventionally used in the steel bar manufacturing process are often based on the experience of the engineer. According to Chinese National Standard (CNS) 560 [26], the important chemical components of steel bars are carbon, silicon, manganese, phosphorus, sulfur, and CE. The CNS560 expressly stipulates restrictions for each chemical element. The major chemical component of steel bar is carbon, which determines mechanical strength. Increasing the carbon content increases mechanical strength but reduces weldability. If gaseous elements such as oxygen (O2) and nitrogen (N2) mix with molten steel during the steelmaking process, the internal and external properties of the steel bar become unbalanced. Therefore, ferro-silicon (Fe-Si) is used to eliminate excess gas. According to CNS560, the percentage of silicon remaining in the steel bar must be lower than 0.55%. Rinebolt and Harris [27] further reported that a 0.1% change in silicon causes a 0.6 kgf/mm2 change in YP and a 1.2 kgf/mm2 change in TS.

Manganese changes the TS and YP of steel bar, which then change density and weldability. For example, Rinebolt and Harris (1951) reported that a 0.1% change in manganese causes a 1 kgf/mm2 change in YP and a 1.3 kgf/mm2 change in TS. Phosphorus reduces the weldability of steel bar but is difficult to eliminate. Sulfur is also difficult to eliminate. Therefore, CNS560 strictly stipulates that both phosphorus and sulfur should be lower than 0.045%. The CE represents the effect of carbon on weldability. In the steel bar manufacturing process, the carbon equivalent is used to convert all chemical compositions to units of carbon weldability. Eq. (2.1) below is used to calculate CE. To ensure that fabricated steel bar has adequate weldability, CNS560 standard for CE is less than 0.55%.

$$
CE\% = C\%+\frac{Mn\%}{6}+\frac{Cu\%}{40}+\frac{Ni\%}{20}+\frac{Cr\%}{10}-\frac{Mo\%}{50}-\frac{V\%}{10} \tag{2.1}
$$

where $CE\%$ denotes the CE of the steel bar and where $C\%$, $Mn\%$, $Cu\%$, $Ni\%$, $Cr\%$, $Mo\%$, and $V\%$ are the percentages of carbon, manganese, copper, nickel, chrome, molybdenum,

and vanadium of the steel bar, respectively. The properties of steel bar are generally affected by ten chemical components: carbon (C%), silicon (Si%), manganese (Mn%), phosphorus (P%), sulfur (S%), copper (Cu%), nickel (Ni%), chrome (Cr%), molybdenum (Mo%), vanadium (V%), and CE%. The CE% can be calculated by Eq. (2.1). The output responses include the TS and YP. For steel bar fabrication, TS is defined as the maximum stress that a material can endure before breaking and failing, and the YP is defined as the maximum stress point at which a material begins to deform plastically. Once the YP is passed, some of the deformation becomes permanent and non-reversible. Fig. 1 shows how the YP and TS of steel bars are related [28]. Generally, high YP and TS values are desirable. However, the different combinations of chemical elements complicate the relationship between YP and TS, and mathematically expressing the relationship between ten chemical elements and two output responses is difficult. In other words, to achieve a high YP and a high TS, a systematic method of optimizing the chemical composition of steel bars is needed.

![](./images/812657079587176449_1.jpg)

**FIGURE 1.** Relationship between yield point and tensile strength of steel bars.

### III. TPSO-BASED THREE-LAYER FEEDFORWARD ANN
The process for modeling and optimizing the chemical composition of steel bar (CCSB) can be divided into the modeling process and the optimizing process. In the proposed modeling approach, three-layer feedforward ANN is fused with TPSO to obtain a TPSO-based ANN for modeling and optimizing CCSB. The inputs for the TPSO-based ANN are the ten chemical components of steel bar, and the outputs are YP (kgf/mm²) and TS (kgf/mm²). To account for nonlinear effects, the following equation is used to transform YP and TS to a single value according to the larger-the-better characteristic of $\eta$:

$$
\eta=-10 \log \left(\frac{1}{n} \sum_{t=1}^{n} y_{t}^{2}\right),\qquad(3.1)
$$

where $n$ is the number of output and $y_{t}$ is the $t^{\text {th }}$ output response.

The proposed method uses ANN as the fitness function of TPSO. Each input value is normalized before importation into the training process. If the imported input is $X=(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}, x_{8}, x_{9}, x_{10})$ and the predicted output is $Y=(y_{1}, y_{2})$, the normalization equation is

$$
x_{j}^{\prime}=\frac{x_{j}-\min \left(x_{j}\right)}{\max \left(x_{j}\right)-\min \left(x_{j}\right)},\qquad(3.2)
$$

where $x_{j}^{\prime}$ denotes the value of input $j$ after normalization, $x_{j}$ denotes the value of the original input $j$, $\min(x_{j})$ is the minima of input $j$, and $\max(x_{j})$ is the maxima of input $j$. The normalization process is complete when each input is normalized. The data are then used to evaluate the performance of the TPSO-based ANN. The input-output relationship of the proposed feedforward neural network is

$$
\begin{aligned}
y_{k}^{\prime}(t)= & \sum_{j=1}^{n_{h}} w_{k, j} \delta_{k, j}^{2} \log \operatorname{sig}\left[\sum_{i=1}^{n_{i}} v_{j, i} \delta_{j, i}^{1} x_{i}^{\prime}(t)-b_{j}^{1} \delta_{j}^{1}\right] \\
& -\delta_{k}^{2} \log \operatorname{sig}\left(b_{k}^{2}\right), \quad k=1,2
\end{aligned}\qquad(3.3)
$$

$$
\log \operatorname{sig}(\alpha)=\frac{1}{1+e^{-0.3 \alpha}}, \quad \alpha \in \Re\qquad(3.4)
$$

where $y_{k}^{\prime}(t)$ is the value of output $k$ for variable set $i$, $w_{k,j}$ denotes the weight value between hidden neuron $j$ and output $k$, $\delta_{k,j}^{2}$ denotes the link strength between hidden neuron $j$ and output $k$, $v_{j,i}$ denotes the weight value between input $i$ and hidden neuron $j$, $\delta_{j,i}^{1}$ denotes the link strength between hidden neuron $j$ and input $i$, $x_{i}^{\prime}(t)$ denotes the $i$th input value, $\delta_{j}^{1}$ denotes the link strength between the biases and the hidden neurons, $\delta_{k}^{2}$ denotes the link strength between the biases and the outputs, and $b_{j}^{1}$ and $b_{k}^{2}$ denote the biases for the hidden neurons and outputs, respectively; the $\log \operatorname{sig}(\cdot)$ denotes the logarithmic sigmoid function. The ANN output is $y_{k}^{\prime}(i)$ and is denormalized as follows:

$$
y_{k}=y_{k}^{\prime}(i) \times\left(\max \left(r_{k}\right)-\min \left(r_{k}\right)\right)+\min \left(r_{k}\right), \quad k=1,2
\qquad(3.5)
$$

where $\max(r_{k})$ and $\min(r_{k})$ are the maxima and the minima of output $k$, respectively.

To evaluate the performance of the training network when using training data, the root mean squared error (RMSE) is applied. For each output, the objective of the training process is to minimize RMSE, which can be represented as

$$
J=\left[\sum_{m=1}^{n} \frac{\left(R_{m}-O_{m}\right)^{2}}{n}\right]^{\frac{1}{2}},\qquad(3.6)
$$

where $n$ denotes the number of training data items, $R_{m}$ denotes the actual output value, and $O_{m}$ denotes the predicted output value. Value $J$ is then sent back to the TPSO for use as a fitness value when selecting the weighting set.

Performance criterion $J$ depends on the parameter set $\{w_{1,1}, w_{1,2}, \ldots, w_{m,l}, \hat{w}_{1,1}, \hat{w}_{1,2}, \ldots, \hat{w}_{n,m}\}$, which is

$$
\begin{aligned}
J & =f\left(w_{1,1}, w_{1,2}, \ldots, w_{m, l}, \hat{w}_{1,1}, \hat{w}_{1,2}, \ldots, \hat{w}_{n, m}\right) \\
& =f\left(f_{1} f_{2}, \ldots, f_{\beta}\right),
\end{aligned}\qquad(3.7)
$$

![](./images/812657079587176449_2.jpg)

**FIGURE 2.** Flowchart of the TPSO-based ANN.

where $w_{m,l}$ is the weight value from the $l$th input to the $m^\text{th}$ hidden neuron, and $\hat{w}_{n,m}$ is the weight value from the $m^\text{th}$ hidden neuron to the $n^\text{th}$ output, and $\beta$ is the number of parameters.

The problem considered in this study is
$$\text{Minimize } J = f(f_1,f_2,\dots,f_\beta). \tag{3.8}$$

The optimization process uses TPSO to optimize the solution obtained by the target equation as follows:
$$Y = y_1 + y_2 = \text{maximize } S(x_1,x_2,\dots,x_{10}) \tag{3.9}$$
where $Y$ is the sum of all outputs, and $x_j$ ($j = 1$, $2,\dots,10$) are the inputs. Fig. 2 shows the steps of the TPSO-based ANN.

## IV. RESULTS AND DISCUSSIONS
First, experiments were performed to demonstrate that the proposed TPSO can search for target values. The performance of the TPSO is evaluated in seven test-function problems. The TPSO results are compared with those of seven existing PSO variants in the same initial and terminal condition, including GPSO [29], LPSO [30], FIPS [31], SPSO [32], CLPSO [33], OLPSO [34], and SLPSOA [35].

Second, the TPSO is used to find the best combination of weight values for the CCSB, and its training results are compared with those of the conventional BP. Then, the trained TPSO-based ANN is used to improve the YP and TS of the CCSB by optimizing its ten chemical components.

## A. COMPUTATIONAL RESULTS FOR TPSO USED TO SOLVE NUMERICAL PROBLEMS
Several global numerical functions were used to test the TPSO. As described in the literature [25], [36], the function can be formulated as

$$
\begin{aligned}
&\text { Minimize } f(x), \\
&\text { subject to } l \leq x \leq u,
\end{aligned}\qquad(4.1)
$$

where $x=(x_{1}, x_{2}, ... x_{i}, ..., x_{n})$ is a variable vector in $R^{n}$, $f(x)$ is the objective function, and $[l, u]$ is the feasible solution space with $l=(l_{1}, l_{2}, ... l_{i}, ..., l_{n})$ and $u=(u_{1}, u_{2}, ... u_{i}, ..., u_{n})$.

<table>
<thead>
  <tr>
    <th>Type</th>
    <th>Function Name</th>
    <th>Function Definition</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">Unimodal</td>
    <td>Sphere</td>
    <td>$f_{1}(x)=\sum_{i=1}^{D} x_{i}^{2}$</td>
  </tr>
  <tr>
    <td>Schwefel P2.22</td>
    <td>$f_{2}(x)=\sum_{i=1}^{D}|x_{i}|+\prod_{i=1}^{D}|x_{i}|$</td>
  </tr>
  <tr>
    <td>Noise</td>
    <td>$f_{3}(x)=\sum_{i=1}^{D} i x_{i}^{4}+Rand[0,1)$</td>
  </tr>
  <tr>
    <td>Multimodal</td>
    <td>Schwefel</td>
    <td>$f_{4}(x)=418.9829D-\sum_{i=1}^{D} x_{i} \sin \sqrt{|x_{i}|}$</td>
  </tr>
  <tr>
    <td rowspan="3">Rotated and Shifted</td>
    <td>Rotated Schwefel</td>
    <td>$f_{5}(x)=418.9828D-\sum_{i=1}^{D} z_{i}$ where $z_{i}=egin{cases}y_{i} \sin \sqrt{|y_{i}|}, & \text{if } |y_{i}| \leq 500 \0, & \text{otherwise} \end{cases}$ $y_{i}=y_{i}'+420.96$ where $Y'=M(X-420.96)$, $M$ is an orthogonal matrix</td>
  </tr>
  <tr>
    <td>Rotated Ackley</td>
    <td>$f_{6}(x)=-20 \exp (-0.2 \sqrt{\sum_{i=1}^{D} y_{i}^{2} / D})$ $-\exp (\sum_{i=1}^{D} \cos (2 \pi y_{i}) / D)+20+e$ where $Y=MX$, $M$ is an orthogonal matrix</td>
  </tr>
  <tr>
    <td>Shifted Rosenbrock</td>
    <td>$f_{7}(x)=\sum_{i=1}^{D-1}[100(y_{i} y_{i+1}-y_{i}^{2})^{2}$ $+(y_{i}-1)^{2}]+390$ where $Y=X-O+1$, $O=[o_{1}, o_{2},..., o_{D}]^{T}$ is a constant vector</td>
  </tr>
</tbody>
</table>

Table 1 shows three different function types with definitions of seven test function [35] used for performance evaluation of the TPSO. Functions $f_{1}$-$f_{3}$ are the unimodal function type, which have only one global optimum region and no local region. Unimodal functions are used to compare convergence speed between the TPSO and other PSO variants.

<table>
<thead>
  <tr>
    <th>Function</th>
    <th>$D$</th>
    <th>Search Range</th>
    <th>Optimal Solution</th>
    <th>Optimal Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$f_{1}$</td>
    <td>30</td>
    <td>$[-100,100]^{D}$</td>
    <td>$[0]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{2}$</td>
    <td>30</td>
    <td>$[-10,10]^{D}$</td>
    <td>$[0]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{3}$</td>
    <td>30</td>
    <td>$[-1.28,1.28]^{D}$</td>
    <td>$[0]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{4}$</td>
    <td>30</td>
    <td>$[-500,500]^{D}$</td>
    <td>$[420.96]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{5}$</td>
    <td>30</td>
    <td>$[-500,500]^{D}$</td>
    <td>$[420.96]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{6}$</td>
    <td>30</td>
    <td>$[-32,32]^{D}$</td>
    <td>$[0]^{D}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>$f_{7}$</td>
    <td>30</td>
    <td>$[-100,100]^{D}$</td>
    <td>$O$</td>
    <td>390</td>
  </tr>
</tbody>
</table>

Since seek for high convergence speed must sacrifice diversity in certain iterations. Functions $f_{4}$ is the multimodal function type, which has one global optimum region and many local optima regions; therefore, achieving the global optimum within a certain time limit is difficult. $f_{4}$ is used to test the particle diversity of the algorithm to avoid early convergence of the TPSO in the global search process. Functions $f_{5}-f_{7}$ included rotated functions and shifted functions. Each rotated function is performed by multiplying the former variable vector by a fixed orthogonal matrix, and each shifted function is performed by subtracting a constant vector. These functions are widely used in complex robotic control systems and for image processing. The seven functions are also useful for optimization and for performance comparisons of different methods. For each test function, Table 2 shows the dimension $D=30$, the search range, the optimal solution, and the optimal value. In the experiments, the TPSO was run in Microsoft visual C# 2012 on a Windows 7 PC (core i7-3770, 3.40 GHz CPU) with 12 GB RAM. The performance of the TPSO was compared with eight other PSO variants reported in [35], including GPSO, LPSO, FIPS, SPSO, CLPSO, OLPSO, and SLPSOA. For a fair comparison, each algorithm was executed in 25 independent trials, and the maximum function call $FE_{max}$ was $2 \times 10^{5}$. In all trials, the average value and standard deviation were recorded for each function. The main TPSO parameters were population size $p_{s}$, acceleration coefficients $c_{1}$ and $c_{2}$, terminal condition maximum function call $FE_{max}$, and number of particles for evolutionary mechanisms $n_{G 1}$,

<table>
<thead>
  <tr>
    <th>No.</th>
    <th>Algorithm</th>
    <th>Parameter settings</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>GPSO</td>
    <td>$\omega_{max}=0.9$, $\omega_{min}=0.4$, $c_{1}=c_{2}=2$</td>
  </tr>
  <tr>
    <td>2</td>
    <td>LPSO</td>
    <td>$\omega_{max}=0.9$, $\omega_{min}=0.4$, $c_{1}=c_{2}=2$</td>
  </tr>
  <tr>
    <td>3</td>
    <td>FIPS</td>
    <td>$x=0.729$, $c_{1}=c_{2}=2.05$</td>
  </tr>
  <tr>
    <td>4</td>
    <td>SPSO</td>
    <td>$\omega=0.721$, $c_{1}=c_{2}=1.193$, $k=3$</td>
  </tr>
  <tr>
    <td>5</td>
    <td>CLPSO</td>
    <td>$\omega_{max}=0.9$, $\omega_{min}=0.4$,</td>
  </tr>
  <tr>
    <td>6</td>
    <td>OLPSO</td>
    <td>$\omega_{max}=0.9$, $\omega_{min}=0.4$, $c=1.49445$, $m=7$</td>
  </tr>
  <tr>
    <td>7</td>
    <td>SLPSOA</td>
    <td>$\omega_{max}=0.9$, $\omega_{min}=0.4$, $c=2$, $M=10$, $\alpha=0.1$, $G=5$</td>
  </tr>
  <tr>
    <td>8</td>
    <td>TPSO</td>
    <td>$p_{s}=40$, $c_{1}=c_{2}=1.193$, $n_{G 1}=n_{G 2}=5$, $n_{G 3}=30$, $\delta=0.01$, $\omega_{max}=2$, $\omega_{min}=0$.</td>
  </tr>
</tbody>
</table>

<table><thead><tr><td>Function</td><td>Term</td><td>GPSO</td><td>LPSO</td><td>FIPS</td><td>SPSO</td><td>CLPSO</td><td>OLPSO</td><td>SLPSOA</td><td>TPSO</td></tr></thead><tbody><tr><td rowspan="2">$f_{1}$</td><td>Mean</td><td>$2.05×10^{-32}$</td><td>$3.34×10^{-14}$</td><td>$2.42×10^{-13}$</td><td>$2.29×10^{-96}$</td><td>$1.58×10^{-12}$</td><td>$1.11×10^{-38}$</td><td>$7.30×10^{-38}$</td><td>$5.51×10^{-102}$</td></tr><tr><td>SD</td><td>$3.56×10^{-32}$</td><td>$5.39×10^{-14}$</td><td>$1.73×10^{-13}$</td><td>$9.48×10^{-96}$</td><td>$7.70×10^{-13}$</td><td>$1.28×10^{-38}$</td><td>$8.14×10^{-38}$</td><td>$1.64×10^{-101}$</td></tr><tr><td rowspan="2">$f_{2}$</td><td>Mean</td><td>$1.49×10^{-21}$</td><td>$1.70×10^{-10}$</td><td>$2.76×10^{-8}$</td><td>$1.74×10^{-53}$</td><td>$2.51×10^{-8}$</td><td>$7.67×10^{-22}$</td><td>$0.00$</td><td>$3.10×10^{-62}$</td></tr><tr><td>SD</td><td>$3.60×10^{-21}$</td><td>$1.39×10^{-10}$</td><td>$9.04×10^{-9}$</td><td>$1.58×10^{-53}$</td><td>$5.84×10^{-9}$</td><td>$5.63×10^{-22}$</td><td>$0.00$</td><td>$5.87×10^{-62}$</td></tr><tr><td rowspan="2">$f_{3}$</td><td>Mean</td><td>$9.32×10^{-3}$</td><td>$2.28×10^{-2}$</td><td>$4.24×10^{-3}$</td><td>$4.02×10^{-3}$</td><td>$5.85×10^{-3}$</td><td>$1.64×10^{-2}$</td><td>$3.14×10^{-3}$</td><td>$4.03×10^{-4}$</td></tr><tr><td>SD</td><td>$2.39×10^{-3}$</td><td>$5.60×10^{-3}$</td><td>$1.28×10^{-3}$</td><td>$1.66×10^{-3}$</td><td>$1.11×10^{-3}$</td><td>$3.25×10^{-3}$</td><td>$1.02×10^{-3}$</td><td>$8.47×10^{-4}$</td></tr><tr><td rowspan="2">$f_{4}$</td><td>Mean</td><td>$2.48×10^{3}$</td><td>$3.16×10^{3}$</td><td>$9.93×10^{2}$</td><td>$3.14×10^{3}$</td><td>$3.82×10^{-4}$</td><td>$3.82×10^{-4}$</td><td>$15.4$</td><td>$3.82×10^{-4}$</td></tr><tr><td>SD</td><td>$2.97×10^{2}$</td><td>$4.06×10^{2}$</td><td>$5.09×10^{2}$</td><td>$7.81×10^{2}$</td><td>$1.28×10^{-4}$</td><td>$0$</td><td>$3.58$</td><td>$0$</td></tr><tr><td rowspan="2">$f_{5}$</td><td>Mean</td><td>$4.61×10^{3}$</td><td>$4.50×10^{3}$</td><td>$4.41×10^{3}$</td><td>$4.57×10^{3}$</td><td>$4.39×10^{3}$</td><td>$3.13×10^{-3}$</td><td>$2.72×10^{3}$</td><td>$3.86×10^{-4}$</td></tr><tr><td>SD</td><td>$6.21×10^{2}$</td><td>$3.97×10^{2}$</td><td>$9.94×10^{2}$</td><td>$6.28×10^{2}$</td><td>$3.51×10^{2}$</td><td>$1.24×10^{-3}$</td><td>$5.95×10^{2}$</td><td>$7.28×10^{-6}$</td></tr><tr><td rowspan="2">$f_{6}$</td><td>Mean</td><td>$1.93$</td><td>$1.55$</td><td>$3.16×10^{-7}$</td><td>$9.24×10^{-2}$</td><td>$5.91×10^{-5}$</td><td>$4.28×10^{-15}$</td><td>$2.07×10^{-14}$</td><td>$4.71×10^{-15}$</td></tr><tr><td>SD</td><td>$0.96$</td><td>$0.45$</td><td>$1.00×10^{-7}$</td><td>$0.32$</td><td>$6.46×10^{-5}$</td><td>$7.11×10^{-16}$</td><td>$6.68×10^{-15}$</td><td>$2.13×10^{-15}$</td></tr><tr><td rowspan="2">$f_{7}$</td><td>Mean</td><td>$427.93$</td><td>$432.33$</td><td>$424.83$</td><td>$424.28$</td><td>$403.07$</td><td>$415.94$</td><td>$401.82$</td><td>$397.38$</td></tr><tr><td>SD</td><td>$54.98$</td><td>$43.41$</td><td>$25.37$</td><td>$48.94$</td><td>$13.50$</td><td>$23.96$</td><td>$16.65$</td><td>$5.27$</td></tr></tbody></table>

$n_{G2}$, and $n_{G3}$. In the experimental stage for each test function, population size $p_s$ was 40; acceleration coefficients $c_1$ and $c_2$ were both 1.193; weight values $\omega_{max}$ and $\omega_{min}$ were both 0; $n_{G1}, n_{G2}$, and $n_{G3}$ were 5, 5, and 30, respectively; and random movement rate $\delta$ was 0.01. For comparison, Table 3 shows the detailed parameter settings for each algorithm.

Table 4 compares the mean values and standard deviations obtained by each algorithm in each function. Table 4 shows that, for most test functions, the mean solutions found by the proposed TPSO were better and had smaller standard deviations compared to those found by other PSO-based algorithms. The TPSO also obtains far smaller deviations in all functions. The experimental results show that the TPSO superior to all other PSO-based algorithms in terms of falling into local optima and in terms of the depth of the solution area.

### B. OPTIMIZATION OF CCSB MODEL

In the experiment, 1000 feasible sets of data were given from the Metal industries Research and Development Centre (MIRDC, http://www.mirdc.org.tw), where 800 feasible sets of data were used for training the TPSO-based ANN model, and 200 feasible sets of data were used for testing the performance of the model. First, the inputs and outputs of training data and test data were normalized according to Eq. (3.2). The input parameters for the CCSB were C (%), Si (%), Mn (%), P (%), S (%), Cu (%), Ni (%), Cr (%), Mo (%), and V (%). Fig. 3 shows that the TPSO-based architecture had ten inputs, five hidden neurons, and two outputs. Table 5 shows the maximum and the minimum input values used for normalization of the training data and the test data. The YP and TS were used as indices of steel bar quality in the performance evaluations. The model required fifty weight values between inputs and hidden neurons, ten weight values between hidden neurons and outputs, five biases for hidden neurons, and two biases for outputs. Each variable had sixty-seven links. The TPSO was used to adjust weight settings during ANN model training. Table 6 shows the parameter settings for TPSO. The $P_s$ was set to 100 for each population. The $c_1$ and $c_2$ were both set to value 1.193.

<table><thead><tr><td rowspan="2">Parameters</td><td colspan="2">Range</td></tr><tr><td>Min.</td><td>Max.</td></tr></thead><tbody><tr><td>C (%)</td><td>0.1903</td><td>0.2478</td></tr><tr><td>Si (%)</td><td>0.0509</td><td>0.1995</td></tr><tr><td>Mn (%)</td><td>0.6000</td><td>0.7975</td></tr><tr><td>P (%)</td><td>0.0165</td><td>0.0488</td></tr><tr><td>S (%)</td><td>0.0700</td><td>0.0484</td></tr><tr><td>Cu (%)</td><td>0.1699</td><td>0.4486</td></tr><tr><td>Ni (%)</td><td>0.0584</td><td>0.1496</td></tr><tr><td>Cr (%)</td><td>0.0842</td><td>0.2454</td></tr><tr><td>Mo (%)</td><td>0.0118</td><td>00587</td></tr><tr><td>V (%)</td><td>0.0030</td><td>0.0078</td></tr></tbody></table>

<table><thead><tr><td>Parameters</td><td>Value</td></tr></thead><tbody><tr><td>$P_{s}$</td><td>100</td></tr><tr><td>$C_{1}$</td><td>1.193</td></tr><tr><td>$C_{2}$</td><td>1.193</td></tr><tr><td>$n_{G1}$</td><td>10</td></tr><tr><td>$n_{G2}$</td><td>10</td></tr><tr><td>$n_{G3}$</td><td>80</td></tr><tr><td>δ</td><td>0.01</td></tr><tr><td>$ω_{max}$</td><td>2</td></tr><tr><td>$ω_{min}$</td><td>2</td></tr><tr><td>G</td><td>1000</td></tr></tbody></table>

The $n_{G1}$ was set to 10, $n_{G2}$ was set to 10, and $n_{G3}$ was set to 80. The $\delta$ was set to 0.01. The $\omega_{max}$ and $\omega_{min}$ were set to 2 and 0, respectively. The terminal iteration number $g_{max}$ was set to 1000. Table 7 compares the conventional BP and proposed TPSO-based ANN models of the chemical composition of steel bar in terms of average RMSE for training data and test data. The table shows that, in both datasets, the TPSO-based ANN outperforms the conventional BP in terms of YP and TS.

Finally, the TPSO was used to optimize the ten inputs (chemical components) for the CCSB model. Table 8 shows

![](./images/812657079587176449_3.jpg)

FIGURE 3. Ten inputs, five hidden neurons, and two outputs in proposed ANN model of chemical composition of steel bar.

<table>
<thead>
<tr>
<th rowspan="2">Method</th>
<th colspan="4">RMSE</th>
</tr>
<tr>
<th colspan="2">Training data set</th>
<th colspan="2">Test data set</th>
</tr>
<tr>
<th></th>
<th>TS</th>
<th>YP</th>
<th>TS</th>
<th>YP</th>
</tr>
</thead>
<tbody>
<tr>
<td>Conventional BP</td>
<td>1.5400</td>
<td>1.4000</td>
<td>2.2551</td>
<td>1.8305</td>
</tr>
<tr>
<td>TPSO-based ANN</td>
<td>1.3700</td>
<td>1.2400</td>
<td>2.0851</td>
<td>1.6630</td>
</tr>
</tbody>
</table>

TABLE 7. The RMSE values for CCSB models obtained by conventional BP and by TPSO-based ANN.

that the predicted and actual chemical compositions and the experimental results for YP and TS were all superior to those in the existing training and test data sets. The experiments were performed in the MIRDC. The experimental results for the first set were $C = 0.2221$ (%), $Si = 0.1113$ (%),
$Mn = 0.6230$ (%), $P = 0.0485$ (%), $S = 0.0329$ (%),
$Cu = 0.2845$ (%), $Ni = 0.0744$ (%), $Cr = 0.1216$ (%),
$Mo = 0.0155$ (%), $V = 0.0049$ (%), $YP = 70.2$ (kgf/mm2),
and $TS = 79.1$ (kgf/mm²). The experimental results for
the second set were $C = 0.2072$ (%), $Si = 0.1486$ (%),
$Mn = 0.6845$ (%), $P = 0.0332$ (%), $S = 0.0308$ (%),
$Cu = 0.2885$ (%), $Ni = 0.0715$ (%), $Cr = 0.1209$ (%),
$Mo = 0.0160$ (%), $V = 0.0046$ (%), $YP = 69.5$ (kgf/mm²),
and $TS = 78.6$ (kgf/mm²). In the first set, the errors in the pre-
dicted and actual values TS and YP were 4.27% and 4.17%,
respectively. In the second set, the respective errors were
3.88% and 2.54%. Before applying the chemical composi-
tion, each factor value was compared with CNS560. The first
and second sets obtained by Eq. (2.1) had CEs of 0.3482 and
0.3434, respectively. The chemical composition of the steel

<table>
<caption>TABLE 8. Predicted CCSB inputs and outputs.</caption>
<thead>
<tr>
<th rowspan="2">Experiment No.</th>
<th colspan="10">Inputs</th>
<th colspan="2">Outputs</th>
</tr>
<tr>
<th>C (%)</th>
<th>Si (%)</th>
<th>Mn (%)</th>
<th>P (%)</th>
<th>S (%)</th>
<th rowspan="2">TS (kgf/mm²)</th>
<th rowspan="2">YP (kgf/mm²)</th>
</tr>
<tr>
<th>Cu (%)</th>
<th>Ni (%)</th>
<th>Cr (%)</th>
<th>Mo (%)</th>
<th>V (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Predict 1</td>
<td>0.2221</td>
<td>0.1113</td>
<td>0.6230</td>
<td>0.0485</td>
<td>0.0329</td>
<td rowspan="2">73.2</td>
<td rowspan="2">82.4</td>
</tr>
<tr>
<td>0.2845</td>
<td>0.0744</td>
<td>0.1216</td>
<td>0.0155</td>
<td>0.0049</td>
</tr>
<tr>
<td rowspan="2">Actual 1</td>
<td>0.2221</td>
<td>0.1113</td>
<td>0.6230</td>
<td>0.0485</td>
<td>0.0329</td>
<td rowspan="2">70.2</td>
<td rowspan="2">79.1</td>
</tr>
<tr>
<td>0.2845</td>
<td>0.0744</td>
<td>0.1216</td>
<td>0.0155</td>
<td>0.0049</td>
</tr>
<tr>
<td>Error (%)</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>4.27%</td>
<td>4.17%</td>
</tr>
<tr>
<td rowspan="2">Predict 2</td>
<td>0.2072</td>
<td>0.1486</td>
<td>0.6845</td>
<td>0.0332</td>
<td>0.0308</td>
<td rowspan="2">72.2</td>
<td rowspan="2">80.5</td>
</tr>
<tr>
<td>0.2885</td>
<td>0.0715</td>
<td>0.1209</td>
<td>0.0160</td>
<td>0.0046</td>
</tr>
<tr>
<td rowspan="2">Actual 2</td>
<td>0.2072</td>
<td>0.1486</td>
<td>0.6845</td>
<td>0.0332</td>
<td>0.0308</td>
<td rowspan="2">69.5</td>
<td rowspan="2">78.6</td>
</tr>
<tr>
<td>0.2885</td>
<td>0.0715</td>
<td>0.1209</td>
<td>0.0160</td>
<td>0.0046</td>
</tr>
<tr>
<td>Error (%)</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>0%</td>
<td>3.88%</td>
<td>2.54%</td>
</tr>
</tbody>
</table>

bars in the first set was superior to that in the second set in terms of both YP and TS. However, P was 0.0485 (%), which exceeded the 0.045 (%) stipulated by CNS560. That is, even though the YP and TS were better in the first set than in the second set, the chemical composition of the first set is still forbidden in the Taiwan steel bar industry. In addition the experimental results show that the YP ($69.5\ \text{kgf/mm}^2$) and TS ($78.6\ \text{kgf/mm}^2$) obtained by the TPSO are better than those obtained by previous designs for existing experimental datasets obtained from the MIRDC. Therefore, the second set is the best chemical composition obtained by the proposed method.

## V. CONCLUSIONS
The proposed TPSO successfully optimized the weight value set in the three-layer feedforward ANN model of CCSB. The important chemical elements of CCSB were C (%), Si (%), Mn (%), P (%), S (%), Cu (%), Ni (%), Cr (%), Mo (%), and V (%). The two output responses used for quality assessments of steel bar were YP and TS. To achieve highly robust results, the proposed TPSO method generated more competitive offspring by combining the advantages of Taguchi combination, random movement, and conventional nonlinear PSO. In the proposed Taguchi combination, OA is used to generate potential offspring during the evolution process, and random movement is used to avoid local optima. The fast convergence and nonlinear evolution of conventional nonlinear PSO is used to explore and exploit the better solutions. To obtain better outputs, the TPSO is again used to optimize inputs in the TPSO-based ANN. The experimental results show that the YP ($69.5\ \text{kgf/mm}^2$) and TS ($78.6\ \text{kgf/mm}^2$) obtained by the TPSO are better than those obtained by previous designs for existing experimental datasets obtained from the MIRDC. Therefore, we conclude that, for solving a problem such as CCSB optimization, the proposed TPSO-based ANN is a highly accurate and useful engineering tool.

## REFERENCES
[1] M. Awais, H. W. Lee, Y. T. Ima, H. C. Kwon, S. M. Byonc, and H. D. Park, "Plastic work approach for surface defect prediction in the hot bar rolling process," J. Mater. Process. Technol., vol. 201, pp. 73-78, May 2008.

[2] H.-C. Kwon, H.-W. Lee, H.-Y. Kim, Y.-T. Im, H.-D. Park, and D.-L. Lee, "Surface wrinkle defect of carbon steel in the hot bar rolling process," J. Mater. Process. Technol., vol. 209, no. 9, pp. 4476-4483, 2009.

[3] J. L. Calvo-Rolle, J. L. Casteleiro-Roca, H. Quintián, and M. del Carmen Meizoso-Lopez, "A hybrid intelligent system for PID controller using in a steel rolling process," Expert Syst. Appl., vol. 40, no. 13, pp. 5188-5196, 2013.

[4] F.-J. Wang, Y.-H. Shuang, J.-H. Hu, Q.-H. Wang, and J.-C. Sun, "Explorative study of tandem skew rolling process for producing seamless steel tubes," J. Mater. Process. Technol., vol. 214, no. 8, pp. 1597-1604, 2014.

[5] J. Perenda, J. Trajkovski, A. Žerovnik, and I. Prebil, "Residual stresses after deep rolling of a torsion bar made from high strength steel," J. Mater. Process. Technol., vol. 218, pp. 89-98, Apr. 2015.

[6] Y. Peng, H. Liu, and R. Du, "A neural network-based shape control system for cold rolling operations," J. Mater. Process. Technol., vol. 202, pp. 54-60, Jun. 2008.

[7] J. A. Abdalla and R. Hawileh, "Modeling and simulation of low-cycle fatigue life of steel reinforcing bars using artificial neural network," J. Franklin Inst., vol. 348, no. 7, pp. 1393-1403, 2011.

[8] J. Ghaisari, H. Jannesari, and M. Vatani, "Artificial neural network predictors for mechanical properties of cold rolling products," Adv. Eng. Softw., vol. 45, no. 1, pp. 91-99, 2012.

[9] E. M. Golafshani, A. Rahai, M. H. Sebt, and H. Akbarpour, "Prediction of bond strength of spliced steel bars in concrete using artificial neural network and fuzzy logic," Construct. Building Mater., vol. 36, pp. 411-418, Nov. 2012.

[10] M. Bagheripoor and H. Bisadi, "Application of artificial neural networks for the prediction of roll force and roll torque in hot strip rolling process," Appl. Math. Model., vol. 37, no. 7, pp. 4593-4607, 2013.

[11] S. Taghizadeh, A. Safarian, S. Jalali, and A. Salimiasl, "Developing a model for hardness prediction in water-quenched and tempered AISI 1045 steel through an artificial neural network," Mater. Design, vol. 51, pp. 530-535, Oct. 2013.

[12] M. Katoh, K. Nishio, and T. Yamaguchi, "Materials evaluation of diffusion bonded steel bar and its impact characteristics," NDT E Int., vol. 35, no. 4, pp. 263-271, 2002.

[13] J. J. González, J. Setién, J. A. Álvarez, J. A. Polanco, and D. O. Ferreño, "Failure of reinforcing concrete steel ribbed bars," Eng. Failure Anal., vol. 13, no. 8, pp. 1376-1387, 2006.

[14] C. A. Apostolopoulos and M. P. Papadopoulos, "Tensile and low cycle fatigue behavior of corroded reinforcing steel bars S400," Construct. Building Mater., vol. 21, no. 4, pp. 855-864, 2007.

[15] K. G. Rakvåg, B. T. Børvik, and O. S. Hopperstad, "A numerical study on the deformation and fracture modes of steel projectiles during Taylor bar impact tests," Int. J. Solids Struct., vol. 51, pp. 808-821, Feb. 2014.

[16] C.-K. Cheng, J.-T. Tsai, T.-T. Lee, J.-H. Chou, and K.-S. Hwang, "Modeling and optimizing tensile strength and yield point on steel bar by artificial neural network with evolutionary algorithm," Proc. 11th IEEE Int. Conf. Autom. Sci. Eng., Gothenburg, Sweden, Aug. 2015, pp. 1562-1563.

[17] E. Cadoni, L. Fenu, and D. Forni, "Strain rate behaviour in tension of austenitic stainless steel used for reinforcing bars," Construct. Building Mater., vol. 35, pp. 399-407, Oct. 2012.

[18] K. Sato, Q. Yu, J. Hiramoto, T. Urabe, and A. Yoshitake, "A method to investigate strain rate effects on necking and fracture behaviors of advanced high-strength steels using digital imaging strain analysis," Int. J. Impact Eng., vol. 75, pp. 11-26, Jan. 2015.

[19] Y.-L. Li, W. Shao, L. You, and B.-Z. Wang, "An improved PSO algorithm and its application to UWB antenna design," IEEE Antennas Wireless Propag. Lett., vol. 12, pp. 1236-1239, Oct. 2013.

[20] T.-H. S. Li, Y.-H. Wang, C.-C. Chen, and C.-J. Lin, "A fast color information setup using EP-like PSO for manipulator grasping color objects," IEEE Trans. Ind. Informat., vol. 10, no. 1, pp. 645-654, Feb. 2014.

[21] M. Veerachary and A. R. Saxena, "Optimized power stage design of low source current ripple fourth-order boost DC-DC converter: A PSO approach," IEEE Trans. Ind. Electron., vol. 62, no. 3, pp. 1491-1502, Mar. 2015.

[22] O. Sandre-Hernandez, R. Morales-Caporal, J. Rangel-Magdaleno, H. Peregrina-Barreto, and J. N. Hernandez-Perez, "Parameter identification of PMSMs using experimental measurements and a PSO algorithm," IEEE Trans. Instrum. Meas., vol. 64, no. 8, pp. 2146-2154, Aug. 2015.

[23] E. H. M. Silva and C. J. A. B. Filho, "PSO efficient implementation on GPUs using low latency memory," IEEE Latin Amer. Trans., vol. 13, no. 5, pp. 1619-1624, May 2015.

[24] G. Taguchi, Systems of Experimental Design. White Plains, NY, USA: Unipub/Kraus Int. Pub., 1987.

[25] J.-T. Tsai, T.-K. Liu, and J.-H. Chou, "Hybrid Taguchi-genetic algorithm for global numerical optimization," IEEE Trans. Evol. Comput., vol. 8, no. 4, pp. 365-377, Aug. 2004.

[26] CNS560. (Sep. 2015). Steel Deformed and Plain Bars for Concrete Reinforcement. [Online]. Available: http://www.cnsonline.com.tw/?node=result&generalno=560&locale=zh_TW

[27] J. A. Rinebolt and W. J. Harris, "Effect of alloying elements on notch toughness of pearlitic steels," Trans. Amer. Soc. Met., vol. 43, pp. 1175-1214, 1951.

[28] TOMTMC. (2015). Interpretation of Stress-Strain Curves and MechanicalProperties of Materials. [Online]. Available: http://www.tiniusolsen.com/pdf/Pamphlet4.pdf

[29] Y. Shi and R. C. Eberhart, "A modified particle swarm optimizer," in Proc. IEEE Int. Conf. Evol. Comput., Anchorage, AK, USA, May 1998, pp. 69-73.

[30] J. Kennedy and R. Mendes, "Population structure and particle swarm performance," in Proc. Congr. Evol. Comput., Honolulu, HI, USA, 2002, pp. 1671-1676.

[31] R. Mendes, J. Kennedy, and J. Neves, "The fully informed particle swarm: Simpler, maybe better," IEEE Trans. Evol. Comput., vol. 8, no. 3, pp. 204-210, Jun. 2004.

[32] D. Bratton and J. Kennedy, "Defining a standard for particle swarm optimization," in Proc. IEEE Swarm Intell. Symp., Apr. 2007, pp. 120-127.

[33] J. J. Liang, A. K. Qin, P. N. Suganthan, and S. Baskar, "Comprehensive learning particle swarm optimizer for global optimization of multimodal functions," IEEE Trans. Evol. Comput., vol. 10, no. 3, pp. 281-295, Jun. 2006.

[34] Z.-H. Zhan, J. Zhang, Y. Li, and Y. H.-Shi, "Orthogonal learning particle swarm optimization," IEEE Trans. Evol. Comput., vol. 15, no. 6, pp. 832-847, Dec. 2011.

[35] Z. Ren, A. Zhang, C. Wen, and Z. Feng, "A scatter learning particle swarm optimization algorithm for multimodal problems," IEEE Trans. Cybern., vol. 44, no. 7, pp. 1127-1140, Jul. 2014.

[36] Z. Ren, A. Zhang, C. Wen, and Z. Feng, "A scatter learning particle swarm optimization algorithm for multimodal problems," IEEE Trans. Cybern., vol. 44, no. 7, pp. 1127-1140, Jul. 2014.

![](./images/812657079587176449_4.jpg)

PING-YI CHOU received the B.S. and M.S. degrees in computer science from the National Pingtung University of Education, Taiwan, in 2010 and 2012, respectively. He is currently pursuing the Ph.D. degree in engineering science and technology with the National Kaohsiung First University of Science and Technology, Kaohsiung, Taiwan. He is an Engineer with the Automation Control Section, Metal Industries Research and Development Center, Taiwan. His research interests include evolutionary algorithms, cloud computing, image processing, neural networks, data analysis, and quality engineering.

![](./images/812657079587176449_5.jpg)

JINN-TSONG TSAI received the B.S. and M.S. degrees in mechanical and electromechanical engineering from National Sun Yat-sen University, Taiwan, in 1986 and 1988, respectively, and the Ph.D. degree in engineering science and technology from the National Kaohsiung First University of Science and Technology, Taiwan, in 2004.

He was a Lecturer with the Vehicle Engineering Department, Chung Cheng Institute of Technology, Taiwan, from 1988 to 1990. From 1990 to 2004, he was a Researcher and the Chief of the Automation Control Section with the Metal Industries Research and Development Center, Taiwan. From 2004 to 2006, he was an Assistant Professor with the Medical Information Management Department, Kaohsiung Medical University, Kaohsiung, Taiwan. From 2006 to 2014, he was an Assistant and Associate Professor with the Department of Computer Science, National Pingtung University, Pingtung, Taiwan, where he is currently a Professor with the Department of Computer Science. His research interests include evolutionary computation, intelligent control and systems, neural networks, and quality engineering.

![](./images/812657079587176449_6.jpg)

JYH-HORNG CHOU (SM'04-F'15) received the B.S. and M.S. degrees in engineering science from National Cheng Kung University, Tainan, Taiwan, in 1981 and 1983, respectively, and the Ph.D. degree in mechatronic engineering from National Sun Yat-sen University, Kaohsiung, Taiwan, in 1988. He is currently the Chair Professor with the Electrical Engineering Department, National Kaohsiung University of Applied Sciences, Taiwan. He has co-authored four books, and published over 270 refereed journal papers. He also holds six patents. His research and teaching interests include intelligent systems and control, computational intelligence and methods, automation technology, robust control, and robust optimization. He is also a fellow of the Institution of Engineering and Technology, the Chinese Automatic Control Society, the Chinese Institute of Automation Engineer, and the Chinese Society of Mechanical Engineers. He was a recipient of the 2011 Distinguished Research Award from the National Science Council of Taiwan, the 2012 IEEE Outstanding Technical Achievement Award from the IEEE Tainan Section, the 2014 Distinguished Research Award from the Ministry of Science and Technology of Taiwan, the Research Award and the Excellent Research Award from the National Science Council of Taiwan 12 times, and numerous academic awards/honors from various societies. Based on the IEEE Computational Intelligence Society (IEEE CIS) evaluation, his Industrial Application Success Story received the 2014 Winner of Highest Rank, thus being selected to become the first internationally industrial success story being reported on the IEEE CIS website.
…