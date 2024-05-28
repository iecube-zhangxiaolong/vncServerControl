import logging
import os
import subprocess
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


# Create your views here.
@require_GET
def curl(request):
    back_msg = {'res': 1, 'data': 0}
    return JsonResponse(back_msg)


@require_POST
def start_vnc(request):
    back_msg = {'res': 0, 'data': 0}
    post_params = request.POST
    vnc = post_params.get('vnc')
    listen = post_params.get('listen')
    try:
        if os.name == 'posix':
            command = ['bash', '/iecube/vncServerControl/start_vnc.sh', str(vnc), str(listen)]
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            back_msg['data'] = int(output.stdout.strip())
            back_msg['res'] = 1
        return JsonResponse(back_msg)
    except Exception as e:
        logging.error("subprocess error: " + str(e))
        return JsonResponse
    finally:
        return JsonResponse(back_msg)


@require_POST
def stop_vnc(request):
    back_msg = {'res': 0, 'data': 0}
    post_params = request.POST
    pid = post_params.get('pid')
    try:
        if os.name == 'posix':
            command = ['bash', '/iecube/vncServerControl/stop_vnc.sh', str(pid)]
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            res = int(output.stdout.strip())   # 1 : 成功杀死 0 ：没有该进程
            back_msg['data'] = res
            back_msg['res'] = 1
        return JsonResponse(back_msg)
    except Exception as e:
        logging.error("subprocess error: " + str(e))
        return JsonResponse(back_msg)
    finally:
        return JsonResponse(back_msg)


