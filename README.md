# Kubernetes Cluster Analysis 

This repository contains our investigation and experiments on Kubernetes, an open-source container orchestration system that automates deployment, scaling, and management of containerized applications. The project explores how Kubernetes achieves scalability, resource efficiency, and fault tolerance by examining core architectural components and running hands-on experiments on a small cluster of virtual machines.

## Background

Kubernetes is widely used in cloud-native and distributed systems. Understanding its design and runtime behavior helps teams build resilient, scalable applications and operate production-grade clusters. This project focuses on both theoretical analysis and practical experimentation to reveal how Kubernetes manages resources, balances workloads, and recovers from failures.

## Project Goals

- Explain key Kubernetes concepts and architecture (control plane, nodes, kubelet, kube-proxy, container runtimes, etc.).
- Study and demonstrate:
  - Cluster formation and node communication
  - Horizontal scaling of workloads (scale up / scale down)
  - Resource allocation and scheduling behavior (CPU/memory requests & limits)
  - Self-healing behaviors (pod restarts, node failures, rollout and rollback)
- Deploy experiments on 2–3 virtual machines hosted on a single physical machine and observe the cluster behavior.
- Collect and visualize runtime metrics to draw conclusions about system behavior under varying loads.

## Experimental Setup

- Host: single physical machine running a desktop/server OS (Linux recommended).
- Virtualization: 2–3 virtual machines (VMs) created on the host (VirtualBox, VMware, or libvirt).
- Kubernetes deployment approach: kubeadm (recommended for educational clusters) or a lightweight local alternative (kind, minikube) for quicker setups.
- Container runtime: containerd or Docker (depending on Kubernetes version and distribution).
- Monitoring and metrics: metrics-server, Prometheus, and Grafana (for collecting and visualizing cluster and application metrics).
- Tooling: kubectl, kubeadm, ssh access to VMs, and a load generator (hey, siege, or custom scripts).

## What We Will Measure

- Node and pod status under normal and failure scenarios.
- Scheduling decisions when requests/limits are applied.
- Autoscaling behavior when Horizontal Pod Autoscaler (HPA) is enabled.
- Rollout and rollback behavior for application updates.
- Resource usage trends (CPU, memory) and latency under load.
- Time-to-recover for pods and services during induced failures.

## Repository Structure

- docs/ — design notes, architecture diagrams, measurement plans, and literature references.
- experiments/ — reproducible experiment manifests, scripts, and results.
- infra/ — VM setup scripts, kubeadm config, and provisioners.
- monitoring/ — Prometheus and Grafana manifests, dashboards, and alerting rules.
- apps/ — sample applications (deployment manifests) used in experiments.
- reports/ — final analysis, graphs, tables, and conclusions.

(Adjust structure as the project evolves — this is a suggested organization for reproducibility.)

## Quickstart — Reproducing Our Experiments

Prerequisites:
- A host machine capable of running 2–3 VMs with at least 8GB RAM (recommended).
- Virtualization software (e.g., VirtualBox) or a cloud account.
- SSH client and basic Linux command-line skills.

High-level steps:
1. Provision 2–3 VMs using the scripts in infra/ or manually create them.
2. Install prerequisites on each VM: container runtime, kubelet, kubeadm, kubectl.
3. Initialize the control plane on one VM:
   - kubeadm init --config infra/kubeadm-config.yaml
4. Join worker VMs using the kubeadm join token produced during init.
5. Install a CNI plugin (Weave Net, Calico, Flannel) as shown in infra/cni/ manifests.
6. Deploy metrics-server, Prometheus, and Grafana from monitoring/.
7. Deploy sample application(s) from apps/ and apply scaling/test scripts from experiments/.
8. Run load generators and run the experiments outlined in experiments/plan.md.
9. Collect and visualize metrics in Grafana dashboards provided in monitoring/dashboards/.

Detailed, step-by-step commands and parameterized scripts are in infra/ and experiments/.

## Example Experiments

- Scaling test:
  - Deploy a stateless web service.
  - Use HPA to scale pods based on CPU utilization.
  - Gradually increase load and observe scaling events, pod scheduling, and node resource utilization.
- Rollout and rollback:
  - Deploy a new application image with a faulty change.
  - Observe rollout behavior, failed pod states, and perform a rollback.
  - Measure time taken to restore service and the effect on running requests.
- Node failure:
  - Simulate a node failure by shutting down a worker VM.
  - Track pod rescheduling, service availability, and recovery time.
- Resource constraint scheduling:
  - Deploy pods with varying requests/limits.
  - Observe scheduler decisions, pending pods, and eviction behavior.

Experiment manifests, measurement scripts, and raw results are stored in experiments/.

## Monitoring & Analysis

- Metrics collected:
  - Pod and node CPU/memory usage
  - Pod restarts and events
  - Scheduling latency and pod start time
  - Application-level latency and error rates
- Visualization:
  - Pre-configured Grafana dashboards in monitoring/dashboards/
  - Prometheus rules and recording rules in monitoring/prometheus/
- Reports:
  - Analysis of each experiment with charts, explanations, and takeaways are in reports/.


## Expected Outcomes

- A clear, reproducible demonstration of Kubernetes scaling, scheduling, and self-healing behaviors.
- Insights into how resource requests/limits and cluster size affect scheduling and performance.
- A set of experiment artifacts (manifests, scripts, dashboards) that can be reused for future learning or projects.

## References

- Kubernetes official documentation: https://kubernetes.io
- kubeadm guides, CNI plugin docs (Calico/Weave), Prometheus & Grafana docs.
- Research and articles about container orchestration and distributed systems (see docs/references.md).

---

If additional details are needed (detailed setup commands, cloud-specific variants, or assistance preparing VM images and automation scripts), the team can expand the infra/ and docs/ folders and add step-by-step walkthroughs.# Kubernetes_BigDataAnalytics
