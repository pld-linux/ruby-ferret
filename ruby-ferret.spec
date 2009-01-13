Summary:	Ferret is a high-performance, full-featured text search engine library
Summary(hu.UTF-8):	Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár
Name:		ferret
Version:	0.11.6
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/28550/%{name}-%{version}.tgz
# Source0-md5:	928b6f90c61593059d8668dc70ebf337
URL:		http://rubyforge.org/projects/ferret/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ferret is a high-performance, full-featured text search engine
library.

%description -l hu.UTF-8
Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár.

%prep
%setup -q

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README lib

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TUTORIAL rdoc/*
%attr(755,root,root) %{_bindir}/ferret-browser
%{ruby_rubylibdir}
