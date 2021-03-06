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
from django.db import models
from django.utils.translation import ugettext_lazy as _

from osis_common.models.auditable_model import AuditableModelAdmin, AuditableModel
from attribution.models.enums import function


class TutorApplicationAdmin(AuditableModelAdmin):
    list_display = ('tutor', 'function', 'learning_container_year', 'volume_lecturing', 'volume_pratical_exercice', 'changed')
    list_filter = ('learning_container_year__academic_year', )
    fieldsets = ((None, {'fields': ('learning_container_year', 'tutor', 'function', 'volume_lecturing', 'volume_pratical_exercice')}),)
    raw_id_fields = ('learning_container_year', 'tutor')
    search_fields = ['tutor__person__first_name', 'tutor__person__last_name', 'learning_container_year__acronym',
                     'tutor__person__global_id', 'function']
    actions = ['publish_application_to_portal']

    def publish_application_to_portal(self, request, queryset):
        from attribution.business import application_json
        global_ids = list(queryset.values_list('tutor__person__global_id', flat=True))
        return application_json.publish_to_portal(global_ids)
    publish_application_to_portal.short_description = _("publish_application_to_portal")


class TutorApplication(AuditableModel):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    changed = models.DateTimeField(null=True, auto_now=True)
    learning_container_year = models.ForeignKey('base.LearningContainerYear')
    tutor = models.ForeignKey('base.Tutor')
    function = models.CharField(max_length=35, blank=True, null=True, choices=function.FUNCTIONS, db_index=True)
    volume_lecturing = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    volume_pratical_exercice = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)

    class Meta:
        unique_together = ('learning_container_year', 'tutor', 'function')

    def __str__(self):
        return u"%s - %s" % (self.tutor, self.function)