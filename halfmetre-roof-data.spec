Name:      halfmetre-roof-data
Version:   20230202
Release:   0
Url:       https://github.com/warwick-one-metre/roofd
Summary:   Roof configuration for the half metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/roofd

%{__install} %{_sourcedir}/10-halfmetre-roof.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/roofd

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/roofd/halfmetre.json
%{_udevrulesdir}/10-halfmetre-roof.rules

%changelog
