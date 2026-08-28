# SOC Procedure: Detection Rule Lifecycle & Tuning Standard

## 1. Detection Engineering Stages

```mermaid
flowchart LR
    A[Threat Intel / MITRE TTP] --> B[Drafting Rules in Staging]
    B --> C[CI/CD Validation Pipeline]
    C --> D[7-Day Tuning Phase]
    D --> E[Production Deployment]

Rule Promotion Standards

    Drafting: Rules are authored in .spl or .xml format and pushed to a non-main branch.

    CI/CD Check: .github/workflows/validate_detection_rules.yml verifies XML syntax, SPL syntax, and Python scripts.

    Staging / Tuning Period (7 Days): Rule runs against index=win_telemetry_staging to record false-positive rates.

    False Positive Threshold: If false-positive volume exceeds 3% of total triggers, refine logic using strict whitelist lookup tables before production deployment.

    Production Promotion: Merge branch to main. Rule is registered in active alert triggers and SOAR webhooks.

---