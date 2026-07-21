**ORIGINAL ARTICLE**

K.S. Lee · J.C. Lin

# Design of the runner and gating system parameters
for a multi-cavity injection mould using FEM and neural network

Received: 15 March 2004 / Accepted: 7 June 2004 / Published online: 2 March 2005
© Springer-Verlag London Limited 2005

**Abstract** The design of the runner and gating systems is of great importance to achieving a successful injection moulding process. The subjects of this study are the finite element and abductive neural network methods applied to the analysis of a multi-cavity injection mould. In order to select the optimal runner system parameters to minimize the warp of an injection mould, FEM, Taguchi’s method and an abductive network are used. These methods are applied to train the abductive neural network. Once the runner and gate system parameters are developed, this network can be used to accurately predict the warp of the multi-injection mould. A simulated annealing (SA) optimization algorithm with a performance index is then applied to the neural network in order to search the gate and runner system parameters. This method obtains a satisfactory result as compared with the corresponding finite element verification.

**Keywords** Abductive neural network · Multi-cavity ·
Simulated annealing

---

## 1 Introduction

Injection moulding is one of the most important industrial processes in industry, owing to a high manufacturing rate, shorter product cycle, low percentage of scrap, excellent product surface and easy moulding of complicated shapes. In the production process, molten polymer is injected under high velocity into the mould cavity. The constant demand for higher quality leads to interest in the analysis of the product’s physical properties.

The main function of runner and gating systems is to deliver molten metal passed into the mould through all sections of the mould cavities. Poor gating designs can lead to defects such as gas porosity, shrinkage porosity, flow line cold shut, and poor surface quality. With a proper runner and gating system design, one may control the filling pattern (e.g. weld-line location), preventing over-packing, diminish the incidence of faulty moulded parts and increase productivity. Optimization of mould filling patterns through improvement of runner and gating system design, therefore, is very important.

In the past, the runner and gating system of an injection mould with a multi-cavity was typically designed by trial and error until the multi-cavity was filled properly without short-shot or other defects. To reduce cost and time at the design stage, it is important to simulate shrinkage of the injection-moulded part that contained residual stress. In this study, an integrated simulation program and neural network for the prediction of the shrinkage in a runner-system design was developed as a part of computer-aided engineering of injection moulding.

### 1.1 Literature review

Recently, research on runner and gating systems has included a growing number of papers on optimization algorithms, the focus being to generate routines to assist the designer in the work of mould and part design. Li [1] presented a feasible way to optimize the runner design automatically by integrating optimization theory with a flow/thermo-simulation program. Shamsuddin [2] used network and FORTRAN to simulate a runner and gating system with four gates. The angles of branches leading to the gate and mould cavities were from 40 to 90 °. A numerical simulation technique was applied for optimization of the runner and gating system by Hu [3]. Optimal injection gate locations were studied by Lin [4] who defined the optimum location with a quality function consisting of temperature difference, over-pack and frictional heating terms. Jong and Wang [5] described the optimal design of a runner system based on flow simulation.

The abductive neural network analysis method is used for simulation, with the aid of a program written in C-language. It

---

K.S. Lee (⊗)
Department of Mechanical Engineering,
Chien Kuo Institute of Technology,
Changhua, Taiwan 500, R.O.C.
E-mail: kingsun@ckit.edu.tw
Tel.: +886-4-7111111
Fax: +886-4-7111137

J.C. Lin
Department of Mechanical Design Engineering,
National Huwei University of Science & Technology,
Huwei, Taiwan 632, R.O.C.

has been shown that prediction accuracy in a abductive networks is much higher than that in a traditional network [6]. Abductive neural analysis based on the abductive modelling technique is able to represent complex and uncertain relationships between injection analysis results and runner and gating systems design. It shows that the warp and runner, and gating system parameters can be predicted with reasonable accuracy based on the developed network.

### 1.2 Studied designs and simulation steps

The purpose of this study is the use of CAD/CAE software to systematically simulate the design process of injection moulding and to derive an optimal set of gate and runner systems parameters for an injection process. This simulation begins by using CAD software (i.e. Pro/Engineer) to create an injection-parts model. Next, the finite element package (i.e. Moldflow/MPI Version 3.1 [7] system) was used to analyze the conditions of injection processing for multi-injection moulds.

This study used a FEM and abductive network to establish the parameter relationship of runner and gating system parameters in order to find the relationship equation. It provides a simulation based on theory for the development and application of the technologies.

