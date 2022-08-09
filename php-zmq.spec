#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-zmq
Version  : ee5fbc693f07b2d6f0d9fd748f131be82310f386
Release  : 9
URL      : https://github.com/zeromq/php-zmq/archive/ee5fbc693f07b2d6f0d9fd748f131be82310f386.tar.gz
Source0  : https://github.com/zeromq/php-zmq/archive/ee5fbc693f07b2d6f0d9fd748f131be82310f386.tar.gz
Summary  : PHP 0MQ/zmq/zeromq extension
Group    : Development/Tools
License  : BSD-3-Clause MPL-2.0
Requires: php-zmq-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pkgconfig(libzmq)

%description
PHP extension for the 0MQ/zmq/zeromq messaging system

%package lib
Summary: lib components for the php-zmq package.
Group: Libraries

%description lib
lib components for the php-zmq package.


%prep
%setup -q -n php-zmq-ee5fbc693f07b2d6f0d9fd748f131be82310f386
cd %{_builddir}/php-zmq-ee5fbc693f07b2d6f0d9fd748f131be82310f386

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/zmq.so
