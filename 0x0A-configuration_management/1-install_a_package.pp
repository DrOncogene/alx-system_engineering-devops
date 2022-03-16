# installs puppet-lint version 2.5.0
package { 'puppet-lint-2.5.0':
  ensure  => 'installed',
  command => '/usr/bin/gem puppet-lint -v 2.5.0'
}