After the FEM simulation, the abductive network formulation is used to establish the relationship between warpage and the gate-runner system parameter models. By using the abductive modelling technique, the complicated and uncertain relationships between the input and output variables can be formulated into a useful mathematical model. For the later derivation, this model will be treated as a black box to represent the process of injection moulding, with adjustable parameters to manipulate overall performance of the model.

Once the abductive network model has been constructed, the relationships between input and output gate-runner parameters variables become obvious. To optimize this process of searching for the best parameters, an algorithm with a performance index is set up. At this stage, an optimization method called simulated annealing [8] was adopted. The simulated annealing algorithm is analogous to the material annealing process for minimizing the performance index.

## 2 Problem formulations

### 2.1 Injection mould-flow process:

The major mould flow equations are divided into three portions as follows:
(A) During the filling stage, the mould cavity is filled with molten plastic fluid under high pressure. Thus, the governing equation includes:
1.  The continuity equation, plastic deformation or shape change accompanying the flow during the filling process, but the mass is conserved.
2.  The momentum equation, Newton's second law deriving the momentum (acceleration condition) or force balance generated by plastic flow.
3.  The energy equation, which is the energy conservation of the system and laws of conservation of the flow material, if it is an incompressible fluid.
(B) Holding pressure analysis. The holding pressure process is to hold the pressure after the mould cavity is filled in order to inject more plastic to compensate for the shrinkage in cooling.
(C) Cooling and warp analysis. The analysis of the cooling process is to discuss the relationship of the plastic flow distribution and heat transmission.

The homogenous mould temperature and filling sequence follow the optimization of the runner-system and gating design, and will be affected by product shrinkage. If the flow paths are unbalanced, or temperature distributions are distributed non-uniformly, there is a tendency for warping to occur.

### 2.2 Simulation parameters and Taguchi's method

After the FEM model is formulated, an abductive network structure needs to be determined by using the results of the Moldflow/MPI system. At this stage, a validation data set is applied to assist in configuration of the network. This will ensure the network is properly trained to avoid the over training or insufficient training due to improper topology of the data set.

In order to provide a proper data set to train the associated abductive network model, Taguchi's method is used. Taguchi's method combines engineering and statistics to provide improvements in both cost and quality. It is a well-known method to optimize process and product design development. Unlike traditional quality control, where the goal is to eliminate the causes of variation, Taguchi's method is based upon the concept that a better way to improve quality is by systematically reducing the number of factorial simulations. In this study, the parameters were balanced against each other to provide an "optimum" where both process and product occur at an acceptable level.

The objective of this study is to determine the optimum gate and runner system setting at which to minimize warp. Several parameters were selected for simulation, such as: (1) mould cavity, (2) volume of injection part, (3) gate diameter and (4) runner diameter, the sprue diameter is equal to the runner diameter as shown in Fig. 1. An $L_{27}^{3}$ orthogonal array was selected for the simulation (Table 1, Table 2). For each of the 27 trials, quality characteristics were generated.

### 2.3 Abductive network synthesis and evaluation

Neural networks, as a class of model, have attracted much attention in process engineering during the last decade, due to their ability to create complex processes, and their fast executing and re-training capacities. In an abductive network, a complex system can be decomposed into smaller, simpler subsystems grouped into several layers using polynomial function nodes. The polynomial network proposed by Ivakhnenko [9] is a group

![](./images/812297196727697408_1.jpg)

Fig. 1. Runner-system parameter

method of data handling (GMDH) techniques. These nodes eval- uate the limited number of inputs by a polynomial function and generate an output to serve as an input to the subsequent nodes of the next layer. The general polynomial function in a polynomial functional node can be expressed as follows:

$$
\begin{aligned}
y_{0}= & B_{0}+\sum_{i=1}^{n} B_{i} x_{i}+\sum_{i=1}^{n} \sum_{j=1}^{n} B_{i j} x_{i} x_{j} \\
& +\sum_{i=1}^{n} \sum_{j=1}^{n} \sum_{k=1}^{n} B_{i j k} x_{i} x_{j} x_{k}+\cdots \cdots.
\end{aligned}
\tag{1}
$$

Where $x_{i}, x_{j}, x_{k}$ are the inputs, $y_{0}$ is the output, and $B_{0}, B_{i}, B_{i j}$, $B_{i j k}$ are the coefficients of the polynomial functional node.

In this paper, several specific types of polynomial function nodes are used for predicting warp in the different kinds of runner and gate systems. These polynomial function nodes are called normalizer (N), unitizer (U), white (W), singles (S), dou- bles (D) and triples (T) nodes. They are explained as follows:

