from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def get_process_factory(self):
        # Instantiate process object
        from train_torchvision_resnet.train_torchvision_resnet_process import TrainResnetFactory
        return TrainResnetFactory()

    def get_widget_factory(self):
        # Instantiate associated widget object
        from train_torchvision_resnet.train_torchvision_resnet_widget import TrainResnetWidgetFactory
        return TrainResnetWidgetFactory()
