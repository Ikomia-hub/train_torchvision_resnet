from ikomia import dataprocess
import ResNetTrain_process as processMod
import ResNetTrain_widget as widgetMod


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNetTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return processMod.ResNetTrainProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return widgetMod.ResNetTrainWidgetFactory()
