# &nbsp; Architecture Overview

## Vision

The goal is to build a **Multi-Agent DevOps Architect** that blends:

* Reinforcement Learning
* DevOps automation
* MLOps tracking

## Agents

1. **Planner Agent** → Creates workflow plan
2. **IaC Generator Agent** → Produces Terraform/Docker configs
3. **CI/CD Agent** → Runs pipelines
4. **Monitor Agent** → Observes system
5. **Optimizer Agent** → RL-based optimization

## Tech Decisions

* **Python** for core logic
* **Docker** for isolation
* **Terraform** for IaC
* **GitHub Actions** for CI/CD

**DVC + MLflow** for tracking
