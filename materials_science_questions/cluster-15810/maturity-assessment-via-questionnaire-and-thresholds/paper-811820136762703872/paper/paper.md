2009 Fifth International Joint Conference on INC, IMS and IDC

# Risk Management in the Trustworthy Software Process: A Novel Risk and Trustworthiness Measurement Model Framework

Minglu Li$^{1,2}$
$^{1}$ Institute of Policy and Management, Chinese Academy of Sciences
$^{2}$ Graduate University of Chinese Academy of Sciences
Beijing 100190, China
mingluli@casipm.ac.cn

Jianping Li*
Institute of Policy and Management, Chinese Academy of Sciences
Beijing 100190, China
ljp@casipm.ac.cn

Hao Song$^{1,2}$
$^{1}$ Institute of Policy and Management, Chinese Academy of Sciences
$^{2}$ Graduate University of Chinese Academy of Sciences
Beijing 100190, China
haosong @casipm.ac.cn

Dengsheng Wu$^{1,2}$
$^{1}$ Institute of Policy and Management, Chinese Academy of Sciences
$^{2}$ Graduate University of Chinese Academy of Sciences
Beijing 100190, China
wds @casipm.ac.cn

Abstract—The growing demands for the trustworthiness of software pose an unprecedented challenge to software industry. An integrated trustworthy software process model is proposed to help improve software process risk management towards trustworthy software, which contains risk management, development process management and deliverables monitoring. Furthermore, based on this process model, a model framework including process risk metrics and trustworthiness metrics is presented. Great efforts have been put to the software trustworthiness measurement model. Simulation cases are then analyzed by this model framework, and some results about process risk and trustworthiness are discussed.

Keywords- Trustworthy Software Process, Software Risk Management, Process Risk Metrics, Trustworthiness Metrics

## I. INTRODUCTION

Over the past decade, trustworthy software has become a hot issue. It is more important than ever to manage the software process risk effectively for trustworthy software products. The significance and necessity of trustworthy software research is affirmed by governments, enterprises and academia [1,2]. In order to achieve the trustworthy software, scholars have carried out researches in two fields: the definition of trustworthy software, and how to produce trustworthy software. Larry Bernstein [3], Hasselbring Wilhelm [4] and John McLean [5] proposed their understanding about trustworthy from the software industry perspective. And they have also shown some opinions about trustworthy software Research Methods.

International Standard Organization introduced the ISO 15504 based on ISO 12207 and CMMI by SEI in 2004 to determine process capability and to improve software process for higher product quality, which provides overall information on the concepts of process assessment [6,7]. For identifying and ranking software process risks, H. Schmidt proposed a risk checklist through analyzing the data by surveying the software engineers in four states and regions [8].

In other industrial, there are some measurement model for product quality and security according to the various index setting [9,10]. Similarly, some process models for security or trustworthy software has been brought forward as well. In the thesis of Aketa Parikh, the software process system were designed and implemented with inbuilt security features [11]. Seok Won Lee established trustworthiness framework in services of the critical infrastructure to aggregate and analyze certification and accreditation related to information at various levels of abstractions [12]. Saleh K. et al. proposed the trustworthy software security requirements behavior model to help obtain secure and trustworthy web services and applications [13]. Zheng Yan et al. present an adaptive trust control model in order to support autonomic trust management for the component software platform using a fuzzy cognitive map [14]. At present, risk management in the software process is mainly risk identification and risk controlling. Though risk management and cost efficiency analysis are very important to support the process management decision making, less involved in the existing software process model risk management. And there is also a large gap between demand and recent research about Trustworthy software oriented risk measurement model.

* Corresponding author.

978-0-7695-3769-6/09 $26.00 © 2009 IEEE
DOI 10.1109/NCM.2009.283
214
![](./images/811820136762703872_1.jpg)

In this paper, based on defining risk management efficiency and process, a model framework including process risk metrics and trustworthiness metrics is presented. It integrates the software development process, process risk management and deliverables trustworthiness analysis together to calculate the value of software product trustworthiness. With development process risk simulation, risk management efficiency and trustworthiness value are calculated by the two measurement models. At the end of the paper, some results and future works are discussed about software process management and software trustworthiness metrics.

