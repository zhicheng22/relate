# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def add_default_permissions(apps, schema_editor):
    from course.models import add_default_roles_and_permissions

    Course = apps.get_model("course", "Course")  # noqa
    ParticipationRole = apps.get_model("course", "ParticipationRole")  # noqa
    ParticipationRolePermission = apps.get_model("course", "ParticipationRolePermission")  # noqa
    Participation = apps.get_model("course", "Participation")  # noqa
    ParticipationPreapproval = apps.get_model("course", "ParticipationPreapproval")  # noqa

    for course in Course.objects.all():
        add_default_roles_and_permissions(
                course,
                ParticipationRole,
                ParticipationRolePermission)

        roles = dict(
                (role.identifier, role)
                for role in ParticipationRole.objects.all())
        roles["auditor"] = roles["student"]
        roles["observer"] = roles["instructor"]

        for participation in Participation.objects.filter(course=course):
            participation.roles.set([roles[participation.role]])

        for preapp in ParticipationPreapproval.objects.filter(course=course):
            preapp.roles.set([roles[preapp.role]])


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0092_unicode_literals'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('edit_course', 'Edit course'), ('use_admin_interface', 'Use admin interface'), ('impersonate_role', 'Impersonate role'), ('set_fake_time', 'Set fake time'), ('set_pretend_facility', 'Pretend to be in facility'), ('edit_course_permissions', 'Edit course permissions'), ('view_hidden_course_page', 'View hidden course page'), ('view_calendar', 'View calendar'), ('send_instant_message', 'Send instant message'), ('access_files_for', 'Access files for'), ('edit_exam', 'Edit exam'), ('issue_exam_ticket', 'Issue exam ticket'), ('batch_issue_exam_ticket', 'Batch issue exam ticket'), ('view_flow_sessions_from_role', 'View flow sessions from role '), ('view_gradebook', 'View gradebook'), ('edit_grading_opportunity', 'Edit grading opportunity'), ('assign_grade', 'Assign grade'), ('view_grader_stats', 'View grader stats'), ('batch_import_grade', 'Batch-import grades'), ('batch_export_grade', 'Batch-export grades'), ('batch_download_submission', 'Batch-download submissions'), ('impose_flow_session_deadline', 'Impose flow session deadline'), ('batch_impose_flow_session_deadline', 'Batch-impose flow session deadline'), ('end_flow_session', 'End flow session'), ('batch_end_flow_session', 'Batch-end flow sessions'), ('regrade_flow_session', 'Regrade flow session'), ('batch_regrade_flow_session', 'Batch-regrade flow sessions'), ('recalculate_flow_session_grade', 'Recalculate flow session grade'), ('batch_recalculate_flow_session_grade', 'Batch-recalculate flow sesssion grades'), ('reopen_flow_session', 'Reopen flow session'), ('grant_exception', 'Grant exception'), ('view_analytics', 'View analytics'), ('preview_content', 'Preview content'), ('update_content', 'Update content'), ('use_markup_sandbox', 'Use markup sandbox'), ('use_page_sandbox', 'Use page sandbox'), ('test_flow', 'Test flow'), ('edit_events', 'Edit events'), ('query_participation', 'Query participation'), ('edit_participation', 'Edit participation'), ('preapprove_participation', 'Preapprove participation'), ('manage_instant_flow_requests', 'Manage instant flow requests')], max_length=200, verbose_name='Permission')),
                ('argument', models.CharField(blank=True, max_length=200, null=True, verbose_name='Argument')),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Participation', verbose_name='Participation')),
            ],
            options={
                'verbose_name': 'Participation permission',
                'verbose_name_plural': 'Participation permissionss',
            },
        ),
        migrations.CreateModel(
            name='ParticipationRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(help_text="A symbolic name for this role, used in course code. lower_case_with_underscores, no spaces. May be any string. The name 'unenrolled' is special and refers to anyone not enrolled in the course.", max_length=100, verbose_name='Role identifier')),
                ('name', models.CharField(help_text='A human-readable description of this role.', max_length=200, verbose_name='Role name')),
                ('is_default_for_new_participants', models.BooleanField(default=False, verbose_name='Is default role for new participants')),
                ('is_default_for_unenrolled', models.BooleanField(default=False, verbose_name='Is default role for unenrolled users')),
            ],
            options={
                'verbose_name': 'Participation role',
                'ordering': ('course', 'identifier'),
                'verbose_name_plural': 'Participation roles',
            },
        ),
        migrations.CreateModel(
            name='ParticipationRolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('edit_course', 'Edit course'), ('use_admin_interface', 'Use admin interface'), ('impersonate_role', 'Impersonate role'), ('set_fake_time', 'Set fake time'), ('set_pretend_facility', 'Pretend to be in facility'), ('edit_course_permissions', 'Edit course permissions'), ('view_hidden_course_page', 'View hidden course page'), ('view_calendar', 'View calendar'), ('send_instant_message', 'Send instant message'), ('access_files_for', 'Access files for'), ('edit_exam', 'Edit exam'), ('issue_exam_ticket', 'Issue exam ticket'), ('batch_issue_exam_ticket', 'Batch issue exam ticket'), ('view_flow_sessions_from_role', 'View flow sessions from role '), ('view_gradebook', 'View gradebook'), ('edit_grading_opportunity', 'Edit grading opportunity'), ('assign_grade', 'Assign grade'), ('view_grader_stats', 'View grader stats'), ('batch_import_grade', 'Batch-import grades'), ('batch_export_grade', 'Batch-export grades'), ('batch_download_submission', 'Batch-download submissions'), ('impose_flow_session_deadline', 'Impose flow session deadline'), ('batch_impose_flow_session_deadline', 'Batch-impose flow session deadline'), ('end_flow_session', 'End flow session'), ('batch_end_flow_session', 'Batch-end flow sessions'), ('regrade_flow_session', 'Regrade flow session'), ('batch_regrade_flow_session', 'Batch-regrade flow sessions'), ('recalculate_flow_session_grade', 'Recalculate flow session grade'), ('batch_recalculate_flow_session_grade', 'Batch-recalculate flow sesssion grades'), ('reopen_flow_session', 'Reopen flow session'), ('grant_exception', 'Grant exception'), ('view_analytics', 'View analytics'), ('preview_content', 'Preview content'), ('update_content', 'Update content'), ('use_markup_sandbox', 'Use markup sandbox'), ('use_page_sandbox', 'Use page sandbox'), ('test_flow', 'Test flow'), ('edit_events', 'Edit events'), ('query_participation', 'Query participation'), ('edit_participation', 'Edit participation'), ('preapprove_participation', 'Preapprove participation'), ('manage_instant_flow_requests', 'Manage instant flow requests')], max_length=200, verbose_name='Permission')),
                ('argument', models.CharField(blank=True, max_length=200, null=True, verbose_name='Argument')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.ParticipationRole', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Participation role permission',
                'verbose_name_plural': 'Participation role permissions',
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='preapproval_require_verified_inst_id',
            field=models.BooleanField(default=True, help_text='If set, students cannot get participation preapproval using institutional ID if the institutional ID they provided is not verified.', verbose_name='Prevent preapproval by institutional ID if not verified?'),
        ),
        migrations.AddField(
            model_name='participationrole',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='participation',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='participation', to='course.ParticipationRole', verbose_name='Roles'),
        ),
        migrations.AddField(
            model_name='participationpreapproval',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='_participationpreapproval_roles_+', to='course.ParticipationRole', verbose_name='Roles'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='role',
            field=models.CharField(max_length=50, verbose_name='Role (unused)'),
        ),
        migrations.AlterField(
            model_name='participationpreapproval',
            name='role',
            field=models.CharField(max_length=50, verbose_name='Role (unused)'),
        ),
        migrations.AlterUniqueTogether(
            name='participationrolepermission',
            unique_together=set([('role', 'permission', 'argument')]),
        ),
        migrations.AlterUniqueTogether(
            name='participationrole',
            unique_together=set([('course', 'identifier')]),
        ),
        migrations.AlterUniqueTogether(
            name='participationpermission',
            unique_together=set([('participation', 'permission', 'argument')]),
        ),
        migrations.RunPython(add_default_permissions),
    ]
