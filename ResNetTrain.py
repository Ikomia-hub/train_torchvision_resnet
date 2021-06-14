from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNetTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        from ResNetTrain.ResNetTrain_process import ResNetTrainProcessFactory
        return ResNetTrainProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        from ResNetTrain.ResNetTrain_widget import ResNetTrainWidgetFactory
        return ResNetTrainWidgetFactory()
