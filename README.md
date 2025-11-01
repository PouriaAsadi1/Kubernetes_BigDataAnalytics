# Kubernetes Cluster Analysis 

This repository contains our investigation and experiments on Kubernetes, an open-source container orchestration system that automates deployment, scaling, and management of containerized applications. The project explores how Kubernetes achieves scalability, resource efficiency, and fault tolerance by examining core architectural components and running hands-on experiments on a small cluster of virtual machines.

## Background

Kubernetes is widely used in cloud-native and distributed systems. Understanding its design and runtime behavior helps teams build resilient, scalable applications and operate production-grade clusters. This project focuses on both theoretical analysis and practical experimentation to reveal how Kubernetes manages resources, balances workloads, and recovers from failures.

## Project Goals

- Explain key Kubernetes concepts and architecture.
- Study and demonstrate:
  - Cluster formation and node communication
  - Horizontal scaling of workloads (scale up / scale down)
  - Resource allocation and scheduling behavior (CPU/memory requests & limits)
- Deploy experiments on a virtual machine hosted on a single physical machine and observe the cluster behavior.
- Collect and visualize runtime metrics to draw conclusions about system behavior under varying loads.

## Experimental Setup

- Host: single physical machine running a desktop/server OS. 
- Virtualization: virtual machines (VMs) created on the host.
- Tooling: kubectl, kubeadm, ssh access to VMs, and a load generator. 

## Comparison/Analysis

We will be running some sample data analysis on the 2013 Taxi Data. The result from the data will be provided in the repo. We will also be comparing and contrasting the Kubernetes cluster and a Google Cloud Dataproc cluster by looking at metrics such as cost, execution time, ease of use, etc.

## References

- Kubernetes official documentation: https://kubernetes.io
- kubeadm guides, CNI plugin docs (Calico/Weave), Prometheus & Grafana docs.
---
