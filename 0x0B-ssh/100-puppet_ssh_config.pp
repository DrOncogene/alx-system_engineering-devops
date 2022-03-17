# modify the sshd_config file
include stdlib
$config_file = '/etc/ssh/ssh_config'
file { $config_file:
  ensure => 'file',
}
file_line { 'Disable password auth':
  ensure  => 'present',
  path    => $config_file,
  line    => "    PasswordAuthentication no\n",
  require => File[$config_file],
}
file_line { 'Specify IdentityFile':
  ensure  => 'present',
  path    => $config_file,
  line    => "    IdentityFile ~/.ssh/school\n",
  require => File[$config_file],
}
