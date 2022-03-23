# configure a custom http response header
include stdlib
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

exec { 'install nginx':
  command => '/usr/bin/apt-get -y install nginx',
  require => Exec['apt-get update'],
}

exec { 'allow traffic':
  command => "/usr/sbin/ufw allow 'Nginx HTTP'",
  require => Exec['install nginx'],
}

exec { 'enable firewall':
  command => '/usr/sbin/ufw enable',
  require => Exec['allow traffic'],
}

exec { 'start nginx':
  command => '/usr/sbin/service nginx start',
  require => Exec['install nginx'],
}

file { 'nginx config file':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  require => Exec['install nginx'],
}

exec { 'custom response header':
  command => 'sed -i -r "s|^(\s+)(location / \{)|\1\2\n\1\1add_header X-Served-By $HOSTNAME always\;\n|g" /etc/nginx/sites-available/default',
  require => File['nginx config file'],
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
