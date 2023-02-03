## Roof daemon

`roofd` communicates with the [SuperWASP roof controller](https://github.com/warwick-one-metre/superwasp-roof-controller) attached via USB.  Control is exposed via Pyro.

`roof` is a commandline utility that interfaces with the roof daemon.

`python3-warwick-observatory-roof` is a python module with the common roof code.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the software architecture and instructions for developing and deploying the code.

### Configuration

Configuration is read from json files that are installed by default to `/etc/roofd`.
A configuration file is specified when launching the roof server, and the `roof` frontend will search this location when launched.

```python
{
  "daemon": "halfmetre_roof", # Run the server as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
  "log_name": "halfmetre_roof", # The name to use when writing messages to the observatory log.
  "control_machines": ["HalfMetreTCS"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `warwick.observatory.common.IP`.
  "serial_port": "/dev/roof", # Serial FIFO for communicating with the roof controller
  "serial_baud": 9600, # Serial baud rate (always 9600)
  "serial_timeout": 3, # Serial comms timeout
  "open_timeout": 60, # Maximum time to wait for the roof to open
  "close_timeout": 120 # Maximum time to wait for the roof to close
}
```

The FIFO device names are defined in the .rules files installed through the `-roof-data` rpm package.
If the physical serial port or USB adaptors change these should be updated to match.

### Initial Installation

The automated packaging scripts will push 4 RPM packages to the observatory package repository:

| Package                          | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| observatory-roof-server          | Contains the `roofd` server and systemd service file.                    |
| observatory-roof-client          | Contains the `roof` commandline utility for controlling the roof server. |
| python3-warwick-observatory-roof | Contains the python module with shared code.                             |
| halfmetre-roof-data              | Contains the json configuration and udev rules for the half metre.       |

`observatory-roof-server` and `observatory-roof-client` and `halfmetre-roof-data` packages should be installed on the `halfmetre-tcs` machine.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now roofd@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `warwick.observatory.common.daemons` for the daemon specified in the roof config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart roofd@<config>
```

### Testing Locally

The roof server and client can be run directly from a git clone:
```
./roofd halfmetre.json
ROOFD_CONFIG_PATH=./halfmetre.json ./roof status
```