## II. TRUSTWORTHY SOFTWARE

Trustworthiness of software means its worthy of being trusted to fulfill requirements which may be needed for a particular software component, application, system, or network. It involves attributes of stability, data security, quality, privacy, safety and so on. With the weighted attributes setting, the trustworthiness value can be calculated further accurately. In addition, different users have different preferences in software trustworthiness demand. And the weights of all attributes can be adjusted to the different users. For example, the financial sector users would give bigger weights to data security and the anti-invasion attributes, while the military customers would focus on the stability and quality of software service.

For high trustworthiness level, the software process should apply a strict quality control and efficient risk management. Software processes are methods and standards for improving and mastering development processes, supporting processes and management processes throughout the software lifecycle.

Software trustworthiness is interrelated with not only risk control in the software process, but also the quality management of the software development process. Furthermore, vision is needed to avoid excessive costs and schedule delays in development and risks management costs in operation; to improve development efforts; and above all.

## III. TRUSTWORTHY SOFTWARE ORIENTED SOFTWARE PROCESS MODEL

Here, a trustworthy software oriented software process model is put forward. Given the capability maturity level of software companies, this is a process model with the goal of maximizing the trustworthiness level of software product. Being different from other models to concern more about the demand of software producers, the ultimate goal of this model is the users' needs and satisfaction.

The integrated trustworthy software process model is constructed by three parts: software process risk management, software development lifecycle process management and deliverables trustworthiness monitoring (See Figure. 1).

![](./images/811820136762703872_2.jpg)

Figure 1. The integrated three-part trustworthy software process management framework (risk management revision based on the software process standard in ISO 12207)

The first part, development process, is defined according to software process definition in the ISO 12207. It includes the five processes: acquisition, supply, development, operation, and maintenance. It is the center of the integrated model. The second part, risk management process, is designed to identify and control risks with checklists and case library in each step of the software process throughout the software lifecycle. In addition, deliverables of ever process are considered as the third part, which affected the software product trustworthiness directly. Consequently, software development, risk management and product trustworthiness are linked as a whole framework.

In software process management, risk management is an important part to guarantee the high trustworthiness level. Risk management for trustworthy software is a structured approach to managing risk factors related to a threat to the trustworthiness of the software product. Simply, it includes risk identification, risk assessment, and risk control [15]. Checklist approach is a quick and low cost way to identifying risk and assessing the risk exposure of the software process. Risk control strategies aim to either reduce or eliminate the likelihood of the threat to the software occurring and limit the impact of the risk if it can be identified. Commonly, risk can be formulated like this: $R = P \times I$ , where $R$ is the project risk exposure, $P$ is the probability of the risk factor occurrence, and $I$ is the impact of the risk factor. The risk in software projects is usually defined as probability-weighted impact of an event on a software project. In this paper, "risk" refers to those risk events which would lead to the decline in trustworthiness of software product.

In general, a company which has the higher management has a higher ability of risk identification and risk control. So, the effectiveness of risk identification and risk control can be considered to have the positive correlation with the CMMI level. Naturally, the level of risk management will also improve with the input of cost and schedule increasing. Because the effectiveness is bounded by the given

environment, the ratio of cost to risk management effectiveness is decreasing with cost increasing. According to input-output function in economics, we assume that the effectiveness of risk identification and risk control has exponential correlation with the budget and the planning time of project risk management. We can construct the effectiveness functions of risk identification ($RI$) and risk control ($RC$):

$$
RI=\frac{2}{1+e^{-CMM\cdot T^{\alpha}C^{\beta}}}-1 \tag{1}
$$

$$
RC=\frac{2}{1+e^{-CMM\cdot T^{\zeta}C^{\xi}}}-1 \tag{2}
$$

where $\alpha$ , $\beta$ are the $RI$ elasticity of time and cost respectively, and $\xi$ ,$\zeta$ are the $RC$ elasticity of time and cost respectively. These values are constants determined by available technology and management level.

## IV. MEASUREMENT MODEL OF PROCESS RISK AND SOFTWARE TRUSTWORTHINESS

