![](./images/812000232190509057_1.jpg)

Available online at www.sciencedirect.com

![](./images/812000232190509057_2.jpg)

Journal of Computational Physics 226 (2007) 301–325

JOURNAL OF
COMPUTATIONAL
PHYSICS

www.elsevier.com/locate/jcp

# Stochastic upscaling in solid mechanics: An excercise
in machine learning

## P.S. Koutsourelakis *

Applied Statistics and Economics, Electronics Engineering Technologies Division, Lawrence Livermore National
Laboratory, L-229, Livermore, CA 94551, United States

Received 2 August 2006; accepted 9 April 2007
Available online 24 April 2007

### Abstract

This paper presents a consistent theoretical and computational framework for upscaling in random microstructures. We adopt an information theoretic approach in order to quantify the informational content of the microstructural details and find ways to condense it while assessing quantitatively the approximation introduced. In particular, we substitute the high-dimensional microscale description by a lower-dimensional representation corresponding for example to an equivalent homogeneous medium. The probabilistic characteristics of the latter are determined by minimizing the distortion between actual macroscale predictions and the predictions made using the coarse model. A machine learning framework is essentially adopted in which a vector quantizer is trained using data generated computationally or collected experimentally. Several parallels and differences with similar problems in source coding theory are pointed out and an efficient computational tool is employed. Various applications in linear and non-linear problems in solid mechanics are examined.
Published by Elsevier Inc.

Keywords: Random; Heterogeneity; Homogenization; Upscaling; Information theory; Rate–distortion; Quantization

## 1. Introduction

Several experimental results and computer simulations have revealed that the behavior and response of engineering materials is a result of the synergy between phenomena that occur in various length scales. The microstructural heterogeneity gives rise to distinct macroscale phenomena and can have a dramatic effect in the their overall performance. In cases where the variability in the physical or mechanical properties that affect the behavior of the system is large, computational analysis in the context of traditional numerical schemes (e.g. Finite Elements, Finite Differences) requires that the size of the discretization be particularly small in order to accurately capture that heterogeneity. The resulting system of equations would however be prohibitively large for current or even foreseeable computational capabilities. Hence there is a dire need for general multiscale

* Tel.: +1 925 424 5231; fax: +1 925 422 4141.
E-mail address: koutsourelakis2@llnl.gov.

0021-9991/$ - see front matter Published by Elsevier Inc.
doi:10.1016/j.jcp.2007.04.012

methods that are able to incorporate microstructural information in a computationally efficient manner and provide accurate predictions for the macroscale response.

An important aspect that has been largely ignored in related efforts thus far is that of uncertainty. Indeed, the majority of materials demonstrate randomness in the microscale as local micro-properties exhibit stochas- tic fluctuations. In multiphase materials for examples the distribution of the constituent phases in space does not necessarily follow a particular pattern and is characterized by disorder. Furthermore, uncertainty arises from error in the measurements which is unavoidable even if those are performed in the controlled environ- ment of a laboratory. Finally, limited or complete lack of knowledge regarding microstructural details that might take place in a few micrometers or millimeters can introduce additional uncertainties. Even if this infor- mation is available (as it is sometimes possible nowadays due to the prodigious increase in resolution of mod- ern imaging techniques) the amount of data would be tremendous and its direct use impracticable.

It is therefore obvious that a probabilistic framework provides a sounder basis for the representation of heterogeneous media as it can quantify the uncertainties associated with microstructural details and allow for rational predictions for the reliability of the system under investigation [29]. Furthermore, statistical tech- niques can be used in order to reveal patterns in large volumes of microstructural data thus allowing not only fast representation of microstructural information but also efficient exploration of structure-property rela- tions. The significance of such a formulation has in fact been recognized in recent workshops organized by the DoE Office of Science on Multiscale Mathematics [8] where it was pointed out that key simulation issues involve the representation of information transfer across levels of scale and type (e.g. stochastic to determin- istic, discrete to continuous, interscale coupling) as well as the determination of the propagation of uncertainty across scales and physical phenomena.

This paper proposes a multiscale analysis procedure that is based on learning from data rather than exhaus- tive physical and numerical modeling [9]. Even though this is in contrast to traditional research practices, we do not dismiss significant work that has been done in this area [15,14,26,10] which in fact can significantly complement the proposed method.

The trend of learning from data (machine learning) which is quite prevalent in statistical circles, is neces- sitated in multiscale material problems by two basic reasons:

(1) The large amount of data that the analyst must process when dealing with microstructures.
(2) The inherent uncertainties of microstructural details which as discussed earlier must be accounted for.

A large number of existing approaches have concentrated on deriving *effective* properties based on the microstructural details i.e. estimating the properties of an equivalent homogeneous medium which on the mac- roscale behaves as the original material [2]. The microstructural details are therefore appropriately condensed and lower-dimensional representations are used which incorporate in some way the underlying information. The solution obtained does not contain any high-frequency fluctuations and under certain conditions is a good approximation to coarse scale behavior. Many classical homogenization techniques are based on the essential assumption that the properties of interest (i.e. stiffness, conductivity, etc.) are periodic on the fine scale or pos- tulate the existence of a representative volume element from which effective values for these properties can be derived. In general however, these conditions are not met in realistic materials where multiple length scales, not known a priori, co-exist and randomness precludes the existence of a representative volume element.

In the context of random heterogeneous materials, we must deal instead with an ensemble of possible microstructural configurations (each occurring with a certain probability) rather than a single one. Hence the procedures of homogenization obtain a new meaning as they have to be valid on a whole range of micro- structures. Even though randomness introduces an additional level of difficulty to the problem, it also provides a more general perspective as upscaling of the microstructural information does not have to be accurate for all possible configurations but, in an average sense at least, lead to predictions that retain the most important response characteristics.

The present paper employs ideas and concepts from information theory in order to quantify the microstruc- tural information and find ways to "upscale" it while assessing quantitatively the approximation introduced. In particular, we substitute the high-dimensional microscale description by a lower-dimensional representa- tion. The probabilistic characteristics of the latter are determined by minimizing the distortion between actual

macroscale predictions and the predictions made using the coarse model. These predictions of the response of the system can be obtained computationally using traditional numerical procedures or some of the recently developed deterministic upscaling methodologies or even experimentally. It is shown that the aforementioned problem is equivalent to designing a vector quantizer in source coding theory with a rather complicated dis- tortion function nevertheless [7]. The paper is organized as follows: In the next section, we provide an intro- duction to the information theoretic concepts and tools that are used in order to perform upscaling in random heterogeneous microstructures. We discuss the computational details of the method of deterministic annealing that is used in order to design the vector quantizer. In the last section, we present several applications of the methodology in linear and non-linear problems.

## 2. Methodology

As mentioned earlier, the approach followed in this paper is information theoretic. Information theory pro- vides a general mathematical framework originally developed in communication [27] in order to deal with the problems of data compression and transmission. One of the most important contributions of Shannon's trea- tise was the quantification of redundancies in a signal and discovery of representations that retain its informa- tional content while requiring a shorter description. The parallels one can draw with multiscale problems are obvious. The signal is the microstructural details and the goal is to find compression schemes that result in a shorter but as informative representation i.e. without depleting its salient characteristics. At this juncture we should point out two fundamental differences.

Firstly, in contrast to information theory where entropy provides an absolute measure of the description length (in terms of bits per symbol for example) that we want to reduce, in heterogeneous media it is the dimension of the description vector (which is essentially equivalent to length scale of heterogeneity), say $\mathbf{X}$ which we want to minimize. Even though entropy cannot directly be used as a measure of description size in our case, relative measures can be meaningfully extended to multiscale representations. One such indicator is the mutual information $I(\mathbf{X}, \mathbf{Y})$ where $\mathbf{Y}$ corresponds to a lower-dimensional description of the microscale details. A representation by $\mathbf{Y}$ implies that larger regions of the domain of interest can be assigned the same value and hence the dimension of $\mathbf{Y}$ is smaller. If $\mathbf{X}$ and $\mathbf{Y}$ are random as is the case in random media, then
$$
I(\mathbf{X}, \mathbf{Y})=\int p_{X Y}(x, y) \log \frac{p_{X Y}(x, y)}{p_{X}(x) p_{Y}(y)} \mathrm{d} x \mathrm{~d} y
\tag{1}
$$
where $p_{X Y}$ is the joint density of $(\mathbf{X}, \mathbf{Y})$ and $p_{X}$ and $p_{Y}$ the respective marginals. Mutual information measures the average information that knowledge of $\mathbf{Y}$ can provide about $\mathbf{X}$ and vice versa. It attains its minimum value zero when $\mathbf{X}$ is independent of $\mathbf{Y}$ (i.e. $p(\mathbf{X}, \mathbf{Y})=p_{X}(\mathbf{X}) p_{Y}(\mathbf{Y})$ ) and its maximum value i.e. the entropy of $\mathbf{X}$, $H(\mathbf{X})=-\int p_{X}(x) \log p_{X}(x) \mathrm{d} x$ when $\mathbf{X} \equiv \mathbf{Y}$.

