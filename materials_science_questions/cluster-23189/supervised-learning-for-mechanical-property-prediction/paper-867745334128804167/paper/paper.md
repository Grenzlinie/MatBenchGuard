# IN SILICO PREDICTION OF CELL TRACTION FORCES

Nicolas Pielawski\*, Jianjiang Hu°, Staffan Strömblad°,Carolina Wählby\*

\*Uppsala University, Dept. of Information Technology, Lägerhyddsvägen 2, 752 37 Uppsala
°Karolinska Institutet, Department of Biosciences and Nutrition, Hälsovägen 7C, 141 57 Huddinge

## ABSTRACT
Traction Force Microscopy (TFM) is a technique used to determine the tensions that a biological cell conveys to the underlying surface. Typically, TFM requires culturing cells on gels with fluorescent beads, followed by bead displacement calculations. We present a new method allowing to predict those forces from a regular fluorescent image of the cell. Using Deep Learning, we trained a Bayesian Neural Network adapted for pixel regression of the forces and show that it generalises on different cells of the same strain. The predicted forces are computed along with an approximated uncertainty, which shows whether the prediction is trustworthy or not. Using the proposed method could help estimating forces when calculating non-trivial bead displacements and can also free one of the fluorescent channels of the microscope. Code is available at https://github.com/wahlby-lab/InSilicoTFM.

Index Terms— Traction Force Microscopy, Deep Learning, Regression, Uncertainty, Bayesian Neural Network

## 1. INTRODUCTION
In 1999, Dembo et al. developed a new technique named Traction Force Microscopy and made possible the visualisation of cellular forces by placing cells on a soft gel containing randomly placed fluorescent beads[1]. Using this technique, they could retrieve the displacement of the beads and generate a vector field representing the local forces, with their magnitude and direction. Traction Forces are often used in studies of cell migration patterns; it has been hypothesised that cancer cells exhibiting high traction forces are more invasive than cells with lower activity [2].

In 2010, Lemmon et al.[3] – on the basis that the shape and size of a cell correlates with the amount of forces it exerts on the substrate – described a method allowing the prediction of traction forces based solely on the cell geometry.

In recent years, neural networks gained popularity in research in biology mainly due to their successful application to various problems as well as the availability of computing capacity to train them. In 2015, Ronneberger et al.[4] proposed a new type of neural network architecture: the U-Net. It contains a down-sampling path working on feature maps of decreasing resolutions and followed by an up-sampling path that constructs the output image. Both paths are connected with skip-connections that allow information to flow through the network. In 2017, Jégou et al. built upon the U-Net architecture to create the Tiramisu neural network[5]. Adding various improvements, such as the dense blocks from the DenseNet neural network by Huang et al.[6], they could improve the performances of the U-Net architecture while substantially reducing the number of trainable weights.

The insight from the method by Lemmon et al.[3], combined with a neural network able to use the structural information of a cell at different scales such as the Tiramisu network, offers an opportunity to translate a fluorescent image of a cell into an image estimating traction forces. To the best of our knowledge, this paper describes the first attempt at using deep neural networks to predict cell traction forces.

This paper describe the process that leads to the creation of the data, the construction of the deep neural network to predict the cellular forces and the measurement of the uncertainty around the prediction of the neural network.

## 2. MATERIAL AND METHODS
### 2.1. Image data
Immortalised human fibrosarcoma cell line HT1080 stably expressing a FRET based RhoA biosensor[7] was used in this study. The cells were seeded on collagen type I coated with red fluorescent beads (Invitrogen, F8801) containing polyacrylamide gel (6.9 kPa) three hours before the imaging started. An environmental chamber equipped with a Nikon A1 confocal microscope with 60x oil objective (NA 1.4) was used to image single-cell migration and displacements of the fluorescent beads at a resolution of 200 nm/pixel and a time interval of 30 seconds for 1.5 hours. 457 nm and 561 nm lasers were used to excite the FRET biosensor and red fluorescent beads respectively, while 525/50 and 595/50 emission filters were used to collect the signals. After the time-lapse imaging, cells were trypsinized and single snapshots of fluorescent beads were collected to get the positions of the beads at the released state. MATLAB R2014b with the traction

Thanks to the Swedish Foundation for Strategic Research for funding (grant SB16-0046).

![](./images/867745334128804167_1.jpg)

