Name:      observatory-roof-client
Version:   20220803
Release:   0
Url:       https://github.com/warwick-one-metre/roofd
Summary:   SuperWASP roof client.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-warwick-observatory-roof

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/roof %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/roof %{buildroot}/etc/bash_completion.d/roof

%files
%defattr(0755,root,root,-)
%{_bindir}/roof
/etc/bash_completion.d/roof

%changelog
