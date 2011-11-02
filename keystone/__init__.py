# Copyright (C) 2011 OpenStack LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gettext


API_VERSION = "2.0"
API_VERSION_STATUS = "ALPHA"
API_VERSION_DATE = "2011-11-19T00:00:00Z"

RELEASE_VERSION = "0.9.1"
RELEASE_VERSION_FINAL = False  # becomes true at Release Candidate time


def canonical_version():
    return RELEASE_VERSION


def version():
    if RELEASE_VERSION_FINAL:
        return RELEASE_VERSION
    else:
        return '%s-dev' % (RELEASE_VERSION)


# This installs the _(...) function as a built-in so all other modules
# don't need to.
gettext.install('keystone')