Fig. 1. Example raw images fed to the neural network (top row), the ground truth (middle row), and the predicted forces (bottom row) of the test cell over a time series. The orange crosses represent the pixel chosen for generating figure 3. The full sequence – the ground-truth force overlapped with the prediction of the test cell – is available at https://youtu.be/QhzNmrA42T4.

force microscopy package from Danuser Lab. [8] was used to calculate the traction force based on the bead displacements.

Two datasets were generated in this fashion at two different occasions and are available on Zenodo[9]. The first dataset (12 cells) was used for training and the second one (11 cells, and 1 test cell) for validation purposes. The last cell from the validation dataset was taken out to generate the figures and will be called test cell.

### 2.2. Deep Learning Model
We modified a Tiramisu segmentation neural network[5] – A U-Net architecture made of Dense blocks from the DenseNet architecture – in order to predict forces and their uncertainties.

The last layer has been replaced by two fully connected layers in order to predict the mean and the variance (aleatoric uncertainty) of the estimated forces. The mean forces have no activation function (linear activation) while the variance has a softplus activation squared: $\ln(1+\exp(x))^2$. The weights of the neural networks are initialised with a Glorot normal distribution except for the variance layer, which is initialised with zeros for the kernels, and $\ln(e-1)$ for the biases, so that the variance is 1 at the beginning of the training.

The drop-out layers have been modified so that they are active during training as well as during inference, in order to predict the epistemic uncertainty. The rate of drop-out is 20% throughout.

The architecture consists of six dense blocks, with five layers per block and a growth rate of 16. The first initial filter has a size of 3x3 and a depth of 48. In the expansive path of the neural network, at each level, the feature maps are up-sampled by a factor of two without interpolation followed by 2-D convolutions with a depth of 128 filters. The Adam optimiser is used with L-2 weight decay of $10^{-4}$ and gradient clipping (maximum L-2 norm of 1.0).

The model was trained on four Titan Xp graphic cards over 200 epochs, with 50 steps per epoch and a batch size of 8, so that each GPU deals with two images at a time.

#### 2.2.1. Loss functions
The Kullback-Leibler (KL) divergence measures the relative entropy between two probability distributions. Training a neural network by Maximum Likelihood Estimation (MLE) is analogous to minimising the KL divergence. Because the log of the data is normally distributed, we used the KL divergence between two log-Normal distributions that yields the following loss function[10]:

$$
\begin{aligned}
\mathcal{L}_{\mathrm{MSE}}(\boldsymbol{\mu}, \hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\sigma}}^{\mathbf{2}}) &= D_{K L}(\ln \mathcal{N}(\boldsymbol{\mu}, 0)|| \ln \mathcal{N}(\hat{\boldsymbol{\mu}}, \boldsymbol{I}_{\boldsymbol{n}} \hat{\boldsymbol{\sigma}}^{\mathbf{2}})) \\
& \propto \frac{1}{n} \sum_{i=0}^{n}\left(\frac{1}{2 \hat{\sigma}_{i}^{2}}|| \mu_{i}-\hat{\mu}_{i}||^{2}+\frac{1}{2} \ln \hat{\sigma}_{i}^{2}\right) \quad (1)
\end{aligned}
$$

with $n$ the number of data points, $\boldsymbol{\mu}$ the ground truth, $\hat{\boldsymbol{\mu}}$ the prediction, $\hat{\boldsymbol{\sigma}}^{\mathbf{2}}$ the predicted uncertainty, and assuming we have no uncertainty on the ground-truth.

This loss function is the mean squared error loss that would be derived from the KL divergence between two normal distributions. Due to the properties of the log-normal distribution, the ground-truth data needs to be log-transformed and the trained neural network will yield log-forces.

### 2.3. Image augmentation
Construction of the forces based on the bead displacement creates high intensity artefacts close to the borders. To cope with this unwanted behaviour all images of forces were masked with a 2-dimensional 10% cosine-tapered (Tukey) window[11].

![](./images/867745334128804167_2.jpg)

Fig. 2. The test cell at time 4320s. The raw data represents the data that was fed to the neural network. The remaining images have been generated from the output of the neural network. The full time sequence is available at: https://youtu.be/U9-Tn9ojXAU.

The construction of the batches follows a pipeline with three distinct steps. First, because the images are composed of mainly background, we extracted the cells from the images by thresholding them. A morphological closing and opening were applied sequentially with a box kernel of size 5x5. A bounding box was then fitted around the biggest blob available. In the second step, the images were flipped horizontally then vertically with a probability of 50%. Resulting images were randomly rotated with a bi-cubic interpolation and randomly cropped to create uniform batches of size 256x256. Salt noise was added over 1% of the pixels of 50% of the input images, with a random intensity sampled from a uniform distribution ($a=0, b=2000$). This increased the robustness of the neural network towards sparse noise of potential high intensity. The final step consisted of log-transforming the resulting images with the clipped log function: $\ln(\max(1, x))$.

