%define lib_major 2
%define libname %mklibname gee %{lib_major}
%define libnamedev %mklibname -d gee 

Name:		libgee
Summary:	GObject-based collection library
Version:	0.6.3
Release:	%mkrel 1
License: 	LGPLv2+
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz

URL: 		http://live.gnome.org/Libgee
BuildRequires:	glib2-devel >= 2.10.0
BuildRequires:	gobject-introspection-devel

%description
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n	%{libname}
Summary:	Collection library providing GObject-based interfaces and classes 
Group:		%{group}

%description -n	%{libname}
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n	%{libnamedev}
Summary:	Libraries and include files for developing with libgee
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libnamedev}
This package provides the necessary development libraries and include
files to allow you to develop with libgee.


%prep
%setup -q

%build

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%post -p /sbin/ldconfig -n %{libname}

%postun -p /sbin/ldconfig -n %{libname}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgee.so.%{lib_major}*
%_libdir/girepository-1.0/Gee-1.0.typelib

%files -n %{libnamedev}
%defattr(-, root, root)
%doc ChangeLog
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/vala/vapi/*.vapi
%_datadir/gir-1.0/Gee-1.0.gir
