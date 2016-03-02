%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from atomic-1.1.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name atomic

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.99
Release: 4%{?dist}
Summary: An atomic reference implementation for JRuby, Rubinius, and MRI
Group: Development/Languages
License: ASL 2.0
URL: http://github.com/ruby-concurrency/atomic
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
An atomic reference implementation for JRuby, Rubinius, and MRI.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}


%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Remove useless shebangs.
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/examples/*.rb

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/examples
%{gem_instdir}/test

%changelog
* Mon Feb 22 2016 Pavel Valena <pvalena@redhat.com> - 1.1.99-4
- Update to 1.1.99

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Vít Ondruch <vondruch@redhat.com> - 1.1.99-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Mon Nov 16 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.99-1
- Update to atomic 1.1.99.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Thu Dec 18 2014 Vít Ondruch <vondruch@redhat.com> - 1.1.16-1
- Update to atomic 1.1.16.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.9-1
- Update to atomic 1.1.9.

* Mon May 06 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.8-1
- Initial package
