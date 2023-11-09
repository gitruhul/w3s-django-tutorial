from django.core.management.base import BaseCommand
from members.models import Member


class Command(BaseCommand):
    help = "Insert data into the Member table"

    def handle(self, *args, **options):
        member1 = Member(firstname="Amit", lastname="Patel")
        member2 = Member(firstname="Rajesh", lastname="Sharma")
        member3 = Member(firstname="Priya", lastname="Verma")
        member4 = Member(firstname="Anjali", lastname="Gupta")
        member5 = Member(firstname="Suresh", lastname="Kumar")
        members_list = [member1, member2, member3, member4, member5]
        for member in members_list:
            member.save()
        self.stdout.write(self.style.SUCCESS("Data inserted into the Member table."))
