# cards/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
    ),
    path(
        "archive",
        views.ArchivedCardListView.as_view(),
        name="archive"
    ),
    path(
        "delete/<int:pk>",
        views.CardDeleteView.as_view(),
        name="card-delete"     
    ),
    path(
        "archive-card/<int:pk>",
        views.CardArchiveView.as_view(),
        name="card-archive"
    ),
    path(
        "restore-card/<int:pk>",
        views.CardRestoreView.as_view(),
        name="card-restore"
    ),
]