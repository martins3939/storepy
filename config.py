import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anime-greasily6-justice-bacon-skimming-chloride-repacking-greeter'
