---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am Yingjie Chen, an AI Researcher at Alibaba TongYi Lab. I graduated with Ph.D. degree in the school of Computer Science from <a href="https://english.pku.edu.cn/">Peking University</a> in 2024, supervised by Prof. Tao Wang and Prof. Yun Liang. Before that, I received B.S. degree from <a href="https://english.pku.edu.cn/">Peking University</a> in 2019. My research focuses on Computer Vision, Affective Computing and  AI Generative Content. At Alibaba, I'm working on generative AI models, especially cotrollable video generation.

We are now recruiting for Summer Internships, and positions for Research Interns (RI) are continuously open for applications. Welcome to contact me with your CV and research statement!
                

# 🔥 News
- *2025.01*: &nbsp;🎉 Perception-as-Control has been released.
- *2024.12*: &nbsp;🎉 Trend-Aware-Supervision has been accepted by AAAI 2024.
- *2023.10*: &nbsp;🎉 EventFormer has been accepted by BMVC 2023.
- *2023.05*: &nbsp;🎉 One paper has been accepted by SMC 2023.
- *2022.12*: &nbsp;🎉 CIS has been accepted by AAAI 2022.
- *2022.07*: &nbsp;🎉 On-Mitigating-Hard-Clusters has been accepted by ECCV 2022.
- *2022.07*: &nbsp;🎉 SupHCL has been accepted by ACM MM 2022.
- *2022.04*: &nbsp;🎉 HUMAN has been accepted by IJCAI 2022.
- *2021.07*: &nbsp;🎉 CaFGraph has been accepted by ACM MM 2021.
- *2021.07*: &nbsp;🎉 FSNet has been accepted by RA-L, 2021.
- *2021.07*: &nbsp;🎉 AUPro has been accepted by ICONIP, 2021.

# 📝 Selected Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/pubs/motion_generation.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Perception-as-Control: Fine-grained Controllable Image Animation with 3D-aware Motion Representation](https://arxiv.org/pdf/2501.05020.pdf)

**Yingjie Chen**, Yifang Men, Yuan Yao, Miaomiao Cui, Liefeng Bo

