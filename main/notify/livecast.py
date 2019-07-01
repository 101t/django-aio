# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from asgiref.sync import async_to_sync, sync_to_async, AsyncToSync
from channels.layers import get_channel_layer
from main.core.utils import get_channel_group_name
from main.users.models import User

import json

channel_layer = get_channel_layer()

def send_to_broadcast(user, cmd="notify", kwargs={}):
	## Send realtime notify to all
	AsyncToSync(channel_layer.group_send)("broadcast", dict(
		type="send.all",
		text=json.dumps(dict(
			sender=user.username if user else "system",
			role=user.role if user else User.TUTOR,
			status=user.user_status if user else User.ONLINE,
			cmd=cmd,
			**kwargs,
		))
	))

def send_to_session(caller, callee, cmd="notify", kwargs={}):
	## Send realtime notify to specific callee
	session_group_name = "session_%s" % get_channel_group_name(user=callee)
	AsyncToSync(channel_layer.group_send)(session_group_name, dict(
		type="data_handller",
		data=json.dumps(dict(
			sender=caller.username if caller else "system",
			role=caller.role if caller else User.TUTOR,
			status=caller.user_status if caller else User.ONLINE,
			cmd=cmd,
			**kwargs,
		))
	))

'''
from main.notify.livecast import send_to_session
from main.users.models import User

caller = User.objects.get(pk=1)
callee = User.objects.get(pk=2)

send_to_session(caller=caller, callee=callee)

'''