$$
\begin{aligned}
O= & \mathrm{u}_{0}+\left(\mathrm{u}_{1} \mathrm{i}_{1}+\mathrm{u}_{2} \mathrm{i}_{1}^{2}+\mathrm{u}_{3} \mathrm{i}_{1}^{3}\right)+\left(\mathrm{u}_{4} \mathrm{i}_{2}+\mathrm{u}_{5} \mathrm{i}_{2}^{2}+\mathrm{u}_{6} \mathrm{i}_{2}^{3}\right) \\
& +\left(\mathrm{u}_{7} \mathrm{i}_{3}+\mathrm{u}_{8} \mathrm{i}_{3}^{2}+\mathrm{u}_{9} \mathrm{i}_{3}^{3}\right) \\
& +\mathrm{u}_{10} \mathrm{i}_{1} \mathrm{i}_{2}+\mathrm{u}_{11} \mathrm{i}_{2} \mathrm{i}_{3}+\mathrm{u}_{12} \mathrm{i}_{1} \mathrm{i}_{3}+\mathrm{u}_{13} \mathrm{i}_{1} \mathrm{i}_{2} \mathrm{i}_{3}+\ldots.
\end{aligned}
\tag{2}
$$

These nodes are maximum third-degree polynomial equations and doubles and triples have cross-terms (triple node), allow- ing interaction among the node input variables. Where $\mathrm{i}_{1}, \mathrm{i}_{2}, \mathrm{i}_{3}$ are the input parameters of the previous layer, O is the output of the node, and $\mathrm{u}_{0}, \mathrm{u}_{1}, \mathrm{u}_{2}, \mathrm{u}_{3} \ldots \mathrm{u}_{n}$ are the coefficients of the single, double, triple and white nodes. A single node is an equa- tion that has only one input parameter and one output parameter $(\mathrm{i}_{1} \neq 0, \mathrm{i}_{2}=\mathrm{i}_{3}=0)$. A double node is an equation that has two input parameters and one output parameter $(\mathrm{i}_{1}, \mathrm{i}_{2} \neq 0, \mathrm{i}_{3}=0)$. A triple node is an equation that has three input parameters and one output parameter $(\mathrm{i}_{1}, \mathrm{i}_{2}, \mathrm{i}_{3} \neq 0)$. A white node is an equation

<table>
<caption>Table 1. The three levels of factors in the orthogonal array</caption>
<thead>
<tr>
<th>Selected factors</th>
<th>Level 1</th>
<th>Level 2</th>
<th>Level 3</th>
</tr>
</thead>
<tbody>
<tr>
<td>A. Mould cavity (N)</td>
<td>1</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td>B. Injection part volume(V)</td>
<td>$10^{L}$x$10^{W}$x$10^{H}$x$1^{l}$mm</td>
<td>$20^{L}$x$20^{W}$x$20^{H}$x$1^{l}$mm</td>
<td>$30^{L}$x$30^{W}$x$30^{H}$x$1^{l}$mm</td>
</tr>
<tr>
<td>C. Runner diameter ($R_{D}$)</td>
<td>$2.1^{D}$X$50^{L}$mm</td>
<td>$3^{D}$mmX$50^{L}$mm</td>
<td>$3.9^{D}$mmX$50^{L}$mm</td>
</tr>
<tr>
<td>D. Gate diameter ($G_{D}$)</td>
<td>$0.98^{D}$mmX$0.5^{L}$mm</td>
<td>$1.4^{D}$mmX$0.5^{L}$mm</td>
<td>$1.82^{D}$mmX$0.5^{L}$mm</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2. The levels of mould flow simulation gate-runner system design data</caption>
<thead>
<tr>
<th>Set no.</th>
<th>Mould cavity</th>
<th>Part volume</th>
<th>Runner diameter</th>
<th>Gate diameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>11</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>12</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>13</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>14</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>15</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>16</td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>17</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>18</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>19</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>20</td>
<td>3</td>
<td>1</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>21</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>22</td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>23</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>24</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>25</td>
<td>3</td>
<td>3</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>26</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>27</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>

that has many input parameters and one output parameter (i₁, i₂,
i₃… ≠ 0).

To build a complete abductive network, the first requirement
is to train the database. The information given by the input and
output parameters must be sufficient. A predicted square error
(PSE) criterion is then used to automatically determine an opti-
mal structure [10]. The principle of the PSE criterion is to select
the least complex, yet most accurate network possible. The PSE
is composed of two terms, that is:

