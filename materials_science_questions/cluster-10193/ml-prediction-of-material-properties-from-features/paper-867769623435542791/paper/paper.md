# Critical Temperature Prediction for a Superconductor:
## A Variational Bayesian Neural Network Approach

Thanh Dung Le, *Member, IEEE*, Rita Noumeir, *Member, IEEE*, Huu Luong Quach, Ji Hyung Kim, Jung Ho Kim, and Ho Min Kim, *Member, IEEE*

**Abstract**—Much research in recent years has focused on using empirical machine learning approaches to extract useful insights on the structure-property relationships of superconductor material. Notably, these approaches are bringing extreme benefits when superconductivity data often come from costly and arduously experimental work. However, this assessment cannot be based solely on an open black-box machine learning, which is not fully interpretable, because it can be counter-intuitive to understand why the model may give an appropriate response to a set of input data for superconductivity characteristic analyses, e.g., critical temperature. The purpose of this study is to describe and examine an alternative approach for predicting the superconducting transition temperature $T_c$ from SuperCon database obtained by Japan's National Institute for Materials Science. We address a generative machine-learning framework called Variational Bayesian Neural Network using superconductors chemical elements and formula to predict $T_c$. In such a context, the importance of the paper in focus is twofold. First, to improve the interpretability, we adopt a variational inference to approximate the distribution in latent parameter space for the generative model. It statistically captures the mutual correlation of superconductor compounds and; then, gives the estimation for the $T_c$. Second, a stochastic optimization algorithm, which embraces a statistical inference named Monte Carlo sampler, is utilized to optimally approximate the proposed inference model, ultimately determine and evaluate the predictive performance. As a result, in comparison with the standard evaluation metrics, the results are promising and also agree with the existing models prevalent in the field. The $R^2$ value obtained is very close to the best model (0.94), whereas a considerable improvement is seen in the RMSE value (3.83 K). Notably, the proposed model is known as the first of its kind for predicting a superconductor's $T_c$.

**Index Terms**—Critical transition temperature, machine learning, Bayesian neural network, variational inference, stochastic optimization algorithm, high temperature superconducting (HTS).

## I. INTRODUCTION

THE generality of machine learning (ML) in material science is increasingly being adopted to discover hidden trends in data and make predictions. Mainly, there are guidance and perspectives when applying ML techniques as a robust protocol to maintain both quantitatively and qualitatively predictive models [1]; impacts of ML technologies on materials, process and structures engineering are likely transformational for advancing new solutions to the long-standing data structure challenge [2]; reliable and explainable ML models from underrepresented materials data provide both model-level and decision-level explanations [3]. Besides, there are also wide ranges of ML applications in material data science, such as illustrative examples of a taxonomy of ML capabilities in soft mater, and data-driven materials design engines [4].

In superconductivity, machine learning-guided iterative experimentation may outperform standard high-throughput screening for discovering breakthrough materials in high temperature (high-$T_c$) superconductors, e.g., a new measure of machine learning model performance in high-$T_c$ by improving the cross-validation with a single neural network [5], empirical analyses for critical current measurement by developing machine learning tool in classification and regression tasks for SuperCon database [6]. These studies confirm that the framework for making machine-based decisions and actions using ML analysis has dominated the predictive models. However, there are growing concern steps for attaining autonomous prediction that require at least three concurrently operating technologies: i) making analyses by endorsing perception of information, ii) predicting the sensed field changing over time, and iii) establishing a policy for a machine to take unsupervised action.

To address the challenges, we describe an alternative ML approach called the generative neural network model. Also, Bayesian-based generative model prediction is advantageous for the two most important reasons: i) uncertainty is intrinsically described, useful for analysis, and prediction, ii) overfitting is avoided by natural penalization of overly complicated models. In this work, we develop the probabilistic high-$T_c$ predictive model using Variational Bayesian Neural Network (VBNN) regression provided by Drugowitsch [7] and build upon the efficient optimization algorithm for learning optimal learnable parameters in the VBNN. In particular, we exploit the Stochastic Gradient Variational Bayes (SGVB) optimization algorithm introduced in [8]. The learning algorithm provides the probability that latent correlation of parameters in superconductors chemical characteristics in drawing the $T_c$ prediction, instead of a fixed linear regression with uncertainty.

