# Enterprise Container & Docker Runtime Hardening Baseline

| Hardening Control | Configuration Parameter | Security Benefit |
|---|---|---|
| **Rootless Execution** | Set `USER nonroot` in Dockerfile | Prevents privilege escalation to host root if container is compromised. |
| **Read-Only Root Filesystem** | `--read-only` flag or `read_only: true` in Compose | Blocks runtime binary modification and persistent webshell drops. |
| **Drop Linux Capabilities** | `--cap-drop=ALL --cap-add=NET_BIND_SERVICE` | Strips unnecessary kernel capabilities (e.g., `CAP_SYS_ADMIN`). |
| **Resource Constraints** | `--memory="512m" --cpus="1.0"` | Mitigates resource exhaustion and cryptomining DoS attacks. |
| **No New Privileges** | `--security-opt=no-new-privileges:true` | Prevents sub-processes from acquiring setuid/setgid privileges. |

## Runtime Validation Verification
Run the following check against active containers to verify capability drop:
```bash
docker inspect --format='{{ .HostConfig.CapDrop }}' <container_id>