The second significant difference with communication problems involves the fidelity of the compression. In traditional problems of information theory this is measured with respect to the source signal itself mean- ing by how close the compressed representation matches the original when the former is uncompressed. In random heterogeneous media however, we are not interested in the microstructural details per se but only in those features that affect the response of the system. Hence, an appropriate measure of the fidelity of our compression should be expressed with respect to the response. We will return to this subject and provide quantitative measures in the following section where we also give a short description of the respective theory of compression in information theory and the arsenal of methods that have been developed to address this problem.

### 2.1. Lossy data compression, rate-distortion theory and vector quantization

Since the subject is not directly related to the scope of the journal we feel inclined to provide a few intro- ductory remarks that will bridge this gap. Interested readers could look into the several references provided in the sequence.

One of the most important contributions of Shannon's original papers was the introduction of rate-distor- tion theory or lossy data compression [27,28]. The rate-distortion function is essentially a generalization of the

concept of entropy. It provides the optimal bounds for a compression scheme in cases where the decompressed signal does not need to be exactly the same as the original source. As Berger puts it in his book on the subject [3], rate-distortion theory is a means for "separating the wheat from the chaff". It arose from the fact that in many practical applications, it is not necessary to exactly reproduce the source signal but rather an appropriate approximation is sufficient. Naturally, this immediately gives rise to the question of how that error is to be measured (or equivalently what would be a good metric). Obviously the answer to the last question is not unique and strongly depends on the context. Generally, a distortion function is introduced $d(\mathbf{X}, \mathbf{Y})$ which assigns a non-negative number to each pair of representations $\mathbf{X}$ and $\mathbf{Y}$. According to rate-distortion theory for every source and distortion measure there exists a function $R(D)$ (called rate-distortion function), where $R$ represents the rate (i.e. in bits per symbol) and $D$ the average value of the distortion, that provides the (asymptotic) limit of achievable encoding compression schemes.

In the words of Blahut [4], rate-distortion theory is concerned with the average amount of information about the source that must be preserved by any data compression scheme such that the reproduction can subsequently generated from the compressed data with average distortion less than or equal to some specified level. Intuitively, if the average distortion $D$ is specified, then any compression must retain an average of at least $R(D)$ bits per source letter and conversely compression arbitrarily close to $R(D)$ is possible by an appropriate selection of the compression scheme.

Even though the theory provides the optimal bound it does not directly suggest techniques for finding this optimal encoding scheme. Several other problems such as classification or clustering or pattern recognition encountered in machine learning share similar motivations and solution tools. Vector Quantization (VQ) is a term often equivalent with source coding or lossy data compression and describes the operation by which an $N$-dimensional random vector $\mathbf{X}$ with distribution $p_{X}(\mathbf{X})$ (in practice the distribution itself might not be available but rather samples $\mathbf{X}_{i}$ drawn from $p_{X}$ ) is encoded by an ensemble of codebook vectors (usually finite in number) $\mathbf{Y} \in \mathbb{R}^{n}$ with distribution $p_{Y}(\mathbf{Y})$ such that the entropy of the latter $H(\mathbf{Y})$ is smaller than $H(\mathbf{X})$ (and hence can be compressed to a higher rate). In most applications in communication (image and voice compression) the dimension of the codebook vectors $\mathbf{Y}, n$ is equal to $N$ i.e. that of the original vector.

An indispensable component of every compression scheme is of course the distortion function which provides a measure of fidelity. As mentioned earlier, in random heterogeneous media the distortion function should not be expressed with respect to the microstructural representation $\mathbf{X}$ itself but rather in terms of the response due to $\mathbf{X}$. The latter can in general be represented by a function $r(\mathbf{X})$ which can be a scalar, vector or even matrix-valued depending on the response components that are of interest. Let $\mathbf{Y}$ denotes a lower-dimensional representation. In the following derivations we assume that $r$ is scalar and adopt the following distortion function:

$$
d(\mathbf{X}, \mathbf{Y})=(r(\mathbf{X})-r(\mathbf{Y}))^{2} \tag{2}
$$

where $r(\mathbf{Y})$ corresponds to the response due to a the compressed representation $\mathbf{Y}$. It should also be noted that in practical applications, the function $r$ is not known analytically but it is implicitly defined by the numerical solver. Furthermore, calculating values of the response is generally easier for $r(\mathbf{Y})$ than $r(\mathbf{X})$ as $\mathbf{Y}$ corresponds to a coarser discretization and the system of equations that must be solved is smaller.

Without loss of generality and for notational economy, in the following presentation we assume that the encoding of the $N$-dimensional random vector $\mathbf{X}$ describing the microstructural details (i.e. the value of a material property in $N$ micro-domains) will be represented by a random variable $Y$ which essentially corresponds to the equivalent homogenized property of the medium. Let $d(\mathbf{X}, Y): \mathbb{R}^{N} \times \mathbb{R} \rightarrow \mathbb{R}^{+}$denote the distortion function as defined above which is always non-negative. Our goal is dual. Firstly we seek the encoding scheme i.e. the mapping from $\mathbf{X}$ to $Y$ that leads to the minimum possible distortion and secondly to determine that minimal value. The latter corresponds to the best homogenization or upscaling scheme that can be achieved in terms of the distortion function adopted. Determining the optimal encoding scheme involves essentially evaluation of the distribution of $Y$ i.e. $p_{Y}(y)$. Once this has been found then the original microstructural ensemble (described by the random vector $\mathbf{X}$ ) can be substituted with a homogeneous medium (described by the scalar $Y$ ). The response predictions made by the homogeneous medium will not deviate on average more than the corresponding distortion value. A schematic illustration of the proposed procedure is depicted in Fig. 1. Apart from those objectives which are perhaps the most important in terms of practical implications,

![](./images/812000232190509057_3.jpg)

Fig. 1. Schematic illustration of proposed methodology: an ensemble of equivalent homogeneous media is constructed so that it recovers the response predictions of the actual random microstructure.

the present formulation will provide various sub-optimal encoding schemes and their respective distortions in the response predictions.

The design of vector quantizers such as the one sought herein involves several intricacies. Interested readers are directed to the book of Gersho and Gray [13] where several details are provided regarding structure, mea- suring performance, optimality and design. The most popular procedure for carrying out such a task is the generalized Lloyd algorithm [19] sometimes known as the $k$-means algorithm and its extensions. It is an iter- ative optimization procedure in which the codebook and the partition of the original space are successively updated. Despite its popularity and success in several problems it can at times get trapped into local minima.

For that purpose we employ the technique of Deterministic Annealing developed first by Rose in [22] and further expanded in [23,24]. As its name suggests, it represents a marriage between the powerful simulated annealing technique from stochastic global optimization and deterministic procedures which direct the ran- dom search in directions that are highly likely to lead to improvement of the objective function. In contrast to the basic form of the generalized Lloyd algorithm, deterministic annealing possesses the ability to move past local minima and approach if not match the global optimum.

In the following we present an alternative derivation of the original procedure which has several similarities with evaluating rate-distortion function in lossy data compression and it is novel in that respect but neverthe- less leads to the same basic formulas as in the original papers [23,24].

Without loss of generality and for notational economy, it is assumed henceforth that $\mathbf{X}$ and $Y$ are discrete variables and therefore integrals can be substituted by summations. Subscripts in the probability mass func- tions will also be omitted. We start from the basic assumption that the mapping between $\mathbf{X}$ to $Y$ is not deter- ministic i.e. there is not a single $Y$ corresponding to each $\mathbf{X}$ but rather this relationship can be expressed by a conditional probability distribution $p(Y/\mathbf{X})$. At the limit this association probability should approach a delta function in the sense that each $\mathbf{X}$ will be represented/encoded by a single $Y$. The reason for the introduction of $p(Y/\mathbf{X})$ will become apparent in the sequence. The objective function to be minimized is now the expected distortion:

$$
D=E[d(\mathbf{X}, Y)]=\sum_{\mathbf{X}, Y} p(\mathbf{X}) p(Y / \mathbf{X}) d(\mathbf{X}, Y)
\tag{3}
$$

