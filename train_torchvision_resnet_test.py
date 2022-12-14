import logging
from ikomia.core import task, ParamMap
from ikomia.utils.tests import run_for_test
import os
import ikomia
import yaml

logger = logging.getLogger(__name__)


def test(t, data_dict):
    logger.info("===== Test::train torchvision resnet =====")
    input_path = t.getInput(0)
    params = task.get_parameters(t)
    params["epochs"] = 1
    params["batch_size"] = 2
    task.set_parameters(t, params)
    input_path.setPath(data_dict["datasets"]["classification"]["dataset_classification"])
    yield run_for_test(t)
