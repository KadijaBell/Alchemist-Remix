import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import current_app

cloudinary.config(
    cloud_name=current_app.config['dit6mlemk'],
    api_key=current_app.config['487456261983376'],
    api_secret=current_app.config['qjhmiVlYjhfBGSoY8hazfH14uco']
)
