Summary:	Ferret is a high-performance, full-featured text search engine library
Summary(hu.UTF-8):	Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár
Name:		ruby-ferret
Version:	0.11.6
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/28550/ferret-%{version}.tgz
# Source0-md5:	928b6f90c61593059d8668dc70ebf337
URL:		http://rubyforge.org/projects/ferret/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ferret is a high-performance, full-featured text search engine
library.

%description -l hu.UTF-8
Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár.

%package rdoc
Summary:	Documentation files for ferret library
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ferret library.

%prep
%setup -q -n ferret-%{version}

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup
rdoc --ri --op ri lib
rdoc --op rdoc -S --main README README lib

rm -rf ri/Date
rm -rf ri/DateTime
rm -rf ri/Float
rm -rf ri/Integer
rm -rf ri/String
rm -rf ri/Time
rm -rf ri/WEBrick
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TUTORIAL
%attr(755,root,root) %{_bindir}/ferret-browser
%{ruby_rubylibdir}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Ferret
