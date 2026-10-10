<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=190&section=header&text=Rohan%20Silva&fontSize=62&fontColor=FFFFFF&fontAlignY=38&desc=DevOps%20%26%20Infrastructure%20Engineer%20%E2%80%A2%20Predictive%20AI%20Engineering%20%40%20H2O.ai&descAlignY=60&descSize=17&animation=fadeIn" width="100%" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3000&pause=800&color=36BCF7&center=true&vCenter=true&width=800&lines=Owner+of+CI%2FCD%2C+release+and+cloud+infrastructure+for+H2O-3+and+Driverless+AI;Jenkins+%E2%86%92+GitHub+Actions+on+a+Spot-first+AWS+runner+fleet;Driverless+AI+images+on+AWS%2C+GCP%2C+Azure+and+OCI+marketplaces;Security+scanning%2C+SBOMs+and+CVE+automation+as+pipelines" alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rohan%20Silva-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rohan-silva-874abb197)
[![Instagram](https://img.shields.io/badge/Instagram-%40luukz__18-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/luukz_18/)
[![H2O.ai](https://img.shields.io/badge/H2O.ai-DevOps%20%26%20Infrastructure%20%E2%80%A2%20Predictive%20AI-FFE600?style=for-the-badge&logoColor=black)](https://h2o.ai)
![Location](https://img.shields.io/badge/Based%20in-Sri%20Lanka-00A86B?style=for-the-badge&logo=googlemaps&logoColor=white)

</div>

## 🧭 About

**Primary DevOps and Infrastructure Engineer for the Predictive AI Engineering team at H2O.ai** (Software Engineer II – DevOps), with 3+ years in cloud infrastructure, CI/CD and release automation across **AWS, GCP, Azure and OCI**. I own the pipelines and infrastructure behind **H2O-3**, the open-source distributed ML platform, and **Driverless AI**, H2O's enterprise AutoML product: if the nightly tests run, a release ships, a security scan fires or a runner spins up with the right GPU and permissions, that is my work. BSc in Engineering, University of Ruhuna.

## 📊 Impact in Numbers

<div align="center">

![Commits](https://img.shields.io/badge/3%2C400%2B-commits-0F2027?style=for-the-badge&labelColor=36BCF7)
![PRs](https://img.shields.io/badge/780%2B-pull%20requests%20%E2%80%A2%20670%2B%20merged-0F2027?style=for-the-badge&labelColor=36BCF7)
![Repos](https://img.shields.io/badge/118-repositories-0F2027?style=for-the-badge&labelColor=36BCF7)
![Year](https://img.shields.io/badge/2%2C600%2B-contributions%20in%20the%20last%2012%20months-0F2027?style=for-the-badge&labelColor=36BCF7)

<sub>Across the H2O.ai organization since October 2023, default branches only. Snapshot: October 2026.</sub>

</div>

## 🚀 What I've Delivered

- **H2O-3 CI/CD, Jenkins → GitHub Actions.** Migrated the nightly regression suites, the PR pipeline with phased gating, the benchmark pipeline and the release jobs to GitHub Actions on **self-hosted EC2 runners** spread across two availability zones with Spot/On-Demand placement by job duration. Reached parity with the legacy Jenkins nightlies and replaced dozens of job logs with one **consolidated test report** that separates infrastructure failures from product failures.
- **H2O-3 release engineering.** Built the nightly and on-demand release workflow: immutable + moving Docker tags, signed Maven artifacts, Conda and Python wheel verification, Hadoop assemblies, Git tag hygiene, documentation to GitHub Pages and S3, and rich Slack alerts. The official **H2O-3 Secure** releases ship on it.
- **Driverless AI CI cost optimization.** Moved smoke tests to **Spot-first runners** with an instance-type ladder, placement scores and automatic fallback to another AZ and then On-Demand. Wrote the AWS cost-optimization roadmap for Driverless AI CI/CD and cut smoke-test runner disks 4x.
- **CI images with Packer.** Replaced large hand-maintained AMIs with small Packer-built CI images for CPU and GPU (CUDA) workloads on **x86_64 and ARM64**, on current Ubuntu.
- **Driverless AI on four cloud marketplaces.** Migrated the cloud-image build pipeline to GitHub Actions and standardized publishing to the **AWS, GCP, Azure and OCI marketplaces**, with NVIDIA GPU handling and live VM validation, including GPU experiments, before an image goes public.
- **Security as a pipeline.** Unified **Trivy and Prisma** vulnerability scanning driven by YAML config, with Prometheus metrics, Grafana dashboards, CVE de-duplication and Slack alerting; automated **SBOM generation** and dependency-graph submission; an **automated CVE-fix workflow** for Driverless AI; secret-scanning alerts; OIDC-based least-privilege IAM.
- **Cloud governance and FinOps.** Deployed **Cloud Custodian** on AWS, Azure and GCP for automated resource cleanup with production safeguards, cloud budget alerts, and EC2 and on-prem machine monitoring with underutilization detection, backed by ELK and Prometheus.
- **Next-generation CI platform.** Prototyping **EKS + Actions Runner Controller + Karpenter** for ephemeral, Spot-first runners, measured on startup time, utilization and cost per job.

## 🧱 Where the Work Lands

| Area | Scope | Footprint |
|---|---|---|
| **H2O-3** | Core and Secure release repos, CI tooling, security scanner, telemetry | 2,300+ commits · 400+ merged PRs |
| **Driverless AI** | Product CI, release utilities, cloud marketplace images | 370+ commits · 85+ merged PRs |
| **Shared cloud infrastructure & security** | Security pipelines, cloud governance, monitoring, ops | 440+ commits · 70+ merged PRs |
| **Everything else** | 100+ other repositories, mostly CI/CD and security fixes | PRs and reviews across the org |

## 🛠️ Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=aws,gcp,azure,terraform,docker,kubernetes,linux&theme=dark" />
  <br/>
  <img src="https://skillicons.dev/icons?i=githubactions,jenkins,gradle,git,py,bash,prometheus,grafana&theme=dark" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Oracle%20Cloud-F80000?style=flat-square" />
  <img src="https://img.shields.io/badge/Packer%20%2F%20HCL2-02A8EF?style=flat-square&logo=packer&logoColor=white" />
  <img src="https://img.shields.io/badge/EKS%20%2B%20ARC%20%2B%20Karpenter-FF9900?style=flat-square&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=trivy&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma%20Cloud-00C0E8?style=flat-square&logo=paloaltonetworks&logoColor=white" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" />
  <img src="https://img.shields.io/badge/Groovy-4298B8?style=flat-square&logo=apachegroovy&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloud%20Custodian-232F3E?style=flat-square" />
  <img src="https://img.shields.io/badge/SBOM%20%2F%20CVE%20Automation-6E40C9?style=flat-square&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/CUDA%20%2F%20ARM64-76B900?style=flat-square&logo=nvidia&logoColor=white" />
  <img src="https://img.shields.io/badge/ELK-005571?style=flat-square&logo=elastic&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20OIDC%20%E2%86%92%20IAM-000000?style=flat-square&logo=openid&logoColor=white" />
</p>

<div align="center">
<sub>"If it isn't automated, it isn't done. If it isn't measured, it isn't optimized. If it isn't reproducible, it isn't shipped."</sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=90&section=footer" width="100%" />
