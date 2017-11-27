from django.core.management.base import BaseCommand, CommandError
from domains.models import Domain, Record, RecordType

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

	zone.to_file('{0}.zone'.format(domain.name))


