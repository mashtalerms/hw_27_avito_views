import os

BASE_DIR = os.path.dirname(os.path.relpath(__file__))


class Config:
    DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'datasets')
