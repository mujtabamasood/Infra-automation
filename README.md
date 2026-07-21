[README.md](https://github.com/user-attachments/files/30208756/README.md)
# infra-automation-examples

Small, sanitized examples of infrastructure automation, provisioning, CI/CD, and reliability tooling.

## Contents
| Folder / File | What's inside |
|---------------|---------------|
| `terraform/`  | AWS VPC + EC2 provisioning (infrastructure-as-code) |
| `ansible/`    | Base server config + hardening playbook |
| `scripts/`    | Python health-check tool and Bash backup/retention script |
| `kubernetes/` | Sample Deployment + Service with health probes |
| `helm/webapp/`| Helm chart (Chart.yaml, values, deployment/service templates) |
| `monitoring/` | Minimal Prometheus scrape config |
| `grafana/`    | Service-health dashboard (JSON) |
| `.gitlab-ci.yml` | GitLab CI/CD pipeline (lint -> test -> build -> deploy) |
| `.github/workflows/ci.yml` | GitHub Actions workflow (lint, test, terraform validate) |
| `Dockerfile`  | Minimal image for the demo tool |

> Generic demo examples only - no secrets, credentials, or proprietary code.