[[Project Page]](https://chen-yingjie.github.io/projects/Perception-as-Control/)
[[Paper]](https://arxiv.org/pdf/2501.05020.pdf)
[[Code]](https://github.com/chen-yingjie/Perception-as-Control)
- We introduce 3D-aware motion representation and propose an image animation framework, Perception-as-Control, to achieve fine-grained collaborative motion control. By constructing 3D-aware motion representation based on various user intentions and taking the perception results as motion control signals, Perception-as-Control can be applied to various motion-related video synthesis tasks. 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='images/pubs/trendaware_motivation_compressed.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Trend-Aware Supervision: On Learning Invariance for Semi-supervised Facial Action Unit Intensity Estimation](https://arxiv.org/pdf/2503.08078.pdf)

**Yingjie Chen**, Jiarui Zhang, Tao Wang, Yun Liang

[[Paper]](https://arxiv.org/pdf/2503.08078.pdf)
[[Code]](https://github.com/chen-yingjie/Trend_Aware_Supervision)
- We inspect the keyframe-based semi-supervised AU intensity estimation problem and identify the spurious correlation problem as the main challenge. To this end, we propose Trend-Aware Supervision to raise intra-trend and inter-trend awareness during training to learn invariant AU-specifc features. 
</div> 
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2022</div><img src='images/pubs/faceclustering_overview.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[On Mitigating Hard Clusters for Face Clustering](https://arxiv.org/pdf/2207.11895.pdf)

**Yingjie Chen**, Huasong Zhong, Chong Chen, Chen Shen, Jianqiang Huang, Tao Wang, Yun Liang, Qianru Sun

[[Paper]](https://arxiv.org/pdf/2207.11895.pdf)
[[Code]](https://github.com/echoanran/On-Mitigating-Hard-Clusters)
- We inspect face clustering problem and find existing methods failed to identify hard clusters—yielding significantly low recall for small or sparse clusters. To mitigate the issue of small clusters, we introduce NDDe based on the diffusion of neighborhood densities.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2022</div><img src='images/pubs/suphcl_motivation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Pursuing Knowledge Consistency: Supervised Hierarchical contrastive Learning for Facial Action Unit Recognition](https://dl.acm.org/doi/10.1145/3503161.3548116)

**Yingjie Chen**, Diqi Chen, Tao Wang, Yizhou Wang, Yun Liang

[[Paper]](https://dl.acm.org/doi/10.1145/3503161.3548116)
[[Code]](https://github.com/echoanran/SupHCL)
- We observe that there are three kinds of inherent relations among AUs, which can be treated as strong prior knowledge, and pursuing the consistency of such knowledge is the key to learning subject-consistent representations. To this end, we propose a supervised hierarchical contrastive learning method (SupHCL) for AU recognition to pursue knowledge consistency among different facial images and different AUs. 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2022</div><img src='images/pubs/cis_overview.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Causal Intervention for Subject-Deconfounded Facial Action Unit Recognition](https://arxiv.org/abs/2204.07935.pdf)

**Yingjie Chen**, Huasong Zhong, Chong Chen, Chen Shen, Jianqiang Huang, Tao Wang, Yun Liang, Qianru Sun

[[Paper]](https://arxiv.org/abs/2204.07935.pdf)
[[Code]](https://github.com/echoanran/CIS)
- We formulate subject variant problem in AU recognition using an AU causal diagram to explain the whys and wherefores. Based on our causal diagram, we propose a plug-in causal intervention module, CIS, which could be inserted into advanced AU recognition models for removing the effect caused by confounder Subject.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2021</div><img src='images/pubs/cafgraph_motivation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CaFGraph: Context-aware Facial Multi-graph Representation for Facial Action Unit Recognition](https://dl.acm.org/doi/abs/10.1145/3474085.3475295)

**Yingjie Chen**, Diqi Chen, Yizhou Wang, Tao Wang, Yun Liang

[[Paper]](https://dl.acm.org/doi/abs/10.1145/3474085.3475295)
[[Code]](https://github.com/echoanran/AU_detection_GCN)
- Considering that context is essential to resolve ambiguity in human visual system, modeling context within or among facial images emerges as a promising approach for AU recognition task. To this end, we propose CaFGraph, a novel context-aware facial multi-graph that can model both morphological & muscular-based region-level local context and region-level temporal context.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">RA-L, 2021</div><img src='images/pubs/fsnet_motivation.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Cross-Modal Representation Learning for Lightweight and Accurate Facial Action Unit Detection](hhttps://ieeexplore.ieee.org/document/9495228)

**Yingjie Chen**, Han Wu, Tao Wang, Yizhou Wang, Yun Liang

[[Paper]](https://ieeexplore.ieee.org/document/9495228)
[[Code]](https://github.com/echoanran/AU_detection_optical_flow)
- The dynamic process of facial muscle movement, as the core feature of AU, is yet ignored and rarely exploited by prior studies. Based on such observation, we propose Flow Supervised Module (FSM) to explicitly capture the dynamic facial movement in the form of Flow and use the learned Flow to provide supervision signals for the detection model during the training stage effectively and efficiently.
</div>
</div>

# 🎖 Honors and Awards
- UBIQuant Scholarship, PKU, 2023
- Peking University President Scholarship, 2022
- PKU Triple-A Student Pacesetter Award, 2021
- Outstanding Graduates, Beijing, 2019
- Outstanding Graduates, PKU, 2019
- Top 10 Excellent Graduation Thesis, 2019
- PKU Triple-A Student Award, 2018
- National Scholarship, 2018
- PKU Triple-A Student Award, 2017
- Scholarship of Kwang-Hua Education Foundation, 2017
- PKU Triple-A Student Award, 2016
- Scholarship of Tianchuang, 2016

# 💻 Work Experiences
- *2024.7 - Present*, AI Reasercher at Alibaba TongYi Lab. 
- *2023.7 - 2023.10*, Research Intern at Tencent.
- *2023.2 - 2023.6*, Research Intern at Apple Inc..
- *2021.5 - 2022.7*, Research Intern at Alibaba Damo Academy.
- *2020.11 - 2021.2*, Research Intern at SenseTime.
- *2018.8 - 2019.2*, Research Intern at MSRA.
