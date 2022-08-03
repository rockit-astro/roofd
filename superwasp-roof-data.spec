Name:      superwasp-roof-data
Version:   20220803
Release:   0
Url:       https://github.com/warwick-one-metre/roofd
Summary:   Roof configuration for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/roofd

%{__install} %{_sourcedir}/10-superwasp-roof.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/roofd

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/roofd/superwasp.json
%{_udevrulesdir}/10-superwasp-roof.rules

%changelog