$$\text{PSE} = \text{FSE} + \text{K}_P \tag{3}$$

where FSE is the average square error of the network for fitting
the training data and $\text{K}_P$ is the complex penalty of the network.
Shown as the following equation:

$$\text{K}_P = \text{CPM} \frac{2\sigma_p^2 K}{N} \tag{4}$$

where CPM is the complex penalty multiplier, $K$ is a coefficient
of the network, N is the number of training data to be used and
$\sigma_p^2$ is a prior estimate of the model error variance.

## 3 Problem solving

### 3.1 FEM simulation

Finite element simulation was undertaken with various runner
and gating systems including different volumes, cavities, runner
diameter, gate diameter and gate length for finding the maximum
warp. Table 3 shows the physical properties of simulation mate-
rial (ABS). Figure 2 is an injection mould with four cavities and
FEM mesh. The major mould-flow simulation is divided into 4
portions, that have a fast-filling process, hold-pressure process,
cool and warp processes. Figure 3 shows the final result of the
warp of the FEM analysis.

Similarly, the relationship between the input parameter (cav-
ities, volume, runner and gating system parameters) and output
parameter (warp) is established when the injection is finished.
Table 4 illustrates the runner and gating system parameters and
the maximum product warp obtained from mould-flow analysis.

Based on the development of an optimal runner and gating
system model, three-layer abductive networks, comprised of the
runner and gating system parameters and the injection results
(warp), were synthesized automatically. The abductive network
is capable of predicting product warp under various gate-runner
parameters, volume of injection par and mould cavity. All poly-
nomial equations used in this network are listed in the Appendix
($\text{FSE}=1.2710^{-3}$, $\text{PSE}=1.26\times10^{-3}$).

Table 5 compares the results predicted by the abductive
model with simulation test cases. These test cases were not in-

![](./images/812297196727697408_2.jpg)

Fig.2. FEM mesh of multi-injection mould part

![](./images/812297196727697408_3.jpg)

Fig.3. The warp of FEM-simulation result

**Table 3.** Material Properties, Thermal Properties: Conductivity
0.149500 /m/°C, Specific Heat
2213.000000 J/kg/°C, Density
949.100037 kg/m³, Ejection Temperature 11.900002 °C, No Flow
Temperature 145.300003 °C

<table>
  <thead>
    <tr>
      <th>Temperature °C</th>
      <th>Shear rate 1/s</th>
      <th>Viscosity Pa s</th>
      <th>Temperature °C</th>
      <th>Pressure MPa</th>
      <th>Specific volume cm³/g</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>225.000</td>
      <td>1000.000</td>
      <td>148.899979</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>0.941092</td>
    </tr>
    <tr>
      <td>245.000</td>
      <td>100.000</td>
      <td>340.299988</td>
      <td>0.0000</td>
      <td>160.000</td>
      <td>0.911333</td>
    </tr>
    <tr>
      <td>245.000</td>
      <td>1000.000</td>
      <td>108.199997</td>
      <td>20.000</td>
      <td>0.000</td>
      <td>0.947145</td>
    </tr>
    <tr>
      <td>245.000</td>
      <td>10000.000</td>
      <td>23.299999</td>
      <td>20.000</td>
      <td>160.000</td>
      <td>0.914493</td>
    </tr>
    <tr>
      <td>265.000</td>
      <td>100.000</td>
      <td>219.800003</td>
      <td>92.320</td>
      <td>0.000</td>
      <td>0.968832</td>
    </tr>
    <tr>
      <td>265.000</td>
      <td>1000.000</td>
      <td>78.900002</td>
      <td>129.552</td>
      <td>160.000</td>
      <td>0.932220</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>210.000</td>
      <td>0.000</td>
      <td>1.041063</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>210.000</td>
      <td>160.000</td>
      <td>0.957964</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>250.000</td>
      <td>0.000</td>
      <td>1.065615</td>
    </tr>
  </tbody>
</table>

