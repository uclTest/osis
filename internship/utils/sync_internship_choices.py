##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2017 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import csv
import sys
import operator
import uuid
from internship.models.internship_choice import InternshipChoice

class InternshipChoiceSynchronizer:
    def __init__(self, choices_file):
        self.choices_file = choices_file

    def run(self):
        with open(self.choices_file, 'rt') as csvfile:
            rows = csv.reader(csvfile)
            next(rows, None)
            uuids = list(map(lambda x: x[-1], rows))
            self.sync_choices_by_uuids(uuids)

    def sync_choices_by_uuids(self, uuids):
        print("%s choices to sync..." % len(uuids))
        choices_to_destroy = InternshipChoice.objects.exclude(uuid__in=uuids).all()
        print("About to delete %s choices. This cannot be reversed. Are you sure?" % len(choices_to_destroy))
        while True:
            confirm = input('[c]continue or [x]exit: ')
            if confirm == 'c':
                print("Deleting %s out-of-sync choices..." % len(choices_to_destroy))
                choices_to_destroy.delete()
                print("Done")
                return confirm
            elif confirm == 'x':
                print("Got it! Come back when your mind is made up.")
                break
            else:
                print("Invalid Option. Please Enter a Valid Option.")
