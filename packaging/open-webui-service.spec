Name:           open-webui
Version:        1.0.0
Release:        1%{?dist}
Summary:        Unified Open WebUI interface with backend service integration

License:        MIT
URL:            https://github.com/open-webui/open-webui
Source0:        %{name}-%{version}.tar.gz
Source1:        open-webui-service.tar.gz

BuildArch:      noarch

Requires:       nodejs >= 14.0
Requires:       systemd
Requires:       python-3.11 
Requires:       ffmpeg

%description
Open WebUI combines a self-hosted, extensible frontend UI with a backend service for API interaction. This package integrates both the frontend from Open WebUI and backend service from Open WebUI Service.

%prep
%setup -q -a 1

# Setup backend service
pushd open-webui-service
npm install --production
popd

# Setup frontend
npm install --production
npm run build

%build
# No additional build steps required.

%install
# Install frontend application
mkdir -p %{buildroot}/usr/share/%{name}/frontend
cp -r dist/* %{buildroot}/usr/share/%{name}/frontend/

# Install backend service
mkdir -p %{buildroot}/usr/share/%{name}/backend
cp -r open-webui-service/* %{buildroot}/usr/share/%{name}/backend/

# Install the systemd service file for backend
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{_sourcedir}/open-webui-backend.service %{buildroot}/usr/lib/systemd/system/

%post
# Reload systemd to include the new services
%systemd_post open-webui-backend.service

%preun
# Stop the services during uninstallation
%systemd_preun open-webui-backend.service

%postun
# Cleanup after uninstallation
%systemd_postun_with_restart open-webui-backend.service

%files
%license LICENSE
%doc README.md
/usr/share/%{name}/frontend
/usr/share/%{name}/backend
/usr/lib/systemd/system/open-webui-backend.service

%changelog
* Sat Nov 30 2024 Seu Nome <seu.email@exemplo.com> - 1.0.0-1
- Unified Open WebUI with backend service support
