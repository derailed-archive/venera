# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.veneralab.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is venera.
#
# the Original Developer is the Initial Developer. The Initial Developer of 
# the Original Code is Venera.
# 
# All portions of the code written by Venera are Copyright (c) 2022 Venera.
# All Rights Reserved.

from .errors import NotFound

# rollouts are separated inside of "buckets",
# only a certain amount of buckets will get the chance to do a feature.
curves = {1: 10, 2: 20, 3: 40, 4: 80, 5: 160}

rollouts = {}


def can_use_feature(guild_id: int, rollout_id: int, curve_id: int):
    f = (guild_id >> 22) % curves[curve_id]

    a = rollouts[rollout_id]

    if f not in a:
        raise NotFound()
