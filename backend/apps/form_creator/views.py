import json

from rest_framework.views import APIView

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from apps.form_creator.models import Form
from apps.form_creator.serializers import FormSerializer

from django.http import Http404

class FormCreatorViewSet(APIView):
    queryset = Form.objects.all()
    permission_classes = []

    def get_object(self, pk):
        try:
            return Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        form = json.loads(request.body)
        title, fields = list(form.items())[0]
        fields_dict = {"title": title}
        for index, field in enumerate(fields):
            field['order'] = index
            field_type = field.pop('type')
            if field_type in fields_dict:
                fields_dict[field_type].append(field)
            else:
                fields_dict[field_type] = [field]
        serializer = FormSerializer(data=fields_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def get(self, request, pk):
        form = self.get_object(pk)
        return Response(FormSerializer(form).data)

    def delete(self, request, pk):
        form = self.get_object(pk)
        form_data = FormSerializer(form).data
        form.delete()
        return Response(form_data, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        self.delete(request, pk)
        return self.post(request, pk)
