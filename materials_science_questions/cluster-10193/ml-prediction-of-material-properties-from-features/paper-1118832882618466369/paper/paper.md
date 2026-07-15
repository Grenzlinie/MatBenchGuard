# Accelerating Multi-Objective Collaborative Optimization of Doped Thermoelectric Materials via Artificial Intelligence

Yuxuan Zeng, $^{1}$ Wenhao Xie, $^{1}$ Wei Cao, $^{1,2, *}$ Tan Peng, $^{2}$ Yue Hou, $^{1}$ Ziyu Wang, $^{1,2,3, \dagger}$ and Jing Shi $^{2}$

$^{1}$ The Institute of Technological Sciences, Wuhan University, 430072, PR China
$^{2}$ Key Laboratory of Artificial Micro- and Nano-Structures of Ministry of Education, School of Physics and Technology, Wuhan University, Wuhan 430072, PR China
$^{3}$ School of Physics and Microelectronics, Key Laboratory of Materials Physics of Ministry of Education, Zhengzhou University, Zhengzhou 450001, PR China

(Dated: April 14, 2025)

The thermoelectric performance of materials exhibits complex nonlinear dependencies on both elemental types and their proportions, rendering traditional trial-and-error approaches inefficient and time-consuming for material discovery. In this work, we present a deep learning model capable of accurately predicting thermoelectric properties of doped materials directly from their chemical formulas, achieving state-of-the-art performance. To enhance interpretability, we further incorporate sensitivity analysis techniques to elucidate how physical descriptors affect the thermoelectric figure of merit ($zT$). Moreover, we establish a coupled framework that integrates a surrogate model with a multi-objective genetic algorithm to efficiently explore the vast compositional space for high-performance candidates. Experimental validation confirms the discovery of a novel thermoelectric material with superior $zT$ values in the medium-temperature regime.

## I. INTRODUCTION

Thermoelectric materials exploit the Seebeck effect to convert temperature gradients into electrical energy. Compared to conventional energy sources such as nuclear and fossil fuels, thermoelectric technologies offer several distinct advantages, including the absence of moving parts, silent operation, and environmental friendliness [1]. In recent years, thermoelectric materials have been widely applied in diverse fields, including health monitoring [2], waste heat recovery [3], and powering wearable electronics [4]. The performance of a thermoelectric material is typically characterized by the dimensionless figure of merit, $zT$, defined as:

$$
zT = \frac{S^2 \sigma T}{\kappa} \tag{1}
$$

where $S$ is the Seebeck coefficient, $\sigma$ is the electrical conductivity, $T$ represents the absolute temperature, and $\kappa$ denotes the total thermal conductivity, comprising both lattice ($\kappa_{\rm L}$) and electronic ($\kappa_{\rm e}$) contributions. A higher $zT$ value signifies superior thermoelectric efficiency.

Widely adopted thermoelectric materials include Bi$_2$Te$_3$-based alloys [5, 6], which are primarily used at room temperature (below $200~^\circ$C); PbTe and its derivatives [7, 8], optimized for mid-temperature applications ($500$-$600~^\circ$C); and SiGe-based alloys [9, 10], which demonstrate superior performance in high-temperature environments (above $800~^\circ$C). The thermoelectric performance of these materials can be significantly enhanced through doping, which enables property optimization beyond the limits of the intrinsic host matrix. Doping strategies in thermoelectrics typically aim to control carrier concentration, engineer the electronic band structure, and reduce lattice thermal conductivity. Common approaches include donor and acceptor doping to modulate electron and hole populations [11]; band convergence to increase the density-of-states effective mass and improve charge transport [12, 13]; and defect engineering to strengthen low-frequency phonon scattering and suppress thermal conductivity [14]. Although the synthesis of doped thermoelectric materials is well-established, the selection of host matrices, dopant species, and their concentrations remains largely empirical. As a result, the discovery of high-performance compositions still relies heavily on time-consuming and costly trial-and-error processes. Furthermore, the computational prediction of thermoelectric properties in doped systems poses considerable challenges. For density functional theory (DFT) calculations, the need to construct large supercells [15, 16] and account for band structure reconstruction [17] leads to substantial computational overhead. Similarly, molecular dynamics (MD) simulations face difficulties such as the lack of accurate force fields [18], limited accessible timescales [19], and other resource constraints.

In recent years, machine learning and deep learning have emerged as powerful data-driven methodologies for addressing complex challenges in thermoelectric materials research, such as predicting power factors [20, 21] and modeling thermal conductivity [22]. To date, the majority of AI-assisted materials studies have concentrated on intrinsic compounds. This is largely attributed to the fact that intrinsic materials possess well-defined crystal and electronic band structures, rendering them more tractable for characterization and computational modeling. Additionally, the availability of large-scale, open-access databases—such as the Materials Project [23] and AFLOW [24]—greatly facilitates data acquisition by providing abundant, high-quality training data. Further-

* wei_cao@whu.edu.cn
$\dagger$ zywang@whu.edu.cn

![](./images/1118832882618466369_1.jpg)

FIG. 1. The proposed deep learning-optimization algorithm coupled framework is designed for multi-objective collaborative optimization in the design of thermoelectric materials with high $zT$ values. (a) Two datasets are employed separately for deep learning training and transfer learning testing, both derived from experimental sources. (b) Digitized descriptors are used to represent different materials. (c) Deep learning is utilized to construct the mapping between descriptors and thermoelectric performance. (d) The Pareto-front is adopted to select a subset of candidate materials with optimal performance from the dataset. (e) The optimization algorithm is applied to explore promising virtual samples from the vast compositional space. (f) Upon completion of the optimization iterations, the most promising candidate(s) are selected for experimental characterization and mechanistic investigation.

more, for intrinsic systems, computational methods like density functional theory (DFT) and molecular dynam- ics (MD) are not only practical but also reliable for val- idating machine learning predictions, and in some cases, for enhancing model performance through active learning strategies [25].

In the prediction of doped materials' properties, three primary challenges have been identified [26]: (1) the ab- sence of crystal structure information; (2) the dilution of doping effects-subtle variations in dopant concentration are often difficult to capture as meaningful distinguish- ing features; and (3) strong nonlinear effects-changes in dopant species and concentrations can have signifi- cant and highly nonlinear impacts on material proper- ties. In the context of thermoelectric transport proper- ties in doped systems, several notable efforts have been made. Gyoung et al. introduced DopNet[26], a deep learning framework specifically developed for predicting the thermoelectric performance of doped materials. In parallel, Parse et al.[27] developed a user-interactive plat- form [28], enhancing accessibility and usability for re- searchers. While these studies offer valuable insights, several limitations persist:

- Suboptimal model accuracy, manifested in overfit- ting to the training set [27] and limited extrapola- tion capability [26].
- Dependence on experimental data for feature con- struction [27].
- Evaluation of extrapolation ability solely through model transfer across different datasets, lacking ex- perimental validation [26, 29].
- Absence of inverse material design considera- tions [26, 27, 29].

To enable efficient exploration of doped thermoelectric materials, it is essential not only to address the aforemen- tioned challenges, but also to account for the vast com- binatorial design space involving host matrices, dopant species, and their concentrations. In related fields such as high-entropy alloy design, optimization strategies like genetic algorithms [30, 31] and Bayesian optimization [32] have been successfully applied to inverse material design. However, in the context of thermoelectric materials, the electrical transport parameters-namely the Seebeck co- efficient $(S)$ and electrical conductivity $(\sigma)$-are inher ently antagonistic, as improvements in one often lead to deterioration of the other. This trade-off is further com- pounded by the effects of electron-phonon coupling [33], which intricately link electrical and thermal transport processes.

This work aims to address the inefficiency of trial- and-error strategies in thermoelectric material discov- ery. We propose a wavelet-based feature enhancement method that extracts both inter- and intra-system vari- ations from chemical formulas. Based on this, we

![](./images/1118832882618466369_2.jpg)

FIG. 2. $k$-means clustering and t-SNE 2D visualization. (a) All samples at 600 K are divided into 9 clusters, from $C_0$ to $C_8$, distinguished by different scatter plot markers. (b) and (c) show local zoom-ins of $C_0$ and $C_2$, respectively, with color mapping indicating the $zT$ values of the samples.

develop the Wavelet-enhanced Thermoelectric Network (WaveTENet), a deep learning model that simultaneously predicts five thermoelectric performance criteria: $S$, $\sigma$, $\text{PF}$, $\kappa$, and $zT$. Validated on multiple datasets, WaveTENet achieves state-of-the-art performance. With the integration of the SHapley Additive exPlanation (SHAP) framework, we conduct sensitivity analysis to interpret the role of physical descriptors in determining $zT$. Coupled with the Non-dominated Sorting Genetic Algorithm III (NSGA-III), the framework enables inverse design by optimizing compositions based on model feedback. We identify several high-$zT$ candidates, one of which is experimentally validated. Although this study focuses on thermoelectrics, the methodology is applicable to broader material domains including high-entropy alloys, superconductors, and magnetic materials.

## II. RESULTS

### A. Nonlinear Effects of Doping on thermoelectric Performance

The influence of doping on thermoelectric materials is intrinsically nonlinear, as even slight variations in elemental type or composition can lead to abrupt and pronounced changes in thermoelectric performance [34, 35]. To validate this perspective, we selected multiple samples at 600 K from the dataset for $k$-means clustering. The features used for material characterization are detailed in Sec. II B; these features are not only employed for clustering but also serve as input for subsequent deep learning model training. We determined the number of clusters as $k = 9$ using the Elbow method [36].

In Fig. 2(a), all samples are grouped into nine clusters, among which clusters $C_0$ and $C_2$ tend to exhibit higher $zT$ values. As shown in Fig. 2(b), cluster $C_0$ is primarily composed of derivatives of $\text{Co}_4\text{Sb}_{12}$, a cobalt antimonide with a skutterudite structure [37]. The left subgroup is dominated by Ba- and Yb-doped samples, whereas the right subgroup mainly consists of Sr-doped compositions with additional Sb incorporation. Although most samples in $C_0$ demonstrate relatively high $zT$ values, $\text{Ba}_{0.03}\text{Co}_4\text{Sb}_{12}$ notably exhibits a significantly lower $zT$ of 0.211. Similarly, Fig. 2(c) provides a magnified view of cluster $C_2$, which mainly comprises derivatives of $\text{Mg}_3\text{Sb}_2$ [38]. Notably, $C_2$ is split into two subgroups: the upper subgroup is predominantly doped with Gd and Te, while the lower subgroup primarily features Ho and Te doping. Despite both $\text{Mg}_{3.5}\text{Ho}_{0.01}\text{Sb}_2$ ($zT = 0.159$) and $\text{Mg}_{3.5}\text{Gd}_{0.01}\text{Sb}_2$ ($zT = 0.431$) belonging to this cluster, their $zT$ values remain lower than those of other high-performing samples.

Such nonlinear behavior poses a significant challenge for supervised learning. When predicting the performance of an unknown sample, reference values derived

from similar compositions within the same system in the training data are inherently limited. Both over-reliance on and complete disregard for structurally similar materi- als may negatively affect model predictions. Therefore, it is essential that both feature engineering and deep learn- ing model design explicitly account for this phenomenon. On the one hand, the influence of similar samples should be carefully mitigated; on the other hand, sufficient non- linear fitting capacity must be ensured through deep net- work architectures.