<table>
<caption>Table 4. The results of mould flow simulation in difference runner-system</caption>
<thead>
<tr>
<th>Set No.</th>
<th>N</th>
<th>Volume of injection part</th>
<th>Runner dimension</th>
<th>Gate dimension</th>
<th>Maximum warp (mm)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.1291</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.1236</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.1320</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.2646</td>
</tr>
<tr>
<td>5</td>
<td>1</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.2489</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.2673</td>
</tr>
<tr>
<td>7</td>
<td>1</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.3948</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.3771</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.4630</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.4628</td>
</tr>
<tr>
<td>11</td>
<td>2</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.6093</td>
</tr>
<tr>
<td>12</td>
<td>2</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.3990</td>
</tr>
<tr>
<td>13</td>
<td>2</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.7870</td>
</tr>
<tr>
<td>14</td>
<td>2</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.8741</td>
</tr>
<tr>
<td>15</td>
<td>2</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.8567</td>
</tr>
<tr>
<td>16</td>
<td>2</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>1.1157</td>
</tr>
<tr>
<td>17</td>
<td>2</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>1.0581</td>
</tr>
<tr>
<td>18</td>
<td>2</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>1.1231</td>
</tr>
<tr>
<td>19</td>
<td>4</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.4332</td>
</tr>
<tr>
<td>20</td>
<td>4</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.5110</td>
</tr>
<tr>
<td>21</td>
<td>4</td>
<td>$10^{L}×10^{W}×10^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.3291</td>
</tr>
<tr>
<td>22</td>
<td>4</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.6742</td>
</tr>
<tr>
<td>23</td>
<td>4</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>0.6521</td>
</tr>
<tr>
<td>24</td>
<td>4</td>
<td>$20^{L}×20^{W}×20^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.6023</td>
</tr>
<tr>
<td>25</td>
<td>4</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.0^{D}$mm×$50^{L}$mm</td>
<td>$1.4^{D}$mm×$0.5^{L}$mm</td>
<td>0.7211</td>
</tr>
<tr>
<td>26</td>
<td>4</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$3.9^{D}$mm×$50^{L}$mm</td>
<td>$1.82^{D}$mm×$0.5^{L}$mm</td>
<td>1.0044</td>
</tr>
<tr>
<td>27</td>
<td>4</td>
<td>$30^{L}×30^{W}×30^{H}×1^{t}$mm</td>
<td>$2.1^{D}×50^{L}$mm</td>
<td>$0.98^{D}$mm×$0.5^{L}$mm</td>
<td>0.9877</td>
</tr>
</tbody>
</table>

cluded in the $L_{27}^{3}$ sets for establishing the model. This set of data is used to test the appropriateness of the abductive model established above. We can see from Table 5 that the maximum warp error is approximately 4%, which shows that the abductive model is suitable for this simulation.

### 3.2 Simulation annealing (SA) algorithm and selection of the optimum gate-runner parameters

Metropolis [11] proposed a criterion to simulate the cooling of a solid to a new state of energy balance. The basic criterion used by Metropolis was an optimization algorithm called "simulated annealing". The algorithm was developed by Kirkpatrick [8] in 1983.

In this paper, the simulated annealing algorithm was used to search for optimal gate and runner system parameters. Figure 4 shows the flow chart in the simulated annealing search. The algorithm is given an initial temperature $T_{s}$, a final temperature $T_{e}$ and a set of initial process parameter vectors $O_{x}$. The objective function [obj] is defined, based on the runner and gating system performance index. The objective function can be recalculated through all the different perturbed compensation parameters. If

<table>
<caption>Table 5. Error between the neural network prediction and FEM simulation (it is not included in any original 27 sets data base)</caption>
<thead>
<tr>
<th>Item</th>
<th>Simulation method</th>
<th>Mould cavity (N)</th>
<th>Volume of injection part</th>
<th>Runner dimension</th>
<th>Gate dimension</th>
<th>Warp</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set 1.</td>
<td>FEM (mould flow)</td>
<td>2</td>
<td>$25^{L}×25^{W}×25^{H}×1^{t}$mm</td>
<td>$3.5^{D}×50^{L}$mm</td>
<td>$1.5^{D}×0.5^{L}$mm</td>
<td>0.9486 mm</td>
</tr>
<tr>
<td>Set 1.</td>
<td>Neural network</td>
<td>2</td>
<td>$25^{L}×25^{W}×25^{H}×1^{t}$mm</td>
<td>$3.5^{D}×50^{L}$mm</td>
<td>$1.5^{D}×0.5^{L}$mm</td>
<td>0.9802mm</td>
</tr>
<tr>
<td>Maximum error</td>
<td colspan="5">$^{*}ABS\left[\frac{FEM-NETWORK}{FEM}\right]$</td>
<td>3.33%</td>
</tr>
<tr>
<td>Set 2.</td>
<td>FEM (mould flow)</td>
<td>4</td>
<td>$22^{L}×22^{W}×22^{H}×1^{t}$mm</td>
<td>$2.8^{D}×50^{L}$ mm</td>
<td>$1.5^{D}×0.5^{L}$mm</td>
<td>0.5995mm</td>
</tr>
<tr>
<td>Set 2.</td>
<td>Neural network</td>
<td>4</td>
<td>$22^{L}×22^{W}×22^{H}×1^{t}$mm</td>
<td>$2.8^{D}×50^{L}$ mm</td>
<td>$1.5^{D}×0.5^{L}$mm</td>
<td>0.6243mm</td>
</tr>
<tr>
<td>Maximum error</td>
<td colspan="5">$^{*}ABS[\frac{FEM-NETWORK}{FEM}]$</td>
<td>4.14%</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">$^{*}$ABS []: Absolute value</td>
</tr>
</tfoot>
</table>

