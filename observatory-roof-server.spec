Name:      observatory-roof-server
Version:   20220803
Release:   0
Url:       https://github.com/warwick-one-metre/roofd
Summary:   SuperWASP roof server.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-pyserial python3-warwick-observatory-common python3-warwick-observatory-roof

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/roofd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/roofd@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/roofd
%defattr(-,root,root,-)
%{_unitdir}/roofd@.service

%changelog
