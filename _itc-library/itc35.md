
---
title: ITC35
year: 2023
---

Keisuke Ishibashi, Takumi Uchida<br/>
**Estimating Traffic Latent Due to QoS Deterioration: A Time-Series Causal Inference Approach**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper1'))
[\[Abstract\]](javascript:toggleVis('abstract_1'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final1.pdf)
[\[BibSonomy\]]()

<div id="itcpaper1" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Estimating Traffic Latent Due to QoS Deterioration: A Time-Series Causal Inference Approach },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Keisuke Ishibashi, Takumi Uchida },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 6 }
    }
</div>
<div id="abstract_1" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We propose a method for estimating the impact of QoS (Quality of Service) degradation on users/applications through the resulting reduction in traffic. QoS degradation often leads to a degradation in QoE (Quality of Experience), which may prompt users to abandon applications or cause applications to reduce content size to prevent abandonment. In both cases, traffic is reduced. By observing such traffic reduction, we can estimate the impact of QoS degradation on users/applications as QoE degradation, which is useful for network/service operation but difficult to measure. Additionally, this estimation allows for accurate traffic engineering and network design by estimating the original traffic demand before reduction.

To estimate the impact, we use a causal inference approach, where the impact can be viewed as a causality from QoS degradation to traffic reduction. Existing causal inference techniques assume a one-way relationship between cause-and-effect variables, but in our case, QoS degradation is mostly caused by traffic increase, thus creating a two-way relationship. Here, we can expect that these two causalities have different timescales, thus if we observe them as a multi-variate time series with appropriate temporal granularity, then we can separate them as "two" one-way relationships to estimate the causality. However, the estimation of the time series is still prone to both bias and variance problems, which we address through our proposed multi-source iterative causal inference method. We evaluate the applicability of our method through simulations, specifically by utilizing appropriate temporal granularity. Additionally, we confirm that our method can estimate the original traffic demand.
</div>

Stefan Geißler, David Raunecker, Stanislav Lange, Tobias Hossfeld<br/>
**DARTA: Generation of Autocorrelated Random Numbers using Discrete AutoRegression To Anything**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper2'))
[\[Abstract\]](javascript:toggleVis('abstract_2'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final3.pdf)
[\[BibSonomy\]]()

<div id="itcpaper2" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { DARTA: Generation of Autocorrelated Random Numbers using Discrete AutoRegression To Anything },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Stefan Geißler, David Raunecker, Stanislav Lange, Tobias Hossfeld },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_2" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Machine-to-machine communications often exhibit autocorrelated arrival processes of IP packets, which necessitates considering this autocorrelation in the analysis of modern communication systems like 5G and future 6G deployments. Discrete-event simulations are suitable for analyzing these complex systems. The AutoRegression To Anything (ARTA) model is commonly used to generate autocorrelated processes with arbitrary autocorrelation structures. Our work introduces the Discrete AutoRegression To Anything (DARTA) model, which extends ARTA and improves performance and numerical computation by using discrete random processes with appropriate time discretization. We evaluate DARTA's performance through a comprehensive parameter study, focusing on its distribution matching capability, configured autocorrelation, and runtime. Our results demonstrate the effectiveness and practicality of DARTA, showing its ability to generate discrete autocorrelated stochastic processes more efficiently than existing deterministic ARTA approaches. We provide a ready-to-use implementation of our proof-of-concept implementation.
</div>

Ankita Koley, Chandramani Singh<br/>
**Optimal Resource Management for Multi-access Edge Computing without using Cross-layer Communication**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper3'))
[\[Abstract\]](javascript:toggleVis('abstract_3'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final13.pdf)
[\[BibSonomy\]]()

<div id="itcpaper3" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Optimal Resource Management for Multi-access Edge Computing without using Cross-layer Communication },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Ankita Koley, Chandramani Singh },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_3" style="display: none;" class="abstract">
    <strong>Abstract:</strong> We consider a Multi-access Edge Computing (MEC) system with a cloud server, a base station (BS) and an MEC server attached to it. The resource constrained MEC server can