![](./images/812297196727697408_4.jpg)

Fig.4. Flow chart in the simulated annealing searching

the new objective function becomes smaller, the perturbed process parameters are accepted as the new process parameters and the temperature drops a little in scale. That is:

$$\mathrm{T}_{i+1}=\mathrm{T}_{i} \mathrm{C}_{T} \tag{5}$$

where $i$ is the index for the temperature decrement and $C_{T}$ is the decaying ratio for the temperature $(C_{T}<1)$.

However, if the objective function becomes larger, the probability of acceptance of the perturbative process parameters is given as:

$$\operatorname{Pr}(\mathrm{obj})=\exp \left[\frac{\Delta \mathrm{obj}}{k_{B} T}\right] \tag{6}$$

where $k_{B}$ is the Boltzmann constant and $\Delta$ obj is the difference in the objective function. The procedure is repeated until temperature $T$ approaches zero, which shows the energy level dropping to its lowest state. The objective function [obj] is formulated as follows:

$$\text { obj }=\mathrm{w}^{*}(\text { minimum warp, Append A) } \tag{7}$$

where $w$ is the weighting function.

The gate and runner parameters of the multi-cavity mould should match the simulation data method. In other words, the basic condition of optimization should fall in a certain range as follows:

1. The runner diameter-$\mathrm{R}_{D}$ determined from optimization should be larger than the minimum runner diameter-$\mathrm{R}_{D}$ and smaller than the maximum runner diameter-$\mathrm{R}_{D}$.
2. The gate diameter-$\mathrm{G}_{D}$ determined from optimization should be larger than the minimum gate diameter-$\mathrm{G}_{D}$ and smaller than the maximum gate diameter-$\mathrm{G}_{D}$.
3. The mould cavity-N determined from optimization should be larger than the minimum mould cavity-N and smaller than the maximum mould cavity-N.
4. The injection part volume-V determined from optimization should be larger than the minimum injection part volume-V and smaller than the maximum injection part volume-V.

The inequality is given as follows:

$$
\begin{aligned}
\text { The smallest runner diameter- } & \mathrm{R}_{D}<\text { runner diameter- } \mathrm{R}_{D} \\
& <\text { the largest runner diameter- } \mathrm{R}_{D}
\end{aligned} \tag{8}
$$

$$
\begin{aligned}
\text { The smallest gate diameter- } & \mathrm{G}_{D}<\text { gate diameter- } \mathrm{G}_{D} \\
& <\text { the largest gate diameter- } \mathrm{G}_{D}
\end{aligned} \tag{9}
$$

$$
\begin{aligned}
\text { The smallest mould cavity- } & \mathrm{N}<\text { mould cavity- } \mathrm{N} \\
& <\text { the largest mould cavity- } \mathrm{N}
\end{aligned} \tag{10}
$$

$$
\begin{aligned}
\text { The smallest injection part volume- } & \mathrm{V}<\text { injection part volume- } \mathrm{V} \\
& <\text { the largest injection part volume- } \mathrm{V}
\end{aligned} \tag{11}
$$

The upper bound conditions should be kept at an acceptable level during the search routine in order to find the optimal value of the gate and runner system parameters.

## 4 Results and discussion

