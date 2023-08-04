import logging
from ikomia.utils.tests import run_for_test

logger = logging.getLogger(__name__)


def test(t, data_dict):
    logger.info("===== Test::train torchvision resnet =====")
    input_path = t.get_input(0)
    params = t.get_param_object()
    params["epochs"] = 1
    params["batch_size"] = 2
    t.set_parameters(params)
    input_path.setPath(data_dict["datasets"]["classification"]["dataset_classification"])
    yield run_for_test(t)
