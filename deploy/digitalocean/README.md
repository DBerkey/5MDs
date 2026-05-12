# DigitalOcean Droplet Deployment

This repository is configured for **DigitalOcean Droplet + systemd** deployment.

## 1) Server bootstrap

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
sudo useradd --system --create-home --home-dir /opt/5MDs 5mds || true
sudo mkdir -p /var/log/5mds
sudo chown -R 5mds:5mds /var/log/5mds
```

## 2) App install

```bash
sudo -u 5mds git clone https://github.com/DBerkey/5MDs /opt/5MDs
cd /opt/5MDs
sudo -u 5mds python3 -m venv .venv
sudo -u 5mds ./.venv/bin/pip install --upgrade pip
sudo -u 5mds ./.venv/bin/pip install -r requirements.txt
```

## 3) Environment and secrets

```bash
sudo -u 5mds cp /opt/5MDs/.env.example /opt/5MDs/.env
sudo -u 5mds mkdir -p /opt/5MDs/secrets
```

Set required secrets in `/opt/5MDs/.env`:
- `DISCORD_BOT_TOKEN`
- `MONGODB_URI`

Optional:
- `GOOGLE_SHEETS_CREDENTIALS_FILE` (path to service account JSON)
- `RAID_SHEET_NAME`
- `FLOOR_SHEET_NAME`
- `ADMIN_IDS`, `RAID_GUIDE_EDITOR_IDS`
- Daily watch channel/message IDs

If Google Sheets commands are used, put the credentials file at the path in `GOOGLE_SHEETS_CREDENTIALS_FILE`.

## 4) Install systemd unit

```bash
sudo cp /opt/5MDs/deploy/digitalocean/5mds.service /etc/systemd/system/5mds.service
sudo systemctl daemon-reload
sudo systemctl enable --now 5mds
```

## 5) Operations baseline

- Check service: `sudo systemctl status 5mds`
- Restart service: `sudo systemctl restart 5mds`
- Tail logs:
  - `sudo tail -f /var/log/5mds/bot.log`
  - `sudo tail -f /var/log/5mds/bot.err.log`
- Journal logs: `sudo journalctl -u 5mds -f`

## 6) Update flow

```bash
cd /opt/5MDs
sudo -u 5mds git pull
sudo -u 5mds ./.venv/bin/pip install -r requirements.txt
sudo systemctl restart 5mds
```

## 7) Secret rotation

1. Update values in `/opt/5MDs/.env`.
2. Replace Google credentials file if used.
3. Restart service: `sudo systemctl restart 5mds`.
