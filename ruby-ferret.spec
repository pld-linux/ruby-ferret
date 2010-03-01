%define pkgname ferret
Summary:	Ferret - a high-performance, full-featured text search engine library
Summary(hu.UTF-8):	Ferret egy gyors, szolgáltatás-gazdag szövegkereső könyvtár
Summary(pl.UTF-8):	Ferret - biblioteka wysokowydajnego silnika wyszukiwania pełnotekstowego
Name:		ruby-%{pkgname}
Version:	0.11.6
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/28550/%{pkgname}-%{version}.tgz
# Source0-md5:	928b6f90c61593059d8668dc70ebf337
URL:		http://rubyforge.org/projects/ferret/
BuildRequires:	rpmbuild(macros) >= 1.484
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
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n ferret-%{version}

%{__sed} -i -e 's|/usr/bin/env ruby|%{__ruby}|' bin/ferret-browser

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc -S --main lib
rm -r ri/{Date,DateTime,Float,Integer,String,Time,WEBrick}
rm ri/created.rid

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
%{ruby_rubylibdir}/ferret.rb
%{ruby_rubylibdir}/ferret_version.rb
%{ruby_rubylibdir}/ferret
%attr(755,root,root) %{ruby_archdir}/ferret_ext.so

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Ferret
