from django.core.management.base import BaseCommand, CommandError
from domains.models import Domain, Record, RecordType

from django.template import Context, Template, loader

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
    for domain_list in options['domain']:
      try:
        domain = Domain.objects.get(name=domain_list)
	get_records = Record.objects.filter(domain=domain)
      except Domain.DoesNotExist:
        raise CommandError('Domain "%s" does not exist' % domain)
      except Record.DoesNotExist:
        raise CommandError('Records for "%s" do not exist' % domain)

      if domain and get_records:
        self.stdout.write('Domain "%s"' % domain)
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


	zone_template = loader.get_template('bind/template.zone')
#	zone_text = zone.to_text('{0}.zone'.format(domain.name))
	zone_text = zone.to_text()

	context = {"domain": domain, "records": zone_text}

	fp = "{0}.zone".format(domain.name)
	with open(fp, 'w+') as f:
	  f.seek(0)
	  f.write(zone_template.render(context))




