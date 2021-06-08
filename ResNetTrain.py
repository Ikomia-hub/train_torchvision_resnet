from ikomia import dataprocess
from ResNetTrain.ResNetTrain_process import ResNetTrainProcessFactory
from ResNetTrain.ResNetTrain_widget import ResNetTrainWidgetFactory


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNetTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return ResNetTrainProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return ResNetTrainWidgetFactory()
