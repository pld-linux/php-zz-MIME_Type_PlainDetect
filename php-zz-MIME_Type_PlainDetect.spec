%define		status		alpha
%define		pearname	MIME_Type_PlainDetect
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Detect the MIME type of source code files
Name:		php-zz-MIME_Type_PlainDetect
Version:	0.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://zustellzentrum.cweiske.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	44856ebc24d03df01a2fd9166fba9370
URL:		http://zustellzentrum.cweiske.de/package/MIME_Type_PlainDetect/
BuildRequires:	php-channel(zustellzentrum.cweiske.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(zustellzentrum.cweiske.de)
Requires:	php-pear
Requires:	php-pear-MIME_Type >= 1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Detect the MIME type of source code files

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/MIME/Type/PlainDetect.php
%{php_pear_dir}/data/MIME_Type_PlainDetect
