from ikomia import core, dataprocess
from ikomia.dnn import dnntrain
import os
import copy
# Your imports below
from ResNetTrain.ResNet import Resnet


# --------------------
# - Class to handle the process parameters
# - Inherits core.CProtocolTaskParam from Ikomia API
# --------------------
class ResNetTrainParam(dnntrain.TrainParam):

    def __init__(self):
        dnntrain.TrainParam.__init__(self)
        # Place default value initialization here
        self.cfg["model_name"] = 'resnet18'
        self.cfg["batch_size"] = 8
        self.cfg["classes"] = 2
        self.cfg["epochs"] = 15
        self.cfg["learning_rate"] = 0.001
        self.cfg["momentum"] = 0.9
        self.cfg["input_size"] = 224
        self.cfg["num_workers"] = 0
        self.cfg["use_pretrained"] = True
        self.cfg["feature_extract"] = True
        self.cfg["export_pth"] = True
        self.cfg["export_onnx"] = False
        self.cfg["output_folder"] = os.path.dirname(os.path.realpath(__file__)) + "/models/"


# --------------------
# - Class which implements the process
# - Inherits core.CProtocolTask or derived from Ikomia API
# --------------------
class ResNetTrainProcess(dnntrain.TrainProcess):

    def __init__(self, name, param):
        dnntrain.TrainProcess.__init__(self, name, param)
        # Add input/output of the process here
        self.addInput(dataprocess.CPathIO(core.IODataType.FOLDER_PATH))

        # Create parameters class
        if param is None:
            self.setParam(ResNetTrainParam())
        else:
            self.setParam(copy.deepcopy(param))

        self.resnet = Resnet(self.getParam())
        self.enableTensorboard(False)

    def getProgressSteps(self, eltCount=1):
        # Function returning the number of progress steps for this process
        # This is handled by the main progress bar of Ikomia application
        param = self.getParam()
        if param is not None:
            return param.cfg["epochs"]
        else:
            return 1

    def run(self):
        # Core function of your process
        # Call beginTaskRun for initialization
        self.beginTaskRun()

        # Get dataset path from input
        path_input = self.getInput(0)

        print("Starting training job...")
        self.resnet.launch(path_input.getPath(), self.on_epoch_end)

        print("Training job finished.")

        # Call endTaskRun to finalize process
        self.endTaskRun()

    def on_epoch_end(self, metrics):
        # Step progress bar:
        self.emitStepProgress()
        # Log metrics
        self.log_metrics(metrics)

    def stop(self):
        super().stop()
        self.resnet.stop()


# --------------------
# - Factory class to build process object
# - Inherits dataprocess.CProcessFactory from Ikomia API
# --------------------
class ResNetTrainProcessFactory(dataprocess.CTaskFactory):

    def __init__(self):
        dataprocess.CTaskFactory.__init__(self)
        # Set process information as string here
        self.info.name = "ResNet Train"
        self.info.shortDescription = "Training process for ResNet convolutional network."
        self.info.description = "Training process for ResNet convolutional network. It requires a specific dataset " \
                                "structure based on folder names. It follows the PyTorch torchvision convention. " \
                                "The process enables to train ResNet network from scratch or for transfer learning. " \
                                "One could train the full network from pre-trained weights or keep extracted features " \
                                "and re-train only the classification layer."
        self.info.authors = "Ikomia team"
        self.info.version = "1.2.0"
        self.info.year = 2020
        self.info.license = "MIT License"
        self.info.repo = "https://github.com/Ikomia-dev"
        # relative path -> as displayed in Ikomia application process tree
        self.info.path = "Plugins/Python/Train"
        self.info.iconPath = "icons/pytorch-logo.png"
        self.info.keywords = "ResNet,classification,train"

    def create(self, param=None):
        # Create process object
        return ResNetTrainProcess(self.info.name, param)