At this form, the minimizer of $D$ with respect to $p(Y/\mathbf{X})$ will be a delta function which assigns to each $\mathbf{X}=x$ the $Y$ that minimizes $d(x, Y)$. Instead we employ the principle of simulated annealing and relax the aforemen- tioned difficult optimization problem by augmenting the problem with the constraint $I(\mathbf{X}, Y) \leqslant R$ where $R$ is an arbitrary positive number and $I(\mathbf{X}, Y)$ the mutual information between the fine and coarse scale descrip- tions $\mathbf{X}$ and $Y$, respectively, i.e. (from Eq. (1)):

$$
I(\mathbf{X}, Y)=\sum_{\mathbf{X}, Y} p(\mathbf{X}) p(Y / \mathbf{X}) \log \frac{p(Y / \mathbf{X})}{q(Y)}
\tag{4}
$$

where
$$
q(Y)=\sum_{\mathbf{X}} p(\mathbf{X}) p(Y / \mathbf{X})
\tag{5}
$$

is the marginal of $Y$. As mentioned earlier $I(\mathbf{X}, Y)$ measures the dependence between $\mathbf{X}$ and $Y$ or equivalently the information that knowledge of one carries about the other. On one limit, i.e. when $I(\mathbf{X}, Y)=0$, the coarse and fine scale descriptions are independent and therefore, no information about $\mathbf{X}$ is contained in $Y$. As $I(\mathbf{X}, Y)$ increases so does the dependence between $\mathbf{X}$ and $Y$ and so does the information that knowledge of $Y$ can provide about the underlying $\mathbf{X}$. Hence by imposing the aforementioned constraint and gradually increasing $R$ we are able to get more informative code-vectors. The inequality constraint thus has a regularizing effect. The respective Lagrangian then takes the following form:

$$
F=D+T(I(\mathbf{X}, Y)-R)
\tag{6}
$$

where $T$ is a Lagrange multiplier which must be non-negative and satisfies the Karush-Kuhn-Tucker condition i.e. $T(I(\mathbf{X}, Y)-R)=0$ at the optimal point. The minimization of $F$ with respect to $p(Y / \mathbf{X})$ is in fact equivalent to minimizing $I(\mathbf{X}, Y)$ with the inequality constraint $D<D_{0}$ (where $D_{0}$ is an arbitrary positive constant) which would involve the Lagrangian $F^{c}$:

$$
F^{c}=I(\mathbf{X}, Y)+\beta\left(D-D_{0}\right)
\tag{7}
$$

Obviously, both Lagrangians $F$ and $F^{c}$ are simultaneously optimized by the same $p(Y / \mathbf{X})$ for $\beta=T^{-1}$ and therefore, the two minimization problems are equivalent. The latter however represents the formulation for finding a rate-distortion curve $R\left(D_{0}\right)[3,7]$ i.e. minimizing the mutual information for a certain distortion level $D_{0}$.

It is worth pointing out that $T$ plays the role of temperature in simulated annealing and can be used as a free parameter. For large values of $T$, minimizing $F$ mainly implies minimizing $I$. As $T$ is lowered a possible decrease in mutual information is outweighed by reduction of the actual distortion $D$. If $T$ is large, then increasing the number of code-vectors $Y$ will decrease $D$ but increase $I$ and hence lead to moderate if any decrease of the Lagrangian. For small $T$, variations in $I$ by changes in $Y$ do not have as much of an effect as an actual decrease in $D$. In a sense, the average distortion $D$ and mutual information $I$ are actually competing meaning we can increase the complexity in $Y$ in order to reduce $D$ (in the case of over-fitting we can introduce a $Y$ for every $X$ ) but this will lead to an increase in $I$ which is highly penalized when $T$ is large. Hence by selecting an appropriate cooling schedule (i.e. decrease in $T$ ) we can achieve a gradual approach to the global minimum and evade possible local minima in the process.

By considering the gradient of $F$ with respect to $p(Y / \mathbf{X})$ we arrive to the following condition regarding the optimum $p^{*}$:

$$
p^{*}(Y / \mathbf{X})=\frac{q(Y) \exp \left(-\frac{d(\mathbf{X}, Y)}{T}\right)}{Z(\mathbf{X})}
\tag{8}
$$

where $Z(\mathbf{X})=\sum_{\mathbf{X}} q(Y) \exp \left(-\frac{d(\mathbf{X}, Y)}{T}\right)$ is the normalizing constant. Hence the optimal $p(Y / \mathbf{X})$ is a Gibbs distribution which converges to a delta as $T$ goes to zero. The corresponding minimum of $F$ say $F^{*}$ arises by substituting Eq. (8) in Eq. (6):

$$
F^{*}=-T \sum_{\mathbf{X}} p(\mathbf{X}) \log Z(\mathbf{X})+T R
\tag{9}
$$

We can overlook the constant $T R$ since the actual value of the minimum $F^{*}$ is not important but rather the minimizer, and focus on minimizing:

$$
F^{*}=-T \sum_{\mathbf{X}} p(\mathbf{X}) \log \sum_{\mathbf{X}} q(Y) \exp \left(-\frac{d(\mathbf{X}, Y)}{T}\right)
\tag{10}
$$

with respect to the free parameters $q(Y)$ i.e. the marginal of $Y$. We assume without loss of generality that $q(Y)$ can be sufficiently approximated by a discrete distribution where $y_i$ indicate the atoms and $q_i$ the respective probabilities such that $\sum_i q_i=1$. It should be noted that the number of the atoms is initially unknown. Hence $F^*$ needs to be minimized with respect to the free parameters $y_i$ and $q_i$. This is equivalent to minimizing the unconstrained Lagrangian:

$$
F' = F^* - \lambda \left( \sum_i q_i - 1 \right)
\tag{11}
$$

The sufficient conditions arise by setting the gradient of $F'$ equal to zero i.e.:

