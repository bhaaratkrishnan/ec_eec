from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

imagekit = ImageKit(
    public_key="public_4O2OleYVghHj861c0wPGwT6LpQE=",
    private_key="private_hfnhATU3QVvaJtFza/0FLxHp3Iw=",
    url_endpoint="https://ik.imagekit.io/energyclubeec",
)

image_base_url = "https://ik.imagekit.io/energyclubeec"
image_options = UploadFileRequestOptions(
    folder="/eec/",
    is_private_file=False,
    use_unique_file_name=False,
)

# result = imagekit.upload_file(file=)
