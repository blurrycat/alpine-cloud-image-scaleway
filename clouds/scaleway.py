from .interfaces.adapter import CloudAdapterInterface


class ScalewayAdapter(CloudAdapterInterface):
    def get_latest_imported_tags(self, project, image_key):
        return None

    def import_image(self, ic):
        pass

    def delete_image(self, config, image_id):
        pass

    def publish_image(self, ic):
        pass


def register(cloud, cred_provider=None):
    return ScalewayAdapter(cloud, cred_provider)