### 2.4. Measure of the uncertainty of the predictions

Measuring uncertainty is an important factor of this study, as it adds another dimension to the understanding of the output of the neural network. Indeed, allowing users to know whether a prediction can be trusted, and to which extent, can be useful for further research. For instance, it becomes possible to select images that reach only a specific certainty, or even perform statistical testing.

#### 2.4.1. Aleatoric and Epistemic uncertainties

The aleatoric and epistemic are two different ways to communicate about uncertainties. The former can be quantified in closed form and provides an uncertainty related to the lack of information in the input data, whereas the latter needs to be approximated and yields information about the lack of agreement within the model. The approximation of the epistemic uncertainty was achieved using the Monte Carlo drop-out method as described by Kendall et al. in [12], with some modifications to accommodate for the log-normal distribution.

![](./images/867745334128804167_3.jpg)

Fig. 3. Ground-truth and predicted force of an arbitrary pixel (displayed as an orange cross in figure 1). Blue regions represent prediction confidence intervals, and entropy is displayed as a dashed line.

Given that a neural network $t$ has the ability to formulate a prediction $\mu_t$ and aleatoric uncertainty $\sigma_t^2$, the force can be

computed as follows:

$$
\mathbb{E}[\hat{y}_{i}|x_{i}^{*}, \mathbf{X}] \approx \frac{1}{T} \sum_{t=1}^{T} \exp(\mu_t + \sigma_t^2/2) \tag{2}
$$

for a given pixel $x_i^*$ and input image $\mathbf{X}$, and $T$ sampled neural networks where the weights are sampled from a drop-out distribution.

Accordingly, the full prediction variance is derived as:

