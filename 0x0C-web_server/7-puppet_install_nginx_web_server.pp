# installs nginx web server and configure a 301 redirect at /redirect_me
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

file { 'write index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file { 'nginx config file':
  ensure  => 'file'
  path    => '/etc/nginx/sites-available/default',
  require => Exec['install nginx'],
}

file_line { 'configure redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  line    => "rewrite ^/redirect_me$ https://google.com permanent;\n# SSL configuration"
  match   => "^\s+# SSL configuration",
  require => File['nginx config file'],
}

exec { 'reload nginx':
  command => '/usr/sbin/service nginx reload',
}
