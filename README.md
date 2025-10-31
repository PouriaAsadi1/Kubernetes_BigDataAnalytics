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


## References

- Kubernetes official documentation: https://kubernetes.io
- kubeadm guides, CNI plugin docs (Calico/Weave), Prometheus & Grafana docs.
---