The rest of this paper is organized as follows. Section II discusses strength, weaknesses, and achievements of the related work, and Section III presents the mathematical un-

Manuscript received Sep 24, 2019; accepted Jan 29, 2020. Date of publication Jan 29, 2020; date of current version Jan 29, 2020. The author (T. D. Le) acknowledges the financial support of the Canada First Research Excellence Fund (CFREF) program through IVADO, and the Doctoral Scholarship for International Student from Le Fonds de Recherche du Quebec Nature et technologies (FRQNT).

T. D. Le and R. Noumeir are with the Biomedical Information Processing Lab, Ecole de Technologie Superieure, Montreal, QC H3C 1K3, Canada (Corresponding email: thanh-dung.le@etsmtl.ca).

H. L. Quach, J. H. Kim, and H. M. Kim are with the Applied Superconducting Lab, Jeju National University, Jeju-si 690-756, S. Korea (Email: {qhuong, jihkim, hmkim}@jejunu.ac.kr).

J. H. Kim is with the Institute for Superconducting & Electronic Materials, Australian Institute of Innovative Materials, University of Wollongong, Wollongong NSW 2522, Australia (Email: jhk@uow.edu.au).

Consequently, the proposed approach provides a more comprehensive and realistic picture of ML model performance in material discovery applications. Mainly, it can outperform deep learning approaches, from the study [13] and [14], which are claimed to be failed because of their function distributions of low cross-predictability with a descent algorithm [15].

## III. MODEL AND PRELIMINARIES

### A. Bayesian Linear Regression Model

Let us start with a simple linear regression function to approximate a true generating function such that:
$$
y_{i}=\mathbf{w}^{T} \mathbf{x}_{i}+\epsilon_{i} \tag{1}
$$
where the response $y_{i}$ is a linear function of the covariate $x_{i} \in \mathcal{R}^{D}$ and is linear in the parameters $w$, additional bias $\epsilon$ as well. Collecting $I$ response variable $Y, \epsilon \in \mathcal{R}^{I}$ we have:
$$
Y=X W+\epsilon \tag{2}
$$
where $X \in \mathcal{R}^{I \times D}, W \in \mathcal{R}^{D \times N}$ is referred to as the design matrix and weight matrix, respectively. The weight matrix is assumed the only parameter $\theta=\{W\}$. Then, the empirical cost function is as follows:
$$
\tilde{C}(\theta)=\frac{1}{N} \sum_{i=1}^{N} \frac{1}{2}\left\|y_{i}-W^{T} x_{i}\right\|_{2}^{2} \tag{3}
$$

The gradient is calculated then to find the minimum of empirical cost function from Eq. 3, by the following expression:
$$
\nabla \tilde{C}(\theta)=-\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-W^{T} x_{i}\right)^{T} x_{i} \tag{4}
$$

We can use Eq. 3 and 4 with an iterative optimization algorithm, such as gradient descent or stochastic gradient descent, to find the best $W$ that minimizes the empirical cost function, as in the study [12]. Even though a better option is to use a validation set that can stop the optimization algorithm when the minimal validation cost function is reached. However, these methods demand clarification of a linear network because:
- First, there is no guarantee whether the real generating function $f$ is a linear function. If it is not, the linear regression model cannot be expected to approximate the true function well.
- Second, there is not much control over what expectations to measure the given input data $x$. Therefore, how well $x$ represents the input remains unclear.

Now, given a training set $\mathcal{D}=\{X, Y\}$, estimate $w$ so that the response $y^{*}$ to a new data point $x^{*}$ can be predicted by calculating the expectation $\mathbb{E}\left[y^{*} \mid x^{*}\right]$ as given $\mathbb{E}\left[y^{*} \mid x^{*}\right]=w^{T} x^{*}$. To do that, we develop a probabilistic graphical model of the Bayesian linear regression model. Then, our target finds the likelihood function for $w$ and the prior over $w$, which is given by [7]:
$$
p(\mathbf{y} \mid \mathbf{X}, \mathbf{w})=\prod_{i=1}^{I} \mathcal{N}\left(y_{i} \mid \mathbf{w}^{T} \mathbf{x}_{i}, \lambda^{-1}\right) \tag{5}
$$
where, $\lambda$ is the noise precision parameter and is assumed to be known for simplicity. Thus, the joint distribution over all the variables is given by the following factorization.
$$
p(\mathbf{y}, \mathbf{w} \mid \mathbf{X})=p(\mathbf{y} \mid \mathbf{X}, \mathbf{w}) p(\mathbf{w}) \tag{6}
$$