### B. Multi-Source Feature Fusion and Wavelet-Based Enhancement

In materials informatics, mainstream feature construc- tion methods include empirical features, structural fea- tures [39–41], embedding vectors [42], and elemental com- position statistics.

Empirical features refer to variables obtained through experiments or DFT calculations that have a theoretical correlation with the target property. Machine learning models based on such features often achieve high accu- racy with ease; however, acquiring these features can be challenging, making them unsuitable for high-throughput screening. Structural features describe the electronic configuration within a crystal and are represented as vec- tors, but characterizing doped systems in this manner is not straightforward. Mat2Vec [43] is a representative embedding vector approach that draws inspiration from word embeddings in natural language processing. How- ever, such features generally lack interpretability, as the individual dimensions of the vector do not have explicit physical meanings.

To efficiently and accurately represent doped systems, we preliminarily select Magpie [44] as one of the feature sources. Magpie analyzes a given chemical formula and extracts interpretable physical, chemical, electronic, and ionic properties—such as melting point, covalent radius, and electronegativity—for each element. It then com- putes statistical measures such as the mean and variance based on elemental composition. This process does not rely on experimental data or structural parameters, en- abling the rapid construction of sample features.

System-Identified Material Descriptor (SIMD) [29] has demonstrated remarkable performance in predicting the properties of doped thermoelectric materials. The SIMD vector consists of four components:

$$
\mathcal{S}=\mathbf{x}_{s} \oplus \mathbf{c}_{s} \oplus \mathbf{w}_{s}^{(K)} \oplus \mathbf{w}_{s}^{(K)} \tag{2}
$$

where $\mathbf{x}_{s}$ is a 100-dimensional vector encoding the frac- tional composition of elements from H to Fm in the chem- ical formula. $\mathbf{c}_{s}$ is a conditional vector incorporating synthesis conditions, which, in this work, only considers temperature conditions. $\mathbf{w}_{s}^{(K)}$ represents the distance- weighted sum of the system vectors of input chemical composition $s$ in the system identification process, $\mathbf{w}_{s}^{(K)}$ denotes the distance-weighted sum of the target statisti- cal vectors for the selected $K$ nearest material clusters, while the symbol "$\oplus$" signifies vector concatenation. A more detailed explanation can be found in Sec. IV A.

SIMD aggregates training samples similar to a predic- tive sample to form an anchor space. Using $k$-nearest neighbor ($k$NN) method, information from the $k$ most similar known clusters is embedded into $\mathbf{w}_{s}^{(K)}$ and $\mathbf{w}_{s}^{(K)}$. This approach effectively constrains the predicted prop- erties of new samples within a reasonable domain based on prior knowledge. Fundamentally, this is a process of "seeking similarity." However, considering the nonlinear effects discussed in Sec. II A, particularly in cases like $\text{Mg}_{3.5}\text{Ho}_{0.01}\text{Sb}_{2}$, such an anchor space may instead in- troduce adverse effects.

The variations in elemental composition and fraction can be captured by Magpie descriptors. However, when the fractional changes are minimal, the corresponding variations in Magpie descriptors are also subtle, making them insufficient to mitigate the over-reliance on the an- chor space. To address this, we apply Discrete Wavelet Transform (DWT) [45, 46] to the features and incorpo- rate the wavelet coefficients as supplementary descrip- tors, thereby achieving a "preserving differences" ap- proach. DWT can be used to provide local slope esti- mation in time series data to assess similarity [47]. In- spired by this, we aim to amplify the differences among materials within the same doping system.

In our case, we concatenated the SIMD vector $\mathcal{S}$ and the Magpie vector $\mathcal{M}$, treating them as a discrete-time signal. Using the Haar wavelet [48], the original feature signal was decomposed into approximation coefficients ($\mathcal{A}$) and detail coefficients ($\mathcal{D}$). The former represented the main trend (smooth component) of the signal, em- phasizing differences between different doping systems, while the latter captured rapid variations (detail compo- nent), distinguishing subtle differences within the same doping system. After concatenating the wavelet coef- ficients with the initial features, we obtained the final feature representation for model input.

$$
\mathcal{X}=\mathcal{S} \oplus \mathcal{M} \oplus \mathcal{A} \oplus \mathcal{D} \tag{3}
$$

Here, we employ cosine similarity (CS) to evaluate the distinguishability of samples at the feature level. Taking the $C_2$ cluster shown in Fig. 2(a) and (c) as an exam- ple, Table I revealed that for $\text{Mg}_{3.5}\text{Ho}_{0.01}\text{Sb}_{2}$, the CS of samples within the same doping system, $\text{Mg}_{3.5}\text{Ho}_{x}\text{Sb}_{2}$, generally decreased significantly. In contrast, samples that originally exhibited greater differences (CS < 0.8) tended to show an increase in CS after the introduction of DWT. This suggested that during model training, the inclusion of DWT broadened the model's perspective, en- abling it to incorporate a more diverse set of samples into decision-making rather than focusing on a limited num- ber of similar materials within the same doping system. Consequently, this enhanced the model's ability to cap- ture the nonlinear effects of the target properties more effectively.

![](./images/1118832882618466369_3.jpg)

FIG. 3. Architecture of WaveTENet. (a) The network is composed of three main components: the input block, the stacked residual branch, and the output block. (b) The structure of the deep residual module. The modules depicted as rectangles with embedded circles represent linear layers.

<table>
<caption>TABLE I. Cosine similarity in $C_2$ cluster. $\mathcal{S} \oplus \mathcal{M}$ represents the computation result using only SIMD and Magpie features, while $\mathcal{S} \oplus \mathcal{M} \oplus \mathcal{A} \oplus \mathcal{D}$ denotes the computation after incorporating wavelet coefficients. The arrows indicate the changes in cosine similarity of the samples before and after introducing DWT transformation.</caption>
<thead>
<tr>
<th>Formula</th>
<th>$zT$</th>
<th>$\mathcal{S} \oplus \mathcal{M}$</th>
<th>$\mathcal{S} \oplus \mathcal{M} \oplus \mathcal{A} \oplus \mathcal{D}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.01}\text{Sb}_2$</td>
<td>0.1588</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.02}\text{Sb}_2$</td>
<td>0.5902</td>
<td>0.9831</td>
<td>0.9759 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.03}\text{Sb}_2$</td>
<td>0.6094</td>
<td>0.9305</td>
<td>0.9032 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.04}\text{Sb}_2$</td>
<td>0.7487</td>
<td>0.8480</td>
<td>0.7961 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.01}\text{Sb}_2$</td>
<td>0.4314</td>
<td>0.7404</td>
<td>0.7860 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.02}\text{Sb}_2$</td>
<td>0.6203</td>
<td>0.6491</td>
<td>0.6899 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.03}\text{Sb}_2$</td>
<td>0.8175</td>
<td>0.5183</td>
<td>0.5483 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.035}\text{Sb}_2$</td>
<td>0.7121</td>
<td>0.4468</td>
<td>0.4713 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.01}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.7781</td>
<td>0.4270</td>
<td>0.4505 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.02}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.8634</td>
<td>0.3894</td>
<td>0.4087 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.03}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.8395</td>
<td>0.3373</td>
<td>0.3465 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.045}\text{Sb}_2$</td>
<td>0.7984</td>
<td>0.3093</td>
<td>0.3251 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Ho}_{0.04}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.8632</td>
<td>0.2761</td>
<td>0.2737 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.04}\text{Sb}_2$</td>
<td>0.8884</td>
<td>0.3763</td>
<td>0.3960 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.03}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.9778</td>
<td>0.0056</td>
<td>0.0566 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.5}\text{Gd}_{0.04}\text{Sb}_{1.97}\text{Te}_{0.03}$</td>
<td>0.8964</td>
<td>-0.0947</td>
<td>-0.0519 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.07}\text{Sb}_{1.5}\text{Bi}_{0.48}\text{Se}_{0.02}$</td>
<td>0.9604</td>
<td>-0.7134</td>
<td>-0.7088 $\uparrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.07}\text{Sb}_{1.5}\text{Bi}_{0.47}\text{Se}_{0.03}$</td>
<td>0.9032</td>
<td>-0.7205</td>
<td>-0.7255 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.07}\text{Sb}_{1.5}\text{Bi}_{0.46}\text{Se}_{0.04}$</td>
<td>0.9064</td>
<td>-0.7235</td>
<td>-0.7347 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.07}\text{Sb}_{1.5}\text{Bi}_{0.45}\text{Se}_{0.05}$</td>
<td>0.8477</td>
<td>-0.7225</td>
<td>-0.7362 $\downarrow$</td>
</tr>
<tr>
<td>$\text{Mg}_{3.07}\text{Sb}_{1.5}\text{Bi}_{0.44}\text{Se}_{0.06}$</td>
<td>0.8254</td>
<td>-0.7176</td>
<td>-0.7305 $\downarrow$</td>
</tr>
</tbody>
</table>

### C. Architecture of WaveTENet

We designed WaveTENet to achieve multi-objective regression of thermoelectric transport properties for doped material compositions. WaveTENet consists of four functional blocks: Featurizer, Input block, Deep residual block, and Output block.

The Featurizer directly generates the corresponding SIMD vector $\mathcal{S} \in \mathbb{R}^{n \times d_{\text{SIMD}}}$ and Magpie vector $\mathcal{M} \in \mathbb{R}^{n \times d_{\text{Magpie}}}$ based on the input material formula and concatenates them. Treating $\mathcal{S} \oplus \mathcal{M}$ as a discrete signal sequence, a first-level Haar wavelet transform is applied to obtain the low-frequency coefficient vector $\mathcal{A} \in \mathbb{R}^{n \times (d_{\text{SIMD}}+d_{\text{Magpie}})/2}$ and the high-frequency coefficient vector $\mathcal{D} \in \mathbb{R}^{n \times (d_{\text{SIMD}}+d_{\text{Magpie}})/2}$. The variables $n$ and $d$ represent the number of samples in the training data (or a single batch) and the dimensionality of the features, respectively. The number of wavelet coefficients obtained from a single-level Haar wavelet transform is half the length of the original signal [49]. In our case, the specific dimension of each vector are:

$$
\begin{cases}
d_{\text{SIMD}} = 219, \\
d_{\text{Magpie}} = 255, \\
d_{\mathcal{A}} = d_{\mathcal{D}} = 237.
\end{cases} \tag{4}
$$

Eq. (3) is the output of Featurizer, denoted as $\mathcal{X}$, which will be read by the Input block for further processing after min-max normalization.

The task of the Input block is to perform fundamental processing on the input features. This block consists of three interconnected components: a linear layer, a batch normalization (BN) layer, and an activation function layer.

We set the input and output dimensions of the linear layer to be identical, thereby preserving the dimensionality of the initial feature vector $\mathbf{x}$. This choice is motivated by the fact that, in our study, the feature differences among samples within the same doping system are inherently subtle. Reducing dimensionality through a linear layer would further obscure these distinctions, potentially compromising the model's ability to capture

meaningful variations. The BN layer computes the mean and standard deviation for each mini-batch and normalizes the data:

$$
\hat{\mathcal{X}} = \frac{\mathcal{X} - \mu}{\sigma} \tag{5}
$$

where $\mu$ is the feature mean vector, and $\sigma$ is the feature standard deviation vector. The significance of BN lies in:

- Ensuring that data from different batches have similar distributions, thereby improving the model's generalization ability [50].
- Addressing the issue of "internal covariate shift." [51]

