from djangocms_moderation.models import ModerationCollection

from .base import Component
from ..utils import get_version


class Collections(Component):
    field_name = "collections"

    def parse(self):
        collection1 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator"],
            name="Collection 1",
            workflow=self.bootstrap.workflows["wf4"],
        )
        collection1.add_version(get_version(self.bootstrap.pages["page1"]))
        collection1.add_version(get_version(self.bootstrap.pages["page2"]))

        collection2 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator2"],
            name="Collection 2",
            workflow=self.bootstrap.workflows["wf4"],
        )
        collection2.add_version(get_version(self.bootstrap.pages["page3"]))
        collection2.add_version(get_version(self.bootstrap.pages["page4"]))

        collection3 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator3"],
            name="Collection 3",
            workflow=self.bootstrap.workflows["wf4"],
        )
        collection3.add_version(get_version(self.bootstrap.pages["page5"]))

        collection4 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator"],
            name="Collection 4",
            workflow=self.bootstrap.workflows["wf4"],
        )
        collection4.add_version(get_version(self.bootstrap.pages["page6"]))


        collection5 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator2"],
            name="Collection 5",
            workflow=self.bootstrap.workflows["wf4"],
        )
        collection5.add_version(get_version(self.bootstrap.pages["page7"]))

        collection6 = ModerationCollection.objects.create(
            author=self.bootstrap.users["moderator3"],
            name="Collection 6",
            workflow=self.bootstrap.workflows["wf5"],
        )
        collection6.add_version(get_version(self.bootstrap.pages["page8"]))
