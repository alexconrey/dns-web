from django.core.management.base import BaseCommand, CommandError
from domains.models import Domain, Record, RecordType

import os
import sys
import dns.rdataset
import dns.rdatatype
import dns.zone



class Command(BaseCommand):
  help = 'Updates DNS Zone files'

  def add_arguments(self, parser):
    parser.add_argument('domain', nargs='+', type=str)


  def _zone_file_header(self, file_path, domain_name, serial_number):
    with open(file_path, 'w+') as f:
      content = f.read()
      f.seek(0,0)
      f.write(serial_number + '\n' + content)
      f.close()

    return True

  def handle(self, *args, **options):
    for domain in options['domain']:
      try:
        get_domain = Domain.objects.get(name=domain)
	get_records = Record.objects.filter(domain=get_domain)
      except Domain.DoesNotExist:
        raise CommandError('Domain "%s" does not exist' % domain)
      except Record.DoesNotExist:
        raise CommandError('Records for "%s" do not exist' % domain)

      if get_domain and get_records:
        domain = get_domain


        self.stdout.write('Domain "%s"' % get_domain)
	self.stdout.write('Records for zone: \n')
	for record in get_records:
	  self.stdout.write("%s\n" % record)
	# create empty zone
	zone = dns.zone.Zone(origin=domain.name) 



	# add records
        for record in get_records:
	  if "@" not in record.name:
	    fqdn = "{0}.{1}".format(record.name, domain)
	  else:
	    fqdn = record


	  record_type = getattr(dns.rdatatype, "%s" % record.record_type) # Directly use built in rdatatypes instead of looking up against list

	  zone[fqdn] = dns.rdataset.from_text('IN', record_type, record.ttl, str(record.content))


        # Automatically increment the serial number
	old_serial_number = get_domain.serial_number 
	new_serial_number = (int(get_domain.serial_number) + 1)

	serial_number = new_serial_number

        if self._zone_file_header('conrey.us.zone'.format(domain.name), domain.name, serial_number):
	  self.stdout.write('Successful initial write')
	else:
	  self.stdout.write('Problem writing header to zone file.')



        zone.to_file('{0}.zone'.format(domain.name))