be dynamically configured to serve different classes of services. The users send all the service requests to the BS which in turn keeps a subset of the requests to be served at the MEC and forwards others to the cloud server. The service requests that are processed at the MEC server incur queuing and processing delays whereas those that are sent to the cloud only incur fixed processing delays. Throughput and delay optimality warrant uplink packet scheduling at the users, MEC server configuration and service scheduling at the BS, and service forwarding to the cloud accounting for the system state. Traditional solutions to
this resource management problem, e.g., those based on back-pressure, entail cross-layer message exchange. We develop two virtual queue-based drift-plus-penalty algorithms that do not require cross-layer communication, are throughput optimal, and
achieve the optimal delay arbitrarily closely. The algorithms offer a tradeoff between the queuing and processing delays at the MEC server and the service processing delay at the cloud. We illustrate the performance of the algorithms via simulations.
</div>

Jianhang Zhu, Jie Gong<br/>
**Optimizing Peak Age of Information in Mobile Edge Computing**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper4'))
[\[Abstract\]](javascript:toggleVis('abstract_4'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final29.pdf)
[\[BibSonomy\]]()

<div id="itcpaper4" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Optimizing Peak Age of Information in Mobile Edge Computing },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Jianhang Zhu, Jie Gong },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_4" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Recently, information freshness in real-time monitoring systems has received increasing attention. Age of Information (AoI) has emerged as a metric for measuring the information
freshness. In many applications, the information embedded in an
update packet needs to be computed before delivering to a destination. Mobile edge computing (MEC) can efficiently accomplish
the computing process. In the MEC system, transmission process
and computation process are coupled together, jointly affecting
freshness. In this paper, we consider minimizing the average peak
AoI (PAoI) in an MEC system, where each update is received and
computed by an edge server before delivering to the destination.
We consider the generate-at-will source model and study when to
generate a new update. We prove that the fixed threshold policy
is optimal for arbitrary transmission time and computation time
distributions. Our numerical simulation results not only validate
the theoretical findings, but also demonstrate the behaviors of the
average PAoI versus the mean transmission time and the mean
computation time.
</div>

Vinay Kumar Bindiganavile Ramadas<br/>
**Spatial Queues with Nearest Neighbour Shifts**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper5'))
[\[Abstract\]](javascript:toggleVis('abstract_5'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final32.pdf)
[\[BibSonomy\]]()

<div id="itcpaper5" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Spatial Queues with Nearest Neighbour Shifts },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Vinay Kumar Bindiganavile Ramadas },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 5 }
    }
</div>
<div id="abstract_5" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Motivated primarily by electric vehicles (EV) queueing at charging stations, in this work we study multiple server queues on a Euclidean space. We consider $N$ servers that are distributed uniformly in $[0,1]^d$. Customers or EV users arrive at the servers according to Poisson processes of intensity $\lambda$. However, they probabilistically decide whether to join the queue they arrived at, or move to one of the nearest neighbours. The strategy followed by the customers affects the load on the servers in the long run. In this paper, we are interested in characterizing the fraction of servers that bear a larger load as compared to when the users do not follow any strategy, i.e., they join the queue they arrive at. These are called \emph{overloaded servers}. We evaluate the expected fraction of overloaded servers in the system for the one dimensional case ($d=1$) when the users follow probabilistic nearest neighbour shift strategies.
</div>

Ludovic Thomas, Jean-Yves Le Boudec<br/>
**Network-Calculus Service Curves of the Interleaved Regulator**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper6'))
[\[Abstract\]](javascript:toggleVis('abstract_6'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final35.pdf)
[\[BibSonomy\]]()

<div id="itcpaper6" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Network-Calculus Service Curves of the Interleaved Regulator },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Ludovic Thomas, Jean-Yves Le Boudec },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_6" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The interleaved regulator (implemented by IEEE TSN Asynchronous Traffic Shaping) is used in time-sensitive networks for reshaping the flows with per-flow contracts. When applied to an aggregate of flows that come from a FIFO system, an interleaved regulator that reshapes the flows with their initial contracts does not increase the worst-case delay of the aggregate. This shaping-for-free property supports the computation of end-to-end latency bounds and the validation of the network’s timing requirements. A common method to establish the properties of a network element is to obtain a network-calculus service-curve model. The existence of such a model for the interleaved regulator remains an open question. If a service-curve model were found for the interleaved regulator, then the analysis of this mechanism would no longer be limited to the situations where the shaping-for-free holds, which would widen its use in time-sensitive networks. In this paper, we investigate if network-calculus service curves can capture the behavior of the interleaved regulator. We find that an interleaved regulator placed outside of the shaping-for-free requirements (after a non-FIFO system) can yield unbounded latencies. Consequently, we prove that no network-calculus service curve exists to explain the interleaved regulator’s behavior. It is still possible to find non-trivial service curves for the interleaved regulator. However, their long-term rate cannot be large enough to provide any guarantee (specifically, we prove that for the regulators that process at least four flows with the same contract, the long-term rate of any service curve is upper bounded by three times the rate of the per-flow contract).
</div>