$$
\frac{\partial F'}{\partial y_k} = 0 = \sum_{\mathbf{X}} p(\mathbf{X}) p^*(y_k / \mathbf{X}) \frac{\partial d(\mathbf{X}, y_k)}{\partial y_k}
\tag{12}
$$

and

$$
\frac{\partial F'}{\partial q_k} = 0 = -T \sum_{\mathbf{X}} \frac{1}{Z(\mathbf{X})} \exp \left( -\frac{d(\mathbf{X}, y_k)}{T} \right) + \lambda
\tag{13}
$$

Given Eq. (8) the latter implies that $\sum_{\mathbf{X}} p(\mathbf{X}) \frac{p^*(Y/\mathbf{X})}{q(Y)} = \frac{\lambda}{T}$. By the definition of $q(Y)$ (Eq. (5)) we therefore have that $\frac{\lambda}{T}=1$ i.e. $\lambda=T$ and by substitution in Eq. (13):

$$
\sum_{\mathbf{X}} \frac{1}{Z(\mathbf{X})} \exp \left( -\frac{d(\mathbf{X}, y_k)}{T} \right) = 1
\tag{14}
$$

It should be noted that Eqs. (12) and (14) are identical to Eqs. (28) and (33) of Rose's paper [24] which were derived following a different process but based on the same assumptions.

Instead of a summary, we present the basic steps of the algorithmic implementation of the deterministic annealing. Let $K$ denote the size of the population of code-vectors $y_i$:

(1) Initialize by selecting a high enough value for $T=T_{\max}$ and $K=1$. Select arbitrary $y_1$ and $q_1=1$.
(2) For $i=1,2,\ldots,K$ update $p(y_i/\mathbf{X})$, $q_i$ and $y_i$ based on Eqs. (8), (5) and (12), respectively i.e.:

$$
p(y_i / \mathbf{X}) = \frac{q_i \exp -\frac{d(\mathbf{X}, y_i)}{T}}{\sum_{l=1}^K q_l \exp -\frac{d(\mathbf{X}, y_l)}{T}}
\tag{15}
$$

$$
q_i = \sum_{X} p(\mathbf{X}) p(y_i / \mathbf{X})
\tag{16}
$$

(where the integration with respect to $\mathbf{X}$ is generally performed by Monte Carlo i.e. by simulating vectors $\{\mathbf{X}_\mathbf{j}\}_{j=1}^M$ from the distribution $p_X$ and approximating the update for $q_i$ by $\frac{1}{M} \sum_{j=1}^M p(y_i / \mathbf{X}_\mathbf{j})$)

$$
y_i = r^{-1} \left( \frac{\sum_X p(\mathbf{X}) p(y_i / \mathbf{X}) r(\mathbf{X})}{q_i} \right)
\tag{17}
$$

where $r^{-1}$ is the inverse of the response function (further details are provided in the applications. As before, the summation with respect to $\mathbf{X}$ is performed by Monte Carlo estimators. For certain distortion measures or responses functions Eq. (12) does not have a unique solution (see Section 3). In these cases we select the solution that results in the minimal average distortion).

(3) Check for convergence in terms of $y_i$ and $q_i$. If it has not been achieved repeat the previous updating step.
Otherwise:
(4) Reduce temperature $T$, i.e. $T=aT$ (where $a<1$).
(5) Double the number of code-vectors $y_i$ i.e. $K=2K$ by setting $y_{K+i}=y_i$ and $q_{K+i}=q_i$ and goto step 2.

It should be noted that the last step is necessary since the number of atoms $K$ that minimize the objective function is unknown a priori for each $T$. In order to capture the phase transitions of the algorithm i.e. times at which the minimizing distribution for $\mathbf{Y}$ has more atoms than prescribed, we artificially double their number.

If during the updating step atoms are found sufficiently close to each other then they are substituted by a single atom and their respective $q_i$ consolidated into one after convergence has been established at step 3. Hence the unknown number of atoms can be determined as the algorithm evolves.

## 3. Applications

This section contains several applications and numerical results of the procedures proposed. We also elu- cidate several algorithmic aspects which has been difficult to do in the general exposition. The presentation is broken up in two parts. In the first we deal with single-cell problems i.e. single domains with known proba- bilistic microstructural details for which we attempt to find equivalent homogeneous representations based on various response components of interest.

In the second part which is perhaps the most interesting for practical applications, a multi-cell problem is examined i.e. the original domain is divided into several sub-domains (cells). The methodology developed is used to estimate macroscale properties of each cell and these are in turn used to evaluate the response of the whole system. This has significant computational advantages as the overall response can be obtained by solving much smaller systems of equations. Indeed, employing well-established deterministic multiscale techniques in random microstructures by Monte Carlo simulations would be computationally inefficient as several, expensive runs on the full system would have to be performed. In the proposed framework, we instead perform several runs on smaller sub-domains from which we learn about the statistical properties of an equiv- alent homogeneous medium that can take the place of each sub-domain. These are finally used to solve on the whole domain by employing a coarser discretization which leads of course to significant computational savings.

It should also be noted that in all cases it was assumed that the probabilistic microstructural characteristics were known i.e. $p_X$ was given or equivalently samples $X_i$ drawn from $p_X$ were available. This is by no means an easy task and the object of active research. A general framework for constructing microstructural distributions and generating sample realizations is presented in [18].

### 3.1. Single-cell problems

#### 3.1.1. One-dimensional elastic bar

We first consider the problem of a one-dimensional elastic bar of unit length, unit cross-sectional area and uncertain modulus of elasticity. The governing equation for the displacement $u(x)$ is

$$
\frac{\mathrm{d}}{\mathrm{d} x}\left(E(x) \frac{\mathrm{d} u}{\mathrm{~d} x}\right)=0, \quad x \in[0,1]
\tag{18}
$$

with boundary conditions $u(0)=0$ and $E(1)\left.\frac{\mathrm{d} u}{\mathrm{~d} x}\right|_{x=1}=F_{0}=1$. We assume the following simple model for the random variability of $E(x)$:

$$
E(x)=1+0.5 \cos \left(2 \pi \frac{x}{x_{0}}+\phi\right)
\tag{19}
$$

where the phase angle $\phi$ is a random variable uniformly distributed in $[0,2 \pi]$ and the constant $x_{0}$ is used to control the length scale of heterogeneity. The present problem does not pose any difficulties as solutions can be obtained in closed form but it serves as a useful illustration of the capabilities of the proposed meth- odology. It can be easily shown that the effective elastic modulus $E_{\text {eff }}(x)$, i.e. a constant elastic modulus that gives the same prediction for $u(x)$ as the original model is given by

$$
E_{\mathrm{eff}}(x)=\left(\int_{0}^{x} \frac{1}{E(s)} \mathrm{d} s\right)^{-1}
\tag{20}
$$

where $E(x)$ is given in Eq. (19). It should be emphasized that the $E_{\text {eff }}$ is still a random variable. Its variance i.e. the spread around the mean decreases as the length scale $x_{0}$ becomes smaller. Hence for very small $x_{0} \ll 1$ the variance is almost zero and $E_{\text {eff }}$ can be approximated by its mean.

We consider a discretization of the domain $[0,1]$ into $N=1000$ elements, introduce a vector $\mathbf{X}$ which contains the values of $E(x)$ at the centroid of each interval and assume that the elastic modulus is constant within each interval $i$ and equal to $X_i$ (this should provide a good approximation to the original problem if $x_0 \gg 1/N$). We evaluate the performance of the upscaling scheme introduced earlier for various cases.

Firstly for $x_0=1/100$ we simulated 100 realizations $\mathbf{X}_i$ of vector $\mathbf{X}$ based on Eq. (19) and calculated the displacement at $x=1$, i.e. $r(\mathbf{X}_i)$. Those were used as the training sample for the vector quantization algorithm presented in the previous section in order to find the distribution of a scalar variable $Y$ which corresponds to the elastic modulus of an equivalent homogeneous bar. When $Y=E=$ const it can be readily established that the response at $x=1$ is given by $r(E)=\frac{F_0}{E}=\frac{1}{E}$ and therefore, the inverse of the function $r$ in Eq. (17) is given by $r^{-1}(u)=1/u$. As the $r(\mathbf{X}_i)$ are practically identical, the algorithm recovers a single atom located at $y_1=E[E_{\text{eff}}]$ for which the expected distortion as defined in Eq. (3) is 0.0.

If however we assume that $x_0=10 \gg 1$ then essentially the entries of each realization of $\mathbf{X}$ exhibit very little variability and their probabilistic characteristics follow that of the random variable $\cos(\phi)$. We simulated 1000 realizations of vector $X$ based on Eq. (19) and calculated the displacement at $x=1$, i.e. $r(\mathbf{X}_i)$. Those were used as the training sample for the vector quantization algorithm presented in the previous section in order to find the distribution of a scalar variable $Y$ which corresponds to the elastic modulus of an equivalent homogeneous bar. A fairly large training sample size was used in order to explore the qualities of algorithm. Normally in practical applications smaller samples will be available as the calculation of the response for each one can be computationally intensive. Naturally, the larger the training sample, the more knowledge we can extract. In order to circumvent getting trapped in local minima a random subsample consisting of 500 points was used in every iteration. The minimal distortion as expressed in Eq. (3) when the distribution of $Y$ consists of a single atom was found equal to 0.20. As the algorithm progresses it discovers more informative distributions with reduced distortion.

A rate-distortion diagram can be seen in Fig. 2. The $x$-axis represents the expected distortion $D$ (Eq. (3)) and the $y$-axis the mutual information $I(\mathbf{X}, \mathbf{Y})$ (Eq. (4)) at various steps. The progression of the algorithm is such that it starts from large $D$ and low $I$ and moves to small $D$ and large $I$ (i.e. from right to left in Fig. 2). The initial temperature was $T_{\max}=100$ and a very slow cooling schedule with $a=1/1.001$ was used. The jagged progression of the curve is due to the Monte Carlo estimators that are used. As mentioned earlier, at each step we used a random subsample of the original 1000-strong population of $\mathbf{X}_j$ consisting of 500 samples at a time. The smallest average distortion observed was $0.82 \times 10^{-4}$ i.e. approximately 4 orders of magnitude smaller than the original. It corresponds to the distribution of the equivalent homogeneous modulus $Y$ that is depicted in Fig. 3 and consists of 42 atoms. As expected it approximates the distribution of $1+0.5 \cos \phi \ \phi \sim U[0,2\pi]$ (Eq. (19)).

![](./images/812000232190509057_4.jpg)

Fig. 2. Rate-distortion curve for the problem of the one-dimensional bar with random elastic modulus (Eq. (19), $x_0=10$).

![](./images/812000232190509057_5.jpg)

Fig. 3. Comparison of the optimal distribution (black) for the elastic modulus of an equivalent homogeneous medium with the distribution of $1+0.5\cos\phi$ $\phi\sim U[0,2\pi]$ (exact) for the problem of the one-dimensional bar with random elastic modulus (Eq. (19), $x_0=10$).

The practical significance of the proposed procedure is that the microstructural details as modeled by the random vector $\mathbf{X}$ of dimension 1000 can be substituted by an equivalent homogeneous bar with elastic modulus $Y$ following the distribution shown in Fig. 3. The expected error/distortion in the predictions made by the latter model will be equal to $D=0.82\times 10^{-4}$ on average. A comparison of the cumulative distribution function of the displacement $u(1)$ made with the exact and the upscaled models can be seen in Fig. 4.

### 3.1.2. Two-dimensional elastostatics

We considered a square domain of unit length consisting of two-phase heterogeneous material. Let $B(\mathbf{x})$, $\mathbf{x}\in[0,1]^2$ the binary random field which describes the medium [18] and takes values 0 and 1 if point $\mathbf{x}$ lies on phase 1 or 2, respectively. We assume the following model for the binary field $B$:

![](./images/812000232190509057_6.jpg)

Fig. 4. Comparison of cumulative distributions of displacement at $x=1$ obtained using the actual microscale model and the equivalent homogeneous approximation for the problem of the one-dimensional bar with random elastic modulus (Eq. (19), $x_0=10$).

$$
B(\mathbf{x})=
\begin{cases}
0 & \text{if } Z(\mathbf{x}) \leqslant 0 \\
1 & \text{if } Z(\mathbf{x}) > 0
\end{cases}
\tag{21}
$$

where $Z(\mathbf{x})$ is a Gaussian, zero mean, unit variance, statistically homogeneous random field with autocorrelation $\rho(\mathbf{z})=E[Z(\mathbf{x}) Z(\mathbf{x}+\mathbf{z})]=e^{-\frac{\|\mathbf{z}\|^{2}}{z_{0}}}$. The parameter $z_{0}$ controls the scale of variability and it was taken equal to 0.1 in this example. The model adopted results in a medium with 50% volume fraction for each phase. A typical realization of the medium can be seen in Fig. 5. It was further assumed that phases 1 and 2 were elastic and isotropic with common Poisson's ratio $v=0.3$ and elastic moduli $E_{1}=1$ and $E_{2}=10$, respectively.

We assumed a discretization of the domain into $512 \times 512$ pixels and introduced the vector $\mathbf{X}$ of dimension $512 \times 512=262144$ to model the microstructural details i.e. the value of the elastic moduli at each pixel. The goal is to obtain an equivalent elastic modulus $Y$ for the whole domain that will minimize the distortions in the response predictions with respect to the full model given by $\mathbf{X}$.

We considered the loading condition in which the right edge is fixed in the horizontal and vertical direction and a unit horizontal stress is applied on the left edge. As the target response we considered the displacements (horizontal and vertical) at 10 arbitrarily selected points within the domain. Their coordinates are also provided in Fig. 5. In this case a similar form of Eq. (3) was used for the distortion function:

$$
d(\mathbf{X}, \mathbf{Y})=\frac{1}{M} \sum_{i=1}^{M}\left(r_{i}(\mathbf{X})-r_{i}(Y)\right)^{2}
\tag{22}
$$

where $r_{i}$ denote the functions giving the displacement component at each of the 10 points selected ($M=10$).

The vector quantization algorithm converges at the first iteration to a single atom distribution for $Y$ located at 2.67 which essentially represents the effective elastic modulus for the particular medium. The fact that it is deterministic implies that the ergodic effects take place which is to be expected due to the linearity of the problem as well as due to the fact the length of heterogeneity is much smaller than the domain examined. The value of the expected distortion is only $1.74 \times 10^{-4}$. Hence by substituting the original random medium by a deterministic medium with an elastic modulus equal to 2.67 one can obtain highly accurate predictions for the displacements at a fraction of the computational cost as the solution of the equivalent homogeneous problem does not require as fine of a discretization.

We examined the same problem by applying a uniform unit displacement on the right edge instead of stress. We recorded the von-Mises stress at the 10 arbitrarily selected points depicted in Fig. 5. We then attempted to

![](./images/812000232190509057_7.jpg)

Fig. 5. Realization of the medium described by Eq. (21). Coordinates of the points indicated by red dots: $A(0.910,0.660)$, $B(0.686,0.316)$, $C(0.830,0.730)$, $D(0.297,0.00195)$, $E(0.943,0.393)$, $F(0.0938,0.379)$, $G(0.0977,0.309)$, $H(0.771,0.926)$, $I(0.990,0.719)$, $J(0.873,0.770)$. (For interpretation of the references in color in this figure legend, the reader is referred to the web version of this article.)

![](./images/812000232190509057_8.jpg)

Fig. 6. Rate-distortion curve for the medium described by Eq. (21) when the von-Mises stress at point A (Fig. 5) is used as target response.

derive effective properties using the stress value at the first of these points as the measure of the distortion. With 500 training samples, the vector quantization algorithm produced the result depicted in Fig. 6 in terms of the rate-distortion curve. The initial average distortion of 0.27 at the first iteration (corresponding to a single atom for $Y$) was ultimately reduced to $0.30 \times 10^{-1}$ which is the minimal possible value attained by a distribution with 42 atoms depicted in Fig. 7.

In contrast to the previous case where displacements were used as the target response, in this case the minimal distortion is quite significant which implies that a substitution with a homogeneous medium will not in general provide accurate prediction in terms of pointwise stresses. This is in a sense a theoretical validation of a common fact in engineering mechanics as stresses are highly local and in order to make accurate estimates the microstructural details have to be accounted. Hence, in terms of stresses there is a significant information loss when upscaling.

![](./images/812000232190509057_9.jpg)

Fig. 7. Optimal distribution of the elastic modulus of an equivalent homogeneous medium for the material described by Eq. (21) when the von-Mises stress at point A (Fig. 5) is used as target response.

This observation becomes more pronounced when stresses in more than one locations are to be predicted. When we run the vector quantization algorithm with all 10 stresses as the target response. The minimal average distortion that was achieved was 2.1 i.e. much higher than before. This is to be expected since as it was mentioned earlier stresses depend on the highly local heterogeneities and hence substitution with a homogeneous medium cannot account for these details at various locations of the domain.

This effect however is not observed when averaged stresses are sought. Indeed, we examined the same problem but used the total reaction on the right edge as the target response. In this case the vector quantization algorithm at the first iteration gives rise to the single atom distribution at 2.67 for which the average distortion is $0.83 \times 10^{-3}$. It is noted that this is exactly the same result with the one obtained when using displacements as the response of interest.

The optimal distortion that can be achieved is equal to $0.51 \times 10^{-5}$ corresponds to the distribution of Fig. 8. The latter is concentrated very tightly around 2.67.

### 3.1.3. Two-dimensional elasto-plastic material
We consider the same square domain of unit length as in the previous example consisting though of a different two-phase heterogeneous material. The latter is described by the Boolean model according to which the inclusion phase is made up of the union of discs of diameter $d = 0.0859375$ centered at the points of a Poisson point process on the square domain. The intensity of the point process is selected so that the volume fraction of the matrix phase is 35%. This was intentionally chosen to be close to the percolation threshold of 68% [31] in order to have realizations where the inclusion phase was connected and disconnected. We assume that both materials were elastic-perfectly plastic with identical elastic properties ($E=1$ and $v=0.3$) but with yield stresses $\sigma_{y1}=1$ (inclusion) and $\sigma_{y2}=0.1$ (matrix). The von-Mises yield criterion was used.

The domain was discretized by $128 \times 128$ elements and subjected to a unit uniform displacement on the right edge while the left edge remained fixed. For sample realizations for which the inclusion (strong) phase was connected (as in Fig. 9), the specimen was able to carry load to the support and hence the reaction of the domain was increased compared to cases when the inclusion phase was disconnected (as in Fig. 10) and there was no internal network to carry the load.

We attempted to find an equivalent homogeneous medium with yield stress $Y$ that can essentially substitute the $128 \times 128=16384$-dimensional vector $\mathbf{X}$ which contains the yield stress of each element. The optimal distribution of $Y$ is depicted in Fig. 12 and corresponds to an average distortion of $0.48 \times 10^{-4}$ with respect to the reaction at the right edge. This implies that if the original random heterogeneous medium was substituted with

![](./images/812000232190509057_10.jpg)

Fig. 8. Optimal distribution of the elastic modulus of an equivalent homogeneous medium for the material described by Eq. (21) when the total reaction along the right edge is used as target response.

![](./images/812000232190509057_11.jpg)

Fig. 9. Sample realization of the Boolean model where inclusion phase is connected.

![](./images/812000232190509057_12.jpg)

Fig. 10. Sample realization of the Boolean model where inclusion phase is disconnected.

an equivalent homogeneous with yield stress following the distribution of Fig. 12 then the mean square error in the prediction of the reaction of the right edge would only be $0.48 \times 10^{-4}$. The rate-distortion curve calculated by the vector quantization algorithm can be seen in Fig. 11.

The same problem was analyzed for a much higher contrast in the yield stresses of the constitutive phases. In particular it was assumed that $\sigma_{y 2}=0.01$ (matrix) whereas $\sigma_{y 1}=1$ was kept the same. The optimal distribution for the yield stress of an equivalent homogeneous medium is depicted in Fig. 13 and corresponds to an expected distortion of $0.14 \times 10^{-3}$. As compared with the optimal distribution for $\sigma_{y 2}=0.1$ (Fig. 12) it is shifted to the right but not perhaps as much as the higher contrast and the new $\sigma_{y 2}$ would imply. This demonstrates clearly that when there is a large contrast in the properties of the constitutive phases, the geometric variability plays a paramount role in response prediction.

#### 3.1.4. Cohesive zone elements – fracture modeling
The concept of cohesive laws which was pioneered by Dugdale [11] and Barenblatt [1] in order to model fracture processes and has been successfully used in a Finite Element setting by several researchers [30,5,20]. In 3D, they introduced surface-like elements which are located at the interfaces of adjacent bulk elements and govern their separation in accordance with a cohesive law. Several crack initiation criteria have been used with the most common being the exceedance of the interfacial strength prescribed by the cohesive

![](./images/812000232190509057_13.jpg)

Fig. 11. Rate-distortion curve for the Boolean medium ($\sigma_{y1}=1$ (inclusion) and $\sigma_{y2}=0.1$ (matrix)) when the total reaction along the right edge is used as target response.

![](./images/812000232190509057_14.jpg)

Fig. 12. Optimal distribution of the yield stress of an equivalent homogeneous medium for the Boolean medium ($\sigma_{y1}=1$ (inclusion) and $\sigma_{y2}=0.1$ (matrix)) when the total reaction along the right edge is used as target response.

model [21,16]. According to this model, fracture is a gradual phenomenon in which separation takes place across an extended crack 'tip' or cohesive zone and is resisted by cohesive tractions. This theory of fracture allows the incorporation into the analysis of well-established fracture parameters such as the spall strength (i.e. the peak cohesive traction) and the fracture energy of the material which is represented by the area under the cohesive law. Naturally the quality of the approximation of the fracture zone depends on the size of the cohesive elements and in general the smaller they are the more accurate the representation. We assume herein a simple constitutive law relating interface traction-separation as seen in Fig. 14. Under monotoning loading the normal interface traction decays as $T=T_{\mathrm{c}}\left(1-\frac{\delta}{\delta_{\mathrm{c}}}\right)$ for $\delta \leqslant \delta_{\mathrm{c}}$ and $T=0$ for $\delta>\delta_{\mathrm{c}}$. The fracture energy $G_{\mathrm{c}}$ is given by $G_{\mathrm{c}}=T_{\mathrm{c}} \delta_{\mathrm{c}} / 2$.

![](./images/812000232190509057_15.jpg)

Fig. 13. Optimal distribution of the yield stress of an equivalent homogeneous medium for the Boolean medium ($\sigma_{y1}=1$ (inclusion) and $\sigma_{y2}=0.01$ (matrix)) when the total reaction along the right edge is used as target response.

![](./images/812000232190509057_16.jpg)

Fig. 14. Cohesive law: $T_{\mathrm{c}}$ denotes ultimate interfacial tension (when the stress reaches $T_{\mathrm{c}}$ the cohesive element is activated), $\delta_{\mathrm{c}}$ denotes the ultimate separation interface (when the separation reaches $\delta_{\mathrm{c}}$ the interface tension becomes zero) and $G_{\mathrm{c}}$ denotes the fracture energy which is equal to the area under the tension-separation curve.

We consider an 1D interface of unit length modeled by 1000 cohesive elements. Their properties i.e. $T_{\mathrm{c}}$ and $\delta_{\mathrm{c}}$ are represented by the random vector $\mathbf{X}$ and they are assumed to be random. In the first case we assumed that the fracture energy of each element $G_{\mathrm{c}}$ is described by the following log-normally distributed random field $Z(x)$:

$$
Z(x)=\mu+\sigma \frac{e^{U(x)}-\mu_{u}}{\sigma_{u}}, \quad x \in[0,1]
\tag{23}
$$

where $U(x)$ is a zero mean, unit variance Gaussian field with autocorrelation $\rho(z)=E[U(x) U(x+z)]=e^{-\frac{|z|}{z_{0}}}$. The parameter $z_{0}$ controls the length scale of heterogeneity and it was taken equal to 0.05. The mean $\mu$ and standard deviation $\sigma$ of $Z(x)$ were taken equal to 1 (the parameters $\mu_{u}=e^{0.5}$ and $\sigma_{u}=\sqrt{e^{2}-e}$ are used

![](./images/812000232190509057_17.jpg)

Fig. 15. Scale effect – optimal distribution of the fracture energy of an equivalent homogeneous cohesive zone when the fracture energy at the microscale varies as in Eq. (23).

for normalizing $e^{U}$). It was further assumed that $\delta_{\mathrm{c}}=2.0$ for all elements and the cohesive strengths were calculated as $T_{\mathrm{c}}=\frac{2 G_{\mathrm{c}}}{\delta_{\mathrm{c}}}$. One thousand realizations were analyzed and used as training samples (some are depicted in Fig. 16) in order to determine the properties of a single cohesive element of unit length which would substitute the 1000 elements in a way that the predictions made with the former in terms of the total reaction vs separation are as close as possible with the exact results using the detailed model (see Fig. 17).

In this case the equivalent homogeneous parameters $\mathbf{Y}$ are the cohesive strength $T_{0}$ and ultimate separation $\delta_{0}$. Given data regarding the total traction $T_{i}$ for various separation displacements $\delta_{i}, i=1,2, \ldots, N$, the distortion function is defined as follows:

![](./images/812000232190509057_18.jpg)

Fig. 16. Sample realizations of the total traction–separation along the cohesive interface when the fracture energy at the microscale varies as in Eq. (23).

![](./images/812000232190509057_19.jpg)

Fig. 17. Rate-distortion curve when the fracture energy at the microscale varies as in Eq. (23).

$$
d(\mathbf{X}, \mathbf{Y})=\frac{1}{N} \sum_{i=1}^{N}\left(T_{i}(\mathbf{X})-T_{0}\left(\delta_{i} ; \mathbf{Y}\right)\right)^{2}
\tag{24}
$$

where
$$
T_{0}(\delta)= \begin{cases}T_{0}\left(1-\frac{\delta}{\delta_{0}}\right), & \delta \leqslant \delta_{0} \\ 0, & \delta>\delta_{0}\end{cases}
\tag{25}
$$

The arguments $\mathbf{X}$ and $\mathbf{Y}$ have been added in order to denote their implicit dependence on the detailed and homogenized microstructural properties, respectively. Since the latter depends on $T_{0}$ and $\delta_{0}$ the solution of Eq. (12) for determining the updated atom positions is a bit more involved and thus has been carried out in Appendix.

At the first iteration of the vector quantization algorithm the optimal distribution with a single atom was found at $T_{0}=1.0$ and $d_{0}=2.0$ i.e. with a fracture energy $G_{\mathrm{c}}=1.0=\mu$. The corresponding average distortion was $0.26 \times 10^{-1}$. The optimal distribution found at the last iteration is depicted in Fig. 15 in terms of the fracture energy where it is compared with the lognormal distribution of the fracture energy at the microscale (Eq. (24)). It can be seen that it is far more concentrated and although its mean is also 1 as that of $Z(x)$ its standard deviation is $0.27 \ll \sigma=1$. The shape of the distribution is also significantly different than the lognormal of the microscale details. The corresponding average distortion is $0.19 \times 10^{-3}$.

In the second case it was assumed that the strength $T_{\mathrm{c}}$ of the cohesive elements varied as in Eq. (23) and the fracture was the same for all elements $G_{\mathrm{c}}=0.5$. A few of the 1000 total traction-separation histories are shown in Fig. 18 where the large variability in the maximum traction as well as the decaying path can be easily observed. The optimal distribution found by the vector quantizer is depicted in Fig. 19 in terms of the cohesive strength and in Fig. 20 in terms of the fracture energy. It consists of 11 atoms and results in an average distortion $0.45 \times 10^{-2}$ which is significantly larger than the optimal value for the previous case. It should also be noted that the distribution for $T_{0}$ is more concentrated than the microscale lognormal, it has a mean of 1.0 and a standard deviation 0.9. As for the fracture energy the mean is 0.45 and the standard deviation 0.011.

### 3.2. Multi-cell problems

For general non-linear problems involving random microstructures, the only accurate method for determining the statistics of the response is Monte Carlo simulation. The generality of the method is a direct consequence of its conceptual simplicity i.e. one has simply to generate samples of the microstructure, solve for

![](./images/812000232190509057_20.jpg)

Fig. 18. Sample realizations of the total traction–separation along the cohesive interface when the cohesive strength at the microscale varies as in Eq. (23).

![](./images/812000232190509057_21.jpg)

Fig. 19. Scale effect – optimal distribution of the cohesive strength of an equivalent homogeneous cohesive zone when the cohesive strength at the microscale varies as in Eq. (23).

each one and process statistically the response values. Even in problems where deterministic multiscale tech- niques are available that can provide accurate estimates of the response for each microstructural sample, the repetitive calls can impose a heavy or even infeasible computational burden.

In order to address this, we divide the problem domain in several sub-domains (cells or macro-elements) and employ the upscaling technique developed in order to obtain their macroscale properties. The latter are subsequently used in order to obtain the response on the whole domain. This is schematically illustrated in Fig. 21. Conceptually the approach we propose is similar perhaps to the deterministic framework of the heterogeneous multiscale method [12] or the gap-tooth scheme [25] extended to random media and microstruc- tures. That is a microscale model is used to extract macroscale properties (such as the stiffness matrix or forces). The upscaling is performed consistently with the statistical nature of the properties of each cell in a

![](./images/812000232190509057_22.jpg)

Fig. 20. Scale effect – optimal distribution of the fracture energy of an equivalent homogeneous cohesive zone when the cohesive strength at the microscale varies as in Eq. (23).

![](./images/812000232190509057_23.jpg)

Fig. 21. Schematic illustration of microstructural upscaling in general problems.

way that minimizes the average distortion i.e. the error in the predictions with respect to macroscale behavior. The size of the cell does not depend on the random characteristics of the microstructure nor on the particulars of the governing equation. Adequate compression can be achieved for various cell sizes. In a sense the procedure proposed is also similar to the residual-free bubble method [6] where the effects of microstructure are accounted for and condensed locally at the macro-element/cell level.

The advantages are immediately obvious. If we assume that obtaining response in the original system requires the solution of a $M \times M$ system of equations which using Gaussian elimination requires operations of the order $\mathrm{O}(M^{3})$ then its solution for $N$ Monte Carlo simulations would require $\mathrm{O}(NM^{3})$ operations. If we divide the domain into $k$ sub-domains, the response of each one can be obtained by solving a system of $m \times m$ equations where $m = \frac{M}{k}$. Thus, even if $N$ simulations are used to extract the macroscale response of each sub-domain (in practice usually much smaller numbers are needed) then the total number of operations would be $\mathrm{O}(Nkm^{3})$. Hence the savings in terms of the number of operations would be of the order of $k^{2}$ (i.e. if $k = 10$

sub-domains are introduced the computations would be 100 times faster. It should be noted that the cost of solving the $k \times k$ is generally negligible for large $M$.

The critical component of course is the upscaling scheme that should able to condense the microstructural details in each sub-cell in a way that does not affect the accuracy of macroscale response. To illustrate the capabilities of the proposed methodology we consider a one-dimensional bar of unit length, unit cross-sectional area and made from an elastic-plastic material with isotropic hardening (the elastic modulus $E$ was taken equal to 1). We assume that the microscale vector $\mathbf{X}$ is 1000-dimensional and that the yield stress $\sigma_y(x)$ and hardening modulus $K(x)$ vary according to the following random fields:

$$
\sigma_{y}(x)=\sigma_{1}+\left(\sigma_{2}-\sigma_{1}\right) \Phi\left(Z_{\sigma}(x)\right), \quad x \in[0,1] \tag{26}
$$

$$
K(x)=\Phi\left(Z_{K}(x)\right), \quad x \in[0,1] \tag{27}
$$

where $Z_{\sigma}(x)$ and $Z_{K}(x)$ are zero mean, unit variance, independent Gaussian random fields with the same autocorrelation $\rho(\Delta x)=e^{-\frac{|\Delta x|}{x_{0}}}$ and $\Phi(z)$ is the standard normal cumulative distribution. The resulting random fields for $\sigma_y(x)$ and $K(x)$ are uniformly distributed in $[\sigma_1, \sigma_2]$ and $[0,1]$ respectively (the values $\sigma_1=0.3$ and $\sigma_2=0.6$ were used). It should also be noted that $K=0$ corresponds to a perfectly plastic material. The parameter $x_0$ is the correlation length and controls the length scale of heterogeneity (it was taken equal to $1/100$ in this study).

The bar was divided into $k=10$ sub-domains of equal length and we employed the upscaling methodology previously presented in order to evaluate the tangential stiffness of each bar for various elongation values. For that purpose 100 sample realizations were used in order to train the vector quantizer. The rate-distortion evolution is depicted in Fig. 22. In Fig. 23, two distributions of the tangential stiffness at various elongations are depicted. The first corresponds to average distortion 0.23 and has 2 atoms and the second to distortion of 0.00801 and has 22 atoms. The latter is in fact the optimal distribution i.e. the one that minimizes the average distortion.

These distributions for the stiffnesses of each sub-domain were subsequently used in a $10 \times 10$ system in order to predict the total reaction at the end of the bar when the latter is fixed at $x=0$ and a displacement is applied at $x=1$. The results (in terms of the histograms of the reaction at various displacements) as compared with the exact values (i.e. those obtained when solving the full 1000.1000 system as shown in Fig. 24) for the two distributions of the sub-domain stiffness depicted in Fig. 23. It is observed that the predictions made are in good agreement and markedly better for the optimal distribution. This is a testament to the quality of

![](./images/812000232190509057_24.jpg)

Fig. 22. Rate-distortion curve for each of the sub-domains of the elasto-plastic bar where the yield stress and plastic modulus vary as in Eqs. (26) and (27), respectively.

![](./images/812000232190509057_25.jpg)

Fig. 23. A sub-optimal (left) and the optimal (right) distribution of the tangential stiffness of an equivalent homogeneous sub-domain of the elasto-plastic bar where the yield stress and plastic modulus vary as in Eqs. (26) and (27), respectively.

![](./images/812000232190509057_26.jpg)

Fig. 24. A comparison of the distribution of the reaction for various elongations between the results obtained using the actual microscale model and the sub-optimal (left) and optimal (right) upscaling schemes of Fig. 23.

the upscaling scheme that was employed in each of the 10 sub-domains. It is also observed that the predictions are significantly better for larger displacements.

### 4. Conclusions

A consistent theoretical and computational framework has been presented in order to upscale random microstructural information. We employed concepts and tools from information theory in order to determine equivalent homogeneous approximations that are optimal in terms of the accuracy of the response predictions. The method proposed apart from providing the optimal upscaling scheme gives a quantitative measure of the error introduced by the compression of the microstructural data. At the core of the proposed methodology lies a very efficient vector quantization procedure based on the technique of Deterministic Annealing. The training of the vector quantizer is performed using results obtained on sub-domains either from experiments or by a deterministic legacy solver. It is envisioned that this scheme can be employed even if constitutive equations are not known in the macroscale (as for example in the equation-free models of Kevrekidis et al. [25,17]). Several applications in linear and non-linear solid mechanics have been presented. The methodology proposed can in principle be applied in various other physical systems.

### Appendix.

Let the distortion function be defined as in Eq. (24):

$$
d(\mathbf{X}, \mathbf{Y})=\frac{1}{N} \sum_{i=1}^{N}\left(T_{i}(\mathbf{X})-T\left(\delta_{i} ; \mathbf{Y}\right)\right)^{2}
\tag{28}
$$

where $T_{i}(\mathbf{X})$ denote $N$ total reaction values for separation $\delta_{i}$ and

$$
T\left(\delta_{i} ; \mathbf{Y}\right)= \begin{cases}T_{0}\left(1-\frac{\delta_{i}}{\delta_{0}}\right) & \text { if } \delta_{i} \leqslant \delta_{0} \\ 0 & \text { if } \delta_{i}>\delta_{0}\end{cases}
\tag{29}
$$

In the following we drop the arguments $\mathbf{X}$ and $\mathbf{Y}$ for notational simplicity. Suppose that the $\delta_{i}$ are ordered in ascending order and that there is $n \leqslant N$ such that: $\delta_{1} \leqslant \delta_{2} \leqslant \cdots \delta_{n} \leqslant \delta_{0} \leqslant \cdots \delta_{N}$. Then the distortion function obtains the form:

$$
d(X, Y)=\frac{1}{N} \sum_{i=1}^{n}\left(T_{i}-T\left(\delta_{i}\right)\right)^{2}+\sum_{i=n+1}^{N} T_{i}^{2}
\tag{30}
$$

The atom update Eq. (12) dictates that $\mathbf{Y}$ should be selected so that

$$
\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X}) \frac{\partial d(\mathbf{X}, \mathbf{Y})}{\partial \mathbf{Y}}=0
\tag{31}
$$

where $\mathbf{Y}=\left(T_{0}, \delta_{0}\right)$ i.e. it a two-dimensional vector. Hence in the equation above

$$
\frac{\partial d(\mathbf{X}, \mathbf{Y})}{\partial \mathbf{Y}}=\frac{2}{N} \sum_{i=1}^{n}\left(T_{i}-T\left(\delta_{i}\right)\right) \frac{\partial T_{i}}{\partial Y}
\tag{32}
$$

The gradient of $T_{i}(\delta_{i})$ with respect to $\mathbf{Y}$ is given based on Eq. (29) by

$$
\begin{aligned}
& \frac{\partial T_{i}}{\partial T_{0}}=1-\frac{\delta_{i}}{\delta_{0}} \\
& \frac{\partial T_{i}}{\partial \delta_{0}}=T_{0} \frac{\delta_{i}}{\delta_{0}^{2}}
\end{aligned}
\tag{33}
$$

It should be noted that apart apart from $T_{0}$ and $\delta_{0}$, $n$ is also an unknown. By considering the partial derivatives w.r.t. to $T_{0}$ and $\delta_{0}$ the following two equations arise:

$$
\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X})\left(a_{n}-\frac{p_{n}}{\delta_{0}}\right)=\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X}) T_{0}\left(n-2 \frac{b_{n}}{\delta_{0}}+\frac{c_{n}}{\delta_{0}^{2}}\right)
\tag{34}
$$

