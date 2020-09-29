# Script to fix the 500 internal server error of .phpp ending files

exec { 'phpchange':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
