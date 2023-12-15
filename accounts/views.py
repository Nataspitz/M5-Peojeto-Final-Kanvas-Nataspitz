from rest_framework.generics import CreateAPIView
from accounts.models import Account
from accounts.serializer import AccountSerializer


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
