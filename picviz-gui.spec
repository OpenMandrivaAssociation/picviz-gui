%define name picviz-gui
%define version 0.7
%define release %mkrel 1

Name: %name
Version: %version
Release: %release
Summary: Graphical frontend for picviz
License: GPLv3+
Group: Graphics
URL: http://www.wallinfire.net/picviz
Source0: http://www.wallinfire.net/files/picviz/%{name}-%{version}.tar.gz
BuildRequires: python-devel
Requires:      PyQt4
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Graphical frontend for picviz.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README samples
%{python_sitelib}/PicvizGui
%{python_sitelib}/picviz_gui*.egg-info
%{_bindir}/picviz-gui
%{_datadir}/picviz-gui


%changelog
* Mon Feb 22 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2010.1
+ Revision: 509548
- import picviz-gui


