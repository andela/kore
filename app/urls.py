from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from app import viewsets

router = routers.DefaultRouter()

router.register(r'org', viewsets.OrgSignUpViewSet, 'org')
router.register(r'user', viewsets.UserSignUpViewSet, 'user')
router.register(r'member', viewsets.MemberViewSet, 'member')
router.register(r'project', viewsets.ProjectViewSet, 'project')
router.register(r'team', viewsets.TeamMemberViewSet)
router.register(r'story', viewsets.StoriesViewSet, 'story')
router.register(r'task', viewsets.TaskViewSet, 'task')
router.register(r'orginvite', viewsets.OrgInvitesViewset)
router.register(r'personal', viewsets.PersonalProjectViewSet, 'personal')
router.register(r'orgprojects', viewsets.OrgProjectViewSet, 'orgprojects')
router.register(r'otherprojects', viewsets.OtherProjectViewSet, 'otherprojects')
router.register(
	r'project-invites',
	viewsets.ProjectInviteViewSet,
	'project-invites'
)
router.register(
	r'org-admin-associations',
	viewsets.OrgAdminAssociationViewSet,
	'org-admin-associations'
)
router.register(
	r'org-associations',
	viewsets.OrgAssociationViewSet,
	'org-associations'
)

urlpatterns = [
	url(r'^', include(router.urls)),
]

urlpatterns += [
	url(r'^api-auth/', include(
		'rest_framework.urls',
		namespace='rest_framework')
	),
	url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),

]
