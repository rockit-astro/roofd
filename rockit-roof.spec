Name:      rockit-roof
Version:   %{_version}
Release:   1
Summary:   Rolling roof controller
Url:       https://github.com/rockit-astro/roofd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/roofd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/roof %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/roofd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/roofd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/roof %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/roofd/
%{__install} %{_sourcedir}/10-halfmetre-roof.rules %{buildroot}%{_udevrulesdir}

%package server
Summary:  Roof server
Group:    Unspecified
Requires: python3-rockit-roof
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/roofd
%defattr(0644,root,root,-)
%{_unitdir}/roofd@.service

%package client
Summary:  Roof client
Group:    Unspecified
Requires: python3-rockit-roof
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/roof
/etc/bash_completion.d/roof

%package data-halfmetre
Summary: Roof configuration for the 0.5m telescope
Group:   Unspecified
%description data-halfmetre

%files data-halfmetre
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-halfmetre-roof.rules
%{_sysconfdir}/roofd/halfmetre.json

%changelog
