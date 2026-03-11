# OpenMediaVault NVIDIA GPU Statistics Plugin

Real-time and historical monitoring of NVIDIA GPU metrics directly in OpenMediaVault dashboards. Monitor GPU utilization, memory, temperature, power consumption, and fan speed with automatic data collection and RRD-based historical graphs.

![Version](https://img.shields.io/badge/version-1.0-blue)
![OMV Requirement](https://img.shields.io/badge/OMV-%3E%3D7-green)
![License](https://img.shields.io/badge/license-GPL--3.0-blue)

## Features

✅ **Real-Time Metrics**
- GPU Utilization (%)
- Memory Usage (GB)
- Temperature (°C)
- Power Consumption (W)
- Fan Speed (%)

✅ **Historical Graphs**
- RRD-based data archival with daily/weekly/monthly views
- LAST, AVERAGE, and MAX statistics per metric
- Automatic data aggregation and retention

✅ **Seamless OMV Integration**
- Native dashboard widgets with role-based access control
- Real-time gauge/doughnut charts (5s refresh)
- Historical stacked area graphs (hourly aggregation)
- Collectd-based metrics collection via exec plugin

✅ **Secure & Lightweight**
- Data collection runs as unprivileged `nobody` user via Collectd
- Minimal resource footprint
- No external dependencies beyond nvidia-smi

## Requirements

- **OpenMediaVault** ≥ 7.x
- **NVIDIA GPU** with NVIDIA drivers installed
- **nvidia-smi** command-line utility
- **Collectd** (included with OMV)

## Installation

### Method 1: From GitHub Release (Recommended)

Download the latest `.deb` package from [Releases](../../releases) and install:

```bash
sudo dpkg -i openmediavault-nvidiastats_*.deb
```

### Method 2: Build From Source

```bash
git clone https://github.com/routmoute/openmediavault-nvidiastats.git
cd openmediavault-nvidiastats
dpkg-buildpackage -us -uc -b
sudo dpkg -i ../openmediavault-nvidiastats_*.deb
```

## Usage

### Dashboard Access

1. Log in to OpenMediaVault Web UI (admin user)
2. Navigate to **Diagnostics** → **Performance Statistics** → **NVIDIA GPU**
3. View real-time metrics and historical graphs

### Real-Time Metrics

The plugin provides 5 widgets with live metrics:
- **GPU Utilization**: Current GPU processing load
- **Memory Usage**: Used vs. Total GPU memory
- **Temperature**: Current GPU core temperature
- **Power**: Power consumption in watts
- **Fan Speed**: GPU fan speed percentage

### Historical Graphs

Four RRD graphs display hourly metrics:
- GPU Utilization over time
- GPU Memory usage over time
- GPU Temperature trend
- Power consumption history

Each graph includes LAST (current), AVERAGE (mean), and MAX (peak) values.

## Troubleshooting

### Metrics Not Appearing

**Symptom**: Dashboard shows no data or "N/A" values

**Check 1: NVIDIA Driver Status**
```bash
nvidia-smi
```
If this fails, install/update NVIDIA drivers:
```bash
sudo apt update
sudo apt install nvidia-driver-XXX
```

**Check 2: Collectd Exec Plugin**
```bash
sudo systemctl status collectd
sudo journalctl -u collectd -n 50
```

Look for errors like:
- `exec-nvidia-gpu: ... [NOTICE]: child keeps exiting: 0`
- Missing nvidia-smi path

**Check 3: Plugin Script Permissions**
```bash
ls -la /usr/bin/nvidia-collectd-gpu
# Should be executable
sudo chmod +x /usr/bin/nvidia-collectd-gpu
```

### Fan Speed Shows "N/A"

Some GPU models (consumer-grade) don't expose fan speed data. This is expected.

### Temperature Extremes (> 150°C or < 0°C)

Check GPU thermal paste and cooling solution. Throttled/faulty GPUs may report invalid temps.

## Known Limitations

⚠️ **Current Version (1.0)**

- **Single GPU monitoring**: Only GPU-0 is monitored. Multi-GPU systems display metrics for first GPU only.
- **No configurable thresholds**: Temperature/power limits are not user-adjustable
- **Fan speed unavailable**: Consumer GPUs may not report fan speed data

These limitations are planned for future releases. See [Issues](../../issues) for feature requests.

## Contributing

Contributions are welcome! Report bugs or request features via [GitHub Issues](../../issues).

## Changelog

### v1.0 (March 2025)
- Initial release
- Real-time GPU metrics dashboard
- Historical RRD graphs
- Collectd integration
