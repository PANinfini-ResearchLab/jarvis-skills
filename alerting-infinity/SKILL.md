---
name: alerting
description: Multi-channel notifications (Telegram, email, ntfy) on system events
  and threshold breaches. Use when the user asks to be warned or notified about
  anything — disk, CPU, GPU, service down, custom thresholds.
---

# Alerting — Multi-channel Notifications

## Configuration
| ALERT_CHANNELS        | telegram,email,ntfy | Active channels (comma-separated)  |
| ALERT_TELEGRAM_TOKEN  | (required if used)  | Telegram bot token                 |
| ALERT_TELEGRAM_CHAT   | (required if used)  | Telegram chat ID                   |
| ALERT_NTFY_URL        | https://ntfy.sh     | ntfy server URL                    |
| ALERT_NTFY_TOPIC      | (required if used)  | ntfy topic                         |
| ALERT_EMAIL_TO        | (required if used)  | Recipient email                    |
| ALERT_SMTP_URL        | (required if used)  | smtp://user:pass@host:port         |
| ALERT_MIN_LEVEL       | WARN                | Minimum level : INFO/WARN/CRIT     |
| ALERT_COOLDOWN        | 900                 | Seconds between duplicate alerts   |

## Alert format
[LEVEL] hostname · component — message · ISO8601

Examples :
[CRIT] myserver · disk — /var 94% used (threshold 90%) · 2026-06-09T14:02:11+02:00
[WARN] myserver · gpu:0 — temperature 82°C (threshold 80°C) · 2026-06-09T14:05:00+02:00
[OK]   myserver · disk — /var recovered 78% · 2026-06-09T14:30:00+02:00

## Send functions

### Telegram
curl -s -X POST https://api.telegram.org/bot$ALERT_TELEGRAM_TOKEN/sendMessage \
  -d chat_id=$ALERT_TELEGRAM_CHAT \
  -d text="$MESSAGE" \
  -d parse_mode=HTML

### ntfy
curl -s -X POST $ALERT_NTFY_URL/$ALERT_NTFY_TOPIC \
  -H "Title: $LEVEL alert — $COMPONENT" \
  -d "$MESSAGE"

### Email (curl SMTP)
curl -s --url "$ALERT_SMTP_URL" \
  --mail-from "$ALERT_EMAIL_FROM" \
  --mail-rcpt "$ALERT_EMAIL_TO" \
  -T <(echo -e "Subject: [$LEVEL] $COMPONENT\n\n$MESSAGE")

## Rules
1. Real values only — measure + threshold from real checks, never assumed
2. Dedup : same (component, level) within cooldown → suppress, count, append "(x N)"
3. Always send recovery : every CRIT/WARN has its [OK] when resolved
4. Log every alert to blackbox with delivery status per channel
5. Channel failure → try next channel ; all failed → local log + surface at next interaction
6. Threshold values = env vars, never hardcoded

## Common threshold checks

### Disk
USAGE=$(df $MOUNT | awk 'NR==2{print $5}' | tr -d '%')
[ "$USAGE" -gt "${DISK_THRESHOLD:-90}" ] && send_alert CRIT disk "$MOUNT ${USAGE}% used"

### CPU (1min load vs core count)
CORES=$(nproc)
LOAD=$(awk '{print $1}' /proc/loadavg | cut -d. -f1)
[ "$LOAD" -gt "$CORES" ] && send_alert WARN cpu "load ${LOAD} exceeds ${CORES} cores"

### GPU temperature (nvidia-smi)
nvidia-smi --query-gpu=index,temperature.gpu --format=csv,noheader,nounits | \
while IFS=, read idx temp; do
  [ "$temp" -gt "${GPU_TEMP_THRESHOLD:-85}" ] && \
    send_alert WARN "gpu:$idx" "temperature ${temp}C"
done

### Service down
systemctl is-active --quiet $SERVICE || send_alert CRIT service "$SERVICE is not running"
