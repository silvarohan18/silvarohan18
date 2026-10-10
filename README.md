<!-- Header banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=200&section=header&text=Rohan%20Silva&fontSize=64&fontColor=FFFFFF&fontAlignY=38&desc=DevOps%20%26%20Infrastructure%20Engineer%20%E2%80%A2%20Predictive%20AI%20Engineering%20%40%20H2O.ai&descAlignY=60&descSize=17&animation=fadeIn" width="100%" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3000&pause=800&color=36BCF7&center=true&vCenter=true&width=820&lines=Migrating+enterprise+CI%2FCD+from+Jenkins+to+GitHub+Actions;Spot-first+CI+on+AWS+with+multi-AZ+and+On-Demand+fallback;Publishing+Driverless+AI+to+AWS%2C+GCP%2C+Azure+and+OCI+marketplaces;Building+CPU%2FGPU+CI+images+with+Packer+for+x86_64+and+ARM64;Prototyping+EKS+%2B+ARC+%2B+Karpenter+runner+platforms;DevSecOps%3A+security+as+a+pipeline%2C+not+a+checklist" alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rohan%20Silva-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rohan-silva-874abb197)
[![Instagram](https://img.shields.io/badge/Instagram-%40luukz__18-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/luukz_18/)
[![H2O.ai](https://img.shields.io/badge/H2O.ai-DevOps%20%26%20Infrastructure%20%E2%80%A2%20Predictive%20AI-FFE600?style=for-the-badge&logo=h2o.ai&logoColor=black)](https://h2o.ai)
[![H2O-3](https://img.shields.io/badge/Open%20Source-h2oai%2Fh2o--3-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/h2oai/h2o-3)
[![Location](https://img.shields.io/badge/Based%20in-Sri%20Lanka-00A86B?style=for-the-badge&logo=googlemaps&logoColor=white)](#-connect)

</div>

---

## 🧭 About

I'm the **primary DevOps and Infrastructure Engineer for the Predictive AI Engineering team at H2O.ai**
(title: Software Engineer II – DevOps), with **3+ years of experience** in cloud infrastructure, CI/CD
automation and deployment operations across multi-cloud environments. I own the cloud infrastructure,
CI/CD and release platforms behind two AI products: [**H2O-3**](https://github.com/h2oai/h2o-3), the
open-source distributed machine learning platform, and **Driverless AI**, H2O's enterprise AutoML product.

If the team's nightly tests run, a release reaches Docker Hub, Maven or a cloud marketplace, a security
scan fires, or an engineer gets a runner with the right permissions and the right GPU, that infrastructure
is mine.

Experienced in designing and optimizing CI/CD pipelines, infrastructure automation, cloud marketplace
operations, monitoring and observability, and **DevSecOps** practices across **AWS, Azure, GCP and OCI**,
with AWS as the primary platform for build and test. Passionate about building scalable, reliable and
secure cloud-native systems while continuously improving engineering efficiency, automation and
operational excellence.

I hold a **BSc in Engineering** from the **University of Ruhuna**, Sri Lanka.

---

## 🎯 What I Own

<table>
<tr>
<th width="50%">🔴 Critical systems I am responsible for</th>
<th width="50%">🟢 Day-to-day platform work</th>
</tr>
<tr>
<td valign="top">

- **Release pipelines** for H2O-3 (open source and Secure builds) and for Driverless AI VM images on the AWS, GCP, Azure and OCI marketplaces
- **CI infrastructure** the whole team depends on: the EC2 runner fleet, CI AMIs, runner provisioning, networking and permissions
- **Nightly and PR test pipelines** for H2O-3 and Driverless AI, including smoke tests, regression suites and release jobs
- **Security posture of the platform**: vulnerability-scanning workflows, CVE remediation, secure release branches, OIDC-scoped IAM access
- **Cloud cost** of the team's build and test footprint: analysis, Spot strategy, right-sizing and architecture proposals

</td>
<td valign="top">

- Maintaining and improving **GitHub Actions workflows and Jenkins pipelines**, reusable workflows and composite actions
- **Failure triage** across CI, Spot capacity, marketplace publishing and security scans, with automated failure reporting
- **Infrastructure design proposals**: IAM permission changes, new subnets and AZs, runner architecture, standard images
- **Monitoring and observability** for CI and platform services with Prometheus and Grafana
- **Cost and reliability reports** with the data behind them, shared with engineering and infrastructure stakeholders
- **Cross-team coordination**: release status, blockers with cloud vendor support, technical handovers and PR reviews

</td>
</tr>
</table>

---

## 🚀 Impact Highlights

| Area | What I build and run |
|---|---|
| **CI/CD modernization** | Driving the migration of H2O-3's Jenkins pipelines to **GitHub Actions**: a PR pipeline with phased gating (fast smoke gate first, heavier suites only when it passes), nightly regression suites split by workload (JUnit per Java version, Python per interpreter, XGBoost single- and multi-node), reusable workflows that remove duplicated configuration, and parity with the legacy Jenkins nightlies. |
| **Spot-first CI & cloud cost optimization** | Moved Driverless AI smoke tests to **EC2 Spot** with automatic fallback to another Availability Zone and then to On-Demand. Measured real Spot vs. fallback usage over 30-day windows, investigated capacity shortages, placement scores, alternative instance strategies and Savings Plans, proposed additional private subnets and AZs, and **right-sized oversized runner disks by 4x**. Analysis of EC2 and Jenkins spend that identified the biggest optimization targets. |
| **Ephemeral runner fleet on AWS** | Designed and operate **just-in-time EC2 runners** for GitHub Actions: spot vs. on-demand placement based on job duration, **two-AZ capacity balancing**, **private-subnet-only** networking with NAT egress, **GitHub OIDC** to tightly scoped IAM roles, and shared **EFS** volumes for multi-GB test datasets. |
| **Next-generation CI platform** | Prototyping an **EKS + Actions Runner Controller (ARC) + Karpenter** architecture: ephemeral, dynamically provisioned runners with Spot-first scheduling and On-Demand fallback, evaluated on startup time, reliability, utilization and cost per job as the long-term replacement for static CI infrastructure. |
| **Multi-cloud marketplace releases** | Automation that builds, validates and publishes **Driverless AI VM images to the AWS, GCP, Azure and OCI marketplaces**, using **HCL2**, reusable composite actions and Terraform. Validation launches real test VMs, checks product access and runs GPU experiments before an image goes live. Consolidating four cloud-specific flows into one standardized release process. |
| **CI image engineering** | A **Packer**-based workflow that builds small, standardized CI AMIs for **CPU and GPU** workloads across **x86_64 and ARM64**, tracking current Ubuntu, CUDA and NVIDIA driver requirements, replacing large hand-maintained images. |
| **Release engineering** | The official H2O-3 release pipeline end to end: **immutable + moving Docker tags** (`X.Y.Z.N`, `latest`, `latest-security`), **signed Maven artifacts**, Conda packaging, S3 distribution, Git tag and `git describe` version hygiene, documentation to **GitHub Pages** and S3, and release re-runs that are safe to repeat. |
| **Security engineering** | H2O-3 Secure release automation, security-only maintenance branches with a defined merge-back policy, **CVE dependency upgrades**, **SBOM submission to the GitHub Dependency Graph**, nightly vulnerability scans pinned to the intended product release, and least-privilege IAM via OIDC. |
| **Observability of CI itself** | A **consolidated nightly test report** that separates infrastructure failures (Spot reclaims, runner registration) from genuine product failures, plus automated failure reporting, so engineers triage one page instead of dozens of job logs. |
| **Cost & hygiene** | Audited the artifact footprint of every pipeline, mapped producers to consumers, and set **tiered retention policies**. Branching model, PR-check automation and naming conventions that keep a multi-branch release process coherent. |

---

## 🛠️ Technical Arsenal

### ☁️ Cloud & Infrastructure
<p>
  <img src="https://skillicons.dev/icons?i=aws,gcp,azure,terraform,linux&theme=dark" />
</p>

![OCI](https://img.shields.io/badge/Oracle%20Cloud-F80000?style=flat-square&logo=oracle&logoColor=white)
![Packer](https://img.shields.io/badge/Packer%20%2F%20HCL2-02A8EF?style=flat-square&logo=packer&logoColor=white)
![OIDC](https://img.shields.io/badge/GitHub%20OIDC%20%E2%86%92%20IAM-000000?style=flat-square&logo=openid&logoColor=white)
![Spot](https://img.shields.io/badge/EC2%20Spot%20%2B%20Fallback-FF9900?style=flat-square&logo=amazonec2&logoColor=white)

**AWS** (EC2 & Spot, VPC, IAM / OIDC, EBS, EFS, S3, ECR, EKS) · **GCP** · **Azure** · **OCI** · **Terraform** · **Packer** · **Linux**

### 📦 Containers & Orchestration
<p>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,helm&theme=dark" />
</p>

![EKS](https://img.shields.io/badge/Amazon%20EKS-FF9900?style=flat-square&logo=amazoneks&logoColor=white)
![ARC](https://img.shields.io/badge/Actions%20Runner%20Controller-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Karpenter](https://img.shields.io/badge/Karpenter-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

**Docker** · **Kubernetes** · **Helm** · **EKS** · **ARC** · **Karpenter** · Platform-aware image builds · UBI and Chainguard base images

### ⚙️ CI/CD & Build Systems
<p>
  <img src="https://skillicons.dev/icons?i=githubactions,jenkins,gradle,git,github&theme=dark" />
</p>

**GitHub Actions** (reusable workflows, composite actions, self-hosted runners, job summaries) · **Jenkins** (declarative pipelines) · **Gradle** · **Make** · **Git**

### 🎮 GPU & Multi-Architecture
![CUDA](https://img.shields.io/badge/CUDA%20%2F%20NVIDIA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![x86](https://img.shields.io/badge/x86__64-0071C5?style=flat-square&logo=intel&logoColor=white)
![ARM](https://img.shields.io/badge/ARM64-0091BD?style=flat-square&logo=arm&logoColor=white)

GPU validation VMs · CUDA / NVIDIA driver tooling in CI images · x86_64 and ARM64 build and test targets

### 📈 Monitoring & Observability
<p>
  <img src="https://skillicons.dev/icons?i=prometheus,grafana&theme=dark" />
</p>

**Prometheus** · **Grafana** · CI job summaries and automated failure reporting

### 💻 Programming & Scripting
<p>
  <img src="https://skillicons.dev/icons?i=py,bash,groovy,java&theme=dark" />
</p>

**Python** · **Bash** · **Groovy** · **Java** (build and test tooling) · **HCL** · **YAML**

### 📬 Release & Artifact Management
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-2496ED?style=flat-square&logo=docker&logoColor=white)
![Maven](https://img.shields.io/badge/Maven%20%2F%20Nexus-C71A36?style=flat-square&logo=apachemaven&logoColor=white)
![Conda](https://img.shields.io/badge/Conda-44A833?style=flat-square&logo=anaconda&logoColor=white)
![PyPI](https://img.shields.io/badge/Python%20Wheels-3775A9?style=flat-square&logo=pypi&logoColor=white)
![S3](https://img.shields.io/badge/S3%20Distribution-569A31?style=flat-square&logo=amazons3&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=flat-square&logo=githubpages&logoColor=white)
![Marketplaces](https://img.shields.io/badge/AWS%20%7C%20GCP%20%7C%20Azure%20%7C%20OCI%20Marketplaces-5C2D91?style=flat-square)

### 🔐 Security & Compliance
![CVE](https://img.shields.io/badge/CVE%20Triage%20%26%20Remediation-D7263D?style=flat-square)
![SBOM](https://img.shields.io/badge/SBOM%20%2F%20Dependency%20Graph-6E40C9?style=flat-square&logo=github&logoColor=white)
![Scanning](https://img.shields.io/badge/Vulnerability%20Scanning%20Pipelines-FF8C00?style=flat-square)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=trivy&logoColor=white)
![DevSecOps](https://img.shields.io/badge/DevSecOps-2E7D32?style=flat-square&logo=owasp&logoColor=white)
![Signing](https://img.shields.io/badge/Signed%20Artifacts-0E7C7B?style=flat-square)
![IAM](https://img.shields.io/badge/Least--Privilege%20IAM%20via%20OIDC-4B5563?style=flat-square)

---

## 🧠 How I Work

- **Measure first.** Thirty days of real Spot usage data before a scheduling change. Cost reports with the reason behind every number.
- **Validate before merge.** Every pipeline change gets a real run on the target branch. Every published image gets a live VM and a GPU experiment.
- **Infrastructure failures are not test failures.** Reports must say which one it was.
- **Never touch the legacy pipeline by accident.** Migration work is gated so systems still in production behave exactly as before.
- **Immutable artifacts, moving pointers.** Every build is addressable forever; only the aliases move.
- **Platform over one-off fixes.** Reusable workflows, composite actions and standard images that every project can adopt.

---

## 🔭 Currently

- Completing the Jenkins → GitHub Actions migration for H2O-3 and retiring the legacy infrastructure
- Consolidating Driverless AI marketplace publishing for AWS, GCP, Azure and OCI into one standardized release process
- Prototyping the EKS + ARC + Karpenter runner platform and measuring it against the current EC2 fleet
- Shipping the Packer pipeline for CPU/GPU CI images across x86_64 and ARM64
- Driving CI cost down with Spot-first scheduling, wider AZ coverage and Savings Plans analysis

---

## 🤝 Connect

**LinkedIn:** [linkedin.com/in/rohan-silva-874abb197](https://www.linkedin.com/in/rohan-silva-874abb197)
**GitHub:** [github.com/silvarohan18](https://github.com/silvarohan18)
**Instagram:** [instagram.com/luukz_18](https://www.instagram.com/luukz_18/)
**Location:** Sri Lanka

---

<div align="center">
<sub>"If it isn't automated, it isn't done. If it isn't measured, it isn't optimized. If it isn't reproducible, it isn't shipped."</sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=100&section=footer" width="100%" />
