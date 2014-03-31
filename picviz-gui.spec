Name:		picviz-gui
Version:	0.7
Release:	2
Summary:	Graphical frontend for picviz
License:	GPLv3+
Group:		Graphics
Url:		http://www.wallinfire.net/picviz
Source0:	http://www.wallinfire.net/files/picviz/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	picviz-cli
Requires:	python-qt4
BuildArch:	noarch

%description
Graphical frontend for picviz.

%files
%doc COPYING README samples
%{_bindir}/picviz-gui
%{_datadir}/picviz-gui
%{python_sitelib}/PicvizGui
%{python_sitelib}/picviz_gui*.egg-info

#----------------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}


