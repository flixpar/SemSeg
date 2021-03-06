import json

from ptsemseg.loader.pascal_voc_loader import pascalVOCLoader
from ptsemseg.loader.camvid_loader import camvidLoader
from ptsemseg.loader.ade20k_loader import ADE20KLoader
from ptsemseg.loader.mit_sceneparsing_benchmark_loader import MITSceneParsingBenchmarkLoader
from ptsemseg.loader.coral_loader import CoralLoader
from ptsemseg.loader.coral_depth_loader import CoralDepthLoader
from ptsemseg.loader.mangrove_loader import MangroveLoader
from ptsemseg.loader.mangrove_rgb_loader import MangroveRGBLoader

def get_loader(name):
    """get_loader

    :param name:
    """
    return {
        'pascal': pascalVOCLoader,
        'camvid': camvidLoader,
        'ade20k': ADE20KLoader,
        'mit_sceneparsing_benchmark': MITSceneParsingBenchmarkLoader,
        'coral': CoralLoader,
        'coral_depth': CoralDepthLoader,
        'mangrove': MangroveLoader,
        'mangrove_rgb': MangroveRGBLoader
    }[name]


def get_data_path(name, config_file='config.json'):
    """get_data_path

    :param name:
    :param config_file:
    """
    data = json.load(open(config_file))
    return data[name]['data_path']
