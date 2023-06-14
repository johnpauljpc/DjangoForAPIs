from rest_framework.routers import SimpleRouter
from .views import UsersViewset, PostViewset


router = SimpleRouter()
router.register('users', UsersViewset, basename="users")
router.register('', PostViewset, basename="post")

urlpatterns = router.urls