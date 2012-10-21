%define version 0.6
%define targetdir mongodb-mongo-c-driver-013fe75

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Name:		mongo-c-driver	
Version:	%{version}
Release:	1%{?dist}
Summary:	C Driver for MongoDB.
Group:		Development/Libraries
License:	ASL 2.0
URL:		https://github.com/mongodb/mongo-c-driver
Source0:	https://github.com/mongodb/mongo-c-driver/tarball/v0.6/mongodb-mongo-c-driver-v0.6-0-g013fe75.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-sphinx10, doxygen
Packager:	Jesse Gonzalez <jesse.gonzalez@rackspace.com>

%description 
This is then 10gen-supported MongoDB C driver. There are two goals for this driver. The first is to provide a strict, default compilation option for ultimate portability, no dependencies, and generic embeddability.

The second is to support more advanced, platform-specific features, like socket timeout, by providing an interface for platform-specific modules.

Until the 1.0 release, this driver should be considered alpha. Keep in mind that the API will be in flux until then.

%package devel
Summary:	C Driver for MongoDB.
%description devel
This is then 10gen-supported MongoDB C driver. There are two goals for this driver. The first is to provide a strict, default compilation option for ultimate portability, no dependencies, and generic embeddability.

The second is to support more advanced, platform-specific features, like socket timeout, by providing an interface for platform-specific modules.

Until the 1.0 release, this driver should be considered alpha. Keep in mind that the API will be in flux until then.

%prep
%setup -q -n %{targetdir}

%build
make %{?_smp_mflags}
make docs

%install
rm -rf %{buildroot}
make INSTALL_INCLUDE_PATH=%{buildroot}%{_includedir} INSTALL_LIBRARY_PATH=%{buildroot}%{_libdir} install

%clean
rm -rf %{buildroot}
rm -rf %{builddir}

%files
%defattr(-,root,root,-)
%doc README.md HISTORY.md APACHE-2.0.txt docs/html 
%{_libdir}

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
* Sun Oct 21 2012 Jesse Gonzalez <jesse.gonzalez@rackspace.com> - 0.6-1
Initial packaging of mongo-c-driver.