$$
\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X}) T_{0} \frac{p_{n}}{\delta_{0}^{2}}=\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X}) T_{0}^{2}\left(\frac{b_{n}}{\delta_{0}^{2}}-\frac{c_{n}}{\delta_{0}^{3}}\right)
\tag{35}
$$

where $a_{n}=\sum_{i=1}^{n} T_{i}, b_{n}=\sum_{i=1}^{n} \delta_{i}, c_{n}=\sum_{i=1}^{n} \delta_{i}^{2}$ and $p_{n}=\sum_{i=1}^{n} T_{i} \delta_{i}$. Let $A_{n}$ and $P_{n}$ denote the expectations of $a_{n}$ and $p_{n}$ with respect to $p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X})$ and since $\sum_{\mathbf{X}} p(\mathbf{X}) p^{*}(\mathbf{Y} / \mathbf{X})=q(\mathbf{Y})$ we have

$$
A_{n}-\frac{P_{n}}{\delta_{0}}=T_{0} q(\mathbf{Y})\left(n-2 \frac{b_{n}}{\delta_{0}}+\frac{c_{n}}{\delta_{0}^{2}}\right)
\tag{36}
$$

$$
P_{n}=T_{0} q(\mathbf{Y})\left(b_{n}-\frac{c_{n}}{\delta_{0}}\right)
\tag{37}
$$