In this section, two measurement models are shown, and some scenario analysis cases are used to find the rules of the different factors which affect the trustworthiness in different constraints and CMMI environments.

### A. Measurement model of software process risk

The software process measurement model, simple but without loss of generality, is based on five large-scale processes: Acquisition, Supply, Development, Maintenance, and Operation. For the sake of simplicity, six primacy categories of risks are used in the model: Requirements Risk, Project Management Risk, User Risk, Development Risk, Developer Risk, and Environment Risk [17,18]. In practice, the settings of processes and the risk categories can be further refined or extended for different measurement demand, and the parameters should be adjusted as well.

In the software process, the same risk will occur in the different processes. And risk in the checklist during a process can be denoted as $R_{ij}$ , where $i$ is the sequence number of the category which the risk affiliate with, and $j$ is the number of the process which the $R_{i}$ occur. The risk $R_{ij}$ is considered an event subjected to an independent and same binomial distribution with the parameter$P_{ij}$. And the probability of risk occurrence is negatively correlated to the company's software project management and risk management levels. So, $P_{ij}$ can be expressed by the function of the company's CMMI level in the same development cost constraint condition.

$$
P_{ij}=\frac{S_{ij}}{CMM} \tag{3}
$$

where $S_{ij}$ is the coefficient on the basis of software project management experience. So the measurement of risk can be calculated as $R_{ij}=P_{ij}I_{i}=\frac{S_{ij}}{CMM}\cdot I_{i}$ , $I_{i}$ can be expressed by the ranking in the risk checklist. For example, $I$ of the 1st risk category can be given five, and $I$ of the 5th risk category can be given 1. Indeed, this is a subjective weight for the evaluation, but it can reflect the risk consequence directly and simply.

For each conversion between two processes, the transition matrix can be constructed on the basis of experts' experience or survey data. Given enough software process historical data, data analysis would gain the more accurate parameters in the risk transition matrix. Because the software process is an activity series, the risk transferring part in the later process risk is only brought from the last process. Between every two processes, the risk transition matrix between processes $j$ and $j+1$ can be denoted as$TR_{j+1}$. After valuation of each transition factor between these two processes, we can obtain the matrix as follows,

$$
\mathrm{TR}_{j+1}=\left[\begin{array}{c}
t r_{1,1}^{(j+1)} \cdots t r_{1,6}^{(j+1)} \\
\cdots \cdots \cdots \cdots \\
t r_{6,1}^{(j+1)} \cdots t r_{6,6}^{(j+1)}
\end{array}\right] \tag{4}
$$

where, $tr_{m,n}^{(j+1)}$ denotes the coefficient which is how much risk $m$ in processes $j$ has been accumulated to the next process $j+1$. For example, the first category of risk value in the process 2 is the value of risk occurs in the process 2 plus $\sum_{m=1}^{6} t r_{m,1}^{(2)} R_{m,1}$ .

Therefore, we can gain the total risk in the software process:

$$
\begin{aligned}
& R_{\text {total }}=\bar{R}_{1} \cdot R I_{1} \cdot R C_{1}+\sum_{j=1}^{4}\left(\left(\bar{R}_{j} T R_{j+1}+\bar{R}_{j+1}\right) \cdot R I_{j} \cdot R C_{j}\right) \\
& =\left(\begin{array}{c}
R_{11} \\
\vdots \\
R_{61}
\end{array}\right)_{1 \times 6}^{T} \cdot R I_{1} \cdot R C_{1}+\sum_{j=1}^{4}\left(\left(\left(\begin{array}{c}
R_{1 j} \\
\vdots \\
R_{6 j}
\end{array}\right)_{1 \times 6}^{T} \cdot\left(\begin{array}{c}
t r_{1,1}^{(j+1)} \cdots t r_{1,6}^{(j+1)} \\
\cdots \cdots \cdots \cdots \\
t r_{6,1}^{(j+1)} \cdots t r_{6,6}^{(j+1)}
\end{array}\right)_{6 \times 6}+\left(\begin{array}{c}
R_{1, j+1} \\
\vdots \\
R_{6, j+1}
\end{array}\right)_{1 \times 6}^{T}\right) \cdot R I_{j} \cdot R C_{j}\right)
\end{aligned} \tag{5}
$$