$$
\begin{aligned}
\mathbb{V}[\hat{y}_{i}|x_{i}^{*}, \mathbf{X}] &\approx \frac{1}{T} \sum_{t=1}^{T}\big(\exp(2\mu_t + \sigma_t^2)(\exp(\sigma_t^2)-1)+ \\
&\quad \frac{1}{T} \sum_{t=1}^{T} \exp(\mu_t + \sigma_t^2/2)^2 - \mathbb{E}[\hat{y}_{i}|x_{i}^{*}, \mathbf{X}]^2 \tag{3}
\end{aligned}
$$

This variance is a sum consisting of both the aleatoric and the epistemic uncertainties, respectively.

### 2.4.2. Coefficient of Variation

The coefficient of variation is derived by dividing the standard deviation by the mean:

$$
CV[\hat{y}_{i}|x_{i}^{*}, \mathbf{X}] \approx \frac{1}{T} \sum_{t=1}^{T} \sqrt{\exp \sigma_t^2 - 1} \tag{4}
$$

and gives information about the amount of uncertainty in relation to the intensity of the force, even though the formula does not take the parameter $\mu$ into account.

### 2.4.3. Differential Entropy

The entropy of a log-normal distribution is defined in Kvalseth [13], and can be approximated in the following way:

$$
\mathbb{H}[\hat{y}_{i}|x_{i}^{*}, \mathbf{X}] \approx \frac{1}{T} \sum_{t=1}^{T} \log_2(\sigma_t \exp(\mu_t + \frac{1}{2})/\sqrt{2\pi}) \tag{5}
$$

and yields the predictive entropy of the neural network. This method, used by Nair et al. "is a measure of how much information is in the model predictive density function at each [pixel] $i$"[14]. This measure reveals the relative number of bits missing from each individual log-normally distributed pixel.

## 3. RESULTS

The neural network was evaluated on the validation set; the test set was used for illustration purposes only, the validation set was not used for hyper-parameter optimisation in order to avoid a possible human bias.

Figure 1 shows the predicted forces of the test cell over time. A small orange cross represents a pixel chosen arbitrarily to generate Figure 3.

![](./images/867745334128804167_4.jpg)

Fig. 4. Mean Absolute Error (MAE) of the training, validation and test sets for each individual frame. The standard deviation represents the spread around the mean for the training set (12 cells) and the validation set (11 cells).

Figure 3 represents the prediction of the forces compared to the ground-truth. The log-normal distribution percent-point (quantile) function was used to generate confidence intervals.

Figure 4 displays the Mean-Absolute Error over the time sequence of the cells (181 frames) for each of the sets. The sets were not augmented, the 10% Tukey mask was still applied to the forces. The mean MAE of the training set reached $43.12 \pm 5.49$ (1 standard deviation), $50.57 \pm 7.13$ for the validation set and 58.05 on the test cell. The figure shows some signs of over-fitting as the training set MAE outperforms the testing and validations sets. Globally, the error remains stable over time, even though the i.i.d. assumption of the data was not respected.

## 4. DISCUSSION AND CONCLUSION

We presented a novel method: using Deep Learning to predict cellular traction forces, even if the information directly related to the forces is not available. Indeed, despite the neural network not having access to the beads or fluorescent channels linked to proteins correlated with the force, it successfully made use of the cell geometry to accurately infer cell forces.

Adding channels representing fluorescent proteins related to cellular traction forces – i.e. actin or integrin – could bring dramatic improvements to the accuracy of the Deep Learning model. More, relying on the intensity of a fluorescent protein could increase the generalisation and stability when varying the softness of the gel, or using a glass medium. In addition, our method has so far been applied to one cell line and generalisation to other cell lines will require further testing and development.

## 5. REFERENCES

[1] Micah Dembo and Yu-Li Wang, "Stresses at the cell-to-substrate interface during locomotion of fibroblasts,"

Biophysical journal, vol. 76, no. 4, pp. 2307-2316, 1999.

[2] Thorsten M Koch, Stefan Münster, Navid Bonakdar, James P Butler, and Ben Fabry, "3d traction forces in cancer cell invasion," PloS one, vol. 7, no. 3, pp. e33476, 2012.

[3] Christopher A Lemmon and Lewis H Romer, "A pre- dictive model of cell traction forces based on cell geom- etry," Biophysical journal, vol. 99, no. 9, pp. L78-L80, 2010.

[4] Olaf Ronneberger, Philipp Fischer, and Thomas Brox, "U-net: Convolutional networks for biomedical image segmentation," in International Conference on Med- ical image computing and computer-assisted interven- tion. Springer, 2015, pp. 234-241.

[5] Simon Jégou, Michal Drozdzal, David Vazquez, Adri- ana Romero, and Yoshua Bengio, "The one hundred lay- ers tiramisu: Fully convolutional densenets for seman- tic segmentation," in Proceedings of the IEEE Confer- ence on Computer Vision and Pattern Recognition Work- shops, 2017, pp. 11-19.

[6] Gao Huang, Zhuang Liu, Laurens Van Der Maaten, and Kilian Q Weinberger, "Densely connected convolu- tional networks," in Proceedings of the IEEE confer- ence on computer vision and pattern recognition, 2017, pp. 4700-4708.

[7] Fritz R. D., Letzelter M., Reimann A., Martin K., Fusco L., Ritsma L., Ponsioen B., Fluri E., Schulte-Merker S., van Rheenen J., and Pertz O., "A versatile toolkit to produce sensitive fret biosensors to visualize signaling in time and space," Science signaling, vol. 6, no. 285, pp. rs12, 2013.

[8] Han S. J., Oak Y., Groisman A., and Danuser G., "Trac- tion microscopy to identify force modulation in subres- olution adhesions," Nature methods, vol. 12, no. 7, pp. 653-656, 2015.

[9] Jianjiang Hu, "Traction force microscopy dataset," Oct 2019, doi: 10.5281/zenodo.3484797.

[10] Manuel Gil, Fady Alajaji, and Tamas Linder, "Rényi di- vergence measures for commonly used univariate con- tinuous distributions," Information Sciences, vol. 249, pp. 124-131, 2013.

[11] Fredric J Harris, "On the use of windows for harmonic analysis with the discrete fourier transform," Proceed- ings of the IEEE, vol. 66, no. 1, pp. 51-83, 1978.

[12] Alex Kendall and Yarin Gal, "What uncertainties do we need in bayesian deep learning for computer vision?," in Advances in neural information processing systems, 2017, pp. 5574-5584.

[13] T Kvalseth, "Some informational properties of the log- normal distribution (corresp.)," IEEE Transactions on Information Theory, vol. 28, no. 6, pp. 963-966, 1982.

[14] Tanya Nair, Doina Precup, Douglas L Arnold, and Tal Arbel, "Exploring uncertainty measures in deep net- works for multiple sclerosis lesion detection and seg- mentation," Medical Image Analysis, p. 101557, 2019.