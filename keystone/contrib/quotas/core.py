# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from keystone.common import controller
from keystone.common import extension
from keystone.common import wsgi


extension.register_admin_extension(
    'OS-QUOTAS', {
        'name': 'OpenStack Keystone Quotas',
        'namespace': 'http://docs.openstack.org/identity/api/ext/'
                     'OS-QUOTAS/v1.0',
        'alias': 'OS-QUOTAS',
        'updated': '2013-07-11T17:14:00-00:00',
        'description': 'OpenStack extensions to Keystone v3.0 API '
                       'enabling Administrative Operations.',
        'links': [
            {
                'rel': 'describedby',
                'type': 'text/html',
                'href': 'https://github.com/openstack/identity-api',
            }
        ]})


class ResourceV3(controller.V3Controller):

    collection_name = 'resources'
    member_name = 'resource'

    @controller.protected
    def create_resource(self, context, resource):
        pass

    @controller.protected
    def get_resource(self, context, resource_id):
        pass

    @controller.protected
    def update_resource(self, context, resource_id):
        pass

    @controller.protected
    def delete_resource(self, context, resource_id):
        pass

    @controller.protected
    def get_resource_list(self, context):
        refs = self.identity_api.list_users()
        return self.wrap_collection(context, refs)


class UserQuotaV3(controller.V3Controller):

    collection_name = 'quotas'
    member_name = 'quota'

    @controller.protected
    def create_quota(self, context, user_id, quota):
        pass

    @controller.protected
    def get_quota(self, context, user_id, quota_id):
        pass

    @controller.protected
    def update_quota(self, context, user_id, quota_id):
        pass

    @controller.protected
    def delete_quota(self, context, user_id, quota_id):
        pass

    @controller.protected
    def get_quota_list(self, context, user_id):
        pass


class ProjectQuotaV3(controller.V3Controller):

    collection_name = 'quotas'
    member_name = 'quota'

    @controller.protected
    def create_quota(self, context, project_id, quota):
        pass

    @controller.protected
    def get_quota(self, context, project_id, quota_id):
        pass

    @controller.protected
    def update_quota(self, context, project_id, quota_id):
        pass

    @controller.protected
    def delete_quota(self, context, project_id, quota_id):
        pass

    @controller.protected
    def get_quota_list(self, context, project_id):
        pass


class QuotasExtention(wsgi.ExtensionRouter):

    def add_routes(self, mapper):
        resource_controller = ResourceV3()
        user_quota_controller = UserQuotaV3()

        # resource oerations
        mapper.connect(
            '/resources',
            controller=resource_controller,
            action='create_resource',
            conditions=dict(method=['POST']))

        mapper.connect(
            '/resources/{resource_id}',
            controller=resource_controller,
            action='get_resource',
            conditions=dict(method=['GET']))

        mapper.connect(
            '/resources/{resource_id}',
            controller=resource_controller,
            action='update_resource',
            conditions=dict(method=['PATCH']))

        mapper.connect(
            '/resources/{resource_id}',
            controller=resource_controller,
            action='delete_resource',
            conditions=dict(method=['DELETE']))

        mapper.connect(
            '/resources',
            controller=resource_controller,
            action='get_resource_list',
            conditions=dict(method=['GET']))

        # user quota operations
        mapper.connect(
            '/user/{user_id}/quotas',
            controller=user_quota_controller,
            action='create_quota',
            conditions=dict(method=['POST']))

        mapper.connect(
            '/user/{user_id}/quotas/{quota_id}',
            controller=user_quota_controller,
            action='get_quota',
            conditions=dict(method=['GET']))

        mapper.connect(
            '/user/{user_id}/quotas/{quota_id}',
            controller=resource_controller,
            action='update_quota',
            conditions=dict(method=['PATCH']))

        mapper.connect(
            '/user/{user_id}/quotas/{quota_id}',
            controller=user_quota_controller,
            action='delete_quota',
            conditions=dict(method=['DELETE']))

        mapper.connect(
            '/user/{user_id}/quotas',
            controller=user_quota_controller,
            action='get_quota_list',
            conditions=dict(method=['GET']))

        # project quota operations
        mapper.connect(
            '/project/{project_id}/quotas',
            controller=project_quota_controller,
            action='create_quota',
            conditions=dict(method=['POST']))

        mapper.connect(
            '/project/{project_id}/quotas/{quota_id}',
            controller=project_quota_controller,
            action='get_quota',
            conditions=dict(method=['GET']))

        mapper.connect(
            '/project/{project_id}/quotas/{quota_id}',
            controller=resource_controller,
            action='update_quota',
            conditions=dict(method=['PATCH']))

        mapper.connect(
            '/project/{project_id}/quotas/{quota_id}',
            controller=project_quota_controller,
            action='delete_quota',
            conditions=dict(method=['DELETE']))

        mapper.connect(
            '/project/{project_id}/quotas',
            controller=project_quota_controller,
            action='get_quota_list',
            conditions=dict(method=['GET']))