For each $R_{ij}$ , $R_{ij}=P_{ij} \cdot I_{i}$ , where $P_{ij}$ is a binary which denotes the risk occurs ($P_{ij}=1$) or not ($P_{ij}=0$), and it only related to the CMMI level of the corporation.

### B. Measurement model of software trustworthiness

During the software process, different deliverables and services offered by the processes affect the trustworthiness attributes of software product differently. The risks in the same process impact the trustworthiness similarly because every risk factor affects the same deliverables. And the deliverables offered by this process is directly related to the final product. Therefore the framework of the software process risks, deliverables and trustworthiness is built (See Figure. 2).

![](./images/811820136762703872_3.jpg)

Figure. 2. The framework of process, risk, deliverables and trustworthiness

For calculating the trustworthiness affected by risk, the impact factors matrix between five process deliverables and five trustworthiness dimensions is constructed as:

$$
I M=\left(\begin{array}{ccc}
I M_{1,1} & \cdots & I M_{1,5} \\
\cdots & \cdots & \cdots \\
I M_{5,1} & \cdots & I M_{5,5}
\end{array}\right)_{5 \times 5}=\left(\begin{array}{c}
I M_{1} \\
\vdots \\
I M_{5}
\end{array}\right)
\tag{6}
$$

Then, the trustworthiness affected by the process risk can be calculated:

$$
\begin{gathered}
T_{R i s k}=W_{1 \times 5}\left(T_{1} \quad \cdots \quad T_{5}\right)_{5 \times 1}^{T} \\
=\left(\begin{array}{c}
\omega_{1} \\
\vdots \\
\omega_{5}
\end{array}\right)_{1 \times 5} \cdot\left(\begin{array}{c}
R_{\text {total }, 1} \cdot I M_{1} \\
\vdots \\
R_{\text {total }, 5} \cdot I M_{5}
\end{array}\right)_{5 \times 5}\left(\begin{array}{l}
1 \\
\vdots \\
1
\end{array}\right)_{5 \times 1}=\left(\begin{array}{c}
\omega_{1} \\
\vdots \\
\omega_{5}
\end{array}\right)_{1 \times 5} \cdot\left(\begin{array}{c}
\sum_{i=1}^{6} R_{i 1} \cdot I M_{1} \\
\vdots \\
\sum_{i=1}^{6} R_{i 5} \cdot I M_{5}
\end{array}\right)_{5 \times 5}\left(\begin{array}{l}
1 \\
\vdots \\
1
\end{array}\right)_{5 \times 1}
\end{gathered}
\tag{7}
$$

For the similar reasons as $RI$ and $RC$ , $T_{Quality}$ affected by the development process quality can be calculated as:

$$
T_{\text {Quality }}=\frac{2}{1+e^{-C M M \cdot S c h_{p}{ }^{a} \cdot \operatorname{Cost}_{p}{ }^{b}}}-1
\tag{8}
$$

where $a$ and $b$ are the $T_{Quality}$ elasticity of time and cost respectively. These values are constants determined by available technology and management level.

So, the trustworthiness of the software can be defined as the difference between trustworthiness affected by quality and risk:

$$
T=T_{\text {Quality }}-T_{\text {Risk }}
\tag{9}
$$

The measure is a relative value but not an absolute value for the specific software. The measure would change significantly due to different parameters chosen. However, this model can be used to evaluate the discrepancy in different risk management environments to improve the risk management and enhance the software development efficiency.

## V. CASE STUDY

In order to verify the proposed models, a case study is conducted. Following the proposed framework, we measured and analyzed in a simulated scenario. The simulation program designed on EXCEL by VBA simulates a software process management in the different CMMI level and other risk management constraints. Some results of the relationship between CMMI level and trustworthiness, and the efficiency of the risk management cost and schedule have been attained.

To simulate the software process in Chinese enterprises accurately, we design the questionnaire about risk management in software process. Nearly 200 copies of the questionnaire have been delivered to the project managers in software companies, and some questionnaires results have been obtained. Before we get the final investigation data, the risk transferring matrix, risk impact matrix and other parameters in the simulation environment are obtain by the AHP among six senior software development project managers. The first risk transferring matrix is:

$$
T R_{2}=\left(\begin{array}{cccccc}
1 & 0.2 & 0.6 & 0.5 & 1 & 0.3 \\
0 & 0.8 & 0.3 & 0.5 & 0 & 0.3 \\
0 & 0 & 0.3 & 0.2 & 0.6 & 0 \\
0.6 & 0 & 0 & 0.2 & 0 & 0.2 \\
0 & 0 & 0 & 0 & 0.4 & 0.2 \\
0.3 & 0.6 & 0.1 & 0.2 & 0.1 & 0.5
\end{array}\right)
\tag{10}
$$

And the other three risk transferring matrixes are omitted here, which are similar with the first one. In addition, based on expert opinion, the risk impact matrix is defined as Table I.

<table>
<caption>TABLE I. RISK IMPACT MATRIX</caption>
<thead>
<tr>
<th></th>
<th>P1</th>
<th>P2</th>
<th>P3</th>
<th>P4</th>
<th>P5</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stability</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
</tr>
<tr>
<td>Data Security</td>
<td>0.4</td>
<td>0.2</td>
<td>0.1</td>
<td>0.1</td>
<td>0.2</td>
</tr>
<tr>
<td>Quality</td>
<td>0.2</td>
<td>0.2</td>
<td>0.5</td>
<td>0.1</td>
<td>0</td>
</tr>
<tr>
<td>Privacy</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.1</td>
<td>0.3</td>
</tr>
<tr>
<td>Safety</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
<td>0.2</td>
</tr>
</tbody>
</table>

In the five different CMMI level cases, we simulated eight software processes for every situation (See Figure. 3). Below CMMI 3 level, the trustworthiness values of eight software products have the bigger volatility and the lower trustworthiness. In certain software process environment, CMMI 4 and CMMI 5 have a similar outstanding performance.

![](./images/811820136762703872_4.jpg)

Figure 3. CMMI level and trustworthiness for the same software process environment

The second case is simulated in common corporations' environments which are CMMI 3 level, most of the trustworthy software products suppliers in China. The risk occurrence in processes is simulated (See Table II).


<table>
<caption>TABLE II. RISK OCCURRENCE RESULTS</caption>
<thead>
<tr>
<th></th>
<th>R1</th>
<th>R2</th>
<th>R3</th>
<th>R4</th>
<th>R5</th>
<th>R6</th>
</tr>
</thead>
<tbody>
<tr>
<td>Process 1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Process 2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Process 3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Process 4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>Process 5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

1 in the cell denotes that the column risk occurs in row process, and 0 denotes no occurrence

With increasing of the risk management (risk identification or risk control) input, bigger schedule input is very significant to improve the trustworthiness in the process which risk occurs, but in the process of no risk occurrence, the bigger input resulted in a greater waste. Moreover, the efficiency of enhancing the trustworthiness by increasing input declines when the inputs arrive to a certain value (See Figure. 4). Like risk management schedule input, the increased cost about finance and human resources has also a relative capacity limit for improving the trustworthiness.

From the above results, some conclusions can be drawn as following:
(1) CMMI level is a key factor affecting the trustworthiness in most process models, so improving the software process management is the most important method to enhance the software product trustworthiness.
(2) In certain CMMI environment, risk management is critical to enhance the trustworthiness. But considering the constraints of schedule and cost, there is a limit of the efficiency of risk management input. So, risk management is an effective complement, rather than the most fundamental decision factor of the trustworthiness.

![](./images/811820136762703872_5.jpg)

Figure. 4. Risk management input and trustworthiness in CMMI 3 environment

Though trustworthiness value is affected by a lot of parameters of the software process, and different settings would lead to different trustworthiness value, the model can be applied to simulate trustworthiness value change with different risk management variables in certain corporation environment or in other conditions. So, it can be used for decision-making support in the software process management practice.

## VI. CONCLUSION