Tan Chen, Jintao Yan, Yuxuan Sun, Sheng Zhou, Deniz Gunduz, Zhisheng Niu<br/>
**Data-Heterogeneous Hierarchical Federated Learning with Mobility**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper7'))
[\[Abstract\]](javascript:toggleVis('abstract_7'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final38.pdf)
[\[BibSonomy\]]()

<div id="itcpaper7" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Data-Heterogeneous Hierarchical Federated Learning with Mobility },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Tan Chen, Jintao Yan, Yuxuan Sun, Sheng Zhou, Deniz Gunduz, Zhisheng Niu },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 5 }
    }
</div>
<div id="abstract_7" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Federated learning enables distributed training of machine learning (ML) models across multiple devices in a privacy-preserving manner. Hierarchical federated learning (HFL) is further proposed to meet the requirements of both latency and coverage. In this paper, we consider a data-heterogeneous HFL scenario with mobility, mainly targeting vehicular networks. We derive the convergence upper bound of HFL with respect to mobility and data heterogeneity, and analyze how mobility impacts the performance of HFL. While mobility is considered as a challenge from a communication point of view, our goal here is to exploit mobility to improve the learning performance by mitigating data heterogeneity. Simulation results verify the analysis and show that mobility can indeed improve the model accuracy by up to 15.1\% when training a convolutional neural network on the CIFAR-10 dataset using HFL.
</div>

Asmad Bin Abdul Razzaque, Andrea Baiocchi<br/>
**Grant-free transmissions based on successive interference cancellation in IoT**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper8'))
[\[Abstract\]](javascript:toggleVis('abstract_8'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final70.pdf)
[\[BibSonomy\]]()

<div id="itcpaper8" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Grant-free transmissions based on successive interference cancellation in IoT },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Asmad Bin Abdul Razzaque, Andrea Baiocchi },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_8" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Advancements in the physical layer design are pushing towards a major re-design of multiple access schemes for Next Generation Wireless Communication Systems. Hence, we turn towards random multiple access. We use a general model to investigate the interplay between random multiple access protocols and physical layer functions, specifically Successive Interference Cancellation (SIC). We focus on the sum-rate metric, which has been shown to exhibit two local maxim as a function of the target Signal to Interference plus Noise Ratio (SINR). The contribution of this paper lies with assessing the sensitivity of the optimal sum-rate to the number of concurrent transmissions, transmission power setting, and imperfect interference cancellation. Furthermore, leveraging the understanding gained on sum-rate optimization, we define a sum-rate optimal adaptive algorithm, when the number of contending nodes varies with time.
</div>

Florian Wiedner, Max Helm, Alexander Daichendt, Jonas Andre, Georg Carle<br/>
**Containing Low Tail-Latencies in Packet Processing Using Lightweight Virtualization**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper9'))
[\[Abstract\]](javascript:toggleVis('abstract_9'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final71.pdf)
[\[BibSonomy\]]()

<div id="itcpaper9" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Containing Low Tail-Latencies in Packet Processing Using Lightweight Virtualization },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Florian Wiedner, Max Helm, Alexander Daichendt, Jonas Andre, Georg Carle },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_9" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Packet processing in current network scenarios faces complex challenges due to the increasing prevalence of requirements such as low latency, high reliability, and resource sharing. Virtualization is a potential solution to mitigate these challenges by enabling resource sharing and on-demand provisioning; however, ensuring high reliability and ultra-low latency remains a key challenge. Since bare-metal systems are often impractical because of high cost and space usage, and virtual machines require substantial additional resources, we evaluate the utilization of containers as a potential lightweight solution for low-latency-enabled packet processing. Herein, we discuss the benefits and drawbacks and encourage the use of container environments in low-latency packet processing when the degree of isolation of customer data is adequate and bare metal systems are unaffordable. Our results demonstrate that containers achieve similar latency performance with more predictable tail-latency behavior compared to bare metal packet processing. Furthermore, we show that the overhead caused by virtualization is negligible in tail latencies.
</div>

