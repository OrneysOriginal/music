from django.views import View


class DataMixin(View):
    paginate_by = 25
