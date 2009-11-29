Summary:	Ferret - a high-performance, full-featured text search engine library
Summary(hu.UTF-8):	Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár
Summary(pl.UTF-8):	Ferret - biblioteka wysokowydajnego silnika wyszukiwania pełnotekstowego
Name:		ruby-ferret
Version:	0.11.6
Release:	1
License:	MIT
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

%description -l pl.UTF-8
Ferret to biblioteka wysokowydajnego, w pełni funkcjonalnego silnika
wyszukiwania pełnotekstowego.

%package rdoc
Summary:	Documentation files for ferret library
Summary(pl.UTF-8):	Pliki dokumentacji do biblioteki ferret
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ferret library.

%description rdoc -l pl.UTF-8
Pliki dokumentacji do biblioteki ferret.

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
%doc CHANGELOG README TODO TUTORIAL MIT-LICENSE
%attr(755,root,root) %{_bindir}/ferret-browser
%{ruby_rubylibdir}/ferret.rb
%{ruby_rubylibdir}/ferret_version.rb
%{ruby_rubylibdir}/ferret
%attr(755,root,root) %{ruby_archdir}/ferret_ext.so

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Ferret