Giampaolo Bovenzi, Davide Di Monda, Antonio Montieri, Valerio Persico, Antonio Pescape<br/>
**META MIMETIC: Few-Shot Classification of Mobile-App Encrypted Traffic via Multimodal Meta-Learning**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper10'))
[\[Abstract\]](javascript:toggleVis('abstract_10'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final76.pdf)
[\[BibSonomy\]]()

<div id="itcpaper10" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { META MIMETIC: Few-Shot Classification of Mobile-App Encrypted Traffic via Multimodal Meta-Learning },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Giampaolo Bovenzi, Davide Di Monda, Antonio Montieri, Valerio Persico, Antonio Pescape },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_10" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Despite its proven effectiveness in classifying encrypted network traffic, deep learning requires large amounts of labeled data to feed typical data-hungry training processes. Few-shot learning provides means to overcome these limitations, supporting classification tasks related to traffic with few labeled data available. Its extensive investigation in other domains notwithstanding (e.g., computer vision), it has been only preliminarily adopted for classifying encrypted traffic.

In this work, we design and evaluate META MIMETIC a novel multimodal few-shot learning solution for classifying mobile-app encrypted traffic. The proposal is based on the meta-learning paradigm and introduces enhancements via the adoption of a multimodal feature extractor trained via a novel ad-hoc meta-learning procedure. Since META MIMETIC is orthogonal to the specific few-shot learning approach, in our experimentation, we adapt it to a number of different meta-learning approaches (namely \textit{MatchingNet}, \textit{ProtoNet}, \textit{RelationNet}, \textit{MetaOptNet}, \textit{fo-MAML}, and \textit{ANIL}). We provide an empirical assessment of these approaches, considering the Mirage-2019 dataset as a test bench. Results show that META MIMETIC represents the best trade-off in terms of performance and complexity in mobile-app traffic classification (up to 91% F1-score) when compared to state-of-the-art solutions. The in-depth analysis of the performance of its components allows us to shed light on the multimodal internal mechanisms and further improve classification performance. Finally, we demonstrate the robustness of our proposal (only ≈ 2% F1-score drop) against the next variations introduced by the TLS 1.3 encryption that may impair the information exploitable by payload-based traffic classifiers.
</div>

Max Helm, Benedikt Jaeger, Christopher Pfefferle, Georg Carle<br/>
**Beyond Mean: Spatio-Temporal Modeling of Queue Utilizations and Flow Latencies Using T-GNNs**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper11'))
[\[Abstract\]](javascript:toggleVis('abstract_11'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final91.pdf)
[\[BibSonomy\]]()

<div id="itcpaper11" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Beyond Mean: Spatio-Temporal Modeling of Queue Utilizations and Flow Latencies Using T-GNNs },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Max Helm, Benedikt Jaeger, Christopher Pfefferle, Georg Carle },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_11" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Network planning and control require precise, reliable, and dynamic digital network models to easily obtain performance metrics. One central performance metric in any network is the end-to-end latency of connections which can be inferred from queue utilizations along its path. Models take a variety of forms: simulation, emulation, stochastic and deterministic formal methods, and machine-learning-based or -assisted approaches. Simulation and emulation require either too much computational time or too many hardware resources, while formal methods often have a high computational complexity leading to poor scalability. Machine-learning-based methods scale better to larger problem spaces, however, current approaches mainly concentrate on mean performance metric predictions. We show that such an approach can be extended to predict queue utilization and end-to-end latency behavior over time in dynamic networks. This is achieved by utilizing Temporal Graph Neural Networks (T-GNNs) which can model spatio-temporal dependencies. The approach achieves a mean queue utilization error of 5.5% and a flow-level end-to-end latency MARE of 5%-55% depending on time resolution over 100 random topologies. We show that this approach outperforms a non-temporal, static Graph Neural Network (GNN) on the same task in terms of capturing dynamic network behavior such as queue build-up and draining. The approach performs similar to related work while increasing flow rates by up to three orders of magnitude-this improvement is bought with a trade-off in supported scheduling mechanisms and traffic patterns. Our results show that such a T-GNN approach can be useful for performance modeling of high data rate flows in dynamic networks.
</div>