The simulation is used to illustrate the process of optimizing the multi-cavity injection moulded parameters. When the weight function $\mathrm{w}_{n}=1$, the $\mathrm{R}_{D}, \mathrm{G}_{D}$, and $\mathrm{V}$ are of equal import and the weighted value $=1$. Fixed cavity (N) and volume (V) parameters used in the simulation annealing algorithm are given as follows: the initial temperature $\mathrm{T}_{s}=100{ }^{\circ} \mathrm{C}$, the final temperature $\mathrm{T}_{e}=0.0001{ }^{\circ} \mathrm{C}$, the decaying ratio $\mathrm{C}_{T}=0.95$ and the Boltzmann constant $\mathrm{k}_{s}=0.00667$. The major aim was to get the minimum warp from the abductive network model and the gate-runner system parameter. In Fig. 5, when the mould cavity is $\mathrm{N}=2$, and the volume of injection parts is $18 \mathrm{x} 18 \mathrm{x} 18 \mathrm{x} 1.0^{\prime} \mathrm{mm}$, the gate diameter $\mathrm{G}_{D}=1.82 \mathrm{~mm}$ is fixed, the parameter of the runner diameter has the minimum warp when the dimension of the runner diameter $\left(\mathrm{R}_{D}\right)$ is $2.4 \mathrm{~mm}$, it can be found that the warp is 0.711 (minimum). In Fig. 6, the runner diameter $\mathrm{R}_{D}=2.4 \mathrm{~mm}$

![](./images/812297196727697408_5.jpg)

Fig. 5. The relationship between runner diameter and minimum warp

![](./images/812297196727697408_6.jpg)

Fig. 6. The relationship between gate diameter and minimum warp

is fixed, the parameter of the gate diameter has the minimum warp when the dimension of the gate diameter $(G_{D})$ is 1.82 mm, it can be found that the warp is 0.711 (minimum).

Table 6 compares the simulation mould-flow error value with the optimal selection value of results predicted by the neural model. The maximum error is approximately 8.6%. In the fore- going discussion, it has been clearly shown that the process parameter for optimum gate-runner system performance can be systematically obtained through this approach.

## 5 Conclusion

This paper illustrates an abductive network approach to mod- elling and optimizing gate and runner system parameters for mulit-cavity moulds. The conclusions of this paper may be stated as follows:

1. By comparing the value of errors using the finite-element method and abductive network prediction, we achieved the best runner system and warp parameter model. Based on the best modelling of the abductive network, the complicated re- lationships between the runner system parameters and warp can be obtained.
2. A comparison was made between the FEM simulation mould-flow error and a model of predicted values of the opti- mization process. This comparison shows that the model not only fits the FEM simulation mould-flow, but also the finite- element and abductive network predictions. The rapidity and efficiency of determining optimal runner system parameters for injection moulding, can successfully improve the accu- racy of the injection-mould design process.
3. Modern injection moulding - especially in the 3C industry - needs less time to fabricate accurate products such as the cell phone with digital camera, the camera lens and the cell phone shell. The injection mould, however, is restricted by the in- jection parameters and can only be produced through single or double cavities. For mouldings with multiple cavities, ad- justing injection parameters of each cavity to the same level is particularly difficult. The resultant rate of failed product is untenable. The adductive network technique and the SA are used to search for the optimal conditions of multiple cavity moulds. The aim is to gain high levels of productivity and to reach a level of accuracy that meets the required conditions.

### References

1. Li CS, Shen YK (1995) Optimum design runner system balancing in injection moulding. Int Commun Heat Mass Transf 22(2):179-188
2. Sulaiman S, Keen TC (1997) Flow analysis along the runner and gating system of a casting process. J Mater Process Technol 63:690-695

Table 6. The predict of optimal selection and the FEM method compared to the maximum warp

<table>
<thead>
<tr>
<th>Item cavity (N)</th>
<th>Mould injection part</th>
<th>Volume of dimension</th>
<th>Runner dimension</th>
<th>Gate</th>
<th>Warp</th>
</tr>
</thead>
<tbody>
<tr>
<td>Neural network</td>
<td>2</td>
<td>$18^{L}$x$18^{W}$x$18^{H}$x$1.0^{I}$mm</td>
<td>$2.4^{D}$X$50^{L}$mm</td>
<td>$1.82^{D}$X$0.5^{L}$mm</td>
<td>0.711</td>
</tr>
<tr>
<td>FEM (mould flow)</td>
<td>2</td>
<td>$18^{L}$x$18^{W}$x$18^{H}$x$1.0^{I}$mm</td>
<td>$2.4^{D}$X$50^{L}$mm</td>
<td>$1.82^{D}$X$0.5^{L}$mm</td>
<td>0.772</td>
</tr>
<tr>
<td colspan="5">Error : *ABS$\left[ \frac{FEM-NETWORK}{FEM} \right]$</td>
<td>8.6%</td>
</tr>
</tbody>
</table>

*ABS [] : Absolute value

3. Hu BH, Tong KK, Niu XP, Pinwill I (2000) Design and optimization of runner and gating systems for the die casting of thin-wall magnesium telecommunication parts through numerical simulation. J Mater Process Technol 105:128–133

