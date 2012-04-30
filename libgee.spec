%define api 0.8
%define major 0
%define gir_major 0.8

%define libname %mklibname gee %{api} %{major}
%define girname %mklibname gee-gir %{gir_major}
%define develname %mklibname -d gee 

Name:		libgee
Summary:	GObject-based collection library
Version:	0.7.2
Release:	3
License: 	LGPLv2+
Group:		System/Libraries
URL: 		http://live.gnome.org/Libgee
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/libgee/%{api}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n	%{libname}
Summary:	Collection library providing GObject-based interfaces and classes 
Group:		%{group}

%description -n	%{libname}
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{develname}
Summary:	Libraries and include files for developing with libgee
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package provides the necessary development libraries and include
files to allow you to develop with libgee.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgee-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gee-%{gir_major}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/gir-1.0/Gee-%{gir_major}.gir

