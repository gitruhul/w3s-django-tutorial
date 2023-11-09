from django.core.management.base import BaseCommand
from members.models import Member
from datetime import date


class Command(BaseCommand):
    help = "Insert data into the Member table"

    def handle(self, *args, **options):
        member1 = Member(
            firstname="Amit",
            lastname="Patel",
            phone=1234567890,
            joined_date=date(2012, 11, 9),
        )
        member2 = Member(
            firstname="Rajesh",
            lastname="Sharma",
            phone=9876543210,
            joined_date=date(2018, 9, 8),
        )
        member3 = Member(
            firstname="Priya",
            lastname="Verma",
            phone=8765432109,
            joined_date=date(2020, 3, 17),
        )
        member4 = Member(
            firstname="Anjali",
            lastname="Gupta",
            phone=7654321098,
            joined_date=date(2023, 11, 6),
        )
        member5 = Member(
            firstname="Suresh",
            lastname="Kumar",
            phone=6543210987,
            joined_date=date(2022, 5, 23),
        )
        members_list = [member1, member2, member3, member4, member5]
        for member in members_list:
            member.save()
        self.stdout.write(self.style.SUCCESS("Data inserted into the Member table."))