The whole procedure of learning given by Eq. 6 is a process of searching for the best *hypothesis* over the entire space $\mathcal{H}$ of hypotheses. It is assumed that each hypothesis corresponds to each possible function with a unique set of parameters and a unique functional form, and that hypothesis only takes the input $x$ and the output $y$.

### B. Variational Inference for Bayesian Neural Network

We can re-write Eq. 6 again with the only parameter $\theta$ for the weight matrix $W$ as the following equation. Then, the posterior inference over $w$ given by Eq. 7 is often intractable, especially, because of the divisor.
$$
p_{\theta}(w \mid x)=\frac{p_{\theta}(x \mid w) p(w)}{p_{\theta}(x)}=\frac{p_{\theta}(w, x)}{p_{\theta}(x)}=\frac{p_{\theta}(w, x)}{\int_{w} p_{\theta}(x, w)} \tag{7}
$$

Therefore, we assume that there is a tractable family of distribution $Q$, which is similar to $p_{\theta}(x \mid w)$. Then, we try to find an approximate posterior inference using $q_{\phi}\left(q_{\phi} \in Q\right)$. Hence, the optimization objective must measure the similarity between $p_{\theta}$ and $q_{\phi}$. To capture this, we use the Kullback-Leibler (KL) divergence as given by:
$$
\operatorname{KL}\left(q_{\phi} \| p_{\theta}\right)=\int_{w} q_{\phi}(w \mid x) \log \frac{q_{\phi}(w \mid x)}{p_{\theta}(w \mid x)} \tag{8}
$$

Because we cannot minimize the KL-Divergence directly, we have isolated the intractable evidence term in KL-Divergence:
$$
\begin{aligned}
\operatorname{KL}\left(q_{\phi} \| p_{\theta}\right) &=\left(\mathbb{E}_{q_{\phi}} \log \frac{q_{\phi}(w \mid x)}{p_{\theta}(w, x)}\right)+\log p_{\theta}(x) \\
&=-\mathcal{L}(x ; \theta, \phi)+\log p_{\theta}(x)
\end{aligned} \tag{9}
$$

Then, let's us rearrange terms to express isolated intractable evidence:
$$
\log p_{\theta}(x)=\operatorname{KL}\left(q_{\phi} \| p_{\theta}\right)+\mathcal{L}(x ; \theta, \phi)
$$

Furthermore, KL-Divergence is non-negative, it is easily to expressed as follows:
$$
\begin{gathered}
\log p_{\theta}(x)=\operatorname{KL}\left(q_{\phi} \| p_{\theta}\right)+\mathcal{L}(x ; \theta, \phi) \\
\log p_{\theta}(x) \geq \mathcal{L}(x ; \theta, \phi)
\end{gathered}
$$
where
$$
\mathcal{L}(x ; \theta, \phi)=-\mathbb{E}_{q_{\phi}} \log \frac{q_{\phi}(w \mid x)}{p_{\theta}(w, x)} \tag{10}
$$