Unlike conventional affine transformations, all linear layer outputs in WaveTENet are first processed by BN before being passed through the ReLU activation function. This design primarily serves to alleviate the vanishing gradient issue associated with ReLU [52].

The deep residual block consists of multiple residual blocks connected in series, where each residual block is composed of three sequentially stacked basic modules, each following the structure of "Linear layer $\rightarrow$ BN $\rightarrow$ ReLU $\rightarrow$ Dropout layer." Experimental results indicate that using six stacked residual blocks achieves an optimal balance between model performance and training efficiency. Dropout is implemented by randomly setting a fixed proportion of neuron outputs to zero during each training iteration, thereby preventing overfitting and enhancing generalization ability [53]. Moreover, to equip the model with strong nonlinear learning capabilities, WaveTENet incorporates multiple stacked linear layers. To mitigate the risk of gradient explosion or vanishing gradients, we adopt residual connections inspired by the ResNet [54].

The structure of the output block is significantly simpler, consisting only of a BN layer and a linear layer. Following the output block, a single neuron is fully connected to the linear layer, serving as the output head of the model.

## D. Model Training & Evaluation

Experimentally Synthesized Thermoelectric Materials (ESTM) (https://github.com/KRICT-DATA/SIMD) is an open-source thermoelectric material dataset constructed via text mining [29], encompassing both doped and intrinsic compounds with thermoelectric performance metrics recorded over a temperature range from as low as 10 K to as high as 1,275 K, comprising up to 5,205 entries. In our study, we excluded intrinsic compounds from the ESTM dataset, as their thermoelectric properties require additional consideration of carrier concentration [21]. In contrast, doping inherently serves as a direct means of modulating carrier concentration [55], which can be reflected in the chemical formula, thereby eliminating the need for an additional carrier-related parameter in doped materials.

During training, we incorporated $\ell_2$ regularization into WaveTENet to mitigate overfitting. Given that most PF values fall within the range of $10^{-5}$ to $10^{-3}$, numerical precision issues in floating-point operations could potentially affect model fitting [56]. To address this, we applied a scaling factor of $10^5$ to PF during data loading. In contrast, $\sigma$ exhibits a broad numerical range, spanning from a minimum of 0 to a maximum on the order of $10^7$. Such a large-scale variation in values can disrupt deep learning model training; hence, we introduced a scaling factor of $10^{-3}$ to $\sigma$ to compress the distribution of the target property.

To evaluate the performance of WaveTENet, we established a benchmark comprising DopNet, CatBoost [57], and a multilayer perceptron (MLP) model. The performance of DopNet was directly extracted from the original paper, while CatBoost and MLP were trained independently by us. We reported the average prediction performance measured over 10 repeated evaluations and ensured consistency in dataset partitioning for CatBoost and MLP. A comparative analysis of thermoelectric property predictions across different models is presented in Table II, where WaveTENet achieved the current State of the Art (SOTA) performance.

<table>
<caption>TABLE II. 10-fold cross-validation results for each of the transport properties for the WaveTENet, DopNet, CatBoost and MLP models in terms of $R^2$. Bold values denotes the SOTA performance.</caption>
<thead>
  <tr>
    <th>Model</th>
    <th>$S$</th>
    <th>$\sigma$</th>
    <th>PF</th>
    <th>$\kappa$</th>
    <th>$zT$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>WaveTENet</th>
    <td><b>0.977</b></td>
    <td><b>0.984</b></td>
    <td>0.981</td>
    <td><b>0.972</b></td>
    <td><b>0.963</b></td>
  </tr>
  <tr>
    <th>DopNet</th>
    <td>0.860</td>
    <td>0.640</td>
    <td>0.790</td>
    <td>0.610</td>
    <td>0.860</td>
  </tr>
  <tr>
    <th>CatBoost</th>
    <td>0.955</td>
    <td>0.973</td>
    <td><b>0.983</b></td>
    <td>0.881</td>
    <td>0.959</td>
  </tr>
  <tr>
    <th>MLP</th>
    <td>0.910</td>
    <td>0.917</td>
    <td>0.914</td>
    <td>0.851</td>
    <td>0.881</td>
  </tr>
</tbody>
</table>

The architecture of the MLP is $64 \times 64 \times 64$, with the number of training iterations determined by early stopping, where the tolerance is set to 30. The optimal hyperparameters for CatBoost were automatically tuned using Optuna [58], and the final hyperparameter configuration is provided in the Supplementary Information. Both MLP and CatBoost were trained exclusively on SIMD and Magpie descriptors without incorporating wavelet transforms. Interestingly, in predicting electronic transport properties, CatBoost and WaveTENet exhibited comparable predictive performance, with CatBoost even slightly surpassing WaveTENet in PF prediction. However, for $\kappa$, the inclusion of wavelet coefficients substantially enhanced accuracy. Generally, due to its tree-based structure, ensemble learning algorithms such as CatBoost tend to outperform deep learning models on non-smooth molecular feature datasets [59–61]. WaveTENet, by leveraging extensive residual stacking of linear layers, attains sufficient nonlinear learning capacity, enabling it to surpass conventional MLPs and achieve

![](./images/1118832882618466369_4.jpg)

FIG. 4. The scatter plots of WaveTENet's predictions for $S$, $\sigma$, PF, $\kappa$, and $zT$ are presented. Each point in the plots corresponds to a sample from the dataset, with the $x$-axis representing the ground truth (experimentally measured values) and the $y$-axis indicating the model's predicted values. The black dashed diagonal line denotes the ideal case where predictions perfectly match the true values. The solid blue and red lines represent the regression fits for the training and test sets, respectively.

![](./images/1118832882618466369_5.jpg)

FIG. 5. Performance comparison between WaveTENet and CatBoost on the transfer learning dataset. In the prediction tasks of PF, $\kappa$, and $zT$, WaveTENet consistently outperforms CatBoost in accuracy.

performance comparable to CatBoost in electronic trans-
port predictions. Notably, WaveTENet significantly out-
performed all other models in predicting $\kappa$, which may
stem from its depth-driven nonlinear learning capacity
or from the preservation of sample distinctiveness via
identity mappings in linear layers and wavelet-derived
features. A similar phenomenon has been observed in
CraTENet's PF predictions [21].

To objectively evaluate the extrapolation capability of
WaveTENet, we assess its performance on a new dataset
using transfer learning and select CatBoost for compar-
ison. Transfer learning refers to fine-tuning a model

![](./images/1118832882618466369_6.jpg)

FIG. 6. SHAP force plot for the ${\text{Mg}}_{3.5}{\text{Ho}}_{x}{\text{Sb}}_{2}$ system at 600 K. Bold numbers denote the surrogate model's estimated $zT$ values (not actual measurements). Numbers below the arrows represent feature values, with red indicating positive contributions and blue negative ones. Arrow length reflects feature influence, while $x$-axis tick marks quantify the impact magnitude. In subplot (c), the unannotated values are attributed to intricate interactions among multiple features, rather than the effect of any individual descriptor alone.

trained on a source task for a new task, thereby re- ducing training costs. In our study, the source task in- volves training a sufficiently well-performing predictive model on the ESTM dataset, which is then transferred to a new dataset to evaluate WaveTENet's performance across different datasets. The transfer learning dataset we employ originates from the UCSB dataset [62, 63], with intrinsic materials manually removed. During train- ing, we freeze the first five deep residual blocks of WaveTENet, leaving only the last one for parameter op- timization.

Notably, to eliminate the influence of feature vectors, we provide CatBoost with the same set of feature vectors, including those derived from wavelet transformations, i.e., $\mathcal{X}$ in Fig. 3(a). The results of transfer learning, as shown in Fig. 5, indicate that WaveTENet outperforms CatBoost in predicting PF, $\kappa$, and $zT$. Moreover, the pre-trained WaveTENet model demonstrates impressive performance on the new dataset, confirming its strong ex- trapolation capability and suitability for novel material discovery.

### E. Deepening Physical Interpretability via Sensitivity Analysis

Among the three types of descriptors employed in our study, SIMD and wavelet coefficients lack explicit phys- ical meaning, whereas Magpie provides statistical rep- resentations of the physical and chemical properties of constituent elements, making it inherently interpretable. As shown in Table II, the predictive accuracy of the Cat- Boost model based solely on Magpie descriptors remains within an acceptable range compared to WaveTENet for $zT$ prediction. Therefore, we select the CatBoost model with Magpie descriptors as a surrogate model for inter- pretability analysis.

To uncover the potential relationships between elemen- tal composition and $zT$, we employ SHAP [64] to quan- tify the contribution of each descriptor to $zT$. The anal- ysis focuses on the 10 key descriptors affecting $zT$, as illustrated in Fig. 7(a). Fig. 7(b) presents a heatmap of the Pearson correlation coefficients (PCC) among the key descriptors. Overall, the majority of descriptors exhibit negligible correlation, which serves as a prerequisite for applying SHAP, as kernel-based SHAP index does not account for dependencies among descriptors [65].

In Fig. 7(a), temperature $T$ emerges as the most sig- nificant feature influencing the $zT$ of thermoelectric ma- terials, exhibiting a clear positive correlation. This is expected, as temperature is an explicit component in the definition of $zT$ in Eq. (1). It is worth noting that the majority of the samples in our dataset correspond to tem- peratures ranging from 300 K to 700 K. In reality, when the temperature exceeds this range, the $zT$ value of some materials tends to decrease [66]. However, if we con- fine our analysis to the dataset used in this study, this conclusion remains valid, as it is well established that

![](./images/1118832882618466369_7.jpg)

FIG. 7. The figure provides an overview of feature importance and temperature-dependent behavior. (a) SHAP summary plot of the top 10 features ranked by the sum of absolute SHAP values. The vertical axis shows feature importance, while the horizontal axis indicates each feature's impact on the model output. Each dot represents a sample, with vertical stacking showing density and color indicating feature values (red: high, blue: low). (b) Pearson correlation heatmap of the top 10 features, where cell values and color intensity represent the strength of correlation. (c) Scatter plot of $zT$ vs. $\Delta \bar{T}_\text{M}$, with samples color-mapped by temperature $T$ to reveal thermal trends. (d) Same plot as (c), limited to samples at $T=600$ K to highlight temperature-specific behavior.

for most thermoelectric materials, $zT$ generally increases with temperature within the 300 K to 700 K range.

Beyond the direct mathematical dependence of $zT$ on $T$, temperature also indirectly influences $zT$ by affecting $\sigma$, $S$, and $\kappa$. The electrical conductivity $\sigma$ and the Seebeck coefficient $S$ are defined as:

$$
\sigma = n q \mu \tag{6}
$$

$$
S = \frac{\pi^2 k_B^2 T}{3e} \left[ \frac{1}{\sigma} \frac{\mathrm{d}\sigma(E)}{\mathrm{d}E} \right]_{E=E_\text{F}} \tag{7}
$$

where $n$ denotes the carrier concentration, representing the number of free electrons or holes per unit volume, $q$ is the elementary charge, and $\mu$ is the carrier mobility, which quantifies the drift velocity of carriers under an applied electric field. Hence, electrical conductivity is jointly determined by carrier concentration and mobility. Eq. (7), known as the Mott relation [67], describes the relationship between the Seebeck coefficient $S$ and the energy-dependent conductivity gradient. The prefactor $\frac{\pi^2 k_B^2 T}{3e}$ is a temperature-dependent coefficient, where $k_B$ is the Boltzmann constant, $T$ is the absolute temperature, and $e$ is the elementary charge. The term inside the brackets, $\left[ \frac{\mathrm{d}\sigma(E)}{\mathrm{d}E} \right]_{E=E_F}$, represents the normalized energy derivative of the conductivity, evaluated at the Fermi level $E_F$. This quantity characterizes the asymmetry of carrier transport properties. An increase in temperature generally leads to a decline in carrier mobility [68], primarily due to enhanced carrier scattering [69]. According to Eq. (6) and Eq. (7), the reduction in carrier mobility directly results in a decrease in $\sigma$, whereas both the decrease in $\sigma$ and the increase in temperature contribute to an increase in $S$. The temperature dependence of $S$ and $\sigma$ exhibits a competing behavior; however, within a given temperature range, a peak in the PF is typically observed [70]. A similar trend is also commonly found in their variations with carrier concentration.

Beyond electrical transport, the temperature dependence of thermal conductivity must also be considered. In thermoelectric semiconductors, lattice thermal conductivity $\kappa_\text{L}$ generally dominates over electronic thermal conductivity $\kappa_\text{e}$ in magnitude and serves as the primary factor. At intermediate to high temperatures, Umklapp scattering intensifies, leading to a reduction in the phonon mean free path and consequently lowering $\kappa_\text{L}$ [71]. In summary, $zT$ exhibits an increasing trend with temperature. However, it is important to note that this conclusion is only valid within the approximate temperature range of 300 K to 700 K.

$M(\chi)$ represents the mode of the electronegativity of elements in a material, defined as:

$$
M(\chi) = \underset{\chi}{\arg \max} f(\chi) \tag{8}
$$

where $\chi$ denotes the electronegativity of an element, and $f(\chi)$ represents the frequency function of electronegativity occurrences in the chemical formula. In simple terms, $M(\chi)$ reflects the electronegativity of the dominant element in the composition.

Electronegativity essentially describes an element's ability to attract electrons when forming chemical bonds [72]. Elements with high electronegativity tend to bind electrons more strongly, thereby reducing the free carrier concentration and consequently decreasing electrical conductivity. By doping elements with lower elec-

tronegativity, the covalency of chemical bonds can be en- hanced, which weakens carrier-phonon coupling, leading to a lower effective mass and thus improving carrier mo- bility [73].

Although, as shown in Eq. (7), a decrease in $\sigma$ may enhance $S$, electronegativity also plays a role in modu- lating the Fermi level. A higher electronegativity of the dominant element suggests that doping enhances the p- type behavior of the material, causing the Fermi level to shift downward (closer to the valence band). This results in a slower variation of the electronic density of states, leading to a decrease in the term $\left[\frac{\mathrm{d}\sigma(E)}{\mathrm{d}E}\right]_{E=E_{F}}$, which in turn negatively impacts the Seebeck coefficients [17, 74].

Fig. 7 presents the global interpretability analysis based on SHAP, while Fig. 6 provides a local explanation for individual samples. Taking the $\mathrm{Mg}_{3.5}\mathrm{Ho}_{x}\mathrm{Sb}_{2}$ system mentioned in Sec. II A as an example, the $zT$ value of this system is primarily positively influenced by $T$ and $M(\chi)$, whereas the deviation of the average melting point of the constituent elements, $\Delta\bar{T}_{\mathrm{M}}$, exerts the most significant negative effect.

As shown in Fig. 6, the dominant factor affecting $\mathrm{Mg}_{3.5}\mathrm{Ho}_{x}\mathrm{Sb}_{2}$ is the fluctuation in the melting point caused by variations in Ho doping concentration. Specif- ically, increasing the Ho fraction by 0.01 leads to an approximately $10\%$ increase in $\Delta\bar{T}_{\mathrm{M}}$. As depicted in Fig. 7(d), under the constraint of $T=600$K, the upper limit of $zT$ appears to decrease as $\Delta\bar{T}_{\mathrm{M}}$ increases.

However, the mechanism by which $\Delta\bar{T}_{\mathrm{M}}$ influences $zT$ remains elusive. From a global perspective (Fig. 7(c)), $zT$ does not exhibit a consistent trend with $\Delta\bar{T}_{\mathrm{M}}$. There exist numerous low-$zT$ materials even when $\Delta\bar{T}_{\mathrm{M}}$ is low, while high-$zT$ materials are often associated with ele- vated $T$, showing no apparent correlation with $\Delta\bar{T}_{\mathrm{M}}$. While $\Delta\bar{T}_{\mathrm{M}}$ can be considered the dominant factor in the $\mathrm{Mg}_{3.5}\mathrm{Ho}_{x}\mathrm{Sb}_{2}$ system, its generalization to a broader scope is not justifiable.

## F. Multi-Objective Optimization using NSGA-III

Unlike traditional Genetic Algorithms (GA) [75], the NSGA-III [76] is specifically designed for MOO involving three or more objectives. In our case, to discover po- tential thermoelectric materials, the algorithm should be capable of simultaneously optimizing both the elemental composition and fraction to maximize $|S|$ and $\sigma$, while minimizing $\kappa$:

$$
\max_{\mathcal{X}}\left(|S(\mathcal{X})|,\sigma(\mathcal{X}),\frac{1}{\kappa(\mathcal{X})}\right)
\tag{9}
$$

For simplicity, we transform $\min_{\mathcal{X}}\kappa(\mathcal{X})$ into the equiv- alent maximization problem $\max_{\mathcal{X}}\frac{1}{\kappa(\mathcal{X})}$. Although it is feasible to directly optimize $zT$ as a single objective using traditional GA or Bayesian optimization, the antagonis- tic nature between $S$ and $\sigma$ (see Sec. II E) makes it im- practical to achieve simultaneously high $S$ and $\sigma$ leading to an exceptionally high $zT$. Therefore, MOO is more advantageous as it ensures the reasonableness of newly generated materials while also tracing the origins of high $zT$.

Since the set of elements and their fractions is too large to exhaustively enumerate, optimization algorithms are necessary to efficiently search the material space. NSGA- III mimics natural selection and principles of genetics, solving the problem through the simulation of biological evolution, where "individuals" gradually improve their fitness via genetic processes such as inheritance, muta- tion, and selection, ultimately finding the optimal solu- tion [76]. We transfer these genetic concepts to material design, treating a compound as an individual organism, with the elemental composition and fractions as its genes, and the material's thermoelectric properties (e.g., $|S|$, $\sigma$, and $\frac{1}{\kappa}$) as its fitness.

To identify high-performance thermoelectric materials suitable for wearable thermoelectric devices, the tem- perature domain is restricted to the range of 300 K to 310 K. In the generation of virtual materials, we select commonly used base materials and introduce dopants at compositions ranging from 0.05 to 1.0, with an incre- ment of 0.05. Candidates of base materials and dopants are summarized in Table IV.

The NSGA-III MOO framework is implemented us- ing the Python library `pymoo-0.6.1.3` [77]. For the parameter configuration of NSGA-III, Latin Hypercube Sampling (LHS) [78] is employed to ensure a uniform distribution of the initial population within the variable space, thereby enhancing diversity. The population size per generation, $T$, is set to 50, meaning that each gener- ation produces 300 candidate solutions. A larger popula- tion facilitates broader exploration of the material space but incurs higher computational costs, whereas a smaller population converges faster but risks being trapped in local optima [79]. The crossover probability ($p_c$) is set to 0.9, indicating that $90\%$ of individuals undergo crossover while $10\%$ remain unchanged—an emulation of natural reproduction processes [80]. To prevent premature con- vergence, polynomial mutation (PM) is incorporated to introduce random variations, mimicking genetic muta- tions in natural evolution [81].

Fig. 8 illustrates the Pareto-front of each generation throughout the NSGA-III optimization process, with the optimal virtual candidate set, post-merging, clearly an- notated. In Fig. 8(a), the distributions of $|S|$ and $\sigma$ for the virtual candidates generally align with those of the original dataset. However, in Fig. 8(b), the corre- sponding distributions of PF and $\kappa$ deviate significantly from the real data. Specifically, some candidates demon- strate unexpectedly elevated PF values, while all can- didates show $\kappa$ values below $2.5$ W/m/K. These ex- cessively high PF values arise from error propagation, where minor overestimations in $S$ and $\sigma$ are amplified through their multiplicative relationship. In the range of $\sigma\in[0.15\times10^{6},0.4\times10^{6}]$, several samples' objectives do not closely match the Pareto-front of the original dataset.

![](./images/1118832882618466369_8.jpg)

FIG. 8. Comparison of the Pareto-fronts before and after MOO. Different colors of circular scatter points and connecting lines represent the optimal candidates and corresponding Pareto-fronts from the initial dataset and different generations, while the black pentagram symbolizes the optimal results after merging across all generations. (a) Focuses on $S$ and $\sigma$, considering them as a unified optimization direction, with candidates selected based solely on the absolute value of $S$. (b) Focuses on PF and $\kappa$, where the candidates in the lower-left region of the gray dashed line more closely align with the Pareto-fronts of the initial dataset.

<table>
<caption>TABLE III. Pareto-optimal candidate materials after screening.</caption>
<thead>
<tr>
<th>Base</th>
<th>Formula</th>
<th>Gen.</th>
<th>Temperature</th>
<th>$S_{pred}$</th>
<th>$\sigma_{pred}$</th>
<th>PF</th>
<th>$\kappa_{pred}$</th>
<th>$zT$</th>
</tr>
</thead>
<tbody>
<tr>
<td>BiSe</td>
<td>BiSeGe$_{0.12}$Bi$_{0.37}$Y$_{0.16}$</td>
<td>2</td>
<td>600</td>
<td>-200.89</td>
<td>31664.66</td>
<td>0.00128</td>
<td>0.4427</td>
<td>1.7319</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeBi$_{0.25}$Y$_{0.18}$</td>
<td>7</td>
<td>600</td>
<td>-237.27</td>
<td>24423.96</td>
<td>0.00137</td>
<td>0.4644</td>
<td>1.7764</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeAg$_{0.32}$Bi$_{0.39}$</td>
<td>0</td>
<td>600</td>
<td>-254.01</td>
<td>35734.53</td>
<td>0.00231</td>
<td>0.4759</td>
<td>2.9070</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeSb$_{0.2}$Y$_{0.13}$Se$_{0.33}$</td>
<td>1</td>
<td>367</td>
<td>-183.36</td>
<td>71620.65</td>
<td>0.00241</td>
<td>0.4806</td>
<td>1.8373</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeAg$_{0.37}$Bi$_{0.46}$</td>
<td>6</td>
<td>600</td>
<td>-266.28</td>
<td>36687.65</td>
<td>0.00260</td>
<td>0.4839</td>
<td>3.2258</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeGe$_{0.06}$Ag$_{0.36}$Bi$_{0.39}$</td>
<td>7</td>
<td>600</td>
<td>-247.77</td>
<td>42446.70</td>
<td>0.00261</td>
<td>0.4990</td>
<td>3.1332</td>
</tr>
<tr>
<td>BiSe</td>
<td>BiSeZn$_{0.26}$Bi$_{0.50}$Ag$_{0.11}$</td>
<td>4</td>
<td>600</td>
<td>-263.10</td>
<td>39256.36</td>
<td>0.00272</td>
<td>0.5156</td>
<td>3.1620</td>
</tr>
<tr>
<td>Bi$_2$Te$_3$</td>
<td>Bi$_2$Te$_3$Y$_{0.23}$Ag$_{0.36}$</td>
<td>1</td>
<td>433</td>
<td>-228.76</td>
<td>59676.69</td>
<td>0.00312</td>
<td>0.5265</td>
<td>2.5701</td>
</tr>
<tr>
<td>Bi$_2$Te$_3$</td>
<td>Bi$_2$Te$_3$Y$_{0.44}$Sn$_{0.23}$</td>
<td>5</td>
<td>600</td>
<td>-203.63</td>
<td>81164.93</td>
<td>0.00337</td>
<td>0.6710</td>
<td>3.0094</td>
</tr>
<tr>
<td>Bi$_2$Te$_3$</td>
<td>Bi$_2$Te$_3$Sn$_{0.19}$Y$_{0.50}$</td>
<td>7</td>
<td>600</td>
<td>-210.32</td>
<td>81858.41</td>
<td>0.00362</td>
<td>0.7015</td>
<td>3.0969</td>
</tr>
<tr>
<td>Bi$_2$Te$_3$</td>
<td>Bi$_2$Te$_3$Se$_{0.18}$Y$_{0.18}$Sb$_{0.17}$</td>
<td>2</td>
<td>433</td>
<td>-219.34</td>
<td>81344.72</td>
<td>0.00391</td>
<td>0.7267</td>
<td>2.3335</td>
</tr>
<tr>
<td>Bi$_2$Te$_3$</td>
<td>Bi$_2$Te$_3$Zn$_{0.41}$Y$_{0.16}$Sb$_{0.25}$</td>
<td>4</td>
<td>433</td>
<td>-206.58</td>
<td>93000.80</td>
<td>0.00397</td>
<td>0.8109</td>
<td>2.1209</td>
</tr>
<tr>
<td>Sb$_2$Te$_3$</td>
<td>Sb$_2$Te$_3$Te$_{0.43}$Y$_{0.18}$Bi$_{0.39}$</td>
<td>7</td>
<td>300</td>
<td>233.58</td>
<td>79066.91</td>
<td>0.00431</td>
<td>0.8552</td>
<td>1.5132</td>
</tr>
<tr>
<td>Sb$_2$Te$_3$</td>
<td>Sb$_2$Te$_3$Te$_{0.43}$Y$_{0.18}$Bi$_{0.39}$</td>
<td>7</td>
<td>333</td>
<td>232.67</td>
<td>79952.61</td>
<td>0.00433</td>
<td>0.8796</td>
<td>1.6403</td>
</tr>
</tbody>
</table>

Although the individual predictions for $\sigma$ and $S$ are reliable, the error in $PF=S^2\sigma$ is substantially magnified. As observed during surrogate model training (see Fig. 4) and transfer learning (see Fig. 5), the model's accuracy for $\kappa$ estimation is the lowest. Consequently, in Fig. 8(b), only the candidates in the lower-left region of the gray dashed line are considered to have validation value. The remaining samples, which display unrealistically high PF values and relatively low $\kappa$, significantly diverge from the distribution of the original dataset and, therefore, do not hold reference value.

Table III summarizes the screened Pareto-optimal candidate materials, all exhibiting PF values above $0.001\ \text{W/m/K}^2$, $\kappa$ below $1.0\ \text{W/m/K}$, and $zT$ exceeding 1.5, with most surpassing 2.0. Despite promising predictions, model uncertainty may lead to deviations in actual performance, necessitating experimental validation.

The candidates are primarily derived from BiSe, Bi$_2$Te$_3$, and Sb$_2$Te$_3$, with only Sb$_2$Te$_3$-based compounds being $p$-type. To differentiate hosts from dopants, identical elements in the formulas were not merged. Considering material cost, Te-containing candidates were excluded. Among the BiSe-based materials, BiSeSb0.2Y0.13Se$_{0.33}$, which achieves a peak $zT$ at 367 K, is selected for experimental validation due to its excellent performance without relying on high-temperature operation.

Here, the formula "BiSeSb0.2Y0.13Se$_{0.33}$" was equivalently replaced with "Bi$_{0.75}$Sb$_{0.15}$Y$_{0.10}$Se" for easier synthesis. As shown in Fig. 9, the measured $zT$ of Bi$_{0.75}$Sb$_{0.15}$Y$_{0.10}$Se at $T=363$ K was 0.91, which is much lower than the predicted value of 1.76. However, this material still demonstrates excellent thermoelectric performance, with a $zT$ at around 360 K that surpasses recent $n$-type materials such as Ag$_8$SiSe$_6$ ($\sim$0.65 at 360 K) [82],

<table>
<caption>TABLE IV. Multi-objective optimization (MOO) parameters.</caption>
<thead>
  <tr>
    <th>MOO Parameters</th>
    <th>Value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Population size</td>
    <td>$N = 300$</td>
  </tr>
  <tr>
    <td>Generations</td>
    <td>$T = 10$</td>
  </tr>
  <tr>
    <td>Crossover rate</td>
    <td>$p_c = 0.9$</td>
  </tr>
  <tr>
    <td>Polynomial mutation</td>
    <td>$\eta = 20$</td>
  </tr>
  <tr>
    <td>Reference direction</td>
    <td>$H = 12$</td>
  </tr>
  <tr>
    <td>Sampling</td>
    <td>LHS</td>
  </tr>
  <tr>
    <td>Base materials</td>
    <td>$\text{Bi}_2\text{Te}_3$, $\text{Sb}_2\text{Te}_3$, PbTe, SnTe, GeTe, SiGe, $\text{Mg}_2\text{Si}$, BiSe</td>
  </tr>
  <tr>
    <td>Dopants</td>
    <td>Bi, Sb, Te, Se, Sn, Pb, Ag, Cu, Ge, Zn, Y</td>
  </tr>
  <tr>
    <td>Temperature</td>
    <td>[300, 600]</td>
  </tr>
</tbody>
</table>

![](./images/1118832882618466369_9.jpg)

FIG. 9. Comparison of the predicted and measured $zT$ values for $\text{BiSeSb}_{0.2}\text{Y}_{0.13}\text{Se}_{0.33}$ ($\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$). The predicted $zT$ is obtained from the WaveTENet model, while the measured value is derived from experimental data.

$\text{Pb}_{1.006}\text{S}_{0.6}\text{Se}_{0.4}$ ($< 0.5$ at 360 K) [83], and $\text{Mg}_3\text{SbBi}$ ($< 0.8$ at 360 K) [84]. In addition to its high $zT$ value, $\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$ also features a relatively simple synthesis process (see Sec. IV D), along with advantages such as low cost and environmental friendliness, making it a promising candidate for practical applications.

Although the deep learning model is subject to uncertainty and has overestimated the $zT$ value of $\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$, it has accurately captured the temperature dependence of its thermoelectric performance, namely, the trend of $zT$ increasing and then decreasing over the range of 303–573 K. The prediction uncertainty arises not only from the inherent limitations of the model itself but also from the lack of representation of synthesis conditions. Even with identical chemical compositions, different synthesis methods can lead to nonnegligible variations in material performance [85–87].

### III. DISCUSSION

This work demonstrates a deep learning model called WaveTENet, which innovatively leverages wavelet transforms for feature enhancement, enabling it to accurately capture both local and global characteristics of materials. This approach significantly mitigates the interference caused by the nonlinear effects between material composition and performance on predictions. To the best of our knowledge, WaveTENet achieves state-of-the-art performance in predicting the thermoelectric properties of doped materials. Furthermore, through sensitivity analysis, we have investigated the impact of the electronegativity and melting point deviation of the constituent elements on thermoelectric performance, enhancing the model’s physical interpretability. Considering the potential antagonistic relationship between key properties, we select NSGA-III as the optimization algorithm, performing multi-objective collaborative optimization on $S$, $\sigma$, and $\kappa$, which ultimately identifies a series of promising candidates with excellent thermoelectric performance. Considering preparation difficulty and application value, we chose $\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$ for experimental validation. Although its actual $zT$ values is lower than predicted, it still demonstrates superior thermoelectric performance, surpassing many commercial $n$-type thermoelectric materials.

Certainly, the predictions made by WaveTENet inevitably involve some degree of uncertainty. On one hand, achieving perfect predictions through deep learning remains impractical at present; on the other hand, the existing data lacks characterization of material fabrication processes, leading us to make necessary simplifications in this work. However, as of now, WaveTENet still represents an efficient and relatively accurate method for predicting the thermoelectric properties of doped materials, and the surrogate model-based MOO framework also provides valuable insights for materials inverse design.

### IV. METHODS

#### A. System-Identified Material Descriptor

As presented in Eq. (2), the SIMD vector consists of $\mathbf{x}_s$, $\mathbf{c}_s$, $\mathbf{w}_s^{(K)}$, and $\mathbf{w}_s^{(K)}$. Specifically, $\mathbf{x}_s$ encodes the elemental fractions in the material composition using a sparse representation:

$$
x_i = 
\begin{cases}
r_e, & \text{if } i = n_e \text{ and } e \in s, \\
0, & \text{otherwise}.
\end{cases} \tag{10}
$$

in this formula, $e$ denotes an element in the composition $s$, $r_e$ represents its fraction, and $n_e$ corresponds to its atomic number. The SIMD framework [29] accounts for 100 elements, spanning from H to Fm. The vector $\mathbf{c}_s$ represents the conditional vector, which, in principle, can incorporate information related to material synthesis, such

as temperature, pressure, and cooling time. However, the ESTM and UCSB datasets provide only temperature in- formation, making $\mathbf{c}_{s}$ an $n \times 1$ vector. Together, $\mathbf{x}_{s}$ and $\mathbf{c}_{s}$ determine the system vector $\mathbf{w}_{s}^{(K)}$:

$$
\left[\begin{array}{cccccc}
x_{11} & \cdots & x_{1 M} & c_{11} & \cdots & c_{1 L} \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
x_{|u| 1} & \cdots & x_{|u| M} & c_{|u| 1} & \cdots & c_{|u| L}
\end{array}\right]\left[\begin{array}{c}
w_{1} \\
\vdots \\
w_{d}
\end{array}\right]=\left[\begin{array}{c}
y_{1} \\
\vdots \\
y_{|u|}
\end{array}\right] \quad(11)
$$

here $|u|$ denotes the number of materials in cluster $u$, and $\dagger$ represents the target property. The solution of Eq. (11), $\mathbf{w}=\left[w_{1}, \ldots, w_{d}\right]^{\mathrm{T}}$, has a dimensionality of $d=M+L$, corresponding to the combined dimensions of $\mathbf{x}_{s}$ and $\mathbf{c}_{s}$. Notably, $\mathbf{w}$ represents only the system vector of a single cluster, while $\mathbf{w}_{s}^{(K)}$ further incorporates information from the $K$ nearest clusters to enhance representation:

$$
\mathbf{w}_{s}^{(K)}=\sum_{u \in \mathcal{N}_{s}} \frac{\frac{1}{r\left(a_{u}, a_{s}\right)}}{\sum_{h \in \mathcal{N}_{s}} \frac{1}{r\left(a_{h}, a_{s}\right)}} \mathbf{w}^{(u)} \quad(12)
$$

where $\mathcal{N}_{s}$ denotes the set of $K$ nearest material clusters to the current cluster. The vector $a_{h}$ represents the anchor point of a material cluster in the anchor space, while $a_{s}$ corresponds to the anchor point of the input composition $s$. The influence of samples from different clusters on the current cluster $u$ is quantified using a distance function $r(\cdot)$, which measures geometric proximity.

The target statistical vector $\mathbf{v}$ comprises the mean, standard deviation, minimum, and maximum of the tar- get properties within a material cluster. It is formally defined as:

$$
v=\left[\bar{y}, y_{\sigma}, y_{\min }, y_{\max }\right] \quad(13)
$$

where $\bar{y}=\frac{1}{|u|} \sum_{i=1}^{|u|} y_{i}$ represents the mean target property, $y_{\sigma}=\sqrt{\frac{\sum_{i=1}^{|u|}\left(y_{i}-\bar{y}\right)^{2}}{|u|}}$ denotes the standard deviation, and $y_{\min }$ and $y_{\max }$ correspond to the minimum and maximum values within the target set $\left\{y_{1}, y_{2}, \ldots, y_{|u|}\right\}$, respectively. Similar to Eq. (12), the target statistical vector is also processed in the anchor space:

$$
\mathbf{v}_{s}^{(K)}=\sum_{u \in \mathcal{N}_{s}} \frac{\frac{1}{r\left(a_{u}, a_{s}\right)}}{\sum_{h \in \mathcal{N}_{s}} \frac{1}{r\left(a_{h}, a_{s}\right)}} \mathbf{v}^{(u)} \quad(14)
$$

Ultimately, the SIMD-generated vector conforms to the structure of Eq. (2).

The Materials-Agnostic Platform for Informatics and Exploration (Magpie) [44] descriptor enables the quanti- tative identification of physical and chemical properties based solely on elemental composition, without consider- ing material structure. These properties include, but are not limited to, stoichiometric attributes, elemental prop- erties, and ionization characteristics. The specific feature types used in this study are detailed in the Supplemen- tary Information.

### B. Discrete Wavelet Transformation

The DWT is a widely used technique for multi- resolution analysis, enabling the decomposition of sig- nals into localized time-frequency components. Unlike Fourier transform, which provides only frequency-domain representation, DWT retains both time and frequency information, making it well-suited for feature extraction in structured data. In this study, we employ the Haar wavelet [48], the simplest and most computationally effi- cient wavelet, to enhance feature representation.

DWT decomposes an input signal $x[n]$ into two sets of coefficients at each level:

- The approximation coefficients $a_{j}$, which capture low-frequency components and preserve the overall trend, and
- The detail coefficients $d_{j}$, which highlight high- frequency variations and fine details. The trans- formation is performed using a low-pass filter $h[n]$ and a high-pass filter $g[n]$, followed by a downsampling operation:

The defination of DWT can be expressed as:

$$
a_{j}[k]=\sum_{n} x[n] h[2 k-n] \quad(15)
$$

$$
d_{j}[k]=\sum_{n} x[n] g[2 k-n] \quad(16)
$$

For the Haar wavelet, the filters are defined as:

$$
h[n]=\frac{1}{\sqrt{2}}[1,1] \quad(17)
$$

$$
g[n]=\frac{1}{\sqrt{2}}[1,-1] \quad(18)
$$

which ensures efficient decomposition while preserving key structural information.

In our approach, each feature undergoes a single-level Haar wavelet decomposition. The resulting approxima- tion and detail coefficients are concatenated with the original feature set to enrich the representation. This augmentation process effectively increases feature diver- sity while maintaining computational efficiency. The choice of a single-level decomposition is based on em- pirical validation, ensuring that essential information is retained without introducing excessive redundancy.

In our work, the choice of DWT over the Fast Fourier Transform (FFT) [88], which is also suitable for discrete signals, is due to DWT's superior capability in detecting transient signal changes [89]. Both SIMD and Magpie descriptors exhibit sparsity, particularly in the element fraction encoding of SIMD and the one-hot vector com- ponent of Magpie. Furthermore, the differences between materials in the same doped system are subtle in terms of their descriptors, and DWT is better suited for capturing high-frequency variations than FFT [90].

### C. SHAP Index

The SHAP values are computed following the method proposed by Lundberg and Lee [64] and implemented using the `shap` package in Python. SHAP, derived from game theory's Shapley values, is a model interpretability approach that quantifies each player's contribution to the overall outcome. In this work we leverage SHAP values to assess the contribution of individual Magpie descriptors $\mathcal{M} \in \mathcal{N} = \{1,2,\cdots,N\}$ to the predicted $zT$ value. For this purpose, the "players" are abstracted as different descriptor dimensions, while the "outcome" corresponds to the $zT$ value. The Shapley value is computed as follows:

$$
\begin{aligned}
\phi_{j}= & \sum_{\mathcal{M} \subseteq \mathcal{N} \backslash\{j\}} \frac{|\mathcal{M}|!(N-|\mathcal{M}|-1)!}{N!}[v(\mathcal{M} \cup\{j\})-v(\mathcal{M})] \\
& j=1, \ldots, N.
\end{aligned}
\tag{19}
$$

where $|\mathcal{M}|$ represents the dimensionality of the feature vector [91]. $v(\mathcal{M})$ represents the contribution value, i.e., the expected model output given a specific feature subset $\mathcal{M}$. It quantifies the extent to which the subset $\mathcal{M}$ influences the model's prediction. Given a surrogate model $zT(\mathcal{X})$, $v(\mathcal{M})$ can be formally expressed as:

$$
z T\left(\mathcal{X}^{*}\right)=\phi_{0}+\sum_{j=1}^{N} \phi_{j}^{*}
\tag{20}
$$

$$
v(\mathcal{M})=E\left[z T(\mathcal{X}) \mid \mathcal{X}_{\mathcal{M}}=\mathcal{X}_{\mathcal{M}}^{*}\right]
\tag{21}
$$

in the above equations, $\phi_{0}$ represents the mean Shapley value of the surrogate model $zT(\mathcal{X})$, which is also the model's average prediction. The term $\mathcal{X}^{*}$ refers to a specific selected feature subset, and $\phi_{j}^{*}$ denotes the Shapley value of the $j$th feature when $\mathcal{X}=\mathcal{X}^{*}$. This process is more intuitively illustrated in Fig. 6, where the "base_value" corresponds to the mean predicted $zT$ value of the surrogate model, i.e., $\phi_{0}$. Under the interplay of multiple features such as $M(\chi)$ and $T$, each with their respective Shapley values $\phi_{j}$, the model's specific prediction is determined [92].

### D. Synthesis methodology of $\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$

The $\text{Bi}_{0.75}\text{Sb}_{0.15}\text{Y}_{0.10}\text{Se}$ compound was synthesized using bismuth (Bi, Afla Aesar, 99.99%, granules), antimony (Sb, Afla Aesar, 99.99%, powder), yttrium (Y, Afla Aesar, 99.99%, powder), and selenium (Se, Afla Aesar, 99.99%, powder) as raw materials. These compounds were prepared by high-energy ball milling for 10 hours in a stainless steel ball mill jar under a pure argon atmosphere. The synthesized powder samples were examined using an X-ray diffractometer (XRD, Rigaku Corporation, Japan), and the peak positions of the samples were compared to standard cards using the Jade 6 program.

### E. Pseudocode of NSGA-III

```
Algorithm 1: NSGA-III for Multi-objective thermoelectric Material Optimization
Input: Population size $N=300$, generations
       $T=10$, crossover rate $p_{\mathrm{c}}=0.9$,
       polynomial mutation PM ($\eta=20$),
       reference directions $H=12$
Output: Pareto-front $\mathcal{P}^{*}$, optimal composition
        $\mathcal{X}^{*}$
1 Step 1: Initialization
    • Generate $H$ reference directions $\boldsymbol{w}_{1},...,\boldsymbol{w}_{H}$;
    • Initialize population $P_{0}$ of size $N$ via LHS;

for $t=1$ to $T$ do
    foreach $\mathcal{X} \in P_{t}$ do
        Evaluate objectives using surrogate models:
        $$
        \boldsymbol{f}(\mathcal{X})=\left[S(\mathcal{X}), \sigma(\mathcal{X}), \frac{1}{\kappa(\mathcal{X})}\right]^{T}
        $$

    Step 2: Non-dominated Sorting
    Partition $P_{t}$ into Pareto-fronts $\mathcal{F}_{1},\mathcal{F}_{2},...$;
    Step 3: Reference Direction Association
    Assign each $\mathcal{X}$ to the closest $\boldsymbol{w}_{h}$ based on
    perpendicular distance:
    $$
    d\left(\boldsymbol{f}(\mathcal{X}), \boldsymbol{w}_{h}\right)=\left\|\boldsymbol{f}(\mathcal{X})-\frac{\boldsymbol{f}(\mathcal{X})^{T} \boldsymbol{w}_{h}}{\left\|\boldsymbol{w}_{h}\right\|^{2}} \boldsymbol{w}_{h}\right\|
    $$

    Step 4: Environmental Selection
    Construct $P_{t+1}$ by selecting from $\mathcal{F}_{1},\mathcal{F}_{2},....$ If
    a front exceeds capacity, prioritize solutions
    maximizing:
    $$
    \max_{\mathcal{X}^{*}}\left(S(\mathcal{X}^{*}), \sigma(\mathcal{X}^{*}), \frac{1}{\kappa(\mathcal{X}^{*})}\right)
    $$
    while maintaining diversity across $\boldsymbol{w}_{h}$;
    Step 5: Variation
        • Select parents via tournament selection;
        • Apply SBX ($p_{\mathrm{c}}=0.9$) for crossover;
        • Apply polynomial mutation ($\eta=20$) for
          diversity;
        • Generate offspring population $Q_{t}$;

    Step 6: Population Update
    Merge parent and offspring populations:
        $P_{t+1} = \text{EnvironmentalSelection}(P_{t} \cup Q_{t}, N)$

return $\mathcal{P}^{*}=\mathcal{F}_{1}$, $\mathcal{X}^{*}$;
```

### F. Details about WaveTENet

For regression problems, the structure of a dataset $\mathcal{I}$ with $N$ samples can be summarized as:

$$
\mathcal{I} = \{\mathcal{X}_i, (y_i^S, y_i^\sigma, y_i^\kappa) \mid 1 \leq i \leq N\} \tag{22}
$$

For the sake of integration, we incorporate the feature generation and wavelet transform modules into the WaveTENet network, as outlined in Algorithm 2.

```
Algorithm 2: WaveTENet Feature Construction
 Input: Chemical formula $\mathcal{F}$, e.g., $\text{Mg}_{3.5}\text{H}_{0.01}\text{Sb}_2$
 Output: Normalized feature vector $\mathcal{X}$
1 Step 1: Generate Descriptors
2    Extract SIMD descriptor:

               $\mathcal{S} = \text{SIMD}(\mathcal{F})$

    Extract Magpie descriptor:

               $\mathcal{M} = \text{Magpie}(\mathcal{F})$

3    Concatenate SIMD and Magpie descriptors:

               $\mathcal{V} = \mathcal{S} \oplus \mathcal{M}$

4 Step 2: Apply Haar Wavelet Transform
5    Compute high-frequency coefficients:

               $\mathcal{D} = \text{HaarHigh}(\mathcal{V})$

    Compute low-frequency coefficients:

               $\mathcal{A} = \text{HaarLow}(\mathcal{V})$

6 Step 3: Concatenate All Features

               $\mathcal{X} = \mathcal{S} \oplus \mathcal{M} \oplus \mathcal{A} \oplus \mathcal{D}$

8 Step 4: Normalize Feature Vector

               $\mathcal{X} = \text{MinMaxNormalize}(\mathcal{X})$

10 return $\mathcal{X}$
```

The objective of the WaveTENet is to minimize the error function to fit the mapping between features and targets, a process typically achieved through backpropagation. Additionally, to prevent overfitting, $\ell_2$ regularization is applied to enhance model robustness. The error function of WaveTENet can be expressed as:

$$
\mathcal{L} = \frac{1}{N} \sum_{i=1}^N [y_i - f(\mathcal{X}_i; \theta)]^2 + \lambda \sum_j \|\theta_j\|^2 \tag{23}
$$

where $f(\mathcal{X}_i; \theta)$ represents the model's prediction given parameters $\theta$ and input features $\mathcal{X}_i$, $\lambda$ is the decay coefficient for $\ell_2$ regularization, and $\sum_j \|\theta_j\|^2$ denotes the sum of the squared $\ell_2$ norms of all model parameters. Algorithm 3 describes the forward and backward propagation of WaveTENet to achieve target prediction and parameter optimization, respectively.

```
Algorithm 3: WaveTENet Backpropagation
 Input: Training data $(\mathcal{X}, y)$, learning rate $\alpha$,
        weight decay $\lambda$, number of epochs $T$
 Output: Optimized model parameters $\theta$
1 for $t = 1$ to $T$ do
2    Step 1: Forward Pass
3    foreach $(\mathcal{X}_i, y_i) \in (\mathcal{X}, y)$ do
4        | Compute input transformation:

               $\mathcal{H}^{(0)} = \text{ReLU}(\text{BN}(\mathcal{W}_0\mathcal{X}_i + \boldsymbol{b}_0))$

5        | for $l = 1$ to $L$ do
6        |    | Compute dense block output:

               $\mathcal{H}^{(l)} = \text{ReLU}(\text{Dropout}(\text{BN}(\mathcal{W}_l\mathcal{H}^{(l-1)}+\boldsymbol{b}_l)))$

            Residual connection:

               $\mathcal{H}^{(l)} = \mathcal{H}^{(l)} + \mathcal{H}^{(l-1)}$

7        | Compute final output:

               $\hat{y}_i = \mathcal{W}_{\text{out}}\mathcal{H}^{(L)} + \boldsymbol{b}_{\text{out}}$

8    Step 2: Compute Loss

               $\mathcal{L} = \frac{1}{N} \sum_{i=1}^N [y_i - \hat{y}_i]^2 + \lambda \sum_j \|\theta_j\|^2$

10   Step 3: Backpropagation
11   foreach layer $l$ from $L$ to $0$ do
12       | Compute gradients:

               $\frac{\partial \mathcal{L}}{\partial \mathcal{W}_l} = \frac{1}{N} \sum_{i=1}^N 2(y_i - \hat{y}_i)(-\mathcal{H}^{(l)}) + \lambda \mathcal{W}_l$

               $\frac{\partial \mathcal{L}}{\partial \boldsymbol{b}_l} = \frac{1}{N} \sum_{i=1}^N 2(y_i - \hat{y}_i)(-1)$

13   Step 4: Update Parameters
14   foreach parameter $\theta_j \in \{\mathcal{W}_l, \boldsymbol{b}_l\}$ do
15       |

               $\theta_j = \theta_j - \alpha \frac{\partial \mathcal{L}}{\partial \theta_j}$

16 return Optimized parameters $\theta$
```

## V. DATA AVAILABILITY

The ESTM (for models training) and UCSB (for transfer learning) datasets can be accessed via our GitHub repository at https://github.com/FlorianTseng/WaveTENet.

## VI. CODE AVAILABILITY

The codes supporting our research are available at https://github.com/FlorianTseng/WaveTENet.

## VII. COMPETING INTERESTS

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## ACKNOWLEDGMENTS

We would like to acknowledge the National Key Research and Development Program of China (Grant No. 2023YFB4603800), the financial support from the project of the National Natural Science Foundation of China (Grants No.12404062, No.12474093, No.12302220, No.12374091), Translational Medicine and Interdisciplinary Research Joint Fund of Zhongnan Hospital of Wuhan University (Grant NO.ZNJC202235), and the Fundamental Research Funds for the Central Universities (Grant No.2042023kf0109). The numerical calculations in this work have been done on the supercomputing system in the Supercomputing Center of Wuhan University.

[1] Zhang, H. & Talapin, D. V. Thermoelectric tin selenide: The beauty of simplicity. Angew. Chem., Int. Ed. Engl 53, 9126-9127 (2014).

[2] Hasan, M. N., Nafea, M., Nayan, N. & Mohamed Ali, M. S. Thermoelectric generator: materials and applications in wearable health monitoring sensors and internet of things devices. Advanced Materials Technologies 7, 2101203 (2022).

[3] Bu, Z. et al. A record thermoelectric efficiency in tellurium-free modules for low-grade waste heat recovery. Nature communications 13, 237 (2022).

[4] Siddique, A. R. M., Mahmud, S. & Van Heyst, B. A review of the state of the science on wearable thermoelectric power generators (tegs) and their existing challenges. Renewable and Sustainable Energy Reviews 73, 730-744 (2017).

[5] Pei, J., Cai, B., Zhuang, H.-L. & Li, J.-F. Bi2te3-based applied thermoelectric materials: research advances and new challenges. National science review 7, 1856-1858 (2020).

[6] Bano, S. et al. Room temperature bi2te3-based thermoelectric materials with high performance. Journal of Materials Science: Materials in Electronics 31, 8607-8617 (2020).

[7] Xiao, Y. & Zhao, L.-D. Charge and phonon transport in pbte-based thermoelectric materials. npj Quantum Materials 3, 55 (2018).

[8] Goyal, A., Gorai, P., Toberer, E. S. & Stevanović, V. First-principles calculation of intrinsic defect chemistry and self-doping in pbte. npj Computational Materials 3, 42 (2017).

[9] Toko, K. et al. Layer exchange synthesis of sige for flexible thermoelectric generators: A comprehensive review. Advanced Electronic Materials 10, 2400130 (2024).

[10] Zhang, H. & Talapin, D. V. Thermoelectric tin selenide: The beauty of simplicity. Angewandte Chemie International Edition 53, 9126-9127 (2014). URL https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201405683. https://onlinelibrary.wiley.com/doi/pdf/10.1002/anie.201405683.

[11] Yang, C.-Y. et al. Enhancing the n-type conductivity and thermoelectric performance of donor-acceptor copolymers through donor engineering. Advanced Materials 30, 1802850 (2018).

[12] Lv, H., Lu, W., Shao, D. & Sun, Y. Enhanced thermoelectric performance of phosphorene by strain-induced band convergence. Physical Review B 90, 085433 (2014).

[13] Pei, Y., Wang, H. & Snyder, G. J. Band engineering of thermoelectric materials. Advanced materials 24, 6125-6135 (2012).

[14] Zheng, Y. et al. Defect engineering in thermoelectric materials: what have we learned? Chemical Society Reviews 50, 9022-9054 (2021).

[15] Lany, S. & Zunger, A. Accurate prediction of defect properties in density functional supercell calculations. Modelling and simulation in materials science and engineering 17, 084002 (2009).

[16] Kang, J., Zhang, X. & Wei, S.-H. Advances and challenges in dft-based energy materials design. Chinese Physics B 31, 107105 (2022).

[17] Chen, S., Cai, K. & Zhao, W. The effect of te doping on the electronic structure and thermoelectric properties of snse. Physica B: Condensed Matter 407, 4154-4159 (2012).

[18] Fang, H., Demir, H., Kamakoti, P. & Sholl, D. S. Recent developments in first-principles force fields for molecules in nanoporous materials. Journal of Materials Chemistry A 2, 274-291 (2014).

[19] Millett, P. C., Selvam, R. P. & Saxena, A. Molecular dynamics simulations of grain size stabilization in nanocrystalline materials by addition of dopants. Acta materialia 54, 297-303 (2006).

[20] Zeng, Y. et al. A machine learning-based framework for predicting the power factor of thermoelectric materials. Applied Materials Today 43, 102627 (2025). URL https://www.sciencedirect.com/science/article/pii/S2352940725000460.

[21] Antunes, L., Butler, K. & Grau-Crespo, R. Predict- ing thermoelectric transport properties from composition with attention-based deep learning. Machine Learning: Science and Technology 4 (2023).

[22] Luo, Y., Li, M., Yuan, H., Liu, H. & Fang, Y. Predicting lattice thermal conductivity via machine learning: a mini review. npj Computational Materials 9, 4 (2023).

[23] Jain, A. et al. The materials project: Accelerating mate- rials design through theory-driven data and tools. Hand- book of Materials Modeling: Methods: Theory and Mod- eling 1751–1784 (2020).

[24] Curtarolo, S. et al. Aflow: An automatic framework for high-throughput materials discovery. Computational Ma- terials Science 58, 218–226 (2012).

[25] Sheng, Y. et al. Active learning for the power factor prediction in diamond-like thermoelectric materials. npj Computational Materials 6, 171 (2020).

[26] Na, G. S., Jang, S. & Chang, H. Predicting thermo- electric properties from chemical formula with explicitly identifying dopant effects. npj Computational Materials 7, 106 (2021).

[27] Parse, N. & Pinitsoontorn, S. Machine learning for predicting zt values of high-performance thermoelectric materials in mid-temperature range. APL Materi- als 11, 081117 (2023). URL https://doi.org/10. 1063/5.0160055. https://pubs.aip.org/aip/apm/article- pdf/doi/10.1063/5.0160055/18091313/081117_1.5.0160055.pdf

[28] Parse, N. & Pinitsoontorn, S. https://ml-te-app. herokuapp.com/.

[29] Na, G. S. & Chang, H. A public database of thermo- electric materials and system-identified material repre- sentation for data-driven discovery. npj Computational Materials 8, 214 (2022).

[30] Guo, T., Wu, L. & Li, T. Machine learning accelerated, high throughput, multi-objective optimization of multi- principal element alloys. Small 17, 2102972 (2021).

[31] Wen, C. et al. Machine-learning-assisted com- positional design of refractory high-entropy alloys with optimal strength and ductility. Engineer- ing (2024). URL https://www.sciencedirect.com/ science/article/pii/S2095809924005113.

[32] Khatamsaz, D. et al. Multi-objective materials bayesian optimization with active learning of design constraints: Design of ductile refractory multi-principal-element al- loys. Acta Materialia 236, 118133 (2022).

[33] Heid, R. Electron-phonon coupling. Lecture Notes of the Autumn School on Correlated Electrons; Pavarini, E., Koch, E., Scalettar, R., Martin, R., Eds 399–427 (2017).

[34] Al Qori', M. D. et al. The effect of ti doping on the ther- moelectric performance of bi2te3 and its chemical stabil- ity. Journal of Materials Engineering and Performance 33, 7265–7276 (2024).

[35] Bernazzani, L., Marchegiani, G., Giazotto, F., Roddaro, S. & Braggio, A. Bipolar thermoelectricity in bilayer- graphene-superconductor tunnel junctions. Physical re- view applied 19, 044017 (2023).

[36] Humaira, H. & Rasyidah, R. Determining the appropri- ate cluster number using elbow method for k-means al- gorithm. In Proceedings of the 2nd Workshop on Multi- disciplinary and Applications (WMA), 1–8 (2020).

[37] Aversano, F. et al. Effect of rapid solidification on the synthesis and thermoelectric properties of yb-filled co4sb12 skutterudite. Journal of Alloys and Compounds 796, 33–41 (2019).

[38] Shi, X., Wang, X., Li, W. & Pei, Y. Advances in ther- moelectric mg3sb2 and its derivatives. Small Methods 2, 1800022 (2018).

[39] Choudhary, K. et al. The joint automated repository for various integrated simulations (jarvis) for data-driven materials design. npj Computational Materials 6, 173 (2020).

[40] Himanen, L. et al. Dscribe: Library of descriptors for machine learning in materials science. Computer Physics Communications 247, 106949 (2020).

[41] Pham, T. L. et al. Machine learning reveals orbital inter- action in materials. Science and technology of advanced materials 18, 756 (2017).

[42] Zhou, Q. et al. Learning atoms for materials discovery. Proceedings of the National Academy of Sciences 115, E6411–E6417 (2018).

[43] Tshitoyan, V. et al. Unsupervised word embeddings cap- ture latent knowledge from materials science literature. Nature 571, 95–98 (2019).

[44] Ward, L., Agrawal, A., Choudhary, A. & Wolverton, C. A general-purpose machine learning framework for predict- ing properties of inorganic materials. npj Computational Materials 2, 1–7 (2016).

[45] Bentley, P. M. & McDonnell, J. Wavelet transforms: an introduction. Electronics & communication engineering journal 6, 175–186 (1994).

[46] Sundararajan, D. Discrete wavelet transform: a signal processing approach (John Wiley & Sons, 2016).

[47] Struzik, Z. R. & Siebes, A. The haar wavelet transform in the time series similarity paradigm. In European Confer- ence on Principles of Data Mining and Knowledge Dis- covery, 12–22 (Springer, 1999).

[48] Lepik, Ü. & Hein, H. Haar wavelets. In Haar wavelets: with applications, 7–20 (Springer, 2014).

[49] Leavey, C. M., James, M. N., Summerscales, J. & Sutton, R. An introduction to wavelet transforms: a tutorial ap- proach. Insight-Non-Destructive Testing and Condition Monitoring 45, 344–353 (2003).

[50] Furusho, Y. & Ikeda, K. Theoretical analysis of skip connections and batch normalization from generalization and optimization perspectives. APSIPA Transactions on Signal and Information Processing 9, e9 (2020).

[51] Ioffe, S. & Szegedy, C. Batch normalization: Accelerat- ing deep network training by reducing internal covariate shift. In International conference on machine learning, 448–456 (pmlr, 2015).

[52] Daneshmand, H., Kohler, J., Bach, F., Hofmann, T. & Lucchi, A. Batch normalization provably avoids ranks collapse for randomly initialised deep networks. Advances in Neural Information Processing Systems 33, 18387–18398 (2020).

[53] Gal, Y. & Ghahramani, Z. A theoretically grounded application of dropout in recurrent neural networks. Advances in neural information processing systems 29 (2016).

[54] He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learn- ing for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, 770–778 (2016).

[55] Lee, J. K. et al. Control of carrier concentration by ag doping in n-type bi2te3 based compounds. Ap- plied Sciences 8 (2018). URL https://www.mdpi.com/2076-3417/8/5/735.

[56] Gupta, S., Agrawal, A., Gopalakrishnan, K. & Narayanan, P. Deep learning with limited numerical pre- cision. In *International conference on machine learning*, 1737–1746 (PMLR, 2015).

[57] Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V. & Gulin, A. Catboost: unbiased boosting with categorical features. *Advances in neural information pro- cessing systems* **31** (2018).

[58] Akiba, T., Sano, S., Yanase, T., Ohta, T. & Koyama, M. Optuna: A next-generation hyperparameter opti- mization framework. In *Proceedings of the 25th ACM SIGKDD international conference on knowledge discov- ery & data mining*, 2623–2631 (2019).

[59] Grinsztajn, L., Oyallon, E. & Varoquaux, G. Why do tree-based models still outperform deep learning on typi- cal tabular data? In *Proceedings of the 36th International Conference on Neural Information Processing Systems*, NIPS'22 (Curran Associates Inc., Red Hook, NY, USA, 2022).

[60] Xia, J. *et al.* Understanding the limitations of deep mod- els for molecular property prediction: Insights and solu- tions. In *Thirty-seventh Conference on Neural Informa- tion Processing Systems* (2023).

[61] Zeng, Y. *et al.* Exploring lattice thermal conductivity models via interpretable deep learning to accelerate ma- terials discovery (2025). URL https://arxiv.org/abs/ 2412.05948. 2412.05948.

[62] Gaultois, M. W. *et al.* Data-driven review of thermoelec- tric materials: performance and resource considerations. *Chemistry of Materials* **25**, 2911–2920 (2013).

[63] Li, Y. *et al.* Large data set-driven machine learning mod- els for accurate prediction of the thermoelectric figure of merit. *ACS Applied Materials & Interfaces* **14**, 55517–55527 (2022).

[64] Lundberg, S. M. & Lee, S.-I. A unified approach to inter- preting model predictions. In *Proceedings of the 31st In- ternational Conference on Neural Information Processing Systems*, NIPS'17, 4768–4777 (Curran Associates Inc., Red Hook, NY, USA, 2017).

[65] Aas, K., Jullum, M. & Løland, A. Explaining individual predictions when features are dependent: More accurate approximations to shapley values. *Artificial Intelligence* **298**, 103502 (2021). URL https://www.sciencedirect. com/science/article/pii/S0004370221000539.

[66] Pei, Y., Wang, H. & Snyder, G. J. Band engineering of thermoelectric materials. *Advanced Materials* **24**, 6125–6135 (2012). URL https://advanced.onlinelibrary. wiley.com/doi/abs/10.1002/adma.201202919. https://advanced.onlinelibrary.wiley.com/doi/pdf/10.1002/adma.201202919.

[67] Buhmann, J. M. & Sigrst, M. Thermoelectric effect of correlated metals: Band-structure effects and the break- down of mott's formula. *Physical Review B—Condensed Matter and Materials Physics* **88**, 115128 (2013).

[68] Klaassen, D. A unified mobility model for device simulation—ii. temperature dependence of carrier mo- bility and lifetime. *Solid-State Electronics* **35**, 961–967 (1992). URL https://www.sciencedirect.com/ science/article/pii/0038110192903268.

[69] McLean, T. & Paige, E. A theory of the effects of carrier-carrier scattering on mobility in semiconductors. *Journal of Physics and Chemistry of Solids* **16**, 220–236 (1960). URL https://www.sciencedirect.com/ science/article/pii/0022369760901529.

[70] Skoug, E. J., Zhou, C., Pei, Y. & Morelli, D. T. High thermoelectric power factor near room temperature in full-heusler alloys. *Journal of electronic materials* **38**, 1221–1223 (2009).

[71] Holland, M. Thermal conductivity. In *Semiconductors and semimetals*, vol. 2, 3–31 (Elsevier, 1966).

[72] Jensen, W. B. The quantification of electronegativity: Some precursors. *Journal of Chemical Education* **89**, 94–96 (2012).

[73] Ren, G.-K. *et al.* Enhancing thermoelectric performance in hierarchically structured bicuseo by increasing bond covalency and weakening carrier–phonon coupling. *En- ergy & Environmental Science* **10**, 1590–1599 (2017).

[74] Yang, X. Enhancing thermoelectric properties of semi- conductors by heavily doping isoelectronic elements with electronegativities distinct from the host atoms. *Journal of alloys and compounds* **594**, 70–75 (2014).

[75] Holland, J. H. Genetic algorithms. *Scholarpedia* **7**, 1482 (2012). URL https://api.semanticscholar.org/ CorpusID:269807074.

[76] Deb, K. & Jain, H. An evolutionary many-objective optimization algorithm using reference-point-based non- dominated sorting approach, part i: Solving problems with box constraints. *IEEE Transactions on Evolution- ary Computation* **18**, 577–601 (2014).

[77] Blank, J. & Deb, K. pymoo: Multi-objective optimiza- tion in python. *IEEE Access* **8**, 89497–89509 (2020).

[78] Stein, M. Large sample properties of simulations using latin hypercube sampling. *Technometrics* **29**, 143–151 (1987).

[79] Tanabe, R. & Oyama, A. The impact of population size, number of children, and number of reference points on the performance of nsga-iii. In *International Conference on Evolutionary Multi-Criterion Optimization*, 606–621 (Springer, 2017).

[80] Yi, J.-H. *et al.* Behavior of crossover operators in nsga-iii for large-scale optimization problems. *Information Sci- ences* **509**, 470–487 (2020).

[81] Rosenthal, S. & Borschbach, M. Impact of population size, selection and multi-parent recombination within a customized nsga-ii and a landscape analysis for biochem- ical optimization. *Int. J. Adv. Life Sci* **6**, 310–324 (2014).

[82] Wang, B. *et al.* A new thermoelectric ag8sise6 argyrodite for room temperature application: sensitivity of thermo- electric performance to cooling conditions. *Materials Ad- vances* **5**, 3735–3741 (2024).

[83] Wang, L. *et al.* Realizing thermoelectric cooling and power generation in n-type pbs0.6se0.4 via lattice plaini- fication and interstitial doping. *Nature Communications* **15**, 3782 (2024).

[84] Zuo, W. *et al.* Atomic-scale interface strengthening un- locks efficient and durable mg-based thermoelectric de- vices. *Nature Materials* 1–8 (2025).

[85] Wang, X., Bourgès, C., Sato, N., Hassam, C. L. & Mori, T. Process influence on thermoelectric performance of digenite (cu1. 8s) and its underlined thermal instability. *Ceramics International* (2025).

[86] Abdellahi, M., Ghayour, H. & Bahmanpour, M. Effect of process parameters and synthesis method on the per- formance of thermoelectric ceramics: a novel simulation. *Ceramics International* **41**, 6991–6998 (2015).

[87] Sotelo, A. *et al.* Effect of synthesis methods on the ca3co4o9 thermoelectric ceramic performances. *Journal of Solid State Chemistry* **221**, 247–254 (2015).

[88] Rao, K. R., Kim, D. N. & Hwang, J. J. *Fast Fourier transform-algorithms and applications* (Springer Science & Business Media, 2011).

[89] Robertson, D. C., Camps, O. I., Mayer, J. S. & Gish, W. B. Wavelets and electromagnetic power system tran- sients. *IEEE Transactions on Power Delivery* **11**, 1050–1058 (1996).

[90] Deokar, S. & Waghmare, L. Integrated dwt-fft approach for detection and classification of power quality distur- bances. *International Journal of Electrical Power & En- ergy Systems* **61**, 594–605 (2014).

[91] Aas, K., Jullum, M. & Løland, Å. Explaining individual predictions when features are dependent: More accurate approximations to shapley values. *Artificial Intelligence* **298**, 103502 (2021).

[92] Purcell, T. A., Scheffler, M., Ghiringhelli, L. M. & Car- bogno, C. Accelerating materials-space exploration for thermal insulators by mapping materials properties via artificial intelligence. *npj Computational Materials* **9**, 112 (2023).