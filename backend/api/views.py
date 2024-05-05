from .controllers.horse import horse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def horse_crud(request):
    return horse(request)
