# Open WebUI RPM Package

**Open WebUI RPM Package** is a solution for packaging and distributing the Open WebUI application as an RPM package. This simplifies deployment on Linux systems that use RPM-based distributions like Red Hat, CentOS, Fedora, and openSUSE.

## Features

- **Simplified Deployment**: Package and distribute the Open WebUI application as a standard RPM package.
- **System Integration**: Includes service scripts for seamless integration with `systemd`.
- **Dependency Management**: Automatically handles dependencies required for running Open WebUI.
- **Customizable**: Easily modify and build RPM packages for your specific needs.

## Requirements

- RPM-based Linux distribution (e.g., Red Hat, CentOS, Fedora)
- `rpm-build` utility
- Basic knowledge of RPM packaging

## Installation

1. Download the RPM package from the [Releases](https://github.com/your-username/open-webui-rpmpackage/releases) page.

2. Install the package using the `rpm` or `dnf` command:

   ```bash
   sudo dnf install open-webui-rpmpackage-<version>.rpm

PS. Before install: 
adduser openwebui --system
su - openwebui
python3.11 -m venv myenv 
pip install open-webui
pip install sqllite   

## TODO list
   adduser openwebui --system
   su - openwebui
   python3.11 -m venv myenv 
   pip install open-webui
   pip install sqllite