In this paper, an integrated trustworthy software process model is constructed by three parts: software process risk management, software development lifecycle process management and deliverables trustworthiness monitoring. Being concluded in this framework, two metrics models are presented to calculate risk management efficiency and trustworthiness value. At the end of the paper, simulation cases are analyzed to display the models. And the results demonstrate that these models are usefulness in the software process management practice. Improving the software process management is considered as the most important method to enhance the software product trustworthiness. And in certain environment, risk management is critical to enhance the trustworthiness. But risk management is an effective complement, rather than the most fundamental decision factor of the trustworthiness as software development process.

Furthermore, we have several future directions to pursue. Firstly, we plan to get more feedback from software process practitioners to further improve the framework settings. Secondly, an extend metrics including more risk categories and sub-processes is necessary to apply the model in software process management practice. Thirdly, the research about optimal decision of risk management input for maximum trustworthiness is the future work direction as well.

## ACKNOWLEDGMENT

This research is supported the Major Research Plan of National Science Foundation of China (#90718042).

## REFERENCES

[1] The 2nd National Software Summit, "The National Software Strategy Steering Group, Software 2015: A National Software Strategy to Ensure U.S. Security and Competitiveness", Technical report, 2005
[2] Barry Boehm, Software risk management: Principles and practices. IEEE Software, Vol. 8, 1991, pp.32-41
[3] Larry Bernstein, "Trustworthy software systems", ACM SIGSOFT Software Engineering Notes, Vol. 30, Issue 1, ACM Press, New York, 2005, pp. 4-5
[4] Hasselbring Wilhelm, Reussner Ralf, Toward Trustworthy Software Systems. IEEE Computer, Vol. 39. Issue 4, 2006, pp. 91-92
[5] John McLean, "Trustworthy Software: Why we need it, Why we don't have it, How we can get it", 30th Annual International Computer Software and Applications Conference, IEEE Press, New York, 2006, pp. 32-33
[6] ISO/IEC 12207, Systems and Software Engineering: Software Life Cycle Processes, ISO, 2008

[7] ISO/IEC 15504, Process Assessment, ISO, 2008

[8] H. Schmidt, "Trustworthy components-compositionality and prediction", The Journal of Systems and Software, Vol. 65, Elsevier, Amsterdam, 2003, pp. 215-225

[9] Sajjad Mahmood, Richard Lai, Yong Soo Kim, Ji Hong Kim, A survey of component based system quality assurance and assessment, Information and Software Technology, Vol. 47, 2005, pp. 693-707

[10] Miroslaw Staron, Wilhelm Meding, Christer Nilsson, A framework for developing measurement systems and its industrial evaluation, Information and Software Technology, Vol. 51, 2009, pp. 721-737

[11] Aketa Parikh, "Trustworthy Software", a thesis for M.S., Stevens Institute of Technology, Hoboken, New York, 2004

[12] Seok Won Lee, Robin A. Gandhi and Gail-Joon Ahn, "Establishing trustworthiness in services of the critical infrastructure through certification and accreditation", ACM SIGSOFT Software Engineering Notes, Vol. 30, Issue 4, ACM Press, New York, 2005, pp. 1-7

[13] Saleh K., Habil M., "The Security Requirements Behavior Model for Trustworthy Software", 2008 International MCETECH Conference on e-Technologies, IEEE Press, New York, 2008, pp. 235-238

[14] Zheng Yan, Christian Prehofer, "An Adaptive Trust Control Model for a Trustworthy Component Software Platform", Autonomic and Trusted Computing, LNCS Vol. 4610, 2007, Springer, Heidelberg, pp. 226-238

[15] Alexander Carol, Sheedy Elizabeth, The Professional Risk Managers' Handbook: A Comprehensive Guide to Current Theory and Best Practices, PRMIA Publications, Wilmington, 2005

[16] Paul L. Bannerman, Risk and risk management in software projects: A reassessment, The Journal of Systems and Software, 2008, doi:10.1016/j.jss.2008.03.059

[17] Wen-Ming Han, Sun-Jen Huang, An empirical analysis of risk components and performance on software projects, The Journal of Systems and Software, Vol. 80, 2007, pp.42-50

[18] Linda Wallace, Mark Keil, Software Project Risks And Their Effect On Outcomes, Communications of the Acm, Vol. 47, 2004, pp. 68-73