4. Lin JC (2001) Optimum gate design of free-form injection mould using the abductive network. Int J Adv Manuf Technol 17:294–304

5. Jong WR, Wang KK (1990) Automatic and optimal design of runner systems in injection moulding based on the flow simulation. SPE An- nual Technical Conference, pp 554–560

6. Montgomery GJ, Drake KC, Abductive reasoning network. Neurocom- puting 2:97–104

7. Mouldflow Corporation (2001) Moldflow course map, basic modeling, mesh editing and post processing, version 3.1. Mouldflow Corporation, USA

8. Kirkpartick S, Gelatt CD, Vecchi MP (1983) Optimization by simulated annealing. Science 220:671–680

9. Ivakhnenko AG (1971) Polynomial theory of complex system. IEEE Trans Syst Man Cybern 1(4):364–378

10. Barron AR (1984) In: Farlow SJ(ed) Predicted square error: a criterion forautomatic model selection, self-organizing methods in modeling: GMDH type algorithms. Dekker, New York

11. Metropolis N, Rosenbluth A, Rosenbluth M, Teller A, Teller E (1953) Equation of state calculation by fast computing machines. J Chem Phys 21:1087–1092

# Appendix: The relationship between of input parameters and warp

![](./images/812297196727697408_7.jpg)

$\text{Normalizer}_{CN2}=-1.83586+0.786796^* \text{ Input parameter(cavity number)};$

$\text{Normalizer}_{RD4}=-4.00617+1.335391* \text{ Input parameter(run- ner diameter)}$

$\text{Normalizer}_{GD5}=-4.00617+2.86155^* \text{ Input parameter(gating diameter)};$

$\text{Normalizer}_{IV3}=-2.4037+0.120185^* \text{ Input parameter(injec- tion volume)};$

$$
\begin{align*}
\text{Triple}_8 &= 0.678393 - 0.3333^* \text{Normalizer}_{CN2} \\
&+0.04411^*\text{Normalizer}_{RD4} - 1.0659^*(\text{Normalizer}_{CN2})^2 \\
&+0.0804199^*(\text{Normalizer}_{RD4})^2 \\
&+0.0616056^*\text{Normalizer}_{CN2}^*\text{Normalizer}_{RD4} \\
&+0.0609406^*\text{Normalizer}_{CN2}^*\text{Normalizer}_{RD4}^*\text{Normalizer}_{GD5} \\
&+0.75^*(\text{Normalizer}_{CN2})^3;
\end{align*}
$$

$$
\begin{align*}
\text{Double}_9 &= 0.678393 - 0.274663^* \text{Normalizer}_{CN2} \\
&+0.0441131^* \text{Normalizer}_{RD4} - 1.0659^*(\text{Normalizer}_{CN2})^2 \\
&+0.0804199^*(\text{Normalizer}_{RD4})^2 \\
&+0.0616^*\text{Normalizer}_{CN2}^*\text{Normalizer}_{RD4} \\
&+0.75^*(\text{Normalizer}_{CN2})^3;
\end{align*}
$$

$$
\begin{align*}
\text{Double}_{10} &= -0.06793 + 0.608463^* \text{Normalizer}_{IV3} \\
&+0.0441131^*\text{Normalizer}_{RD4} \\
&-0.00987721^*(\text{Normalizer}_{IV3})^2 \\
&+0.0804199^*(\text{Normalizer}_{RD4})^2 \\
&-0.095574^*\text{Normalizer}_{IV3}^*\text{Normalizer}_{RD4} ;
\end{align*}
$$

$$
\begin{align*}
\text{Triple}_7 &= 0.804449 - 8.76191^*\text{Triple}_8 + 8.9015^*\text{Double}_9 \\
&+0.74973^* \text{Double}_{10} - 211.981^*(\text{Triple}_8)^2 \\
&-215.076^*(\text{Double}_9)^2 + 0.0274245^*(\text{Double}_{10})^2 \\
&+426.355^*\text{Triple}_8^*\text{Double}_9 + 3.10301^*\text{Triple}_8^*\text{Double}_{10} \\
&-2.65269^*\text{Double}_9^*\text{Double}_{10} \\
&+0.115732^*\text{Triple}_8^* \text{Double}_9^*\text{Double}_{10} + 7.3526^* \\
&(\text{Triple}_8)^3 - 6.733^*(\text{Double}_9)^3 + 0.321305^*(\text{Double}_{10})^3 ;
\end{align*}
$$

$\text{Warp(output)} = \text{U}_6=0+0.577826+0.312686^* \text{Triple}_7 ;$