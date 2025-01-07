from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import StudentSerializer

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        data = request.body
        st = io.BytesIO(data)
        par = JSONParser().parse(st)
        id = par.get('roll_no', None)
        if id is not None:
            re_data = Student.objects.get(roll_no=id)
            serial = StudentSerializer(re_data)
            json_data = JSONRenderer().render(data=serial.data)
            return HttpResponse(json_data, content_type="application/json")
        crud_all = Student.objects.all()
        crud_serial = StudentSerializer(crud_all, many=True)
        # return JsonResponse(crud_serial.data, safe=False)
        js_dt = JSONRenderer().render(crud_serial.data)
        return HttpResponse(js_dt, content_type="application/json")

    def post(self, request, *args, **kwargs):
        js_dt = request.body
        readable = io.BytesIO(js_dt)
        post_parser = JSONParser().parse(readable)
        serialze_data = StudentSerializer(data=post_parser)
        if serialze_data.is_valid():
            serialze_data.save()
            msg = {"response":"Data inserted"}
            msg_data = JSONRenderer().render(msg)
            return HttpResponse(msg_data, content_type="application/json")
        msg_data = JSONRenderer().render(serialze_data.errors)
        return HttpResponse(msg_data, content_type="application/json")

    def put(self, request, *args, **kwargs):
        re_data = request.body
        strm = io.BytesIO(re_data)
        up_data = JSONParser().parse(strm)
        unique_id = up_data.get("roll_no")
        update = Student.objects.get(roll_no=unique_id)
        # If you want to update whole record then below changes we have to
        # but here we have to pass field that present in model.
        # remove partial parameter from the serializer object.
        # serial_update = StudentSerializer(update, data=up_data)
        serial_update = StudentSerializer(update, data=up_data, partial=True)

        if serial_update.is_valid():
            serial_update.save()
            msg = {"data":"Update"}
            # js = JSONRenderer().render(msg)
            # return HttpResponse(js, content_type="application/json")
            return JsonResponse(msg, safe=False)
        # msg_data = JSONRenderer().render(serial_update.errors)
        # return HttpResponse(msg_data, content_type="application/json")
        return JsonResponse(serial_update.errors, safe=False)
    def delete(self, request, *args, **kwargs):
        re_data = request.body
        strm = io.BytesIO(re_data)
        up_data = JSONParser().parse(strm)
        unique_id = up_data.get("roll_no")
        delete_dt = Student.objects.get(roll_no=unique_id)
        delete_dt.delete()
        msg = {"data": "Deleted"}
        return JsonResponse(msg, safe=False)
        # js = JSONRenderer().render(msg)
        # return HttpResponse(js, content_type="application/json")