Solution of the aforementioned equations leads to the following values:

$$
\delta_{0}=\frac{A_{n} c_{n}-P_{n} b_{n}}{P A_{n} b_{n}-n P_{n}}
\tag{38}
$$

and

$$
T_{0}=\frac{1}{q(\mathbf{Y})} \frac{A_{n}}{n-\frac{b_{n}}{\delta_{0}}}
\tag{39}
$$

It must be noted that $\delta_{0}$ above must also satisfy $\delta_{n} \leqslant \delta_{0} \leqslant \delta_{n+1}$. There is a possibility that multiple pairs of $T_{0}$ and $\delta_{0}$ satisfy the aforementioned conditions in which case the one with the least average distortion was selected.

## References

[1] G.I. Barenblatt, The mathematical theory of equilibrium of cracks in brittle fracture, Advances in Applied Mechanics 7 (1962) 55.

[2] A. Bensoussan, J.L. Lions, G. Papanicolau, Asymptotic analysis for Periodic Structures, North-Holland, amstredam, 1978.

[3] T. Berger, Rate Distortion Theory: A Mathematical Basis for Data Compression, Prentice-Hall, Inc., Engelwood Cliffs, New Jersey, 1971.

[4] R. Blahut, Computation of channel capacity and rate-distortion functions, IEEE Transactions on Information Theory 18 (4) (1972) 460.

