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

  def handle(self, *args, **options):
    for domain in options['domain']:
      try:
        get_domain = Domain.objects.get(name=domain)
	get_records = Record.objects.filter(domain=get_domain)
      except Domain.DoesNotExist:
        raise CommandError('Domain "%s" does not exist' % get_domain)
      except Record.DoesNotExist:
        raise CommandError('Records for "%s" do not exist' % get_domain)

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
	old_serial_number = domain.serial_number 
	new_serial_number = (int(domain.serial_number) + 1)

	serial_number = new_serial_number

        self.stdout.write("%s\n" % serial_number)

        zs = str(serial_number) + "\n" + zone.to_text('{0}.zone'.format(domain.name))

	fp = "{0}.zone".format(domain.name)
	with open(fp, 'w+') as f:
	  f.seek(0)
	  f.write(zs)


	self.stdout.write("%s\n" % zs)