The Eq. 10 is also called the Evidence Lower Bound (ELBO). Let's us expand the derived variational lower bound, we will have then:
$$
\begin{aligned}
\mathcal{L}(x ; \theta, \phi) &=-\mathbb{E}_{q_{\phi}}\left[\log \frac{q_{\phi}(w \mid x)}{p_{\theta}(w, x)}\right] \\
&=\mathbb{E}_{q_{\phi}}\left[\log p_{\theta}(x \mid w)+\log p(w)-\log q_{\phi}(w \mid x)\right]
\end{aligned}
$$
```

### C. Optimization
The objective is to optimize the ELBO for the derived inference model, or it can be restated as the following equation:
$$
\mathcal{L}(x ; \theta, \phi)=\underbrace{\mathbb{E}_{q_{\phi}}\left[\log p_{\theta}(x | w)\right]}_{\text {Reconstruction likelihood }}-\underbrace{\mathrm{KL}\left(q_{\phi}(w | x) \| p(w)\right)}_{\text {divergence from prior }} \quad(11)
$$

Then, the gradients $\nabla_{\theta} \mathcal{L}$ and $\nabla_{\phi} \mathcal{L}$ need to be computed. To achieve that, we apply the Stochastic Gradient Variational Bayes (SGVB) approach given by [8]. Technically, the key of SGVB estimator is a reparameterization trick, i.e., they reparameterize the random variable, as given:
$$
w \sim q_{\phi}(w | x)=\mathcal{N}\left(w | \mu_{w}(x ; \phi), \sigma_{w}^{2}(x ; \phi)\right)
$$
as
$$
w=w(\epsilon ; x, \phi)=\epsilon \sigma_{w}(x ; \phi)+\mu_{w}(x ; \phi), \epsilon \sim \mathcal{N}(0, I)
$$

Then, the expectation can be written with respect to $\epsilon$:
$$
\begin{aligned}
\mathcal{L}(\phi, \theta)=\mathbb{E}_{w \sim q_{\phi}(w | x)} & {\left[\log p_{\theta}(x, w)-\log q_{\phi}(w | x)\right] } \\
=\mathbb{E}_{\epsilon \sim N(0, I)}[ & \log p_{\theta}(x, w(\epsilon ; x, \phi)) \\
& \left.-\log q_{\phi}(w(\epsilon ; x, \phi) | x)\right]
\end{aligned}
$$

Consequently, the gradient with variational parameter $\phi$ can be directly moved into the expectation, enabling an unbiased low variance Monte Carlo estimator:
$$
\begin{aligned}
\nabla_{\phi} L(\phi, \theta)=\mathbb{E}_{\epsilon \sim \mathbb{N}(0, I)} \nabla_{\phi}[ & \log p_{\theta}(x, w(\epsilon ; x, \phi)) \\
& \left.-\log q_{\phi}(w(\epsilon ; x, \phi) | x)\right] \\
\approx \frac{1}{k} \sum_{i=1}^{k} \nabla_{\phi}[ & \log p_{\theta}\left(x, w\left(\epsilon_{i} ; x, \phi\right)\right) \\
& \left.-\log q_{\phi}\left(w\left(\epsilon_{i} ; x, \phi\right) | x\right)\right]
\end{aligned}
$$
where $\epsilon_{i} \sim \mathcal{N}(0, I)$

### IV. CRITICAL TEMPERATURE PREDICTIVE MODEL

#### A. High-Tc Data
Although there are many public data available for superconductors [9], [10], the present study used only the SuperCon database. We will restate the refined data from the study [11] because of significant reasons. First, the material investigated is a Standardized Data for Typical Oxide High-$T_c$ materials; all preparation, characterization is captured with i) larger amount dataset, ii) a more substantial number of features from elemental properties, iii) freely available access for everyone, and iv) compatibility as a performance benchmark. Besides, we can assess the importance of the features, which are based on thermal conductivity, atomic radius, valence, electron affinity, and atomic mass in prediction accuracy for $T_c$.

Studies [6], [11]–[14] also create a model to predict $T_c$ from the SuperCon data. Our approach is different from those studies in the following ways: (i) We use generative neural network as illustrated in Fig. 1, that probabilistic analyses and statistical learning theories are utilized to tune the learnable hyper-parameters, and (ii) most importantly, the model promises to discover rich structure (latent and distributional formation) in superconductor's chemical formula data while generating realistic data distribution from a latent code space. Then, the nature of the relationship between the features and $T_c$ can be statistically inferred from the model.

![](./images/867769623435542791_1.jpg)

Fig. 1. Probabilistic graphical model of the VBNN model to predict $T_c$.

### B. High-Tc Prediction
The model, in previous section III, have been defined to infer the parameters. Next, the main target is to predict about new data. As consequence, the probability distribution of new data $y=T_c$ given its input feature $x$ and our training data $D$ is defined as follows:
$$
p(y | x, D)=\int_{w} p(y | x, w) p(w | D)
$$

Because we have learned the approximation of $p_{\theta}(w | D)$ by the variational $q_{\phi}(w)$ in Eq. 11. Therefore, we can use the Monte Carlo estimation to get an unbiased estimate of it by sampling from the variational posterior as given by:
$$
p(y | x, D) \simeq \frac{1}{M} \sum_{i=1}^{M} p\left(y | x, w\right)
$$

As a result, the prediction for new superconductor data is the mean of the predictive distribution as expressed by:
$$
\hat{y}=\mathbb{E}_{p(y | x, D)} y \simeq \frac{1}{M} \sum_{i=1}^{M} \mathbb{E}_{p(y | x, w)} y \tag{12}
$$

### C. Predictive Model Evaluation
The most common technique for model validation is RMSE, $R^2$ and log-likelihood. RMSE is the square root of the predictive mean square error, and the smaller RMSE means, the better predictive accuracy is:
$$
R M S E=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(\hat{y}_{i}-y_{i}\right)^{2}} \tag{13}
$$

$R^2$ values are commonly expressed as percentages from 0% to 100% (or its values range from 0 to 1). It approximates how well the model's input can explain the observed variation.
$$
R^{2}=1-\frac{\sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)^{2}}{\sum_{i=1}^{N}\left(y_{i}-\bar{y}_{i}\right)^{2}} \tag{14}
$$

<table>
<caption>TABLE I Numerical Result Comparison</caption>
<thead>
<tr>
<th>ML Approaches</th>
<th>$R^2$</th>
<th>RMSE (K)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Random Forest [6]</td>
<td>0.85</td>
<td>N/A</td>
</tr>
<tr>
<td>Random Forest & XGboost [11]</td>
<td>0.74</td>
<td>17.6</td>
</tr>
<tr>
<td>Support Vector Machine [12]</td>
<td>0.96</td>
<td>N/A</td>
</tr>
<tr>
<td>Convolutional Neural Network [13]</td>
<td>0.93</td>
<td>N/A</td>
</tr>
<tr>
<td>Atom Table Convolutional Neural Network [14]</td>
<td>0.97</td>
<td>8.14</td>
</tr>
<tr>
<td>Variational Bayesian Neural Network</td>
<td>0.94</td>
<td>3.83</td>
</tr>
</tbody>
</table>

## V. NUMERICAL RESULTS AND DISCUSSIONS

For the implementation, we use the Python-based Bayesian deep learning library [16]. Then, the predictive model training and testing are executed by using the Tensorflow on an NVIDIA Tesla k80 GPU. There is no need for the validation set to explore the effect of VBNN on overcoming the overfitting challenge, then the dataset is solely divided into 30%, 70% for test-set and train-set, respectively. Practically, it is problematic to determine a good network topology just from the number of inputs and outputs. Because accuracy is the main criteria for designing the VBNN, the hidden layers can be increased [17]. In general, the neural network models improve with more epochs of training, and the accuracy remains stable as they converge [18]. And, the larger batch sizes result in faster progress in training but do not always converge as fast. In contrast, the smaller batch sizes train slower but can converge faster [19]. Besides, averaging over a multiplicity batch of 10 is going to produce a gradient that is a more reasonable approximation of the full batch-mode gradient. As a consequence, the experiment converged with the running of 1000 epochs, the batch size of 10, and 100 hidden layers. For the reproducible analysis, predictions and evaluations, the implementation code and results are available at GitHub repository (https://github.com/ltdung/VBNN_HighTc).

The presented Bayesian regression approach can also directly be applied to predict the critical temperature of a superconductor, as shown in Table I. Our confidence scores $R^2$ have strong overall concordance with previous predictions ($R^2=0.94$). Besides, a significant improvement was obtained in the RMSE at 3.83 K. The result is a striking illustration of VBNN performance compared with other techniques. In short, to the knowledge of the authors, the generative approach for superconductors $T_c$ prediction is the first of its kind. Our results are encouraging; however, reproducibility of replicated experiments should be conducted for worthy investigations:

- First, an important question for future studies is to use the pre-trained VBNN predictive model to validate its performance on different superconductor datasets. Possible directions are customizing the “transfer learning” paradigm to take advantages of the optimized hyperparameters from the VBNN neural network.
- Second, future work should focus on exploring feasible compounds as a new superconductor. It will be beneficial in having an initial feedback to determine the correctness and efficiency of alternative compounds before conducting costly, effortfully experiments in real practice.

## VI. CONCLUSION

The material data science, specifically in superconductor exploring, is in the early stages of ML adoption. There is a growing number of single-use applications, but more intelligible models are yet to be seen. In this work, we developed a new probabilistic approach using variational Bayesian neural network for estimating the $T_c$ value of high-temperature superconductors. Our results are in general agreement with existing studies in $T_c$ predictive model. These preliminary results demonstrate the feasibility of using generative neural network, which provides compelling, helpful evidence to understand the underlying superconductivity physics. This finding is promising and should be investigated with other advanced predictive models, which could eventually lead to the discovery of new superconductors in future.

## REFERENCES

[1] N. Wagner and J. M. Rondinelli, “Theory-guided machine learning in materials science,” *Frontiers in Materials*, vol. 3, p. 28, 2016.

[2] D. M. Dimiduk *et al.*, “Perspectives on the impact of machine learning, deep learning, and artificial intelligence on materials, processes, and structures engineering,” *Integrating Materials and Manufacturing Innovation*, pp. 1–16, 2018.

[3] B. Kaikhura *et al.*, “Reliable and explainable machine learning methods for accelerated material discovery,” *arXiv preprint arXiv:1901.02717*, 2019.

[4] A. L. Ferguson, “Machine learning and data science in soft materials engineering,” *Journal of Physics: Condensed Matter*, vol. 30, no. 4, p. 043002, 2017.

[5] B. Meredig *et al.*, “Can machine learning identify the next high-temperature superconductor? examining extrapolation performance for materials discovery,” *Molecular Systems Design & Engineering*, vol. 3, no. 5, pp. 819–825, 2018.

[6] V. Stanev *et al.*, “Machine learning modeling of superconducting critical temperature,” *NPJ Computational Materials*, vol. 4, no. 1, p. 29, 2018.

[7] J. Drugowitsch, “Variational bayesian inference for linear and logistic regression,” *arXiv preprint arXiv:1310.5438*, 2013.

[8] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” *arXiv preprint arXiv:1312.6114*, 2013.

[9] S. C. Wimbush and N. M. Strickland, “A public database of high-temperature superconductor critical current data,” *IEEE Transactions on Applied Superconductivity*, vol. 27, no. 4, pp. 1–5, 2016.

[10] Japan’s National Institute for Materials Science, *Superconducting Material Database (SuperCon)*, 2019 (accessed February 3, 2019). [Online]. Available: https://supercon.nims.go.jp/index_en.html

[11] K. Hamidieh, “A data-driven statistical model for predicting the critical temperature of a superconductor,” *Computational Materials Science*, vol. 154, pp. 346–354, 2018.

[12] T. O. Owolabi *et al.*, “Application of computational intelligence technique for estimating superconducting transition temperature of YBCO superconductors,” *Applied Soft Computing*, vol. 43, pp. 143–149, 2016.

[13] T. Konno *et al.*, “Deep learning of superconductors I: Estimation of critical temperature of superconductor toward the search for new materials,” *arXiv preprint arXiv:1812.01995*, 2018.

[14] S. Zeng *et al.*, “Atom table convolutional neural networks for an accurate prediction of compounds properties,” *NPJ Computational Materials*, vol. 5, no. 1, pp. 1–7, 2019.

[15] E. Abbe and C. Sandon, “Provable limitations of deep learning,” *arXiv preprint arXiv:1812.06369*, 2019.

[16] J. Shi *et al.*, “ZhuSuan: A library for Bayesian deep learning,” *arXiv preprint arXiv:1709.05870*, 2017.

[17] K. G. Sheela and S. N. Deepa, “Review on methods to fix number of hidden neurons in neural networks,” *Mathematical Problems in Engineering*, vol. 2013, 2013.

[18] E. Hoffer, I. Hubara, and D. Soudry, “Train longer, generalize better: closing the generalization gap in large batch training of neural networks,” in *Advances in Neural Information Processing Systems*, 2017, pp. 1731–1741.

[19] L. Chen *et al.*, “The effect of network width on the performance of large-batch training,” in *Advances in Neural Information Processing Systems*, 2018, pp. 9302–9309.