Ziad TLAISS, Alexandre FERRIEUX, Isabel AMIGO, Isabelle HAMCHAOUI, Sandrine VATON<br/>
**Automated Identification of BBR Traffic based on Packet Inter-Arrival Times Analysis**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper12'))
[\[Abstract\]](javascript:toggleVis('abstract_12'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final93.pdf)
[\[BibSonomy\]]()

<div id="itcpaper12" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { Automated Identification of BBR Traffic based on Packet Inter-Arrival Times Analysis },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Ziad TLAISS, Alexandre FERRIEUX, Isabel AMIGO, Isabelle HAMCHAOUI, Sandrine VATON },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 9 }
    }
</div>
<div id="abstract_12" style="display: none;" class="abstract">
    <strong>Abstract:</strong> The Internet is a complex and constantly evolving system, and congestion control algorithms play a crucial role in ensuring its functioning by managing network performance. These algorithms regulate the flow of data within a network and optimize data transmission for efficiency and effectiveness. They do this by continuously estimating available network resources and adjusting the data transmission rate accordingly.

For network operators, identifying the congestion control algorithms being used on their network is essential to gain valuable insights into network performance and device behavior. This information can help them gain a better understanding of how the network is being utilized and which algorithms are most effective in different scenarios. With a clear understanding of the congestion control algorithms in use, they can make decisions about network design, configuration, and management.

Nowadays, over 85\% of total Internet traffic is TCP traffic. TCP uses different congestion control algorithms, of which BBR and CUBIC represent 73\% of the total TCP traffic. In this work, we present a method for automatically identifying BBR traffic on the Internet. Our method relies on analyzing packet inter-arrival times, specifically comparing the distribution of packet inter-arrival times during the Slow-Start state of a BBR capture with those of a CUBIC capture. We introduce a model that allows us to detect the silence period after packet bursts that are present in almost all non-BBR congestion control algorithms. This method is characterized by a very simple frontend signal processing that exploits the algorithms' core principles, allowing for a tiny parameter space dimension (two), which is sufficient for robust discrimination: an error rate of 4.1\% was obtained on a test dataset independent from training.
</div>

Hadi Hosseini, Ahmed Almutairi, Syed Muhammad Hashir, Ehsan Aryafar, Joseph Camp<br/>
**An Outdoor Experimental Study of Many Antenna Full-Duplex Wireless**<br/>
In *35th International Teletraffic Congress (ITC-35) *. Torino, Italy 2023<br/>
[\[BibTeX\]](javascript:toggleVis('itcpaper13'))
[\[Abstract\]](javascript:toggleVis('abstract_13'))
[\[Download\]](https://puma2.inet.tu-berlin.de/~oliver/itc-library/itc35//itc2023-final94.pdf)
[\[BibSonomy\]]()

<div id="itcpaper13" style="display: none;" class="bibtex">
    @inproceedings{  ,
        title         = { An Outdoor Experimental Study of Many Antenna Full-Duplex Wireless },
        year          = { 2023 },
        address       = { Torino, Italy },
        author        = { Hadi Hosseini, Ahmed Almutairi, Syed Muhammad Hashir, Ehsan Aryafar, Joseph Camp },
        booktitle     = { 35th International Teletraffic Congress (ITC-35)  },
        month         = { September },
        pages         = { 1 -- 5 }
    }
</div>
<div id="abstract_13" style="display: none;" class="abstract">
    <strong>Abstract:</strong> Full-duplex (FD) wireless communication refers to a communication system in which both ends of a wireless link transmit and receive data simultaneously and on the same frequency band. One of the major challenges of FD communication is self-interference (SI), which refers to the interference caused by transmitting elements of a radio to its own receiving elements. Fully digital beamforming is a technique used to conduct beamforming and has been recently repurposed to also reduce SI. However, the cost of fully digital systems (e.g., base stations) dramatically increases with the increase in the number of antennas as these systems use a separate Tx-Rx RF chain for each antenna element. Hybrid beamforming systems use a much smaller number of RF chains to feed the same number of antennas, and hence can significantly reduce the deployment
cost. In this paper, we aim to quantify the performance gap between these two radio architectures in terms of SI cancellation and system capacity in FD multi-user MIMO setups. We first obtained over-the-air channel measurement data on two outdoor massive MIMO deployments over the course of three months. We next study two state-of-the-art transmit beamforming based FD systems for fully digital and hybrid architectures. We show that the hybrid beamforming system can achieve 80-97% of the fully digital system capacity, depending on the number of clients.
</div>
