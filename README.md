<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=190&section=header&text=Rohan%20Silva&fontSize=62&fontColor=FFFFFF&fontAlignY=38&desc=DevOps%20and%20Infrastructure%20Engineer%20%E2%80%A2%20Predictive%20AI%20Engineering%20%40%20H2O.ai&descAlignY=60&descSize=17&animation=fadeIn" width="100%" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=3000&pause=800&color=36BCF7&center=true&vCenter=true&width=880&lines=Owning+CI%2FCD%2C+releases+and+cloud+infrastructure+for+H2O-3+Secure;Migrating+Jenkins+%E2%86%92+GitHub+Actions+onto+a+Spot-first+AWS+runner+fleet;Shipping+Driverless+AI+to+the+AWS%2C+GCP%2C+Azure+and+OCI+marketplaces;Automating+CVE+and+security+scanning+for+H2O-3+and+Driverless+AI;Cutting+cloud+spend+with+Spot%2C+Cloud+Custodian+and+right-sized+runners" alt="Typing SVG" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rohan%20Silva-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rohan-silva-874abb197)
[![Instagram](https://img.shields.io/badge/Instagram-%40luukz__18-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/luukz_18/)
[![H2O.ai](https://img.shields.io/badge/H2O.ai-DevOps%20%26%20Infrastructure%20%E2%80%A2%20Predictive%20AI-FFE600?style=for-the-badge&logoColor=black)](https://h2o.ai)
![Location](https://img.shields.io/badge/Based%20in-Sri%20Lanka-00A86B?style=for-the-badge&logo=googlemaps&logoColor=white)

</div>

<br/>

## 🧭 About

**Primary DevOps and Infrastructure Engineer for the Predictive AI Engineering team at H2O.ai** (Software Engineer II – DevOps), with 3+ years in cloud infrastructure, CI/CD and release automation across **AWS, GCP, Azure and OCI**. I own the pipelines and infrastructure behind **H2O-3**, the open-source distributed ML platform, and **Driverless AI**, H2O's enterprise AutoML product: if the nightly tests run, a release ships, a security scan fires or a runner spins up with the right GPU and permissions, that is my work. BSc in Engineering, University of Ruhuna.

<br/>

## 🚀 What I've Delivered

<table>
<tr>
<td width="50%" valign="top">

### ⚙️ H2O-3 CI/CD: Jenkins → GitHub Actions
Moved the nightly regression suites, the phased PR pipeline, benchmarks and release jobs to GitHub Actions on <b>self-hosted EC2 runners</b> across two availability zones with Spot/On-Demand placement by job duration. Full parity with the legacy Jenkins nightlies, and one <b>consolidated test report</b> that separates infrastructure failures from product failures.

</td>
<td width="50%" valign="top">

### 📦 H2O-3 Release Engineering
Nightly and on-demand releases: <b>immutable + moving Docker tags</b>, signed Maven artifacts, Conda and Python wheel verification, Hadoop assemblies, Git tag hygiene, documentation to GitHub Pages and S3, rich Slack alerts. The official <b>H2O-3 Secure</b> releases ship on it.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛡️ Security Scanning Platform
Designed and own the organization's vulnerability-scanning platform on GitHub Actions, with about 70% of its commits and 80+ merged PRs: scheduled, config-driven scans of release artifacts and container images for <b>H2O-3, H2O-3 Secure and Driverless AI</b> across every supported release line, cross-checked against a second scanner, with CVE tracking and de-duplication, prioritized alerting, AI-assisted triage, and a template that onboards a new product in minutes.

</td>
<td width="50%" valign="top">

### 🔐 Security Automation Everywhere Else
Unified <b>Trivy and Prisma</b> scanning in the Jenkins pipelines with Prometheus metrics and Grafana dashboards, automated <b>SBOM generation</b> and dependency-graph submission, an <b>automated CVE-fix workflow</b> for Driverless AI, and OIDC-based least-privilege IAM across CI.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💸 Driverless AI CI Cost Optimization
Smoke tests on <b>Spot-first runners</b> with an instance-type ladder, placement scores and automatic fallback to another AZ and then On-Demand. Authored the AWS cost-optimization roadmap for Driverless AI CI/CD and cut smoke-test runner disks 4x.

</td>
<td width="50%" valign="top">

### ☁️ Driverless AI on Four Cloud Marketplaces
Cloud-image build pipeline on GitHub Actions and standardized publishing to the <b>AWS, GCP, Azure and OCI marketplaces</b>, with NVIDIA GPU handling and live VM validation, including GPU experiments, before an image goes public.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧱 CI Images with Packer
Small <b>Packer-built CI images</b> for CPU and GPU (CUDA) workloads on x86_64 and ARM64, on current Ubuntu, replacing large hand-maintained AMIs.

</td>
<td width="50%" valign="top">

### 🧹 Cloud Governance and FinOps
<b>Cloud Custodian</b> on AWS, Azure and GCP for automated resource cleanup with production safeguards, cloud budget alerts, and EC2 and on-prem utilization monitoring on ELK and Prometheus. Next up: an <b>EKS + ARC + Karpenter</b> runner platform, measured on startup time, utilization and cost per job.

</td>
</tr>
</table>

<br/>

## 🛠️ Stack

<table align="center">
<tr>
<td align="right"><b>☁️&nbsp; Cloud</b></td>
<td><img src="https://skillicons.dev/icons?i=aws,gcp,azure,terraform&theme=dark" height="40" /></td>
</tr>
<tr>
<td align="right"><b>📦&nbsp; Containers</b></td>
<td><img src="https://skillicons.dev/icons?i=docker,kubernetes,linux&theme=dark" height="40" /></td>
</tr>
<tr>
<td align="right"><b>⚙️&nbsp; CI/CD and Build</b></td>
<td><img src="https://skillicons.dev/icons?i=githubactions,jenkins,gradle,git&theme=dark" height="40" /></td>
</tr>
<tr>
<td align="right"><b>📈&nbsp; Observability</b></td>
<td><img src="https://skillicons.dev/icons?i=prometheus,grafana&theme=dark" height="40" /></td>
</tr>
<tr>
<td align="right"><b>💻&nbsp; Scripting</b></td>
<td><img src="https://skillicons.dev/icons?i=py,bash&theme=dark" height="40" /></td>
</tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/Oracle%20Cloud-F80000?style=flat-square" />
  <img src="https://img.shields.io/badge/Packer%20%2F%20HCL2-02A8EF?style=flat-square&logo=packer&logoColor=white" />
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" />
  <img src="https://img.shields.io/badge/EKS%20%2B%20ARC%20%2B%20Karpenter-FF9900?style=flat-square&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=trivy&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma%20Cloud-00C0E8?style=flat-square&logo=paloaltonetworks&logoColor=white" />
  <img src="https://img.shields.io/badge/Cloud%20Custodian-232F3E?style=flat-square" />
  <img src="https://img.shields.io/badge/SBOM%20%2F%20CVE%20Automation-6E40C9?style=flat-square&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/CUDA%20%2F%20ARM64-76B900?style=flat-square&logo=nvidia&logoColor=white" />
  <img src="https://img.shields.io/badge/ELK-005571?style=flat-square&logo=elastic&logoColor=white" />
  <img src="https://img.shields.io/badge/Groovy-4298B8?style=flat-square&logo=apachegroovy&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20OIDC%20%E2%86%92%20IAM-000000?style=flat-square&logo=openid&logoColor=white" />
</p>

<br/>

## 📈 Activity

<div align="center">

<img src="https://streak-stats.demolab.com?user=silvarohan18&mode=weekly&theme=dark&hide_border=true&background=0F2027&ring=36BCF7&fire=36BCF7&currStreakLabel=36BCF7&sideLabels=FFFFFF&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=9CA3AF" alt="Contribution streak" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/silvarohan18/silvarohan18/output/github-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/silvarohan18/silvarohan18/output/github-snake.svg" alt="Contribution graph snake animation" width="100%" />
</picture>

</div>

<br/>

<div align="center">
<sub>"If it isn't automated, it isn't done. If it isn't measured, it isn't optimized. If it isn't reproducible, it isn't shipped."</sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=90&section=footer" width="100%" />