[5] G.T. Camacho, M. Ortiz, Computational modeling of impact damage in brittle materials, International Journal of Solids and Structures 33 (20) (1996) 2899.

[6] A. Cangiani, The residual-free bubble method for problems with multiple scales, PhD thesis, St. Hughes College, Oxford University, 2004.

[7] T. Cover, J. Thomas, Elements of Information Theory, John Wiley & Sons, 1991.

[8] J. Dolbow, M.A. Khaleel, J. Mitchell, Multiscale mathematics initiative: a roadmap. Technical report, Prepared for the US Department of Energy under contract DE-AC05-76RL01830, December 2004.

[9] D.L. Donoho, High-dimensional data analysis: The curses and blessings of dimensionality, in: Mathematical Challenges of the 21st Century, University of California Los Angeles, August 7-12, 2000, American Mathematical Society.

[10] M. Dorobantu, B. Engquist, Wavelet-based numerical homogenization, SIAM Journal of Numerical Analysis 35 (2) (1998) 540.

[11] D.S. Dugdale, Yielding of steel sheets containing clits, Journal of the Mechanics and Physics of Solids 8 (1960) 100.

[12] E. Weinan, B. Engquist, The heterogeneous multi-scale methods, Communications in Mathematical Sciences 1 (2003) 87.

