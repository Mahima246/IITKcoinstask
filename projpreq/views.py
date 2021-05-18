from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
coins = {'190468':6,'190289':7,'189088':9,'189789':9}
@csrf_exempt
def get_coins(request):
    data = json.loads(request.body)
    if 'rollno' not in data:
        return JsonResponse({'error':'Invalid fields'})
    if coins.get(data['rollno'],None) == None:
        return JsonResponse({'error':'roll no does not exist '})

    res = {'coins':coins[data['rollno']]}
    print(res)
    return JsonResponse(res)