[13] A. Gersho, R.M. Gray, Vector Quantization and Signal compression, Kluwer Academic Publishers, 1991.

[14] T.Y. Hou, X.-H. Wu, A multiscale finite element method for elliptic problems in composite materials and porous media, Journal of Computational Physics 134 (1997) 169.

[15] T.J.R. Hughes, G.R. Feijóo, L. Mazzei, J.-B. Quincy, The variational multiscale method: a paradigm for computational mechanics, Computer Methods in Applied Mechanics and Engineering 166 (1-2) (1998) 3.

[16] A.R. Ingraffea, E. Iselulauro, K. Dodhia, P.A. Wawrzynek, A multiscale modeling approach to crack initiation in aluminum polycrystals, in: H.A. Mang, F.G. Rammerstorfer, J. Eberhardsteiner (Eds.), Proceedings of the Fifth World Congress on Computational Mechanics, Vienna, Austria, July 2002.

[17] I.G. Kevrekidis, C.W. Gear, J.M. Hyman, P.G. Kevrekidis, O. Runborg, K. Theodoropoulos, Equation-free multiscale computation: enabling microscopic simulators to perform system-level tasks, Communications in Mathematical Sciences 1 (4) (2003) 715-762.

[18] P.S. Koutsourelakis, Probabilistic characterization and simulation of multi-phase random media, Probabilistic Engineering Mechanics 21 (3) (2006) 227-234.

[19] S.P. Lloyd, Least squares quantization in pcm. Unpublished Bell Laboratories Technical Note. Published in March 1982 special issue on quantization of the IEEE Transactions on Information Theory, 1957.

[20] M. Ortiz, A. Pandolfi, Finite-deformation irreversible cohesive elements for three-dimensional crack propagation analysis, International Journal for Numerical Methods in Engineering 44 (1999) 1267.

[21] J. Planas, M. Elices, G.V. Guinea, F.J. Gómez, D.A. Cendoón, I. Arbilla, Generalizations and specializations of cohesive crack models, Engineering Fracture Mechanics 70 (2003) 1759.

[22] K. Rose, Deterministing annealing, clustering and optimization. PhD thesis, California Institute of Technology, Pasadena, CA, 1991.

[23] K. Rose, A mapping approach to rate-distortion computation and analysis, IEEE Transactions on Information Theory 40 (1994) 1939-1952.

[24] K. Rose, Deterministic annealing for clustering, compression, classification regression and related optimization problems, Proceedings of the IEEE 86 (11) (1998) 2210.

[25] G. Samaey, D. Roose, I. Kevrekidis, The gap-tooth scheme for homogenization problems, SIAM Journal on Multiscale Modeling and Simulation 4 (1) (2005) 278-306.

[26] G. Sangali, Capturing small scales in elliptic problems using a residual-free bubbles finite element method, SIAM Journal on Multiscale Modeling and Simulation 1 (3) (2003) 485.

[27] C.E. Shannon, A mathematical theory of communication, Bell System Technical Journal 27 (1948) 379-423, 623-656, July and October.

[28] C.E. Shannon, Coding theorems for a discrete source with a fidelity criterion, IRE National Convention Record 7 (4) (1959) 142-163.

[29] B. Velamur Asokan, N. Zabaras, A stochastic variational multiscale method for diffusion in heterogeneous random media, Journal of Computational Physics 218 (2) (2006) 654–676.

[30] X.P. Xu, A. Needleman, Numerical simulations of fast crack growth in brittle solids, Journal of the Mechanics and Physics of Solids 42 (1994) 1397.

[31] C.L.Y. Yeong, S. Torquato, Reconstructing random media I and II, Physical Review E 58 (1) (1998) 224–233.